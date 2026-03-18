---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__model.html
original_path: doxygen/html/structbt__mesh__model.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_model Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Abstraction that describes a Mesh Model instance.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_model\_rt\_ctx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md) |

| Data Fields | |
| --- | --- |
| union { |  |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [id](#a848ccf09f7b75ff8a48acb6c8088cf2a) |  |
|  | SIG model ID. [More...](#a848ccf09f7b75ff8a48acb6c8088cf2a) |
| const struct [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md)   [vnd](#a3372deccde1a5ab26d9204c97339596e) |  |
|  | Vendor model ID. [More...](#a3372deccde1a5ab26d9204c97339596e) |
| }; |  |
| struct [bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md) | [rt](#a3980e6f8100151cb3339792821fa7858) |
| struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) \*const | [pub](#af4a1b5e837b3a1266c7f61ee21020c0b) |
|  | Model Publication. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const | [keys](#a63595a0559ca70ca76c996f0b71c7983) |
|  | AppKey List. |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [keys\_cnt](#a79b8fd44ced901c3478f0e04d7dadfcd) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const | [groups](#a460ab46730afa4f74e4066f787864b0b) |
|  | Subscription List (group or virtual addresses). |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [groups\_cnt](#adf3e3f0dab9838cc76361949b237bb9e) |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*const | [uuids](#a274c811c22b764908599127b128ce584) |
|  | List of Label UUIDs the model is subscribed to. |
| const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \*const | [op](#a4acc656c737cf79161414984312100b6) |
|  | Opcode handler list. |
| const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \*const | [cb](#a67a91d64051e055b79f5d9166ab12660) |
|  | Model callback structure. |
| const struct [bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md) \*const | [metadata](#af5b948709773e5388c30d457ec2a9559) |

## Detailed Description

Abstraction that describes a Mesh Model instance.

## Field Documentation

## [◆ ](#abfe9db5b0639ad7566f966ecdafd7082)[union]

| union { ... } [bt\_mesh\_model](structbt__mesh__model.md) |
| --- |

## [◆ ](#a67a91d64051e055b79f5d9166ab12660)cb

| const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)\* const bt\_mesh\_model::cb |
| --- |

Model callback structure.

## [◆ ](#a460ab46730afa4f74e4066f787864b0b)groups

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)\* const bt\_mesh\_model::groups |
| --- |

Subscription List (group or virtual addresses).

## [◆ ](#adf3e3f0dab9838cc76361949b237bb9e)groups\_cnt

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model::groups\_cnt |
| --- |

## [◆ ](#a848ccf09f7b75ff8a48acb6c8088cf2a)id

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model::id |
| --- |

SIG model ID.

## [◆ ](#a63595a0559ca70ca76c996f0b71c7983)keys

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)\* const bt\_mesh\_model::keys |
| --- |

AppKey List.

## [◆ ](#a79b8fd44ced901c3478f0e04d7dadfcd)keys\_cnt

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model::keys\_cnt |
| --- |

## [◆ ](#af5b948709773e5388c30d457ec2a9559)metadata

| const struct [bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md)\* const bt\_mesh\_model::metadata |
| --- |

## [◆ ](#a4acc656c737cf79161414984312100b6)op

| const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md)\* const bt\_mesh\_model::op |
| --- |

Opcode handler list.

## [◆ ](#af4a1b5e837b3a1266c7f61ee21020c0b)pub

| struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md)\* const bt\_mesh\_model::pub |
| --- |

Model Publication.

## [◆ ](#a3980e6f8100151cb3339792821fa7858)rt

| struct [bt\_mesh\_model::bt\_mesh\_model\_rt\_ctx](structbt__mesh__model_1_1bt__mesh__model__rt__ctx.md) bt\_mesh\_model::rt |
| --- |

## [◆ ](#a274c811c22b764908599127b128ce584)uuids

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\*\* const bt\_mesh\_model::uuids |
| --- |

List of Label UUIDs the model is subscribed to.

## [◆ ](#a3372deccde1a5ab26d9204c97339596e)vnd

| const struct [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md) bt\_mesh\_model::vnd |
| --- |

Vendor model ID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_model](structbt__mesh__model.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
