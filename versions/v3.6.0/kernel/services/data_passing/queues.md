---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/services/data_passing/queues.html
original_path: kernel/services/data_passing/queues.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Queues

A Queue in Zephyr is a kernel object that implements a traditional queue, allowing
threads and ISRs to add and remove data items of any size. The queue is similar
to a FIFO and serves as the underlying implementation for both [k\_fifo](fifos.md#fifos-v2) and [k\_lifo](lifos.md#lifos-v2). For more information on usage see
[k\_fifo](fifos.md#fifos-v2).

## Configuration Options

Related configuration options:

- None

## API Reference

*group* queue\_apis
:   Defines

    K\_QUEUE\_DEFINE(name)
    :   Statically define and initialize a queue.

        The queue can be accessed outside the module where it is defined using:

        ```text
        extern struct k_queue <name>;
        ```

        Parameters:
        :   - **name** – Name of the queue.

    Functions

    void k\_queue\_init(struct k\_queue \*queue)
    :   Initialize a queue.

        This routine initializes a queue object, prior to its first use.

        Parameters:
        :   - **queue** – Address of the queue.

    void k\_queue\_cancel\_wait(struct k\_queue \*queue)
    :   Cancel waiting on a queue.

        This routine causes first thread pending on *queue*, if any, to return from [k\_queue\_get()](#group__queue__apis_1ga0a77d8556e7d253319275de034f01619) call with NULL value (as if timeout expired). If the queue is being waited on by [k\_poll()](../polling.md#group__poll__apis_1gac550dc93662ce164fb22a5a91d6830db), it will return with -EINTR and K\_POLL\_STATE\_CANCELLED state (and per above, subsequent [k\_queue\_get()](#group__queue__apis_1ga0a77d8556e7d253319275de034f01619) will return NULL).

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.

    void k\_queue\_append(struct k\_queue \*queue, void \*data)
    :   Append an element to the end of a queue.

        This routine appends a data item to *queue*. A queue data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel’s use.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.
            - **data** – Address of the data item.

    int32\_t k\_queue\_alloc\_append(struct k\_queue \*queue, void \*data)
    :   Append an element to a queue.

        This routine appends a data item to *queue*. There is an implicit memory allocation to create an additional temporary bookkeeping data structure from the calling thread’s resource pool, which is automatically freed when the item is removed. The data itself is not copied.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.
            - **data** – Address of the data item.

        Return values:
        :   - **0** – on success
            - **-ENOMEM** – if there isn’t sufficient RAM in the caller’s resource pool

    void k\_queue\_prepend(struct k\_queue \*queue, void \*data)
    :   Prepend an element to a queue.

        This routine prepends a data item to *queue*. A queue data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel’s use.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.
            - **data** – Address of the data item.

    int32\_t k\_queue\_alloc\_prepend(struct k\_queue \*queue, void \*data)
    :   Prepend an element to a queue.

        This routine prepends a data item to *queue*. There is an implicit memory allocation to create an additional temporary bookkeeping data structure from the calling thread’s resource pool, which is automatically freed when the item is removed. The data itself is not copied.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.
            - **data** – Address of the data item.

        Return values:
        :   - **0** – on success
            - **-ENOMEM** – if there isn’t sufficient RAM in the caller’s resource pool

    void k\_queue\_insert(struct k\_queue \*queue, void \*prev, void \*data)
    :   Inserts an element to a queue.

        This routine inserts a data item to *queue* after previous item. A queue data item must be aligned on a word boundary, and the first word of the item is reserved for the kernel’s use.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.
            - **prev** – Address of the previous data item.
            - **data** – Address of the data item.

    int k\_queue\_append\_list(struct k\_queue \*queue, void \*head, void \*tail)
    :   Atomically append a list of elements to a queue.

        This routine adds a list of data items to *queue* in one operation. The data items must be in a singly-linked list, with the first word in each data item pointing to the next data item; the list must be NULL-terminated.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.
            - **head** – Pointer to first node in singly-linked list.
            - **tail** – Pointer to last node in singly-linked list.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – on invalid supplied data

    int k\_queue\_merge\_slist(struct k\_queue \*queue, [sys\_slist\_t](../../data_structures/slist.md#c.sys_slist_t "sys_slist_t") \*list)
    :   Atomically add a list of elements to a queue.

        This routine adds a list of data items to *queue* in one operation. The data items must be in a singly-linked list implemented using a [sys\_slist\_t](../../data_structures/slist.md#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) object. Upon completion, the original list is empty.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.
            - **list** – Pointer to [sys\_slist\_t](../../data_structures/slist.md#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) object.

        Return values:
        :   - **0** – on success
            - **-EINVAL** – on invalid data

    void \*k\_queue\_get(struct k\_queue \*queue, [k\_timeout\_t](../timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Get an element from a queue.

        This routine removes first data item from *queue*. The first word of the data item is reserved for the kernel’s use.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Parameters:
        :   - **queue** – Address of the queue.
            - **timeout** – Non-negative waiting period to obtain a data item or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Returns:
        :   Address of the data item if successful; NULL if returned without waiting, or waiting period timed out.

    bool k\_queue\_remove(struct k\_queue \*queue, void \*data)
    :   Remove an element from a queue.

        This routine removes data item from *queue*. The first word of the data item is reserved for the kernel’s use. Removing elements from k\_queue rely on sys\_slist\_find\_and\_remove which is not a constant time operation.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        *timeout* must be set to K\_NO\_WAIT if called from ISR.

        Parameters:
        :   - **queue** – Address of the queue.
            - **data** – Address of the data item.

        Returns:
        :   true if data item was removed

    bool k\_queue\_unique\_append(struct k\_queue \*queue, void \*data)
    :   Append an element to a queue only if it’s not present already.

        This routine appends data item to *queue*. The first word of the data item is reserved for the kernel’s use. Appending elements to k\_queue relies on sys\_slist\_is\_node\_in\_list which is not a constant time operation.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.
            - **data** – Address of the data item.

        Returns:
        :   true if data item was added, false if not

    int k\_queue\_is\_empty(struct k\_queue \*queue)
    :   Query a queue to see if it has data available.

        Note that the data might be already gone by the time this function returns if other threads are also trying to read from the queue.

        **Function properties (list may not be complete)**
        :   [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **queue** – Address of the queue.

        Returns:
        :   Non-zero if the queue is empty.

        Returns:
        :   0 if data is available.

    void \*k\_queue\_peek\_head(struct k\_queue \*queue)
    :   Peek element at the head of queue.

        Return element from the head of queue without removing it.

        Parameters:
        :   - **queue** – Address of the queue.

        Returns:
        :   Head element, or NULL if queue is empty.

    void \*k\_queue\_peek\_tail(struct k\_queue \*queue)
    :   Peek element at the tail of queue.

        Return element from the tail of queue without removing it.

        Parameters:
        :   - **queue** – Address of the queue.

        Returns:
        :   Tail element, or NULL if queue is empty.
