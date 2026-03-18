---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__net__config.html
original_path: doxygen/html/group__net__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Configuration Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network configuration library.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [NET\_CONFIG\_NEED\_ROUTER](#ga5c1a321477ce072a964bc610aef805f1)   0x00000001 |
|  | Application needs routers to be set so that connectivity to remote network is possible. |
| #define | [NET\_CONFIG\_NEED\_IPV6](#ga469731c167f97b5df40b51ee0c87313c)   0x00000002 |
|  | Application needs IPv6 subsystem configured and initialized. |
| #define | [NET\_CONFIG\_NEED\_IPV4](#ga4312efaa62093c93968c0ae81efc36dd)   0x00000004 |
|  | Application needs IPv4 subsystem configured and initialized. |

| Functions | |
| --- | --- |
| int | [net\_config\_init](#ga02a2b4fbac3eba68a175630293c91484) (const char \*app\_info, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Initialize this network application. |
| int | [net\_config\_init\_by\_iface](#gab19ec1b3411f38d9bee5abcb25926ea0) (struct [net\_if](structnet__if.md) \*iface, const char \*app\_info, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Initialize this network application using a specific network interface. |
| int | [net\_config\_init\_app](#ga49c6b4cd9d338f1b3d76225a9872c84c) (const struct [device](structdevice.md) \*dev, const char \*app\_info) |
|  | Initialize this network application. |

## Detailed Description

Network configuration library.

## Macro Definition Documentation

## [◆ ](#ga4312efaa62093c93968c0ae81efc36dd)NET\_CONFIG\_NEED\_IPV4

| #define NET\_CONFIG\_NEED\_IPV4   0x00000004 |
| --- |

`#include <[net_config.h](net__config_8h.md)>`

Application needs IPv4 subsystem configured and initialized.

Typically this means that the device has IPv4 address set.

## [◆ ](#ga469731c167f97b5df40b51ee0c87313c)NET\_CONFIG\_NEED\_IPV6

| #define NET\_CONFIG\_NEED\_IPV6   0x00000002 |
| --- |

`#include <[net_config.h](net__config_8h.md)>`

Application needs IPv6 subsystem configured and initialized.

Typically this means that the device has IPv6 address set.

## [◆ ](#ga5c1a321477ce072a964bc610aef805f1)NET\_CONFIG\_NEED\_ROUTER

| #define NET\_CONFIG\_NEED\_ROUTER   0x00000001 |
| --- |

`#include <[net_config.h](net__config_8h.md)>`

Application needs routers to be set so that connectivity to remote network is possible.

For IPv6 networks, this means that the device should receive IPv6 router advertisement message before continuing.

## Function Documentation

## [◆ ](#ga02a2b4fbac3eba68a175630293c91484)net\_config\_init()

| int net\_config\_init | ( | const char \* | *app\_info*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[net_config.h](net__config_8h.md)>`

Initialize this network application.

This will call [net\_config\_init\_by\_iface()](#gab19ec1b3411f38d9bee5abcb25926ea0) with NULL network interface.

Parameters
:   | app\_info | String describing this application. |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags related to services needed by the client. |
    | timeout | How long to wait the network setup before continuing the startup. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#ga49c6b4cd9d338f1b3d76225a9872c84c)net\_config\_init\_app()

| int net\_config\_init\_app | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const char \* | *app\_info* ) |

`#include <[net_config.h](net__config_8h.md)>`

Initialize this network application.

If CONFIG\_NET\_CONFIG\_AUTO\_INIT is set, then this function is called automatically when the device boots. If that is not desired, unset the config option and call the function manually when the application starts.

Parameters
:   | dev | Network device to use. The function will figure out what network interface to use based on the device. If the device is NULL, then default network interface is used by the function. |
    | --- | --- |
    | app\_info | String describing this application. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#gab19ec1b3411f38d9bee5abcb25926ea0)net\_config\_init\_by\_iface()

| int net\_config\_init\_by\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const char \* | *app\_info*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) |

`#include <[net_config.h](net__config_8h.md)>`

Initialize this network application using a specific network interface.

If network interface is set to NULL, then the default one is used in the configuration.

Parameters
:   | iface | Initialize networking using this network interface. |
    | --- | --- |
    | app\_info | String describing this application. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags related to services needed by the client. |
    | timeout | How long to wait the network setup before continuing the startup. |

Returns
:   0 if ok, <0 if error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
