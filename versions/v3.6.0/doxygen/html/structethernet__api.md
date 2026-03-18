---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structethernet__api.html
original_path: doxygen/html/structethernet__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_api Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_if\_api | [iface\_api](#a03dfbaed9cdf2bdd17b0bfd28d5a1056) |
|  | The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API. |
| int(\* | [start](#a2abe87be47f265a6d5b3e7b598682da1) )(const struct [device](structdevice.md) \*dev) |
|  | Start the device. |
| int(\* | [stop](#a819599fe26b90860147ccfa86f337f84) )(const struct [device](structdevice.md) \*dev) |
|  | Stop the device. |
| enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5)(\* | [get\_capabilities](#a8731846f9bd07398b2f5c154c6ec0fe3) )(const struct [device](structdevice.md) \*dev) |
|  | Get the device capabilities. |
| int(\* | [set\_config](#ae204fdf7e8c72fdea3dee67a7068afe1) )(const struct [device](structdevice.md) \*dev, enum ethernet\_config\_type type, const struct ethernet\_config \*config) |
|  | Set specific hardware configuration. |
| int(\* | [get\_config](#a3f71e6bf922b91289efa3ac97df70e81) )(const struct [device](structdevice.md) \*dev, enum ethernet\_config\_type type, struct ethernet\_config \*config) |
|  | Get hardware specific configuration. |
| int(\* | [send](#a8f6fd0d640b5a883c9f5150d9ed71241) )(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send a network packet. |

## Field Documentation

## [◆ ](#a8731846f9bd07398b2f5c154c6ec0fe3)get\_capabilities

| enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5)(\* ethernet\_api::get\_capabilities) (const struct [device](structdevice.md) \*dev) |
| --- |

Get the device capabilities.

## [◆ ](#a3f71e6bf922b91289efa3ac97df70e81)get\_config

| int(\* ethernet\_api::get\_config) (const struct [device](structdevice.md) \*dev, enum ethernet\_config\_type type, struct ethernet\_config \*config) |
| --- |

Get hardware specific configuration.

## [◆ ](#a03dfbaed9cdf2bdd17b0bfd28d5a1056)iface\_api

| struct net\_if\_api ethernet\_api::iface\_api |
| --- |

The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API.

## [◆ ](#a8f6fd0d640b5a883c9f5150d9ed71241)send

| int(\* ethernet\_api::send) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

Send a network packet.

## [◆ ](#ae204fdf7e8c72fdea3dee67a7068afe1)set\_config

| int(\* ethernet\_api::set\_config) (const struct [device](structdevice.md) \*dev, enum ethernet\_config\_type type, const struct ethernet\_config \*config) |
| --- |

Set specific hardware configuration.

## [◆ ](#a2abe87be47f265a6d5b3e7b598682da1)start

| int(\* ethernet\_api::start) (const struct [device](structdevice.md) \*dev) |
| --- |

Start the device.

## [◆ ](#a819599fe26b90860147ccfa86f337f84)stop

| int(\* ethernet\_api::stop) (const struct [device](structdevice.md) \*dev) |
| --- |

Stop the device.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_api](structethernet__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
