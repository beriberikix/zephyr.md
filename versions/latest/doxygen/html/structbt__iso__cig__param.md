---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__iso__cig__param.html
original_path: doxygen/html/structbt__iso__cig__param.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
|  | Number channels in `cis_channels`. |
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

## Detailed Description

Connected Isochronous Group (CIG) parameters.

## Field Documentation

## [◆ ](#ad7349213bab902a68c726da51fac2306)c\_to\_p\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_cig\_param::c\_to\_p\_interval |
| --- |

Channel interval in us for SDUs sent from Central to Peripheral.

Value range BT\_ISO\_SDU\_INTERVAL\_MIN - BT\_ISO\_SDU\_INTERVAL\_MAX.

## [◆ ](#aeffe10e87d81285196e931dcad2882ba)c\_to\_p\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_cig\_param::c\_to\_p\_latency |
| --- |

Channel Latency in ms for SDUs sent from Central to Peripheral.

Value range BT\_ISO\_LATENCY\_MIN - BT\_ISO\_LATENCY\_MAX.

This value is ignored if any advanced ISO parameters are set.

## [◆ ](#a841dee850f3161bd8e904376792c8ad7)cis\_channels

| struct [bt\_iso\_chan](structbt__iso__chan.md)\*\* bt\_iso\_cig\_param::cis\_channels |
| --- |

Array of pointers to CIS channels.

## [◆ ](#a4a09f9f6e7a8db17c3037c9f1761b18a)framing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::framing |
| --- |

Channel framing mode.

BT\_ISO\_FRAMING\_UNFRAMED for unframed and BT\_ISO\_FRAMING\_FRAMED for framed.

## [◆ ](#a69c12b704b9897d88b71bc96bd2d3024)num\_cis

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::num\_cis |
| --- |

Number channels in `cis_channels`.

Maximum number of channels in a single group is BT\_ISO\_MAX\_GROUP\_ISO\_COUNT

## [◆ ](#a36d2eaa4fd3e08988d4c49ca0902a882)p\_to\_c\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_cig\_param::p\_to\_c\_interval |
| --- |

Channel interval in us for SDUs sent from Peripheral to Central.

Value range BT\_ISO\_SDU\_INTERVAL\_MIN - BT\_ISO\_SDU\_INTERVAL\_MAX.

## [◆ ](#ad1725e09a397e83d1cc88ebd3a60ed93)p\_to\_c\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_cig\_param::p\_to\_c\_latency |
| --- |

Channel Latency in ms for SDUs sent from Peripheral to Central.

Value range BT\_ISO\_LATENCY\_MIN - BT\_ISO\_LATENCY\_MAX.

This value is ignored if any advanced ISO parameters are set.

## [◆ ](#a3908eadf3080731cb891e803162d321c)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::packing |
| --- |

Channel packing mode.

BT\_ISO\_PACKING\_SEQUENTIAL or BT\_ISO\_PACKING\_INTERLEAVED

## [◆ ](#a83fdc5374f341a421e1394b08297cdff)sca

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_cig\_param::sca |
| --- |

Channel peripherals sleep clock accuracy Only for CIS.

Shall be worst case sleep clock accuracy of all the peripherals. For possible values see the BT\_GAP\_SCA\_\* values. If unknown for the peripherals, this should be set to BT\_GAP\_SCA\_UNKNOWN.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_cig\_param](structbt__iso__cig__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
