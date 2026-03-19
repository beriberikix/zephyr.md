---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__br__discovery__result.html
original_path: doxygen/html/structbt__br__discovery__result.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_br\_discovery\_result Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

BR/EDR discovery result structure.
[More...](#details)

`#include <[classic.h](classic_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_t](structbt__addr__t.md) | [addr](#a833b05883132a0c20690f71b2c14a62a) |
|  | Remote device address. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#ad1f6bbfc27796e998ed30e307a251841) |
|  | RSSI from inquiry. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cod](#aec239cbb82436ace39c8928a3baa0cf6) [3] |
|  | Class of Device. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [eir](#a6bfe9a421257e2460eb9b4381252f9cc) [240] |
|  | Extended Inquiry Response. |

## Detailed Description

BR/EDR discovery result structure.

## Field Documentation

## [◆ ](#a833b05883132a0c20690f71b2c14a62a)addr

| [bt\_addr\_t](structbt__addr__t.md) bt\_br\_discovery\_result::addr |
| --- |

Remote device address.

## [◆ ](#aec239cbb82436ace39c8928a3baa0cf6)cod

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_br\_discovery\_result::cod[3] |
| --- |

Class of Device.

## [◆ ](#a6bfe9a421257e2460eb9b4381252f9cc)eir

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_br\_discovery\_result::eir[240] |
| --- |

Extended Inquiry Response.

## [◆ ](#ad1f6bbfc27796e998ed30e307a251841)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_br\_discovery\_result::rssi |
| --- |

RSSI from inquiry.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[classic.h](classic_8h_source.md)

- [bt\_br\_discovery\_result](structbt__br__discovery__result.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
