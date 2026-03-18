---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__wifi__nm.html
original_path: doxygen/html/group__wifi__nm.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| struct | [wifi\_nm\_instance](structwifi__nm__instance.md) |
|  | WiFi Network manager instance. [More...](structwifi__nm__instance.md#details) |

| Macros | |
| --- | --- |
| #define | [WIFI\_NM\_NAME](#ga476afa0a50621396bc959d9cc7eca19f)(name) |
| #define | [DEFINE\_WIFI\_NM\_INSTANCE](#ga618fa06395943215db2fa96cbfa3fc99)(\_name, \_ops) |

| Functions | |
| --- | --- |
| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | [wifi\_nm\_get\_instance](#ga781238fda024558c8ccb4cd8877467ed) (const char \*name) |
|  | Get a Network manager instance for a given name. |
| struct [wifi\_nm\_instance](structwifi__nm__instance.md) \* | [wifi\_nm\_get\_instance\_iface](#ga813b6b6cc227115e83b8e632dd39e6f3) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a Network manager instance for a given interface. |
| int | [wifi\_nm\_register\_mgd\_iface](#ga26edd4cbb045a87613b79f8edd8e9dbb) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface) |
|  | Register a managed interface. |
| int | [wifi\_nm\_unregister\_mgd\_iface](#ga467b630fa57bb5587c0237b9cdf403ff) (struct [wifi\_nm\_instance](structwifi__nm__instance.md) \*nm, struct [net\_if](structnet__if.md) \*iface) |
|  | Unregister managed interface. |

## Detailed Description

Wi-Fi Network manager API.

## Macro Definition Documentation

## [◆ ](#ga618fa06395943215db2fa96cbfa3fc99)DEFINE\_WIFI\_NM\_INSTANCE

| #define DEFINE\_WIFI\_NM\_INSTANCE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_ops* ) |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([wifi\_nm\_instance](structwifi__nm__instance.md), [WIFI\_NM\_NAME](#ga476afa0a50621396bc959d9cc7eca19f)(\_name)) = { \

.name = [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), \

.ops = \_ops, \

.mgd\_ifaces = { NULL }, \

}

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[WIFI\_NM\_NAME](#ga476afa0a50621396bc959d9cc7eca19f)

#define WIFI\_NM\_NAME(name)

**Definition** wifi\_nm.h:45

[wifi\_nm\_instance](structwifi__nm__instance.md)

WiFi Network manager instance.

**Definition** wifi\_nm.h:36

## [◆ ](#ga476afa0a50621396bc959d9cc7eca19f)WIFI\_NM\_NAME

| #define WIFI\_NM\_NAME | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_nm.h](wifi__nm_8h.md)>`

**Value:**

wifi\_nm\_##name

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
