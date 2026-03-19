---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__iso__chan__path.html
original_path: doxygen/html/structbt__iso__chan__path.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_chan\_path Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO Channel Data Path structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pid](#a5e4fb798376489a38a87e4052ff85550) |
|  | Default path ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [format](#a519c884281207d1165a61ccfb7fbcdf4) |
|  | Coding Format. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cid](#a95db7917f7b9e90a33f494233c3266eb) |
|  | Company ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [vid](#aebc12293ba0b10a87f1852e2a3e53a23) |
|  | Vendor-defined Codec ID. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [delay](#adaed07de7e09263e3e941817eeb44258) |
|  | Controller Delay. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cc\_len](#a0da75c4911a197fed7fd7f17c76dddae) |
|  | Codec Configuration length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [cc](#acba5454d02460e8c2d51851677e310bb) |
|  | Pointer to an array containing the Codec Configuration. |

## Detailed Description

ISO Channel Data Path structure.

## Field Documentation

## [◆ ](#acba5454d02460e8c2d51851677e310bb)cc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_iso\_chan\_path::cc |
| --- |

Pointer to an array containing the Codec Configuration.

## [◆ ](#a0da75c4911a197fed7fd7f17c76dddae)cc\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_path::cc\_len |
| --- |

Codec Configuration length.

## [◆ ](#a95db7917f7b9e90a33f494233c3266eb)cid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_chan\_path::cid |
| --- |

Company ID.

## [◆ ](#adaed07de7e09263e3e941817eeb44258)delay

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_iso\_chan\_path::delay |
| --- |

Controller Delay.

## [◆ ](#a519c884281207d1165a61ccfb7fbcdf4)format

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_path::format |
| --- |

Coding Format.

## [◆ ](#a5e4fb798376489a38a87e4052ff85550)pid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_chan\_path::pid |
| --- |

Default path ID.

## [◆ ](#aebc12293ba0b10a87f1852e2a3e53a23)vid

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_chan\_path::vid |
| --- |

Vendor-defined Codec ID.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_chan\_path](structbt__iso__chan__path.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
