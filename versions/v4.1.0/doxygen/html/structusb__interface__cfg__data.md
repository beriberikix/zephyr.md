---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusb__interface__cfg__data.html
original_path: doxygen/html/structusb__interface__cfg__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_interface\_cfg\_data Struct Reference

[USB Device Core API](group____usb__device__core__api.md)

USB Interface Configuration.
[More...](#details)

`#include <[usb_device.h](usb__device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) | [class\_handler](#a144ed5ba67d1adb8dbb1d936ac440272) |
|  | Handler for USB Class specific Control (EP 0) communications. |
| [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) | [vendor\_handler](#a2d5d65d41cef609173287161797318d2) |
|  | Handler for USB Vendor specific commands. |
| [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) | [custom\_handler](#a117a1a88c02048ee43994d3e5a4ce922) |
|  | The custom request handler gets a first chance at handling the request before it is handed over to the 'chapter 9' request handler. |

## Detailed Description

USB Interface Configuration.

This structure contains USB interface configuration.

## Field Documentation

## [◆ ](#a144ed5ba67d1adb8dbb1d936ac440272)class\_handler

| [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) usb\_interface\_cfg\_data::class\_handler |
| --- |

Handler for USB Class specific Control (EP 0) communications.

## [◆ ](#a117a1a88c02048ee43994d3e5a4ce922)custom\_handler

| [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) usb\_interface\_cfg\_data::custom\_handler |
| --- |

The custom request handler gets a first chance at handling the request before it is handed over to the 'chapter 9' request handler.

return 0 on success, -EINVAL if the request has not been handled by the custom handler and instead needs to be handled by the core USB stack. Any other error code to denote failure within the custom handler.

## [◆ ](#a2d5d65d41cef609173287161797318d2)vendor\_handler

| [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804) usb\_interface\_cfg\_data::vendor\_handler |
| --- |

Handler for USB Vendor specific commands.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usb\_device.h](usb__device_8h_source.md)

- [usb\_interface\_cfg\_data](structusb__interface__cfg__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
