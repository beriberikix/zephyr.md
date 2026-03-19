---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__work__delayable.html
original_path: doxygen/html/structk__work__delayable.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_work\_delayable Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Work Queue APIs](group__workqueue__apis.md)

A structure used to submit work after a delay.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_work](structk__work.md) | [work](#a594ad30acf08249909c30c0af76c1629) |
| struct \_timeout | [timeout](#a1db9148a05731100d3d3915534ac2d4d) |
| struct [k\_work\_q](structk__work__q.md) \* | [queue](#a25dc6aaf1713e1db0f2530370afd4dc4) |

## Detailed Description

A structure used to submit work after a delay.

## Field Documentation

## [◆ ](#a25dc6aaf1713e1db0f2530370afd4dc4)queue

| struct [k\_work\_q](structk__work__q.md)\* k\_work\_delayable::queue |
| --- |

## [◆ ](#a1db9148a05731100d3d3915534ac2d4d)timeout

| struct \_timeout k\_work\_delayable::timeout |
| --- |

## [◆ ](#a594ad30acf08249909c30c0af76c1629)work

| struct [k\_work](structk__work.md) k\_work\_delayable::work |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_work\_delayable](structk__work__delayable.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
