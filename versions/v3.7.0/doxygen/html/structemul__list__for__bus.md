---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structemul__list__for__bus.html
original_path: doxygen/html/structemul__list__for__bus.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_list\_for\_bus Struct Reference

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md)

List of emulators attached to a bus.
[More...](#details)

`#include <[emul.h](drivers_2emul_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [emul\_link\_for\_bus](structemul__link__for__bus.md) \* | [children](#a4cd116abd8480895312564dcdf3f2e03) |
|  | Identifiers for children of the node. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [num\_children](#abcfe7bc6d82a16959c3d89b8598a8563) |
|  | Number of children of the node. |

## Detailed Description

List of emulators attached to a bus.

## Field Documentation

## [◆ ](#a4cd116abd8480895312564dcdf3f2e03)children

| const struct [emul\_link\_for\_bus](structemul__link__for__bus.md)\* emul\_list\_for\_bus::children |
| --- |

Identifiers for children of the node.

## [◆ ](#abcfe7bc6d82a16959c3d89b8598a8563)num\_children

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int emul\_list\_for\_bus::num\_children |
| --- |

Number of children of the node.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[emul.h](drivers_2emul_8h_source.md)

- [emul\_list\_for\_bus](structemul__list__for__bus.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
