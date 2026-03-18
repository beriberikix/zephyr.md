---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__hci__evt__le__connection__iq__report.html
original_path: doxygen/html/structbt__hci__evt__le__connection__iq__report.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_connection\_iq\_report Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_handle](#a446f4eab3db19452a84023a676333d1d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_phy](#aa052e03491647acc9f7a6dc7d91cedcc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_chan\_idx](#ac01a14c591c8bd8e6313aff021ca8d61) |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [rssi](#a49e63523f7219174540666c7e5ab3550) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rssi\_ant\_id](#a135498a4abae604967f94840e2f88d2c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#a0188ce28a6c0a2002ae2c64a7bd95e52) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_durations](#a74670ca77bb2be81db2cee613dd9c82b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_status](#af66e8f09a4442b658b80a6eb4dd3064b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_evt\_counter](#a1f388ba96bd52f9ce0f68bacb2945ed8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sample\_count](#a801dd9373935ba06175ac52237fea759) |
| struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) | [sample](#a5acc2683312523a1137db7897a7373a6) [0] |

## Field Documentation

## [◆ ](#a1f388ba96bd52f9ce0f68bacb2945ed8)conn\_evt\_counter

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_connection\_iq\_report::conn\_evt\_counter |
| --- |

## [◆ ](#a446f4eab3db19452a84023a676333d1d)conn\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_connection\_iq\_report::conn\_handle |
| --- |

## [◆ ](#a0188ce28a6c0a2002ae2c64a7bd95e52)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connection\_iq\_report::cte\_type |
| --- |

## [◆ ](#ac01a14c591c8bd8e6313aff021ca8d61)data\_chan\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connection\_iq\_report::data\_chan\_idx |
| --- |

## [◆ ](#af66e8f09a4442b658b80a6eb4dd3064b)packet\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connection\_iq\_report::packet\_status |
| --- |

## [◆ ](#a49e63523f7219174540666c7e5ab3550)rssi

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_evt\_le\_connection\_iq\_report::rssi |
| --- |

## [◆ ](#a135498a4abae604967f94840e2f88d2c)rssi\_ant\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connection\_iq\_report::rssi\_ant\_id |
| --- |

## [◆ ](#aa052e03491647acc9f7a6dc7d91cedcc)rx\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connection\_iq\_report::rx\_phy |
| --- |

## [◆ ](#a5acc2683312523a1137db7897a7373a6)sample

| struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) bt\_hci\_evt\_le\_connection\_iq\_report::sample[0] |
| --- |

## [◆ ](#a801dd9373935ba06175ac52237fea759)sample\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connection\_iq\_report::sample\_count |
| --- |

## [◆ ](#a74670ca77bb2be81db2cee613dd9c82b)slot\_durations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connection\_iq\_report::slot\_durations |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_connection\_iq\_report](structbt__hci__evt__le__connection__iq__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
