---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__timeout.html
original_path: doxygen/html/structnet__timeout.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_timeout Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network long timeout primitives and helpers](group__net__timeout.md)

Generic struct for handling network timeouts.
[More...](#details)

`#include <[net_timeout.h](net__timeout_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#aad22be1aa3cdc73fbb14a436fc778282) |
|  | Used to link multiple timeouts that share a common timer infrastructure. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timer\_start](#af4cdf7a22fea4da9bb68105850c2f1ad) |
|  | Time at which the timer was last set. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timer\_timeout](#a05142cac2404dc31bf068a439ed309e1) |
|  | Portion of remaining timeout that does not exceed NET\_TIMEOUT\_MAX\_VALUE. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [wrap\_counter](#a35b1f793d3f1432123093ca48220426b) |
|  | Timer wrap count. |

## Detailed Description

Generic struct for handling network timeouts.

Except for the linking node, all access to state from these objects must go through the defined API.

## Field Documentation

## [◆ ](#aad22be1aa3cdc73fbb14a436fc778282)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) net\_timeout::node |
| --- |

Used to link multiple timeouts that share a common timer infrastructure.

For examples a set of related timers may use a single delayed work structure, which is always scheduled at the shortest time to a timeout event.

## [◆ ](#af4cdf7a22fea4da9bb68105850c2f1ad)timer\_start

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_timeout::timer\_start |
| --- |

Time at which the timer was last set.

This usually corresponds to the low 32 bits of [k\_uptime\_get()](group__clock__apis.md#gae3e992cd3257c23d5b26d765fcbb2b69 "Get system uptime.").

## [◆ ](#a05142cac2404dc31bf068a439ed309e1)timer\_timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_timeout::timer\_timeout |
| --- |

Portion of remaining timeout that does not exceed NET\_TIMEOUT\_MAX\_VALUE.

This value is updated in parallel with timer\_start and wrap\_counter by [net\_timeout\_evaluate()](group__net__timeout.md#ga07b07966dd10929f6d3774467614f006 "Update state to reflect elapsed time and get new delay.").

## [◆ ](#a35b1f793d3f1432123093ca48220426b)wrap\_counter

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_timeout::wrap\_counter |
| --- |

Timer wrap count.

This tracks multiples of NET\_TIMEOUT\_MAX\_VALUE milliseconds that have yet to pass. It is also updated along with timer\_start and wrap\_counter by [net\_timeout\_evaluate()](group__net__timeout.md#ga07b07966dd10929f6d3774467614f006 "Update state to reflect elapsed time and get new delay.").

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_timeout.h](net__timeout_8h_source.md)

- [net\_timeout](structnet__timeout.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
