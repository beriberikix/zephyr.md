---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structieee802154__header__ie__csl.html
original_path: doxygen/html/structieee802154__header__ie__csl.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_header\_ie\_csl Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

Generic CSL IE, see section 7.4.2.3.
[More...](#details)

`#include <[ieee802154_ie.h](ieee802154__ie_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct [ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md)   [full](#abb040a32c97c219ae0674a30ce3c916b) |  |
|  | CSL full information. [More...](#abb040a32c97c219ae0674a30ce3c916b) |
| struct [ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md)   [reduced](#a8373e14f7c6cd1dfe8cd214dfa5d0676) |  |
|  | CSL reduced information. [More...](#a8373e14f7c6cd1dfe8cd214dfa5d0676) |
| }; |  |

## Detailed Description

Generic CSL IE, see section 7.4.2.3.

## Field Documentation

## [◆ ](#aa325120993785fd17e1c49b74c2fdc4f)[union]

| union { ... } [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md) |
| --- |

## [◆ ](#abb040a32c97c219ae0674a30ce3c916b)full

| struct [ieee802154\_header\_ie\_csl\_full](structieee802154__header__ie__csl__full.md) ieee802154\_header\_ie\_csl::full |
| --- |

CSL full information.

## [◆ ](#a8373e14f7c6cd1dfe8cd214dfa5d0676)reduced

| struct [ieee802154\_header\_ie\_csl\_reduced](structieee802154__header__ie__csl__reduced.md) ieee802154\_header\_ie\_csl::reduced |
| --- |

CSL reduced information.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_ie.h](ieee802154__ie_8h_source.md)

- [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
