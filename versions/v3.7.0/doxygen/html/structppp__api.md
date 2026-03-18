---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structppp__api.html
original_path: doxygen/html/structppp__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ppp\_api Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [PPP L2/driver Support Functions](group__ppp.md)

PPP L2 API.
[More...](#details)

`#include <[ppp.h](net_2ppp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_if\_api | [iface\_api](#acc4e82fbaa8b933040b0a77da8a3cae0) |
|  | The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API. |
| int(\* | [start](#ab85010475c4f03a48ad7629ed4947626) )(const struct [device](structdevice.md) \*dev) |
|  | Start the device. |
| int(\* | [stop](#a42576f1d58920f48a0d0adf888f99006) )(const struct [device](structdevice.md) \*dev) |
|  | Stop the device. |
| int(\* | [send](#aa0ec35e57f22674ef06f8cc3bc09987f) )(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send a network packet. |

## Detailed Description

PPP L2 API.

## Field Documentation

## [◆ ](#acc4e82fbaa8b933040b0a77da8a3cae0)iface\_api

| struct net\_if\_api ppp\_api::iface\_api |
| --- |

The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API.

## [◆ ](#aa0ec35e57f22674ef06f8cc3bc09987f)send

| int(\* ppp\_api::send) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

Send a network packet.

## [◆ ](#ab85010475c4f03a48ad7629ed4947626)start

| int(\* ppp\_api::start) (const struct [device](structdevice.md) \*dev) |
| --- |

Start the device.

## [◆ ](#a42576f1d58920f48a0d0adf888f99006)stop

| int(\* ppp\_api::stop) (const struct [device](structdevice.md) \*dev) |
| --- |

Stop the device.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ppp.h](net_2ppp_8h_source.md)

- [ppp\_api](structppp__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
