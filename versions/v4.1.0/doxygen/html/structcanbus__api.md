---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcanbus__api.html
original_path: doxygen/html/structcanbus__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

canbus\_api Struct Reference

CAN L2 network driver API.
[More...](#details)

`#include <[canbus.h](canbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct net\_if\_api | [iface\_api](#af8f809bf252a5d261209af2b7b3096f7) |
|  | The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API. |
| int(\* | [send](#a31fee4b60f4ab2f832e0599c23337b6c) )(const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send a CAN packet by socket. |
| void(\* | [close](#abff03e6144170f8f223e11a7f28b59b7) )(const struct [device](structdevice.md) \*dev, int filter\_id) |
|  | Close the related CAN socket. |
| int(\* | [setsockopt](#aad0cbe71d16cec3c99c812ab324e5382) )(const struct [device](structdevice.md) \*dev, void \*obj, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen) |
|  | Set socket CAN option. |
| int(\* | [getsockopt](#a0d61e7052367475a10b8c72461f7361f) )(const struct [device](structdevice.md) \*dev, void \*obj, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen) |
|  | Get socket CAN option. |

## Detailed Description

CAN L2 network driver API.

## Field Documentation

## [◆ ](#abff03e6144170f8f223e11a7f28b59b7)close

| void(\* canbus\_api::close) (const struct [device](structdevice.md) \*dev, int filter\_id) |
| --- |

Close the related CAN socket.

## [◆ ](#a0d61e7052367475a10b8c72461f7361f)getsockopt

| int(\* canbus\_api::getsockopt) (const struct [device](structdevice.md) \*dev, void \*obj, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen) |
| --- |

Get socket CAN option.

## [◆ ](#af8f809bf252a5d261209af2b7b3096f7)iface\_api

| struct net\_if\_api canbus\_api::iface\_api |
| --- |

The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API.

## [◆ ](#a31fee4b60f4ab2f832e0599c23337b6c)send

| int(\* canbus\_api::send) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

Send a CAN packet by socket.

## [◆ ](#aad0cbe71d16cec3c99c812ab324e5382)setsockopt

| int(\* canbus\_api::setsockopt) (const struct [device](structdevice.md) \*dev, void \*obj, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen) |
| --- |

Set socket CAN option.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[canbus.h](canbus_8h_source.md)

- [canbus\_api](structcanbus__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
