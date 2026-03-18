---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/clock__agilex__ll_8h_source.html
original_path: doxygen/html/clock__agilex__ll_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_agilex\_ll.h

[Go to the documentation of this file.](clock__agilex__ll_8h.md)

1/\*

2 \* Copyright (c) 2019-2022, Intel Corporation. All rights reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef CLOCKMANAGER\_H

8#define CLOCKMANAGER\_H

9

10#include <socfpga\_handoff.h>

11

12/\* Clock Manager Registers \*/

[ 13](clock__agilex__ll_8h.md#a7ce2e6aec96ecc51999e93153e45c437)#define CLKMGR\_OFFSET 0xffd10000

14

[ 15](clock__agilex__ll_8h.md#af5d589d3674dd3ab4092a1b8fc54c36e)#define CLKMGR\_CTRL 0x0

[ 16](clock__agilex__ll_8h.md#a7aa1ea6315cdfba9836596bdd9330d6f)#define CLKMGR\_STAT 0x4

[ 17](clock__agilex__ll_8h.md#a0b70ada815bf2d1165e09c01d341b13d)#define CLKMGR\_INTRCLR 0x14

18

19/\* Main PLL Group \*/

[ 20](clock__agilex__ll_8h.md#aa6f1c676b1fd193c48c0aaf7554b2d6e)#define CLKMGR\_MAINPLL 0xffd10024

[ 21](clock__agilex__ll_8h.md#af4f0772c563c9016457459e623681ffe)#define CLKMGR\_MAINPLL\_EN 0x0

[ 22](clock__agilex__ll_8h.md#a4a8e8063880880a26f938675bb6af59b)#define CLKMGR\_MAINPLL\_BYPASS 0xc

[ 23](clock__agilex__ll_8h.md#a87ea7de8d3625861d119d7b9e17b72b1)#define CLKMGR\_MAINPLL\_MPUCLK 0x18

[ 24](clock__agilex__ll_8h.md#a7e31fed5050598f8944186b387d738ba)#define CLKMGR\_MAINPLL\_NOCCLK 0x1c

[ 25](clock__agilex__ll_8h.md#a5dea9faa03275b82f29cc03bb7a82998)#define CLKMGR\_MAINPLL\_NOCDIV 0x20

[ 26](clock__agilex__ll_8h.md#a86db445343ab57a0c7d7650bd3a5d727)#define CLKMGR\_MAINPLL\_PLLGLOB 0x24

[ 27](clock__agilex__ll_8h.md#a585119c5c27cf0b02b925cfca929c1a4)#define CLKMGR\_MAINPLL\_FDBCK 0x28

[ 28](clock__agilex__ll_8h.md#a44c3eb51a678369d368f5def509ec098)#define CLKMGR\_MAINPLL\_MEM 0x2c

[ 29](clock__agilex__ll_8h.md#add31f35ee1f5d3c75324143fd9d91e2a)#define CLKMGR\_MAINPLL\_MEMSTAT 0x30

[ 30](clock__agilex__ll_8h.md#ab09e3ec031a2f074172e165ac5928aa7)#define CLKMGR\_MAINPLL\_PLLC0 0x34

[ 31](clock__agilex__ll_8h.md#aaf0a5fa071ee92ce4de423ac44984e36)#define CLKMGR\_MAINPLL\_PLLC1 0x38

[ 32](clock__agilex__ll_8h.md#a4a3459c7a5d1df04882a8cf21b477629)#define CLKMGR\_MAINPLL\_VCOCALIB 0x3c

[ 33](clock__agilex__ll_8h.md#a5149cc7c7323438b9660608329cafb18)#define CLKMGR\_MAINPLL\_PLLC2 0x40

[ 34](clock__agilex__ll_8h.md#a3ce82fe6e2087d5c46b75c4ccc44ac9d)#define CLKMGR\_MAINPLL\_PLLC3 0x44

[ 35](clock__agilex__ll_8h.md#af354805596754d304bc54ca0e75306c0)#define CLKMGR\_MAINPLL\_PLLM 0x48

[ 36](clock__agilex__ll_8h.md#ad18f16daf2a4ce5e628f16a829097d61)#define CLKMGR\_MAINPLL\_LOSTLOCK 0x54

37

38/\* Peripheral PLL Group \*/

[ 39](clock__agilex__ll_8h.md#abffd6d11b10b59f792c74bd292778d97)#define CLKMGR\_PERPLL 0xffd1007c

[ 40](clock__agilex__ll_8h.md#aca57ee95281d79ae0429fbfe29a116f5)#define CLKMGR\_PERPLL\_EN 0x0

[ 41](clock__agilex__ll_8h.md#afa44f1602dd9a119077821a57a9639ec)#define CLKMGR\_PERPLL\_BYPASS 0xc

[ 42](clock__agilex__ll_8h.md#a61ed24c0d6e3cd458bbcfec8a67acc34)#define CLKMGR\_PERPLL\_EMACCTL 0x18

[ 43](clock__agilex__ll_8h.md#aa9e9981aa179f50973776374b83eee45)#define CLKMGR\_PERPLL\_GPIODIV 0x1c

[ 44](clock__agilex__ll_8h.md#a5c5113dd9047084667ad3b6c48c9b059)#define CLKMGR\_PERPLL\_PLLGLOB 0x20

[ 45](clock__agilex__ll_8h.md#af03410c71da48d28ade194581b655aba)#define CLKMGR\_PERPLL\_FDBCK 0x24

[ 46](clock__agilex__ll_8h.md#a9a704394b4a7706895cc5bd3327d9b1e)#define CLKMGR\_PERPLL\_MEM 0x28

[ 47](clock__agilex__ll_8h.md#ad8e83a05ecaa545e5c8d7cc4fd13b12c)#define CLKMGR\_PERPLL\_MEMSTAT 0x2c

[ 48](clock__agilex__ll_8h.md#a94f5888bfcec5a4a04df8226defc56a1)#define CLKMGR\_PERPLL\_PLLC0 0x30

[ 49](clock__agilex__ll_8h.md#affe47567111a1959d4b060a171411811)#define CLKMGR\_PERPLL\_PLLC1 0x34

[ 50](clock__agilex__ll_8h.md#a83c322b74ee05528ffbe9434bcf52067)#define CLKMGR\_PERPLL\_VCOCALIB 0x38

[ 51](clock__agilex__ll_8h.md#a9cac40abca09e28cac234e92ca2de7fc)#define CLKMGR\_PERPLL\_PLLC2 0x3c

[ 52](clock__agilex__ll_8h.md#a8f386922aae4a7c70359302b7b044b27)#define CLKMGR\_PERPLL\_PLLC3 0x40

[ 53](clock__agilex__ll_8h.md#a8334e2e3d21ff2d36fa4d744d68b9a70)#define CLKMGR\_PERPLL\_PLLM 0x44

[ 54](clock__agilex__ll_8h.md#a05fb71dae6c53fd336c3ae792f51eb25)#define CLKMGR\_PERPLL\_LOSTLOCK 0x50

55

56/\* Altera Group \*/

[ 57](clock__agilex__ll_8h.md#a2fb528b9c63cb22806e89265a0ea5f67)#define CLKMGR\_ALTERA 0xffd100d0

[ 58](clock__agilex__ll_8h.md#a99f91779ac440853879974133e2a18d9)#define CLKMGR\_ALTERA\_JTAG 0x0

[ 59](clock__agilex__ll_8h.md#a2e37d7f74049fd3203370d67f97f0d1b)#define CLKMGR\_ALTERA\_EMACACTR 0x4

[ 60](clock__agilex__ll_8h.md#a478ee107d6162910a8508c95de702672)#define CLKMGR\_ALTERA\_EMACBCTR 0x8

[ 61](clock__agilex__ll_8h.md#a348269b9667529877e138fe85b45453f)#define CLKMGR\_ALTERA\_EMACPTPCTR 0xc

[ 62](clock__agilex__ll_8h.md#a938138d6369d0f84d4c0ca350aec33aa)#define CLKMGR\_ALTERA\_GPIODBCTR 0x10

[ 63](clock__agilex__ll_8h.md#a5877bdb7b50181bdd08956cb81b89878)#define CLKMGR\_ALTERA\_SDMMCCTR 0x14

[ 64](clock__agilex__ll_8h.md#ad66a4e5eedaee77dd554601bc9e0700e)#define CLKMGR\_ALTERA\_S2FUSER0CTR 0x18

[ 65](clock__agilex__ll_8h.md#a3855729ea087e571004c7fff1e718a9e)#define CLKMGR\_ALTERA\_S2FUSER1CTR 0x1c

[ 66](clock__agilex__ll_8h.md#a31f2df94d9b2cc020d4abab3b0152007)#define CLKMGR\_ALTERA\_PSIREFCTR 0x20

[ 67](clock__agilex__ll_8h.md#ae13120d546f6efecbbd0b13bf68e6324)#define CLKMGR\_ALTERA\_EXTCNTRST 0x24

68

69/\* Membus \*/

[ 70](clock__agilex__ll_8h.md#a983bee0c9f469bc77fa1725c4bb481be)#define CLKMGR\_MEM\_REQ BIT(24)

[ 71](clock__agilex__ll_8h.md#a92722915ca5ab507ebc3849fc45271bf)#define CLKMGR\_MEM\_WR BIT(25)

[ 72](clock__agilex__ll_8h.md#a185c1b42f6b54f1bf77727957a1e34b0)#define CLKMGR\_MEM\_ERR BIT(26)

[ 73](clock__agilex__ll_8h.md#ac771635c52ff366a2b083b5d86a36a68)#define CLKMGR\_MEM\_WDAT\_OFFSET 16

[ 74](clock__agilex__ll_8h.md#a8f4fd8cb47546aa1217472c18b65ec2a)#define CLKMGR\_MEM\_ADDR 0x4027

[ 75](clock__agilex__ll_8h.md#a466aa1fc4ffacf0494df00dcb43cae63)#define CLKMGR\_MEM\_WDAT 0x80

76

77/\* Clock Manager Macros \*/

[ 78](clock__agilex__ll_8h.md#ab78537c12a99cc485ccceab8ff661145)#define CLKMGR\_CTRL\_BOOTMODE\_SET\_MSK 0x00000001

[ 79](clock__agilex__ll_8h.md#ae0c120f58b7c7c672b432d1550bd5f49)#define CLKMGR\_STAT\_BUSY\_E\_BUSY 0x1

[ 80](clock__agilex__ll_8h.md#a49b947aba126c7dfc0c32145c8ba3b13)#define CLKMGR\_STAT\_BUSY(x) (((x) & 0x00000001) >> 0)

[ 81](clock__agilex__ll_8h.md#a631937c42d864f312399859fdf09d895)#define CLKMGR\_STAT\_MAINPLLLOCKED(x) (((x) & 0x00000100) >> 8)

[ 82](clock__agilex__ll_8h.md#ac09c2acac5dce5da3f333c603393f9d9)#define CLKMGR\_STAT\_PERPLLLOCKED(x) (((x) & 0x00010000) >> 16)

[ 83](clock__agilex__ll_8h.md#ac51105f17860589a1222c91d633c3e14)#define CLKMGR\_INTRCLR\_MAINLOCKLOST\_SET\_MSK 0x00000004

[ 84](clock__agilex__ll_8h.md#a90cba4544b7ff82fe03faa9659e69cc1)#define CLKMGR\_INTRCLR\_PERLOCKLOST\_SET\_MSK 0x00000008

[ 85](clock__agilex__ll_8h.md#a7901ba453bc5083e5b71108051cd53aa)#define CLKMGR\_INTOSC\_HZ 460000000

86

87/\* Main PLL Macros \*/

[ 88](clock__agilex__ll_8h.md#ae6382ca96b72dc2169219c092428d522)#define CLKMGR\_MAINPLL\_EN\_RESET 0x000000ff

89

90/\* Peripheral PLL Macros \*/

[ 91](clock__agilex__ll_8h.md#a0efbebef5965f0fdc2fefa4336aeca0f)#define CLKMGR\_PERPLL\_EN\_RESET 0x00000fff

[ 92](clock__agilex__ll_8h.md#abed91c06356654901088ca6d64b46b41)#define CLKMGR\_PERPLL\_EN\_SDMMCCLK BIT(5)

[ 93](clock__agilex__ll_8h.md#a1a8ce17cc92e9c8a55ed5a56c79183df)#define CLKMGR\_PERPLL\_GPIODIV\_GPIODBCLK\_SET(x) (((x) << 0) & 0x0000ffff)

94

95/\* Altera Macros \*/

[ 96](clock__agilex__ll_8h.md#a1b0ef45bf5d6403362a4c0579b7221c3)#define CLKMGR\_ALTERA\_EXTCNTRST\_RESET 0xff

97

98/\* Shared Macros \*/

[ 99](clock__agilex__ll_8h.md#ab8dcd2c21c183c097b74a8b2c5974b73)#define CLKMGR\_PSRC(x) (((x) & 0x00030000) >> 16)

[ 100](clock__agilex__ll_8h.md#a52626e2d7ad13fc2ad32d0ee9b5bd048)#define CLKMGR\_PSRC\_MAIN 0

[ 101](clock__agilex__ll_8h.md#a7101c2e1996f4adee854745ff9feb938)#define CLKMGR\_PSRC\_PER 1

102

[ 103](clock__agilex__ll_8h.md#a1e26c5032c40ffe903109e23aae95170)#define CLKMGR\_PLLGLOB\_PSRC\_EOSC1 0x0

[ 104](clock__agilex__ll_8h.md#a55457cdf91596fab57fe5016898dd66f)#define CLKMGR\_PLLGLOB\_PSRC\_INTOSC 0x1

[ 105](clock__agilex__ll_8h.md#acd3529f6d4fe0298ac156e80b1e2e9c3)#define CLKMGR\_PLLGLOB\_PSRC\_F2S 0x2

106

[ 107](clock__agilex__ll_8h.md#ab39e427e438e5a994573bc8df4400727)#define CLKMGR\_PLLM\_MDIV(x) ((x) & 0x000003ff)

[ 108](clock__agilex__ll_8h.md#a3fb498116d432701d280e503200559a2)#define CLKMGR\_PLLGLOB\_PD\_SET\_MSK 0x00000001

[ 109](clock__agilex__ll_8h.md#a8413bbfbee567a7dfec2bf7c82b663d4)#define CLKMGR\_PLLGLOB\_RST\_SET\_MSK 0x00000002

110

[ 111](clock__agilex__ll_8h.md#af6208d347c28b5688f4a6caefe3eced7)#define CLKMGR\_PLLGLOB\_REFCLKDIV(x) (((x) & 0x00003f00) >> 8)

[ 112](clock__agilex__ll_8h.md#a1da55c1bbb0e133afe769e0e9f3be5d7)#define CLKMGR\_PLLGLOB\_AREFCLKDIV(x) (((x) & 0x00000f00) >> 8)

[ 113](clock__agilex__ll_8h.md#ad9bdc9e849335224cd4449c3e45a5779)#define CLKMGR\_PLLGLOB\_DREFCLKDIV(x) (((x) & 0x00003000) >> 12)

114

[ 115](clock__agilex__ll_8h.md#a818647eff6b91c033efc41c2022bf16b)#define CLKMGR\_VCOCALIB\_HSCNT\_SET(x) (((x) << 0) & 0x000003ff)

[ 116](clock__agilex__ll_8h.md#a054daafab40b9f41a2269eadaea78e05)#define CLKMGR\_VCOCALIB\_MSCNT\_SET(x) (((x) << 16) & 0x00ff0000)

117

[ 118](clock__agilex__ll_8h.md#af6457691c9e7ed5014fadad1fb36a6fb)#define CLKMGR\_CLR\_LOSTLOCK\_BYPASS 0x20000000

119

[ 120](clock__agilex__ll_8h.md#acbc7941cdcb96d94336aef1649fdd4e9)void [config\_clkmgr\_handoff](clock__agilex__ll_8h.md#acbc7941cdcb96d94336aef1649fdd4e9)(struct handoff \*hoff\_ptr);

[ 121](clock__agilex__ll_8h.md#ad2b025eee2ac7f5ac5f49c004d1f66e9)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [get\_mpu\_clk](clock__agilex__ll_8h.md#ad2b025eee2ac7f5ac5f49c004d1f66e9)(void);

[ 122](clock__agilex__ll_8h.md#a223981ca09133eb12a2be066426be7bd)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [get\_wdt\_clk](clock__agilex__ll_8h.md#a223981ca09133eb12a2be066426be7bd)(void);

[ 123](clock__agilex__ll_8h.md#a15c79941c9f9622bb453349dc1b965a6)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [get\_uart\_clk](clock__agilex__ll_8h.md#a15c79941c9f9622bb453349dc1b965a6)(void);

[ 124](clock__agilex__ll_8h.md#afa5f97189dc639da0859fe027c0af4ee)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [get\_mmc\_clk](clock__agilex__ll_8h.md#afa5f97189dc639da0859fe027c0af4ee)(void);

125

126#endif

[get\_uart\_clk](clock__agilex__ll_8h.md#a15c79941c9f9622bb453349dc1b965a6)

uint32\_t get\_uart\_clk(void)

[get\_wdt\_clk](clock__agilex__ll_8h.md#a223981ca09133eb12a2be066426be7bd)

uint32\_t get\_wdt\_clk(void)

[config\_clkmgr\_handoff](clock__agilex__ll_8h.md#acbc7941cdcb96d94336aef1649fdd4e9)

void config\_clkmgr\_handoff(struct handoff \*hoff\_ptr)

[get\_mpu\_clk](clock__agilex__ll_8h.md#ad2b025eee2ac7f5ac5f49c004d1f66e9)

uint32\_t get\_mpu\_clk(void)

[get\_mmc\_clk](clock__agilex__ll_8h.md#afa5f97189dc639da0859fe027c0af4ee)

uint32\_t get\_mmc\_clk(void)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_agilex\_ll.h](clock__agilex__ll_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
