---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structieee802154__phy__supported__channels.html
original_path: doxygen/html/structieee802154__phy__supported__channels.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_phy\_supported\_channels Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 Drivers](group__ieee802154__driver.md)

Represents a list channels supported by a driver for a given interface, see [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d "IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES").
[More...](#details)

`#include <[ieee802154_radio.h](ieee802154__radio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md) \*const | [ranges](#a73ccabf887b567a0ce3ddc5f8a3eeed1) |
|  | Pointer to an array of channel range structures. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_ranges](#a8fb56a7fc6be96035cf4b51891582da9) |
|  | The number of currently available channel ranges. |

## Detailed Description

Represents a list channels supported by a driver for a given interface, see [IEEE802154\_ATTR\_PHY\_SUPPORTED\_CHANNEL\_RANGES](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430aba76daa0a70bcdd573ecbfd63ca19e7d "IEEE802154_ATTR_PHY_SUPPORTED_CHANNEL_RANGES").

## Field Documentation

## [◆ ](#a8fb56a7fc6be96035cf4b51891582da9)num\_ranges

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_phy\_supported\_channels::num\_ranges |
| --- |

The number of currently available channel ranges.

## [◆ ](#a73ccabf887b567a0ce3ddc5f8a3eeed1)ranges

| const struct [ieee802154\_phy\_channel\_range](structieee802154__phy__channel__range.md)\* const ieee802154\_phy\_supported\_channels::ranges |
| --- |

Pointer to an array of channel range structures.

Warning
:   The pointer must be valid and constant throughout the life of the interface.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_radio.h](ieee802154__radio_8h_source.md)

- [ieee802154\_phy\_supported\_channels](structieee802154__phy__supported__channels.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
