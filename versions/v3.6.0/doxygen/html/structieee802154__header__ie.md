---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structieee802154__header__ie.html
original_path: doxygen/html/structieee802154__header__ie.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_header\_ie Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

`#include <[ieee802154_ie.h](ieee802154__ie_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [element\_id\_low](#ab389f739b6e6f77add4f77786f8c0577): 1 |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [length](#a9c1632eac7955370784445f5571d337d): 7 |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [type](#aa2c087927391e811437028c55141ce94): 1 |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [element\_id\_high](#a8521084dddda0853d3711d5b0dc1eada): 7 |
| union { |  |
| struct [ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md)   [vendor\_specific](#ac932f99fb3b93debde45e1f82d059cf8) |  |
| struct [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md)   [csl](#af73871d2a4c26d6e3cde0c18a74e7006) |  |
| struct [ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md)   [rit](#a0950703553d298a6af00cdb11012146c) |  |
| struct [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md)   [rendezvous\_time](#aecf96d749b103c1c5f702da675bacb26) |  |
| struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md)   [time\_correction](#a6a9c76df7d1e7b082642f10eeb4875af) |  |
| } | [content](#ac2d67fc001eddde667f25ebbf5ef5ce1) |

## Field Documentation

## [◆ ](#ac2d67fc001eddde667f25ebbf5ef5ce1)[union]

| union { ... } ieee802154\_header\_ie::content |
| --- |

## [◆ ](#af73871d2a4c26d6e3cde0c18a74e7006)csl

| struct [ieee802154\_header\_ie\_csl](structieee802154__header__ie__csl.md) ieee802154\_header\_ie::csl |
| --- |

## [◆ ](#a8521084dddda0853d3711d5b0dc1eada)element\_id\_high

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_header\_ie::element\_id\_high |
| --- |

## [◆ ](#ab389f739b6e6f77add4f77786f8c0577)element\_id\_low

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_header\_ie::element\_id\_low |
| --- |

## [◆ ](#a9c1632eac7955370784445f5571d337d)length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_header\_ie::length |
| --- |

## [◆ ](#aecf96d749b103c1c5f702da675bacb26)rendezvous\_time

| struct [ieee802154\_header\_ie\_rendezvous\_time](structieee802154__header__ie__rendezvous__time.md) ieee802154\_header\_ie::rendezvous\_time |
| --- |

## [◆ ](#a0950703553d298a6af00cdb11012146c)rit

| struct [ieee802154\_header\_ie\_rit](structieee802154__header__ie__rit.md) ieee802154\_header\_ie::rit |
| --- |

## [◆ ](#a6a9c76df7d1e7b082642f10eeb4875af)time\_correction

| struct [ieee802154\_header\_ie\_time\_correction](structieee802154__header__ie__time__correction.md) ieee802154\_header\_ie::time\_correction |
| --- |

## [◆ ](#aa2c087927391e811437028c55141ce94)type

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_header\_ie::type |
| --- |

## [◆ ](#ac932f99fb3b93debde45e1f82d059cf8)vendor\_specific

| struct [ieee802154\_header\_ie\_vendor\_specific](structieee802154__header__ie__vendor__specific.md) ieee802154\_header\_ie::vendor\_specific |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_ie.h](ieee802154__ie_8h_source.md)

- [ieee802154\_header\_ie](structieee802154__header__ie.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
