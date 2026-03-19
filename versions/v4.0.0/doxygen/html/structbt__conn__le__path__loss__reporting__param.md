---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__le__path__loss__reporting__param.html
original_path: doxygen/html/structbt__conn__le__path__loss__reporting__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_path\_loss\_reporting\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

LE Path Loss Monitoring Parameters Structure as defined in Core Spec.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [high\_threshold](#a5cc7a17efee69d61b8f8d0c242321054) |
|  | High threshold for the path loss (dB). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [high\_hysteresis](#aec49adc896604d878060b03bd40ab0f4) |
|  | Hysteresis value for the high threshold (dB). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [low\_threshold](#a634c08e573cffd97a94ad681bed9239e) |
|  | Low threshold for the path loss (dB). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [low\_hysteresis](#af8e70508a39ee73b75a4769769aa303f) |
|  | Hysteresis value for the low threshold (dB). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [min\_time\_spent](#a6fec4497c6fd95fa6f265bd859976c9d) |
|  | Minimum time in number of connection events to be observed once the path loss crosses the threshold before an event is generated. |

## Detailed Description

LE Path Loss Monitoring Parameters Structure as defined in Core Spec.

Version 5.4 Vol.4, Part E, 7.8.119 LE Set Path Loss Reporting Parameters command.

## Field Documentation

## [◆ ](#aec49adc896604d878060b03bd40ab0f4)high\_hysteresis

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_path\_loss\_reporting\_param::high\_hysteresis |
| --- |

Hysteresis value for the high threshold (dB).

## [◆ ](#a5cc7a17efee69d61b8f8d0c242321054)high\_threshold

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_path\_loss\_reporting\_param::high\_threshold |
| --- |

High threshold for the path loss (dB).

## [◆ ](#af8e70508a39ee73b75a4769769aa303f)low\_hysteresis

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_path\_loss\_reporting\_param::low\_hysteresis |
| --- |

Hysteresis value for the low threshold (dB).

## [◆ ](#a634c08e573cffd97a94ad681bed9239e)low\_threshold

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_conn\_le\_path\_loss\_reporting\_param::low\_threshold |
| --- |

Low threshold for the path loss (dB).

## [◆ ](#a6fec4497c6fd95fa6f265bd859976c9d)min\_time\_spent

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_path\_loss\_reporting\_param::min\_time\_spent |
| --- |

Minimum time in number of connection events to be observed once the path loss crosses the threshold before an event is generated.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_path\_loss\_reporting\_param](structbt__conn__le__path__loss__reporting__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
