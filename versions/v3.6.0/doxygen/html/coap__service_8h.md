---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/coap__service_8h.html
original_path: doxygen/html/coap__service_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_service.h File Reference

CoAP Service API.
[More...](#details)

`#include <[zephyr/net/coap.h](coap_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](coap__service_8h_source.md)

| Macros | |
| --- | --- |
| #define | [COAP\_RESOURCE\_DEFINE](group__coap__service.md#gaef40d300170926ad131d06ce62c63d6a)(\_name, \_service, ...) |
|  | Define a static CoAP resource owned by the service named `_service` . |
| #define | [COAP\_SERVICE\_DEFINE](group__coap__service.md#ga8dc5473755efd48548ec4cb6ac2584ec)(\_name, \_host, \_port, \_flags) |
|  | Define a CoAP service with static resources. |
| #define | [COAP\_SERVICE\_COUNT](group__coap__service.md#ga1f0c3bf81baa9da11197a74415d3a9ae)(\_dst) |
|  | Count the number of CoAP services. |
| #define | [COAP\_SERVICE\_RESOURCE\_COUNT](group__coap__service.md#gade9e9a55968a5ad6b3addbb08f2ccb6f)(\_service) |
|  | Count CoAP service static resources. |
| #define | [COAP\_SERVICE\_HAS\_RESOURCE](group__coap__service.md#gaf01cb4d11b18272eb27be93cb1a7197b)(\_service, \_resource) |
|  | Check if service has the specified resource. |
| #define | [COAP\_SERVICE\_FOREACH](group__coap__service.md#gab4d154d5b02235a83c7a2c681b1e22e7)(\_it) |
|  | Iterate over all CoAP services. |
| #define | [COAP\_RESOURCE\_FOREACH](group__coap__service.md#gac3e92107fa12b111771d56987a242b1a)(\_service, \_it) |
|  | Iterate over static CoAP resources associated with a given `_service`. |
| #define | [COAP\_SERVICE\_FOREACH\_RESOURCE](group__coap__service.md#gaaca92287c495f4afb79e584c47316037)(\_service, \_it) |
|  | Iterate over all static resources associated with `_service` . |
| CoAP Service configuration flags | |
|  | |
| #define | [COAP\_SERVICE\_AUTOSTART](group__coap__service.md#gaf5799a7fbf309f8963d22039a6fe2fbb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Start the service on boot. |

| Functions | |
| --- | --- |
| int | [coap\_service\_start](group__coap__service.md#gad1e64f8fe2c6ae32730a9a61f8351bab) (const struct coap\_service \*service) |
|  | Start the provided `service` . |
| int | [coap\_service\_stop](group__coap__service.md#ga58bc31fc4d53ebce9c18ccbc5aab72ce) (const struct coap\_service \*service) |
|  | Stop the provided `service` . |
| int | [coap\_service\_is\_running](group__coap__service.md#ga08638f2001ca2f807489c12ff426784c) (const struct coap\_service \*service) |
|  | Query the provided `service` running state. |
| int | [coap\_service\_send](group__coap__service.md#gad4254ddb71400026211fe8a6da05b2be) (const struct coap\_service \*service, const struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len, const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Send a CoAP message from the provided `service` . |
| int | [coap\_resource\_send](group__coap__service.md#ga67e2cebcfa83f6d11dc335de5dc51a47) (const struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*cpkt, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len, const struct [coap\_transmission\_parameters](structcoap__transmission__parameters.md) \*params) |
|  | Send a CoAP message from the provided `resource` . |
| int | [coap\_resource\_parse\_observe](group__coap__service.md#ga098e08b3bc809499b789b890b67cacd5) (struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*request, const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Parse a CoAP observe request for the provided `resource` . |
| int | [coap\_resource\_remove\_observer\_by\_addr](group__coap__service.md#ga8d9ab0bf6b1ea15408f1c80c45aae16b) (struct [coap\_resource](structcoap__resource.md) \*resource, const struct [sockaddr](structsockaddr.md) \*addr) |
|  | Lookup an observer by address and remove it from the `resource` . |
| int | [coap\_resource\_remove\_observer\_by\_token](group__coap__service.md#gad575a7209a56874002c540eb3f8c0733) (struct [coap\_resource](structcoap__resource.md) \*resource, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*token, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) token\_len) |
|  | Lookup an observer by token and remove it from the `resource` . |

## Detailed Description

CoAP Service API.

An API for applications to respond to CoAP requests

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_service.h](coap__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
