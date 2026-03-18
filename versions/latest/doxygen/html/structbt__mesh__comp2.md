---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__comp2.html
original_path: doxygen/html/structbt__mesh__comp2.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_comp2 Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Node Composition data page 2.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [record\_cnt](#a9f3425cd64cc487e9a49b85bb0f2159b) |
|  | The number of Mesh Profile records on a device. |
| const struct [bt\_mesh\_comp2\_record](structbt__mesh__comp2__record.md) \* | [record](#adf022ca0738626832d566fd6a5a1d889) |
|  | List of records. |

## Detailed Description

Node Composition data page 2.

## Field Documentation

## [◆ ](#adf022ca0738626832d566fd6a5a1d889)record

| const struct [bt\_mesh\_comp2\_record](structbt__mesh__comp2__record.md)\* bt\_mesh\_comp2::record |
| --- |

List of records.

## [◆ ](#a9f3425cd64cc487e9a49b85bb0f2159b)record\_cnt

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_comp2::record\_cnt |
| --- |

The number of Mesh Profile records on a device.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_comp2](structbt__mesh__comp2.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
