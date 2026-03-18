---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structk__p4wq.html
original_path: doxygen/html/structk__p4wq.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_p4wq Struct Reference

P4 Queue.
[More...](#details)

`#include <[p4wq.h](p4wq_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#abb4af1223997eb31ae7a17f3a933fb19) |
| \_wait\_q\_t | [waitq](#a8cac5e806d2e432f50051db5a7d08c99) |
| struct [rbtree](structrbtree.md) | [queue](#aa36eb7d19dd3da5be7668aee5231edf6) |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [active](#afc1544bdca24633b3b30673686b93e9b) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a2f5cc7f74e4e46642ce3c5ef61555f94) |

## Detailed Description

P4 Queue.

Kernel pooled parallel preemptible priority-based work queue

## Field Documentation

## [◆ ](#afc1544bdca24633b3b30673686b93e9b)active

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) k\_p4wq::active |
| --- |

## [◆ ](#a2f5cc7f74e4e46642ce3c5ef61555f94)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_p4wq::flags |
| --- |

## [◆ ](#abb4af1223997eb31ae7a17f3a933fb19)lock

| struct [k\_spinlock](structk__spinlock.md) k\_p4wq::lock |
| --- |

## [◆ ](#aa36eb7d19dd3da5be7668aee5231edf6)queue

| struct [rbtree](structrbtree.md) k\_p4wq::queue |
| --- |

## [◆ ](#a8cac5e806d2e432f50051db5a7d08c99)waitq

| \_wait\_q\_t k\_p4wq::waitq |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[p4wq.h](p4wq_8h_source.md)

- [k\_p4wq](structk__p4wq.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
