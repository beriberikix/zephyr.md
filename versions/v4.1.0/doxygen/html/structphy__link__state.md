---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structphy__link__state.html
original_path: doxygen/html/structphy__link__state.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

phy\_link\_state Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet PHY Interface](group__ethernet__phy.md)

Link state.
[More...](#details)

`#include <[phy.h](phy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) | [speed](#ab47802265dcf47b0aa815f4579467b6f) |
|  | Link speed. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_up](#aaced7164c07c5f964c952c2b04d68395) |
|  | When true the link is active and connected. |

## Detailed Description

Link state.

## Field Documentation

## [◆ ](#aaced7164c07c5f964c952c2b04d68395)is\_up

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) phy\_link\_state::is\_up |
| --- |

When true the link is active and connected.

## [◆ ](#ab47802265dcf47b0aa815f4579467b6f)speed

| enum [phy\_link\_speed](group__ethernet__phy.md#ga9b97fff9fcd6823c9b564b3e86b8da68) phy\_link\_state::speed |
| --- |

Link speed.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[phy.h](phy_8h_source.md)

- [phy\_link\_state](structphy__link__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
