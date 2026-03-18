---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/polling.html
original_path: kernel/services/polling.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Polling API

The polling API is used to wait concurrently for any one of multiple conditions
to be fulfilled.

## [Concepts](#id1)

The polling API’s main function is [`k_poll()`](#c.k_poll), which is very similar
in concept to the POSIX [`poll()`](../../connectivity/networking/api/sockets.md#c.poll "poll") function, except that it operates on
kernel objects rather than on file descriptors.

The polling API allows a single thread to wait concurrently for one or more
conditions to be fulfilled without actively looking at each one individually.

There is a limited set of such conditions:

- a semaphore becomes available
- a kernel FIFO contains data ready to be retrieved
- a kernel message queue contains data ready to be retrieved
- a kernel pipe contains data ready to be retrieved
- a poll signal is raised

A thread that wants to wait on multiple conditions must define an array of
**poll events**, one for each condition.

All events in the array must be initialized before the array can be polled on.

Each event must specify which **type** of condition must be satisfied so that
its state is changed to signal the requested condition has been met.

Each event must specify what **kernel object** it wants the condition to be
satisfied.

Each event must specify which **mode** of operation is used when the condition
is satisfied.

Each event can optionally specify a **tag** to group multiple events together,
to the user’s discretion.

Apart from the kernel objects, there is also a **poll signal** pseudo-object
type that be directly signaled.

The [`k_poll()`](#c.k_poll) function returns as soon as one of the conditions it
is waiting for is fulfilled. It is possible for more than one to be fulfilled
when [`k_poll()`](#c.k_poll) returns, if they were fulfilled before
[`k_poll()`](#c.k_poll) was called, or due to the preemptive multi-threading
nature of the kernel. The caller must look at the state of all the poll events
in the array to figure out which ones were fulfilled and what actions to take.

Currently, there is only one mode of operation available: the object is not
acquired. As an example, this means that when [`k_poll()`](#c.k_poll) returns and
the poll event states that the semaphore is available, the caller of
[`k_poll()`](#c.k_poll) must then invoke [`k_sem_take()`](synchronization/semaphores.md#c.k_sem_take "k_sem_take") to take
ownership of the semaphore. If the semaphore is contested, there is no
guarantee that it will be still available when [`k_sem_take()`](synchronization/semaphores.md#c.k_sem_take "k_sem_take") is
called.

## [Implementation](#id2)

### [Using k\_poll()](#id3)

The main API is [`k_poll()`](#c.k_poll), which operates on an array of poll events
of type [`k_poll_event`](#c.k_poll_event). Each entry in the array represents one
event a call to [`k_poll()`](#c.k_poll) will wait for its condition to be
fulfilled.

Poll events can be initialized using either the runtime initializers
[`K_POLL_EVENT_INITIALIZER()`](#c.K_POLL_EVENT_INITIALIZER) or [`k_poll_event_init()`](#c.k_poll_event_init), or
the static initializer [`K_POLL_EVENT_STATIC_INITIALIZER()`](#c.K_POLL_EVENT_STATIC_INITIALIZER). An object
that matches the **type** specified must be passed to the initializers. The
**mode** *must* be set to [`K_POLL_MODE_NOTIFY_ONLY`](#c.k_poll_modes.K_POLL_MODE_NOTIFY_ONLY). The state *must*
be set to [`K_POLL_STATE_NOT_READY`](#c.K_POLL_STATE_NOT_READY) (the initializers take care of
this). The user **tag** is optional and completely opaque to the API: it is
there to help a user to group similar events together. Being optional, it is
passed to the static initializer, but not the runtime ones for performance
reasons. If using runtime initializers, the user must set it separately in the
[`k_poll_event`](#c.k_poll_event) data structure. If an event in the array is to be
ignored, most likely temporarily, its type can be set to K\_POLL\_TYPE\_IGNORE.

```c
struct k_poll_event events[4] = {
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_SEM_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_sem, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_FIFO_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_fifo, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_MSGQ_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_msgq, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_PIPE_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_pipe, 0),
};
```

or at runtime

```c
struct k_poll_event events[4];
void some_init(void)
{
    k_poll_event_init(&events[0],
                      K_POLL_TYPE_SEM_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_sem);

    k_poll_event_init(&events[1],
                      K_POLL_TYPE_FIFO_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_fifo);

    k_poll_event_init(&events[2],
                      K_POLL_TYPE_MSGQ_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_msgq);

    k_poll_event_init(&events[3],
                      K_POLL_TYPE_PIPE_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_pipe);

    // tags are left uninitialized if unused
}
```

After the events are initialized, the array can be passed to
[`k_poll()`](#c.k_poll). A timeout can be specified to wait only for a specified
amount of time, or the special values [`K_NO_WAIT`](timing/clocks.md#c.K_NO_WAIT "K_NO_WAIT") and
[`K_FOREVER`](timing/clocks.md#c.K_FOREVER "K_FOREVER") to either not wait or wait until an event condition is
satisfied and not sooner.

A list of pollers is offered on each semaphore or FIFO and as many events
can wait in it as the app wants.
Notice that the waiters will be served in first-come-first-serve order,
not in priority order.

In case of success, [`k_poll()`](#c.k_poll) returns 0. If it times out, it returns
-[`EAGAIN`](../../develop/languages/c/minimal_libc.md#c.EAGAIN "EAGAIN").

```c
// assume there is no contention on this semaphore and FIFO
// -EADDRINUSE will not occur; the semaphore and/or data will be available

void do_stuff(void)
{
    rc = k_poll(events, 2, 1000);
    if (rc == 0) {
        if (events[0].state == K_POLL_STATE_SEM_AVAILABLE) {
            k_sem_take(events[0].sem, 0);
        } else if (events[1].state == K_POLL_STATE_FIFO_DATA_AVAILABLE) {
            data = k_fifo_get(events[1].fifo, 0);
            // handle data
        } else if (events[2].state == K_POLL_STATE_MSGQ_DATA_AVAILABLE) {
            ret = k_msgq_get(events[2].msgq, buf, K_NO_WAIT);
            // handle data
        } else if (events[3].state == K_POLL_STATE_PIPE_DATA_AVAILABLE) {
            ret = k_pipe_get(events[3].pipe, buf, bytes_to_read, &bytes_read, min_xfer, K_NO_WAIT);
            // handle data
        }
    } else {
        // handle timeout
    }
}
```

When [`k_poll()`](#c.k_poll) is called in a loop, the events state must be reset
to [`K_POLL_STATE_NOT_READY`](#c.K_POLL_STATE_NOT_READY) by the user.

```c
void do_stuff(void)
{
    for(;;) {
        rc = k_poll(events, 2, K_FOREVER);
        if (events[0].state == K_POLL_STATE_SEM_AVAILABLE) {
            k_sem_take(events[0].sem, 0);
        } else if (events[1].state == K_POLL_STATE_FIFO_DATA_AVAILABLE) {
            data = k_fifo_get(events[1].fifo, 0);
            // handle data
        } else if (events[2].state == K_POLL_STATE_MSGQ_DATA_AVAILABLE) {
            ret = k_msgq_get(events[2].msgq, buf, K_NO_WAIT);
            // handle data
        } else if (events[3].state == K_POLL_STATE_PIPE_DATA_AVAILABLE) {
            ret = k_pipe_get(events[3].pipe, buf, bytes_to_read, &bytes_read, min_xfer, K_NO_WAIT);
            // handle data
        events[0].state = K_POLL_STATE_NOT_READY;
        events[1].state = K_POLL_STATE_NOT_READY;
        events[2].state = K_POLL_STATE_NOT_READY;
        events[3].state = K_POLL_STATE_NOT_READY;
    }
}
```

### [Using k\_poll\_signal\_raise()](#id4)

One of the types of events is [`K_POLL_TYPE_SIGNAL`](#c.K_POLL_TYPE_SIGNAL): this is a “direct”
signal to a poll event. This can be seen as a lightweight binary semaphore only
one thread can wait for.

A poll signal is a separate object of type [`k_poll_signal`](#c.k_poll_signal) that
must be attached to a k\_poll\_event, similar to a semaphore or FIFO. It must
first be initialized either via [`K_POLL_SIGNAL_INITIALIZER()`](#c.K_POLL_SIGNAL_INITIALIZER) or
[`k_poll_signal_init()`](#c.k_poll_signal_init).

```c
struct k_poll_signal signal;
void do_stuff(void)
{
    k_poll_signal_init(&signal);
}
```

It is signaled via the [`k_poll_signal_raise()`](#c.k_poll_signal_raise) function. This function
takes a user **result** parameter that is opaque to the API and can be used to
pass extra information to the thread waiting on the event.

```c
struct k_poll_signal signal;

// thread A
void do_stuff(void)
{
    k_poll_signal_init(&signal);

    struct k_poll_event events[1] = {
        K_POLL_EVENT_INITIALIZER(K_POLL_TYPE_SIGNAL,
                                 K_POLL_MODE_NOTIFY_ONLY,
                                 &signal),
    };

    k_poll(events, 1, K_FOREVER);

    if (events.signal->result == 0x1337) {
        // A-OK!
    } else {
        // weird error
    }
}

// thread B
void signal_do_stuff(void)
{
    k_poll_signal_raise(&signal, 0x1337);
}
```

If the signal is to be polled in a loop, *both* its event state and its
**signaled** field *must* be reset on each iteration if it has been signaled.

```c
struct k_poll_signal signal;
void do_stuff(void)
{
    k_poll_signal_init(&signal);

    struct k_poll_event events[1] = {
        K_POLL_EVENT_INITIALIZER(K_POLL_TYPE_SIGNAL,
                                 K_POLL_MODE_NOTIFY_ONLY,
                                 &signal),
    };

    for (;;) {
        k_poll(events, 1, K_FOREVER);

        if (events[0].signal->result == 0x1337) {
            // A-OK!
        } else {
            // weird error
        }

        events[0].signal->signaled = 0;
        events[0].state = K_POLL_STATE_NOT_READY;
    }
}
```

Note that poll signals are not internally synchronized. A [`k_poll()`](#c.k_poll) call
that is passed a signal will return after any code in the system calls
[`k_poll_signal_raise()`](#c.k_poll_signal_raise). But if the signal is being
externally managed and reset via [`k_poll_signal_init()`](#c.k_poll_signal_init), it is
possible that by the time the application checks, the event state may
no longer be equal to [`K_POLL_STATE_SIGNALED`](#c.K_POLL_STATE_SIGNALED), and a (naive)
application will miss events. Best practice is always to reset the
signal only from within the thread invoking the [`k_poll()`](#c.k_poll) loop, or else
to use some other event type which tracks event counts: semaphores and
FIFOs are more error-proof in this sense because they can’t “miss”
events, architecturally.

## [Suggested Uses](#id5)

Use [`k_poll()`](#c.k_poll) to consolidate multiple threads that would be pending
on one object each, saving possibly large amounts of stack space.

Use a poll signal as a lightweight binary semaphore if only one thread pends on
it.

Note

Because objects are only signaled if no other thread is waiting for them to
become available and only one thread can poll on a specific object, polling
is best used when objects are not subject of contention between multiple
threads, basically when a single thread operates as a main “server” or
“dispatcher” for multiple objects and is the only one trying to acquire
these objects.

## [Configuration Options](#id6)

Related configuration options:

- [`CONFIG_POLL`](../../kconfig.md#CONFIG_POLL "CONFIG_POLL")

## [API Reference](#id7)

*group* poll\_apis
:   Defines

    K\_POLL\_TYPE\_IGNORE

    K\_POLL\_TYPE\_SIGNAL

    K\_POLL\_TYPE\_SEM\_AVAILABLE

    K\_POLL\_TYPE\_DATA\_AVAILABLE

    K\_POLL\_TYPE\_FIFO\_DATA\_AVAILABLE

    K\_POLL\_TYPE\_MSGQ\_DATA\_AVAILABLE

    K\_POLL\_TYPE\_PIPE\_DATA\_AVAILABLE

    K\_POLL\_STATE\_NOT\_READY

    K\_POLL\_STATE\_SIGNALED

    K\_POLL\_STATE\_SEM\_AVAILABLE

    K\_POLL\_STATE\_DATA\_AVAILABLE

    K\_POLL\_STATE\_FIFO\_DATA\_AVAILABLE

    K\_POLL\_STATE\_MSGQ\_DATA\_AVAILABLE

    K\_POLL\_STATE\_PIPE\_DATA\_AVAILABLE

    K\_POLL\_STATE\_CANCELLED

    K\_POLL\_SIGNAL\_INITIALIZER(obj)

    K\_POLL\_EVENT\_INITIALIZER(\_event\_type, \_event\_mode, \_event\_obj)

    K\_POLL\_EVENT\_STATIC\_INITIALIZER(\_event\_type, \_event\_mode, \_event\_obj, event\_tag)

    Enums

    enum k\_poll\_modes
    :   *Values:*

        enumerator K\_POLL\_MODE\_NOTIFY\_ONLY = 0

        enumerator K\_POLL\_NUM\_MODES

    Functions

    void k\_poll\_event\_init(struct [k\_poll\_event](#c.k_poll_event) \*event, uint32\_t type, int mode, void \*obj)
    :   Initialize one struct [k\_poll\_event](#structk__poll__event) instance.

        After this routine is called on a poll event, the event it ready to be placed in an event array to be passed to [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db).

        Parameters:
        :   - **event** – The event to initialize.
            - **type** – A bitfield of the types of event, from the K\_POLL\_TYPE\_xxx values. Only values that apply to the same object being polled can be used together. Choosing K\_POLL\_TYPE\_IGNORE disables the event.
            - **mode** – Future. Use K\_POLL\_MODE\_NOTIFY\_ONLY.
            - **obj** – Kernel object or poll signal.

    int k\_poll(struct [k\_poll\_event](#c.k_poll_event) \*events, int num\_events, [k\_timeout\_t](timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Wait for one or many of multiple poll events to occur.

        This routine allows a thread to wait concurrently for one or many of multiple poll events to have occurred. Such events can be a kernel object being available, like a semaphore, or a poll signal event.

        When an event notifies that a kernel object is available, the kernel object is not “given” to the thread calling [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db): it merely signals the fact that the object was available when the [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db) call was in effect. Also, all threads trying to acquire an object the regular way, i.e. by pending on the object, have precedence over the thread polling on the object. This means that the polling thread will never get the poll event on an object until the object becomes available and its pend queue is empty. For this reason, the [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db) call is more effective when the objects being polled only have one thread, the polling thread, trying to acquire them.

        When [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db) returns 0, the caller should loop on all the events that were passed to [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db) and check the state field for the values that were expected and take the associated actions.

        Before being reused for another call to [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db), the user has to reset the state field to K\_POLL\_STATE\_NOT\_READY.

        When called from user mode, a temporary memory allocation is required from the caller’s resource pool.

        Parameters:
        :   - **events** – An array of events to be polled for.
            - **num\_events** – The number of events in the array.
            - **timeout** – Waiting period for an event to be ready, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – One or more events are ready.
            - **-EAGAIN** – Waiting period timed out.
            - **-EINTR** – Polling has been interrupted, e.g. with [k\_queue\_cancel\_wait()](data_passing/queues.md#group__queue__apis_1ga7c39d86cc6509f59ff9223cac3ea5071). All output events are still set and valid, cancelled event(s) will be set to K\_POLL\_STATE\_CANCELLED. In other words, -EINTR status means that at least one of output events is K\_POLL\_STATE\_CANCELLED.
            - **-ENOMEM** – Thread resource pool insufficient memory (user mode only)
            - **-EINVAL** – Bad parameters (user mode only)

    void k\_poll\_signal\_init(struct [k\_poll\_signal](#c.k_poll_signal) \*sig)
    :   Initialize a poll signal object.

        Ready a poll signal object to be signaled via [k\_poll\_signal\_raise()](#group__poll__apis_1gad0bf3825f828ec3ca37481bf3cbd6723).

        Parameters:
        :   - **sig** – A poll signal.

    void k\_poll\_signal\_reset(struct [k\_poll\_signal](#c.k_poll_signal) \*sig)

    void k\_poll\_signal\_check(struct [k\_poll\_signal](#c.k_poll_signal) \*sig, unsigned int \*signaled, int \*result)
    :   Fetch the signaled state and result value of a poll signal.

        Parameters:
        :   - **sig** – A poll signal object
            - **signaled** – An integer buffer which will be written nonzero if the object was signaled
            - **result** – An integer destination buffer which will be written with the result value if the object was signaled, or an undefined value if it was not.

    int k\_poll\_signal\_raise(struct [k\_poll\_signal](#c.k_poll_signal) \*sig, int result)
    :   Signal a poll signal object.

        This routine makes ready a poll signal, which is basically a poll event of type K\_POLL\_TYPE\_SIGNAL. If a thread was polling on that event, it will be made ready to run. A *result* value can be specified.

        The poll signal contains a ‘signaled’ field that, when set by [k\_poll\_signal\_raise()](#group__poll__apis_1gad0bf3825f828ec3ca37481bf3cbd6723), stays set until the user sets it back to 0 with [k\_poll\_signal\_reset()](#group__poll__apis_1ga02d899d1455ae1f3f55ffe8f1ebd6994). It thus has to be reset by the user before being passed again to [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db) or [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db) will consider it being signaled, and will return immediately.

        Note

        The result is stored and the ‘signaled’ field is set even if this function returns an error indicating that an expiring poll was not notified. The next [k\_poll()](#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db) will detect the missed raise.

        Parameters:
        :   - **sig** – A poll signal.
            - **result** – The value to store in the result field of the signal.

        Return values:
        :   - **0** – The signal was delivered successfully.
            - **-EAGAIN** – The polling thread’s timeout is in the process of expiring.

    struct k\_poll\_signal
    :   *#include <kernel.h>*

        Public Members

        [sys\_dlist\_t](../data_structures/dlist.md#c.sys_dlist_t "sys_dlist_t") poll\_events
        :   PRIVATE - DO NOT TOUCH.

        unsigned int signaled
        :   1 if the event has been signaled, 0 otherwise.

            Stays set to 1 until user resets it to 0.

        int result
        :   custom result value passed to [k\_poll\_signal\_raise()](#group__poll__apis_1gad0bf3825f828ec3ca37481bf3cbd6723) if needed

    struct k\_poll\_event
    :   *#include <kernel.h>*

        Poll Event.

        Public Members

        struct z\_poller \*poller
        :   PRIVATE - DO NOT TOUCH.

        uint32\_t tag
        :   optional user-specified tag, opaque, untouched by the API

        uint32\_t type
        :   bitfield of event types (bitwise-ORed K\_POLL\_TYPE\_xxx values)

        uint32\_t state
        :   bitfield of event states (bitwise-ORed K\_POLL\_STATE\_xxx values)

        uint32\_t mode
        :   mode of operation, from enum [k\_poll\_modes](#group__poll__apis_1ga36d7978872a83191dd3cc16d62165add)

        uint32\_t unused
        :   unused bits in 32-bit word

        union [k\_poll\_event](#c.k_poll_event).[anonymous] [anonymous]
        :   per-type data
