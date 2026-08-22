---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__dsa__core.html
original_path: doxygen/html/group__dsa__core.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Distributed Switch Architecture (DSA)

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Distributed Switch Architecture (DSA).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [dsa\_switch\_context](structdsa__switch__context.md) |
|  | DSA switch context data. [More...](structdsa__switch__context.md#details) |
| struct | [dsa\_api](structdsa__api.md) |
|  | Structure to provide DSA switch api callbacks - it is an augmented struct [ethernet\_api](structethernet__api.md "Ethernet L2 API operations."). [More...](structdsa__api.md#details) |
| struct | [dsa\_port\_config](structdsa__port__config.md) |
|  | Structure of DSA port configuration. [More...](structdsa__port__config.md#details) |

| Macros | |
| --- | --- |
| #define | [DSA\_PORT\_INST\_INIT](#ga012eeda4facb67b5c387b74878b53188)(port, n, cfg) |
|  | Macro for DSA port instance initialization. |
| #define | [DSA\_SWITCH\_INST\_INIT](#gaa7665e4b96cbc40cbae6de621f773aa4)(n, \_dapi, data, fn) |
|  | Macro for DSA switch instance initialization. |

| Functions | |
| --- | --- |
| struct [net\_if](structnet__if.md) \* | [dsa\_user\_get\_iface](#ga16d03129d1e4c39f8662dae4b35598d9) (struct [net\_if](structnet__if.md) \*iface, int port\_idx) |
|  | Get network interface of a user port. |

## Detailed Description

Distributed Switch Architecture (DSA).

Since
:   4.2

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga012eeda4facb67b5c387b74878b53188)DSA\_PORT\_INST\_INIT

| #define DSA\_PORT\_INST\_INIT | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *n*, |
|  |  |  | *cfg* ) |

`#include <[zephyr/net/dsa_core.h](dsa__core_8h.md)>`

**Value:**

[NET\_DEVICE\_INIT\_INSTANCE](group__net__if.md#gacc7edecdd9de9920cc155977d8fec2a2)([CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(dsa\_, n, port), [DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(port), [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(port), \

dsa\_port\_initialize, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), &dsa\_switch\_context\_##n, cfg, \

CONFIG\_ETH\_INIT\_PRIORITY, &dsa\_eth\_api, ETHERNET\_L2, \

NET\_L2\_GET\_CTX\_TYPE(ETHERNET\_L2), [NET\_ETH\_MTU](group__ethernet.md#gaa337199b1edc50c9003afa5c3a951d8b));

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:201

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2461

[NET\_ETH\_MTU](group__ethernet.md#gaa337199b1edc50c9003afa5c3a951d8b)

#define NET\_ETH\_MTU

Ethernet MTU size.

**Definition** ethernet.h:122

[NET\_DEVICE\_INIT\_INSTANCE](group__net__if.md#gacc7edecdd9de9920cc155977d8fec2a2)

#define NET\_DEVICE\_INIT\_INSTANCE(dev\_id, name, instance, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu)

Create multiple network interfaces and bind them to network device.

**Definition** net\_if.h:3598

[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)

#define CONCAT(...)

Concatenate input arguments.

**Definition** util.h:312

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Macro for DSA port instance initialization.

Parameters
:   | port | DSA port node identifier. |
    | --- | --- |
    | n | DSA instance number. |
    | cfg | Pointer to [dsa\_port\_config](structdsa__port__config.md "Structure of DSA port configuration."). |

## [◆ ](#gaa7665e4b96cbc40cbae6de621f773aa4)DSA\_SWITCH\_INST\_INIT

| #define DSA\_SWITCH\_INST\_INIT | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *\_dapi*, |
|  |  |  | *data*, |
|  |  |  | *fn* ) |

`#include <[zephyr/net/dsa_core.h](dsa__core_8h.md)>`

**Value:**

struct [dsa\_switch\_context](structdsa__switch__context.md) dsa\_switch\_context\_##n = { \

.dapi = \_dapi, \

.prv\_data = data, \

.init\_ports = 0, \

.num\_ports = [DT\_INST\_CHILD\_NUM\_STATUS\_OKAY](group__devicetree-inst.md#ga1a54403986077e46684c5198f4d53421)(n), \

}; \

DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(n, fn, n);

[DT\_INST\_CHILD\_NUM\_STATUS\_OKAY](group__devicetree-inst.md#ga1a54403986077e46684c5198f4d53421)

#define DT\_INST\_CHILD\_NUM\_STATUS\_OKAY(inst)

Get the number of child nodes of a given node.

**Definition** devicetree.h:3961

[dsa\_switch\_context](structdsa__switch__context.md)

DSA switch context data.

**Definition** dsa\_core.h:79

Macro for DSA switch instance initialization.

Parameters
:   | n | DSA instance number. |
    | --- | --- |
    | \_dapi | Pointer to [dsa\_api](structdsa__api.md "Structure to provide DSA switch api callbacks - it is an augmented struct ethernet_api."). |
    | data | Pointer to private data. |
    | fn | DSA port instance init function. |

## Function Documentation

## [◆ ](#ga16d03129d1e4c39f8662dae4b35598d9)dsa\_user\_get\_iface()

| struct [net\_if](structnet__if.md) \* dsa\_user\_get\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *port\_idx* ) |

`#include <[zephyr/net/dsa_core.h](dsa__core_8h.md)>`

Get network interface of a user port.

Parameters
:   |  | iface | Conduit port |
    | --- | --- | --- |
    | [in] | port\_idx | Port index |

Returns
:   network interface of the user if successful
:   NULL if user port does not exist

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
