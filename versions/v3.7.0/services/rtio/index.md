---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/rtio/index.html
original_path: services/rtio/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Real Time I/O (RTIO)

[![Submissions and Completion Ring Queues](../../_images/rings.png)](../../_images/rings.png)

RTIO provides a framework for doing asynchronous operation chains with event
driven I/O. This section covers the RTIO API, queues, executor, iodev,
and common usage patterns with peripheral devices.

RTIO takes a lot of inspiration from Linux’s io\_uring in its operations and API
as that API matches up well with hardware transfer queues and descriptions such as
DMA transfer lists.

## [Problem](#id1)

An application wishing to do complex DMA or interrupt driven operations today
in Zephyr requires direct knowledge of the hardware and how it works. There is
no understanding in the DMA API of other Zephyr devices and how they relate.

This means doing complex audio, video, or sensor streaming requires direct
hardware knowledge or leaky abstractions over DMA controllers. Neither is ideal.

To enable asynchronous operations, especially with DMA, a description of what
to do rather than direct operations through C and callbacks is needed. Enabling
DMA features such as channels with priority, and sequences of transfers requires
more than a simple list of descriptions.

Using DMA and/or interrupt driven I/O shouldn’t dictate whether or not the
call is blocking or not.

## [Inspiration, introducing io\_uring](#id2)

It’s better not to reinvent the wheel (or ring in this case) and io\_uring as an
API from the Linux kernel provides a winning model. In io\_uring there are two
lock-free ring buffers acting as queues shared between the kernel and a userland
application. One queue for submission entries which may be chained and flushed to
create concurrent sequential requests. A second queue for completion queue events.
Only a single syscall is actually required to execute many operations, the
io\_uring\_submit call. This call may block the caller when a number of
operations to wait on is given.

This model maps well to DMA and interrupt driven transfers. A request to do a
sequence of operations in an asynchronous way directly relates
to the way hardware typically works with interrupt driven state machines
potentially involving multiple peripheral IPs like bus and DMA controllers.

## [Submission Queue](#id3)

The submission queue (sq), is the description of the operations
to perform in concurrent chains.

For example imagine a typical SPI transfer where you wish to write a
register address to then read from. So the sequence of operations might be…

> 1. Chip Select
> 2. Clock Enable
> 3. Write register address into SPI transmit register
> 4. Read from the SPI receive register into a buffer
> 5. Disable clock
> 6. Disable Chip Select

If anything in this chain of operations fails give up. Some of those operations
can be embodied in a device abstraction that understands a read or write
implicitly means setup the clock and chip select. The transactional nature of
the request also needs to be embodied in some manner. Of the operations above
perhaps the read could be done using DMA as its large enough make sense. That
requires an understanding of how to setup the device’s particular DMA to do so.

The above sequence of operations is embodied in RTIO as chain of
submission queue entries (sqe). Chaining is done by setting a bitflag in
an sqe to signify the next sqe must wait on the current one.

Because the chip select and clocking is common to a particular SPI controller
and device on the bus it is embodied in what RTIO calls an iodev.

Multiple operations against the same iodev are done in the order provided as
soon as possible. If two operation chains have varying points using the same
device its possible one chain will have to wait for another to complete.

## [Completion Queue](#id4)

In order to know when a sqe has completed there is a completion
queue (cq) with completion queue events (cqe). A sqe once completed results in
a cqe being pushed into the cq. The ordering of cqe may not be the same order of
sqe. A chain of sqe will however ensure ordering and failure cascading.

Other potential schemes are possible but a completion queue is a well trod
idea with io\_uring and other similar operating system APIs.

## [Executor](#id5)

The RTIO executor is a low overhead concurrent I/O task scheduler. It ensures
certain request flags provide the expected behavior. It takes a list of
submissions working through them in order. Various flags allow for changing the
behavior of how submissions are worked through. Flags to form in order chains of
submissions, transactional sets of submissions, or create multi-shot
(continuously producing) requests are all possible!

## [IO Device](#id6)

Turning submission queue entries (sqe) into completion queue events (cqe) is the
job of objects implementing the iodev (IO device) API. This API accepts requests
in the form of the iodev submit API call. It is the io devices job to work
through its internal queue of submissions and convert them into completions. In
effect every io device can be viewed as an independent, event driven actor like
object, that accepts a never ending queue of I/O like requests. How the iodev
does this work is up to the author of the iodev, perhaps the entire queue of
operations can be converted to a set of DMA transfer descriptors, meaning the
hardware does almost all of the real work.

## [Cancellation](#id7)

Canceling an already queued operation is possible but not guaranteed. If the
SQE has not yet started, it’s likely that a call to [`rtio_sqe_cancel()`](#c.rtio_sqe_cancel)
will remove the SQE and never run it. If, however, the SQE already started
running, the cancel request will be ignored.

## [Memory pools](#id8)

In some cases requests to read may not know how much data will be produced.
Alternatively, a reader might be handling data from multiple io devices where
the frequency of the data is unpredictable. In these cases it may be wasteful
to bind memory to in flight read requests. Instead with memory pools the memory
to read into is left to the iodev to allocate from a memory pool associated with
the RTIO context that the read was associated with. To create such an RTIO
context the [`RTIO_DEFINE_WITH_MEMPOOL`](#c.RTIO_DEFINE_WITH_MEMPOOL) can be used. It allows creating
an RTIO context with a dedicated pool of “memory blocks” which can be consumed by
the iodev. Below is a snippet setting up the RTIO context with a memory pool.
The memory pool has 128 blocks, each block has the size of 16 bytes, and the data
is 4 byte aligned.

```c
#include <zephyr/rtio/rtio.h>

#define SQ_SIZE       4
#define CQ_SIZE       4
#define MEM_BLK_COUNT 128
#define MEM_BLK_SIZE  16
#define MEM_BLK_ALIGN 4

RTIO_DEFINE_WITH_MEMPOOL(rtio_context,
    SQ_SIZE, CQ_SIZE, MEM_BLK_COUNT, MEM_BLK_SIZE, MEM_BLK_ALIGN);
```

When a read is needed, the caller simply needs to replace the call
[`rtio_sqe_prep_read()`](#c.rtio_sqe_prep_read) (which takes a pointer to a buffer and a length)
with a call to [`rtio_sqe_prep_read_with_pool()`](#c.rtio_sqe_prep_read_with_pool). The iodev requires
only a small change which works with both pre-allocated data buffers as well as
the mempool. When the read is ready, instead of getting the buffers directly
from the [`rtio_iodev_sqe`](#c.rtio_iodev_sqe), the iodev should get the buffer and count
by calling [`rtio_sqe_rx_buf()`](#c.rtio_sqe_rx_buf) like so:

```c
uint8_t *buf;
uint32_t buf_len;
int rc = rtio_sqe_rx_buff(iodev_sqe, MIN_BUF_LEN, DESIRED_BUF_LEN, &buf, &buf_len);

if (rc != 0) {
  LOG_ERR("Failed to get buffer of at least %u bytes", MIN_BUF_LEN);
  return;
}
```

Finally, the consumer will be able to access the allocated buffer via
[`rtio_cqe_get_mempool_buffer()`](#c.rtio_cqe_get_mempool_buffer).

```c
uint8_t *buf;
uint32_t buf_len;
int rc = rtio_cqe_get_mempool_buffer(&rtio_context, &cqe, &buf, &buf_len);

if (rc != 0) {
  LOG_ERR("Failed to get mempool buffer");
  return rc;
}

/* Release the cqe events (note that the buffer is not released yet */
rtio_cqe_release_all(&rtio_context);

/* Do something with the memory */

/* Release the mempool buffer */
rtio_release_buffer(&rtio_context, buf);
```

## [When to Use](#id9)

RTIO is useful in cases where concurrent or batch like I/O flows are useful.

From the driver/hardware perspective the API enables batching of I/O requests, potentially in an optimal way.
Many requests to the same SPI peripheral for example might be translated to hardware command queues or DMA transfer
descriptors entirely. Meaning the hardware can potentially do more than ever.

There is a small cost to each RTIO context and iodev. This cost could be weighed
against using a thread for each concurrent I/O operation or custom queues and
threads per peripheral. RTIO is much lower cost than that.

## [API Reference](#id10)

*group* RTIO
:   RTIO.

    **Since**
    :   3.2

    **Version**
    :   0.1.0

    Defines

    RTIO\_IODEV\_I2C\_STOP
    :   Equivalent to the I2C\_MSG\_STOP flag.

    RTIO\_IODEV\_I2C\_RESTART
    :   Equivalent to the I2C\_MSG\_RESTART flag.

    RTIO\_IODEV\_I2C\_10\_BITS
    :   Equivalent to the I2C\_MSG\_ADDR\_10\_BITS.

    RTIO\_OP\_NOP
    :   An operation that does nothing and will complete immediately.

    RTIO\_OP\_RX
    :   An operation that receives (reads).

    RTIO\_OP\_TX
    :   An operation that transmits (writes).

    RTIO\_OP\_TINY\_TX
    :   An operation that transmits tiny writes by copying the data to write.

    RTIO\_OP\_CALLBACK
    :   An operation that calls a given function (callback).

    RTIO\_OP\_TXRX
    :   An operation that transceives (reads and writes simultaneously).

    RTIO\_OP\_I2C\_RECOVER
    :   An operation to recover I2C buses.

    RTIO\_OP\_I2C\_CONFIGURE
    :   An operation to configure I2C buses.

    RTIO\_IODEV\_DEFINE(name, iodev\_api, iodev\_data)
    :   Statically define and initialize an RTIO IODev.

        Parameters:
        :   - **name** – Name of the iodev
            - **iodev\_api** – Pointer to struct [rtio\_iodev\_api](#structrtio__iodev__api)
            - **iodev\_data** – Data pointer

    RTIO\_BMEM
    :   Allocate to bss if available.

        If CONFIG\_USERSPACE is selected, allocate to the rtio\_partition bss. Maps to: K\_APP\_BMEM(rtio\_partition) static

        If CONFIG\_USERSPACE is disabled, allocate as plain static: static

    RTIO\_DMEM
    :   Allocate as initialized memory if available.

        If CONFIG\_USERSPACE is selected, allocate to the rtio\_partition init. Maps to: K\_APP\_DMEM(rtio\_partition) static

        If CONFIG\_USERSPACE is disabled, allocate as plain static: static

    RTIO\_DEFINE(name, sq\_sz, cq\_sz)
    :   Statically define and initialize an RTIO context.

        Parameters:
        :   - **name** – Name of the RTIO
            - **sq\_sz** – Size of the submission queue entry pool
            - **cq\_sz** – Size of the completion queue entry pool

    RTIO\_DEFINE\_WITH\_MEMPOOL(name, sq\_sz, cq\_sz, num\_blks, blk\_size, balign)
    :   Statically define and initialize an RTIO context.

        Parameters:
        :   - **name** – Name of the RTIO
            - **sq\_sz** – Size of the submission queue, must be power of 2
            - **cq\_sz** – Size of the completion queue, must be power of 2
            - **num\_blks** – Number of blocks in the memory pool
            - **blk\_size** – The number of bytes in each block
            - **balign** – The block alignment

    Typedefs

    typedef void (\*rtio\_callback\_t)(struct [rtio](#c.rtio) \*r, const struct [rtio\_sqe](#c.rtio_sqe) \*sqe, void \*arg0)
    :   Callback signature for RTIO\_OP\_CALLBACK.

        Param r:
        :   RTIO context being used with the callback

        Param sqe:
        :   Submission for the callback op

        Param arg0:
        :   Argument option as part of the sqe

    Functions

    static inline size\_t rtio\_mempool\_block\_size(const struct [rtio](#c.rtio) \*r)
    :   Get the mempool block size of the RTIO context.

        Parameters:
        :   - **r** – The RTIO context

        Returns:
        :   The size of each block in the context’s mempool

        Returns:
        :   0 if the context doesn’t have a mempool

    static inline void rtio\_sqe\_prep\_nop(struct [rtio\_sqe](#c.rtio_sqe) \*sqe, const struct [rtio\_iodev](#c.rtio_iodev) \*iodev, void \*userdata)
    :   Prepare a nop (no op) submission.

    static inline void rtio\_sqe\_prep\_read(struct [rtio\_sqe](#c.rtio_sqe) \*sqe, const struct [rtio\_iodev](#c.rtio_iodev) \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)
    :   Prepare a read op submission.

    static inline void rtio\_sqe\_prep\_read\_with\_pool(struct [rtio\_sqe](#c.rtio_sqe) \*sqe, const struct [rtio\_iodev](#c.rtio_iodev) \*iodev, int8\_t prio, void \*userdata)
    :   Prepare a read op submission with context’s mempool.

        See also

        [rtio\_sqe\_prep\_read()](#group__rtio_1ga89c7cc2494e3dda50737f78f1a1376cf)

    static inline void rtio\_sqe\_prep\_read\_multishot(struct [rtio\_sqe](#c.rtio_sqe) \*sqe, const struct [rtio\_iodev](#c.rtio_iodev) \*iodev, int8\_t prio, void \*userdata)

    static inline void rtio\_sqe\_prep\_write(struct [rtio\_sqe](#c.rtio_sqe) \*sqe, const struct [rtio\_iodev](#c.rtio_iodev) \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)
    :   Prepare a write op submission.

    static inline void rtio\_sqe\_prep\_tiny\_write(struct [rtio\_sqe](#c.rtio_sqe) \*sqe, const struct [rtio\_iodev](#c.rtio_iodev) \*iodev, int8\_t prio, const uint8\_t \*tiny\_write\_data, uint8\_t tiny\_write\_len, void \*userdata)
    :   Prepare a tiny write op submission.

        Unlike the normal write operation where the source buffer must outlive the call the tiny write data in this case is copied to the sqe. It must be tiny to fit within the specified size of a [rtio\_sqe](#structrtio__sqe).

        This is useful in many scenarios with RTL logic where a write of the register to subsequently read must be done.

    static inline void rtio\_sqe\_prep\_callback(struct [rtio\_sqe](#c.rtio_sqe) \*sqe, [rtio\_callback\_t](#c.rtio_callback_t) callback, void \*arg0, void \*userdata)
    :   Prepare a callback op submission.

        A somewhat special operation in that it may only be done in kernel mode.

        Used where general purpose logic is required in a queue of io operations to do transforms or logic.

    static inline void rtio\_sqe\_prep\_transceive(struct [rtio\_sqe](#c.rtio_sqe) \*sqe, const struct [rtio\_iodev](#c.rtio_iodev) \*iodev, int8\_t prio, uint8\_t \*tx\_buf, uint8\_t \*rx\_buf, uint32\_t buf\_len, void \*userdata)
    :   Prepare a transceive op submission.

    static inline struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*rtio\_sqe\_pool\_alloc(struct [rtio\_sqe\_pool](#c.rtio_sqe_pool) \*pool)

    static inline void rtio\_sqe\_pool\_free(struct [rtio\_sqe\_pool](#c.rtio_sqe_pool) \*pool, struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe)

    static inline struct [rtio\_cqe](#c.rtio_cqe) \*rtio\_cqe\_pool\_alloc(struct [rtio\_cqe\_pool](#c.rtio_cqe_pool) \*pool)

    static inline void rtio\_cqe\_pool\_free(struct [rtio\_cqe\_pool](#c.rtio_cqe_pool) \*pool, struct [rtio\_cqe](#c.rtio_cqe) \*cqe)

    static inline int rtio\_block\_pool\_alloc(struct [rtio](#c.rtio) \*r, size\_t min\_sz, size\_t max\_sz, uint8\_t \*\*buf, uint32\_t \*buf\_len)

    static inline void rtio\_block\_pool\_free(struct [rtio](#c.rtio) \*r, void \*buf, uint32\_t buf\_len)

    static inline uint32\_t rtio\_sqe\_acquirable(struct [rtio](#c.rtio) \*r)
    :   Count of acquirable submission queue events.

        Parameters:
        :   - **r** – RTIO context

        Returns:
        :   Count of acquirable submission queue events

    static inline struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*rtio\_txn\_next(const struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe)
    :   Get the next sqe in the transaction.

        Parameters:
        :   - **iodev\_sqe** – Submission queue entry

        Return values:
        :   - **NULL** – if current sqe is last in transaction
            - **struct** – [rtio\_sqe](#structrtio__sqe) \* if available

    static inline struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*rtio\_chain\_next(const struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe)
    :   Get the next sqe in the chain.

        Parameters:
        :   - **iodev\_sqe** – Submission queue entry

        Return values:
        :   - **NULL** – if current sqe is last in chain
            - **struct** – [rtio\_sqe](#structrtio__sqe) \* if available

    static inline struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*rtio\_iodev\_sqe\_next(const struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe)
    :   Get the next sqe in the chain or transaction.

        Parameters:
        :   - **iodev\_sqe** – Submission queue entry

        Return values:
        :   - **NULL** – if current sqe is last in chain
            - **struct** – [rtio\_iodev\_sqe](#structrtio__iodev__sqe) \* if available

    static inline struct [rtio\_sqe](#c.rtio_sqe) \*rtio\_sqe\_acquire(struct [rtio](#c.rtio) \*r)
    :   Acquire a single submission queue event if available.

        Parameters:
        :   - **r** – RTIO context

        Return values:
        :   - **sqe** – A valid submission queue event acquired from the submission queue
            - **NULL** – No subsmission queue event available

    static inline void rtio\_sqe\_drop\_all(struct [rtio](#c.rtio) \*r)
    :   Drop all previously acquired sqe.

        Parameters:
        :   - **r** – RTIO context

    static inline struct [rtio\_cqe](#c.rtio_cqe) \*rtio\_cqe\_acquire(struct [rtio](#c.rtio) \*r)
    :   Acquire a complete queue event if available.

    static inline void rtio\_cqe\_produce(struct [rtio](#c.rtio) \*r, struct [rtio\_cqe](#c.rtio_cqe) \*cqe)
    :   Produce a complete queue event if available.

    static inline struct [rtio\_cqe](#c.rtio_cqe) \*rtio\_cqe\_consume(struct [rtio](#c.rtio) \*r)
    :   Consume a single completion queue event if available.

        If a completion queue event is returned rtio\_cq\_release(r) must be called at some point to release the cqe spot for the cqe producer.

        Parameters:
        :   - **r** – RTIO context

        Return values:
        :   - **cqe** – A valid completion queue event consumed from the completion queue
            - **NULL** – No completion queue event available

    static inline struct [rtio\_cqe](#c.rtio_cqe) \*rtio\_cqe\_consume\_block(struct [rtio](#c.rtio) \*r)
    :   Wait for and consume a single completion queue event.

        If a completion queue event is returned rtio\_cq\_release(r) must be called at some point to release the cqe spot for the cqe producer.

        Parameters:
        :   - **r** – RTIO context

        Return values:
        :   **cqe** – A valid completion queue event consumed from the completion queue

    static inline void rtio\_cqe\_release(struct [rtio](#c.rtio) \*r, struct [rtio\_cqe](#c.rtio_cqe) \*cqe)
    :   Release consumed completion queue event.

        Parameters:
        :   - **r** – RTIO context
            - **cqe** – Completion queue entry

    static inline uint32\_t rtio\_cqe\_compute\_flags(struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe)
    :   Compute the CQE flags from the [rtio\_iodev\_sqe](#structrtio__iodev__sqe) entry.

        Parameters:
        :   - **iodev\_sqe** – The SQE entry in question.

        Returns:
        :   The value that should be set for the CQE’s flags field.

    int rtio\_cqe\_get\_mempool\_buffer(const struct [rtio](#c.rtio) \*r, struct [rtio\_cqe](#c.rtio_cqe) \*cqe, uint8\_t \*\*buff, uint32\_t \*buff\_len)
    :   Retrieve the mempool buffer that was allocated for the CQE.

        If the RTIO context contains a memory pool, and the SQE was created by calling rtio\_sqe\_read\_with\_pool(), this function can be used to retrieve the memory associated with the read. Once processing is done, it should be released by calling [rtio\_release\_buffer()](#group__rtio_1ga6530bf56ccbab046a362a6448f941609).

        Parameters:
        :   - **r** – RTIO context
            - **cqe** – **[in]** The CQE handling the event.
            - **buff** – **[out]** Pointer to the mempool buffer
            - **buff\_len** – **[out]** Length of the allocated buffer

        Returns:
        :   0 on success

        Returns:
        :   -EINVAL if the buffer wasn’t allocated for this cqe

        Returns:
        :   -ENOTSUP if memory blocks are disabled

    void rtio\_executor\_submit(struct [rtio](#c.rtio) \*r)

    void rtio\_executor\_ok(struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe, int result)

    void rtio\_executor\_err(struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe, int result)

    static inline void rtio\_iodev\_sqe\_ok(struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe, int result)
    :   Inform the executor of a submission completion with success.

        This may start the next asynchronous request if one is available.

        Parameters:
        :   - **iodev\_sqe** – IODev Submission that has succeeded
            - **result** – Result of the request

    static inline void rtio\_iodev\_sqe\_err(struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe, int result)
    :   Inform the executor of a submissions completion with error.

        This SHALL fail the remaining submissions in the chain.

        Parameters:
        :   - **iodev\_sqe** – Submission that has failed
            - **result** – Result of the request

    static inline void rtio\_cqe\_submit(struct [rtio](#c.rtio) \*r, int result, void \*userdata, uint32\_t flags)
    :   Submit a completion queue event with a given result and userdata.

        Called by the executor to produce a completion queue event, no inherent locking is performed and this is not safe to do from multiple callers.

        Parameters:
        :   - **r** – RTIO context
            - **result** – Integer result code (could be -errno)
            - **userdata** – Userdata to pass along to completion
            - **flags** – Flags to use for the CEQ see RTIO\_CQE\_FLAG\_\*

    static inline int rtio\_sqe\_rx\_buf(const struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe, uint32\_t min\_buf\_len, uint32\_t max\_buf\_len, uint8\_t \*\*buf, uint32\_t \*buf\_len)
    :   Get the buffer associate with the RX submission.

        Parameters:
        :   - **iodev\_sqe** – **[in]** The submission to probe
            - **min\_buf\_len** – **[in]** The minimum number of bytes needed for the operation
            - **max\_buf\_len** – **[in]** The maximum number of bytes needed for the operation
            - **buf** – **[out]** Where to store the pointer to the buffer
            - **buf\_len** – **[out]** Where to store the size of the buffer

        Returns:
        :   0 if `buf` and `buf_len` were successfully filled

        Returns:
        :   -ENOMEM Not enough memory for `min_buf_len`

    void rtio\_release\_buffer(struct [rtio](#c.rtio) \*r, void \*buff, uint32\_t buff\_len)
    :   Release memory that was allocated by the RTIO’s memory pool.

        If the RTIO context was created by a call to [RTIO\_DEFINE\_WITH\_MEMPOOL()](#group__rtio_1gae4c2a9384a9ae4ed16dff914b1184ca8), then the cqe data might contain a buffer that’s owned by the RTIO context. In those cases (if the read request was configured via rtio\_sqe\_read\_with\_pool()) the buffer must be returned back to the pool.

        Call this function when processing is complete. This function will validate that the memory actually belongs to the RTIO context and will ignore invalid arguments.

        Parameters:
        :   - **r** – RTIO context
            - **buff** – Pointer to the buffer to be released.
            - **buff\_len** – Number of bytes to free (will be rounded up to nearest memory block).

    static inline void rtio\_access\_grant(struct [rtio](#c.rtio) \*r, struct [k\_thread](../../kernel/services/threads/index.md#c.k_thread "k_thread") \*t)
    :   Grant access to an RTIO context to a user thread.

    int rtio\_sqe\_cancel(struct [rtio\_sqe](#c.rtio_sqe) \*sqe)
    :   Attempt to cancel an SQE.

        If possible (not currently executing), cancel an SQE and generate a failure with -ECANCELED result.

        Parameters:
        :   - **sqe** – **[in]** The SQE to cancel

        Returns:
        :   0 if the SQE was flagged for cancellation

        Returns:
        :   <0 on error

    int rtio\_sqe\_copy\_in\_get\_handles(struct [rtio](#c.rtio) \*r, const struct [rtio\_sqe](#c.rtio_sqe) \*sqes, struct [rtio\_sqe](#c.rtio_sqe) \*\*handle, size\_t sqe\_count)
    :   Copy an array of SQEs into the queue and get resulting handles back.

        Copies one or more SQEs into the RTIO context and optionally returns their generated SQE handles. Handles can be used to cancel events via the [rtio\_sqe\_cancel()](#group__rtio_1gac01252e55d2848b38c0ed77b71d600a7) call.

        Parameters:
        :   - **r** – RTIO context
            - **sqes** – **[in]** Pointer to an array of SQEs
            - **handle** – **[out]** Optional pointer to [rtio\_sqe](#structrtio__sqe) pointer to store the handle of the first generated SQE. Use NULL to ignore.
            - **sqe\_count** – **[in]** Count of sqes in array

        Return values:
        :   - **0** – success
            - **-ENOMEM** – not enough room in the queue

    static inline int rtio\_sqe\_copy\_in(struct [rtio](#c.rtio) \*r, const struct [rtio\_sqe](#c.rtio_sqe) \*sqes, size\_t sqe\_count)
    :   Copy an array of SQEs into the queue.

        Useful if a batch of submissions is stored in ROM or RTIO is used from user mode where a copy must be made.

        Partial copying is not done as chained SQEs need to be submitted as a whole set.

        Parameters:
        :   - **r** – RTIO context
            - **sqes** – Pointer to an array of SQEs
            - **sqe\_count** – Count of sqes in array

        Return values:
        :   - **0** – success
            - **-ENOMEM** – not enough room in the queue

    int rtio\_cqe\_copy\_out(struct [rtio](#c.rtio) \*r, struct [rtio\_cqe](#c.rtio_cqe) \*cqes, size\_t cqe\_count, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Copy an array of CQEs from the queue.

        Copies from the RTIO context and its queue completion queue events, waiting for the given time period to gather the number of completions requested.

        Parameters:
        :   - **r** – RTIO context
            - **cqes** – Pointer to an array of SQEs
            - **cqe\_count** – Count of sqes in array
            - **timeout** – Timeout to wait for each completion event. Total wait time is potentially timeout\*cqe\_count at maximum.

        Return values:
        :   **copy\_count** – Count of copied CQEs (0 to cqe\_count)

    int rtio\_submit(struct [rtio](#c.rtio) \*r, uint32\_t wait\_count)
    :   Submit I/O requests to the underlying executor.

        Submits the queue of submission queue events to the executor. The executor will do the work of managing tasks representing each submission chain, freeing submission queue events when done, and producing completion queue events as submissions are completed.

        Parameters:
        :   - **r** – RTIO context
            - **wait\_count** – Number of submissions to wait for completion of.

        Return values:
        :   **0** – On success

    Variables

    struct [k\_mem\_partition](../../kernel/usermode/memory_domain.md#c.k_mem_partition "k_mem_partition") rtio\_partition
    :   The memory partition associated with all RTIO context information.

    struct rtio\_sqe
    :   *#include <rtio.h>*

        A submission queue event.

        Public Members

        uint8\_t op
        :   Op code.

        uint8\_t prio
        :   Op priority.

        uint16\_t flags
        :   Op Flags.

        uint16\_t iodev\_flags
        :   Op iodev flags.

        const struct [rtio\_iodev](#c.rtio_iodev) \*iodev
        :   Device to operation on.

        void \*userdata
        :   User provided data which is returned upon operation completion.

            Could be a pointer or integer.

            If unique identification of completions is desired this should be unique as well.

        uint32\_t buf\_len
        :   Length of buffer.

        uint8\_t \*buf
        :   Buffer to use.

        uint8\_t tiny\_buf\_len
        :   Length of tiny buffer.

        uint8\_t tiny\_buf[7]
        :   Tiny buffer.

        void \*arg0
        :   Last argument given to callback.

        uint32\_t i2c\_config
        :   OP\_I2C\_CONFIGURE.

    struct rtio\_cqe
    :   *#include <rtio.h>*

        A completion queue event.

        Public Members

        int32\_t result
        :   Result from operation.

        void \*userdata
        :   Associated userdata with operation.

        uint32\_t flags
        :   Flags associated with the operation.

    struct rtio\_sqe\_pool
    :   *#include <rtio.h>*

    struct rtio\_cqe\_pool
    :   *#include <rtio.h>*

    struct rtio
    :   *#include <rtio.h>*

        An RTIO context containing what can be viewed as a pair of queues.

        A queue for submissions (available and in queue to be produced) as well as a queue of completions (available and ready to be consumed).

        The rtio executor along with any objects implementing the [rtio\_iodev](#structrtio__iodev) interface are the consumers of submissions and producers of completions.

        No work is started until [rtio\_submit()](#group__rtio_1gafee27c64a4a4989c4eb774addde8eb2e) is called.

    struct rtio\_iodev\_sqe
    :   *#include <rtio.h>*

        Compute the mempool block index for a given pointer.

        IO device submission queue entry

        May be cast safely to and from a [rtio\_sqe](#structrtio__sqe) as they occupy the same memory provided by the pool

        Param r:
        :   RTIO context

        Param ptr:
        :   **[in]** Memory pointer in the mempool

        Return:
        :   Index of the mempool block associated with the pointer. Or UINT16\_MAX if invalid.

    struct rtio\_iodev\_api
    :   *#include <rtio.h>*

        API that an RTIO IO device should implement.

        Public Members

        void (\*submit)(struct [rtio\_iodev\_sqe](#c.rtio_iodev_sqe) \*iodev\_sqe)
        :   Submit to the iodev an entry to work on.

            This call should be short in duration and most likely either enqueue or kick off an entry with the hardware.

            Param iodev\_sqe:
            :   Submission queue entry

    struct rtio\_iodev
    :   *#include <rtio.h>*

        An IO device with a function table for submitting requests.
