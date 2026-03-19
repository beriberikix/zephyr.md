---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas__rzg__clock_8h_source.html
original_path: doxygen/html/renesas__rzg__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rzg\_clock.h

[Go to the documentation of this file.](renesas__rzg__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_RZG\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_RZG\_CLOCK\_H\_

9

[ 11](renesas__rzg__clock_8h.md#af22fb58317528ced8ad8cdfc399ad2ac)#define RZ\_IP\_MASK 0xFF000000UL

[ 12](renesas__rzg__clock_8h.md#a0bfeafa5676753c0e6750a9c3c2f18f1)#define RZ\_IP\_SHIFT 24UL

[ 13](renesas__rzg__clock_8h.md#a73baaadd858826d7b7e613120a9e4509)#define RZ\_IP\_CH\_MASK 0xFF0000UL

[ 14](renesas__rzg__clock_8h.md#a4854f76eb8144726dcc49da30bb49494)#define RZ\_IP\_CH\_SHIFT 16UL

[ 15](renesas__rzg__clock_8h.md#a9712059a7005130fbeb48f2ce7f45f66)#define RZ\_CLOCK\_MASK 0xFF00UL

[ 16](renesas__rzg__clock_8h.md#a0f4444cd8f843699d43be43968a76f60)#define RZ\_CLOCK\_SHIFT 8UL

[ 17](renesas__rzg__clock_8h.md#a68e6f2ee01f4ba23c076f5a0c3574ec3)#define RZ\_CLOCK\_DIV\_MASK 0xFFUL

[ 18](renesas__rzg__clock_8h.md#a2a394bb9c50b68c2c0b4250d529e96fa)#define RZ\_CLOCK\_DIV\_SHIFT 0UL

19

[ 20](renesas__rzg__clock_8h.md#a85c1cd03e46043357e15c2020cf8db25)#define RZ\_IP\_GTM 0UL /\* General Timer \*/

[ 21](renesas__rzg__clock_8h.md#a258d150ad8458cb580f823296dd4b863)#define RZ\_IP\_GPT 1UL /\* General PWM Timer \*/

[ 22](renesas__rzg__clock_8h.md#a4d01bb6e25a7d8f0cc520efd1693f6b0)#define RZ\_IP\_SCIF 2UL /\* Serial Communications Interface with FIFO \*/

[ 23](renesas__rzg__clock_8h.md#a20be7b897467fae2e11d31b9404db77e)#define RZ\_IP\_RIIC 3UL /\* I2C Bus Interface \*/

[ 24](renesas__rzg__clock_8h.md#abe3258c6780f7e818d6a0bfa621c0c39)#define RZ\_IP\_RSPI 4UL /\* Renesas Serial Peripheral Interface \*/

[ 25](renesas__rzg__clock_8h.md#a545f1dab775039d3e00320f4c2fa2266)#define RZ\_IP\_MHU 5UL /\* Message Handling Unit \*/

[ 26](renesas__rzg__clock_8h.md#a6fb0a952bce1f87fdc485e3407885aab)#define RZ\_IP\_DMAC 6UL /\* Direct Memory Access Controller \*/

[ 27](renesas__rzg__clock_8h.md#a2a5b46c7954d9931d05ba9b78b6bfa92)#define RZ\_IP\_CANFD 7UL /\* CANFD Interface (RS-CANFD) \*/

[ 28](renesas__rzg__clock_8h.md#ad6e07b47929a05a957f6685c8207a0d4)#define RZ\_IP\_ADC 8UL /\* A/D Converter \*/

29

[ 30](renesas__rzg__clock_8h.md#a244252c9570d2ce5142a1dacb71aca93)#define RZ\_CLOCK\_ICLK 0UL /\* Cortex-A55 Clock \*/

[ 31](renesas__rzg__clock_8h.md#a9970fbd46cf921c331ad693053100e6f)#define RZ\_CLOCK\_I2CLK 1UL /\* Cortex-M33 Clock \*/

[ 32](renesas__rzg__clock_8h.md#a19ef59ea7eadc3ef12705e6bcd650cfc)#define RZ\_CLOCK\_I3CLK 2UL /\* Cortex-M33 FPU Clock \*/

[ 33](renesas__rzg__clock_8h.md#af7ba3a355a4c56b7c2700d4179bece3f)#define RZ\_CLOCK\_S0CLK 3UL /\* DDR-PHY Clock \*/

[ 34](renesas__rzg__clock_8h.md#a8558bb747c644c3ba838d0b564fef57b)#define RZ\_CLOCK\_OC0CLK 4UL /\* OCTA0 Clock \*/

[ 35](renesas__rzg__clock_8h.md#abe1148e7058c4e6997c83e86470e1784)#define RZ\_CLOCK\_OC1CLK 5UL /\* OCTA1 Clock \*/

[ 36](renesas__rzg__clock_8h.md#ab4e5d3a27f25df5591d3170f2e944e0f)#define RZ\_CLOCK\_SPI0CLK 6UL /\* SPI0 Clock \*/

[ 37](renesas__rzg__clock_8h.md#ab02c603153146d64db7a98b4f332a7d5)#define RZ\_CLOCK\_SPI1CLK 7UL /\* SPI1 Clock \*/

[ 38](renesas__rzg__clock_8h.md#af49247c2ed779dc006ce90a7cdf3a8c1)#define RZ\_CLOCK\_SD0CLK 8UL /\* SDH0 Clock \*/

[ 39](renesas__rzg__clock_8h.md#a17b5762dca74eb50645508737085f6c1)#define RZ\_CLOCK\_SD1CLK 9UL /\* SDH1 Clock \*/

[ 40](renesas__rzg__clock_8h.md#a9b9efa69cb954f3bd2e590974f2f5b68)#define RZ\_CLOCK\_SD2CLK 10UL /\* SDH2 Clock \*/

[ 41](renesas__rzg__clock_8h.md#ab42089566bde80f80a5a672c39f5f4a9)#define RZ\_CLOCK\_M0CLK 11UL /\* VCP LCDC Clock \*/

[ 42](renesas__rzg__clock_8h.md#a357ba27e1964a6f63d756d957213a94d)#define RZ\_CLOCK\_HPCLK 12UL /\* Ethernet Clock \*/

[ 43](renesas__rzg__clock_8h.md#a622f3e70a5fe08a61474322492130319)#define RZ\_CLOCK\_TSUCLK 13UL /\* TSU Clock \*/

[ 44](renesas__rzg__clock_8h.md#a67327a7c0fcff2dc0374a0fbde6422c6)#define RZ\_CLOCK\_ZTCLK 14UL /\* JAUTH Clock \*/

[ 45](renesas__rzg__clock_8h.md#a43f77faab57d93e59c93956572ed73a5)#define RZ\_CLOCK\_P0CLK 15UL /\* APB-BUS Clock \*/

[ 46](renesas__rzg__clock_8h.md#a960f074fd0a8e9ea8c5b02a4d6d977c9)#define RZ\_CLOCK\_P1CLK 16UL /\* AXI-BUS Clock \*/

[ 47](renesas__rzg__clock_8h.md#a794d8d5f1cb8a2df70ca2ab4caf2b049)#define RZ\_CLOCK\_P2CLK 17UL /\* P2CLK \*/

[ 48](renesas__rzg__clock_8h.md#a2dbb22921c00fb5398666f595da080d9)#define RZ\_CLOCK\_P3CLK 18UL /\* P3CLK \*/

[ 49](renesas__rzg__clock_8h.md#a3e09739b70bf6fbcd7cb3a72002c0339)#define RZ\_CLOCK\_P4CLK 19UL /\* P4CLK \*/

[ 50](renesas__rzg__clock_8h.md#a764d5d9af4b6ef76a903f93f15f53b74)#define RZ\_CLOCK\_P5CLK 20UL /\* P5CLK \*/

[ 51](renesas__rzg__clock_8h.md#a7b51d8e0e38165e26975696bf90d834b)#define RZ\_CLOCK\_ATCLK 21UL /\* ATCLK \*/

[ 52](renesas__rzg__clock_8h.md#a800d72bacbe85d766ed0e027b28b36c8)#define RZ\_CLOCK\_OSCCLK 22UL /\* OSC Clock \*/

[ 53](renesas__rzg__clock_8h.md#a4811a342819ebdb27d9ad77aa3bfc48e)#define RZ\_CLOCK\_OSCCLK2 23UL /\* OSC2 Clock \*/

54

[ 55](renesas__rzg__clock_8h.md#af2b6678567dacec847501d2a634b7773)#define RZ\_CLOCK(IP, ch, clk, div) \

56 ((RZ\_IP\_##IP << RZ\_IP\_SHIFT) | ((ch) << RZ\_IP\_CH\_SHIFT) | ((clk) << RZ\_CLOCK\_SHIFT) | \

57 ((div) << RZ\_CLOCK\_DIV\_SHIFT))

58

65

66/\* SCIF \*/

[ 67](renesas__rzg__clock_8h.md#ab5ba6102fd209a05b2a5cce69874594a)#define RZ\_CLOCK\_SCIF(ch) RZ\_CLOCK(SCIF, ch, RZ\_CLOCK\_P0CLK, 1)

68

69/\* GPT \*/

[ 70](renesas__rzg__clock_8h.md#adda08ff063353c356bae99dada0352c8)#define RZ\_CLOCK\_GPT(ch) RZ\_CLOCK(GPT, ch, RZ\_CLOCK\_P0CLK, 1)

71

72/\* MHU \*/

[ 73](renesas__rzg__clock_8h.md#ab7297a9bbf3181ab73f1ea0e2c67decd)#define RZ\_CLOCK\_MHU(ch) RZ\_CLOCK(MHU, ch, RZ\_CLOCK\_P1CLK, 2)

74

75/\* ADC \*/

[ 76](renesas__rzg__clock_8h.md#aabe15d33711286e3c8a9a99774afffc4)#define RZ\_CLOCK\_ADC(ch) RZ\_CLOCK(ADC, ch, RZ\_CLOCK\_TSUCLK, 1)

77

78/\* RIIC \*/

[ 79](renesas__rzg__clock_8h.md#ae138403b21ab0a308312072d1ffa06f1)#define RZ\_CLOCK\_RIIC(ch) RZ\_CLOCK(RIIC, ch, RZ\_CLOCK\_P0CLK, 1)

80

81/\* GTM \*/

[ 82](renesas__rzg__clock_8h.md#a435c6e38774d8d95067cb4e7513dd74d)#define RZ\_CLOCK\_GTM(ch) RZ\_CLOCK(GTM, ch, RZ\_CLOCK\_P0CLK, 1)

83

84/\* CAN \*/

[ 85](renesas__rzg__clock_8h.md#a637295af9157f6757bed145911ca2a3a)#define RZ\_CLOCK\_CANFD(ch) RZ\_CLOCK(CANFD, ch, RZ\_CLOCK\_P4CLK, 2)

86

87/\* RSPI \*/

[ 88](renesas__rzg__clock_8h.md#a566a4e447745ff7d5ed3b4d0dd0fa666)#define RZ\_CLOCK\_RSPI(ch) RZ\_CLOCK(RSPI, ch, RZ\_CLOCK\_P0CLK, 1)

89

90/\* DMAC \*/

[ 91](renesas__rzg__clock_8h.md#a3a3baef1dbd6eae8f7d54a0610521aa0)#define RZ\_CLOCK\_DMAC(ch) RZ\_CLOCK(DMAC, ch, RZ\_CLOCK\_P3CLK, 1)

92

93#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_RZG\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [renesas\_rzg\_clock.h](renesas__rzg__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
