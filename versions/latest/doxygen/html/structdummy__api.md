---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structdummy__api.html
original_path: doxygen/html/structdummy__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dummy\_api Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Dummy L2/driver Support Functions](group__dummy.md)

`#include <[dummy.h](dummy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_if\_api | [iface\_api](#ade5d5f20076909da1e9ea7a819192cf1) |
|  | The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API. |
| int(\* | [send](#a3a6110e3de2300931ac5e0aeabbd7311) )(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send a network packet. |
| int(\* | [start](#a9f535aaf72c9e6781cceffdd019b3f85) )(const struct [device](structdevice.md) \*dev) |
|  | Start the device. |
| int(\* | [stop](#a092fe1f0d12b091dad21e6dd7c717aa3) )(const struct [device](structdevice.md) \*dev) |
|  | Stop the device. |

## Field Documentation

## [◆ ](#ade5d5f20076909da1e9ea7a819192cf1)iface\_api

| struct net\_if\_api dummy\_api::iface\_api |
| --- |

The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API.

## [◆ ](#a3a6110e3de2300931ac5e0aeabbd7311)send

| int(\* dummy\_api::send) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

Send a network packet.

## [◆ ](#a9f535aaf72c9e6781cceffdd019b3f85)start

| int(\* dummy\_api::start) (const struct [device](structdevice.md) \*dev) |
| --- |

Start the device.

Called when the bound network interface is brought up.

## [◆ ](#a092fe1f0d12b091dad21e6dd7c717aa3)stop

| int(\* dummy\_api::stop) (const struct [device](structdevice.md) \*dev) |
| --- |

Stop the device.

Called when the bound network interface is taken down.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dummy.h](dummy_8h_source.md)

- [dummy\_api](structdummy__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
