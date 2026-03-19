---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__comp__p1__model__item.html
original_path: doxygen/html/structbt__mesh__comp__p1__model__item.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_comp\_p1\_model\_item Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Composition data page 1 model item representation.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [cor\_present](#aee352e8563133dddbb37c1f31dfe7c09) |
|  | Corresponding\_Group\_ID field indicator. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [format](#af2f213813440cb4a87884e3625a704e7) |
|  | Determines the format of Extended Model Item. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ext\_item\_cnt](#ae019a211eafeb20f323ad97328d938f7): 6 |
|  | Number of items in Extended Model Items. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cor\_id](#a95baa1acf3a82e8559ce4a47b7e03be8) |
|  | Buffer containing Extended Model Items. |

## Detailed Description

Composition data page 1 model item representation.

## Field Documentation

## [◆ ](#a95baa1acf3a82e8559ce4a47b7e03be8)cor\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp\_p1\_model\_item::cor\_id |
| --- |

Buffer containing Extended Model Items.

If cor\_present is set to 1 it starts with Corresponding\_Group\_ID

## [◆ ](#aee352e8563133dddbb37c1f31dfe7c09)cor\_present

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_comp\_p1\_model\_item::cor\_present |
| --- |

Corresponding\_Group\_ID field indicator.

## [◆ ](#ae019a211eafeb20f323ad97328d938f7)ext\_item\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp\_p1\_model\_item::ext\_item\_cnt |
| --- |

Number of items in Extended Model Items.

## [◆ ](#af2f213813440cb4a87884e3625a704e7)format

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_comp\_p1\_model\_item::format |
| --- |

Determines the format of Extended Model Item.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
