---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dfu__metadata_8h.html
original_path: doxygen/html/dfu__metadata_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu\_metadata.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`

[Go to the source code of this file.](dfu__metadata_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dfu\_metadata\_fw\_ver](structbt__mesh__dfu__metadata__fw__ver.md) |
|  | Firmware version. [More...](structbt__mesh__dfu__metadata__fw__ver.md#details) |
| struct | [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) |
|  | Firmware metadata. [More...](structbt__mesh__dfu__metadata.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_dfu\_metadata\_fw\_core\_type](group__bt__mesh__dfu__metadata.md#gaec5fa6e61a6ae88ac7a14f1ec09585b8) { [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0) = BIT(0) , [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_NETWORK](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692) = BIT(1) , [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP\_SPECIFIC\_BLOB](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2) = BIT(2) } |
|  | Firmware core type. [More...](group__bt__mesh__dfu__metadata.md#gaec5fa6e61a6ae88ac7a14f1ec09585b8) |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_dfu\_metadata\_decode](group__bt__mesh__dfu__metadata.md#ga7f9ab277a7a47ad9cd8e616d3aa810d4) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) \*metadata) |
|  | Decode a firmware metadata from a network buffer. |
| int | [bt\_mesh\_dfu\_metadata\_encode](group__bt__mesh__dfu__metadata.md#ga94de2f3730f600d58ff2102257d7ead9) (const struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) \*metadata, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Encode a firmare metadata into a network buffer. |
| int | [bt\_mesh\_dfu\_metadata\_comp\_hash\_get](group__bt__mesh__dfu__metadata.md#ga3c5de8cefc6a47805a9c1af166e956c7) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*key, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*hash) |
|  | Compute hash of the Composition Data state. |
| int | [bt\_mesh\_dfu\_metadata\_comp\_hash\_local\_get](group__bt__mesh__dfu__metadata.md#gadc818fb83b429b0f1bef0ba83ae7a52a) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*key, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*hash) |
|  | Compute hash of the Composition Data Page 0 of this device. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfu\_metadata.h](dfu__metadata_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
