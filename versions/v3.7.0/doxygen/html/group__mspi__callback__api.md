---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mspi__callback__api.html
original_path: doxygen/html/group__mspi__callback__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MSPI callback API

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md)

MSPI callback API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mspi\_event\_data](structmspi__event__data.md) |
|  | MSPI event data. [More...](structmspi__event__data.md#details) |
| struct | [mspi\_event](structmspi__event.md) |
|  | MSPI event. [More...](structmspi__event.md#details) |
| struct | [mspi\_callback\_context](structmspi__callback__context.md) |
|  | MSPI callback context. [More...](structmspi__callback__context.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mspi\_callback\_handler\_t](#ga29421f748fdb89c823e1a48ff69cf0f4)) (struct [mspi\_callback\_context](structmspi__callback__context.md) \*mspi\_cb\_ctx,...) |
|  | Define the application callback handler function signature. |

| Functions | |
| --- | --- |
| static int | [mspi\_register\_callback](#ga967f5fed63f08ac2d5a88625b030cd14) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type, [mspi\_callback\_handler\_t](#ga29421f748fdb89c823e1a48ff69cf0f4) cb, struct [mspi\_callback\_context](structmspi__callback__context.md) \*ctx) |
|  | Register the mspi callback functions. |

## Detailed Description

MSPI callback API.

## Typedef Documentation

## [◆ ](#ga29421f748fdb89c823e1a48ff69cf0f4)mspi\_callback\_handler\_t

| typedef void(\* mspi\_callback\_handler\_t) (struct [mspi\_callback\_context](structmspi__callback__context.md) \*mspi\_cb\_ctx,...) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

Define the application callback handler function signature.

Parameters
:   | mspi\_cb\_ctx | Pointer to the MSPI callback context |
    | --- | --- |

## Function Documentation

## [◆ ](#ga967f5fed63f08ac2d5a88625b030cd14)mspi\_register\_callback()

| | int mspi\_register\_callback | ( | const struct [device](structdevice.md) \* | *controller*, | | --- | --- | --- | --- | |  |  | const struct [mspi\_dev\_id](structmspi__dev__id.md) \* | *dev\_id*, | |  |  | const enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) | *evt\_type*, | |  |  | [mspi\_callback\_handler\_t](#ga29421f748fdb89c823e1a48ff69cf0f4) | *cb*, | |  |  | struct [mspi\_callback\_context](structmspi__callback__context.md) \* | *ctx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mspi.h](mspi_8h.md)>`

Register the mspi callback functions.

This routines provides a generic interface to register mspi callback functions. In generally it should be called before mspi\_transceive.

Parameters
:   | controller | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dev\_id | Pointer to the device ID structure from a device. |
    | evt\_type | The event type associated the callback. |
    | cb | Pointer to the user implemented callback function. |
    | ctx | Pointer to the callback context. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP |  |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
