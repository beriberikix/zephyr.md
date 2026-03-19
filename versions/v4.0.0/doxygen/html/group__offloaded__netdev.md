---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__offloaded__netdev.html
original_path: doxygen/html/group__offloaded__netdev.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Offloaded Net Devices

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Offloaded Net Devices.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [offloaded\_if\_api](structoffloaded__if__api.md) |
|  | Extended net\_if\_api for offloaded ifaces/network devices, allowing handling of admin up/down state changes. [More...](structoffloaded__if__api.md#details) |

| Enumerations | |
| --- | --- |
| enum | [offloaded\_net\_if\_types](#gac1980977f6da3ace33ede7949d43f81f) { [L2\_OFFLOADED\_NET\_IF\_TYPE\_UNKNOWN](#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d) , [L2\_OFFLOADED\_NET\_IF\_TYPE\_ETHERNET](#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a) , [L2\_OFFLOADED\_NET\_IF\_TYPE\_MODEM](#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21) , [L2\_OFFLOADED\_NET\_IF\_TYPE\_WIFI](#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24) } |
|  | Types of offloaded netdev L2. [More...](#gac1980977f6da3ace33ede7949d43f81f) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_off\_is\_wifi\_offloaded](#gad1076eacf1b1e82f70759f9b54937ced) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the offloaded network interface supports Wi-Fi. |

## Detailed Description

Offloaded Net Devices.

Since
:   3.4

Version
:   0.8.0

## Enumeration Type Documentation

## [◆ ](#gac1980977f6da3ace33ede7949d43f81f)offloaded\_net\_if\_types

| enum [offloaded\_net\_if\_types](#gac1980977f6da3ace33ede7949d43f81f) |
| --- |

`#include <[offloaded_netdev.h](offloaded__netdev_8h.md)>`

Types of offloaded netdev L2.

| Enumerator | |
| --- | --- |
| L2\_OFFLOADED\_NET\_IF\_TYPE\_UNKNOWN | Unknown, device hasn't register a type. |
| L2\_OFFLOADED\_NET\_IF\_TYPE\_ETHERNET | Ethernet devices. |
| L2\_OFFLOADED\_NET\_IF\_TYPE\_MODEM | Modem. |
| L2\_OFFLOADED\_NET\_IF\_TYPE\_WIFI | IEEE 802.11 Wi-Fi. |

## Function Documentation

## [◆ ](#gad1076eacf1b1e82f70759f9b54937ced)net\_off\_is\_wifi\_offloaded()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_off\_is\_wifi\_offloaded | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[offloaded_netdev.h](offloaded__netdev_8h.md)>`

Check if the offloaded network interface supports Wi-Fi.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if interface supports Wi-Fi, False otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
