---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structgpio__driver__data.html
original_path: doxygen/html/structgpio__driver__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_driver\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

This structure is common to all GPIO drivers and is expected to be the first element in the driver's struct driver\_data declaration.
[More...](#details)

`#include <[gpio.h](drivers_2gpio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | [invert](#ab62038a3c7c341cafda6665dfab3f169) |
|  | Mask identifying pins that are configured as active low. |

## Detailed Description

This structure is common to all GPIO drivers and is expected to be the first element in the driver's struct driver\_data declaration.

## Field Documentation

## [◆ ](#ab62038a3c7c341cafda6665dfab3f169)invert

| [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) gpio\_driver\_data::invert |
| --- |

Mask identifying pins that are configured as active low.

Management of this mask is the responsibility of the wrapper functions in this header.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gpio.h](drivers_2gpio_8h_source.md)

- [gpio\_driver\_data](structgpio__driver__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
