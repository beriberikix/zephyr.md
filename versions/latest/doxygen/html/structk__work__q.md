---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structk__work__q.html
original_path: doxygen/html/structk__work__q.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_work\_q Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Work Queue APIs](group__workqueue__apis.md)

A structure used to hold work until it can be processed.
[More...](#details)

`#include <[kernel.h](include_2zephyr_2kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_thread](structk__thread.md) | [thread](#aa42ca271a4989f129bf1a43c491327eb) |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [pending](#a2012199571f6b658873550d64386b00c) |
| \_wait\_q\_t | [notifyq](#a561c90f8bb944217230e00052cdecf10) |
| \_wait\_q\_t | [drainq](#a308d1ac78b1203b7ea78b0f18c5bdf5b) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a68bc8e9c412ebdbf34827087d91a080e) |

## Detailed Description

A structure used to hold work until it can be processed.

## Field Documentation

## [◆ ](#a308d1ac78b1203b7ea78b0f18c5bdf5b)drainq

| \_wait\_q\_t k\_work\_q::drainq |
| --- |

## [◆ ](#a68bc8e9c412ebdbf34827087d91a080e)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_work\_q::flags |
| --- |

## [◆ ](#a561c90f8bb944217230e00052cdecf10)notifyq

| \_wait\_q\_t k\_work\_q::notifyq |
| --- |

## [◆ ](#a2012199571f6b658873550d64386b00c)pending

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) k\_work\_q::pending |
| --- |

## [◆ ](#aa42ca271a4989f129bf1a43c491327eb)thread

| struct [k\_thread](structk__thread.md) k\_work\_q::thread |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](include_2zephyr_2kernel_8h_source.md)

- [k\_work\_q](structk__work__q.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
