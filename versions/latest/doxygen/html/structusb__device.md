---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusb__device.html
original_path: doxygen/html/structusb__device.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_device Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [USB host controller driver API](group__uhc__api.md)

Host representation of a USB device.
[More...](#details)

`#include <[uhc.h](uhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) | [node](#a0215608e40123de4a3a79ca440c6c593) |
|  | dlist node |
| void \* | [ctx](#a72ee0e53efd86c91e0cea6c7e873d5ce) |
|  | An opaque pointer to the host context to which this device belongs. |
| struct [k\_mutex](structk__mutex.md) | [mutex](#a4203b2cfd65f70096a43a20c7c37de27) |
|  | Device mutex. |
| struct [usb\_device\_descriptor](structusb__device__descriptor.md) | [dev\_desc](#a24be9609d416d3a184fdedbefa298490) |
|  | USB device descriptor. |
| enum [usb\_device\_state](group__uhc__api.md#ga7127ac2a46b577f2aa1bb9a650e62a3f) | [state](#aa75bbea6a879460b39216453323d177f) |
|  | Device state. |
| enum [usb\_device\_speed](group__uhc__api.md#ga59ba7bbb99177a622f3c073fc48b7bc5) | [speed](#a1b3f4becfd9fbfae80074fc2e76ea6a8) |
|  | Device speed. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [actual\_cfg](#a101d30facb781bd410581fc6c2d3fa59) |
|  | Actual active device configuration. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#aa9062a5b9da663863e6d51ef2e04197b) |
|  | Device address. |
| void \* | [cfg\_desc](#ac98af9fb0d5bba21bc8037a8fcfb3126) |
|  | Pointer to actual device configuration descriptor. |
| struct [usb\_host\_interface](structusb__host__interface.md) | [ifaces](#a5cccbb483d91032f4a7f25f88270747f) [32+1] |
|  | Pointers to device interfaces. |
| struct [usb\_host\_ep](structusb__host__ep.md) | [ep\_out](#a658b9992a472574b1d88e49b7fea478d) [16] |
|  | Pointers to device OUT endpoints. |
| struct [usb\_host\_ep](structusb__host__ep.md) | [ep\_in](#ad3091acb2a713b9e66c595bbf4a736a5) [16] |
|  | Pointers to device IN endpoints. |

## Detailed Description

Host representation of a USB device.

## Field Documentation

## [◆ ](#a101d30facb781bd410581fc6c2d3fa59)actual\_cfg

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device::actual\_cfg |
| --- |

Actual active device configuration.

## [◆ ](#aa9062a5b9da663863e6d51ef2e04197b)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usb\_device::addr |
| --- |

Device address.

## [◆ ](#ac98af9fb0d5bba21bc8037a8fcfb3126)cfg\_desc

| void\* usb\_device::cfg\_desc |
| --- |

Pointer to actual device configuration descriptor.

## [◆ ](#a72ee0e53efd86c91e0cea6c7e873d5ce)ctx

| void\* usb\_device::ctx |
| --- |

An opaque pointer to the host context to which this device belongs.

## [◆ ](#a24be9609d416d3a184fdedbefa298490)dev\_desc

| struct [usb\_device\_descriptor](structusb__device__descriptor.md) usb\_device::dev\_desc |
| --- |

USB device descriptor.

## [◆ ](#ad3091acb2a713b9e66c595bbf4a736a5)ep\_in

| struct [usb\_host\_ep](structusb__host__ep.md) usb\_device::ep\_in[16] |
| --- |

Pointers to device IN endpoints.

## [◆ ](#a658b9992a472574b1d88e49b7fea478d)ep\_out

| struct [usb\_host\_ep](structusb__host__ep.md) usb\_device::ep\_out[16] |
| --- |

Pointers to device OUT endpoints.

## [◆ ](#a5cccbb483d91032f4a7f25f88270747f)ifaces

| struct [usb\_host\_interface](structusb__host__interface.md) usb\_device::ifaces[32+1] |
| --- |

Pointers to device interfaces.

## [◆ ](#a4203b2cfd65f70096a43a20c7c37de27)mutex

| struct [k\_mutex](structk__mutex.md) usb\_device::mutex |
| --- |

Device mutex.

## [◆ ](#a0215608e40123de4a3a79ca440c6c593)node

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) usb\_device::node |
| --- |

dlist node

## [◆ ](#a1b3f4becfd9fbfae80074fc2e76ea6a8)speed

| enum [usb\_device\_speed](group__uhc__api.md#ga59ba7bbb99177a622f3c073fc48b7bc5) usb\_device::speed |
| --- |

Device speed.

## [◆ ](#aa75bbea6a879460b39216453323d177f)state

| enum [usb\_device\_state](group__uhc__api.md#ga7127ac2a46b577f2aa1bb9a650e62a3f) usb\_device::state |
| --- |

Device state.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[uhc.h](uhc_8h_source.md)

- [usb\_device](structusb__device.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
