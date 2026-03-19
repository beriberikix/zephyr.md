---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__cp__le__ext__create__conn__v2.html
original_path: doxygen/html/structbt__hci__cp__le__ext__create__conn__v2.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_cp\_le\_ext\_create\_conn\_v2 Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_handle](#addf1f80c4d3625e0c6d6e716f6e2e207) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent](#a536da199958b3b54469f5b4b029e1bac) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [filter\_policy](#a66632dbac1605cff69e8da566e800347) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [own\_addr\_type](#a05fd0089a0fd43f98042835231407a60) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [peer\_addr](#a25466a04d224bdf495266b0064c424dd) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phys](#ae2d3e3079a2848907224bb7ff0efc64b) |
| struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) | [p](#a8d606c5aa480f54c8da9f42a35ad513e) [0] |

## Field Documentation

## [◆ ](#addf1f80c4d3625e0c6d6e716f6e2e207)adv\_handle

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_ext\_create\_conn\_v2::adv\_handle |
| --- |

## [◆ ](#a66632dbac1605cff69e8da566e800347)filter\_policy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_ext\_create\_conn\_v2::filter\_policy |
| --- |

## [◆ ](#a05fd0089a0fd43f98042835231407a60)own\_addr\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_ext\_create\_conn\_v2::own\_addr\_type |
| --- |

## [◆ ](#a8d606c5aa480f54c8da9f42a35ad513e)p

| struct [bt\_hci\_ext\_conn\_phy](structbt__hci__ext__conn__phy.md) bt\_hci\_cp\_le\_ext\_create\_conn\_v2::p[0] |
| --- |

## [◆ ](#a25466a04d224bdf495266b0064c424dd)peer\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_cp\_le\_ext\_create\_conn\_v2::peer\_addr |
| --- |

## [◆ ](#ae2d3e3079a2848907224bb7ff0efc64b)phys

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_ext\_create\_conn\_v2::phys |
| --- |

## [◆ ](#a536da199958b3b54469f5b4b029e1bac)subevent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_ext\_create\_conn\_v2::subevent |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_cp\_le\_ext\_create\_conn\_v2](structbt__hci__cp__le__ext__create__conn__v2.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
