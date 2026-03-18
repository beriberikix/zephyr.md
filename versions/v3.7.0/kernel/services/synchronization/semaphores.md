---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/services/synchronization/semaphores.html
original_path: kernel/services/synchronization/semaphores.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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
It must then be initialized by calling [`k_sem_init()`](#c.k_sem_init).

The following code defines a semaphore, then configures it as a binary
semaphore by setting its count to 0 and its limit to 1.

```c
struct k_sem my_sem;

k_sem_init(&my_sem, 0, 1);
```

Alternatively, a semaphore can be defined and initialized at compile time
by calling [`K_SEM_DEFINE`](#c.K_SEM_DEFINE).

The following code has the same effect as the code segment above.

```c
K_SEM_DEFINE(my_sem, 0, 1);
```

### [Giving a Semaphore](#id4)

A semaphore is given by calling [`k_sem_give()`](#c.k_sem_give).

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

A semaphore is taken by calling [`k_sem_take()`](#c.k_sem_take).

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

Related code samples

[Basic Synchronization](../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.")
:   Manipulate basic kernel synchronization primitives.

*group* Semaphore APIs
:   Defines

    K\_SEM\_MAX\_LIMIT
    :   Maximum limit value allowed for a semaphore.

        This is intended for use when a semaphore does not have an explicit maximum limit, and instead is just used for counting purposes.

    K\_SEM\_DEFINE(name, initial\_count, count\_limit)
    :   Statically define and initialize a semaphore.

        The semaphore can be accessed outside the module where it is defined using:

        ```text
        extern struct k_sem <name>;
        ```

        Parameters:
        :   - **name** – Name of the semaphore.
            - **initial\_count** – Initial semaphore count.
            - **count\_limit** – Maximum permitted semaphore count.

    Functions

    int k\_sem\_init(struct k\_sem \*sem, unsigned int initial\_count, unsigned int limit)
    :   Initialize a semaphore.

        This routine initializes a semaphore object, prior to its first use.

        See also

        [K\_SEM\_MAX\_LIMIT](#group__semaphore__apis_1ga689359a77a0cebe737ef644c188f7e57)

        Parameters:
        :   - **sem** – Address of the semaphore.
            - **initial\_count** – Initial semaphore count.
            - **limit** – Maximum permitted semaphore count.

        Return values:
        :   - **0** – Semaphore created successfully
            - **-EINVAL** – Invalid values

    int k\_sem\_take(struct k\_sem \*sem, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Take a semaphore.

        This routine takes *sem*.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Parameters:
        :   - **sem** – Address of the semaphore.
            - **timeout** – Waiting period to take the semaphore, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – Semaphore taken.
            - **-EBUSY** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out, or the semaphore was reset during the waiting period.

    void k\_sem\_give(struct k\_sem \*sem)
    :   Give a semaphore.

        This routine gives *sem*, unless the semaphore is already at its maximum permitted count.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **sem** – Address of the semaphore.

    void k\_sem\_reset(struct k\_sem \*sem)
    :   Resets a semaphore’s count to zero.

        This routine sets the count of *sem* to zero. Any outstanding semaphore takes will be aborted with -EAGAIN.

        Parameters:
        :   - **sem** – Address of the semaphore.

    unsigned int k\_sem\_count\_get(struct k\_sem \*sem)
    :   Get a semaphore’s count.

        This routine returns the current count of *sem*.

        Parameters:
        :   - **sem** – Address of the semaphore.

        Returns:
        :   Current semaphore count.

## [User Mode Semaphore API Reference](#id9)

The sys\_sem exists in user memory working as counter semaphore for user mode
thread when user mode enabled. When user mode isn’t enabled, sys\_sem behaves
like k\_sem.

*group* User mode semaphore APIs
:   Defines

    SYS\_SEM\_DEFINE(\_name, \_initial\_count, \_count\_limit)
    :   Statically define and initialize a sys\_sem.

        The semaphore can be accessed outside the module where it is defined using:

        ```text
        extern struct sys_sem <name>;
        ```

        Route this to memory domains using K\_APP\_DMEM().

        Parameters:
        :   - **\_name** – Name of the semaphore.
            - **\_initial\_count** – Initial semaphore count.
            - **\_count\_limit** – Maximum permitted semaphore count.

    Functions

    int sys\_sem\_init(struct sys\_sem \*sem, unsigned int initial\_count, unsigned int limit)
    :   Initialize a semaphore.

        This routine initializes a semaphore instance, prior to its first use.

        Parameters:
        :   - **sem** – Address of the semaphore.
            - **initial\_count** – Initial semaphore count.
            - **limit** – Maximum permitted semaphore count.

        Return values:
        :   - **0** – Initial success.
            - **-EINVAL** – Bad parameters, the value of limit should be located in (0, INT\_MAX] and initial\_count shouldn’t be greater than limit.

    int sys\_sem\_give(struct sys\_sem \*sem)
    :   Give a semaphore.

        This routine gives *sem*, unless the semaphore is already at its maximum permitted count.

        Parameters:
        :   - **sem** – Address of the semaphore.

        Return values:
        :   - **0** – Semaphore given.
            - **-EINVAL** – Parameter address not recognized.
            - **-EACCES** – Caller does not have enough access.
            - **-EAGAIN** – Count reached Maximum permitted count and try again.

    int sys\_sem\_take(struct sys\_sem \*sem, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Take a sys\_sem.

        This routine takes *sem*.

        Parameters:
        :   - **sem** – Address of the sys\_sem.
            - **timeout** – Waiting period to take the sys\_sem, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – sys\_sem taken.
            - **-EINVAL** – Parameter address not recognized.
            - **-ETIMEDOUT** – Waiting period timed out.
            - **-EACCES** – Caller does not have enough access.

    unsigned int sys\_sem\_count\_get(struct sys\_sem \*sem)
    :   Get sys\_sem’s value.

        This routine returns the current value of *sem*.

        Parameters:
        :   - **sem** – Address of the sys\_sem.

        Returns:
        :   Current value of sys\_sem.
