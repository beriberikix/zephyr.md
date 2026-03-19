---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__has__features__param.html
original_path: doxygen/html/structbt__has__features__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_has\_features\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hearing Access Service (HAS)](group__bt__has.md)

Structure for registering features of a Hearing Access Service instance.
[More...](#details)

`#include <[has.h](has_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) | [type](#abcaf8630309bcae1a8184095c1eca656) |
|  | Hearing Aid Type value. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [preset\_sync\_support](#ada946ee62547349bc01054db5cafa279) |
|  | Preset Synchronization Support. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [independent\_presets](#a5ff95f2633bf577fc0f4c3d714d53bb1) |
|  | Independent Presets. |

## Detailed Description

Structure for registering features of a Hearing Access Service instance.

## Field Documentation

## [◆ ](#a5ff95f2633bf577fc0f4c3d714d53bb1)independent\_presets

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_has\_features\_param::independent\_presets |
| --- |

Independent Presets.

Only applicable if `type` is [BT\_HAS\_HEARING\_AID\_TYPE\_BINAURAL](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c "BT_HAS_HEARING_AID_TYPE_BINAURAL") and `CONFIG_BT_HAS_PRESET_COUNT` is non-zero.

## [◆ ](#ada946ee62547349bc01054db5cafa279)preset\_sync\_support

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_has\_features\_param::preset\_sync\_support |
| --- |

Preset Synchronization Support.

Only applicable if `type` is [BT\_HAS\_HEARING\_AID\_TYPE\_BINAURAL](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c "BT_HAS_HEARING_AID_TYPE_BINAURAL") and `CONFIG_BT_HAS_PRESET_COUNT` is non-zero.

## [◆ ](#abcaf8630309bcae1a8184095c1eca656)type

| enum [bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) bt\_has\_features\_param::type |
| --- |

Hearing Aid Type value.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[has.h](has_8h_source.md)

- [bt\_has\_features\_param](structbt__has__features__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
