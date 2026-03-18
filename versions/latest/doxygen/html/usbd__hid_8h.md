---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/usbd__hid_8h.html
original_path: doxygen/html/usbd__hid_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_hid.h File Reference

USBD HID device API header.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/usb/class/hid.h](hid_8h_source.md)>`

[Go to the source code of this file.](usbd__hid_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [hid\_device\_ops](structhid__device__ops.md) |
|  | HID device user callbacks. [More...](structhid__device__ops.md#details) |

| Enumerations | |
| --- | --- |
| enum | { [HID\_REPORT\_TYPE\_INPUT](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1da451c0c5bb29aa79f5ce554ac9a914acd) = 1 , [HID\_REPORT\_TYPE\_OUTPUT](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dac019f1ccb72d64b8ce9dc5c5d952f8a3) , [HID\_REPORT\_TYPE\_FEATURE](group__usbd__hid__device.md#ggabfdd923d3dea1fc17d6c21f4ad7dab1dadb047f4ed99575941ca9d857244f5aea) } |
|  | HID report types Report types used in Get/Set Report requests. [More...](group__usbd__hid__device.md#gabfdd923d3dea1fc17d6c21f4ad7dab1d) |

| Functions | |
| --- | --- |
| int | [hid\_device\_register](group__usbd__hid__device.md#gabb4502a7c3ab5d2400c039549577f4d0) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const rdesc, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rsize, const struct [hid\_device\_ops](structhid__device__ops.md) \*const ops) |
|  | Register HID device report descriptor and user callbacks. |
| int | [hid\_device\_submit\_report](group__usbd__hid__device.md#ga547f99b1089a4d65a297faa5d6e8edd8) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const report) |
|  | Submit new input report. |

## Detailed Description

USBD HID device API header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_hid.h](usbd__hid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
