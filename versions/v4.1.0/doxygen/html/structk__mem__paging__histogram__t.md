---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__mem__paging__histogram__t.html
original_path: doxygen/html/structk__mem__paging__histogram__t.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_mem\_paging\_histogram\_t Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Kernel Memory Management](group__kernel__memory__management.md) » [Demand Paging](group__demand__paging.md) » [Demand Paging APIs](group__mem-demand-paging.md)

Paging Statistics Histograms.
[More...](#details)

`#include <[demand_paging.h](demand__paging_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [counts](#a4421676cbc9f6c63808ee914e2ff8c90) [CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM\_NUM\_BINS] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [bounds](#a893236502aeb56975263b27cf4f2755a) [CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM\_NUM\_BINS] |

## Detailed Description

Paging Statistics Histograms.

## Field Documentation

## [◆ ](#a893236502aeb56975263b27cf4f2755a)bounds

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long k\_mem\_paging\_histogram\_t::bounds[CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM\_NUM\_BINS] |
| --- |

## [◆ ](#a4421676cbc9f6c63808ee914e2ff8c90)counts

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long k\_mem\_paging\_histogram\_t::counts[CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM\_NUM\_BINS] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/kernel/mm/[demand\_paging.h](demand__paging_8h_source.md)

- [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
