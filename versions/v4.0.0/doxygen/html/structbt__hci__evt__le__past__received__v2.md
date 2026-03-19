---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__evt__le__past__received__v2.html
original_path: doxygen/html/structbt__hci__evt__le__past__received__v2.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_past\_received\_v2 Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#aefe79f973eda8c7c5670c7a721d55d8a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_handle](#adb011949f592ec7f8843d4fd47eca2e9) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [service\_data](#acffc2fa22a16a3a12a4f7dfc3bb45866) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sync\_handle](#a00bf4bdf12fce6cbf2874b9c4ae09f9f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_sid](#a05d798c9415541ef7f5716992157b1a1) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#aff78554e8980635290767e9877ac479b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [phy](#ae7a73293519ab45aec40a9a1aeaa4e89) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a736af2c2ee0afd3cb00e8eb4d103991c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clock\_accuracy](#a78853d14c3bf9a9aba3c4e15b2e06abb) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_subevents](#ab8a2a55fe071218284d60f1a2896945b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent\_interval](#aefdc5ac7ef125f4dc5865c198b98c67d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [response\_slot\_delay](#a9f55d5f6d17d11e72f7cac363a69fe97) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [response\_slot\_spacing](#acf711399e575295dcef73cfeeb844eab) |

## Field Documentation

## [◆ ](#aff78554e8980635290767e9877ac479b)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_evt\_le\_past\_received\_v2::addr |
| --- |

## [◆ ](#a05d798c9415541ef7f5716992157b1a1)adv\_sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received\_v2::adv\_sid |
| --- |

## [◆ ](#a78853d14c3bf9a9aba3c4e15b2e06abb)clock\_accuracy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received\_v2::clock\_accuracy |
| --- |

## [◆ ](#adb011949f592ec7f8843d4fd47eca2e9)conn\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_past\_received\_v2::conn\_handle |
| --- |

## [◆ ](#a736af2c2ee0afd3cb00e8eb4d103991c)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_past\_received\_v2::interval |
| --- |

## [◆ ](#ab8a2a55fe071218284d60f1a2896945b)num\_subevents

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received\_v2::num\_subevents |
| --- |

## [◆ ](#ae7a73293519ab45aec40a9a1aeaa4e89)phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received\_v2::phy |
| --- |

## [◆ ](#a9f55d5f6d17d11e72f7cac363a69fe97)response\_slot\_delay

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received\_v2::response\_slot\_delay |
| --- |

## [◆ ](#acf711399e575295dcef73cfeeb844eab)response\_slot\_spacing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received\_v2::response\_slot\_spacing |
| --- |

## [◆ ](#acffc2fa22a16a3a12a4f7dfc3bb45866)service\_data

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_past\_received\_v2::service\_data |
| --- |

## [◆ ](#aefe79f973eda8c7c5670c7a721d55d8a)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received\_v2::status |
| --- |

## [◆ ](#aefdc5ac7ef125f4dc5865c198b98c67d)subevent\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_past\_received\_v2::subevent\_interval |
| --- |

## [◆ ](#a00bf4bdf12fce6cbf2874b9c4ae09f9f)sync\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_past\_received\_v2::sync\_handle |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_past\_received\_v2](structbt__hci__evt__le__past__received__v2.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
