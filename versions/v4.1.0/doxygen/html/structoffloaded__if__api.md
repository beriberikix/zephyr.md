---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structoffloaded__if__api.html
original_path: doxygen/html/structoffloaded__if__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

offloaded\_if\_api Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Offloaded Net Devices](group__offloaded__netdev.md)

Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state changes.
[More...](#details)

`#include <[offloaded_netdev.h](offloaded__netdev_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_if\_api | [iface\_api](#a24cc2bd70d18075731be617955e3e1a8) |
|  | The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API. |
| int(\* | [enable](#aadf471a8e3ae22f3294df1cab090a7a3) )(const struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Enable or disable the device (in response to admin state change). |
| enum [offloaded\_net\_if\_types](group__offloaded__netdev.md#gac1980977f6da3ace33ede7949d43f81f)(\* | [get\_type](#a5ae87a9ed455f62958e1f2fa8cb715e7) )(void) |
|  | Types of offloaded net device. |

## Detailed Description

Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state changes.

## Field Documentation

## [◆ ](#aadf471a8e3ae22f3294df1cab090a7a3)enable

| int(\* offloaded\_if\_api::enable) (const struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Enable or disable the device (in response to admin state change).

## [◆ ](#a5ae87a9ed455f62958e1f2fa8cb715e7)get\_type

| enum [offloaded\_net\_if\_types](group__offloaded__netdev.md#gac1980977f6da3ace33ede7949d43f81f)(\* offloaded\_if\_api::get\_type) (void) |
| --- |

Types of offloaded net device.

## [◆ ](#a24cc2bd70d18075731be617955e3e1a8)iface\_api

| struct net\_if\_api offloaded\_if\_api::iface\_api |
| --- |

The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[offloaded\_netdev.h](offloaded__netdev_8h_source.md)

- [offloaded\_if\_api](structoffloaded__if__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
