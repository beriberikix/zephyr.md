---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structrtio__mpsc.html
original_path: doxygen/html/structrtio__mpsc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_mpsc Struct Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md) » [RTIO MPSC API](group__rtio__mpsc.md)

MPSC Queue.
[More...](#details)

`#include <[rtio_mpsc.h](rtio__mpsc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [mpsc\_ptr\_t](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626) | [head](#a428414dcd0cf037bb44a7adb2f5e457d) |
| struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \* | [tail](#a82dee3ba37c8299adb68aac527696398) |
| struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) | [stub](#a726de5d439073f63bf267788847bbfca) |

## Detailed Description

MPSC Queue.

## Field Documentation

## [◆ ](#a428414dcd0cf037bb44a7adb2f5e457d)head

| [mpsc\_ptr\_t](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626) rtio\_mpsc::head |
| --- |

## [◆ ](#a726de5d439073f63bf267788847bbfca)stub

| struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) rtio\_mpsc::stub |
| --- |

## [◆ ](#a82dee3ba37c8299adb68aac527696398)tail

| struct [rtio\_mpsc\_node](structrtio__mpsc__node.md)\* rtio\_mpsc::tail |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[rtio\_mpsc.h](rtio__mpsc_8h_source.md)

- [rtio\_mpsc](structrtio__mpsc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
