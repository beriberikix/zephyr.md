---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__le__cis__established__v2.html
original_path: doxygen/html/structbt__hci__evt__le__cis__established__v2.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_cis\_established\_v2 Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [status](#a1f43b72368227f212511bb248b4a0e22) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_handle](#a7a7b8303183a916225bb0a3ea11d5480) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cig\_sync\_delay](#a754ad7e68821da0bdb8da0bdeb3b4697) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cis\_sync\_delay](#af134783424a77274abac44613bf61264) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_latency](#ae580ff8c0ef4cd03365cbf1a06aed8bc) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_latency](#a26b25e1615991977735cbfc679d747f3) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_phy](#a9b7ba96597a5131927e365b7a45f8d6f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_phy](#a5a0b08098ac4e6ec93a6ecbbbf4ef587) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [nse](#ac3a87b20b2f10e980639d232a013f702) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_bn](#a5f68c3cba98ed96afef0949f6b14ded9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_bn](#a64b48b20283415100fc8bdf33edf2b0e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_ft](#a2de704a032ac2379528991f2d01e6979) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_ft](#a3b1fc27cca2bc85c36e257aabd8ea612) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [c\_max\_pdu](#acd8cf2d2d85b65d839256f3412a4bb43) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [p\_max\_pdu](#aeea230245aa75dd7f44bf5a4a286e9a5) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a71762f8a31e20b233a252ac974f6d329) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sub\_interval](#a353409fe069aba91c5372ee8ae6e1b79) [3] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [c\_max\_sdu](#ad054af39ddad854423379b3cc7aafc26) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [p\_max\_sdu](#a2a060c0bb2831eb3df0dc8ffb74ecebd) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c\_sdu\_interval](#a926a5faeb98a99333310d860da37f6f5) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [p\_sdu\_interval](#acf30d6a745803fd4e984d66548ceff58) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [framing](#af59ca6d54ca770ef8334ea091bcc53f6) |

## Field Documentation

## [◆ ](#a5f68c3cba98ed96afef0949f6b14ded9)c\_bn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::c\_bn |
| --- |

## [◆ ](#a2de704a032ac2379528991f2d01e6979)c\_ft

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::c\_ft |
| --- |

## [◆ ](#ae580ff8c0ef4cd03365cbf1a06aed8bc)c\_latency

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::c\_latency[3] |
| --- |

## [◆ ](#acd8cf2d2d85b65d839256f3412a4bb43)c\_max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cis\_established\_v2::c\_max\_pdu |
| --- |

## [◆ ](#ad054af39ddad854423379b3cc7aafc26)c\_max\_sdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cis\_established\_v2::c\_max\_sdu |
| --- |

## [◆ ](#a9b7ba96597a5131927e365b7a45f8d6f)c\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::c\_phy |
| --- |

## [◆ ](#a926a5faeb98a99333310d860da37f6f5)c\_sdu\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::c\_sdu\_interval[3] |
| --- |

## [◆ ](#a754ad7e68821da0bdb8da0bdeb3b4697)cig\_sync\_delay

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::cig\_sync\_delay[3] |
| --- |

## [◆ ](#af134783424a77274abac44613bf61264)cis\_sync\_delay

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::cis\_sync\_delay[3] |
| --- |

## [◆ ](#a7a7b8303183a916225bb0a3ea11d5480)conn\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cis\_established\_v2::conn\_handle |
| --- |

## [◆ ](#af59ca6d54ca770ef8334ea091bcc53f6)framing

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::framing |
| --- |

## [◆ ](#a71762f8a31e20b233a252ac974f6d329)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cis\_established\_v2::interval |
| --- |

## [◆ ](#ac3a87b20b2f10e980639d232a013f702)nse

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::nse |
| --- |

## [◆ ](#a64b48b20283415100fc8bdf33edf2b0e)p\_bn

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::p\_bn |
| --- |

## [◆ ](#a3b1fc27cca2bc85c36e257aabd8ea612)p\_ft

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::p\_ft |
| --- |

## [◆ ](#a26b25e1615991977735cbfc679d747f3)p\_latency

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::p\_latency[3] |
| --- |

## [◆ ](#aeea230245aa75dd7f44bf5a4a286e9a5)p\_max\_pdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cis\_established\_v2::p\_max\_pdu |
| --- |

## [◆ ](#a2a060c0bb2831eb3df0dc8ffb74ecebd)p\_max\_sdu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_cis\_established\_v2::p\_max\_sdu |
| --- |

## [◆ ](#a5a0b08098ac4e6ec93a6ecbbbf4ef587)p\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::p\_phy |
| --- |

## [◆ ](#acf30d6a745803fd4e984d66548ceff58)p\_sdu\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::p\_sdu\_interval[3] |
| --- |

## [◆ ](#a1f43b72368227f212511bb248b4a0e22)status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::status |
| --- |

## [◆ ](#a353409fe069aba91c5372ee8ae6e1b79)sub\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_cis\_established\_v2::sub\_interval[3] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_cis\_established\_v2](structbt__hci__evt__le__cis__established__v2.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
