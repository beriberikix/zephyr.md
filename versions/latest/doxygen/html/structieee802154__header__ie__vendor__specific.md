---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structieee802154__header__ie__vendor__specific.html
original_path: doxygen/html/structieee802154__header__ie__vendor__specific.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_header\_ie\_vendor\_specific Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

Vendor Specific Header IE, see section 7.4.2.3.
[More...](#details)

`#include <[ieee802154_ie.h](ieee802154__ie_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [vendor\_oui](#a52d5ef47cbf674438bdc59aff40d0cbe) [IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [vendor\_specific\_info](#a7227c96e07f5cd26353d10710d5a8db1) |

## Detailed Description

Vendor Specific Header IE, see section 7.4.2.3.

## Field Documentation

## [◆ ](#a52d5ef47cbf674438bdc59aff40d0cbe)vendor\_oui

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_header\_ie\_vendor\_specific::vendor\_oui[IEEE802154\_VENDOR\_SPECIFIC\_IE\_OUI\_LEN] |
| --- |

## [◆ ](#a7227c96e07f5cd26353d10710d5a8db1)vendor\_specific\_info

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* ieee802154\_header\_ie\_vendor\_specific::vendor\_specific\_info |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_ie.h](ieee802154__ie_8h_source.md)

- [ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
