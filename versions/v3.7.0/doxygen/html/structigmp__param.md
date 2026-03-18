---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structigmp__param.html
original_path: doxygen/html/structigmp__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

igmp\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IGMP API](group__igmp.md)

IGMP parameters.
[More...](#details)

`#include <[igmp.h](igmp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in\_addr](structin__addr.md) \* | [source\_list](#ab64622c259c381d4c1ae3e3c0497b2b7) |
|  | List of sources to include or exclude. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sources\_len](#acb8f39f66f0c11733cf855f4303b0495) |
|  | Length of source list. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [include](#a2b60c5de6e21371dacc7f7f34ba6904b) |
|  | Source list filter type. |

## Detailed Description

IGMP parameters.

## Field Documentation

## [◆ ](#a2b60c5de6e21371dacc7f7f34ba6904b)include

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) igmp\_param::include |
| --- |

Source list filter type.

## [◆ ](#ab64622c259c381d4c1ae3e3c0497b2b7)source\_list

| struct [in\_addr](structin__addr.md)\* igmp\_param::source\_list |
| --- |

List of sources to include or exclude.

## [◆ ](#acb8f39f66f0c11733cf855f4303b0495)sources\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) igmp\_param::sources\_len |
| --- |

Length of source list.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[igmp.h](igmp_8h_source.md)

- [igmp\_param](structigmp__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
