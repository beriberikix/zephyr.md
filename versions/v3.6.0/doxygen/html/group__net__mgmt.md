---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__net__mgmt.html
original_path: doxygen/html/group__net__mgmt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Management

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network Management.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_event\_ipv6\_addr](structnet__event__ipv6__addr.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ADDR\_ADD, NET\_EVENT\_IPV6\_ADDR\_DEL, NET\_EVENT\_IPV6\_MADDR\_ADD and NET\_EVENT\_IPV6\_MADDR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__addr.md#details) |
| struct | [net\_event\_ipv6\_nbr](structnet__event__ipv6__nbr.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_NBR\_ADD and NET\_EVENT\_IPV6\_NBR\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__nbr.md#details) |
| struct | [net\_event\_ipv6\_route](structnet__event__ipv6__route.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_ROUTE\_ADD and NET\_EVENT\_IPV6\_ROUTE\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO enabled and event generator pass the information. [More...](structnet__event__ipv6__route.md#details) |
| struct | [net\_event\_ipv6\_prefix](structnet__event__ipv6__prefix.md) |
|  | Network Management event information structure Used to pass information on network events like NET\_EVENT\_IPV6\_PREFIX\_ADD and NET\_EVENT\_IPV6\_PREFIX\_DEL when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information. [More...](structnet__event__ipv6__prefix.md#details) |
| struct | [net\_event\_l4\_hostname](structnet__event__l4__hostname.md) |
|  | Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED event when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information. [More...](structnet__event__l4__hostname.md#details) |
| struct | [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) |
|  | Network Management event callback structure Used to register a callback into the network management event part, in order to let the owner of this struct to get network event notification based on given event mask. [More...](structnet__mgmt__event__callback.md#details) |

| Macros | |
| --- | --- |
| #define | [net\_mgmt](#ga40e0f9fc86812ad9f6fe174b4c3804e6)(\_mgmt\_request, \_iface, \_data, \_len) |
| #define | [NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](#ga08bde8717fd8e12a338c517b22b87776)(\_mgmt\_request) |
| #define | [NET\_MGMT\_REGISTER\_REQUEST\_HANDLER](#gab67d09d1e65b806ec1957451cbf60501)(\_mgmt\_request, \_func) |
| #define | [NET\_MGMT\_REGISTER\_EVENT\_HANDLER](#ga3a6ca8a72ab12afd4f9b0461253eaa12)(\_name, \_event\_mask, \_func, \_user\_data) |
|  | Define a static network event handler. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [net\_mgmt\_request\_handler\_t](#gae288951a34f7810c291986046ebe4056)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request, struct [net\_if](structnet__if.md) \*iface, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Signature which all Net MGMT request handler need to follow. |
| typedef void(\* | [net\_mgmt\_event\_handler\_t](#gadb876a681fe7f5fb6d2709015625a67f)) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
|  | Define the user's callback handler function signature. |
| typedef void(\* | [net\_mgmt\_event\_static\_handler\_t](#ga14c81781b5bb1e6675e78a249a69357c)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) info\_length, void \*user\_data) |
|  | Define the user's callback handler function signature. |

| Functions | |
| --- | --- |
| static void | [net\_mgmt\_init\_event\_callback](#gaa1d086dcdeb54412073e287129bc50e0) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [net\_mgmt\_event\_handler\_t](#gadb876a681fe7f5fb6d2709015625a67f) handler, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask) |
|  | Helper to initialize a struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") properly. |
| void | [net\_mgmt\_add\_event\_callback](#gae53f5bbc973b0f414107eca75ac0c26f) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb) |
|  | Add a user callback. |
| void | [net\_mgmt\_del\_event\_callback](#ga4960bfb01ecd891da72c57f17587f946) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb) |
|  | Delete a user callback. |
| void | [net\_mgmt\_event\_notify\_with\_info](#ga10882f80c53400b94401a2a08d31697d) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, const void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Used by the system to notify an event. |
| static void | [net\_mgmt\_event\_notify](#ga0648b82762467395b98a3bc13ab451d0) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
| int | [net\_mgmt\_event\_wait](#gacbaa95c65717747d802dc80eb745aa17) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event, struct [net\_if](structnet__if.md) \*\*iface, const void \*\*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*info\_length, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Used to wait synchronously on an event mask. |
| int | [net\_mgmt\_event\_wait\_on\_iface](#ga03c39d5f2af3f2d7a633513fb5ec8a7d) (struct [net\_if](structnet__if.md) \*iface, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event, const void \*\*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*info\_length, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Used to wait synchronously on an event mask for a specific iface. |
| void | [net\_mgmt\_event\_init](#gaab4fe2e9ea0657bf91fb1910af6729cc) (void) |
|  | Used by the core of the network stack to initialize the network event processing. |

## Detailed Description

Network Management.

## Macro Definition Documentation

## [◆ ](#ga40e0f9fc86812ad9f6fe174b4c3804e6)net\_mgmt

| #define net\_mgmt | ( |  | *\_mgmt\_request*, |
| --- | --- | --- | --- |
|  |  |  | *\_iface*, |
|  |  |  | *\_data*, |
|  |  |  | *\_len* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

**Value:**

net\_mgmt\_##\_mgmt\_request(\_mgmt\_request, \_iface, \_data, \_len)

## [◆ ](#ga08bde8717fd8e12a338c517b22b87776)NET\_MGMT\_DEFINE\_REQUEST\_HANDLER

| #define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER | ( |  | *\_mgmt\_request* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

**Value:**

extern int net\_mgmt\_##\_mgmt\_request([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request, \

struct [net\_if](structnet__if.md) \*iface, \

void \*data, size\_t len)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

## [◆ ](#ga3a6ca8a72ab12afd4f9b0461253eaa12)NET\_MGMT\_REGISTER\_EVENT\_HANDLER

| #define NET\_MGMT\_REGISTER\_EVENT\_HANDLER | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_event\_mask*, |
|  |  |  | *\_func*, |
|  |  |  | *\_user\_data* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

**Value:**

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(net\_mgmt\_event\_static\_handler, \_name) = { \

.event\_mask = \_event\_mask, \

.handler = \_func, \

.user\_data = (void \*)\_user\_data, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Define a static network event handler.

Parameters
:   | \_name | Name of the event handler. |
    | --- | --- |
    | \_event\_mask | A mask of network events on which the passed handler should be called in case those events come. Note that only the command part is treated as a mask, matching one to several commands. Layer and layer code will be made of an exact match. This means that in order to receive events from multiple layers, one must have multiple listeners registered, one for each layer being listened. |
    | \_func | The function to be called upon network events being emitted. |
    | \_user\_data | User data passed to the handler being called on network events. |

## [◆ ](#gab67d09d1e65b806ec1957451cbf60501)NET\_MGMT\_REGISTER\_REQUEST\_HANDLER

| #define NET\_MGMT\_REGISTER\_REQUEST\_HANDLER | ( |  | *\_mgmt\_request*, |
| --- | --- | --- | --- |
|  |  |  | *\_func* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

**Value:**

FUNC\_ALIAS(\_func, net\_mgmt\_##\_mgmt\_request, int)

## Typedef Documentation

## [◆ ](#gadb876a681fe7f5fb6d2709015625a67f)net\_mgmt\_event\_handler\_t

| typedef void(\* net\_mgmt\_event\_handler\_t) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
| --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Define the user's callback handler function signature.

Parameters
:   | cb | Original struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") owning this handler. |
    | --- | --- |
    | mgmt\_event | The network event being notified. |
    | iface | A pointer on a struct [net\_if](structnet__if.md "Network Interface structure.") to which the event belongs to, if it's an event on an iface. NULL otherwise. |

## [◆ ](#ga14c81781b5bb1e6675e78a249a69357c)net\_mgmt\_event\_static\_handler\_t

| typedef void(\* net\_mgmt\_event\_static\_handler\_t) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) info\_length, void \*user\_data) |
| --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Define the user's callback handler function signature.

Parameters
:   | mgmt\_event | The network event being notified. |
    | --- | --- |
    | iface | A pointer on a struct [net\_if](structnet__if.md "Network Interface structure.") to which the event belongs to, if it's an event on an iface. NULL otherwise. |
    | info | A valid pointer on a data understood by the handler. NULL otherwise. |
    | info\_length | Length in bytes of the memory pointed by `info`. |
    | user\_data | Data provided by the user to the handler. |

## [◆ ](#gae288951a34f7810c291986046ebe4056)net\_mgmt\_request\_handler\_t

| typedef int(\* net\_mgmt\_request\_handler\_t) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request, struct [net\_if](structnet__if.md) \*iface, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Signature which all Net MGMT request handler need to follow.

Parameters
:   | mgmt\_request | The exact request value the handler is being called through |
    | --- | --- |
    | iface | A valid pointer on struct [net\_if](structnet__if.md "Network Interface structure.") if the request is meant to be tight to a network interface. NULL otherwise. |
    | data | A valid pointer on a data understood by the handler. NULL otherwise. |
    | len | Length in byte of the memory pointed by data. |

## Function Documentation

## [◆ ](#gae53f5bbc973b0f414107eca75ac0c26f)net\_mgmt\_add\_event\_callback()

| void net\_mgmt\_add\_event\_callback | ( | struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Add a user callback.

Parameters
:   | cb | A valid pointer on user's callback to add. |
    | --- | --- |

## [◆ ](#ga4960bfb01ecd891da72c57f17587f946)net\_mgmt\_del\_event\_callback()

| void net\_mgmt\_del\_event\_callback | ( | struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Delete a user callback.

Parameters
:   | cb | A valid pointer on user's callback to delete. |
    | --- | --- |

## [◆ ](#gaab4fe2e9ea0657bf91fb1910af6729cc)net\_mgmt\_event\_init()

| void net\_mgmt\_event\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used by the core of the network stack to initialize the network event processing.

## [◆ ](#ga0648b82762467395b98a3bc13ab451d0)net\_mgmt\_event\_notify()

| | void net\_mgmt\_event\_notify | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \* | *iface* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

## [◆ ](#ga10882f80c53400b94401a2a08d31697d)net\_mgmt\_event\_notify\_with\_info()

| void net\_mgmt\_event\_notify\_with\_info | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface*, |
|  |  | const void \* | *info*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used by the system to notify an event.

Parameters
:   | mgmt\_event | The actual network event code to notify |
    | --- | --- |
    | iface | a valid pointer on a struct [net\_if](structnet__if.md "Network Interface structure.") if only the event is based on an iface. NULL otherwise. |
    | info | a valid pointer on the information you want to pass along with the event. NULL otherwise. Note the data pointed there is normalized by the related event. |
    | length | size of the data pointed by info pointer. |

Note: info and length are disabled if CONFIG\_NET\_MGMT\_EVENT\_INFO is not defined.

## [◆ ](#gacbaa95c65717747d802dc80eb745aa17)net\_mgmt\_event\_wait()

| int net\_mgmt\_event\_wait | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event\_mask*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *raised\_event*, |
|  |  | struct [net\_if](structnet__if.md) \*\* | *iface*, |
|  |  | const void \*\* | *info*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *info\_length*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used to wait synchronously on an event mask.

Parameters
:   | mgmt\_event\_mask | A mask of relevant events to wait on. |
    | --- | --- |
    | raised\_event | a pointer on a [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) to get which event from the mask generated the event. Can be NULL if the caller is not interested in that information. |
    | iface | a pointer on a place holder for the iface on which the event has originated from. This is valid if only the event mask has bit NET\_MGMT\_IFACE\_BIT set relevantly, depending on events the caller wants to listen to. |
    | info | a valid pointer if user wants to get the information the event might bring along. NULL otherwise. |
    | info\_length | tells how long the info memory area is. Only valid if the info is not NULL. |
    | timeout | A timeout delay. K\_FOREVER can be used to wait indefinitely. |

Returns
:   0 on success, a negative error code otherwise. -ETIMEDOUT will be specifically returned if the timeout kick-in instead of an actual event.

## [◆ ](#ga03c39d5f2af3f2d7a633513fb5ec8a7d)net\_mgmt\_event\_wait\_on\_iface()

| int net\_mgmt\_event\_wait\_on\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event\_mask*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *raised\_event*, |
|  |  | const void \*\* | *info*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *info\_length*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Used to wait synchronously on an event mask for a specific iface.

Parameters
:   | iface | a pointer on a valid network interface to listen event to |
    | --- | --- |
    | mgmt\_event\_mask | A mask of relevant events to wait on. Listened to events should be relevant to iface events and thus have the bit NET\_MGMT\_IFACE\_BIT set. |
    | raised\_event | a pointer on a [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) to get which event from the mask generated the event. Can be NULL if the caller is not interested in that information. |
    | info | a valid pointer if user wants to get the information the event might bring along. NULL otherwise. |
    | info\_length | tells how long the info memory area is. Only valid if the info is not NULL. |
    | timeout | A timeout delay. K\_FOREVER can be used to wait indefinitely. |

Returns
:   0 on success, a negative error code otherwise. -ETIMEDOUT will be specifically returned if the timeout kick-in instead of an actual event.

## [◆ ](#gaa1d086dcdeb54412073e287129bc50e0)net\_mgmt\_init\_event\_callback()

| | void net\_mgmt\_init\_event\_callback | ( | struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \* | *cb*, | | --- | --- | --- | --- | |  |  | [net\_mgmt\_event\_handler\_t](#gadb876a681fe7f5fb6d2709015625a67f) | *handler*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *mgmt\_event\_mask* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_mgmt.h](net__mgmt_8h.md)>`

Helper to initialize a struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") properly.

Parameters
:   | cb | A valid application's callback structure pointer. |
    | --- | --- |
    | handler | A valid handler function pointer. |
    | mgmt\_event\_mask | A mask of relevant events for the handler |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
