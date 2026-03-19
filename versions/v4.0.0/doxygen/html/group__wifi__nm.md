---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__wifi__nm.html
original_path: doxygen/html/group__wifi__nm.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Wi-Fi Network Manager API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Wi-Fi Network manager API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [wifi\_nm\_mgd\_iface](structwifi__nm__mgd__iface.md) |
|  | WiFi Network Managed interfaces. [More...](structwifi__nm__mgd__iface.md#details) |
| struct | [wifi\_nm\_instance](structwifi__nm__instance.md) |
|  | WiFi Network manager instance. [More...](structwifi__nm__instance.md#details) |

| Enumerations | |
| --- | --- |
| enum | [wifi\_nm\_iface\_type](#gadba91c7f3ef5027f7d2a01229372a1a1) { [WIFI\_TYPE\_STA](#ggadba91c7f3ef5027f7d2a01229372a1a1aa2aa21793c3c19fd559e469d63ed1468) = 0 , [WIFI\_TYPE\_SAP](#ggadba91c7f3ef5027f7d2a01229372a1a1adf2032231c71212f10a5e2da2345e345) } |
|  | Types of Wi-Fi interface. [More...](#gadba91c7f3ef5027f7d2a01229372a1a1) |

| Functions | |
| --- | --- |
| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | [wifi\_nm\_get\_instance](#ga781238fda024558c8ccb4cd8877467ed) (const char \*name) |
|  | Get a Network manager instance for a given name. |
| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | [wifi\_nm\_get\_instance\_iface](#ga813b6b6cc227115e83b8e632dd39e6f3) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a Network manager instance for a given interface. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [wifi\_nm\_get\_type\_iface](#ga6a598af94e36a1f4ade05d7a18c019f5) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a Wi-Fi type for a given interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_nm\_iface\_is\_sta](#gaa89e5acfa5eebc9267aa7ed2ce3adc39) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the interface is a Wi-Fi station interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_nm\_iface\_is\_sap](#ga963f646981e9a64c9e61659e40c9880e) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the interface is a Wi-Fi Soft AP interface. |
| int | [wifi\_nm\_register\_mgd\_iface](#ga26edd4cbb045a87613b79f8edd8e9dbb) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface) |
|  | Register a managed interface. |
| int | [wifi\_nm\_register\_mgd\_type\_iface](#gafea087a6c50d6ad05933ef62546868d6) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, enum [wifi\_nm\_iface\_type](#gadba91c7f3ef5027f7d2a01229372a1a1) type, struct [net\_if](structnet__if.md) \*iface) |
|  | Register a managed interface. |
| int | [wifi\_nm\_unregister\_mgd\_iface](#ga467b630fa57bb5587c0237b9cdf403ff) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface) |
|  | Unregister managed interface. |

## Detailed Description

Wi-Fi Network manager API.

Since
:   3.5

Version
:   0.8.0

## Enumeration Type Documentation

## [◆ ](#gadba91c7f3ef5027f7d2a01229372a1a1)wifi\_nm\_iface\_type

| enum [wifi\_nm\_iface\_type](#gadba91c7f3ef5027f7d2a01229372a1a1) |
| --- |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Types of Wi-Fi interface.

| Enumerator | |
| --- | --- |
| WIFI\_TYPE\_STA | IEEE 802.11 Wi-Fi Station. |
| WIFI\_TYPE\_SAP | IEEE 802.11 Wi-Fi Soft AP. |

## Function Documentation

## [◆ ](#ga781238fda024558c8ccb4cd8877467ed)wifi\_nm\_get\_instance()

| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* wifi\_nm\_get\_instance | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Get a Network manager instance for a given name.

Parameters
:   | name | Name of the Network manager instance |
    | --- | --- |

## [◆ ](#ga813b6b6cc227115e83b8e632dd39e6f3)wifi\_nm\_get\_instance\_iface()

| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* wifi\_nm\_get\_instance\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Get a Network manager instance for a given interface.

Parameters
:   | iface | Interface |
    | --- | --- |

## [◆ ](#ga6a598af94e36a1f4ade05d7a18c019f5)wifi\_nm\_get\_type\_iface()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char wifi\_nm\_get\_type\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Get a Wi-Fi type for a given interface.

Parameters
:   | iface | Interface |
    | --- | --- |

## [◆ ](#ga963f646981e9a64c9e61659e40c9880e)wifi\_nm\_iface\_is\_sap()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_nm\_iface\_is\_sap | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Check if the interface is a Wi-Fi Soft AP interface.

Parameters
:   | iface | Interface |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If the interface is a Wi-Fi Soft AP interface. |
    | --- | --- |

## [◆ ](#gaa89e5acfa5eebc9267aa7ed2ce3adc39)wifi\_nm\_iface\_is\_sta()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_nm\_iface\_is\_sta | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Check if the interface is a Wi-Fi station interface.

Parameters
:   | iface | Interface |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If the interface is a Wi-Fi station interface. |
    | --- | --- |

## [◆ ](#ga26edd4cbb045a87613b79f8edd8e9dbb)wifi\_nm\_register\_mgd\_iface()

| int wifi\_nm\_register\_mgd\_iface | ( | struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | *nm*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface* ) |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Register a managed interface.

Parameters
:   | nm | Pointer to Network manager instance |
    | --- | --- |
    | iface | Managed interface |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If invalid parameters were passed. |
    | -ENOTSUP | If the interface is not a Wi-Fi interface. |
    | -ENOMEM | If the maximum number of managed interfaces has been reached. |

## [◆ ](#gafea087a6c50d6ad05933ef62546868d6)wifi\_nm\_register\_mgd\_type\_iface()

| int wifi\_nm\_register\_mgd\_type\_iface | ( | struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | *nm*, |
| --- | --- | --- | --- |
|  |  | enum [wifi\_nm\_iface\_type](#gadba91c7f3ef5027f7d2a01229372a1a1) | *type*, |
|  |  | struct [net\_if](structnet__if.md) \* | *iface* ) |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Register a managed interface.

Parameters
:   | nm | Pointer to Network manager instance |
    | --- | --- |
    | type | Wi-Fi type |
    | iface | Managed interface |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If invalid parameters were passed. |
    | -ENOTSUP | If the interface is not a Wi-Fi interface. |
    | -ENOMEM | If the maximum number of managed interfaces has been reached. |

## [◆ ](#ga467b630fa57bb5587c0237b9cdf403ff)wifi\_nm\_unregister\_mgd\_iface()

| int wifi\_nm\_unregister\_mgd\_iface | ( | struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | *nm*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface* ) |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

Unregister managed interface.

Parameters
:   | nm | Pointer to Network manager instance |
    | --- | --- |
    | iface | Interface |

Returns
:   int 0 for OK; -EINVAL for invalid parameters; -ENOENT if interface is not registered with the Network manager.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
