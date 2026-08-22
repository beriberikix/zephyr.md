---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/stepper__drv84xx_8h.html
original_path: doxygen/html/stepper__drv84xx_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper\_drv84xx.h File Reference

Public API for DRV84XX Stepper Controller Specific Functions.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/drivers/stepper.h](stepper_8h_source.md)>`

[Go to the source code of this file.](stepper__drv84xx_8h_source.md)

| Functions | |
| --- | --- |
| int | [drv84xx\_microstep\_recovery](#aee40af14c8f26a7df237e9be0597942e) (const struct [device](structdevice.md) \*dev) |
|  | After microstep setter fails, attempt to recover into previous state. |

## Detailed Description

Public API for DRV84XX Stepper Controller Specific Functions.

## Function Documentation

## [◆ ](#aee40af14c8f26a7df237e9be0597942e)drv84xx\_microstep\_recovery()

| int drv84xx\_microstep\_recovery | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
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
- [stepper\_drv84xx.h](stepper__drv84xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
