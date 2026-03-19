---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structieee802154__header__ie__rendezvous__time.html
original_path: doxygen/html/structieee802154__header__ie__rendezvous__time.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_header\_ie\_rendezvous\_time Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

Rendezvous Time IE, see section 7.4.2.6.
[More...](#details)

`#include <[ieee802154_ie.h](ieee802154__ie_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct [ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md)   [full](#ad977678922a3cecd1159a9089c5d41b5) |  |
|  | Rendezvous time full information. [More...](#ad977678922a3cecd1159a9089c5d41b5) |
| struct [ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md)   [reduced](#a620857d35fb7dd3a56d193c7f056e4b5) |  |
|  | Rendezvous time reduced information. [More...](#a620857d35fb7dd3a56d193c7f056e4b5) |
| }; |  |

## Detailed Description

Rendezvous Time IE, see section 7.4.2.6.

## Field Documentation

## [◆ ](#ac52322722b1ecd41dd43a33aaecc4e08)[union]

| union { ... } [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md) |
| --- |

## [◆ ](#ad977678922a3cecd1159a9089c5d41b5)full

| struct [ieee802154\_header\_ie\_rendezvous\_time\_full](structieee802154__header__ie__rendezvous__time__full.md) ieee802154\_header\_ie\_rendezvous\_time::full |
| --- |

Rendezvous time full information.

## [◆ ](#a620857d35fb7dd3a56d193c7f056e4b5)reduced

| struct [ieee802154\_header\_ie\_rendezvous\_time\_reduced](structieee802154__header__ie__rendezvous__time__reduced.md) ieee802154\_header\_ie\_rendezvous\_time::reduced |
| --- |

Rendezvous time reduced information.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_ie.h](ieee802154__ie_8h_source.md)

- [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
