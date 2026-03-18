---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cdc__acm_8h.html
original_path: doxygen/html/cdc__acm_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdc\_acm.h File Reference

Public APIs for the CDC ACM class driver.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](cdc__acm_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [cdc\_dte\_rate\_callback\_t](#a0b2e4a171e5d56dba45c3d2e7cef72b4)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rate) |
|  | A function that is called when the USB host changes the baud rate. |

| Functions | |
| --- | --- |
| int | [cdc\_acm\_dte\_rate\_callback\_set](#a5b71bd70532ed059fb31a1ee3e73eaa5) (const struct [device](structdevice.md) \*dev, [cdc\_dte\_rate\_callback\_t](#a0b2e4a171e5d56dba45c3d2e7cef72b4) callback) |
|  | Set the callback for dwDTERate SetLineCoding requests. |

## Detailed Description

Public APIs for the CDC ACM class driver.

## Typedef Documentation

## [◆ ](#a0b2e4a171e5d56dba45c3d2e7cef72b4)cdc\_dte\_rate\_callback\_t

| typedef void(\* cdc\_dte\_rate\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rate) |
| --- |

A function that is called when the USB host changes the baud rate.

Parameters
:   | dev | Device struct for the CDC ACM device. |
    | --- | --- |
    | rate | New USB baud rate |

## Function Documentation

## [◆ ](#a5b71bd70532ed059fb31a1ee3e73eaa5)cdc\_acm\_dte\_rate\_callback\_set()

| int cdc\_acm\_dte\_rate\_callback\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [cdc\_dte\_rate\_callback\_t](#a0b2e4a171e5d56dba45c3d2e7cef72b4) | *callback* ) |

Set the callback for dwDTERate SetLineCoding requests.

The callback is invoked when the USB host changes the baud rate.

Note
:   This function is available only when CONFIG\_CDC\_ACM\_DTE\_RATE\_CALLBACK\_SUPPORT is enabled.

Parameters
:   | dev | CDC ACM device structure. |
    | --- | --- |
    | callback | Event handler. |

Returns
:   0 on success.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart](dir_eceb547fc512cd90b0f2ab20ab1dbc9a.md)
- [cdc\_acm.h](cdc__acm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
