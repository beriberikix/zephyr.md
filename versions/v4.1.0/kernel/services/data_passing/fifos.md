---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/services/data_passing/fifos.html
original_path: kernel/services/data_passing/fifos.html
---

# FIFOs

A *FIFO* is a kernel object that implements a traditional
first in, first out (FIFO) queue, allowing threads and ISRs
to add and remove data items of any size.

## [Concepts](#id1)

Any number of FIFOs can be defined (limited only by available RAM). Each FIFO is
referenced by its memory address.

A FIFO has the following key properties:

- A **queue** of data items that have been added but not yet removed.
  The queue is implemented as a simple linked list.

A FIFO must be initialized before it can be used. This sets its queue to empty.

FIFO data items must be aligned on a word boundary, as the kernel reserves
the first word of an item for use as a pointer to the next data item in
the queue. Consequently, a data item that holds N bytes of application
data requires N+4 (or N+8) bytes of memory. There are no alignment or
reserved space requirements for data items if they are added with
[`k_fifo_alloc_put()`](../../../doxygen/html/group__fifo__apis.md#gab1c5212040d12cbb92cede5cf54928ba), instead additional memory is temporarily
allocated from the calling thread’s resource pool.

Note

FIFO data items are restricted to single active instance across all FIFO
data queues. Any attempt to re-add a FIFO data item to a queue before
it has been removed from the queue to which it was previously added will
result in undefined behavior.

A data item may be **added** to a FIFO by a thread or an ISR.
The item is given directly to a waiting thread, if one exists;
otherwise the item is added to the FIFO’s queue.
There is no limit to the number of items that may be queued.

A data item may be **removed** from a FIFO by a thread. If the FIFO’s queue
is empty a thread may choose to wait for a data item to be given.
Any number of threads may wait on an empty FIFO simultaneously.
When a data item is added, it is given to the highest priority thread
that has waited longest.

Note

The kernel does allow an ISR to remove an item from a FIFO, however
the ISR must not attempt to wait if the FIFO is empty.

If desired, **multiple data items** can be added to a FIFO in a single operation
if they are chained together into a singly-linked list. This capability can be
useful if multiple writers are adding sets of related data items to the FIFO,
as it ensures the data items in each set are not interleaved with other data
items. Adding multiple data items to a FIFO is also more efficient than adding
them one at a time, and can be used to guarantee that anyone who removes
the first data item in a set will be able to remove the remaining data items
without waiting.

## [Implementation](#id2)

### [Defining a FIFO](#id3)

A FIFO is defined using a variable of type [`k_fifo`](../../../doxygen/html/structk__fifo.md).
It must then be initialized by calling [`k_fifo_init()`](../../../doxygen/html/group__fifo__apis.md#gaeebf6ef54d4be61e19408f44a734a159).

The following code defines and initializes an empty FIFO.

```c
struct k_fifo my_fifo;

k_fifo_init(&my_fifo);
```

Alternatively, an empty FIFO can be defined and initialized at compile time
by calling [`K_FIFO_DEFINE`](../../../doxygen/html/group__fifo__apis.md#ga230b02a526ecb0ae1598be75cb9a8274).

The following code has the same effect as the code segment above.

```c
K_FIFO_DEFINE(my_fifo);
```

### [Writing to a FIFO](#id4)

A data item is added to a FIFO by calling [`k_fifo_put()`](../../../doxygen/html/group__fifo__apis.md#ga3addb10f86f19e245c23362433d5c913).

The following code builds on the example above, and uses the FIFO
to send data to one or more consumer threads.

```c
struct data_item_t {
    void *fifo_reserved;   /* 1st word reserved for use by FIFO */
    ...
};

struct data_item_t tx_data;

void producer_thread(int unused1, int unused2, int unused3)
{
    while (1) {
        /* create data item to send */
        tx_data = ...

        /* send data to consumers */
        k_fifo_put(&my_fifo, &tx_data);

        ...
    }
}
```

Additionally, a singly-linked list of data items can be added to a FIFO
by calling [`k_fifo_put_list()`](../../../doxygen/html/group__fifo__apis.md#ga1bf5f52290c83e54ba14358cbbb4051b) or [`k_fifo_put_slist()`](../../../doxygen/html/group__fifo__apis.md#ga4cdc286a7a6f0d43acab63a4846815e7).

Finally, a data item can be added to a FIFO with [`k_fifo_alloc_put()`](../../../doxygen/html/group__fifo__apis.md#gab1c5212040d12cbb92cede5cf54928ba).
With this API, there is no need to reserve space for the kernel’s use in
the data item, instead additional memory will be allocated from the calling
thread’s resource pool until the item is read.

### [Reading from a FIFO](#id5)

A data item is removed from a FIFO by calling [`k_fifo_get()`](../../../doxygen/html/group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6).

The following code builds on the example above, and uses the FIFO
to obtain data items from a producer thread,
which are then processed in some manner.

```c
void consumer_thread(int unused1, int unused2, int unused3)
{
    struct data_item_t  *rx_data;

    while (1) {
        rx_data = k_fifo_get(&my_fifo, K_FOREVER);

        /* process FIFO data item */
        ...
    }
}
```

## [Suggested Uses](#id6)

Use a FIFO to asynchronously transfer data items of arbitrary size
in a “first in, first out” manner.

## [Configuration Options](#id7)

Related configuration options:

- None

## [API Reference](#id8)

[FIFO APIs](../../../doxygen/html/group__fifo__apis.md)

Related code samples

- [Dining Philosophers](../../../samples/philosophers/README.md#dining-philosophers "Implement a solution to the Dining Philosophers problem using Zephyr kernel services.")Implement a solution to the Dining Philosophers problem using Zephyr kernel services.
