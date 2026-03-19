---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__cdb.html
original_path: doxygen/html/structbt__mesh__cdb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_cdb Struct Reference

`#include <[cdb.h](cdb_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [iv\_index](#a48b3cf852a42b580f911e193a9764517) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [lowest\_avail\_addr](#acb7f3ae85a5929b9cfc18531e1d98ab5) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flags](#a24e2334468e9be08a435f4854af195f4) [[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)([BT\_MESH\_CDB\_FLAG\_COUNT](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41))] |
| struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) | [nodes](#a7af2ac65c8919c594b8283ff57b5b7fc) [0] |
| struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) | [subnets](#ae391c898d11257c484c4e8d1b38fd9dc) [0] |
| struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) | [app\_keys](#a59a130ffed26c362dc72d57d1ac7d7fd) [0] |

## Field Documentation

## [◆ ](#a59a130ffed26c362dc72d57d1ac7d7fd)app\_keys

| struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) bt\_mesh\_cdb::app\_keys[0] |
| --- |

## [◆ ](#a24e2334468e9be08a435f4854af195f4)flags

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) bt\_mesh\_cdb::flags[[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)([BT\_MESH\_CDB\_FLAG\_COUNT](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41))] |
| --- |

## [◆ ](#a48b3cf852a42b580f911e193a9764517)iv\_index

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_cdb::iv\_index |
| --- |

## [◆ ](#acb7f3ae85a5929b9cfc18531e1d98ab5)lowest\_avail\_addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cdb::lowest\_avail\_addr |
| --- |

## [◆ ](#a7af2ac65c8919c594b8283ff57b5b7fc)nodes

| struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) bt\_mesh\_cdb::nodes[0] |
| --- |

## [◆ ](#ae391c898d11257c484c4e8d1b38fd9dc)subnets

| struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) bt\_mesh\_cdb::subnets[0] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[cdb.h](cdb_8h_source.md)

- [bt\_mesh\_cdb](structbt__mesh__cdb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
