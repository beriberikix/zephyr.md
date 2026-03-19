---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ast10x0__clock_8h_source.html
original_path: doxygen/html/ast10x0__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ast10x0\_clock.h

[Go to the documentation of this file.](ast10x0__clock_8h.md)

1/\*

2 \* Copyright (c) 2022 Aspeed Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_AST10X0\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_AST10X0\_H\_

9

[ 10](ast10x0__clock_8h.md#a037d8cf6fe0039675c6d0b3ace4421d9)#define ASPEED\_CLK\_GRP\_0\_OFFSET (0)

[ 11](ast10x0__clock_8h.md#ab37a99b66163853d3e6ca8f4a9f4d57f)#define ASPEED\_CLK\_GRP\_1\_OFFSET (32)

[ 12](ast10x0__clock_8h.md#a608fc420936e936d77ef94427419184d)#define ASPEED\_CLK\_GRP\_2\_OFFSET (64)

13

[ 14](ast10x0__clock_8h.md#a3b37b31cba1a39e9d641c9f97ed32a28)#define ASPEED\_CLK\_MCLK (ASPEED\_CLK\_GRP\_0\_OFFSET + 0)

[ 15](ast10x0__clock_8h.md#a165a6862679163abf282c0eb67e94def)#define ASPEED\_CLK\_USB\_DEVICE (ASPEED\_CLK\_GRP\_0\_OFFSET + 7)

[ 16](ast10x0__clock_8h.md#a74d307980b4aa1dcb0ad90c306d15448)#define ASPEED\_CLK\_YCLK (ASPEED\_CLK\_GRP\_0\_OFFSET + 13)

17

[ 18](ast10x0__clock_8h.md#a52b659f282d1bf17122e8d6cc4cb89ac)#define ASPEED\_CLK\_LCLK (ASPEED\_CLK\_GRP\_1\_OFFSET + 0)

[ 19](ast10x0__clock_8h.md#a601a84a17a471f751ae260374e39d66c)#define ASPEED\_CLK\_ESPI (ASPEED\_CLK\_GRP\_1\_OFFSET + 1)

[ 20](ast10x0__clock_8h.md#a27b8f6c3f72aebbf0559e85bd43e8641)#define ASPEED\_CLK\_REFCLK (ASPEED\_CLK\_GRP\_1\_OFFSET + 2)

21

[ 22](ast10x0__clock_8h.md#a75e3ccf175dbbfd553b0fe4bf4c8b63c)#define ASPEED\_CLK\_LHCCLK (ASPEED\_CLK\_GRP\_1\_OFFSET + 5)

[ 23](ast10x0__clock_8h.md#ab111e4dccb054d2b38c7acdda204ed19)#define ASPEED\_CLK\_RSACLK (ASPEED\_CLK\_GRP\_1\_OFFSET + 6)

24

[ 25](ast10x0__clock_8h.md#a410403d49c1bb708d71bf8247dbdc0e2)#define ASPEED\_CLK\_I3C0 (ASPEED\_CLK\_GRP\_1\_OFFSET + 8)

[ 26](ast10x0__clock_8h.md#ae7e435ba8c54b91d2f0b4d244fe8c052)#define ASPEED\_CLK\_I3C1 (ASPEED\_CLK\_GRP\_1\_OFFSET + 9)

[ 27](ast10x0__clock_8h.md#a1d189580a83d1167491ca053ef22b7fa)#define ASPEED\_CLK\_I3C2 (ASPEED\_CLK\_GRP\_1\_OFFSET + 10)

[ 28](ast10x0__clock_8h.md#a755ef8cfe6c78e01a06113f2b3e78204)#define ASPEED\_CLK\_I3C3 (ASPEED\_CLK\_GRP\_1\_OFFSET + 11)

29

[ 30](ast10x0__clock_8h.md#a3d645146fe6742ed4d56ece6265fc6e2)#define ASPEED\_CLK\_UART1 (ASPEED\_CLK\_GRP\_1\_OFFSET + 16)

[ 31](ast10x0__clock_8h.md#a2c86ad831ad2d720edd3a9c63ad9acb3)#define ASPEED\_CLK\_UART2 (ASPEED\_CLK\_GRP\_1\_OFFSET + 17)

[ 32](ast10x0__clock_8h.md#a8d1afc478750f1746f2bd280ec6aff74)#define ASPEED\_CLK\_UART3 (ASPEED\_CLK\_GRP\_1\_OFFSET + 18)

[ 33](ast10x0__clock_8h.md#a5eb5ae4923c04c925b8763330ead0062)#define ASPEED\_CLK\_UART4 (ASPEED\_CLK\_GRP\_1\_OFFSET + 19)

[ 34](ast10x0__clock_8h.md#ade068404e397460803ec43eac6bf2380)#define ASPEED\_CLK\_MAC (ASPEED\_CLK\_GRP\_1\_OFFSET + 20)

35

[ 36](ast10x0__clock_8h.md#ab834e06518b4054ade5ad5f43971c262)#define ASPEED\_CLK\_UART6 (ASPEED\_CLK\_GRP\_1\_OFFSET + 22)

[ 37](ast10x0__clock_8h.md#a607209d0fc0eae0b7e16f9caf2e9266f)#define ASPEED\_CLK\_UART7 (ASPEED\_CLK\_GRP\_1\_OFFSET + 23)

[ 38](ast10x0__clock_8h.md#adde45b96aa4dfcacfe9830f0d18c08e7)#define ASPEED\_CLK\_UART8 (ASPEED\_CLK\_GRP\_1\_OFFSET + 24)

[ 39](ast10x0__clock_8h.md#a5a99a566a02c34e68a56d2953e885457)#define ASPEED\_CLK\_UART9 (ASPEED\_CLK\_GRP\_1\_OFFSET + 25)

[ 40](ast10x0__clock_8h.md#afc181e59d2e1deca6af256d34d57e25c)#define ASPEED\_CLK\_UART10 (ASPEED\_CLK\_GRP\_1\_OFFSET + 26)

[ 41](ast10x0__clock_8h.md#adbd0d3f7c91d1281e785363095a48077)#define ASPEED\_CLK\_UART11 (ASPEED\_CLK\_GRP\_1\_OFFSET + 27)

[ 42](ast10x0__clock_8h.md#a7d6f4a6d172b574d4a28ff4b6777df69)#define ASPEED\_CLK\_UART12 (ASPEED\_CLK\_GRP\_1\_OFFSET + 28)

[ 43](ast10x0__clock_8h.md#ad2e83af2a4c95f211c9d5f65fb1991d7)#define ASPEED\_CLK\_UART13 (ASPEED\_CLK\_GRP\_1\_OFFSET + 29)

44

[ 45](ast10x0__clock_8h.md#a9f9b71ba0ba43b4cebf27a077fd596ed)#define ASPEED\_CLK\_PCLK (ASPEED\_CLK\_GRP\_2\_OFFSET + 0)

[ 46](ast10x0__clock_8h.md#abc5d16026e5da37c2a09fdef727fe7ce)#define ASPEED\_CLK\_HCLK (ASPEED\_CLK\_GRP\_2\_OFFSET + 1)

[ 47](ast10x0__clock_8h.md#a9a92e4a9a3024f13c9ba2c73a73c2ddb)#define ASPEED\_CLK\_UART5 (ASPEED\_CLK\_GRP\_2\_OFFSET + 2)

48

49#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_AST10X0\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [ast10x0\_clock.h](ast10x0__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
