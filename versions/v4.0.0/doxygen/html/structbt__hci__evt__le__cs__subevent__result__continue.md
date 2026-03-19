---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__evt__le__cs__subevent__result__continue.html
original_path: doxygen/html/structbt__hci__evt__le__cs__subevent__result__continue.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_cs\_subevent\_result\_continue Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_handle](#a4126bebec093f6f4d1a22b43abec6b1c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [config\_id](#adefb9ad1f998460a6d235ebd39bbfe4a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [procedure\_done\_status](#a3e5b1e8a247fff36c06447c9ff7c3bb8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent\_done\_status](#a49cf181c8518fb3015a0c54f7558aa8c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent\_abort\_reason](#a1801aeaac839831198e17b7d96a5532a): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [procedure\_abort\_reason](#a3c7ac056a5898710ffbc0776ef551b4b): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_antenna\_paths](#a2f8e1f634e28100815c881a463b51f2c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_steps\_reported](#af127774b52c4e088f628999136b6cd7c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [steps](#abbddd0e27178e49abe6eef62bc094a16) [] |

## Field Documentation

## [◆ ](#adefb9ad1f998460a6d235ebd39bbfe4a)config\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::config\_id |
| --- |

## [◆ ](#a4126bebec093f6f4d1a22b43abec6b1c)conn\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::conn\_handle |
| --- |

## [◆ ](#a2f8e1f634e28100815c881a463b51f2c)num\_antenna\_paths

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::num\_antenna\_paths |
| --- |

## [◆ ](#af127774b52c4e088f628999136b6cd7c)num\_steps\_reported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::num\_steps\_reported |
| --- |

## [◆ ](#a3c7ac056a5898710ffbc0776ef551b4b)procedure\_abort\_reason

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::procedure\_abort\_reason |
| --- |

## [◆ ](#a3e5b1e8a247fff36c06447c9ff7c3bb8)procedure\_done\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::procedure\_done\_status |
| --- |

## [◆ ](#abbddd0e27178e49abe6eef62bc094a16)steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::steps[] |
| --- |

## [◆ ](#a1801aeaac839831198e17b7d96a5532a)subevent\_abort\_reason

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::subevent\_abort\_reason |
| --- |

## [◆ ](#a49cf181c8518fb3015a0c54f7558aa8c)subevent\_done\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result\_continue::subevent\_done\_status |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_cs\_subevent\_result\_continue](structbt__hci__evt__le__cs__subevent__result__continue.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
