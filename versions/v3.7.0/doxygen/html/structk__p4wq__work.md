---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structk__p4wq__work.html
original_path: doxygen/html/structk__p4wq__work.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_p4wq\_work Struct Reference

P4 Queue Work Item.
[More...](#details)

`#include <[p4wq.h](p4wq_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [priority](#ac0420f86fea6302c6867d20705cda454) |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [deadline](#a7d841cb4cd18d0a61c0eac7dd448f61c) |
| [k\_p4wq\_handler\_t](p4wq_8h.md#aa164250d00319b0d71670e95201e45b0) | [handler](#ac1cc19646f95589ecfe8892c5666c5ef) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sync](#a11eaae7aa6447baf732cf9060fbf70a4) |
| struct k\_sem | [done\_sem](#a8dec82b6c03fab9316b7a96c99466920) |
| union { |  |
| struct [rbnode](structrbnode.md)   [rbnode](#a6f02066d7035d0ffbd570395a65411e5) |  |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)   [dlnode](#aadfa029b6833630ac9d4a3507452d278) |  |
| }; |  |
| struct [k\_thread](structk__thread.md) \* | [thread](#aa767524655c69e35ef284b6de9af1f46) |
| struct [k\_p4wq](structk__p4wq.md) \* | [queue](#ac1ceadaf2e64eb13b1c89f7fb47efc38) |

## Detailed Description

P4 Queue Work Item.

User-populated struct representing a single work item. The priority and deadline fields are interpreted as thread scheduling priorities, exactly as per [k\_thread\_priority\_set()](group__thread__apis.md#ga24e50a60c524d1eb22fe21cdf269b6a6 "Set a thread's priority.") and [k\_thread\_deadline\_set()](group__thread__apis.md#gad887f16c1dd6f3247682a83beb22d1ce "Set deadline expiration time for scheduler.").

## Field Documentation

## [◆ ](#ad18473676d08121326e0cd0293b95269)[union]

| union { ... } [k\_p4wq\_work](structk__p4wq__work.md) |
| --- |

## [◆ ](#a7d841cb4cd18d0a61c0eac7dd448f61c)deadline

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) k\_p4wq\_work::deadline |
| --- |

## [◆ ](#aadfa029b6833630ac9d4a3507452d278)dlnode

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) k\_p4wq\_work::dlnode |
| --- |

## [◆ ](#a8dec82b6c03fab9316b7a96c99466920)done\_sem

| struct k\_sem k\_p4wq\_work::done\_sem |
| --- |

## [◆ ](#ac1cc19646f95589ecfe8892c5666c5ef)handler

| [k\_p4wq\_handler\_t](p4wq_8h.md#aa164250d00319b0d71670e95201e45b0) k\_p4wq\_work::handler |
| --- |

## [◆ ](#ac0420f86fea6302c6867d20705cda454)priority

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) k\_p4wq\_work::priority |
| --- |

## [◆ ](#ac1ceadaf2e64eb13b1c89f7fb47efc38)queue

| struct [k\_p4wq](structk__p4wq.md)\* k\_p4wq\_work::queue |
| --- |

## [◆ ](#a6f02066d7035d0ffbd570395a65411e5)rbnode

| struct [rbnode](structrbnode.md) k\_p4wq\_work::rbnode |
| --- |

## [◆ ](#a11eaae7aa6447baf732cf9060fbf70a4)sync

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_p4wq\_work::sync |
| --- |

## [◆ ](#aa767524655c69e35ef284b6de9af1f46)thread

| struct [k\_thread](structk__thread.md)\* k\_p4wq\_work::thread |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[p4wq.h](p4wq_8h_source.md)

- [k\_p4wq\_work](structk__p4wq__work.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
