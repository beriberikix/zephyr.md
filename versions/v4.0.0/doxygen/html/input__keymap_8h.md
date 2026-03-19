---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/input__keymap_8h.html
original_path: doxygen/html/input__keymap_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_keymap.h File Reference

[Go to the source code of this file.](input__keymap_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MATRIX\_ROW](#afd3fd33c07ccb96c0c88c1a8d340fee3)(keymap\_entry) |
| #define | [MATRIX\_COL](#ad3b19ba368920538444393be76bf7214)(keymap\_entry) |

## Macro Definition Documentation

## [◆ ](#ad3b19ba368920538444393be76bf7214)MATRIX\_COL

| #define MATRIX\_COL | ( |  | *keymap\_entry* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((keymap\_entry) >> 16) & 0xff)

## [◆ ](#afd3fd33c07ccb96c0c88c1a8d340fee3)MATRIX\_ROW

| #define MATRIX\_ROW | ( |  | *keymap\_entry* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((keymap\_entry) >> 24) & 0xff)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_keymap.h](input__keymap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
