---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__fcb__internal.html
original_path: doxygen/html/group__fcb__internal.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcb non-API prototypes

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Flash Circular Buffer (FCB)](group__fcb.md)

Flash Circular internal.
[More...](#details)

| Functions | |
| --- | --- |
| int | [fcb\_flash\_read](#ga0b921b509dab767661058d164e80f55e) (const struct [fcb](structfcb.md) \*fcbp, const struct [flash\_sector](structflash__sector.md) \*sector, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read raw data from the fcb flash sector. |
| int | [fcb\_flash\_write](#gafcfb9b6d4b5c0e593c0a9e512a0ec309) (const struct [fcb](structfcb.md) \*fcbp, const struct [flash\_sector](structflash__sector.md) \*sector, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write raw data to the fcb flash sector. |

## Detailed Description

Flash Circular internal.

## Function Documentation

## [◆ ](#ga0b921b509dab767661058d164e80f55e)fcb\_flash\_read()

| int fcb\_flash\_read | ( | const struct [fcb](structfcb.md) \* | *fcbp*, |
| --- | --- | --- | --- |
|  |  | const struct [flash\_sector](structflash__sector.md) \* | *sector*, |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *off*, |
|  |  | void \* | *dst*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[fcb.h](fcb_8h.md)>`

Read raw data from the fcb flash sector.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |
    | [in] | sector | FCB sector. |
    | [in] | [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) | Read offset form sector begin. |
    | [out] | dst | Destination buffer. |
    | [in] | len | Read-out size. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gafcfb9b6d4b5c0e593c0a9e512a0ec309)fcb\_flash\_write()

| int fcb\_flash\_write | ( | const struct [fcb](structfcb.md) \* | *fcbp*, |
| --- | --- | --- | --- |
|  |  | const struct [flash\_sector](structflash__sector.md) \* | *sector*, |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *off*, |
|  |  | const void \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[fcb.h](fcb_8h.md)>`

Write raw data to the fcb flash sector.

Parameters
:   | [in] | fcbp | FCB instance structure. |
    | --- | --- | --- |
    | [in] | sector | FCB sector. |
    | [in] | [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) | Write offset form sector begin. |
    | [in] | src | Source buffer. |
    | [in] | len | Write size. |

Returns
:   0 on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
