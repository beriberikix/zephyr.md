---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__rza2m__clock_8h_source.html
original_path: doxygen/html/renesas__rza2m__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rza2m\_clock.h

[Go to the documentation of this file.](renesas__rza2m__clock_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_RZA2M\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_RZA2M\_CLOCK\_H\_

9

[ 10](renesas__rza2m__clock_8h.md#ad913e7ca9a4d51a258b4999ffdeaf0a6)#define RZA2M\_MODULE\_CORESIGHT 1UL

[ 11](renesas__rza2m__clock_8h.md#a0d5d648a96331456fe0396835161132d)#define RZA2M\_MODULE\_OSTM0 2UL

[ 12](renesas__rza2m__clock_8h.md#a582c324d8bde82b09cf776a73646df23)#define RZA2M\_MODULE\_OSTM1 3UL

[ 13](renesas__rza2m__clock_8h.md#aed5e3da53437ae362f406ee4daa59815)#define RZA2M\_MODULE\_OSTM2 4UL

[ 14](renesas__rza2m__clock_8h.md#a50a5ef1e73afdd09911f2efa5bc54ea1)#define RZA2M\_MODULE\_MTU3 5UL

[ 15](renesas__rza2m__clock_8h.md#a010acbedd3ee21d7ebe19ec2390f854b)#define RZA2M\_MODULE\_CANFD 6UL

[ 16](renesas__rza2m__clock_8h.md#af3e603f30ce17e79273682bec286beff)#define RZA2M\_MODULE\_ADC 7UL

[ 17](renesas__rza2m__clock_8h.md#a0db8262a06534defd719aa538d8f6c75)#define RZA2M\_MODULE\_GPT 8UL

[ 18](renesas__rza2m__clock_8h.md#a404e4a90fd2b68f948a7885902a83e6e)#define RZA2M\_MODULE\_SCIFA0 9UL

[ 19](renesas__rza2m__clock_8h.md#a2485a0f2ee28daf0edb9e92019d98679)#define RZA2M\_MODULE\_SCIFA1 10UL

[ 20](renesas__rza2m__clock_8h.md#a5480c3e3eecdb30b1ef42dc4d520a369)#define RZA2M\_MODULE\_SCIFA2 11UL

[ 21](renesas__rza2m__clock_8h.md#a5b1eb164a60e206242b483c0afa8bfc1)#define RZA2M\_MODULE\_SCIFA3 12UL

[ 22](renesas__rza2m__clock_8h.md#a54b05f152b924c2d4c21061c0a2a9ec3)#define RZA2M\_MODULE\_SCIFA4 13UL

[ 23](renesas__rza2m__clock_8h.md#a440435cf25066e90493e013b88876584)#define RZA2M\_MODULE\_SCI0 14UL

[ 24](renesas__rza2m__clock_8h.md#a2bb73224387761644e14a7ec09cdfa31)#define RZA2M\_MODULE\_SCI1 15UL

[ 25](renesas__rza2m__clock_8h.md#af87cbbe8cf64e7304163f08503b1f64d)#define RZA2M\_MODULE\_IrDA 16UL

[ 26](renesas__rza2m__clock_8h.md#ae2dc5389c0b0d611a092b8a7078ff56c)#define RZA2M\_MODULE\_CEU 17UL

[ 27](renesas__rza2m__clock_8h.md#a608d5eaa878c5da023dca1b5421dcae7)#define RZA2M\_MODULE\_RTC0 18UL

[ 28](renesas__rza2m__clock_8h.md#a4b2abc17b5f85e1e68b36998dfae634d)#define RZA2M\_MODULE\_RTC1 19UL

[ 29](renesas__rza2m__clock_8h.md#a3c2761cf0d87aca179655dc38b7174ca)#define RZA2M\_MODULE\_JCU 20UL

[ 30](renesas__rza2m__clock_8h.md#a0d7fa9df9f1a91a7a079c8f583965166)#define RZA2M\_MODULE\_VIN 21UL

[ 31](renesas__rza2m__clock_8h.md#a766c1c63f74f1f71a32bdfd284eb92ef)#define RZA2M\_MODULE\_ETHER 22UL

[ 32](renesas__rza2m__clock_8h.md#acc130aba2677d21ead406cf967a20a9c)#define RZA2M\_MODULE\_USB0 23UL

[ 33](renesas__rza2m__clock_8h.md#a738c68b1d816d6e439fbb2483a179f22)#define RZA2M\_MODULE\_USB1 24UL

[ 34](renesas__rza2m__clock_8h.md#a17147e2fc056e58682488e698dad9154)#define RZA2M\_MODULE\_IMR2 25UL

[ 35](renesas__rza2m__clock_8h.md#ae7ad0a7ba588f298ea0b7c93ff2e23db)#define RZA2M\_MODULE\_DRW 26UL

[ 36](renesas__rza2m__clock_8h.md#af8432bf3e6231702b2d103801d6041e7)#define RZA2M\_MODULE\_MIPI 27UL

[ 37](renesas__rza2m__clock_8h.md#aa19f67d862c578c2c85b41259ef94f73)#define RZA2M\_MODULE\_SSIF0 28UL

[ 38](renesas__rza2m__clock_8h.md#a80181453c9be0e3d66aea1839e2ca711)#define RZA2M\_MODULE\_SSIF1 29UL

[ 39](renesas__rza2m__clock_8h.md#aa0505466fa2f7ae4d0b335f104d7314b)#define RZA2M\_MODULE\_SSIF2 30UL

[ 40](renesas__rza2m__clock_8h.md#af24185872b2e50945a41bb67681437b1)#define RZA2M\_MODULE\_SSIF3 31UL

[ 41](renesas__rza2m__clock_8h.md#abc345e633f717a9a6fdf9c03b580ae61)#define RZA2M\_MODULE\_I2C0 32UL

[ 42](renesas__rza2m__clock_8h.md#a1b3e35de52a53f687a8232d2119dc053)#define RZA2M\_MODULE\_I2C1 33UL

[ 43](renesas__rza2m__clock_8h.md#a94666ff671b49fe996a43e0e6252b504)#define RZA2M\_MODULE\_I2C2 34UL

[ 44](renesas__rza2m__clock_8h.md#a11031c7a706b724517105f2aac4c34ea)#define RZA2M\_MODULE\_I2C3 35UL

[ 45](renesas__rza2m__clock_8h.md#a73b00f18e75f52aaa1e1d62252a19afb)#define RZA2M\_MODULE\_SPIBSC 36UL

[ 46](renesas__rza2m__clock_8h.md#ab6d8dc2deda51355cce66c2cc7834073)#define RZA2M\_MODULE\_VDC6 37UL

[ 47](renesas__rza2m__clock_8h.md#a35b9e44c2b2db08e765dd91fbcf3ae61)#define RZA2M\_MODULE\_RSPI0 38UL

[ 48](renesas__rza2m__clock_8h.md#a4a3163013d049e366d6c3fd828674439)#define RZA2M\_MODULE\_RSPI1 39UL

[ 49](renesas__rza2m__clock_8h.md#a98bc74b2557d704ab33a8575d4915e40)#define RZA2M\_MODULE\_RSPI2 40UL

[ 50](renesas__rza2m__clock_8h.md#a90c1f41aa4bc71594eaf5c7b1c2be75f)#define RZA2M\_MODULE\_HYPERBUS 41UL

[ 51](renesas__rza2m__clock_8h.md#ab7d667e44b3c080868712efc5c2b2487)#define RZA2M\_MODULE\_OCTAMEM 42UL

[ 52](renesas__rza2m__clock_8h.md#a755689015ba0a17d52f43e6d7f992ff9)#define RZA2M\_MODULE\_RSPDIF 43UL

[ 53](renesas__rza2m__clock_8h.md#a32a3fab23c6372734f84baa2b479c0e9)#define RZA2M\_MODULE\_DRP 44UL

[ 54](renesas__rza2m__clock_8h.md#ad152632e6429086f9fcf041bc603425f)#define RZA2M\_MODULE\_TSIP 45UL

[ 55](renesas__rza2m__clock_8h.md#aae0f6a3444ba7e82817dbc4742a53655)#define RZA2M\_MODULE\_NAND 46UL

[ 56](renesas__rza2m__clock_8h.md#a4f416d4e8943198ee7c7bb5df132f703)#define RZA2M\_MODULE\_SDMMC0 47UL

[ 57](renesas__rza2m__clock_8h.md#a6098160614c6c2f80de660a90e883da3)#define RZA2M\_MODULE\_SDMMC1 48UL

58

[ 60](renesas__rza2m__clock_8h.md#a22bf8b9faf6a14aeafee7b9e2a91d9d4)#define RZA2M\_MODULE\_SHIFT 8UL

[ 61](renesas__rza2m__clock_8h.md#a779dc4c8ca1e4dba9f10418924b32db5)#define RZA2M\_CLOCK\_SRC\_SHIFT 0UL

62

[ 63](renesas__rza2m__clock_8h.md#ac29eecb7c5051c1ac11ef54717f8fabe)#define RZA2M\_CLK\_EXTAL 0UL

[ 64](renesas__rza2m__clock_8h.md#af8aa81693c8dea95bbb988bc22db3380)#define RZA2M\_CLK\_I 1UL

[ 65](renesas__rza2m__clock_8h.md#a2e9a523b90878e757c037d9e54500a85)#define RZA2M\_CLK\_G 2UL

[ 66](renesas__rza2m__clock_8h.md#a48a469ebe1fb4316aa06ab1ffd2964e5)#define RZA2M\_CLK\_B 3UL

[ 67](renesas__rza2m__clock_8h.md#ac57acf32507580b6f015d7c30cb833fe)#define RZA2M\_CLK\_P1 4UL

[ 68](renesas__rza2m__clock_8h.md#a908560d73351c416c00d3260cfb88821)#define RZA2M\_CLK\_P1C 4UL

[ 69](renesas__rza2m__clock_8h.md#a6f6b567b212fadd770e99417c20e6be6)#define RZA2M\_CLK\_P0 5UL

70

[ 71](renesas__rza2m__clock_8h.md#a019467d06f81cb91987afe816707c4e0)#define RZA2M\_CLOCK(module, clk) \

72 (((module) << RZA2M\_MODULE\_SHIFT) | ((clk) << RZA2M\_CLOCK\_SRC\_SHIFT))

73

74/\*

75 \* Example: RZA2M\_CLOCK(MODULE\_SCIFA4, RZA2M\_CLK\_P1C) // SCIFA4

76 \*/

77

78#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_RZA2M\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [renesas\_rza2m\_clock.h](renesas__rza2m__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
