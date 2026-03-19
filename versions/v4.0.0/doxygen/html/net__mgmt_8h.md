---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__mgmt_8h.html
original_path: doxygen/html/net__mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_mgmt.h File Reference

Network Management API public header.
[More...](#details)

`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`  
`#include <[zephyr/net/net_event.h](net__event_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](net__mgmt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) |
|  | Network Management event callback structure Used to register a callback into the network management event part, in order to let the owner of this struct to get network event notification based on given event mask. [More...](structnet__mgmt__event__callback.md#details) |

| Macros | |
| --- | --- |
| #define | [net\_mgmt](group__net__mgmt.md#ga40e0f9fc86812ad9f6fe174b4c3804e6)(\_mgmt\_request, \_iface, \_data, \_len) |
|  | Generate a network management event. |
| #define | [NET\_MGMT\_DEFINE\_REQUEST\_HANDLER](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)(\_mgmt\_request) |
|  | Declare a request handler function for the given network event. |
| #define | [NET\_MGMT\_REGISTER\_REQUEST\_HANDLER](group__net__mgmt.md#gab67d09d1e65b806ec1957451cbf60501)(\_mgmt\_request, \_func) |
|  | Create a request handler function for the given network event. |
| #define | [NET\_MGMT\_REGISTER\_EVENT\_HANDLER](group__net__mgmt.md#ga3a6ca8a72ab12afd4f9b0461253eaa12)(\_name, \_event\_mask, \_func, \_user\_data) |
|  | Define a static network event handler. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [net\_mgmt\_request\_handler\_t](group__net__mgmt.md#gae288951a34f7810c291986046ebe4056)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_request, struct [net\_if](structnet__if.md) \*iface, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Signature which all Net MGMT request handler need to follow. |
| typedef void(\* | [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f)) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
|  | Define the user's callback handler function signature. |
| typedef void(\* | [net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#ga14c81781b5bb1e6675e78a249a69357c)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) info\_length, void \*user\_data) |
|  | Define the user's callback handler function signature. |

| Functions | |
| --- | --- |
| static void | [net\_mgmt\_init\_event\_callback](group__net__mgmt.md#gaa1d086dcdeb54412073e287129bc50e0) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#gadb876a681fe7f5fb6d2709015625a67f) handler, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask) |
|  | Helper to initialize a struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") properly. |
| void | [net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb) |
|  | Add a user callback. |
| void | [net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb) |
|  | Delete a user callback. |
| void | [net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga10882f80c53400b94401a2a08d31697d) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, const void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Used by the system to notify an event. |
| static void | [net\_mgmt\_event\_notify](group__net__mgmt.md#ga0648b82762467395b98a3bc13ab451d0) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
|  | Used by the system to notify an event without any additional information. |
| int | [net\_mgmt\_event\_wait](group__net__mgmt.md#gacbaa95c65717747d802dc80eb745aa17) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event, struct [net\_if](structnet__if.md) \*\*iface, const void \*\*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*info\_length, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Used to wait synchronously on an event mask. |
| int | [net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga03c39d5f2af3f2d7a633513fb5ec8a7d) (struct [net\_if](structnet__if.md) \*iface, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mgmt\_event\_mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*raised\_event, const void \*\*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*info\_length, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Used to wait synchronously on an event mask for a specific iface. |
| void | [net\_mgmt\_event\_init](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc) (void) |
|  | Used by the core of the network stack to initialize the network event processing. |

## Detailed Description

Network Management API public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_mgmt.h](net__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
