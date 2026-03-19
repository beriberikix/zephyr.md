---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__le__per__adv__response__report.html
original_path: doxygen/html/structbt__hci__evt__le__per__adv__response__report.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_per\_adv\_response\_report Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_handle](#a9d746015a9c2b48c54008319c892b063) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent](#ad4f8f61150f82f4ba420e3c0a1f333c2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_status](#a46a5b74321a80697fd700a276be18ed3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_responses](#a37f3519eefe33e87d49c7c2ad0f8b40c) |
| struct [bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md) | [responses](#a3b1bcca7a7dbc6fcf5709f6152268b87) [0] |

## Field Documentation

## [◆ ](#a9d746015a9c2b48c54008319c892b063)adv\_handle

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_per\_adv\_response\_report::adv\_handle |
| --- |

## [◆ ](#a37f3519eefe33e87d49c7c2ad0f8b40c)num\_responses

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_per\_adv\_response\_report::num\_responses |
| --- |

## [◆ ](#a3b1bcca7a7dbc6fcf5709f6152268b87)responses

| struct [bt\_hci\_evt\_le\_per\_adv\_response](structbt__hci__evt__le__per__adv__response.md) bt\_hci\_evt\_le\_per\_adv\_response\_report::responses[0] |
| --- |

## [◆ ](#ad4f8f61150f82f4ba420e3c0a1f333c2)subevent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_per\_adv\_response\_report::subevent |
| --- |

## [◆ ](#a46a5b74321a80697fd700a276be18ed3)tx\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_per\_adv\_response\_report::tx\_status |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_per\_adv\_response\_report](structbt__hci__evt__le__per__adv__response__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
