---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__iso__biginfo.html
original_path: doxygen/html/structbt__iso__biginfo.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_biginfo Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

Broadcast Isochronous Group (BIG) information.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [addr](#aa7dbfd342eecf8ffc2fce9d3fa7209ea) |
|  | Address of the advertiser. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a78e0a53f920980081d7b0702b02cf386) |
|  | Advertiser SID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_bis](#a10eb24596a4353da3feb0d30fed35ae7) |
|  | Number of BISes in the BIG. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sub\_evt\_count](#a24eb83f7b54e9f949cc07e9955b4a8b8) |
|  | Maximum number of subevents in each isochronous event. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iso\_interval](#afe96caf570314731f6c543b40d7def9a) |
|  | Interval between two BIG anchor point (N \* 1.25 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [burst\_number](#ad114dd97500d12242da77e8522133953) |
|  | The number of new payloads in each BIS event. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [offset](#a4efb91dc2f249e41c65cd0dcbfe45bad) |
|  | Offset used for pre-transmissions. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rep\_count](#a8458f6d6ebe936212d928caca61b13bd) |
|  | The number of times a payload is transmitted in a BIS event. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_pdu](#af356aa29aa82c8deb63a9f47e54070a1) |
|  | Maximum size, in octets, of the payload. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sdu\_interval](#a4a6d6cdea56a69a0b3b3fd021489750d) |
|  | The interval, in microseconds, of periodic SDUs. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_sdu](#a9fddcb74f3de7eb857583a0179427f84) |
|  | Maximum size of an SDU, in octets. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#a2cbaf6a89e8aaf62c7048e04523e57d4) |
|  | Channel PHY. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [framing](#a1084c209d122d2d13244b77659ce28dd) |
|  | Channel framing mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [encryption](#a7d54ecb896c0d6bc590311d5d5a3ac7b) |
|  | Whether or not the BIG is encrypted. |

## Detailed Description

Broadcast Isochronous Group (BIG) information.

## Field Documentation

## [◆ ](#aa7dbfd342eecf8ffc2fce9d3fa7209ea)addr

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_iso\_biginfo::addr |
| --- |

Address of the advertiser.

## [◆ ](#ad114dd97500d12242da77e8522133953)burst\_number

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_biginfo::burst\_number |
| --- |

The number of new payloads in each BIS event.

## [◆ ](#a7d54ecb896c0d6bc590311d5d5a3ac7b)encryption

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_iso\_biginfo::encryption |
| --- |

Whether or not the BIG is encrypted.

## [◆ ](#a1084c209d122d2d13244b77659ce28dd)framing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_biginfo::framing |
| --- |

Channel framing mode.

## [◆ ](#afe96caf570314731f6c543b40d7def9a)iso\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_biginfo::iso\_interval |
| --- |

Interval between two BIG anchor point (N \* 1.25 ms).

## [◆ ](#af356aa29aa82c8deb63a9f47e54070a1)max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_biginfo::max\_pdu |
| --- |

Maximum size, in octets, of the payload.

## [◆ ](#a9fddcb74f3de7eb857583a0179427f84)max\_sdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_biginfo::max\_sdu |
| --- |

Maximum size of an SDU, in octets.

## [◆ ](#a10eb24596a4353da3feb0d30fed35ae7)num\_bis

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_biginfo::num\_bis |
| --- |

Number of BISes in the BIG.

## [◆ ](#a4efb91dc2f249e41c65cd0dcbfe45bad)offset

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_biginfo::offset |
| --- |

Offset used for pre-transmissions.

## [◆ ](#a2cbaf6a89e8aaf62c7048e04523e57d4)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_biginfo::phy |
| --- |

Channel PHY.

## [◆ ](#a8458f6d6ebe936212d928caca61b13bd)rep\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_biginfo::rep\_count |
| --- |

The number of times a payload is transmitted in a BIS event.

## [◆ ](#a4a6d6cdea56a69a0b3b3fd021489750d)sdu\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_biginfo::sdu\_interval |
| --- |

The interval, in microseconds, of periodic SDUs.

## [◆ ](#a78e0a53f920980081d7b0702b02cf386)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_biginfo::sid |
| --- |

Advertiser SID.

## [◆ ](#a24eb83f7b54e9f949cc07e9955b4a8b8)sub\_evt\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_biginfo::sub\_evt\_count |
| --- |

Maximum number of subevents in each isochronous event.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_biginfo](structbt__iso__biginfo.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
