---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ospi_8h_source.html
original_path: doxygen/html/ospi_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ospi.h

[Go to the documentation of this file.](ospi_8h.md)

1/\*

2 \* Copyright (c) 2022 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_OSPI\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_OSPI\_H\_

8

16

17/\* OSPI mode operating on 1 line, 2 lines, 4 lines or 8 lines \*/

18/\* 1 Cmd Line, 1 Address Line and 1 Data Line \*/

[ 19](ospi_8h.md#aa05908cb55f8b2c2b075fa5fe63295d6)#define OSPI\_SPI\_MODE 1

20/\* 2 Cmd Lines, 2 Address Lines and 2 Data Lines \*/

[ 21](ospi_8h.md#a16b26e6d0f41ec784419f650580bab70)#define OSPI\_DUAL\_MODE 2

22/\* 4 Cmd Lines, 4 Address Lines and 4 Data Lines \*/

[ 23](ospi_8h.md#a9baa648178c8018dc3371df3ec62ad46)#define OSPI\_QUAD\_MODE 4

24/\* 8 Cmd Lines, 8 Address Lines and 8 Data Lines \*/

[ 25](ospi_8h.md#a3a5249c447488edc0bd67e69ffbb2323)#define OSPI\_OPI\_MODE 8

26

27/\* OSPI mode operating on Single or Double Transfer Rate \*/

28/\* Single Transfer Rate \*/

[ 29](ospi_8h.md#a05dc6d0a9546bb2ddad1b519cf663a3b)#define OSPI\_STR\_TRANSFER 1

30/\* Double Transfer Rate \*/

[ 31](ospi_8h.md#adc6ece270c248515bc36b7e73b32fedd)#define OSPI\_DTR\_TRANSFER 2

32

33#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_OSPI\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [flash\_controller](dir_cd262f46d6d541746154471716dc2a72.md)
- [ospi.h](ospi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
