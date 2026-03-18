---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/storage/stream/stream_flash.html
original_path: services/storage/stream/stream_flash.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Stream Flash

The Stream Flash module takes contiguous fragments of a stream of data (e.g.
from radio packets), aggregates them into a user-provided buffer, then when the
buffer fills (or stream ends) writes it to a raw flash partition. It supports
providing the read-back buffer to the client to use in validating the persisted
stream content.

One typical use of a stream write operation is when receiving a new firmware
image to be used in a DFU operation.

There are several reasons why one might want to use buffered writes instead of
writing the data directly as it is made available. Some devices have hardware
limitations which does not allow flash writes to be performed in parallel with
other operations, such as radio RX and TX. Also, fewer write operations result
in faster response times seen from the application.

## Persistent stream write progress

Some stream write operations, such as DFU operations, may run for a long time.
When performing such long running operations it can be useful to be able to save
the stream write progress to persistent storage so that the operation can resume
at the same point after an unexpected interruption.

The Stream Flash module offers an API for loading, saving and clearing stream
write progress to persistent storage using the [Settings](../../settings/index.md#settings-api)
module. The API can be enabled using [`CONFIG_STREAM_FLASH_PROGRESS`](../../../kconfig.md#CONFIG_STREAM_FLASH_PROGRESS "CONFIG_STREAM_FLASH_PROGRESS").

## API Reference

*group* stream\_flash
:   Abstraction over stream writes to flash.

    Typedefs

    typedef int (\*stream\_flash\_callback\_t)(uint8\_t \*buf, size\_t len, size\_t offset)
    :   Signature for callback invoked after flash write completes.

        Functions of this type are invoked with a buffer containing data read back from the flash after a flash write has completed. This enables verifying that the data has been correctly stored (for instance by using a SHA function). The write buffer ‘buf’ provided in stream\_flash\_init is used as a read buffer for this purpose.

        Param buf:
        :   Pointer to the data read.

        Param len:
        :   The length of the data read.

        Param offset:
        :   The offset the data was read from.

    Functions

    int stream\_flash\_init(struct [stream\_flash\_ctx](#c.stream_flash_ctx) \*ctx, const struct [device](../../../kernel/drivers/index.md#c.device "device") \*fdev, uint8\_t \*buf, size\_t buf\_len, size\_t offset, size\_t size, [stream\_flash\_callback\_t](#c.stream_flash_callback_t) cb)
    :   Initialize context needed for stream writes to flash.

        Parameters:
        :   - **ctx** – context to be initialized
            - **fdev** – Flash device to operate on
            - **buf** – Write buffer
            - **buf\_len** – Length of write buffer. Can not be larger than the page size. Must be multiple of the flash device write-block-size.
            - **offset** – Offset within flash device to start writing to
            - **size** – Number of bytes available for performing buffered write. If this is ‘0’, the size will be set to the total size of the flash device minus the offset.
            - **cb** – Callback to be invoked on completed flash write operations.

        Returns:
        :   non-negative on success, negative errno code on fail

    size\_t stream\_flash\_bytes\_written(struct [stream\_flash\_ctx](#c.stream_flash_ctx) \*ctx)
    :   Read number of bytes written to the flash.

        Note

        api-tags: pre-kernel-ok isr-ok

        Parameters:
        :   - **ctx** – context

        Returns:
        :   Number of payload bytes written to flash.

    int stream\_flash\_buffered\_write(struct [stream\_flash\_ctx](#c.stream_flash_ctx) \*ctx, const uint8\_t \*data, size\_t len, bool flush)
    :   Process input buffers to be written to flash device in single blocks.

        Will store remainder between calls.

        A final call to this function with flush set to true will write out the remaining block buffer to flash.

        Parameters:
        :   - **ctx** – context
            - **data** – data to write
            - **len** – Number of bytes to write
            - **flush** – when true this forces any buffered data to be written to flash A flush write should be the last write operation in a sequence of write operations for given context (although this is not mandatory if the total data size is a multiple of the buffer size).

        Returns:
        :   non-negative on success, negative errno code on fail

    int stream\_flash\_erase\_page(struct [stream\_flash\_ctx](#c.stream_flash_ctx) \*ctx, off\_t off)
    :   Erase the flash page to which a given offset belongs.

        This function erases a flash page to which an offset belongs if this page is not the page previously erased by the provided ctx (ctx->last\_erased\_page\_start\_offset).

        Parameters:
        :   - **ctx** – context
            - **off** – offset from the base address of the flash device

        Returns:
        :   non-negative on success, negative errno code on fail

    int stream\_flash\_progress\_load(struct [stream\_flash\_ctx](#c.stream_flash_ctx) \*ctx, const char \*settings\_key)
    :   Load persistent stream write progress stored with key `settings_key` .

        This function should be called directly after [stream\_flash\_init](#group__stream__flash_1ga63e6418e220136a9a0ab2992d9d8f937) to load previous stream write progress before writing any data. If the loaded progress has fewer bytes written than `ctx` then it will be ignored.

        Parameters:
        :   - **ctx** – context
            - **settings\_key** – key to use with the settings module for loading the stream write progress

        Returns:
        :   non-negative on success, negative errno code on fail

    int stream\_flash\_progress\_save(struct [stream\_flash\_ctx](#c.stream_flash_ctx) \*ctx, const char \*settings\_key)
    :   Save persistent stream write progress using key `settings_key` .

        Parameters:
        :   - **ctx** – context
            - **settings\_key** – key to use with the settings module for storing the stream write progress

        Returns:
        :   non-negative on success, negative errno code on fail

    int stream\_flash\_progress\_clear(struct [stream\_flash\_ctx](#c.stream_flash_ctx) \*ctx, const char \*settings\_key)
    :   Clear persistent stream write progress stored with key `settings_key` .

        Parameters:
        :   - **ctx** – context
            - **settings\_key** – key previously used for storing the stream write progress

        Returns:
        :   non-negative on success, negative errno code on fail

    struct stream\_flash\_ctx
    :   *#include <stream\_flash.h>*

        Structure for stream flash context.

        Users should treat these structures as opaque values and only interact with them through the below API.
