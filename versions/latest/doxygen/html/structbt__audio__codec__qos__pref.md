---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__audio__codec__qos__pref.html
original_path: doxygen/html/structbt__audio__codec__qos__pref.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_audio\_codec\_qos\_pref Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Audio](group__bt__audio.md)

Audio Stream Quality of Service Preference structure.
[More...](#details)

`#include <[audio.h](bluetooth_2audio_2audio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [unframed\_supported](#a3bdb319d2aa401102fb9e54f92993e83) |
|  | Unframed PDUs supported. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a36fc375290b8f76c7278a236942db692) |
|  | Preferred PHY. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtn](#abc2142ef5c8ad1744b829ae626a57e9d) |
|  | Preferred Retransmission Number. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [latency](#a1d46cf0aa05cfb7c88446719e59e0011) |
|  | Preferred Transport Latency. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pd\_min](#a7437273abb18ce93c15bb789eeeb65d3) |
|  | Minimum Presentation Delay in microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pd\_max](#ab07f2245bfed3a1400b6a1e6eaad2735) |
|  | Maximum Presentation Delay. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pref\_pd\_min](#ab38a4b98b47ab773f91873b42c69ed71) |
|  | Preferred minimum Presentation Delay. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pref\_pd\_max](#a5486cacf6cd5016e9b44b69e3da67d6d) |
|  | Preferred maximum Presentation Delay. |

## Detailed Description

Audio Stream Quality of Service Preference structure.

## Field Documentation

## [◆ ](#a1d46cf0aa05cfb7c88446719e59e0011)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_qos\_pref::latency |
| --- |

Preferred Transport Latency.

## [◆ ](#ab07f2245bfed3a1400b6a1e6eaad2735)pd\_max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_audio\_codec\_qos\_pref::pd\_max |
| --- |

Maximum Presentation Delay.

Unlike the other fields, this is not a preference but a maximum requirement.

Value range 0 to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX"), or [BT\_AUDIO\_PD\_PREF\_NONE](group__bt__audio.md#ga663ab7bf74d56f36ee6cc80b369cbc16 "BT_AUDIO_PD_PREF_NONE") to indicate no preference.

## [◆ ](#a7437273abb18ce93c15bb789eeeb65d3)pd\_min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_audio\_codec\_qos\_pref::pd\_min |
| --- |

Minimum Presentation Delay in microseconds.

Unlike the other fields, this is not a preference but a minimum requirement.

Value range 0 to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX"), or [BT\_AUDIO\_PD\_PREF\_NONE](group__bt__audio.md#ga663ab7bf74d56f36ee6cc80b369cbc16 "BT_AUDIO_PD_PREF_NONE") to indicate no preference.

## [◆ ](#a36fc375290b8f76c7278a236942db692)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_qos\_pref::phy |
| --- |

Preferred PHY.

## [◆ ](#a5486cacf6cd5016e9b44b69e3da67d6d)pref\_pd\_max

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_audio\_codec\_qos\_pref::pref\_pd\_max |
| --- |

Preferred maximum Presentation Delay.

Value range 0 to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX").

## [◆ ](#ab38a4b98b47ab773f91873b42c69ed71)pref\_pd\_min

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_audio\_codec\_qos\_pref::pref\_pd\_min |
| --- |

Preferred minimum Presentation Delay.

Value range 0 to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX").

## [◆ ](#abc2142ef5c8ad1744b829ae626a57e9d)rtn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_qos\_pref::rtn |
| --- |

Preferred Retransmission Number.

## [◆ ](#a3bdb319d2aa401102fb9e54f92993e83)unframed\_supported

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_audio\_codec\_qos\_pref::unframed\_supported |
| --- |

Unframed PDUs supported.

Unlike the other fields, this is not a preference but whether the codec supports unframed ISOAL PDUs.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[audio.h](bluetooth_2audio_2audio_8h_source.md)

- [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
