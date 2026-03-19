---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/reg_8h.html
original_path: doxygen/html/reg_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reg.h File Reference

[Go to the source code of this file.](reg_8h_source.md)

| Macros | |
| --- | --- |
| #define | [reg\_read](#aa57645f8a20e83b1ae1037cc3a81e1d1)(reg) |
| #define | [reg\_write](#ab38fcaa2c682800f1bef4159e1949f47)(reg, val) |

## Macro Definition Documentation

## [◆ ](#aa57645f8a20e83b1ae1037cc3a81e1d1)reg\_read

| #define reg\_read | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

register unsigned long \_\_rv; \

\_\_asm\_\_ volatile("mv %0, " [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(reg) : "=r"(\_\_rv)); \

\_\_rv; \

})

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

## [◆ ](#ab38fcaa2c682800f1bef4159e1949f47)reg\_write

| #define reg\_write | ( |  | *reg*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

({ \_\_asm\_\_("mv " [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(reg) ", %0" : : "r"(val)); })

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [reg.h](reg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
