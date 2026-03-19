---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/coap__mgmt_8h.html
original_path: doxygen/html/coap__mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_mgmt.h File Reference

CoAP Events code public header.
[More...](#details)

`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`

[Go to the source code of this file.](coap__mgmt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_event\_coap\_service](structnet__event__coap__service.md) |
|  | CoAP Service event structure. [More...](structnet__event__coap__service.md#details) |
| struct | [net\_event\_coap\_observer](structnet__event__coap__observer.md) |
|  | CoAP Observer event structure. [More...](structnet__event__coap__observer.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_EVENT\_COAP\_SERVICE\_STARTED](group__coap__mgmt.md#ga3b46cdbe035664256827049e4913643d)   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED) |
|  | coap\_mgmt event raised when a service has started |
| #define | [NET\_EVENT\_COAP\_SERVICE\_STOPPED](group__coap__mgmt.md#ga9a43c93ef72e152b17992af238507b9d)   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED) |
|  | coap\_mgmt event raised when a service has stopped |
| #define | [NET\_EVENT\_COAP\_OBSERVER\_ADDED](group__coap__mgmt.md#gaf29083f98f6aa9e7f5192ee7f0504959)   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED) |
|  | coap\_mgmt event raised when an observer has been added to a resource |
| #define | [NET\_EVENT\_COAP\_OBSERVER\_REMOVED](group__coap__mgmt.md#ga6b56912cf30fa27cc2ccf27805274c69)   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED) |
|  | coap\_mgmt event raised when an observer has been removed from a resource |

## Detailed Description

CoAP Events code public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_mgmt.h](coap__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
