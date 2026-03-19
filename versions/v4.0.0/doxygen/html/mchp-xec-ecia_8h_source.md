---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mchp-xec-ecia_8h_source.html
original_path: doxygen/html/mchp-xec-ecia_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp-xec-ecia.h

[Go to the documentation of this file.](mchp-xec-ecia_8h.md)

1/\*

2 \* Copyright (c) 2021 Microchip Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_\_DT\_BINDING\_MCHP\_XEC\_ECIA\_H

7#define \_\_DT\_BINDING\_MCHP\_XEC\_ECIA\_H

8

9/\*

10 \* Encode peripheral interrupt information into a 32-bit unsigned.

11 \* g = bits[0:4], GIRQ number in [8, 26]

12 \* gb = bits[12:8], peripheral source bit position [0, 31] in the GIRQ

13 \* na = bits[23:16], aggregated GIRQ NVIC number

14 \* nd = bits[31:24], direct NVIC number. For sources without a direct

15 \* connection nd = na.

16 \* NOTE: GIRQ22 is a peripheral clock wake only. GIRQ22 and its sources

17 \* are not connected to the NVIC. Use 255 for na and nd.

18 \*/

[ 19](mchp-xec-ecia_8h.md#ac1daa9f5e1b5764f0748577ee60550d3)#define MCHP\_XEC\_ECIA(g, gb, na, nd) \

20 (((g) & 0x1f) + (((gb) & 0x1f) << 8) + (((na) & 0xff) << 16) + \

21 (((nd) & 0xff) << 24))

22

23/\* extract specific information from encoded MCHP\_XEC\_ECIA \*/

[ 24](mchp-xec-ecia_8h.md#a6fee82b914dc9f73392586224f0708e7)#define MCHP\_XEC\_ECIA\_GIRQ(e) ((e) & 0x1f)

[ 25](mchp-xec-ecia_8h.md#a32c0b5e661fbee763a496b3b06eae34a)#define MCHP\_XEC\_ECIA\_GIRQ\_POS(e) (((e) >> 8) & 0x1f)

[ 26](mchp-xec-ecia_8h.md#a9099e944648c0d8b6946b2092f872122)#define MCHP\_XEC\_ECIA\_NVIC\_AGGR(e) (((e) >> 16) & 0xff)

[ 27](mchp-xec-ecia_8h.md#a1efb0ece73d7b15da7cdc316c162bc3a)#define MCHP\_XEC\_ECIA\_NVIC\_DIRECT(e) (((e) >> 24) & 0xff)

28

29#endif /\* \_\_DT\_BINDING\_MCHP\_XEC\_ECIA\_H \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [mchp-xec-ecia.h](mchp-xec-ecia_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
