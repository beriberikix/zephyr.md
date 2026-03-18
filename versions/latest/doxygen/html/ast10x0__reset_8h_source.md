---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ast10x0__reset_8h_source.html
original_path: doxygen/html/ast10x0__reset_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ast10x0\_reset.h

[Go to the documentation of this file.](ast10x0__reset_8h.md)

1/\*

2 \* Copyright (c) 2022 Aspeed Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_AST10X0\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_AST10X0\_H\_

9

[ 10](ast10x0__reset_8h.md#a58f51601c877080d344167774969c9b4)#define ASPEED\_RESET\_GRP\_0\_OFFSET (0)

[ 11](ast10x0__reset_8h.md#af60cf3c19df220966fcc6aeb553677a8)#define ASPEED\_RESET\_GRP\_1\_OFFSET (32)

12

[ 13](ast10x0__reset_8h.md#a18a69d795a56e9077333b8d50fac36b0)#define ASPEED\_RESET\_HACE (ASPEED\_RESET\_GRP\_0\_OFFSET + 4)

[ 14](ast10x0__reset_8h.md#aa63cefb88f641936f49389acaff04cbc)#define ASPEED\_RESET\_USB (ASPEED\_RESET\_GRP\_0\_OFFSET + 3)

[ 15](ast10x0__reset_8h.md#a54fbdaa166cf43dadb6a4d9777b581c3)#define ASPEED\_RESET\_SRAM (ASPEED\_RESET\_GRP\_0\_OFFSET + 0)

16

[ 17](ast10x0__reset_8h.md#a19e6207b2212a0a58b8dc5c736748df1)#define ASPEED\_RESET\_UART4 (ASPEED\_RESET\_GRP\_1\_OFFSET + 31)

[ 18](ast10x0__reset_8h.md#a31e0692dd65c0adbe937daebee4477e2)#define ASPEED\_RESET\_UART3 (ASPEED\_RESET\_GRP\_1\_OFFSET + 30)

[ 19](ast10x0__reset_8h.md#a67087547f237de76d2ab1e9c2fd774f1)#define ASPEED\_RESET\_UART2 (ASPEED\_RESET\_GRP\_1\_OFFSET + 29)

[ 20](ast10x0__reset_8h.md#ab7429f58459c26d3cf637e4d9e764d67)#define ASPEED\_RESET\_UART1 (ASPEED\_RESET\_GRP\_1\_OFFSET + 28)

21

[ 22](ast10x0__reset_8h.md#a2000c2cd1474abe2acf6716293f9a656)#define ASPEED\_RESET\_JTAG\_M0 (ASPEED\_RESET\_GRP\_1\_OFFSET + 26)

[ 23](ast10x0__reset_8h.md#a76bc43a3b57f919db372e4a79dc79b6f)#define ASPEED\_RESET\_ESPI (ASPEED\_RESET\_GRP\_1\_OFFSET + 25)

24

[ 25](ast10x0__reset_8h.md#ac8cad68c9911554194574d460d3f3814)#define ASPEED\_RESET\_ADC (ASPEED\_RESET\_GRP\_1\_OFFSET + 23)

[ 26](ast10x0__reset_8h.md#a8e20719b17e4f21c9673a7e740362b8e)#define ASPEED\_RESET\_JTAG\_M1 (ASPEED\_RESET\_GRP\_1\_OFFSET + 22)

27

[ 28](ast10x0__reset_8h.md#ae546e699360d23e89ddba7310d637c8a)#define ASPEED\_RESET\_MAC (ASPEED\_RESET\_GRP\_1\_OFFSET + 20)

29

[ 30](ast10x0__reset_8h.md#a6eb1a65fee7f7d589e5c40acb06a59a7)#define ASPEED\_RESET\_I3C3 (ASPEED\_RESET\_GRP\_1\_OFFSET + 11)

[ 31](ast10x0__reset_8h.md#a3e76867407846a68533e1ef13e5612e0)#define ASPEED\_RESET\_I3C2 (ASPEED\_RESET\_GRP\_1\_OFFSET + 10)

[ 32](ast10x0__reset_8h.md#a792d63822aaf04bcf8670471c6f5cb5c)#define ASPEED\_RESET\_I3C1 (ASPEED\_RESET\_GRP\_1\_OFFSET + 9)

[ 33](ast10x0__reset_8h.md#a392ac704a9bbddcee588e9f52af8557e)#define ASPEED\_RESET\_I3C0 (ASPEED\_RESET\_GRP\_1\_OFFSET + 8)

[ 34](ast10x0__reset_8h.md#a49e0d2e074659166bb20ad0a9a603435)#define ASPEED\_RESET\_I3C (ASPEED\_RESET\_GRP\_1\_OFFSET + 7)

[ 35](ast10x0__reset_8h.md#a49f53d3791ab6d0104837204c31eb1ad)#define ASPEED\_RESET\_PWM\_TACH (ASPEED\_RESET\_GRP\_1\_OFFSET + 5)

[ 36](ast10x0__reset_8h.md#a6cab61e115cc50636d3c5aa8b509f5c5)#define ASPEED\_RESET\_PECI (ASPEED\_RESET\_GRP\_1\_OFFSET + 4)

[ 37](ast10x0__reset_8h.md#abb494d1ccc9ab01d50fc21bb7c2eb7de)#define ASPEED\_RESET\_MII (ASPEED\_RESET\_GRP\_1\_OFFSET + 3)

[ 38](ast10x0__reset_8h.md#a235bf82edd62f2f72fb9de4efa11c7f9)#define ASPEED\_RESET\_I2C (ASPEED\_RESET\_GRP\_1\_OFFSET + 2)

39

[ 40](ast10x0__reset_8h.md#a93f2fc81c8a9cdfee97548fb48281bed)#define ASPEED\_RESET\_LPC (ASPEED\_RESET\_GRP\_1\_OFFSET + 0)

41

42#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_AST10X0\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [ast10x0\_reset.h](ast10x0__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
