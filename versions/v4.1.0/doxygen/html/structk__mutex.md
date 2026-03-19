---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__mutex.html
original_path: doxygen/html/structk__mutex.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_mutex Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Mutex APIs](group__mutex__apis.md)

Mutex Structure.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| \_wait\_q\_t | [wait\_q](#a4add234295bceff22551ee74f3aed802) |
|  | Mutex wait queue. |
| struct [k\_thread](structk__thread.md) \* | [owner](#af910bb07dc99e50078de26fccca468e4) |
|  | Mutex owner. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [lock\_count](#a0db401fc8e03e1f984b8fd15af974718) |
|  | Current lock count. |
| int | [owner\_orig\_prio](#ab0d16fac9f8af960a501ffd93ec08c80) |
|  | Original thread priority. |

## Detailed Description

Mutex Structure.

## Field Documentation

## [◆ ](#a0db401fc8e03e1f984b8fd15af974718)lock\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mutex::lock\_count |
| --- |

Current lock count.

## [◆ ](#af910bb07dc99e50078de26fccca468e4)owner

| struct [k\_thread](structk__thread.md)\* k\_mutex::owner |
| --- |

Mutex owner.

## [◆ ](#ab0d16fac9f8af960a501ffd93ec08c80)owner\_orig\_prio

| int k\_mutex::owner\_orig\_prio |
| --- |

Original thread priority.

## [◆ ](#a4add234295bceff22551ee74f3aed802)wait\_q

| \_wait\_q\_t k\_mutex::wait\_q |
| --- |

Mutex wait queue.

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_mutex](structk__mutex.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
