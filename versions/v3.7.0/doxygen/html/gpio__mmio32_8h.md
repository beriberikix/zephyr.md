---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gpio__mmio32_8h.html
original_path: doxygen/html/gpio__mmio32_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_mmio32.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](gpio__mmio32_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gpio\_mmio32\_config](structgpio__mmio32__config.md) |
| struct | [gpio\_mmio32\_context](structgpio__mmio32__context.md) |

| Macros | |
| --- | --- |
| #define | [GPIO\_MMIO32\_INIT](#a91033e14faef5aebc20314549e08e932)(node\_id, \_address, \_mask) |

| Functions | |
| --- | --- |
| int | [gpio\_mmio32\_init](#a1896015c34f1b9dac9d8c50b391fdec0) (const struct [device](structdevice.md) \*dev) |

| Variables | |
| --- | --- |
| const struct gpio\_driver\_api | [gpio\_mmio32\_api](#ab8dc4ce9baa25b80565dbde9fd05dcb4) |

## Macro Definition Documentation

## [◆ ](#a91033e14faef5aebc20314549e08e932)GPIO\_MMIO32\_INIT

| #define GPIO\_MMIO32\_INIT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_address*, |
|  |  |  | *\_mask* ) |

## Function Documentation

## [◆ ](#a1896015c34f1b9dac9d8c50b391fdec0)gpio\_mmio32\_init()

| int gpio\_mmio32\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

## Variable Documentation

## [◆ ](#ab8dc4ce9baa25b80565dbde9fd05dcb4)gpio\_mmio32\_api

| | const struct gpio\_driver\_api gpio\_mmio32\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_mmio32.h](gpio__mmio32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
