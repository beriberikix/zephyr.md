---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnxp__enet__qos__config.html
original_path: doxygen/html/structnxp__enet__qos__config.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_enet\_qos\_config Struct Reference

`#include <[eth_nxp_enet_qos.h](eth__nxp__enet__qos_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \* | [pincfg](#aee279c78eb397e48b8bb98e34ee74ed6) |
| const struct [device](structdevice.md) \* | [clock\_dev](#adccf48e699c07360b1d6989b3e99b271) |
| [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) | [clock\_subsys](#a60394ad2fbfe59bcfc1c36d403be1c01) |
| enet\_qos\_t \* | [base](#a45491916ea24ab9b99fe2fc14cf94552) |

## Field Documentation

## [◆ ](#a45491916ea24ab9b99fe2fc14cf94552)base

| enet\_qos\_t\* nxp\_enet\_qos\_config::base |
| --- |

## [◆ ](#adccf48e699c07360b1d6989b3e99b271)clock\_dev

| const struct [device](structdevice.md)\* nxp\_enet\_qos\_config::clock\_dev |
| --- |

## [◆ ](#a60394ad2fbfe59bcfc1c36d403be1c01)clock\_subsys

| [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) nxp\_enet\_qos\_config::clock\_subsys |
| --- |

## [◆ ](#aee279c78eb397e48b8bb98e34ee74ed6)pincfg

| const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md)\* nxp\_enet\_qos\_config::pincfg |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/ethernet/[eth\_nxp\_enet\_qos.h](eth__nxp__enet__qos_8h_source.md)

- [nxp\_enet\_qos\_config](structnxp__enet__qos__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
