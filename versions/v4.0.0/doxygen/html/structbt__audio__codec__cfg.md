---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__audio__codec__cfg.html
original_path: doxygen/html/structbt__audio__codec__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_len](#a8a5a789e9993a48ce4c83a2156c1f43c) |
|  | Codec Specific Capabilities Data count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#ad3709d5321f6faeb392452cb3b21023b) [CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE] |
|  | Codec Specific Capabilities Data. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [meta\_len](#a1e69a5c017e9571b50aba721f86876fb) |
|  | Codec Specific Capabilities Metadata count. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [meta](#a4f84974ea14b773ad8e2fd7c0ffa0c7f) [CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE] |
|  | Codec Specific Capabilities Metadata. |

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

## [◆ ](#ad3709d5321f6faeb392452cb3b21023b)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_cfg::data[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE] |
| --- |

Codec Specific Capabilities Data.

## [◆ ](#a8a5a789e9993a48ce4c83a2156c1f43c)data\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_audio\_codec\_cfg::data\_len |
| --- |

Codec Specific Capabilities Data count.

## [◆ ](#aa2f99ec31ff3eb9b7b738bc8a1170f20)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_cfg::id |
| --- |

Codec ID.

## [◆ ](#a4f84974ea14b773ad8e2fd7c0ffa0c7f)meta

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_cfg::meta[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE] |
| --- |

Codec Specific Capabilities Metadata.

## [◆ ](#a1e69a5c017e9571b50aba721f86876fb)meta\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_audio\_codec\_cfg::meta\_len |
| --- |

Codec Specific Capabilities Metadata count.

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
