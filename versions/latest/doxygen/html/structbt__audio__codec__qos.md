---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__audio__codec__qos.html
original_path: doxygen/html/structbt__audio__codec__qos.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_audio\_codec\_qos Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Audio](group__bt__audio.md)

Codec QoS structure.
[More...](#details)

`#include <[audio.h](bluetooth_2audio_2audio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a8911b0b9db8e4de55b3c313e3ad7c502) |
|  | QoS PHY. |
| enum [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) | [framing](#a4212bf93b65e0faa218a1e0d03ae0283) |
|  | QoS Framing. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtn](#ab05af8d47df82d34921afdd557770dbd) |
|  | QoS Retransmission Number. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sdu](#ae1a5adb80af9357fd6ee6532b0ba228e) |
|  | QoS SDU. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval](#ad906dc06624b0f80701d7ee92d849152) |
|  | QoS Frame Interval. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pd](#a28d87b06785e016fe7e12a0504f3b419) |
|  | QoS Presentation Delay in microseconds. |

## Detailed Description

Codec QoS structure.

## Field Documentation

## [◆ ](#a4212bf93b65e0faa218a1e0d03ae0283)framing

| enum [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) bt\_audio\_codec\_qos::framing |
| --- |

QoS Framing.

## [◆ ](#ad906dc06624b0f80701d7ee92d849152)interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_audio\_codec\_qos::interval |
| --- |

QoS Frame Interval.

## [◆ ](#a28d87b06785e016fe7e12a0504f3b419)pd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_audio\_codec\_qos::pd |
| --- |

QoS Presentation Delay in microseconds.

Value range 0 to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX").

## [◆ ](#a8911b0b9db8e4de55b3c313e3ad7c502)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_qos::phy |
| --- |

QoS PHY.

## [◆ ](#ab05af8d47df82d34921afdd557770dbd)rtn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_qos::rtn |
| --- |

QoS Retransmission Number.

## [◆ ](#ae1a5adb80af9357fd6ee6532b0ba228e)sdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_qos::sdu |
| --- |

QoS SDU.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[audio.h](bluetooth_2audio_2audio_8h_source.md)

- [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
