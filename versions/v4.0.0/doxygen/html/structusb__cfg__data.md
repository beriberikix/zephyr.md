---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusb__cfg__data.html
original_path: doxygen/html/structusb__cfg__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_cfg\_data Struct Reference

[USB Device Core API](group____usb__device__core__api.md)

USB device configuration.
[More...](#details)

`#include <[usb_device.h](usb__device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [usb\_device\_description](#a842d4d8a08dd619dd8ee5ccf62ae1e2a) |
|  | USB device description, see [http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors](http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors). |
| void \* | [interface\_descriptor](#ade7cc5e164a82a86d7c57d7a2a4ef306) |
|  | Pointer to interface descriptor. |
| [usb\_interface\_config](group____usb__device__core__api.md#ga3439af9464471b3acdc21f4359efb53a) | [interface\_config](#a3ea73c7ea8759d3637852ff2d02ee96b) |
|  | Function for interface runtime configuration. |
| void(\* | [cb\_usb\_status](#aaf33be8983eb59105beb2d6e551ff195) )(struct [usb\_cfg\_data](structusb__cfg__data.md) \*cfg, enum [usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7) cb\_status, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*param) |
|  | Callback to be notified on USB connection status change. |
| struct [usb\_interface\_cfg\_data](structusb__interface__cfg__data.md) | [interface](#a84b41f3ddabab946ed165c03e3812e10) |
|  | USB interface (Class) handler and storage space. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_endpoints](#a5e58af56af22ecdf0e2222afc408a33b) |
|  | Number of individual endpoints in the device configuration. |
| struct [usb\_ep\_cfg\_data](structusb__ep__cfg__data.md) \* | [endpoint](#adbd7a747db040b54d047c48bed2f50c3) |
|  | Pointer to an array of endpoint structs of length equal to the number of EP associated with the device description, not including control endpoints. |

## Detailed Description

USB device configuration.

The Application instantiates this with given parameters added using the "usb\_set\_config" function. Once this function is called changes to this structure will result in undefined behavior. This structure may only be updated after calls to usb\_deconfig

## Field Documentation

## [◆ ](#aaf33be8983eb59105beb2d6e551ff195)cb\_usb\_status

| void(\* usb\_cfg\_data::cb\_usb\_status) (struct [usb\_cfg\_data](structusb__cfg__data.md) \*cfg, enum [usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7) cb\_status, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*param) |
| --- |

Callback to be notified on USB connection status change.

## [◆ ](#adbd7a747db040b54d047c48bed2f50c3)endpoint

| struct [usb\_ep\_cfg\_data](structusb__ep__cfg__data.md)\* usb\_cfg\_data::endpoint |
| --- |

Pointer to an array of endpoint structs of length equal to the number of EP associated with the device description, not including control endpoints.

## [◆ ](#a84b41f3ddabab946ed165c03e3812e10)interface

| struct [usb\_interface\_cfg\_data](structusb__interface__cfg__data.md) usb\_cfg\_data::interface |
| --- |

USB interface (Class) handler and storage space.

## [◆ ](#a3ea73c7ea8759d3637852ff2d02ee96b)interface\_config

| [usb\_interface\_config](group____usb__device__core__api.md#ga3439af9464471b3acdc21f4359efb53a) usb\_cfg\_data::interface\_config |
| --- |

Function for interface runtime configuration.

## [◆ ](#ade7cc5e164a82a86d7c57d7a2a4ef306)interface\_descriptor

| void\* usb\_cfg\_data::interface\_descriptor |
| --- |

Pointer to interface descriptor.

## [◆ ](#a5e58af56af22ecdf0e2222afc408a33b)num\_endpoints

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_cfg\_data::num\_endpoints |
| --- |

Number of individual endpoints in the device configuration.

## [◆ ](#a842d4d8a08dd619dd8ee5ccf62ae1e2a)usb\_device\_description

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* usb\_cfg\_data::usb\_device\_description |
| --- |

USB device description, see [http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors](http://www.beyondlogic.org/usbnutshell/usb5.shtml#DeviceDescriptors).

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usb\_device.h](usb__device_8h_source.md)

- [usb\_cfg\_data](structusb__cfg__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
