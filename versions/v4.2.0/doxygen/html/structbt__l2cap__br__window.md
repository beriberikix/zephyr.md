---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__l2cap__br__window.html
original_path: doxygen/html/structbt__l2cap__br__window.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_l2cap\_br\_window Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [L2CAP](group__bt__l2cap.md)

I-Frame transmission window for none BASIC mode L2cap connected channel.
[More...](#details)

`#include <[zephyr/bluetooth/l2cap.h](l2cap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#acff85df74b031445a69c75cad1765e90) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_seq](#afb66e50f934e763680200ce209ca940c) |
|  | tx seq |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#a781e76efc763c70a9c716f4737fb9243) |
|  | data len |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#a3332cc2a424d1e2d1438232594b81a95) |
|  | data address |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [transmit\_counter](#ab7bb9eb3949b37973228630b8acacd2f) |
|  | Transmit Counter. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sar](#ac2deea3f4fd7893408412ff6599c1a1a) |
|  | SAR flag. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [srej](#a39456c041bd7d8badde949008835f891) |
|  | srej flag |
| struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) | [sdu\_state](#a65acb18fd339978960419ffb2c95111e) |
| struct [net\_buf](structnet__buf.md) \* | [sdu](#affc53286b080a6914935577ffc15959c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sdu\_total\_len](#a3b0a68d77f21c9b02dec816f2c37a479) |

## Detailed Description

I-Frame transmission window for none BASIC mode L2cap connected channel.

## Field Documentation

## [◆ ](#a3332cc2a424d1e2d1438232594b81a95)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_l2cap\_br\_window::data |
| --- |

data address

## [◆ ](#a781e76efc763c70a9c716f4737fb9243)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_window::len |
| --- |

data len

## [◆ ](#acff85df74b031445a69c75cad1765e90)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_l2cap\_br\_window::node |
| --- |

## [◆ ](#ac2deea3f4fd7893408412ff6599c1a1a)sar

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_l2cap\_br\_window::sar |
| --- |

SAR flag.

## [◆ ](#affc53286b080a6914935577ffc15959c)sdu

| struct [net\_buf](structnet__buf.md)\* bt\_l2cap\_br\_window::sdu |
| --- |

## [◆ ](#a65acb18fd339978960419ffb2c95111e)sdu\_state

| struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) bt\_l2cap\_br\_window::sdu\_state |
| --- |

## [◆ ](#a3b0a68d77f21c9b02dec816f2c37a479)sdu\_total\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_window::sdu\_total\_len |
| --- |

## [◆ ](#a39456c041bd7d8badde949008835f891)srej

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_l2cap\_br\_window::srej |
| --- |

srej flag

## [◆ ](#ab7bb9eb3949b37973228630b8acacd2f)transmit\_counter

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_l2cap\_br\_window::transmit\_counter |
| --- |

Transmit Counter.

## [◆ ](#afb66e50f934e763680200ce209ca940c)tx\_seq

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_l2cap\_br\_window::tx\_seq |
| --- |

tx seq

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[l2cap.h](l2cap_8h_source.md)

- [bt\_l2cap\_br\_window](structbt__l2cap__br__window.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
