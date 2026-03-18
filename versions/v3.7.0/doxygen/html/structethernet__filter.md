---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structethernet__filter.html
original_path: doxygen/html/structethernet__filter.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_filter Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Ethernet filter description.
[More...](#details)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum ethernet\_filter\_type | [type](#aec00b1ecd6af658a5164d375bccdaa10) |
|  | Type of filter. |
| struct [net\_eth\_addr](structnet__eth__addr.md) | [mac\_address](#aaacda9b89d6b21934654e0f2b19624e0) |
|  | MAC address to filter. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [set](#ad83053c859c65e0c0432fe3f59671335) |
|  | Set (true) or unset (false) the filter. |

## Detailed Description

Ethernet filter description.

## Field Documentation

## [◆ ](#aaacda9b89d6b21934654e0f2b19624e0)mac\_address

| struct [net\_eth\_addr](structnet__eth__addr.md) ethernet\_filter::mac\_address |
| --- |

MAC address to filter.

## [◆ ](#ad83053c859c65e0c0432fe3f59671335)set

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_filter::set |
| --- |

Set (true) or unset (false) the filter.

## [◆ ](#aec00b1ecd6af658a5164d375bccdaa10)type

| enum ethernet\_filter\_type ethernet\_filter::type |
| --- |

Type of filter.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_filter](structethernet__filter.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
