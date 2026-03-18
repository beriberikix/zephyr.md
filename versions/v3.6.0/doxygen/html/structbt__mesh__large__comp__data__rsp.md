---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__large__comp__data__rsp.html
original_path: doxygen/html/structbt__mesh__large__comp__data__rsp.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_large\_comp\_data\_rsp Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Large Composition Data Client model](group__bt__mesh__large__comp__data__cli.md)

Large Composition Data response.
[More...](#details)

`#include <[large_comp_data_cli.h](large__comp__data__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [page](#ad3d781276eaf84fd1a8a4d031c005deb) |
|  | Page number. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [offset](#a8bba19b3687a67442e91873c228be361) |
|  | Offset within the page. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [total\_size](#aaab8add82c9f24d68af0ddd279164882) |
|  | Total size of the page. |
| struct [net\_buf\_simple](structnet__buf__simple.md) \* | [data](#a02d92a210b5b7a26b1df4f5076ed99d8) |
|  | Pointer to allocated buffer for storing received data. |

## Detailed Description

Large Composition Data response.

## Field Documentation

## [◆ ](#a02d92a210b5b7a26b1df4f5076ed99d8)data

| struct [net\_buf\_simple](structnet__buf__simple.md)\* bt\_mesh\_large\_comp\_data\_rsp::data |
| --- |

Pointer to allocated buffer for storing received data.

## [◆ ](#a8bba19b3687a67442e91873c228be361)offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_large\_comp\_data\_rsp::offset |
| --- |

Offset within the page.

## [◆ ](#ad3d781276eaf84fd1a8a4d031c005deb)page

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_large\_comp\_data\_rsp::page |
| --- |

Page number.

## [◆ ](#aaab8add82c9f24d68af0ddd279164882)total\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_large\_comp\_data\_rsp::total\_size |
| --- |

Total size of the page.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[large\_comp\_data\_cli.h](large__comp__data__cli_8h_source.md)

- [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
