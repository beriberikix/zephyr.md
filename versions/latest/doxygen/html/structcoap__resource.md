---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structcoap__resource.html
original_path: doxygen/html/structcoap__resource.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coap\_resource Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [COAP Library](group__coap.md)

Description of CoAP resource.
[More...](#details)

`#include <[coap.h](coap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) | [get](#aebe880e3ccbd2441854dfa899dc72c13) |
|  | Which function to be called for each CoAP method. |
| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) | [post](#a1efed8197d44aba3b63aaa9d9bb0f5bb) |
| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) | [put](#a3152a778e27e36fad7dd62985621d58b) |
| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) | [del](#a77dfb6d59c25e6e58141226023bf59ea) |
| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) | [fetch](#a6975e84ebc67d6aff2efb755695518f5) |
| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) | [patch](#aa0a5465fc5b49a566e3803a9f1638724) |
| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) | [ipatch](#a7657cb2e9bbac7f98e35b4ed33f13163) |
| [coap\_notify\_t](group__coap.md#ga4180b2476430fbe4a5e0418fb628ea91) | [notify](#a3199679fd990d757e9a500fbd7c653d7) |
| const char \*const \* | [path](#ada7a41309b6ca11612b17fabf6cd56c5) |
| void \* | [user\_data](#a202a83a5aa024a62bd25cc40f42e8d65) |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [observers](#a5035dc9c88c2b0ae557608e34ec14433) |
| int | [age](#ae8e1b2b1920689913e0910a82a30e009) |

## Detailed Description

Description of CoAP resource.

CoAP servers often want to register resources, so that clients can act on them, by fetching their state or requesting updates to them.

## Field Documentation

## [◆ ](#ae8e1b2b1920689913e0910a82a30e009)age

| int coap\_resource::age |
| --- |

## [◆ ](#a77dfb6d59c25e6e58141226023bf59ea)del

| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) coap\_resource::del |
| --- |

## [◆ ](#a6975e84ebc67d6aff2efb755695518f5)fetch

| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) coap\_resource::fetch |
| --- |

## [◆ ](#aebe880e3ccbd2441854dfa899dc72c13)get

| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) coap\_resource::get |
| --- |

Which function to be called for each CoAP method.

## [◆ ](#a7657cb2e9bbac7f98e35b4ed33f13163)ipatch

| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) coap\_resource::ipatch |
| --- |

## [◆ ](#a3199679fd990d757e9a500fbd7c653d7)notify

| [coap\_notify\_t](group__coap.md#ga4180b2476430fbe4a5e0418fb628ea91) coap\_resource::notify |
| --- |

## [◆ ](#a5035dc9c88c2b0ae557608e34ec14433)observers

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) coap\_resource::observers |
| --- |

## [◆ ](#aa0a5465fc5b49a566e3803a9f1638724)patch

| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) coap\_resource::patch |
| --- |

## [◆ ](#ada7a41309b6ca11612b17fabf6cd56c5)path

| const char\* const\* coap\_resource::path |
| --- |

## [◆ ](#a1efed8197d44aba3b63aaa9d9bb0f5bb)post

| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) coap\_resource::post |
| --- |

## [◆ ](#a3152a778e27e36fad7dd62985621d58b)put

| [coap\_method\_t](group__coap.md#gaa509d49f06101342908a71f2f18f18fc) coap\_resource::put |
| --- |

## [◆ ](#a202a83a5aa024a62bd25cc40f42e8d65)user\_data

| void\* coap\_resource::user\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[coap.h](coap_8h_source.md)

- [coap\_resource](structcoap__resource.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
