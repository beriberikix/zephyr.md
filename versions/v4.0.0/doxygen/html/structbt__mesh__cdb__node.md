---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__cdb__node.html
original_path: doxygen/html/structbt__mesh__cdb__node.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_cdb\_node Struct Reference

`#include <[cdb.h](cdb_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uuid](#a751671f52c4fdf3f42b6f71193976dd5) [16] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#a8c9941929a8ce6228817d76fe4e2375c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx](#aa936534676ef7e256670d356eff7ac17) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_elem](#a2313e29b756344a493989f39ba1ec726) |
| struct bt\_mesh\_key | [dev\_key](#a54e5130d7dabedf09e23419a40f6778b) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flags](#a3c7e6369501f577ede53a4071e257956) [[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)([BT\_MESH\_CDB\_NODE\_FLAG\_COUNT](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd))] |

## Field Documentation

## [◆ ](#a8c9941929a8ce6228817d76fe4e2375c)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cdb\_node::addr |
| --- |

## [◆ ](#a54e5130d7dabedf09e23419a40f6778b)dev\_key

| struct bt\_mesh\_key bt\_mesh\_cdb\_node::dev\_key |
| --- |

## [◆ ](#a3c7e6369501f577ede53a4071e257956)flags

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) bt\_mesh\_cdb\_node::flags[[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)([BT\_MESH\_CDB\_NODE\_FLAG\_COUNT](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd))] |
| --- |

## [◆ ](#aa936534676ef7e256670d356eff7ac17)net\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cdb\_node::net\_idx |
| --- |

## [◆ ](#a2313e29b756344a493989f39ba1ec726)num\_elem

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cdb\_node::num\_elem |
| --- |

## [◆ ](#a751671f52c4fdf3f42b6f71193976dd5)uuid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cdb\_node::uuid[16] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cdb.h](cdb_8h_source.md)

- [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
