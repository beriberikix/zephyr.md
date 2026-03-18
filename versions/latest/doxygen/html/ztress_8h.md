---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ztress_8h.html
original_path: doxygen/html/ztress_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztress.h File Reference

Zephyr testing framework ztress macros.
[More...](#details)

`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`

[Go to the source code of this file.](ztress_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ztress\_context\_data](structztress__context__data.md) |

| Macros | |
| --- | --- |
| #define | [ZTRESS\_ID\_THREAD](#a8752d529cfc4d77b1dd71c4572fd63c3)   0 |
| #define | [ZTRESS\_ID\_K\_TIMER](#a937803e1398db7d0e10ea60c9c9ef642)   1 |
| #define | [ZTRESS\_TIMER](group__ztest__ztress.md#gabab05b8db44a7024ce23cb34bf999e42)(handler, user\_data, exec\_cnt, init\_timeout) |
|  | Descriptor of a k\_timer handler execution context. |
| #define | [ZTRESS\_THREAD](group__ztest__ztress.md#gaed561641541e8ced6866f2f1227f21c0)(handler, user\_data, exec\_cnt, preempt\_cnt, init\_timeout) |
|  | Descriptor of a thread execution context. |
| #define | [ZTRESS\_CONTEXT\_INITIALIZER](group__ztest__ztress.md#gab5e8bbcecd77db06e7a90631fc0c202b)(\_handler, \_user\_data, \_exec\_cnt, \_preempt\_cnt, \_t) |
|  | Initialize context structure. |
| #define | [ZTRESS\_EXECUTE](group__ztest__ztress.md#ga6acc3a50e0eff7360873006482f5c8e9)(...) |
|  | Setup and run stress test. |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [ztress\_handler](group__ztest__ztress.md#ga633439263754bf08baee06c37dddab40)) (void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last, int prio) |
|  | User handler called in one of the configured contexts. |

| Functions | |
| --- | --- |
| int | [ztress\_execute](group__ztest__ztress.md#gaf706f1af4c42f5925d7545dadf5548fd) (struct [ztress\_context\_data](structztress__context__data.md) \*timer\_data, struct [ztress\_context\_data](structztress__context__data.md) \*thread\_data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cnt) |
|  | Execute contexts. |
| void | [ztress\_abort](group__ztest__ztress.md#ga57f171e230fba462b3dea6b2d3cf71f6) (void) |
|  | Abort ongoing stress test. |
| void | [ztress\_set\_timeout](group__ztest__ztress.md#ga5b3069bb2aa35ddc64c46c18d2e30091) ([k\_timeout\_t](structk__timeout__t.md) t) |
|  | Set test timeout. |
| void | [ztress\_report](group__ztest__ztress.md#gaf4db2092eee17d863c9810333ba4c870) (void) |
|  | Print last test report. |
| int | [ztress\_exec\_count](group__ztest__ztress.md#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Get number of executions of a given context in the last test. |
| int | [ztress\_preempt\_count](group__ztest__ztress.md#ga4406b828d170bc19065aaf65aeb4613e) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Get number of preemptions of a given context in the last test. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ztress\_optimized\_ticks](group__ztest__ztress.md#gacbbdb8e7bad532d6dd20c486b3256e21) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id) |
|  | Get optimized timeout base of a given context in the last test. |

## Detailed Description

Zephyr testing framework ztress macros.

## Macro Definition Documentation

## [◆ ](#a937803e1398db7d0e10ea60c9c9ef642)ZTRESS\_ID\_K\_TIMER

| #define ZTRESS\_ID\_K\_TIMER   1 |
| --- |

## [◆ ](#a8752d529cfc4d77b1dd71c4572fd63c3)ZTRESS\_ID\_THREAD

| #define ZTRESS\_ID\_THREAD   0 |
| --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztress.h](ztress_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
