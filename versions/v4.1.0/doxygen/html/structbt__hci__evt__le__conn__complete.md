---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__le__conn__complete.html
original_path: doxygen/html/structbt__hci__evt__le__conn__complete.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_conn\_complete Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a897981117139c0e53ea7275b689f3799) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [handle](#a67618a1efa0149fadc1063a719d5b674) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [role](#a8455e714d4333d90c2f117892f3dcd6f) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [peer\_addr](#a97e1aaa10832292ddfe4ee6731ef8999) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#abe4bc0407d0295329631cb14672a7ee7) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [latency](#ab60cb42ecc83632c61656cd352b71cbe) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [supv\_timeout](#a4a90c9824d167b6c45b301e18bfe7f17) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clock\_accuracy](#a3fff4c3b30da5922f75d36d97fdeee33) |

## Field Documentation

## [◆ ](#a3fff4c3b30da5922f75d36d97fdeee33)clock\_accuracy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_conn\_complete::clock\_accuracy |
| --- |

## [◆ ](#a67618a1efa0149fadc1063a719d5b674)handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_conn\_complete::handle |
| --- |

## [◆ ](#abe4bc0407d0295329631cb14672a7ee7)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_conn\_complete::interval |
| --- |

## [◆ ](#ab60cb42ecc83632c61656cd352b71cbe)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_conn\_complete::latency |
| --- |

## [◆ ](#a97e1aaa10832292ddfe4ee6731ef8999)peer\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_evt\_le\_conn\_complete::peer\_addr |
| --- |

## [◆ ](#a8455e714d4333d90c2f117892f3dcd6f)role

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_conn\_complete::role |
| --- |

## [◆ ](#a897981117139c0e53ea7275b689f3799)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_conn\_complete::status |
| --- |

## [◆ ](#a4a90c9824d167b6c45b301e18bfe7f17)supv\_timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_conn\_complete::supv\_timeout |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_conn\_complete](structbt__hci__evt__le__conn__complete.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
