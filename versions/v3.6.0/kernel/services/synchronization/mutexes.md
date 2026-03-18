---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/synchronization/mutexes.html
original_path: kernel/services/synchronization/mutexes.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Mutexes

A *mutex* is a kernel object that implements a traditional
reentrant mutex. A mutex allows multiple threads to safely share
an associated hardware or software resource by ensuring mutually exclusive
access to the resource.

## [Concepts](#id1)

Any number of mutexes can be defined (limited only by available RAM). Each mutex
is referenced by its memory address.

A mutex has the following key properties:

- A **lock count** that indicates the number of times the mutex has been locked
  by the thread that has locked it. A count of zero indicates that the mutex
  is unlocked.
- An **owning thread** that identifies the thread that has locked the mutex,
  when it is locked.

A mutex must be initialized before it can be used. This sets its lock count
to zero.

A thread that needs to use a shared resource must first gain exclusive rights
to access it by **locking** the associated mutex. If the mutex is already locked
by another thread, the requesting thread may choose to wait for the mutex
to be unlocked.

After locking a mutex, the thread may safely use the associated resource
for as long as needed; however, it is considered good practice to hold the lock
for as short a time as possible to avoid negatively impacting other threads
that want to use the resource. When the thread no longer needs the resource
it must **unlock** the mutex to allow other threads to use the resource.

Any number of threads may wait on a locked mutex simultaneously.
When the mutex becomes unlocked it is then locked by the highest-priority
thread that has waited the longest.

Note

Mutex objects are *not* designed for use by ISRs.

### [Reentrant Locking](#id2)

A thread is permitted to lock a mutex it has already locked.
This allows the thread to access the associated resource at a point
in its execution when the mutex may or may not already be locked.

A mutex that is repeatedly locked by a thread must be unlocked an equal number
of times before the mutex becomes fully unlocked so it can be claimed
by another thread.

### [Priority Inheritance](#id3)

The thread that has locked a mutex is eligible for *priority inheritance*.
This means the kernel will *temporarily* elevate the thread’s priority
if a higher priority thread begins waiting on the mutex. This allows the owning
thread to complete its work and release the mutex more rapidly by executing
at the same priority as the waiting thread. Once the mutex has been unlocked,
the unlocking thread resets its priority to the level it had before locking
that mutex.

Note

The [`CONFIG_PRIORITY_CEILING`](../../../kconfig.md#CONFIG_PRIORITY_CEILING "CONFIG_PRIORITY_CEILING") configuration option limits
how high the kernel can raise a thread’s priority due to priority
inheritance. The default value of 0 permits unlimited elevation.

The owning thread’s base priority is saved in the mutex when it obtains the
lock. Each time a higher priority thread waits on a mutex, the kernel adjusts
the owning thread’s priority. When the owning thread releases the lock (or if
the high priority waiting thread times out), the kernel restores the thread’s
base priority from the value saved in the mutex.

This works well for priority inheritance as long as only one locked mutex is
involved. However, if multiple mutexes are involved, sub-optimal behavior will
be observed if the mutexes are not unlocked in the reverse order to which the
owning thread’s priority was previously raised. Consequently it is recommended
that a thread lock only a single mutex at a time when multiple mutexes are
shared between threads of different priorities.

## [Implementation](#id4)

### [Defining a Mutex](#id5)

A mutex is defined using a variable of type [`k_mutex`](#c.k_mutex).
It must then be initialized by calling [`k_mutex_init()`](#c.k_mutex_init).

The following code defines and initializes a mutex.

```c
struct k_mutex my_mutex;

k_mutex_init(&my_mutex);
```

Alternatively, a mutex can be defined and initialized at compile time
by calling [`K_MUTEX_DEFINE`](#c.K_MUTEX_DEFINE).

The following code has the same effect as the code segment above.

```c
K_MUTEX_DEFINE(my_mutex);
```

### [Locking a Mutex](#id6)

A mutex is locked by calling [`k_mutex_lock()`](#c.k_mutex_lock).

The following code builds on the example above, and waits indefinitely
for the mutex to become available if it is already locked by another thread.

```c
k_mutex_lock(&my_mutex, K_FOREVER);
```

The following code waits up to 100 milliseconds for the mutex to become
available, and gives a warning if the mutex does not become available.

```c
if (k_mutex_lock(&my_mutex, K_MSEC(100)) == 0) {
    /* mutex successfully locked */
} else {
    printf("Cannot lock XYZ display\n");
}
```

### [Unlocking a Mutex](#id7)

A mutex is unlocked by calling [`k_mutex_unlock()`](#c.k_mutex_unlock).

The following code builds on the example above,
and unlocks the mutex that was previously locked by the thread.

```c
k_mutex_unlock(&my_mutex);
```

## [Suggested Uses](#id8)

Use a mutex to provide exclusive access to a resource, such as a physical
device.

## [Configuration Options](#id9)

Related configuration options:

- [`CONFIG_PRIORITY_CEILING`](../../../kconfig.md#CONFIG_PRIORITY_CEILING "CONFIG_PRIORITY_CEILING")

## [API Reference](#id10)

*group* mutex\_apis
:   Defines

    K\_MUTEX\_DEFINE(name)
    :   Statically define and initialize a mutex.

        The mutex can be accessed outside the module where it is defined using:

        ```text
        extern struct k_mutex <name>;
        ```

        Parameters:
        :   - **name** – Name of the mutex.

    Functions

    int k\_mutex\_init(struct [k\_mutex](#c.k_mutex) \*mutex)
    :   Initialize a mutex.

        This routine initializes a mutex object, prior to its first use.

        Upon completion, the mutex is available and does not have an owner.

        Parameters:
        :   - **mutex** – Address of the mutex.

        Return values:
        :   **0** – Mutex object created

    int k\_mutex\_lock(struct [k\_mutex](#c.k_mutex) \*mutex, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Lock a mutex.

        This routine locks *mutex*. If the mutex is locked by another thread, the calling thread waits until the mutex becomes available or until a timeout occurs.

        A thread is permitted to lock a mutex it has already locked. The operation completes immediately and the lock count is increased by 1.

        Mutexes may not be locked in ISRs.

        Parameters:
        :   - **mutex** – Address of the mutex.
            - **timeout** – Waiting period to lock the mutex, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – Mutex locked.
            - **-EBUSY** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.

    int k\_mutex\_unlock(struct [k\_mutex](#c.k_mutex) \*mutex)
    :   Unlock a mutex.

        This routine unlocks *mutex*. The mutex must already be locked by the calling thread.

        The mutex cannot be claimed by another thread until it has been unlocked by the calling thread as many times as it was previously locked by that thread.

        Mutexes may not be unlocked in ISRs, as mutexes must only be manipulated in thread context due to ownership and priority inheritance semantics.

        Parameters:
        :   - **mutex** – Address of the mutex.

        Return values:
        :   - **0** – Mutex unlocked.
            - **-EPERM** – The current thread does not own the mutex
            - **-EINVAL** – The mutex is not locked

    struct k\_mutex
    :   *#include <kernel.h>*

        Mutex Structure.

        Public Members

        \_wait\_q\_t wait\_q
        :   Mutex wait queue.

        struct [k\_thread](../threads/index.md#c.k_thread "k_thread") \*owner
        :   Mutex owner.

        uint32\_t lock\_count
        :   Current lock count.

        int owner\_orig\_prio
        :   Original thread priority.

## [Futex API Reference](#id11)

k\_futex is a lightweight mutual exclusion primitive designed to minimize
kernel involvement. Uncontended operation relies only on atomic access
to shared memory. k\_futex are tracked as kernel objects and can live in
user memory so that any access bypasses the kernel object permission
management mechanism.

*group* futex\_apis
:   Functions

    int k\_futex\_wait(struct k\_futex \*futex, int expected, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Pend the current thread on a futex.

        Tests that the supplied futex contains the expected value, and if so, goes to sleep until some other thread calls [k\_futex\_wake()](#group__futex__apis_1ga62de1aeb7c5c273aed20d0e05336d7a0) on it.

        Parameters:
        :   - **futex** – Address of the futex.
            - **expected** – Expected value of the futex, if it is different the caller will not wait on it.
            - **timeout** – Non-negative waiting period on the futex, or one of the special values K\_NO\_WAIT or K\_FOREVER.

        Return values:
        :   - **-EACCES** – Caller does not have read access to futex address.
            - **-EAGAIN** – If the futex value did not match the expected parameter.
            - **-EINVAL** – Futex parameter address not recognized by the kernel.
            - **-ETIMEDOUT** – Thread woke up due to timeout and not a futex wakeup.
            - **0** – if the caller went to sleep and was woken up. The caller should check the futex’s value on wakeup to determine if it needs to block again.

    int k\_futex\_wake(struct k\_futex \*futex, bool wake\_all)
    :   Wake one/all threads pending on a futex.

        Wake up the highest priority thread pending on the supplied futex, or wakeup all the threads pending on the supplied futex, and the behavior depends on wake\_all.

        Parameters:
        :   - **futex** – Futex to wake up pending threads.
            - **wake\_all** – If true, wake up all pending threads; If false, wakeup the highest priority thread.

        Return values:
        :   - **-EACCES** – Caller does not have access to the futex address.
            - **-EINVAL** – Futex parameter address not recognized by the kernel.
            - **Number** – of threads that were woken up.

## [User Mode Mutex API Reference](#id12)

sys\_mutex behaves almost exactly like k\_mutex, with the added advantage
that a sys\_mutex instance can reside in user memory. When user mode isn’t
enabled, sys\_mutex behaves like k\_mutex.

*group* user\_mutex\_apis
:   Defines

    SYS\_MUTEX\_DEFINE(name)
    :   Statically define and initialize a sys\_mutex.

        The mutex can be accessed outside the module where it is defined using:

        ```text
        extern struct sys_mutex <name>;
        ```

        Route this to memory domains using K\_APP\_DMEM().

        Parameters:
        :   - **name** – Name of the mutex.

    Functions

    static inline void sys\_mutex\_init(struct sys\_mutex \*mutex)
    :   Initialize a mutex.

        This routine initializes a mutex object, prior to its first use.

        Upon completion, the mutex is available and does not have an owner.

        This routine is only necessary to call when userspace is disabled and the mutex was not created with [SYS\_MUTEX\_DEFINE()](#group__user__mutex__apis_1ga486bd6a11d0b0d312cdf8a6a8f66c1a3).

        Parameters:
        :   - **mutex** – Address of the mutex.

    static inline int sys\_mutex\_lock(struct sys\_mutex \*mutex, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Lock a mutex.

        This routine locks *mutex*. If the mutex is locked by another thread, the calling thread waits until the mutex becomes available or until a timeout occurs.

        A thread is permitted to lock a mutex it has already locked. The operation completes immediately and the lock count is increased by 1.

        Parameters:
        :   - **mutex** – Address of the mutex, which may reside in user memory
            - **timeout** – Waiting period to lock the mutex, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – Mutex locked.
            - **-EBUSY** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.
            - **-EACCES** – Caller has no access to provided mutex address
            - **-EINVAL** – Provided mutex not recognized by the kernel

    static inline int sys\_mutex\_unlock(struct sys\_mutex \*mutex)
    :   Unlock a mutex.

        This routine unlocks *mutex*. The mutex must already be locked by the calling thread.

        The mutex cannot be claimed by another thread until it has been unlocked by the calling thread as many times as it was previously locked by that thread.

        Parameters:
        :   - **mutex** – Address of the mutex, which may reside in user memory

        Return values:
        :   - **0** – Mutex unlocked
            - **-EACCES** – Caller has no access to provided mutex address
            - **-EINVAL** – Provided mutex not recognized by the kernel or mutex wasn’t locked
            - **-EPERM** – Caller does not own the mutex
