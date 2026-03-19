---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__vcp__included.html
original_path: doxygen/html/structbt__vcp__included.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_vcp\_included Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Volume Control Profile (VCP)](group__bt__vcp.md)

Volume Control Service included services.
[More...](#details)

`#include <[vcp.h](vcp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [vocs\_cnt](#acb0c8e853808adfd9c3b92b45e874103) |
|  | Number of Volume Offset Control Service instances. |
| struct bt\_vocs \*\* | [vocs](#a1f04068dd88d2fecef5fd78a3c7d4429) |
|  | Array of pointers to Volume Offset Control Service instances. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [aics\_cnt](#af521bb12ebef4c5f60609040140474c0) |
|  | Number of Audio Input Control Service instances. |
| struct bt\_aics \*\* | [aics](#aa6c87b8c9b4b2be6ec6429fd2ee68398) |
|  | Array of pointers to Audio Input Control Service instances. |

## Detailed Description

Volume Control Service included services.

Used for to represent the Volume Control Service included service instances, for either a client or a server. The instance pointers either represent local server instances, or remote service instances.

## Field Documentation

## [◆ ](#aa6c87b8c9b4b2be6ec6429fd2ee68398)aics

| struct bt\_aics\*\* bt\_vcp\_included::aics |
| --- |

Array of pointers to Audio Input Control Service instances.

## [◆ ](#af521bb12ebef4c5f60609040140474c0)aics\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_vcp\_included::aics\_cnt |
| --- |

Number of Audio Input Control Service instances.

## [◆ ](#a1f04068dd88d2fecef5fd78a3c7d4429)vocs

| struct bt\_vocs\*\* bt\_vcp\_included::vocs |
| --- |

Array of pointers to Volume Offset Control Service instances.

## [◆ ](#acb0c8e853808adfd9c3b92b45e874103)vocs\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_vcp\_included::vocs\_cnt |
| --- |

Number of Volume Offset Control Service instances.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[vcp.h](vcp_8h_source.md)

- [bt\_vcp\_included](structbt__vcp__included.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
