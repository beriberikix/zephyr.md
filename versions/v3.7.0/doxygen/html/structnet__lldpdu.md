---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__lldpdu.html
original_path: doxygen/html/structnet__lldpdu.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_lldpdu Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Link Layer Discovery Protocol definitions and helpers](group__lldp.md)

LLDP Data Unit (LLDPDU) shall contain the following ordered TLVs as stated in "8.2 LLDPDU format" from the IEEE 802.1AB.
[More...](#details)

`#include <[lldp.h](lldp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_lldp\_chassis\_tlv](structnet__lldp__chassis__tlv.md) | [chassis\_id](#a1a1c80fe7462ddbfd84289735013834c) |
|  | Mandatory Chassis TLV. |
| struct [net\_lldp\_port\_tlv](structnet__lldp__port__tlv.md) | [port\_id](#aa55adafc5528576017c37a28413bdaf9) |
|  | Mandatory Port TLV. |
| struct [net\_lldp\_time\_to\_live\_tlv](structnet__lldp__time__to__live__tlv.md) | [ttl](#afbe0618b6d849b8ee7b225844ac399df) |
|  | Mandatory TTL TLV. |

## Detailed Description

LLDP Data Unit (LLDPDU) shall contain the following ordered TLVs as stated in "8.2 LLDPDU format" from the IEEE 802.1AB.

## Field Documentation

## [◆ ](#a1a1c80fe7462ddbfd84289735013834c)chassis\_id

| struct [net\_lldp\_chassis\_tlv](structnet__lldp__chassis__tlv.md) net\_lldpdu::chassis\_id |
| --- |

Mandatory Chassis TLV.

## [◆ ](#aa55adafc5528576017c37a28413bdaf9)port\_id

| struct [net\_lldp\_port\_tlv](structnet__lldp__port__tlv.md) net\_lldpdu::port\_id |
| --- |

Mandatory Port TLV.

## [◆ ](#afbe0618b6d849b8ee7b225844ac399df)ttl

| struct [net\_lldp\_time\_to\_live\_tlv](structnet__lldp__time__to__live__tlv.md) net\_lldpdu::ttl |
| --- |

Mandatory TTL TLV.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lldp.h](lldp_8h_source.md)

- [net\_lldpdu](structnet__lldpdu.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
