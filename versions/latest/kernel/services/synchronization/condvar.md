---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/synchronization/condvar.html
original_path: kernel/services/synchronization/condvar.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Condition Variables

A *condition variable* is a synchronization primitive
that enables threads to wait until a particular condition occurs.

## [Concepts](#id1)

Any number of condition variables can be defined (limited only by available RAM). Each
condition variable is referenced by its memory address.

To wait for a condition to become true, a thread can make use of a condition
variable.

A condition variable is basically a queue of threads that threads can put
themselves on when some state of execution (i.e., some condition) is not as
desired (by waiting on the condition). The function
[`k_condvar_wait()`](#c.k_condvar_wait) performs atomically the following steps;

1. Releases the last acquired mutex.
2. Puts the current thread in the condition variable queue.

Some other thread, when it changes said state, can then wake one (or more)
of those waiting threads and thus allow them to continue by signaling on
the condition using [`k_condvar_signal()`](#c.k_condvar_signal) or
[`k_condvar_broadcast()`](#c.k_condvar_broadcast) then it:

1. Re-acquires the mutex previously released.
2. Returns from [`k_condvar_wait()`](#c.k_condvar_wait).

A condition variable must be initialized before it can be used.

## [Implementation](#id2)

### [Defining a Condition Variable](#id3)

A condition variable is defined using a variable of type `k_condvar`.
It must then be initialized by calling [`k_condvar_init()`](#c.k_condvar_init).

The following code defines a condition variable:

```c
struct k_condvar my_condvar;

k_condvar_init(&my_condvar);
```

Alternatively, a condition variable can be defined and initialized at compile time
by calling [`K_CONDVAR_DEFINE`](#c.K_CONDVAR_DEFINE).

The following code has the same effect as the code segment above.

```c
K_CONDVAR_DEFINE(my_condvar);
```

### [Waiting on a Condition Variable](#id4)

A thread can wait on a condition by calling [`k_condvar_wait()`](#c.k_condvar_wait).

The following code waits on the condition variable.

```c
K_MUTEX_DEFINE(mutex);
K_CONDVAR_DEFINE(condvar)

int main(void)
{
    k_mutex_lock(&mutex, K_FOREVER);

    /* block this thread until another thread signals cond. While
     * blocked, the mutex is released, then re-acquired before this
     * thread is woken up and the call returns.
     */
    k_condvar_wait(&condvar, &mutex, K_FOREVER);
    ...
    k_mutex_unlock(&mutex);
}
```

### [Signaling a Condition Variable](#id5)

A condition variable is signaled on by calling [`k_condvar_signal()`](#c.k_condvar_signal) for
one thread or by calling [`k_condvar_broadcast()`](#c.k_condvar_broadcast) for multiple threads.

The following code builds on the example above.

```c
void worker_thread(void)
{
    k_mutex_lock(&mutex, K_FOREVER);

    /*
     * Do some work and fulfill the condition
     */
    ...
    ...
    k_condvar_signal(&condvar);
    k_mutex_unlock(&mutex);
}
```

## [Suggested Uses](#id6)

Use condition variables with a mutex to signal changing states (conditions) from
one thread to another thread.
Condition variables are not the condition itself and they are not events.
The condition is contained in the surrounding programming logic.

Mutexes alone are not designed for use as a notification/synchronization
mechanism. They are meant to provide mutually exclusive access to a shared
resource only.

## [Configuration Options](#id7)

Related configuration options:

- None.

## [API Reference](#id8)

Related code samples

[Condition Variables](../../../samples/kernel/condition_variables/condvar/README.md#kernel-condvar "Manipulate condition variables in a multithreaded application.")
:   Manipulate condition variables in a multithreaded application.

*group* condvar\_apis
:   Defines

    K\_CONDVAR\_DEFINE(name)
    :   Statically define and initialize a condition variable.

        The condition variable can be accessed outside the module where it is defined using:

        ```text
        extern struct k_condvar <name>;
        ```

        Parameters:
        :   - **name** – Name of the condition variable.

    Functions

    int k\_condvar\_init(struct k\_condvar \*condvar)
    :   Initialize a condition variable.

        Parameters:
        :   - **condvar** – pointer to a `k_condvar` structure

        Return values:
        :   **0** – Condition variable created successfully

    int k\_condvar\_signal(struct k\_condvar \*condvar)
    :   Signals one thread that is pending on the condition variable.

        Parameters:
        :   - **condvar** – pointer to a `k_condvar` structure

        Return values:
        :   **0** – On success

    int k\_condvar\_broadcast(struct k\_condvar \*condvar)
    :   Unblock all threads that are pending on the condition variable.

        Parameters:
        :   - **condvar** – pointer to a `k_condvar` structure

        Returns:
        :   An integer with number of woken threads on success

    int k\_condvar\_wait(struct k\_condvar \*condvar, struct [k\_mutex](mutexes.md#c.k_mutex "k_mutex") \*mutex, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Waits on the condition variable releasing the mutex lock.

        Atomically releases the currently owned mutex, blocks the current thread waiting on the condition variable specified by *condvar*, and finally acquires the mutex again.

        The waiting thread unblocks only after another thread calls k\_condvar\_signal, or k\_condvar\_broadcast with the same condition variable.

        Parameters:
        :   - **condvar** – pointer to a `k_condvar` structure
            - **mutex** – Address of the mutex.
            - **timeout** – Waiting period for the condition variable or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – On success
            - **-EAGAIN** – Waiting period timed out.
