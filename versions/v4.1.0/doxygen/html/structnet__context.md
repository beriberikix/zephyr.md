---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__context.html
original_path: doxygen/html/structnet__context.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_context Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Application network context](group__net__context.md)

Note that we do not store the actual source IP address in the context because the address is already set in the network interface struct.
[More...](#details)

`#include <[net_context.h](net__context_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [fifo\_reserved](#a2c6f6d484e8744ec97aa966d6f0079c7) |
|  | First member of the structure to allow to put contexts into a FIFO. |
| void \* | [user\_data](#a1679e131dd6626bc210f23938df3fbcb) |
|  | User data associated with a context. |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [refcount](#a0ae23462dcc7f84c95e0cc69dfeb6d5a) |
|  | Reference count. |
| struct [k\_mutex](structk__mutex.md) | [lock](#a730e72866e94ed1695010b50c618a281) |
|  | Internal lock for protecting this context from multiple access. |
| struct sockaddr\_ptr | [local](#a7ed765f4d8b9cdc0fbd080287215f955) |
|  | Local endpoint address. |
| struct [sockaddr](structsockaddr.md) | [remote](#a4a58fc21990e3c3ddb5ebf77c8212b9c) |
|  | Remote endpoint address. |
| struct net\_conn\_handle \* | [conn\_handler](#abd8ff1b4826535df911d2af14b46e312) |
|  | Connection handle. |
| [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) | [recv\_cb](#af551b252faf29ee6018d4bd783c5f2b4) |
|  | Receive callback to be called when desired packet has been received. |
| [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) | [send\_cb](#a38c83746c8b2fcddf187a20299d6eb3c) |
|  | Send callback to be called when the packet has been sent successfully. |
| [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) | [connect\_cb](#abc30f85e6016901b1d6fbb771b07370d) |
|  | Connect callback to be called when a connection has been established. |
| void \* | [tcp](#adee6e668bfae2749df9b986d0049f10b) |
|  | TCP connection information. |
| struct { |  |
| } | [options](#ae3d6ad67411b3e590fe8a627437c1d07) |
|  | Option values. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [proto](#abfb04fc163636498f72b29aa12087e19) |
|  | Protocol (UDP, TCP or IEEE 802.3 protocol value). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#a300e382f78b20f220fc1b450784bbd3c) |
|  | Flags for the context. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [iface](#ad71d151e1e9e35b934949482066f1947) |
|  | Network interface assigned to this context. |
| union { |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ipv6\_hop\_limit](#af9801980b3f2bb16f5ea2126a6e18cb4) |  |
|  | IPv6 hop limit. [More...](#af9801980b3f2bb16f5ea2126a6e18cb4) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ipv6\_mcast\_hop\_limit](#ab6d310ba4253933448584fa40e6ff4b7) |  |
|  | IPv6 multicast hop limit. [More...](#ab6d310ba4253933448584fa40e6ff4b7) |
| } |  |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ipv4\_ttl](#a9a9116844b52dc0366f770f3e6c572eb) |  |
|  | IPv4 TTL. [More...](#a9a9116844b52dc0366f770f3e6c572eb) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ipv4\_mcast\_ttl](#a329f737a3eaf0a57aa6700c59f3733dd) |  |
|  | IPv4 multicast TTL. [More...](#a329f737a3eaf0a57aa6700c59f3733dd) |
| } |  |
| }; |  |
|  | IPv6 hop limit or IPv4 ttl for packets sent via this context. |

## Detailed Description

Note that we do not store the actual source IP address in the context because the address is already set in the network interface struct.

If there is no such source address there, the packet cannot be sent anyway. This saves 12 bytes / context in IPv6.

## Field Documentation

## [◆ ](#ab3e568e7e506ffacaba84255e2c4ea30)[union]

| union { ... } [net\_context](structnet__context.md) |
| --- |

IPv6 hop limit or IPv4 ttl for packets sent via this context.

## [◆ ](#abd8ff1b4826535df911d2af14b46e312)conn\_handler

| struct net\_conn\_handle\* net\_context::conn\_handler |
| --- |

Connection handle.

## [◆ ](#abc30f85e6016901b1d6fbb771b07370d)connect\_cb

| [net\_context\_connect\_cb\_t](group__net__context.md#ga120ae8d4ff788ab21b19c11ed1738a71) net\_context::connect\_cb |
| --- |

Connect callback to be called when a connection has been established.

## [◆ ](#a2c6f6d484e8744ec97aa966d6f0079c7)fifo\_reserved

| void\* net\_context::fifo\_reserved |
| --- |

First member of the structure to allow to put contexts into a FIFO.

## [◆ ](#a300e382f78b20f220fc1b450784bbd3c)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_context::flags |
| --- |

Flags for the context.

## [◆ ](#ad71d151e1e9e35b934949482066f1947)iface

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) net\_context::iface |
| --- |

Network interface assigned to this context.

## [◆ ](#a329f737a3eaf0a57aa6700c59f3733dd)ipv4\_mcast\_ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_context::ipv4\_mcast\_ttl |
| --- |

IPv4 multicast TTL.

## [◆ ](#a9a9116844b52dc0366f770f3e6c572eb)ipv4\_ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_context::ipv4\_ttl |
| --- |

IPv4 TTL.

## [◆ ](#af9801980b3f2bb16f5ea2126a6e18cb4)ipv6\_hop\_limit

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_context::ipv6\_hop\_limit |
| --- |

IPv6 hop limit.

## [◆ ](#ab6d310ba4253933448584fa40e6ff4b7)ipv6\_mcast\_hop\_limit

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_context::ipv6\_mcast\_hop\_limit |
| --- |

IPv6 multicast hop limit.

## [◆ ](#a7ed765f4d8b9cdc0fbd080287215f955)local

| struct sockaddr\_ptr net\_context::local |
| --- |

Local endpoint address.

Note that the values are in network byte order.

## [◆ ](#a730e72866e94ed1695010b50c618a281)lock

| struct [k\_mutex](structk__mutex.md) net\_context::lock |
| --- |

Internal lock for protecting this context from multiple access.

## [◆ ](#ae3d6ad67411b3e590fe8a627437c1d07)[struct]

| struct { ... } net\_context::options |
| --- |

Option values.

## [◆ ](#abfb04fc163636498f72b29aa12087e19)proto

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_context::proto |
| --- |

Protocol (UDP, TCP or IEEE 802.3 protocol value).

## [◆ ](#af551b252faf29ee6018d4bd783c5f2b4)recv\_cb

| [net\_context\_recv\_cb\_t](group__net__context.md#gafa485a6fae8237dd7e6856f4567b2317) net\_context::recv\_cb |
| --- |

Receive callback to be called when desired packet has been received.

## [◆ ](#a0ae23462dcc7f84c95e0cc69dfeb6d5a)refcount

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) net\_context::refcount |
| --- |

Reference count.

## [◆ ](#a4a58fc21990e3c3ddb5ebf77c8212b9c)remote

| struct [sockaddr](structsockaddr.md) net\_context::remote |
| --- |

Remote endpoint address.

Note that the values are in network byte order.

## [◆ ](#a38c83746c8b2fcddf187a20299d6eb3c)send\_cb

| [net\_context\_send\_cb\_t](group__net__context.md#gab3caccfe9fa1bc7ce0e4654192a5de93) net\_context::send\_cb |
| --- |

Send callback to be called when the packet has been sent successfully.

## [◆ ](#adee6e668bfae2749df9b986d0049f10b)tcp

| void\* net\_context::tcp |
| --- |

TCP connection information.

## [◆ ](#a1679e131dd6626bc210f23938df3fbcb)user\_data

| void\* net\_context::user\_data |
| --- |

User data associated with a context.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_context.h](net__context_8h_source.md)

- [net\_context](structnet__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
