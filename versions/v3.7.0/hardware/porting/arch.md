---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/porting/arch.html
original_path: hardware/porting/arch.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

- locking interrupts: [`irq_lock()`](../../kernel/services/interrupts.md#c.irq_lock "irq_lock"), [`irq_unlock()`](../../kernel/services/interrupts.md#c.irq_unlock "irq_unlock").
- registering interrupts: [`IRQ_CONNECT()`](../../kernel/services/interrupts.md#c.IRQ_CONNECT "IRQ_CONNECT").
- programming the priority if possible `irq_priority_set()`.
- enabling/disabling interrupts: [`irq_enable()`](../../kernel/services/interrupts.md#c.irq_enable "irq_enable"), [`irq_disable()`](../../kernel/services/interrupts.md#c.irq_disable "irq_disable").

Note

[`IRQ_CONNECT`](../../kernel/services/interrupts.md#c.IRQ_CONNECT "IRQ_CONNECT") is a macro that uses assembler and/or linker script
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
[`k_thread_abort()`](../../kernel/services/threads/index.md#c.k_thread_abort "k_thread_abort"), and setting the Kconfig option
`CONFIG_ARCH_HAS_THREAD_ABORT` as needed for the architecture (e.g. see
[arch/arm/core/cortex\_m/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/arch/arm/core/cortex_m/Kconfig)).

## Thread Local Storage

To enable thread local storage on a new architecture:

1. Implement [`arch_tls_stack_setup()`](#c.arch_tls_stack_setup) to setup the TLS storage area in
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
    a generic version that wraps [`irq_lock()`](../../kernel/services/interrupts.md#c.irq_lock "irq_lock") or [`irq_unlock()`](../../kernel/services/interrupts.md#c.irq_unlock "irq_unlock")
    around non-atomic operations exists. It is configured using the
    [`CONFIG_ATOMIC_OPERATIONS_C`](../../kconfig.md#CONFIG_ATOMIC_OPERATIONS_C "CONFIG_ATOMIC_OPERATIONS_C") Kconfig option.
- Find-least-significant-bit-set and find-most-significant-bit-set.

  - If instructions do not exist for a given architecture, it is always
    possible to implement these functions as generic C functions.

It is possible to use compiler built-ins to implement these, but be careful
they use the required compiler barriers.

## CPU Idling/Power Management

The kernel provides support for CPU power management with two functions:
[`arch_cpu_idle()`](#c.arch_cpu_idle) and [`arch_cpu_atomic_idle()`](#c.arch_cpu_atomic_idle).

[`arch_cpu_idle()`](#c.arch_cpu_idle) can be as simple as calling the power saving
instruction for the architecture with interrupts unlocked, for example
`hlt` on x86, `wfi` or `wfe` on ARM, `sleep` on ARC.
This function can be called in a loop within a context that does not care if it
get interrupted or not by an interrupt before going to sleep. There are
basically two scenarios when it is correct to use this function:

- In a single-threaded system, in the only thread when the thread is not used
  for doing real work after initialization, i.e. it is sitting in a loop doing
  nothing for the duration of the application.
- In the idle thread.

[`arch_cpu_atomic_idle()`](#c.arch_cpu_atomic_idle), on the other hand, must be able to atomically
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

- [`arch_mem_map()`](#c.arch_mem_map)
- [`arch_mem_unmap()`](#c.arch_mem_unmap)
- [`arch_page_phys_get()`](#c.arch_page_phys_get)

## Stack Objects

The presence of memory protection hardware affects how stack objects are
created. All architecture ports must specify the required alignment of the
stack pointer, which is some combination of CPU and ABI requirements. This
is defined in architecture headers with `ARCH_STACK_PTR_ALIGN` and
is typically something small like 4, 8, or 16 bytes.

Two types of thread stacks exist:

- “kernel” stacks defined with [`K_KERNEL_STACK_DEFINE()`](../../kernel/services/threads/index.md#c.K_KERNEL_STACK_DEFINE "K_KERNEL_STACK_DEFINE") and related
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

- `ARCH_KERNEL_STACK_RESERVED`: default no reserved space
- `ARCH_THREAD_STACK_RESERVED`: default no reserved space
- `ARCH_KERNEL_STACK_OBJ_ALIGN`: default align to
  `ARCH_STACK_PTR_ALIGN`
- `ARCH_THREAD_STACK_OBJ_ALIGN`: default align to
  `ARCH_STACK_PTR_ALIGN`
- `ARCH_THREAD_STACK_SIZE_ALIGN`: default round up to
  `ARCH_STACK_PTR_ALIGN`

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

`ARCH_KERNEL_STACK_RESERVED` should be defined to the minimum size
of a memory protection region. On most ARM CPUs this is 32 bytes.
`ARCH_KERNEL_STACK_OBJ_ALIGN` should also be set to the required
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
  implies that `ARCH_THREAD_STACK_SIZE_ADJUST()` will need to round
  up the requested stack size so that a region may cover it, and that
  `ARCH_THREAD_STACK_OBJ_ALIGN()` is also specified per the
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
for threads stacks defined by `K_THREAD_STACK_RESERVED` may be used to
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

`ARCH_THREAD_STACK_RESERVED` will need to be defined to capture
the size of the reserved region containing platform data, privilege elevation
stacks, and guards. It must be appropriately sized such that an MPU region
to grant user mode access to the stack buffer can be placed immediately
after it.

#### Power-of-two memory region requirements

Thread stack objects must be sized and aligned to the same power of two,
without any reserved memory to allow efficient packing in memory. Thus,
any guards in the thread stack must be completely carved out, and the
privilege elevation stack must be allocated elsewhere.

`ARCH_THREAD_STACK_SIZE_ADJUST()` and
`ARCH_THREAD_STACK_OBJ_ALIGN()` should both be defined to
`Z_POW2_CEIL()`. `K_THREAD_STACK_RESERVED` must be 0.

For the privilege stacks, the [`CONFIG_GEN_PRIV_STACKS`](../../kconfig.md#CONFIG_GEN_PRIV_STACKS "CONFIG_GEN_PRIV_STACKS") must be,
enabled. For every thread stack found in the system, a corresponding fixed-
size kernel stack used for handling system calls is generated. The address
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

- [`arch_buffer_validate()`](#c.arch_buffer_validate) to test whether the current thread has
  access permissions to a particular memory region
- [`arch_user_mode_enter()`](#c.arch_user_mode_enter) which will irreversibly drop a supervisor
  thread to user mode privileges. The stack must be wiped.
- [`arch_syscall_oops()`](#c.arch_syscall_oops) which generates a kernel oops when system
  call parameters can’t be validated, in such a way that the oops appears to be
  generated from where the system call was invoked in the user thread
- [`arch_syscall_invoke0()`](#c.arch_syscall_invoke0) through
  [`arch_syscall_invoke6()`](#c.arch_syscall_invoke6) invoke a system call with the
  appropriate number of arguments which must all be passed in during the
  privilege elevation via registers.
- [`arch_is_user_context()`](#c.arch_is_user_context) return nonzero if the CPU is currently
  running in user mode
- [`arch_mem_domain_max_partitions_get()`](#c.arch_mem_domain_max_partitions_get) which indicates the max
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

- `_new_thread()` needs to spawn threads with [`K_USER`](../../kernel/services/threads/index.md#c.K_USER "K_USER") in
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
   - Before calling `z_gdb_main_loop()`, `gdb_ctx.exception`
     must be set to specify the exception reason.
3. Implement necessary functions to support GDB stub functionality:

   - [`arch_gdb_init()`](#c.arch_gdb_init)

     - This needs to initialize necessary bits to support GDB stub functionality,
       for example, setting up the GDB context and connecting debug interrupts.
     - This must stop code execution via architecture specific method (e.g.
       raising debug interrupts). This allows GDB to connect during boot.
   - [`arch_gdb_continue()`](#c.arch_gdb_continue)

     - This function is called when GDB sends a `c` or `continue` command
       to continue code execution.
   - [`arch_gdb_step()`](#c.arch_gdb_step)

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
     - [`arch_gdb_reg_readall()`](#c.arch_gdb_reg_readall)

       - This collects all hardware register values that would appear in
         a `g`/`G` packets which will be sent back to GDB. The format of
         the G-packet is architecture specific. Consult GDB on what is
         expected.
       - Note that, for most architectures, a valid G-packet must be returned
         and sent to GDB. If a packet without incorrect length is sent to
         GDB, GDB will abort the debugging session.
     - [`arch_gdb_reg_writeall()`](#c.arch_gdb_reg_writeall)

       - This takes a G-packet sent by GDB and populates the hardware
         registers with values from the G-packet.
     - [`arch_gdb_reg_readone()`](#c.arch_gdb_reg_readone)

       - This reads the value of one hardware register and sends
         the result to GDB.
     - [`arch_gdb_reg_writeone()`](#c.arch_gdb_reg_writeone)

       - This writes the value of one hardware register received from GDB.
   - Breakpoints:

     - [`arch_gdb_add_breakpoint()`](#c.arch_gdb_add_breakpoint) and
       [`arch_gdb_remove_breakpoint()`](#c.arch_gdb_remove_breakpoint)
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
   an array named `gdb_mem_region_array` of type
   `gdb_mem_region` needs to be defined to specify regions
   that are accessible. For each array item:

   - `gdb_mem_region.start` specifies the start of a memory
     region.
   - `gdb_mem_region.end` specifies the end of a memory
     region.
   - `gdb_mem_region.attributes` specifies the permission
     of a memory region.

     - `GDB_MEM_REGION_RO`: region is read-only.
     - `GDB_MEM_REGION_RW`: region is read-write.
   - `gdb_mem_region.alignment` specifies read/write alignment
     of a memory region. Use `0` if there is no alignment requirement
     and read/write can be done byte-by-byte.

## API Reference

### Timing

*group* Architecture timing APIs
:   Functions

    void arch\_busy\_wait(uint32\_t usec\_to\_wait)
    :   Architecture-specific implementation of busy-waiting.

        Parameters:
        :   - **usec\_to\_wait** – Wait period, in microseconds

    static inline uint32\_t arch\_k\_cycle\_get\_32(void)
    :   Obtain the current cycle count, in units specified by CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC.

        While this is historically specified as part of the architecture API, in practice virtually all platforms forward it to the sys\_clock\_cycle\_get\_32() API provided by the timer driver.

        See also

        [k\_cycle\_get\_32()](../../kernel/services/timing/clocks.md#group__clock__apis_1ga208687de625e0036558343b4e66143d3)

        Returns:
        :   The current cycle time. This should count up monotonically through the full 32 bit space, wrapping at 0xffffffff. Hardware with fewer bits of precision in the timer is expected to synthesize a 32 bit count.

    static inline uint64\_t arch\_k\_cycle\_get\_64(void)
    :   As for [arch\_k\_cycle\_get\_32()](#group__arch-timing_1ga9ee9f897ec750957de45bf8d43349d5e), but with a 64 bit return value.

        Not all timer hardware has a 64 bit timer, this needs to be implemented only if CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER is set.

        See also

        [arch\_k\_cycle\_get\_32()](#group__arch-timing_1ga9ee9f897ec750957de45bf8d43349d5e)

        Returns:
        :   The current cycle time. This should count up monotonically through the full 64 bit space, wrapping at 2^64-1. Hardware with fewer bits of precision in the timer is generally not expected to implement this API.

### Threads

*group* Architecture thread APIs
:   Functions

    void arch\_new\_thread(struct [k\_thread](../../kernel/services/threads/index.md#c.k_thread "k_thread") \*thread, k\_thread\_stack\_t \*stack, char \*stack\_ptr, k\_thread\_entry\_t entry, void \*p1, void \*p2, void \*p3)
    :   Handle arch-specific logic for setting up new threads.

        The stack and arch-specific thread state variables must be set up such that a later attempt to switch to this thread will succeed and we will enter z\_thread\_entry with the requested thread and arguments as its parameters.

        At some point in this function’s implementation, z\_setup\_new\_thread() must be called with the true bounds of the available stack buffer within the thread’s stack object.

        The provided stack pointer is guaranteed to be properly aligned with respect to the CPU and ABI requirements. There may be space reserved between the stack pointer and the bounds of the stack buffer for initial stack pointer randomization and thread-local storage.

        Fields in thread->base will be initialized when this is called.

        Parameters:
        :   - **thread** – Pointer to uninitialized struct [k\_thread](../../kernel/services/threads/index.md#structk__thread)
            - **stack** – Pointer to the stack object
            - **stack\_ptr** – Aligned initial stack pointer
            - **entry** – Thread entry function
            - **p1** – 1st entry point parameter
            - **p2** – 2nd entry point parameter
            - **p3** – 3rd entry point parameter

    static inline void arch\_switch(void \*switch\_to, void \*\*switched\_from)
    :   Cooperative context switch primitive.

        The action of [arch\_switch()](#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025) should be to switch to a new context passed in the first argument, and save a pointer to the current context into the address passed in the second argument.

        The actual type and interpretation of the switch handle is specified by the architecture. It is the same data structure stored in the “switch\_handle” field of a newly-created thread in [arch\_new\_thread()](#group__arch-threads_1gade449838e445fa8201266e38215c616c), and passed to the kernel as the “interrupted” argument to z\_get\_next\_switch\_handle().

        Note that on SMP systems, the kernel uses the store through the second pointer as a synchronization point to detect when a thread context is completely saved (so another CPU can know when it is safe to switch). This store must be done AFTER all relevant state is saved, and must include whatever memory barriers or cache management code is required to be sure another CPU will see the result correctly.

        The simplest implementation of [arch\_switch()](#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025) is generally to push state onto the thread stack and use the resulting stack pointer as the switch handle. Some architectures may instead decide to use a pointer into the thread struct as the “switch handle” type. These can legally assume that the second argument to [arch\_switch()](#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025) is the address of the switch\_handle field of struct thread\_base and can use an offset on this value to find other parts of the thread struct. For example a (C pseudocode) implementation of [arch\_switch()](#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025) might look like:

        void [arch\_switch(void \*switch\_to, void \*\*switched\_from)](#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025) { struct [k\_thread](../../kernel/services/threads/index.md#structk__thread) \*new = switch\_to; struct [k\_thread](../../kernel/services/threads/index.md#structk__thread) \*old = [CONTAINER\_OF(switched\_from, struct k\_thread,switch\_handle)](../../kernel/util/index.md#group__sys-util_1gac5bc561d1bfd1bf68877fe577779bd2f);

        // save old context… \*switched\_from = old; // restore new context… }

        Note that the kernel manages the switch\_handle field for synchronization as described above. So it is not legal for architecture code to assume that it has any particular value at any other time. In particular it is not legal to read the field from the address passed in the second argument.

        Parameters:
        :   - **switch\_to** – Incoming thread’s switch handle
            - **switched\_from** – Pointer to outgoing thread’s switch handle storage location, which must be updated.

    void arch\_switch\_to\_main\_thread(struct [k\_thread](../../kernel/services/threads/index.md#c.k_thread "k_thread") \*main\_thread, char \*stack\_ptr, k\_thread\_entry\_t \_main)
    :   Custom logic for entering main thread context at early boot.

        Used by architectures where the typical trick of setting up a dummy thread in early boot context to “switch out” of isn’t workable.

        Parameters:
        :   - **main\_thread** – main thread object
            - **stack\_ptr** – Initial stack pointer
            - **\_main** – Entry point for application main function.

    int arch\_float\_disable(struct [k\_thread](../../kernel/services/threads/index.md#c.k_thread "k_thread") \*thread)
    :   Disable floating point context preservation.

        The function is used to disable the preservation of floating point context information for a particular thread.

        Note

        For ARM architecture, disabling floating point preservation may only be requested for the current thread and cannot be requested in ISRs.

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If the floating point disabling could not be performed.
            - **-ENOTSUP** – If the operation is not supported

    int arch\_float\_enable(struct [k\_thread](../../kernel/services/threads/index.md#c.k_thread "k_thread") \*thread, unsigned int options)
    :   Enable floating point context preservation.

        The function is used to enable the preservation of floating point context information for a particular thread. This API depends on each architecture implementation. If the architecture does not support enabling, this API will always be failed.

        The *options* parameter indicates which floating point register sets will be used by the specified thread. Currently it is used by x86 only.

        Parameters:
        :   - **thread** – ID of thread.
            - **options** – architecture dependent options

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If the floating point enabling could not be performed.
            - **-ENOTSUP** – If the operation is not supported

*group* Architecture-specific Thread Local Storage APIs
:   Functions

    size\_t arch\_tls\_stack\_setup(struct [k\_thread](../../kernel/services/threads/index.md#c.k_thread "k_thread") \*new\_thread, char \*stack\_ptr)
    :   Setup Architecture-specific TLS area in stack.

        This sets up the stack area for thread local storage. The structure inside TLS area is architecture specific.

        Parameters:
        :   - **new\_thread** – New thread object
            - **stack\_ptr** – Stack pointer

        Returns:
        :   Number of bytes taken by the TLS area

### Power Management

*group* Architecture-specific power management APIs
:   Functions

    FUNC\_NORETURN void arch\_system\_halt(unsigned int reason)
    :   Halt the system, optionally propagating a reason code.

    void arch\_cpu\_idle(void)
    :   Power save idle routine.

        This function will be called by the kernel idle loop or possibly within an implementation of z\_pm\_save\_idle in the kernel when the ‘\_pm\_save\_flag’ variable is non-zero.

        Architectures that do not implement power management instructions may immediately return, otherwise a power-saving instruction should be issued to wait for an interrupt.

        See also

        [k\_cpu\_idle()](../../kernel/services/scheduling/index.md#group__cpu__idle__apis_1ga7b25e1bed511a813b32fbd0f91b09356)

        Note

        The function is expected to return after the interrupt that has caused the CPU to exit power-saving mode has been serviced, although this is not a firm requirement.

    void arch\_cpu\_atomic\_idle(unsigned int key)
    :   Atomically re-enable interrupts and enter low power mode.

        The requirements for [arch\_cpu\_atomic\_idle()](#group__arch-pm_1ga4d0297717c23a3cc5df434549e26924d) are as follows:

        1. Enabling interrupts and entering a low-power mode needs to be atomic, i.e. there should be no period of time where interrupts are enabled before the processor enters a low-power mode. See the comments in [k\_lifo\_get()](../../kernel/services/data_passing/lifos.md#group__lifo__apis_1gad5f1775947b07a2a77f667aa9e41db5a), for example, of the race condition that occurs if this requirement is not met.
        2. After waking up from the low-power mode, the interrupt lockout state must be restored as indicated in the ‘key’ input parameter.

        See also

        [k\_cpu\_atomic\_idle()](../../kernel/services/scheduling/index.md#group__cpu__idle__apis_1gadf88ece6447b65b7d0d2f3a70ab4fe8f)

        Parameters:
        :   - **key** – Lockout key returned by previous invocation of [arch\_irq\_lock()](#group__arch-irq_1ga25bca3069cb999b6d4f924b87bf7de38)

### Symmetric Multi-Processing

*group* Architecture-specific SMP APIs
:   Typedefs

    typedef void (\*arch\_cpustart\_t)(void \*data)
    :   Per-cpu entry function.

        Param data:
        :   context parameter, implementation specific

    Functions

    void arch\_cpu\_start(int cpu\_num, k\_thread\_stack\_t \*stack, int sz, [arch\_cpustart\_t](#c.arch_cpustart_t) fn, void \*arg)
    :   Start a numbered CPU on a MP-capable system.

        This starts and initializes a specific CPU. The main thread on startup is running on CPU zero, other processors are numbered sequentially. On return from this function, the CPU is known to have begun operating and will enter the provided function. Its interrupts will be initialized but disabled such that [irq\_unlock()](../../kernel/services/interrupts.md#group__isr__apis_1ga646045943b3b2a130738bcc48867bf57) with the provided key will work to enable them.

        Normally, in SMP mode this function will be called by the kernel initialization and should not be used as a user API. But it is defined here for special-purpose apps which want Zephyr running on one core and to use others for design-specific processing.

        Parameters:
        :   - **cpu\_num** – Integer number of the CPU
            - **stack** – Stack memory for the CPU
            - **sz** – Stack buffer size, in bytes
            - **fn** – Function to begin running on the CPU.
            - **arg** – Untyped argument to be passed to “fn”

    bool arch\_cpu\_active(int cpu\_num)
    :   Return CPU power status.

        Parameters:
        :   - **cpu\_num** – Integer number of the CPU

    static inline struct \_cpu \*arch\_curr\_cpu(void)
    :   Return the CPU struct for the currently executing CPU.

    static inline uint32\_t arch\_proc\_id(void)
    :   Processor hardware ID.

        Most multiprocessor architectures have a low-level unique ID value associated with the current CPU that can be retrieved rapidly and efficiently in kernel context. Note that while the numbering of the CPUs is guaranteed to be unique, the values are platform-defined. In particular, they are not guaranteed to match Zephyr’s own sequential CPU IDs (even though on some platforms they do).

        Note

        There is an inherent race with this API: the system may preempt the current thread and migrate it to another CPU before the value is used. Safe usage requires knowing the migration is impossible (e.g. because the code is in interrupt context, holds a spinlock, or cannot migrate due to k\_cpu\_mask state).

        Returns:
        :   Unique ID for currently-executing CPU

    void arch\_sched\_broadcast\_ipi(void)
    :   Broadcast an interrupt to all CPUs.

        This will invoke z\_sched\_ipi() on all other CPUs in the system.

    void arch\_sched\_directed\_ipi(uint32\_t cpu\_bitmap)
    :   Direct IPIs to the specified CPUs.

        This will invoke z\_sched\_ipi() on the CPUs identified by *cpu\_bitmap*.

        Parameters:
        :   - **cpu\_bitmap** – A bitmap indicating which CPUs need the IPI

    int arch\_smp\_init(void)

    static inline unsigned int arch\_num\_cpus(void)
    :   Returns the number of CPUs.

        For most systems this will be the same as CONFIG\_MP\_MAX\_NUM\_CPUS, however some systems may determine this at runtime instead.

        Returns:
        :   the number of CPUs

### Interrupts

*group* Architecture-specific IRQ APIs
:   Functions

    static inline \_Bool arch\_is\_in\_isr(void)
    :   Test if the current context is in interrupt context.

        XXX: This is inconsistently handled among arches wrt exception context See: #17656

        Returns:
        :   true if we are in interrupt context

    static inline unsigned int arch\_irq\_lock(void)
    :   Lock interrupts on the current CPU.

        See also

        [irq\_lock()](../../kernel/services/interrupts.md#group__isr__apis_1ga19fdde73c3b02fcca6cf1d1e67631228)

    static inline void arch\_irq\_unlock(unsigned int key)
    :   Unlock interrupts on the current CPU.

        See also

        [irq\_unlock()](../../kernel/services/interrupts.md#group__isr__apis_1ga646045943b3b2a130738bcc48867bf57)

    static inline bool arch\_irq\_unlocked(unsigned int key)
    :   Test if calling [arch\_irq\_unlock()](#group__arch-irq_1gaa2b2745d8e99b8730b44805f4d3bbf05) with this key would unlock irqs.

        Parameters:
        :   - **key** – value returned by [arch\_irq\_lock()](#group__arch-irq_1ga25bca3069cb999b6d4f924b87bf7de38)

        Returns:
        :   true if interrupts were unlocked prior to the [arch\_irq\_lock()](#group__arch-irq_1ga25bca3069cb999b6d4f924b87bf7de38) call that produced the key argument.

    void arch\_irq\_disable(unsigned int irq)
    :   Disable the specified interrupt line.

        See also

        [irq\_disable()](../../kernel/services/interrupts.md#group__isr__apis_1ga82c3a15d812f58e0f6525f358d031e6d)

        Note

        : The behavior of interrupts that arrive after this call returns and before the corresponding call to arch\_irq\_enable() is undefined. The hardware is not required to latch and deliver such an interrupt, though on some architectures that may work. Other architectures will simply lose such an interrupt and never deliver it. Many drivers and subsystems are not tolerant of such dropped interrupts and it is the job of the application layer to ensure that behavior remains correct.

    void arch\_irq\_enable(unsigned int irq)
    :   Enable the specified interrupt line.

        See also

        [irq\_enable()](../../kernel/services/interrupts.md#group__isr__apis_1ga7ea700ee31e4ff036c997a554dbedfeb)

    int arch\_irq\_is\_enabled(unsigned int irq)
    :   Test if an interrupt line is enabled.

        See also

        [irq\_is\_enabled()](../../kernel/services/interrupts.md#group__isr__apis_1ga71fef3867ba9818cf0a5baf8410a6354)

    int arch\_irq\_connect\_dynamic(unsigned int irq, unsigned int priority, void (\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)
    :   Arch-specific hook to install a dynamic interrupt.

        Parameters:
        :   - **irq** – IRQ line number
            - **priority** – Interrupt priority
            - **routine** – Interrupt service routine
            - **parameter** – ISR parameter
            - **flags** – Arch-specific IRQ configuration flag

        Returns:
        :   The vector assigned to this interrupt

    int arch\_irq\_disconnect\_dynamic(unsigned int irq, unsigned int priority, void (\*routine)(const void \*parameter), const void \*parameter, uint32\_t flags)
    :   Arch-specific hook to dynamically uninstall a shared interrupt.

        If the interrupt is not being shared, then the associated \_sw\_isr\_table entry will be replaced by (NULL, z\_irq\_spurious) (default entry).

        Parameters:
        :   - **irq** – IRQ line number
            - **priority** – Interrupt priority
            - **routine** – Interrupt service routine
            - **parameter** – ISR parameter
            - **flags** – Arch-specific IRQ configuration flag

        Returns:
        :   0 in case of success, negative value otherwise

    unsigned int arch\_irq\_allocate(void)
    :   Arch-specific hook for allocating IRQs.

        Note: disable/enable IRQ relevantly inside the implementation of such function to avoid concurrency issues. Also, an allocated IRQ is assumed to be used thus a following

        See also

        [arch\_irq\_is\_used()](#group__arch-irq_1ga5c85d7bf54a83190ed27587dc5a01de5) should return true.

        Returns:
        :   The newly allocated IRQ or UINT\_MAX on error.

    void arch\_irq\_set\_used(unsigned int irq)
    :   Arch-specific hook for declaring an IRQ being used.

        Note: disable/enable IRQ relevantly inside the implementation of such function to avoid concurrency issues.

        Parameters:
        :   - **irq** – the IRQ to declare being used

    bool arch\_irq\_is\_used(unsigned int irq)
    :   Arch-specific hook for checking if an IRQ is being used already.

        Parameters:
        :   - **irq** – the IRQ to check

        Returns:
        :   true if being, false otherwise

### Userspace

*group* Architecture-specific userspace APIs
:   Functions

    static inline uintptr\_t arch\_syscall\_invoke0(uintptr\_t call\_id)
    :   Invoke a system call with 0 arguments.

        No general-purpose register state other than return value may be preserved when transitioning from supervisor mode back down to user mode for security reasons.

        It is required that all arguments be stored in registers when elevating privileges from user to supervisor mode.

        Processing of the syscall takes place on a separate kernel stack. Interrupts should be enabled when invoking the system call marshallers from the dispatch table. Thread preemption may occur when handling system calls.

        Call IDs are untrusted and must be bounds-checked, as the value is used to index the system call dispatch table, containing function pointers to the specific system call code.

        Parameters:
        :   - **call\_id** – System call ID

        Returns:
        :   Return value of the system call. Void system calls return 0 here.

    static inline uintptr\_t arch\_syscall\_invoke1(uintptr\_t arg1, uintptr\_t call\_id)
    :   Invoke a system call with 1 argument.

        See also

        [arch\_syscall\_invoke0()](#group__arch-userspace_1ga5e9ab24b9c980e327903fbe3f5bd97f3)

        Parameters:
        :   - **arg1** – First argument to the system call.
            - **call\_id** – System call ID, will be bounds-checked and used to reference kernel-side dispatch table

        Returns:
        :   Return value of the system call. Void system calls return 0 here.

    static inline uintptr\_t arch\_syscall\_invoke2(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t call\_id)
    :   Invoke a system call with 2 arguments.

        See also

        [arch\_syscall\_invoke0()](#group__arch-userspace_1ga5e9ab24b9c980e327903fbe3f5bd97f3)

        Parameters:
        :   - **arg1** – First argument to the system call.
            - **arg2** – Second argument to the system call.
            - **call\_id** – System call ID, will be bounds-checked and used to reference kernel-side dispatch table

        Returns:
        :   Return value of the system call. Void system calls return 0 here.

    static inline uintptr\_t arch\_syscall\_invoke3(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t call\_id)
    :   Invoke a system call with 3 arguments.

        See also

        [arch\_syscall\_invoke0()](#group__arch-userspace_1ga5e9ab24b9c980e327903fbe3f5bd97f3)

        Parameters:
        :   - **arg1** – First argument to the system call.
            - **arg2** – Second argument to the system call.
            - **arg3** – Third argument to the system call.
            - **call\_id** – System call ID, will be bounds-checked and used to reference kernel-side dispatch table

        Returns:
        :   Return value of the system call. Void system calls return 0 here.

    static inline uintptr\_t arch\_syscall\_invoke4(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t call\_id)
    :   Invoke a system call with 4 arguments.

        See also

        [arch\_syscall\_invoke0()](#group__arch-userspace_1ga5e9ab24b9c980e327903fbe3f5bd97f3)

        Parameters:
        :   - **arg1** – First argument to the system call.
            - **arg2** – Second argument to the system call.
            - **arg3** – Third argument to the system call.
            - **arg4** – Fourth argument to the system call.
            - **call\_id** – System call ID, will be bounds-checked and used to reference kernel-side dispatch table

        Returns:
        :   Return value of the system call. Void system calls return 0 here.

    static inline uintptr\_t arch\_syscall\_invoke5(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t arg5, uintptr\_t call\_id)
    :   Invoke a system call with 5 arguments.

        See also

        [arch\_syscall\_invoke0()](#group__arch-userspace_1ga5e9ab24b9c980e327903fbe3f5bd97f3)

        Parameters:
        :   - **arg1** – First argument to the system call.
            - **arg2** – Second argument to the system call.
            - **arg3** – Third argument to the system call.
            - **arg4** – Fourth argument to the system call.
            - **arg5** – Fifth argument to the system call.
            - **call\_id** – System call ID, will be bounds-checked and used to reference kernel-side dispatch table

        Returns:
        :   Return value of the system call. Void system calls return 0 here.

    static inline uintptr\_t arch\_syscall\_invoke6(uintptr\_t arg1, uintptr\_t arg2, uintptr\_t arg3, uintptr\_t arg4, uintptr\_t arg5, uintptr\_t arg6, uintptr\_t call\_id)
    :   Invoke a system call with 6 arguments.

        See also

        [arch\_syscall\_invoke0()](#group__arch-userspace_1ga5e9ab24b9c980e327903fbe3f5bd97f3)

        Parameters:
        :   - **arg1** – First argument to the system call.
            - **arg2** – Second argument to the system call.
            - **arg3** – Third argument to the system call.
            - **arg4** – Fourth argument to the system call.
            - **arg5** – Fifth argument to the system call.
            - **arg6** – Sixth argument to the system call.
            - **call\_id** – System call ID, will be bounds-checked and used to reference kernel-side dispatch table

        Returns:
        :   Return value of the system call. Void system calls return 0 here.

    static inline bool arch\_is\_user\_context(void)
    :   Indicate whether we are currently running in user mode.

        Returns:
        :   True if the CPU is currently running with user permissions

    int arch\_mem\_domain\_max\_partitions\_get(void)
    :   Get the maximum number of partitions for a memory domain.

        Returns:
        :   Max number of partitions, or -1 if there is no limit

    int arch\_buffer\_validate(const void \*addr, size\_t size, int write)
    :   Check memory region permissions.

        Given a memory region, return whether the current memory management hardware configuration would allow a user thread to read/write that region. Used by system calls to validate buffers coming in from userspace.

        Notes: The function is guaranteed to never return validation success, if the entire buffer area is not user accessible.

        The function is guaranteed to correctly validate the permissions of the supplied buffer, if the user access permissions of the entire buffer are enforced by a single, enabled memory management region.

        In some architectures the validation will always return failure if the supplied memory buffer spans multiple enabled memory management regions (even if all such regions permit user access).

        Warning

        Buffer of size zero (0) has undefined behavior.

        Parameters:
        :   - **addr** – start address of the buffer
            - **size** – the size of the buffer
            - **write** – If non-zero, additionally check if the area is writable. Otherwise, just check if the memory can be read.

        Returns:
        :   nonzero if the permissions don’t match.

    size\_t arch\_virt\_region\_align(uintptr\_t phys, size\_t size)
    :   Get the optimal virtual region alignment to optimize the MMU table layout.

        Some MMU HW requires some region to be aligned to some of the intermediate block alignment in order to reduce table usage. This call returns the optimal virtual address alignment in order to permit such optimization in the following MMU mapping call.

        Parameters:
        :   - **phys** – **[in]** Physical address of region to be mapped, aligned to  [`CONFIG_MMU_PAGE_SIZE`](../../kconfig.md#CONFIG_MMU_PAGE_SIZE "CONFIG_MMU_PAGE_SIZE")
            - **size** – **[in]** Size of region to be mapped, aligned to  [`CONFIG_MMU_PAGE_SIZE`](../../kconfig.md#CONFIG_MMU_PAGE_SIZE "CONFIG_MMU_PAGE_SIZE")

        Returns:
        :   Alignment to apply on the virtual address of this region

    FUNC\_NORETURN void arch\_user\_mode\_enter(k\_thread\_entry\_t user\_entry, void \*p1, void \*p2, void \*p3)
    :   Perform a one-way transition from supervisor to user mode.

        Implementations of this function must do the following:

        - Reset the thread’s stack pointer to a suitable initial value. We do not need any prior context since this is a one-way operation.
        - Set up any kernel stack region for the CPU to use during privilege elevation
        - Put the CPU in whatever its equivalent of user mode is
        - Transfer execution to [arch\_new\_thread()](#group__arch-threads_1gade449838e445fa8201266e38215c616c) passing along all the supplied arguments, in user mode.

        Parameters:
        :   - **user\_entry** – Entry point to start executing as a user thread
            - **p1** – 1st parameter to user thread
            - **p2** – 2nd parameter to user thread
            - **p3** – 3rd parameter to user thread

    FUNC\_NORETURN void arch\_syscall\_oops(void \*ssf)
    :   Induce a kernel oops that appears to come from a specific location.

        Normally, k\_oops() generates an exception that appears to come from the call site of the k\_oops() itself.

        However, when validating arguments to a system call, if there are problems we want the oops to appear to come from where the system call was invoked and not inside the validation function.

        Parameters:
        :   - **ssf** – System call stack frame pointer. This gets passed as an argument to \_k\_syscall\_handler\_t functions and its contents are completely architecture specific.

    size\_t arch\_user\_string\_nlen(const char \*s, size\_t maxsize, int \*err)
    :   Safely take the length of a potentially bad string.

        This must not fault, instead the `err` parameter must have -1 written to it. This function otherwise should work exactly like libc strnlen(). On success `err` should be set to 0.

        Parameters:
        :   - **s** – String to measure
            - **maxsize** – Max length of the string
            - **err** – Error value to write

        Returns:
        :   Length of the string, not counting NULL byte, up to maxsize

    static inline bool arch\_mem\_coherent(void \*ptr)
    :   Detect memory coherence type.

        Required when ARCH\_HAS\_COHERENCE is true. This function returns true if the byte pointed to lies within an architecture-defined “coherence region” (typically implemented with uncached memory) and can safely be used in multiprocessor code without explicit flush or invalidate operations.

        Note

        The result is for only the single byte at the specified address, this API is not required to check region boundaries or to expect aligned pointers. The expectation is that the code above will have queried the appropriate address(es).

    static inline void arch\_cohere\_stacks(struct [k\_thread](../../kernel/services/threads/index.md#c.k_thread "k_thread") \*old\_thread, void \*old\_switch\_handle, struct [k\_thread](../../kernel/services/threads/index.md#c.k_thread "k_thread") \*new\_thread)
    :   Ensure cache coherence prior to context switch.

        Required when ARCH\_HAS\_COHERENCE is true. On cache-incoherent multiprocessor architectures, thread stacks are cached by default for performance reasons. They must therefore be flushed appropriately on context switch. The rules are:

        1. The region containing live data in the old stack (generally the bytes between the current stack pointer and the top of the stack memory) must be flushed to underlying storage so a new CPU that runs the same thread sees the correct data. This must happen before the assignment of the switch\_handle field in the thread struct which signals the completion of context switch.
        2. Any data areas to be read from the new stack (generally the same as the live region when it was saved) should be invalidated (and NOT flushed!) in the data cache. This is because another CPU may have run or re-initialized the thread since this CPU suspended it, and any data present in cache will be stale.

        Note

        The kernel will call this function during interrupt exit when a new thread has been chosen to run, and also immediately before entering [arch\_switch()](#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025) to effect a code-driven context switch. In the latter case, it is very likely that more data will be written to the old\_thread stack region after this function returns but before the completion of the switch. Simply flushing naively here is not sufficient on many architectures and coordination with the [arch\_switch()](#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025) implementation is likely required.

        Parameters:
        :   - **old\_thread** – The old thread to be flushed before being allowed to run on other CPUs.
            - **old\_switch\_handle** – The switch handle to be stored into old\_thread (it will not be valid until the cache is flushed so is not present yet). This will be NULL if inside z\_swap() (because the [arch\_switch()](#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025) has not saved it yet).
            - **new\_thread** – The new thread to be invalidated before it runs locally.

### Memory Management

*group* Architecture-specific memory-mapping APIs
:   Defines

    ARCH\_DATA\_PAGE\_ACCESSED
    :   Bit indicating the data page was accessed since the value was last cleared.

        Used by marking eviction algorithms. Safe to set this if uncertain.

        This bit is undefined if ARCH\_DATA\_PAGE\_LOADED is not set.

    ARCH\_DATA\_PAGE\_DIRTY
    :   Bit indicating the data page, if evicted, will need to be paged out.

        Set if the data page was modified since it was last paged out, or if it has never been paged out before. Safe to set this if uncertain.

        This bit is undefined if ARCH\_DATA\_PAGE\_LOADED is not set.

    ARCH\_DATA\_PAGE\_LOADED
    :   Bit indicating that the data page is loaded into a physical page frame.

        If un-set, the data page is paged out or not mapped.

    ARCH\_DATA\_PAGE\_NOT\_MAPPED
    :   If ARCH\_DATA\_PAGE\_LOADED is un-set, this will indicate that the page is not mapped at all.

        This bit is undefined if ARCH\_DATA\_PAGE\_LOADED is set.

    Enums

    enum arch\_page\_location
    :   Status of a particular page location.

        *Values:*

        enumerator ARCH\_PAGE\_LOCATION\_PAGED\_OUT
        :   The page has been evicted to the backing store.

        enumerator ARCH\_PAGE\_LOCATION\_PAGED\_IN
        :   The page is resident in memory.

        enumerator ARCH\_PAGE\_LOCATION\_BAD
        :   The page is not mapped.

    Functions

    void arch\_mem\_map(void \*virt, uintptr\_t phys, size\_t size, uint32\_t flags)
    :   Map physical memory into the virtual address space.

        This is a low-level interface to mapping pages into the address space. Behavior when providing unaligned addresses/sizes is undefined, these are assumed to be aligned to CONFIG\_MMU\_PAGE\_SIZE.

        The core kernel handles all management of the virtual address space; by the time we invoke this function, we know exactly where this mapping will be established. If the page tables already had mappings installed for the virtual memory region, these will be overwritten.

        If the target architecture supports multiple page sizes, currently only the smallest page size will be used.

        The memory range itself is never accessed by this operation.

        This API must be safe to call in ISRs or exception handlers. Calls to this API are assumed to be serialized, and indeed all usage will originate from kernel/mm.c which handles virtual memory management.

        Architectures are expected to pre-allocate page tables for the entire address space, as defined by CONFIG\_KERNEL\_VM\_BASE and CONFIG\_KERNEL\_VM\_SIZE. This operation should never require any kind of allocation for paging structures.

        Validation of arguments should be done via assertions.

        This API is part of infrastructure still under development and may change.

        Parameters:
        :   - **virt** – Page-aligned Destination virtual address to map
            - **phys** – Page-aligned Source physical address to map
            - **size** – Page-aligned size of the mapped memory region in bytes
            - **flags** – Caching, access and control flags, see K\_MAP\_\* macros

    void arch\_mem\_unmap(void \*addr, size\_t size)
    :   Remove mappings for a provided virtual address range.

        This is a low-level interface for un-mapping pages from the address space. When this completes, the relevant page table entries will be updated as if no mapping was ever made for that memory range. No previous context needs to be preserved. This function must update mappings in all active page tables.

        Behavior when providing unaligned addresses/sizes is undefined, these are assumed to be aligned to CONFIG\_MMU\_PAGE\_SIZE.

        Behavior when providing an address range that is not already mapped is undefined.

        This function should never require memory allocations for paging structures, and it is not necessary to free any paging structures. Empty page tables due to all contained entries being un-mapped may remain in place.

        Implementations must invalidate TLBs as necessary.

        This API is part of infrastructure still under development and may change.

        Parameters:
        :   - **addr** – Page-aligned base virtual address to un-map
            - **size** – Page-aligned region size

    int arch\_page\_phys\_get(void \*virt, uintptr\_t \*phys)
    :   Get the mapped physical memory address from virtual address.

        The function only needs to query the current set of page tables as the information it reports must be common to all of them if multiple page tables are in use. If multiple page tables are active it is unnecessary to iterate over all of them.

        Unless otherwise specified, virtual pages have the same mappings across all page tables. Calling this function on data pages that are exceptions to this rule (such as the scratch page) is undefined behavior. Just check the currently installed page tables and return the information in that.

        Parameters:
        :   - **virt** – Page-aligned virtual address
            - **phys** – **[out]** Mapped physical address (can be NULL if only checking if virtual address is mapped)

        Return values:
        :   - **0** – if mapping is found and valid
            - **-EFAULT** – if virtual address is not mapped

    void arch\_reserved\_pages\_update(void)
    :   Update page frame database with reserved pages.

        Some page frames within system RAM may not be available for use. A good example of this is reserved regions in the first megabyte on PC-like systems.

        Implementations of this function should mark all relevant entries in k\_mem\_page\_frames with K\_PAGE\_FRAME\_RESERVED. This function is called at early system initialization with mm\_lock held.

    void arch\_mem\_page\_out(void \*addr, uintptr\_t location)
    :   Update all page tables for a paged-out data page.

        This function:

        - Sets the data page virtual address to trigger a fault if accessed that can be distinguished from access violations or un-mapped pages.
        - Saves the provided location value so that it can retrieved for that data page in the page fault handler.
        - The location value semantics are undefined here but the value will be always be page-aligned. It could be 0.

        If multiple page tables are in use, this must update all page tables. This function is called with interrupts locked.

        Calling this function on data pages which are already paged out is undefined behavior.

        This API is part of infrastructure still under development and may change.

    void arch\_mem\_page\_in(void \*addr, uintptr\_t phys)
    :   Update all page tables for a paged-in data page.

        This function:

        - Maps the specified virtual data page address to the provided physical page frame address, such that future memory accesses will function as expected. Access and caching attributes are undisturbed.
        - Clears any accounting for “accessed” and “dirty” states.

        If multiple page tables are in use, this must update all page tables. This function is called with interrupts locked.

        Calling this function on data pages which are already paged in is undefined behavior.

        This API is part of infrastructure still under development and may change.

    void arch\_mem\_scratch(uintptr\_t phys)
    :   Update current page tables for a temporary mapping.

        Map a physical page frame address to a special virtual address K\_MEM\_SCRATCH\_PAGE, with read/write access to supervisor mode, such that when this function returns, the calling context can read/write the page frame’s contents from the K\_MEM\_SCRATCH\_PAGE address.

        This mapping only needs to be done on the current set of page tables, as it is only used for a short period of time exclusively by the caller. This function is called with interrupts locked.

        This API is part of infrastructure still under development and may change.

    enum [arch\_page\_location](#c.arch_page_location) arch\_page\_location\_get(void \*addr, uintptr\_t \*location)
    :   Fetch location information about a page at a particular address.

        The function only needs to query the current set of page tables as the information it reports must be common to all of them if multiple page tables are in use. If multiple page tables are active it is unnecessary to iterate over all of them. This may allow certain types of optimizations (such as reverse page table mapping on x86).

        This function is called with interrupts locked, so that the reported information can’t become stale while decisions are being made based on it.

        Unless otherwise specified, virtual data pages have the same mappings across all page tables. Calling this function on data pages that are exceptions to this rule (such as the scratch page) is undefined behavior. Just check the currently installed page tables and return the information in that.

        Parameters:
        :   - **addr** – Virtual data page address that took the page fault
            - **location** – **[out]** In the case of ARCH\_PAGE\_LOCATION\_PAGED\_OUT, the backing store location value used to retrieve the data page. In the case of ARCH\_PAGE\_LOCATION\_PAGED\_IN, the physical address the page is mapped to.

        Return values:
        :   - **ARCH\_PAGE\_LOCATION\_PAGED\_OUT** – The page was evicted to the backing store.
            - **ARCH\_PAGE\_LOCATION\_PAGED\_IN** – The data page is resident in memory.
            - **ARCH\_PAGE\_LOCATION\_BAD** – The page is un-mapped or otherwise has had invalid access

    uintptr\_t arch\_page\_info\_get(void \*addr, uintptr\_t \*location, \_Bool clear\_accessed)
    :   Retrieve page characteristics from the page table(s).

        The architecture is responsible for maintaining “accessed” and “dirty” states of data pages to support marking eviction algorithms. This can either be directly supported by hardware or emulated by modifying protection policy to generate faults on reads or writes. In all cases the architecture must maintain this information in some way.

        For the provided virtual address, report the logical OR of the accessed and dirty states for the relevant entries in all active page tables in the system if the page is mapped and not paged out.

        If clear\_accessed is true, the ARCH\_DATA\_PAGE\_ACCESSED flag will be reset. This function will report its prior state. If multiple page tables are in use, this function clears accessed state in all of them.

        This function is called with interrupts locked, so that the reported information can’t become stale while decisions are being made based on it.

        The return value may have other bits set which the caller must ignore.

        Clearing accessed state for data pages that are not ARCH\_DATA\_PAGE\_LOADED is undefined behavior.

        ARCH\_DATA\_PAGE\_DIRTY and ARCH\_DATA\_PAGE\_ACCESSED bits in the return value are only significant if ARCH\_DATA\_PAGE\_LOADED is set, otherwise ignore them.

        ARCH\_DATA\_PAGE\_NOT\_MAPPED bit in the return value is only significant if ARCH\_DATA\_PAGE\_LOADED is un-set, otherwise ignore it.

        Unless otherwise specified, virtual data pages have the same mappings across all page tables. Calling this function on data pages that are exceptions to this rule (such as the scratch page) is undefined behavior.

        This API is part of infrastructure still under development and may change.

        Parameters:
        :   - **addr** – Virtual address to look up in page tables
            - **location** – **[out]** If non-NULL, updated with either physical page frame address or backing store location depending on ARCH\_DATA\_PAGE\_LOADED state. This is not touched if ARCH\_DATA\_PAGE\_NOT\_MAPPED.
            - **clear\_accessed** – Whether to clear ARCH\_DATA\_PAGE\_ACCESSED state

        Return values:
        :   **Value** – with ARCH\_DATA\_PAGE\_\* bits set reflecting the data page configuration

### Miscellaneous Architecture APIs

*group* Miscellaneous architecture APIs
:   Functions

    int arch\_printk\_char\_out(int c)
    :   Early boot console output hook.

        Definition of this function is optional. If implemented, any invocation of printk() (or logging calls with CONFIG\_LOG\_MODE\_MINIMAL which are backed by printk) will default to sending characters to this function. It is useful for early boot debugging before main serial or console drivers come up.

        This can be overridden at runtime with \_\_printk\_hook\_install().

        The default \_\_weak implementation of this does nothing.

        Parameters:
        :   - **c** – Character to print

        Returns:
        :   The character printed

    static inline void arch\_kernel\_init(void)
    :   Architecture-specific kernel initialization hook.

        This function is invoked near the top of z\_cstart, for additional architecture-specific setup before the rest of the kernel is brought up.

    static inline void arch\_nop(void)
    :   Do nothing and return.

        Yawn.

### GDB Stub APIs

*group* Architecture-specific gdbstub APIs
:   Functions

    void arch\_gdb\_init(void)
    :   Architecture layer debug start.

        This function is called by `gdb_init()`

    void arch\_gdb\_continue(void)
    :   Continue running program.

        Continue software execution.

    void arch\_gdb\_step(void)
    :   Continue with one step.

        Continue software execution until reaches the next statement.

    size\_t arch\_gdb\_reg\_readall(struct gdb\_ctx \*ctx, uint8\_t \*buf, size\_t buflen)
    :   Read all registers, and outputs as hexadecimal string.

        This reads all CPU registers and outputs as hexadecimal string. The output string must be parsable by GDB.

        Parameters:
        :   - **ctx** – GDB context
            - **buf** – Buffer to output hexadecimal string.
            - **buflen** – Length of buffer.

        Returns:
        :   Length of hexadecimal string written. Return 0 if error or not supported.

    size\_t arch\_gdb\_reg\_writeall(struct gdb\_ctx \*ctx, uint8\_t \*hex, size\_t hexlen)
    :   Take a hexadecimal string and update all registers.

        This takes in a hexadecimal string as presented from GDB, and updates all CPU registers with new values.

        Parameters:
        :   - **ctx** – GDB context
            - **hex** – Input hexadecimal string.
            - **hexlen** – Length of hexadecimal string.

        Returns:
        :   Length of hexadecimal string parsed. Return 0 if error or not supported.

    size\_t arch\_gdb\_reg\_readone(struct gdb\_ctx \*ctx, uint8\_t \*buf, size\_t buflen, uint32\_t regno)
    :   Read one register, and outputs as hexadecimal string.

        This reads one CPU register and outputs as hexadecimal string. The output string must be parsable by GDB.

        Parameters:
        :   - **ctx** – GDB context
            - **buf** – Buffer to output hexadecimal string.
            - **buflen** – Length of buffer.
            - **regno** – Register number

        Returns:
        :   Length of hexadecimal string written. Return 0 if error or not supported.

    size\_t arch\_gdb\_reg\_writeone(struct gdb\_ctx \*ctx, uint8\_t \*hex, size\_t hexlen, uint32\_t regno)
    :   Take a hexadecimal string and update one register.

        This takes in a hexadecimal string as presented from GDB, and updates one CPU registers with new value.

        Parameters:
        :   - **ctx** – GDB context
            - **hex** – Input hexadecimal string.
            - **hexlen** – Length of hexadecimal string.
            - **regno** – Register number

        Returns:
        :   Length of hexadecimal string parsed. Return 0 if error or not supported.

    int arch\_gdb\_add\_breakpoint(struct gdb\_ctx \*ctx, uint8\_t type, uintptr\_t addr, uint32\_t kind)
    :   Add breakpoint or watchpoint.

        Parameters:
        :   - **ctx** – GDB context
            - **type** – Breakpoint or watchpoint type
            - **addr** – Address of breakpoint or watchpoint
            - **kind** – Size of breakpoint/watchpoint in bytes

        Return values:
        :   - **0** – Operation successful
            - **-1** – Error encountered
            - **-2** – Not supported

    int arch\_gdb\_remove\_breakpoint(struct gdb\_ctx \*ctx, uint8\_t type, uintptr\_t addr, uint32\_t kind)
    :   Remove breakpoint or watchpoint.

        Parameters:
        :   - **ctx** – GDB context
            - **type** – Breakpoint or watchpoint type
            - **addr** – Address of breakpoint or watchpoint
            - **kind** – Size of breakpoint/watchpoint in bytes

        Return values:
        :   - **0** – Operation successful
            - **-1** – Error encountered
            - **-2** – Not supported
