---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__evt__vs__le__connectionless__iq__report.html
original_path: doxygen/html/structbt__hci__evt__vs__le__connectionless__iq__report.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report Struct Reference

`#include <[hci_vs.h](hci__vs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sync\_handle](#a9c199121ac475d635fc51289e8eba979) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [chan\_idx](#ad15beccc7c2207565678ebef72346158) |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [rssi](#a9b7eb8a5cf363c3aec96b49853056dc7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rssi\_ant\_id](#a5fcd776dce904763c5cc6fab9a1373f4) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#a808a2a134104c69073af253a3c4dd1bd) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_durations](#ac0b077d7b5e2b7c5ce61b3060913cad5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_status](#af5b27c1504ce4ff8afe23c28a9ac423f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [per\_evt\_counter](#ab6911af90d85c565615c437715d9c7eb) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sample\_count](#a2698510deb6bd8943bf57104f96673db) |
| struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) | [sample](#a17c9d19883c9d8e34f300fbff614b475) [0] |

## Field Documentation

## [◆ ](#ad15beccc7c2207565678ebef72346158)chan\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::chan\_idx |
| --- |

## [◆ ](#a808a2a134104c69073af253a3c4dd1bd)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::cte\_type |
| --- |

## [◆ ](#af5b27c1504ce4ff8afe23c28a9ac423f)packet\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::packet\_status |
| --- |

## [◆ ](#ab6911af90d85c565615c437715d9c7eb)per\_evt\_counter

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::per\_evt\_counter |
| --- |

## [◆ ](#a9b7eb8a5cf363c3aec96b49853056dc7)rssi

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::rssi |
| --- |

## [◆ ](#a5fcd776dce904763c5cc6fab9a1373f4)rssi\_ant\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::rssi\_ant\_id |
| --- |

## [◆ ](#a17c9d19883c9d8e34f300fbff614b475)sample

| struct [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::sample[0] |
| --- |

## [◆ ](#a2698510deb6bd8943bf57104f96673db)sample\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::sample\_count |
| --- |

## [◆ ](#ac0b077d7b5e2b7c5ce61b3060913cad5)slot\_durations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::slot\_durations |
| --- |

## [◆ ](#a9c199121ac475d635fc51289e8eba979)sync\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report::sync\_handle |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_vs.h](hci__vs_8h_source.md)

- [bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report](structbt__hci__evt__vs__le__connectionless__iq__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
