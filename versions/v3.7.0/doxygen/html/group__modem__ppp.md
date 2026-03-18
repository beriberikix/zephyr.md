---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__modem__ppp.html
original_path: doxygen/html/group__modem__ppp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Modem PPP

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md)

Modem PPP.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [MODEM\_PPP\_DEFINE](#ga78bbcfb655ae8009a6abbc8e09dfbcc0)(\_name, \_init\_iface, \_prio, \_mtu, \_buf\_size) |
|  | Define a modem PPP module and bind it to a network interface. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [modem\_ppp\_init\_iface](#gafdd04a06c32e9ab70755d4f2e68deaad)) (struct [net\_if](structnet__if.md) \*iface) |
|  | L2 network interface init callback. |

| Functions | |
| --- | --- |
| int | [modem\_ppp\_attach](#gad3ce02dd0a6cf7067c5ca0341f807f88) (struct modem\_ppp \*ppp, struct modem\_pipe \*pipe) |
|  | Attach pipe to instance and connect. |
| struct [net\_if](structnet__if.md) \* | [modem\_ppp\_get\_iface](#gaebb69341b2b88338b2cfccaa1c0cba0b) (struct modem\_ppp \*ppp) |
|  | Get network interface modem PPP instance is bound to. |
| void | [modem\_ppp\_release](#gaf2177b83100647ed0894cac7fa435cb3) (struct modem\_ppp \*ppp) |
|  | Release pipe from instance. |

## Detailed Description

Modem PPP.

## Macro Definition Documentation

## [◆ ](#ga78bbcfb655ae8009a6abbc8e09dfbcc0)MODEM\_PPP\_DEFINE

| #define MODEM\_PPP\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_init\_iface*, |
|  |  |  | *\_prio*, |
|  |  |  | *\_mtu*, |
|  |  |  | *\_buf\_size* ) |

`#include <[ppp.h](modem_2ppp_8h.md)>`

**Value:**

extern const struct [ppp\_api](structppp__api.md) modem\_ppp\_ppp\_api; \

\

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_CONCAT(\_name, \_receive\_buf)[\_buf\_size]; \

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_CONCAT(\_name, \_transmit\_buf)[\_buf\_size]; \

\

static struct modem\_ppp \_name = { \

.init\_iface = \_init\_iface, \

.receive\_buf = \_CONCAT(\_name, \_receive\_buf), \

.transmit\_buf = \_CONCAT(\_name, \_transmit\_buf), \

.buf\_size = \_buf\_size, \

}; \

\

NET\_DEVICE\_INIT(\_CONCAT(ppp\_net\_dev\_, \_name), "modem\_ppp\_" # \_name, \

modem\_ppp\_init\_internal, NULL, &\_name, NULL, \_prio, &modem\_ppp\_ppp\_api, \

PPP\_L2, NET\_L2\_GET\_CTX\_TYPE(PPP\_L2), \_mtu)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[ppp\_api](structppp__api.md)

PPP L2 API.

**Definition** ppp.h:44

Define a modem PPP module and bind it to a network interface.

This macro defines the modem\_ppp instance, initializes a PPP L2 network device instance, and binds the modem\_ppp instance to the PPP L2 instance.

Parameters
:   | \_name | Name of the statically defined modem\_ppp instance |
    | --- | --- |
    | \_init\_iface | Hook for the PPP L2 network interface init function |
    | \_prio | Initialization priority of the PPP L2 net iface |
    | \_mtu | Max size of [net\_pkt](structnet__pkt.md "Network packet.") data sent and received on PPP L2 net iface |
    | \_buf\_size | Size of partial PPP frame transmit and receive buffers |

## Typedef Documentation

## [◆ ](#gafdd04a06c32e9ab70755d4f2e68deaad)modem\_ppp\_init\_iface

| typedef void(\* modem\_ppp\_init\_iface) (struct [net\_if](structnet__if.md) \*iface) |
| --- |

`#include <[ppp.h](modem_2ppp_8h.md)>`

L2 network interface init callback.

## Function Documentation

## [◆ ](#gad3ce02dd0a6cf7067c5ca0341f807f88)modem\_ppp\_attach()

| int modem\_ppp\_attach | ( | struct modem\_ppp \* | *ppp*, |
| --- | --- | --- | --- |
|  |  | struct modem\_pipe \* | *pipe* ) |

`#include <[ppp.h](modem_2ppp_8h.md)>`

Attach pipe to instance and connect.

Parameters
:   | [PPP L2/driver Support Functions](group__ppp.md "Point-to-point (PPP) L2/driver support functions.") | Modem PPP instance |
    | --- | --- |
    | pipe | Pipe to attach to modem PPP instance |

## [◆ ](#gaebb69341b2b88338b2cfccaa1c0cba0b)modem\_ppp\_get\_iface()

| struct [net\_if](structnet__if.md) \* modem\_ppp\_get\_iface | ( | struct modem\_ppp \* | *ppp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](modem_2ppp_8h.md)>`

Get network interface modem PPP instance is bound to.

Parameters
:   | [PPP L2/driver Support Functions](group__ppp.md "Point-to-point (PPP) L2/driver support functions.") | Modem PPP instance |
    | --- | --- |

Returns
:   Pointer to network interface modem PPP instance is bound to

## [◆ ](#gaf2177b83100647ed0894cac7fa435cb3)modem\_ppp\_release()

| void modem\_ppp\_release | ( | struct modem\_ppp \* | *ppp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ppp.h](modem_2ppp_8h.md)>`

Release pipe from instance.

Parameters
:   | [PPP L2/driver Support Functions](group__ppp.md "Point-to-point (PPP) L2/driver support functions.") | Modem PPP instance |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
