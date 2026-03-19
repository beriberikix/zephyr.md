---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcan__bus__err__cnt.html
original_path: doxygen/html/structcan__bus__err__cnt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_bus\_err\_cnt Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [CAN Interface](group__can__interface.md)

CAN controller error counters.
[More...](#details)

`#include <[can.h](drivers_2can_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_err\_cnt](#a01bb2cb16656d0fd4f99cfbfa1f30e98) |
|  | Value of the CAN controller transmit error counter. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_err\_cnt](#a6be6ce6b592641ba0dce36fe1cd8902a) |
|  | Value of the CAN controller receive error counter. |

## Detailed Description

CAN controller error counters.

## Field Documentation

## [◆ ](#a6be6ce6b592641ba0dce36fe1cd8902a)rx\_err\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_bus\_err\_cnt::rx\_err\_cnt |
| --- |

Value of the CAN controller receive error counter.

## [◆ ](#a01bb2cb16656d0fd4f99cfbfa1f30e98)tx\_err\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_bus\_err\_cnt::tx\_err\_cnt |
| --- |

Value of the CAN controller transmit error counter.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[can.h](drivers_2can_8h_source.md)

- [can\_bus\_err\_cnt](structcan__bus__err__cnt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
