---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/net_buf/index.html
original_path: services/net_buf/index.html
---

# Network Buffers

## [Overview](#id1)

Network buffers are a core concept of how the networking stack
(as well as the Bluetooth stack) pass data around. The API for them is
defined in [include/zephyr/net\_buf.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net_buf.h):.

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
buffers, rather this is done implicitly as [`net_buf_alloc()`](../../doxygen/html/group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005) gets
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
objects. Use [`k_fifo_put()`](../../doxygen/html/group__fifo__apis.md#ga3addb10f86f19e245c23362433d5c913) and [`k_fifo_get()`](../../doxygen/html/group__fifo__apis.md#ga1e2c480e2124116af97e94e7b4435de6) to pass buffer
from one thread to another.

Special functions exist for dealing with buffers in single linked lists,
where the [`net_buf_slist_put()`](../../doxygen/html/group__net__buf.md#ga6d2dfc45e1e5acf21fe08359a4f92a18) and [`net_buf_slist_get()`](../../doxygen/html/group__net__buf.md#ga218d4a0c160c57a44946154478724cb3)
functions must be used instead of [`sys_slist_append()`](../../doxygen/html/group__single-linked-list__apis.md#ga829fd7b6f1944dc38e10685e861e62b5) and
[`sys_slist_get()`](../../doxygen/html/group__single-linked-list__apis.md#ga497d7e9069c08e25a03ebc212ef8bbb3).

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
acquired from a free buffers pool by calling [`net_buf_alloc()`](../../doxygen/html/group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005),
resulting in a buffer with reference count 1. The reference count can be
incremented with [`net_buf_ref()`](../../doxygen/html/group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f) or decremented with
[`net_buf_unref()`](../../doxygen/html/group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273). When the count drops to zero the buffer is
automatically placed back to the free buffers pool.

## [API Reference](#id5)

[Network Buffer Library](../../doxygen/html/group__net__buf.md)
