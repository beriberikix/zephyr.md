---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__evt__le__connectionless__iq__report.html
original_path: doxygen/html/structbt__hci__evt__le__connectionless__iq__report.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_connectionless\_iq\_report Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sync\_handle](#a36f853d29b8dae1dd393546bbdec5ae2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [chan\_idx](#af50e710884a17191d22f652eaf5788fd) |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [rssi](#a09112f3711aca00b56045c46958c0992) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rssi\_ant\_id](#af8c2055666a97f3c8d95747c59515c31) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cte\_type](#a6b11b00199b002129c569cfec6e83174) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [slot\_durations](#a9d9f0cfe343d81c44e8342b81e2a0608) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [packet\_status](#ab6fb0f6e32e32a3364ae79d867d9e640) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [per\_evt\_counter](#abfeb0aaa411464bbd7bca927219144fb) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sample\_count](#a39109ea3f657d0566a73c7ca81bdd2b1) |
| struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) | [sample](#a1a81f2c8653d85dc29582eed67b4a2a8) [0] |

## Field Documentation

## [◆ ](#af50e710884a17191d22f652eaf5788fd)chan\_idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connectionless\_iq\_report::chan\_idx |
| --- |

## [◆ ](#a6b11b00199b002129c569cfec6e83174)cte\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connectionless\_iq\_report::cte\_type |
| --- |

## [◆ ](#ab6fb0f6e32e32a3364ae79d867d9e640)packet\_status

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connectionless\_iq\_report::packet\_status |
| --- |

## [◆ ](#abfeb0aaa411464bbd7bca927219144fb)per\_evt\_counter

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_connectionless\_iq\_report::per\_evt\_counter |
| --- |

## [◆ ](#a09112f3711aca00b56045c46958c0992)rssi

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) bt\_hci\_evt\_le\_connectionless\_iq\_report::rssi |
| --- |

## [◆ ](#af8c2055666a97f3c8d95747c59515c31)rssi\_ant\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connectionless\_iq\_report::rssi\_ant\_id |
| --- |

## [◆ ](#a1a81f2c8653d85dc29582eed67b4a2a8)sample

| struct [bt\_hci\_le\_iq\_sample](structbt__hci__le__iq__sample.md) bt\_hci\_evt\_le\_connectionless\_iq\_report::sample[0] |
| --- |

## [◆ ](#a39109ea3f657d0566a73c7ca81bdd2b1)sample\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connectionless\_iq\_report::sample\_count |
| --- |

## [◆ ](#a9d9f0cfe343d81c44e8342b81e2a0608)slot\_durations

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_connectionless\_iq\_report::slot\_durations |
| --- |

## [◆ ](#a36f853d29b8dae1dd393546bbdec5ae2)sync\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_connectionless\_iq\_report::sync\_handle |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_connectionless\_iq\_report](structbt__hci__evt__le__connectionless__iq__report.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
