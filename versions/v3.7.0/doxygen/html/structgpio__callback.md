---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structgpio__callback.html
original_path: doxygen/html/structgpio__callback.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_callback Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [GPIO Driver APIs](group__gpio__interface.md)

GPIO callback structure.
[More...](#details)

`#include <[gpio.h](drivers_2gpio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#ab60e7093072964bd818d536c746211e4) |
|  | This is meant to be used in the driver and the user should not mess with it (see [drivers/gpio/gpio\_utils.h](gpio__utils_8h.md)). |
| [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) | [handler](#af89dc41cbd610d81ac03cae7ab764ceb) |
|  | Actual callback function being called when relevant. |
| [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) | [pin\_mask](#ace5c2b83f1d51f73877a1f2c54ba8c67) |
|  | A mask of pins the callback is interested in, if 0 the callback will never be called. |

## Detailed Description

GPIO callback structure.

Used to register a callback in the driver instance callback list. As many callbacks as needed can be added as long as each of them are unique pointers of struct [gpio\_callback](structgpio__callback.md "GPIO callback structure."). Beware such structure should not be allocated on stack.

Note: To help setting it, see [gpio\_init\_callback()](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c "Helper to initialize a struct gpio_callback properly.") below

## Field Documentation

## [◆ ](#af89dc41cbd610d81ac03cae7ab764ceb)handler

| [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) gpio\_callback::handler |
| --- |

Actual callback function being called when relevant.

## [◆ ](#ab60e7093072964bd818d536c746211e4)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) gpio\_callback::node |
| --- |

This is meant to be used in the driver and the user should not mess with it (see [drivers/gpio/gpio\_utils.h](gpio__utils_8h.md)).

## [◆ ](#ace5c2b83f1d51f73877a1f2c54ba8c67)pin\_mask

| [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) gpio\_callback::pin\_mask |
| --- |

A mask of pins the callback is interested in, if 0 the callback will never be called.

Such pin\_mask can be modified whenever necessary by the owner, and thus will affect the handler being called or not. The selected pins must be configured to trigger an interrupt.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[gpio.h](drivers_2gpio_8h_source.md)

- [gpio\_callback](structgpio__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
