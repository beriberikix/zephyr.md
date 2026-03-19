---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__proxy.html
original_path: doxygen/html/group__bt__mesh__proxy.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Proxy

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Proxy.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_proxy\_cb](structbt__mesh__proxy__cb.md) |
|  | Callbacks for the Proxy feature. [More...](structbt__mesh__proxy__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_PROXY\_CB\_DEFINE](#ga325b71c3d7ed69952bf760c0288b28ef)(\_name) |
|  | Register a callback structure for Proxy events. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_proxy\_identity\_enable](#ga7fb3c76f1be6943dd4a18f26e8dd18e7) (void) |
|  | Enable advertising with Node Identity. |
| int | [bt\_mesh\_proxy\_private\_identity\_enable](#gaecd529a9fd0df83b3d775d32885802f1) (void) |
|  | Enable advertising with Private Node Identity. |
| int | [bt\_mesh\_proxy\_connect](#ga07d4edf80bdbc39f626f66720035c98b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Allow Proxy Client to auto connect to a network. |
| int | [bt\_mesh\_proxy\_disconnect](#gaa9978d460b31412c96c6c1685729ec4f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Disallow Proxy Client to auto connect to a network. |
| int | [bt\_mesh\_proxy\_solicit](#ga9a72515992af4f93a34a6c1aaf69d8df) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Schedule advertising of Solicitation PDUs. |

## Detailed Description

Proxy.

## Macro Definition Documentation

## [◆ ](#ga325b71c3d7ed69952bf760c0288b28ef)BT\_MESH\_PROXY\_CB\_DEFINE

| #define BT\_MESH\_PROXY\_CB\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[proxy.h](proxy_8h.md)>`

**Value:**

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)( \

[bt\_mesh\_proxy\_cb](structbt__mesh__proxy__cb.md), \_CONCAT(bt\_mesh\_proxy\_cb\_, \_name))

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[bt\_mesh\_proxy\_cb](structbt__mesh__proxy__cb.md)

Callbacks for the Proxy feature.

**Definition** proxy.h:33

Register a callback structure for Proxy events.

Registers a structure with callback functions that gets called on various Proxy events.

Parameters
:   | \_name | Name of callback structure. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga07d4edf80bdbc39f626f66720035c98b)bt\_mesh\_proxy\_connect()

| int bt\_mesh\_proxy\_connect | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[proxy.h](proxy_8h.md)>`

Allow Proxy Client to auto connect to a network.

This API allows a proxy client to auto-connect a given network.

Parameters
:   | net\_idx | Network Key Index |
    | --- | --- |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaa9978d460b31412c96c6c1685729ec4f)bt\_mesh\_proxy\_disconnect()

| int bt\_mesh\_proxy\_disconnect | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[proxy.h](proxy_8h.md)>`

Disallow Proxy Client to auto connect to a network.

This API disallows a proxy client to connect a given network.

Parameters
:   | net\_idx | Network Key Index |
    | --- | --- |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga7fb3c76f1be6943dd4a18f26e8dd18e7)bt\_mesh\_proxy\_identity\_enable()

| int bt\_mesh\_proxy\_identity\_enable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[proxy.h](proxy_8h.md)>`

Enable advertising with Node Identity.

This API requires that GATT Proxy support has been enabled. Once called each subnet will start advertising using Node Identity for the next 60 seconds.

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaecd529a9fd0df83b3d775d32885802f1)bt\_mesh\_proxy\_private\_identity\_enable()

| int bt\_mesh\_proxy\_private\_identity\_enable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[proxy.h](proxy_8h.md)>`

Enable advertising with Private Node Identity.

This API requires that GATT Proxy support has been enabled. Once called each subnet will start advertising using Private Node Identity for the next 60 seconds.

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga9a72515992af4f93a34a6c1aaf69d8df)bt\_mesh\_proxy\_solicit()

| int bt\_mesh\_proxy\_solicit | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[proxy.h](proxy_8h.md)>`

Schedule advertising of Solicitation PDUs.

Once called, the device will schedule advertising Solicitation PDUs for the amount of time defined by `adv_int` \* (`CONFIG_BT_MESH_SOL_ADV_XMIT` + 1), where `adv_int` is 20ms for Bluetooth v5.0 or higher, or 100ms otherwise.

If the number of advertised Solicitation PDUs reached 0xFFFFFF, the advertisements will no longer be started until the node is reprovisioned.

Parameters
:   | net\_idx | Network Key Index |
    | --- | --- |

Returns
:   0 on success, or (negative) error code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
