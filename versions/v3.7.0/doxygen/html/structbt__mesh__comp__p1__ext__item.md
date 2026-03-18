---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__comp__p1__ext__item.html
original_path: doxygen/html/structbt__mesh__comp__p1__ext__item.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_comp\_p1\_ext\_item Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Extended Model Item.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Public Types | |
| --- | --- |
| enum | { [SHORT](#a05a526a8448e7b8a4766eb038e4c1a39a23a15546d8722d7a4706ea34c5785658) , [LONG](#a05a526a8448e7b8a4766eb038e4c1a39ae96bb3e960c4d2c356c0070f34740119) } |

| Data Fields | |
| --- | --- |
| enum bt\_mesh\_comp\_p1\_ext\_item:: { ... } | [type](#a43f50f35690e54d3680a6daa989ce1c0) |
| union { |  |
| struct [bt\_mesh\_comp\_p1\_item\_short](structbt__mesh__comp__p1__item__short.md)   [short\_item](#ae17176001203ee8c282f06e994cee647) |  |
|  | Item in short representation. [More...](#ae17176001203ee8c282f06e994cee647) |
| struct [bt\_mesh\_comp\_p1\_item\_long](structbt__mesh__comp__p1__item__long.md)   [long\_item](#a3962046fc095348035a193dad60d1149) |  |
|  | Item in long representation. [More...](#a3962046fc095348035a193dad60d1149) |
| }; |  |

## Detailed Description

Extended Model Item.

## Member Enumeration Documentation

## [◆ ](#a05a526a8448e7b8a4766eb038e4c1a39)anonymous enum

| anonymous enum |
| --- |

| Enumerator | |
| --- | --- |
| SHORT |  |
| LONG |  |

## Field Documentation

## [◆ ](#aff092a724a2997ae05b0c4f1d1045c2f)[union]

| union { ... } [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) |
| --- |

## [◆ ](#a3962046fc095348035a193dad60d1149)long\_item

| struct [bt\_mesh\_comp\_p1\_item\_long](structbt__mesh__comp__p1__item__long.md) bt\_mesh\_comp\_p1\_ext\_item::long\_item |
| --- |

Item in long representation.

## [◆ ](#ae17176001203ee8c282f06e994cee647)short\_item

| struct [bt\_mesh\_comp\_p1\_item\_short](structbt__mesh__comp__p1__item__short.md) bt\_mesh\_comp\_p1\_ext\_item::short\_item |
| --- |

Item in short representation.

## [◆ ](#a43f50f35690e54d3680a6daa989ce1c0)[]

| enum { ... } bt\_mesh\_comp\_p1\_ext\_item::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
