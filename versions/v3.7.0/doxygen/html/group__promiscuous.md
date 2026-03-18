---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__promiscuous.html
original_path: doxygen/html/group__promiscuous.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Promiscuous mode

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Promiscuous mode support.
[More...](#details)

| Functions | |
| --- | --- |
| static struct [net\_pkt](structnet__pkt.md) \* | [net\_promisc\_mode\_wait\_data](#ga2fc01f791b635c54e85346cf898b324e) ([k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Start to wait received network packets. |
| static int | [net\_promisc\_mode\_on](#gac1a4b50b547d0f4b9396d71eecafd926) (struct [net\_if](structnet__if.md) \*iface) |
|  | Enable promiscuous mode for a given network interface. |
| static int | [net\_promisc\_mode\_off](#ga089aebe5ce5b6ffc48b485d361bf9e7a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Disable promiscuous mode for a given network interface. |

## Detailed Description

Promiscuous mode support.

## Function Documentation

## [◆ ](#ga089aebe5ce5b6ffc48b485d361bf9e7a)net\_promisc\_mode\_off()

| | int net\_promisc\_mode\_off | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[promiscuous.h](promiscuous_8h.md)>`

Disable promiscuous mode for a given network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   0 if ok, <0 if error

## [◆ ](#gac1a4b50b547d0f4b9396d71eecafd926)net\_promisc\_mode\_on()

| | int net\_promisc\_mode\_on | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[promiscuous.h](promiscuous_8h.md)>`

Enable promiscuous mode for a given network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga2fc01f791b635c54e85346cf898b324e)net\_promisc\_mode\_wait\_data()

| | struct [net\_pkt](structnet__pkt.md) \* net\_promisc\_mode\_wait\_data | ( | [k\_timeout\_t](structk__timeout__t.md) | *timeout* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[promiscuous.h](promiscuous_8h.md)>`

Start to wait received network packets.

Parameters
:   | timeout | How long to wait before returning. |
    | --- | --- |

Returns
:   Received [net\_pkt](structnet__pkt.md "Network packet."), NULL if not received any packet.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
