---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2coredump_8h.html
original_path: doxygen/html/drivers_2coredump_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coredump.h File Reference

Public APIs for coredump pseudo-device driver.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](drivers_2coredump_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) |
|  | Structure describing a region in memory that may be stored in core dump at the time it is generated. [More...](structcoredump__mem__region__node.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [coredump\_dump\_callback\_t](group__coredump__device__interface.md#ga47ab4c7475a938c294d65dd7bd0197eb)) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dump\_area, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dump\_area\_size) |
|  | Callback that occurs at dump time, data copied into dump\_area will be included in the dump that is generated. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coredump\_device\_register\_memory](group__coredump__device__interface.md#ga14ccecab2b077a32a0bc3bf4ec5df909) (const struct [device](structdevice.md) \*dev, struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \*region) |
|  | Register a region of memory to be stored in core dump at the time it is generated. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coredump\_device\_unregister\_memory](group__coredump__device__interface.md#gafd4e43696175eeb3ad1a2894df945530) (const struct [device](structdevice.md) \*dev, struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \*region) |
|  | Unregister a region of memory to be stored in core dump at the time it is generated. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coredump\_device\_register\_callback](group__coredump__device__interface.md#ga9a59905e1440bdc78aa115645d85d363) (const struct [device](structdevice.md) \*dev, [coredump\_dump\_callback\_t](group__coredump__device__interface.md#ga47ab4c7475a938c294d65dd7bd0197eb) callback) |
|  | Register a callback to be invoked at dump time. |

## Detailed Description

Public APIs for coredump pseudo-device driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [coredump.h](drivers_2coredump_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
