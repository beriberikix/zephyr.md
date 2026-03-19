---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stepper__drv8424_8h.html
original_path: doxygen/html/stepper__drv8424_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper\_drv8424.h File Reference

Public API for DRV8424 Stepper Controller Specific Functions.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/drivers/stepper.h](stepper_8h_source.md)>`

[Go to the source code of this file.](stepper__drv8424_8h_source.md)

| Functions | |
| --- | --- |
| int | [drv8424\_microstep\_recovery](#af25c14a3f91974bd689755989dc962d0) (const struct [device](structdevice.md) \*dev) |
|  | After microstep setter fails, attempt to recover into previous state. |

## Detailed Description

Public API for DRV8424 Stepper Controller Specific Functions.

## Function Documentation

## [◆ ](#af25c14a3f91974bd689755989dc962d0)drv8424\_microstep\_recovery()

| int drv8424\_microstep\_recovery | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

After microstep setter fails, attempt to recover into previous state.

Parameters
:   | dev | Pointer to the stepper motor controller instance |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | <0 | Error code dependent on the gpio controller of the microstep pins |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_drv8424.h](stepper__drv8424_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
