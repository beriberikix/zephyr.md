---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/printk-hooks_8h.html
original_path: doxygen/html/printk-hooks_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

printk-hooks.h File Reference

[Go to the source code of this file.](printk-hooks_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef int(\* | [printk\_hook\_fn\_t](#a17d0c01ee515cc6f962dbd56a4c9b36f)) (int c) |
|  | printk function handler |

## Typedef Documentation

## [◆ ](#a17d0c01ee515cc6f962dbd56a4c9b36f)printk\_hook\_fn\_t

| typedef int(\* printk\_hook\_fn\_t) (int c) |
| --- |

printk function handler

Parameters
:   | c | Character to output |
    | --- | --- |

Returns
:   The character passed as input.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [printk-hooks.h](printk-hooks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
