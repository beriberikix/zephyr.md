---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__elem.html
original_path: doxygen/html/structbt__mesh__elem.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_elem Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Abstraction that describes a Mesh Element.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_elem\_rt\_ctx](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md) |
|  | Mesh Element runtime information. [More...](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md#details) |

| Data Fields | |
| --- | --- |
| struct [bt\_mesh\_elem::bt\_mesh\_elem\_rt\_ctx](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md) | [rt](#a2090fa7827eb6a7b8bd1adfb831439cb) |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [loc](#a5f4c8ded34cf56c7f60189584e8e5b46) |
|  | Location Descriptor (GATT Bluetooth Namespace Descriptors). |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [model\_count](#a648273e844ff9fa71578372e764ca8cf) |
|  | The number of SIG models in this element. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [vnd\_model\_count](#aea56fd98c9aecfb9de3772ad3f14b25e) |
|  | The number of vendor models in this element. |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \*const | [models](#a57fefe57d9425d6666495d1f72a3f132) |
|  | The list of SIG models in this element. |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \*const | [vnd\_models](#a81d4fc1c41e2944bf7f6e71b00e19a0f) |
|  | The list of vendor models in this element. |

## Detailed Description

Abstraction that describes a Mesh Element.

## Field Documentation

## [◆ ](#a5f4c8ded34cf56c7f60189584e8e5b46)loc

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_elem::loc |
| --- |

Location Descriptor (GATT Bluetooth Namespace Descriptors).

## [◆ ](#a648273e844ff9fa71578372e764ca8cf)model\_count

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_elem::model\_count |
| --- |

The number of SIG models in this element.

## [◆ ](#a57fefe57d9425d6666495d1f72a3f132)models

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* const bt\_mesh\_elem::models |
| --- |

The list of SIG models in this element.

## [◆ ](#a2090fa7827eb6a7b8bd1adfb831439cb)rt

| struct [bt\_mesh\_elem::bt\_mesh\_elem\_rt\_ctx](structbt__mesh__elem_1_1bt__mesh__elem__rt__ctx.md) bt\_mesh\_elem::rt |
| --- |

## [◆ ](#aea56fd98c9aecfb9de3772ad3f14b25e)vnd\_model\_count

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_elem::vnd\_model\_count |
| --- |

The number of vendor models in this element.

## [◆ ](#a81d4fc1c41e2944bf7f6e71b00e19a0f)vnd\_models

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* const bt\_mesh\_elem::vnd\_models |
| --- |

The list of vendor models in this element.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_elem](structbt__mesh__elem.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
