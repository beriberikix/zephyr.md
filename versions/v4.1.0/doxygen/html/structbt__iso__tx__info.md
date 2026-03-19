---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__iso__tx__info.html
original_path: doxygen/html/structbt__iso__tx__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_tx\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Meta Data structure for transmitted ISO packets.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ts](#ac8a6a4c073e4df1553d32339a6e4b051) |
|  | CIG reference point or BIG anchor point of a transmitted SDU, in microseconds. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [offset](#a0cff6aa2893fdc11160e4327afebed13) |
|  | Time offset, in microseconds. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [seq\_num](#a2791edea2f4f4459acc24c8dbaa33ded) |
|  | Packet sequence number. |

## Detailed Description

ISO Meta Data structure for transmitted ISO packets.

## Field Documentation

## [◆ ](#a0cff6aa2893fdc11160e4327afebed13)offset

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_tx\_info::offset |
| --- |

Time offset, in microseconds.

## [◆ ](#a2791edea2f4f4459acc24c8dbaa33ded)seq\_num

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_tx\_info::seq\_num |
| --- |

Packet sequence number.

## [◆ ](#ac8a6a4c073e4df1553d32339a6e4b051)ts

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_tx\_info::ts |
| --- |

CIG reference point or BIG anchor point of a transmitted SDU, in microseconds.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_tx\_info](structbt__iso__tx__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
