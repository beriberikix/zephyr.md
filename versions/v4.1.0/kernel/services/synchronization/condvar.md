---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/services/synchronization/condvar.html
original_path: kernel/services/synchronization/condvar.html
---

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
[`k_condvar_wait()`](../../../doxygen/html/group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc) performs atomically the following steps;

1. Releases the last acquired mutex.
2. Puts the current thread in the condition variable queue.

Some other thread, when it changes said state, can then wake one (or more)
of those waiting threads and thus allow them to continue by signaling on
the condition using [`k_condvar_signal()`](../../../doxygen/html/group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b) or
[`k_condvar_broadcast()`](../../../doxygen/html/group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8) then it:

1. Re-acquires the mutex previously released.
2. Returns from [`k_condvar_wait()`](../../../doxygen/html/group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc).

A condition variable must be initialized before it can be used.

## [Implementation](#id2)

### [Defining a Condition Variable](#id3)

A condition variable is defined using a variable of type [`k_condvar`](../../../doxygen/html/structk__condvar.md).
It must then be initialized by calling [`k_condvar_init()`](../../../doxygen/html/group__condvar__apis.md#gac9b497c56cc4642965afa6c0c6d7ecfc).

The following code defines a condition variable:

```c
struct k_condvar my_condvar;

k_condvar_init(&my_condvar);
```

Alternatively, a condition variable can be defined and initialized at compile time
by calling [`K_CONDVAR_DEFINE`](../../../doxygen/html/group__condvar__apis.md#ga770816651e25f7e7dae992a0b2260c21).

The following code has the same effect as the code segment above.

```c
K_CONDVAR_DEFINE(my_condvar);
```

### [Waiting on a Condition Variable](#id4)

A thread can wait on a condition by calling [`k_condvar_wait()`](../../../doxygen/html/group__condvar__apis.md#gab2e1d05db4f954755f430ca894e44dbc).

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

A condition variable is signaled on by calling [`k_condvar_signal()`](../../../doxygen/html/group__condvar__apis.md#ga0376a8f7dc6e4f1e1eed55940f43015b) for
one thread or by calling [`k_condvar_broadcast()`](../../../doxygen/html/group__condvar__apis.md#gad2e46a7b9e1bc934fd1f5cb38dde40d8) for multiple threads.

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

[Condition Variables APIs](../../../doxygen/html/group__condvar__apis.md)

Related code samples

- [Condition Variables](../../../samples/kernel/condition_variables/condvar/README.md#kernel-condvar "Manipulate condition variables in a multithreaded application.")Manipulate condition variables in a multithreaded application.
