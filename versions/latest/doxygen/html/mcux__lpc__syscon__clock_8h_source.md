---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mcux__lpc__syscon__clock_8h_source.html
original_path: doxygen/html/mcux__lpc__syscon__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux\_lpc\_syscon\_clock.h

[Go to the documentation of this file.](mcux__lpc__syscon__clock_8h.md)

1/\*

2 \* Copyright 2020-2023, NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCUX\_LPC\_SYSCON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCUX\_LPC\_SYSCON\_H\_

9

[ 10](mcux__lpc__syscon__clock_8h.md#a0131126fce0a606a4d1ade85654bb61a)#define MCUX\_FLEXCOMM0\_CLK 0

[ 11](mcux__lpc__syscon__clock_8h.md#a94328a748738aa7599c54178320a4270)#define MCUX\_FLEXCOMM1\_CLK 1

[ 12](mcux__lpc__syscon__clock_8h.md#ac7b838481b0c3e22ea0c73cc20649261)#define MCUX\_FLEXCOMM2\_CLK 2

[ 13](mcux__lpc__syscon__clock_8h.md#a81d32a4628c73ae2cff0c7083269adb3)#define MCUX\_FLEXCOMM3\_CLK 3

[ 14](mcux__lpc__syscon__clock_8h.md#aae97de225885a02eaf43c02bdb63a0f7)#define MCUX\_FLEXCOMM4\_CLK 4

[ 15](mcux__lpc__syscon__clock_8h.md#aea277f7f67bc9cfaa9fce0c6028a7ffb)#define MCUX\_FLEXCOMM5\_CLK 5

[ 16](mcux__lpc__syscon__clock_8h.md#ada5a860ef2da608f969b9efcbc17f2c7)#define MCUX\_FLEXCOMM6\_CLK 6

[ 17](mcux__lpc__syscon__clock_8h.md#abd3d4114d1d3214eb08513ea3a8b904b)#define MCUX\_FLEXCOMM7\_CLK 7

[ 18](mcux__lpc__syscon__clock_8h.md#a4db5314db3735bd28e4742e37b703cf1)#define MCUX\_FLEXCOMM8\_CLK 8

[ 19](mcux__lpc__syscon__clock_8h.md#ad3931251f9e41dfb1529c784b25e52f7)#define MCUX\_FLEXCOMM9\_CLK 9

[ 20](mcux__lpc__syscon__clock_8h.md#a27e647672c88a6cdf3dce2a1918e3745)#define MCUX\_FLEXCOMM10\_CLK 10

[ 21](mcux__lpc__syscon__clock_8h.md#a3cc7e2a23e06ed72cb5fc267dc0bbd8a)#define MCUX\_FLEXCOMM11\_CLK 11

[ 22](mcux__lpc__syscon__clock_8h.md#a69bbe063f4e3a961d7cf5818e4538e09)#define MCUX\_FLEXCOMM12\_CLK 12

[ 23](mcux__lpc__syscon__clock_8h.md#ad70ee63f0f119911b8d2b3ecf57c4dea)#define MCUX\_FLEXCOMM13\_CLK 13

[ 24](mcux__lpc__syscon__clock_8h.md#ace02fa0f8524187210a42b35cc81b3b4)#define MCUX\_HS\_SPI\_CLK 14

[ 25](mcux__lpc__syscon__clock_8h.md#afd7c883dfbd0d6f45c0dda39fb454c3c)#define MCUX\_PMIC\_I2C\_CLK 15

[ 26](mcux__lpc__syscon__clock_8h.md#a79a1c0861f807daa840d8f2cb7884888)#define MCUX\_HS\_SPI1\_CLK 16

27

[ 28](mcux__lpc__syscon__clock_8h.md#af75d628dbb0a7721ad41e975149ac933)#define MCUX\_USDHC1\_CLK 20

[ 29](mcux__lpc__syscon__clock_8h.md#a035029233e88559d5cc8c278f57f2327)#define MCUX\_USDHC2\_CLK 21

30

[ 31](mcux__lpc__syscon__clock_8h.md#ae1a860e5ab8828ea6547994b786b05e8)#define MCUX\_CTIMER\_CLK\_OFFSET 22

32

[ 33](mcux__lpc__syscon__clock_8h.md#a29436fa81a77c707ca9c08a42a301019)#define MCUX\_CTIMER0\_CLK 0

[ 34](mcux__lpc__syscon__clock_8h.md#a813bc9c11cded4fa7abda6fa3ac33bf2)#define MCUX\_CTIMER1\_CLK 1

[ 35](mcux__lpc__syscon__clock_8h.md#a4f142a3a6cf54650c0a9c1510d078e59)#define MCUX\_CTIMER2\_CLK 2

[ 36](mcux__lpc__syscon__clock_8h.md#aa8835aa87fd2ce75ea4a734c0f9dcf61)#define MCUX\_CTIMER3\_CLK 3

[ 37](mcux__lpc__syscon__clock_8h.md#a0cd96aaaf82fd1acba2c8e24914547a1)#define MCUX\_CTIMER4\_CLK 4

38

[ 39](mcux__lpc__syscon__clock_8h.md#afe9d906202d3e843dcfc340e4bb65571)#define MCUX\_MCAN\_CLK 27

40

[ 41](mcux__lpc__syscon__clock_8h.md#aa13d3e469489fcb89348867a8cacdb3e)#define MCUX\_BUS\_CLK 28

42

[ 43](mcux__lpc__syscon__clock_8h.md#aecd4904bd578ff819e6e871aecc438b5)#define MCUX\_SDIF\_CLK 29

44

[ 45](mcux__lpc__syscon__clock_8h.md#aefcdabc53569382c9f01f481eec4a6d2)#define MCUX\_I3C\_CLK 30

46

[ 47](mcux__lpc__syscon__clock_8h.md#afd1ed6a3c1c3b3c8f96ca2bc55a6d20c)#define MCUX\_MIPI\_DSI\_DPHY\_CLK 31

[ 48](mcux__lpc__syscon__clock_8h.md#a182f8126cae1792c3c8e4c1a81f13fda)#define MCUX\_MIPI\_DSI\_ESC\_CLK 32

49

[ 50](mcux__lpc__syscon__clock_8h.md#a1b3db2423ad6e3c7dfc3943756fa0cb7)#define MCUX\_LCDIF\_PIXEL\_CLK 33

51

[ 52](mcux__lpc__syscon__clock_8h.md#a9eda466db2baa4c504798e0878a3ef48)#define MCUX\_SCTIMER\_CLK 34

53

[ 54](mcux__lpc__syscon__clock_8h.md#a161ba4b82b6a6423afd54b334d22ecdf)#define MCUX\_DMIC\_CLK 35

55

[ 56](mcux__lpc__syscon__clock_8h.md#a5afbfb7ac6f3da817ab539112a951e4e)#define MCUX\_FLEXSPI\_CLK 36

[ 57](mcux__lpc__syscon__clock_8h.md#a53c6b6b4fd0ca41960a831dc752e7d5f)#define MCUX\_FLEXSPI2\_CLK 37

58

[ 59](mcux__lpc__syscon__clock_8h.md#a158d5ef92e191535e5170dffbea757fc)#define MCUX\_MRT\_CLK 40

60

61#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_MCUX\_LPC\_SYSCON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [mcux\_lpc\_syscon\_clock.h](mcux__lpc__syscon__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
