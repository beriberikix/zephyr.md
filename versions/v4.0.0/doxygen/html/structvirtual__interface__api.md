---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structvirtual__interface__api.html
original_path: doxygen/html/structvirtual__interface__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtual\_interface\_api Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Virtual Network Interface Support Functions](group__virtual.md)

Virtual L2 API operations.
[More...](#details)

`#include <[virtual.h](virtual_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_if\_api | [iface\_api](#aee1250773938536ab28e129113073ae7) |
|  | The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API. |
| enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091)(\* | [get\_capabilities](#a827cd13d885b7cc2f80eddd73e438e07) )(struct [net\_if](structnet__if.md) \*iface) |
|  | Get the virtual interface capabilities. |
| int(\* | [start](#af28a6ed36799006d185fab9129c6c120) )(const struct [device](structdevice.md) \*dev) |
|  | Start the device. |
| int(\* | [stop](#a09a317009d31ac5e9340c3ca7d2191c4) )(const struct [device](structdevice.md) \*dev) |
|  | Stop the device. |
| int(\* | [send](#a6fbfa013374bbafaa610b0a054d3a415) )(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send a network packet. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* | [recv](#a6f21e33e39caa00d51cca900a26f7070) )(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Receive a network packet. |
| int(\* | [attach](#a753258a8929347877997ca5d6a76eb8c) )(struct [net\_if](structnet__if.md) \*virtual\_iface, struct [net\_if](structnet__if.md) \*iface) |
|  | Pass the attachment information to virtual interface. |
| int(\* | [set\_config](#a591f1b7df5313c4a225dceaa04b1eeae) )(struct [net\_if](structnet__if.md) \*iface, enum virtual\_interface\_config\_type type, const struct virtual\_interface\_config \*config) |
|  | Set specific L2 configuration. |
| int(\* | [get\_config](#a4ff5b92897926616778eb6fb696ebb16) )(struct [net\_if](structnet__if.md) \*iface, enum virtual\_interface\_config\_type type, struct virtual\_interface\_config \*config) |
|  | Get specific L2 configuration. |

## Detailed Description

Virtual L2 API operations.

## Field Documentation

## [◆ ](#a753258a8929347877997ca5d6a76eb8c)attach

| int(\* virtual\_interface\_api::attach) (struct [net\_if](structnet__if.md) \*virtual\_iface, struct [net\_if](structnet__if.md) \*iface) |
| --- |

Pass the attachment information to virtual interface.

## [◆ ](#a827cd13d885b7cc2f80eddd73e438e07)get\_capabilities

| enum [virtual\_interface\_caps](group__virtual.md#ga8f188f5c2f19960d7113da52aefe8091)(\* virtual\_interface\_api::get\_capabilities) (struct [net\_if](structnet__if.md) \*iface) |
| --- |

Get the virtual interface capabilities.

## [◆ ](#a4ff5b92897926616778eb6fb696ebb16)get\_config

| int(\* virtual\_interface\_api::get\_config) (struct [net\_if](structnet__if.md) \*iface, enum virtual\_interface\_config\_type type, struct virtual\_interface\_config \*config) |
| --- |

Get specific L2 configuration.

## [◆ ](#aee1250773938536ab28e129113073ae7)iface\_api

| struct net\_if\_api virtual\_interface\_api::iface\_api |
| --- |

The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API.

## [◆ ](#a6f21e33e39caa00d51cca900a26f7070)recv

| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* virtual\_interface\_api::recv) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

Receive a network packet.

The callback returns NET\_OK if this interface will accept the packet and pass it upper layers, NET\_DROP if the packet is to be dropped and NET\_CONTINUE to pass it to next interface.

## [◆ ](#a6fbfa013374bbafaa610b0a054d3a415)send

| int(\* virtual\_interface\_api::send) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

Send a network packet.

## [◆ ](#a591f1b7df5313c4a225dceaa04b1eeae)set\_config

| int(\* virtual\_interface\_api::set\_config) (struct [net\_if](structnet__if.md) \*iface, enum virtual\_interface\_config\_type type, const struct virtual\_interface\_config \*config) |
| --- |

Set specific L2 configuration.

## [◆ ](#af28a6ed36799006d185fab9129c6c120)start

| int(\* virtual\_interface\_api::start) (const struct [device](structdevice.md) \*dev) |
| --- |

Start the device.

## [◆ ](#a09a317009d31ac5e9340c3ca7d2191c4)stop

| int(\* virtual\_interface\_api::stop) (const struct [device](structdevice.md) \*dev) |
| --- |

Stop the device.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[virtual.h](virtual_8h_source.md)

- [virtual\_interface\_api](structvirtual__interface__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
