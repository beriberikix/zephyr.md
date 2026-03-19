---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/services/data_passing/message_queues.html
original_path: kernel/services/data_passing/message_queues.html
---

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
The underlying implementation uses [`memcpy()`](../../../doxygen/html/string_8h.md#af0f01bffcd16daa9143f6014d10a25ad) (which is
alignment-agnostic) and does not expose any internal pointers.

## [Implementation](#id2)

### [Defining a Message Queue](#id3)

A message queue is defined using a variable of type [`k_msgq`](../../../doxygen/html/structk__msgq.md).
It must then be initialized by calling [`k_msgq_init()`](../../../doxygen/html/group__msgq__apis.md#ga54a5cdcaea2236c383ace433fedc0d39).

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
by calling [`K_MSGQ_DEFINE`](../../../doxygen/html/group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b).

The following code has the same effect as the code segment above. Observe
that the macro defines both the message queue and its buffer.

```c
K_MSGQ_DEFINE(my_msgq, sizeof(struct data_item_type), 10, 1);
```

### [Writing to a Message Queue](#id4)

A data item is added to a message queue by calling [`k_msgq_put()`](../../../doxygen/html/group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe).

The following code builds on the example above, and uses the message queue
to pass data items from a producing thread to one or more consuming threads.
If the message queue fills up because the consumers can’t keep up, the
producing thread throws away all existing data so the newer data can be saved.
Note that this api will trigger reschedule.

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

A data item is taken from a message queue by calling [`k_msgq_get()`](../../../doxygen/html/group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7).

The following code builds on the example above, and uses the message queue
to process data items generated by one or more producing threads. Note that
the return value of [`k_msgq_get()`](../../../doxygen/html/group__msgq__apis.md#gae67f2ced2df1f9c290ae15dab9097cb7) should be tested as `-ENOMSG`
can be returned due to [`k_msgq_purge()`](../../../doxygen/html/group__msgq__apis.md#gaa18875887773195ae44b7fe0972ee760).

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

A data item is read from a message queue by calling [`k_msgq_peek()`](../../../doxygen/html/group__msgq__apis.md#ga14f543472f2f63cfde0bdfa87b95c915).

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

[Message Queue APIs](../../../doxygen/html/group__msgq__apis.md)
