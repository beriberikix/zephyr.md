---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__coredump__device__interface.html
original_path: doxygen/html/group__coredump__device__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Coredump pseudo-device driver APIs

[Device Driver APIs](group__io__interfaces.md)

Coredump pseudo-device driver APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) |
|  | Structure describing a region in memory that may be stored in core dump at the time it is generated. [More...](structcoredump__mem__region__node.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [coredump\_dump\_callback\_t](#ga47ab4c7475a938c294d65dd7bd0197eb)) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dump\_area, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dump\_area\_size) |
|  | Callback that occurs at dump time, data copied into dump\_area will be included in the dump that is generated. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coredump\_device\_register\_memory](#ga14ccecab2b077a32a0bc3bf4ec5df909) (const struct [device](structdevice.md) \*dev, struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \*region) |
|  | Register a region of memory to be stored in core dump at the time it is generated. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coredump\_device\_unregister\_memory](#gafd4e43696175eeb3ad1a2894df945530) (const struct [device](structdevice.md) \*dev, struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \*region) |
|  | Unregister a region of memory to be stored in core dump at the time it is generated. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [coredump\_device\_register\_callback](#ga9a59905e1440bdc78aa115645d85d363) (const struct [device](structdevice.md) \*dev, [coredump\_dump\_callback\_t](#ga47ab4c7475a938c294d65dd7bd0197eb) callback) |
|  | Register a callback to be invoked at dump time. |

## Detailed Description

Coredump pseudo-device driver APIs.

## Typedef Documentation

## [◆ ](#ga47ab4c7475a938c294d65dd7bd0197eb)coredump\_dump\_callback\_t

| typedef void(\* coredump\_dump\_callback\_t) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dump\_area, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dump\_area\_size) |
| --- |

`#include <[coredump.h](drivers_2coredump_8h.md)>`

Callback that occurs at dump time, data copied into dump\_area will be included in the dump that is generated.

Parameters
:   | dump\_area | Pointer to area to copy data into for inclusion in dump |
    | --- | --- |
    | dump\_area\_size | Size of available memory at dump\_area |

## Function Documentation

## [◆ ](#ga9a59905e1440bdc78aa115645d85d363)coredump\_device\_register\_callback()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coredump\_device\_register\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [coredump\_dump\_callback\_t](#ga47ab4c7475a938c294d65dd7bd0197eb) | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[coredump.h](drivers_2coredump_8h.md)>`

Register a callback to be invoked at dump time.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | Callback to be invoked at dump time |

Returns
:   true if registration succeeded
:   false if registration failed

## [◆ ](#ga14ccecab2b077a32a0bc3bf4ec5df909)coredump\_device\_register\_memory()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coredump\_device\_register\_memory | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \* | *region* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[coredump.h](drivers_2coredump_8h.md)>`

Register a region of memory to be stored in core dump at the time it is generated.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | region | Struct describing memory to be collected |

Returns
:   true if registration succeeded
:   false if registration failed

## [◆ ](#gafd4e43696175eeb3ad1a2894df945530)coredump\_device\_unregister\_memory()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coredump\_device\_unregister\_memory | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [coredump\_mem\_region\_node](structcoredump__mem__region__node.md) \* | *region* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[coredump.h](drivers_2coredump_8h.md)>`

Unregister a region of memory to be stored in core dump at the time it is generated.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | region | Struct describing memory to be collected |

Returns
:   true if unregistration succeeded
:   false if unregistration failed

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
