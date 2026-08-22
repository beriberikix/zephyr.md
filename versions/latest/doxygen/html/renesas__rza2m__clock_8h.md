---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__rza2m__clock_8h.html
original_path: doxygen/html/renesas__rza2m__clock_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rza2m\_clock.h File Reference

[Go to the source code of this file.](renesas__rza2m__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZA2M\_MODULE\_CORESIGHT](#ad913e7ca9a4d51a258b4999ffdeaf0a6)   1UL |
| #define | [RZA2M\_MODULE\_OSTM0](#a0d5d648a96331456fe0396835161132d)   2UL |
| #define | [RZA2M\_MODULE\_OSTM1](#a582c324d8bde82b09cf776a73646df23)   3UL |
| #define | [RZA2M\_MODULE\_OSTM2](#aed5e3da53437ae362f406ee4daa59815)   4UL |
| #define | [RZA2M\_MODULE\_MTU3](#a50a5ef1e73afdd09911f2efa5bc54ea1)   5UL |
| #define | [RZA2M\_MODULE\_CANFD](#a010acbedd3ee21d7ebe19ec2390f854b)   6UL |
| #define | [RZA2M\_MODULE\_ADC](#af3e603f30ce17e79273682bec286beff)   7UL |
| #define | [RZA2M\_MODULE\_GPT](#a0db8262a06534defd719aa538d8f6c75)   8UL |
| #define | [RZA2M\_MODULE\_SCIFA0](#a404e4a90fd2b68f948a7885902a83e6e)   9UL |
| #define | [RZA2M\_MODULE\_SCIFA1](#a2485a0f2ee28daf0edb9e92019d98679)   10UL |
| #define | [RZA2M\_MODULE\_SCIFA2](#a5480c3e3eecdb30b1ef42dc4d520a369)   11UL |
| #define | [RZA2M\_MODULE\_SCIFA3](#a5b1eb164a60e206242b483c0afa8bfc1)   12UL |
| #define | [RZA2M\_MODULE\_SCIFA4](#a54b05f152b924c2d4c21061c0a2a9ec3)   13UL |
| #define | [RZA2M\_MODULE\_SCI0](#a440435cf25066e90493e013b88876584)   14UL |
| #define | [RZA2M\_MODULE\_SCI1](#a2bb73224387761644e14a7ec09cdfa31)   15UL |
| #define | [RZA2M\_MODULE\_IrDA](#af87cbbe8cf64e7304163f08503b1f64d)   16UL |
| #define | [RZA2M\_MODULE\_CEU](#ae2dc5389c0b0d611a092b8a7078ff56c)   17UL |
| #define | [RZA2M\_MODULE\_RTC0](#a608d5eaa878c5da023dca1b5421dcae7)   18UL |
| #define | [RZA2M\_MODULE\_RTC1](#a4b2abc17b5f85e1e68b36998dfae634d)   19UL |
| #define | [RZA2M\_MODULE\_JCU](#a3c2761cf0d87aca179655dc38b7174ca)   20UL |
| #define | [RZA2M\_MODULE\_VIN](#a0d7fa9df9f1a91a7a079c8f583965166)   21UL |
| #define | [RZA2M\_MODULE\_ETHER](#a766c1c63f74f1f71a32bdfd284eb92ef)   22UL |
| #define | [RZA2M\_MODULE\_USB0](#acc130aba2677d21ead406cf967a20a9c)   23UL |
| #define | [RZA2M\_MODULE\_USB1](#a738c68b1d816d6e439fbb2483a179f22)   24UL |
| #define | [RZA2M\_MODULE\_IMR2](#a17147e2fc056e58682488e698dad9154)   25UL |
| #define | [RZA2M\_MODULE\_DRW](#ae7ad0a7ba588f298ea0b7c93ff2e23db)   26UL |
| #define | [RZA2M\_MODULE\_MIPI](#af8432bf3e6231702b2d103801d6041e7)   27UL |
| #define | [RZA2M\_MODULE\_SSIF0](#aa19f67d862c578c2c85b41259ef94f73)   28UL |
| #define | [RZA2M\_MODULE\_SSIF1](#a80181453c9be0e3d66aea1839e2ca711)   29UL |
| #define | [RZA2M\_MODULE\_SSIF2](#aa0505466fa2f7ae4d0b335f104d7314b)   30UL |
| #define | [RZA2M\_MODULE\_SSIF3](#af24185872b2e50945a41bb67681437b1)   31UL |
| #define | [RZA2M\_MODULE\_I2C0](#abc345e633f717a9a6fdf9c03b580ae61)   32UL |
| #define | [RZA2M\_MODULE\_I2C1](#a1b3e35de52a53f687a8232d2119dc053)   33UL |
| #define | [RZA2M\_MODULE\_I2C2](#a94666ff671b49fe996a43e0e6252b504)   34UL |
| #define | [RZA2M\_MODULE\_I2C3](#a11031c7a706b724517105f2aac4c34ea)   35UL |
| #define | [RZA2M\_MODULE\_SPIBSC](#a73b00f18e75f52aaa1e1d62252a19afb)   36UL |
| #define | [RZA2M\_MODULE\_VDC6](#ab6d8dc2deda51355cce66c2cc7834073)   37UL |
| #define | [RZA2M\_MODULE\_RSPI0](#a35b9e44c2b2db08e765dd91fbcf3ae61)   38UL |
| #define | [RZA2M\_MODULE\_RSPI1](#a4a3163013d049e366d6c3fd828674439)   39UL |
| #define | [RZA2M\_MODULE\_RSPI2](#a98bc74b2557d704ab33a8575d4915e40)   40UL |
| #define | [RZA2M\_MODULE\_HYPERBUS](#a90c1f41aa4bc71594eaf5c7b1c2be75f)   41UL |
| #define | [RZA2M\_MODULE\_OCTAMEM](#ab7d667e44b3c080868712efc5c2b2487)   42UL |
| #define | [RZA2M\_MODULE\_RSPDIF](#a755689015ba0a17d52f43e6d7f992ff9)   43UL |
| #define | [RZA2M\_MODULE\_DRP](#a32a3fab23c6372734f84baa2b479c0e9)   44UL |
| #define | [RZA2M\_MODULE\_TSIP](#ad152632e6429086f9fcf041bc603425f)   45UL |
| #define | [RZA2M\_MODULE\_NAND](#aae0f6a3444ba7e82817dbc4742a53655)   46UL |
| #define | [RZA2M\_MODULE\_SDMMC0](#a4f416d4e8943198ee7c7bb5df132f703)   47UL |
| #define | [RZA2M\_MODULE\_SDMMC1](#a6098160614c6c2f80de660a90e883da3)   48UL |
| #define | [RZA2M\_MODULE\_SHIFT](#a22bf8b9faf6a14aeafee7b9e2a91d9d4)   8UL |
|  | RZ/A2M clock configuration values. |
| #define | [RZA2M\_CLOCK\_SRC\_SHIFT](#a779dc4c8ca1e4dba9f10418924b32db5)   0UL |
| #define | [RZA2M\_CLK\_EXTAL](#ac29eecb7c5051c1ac11ef54717f8fabe)   0UL |
| #define | [RZA2M\_CLK\_I](#af8aa81693c8dea95bbb988bc22db3380)   1UL |
| #define | [RZA2M\_CLK\_G](#a2e9a523b90878e757c037d9e54500a85)   2UL |
| #define | [RZA2M\_CLK\_B](#a48a469ebe1fb4316aa06ab1ffd2964e5)   3UL |
| #define | [RZA2M\_CLK\_P1](#ac57acf32507580b6f015d7c30cb833fe)   4UL |
| #define | [RZA2M\_CLK\_P1C](#a908560d73351c416c00d3260cfb88821)   4UL |
| #define | [RZA2M\_CLK\_P0](#a6f6b567b212fadd770e99417c20e6be6)   5UL |
| #define | [RZA2M\_CLOCK](#a019467d06f81cb91987afe816707c4e0)(module, clk) |

## Macro Definition Documentation

## [◆ ](#a48a469ebe1fb4316aa06ab1ffd2964e5)RZA2M\_CLK\_B

| #define RZA2M\_CLK\_B   3UL |
| --- |

## [◆ ](#ac29eecb7c5051c1ac11ef54717f8fabe)RZA2M\_CLK\_EXTAL

| #define RZA2M\_CLK\_EXTAL   0UL |
| --- |

## [◆ ](#a2e9a523b90878e757c037d9e54500a85)RZA2M\_CLK\_G

| #define RZA2M\_CLK\_G   2UL |
| --- |

## [◆ ](#af8aa81693c8dea95bbb988bc22db3380)RZA2M\_CLK\_I

| #define RZA2M\_CLK\_I   1UL |
| --- |

## [◆ ](#a6f6b567b212fadd770e99417c20e6be6)RZA2M\_CLK\_P0

| #define RZA2M\_CLK\_P0   5UL |
| --- |

## [◆ ](#ac57acf32507580b6f015d7c30cb833fe)RZA2M\_CLK\_P1

| #define RZA2M\_CLK\_P1   4UL |
| --- |

## [◆ ](#a908560d73351c416c00d3260cfb88821)RZA2M\_CLK\_P1C

| #define RZA2M\_CLK\_P1C   4UL |
| --- |

## [◆ ](#a019467d06f81cb91987afe816707c4e0)RZA2M\_CLOCK

| #define RZA2M\_CLOCK | ( |  | *module*, |
| --- | --- | --- | --- |
|  |  |  | *clk* ) |

**Value:**

(((module) << [RZA2M\_MODULE\_SHIFT](#a22bf8b9faf6a14aeafee7b9e2a91d9d4)) | ((clk) << [RZA2M\_CLOCK\_SRC\_SHIFT](#a779dc4c8ca1e4dba9f10418924b32db5)))

[RZA2M\_MODULE\_SHIFT](#a22bf8b9faf6a14aeafee7b9e2a91d9d4)

#define RZA2M\_MODULE\_SHIFT

RZ/A2M clock configuration values.

**Definition** renesas\_rza2m\_clock.h:60

[RZA2M\_CLOCK\_SRC\_SHIFT](#a779dc4c8ca1e4dba9f10418924b32db5)

#define RZA2M\_CLOCK\_SRC\_SHIFT

**Definition** renesas\_rza2m\_clock.h:61

## [◆ ](#a779dc4c8ca1e4dba9f10418924b32db5)RZA2M\_CLOCK\_SRC\_SHIFT

| #define RZA2M\_CLOCK\_SRC\_SHIFT   0UL |
| --- |

## [◆ ](#af3e603f30ce17e79273682bec286beff)RZA2M\_MODULE\_ADC

| #define RZA2M\_MODULE\_ADC   7UL |
| --- |

## [◆ ](#a010acbedd3ee21d7ebe19ec2390f854b)RZA2M\_MODULE\_CANFD

| #define RZA2M\_MODULE\_CANFD   6UL |
| --- |

## [◆ ](#ae2dc5389c0b0d611a092b8a7078ff56c)RZA2M\_MODULE\_CEU

| #define RZA2M\_MODULE\_CEU   17UL |
| --- |

## [◆ ](#ad913e7ca9a4d51a258b4999ffdeaf0a6)RZA2M\_MODULE\_CORESIGHT

| #define RZA2M\_MODULE\_CORESIGHT   1UL |
| --- |

## [◆ ](#a32a3fab23c6372734f84baa2b479c0e9)RZA2M\_MODULE\_DRP

| #define RZA2M\_MODULE\_DRP   44UL |
| --- |

## [◆ ](#ae7ad0a7ba588f298ea0b7c93ff2e23db)RZA2M\_MODULE\_DRW

| #define RZA2M\_MODULE\_DRW   26UL |
| --- |

## [◆ ](#a766c1c63f74f1f71a32bdfd284eb92ef)RZA2M\_MODULE\_ETHER

| #define RZA2M\_MODULE\_ETHER   22UL |
| --- |

## [◆ ](#a0db8262a06534defd719aa538d8f6c75)RZA2M\_MODULE\_GPT

| #define RZA2M\_MODULE\_GPT   8UL |
| --- |

## [◆ ](#a90c1f41aa4bc71594eaf5c7b1c2be75f)RZA2M\_MODULE\_HYPERBUS

| #define RZA2M\_MODULE\_HYPERBUS   41UL |
| --- |

## [◆ ](#abc345e633f717a9a6fdf9c03b580ae61)RZA2M\_MODULE\_I2C0

| #define RZA2M\_MODULE\_I2C0   32UL |
| --- |

## [◆ ](#a1b3e35de52a53f687a8232d2119dc053)RZA2M\_MODULE\_I2C1

| #define RZA2M\_MODULE\_I2C1   33UL |
| --- |

## [◆ ](#a94666ff671b49fe996a43e0e6252b504)RZA2M\_MODULE\_I2C2

| #define RZA2M\_MODULE\_I2C2   34UL |
| --- |

## [◆ ](#a11031c7a706b724517105f2aac4c34ea)RZA2M\_MODULE\_I2C3

| #define RZA2M\_MODULE\_I2C3   35UL |
| --- |

## [◆ ](#a17147e2fc056e58682488e698dad9154)RZA2M\_MODULE\_IMR2

| #define RZA2M\_MODULE\_IMR2   25UL |
| --- |

## [◆ ](#af87cbbe8cf64e7304163f08503b1f64d)RZA2M\_MODULE\_IrDA

| #define RZA2M\_MODULE\_IrDA   16UL |
| --- |

## [◆ ](#a3c2761cf0d87aca179655dc38b7174ca)RZA2M\_MODULE\_JCU

| #define RZA2M\_MODULE\_JCU   20UL |
| --- |

## [◆ ](#af8432bf3e6231702b2d103801d6041e7)RZA2M\_MODULE\_MIPI

| #define RZA2M\_MODULE\_MIPI   27UL |
| --- |

## [◆ ](#a50a5ef1e73afdd09911f2efa5bc54ea1)RZA2M\_MODULE\_MTU3

| #define RZA2M\_MODULE\_MTU3   5UL |
| --- |

## [◆ ](#aae0f6a3444ba7e82817dbc4742a53655)RZA2M\_MODULE\_NAND

| #define RZA2M\_MODULE\_NAND   46UL |
| --- |

## [◆ ](#ab7d667e44b3c080868712efc5c2b2487)RZA2M\_MODULE\_OCTAMEM

| #define RZA2M\_MODULE\_OCTAMEM   42UL |
| --- |

## [◆ ](#a0d5d648a96331456fe0396835161132d)RZA2M\_MODULE\_OSTM0

| #define RZA2M\_MODULE\_OSTM0   2UL |
| --- |

## [◆ ](#a582c324d8bde82b09cf776a73646df23)RZA2M\_MODULE\_OSTM1

| #define RZA2M\_MODULE\_OSTM1   3UL |
| --- |

## [◆ ](#aed5e3da53437ae362f406ee4daa59815)RZA2M\_MODULE\_OSTM2

| #define RZA2M\_MODULE\_OSTM2   4UL |
| --- |

## [◆ ](#a755689015ba0a17d52f43e6d7f992ff9)RZA2M\_MODULE\_RSPDIF

| #define RZA2M\_MODULE\_RSPDIF   43UL |
| --- |

## [◆ ](#a35b9e44c2b2db08e765dd91fbcf3ae61)RZA2M\_MODULE\_RSPI0

| #define RZA2M\_MODULE\_RSPI0   38UL |
| --- |

## [◆ ](#a4a3163013d049e366d6c3fd828674439)RZA2M\_MODULE\_RSPI1

| #define RZA2M\_MODULE\_RSPI1   39UL |
| --- |

## [◆ ](#a98bc74b2557d704ab33a8575d4915e40)RZA2M\_MODULE\_RSPI2

| #define RZA2M\_MODULE\_RSPI2   40UL |
| --- |

## [◆ ](#a608d5eaa878c5da023dca1b5421dcae7)RZA2M\_MODULE\_RTC0

| #define RZA2M\_MODULE\_RTC0   18UL |
| --- |

## [◆ ](#a4b2abc17b5f85e1e68b36998dfae634d)RZA2M\_MODULE\_RTC1

| #define RZA2M\_MODULE\_RTC1   19UL |
| --- |

## [◆ ](#a440435cf25066e90493e013b88876584)RZA2M\_MODULE\_SCI0

| #define RZA2M\_MODULE\_SCI0   14UL |
| --- |

## [◆ ](#a2bb73224387761644e14a7ec09cdfa31)RZA2M\_MODULE\_SCI1

| #define RZA2M\_MODULE\_SCI1   15UL |
| --- |

## [◆ ](#a404e4a90fd2b68f948a7885902a83e6e)RZA2M\_MODULE\_SCIFA0

| #define RZA2M\_MODULE\_SCIFA0   9UL |
| --- |

## [◆ ](#a2485a0f2ee28daf0edb9e92019d98679)RZA2M\_MODULE\_SCIFA1

| #define RZA2M\_MODULE\_SCIFA1   10UL |
| --- |

## [◆ ](#a5480c3e3eecdb30b1ef42dc4d520a369)RZA2M\_MODULE\_SCIFA2

| #define RZA2M\_MODULE\_SCIFA2   11UL |
| --- |

## [◆ ](#a5b1eb164a60e206242b483c0afa8bfc1)RZA2M\_MODULE\_SCIFA3

| #define RZA2M\_MODULE\_SCIFA3   12UL |
| --- |

## [◆ ](#a54b05f152b924c2d4c21061c0a2a9ec3)RZA2M\_MODULE\_SCIFA4

| #define RZA2M\_MODULE\_SCIFA4   13UL |
| --- |

## [◆ ](#a4f416d4e8943198ee7c7bb5df132f703)RZA2M\_MODULE\_SDMMC0

| #define RZA2M\_MODULE\_SDMMC0   47UL |
| --- |

## [◆ ](#a6098160614c6c2f80de660a90e883da3)RZA2M\_MODULE\_SDMMC1

| #define RZA2M\_MODULE\_SDMMC1   48UL |
| --- |

## [◆ ](#a22bf8b9faf6a14aeafee7b9e2a91d9d4)RZA2M\_MODULE\_SHIFT

| #define RZA2M\_MODULE\_SHIFT   8UL |
| --- |

RZ/A2M clock configuration values.

## [◆ ](#a73b00f18e75f52aaa1e1d62252a19afb)RZA2M\_MODULE\_SPIBSC

| #define RZA2M\_MODULE\_SPIBSC   36UL |
| --- |

## [◆ ](#aa19f67d862c578c2c85b41259ef94f73)RZA2M\_MODULE\_SSIF0

| #define RZA2M\_MODULE\_SSIF0   28UL |
| --- |

## [◆ ](#a80181453c9be0e3d66aea1839e2ca711)RZA2M\_MODULE\_SSIF1

| #define RZA2M\_MODULE\_SSIF1   29UL |
| --- |

## [◆ ](#aa0505466fa2f7ae4d0b335f104d7314b)RZA2M\_MODULE\_SSIF2

| #define RZA2M\_MODULE\_SSIF2   30UL |
| --- |

## [◆ ](#af24185872b2e50945a41bb67681437b1)RZA2M\_MODULE\_SSIF3

| #define RZA2M\_MODULE\_SSIF3   31UL |
| --- |

## [◆ ](#ad152632e6429086f9fcf041bc603425f)RZA2M\_MODULE\_TSIP

| #define RZA2M\_MODULE\_TSIP   45UL |
| --- |

## [◆ ](#acc130aba2677d21ead406cf967a20a9c)RZA2M\_MODULE\_USB0

| #define RZA2M\_MODULE\_USB0   23UL |
| --- |

## [◆ ](#a738c68b1d816d6e439fbb2483a179f22)RZA2M\_MODULE\_USB1

| #define RZA2M\_MODULE\_USB1   24UL |
| --- |

## [◆ ](#ab6d8dc2deda51355cce66c2cc7834073)RZA2M\_MODULE\_VDC6

| #define RZA2M\_MODULE\_VDC6   37UL |
| --- |

## [◆ ](#a0d7fa9df9f1a91a7a079c8f583965166)RZA2M\_MODULE\_VIN

| #define RZA2M\_MODULE\_VIN   21UL |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [renesas\_rza2m\_clock.h](renesas__rza2m__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
