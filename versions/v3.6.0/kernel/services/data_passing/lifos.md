---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/data_passing/lifos.html
original_path: kernel/services/data_passing/lifos.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LIFOs

A *LIFO* is a kernel object that implements a traditional
last in, first out (LIFO) queue, allowing threads and ISRs
to add and remove data items of any size.

## [Concepts](#id1)

Any number of LIFOs can be defined (limited only by available RAM). Each LIFO is
referenced by its memory address.

A LIFO has the following key properties:

- A **queue** of data items that have been added but not yet removed.
  The queue is implemented as a simple linked list.

A LIFO must be initialized before it can be used. This sets its queue to empty.

LIFO data items must be aligned on a word boundary, as the kernel reserves
the first word of an item for use as a pointer to the next data item in the
queue. Consequently, a data item that holds N bytes of application data
requires N+4 (or N+8) bytes of memory. There are no alignment or reserved
space requirements for data items if they are added with
[`k_lifo_alloc_put()`](#c.k_lifo_alloc_put), instead additional memory is temporarily
allocated from the calling thread’s resource pool.

Note

LIFO data items are restricted to single active instance across all LIFO
data queues. Any attempt to re-add a LIFO data item to a queue before
it has been removed from the queue to which it was previously added will
result in undefined behavior.

A data item may be **added** to a LIFO by a thread or an ISR.
The item is given directly to a waiting thread, if one exists;
otherwise the item is added to the LIFO’s queue.
There is no limit to the number of items that may be queued.

A data item may be **removed** from a LIFO by a thread. If the LIFO’s queue
is empty a thread may choose to wait for a data item to be given.
Any number of threads may wait on an empty LIFO simultaneously.
When a data item is added, it is given to the highest priority thread
that has waited longest.

Note

The kernel does allow an ISR to remove an item from a LIFO, however
the ISR must not attempt to wait if the LIFO is empty.

## [Implementation](#id2)

### [Defining a LIFO](#id3)

A LIFO is defined using a variable of type `k_lifo`.
It must then be initialized by calling [`k_lifo_init()`](#c.k_lifo_init).

The following defines and initializes an empty LIFO.

```c
struct k_lifo my_lifo;

k_lifo_init(&my_lifo);
```

Alternatively, an empty LIFO can be defined and initialized at compile time
by calling [`K_LIFO_DEFINE`](#c.K_LIFO_DEFINE).

The following code has the same effect as the code segment above.

```c
K_LIFO_DEFINE(my_lifo);
```

### [Writing to a LIFO](#id4)

A data item is added to a LIFO by calling [`k_lifo_put()`](#c.k_lifo_put).

The following code builds on the example above, and uses the LIFO
to send data to one or more consumer threads.

```c
struct data_item_t {
    void *LIFO_reserved;   /* 1st word reserved for use by LIFO */
    ...
};

struct data_item_t tx data;

void producer_thread(int unused1, int unused2, int unused3)
{
    while (1) {
        /* create data item to send */
        tx_data = ...

        /* send data to consumers */
        k_lifo_put(&my_lifo, &tx_data);

        ...
    }
}
```

A data item can be added to a LIFO with [`k_lifo_alloc_put()`](#c.k_lifo_alloc_put).
With this API, there is no need to reserve space for the kernel’s use in
the data item, instead additional memory will be allocated from the calling
thread’s resource pool until the item is read.

### [Reading from a LIFO](#id5)

A data item is removed from a LIFO by calling [`k_lifo_get()`](#c.k_lifo_get).

The following code builds on the example above, and uses the LIFO
to obtain data items from a producer thread,
which are then processed in some manner.

```c
void consumer_thread(int unused1, int unused2, int unused3)
{
    struct data_item_t  *rx_data;

    while (1) {
        rx_data = k_lifo_get(&my_lifo, K_FOREVER);

        /* process LIFO data item */
        ...
    }
}
```

## [Suggested Uses](#id6)

Use a LIFO to asynchronously transfer data items of arbitrary size
in a “last in, first out” manner.

## [Configuration Options](#id7)

Related configuration options:

- None.

## [API Reference](#id8)

*group* lifo\_apis
:   Defines

    k\_lifo\_init(lifo)
    :   Initialize a LIFO queue.

        This routine initializes a LIFO queue object, prior to its first use.

        Parameters:
        :   - **lifo** – Address of the LIFO queue.

    k\_lifo\_put(lifo, data)
    :   Add an element to a LIFO queue.

        This routine adds a data item to *lifo*. A LIFO queue data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel’s use.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **lifo** – Address of the LIFO queue.
            - **data** – Address of the data item.

    k\_lifo\_alloc\_put(lifo, data)
    :   Add an element to a LIFO queue.

        This routine adds a data item to *lifo*. There is an implicit memory allocation to create an additional temporary bookkeeping data structure from the calling thread’s resource pool, which is automatically freed when the item is removed. The data itself is not copied.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **lifo** – Address of the LIFO.
            - **data** – Address of the data item.

        Return values:
        :   - **0** – on success
            - **-ENOMEM** – if there isn’t sufficient RAM in the caller’s resource pool

    k\_lifo\_get(lifo, timeout)
    :   Get an element from a LIFO queue.

        This routine removes a data item from *LIFO* in a “last in, first out” manner. The first word of the data item is reserved for the kernel’s use.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Parameters:
        :   - **lifo** – Address of the LIFO queue.
            - **timeout** – Waiting period to obtain a data item, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Returns:
        :   Address of the data item if successful; NULL if returned without waiting, or waiting period timed out.

    K\_LIFO\_DEFINE(name)
    :   Statically define and initialize a LIFO queue.

        The LIFO queue can be accessed outside the module where it is defined using:

        ```text
        extern struct k_lifo <name>;
        ```

        Parameters:
        :   - **name** – Name of the fifo.
