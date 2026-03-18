---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__comp__p2__record.html
original_path: doxygen/html/structbt__mesh__comp__p2__record.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_comp\_p2\_record Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Configuration Client Model](group__bt__mesh__cfg__cli.md)

Composition data page 2 record parsing structure.
[More...](#details)

`#include <[cfg_cli.h](cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#a4d947193b1a0f46c9df1eca298135646) |
|  | Mesh profile ID. |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [x](#a5377ce835db8ce408d8dabfd87c858f5) |  |
|  | Major version. [More...](#a5377ce835db8ce408d8dabfd87c858f5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [y](#a0ceff9becd0eb14ca190c49f56ec0957) |  |
|  | Minor version. [More...](#a0ceff9becd0eb14ca190c49f56ec0957) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [z](#a90e80906ef6d2b8b932215ad183db2d5) |  |
|  | Z version. [More...](#a90e80906ef6d2b8b932215ad183db2d5) |
| } | [version](#aa718c024d6ce339ac8c352319b878c53) |
|  | Mesh Profile Version. |
| struct [net\_buf\_simple](structnet__buf__simple.md) \* | [elem\_buf](#ad310f8c8e3a167492a6e698336b7f400) |
|  | Element offset buffer. |
| struct [net\_buf\_simple](structnet__buf__simple.md) \* | [data\_buf](#abd0975a47c848265ad13044dfcd3b78d) |
|  | Additional data buffer. |

## Detailed Description

Composition data page 2 record parsing structure.

## Field Documentation

## [◆ ](#abd0975a47c848265ad13044dfcd3b78d)data\_buf

| struct [net\_buf\_simple](structnet__buf__simple.md)\* bt\_mesh\_comp\_p2\_record::data\_buf |
| --- |

Additional data buffer.

## [◆ ](#ad310f8c8e3a167492a6e698336b7f400)elem\_buf

| struct [net\_buf\_simple](structnet__buf__simple.md)\* bt\_mesh\_comp\_p2\_record::elem\_buf |
| --- |

Element offset buffer.

## [◆ ](#a4d947193b1a0f46c9df1eca298135646)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp\_p2\_record::id |
| --- |

Mesh profile ID.

## [◆ ](#aa718c024d6ce339ac8c352319b878c53)[struct]

| struct { ... } bt\_mesh\_comp\_p2\_record::version |
| --- |

Mesh Profile Version.

## [◆ ](#a5377ce835db8ce408d8dabfd87c858f5)x

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp\_p2\_record::x |
| --- |

Major version.

## [◆ ](#a0ceff9becd0eb14ca190c49f56ec0957)y

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp\_p2\_record::y |
| --- |

Minor version.

## [◆ ](#a90e80906ef6d2b8b932215ad183db2d5)z

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_comp\_p2\_record::z |
| --- |

Z version.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cfg\_cli.h](cfg__cli_8h_source.md)

- [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
