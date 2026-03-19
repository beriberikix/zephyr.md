---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__event__coap__observer.html
original_path: doxygen/html/structnet__event__coap__observer.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_coap\_observer Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [CoAP Manager Events](group__coap__mgmt.md)

CoAP Observer event structure.
[More...](#details)

`#include <[coap_mgmt.h](coap__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [coap\_resource](structcoap__resource.md) \* | [resource](#a4522acf85fff0a65def80f3a7d794d2b) |
|  | The CoAP resource for which the event is emitted. |
| struct [coap\_observer](structcoap__observer.md) \* | [observer](#af15a9f085271fdc5e88180980013bfd2) |
|  | The observer that is added/removed. |

## Detailed Description

CoAP Observer event structure.

## Field Documentation

## [◆ ](#af15a9f085271fdc5e88180980013bfd2)observer

| struct [coap\_observer](structcoap__observer.md)\* net\_event\_coap\_observer::observer |
| --- |

The observer that is added/removed.

## [◆ ](#a4522acf85fff0a65def80f3a7d794d2b)resource

| struct [coap\_resource](structcoap__resource.md)\* net\_event\_coap\_observer::resource |
| --- |

The CoAP resource for which the event is emitted.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap\_mgmt.h](coap__mgmt_8h_source.md)

- [net\_event\_coap\_observer](structnet__event__coap__observer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
