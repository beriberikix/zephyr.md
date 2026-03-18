---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/threads/workqueue.html
original_path: kernel/services/threads/workqueue.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Workqueue Threads

A *workqueue* is a kernel object that uses a dedicated thread to process
work items in a first in, first out manner. Each work item is processed by
calling the function specified by the work item. A workqueue is typically
used by an ISR or a high-priority thread to offload non-urgent processing
to a lower-priority thread so it does not impact time-sensitive processing.

Any number of workqueues can be defined (limited only by available RAM). Each
workqueue is referenced by its memory address.

A workqueue has the following key properties:

- A **queue** of work items that have been added, but not yet processed.
- A **thread** that processes the work items in the queue. The priority of the
  thread is configurable, allowing it to be either cooperative or preemptive
  as required.

Regardless of workqueue thread priority the workqueue thread will yield
between each submitted work item, to prevent a cooperative workqueue from
starving other threads.

A workqueue must be initialized before it can be used. This sets its queue to
empty and spawns the workqueue’s thread. The thread runs forever, but sleeps
when no work items are available.

Note

The behavior described here is changed from the Zephyr workqueue
implementation used prior to release 2.6. Among the changes are:

- Precise tracking of the status of cancelled work items, so that the
  caller need not be concerned that an item may be processing when the
  cancellation returns. Checking of return values on cancellation is still
  required.
- Direct submission of delayable work items to the queue with
  [`K_NO_WAIT`](../timing/clocks.md#c.K_NO_WAIT "K_NO_WAIT") rather than always going through the timeout API,
  which could introduce delays.
- The ability to wait until a work item has completed or a queue has been
  drained.
- Finer control of behavior when scheduling a delayable work item,
  specifically allowing a previous deadline to remain unchanged when a work
  item is scheduled again.
- Safe handling of work item resubmission when the item is being processed
  on another workqueue.

Using the return values of [`k_work_busy_get()`](#c.k_work_busy_get) or
[`k_work_is_pending()`](#c.k_work_is_pending), or measurements of remaining time until
delayable work is scheduled, should be avoided to prevent race conditions
of the type observed with the previous implementation. See also [Workqueue
Best Practices](#workqueue-best-practices).

## [Work Item Lifecycle](#id1)

Any number of **work items** can be defined. Each work item is referenced
by its memory address.

A work item is assigned a **handler function**, which is the function
executed by the workqueue’s thread when the work item is processed. This
function accepts a single argument, which is the address of the work item
itself. The work item also maintains information about its status.

A work item must be initialized before it can be used. This records the work
item’s handler function and marks it as not pending.

A work item may be **queued** ([`K_WORK_QUEUED`](#c.@343312232126365371060313064061273354303275321114.K_WORK_QUEUED)) by submitting it to a
workqueue by an ISR or a thread. Submitting a work item appends the work item
to the workqueue’s queue. Once the workqueue’s thread has processed all of
the preceding work items in its queue the thread will remove the next work
item from the queue and invoke the work item’s handler function. Depending on
the scheduling priority of the workqueue’s thread, and the work required by
other items in the queue, a queued work item may be processed quickly or it
may remain in the queue for an extended period of time.

A delayable work item may be **scheduled** ([`K_WORK_DELAYED`](#c.@343312232126365371060313064061273354303275321114.K_WORK_DELAYED)) to a
workqueue; see [Delayable Work](#delayable-work).

A work item will be **running** ([`K_WORK_RUNNING`](#c.@343312232126365371060313064061273354303275321114.K_WORK_RUNNING)) when it is running
on a work queue, and may also be **canceling** ([`K_WORK_CANCELING`](#c.@343312232126365371060313064061273354303275321114.K_WORK_CANCELING))
if it started running before a thread has requested that it be cancelled.

A work item can be in multiple states; for example it can be:

- running on a queue;
- marked canceling (because a thread used [`k_work_cancel_sync()`](#c.k_work_cancel_sync) to
  wait until the work item completed);
- queued to run again on the same queue;
- scheduled to be submitted to a (possibly different) queue

*all simultaneously*. A work item that is in any of these states is **pending**
([`k_work_is_pending()`](#c.k_work_is_pending)) or **busy** ([`k_work_busy_get()`](#c.k_work_busy_get)).

A handler function can use any kernel API available to threads. However,
operations that are potentially blocking (e.g. taking a semaphore) must be
used with care, since the workqueue cannot process subsequent work items in
its queue until the handler function finishes executing.

The single argument that is passed to a handler function can be ignored if it
is not required. If the handler function requires additional information about
the work it is to perform, the work item can be embedded in a larger data
structure. The handler function can then use the argument value to compute the
address of the enclosing data structure with [`CONTAINER_OF`](../../util/index.md#c.CONTAINER_OF "CONTAINER_OF"), and
thereby obtain access to the additional information it needs.

A work item is typically initialized once and then submitted to a specific
workqueue whenever work needs to be performed. If an ISR or a thread attempts
to submit a work item that is already queued the work item is not affected;
the work item remains in its current place in the workqueue’s queue, and
the work is only performed once.

A handler function is permitted to re-submit its work item argument
to the workqueue, since the work item is no longer queued at that time.
This allows the handler to execute work in stages, without unduly delaying
the processing of other work items in the workqueue’s queue.

Important

A pending work item *must not* be altered until the item has been processed
by the workqueue thread. This means a work item must not be re-initialized
while it is busy. Furthermore, any additional information the work item’s
handler function needs to perform its work must not be altered until
the handler function has finished executing.

## [Delayable Work](#id2)

An ISR or a thread may need to schedule a work item that is to be processed
only after a specified period of time, rather than immediately. This can be
done by **scheduling** a **delayable work item** to be submitted to a
workqueue at a future time.

A delayable work item contains a standard work item but adds fields that
record when and where the item should be submitted.

A delayable work item is initialized and scheduled to a workqueue in a similar
manner to a standard work item, although different kernel APIs are used. When
the schedule request is made the kernel initiates a timeout mechanism that is
triggered after the specified delay has elapsed. Once the timeout occurs the
kernel submits the work item to the specified workqueue, where it remains
queued until it is processed in the standard manner.

Note that work handler used for delayable still receives a pointer to the
underlying non-delayable work structure, which is not publicly accessible from
[`k_work_delayable`](#c.k_work_delayable). To get access to an object that contains the
delayable work object use this idiom:

```c
static void work_handler(struct k_work *work)
{
        struct k_work_delayable *dwork = k_work_delayable_from_work(work);
        struct work_context *ctx = CONTAINER_OF(dwork, struct work_context,
                                                timed_work);
        ...
```

## [Triggered Work](#id3)

The [`k_work_poll_submit()`](#c.k_work_poll_submit) interface schedules a triggered work
item in response to a **poll event** (see [Polling API](../polling.md#polling-v2)), that will
call a user-defined function when a monitored resource becomes available
or poll signal is raised, or a timeout occurs.
In contrast to [`k_poll()`](../polling.md#c.k_poll "k_poll"), the triggered work does not require
a dedicated thread waiting or actively polling for a poll event.

A triggered work item is a standard work item that has the following
added properties:

- A pointer to an array of poll events that will trigger work item
  submissions to the workqueue
- A size of the array containing poll events.

A triggered work item is initialized and submitted to a workqueue in a similar
manner to a standard work item, although dedicated kernel APIs are used.
When a submit request is made, the kernel begins observing kernel objects
specified by the poll events. Once at least one of the observed kernel
object’s changes state, the work item is submitted to the specified workqueue,
where it remains queued until it is processed in the standard manner.

Important

The triggered work item as well as the referenced array of poll events
have to be valid and cannot be modified for a complete triggered work
item lifecycle, from submission to work item execution or cancellation.

An ISR or a thread may **cancel** a triggered work item it has submitted
as long as it is still waiting for a poll event. In such case, the kernel
stops waiting for attached poll events and the specified work is not executed.
Otherwise the cancellation cannot be performed.

## [System Workqueue](#id4)

The kernel defines a workqueue known as the *system workqueue*, which is
available to any application or kernel code that requires workqueue support.
The system workqueue is optional, and only exists if the application makes
use of it.

Important

Additional workqueues should only be defined when it is not possible
to submit new work items to the system workqueue, since each new workqueue
incurs a significant cost in memory footprint. A new workqueue can be
justified if it is not possible for its work items to co-exist with
existing system workqueue work items without an unacceptable impact;
for example, if the new work items perform blocking operations that
would delay other system workqueue processing to an unacceptable degree.

## [How to Use Workqueues](#id5)

### Defining and Controlling a Workqueue

A workqueue is defined using a variable of type [`k_work_q`](#c.k_work_q).
The workqueue is initialized by defining the stack area used by its
thread, initializing the [`k_work_q`](#c.k_work_q), either zeroing its
memory or calling [`k_work_queue_init()`](#c.k_work_queue_init), and then calling
[`k_work_queue_start()`](#c.k_work_queue_start). The stack area must be defined using
[`K_THREAD_STACK_DEFINE`](index.md#c.K_THREAD_STACK_DEFINE "K_THREAD_STACK_DEFINE") to ensure it is properly set up in
memory.

The following code defines and initializes a workqueue:

```c
#define MY_STACK_SIZE 512
#define MY_PRIORITY 5

K_THREAD_STACK_DEFINE(my_stack_area, MY_STACK_SIZE);

struct k_work_q my_work_q;

k_work_queue_init(&my_work_q);

k_work_queue_start(&my_work_q, my_stack_area,
                   K_THREAD_STACK_SIZEOF(my_stack_area), MY_PRIORITY,
                   NULL);
```

In addition the queue identity and certain behavior related to thread
rescheduling can be controlled by the optional final parameter; see
[`k_work_queue_start()`](#c.k_work_queue_start) for details.

The following API can be used to interact with a workqueue:

- [`k_work_queue_drain()`](#c.k_work_queue_drain) can be used to block the caller until the
  work queue has no items left. Work items resubmitted from the workqueue
  thread are accepted while a queue is draining, but work items from any other
  thread or ISR are rejected. The restriction on submitting more work can be
  extended past the completion of the drain operation in order to allow the
  blocking thread to perform additional work while the queue is “plugged”.
  Note that draining a queue has no effect on scheduling or processing
  delayable items, but if the queue is plugged and the deadline expires the
  item will silently fail to be submitted.
- [`k_work_queue_unplug()`](#c.k_work_queue_unplug) removes any previous block on submission to
  the queue due to a previous drain operation.

### Submitting a Work Item

A work item is defined using a variable of type [`k_work`](#c.k_work). It must
be initialized by calling [`k_work_init()`](#c.k_work_init), unless it is defined using
[`K_WORK_DEFINE`](#c.K_WORK_DEFINE) in which case initialization is performed at
compile-time.

An initialized work item can be submitted to the system workqueue by
calling [`k_work_submit()`](#c.k_work_submit), or to a specified workqueue by
calling [`k_work_submit_to_queue()`](#c.k_work_submit_to_queue).

The following code demonstrates how an ISR can offload the printing
of error messages to the system workqueue. Note that if the ISR attempts
to resubmit the work item while it is still queued, the work item is left
unchanged and the associated error message will not be printed.

```c
struct device_info {
    struct k_work work;
    char name[16]
} my_device;

void my_isr(void *arg)
{
    ...
    if (error detected) {
        k_work_submit(&my_device.work);
    }
    ...
}

void print_error(struct k_work *item)
{
    struct device_info *the_device =
        CONTAINER_OF(item, struct device_info, work);
    printk("Got error on device %s\n", the_device->name);
}

/* initialize name info for a device */
strcpy(my_device.name, "FOO_dev");

/* initialize work item for printing device's error messages */
k_work_init(&my_device.work, print_error);

/* install my_isr() as interrupt handler for the device (not shown) */
...
```

The following API can be used to check the status of or synchronize with the
work item:

- [`k_work_busy_get()`](#c.k_work_busy_get) returns a snapshot of flags indicating work item
  state. A zero value indicates the work is not scheduled, submitted, being
  executed, or otherwise still being referenced by the workqueue
  infrastructure.
- [`k_work_is_pending()`](#c.k_work_is_pending) is a helper that indicates `true` if and only
  if the work is scheduled, queued, or running.
- [`k_work_flush()`](#c.k_work_flush) may be invoked from threads to block until the work
  item has completed. It returns immediately if the work is not pending.
- [`k_work_cancel()`](#c.k_work_cancel) attempts to prevent the work item from being
  executed. This may or may not be successful. This is safe to invoke
  from ISRs.
- [`k_work_cancel_sync()`](#c.k_work_cancel_sync) may be invoked from threads to block until
  the work completes; it will return immediately if the cancellation was
  successful or not necessary (the work wasn’t submitted or running). This
  can be used after [`k_work_cancel()`](#c.k_work_cancel) is invoked (from an ISR)` to
  confirm completion of an ISR-initiated cancellation.

### Scheduling a Delayable Work Item

A delayable work item is defined using a variable of type
[`k_work_delayable`](#c.k_work_delayable). It must be initialized by calling
[`k_work_init_delayable()`](#c.k_work_init_delayable).

For delayed work there are two common use cases, depending on whether a
deadline should be extended if a new event occurs. An example is collecting
data that comes in asynchronously, e.g. characters from a UART associated with
a keyboard. There are two APIs that submit work after a delay:

- [`k_work_schedule()`](#c.k_work_schedule) (or [`k_work_schedule_for_queue()`](#c.k_work_schedule_for_queue))
  schedules work to be executed at a specific time or after a delay. Further
  attempts to schedule the same item with this API before the delay completes
  will not change the time at which the item will be submitted to its queue.
  Use this if the policy is to keep collecting data until a specified delay
  since the **first** unprocessed data was received;
- [`k_work_reschedule()`](#c.k_work_reschedule) (or [`k_work_reschedule_for_queue()`](#c.k_work_reschedule_for_queue))
  unconditionally sets the deadline for the work, replacing any previous
  incomplete delay and changing the destination queue if necessary. Use this
  if the policy is to keep collecting data until a specified delay since the
  **last** unprocessed data was received.

If the work item is not scheduled both APIs behave the same. If
[`K_NO_WAIT`](../timing/clocks.md#c.K_NO_WAIT "K_NO_WAIT") is specified as the delay the behavior is as if the item
was immediately submitted directly to the target queue, without waiting for a
minimal timeout (unless [`k_work_schedule()`](#c.k_work_schedule) is used and a previous
delay has not completed).

Both also have variants that allow
control of the queue used for submission.

The helper function [`k_work_delayable_from_work()`](#c.k_work_delayable_from_work) can be used to get
a pointer to the containing [`k_work_delayable`](#c.k_work_delayable) from a pointer to
[`k_work`](#c.k_work) that is passed to a work handler function.

The following additional API can be used to check the status of or synchronize
with the work item:

- [`k_work_delayable_busy_get()`](#c.k_work_delayable_busy_get) is the analog to [`k_work_busy_get()`](#c.k_work_busy_get)
  for delayable work.
- [`k_work_delayable_is_pending()`](#c.k_work_delayable_is_pending) is the analog to
  [`k_work_is_pending()`](#c.k_work_is_pending) for delayable work.
- [`k_work_flush_delayable()`](#c.k_work_flush_delayable) is the analog to [`k_work_flush()`](#c.k_work_flush)
  for delayable work.
- [`k_work_cancel_delayable()`](#c.k_work_cancel_delayable) is the analog to
  [`k_work_cancel()`](#c.k_work_cancel) for delayable work; similarly with
  [`k_work_cancel_delayable_sync()`](#c.k_work_cancel_delayable_sync).

### Synchronizing with Work Items

While the state of both regular and delayable work items can be determined
from any context using [`k_work_busy_get()`](#c.k_work_busy_get) and
[`k_work_delayable_busy_get()`](#c.k_work_delayable_busy_get) some use cases require synchronizing
with work items after they’ve been submitted. [`k_work_flush()`](#c.k_work_flush),
[`k_work_cancel_sync()`](#c.k_work_cancel_sync), and [`k_work_cancel_delayable_sync()`](#c.k_work_cancel_delayable_sync)
can be invoked from thread context to wait until the requested state has been
reached.

These APIs must be provided with a [`k_work_sync`](#c.k_work_sync) object that has no
application-inspectable components but is needed to provide the
synchronization objects. These objects should not be allocated on a stack if
the code is expected to work on architectures with
[`CONFIG_KERNEL_COHERENCE`](../../../kconfig.md#CONFIG_KERNEL_COHERENCE "CONFIG_KERNEL_COHERENCE").

## [Workqueue Best Practices](#id6)

### Avoid Race Conditions

Sometimes the data a work item must process is naturally thread-safe, for
example when it’s put into a `k_queue` by some thread and processed
in the work thread. More often external synchronization is required to avoid
data races: cases where the work thread might inspect or manipulate shared
state that’s being accessed by another thread or interrupt. Such state might
be a flag indicating that work needs to be done, or a shared object that is
filled by an ISR or thread and read by the work handler.

For simple flags [Atomic Services](../other/atomic.md#atomic-v2) may be sufficient. In other cases spin
locks (`k_spinlock_t`) or thread-aware locks (`k_sem`,
[`k_mutex`](../synchronization/mutexes.md#c.k_mutex "k_mutex") , …) may be used to ensure data races don’t occur.

If the selected lock mechanism can [sleep](../../../develop/api/terminology.md#api-term-sleep) then allowing the
work thread to sleep will starve other work queue items, which may need to
make progress in order to get the lock released. Work handlers should try to
take the lock with its no-wait path. For example:

```c
static void work_handler(struct work *work)
{
        struct work_context *parent = CONTAINER_OF(work, struct work_context,
                                                   work_item);

        if (k_mutex_lock(&parent->lock, K_NO_WAIT) != 0) {
                /* NB: Submit will fail if the work item is being cancelled. */
                (void)k_work_submit(work);
                return;
        }

        /* do stuff under lock */
        k_mutex_unlock(&parent->lock);
        /* do stuff without lock */
}
```

Be aware that if the lock is held by a thread with a lower priority than the
work queue the resubmission may starve the thread that would release the lock,
causing the application to fail. Where the idiom above is required a
delayable work item is preferred, and the work should be (re-)scheduled with a
non-zero delay to allow the thread holding the lock to make progress.

Note that submitting from the work handler can fail if the work item had been
cancelled. Generally this is acceptable, since the cancellation will complete
once the handler finishes. If it is not, the code above must take other steps
to notify the application that the work could not be performed.

Work items in isolation are self-locking, so you don’t need to hold an
external lock just to submit or schedule them. Even if you use external state
protected by such a lock to prevent further resubmission, it’s safe to do the
resubmit as long as you’re sure that eventually the item will take its lock
and check that state to determine whether it should do anything. Where a
delayable work item is being rescheduled in its handler due to inability to
take the lock some other self-locking state, such as an atomic flag set by the
application/driver when the cancel is initiated, would be required to detect
the cancellation and avoid the cancelled work item being submitted again after
the deadline.

### Check Return Values

All work API functions return status of the underlying operation, and in many
cases it is important to verify that the intended result was obtained.

- Submitting a work item ([`k_work_submit_to_queue()`](#c.k_work_submit_to_queue)) can fail if the
  work is being cancelled or the queue is not accepting new items. If this
  happens the work will not be executed, which could cause a subsystem that is
  animated by work handler activity to become non-responsive.
- Asynchronous cancellation ([`k_work_cancel()`](#c.k_work_cancel) or
  [`k_work_cancel_delayable()`](#c.k_work_cancel_delayable)) can complete while the work item is still
  being run by a handler. Proceeding to manipulate state shared with the work
  handler will result in data races that can cause failures.

Many race conditions have been present in Zephyr code because the results of
an operation were not checked.

There may be good reason to believe that a return value indicating that the
operation did not complete as expected is not a problem. In those cases the
code should clearly document this, by (1) casting the return value to `void`
to indicate that the result is intentionally ignored, and (2) documenting what
happens in the unexpected case. For example:

```c
/* If this fails, the work handler will check pub->active and
 * exit without transmitting.
 */
(void)k_work_cancel_delayable(&pub->timer);
```

However in such a case the following code must still avoid data races, as it
cannot guarantee that the work thread is not accessing work-related state.

### Don’t Optimize Prematurely

The workqueue API is designed to be safe when invoked from multiple threads
and interrupts. Attempts to externally inspect a work item’s state and make
decisions based on the result are likely to create new problems.

So when new work comes in, just submit it. Don’t attempt to “optimize” by
checking whether the work item is already submitted by inspecting snapshot
state with [`k_work_is_pending()`](#c.k_work_is_pending) or [`k_work_busy_get()`](#c.k_work_busy_get), or
checking for a non-zero delay from
[`k_work_delayable_remaining_get()`](#c.k_work_delayable_remaining_get). Those checks are fragile: a “busy”
indication can be obsolete by the time the test is returned, and a “not-busy”
indication can also be wrong if work is submitted from multiple contexts, or
(for delayable work) if the deadline has completed but the work is still in
queued or running state.

A general best practice is to always maintain in shared state some condition
that can be checked by the handler to confirm whether there is work to be
done. This way you can use the work handler as the standard cleanup path:
rather than having to deal with cancellation and cleanup at points where items
are submitted, you may be able to have everything done in the work handler
itself.

A rare case where you could safely use [`k_work_is_pending()`](#c.k_work_is_pending) is as a
check to avoid invoking [`k_work_flush()`](#c.k_work_flush) or
[`k_work_cancel_sync()`](#c.k_work_cancel_sync), if you are *certain* that nothing else might
submit the work while you’re checking (generally because you’re holding a lock
that prevents access to state used for submission).

## [Suggested Uses](#id7)

Use the system workqueue to defer complex interrupt-related processing from an
ISR to a shared thread. This allows the interrupt-related processing to be
done promptly without compromising the system’s ability to respond to
subsequent interrupts, and does not require the application to define and
manage an additional thread to do the processing.

## [Configuration Options](#id8)

Related configuration options:

- [`CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE`](../../../kconfig.md#CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE "CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE")
- [`CONFIG_SYSTEM_WORKQUEUE_PRIORITY`](../../../kconfig.md#CONFIG_SYSTEM_WORKQUEUE_PRIORITY "CONFIG_SYSTEM_WORKQUEUE_PRIORITY")
- [`CONFIG_SYSTEM_WORKQUEUE_NO_YIELD`](../../../kconfig.md#CONFIG_SYSTEM_WORKQUEUE_NO_YIELD "CONFIG_SYSTEM_WORKQUEUE_NO_YIELD")

## [API Reference](#id9)

*group* workqueue\_apis
:   Defines

    K\_WORK\_DELAYABLE\_DEFINE(work, work\_handler)
    :   Initialize a statically-defined delayable work item.

        This macro can be used to initialize a statically-defined delayable work item, prior to its first use. For example,

        ```text
        static K_WORK_DELAYABLE_DEFINE(<dwork>, <work_handler>);
        ```

        Note that if the runtime dependencies support initialization with [k\_work\_init\_delayable()](#group__workqueue__apis_1ga2876c5d82fb2340a093bc4d689a55465) using that will eliminate the initialized object in ROM that is produced by this macro and copied in at system startup.

        Parameters:
        :   - **work** – Symbol name for delayable work item object
            - **work\_handler** – Function to invoke each time work item is processed.

    K\_WORK\_USER\_DEFINE(work, work\_handler)
    :   Initialize a statically-defined user work item.

        This macro can be used to initialize a statically-defined user work item, prior to its first use. For example,

        ```text
        static K_WORK_USER_DEFINE(<work>, <work_handler>);
        ```

        Parameters:
        :   - **work** – Symbol name for work item object
            - **work\_handler** – Function to invoke each time work item is processed.

    K\_WORK\_DEFINE(work, work\_handler)
    :   Initialize a statically-defined work item.

        This macro can be used to initialize a statically-defined workqueue work item, prior to its first use. For example,

        ```text
        static K_WORK_DEFINE(<work>, <work_handler>);
        ```

        Parameters:
        :   - **work** – Symbol name for work item object
            - **work\_handler** – Function to invoke each time work item is processed.

    Typedefs

    typedef void (\*k\_work\_handler\_t)(struct [k\_work](#c.k_work) \*work)
    :   The signature for a work item handler function.

        The function will be invoked by the thread animating a work queue.

        Param work:
        :   the work item that provided the handler.

    typedef void (\*k\_work\_user\_handler\_t)(struct k\_work\_user \*work)
    :   Work item handler function type for user work queues.

        A work item’s handler function is executed by a user workqueue’s thread when the work item is processed by the workqueue.

        Param work:
        :   Address of the work item.

    Enums

    enum [anonymous]
    :   *Values:*

        enumerator K\_WORK\_RUNNING = [BIT](../../util/index.md#c.BIT "BIT")(K\_WORK\_RUNNING\_BIT)
        :   Flag indicating a work item that is running under a work queue thread.

            Accessed via [k\_work\_busy\_get()](#group__workqueue__apis_1gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags.

        enumerator K\_WORK\_CANCELING = [BIT](../../util/index.md#c.BIT "BIT")(K\_WORK\_CANCELING\_BIT)
        :   Flag indicating a work item that is being canceled.

            Accessed via [k\_work\_busy\_get()](#group__workqueue__apis_1gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags.

        enumerator K\_WORK\_QUEUED = [BIT](../../util/index.md#c.BIT "BIT")(K\_WORK\_QUEUED\_BIT)
        :   Flag indicating a work item that has been submitted to a queue but has not started running.

            Accessed via [k\_work\_busy\_get()](#group__workqueue__apis_1gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags.

        enumerator K\_WORK\_DELAYED = [BIT](../../util/index.md#c.BIT "BIT")(K\_WORK\_DELAYED\_BIT)
        :   Flag indicating a delayed work item that is scheduled for submission to a queue.

            Accessed via [k\_work\_busy\_get()](#group__workqueue__apis_1gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags.

        enumerator K\_WORK\_FLUSHING = [BIT](../../util/index.md#c.BIT "BIT")(K\_WORK\_FLUSHING\_BIT)
        :   Flag indicating a synced work item that is being flushed.

            Accessed via [k\_work\_busy\_get()](#group__workqueue__apis_1gaba8a8734768d768b433f9d8490e7df7b). May co-occur with other flags.

    Functions

    void k\_work\_init(struct [k\_work](#c.k_work) \*work, [k\_work\_handler\_t](#c.k_work_handler_t) handler)
    :   Initialize a (non-delayable) work structure.

        This must be invoked before submitting a work structure for the first time. It need not be invoked again on the same work structure. It can be re-invoked to change the associated handler, but this must be done when the work item is idle.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **work** – the work structure to be initialized.
            - **handler** – the handler to be invoked by the work item.

    int k\_work\_busy\_get(const struct [k\_work](#c.k_work) \*work)
    :   Busy state flags from the work item.

        A zero return value indicates the work item appears to be idle.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        This is a live snapshot of state, which may change before the result is checked. Use locks where appropriate.

        Parameters:
        :   - **work** – pointer to the work item.

        Returns:
        :   a mask of flags K\_WORK\_DELAYED, K\_WORK\_QUEUED, K\_WORK\_RUNNING, K\_WORK\_CANCELING, and K\_WORK\_FLUSHING.

    static inline bool k\_work\_is\_pending(const struct [k\_work](#c.k_work) \*work)
    :   Test whether a work item is currently pending.

        Wrapper to determine whether a work item is in a non-idle dstate.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        This is a live snapshot of state, which may change before the result is checked. Use locks where appropriate.

        Parameters:
        :   - **work** – pointer to the work item.

        Returns:
        :   true if and only if [k\_work\_busy\_get()](#group__workqueue__apis_1gaba8a8734768d768b433f9d8490e7df7b) returns a non-zero value.

    int k\_work\_submit\_to\_queue(struct [k\_work\_q](#c.k_work_q) \*queue, struct [k\_work](#c.k_work) \*work)
    :   Submit a work item to a queue.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – pointer to the work queue on which the item should run. If NULL the queue from the most recent submission will be used.
            - **work** – pointer to the work item.

        Return values:
        :   - **0** – if work was already submitted to a queue
            - **1** – if work was not submitted and has been queued to `queue`
            - **2** – if work was running and has been queued to the queue that was running it
            - **-EBUSY** –

              - if work submission was rejected because the work item is cancelling; or
              - `queue` is draining; or
              - `queue` is plugged.
            - **-EINVAL** – if `queue` is null and the work item has never been run.
            - **-ENODEV** – if `queue` has not been started.

    int k\_work\_submit(struct [k\_work](#c.k_work) \*work)
    :   Submit a work item to the system queue.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **work** – pointer to the work item.

        Returns:
        :   as with [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c).

    bool k\_work\_flush(struct [k\_work](#c.k_work) \*work, struct [k\_work\_sync](#c.k_work_sync) \*sync)
    :   Wait for last-submitted instance to complete.

        Resubmissions may occur while waiting, including chained submissions (from within the handler).

        Note

        Be careful of caller and work queue thread relative priority. If this function sleeps it will not return until the work queue thread completes the tasks that allow this thread to resume.

        Note

        Behavior is undefined if this function is invoked on `work` from a work queue running `work`.

        Parameters:
        :   - **work** – pointer to the work item.
            - **sync** – pointer to an opaque item containing state related to the pending cancellation. The object must persist until the call returns, and be accessible from both the caller thread and the work queue thread. The object must not be used for any other flush or cancel operation until this one completes. On architectures with CONFIG\_KERNEL\_COHERENCE the object must be allocated in coherent memory.

        Return values:
        :   - **true** – if call had to wait for completion
            - **false** – if work was already idle

    int k\_work\_cancel(struct [k\_work](#c.k_work) \*work)
    :   Cancel a work item.

        This attempts to prevent a pending (non-delayable) work item from being processed by removing it from the work queue. If the item is being processed, the work item will continue to be processed, but resubmissions are rejected until cancellation completes.

        If this returns zero cancellation is complete, otherwise something (probably a work queue thread) is still referencing the item.

        See also [k\_work\_cancel\_sync()](#group__workqueue__apis_1gab2b05cfe3af08f7d32c3946fa1c808f9).

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **work** – pointer to the work item.

        Returns:
        :   the [k\_work\_busy\_get()](#group__workqueue__apis_1gaba8a8734768d768b433f9d8490e7df7b) status indicating the state of the item after all cancellation steps performed by this call are completed.

    bool k\_work\_cancel\_sync(struct [k\_work](#c.k_work) \*work, struct [k\_work\_sync](#c.k_work_sync) \*sync)
    :   Cancel a work item and wait for it to complete.

        Same as [k\_work\_cancel()](#group__workqueue__apis_1ga389fe2a8fb20f9bd593cf8d990727078) but does not return until cancellation is complete. This can be invoked by a thread after [k\_work\_cancel()](#group__workqueue__apis_1ga389fe2a8fb20f9bd593cf8d990727078) to synchronize with a previous cancellation.

        On return the work structure will be idle unless something submits it after the cancellation was complete.

        Note

        Be careful of caller and work queue thread relative priority. If this function sleeps it will not return until the work queue thread completes the tasks that allow this thread to resume.

        Note

        Behavior is undefined if this function is invoked on `work` from a work queue running `work`.

        Parameters:
        :   - **work** – pointer to the work item.
            - **sync** – pointer to an opaque item containing state related to the pending cancellation. The object must persist until the call returns, and be accessible from both the caller thread and the work queue thread. The object must not be used for any other flush or cancel operation until this one completes. On architectures with CONFIG\_KERNEL\_COHERENCE the object must be allocated in coherent memory.

        Return values:
        :   - **true** – if work was pending (call had to wait for cancellation of a running handler to complete, or scheduled or submitted operations were cancelled);
            - **false** – otherwise

    void k\_work\_queue\_init(struct [k\_work\_q](#c.k_work_q) \*queue)
    :   Initialize a work queue structure.

        This must be invoked before starting a work queue structure for the first time. It need not be invoked again on the same work queue structure.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – the queue structure to be initialized.

    void k\_work\_queue\_start(struct [k\_work\_q](#c.k_work_q) \*queue, k\_thread\_stack\_t \*stack, size\_t stack\_size, int prio, const struct [k\_work\_queue\_config](#c.k_work_queue_config) \*cfg)
    :   Initialize a work queue.

        This configures the work queue thread and starts it running. The function should not be re-invoked on a queue.

        Parameters:
        :   - **queue** – pointer to the queue structure. It must be initialized in zeroed/bss memory or with [k\_work\_queue\_init](#group__workqueue__apis_1gada77d818ea9e4d07c14a960872ed5492) before use.
            - **stack** – pointer to the work thread stack area.
            - **stack\_size** – size of the the work thread stack area, in bytes.
            - **prio** – initial thread priority
            - **cfg** – optional additional configuration parameters. Pass `NULL` if not required, to use the defaults documented in [k\_work\_queue\_config](#structk__work__queue__config).

    static inline k\_tid\_t k\_work\_queue\_thread\_get(struct [k\_work\_q](#c.k_work_q) \*queue)
    :   Access the thread that animates a work queue.

        This is necessary to grant a work queue thread access to things the work items it will process are expected to use.

        Parameters:
        :   - **queue** – pointer to the queue structure.

        Returns:
        :   the thread associated with the work queue.

    int k\_work\_queue\_drain(struct [k\_work\_q](#c.k_work_q) \*queue, bool plug)
    :   Wait until the work queue has drained, optionally plugging it.

        This blocks submission to the work queue except when coming from queue thread, and blocks the caller until no more work items are available in the queue.

        If `plug` is true then submission will continue to be blocked after the drain operation completes until [k\_work\_queue\_unplug()](#group__workqueue__apis_1gaa0463bb79af3ec470f7d3be02052139f) is invoked.

        Note that work items that are delayed are not yet associated with their work queue. They must be cancelled externally if a goal is to ensure the work queue remains empty. The `plug` feature can be used to prevent delayed items from being submitted after the drain completes.

        Parameters:
        :   - **queue** – pointer to the queue structure.
            - **plug** – if true the work queue will continue to block new submissions after all items have drained.

        Return values:
        :   - **1** – if call had to wait for the drain to complete
            - **0** – if call did not have to wait
            - **negative** – if wait was interrupted or failed

    int k\_work\_queue\_unplug(struct [k\_work\_q](#c.k_work_q) \*queue)
    :   Release a work queue to accept new submissions.

        This releases the block on new submissions placed when [k\_work\_queue\_drain()](#group__workqueue__apis_1ga0fefe3e0225ac99b47b250849f6cd863) is invoked with the `plug` option enabled. If this is invoked before the drain completes new items may be submitted as soon as the drain completes.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – pointer to the queue structure.

        Return values:
        :   - **0** – if successfully unplugged
            - **-EALREADY** – if the work queue was not plugged.

    void k\_work\_init\_delayable(struct [k\_work\_delayable](#c.k_work_delayable) \*dwork, [k\_work\_handler\_t](#c.k_work_handler_t) handler)
    :   Initialize a delayable work structure.

        This must be invoked before scheduling a delayable work structure for the first time. It need not be invoked again on the same work structure. It can be re-invoked to change the associated handler, but this must be done when the work item is idle.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dwork** – the delayable work structure to be initialized.
            - **handler** – the handler to be invoked by the work item.

    static inline struct [k\_work\_delayable](#c.k_work_delayable) \*k\_work\_delayable\_from\_work(struct [k\_work](#c.k_work) \*work)
    :   Get the parent delayable work structure from a work pointer.

        This function is necessary when a `[k_work_handler_t](#group__workqueue__apis_1ga5add9ef0dce306a08413c4140fc0bdda)` function is passed to [k\_work\_schedule\_for\_queue()](#group__workqueue__apis_1ga17f863c9f6ff2fb41dc0f3b7de4fdf23) and the handler needs to access data from the container of the containing `[k_work_delayable](#structk__work__delayable)`.

        Parameters:
        :   - **work** – Address passed to the work handler

        Returns:
        :   Address of the containing `[k_work_delayable](#structk__work__delayable)` structure.

    int k\_work\_delayable\_busy\_get(const struct [k\_work\_delayable](#c.k_work_delayable) \*dwork)
    :   Busy state flags from the delayable work item.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        This is a live snapshot of state, which may change before the result can be inspected. Use locks where appropriate.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.

        Returns:
        :   a mask of flags K\_WORK\_DELAYED, K\_WORK\_QUEUED, K\_WORK\_RUNNING, K\_WORK\_CANCELING, and K\_WORK\_FLUSHING. A zero return value indicates the work item appears to be idle.

    static inline bool k\_work\_delayable\_is\_pending(const struct [k\_work\_delayable](#c.k_work_delayable) \*dwork)
    :   Test whether a delayed work item is currently pending.

        Wrapper to determine whether a delayed work item is in a non-idle state.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        This is a live snapshot of state, which may change before the result can be inspected. Use locks where appropriate.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.

        Returns:
        :   true if and only if [k\_work\_delayable\_busy\_get()](#group__workqueue__apis_1ga1b76969667844f0981d348c9c671bc9f) returns a non-zero value.

    static inline [k\_ticks\_t](../timing/clocks.md#c.k_ticks_t "k_ticks_t") k\_work\_delayable\_expires\_get(const struct [k\_work\_delayable](#c.k_work_delayable) \*dwork)
    :   Get the absolute tick count at which a scheduled delayable work will be submitted.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        This is a live snapshot of state, which may change before the result can be inspected. Use locks where appropriate.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.

        Returns:
        :   the tick count when the timer that will schedule the work item will expire, or the current tick count if the work is not scheduled.

    static inline [k\_ticks\_t](../timing/clocks.md#c.k_ticks_t "k_ticks_t") k\_work\_delayable\_remaining\_get(const struct [k\_work\_delayable](#c.k_work_delayable) \*dwork)
    :   Get the number of ticks until a scheduled delayable work will be submitted.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        This is a live snapshot of state, which may change before the result can be inspected. Use locks where appropriate.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.

        Returns:
        :   the number of ticks until the timer that will schedule the work item will expire, or zero if the item is not scheduled.

    int k\_work\_schedule\_for\_queue(struct [k\_work\_q](#c.k_work_q) \*queue, struct [k\_work\_delayable](#c.k_work_delayable) \*dwork, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") delay)
    :   Submit an idle work item to a queue after a delay.

        Unlike [k\_work\_reschedule\_for\_queue()](#group__workqueue__apis_1gabf5db091eac19b19a4e12c0cb381f0a8) this is a no-op if the work item is already scheduled or submitted, even if `delay` is `K_NO_WAIT`.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – the queue on which the work item should be submitted after the delay.
            - **dwork** – pointer to the delayable work item.
            - **delay** – the time to wait before submitting the work item. If `K_NO_WAIT` and the work is not pending this is equivalent to [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c).

        Return values:
        :   - **0** – if work was already scheduled or submitted.
            - **1** – if work has been scheduled.
            - **-EBUSY** – if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c) fails with this code.
            - **-EINVAL** – if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c) fails with this code.
            - **-ENODEV** – if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c) fails with this code.

    int k\_work\_schedule(struct [k\_work\_delayable](#c.k_work_delayable) \*dwork, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") delay)
    :   Submit an idle work item to the system work queue after a delay.

        This is a thin wrapper around [k\_work\_schedule\_for\_queue()](#group__workqueue__apis_1ga17f863c9f6ff2fb41dc0f3b7de4fdf23), with all the API characteristics of that function.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.
            - **delay** – the time to wait before submitting the work item. If `K_NO_WAIT` this is equivalent to [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c).

        Returns:
        :   as with [k\_work\_schedule\_for\_queue()](#group__workqueue__apis_1ga17f863c9f6ff2fb41dc0f3b7de4fdf23).

    int k\_work\_reschedule\_for\_queue(struct [k\_work\_q](#c.k_work_q) \*queue, struct [k\_work\_delayable](#c.k_work_delayable) \*dwork, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") delay)
    :   Reschedule a work item to a queue after a delay.

        Unlike [k\_work\_schedule\_for\_queue()](#group__workqueue__apis_1ga17f863c9f6ff2fb41dc0f3b7de4fdf23) this function can change the deadline of a scheduled work item, and will schedule a work item that is in any state (e.g. is idle, submitted, or running). This function does not affect (“unsubmit”) a work item that has been submitted to a queue.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        If delay is `K_NO_WAIT` (“no delay”) the return values are as with [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c).

        Parameters:
        :   - **queue** – the queue on which the work item should be submitted after the delay.
            - **dwork** – pointer to the delayable work item.
            - **delay** – the time to wait before submitting the work item. If `K_NO_WAIT` this is equivalent to [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c) after canceling any previous scheduled submission.

        Return values:
        :   - **0** – if delay is `K_NO_WAIT` and work was already on a queue
            - **1** – if

              - delay is `K_NO_WAIT` and work was not submitted but has now been queued to `queue`; or
              - delay not `K_NO_WAIT` and work has been scheduled
            - **2** – if delay is `K_NO_WAIT` and work was running and has been queued to the queue that was running it
            - **-EBUSY** – if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c) fails with this code.
            - **-EINVAL** – if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c) fails with this code.
            - **-ENODEV** – if `delay` is `K_NO_WAIT` and [k\_work\_submit\_to\_queue()](#group__workqueue__apis_1ga5353e76f73db070614f50d06d292d05c) fails with this code.

    int k\_work\_reschedule(struct [k\_work\_delayable](#c.k_work_delayable) \*dwork, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") delay)
    :   Reschedule a work item to the system work queue after a delay.

        This is a thin wrapper around [k\_work\_reschedule\_for\_queue()](#group__workqueue__apis_1gabf5db091eac19b19a4e12c0cb381f0a8), with all the API characteristics of that function.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.
            - **delay** – the time to wait before submitting the work item.

        Returns:
        :   as with [k\_work\_reschedule\_for\_queue()](#group__workqueue__apis_1gabf5db091eac19b19a4e12c0cb381f0a8).

    bool k\_work\_flush\_delayable(struct [k\_work\_delayable](#c.k_work_delayable) \*dwork, struct [k\_work\_sync](#c.k_work_sync) \*sync)
    :   Flush delayable work.

        If the work is scheduled, it is immediately submitted. Then the caller blocks until the work completes, as with [k\_work\_flush()](#group__workqueue__apis_1gabd1cda459bab538fb2d6dfd84a73b253).

        Note

        Be careful of caller and work queue thread relative priority. If this function sleeps it will not return until the work queue thread completes the tasks that allow this thread to resume.

        Note

        Behavior is undefined if this function is invoked on `dwork` from a work queue running `dwork`.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.
            - **sync** – pointer to an opaque item containing state related to the pending cancellation. The object must persist until the call returns, and be accessible from both the caller thread and the work queue thread. The object must not be used for any other flush or cancel operation until this one completes. On architectures with CONFIG\_KERNEL\_COHERENCE the object must be allocated in coherent memory.

        Return values:
        :   - **true** – if call had to wait for completion
            - **false** – if work was already idle

    int k\_work\_cancel\_delayable(struct [k\_work\_delayable](#c.k_work_delayable) \*dwork)
    :   Cancel delayable work.

        Similar to [k\_work\_cancel()](#group__workqueue__apis_1ga389fe2a8fb20f9bd593cf8d990727078) but for delayable work. If the work is scheduled or submitted it is canceled. This function does not wait for the cancellation to complete.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        The work may still be running when this returns. Use [k\_work\_flush\_delayable()](#group__workqueue__apis_1gad47d54e513030304be2600d75b1a965f) or [k\_work\_cancel\_delayable\_sync()](#group__workqueue__apis_1ga7e7ec237648556fc16bfda8d35f7cd86) to ensure it is not running.

        Note

        Canceling delayable work does not prevent rescheduling it. It does prevent submitting it until the cancellation completes.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.

        Returns:
        :   the [k\_work\_delayable\_busy\_get()](#group__workqueue__apis_1ga1b76969667844f0981d348c9c671bc9f) status indicating the state of the item after all cancellation steps performed by this call are completed.

    bool k\_work\_cancel\_delayable\_sync(struct [k\_work\_delayable](#c.k_work_delayable) \*dwork, struct [k\_work\_sync](#c.k_work_sync) \*sync)
    :   Cancel delayable work and wait.

        Like [k\_work\_cancel\_delayable()](#group__workqueue__apis_1ga92355914ee178d4c3e848a1946bed3e4) but waits until the work becomes idle.

        Note

        Canceling delayable work does not prevent rescheduling it. It does prevent submitting it until the cancellation completes.

        Note

        Be careful of caller and work queue thread relative priority. If this function sleeps it will not return until the work queue thread completes the tasks that allow this thread to resume.

        Note

        Behavior is undefined if this function is invoked on `dwork` from a work queue running `dwork`.

        Parameters:
        :   - **dwork** – pointer to the delayable work item.
            - **sync** – pointer to an opaque item containing state related to the pending cancellation. The object must persist until the call returns, and be accessible from both the caller thread and the work queue thread. The object must not be used for any other flush or cancel operation until this one completes. On architectures with CONFIG\_KERNEL\_COHERENCE the object must be allocated in coherent memory.

        Return values:
        :   - **true** – if work was not idle (call had to wait for cancellation of a running handler to complete, or scheduled or submitted operations were cancelled);
            - **false** – otherwise

    static inline void k\_work\_user\_init(struct k\_work\_user \*work, [k\_work\_user\_handler\_t](#c.k_work_user_handler_t) handler)
    :   Initialize a userspace work item.

        This routine initializes a user workqueue work item, prior to its first use.

        Parameters:
        :   - **work** – Address of work item.
            - **handler** – Function to invoke each time work item is processed.

    static inline bool k\_work\_user\_is\_pending(struct k\_work\_user \*work)
    :   Check if a userspace work item is pending.

        This routine indicates if user work item *work* is pending in a workqueue’s queue.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        Checking if the work is pending gives no guarantee that the work will still be pending when this information is used. It is up to the caller to make sure that this information is used in a safe manner.

        Parameters:
        :   - **work** – Address of work item.

        Returns:
        :   true if work item is pending, or false if it is not pending.

    static inline int k\_work\_user\_submit\_to\_queue(struct k\_work\_user\_q \*work\_q, struct k\_work\_user \*work)
    :   Submit a work item to a user mode workqueue.

        Submits a work item to a workqueue that runs in user mode. A temporary memory allocation is made from the caller’s resource pool which is freed once the worker thread consumes the [k\_work](#structk__work) item. The workqueue thread must have memory access to the [k\_work](#structk__work) item being submitted. The caller must have permission granted on the work\_q parameter’s queue object.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **work\_q** – Address of workqueue.
            - **work** – Address of work item.

        Return values:
        :   - **-EBUSY** – if the work item was already in some workqueue
            - **-ENOMEM** – if no memory for thread resource pool allocation
            - **0** – Success

    void k\_work\_user\_queue\_start(struct k\_work\_user\_q \*work\_q, k\_thread\_stack\_t \*stack, size\_t stack\_size, int prio, const char \*name)
    :   Start a workqueue in user mode.

        This works identically to [k\_work\_queue\_start()](#group__workqueue__apis_1gadfc56554f9bfe7b52309d79660188593) except it is callable from user mode, and the worker thread created will run in user mode. The caller must have permissions granted on both the work\_q parameter’s thread and queue objects, and the same restrictions on priority apply as [k\_thread\_create()](index.md#group__thread__apis_1gad5b0bff3102f1656089f5875d999a367).

        Parameters:
        :   - **work\_q** – Address of workqueue.
            - **stack** – Pointer to work queue thread’s stack space, as defined by [K\_THREAD\_STACK\_DEFINE()](index.md#group__thread__stack__api_1gac5368ce24fdeab3863b5c8dee2ebd955)
            - **stack\_size** – Size of the work queue thread’s stack (in bytes), which should either be the same constant passed to [K\_THREAD\_STACK\_DEFINE()](index.md#group__thread__stack__api_1gac5368ce24fdeab3863b5c8dee2ebd955) or the value of [K\_THREAD\_STACK\_SIZEOF()](index.md#group__thread__stack__api_1ga775f8e6b4144cfdd24f3261b6db64150).
            - **prio** – Priority of the work queue’s thread.
            - **name** – optional thread name. If not null a copy is made into the thread’s name buffer.

    static inline k\_tid\_t k\_work\_user\_queue\_thread\_get(struct k\_work\_user\_q \*work\_q)
    :   Access the user mode thread that animates a work queue.

        This is necessary to grant a user mode work queue thread access to things the work items it will process are expected to use.

        Parameters:
        :   - **work\_q** – pointer to the user mode queue structure.

        Returns:
        :   the user mode thread associated with the work queue.

    void k\_work\_poll\_init(struct k\_work\_poll \*work, [k\_work\_handler\_t](#c.k_work_handler_t) handler)
    :   Initialize a triggered work item.

        This routine initializes a workqueue triggered work item, prior to its first use.

        Parameters:
        :   - **work** – Address of triggered work item.
            - **handler** – Function to invoke each time work item is processed.

    int k\_work\_poll\_submit\_to\_queue(struct [k\_work\_q](#c.k_work_q) \*work\_q, struct k\_work\_poll \*work, struct [k\_poll\_event](../polling.md#c.k_poll_event "k_poll_event") \*events, int num\_events, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Submit a triggered work item.

        This routine schedules work item *work* to be processed by workqueue *work\_q* when one of the given *events* is signaled. The routine initiates internal poller for the work item and then returns to the caller. Only when one of the watched events happen the work item is actually submitted to the workqueue and becomes pending.

        Submitting a previously submitted triggered work item that is still waiting for the event cancels the existing submission and reschedules it the using the new event list. Note that this behavior is inherently subject to race conditions with the pre-existing triggered work item and work queue, so care must be taken to synchronize such resubmissions externally.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Warning

        Provided array of events as well as a triggered work item must be placed in persistent memory (valid until work handler execution or work cancellation) and cannot be modified after submission.

        Parameters:
        :   - **work\_q** – Address of workqueue.
            - **work** – Address of delayed work item.
            - **events** – An array of events which trigger the work.
            - **num\_events** – The number of events in the array.
            - **timeout** – Timeout after which the work will be scheduled for execution even if not triggered.

        Return values:
        :   - **0** – Work item started watching for events.
            - **-EINVAL** – Work item is being processed or has completed its work.
            - **-EADDRINUSE** – Work item is pending on a different workqueue.

    int k\_work\_poll\_submit(struct k\_work\_poll \*work, struct [k\_poll\_event](../polling.md#c.k_poll_event "k_poll_event") \*events, int num\_events, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Submit a triggered work item to the system workqueue.

        This routine schedules work item *work* to be processed by system workqueue when one of the given *events* is signaled. The routine initiates internal poller for the work item and then returns to the caller. Only when one of the watched events happen the work item is actually submitted to the workqueue and becomes pending.

        Submitting a previously submitted triggered work item that is still waiting for the event cancels the existing submission and reschedules it the using the new event list. Note that this behavior is inherently subject to race conditions with the pre-existing triggered work item and work queue, so care must be taken to synchronize such resubmissions externally.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Warning

        Provided array of events as well as a triggered work item must not be modified until the item has been processed by the workqueue.

        Parameters:
        :   - **work** – Address of delayed work item.
            - **events** – An array of events which trigger the work.
            - **num\_events** – The number of events in the array.
            - **timeout** – Timeout after which the work will be scheduled for execution even if not triggered.

        Return values:
        :   - **0** – Work item started watching for events.
            - **-EINVAL** – Work item is being processed or has completed its work.
            - **-EADDRINUSE** – Work item is pending on a different workqueue.

    int k\_work\_poll\_cancel(struct k\_work\_poll \*work)
    :   Cancel a triggered work item.

        This routine cancels the submission of triggered work item *work*. A triggered work item can only be canceled if no event triggered work submission.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **work** – Address of delayed work item.

        Return values:
        :   - **0** – Work item canceled.
            - **-EINVAL** – Work item is being processed or has completed its work.

    struct k\_work
    :   *#include <kernel.h>*

        A structure used to submit work.

    struct k\_work\_delayable
    :   *#include <kernel.h>*

        A structure used to submit work after a delay.

    struct k\_work\_sync
    :   *#include <kernel.h>*

        A structure holding internal state for a pending synchronous operation on a work item or queue.

        Instances of this type are provided by the caller for invocation of [k\_work\_flush()](#group__workqueue__apis_1gabd1cda459bab538fb2d6dfd84a73b253), [k\_work\_cancel\_sync()](#group__workqueue__apis_1gab2b05cfe3af08f7d32c3946fa1c808f9) and sibling flush and cancel APIs. A referenced object must persist until the call returns, and be accessible from both the caller thread and the work queue thread.

        Note

        If CONFIG\_KERNEL\_COHERENCE is enabled the object must be allocated in coherent memory; see [arch\_mem\_coherent()](../../../hardware/porting/arch.md#group__arch-userspace_1ga8c6bb0f6730c115689452b016ac1761f). The stack on these architectures is generally not coherent. be stack-allocated. Violations are detected by runtime assertion.

    struct k\_work\_queue\_config
    :   *#include <kernel.h>*

        A structure holding optional configuration items for a work queue.

        This structure, and values it references, are not retained by [k\_work\_queue\_start()](#group__workqueue__apis_1gadfc56554f9bfe7b52309d79660188593).

        Public Members

        const char \*name
        :   The name to be given to the work queue thread.

            If left null the thread will not have a name.

        bool no\_yield
        :   Control whether the work queue thread should yield between items.

            Yielding between items helps guarantee the work queue thread does not starve other threads, including cooperative ones released by a work item. This is the default behavior.

            Set this to `true` to prevent the work queue thread from yielding between items. This may be appropriate when a sequence of items should complete without yielding control.

    struct k\_work\_q
    :   *#include <kernel.h>*

        A structure used to hold work until it can be processed.
