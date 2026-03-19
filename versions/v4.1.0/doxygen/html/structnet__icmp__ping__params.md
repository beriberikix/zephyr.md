---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__icmp__ping__params.html
original_path: doxygen/html/structnet__icmp__ping__params.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_icmp\_ping\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Send and receive IPv4 or IPv6 ICMP Echo Request messages.](group__icmp.md)

Struct presents parameters that are needed when sending Echo-Request (ping) messages.
[More...](#details)

`#include <[icmp.h](icmp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [identifier](#a138d6de6072ebbf3ae454eb3ee28b138) |
|  | An identifier to aid in matching Echo Replies to this Echo Request. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sequence](#a3756461b95ce1b7fde9d59819de10d85) |
|  | A sequence number to aid in matching Echo Replies to this Echo Request. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tc\_tos](#aaf5a9493b5d98f72bb27758fd24c64ec) |
|  | Can be either IPv4 Type-of-service field value, or IPv6 Traffic Class field value. |
| int | [priority](#a3a9abdb27bfb94ca6515e280bf6bee3c) |
|  | Network packet priority. |
| const void \* | [data](#ac2247bc63eea000200429f0f441031bf) |
|  | Arbitrary payload data that will be included in the Echo Reply verbatim. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [data\_size](#a342b75123a32e35f91bda3e11601598b) |
|  | Size of the Payload Data in bytes. |

## Detailed Description

Struct presents parameters that are needed when sending Echo-Request (ping) messages.

## Field Documentation

## [◆ ](#ac2247bc63eea000200429f0f441031bf)data

| const void\* net\_icmp\_ping\_params::data |
| --- |

Arbitrary payload data that will be included in the Echo Reply verbatim.

May be NULL.

## [◆ ](#a342b75123a32e35f91bda3e11601598b)data\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) net\_icmp\_ping\_params::data\_size |
| --- |

Size of the Payload Data in bytes.

May be zero. In case data pointer is NULL, the function will generate the payload up to the requested size.

## [◆ ](#a138d6de6072ebbf3ae454eb3ee28b138)identifier

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_icmp\_ping\_params::identifier |
| --- |

An identifier to aid in matching Echo Replies to this Echo Request.

May be zero.

## [◆ ](#a3a9abdb27bfb94ca6515e280bf6bee3c)priority

| int net\_icmp\_ping\_params::priority |
| --- |

Network packet priority.

## [◆ ](#a3756461b95ce1b7fde9d59819de10d85)sequence

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_icmp\_ping\_params::sequence |
| --- |

A sequence number to aid in matching Echo Replies to this Echo Request.

May be zero.

## [◆ ](#aaf5a9493b5d98f72bb27758fd24c64ec)tc\_tos

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_icmp\_ping\_params::tc\_tos |
| --- |

Can be either IPv4 Type-of-service field value, or IPv6 Traffic Class field value.

Represents combined DSCP and ECN values.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[icmp.h](icmp_8h_source.md)

- [net\_icmp\_ping\_params](structnet__icmp__ping__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
