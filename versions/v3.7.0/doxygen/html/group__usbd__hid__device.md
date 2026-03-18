---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__usbd__hid__device.html
original_path: doxygen/html/group__usbd__hid__device.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USBD HID device API

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

USBD HID Device API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [hid\_device\_ops](structhid__device__ops.md) |
|  | HID device user callbacks. [More...](structhid__device__ops.md#details) |

| Enumerations | |
| --- | --- |
| enum | { [HID\_REPORT\_TYPE\_INPUT](#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd) = 1 , [HID\_REPORT\_TYPE\_OUTPUT](#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3) , [HID\_REPORT\_TYPE\_FEATURE](#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea) } |
|  | HID report types Report types used in Get/Set Report requests. [More...](#gabfdd923d3dea1fc17d6c21f4ad7dab1d) |

| Functions | |
| --- | --- |
| int | [hid\_device\_register](#gabb4502a7c3ab5d2400c039549577f4d0) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const rdesc, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rsize, const struct [hid\_device\_ops](structhid__device__ops.md) \*const ops) |
|  | Register HID device report descriptor and user callbacks. |
| int | [hid\_device\_submit\_report](#ga547f99b1089a4d65a297faa5d6e8edd8) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const report) |
|  | Submit new input report. |

## Detailed Description

USBD HID Device API.

## Enumeration Type Documentation

## [◆ ](#gabfdd923d3dea1fc17d6c21f4ad7dab1d)anonymous enum

| anonymous enum |
| --- |

`#include <[usbd_hid.h](usbd__hid_8h.md)>`

HID report types Report types used in Get/Set Report requests.

| Enumerator | |
| --- | --- |
| HID\_REPORT\_TYPE\_INPUT |  |
| HID\_REPORT\_TYPE\_OUTPUT |  |
| HID\_REPORT\_TYPE\_FEATURE |  |

## Function Documentation

## [◆ ](#gabb4502a7c3ab5d2400c039549577f4d0)hid\_device\_register()

| int hid\_device\_register | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const | *rdesc*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *rsize*, |
|  |  | const struct [hid\_device\_ops](structhid__device__ops.md) \*const | *ops* ) |

`#include <[usbd_hid.h](usbd__hid_8h.md)>`

Register HID device report descriptor and user callbacks.

The device must register report descriptor and user callbacks before USB device support is initialized and enabled.

Parameters
:   | [in] | dev | Pointer to HID device |
    | --- | --- | --- |
    | [in] | rdesc | Pointer to HID report descriptor |
    | [in] | rsize | Size of HID report descriptor |
    | [in] | ops | Pointer to HID device callbacks |

## [◆ ](#ga547f99b1089a4d65a297faa5d6e8edd8)hid\_device\_submit\_report()

| int hid\_device\_submit\_report | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *size*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const | *report* ) |

`#include <[usbd_hid.h](usbd__hid_8h.md)>`

Submit new input report.

Submit a new input report to be sent via the interrupt IN pipe. If sync is true, the functions will block until the report is sent. If the device does not provide input\_report\_done() callback, [hid\_device\_submit\_report()](#ga547f99b1089a4d65a297faa5d6e8edd8) will be processed synchronously.

Parameters
:   | [in] | dev | Pointer to HID device |
    | --- | --- | --- |
    | [in] | size | Size of the input report |
    | [in] | report | Input report buffer. Report buffer must be aligned. |

Returns
:   0 on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
