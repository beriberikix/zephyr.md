---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsmp__transport.html
original_path: doxygen/html/structsmp__transport.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_transport Struct Reference

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md) » [MCUmgr transport SMP API](group__mcumgr__transport__smp.md)

SMP transport object for sending SMP responses.
[More...](#details)

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_work](structk__work.md) | [work](#a2bb0436ae57a1c1d084f3fed1aa16652) |
| struct [k\_fifo](structk__fifo.md) | [fifo](#a929ff7e97273dd18920ddc8426c6646f) |
| struct [smp\_transport\_api\_t](structsmp__transport__api__t.md) | [functions](#ab732e7d9574b78635a90ff559306daaa) |

## Detailed Description

SMP transport object for sending SMP responses.

## Field Documentation

## [◆ ](#a929ff7e97273dd18920ddc8426c6646f)fifo

| struct [k\_fifo](structk__fifo.md) smp\_transport::fifo |
| --- |

## [◆ ](#ab732e7d9574b78635a90ff559306daaa)functions

| struct [smp\_transport\_api\_t](structsmp__transport__api__t.md) smp\_transport::functions |
| --- |

## [◆ ](#a2bb0436ae57a1c1d084f3fed1aa16652)work

| struct [k\_work](structk__work.md) smp\_transport::work |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/transport/[smp.h](mgmt_2mcumgr_2transport_2smp_8h_source.md)

- [smp\_transport](structsmp__transport.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
