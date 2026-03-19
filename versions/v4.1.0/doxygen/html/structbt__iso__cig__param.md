---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__iso__cig__param.html
original_path: doxygen/html/structbt__iso__cig__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_cig\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

Connected Isochronous Group (CIG) parameters.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_iso\_chan](structbt__iso__chan.md) \*\* | [cis\_channels](#a841dee850f3161bd8e904376792c8ad7) |
|  | Array of pointers to CIS channels. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_cis](#a69c12b704b9897d88b71bc96bd2d3024) |
|  | Number of channels in `cis_channels`. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [c\_to\_p\_interval](#ad7349213bab902a68c726da51fac2306) |
|  | Channel interval in us for SDUs sent from Central to Peripheral. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [p\_to\_c\_interval](#a36d2eaa4fd3e08988d4c49ca0902a882) |
|  | Channel interval in us for SDUs sent from Peripheral to Central. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [c\_to\_p\_latency](#aeffe10e87d81285196e931dcad2882ba) |
|  | Channel Latency in ms for SDUs sent from Central to Peripheral. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [p\_to\_c\_latency](#ad1725e09a397e83d1cc88ebd3a60ed93) |
|  | Channel Latency in ms for SDUs sent from Peripheral to Central. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sca](#a83fdc5374f341a421e1394b08297cdff) |
|  | Channel peripherals sleep clock accuracy Only for CIS. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#a3908eadf3080731cb891e803162d321c) |
|  | Channel packing mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [framing](#a4a09f9f6e7a8db17c3037c9f1761b18a) |
|  | Channel framing mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_to\_p\_ft](#aadc3762f3fec3127014378fe58c5b684) |
|  | Central to Peripheral flush timeout. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_to\_c\_ft](#ab222cdb0af475180dd715b4f5658dc65) |
|  | Peripheral to Central flush timeout. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iso\_interval](#a85641a8f01d63b4221c013815c055526) |
|  | ISO interval. |

## Detailed Description

Connected Isochronous Group (CIG) parameters.

## Field Documentation

## [◆ ](#aadc3762f3fec3127014378fe58c5b684)c\_to\_p\_ft

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::c\_to\_p\_ft |
| --- |

Central to Peripheral flush timeout.

The flush timeout in multiples of ISO\_Interval for each payload sent from the Central to Peripheral.

Value range from [BT\_ISO\_FT\_MIN](group__bt__iso.md#ga2d3bde6b34f6b15474926ed97ad11d98 "BT_ISO_FT_MIN") to [BT\_ISO\_FT\_MAX](group__bt__iso.md#ga011c9d5840658fd0ef244f47893ec70e "BT_ISO_FT_MAX")

## [◆ ](#ad7349213bab902a68c726da51fac2306)c\_to\_p\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_cig\_param::c\_to\_p\_interval |
| --- |

Channel interval in us for SDUs sent from Central to Peripheral.

Value range [BT\_ISO\_SDU\_INTERVAL\_MIN](group__bt__iso.md#ga8122de88b6e5423dca653b1f0a484316 "BT_ISO_SDU_INTERVAL_MIN") to [BT\_ISO\_SDU\_INTERVAL\_MAX](group__bt__iso.md#ga077eb6d219bba947d363e2cce8e0080c "BT_ISO_SDU_INTERVAL_MAX").

## [◆ ](#aeffe10e87d81285196e931dcad2882ba)c\_to\_p\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_cig\_param::c\_to\_p\_latency |
| --- |

Channel Latency in ms for SDUs sent from Central to Peripheral.

Value range [BT\_ISO\_LATENCY\_MIN](group__bt__iso.md#ga77ae350543eb05617c590c0ad9cb0048 "BT_ISO_LATENCY_MIN") to [BT\_ISO\_LATENCY\_MAX](group__bt__iso.md#gad5e89d05d8706509d8d9d8dac40e3347 "BT_ISO_LATENCY_MAX").

This value is ignored if any advanced ISO parameters are set.

## [◆ ](#a841dee850f3161bd8e904376792c8ad7)cis\_channels

| struct [bt\_iso\_chan](structbt__iso__chan.md)\*\* bt\_iso\_cig\_param::cis\_channels |
| --- |

Array of pointers to CIS channels.

## [◆ ](#a4a09f9f6e7a8db17c3037c9f1761b18a)framing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::framing |
| --- |

Channel framing mode.

[BT\_ISO\_FRAMING\_UNFRAMED](group__bt__iso.md#ga696a81180ae25aa686a53b73e352c9d2 "BT_ISO_FRAMING_UNFRAMED") for unframed and [BT\_ISO\_FRAMING\_FRAMED](group__bt__iso.md#ga8f9aba389529ad2a3667ca378e99de2b "BT_ISO_FRAMING_FRAMED") for framed.

## [◆ ](#a85641a8f01d63b4221c013815c055526)iso\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_cig\_param::iso\_interval |
| --- |

ISO interval.

Time between consecutive CIS anchor points.

Value range from [BT\_ISO\_ISO\_INTERVAL\_MIN](group__bt__iso.md#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de "BT_ISO_ISO_INTERVAL_MIN") to [BT\_ISO\_ISO\_INTERVAL\_MAX](group__bt__iso.md#gabc381a7f565061ec91d23b7783521da3 "BT_ISO_ISO_INTERVAL_MAX").

## [◆ ](#a69c12b704b9897d88b71bc96bd2d3024)num\_cis

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::num\_cis |
| --- |

Number of channels in `cis_channels`.

Maximum number of channels in a single group is [BT\_ISO\_MAX\_GROUP\_ISO\_COUNT](group__bt__iso.md#gae9dc30b300e2c309d646e3227e8cc00e "BT_ISO_MAX_GROUP_ISO_COUNT")

## [◆ ](#ab222cdb0af475180dd715b4f5658dc65)p\_to\_c\_ft

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::p\_to\_c\_ft |
| --- |

Peripheral to Central flush timeout.

The flush timeout in multiples of ISO\_Interval for each payload sent from the Peripheral to Central.

Value range from [BT\_ISO\_FT\_MIN](group__bt__iso.md#ga2d3bde6b34f6b15474926ed97ad11d98 "BT_ISO_FT_MIN") to [BT\_ISO\_FT\_MAX](group__bt__iso.md#ga011c9d5840658fd0ef244f47893ec70e "BT_ISO_FT_MAX").

## [◆ ](#a36d2eaa4fd3e08988d4c49ca0902a882)p\_to\_c\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_cig\_param::p\_to\_c\_interval |
| --- |

Channel interval in us for SDUs sent from Peripheral to Central.

Value range [BT\_ISO\_SDU\_INTERVAL\_MIN](group__bt__iso.md#ga8122de88b6e5423dca653b1f0a484316 "BT_ISO_SDU_INTERVAL_MIN") to [BT\_ISO\_SDU\_INTERVAL\_MAX](group__bt__iso.md#ga077eb6d219bba947d363e2cce8e0080c "BT_ISO_SDU_INTERVAL_MAX").

## [◆ ](#ad1725e09a397e83d1cc88ebd3a60ed93)p\_to\_c\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_cig\_param::p\_to\_c\_latency |
| --- |

Channel Latency in ms for SDUs sent from Peripheral to Central.

Value range [BT\_ISO\_LATENCY\_MIN](group__bt__iso.md#ga77ae350543eb05617c590c0ad9cb0048 "BT_ISO_LATENCY_MIN") to [BT\_ISO\_LATENCY\_MAX](group__bt__iso.md#gad5e89d05d8706509d8d9d8dac40e3347 "BT_ISO_LATENCY_MAX").

This value is ignored if any advanced ISO parameters are set.

## [◆ ](#a3908eadf3080731cb891e803162d321c)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::packing |
| --- |

Channel packing mode.

[BT\_ISO\_PACKING\_SEQUENTIAL](group__bt__iso.md#ga6275e8d805e2366522a78f18ca47ac19 "BT_ISO_PACKING_SEQUENTIAL") or [BT\_ISO\_PACKING\_INTERLEAVED](group__bt__iso.md#ga35b037fcce858857642b4c54bae8dd79 "BT_ISO_PACKING_INTERLEAVED")

## [◆ ](#a83fdc5374f341a421e1394b08297cdff)sca

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::sca |
| --- |

Channel peripherals sleep clock accuracy Only for CIS.

Shall be worst case sleep clock accuracy of all the peripherals. For possible values see the BT\_GAP\_SCA\_\* values. If unknown for the peripherals, this should be set to [BT\_GAP\_SCA\_UNKNOWN](group__bt__gap__defines.md#ggafa0d8b6c50823ebb6bd38340efbb5a6bace5a2d3f9fcb1a8913203ee6f437b910 "BT_GAP_SCA_UNKNOWN").

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_cig\_param](structbt__iso__cig__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
