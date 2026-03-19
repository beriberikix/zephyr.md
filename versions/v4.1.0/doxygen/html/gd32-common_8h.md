---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gd32-common_8h.html
original_path: doxygen/html/gd32-common_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gd32-common.h File Reference

[Go to the source code of this file.](gd32-common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GD32\_RESET\_CONFIG](#a518d3150ddd85f37ae028ee744378594)(reg, bit) |
|  | Encode RCU register offset and configuration bit. |

## Macro Definition Documentation

## [◆ ](#a518d3150ddd85f37ae028ee744378594)GD32\_RESET\_CONFIG

| #define GD32\_RESET\_CONFIG | ( |  | *reg*, |
| --- | --- | --- | --- |
|  |  |  | *bit* ) |

**Value:**

(((GD32\_ ## reg ## \_OFFSET) << 6U) | (bit))

Encode RCU register offset and configuration bit.

- 0..5: bit number
- 6..14: offset
- 15: reserved

Parameters
:   | reg | RCU register name (expands to GD32\_{reg}\_OFFSET) |
    | --- | --- |
    | bit | Configuration bit |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [gd32-common.h](gd32-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
