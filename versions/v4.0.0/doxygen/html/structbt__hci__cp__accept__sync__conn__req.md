---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__cp__accept__sync__conn__req.html
original_path: doxygen/html/structbt__hci__cp__accept__sync__conn__req.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_cp\_accept\_sync\_conn\_req Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_addr\_t](structbt__addr__t.md) | [bdaddr](#a6a5a56d3a9d1a6d1064e7bd4c9fd333e) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tx\_bandwidth](#a53fe4c6d61dbb99f99aa445b2c47a8ef) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rx\_bandwidth](#aceda6dbd3e221ad080850e9635886a86) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_latency](#a4ba6dffd840ef868524b490d227fd085) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [content\_format](#adba31b588bf12e852cc43b85c006aaa3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [retrans\_effort](#ab5ece67c5a1e62fc4124556eef743c26) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pkt\_type](#ab5d9c27ebdf45fb54b0c6330b5b095be) |

## Field Documentation

## [◆ ](#a6a5a56d3a9d1a6d1064e7bd4c9fd333e)bdaddr

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_cp\_accept\_sync\_conn\_req::bdaddr |
| --- |

## [◆ ](#adba31b588bf12e852cc43b85c006aaa3)content\_format

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_accept\_sync\_conn\_req::content\_format |
| --- |

## [◆ ](#a4ba6dffd840ef868524b490d227fd085)max\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_accept\_sync\_conn\_req::max\_latency |
| --- |

## [◆ ](#ab5d9c27ebdf45fb54b0c6330b5b095be)pkt\_type

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_accept\_sync\_conn\_req::pkt\_type |
| --- |

## [◆ ](#ab5ece67c5a1e62fc4124556eef743c26)retrans\_effort

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_accept\_sync\_conn\_req::retrans\_effort |
| --- |

## [◆ ](#aceda6dbd3e221ad080850e9635886a86)rx\_bandwidth

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_hci\_cp\_accept\_sync\_conn\_req::rx\_bandwidth |
| --- |

## [◆ ](#a53fe4c6d61dbb99f99aa445b2c47a8ef)tx\_bandwidth

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_hci\_cp\_accept\_sync\_conn\_req::tx\_bandwidth |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_cp\_accept\_sync\_conn\_req](structbt__hci__cp__accept__sync__conn__req.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
