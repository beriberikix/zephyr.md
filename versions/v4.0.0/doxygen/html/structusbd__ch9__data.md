---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusbd__ch9__data.html
original_path: doxygen/html/structusbd__ch9__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_ch9\_data Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

USB device support middle layer runtime data.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [usb\_setup\_packet](structusb__setup__packet.md) | [setup](#a85f96c69cede5b51c1f9739a4ae67f4d) |
|  | Setup packet, up-to-date for the respective control request. |
| int | [ctrl\_type](#a095a2a98f19ea40e8bd1bf65eed77dac) |
|  | Control type, internally used for stage verification. |
| enum [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) | [state](#a70d1a1be0aab6167ca4f4580b9c65eff) |
|  | Protocol state of the USB device stack. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ep\_halt](#a504360b7cb11240a2fda68344f2e3b62) |
|  | Halted endpoints bitmap. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [configuration](#a1f759fb0d758e50c4589b6b6b1fd2a24) |
|  | USB device stack selected configuration. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [post\_status](#a6ab6f611fd1eff8d6fde0617c587fefb) |
|  | Post status stage work required, e.g. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [alternate](#a8f831eca1974b8411072f8102c444d45) [16U] |
|  | Array to track interfaces alternate settings. |

## Detailed Description

USB device support middle layer runtime data.

## Field Documentation

## [◆ ](#a8f831eca1974b8411072f8102c444d45)alternate

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usbd\_ch9\_data::alternate[16U] |
| --- |

Array to track interfaces alternate settings.

## [◆ ](#a1f759fb0d758e50c4589b6b6b1fd2a24)configuration

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usbd\_ch9\_data::configuration |
| --- |

USB device stack selected configuration.

## [◆ ](#a095a2a98f19ea40e8bd1bf65eed77dac)ctrl\_type

| int usbd\_ch9\_data::ctrl\_type |
| --- |

Control type, internally used for stage verification.

## [◆ ](#a504360b7cb11240a2fda68344f2e3b62)ep\_halt

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usbd\_ch9\_data::ep\_halt |
| --- |

Halted endpoints bitmap.

## [◆ ](#a6ab6f611fd1eff8d6fde0617c587fefb)post\_status

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usbd\_ch9\_data::post\_status |
| --- |

Post status stage work required, e.g.

set new device address

## [◆ ](#a85f96c69cede5b51c1f9739a4ae67f4d)setup

| struct [usb\_setup\_packet](structusb__setup__packet.md) usbd\_ch9\_data::setup |
| --- |

Setup packet, up-to-date for the respective control request.

## [◆ ](#a70d1a1be0aab6167ca4f4580b9c65eff)state

| enum [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) usbd\_ch9\_data::state |
| --- |

Protocol state of the USB device stack.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_ch9\_data](structusbd__ch9__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
