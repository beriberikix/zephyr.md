---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__scan__param.html
original_path: doxygen/html/structbt__le__scan__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_scan\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

LE scan parameters.
[More...](#details)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a02d75322390287c3fa754bf915660d0c) |
|  | Scan type (BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [options](#ac815b05fee8ce0dd24228305b7596207) |
|  | Bit-field of scanning options. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a2f4e053d97c62b6fdf42a245908607f8) |
|  | Scan interval (N \* 0.625 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [window](#a37a7ee82e86a91cf7a9c2adf60bb526a) |
|  | Scan window (N \* 0.625 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout](#a3e71ce551dcc7762c29e2316996e2912) |
|  | Scan timeout (N \* 10 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval\_coded](#a67a20bc94a3d98fa10af7b5b42dde328) |
|  | Scan interval LE Coded PHY (N \* 0.625 MS). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [window\_coded](#a93166af55dca71393c60cb3f7ac6d809) |
|  | Scan window LE Coded PHY (N \* 0.625 MS). |

## Detailed Description

LE scan parameters.

## Field Documentation

## [◆ ](#a2f4e053d97c62b6fdf42a245908607f8)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_scan\_param::interval |
| --- |

Scan interval (N \* 0.625 ms).

Note
:   When `CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL` is enabled and the application wants to scan and connect in parallel, the Bluetooth Controller may require the scan interval used for scanning and connection establishment to be equal to obtain the best performance.

## [◆ ](#a67a20bc94a3d98fa10af7b5b42dde328)interval\_coded

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_scan\_param::interval\_coded |
| --- |

Scan interval LE Coded PHY (N \* 0.625 MS).

Set zero to use same as LE 1M PHY scan interval.

## [◆ ](#ac815b05fee8ce0dd24228305b7596207)options

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_scan\_param::options |
| --- |

Bit-field of scanning options.

## [◆ ](#a3e71ce551dcc7762c29e2316996e2912)timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_scan\_param::timeout |
| --- |

Scan timeout (N \* 10 ms).

Application will be notified by the scan timeout callback. Set zero to disable timeout.

## [◆ ](#a02d75322390287c3fa754bf915660d0c)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_scan\_param::type |
| --- |

Scan type (BT\_LE\_SCAN\_TYPE\_ACTIVE or BT\_LE\_SCAN\_TYPE\_PASSIVE).

## [◆ ](#a37a7ee82e86a91cf7a9c2adf60bb526a)window

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_scan\_param::window |
| --- |

Scan window (N \* 0.625 ms).

Note
:   When `CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL` is enabled and the application wants to scan and connect in parallel, the Bluetooth Controller may require the scan window used for scanning and connection establishment to be equal to obtain the best performance.

## [◆ ](#a93166af55dca71393c60cb3f7ac6d809)window\_coded

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_scan\_param::window\_coded |
| --- |

Scan window LE Coded PHY (N \* 0.625 MS).

Set zero to use same as LE 1M PHY scan window.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_scan\_param](structbt__le__scan__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
