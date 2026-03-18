---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/services/smp/smp.html
original_path: kernel/services/smp/smp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Symmetric Multiprocessing

On multiprocessor architectures, Zephyr supports the use of multiple
physical CPUs running Zephyr application code. This support is
“symmetric” in the sense that no specific CPU is treated specially by
default. Any processor is capable of running any Zephyr thread, with
access to all standard Zephyr APIs supported.

No special application code needs to be written to take advantage of
this feature. If there are two Zephyr application threads runnable on
a supported dual processor device, they will both run simultaneously.

SMP configuration is controlled under the [`CONFIG_SMP`](../../../kconfig.md#CONFIG_SMP "CONFIG_SMP") kconfig
variable. This must be set to “y” to enable SMP features, otherwise
a uniprocessor kernel will be built. In general the platform default
will have enabled this anywhere it’s supported. When enabled, the
number of physical CPUs available is visible at build time as
[`CONFIG_MP_MAX_NUM_CPUS`](../../../kconfig.md#CONFIG_MP_MAX_NUM_CPUS "CONFIG_MP_MAX_NUM_CPUS"). Likewise, the default for this will be the
number of available CPUs on the platform and it is not expected that
typical apps will change it. But it is legal and supported to set
this to a smaller (but obviously not larger) number for special
purposes (e.g. for testing, or to reserve a physical CPU for running
non-Zephyr code).

## Synchronization

At the application level, core Zephyr IPC and synchronization
primitives all behave identically under an SMP kernel. For example
semaphores used to implement blocking mutual exclusion continue to be
a proper application choice.

At the lowest level, however, Zephyr code has often used the
[`irq_lock()`](../interrupts.md#c.irq_lock "irq_lock")/[`irq_unlock()`](../interrupts.md#c.irq_unlock "irq_unlock") primitives to implement fine grained
critical sections using interrupt masking. These APIs continue to
work via an emulation layer (see below), but the masking technique
does not: the fact that your CPU will not be interrupted while you are
in your critical section says nothing about whether a different CPU
will be running simultaneously and be inspecting or modifying the same
data!

### Spinlocks

SMP systems provide a more constrained [`k_spin_lock()`](#c.k_spin_lock) primitive
that not only masks interrupts locally, as done by [`irq_lock()`](../interrupts.md#c.irq_lock "irq_lock"), but
also atomically validates that a shared lock variable has been
modified before returning to the caller, “spinning” on the check if
needed to wait for the other CPU to exit the lock. The default Zephyr
implementation of [`k_spin_lock()`](#c.k_spin_lock) and [`k_spin_unlock()`](#c.k_spin_unlock) is built
on top of the pre-existing `atomic_` layer (itself usually
implemented using compiler intrinsics), though facilities exist for
architectures to define their own for performance reasons.

One important difference between IRQ locks and spinlocks is that the
earlier API was naturally recursive: the lock was global, so it was
legal to acquire a nested lock inside of a critical section.
Spinlocks are separable: you can have many locks for separate
subsystems or data structures, preventing CPUs from contending on a
single global resource. But that means that spinlocks must not be
used recursively. Code that holds a specific lock must not try to
re-acquire it or it will deadlock (it is perfectly legal to nest
**distinct** spinlocks, however). A validation layer is available to
detect and report bugs like this.

When used on a uniprocessor system, the data component of the spinlock
(the atomic lock variable) is unnecessary and elided. Except for the
recursive semantics above, spinlocks in single-CPU contexts produce
identical code to legacy IRQ locks. In fact the entirety of the
Zephyr core kernel has now been ported to use spinlocks exclusively.

### Legacy irq\_lock() emulation

For the benefit of applications written to the uniprocessor locking
API, [`irq_lock()`](../interrupts.md#c.irq_lock "irq_lock") and [`irq_unlock()`](../interrupts.md#c.irq_unlock "irq_unlock") continue to work compatibly on
SMP systems with identical semantics to their legacy versions. They
are implemented as a single global spinlock, with a nesting count and
the ability to be atomically reacquired on context switch into locked
threads. The kernel will ensure that only one thread across all CPUs
can hold the lock at any time, that it is released on context switch,
and that it is re-acquired when necessary to restore the lock state
when a thread is switched in. Other CPUs will spin waiting for the
release to happen.

The overhead involved in this process has measurable performance
impact, however. Unlike uniprocessor apps, SMP apps using
[`irq_lock()`](../interrupts.md#c.irq_lock "irq_lock") are not simply invoking a very short (often ~1
instruction) interrupt masking operation. That, and the fact that the
IRQ lock is global, means that code expecting to be run in an SMP
context should be using the spinlock API wherever possible.

## CPU Mask

It is often desirable for real time applications to deliberately
partition work across physical CPUs instead of relying solely on the
kernel scheduler to decide on which threads to execute. Zephyr
provides an API, controlled by the [`CONFIG_SCHED_CPU_MASK`](../../../kconfig.md#CONFIG_SCHED_CPU_MASK "CONFIG_SCHED_CPU_MASK")
kconfig variable, which can associate a specific set of CPUs with each
thread, indicating on which CPUs it can run.

By default, new threads can run on any CPU. Calling
[`k_thread_cpu_mask_disable()`](../threads/index.md#c.k_thread_cpu_mask_disable "k_thread_cpu_mask_disable") with a particular CPU ID will prevent
that thread from running on that CPU in the future. Likewise
[`k_thread_cpu_mask_enable()`](../threads/index.md#c.k_thread_cpu_mask_enable "k_thread_cpu_mask_enable") will re-enable execution. There are also
[`k_thread_cpu_mask_clear()`](../threads/index.md#c.k_thread_cpu_mask_clear "k_thread_cpu_mask_clear") and [`k_thread_cpu_mask_enable_all()`](../threads/index.md#c.k_thread_cpu_mask_enable_all "k_thread_cpu_mask_enable_all") APIs
available for convenience. For obvious reasons, these APIs are
illegal if called on a runnable thread. The thread must be blocked or
suspended, otherwise an `-EINVAL` will be returned.

Note that when this feature is enabled, the scheduler algorithm
involved in doing the per-CPU mask test requires that the list be
traversed in full. The kernel does not keep a per-CPU run queue.
That means that the performance benefits from the
[`CONFIG_SCHED_SCALABLE`](../../../kconfig.md#CONFIG_SCHED_SCALABLE "CONFIG_SCHED_SCALABLE") and [`CONFIG_SCHED_MULTIQ`](../../../kconfig.md#CONFIG_SCHED_MULTIQ "CONFIG_SCHED_MULTIQ")
scheduler backends cannot be realized. CPU mask processing is
available only when [`CONFIG_SCHED_DUMB`](../../../kconfig.md#CONFIG_SCHED_DUMB "CONFIG_SCHED_DUMB") is the selected
backend. This requirement is enforced in the configuration layer.

## SMP Boot Process

A Zephyr SMP kernel begins boot identically to a uniprocessor kernel.
Auxiliary CPUs begin in a disabled state in the architecture layer.
All standard kernel initialization, including device initialization,
happens on a single CPU before other CPUs are brought online.

Just before entering the application `main()` function, the kernel
calls `z_smp_init()` to launch the SMP initialization process. This
enumerates over the configured CPUs, calling into the architecture
layer using [`arch_cpu_start()`](../../../hardware/porting/arch.md#c.arch_cpu_start "arch_cpu_start") for each one. This function is
passed a memory region to use as a stack on the foreign CPU (in
practice it uses the area that will become that CPU’s interrupt
stack), the address of a local `smp_init_top()` callback function to
run on that CPU, and a pointer to a “start flag” address which will be
used as an atomic signal.

The local SMP initialization (`smp_init_top()`) on each CPU is then
invoked by the architecture layer. Note that interrupts are still
masked at this point. This routine is responsible for calling
`smp_timer_init()` to set up any needed stat in the timer driver. On
many architectures the timer is a per-CPU device and needs to be
configured specially on auxiliary CPUs. Then it waits (spinning) for
the atomic “start flag” to be released in the main thread, to
guarantee that all SMP initialization is complete before any Zephyr
application code runs, and finally calls `z_swap()` to transfer
control to the appropriate runnable thread via the standard scheduler
API.

![SMP Initialization](../../../_images/smpinit.svg)

Example SMP initialization process, showing a configuration with
two CPUs and two app threads which begin operating simultaneously.

## Interprocessor Interrupts

When running in multiprocessor environments, it is occasionally the
case that state modified on the local CPU needs to be synchronously
handled on a different processor.

One example is the Zephyr [`k_thread_abort()`](../threads/index.md#c.k_thread_abort "k_thread_abort") API, which cannot return
until the thread that had been aborted is no longer runnable. If it
is currently running on another CPU, that becomes difficult to
implement.

Another is low power idle. It is a firm requirement on many devices
that system idle be implemented using a low-power mode with as many
interrupts (including periodic timer interrupts) disabled or deferred
as is possible. If a CPU is in such a state, and on another CPU a
thread becomes runnable, the idle CPU has no way to “wake up” to
handle the newly-runnable load.

So where possible, Zephyr SMP architectures should implement an
interprocessor interrupt. The current framework is very simple: the
architecture provides at least a [`arch_sched_broadcast_ipi()`](../../../hardware/porting/arch.md#c.arch_sched_broadcast_ipi "arch_sched_broadcast_ipi") call,
which when invoked will flag an interrupt on all CPUs (except the current one,
though that is allowed behavior). If the architecture supports directed IPIs
(see [`CONFIG_ARCH_HAS_DIRECTED_IPIS`](../../../kconfig.md#CONFIG_ARCH_HAS_DIRECTED_IPIS "CONFIG_ARCH_HAS_DIRECTED_IPIS")), then the
architecture also provides a [`arch_sched_directed_ipi()`](../../../hardware/porting/arch.md#c.arch_sched_directed_ipi "arch_sched_directed_ipi") call, which
when invoked will flag an interrupt on the specified CPUs. When an interrupt is
flagged on the CPUs, the `z_sched_ipi()` function implemented in the
scheduler will get invoked on those CPUs. The expectation is that these
APIs will evolve over time to encompass more functionality (e.g. cross-CPU
calls), and that the scheduler-specific calls here will be implemented in
terms of a more general framework.

Note that not all SMP architectures will have a usable IPI mechanism
(either missing, or just undocumented/unimplemented). In those cases
Zephyr provides fallback behavior that is correct, but perhaps
suboptimal.

Using this, [`k_thread_abort()`](../threads/index.md#c.k_thread_abort "k_thread_abort") becomes only slightly more
complicated in SMP: for the case where a thread is actually running on
another CPU (we can detect this atomically inside the scheduler), we
broadcast an IPI and spin, waiting for the thread to either become
“DEAD” or for it to re-enter the queue (in which case we terminate it
the same way we would have in uniprocessor mode). Note that the
“aborted” check happens on any interrupt exit, so there is no special
handling needed in the IPI per se. This allows us to implement a
reasonable fallback when IPI is not available: we can simply spin,
waiting until the foreign CPU receives any interrupt, though this may
be a much longer time!

Likewise idle wakeups are trivially implementable with an empty IPI
handler. If a thread is added to an empty run queue (i.e. there may
have been idle CPUs), we broadcast an IPI. A foreign CPU will then be
able to see the new thread when exiting from the interrupt and will
switch to it if available.

Without an IPI, however, a low power idle that requires an interrupt
will not work to synchronously run new threads. The workaround in
that case is more invasive: Zephyr will **not** enter the system idle
handler and will instead spin in its idle loop, testing the scheduler
state at high frequency (not spinning on it though, as that would
involve severe lock contention) for new threads. The expectation is
that power constrained SMP applications are always going to provide an
IPI, and this code will only be used for testing purposes or on
systems without power consumption requirements.

### IPI Cascades

The kernel can not control the order in which IPIs are processed by the CPUs
in the system. In general, this is not an issue and a single set of IPIs is
sufficient to trigger a reschedule on the N CPUs that results with them
scheduling the highest N priority ready threads to execute. When CPU masking
is used, there may be more than one valid set of threads (not to be confused
with an optimal set of threads) that can be scheduled on the N CPUs and a
single set of IPIs may be insufficient to result in any of these valid sets.

Note

When CPU masking is not in play, the optimal set of threads is the same
as the valid set of threads. However when CPU masking is in play, there
may be more than one valid set–one of which may be optimal.

To better illustrate the distinction, consider a 2-CPU system with ready
threads T1 and T2 at priorities 1 and 2 respectively. Let T2 be pinned to
CPU0 and T1 not be pinned. If CPU0 is executing T2 and CPU1 executing T1,
then this set is is both valid and optimal. However, if CPU0 is executing
T1 and CPU1 is idling, then this too would be valid though not optimal.

In those cases where a single set of IPIs is not sufficient to generate a valid
set, the resulting set of executing threads are expected to be close to a valid
set, and subsequent IPIs can generally be expected to correct the situation
soon. However, for cases where neither the approximation nor the delay are
acceptable, enabling [`CONFIG_SCHED_IPI_CASCADE`](../../../kconfig.md#CONFIG_SCHED_IPI_CASCADE "CONFIG_SCHED_IPI_CASCADE") will allow the
kernel to generate cascading IPIs until the kernel has selected a valid set of
ready threads for the CPUs.

There are three types of costs/penalties associated with the IPI cascades–and
for these reasons they are disabled by default. The first is a cost incurred
by the CPU producing the IPI when a new thread preempts the old thread as checks
must be done to compare the old thread against the threads executing on the
other CPUs. The second is a cost incurred by the CPUs receiving the IPIs as
they must be processed. The third is the apparent sputtering of a thread as it
“winks in” and then “winks out” due to cascades stemming from the
aforementioned first cost.

## SMP Kernel Internals

In general, Zephyr kernel code is SMP-agnostic and, like application
code, will work correctly regardless of the number of CPUs available.
But in a few areas there are notable changes in structure or behavior.

### Per-CPU data

Many elements of the core kernel data need to be implemented for each
CPU in SMP mode. For example, the `_current` thread pointer obviously
needs to reflect what is running locally, there are many threads
running concurrently. Likewise a kernel-provided interrupt stack
needs to be created and assigned for each physical CPU, as does the
interrupt nesting count used to detect ISR state.

These fields are now moved into a separate struct `_cpu` instance
within the `_kernel` struct, which has a `cpus[]` array indexed by ID.
Compatibility fields are provided for legacy uniprocessor code trying
to access the fields of `cpus[0]` using the older syntax and assembly
offsets.

Note that an important requirement on the architecture layer is that
the pointer to this CPU struct be available rapidly when in kernel
context. The expectation is that [`arch_curr_cpu()`](../../../hardware/porting/arch.md#c.arch_curr_cpu "arch_curr_cpu") will be
implemented using a CPU-provided register or addressing mode that can
store this value across arbitrary context switches or interrupts and
make it available to any kernel-mode code.

Similarly, where on a uniprocessor system Zephyr could simply create a
global “idle thread” at the lowest priority, in SMP we may need one
for each CPU. This makes the internal predicate test for “\_is\_idle()”
in the scheduler, which is a hot path performance environment, more
complicated than simply testing the thread pointer for equality with a
known static variable. In SMP mode, idle threads are distinguished by
a separate field in the thread struct.

### Switch-based context switching

The traditional Zephyr context switch primitive has been `z_swap()`.
Unfortunately, this function takes no argument specifying a thread to
switch to. The expectation has always been that the scheduler has
already made its preemption decision when its state was last modified
and cached the resulting “next thread” pointer in a location where
architecture context switch primitives can find it via a simple struct
offset. That technique will not work in SMP, because the other CPU
may have modified scheduler state since the current CPU last exited
the scheduler (for example: it might already be running that cached
thread!).

Instead, the SMP “switch to” decision needs to be made synchronously
with the swap call, and as we don’t want per-architecture assembly
code to be handling scheduler internal state, Zephyr requires a
somewhat lower-level context switch primitives for SMP systems:
[`arch_switch()`](../../../hardware/porting/arch.md#c.arch_switch "arch_switch") is always called with interrupts masked, and takes
exactly two arguments. The first is an opaque (architecture defined)
handle to the context to which it should switch, and the second is a
pointer to such a handle into which it should store the handle
resulting from the thread that is being switched out.
The kernel then implements a portable `z_swap()` implementation on top
of this primitive which includes the relevant scheduler logic in a
location where the architecture doesn’t need to understand it.

Similarly, on interrupt exit, switch-based architectures are expected
to call `z_get_next_switch_handle()` to retrieve the next thread to
run from the scheduler. The argument to `z_get_next_switch_handle()`
is either the interrupted thread’s “handle” reflecting the same opaque type
used by [`arch_switch()`](../../../hardware/porting/arch.md#c.arch_switch "arch_switch"), or NULL if that thread cannot be released
to the scheduler just yet. The choice between a handle value or NULL
depends on the way CPU interrupt mode is implemented.

Architectures with a large CPU register file would typically preserve only
the caller-saved registers on the current thread’s stack when interrupted
in order to minimize interrupt latency, and preserve the callee-saved
registers only when [`arch_switch()`](../../../hardware/porting/arch.md#c.arch_switch "arch_switch") is called to minimize context
switching latency. Such architectures must use NULL as the argument to
`z_get_next_switch_handle()` to determine if there is a new thread
to schedule, and follow through with their own [`arch_switch()`](../../../hardware/porting/arch.md#c.arch_switch "arch_switch") or
derivative if so, or directly leave interrupt mode otherwise.
In the former case it is up to that switch code to store the handle
resulting from the thread that is being switched out in that thread’s
“switch\_handle” field after its context has fully been saved.

Architectures whose entry in interrupt mode already preserves the entire
thread state may pass that thread’s handle directly to
`z_get_next_switch_handle()` and be done in one step.

Note that while SMP requires [`CONFIG_USE_SWITCH`](../../../kconfig.md#CONFIG_USE_SWITCH "CONFIG_USE_SWITCH"), the reverse is not
true. A uniprocessor architecture built with [`CONFIG_SMP`](../../../kconfig.md#CONFIG_SMP "CONFIG_SMP") set to No might
still decide to implement its context switching using
[`arch_switch()`](../../../hardware/porting/arch.md#c.arch_switch "arch_switch").

## API Reference

*group* Spinlock APIs
:   Spinlock APIs.

    Defines

    K\_SPINLOCK\_BREAK
    :   Leaves a code block guarded with [K\_SPINLOCK](#group__spinlock__apis_1ga6d0db300193464dc4e603110e891f856) after releasing the lock.

        See [K\_SPINLOCK](#group__spinlock__apis_1ga6d0db300193464dc4e603110e891f856) for details.

    K\_SPINLOCK(lck)
    :   Guards a code block with the given spinlock, automatically acquiring the lock before executing the code block.

        The lock will be released either when reaching the end of the code block or when leaving the block with [K\_SPINLOCK\_BREAK](#group__spinlock__apis_1ga7b16542003f7eca7f5bcae5ba494f823).

        Example usage:

        ```c
        K_SPINLOCK(&mylock) {

          ...execute statements with the lock held...

          if (some_condition) {
            ...release the lock and leave the guarded section prematurely:
            K_SPINLOCK_BREAK;
          }

          ...execute statements with the lock held...

        }
        ```

        Behind the scenes this pattern expands to a for-loop whose body is executed exactly once:

        ```c
        for (k_spinlock_key_t key = k_spin_lock(&mylock); ...; k_spin_unlock(&mylock, key)) {
            ...
        }
        ```

        Note

        In user mode the spinlock must be placed in memory accessible to the application, see K\_APP\_DMEM and K\_APP\_BMEM macros for details.

        Warning

        The code block must execute to its end or be left by calling [K\_SPINLOCK\_BREAK](#group__spinlock__apis_1ga7b16542003f7eca7f5bcae5ba494f823). Otherwise, e.g. if exiting the block with a break, goto or return statement, the spinlock will not be released on exit.

        Parameters:
        :   - **lck** – Spinlock used to guard the enclosed code block.

    Typedefs

    typedef struct z\_spinlock\_key k\_spinlock\_key\_t
    :   Spinlock key type.

        This type defines a “key” value used by a spinlock implementation to store the system interrupt state at the time of a call to [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf). It is expected to be passed to a matching [k\_spin\_unlock()](#group__spinlock__apis_1gaa54fc60d17d1033276aed4605671ed8e).

        This type is opaque and should not be inspected by application code.

    Functions

    ALWAYS\_INLINE static [k\_spinlock\_key\_t](#c.k_spinlock_key_t) k\_spin\_lock(struct [k\_spinlock](#c.k_spinlock) \*l)
    :   Lock a spinlock.

        This routine locks the specified spinlock, returning a key handle representing interrupt state needed at unlock time. Upon returning, the calling thread is guaranteed not to be suspended or interrupted on its current CPU until it calls [k\_spin\_unlock()](#group__spinlock__apis_1gaa54fc60d17d1033276aed4605671ed8e). The implementation guarantees mutual exclusion: exactly one thread on one CPU will return from [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf) at a time. Other CPUs trying to acquire a lock already held by another CPU will enter an implementation-defined busy loop (“spinning”) until the lock is released.

        Separate spin locks may be nested. It is legal to lock an (unlocked) spin lock while holding a different lock. Spin locks are not recursive, however: an attempt to acquire a spin lock that the CPU already holds will deadlock.

        In circumstances where only one CPU exists, the behavior of [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf) remains as specified above, though obviously no spinning will take place. Implementations may be free to optimize in uniprocessor contexts such that the locking reduces to an interrupt mask operation.

        Parameters:
        :   - **l** – A pointer to the spinlock to lock

        Returns:
        :   A key value that must be passed to [k\_spin\_unlock()](#group__spinlock__apis_1gaa54fc60d17d1033276aed4605671ed8e) when the lock is released.

    ALWAYS\_INLINE static int k\_spin\_trylock(struct [k\_spinlock](#c.k_spinlock) \*l, [k\_spinlock\_key\_t](#c.k_spinlock_key_t) \*k)
    :   Attempt to lock a spinlock.

        This routine makes one attempt to lock `l`. If it is successful, then it will store the key into `k`.

        See also

        [k\_spin\_lock](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf)

        See also

        [k\_spin\_unlock](#group__spinlock__apis_1gaa54fc60d17d1033276aed4605671ed8e)

        Parameters:
        :   - **l** – **[in]** A pointer to the spinlock to lock
            - **k** – **[out]** A pointer to the spinlock key

        Return values:
        :   - **0** – on success
            - **-EBUSY** – if another thread holds the lock

    ALWAYS\_INLINE static void k\_spin\_unlock(struct [k\_spinlock](#c.k_spinlock) \*l, [k\_spinlock\_key\_t](#c.k_spinlock_key_t) key)
    :   Unlock a spin lock.

        This releases a lock acquired by [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf). After this function is called, any CPU will be able to acquire the lock. If other CPUs are currently spinning inside [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf) waiting for this lock, exactly one of them will return synchronously with the lock held.

        Spin locks must be properly nested. A call to [k\_spin\_unlock()](#group__spinlock__apis_1gaa54fc60d17d1033276aed4605671ed8e) must be made on the lock object most recently locked using [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf), using the key value that it returned. Attempts to unlock mis-nested locks, or to unlock locks that are not held, or to passing a key parameter other than the one returned from [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf), are illegal. When CONFIG\_SPIN\_VALIDATE is set, some of these errors can be detected by the framework.

        Parameters:
        :   - **l** – A pointer to the spinlock to release
            - **key** – The value returned from [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf) when this lock was acquired

    struct k\_spinlock
    :   *#include <spinlock.h>*

        Kernel Spin Lock.

        This struct defines a spin lock record on which CPUs can wait with [k\_spin\_lock()](#group__spinlock__apis_1gaac60da4347f5b29ff8c4e5f24c99b3bf). Any number of spinlocks may be defined in application code.
