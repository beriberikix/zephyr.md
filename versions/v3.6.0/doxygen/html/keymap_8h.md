---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/keymap_8h.html
original_path: doxygen/html/keymap_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

keymap.h File Reference

[Go to the source code of this file.](keymap_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MATRIX\_KEY](#ab43c29335b0939bfa3e770c86d1622a0)(row, col, code) |

## Macro Definition Documentation

## [◆ ](#ab43c29335b0939bfa3e770c86d1622a0)MATRIX\_KEY

| #define MATRIX\_KEY | ( |  | *row*, |
| --- | --- | --- | --- |
|  |  |  | *col*, |
|  |  |  | *code* ) |

**Value:**

((((row) & 0xff) << 24) | (((col) & 0xff) << 16) | ((code) & 0xffff))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [input](dir_ab844d62c7a22d129cc80e6c359d2c21.md)
- [keymap.h](keymap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
