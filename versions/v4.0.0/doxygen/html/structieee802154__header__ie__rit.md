---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structieee802154__header__ie__rit.html
original_path: doxygen/html/structieee802154__header__ie__rit.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_header\_ie\_rit Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

RIT IE, see section 7.4.2.4.
[More...](#details)

`#include <[ieee802154_ie.h](ieee802154__ie_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [time\_to\_first\_listen](#a94efc1605d6799a9d88e6cb801f7ec0b) |
|  | Time to First Listen. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [number\_of\_repeat\_listen](#a5eaca9e09ebdbb933b4324c899c248b4) |
|  | Number of Repeat Listen. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [repeat\_listen\_interval](#a73cd396d5e98799b655242f525ccf42b) |
|  | Repeat listen interval. |

## Detailed Description

RIT IE, see section 7.4.2.4.

## Field Documentation

## [◆ ](#a5eaca9e09ebdbb933b4324c899c248b4)number\_of\_repeat\_listen

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_header\_ie\_rit::number\_of\_repeat\_listen |
| --- |

Number of Repeat Listen.

## [◆ ](#a73cd396d5e98799b655242f525ccf42b)repeat\_listen\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_header\_ie\_rit::repeat\_listen\_interval |
| --- |

Repeat listen interval.

## [◆ ](#a94efc1605d6799a9d88e6cb801f7ec0b)time\_to\_first\_listen

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_header\_ie\_rit::time\_to\_first\_listen |
| --- |

Time to First Listen.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_ie.h](ieee802154__ie_8h_source.md)

- [ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
