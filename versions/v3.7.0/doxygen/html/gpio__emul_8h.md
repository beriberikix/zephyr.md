---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gpio__emul_8h.html
original_path: doxygen/html/gpio__emul_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_emul.h File Reference

Backend API for emulated GPIO.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](gpio__emul_8h_source.md)

| Functions | |
| --- | --- |
| int | [gpio\_emul\_input\_set\_masked](group__gpio__emul.md#gaa7eae6a0f85d0f0fb6a8aa41329f4709) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) values) |
|  | Modify the values of one or more emulated GPIO input `pins`. |
| static int | [gpio\_emul\_input\_set](group__gpio__emul.md#ga3962e337bc22e532f2c181724621fcf8) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, int value) |
|  | Modify the value of one emulated GPIO input `pin`. |
| int | [gpio\_emul\_output\_get\_masked](group__gpio__emul.md#gaa6e4c5c2c53d421e9635c0a977172205) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*values) |
|  | Read the value of one or more emulated GPIO output `pins`. |
| static int | [gpio\_emul\_output\_get](group__gpio__emul.md#gaa62613aa6eb442d2c4e436893316124f) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Read the value of one emulated GPIO output `pin`. |
| int | [gpio\_emul\_flags\_get](group__gpio__emul.md#ga86bd5ff4f557e4d520a4f760fb74cdd5) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get `flags` for a given emulated GPIO `pin`. |

## Detailed Description

Backend API for emulated GPIO.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_emul.h](gpio__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
