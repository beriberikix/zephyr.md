---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structusbd__class__api.html
original_path: doxygen/html/structusbd__class__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| void(\* | [feature\_halt](#a90d7370d6d58467b8516dc23fa85da6e) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) halted) |
|  | Feature halt state update handler. |
| void(\* | [update](#adaa09908b17f85e97f39266f79cb32a8) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) alternate) |
|  | Configuration update handler. |
| int(\* | [control\_to\_dev](#a5c7fa1a0d05a8eab486e1ee61cc0b73f) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, const struct [net\_buf](structnet__buf.md) \*const buf) |
|  | USB control request handler to device. |
| int(\* | [control\_to\_host](#a5eac92c9ab6ebb6eb61c683f0b289e21) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | USB control request handler to host. |
| int(\* | [request](#aff8426da1f7dd1f5fa5d27ce135bf0f8) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node, struct [net\_buf](structnet__buf.md) \*buf, int err) |
|  | Endpoint request completion event handler. |
| void(\* | [suspended](#a36bf045b23c0fda4865db2978c94b6d1) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
|  | USB power management handler suspended. |
| void(\* | [resumed](#a26411223bbe266a1cb7015a7ccb5c100) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
|  | USB power management handler resumed. |
| void(\* | [sof](#a9dd501ae803c5f0e8b4d62f4a57b04ca) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
|  | Start of Frame. |
| void(\* | [enable](#a03585c10422b27cf7712cc88e99a5fc2) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
|  | Class associated configuration is selected. |
| void(\* | [disable](#a3e9c54c768d12341d242cdecd83e96bd) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
|  | Class associated configuration is disabled. |
| int(\* | [init](#a20ec6b44ddded48eadffc9a82115766e) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
|  | Initialization of the class implementation. |
| void(\* | [shutdown](#a11e02db41023c9a4d8e853d1eaddac00) )(struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
|  | Shutdown of the class implementation. |

## Detailed Description

USB device support class instance API.

## Field Documentation

## [◆ ](#a5c7fa1a0d05a8eab486e1ee61cc0b73f)control\_to\_dev

| int(\* usbd\_class\_api::control\_to\_dev) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, const struct [net\_buf](structnet__buf.md) \*const buf) |
| --- |

USB control request handler to device.

## [◆ ](#a5eac92c9ab6ebb6eb61c683f0b289e21)control\_to\_host

| int(\* usbd\_class\_api::control\_to\_host) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node, const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup, struct [net\_buf](structnet__buf.md) \*const buf) |
| --- |

USB control request handler to host.

## [◆ ](#a3e9c54c768d12341d242cdecd83e96bd)disable

| void(\* usbd\_class\_api::disable) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
| --- |

Class associated configuration is disabled.

## [◆ ](#a03585c10422b27cf7712cc88e99a5fc2)enable

| void(\* usbd\_class\_api::enable) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
| --- |

Class associated configuration is selected.

## [◆ ](#a90d7370d6d58467b8516dc23fa85da6e)feature\_halt

| void(\* usbd\_class\_api::feature\_halt) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) halted) |
| --- |

Feature halt state update handler.

## [◆ ](#a20ec6b44ddded48eadffc9a82115766e)init

| int(\* usbd\_class\_api::init) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
| --- |

Initialization of the class implementation.

## [◆ ](#aff8426da1f7dd1f5fa5d27ce135bf0f8)request

| int(\* usbd\_class\_api::request) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node, struct [net\_buf](structnet__buf.md) \*buf, int err) |
| --- |

Endpoint request completion event handler.

## [◆ ](#a26411223bbe266a1cb7015a7ccb5c100)resumed

| void(\* usbd\_class\_api::resumed) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
| --- |

USB power management handler resumed.

## [◆ ](#a11e02db41023c9a4d8e853d1eaddac00)shutdown

| void(\* usbd\_class\_api::shutdown) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
| --- |

Shutdown of the class implementation.

## [◆ ](#a9dd501ae803c5f0e8b4d62f4a57b04ca)sof

| void(\* usbd\_class\_api::sof) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
| --- |

Start of Frame.

## [◆ ](#a36bf045b23c0fda4865db2978c94b6d1)suspended

| void(\* usbd\_class\_api::suspended) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node) |
| --- |

USB power management handler suspended.

## [◆ ](#adaa09908b17f85e97f39266f79cb32a8)update

| void(\* usbd\_class\_api::update) (struct [usbd\_class\_node](structusbd__class__node.md) \*const node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) alternate) |
| --- |

Configuration update handler.

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_class\_api](structusbd__class__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
