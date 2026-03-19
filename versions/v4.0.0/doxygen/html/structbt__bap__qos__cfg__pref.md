---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__qos__cfg__pref.html
original_path: doxygen/html/structbt__bap__qos__cfg__pref.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_qos\_cfg\_pref Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Audio Stream Quality of Service Preference structure.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [unframed\_supported](#a2a2de382f04a50d26d174dcc7c7a12c1) |
|  | Unframed PDUs supported. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a697a67e623d758b76be342a125a369a6) |
|  | Preferred PHY bitfield. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtn](#a286bfb02d35ca148f263f1fa1ca9e061) |
|  | Preferred Retransmission Number. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [latency](#ac5871b4f58be038eeda483e8d07b9b53) |
|  | Preferred Transport Latency. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pd\_min](#a3f643768de9d8b0a7a62e403703e0033) |
|  | Minimum Presentation Delay in microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pd\_max](#a666be60856b5b4688d21d7a36b956c29) |
|  | Maximum Presentation Delay in microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pref\_pd\_min](#a1df8cd4ed27e9099b8b2a069855010aa) |
|  | Preferred minimum Presentation Delay in microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pref\_pd\_max](#ab6475a80b33a9cea69edeaa3093c9070) |
|  | Preferred maximum Presentation Delay in microseconds. |

## Detailed Description

Audio Stream Quality of Service Preference structure.

## Field Documentation

## [◆ ](#ac5871b4f58be038eeda483e8d07b9b53)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_qos\_cfg\_pref::latency |
| --- |

Preferred Transport Latency.

Value range [BT\_ISO\_LATENCY\_MIN](group__bt__iso.md#ga77ae350543eb05617c590c0ad9cb0048 "BT_ISO_LATENCY_MIN") to [BT\_ISO\_LATENCY\_MAX](group__bt__iso.md#gad5e89d05d8706509d8d9d8dac40e3347 "BT_ISO_LATENCY_MAX")

## [◆ ](#a666be60856b5b4688d21d7a36b956c29)pd\_max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_qos\_cfg\_pref::pd\_max |
| --- |

Maximum Presentation Delay in microseconds.

Unlike the other fields, this is not a preference but a maximum requirement.

Value range [bt\_bap\_qos\_cfg\_pref::pd\_min](#a3f643768de9d8b0a7a62e403703e0033) to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX")

## [◆ ](#a3f643768de9d8b0a7a62e403703e0033)pd\_min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_qos\_cfg\_pref::pd\_min |
| --- |

Minimum Presentation Delay in microseconds.

Unlike the other fields, this is not a preference but a minimum requirement.

Value range 0 to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX")

## [◆ ](#a697a67e623d758b76be342a125a369a6)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_qos\_cfg\_pref::phy |
| --- |

Preferred PHY bitfield.

Bitfield consisting of one or more of [BT\_GAP\_LE\_PHY\_1M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba53eff400720a20fe1a91da4834bad752 "BT_GAP_LE_PHY_1M"), [BT\_GAP\_LE\_PHY\_2M](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba662049cc8293959194bcb481e1dd50a8 "BT_GAP_LE_PHY_2M") and [BT\_GAP\_LE\_PHY\_CODED](group__bt__gap__defines.md#gga7dc8e89251aa575e28331e05775ba20ba97d042e48448fdf6a9e35e5d38cb14c3 "BT_GAP_LE_PHY_CODED").

## [◆ ](#ab6475a80b33a9cea69edeaa3093c9070)pref\_pd\_max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_qos\_cfg\_pref::pref\_pd\_max |
| --- |

Preferred maximum Presentation Delay in microseconds.

Value range [bt\_bap\_qos\_cfg\_pref::pd\_min](#a3f643768de9d8b0a7a62e403703e0033) to [bt\_bap\_qos\_cfg\_pref::pd\_max](#a666be60856b5b4688d21d7a36b956c29), and higher than or equal to [bt\_bap\_qos\_cfg\_pref::pref\_pd\_min](#a1df8cd4ed27e9099b8b2a069855010aa), or [BT\_AUDIO\_PD\_PREF\_NONE](group__bt__audio.md#ga663ab7bf74d56f36ee6cc80b369cbc16 "BT_AUDIO_PD_PREF_NONE") to indicate no preference.

## [◆ ](#a1df8cd4ed27e9099b8b2a069855010aa)pref\_pd\_min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_qos\_cfg\_pref::pref\_pd\_min |
| --- |

Preferred minimum Presentation Delay in microseconds.

Value range [bt\_bap\_qos\_cfg\_pref::pd\_min](#a3f643768de9d8b0a7a62e403703e0033) to [bt\_bap\_qos\_cfg\_pref::pd\_max](#a666be60856b5b4688d21d7a36b956c29), or [BT\_AUDIO\_PD\_PREF\_NONE](group__bt__audio.md#ga663ab7bf74d56f36ee6cc80b369cbc16 "BT_AUDIO_PD_PREF_NONE") to indicate no preference.

## [◆ ](#a286bfb02d35ca148f263f1fa1ca9e061)rtn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_qos\_cfg\_pref::rtn |
| --- |

Preferred Retransmission Number.

[BT\_AUDIO\_RTN\_PREF\_NONE](group__bt__audio.md#ga4a5fd440b96f4e4acbb791badef8c255 "BT_AUDIO_RTN_PREF_NONE") indicates no preference.

## [◆ ](#a2a2de382f04a50d26d174dcc7c7a12c1)unframed\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_bap\_qos\_cfg\_pref::unframed\_supported |
| --- |

Unframed PDUs supported.

Unlike the other fields, this is not a preference but whether the codec supports unframed ISOAL PDUs.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
