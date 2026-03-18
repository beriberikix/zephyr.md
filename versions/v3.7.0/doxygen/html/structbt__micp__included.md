---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__micp__included.html
original_path: doxygen/html/structbt__micp__included.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_micp\_included Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Microphone Control Profile (MICP)](group__bt__gatt__micp.md)

Microphone Control Profile included services.
[More...](#details)

`#include <[micp.h](micp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [aics\_cnt](#a32cff1b68d96319958eeba66f249cd67) |
|  | Number of Audio Input Control Service instances. |
| struct bt\_aics \*\* | [aics](#a2afddd15bd726039682151038b2415d1) |
|  | Array of pointers to Audio Input Control Service instances. |

## Detailed Description

Microphone Control Profile included services.

Used for to represent the Microphone Control Profile included service instances, for either a Microphone Controller or a Microphone Device. The instance pointers either represent local service instances, or remote service instances.

## Field Documentation

## [◆ ](#a2afddd15bd726039682151038b2415d1)aics

| struct bt\_aics\*\* bt\_micp\_included::aics |
| --- |

Array of pointers to Audio Input Control Service instances.

## [◆ ](#a32cff1b68d96319958eeba66f249cd67)aics\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_micp\_included::aics\_cnt |
| --- |

Number of Audio Input Control Service instances.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[micp.h](micp_8h_source.md)

- [bt\_micp\_included](structbt__micp__included.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
