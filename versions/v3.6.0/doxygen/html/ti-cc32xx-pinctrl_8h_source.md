---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ti-cc32xx-pinctrl_8h_source.html
original_path: doxygen/html/ti-cc32xx-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti-cc32xx-pinctrl.h

[Go to the documentation of this file.](ti-cc32xx-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_TI\_CC32XX\_PINCTRL\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_TI\_CC32XX\_PINCTRL\_H\_

8

9/\*

10 \* The whole TI CC32XX pin configuration information is encoded in a 32-bit

11 \* bitfield organized as follows:

12 \*

13 \* - 31..22: Reserved

14 \* - 21..16: Pin.

15 \* - 15..10: Reserved.

16 \* - 9: Pull-down flag.

17 \* - 8: Pull-up flag.

18 \* - 7..5: Drive strength.

19 \* - 4: Enable open-drain flag.

20 \* - 3..0: Configuration mode

21 \*

22 \* Note that the lower bits (11..0) map directly to the MEM\_GPIO\_PAD\_CONFIG

23 \* register.

24 \*/

25

30

[ 31](ti-cc32xx-pinctrl_8h.md#a40cc14e2a5969a01d7a764fb5bdb84a7)#define TI\_CC32XX\_PIN\_MSK 0x3FU

[ 32](ti-cc32xx-pinctrl_8h.md#aea6f7d34537febd574f9ea0db1fbf3f3)#define TI\_CC32XX\_PIN\_POS 16U

[ 33](ti-cc32xx-pinctrl_8h.md#a381590ba2880c42636058c248f7e0e2e)#define TI\_CC32XX\_MUX\_MSK 0xFU

[ 34](ti-cc32xx-pinctrl_8h.md#ac9e2e00ac00ddd1eaf84331d18806339)#define TI\_CC32XX\_MUX\_POS 0U

35

37

[ 44](ti-cc32xx-pinctrl_8h.md#a4bf6d48b1ebcaaeb96b0450533dfa428)#define TI\_CC32XX\_PINMUX(pin, mux) \

45 ((((pin)&TI\_CC32XX\_PIN\_MSK) << TI\_CC32XX\_PIN\_POS) | \

46 (((mux)&TI\_CC32XX\_MUX\_MSK) << TI\_CC32XX\_MUX\_POS))

47

52

[ 53](ti-cc32xx-pinctrl_8h.md#a89f97aa766818f7482c3131b39fc57c6)#define GPIO10\_P1 TI\_CC32XX\_PINMUX(1U, 0U)

[ 54](ti-cc32xx-pinctrl_8h.md#abd05f625495d2ea978dd73f2163ac895)#define I2C\_SCL\_P1 TI\_CC32XX\_PINMUX(1U, 1U)

[ 55](ti-cc32xx-pinctrl_8h.md#a1b2e5aea3aad1cf49a0c9ed9c1abd0ac)#define GT\_PWM06\_P1 TI\_CC32XX\_PINMUX(1U, 3U)

[ 56](ti-cc32xx-pinctrl_8h.md#a995c80839609dc2f99440020c4b376c4)#define UART1\_TX\_P1 TI\_CC32XX\_PINMUX(1U, 7U)

[ 57](ti-cc32xx-pinctrl_8h.md#a0348e53054efacbcc5f4b36f5983b483)#define SDCARD\_CLK\_P1 TI\_CC32XX\_PINMUX(1U, 6U)

[ 58](ti-cc32xx-pinctrl_8h.md#a41832e073da75fce278ea3f3a10c7981)#define GT\_CCP01\_P1 TI\_CC32XX\_PINMUX(1U, 12U)

59

[ 60](ti-cc32xx-pinctrl_8h.md#a092456dadbe48fb30ca448f893ff182d)#define GPIO11\_P2 TI\_CC32XX\_PINMUX(2U, 0U)

[ 61](ti-cc32xx-pinctrl_8h.md#a38fbe2595b40a64618809999d9ff7e88)#define I2C\_SDA\_P2 TI\_CC32XX\_PINMUX(2U, 1U)

[ 62](ti-cc32xx-pinctrl_8h.md#a158549be521c32cbadd7fd94a59bc945)#define GT\_PWM07\_P2 TI\_CC32XX\_PINMUX(2U, 3U)

[ 63](ti-cc32xx-pinctrl_8h.md#af0194d8218ffae6e4ca6afdc1b75184c)#define PXCLK\_P2 TI\_CC32XX\_PINMUX(2U, 4U)

[ 64](ti-cc32xx-pinctrl_8h.md#af4b6115dd55265aa56f4fd0e4519449d)#define SDCARD\_CMD\_P2 TI\_CC32XX\_PINMUX(2U, 6U)

[ 65](ti-cc32xx-pinctrl_8h.md#a6c343f9636e9d3b43d19b3d0fe9f00b1)#define UART1\_RX\_P2 TI\_CC32XX\_PINMUX(2U, 7U)

[ 66](ti-cc32xx-pinctrl_8h.md#a29f1d9fd07affc428b9ec13021951496)#define GT\_CCP02\_P2 TI\_CC32XX\_PINMUX(2U, 12U)

[ 67](ti-cc32xx-pinctrl_8h.md#af81018b6a0cfba2b48bcdc9cf864d609)#define MCAFSX\_P2 TI\_CC32XX\_PINMUX(2U, 13U)

68

[ 69](ti-cc32xx-pinctrl_8h.md#aa7fe336032aa6ad0cc8377bef839c249)#define GPIO12\_P3 TI\_CC32XX\_PINMUX(3U, 0U)

[ 70](ti-cc32xx-pinctrl_8h.md#a449900e101576c23577ae8731ff6d832)#define MCACLK\_P3 TI\_CC32XX\_PINMUX(3U, 3U)

[ 71](ti-cc32xx-pinctrl_8h.md#a040fa03ccf78c01cf8353dfafaed4363)#define PVS\_P3 TI\_CC32XX\_PINMUX(3U, 4U)

[ 72](ti-cc32xx-pinctrl_8h.md#a7f43eaa1290d1c51ad8dd0eead54eac8)#define I2C\_SCL\_P3 TI\_CC32XX\_PINMUX(3U, 5U)

[ 73](ti-cc32xx-pinctrl_8h.md#a0a31d5b2068953d90f7e152cfdeec235)#define UART0\_TX\_P3 TI\_CC32XX\_PINMUX(3U, 7U)

[ 74](ti-cc32xx-pinctrl_8h.md#a11be8733f58686a917f33eebc3f83f9f)#define GT\_CCP03\_P3 TI\_CC32XX\_PINMUX(3U, 12U)

75

[ 76](ti-cc32xx-pinctrl_8h.md#aa63a6fa68392be5d91f17f1512bca933)#define GPIO13\_P4 TI\_CC32XX\_PINMUX(4U, 0U)

[ 77](ti-cc32xx-pinctrl_8h.md#a2ac054fb4527be70688dfbad814da263)#define I2C\_SDA\_P4 TI\_CC32XX\_PINMUX(4U, 5U)

[ 78](ti-cc32xx-pinctrl_8h.md#a784b4247574d785820e1960b77d243f8)#define PHS\_P4 TI\_CC32XX\_PINMUX(4U, 4U)

[ 79](ti-cc32xx-pinctrl_8h.md#a8526e278e737f86b5416d2432e06a961)#define UART0\_RX\_P4 TI\_CC32XX\_PINMUX(4U, 7U)

[ 80](ti-cc32xx-pinctrl_8h.md#a469f19224eef6881cc1247eed19c94a9)#define GT\_CCP04\_P4 TI\_CC32XX\_PINMUX(4U, 12U)

81

[ 82](ti-cc32xx-pinctrl_8h.md#a9c9da9f7d6f9b370c7548f936fe70b65)#define GPIO14\_P5 TI\_CC32XX\_PINMUX(5U, 0U)

[ 83](ti-cc32xx-pinctrl_8h.md#a4894dca0ecb760732bf032d80a6d8a13)#define I2C\_SCL\_P5 TI\_CC32XX\_PINMUX(5U, 5U)

[ 84](ti-cc32xx-pinctrl_8h.md#a0835204b6761fdb5da07401588cb60a8)#define GSPI\_CLK\_P5 TI\_CC32XX\_PINMUX(5U, 7U)

[ 85](ti-cc32xx-pinctrl_8h.md#a420084bc2bed97ccfa6cabbdcea111b8)#define PDATA8\_P5 TI\_CC32XX\_PINMUX(5U, 4U)

[ 86](ti-cc32xx-pinctrl_8h.md#a85dd880198761cbddb32b2d482247bfa)#define GT\_CCP05\_P5 TI\_CC32XX\_PINMUX(5U, 12U)

87

[ 88](ti-cc32xx-pinctrl_8h.md#a0b94b2938ede1a6d84b397b12399aa58)#define GPIO15\_P6 TI\_CC32XX\_PINMUX(6U, 0U)

[ 89](ti-cc32xx-pinctrl_8h.md#ac8ded51ba9587b17cf1c2565f635a8a2)#define I2C\_SDA\_P6 TI\_CC32XX\_PINMUX(6U, 5U)

[ 90](ti-cc32xx-pinctrl_8h.md#a2e33fd1fd267afccbef0ca274336708d)#define GSPI\_MISO\_P6 TI\_CC32XX\_PINMUX(6U, 7U)

[ 91](ti-cc32xx-pinctrl_8h.md#a74f7003fe754549a7abd536ce7ca18e0)#define PDATA9\_P6 TI\_CC32XX\_PINMUX(6U, 4U)

[ 92](ti-cc32xx-pinctrl_8h.md#a1f11274609e837c40dbfcf3f4bb2c65b)#define SDCARD\_DATA3\_P6 TI\_CC32XX\_PINMUX(6U, 8U)

[ 93](ti-cc32xx-pinctrl_8h.md#a912c145e14635c2fade2b206d71df0a3)#define GT\_CCP06\_P6 TI\_CC32XX\_PINMUX(6U, 13U)

94

[ 95](ti-cc32xx-pinctrl_8h.md#a48e7884a7dfad77efe683eea6e678e1b)#define GPIO16\_P7 TI\_CC32XX\_PINMUX(7U, 0U)

[ 96](ti-cc32xx-pinctrl_8h.md#a06cd1b5b0df08a309fc7d9d0eb176948)#define GSPI\_MOSI\_P7 TI\_CC32XX\_PINMUX(7U, 7U)

[ 97](ti-cc32xx-pinctrl_8h.md#a4ba12e404845b1777c7fc27673a358c6)#define PDATA10\_P7 TI\_CC32XX\_PINMUX(7U, 4U)

[ 98](ti-cc32xx-pinctrl_8h.md#a3e9e600bebc357ff182f42317b4fbc5f)#define UART1\_TX\_P7 TI\_CC32XX\_PINMUX(7U, 5U)

[ 99](ti-cc32xx-pinctrl_8h.md#ad19d6a6d4e575fdedc182d95c426ef7a)#define SDCARD\_CLK\_P7 TI\_CC32XX\_PINMUX(7U, 8U)

[ 100](ti-cc32xx-pinctrl_8h.md#a2688169c0aa3bfc4333550d77b03f301)#define GT\_CCP07\_P7 TI\_CC32XX\_PINMUX(7U, 13U)

101

[ 102](ti-cc32xx-pinctrl_8h.md#a499b75b5acdf56015bc34363e8770625)#define GPIO17\_P8 TI\_CC32XX\_PINMUX(8U, 0U)

[ 103](ti-cc32xx-pinctrl_8h.md#a9f7daa4bf7f1e01439d84c58da7c7235)#define UART1\_RX\_P8 TI\_CC32XX\_PINMUX(8U, 5U)

[ 104](ti-cc32xx-pinctrl_8h.md#a4a2c3ec59d144e1e20147f3fac31c7cf)#define GSPI\_CS\_P8 TI\_CC32XX\_PINMUX(8U, 7U)

[ 105](ti-cc32xx-pinctrl_8h.md#a23c36223a0811761121eb6992e733191)#define SDCARD\_CMD\_P8 TI\_CC32XX\_PINMUX(8U, 8U)

[ 106](ti-cc32xx-pinctrl_8h.md#aec9421895f489defea513f9451f19a59)#define PDATA11\_P8 TI\_CC32XX\_PINMUX(8U, 4U)

107

[ 108](ti-cc32xx-pinctrl_8h.md#a7bccf18256e2c16eeb9c2712b4123bed)#define GPIO22\_P15 TI\_CC32XX\_PINMUX(15U, 0U)

[ 109](ti-cc32xx-pinctrl_8h.md#ae4a09b647c36db2a78d4d8a128d47ac5)#define MCAFSX\_P15 TI\_CC32XX\_PINMUX(15U, 7U)

[ 110](ti-cc32xx-pinctrl_8h.md#a93a7b969c1094f0c7a4811218a6d6b05)#define GT\_CCP04\_P15 TI\_CC32XX\_PINMUX(15U, 5U)

111

[ 112](ti-cc32xx-pinctrl_8h.md#a6e86e11b2fa406cf3d0a0ec57d1e856f)#define GPIO23\_P16 TI\_CC32XX\_PINMUX(16U, 0U)

[ 113](ti-cc32xx-pinctrl_8h.md#aa8b475c426b332c82e21567727bb482a)#define TDI\_P16 TI\_CC32XX\_PINMUX(16U, 1U)

[ 114](ti-cc32xx-pinctrl_8h.md#af2bdaab6fc0f793aee2bc8821869aad6)#define UART1\_TX\_P16 TI\_CC32XX\_PINMUX(16U, 2U)

[ 115](ti-cc32xx-pinctrl_8h.md#a8267f2892d868a33b27c68ae6673f239)#define I2C\_SCL\_P16 TI\_CC32XX\_PINMUX(16U, 9U)

116

[ 117](ti-cc32xx-pinctrl_8h.md#a80df0d9d7b3c95e556dd6f82f4551f0b)#define GPIO24\_P17 TI\_CC32XX\_PINMUX(17U, 0U)

[ 118](ti-cc32xx-pinctrl_8h.md#a16ea3f7a2cb062dcdab07e50b4f5c049)#define TDO\_P17 TI\_CC32XX\_PINMUX(17U, 1U)

[ 119](ti-cc32xx-pinctrl_8h.md#a6c881b3b5ceb937e8441bd0cd3b449e8)#define PWM0\_P17 TI\_CC32XX\_PINMUX(17U, 5U)

[ 120](ti-cc32xx-pinctrl_8h.md#a632c817fbe28a138a9916a4946ee9da5)#define UART1\_RX\_P17 TI\_CC32XX\_PINMUX(17U, 2U)

[ 121](ti-cc32xx-pinctrl_8h.md#a0b1353bc11a6e1a156c6dbe4e59f74d0)#define I2C\_SDA\_P17 TI\_CC32XX\_PINMUX(17U, 9U)

[ 122](ti-cc32xx-pinctrl_8h.md#a3ba8bacb70f2bcadaa6dfd786a673bd7)#define GT\_CCP06\_P17 TI\_CC32XX\_PINMUX(17U, 4U)

[ 123](ti-cc32xx-pinctrl_8h.md#a082b74a8cdfc05bef2c377e8d271bac3)#define MCAFSX\_P17 TI\_CC32XX\_PINMUX(17U, 6U)

124

[ 125](ti-cc32xx-pinctrl_8h.md#a91221a9648fa4d08c5b4f928a9756c50)#define GPIO28\_P18 TI\_CC32XX\_PINMUX(18U, 0U)

126

[ 127](ti-cc32xx-pinctrl_8h.md#af651d7aa9e7ee9ed0f39ea4ea72d6c3b)#define TCK\_P19 TI\_CC32XX\_PINMUX(19U, 1U)

[ 128](ti-cc32xx-pinctrl_8h.md#a7c7fb987ccc55419a645a4a04b30e200)#define GT\_PWM03\_P19 TI\_CC32XX\_PINMUX(19U, 8U)

129

[ 130](ti-cc32xx-pinctrl_8h.md#abcec00f5b87b8c75cedc5d73ad7107d3)#define GPIO29\_P20 TI\_CC32XX\_PINMUX(20U, 0U)

[ 131](ti-cc32xx-pinctrl_8h.md#a5d14159904ec1c4f56c911e643a7eed4)#define TMS\_P20 TI\_CC32XX\_PINMUX(20U, 1U)

132

[ 133](ti-cc32xx-pinctrl_8h.md#ab316bbdba3762342b3823d9eee34809d)#define GPIO25\_P21 TI\_CC32XX\_PINMUX(21U, 0U)

[ 134](ti-cc32xx-pinctrl_8h.md#aa34e4da30d6f3b91df53e14b195650bc)#define GT\_PWM02\_P21 TI\_CC32XX\_PINMUX(21U, 9U)

[ 135](ti-cc32xx-pinctrl_8h.md#ad0767fcefbfc59f576341422ab3c466f)#define MCASFX\_P21 TI\_CC32XX\_PINMUX(21U, 2U)

136

[ 137](ti-cc32xx-pinctrl_8h.md#ae4b7bd32af0c430944caa10343c7ba89)#define ANTSEL1\_P29 TI\_CC32XX\_PINMUX(29U, 0U)

138

[ 139](ti-cc32xx-pinctrl_8h.md#a637bd5bc2080ed718ed875255907ab81)#define ANTSEL2\_P30 TI\_CC32XX\_PINMUX(30U, 0U)

140

[ 141](ti-cc32xx-pinctrl_8h.md#a0ad70dd2e46b8e463283999c065b1031)#define GPIO31\_P45 TI\_CC32XX\_PINMUX(45U, 0U)

[ 142](ti-cc32xx-pinctrl_8h.md#aec30ecff2290ff162f4940376f092f77)#define UART0\_RX\_P45 TI\_CC32XX\_PINMUX(45U, 9U)

[ 143](ti-cc32xx-pinctrl_8h.md#a0c5127de54dfe7be823dbba91260eeb8)#define MCAFSX\_P45 TI\_CC32XX\_PINMUX(45U, 12U)

[ 144](ti-cc32xx-pinctrl_8h.md#ac379119f98304c790ab8cbba4752feec)#define UART1\_RX\_P45 TI\_CC32XX\_PINMUX(45U, 2U)

[ 145](ti-cc32xx-pinctrl_8h.md#a93408262bf38798525fc1ed43b759759)#define MCAXR0\_P45 TI\_CC32XX\_PINMUX(45U, 6U)

[ 146](ti-cc32xx-pinctrl_8h.md#a41607ce5c19fb904cef1b5b9ff065bca)#define GSPI\_CLK\_P45 TI\_CC32XX\_PINMUX(45U, 7U)

147

[ 148](ti-cc32xx-pinctrl_8h.md#a0023dcef0f950996fb69b99ae6cb7529)#define GPIO0\_P50 TI\_CC32XX\_PINMUX(50U, 0U)

[ 149](ti-cc32xx-pinctrl_8h.md#aa8acf830a7e0ba5aef12422b0f594999)#define UART0\_CTSN\_P50 TI\_CC32XX\_PINMUX(50U, 12U)

[ 150](ti-cc32xx-pinctrl_8h.md#a2c2f38b43528c3d2ed0d909cb276a834)#define MCAXR1\_P50 TI\_CC32XX\_PINMUX(50U, 6U)

[ 151](ti-cc32xx-pinctrl_8h.md#a4b59e68f954e26a5a22a946c83c7b35c)#define GT\_CCP00\_P50 TI\_CC32XX\_PINMUX(50U, 7U)

[ 152](ti-cc32xx-pinctrl_8h.md#a9531166ec008c53ebcb3bb7770bc9cfb)#define GSPI\_CS\_P50 TI\_CC32XX\_PINMUX(50U, 9U)

[ 153](ti-cc32xx-pinctrl_8h.md#afc79f99843ab6ec1fcc46e475516d3ea)#define UART1\_RTS\_P50 TI\_CC32XX\_PINMUX(50U, 10U)

[ 154](ti-cc32xx-pinctrl_8h.md#a202ce4d02639e2277dc70f8c34e96796)#define UART0\_RTS\_P50 TI\_CC32XX\_PINMUX(50U, 3U)

[ 155](ti-cc32xx-pinctrl_8h.md#a92fa65531018efc9a2fe37d1920d609e)#define MCAXR0\_P50 TI\_CC32XX\_PINMUX(50U, 4U)

156

[ 157](ti-cc32xx-pinctrl_8h.md#a6f73c352c071329e8b51d62272e6b597)#define GPIO32\_P52 TI\_CC32XX\_PINMUX(52U, 0U)

[ 158](ti-cc32xx-pinctrl_8h.md#a4de157ff760a13c620d8bc5730166dfd)#define MCACLK\_P52 TI\_CC32XX\_PINMUX(52U, 2U)

[ 159](ti-cc32xx-pinctrl_8h.md#a85e3fa7f05e7b0f8d2b58741d42e90bc)#define MCAXR0\_P52 TI\_CC32XX\_PINMUX(52U, 4U)

[ 160](ti-cc32xx-pinctrl_8h.md#ae3dd30595d8647e48844b8b9a204eee4)#define UART0\_RTS\_P52 TI\_CC32XX\_PINMUX(52U, 6U)

[ 161](ti-cc32xx-pinctrl_8h.md#a0472ccf0e3dde61e9b10c4ee44034a05)#define GSPI\_MOSI\_P52 TI\_CC32XX\_PINMUX(52U, 8U)

162

[ 163](ti-cc32xx-pinctrl_8h.md#af1056beafa7c3f45e3096c66e1631096)#define GPIO30\_P53 TI\_CC32XX\_PINMUX(53U, 0U)

[ 164](ti-cc32xx-pinctrl_8h.md#afa26fef4c910605bfc58516bba2b0446)#define UART0\_TX\_P53 TI\_CC32XX\_PINMUX(53U, 9U)

[ 165](ti-cc32xx-pinctrl_8h.md#ad2986e8a3004f19836aaf1264bbb052d)#define MCACLK\_P53 TI\_CC32XX\_PINMUX(53U, 2U)

[ 166](ti-cc32xx-pinctrl_8h.md#a8433ec0dd136e712bcffc99562d77a13)#define MCAFSX\_P53 TI\_CC32XX\_PINMUX(53U, 3U)

[ 167](ti-cc32xx-pinctrl_8h.md#ac91e88a5f0e186cea7cf4c1089a93e7e)#define GT\_CCP05\_P53 TI\_CC32XX\_PINMUX(53U, 4U)

[ 168](ti-cc32xx-pinctrl_8h.md#aaadb7b665b0adb1eed8d7a632c361910)#define GSPI\_MISO\_P53 TI\_CC32XX\_PINMUX(53U, 7U)

169

[ 170](ti-cc32xx-pinctrl_8h.md#a581e291b3887f522a35a7529db6c6a9b)#define GPIO1\_P55 TI\_CC32XX\_PINMUX(55U, 0U)

[ 171](ti-cc32xx-pinctrl_8h.md#ae02a8d280e708f2b28314c565b8368c7)#define UART0\_TX\_P55 TI\_CC32XX\_PINMUX(55U, 3U)

[ 172](ti-cc32xx-pinctrl_8h.md#acd84f05bdec8c70ee04acb87020286a1)#define PCLK\_P55 TI\_CC32XX\_PINMUX(55U, 4U)

[ 173](ti-cc32xx-pinctrl_8h.md#a06c9f6cc98ffdc8b53495a785fbcb3bd)#define UART1\_TX\_P55 TI\_CC32XX\_PINMUX(55U, 6U)

[ 174](ti-cc32xx-pinctrl_8h.md#a8d323feb4cf8d2264da5f94853acfcd2)#define GT\_CCP01\_P55 TI\_CC32XX\_PINMUX(55U, 7U)

175

[ 176](ti-cc32xx-pinctrl_8h.md#ad92d7838cfa819c6ba4a896101d4ffca)#define GPIO2\_P57 TI\_CC32XX\_PINMUX(57U, 0U)

[ 177](ti-cc32xx-pinctrl_8h.md#a9220f19106cb9f8840a1b90607948dcc)#define UART0\_RX\_P57 TI\_CC32XX\_PINMUX(57U, 3U)

[ 178](ti-cc32xx-pinctrl_8h.md#a2a67e698005d5be4baf74216341adf8e)#define UART1\_RX\_P57 TI\_CC32XX\_PINMUX(57U, 6U)

[ 179](ti-cc32xx-pinctrl_8h.md#af126c52c2ae52c91b68e9184004cfdcf)#define GT\_CCP02\_P57 TI\_CC32XX\_PINMUX(57U, 7U)

180

[ 181](ti-cc32xx-pinctrl_8h.md#a70ea8f18a9106a3c5d43bbee1d8af546)#define GPIO3\_P58 TI\_CC32XX\_PINMUX(58U, 0U)

[ 182](ti-cc32xx-pinctrl_8h.md#a33fe230e16d7b9ddfc5c4e5f6affa32d)#define UART1\_TX\_P58 TI\_CC32XX\_PINMUX(58U, 6U)

[ 183](ti-cc32xx-pinctrl_8h.md#a97849d9928b913f404d1a7be447051bf)#define PDATA7\_P58 TI\_CC32XX\_PINMUX(58U, 7U)

184

[ 185](ti-cc32xx-pinctrl_8h.md#aa189b623df8558a6438d176fc406abc2)#define GPIO5\_P59 TI\_CC32XX\_PINMUX(59U, 0U)

[ 186](ti-cc32xx-pinctrl_8h.md#a20c1984c49c52b45fb9024d45a0bdb27)#define UART1\_RX\_P59 TI\_CC32XX\_PINMUX(59U, 6U)

[ 187](ti-cc32xx-pinctrl_8h.md#aa631c65c36a4db5ba54f9603427911d3)#define PDATA6\_P59 TI\_CC32XX\_PINMUX(59U, 4U)

188

[ 189](ti-cc32xx-pinctrl_8h.md#ae248cf8dc867d6f9114cd3aaa51b06ca)#define GPIO5\_P60 TI\_CC32XX\_PINMUX(60U, 0U)

[ 190](ti-cc32xx-pinctrl_8h.md#a0a03dacfa4378314839df59511f7af27)#define PDATA5\_P60 TI\_CC32XX\_PINMUX(60U, 4U)

[ 191](ti-cc32xx-pinctrl_8h.md#a7f6eb41b90608548c67fe52ac7285678)#define MCAXR1\_P60 TI\_CC32XX\_PINMUX(60U, 6U)

[ 192](ti-cc32xx-pinctrl_8h.md#adcfc77087d75e8f687ca40cf102c5672)#define GT\_CCP05\_P60 TI\_CC32XX\_PINMUX(60U, 7U)

193

[ 194](ti-cc32xx-pinctrl_8h.md#a9fdaf32c4cf8469a4965405f564066dc)#define GPIO6\_P61 TI\_CC32XX\_PINMUX(61U, 0U)

[ 195](ti-cc32xx-pinctrl_8h.md#a68e13f52aab072bee8eed2de25737730)#define UART0\_RTS\_P61 TI\_CC32XX\_PINMUX(61U, 5U)

[ 196](ti-cc32xx-pinctrl_8h.md#aca1510ae9b35a8c0f75d486bcd219feb)#define PDATA4\_P61 TI\_CC32XX\_PINMUX(61U, 4U)

[ 197](ti-cc32xx-pinctrl_8h.md#a182be28929eb2e11c780d3f7bd3914a6)#define UART1\_CTS\_P61 TI\_CC32XX\_PINMUX(61U, 3U)

[ 198](ti-cc32xx-pinctrl_8h.md#abebbd1dd7206417c61aff603dc0d3c3a)#define UART0\_CTS\_P61 TI\_CC32XX\_PINMUX(61U, 6U)

[ 199](ti-cc32xx-pinctrl_8h.md#a1de5f909c12eadb029562bf14197ffc7)#define GT\_CCP06\_P61 TI\_CC32XX\_PINMUX(61U, 7U)

200

[ 201](ti-cc32xx-pinctrl_8h.md#a0a6f11f997a0e220dfff39bb2b419219)#define GPIO7\_P62 TI\_CC32XX\_PINMUX(62U, 0U)

[ 202](ti-cc32xx-pinctrl_8h.md#a900e65546f481f00fc2cb80218063bfd)#define MCACLKX\_P62 TI\_CC32XX\_PINMUX(62U, 13U)

[ 203](ti-cc32xx-pinctrl_8h.md#a2f6c6154904c3dce5496d8c837e4fbf0)#define UART1\_RTS\_P62 TI\_CC32XX\_PINMUX(62U, 3U)

[ 204](ti-cc32xx-pinctrl_8h.md#af4ef5b36c0c036734bd924586fabc519)#define UART0\_RTS\_P62 TI\_CC32XX\_PINMUX(62U, 10U)

[ 205](ti-cc32xx-pinctrl_8h.md#a29e0564a1b5101a50836a9cfa97a7a63)#define UART0\_TX\_P62 TI\_CC32XX\_PINMUX(62U, 11U)

206

[ 207](ti-cc32xx-pinctrl_8h.md#ad36e2c84424950a91028054c3499b579)#define GPIO8\_P63 TI\_CC32XX\_PINMUX(63U, 0U)

[ 208](ti-cc32xx-pinctrl_8h.md#a2edc3859ba96c9902d3c5eb2298a86ca)#define SDCARD\_IRQ\_P63 TI\_CC32XX\_PINMUX(63U, 6U)

[ 209](ti-cc32xx-pinctrl_8h.md#a24efd787cbb04117197d27289eab0d83)#define MCAFSX\_P63 TI\_CC32XX\_PINMUX(63U, 7U)

[ 210](ti-cc32xx-pinctrl_8h.md#af36b5558e59ca508f363a52c3fb180a0)#define GT\_CCP06\_P63 TI\_CC32XX\_PINMUX(63U, 12U)

211

[ 212](ti-cc32xx-pinctrl_8h.md#a25a3031376018d5d679597770b0552f0)#define GPIO9\_P64 TI\_CC32XX\_PINMUX(64U, 0U)

[ 213](ti-cc32xx-pinctrl_8h.md#a4a276c8f1545d3b817ced42811b934f7)#define GT\_PWM05\_P64 TI\_CC32XX\_PINMUX(64U, 3U)

[ 214](ti-cc32xx-pinctrl_8h.md#a18587659510c1d7f7a3fc761b021999d)#define SDCARD\_DATA\_P64 TI\_CC32XX\_PINMUX(64U, 6U)

[ 215](ti-cc32xx-pinctrl_8h.md#a98e96c0252ec68f37144096625e1492d)#define MCAXR0\_P64 TI\_CC32XX\_PINMUX(64U, 7U)

[ 216](ti-cc32xx-pinctrl_8h.md#a45b13479b3cdedf5488f122a3b3ec288)#define GT\_CCP00\_P64 TI\_CC32XX\_PINMUX(64U, 12U)

217

219

220#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_TI\_CC32XX\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ti-cc32xx-pinctrl.h](ti-cc32xx-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
