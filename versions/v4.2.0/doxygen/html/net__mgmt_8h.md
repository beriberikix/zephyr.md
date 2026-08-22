---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net__mgmt_8h.html
original_path: doxygen/html/net__mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_mgmt.h File Reference

Network Management API public header.
[More...](#details)

`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/net_event.h](net__event_8h_source.md)>`

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
| typedef int(\* | [net\_mgmt\_request\_handler\_t](group__net__mgmt.md#ga78b9302193bd0c5cc35d81d298a5eb6b)) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_request, struct [net\_if](structnet__if.md) \*iface, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Signature which all Net MGMT request handler need to follow. |
| typedef void(\* | [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2)) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
|  | Define the user's callback handler function signature. |
| typedef void(\* | [net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#gaf3773f8e945c4ec05b2fab46cd8b1881)) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) info\_length, void \*user\_data) |
|  | Define the user's callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [net\_mgmt\_layer\_code](group__net__mgmt.md#ga5e6911455b9ab9f4c82780001459461a) {     [NET\_MGMT\_LAYER\_CODE\_UNKNOWN](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd) = 0x00 , [NET\_MGMT\_LAYER\_CODE\_IFACE](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518) = 0x01 , [NET\_MGMT\_LAYER\_CODE\_CONN](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7) = 0x02 , [NET\_MGMT\_LAYER\_CODE\_IPV4](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2) = 0x03 ,     [NET\_MGMT\_LAYER\_CODE\_IPV6](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8) = 0x04 , [NET\_MGMT\_LAYER\_CODE\_L4](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e) = 0x05 , [NET\_MGMT\_LAYER\_CODE\_COAP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7) = 0x06 , [NET\_MGMT\_LAYER\_CODE\_STATS](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6) = 0x07 ,     [NET\_MGMT\_LAYER\_CODE\_HOSTAP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc) = 0x08 , [NET\_MGMT\_LAYER\_CODE\_ETHERNET](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4) = 0x09 , [NET\_MGMT\_LAYER\_CODE\_IEEE802514](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b) = 0x0A , [NET\_MGMT\_LAYER\_CODE\_PPP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1) = 0x0B ,     [NET\_MGMT\_LAYER\_CODE\_VIRTUAL](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca) = 0x0C , [NET\_MGMT\_LAYER\_CODE\_WIFI](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789) = 0x0D , [NET\_MGMT\_LAYER\_CODE\_USER3](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977) = 0x7C , [NET\_MGMT\_LAYER\_CODE\_USER2](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4) = 0x7D ,     [NET\_MGMT\_LAYER\_CODE\_USER1](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a) = 0x7E , [NET\_MGMT\_LAYER\_CODE\_RESERVED](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75) = 0x7F   } |
|  | Central place the definition of the layer codes (7 bit value). [More...](group__net__mgmt.md#ga5e6911455b9ab9f4c82780001459461a) |

| Functions | |
| --- | --- |
| static void | [net\_mgmt\_init\_event\_callback](group__net__mgmt.md#ga4e42b6d16b863ca374d032682e8c11fb) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb, [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2) handler, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event\_mask) |
|  | Helper to initialize a struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md "Network Management event callback structure Used to register a callback into the network management e...") properly. |
| void | [net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb) |
|  | Add a user callback. |
| void | [net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946) (struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb) |
|  | Delete a user callback. |
| void | [net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga6415ec1e2e7f477c8976022ac33b0654) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event, struct [net\_if](structnet__if.md) \*iface, const void \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Used by the system to notify an event. |
| static void | [net\_mgmt\_event\_notify](group__net__mgmt.md#gabf710692e596a2d98f37b82da884a82a) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event, struct [net\_if](structnet__if.md) \*iface) |
|  | Used by the system to notify an event without any additional information. |
| int | [net\_mgmt\_event\_wait](group__net__mgmt.md#ga7137c77c55ee2609941c88db79e22d1a) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event\_mask, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*raised\_event, struct [net\_if](structnet__if.md) \*\*iface, const void \*\*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*info\_length, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Used to wait synchronously on an event mask. |
| int | [net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga3ab114106df41144c0fae8e6faad12cb) (struct [net\_if](structnet__if.md) \*iface, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event\_mask, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*raised\_event, const void \*\*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*info\_length, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Used to wait synchronously on an event mask for a specific iface. |
| void | [net\_mgmt\_event\_init](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc) (void) |
|  | Used by the core of the network stack to initialize the network event processing. |

## Detailed Description

Network Management API public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_mgmt.h](net__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
