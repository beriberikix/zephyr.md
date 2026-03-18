---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unioncharger__propval.html
original_path: doxygen/html/unioncharger__propval.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

charger\_propval Union Reference

[Device Driver APIs](group__io__interfaces.md) » [Charger Interface](group__charger__interface.md)

container for a [charger\_property](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7 "Runtime Dynamic Battery Parameters.") value
[More...](#details)

`#include <[charger.h](charger_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) | [online](#a8589124e6152b70b649788a8b94461ab) |
|  | CHARGER\_PROP\_ONLINE. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [present](#ab0eec508b90d205a1662fd6c69638764) |
|  | CHARGER\_PROP\_PRESENT. |
| enum [charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) | [status](#a7f4976d72d4a7d48385ceb9f18c510b5) |
|  | CHARGER\_PROP\_STATUS. |
| enum [charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803) | [charge\_type](#ac1a594de2b1c10d28b6a81dd66f1a6ba) |
|  | CHARGER\_PROP\_CHARGE\_TYPE. |
| enum [charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412) | [health](#abd990f67423424da60856f4b6e8824a3) |
|  | CHARGER\_PROP\_HEALTH. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [const\_charge\_current\_ua](#af4e383bb797432033050937740ce0ac3) |
|  | CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [precharge\_current\_ua](#a24a97e16505fa336bd3a68743d05936b) |
|  | CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [charge\_term\_current\_ua](#a89d0c93d68650cefe29e891f4db928f4) |
|  | CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [const\_charge\_voltage\_uv](#a733bae9ce0bf7e902f8af307f94a356c) |
|  | CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [input\_current\_regulation\_current\_ua](#ae51670de8fa560f0c7610452db029bc2) |
|  | CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [input\_voltage\_regulation\_voltage\_uv](#afbe7b5fe1e421fb97b37d71ce14dc51a) |
|  | CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV. |
| struct [charger\_current\_notifier](structcharger__current__notifier.md) | [input\_current\_notification](#a0ad956ab4d0b306f94cce2aa81283a35) |
|  | CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION. |
| struct [charger\_current\_notifier](structcharger__current__notifier.md) | [discharge\_current\_notification](#af256e63ca94f7809da101ad1c33c8e7a) |
|  | CHARGER\_PROP\_DISCHARGE\_CURRENT\_NOTIFICATION. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [system\_voltage\_notification](#a541d1bf0b3e32d7aaeb6a2f4f443c5dc) |
|  | CHARGER\_PROP\_SYSTEM\_VOLTAGE\_NOTIFICATION\_UV. |
| [charger\_status\_notifier\_t](group__charger__interface.md#ga7666697bde91b66829113efe151d1cb2) | [status\_notification](#ad77547e88ec465d2e37526751008f634) |
|  | CHARGER\_PROP\_STATUS\_NOTIFICATION. |
| [charger\_online\_notifier\_t](group__charger__interface.md#gab29c2fafc53988555d72974199f25475) | [online\_notification](#ab9f40a6083ff2361ea4d161226cd77ad) |
|  | CHARGER\_PROP\_ONLINE\_NOTIFICATION. |

## Detailed Description

container for a [charger\_property](group__charger__interface.md#ga6eb3b4cc76e4f1e34732b7853eb860b7 "Runtime Dynamic Battery Parameters.") value

## Field Documentation

## [◆ ](#a89d0c93d68650cefe29e891f4db928f4)charge\_term\_current\_ua

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_propval::charge\_term\_current\_ua |
| --- |

CHARGER\_PROP\_CHARGE\_TERM\_CURRENT\_UA.

## [◆ ](#ac1a594de2b1c10d28b6a81dd66f1a6ba)charge\_type

| enum [charger\_charge\_type](group__charger__interface.md#gaee833a379a8674621d2fdf9b57d1f803) charger\_propval::charge\_type |
| --- |

CHARGER\_PROP\_CHARGE\_TYPE.

## [◆ ](#af4e383bb797432033050937740ce0ac3)const\_charge\_current\_ua

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_propval::const\_charge\_current\_ua |
| --- |

CHARGER\_PROP\_CONSTANT\_CHARGE\_CURRENT\_UA.

## [◆ ](#a733bae9ce0bf7e902f8af307f94a356c)const\_charge\_voltage\_uv

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_propval::const\_charge\_voltage\_uv |
| --- |

CHARGER\_PROP\_CONSTANT\_CHARGE\_VOLTAGE\_UV.

## [◆ ](#af256e63ca94f7809da101ad1c33c8e7a)discharge\_current\_notification

| struct [charger\_current\_notifier](structcharger__current__notifier.md) charger\_propval::discharge\_current\_notification |
| --- |

CHARGER\_PROP\_DISCHARGE\_CURRENT\_NOTIFICATION.

## [◆ ](#abd990f67423424da60856f4b6e8824a3)health

| enum [charger\_health](group__charger__interface.md#gaab33241d3b85ab0770be9b1bd17e4412) charger\_propval::health |
| --- |

CHARGER\_PROP\_HEALTH.

## [◆ ](#a0ad956ab4d0b306f94cce2aa81283a35)input\_current\_notification

| struct [charger\_current\_notifier](structcharger__current__notifier.md) charger\_propval::input\_current\_notification |
| --- |

CHARGER\_PROP\_INPUT\_CURRENT\_NOTIFICATION.

## [◆ ](#ae51670de8fa560f0c7610452db029bc2)input\_current\_regulation\_current\_ua

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_propval::input\_current\_regulation\_current\_ua |
| --- |

CHARGER\_PROP\_INPUT\_REGULATION\_CURRENT\_UA.

## [◆ ](#afbe7b5fe1e421fb97b37d71ce14dc51a)input\_voltage\_regulation\_voltage\_uv

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_propval::input\_voltage\_regulation\_voltage\_uv |
| --- |

CHARGER\_PROP\_INPUT\_REGULATION\_VOLTAGE\_UV.

## [◆ ](#a8589124e6152b70b649788a8b94461ab)online

| enum [charger\_online](group__charger__interface.md#gad95d2b1aaf18ac3a1c536f2d40317c19) charger\_propval::online |
| --- |

CHARGER\_PROP\_ONLINE.

## [◆ ](#ab9f40a6083ff2361ea4d161226cd77ad)online\_notification

| [charger\_online\_notifier\_t](group__charger__interface.md#gab29c2fafc53988555d72974199f25475) charger\_propval::online\_notification |
| --- |

CHARGER\_PROP\_ONLINE\_NOTIFICATION.

## [◆ ](#a24a97e16505fa336bd3a68743d05936b)precharge\_current\_ua

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_propval::precharge\_current\_ua |
| --- |

CHARGER\_PROP\_PRECHARGE\_CURRENT\_UA.

## [◆ ](#ab0eec508b90d205a1662fd6c69638764)present

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) charger\_propval::present |
| --- |

CHARGER\_PROP\_PRESENT.

## [◆ ](#a7f4976d72d4a7d48385ceb9f18c510b5)status

| enum [charger\_status](group__charger__interface.md#ga4a3c46bc0916082d15e665f7665c89d7) charger\_propval::status |
| --- |

CHARGER\_PROP\_STATUS.

## [◆ ](#ad77547e88ec465d2e37526751008f634)status\_notification

| [charger\_status\_notifier\_t](group__charger__interface.md#ga7666697bde91b66829113efe151d1cb2) charger\_propval::status\_notification |
| --- |

CHARGER\_PROP\_STATUS\_NOTIFICATION.

## [◆ ](#a541d1bf0b3e32d7aaeb6a2f4f443c5dc)system\_voltage\_notification

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) charger\_propval::system\_voltage\_notification |
| --- |

CHARGER\_PROP\_SYSTEM\_VOLTAGE\_NOTIFICATION\_UV.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/[charger.h](charger_8h_source.md)

- [charger\_propval](unioncharger__propval.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
