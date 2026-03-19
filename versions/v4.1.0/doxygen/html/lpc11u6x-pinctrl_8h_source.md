---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lpc11u6x-pinctrl_8h_source.html
original_path: doxygen/html/lpc11u6x-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lpc11u6x-pinctrl.h

[Go to the documentation of this file.](lpc11u6x-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2020 Seagate Technology LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_LPC11U6X\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_LPC11U6X\_PINCTRL\_H\_

9

23

39

51

[ 52](lpc11u6x-pinctrl_8h.md#ab08f72eae45dd5656aeca24c346c8626)#define IOCON\_FUNC0 0

[ 53](lpc11u6x-pinctrl_8h.md#ab6449233bd56957c684b9ad694606e3a)#define IOCON\_FUNC1 1

[ 54](lpc11u6x-pinctrl_8h.md#a43ebb7abf055ce2491fbba5ef72f6fc7)#define IOCON\_FUNC2 2

[ 55](lpc11u6x-pinctrl_8h.md#ace4708e511b3aa9c352600604331bec0)#define IOCON\_FUNC3 3

[ 56](lpc11u6x-pinctrl_8h.md#ac621b96a2bd1ee57a83ff1af98287a8d)#define IOCON\_FUNC4 4

[ 57](lpc11u6x-pinctrl_8h.md#a0f9630599f40a3f96a5887c7e65508a9)#define IOCON\_FUNC5 5

58

[ 59](lpc11u6x-pinctrl_8h.md#afc593aafe607c88c52864ecb7586ffe9)#define IOCON\_MODE\_INACT (0 << 3) /\* No pull resistor. \*/

[ 60](lpc11u6x-pinctrl_8h.md#a270261df49234519bfd09e076dfcec6c)#define IOCON\_MODE\_PULLDOWN (1 << 3) /\* Enable pull-down resistor. \*/

[ 61](lpc11u6x-pinctrl_8h.md#ad8fe947d8e7076d6cec01a5b30261141)#define IOCON\_MODE\_PULLUP (2 << 3) /\* Enable Pull-up resistor. \*/

[ 62](lpc11u6x-pinctrl_8h.md#a53d705841cc362c6f43ffc1370d71726)#define IOCON\_MODE\_REPEATER (3 << 3) /\* Repeater mode. \*/

63

[ 64](lpc11u6x-pinctrl_8h.md#afb7c408ac1f52b7b7e46fde3061fe0b7)#define IOCON\_HYS\_EN (1 << 5) /\* Enable hysteresis. \*/

65

[ 66](lpc11u6x-pinctrl_8h.md#ae1fd1faa316f6c3108b499928f8c9922)#define IOCON\_INV\_EN (1 << 6) /\* Invert input polarity. \*/

67

68/\* Only for analog pins. \*/

[ 69](lpc11u6x-pinctrl_8h.md#a9a3d4f3e281c382f795b9a769073d4e4)#define IOCON\_ADMODE\_EN (0 << 7) /\* Enable analog input mode. \*/

[ 70](lpc11u6x-pinctrl_8h.md#a516e9d9bc7b1f3aaefd9d09c6ece74d2)#define IOCON\_DIGMODE\_EN (1 << 7) /\* Enable digital I/O mode. \*/

[ 71](lpc11u6x-pinctrl_8h.md#a5a141a4fd02a8a7204cb251e1815b2ff)#define IOCON\_FILTR\_DIS (1 << 8) /\* Disable noise filtering. \*/

72

73/\* Only for open-drain pins (I2C). \*/

[ 74](lpc11u6x-pinctrl_8h.md#aa7dd24866523506919c8f3fa7a8614a8)#define IOCON\_SFI2C\_EN (0 << 8) /\* I2C standard mode / Fast-mode. \*/

[ 75](lpc11u6x-pinctrl_8h.md#a897f505b779e01014e235f1d73745787)#define IOCON\_STDI2C\_EN (1 << 8) /\* GPIO functionality. \*/

[ 76](lpc11u6x-pinctrl_8h.md#a5454c9c23da82b9db63d63866d054989)#define IOCON\_FASTI2C\_EN (2 << 8) /\* I2C Fast-mode Plus. \*/

77

[ 78](lpc11u6x-pinctrl_8h.md#a226b54f672e61a7a2d2893d9ef8cbc9c)#define IOCON\_OPENDRAIN\_EN (1 << 10) /\* Enable open-drain mode. \*/

79

80/\*

81 \* The digital filter mode allows to discard input pulses shorter than

82 \* 1, 2 or 3 clock cycles.

83 \*/

[ 84](lpc11u6x-pinctrl_8h.md#a05f3ba263e98d5ee980f1604e5bb901c)#define IOCON\_S\_MODE\_0CLK (0 << 11) /\* No input filter. \*/

[ 85](lpc11u6x-pinctrl_8h.md#a7148355cde16d13476362ff1c1bc1668)#define IOCON\_S\_MODE\_1CLK (1 << 11)

[ 86](lpc11u6x-pinctrl_8h.md#a87827c87941a76ce73118c65afb439f5)#define IOCON\_S\_MODE\_2CLK (2 << 11)

[ 87](lpc11u6x-pinctrl_8h.md#a54dba7082ab18b6a15eea0a87c119a71)#define IOCON\_S\_MODE\_3CLK (3 << 11)

88

89/\*

90 \* Clock divisor.

91 \*/

[ 92](lpc11u6x-pinctrl_8h.md#a32dad85c69cde862614f7dc694de25e1)#define IOCON\_CLKDIV0 (0 << 13)

[ 93](lpc11u6x-pinctrl_8h.md#a9cf0243a32cce57e52c3b3931979a0c4)#define IOCON\_CLKDIV1 (1 << 13)

[ 94](lpc11u6x-pinctrl_8h.md#a05aed1b2f2679b3bb56a1bdc08e032a1)#define IOCON\_CLKDIV2 (2 << 13)

[ 95](lpc11u6x-pinctrl_8h.md#a96b9d2b722278cdc733ddec36aca82b8)#define IOCON\_CLKDIV3 (3 << 13)

[ 96](lpc11u6x-pinctrl_8h.md#a293173c3047155fd78ba45a0f4e464f5)#define IOCON\_CLKDIV4 (4 << 13)

[ 97](lpc11u6x-pinctrl_8h.md#aecba1dab2a9cb8c19052ab56c7efbc6d)#define IOCON\_CLKDIV5 (5 << 13)

[ 98](lpc11u6x-pinctrl_8h.md#a25f5cc1afc44889d9e77b62923135411)#define IOCON\_CLKDIV6 (6 << 13)

99

100

101/\*

102 \* Pin control definitions used by LPC pin control driver to make pinmux

103 \* selections.

104 \*/

105

[ 106](lpc11u6x-pinctrl_8h.md#a3c281dcff389739802d68c2fc59d608e)#define IOCON\_MUX(offset, type, mux) \

107 (((offset & 0xFFF) << 20) | \

108 (((type) & 0x3) << 18) | \

109 (((mux) & 0xF) << 0))

110

[ 111](lpc11u6x-pinctrl_8h.md#a9ae60793668890cd0dc2117dc64f02ba)#define IOCON\_TYPE\_D 0x0

[ 112](lpc11u6x-pinctrl_8h.md#a6c16820a5170feb2c133f82216318bbb)#define IOCON\_TYPE\_I 0x1

[ 113](lpc11u6x-pinctrl_8h.md#afd7386a10a00b7f0cfbb44d6ceb66df3)#define IOCON\_TYPE\_A 0x2

114

[ 115](lpc11u6x-pinctrl_8h.md#abd7869399ab5c12219c1d7e06885e391)#define RESET\_PIO0\_0 IOCON\_MUX(0, IOCON\_TYPE\_D, 0) /\* PIO0\_0 \*/

[ 116](lpc11u6x-pinctrl_8h.md#aa1d6732f64540461cae792821ac7b2d6)#define PIO0\_0\_PIO0\_0 IOCON\_MUX(0, IOCON\_TYPE\_D, 1) /\* PIO0\_0 \*/

[ 117](lpc11u6x-pinctrl_8h.md#ab44c7ff7f772892dbb66149d8064ba04)#define PIO0\_1\_PIO0\_1 IOCON\_MUX(1, IOCON\_TYPE\_D, 0) /\* PIO0\_1 \*/

[ 118](lpc11u6x-pinctrl_8h.md#a4d2452db92940671b276775adec24700)#define CLKOUT\_PIO0\_1 IOCON\_MUX(1, IOCON\_TYPE\_D, 1) /\* PIO0\_1 \*/

[ 119](lpc11u6x-pinctrl_8h.md#aa6fbfccc166375429d6c720684686a24)#define CT32B0\_MAT2\_PIO0\_1 IOCON\_MUX(1, IOCON\_TYPE\_D, 2) /\* PIO0\_1 \*/

[ 120](lpc11u6x-pinctrl_8h.md#a827fea9b1eb5d3d16dbb1f95bd06b40e)#define USB\_FTOGGLE\_PIO0\_1 IOCON\_MUX(1, IOCON\_TYPE\_D, 3) /\* PIO0\_1 \*/

[ 121](lpc11u6x-pinctrl_8h.md#ab5a06c37a003d97135fc0da7c9949f60)#define PIO0\_2\_PIO0\_2 IOCON\_MUX(2, IOCON\_TYPE\_D, 0) /\* PIO0\_2 \*/

[ 122](lpc11u6x-pinctrl_8h.md#a883806b472afb21f170006c620fe2b2d)#define SSP0\_SSEL\_PIO0\_2 IOCON\_MUX(2, IOCON\_TYPE\_D, 1) /\* PIO0\_2 \*/

[ 123](lpc11u6x-pinctrl_8h.md#a2c44ad39551919eaf469137d3d37f78b)#define CT16B0\_CAP0\_PIO0\_2 IOCON\_MUX(2, IOCON\_TYPE\_D, 2) /\* PIO0\_2 \*/

[ 124](lpc11u6x-pinctrl_8h.md#a497b4217421b6854a707201765ff12a8)#define R\_0\_PIO0\_2 IOCON\_MUX(2, IOCON\_TYPE\_D, 3) /\* PIO0\_2 \*/

[ 125](lpc11u6x-pinctrl_8h.md#a89f6d1689c8672f14033a31543ced43a)#define PIO0\_3\_PIO0\_3 IOCON\_MUX(3, IOCON\_TYPE\_D, 0) /\* PIO0\_3 \*/

[ 126](lpc11u6x-pinctrl_8h.md#a410001d990fb8424e9f6d75f6a7f2c67)#define USB\_VBUS\_PIO0\_3 IOCON\_MUX(3, IOCON\_TYPE\_D, 1) /\* PIO0\_3 \*/

[ 127](lpc11u6x-pinctrl_8h.md#a54242b6862e052d7d1c2ee998b6d3927)#define R\_1\_PIO0\_3 IOCON\_MUX(3, IOCON\_TYPE\_D, 2) /\* PIO0\_3 \*/

[ 128](lpc11u6x-pinctrl_8h.md#a017c42b9bbbacfbbd9310b3f1a918a66)#define PIO0\_4\_PIO0\_4 IOCON\_MUX(4, IOCON\_TYPE\_I, 0) /\* PIO0\_4 \*/

[ 129](lpc11u6x-pinctrl_8h.md#af03e2705d8630f60521f853e9b4b1d61)#define I2C0\_SCL\_PIO0\_4 IOCON\_MUX(4, IOCON\_TYPE\_I, 1) /\* PIO0\_4 \*/

[ 130](lpc11u6x-pinctrl_8h.md#ab0e34b062fd26c27d29891c77d8542a0)#define R\_2\_PIO0\_4 IOCON\_MUX(4, IOCON\_TYPE\_I, 2) /\* PIO0\_4 \*/

[ 131](lpc11u6x-pinctrl_8h.md#aa0fe8d6e7a4f69dd54980143f92df7ab)#define PIO0\_5\_PIO0\_5 IOCON\_MUX(5, IOCON\_TYPE\_I, 0) /\* PIO0\_5 \*/

[ 132](lpc11u6x-pinctrl_8h.md#a7a30f5f10c3c59925e18d0526fa94431)#define I2C0\_SDA\_PIO0\_5 IOCON\_MUX(5, IOCON\_TYPE\_I, 1) /\* PIO0\_5 \*/

[ 133](lpc11u6x-pinctrl_8h.md#a372339383fc7d4d6e70965b744c10e48)#define R\_3\_PIO0\_5 IOCON\_MUX(5, IOCON\_TYPE\_I, 2) /\* PIO0\_5 \*/

[ 134](lpc11u6x-pinctrl_8h.md#a50ab17a232562ebc41deb8238de35f20)#define PIO0\_6\_PIO0\_6 IOCON\_MUX(6, IOCON\_TYPE\_D, 0) /\* PIO0\_6 \*/

[ 135](lpc11u6x-pinctrl_8h.md#a0d784ee93461dd2f05beeb7c9cfa46b7)#define R\_PIO0\_6 IOCON\_MUX(6, IOCON\_TYPE\_D, 1) /\* PIO0\_6 \*/

[ 136](lpc11u6x-pinctrl_8h.md#a632c9844b7638e69f8846b845dce32f7)#define SSP0\_SCK\_PIO0\_6 IOCON\_MUX(6, IOCON\_TYPE\_D, 2) /\* PIO0\_6 \*/

[ 137](lpc11u6x-pinctrl_8h.md#a49f11eb792f5b0a7ecf80aeaa82291e2)#define R\_4\_PIO0\_6 IOCON\_MUX(6, IOCON\_TYPE\_D, 3) /\* PIO0\_6 \*/

[ 138](lpc11u6x-pinctrl_8h.md#a95b8cc1a76a6097556568f4554bf4e3f)#define PIO0\_7\_PIO0\_7 IOCON\_MUX(7, IOCON\_TYPE\_D, 0) /\* PIO0\_7 \*/

[ 139](lpc11u6x-pinctrl_8h.md#aad418e1711b045ea50806d464c92fbcf)#define U0\_CTS\_PIO0\_7 IOCON\_MUX(7, IOCON\_TYPE\_D, 1) /\* PIO0\_7 \*/

[ 140](lpc11u6x-pinctrl_8h.md#aea308935da9604f8bdfea4d58959e518)#define R\_5\_PIO0\_7 IOCON\_MUX(7, IOCON\_TYPE\_D, 2) /\* PIO0\_7 \*/

[ 141](lpc11u6x-pinctrl_8h.md#a747ec67e7cb403d747b9f57429b71983)#define I2C1\_SCL\_PIO0\_7 IOCON\_MUX(7, IOCON\_TYPE\_D, 3) /\* PIO0\_7 \*/

[ 142](lpc11u6x-pinctrl_8h.md#a9e4b255125ef44e2de5c77743b4010ee)#define PIO0\_8\_PIO0\_8 IOCON\_MUX(8, IOCON\_TYPE\_D, 0) /\* PIO0\_8 \*/

[ 143](lpc11u6x-pinctrl_8h.md#a1d448d4e7bfeed79bc6e3fb14947afa7)#define SSP0\_MISO\_PIO0\_8 IOCON\_MUX(8, IOCON\_TYPE\_D, 1) /\* PIO0\_8 \*/

[ 144](lpc11u6x-pinctrl_8h.md#ad3f05ac410ca8c36aa81a57b635c1bb5)#define CT16B0\_MAT0\_PIO0\_8 IOCON\_MUX(8, IOCON\_TYPE\_D, 2) /\* PIO0\_8 \*/

[ 145](lpc11u6x-pinctrl_8h.md#a8feac8b8845786a001a5dedbd2c749cd)#define R\_6\_PIO0\_8 IOCON\_MUX(8, IOCON\_TYPE\_D, 3) /\* PIO0\_8 \*/

[ 146](lpc11u6x-pinctrl_8h.md#a0db63ca26d440f3bc24a48d39fbfcc4b)#define PIO0\_9\_PIO0\_9 IOCON\_MUX(9, IOCON\_TYPE\_D, 0) /\* PIO0\_9 \*/

[ 147](lpc11u6x-pinctrl_8h.md#af1a1f4c533ae4806d692aff574334ebf)#define SSP0\_MOSI\_PIO0\_9 IOCON\_MUX(9, IOCON\_TYPE\_D, 1) /\* PIO0\_9 \*/

[ 148](lpc11u6x-pinctrl_8h.md#a8f50532277b4b0b30b926e1f67a31cf1)#define CT16B0\_MAT1\_PIO0\_9 IOCON\_MUX(9, IOCON\_TYPE\_D, 2) /\* PIO0\_9 \*/

[ 149](lpc11u6x-pinctrl_8h.md#add1b38cd0b4e6b4557b5feeb39df424e)#define R\_7\_PIO0\_9 IOCON\_MUX(9, IOCON\_TYPE\_D, 3) /\* PIO0\_9 \*/

[ 150](lpc11u6x-pinctrl_8h.md#a9694c0dc682d5d6be38b963226aaef3c)#define SWCLK\_PIO0\_10 IOCON\_MUX(10, IOCON\_TYPE\_D, 0) /\* PIO0\_10 \*/

[ 151](lpc11u6x-pinctrl_8h.md#a0b09489a89b80784605cddcc430914d6)#define PIO0\_10\_PIO0\_10 IOCON\_MUX(10, IOCON\_TYPE\_D, 1) /\* PIO0\_10 \*/

[ 152](lpc11u6x-pinctrl_8h.md#ad68005dc04bde783a05f6c47da6dc4ef)#define SSP0\_SCK\_PIO0\_10 IOCON\_MUX(10, IOCON\_TYPE\_D, 2) /\* PIO0\_10 \*/

[ 153](lpc11u6x-pinctrl_8h.md#adca5657fc469b0f579f7a42f94ca5261)#define CT16B0\_MAT2\_PIO0\_10 IOCON\_MUX(10, IOCON\_TYPE\_D, 3) /\* PIO0\_10 \*/

[ 154](lpc11u6x-pinctrl_8h.md#afbfb770c4372aadbdb6f5c18d399e17e)#define TDI\_PIO0\_11 IOCON\_MUX(11, IOCON\_TYPE\_A, 0) /\* PIO0\_11 \*/

[ 155](lpc11u6x-pinctrl_8h.md#a157b55ccf1883066cc9217629366b809)#define PIO0\_11\_PIO0\_11 IOCON\_MUX(11, IOCON\_TYPE\_A, 1) /\* PIO0\_11 \*/

[ 156](lpc11u6x-pinctrl_8h.md#abfeca937f748f0b54ee4178c072ed1f5)#define ADC\_9\_PIO0\_11 IOCON\_MUX(11, IOCON\_TYPE\_A, 2) /\* PIO0\_11 \*/

[ 157](lpc11u6x-pinctrl_8h.md#a005db7665d634e68c56b59a3cb5b456d)#define CT32B0\_MAT3\_PIO0\_11 IOCON\_MUX(11, IOCON\_TYPE\_A, 3) /\* PIO0\_11 \*/

[ 158](lpc11u6x-pinctrl_8h.md#aaa87da84c9da4433539b55b513ab932b)#define U1\_RTS\_PIO0\_11 IOCON\_MUX(11, IOCON\_TYPE\_A, 4) /\* PIO0\_11 \*/

[ 159](lpc11u6x-pinctrl_8h.md#a3c5e8df87f093df6858f6ceb7e33e5ec)#define U1\_SCLK\_PIO0\_11 IOCON\_MUX(11, IOCON\_TYPE\_A, 5) /\* PIO0\_11 \*/

[ 160](lpc11u6x-pinctrl_8h.md#a8e608b93b683519cda35d166e08ab587)#define TMS\_PIO0\_12 IOCON\_MUX(12, IOCON\_TYPE\_A, 0) /\* PIO0\_12 \*/

[ 161](lpc11u6x-pinctrl_8h.md#ab4b3327e260eccbcccf80f0c1904ac56)#define PIO0\_12\_PIO0\_12 IOCON\_MUX(12, IOCON\_TYPE\_A, 1) /\* PIO0\_12 \*/

[ 162](lpc11u6x-pinctrl_8h.md#ae9f30a9545a11701304231e5efb707a5)#define ADC\_8\_PIO0\_12 IOCON\_MUX(12, IOCON\_TYPE\_A, 2) /\* PIO0\_12 \*/

[ 163](lpc11u6x-pinctrl_8h.md#a7b28030377332811f795cd1462bf631f)#define CT32B1\_CAP0\_PIO0\_12 IOCON\_MUX(12, IOCON\_TYPE\_A, 3) /\* PIO0\_12 \*/

[ 164](lpc11u6x-pinctrl_8h.md#ac58b55301756d90dcbfac6264df577b2)#define U1\_CTS\_PIO0\_12 IOCON\_MUX(12, IOCON\_TYPE\_A, 4) /\* PIO0\_12 \*/

165#define PIO0\_12\_PIO0\_12 IOCON\_MUX(12, IOCON\_TYPE\_A, 5) /\* PIO0\_12 \*/

[ 166](lpc11u6x-pinctrl_8h.md#ace1983c57935ab76096a42fa0d9af286)#define TDO\_PIO0\_13 IOCON\_MUX(13, IOCON\_TYPE\_A, 0) /\* PIO0\_13 \*/

[ 167](lpc11u6x-pinctrl_8h.md#af1f156f6bca42a308c3d154ce6033f5a)#define PIO0\_13\_PIO0\_13 IOCON\_MUX(13, IOCON\_TYPE\_A, 1) /\* PIO0\_13 \*/

[ 168](lpc11u6x-pinctrl_8h.md#a706b80599c77ce5212b2359187d3fab1)#define ADC\_7\_PIO0\_13 IOCON\_MUX(13, IOCON\_TYPE\_A, 2) /\* PIO0\_13 \*/

[ 169](lpc11u6x-pinctrl_8h.md#af55d0700864a68532d8b253344160ebf)#define CT32B1\_MAT0\_PIO0\_13 IOCON\_MUX(13, IOCON\_TYPE\_A, 3) /\* PIO0\_13 \*/

[ 170](lpc11u6x-pinctrl_8h.md#a3eb45ad4dd10da96ed90153ef3b53665)#define U1\_RXD\_PIO0\_13 IOCON\_MUX(13, IOCON\_TYPE\_A, 4) /\* PIO0\_13 \*/

171#define PIO0\_13\_PIO0\_13 IOCON\_MUX(13, IOCON\_TYPE\_A, 5) /\* PIO0\_13 \*/

[ 172](lpc11u6x-pinctrl_8h.md#ad8c652abc5c8558f9312bd0ea201d7fc)#define TRST\_PIO0\_14 IOCON\_MUX(14, IOCON\_TYPE\_A, 0) /\* PIO0\_14 \*/

[ 173](lpc11u6x-pinctrl_8h.md#a692e4e1765be1cbca9897691a6bfbc39)#define PIO0\_14\_PIO0\_14 IOCON\_MUX(14, IOCON\_TYPE\_A, 1) /\* PIO0\_14 \*/

[ 174](lpc11u6x-pinctrl_8h.md#ae6c3bb89b08367707e91bb00d3f55da5)#define ADC\_6\_PIO0\_14 IOCON\_MUX(14, IOCON\_TYPE\_A, 2) /\* PIO0\_14 \*/

[ 175](lpc11u6x-pinctrl_8h.md#acc4bcbd80fa3306bfa4ab8a4d3023c34)#define CT32B1\_MAT1\_PIO0\_14 IOCON\_MUX(14, IOCON\_TYPE\_A, 3) /\* PIO0\_14 \*/

[ 176](lpc11u6x-pinctrl_8h.md#a567bb0593686aa6552e868caeb623532)#define U1\_TXD\_PIO0\_14 IOCON\_MUX(14, IOCON\_TYPE\_A, 4) /\* PIO0\_14 \*/

[ 177](lpc11u6x-pinctrl_8h.md#a0b65345797054d59564518f73eee1602)#define SWDIO\_PIO0\_15 IOCON\_MUX(15, IOCON\_TYPE\_A, 0) /\* PIO0\_15 \*/

[ 178](lpc11u6x-pinctrl_8h.md#a59a92f1c63f7eb548a19f555cfe0208e)#define PIO0\_15\_PIO0\_15 IOCON\_MUX(15, IOCON\_TYPE\_A, 1) /\* PIO0\_15 \*/

[ 179](lpc11u6x-pinctrl_8h.md#af92fd1b534c099ad808403a199cad8a0)#define ADC\_3\_PIO0\_15 IOCON\_MUX(15, IOCON\_TYPE\_A, 2) /\* PIO0\_15 \*/

[ 180](lpc11u6x-pinctrl_8h.md#ac5ed12914616e50cac147b251291d3f6)#define CT32B1\_MAT2\_PIO0\_15 IOCON\_MUX(15, IOCON\_TYPE\_A, 3) /\* PIO0\_15 \*/

[ 181](lpc11u6x-pinctrl_8h.md#a285bf9c6e5c1b7bfc8ada6ececbe466e)#define WAKEUP\_PIO0\_16 IOCON\_MUX(16, IOCON\_TYPE\_A, 0) /\* PIO0\_16 \*/

[ 182](lpc11u6x-pinctrl_8h.md#aa4a10249e5ee8e04ce01f62864476727)#define PIO0\_16\_PIO0\_16 IOCON\_MUX(16, IOCON\_TYPE\_A, 1) /\* PIO0\_16 \*/

[ 183](lpc11u6x-pinctrl_8h.md#a21eeb0732f5d35d747f63db3eac9cfad)#define ADC\_2\_PIO0\_16 IOCON\_MUX(16, IOCON\_TYPE\_A, 2) /\* PIO0\_16 \*/

[ 184](lpc11u6x-pinctrl_8h.md#a26ecf5bab459bde9bbb64ff5a019b09a)#define CT32B1\_MAT3\_PIO0\_16 IOCON\_MUX(16, IOCON\_TYPE\_A, 3) /\* PIO0\_16 \*/

[ 185](lpc11u6x-pinctrl_8h.md#a58df208f71b6efffed28bbabddf45f41)#define R\_8\_PIO0\_16 IOCON\_MUX(16, IOCON\_TYPE\_A, 4) /\* PIO0\_16 \*/

[ 186](lpc11u6x-pinctrl_8h.md#a34451e215c47228b8337d0aed0c2c929)#define PIO0\_17\_PIO0\_17 IOCON\_MUX(17, IOCON\_TYPE\_D, 0) /\* PIO0\_17 \*/

[ 187](lpc11u6x-pinctrl_8h.md#ad946bbd06292183b7bdcd8db7d93d980)#define U0\_RTS\_PIO0\_17 IOCON\_MUX(17, IOCON\_TYPE\_D, 1) /\* PIO0\_17 \*/

[ 188](lpc11u6x-pinctrl_8h.md#afa844a06c34eb41b114b49aac65d5eb1)#define CT32B0\_CAP0\_PIO0\_17 IOCON\_MUX(17, IOCON\_TYPE\_D, 2) /\* PIO0\_17 \*/

[ 189](lpc11u6x-pinctrl_8h.md#a5f911210bf444c31df578680aa92ba9e)#define U0\_SCLK\_PIO0\_17 IOCON\_MUX(17, IOCON\_TYPE\_D, 3) /\* PIO0\_17 \*/

[ 190](lpc11u6x-pinctrl_8h.md#a87d216855b3f78407343517d639cd75c)#define PIO0\_18\_PIO0\_18 IOCON\_MUX(18, IOCON\_TYPE\_D, 0) /\* PIO0\_18 \*/

[ 191](lpc11u6x-pinctrl_8h.md#a22d6493688b04414c7dc732d43f4c0f2)#define U0\_RXD\_PIO0\_18 IOCON\_MUX(18, IOCON\_TYPE\_D, 1) /\* PIO0\_18 \*/

[ 192](lpc11u6x-pinctrl_8h.md#a099d0dca10dd8ac2762ac340473a798b)#define CT32B0\_MAT0\_PIO0\_18 IOCON\_MUX(18, IOCON\_TYPE\_D, 2) /\* PIO0\_18 \*/

[ 193](lpc11u6x-pinctrl_8h.md#a83757ba41e5c8ff4a04384a6f59550e1)#define PIO0\_19\_PIO0\_19 IOCON\_MUX(19, IOCON\_TYPE\_D, 0) /\* PIO0\_19 \*/

[ 194](lpc11u6x-pinctrl_8h.md#a602172b5fe5dde4f7064ea152914e3b4)#define U0\_TXD\_PIO0\_19 IOCON\_MUX(19, IOCON\_TYPE\_D, 1) /\* PIO0\_19 \*/

[ 195](lpc11u6x-pinctrl_8h.md#a579df8a29d7f50a93ae328c1aec9385a)#define CT32B0\_MAT1\_PIO0\_19 IOCON\_MUX(19, IOCON\_TYPE\_D, 2) /\* PIO0\_19 \*/

[ 196](lpc11u6x-pinctrl_8h.md#a28a9784674717e3617070ed87923a1f1)#define PIO0\_20\_PIO0\_20 IOCON\_MUX(20, IOCON\_TYPE\_D, 0) /\* PIO0\_20 \*/

[ 197](lpc11u6x-pinctrl_8h.md#aa7942f15263a5a5c36bd4513da5223c2)#define CT16B1\_CAP0\_PIO0\_20 IOCON\_MUX(20, IOCON\_TYPE\_D, 1) /\* PIO0\_20 \*/

[ 198](lpc11u6x-pinctrl_8h.md#a9fc4de327d564720e61a338e4a5d3b5b)#define U2\_RXD\_PIO0\_20 IOCON\_MUX(20, IOCON\_TYPE\_D, 2) /\* PIO0\_20 \*/

[ 199](lpc11u6x-pinctrl_8h.md#abfb5b6fa233853dc18ed899fa4418b1b)#define PIO0\_21\_PIO0\_21 IOCON\_MUX(21, IOCON\_TYPE\_D, 0) /\* PIO0\_21 \*/

[ 200](lpc11u6x-pinctrl_8h.md#a91549c703ace01d5e5cd3f5477ec156e)#define CT16B1\_MAT0\_PIO0\_21 IOCON\_MUX(21, IOCON\_TYPE\_D, 1) /\* PIO0\_21 \*/

[ 201](lpc11u6x-pinctrl_8h.md#aaec77c9670e3e88d00641020ec0d47d6)#define SSP1\_MOSI\_PIO0\_21 IOCON\_MUX(21, IOCON\_TYPE\_D, 2) /\* PIO0\_21 \*/

[ 202](lpc11u6x-pinctrl_8h.md#a9df3dda1a040239ee21e73c813659ccd)#define PIO0\_22\_PIO0\_22 IOCON\_MUX(22, IOCON\_TYPE\_A, 0) /\* PIO0\_22 \*/

[ 203](lpc11u6x-pinctrl_8h.md#aafede8fcd15e8bfe236e95c9a7b49b96)#define ADC\_11\_PIO0\_22 IOCON\_MUX(22, IOCON\_TYPE\_A, 1) /\* PIO0\_22 \*/

[ 204](lpc11u6x-pinctrl_8h.md#a2630aa1a98d13baf6f04f78f005bf704)#define CT16B1\_CAP1\_PIO0\_22 IOCON\_MUX(22, IOCON\_TYPE\_A, 2) /\* PIO0\_22 \*/

[ 205](lpc11u6x-pinctrl_8h.md#a783a183d806cac03c7db41096bae4272)#define SSP1\_MISO\_PIO0\_22 IOCON\_MUX(22, IOCON\_TYPE\_A, 3) /\* PIO0\_22 \*/

[ 206](lpc11u6x-pinctrl_8h.md#a07878c04e96b6472f26d3760a42ac212)#define PIO0\_23\_PIO0\_23 IOCON\_MUX(23, IOCON\_TYPE\_A, 0) /\* PIO0\_23 \*/

[ 207](lpc11u6x-pinctrl_8h.md#ab00e7a1a150e2e1c9b45d86c850a4a0b)#define ADC\_1\_PIO0\_23 IOCON\_MUX(23, IOCON\_TYPE\_A, 1) /\* PIO0\_23 \*/

[ 208](lpc11u6x-pinctrl_8h.md#ab0d0d78534d6cc1d4cee77b3eee84114)#define R\_9\_PIO0\_23 IOCON\_MUX(23, IOCON\_TYPE\_A, 2) /\* PIO0\_23 \*/

[ 209](lpc11u6x-pinctrl_8h.md#a1b2efba93021237e6fd7e3e276fef4e5)#define U0\_RI\_PIO0\_23 IOCON\_MUX(23, IOCON\_TYPE\_A, 3) /\* PIO0\_23 \*/

[ 210](lpc11u6x-pinctrl_8h.md#a0a3ad1a37c02adc62dbae966523e6d4c)#define SSP1\_SSEL\_PIO0\_23 IOCON\_MUX(23, IOCON\_TYPE\_A, 4) /\* PIO0\_23 \*/

[ 211](lpc11u6x-pinctrl_8h.md#ac68053b619744fbf1c1f17f7b08cf580)#define PIO1\_0\_PIO1\_0 IOCON\_MUX(24, IOCON\_TYPE\_D, 0) /\* PIO1\_0 \*/

[ 212](lpc11u6x-pinctrl_8h.md#a5ee6340e6fe3b732b6d49bbef6c90155)#define CT32B1\_MAT0\_PIO1\_0 IOCON\_MUX(24, IOCON\_TYPE\_D, 1) /\* PIO1\_0 \*/

[ 213](lpc11u6x-pinctrl_8h.md#a1ac3960333408442de9bd74e694595de)#define R\_10\_PIO1\_0 IOCON\_MUX(24, IOCON\_TYPE\_D, 2) /\* PIO1\_0 \*/

[ 214](lpc11u6x-pinctrl_8h.md#a4319b4d5227cd2a7ff75de78a422a870)#define U2\_TXD\_PIO1\_0 IOCON\_MUX(24, IOCON\_TYPE\_D, 3) /\* PIO1\_0 \*/

[ 215](lpc11u6x-pinctrl_8h.md#a299fee16f12cef2f585e132548ba3b72)#define PIO1\_1\_PIO1\_1 IOCON\_MUX(25, IOCON\_TYPE\_D, 0) /\* PIO1\_1 \*/

[ 216](lpc11u6x-pinctrl_8h.md#afb61298e6db2c507f6090a86566edc91)#define CT32B1\_MAT1\_PIO1\_1 IOCON\_MUX(25, IOCON\_TYPE\_D, 1) /\* PIO1\_1 \*/

[ 217](lpc11u6x-pinctrl_8h.md#aaae95bceef30b054294e7a7eed2d68a4)#define R\_11\_PIO1\_1 IOCON\_MUX(25, IOCON\_TYPE\_D, 2) /\* PIO1\_1 \*/

[ 218](lpc11u6x-pinctrl_8h.md#a7a17c6326f865f7eee09ec236ce12216)#define U0\_DTR\_PIO1\_1 IOCON\_MUX(25, IOCON\_TYPE\_D, 3) /\* PIO1\_1 \*/

[ 219](lpc11u6x-pinctrl_8h.md#a5265479414c8dd9845e6aa5213eda99e)#define PIO1\_2\_PIO1\_2 IOCON\_MUX(26, IOCON\_TYPE\_D, 0) /\* PIO1\_2 \*/

[ 220](lpc11u6x-pinctrl_8h.md#ab158e092af2c6ad056cc6f4d298c1951)#define CT32B1\_MAT2\_PIO1\_2 IOCON\_MUX(26, IOCON\_TYPE\_D, 1) /\* PIO1\_2 \*/

[ 221](lpc11u6x-pinctrl_8h.md#ac7bd9d42184bd9175925b2e789d4e0f8)#define R\_12\_PIO1\_2 IOCON\_MUX(26, IOCON\_TYPE\_D, 2) /\* PIO1\_2 \*/

[ 222](lpc11u6x-pinctrl_8h.md#a4af77ea4a454643946504e10d249edcc)#define U1\_RXD\_PIO1\_2 IOCON\_MUX(26, IOCON\_TYPE\_D, 3) /\* PIO1\_2 \*/

[ 223](lpc11u6x-pinctrl_8h.md#a2d403da5360929eed6c833567c415fe5)#define PIO1\_3\_PIO1\_3 IOCON\_MUX(27, IOCON\_TYPE\_A, 0) /\* PIO1\_3 \*/

[ 224](lpc11u6x-pinctrl_8h.md#a7edf5d0d95f5fa253b03ccc77447ed9a)#define CT32B1\_MAT3\_PIO1\_3 IOCON\_MUX(27, IOCON\_TYPE\_A, 1) /\* PIO1\_3 \*/

[ 225](lpc11u6x-pinctrl_8h.md#a1f35a5b9268e09e3ff279d0d7b27e8d9)#define R\_13\_PIO1\_3 IOCON\_MUX(27, IOCON\_TYPE\_A, 2) /\* PIO1\_3 \*/

[ 226](lpc11u6x-pinctrl_8h.md#ae63879080611307c152e569946e7a7ae)#define I2C1\_SDA\_PIO1\_3 IOCON\_MUX(27, IOCON\_TYPE\_A, 3) /\* PIO1\_3 \*/

[ 227](lpc11u6x-pinctrl_8h.md#ac4f0bd23dfc3f744220cadb6949d4e1f)#define ADC\_5\_PIO1\_3 IOCON\_MUX(27, IOCON\_TYPE\_A, 4) /\* PIO1\_3 \*/

[ 228](lpc11u6x-pinctrl_8h.md#aecf77d09221ba70819899708b4ad74a8)#define PIO1\_4\_PIO1\_4 IOCON\_MUX(28, IOCON\_TYPE\_D, 0) /\* PIO1\_4 \*/

[ 229](lpc11u6x-pinctrl_8h.md#a54bfd60ff58b0148b6848f8b2982442e)#define CT32B1\_CAP0\_PIO1\_4 IOCON\_MUX(28, IOCON\_TYPE\_D, 1) /\* PIO1\_4 \*/

[ 230](lpc11u6x-pinctrl_8h.md#aaba8b00d104b3163f0c7cee32b91cf1e)#define R\_14\_PIO1\_4 IOCON\_MUX(28, IOCON\_TYPE\_D, 2) /\* PIO1\_4 \*/

[ 231](lpc11u6x-pinctrl_8h.md#a0a7cdf5fa1cae307725c7cf8742cc599)#define U0\_DSR\_PIO1\_4 IOCON\_MUX(28, IOCON\_TYPE\_D, 3) /\* PIO1\_4 \*/

[ 232](lpc11u6x-pinctrl_8h.md#ab070530de6c3105054206c5a526f5730)#define PIO1\_5\_PIO1\_5 IOCON\_MUX(29, IOCON\_TYPE\_D, 0) /\* PIO1\_5 \*/

[ 233](lpc11u6x-pinctrl_8h.md#a1ab5d0cd48d5ade99b0a6e4fc8bc9f68)#define CT32B1\_CAP1\_PIO1\_5 IOCON\_MUX(29, IOCON\_TYPE\_D, 1) /\* PIO1\_5 \*/

[ 234](lpc11u6x-pinctrl_8h.md#adcccebfaed3f6f65e12a4052ff04fdcd)#define R\_15\_PIO1\_5 IOCON\_MUX(29, IOCON\_TYPE\_D, 2) /\* PIO1\_5 \*/

[ 235](lpc11u6x-pinctrl_8h.md#a0abbdcaf023079f9181f260779ced50e)#define U0\_DCD\_PIO1\_5 IOCON\_MUX(29, IOCON\_TYPE\_D, 3) /\* PIO1\_5 \*/

[ 236](lpc11u6x-pinctrl_8h.md#af6b1804a5aefa54e7a3c4dba33394805)#define PIO1\_6\_PIO1\_6 IOCON\_MUX(30, IOCON\_TYPE\_D, 0) /\* PIO1\_6 \*/

[ 237](lpc11u6x-pinctrl_8h.md#a9f77fd7bcd00d7bc4e179cb3c3db622e)#define R\_16\_PIO1\_6 IOCON\_MUX(30, IOCON\_TYPE\_D, 1) /\* PIO1\_6 \*/

[ 238](lpc11u6x-pinctrl_8h.md#a48ac3c0096037bbe64d92b2d2b0e621f)#define U2\_RXD\_PIO1\_6 IOCON\_MUX(30, IOCON\_TYPE\_D, 2) /\* PIO1\_6 \*/

[ 239](lpc11u6x-pinctrl_8h.md#a01c2a127b550f1c904cf747a2351c006)#define CT32B0\_CAP1\_PIO1\_6 IOCON\_MUX(30, IOCON\_TYPE\_D, 3) /\* PIO1\_6 \*/

[ 240](lpc11u6x-pinctrl_8h.md#ab77050cd6c5323ede0c6ce3f52f4f83e)#define PIO1\_7\_PIO1\_7 IOCON\_MUX(31, IOCON\_TYPE\_D, 0) /\* PIO1\_7 \*/

[ 241](lpc11u6x-pinctrl_8h.md#a2478b21ed3999f9fb27e1ddcc555383f)#define R\_17\_PIO1\_7 IOCON\_MUX(31, IOCON\_TYPE\_D, 1) /\* PIO1\_7 \*/

[ 242](lpc11u6x-pinctrl_8h.md#a23bb3cc2ede010588651fede510df3db)#define U2\_CTS\_PIO1\_7 IOCON\_MUX(31, IOCON\_TYPE\_D, 2) /\* PIO1\_7 \*/

[ 243](lpc11u6x-pinctrl_8h.md#a6673a36d9b33d563295063f73c466b58)#define CT16B1\_CAP0\_PIO1\_7 IOCON\_MUX(31, IOCON\_TYPE\_D, 3) /\* PIO1\_7 \*/

[ 244](lpc11u6x-pinctrl_8h.md#a5eb361e081a52918777d89f61c0a26fa)#define PIO1\_8\_PIO1\_8 IOCON\_MUX(32, IOCON\_TYPE\_D, 0) /\* PIO1\_8 \*/

[ 245](lpc11u6x-pinctrl_8h.md#a01a390f0311638bc09569b06839fb7dd)#define R\_18\_PIO1\_8 IOCON\_MUX(32, IOCON\_TYPE\_D, 1) /\* PIO1\_8 \*/

[ 246](lpc11u6x-pinctrl_8h.md#a253fad10b49809895c3f27ec3e51a567)#define U1\_TXD\_PIO1\_8 IOCON\_MUX(32, IOCON\_TYPE\_D, 2) /\* PIO1\_8 \*/

[ 247](lpc11u6x-pinctrl_8h.md#a598b61d037bfcacc335bf0996a477843)#define CT16B0\_CAP0\_PIO1\_8 IOCON\_MUX(32, IOCON\_TYPE\_D, 3) /\* PIO1\_8 \*/

[ 248](lpc11u6x-pinctrl_8h.md#a75ab800970f73ac0177aaf8139ba8739)#define PIO1\_9\_PIO1\_9 IOCON\_MUX(33, IOCON\_TYPE\_A, 0) /\* PIO1\_9 \*/

[ 249](lpc11u6x-pinctrl_8h.md#a5ec91d14ec34a2080c1d857e1fd6f572)#define U0\_CTS\_PIO1\_9 IOCON\_MUX(33, IOCON\_TYPE\_A, 1) /\* PIO1\_9 \*/

[ 250](lpc11u6x-pinctrl_8h.md#a9db77081025e9907d1d90cf993d8a028)#define CT16B1\_MAT1\_PIO1\_9 IOCON\_MUX(33, IOCON\_TYPE\_A, 2) /\* PIO1\_9 \*/

[ 251](lpc11u6x-pinctrl_8h.md#a03ce0c70811dc7195ee48649532f2ebd)#define ADC\_0\_PIO1\_9 IOCON\_MUX(33, IOCON\_TYPE\_A, 3) /\* PIO1\_9 \*/

[ 252](lpc11u6x-pinctrl_8h.md#a037f6a357a5bbea0dc0cb9902c94c846)#define PIO1\_10\_PIO1\_10 IOCON\_MUX(34, IOCON\_TYPE\_D, 0) /\* PIO1\_10 \*/

[ 253](lpc11u6x-pinctrl_8h.md#a2f2957c1a43d63106ce2d61678103f62)#define U2\_RTS\_PIO1\_10 IOCON\_MUX(34, IOCON\_TYPE\_D, 1) /\* PIO1\_10 \*/

[ 254](lpc11u6x-pinctrl_8h.md#ac7236d26fd68c0be4b0f80e7ac6614cd)#define U2\_SCLK\_PIO1\_10 IOCON\_MUX(34, IOCON\_TYPE\_D, 2) /\* PIO1\_10 \*/

[ 255](lpc11u6x-pinctrl_8h.md#abd7606b5f7f902397d6c2ab8fedfd2b3)#define CT16B1\_MAT0\_PIO1\_10 IOCON\_MUX(34, IOCON\_TYPE\_D, 3) /\* PIO1\_10 \*/

[ 256](lpc11u6x-pinctrl_8h.md#a97b3bfd02acef68ffc82952e49bd03fe)#define PIO1\_11\_PIO1\_11 IOCON\_MUX(35, IOCON\_TYPE\_D, 0) /\* PIO1\_11 \*/

[ 257](lpc11u6x-pinctrl_8h.md#abd5321e5d55560fb0927e8a26027d001)#define I2C1\_SCL\_PIO1\_11 IOCON\_MUX(35, IOCON\_TYPE\_D, 1) /\* PIO1\_11 \*/

[ 258](lpc11u6x-pinctrl_8h.md#ad0ae914ba48296f972618dee04cc6490)#define CT16B0\_MAT2\_PIO1\_11 IOCON\_MUX(35, IOCON\_TYPE\_D, 2) /\* PIO1\_11 \*/

[ 259](lpc11u6x-pinctrl_8h.md#aa43f68879f82d124e3d1da1b1a4bee16)#define U0\_RI\_PIO1\_11 IOCON\_MUX(35, IOCON\_TYPE\_D, 3) /\* PIO1\_11 \*/

[ 260](lpc11u6x-pinctrl_8h.md#a896bd464fd196266a8862fde369e899b)#define PIO1\_12\_PIO1\_12 IOCON\_MUX(36, IOCON\_TYPE\_D, 0) /\* PIO1\_12 \*/

[ 261](lpc11u6x-pinctrl_8h.md#a0bc3c1d34d0bc7a92543edd4e743905f)#define SSP0\_MOSI\_PIO1\_12 IOCON\_MUX(36, IOCON\_TYPE\_D, 1) /\* PIO1\_12 \*/

[ 262](lpc11u6x-pinctrl_8h.md#a5b8fcd82c3feca9ed3dfbd2f905b4a74)#define CT16B0\_MAT1\_PIO1\_12 IOCON\_MUX(36, IOCON\_TYPE\_D, 2) /\* PIO1\_12 \*/

[ 263](lpc11u6x-pinctrl_8h.md#abe8e17586c29617e61a2671408e84637)#define R\_21\_PIO1\_12 IOCON\_MUX(36, IOCON\_TYPE\_D, 3) /\* PIO1\_12 \*/

[ 264](lpc11u6x-pinctrl_8h.md#ad2d3d8b8bb3a17fab2dc03850b9934e6)#define PIO1\_13\_PIO1\_13 IOCON\_MUX(37, IOCON\_TYPE\_D, 0) /\* PIO1\_13 \*/

[ 265](lpc11u6x-pinctrl_8h.md#ad00e6299050aceda961b3b6af7a78f79)#define U1\_CTS\_PIO1\_13 IOCON\_MUX(37, IOCON\_TYPE\_D, 1) /\* PIO1\_13 \*/

[ 266](lpc11u6x-pinctrl_8h.md#a504a57a6c6e3014ed4df4320736c7713)#define SCT0\_OUT3\_PIO1\_13 IOCON\_MUX(37, IOCON\_TYPE\_D, 2) /\* PIO1\_13 \*/

[ 267](lpc11u6x-pinctrl_8h.md#a8613dd791e9ddf76c84d12c9f25f31ed)#define R\_22\_PIO1\_13 IOCON\_MUX(37, IOCON\_TYPE\_D, 3) /\* PIO1\_13 \*/

[ 268](lpc11u6x-pinctrl_8h.md#aec627d88659627216048116352084463)#define PIO1\_14\_PIO1\_14 IOCON\_MUX(38, IOCON\_TYPE\_D, 0) /\* PIO1\_14 \*/

[ 269](lpc11u6x-pinctrl_8h.md#aa478831aabf3f70f44dc83be779f29df)#define I2C1\_SDA\_PIO1\_14 IOCON\_MUX(38, IOCON\_TYPE\_D, 1) /\* PIO1\_14 \*/

[ 270](lpc11u6x-pinctrl_8h.md#a7e9fefa7d3b24bcf91c2af8143934e1b)#define CT32B1\_MAT2\_PIO1\_14 IOCON\_MUX(38, IOCON\_TYPE\_D, 2) /\* PIO1\_14 \*/

[ 271](lpc11u6x-pinctrl_8h.md#a75b2a3bdcdc904bce2ed4641fd77d36f)#define R\_23\_PIO1\_14 IOCON\_MUX(38, IOCON\_TYPE\_D, 3) /\* PIO1\_14 \*/

[ 272](lpc11u6x-pinctrl_8h.md#ad430442be04fb9768354a29392aa3150)#define PIO1\_15\_PIO1\_15 IOCON\_MUX(39, IOCON\_TYPE\_D, 0) /\* PIO1\_15 \*/

[ 273](lpc11u6x-pinctrl_8h.md#acc0fec039c618cf46e788bfb6f651cfe)#define SSP0\_SSEL\_PIO1\_15 IOCON\_MUX(39, IOCON\_TYPE\_D, 1) /\* PIO1\_15 \*/

[ 274](lpc11u6x-pinctrl_8h.md#af960ef8b39ccd08fbe57d0fb2808507a)#define CT32B1\_MAT3\_PIO1\_15 IOCON\_MUX(39, IOCON\_TYPE\_D, 2) /\* PIO1\_15 \*/

[ 275](lpc11u6x-pinctrl_8h.md#a31607e58141be4451603b21142dc2b78)#define R\_24\_PIO1\_15 IOCON\_MUX(39, IOCON\_TYPE\_D, 3) /\* PIO1\_15 \*/

[ 276](lpc11u6x-pinctrl_8h.md#a890647261f0d13600177b8da109e7f80)#define PIO1\_16\_PIO1\_16 IOCON\_MUX(40, IOCON\_TYPE\_D, 0) /\* PIO1\_16 \*/

[ 277](lpc11u6x-pinctrl_8h.md#adb527bbcf8d059c9bfccdf29f3ac4aa5)#define SSP0\_MISO\_PIO1\_16 IOCON\_MUX(40, IOCON\_TYPE\_D, 1) /\* PIO1\_16 \*/

[ 278](lpc11u6x-pinctrl_8h.md#acead3031fd80d06b2f87cf0ad8e9e8e2)#define CT16B0\_MAT0\_PIO1\_16 IOCON\_MUX(40, IOCON\_TYPE\_D, 2) /\* PIO1\_16 \*/

[ 279](lpc11u6x-pinctrl_8h.md#afbf96bb8cc6cf2f8f56ac0f48de55a9d)#define R\_25\_PIO1\_16 IOCON\_MUX(40, IOCON\_TYPE\_D, 3) /\* PIO1\_16 \*/

[ 280](lpc11u6x-pinctrl_8h.md#ab7c4014e4c5aff2215d00bfbfcdca7c6)#define PIO1\_17\_PIO1\_17 IOCON\_MUX(41, IOCON\_TYPE\_D, 0) /\* PIO1\_17 \*/

[ 281](lpc11u6x-pinctrl_8h.md#a27237240e4f0c84be58ac4a40915b30b)#define CT16B0\_CAP2\_PIO1\_17 IOCON\_MUX(41, IOCON\_TYPE\_D, 1) /\* PIO1\_17 \*/

[ 282](lpc11u6x-pinctrl_8h.md#a974de383ed91f1e80b6e67ab95f627d3)#define U0\_RXD\_PIO1\_17 IOCON\_MUX(41, IOCON\_TYPE\_D, 2) /\* PIO1\_17 \*/

[ 283](lpc11u6x-pinctrl_8h.md#a485ea3b9fe56406e22a835ad8101ca2a)#define R\_26\_PIO1\_17 IOCON\_MUX(41, IOCON\_TYPE\_D, 3) /\* PIO1\_17 \*/

[ 284](lpc11u6x-pinctrl_8h.md#abd5742cad3a656c0cca0a02ec6b41acf)#define PIO1\_18\_PIO1\_18 IOCON\_MUX(42, IOCON\_TYPE\_D, 0) /\* PIO1\_18 \*/

[ 285](lpc11u6x-pinctrl_8h.md#af2925353ca8342deac5cc6c47623b40c)#define CT16B1\_CAP1\_PIO1\_18 IOCON\_MUX(42, IOCON\_TYPE\_D, 1) /\* PIO1\_18 \*/

[ 286](lpc11u6x-pinctrl_8h.md#a15cb6f2cf2ca2ba9b04b54b490e2c88b)#define U0\_TXD\_PIO1\_18 IOCON\_MUX(42, IOCON\_TYPE\_D, 2) /\* PIO1\_18 \*/

[ 287](lpc11u6x-pinctrl_8h.md#a7a373b17b448fdd55c2b0b4e88750d38)#define R\_27\_PIO1\_18 IOCON\_MUX(42, IOCON\_TYPE\_D, 3) /\* PIO1\_18 \*/

[ 288](lpc11u6x-pinctrl_8h.md#ae56e1309f5dfaff815c892ef0e1ed2b9)#define PIO1\_19\_PIO1\_19 IOCON\_MUX(43, IOCON\_TYPE\_D, 0) /\* PIO1\_19 \*/

[ 289](lpc11u6x-pinctrl_8h.md#a14b9435d73cf7890108f3f7e929154e7)#define U2\_CTS\_PIO1\_19 IOCON\_MUX(43, IOCON\_TYPE\_D, 1) /\* PIO1\_19 \*/

[ 290](lpc11u6x-pinctrl_8h.md#ac19819cd774abe2a0597247136804d2e)#define SCT0\_OUT0\_PIO1\_19 IOCON\_MUX(43, IOCON\_TYPE\_D, 2) /\* PIO1\_19 \*/

[ 291](lpc11u6x-pinctrl_8h.md#a1a87c8b465b4539dee7d82dcf0067d5b)#define R\_28\_PIO1\_19 IOCON\_MUX(43, IOCON\_TYPE\_D, 3) /\* PIO1\_19 \*/

[ 292](lpc11u6x-pinctrl_8h.md#adea5f43202f54b478043589ea1d4b1e1)#define PIO1\_20\_PIO1\_20 IOCON\_MUX(44, IOCON\_TYPE\_D, 0) /\* PIO1\_20 \*/

[ 293](lpc11u6x-pinctrl_8h.md#a3ed819b62c0253666670f98230fb6194)#define U0\_DSR\_PIO1\_20 IOCON\_MUX(44, IOCON\_TYPE\_D, 1) /\* PIO1\_20 \*/

[ 294](lpc11u6x-pinctrl_8h.md#af998519da9f4ffd89b606b0261f95a1e)#define SSP1\_SCK\_PIO1\_20 IOCON\_MUX(44, IOCON\_TYPE\_D, 2) /\* PIO1\_20 \*/

[ 295](lpc11u6x-pinctrl_8h.md#a55e45a077e426ae5e06508b66d899c4c)#define CT16B0\_MAT0\_PIO1\_20 IOCON\_MUX(44, IOCON\_TYPE\_D, 3) /\* PIO1\_20 \*/

[ 296](lpc11u6x-pinctrl_8h.md#a0c6805b1f84117dee5e66f091818d9ca)#define PIO1\_21\_PIO1\_21 IOCON\_MUX(45, IOCON\_TYPE\_D, 0) /\* PIO1\_21 \*/

[ 297](lpc11u6x-pinctrl_8h.md#aaf239310ed5db40a24ca15cc7f48ed2b)#define U0\_DCD\_PIO1\_21 IOCON\_MUX(45, IOCON\_TYPE\_D, 1) /\* PIO1\_21 \*/

[ 298](lpc11u6x-pinctrl_8h.md#af44b09e3f6bf4ac86fae8f257a0620c6)#define SSP1\_MISO\_PIO1\_21 IOCON\_MUX(45, IOCON\_TYPE\_D, 2) /\* PIO1\_21 \*/

[ 299](lpc11u6x-pinctrl_8h.md#a1ef21fd46fa25d46c8eb7b8881f4b08c)#define CT16B0\_CAP1\_PIO1\_21 IOCON\_MUX(45, IOCON\_TYPE\_D, 3) /\* PIO1\_21 \*/

[ 300](lpc11u6x-pinctrl_8h.md#a689cbb1bd742d803a7d512f5be6c4cfb)#define PIO1\_22\_PIO1\_22 IOCON\_MUX(46, IOCON\_TYPE\_A, 0) /\* PIO1\_22 \*/

[ 301](lpc11u6x-pinctrl_8h.md#aa39927fc00dacde807c16c4044fa62b5)#define SSP1\_MOSI\_PIO1\_22 IOCON\_MUX(46, IOCON\_TYPE\_A, 1) /\* PIO1\_22 \*/

[ 302](lpc11u6x-pinctrl_8h.md#a39a31d62e31f796e3a54f43056577675)#define CT32B1\_CAP1\_PIO1\_22 IOCON\_MUX(46, IOCON\_TYPE\_A, 2) /\* PIO1\_22 \*/

[ 303](lpc11u6x-pinctrl_8h.md#a9686cbbd0389bec5c771f2776f05cde7)#define ADC\_4\_PIO1\_22 IOCON\_MUX(46, IOCON\_TYPE\_A, 3) /\* PIO1\_22 \*/

[ 304](lpc11u6x-pinctrl_8h.md#adfbe0b94e760582fccaa92f88f41d1f4)#define R\_29\_PIO1\_22 IOCON\_MUX(46, IOCON\_TYPE\_A, 4) /\* PIO1\_22 \*/

[ 305](lpc11u6x-pinctrl_8h.md#ab15b87098dc679562fcd0eb74aa8c761)#define PIO1\_23\_PIO1\_23 IOCON\_MUX(47, IOCON\_TYPE\_D, 0) /\* PIO1\_23 \*/

[ 306](lpc11u6x-pinctrl_8h.md#aa168a44ff47701e1e090bc95de4b4601)#define CT16B1\_MAT1\_PIO1\_23 IOCON\_MUX(47, IOCON\_TYPE\_D, 1) /\* PIO1\_23 \*/

[ 307](lpc11u6x-pinctrl_8h.md#a241d8f9f8546f68c66e490a4f42951ca)#define SSP1\_SSEL\_PIO1\_23 IOCON\_MUX(47, IOCON\_TYPE\_D, 2) /\* PIO1\_23 \*/

[ 308](lpc11u6x-pinctrl_8h.md#adbafcde4cb5f052835ed790774e91a67)#define U2\_TXD\_PIO1\_23 IOCON\_MUX(47, IOCON\_TYPE\_D, 3) /\* PIO1\_23 \*/

[ 309](lpc11u6x-pinctrl_8h.md#a86877f01c21462c697dcdf1163ef2057)#define PIO1\_24\_PIO1\_24 IOCON\_MUX(48, IOCON\_TYPE\_D, 0) /\* PIO1\_24 \*/

[ 310](lpc11u6x-pinctrl_8h.md#aa5758ecd3938aa9210fad9e6a291fb54)#define CT32B0\_MAT0\_PIO1\_24 IOCON\_MUX(48, IOCON\_TYPE\_D, 1) /\* PIO1\_24 \*/

[ 311](lpc11u6x-pinctrl_8h.md#ae7f01370d20cb64565a5e0d17190f11c)#define I2C1\_SDA\_PIO1\_24 IOCON\_MUX(48, IOCON\_TYPE\_D, 2) /\* PIO1\_24 \*/

[ 312](lpc11u6x-pinctrl_8h.md#ad1f94b842d9d03ecfd95521ad4fc50ef)#define PIO1\_25\_PIO1\_25 IOCON\_MUX(49, IOCON\_TYPE\_D, 0) /\* PIO1\_25 \*/

[ 313](lpc11u6x-pinctrl_8h.md#afc6ec4baef4bad621e4d62ae945a1163)#define U2\_RTS\_PIO1\_25 IOCON\_MUX(49, IOCON\_TYPE\_D, 1) /\* PIO1\_25 \*/

[ 314](lpc11u6x-pinctrl_8h.md#a784ceb0c6b7772018f082fcd508cba4f)#define U2\_SCLK\_PIO1\_25 IOCON\_MUX(49, IOCON\_TYPE\_D, 2) /\* PIO1\_25 \*/

[ 315](lpc11u6x-pinctrl_8h.md#add2cbf06dc14447e4661ce8a3de45f2f)#define SCT0\_IN0\_PIO1\_25 IOCON\_MUX(49, IOCON\_TYPE\_D, 3) /\* PIO1\_25 \*/

[ 316](lpc11u6x-pinctrl_8h.md#a387b44f72acc4eb20b382da8f076d195)#define R\_30\_PIO1\_25 IOCON\_MUX(49, IOCON\_TYPE\_D, 4) /\* PIO1\_25 \*/

[ 317](lpc11u6x-pinctrl_8h.md#a6b8c76bf4eb6a9e621363bbd7862a3c5)#define PIO1\_26\_PIO1\_26 IOCON\_MUX(50, IOCON\_TYPE\_D, 0) /\* PIO1\_26 \*/

[ 318](lpc11u6x-pinctrl_8h.md#a1733e97cfa0bb66c7717450596b0cfea)#define CT32B0\_MAT2\_PIO1\_26 IOCON\_MUX(50, IOCON\_TYPE\_D, 1) /\* PIO1\_26 \*/

[ 319](lpc11u6x-pinctrl_8h.md#a3cc2c9440f957296aa32d4636b2d6130)#define U0\_RXD\_PIO1\_26 IOCON\_MUX(50, IOCON\_TYPE\_D, 2) /\* PIO1\_26 \*/

[ 320](lpc11u6x-pinctrl_8h.md#ab0411bc0f8b6654e0f7bb8259cb47e7e)#define R\_19\_PIO1\_26 IOCON\_MUX(50, IOCON\_TYPE\_D, 3) /\* PIO1\_26 \*/

[ 321](lpc11u6x-pinctrl_8h.md#ac22ea9cd9fdb0dcf4125628fd41ad4e2)#define PIO1\_27\_PIO1\_27 IOCON\_MUX(51, IOCON\_TYPE\_D, 0) /\* PIO1\_27 \*/

[ 322](lpc11u6x-pinctrl_8h.md#ac2a89c71d21325e0e64cd8a3d8c4ebdc)#define CT32B0\_MAT3\_PIO1\_27 IOCON\_MUX(51, IOCON\_TYPE\_D, 1) /\* PIO1\_27 \*/

[ 323](lpc11u6x-pinctrl_8h.md#aef4522554340d95f52f21f6896d121c6)#define U0\_TXD\_PIO1\_27 IOCON\_MUX(51, IOCON\_TYPE\_D, 2) /\* PIO1\_27 \*/

[ 324](lpc11u6x-pinctrl_8h.md#a629bba740c1f829a7401dbe6972b155e)#define R\_20\_PIO1\_27 IOCON\_MUX(51, IOCON\_TYPE\_D, 3) /\* PIO1\_27 \*/

[ 325](lpc11u6x-pinctrl_8h.md#adc98f945f54727aa26fb4bb5acccb1b2)#define SSP1\_SCK\_PIO1\_27 IOCON\_MUX(51, IOCON\_TYPE\_D, 4) /\* PIO1\_27 \*/

[ 326](lpc11u6x-pinctrl_8h.md#ae45e38efb89456519fd29191d1bfd41e)#define PIO1\_28\_PIO1\_28 IOCON\_MUX(52, IOCON\_TYPE\_D, 0) /\* PIO1\_28 \*/

[ 327](lpc11u6x-pinctrl_8h.md#acbc5db1dfeb27c0e9e9c37760876aa7f)#define CT32B0\_CAP0\_PIO1\_28 IOCON\_MUX(52, IOCON\_TYPE\_D, 1) /\* PIO1\_28 \*/

[ 328](lpc11u6x-pinctrl_8h.md#a2eb7dfc050a7afad6630db88a430ffa4)#define U0\_SCLK\_PIO1\_28 IOCON\_MUX(52, IOCON\_TYPE\_D, 2) /\* PIO1\_28 \*/

[ 329](lpc11u6x-pinctrl_8h.md#a030246ec2f49c51f0ea088ed565d0f6d)#define U0\_RTS\_PIO1\_28 IOCON\_MUX(52, IOCON\_TYPE\_D, 3) /\* PIO1\_28 \*/

[ 330](lpc11u6x-pinctrl_8h.md#a07775fe074a265e8594cc0f1bc3c4553)#define PIO1\_29\_PIO1\_29 IOCON\_MUX(53, IOCON\_TYPE\_A, 0) /\* PIO1\_29 \*/

[ 331](lpc11u6x-pinctrl_8h.md#afa406dcc3b4ce8853b38782aaee8b34c)#define SSP0\_SCK\_PIO1\_29 IOCON\_MUX(53, IOCON\_TYPE\_A, 1) /\* PIO1\_29 \*/

[ 332](lpc11u6x-pinctrl_8h.md#a8c9a3e151294c9fab0c8ef47d0f0e4fe)#define CT32B0\_CAP1\_PIO1\_29 IOCON\_MUX(53, IOCON\_TYPE\_A, 2) /\* PIO1\_29 \*/

[ 333](lpc11u6x-pinctrl_8h.md#affc255b3a5b093927b05ec78056090fa)#define U0\_DTRn\_PIO1\_29 IOCON\_MUX(53, IOCON\_TYPE\_A, 3) /\* PIO1\_29 \*/

[ 334](lpc11u6x-pinctrl_8h.md#a15dfb4021a3db0723c8918d89840f569)#define ADC\_10\_PIO1\_29 IOCON\_MUX(53, IOCON\_TYPE\_A, 4) /\* PIO1\_29 \*/

[ 335](lpc11u6x-pinctrl_8h.md#a0452698f8cda9677cc606f6e8386f0c5)#define PIO1\_30\_PIO1\_30 IOCON\_MUX(54, IOCON\_TYPE\_D, 0) /\* PIO1\_30 \*/

[ 336](lpc11u6x-pinctrl_8h.md#a8edcf1fdf2dd40db40fc0e3bb226c868)#define I2C1\_SCL\_PIO1\_30 IOCON\_MUX(54, IOCON\_TYPE\_D, 1) /\* PIO1\_30 \*/

[ 337](lpc11u6x-pinctrl_8h.md#a92bceca4249eed78de2037929325bc58)#define SCT0\_IN3\_PIO1\_30 IOCON\_MUX(54, IOCON\_TYPE\_D, 2) /\* PIO1\_30 \*/

[ 338](lpc11u6x-pinctrl_8h.md#a85192c0b77e70e515a9165852d221208)#define R\_31\_PIO1\_30 IOCON\_MUX(54, IOCON\_TYPE\_D, 3) /\* PIO1\_30 \*/

[ 339](lpc11u6x-pinctrl_8h.md#ae459ff2b755df0e5a22378e59fb1ccbc)#define PIO1\_31\_PIO1\_31 IOCON\_MUX(55, IOCON\_TYPE\_D, 0) /\* PIO1\_31 \*/

[ 340](lpc11u6x-pinctrl_8h.md#a5fafd0c519a03d1f678c7f1c6c3b34ed)#define PIO2\_0\_PIO2\_0 IOCON\_MUX(60, IOCON\_TYPE\_A, 0) /\* PIO2\_0 \*/

[ 341](lpc11u6x-pinctrl_8h.md#a5f3bfb1721c59d5800bcdf187dbddeb1)#define XTALIN\_PIO2\_0 IOCON\_MUX(60, IOCON\_TYPE\_A, 1) /\* PIO2\_0 \*/

[ 342](lpc11u6x-pinctrl_8h.md#ab18db336e17b21d3e1864f47fbfe211b)#define PIO2\_1\_PIO2\_1 IOCON\_MUX(61, IOCON\_TYPE\_A, 0) /\* PIO2\_1 \*/

[ 343](lpc11u6x-pinctrl_8h.md#a8c1b112e94052158ccefdda7c023d9e0)#define XTALOUT\_PIO2\_1 IOCON\_MUX(61, IOCON\_TYPE\_A, 1) /\* PIO2\_1 \*/

[ 344](lpc11u6x-pinctrl_8h.md#a5ee88fb076ffc8f05c54ffa403976fa4)#define PIO2\_2\_PIO2\_2 IOCON\_MUX(63, IOCON\_TYPE\_D, 0) /\* PIO2\_2 \*/

[ 345](lpc11u6x-pinctrl_8h.md#aa079f73f9150780aabd8e2cc2325c465)#define U3\_RTS\_PIO2\_2 IOCON\_MUX(63, IOCON\_TYPE\_D, 1) /\* PIO2\_2 \*/

[ 346](lpc11u6x-pinctrl_8h.md#ab257d298276dc7d42c7c4ccfbde4b2fe)#define U3\_SCLK\_PIO2\_2 IOCON\_MUX(63, IOCON\_TYPE\_D, 2) /\* PIO2\_2 \*/

[ 347](lpc11u6x-pinctrl_8h.md#adf678074b20d6e433bd2d9e9fb13681e)#define SCT0\_OUT1\_PIO2\_2 IOCON\_MUX(63, IOCON\_TYPE\_D, 3) /\* PIO2\_2 \*/

[ 348](lpc11u6x-pinctrl_8h.md#ab76b9f2a58719e0cbd557e5b3019861d)#define PIO2\_3\_PIO2\_3 IOCON\_MUX(64, IOCON\_TYPE\_D, 0) /\* PIO2\_3 \*/

[ 349](lpc11u6x-pinctrl_8h.md#a330a0f6bb26f2a8d1881433d42251d88)#define U3\_RXD\_PIO2\_3 IOCON\_MUX(64, IOCON\_TYPE\_D, 1) /\* PIO2\_3 \*/

[ 350](lpc11u6x-pinctrl_8h.md#a54da6ec8f7f08351101969ebdbc6d7f9)#define CT32B0\_MAT1\_PIO2\_3 IOCON\_MUX(64, IOCON\_TYPE\_D, 2) /\* PIO2\_3 \*/

[ 351](lpc11u6x-pinctrl_8h.md#aec83c87cf4c5c7a6cd72370978c5f3ab)#define PIO2\_4\_PIO2\_4 IOCON\_MUX(65, IOCON\_TYPE\_D, 0) /\* PIO2\_4 \*/

[ 352](lpc11u6x-pinctrl_8h.md#a69efa41cce2c5e868b790df9bb2f2fe5)#define U3\_TXD\_PIO2\_4 IOCON\_MUX(65, IOCON\_TYPE\_D, 1) /\* PIO2\_4 \*/

[ 353](lpc11u6x-pinctrl_8h.md#a42c6c88c505fdd8101ff9abaa61c7896)#define CT32B0\_MAT2\_PIO2\_4 IOCON\_MUX(65, IOCON\_TYPE\_D, 2) /\* PIO2\_4 \*/

[ 354](lpc11u6x-pinctrl_8h.md#abd48058e2c15f74525c6354cf245db73)#define PIO2\_5\_PIO2\_5 IOCON\_MUX(66, IOCON\_TYPE\_D, 0) /\* PIO2\_5 \*/

[ 355](lpc11u6x-pinctrl_8h.md#a478a19515c027a5282b061de7a201317)#define U3\_CTS\_PIO2\_5 IOCON\_MUX(66, IOCON\_TYPE\_D, 1) /\* PIO2\_5 \*/

[ 356](lpc11u6x-pinctrl_8h.md#a73d3caf803f8a4df930c63cf4fe3f37c)#define SCT0\_IN1\_PIO2\_5 IOCON\_MUX(66, IOCON\_TYPE\_D, 2) /\* PIO2\_5 \*/

[ 357](lpc11u6x-pinctrl_8h.md#a180b0de4ca0603c2e171c869a52f7580)#define PIO2\_6\_PIO2\_6 IOCON\_MUX(67, IOCON\_TYPE\_D, 0) /\* PIO2\_6 \*/

[ 358](lpc11u6x-pinctrl_8h.md#ab9a1ba400672c6486a0f8647164a1397)#define U1\_RTS\_PIO2\_6 IOCON\_MUX(67, IOCON\_TYPE\_D, 1) /\* PIO2\_6 \*/

[ 359](lpc11u6x-pinctrl_8h.md#a3885a451ceef59f37c8cb470aa3c23d0)#define U1\_SCLK\_PIO2\_6 IOCON\_MUX(67, IOCON\_TYPE\_D, 2) /\* PIO2\_6 \*/

[ 360](lpc11u6x-pinctrl_8h.md#ae14001bfffc9a00d61caf9647a3527f0)#define SCT0\_IN2\_PIO2\_6 IOCON\_MUX(67, IOCON\_TYPE\_D, 3) /\* PIO2\_6 \*/

[ 361](lpc11u6x-pinctrl_8h.md#a7e1cd4171f323202a5b67bb1e9363732)#define PIO2\_7\_PIO2\_7 IOCON\_MUX(68, IOCON\_TYPE\_D, 0) /\* PIO2\_7 \*/

[ 362](lpc11u6x-pinctrl_8h.md#a6f00dd7928fb37ed72b08f0ce57ee03c)#define SSP0\_SCK\_PIO2\_7 IOCON\_MUX(68, IOCON\_TYPE\_D, 1) /\* PIO2\_7 \*/

[ 363](lpc11u6x-pinctrl_8h.md#a41199c507951e02ae2aad6b1b94a2aa5)#define SCT0\_OUT2\_PIO2\_7 IOCON\_MUX(68, IOCON\_TYPE\_D, 2) /\* PIO2\_7 \*/

[ 364](lpc11u6x-pinctrl_8h.md#aa423ccac69367faeaee101c4ca4d411a)#define PIO2\_8\_PIO2\_8 IOCON\_MUX(69, IOCON\_TYPE\_D, 0) /\* PIO2\_8 \*/

[ 365](lpc11u6x-pinctrl_8h.md#af4e4c1f8972faff68d459b159c385dd2)#define SCT1\_IN0\_PIO2\_8 IOCON\_MUX(69, IOCON\_TYPE\_D, 1) /\* PIO2\_8 \*/

[ 366](lpc11u6x-pinctrl_8h.md#aa849da24aea3e3d29c43cc8f7264b434)#define PIO2\_9\_PIO2\_9 IOCON\_MUX(70, IOCON\_TYPE\_D, 0) /\* PIO2\_9 \*/

[ 367](lpc11u6x-pinctrl_8h.md#afd99a1f94ac011c63fbb8a9a9db511da)#define SCT1\_IN1\_PIO2\_9 IOCON\_MUX(70, IOCON\_TYPE\_D, 1) /\* PIO2\_9 \*/

[ 368](lpc11u6x-pinctrl_8h.md#a2471788decdf2d9119ca1245ddc77981)#define PIO2\_10\_PIO2\_10 IOCON\_MUX(71, IOCON\_TYPE\_D, 0) /\* PIO2\_10 \*/

[ 369](lpc11u6x-pinctrl_8h.md#a531b7e88f7193b4ce754081685e6d23f)#define U4\_RTS\_PIO2\_10 IOCON\_MUX(71, IOCON\_TYPE\_D, 1) /\* PIO2\_10 \*/

[ 370](lpc11u6x-pinctrl_8h.md#a34a74c9cc41c9839ee54dccf1aaa9ad7)#define U4\_SCLK\_PIO2\_10 IOCON\_MUX(71, IOCON\_TYPE\_D, 2) /\* PIO2\_10 \*/

[ 371](lpc11u6x-pinctrl_8h.md#a25f558f2d23c6a973da481216a331047)#define PIO2\_11\_PIO2\_11 IOCON\_MUX(72, IOCON\_TYPE\_D, 0) /\* PIO2\_11 \*/

[ 372](lpc11u6x-pinctrl_8h.md#aaabe5ad6b984f52723df7c958e043cd2)#define U4\_RXD\_PIO2\_11 IOCON\_MUX(72, IOCON\_TYPE\_D, 1) /\* PIO2\_11 \*/

[ 373](lpc11u6x-pinctrl_8h.md#a55b8398b79ab94885c5b1a266cc96b67)#define PIO2\_12\_PIO2\_12 IOCON\_MUX(73, IOCON\_TYPE\_D, 0) /\* PIO2\_12 \*/

[ 374](lpc11u6x-pinctrl_8h.md#aa676078e9cc9a7dbb114e9e39bbdee07)#define U4\_TXD\_PIO2\_12 IOCON\_MUX(73, IOCON\_TYPE\_D, 1) /\* PIO2\_12 \*/

[ 375](lpc11u6x-pinctrl_8h.md#aad0ffb60a10d384eec0c88137e9f5049)#define PIO2\_13\_PIO2\_13 IOCON\_MUX(74, IOCON\_TYPE\_D, 0) /\* PIO2\_13 \*/

[ 376](lpc11u6x-pinctrl_8h.md#a2481a40bdab053f1d25e6fd4daeb90cc)#define U4\_CTS\_PIO2\_13 IOCON\_MUX(74, IOCON\_TYPE\_D, 1) /\* PIO2\_13 \*/

[ 377](lpc11u6x-pinctrl_8h.md#a4d600902f1f7cfa6d6d7a15dad9fa47e)#define PIO2\_14\_PIO2\_14 IOCON\_MUX(75, IOCON\_TYPE\_D, 0) /\* PIO2\_14 \*/

[ 378](lpc11u6x-pinctrl_8h.md#a372dcaa75ccd7aea049ae958f41e9332)#define SCT1\_IN2\_PIO2\_14 IOCON\_MUX(75, IOCON\_TYPE\_D, 1) /\* PIO2\_14 \*/

[ 379](lpc11u6x-pinctrl_8h.md#a4247567257584b93a079dde0636a8d82)#define PIO2\_15\_PIO2\_15 IOCON\_MUX(76, IOCON\_TYPE\_D, 0) /\* PIO2\_15 \*/

[ 380](lpc11u6x-pinctrl_8h.md#ad4ea56df396ac4cab517d5bd7b735f5c)#define SCT1\_IN3\_PIO2\_15 IOCON\_MUX(76, IOCON\_TYPE\_D, 1) /\* PIO2\_15 \*/

[ 381](lpc11u6x-pinctrl_8h.md#a68ae2af37b444a788e82cbdd59a9518e)#define PIO2\_16\_PIO2\_16 IOCON\_MUX(77, IOCON\_TYPE\_D, 0) /\* PIO2\_16 \*/

[ 382](lpc11u6x-pinctrl_8h.md#affe7ba3bec6cfd4b2bba3533ea8cbd66)#define SCT1\_OUT0\_PIO2\_16 IOCON\_MUX(77, IOCON\_TYPE\_D, 1) /\* PIO2\_16 \*/

[ 383](lpc11u6x-pinctrl_8h.md#aafd4249d51198bee34d7f03275b70bc6)#define PIO2\_17\_PIO2\_17 IOCON\_MUX(78, IOCON\_TYPE\_D, 0) /\* PIO2\_17 \*/

[ 384](lpc11u6x-pinctrl_8h.md#a2e3304361cf9766f08c764fac50ef9bc)#define SCT1\_OUT1\_PIO2\_17 IOCON\_MUX(78, IOCON\_TYPE\_D, 1) /\* PIO2\_17 \*/

[ 385](lpc11u6x-pinctrl_8h.md#ab01949c5d3a85a0acb2266d7c4e71b8a)#define PIO2\_18\_PIO2\_18 IOCON\_MUX(79, IOCON\_TYPE\_D, 0) /\* PIO2\_18 \*/

[ 386](lpc11u6x-pinctrl_8h.md#af2c8a7e95a4a2f63e1f86ed9aa83a76f)#define SCT1\_OUT2\_PIO2\_18 IOCON\_MUX(79, IOCON\_TYPE\_D, 1) /\* PIO2\_18 \*/

[ 387](lpc11u6x-pinctrl_8h.md#a10046d3d553609d2e46568d31bcbd22b)#define PIO2\_19\_PIO2\_19 IOCON\_MUX(80, IOCON\_TYPE\_D, 0) /\* PIO2\_19 \*/

[ 388](lpc11u6x-pinctrl_8h.md#a89409cbd5a036dd7ff5c5a868eef4521)#define SCT1\_OUT3\_PIO2\_19 IOCON\_MUX(80, IOCON\_TYPE\_D, 1) /\* PIO2\_19 \*/

[ 389](lpc11u6x-pinctrl_8h.md#a379470de275ec9e879c6a7da55dc81e2)#define PIO2\_20\_PIO2\_20 IOCON\_MUX(81, IOCON\_TYPE\_D, 0) /\* PIO2\_20 \*/

[ 390](lpc11u6x-pinctrl_8h.md#a8cc6a3d1353183ec7277fbb88a405961)#define PIO2\_21\_PIO2\_21 IOCON\_MUX(82, IOCON\_TYPE\_D, 0) /\* PIO2\_21 \*/

[ 391](lpc11u6x-pinctrl_8h.md#a12640000bfec871e24fff6deaa5cdd08)#define PIO2\_22\_PIO2\_22 IOCON\_MUX(83, IOCON\_TYPE\_D, 0) /\* PIO2\_22 \*/

[ 392](lpc11u6x-pinctrl_8h.md#ab78b84af5278ada6d4c31bbc85928899)#define PIO2\_23\_PIO2\_23 IOCON\_MUX(84, IOCON\_TYPE\_D, 0) /\* PIO2\_23 \*/

393

394#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_LPC11U6X\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [lpc11u6x-pinctrl.h](lpc11u6x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
