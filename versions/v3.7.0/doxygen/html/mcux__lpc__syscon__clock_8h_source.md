---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mcux__lpc__syscon__clock_8h_source.html
original_path: doxygen/html/mcux__lpc__syscon__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

24

[ 25](mcux__lpc__syscon__clock_8h.md#a0131126fce0a606a4d1ade85654bb61a)#define MCUX\_FLEXCOMM0\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x00)

[ 26](mcux__lpc__syscon__clock_8h.md#a94328a748738aa7599c54178320a4270)#define MCUX\_FLEXCOMM1\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x01)

[ 27](mcux__lpc__syscon__clock_8h.md#ac7b838481b0c3e22ea0c73cc20649261)#define MCUX\_FLEXCOMM2\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x02)

[ 28](mcux__lpc__syscon__clock_8h.md#a81d32a4628c73ae2cff0c7083269adb3)#define MCUX\_FLEXCOMM3\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x03)

[ 29](mcux__lpc__syscon__clock_8h.md#aae97de225885a02eaf43c02bdb63a0f7)#define MCUX\_FLEXCOMM4\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x04)

[ 30](mcux__lpc__syscon__clock_8h.md#aea277f7f67bc9cfaa9fce0c6028a7ffb)#define MCUX\_FLEXCOMM5\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x05)

[ 31](mcux__lpc__syscon__clock_8h.md#ada5a860ef2da608f969b9efcbc17f2c7)#define MCUX\_FLEXCOMM6\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x06)

[ 32](mcux__lpc__syscon__clock_8h.md#abd3d4114d1d3214eb08513ea3a8b904b)#define MCUX\_FLEXCOMM7\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x07)

[ 33](mcux__lpc__syscon__clock_8h.md#a4db5314db3735bd28e4742e37b703cf1)#define MCUX\_FLEXCOMM8\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x08)

[ 34](mcux__lpc__syscon__clock_8h.md#ad3931251f9e41dfb1529c784b25e52f7)#define MCUX\_FLEXCOMM9\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x09)

[ 35](mcux__lpc__syscon__clock_8h.md#a27e647672c88a6cdf3dce2a1918e3745)#define MCUX\_FLEXCOMM10\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0A)

[ 36](mcux__lpc__syscon__clock_8h.md#a3cc7e2a23e06ed72cb5fc267dc0bbd8a)#define MCUX\_FLEXCOMM11\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0B)

[ 37](mcux__lpc__syscon__clock_8h.md#a69bbe063f4e3a961d7cf5818e4538e09)#define MCUX\_FLEXCOMM12\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0C)

[ 38](mcux__lpc__syscon__clock_8h.md#ad70ee63f0f119911b8d2b3ecf57c4dea)#define MCUX\_FLEXCOMM13\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0D)

[ 39](mcux__lpc__syscon__clock_8h.md#ace02fa0f8524187210a42b35cc81b3b4)#define MCUX\_HS\_SPI\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0E)

[ 40](mcux__lpc__syscon__clock_8h.md#a0b68c4607dfc6a6b8cd172c14b641515)#define MCUX\_FLEXCOMM14\_CLK MCUX\_HS\_SPI\_CLK

[ 41](mcux__lpc__syscon__clock_8h.md#afd7c883dfbd0d6f45c0dda39fb454c3c)#define MCUX\_PMIC\_I2C\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x0F)

[ 42](mcux__lpc__syscon__clock_8h.md#a79a1c0861f807daa840d8f2cb7884888)#define MCUX\_HS\_SPI1\_CLK MCUX\_LPC\_CLK\_ID(0x01, 0x10)

43

[ 44](mcux__lpc__syscon__clock_8h.md#af75d628dbb0a7721ad41e975149ac933)#define MCUX\_USDHC1\_CLK MCUX\_LPC\_CLK\_ID(0x02, 0x00)

[ 45](mcux__lpc__syscon__clock_8h.md#a035029233e88559d5cc8c278f57f2327)#define MCUX\_USDHC2\_CLK MCUX\_LPC\_CLK\_ID(0x02, 0x01)

46

[ 47](mcux__lpc__syscon__clock_8h.md#afe9d906202d3e843dcfc340e4bb65571)#define MCUX\_MCAN\_CLK MCUX\_LPC\_CLK\_ID(0x03, 0x00)

48

[ 49](mcux__lpc__syscon__clock_8h.md#aa13d3e469489fcb89348867a8cacdb3e)#define MCUX\_BUS\_CLK MCUX\_LPC\_CLK\_ID(0x04, 0x00)

50

[ 51](mcux__lpc__syscon__clock_8h.md#aecd4904bd578ff819e6e871aecc438b5)#define MCUX\_SDIF\_CLK MCUX\_LPC\_CLK\_ID(0x05, 0x00)

52

[ 53](mcux__lpc__syscon__clock_8h.md#aefcdabc53569382c9f01f481eec4a6d2)#define MCUX\_I3C\_CLK MCUX\_LPC\_CLK\_ID(0x06, 0x00)

54

[ 55](mcux__lpc__syscon__clock_8h.md#afd1ed6a3c1c3b3c8f96ca2bc55a6d20c)#define MCUX\_MIPI\_DSI\_DPHY\_CLK MCUX\_LPC\_CLK\_ID(0x07, 0x00)

[ 56](mcux__lpc__syscon__clock_8h.md#a182f8126cae1792c3c8e4c1a81f13fda)#define MCUX\_MIPI\_DSI\_ESC\_CLK MCUX\_LPC\_CLK\_ID(0x07, 0x01)

57

[ 58](mcux__lpc__syscon__clock_8h.md#a1b3db2423ad6e3c7dfc3943756fa0cb7)#define MCUX\_LCDIF\_PIXEL\_CLK MCUX\_LPC\_CLK\_ID(0x08, 0x00)

59

[ 60](mcux__lpc__syscon__clock_8h.md#a9eda466db2baa4c504798e0878a3ef48)#define MCUX\_SCTIMER\_CLK MCUX\_LPC\_CLK\_ID(0x09, 0x00)

61

[ 62](mcux__lpc__syscon__clock_8h.md#a161ba4b82b6a6423afd54b334d22ecdf)#define MCUX\_DMIC\_CLK MCUX\_LPC\_CLK\_ID(0x0A, 0x00)

63

[ 64](mcux__lpc__syscon__clock_8h.md#a5afbfb7ac6f3da817ab539112a951e4e)#define MCUX\_FLEXSPI\_CLK MCUX\_LPC\_CLK\_ID(0x0A, 0x00)

[ 65](mcux__lpc__syscon__clock_8h.md#a53c6b6b4fd0ca41960a831dc752e7d5f)#define MCUX\_FLEXSPI2\_CLK MCUX\_LPC\_CLK\_ID(0x0A, 0x01)

66

[ 67](mcux__lpc__syscon__clock_8h.md#a158d5ef92e191535e5170dffbea757fc)#define MCUX\_MRT\_CLK MCUX\_LPC\_CLK\_ID(0x0B, 0x00)

[ 68](mcux__lpc__syscon__clock_8h.md#a8f064dcf75db9a88930a09f8f100c0fd)#define MCUX\_FREEMRT\_CLK MCUX\_LPC\_CLK\_ID(0x0B, 0x01)

69

[ 70](mcux__lpc__syscon__clock_8h.md#a6c42df5400351c99bd761db7370951d9)#define MCUX\_PORT0\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x00)

[ 71](mcux__lpc__syscon__clock_8h.md#a195eb8a8c3b6c7b6e251d72416e9f5ca)#define MCUX\_PORT1\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x01)

[ 72](mcux__lpc__syscon__clock_8h.md#a6221119101d1ebbbe579ecba94f9a5d7)#define MCUX\_PORT2\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x02)

[ 73](mcux__lpc__syscon__clock_8h.md#a1445a4269c881125cb70ac7aa1500123)#define MCUX\_PORT3\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x03)

[ 74](mcux__lpc__syscon__clock_8h.md#a21e747d64625513e989f820336695fe6)#define MCUX\_PORT4\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x04)

[ 75](mcux__lpc__syscon__clock_8h.md#a383375e04ea889d4e8b81ab9bbfe0777)#define MCUX\_PORT5\_CLK MCUX\_LPC\_CLK\_ID(0x0C, 0x05)

76

[ 77](mcux__lpc__syscon__clock_8h.md#a7cd90356302a128dbba7153d3e891cb0)#define MCUX\_ENET\_QOS\_CLK MCUX\_LPC\_CLK\_ID(0x0D, 0x00)

78

[ 79](mcux__lpc__syscon__clock_8h.md#ab9e21c8fe5c2c5443bbef9f4899758c7)#define MCUX\_ENET\_CLK MCUX\_LPC\_CLK\_ID(0x0D, 0x80)

[ 80](mcux__lpc__syscon__clock_8h.md#a2f2facda8354375dc42a13f4f694bce1)#define MCUX\_ENET\_PLL MCUX\_LPC\_CLK\_ID(0x0D, 0x81)

81

[ 82](mcux__lpc__syscon__clock_8h.md#afa330bf26e20bb06562369b957b20a74)#define MCUX\_LCDIC\_CLK MCUX\_LPC\_CLK\_ID(0x0E, 0x00)

83

[ 84](mcux__lpc__syscon__clock_8h.md#ab7cbf63deb386a00ccb16e7197425278)#define MCUX\_LPADC1\_CLK MCUX\_LPC\_CLK\_ID(0x0F, 0x00)

[ 85](mcux__lpc__syscon__clock_8h.md#a84dd7bf290241ce33607bbf4b89c3a74)#define MCUX\_LPADC2\_CLK MCUX\_LPC\_CLK\_ID(0x0F, 0x01)

86

[ 87](mcux__lpc__syscon__clock_8h.md#a6edb49e04b4b5b8631e41d8996ea4f4d)#define MCUX\_FLEXCAN0\_CLK MCUX\_LPC\_CLK\_ID(0x10, 0x00)

[ 88](mcux__lpc__syscon__clock_8h.md#acb74116a4a63a5d264fa1ac4323889d1)#define MCUX\_FLEXCAN1\_CLK MCUX\_LPC\_CLK\_ID(0x10, 0x01)

89

[ 90](mcux__lpc__syscon__clock_8h.md#a9e89cb2e835cb45f9d3dc31043644381)#define MCUX\_FLEXIO0\_CLK MCUX\_LPC\_CLK\_ID(0x11, 0x00)

91

92#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCUX\_LPC\_SYSCON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [mcux\_lpc\_syscon\_clock.h](mcux__lpc__syscon__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
