---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/services/synchronization/semaphores.html
original_path: kernel/services/synchronization/semaphores.html
---

# Semaphores

A *semaphore* is a kernel object that implements a traditional
counting semaphore.

## [Concepts](#id1)

Any number of semaphores can be defined (limited only by available RAM). Each
semaphore is referenced by its memory address.

A semaphore has the following key properties:

- A **count** that indicates the number of times the semaphore can be taken.
  A count of zero indicates that the semaphore is unavailable.
- A **limit** that indicates the maximum value the semaphore’s count
  can reach.

A semaphore must be initialized before it can be used. Its count must be set
to a non-negative value that is less than or equal to its limit.

A semaphore may be **given** by a thread or an ISR. Giving the semaphore
increments its count, unless the count is already equal to the limit.

A semaphore may be **taken** by a thread. Taking the semaphore
decrements its count, unless the semaphore is unavailable (i.e. at zero).
When a semaphore is unavailable a thread may choose to wait for it to be given.
Any number of threads may wait on an unavailable semaphore simultaneously.
When the semaphore is given, it is taken by the highest priority thread
that has waited longest.

Note

You may initialize a “full” semaphore (count equal to limit) to limit the number
of threads able to execute the critical section at the same time. You may also
initialize an empty semaphore (count equal to 0, with a limit greater than 0)
to create a gate through which no waiting thread may pass until the semaphore
is incremented. All standard use cases of the common semaphore are supported.

Note

The kernel does allow an ISR to take a semaphore, however the ISR must
not attempt to wait if the semaphore is unavailable.

## [Implementation](#id2)

### [Defining a Semaphore](#id3)

A semaphore is defined using a variable of type `k_sem`.
It must then be initialized by calling [`k_sem_init()`](../../../doxygen/html/group__semaphore__apis.md#gadcd0e6cfba3392fb887222eafe4c1845).

The following code defines a semaphore, then configures it as a binary
semaphore by setting its count to 0 and its limit to 1.

```c
struct k_sem my_sem;

k_sem_init(&my_sem, 0, 1);
```

Alternatively, a semaphore can be defined and initialized at compile time
by calling [`K_SEM_DEFINE`](../../../doxygen/html/group__semaphore__apis.md#ga018a8aa43e02e704deee7b6341502946).

The following code has the same effect as the code segment above.

```c
K_SEM_DEFINE(my_sem, 0, 1);
```

### [Giving a Semaphore](#id4)

A semaphore is given by calling [`k_sem_give()`](../../../doxygen/html/group__semaphore__apis.md#gab9be3cf1988af2cd6afdace52d497c84).

The following code builds on the example above, and gives the semaphore to
indicate that a unit of data is available for processing by a consumer thread.

```c
void input_data_interrupt_handler(void *arg)
{
    /* notify thread that data is available */
    k_sem_give(&my_sem);

    ...
}
```

### [Taking a Semaphore](#id5)

A semaphore is taken by calling [`k_sem_take()`](../../../doxygen/html/group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090).

The following code builds on the example above, and waits up to 50 milliseconds
for the semaphore to be given.
A warning is issued if the semaphore is not obtained in time.

```c
void consumer_thread(void)
{
    ...

    if (k_sem_take(&my_sem, K_MSEC(50)) != 0) {
        printk("Input data not available!");
    } else {
        /* fetch available data */
        ...
    }
    ...
}
```

## [Suggested Uses](#id6)

Use a semaphore to control access to a set of resources by multiple threads.

Use a semaphore to synchronize processing between a producing and consuming
threads or ISRs.

## [Configuration Options](#id7)

Related configuration options:

- None.

## [API Reference](#id8)

[Semaphore APIs](../../../doxygen/html/group__semaphore__apis.md)

Related code samples

- [Basic Synchronization](../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.")Manipulate basic kernel synchronization primitives.
- [Dining Philosophers](../../../samples/philosophers/README.md#dining-philosophers "Implement a solution to the Dining Philosophers problem using Zephyr kernel services.")Implement a solution to the Dining Philosophers problem using Zephyr kernel services.

## [User Mode Semaphore API Reference](#id9)

The sys\_sem exists in user memory working as counter semaphore for user mode
thread when user mode enabled. When user mode isn’t enabled, sys\_sem behaves
like k\_sem.

[User mode semaphore APIs](../../../doxygen/html/group__user__semaphore__apis.md)
