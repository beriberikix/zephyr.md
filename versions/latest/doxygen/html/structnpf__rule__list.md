---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnpf__rule__list.html
original_path: doxygen/html/structnpf__rule__list.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npf\_rule\_list Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Packet Filter API](group__net__pkt__filter.md)

rule set for a given test location
[More...](#details)

`#include <[net_pkt_filter.h](net__pkt__filter_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [rule\_head](#ab6aadf2d3479853c28e94972e7862931) |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#af4d539d930acb257b1496761219d26cd) |

## Detailed Description

rule set for a given test location

## Field Documentation

## [◆ ](#af4d539d930acb257b1496761219d26cd)lock

| struct [k\_spinlock](structk__spinlock.md) npf\_rule\_list::lock |
| --- |

## [◆ ](#ab6aadf2d3479853c28e94972e7862931)rule\_head

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) npf\_rule\_list::rule\_head |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_pkt\_filter.h](net__pkt__filter_8h_source.md)

- [npf\_rule\_list](structnpf__rule__list.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
