---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structusbd__class__api.html
original_path: doxygen/html/structusbd__class__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_class\_api Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

USB device support class instance API.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [feature\_halt](#a09475f1b29f482e548b6bc168dcd19e7) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) halted) |
|  | Feature halt state update handler. |
| void(\* | [update](#a11d09e35f9d4c4d6b18e12bf4ea241b0) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) alternate) |
|  | Configuration update handler. |
| int(\* | [control\_to\_dev](#ab37dd5f2bf4029f149e69046702626a1) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, const struct [net\_buf](structnet__buf.md) \*const buf) |
|  | USB control request handler to device. |
| int(\* | [control\_to\_host](#ac52356c07c26a3bcb1025cd6778ca8ef) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | USB control request handler to host. |
| int(\* | [request](#a70425718fd34534fd976240340b4496d) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, struct [net\_buf](structnet__buf.md) \*buf, int err) |
|  | Endpoint request completion event handler. |
| void(\* | [suspended](#a598afe76b5c2f9e75a049fe785393e04) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | USB power management handler suspended. |
| void(\* | [resumed](#ae6f3a658e5768f5d6672cd0e5f2d24a5) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | USB power management handler resumed. |
| void(\* | [sof](#a488b102936b5cd3e4095578119b71510) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Start of Frame. |
| void(\* | [enable](#ab42f61db338471f0c5260576680409e9) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Class associated configuration is selected. |
| void(\* | [disable](#afd43bfa4aab664c50648aa59a0c713de) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Class associated configuration is disabled. |
| int(\* | [init](#a7d749f007d70e30f76aa121067b7a5c6) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Initialization of the class implementation. |
| void(\* | [shutdown](#a5ca5bc6d3f5220bd3658d9398e09016e) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Shutdown of the class implementation. |
| void \*(\* | [get\_desc](#a9d6ecb2a5ff55427502ba7ad8f96a146) )(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed) |
|  | Get function descriptor based on speed parameter. |

## Detailed Description

USB device support class instance API.

## Field Documentation

## [◆ ](#ab37dd5f2bf4029f149e69046702626a1)control\_to\_dev

| int(\* usbd\_class\_api::control\_to\_dev) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, const struct [net\_buf](structnet__buf.md) \*const buf) |
| --- |

USB control request handler to device.

## [◆ ](#ac52356c07c26a3bcb1025cd6778ca8ef)control\_to\_host

| int(\* usbd\_class\_api::control\_to\_host) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, struct [net\_buf](structnet__buf.md) \*const buf) |
| --- |

USB control request handler to host.

## [◆ ](#afd43bfa4aab664c50648aa59a0c713de)disable

| void(\* usbd\_class\_api::disable) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
| --- |

Class associated configuration is disabled.

## [◆ ](#ab42f61db338471f0c5260576680409e9)enable

| void(\* usbd\_class\_api::enable) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
| --- |

Class associated configuration is selected.

## [◆ ](#a09475f1b29f482e548b6bc168dcd19e7)feature\_halt

| void(\* usbd\_class\_api::feature\_halt) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) halted) |
| --- |

Feature halt state update handler.

## [◆ ](#a9d6ecb2a5ff55427502ba7ad8f96a146)get\_desc

| void \*(\* usbd\_class\_api::get\_desc) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed) |
| --- |

Get function descriptor based on speed parameter.

## [◆ ](#a7d749f007d70e30f76aa121067b7a5c6)init

| int(\* usbd\_class\_api::init) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
| --- |

Initialization of the class implementation.

## [◆ ](#a70425718fd34534fd976240340b4496d)request

| int(\* usbd\_class\_api::request) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, struct [net\_buf](structnet__buf.md) \*buf, int err) |
| --- |

Endpoint request completion event handler.

## [◆ ](#ae6f3a658e5768f5d6672cd0e5f2d24a5)resumed

| void(\* usbd\_class\_api::resumed) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
| --- |

USB power management handler resumed.

## [◆ ](#a5ca5bc6d3f5220bd3658d9398e09016e)shutdown

| void(\* usbd\_class\_api::shutdown) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
| --- |

Shutdown of the class implementation.

## [◆ ](#a488b102936b5cd3e4095578119b71510)sof

| void(\* usbd\_class\_api::sof) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
| --- |

Start of Frame.

## [◆ ](#a598afe76b5c2f9e75a049fe785393e04)suspended

| void(\* usbd\_class\_api::suspended) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
| --- |

USB power management handler suspended.

## [◆ ](#a11d09e35f9d4c4d6b18e12bf4ea241b0)update

| void(\* usbd\_class\_api::update) (struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) alternate) |
| --- |

Configuration update handler.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_class\_api](structusbd__class__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
