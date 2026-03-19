---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__net__capture.html
original_path: doxygen/html/group__net__capture.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network packet capture

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network packet capture support functions.
[More...](#details)

| Functions | |
| --- | --- |
| int | [net\_capture\_setup](#gab280c0c6cc607bdb07211a9450eae262) (const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr, const struct [device](structdevice.md) \*\*dev) |
|  | Setup network packet capturing support. |
| static int | [net\_capture\_cleanup](#ga7a56719068938c34c9c6149296074d01) (const struct [device](structdevice.md) \*dev) |
|  | Cleanup network packet capturing support. |
| static int | [net\_capture\_enable](#gaf449c308080dc126e2e7c03b38d2a0aa) (const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface) |
|  | Enable network packet capturing support. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_capture\_is\_enabled](#ga651987b8b1e713865cff01412934f3cc) (const struct [device](structdevice.md) \*dev) |
|  | Is network packet capture enabled or disabled. |
| static int | [net\_capture\_disable](#ga32c66260fc888dcd38b6a3cffca3b951) (const struct [device](structdevice.md) \*dev) |
|  | Disable network packet capturing support. |

## Detailed Description

Network packet capture support functions.

Since
:   2.6

Version
:   0.8.0

## Function Documentation

## [◆ ](#ga7a56719068938c34c9c6149296074d01)net\_capture\_cleanup()

| | int net\_capture\_cleanup | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[capture.h](capture_8h.md)>`

Cleanup network packet capturing support.

This should be called after the capturing is done and resources can be released.

Parameters
:   | dev | Network capture device. User must allocate using the [net\_capture\_setup()](#gab280c0c6cc607bdb07211a9450eae262) function. |
    | --- | --- |

Returns
:   0 if ok, <0 if network packet capture cleanup failed

## [◆ ](#ga32c66260fc888dcd38b6a3cffca3b951)net\_capture\_disable()

| | int net\_capture\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[capture.h](capture_8h.md)>`

Disable network packet capturing support.

Parameters
:   | dev | Network capture device |
    | --- | --- |

Returns
:   0 if ok, <0 if network packet capture disable failed

## [◆ ](#gaf449c308080dc126e2e7c03b38d2a0aa)net\_capture\_enable()

| | int net\_capture\_enable | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [net\_if](structnet__if.md) \* | *iface* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[capture.h](capture_8h.md)>`

Enable network packet capturing support.

This creates tunnel network interface where all the captured packets are pushed. The captured network packets are placed in UDP packets that are sent to tunnel peer.

Parameters
:   | dev | Network capture device |
    | --- | --- |
    | iface | Network interface we are starting to capture packets. |

Returns
:   0 if ok, <0 if network packet capture enable failed

## [◆ ](#ga651987b8b1e713865cff01412934f3cc)net\_capture\_is\_enabled()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_capture\_is\_enabled | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[capture.h](capture_8h.md)>`

Is network packet capture enabled or disabled.

Parameters
:   | dev | Network capture device. If set to NULL, then the default capture device is used. |
    | --- | --- |

Returns
:   True if enabled, False if network capture is disabled.

## [◆ ](#gab280c0c6cc607bdb07211a9450eae262)net\_capture\_setup()

| int net\_capture\_setup | ( | const char \* | *remote\_addr*, |
| --- | --- | --- | --- |
|  |  | const char \* | *my\_local\_addr*, |
|  |  | const char \* | *peer\_addr*, |
|  |  | const struct [device](structdevice.md) \*\* | *dev* ) |

`#include <[capture.h](capture_8h.md)>`

Setup network packet capturing support.

Parameters
:   | remote\_addr | The value tells the tunnel remote/outer endpoint IP address. The IP address can be either IPv4 or IPv6 address. This address is used to select the network interface where the tunnel is created. |
    | --- | --- |
    | my\_local\_addr | The local/inner IP address of the tunnel. Can contain also port number which is used as UDP source port. |
    | peer\_addr | The peer/inner IP address of the tunnel. Can contain also port number which is used as UDP destination port. |
    | dev | Network capture device. This is returned to the caller. |

Returns
:   0 if ok, <0 if network packet capture setup failed

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
