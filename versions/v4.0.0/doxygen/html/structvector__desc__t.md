---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structvector__desc__t.html
original_path: doxygen/html/structvector__desc__t.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vector\_desc\_t Struct Reference

`#include <[intc_esp32.h](intc__esp32_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [flags](#a08740a5225fef571398bbd91a42fc970): 16 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [cpu](#a853c50cd06725b9502fa14af262d76b9): 1 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [intno](#a74e81e89da2ca79df99911d0599e5f77): 5 |
| int | [source](#a8adcec0946b8790de75af65a6ae03ccc): 8 |
| struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md) \* | [shared\_vec\_info](#a9934f0a683b6f2145ce35a395a65b967) |
| struct [vector\_desc\_t](structvector__desc__t.md) \* | [next](#a4b3b6db584511e25407e187d4dbf6ac8) |

## Field Documentation

## [◆ ](#a853c50cd06725b9502fa14af262d76b9)cpu

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int vector\_desc\_t::cpu |
| --- |

## [◆ ](#a08740a5225fef571398bbd91a42fc970)flags

| int vector\_desc\_t::flags |
| --- |

## [◆ ](#a74e81e89da2ca79df99911d0599e5f77)intno

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int vector\_desc\_t::intno |
| --- |

## [◆ ](#a4b3b6db584511e25407e187d4dbf6ac8)next

| struct [vector\_desc\_t](structvector__desc__t.md)\* vector\_desc\_t::next |
| --- |

## [◆ ](#a9934f0a683b6f2145ce35a395a65b967)shared\_vec\_info

| struct [shared\_vector\_desc\_t](structshared__vector__desc__t.md)\* vector\_desc\_t::shared\_vec\_info |
| --- |

## [◆ ](#a8adcec0946b8790de75af65a6ae03ccc)source

| int vector\_desc\_t::source |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/interrupt\_controller/[intc\_esp32.h](intc__esp32_8h_source.md)

- [vector\_desc\_t](structvector__desc__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
