---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structk__mem__domain.html
original_path: doxygen/html/structk__mem__domain.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_mem\_domain Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Memory domain APIs](group__mem__domain__apis.md)

Memory Domain.
[More...](#details)

`#include <[mem_domain.h](mem__domain_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_mem\_partition](structk__mem__partition.md) | [partitions](#a48cbffd5f2e85bee1b4b5b02b753980e) [CONFIG\_MAX\_DOMAIN\_PARTITIONS] |
|  | partitions in the domain |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [mem\_domain\_q](#afc3d3a778e84fe98d778f548d707929a) |
|  | Doubly linked list of member threads. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_partitions](#abc876ea435863315f66631e28e49ab8a) |
|  | number of active partitions in the domain |

## Detailed Description

Memory Domain.

A memory domain is a collection of memory partitions, used to represent a user thread's access policy for the linear address space. A thread may be a member of only one memory domain, but any memory domain may have multiple threads that are members.

Supervisor threads may also be a member of a memory domain; this has no implications on their memory access but can be useful as any child threads inherit the memory domain membership of the parent.

A user thread belonging to a memory domain with no active partitions will have guaranteed access to its own stack buffer, program text, and read-only data.

## Field Documentation

## [◆ ](#afc3d3a778e84fe98d778f548d707929a)mem\_domain\_q

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) k\_mem\_domain::mem\_domain\_q |
| --- |

Doubly linked list of member threads.

## [◆ ](#abc876ea435863315f66631e28e49ab8a)num\_partitions

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k\_mem\_domain::num\_partitions |
| --- |

number of active partitions in the domain

## [◆ ](#a48cbffd5f2e85bee1b4b5b02b753980e)partitions

| struct [k\_mem\_partition](structk__mem__partition.md) k\_mem\_domain::partitions[CONFIG\_MAX\_DOMAIN\_PARTITIONS] |
| --- |

partitions in the domain

---

The documentation for this struct was generated from the following file:

- zephyr/app\_memory/[mem\_domain.h](mem__domain_8h_source.md)

- [k\_mem\_domain](structk__mem__domain.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
