---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ft8xx__dl_8h_source.html
original_path: doxygen/html/ft8xx__dl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_dl.h

[Go to the documentation of this file.](ft8xx__dl_8h.md)

1/\*

2 \* Copyright (c) 2020 Hubert Miś

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_DL\_H\_

13#define ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_DL\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

[ 29](group__ft8xx__dl.md#ga28f7596c367f67f73d701b792300aa09)#define FT8XX\_BITMAPS 1U

[ 31](group__ft8xx__dl.md#ga1d6f49b3817f9927fa1cd3cd42820490)#define FT8XX\_POINTS 2U

[ 36](group__ft8xx__dl.md#ga62bcf30c7a9eae4c468e1c7de144ad01)#define FT8XX\_LINES 3U

[ 38](group__ft8xx__dl.md#gac1b1188c36a4078e7db50d3c5aee7d25)#define FT8XX\_LINE\_STRIP 4U

[ 40](group__ft8xx__dl.md#ga0b3ce2828323978e9648bfd07caa1065)#define FT8XX\_EDGE\_STRIP\_R 5U

[ 42](group__ft8xx__dl.md#ga97229abf592bba4039f19a98451cdc5b)#define FT8XX\_EDGE\_STRIP\_L 6U

[ 44](group__ft8xx__dl.md#gaf5ad60bbe137dbf64281ad8d0be051e0)#define FT8XX\_EDGE\_STRIP\_A 7U

[ 46](group__ft8xx__dl.md#ga9aff3a3c58e12b990130271e845662a8)#define FT8XX\_EDGE\_STRIP\_B 8U

[ 51](group__ft8xx__dl.md#ga05077568fea624ed7e3f9e3f6e8d72b8)#define FT8XX\_RECTS 9U

52

[ 76](group__ft8xx__dl.md#ga25324ac604e037baf26cdd37341bee44)#define FT8XX\_BEGIN(prim) (0x1f000000 | ((prim) & 0x0f))

77

[ 101](group__ft8xx__dl.md#gab0fb60eec6f4c3b68d47f61886e7b933)#define FT8XX\_CLEAR(c, s, t) (0x26000000 | \

102 ((c) ? 0x04 : 0) | ((s) ? 0x02 : 0) | ((t) ? 0x01 : 0))

103

[ 113](group__ft8xx__dl.md#ga180b0ed70243277462cf303bc788e094)#define FT8XX\_CLEAR\_COLOR\_RGB(red, green, blue) (0x02000000 | \

114 (((uint32\_t)(red) & 0xff) << 16) | \

115 (((uint32\_t)(green) & 0xff) << 8) | \

116 ((uint32\_t)(blue) & 0xff))

117

[ 128](group__ft8xx__dl.md#ga3bc794705028fc7e8e1b742db180055d)#define FT8XX\_COLOR\_RGB(red, green, blue) (0x04000000 | \

129 (((uint32\_t)(red) & 0xff) << 16) | \

130 (((uint32\_t)(green) & 0xff) << 8) | \

131 ((uint32\_t)(blue) & 0xff))

132

[ 138](group__ft8xx__dl.md#ga135472b1cdf30d4bd69372e36c9960ce)#define FT8XX\_DISPLAY() 0

139

[ 147](group__ft8xx__dl.md#ga8a9d0eb6521459eb7ce50b397de194d9)#define FT8XX\_END() 0x21000000

148

[ 162](group__ft8xx__dl.md#ga1d22204625ef070a6b8d16af7ad97578)#define FT8XX\_LINE\_WIDTH(width) (0x0e000000 | ((uint32\_t)(width) & 0xfff))

163

[ 183](group__ft8xx__dl.md#gab0721051bb3f3cb9f555f696f36dfbbf)#define FT8XX\_TAG(s) (0x03000000 | (uint8\_t)(s))

184

[ 197](group__ft8xx__dl.md#ga2648ab069991c02b2e8de62bf13913ab)#define FT8XX\_VERTEX2F(x, y) (0x40000000 | \

198 (((int32\_t)(x) & 0x7fff) << 15) | \

199 ((int32\_t)(y) & 0x7fff))

200

[ 216](group__ft8xx__dl.md#ga560836cd8c85599f24e5623a3e286b12)#define FT8XX\_VERTEX2II(x, y, handle, cell) (0x80000000 | \

217 (((uint32\_t)(x) & 0x01ff) << 21) | \

218 (((uint32\_t)(y) & 0x01ff) << 12) | \

219 (((uint32\_t)(handle) & 0x1f) << 7) | \

220 ((uint32\_t)(cell) & 0x7f))

221

225

226#ifdef \_\_cplusplus

227}

228#endif

229

230#endif /\* ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_DL\_H\_ \*/

[stdint.h](stdint_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_dl.h](ft8xx__dl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
