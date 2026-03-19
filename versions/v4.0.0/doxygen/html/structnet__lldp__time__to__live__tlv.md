---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structnet__lldp__time__to__live__tlv.html
original_path: doxygen/html/structnet__lldp__time__to__live__tlv.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_lldp\_time\_to\_live\_tlv Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Link Layer Discovery Protocol definitions and helpers](group__lldp.md)

Time To Live TLV, see chapter 8.5.4 in IEEE 802.1AB.
[More...](#details)

`#include <[lldp.h](lldp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [type\_length](#a78b88d66184a0d25c413baf2fec495ab) |
|  | 7 bits for type, 9 bits for length |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ttl](#ab967792a938a5d67f744e53be8d5f0fd) |
|  | Time To Live (TTL) value. |

## Detailed Description

Time To Live TLV, see chapter 8.5.4 in IEEE 802.1AB.

## Field Documentation

## [◆ ](#ab967792a938a5d67f744e53be8d5f0fd)ttl

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_lldp\_time\_to\_live\_tlv::ttl |
| --- |

Time To Live (TTL) value.

## [◆ ](#a78b88d66184a0d25c413baf2fec495ab)type\_length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_lldp\_time\_to\_live\_tlv::type\_length |
| --- |

7 bits for type, 9 bits for length

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lldp.h](lldp_8h_source.md)

- [net\_lldp\_time\_to\_live\_tlv](structnet__lldp__time__to__live__tlv.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
