---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcan__mcan__std__filter.html
original_path: doxygen/html/structcan__mcan__std__filter.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan\_std\_filter Struct Reference

Bosch M\_CAN Standard Message ID Filter Element.
[More...](#details)

`#include <[can_mcan.h](can__mcan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sfid2](#a050f5018825d3afa350b35d101569f50): 11 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [res](#adb5bb096566c3fecf9727a800dbfe3cd): 5 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sfid1](#a7d80d641985ab67e09eb4d11015af2b3): 11 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sfec](#ad943ff357a00cca569f164599b9f49e5): 3 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sft](#afb89a40ac7c585c75d6bbaf3705e913a): 2 |

## Detailed Description

Bosch M\_CAN Standard Message ID Filter Element.

See Bosch M\_CAN Users Manual section 2.4.5 for details.

## Field Documentation

## [◆ ](#adb5bb096566c3fecf9727a800dbfe3cd)res

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_std\_filter::res |
| --- |

## [◆ ](#ad943ff357a00cca569f164599b9f49e5)sfec

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_std\_filter::sfec |
| --- |

## [◆ ](#a7d80d641985ab67e09eb4d11015af2b3)sfid1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_std\_filter::sfid1 |
| --- |

## [◆ ](#a050f5018825d3afa350b35d101569f50)sfid2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_std\_filter::sfid2 |
| --- |

## [◆ ](#afb89a40ac7c585c75d6bbaf3705e913a)sft

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_mcan\_std\_filter::sft |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_mcan.h](can__mcan_8h_source.md)

- [can\_mcan\_std\_filter](structcan__mcan__std__filter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
