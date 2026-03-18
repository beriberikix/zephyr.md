---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/data_passing/fifos.html
original_path: kernel/services/data_passing/fifos.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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
[`k_fifo_alloc_put()`](#c.k_fifo_alloc_put), instead additional memory is temporarily
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

A FIFO is defined using a variable of type `k_fifo`.
It must then be initialized by calling [`k_fifo_init()`](#c.k_fifo_init).

The following code defines and initializes an empty FIFO.

```c
struct k_fifo my_fifo;

k_fifo_init(&my_fifo);
```

Alternatively, an empty FIFO can be defined and initialized at compile time
by calling [`K_FIFO_DEFINE`](#c.K_FIFO_DEFINE).

The following code has the same effect as the code segment above.

```c
K_FIFO_DEFINE(my_fifo);
```

### [Writing to a FIFO](#id4)

A data item is added to a FIFO by calling [`k_fifo_put()`](#c.k_fifo_put).

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
by calling [`k_fifo_put_list()`](#c.k_fifo_put_list) or [`k_fifo_put_slist()`](#c.k_fifo_put_slist).

Finally, a data item can be added to a FIFO with [`k_fifo_alloc_put()`](#c.k_fifo_alloc_put).
With this API, there is no need to reserve space for the kernel’s use in
the data item, instead additional memory will be allocated from the calling
thread’s resource pool until the item is read.

### [Reading from a FIFO](#id5)

A data item is removed from a FIFO by calling [`k_fifo_get()`](#c.k_fifo_get).

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

*group* fifo\_apis
:   Defines

    k\_fifo\_init(fifo)
    :   Initialize a FIFO queue.

        This routine initializes a FIFO queue, prior to its first use.

        Parameters:
        :   - **fifo** – Address of the FIFO queue.

    k\_fifo\_cancel\_wait(fifo)
    :   Cancel waiting on a FIFO queue.

        This routine causes first thread pending on *fifo*, if any, to return from [k\_fifo\_get()](#group__fifo__apis_1ga1e2c480e2124116af97e94e7b4435de6) call with NULL value (as if timeout expired).

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **fifo** – Address of the FIFO queue.

    k\_fifo\_put(fifo, data)
    :   Add an element to a FIFO queue.

        This routine adds a data item to *fifo*. A FIFO data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel’s use.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **fifo** – Address of the FIFO.
            - **data** – Address of the data item.

    k\_fifo\_alloc\_put(fifo, data)
    :   Add an element to a FIFO queue.

        This routine adds a data item to *fifo*. There is an implicit memory allocation to create an additional temporary bookkeeping data structure from the calling thread’s resource pool, which is automatically freed when the item is removed. The data itself is not copied.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **fifo** – Address of the FIFO.
            - **data** – Address of the data item.

        Return values:
        :   - **0** – on success
            - **-ENOMEM** – if there isn’t sufficient RAM in the caller’s resource pool

    k\_fifo\_put\_list(fifo, head, tail)
    :   Atomically add a list of elements to a FIFO.

        This routine adds a list of data items to *fifo* in one operation. The data items must be in a singly-linked list, with the first word of each data item pointing to the next data item; the list must be NULL-terminated.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **fifo** – Address of the FIFO queue.
            - **head** – Pointer to first node in singly-linked list.
            - **tail** – Pointer to last node in singly-linked list.

    k\_fifo\_put\_slist(fifo, list)
    :   Atomically add a list of elements to a FIFO queue.

        This routine adds a list of data items to *fifo* in one operation. The data items must be in a singly-linked list implemented using a [sys\_slist\_t](../../data_structures/slist.md#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) object. Upon completion, the [sys\_slist\_t](../../data_structures/slist.md#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) object is invalid and must be re-initialized via [sys\_slist\_init()](../../data_structures/slist.md#group__single-linked-list__apis_1ga913aea7661b4ab3b4b50a8efc0d70428).

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **fifo** – Address of the FIFO queue.
            - **list** – Pointer to [sys\_slist\_t](../../data_structures/slist.md#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) object.

    k\_fifo\_get(fifo, timeout)
    :   Get an element from a FIFO queue.

        This routine removes a data item from *fifo* in a “first in, first out” manner. The first word of the data item is reserved for the kernel’s use.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Parameters:
        :   - **fifo** – Address of the FIFO queue.
            - **timeout** – Waiting period to obtain a data item, or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Returns:
        :   Address of the data item if successful; NULL if returned without waiting, or waiting period timed out.

    k\_fifo\_is\_empty(fifo)
    :   Query a FIFO queue to see if it has data available.

        Note that the data might be already gone by the time this function returns if other threads is also trying to read from the FIFO.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **fifo** – Address of the FIFO queue.

        Returns:
        :   Non-zero if the FIFO queue is empty.

        Returns:
        :   0 if data is available.

    k\_fifo\_peek\_head(fifo)
    :   Peek element at the head of a FIFO queue.

        Return element from the head of FIFO queue without removing it. A usecase for this is if elements of the FIFO object are themselves containers. Then on each iteration of processing, a head container will be peeked, and some data processed out of it, and only if the container is empty, it will be completely remove from the FIFO queue.

        Parameters:
        :   - **fifo** – Address of the FIFO queue.

        Returns:
        :   Head element, or NULL if the FIFO queue is empty.

    k\_fifo\_peek\_tail(fifo)
    :   Peek element at the tail of FIFO queue.

        Return element from the tail of FIFO queue (without removing it). A usecase for this is if elements of the FIFO queue are themselves containers. Then it may be useful to add more data to the last container in a FIFO queue.

        Parameters:
        :   - **fifo** – Address of the FIFO queue.

        Returns:
        :   Tail element, or NULL if a FIFO queue is empty.

    K\_FIFO\_DEFINE(name)
    :   Statically define and initialize a FIFO queue.

        The FIFO queue can be accessed outside the module where it is defined using:

        ```text
        extern struct k_fifo <name>;
        ```

        Parameters:
        :   - **name** – Name of the FIFO queue.
