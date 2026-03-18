---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ft8xx__dl_8h.html
original_path: doxygen/html/ft8xx__dl_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_dl.h File Reference

FT8XX display list commands.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](ft8xx__dl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [FT8XX\_BITMAPS](group__ft8xx__dl.md#ga28f7596c367f67f73d701b792300aa09)   1U |
|  | Rectangular pixel arrays, in various color formats. |
| #define | [FT8XX\_POINTS](group__ft8xx__dl.md#ga1d6f49b3817f9927fa1cd3cd42820490)   2U |
|  | Anti-aliased points, point radius is 1-256 pixels. |
| #define | [FT8XX\_LINES](group__ft8xx__dl.md#ga62bcf30c7a9eae4c468e1c7de144ad01)   3U |
|  | Anti-aliased lines, with width from 0 to 4095 1/16th of pixel units. |
| #define | [FT8XX\_LINE\_STRIP](group__ft8xx__dl.md#gac1b1188c36a4078e7db50d3c5aee7d25)   4U |
|  | Anti-aliased lines, connected head-to-tail. |
| #define | [FT8XX\_EDGE\_STRIP\_R](group__ft8xx__dl.md#ga0b3ce2828323978e9648bfd07caa1065)   5U |
|  | Edge strips for right. |
| #define | [FT8XX\_EDGE\_STRIP\_L](group__ft8xx__dl.md#ga97229abf592bba4039f19a98451cdc5b)   6U |
|  | Edge strips for left. |
| #define | [FT8XX\_EDGE\_STRIP\_A](group__ft8xx__dl.md#gaf5ad60bbe137dbf64281ad8d0be051e0)   7U |
|  | Edge strips for above. |
| #define | [FT8XX\_EDGE\_STRIP\_B](group__ft8xx__dl.md#ga9aff3a3c58e12b990130271e845662a8)   8U |
|  | Edge strips for below. |
| #define | [FT8XX\_RECTS](group__ft8xx__dl.md#ga05077568fea624ed7e3f9e3f6e8d72b8)   9U |
|  | Round-cornered rectangles, curvature of the corners can be adjusted using FT8XX\_LINE\_WIDTH. |
| #define | [FT8XX\_BEGIN](group__ft8xx__dl.md#ga25324ac604e037baf26cdd37341bee44)(prim) |
|  | Begin drawing a graphics primitive. |
| #define | [FT8XX\_CLEAR](group__ft8xx__dl.md#gab0fb60eec6f4c3b68d47f61886e7b933)(c, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), t) |
|  | Clear buffers to preset values. |
| #define | [FT8XX\_CLEAR\_COLOR\_RGB](group__ft8xx__dl.md#ga180b0ed70243277462cf303bc788e094)(red, green, blue) |
|  | Specify clear values for red, green and blue channels. |
| #define | [FT8XX\_COLOR\_RGB](group__ft8xx__dl.md#ga3bc794705028fc7e8e1b742db180055d)(red, green, blue) |
|  | Set the current color red, green and blue. |
| #define | [FT8XX\_DISPLAY](group__ft8xx__dl.md#ga135472b1cdf30d4bd69372e36c9960ce)() |
|  | End the display list. |
| #define | [FT8XX\_END](group__ft8xx__dl.md#ga8a9d0eb6521459eb7ce50b397de194d9)() |
|  | End drawing a graphics primitive. |
| #define | [FT8XX\_LINE\_WIDTH](group__ft8xx__dl.md#ga1d22204625ef070a6b8d16af7ad97578)(width) |
|  | Specify the width of lines to be drawn with primitive [FT8XX\_LINES](group__ft8xx__dl.md#ga62bcf30c7a9eae4c468e1c7de144ad01 "FT8XX_LINES"). |
| #define | [FT8XX\_TAG](group__ft8xx__dl.md#gab0721051bb3f3cb9f555f696f36dfbbf)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Attach the tag value for the following graphics objects. |
| #define | [FT8XX\_VERTEX2F](group__ft8xx__dl.md#ga2648ab069991c02b2e8de62bf13913ab)(x, y) |
|  | Start the operation of graphics primitives at the specified coordinate. |
| #define | [FT8XX\_VERTEX2II](group__ft8xx__dl.md#ga560836cd8c85599f24e5623a3e286b12)(x, y, handle, cell) |
|  | Start the operation of graphics primitive at the specified coordinates. |

## Detailed Description

FT8XX display list commands.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_dl.h](ft8xx__dl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
