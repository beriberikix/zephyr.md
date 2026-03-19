---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusb__ep__cfg__data.html
original_path: doxygen/html/structusb__ep__cfg__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_ep\_cfg\_data Struct Reference

[USB Device Core API](group____usb__device__core__api.md)

USB Endpoint Configuration.
[More...](#details)

`#include <[usb_device.h](usb__device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [usb\_ep\_callback](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725) | [ep\_cb](#a5d03244508b6a58d9d0bfb896c2537d1) |
|  | Callback function for notification of data received and available to application or transmit done, NULL if callback not required by application code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ep\_addr](#aa87f676a577a8c1605bb9a8fa04f411c) |
|  | The number associated with the EP in the device configuration structure IN EP = 0x80 | <endpoint number> OUT EP = 0x00 | <endpoint number>. |

## Detailed Description

USB Endpoint Configuration.

This structure contains configuration for the endpoint.

## Field Documentation

## [◆ ](#aa87f676a577a8c1605bb9a8fa04f411c)ep\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_ep\_cfg\_data::ep\_addr |
| --- |

The number associated with the EP in the device configuration structure IN EP = 0x80 | <endpoint number> OUT EP = 0x00 | <endpoint number>.

## [◆ ](#a5d03244508b6a58d9d0bfb896c2537d1)ep\_cb

| [usb\_ep\_callback](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725) usb\_ep\_cfg\_data::ep\_cb |
| --- |

Callback function for notification of data received and available to application or transmit done, NULL if callback not required by application code.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usb\_device.h](usb__device_8h_source.md)

- [usb\_ep\_cfg\_data](structusb__ep__cfg__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
