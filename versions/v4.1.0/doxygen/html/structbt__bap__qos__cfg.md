---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__qos__cfg.html
original_path: doxygen/html/structbt__bap__qos__cfg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_qos\_cfg Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

QoS configuration structure.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pd](#addf190fac00b2fb99c0d1abf13eb20b3) |
|  | Presentation Delay in microseconds. |
| struct { |  |
| enum [bt\_bap\_qos\_cfg\_framing](group__bt__bap.md#ga37a5f9d7198739eef8bde6764da30de9)   [framing](#a60057a7812cdc5b26f839e68dc4603c4) |  |
|  | QoS Framing. [More...](#a60057a7812cdc5b26f839e68dc4603c4) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [phy](#ac50ea51e1645546d8f8faa58c64672ce) |  |
|  | PHY. [More...](#ac50ea51e1645546d8f8faa58c64672ce) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [rtn](#aaaa4a88499cfd1f90e409fa98891bf2c) |  |
|  | Retransmission Number. [More...](#aaaa4a88499cfd1f90e409fa98891bf2c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [sdu](#a294709496f7779ee4cb7aa542da8832b) |  |
|  | Maximum SDU size. [More...](#a294709496f7779ee4cb7aa542da8832b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [latency](#a912ee316aa2ddb00ebab7bb78af0f34a) |  |
|  | Maximum Transport Latency. [More...](#a912ee316aa2ddb00ebab7bb78af0f34a) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [interval](#abf8a1b76cc0735b9aec1962d2ce574ec) |  |
|  | SDU Interval. [More...](#abf8a1b76cc0735b9aec1962d2ce574ec) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [max\_pdu](#acb84f2da73e865e38dcefa92007f01e1) |  |
|  | Maximum PDU size. [More...](#acb84f2da73e865e38dcefa92007f01e1) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [burst\_number](#a597b81261511ec820caa66bd091ab896) |  |
|  | Burst number. [More...](#a597b81261511ec820caa66bd091ab896) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [num\_subevents](#a97094ac8254ff3e97790943a5c71cdf3) |  |
|  | Number of subevents. [More...](#a97094ac8254ff3e97790943a5c71cdf3) |
| }; |  |
|  | Connected Isochronous Group (CIG) parameters. |

## Detailed Description

QoS configuration structure.

## Field Documentation

## [◆ ](#a9a3980ad5dcdb2e8fd5646d09364c555)[struct]

| struct { ... } [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) |
| --- |

Connected Isochronous Group (CIG) parameters.

The fields in this struct affect the value sent to the controller via HCI when creating the CIG. Once the group has been created with [bt\_bap\_unicast\_group\_create()](group__bt__bap__unicast__client.md#gaafd53b5f45d998b44e94a1b58e93ba21 "Create unicast group."), modifying these fields will not affect the group.

## [◆ ](#a597b81261511ec820caa66bd091ab896)burst\_number

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_qos\_cfg::burst\_number |
| --- |

Burst number.

Value range [BT\_ISO\_BN\_MIN](group__bt__iso.md#ga2905cddfa456fc846f0c8025487b404d "BT_ISO_BN_MIN") to [BT\_ISO\_BN\_MAX](group__bt__iso.md#gac05f4f51ea04962679f616bb167b724d "BT_ISO_BN_MAX").

## [◆ ](#a60057a7812cdc5b26f839e68dc4603c4)framing

| enum [bt\_bap\_qos\_cfg\_framing](group__bt__bap.md#ga37a5f9d7198739eef8bde6764da30de9) bt\_bap\_qos\_cfg::framing |
| --- |

QoS Framing.

## [◆ ](#abf8a1b76cc0735b9aec1962d2ce574ec)interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_qos\_cfg::interval |
| --- |

SDU Interval.

Value range [BT\_ISO\_SDU\_INTERVAL\_MIN](group__bt__iso.md#ga8122de88b6e5423dca653b1f0a484316 "BT_ISO_SDU_INTERVAL_MIN") to [BT\_ISO\_SDU\_INTERVAL\_MAX](group__bt__iso.md#ga077eb6d219bba947d363e2cce8e0080c "BT_ISO_SDU_INTERVAL_MAX")

## [◆ ](#a912ee316aa2ddb00ebab7bb78af0f34a)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_qos\_cfg::latency |
| --- |

Maximum Transport Latency.

Not used for the `CONFIG_BT_BAP_BROADCAST_SINK` role.

## [◆ ](#acb84f2da73e865e38dcefa92007f01e1)max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_qos\_cfg::max\_pdu |
| --- |

Maximum PDU size.

Maximum size, in octets, of the payload from link layer to link layer.

Value range [BT\_ISO\_CONNECTED\_PDU\_MIN](group__bt__iso.md#ga4e29d5966f959114754d62a8763c8c1e "BT_ISO_CONNECTED_PDU_MIN") to [BT\_ISO\_PDU\_MAX](group__bt__iso.md#ga88fb5690cd1cab4e5e8d5c025cc1af00 "BT_ISO_PDU_MAX") for connected ISO.

Value range [BT\_ISO\_BROADCAST\_PDU\_MIN](group__bt__iso.md#gaee766ff789f1bf01f75c88112ddd2afa "BT_ISO_BROADCAST_PDU_MIN") to [BT\_ISO\_PDU\_MAX](group__bt__iso.md#ga88fb5690cd1cab4e5e8d5c025cc1af00 "BT_ISO_PDU_MAX") for broadcast ISO.

## [◆ ](#a97094ac8254ff3e97790943a5c71cdf3)num\_subevents

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_qos\_cfg::num\_subevents |
| --- |

Number of subevents.

Maximum number of subevents in each CIS or BIS event.

Value range [BT\_ISO\_NSE\_MIN](group__bt__iso.md#ga3eba4c20b4203b0323b14178522e6159 "BT_ISO_NSE_MIN") to [BT\_ISO\_NSE\_MAX](group__bt__iso.md#gab7637d96bde7a41123b34f487eec3436 "BT_ISO_NSE_MAX").

## [◆ ](#addf190fac00b2fb99c0d1abf13eb20b3)pd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_bap\_qos\_cfg::pd |
| --- |

Presentation Delay in microseconds.

This value can be changed up and until [bt\_bap\_stream\_qos()](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d "Configure Audio Stream QoS.") has been called. Once a stream has been QoS configured, modifying this field does not modify the value. It is however possible to modify this field and call [bt\_bap\_stream\_qos()](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d "Configure Audio Stream QoS.") again to update the value, assuming that the stream is in the correct state.

Value range 0 to [BT\_AUDIO\_PD\_MAX](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc "BT_AUDIO_PD_MAX").

## [◆ ](#ac50ea51e1645546d8f8faa58c64672ce)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_qos\_cfg::phy |
| --- |

PHY.

Allowed values are [BT\_BAP\_QOS\_CFG\_1M](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44af5bc162fe51c445cb3c77bcf640bbe28 "BT_BAP_QOS_CFG_1M"), [BT\_BAP\_QOS\_CFG\_2M](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ad7cee00c6f3276d2c336509d1f16f147 "BT_BAP_QOS_CFG_2M") and [BT\_BAP\_QOS\_CFG\_CODED](group__bt__bap.md#gga5e8ebf4db88f94f44828bb6f41e81d44ab41e06fe31c57bb7dac5a77acb53be73 "BT_BAP_QOS_CFG_CODED").

## [◆ ](#aaaa4a88499cfd1f90e409fa98891bf2c)rtn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_qos\_cfg::rtn |
| --- |

Retransmission Number.

This a recommendation to the controller, and the actual retransmission number may be different than this.

## [◆ ](#a294709496f7779ee4cb7aa542da8832b)sdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_bap\_qos\_cfg::sdu |
| --- |

Maximum SDU size.

Value range [BT\_ISO\_MIN\_SDU](group__bt__iso.md#ga4cc5565eeda9a3661d49d485637d1db2 "BT_ISO_MIN_SDU") to [BT\_ISO\_MAX\_SDU](group__bt__iso.md#gaa5d5588e7229db16219b0c44921bbcf7 "BT_ISO_MAX_SDU").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
