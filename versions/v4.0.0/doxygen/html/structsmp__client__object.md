---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsmp__client__object.html
original_path: doxygen/html/structsmp__client__object.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_client\_object Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [SMP client API](group__mcumgr__smp__client.md)

SMP client object.
[More...](#details)

`#include <[smp_client.h](smp__client_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_work](structk__work.md) | [work](#ae4c73b23b90ef9f6cb8a93efde992c8a) |
|  | Must be the first member. |
| struct [k\_fifo](structk__fifo.md) | [tx\_fifo](#a5d3cf1e109692112bf52b0b8514bab9f) |
|  | FIFO for client TX queue. |
| struct [smp\_transport](structsmp__transport.md) \* | [smpt](#a01507d6fa5a75751b39ccda82d0836ef) |
|  | SMP transport object. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [smp\_seq](#a0de9e7ee538b84cf1a6065b7b8b0bc53) |
|  | SMP SEQ. |

## Detailed Description

SMP client object.

## Field Documentation

## [◆ ](#a0de9e7ee538b84cf1a6065b7b8b0bc53)smp\_seq

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) smp\_client\_object::smp\_seq |
| --- |

SMP SEQ.

## [◆ ](#a01507d6fa5a75751b39ccda82d0836ef)smpt

| struct [smp\_transport](structsmp__transport.md)\* smp\_client\_object::smpt |
| --- |

SMP transport object.

## [◆ ](#a5d3cf1e109692112bf52b0b8514bab9f)tx\_fifo

| struct [k\_fifo](structk__fifo.md) smp\_client\_object::tx\_fifo |
| --- |

FIFO for client TX queue.

## [◆ ](#ae4c73b23b90ef9f6cb8a93efde992c8a)work

| struct [k\_work](structk__work.md) smp\_client\_object::work |
| --- |

Must be the first member.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/smp/[smp\_client.h](smp__client_8h_source.md)

- [smp\_client\_object](structsmp__client__object.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
