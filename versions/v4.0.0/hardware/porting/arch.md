---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/hardware/porting/arch.html
original_path: hardware/porting/arch.html
---

# Architecture Porting Guide

An architecture port is needed to enable Zephyr to run on an ISA or an ABI that is not currently supported.

The following are examples of ISAs and ABIs that Zephyr supports:

- x86\_32 ISA with System V ABI
- ARMv7-M ISA with Thumb2 instruction set and ARM Embedded ABI (aeabi)
- ARCv2 ISA

For information on Kconfig configuration, see
[Setting Kconfig configuration values](../../build/kconfig/setting.md#setting-configuration-values). Architectures use a Kconfig configuration
scheme similar to boards.

An architecture port can be divided in several parts; most are required and
some are optional:

- **The early boot sequence**: each architecture has different steps it must
  take when the CPU comes out of reset (required).
- **Interrupt and exception handling**: each architecture handles asynchronous
  and unrequested events in a specific manner (required).
- **Thread context switching**: the Zephyr context switch is dependent on the
  ABI and each ISA has a different set of registers to save (required).
- **Thread creation and termination**: A thread’s initial stack frame is ABI
  and architecture-dependent, and thread abortion possibly as well (required).
- **Device drivers**: most often, the system clock timer and the interrupt
  controller are tied to the architecture (some required, some optional).
- **Utility libraries**: some common kernel APIs rely on a
  architecture-specific implementation for performance reasons (required).
- **CPU idling/power management**: most architectures implement instructions
  for putting the CPU to sleep (partly optional, most likely very desired).
- **Fault management**: for implementing architecture-specific debug help and
  handling of fatal error in threads (partly optional).
- **Linker scripts and toolchains**: architecture-specific details will most
  likely be needed in the build system and when linking the image (required).
- **Memory Management and Memory Mapping**: for architecture-specific details
  on supporting memory management and memory mapping.
- **Stack Objects**: for architecture-specific details on memory protection
  hardware regarding stack objects.
- **User Mode Threads**: for supporting threads in user mode.
- **GDB Stub**: for supporting GDB stub to enable remote debugging.

## Early Boot Sequence

The goal of the early boot sequence is to take the system from the state it is
after reset to a state where is can run C code and thus the common kernel
initialization sequence. Most of the time, very few steps are needed, while
some architectures require a bit more work to be performed.

Common steps for all architectures:

- Setup an initial stack.
- If running an XIP kernel, copy initialized data
  from ROM to RAM.
- If not using an ELF loader, zero the BSS section.
- Jump to `z_cstart()`, the early kernel initialization

  - `z_cstart()` is responsible for context switching out of the fake
    context running at startup into the main thread.

Some examples of architecture-specific steps that have to be taken:

- If given control in real mode on x86\_32, switch to 32-bit protected mode.
- Setup the segment registers on x86\_32 to handle boot loaders that leave them
  in an unknown or broken state.
- Initialize a board-specific watchdog on Cortex-M3/4.
- Switch stacks from MSP to PSP on Cortex-M.
- Use a different approach than calling into \_Swap() on Cortex-M to prevent
  race conditions.
- Setup FIRQ and regular IRQ handling on ARCv2.

## Interrupt and Exception Handling

Each architecture defines interrupt and exception handling differently.

When a device wants to signal the processor that there is some work to be done
on its behalf, it raises an interrupt. When a thread does an operation that is
not handled by the serial flow of the software itself, it raises an exception.
Both, interrupts and exceptions, pass control to a handler. The handler is
known as an ISR in the case of
interrupts. The handler performs the work required by the exception or the
interrupt. For interrupts, that work is device-specific. For exceptions, it
depends on the exception, but most often the core kernel itself is responsible
for providing the handler.

The kernel has to perform some work in addition to the work the handler itself
performs. For example:

- Prior to handing control to the handler:

  - Save the currently executing context.
  - Possibly getting out of power saving mode, which includes waking up
    devices.
  - Updating the kernel uptime if getting out of tickless idle mode.
- After getting control back from the handler:

  - Decide whether to perform a context switch.
  - When performing a context switch, restore the context being context
    switched in.

This work is conceptually the same across architectures, but the details are
completely different:

- The registers to save and restore.
- The processor instructions to perform the work.
- The numbering of the exceptions.
- etc.

It thus needs an architecture-specific implementation, called the
interrupt/exception stub.

Another issue is that the kernel defines the signature of ISRs as:

```c
void (*isr)(void *parameter)
```

Architectures do not have a consistent or native way of handling parameters to
an ISR. As such there are two commonly used methods for handling the
parameter.

- Using some architecture defined mechanism, the parameter value is forced in
  the stub. This is commonly found in X86-based architectures.
- The parameters to the ISR are inserted and tracked via a separate table
  requiring the architecture to discover at runtime which interrupt is
  executing. A common interrupt handler demuxer is installed for all entries of
  the real interrupt vector table, which then fetches the device’s ISR and
  parameter from the separate table. This approach is commonly used in the ARC
  and ARM architectures via the [`CONFIG_GEN_ISR_TABLES`](../../kconfig.md#CONFIG_GEN_ISR_TABLES "CONFIG_GEN_ISR_TABLES") implementation.
  You can find examples of the stubs by looking at `_interrupt_enter()` in
  x86, `_IntExit()` in ARM, `_isr_wrapper()` in ARM, or the full
  implementation description for ARC in [arch/arc/core/isr\_wrapper.S](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arc/core/isr_wrapper.S).

Each architecture also has to implement primitives for interrupt control:

- locking interrupts: [`irq_lock()`](../../doxygen/html/group__isr__apis.md#ga19fdde73c3b02fcca6cf1d1e67631228), [`irq_unlock()`](../../doxygen/html/group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57).
- registering interrupts: [`IRQ_CONNECT()`](../../doxygen/html/group__isr__apis.md#ga131739d1faf501a15590053817aba984).
- programming the priority if possible `irq_priority_set()`.
- enabling/disabling interrupts: [`irq_enable()`](../../doxygen/html/group__isr__apis.md#ga7ea700ee31e4ff036c997a554dbedfeb), [`irq_disable()`](../../doxygen/html/group__isr__apis.md#ga82c3a15d812f58e0f6525f358d031e6d).

Note

[`IRQ_CONNECT`](../../doxygen/html/group__isr__apis.md#ga131739d1faf501a15590053817aba984) is a macro that uses assembler and/or linker script
tricks to connect interrupts at build time, saving boot time and text size.

The vector table should contain a handler for each interrupt and exception that
can possibly occur. The handler can be as simple as a spinning loop. However,
we strongly suggest that handlers at least print some debug information. The
information helps figuring out what went wrong when hitting an exception that
is a fault, like divide-by-zero or invalid memory access, or an interrupt that
is not expected (*spurious interrupt*). See the ARM implementation in
[arch/arm/core/cortex\_m/fault.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/fault.c) for an example.

## Thread Context Switching

Multi-threading is the basic purpose to have a kernel at all. Zephyr supports
two types of threads: preemptible and cooperative.

Two crucial concepts when writing an architecture port are the following:

- Cooperative threads run at a higher priority than preemptible ones, and
  always preempt them.
- After handling an interrupt, if a cooperative thread was interrupted, the
  kernel always goes back to running that thread, since it is not preemptible.

A context switch can happen in several circumstances:

- When a thread executes a blocking operation, such as taking a semaphore that
  is currently unavailable.
- When a preemptible thread unblocks a thread of higher priority by releasing
  the object on which it was blocked.
- When an interrupt unblocks a thread of higher priority than the one currently
  executing, if the currently executing thread is preemptible.
- When a thread runs to completion.
- When a thread causes a fatal exception and is removed from the running
  threads. For example, referencing invalid memory,

Therefore, the context switching must thus be able to handle all these cases.

The kernel keeps the next thread to run in a “cache”, and thus the context
switching code only has to fetch from that cache to select which thread to run.

There are two types of context switches: *cooperative* and *preemptive*.

- A *cooperative* context switch happens when a thread willfully gives the
  control to another thread. There are two cases where this happens

  - When a thread explicitly yields.
  - When a thread tries to take an object that is currently unavailable and is
    willing to wait until the object becomes available.
- A *preemptive* context switch happens either because an ISR or a
  thread causes an operation that schedules a thread of higher priority than the
  one currently running, if the currently running thread is preemptible.
  An example of such an operation is releasing an object on which the thread
  of higher priority was waiting.

Note

Control is never taken from cooperative thread when one of them is the
running thread.

A cooperative context switch is always done by having a thread call the
`_Swap()` kernel internal symbol. When `_Swap` is called, the
kernel logic knows that a context switch has to happen: `_Swap` does not
check to see if a context switch must happen. Rather, `_Swap` decides
what thread to context switch in. `_Swap` is called by the kernel logic
when an object being operated on is unavailable, and some thread
yielding/sleeping primitives.

Note

On x86 and Nios2, `_Swap` is generic enough and the architecture
flexible enough that `_Swap` can be called when exiting an interrupt
to provoke the context switch. This should not be taken as a rule, since
neither the ARM Cortex-M or ARCv2 port do this.

Since `_Swap` is cooperative, the caller-saved registers from the ABI are
already on the stack. There is no need to save them in the k\_thread structure.

A context switch can also be performed preemptively. This happens upon exiting
an ISR, in the kernel interrupt exit stub:

- `_interrupt_enter` on x86 after the handler is called.
- `_IntExit` on ARM.
- `_firq_exit` and `_rirq_exit` on ARCv2.

In this case, the context switch must only be invoked when the interrupted
thread was preemptible, not when it was a cooperative one, and only when the
current interrupt is not nested.

The kernel also has the concept of “locking the scheduler”. This is a concept
similar to locking the interrupts, but lighter-weight since interrupts can
still occur. If a thread has locked the scheduler, is it temporarily
non-preemptible.

So, the decision logic to invoke the context switch when exiting an interrupt
is simple:

- If the interrupted thread is not preemptible, do not invoke it.
- Else, fetch the cached thread from the ready queue, and:

  - If the cached thread is not the current thread, invoke the context switch.
  - Else, do not invoke it.

This is simple, but crucial: if this is not implemented correctly, the kernel
will not function as intended and will experience bizarre crashes, mostly due
to stack corruption.

Note

If running a coop-only system, i.e. if [`CONFIG_NUM_PREEMPT_PRIORITIES`](../../kconfig.md#CONFIG_NUM_PREEMPT_PRIORITIES "CONFIG_NUM_PREEMPT_PRIORITIES")
is 0, no preemptive context switch ever happens. The interrupt code can be
optimized to not take any scheduling decision when this is the case.

## Thread Creation and Termination

To start a new thread, a stack frame must be constructed so that the context
switch can pop it the same way it would pop one from a thread that had been
context switched out. This is to be implemented in an architecture-specific
`_new_thread` internal routine.

The thread entry point is also not to be called directly, i.e. it should not be
set as the PC for the new thread. Rather it must be
wrapped in `_thread_entry`. This means that the PC in the stack
frame shall be set to `_thread_entry`, and the thread entry point shall
be passed as the first parameter to `_thread_entry`. The specifics of
this depend on the ABI.

The need for an architecture-specific thread termination implementation depends
on the architecture. There is a generic implementation, but it might not work
for a given architecture.

One reason that has been encountered for having an architecture-specific
implementation of thread termination is that aborting a thread might be
different if aborting because of a graceful exit or because of an exception.
This is the case for ARM Cortex-M, where the CPU has to be taken out of handler
mode if the thread triggered a fatal exception, but not if the thread
gracefully exits its entry point function.

This means implementing an architecture-specific version of
[`k_thread_abort()`](../../doxygen/html/group__thread__apis.md#ga1f44bb0307bea7a97227764ecd7bf963), and setting the Kconfig option
`CONFIG_ARCH_HAS_THREAD_ABORT` as needed for the architecture (e.g. see
[arch/arm/core/cortex\_m/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig)).

## Thread Local Storage

To enable thread local storage on a new architecture:

1. Implement [`arch_tls_stack_setup()`](../../doxygen/html/group__arch-tls.md#ga7f159caca46063b04cf03a54b39255fc) to setup the TLS storage area in
   stack. Refer to the toolchain documentation on how the storage area needs
   to be structured. Some helper functions can be used:

   - Function `z_tls_data_size()` returns the size
     needed for thread local variables (excluding any extra data required by
     toolchain and architecture).
   - Function `z_tls_copy()` prepares the TLS storage area for
     thread local variables. This only copies the variable themselves and
     does not do architecture and/or toolchain specific data.
2. In the context switching, grab the `tls` field inside the new thread’s
   `struct k_thread` and put it into an appropriate register (or some
   other variable) for access to the TLS storage area. Refer to toolchain
   and architecture documentation on which registers to use.
3. In kconfig, add `select CONFIG_ARCH_HAS_THREAD_LOCAL_STORAGE` to
   kconfig related to the new architecture.
4. Run the `tests/kernel/threads/tls` to make sure the new code works.

## Device Drivers

The kernel requires very few hardware devices to function. In theory, the only
required device is the interrupt controller, since the kernel can run without a
system clock. In practice, to get access to most, if not all, of the sanity
check test suite, a system clock is needed as well. Since these two are usually
tied to the architecture, they are part of the architecture port.

### Interrupt Controllers

There can be significant differences between the interrupt controllers and the
interrupt concepts across architectures.

For example, x86 has the concept of an IDT
and different interrupt controllers. The position of an interrupt in the IDT
determines its priority.

On the other hand, the ARM Cortex-M has the NVIC as part of the architecture definition. There is no need
for an IDT-like table that is separate from the NVIC vector table. The position
in the table has nothing to do with priority of an IRQ: priorities are
programmable per-entry.

The ARCv2 has its interrupt unit as part of the architecture definition, which
is somewhat similar to the NVIC. However, where ARC defines interrupts as
having a one-to-one mapping between exception and interrupt numbers (i.e.
exception 1 is IRQ1, and device IRQs start at 16), ARM has IRQ0 being
equivalent to exception 16 (and weirdly enough, exception 1 can be seen as
IRQ-15).

All these differences mean that very little, if anything, can be shared between
architectures with regards to interrupt controllers.

### System Clock

x86 has APIC timers and the HPET as part of its architecture definition. ARM
Cortex-M has the SYSTICK exception. Finally, ARCv2 has the timer0/1 device.

Kernel timeouts are handled in the context of the system clock timer driver’s
interrupt handler.

### Console Over Serial Line

There is one other device that is almost a requirement for an architecture
port, since it is so useful for debugging. It is a simple polling, output-only,
serial port driver on which to send the console (`printk`,
`printf`) output.

It is not required, and a RAM console ([`CONFIG_RAM_CONSOLE`](../../kconfig.md#CONFIG_RAM_CONSOLE "CONFIG_RAM_CONSOLE"))
can be used to send all output to a circular buffer that can be read
by a debugger instead.

## Utility Libraries

The kernel depends on a few functions that can be implemented with very few
instructions or in a lock-less manner in modern processors. Those are thus
expected to be implemented as part of an architecture port.

- Atomic operators.

  - If instructions do exist for a given architecture, the implementation is
    configured using the [`CONFIG_ATOMIC_OPERATIONS_ARCH`](../../kconfig.md#CONFIG_ATOMIC_OPERATIONS_ARCH "CONFIG_ATOMIC_OPERATIONS_ARCH") Kconfig
    option.
  - If instructions do not exist for a given architecture,
    a generic version that wraps [`irq_lock()`](../../doxygen/html/group__isr__apis.md#ga19fdde73c3b02fcca6cf1d1e67631228) or [`irq_unlock()`](../../doxygen/html/group__isr__apis.md#ga646045943b3b2a130738bcc48867bf57)
    around non-atomic operations exists. It is configured using the
    [`CONFIG_ATOMIC_OPERATIONS_C`](../../kconfig.md#CONFIG_ATOMIC_OPERATIONS_C "CONFIG_ATOMIC_OPERATIONS_C") Kconfig option.
- Find-least-significant-bit-set and find-most-significant-bit-set.

  - If instructions do not exist for a given architecture, it is always
    possible to implement these functions as generic C functions.

It is possible to use compiler built-ins to implement these, but be careful
they use the required compiler barriers.

## CPU Idling/Power Management

The kernel provides support for CPU power management with two functions:
[`arch_cpu_idle()`](../../doxygen/html/group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48) and [`arch_cpu_atomic_idle()`](../../doxygen/html/group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d).

[`arch_cpu_idle()`](../../doxygen/html/group__arch-pm.md#ga6ce051203e6cc091d0fb42a15f662a48) can be as simple as calling the power saving
instruction for the architecture with interrupts unlocked, for example
`hlt` on x86, `wfi` or `wfe` on ARM, `sleep` on ARC.
This function can be called in a loop within a context that does not care if it
get interrupted or not by an interrupt before going to sleep. There are
basically two scenarios when it is correct to use this function:

- In a single-threaded system, in the only thread when the thread is not used
  for doing real work after initialization, i.e. it is sitting in a loop doing
  nothing for the duration of the application.
- In the idle thread.

[`arch_cpu_atomic_idle()`](../../doxygen/html/group__arch-pm.md#ga4d0297717c23a3cc5df434549e26924d), on the other hand, must be able to atomically
re-enable interrupts and invoke the power saving instruction. It can thus be
used in real application code, again in single-threaded systems.

Normally, idling the CPU should be left to the idle thread, but in some very
special scenarios, these APIs can be used by applications.

Both functions must exist for a given architecture. However, the implementation
can be simply the following steps, if desired:

1. unlock interrupts
2. NOP

However, a real implementation is strongly recommended.

## Fault Management

In the event of an unhandled CPU exception, the architecture
code must call into `z_fatal_error()`. This function dumps
out architecture-agnostic information and makes a policy
decision on what to do next by invoking `k_sys_fatal_error()`.
This function can be overridden to implement application-specific
policies that could include locking interrupts and spinning forever
(the default implementation) or even powering off the
system (if supported).

## Toolchain and Linking

Toolchain support has to be added to the build system.

Some architecture-specific definitions are needed in [include/zephyr/toolchain/gcc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/toolchain/gcc.h).
See what exists in that file for currently supported architectures.

Each architecture also needs its own linker script, even if most sections can
be derived from the linker scripts of other architectures. Some sections might
be specific to the new architecture, for example the SCB section on ARM and the
IDT section on x86.

## Memory Management and Memory Mapping

If the target platform enables paging and requires drivers to memory-map
their I/O regions, [`CONFIG_MMU`](../../kconfig.md#CONFIG_MMU "CONFIG_MMU") needs to be enabled and the
following API implemented:

- [`arch_mem_map()`](../../doxygen/html/group__arch-mmu.md#ga627bee468e54bb2d5ebe6ac53bb7fc94)
- [`arch_mem_unmap()`](../../doxygen/html/group__arch-mmu.md#ga8783e1d292510477b3816b6686d7d8cd)
- [`arch_page_phys_get()`](../../doxygen/html/group__arch-mmu.md#gaa31a233dab4ad575a9a969de10965200)

## Stack Objects

The presence of memory protection hardware affects how stack objects are
created. All architecture ports must specify the required alignment of the
stack pointer, which is some combination of CPU and ABI requirements. This
is defined in architecture headers with [`ARCH_STACK_PTR_ALIGN`](../../doxygen/html/ztest_8h.md#af0f8ad93611d93cd0626914837e761d3) and
is typically something small like 4, 8, or 16 bytes.

Two types of thread stacks exist:

- “kernel” stacks defined with [`K_KERNEL_STACK_DEFINE()`](../../doxygen/html/group__thread__stack__api.md#ga9e05e3cb5aa5b72d6f19e2f327313271) and related
  APIs, which can host kernel threads running in supervisor mode or
  used as the stack for interrupt/exception handling. These have significantly
  relaxed alignment requirements and use less reserved data. No memory is
  reserved for privilege elevation stacks.
- “thread” stacks which typically use more memory, but are capable of hosting
  thread running in user mode, as well as any use-cases for kernel stacks.

If [`CONFIG_USERSPACE`](../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is not enabled, “thread” and “kernel” stacks are
equivalent.

Additional macros may be defined in the architecture layer to specify
the alignment of the base of stack objects, any reserved data inside the
stack object not used for the thread’s stack buffer, and how to round up
stack sizes to support user mode threads. In the absence of definitions
some defaults are assumed:

- [`ARCH_KERNEL_STACK_RESERVED`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#a75b8e6cce01f5a34e9f3d649e561c3af): default no reserved space
- [`ARCH_THREAD_STACK_RESERVED`](../../doxygen/html/arch_2x86_2thread__stack_8h.md#ace8831316d471ccfb06eeddb6d69d817): default no reserved space
- [`ARCH_KERNEL_STACK_OBJ_ALIGN`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#ac5a3684c543902ec50373d2c774c5bf6): default align to
  [`ARCH_STACK_PTR_ALIGN`](../../doxygen/html/ztest_8h.md#af0f8ad93611d93cd0626914837e761d3)
- [`ARCH_THREAD_STACK_OBJ_ALIGN`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7): default align to
  [`ARCH_STACK_PTR_ALIGN`](../../doxygen/html/ztest_8h.md#af0f8ad93611d93cd0626914837e761d3)
- `ARCH_THREAD_STACK_SIZE_ALIGN`: default round up to
  [`ARCH_STACK_PTR_ALIGN`](../../doxygen/html/ztest_8h.md#af0f8ad93611d93cd0626914837e761d3)

All stack creation macros are defined in terms of these.

Stack objects all have the following layout, with some regions potentially
zero-sized depending on configuration. There are always two main parts:
reserved memory at the beginning, and then the stack buffer itself. The
bounds of some areas can only be determined at runtime in the context of
its associated thread object. Other areas are entirely computable at build
time.

Some architectures may need to carve-out reserved memory at runtime from the
stack buffer, instead of unconditionally reserving it at build time, or to
supplement an existing reserved area (as is the case with the ARM FPU).
Such carve-outs will always be tracked in `thread.stack_info.start`.
The region specified by `thread.stack_info.start` and
`thread.stack_info.size` is always fully accessible by a user mode thread.
`thread.stack_info.delta` denotes an offset which can be used to compute
the initial stack pointer from the very end of the stack object, taking into
account storage for TLS and ASLR random offsets.

```text
+---------------------+ <- thread.stack_obj
| Reserved Memory     | } K_(THREAD|KERNEL)_STACK_RESERVED
+---------------------+
| Carved-out memory   |
|.....................| <- thread.stack_info.start
| Unused stack buffer |
|                     |
|.....................| <- thread's current stack pointer
| Used stack buffer   |
|                     |
|.....................| <- Initial stack pointer. Computable
| ASLR Random offset  |      with thread.stack_info.delta
+---------------------| <- thread.userspace_local_data
| Thread-local data   |
+---------------------+ <- thread.stack_info.start + thread.stack_info.size
```

At present, Zephyr does not support stacks that grow upward.

### No Memory Protection

If no memory protection is in use, then the defaults are sufficient.

### HW-based stack overflow detection

This option uses hardware features to generate a fatal error if a thread
in supervisor mode overflows its stack. This is useful for debugging, although
for a couple reasons, you can’t reliably make any assertions about the state
of the system after this happens:

- The kernel could have been inside a critical section when the overflow
  occurs, leaving important global data structures in a corrupted state.
- For systems that implement stack protection using a guard memory region,
  it’s possible to overshoot the guard and corrupt adjacent data structures
  before the hardware detects this situation.

To enable the [`CONFIG_HW_STACK_PROTECTION`](../../kconfig.md#CONFIG_HW_STACK_PROTECTION "CONFIG_HW_STACK_PROTECTION") feature, the system must
provide some kind of hardware-based stack overflow protection, and enable the
`CONFIG_ARCH_HAS_STACK_PROTECTION` option.

Two forms of HW-based stack overflow detection are supported: dedicated
CPU features for this purpose, or special read-only guard regions immediately
preceding stack buffers.

[`CONFIG_HW_STACK_PROTECTION`](../../kconfig.md#CONFIG_HW_STACK_PROTECTION "CONFIG_HW_STACK_PROTECTION") only catches stack overflows for
supervisor threads. This is not required to catch stack overflow from user
threads; [`CONFIG_USERSPACE`](../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is orthogonal.

This feature only detects supervisor mode stack overflows, including stack
overflows when handling system calls. It doesn’t guarantee that the kernel has
not been corrupted. Any stack overflow in supervisor mode should be treated as
a fatal error, with no assertions about the integrity of the overall system
possible.

Stack overflows in user mode are recoverable (from the kernel’s perspective)
and require no special configuration; [`CONFIG_HW_STACK_PROTECTION`](../../kconfig.md#CONFIG_HW_STACK_PROTECTION "CONFIG_HW_STACK_PROTECTION")
only applies to catching overflows when the CPU is in supervisor mode.

#### CPU-based stack overflow detection

If we are detecting stack overflows in supervisor mode via special CPU
registers (like ARM’s SPLIM), then the defaults are sufficient.

#### Guard-based stack overflow detection

We are detecting supervisor mode stack overflows via special memory protection
region located immediately before the stack buffer that generates an exception
on write. Reserved memory will be used for the guard region.

[`ARCH_KERNEL_STACK_RESERVED`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#a75b8e6cce01f5a34e9f3d649e561c3af) should be defined to the minimum size
of a memory protection region. On most ARM CPUs this is 32 bytes.
[`ARCH_KERNEL_STACK_OBJ_ALIGN`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#ac5a3684c543902ec50373d2c774c5bf6) should also be set to the required
alignment for this region.

MMU-based systems should not reserve RAM for the guard region and instead
simply leave an non-present virtual page below every stack when it is mapped
into the address space. The stack object will still need to be properly aligned
and sized to page granularity.

```text
+-----------------------------+ <- thread.stack_obj
| Guard reserved memory       | } K_KERNEL_STACK_RESERVED
+-----------------------------+
| Guard carve-out             |
|.............................| <- thread.stack_info.start
| Stack buffer                |
.                             .
```

Guard carve-outs for kernel stacks are uncommon and should be avoided if
possible. They tend to be needed for two situations:

- The same stack may be re-purposed to host a user thread, in which case
  the guard is unnecessary and shouldn’t be unconditionally reserved.
  This is the case when privilege elevation stacks are not inside the stack
  object.
- The required guard size is variable and depends on context. For example, some
  ARM CPUs have lazy floating point stacking during exceptions and may
  decrement the stack pointer by a large value without writing anything,
  completely overshooting a minimally-sized guard and corrupting adjacent
  memory. Rather than unconditionally reserving a larger guard, the extra
  memory is carved out if the thread uses floating point.

### User mode enabled

Enabling user mode activates two new requirements:

- A separate fixed-sized privilege mode stack, specified by
  [`CONFIG_PRIVILEGED_STACK_SIZE`](../../kconfig.md#CONFIG_PRIVILEGED_STACK_SIZE "CONFIG_PRIVILEGED_STACK_SIZE"), must be allocated that the user
  thread cannot access. It is used as the stack by the kernel when handling
  system calls. If stack guards are implemented, a stack guard region must
  be able to be placed before it, with support for carve-outs if necessary.
- The memory protection hardware must be able to program a region that exactly
  covers the thread’s stack buffer, tracked in `thread.stack_info`. This
  implies that [`ARCH_THREAD_STACK_SIZE_ADJUST()`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8) will need to round
  up the requested stack size so that a region may cover it, and that
  [`ARCH_THREAD_STACK_OBJ_ALIGN()`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7) is also specified per the
  granularity of the memory protection hardware.

This becomes more complicated if the memory protection hardware requires that
all memory regions be sized to a power of two, and aligned to their own size.
This is common on older MPUs and is known with
[`CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT`](../../kconfig.md#CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT "CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT").

`thread.stack_info` always tracks the user-accessible part of the stack
object, it must always be correct to program a memory protection region with
user access using the range stored within.

#### Non power-of-two memory region requirements

On systems without power-of-two region requirements, the reserved memory area
for threads stacks defined by [`K_THREAD_STACK_RESERVED`](../../doxygen/html/kernel_2thread__stack_8h.md#a025b257739ad52fe7106585b51468e49) may be used to
contain the privilege mode stack. The layout could be something like:

```text
+------------------------------+ <- thread.stack_obj
| Other platform data          |
+------------------------------+
| Guard region (if enabled)    |
+------------------------------+
| Guard carve-out (if needed)  |
|..............................|
| Privilege elevation stack    |
+------------------------------| <- thread.stack_obj +
| Stack buffer                 |      K_THREAD_STACK_RESERVED =
.                              .      thread.stack_info.start
```

The guard region, and any carve-out (if needed) would be configured as a
read-only region when the thread is created.

- If the thread is a supervisor thread, the privilege elevation region is just
  extra stack memory. An overflow will eventually crash into the guard region.
- If the thread is running in user mode, a memory protection region will be
  configured to allow user threads access to the stack buffer, but nothing
  before or after it. An overflow in user mode will crash into the privilege
  elevation stack, which the user thread has no access to. An overflow when
  handling a system call will crash into the guard region.

On an MMU system there should be no physical guards; the privilege mode stack
will be mapped into kernel memory, and the stack buffer in the user part of
memory, each with non-present virtual guard pages below them to catch runtime
stack overflows.

Other platform data may be stored before the guard region, but this is highly
discouraged if such data could be stored in `thread.arch` somewhere.

[`ARCH_THREAD_STACK_RESERVED`](../../doxygen/html/arch_2x86_2thread__stack_8h.md#ace8831316d471ccfb06eeddb6d69d817) will need to be defined to capture
the size of the reserved region containing platform data, privilege elevation
stacks, and guards. It must be appropriately sized such that an MPU region
to grant user mode access to the stack buffer can be placed immediately
after it.

#### Power-of-two memory region requirements

Thread stack objects must be sized and aligned to the same power of two,
without any reserved memory to allow efficient packing in memory. Thus,
any guards in the thread stack must be completely carved out, and the
privilege elevation stack must be allocated elsewhere.

[`ARCH_THREAD_STACK_SIZE_ADJUST()`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#ab76d60bd06e5c5a0f995c6b11bf97fd8) and
[`ARCH_THREAD_STACK_OBJ_ALIGN()`](../../doxygen/html/arch_2xtensa_2thread__stack_8h.md#ab6c1d96f5e018ed166ee401dc84b7ab7) should both be defined to
`Z_POW2_CEIL()`. [`K_THREAD_STACK_RESERVED`](../../doxygen/html/kernel_2thread__stack_8h.md#a025b257739ad52fe7106585b51468e49) must be 0.

For the privilege stacks, the [`CONFIG_GEN_PRIV_STACKS`](../../kconfig.md#CONFIG_GEN_PRIV_STACKS "CONFIG_GEN_PRIV_STACKS") must be,
enabled. For every thread stack found in the system, a corresponding fixed-size
kernel stack used for handling system calls is generated. The address
of the privilege stacks can be looked up quickly at runtime based on the
thread stack address using `z_priv_stack_find()`. These stacks are
laid out the same way as other kernel-only stacks.

```text
+-----------------------------+ <- z_priv_stack_find(thread.stack_obj)
| Reserved memory             | } K_KERNEL_STACK_RESERVED
+-----------------------------+
| Guard carve-out (if needed) |
|.............................|
| Privilege elevation stack   |
|                             |
+-----------------------------+ <- z_priv_stack_find(thread.stack_obj) +
                                     K_KERNEL_STACK_RESERVED +
                                     CONFIG_PRIVILEGED_STACK_SIZE

+-----------------------------+ <- thread.stack_obj
| MPU guard carve-out         |
| (supervisor mode only)      |
|.............................| <- thread.stack_info.start
| Stack buffer                |
.                             .
```

The guard carve-out in the thread stack object is only used if the thread is
running in supervisor mode. If the thread drops to user mode, there is no guard
and the entire object is used as the stack buffer, with full access to the
associated user mode thread and `thread.stack_info` updated appropriately.

## User Mode Threads

To support user mode threads, several kernel-to-arch APIs need to be
implemented, and the system must enable the `CONFIG_ARCH_HAS_USERSPACE`
option. Please see the documentation for each of these functions for more
details:

- [`arch_buffer_validate()`](../../doxygen/html/group__arch-userspace.md#ga13053a9233b86d5cd19dc3cea5804a16) to test whether the current thread has
  access permissions to a particular memory region
- [`arch_user_mode_enter()`](../../doxygen/html/group__arch-userspace.md#ga447daa0454a90a7a3a247de01e522567) which will irreversibly drop a supervisor
  thread to user mode privileges. The stack must be wiped.
- [`arch_syscall_oops()`](../../doxygen/html/group__arch-userspace.md#gad53908f229d7e2c333574b009493644b) which generates a kernel oops when system
  call parameters can’t be validated, in such a way that the oops appears to be
  generated from where the system call was invoked in the user thread
- [`arch_syscall_invoke0()`](../../doxygen/html/group__arch-userspace.md#ga5e9ab24b9c980e327903fbe3f5bd97f3) through
  [`arch_syscall_invoke6()`](../../doxygen/html/group__arch-userspace.md#gac6cae2197637993a86b6ec6803b5742b) invoke a system call with the
  appropriate number of arguments which must all be passed in during the
  privilege elevation via registers.
- [`arch_is_user_context()`](../../doxygen/html/group__arch-userspace.md#ga89ab53a218add419e37f89c1f5fd955f) return nonzero if the CPU is currently
  running in user mode
- [`arch_mem_domain_max_partitions_get()`](../../doxygen/html/group__arch-userspace.md#ga71542fcc679a94ad9ea60d7ac46da361) which indicates the max
  number of regions for a memory domain. MMU systems have an unlimited amount,
  MPU systems have constraints on this.

Some architectures may need to update software memory management structures
or modify hardware registers on another CPU when memory domain APIs are invoked.
If so, [`CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`](../../kconfig.md#CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API "CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API") must be selected by the
architecture and some additional APIs must be implemented. This is common
on MMU systems and uncommon on MPU systems:

- `arch_mem_domain_thread_add()`
- `arch_mem_domain_thread_remove()`
- `arch_mem_domain_partition_add()`
- `arch_mem_domain_partition_remove()`

Please see the doxygen documentation of these APIs for details.

In addition to implementing these APIs, there are some other tasks as well:

- `_new_thread()` needs to spawn threads with [`K_USER`](../../doxygen/html/group__thread__apis.md#gacb5340339892f22301e02697c6039ccc) in
  user mode
- On context switch, the outgoing thread’s stack memory should be marked
  inaccessible to user mode by making the appropriate configuration changes in
  the memory management hardware.. The incoming thread’s stack memory should
  likewise be marked as accessible. This ensures that threads can’t mess with
  other thread stacks.
- On context switch, the system needs to switch between memory domains for
  the incoming and outgoing threads.
- Thread stack areas must include a kernel stack region. This should be
  inaccessible to user threads at all times. This stack will be used when
  system calls are made. This should be fixed size for all threads, and must
  be large enough to handle any system call.
- A software interrupt or some kind of privilege elevation mechanism needs to
  be established. This is closely tied to how the \_arch\_syscall\_invoke macros
  are implemented. On system call, the appropriate handler function needs to
  be looked up in \_k\_syscall\_table. Bad system call IDs should jump to the
  `K_SYSCALL_BAD` handler. Upon completion of the system call, care
  must be taken not to leak any register state back to user mode.

## GDB Stub

To enable GDB stub for remote debugging on a new architecture:

1. Create a new `gdbstub.h` header file under appropriate architecture
   include directory (`include/arch/<arch>/gdbstub.h`).

   - Create a new struct `struct gdb_ctx` as the GDB context.

     - Must define a member named `exception` of type `unsigned int` to
       store the GDB exception reason. This value needs to be set before
       entering `z_gdb_main_loop()`.
     - Architecture can define as many members as needed for GDB stub to
       function.
     - Pointer to this struct needs to be passed to `z_gdb_main_loop()`,
       where this pointer will be passed to other GDB stub functions.
2. Functions for entering and exiting GDB stub main loop.

   - If the architecture relies on interrupts to service breakpoints,
     interrupt service routines (ISR) need to be implemented, which
     will serve as the entry point to GDB stub main loop.
   - These functions need to save and restore context so code execution
     can continue as if no breakpoints have been encountered.
   - These functions need to call `z_gdb_main_loop()` after saving
     execution context to go into the GDB stub main loop to receive commands
     from GDB.
   - Before calling `z_gdb_main_loop()`, [`gdb_ctx.exception`](../../doxygen/html/structgdb__ctx.md#adba5c39e347abc419b365bab2a1a0999)
     must be set to specify the exception reason.
3. Implement necessary functions to support GDB stub functionality:

   - [`arch_gdb_init()`](../../doxygen/html/group__arch-gdbstub.md#ga21c8a32d35c4d267b8306d595ff1d726)

     - This needs to initialize necessary bits to support GDB stub functionality,
       for example, setting up the GDB context and connecting debug interrupts.
     - This must stop code execution via architecture specific method (e.g.
       raising debug interrupts). This allows GDB to connect during boot.
   - [`arch_gdb_continue()`](../../doxygen/html/group__arch-gdbstub.md#ga9c130421feeee919651828511743b346)

     - This function is called when GDB sends a `c` or `continue` command
       to continue code execution.
   - [`arch_gdb_step()`](../../doxygen/html/group__arch-gdbstub.md#ga2aa577d5e55c8b739e2be6187336aaf0)

     - This function is called when GDB sends a `si` or `stepi` command
       to execute one machine instruction, before returning to GDB prompt.
   - Hardware register read/write functions:

     - Since the GDB stub is running on the target, manipulation of hardware
       registers need to cached to avoid affecting the execution of GDB stub.
       Think of it as context switching, where the execution context is
       changed to the GDB stub. So that the register values of the running
       thread before context switch need to be stored. Manipulation of
       register values must only be done to this cached copy. The updated
       values will then be written to hardware registers before switching
       back to the previous running thread.
     - [`arch_gdb_reg_readall()`](../../doxygen/html/group__arch-gdbstub.md#ga5317106a8022bea2a0d42af0789cc016)

       - This collects all hardware register values that would appear in
         a `g`/`G` packets which will be sent back to GDB. The format of
         the G-packet is architecture specific. Consult GDB on what is
         expected.
       - Note that, for most architectures, a valid G-packet must be returned
         and sent to GDB. If a packet without incorrect length is sent to
         GDB, GDB will abort the debugging session.
     - [`arch_gdb_reg_writeall()`](../../doxygen/html/group__arch-gdbstub.md#ga0ef78d7e193e98549d9665632e53d5ca)

       - This takes a G-packet sent by GDB and populates the hardware
         registers with values from the G-packet.
     - [`arch_gdb_reg_readone()`](../../doxygen/html/group__arch-gdbstub.md#gaa3216e9f381f974c374a6399af5cdba5)

       - This reads the value of one hardware register and sends
         the result to GDB.
     - [`arch_gdb_reg_writeone()`](../../doxygen/html/group__arch-gdbstub.md#gad717b520d774294bbda78a56cddcaeff)

       - This writes the value of one hardware register received from GDB.
   - Breakpoints:

     - [`arch_gdb_add_breakpoint()`](../../doxygen/html/group__arch-gdbstub.md#gab6f42110cf2340132bf2b3916810c01d) and
       [`arch_gdb_remove_breakpoint()`](../../doxygen/html/group__arch-gdbstub.md#ga734041433f69030ad98439d10ef56ad6)
     - GDB may decide to use software breakpoints which modifies
       the memory at the breakpoint locations to replace the instruction
       with software breakpoint or trap instructions. GDB will then
       restore the memory content once execution reaches the breakpoints.
       GDB supports this by default and there is usually no need to
       handle software breakpoints in the architecture code (where
       breakpoint type is `0`).
     - Hardware breakpoints (type `1`) are required if the code is
       in ROM or flash that cannot be modified at runtime. Consult
       the architecture datasheet on how to enable hardware breakpoints.
     - If hardware breakpoints are not supported by the architecture,
       there is no need to implement these in architecture code.
       GDB will then rely on software breakpoints.
4. For architecture where certain memory regions are not accessible,
   an array named [`gdb_mem_region_array`](../../doxygen/html/debug_2gdbstub_8h.md#a9d01831c656bae3ee4592ccb45456295) of type
   [`gdb_mem_region`](../../doxygen/html/structgdb__mem__region.md) needs to be defined to specify regions
   that are accessible. For each array item:

   - [`gdb_mem_region.start`](../../doxygen/html/structgdb__mem__region.md#a463465123fd373996a857b38c71474b3) specifies the start of a memory
     region.
   - [`gdb_mem_region.end`](../../doxygen/html/structgdb__mem__region.md#a16001ef766b3c5775c1d1b2c59575b74) specifies the end of a memory
     region.
   - [`gdb_mem_region.attributes`](../../doxygen/html/structgdb__mem__region.md#ad8ae6acf6950428a9846a25fb0219eeb) specifies the permission
     of a memory region.

     - [`GDB_MEM_REGION_RO`](../../doxygen/html/debug_2gdbstub_8h.md#a083549c8b9db7f28536481e33d362479): region is read-only.
     - [`GDB_MEM_REGION_RW`](../../doxygen/html/debug_2gdbstub_8h.md#a386751baaedc3e607a37a473a88bb05a): region is read-write.
   - [`gdb_mem_region.alignment`](../../doxygen/html/structgdb__mem__region.md#aa714bde657eb3572367a924298dd927f) specifies read/write alignment
     of a memory region. Use `0` if there is no alignment requirement
     and read/write can be done byte-by-byte.

## API Reference

### Timing

[Architecture timing APIs](../../doxygen/html/group__arch-timing.md)

### Threads

[Architecture thread APIs](../../doxygen/html/group__arch-threads.md)

[Architecture-specific Thread Local Storage APIs](../../doxygen/html/group__arch-tls.md)

### Power Management

[Architecture-specific power management APIs](../../doxygen/html/group__arch-pm.md)

### Symmetric Multi-Processing

[Architecture-specific SMP APIs](../../doxygen/html/group__arch-smp.md)

### Interrupts

[Architecture-specific IRQ APIs](../../doxygen/html/group__arch-irq.md)

### Userspace

[Architecture-specific userspace APIs](../../doxygen/html/group__arch-userspace.md)

### Memory Management

[Architecture-specific memory-mapping APIs](../../doxygen/html/group__arch-mmu.md)

### Miscellaneous Architecture APIs

[Miscellaneous architecture APIs](../../doxygen/html/group__arch-misc.md)

### GDB Stub APIs

[Architecture-specific gdbstub APIs](../../doxygen/html/group__arch-gdbstub.md)
