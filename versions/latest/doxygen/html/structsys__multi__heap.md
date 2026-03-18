---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsys__multi__heap.html
original_path: doxygen/html/structsys__multi__heap.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_multi\_heap Struct Reference

`#include <[multi_heap.h](multi__heap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [nheaps](#a3830f646e39d16401cfe75099e2facc1) |
| [sys\_multi\_heap\_fn\_t](multi__heap_8h.md#a2d8ac07e590ef36ba6f35ae88235564e) | [choice](#a01dd6ce40b1ab9c84c034475e70a4fa6) |
| struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) | [heaps](#a36be24709ad7083957a65aad6100806e) [8] |

## Field Documentation

## [◆ ](#a01dd6ce40b1ab9c84c034475e70a4fa6)choice

| [sys\_multi\_heap\_fn\_t](multi__heap_8h.md#a2d8ac07e590ef36ba6f35ae88235564e) sys\_multi\_heap::choice |
| --- |

## [◆ ](#a36be24709ad7083957a65aad6100806e)heaps

| struct [sys\_multi\_heap\_rec](structsys__multi__heap__rec.md) sys\_multi\_heap::heaps[8] |
| --- |

## [◆ ](#a3830f646e39d16401cfe75099e2facc1)nheaps

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sys\_multi\_heap::nheaps |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[multi\_heap.h](multi__heap_8h_source.md)

- [sys\_multi\_heap](structsys__multi__heap.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
