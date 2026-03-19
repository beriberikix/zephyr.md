---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structcoap__core__metadata.html
original_path: doxygen/html/structcoap__core__metadata.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_core\_metadata Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resource, the 'user\_data' field should point to a valid [coap\_core\_metadata](structcoap__core__metadata.md "In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resou...") structure.
[More...](#details)

`#include <[coap_link_format.h](coap__link__format_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \*const \* | [attributes](#aeb04ef8b47ecc144dd036007cccd2e59) |
|  | List of attributes to add. |
| void \* | [user\_data](#a74e8a533d7f8596498d5d0ce2afc102f) |
|  | User specific data. |

## Detailed Description

In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resource, the 'user\_data' field should point to a valid [coap\_core\_metadata](structcoap__core__metadata.md "In case you want to add attributes to the resources included in the 'well-known/core' "virtual" resou...") structure.

## Field Documentation

## [◆ ](#aeb04ef8b47ecc144dd036007cccd2e59)attributes

| const char\* const\* coap\_core\_metadata::attributes |
| --- |

List of attributes to add.

## [◆ ](#a74e8a533d7f8596498d5d0ce2afc102f)user\_data

| void\* coap\_core\_metadata::user\_data |
| --- |

User specific data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap\_link\_format.h](coap__link__format_8h_source.md)

- [coap\_core\_metadata](structcoap__core__metadata.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
