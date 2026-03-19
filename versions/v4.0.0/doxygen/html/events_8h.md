---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/events_8h.html
original_path: doxygen/html/events_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

events.h File Reference

`#include <[zephyr/xen/public/event_channel.h](event__channel_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](events_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [event\_channel\_handle](structevent__channel__handle.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [evtchn\_cb\_t](#a1e631dcb6d0ab84d2b63cced85f28d47)) (void \*priv) |
| typedef struct [event\_channel\_handle](structevent__channel__handle.md) | [evtchn\_handle\_t](#a057cac7f834e8352d4b8b48d5ae22fcb) |

| Functions | |
| --- | --- |
| int | [evtchn\_status](#ae5391f2b67ddbd598f33d796ba591568) ([evtchn\_status\_t](event__channel_8h.md#a8ed9ed5019e8da76a67eaddc44c3f6a9) \*status) |
| int | [evtchn\_close](#abed06147ec0c0f9650ac7348a04ee430) ([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port) |
| int | [evtchn\_set\_priority](#a761efce6eab19f91b33391d4bf516fff) ([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) priority) |
| void | [notify\_evtchn](#a050856eda5a9c15075b3bc5314658d3a) ([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port) |
| int | [alloc\_unbound\_event\_channel](#a46ba842a0e4f518d03683253d35b7126) ([domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) remote\_dom) |
| int | [bind\_interdomain\_event\_channel](#adc0a69c0205307e86458ada50aa0302d) ([domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) remote\_dom, [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) remote\_port, [evtchn\_cb\_t](#a1e631dcb6d0ab84d2b63cced85f28d47) cb, void \*data) |
| int | [bind\_event\_channel](#a74e60b33dd93a62835e86b251a9cd43c) ([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port, [evtchn\_cb\_t](#a1e631dcb6d0ab84d2b63cced85f28d47) cb, void \*data) |
| int | [unbind\_event\_channel](#abad4417540bf329eca43842bf83549e9) ([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port) |
| int | [get\_missed\_events](#a2ac07d6eff7d3406716917578b5f7daf) ([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) port) |
| int | [xen\_events\_init](#af6542be4472fb2d1dc17deca6c323972) (void) |

## Typedef Documentation

## [◆ ](#a1e631dcb6d0ab84d2b63cced85f28d47)evtchn\_cb\_t

| typedef void(\* evtchn\_cb\_t) (void \*priv) |
| --- |

## [◆ ](#a057cac7f834e8352d4b8b48d5ae22fcb)evtchn\_handle\_t

| typedef struct [event\_channel\_handle](structevent__channel__handle.md) [evtchn\_handle\_t](#a057cac7f834e8352d4b8b48d5ae22fcb) |
| --- |

## Function Documentation

## [◆ ](#a46ba842a0e4f518d03683253d35b7126)alloc\_unbound\_event\_channel()

| int alloc\_unbound\_event\_channel | ( | [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | *remote\_dom* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a74e60b33dd93a62835e86b251a9cd43c)bind\_event\_channel()

| int bind\_event\_channel | ( | [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) | *port*, |
| --- | --- | --- | --- |
|  |  | [evtchn\_cb\_t](#a1e631dcb6d0ab84d2b63cced85f28d47) | *cb*, |
|  |  | void \* | *data* ) |

## [◆ ](#adc0a69c0205307e86458ada50aa0302d)bind\_interdomain\_event\_channel()

| int bind\_interdomain\_event\_channel | ( | [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | *remote\_dom*, |
| --- | --- | --- | --- |
|  |  | [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) | *remote\_port*, |
|  |  | [evtchn\_cb\_t](#a1e631dcb6d0ab84d2b63cced85f28d47) | *cb*, |
|  |  | void \* | *data* ) |

## [◆ ](#abed06147ec0c0f9650ac7348a04ee430)evtchn\_close()

| int evtchn\_close | ( | [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) | *port* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a761efce6eab19f91b33391d4bf516fff)evtchn\_set\_priority()

| int evtchn\_set\_priority | ( | [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) | *port*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *priority* ) |

## [◆ ](#ae5391f2b67ddbd598f33d796ba591568)evtchn\_status()

| int evtchn\_status | ( | [evtchn\_status\_t](event__channel_8h.md#a8ed9ed5019e8da76a67eaddc44c3f6a9) \* | *status* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a2ac07d6eff7d3406716917578b5f7daf)get\_missed\_events()

| int get\_missed\_events | ( | [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) | *port* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a050856eda5a9c15075b3bc5314658d3a)notify\_evtchn()

| void notify\_evtchn | ( | [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) | *port* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#abad4417540bf329eca43842bf83549e9)unbind\_event\_channel()

| int unbind\_event\_channel | ( | [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) | *port* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#af6542be4472fb2d1dc17deca6c323972)xen\_events\_init()

| int xen\_events\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [events.h](events_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
