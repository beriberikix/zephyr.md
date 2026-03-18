---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/timing/timers.html
original_path: kernel/services/timing/timers.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Timers

A *timer* is a kernel object that measures the passage of time
using the kernel’s system clock. When a timer’s specified time limit
is reached it can perform an application-defined action,
or it can simply record the expiration and wait for the application
to read its status.

## [Concepts](#id1)

Any number of timers can be defined (limited only by available RAM). Each timer
is referenced by its memory address.

A timer has the following key properties:

- A **duration** specifying the time interval before the timer
  expires for the first time. This is a `k_timeout_t` value that
  may be initialized via different units.
- A **period** specifying the time interval between all timer
  expirations after the first one, also a `k_timeout_t`. It must be
  non-negative. A period of `K_NO_WAIT` (i.e. zero) or
  `K_FOREVER` means that the timer is a one-shot timer that stops
  after a single expiration. (For example then, if a timer is started
  with a duration of 200 and a period of 75, it will first expire
  after 200 ms and then every 75 ms after that.)
- An **expiry function** that is executed each time the timer expires.
  The function is executed by the system clock interrupt handler.
  If no expiry function is required a `NULL` function can be specified.
- A **stop function** that is executed if the timer is stopped prematurely
  while running. The function is executed by the thread that stops the timer.
  If no stop function is required a `NULL` function can be specified.
- A **status** value that indicates how many times the timer has expired
  since the status value was last read.

A timer must be initialized before it can be used. This specifies its
expiry function and stop function values, sets the timer’s status to zero,
and puts the timer into the **stopped** state.

A timer is **started** by specifying a duration and a period.
The timer’s status is reset to zero, and then the timer enters
the **running** state and begins counting down towards expiry.

Note that the timer’s duration and period parameters specify
**minimum** delays that will elapse. Because of internal system timer
precision (and potentially runtime interactions like interrupt delay)
it is possible that more time may have passed as measured by reads
from the relevant system time APIs. But at least this much time is
guaranteed to have elapsed.

When a running timer expires its status is incremented
and the timer executes its expiry function, if one exists;
If a thread is waiting on the timer, it is unblocked.
If the timer’s period is zero the timer enters the stopped state;
otherwise, the timer restarts with a new duration equal to its period.

A running timer can be stopped in mid-countdown, if desired.
The timer’s status is left unchanged, then the timer enters the stopped state
and executes its stop function, if one exists.
If a thread is waiting on the timer, it is unblocked.
Attempting to stop a non-running timer is permitted,
but has no effect on the timer since it is already stopped.

A running timer can be restarted in mid-countdown, if desired.
The timer’s status is reset to zero, then the timer begins counting down
using the new duration and period values specified by the caller.
If a thread is waiting on the timer, it continues waiting.

A timer’s status can be read directly at any time to determine how many times
the timer has expired since its status was last read.
Reading a timer’s status resets its value to zero.
The amount of time remaining before the timer expires can also be read;
a value of zero indicates that the timer is stopped.

A thread may read a timer’s status indirectly by **synchronizing**
with the timer. This blocks the thread until the timer’s status is non-zero
(indicating that it has expired at least once) or the timer is stopped;
if the timer status is already non-zero or the timer is already stopped
the thread continues without waiting. The synchronization operation
returns the timer’s status and resets it to zero.

Note

Only a single user should examine the status of any given timer,
since reading the status (directly or indirectly) changes its value.
Similarly, only a single thread at a time should synchronize
with a given timer. ISRs are not permitted to synchronize with timers,
since ISRs are not allowed to block.

## [Implementation](#id2)

### [Defining a Timer](#id3)

A timer is defined using a variable of type `k_timer`.
It must then be initialized by calling [`k_timer_init()`](#c.k_timer_init).

The following code defines and initializes a timer.

```c
struct k_timer my_timer;
extern void my_expiry_function(struct k_timer *timer_id);

k_timer_init(&my_timer, my_expiry_function, NULL);
```

Alternatively, a timer can be defined and initialized at compile time
by calling [`K_TIMER_DEFINE`](#c.K_TIMER_DEFINE).

The following code has the same effect as the code segment above.

```c
K_TIMER_DEFINE(my_timer, my_expiry_function, NULL);
```

### [Using a Timer Expiry Function](#id4)

The following code uses a timer to perform a non-trivial action on a periodic
basis. Since the required work cannot be done at the interrupt level,
the timer’s expiry function submits a work item to the
[system workqueue](../threads/workqueue.md#workqueues-v2), whose thread performs the work.

```c
void my_work_handler(struct k_work *work)
{
    /* do the processing that needs to be done periodically */
    ...
}

K_WORK_DEFINE(my_work, my_work_handler);

void my_timer_handler(struct k_timer *dummy)
{
    k_work_submit(&my_work);
}

K_TIMER_DEFINE(my_timer, my_timer_handler, NULL);

...

/* start a periodic timer that expires once every second */
k_timer_start(&my_timer, K_SECONDS(1), K_SECONDS(1));
```

### [Reading Timer Status](#id5)

The following code reads a timer’s status directly to determine
if the timer has expired or not.

```c
K_TIMER_DEFINE(my_status_timer, NULL, NULL);

...

/* start a one-shot timer that expires after 200 ms */
k_timer_start(&my_status_timer, K_MSEC(200), K_NO_WAIT);

/* do work */
...

/* check timer status */
if (k_timer_status_get(&my_status_timer) > 0) {
    /* timer has expired */
} else if (k_timer_remaining_get(&my_status_timer) == 0) {
    /* timer was stopped (by someone else) before expiring */
} else {
    /* timer is still running */
}
```

### [Using Timer Status Synchronization](#id6)

The following code performs timer status synchronization to allow a thread
to do useful work while ensuring that a pair of protocol operations
are separated by the specified time interval.

```c
K_TIMER_DEFINE(my_sync_timer, NULL, NULL);

...

/* do first protocol operation */
...

/* start a one-shot timer that expires after 500 ms */
k_timer_start(&my_sync_timer, K_MSEC(500), K_NO_WAIT);

/* do other work */
...

/* ensure timer has expired (waiting for expiry, if necessary) */
k_timer_status_sync(&my_sync_timer);

/* do second protocol operation */
...
```

Note

If the thread had no other work to do it could simply sleep
between the two protocol operations, without using a timer.

## [Suggested Uses](#id7)

Use a timer to initiate an asynchronous operation after a specified
amount of time.

Use a timer to determine whether or not a specified amount of time has
elapsed. In particular, timers should be used when higher precision
and/or unit control is required than that afforded by the simpler
[`k_sleep()`](../threads/index.md#c.k_sleep "k_sleep") and [`k_usleep()`](../threads/index.md#c.k_usleep "k_usleep") calls.

Use a timer to perform other work while carrying out operations
involving time limits.

Note

If a thread needs to measure the time required to perform an operation
it can read the [system clock or the hardware clock](clocks.md#kernel-timing)
directly, rather than using a timer.

## [Configuration Options](#id8)

Related configuration options:

- None

## [API Reference](#id9)

Related code samples

[KSCAN](../../../samples/drivers/kscan/README.md#kscan "Use the KSCAN API to read key presses and releases on a keyboard matrix.")
:   Use the KSCAN API to read key presses and releases on a keyboard matrix.

*group* timer\_apis
:   Defines

    K\_TIMER\_DEFINE(name, expiry\_fn, stop\_fn)
    :   Statically define and initialize a timer.

        The timer can be accessed outside the module where it is defined using:

        ```text
        extern struct k_timer <name>;
        ```

        Parameters:
        :   - **name** – Name of the timer variable.
            - **expiry\_fn** – Function to invoke each time the timer expires.
            - **stop\_fn** – Function to invoke if the timer is stopped while running.

    Typedefs

    typedef void (\*k\_timer\_expiry\_t)(struct k\_timer \*timer)
    :   Timer expiry function type.

        A timer’s expiry function is executed by the system clock interrupt handler each time the timer expires. The expiry function is optional, and is only invoked if the timer has been initialized with one.

        Param timer:
        :   Address of timer.

    typedef void (\*k\_timer\_stop\_t)(struct k\_timer \*timer)
    :   Timer stop function type.

        A timer’s stop function is executed if the timer is stopped prematurely. The function runs in the context of call that stops the timer. As [k\_timer\_stop()](#group__timer__apis_1ga8d3e3356a10d36570e16f7920e4c8772) can be invoked from an ISR, the stop function must be callable from interrupt context (isr-ok).

        The stop function is optional, and is only invoked if the timer has been initialized with one.

        Param timer:
        :   Address of timer.

    Functions

    void k\_timer\_init(struct k\_timer \*timer, [k\_timer\_expiry\_t](#c.k_timer_expiry_t) expiry\_fn, [k\_timer\_stop\_t](#c.k_timer_stop_t) stop\_fn)
    :   Initialize a timer.

        This routine initializes a timer, prior to its first use.

        Parameters:
        :   - **timer** – Address of timer.
            - **expiry\_fn** – Function to invoke each time the timer expires.
            - **stop\_fn** – Function to invoke if the timer is stopped while running.

    void k\_timer\_start(struct k\_timer \*timer, [k\_timeout\_t](clocks.md#c.k_timeout_t "k_timeout_t") duration, [k\_timeout\_t](clocks.md#c.k_timeout_t "k_timeout_t") period)
    :   Start a timer.

        This routine starts a timer, and resets its status to zero. The timer begins counting down using the specified duration and period values.

        Attempting to start a timer that is already running is permitted. The timer’s status is reset to zero and the timer begins counting down using the new duration and period values.

        Parameters:
        :   - **timer** – Address of timer.
            - **duration** – Initial timer duration.
            - **period** – Timer period.

    void k\_timer\_stop(struct k\_timer \*timer)
    :   Stop a timer.

        This routine stops a running timer prematurely. The timer’s stop function, if one exists, is invoked by the caller.

        Attempting to stop a timer that is not running is permitted, but has no effect on the timer.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        The stop handler has to be callable from ISRs if *k\_timer\_stop* is to be called from ISRs.

        Parameters:
        :   - **timer** – Address of timer.

    uint32\_t k\_timer\_status\_get(struct k\_timer \*timer)
    :   Read timer status.

        This routine reads the timer’s status, which indicates the number of times it has expired since its status was last read.

        Calling this routine resets the timer’s status to zero.

        Parameters:
        :   - **timer** – Address of timer.

        Returns:
        :   Timer status.

    uint32\_t k\_timer\_status\_sync(struct k\_timer \*timer)
    :   Synchronize thread to timer expiration.

        This routine blocks the calling thread until the timer’s status is non-zero (indicating that it has expired at least once since it was last examined) or the timer is stopped. If the timer status is already non-zero, or the timer is already stopped, the caller continues without waiting.

        Calling this routine resets the timer’s status to zero.

        This routine must not be used by interrupt handlers, since they are not allowed to block.

        Parameters:
        :   - **timer** – Address of timer.

        Returns:
        :   Timer status.

    [k\_ticks\_t](clocks.md#c.k_ticks_t "k_ticks_t") k\_timer\_expires\_ticks(const struct k\_timer \*timer)
    :   Get next expiration time of a timer, in system ticks.

        This routine returns the future system uptime reached at the next time of expiration of the timer, in units of system ticks. If the timer is not running, current system time is returned.

        Parameters:
        :   - **timer** – The timer object

        Returns:
        :   Uptime of expiration, in ticks

    [k\_ticks\_t](clocks.md#c.k_ticks_t "k_ticks_t") k\_timer\_remaining\_ticks(const struct k\_timer \*timer)
    :   Get time remaining before a timer next expires, in system ticks.

        This routine computes the time remaining before a running timer next expires, in units of system ticks. If the timer is not running, it returns zero.

    static inline uint32\_t k\_timer\_remaining\_get(struct k\_timer \*timer)
    :   Get time remaining before a timer next expires.

        This routine computes the (approximate) time remaining before a running timer next expires. If the timer is not running, it returns zero.

        Parameters:
        :   - **timer** – Address of timer.

        Returns:
        :   Remaining time (in milliseconds).

    void k\_timer\_user\_data\_set(struct k\_timer \*timer, void \*user\_data)
    :   Associate user-specific data with a timer.

        This routine records the *user\_data* with the *timer*, to be retrieved later.

        It can be used e.g. in a timer handler shared across multiple subsystems to retrieve data specific to the subsystem this timer is associated with.

        Parameters:
        :   - **timer** – Address of timer.
            - **user\_data** – User data to associate with the timer.

    void \*k\_timer\_user\_data\_get(const struct k\_timer \*timer)
    :   Retrieve the user-specific data from a timer.

        Parameters:
        :   - **timer** – Address of timer.

        Returns:
        :   The user data.
