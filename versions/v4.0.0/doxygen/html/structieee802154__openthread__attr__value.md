---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structieee802154__openthread__attr__value.html
original_path: doxygen/html/structieee802154__openthread__attr__value.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_openthread\_attr\_value Struct Reference

OpenThread specific attribute value data of ieee802154 driver.
[More...](#details)

`#include <[ieee802154_radio_openthread.h](ieee802154__radio__openthread_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct [ieee802154\_attr\_value](structieee802154__attr__value.md)   [common](#a794c867bf25cd23b9b1797d995696c8a) |  |
|  | Common attribute value. [More...](#a794c867bf25cd23b9b1797d995696c8a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [t\_recca](#a84f1a03b847ff2050f38a59573a00cd8) |  |
|  | Attribute value for [IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5 "IEEE802154_OPENTHREAD_ATTR_T_RECCA"). [More...](#a84f1a03b847ff2050f38a59573a00cd8) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [t\_ccatx](#a423bc2cc48ceead6a6febd7f78504843) |  |
|  | Attribute value for [IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b "IEEE802154_OPENTHREAD_ATTR_T_CCATX"). [More...](#a423bc2cc48ceead6a6febd7f78504843) |
| }; |  |

## Detailed Description

OpenThread specific attribute value data of ieee802154 driver.

This type extends [ieee802154\_attr\_value](structieee802154__attr__value.md "ieee802154_attr_value")

## Field Documentation

## [◆ ](#ab5416f1746e6758118f41db80a5a6392)[union]

| union { ... } [ieee802154\_openthread\_attr\_value](structieee802154__openthread__attr__value.md) |
| --- |

## [◆ ](#a794c867bf25cd23b9b1797d995696c8a)common

| struct [ieee802154\_attr\_value](structieee802154__attr__value.md) ieee802154\_openthread\_attr\_value::common |
| --- |

Common attribute value.

## [◆ ](#a423bc2cc48ceead6a6febd7f78504843)t\_ccatx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_openthread\_attr\_value::t\_ccatx |
| --- |

Attribute value for [IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b "IEEE802154_OPENTHREAD_ATTR_T_CCATX").

## [◆ ](#a84f1a03b847ff2050f38a59573a00cd8)t\_recca

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_openthread\_attr\_value::t\_recca |
| --- |

Attribute value for [IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5 "IEEE802154_OPENTHREAD_ATTR_T_RECCA").

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_radio\_openthread.h](ieee802154__radio__openthread_8h_source.md)

- [ieee802154\_openthread\_attr\_value](structieee802154__openthread__attr__value.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
