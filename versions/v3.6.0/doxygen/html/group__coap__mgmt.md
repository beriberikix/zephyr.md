---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__coap__mgmt.html
original_path: doxygen/html/group__coap__mgmt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| #define | [NET\_EVENT\_COAP\_SERVICE\_STARTED](#ga3b46cdbe035664256827049e4913643d)   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a0e327a65115ed76487deb74c2aa48ea3)) |
|  | coap\_mgmt event raised when a service has started |
| #define | [NET\_EVENT\_COAP\_SERVICE\_STOPPED](#ga9a43c93ef72e152b17992af238507b9d)   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a5f5dc678a520757663454024d1b1e507)) |
|  | coap\_mgmt event raised when a service has stopped |
| #define | [NET\_EVENT\_COAP\_OBSERVER\_ADDED](#gaf29083f98f6aa9e7f5192ee7f0504959)   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a29f26377c082d20efc75ab07f9a0433b)) |
|  | coap\_mgmt event raised when an observer has been added to a resource |
| #define | [NET\_EVENT\_COAP\_OBSERVER\_REMOVED](#ga6b56912cf30fa27cc2ccf27805274c69)   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a27cad6e90f4133d6a651d26dcf0332a5)) |
|  | coap\_mgmt event raised when an observer has been removed from a resource |

| Enumerations | |
| --- | --- |
| enum | [net\_event\_coap\_cmd](#ga126f9bc23ae3d6a94ff34fcaceba47f5) { [NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a0e327a65115ed76487deb74c2aa48ea3) = 1 , [NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a5f5dc678a520757663454024d1b1e507) , [NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a29f26377c082d20efc75ab07f9a0433b) , [NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a27cad6e90f4133d6a651d26dcf0332a5) } |

## Detailed Description

CoAP Manager Events.

## Macro Definition Documentation

## [◆ ](#gaf29083f98f6aa9e7f5192ee7f0504959)NET\_EVENT\_COAP\_OBSERVER\_ADDED

| #define NET\_EVENT\_COAP\_OBSERVER\_ADDED   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a29f26377c082d20efc75ab07f9a0433b)) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

coap\_mgmt event raised when an observer has been added to a resource

## [◆ ](#ga6b56912cf30fa27cc2ccf27805274c69)NET\_EVENT\_COAP\_OBSERVER\_REMOVED

| #define NET\_EVENT\_COAP\_OBSERVER\_REMOVED   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a27cad6e90f4133d6a651d26dcf0332a5)) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

coap\_mgmt event raised when an observer has been removed from a resource

## [◆ ](#ga3b46cdbe035664256827049e4913643d)NET\_EVENT\_COAP\_SERVICE\_STARTED

| #define NET\_EVENT\_COAP\_SERVICE\_STARTED   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a0e327a65115ed76487deb74c2aa48ea3)) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

coap\_mgmt event raised when a service has started

## [◆ ](#ga9a43c93ef72e152b17992af238507b9d)NET\_EVENT\_COAP\_SERVICE\_STOPPED

| #define NET\_EVENT\_COAP\_SERVICE\_STOPPED   (\_NET\_COAP\_IF\_BASE | [NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED](#gga126f9bc23ae3d6a94ff34fcaceba47f5a5f5dc678a520757663454024d1b1e507)) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

coap\_mgmt event raised when a service has stopped

## Enumeration Type Documentation

## [◆ ](#ga126f9bc23ae3d6a94ff34fcaceba47f5)net\_event\_coap\_cmd

| enum [net\_event\_coap\_cmd](#ga126f9bc23ae3d6a94ff34fcaceba47f5) |
| --- |

`#include <[coap_mgmt.h](coap__mgmt_8h.md)>`

| Enumerator | |
| --- | --- |
| NET\_EVENT\_COAP\_CMD\_SERVICE\_STARTED |  |
| NET\_EVENT\_COAP\_CMD\_SERVICE\_STOPPED |  |
| NET\_EVENT\_COAP\_CMD\_OBSERVER\_ADDED |  |
| NET\_EVENT\_COAP\_CMD\_OBSERVER\_REMOVED |  |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
