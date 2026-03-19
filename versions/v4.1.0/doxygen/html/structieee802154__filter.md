---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structieee802154__filter.html
original_path: doxygen/html/structieee802154__filter.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_filter Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

Filter value, see [ieee802154\_radio\_api::filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3 "ieee802154_radio_api::filter").
[More...](#details)

`#include <[ieee802154_radio.h](ieee802154__radio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [ieee\_addr](#a636ec85ca79b2880de51ed93f6788909) |  |
|  | Extended address, in little endian. [More...](#a636ec85ca79b2880de51ed93f6788909) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [short\_addr](#a16a1779ff43accda31bba35b9bdd61c3) |  |
|  | Short address, in CPU byte order. [More...](#a16a1779ff43accda31bba35b9bdd61c3) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [pan\_id](#a40f77239924af29d40f7595e23475e9b) |  |
|  | PAN ID, in CPU byte order. [More...](#a40f77239924af29d40f7595e23475e9b) |
| }; |  |

## Detailed Description

Filter value, see [ieee802154\_radio\_api::filter](structieee802154__radio__api.md#aa9502e0e014a8d05ffe235567e8c98f3 "ieee802154_radio_api::filter").

## Field Documentation

## [◆ ](#a16b217049a2aaa4193a2a994533e235e)[union]

| union { ... } [ieee802154\_filter](structieee802154__filter.md) |
| --- |

## [◆ ](#a636ec85ca79b2880de51ed93f6788909)ieee\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* ieee802154\_filter::ieee\_addr |
| --- |

Extended address, in little endian.

## [◆ ](#a40f77239924af29d40f7595e23475e9b)pan\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_filter::pan\_id |
| --- |

PAN ID, in CPU byte order.

## [◆ ](#a16a1779ff43accda31bba35b9bdd61c3)short\_addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_filter::short\_addr |
| --- |

Short address, in CPU byte order.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_radio.h](ieee802154__radio_8h_source.md)

- [ieee802154\_filter](structieee802154__filter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
