---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__coap__mgmt.html
original_path: doxygen/html/group__coap__mgmt.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CoAP Manager Events

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

CoAP Manager Events.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_event\_coap\_service](structnet__event__coap__service.md) |
|  | CoAP Service event structure. [More...](structnet__event__coap__service.md#details) |
| struct | [net\_event\_coap\_observer](structnet__event__coap__observer.md) |
|  | CoAP Observer event structure. [More...](structnet__event__coap__observer.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_EVENT\_COAP\_SERVICE\_STARTED](#ga3b46cdbe035664256827049e4913643d)   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED) |
|  | coap\_mgmt event raised when a service has started |
| #define | [NET\_EVENT\_COAP\_SERVICE\_STOPPED](#ga9a43c93ef72e152b17992af238507b9d)   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED) |
|  | coap\_mgmt event raised when a service has stopped |
| #define | [NET\_EVENT\_COAP\_OBSERVER\_ADDED](#gaf29083f98f6aa9e7f5192ee7f0504959)   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED) |
|  | coap\_mgmt event raised when an observer has been added to a resource |
| #define | [NET\_EVENT\_COAP\_OBSERVER\_REMOVED](#ga6b56912cf30fa27cc2ccf27805274c69)   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED) |
|  | coap\_mgmt event raised when an observer has been removed from a resource |

## Detailed Description

CoAP Manager Events.

## Macro Definition Documentation

## [◆ ](#gaf29083f98f6aa9e7f5192ee7f0504959)NET\_EVENT\_COAP\_OBSERVER\_ADDED

| #define NET\_EVENT\_COAP\_OBSERVER\_ADDED   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

coap\_mgmt event raised when an observer has been added to a resource

## [◆ ](#ga6b56912cf30fa27cc2ccf27805274c69)NET\_EVENT\_COAP\_OBSERVER\_REMOVED

| #define NET\_EVENT\_COAP\_OBSERVER\_REMOVED   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

coap\_mgmt event raised when an observer has been removed from a resource

## [◆ ](#ga3b46cdbe035664256827049e4913643d)NET\_EVENT\_COAP\_SERVICE\_STARTED

| #define NET\_EVENT\_COAP\_SERVICE\_STARTED   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

coap\_mgmt event raised when a service has started

## [◆ ](#ga9a43c93ef72e152b17992af238507b9d)NET\_EVENT\_COAP\_SERVICE\_STOPPED

| #define NET\_EVENT\_COAP\_SERVICE\_STOPPED   (\_NET\_COAP\_IF\_BASE | NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

coap\_mgmt event raised when a service has stopped

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
