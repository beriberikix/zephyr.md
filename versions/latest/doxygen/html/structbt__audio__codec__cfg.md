---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__audio__codec__cfg.html
original_path: doxygen/html/structbt__audio__codec__cfg.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_audio\_codec\_cfg Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Audio](group__bt__audio.md)

Codec specific configuration structure.
[More...](#details)

`#include <[audio.h](bluetooth_2audio_2audio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [path\_id](#a9386056bb02908407c9e3aad48abbd87) |
|  | Data path ID. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ctlr\_transcode](#a9e2c8081950a0830ffc270245ab308c1) |
|  | Whether or not the local controller should transcode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#aa2f99ec31ff3eb9b7b738bc8a1170f20) |
|  | Codec ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cid](#a664e21bcd6002b21d4b1b53d866db32d) |
|  | Codec Company ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vid](#a2996ab3f6ae1cab09ff5e3329b42468e) |
|  | Codec Company Vendor ID. |

## Detailed Description

Codec specific configuration structure.

## Field Documentation

## [◆ ](#a664e21bcd6002b21d4b1b53d866db32d)cid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_cfg::cid |
| --- |

Codec Company ID.

## [◆ ](#a9e2c8081950a0830ffc270245ab308c1)ctlr\_transcode

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_audio\_codec\_cfg::ctlr\_transcode |
| --- |

Whether or not the local controller should transcode.

This effectively sets the coding format for the ISO data path to [BT\_HCI\_CODING\_FORMAT\_TRANSPARENT](hci__types_8h.md#ad93af498e2265c180a01055eca2a4de0 "BT_HCI_CODING_FORMAT_TRANSPARENT") if false, else uses the [bt\_audio\_codec\_cfg::id](#aa2f99ec31ff3eb9b7b738bc8a1170f20).

## [◆ ](#aa2f99ec31ff3eb9b7b738bc8a1170f20)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_cfg::id |
| --- |

Codec ID.

## [◆ ](#a9386056bb02908407c9e3aad48abbd87)path\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_cfg::path\_id |
| --- |

Data path ID.

[BT\_ISO\_DATA\_PATH\_HCI](group__bt__iso.md#gadd421c69edccfd695d728ded5feb6862 "BT_ISO_DATA_PATH_HCI") for HCI path, or any other value for vendor specific ID.

## [◆ ](#a2996ab3f6ae1cab09ff5e3329b42468e)vid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_cfg::vid |
| --- |

Codec Company Vendor ID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[audio.h](bluetooth_2audio_2audio_8h_source.md)

- [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
