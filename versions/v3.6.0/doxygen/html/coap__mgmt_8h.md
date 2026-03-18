---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/coap__mgmt_8h.html
original_path: doxygen/html/coap__mgmt_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| #define | [NET\_EVENT\_COAP\_SERVICE\_STARTED](group__coap__mgmt.md#ga3b46cdbe035664256827049e4913643d)   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED](group__coap__mgmt.md#gga126f9bc23ae3d6a94ff34fcaceba47f5a0e327a65115ed76487deb74c2aa48ea3)) |
|  | coap\_mgmt event raised when a service has started |
| #define | [NET\_EVENT\_COAP\_SERVICE\_STOPPED](group__coap__mgmt.md#ga9a43c93ef72e152b17992af238507b9d)   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED](group__coap__mgmt.md#gga126f9bc23ae3d6a94ff34fcaceba47f5a5f5dc678a520757663454024d1b1e507)) |
|  | coap\_mgmt event raised when a service has stopped |
| #define | [NET\_EVENT\_COAP\_OBSERVER\_ADDED](group__coap__mgmt.md#gaf29083f98f6aa9e7f5192ee7f0504959)   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED](group__coap__mgmt.md#gga126f9bc23ae3d6a94ff34fcaceba47f5a29f26377c082d20efc75ab07f9a0433b)) |
|  | coap\_mgmt event raised when an observer has been added to a resource |
| #define | [NET\_EVENT\_COAP\_OBSERVER\_REMOVED](group__coap__mgmt.md#ga6b56912cf30fa27cc2ccf27805274c69)   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED](group__coap__mgmt.md#gga126f9bc23ae3d6a94ff34fcaceba47f5a27cad6e90f4133d6a651d26dcf0332a5)) |
|  | coap\_mgmt event raised when an observer has been removed from a resource |

| Enumerations | |
| --- | --- |
| enum | [net\_event\_coap\_cmd](group__coap__mgmt.md#ga126f9bc23ae3d6a94ff34fcaceba47f5) { [NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED](group__coap__mgmt.md#gga126f9bc23ae3d6a94ff34fcaceba47f5a0e327a65115ed76487deb74c2aa48ea3) = 1 , [NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED](group__coap__mgmt.md#gga126f9bc23ae3d6a94ff34fcaceba47f5a5f5dc678a520757663454024d1b1e507) , [NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED](group__coap__mgmt.md#gga126f9bc23ae3d6a94ff34fcaceba47f5a29f26377c082d20efc75ab07f9a0433b) , [NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED](group__coap__mgmt.md#gga126f9bc23ae3d6a94ff34fcaceba47f5a27cad6e90f4133d6a651d26dcf0332a5) } |

## Detailed Description

CoAP Events code public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [coap\_mgmt.h](coap__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
