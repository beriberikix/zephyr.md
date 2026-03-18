---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/data_passing/message_queues.html
original_path: kernel/services/data_passing/message_queues.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Message Queues

A *message queue* is a kernel object that implements a simple
message queue, allowing threads and ISRs to asynchronously send and receive
fixed-size data items.

## [Concepts](#id1)

Any number of message queues can be defined (limited only by available RAM).
Each message queue is referenced by its memory address.

A message queue has the following key properties:

- A **ring buffer** of data items that have been sent but not yet received.
- A **data item size**, measured in bytes.
- A **maximum quantity** of data items that can be queued in the ring buffer.

A message queue must be initialized before it can be used.
This sets its ring buffer to empty.

A data item can be **sent** to a message queue by a thread or an ISR.
The data item pointed at by the sending thread is copied to a waiting thread,
if one exists; otherwise the item is copied to the message queue’s ring buffer,
if space is available. In either case, the size of the data area being sent
*must* equal the message queue’s data item size.

If a thread attempts to send a data item when the ring buffer is full,
the sending thread may choose to wait for space to become available.
Any number of sending threads may wait simultaneously when the ring buffer
is full; when space becomes available
it is given to the highest priority sending thread that has waited the longest.

A data item can be **received** from a message queue by a thread.
The data item is copied to the area specified by the receiving thread;
the size of the receiving area *must* equal the message queue’s data item size.

If a thread attempts to receive a data item when the ring buffer is empty,
the receiving thread may choose to wait for a data item to be sent.
Any number of receiving threads may wait simultaneously when the ring buffer
is empty; when a data item becomes available it is given to
the highest priority receiving thread that has waited the longest.

A thread can also **peek** at the message on the head of a message queue without
removing it from the queue.
The data item is copied to the area specified by the receiving thread;
the size of the receiving area *must* equal the message queue’s data item size.

Note

The kernel does allow an ISR to receive an item from a message queue,
however the ISR must not attempt to wait if the message queue is empty.

Note

Alignment of the message queue’s ring buffer is not necessary.
The underlying implementation uses `memcpy()` (which is
alignment-agnostic) and does not expose any internal pointers.

## [Implementation](#id2)

### [Defining a Message Queue](#id3)

A message queue is defined using a variable of type [`k_msgq`](#c.k_msgq).
It must then be initialized by calling [`k_msgq_init()`](#c.k_msgq_init).

The following code defines and initializes an empty message queue
that is capable of holding 10 items, each of which is 12 bytes long.

```c
struct data_item_type {
    uint32_t field1;
    uint32_t field2;
    uint32_t field3;
};

char my_msgq_buffer[10 * sizeof(struct data_item_type)];
struct k_msgq my_msgq;

k_msgq_init(&my_msgq, my_msgq_buffer, sizeof(struct data_item_type), 10);
```

Alternatively, a message queue can be defined and initialized at compile time
by calling [`K_MSGQ_DEFINE`](#c.K_MSGQ_DEFINE).

The following code has the same effect as the code segment above. Observe
that the macro defines both the message queue and its buffer.

```c
K_MSGQ_DEFINE(my_msgq, sizeof(struct data_item_type), 10, 1);
```

### [Writing to a Message Queue](#id4)

A data item is added to a message queue by calling [`k_msgq_put()`](#c.k_msgq_put).

The following code builds on the example above, and uses the message queue
to pass data items from a producing thread to one or more consuming threads.
If the message queue fills up because the consumers can’t keep up, the
producing thread throws away all existing data so the newer data can be saved.

```c
void producer_thread(void)
{
    struct data_item_type data;

    while (1) {
        /* create data item to send (e.g. measurement, timestamp, ...) */
        data = ...

        /* send data to consumers */
        while (k_msgq_put(&my_msgq, &data, K_NO_WAIT) != 0) {
            /* message queue is full: purge old data & try again */
            k_msgq_purge(&my_msgq);
        }

        /* data item was successfully added to message queue */
    }
}
```

### [Reading from a Message Queue](#id5)

A data item is taken from a message queue by calling [`k_msgq_get()`](#c.k_msgq_get).

The following code builds on the example above, and uses the message queue
to process data items generated by one or more producing threads. Note that
the return value of [`k_msgq_get()`](#c.k_msgq_get) should be tested as `-ENOMSG`
can be returned due to [`k_msgq_purge()`](#c.k_msgq_purge).

```c
void consumer_thread(void)
{
    struct data_item_type data;

    while (1) {
        /* get a data item */
        k_msgq_get(&my_msgq, &data, K_FOREVER);

        /* process data item */
        ...
    }
}
```

### [Peeking into a Message Queue](#id6)

A data item is read from a message queue by calling [`k_msgq_peek()`](#c.k_msgq_peek).

The following code peeks into the message queue to read the data item at the
head of the queue that is generated by one or more producing threads.

```c
void consumer_thread(void)
{
    struct data_item_type data;

    while (1) {
        /* read a data item by peeking into the queue */
        k_msgq_peek(&my_msgq, &data);

        /* process data item */
        ...
    }
}
```

## [Suggested Uses](#id7)

Use a message queue to transfer small data items between threads
in an asynchronous manner.

Note

A message queue can be used to transfer large data items, if desired.
However, this can increase interrupt latency as interrupts are locked
while a data item is written or read. The time to write or read a data item
increases linearly with its size since the item is copied in its entirety
to or from the buffer in memory. For this reason, it is usually preferable
to transfer large data items by exchanging a pointer to the data item,
rather than the data item itself.

A synchronous transfer can be achieved by using the kernel’s mailbox
object type.

## [Configuration Options](#id8)

Related configuration options:

- None.

## [API Reference](#id9)

*group* msgq\_apis
:   Defines

    K\_MSGQ\_FLAG\_ALLOC

    K\_MSGQ\_DEFINE(q\_name, q\_msg\_size, q\_max\_msgs, q\_align)
    :   Statically define and initialize a message queue.

        The message queue’s ring buffer contains space for *q\_max\_msgs* messages, each of which is *q\_msg\_size* bytes long. Alignment of the message queue’s ring buffer is not necessary, setting *q\_align* to 1 is sufficient.

        The message queue can be accessed outside the module where it is defined using:

        ```text
        extern struct k_msgq <name>;
        ```

        Parameters:
        :   - **q\_name** – Name of the message queue.
            - **q\_msg\_size** – Message size (in bytes).
            - **q\_max\_msgs** – Maximum number of messages that can be queued.
            - **q\_align** – Alignment of the message queue’s ring buffer (power of 2).

    Functions

    void k\_msgq\_init(struct [k\_msgq](#c.k_msgq) \*msgq, char \*buffer, size\_t msg\_size, uint32\_t max\_msgs)
    :   Initialize a message queue.

        This routine initializes a message queue object, prior to its first use.

        The message queue’s ring buffer must contain space for *max\_msgs* messages, each of which is *msg\_size* bytes long. Alignment of the message queue’s ring buffer is not necessary.

        Parameters:
        :   - **msgq** – Address of the message queue.
            - **buffer** – Pointer to ring buffer that holds queued messages.
            - **msg\_size** – Message size (in bytes).
            - **max\_msgs** – Maximum number of messages that can be queued.

    int k\_msgq\_alloc\_init(struct [k\_msgq](#c.k_msgq) \*msgq, size\_t msg\_size, uint32\_t max\_msgs)
    :   Initialize a message queue.

        This routine initializes a message queue object, prior to its first use, allocating its internal ring buffer from the calling thread’s resource pool.

        Memory allocated for the ring buffer can be released by calling [k\_msgq\_cleanup()](#group__msgq__apis_1gafda4399aa9b8f1e44bdf752e00ea787b), or if userspace is enabled and the msgq object loses all of its references.

        Parameters:
        :   - **msgq** – Address of the message queue.
            - **msg\_size** – Message size (in bytes).
            - **max\_msgs** – Maximum number of messages that can be queued.

        Returns:
        :   0 on success, -ENOMEM if there was insufficient memory in the thread’s resource pool, or -EINVAL if the size parameters cause an integer overflow.

    int k\_msgq\_cleanup(struct [k\_msgq](#c.k_msgq) \*msgq)
    :   Release allocated buffer for a queue.

        Releases memory allocated for the ring buffer.

        Parameters:
        :   - **msgq** – message queue to cleanup

        Return values:
        :   - **0** – on success
            - **-EBUSY** – Queue not empty

    int k\_msgq\_put(struct [k\_msgq](#c.k_msgq) \*msgq, const void \*data, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Send a message to a message queue.

        This routine sends a message to message queue *q*.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        The message content is copied from *data* into *msgq* and the *data* pointer is not retained, so the message content will not be modified by this function.

        Parameters:
        :   - **msgq** – Address of the message queue.
            - **data** – Pointer to the message.
            - **timeout** – Non-negative waiting period to add the message, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – Message sent.
            - **-ENOMSG** – Returned without waiting or queue purged.
            - **-EAGAIN** – Waiting period timed out.

    int k\_msgq\_get(struct [k\_msgq](#c.k_msgq) \*msgq, void \*data, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Receive a message from a message queue.

        This routine receives a message from message queue *q*

        in a “first in,

        first out” manner.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Parameters:
        :   - **msgq** – Address of the message queue.
            - **data** – Address of area to hold the received message.
            - **timeout** – Waiting period to receive the message, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Return values:
        :   - **0** – Message received.
            - **-ENOMSG** – Returned without waiting.
            - **-EAGAIN** – Waiting period timed out.

    int k\_msgq\_peek(struct [k\_msgq](#c.k_msgq) \*msgq, void \*data)
    :   Peek/read a message from a message queue.

        This routine reads a message from message queue *q*

        in a “first in,

        first out” manner and leaves the message in the queue.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **msgq** – Address of the message queue.
            - **data** – Address of area to hold the message read from the queue.

        Return values:
        :   - **0** – Message read.
            - **-ENOMSG** – Returned when the queue has no message.

    int k\_msgq\_peek\_at(struct [k\_msgq](#c.k_msgq) \*msgq, void \*data, uint32\_t idx)
    :   Peek/read a message from a message queue at the specified index.

        This routine reads a message from message queue at the specified index and leaves the message in the queue. k\_msgq\_peek\_at(msgq, data, 0) is equivalent to k\_msgq\_peek(msgq, data)

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **msgq** – Address of the message queue.
            - **data** – Address of area to hold the message read from the queue.
            - **idx** – Message queue index at which to peek

        Return values:
        :   - **0** – Message read.
            - **-ENOMSG** – Returned when the queue has no message at index.

    void k\_msgq\_purge(struct [k\_msgq](#c.k_msgq) \*msgq)
    :   Purge a message queue.

        This routine discards all unreceived messages in a message queue’s ring buffer. Any threads that are blocked waiting to send a message to the message queue are unblocked and see an -ENOMSG error code.

        Parameters:
        :   - **msgq** – Address of the message queue.

    uint32\_t k\_msgq\_num\_free\_get(struct [k\_msgq](#c.k_msgq) \*msgq)
    :   Get the amount of free space in a message queue.

        This routine returns the number of unused entries in a message queue’s ring buffer.

        Parameters:
        :   - **msgq** – Address of the message queue.

        Returns:
        :   Number of unused ring buffer entries.

    void k\_msgq\_get\_attrs(struct [k\_msgq](#c.k_msgq) \*msgq, struct [k\_msgq\_attrs](#c.k_msgq_attrs) \*attrs)
    :   Get basic attributes of a message queue.

        This routine fetches basic attributes of message queue into attr argument.

        Parameters:
        :   - **msgq** – Address of the message queue.
            - **attrs** – pointer to message queue attribute structure.

    uint32\_t k\_msgq\_num\_used\_get(struct [k\_msgq](#c.k_msgq) \*msgq)
    :   Get the number of messages in a message queue.

        This routine returns the number of messages in a message queue’s ring buffer.

        Parameters:
        :   - **msgq** – Address of the message queue.

        Returns:
        :   Number of messages.

    struct k\_msgq
    :   *#include <kernel.h>*

        Message Queue Structure.

        Public Members

        \_wait\_q\_t wait\_q
        :   Message queue wait queue.

        struct [k\_spinlock](../smp/smp.md#c.k_spinlock "k_spinlock") lock
        :   Lock.

        size\_t msg\_size
        :   Message size.

        uint32\_t max\_msgs
        :   Maximal number of messages.

        char \*buffer\_start
        :   Start of message buffer.

        char \*buffer\_end
        :   End of message buffer.

        char \*read\_ptr
        :   Read pointer.

        char \*write\_ptr
        :   Write pointer.

        uint32\_t used\_msgs
        :   Number of used messages.

        uint8\_t flags
        :   Message queue.

    struct k\_msgq\_attrs
    :   *#include <kernel.h>*

        Message Queue Attributes.

        Public Members

        size\_t msg\_size
        :   Message Size.

        uint32\_t max\_msgs
        :   Maximal number of messages.

        uint32\_t used\_msgs
        :   Used messages.
