---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structosdp__cmd__led__params.html
original_path: doxygen/html/structosdp__cmd__led__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_cmd\_led\_params Struct Reference

LED params sub-structure.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [control\_code](#ae95e3b87bbccd7d9897fef329001ce39) |
|  | Control code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [on\_count](#adde9dfdd167d9dfc122b56cf5e47b10f) |
|  | The ON duration of the flash, in units of 100 ms. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [off\_count](#a278ff380c2ab7d9c83b55aa49b3137cb) |
|  | The OFF duration of the flash, in units of 100 ms. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [on\_color](#a80b47a4c55494d7062c4a83fd81b0910) |
|  | Color to set during the ON timer (see [osdp\_led\_color\_e](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84e "osdp_led_color_e")). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [off\_color](#ac6f1c1269697fcab96b6f68d62381ded) |
|  | Color to set during the OFF timer (see [osdp\_led\_color\_e](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84e "osdp_led_color_e")). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timer\_count](#a002de25cd5070cb96e90ccd0d2091216) |
|  | Time in units of 100 ms (only for temporary mode). |

## Detailed Description

LED params sub-structure.

Part of LED command. See [osdp\_cmd\_led](structosdp__cmd__led.md "osdp_cmd_led").

## Field Documentation

## [◆ ](#ae95e3b87bbccd7d9897fef329001ce39)control\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_led\_params::control\_code |
| --- |

Control code.

Temporary Control Code:

- 0 - NOP - do not alter this LED's temporary settings.
- 1 - Cancel any temporary operation and display this LED's permanent state immediately.
- 2 - Set the temporary state as given and start timer immediately.

Permanent Control Code:

- 0 - NOP - do not alter this LED's permanent settings.
- 1 - Set the permanent state as given.

## [◆ ](#ac6f1c1269697fcab96b6f68d62381ded)off\_color

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_led\_params::off\_color |
| --- |

Color to set during the OFF timer (see [osdp\_led\_color\_e](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84e "osdp_led_color_e")).

## [◆ ](#a278ff380c2ab7d9c83b55aa49b3137cb)off\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_led\_params::off\_count |
| --- |

The OFF duration of the flash, in units of 100 ms.

## [◆ ](#a80b47a4c55494d7062c4a83fd81b0910)on\_color

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_led\_params::on\_color |
| --- |

Color to set during the ON timer (see [osdp\_led\_color\_e](osdp_8h.md#a97ee0d8eb19e4e37ac89b2b6d338b84e "osdp_led_color_e")).

## [◆ ](#adde9dfdd167d9dfc122b56cf5e47b10f)on\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_led\_params::on\_count |
| --- |

The ON duration of the flash, in units of 100 ms.

## [◆ ](#a002de25cd5070cb96e90ccd0d2091216)timer\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) osdp\_cmd\_led\_params::timer\_count |
| --- |

Time in units of 100 ms (only for temporary mode).

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_cmd\_led\_params](structosdp__cmd__led__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
