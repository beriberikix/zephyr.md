---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__audio__codec__qos.html
original_path: doxygen/html/structbt__audio__codec__qos.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pd](#a28d87b06785e016fe7e12a0504f3b419) |
|  | Presentation Delay in microseconds. |
| struct { |  |
| enum [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9)   [framing](#a4212bf93b65e0faa218a1e0d03ae0283) |  |
|  | QoS Framing. [More...](#a4212bf93b65e0faa218a1e0d03ae0283) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [phy](#a8911b0b9db8e4de55b3c313e3ad7c502) |  |
|  | PHY. [More...](#a8911b0b9db8e4de55b3c313e3ad7c502) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [rtn](#ab05af8d47df82d34921afdd557770dbd) |  |
|  | Retransmission Number. [More...](#ab05af8d47df82d34921afdd557770dbd) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [sdu](#ae1a5adb80af9357fd6ee6532b0ba228e) |  |
|  | Maximum SDU size. [More...](#ae1a5adb80af9357fd6ee6532b0ba228e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [latency](#acb0fb67ff7c24d6d00c318cccb6b6eb3) |  |
|  | Maximum Transport Latency. [More...](#acb0fb67ff7c24d6d00c318cccb6b6eb3) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [interval](#ad906dc06624b0f80701d7ee92d849152) |  |
|  | SDU Interval. [More...](#ad906dc06624b0f80701d7ee92d849152) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [max\_pdu](#a98a5b8ba8ab2b2a289714916f38a1e27) |  |
|  | Maximum PDU size. [More...](#a98a5b8ba8ab2b2a289714916f38a1e27) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [burst\_number](#a42c025d09fb7f6ce8af136e01837e002) |  |
|  | Burst number. [More...](#a42c025d09fb7f6ce8af136e01837e002) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [num\_subevents](#a7b66a27686feda162ea70fdc9ae17425) |  |
|  | Number of subevents. [More...](#a7b66a27686feda162ea70fdc9ae17425) |
| }; |  |
|  | Connected Isochronous Group (CIG) parameters. |

## Detailed Description

Codec QoS structure.

## Field Documentation

## [◆ ](#a867f462adc27dbbe6305b29c6d6ee1fb)[struct]

| struct { ... } [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) |
| --- |

Connected Isochronous Group (CIG) parameters.

The fields in this struct affect the value sent to the controller via HCI when creating the CIG. Once the group has been created with [bt\_bap\_unicast\_group\_create()](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21 "Create audio unicast group."), modifying these fields will not affect the group.

## [◆ ](#a42c025d09fb7f6ce8af136e01837e002)burst\_number

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_qos::burst\_number |
| --- |

Burst number.

Value range [BT\_ISO\_BN\_MIN](group__bt__iso.md#ga2905cddfa456fc846f0c8025487b404d "BT_ISO_BN_MIN") to [BT\_ISO\_BN\_MAX](group__bt__iso.md#gac05f4f51ea04962679f616bb167b724d "BT_ISO_BN_MAX").

## [◆ ](#a4212bf93b65e0faa218a1e0d03ae0283)framing

| enum [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) bt\_audio\_codec\_qos::framing |
| --- |

QoS Framing.

## [◆ ](#ad906dc06624b0f80701d7ee92d849152)interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_audio\_codec\_qos::interval |
| --- |

SDU Interval.

Value range [BT\_ISO\_SDU\_INTERVAL\_MIN](group__bt__iso.md#ga8122de88b6e5423dca653b1f0a484316 "BT_ISO_SDU_INTERVAL_MIN") to [BT\_ISO\_SDU\_INTERVAL\_MAX](group__bt__iso.md#ga077eb6d219bba947d363e2cce8e0080c "BT_ISO_SDU_INTERVAL_MAX")

## [◆ ](#acb0fb67ff7c24d6d00c318cccb6b6eb3)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_qos::latency |
| --- |

Maximum Transport Latency.

Not used for the `CONFIG_BT_BAP_BROADCAST_SINK` role.

## [◆ ](#a98a5b8ba8ab2b2a289714916f38a1e27)max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_qos::max\_pdu |
| --- |

Maximum PDU size.

Maximum size, in octets, of the payload from link layer to link layer.

Value range [BT\_ISO\_CONNECTED\_PDU\_MIN](group__bt__iso.md#ga4e29d5966f959114754d62a8763c8c1e "BT_ISO_CONNECTED_PDU_MIN") to [BT\_ISO\_PDU\_MAX](group__bt__iso.md#ga88fb5690cd1cab4e5e8d5c025cc1af00 "BT_ISO_PDU_MAX") for connected ISO.

Value range [BT\_ISO\_BROADCAST\_PDU\_MIN](group__bt__iso.md#gaee766ff789f1bf01f75c88112ddd2afa "BT_ISO_BROADCAST_PDU_MIN") to [BT\_ISO\_PDU\_MAX](group__bt__iso.md#ga88fb5690cd1cab4e5e8d5c025cc1af00 "BT_ISO_PDU_MAX") for broadcast ISO.

## [◆ ](#a7b66a27686feda162ea70fdc9ae17425)num\_subevents

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_qos::num\_subevents |
| --- |

Number of subevents.

Maximum number of subevents in each CIS or BIS event.

Value range [BT\_ISO\_NSE\_MIN](group__bt__iso.md#ga3eba4c20b4203b0323b14178522e6159 "BT_ISO_NSE_MIN") to [BT\_ISO\_NSE\_MAX](group__bt__iso.md#gab7637d96bde7a41123b34f487eec3436 "BT_ISO_NSE_MAX").

## [◆ ](#a28d87b06785e016fe7e12a0504f3b419)pd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_audio\_codec\_qos::pd |
| --- |

Presentation Delay in microseconds.

This value can be changed up and until [bt\_bap\_stream\_qos()](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d "Configure Audio Stream QoS.") has been called. Once a stream has been QoS configured, modifying this field does not modify the value. It is however possible to modify this field and call [bt\_bap\_stream\_qos()](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d "Configure Audio Stream QoS.") again to update the value, assuming that the stream is in the correct state.

Value range 0 to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX").

## [◆ ](#a8911b0b9db8e4de55b3c313e3ad7c502)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_qos::phy |
| --- |

PHY.

Allowed values are [BT\_AUDIO\_CODEC\_QOS\_1M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ab387760c001ea6c81e889de55e74d5d5 "BT_AUDIO_CODEC_QOS_1M"), [BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297 "BT_AUDIO_CODEC_QOS_2M") and [BT\_AUDIO\_CODEC\_QOS\_CODED](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0a9789c1b6b319370a3b98ab37b61a86e0 "BT_AUDIO_CODEC_QOS_CODED").

## [◆ ](#ab05af8d47df82d34921afdd557770dbd)rtn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_audio\_codec\_qos::rtn |
| --- |

Retransmission Number.

This a recommendation to the controller, and the actual retransmission number may be different than this.

## [◆ ](#ae1a5adb80af9357fd6ee6532b0ba228e)sdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_audio\_codec\_qos::sdu |
| --- |

Maximum SDU size.

Value range [BT\_ISO\_MIN\_SDU](group__bt__iso.md#ga4cc5565eeda9a3661d49d485637d1db2 "BT_ISO_MIN_SDU") to [BT\_ISO\_MAX\_SDU](group__bt__iso.md#gaa5d5588e7229db16219b0c44921bbcf7 "BT_ISO_MAX_SDU").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[audio.h](bluetooth_2audio_2audio_8h_source.md)

- [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
