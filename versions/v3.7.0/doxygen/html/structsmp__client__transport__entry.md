---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsmp__client__transport__entry.html
original_path: doxygen/html/structsmp__client__transport__entry.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_client\_transport\_entry Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr transport SMP API](group__mcumgr__transport__smp.md)

SMP Client transport structure.
[More...](#details)

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#ad8ebd9f6bc7d322c51e6aecb2e926022) |
| struct [smp\_transport](structsmp__transport.md) \* | [smpt](#aebf774d7d0fe4eebe2e230a3680e0acf) |
|  | Transport structure pointer. |
| int | [smpt\_type](#a6a8a368d3db1f03b4e6774d4a86123c2) |
|  | Transport type. |

## Detailed Description

SMP Client transport structure.

## Field Documentation

## [◆ ](#ad8ebd9f6bc7d322c51e6aecb2e926022)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) smp\_client\_transport\_entry::node |
| --- |

## [◆ ](#aebf774d7d0fe4eebe2e230a3680e0acf)smpt

| struct [smp\_transport](structsmp__transport.md)\* smp\_client\_transport\_entry::smpt |
| --- |

Transport structure pointer.

## [◆ ](#a6a8a368d3db1f03b4e6774d4a86123c2)smpt\_type

| int smp\_client\_transport\_entry::smpt\_type |
| --- |

Transport type.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/transport/[smp.h](mgmt_2mcumgr_2transport_2smp_8h_source.md)

- [smp\_client\_transport\_entry](structsmp__client__transport__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
