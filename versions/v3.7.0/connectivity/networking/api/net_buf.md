---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/net_buf.html
original_path: connectivity/networking/api/net_buf.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Network Buffer

## [Overview](#id1)

Network buffers are a core concept of how the networking stack
(as well as the Bluetooth stack) pass data around. The API for them is
defined in [include/zephyr/net/buf.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/buf.h):.

## [Creating buffers](#id2)

Network buffers are created by first defining a pool of them:

```c
NET_BUF_POOL_DEFINE(pool_name, buf_count, buf_size, user_data_size, NULL);
```

The pool is a static variable, so if it’s needed to be exported to
another module a separate pointer is needed.

Once the pool has been defined, buffers can be allocated from it with:

```c
buf = net_buf_alloc(&pool_name, timeout);
```

There is no explicit initialization function for the pool or its
buffers, rather this is done implicitly as [`net_buf_alloc()`](#c.net_buf_alloc) gets
called.

If there is a need to reserve space in the buffer for protocol headers
to be prepended later, it’s possible to reserve this headroom with:

```c
net_buf_reserve(buf, headroom);
```

In addition to actual protocol data and generic parsing context, network
buffers may also contain protocol-specific context, known as user data.
Both the maximum data and user data capacity of the buffers is
compile-time defined when declaring the buffer pool.

The buffers have native support for being passed through k\_fifo kernel
objects. This is a very practical feature when the buffers need to be
passed from one thread to another. However, since a net\_buf may have a
fragment chain attached to it, instead of using the [`k_fifo_put()`](../../../kernel/services/data_passing/fifos.md#c.k_fifo_put "k_fifo_put")
and [`k_fifo_get()`](../../../kernel/services/data_passing/fifos.md#c.k_fifo_get "k_fifo_get") APIs, special [`net_buf_put()`](#c.net_buf_put) and
[`net_buf_get()`](#c.net_buf_get) APIs must be used when passing buffers through
FIFOs. These APIs ensure that the buffer chains stay intact. The same
applies for passing buffers through a singly linked list, in which case
the [`net_buf_slist_put()`](#c.net_buf_slist_put) and [`net_buf_slist_get()`](#c.net_buf_slist_get)
functions must be used instead of [`sys_slist_append()`](../../../kernel/data_structures/slist.md#c.sys_slist_append "sys_slist_append") and
[`sys_slist_get()`](../../../kernel/data_structures/slist.md#c.sys_slist_get "sys_slist_get").

## [Common Operations](#id3)

The network buffer API provides some useful helpers for encoding and
decoding data in the buffers. To fully understand these helpers it’s
good to understand the basic names of operations used with them:

Add
:   Add data to the end of the buffer. Modifies the data length value
    while leaving the actual data pointer intact. Requires that there is
    enough tailroom in the buffer. Some examples of APIs for adding data:

    ```c
    void *net_buf_add(struct net_buf *buf, size_t len);
    void *net_buf_add_mem(struct net_buf *buf, const void *mem, size_t len);
    uint8_t *net_buf_add_u8(struct net_buf *buf, uint8_t value);
    void net_buf_add_le16(struct net_buf *buf, uint16_t value);
    void net_buf_add_le32(struct net_buf *buf, uint32_t value);
    ```

Remove
:   Remove data from the end of the buffer. Modifies the data length value
    while leaving the actual data pointer intact. Some examples of APIs for
    removing data:

    ```c
    void *net_buf_remove_mem(struct net_buf *buf, size_t len);
    uint8_t net_buf_remove_u8(struct net_buf *buf);
    uint16_t net_buf_remove_le16(struct net_buf *buf);
    uint32_t net_buf_remove_le32(struct net_buf *buf);
    ```

Push
:   Prepend data to the beginning of the buffer. Modifies both the data
    length value as well as the data pointer. Requires that there is
    enough headroom in the buffer. Some examples of APIs for pushing data:

    ```c
    void *net_buf_push(struct net_buf *buf, size_t len);
    void *net_buf_push_mem(struct net_buf *buf, const void *mem, size_t len);
    void net_buf_push_u8(struct net_buf *buf, uint8_t value);
    void net_buf_push_le16(struct net_buf *buf, uint16_t value);
    ```

Pull
:   Remove data from the beginning of the buffer. Modifies both the data
    length value as well as the data pointer. Some examples of APIs for
    pulling data:

    ```c
    void *net_buf_pull(struct net_buf *buf, size_t len);
    void *net_buf_pull_mem(struct net_buf *buf, size_t len);
    uint8_t net_buf_pull_u8(struct net_buf *buf);
    uint16_t net_buf_pull_le16(struct net_buf *buf);
    uint32_t net_buf_pull_le32(struct net_buf *buf);
    ```

The Add and Push operations are used when encoding data into the buffer,
whereas the Remove and Pull operations are used when decoding data from a
buffer.

## [Reference Counting](#id4)

Each network buffer is reference counted. The buffer is initially
acquired from a free buffers pool by calling [`net_buf_alloc()`](#c.net_buf_alloc),
resulting in a buffer with reference count 1. The reference count can be
incremented with [`net_buf_ref()`](#c.net_buf_ref) or decremented with
[`net_buf_unref()`](#c.net_buf_unref). When the count drops to zero the buffer is
automatically placed back to the free buffers pool.

## [API Reference](#id5)

*group* Network Buffer Library
:   Network buffer library.

    Defines

    NET\_BUF\_SIMPLE\_DEFINE(\_name, \_size)
    :   Define a [net\_buf\_simple](#structnet__buf__simple) stack variable.

        This is a helper macro which is used to define a [net\_buf\_simple](#structnet__buf__simple) object on the stack.

        Parameters:
        :   - **\_name** – Name of the [net\_buf\_simple](#structnet__buf__simple) object.
            - **\_size** – Maximum data storage for the buffer.

    NET\_BUF\_SIMPLE\_DEFINE\_STATIC(\_name, \_size)
    :   Define a static [net\_buf\_simple](#structnet__buf__simple) variable.

        This is a helper macro which is used to define a static [net\_buf\_simple](#structnet__buf__simple) object.

        Parameters:
        :   - **\_name** – Name of the [net\_buf\_simple](#structnet__buf__simple) object.
            - **\_size** – Maximum data storage for the buffer.

    NET\_BUF\_SIMPLE(\_size)
    :   Define a [net\_buf\_simple](#structnet__buf__simple) stack variable and get a pointer to it.

        This is a helper macro which is used to define a [net\_buf\_simple](#structnet__buf__simple) object on the stack and the get a pointer to it as follows:

        struct [net\_buf\_simple](#structnet__buf__simple) \*my\_buf = [NET\_BUF\_SIMPLE(10)](#group__net__buf_1ga0b01dc80027d13b1895379d4d1397207);

        After creating the object it needs to be initialized by calling [net\_buf\_simple\_init()](#group__net__buf_1ga040279b601191367dee013bab9916d8d).

        Parameters:
        :   - **\_size** – Maximum data storage for the buffer.

        Returns:
        :   Pointer to stack-allocated [net\_buf\_simple](#structnet__buf__simple) object.

    NET\_BUF\_EXTERNAL\_DATA
    :   Flag indicating that the buffer’s associated data pointer, points to externally allocated memory.

        Therefore once ref goes down to zero, the pointed data will not need to be deallocated. This never needs to be explicitly set or unset by the [net\_buf](#structnet__buf) API user. Such [net\_buf](#structnet__buf) is exclusively instantiated via [net\_buf\_alloc\_with\_data()](#group__net__buf_1ga8c24d0761d6d38facb6cca60c7c13c0c) function. Reference count mechanism however will behave the same way, and ref count going to 0 will free the [net\_buf](#structnet__buf) but no the data pointer in it.

    NET\_BUF\_POOL\_HEAP\_DEFINE(\_name, \_count, \_ud\_size, \_destroy)
    :   Define a new pool for buffers using the heap for the data.

        Defines a [net\_buf\_pool](#structnet__buf__pool) struct and the necessary memory storage (array of structs) for the needed amount of buffers. After this, the buffers can be accessed from the pool through net\_buf\_alloc. The pool is defined as a static variable, so if it needs to be exported outside the current module this needs to happen with the help of a separate pointer rather than an extern declaration.

        The data payload of the buffers will be allocated from the heap using k\_malloc, so CONFIG\_HEAP\_MEM\_POOL\_SIZE must be set to a positive value. This kind of pool does not support blocking on the data allocation, so the timeout passed to net\_buf\_alloc will be always treated as K\_NO\_WAIT when trying to allocate the data. This means that allocation failures, i.e. NULL returns, must always be handled cleanly.

        If provided with a custom destroy callback, this callback is responsible for eventually calling [net\_buf\_destroy()](#group__net__buf_1ga739249547eb37b839b3c1ebdbcb88d28) to complete the process of returning the buffer to the pool.

        Parameters:
        :   - **\_name** – Name of the pool variable.
            - **\_count** – Number of buffers in the pool.
            - **\_ud\_size** – User data space to reserve per buffer.
            - **\_destroy** – Optional destroy callback when buffer is freed.

    NET\_BUF\_POOL\_FIXED\_DEFINE(\_name, \_count, \_data\_size, \_ud\_size, \_destroy)
    :   Define a new pool for buffers based on fixed-size data.

        Defines a [net\_buf\_pool](#structnet__buf__pool) struct and the necessary memory storage (array of structs) for the needed amount of buffers. After this, the buffers can be accessed from the pool through net\_buf\_alloc. The pool is defined as a static variable, so if it needs to be exported outside the current module this needs to happen with the help of a separate pointer rather than an extern declaration.

        The data payload of the buffers will be allocated from a byte array of fixed sized chunks. This kind of pool does not support blocking on the data allocation, so the timeout passed to net\_buf\_alloc will be always treated as K\_NO\_WAIT when trying to allocate the data. This means that allocation failures, i.e. NULL returns, must always be handled cleanly.

        If provided with a custom destroy callback, this callback is responsible for eventually calling [net\_buf\_destroy()](#group__net__buf_1ga739249547eb37b839b3c1ebdbcb88d28) to complete the process of returning the buffer to the pool.

        Parameters:
        :   - **\_name** – Name of the pool variable.
            - **\_count** – Number of buffers in the pool.
            - **\_data\_size** – Maximum data payload per buffer.
            - **\_ud\_size** – User data space to reserve per buffer.
            - **\_destroy** – Optional destroy callback when buffer is freed.

    NET\_BUF\_POOL\_VAR\_DEFINE(\_name, \_count, \_data\_size, \_ud\_size, \_destroy)
    :   Define a new pool for buffers with variable size payloads.

        Defines a [net\_buf\_pool](#structnet__buf__pool) struct and the necessary memory storage (array of structs) for the needed amount of buffers. After this, the buffers can be accessed from the pool through net\_buf\_alloc. The pool is defined as a static variable, so if it needs to be exported outside the current module this needs to happen with the help of a separate pointer rather than an extern declaration.

        The data payload of the buffers will be based on a memory pool from which variable size payloads may be allocated.

        If provided with a custom destroy callback, this callback is responsible for eventually calling [net\_buf\_destroy()](#group__net__buf_1ga739249547eb37b839b3c1ebdbcb88d28) to complete the process of returning the buffer to the pool.

        Parameters:
        :   - **\_name** – Name of the pool variable.
            - **\_count** – Number of buffers in the pool.
            - **\_data\_size** – Total amount of memory available for data payloads.
            - **\_ud\_size** – User data space to reserve per buffer.
            - **\_destroy** – Optional destroy callback when buffer is freed.

    NET\_BUF\_POOL\_DEFINE(\_name, \_count, \_size, \_ud\_size, \_destroy)
    :   Define a new pool for buffers.

        Defines a [net\_buf\_pool](#structnet__buf__pool) struct and the necessary memory storage (array of structs) for the needed amount of buffers. After this,the buffers can be accessed from the pool through net\_buf\_alloc. The pool is defined as a static variable, so if it needs to be exported outside the current module this needs to happen with the help of a separate pointer rather than an extern declaration.

        If provided with a custom destroy callback this callback is responsible for eventually calling [net\_buf\_destroy()](#group__net__buf_1ga739249547eb37b839b3c1ebdbcb88d28) to complete the process of returning the buffer to the pool.

        Parameters:
        :   - **\_name** – Name of the pool variable.
            - **\_count** – Number of buffers in the pool.
            - **\_size** – Maximum data size for each buffer.
            - **\_ud\_size** – Amount of user data space to reserve.
            - **\_destroy** – Optional destroy callback when buffer is freed.

    Typedefs

    typedef struct [net\_buf](#c.net_buf) \*(\*net\_buf\_allocator\_cb)([k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout, void \*user\_data)
    :   Network buffer allocator callback.

        The allocator callback is called when net\_buf\_append\_bytes needs to allocate a new [net\_buf](#structnet__buf).

        Param timeout:
        :   Affects the action taken should the net buf pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout.

        Param user\_data:
        :   The user data given in net\_buf\_append\_bytes call.

        Return:
        :   pointer to allocated [net\_buf](#structnet__buf) or NULL on error.

    Functions

    static inline void net\_buf\_simple\_init(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, size\_t reserve\_head)
    :   Initialize a [net\_buf\_simple](#structnet__buf__simple) object.

        This needs to be called after creating a [net\_buf\_simple](#structnet__buf__simple) object using the NET\_BUF\_SIMPLE macro.

        Parameters:
        :   - **buf** – Buffer to initialize.
            - **reserve\_head** – Headroom to reserve.

    void net\_buf\_simple\_init\_with\_data(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, void \*data, size\_t size)
    :   Initialize a [net\_buf\_simple](#structnet__buf__simple) object with data.

        Initialized buffer object with external data.

        Parameters:
        :   - **buf** – Buffer to initialize.
            - **data** – External data pointer
            - **size** – Amount of data the pointed data buffer if able to fit.

    static inline void net\_buf\_simple\_reset(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Reset buffer.

        Reset buffer data so it can be reused for other purposes.

        Parameters:
        :   - **buf** – Buffer to reset.

    void net\_buf\_simple\_clone(const struct [net\_buf\_simple](#c.net_buf_simple) \*original, struct [net\_buf\_simple](#c.net_buf_simple) \*clone)
    :   Clone buffer state, using the same data buffer.

        Initializes a buffer to point to the same data as an existing buffer. Allows operations on the same data without altering the length and offset of the original.

        Parameters:
        :   - **original** – Buffer to clone.
            - **clone** – The new clone.

    void \*net\_buf\_simple\_add(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, size\_t len)
    :   Prepare data to be added at the end of the buffer.

        Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to increment the length with.

        Returns:
        :   The original tail of the buffer.

    void \*net\_buf\_simple\_add\_mem(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, const void \*mem, size\_t len)
    :   Copy given number of bytes from memory to the end of the buffer.

        Increments the data length of the buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **mem** – Location of data to be added.
            - **len** – Length of data to be added

        Returns:
        :   The original tail of the buffer.

    uint8\_t \*net\_buf\_simple\_add\_u8(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint8\_t val)
    :   Add (8-bit) byte at the end of the buffer.

        Increments the data length of the buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – byte value to be added.

        Returns:
        :   Pointer to the value added

    void net\_buf\_simple\_add\_le16(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint16\_t val)
    :   Add 16-bit value at the end of the buffer.

        Adds 16-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 16-bit value to be added.

    void net\_buf\_simple\_add\_be16(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint16\_t val)
    :   Add 16-bit value at the end of the buffer.

        Adds 16-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 16-bit value to be added.

    void net\_buf\_simple\_add\_le24(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint32\_t val)
    :   Add 24-bit value at the end of the buffer.

        Adds 24-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 24-bit value to be added.

    void net\_buf\_simple\_add\_be24(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint32\_t val)
    :   Add 24-bit value at the end of the buffer.

        Adds 24-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 24-bit value to be added.

    void net\_buf\_simple\_add\_le32(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint32\_t val)
    :   Add 32-bit value at the end of the buffer.

        Adds 32-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 32-bit value to be added.

    void net\_buf\_simple\_add\_be32(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint32\_t val)
    :   Add 32-bit value at the end of the buffer.

        Adds 32-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 32-bit value to be added.

    void net\_buf\_simple\_add\_le40(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Add 40-bit value at the end of the buffer.

        Adds 40-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 40-bit value to be added.

    void net\_buf\_simple\_add\_be40(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Add 40-bit value at the end of the buffer.

        Adds 40-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 40-bit value to be added.

    void net\_buf\_simple\_add\_le48(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Add 48-bit value at the end of the buffer.

        Adds 48-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 48-bit value to be added.

    void net\_buf\_simple\_add\_be48(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Add 48-bit value at the end of the buffer.

        Adds 48-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 48-bit value to be added.

    void net\_buf\_simple\_add\_le64(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Add 64-bit value at the end of the buffer.

        Adds 64-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 64-bit value to be added.

    void net\_buf\_simple\_add\_be64(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Add 64-bit value at the end of the buffer.

        Adds 64-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 64-bit value to be added.

    void \*net\_buf\_simple\_remove\_mem(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, size\_t len)
    :   Remove data from the end of the buffer.

        Removes data from the end of the buffer by modifying the buffer length.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to remove.

        Returns:
        :   New end of the buffer data.

    uint8\_t net\_buf\_simple\_remove\_u8(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove a 8-bit value from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 8-bit values.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   The 8-bit removed value

    uint16\_t net\_buf\_simple\_remove\_le16(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 16 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 16-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   16-bit value converted from little endian to host endian.

    uint16\_t net\_buf\_simple\_remove\_be16(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 16 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 16-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   16-bit value converted from big endian to host endian.

    uint32\_t net\_buf\_simple\_remove\_le24(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 24 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 24-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   24-bit value converted from little endian to host endian.

    uint32\_t net\_buf\_simple\_remove\_be24(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 24 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 24-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   24-bit value converted from big endian to host endian.

    uint32\_t net\_buf\_simple\_remove\_le32(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 32 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 32-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   32-bit value converted from little endian to host endian.

    uint32\_t net\_buf\_simple\_remove\_be32(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 32 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 32-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   32-bit value converted from big endian to host endian.

    uint64\_t net\_buf\_simple\_remove\_le40(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 40 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 40-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   40-bit value converted from little endian to host endian.

    uint64\_t net\_buf\_simple\_remove\_be40(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 40 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 40-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   40-bit value converted from big endian to host endian.

    uint64\_t net\_buf\_simple\_remove\_le48(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 48 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 48-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   48-bit value converted from little endian to host endian.

    uint64\_t net\_buf\_simple\_remove\_be48(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 48 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 48-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   48-bit value converted from big endian to host endian.

    uint64\_t net\_buf\_simple\_remove\_le64(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 64 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 64-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   64-bit value converted from little endian to host endian.

    uint64\_t net\_buf\_simple\_remove\_be64(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 64 bits from the end of the buffer.

        Same idea as with [net\_buf\_simple\_remove\_mem()](#group__net__buf_1ga8473bdffadc05b22335a321df89f4b83), but a helper for operating on 64-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   64-bit value converted from big endian to host endian.

    void \*net\_buf\_simple\_push(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, size\_t len)
    :   Prepare data to be added to the start of the buffer.

        Modifies the data pointer and buffer length to account for more data in the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to add to the beginning.

        Returns:
        :   The new beginning of the buffer data.

    void \*net\_buf\_simple\_push\_mem(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, const void \*mem, size\_t len)
    :   Copy given number of bytes from memory to the start of the buffer.

        Modifies the data pointer and buffer length to account for more data in the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **mem** – Location of data to be added.
            - **len** – Length of data to be added.

        Returns:
        :   The new beginning of the buffer data.

    void net\_buf\_simple\_push\_le16(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint16\_t val)
    :   Push 16-bit value to the beginning of the buffer.

        Adds 16-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 16-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_be16(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint16\_t val)
    :   Push 16-bit value to the beginning of the buffer.

        Adds 16-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 16-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_u8(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint8\_t val)
    :   Push 8-bit value to the beginning of the buffer.

        Adds 8-bit value the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 8-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_le24(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint32\_t val)
    :   Push 24-bit value to the beginning of the buffer.

        Adds 24-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 24-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_be24(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint32\_t val)
    :   Push 24-bit value to the beginning of the buffer.

        Adds 24-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 24-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_le32(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint32\_t val)
    :   Push 32-bit value to the beginning of the buffer.

        Adds 32-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 32-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_be32(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint32\_t val)
    :   Push 32-bit value to the beginning of the buffer.

        Adds 32-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 32-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_le40(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Push 40-bit value to the beginning of the buffer.

        Adds 40-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 40-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_be40(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Push 40-bit value to the beginning of the buffer.

        Adds 40-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 40-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_le48(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Push 48-bit value to the beginning of the buffer.

        Adds 48-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 48-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_be48(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Push 48-bit value to the beginning of the buffer.

        Adds 48-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 48-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_le64(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Push 64-bit value to the beginning of the buffer.

        Adds 64-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 64-bit value to be pushed to the buffer.

    void net\_buf\_simple\_push\_be64(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, uint64\_t val)
    :   Push 64-bit value to the beginning of the buffer.

        Adds 64-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 64-bit value to be pushed to the buffer.

    void \*net\_buf\_simple\_pull(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, size\_t len)
    :   Remove data from the beginning of the buffer.

        Removes data from the beginning of the buffer by modifying the data pointer and buffer length.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to remove.

        Returns:
        :   New beginning of the buffer data.

    void \*net\_buf\_simple\_pull\_mem(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, size\_t len)
    :   Remove data from the beginning of the buffer.

        Removes data from the beginning of the buffer by modifying the data pointer and buffer length.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to remove.

        Returns:
        :   Pointer to the old location of the buffer data.

    uint8\_t net\_buf\_simple\_pull\_u8(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove a 8-bit value from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 8-bit values.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   The 8-bit removed value

    uint16\_t net\_buf\_simple\_pull\_le16(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 16 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 16-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   16-bit value converted from little endian to host endian.

    uint16\_t net\_buf\_simple\_pull\_be16(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 16 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 16-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   16-bit value converted from big endian to host endian.

    uint32\_t net\_buf\_simple\_pull\_le24(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 24 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 24-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   24-bit value converted from little endian to host endian.

    uint32\_t net\_buf\_simple\_pull\_be24(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 24 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 24-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   24-bit value converted from big endian to host endian.

    uint32\_t net\_buf\_simple\_pull\_le32(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 32 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 32-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   32-bit value converted from little endian to host endian.

    uint32\_t net\_buf\_simple\_pull\_be32(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 32 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 32-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   32-bit value converted from big endian to host endian.

    uint64\_t net\_buf\_simple\_pull\_le40(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 40 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 40-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   40-bit value converted from little endian to host endian.

    uint64\_t net\_buf\_simple\_pull\_be40(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 40 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 40-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   40-bit value converted from big endian to host endian.

    uint64\_t net\_buf\_simple\_pull\_le48(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 48 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 48-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   48-bit value converted from little endian to host endian.

    uint64\_t net\_buf\_simple\_pull\_be48(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 48 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 48-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   48-bit value converted from big endian to host endian.

    uint64\_t net\_buf\_simple\_pull\_le64(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 64 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 64-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   64-bit value converted from little endian to host endian.

    uint64\_t net\_buf\_simple\_pull\_be64(struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Remove and convert 64 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_simple\_pull()](#group__net__buf_1gaf5ab4a5fe4a6226be72a510fea0ed8a8), but a helper for operating on 64-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   64-bit value converted from big endian to host endian.

    static inline uint8\_t \*net\_buf\_simple\_tail(const struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Get the tail pointer for a buffer.

        Get a pointer to the end of the data in a buffer.

        Parameters:
        :   - **buf** – Buffer.

        Returns:
        :   Tail pointer for the buffer.

    size\_t net\_buf\_simple\_headroom(const struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Check buffer headroom.

        Check how much free space there is in the beginning of the buffer.

        buf A valid pointer on a buffer

        Returns:
        :   Number of bytes available in the beginning of the buffer.

    size\_t net\_buf\_simple\_tailroom(const struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Check buffer tailroom.

        Check how much free space there is at the end of the buffer.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   Number of bytes available at the end of the buffer.

    uint16\_t net\_buf\_simple\_max\_len(const struct [net\_buf\_simple](#c.net_buf_simple) \*buf)
    :   Check maximum [net\_buf\_simple::len](#structnet__buf__simple_1ae8707c50d70c26b53281b40eb1720cf3) value.

        This value is depending on the number of bytes being reserved as headroom.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   Number of bytes usable behind the [net\_buf\_simple::data](#structnet__buf__simple_1ad232efff435f425d30ac78f5abf2d8b1) pointer.

    static inline void net\_buf\_simple\_save(const struct [net\_buf\_simple](#c.net_buf_simple) \*buf, struct [net\_buf\_simple\_state](#c.net_buf_simple_state) \*state)
    :   Save the parsing state of a buffer.

        Saves the parsing state of a buffer so it can be restored later.

        Parameters:
        :   - **buf** – Buffer from which the state should be saved.
            - **state** – Storage for the state.

    static inline void net\_buf\_simple\_restore(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, struct [net\_buf\_simple\_state](#c.net_buf_simple_state) \*state)
    :   Restore the parsing state of a buffer.

        Restores the parsing state of a buffer from a state previously stored by [net\_buf\_simple\_save()](#group__net__buf_1gabf5b098aa0926d9b7fb88baff8a3e2d8).

        Parameters:
        :   - **buf** – Buffer to which the state should be restored.
            - **state** – Stored state.

    struct [net\_buf\_pool](#c.net_buf_pool) \*net\_buf\_pool\_get(int id)
    :   Looks up a pool based on its ID.

        Parameters:
        :   - **id** – Pool ID (e.g. from buf->pool\_id).

        Returns:
        :   Pointer to pool.

    int net\_buf\_id(const struct [net\_buf](#c.net_buf) \*buf)
    :   Get a zero-based index for a buffer.

        This function will translate a buffer into a zero-based index, based on its placement in its buffer pool. This can be useful if you want to associate an external array of meta-data contexts with the buffers of a pool.

        Parameters:
        :   - **buf** – Network buffer.

        Returns:
        :   Zero-based index for the buffer.

    struct [net\_buf](#c.net_buf) \*net\_buf\_alloc\_fixed(struct [net\_buf\_pool](#c.net_buf_pool) \*pool, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate a new fixed buffer from a pool.

        Note

        Some types of data allocators do not support blocking (such as the HEAP type). In this case it’s still possible for [net\_buf\_alloc()](#group__net__buf_1ga534366f3b5c7f41a28372c12149ca005) to fail (return NULL) even if it was given K\_FOREVER.

        Note

        The timeout value will be overridden to K\_NO\_WAIT if called from the system workqueue.

        Parameters:
        :   - **pool** – Which pool to allocate the buffer from.
            - **timeout** – Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout.

        Returns:
        :   New buffer or NULL if out of buffers.

    static inline struct [net\_buf](#c.net_buf) \*net\_buf\_alloc(struct [net\_buf\_pool](#c.net_buf_pool) \*pool, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Note

        Some types of data allocators do not support blocking (such as the HEAP type). In this case it’s still possible for [net\_buf\_alloc()](#group__net__buf_1ga534366f3b5c7f41a28372c12149ca005) to fail (return NULL) even if it was given K\_FOREVER.

        Note

        The timeout value will be overridden to K\_NO\_WAIT if called from the system workqueue.

        Parameters:
        :   - **pool** – Which pool to allocate the buffer from.
            - **timeout** – Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout.

        Returns:
        :   New buffer or NULL if out of buffers.

    struct [net\_buf](#c.net_buf) \*net\_buf\_alloc\_len(struct [net\_buf\_pool](#c.net_buf_pool) \*pool, size\_t size, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate a new variable length buffer from a pool.

        Note

        Some types of data allocators do not support blocking (such as the HEAP type). In this case it’s still possible for [net\_buf\_alloc()](#group__net__buf_1ga534366f3b5c7f41a28372c12149ca005) to fail (return NULL) even if it was given K\_FOREVER.

        Note

        The timeout value will be overridden to K\_NO\_WAIT if called from the system workqueue.

        Parameters:
        :   - **pool** – Which pool to allocate the buffer from.
            - **size** – Amount of data the buffer must be able to fit.
            - **timeout** – Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout.

        Returns:
        :   New buffer or NULL if out of buffers.

    struct [net\_buf](#c.net_buf) \*net\_buf\_alloc\_with\_data(struct [net\_buf\_pool](#c.net_buf_pool) \*pool, void \*data, size\_t size, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate a new buffer from a pool but with external data pointer.

        Allocate a new buffer from a pool, where the data pointer comes from the user and not from the pool.

        Note

        Some types of data allocators do not support blocking (such as the HEAP type). In this case it’s still possible for [net\_buf\_alloc()](#group__net__buf_1ga534366f3b5c7f41a28372c12149ca005) to fail (return NULL) even if it was given K\_FOREVER.

        Note

        The timeout value will be overridden to K\_NO\_WAIT if called from the system workqueue.

        Parameters:
        :   - **pool** – Which pool to allocate the buffer from.
            - **data** – External data pointer
            - **size** – Amount of data the pointed data buffer if able to fit.
            - **timeout** – Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout.

        Returns:
        :   New buffer or NULL if out of buffers.

    struct [net\_buf](#c.net_buf) \*net\_buf\_get(struct k\_fifo \*fifo, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Get a buffer from a FIFO.

        This function is NOT thread-safe if the buffers in the FIFO contain fragments.

        Parameters:
        :   - **fifo** – Which FIFO to take the buffer from.
            - **timeout** – Affects the action taken should the FIFO be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout.

        Returns:
        :   New buffer or NULL if the FIFO is empty.

    static inline void net\_buf\_destroy(struct [net\_buf](#c.net_buf) \*buf)
    :   Destroy buffer from custom destroy callback.

        This helper is only intended to be used from custom destroy callbacks. If no custom destroy callback is given to NET\_BUF\_POOL\_\*\_DEFINE() then there is no need to use this API.

        Parameters:
        :   - **buf** – Buffer to destroy.

    void net\_buf\_reset(struct [net\_buf](#c.net_buf) \*buf)
    :   Reset buffer.

        Reset buffer data and flags so it can be reused for other purposes.

        Parameters:
        :   - **buf** – Buffer to reset.

    void net\_buf\_simple\_reserve(struct [net\_buf\_simple](#c.net_buf_simple) \*buf, size\_t reserve)
    :   Initialize buffer with the given headroom.

        The buffer is not expected to contain any data when this API is called.

        Parameters:
        :   - **buf** – Buffer to initialize.
            - **reserve** – How much headroom to reserve.

    void net\_buf\_slist\_put([sys\_slist\_t](../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") \*list, struct [net\_buf](#c.net_buf) \*buf)
    :   Put a buffer into a list.

        If the buffer contains follow-up fragments this function will take care of inserting them as well into the list.

        Parameters:
        :   - **list** – Which list to append the buffer to.
            - **buf** – Buffer.

    struct [net\_buf](#c.net_buf) \*net\_buf\_slist\_get([sys\_slist\_t](../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") \*list)
    :   Get a buffer from a list.

        If the buffer had any fragments, these will automatically be recovered from the list as well and be placed to the buffer’s fragment list.

        Parameters:
        :   - **list** – Which list to take the buffer from.

        Returns:
        :   New buffer or NULL if the FIFO is empty.

    void net\_buf\_put(struct k\_fifo \*fifo, struct [net\_buf](#c.net_buf) \*buf)
    :   Put a buffer to the end of a FIFO.

        If the buffer contains follow-up fragments this function will take care of inserting them as well into the FIFO.

        Parameters:
        :   - **fifo** – Which FIFO to put the buffer to.
            - **buf** – Buffer.

    void net\_buf\_unref(struct [net\_buf](#c.net_buf) \*buf)
    :   Decrements the reference count of a buffer.

        The buffer is put back into the pool if the reference count reaches zero.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

    struct [net\_buf](#c.net_buf) \*net\_buf\_ref(struct [net\_buf](#c.net_buf) \*buf)
    :   Increment the reference count of a buffer.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   the buffer newly referenced

    struct [net\_buf](#c.net_buf) \*net\_buf\_clone(struct [net\_buf](#c.net_buf) \*buf, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Clone buffer.

        Duplicate given buffer including any (user) data and headers currently stored.

        Parameters:
        :   - **buf** – A valid pointer on a buffer
            - **timeout** – Affects the action taken should the pool be empty. If K\_NO\_WAIT, then return immediately. If K\_FOREVER, then wait as long as necessary. Otherwise, wait until the specified timeout.

        Returns:
        :   Cloned buffer or NULL if out of buffers.

    static inline void \*net\_buf\_user\_data(const struct [net\_buf](#c.net_buf) \*buf)
    :   Get a pointer to the user data of a buffer.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   Pointer to the user data of the buffer.

    int net\_buf\_user\_data\_copy(struct [net\_buf](#c.net_buf) \*dst, const struct [net\_buf](#c.net_buf) \*src)
    :   Copy user data from one to another buffer.

        Parameters:
        :   - **dst** – A valid pointer to a buffer gettings its user data overwritten.
            - **src** – A valid pointer to a buffer gettings its user data copied. User data size must be equal to or exceed *dst*.

        Returns:
        :   0 on success or negative error number on failure.

    static inline void net\_buf\_reserve(struct [net\_buf](#c.net_buf) \*buf, size\_t reserve)
    :   Initialize buffer with the given headroom.

        The buffer is not expected to contain any data when this API is called.

        Parameters:
        :   - **buf** – Buffer to initialize.
            - **reserve** – How much headroom to reserve.

    static inline void \*net\_buf\_add(struct [net\_buf](#c.net_buf) \*buf, size\_t len)
    :   Prepare data to be added at the end of the buffer.

        Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to increment the length with.

        Returns:
        :   The original tail of the buffer.

    static inline void \*net\_buf\_add\_mem(struct [net\_buf](#c.net_buf) \*buf, const void \*mem, size\_t len)
    :   Copies the given number of bytes to the end of the buffer.

        Increments the data length of the buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **mem** – Location of data to be added.
            - **len** – Length of data to be added

        Returns:
        :   The original tail of the buffer.

    static inline uint8\_t \*net\_buf\_add\_u8(struct [net\_buf](#c.net_buf) \*buf, uint8\_t val)
    :   Add (8-bit) byte at the end of the buffer.

        Increments the data length of the buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – byte value to be added.

        Returns:
        :   Pointer to the value added

    static inline void net\_buf\_add\_le16(struct [net\_buf](#c.net_buf) \*buf, uint16\_t val)
    :   Add 16-bit value at the end of the buffer.

        Adds 16-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 16-bit value to be added.

    static inline void net\_buf\_add\_be16(struct [net\_buf](#c.net_buf) \*buf, uint16\_t val)
    :   Add 16-bit value at the end of the buffer.

        Adds 16-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 16-bit value to be added.

    static inline void net\_buf\_add\_le24(struct [net\_buf](#c.net_buf) \*buf, uint32\_t val)
    :   Add 24-bit value at the end of the buffer.

        Adds 24-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 24-bit value to be added.

    static inline void net\_buf\_add\_be24(struct [net\_buf](#c.net_buf) \*buf, uint32\_t val)
    :   Add 24-bit value at the end of the buffer.

        Adds 24-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 24-bit value to be added.

    static inline void net\_buf\_add\_le32(struct [net\_buf](#c.net_buf) \*buf, uint32\_t val)
    :   Add 32-bit value at the end of the buffer.

        Adds 32-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 32-bit value to be added.

    static inline void net\_buf\_add\_be32(struct [net\_buf](#c.net_buf) \*buf, uint32\_t val)
    :   Add 32-bit value at the end of the buffer.

        Adds 32-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 32-bit value to be added.

    static inline void net\_buf\_add\_le40(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Add 40-bit value at the end of the buffer.

        Adds 40-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 40-bit value to be added.

    static inline void net\_buf\_add\_be40(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Add 40-bit value at the end of the buffer.

        Adds 40-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 40-bit value to be added.

    static inline void net\_buf\_add\_le48(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Add 48-bit value at the end of the buffer.

        Adds 48-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 48-bit value to be added.

    static inline void net\_buf\_add\_be48(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Add 48-bit value at the end of the buffer.

        Adds 48-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 48-bit value to be added.

    static inline void net\_buf\_add\_le64(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Add 64-bit value at the end of the buffer.

        Adds 64-bit value in little endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 64-bit value to be added.

    static inline void net\_buf\_add\_be64(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Add 64-bit value at the end of the buffer.

        Adds 64-bit value in big endian format at the end of buffer. Increments the data length of a buffer to account for more data at the end.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 64-bit value to be added.

    static inline void \*net\_buf\_remove\_mem(struct [net\_buf](#c.net_buf) \*buf, size\_t len)
    :   Remove data from the end of the buffer.

        Removes data from the end of the buffer by modifying the buffer length.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to remove.

        Returns:
        :   New end of the buffer data.

    static inline uint8\_t net\_buf\_remove\_u8(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove a 8-bit value from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 8-bit values.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   The 8-bit removed value

    static inline uint16\_t net\_buf\_remove\_le16(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 16 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 16-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   16-bit value converted from little endian to host endian.

    static inline uint16\_t net\_buf\_remove\_be16(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 16 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 16-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   16-bit value converted from big endian to host endian.

    static inline uint32\_t net\_buf\_remove\_be24(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 24 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 24-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   24-bit value converted from big endian to host endian.

    static inline uint32\_t net\_buf\_remove\_le24(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 24 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 24-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   24-bit value converted from little endian to host endian.

    static inline uint32\_t net\_buf\_remove\_le32(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 32 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 32-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   32-bit value converted from little endian to host endian.

    static inline uint32\_t net\_buf\_remove\_be32(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 32 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 32-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   32-bit value converted from big endian to host endian.

    static inline uint64\_t net\_buf\_remove\_le40(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 40 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 40-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   40-bit value converted from little endian to host endian.

    static inline uint64\_t net\_buf\_remove\_be40(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 40 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 40-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   40-bit value converted from big endian to host endian.

    static inline uint64\_t net\_buf\_remove\_le48(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 48 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 48-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   48-bit value converted from little endian to host endian.

    static inline uint64\_t net\_buf\_remove\_be48(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 48 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 48-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   48-bit value converted from big endian to host endian.

    static inline uint64\_t net\_buf\_remove\_le64(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 64 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 64-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   64-bit value converted from little endian to host endian.

    static inline uint64\_t net\_buf\_remove\_be64(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 64 bits from the end of the buffer.

        Same idea as with [net\_buf\_remove\_mem()](#group__net__buf_1gace5ad98eac4772db3b0fa2181912f1f0), but a helper for operating on 64-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   64-bit value converted from big endian to host endian.

    static inline void \*net\_buf\_push(struct [net\_buf](#c.net_buf) \*buf, size\_t len)
    :   Prepare data to be added at the start of the buffer.

        Modifies the data pointer and buffer length to account for more data in the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to add to the beginning.

        Returns:
        :   The new beginning of the buffer data.

    static inline void \*net\_buf\_push\_mem(struct [net\_buf](#c.net_buf) \*buf, const void \*mem, size\_t len)
    :   Copies the given number of bytes to the start of the buffer.

        Modifies the data pointer and buffer length to account for more data in the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **mem** – Location of data to be added.
            - **len** – Length of data to be added.

        Returns:
        :   The new beginning of the buffer data.

    static inline void net\_buf\_push\_u8(struct [net\_buf](#c.net_buf) \*buf, uint8\_t val)
    :   Push 8-bit value to the beginning of the buffer.

        Adds 8-bit value the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 8-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_le16(struct [net\_buf](#c.net_buf) \*buf, uint16\_t val)
    :   Push 16-bit value to the beginning of the buffer.

        Adds 16-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 16-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_be16(struct [net\_buf](#c.net_buf) \*buf, uint16\_t val)
    :   Push 16-bit value to the beginning of the buffer.

        Adds 16-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 16-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_le24(struct [net\_buf](#c.net_buf) \*buf, uint32\_t val)
    :   Push 24-bit value to the beginning of the buffer.

        Adds 24-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 24-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_be24(struct [net\_buf](#c.net_buf) \*buf, uint32\_t val)
    :   Push 24-bit value to the beginning of the buffer.

        Adds 24-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 24-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_le32(struct [net\_buf](#c.net_buf) \*buf, uint32\_t val)
    :   Push 32-bit value to the beginning of the buffer.

        Adds 32-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 32-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_be32(struct [net\_buf](#c.net_buf) \*buf, uint32\_t val)
    :   Push 32-bit value to the beginning of the buffer.

        Adds 32-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 32-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_le40(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Push 40-bit value to the beginning of the buffer.

        Adds 40-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 40-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_be40(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Push 40-bit value to the beginning of the buffer.

        Adds 40-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 40-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_le48(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Push 48-bit value to the beginning of the buffer.

        Adds 48-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 48-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_be48(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Push 48-bit value to the beginning of the buffer.

        Adds 48-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 48-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_le64(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Push 64-bit value to the beginning of the buffer.

        Adds 64-bit value in little endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 64-bit value to be pushed to the buffer.

    static inline void net\_buf\_push\_be64(struct [net\_buf](#c.net_buf) \*buf, uint64\_t val)
    :   Push 64-bit value to the beginning of the buffer.

        Adds 64-bit value in big endian format to the beginning of the buffer.

        Parameters:
        :   - **buf** – Buffer to update.
            - **val** – 64-bit value to be pushed to the buffer.

    static inline void \*net\_buf\_pull(struct [net\_buf](#c.net_buf) \*buf, size\_t len)
    :   Remove data from the beginning of the buffer.

        Removes data from the beginning of the buffer by modifying the data pointer and buffer length.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to remove.

        Returns:
        :   New beginning of the buffer data.

    static inline void \*net\_buf\_pull\_mem(struct [net\_buf](#c.net_buf) \*buf, size\_t len)
    :   Remove data from the beginning of the buffer.

        Removes data from the beginning of the buffer by modifying the data pointer and buffer length.

        Parameters:
        :   - **buf** – Buffer to update.
            - **len** – Number of bytes to remove.

        Returns:
        :   Pointer to the old beginning of the buffer data.

    static inline uint8\_t net\_buf\_pull\_u8(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove a 8-bit value from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 8-bit values.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   The 8-bit removed value

    static inline uint16\_t net\_buf\_pull\_le16(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 16 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 16-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   16-bit value converted from little endian to host endian.

    static inline uint16\_t net\_buf\_pull\_be16(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 16 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 16-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   16-bit value converted from big endian to host endian.

    static inline uint32\_t net\_buf\_pull\_le24(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 24 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 24-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   24-bit value converted from little endian to host endian.

    static inline uint32\_t net\_buf\_pull\_be24(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 24 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 24-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   24-bit value converted from big endian to host endian.

    static inline uint32\_t net\_buf\_pull\_le32(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 32 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 32-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   32-bit value converted from little endian to host endian.

    static inline uint32\_t net\_buf\_pull\_be32(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 32 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 32-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   32-bit value converted from big endian to host endian.

    static inline uint64\_t net\_buf\_pull\_le40(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 40 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 40-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   40-bit value converted from little endian to host endian.

    static inline uint64\_t net\_buf\_pull\_be40(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 40 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 40-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   40-bit value converted from big endian to host endian.

    static inline uint64\_t net\_buf\_pull\_le48(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 48 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 48-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   48-bit value converted from little endian to host endian.

    static inline uint64\_t net\_buf\_pull\_be48(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 48 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 48-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   48-bit value converted from big endian to host endian.

    static inline uint64\_t net\_buf\_pull\_le64(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 64 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 64-bit little endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer.

        Returns:
        :   64-bit value converted from little endian to host endian.

    static inline uint64\_t net\_buf\_pull\_be64(struct [net\_buf](#c.net_buf) \*buf)
    :   Remove and convert 64 bits from the beginning of the buffer.

        Same idea as with [net\_buf\_pull()](#group__net__buf_1gaef433d92734dd8691c292abdb823ba0e), but a helper for operating on 64-bit big endian data.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   64-bit value converted from big endian to host endian.

    static inline size\_t net\_buf\_tailroom(const struct [net\_buf](#c.net_buf) \*buf)
    :   Check buffer tailroom.

        Check how much free space there is at the end of the buffer.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   Number of bytes available at the end of the buffer.

    static inline size\_t net\_buf\_headroom(const struct [net\_buf](#c.net_buf) \*buf)
    :   Check buffer headroom.

        Check how much free space there is in the beginning of the buffer.

        buf A valid pointer on a buffer

        Returns:
        :   Number of bytes available in the beginning of the buffer.

    static inline uint16\_t net\_buf\_max\_len(const struct [net\_buf](#c.net_buf) \*buf)
    :   Check maximum [net\_buf::len](#structnet__buf_1ae75b7ca728fb7440ea483be8bf88bc38) value.

        This value is depending on the number of bytes being reserved as headroom.

        Parameters:
        :   - **buf** – A valid pointer on a buffer

        Returns:
        :   Number of bytes usable behind the [net\_buf::data](#structnet__buf_1ac6eef59915e7ce167442fdacbbfb5e56) pointer.

    static inline uint8\_t \*net\_buf\_tail(const struct [net\_buf](#c.net_buf) \*buf)
    :   Get the tail pointer for a buffer.

        Get a pointer to the end of the data in a buffer.

        Parameters:
        :   - **buf** – Buffer.

        Returns:
        :   Tail pointer for the buffer.

    struct [net\_buf](#c.net_buf) \*net\_buf\_frag\_last(struct [net\_buf](#c.net_buf) \*frags)
    :   Find the last fragment in the fragment list.

        Returns:
        :   Pointer to last fragment in the list.

    void net\_buf\_frag\_insert(struct [net\_buf](#c.net_buf) \*parent, struct [net\_buf](#c.net_buf) \*frag)
    :   Insert a new fragment to a chain of bufs.

        Insert a new fragment into the buffer fragments list after the parent.

        Note: This function takes ownership of the fragment reference so the caller is not required to unref.

        Parameters:
        :   - **parent** – Parent buffer/fragment.
            - **frag** – Fragment to insert.

    struct [net\_buf](#c.net_buf) \*net\_buf\_frag\_add(struct [net\_buf](#c.net_buf) \*head, struct [net\_buf](#c.net_buf) \*frag)
    :   Add a new fragment to the end of a chain of bufs.

        Append a new fragment into the buffer fragments list.

        Note: This function takes ownership of the fragment reference so the caller is not required to unref.

        Parameters:
        :   - **head** – Head of the fragment chain.
            - **frag** – Fragment to add.

        Returns:
        :   New head of the fragment chain. Either head (if head was non-NULL) or frag (if head was NULL).

    struct [net\_buf](#c.net_buf) \*net\_buf\_frag\_del(struct [net\_buf](#c.net_buf) \*parent, struct [net\_buf](#c.net_buf) \*frag)
    :   Delete existing fragment from a chain of bufs.

        Parameters:
        :   - **parent** – Parent buffer/fragment, or NULL if there is no parent.
            - **frag** – Fragment to delete.

        Returns:
        :   Pointer to the buffer following the fragment, or NULL if it had no further fragments.

    size\_t net\_buf\_linearize(void \*dst, size\_t dst\_len, const struct [net\_buf](#c.net_buf) \*src, size\_t offset, size\_t len)
    :   Copy bytes from [net\_buf](#structnet__buf) chain starting at offset to linear buffer.

        Copy (extract) *len* bytes from *src* [net\_buf](#structnet__buf) chain, starting from *offset* in it, to a linear buffer *dst*. Return number of bytes actually copied, which may be less than requested, if [net\_buf](#structnet__buf) chain doesn’t have enough data, or destination buffer is too small.

        Parameters:
        :   - **dst** – Destination buffer
            - **dst\_len** – Destination buffer length
            - **src** – Source [net\_buf](#structnet__buf) chain
            - **offset** – Starting offset to copy from
            - **len** – Number of bytes to copy

        Returns:
        :   number of bytes actually copied

    size\_t net\_buf\_append\_bytes(struct [net\_buf](#c.net_buf) \*buf, size\_t len, const void \*value, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout, [net\_buf\_allocator\_cb](#c.net_buf_allocator_cb) allocate\_cb, void \*user\_data)
    :   Append data to a list of [net\_buf](#structnet__buf).

        Append data to a [net\_buf](#structnet__buf). If there is not enough space in the [net\_buf](#structnet__buf) then more [net\_buf](#structnet__buf) will be added, unless there are no free [net\_buf](#structnet__buf) and timeout occurs. If not allocator is provided it attempts to allocate from the same pool as the original buffer.

        Parameters:
        :   - **buf** – Network buffer.
            - **len** – Total length of input data
            - **value** – Data to be added
            - **timeout** – Timeout is passed to the [net\_buf](#structnet__buf) allocator callback.
            - **allocate\_cb** – When a new [net\_buf](#structnet__buf) is required, use this callback.
            - **user\_data** – A user data pointer to be supplied to the allocate\_cb. This pointer is can be anything from a mem\_pool or a [net\_pkt](net_pkt.md#structnet__pkt), the logic is left up to the allocate\_cb function.

        Returns:
        :   Length of data actually added. This may be less than input length if other timeout than K\_FOREVER was used, and there were no free fragments in a pool to accommodate all data.

    size\_t net\_buf\_data\_match(const struct [net\_buf](#c.net_buf) \*buf, size\_t offset, const void \*data, size\_t len)
    :   Match data with a [net\_buf](#structnet__buf)’s content.

        Compare data with a content of a [net\_buf](#structnet__buf). Provide information about the number of bytes matching between both. If needed, traverse through multiple buffer fragments.

        Parameters:
        :   - **buf** – Network buffer
            - **offset** – Starting offset to compare from
            - **data** – Data buffer for comparison
            - **len** – Number of bytes to compare

        Returns:
        :   The number of bytes compared before the first difference.

    static inline struct [net\_buf](#c.net_buf) \*net\_buf\_skip(struct [net\_buf](#c.net_buf) \*buf, size\_t len)
    :   Skip N number of bytes in a [net\_buf](#structnet__buf).

        Skip N number of bytes starting from fragment’s offset. If the total length of data is placed in multiple fragments, this function will skip from all fragments until it reaches N number of bytes. Any fully skipped buffers are removed from the [net\_buf](#structnet__buf) list.

        Parameters:
        :   - **buf** – Network buffer.
            - **len** – Total length of data to be skipped.

        Returns:
        :   Pointer to the fragment or NULL and pos is 0 after successful skip, NULL and pos is 0xffff otherwise.

    static inline size\_t net\_buf\_frags\_len(const struct [net\_buf](#c.net_buf) \*buf)
    :   Calculate amount of bytes stored in fragments.

        Calculates the total amount of data stored in the given buffer and the fragments linked to it.

        Parameters:
        :   - **buf** – Buffer to start off with.

        Returns:
        :   Number of bytes in the buffer and its fragments.

    struct net\_buf\_simple
    :   *#include <buf.h>*

        Simple network buffer representation.

        This is a simpler variant of the [net\_buf](#structnet__buf) object (in fact [net\_buf](#structnet__buf) uses [net\_buf\_simple](#structnet__buf__simple) internally). It doesn’t provide any kind of reference counting, user data, dynamic allocation, or in general the ability to pass through kernel objects such as FIFOs.

        The main use of this is for scenarios where the meta-data of the normal [net\_buf](#structnet__buf) isn’t needed and causes too much overhead. This could be e.g. when the buffer only needs to be allocated on the stack or when the access to and lifetime of the buffer is well controlled and constrained.

        Public Members

        uint8\_t \*data
        :   Pointer to the start of data in the buffer.

        uint16\_t len
        :   Length of the data behind the data pointer.

            To determine the max length, use [net\_buf\_simple\_max\_len()](#group__net__buf_1gabfe255688a80c0abea866762ff4c5a6c), not [size](#structnet__buf__simple_1ae6dc4aa029a67d3911293618eb30caa6)!

        uint16\_t size
        :   Amount of data that net\_buf\_simple::\_\_buf can store.

    struct net\_buf\_simple\_state
    :   *#include <buf.h>*

        Parsing state of a buffer.

        This is used for temporarily storing the parsing state of a buffer while giving control of the parsing to a routine which we don’t control.

        Public Members

        uint16\_t offset
        :   Offset of the data pointer from the beginning of the storage.

        uint16\_t len
        :   Length of data.

    struct net\_buf
    :   *#include <buf.h>*

        Network buffer representation.

        This struct is used to represent network buffers. Such buffers are normally defined through the NET\_BUF\_POOL\_\*\_DEFINE() APIs and allocated using the [net\_buf\_alloc()](#group__net__buf_1ga534366f3b5c7f41a28372c12149ca005) API.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Allow placing the buffer into [sys\_slist\_t](../../../kernel/data_structures/slist.md#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8).

        struct [net\_buf](#c.net_buf) \*frags
        :   Fragments associated with this buffer.

        uint8\_t ref
        :   Reference count.

        uint8\_t flags
        :   Bit-field of buffer flags.

        uint8\_t pool\_id
        :   Where the buffer should go when freed up.

        uint8\_t user\_data\_size
        :   Size of user data on this buffer.

        uint8\_t \*data
        :   Pointer to the start of data in the buffer.

        uint16\_t len
        :   Length of the data behind the data pointer.

        uint16\_t size
        :   Amount of data that this buffer can store.

        union [net\_buf](#c.net_buf).[anonymous] [anonymous]
        :   Union for convenience access to the [net\_buf\_simple](#structnet__buf__simple) members, also preserving the old API.

        uint8\_t user\_data[]
        :   System metadata for this buffer.

    struct net\_buf\_pool
    :   *#include <buf.h>*

        Network buffer pool representation.

        This struct is used to represent a pool of network buffers.

        Public Members

        struct k\_lifo free
        :   LIFO to place the buffer into when free.

        struct [k\_spinlock](../../../kernel/services/smp/smp.md#c.k_spinlock "k_spinlock") lock
        :   To prevent concurrent access/modifications.

        const uint16\_t buf\_count
        :   Number of buffers in pool.

        uint16\_t uninit\_count
        :   Number of uninitialized buffers.

        uint8\_t user\_data\_size
        :   Size of user data allocated to this pool.

        void (\*const destroy)(struct [net\_buf](#c.net_buf) \*buf)
        :   Optional destroy callback when buffer is freed.

        const struct net\_buf\_data\_alloc \*alloc
        :   Data allocation handlers.
