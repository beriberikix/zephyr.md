---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xspi_8h_source.html
original_path: doxygen/html/xspi_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xspi.h

[Go to the documentation of this file.](xspi_8h.md)

1/\*

2 \* Copyright (c) 2024 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_XSPI\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_XSPI\_H\_

8

14

15/\* XSPI mode operating on 1 line, 2 lines, 4 lines or 8 lines \*/

16/\* 1 Cmd Line, 1 Address Line and 1 Data Line \*/

[ 17](xspi_8h.md#af46f316833f2edf8ad528c2247050f7b)#define XSPI\_SPI\_MODE 1

18/\* 2 Cmd Lines, 2 Address Lines and 2 Data Lines \*/

[ 19](xspi_8h.md#a6b13657beb90f13af580a7ffce42af33)#define XSPI\_DUAL\_MODE 2

20/\* 4 Cmd Lines, 4 Address Lines and 4 Data Lines \*/

[ 21](xspi_8h.md#a707d8a21a2b53d6b9d5ccbcb830bec39)#define XSPI\_QUAD\_MODE 4

22/\* 8 Cmd Lines, 8 Address Lines and 8 Data Lines \*/

[ 23](xspi_8h.md#a31cb4ace810add7d7b9bd9b18114f83e)#define XSPI\_OCTO\_MODE 8

24

25/\* XSPI mode operating on Single or Double Transfer Rate \*/

26/\* Single Transfer Rate \*/

[ 27](xspi_8h.md#aaba9227de2cc14e8e8215391c8e8d569)#define XSPI\_STR\_TRANSFER 1

28/\* Double Transfer Rate \*/

[ 29](xspi_8h.md#a779d385b42986b752d93b0de74b52015)#define XSPI\_DTR\_TRANSFER 2

30

31#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_XSPI\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [flash\_controller](dir_cd262f46d6d541746154471716dc2a72.md)
- [xspi.h](xspi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
