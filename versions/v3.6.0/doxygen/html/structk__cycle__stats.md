---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structk__cycle__stats.html
original_path: doxygen/html/structk__cycle__stats.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_cycle\_stats Struct Reference

Structure used to track internal statistics about both thread and CPU usage.
[More...](#details)

`#include <[stats.h](kernel_2stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [total](#a1d49158db605872cd8d31225c0ae8ab5) |
|  | total usage in cycles |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [track\_usage](#a8a955f987ddc88ff587edab8cb71dd6f) |
|  | true if gathering usage stats |
| Fields available when CONFIG\_SCHED\_THREAD\_USAGE\_ANALYSIS is selected. | |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [current](#a9c12b140936bcc4a8630c68680a245b4) |
|  | # of cycles in current usage window |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [longest](#a161c8d21c7d4a3d21c7cce87237c8334) |
|  | # of cycles in longest usage window |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num\_windows](#acdb6a6b005384535607aaf1bc5dd3feb) |
|  | # of usage windows |

## Detailed Description

Structure used to track internal statistics about both thread and CPU usage.

## Field Documentation

## [◆ ](#a9c12b140936bcc4a8630c68680a245b4)current

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) k\_cycle\_stats::current |
| --- |

# of cycles in current usage window

## [◆ ](#a161c8d21c7d4a3d21c7cce87237c8334)longest

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) k\_cycle\_stats::longest |
| --- |

# of cycles in longest usage window

## [◆ ](#acdb6a6b005384535607aaf1bc5dd3feb)num\_windows

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_cycle\_stats::num\_windows |
| --- |

# of usage windows

## [◆ ](#a1d49158db605872cd8d31225c0ae8ab5)total

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) k\_cycle\_stats::total |
| --- |

total usage in cycles

## [◆ ](#a8a955f987ddc88ff587edab8cb71dd6f)track\_usage

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_cycle\_stats::track\_usage |
| --- |

true if gathering usage stats

---

The documentation for this struct was generated from the following file:

- zephyr/kernel/[stats.h](kernel_2stats_8h_source.md)

- [k\_cycle\_stats](structk__cycle__stats.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
