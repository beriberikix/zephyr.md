---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rtc__ds3231_8h_source.html
original_path: doxygen/html/rtc__ds3231_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtc\_ds3231.h

[Go to the documentation of this file.](rtc__ds3231_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright (c) 2024 Gergo Vari <work@gergovari.com>

5 \*/

6

7/\*

8 \* REGISTERS

9 \*/

10

11/\* Time registers \*/

[ 12](rtc__ds3231_8h.md#a187993c430c68d3841b312cddd4fe14c)#define DS3231\_REG\_TIME\_SECONDS 0x00

[ 13](rtc__ds3231_8h.md#ac66924e0c5c3dc095c8cf6c9666571fd)#define DS3231\_REG\_TIME\_MINUTES 0x01

[ 14](rtc__ds3231_8h.md#ae5e85807525a616b6b49979c7615ae4a)#define DS3231\_REG\_TIME\_HOURS 0x02

[ 15](rtc__ds3231_8h.md#abe540c9bcdc7bd43898220dd836c074c)#define DS3231\_REG\_TIME\_DAY\_OF\_WEEK 0x03

[ 16](rtc__ds3231_8h.md#aac944d073c221f89d3fc00fdccc2dec7)#define DS3231\_REG\_TIME\_DATE 0x04

[ 17](rtc__ds3231_8h.md#a141283f5923a36019c2064fb60f56326)#define DS3231\_REG\_TIME\_MONTH 0x05

[ 18](rtc__ds3231_8h.md#af1e20c0549eaf16de73814c9bb93135d)#define DS3231\_REG\_TIME\_YEAR 0x06

19

20/\* Alarm 1 registers \*/

[ 21](rtc__ds3231_8h.md#a337349639f9eeac901ecd5c9fbcb8998)#define DS3231\_REG\_ALARM\_1\_SECONDS 0x07

[ 22](rtc__ds3231_8h.md#a8e7495a5790b651ec35dc5f8d6a46e95)#define DS3231\_REG\_ALARM\_1\_MINUTES 0x08

[ 23](rtc__ds3231_8h.md#aab48f5a7f301d470047f4410f406224c)#define DS3231\_REG\_ALARM\_1\_HOURS 0x09

[ 24](rtc__ds3231_8h.md#a89d12b2aa1a5412ed394080531c04c8c)#define DS3231\_REG\_ALARM\_1\_DATE 0x0A

25

26/\* Alarm 2 registers \*/

27/\* Alarm 2 has no seconds to set, it only has minute accuracy. \*/

[ 28](rtc__ds3231_8h.md#aa03fe6e862f1e5094f05e06ae4bbf108)#define DS3231\_REG\_ALARM\_2\_MINUTES 0x0B

[ 29](rtc__ds3231_8h.md#a0f374dcba3ebc59daf345f6ecaa59f16)#define DS3231\_REG\_ALARM\_2\_HOURS 0x0C

[ 30](rtc__ds3231_8h.md#a6fc6b9519ca96bed9d62a253199af1f0)#define DS3231\_REG\_ALARM\_2\_DATE 0x0D

31

32/\* Control registers \*/

[ 33](rtc__ds3231_8h.md#aea14f214d3c7c4feaa29c2632fd92371)#define DS3231\_REG\_CTRL 0x0E

[ 34](rtc__ds3231_8h.md#a6d2cfdba50a2f834cd5f2e372c46a0a2)#define DS3231\_REG\_CTRL\_STS 0x0F

35

36/\* Aging offset register \*/

[ 37](rtc__ds3231_8h.md#a2c630e7f3a057480946da744449d2eb3)#define DS3231\_REG\_AGING\_OFFSET 0x10

38

39/\*

40 \* BITMASKS

41 \*/

42

43/\* Time bitmasks \*/

[ 44](rtc__ds3231_8h.md#af1a6735d3f31fdd3ac2892437e7322df)#define DS3231\_BITS\_TIME\_SECONDS GENMASK(6, 0)

[ 45](rtc__ds3231_8h.md#a3d4c98bdf335837ce0780176b8e08119)#define DS3231\_BITS\_TIME\_MINUTES GENMASK(6, 0)

[ 46](rtc__ds3231_8h.md#aee073fea577330d4ecbd37f1da498dd3)#define DS3231\_BITS\_TIME\_HOURS GENMASK(5, 0)

[ 47](rtc__ds3231_8h.md#a1050727c51f29cf040196d76c171a30b)#define DS3231\_BITS\_TIME\_PM BIT(5)

[ 48](rtc__ds3231_8h.md#a52613d566dcd8497b39ad4c154d95b28)#define DS3231\_BITS\_TIME\_12HR BIT(6)

[ 49](rtc__ds3231_8h.md#a7d917b52957e4b61ef0c933ce9fd73c7)#define DS3231\_BITS\_TIME\_DAY\_OF\_WEEK GENMASK(2, 0)

[ 50](rtc__ds3231_8h.md#abeab153561c71060cdd8ab82b20207f7)#define DS3231\_BITS\_TIME\_DATE GENMASK(5, 0)

[ 51](rtc__ds3231_8h.md#a65dea42153d17bd5163b2c35296e54fb)#define DS3231\_BITS\_TIME\_MONTH GENMASK(4, 0)

[ 52](rtc__ds3231_8h.md#a65fd40e64760a2178c4fc82bf2d8a060)#define DS3231\_BITS\_TIME\_CENTURY BIT(7)

[ 53](rtc__ds3231_8h.md#a95db7b4dc81d7951205d78fcfc041fa5)#define DS3231\_BITS\_TIME\_YEAR GENMASK(7, 0)

54

55/\* Alarm bitmasks \*/

56/\* All alarm bitmasks match with time other than date and the alarm rate bit. \*/

[ 57](rtc__ds3231_8h.md#ad1fdc4e68cdaa52333c3e62b63f0ab83)#define DS3231\_BITS\_ALARM\_RATE BIT(7)

[ 58](rtc__ds3231_8h.md#a793f06ed1fa6530cb5f670d047b6f11b)#define DS3231\_BITS\_ALARM\_DATE\_W\_OR\_M BIT(6)

59

[ 60](rtc__ds3231_8h.md#a6c3c187e805d1690fc95b8cf28464dfe)#define DS3231\_BITS\_SIGN BIT(7)

61/\* Control bitmasks \*/

[ 62](rtc__ds3231_8h.md#a8af0c897cfc7b5e14b0e41b79f19cd4d)#define DS3231\_BITS\_CTRL\_EOSC BIT(7) /\* enable oscillator, active low \*/

[ 63](rtc__ds3231_8h.md#a700ff940db5f1cb1deda9807c6ea789a)#define DS3231\_BITS\_CTRL\_BBSQW BIT(6) /\* enable battery-backed square-wave \*/

64

65/\* Setting the CONV bit to 1 forces the temperature sensor to

66 \* convert the temperature into digital code and

67 \* execute the TCXO algorithm to update

68 \* the capacitance array to the oscillator. This can only

69 \* happen when a conversion is not already in progress.

70 \* The user should check the status bit BSY before

71 \* forcing the controller to start a new TCXO execution.

72 \* A user-initiated temperature conversion

73 \* does not affect the internal 64-second update cycle.

74 \*/

[ 75](rtc__ds3231_8h.md#a67e01c51fc4d1f0615d00f276eede03a)#define DS3231\_BITS\_CTRL\_CONV BIT(6)

76

77/\* Rate selectors \*/

78/\* RS2 | RS1 | SQW FREQ

79 \* 0 | 0 | 1Hz

80 \* 0 | 1 | 1.024kHz

81 \* 1 | 0 | 4.096kHz

82 \* 1 | 1 | 8.192kHz

83 \*/

[ 84](rtc__ds3231_8h.md#ae1601b168cd49a5dc4fe49fe0c46817d)#define DS3231\_BITS\_CTRL\_RS2 BIT(4)

[ 85](rtc__ds3231_8h.md#ac0a14b3ee52a170089213d13fa661698)#define DS3231\_BITS\_CTRL\_RS1 BIT(3)

86

[ 87](rtc__ds3231_8h.md#a725674abd8a3b0df46057d92a90d4e9c)#define DS3231\_BITS\_CTRL\_INTCTRL BIT(2)

[ 88](rtc__ds3231_8h.md#a98081c1e726f3d61c9fa4cc96f2e5896)#define DS3231\_BITS\_CTRL\_ALARM\_2\_EN BIT(1)

[ 89](rtc__ds3231_8h.md#a6b4e6afb16cf51e06891c3b9f8e4471e)#define DS3231\_BITS\_CTRL\_ALARM\_1\_EN BIT(0)

90

91/\* Control status bitmasks \*/

92/\* For some reason you can access OSF in both control and control status registers. \*/

[ 93](rtc__ds3231_8h.md#aac6acc5700a872e9819642a404f01c1b)#define DS3231\_BITS\_CTRL\_STS\_OSF BIT(7) /\* oscillator stop flag \*/ /\* read only \*/

[ 94](rtc__ds3231_8h.md#a30d036ea3357246e979870687436fb63)#define DS3231\_BITS\_CTRL\_STS\_32\_EN BIT(3) /\* 32kHz square-wave \*/

95/\* set when TXCO is busy, see CONV flag: read only \*/

[ 96](rtc__ds3231_8h.md#a175dc0d5e5780fa9c3ab27f461c0088f)#define DS3231\_BITS\_CTRL\_STS\_BSY BIT(2)

[ 97](rtc__ds3231_8h.md#a112b3f339727a4239707564438e90566)#define DS3231\_BITS\_CTRL\_STS\_ALARM\_2\_FLAG BIT(1) /\* can only be set to 0 \*/

[ 98](rtc__ds3231_8h.md#a56b77005b72874a2dffc3ff9d7691254)#define DS3231\_BITS\_CTRL\_STS\_ALARM\_1\_FLAG BIT(0) /\* can only be set to 0 \*/

99

100/\* Aging offset bitmask \*/

[ 101](rtc__ds3231_8h.md#a07b1af46954b37add67cb3fdf975af5a)#define DS3231\_BITS\_DATA BIT(6, 0)

102

103/\* Settings bitmasks \*/

[ 104](rtc__ds3231_8h.md#a701b74da1c41863195f36d0779c543c9)#define DS3231\_BITS\_STS\_OSC BIT(0)

[ 105](rtc__ds3231_8h.md#afa345544f3a610bcce7a0fdd68a3d553)#define DS3231\_BITS\_STS\_INTCTRL BIT(1)

[ 106](rtc__ds3231_8h.md#a18c98b9dcd706f8f2bb25d38e8d1d9f8)#define DS3231\_BITS\_STS\_SQW BIT(2)

[ 107](rtc__ds3231_8h.md#ad1b79e60328b65a381873c42ca5247dd)#define DS3231\_BITS\_STS\_32KHZ BIT(3)

[ 108](rtc__ds3231_8h.md#a3cd872a940476ef5918324f23680e4d5)#define DS3231\_BITS\_STS\_ALARM\_1 BIT(4)

[ 109](rtc__ds3231_8h.md#a6e4f4fbd24d13165fa24b41bbfc410fe)#define DS3231\_BITS\_STS\_ALARM\_2 BIT(5)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc](dir_fe6de79d2b035e3fa4834af86b312149.md)
- [rtc\_ds3231.h](rtc__ds3231_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
