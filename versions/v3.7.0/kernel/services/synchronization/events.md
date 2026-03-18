---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/services/synchronization/events.html
original_path: kernel/services/synchronization/events.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Events

An *event object* is a kernel object that implements traditional events.

## [Concepts](#id2)

Any number of event objects can be defined (limited only by available RAM). Each
event object is referenced by its memory address. One or more threads may wait
on an event object until the desired set of events has been delivered to the
event object. When new events are delivered to the event object, all threads
whose wait conditions have been satisfied become ready simultaneously.

An event object has the following key properties:

- A 32-bit value that tracks which events have been delivered to it.

An event object must be initialized before it can be used.

Events may be **delivered** by a thread or an ISR. When delivering events, the
events may either overwrite the existing set of events or add to them in
a bitwise fashion. When overwriting the existing set of events, this is referred
to as setting. When adding to them in a bitwise fashion, this is referred to as
posting. Both posting and setting events have the potential to fulfill match
conditions of multiple threads waiting on the event object. All threads whose
match conditions have been met are made active at the same time.

Threads may wait on one or more events. They may either wait for all of the
requested events, or for any of them. Furthermore, threads making a wait request
have the option of resetting the current set of events tracked by the event
object prior to waiting. Care must be taken with this option when multiple
threads wait on the same event object.

Note

The kernel does allow an ISR to query an event object, however the ISR must
not attempt to wait for the events.

## [Implementation](#id3)

### [Defining an Event Object](#id4)

An event object is defined using a variable of type [`k_event`](#c.k_event).
It must then be initialized by calling [`k_event_init()`](#c.k_event_init).

The following code defines an event object.

```c
struct k_event my_event;

k_event_init(&my_event);
```

Alternatively, an event object can be defined and initialized at compile time
by calling [`K_EVENT_DEFINE`](#c.K_EVENT_DEFINE).

The following code has the same effect as the code segment above.

```c
K_EVENT_DEFINE(my_event);
```

### [Setting Events](#id5)

Events in an event object are set by calling [`k_event_set()`](#c.k_event_set).

The following code builds on the example above, and sets the events tracked by
the event object to 0x001.

```c
void input_available_interrupt_handler(void *arg)
{
    /* notify threads that data is available */

    k_event_set(&my_event, 0x001);

    ...
}
```

### [Posting Events](#id6)

Events are posted to an event object by calling [`k_event_post()`](#c.k_event_post).

The following code builds on the example above, and posts a set of events to
the event object.

```c
void input_available_interrupt_handler(void *arg)
{
    ...

    /* notify threads that more data is available */

    k_event_post(&my_event, 0x120);

    ...
}
```

### [Waiting for Events](#id7)

Threads wait for events by calling [`k_event_wait()`](#c.k_event_wait).

The following code builds on the example above, and waits up to 50 milliseconds
for any of the specified events to be posted. A warning is issued if none
of the events are posted in time.

```c
void consumer_thread(void)
{
    uint32_t  events;

    events = k_event_wait(&my_event, 0xFFF, false, K_MSEC(50));
    if (events == 0) {
        printk("No input devices are available!");
    } else {
        /* Access the desired input device(s) */
        ...
    }
    ...
}
```

Alternatively, the consumer thread may desire to wait for all the events
before continuing.

```c
void consumer_thread(void)
{
    uint32_t  events;

    events = k_event_wait_all(&my_event, 0x121, false, K_MSEC(50));
    if (events == 0) {
        printk("At least one input device is not available!");
    } else {
        /* Access the desired input devices */
        ...
    }
    ...
}
```

## [Suggested Uses](#id8)

Use events to indicate that a set of conditions have occurred.

Use events to pass small amounts of data to multiple threads at once.

## [Configuration Options](#id9)

Related configuration options:

- [`CONFIG_EVENTS`](../../../kconfig.md#CONFIG_EVENTS "CONFIG_EVENTS")

## [API Reference](#id10)

*group* Event APIs
:   Defines

    K\_EVENT\_DEFINE(name)
    :   Statically define and initialize an event object.

        The event can be accessed outside the module where it is defined using:

        ```text
        extern struct k_event <name>;
        ```

        Parameters:
        :   - **name** – Name of the event object.

    Functions

    void k\_event\_init(struct [k\_event](#c.k_event) \*event)
    :   Initialize an event object.

        This routine initializes an event object, prior to its first use.

        Parameters:
        :   - **event** – Address of the event object.

    uint32\_t k\_event\_post(struct [k\_event](#c.k_event) \*event, uint32\_t events)
    :   Post one or more events to an event object.

        This routine posts one or more events to an event object. All tasks waiting on the event object *event* whose waiting conditions become met by this posting immediately unpend.

        Posting differs from setting in that posted events are merged together with the current set of events tracked by the event object.

        Parameters:
        :   - **event** – Address of the event object
            - **events** – Set of events to post to *event*

        Return values:
        :   **Previous** – value of the events in *event*

    uint32\_t k\_event\_set(struct [k\_event](#c.k_event) \*event, uint32\_t events)
    :   Set the events in an event object.

        This routine sets the events stored in event object to the specified value. All tasks waiting on the event object *event* whose waiting conditions become met by this immediately unpend.

        Setting differs from posting in that set events replace the current set of events tracked by the event object.

        Parameters:
        :   - **event** – Address of the event object
            - **events** – Set of events to set in *event*

        Return values:
        :   **Previous** – value of the events in *event*

    uint32\_t k\_event\_set\_masked(struct [k\_event](#c.k_event) \*event, uint32\_t events, uint32\_t events\_mask)
    :   Set or clear the events in an event object.

        This routine sets the events stored in event object to the specified value. All tasks waiting on the event object *event* whose waiting conditions become met by this immediately unpend. Unlike [k\_event\_set](#group__event__apis_1gac22e9d768d003246e68b4b0b64e60f49), this routine allows specific event bits to be set and cleared as determined by the mask.

        Parameters:
        :   - **event** – Address of the event object
            - **events** – Set of events to set/clear in *event*
            - **events\_mask** – Mask to be applied to *events*

        Return values:
        :   **Previous** – value of the events in *events\_mask*

    uint32\_t k\_event\_clear(struct [k\_event](#c.k_event) \*event, uint32\_t events)
    :   Clear the events in an event object.

        This routine clears (resets) the specified events stored in an event object.

        Parameters:
        :   - **event** – Address of the event object
            - **events** – Set of events to clear in *event*

        Return values:
        :   **Previous** – value of the events in *event*

    uint32\_t k\_event\_wait(struct [k\_event](#c.k_event) \*event, uint32\_t events, bool reset, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Wait for any of the specified events.

        This routine waits on event object *event* until any of the specified events have been delivered to the event object, or the maximum wait time *timeout* has expired. A thread may wait on up to 32 distinctly numbered events that are expressed as bits in a single 32-bit word.

        Note

        The caller must be careful when resetting if there are multiple threads waiting for the event object *event*.

        Parameters:
        :   - **event** – Address of the event object
            - **events** – Set of desired events on which to wait
            - **reset** – If true, clear the set of events tracked by the event object before waiting. If false, do not clear the events.
            - **timeout** – Waiting period for the desired set of events or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **set** – of matching events upon success
            - **0** – if matching events were not received within the specified time

    uint32\_t k\_event\_wait\_all(struct [k\_event](#c.k_event) \*event, uint32\_t events, bool reset, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Wait for all of the specified events.

        This routine waits on event object *event* until all of the specified events have been delivered to the event object, or the maximum wait time *timeout* has expired. A thread may wait on up to 32 distinctly numbered events that are expressed as bits in a single 32-bit word.

        Note

        The caller must be careful when resetting if there are multiple threads waiting for the event object *event*.

        Parameters:
        :   - **event** – Address of the event object
            - **events** – Set of desired events on which to wait
            - **reset** – If true, clear the set of events tracked by the event object before waiting. If false, do not clear the events.
            - **timeout** – Waiting period for the desired set of events or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **set** – of matching events upon success
            - **0** – if matching events were not received within the specified time

    static inline uint32\_t k\_event\_test(struct [k\_event](#c.k_event) \*event, uint32\_t events\_mask)
    :   Test the events currently tracked in the event object.

        Parameters:
        :   - **event** – Address of the event object
            - **events\_mask** – Set of desired events to test

        Return values:
        :   **Current** – value of events in *events\_mask*

    struct k\_event
    :   *#include <kernel.h>*

        Event Structure.
