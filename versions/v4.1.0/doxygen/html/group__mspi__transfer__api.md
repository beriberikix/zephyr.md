---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mspi__transfer__api.html
original_path: doxygen/html/group__mspi__transfer__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MSPI Transfer API

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md)

MSPI Transfer API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mspi\_ce\_control](structmspi__ce__control.md) |
|  | MSPI Chip Select control structure. [More...](structmspi__ce__control.md#details) |
| struct | [mspi\_xfer\_packet](structmspi__xfer__packet.md) |
|  | MSPI peripheral xfer packet format. [More...](structmspi__xfer__packet.md#details) |
| struct | [mspi\_xfer](structmspi__xfer.md) |
|  | MSPI peripheral xfer format This includes transfer related settings that may require configuring the hardware. [More...](structmspi__xfer.md#details) |

| Functions | |
| --- | --- |
| int | [mspi\_transceive](#ga8c98c73e322c575b759ce911cc115129) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xfer](structmspi__xfer.md) \*req) |
|  | Transfer request over MSPI. |

## Detailed Description

MSPI Transfer API.

## Function Documentation

## [◆ ](#ga8c98c73e322c575b759ce911cc115129)mspi\_transceive()

| int mspi\_transceive | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | const struct [mspi\_dev\_id](structmspi__dev__id.md) \* | *dev\_id*, |
|  |  | const struct [mspi\_xfer](structmspi__xfer.md) \* | *req* ) |

`#include <[mspi.h](mspi_8h.md)>`

Transfer request over MSPI.

This routines provides a generic interface to transfer a request synchronously/asynchronously.

The

See also
:   [mspi\_xfer](structmspi__xfer.md "MSPI peripheral xfer format This includes transfer related settings that may require configuring the ...") allows for dynamically changing the transfer related [Settings](group__settings.md) once the mode of operation is determined and configured. The API supports bulk transfers with different starting addresses and sizes with
:   [mspi\_xfer\_packet](structmspi__xfer__packet.md "MSPI peripheral xfer packet format."). However, it is up to the controller implementation whether to support scatter IO and callback management. The controller can determine which user callback to trigger based on
:   [mspi\_bus\_event\_cb\_mask](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1 "MSPI bus event callback mask This is a preliminary list same as mspi_bus_event.") upon completion of each async/sync transfer if the callback had been registered. Or not to trigger any callback at all with [MSPI\_BUS\_NO\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277) even if the callbacks are already registered.

Parameters
:   | controller | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dev\_id | Pointer to the device ID structure from a device. |
    | req | Content of the request and request specific settings. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP |  |
    | -EIO | General input / output error, failed to send over the bus. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
