---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__rfcomm__rpn.html
original_path: doxygen/html/structbt__rfcomm__rpn.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_rfcomm\_rpn Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [RFCOMM](group__bt__rfcomm.md)

RFCOMM Remote Port Negotiation (RPN) structure.
[More...](#details)

`#include <[zephyr/bluetooth/classic/rfcomm.h](rfcomm_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dlci](#afacd73edbb63e3ade9573100967faffa) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [baud\_rate](#aad2f64edcb82e864293869474d20fa81) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [line\_settings](#acd61f81d3de1fe4da58fd5ee0d4e5e77) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flow\_control](#ae0db46df73fae846cb53f8a0cf01350a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [xon\_char](#ae637cd243e9b016231b5071e171b6b54) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [xoff\_char](#adc651e1ac74d616fd03b07a647139296) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [param\_mask](#a9eaac13558a5be2fed82084e0bb7a20a) |

## Detailed Description

RFCOMM Remote Port Negotiation (RPN) structure.

## Field Documentation

## [◆ ](#aad2f64edcb82e864293869474d20fa81)baud\_rate

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_rpn::baud\_rate |
| --- |

## [◆ ](#afacd73edbb63e3ade9573100967faffa)dlci

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_rpn::dlci |
| --- |

## [◆ ](#ae0db46df73fae846cb53f8a0cf01350a)flow\_control

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_rpn::flow\_control |
| --- |

## [◆ ](#acd61f81d3de1fe4da58fd5ee0d4e5e77)line\_settings

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_rpn::line\_settings |
| --- |

## [◆ ](#a9eaac13558a5be2fed82084e0bb7a20a)param\_mask

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_rfcomm\_rpn::param\_mask |
| --- |

## [◆ ](#adc651e1ac74d616fd03b07a647139296)xoff\_char

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_rpn::xoff\_char |
| --- |

## [◆ ](#ae637cd243e9b016231b5071e171b6b54)xon\_char

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_rfcomm\_rpn::xon\_char |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[rfcomm.h](rfcomm_8h_source.md)

- [bt\_rfcomm\_rpn](structbt__rfcomm__rpn.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
