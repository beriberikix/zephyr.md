---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h.html
original_path: doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

it8xxx2\_vcmp.h File Reference

[Go to the source code of this file.](dt-bindings_2sensor_2it8xxx2__vcmp_8h_source.md)

| Macros | |
| --- | --- |
| it8xxx2 voltage comparator channel references | |
| #define | [VCMP\_CHANNEL\_0](#a04c6b4af3a7fa2c266f9bc4cf8f580f8)   0 |
| #define | [VCMP\_CHANNEL\_1](#ab284eddb8412223f865380f69311884c)   1 |
| #define | [VCMP\_CHANNEL\_2](#abf666272da5df739c38349f8dc0673d7)   2 |
| #define | [VCMP\_CHANNEL\_3](#aad5d65c9659dedf702b54d8a7d3857ea)   3 |
| #define | [VCMP\_CHANNEL\_4](#a3148e4a63af5791c0d88e3ede54c1443)   4 |
| #define | [VCMP\_CHANNEL\_5](#a1460631599e37050e844032297578d2c)   5 |
| #define | [VCMP\_CHANNEL\_CNT](#ad7d3ef8e2a0157c43c68ef12f02b6181)   6 |
| it8xxx2 voltage comparator scan period for "all comparator channel" | |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_100US](#afee8d841314119709484eeb1a7919fc4)   0x10 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_200US](#ac22de93d09665b40b736f638bb106143)   0x20 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_400US](#ac4cd52baa765f7f9e148f49e3a5eb137)   0x30 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_600US](#a3e98391265d430652e996798979d6e32)   0x40 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_800US](#ace0bbf4e49fe2e939926c8973b1d9e6c)   0x50 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_1MS](#add00ffb6d51398fb9207d9709d35f294)   0x60 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_1\_5MS](#a1aa53f56577acc7cbd34f9f37d166e7c)   0x70 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_2MS](#a012e4fcc993d9aed16203e1cdbbeca05)   0x80 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_2\_5MS](#aa702079843ff113a79589c6daca88587)   0x90 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_3MS](#aad950cc6bec74a685ec3d37f451e1a10)   0xa0 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_4MS](#a4f296f81c2a751d53977abf2aff5d6dd)   0xb0 |
| #define | [IT8XXX2\_VCMP\_SCAN\_PERIOD\_5MS](#a7c31ca003dc472e5e567c6274f62dceb)   0xc0 |
| it8xxx2 voltage comparator interrupt trigger mode | |
| #define | [IT8XXX2\_VCMP\_LESS\_OR\_EQUAL](#a46e65d3ca651e9a75d90d0d456e6bc28)   0 |
| #define | [IT8XXX2\_VCMP\_GREATER](#a2f1ccc3b8b3d0ff5b1fab7d401adb2c7)   1 |
| #define | [IT8XXX2\_VCMP\_UNDEFINED](#ac54b4d008105b4d2ad956cf076c29acc)   0xffff |

## Macro Definition Documentation

## [◆ ](#a2f1ccc3b8b3d0ff5b1fab7d401adb2c7)IT8XXX2\_VCMP\_GREATER

| #define IT8XXX2\_VCMP\_GREATER   1 |
| --- |

## [◆ ](#a46e65d3ca651e9a75d90d0d456e6bc28)IT8XXX2\_VCMP\_LESS\_OR\_EQUAL

| #define IT8XXX2\_VCMP\_LESS\_OR\_EQUAL   0 |
| --- |

## [◆ ](#afee8d841314119709484eeb1a7919fc4)IT8XXX2\_VCMP\_SCAN\_PERIOD\_100US

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_100US   0x10 |
| --- |

## [◆ ](#a1aa53f56577acc7cbd34f9f37d166e7c)IT8XXX2\_VCMP\_SCAN\_PERIOD\_1\_5MS

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_1\_5MS   0x70 |
| --- |

## [◆ ](#add00ffb6d51398fb9207d9709d35f294)IT8XXX2\_VCMP\_SCAN\_PERIOD\_1MS

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_1MS   0x60 |
| --- |

## [◆ ](#ac22de93d09665b40b736f638bb106143)IT8XXX2\_VCMP\_SCAN\_PERIOD\_200US

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_200US   0x20 |
| --- |

## [◆ ](#aa702079843ff113a79589c6daca88587)IT8XXX2\_VCMP\_SCAN\_PERIOD\_2\_5MS

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_2\_5MS   0x90 |
| --- |

## [◆ ](#a012e4fcc993d9aed16203e1cdbbeca05)IT8XXX2\_VCMP\_SCAN\_PERIOD\_2MS

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_2MS   0x80 |
| --- |

## [◆ ](#aad950cc6bec74a685ec3d37f451e1a10)IT8XXX2\_VCMP\_SCAN\_PERIOD\_3MS

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_3MS   0xa0 |
| --- |

## [◆ ](#ac4cd52baa765f7f9e148f49e3a5eb137)IT8XXX2\_VCMP\_SCAN\_PERIOD\_400US

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_400US   0x30 |
| --- |

## [◆ ](#a4f296f81c2a751d53977abf2aff5d6dd)IT8XXX2\_VCMP\_SCAN\_PERIOD\_4MS

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_4MS   0xb0 |
| --- |

## [◆ ](#a7c31ca003dc472e5e567c6274f62dceb)IT8XXX2\_VCMP\_SCAN\_PERIOD\_5MS

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_5MS   0xc0 |
| --- |

## [◆ ](#a3e98391265d430652e996798979d6e32)IT8XXX2\_VCMP\_SCAN\_PERIOD\_600US

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_600US   0x40 |
| --- |

## [◆ ](#ace0bbf4e49fe2e939926c8973b1d9e6c)IT8XXX2\_VCMP\_SCAN\_PERIOD\_800US

| #define IT8XXX2\_VCMP\_SCAN\_PERIOD\_800US   0x50 |
| --- |

## [◆ ](#ac54b4d008105b4d2ad956cf076c29acc)IT8XXX2\_VCMP\_UNDEFINED

| #define IT8XXX2\_VCMP\_UNDEFINED   0xffff |
| --- |

## [◆ ](#a04c6b4af3a7fa2c266f9bc4cf8f580f8)VCMP\_CHANNEL\_0

| #define VCMP\_CHANNEL\_0   0 |
| --- |

## [◆ ](#ab284eddb8412223f865380f69311884c)VCMP\_CHANNEL\_1

| #define VCMP\_CHANNEL\_1   1 |
| --- |

## [◆ ](#abf666272da5df739c38349f8dc0673d7)VCMP\_CHANNEL\_2

| #define VCMP\_CHANNEL\_2   2 |
| --- |

## [◆ ](#aad5d65c9659dedf702b54d8a7d3857ea)VCMP\_CHANNEL\_3

| #define VCMP\_CHANNEL\_3   3 |
| --- |

## [◆ ](#a3148e4a63af5791c0d88e3ede54c1443)VCMP\_CHANNEL\_4

| #define VCMP\_CHANNEL\_4   4 |
| --- |

## [◆ ](#a1460631599e37050e844032297578d2c)VCMP\_CHANNEL\_5

| #define VCMP\_CHANNEL\_5   5 |
| --- |

## [◆ ](#ad7d3ef8e2a0157c43c68ef12f02b6181)VCMP\_CHANNEL\_CNT

| #define VCMP\_CHANNEL\_CNT   6 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [it8xxx2\_vcmp.h](dt-bindings_2sensor_2it8xxx2__vcmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
