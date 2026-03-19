---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structosdp__cmd__led.html
original_path: doxygen/html/structosdp__cmd__led.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_cmd\_led Struct Reference

Sent from CP to PD to control the behaviour of it's on-board LEDs.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reader](#afe5e061d91fda9f008b5f8e5441df467) |
|  | Reader number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [led\_number](#ae4ff10389198d00047ffa2a7ec7d15ac) |
|  | LED number. |
| struct [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md) | [temporary](#a2130237d1b79ee36c5f5087cdec7acfb) |
|  | Ephemeral LED status descriptor. |
| struct [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md) | [permanent](#a033fd34a88b03d22a088bd7d2676efb5) |
|  | Permanent LED status descriptor. |

## Detailed Description

Sent from CP to PD to control the behaviour of it's on-board LEDs.

## Field Documentation

## [◆ ](#ae4ff10389198d00047ffa2a7ec7d15ac)led\_number

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_led::led\_number |
| --- |

LED number.

0 = first LED, 1 = second LED, etc.

## [◆ ](#a033fd34a88b03d22a088bd7d2676efb5)permanent

| struct [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md) osdp\_cmd\_led::permanent |
| --- |

Permanent LED status descriptor.

## [◆ ](#afe5e061d91fda9f008b5f8e5441df467)reader

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_led::reader |
| --- |

Reader number.

0 = First Reader, 1 = Second Reader, etc.

## [◆ ](#a2130237d1b79ee36c5f5087cdec7acfb)temporary

| struct [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md) osdp\_cmd\_led::temporary |
| --- |

Ephemeral LED status descriptor.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_cmd\_led](structosdp__cmd__led.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
