---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/services/polling.html
original_path: kernel/services/polling.html
---

# Polling API

The polling API is used to wait concurrently for any one of multiple conditions
to be fulfilled.

## [Concepts](#id1)

The polling API’s main function is [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db), which is very similar
in concept to the POSIX [`poll()`](../../doxygen/html/poll_8h.md#afa7e83ddea0ab5b08fcf614b89ac48ba) function, except that it operates on
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

The [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) function returns as soon as one of the conditions it
is waiting for is fulfilled. It is possible for more than one to be fulfilled
when [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) returns, if they were fulfilled before
[`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) was called, or due to the preemptive multi-threading
nature of the kernel. The caller must look at the state of all the poll events
in the array to figure out which ones were fulfilled and what actions to take.

Currently, there is only one mode of operation available: the object is not
acquired. As an example, this means that when [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) returns and
the poll event states that the semaphore is available, the caller of
[`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) must then invoke [`k_sem_take()`](../../doxygen/html/group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090) to take
ownership of the semaphore. If the semaphore is contested, there is no
guarantee that it will be still available when [`k_sem_take()`](../../doxygen/html/group__semaphore__apis.md#gac71e2383c1920dddc45a561cacfef090) is
called.

## [Implementation](#id2)

### [Using k\_poll()](#id3)

The main API is [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db), which operates on an array of poll events
of type [`k_poll_event`](../../doxygen/html/structk__poll__event.md). Each entry in the array represents one
event a call to [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) will wait for its condition to be
fulfilled.

Poll events can be initialized using either the runtime initializers
[`K_POLL_EVENT_INITIALIZER()`](../../doxygen/html/group__poll__apis.md#ga8e3889f2bac281a6e65e31068e58047e) or [`k_poll_event_init()`](../../doxygen/html/group__poll__apis.md#gaa06bddd93a024fc5326d93187d80eb03), or
the static initializer [`K_POLL_EVENT_STATIC_INITIALIZER()`](../../doxygen/html/group__poll__apis.md#gada2366896d913dc916b3c28642648b63). An object
that matches the **type** specified must be passed to the initializers. The
**mode** *must* be set to [`K_POLL_MODE_NOTIFY_ONLY`](../../doxygen/html/group__poll__apis.md#gga36d7978872a83191dd3cc16d62165adda22874743e2f6b0f1fd55c5375732b681). The state
*must* be set to [`K_POLL_STATE_NOT_READY`](../../doxygen/html/group__poll__apis.md#ga522822c5e06a89b22ce4dcefd10c66aa) (the initializers take care
of this). The user **tag** is optional and completely opaque to the API: it is
there to help a user to group similar events together. Being optional, it is
passed to the static initializer, but not the runtime ones for performance
reasons. If using runtime initializers, the user must set it separately in the
[`k_poll_event`](../../doxygen/html/structk__poll__event.md) data structure. If an event in the array is to be
ignored, most likely temporarily, its type can be set to
[`K_POLL_TYPE_IGNORE`](../../doxygen/html/group__poll__apis.md#gafd5d801eb9e9cf6097b2c08b4933998e).

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
[`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db). A timeout can be specified to wait only for a specified
amount of time, or the special values [`K_NO_WAIT`](../../doxygen/html/group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f) and
[`K_FOREVER`](../../doxygen/html/group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca) to either not wait or wait until an event condition is
satisfied and not sooner.

A list of pollers is offered on each semaphore or FIFO and as many events
can wait in it as the app wants.
Notice that the waiters will be served in first-come-first-serve order,
not in priority order.

In case of success, [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) returns 0. If it times out, it returns
-[`EAGAIN`](../../doxygen/html/group__system__errno.md#gaf0fac1cea1165b4debec7f686edf3313).

```c
// assume there is no contention on this semaphore and FIFO
// -EADDRINUSE will not occur; the semaphore and/or data will be available

void do_stuff(void)
{
    rc = k_poll(events, ARRAY_SIZE(events), K_MSEC(1000));
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

When [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) is called in a loop, the events state must be reset
to [`K_POLL_STATE_NOT_READY`](../../doxygen/html/group__poll__apis.md#ga522822c5e06a89b22ce4dcefd10c66aa) by the user.

```c
void do_stuff(void)
{
    for(;;) {
        rc = k_poll(events, ARRAY_SIZE(events), K_FOREVER);
        if (events[0].state == K_POLL_STATE_SEM_AVAILABLE) {
            k_sem_take(events[0].sem, 0);
        }
        if (events[1].state == K_POLL_STATE_FIFO_DATA_AVAILABLE) {
            data = k_fifo_get(events[1].fifo, 0);
            // handle data
        }
        if (events[2].state == K_POLL_STATE_MSGQ_DATA_AVAILABLE) {
            ret = k_msgq_get(events[2].msgq, buf, K_NO_WAIT);
            // handle data
        }
        if (events[3].state == K_POLL_STATE_PIPE_DATA_AVAILABLE) {
            ret = k_pipe_get(events[3].pipe, buf, bytes_to_read, &bytes_read, min_xfer, K_NO_WAIT);
            // handle data
        }
        events[0].state = K_POLL_STATE_NOT_READY;
        events[1].state = K_POLL_STATE_NOT_READY;
        events[2].state = K_POLL_STATE_NOT_READY;
        events[3].state = K_POLL_STATE_NOT_READY;
    }
}
```

### [Using k\_poll\_signal\_raise()](#id4)

One of the types of events is [`K_POLL_TYPE_SIGNAL`](../../doxygen/html/group__poll__apis.md#ga144d8eb34d85f6053e454410a10bf56a): this is a “direct”
signal to a poll event. This can be seen as a lightweight binary semaphore only
one thread can wait for.

A poll signal is a separate object of type [`k_poll_signal`](../../doxygen/html/structk__poll__signal.md) that
must be attached to a k\_poll\_event, similar to a semaphore or FIFO. It must
first be initialized either via [`K_POLL_SIGNAL_INITIALIZER()`](../../doxygen/html/group__poll__apis.md#ga6d6321e189afca73a276cd671ec531ae) or
[`k_poll_signal_init()`](../../doxygen/html/group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551).

```c
struct k_poll_signal signal;
void do_stuff(void)
{
    k_poll_signal_init(&signal);
}
```

It is signaled via the [`k_poll_signal_raise()`](../../doxygen/html/group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723) function. This function
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

    int signaled, result;

    k_poll_signal_check(&signal, &signaled, &result);

    if (signaled && (result == 0x1337)) {
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

If the signal is to be polled in a loop, *both* its event state must be
reset to [`K_POLL_STATE_NOT_READY`](../../doxygen/html/group__poll__apis.md#ga522822c5e06a89b22ce4dcefd10c66aa) *and* its `result` must be
reset using [`k_poll_signal_reset()`](../../doxygen/html/group__poll__apis.md#ga02d899d1455ae1f3f55ffe8f1ebd6994) on each iteration if it has
been signaled.

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

        int signaled, result;

        k_poll_signal_check(&signal, &signaled, &result);

        if (signaled && (result == 0x1337)) {
            // A-OK!
        } else {
            // weird error
        }

        k_poll_signal_reset(signal);
        events[0].state = K_POLL_STATE_NOT_READY;
    }
}
```

Note that poll signals are not internally synchronized. A [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) call
that is passed a signal will return after any code in the system calls
[`k_poll_signal_raise()`](../../doxygen/html/group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723). But if the signal is being
externally managed and reset via [`k_poll_signal_init()`](../../doxygen/html/group__poll__apis.md#gaee3090c2a912b93b6a5855e3018c3551), it is
possible that by the time the application checks, the event state may
no longer be equal to [`K_POLL_STATE_SIGNALED`](../../doxygen/html/group__poll__apis.md#ga478aae7fe4fb5c7b7c76ed216c22a7f1), and a (naive)
application will miss events. Best practice is always to reset the
signal only from within the thread invoking the [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) loop, or else
to use some other event type which tracks event counts: semaphores and
FIFOs are more error-proof in this sense because they can’t “miss”
events, architecturally.

## [Suggested Uses](#id5)

Use [`k_poll()`](../../doxygen/html/group__poll__apis.md#gac550dc93662ce164fb22a5a91d6830db) to consolidate multiple threads that would be pending
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

[Async polling APIs](../../doxygen/html/group__poll__apis.md)
