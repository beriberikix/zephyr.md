---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/services/synchronization/events.html
original_path: kernel/services/synchronization/events.html
---

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

An event object is defined using a variable of type [`k_event`](../../../doxygen/html/structk__event.md).
It must then be initialized by calling [`k_event_init()`](../../../doxygen/html/group__event__apis.md#gacf803590b39b095056f2b1c5090c4019).

The following code defines an event object.

```c
struct k_event my_event;

k_event_init(&my_event);
```

Alternatively, an event object can be defined and initialized at compile time
by calling [`K_EVENT_DEFINE`](../../../doxygen/html/group__event__apis.md#ga093449cc6686d3235944f3faad284893).

The following code has the same effect as the code segment above.

```c
K_EVENT_DEFINE(my_event);
```

### [Setting Events](#id5)

Events in an event object are set by calling [`k_event_set()`](../../../doxygen/html/group__event__apis.md#gac22e9d768d003246e68b4b0b64e60f49).

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

Events are posted to an event object by calling [`k_event_post()`](../../../doxygen/html/group__event__apis.md#gac88d17410a71642a903890e420d23d76).

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

Threads wait for events by calling [`k_event_wait()`](../../../doxygen/html/group__event__apis.md#ga0f83f5f034e13bab65149fb90b87a753).

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

[Event APIs](../../../doxygen/html/group__event__apis.md)
