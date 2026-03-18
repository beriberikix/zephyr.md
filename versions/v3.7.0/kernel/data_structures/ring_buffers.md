---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/data_structures/ring_buffers.html
original_path: kernel/data_structures/ring_buffers.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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
memory, and must be initialized with [`ring_buf_init()`](#c.ring_buf_init) or
[`ring_buf_item_init()`](#c.ring_buf_item_init) before use. This must be provided a region
of user-controlled memory for use as the buffer itself. Note carefully that the units of the size of the
buffer passed change (either bytes or words) depending on how the ring
buffer will be used later. Macros for combining these steps in a
single static declaration exist for convenience.
[`RING_BUF_DECLARE`](#c.RING_BUF_DECLARE) will declare and statically initialize a ring
buffer with a specified byte count, where
[`RING_BUF_ITEM_DECLARE`](#c.RING_BUF_ITEM_DECLARE) will declare and statically
initialize a buffer with a given count of 32 bit words.
[`RING_BUF_ITEM_SIZEOF`](#c.RING_BUF_ITEM_SIZEOF) will compute the size in 32-bit words
corresponding to a type or an expression. Note: rounds up if the size is
not a multiple of 32 bits.

“Bytes” data may be copied into the ring buffer using
[`ring_buf_put()`](#c.ring_buf_put), passing a data pointer and byte count. These
bytes will be copied into the buffer in order, as many as will fit in
the allocated buffer. The total number of bytes copied (which may be
fewer than provided) will be returned. Likewise [`ring_buf_get()`](#c.ring_buf_get)
will copy bytes out of the ring buffer in the order that they were
written, into a user-provided buffer, returning the number of bytes
that were transferred.

To avoid multiply-copied-data situations, a “claim” API exists for
byte mode. [`ring_buf_put_claim()`](#c.ring_buf_put_claim) takes a byte size value from the
user and returns a pointer to memory internal to the ring buffer that
can be used to receive those bytes, along with a size of the
contiguous internal region (which may be smaller than requested). The
user can then copy data into that region at a later time without
assembling all the bytes in a single region first. When complete,
[`ring_buf_put_finish()`](#c.ring_buf_put_finish) can be used to signal the buffer that the
transfer is complete, passing the number of bytes actually
transferred. At this point a new transfer can be initiated.
Similarly, [`ring_buf_get_claim()`](#c.ring_buf_get_claim) returns a pointer to internal ring
buffer data from which the user can read without making a verbatim
copy, and [`ring_buf_get_finish()`](#c.ring_buf_get_finish) signals the buffer with how many
bytes have been consumed and allows for a new transfer to begin.

“Items” mode works similarly to bytes mode, except that all transfers
are in units of 32 bit words and all memory is assumed to be aligned
on 32 bit boundaries. The write and read operations are
[`ring_buf_item_put()`](#c.ring_buf_item_put) and [`ring_buf_item_get()`](#c.ring_buf_item_get), and work
otherwise identically to the bytes mode APIs. There no “claim” API
provided for items mode. One important difference is that unlike
[`ring_buf_put()`](#c.ring_buf_put), [`ring_buf_item_put()`](#c.ring_buf_item_put) will not do a partial
transfer; it will return an error in the case where the provided data
does not fit in its entirety.

The user can manage the capacity of a ring buffer without modifying it
using either [`ring_buf_space_get()`](#c.ring_buf_space_get) or [`ring_buf_item_space_get()`](#c.ring_buf_item_space_get)
which returns the number of free bytes or free 32-bit item words respectively,
or by testing the [`ring_buf_is_empty()`](#c.ring_buf_is_empty) predicate.

Finally, a [`ring_buf_reset()`](#c.ring_buf_reset) call exists to immediately empty a
ring buffer, discarding the tracking of any bytes or items already
written to the buffer. It does not modify the memory contents of the
buffer itself, however.

### [Byte mode](#id2)

A **byte mode** ring buffer instance is declared using
[`RING_BUF_DECLARE()`](#c.RING_BUF_DECLARE) and accessed using:
[`ring_buf_put_claim()`](#c.ring_buf_put_claim), [`ring_buf_put_finish()`](#c.ring_buf_put_finish),
[`ring_buf_get_claim()`](#c.ring_buf_get_claim), [`ring_buf_get_finish()`](#c.ring_buf_get_finish),
[`ring_buf_put()`](#c.ring_buf_put) and [`ring_buf_get()`](#c.ring_buf_get).

Data can be copied into the ring buffer (see
[`ring_buf_put()`](#c.ring_buf_put)) or ring buffer memory can be used
directly by the user. In the latter case, the operation is split into three stages:

1. allocating the buffer ([`ring_buf_put_claim()`](#c.ring_buf_put_claim)) when
   user requests the destination location where data can be written.
2. writing the data by the user (e.g. buffer written by DMA).
3. indicating the amount of data written to the provided buffer
   ([`ring_buf_put_finish()`](#c.ring_buf_put_finish)). The amount
   can be less than or equal to the allocated amount.

Data can be retrieved from a ring buffer through copying
(see [`ring_buf_get()`](#c.ring_buf_get)) or accessed directly by address. In the latter
case, the operation is split into three stages:

1. retrieving source location with valid data written to a ring buffer
   (see [`ring_buf_get_claim()`](#c.ring_buf_get_claim)).
2. processing data
3. freeing processed data (see [`ring_buf_get_finish()`](#c.ring_buf_get_finish)).
   The amount freed can be less than or equal or to the retrieved amount.

### [Data item mode](#id3)

A **data item mode** ring buffer instance is declared using
[`RING_BUF_ITEM_DECLARE()`](#c.RING_BUF_ITEM_DECLARE) and accessed using
[`ring_buf_item_put()`](#c.ring_buf_item_put) and [`ring_buf_item_get()`](#c.ring_buf_item_get).

A ring buffer **data item** is an array of 32-bit words from 0 to 1020 bytes
in length. When a data item is **enqueued** ([`ring_buf_item_put()`](#c.ring_buf_item_put))
its contents are copied to the data buffer, along with its associated metadata
values (which occupy one additional 32-bit word). If the ring buffer has
insufficient space to hold the new data item the enqueue operation fails.

A data item is **dequeued** ([`ring_buf_item_get()`](#c.ring_buf_item_get)) from a ring
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

A ring buffer is defined using a variable of type [`ring_buf`](#c.ring_buf).
It must then be initialized by calling [`ring_buf_init()`](#c.ring_buf_init) or
[`ring_buf_item_init()`](#c.ring_buf_item_init).

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
[`ring_buf_put()`](#c.ring_buf_put).

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
[`ring_buf_item_put()`](#c.ring_buf_item_put).

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
[`ring_buf_get()`](#c.ring_buf_get). For example:

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
[`ring_buf_item_get()`](#c.ring_buf_item_get).

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

*group* Ring Buffer APIs
:   Simple ring buffer implementation.

    Defines

    RING\_BUF\_DECLARE(name, size8)
    :   Define and initialize a ring buffer for byte data.

        This macro establishes a ring buffer of an arbitrary size. The basic storage unit is a byte.

        The ring buffer can be accessed outside the module where it is defined using:

        ```text
        extern struct ring_buf <name>;
        ```

        Parameters:
        :   - **name** – Name of the ring buffer.
            - **size8** – Size of ring buffer (in bytes).

    RING\_BUF\_ITEM\_DECLARE(name, size32)
    :   Define and initialize an “item based” ring buffer.

        This macro establishes an “item based” ring buffer. Each data item is an array of 32-bit words (from zero to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

        The ring buffer can be accessed outside the module where it is defined using:

        ```text
        extern struct ring_buf <name>;
        ```

        Parameters:
        :   - **name** – Name of the ring buffer.
            - **size32** – Size of ring buffer (in 32-bit words).

    RING\_BUF\_ITEM\_DECLARE\_SIZE(name, size32)
    :   Define and initialize an “item based” ring buffer.

        This exists for backward compatibility reasons. [RING\_BUF\_ITEM\_DECLARE](#group__ring__buffer__apis_1ga2fc2f4515121ac6bbf6aebf3e029bb5d) should be used instead.

        Parameters:
        :   - **name** – Name of the ring buffer.
            - **size32** – Size of ring buffer (in 32-bit words).

    RING\_BUF\_ITEM\_DECLARE\_POW2(name, pow)
    :   Define and initialize a power-of-2 sized “item based” ring buffer.

        This macro establishes an “item based” ring buffer by specifying its size using a power of 2. This exists mainly for backward compatibility reasons. [RING\_BUF\_ITEM\_DECLARE](#group__ring__buffer__apis_1ga2fc2f4515121ac6bbf6aebf3e029bb5d) should be used instead.

        Parameters:
        :   - **name** – Name of the ring buffer.
            - **pow** – Ring buffer size exponent.

    RING\_BUF\_ITEM\_SIZEOF(expr)
    :   Compute the ring buffer size in 32-bit needed to store an element.

        The argument can be a type or an expression. Note: rounds up if the size is not a multiple of 32 bits.

        Parameters:
        :   - **expr** – Expression or type to compute the size of

    Functions

    static inline void ring\_buf\_internal\_reset(struct [ring\_buf](#c.ring_buf) \*buf, int32\_t value)
    :   Function to force [ring\_buf](#structring__buf) internal states to given value.

        Any value other than 0 makes sense only in validation testing context.

    static inline void ring\_buf\_init(struct [ring\_buf](#c.ring_buf) \*buf, uint32\_t size, uint8\_t \*data)
    :   Initialize a ring buffer for byte data.

        This routine initializes a ring buffer, prior to its first use. It is only used for ring buffers not defined using RING\_BUF\_DECLARE.

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **size** – Ring buffer size (in bytes).
            - **data** – Ring buffer data area (uint8\_t data[size]).

    static inline void ring\_buf\_item\_init(struct [ring\_buf](#c.ring_buf) \*buf, uint32\_t size, uint32\_t \*data)
    :   Initialize an “item based” ring buffer.

        This routine initializes a ring buffer, prior to its first use. It is only used for ring buffers not defined using RING\_BUF\_ITEM\_DECLARE.

        Each data item is an array of 32-bit words (from zero to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

        Each data item is an array of 32-bit words (from zero to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **size** – Ring buffer size (in 32-bit words)
            - **data** – Ring buffer data area (uint32\_t data[size]).

    static inline bool ring\_buf\_is\_empty(struct [ring\_buf](#c.ring_buf) \*buf)
    :   Determine if a ring buffer is empty.

        Parameters:
        :   - **buf** – Address of ring buffer.

        Returns:
        :   true if the ring buffer is empty, or false if not.

    static inline void ring\_buf\_reset(struct [ring\_buf](#c.ring_buf) \*buf)
    :   Reset ring buffer state.

        Parameters:
        :   - **buf** – Address of ring buffer.

    static inline uint32\_t ring\_buf\_space\_get(struct [ring\_buf](#c.ring_buf) \*buf)
    :   Determine free space in a ring buffer.

        Parameters:
        :   - **buf** – Address of ring buffer.

        Returns:
        :   Ring buffer free space (in bytes).

    static inline uint32\_t ring\_buf\_item\_space\_get(struct [ring\_buf](#c.ring_buf) \*buf)
    :   Determine free space in an “item based” ring buffer.

        Parameters:
        :   - **buf** – Address of ring buffer.

        Returns:
        :   Ring buffer free space (in 32-bit words).

    static inline uint32\_t ring\_buf\_capacity\_get(struct [ring\_buf](#c.ring_buf) \*buf)
    :   Return ring buffer capacity.

        Parameters:
        :   - **buf** – Address of ring buffer.

        Returns:
        :   Ring buffer capacity (in bytes).

    static inline uint32\_t ring\_buf\_size\_get(struct [ring\_buf](#c.ring_buf) \*buf)
    :   Determine used space in a ring buffer.

        Parameters:
        :   - **buf** – Address of ring buffer.

        Returns:
        :   Ring buffer space used (in bytes).

    uint32\_t ring\_buf\_put\_claim(struct [ring\_buf](#c.ring_buf) \*buf, uint8\_t \*\*data, uint32\_t size)
    :   Allocate buffer for writing data to a ring buffer.

        With this routine, memory copying can be reduced since internal ring buffer can be used directly by the user. Once data is written to allocated area number of bytes written must be confirmed (see [ring\_buf\_put\_finish](#group__ring__buffer__apis_1ga465feaf6cf5312e75060ecf65db963ad)).

        Warning

        Use cases involving multiple writers to the ring buffer must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the ring buffer.

        Warning

        Ring buffer instance should not mix byte access and item access (calls prefixed with ring\_buf\_item\_).

        Parameters:
        :   - **buf** – **[in]** Address of ring buffer.
            - **data** – **[out]** Pointer to the address. It is set to a location within ring buffer.
            - **size** – **[in]** Requested allocation size (in bytes).

        Returns:
        :   Size of allocated buffer which can be smaller than requested if there is not enough free space or buffer wraps.

    int ring\_buf\_put\_finish(struct [ring\_buf](#c.ring_buf) \*buf, uint32\_t size)
    :   Indicate number of bytes written to allocated buffers.

        The number of bytes must be equal to or lower than the sum corresponding to all preceding [ring\_buf\_put\_claim](#group__ring__buffer__apis_1gae15934b40fd208a63eba98b2382e8ad1) invocations (or even 0). Surplus bytes will be returned to the available free buffer space.

        Warning

        Use cases involving multiple writers to the ring buffer must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the ring buffer.

        Warning

        Ring buffer instance should not mix byte access and item access (calls prefixed with ring\_buf\_item\_).

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **size** – Number of valid bytes in the allocated buffers.

        Return values:
        :   - **0** – Successful operation.
            - **-EINVAL** – Provided *size* exceeds free space in the ring buffer.

    uint32\_t ring\_buf\_put(struct [ring\_buf](#c.ring_buf) \*buf, const uint8\_t \*data, uint32\_t size)
    :   Write (copy) data to a ring buffer.

        This routine writes data to a ring buffer *buf*.

        Warning

        Use cases involving multiple writers to the ring buffer must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the ring buffer.

        Warning

        Ring buffer instance should not mix byte access and item access (calls prefixed with ring\_buf\_item\_).

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **data** – Address of data.
            - **size** – Data size (in bytes).

        Return values:
        :   **Number** – of bytes written.

    uint32\_t ring\_buf\_get\_claim(struct [ring\_buf](#c.ring_buf) \*buf, uint8\_t \*\*data, uint32\_t size)
    :   Get address of a valid data in a ring buffer.

        With this routine, memory copying can be reduced since internal ring buffer can be used directly by the user. Once data is processed it must be freed using [ring\_buf\_get\_finish](#group__ring__buffer__apis_1ga36177459f4e352b52a6f2046a33c3aa1).

        Warning

        Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.

        Warning

        Ring buffer instance should not mix byte access and item access (calls prefixed with ring\_buf\_item\_).

        Parameters:
        :   - **buf** – **[in]** Address of ring buffer.
            - **data** – **[out]** Pointer to the address. It is set to a location within ring buffer.
            - **size** – **[in]** Requested size (in bytes).

        Returns:
        :   Number of valid bytes in the provided buffer which can be smaller than requested if there is not enough free space or buffer wraps.

    int ring\_buf\_get\_finish(struct [ring\_buf](#c.ring_buf) \*buf, uint32\_t size)
    :   Indicate number of bytes read from claimed buffer.

        The number of bytes must be equal or lower than the sum corresponding to all preceding [ring\_buf\_get\_claim](#group__ring__buffer__apis_1ga7ab4fea7b19b1ffa58a7d3a581396b1c) invocations (or even 0). Surplus bytes will remain available in the buffer.

        Warning

        Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.

        Warning

        Ring buffer instance should not mix byte access and item mode (calls prefixed with ring\_buf\_item\_).

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **size** – Number of bytes that can be freed.

        Return values:
        :   - **0** – Successful operation.
            - **-EINVAL** – Provided *size* exceeds valid bytes in the ring buffer.

    uint32\_t ring\_buf\_get(struct [ring\_buf](#c.ring_buf) \*buf, uint8\_t \*data, uint32\_t size)
    :   Read data from a ring buffer.

        This routine reads data from a ring buffer *buf*.

        Warning

        Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.

        Warning

        Ring buffer instance should not mix byte access and item mode (calls prefixed with ring\_buf\_item\_).

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **data** – Address of the output buffer. Can be NULL to discard data.
            - **size** – Data size (in bytes).

        Return values:
        :   **Number** – of bytes written to the output buffer.

    uint32\_t ring\_buf\_peek(struct [ring\_buf](#c.ring_buf) \*buf, uint8\_t \*data, uint32\_t size)
    :   Peek at data from a ring buffer.

        This routine reads data from a ring buffer *buf* without removal.

        Warning

        Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.

        Warning

        Ring buffer instance should not mix byte access and item mode (calls prefixed with ring\_buf\_item\_).

        Warning

        Multiple calls to peek will result in the same data being ‘peeked’ multiple times. To remove data, use either [ring\_buf\_get](#group__ring__buffer__apis_1ga209bef22c47f3938a36d7eb6c3b3dbc7) or [ring\_buf\_get\_claim](#group__ring__buffer__apis_1ga7ab4fea7b19b1ffa58a7d3a581396b1c) followed by [ring\_buf\_get\_finish](#group__ring__buffer__apis_1ga36177459f4e352b52a6f2046a33c3aa1) with a non-zero `size`.

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **data** – Address of the output buffer. Cannot be NULL.
            - **size** – Data size (in bytes).

        Return values:
        :   **Number** – of bytes written to the output buffer.

    int ring\_buf\_item\_put(struct [ring\_buf](#c.ring_buf) \*buf, uint16\_t type, uint8\_t value, uint32\_t \*data, uint8\_t size32)
    :   Write a data item to a ring buffer.

        This routine writes a data item to ring buffer *buf*. The data item is an array of 32-bit words (from zero to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

        Warning

        Use cases involving multiple writers to the ring buffer must prevent concurrent write operations, either by preventing all writers from being preempted or by using a mutex to govern writes to the ring buffer.

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **type** – Data item’s type identifier (application specific).
            - **value** – Data item’s integer value (application specific).
            - **data** – Address of data item.
            - **size32** – Data item size (number of 32-bit words).

        Return values:
        :   - **0** – Data item was written.
            - **-EMSGSIZE** – Ring buffer has insufficient free space.

    int ring\_buf\_item\_get(struct [ring\_buf](#c.ring_buf) \*buf, uint16\_t \*type, uint8\_t \*value, uint32\_t \*data, uint8\_t \*size32)
    :   Read a data item from a ring buffer.

        This routine reads a data item from ring buffer *buf*. The data item is an array of 32-bit words (up to 1020 bytes in length), coupled with a 16-bit type identifier and an 8-bit integer value.

        Warning

        Use cases involving multiple reads of the ring buffer must prevent concurrent read operations, either by preventing all readers from being preempted or by using a mutex to govern reads to the ring buffer.

        Parameters:
        :   - **buf** – Address of ring buffer.
            - **type** – Area to store the data item’s type identifier.
            - **value** – Area to store the data item’s integer value.
            - **data** – Area to store the data item. Can be NULL to discard data.
            - **size32** – Size of the data item storage area (number of 32-bit chunks).

        Return values:
        :   - **0** – Data item was fetched; *size32* now contains the number of 32-bit words read into data area *data*.
            - **-EAGAIN** – Ring buffer is empty.
            - **-EMSGSIZE** – Data area *data* is too small; *size32* now contains the number of 32-bit words needed.

    struct ring\_buf
    :   *#include <ring\_buffer.h>*

        A structure to represent a ring buffer.
