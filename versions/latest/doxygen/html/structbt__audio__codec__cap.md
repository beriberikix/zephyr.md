---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__audio__codec__cap.html
original_path: doxygen/html/structbt__audio__codec__cap.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_audio\_codec\_cap Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Audio](group__bt__audio.md)

Codec capability structure.
[More...](#details)

`#include <[audio.h](bluetooth_2audio_2audio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [path\_id](#a822a06f815091cc580ca2e5bbb3126f7) |
|  | Data path ID. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ctlr\_transcode](#a900a77db09e72de61d4ff652c6dbb10b) |
|  | Whether or not the local controller should transcode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#ae3892731e7ca05f3ec426c70f0d9e1a9) |
|  | Codec ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cid](#a763222d12a87958a5ba806303f98829a) |
|  | Codec Company ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vid](#a3b91269e16a3d63b3128a527caa5e3ff) |
|  | Codec Company Vendor ID. |

## Detailed Description

Codec capability structure.

## Field Documentation

## [◆ ](#a763222d12a87958a5ba806303f98829a)cid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_cap::cid |
| --- |

Codec Company ID.

## [◆ ](#a900a77db09e72de61d4ff652c6dbb10b)ctlr\_transcode

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_audio\_codec\_cap::ctlr\_transcode |
| --- |

Whether or not the local controller should transcode.

This effectively sets the coding format for the ISO data path to [BT\_HCI\_CODING\_FORMAT\_TRANSPARENT](hci__types_8h.md#ad93af498e2265c180a01055eca2a4de0 "BT_HCI_CODING_FORMAT_TRANSPARENT") if false, else uses the [bt\_audio\_codec\_cfg::id](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20 "bt_audio_codec_cfg::id").

## [◆ ](#ae3892731e7ca05f3ec426c70f0d9e1a9)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_cap::id |
| --- |

Codec ID.

## [◆ ](#a822a06f815091cc580ca2e5bbb3126f7)path\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_cap::path\_id |
| --- |

Data path ID.

[BT\_ISO\_DATA\_PATH\_HCI](group__bt__iso.md#gadd421c69edccfd695d728ded5feb6862 "BT_ISO_DATA_PATH_HCI") for HCI path, or any other value for vendor specific ID.

## [◆ ](#a3b91269e16a3d63b3128a527caa5e3ff)vid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_cap::vid |
| --- |

Codec Company Vendor ID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[audio.h](bluetooth_2audio_2audio_8h_source.md)

- [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
