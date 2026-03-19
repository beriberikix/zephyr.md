---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/npcx-i2c_8h.html
original_path: doxygen/html/npcx-i2c_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcx-i2c.h File Reference

[Go to the source code of this file.](npcx-i2c_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NPCX\_I2C\_CTRL\_PORT](#a9349b34193640f28fe8c07d192e408ee)(ctrl, port) |

## Macro Definition Documentation

## [◆ ](#a9349b34193640f28fe8c07d192e408ee)NPCX\_I2C\_CTRL\_PORT

| #define NPCX\_I2C\_CTRL\_PORT | ( |  | *ctrl*, |
| --- | --- | --- | --- |
|  |  |  | *port* ) |

**Value:**

(((ctrl & 0xf) << 4) | (port & 0xf))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [i2c](dir_fcc76e97acca71d0ab1d4f13f62b3078.md)
- [npcx-i2c.h](npcx-i2c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
