---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__i3c__target__device.html
original_path: doxygen/html/group__i3c__target__device.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I3C Target Device API

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

I3C Target Device API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [i3c\_config\_target](structi3c__config__target.md) |
|  | Configuration parameters for I3C hardware to act as target device. [More...](structi3c__config__target.md#details) |
| struct | [i3c\_target\_config](structi3c__target__config.md) |
|  | Structure describing a device that supports the I3C target API. [More...](structi3c__target__config.md#details) |
| struct | [i3c\_target\_callbacks](structi3c__target__callbacks.md) |
| struct | [i3c\_target\_driver\_api](structi3c__target__driver__api.md) |

| Functions | |
| --- | --- |
| static int | [i3c\_target\_tx\_write](#gafb5ebdfd5536ee265a3719beb8ae81dc) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hdr\_mode) |
|  | Writes to the target's TX FIFO. |
| static int | [i3c\_target\_register](#gaf13d2b84a91e17d5ec49a41e9c553d42) (const struct [device](structdevice.md) \*dev, struct [i3c\_target\_config](structi3c__target__config.md) \*cfg) |
|  | Registers the provided config as target device of a controller. |
| static int | [i3c\_target\_unregister](#ga3dc0e6451fb13fa063c5ec3e18fe22e4) (const struct [device](structdevice.md) \*dev, struct [i3c\_target\_config](structi3c__target__config.md) \*cfg) |
|  | Unregisters the provided config as target device. |

## Detailed Description

I3C Target Device API.

## Function Documentation

## [◆ ](#gaf13d2b84a91e17d5ec49a41e9c553d42)i3c\_target\_register()

| | int i3c\_target\_register | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i3c\_target\_config](structi3c__target__config.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[target_device.h](target__device_8h.md)>`

Registers the provided config as target device of a controller.

Enable I3C target mode for the `dev` I3C bus driver using the provided config struct (`cfg`) containing the functions and parameters to send bus events. The I3C target will be registered at the address provided as [i3c\_target\_config::address](structi3c__target__config.md#a89b7f8bd52beec7dd733ab6dd1111758 "i3c_target_config::address") struct member. Any I3C bus events related to the target mode will be passed onto I3C target device driver via a set of callback functions provided in the 'callbacks' struct member.

Most of the existing hardware allows simultaneous support for master and target mode. This is however not guaranteed.

Parameters
:   | dev | Pointer to the device structure for an I3C controller driver configured in target mode. |
    | --- | --- |
    | cfg | Config struct with functions and parameters used by the I3C target driver to send bus events |

Return values
:   | 0 | Is successful |
    | --- | --- |
    | -EINVAL | If parameters are invalid |
    | -EIO | General input / output error. |
    | -ENOSYS | If target mode is not implemented |

## [◆ ](#gafb5ebdfd5536ee265a3719beb8ae81dc)i3c\_target\_tx\_write()

| | int i3c\_target\_tx\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *hdr\_mode* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[target_device.h](target__device_8h.md)>`

Writes to the target's TX FIFO.

Write to the TX FIFO `dev` I3C bus driver using the provided buffer and length. Some I3C targets will NACK read requests until data is written to the TX FIFO. This function will write as much as it can to the FIFO return the total number of bytes written. It is then up to the application to utalize the target callbacks to write the remaining data. Negative returns indicate error.

Most of the existing hardware allows simultaneous support for master and target mode. This is however not guaranteed.

Parameters
:   | dev | Pointer to the device structure for an I3C controller driver configured in target mode. |
    | --- | --- |
    | buf | Pointer to the buffer |
    | len | Length of the buffer |
    | hdr\_mode | HDR mode see `I3C_MSG_HDR_MODE*` |

Return values
:   | Total | number of bytes written |
    | --- | --- |
    | -ENOTSUP | Not in Target Mode or HDR Mode not supported |
    | -ENOSPC | No space in Tx FIFO |
    | -ENOSYS | If target mode is not implemented |

## [◆ ](#ga3dc0e6451fb13fa063c5ec3e18fe22e4)i3c\_target\_unregister()

| | int i3c\_target\_unregister | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [i3c\_target\_config](structi3c__target__config.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[target_device.h](target__device_8h.md)>`

Unregisters the provided config as target device.

This routine disables I3C target mode for the `dev` I3C bus driver using the provided config struct (`cfg`) containing the functions and parameters to send bus events.

Parameters
:   | dev | Pointer to the device structure for an I3C controller driver configured in target mode. |
    | --- | --- |
    | cfg | Config struct with functions and parameters used by the I3C target driver to send bus events |

Return values
:   | 0 | Is successful |
    | --- | --- |
    | -EINVAL | If parameters are invalid |
    | -ENOSYS | If target mode is not implemented |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
