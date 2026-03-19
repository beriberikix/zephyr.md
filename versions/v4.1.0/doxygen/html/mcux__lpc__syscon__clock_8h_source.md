---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mcux__lpc__syscon__clock_8h_source.html
original_path: doxygen/html/mcux__lpc__syscon__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_lpc\_syscon\_clock.h

[Go to the documentation of this file.](mcux__lpc__syscon__clock_8h.md)

1/\*

2 \* Copyright 2020-2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCUX\_LPC\_SYSCON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCUX\_LPC\_SYSCON\_H\_

9

10/\* Note- clock identifiers in this file must be unique,

11 \* as the driver uses them in a switch case

12 \*/

13

[ 14](mcux__lpc__syscon__clock_8h.md#ae88d17964b48b5a76be33cf697a88d8f)#define MCUX\_LPC\_CLK\_ID(high, low) ((high << 8) | (low))

15

16/\* These IDs are used within SOC macros, and thus cannot be defined

17 \* using the standard MCUX\_LPC\_CLK\_ID form

18 \*/

[ 19](mcux__lpc__syscon__clock_8h.md#a29436fa81a77c707ca9c08a42a301019)#define MCUX\_CTIMER0\_CLK 0

[ 20](mcux__lpc__syscon__clock_8h.md#a813bc9c11cded4fa7abda6fa3ac33bf2)#define MCUX\_CTIMER1\_CLK 1

[ 21](mcux__lpc__syscon__clock_8h.md#a4f142a3a6cf54650c0a9c1510d078e59)#define MCUX\_CTIMER2\_CLK 2

[ 22](mcux__lpc__syscon__clock_8h.md#aa8835aa87fd2ce75ea4a734c0f9dcf61)#define MCUX\_CTIMER3\_CLK 3

[ 23](mcux__lpc__syscon__clock_8h.md#a0cd96aaaf82fd1acba2c8e24914547a1)#define MCUX\_CTIMER4\_CLK 4

[ 24](mcux__lpc__syscon__clock_8h.md#a3f397098d6cb8fc9f73832a4d8216dfd)#define MCUX\_CTIMER5\_CLK 5

[ 25](mcux__lpc__syscon__clock_8h.md#a72d0a769edd497c3e426efd60025d749)#define MCUX\_CTIMER6\_CLK 6

[ 26](mcux__lpc__syscon__clock_8h.md#aa3ed8805e53845ae8fd832c7f02ce406)#define MCUX\_CTIMER7\_CLK 7

27

[ 28](mcux__lpc__syscon__clock_8h.md#a0131126fce0a606a4d1ade85654bb61a)#define MCUX\_FLEXCOMM0\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x00)

[ 29](mcux__lpc__syscon__clock_8h.md#a94328a748738aa7599c54178320a4270)#define MCUX\_FLEXCOMM1\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x01)

[ 30](mcux__lpc__syscon__clock_8h.md#ac7b838481b0c3e22ea0c73cc20649261)#define MCUX\_FLEXCOMM2\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x02)

[ 31](mcux__lpc__syscon__clock_8h.md#a81d32a4628c73ae2cff0c7083269adb3)#define MCUX\_FLEXCOMM3\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x03)

[ 32](mcux__lpc__syscon__clock_8h.md#aae97de225885a02eaf43c02bdb63a0f7)#define MCUX\_FLEXCOMM4\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x04)

[ 33](mcux__lpc__syscon__clock_8h.md#aea277f7f67bc9cfaa9fce0c6028a7ffb)#define MCUX\_FLEXCOMM5\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x05)

[ 34](mcux__lpc__syscon__clock_8h.md#ada5a860ef2da608f969b9efcbc17f2c7)#define MCUX\_FLEXCOMM6\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x06)

[ 35](mcux__lpc__syscon__clock_8h.md#abd3d4114d1d3214eb08513ea3a8b904b)#define MCUX\_FLEXCOMM7\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x07)

[ 36](mcux__lpc__syscon__clock_8h.md#a4db5314db3735bd28e4742e37b703cf1)#define MCUX\_FLEXCOMM8\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x08)

[ 37](mcux__lpc__syscon__clock_8h.md#ad3931251f9e41dfb1529c784b25e52f7)#define MCUX\_FLEXCOMM9\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x09)

[ 38](mcux__lpc__syscon__clock_8h.md#a27e647672c88a6cdf3dce2a1918e3745)#define MCUX\_FLEXCOMM10\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0A)

[ 39](mcux__lpc__syscon__clock_8h.md#a3cc7e2a23e06ed72cb5fc267dc0bbd8a)#define MCUX\_FLEXCOMM11\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0B)

[ 40](mcux__lpc__syscon__clock_8h.md#a69bbe063f4e3a961d7cf5818e4538e09)#define MCUX\_FLEXCOMM12\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0C)

[ 41](mcux__lpc__syscon__clock_8h.md#ad70ee63f0f119911b8d2b3ecf57c4dea)#define MCUX\_FLEXCOMM13\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0D)

[ 42](mcux__lpc__syscon__clock_8h.md#ace02fa0f8524187210a42b35cc81b3b4)#define MCUX\_HS\_SPI\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0E)

[ 43](mcux__lpc__syscon__clock_8h.md#a0b68c4607dfc6a6b8cd172c14b641515)#define MCUX\_FLEXCOMM14\_CLK MCUX\_HS\_SPI\_CLK

[ 44](mcux__lpc__syscon__clock_8h.md#afd7c883dfbd0d6f45c0dda39fb454c3c)#define MCUX\_PMIC\_I2C\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0F)

[ 45](mcux__lpc__syscon__clock_8h.md#a79a1c0861f807daa840d8f2cb7884888)#define MCUX\_HS\_SPI1\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x10)

[ 46](mcux__lpc__syscon__clock_8h.md#abd05ff52d1547abbbb53a27a8931d28c)#define MCUX\_FLEXCOMM17\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x11)

[ 47](mcux__lpc__syscon__clock_8h.md#a9d374131aea6a92415b9af4bf3d748b0)#define MCUX\_FLEXCOMM18\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x12)

[ 48](mcux__lpc__syscon__clock_8h.md#a7ff5d4412485aa034334c8296f417435)#define MCUX\_FLEXCOMM19\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x13)

[ 49](mcux__lpc__syscon__clock_8h.md#a82bdcc56f9fd6ae50cd42da5ee3cb252)#define MCUX\_FLEXCOMM20\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x14)

50/\* On RT7xx, flexcomm14 and 16 only can be LPSPI, flexcomm15 only can be I2C. \*/

[ 51](mcux__lpc__syscon__clock_8h.md#af017a01382113ea8c4b0d241b45a5843)#define MCUX\_LPSPI14\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x24)

[ 52](mcux__lpc__syscon__clock_8h.md#a93c91ed481c6029670f11b47ffa3bce0)#define MCUX\_LPI2C15\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x25)

[ 53](mcux__lpc__syscon__clock_8h.md#a3490429ebd674b0da98aa8c91a92c195)#define MCUX\_LPSPI16\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x26)

[ 54](mcux__lpc__syscon__clock_8h.md#af75d628dbb0a7721ad41e975149ac933)#define MCUX\_USDHC1\_CLK MCUX\_LPC\_CLK\_ID(0x02, 0x00)

[ 55](mcux__lpc__syscon__clock_8h.md#a035029233e88559d5cc8c278f57f2327)#define MCUX\_USDHC2\_CLK MCUX\_LPC\_CLK\_ID(0x02, 0x01)

56

[ 57](mcux__lpc__syscon__clock_8h.md#afe9d906202d3e843dcfc340e4bb65571)#define MCUX\_MCAN\_CLK MCUX\_LPC\_CLK\_ID(0x03, 0x00)

58

[ 59](mcux__lpc__syscon__clock_8h.md#aa13d3e469489fcb89348867a8cacdb3e)#define MCUX\_BUS\_CLK MCUX\_LPC\_CLK\_ID(0x04, 0x00)

60

[ 61](mcux__lpc__syscon__clock_8h.md#aecd4904bd578ff819e6e871aecc438b5)#define MCUX\_SDIF\_CLK MCUX\_LPC\_CLK\_ID(0x05, 0x00)

62

[ 63](mcux__lpc__syscon__clock_8h.md#aefcdabc53569382c9f01f481eec4a6d2)#define MCUX\_I3C\_CLK MCUX\_LPC\_CLK\_ID(0x06, 0x00)

[ 64](mcux__lpc__syscon__clock_8h.md#a5042a2326e8b6c7ed5d751362fb26454)#define MCUX\_I3C2\_CLK MCUX\_LPC\_CLK\_ID(0x06, 0x01)

65

[ 66](mcux__lpc__syscon__clock_8h.md#afd1ed6a3c1c3b3c8f96ca2bc55a6d20c)#define MCUX\_MIPI\_DSI\_DPHY\_CLK MCUX\_LPC\_CLK\_ID(0x07, 0x00)

[ 67](mcux__lpc__syscon__clock_8h.md#a182f8126cae1792c3c8e4c1a81f13fda)#define MCUX\_MIPI\_DSI\_ESC\_CLK MCUX\_LPC\_CLK\_ID(0x07, 0x01)

68

[ 69](mcux__lpc__syscon__clock_8h.md#a1b3db2423ad6e3c7dfc3943756fa0cb7)#define MCUX\_LCDIF\_PIXEL\_CLK MCUX\_LPC\_CLK\_ID(0x08, 0x00)

70

[ 71](mcux__lpc__syscon__clock_8h.md#a9eda466db2baa4c504798e0878a3ef48)#define MCUX\_SCTIMER\_CLK MCUX\_LPC\_CLK\_ID(0x09, 0x00)

72

[ 73](mcux__lpc__syscon__clock_8h.md#a161ba4b82b6a6423afd54b334d22ecdf)#define MCUX\_DMIC\_CLK MCUX\_LPC\_CLK\_ID(0x0A, 0x00)

74

[ 75](mcux__lpc__syscon__clock_8h.md#a5afbfb7ac6f3da817ab539112a951e4e)#define MCUX\_FLEXSPI\_CLK MCUX\_LPC\_CLK\_ID(0x0A, 0x00)

[ 76](mcux__lpc__syscon__clock_8h.md#a53c6b6b4fd0ca41960a831dc752e7d5f)#define MCUX\_FLEXSPI2\_CLK MCUX\_LPC\_CLK\_ID(0x0A, 0x01)

77

[ 78](mcux__lpc__syscon__clock_8h.md#a158d5ef92e191535e5170dffbea757fc)#define MCUX\_MRT\_CLK MCUX\_LPC\_CLK\_ID(0x0B, 0x00)

[ 79](mcux__lpc__syscon__clock_8h.md#a8f064dcf75db9a88930a09f8f100c0fd)#define MCUX\_FREEMRT\_CLK MCUX\_LPC\_CLK\_ID(0x0B, 0x01)

80

[ 81](mcux__lpc__syscon__clock_8h.md#a6c42df5400351c99bd761db7370951d9)#define MCUX\_PORT0\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x00)

[ 82](mcux__lpc__syscon__clock_8h.md#a195eb8a8c3b6c7b6e251d72416e9f5ca)#define MCUX\_PORT1\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x01)

[ 83](mcux__lpc__syscon__clock_8h.md#a6221119101d1ebbbe579ecba94f9a5d7)#define MCUX\_PORT2\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x02)

[ 84](mcux__lpc__syscon__clock_8h.md#a1445a4269c881125cb70ac7aa1500123)#define MCUX\_PORT3\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x03)

[ 85](mcux__lpc__syscon__clock_8h.md#a21e747d64625513e989f820336695fe6)#define MCUX\_PORT4\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x04)

[ 86](mcux__lpc__syscon__clock_8h.md#a383375e04ea889d4e8b81ab9bbfe0777)#define MCUX\_PORT5\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x05)

87

[ 88](mcux__lpc__syscon__clock_8h.md#a7cd90356302a128dbba7153d3e891cb0)#define MCUX\_ENET\_QOS\_CLK MCUX\_LPC\_CLK\_ID(0x0D, 0x00)

89

[ 90](mcux__lpc__syscon__clock_8h.md#ab9e21c8fe5c2c5443bbef9f4899758c7)#define MCUX\_ENET\_CLK MCUX\_LPC\_CLK\_ID(0x0D, 0x80)

[ 91](mcux__lpc__syscon__clock_8h.md#a2f2facda8354375dc42a13f4f694bce1)#define MCUX\_ENET\_PLL MCUX\_LPC\_CLK\_ID(0x0D, 0x81)

92

[ 93](mcux__lpc__syscon__clock_8h.md#afa330bf26e20bb06562369b957b20a74)#define MCUX\_LCDIC\_CLK MCUX\_LPC\_CLK\_ID(0x0E, 0x00)

94

[ 95](mcux__lpc__syscon__clock_8h.md#ab7cbf63deb386a00ccb16e7197425278)#define MCUX\_LPADC1\_CLK MCUX\_LPC\_CLK\_ID(0x0F, 0x00)

[ 96](mcux__lpc__syscon__clock_8h.md#a84dd7bf290241ce33607bbf4b89c3a74)#define MCUX\_LPADC2\_CLK MCUX\_LPC\_CLK\_ID(0x0F, 0x01)

97

[ 98](mcux__lpc__syscon__clock_8h.md#a6edb49e04b4b5b8631e41d8996ea4f4d)#define MCUX\_FLEXCAN0\_CLK MCUX\_LPC\_CLK\_ID(0x10, 0x00)

[ 99](mcux__lpc__syscon__clock_8h.md#acb74116a4a63a5d264fa1ac4323889d1)#define MCUX\_FLEXCAN1\_CLK MCUX\_LPC\_CLK\_ID(0x10, 0x01)

100

[ 101](mcux__lpc__syscon__clock_8h.md#a9e89cb2e835cb45f9d3dc31043644381)#define MCUX\_FLEXIO0\_CLK MCUX\_LPC\_CLK\_ID(0x11, 0x00)

102

[ 103](mcux__lpc__syscon__clock_8h.md#ae728e9ceeb6589342b0e55c15f9280f4)#define MCUX\_AUDIO\_MCLK MCUX\_LPC\_CLK\_ID(0x12, 0x00)

104

[ 105](mcux__lpc__syscon__clock_8h.md#a84a3bc84d608d79a0332a03ae33870c0)#define MCUX\_LPUART0\_CLK MCUX\_LPC\_CLK\_ID(0x13, 0x00)

[ 106](mcux__lpc__syscon__clock_8h.md#a86b6e5c56bb593e263d8566937fbc91a)#define MCUX\_LPUART1\_CLK MCUX\_LPC\_CLK\_ID(0x13, 0x01)

[ 107](mcux__lpc__syscon__clock_8h.md#ab54611b4971d9070767662dae0c354f2)#define MCUX\_LPUART2\_CLK MCUX\_LPC\_CLK\_ID(0x13, 0x02)

[ 108](mcux__lpc__syscon__clock_8h.md#a1947965c97fcbf0fd4496e15cfab9898)#define MCUX\_LPUART3\_CLK MCUX\_LPC\_CLK\_ID(0x13, 0x03)

[ 109](mcux__lpc__syscon__clock_8h.md#add2e2cbf902282eb801d4cb8ace8208f)#define MCUX\_LPUART4\_CLK MCUX\_LPC\_CLK\_ID(0x13, 0x04)

110

[ 111](mcux__lpc__syscon__clock_8h.md#ae8503d57d003aeb98b33d6dde1321a38)#define MCUX\_LPI2C0\_CLK MCUX\_LPC\_CLK\_ID(0x14, 0x00)

[ 112](mcux__lpc__syscon__clock_8h.md#a85050aee71f14baa6dd1d949b2fad2e7)#define MCUX\_LPI2C1\_CLK MCUX\_LPC\_CLK\_ID(0x14, 0x01)

[ 113](mcux__lpc__syscon__clock_8h.md#aad63572936842d961a103ead8b7d26a3)#define MCUX\_LPI2C2\_CLK MCUX\_LPC\_CLK\_ID(0x14, 0x02)

[ 114](mcux__lpc__syscon__clock_8h.md#a5cb5608e339cf546b02af5e57ce066d1)#define MCUX\_LPI2C3\_CLK MCUX\_LPC\_CLK\_ID(0x14, 0x03)

115

[ 116](mcux__lpc__syscon__clock_8h.md#ac53c30480643b8f20da8a9bcac7d51d6)#define MCUX\_XSPI\_CLK MCUX\_LPC\_CLK\_ID(0x15, 0x00)

[ 117](mcux__lpc__syscon__clock_8h.md#a21749a4bce2094a7c914a83e38b5c7f8)#define MCUX\_XSPI0\_CLK MCUX\_LPC\_CLK\_ID(0x15, 0x00)

[ 118](mcux__lpc__syscon__clock_8h.md#afa58297d3a7ace085f0be5699222c551)#define MCUX\_XSPI1\_CLK MCUX\_LPC\_CLK\_ID(0x15, 0x01)

[ 119](mcux__lpc__syscon__clock_8h.md#a4e6ec0fec25394c08bffa7c5ac03ed72)#define MCUX\_XSPI2\_CLK MCUX\_LPC\_CLK\_ID(0x15, 0x02)

120

[ 121](mcux__lpc__syscon__clock_8h.md#a5e5aa8dc1ab7aee30be7e3466d361d8a)#define MCUX\_SAI0\_CLK MCUX\_LPC\_CLK\_ID(0x16, 0x00)

[ 122](mcux__lpc__syscon__clock_8h.md#a3d50ebfa7d62e8e845281285ec9ea4fb)#define MCUX\_SAI1\_CLK MCUX\_LPC\_CLK\_ID(0x16, 0x01)

123

[ 124](mcux__lpc__syscon__clock_8h.md#a6935ee5a59d23138756ed39b2cc5aaae)#define MCUX\_LPSPI0\_CLK MCUX\_LPC\_CLK\_ID(0x17, 0x00)

[ 125](mcux__lpc__syscon__clock_8h.md#a34ea67ed1fef46d1244791f4af5836c5)#define MCUX\_LPSPI1\_CLK MCUX\_LPC\_CLK\_ID(0x17, 0x01)

126

127#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCUX\_LPC\_SYSCON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [mcux\_lpc\_syscon\_clock.h](mcux__lpc__syscon__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
