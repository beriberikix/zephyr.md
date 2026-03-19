---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/kinetis__scg_8h_source.html
original_path: doxygen/html/kinetis__scg_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kinetis\_scg.h

[Go to the documentation of this file.](kinetis__scg_8h.md)

1/\*

2 \* Copyright (c) 2019 Vestas Wind Systems A/S

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_SCG\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_SCG\_H\_

9

10/\* SCG system oscillator mode \*/

[ 11](kinetis__scg_8h.md#ac5bf581c1f7ccd862ef8693b05e99465)#define KINETIS\_SCG\_SOSC\_MODE\_EXT 0U

[ 12](kinetis__scg_8h.md#a4fb36fecd0f33883d4cafe341b63e168)#define KINETIS\_SCG\_SOSC\_MODE\_LOW\_POWER 4U

[ 13](kinetis__scg_8h.md#a8ebac8f54a0391c791ca619ab58e7707)#define KINETIS\_SCG\_SOSC\_MODE\_HIGH\_GAIN 12U

14

15/\* SCG clock controller clock names \*/

[ 16](kinetis__scg_8h.md#ad1584e260f99a07a428f1c56def160c4)#define KINETIS\_SCG\_CORESYS\_CLK 0U

[ 17](kinetis__scg_8h.md#ab1d0e93d2e0bbe66ea5021399530eb2b)#define KINETIS\_SCG\_BUS\_CLK 1U

[ 18](kinetis__scg_8h.md#a1f02848d46c5a32569bd514a5041c537)#define KINETIS\_SCG\_FLEXBUS\_CLK 2U

[ 19](kinetis__scg_8h.md#a0bd69e846f41008346dfeab59bad7b9f)#define KINETIS\_SCG\_FLASH\_CLK 3U

[ 20](kinetis__scg_8h.md#aeb6f75f1a1f78808214c725ba77a9789)#define KINETIS\_SCG\_SOSC\_CLK 4U

[ 21](kinetis__scg_8h.md#a291e583094a9acf7a9252846b70be48c)#define KINETIS\_SCG\_SIRC\_CLK 5U

[ 22](kinetis__scg_8h.md#a36a96d5af13e36190e6c8814159d4ba5)#define KINETIS\_SCG\_FIRC\_CLK 6U

[ 23](kinetis__scg_8h.md#a4afb95604441790c14ad60a44b3a4c0b)#define KINETIS\_SCG\_SPLL\_CLK 7U

[ 24](kinetis__scg_8h.md#ab32db7df492ab7eedf3b0537f9984d53)#define KINETIS\_SCG\_SOSC\_ASYNC\_DIV1\_CLK 8U

[ 25](kinetis__scg_8h.md#a607e8369e67fab74ec71012af025a204)#define KINETIS\_SCG\_SOSC\_ASYNC\_DIV2\_CLK 9U

[ 26](kinetis__scg_8h.md#a01edc69d8ce4e2b314ea2d2094fbbdfc)#define KINETIS\_SCG\_SIRC\_ASYNC\_DIV1\_CLK 10U

[ 27](kinetis__scg_8h.md#a13a5f86cb9aacc51e44c86f6ccc7e4a3)#define KINETIS\_SCG\_SIRC\_ASYNC\_DIV2\_CLK 11U

[ 28](kinetis__scg_8h.md#aa0fedc77870dcdf4dce2a57fcd97c2c5)#define KINETIS\_SCG\_FIRC\_ASYNC\_DIV1\_CLK 12U

[ 29](kinetis__scg_8h.md#a90f4873eb5c2677db1209d7d934759b5)#define KINETIS\_SCG\_FIRC\_ASYNC\_DIV2\_CLK 13U

[ 30](kinetis__scg_8h.md#af03b15968b1f3c9dcff3ac6525ed7ed9)#define KINETIS\_SCG\_SPLL\_ASYNC\_DIV1\_CLK 14U

[ 31](kinetis__scg_8h.md#a44c05dbbd6ceea9cb620da843118e090)#define KINETIS\_SCG\_SPLL\_ASYNC\_DIV2\_CLK 15U

32

33#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_KINETIS\_SCG\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [kinetis\_scg.h](kinetis__scg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
