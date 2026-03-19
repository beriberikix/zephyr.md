---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__brg__cfg__table__entry.html
original_path: doxygen/html/structbt__mesh__brg__cfg__table__entry.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_brg\_cfg\_table\_entry Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bridge Configuration common header](group__bt__mesh__brg__cfg.md)

Bridging Table state entry corresponding to a entry in the Bridging Table.
[More...](#details)

`#include <[brg_cfg.h](brg__cfg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [directions](#a8ce83ebdec5f306382881ceba71918cf) |
|  | Allowed directions for the bridged traffic (or bridged traffic not allowed). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx1](#acd096d1ddcf598f533c5b2b2a64c22af) |
|  | NetKey Index of the first subnet. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx2](#a672407976b409e44d06875f22f6891d3) |
|  | NetKey Index of the second subnet. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr1](#aa1150034663bb584779e88a5bed3fc8c) |
|  | Address of the node in the first subnet. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr2](#a9262e4a78ca69846d3ac7e4f38d17d0d) |
|  | Address of the node in the second subnet. |

## Detailed Description

Bridging Table state entry corresponding to a entry in the Bridging Table.

## Field Documentation

## [◆ ](#aa1150034663bb584779e88a5bed3fc8c)addr1

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_brg\_cfg\_table\_entry::addr1 |
| --- |

Address of the node in the first subnet.

## [◆ ](#a9262e4a78ca69846d3ac7e4f38d17d0d)addr2

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_brg\_cfg\_table\_entry::addr2 |
| --- |

Address of the node in the second subnet.

## [◆ ](#a8ce83ebdec5f306382881ceba71918cf)directions

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_brg\_cfg\_table\_entry::directions |
| --- |

Allowed directions for the bridged traffic (or bridged traffic not allowed).

## [◆ ](#acd096d1ddcf598f533c5b2b2a64c22af)net\_idx1

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_brg\_cfg\_table\_entry::net\_idx1 |
| --- |

NetKey Index of the first subnet.

## [◆ ](#a672407976b409e44d06875f22f6891d3)net\_idx2

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_brg\_cfg\_table\_entry::net\_idx2 |
| --- |

NetKey Index of the second subnet.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[brg\_cfg.h](brg__cfg_8h_source.md)

- [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
