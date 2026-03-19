---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structieee802154__attr__value.html
original_path: doxygen/html/structieee802154__attr__value.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_attr\_value Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

IEEE 802.15.4 driver attribute values.
[More...](#details)

`#include <[ieee802154_radio.h](ieee802154__radio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [phy\_supported\_channel\_pages](#a75913597f93de1a80f96bb9dc32d38df) |  |
|  | A bit field that represents the supported channel pages, see [ieee802154\_phy\_channel\_page](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9 "ieee802154_phy_channel_page"). [More...](#a75913597f93de1a80f96bb9dc32d38df) |
| const struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md) \*   [phy\_supported\_channels](#a840d2f3a2502f87806ef79c6926f73f0) |  |
|  | Pointer to a structure representing channel ranges currently available on the selected channel page. [More...](#a840d2f3a2502f87806ef79c6926f73f0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [phy\_hrp\_uwb\_supported\_nominal\_prfs](#af157805fb8acffb634cba4b37472bdb3) |  |
|  | A bit field representing supported HRP UWB pulse repetition frequencies (PRF), see enum [ieee802154\_phy\_hrp\_uwb\_nominal\_prf](group__ieee802154__driver.md#ga13610aeef06372bc47d84464537fdded "represents the nominal pulse rate frequency of an HRP UWB PHY"). [More...](#af157805fb8acffb634cba4b37472bdb3) |
| }; |  |

## Detailed Description

IEEE 802.15.4 driver attribute values.

This structure is reserved to scalar and structured attributes that originate in the driver implementation and can neither be implemented as boolean [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4 "ieee802154_hw_caps") nor be derived directly or indirectly by the MAC (L2) layer. In particular this structure MUST NOT be used to return configuration data that originate from L2.

Note
:   To keep this union reasonably small, any attribute requiring a large memory area, SHALL be provided pointing to static memory allocated by the driver and valid throughout the lifetime of the driver instance.

## Field Documentation

## [◆ ](#a21799efa85150124b6333ac5c91d5f80)[union]

| union { ... } [ieee802154\_attr\_value](structieee802154__attr__value.md) |
| --- |

## [◆ ](#af157805fb8acffb634cba4b37472bdb3)phy\_hrp\_uwb\_supported\_nominal\_prfs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ieee802154\_attr\_value::phy\_hrp\_uwb\_supported\_nominal\_prfs |
| --- |

A bit field representing supported HRP UWB pulse repetition frequencies (PRF), see enum [ieee802154\_phy\_hrp\_uwb\_nominal\_prf](group__ieee802154__driver.md#ga13610aeef06372bc47d84464537fdded "represents the nominal pulse rate frequency of an HRP UWB PHY").

Note
:   Currently none of the Zephyr HRP UWB drivers implements more than one nominal PRF at runtime, therefore only one bit will be set and the current PRF (UwbPrf, MCPS-DATA.request, section 8.3.2, table 8-88) is considered to be read-only, fixed and "well known" via the supported PRF attribute.

## [◆ ](#a75913597f93de1a80f96bb9dc32d38df)phy\_supported\_channel\_pages

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ieee802154\_attr\_value::phy\_supported\_channel\_pages |
| --- |

A bit field that represents the supported channel pages, see [ieee802154\_phy\_channel\_page](group__ieee802154__driver.md#gacabc7386bea701373dfb36ab65bd36a9 "ieee802154_phy_channel_page").

Note
:   To keep the API extensible as required by the standard, supported pages are modeled as a bitmap to support drivers that implement runtime switching between multiple channel pages.
:   Currently none of the Zephyr drivers implements more than one channel page at runtime, therefore only one bit will be set and the current channel page (see the PHY PIB attribute phyCurrentPage, section 11.3, table 11-2) is considered to be read-only, fixed and "well known" via the supported channel pages attribute.

## [◆ ](#a840d2f3a2502f87806ef79c6926f73f0)phy\_supported\_channels

| const struct [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md)\* ieee802154\_attr\_value::phy\_supported\_channels |
| --- |

Pointer to a structure representing channel ranges currently available on the selected channel page.

Warning
:   The pointer must be valid and constant throughout the life of the interface.

The selected channel page corresponds to the phyCurrentPage PHY PIB attribute, see the description of phy\_supported\_channel\_pages above. Currently it can be retrieved via the [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_PAGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430a4ad28f920776c45af9d430db786a926a "IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_PAGES") attribute.

Most drivers will expose a single channel page with a single, often zero-based, fixed channel range.

Some notable exceptions:

- The legacy channel page (zero) exposes ranges in different bands and even PHYs that are usually not implemented by a single driver.
- SUN and LECIM PHYs specify a large number of bands and operating modes on a single page with overlapping channel ranges each. Some of these ranges are not zero-based or contain "holes". This explains why several ranges may be necessary to represent all available channels.
- UWB PHYs often support partial channel ranges on the same channel page depending on the supported bands.

In these cases, drivers may expose custom configuration attributes (Kconfig, devicetree, runtime, ...) that allow switching between sub-ranges within the same channel page (e.g. switching between SubG and 2.4G bands on channel page zero or switching between multiple operating modes in the SUN or LECIM PHYs.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_radio.h](ieee802154__radio_8h_source.md)

- [ieee802154\_attr\_value](structieee802154__attr__value.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
