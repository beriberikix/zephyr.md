---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__hci__evt__vs__le__connection__iq__report.html
original_path: doxygen/html/structbt__hci__evt__vs__le__connection__iq__report.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_vs\_le\_connection\_iq\_report Struct Reference

`#include <[hci_vs.h](hci__vs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_handle](#a941d0e025334a0c041cc7a59b69f0af3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_phy](#a959c7e2b910aec90f8b186550cb7f4d8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_chan\_idx](#af634fa464d4ca435ea935ae58db86cfa) |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [rssi](#a87d4a6ebd1cc172816f3fe786c22f058) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rssi\_ant\_id](#a55a290121f661f155684d37fa0df77d2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#ad714bb1f2292764eba9c506bcc72bccd) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_durations](#a71227b896453143a6a4ad11b7e985a16) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_status](#aa2a9c3589bf8e152627a79c17102ec7c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [conn\_evt\_counter](#aaa29121a6b7fc8f9a76e6b83f6b80f4d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sample\_count](#ab96606229994abe966f03c65d57e5568) |
| struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) | [sample](#abb2b6e915f8de6ad2013a79d0b4ee288) [0] |

## Field Documentation

## [◆ ](#aaa29121a6b7fc8f9a76e6b83f6b80f4d)conn\_evt\_counter

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::conn\_evt\_counter |
| --- |

## [◆ ](#a941d0e025334a0c041cc7a59b69f0af3)conn\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::conn\_handle |
| --- |

## [◆ ](#ad714bb1f2292764eba9c506bcc72bccd)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::cte\_type |
| --- |

## [◆ ](#af634fa464d4ca435ea935ae58db86cfa)data\_chan\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::data\_chan\_idx |
| --- |

## [◆ ](#aa2a9c3589bf8e152627a79c17102ec7c)packet\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::packet\_status |
| --- |

## [◆ ](#a87d4a6ebd1cc172816f3fe786c22f058)rssi

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::rssi |
| --- |

## [◆ ](#a55a290121f661f155684d37fa0df77d2)rssi\_ant\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::rssi\_ant\_id |
| --- |

## [◆ ](#a959c7e2b910aec90f8b186550cb7f4d8)rx\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::rx\_phy |
| --- |

## [◆ ](#abb2b6e915f8de6ad2013a79d0b4ee288)sample

| struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::sample[0] |
| --- |

## [◆ ](#ab96606229994abe966f03c65d57e5568)sample\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::sample\_count |
| --- |

## [◆ ](#a71227b896453143a6a4ad11b7e985a16)slot\_durations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connection\_iq\_report::slot\_durations |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_vs.h](hci__vs_8h_source.md)

- [bt\_hci\_evt\_vs\_le\_connection\_iq\_report](structbt__hci__evt__vs__le__connection__iq__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
