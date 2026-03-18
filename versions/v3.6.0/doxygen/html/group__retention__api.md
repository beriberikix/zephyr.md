---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__retention__api.html
original_path: doxygen/html/group__retention__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Retention API

[Operating System Services](group__os__services.md)

Retention API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Boot mode interface](group__boot__mode__interface.md) |
|  | Boot mode interface. |
|  | [Bootloader info interface](group__bootloader__info__interface.md) |
|  | Bootloader info interface. |

| Data Structures | |
| --- | --- |
| struct | [retention\_api](structretention__api.md) |

| Typedefs | |
| --- | --- |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [retention\_size\_api](#ga769bf90c91fd3722878869fac90f9b49)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [retention\_is\_valid\_api](#gaefaa65af1dc36193ddd4e75c9bc5d7ca)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [retention\_read\_api](#ga6f9ae5917a8fbe4353da2f5a643c56b9)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| typedef int(\* | [retention\_write\_api](#ga45734d6dbf7438229a2d51de58f304b5)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| typedef int(\* | [retention\_clear\_api](#ga87c06c45b70c4bf2e3a2c7f36b26ab89)) (const struct [device](structdevice.md) \*dev) |

| Functions | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [retention\_size](#gaf20780720d64144b50e03f9e04d3f39b) (const struct [device](structdevice.md) \*dev) |
|  | Returns the size of the retention area. |
| int | [retention\_is\_valid](#gaa3f12ad0b1929a828e8d42c7c073a16d) (const struct [device](structdevice.md) \*dev) |
|  | Checks if the underlying data in the retention area is valid or not. |
| int | [retention\_read](#ga7b4c04850ec0b57d120a0f1425d8b583) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Reads data from the retention area. |
| int | [retention\_write](#ga6131168ffc3f6d0e4329cf56f32071cc) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Writes data to the retention area (underlying data does not need to be cleared prior to writing), once function returns with a success code, the data will be classed as valid if queried using [retention\_is\_valid()](#gaa3f12ad0b1929a828e8d42c7c073a16d). |
| int | [retention\_clear](#gaab8a56b5879faabd10982bc110577a1d) (const struct [device](structdevice.md) \*dev) |
|  | Clears all data in the retention area (sets it to 0). |

## Detailed Description

Retention API.

## Typedef Documentation

## [◆ ](#ga87c06c45b70c4bf2e3a2c7f36b26ab89)retention\_clear\_api

| typedef int(\* retention\_clear\_api) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[retention.h](retention_8h.md)>`

## [◆ ](#gaefaa65af1dc36193ddd4e75c9bc5d7ca)retention\_is\_valid\_api

| typedef int(\* retention\_is\_valid\_api) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[retention.h](retention_8h.md)>`

## [◆ ](#ga6f9ae5917a8fbe4353da2f5a643c56b9)retention\_read\_api

| typedef int(\* retention\_read\_api) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| --- |

`#include <[retention.h](retention_8h.md)>`

## [◆ ](#ga769bf90c91fd3722878869fac90f9b49)retention\_size\_api

| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* retention\_size\_api) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[retention.h](retention_8h.md)>`

## [◆ ](#ga45734d6dbf7438229a2d51de58f304b5)retention\_write\_api

| typedef int(\* retention\_write\_api) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| --- |

`#include <[retention.h](retention_8h.md)>`

## Function Documentation

## [◆ ](#gaab8a56b5879faabd10982bc110577a1d)retention\_clear()

| int retention\_clear | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[retention.h](retention_8h.md)>`

Clears all data in the retention area (sets it to 0).

Parameters
:   | dev | Retention device to use. |
    | --- | --- |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |

## [◆ ](#gaa3f12ad0b1929a828e8d42c7c073a16d)retention\_is\_valid()

| int retention\_is\_valid | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[retention.h](retention_8h.md)>`

Checks if the underlying data in the retention area is valid or not.

Parameters
:   | dev | Retention device to use. |
    | --- | --- |

Return values
:   | 1 | If successful and data is valid. |
    | --- | --- |
    | 0 | If data is not valid. |
    | -ENOTSUP | If there is no header/checksum configured for the retention area. |
    | -errno | Error code code. |

## [◆ ](#ga7b4c04850ec0b57d120a0f1425d8b583)retention\_read()

| int retention\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[retention.h](retention_8h.md)>`

Reads data from the retention area.

Parameters
:   | dev | Retention device to use. |
    | --- | --- |
    | offset | Offset to read data from. |
    | buffer | Buffer to store read data in. |
    | size | Size of data to read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Error code code. |

## [◆ ](#gaf20780720d64144b50e03f9e04d3f39b)retention\_size()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) retention\_size | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[retention.h](retention_8h.md)>`

Returns the size of the retention area.

Parameters
:   | dev | Retention device to use. |
    | --- | --- |

Return values
:   | Positive | value indicating size in bytes on success, else negative errno code. |
    | --- | --- |

## [◆ ](#ga6131168ffc3f6d0e4329cf56f32071cc)retention\_write()

| int retention\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[retention.h](retention_8h.md)>`

Writes data to the retention area (underlying data does not need to be cleared prior to writing), once function returns with a success code, the data will be classed as valid if queried using [retention\_is\_valid()](#gaa3f12ad0b1929a828e8d42c7c073a16d).

Parameters
:   | dev | Retention device to use. |
    | --- | --- |
    | offset | Offset to write data to. |
    | buffer | Data to write. |
    | size | Size of data to be written. |

Return values
:   | 0 | on success else negative errno code. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
