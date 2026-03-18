---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__has__preset__register__param.html
original_path: doxygen/html/structbt__has__preset__register__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_has\_preset\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hearing Access Service (HAS)](group__bt__has.md)

Register structure for preset.
[More...](#details)

`#include <[has.h](has_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [index](#a9a3ade943b4f7569577c092df3ec467c) |
|  | Preset index. |
| enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) | [properties](#a8273bbec14040a7dd67aeac14188b86b) |
|  | Preset properties. |
| const char \* | [name](#a35b8d2e9a01198cc34350595c786f1ae) |
|  | Preset name. |
| const struct [bt\_has\_preset\_ops](structbt__has__preset__ops.md) \* | [ops](#a6e480fb6337d363353ca7ba6f716cd71) |
|  | Preset operations structure. |

## Detailed Description

Register structure for preset.

## Field Documentation

## [◆ ](#a9a3ade943b4f7569577c092df3ec467c)index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_has\_preset\_register\_param::index |
| --- |

Preset index.

Unique preset identifier. The value shall be other than [BT\_HAS\_PRESET\_INDEX\_NONE](group__bt__has.md#ga462679b8b5c91762c6d1daf03c5675d0 "BT_HAS_PRESET_INDEX_NONE").

## [◆ ](#a35b8d2e9a01198cc34350595c786f1ae)name

| const char\* bt\_has\_preset\_register\_param::name |
| --- |

Preset name.

Preset name that further can be changed by either server or client if `CONFIG_BT_HAS_PRESET_NAME_DYNAMIC` configuration option has been enabled. It's length shall be greater than [BT\_HAS\_PRESET\_NAME\_MIN](group__bt__has.md#gacbc29958c09b26a81e02893cd5914074 "BT_HAS_PRESET_NAME_MIN"). If the length exceeds [BT\_HAS\_PRESET\_NAME\_MAX](group__bt__has.md#gae133807f12d0d7a1ecd1f8dda24c7f09 "BT_HAS_PRESET_NAME_MAX"), the name will be truncated.

## [◆ ](#a6e480fb6337d363353ca7ba6f716cd71)ops

| const struct [bt\_has\_preset\_ops](structbt__has__preset__ops.md)\* bt\_has\_preset\_register\_param::ops |
| --- |

Preset operations structure.

## [◆ ](#a8273bbec14040a7dd67aeac14188b86b)properties

| enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) bt\_has\_preset\_register\_param::properties |
| --- |

Preset properties.

Bitfield of preset properties.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[has.h](has_8h_source.md)

- [bt\_has\_preset\_register\_param](structbt__has__preset__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
