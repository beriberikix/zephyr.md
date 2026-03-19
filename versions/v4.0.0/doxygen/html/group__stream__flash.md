---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__stream__flash.html
original_path: doxygen/html/group__stream__flash.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Stream to flash interface

[Operating System Services](group__os__services.md) » [Storage APIs](group__storage__apis.md)

Abstraction over stream writes to flash.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [stream\_flash\_ctx](structstream__flash__ctx.md) |
|  | Structure for stream flash context. [More...](structstream__flash__ctx.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [stream\_flash\_callback\_t](#ga0bf1914bba75d4d799d546b917e35705)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Signature for callback invoked after flash write completes. |

| Functions | |
| --- | --- |
| int | [stream\_flash\_init](#ga63e6418e220136a9a0ab2992d9d8f937) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const struct [device](structdevice.md) \*fdev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buf\_len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [stream\_flash\_callback\_t](#ga0bf1914bba75d4d799d546b917e35705) cb) |
|  | Initialize context needed for stream writes to flash. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [stream\_flash\_bytes\_written](#gaece0b1df3d2bf4f46df588e409c3664b) (const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx) |
|  | Read number of bytes written to the flash. |
| int | [stream\_flash\_buffered\_write](#gaa23d33939f344fcd42a281afa5e6f1db) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) flush) |
|  | Process input buffers to be written to flash device in single blocks. |
| int | [stream\_flash\_erase\_page](#ga75711b22789724c2d8629e1202dcb48d) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)) |
|  | Erase the flash page to which a given offset belongs. |
| int | [stream\_flash\_progress\_load](#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f) (struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const char \*settings\_key) |
|  | Load persistent stream write progress stored with key `settings_key` . |
| int | [stream\_flash\_progress\_save](#ga44d5791cc2e8f9bacba723d6645b0d46) (const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const char \*settings\_key) |
|  | Save persistent stream write progress using key `settings_key` . |
| int | [stream\_flash\_progress\_clear](#ga94d230f73434e90eb692b02f3fbf9ff8) (const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const char \*settings\_key) |
|  | Clear persistent stream write progress stored with key `settings_key` . |

## Detailed Description

Abstraction over stream writes to flash.

Since
:   2.3

Version
:   0.1.0

## Typedef Documentation

## [◆ ](#ga0bf1914bba75d4d799d546b917e35705)stream\_flash\_callback\_t

| typedef int(\* stream\_flash\_callback\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
| --- |

`#include <[stream_flash.h](stream__flash_8h.md)>`

Signature for callback invoked after flash write completes.

Functions of this type are invoked with a buffer containing data read back from the flash after a flash write has completed. This enables verifying that the data has been correctly stored (for instance by using a SHA function). The write buffer 'buf' provided in stream\_flash\_init is used as a read buffer for this purpose.

Parameters
:   | buf | Pointer to the data read. |
    | --- | --- |
    | len | The length of the data read. |
    | offset | The offset the data was read from. |

## Function Documentation

## [◆ ](#gaa23d33939f344fcd42a281afa5e6f1db)stream\_flash\_buffered\_write()

| int stream\_flash\_buffered\_write | ( | struct [stream\_flash\_ctx](structstream__flash__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *flush* ) |

`#include <[stream_flash.h](stream__flash_8h.md)>`

Process input buffers to be written to flash device in single blocks.

Will store remainder between calls.

A write with the `flush` set to true has to be issued as the last write request for a given context, as it concludes write of a stream, and flushes buffers to storage device.

Warning
:   There must not be any additional write requests issued for a flushed context, unless it is re-initialized, as such write attempts may result in the function failing and returning error. Once context has been flushed, it can be re-initialized and re-used for new stream flash session.

Parameters
:   | ctx | context |
    | --- | --- |
    | data | data to write |
    | len | Number of bytes to write |
    | flush | when true this forces any buffered data to be written to flash |

Returns
:   non-negative on success, negative errno code on fail

## [◆ ](#gaece0b1df3d2bf4f46df588e409c3664b)stream\_flash\_bytes\_written()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stream\_flash\_bytes\_written | ( | const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[stream_flash.h](stream__flash_8h.md)>`

Read number of bytes written to the flash.

Note
:   api-tags: pre-kernel-ok isr-ok

Parameters
:   | ctx | context |
    | --- | --- |

Returns
:   Number of payload bytes written to flash.

## [◆ ](#ga75711b22789724c2d8629e1202dcb48d)stream\_flash\_erase\_page()

| int stream\_flash\_erase\_page | ( | struct [stream\_flash\_ctx](structstream__flash__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *off* ) |

`#include <[stream_flash.h](stream__flash_8h.md)>`

Erase the flash page to which a given offset belongs.

This function erases a flash page to which an offset belongs if this page is not the page previously erased by the provided ctx (ctx->last\_erased\_page\_start\_offset).

Parameters
:   | ctx | context |
    | --- | --- |
    | [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) | offset from the base address of the flash device |

Returns
:   non-negative on success, negative errno code on fail

## [◆ ](#ga63e6418e220136a9a0ab2992d9d8f937)stream\_flash\_init()

| int stream\_flash\_init | ( | struct [stream\_flash\_ctx](structstream__flash__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *fdev*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buf\_len*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [stream\_flash\_callback\_t](#ga0bf1914bba75d4d799d546b917e35705) | *cb* ) |

`#include <[stream_flash.h](stream__flash_8h.md)>`

Initialize context needed for stream writes to flash.

Parameters
:   | ctx | context to be initialized |
    | --- | --- |
    | fdev | Flash device to operate on |
    | buf | Write buffer |
    | buf\_len | Length of write buffer. Can not be larger than the page size. Must be multiple of the flash device write-block-size. |
    | offset | Offset within flash device to start writing to |
    | size | Number of bytes available for performing buffered write. If this is '0', the size will be set to the total size of the flash device minus the offset. |
    | cb | Callback to be invoked on completed flash write operations. |

Returns
:   non-negative on success, negative errno code on fail

## [◆ ](#ga94d230f73434e90eb692b02f3fbf9ff8)stream\_flash\_progress\_clear()

| int stream\_flash\_progress\_clear | ( | const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *settings\_key* ) |

`#include <[stream_flash.h](stream__flash_8h.md)>`

Clear persistent stream write progress stored with key `settings_key` .

Parameters
:   | ctx | context |
    | --- | --- |
    | settings\_key | key previously used for storing the stream write progress |

Returns
:   non-negative on success, negative errno code on fail

## [◆ ](#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)stream\_flash\_progress\_load()

| int stream\_flash\_progress\_load | ( | struct [stream\_flash\_ctx](structstream__flash__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *settings\_key* ) |

`#include <[stream_flash.h](stream__flash_8h.md)>`

Load persistent stream write progress stored with key `settings_key` .

This function should be called directly after [stream\_flash\_init](#ga63e6418e220136a9a0ab2992d9d8f937) to load previous stream write progress before writing any data. If the loaded progress has fewer bytes written than `ctx` then it will be ignored.

Parameters
:   | ctx | context |
    | --- | --- |
    | settings\_key | key to use with the settings module for loading the stream write progress |

Returns
:   non-negative on success, -ERANGE in case when `off` is out of area designated for stream or negative errno code on fail

## [◆ ](#ga44d5791cc2e8f9bacba723d6645b0d46)stream\_flash\_progress\_save()

| int stream\_flash\_progress\_save | ( | const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *settings\_key* ) |

`#include <[stream_flash.h](stream__flash_8h.md)>`

Save persistent stream write progress using key `settings_key` .

Parameters
:   | ctx | context |
    | --- | --- |
    | settings\_key | key to use with the settings module for storing the stream write progress |

Returns
:   non-negative on success, negative errno code on fail

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
