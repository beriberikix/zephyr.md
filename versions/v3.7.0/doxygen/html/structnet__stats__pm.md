---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__stats__pm.html
original_path: doxygen/html/structnet__stats__pm.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_stats\_pm Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Statistics Library](group__net__stats.md)

Power management statistics.
[More...](#details)

`#include <[net_stats.h](net__stats_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [overall\_suspend\_time](#ab43935fcfe9efc1cd5f3e7e329996805) |
|  | Total suspend time. |
| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) | [suspend\_count](#ac14122a4765c499c045f18c70af355a0) |
|  | How many times we were suspended. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [last\_suspend\_time](#a0bdf9c3676298e2df4ff3bfa03f5e823) |
|  | How long the last suspend took. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [start\_time](#a6784806eaa093431ed3c0f7acfe5a89c) |
|  | Network interface last suspend start time. |

## Detailed Description

Power management statistics.

## Field Documentation

## [◆ ](#a0bdf9c3676298e2df4ff3bfa03f5e823)last\_suspend\_time

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_stats\_pm::last\_suspend\_time |
| --- |

How long the last suspend took.

## [◆ ](#ab43935fcfe9efc1cd5f3e7e329996805)overall\_suspend\_time

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_stats\_pm::overall\_suspend\_time |
| --- |

Total suspend time.

## [◆ ](#a6784806eaa093431ed3c0f7acfe5a89c)start\_time

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_stats\_pm::start\_time |
| --- |

Network interface last suspend start time.

## [◆ ](#ac14122a4765c499c045f18c70af355a0)suspend\_count

| [net\_stats\_t](group__net__stats.md#ga05ec15873e79256c287f21b6b6fcd752) net\_stats\_pm::suspend\_count |
| --- |

How many times we were suspended.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_stats.h](net__stats_8h_source.md)

- [net\_stats\_pm](structnet__stats__pm.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
