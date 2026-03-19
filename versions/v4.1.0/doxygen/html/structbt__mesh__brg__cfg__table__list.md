---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__brg__cfg__table__list.html
original_path: doxygen/html/structbt__mesh__brg__cfg__table__list.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_brg\_cfg\_table\_list Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bridge Configuration common header](group__bt__mesh__brg__cfg.md)

Bridging Table List response.
[More...](#details)

`#include <[brg_cfg.h](brg__cfg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a6ac8abf7a95eda792065171e71f699b2) |
|  | Status Code of the requesting message. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx1](#a68cfc1c6514f3b7f6eb0d7ad98a15e96) |
|  | NetKey Index of the first subnet. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx2](#a091f7458fb6fcd6423c944cc1ebfe0a0) |
|  | NetKey Index of the second subnet. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [start\_idx](#a7c8ebdfc898826d95ec94b34ec3c0945) |
|  | Start offset in units of bridging table state entries. |
| struct [net\_buf\_simple](structnet__buf__simple.md) \* | [list](#a44ce11d9a2cbda69b605fab6ed68cc56) |
|  | Pointer to allocated buffer for storing list of bridged addresses and directions. |

## Detailed Description

Bridging Table List response.

## Field Documentation

## [◆ ](#a44ce11d9a2cbda69b605fab6ed68cc56)list

| struct [net\_buf\_simple](structnet__buf__simple.md)\* bt\_mesh\_brg\_cfg\_table\_list::list |
| --- |

Pointer to allocated buffer for storing list of bridged addresses and directions.

## [◆ ](#a68cfc1c6514f3b7f6eb0d7ad98a15e96)net\_idx1

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_brg\_cfg\_table\_list::net\_idx1 |
| --- |

NetKey Index of the first subnet.

## [◆ ](#a091f7458fb6fcd6423c944cc1ebfe0a0)net\_idx2

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_brg\_cfg\_table\_list::net\_idx2 |
| --- |

NetKey Index of the second subnet.

## [◆ ](#a7c8ebdfc898826d95ec94b34ec3c0945)start\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_brg\_cfg\_table\_list::start\_idx |
| --- |

Start offset in units of bridging table state entries.

## [◆ ](#a6ac8abf7a95eda792065171e71f699b2)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_brg\_cfg\_table\_list::status |
| --- |

Status Code of the requesting message.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[brg\_cfg.h](brg__cfg_8h_source.md)

- [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
