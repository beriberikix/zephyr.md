---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__comp__p0__elem.html
original_path: doxygen/html/structbt__mesh__comp__p0__elem.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_comp\_p0\_elem Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Composition data page 0 element representation.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [loc](#a832cdb0a10d364a048971f59f51e841d) |
|  | Element location. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [nsig](#a17f61eab2df28f2031f2fbab28254484) |
|  | The number of SIG models in this element. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [nvnd](#a2e1bd3146ebc934e9fab0242a06d5b99) |
|  | The number of vendor models in this element. |

## Detailed Description

Composition data page 0 element representation.

## Field Documentation

## [◆ ](#a832cdb0a10d364a048971f59f51e841d)loc

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp\_p0\_elem::loc |
| --- |

Element location.

## [◆ ](#a17f61eab2df28f2031f2fbab28254484)nsig

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_comp\_p0\_elem::nsig |
| --- |

The number of SIG models in this element.

## [◆ ](#a2e1bd3146ebc934e9fab0242a06d5b99)nvnd

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_comp\_p0\_elem::nvnd |
| --- |

The number of vendor models in this element.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
