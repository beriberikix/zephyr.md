---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__hci__cp__le__set__cig__params.html
original_path: doxygen/html/structbt__hci__cp__le__set__cig__params.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_cp\_le\_set\_cig\_params Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cig\_id](#a7dbf75c6ed92a053c4ec0d8f7268c92e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_interval](#a14f5c0cf7f99ab406714501038048035) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_interval](#a50a260a15f3a0ceae716da6c04c5b768) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sca](#a46a657cdfbc7a49e6761d9f18d980c2a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packing](#a79fc069492741f14f348650abef4c66b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [framing](#a867bf5ddbcadd27dbec2c3059d67d6d6) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [c\_latency](#afec8ebd17cc6ca5b3d13ef54f406df62) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [p\_latency](#a810822396b97d54988ec57561b4ee7d5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_cis](#adf468a8a195447a7bbed4dcd53d287f6) |
| struct [bt\_hci\_cis\_params](structbt__hci__cis__params.md) | [cis](#ac922e59065920421f40468754d2ba5a2) [0] |

## Field Documentation

## [◆ ](#a14f5c0cf7f99ab406714501038048035)c\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_cig\_params::c\_interval[3] |
| --- |

## [◆ ](#afec8ebd17cc6ca5b3d13ef54f406df62)c\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_set\_cig\_params::c\_latency |
| --- |

## [◆ ](#a7dbf75c6ed92a053c4ec0d8f7268c92e)cig\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_cig\_params::cig\_id |
| --- |

## [◆ ](#ac922e59065920421f40468754d2ba5a2)cis

| struct [bt\_hci\_cis\_params](structbt__hci__cis__params.md) bt\_hci\_cp\_le\_set\_cig\_params::cis[0] |
| --- |

## [◆ ](#a867bf5ddbcadd27dbec2c3059d67d6d6)framing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_cig\_params::framing |
| --- |

## [◆ ](#adf468a8a195447a7bbed4dcd53d287f6)num\_cis

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_cig\_params::num\_cis |
| --- |

## [◆ ](#a50a260a15f3a0ceae716da6c04c5b768)p\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_cig\_params::p\_interval[3] |
| --- |

## [◆ ](#a810822396b97d54988ec57561b4ee7d5)p\_latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_set\_cig\_params::p\_latency |
| --- |

## [◆ ](#a79fc069492741f14f348650abef4c66b)packing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_cig\_params::packing |
| --- |

## [◆ ](#a46a657cdfbc7a49e6761d9f18d980c2a)sca

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_cig\_params::sca |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_cp\_le\_set\_cig\_params](structbt__hci__cp__le__set__cig__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
