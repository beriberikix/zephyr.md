---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/retention_8h.html
original_path: doxygen/html/retention_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

retention.h File Reference

Public API for retention API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](retention_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [retention\_api](structretention__api.md) |

| Typedefs | |
| --- | --- |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [retention\_size\_api](group__retention__api.md#ga769bf90c91fd3722878869fac90f9b49)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [retention\_is\_valid\_api](group__retention__api.md#gaefaa65af1dc36193ddd4e75c9bc5d7ca)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [retention\_read\_api](group__retention__api.md#ga6f9ae5917a8fbe4353da2f5a643c56b9)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| typedef int(\* | [retention\_write\_api](group__retention__api.md#ga45734d6dbf7438229a2d51de58f304b5)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| typedef int(\* | [retention\_clear\_api](group__retention__api.md#ga87c06c45b70c4bf2e3a2c7f36b26ab89)) (const struct [device](structdevice.md) \*dev) |

| Functions | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [retention\_size](group__retention__api.md#gaf20780720d64144b50e03f9e04d3f39b) (const struct [device](structdevice.md) \*dev) |
|  | Returns the size of the retention area. |
| int | [retention\_is\_valid](group__retention__api.md#gaa3f12ad0b1929a828e8d42c7c073a16d) (const struct [device](structdevice.md) \*dev) |
|  | Checks if the underlying data in the retention area is valid or not. |
| int | [retention\_read](group__retention__api.md#ga7b4c04850ec0b57d120a0f1425d8b583) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Reads data from the retention area. |
| int | [retention\_write](group__retention__api.md#ga6131168ffc3f6d0e4329cf56f32071cc) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Writes data to the retention area (underlying data does not need to be cleared prior to writing), once function returns with a success code, the data will be classed as valid if queried using [retention\_is\_valid()](group__retention__api.md#gaa3f12ad0b1929a828e8d42c7c073a16d "Checks if the underlying data in the retention area is valid or not."). |
| int | [retention\_clear](group__retention__api.md#gaab8a56b5879faabd10982bc110577a1d) (const struct [device](structdevice.md) \*dev) |
|  | Clears all data in the retention area (sets it to 0). |

## Detailed Description

Public API for retention API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [retention](dir_acb4c99582103da541bc87f13e94ee5a.md)
- [retention.h](retention_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
