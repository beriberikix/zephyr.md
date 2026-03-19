---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structgpio__driver__config.html
original_path: doxygen/html/structgpio__driver__config.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_driver\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

This structure is common to all GPIO drivers and is expected to be the first element in the object pointed to by the config field in the device structure.
[More...](#details)

`#include <[gpio.h](drivers_2gpio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | [port\_pin\_mask](#af73c0d9d433b86b9d0e0c6703e737052) |
|  | Mask identifying pins supported by the controller. |

## Detailed Description

This structure is common to all GPIO drivers and is expected to be the first element in the object pointed to by the config field in the device structure.

## Field Documentation

## [◆ ](#af73c0d9d433b86b9d0e0c6703e737052)port\_pin\_mask

| [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) gpio\_driver\_config::port\_pin\_mask |
| --- |

Mask identifying pins supported by the controller.

Initialization of this mask is the responsibility of device instance generation in the driver.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gpio.h](drivers_2gpio_8h_source.md)

- [gpio\_driver\_config](structgpio__driver__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
