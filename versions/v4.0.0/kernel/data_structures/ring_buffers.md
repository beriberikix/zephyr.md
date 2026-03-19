---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/data_structures/ring_buffers.html
original_path: kernel/data_structures/ring_buffers.html
---

# Ring Buffers

A *ring buffer* is a circular buffer, whose contents are stored in
first-in-first-out order.

For circumstances where an application needs to implement asynchronous
“streaming” copying of data, Zephyr provides a `struct ring_buf`
abstraction to manage copies of such data in and out of a shared
buffer of memory.

Two content data modes are supported:

- **Byte mode**: raw bytes can be enqueued and dequeued.
- **Data item mode**: Multiple 32-bit word data items with metadata
  can be enqueued and dequeued from the ring buffer in
  chunks of up to 1020 bytes. Each data item also has two
  associated metadata values: a type identifier and a 16-bit
  integer value, both of which are application-specific.

While the underlying data structure is the same, it is not
legal to mix these two modes on a single ring buffer instance. A ring
buffer initialized with a byte count must be used only with the
“bytes” API, one initialized with a word count must use the “items”
calls.

## [Concepts](#id1)

Any number of ring buffers can be defined (limited only by available RAM). Each
ring buffer is referenced by its memory address.

A ring buffer has the following key properties:

- A **data buffer** of bytes or 32-bit words. The data buffer contains the raw
  bytes or 32-bit words that have been added to the ring buffer but not yet
  removed.
- A **data buffer size**, measured in bytes or 32-bit words. This governs
  the maximum amount of data (including possible metadata values) the ring
  buffer can hold.

A ring buffer must be initialized before it can be used. This sets its
data buffer to empty.

A `struct ring_buf` may be placed anywhere in user-accessible
memory, and must be initialized with [`ring_buf_init()`](../../doxygen/html/group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55) or
[`ring_buf_item_init()`](../../doxygen/html/group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d) before use. This must be provided a region
of user-controlled memory for use as the buffer itself. Note carefully that the units of the size of the
buffer passed change (either bytes or words) depending on how the ring
buffer will be used later. Macros for combining these steps in a
single static declaration exist for convenience.
[`RING_BUF_DECLARE`](../../doxygen/html/group__ring__buffer__apis.md#ga803e45abf48ee207fc0ab4028726a82b) will declare and statically initialize a ring
buffer with a specified byte count, where
[`RING_BUF_ITEM_DECLARE`](../../doxygen/html/group__ring__buffer__apis.md#ga2fc2f4515121ac6bbf6aebf3e029bb5d) will declare and statically
initialize a buffer with a given count of 32 bit words.
[`RING_BUF_ITEM_SIZEOF`](../../doxygen/html/group__ring__buffer__apis.md#ga60451a56ed9b742abfa8e75ca320b004) will compute the size in 32-bit words
corresponding to a type or an expression. Note: rounds up if the size is
not a multiple of 32 bits.

“Bytes” data may be copied into the ring buffer using
[`ring_buf_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3), passing a data pointer and byte count. These
bytes will be copied into the buffer in order, as many as will fit in
the allocated buffer. The total number of bytes copied (which may be
fewer than provided) will be returned. Likewise [`ring_buf_get()`](../../doxygen/html/group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)
will copy bytes out of the ring buffer in the order that they were
written, into a user-provided buffer, returning the number of bytes
that were transferred.

To avoid multiply-copied-data situations, a “claim” API exists for
byte mode. [`ring_buf_put_claim()`](../../doxygen/html/group__ring__buffer__apis.md#gae15934b40fd208a63eba98b2382e8ad1) takes a byte size value from the
user and returns a pointer to memory internal to the ring buffer that
can be used to receive those bytes, along with a size of the
contiguous internal region (which may be smaller than requested). The
user can then copy data into that region at a later time without
assembling all the bytes in a single region first. When complete,
[`ring_buf_put_finish()`](../../doxygen/html/group__ring__buffer__apis.md#ga465feaf6cf5312e75060ecf65db963ad) can be used to signal the buffer that the
transfer is complete, passing the number of bytes actually
transferred. At this point a new transfer can be initiated.
Similarly, [`ring_buf_get_claim()`](../../doxygen/html/group__ring__buffer__apis.md#ga7ab4fea7b19b1ffa58a7d3a581396b1c) returns a pointer to internal ring
buffer data from which the user can read without making a verbatim
copy, and [`ring_buf_get_finish()`](../../doxygen/html/group__ring__buffer__apis.md#ga36177459f4e352b52a6f2046a33c3aa1) signals the buffer with how many
bytes have been consumed and allows for a new transfer to begin.

“Items” mode works similarly to bytes mode, except that all transfers
are in units of 32 bit words and all memory is assumed to be aligned
on 32 bit boundaries. The write and read operations are
[`ring_buf_item_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599) and [`ring_buf_item_get()`](../../doxygen/html/group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8), and work
otherwise identically to the bytes mode APIs. There no “claim” API
provided for items mode. One important difference is that unlike
[`ring_buf_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3), [`ring_buf_item_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599) will not do a partial
transfer; it will return an error in the case where the provided data
does not fit in its entirety.

The user can manage the capacity of a ring buffer without modifying it
using either [`ring_buf_space_get()`](../../doxygen/html/group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb) or [`ring_buf_item_space_get()`](../../doxygen/html/group__ring__buffer__apis.md#gab58be76e8d3fc5542fb7b03717b89544)
which returns the number of free bytes or free 32-bit item words respectively,
or by testing the [`ring_buf_is_empty()`](../../doxygen/html/group__ring__buffer__apis.md#gabb7006d786b1ddc640b5fd2338d1d01c) predicate.

Finally, a [`ring_buf_reset()`](../../doxygen/html/group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18) call exists to immediately empty a
ring buffer, discarding the tracking of any bytes or items already
written to the buffer. It does not modify the memory contents of the
buffer itself, however.

### [Byte mode](#id2)

A **byte mode** ring buffer instance is declared using
[`RING_BUF_DECLARE()`](../../doxygen/html/group__ring__buffer__apis.md#ga803e45abf48ee207fc0ab4028726a82b) and accessed using:
[`ring_buf_put_claim()`](../../doxygen/html/group__ring__buffer__apis.md#gae15934b40fd208a63eba98b2382e8ad1), [`ring_buf_put_finish()`](../../doxygen/html/group__ring__buffer__apis.md#ga465feaf6cf5312e75060ecf65db963ad),
[`ring_buf_get_claim()`](../../doxygen/html/group__ring__buffer__apis.md#ga7ab4fea7b19b1ffa58a7d3a581396b1c), [`ring_buf_get_finish()`](../../doxygen/html/group__ring__buffer__apis.md#ga36177459f4e352b52a6f2046a33c3aa1),
[`ring_buf_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3) and [`ring_buf_get()`](../../doxygen/html/group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7).

Data can be copied into the ring buffer (see
[`ring_buf_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)) or ring buffer memory can be used
directly by the user. In the latter case, the operation is split into three stages:

1. allocating the buffer ([`ring_buf_put_claim()`](../../doxygen/html/group__ring__buffer__apis.md#gae15934b40fd208a63eba98b2382e8ad1)) when
   user requests the destination location where data can be written.
2. writing the data by the user (e.g. buffer written by DMA).
3. indicating the amount of data written to the provided buffer
   ([`ring_buf_put_finish()`](../../doxygen/html/group__ring__buffer__apis.md#ga465feaf6cf5312e75060ecf65db963ad)). The amount
   can be less than or equal to the allocated amount.

Data can be retrieved from a ring buffer through copying
(see [`ring_buf_get()`](../../doxygen/html/group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)) or accessed directly by address. In the latter
case, the operation is split into three stages:

1. retrieving source location with valid data written to a ring buffer
   (see [`ring_buf_get_claim()`](../../doxygen/html/group__ring__buffer__apis.md#ga7ab4fea7b19b1ffa58a7d3a581396b1c)).
2. processing data
3. freeing processed data (see [`ring_buf_get_finish()`](../../doxygen/html/group__ring__buffer__apis.md#ga36177459f4e352b52a6f2046a33c3aa1)).
   The amount freed can be less than or equal or to the retrieved amount.

### [Data item mode](#id3)

A **data item mode** ring buffer instance is declared using
[`RING_BUF_ITEM_DECLARE()`](../../doxygen/html/group__ring__buffer__apis.md#ga2fc2f4515121ac6bbf6aebf3e029bb5d) and accessed using
[`ring_buf_item_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599) and [`ring_buf_item_get()`](../../doxygen/html/group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8).

A ring buffer **data item** is an array of 32-bit words from 0 to 1020 bytes
in length. When a data item is **enqueued** ([`ring_buf_item_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599))
its contents are copied to the data buffer, along with its associated metadata
values (which occupy one additional 32-bit word). If the ring buffer has
insufficient space to hold the new data item the enqueue operation fails.

A data item is **dequeued** ([`ring_buf_item_get()`](../../doxygen/html/group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)) from a ring
buffer by removing the oldest enqueued item. The contents of the dequeued data
item, as well as its two metadata values, are copied to areas supplied by the
retriever. If the ring buffer is empty, or if the data array supplied by the
retriever is not large enough to hold the data item’s data, the dequeue
operation fails.

### [Concurrency](#id4)

The ring buffer APIs do not provide any concurrency control.
Depending on usage (particularly with respect to number of concurrent
readers/writers) applications may need to protect the ring buffer with
mutexes and/or use semaphores to notify consumers that there is data to
read.

For the trivial case of one producer and one consumer, concurrency
control shouldn’t be needed.

### [Internal Operation](#id5)

Data streamed through a ring buffer is always written to the next byte
within the buffer, wrapping around to the first element after reaching
the end, thus the “ring” structure. Internally, the `struct
ring_buf` contains its own buffer pointer and its size, and also a
set of “head” and “tail” indices representing where the next read and write
operations may occur.

This boundary is invisible to the user using the normal put/get APIs,
but becomes a barrier to the “claim” API, because obviously no
contiguous region can be returned that crosses the end of the buffer.
This can be surprising to application code, and produce performance
artifacts when transfers need to happen close to the end of the
buffer, as the number of calls to claim/finish needs to double for such
transfers.

## [Implementation](#id6)

### [Defining a Ring Buffer](#id7)

A ring buffer is defined using a variable of type [`ring_buf`](../../doxygen/html/structring__buf.md).
It must then be initialized by calling [`ring_buf_init()`](../../doxygen/html/group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55) or
[`ring_buf_item_init()`](../../doxygen/html/group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d).

The following code defines and initializes an empty **data item mode** ring
buffer (which is part of a larger data structure). The ring buffer’s data buffer
is capable of holding 64 words of data and metadata information.

```c
#define MY_RING_BUF_WORDS 64

struct my_struct {
    struct ring_buf rb;
    uint32_t buffer[MY_RING_BUF_WORDS];
    ...
};
struct my_struct ms;

void init_my_struct {
    ring_buf_item_init(&ms.rb, MY_RING_BUF_WORDS, ms.buffer);
    ...
}
```

Alternatively, a ring buffer can be defined and initialized at compile time
using one of two macros at file scope. Each macro defines both the ring
buffer itself and its data buffer.

The following code defines a **data item mode** ring buffer:

```c
#define MY_RING_BUF_WORDS 93
RING_BUF_ITEM_DECLARE(my_ring_buf, MY_RING_BUF_WORDS);
```

The following code defines a ring buffer intended to be used for raw bytes:

```c
#define MY_RING_BUF_BYTES 93
RING_BUF_DECLARE(my_ring_buf, MY_RING_BUF_BYTES);
```

### [Enqueuing Data](#id8)

Bytes are copied to a **byte mode** ring buffer by calling
[`ring_buf_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3).

```c
uint8_t my_data[MY_RING_BUF_BYTES];
uint32_t ret;

ret = ring_buf_put(&ring_buf, my_data, MY_RING_BUF_BYTES);
if (ret != MY_RING_BUF_BYTES) {
    /* not enough room, partial copy. */
    ...
}
```

Data can be added to a **byte mode** ring buffer by directly accessing the
ring buffer’s memory. For example:

```c
uint32_t size;
uint32_t rx_size;
uint8_t *data;
int err;

/* Allocate buffer within a ring buffer memory. */
size = ring_buf_put_claim(&ring_buf, &data, MY_RING_BUF_BYTES);

/* Work directly on a ring buffer memory. */
rx_size = uart_rx(data, size);

/* Indicate amount of valid data. rx_size can be equal or less than size. */
err = ring_buf_put_finish(&ring_buf, rx_size);
if (err != 0) {
    /* This shouldn't happen unless rx_size > size */
    ...
}
```

A data item is added to a ring buffer by calling
[`ring_buf_item_put()`](../../doxygen/html/group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599).

```c
uint32_t data[MY_DATA_WORDS];
int ret;

ret = ring_buf_item_put(&ring_buf, TYPE_FOO, 0, data, MY_DATA_WORDS);
if (ret == -EMSGSIZE) {
    /* not enough room for the data item */
    ...
}
```

If the data item requires only the type or application-specific integer value
(i.e. it has no data array), a size of 0 and data pointer of `NULL`
can be specified.

```c
int ret;

ret = ring_buf_item_put(&ring_buf, TYPE_BAR, 17, NULL, 0);
if (ret == -EMSGSIZE) {
    /* not enough room for the data item */
    ...
}
```

### [Retrieving Data](#id9)

Data bytes are copied out from a **byte mode** ring buffer by calling
[`ring_buf_get()`](../../doxygen/html/group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7). For example:

```c
uint8_t my_data[MY_DATA_BYTES];
size_t  ret;

ret = ring_buf_get(&ring_buf, my_data, sizeof(my_data));
if (ret != sizeof(my_data)) {
    /* Fewer bytes copied. */
} else {
    /* Requested amount of bytes retrieved. */
    ...
}
```

Data can be retrieved from a **byte mode** ring buffer by direct
operations on the ring buffer’s memory. For example:

```c
uint32_t size;
uint32_t proc_size;
uint8_t *data;
int err;

/* Get buffer within a ring buffer memory. */
size = ring_buf_get_claim(&ring_buf, &data, MY_RING_BUF_BYTES);

/* Work directly on a ring buffer memory. */
proc_size = process(data, size);

/* Indicate amount of data that can be freed. proc_size can be equal or less
 * than size.
 */
err = ring_buf_get_finish(&ring_buf, proc_size);
if (err != 0) {
    /* proc_size exceeds amount of valid data in a ring buffer. */
    ...
}
```

A data item is removed from a ring buffer by calling
[`ring_buf_item_get()`](../../doxygen/html/group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8).

```c
uint32_t my_data[MY_DATA_WORDS];
uint16_t my_type;
uint8_t  my_value;
uint8_t  my_size;
int ret;

my_size = MY_DATA_WORDS;
ret = ring_buf_item_get(&ring_buf, &my_type, &my_value, my_data, &my_size);
if (ret == -EMSGSIZE) {
    printk("Buffer is too small, need %d uint32_t\n", my_size);
} else if (ret == -EAGAIN) {
    printk("Ring buffer is empty\n");
} else {
    printk("Got item of type %u value &u of size %u dwords\n",
           my_type, my_value, my_size);
    ...
}
```

## [Configuration Options](#id10)

Related configuration options:

- [`CONFIG_RING_BUFFER`](../../kconfig.md#CONFIG_RING_BUFFER "CONFIG_RING_BUFFER"): Enable ring buffer.

## [API Reference](#id11)

The following ring buffer APIs are provided by [include/zephyr/sys/ring\_buffer.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/ring_buffer.h):

[Ring Buffer APIs](../../doxygen/html/group__ring__buffer__apis.md)
