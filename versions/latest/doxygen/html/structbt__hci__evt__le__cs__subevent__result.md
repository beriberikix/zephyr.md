---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__le__cs__subevent__result.html
original_path: doxygen/html/structbt__hci__evt__le__cs__subevent__result.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_cs\_subevent\_result Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_handle](#a3b9c8392fa3aadc2e0673923e0346278) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [config\_id](#a2e8bdef7f85a4cefeaf625d0c3a4db03) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [start\_acl\_conn\_event\_counter](#a0d6b2ca9f148173abb6207cf7c473c7f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [procedure\_counter](#ad08558fd68eb6c43d95a3f0f62bafff0) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [frequency\_compensation](#aba480f7ad78069fd8b83493fac42244e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reference\_power\_level](#a9a7260f63122a94cf7eb6ddc3344f742) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [procedure\_done\_status](#a27a2848009838977f26df75bfc9bc3c3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent\_done\_status](#aeda28dfb30c51ce2955e1c313069c111) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent\_abort\_reason](#acf6f9c4e6fa5897be872d9953993517b): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [procedure\_abort\_reason](#ab81c9c55697b2f2c92e3ea2073932ad1): 4 |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_antenna\_paths](#a9931d5818b801a9c36853f88b259c25e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_steps\_reported](#af8c827d508614f553b9f503d0394411b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [steps](#a43b46a37648b9fde72634dd7dd6a68e6) [] |

## Field Documentation

## [◆ ](#a2e8bdef7f85a4cefeaf625d0c3a4db03)config\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::config\_id |
| --- |

## [◆ ](#a3b9c8392fa3aadc2e0673923e0346278)conn\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_subevent\_result::conn\_handle |
| --- |

## [◆ ](#aba480f7ad78069fd8b83493fac42244e)frequency\_compensation

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_subevent\_result::frequency\_compensation |
| --- |

## [◆ ](#a9931d5818b801a9c36853f88b259c25e)num\_antenna\_paths

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::num\_antenna\_paths |
| --- |

## [◆ ](#af8c827d508614f553b9f503d0394411b)num\_steps\_reported

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::num\_steps\_reported |
| --- |

## [◆ ](#ab81c9c55697b2f2c92e3ea2073932ad1)procedure\_abort\_reason

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::procedure\_abort\_reason |
| --- |

## [◆ ](#ad08558fd68eb6c43d95a3f0f62bafff0)procedure\_counter

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_subevent\_result::procedure\_counter |
| --- |

## [◆ ](#a27a2848009838977f26df75bfc9bc3c3)procedure\_done\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::procedure\_done\_status |
| --- |

## [◆ ](#a9a7260f63122a94cf7eb6ddc3344f742)reference\_power\_level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::reference\_power\_level |
| --- |

## [◆ ](#a0d6b2ca9f148173abb6207cf7c473c7f)start\_acl\_conn\_event\_counter

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cs\_subevent\_result::start\_acl\_conn\_event\_counter |
| --- |

## [◆ ](#a43b46a37648b9fde72634dd7dd6a68e6)steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::steps[] |
| --- |

## [◆ ](#acf6f9c4e6fa5897be872d9953993517b)subevent\_abort\_reason

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::subevent\_abort\_reason |
| --- |

## [◆ ](#aeda28dfb30c51ce2955e1c313069c111)subevent\_done\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cs\_subevent\_result::subevent\_done\_status |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_cs\_subevent\_result](structbt__hci__evt__le__cs__subevent__result.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
