---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/coap__link__format_8h.html
original_path: doxygen/html/coap__link__format_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_link\_format.h File Reference

CoAP implementation for Zephyr.
[More...](#details)

[Go to the source code of this file.](coap__link__format_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [coap\_core\_metadata](structcoap__core__metadata.md) |
|  | In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resource, the 'user\_data' field should point to a valid [coap\_core\_metadata](structcoap__core__metadata.md "In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resou...") structure. [More...](structcoap__core__metadata.md#details) |

| Macros | |
| --- | --- |
| #define | [COAP\_WELL\_KNOWN\_CORE\_PATH](group__coap.md#ga09d2c727fc6fc76aa9d908b759a3f40b)   ((const char \* const[]) { ".well-known", "core", NULL }) |
|  | This resource should be added before all other resources that should be included in the responses of the .well-known/core resource if is to be used with coap\_well\_known\_core\_get. |

| Functions | |
| --- | --- |
| int | [coap\_well\_known\_core\_get](group__coap.md#ga3f2eded87dbeb7408ff6f07e04afb30b) (struct [coap\_resource](structcoap__resource.md) \*resource, const struct [coap\_packet](structcoap__packet.md) \*request, struct [coap\_packet](structcoap__packet.md) \*response, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Build a CoAP response for a .well-known/core CoAP request. |
| int | [coap\_well\_known\_core\_get\_len](group__coap.md#ga49d63f12b593d7509690a504b05da730) (struct [coap\_resource](structcoap__resource.md) \*resources, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) resources\_len, const struct [coap\_packet](structcoap__packet.md) \*request, struct [coap\_packet](structcoap__packet.md) \*response, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len) |
|  | Build a CoAP response for a .well-known/core CoAP request. |

## Detailed Description

CoAP implementation for Zephyr.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_link\_format.h](coap__link__format_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
