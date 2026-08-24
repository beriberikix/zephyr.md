---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/gpio__ambiq_8h.html
original_path: doxygen/html/gpio__ambiq_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_ambiq.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](gpio__ambiq_8h_source.md)

| Functions | |
| --- | --- |
| [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | [ambiq\_gpio\_get\_pinnum](#aaaf57fd1692176a44714852f7593913d) (const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Get the actual gpio pin number. |

## Function Documentation

## [◆ ](#aaaf57fd1692176a44714852f7593913d)ambiq\_gpio\_get\_pinnum()

| [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) ambiq\_gpio\_get\_pinnum | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) |

Get the actual gpio pin number.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number of the select gpio group. |

Return values
:   | pin | number. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_ambiq.h](gpio__ambiq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
