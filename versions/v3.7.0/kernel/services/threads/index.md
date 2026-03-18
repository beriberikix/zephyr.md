---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/services/threads/index.html
original_path: kernel/services/threads/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Threads

Note

There is also limited support for using [Operation without Threads](nothread.md#nothread).

This section describes kernel services for creating, scheduling, and deleting
independently executable threads of instructions.

A *thread* is a kernel object that is used for application processing
that is too lengthy or too complex to be performed by an ISR.

Any number of threads can be defined by an application (limited only by
available RAM). Each thread is referenced by a *thread id* that is assigned
when the thread is spawned.

A thread has the following key properties:

- A **stack area**, which is a region of memory used for the thread’s stack.
  The **size** of the stack area can be tailored to conform to the actual needs
  of the thread’s processing. Special macros exist to create and work with
  stack memory regions.
- A **thread control block** for private kernel bookkeeping of the thread’s
  metadata. This is an instance of type [`k_thread`](#c.k_thread).
- An **entry point function**, which is invoked when the thread is started.
  Up to 3 **argument values** can be passed to this function.
- A **scheduling priority**, which instructs the kernel’s scheduler how to
  allocate CPU time to the thread. (See [Scheduling](../scheduling/index.md#scheduling-v2).)
- A set of **thread options**, which allow the thread to receive special
  treatment by the kernel under specific circumstances.
  (See [Thread Options](#thread-options-v2).)
- A **start delay**, which specifies how long the kernel should wait before
  starting the thread.
- An **execution mode**, which can either be supervisor or user mode.
  By default, threads run in supervisor mode and allow access to
  privileged CPU instructions, the entire memory address space, and
  peripherals. User mode threads have a reduced set of privileges.
  This depends on the [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") option. See [User Mode](../../usermode/index.md#usermode-api).

## [Lifecycle](#id3)

### [Thread Creation](#id4)

A thread must be created before it can be used. The kernel initializes
the thread control block as well as one end of the stack portion. The remainder
of the thread’s stack is typically left uninitialized.

Specifying a start delay of [`K_NO_WAIT`](../timing/clocks.md#c.K_NO_WAIT "K_NO_WAIT") instructs the kernel
to start thread execution immediately. Alternatively, the kernel can be
instructed to delay execution of the thread by specifying a timeout
value – for example, to allow device hardware used by the thread
to become available.

The kernel allows a delayed start to be canceled before the thread begins
executing. A cancellation request has no effect if the thread has already
started. A thread whose delayed start was successfully canceled must be
re-spawned before it can be used.

### [Thread Termination](#id5)

Once a thread is started it typically executes forever. However, a thread may
synchronously end its execution by returning from its entry point function.
This is known as **termination**.

A thread that terminates is responsible for releasing any shared resources
it may own (such as mutexes and dynamically allocated memory)
prior to returning, since the kernel does *not* reclaim them automatically.

In some cases a thread may want to sleep until another thread terminates.
This can be accomplished with the [`k_thread_join()`](#c.k_thread_join) API. This
will block the calling thread until either the timeout expires, the target
thread self-exits, or the target thread aborts (either due to a
[`k_thread_abort()`](#c.k_thread_abort) call or triggering a fatal error).

Once a thread has terminated, the kernel guarantees that no use will
be made of the thread struct. The memory of such a struct can then be
re-used for any purpose, including spawning a new thread. Note that
the thread must be fully terminated, which presents race conditions
where a thread’s own logic signals completion which is seen by another
thread before the kernel processing is complete. Under normal
circumstances, application code should use [`k_thread_join()`](#c.k_thread_join) or
[`k_thread_abort()`](#c.k_thread_abort) to synchronize on thread termination state
and not rely on signaling from within application logic.

### [Thread Aborting](#id6)

A thread may asynchronously end its execution by **aborting**. The kernel
automatically aborts a thread if the thread triggers a fatal error condition,
such as dereferencing a null pointer.

A thread can also be aborted by another thread (or by itself)
by calling [`k_thread_abort()`](#c.k_thread_abort). However, it is typically preferable
to signal a thread to terminate itself gracefully, rather than aborting it.

As with thread termination, the kernel does not reclaim shared resources
owned by an aborted thread.

Note

The kernel does not currently make any claims regarding an application’s
ability to respawn a thread that aborts.

### [Thread Suspension](#id7)

A thread can be prevented from executing for an indefinite period of time
if it becomes **suspended**. The function [`k_thread_suspend()`](#c.k_thread_suspend)
can be used to suspend any thread, including the calling thread.
Suspending a thread that is already suspended has no additional effect.

Once suspended, a thread cannot be scheduled until another thread calls
[`k_thread_resume()`](#c.k_thread_resume) to remove the suspension.

Note

A thread can prevent itself from executing for a specified period of time
using [`k_sleep()`](#c.k_sleep). However, this is different from suspending
a thread since a sleeping thread becomes executable automatically when the
time limit is reached.

## [Thread States](#id8)

A thread that has no factors that prevent its execution is deemed
to be **ready**, and is eligible to be selected as the current thread.

A thread that has one or more factors that prevent its execution
is deemed to be **unready**, and cannot be selected as the current thread.

The following factors make a thread unready:

- The thread has not been started.
- The thread is waiting for a kernel object to complete an operation.
  (For example, the thread is taking a semaphore that is unavailable.)
- The thread is waiting for a timeout to occur.
- The thread has been suspended.
- The thread has terminated or aborted.

  ![../../../_images/thread_states.svg](../../../_images/thread_states.svg)

Note

Although the diagram above may appear to suggest that both **Ready** and
**Running** are distinct thread states, that is not the correct
interpretation. **Ready** is a thread state, and **Running** is a
schedule state that only applies to **Ready** threads.

## [Thread Stack objects](#id9)

Every thread requires its own stack buffer for the CPU to push context.
Depending on configuration, there are several constraints that must be
met:

- There may need to be additional memory reserved for memory management
  structures
- If guard-based stack overflow detection is enabled, a small write-
  protected memory management region must immediately precede the stack buffer
  to catch overflows.
- If userspace is enabled, a separate fixed-size privilege elevation stack must
  be reserved to serve as a private kernel stack for handling system calls.
- If userspace is enabled, the thread’s stack buffer must be appropriately
  sized and aligned such that a memory protection region may be programmed
  to exactly fit.

The alignment constraints can be quite restrictive, for example some MPUs
require their regions to be of some power of two in size, and aligned to its
own size.

Because of this, portable code can’t simply pass an arbitrary character buffer
to [`k_thread_create()`](#c.k_thread_create). Special macros exist to instantiate stacks,
prefixed with `K_KERNEL_STACK` and `K_THREAD_STACK`.

### [Kernel-only Stacks](#id10)

If it is known that a thread will never run in user mode, or the stack is
being used for special contexts like handling interrupts, it is best to
define stacks using the `K_KERNEL_STACK` macros.

These stacks save memory because an MPU region will never need to be
programmed to cover the stack buffer itself, and the kernel will not need
to reserve additional room for the privilege elevation stack, or memory
management data structures which only pertain to user mode threads.

Attempts from user mode to use stacks declared in this way will result in
a fatal error for the caller.

If `CONFIG_USERSPACE` is not enabled, the set of `K_THREAD_STACK` macros
have an identical effect to the `K_KERNEL_STACK` macros.

### [Thread stacks](#id11)

If it is known that a stack will need to host user threads, or if this
cannot be determined, define the stack with `K_THREAD_STACK` macros.
This may use more memory but the stack object is suitable for hosting
user threads.

If `CONFIG_USERSPACE` is not enabled, the set of `K_THREAD_STACK` macros
have an identical effect to the `K_KERNEL_STACK` macros.

## [Thread Priorities](#id12)

A thread’s priority is an integer value, and can be either negative or
non-negative.
Numerically lower priorities takes precedence over numerically higher values.
For example, the scheduler gives thread A of priority 4 *higher* priority
over thread B of priority 7; likewise thread C of priority -2 has higher
priority than both thread A and thread B.

The scheduler distinguishes between two classes of threads,
based on each thread’s priority.

- A *cooperative thread* has a negative priority value.
  Once it becomes the current thread, a cooperative thread remains
  the current thread until it performs an action that makes it unready.
- A *preemptible thread* has a non-negative priority value.
  Once it becomes the current thread, a preemptible thread may be supplanted
  at any time if a cooperative thread, or a preemptible thread of higher
  or equal priority, becomes ready.

A thread’s initial priority value can be altered up or down after the thread
has been started. Thus it is possible for a preemptible thread to become
a cooperative thread, and vice versa, by changing its priority.

Note

The scheduler does not make heuristic decisions to re-prioritize threads.
Thread priorities are set and changed only at the application’s request.

The kernel supports a virtually unlimited number of thread priority levels.
The configuration options [`CONFIG_NUM_COOP_PRIORITIES`](../../../kconfig.md#CONFIG_NUM_COOP_PRIORITIES "CONFIG_NUM_COOP_PRIORITIES") and
[`CONFIG_NUM_PREEMPT_PRIORITIES`](../../../kconfig.md#CONFIG_NUM_PREEMPT_PRIORITIES "CONFIG_NUM_PREEMPT_PRIORITIES") specify the number of priority
levels for each class of thread, resulting in the following usable priority
ranges:

- cooperative threads: (-[`CONFIG_NUM_COOP_PRIORITIES`](../../../kconfig.md#CONFIG_NUM_COOP_PRIORITIES "CONFIG_NUM_COOP_PRIORITIES")) to -1
- preemptive threads: 0 to ([`CONFIG_NUM_PREEMPT_PRIORITIES`](../../../kconfig.md#CONFIG_NUM_PREEMPT_PRIORITIES "CONFIG_NUM_PREEMPT_PRIORITIES") - 1)

![../../../_images/priorities.svg](../../../_images/priorities.svg)

For example, configuring 5 cooperative priorities and 10 preemptive priorities
results in the ranges -5 to -1 and 0 to 9, respectively.

### [Meta-IRQ Priorities](#id13)

When enabled (see [`CONFIG_NUM_METAIRQ_PRIORITIES`](../../../kconfig.md#CONFIG_NUM_METAIRQ_PRIORITIES "CONFIG_NUM_METAIRQ_PRIORITIES")), there is a special
subclass of cooperative priorities at the highest (numerically lowest)
end of the priority space: meta-IRQ threads. These are scheduled
according to their normal priority, but also have the special ability
to preempt all other threads (and other meta-IRQ threads) at lower
priorities, even if those threads are cooperative and/or have taken a
scheduler lock. Meta-IRQ threads are still threads, however,
and can still be interrupted by any hardware interrupt.

This behavior makes the act of unblocking a meta-IRQ thread (by any
means, e.g. creating it, calling k\_sem\_give(), etc.) into the
equivalent of a synchronous system call when done by a lower
priority thread, or an ARM-like “pended IRQ” when done from true
interrupt context. The intent is that this feature will be used to
implement interrupt “bottom half” processing and/or “tasklet” features
in driver subsystems. The thread, once woken, will be guaranteed to
run before the current CPU returns into application code.

Unlike similar features in other OSes, meta-IRQ threads are true
threads and run on their own stack (which must be allocated normally),
not the per-CPU interrupt stack. Design work to enable the use of the
IRQ stack on supported architectures is pending.

Note that because this breaks the promise made to cooperative
threads by the Zephyr API (namely that the OS won’t schedule other
thread until the current thread deliberately blocks), it should be
used only with great care from application code. These are not simply
very high priority threads and should not be used as such.

## [Thread Options](#id14)

The kernel supports a small set of *thread options* that allow a thread
to receive special treatment under specific circumstances. The set of options
associated with a thread are specified when the thread is spawned.

A thread that does not require any thread option has an option value of zero.
A thread that requires a thread option specifies it by name, using the
`|` character as a separator if multiple options are needed
(i.e. combine options using the bitwise OR operator).

The following thread options are supported.

[`K_ESSENTIAL`](#c.K_ESSENTIAL)
:   This option tags the thread as an *essential thread*. This instructs
    the kernel to treat the termination or aborting of the thread as a fatal
    system error.

    By default, the thread is not considered to be an essential thread.

[`K_SSE_REGS`](#c.K_SSE_REGS)
:   This x86-specific option indicate that the thread uses the CPU’s
    SSE registers. Also see [`K_FP_REGS`](#c.K_FP_REGS).

    By default, the kernel does not attempt to save and restore the contents
    of these registers when scheduling the thread.

[`K_FP_REGS`](#c.K_FP_REGS)
:   This option indicate that the thread uses the CPU’s floating point
    registers. This instructs the kernel to take additional steps to save
    and restore the contents of these registers when scheduling the thread.
    (For more information see [Floating Point Services](../other/float.md#float-v2).)

    By default, the kernel does not attempt to save and restore the contents
    of this register when scheduling the thread.

[`K_USER`](#c.K_USER)
:   If [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is enabled, this thread will be created in
    user mode and will have reduced privileges. See [User Mode](../../usermode/index.md#usermode-api). Otherwise
    this flag does nothing.

[`K_INHERIT_PERMS`](#c.K_INHERIT_PERMS)
:   If [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is enabled, this thread will inherit all
    kernel object permissions that the parent thread had, except the parent
    thread object. See [User Mode](../../usermode/index.md#usermode-api).

## [Thread Custom Data](#id15)

Every thread has a 32-bit *custom data* area, accessible only by
the thread itself, and may be used by the application for any purpose
it chooses. The default custom data value for a thread is zero.

Note

Custom data support is not available to ISRs because they operate
within a single shared kernel interrupt handling context.

By default, thread custom data support is disabled. The configuration option
[`CONFIG_THREAD_CUSTOM_DATA`](../../../kconfig.md#CONFIG_THREAD_CUSTOM_DATA "CONFIG_THREAD_CUSTOM_DATA") can be used to enable support.

The [`k_thread_custom_data_set()`](#c.k_thread_custom_data_set) and
[`k_thread_custom_data_get()`](#c.k_thread_custom_data_get) functions are used to write and read
a thread’s custom data, respectively. A thread can only access its own
custom data, and not that of another thread.

The following code uses the custom data feature to record the number of times
each thread calls a specific routine.

Note

Obviously, only a single routine can use this technique,
since it monopolizes the use of the custom data feature.

```c
int call_tracking_routine(void)
{
    uint32_t call_count;

    if (k_is_in_isr()) {
        /* ignore any call made by an ISR */
    } else {
        call_count = (uint32_t)k_thread_custom_data_get();
        call_count++;
        k_thread_custom_data_set((void *)call_count);
    }

    /* do rest of routine's processing */
    ...
}
```

Use thread custom data to allow a routine to access thread-specific information,
by using the custom data as a pointer to a data structure owned by the thread.

## [Implementation](#id16)

### [Spawning a Thread](#id17)

A thread is spawned by defining its stack area and its thread control block,
and then calling [`k_thread_create()`](#c.k_thread_create).

The stack area must be defined using [`K_THREAD_STACK_DEFINE`](#c.K_THREAD_STACK_DEFINE) or
[`K_KERNEL_STACK_DEFINE`](#c.K_KERNEL_STACK_DEFINE) to ensure it is properly set up in memory.

The size parameter for the stack must be one of three values:

- The original requested stack size passed to
  `K_THREAD_STACK` or `K_KERNEL_STACK` family of stack instantiation
  macros.
- For a stack object defined with the `K_THREAD_STACK` family of
  macros, the return value of [`K_THREAD_STACK_SIZEOF()`](#c.K_THREAD_STACK_SIZEOF) for that’
  object.
- For a stack object defined with the `K_KERNEL_STACK` family of
  macros, the return value of [`K_KERNEL_STACK_SIZEOF()`](#c.K_KERNEL_STACK_SIZEOF) for that
  object.

The thread spawning function returns its thread id, which can be used
to reference the thread.

The following code spawns a thread that starts immediately.

```c
#define MY_STACK_SIZE 500
#define MY_PRIORITY 5

extern void my_entry_point(void *, void *, void *);

K_THREAD_STACK_DEFINE(my_stack_area, MY_STACK_SIZE);
struct k_thread my_thread_data;

k_tid_t my_tid = k_thread_create(&my_thread_data, my_stack_area,
                                 K_THREAD_STACK_SIZEOF(my_stack_area),
                                 my_entry_point,
                                 NULL, NULL, NULL,
                                 MY_PRIORITY, 0, K_NO_WAIT);
```

Alternatively, a thread can be declared at compile time by calling
[`K_THREAD_DEFINE`](#c.K_THREAD_DEFINE). Observe that the macro defines
the stack area, control block, and thread id variables automatically.

The following code has the same effect as the code segment above.

```c
#define MY_STACK_SIZE 500
#define MY_PRIORITY 5

extern void my_entry_point(void *, void *, void *);

K_THREAD_DEFINE(my_tid, MY_STACK_SIZE,
                my_entry_point, NULL, NULL, NULL,
                MY_PRIORITY, 0, 0);
```

Note

The delay parameter to [`k_thread_create()`](#c.k_thread_create) is a
[`k_timeout_t`](../timing/clocks.md#c.k_timeout_t "k_timeout_t") value, so [`K_NO_WAIT`](../timing/clocks.md#c.K_NO_WAIT "K_NO_WAIT") means to start the
thread immediately. The corresponding parameter to [`K_THREAD_DEFINE`](#c.K_THREAD_DEFINE)
is a duration in integral milliseconds, so the equivalent argument is 0.

#### User Mode Constraints

This section only applies if [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is enabled, and a user
thread tries to create a new thread. The [`k_thread_create()`](#c.k_thread_create) API is
still used, but there are additional constraints which must be met or the
calling thread will be terminated:

- The calling thread must have permissions granted on both the child thread
  and stack parameters; both are tracked by the kernel as kernel objects.
- The child thread and stack objects must be in an uninitialized state,
  i.e. it is not currently running and the stack memory is unused.
- The stack size parameter passed in must be equal to or less than the
  bounds of the stack object when it was declared.
- The [`K_USER`](#c.K_USER) option must be used, as user threads can only create
  other user threads.
- The [`K_ESSENTIAL`](#c.K_ESSENTIAL) option must not be used, user threads may not be
  considered essential threads.
- The priority of the child thread must be a valid priority value, and equal to
  or lower than the parent thread.

### [Dropping Permissions](#id18)

If [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is enabled, a thread running in supervisor mode
may perform a one-way transition to user mode using the
[`k_thread_user_mode_enter()`](#c.k_thread_user_mode_enter) API. This is a one-way operation which
will reset and zero the thread’s stack memory. The thread will be marked
as non-essential.

### [Terminating a Thread](#id19)

A thread terminates itself by returning from its entry point function.

The following code illustrates the ways a thread can terminate.

```c
void my_entry_point(int unused1, int unused2, int unused3)
{
    while (1) {
        ...
        if (<some condition>) {
            return; /* thread terminates from mid-entry point function */
        }
        ...
    }

    /* thread terminates at end of entry point function */
}
```

If [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is enabled, aborting a thread will additionally
mark the thread and stack objects as uninitialized so that they may be re-used.

## [Runtime Statistics](#id20)

Thread runtime statistics can be gathered and retrieved if
[`CONFIG_THREAD_RUNTIME_STATS`](../../../kconfig.md#CONFIG_THREAD_RUNTIME_STATS "CONFIG_THREAD_RUNTIME_STATS") is enabled, for example, total number of
execution cycles of a thread.

By default, the runtime statistics are gathered using the default kernel
timer. For some architectures, SoCs or boards, there are timers with higher
resolution available via timing functions. Using of these timers can be
enabled via [`CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS`](../../../kconfig.md#CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS "CONFIG_THREAD_RUNTIME_STATS_USE_TIMING_FUNCTIONS").

Here is an example:

```c
k_thread_runtime_stats_t rt_stats_thread;

k_thread_runtime_stats_get(k_current_get(), &rt_stats_thread);

printk("Cycles: %llu\n", rt_stats_thread.execution_cycles);
```

## [Suggested Uses](#id21)

Use threads to handle processing that cannot be handled in an ISR.

Use separate threads to handle logically distinct processing operations
that can execute in parallel.

## [Configuration Options](#id22)

Related configuration options:

- [`CONFIG_MAIN_THREAD_PRIORITY`](../../../kconfig.md#CONFIG_MAIN_THREAD_PRIORITY "CONFIG_MAIN_THREAD_PRIORITY")
- [`CONFIG_MAIN_STACK_SIZE`](../../../kconfig.md#CONFIG_MAIN_STACK_SIZE "CONFIG_MAIN_STACK_SIZE")
- [`CONFIG_IDLE_STACK_SIZE`](../../../kconfig.md#CONFIG_IDLE_STACK_SIZE "CONFIG_IDLE_STACK_SIZE")
- [`CONFIG_THREAD_CUSTOM_DATA`](../../../kconfig.md#CONFIG_THREAD_CUSTOM_DATA "CONFIG_THREAD_CUSTOM_DATA")
- [`CONFIG_NUM_COOP_PRIORITIES`](../../../kconfig.md#CONFIG_NUM_COOP_PRIORITIES "CONFIG_NUM_COOP_PRIORITIES")
- [`CONFIG_NUM_PREEMPT_PRIORITIES`](../../../kconfig.md#CONFIG_NUM_PREEMPT_PRIORITIES "CONFIG_NUM_PREEMPT_PRIORITIES")
- [`CONFIG_TIMESLICING`](../../../kconfig.md#CONFIG_TIMESLICING "CONFIG_TIMESLICING")
- [`CONFIG_TIMESLICE_SIZE`](../../../kconfig.md#CONFIG_TIMESLICE_SIZE "CONFIG_TIMESLICE_SIZE")
- [`CONFIG_TIMESLICE_PRIORITY`](../../../kconfig.md#CONFIG_TIMESLICE_PRIORITY "CONFIG_TIMESLICE_PRIORITY")
- [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE")

## [API Reference](#id23)

Related code samples

[Basic Synchronization](../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.")
:   Manipulate basic kernel synchronization primitives.

[Basic thread manipulation](../../../samples/basic/threads/README.md#multi-thread-blinky "Spawn multiple threads that blink LEDs and print information to the console.")
:   Spawn multiple threads that blink LEDs and print information to the console.

[Dumb HTTP server (multi-threaded)](../../../samples/net/sockets/dumb_http_server_mt/README.md#socket-dumb-http-server-mt "Implement a simple HTTP server supporting simultaneous connections using BSD sockets.")
:   Implement a simple HTTP server supporting simultaneous connections using BSD sockets.

*group* Thread APIs
:   Defines

    K\_ESSENTIAL
    :   system thread that must not abort

    K\_FP\_IDX
    :   FPU registers are managed by context switch.

        This option indicates that the thread uses the CPU’s floating point registers. This instructs the kernel to take additional steps to save and restore the contents of these registers when scheduling the thread. No effect if  [`CONFIG_FPU_SHARING`](../../../kconfig.md#CONFIG_FPU_SHARING "CONFIG_FPU_SHARING") is not enabled.

    K\_FP\_REGS

    K\_USER
    :   user mode thread

        This thread has dropped from supervisor mode to user mode and consequently has additional restrictions

    K\_INHERIT\_PERMS
    :   Inherit Permissions.

        Indicates that the thread being created should inherit all kernel object permissions from the thread that created it. No effect if  [`CONFIG_USERSPACE`](../../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is not enabled.

    K\_CALLBACK\_STATE
    :   Callback item state.

        This is a single bit of state reserved for “callback manager” utilities (p4wq initially) who need to track operations invoked from within a user-provided callback they have been invoked. Effectively it serves as a tiny bit of zero-overhead TLS data.

    K\_DSP\_IDX
    :   DSP registers are managed by context switch.

        This option indicates that the thread uses the CPU’s DSP registers. This instructs the kernel to take additional steps to save and restore the contents of these registers when scheduling the thread. No effect if  [`CONFIG_DSP_SHARING`](../../../kconfig.md#CONFIG_DSP_SHARING "CONFIG_DSP_SHARING") is not enabled.

    K\_DSP\_REGS

    K\_AGU\_IDX
    :   AGU registers are managed by context switch.

        This option indicates that the thread uses the ARC processor’s XY memory and DSP feature. Often used with  [`CONFIG_ARC_AGU_SHARING`](../../../kconfig.md#CONFIG_ARC_AGU_SHARING "CONFIG_ARC_AGU_SHARING") . No effect if  [`CONFIG_ARC_AGU_SHARING`](../../../kconfig.md#CONFIG_ARC_AGU_SHARING "CONFIG_ARC_AGU_SHARING") is not enabled.

    K\_AGU\_REGS

    K\_SSE\_REGS
    :   FP and SSE registers are managed by context switch on x86.

        This option indicates that the thread uses the x86 CPU’s floating point and SSE registers. This instructs the kernel to take additional steps to save and restore the contents of these registers when scheduling the thread. No effect if  [`CONFIG_X86_SSE`](../../../kconfig.md#CONFIG_X86_SSE "CONFIG_X86_SSE") is not enabled.

    k\_thread\_access\_grant(thread, ...)
    :   Grant a thread access to a set of kernel objects.

        This is a convenience function. For the provided thread, grant access to the remaining arguments, which must be pointers to kernel objects.

        The thread object must be initialized (i.e. running). The objects don’t need to be. Note that NULL shouldn’t be passed as an argument.

        Parameters:
        :   - **thread** – Thread to grant access to objects
            - **...** – list of kernel object pointers

    K\_THREAD\_DEFINE(name, stack\_size, entry, p1, p2, p3, prio, options, delay)
    :   Statically define and initialize a thread.

        The thread may be scheduled for immediate execution or a delayed start.

        Thread options are architecture-specific, and can include K\_ESSENTIAL, K\_FP\_REGS, and K\_SSE\_REGS. Multiple options may be specified by separating them using “|” (the logical OR operator).

        The ID of the thread can be accessed using:

        ```text
        extern const k_tid_t <name>;
        ```

        Note

        Static threads with zero delay should not normally have MetaIRQ priority levels. This can preempt the system initialization handling (depending on the priority of the main thread) and cause surprising ordering side effects. It will not affect anything in the OS per se, but consider it bad practice. Use a SYS\_INIT() callback if you need to run code before entrance to the application main().

        Parameters:
        :   - **name** – Name of the thread.
            - **stack\_size** – Stack size in bytes.
            - **entry** – Thread entry function.
            - **p1** – 1st entry point parameter.
            - **p2** – 2nd entry point parameter.
            - **p3** – 3rd entry point parameter.
            - **prio** – Thread priority.
            - **options** – Thread options.
            - **delay** – Scheduling delay (in milliseconds), zero for no delay.

    K\_KERNEL\_THREAD\_DEFINE(name, stack\_size, entry, p1, p2, p3, prio, options, delay)
    :   Statically define and initialize a thread intended to run only in kernel mode.

        The thread may be scheduled for immediate execution or a delayed start.

        Thread options are architecture-specific, and can include K\_ESSENTIAL, K\_FP\_REGS, and K\_SSE\_REGS. Multiple options may be specified by separating them using “|” (the logical OR operator).

        The ID of the thread can be accessed using:

        ```text
        extern const k_tid_t <name>;
        ```

        Note

        Threads defined by this can only run in kernel mode, and cannot be transformed into user thread via [k\_thread\_user\_mode\_enter()](#group__thread__apis_1ga3fbe1c8a5f3ef1c25382c7d6fca35764).

        Warning

        Depending on the architecture, the stack size (`stack_size`) may need to be multiples of CONFIG\_MMU\_PAGE\_SIZE (if MMU) or in power-of-two size (if MPU).

        Parameters:
        :   - **name** – Name of the thread.
            - **stack\_size** – Stack size in bytes.
            - **entry** – Thread entry function.
            - **p1** – 1st entry point parameter.
            - **p2** – 2nd entry point parameter.
            - **p3** – 3rd entry point parameter.
            - **prio** – Thread priority.
            - **options** – Thread options.
            - **delay** – Scheduling delay (in milliseconds), zero for no delay.

    Typedefs

    typedef void (\*k\_thread\_user\_cb\_t)(const struct [k\_thread](#c.k_thread) \*thread, void \*user\_data)

    Functions

    void k\_thread\_foreach([k\_thread\_user\_cb\_t](#c.k_thread_user_cb_t) user\_cb, void \*user\_data)
    :   Iterate over all the threads in the system.

        This routine iterates over all the threads in the system and calls the user\_cb function for each thread.

        Note

        [`CONFIG_THREAD_MONITOR`](../../../kconfig.md#CONFIG_THREAD_MONITOR "CONFIG_THREAD_MONITOR") must be set for this function to be effective.

        Note

        This API uses [k\_spin\_lock](../smp/smp.md#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf) to protect the \_kernel.threads list which means creation of new threads and terminations of existing threads are blocked until this API returns.

        Parameters:
        :   - **user\_cb** – Pointer to the user callback function.
            - **user\_data** – Pointer to user data.

    void k\_thread\_foreach\_unlocked([k\_thread\_user\_cb\_t](#c.k_thread_user_cb_t) user\_cb, void \*user\_data)
    :   Iterate over all the threads in the system without locking.

        This routine works exactly the same like [k\_thread\_foreach](#group__thread__apis_1gae2596d56800769b06fc03c194a126a97) but unlocks interrupts when user\_cb is executed.

        Note

        [`CONFIG_THREAD_MONITOR`](../../../kconfig.md#CONFIG_THREAD_MONITOR "CONFIG_THREAD_MONITOR") must be set for this function to be effective.

        Note

        This API uses [k\_spin\_lock](../smp/smp.md#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf) only when accessing the \_kernel.threads queue elements. It unlocks it during user callback function processing. If a new task is created when this `foreach` function is in progress, the added new task would not be included in the enumeration. If a task is aborted during this enumeration, there would be a race here and there is a possibility that this aborted task would be included in the enumeration.

        Note

        If the task is aborted and the memory occupied by its `[k_thread](#structk__thread)` structure is reused when this `k_thread_foreach_unlocked` is in progress it might even lead to the system behave unstable. This function may never return, as it would follow some `next` task pointers treating given pointer as a pointer to the [k\_thread](#structk__thread) structure while it is something different right now. Do not reuse the memory that was occupied by [k\_thread](#structk__thread) structure of aborted task if it was aborted after this function was called in any context.

        Parameters:
        :   - **user\_cb** – Pointer to the user callback function.
            - **user\_data** – Pointer to user data.

    k\_thread\_stack\_t \*k\_thread\_stack\_alloc(size\_t size, int flags)
    :   Dynamically allocate a thread stack.

        Relevant stack creation flags include:

        - [K\_USER](#group__thread__apis_1gacb5340339892f22301e02697c6039ccc) allocate a userspace thread (requires `CONFIG_USERSPACE=y`)

        See also

        CONFIG\_DYNAMIC\_THREAD

        Parameters:
        :   - **size** – Stack size in bytes.
            - **flags** – Stack creation flags, or 0.

        Return values:
        :   - **the** – allocated thread stack on success.
            - **NULL** – on failure.

    int k\_thread\_stack\_free(k\_thread\_stack\_t \*stack)
    :   Free a dynamically allocated thread stack.

        See also

        CONFIG\_DYNAMIC\_THREAD

        Parameters:
        :   - **stack** – Pointer to the thread stack.

        Return values:
        :   - **0** – on success.
            - **-EBUSY** – if the thread stack is in use.
            - **-EINVAL** – if `stack` is invalid.
            - **-ENOSYS** – if dynamic thread stack allocation is disabled

    k\_tid\_t k\_thread\_create(struct [k\_thread](#c.k_thread) \*new\_thread, k\_thread\_stack\_t \*stack, size\_t stack\_size, k\_thread\_entry\_t entry, void \*p1, void \*p2, void \*p3, int prio, uint32\_t options, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") delay)
    :   Create a thread.

        This routine initializes a thread, then schedules it for execution.

        The new thread may be scheduled for immediate execution or a delayed start. If the newly spawned thread does not have a delayed start the kernel scheduler may preempt the current thread to allow the new thread to execute.

        Thread options are architecture-specific, and can include K\_ESSENTIAL, K\_FP\_REGS, and K\_SSE\_REGS. Multiple options may be specified by separating them using “|” (the logical OR operator).

        Stack objects passed to this function must be originally defined with either of these macros in order to be portable:

        - [K\_THREAD\_STACK\_DEFINE()](#group__thread__stack__api_1gac5368ce24fdeab3863b5c8dee2ebd955) - For stacks that may support either user or supervisor threads.
        - [K\_KERNEL\_STACK\_DEFINE()](#group__thread__stack__api_1ga9e05e3cb5aa5b72d6f19e2f327313271) - For stacks that may support supervisor threads only. These stacks use less memory if CONFIG\_USERSPACE is enabled.

        The stack\_size parameter has constraints. It must either be:

        - The original size value passed to [K\_THREAD\_STACK\_DEFINE()](#group__thread__stack__api_1gac5368ce24fdeab3863b5c8dee2ebd955) or [K\_KERNEL\_STACK\_DEFINE()](#group__thread__stack__api_1ga9e05e3cb5aa5b72d6f19e2f327313271)
        - The return value of [K\_THREAD\_STACK\_SIZEOF(stack)](#group__thread__stack__api_1ga775f8e6b4144cfdd24f3261b6db64150) if the stack was defined with [K\_THREAD\_STACK\_DEFINE()](#group__thread__stack__api_1gac5368ce24fdeab3863b5c8dee2ebd955)
        - The return value of [K\_KERNEL\_STACK\_SIZEOF(stack)](#group__thread__stack__api_1ga57b3824b117c634dbb6052d47dc4301c) if the stack was defined with [K\_KERNEL\_STACK\_DEFINE()](#group__thread__stack__api_1ga9e05e3cb5aa5b72d6f19e2f327313271).

        Using other values, or sizeof(stack) may produce undefined behavior.

        Parameters:
        :   - **new\_thread** – Pointer to uninitialized struct [k\_thread](#structk__thread)
            - **stack** – Pointer to the stack space.
            - **stack\_size** – Stack size in bytes.
            - **entry** – Thread entry function.
            - **p1** – 1st entry point parameter.
            - **p2** – 2nd entry point parameter.
            - **p3** – 3rd entry point parameter.
            - **prio** – Thread priority.
            - **options** – Thread options.
            - **delay** – Scheduling delay, or K\_NO\_WAIT (for no delay).

        Returns:
        :   ID of new thread.

    FUNC\_NORETURN void k\_thread\_user\_mode\_enter(k\_thread\_entry\_t entry, void \*p1, void \*p2, void \*p3)
    :   Drop a thread’s privileges permanently to user mode.

        This allows a supervisor thread to be re-used as a user thread. This function does not return, but control will transfer to the provided entry point as if this was a new user thread.

        The implementation ensures that the stack buffer contents are erased. Any thread-local storage will be reverted to a pristine state.

        Memory domain membership, resource pool assignment, kernel object permissions, priority, and thread options are preserved.

        A common use of this function is to re-use the main thread as a user thread once all supervisor mode-only tasks have been completed.

        Parameters:
        :   - **entry** – Function to start executing from
            - **p1** – 1st entry point parameter
            - **p2** – 2nd entry point parameter
            - **p3** – 3rd entry point parameter

    static inline void k\_thread\_heap\_assign(struct [k\_thread](#c.k_thread) \*thread, struct [k\_heap](../../memory_management/heap.md#c.k_heap "k_heap") \*heap)
    :   Assign a resource memory pool to a thread.

        By default, threads have no resource pool assigned unless their parent thread has a resource pool, in which case it is inherited. Multiple threads may be assigned to the same memory pool.

        Changing a thread’s resource pool will not migrate allocations from the previous pool.

        Parameters:
        :   - **thread** – Target thread to assign a memory pool for resource requests.
            - **heap** – Heap object to use for resources, or NULL if the thread should no longer have a memory pool.

    int k\_thread\_join(struct [k\_thread](#c.k_thread) \*thread, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Sleep until a thread exits.

        The caller will be put to sleep until the target thread exits, either due to being aborted, self-exiting, or taking a fatal error. This API returns immediately if the thread isn’t running.

        This API may only be called from ISRs with a K\_NO\_WAIT timeout, where it can be useful as a predicate to detect when a thread has aborted.

        Parameters:
        :   - **thread** – Thread to wait to exit
            - **timeout** – upper bound time to wait for the thread to exit.

        Return values:
        :   - **0** – success, target thread has exited or wasn’t running
            - **-EBUSY** – returned without waiting
            - **-EAGAIN** – waiting period timed out
            - **-EDEADLK** – target thread is joining on the caller, or target thread is the caller

    int32\_t k\_sleep([k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Put the current thread to sleep.

        This routine puts the current thread to sleep for *duration*, specified as a [k\_timeout\_t](../timing/clocks.md#structk__timeout__t) object.

        Note

        if *timeout* is set to K\_FOREVER then the thread is suspended.

        Parameters:
        :   - **timeout** – Desired duration of sleep.

        Returns:
        :   Zero if the requested time has elapsed or if the thread was woken up by the [k\_wakeup](#group__thread__apis_1ga9275a019c8ff3c7fe49a81f8c078157e) call, the time left to sleep rounded up to the nearest millisecond.

    static inline int32\_t k\_msleep(int32\_t ms)
    :   Put the current thread to sleep.

        This routine puts the current thread to sleep for *duration* milliseconds.

        Parameters:
        :   - **ms** – Number of milliseconds to sleep.

        Returns:
        :   Zero if the requested time has elapsed or if the thread was woken up by the [k\_wakeup](#group__thread__apis_1ga9275a019c8ff3c7fe49a81f8c078157e) call, the time left to sleep rounded up to the nearest millisecond.

    int32\_t k\_usleep(int32\_t us)
    :   Put the current thread to sleep with microsecond resolution.

        This function is unlikely to work as expected without kernel tuning. In particular, because the lower bound on the duration of a sleep is the duration of a tick,  [`CONFIG_SYS_CLOCK_TICKS_PER_SEC`](../../../kconfig.md#CONFIG_SYS_CLOCK_TICKS_PER_SEC "CONFIG_SYS_CLOCK_TICKS_PER_SEC") must be adjusted to achieve the resolution desired. The implications of doing this must be understood before attempting to use [k\_usleep()](#group__thread__apis_1gaeac56bb072ce295b9fdc372ab8cee67e). Use with caution.

        Parameters:
        :   - **us** – Number of microseconds to sleep.

        Returns:
        :   Zero if the requested time has elapsed or if the thread was woken up by the [k\_wakeup](#group__thread__apis_1ga9275a019c8ff3c7fe49a81f8c078157e) call, the time left to sleep rounded up to the nearest microsecond.

    void k\_busy\_wait(uint32\_t usec\_to\_wait)
    :   Cause the current thread to busy wait.

        This routine causes the current thread to execute a “do nothing” loop for *usec\_to\_wait* microseconds.

        Note

        The clock used for the microsecond-resolution delay here may be skewed relative to the clock used for system timeouts like [k\_sleep()](#group__thread__apis_1ga48d4b041790454da4d68ac8711f29657). For example k\_busy\_wait(1000) may take slightly more or less time than k\_sleep(K\_MSEC(1)), with the offset dependent on clock tolerances.

        Note

        In case when  [`CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE`](../../../kconfig.md#CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE "CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE") and  [`CONFIG_PM`](../../../kconfig.md#CONFIG_PM "CONFIG_PM") options are enabled, this function may not work. The timer/clock used for delay processing may be disabled/inactive.

    bool k\_can\_yield(void)
    :   Check whether it is possible to yield in the current context.

        This routine checks whether the kernel is in a state where it is possible to yield or call blocking API’s. It should be used by code that needs to yield to perform correctly, but can feasibly be called from contexts where that is not possible. For example in the PRE\_KERNEL initialization step, or when being run from the idle thread.

        Returns:
        :   True if it is possible to yield in the current context, false otherwise.

    void k\_yield(void)
    :   Yield the current thread.

        This routine causes the current thread to yield execution to another thread of the same or higher priority. If there are no other ready threads of the same or higher priority, the routine returns immediately.

    void k\_wakeup(k\_tid\_t thread)
    :   Wake up a sleeping thread.

        This routine prematurely wakes up *thread* from sleeping.

        If *thread* is not currently sleeping, the routine has no effect.

        Parameters:
        :   - **thread** – ID of thread to wake.

    \_\_attribute\_const\_\_ k\_tid\_t k\_sched\_current\_thread\_query(void)
    :   Query thread ID of the current thread.

        This unconditionally queries the kernel via a system call.

        Note

        Use [k\_current\_get()](#group__thread__apis_1ga7ef1ed0fb9513df8096ede1e52fc76b2) unless absolutely sure this is necessary. This should only be used directly where the thread local variable cannot be used or may contain invalid values if thread local storage (TLS) is enabled. If TLS is not enabled, this is the same as [k\_current\_get()](#group__thread__apis_1ga7ef1ed0fb9513df8096ede1e52fc76b2).

        Returns:
        :   ID of current thread.

    \_\_attribute\_const\_\_ static inline k\_tid\_t k\_current\_get(void)
    :   Get thread ID of the current thread.

        Returns:
        :   ID of current thread.

    void k\_thread\_abort(k\_tid\_t thread)
    :   Abort a thread.

        This routine permanently stops execution of *thread*. The thread is taken off all kernel queues it is part of (i.e. the ready queue, the timeout queue, or a kernel object wait queue). However, any kernel resources the thread might currently own (such as mutexes or memory blocks) are not released. It is the responsibility of the caller of this routine to ensure all necessary cleanup is performed.

        After [k\_thread\_abort()](#group__thread__apis_1ga1f44bb0307bea7a97227764ecd7bf963) returns, the thread is guaranteed not to be running or to become runnable anywhere on the system. Normally this is done via blocking the caller (in the same manner as [k\_thread\_join()](#group__thread__apis_1ga40a733561eb1f64dcaae0e01b167d233)), but in interrupt context on SMP systems the implementation is required to spin for threads that are running on other CPUs.

        Parameters:
        :   - **thread** – ID of thread to abort.

    void k\_thread\_start(k\_tid\_t thread)
    :   Start an inactive thread.

        If a thread was created with K\_FOREVER in the delay parameter, it will not be added to the scheduling queue until this function is called on it.

        Parameters:
        :   - **thread** – thread to start

    [k\_ticks\_t](../timing/clocks.md#c.k_ticks_t "k_ticks_t") k\_thread\_timeout\_expires\_ticks(const struct [k\_thread](#c.k_thread) \*thread)
    :   Get time when a thread wakes up, in system ticks.

        This routine computes the system uptime when a waiting thread next executes, in units of system ticks. If the thread is not waiting, it returns current system time.

    [k\_ticks\_t](../timing/clocks.md#c.k_ticks_t "k_ticks_t") k\_thread\_timeout\_remaining\_ticks(const struct [k\_thread](#c.k_thread) \*thread)
    :   Get time remaining before a thread wakes up, in system ticks.

        This routine computes the time remaining before a waiting thread next executes, in units of system ticks. If the thread is not waiting, it returns zero.

    int k\_thread\_priority\_get(k\_tid\_t thread)
    :   Get a thread’s priority.

        This routine gets the priority of *thread*.

        Parameters:
        :   - **thread** – ID of thread whose priority is needed.

        Returns:
        :   Priority of *thread*.

    void k\_thread\_priority\_set(k\_tid\_t thread, int prio)
    :   Set a thread’s priority.

        This routine immediately changes the priority of *thread*.

        Rescheduling can occur immediately depending on the priority *thread* is set to:

        - If its priority is raised above the priority of the caller of this function, and the caller is preemptible, *thread* will be scheduled in.
        - If the caller operates on itself, it lowers its priority below that of other threads in the system, and the caller is preemptible, the thread of highest priority will be scheduled in.

        Priority can be assigned in the range of -CONFIG\_NUM\_COOP\_PRIORITIES to CONFIG\_NUM\_PREEMPT\_PRIORITIES-1, where -CONFIG\_NUM\_COOP\_PRIORITIES is the highest priority.

        Warning

        Changing the priority of a thread currently involved in mutex priority inheritance may result in undefined behavior.

        Parameters:
        :   - **thread** – ID of thread whose priority is to be set.
            - **prio** – New priority.

    void k\_thread\_deadline\_set(k\_tid\_t thread, int deadline)
    :   Set deadline expiration time for scheduler.

        This sets the “deadline” expiration as a time delta from the current time, in the same units used by [k\_cycle\_get\_32()](../timing/clocks.md#group__clock__apis_1ga208687de625e0036558343b4e66143d3). The scheduler (when deadline scheduling is enabled) will choose the next expiring thread when selecting between threads at the same static priority. Threads at different priorities will be scheduled according to their static priority.

        Note

        Deadlines are stored internally using 32 bit unsigned integers. The number of cycles between the “first” deadline in the scheduler queue and the “last” deadline must be less than 2^31 (i.e a signed non-negative quantity). Failure to adhere to this rule may result in scheduled threads running in an incorrect deadline order.

        Note

        Despite the API naming, the scheduler makes no guarantees the thread WILL be scheduled within that deadline, nor does it take extra metadata (like e.g. the “runtime” and “period” parameters in Linux sched\_setattr()) that allows the kernel to validate the scheduling for achievability. Such features could be implemented above this call, which is simply input to the priority selection logic.

        Note

        You should enable  [`CONFIG_SCHED_DEADLINE`](../../../kconfig.md#CONFIG_SCHED_DEADLINE "CONFIG_SCHED_DEADLINE") in your project configuration.

        Parameters:
        :   - **thread** – A thread on which to set the deadline
            - **deadline** – A time delta, in cycle units

    int k\_thread\_cpu\_mask\_clear(k\_tid\_t thread)
    :   Sets all CPU enable masks to zero.

        After this returns, the thread will no longer be schedulable on any CPUs. The thread must not be currently runnable.

        Note

        You should enable  [`CONFIG_SCHED_CPU_MASK`](../../../kconfig.md#CONFIG_SCHED_CPU_MASK "CONFIG_SCHED_CPU_MASK") in your project configuration.

        Parameters:
        :   - **thread** – Thread to operate upon

        Returns:
        :   Zero on success, otherwise error code

    int k\_thread\_cpu\_mask\_enable\_all(k\_tid\_t thread)
    :   Sets all CPU enable masks to one.

        After this returns, the thread will be schedulable on any CPU. The thread must not be currently runnable.

        Note

        You should enable  [`CONFIG_SCHED_CPU_MASK`](../../../kconfig.md#CONFIG_SCHED_CPU_MASK "CONFIG_SCHED_CPU_MASK") in your project configuration.

        Parameters:
        :   - **thread** – Thread to operate upon

        Returns:
        :   Zero on success, otherwise error code

    int k\_thread\_cpu\_mask\_enable(k\_tid\_t thread, int cpu)
    :   Enable thread to run on specified CPU.

        The thread must not be currently runnable.

        Note

        You should enable  [`CONFIG_SCHED_CPU_MASK`](../../../kconfig.md#CONFIG_SCHED_CPU_MASK "CONFIG_SCHED_CPU_MASK") in your project configuration.

        Parameters:
        :   - **thread** – Thread to operate upon
            - **cpu** – CPU index

        Returns:
        :   Zero on success, otherwise error code

    int k\_thread\_cpu\_mask\_disable(k\_tid\_t thread, int cpu)
    :   Prevent thread to run on specified CPU.

        The thread must not be currently runnable.

        Note

        You should enable  [`CONFIG_SCHED_CPU_MASK`](../../../kconfig.md#CONFIG_SCHED_CPU_MASK "CONFIG_SCHED_CPU_MASK") in your project configuration.

        Parameters:
        :   - **thread** – Thread to operate upon
            - **cpu** – CPU index

        Returns:
        :   Zero on success, otherwise error code

    int k\_thread\_cpu\_pin(k\_tid\_t thread, int cpu)
    :   Pin a thread to a CPU.

        Pin a thread to a CPU by first clearing the cpu mask and then enabling the thread on the selected CPU.

        Parameters:
        :   - **thread** – Thread to operate upon
            - **cpu** – CPU index

        Returns:
        :   Zero on success, otherwise error code

    void k\_thread\_suspend(k\_tid\_t thread)
    :   Suspend a thread.

        This routine prevents the kernel scheduler from making *thread* the current thread. All other internal operations on *thread* are still performed; for example, kernel objects it is waiting on are still handed to it. Note that any existing timeouts (e.g. [k\_sleep()](#group__thread__apis_1ga48d4b041790454da4d68ac8711f29657), or a timeout argument to [k\_sem\_take()](../synchronization/semaphores.md#group__semaphore__apis_1gac71e2383c1920dddc45a561cacfef090) et. al.) will be canceled. On resume, the thread will begin running immediately and return from the blocked call.

        When the target thread is active on another CPU, the caller will block until the target thread is halted (suspended or aborted). But if the caller is in an interrupt context, it will spin waiting for that target thread active on another CPU to halt.

        If *thread* is already suspended, the routine has no effect.

        Parameters:
        :   - **thread** – ID of thread to suspend.

    void k\_thread\_resume(k\_tid\_t thread)
    :   Resume a suspended thread.

        This routine allows the kernel scheduler to make *thread* the current thread, when it is next eligible for that role.

        If *thread* is not currently suspended, the routine has no effect.

        Parameters:
        :   - **thread** – ID of thread to resume.

    void k\_sched\_time\_slice\_set(int32\_t slice, int prio)
    :   Set time-slicing period and scope.

        This routine specifies how the scheduler will perform time slicing of preemptible threads.

        To enable time slicing, *slice* must be non-zero. The scheduler ensures that no thread runs for more than the specified time limit before other threads of that priority are given a chance to execute. Any thread whose priority is higher than *prio* is exempted, and may execute as long as desired without being preempted due to time slicing.

        Time slicing only limits the maximum amount of time a thread may continuously execute. Once the scheduler selects a thread for execution, there is no minimum guaranteed time the thread will execute before threads of greater or equal priority are scheduled.

        When the current thread is the only one of that priority eligible for execution, this routine has no effect; the thread is immediately rescheduled after the slice period expires.

        To disable timeslicing, set both *slice* and *prio* to zero.

        Parameters:
        :   - **slice** – Maximum time slice length (in milliseconds).
            - **prio** – Highest thread priority level eligible for time slicing.

    void k\_thread\_time\_slice\_set(struct [k\_thread](#c.k_thread) \*th, int32\_t slice\_ticks, k\_thread\_timeslice\_fn\_t expired, void \*data)
    :   Set thread time slice.

        As for k\_sched\_time\_slice\_set, but (when CONFIG\_TIMESLICE\_PER\_THREAD=y) sets the timeslice for a specific thread. When non-zero, this timeslice will take precedence over the global value.

        When such a thread’s timeslice expires, the configured callback will be called before the thread is removed/re-added to the run queue. This callback will occur in interrupt context, and the specified thread is guaranteed to have been preempted by the currently-executing ISR. Such a callback is free to, for example, modify the thread priority or slice time for future execution, suspend the thread, etc…

        Note

        Unlike the older API, the time slice parameter here is specified in ticks, not milliseconds. Ticks have always been the internal unit, and not all platforms have integer conversions between the two.

        Note

        Threads with a non-zero slice time set will be timesliced always, even if they are higher priority than the maximum timeslice priority set via [k\_sched\_time\_slice\_set()](#group__thread__apis_1ga877c1bfeffbf8f097d1656f9e10a66e8).

        Note

        The callback notification for slice expiration happens, as it must, while the thread is still “current”, and thus it happens before any registered timeouts at this tick. This has the somewhat confusing side effect that the tick time (c.f. [k\_uptime\_get()](../timing/clocks.md#group__clock__apis_1gae3e992cd3257c23d5b26d765fcbb2b69)) does not yet reflect the expired ticks. Applications wishing to make fine-grained timing decisions within this callback should use the cycle API, or derived facilities like k\_thread\_runtime\_stats\_get().

        Parameters:
        :   - **th** – A valid, initialized thread
            - **slice\_ticks** – Maximum timeslice, in ticks
            - **expired** – Callback function called on slice expiration
            - **data** – Parameter for the expiration handler

    void k\_sched\_lock(void)
    :   Lock the scheduler.

        This routine prevents the current thread from being preempted by another thread by instructing the scheduler to treat it as a cooperative thread. If the thread subsequently performs an operation that makes it unready, it will be context switched out in the normal manner. When the thread again becomes the current thread, its non-preemptible status is maintained.

        This routine can be called recursively.

        Owing to clever implementation details, scheduler locks are extremely fast for non-userspace threads (just one byte inc/decrement in the thread struct).

        Note

        This works by elevating the thread priority temporarily to a cooperative priority, allowing cheap synchronization vs. other preemptible or cooperative threads running on the current CPU. It does not prevent preemption or asynchrony of other types. It does not prevent threads from running on other CPUs when CONFIG\_SMP=y. It does not prevent interrupts from happening, nor does it prevent threads with MetaIRQ priorities from preempting the current thread. In general this is a historical API not well-suited to modern applications, use with care.

    void k\_sched\_unlock(void)
    :   Unlock the scheduler.

        This routine reverses the effect of a previous call to [k\_sched\_lock()](#group__thread__apis_1ga4f0c5d0b9f279b12a4ad97db0c116a5f). A thread must call the routine once for each time it called [k\_sched\_lock()](#group__thread__apis_1ga4f0c5d0b9f279b12a4ad97db0c116a5f) before the thread becomes preemptible.

    void k\_thread\_custom\_data\_set(void \*value)
    :   Set current thread’s custom data.

        This routine sets the custom data for the current thread to @ value.

        Custom data is not used by the kernel itself, and is freely available for a thread to use as it sees fit. It can be used as a framework upon which to build thread-local storage.

        Parameters:
        :   - **value** – New custom data value.

    void \*k\_thread\_custom\_data\_get(void)
    :   Get current thread’s custom data.

        This routine returns the custom data for the current thread.

        Returns:
        :   Current custom data value.

    int k\_thread\_name\_set(k\_tid\_t thread, const char \*str)
    :   Set current thread name.

        Set the name of the thread to be used when  [`CONFIG_THREAD_MONITOR`](../../../kconfig.md#CONFIG_THREAD_MONITOR "CONFIG_THREAD_MONITOR") is enabled for tracing and debugging.

        Parameters:
        :   - **thread** – Thread to set name, or NULL to set the current thread
            - **str** – Name string

        Return values:
        :   - **0** – on success
            - **-EFAULT** – Memory access error with supplied string
            - **-ENOSYS** – Thread name configuration option not enabled
            - **-EINVAL** – Thread name too long

    const char \*k\_thread\_name\_get(k\_tid\_t thread)
    :   Get thread name.

        Get the name of a thread

        Parameters:
        :   - **thread** – Thread ID

        Return values:
        :   **Thread** – name, or NULL if configuration not enabled

    int k\_thread\_name\_copy(k\_tid\_t thread, char \*buf, size\_t size)
    :   Copy the thread name into a supplied buffer.

        Parameters:
        :   - **thread** – Thread to obtain name information
            - **buf** – Destination buffer
            - **size** – Destination buffer size

        Return values:
        :   - **-ENOSPC** – Destination buffer too small
            - **-EFAULT** – Memory access error
            - **-ENOSYS** – Thread name feature not enabled
            - **0** – Success

    const char \*k\_thread\_state\_str(k\_tid\_t thread\_id, char \*buf, size\_t buf\_size)
    :   Get thread state string.

        This routine generates a human friendly string containing the thread’s state, and copies as much of it as possible into *buf*.

        Parameters:
        :   - **thread\_id** – Thread ID
            - **buf** – Buffer into which to copy state strings
            - **buf\_size** – Size of the buffer

        Return values:
        :   **Pointer** – to *buf* if data was copied, else a pointer to “”.

    struct k\_thread
    :   *#include <thread.h>*

        Thread Structure.

        Public Members

        struct \_callee\_saved callee\_saved
        :   defined by the architecture, but all archs need these

        void \*init\_data
        :   static thread init data

        \_wait\_q\_t join\_queue
        :   threads waiting in [k\_thread\_join()](#group__thread__apis_1ga40a733561eb1f64dcaae0e01b167d233)

        struct \_\_thread\_entry entry
        :   thread entry and parameters description

        struct [k\_thread](#c.k_thread) \*next\_thread
        :   next item in list of all threads

        void \*custom\_data
        :   crude thread-local storage

        struct \_thread\_stack\_info stack\_info
        :   Stack Info.

        struct \_mem\_domain\_info mem\_domain\_info
        :   memory domain info of the thread

        k\_thread\_stack\_t \*stack\_obj
        :   Base address of thread stack.

            If memory mapped stack (CONFIG\_THREAD\_STACK\_MEM\_MAPPED) is enabled, this is the physical address of the stack.

        void \*syscall\_frame
        :   current syscall frame pointer

        int swap\_retval
        :   z\_swap() return value

        void \*switch\_handle
        :   Context handle returned via [arch\_switch()](../../../hardware/porting/arch.md#group__arch-threads_1gab411d82ce5b60f062171f5a19e33e025).

        struct [k\_heap](../../memory_management/heap.md#c.k_heap "k_heap") \*resource\_pool
        :   resource pool

        \_wait\_q\_t halt\_queue
        :   threads waiting in [k\_thread\_suspend()](#group__thread__apis_1ga66cf8682fb65870eceb5e57d667a8d4e)

        struct \_thread\_arch arch
        :   arch-specifics: must always be at the end

*group* Thread Stack APIs
:   Thread Stack APIs.

    Defines

    K\_KERNEL\_STACK\_DECLARE(sym, size)
    :   Declare a reference to a thread stack.

        This macro declares the symbol of a thread stack defined elsewhere in the current scope.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **size** – Size of the stack memory region

    K\_KERNEL\_STACK\_ARRAY\_DECLARE(sym, nmemb, size)
    :   Declare a reference to a thread stack array.

        This macro declares the symbol of a thread stack array defined elsewhere in the current scope.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **nmemb** – Number of stacks defined
            - **size** – Size of the stack memory region

    K\_KERNEL\_PINNED\_STACK\_ARRAY\_DECLARE(sym, nmemb, size)
    :   Declare a reference to a pinned thread stack array.

        This macro declares the symbol of a pinned thread stack array defined elsewhere in the current scope.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **nmemb** – Number of stacks defined
            - **size** – Size of the stack memory region

    K\_KERNEL\_STACK\_DEFINE(sym, size)
    :   Define a toplevel kernel stack memory region.

        This defines a region of memory for use as a thread stack, for threads that exclusively run in supervisor mode. This is also suitable for declaring special stacks for interrupt or exception handling.

        Stacks defined with this macro may not host user mode threads.

        It is legal to precede this definition with the ‘static’ keyword.

        It is NOT legal to take the sizeof(sym) and pass that to the stackSize parameter of [k\_thread\_create()](#group__thread__apis_1gad5b0bff3102f1656089f5875d999a367), it may not be the same as the ‘size’ parameter. Use [K\_KERNEL\_STACK\_SIZEOF()](#group__thread__stack__api_1ga57b3824b117c634dbb6052d47dc4301c) instead.

        The total amount of memory allocated may be increased to accommodate fixed-size stack overflow guards.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **size** – Size of the stack memory region

    K\_KERNEL\_PINNED\_STACK\_DEFINE(sym, size)
    :   Define a toplevel kernel stack memory region in pinned section.

        See [K\_KERNEL\_STACK\_DEFINE()](#group__thread__stack__api_1ga9e05e3cb5aa5b72d6f19e2f327313271) for more information and constraints.

        This puts the stack into the pinned noinit linker section if CONFIG\_LINKER\_USE\_PINNED\_SECTION is enabled, or else it would put the stack into the same section as [K\_KERNEL\_STACK\_DEFINE()](#group__thread__stack__api_1ga9e05e3cb5aa5b72d6f19e2f327313271).

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **size** – Size of the stack memory region

    K\_KERNEL\_STACK\_ARRAY\_DEFINE(sym, nmemb, size)
    :   Define a toplevel array of kernel stack memory regions.

        Stacks defined with this macro may not host user mode threads.

        Parameters:
        :   - **sym** – Kernel stack array symbol name
            - **nmemb** – Number of stacks to define
            - **size** – Size of the stack memory region

    K\_KERNEL\_PINNED\_STACK\_ARRAY\_DEFINE(sym, nmemb, size)
    :   Define a toplevel array of kernel stack memory regions in pinned section.

        See [K\_KERNEL\_STACK\_ARRAY\_DEFINE()](#group__thread__stack__api_1gaf05127bd2ab7e8a0aeb394f18cbd923a) for more information and constraints.

        This puts the stack into the pinned noinit linker section if CONFIG\_LINKER\_USE\_PINNED\_SECTION is enabled, or else it would put the stack into the same section as [K\_KERNEL\_STACK\_ARRAY\_DEFINE()](#group__thread__stack__api_1gaf05127bd2ab7e8a0aeb394f18cbd923a).

        Parameters:
        :   - **sym** – Kernel stack array symbol name
            - **nmemb** – Number of stacks to define
            - **size** – Size of the stack memory region

    K\_KERNEL\_STACK\_MEMBER(sym, size)
    :   Define an embedded stack memory region.

        Used for kernel stacks embedded within other data structures.

        Stacks defined with this macro may not host user mode threads.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **size** – Size of the stack memory region

    K\_KERNEL\_STACK\_SIZEOF(sym)

    K\_THREAD\_STACK\_DECLARE(sym, size)
    :   Declare a reference to a thread stack.

        This macro declares the symbol of a thread stack defined elsewhere in the current scope.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **size** – Size of the stack memory region

    K\_THREAD\_STACK\_ARRAY\_DECLARE(sym, nmemb, size)
    :   Declare a reference to a thread stack array.

        This macro declares the symbol of a thread stack array defined elsewhere in the current scope.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **nmemb** – Number of stacks defined
            - **size** – Size of the stack memory region

    K\_THREAD\_STACK\_SIZEOF(sym)
    :   Return the size in bytes of a stack memory region.

        Convenience macro for passing the desired stack size to [k\_thread\_create()](#group__thread__apis_1gad5b0bff3102f1656089f5875d999a367) since the underlying implementation may actually create something larger (for instance a guard area).

        The value returned here is not guaranteed to match the ‘size’ parameter passed to K\_THREAD\_STACK\_DEFINE and may be larger, but is always safe to pass to [k\_thread\_create()](#group__thread__apis_1gad5b0bff3102f1656089f5875d999a367) for the associated stack object.

        Parameters:
        :   - **sym** – Stack memory symbol

        Returns:
        :   Size of the stack buffer

    K\_THREAD\_STACK\_DEFINE(sym, size)
    :   Define a toplevel thread stack memory region.

        This defines a region of memory suitable for use as a thread’s stack.

        This is the generic, historical definition. Align to Z\_THREAD\_STACK\_OBJ\_ALIGN and put in ‘noinit’ section so that it isn’t zeroed at boot

        The defined symbol will always be a k\_thread\_stack\_t which can be passed to [k\_thread\_create()](#group__thread__apis_1gad5b0bff3102f1656089f5875d999a367), but should otherwise not be manipulated. If the buffer inside needs to be examined, examine thread->stack\_info for the associated thread object to obtain the boundaries.

        It is legal to precede this definition with the ‘static’ keyword.

        It is NOT legal to take the sizeof(sym) and pass that to the stackSize parameter of [k\_thread\_create()](#group__thread__apis_1gad5b0bff3102f1656089f5875d999a367), it may not be the same as the ‘size’ parameter. Use [K\_THREAD\_STACK\_SIZEOF()](#group__thread__stack__api_1ga775f8e6b4144cfdd24f3261b6db64150) instead.

        Some arches may round the size of the usable stack region up to satisfy alignment constraints. [K\_THREAD\_STACK\_SIZEOF()](#group__thread__stack__api_1ga775f8e6b4144cfdd24f3261b6db64150) will return the aligned size.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **size** – Size of the stack memory region

    K\_THREAD\_PINNED\_STACK\_DEFINE(sym, size)
    :   Define a toplevel thread stack memory region in pinned section.

        This defines a region of memory suitable for use as a thread’s stack.

        This is the generic, historical definition. Align to Z\_THREAD\_STACK\_OBJ\_ALIGN and put in ‘noinit’ section so that it isn’t zeroed at boot

        The defined symbol will always be a k\_thread\_stack\_t which can be passed to [k\_thread\_create()](#group__thread__apis_1gad5b0bff3102f1656089f5875d999a367), but should otherwise not be manipulated. If the buffer inside needs to be examined, examine thread->stack\_info for the associated thread object to obtain the boundaries.

        It is legal to precede this definition with the ‘static’ keyword.

        It is NOT legal to take the sizeof(sym) and pass that to the stackSize parameter of [k\_thread\_create()](#group__thread__apis_1gad5b0bff3102f1656089f5875d999a367), it may not be the same as the ‘size’ parameter. Use [K\_THREAD\_STACK\_SIZEOF()](#group__thread__stack__api_1ga775f8e6b4144cfdd24f3261b6db64150) instead.

        Some arches may round the size of the usable stack region up to satisfy alignment constraints. [K\_THREAD\_STACK\_SIZEOF()](#group__thread__stack__api_1ga775f8e6b4144cfdd24f3261b6db64150) will return the aligned size.

        This puts the stack into the pinned noinit linker section if CONFIG\_LINKER\_USE\_PINNED\_SECTION is enabled, or else it would put the stack into the same section as [K\_THREAD\_STACK\_DEFINE()](#group__thread__stack__api_1gac5368ce24fdeab3863b5c8dee2ebd955).

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **size** – Size of the stack memory region

    K\_THREAD\_STACK\_LEN(size)
    :   Calculate size of stacks to be allocated in a stack array.

        This macro calculates the size to be allocated for the stacks inside a stack array. It accepts the indicated “size” as a parameter and if required, pads some extra bytes (e.g. for MPU scenarios). Refer K\_THREAD\_STACK\_ARRAY\_DEFINE definition to see how this is used. The returned size ensures each array member will be aligned to the required stack base alignment.

        Parameters:
        :   - **size** – Size of the stack memory region

        Returns:
        :   Appropriate size for an array member

    K\_THREAD\_STACK\_ARRAY\_DEFINE(sym, nmemb, size)
    :   Define a toplevel array of thread stack memory regions.

        Create an array of equally sized stacks. See K\_THREAD\_STACK\_DEFINE definition for additional details and constraints.

        This is the generic, historical definition. Align to Z\_THREAD\_STACK\_OBJ\_ALIGN and put in ‘noinit’ section so that it isn’t zeroed at boot

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **nmemb** – Number of stacks to define
            - **size** – Size of the stack memory region

    K\_THREAD\_PINNED\_STACK\_ARRAY\_DEFINE(sym, nmemb, size)
    :   Define a toplevel array of thread stack memory regions in pinned section.

        Create an array of equally sized stacks. See K\_THREAD\_STACK\_DEFINE definition for additional details and constraints.

        This is the generic, historical definition. Align to Z\_THREAD\_STACK\_OBJ\_ALIGN and put in ‘noinit’ section so that it isn’t zeroed at boot

        This puts the stack into the pinned noinit linker section if CONFIG\_LINKER\_USE\_PINNED\_SECTION is enabled, or else it would put the stack into the same section as [K\_THREAD\_STACK\_DEFINE()](#group__thread__stack__api_1gac5368ce24fdeab3863b5c8dee2ebd955).

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **nmemb** – Number of stacks to define
            - **size** – Size of the stack memory region

    K\_THREAD\_STACK\_MEMBER(sym, size)
    :   Define an embedded stack memory region.

        Used for stacks embedded within other data structures. Use is highly discouraged but in some cases necessary. For memory protection scenarios, it is very important that any RAM preceding this member not be writable by threads else a stack overflow will lead to silent corruption. In other words, the containing data structure should live in RAM owned by the kernel.

        A user thread can only be started with a stack defined in this way if the thread starting it is in supervisor mode.

        *Deprecated:*
        :   This is now deprecated, as stacks defined in this way are not usable from user mode. Use K\_KERNEL\_STACK\_MEMBER.

        Parameters:
        :   - **sym** – Thread stack symbol name
            - **size** – Size of the stack memory region
