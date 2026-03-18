---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__b12__emulator__backend.html
original_path: doxygen/html/group__b12__emulator__backend.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BC1.2 backed emulator APIs

[Device Driver APIs](group__io__interfaces.md)

BC1.2 backend emulator APIs.
[More...](#details)

| Functions | |
| --- | --- |
| static int | [bc12\_emul\_set\_charging\_partner](#gaca0e62f2f8a5ec3135523fa3a1308034) (const struct [emul](structemul.md) \*target, enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) partner\_type) |
|  | Set the charging partner type connected to the BC1.2 device. |
| static int | [bc12\_emul\_set\_pd\_partner](#gaa71771a3199aef043fe313f09f3bb4f2) (const struct [emul](structemul.md) \*target, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) connected) |
|  | Set the portable device partner state. |

## Detailed Description

BC1.2 backend emulator APIs.

## Function Documentation

## [◆ ](#gaca0e62f2f8a5ec3135523fa3a1308034)bc12\_emul\_set\_charging\_partner()

| | int bc12\_emul\_set\_charging\_partner | ( | const struct [emul](structemul.md) \* | *target*, | | --- | --- | --- | --- | |  |  | enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) | *partner\_type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_bc12.h](emul__bc12_8h.md)>`

Set the charging partner type connected to the BC1.2 device.

The corresponding BC1.2 emulator updates the vendor specific registers to simulate connection of the specified charging partner type. The emulator also generates an interrupt for processing by the real driver, if supported.

Parameters
:   | target | Pointer to the emulator structure for the BC1.2 emulator instance. |
    | --- | --- |
    | partner\_type | The simulated partner type. Set to BC12\_TYPE\_NONE to disconnect the charging partner. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | if the partner type is not supported. |

## [◆ ](#gaa71771a3199aef043fe313f09f3bb4f2)bc12\_emul\_set\_pd\_partner()

| | int bc12\_emul\_set\_pd\_partner | ( | const struct [emul](structemul.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *connected* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[emul_bc12.h](emul__bc12_8h.md)>`

Set the portable device partner state.

The corresponding BC1.2 emulator updates the vendor specific registers to simulate connection or disconnection of a portable device partner. The emulator also generates an interrupt for processing by the real driver, if supported.

Parameters
:   | target | Pointer to the emulator structure for the BC1.2 emulator instance. |
    | --- | --- |
    | connected | If true, emulate a connection of a portable device partner. If false, emulate a disconnect event. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | if the connection/disconnection of PD partner is not supported. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
