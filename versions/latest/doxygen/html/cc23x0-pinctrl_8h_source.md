---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cc23x0-pinctrl_8h_source.html
original_path: doxygen/html/cc23x0-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cc23x0-pinctrl.h

[Go to the documentation of this file.](cc23x0-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2024 Texas Instruments Incorporated

3 \* Copyright (c) 2024 BayLibre, SAS

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef CC23X0\_PINCTRL\_COMMON\_H\_

9#define CC23X0\_PINCTRL\_COMMON\_H\_

10

11/\*

12 \* The whole TI CC23X0 pin configuration information is encoded in a 32-bit

13 \* bitfield organized as follow:

14 \*

15 \* - 31: Reserved

16 \* - 30: Input hysteresis

17 \* - 29: Input capability of IO

18 \* - 28..27: Reserved

19 \* - 26..24: IO mode

20 \* - 23..22: Reserved

21 \* - 21..20: Wakeup configuration from shutdown

22 \* - 19: Reserved

23 \* - 18: Wakeup capability from standby

24 \* - 17..16: Edge detection configuration

25 \* - 15: Reserved

26 \* - 14..13: Pull control

27 \* - 12..3: Reserved

28 \* - 2..0: Function configuration

29 \*/

30

31/\* TI CC23X0 function configuration \*/

32

[ 33](cc23x0-pinctrl_8h.md#aa502a06b1e9f31be173481ff4626bb70)#define IOC\_PORTCFG\_BASE 0U

[ 34](cc23x0-pinctrl_8h.md#a4ac7f9fbb7a989da2815fa48a2c63bd9)#define IOC\_PORTCFG\_PFUNC1 1U

[ 35](cc23x0-pinctrl_8h.md#a469848941ebbce5b2fc1b54d57f7d965)#define IOC\_PORTCFG\_PFUNC2 2U

[ 36](cc23x0-pinctrl_8h.md#a420b3a48d4a6010feb9866b97a7492dd)#define IOC\_PORTCFG\_PFUNC3 3U

[ 37](cc23x0-pinctrl_8h.md#a3f27b6bb5191b2c2def7b74afa0c0019)#define IOC\_PORTCFG\_PFUNC4 4U

[ 38](cc23x0-pinctrl_8h.md#af33d2e20e5de9cc53b70a3e826624837)#define IOC\_PORTCFG\_PFUNC5 5U

[ 39](cc23x0-pinctrl_8h.md#a375a32390601a0a7e8daf034bf696482)#define IOC\_PORTCFG\_ANA 6U

[ 40](cc23x0-pinctrl_8h.md#a6c1e87a84343d63b8ab60e53b14944d3)#define IOC\_PORTCFG\_DTB 7U

41

42/\* TI CC23X0 peripheral pin mapping \*/

43

[ 44](cc23x0-pinctrl_8h.md#ade776b707cd244b692be71202a7e08cb)#define DIO0\_GPIO0 IOC\_PORTCFG\_BASE

[ 45](cc23x0-pinctrl_8h.md#a92c899e5d01e371e4abee45e3f31c5f4)#define DIO0\_SPI0\_CSN IOC\_PORTCFG\_PFUNC1

[ 46](cc23x0-pinctrl_8h.md#a1da175a81e69788efebd00db91beba6e)#define DIO0\_I2C0\_SDA IOC\_PORTCFG\_PFUNC2

[ 47](cc23x0-pinctrl_8h.md#ae6321d9d1d78a0ee5c58b5f94577f501)#define DIO0\_T3\_C2 IOC\_PORTCFG\_PFUNC3

[ 48](cc23x0-pinctrl_8h.md#ab256a8550b3c03978e5c6b707ba6d1ce)#define DIO0\_ADC5 IOC\_PORTCFG\_ANA

49

[ 50](cc23x0-pinctrl_8h.md#ac38ece6a277c436f774ab4b0392ea635)#define DIO1\_GPIO1 IOC\_PORTCFG\_BASE

[ 51](cc23x0-pinctrl_8h.md#a2b5d4a0a786d41a76b959a976c3435a4)#define DIO1\_T3\_C1 IOC\_PORTCFG\_PFUNC1

[ 52](cc23x0-pinctrl_8h.md#acb8c92941a28948edf78ea8ba7bf1a3f)#define DIO1\_LRFD7 IOC\_PORTCFG\_PFUNC2

[ 53](cc23x0-pinctrl_8h.md#a522504deec63fc7e124ee2628e21158c)#define DIO1\_T1\_F IOC\_PORTCFG\_PFUNC3

[ 54](cc23x0-pinctrl_8h.md#a6f9ff300c12b1d0f6291da925d53d049)#define DIO1\_UART0\_RTS IOC\_PORTCFG\_PFUNC4

[ 55](cc23x0-pinctrl_8h.md#ac1db8b2eec7a587f2777ec42bc741332)#define DIO1\_ADC4 IOC\_PORTCFG\_ANA

[ 56](cc23x0-pinctrl_8h.md#a22d9f90c38345c7487044591caaa5a60)#define DIO1\_DTB2 IOC\_PORTCFG\_DTB

57

[ 58](cc23x0-pinctrl_8h.md#acce8374fb4d805494ebaf78834d431d6)#define DIO2\_GPIO2 IOC\_PORTCFG\_BASE

[ 59](cc23x0-pinctrl_8h.md#ae1e1837425d79845e84a9551c6ce90d3)#define DIO2\_T0\_PE IOC\_PORTCFG\_PFUNC1

[ 60](cc23x0-pinctrl_8h.md#a943d0d0497b8d939b4bdf6eb1ed7af03)#define DIO2\_T2\_C1N IOC\_PORTCFG\_PFUNC2

[ 61](cc23x0-pinctrl_8h.md#aebfe126f475d93068b93eb195049f586)#define DIO2\_UART0\_CTS IOC\_PORTCFG\_PFUNC3

[ 62](cc23x0-pinctrl_8h.md#a592b7a2687e97ac64b684681a43dbc0b)#define DIO2\_ADC3 IOC\_PORTCFG\_ANA

63

[ 64](cc23x0-pinctrl_8h.md#a02eb22dc2b9867c418e972a64c4e549c)#define DIO3\_GPIO3 IOC\_PORTCFG\_BASE

[ 65](cc23x0-pinctrl_8h.md#a9babb38598d110fa6972313e4a5f90ac)#define DIO3\_LFCI IOC\_PORTCFG\_PFUNC1

[ 66](cc23x0-pinctrl_8h.md#ad5f0fade34b37ed25a23b27a101f9796)#define DIO3\_T0\_C1N IOC\_PORTCFG\_PFUNC2

[ 67](cc23x0-pinctrl_8h.md#a2680e26e7c1dd92e43413727f9f4c415)#define DIO3\_LRFD0 IOC\_PORTCFG\_PFUNC3

[ 68](cc23x0-pinctrl_8h.md#a3856eb90a0dec21a3055041edf7c975a)#define DIO3\_T3\_C1 IOC\_PORTCFG\_PFUNC4

[ 69](cc23x0-pinctrl_8h.md#a31ecae7e3f360d17dee9b78b2a8f18b1)#define DIO3\_T1\_C2 IOC\_PORTCFG\_PFUNC5

[ 70](cc23x0-pinctrl_8h.md#a6d5fd06f8df458a27ee0cb75746203df)#define DIO3\_LFXT\_P IOC\_PORTCFG\_ANA

[ 71](cc23x0-pinctrl_8h.md#a95e01bbcdcd732983e0bca7cf02fcf33)#define DIO3\_DTB7 IOC\_PORTCFG\_DTB

72

[ 73](cc23x0-pinctrl_8h.md#ae3239b06b452ff8757f9990f5f091a61)#define DIO4\_GPIO4 IOC\_PORTCFG\_BASE

[ 74](cc23x0-pinctrl_8h.md#a040b8faba6859f0decc43d318cee6ed1)#define DIO4\_T0\_C2N IOC\_PORTCFG\_PFUNC1

[ 75](cc23x0-pinctrl_8h.md#a4ee4d6b4e97e0053b9dfdadd47ffd55e)#define DIO4\_UART0\_TXD IOC\_PORTCFG\_PFUNC2

[ 76](cc23x0-pinctrl_8h.md#a5f4c955ea6d875eb53f8575a59b8fc1a)#define DIO4\_LRFD1 IOC\_PORTCFG\_PFUNC3

[ 77](cc23x0-pinctrl_8h.md#a17ea74b30c1aed816d675fcc2ff076fc)#define DIO4\_SPI0\_MOSI IOC\_PORTCFG\_PFUNC4

[ 78](cc23x0-pinctrl_8h.md#ab42c816bea20237638d790ffcee2b2cf)#define DIO4\_T0\_C2 IOC\_PORTCFG\_PFUNC5

[ 79](cc23x0-pinctrl_8h.md#ae5bbef3a760612759307039d94ae8d4c)#define DIO4\_LFXT\_N IOC\_PORTCFG\_ANA

[ 80](cc23x0-pinctrl_8h.md#abebb35dde4a811b0237b9fb24517b41f)#define DIO4\_DTB8 IOC\_PORTCFG\_DTB

81

[ 82](cc23x0-pinctrl_8h.md#ae860734b858834f5024b4f35377c56cb)#define DIO5\_GPIO5 IOC\_PORTCFG\_BASE

[ 83](cc23x0-pinctrl_8h.md#abbada75153e0f5b9c352a2cfd6669037)#define DIO5\_T2\_C2 IOC\_PORTCFG\_PFUNC1

[ 84](cc23x0-pinctrl_8h.md#aff51e9eb6eb949038b5cccb4fa074212)#define DIO5\_LRFD6 IOC\_PORTCFG\_PFUNC3

[ 85](cc23x0-pinctrl_8h.md#a09619eb634cab8068134cb40a152f17b)#define DIO5\_ADC2 IOC\_PORTCFG\_ANA

86

[ 87](cc23x0-pinctrl_8h.md#a56f5afccece122855f957668e81d1bcd)#define DIO6\_GPIO6 IOC\_PORTCFG\_BASE

[ 88](cc23x0-pinctrl_8h.md#a38d80b5fc0894b55beba01019350edca)#define DIO6\_SPI0\_CSN IOC\_PORTCFG\_PFUNC1

[ 89](cc23x0-pinctrl_8h.md#a914b6a41adb66c2f65413c46ff620c5c)#define DIO6\_I2C0\_SCL IOC\_PORTCFG\_PFUNC2

[ 90](cc23x0-pinctrl_8h.md#ad17cc424f3421617c753d1387da6c6bf)#define DIO6\_T1\_C2 IOC\_PORTCFG\_PFUNC3

[ 91](cc23x0-pinctrl_8h.md#a834af6e67831d342dbef9084a4bc422e)#define DIO6\_LRFD2 IOC\_PORTCFG\_PFUNC4

[ 92](cc23x0-pinctrl_8h.md#ac55e5ce877a5e57cf565830193c076e6)#define DIO6\_UART0\_TXD IOC\_PORTCFG\_PFUNC5

[ 93](cc23x0-pinctrl_8h.md#a39e4a39c6d312c974b37acac1b1054da)#define DIO6\_ADC1\_AREFP IOC\_PORTCFG\_ANA

[ 94](cc23x0-pinctrl_8h.md#aac1e3c63427f92bd1d73d472ca215eb1)#define DIO6\_DTB6 IOC\_PORTCFG\_DTB

95

[ 96](cc23x0-pinctrl_8h.md#ae0e5f07c43371d3602b4353f6178a214)#define DIO7\_GPIO7 IOC\_PORTCFG\_BASE

[ 97](cc23x0-pinctrl_8h.md#ae60dd20c9960b001a992d37fbfa05956)#define DIO7\_T3\_C1 IOC\_PORTCFG\_PFUNC1

[ 98](cc23x0-pinctrl_8h.md#a8a354e58d7f6425c9cb91137dc4aa766)#define DIO7\_LRFD4 IOC\_PORTCFG\_PFUNC3

[ 99](cc23x0-pinctrl_8h.md#a3c92801ae0b96fae2be1a9b018022aea)#define DIO7\_ADC0\_AREFM IOC\_PORTCFG\_ANA

100

[ 101](cc23x0-pinctrl_8h.md#afe29503f0e97bf76bea3ed2ec3fe4b64)#define DIO8\_GPIO8 IOC\_PORTCFG\_BASE

[ 102](cc23x0-pinctrl_8h.md#a3d22644d12be2b507ed4a4a05097b29f)#define DIO8\_SPI0\_SCLK IOC\_PORTCFG\_PFUNC1

[ 103](cc23x0-pinctrl_8h.md#a82f64fe945445f96be0db2aa2d021e6b)#define DIO8\_UART0\_RTS IOC\_PORTCFG\_PFUNC2

[ 104](cc23x0-pinctrl_8h.md#ab32d21fdbcde3256731b561d9f5f2ad1)#define DIO8\_T1\_C0N IOC\_PORTCFG\_PFUNC3

[ 105](cc23x0-pinctrl_8h.md#a2b845037d4c448c3847ba408ba98720d)#define DIO8\_I2C0\_SDA IOC\_PORTCFG\_PFUNC4

[ 106](cc23x0-pinctrl_8h.md#aff36d54d77c72974b870285fb6d8b801)#define DIO8\_T0\_C0N IOC\_PORTCFG\_PFUNC5

[ 107](cc23x0-pinctrl_8h.md#a82913b1243033ac74f06eeaf4aff7df4)#define DIO8\_DTB3 IOC\_PORTCFG\_DTB

108

[ 109](cc23x0-pinctrl_8h.md#a74d0f7de1cb705b147947312f67e273a)#define DIO9\_GPIO9 IOC\_PORTCFG\_BASE

[ 110](cc23x0-pinctrl_8h.md#a87eac578bb6d3ba94be53508d81ddae8)#define DIO9\_T3\_C0 IOC\_PORTCFG\_PFUNC1

[ 111](cc23x0-pinctrl_8h.md#a069db119313663a8bd1052992e12e85a)#define DIO9\_LRFD3 IOC\_PORTCFG\_PFUNC3

112

[ 113](cc23x0-pinctrl_8h.md#a4d4ecf52202b89bd18fd07df9f8cf23c)#define DIO10\_GPIO10 IOC\_PORTCFG\_BASE

[ 114](cc23x0-pinctrl_8h.md#a7c38cc0d168019884b5d0e022be58047)#define DIO10\_LPC0 IOC\_PORTCFG\_PFUNC1

[ 115](cc23x0-pinctrl_8h.md#a401c41789d4f0730631c8d95c95356f1)#define DIO10\_T2\_PE IOC\_PORTCFG\_PFUNC2

[ 116](cc23x0-pinctrl_8h.md#a132cf71891f6ac14dd1f3cdae463b369)#define DIO10\_T3\_C0N IOC\_PORTCFG\_PFUNC3

117

[ 118](cc23x0-pinctrl_8h.md#a406be9c9748d230aaa5f6a0936a59fa1)#define DIO11\_GPIO11 IOC\_PORTCFG\_BASE

[ 119](cc23x0-pinctrl_8h.md#ac4ad3c53ba96f31cc859d3126c477049)#define DIO11\_SPI0\_CSN IOC\_PORTCFG\_PFUNC1

[ 120](cc23x0-pinctrl_8h.md#ac72ec42df93ef20cc55b1d33bea8a3b7)#define DIO11\_T1\_C2N IOC\_PORTCFG\_PFUNC2

[ 121](cc23x0-pinctrl_8h.md#af351c707516ced033891623bdacf3b4f)#define DIO11\_T0\_C0 IOC\_PORTCFG\_PFUNC3

[ 122](cc23x0-pinctrl_8h.md#a8e5989e85216c9b9fa9e7e66d9339371)#define DIO11\_LRFD0 IOC\_PORTCFG\_PFUNC4

[ 123](cc23x0-pinctrl_8h.md#ac8e3ba0e0fbcaaeeb910680f1ebed192)#define DIO11\_SPI0\_MISO IOC\_PORTCFG\_PFUNC5

[ 124](cc23x0-pinctrl_8h.md#a14a9531e81aa7d43ab54d458ab6ea221)#define DIO11\_DTB9 IOC\_PORTCFG\_DTB

125

[ 126](cc23x0-pinctrl_8h.md#a2ad2d410f5ff120cb65fd6b899ddc165)#define DIO12\_GPIO12 IOC\_PORTCFG\_BASE

[ 127](cc23x0-pinctrl_8h.md#a7e1b7a3e5d11986b97f56d85a3ff5c76)#define DIO12\_SPI0\_MISO IOC\_PORTCFG\_PFUNC1

[ 128](cc23x0-pinctrl_8h.md#a37571bec3db0e47d21abbe176d87d96c)#define DIO12\_SPI0\_MOSI IOC\_PORTCFG\_PFUNC2

[ 129](cc23x0-pinctrl_8h.md#a1dda1b7dd1213db83dac067a3995419e)#define DIO12\_UART0\_RXD IOC\_PORTCFG\_PFUNC3

[ 130](cc23x0-pinctrl_8h.md#adc65e540bd2e34316f283cedc4cccfea)#define DIO12\_T1\_C1 IOC\_PORTCFG\_PFUNC4

[ 131](cc23x0-pinctrl_8h.md#a6b0c99c8c413097f40eac6523b9d5924)#define DIO12\_I2C0\_SDA IOC\_PORTCFG\_PFUNC5

[ 132](cc23x0-pinctrl_8h.md#a693aebfd8e479fe790e147df42ffa526)#define DIO12\_DTB13 IOC\_PORTCFG\_DTB

133

[ 134](cc23x0-pinctrl_8h.md#a13e07e2b2ebb2fbd832e032046b18ad4)#define DIO13\_GPIO13 IOC\_PORTCFG\_BASE

[ 135](cc23x0-pinctrl_8h.md#a0c3a3c06beb7126113bf9e0bb5599d51)#define DIO13\_SPI0\_MISO IOC\_PORTCFG\_PFUNC1

[ 136](cc23x0-pinctrl_8h.md#a1a10e7a429f2a8d0885999e57780387e)#define DIO13\_SPI0\_MOSI IOC\_PORTCFG\_PFUNC2

[ 137](cc23x0-pinctrl_8h.md#abb44537be4746bbcf1d3e0d32bfa3cba)#define DIO13\_UART0\_TXD IOC\_PORTCFG\_PFUNC3

[ 138](cc23x0-pinctrl_8h.md#a856cc517f1a799d293114daaa33aeb38)#define DIO13\_T0\_C0N IOC\_PORTCFG\_PFUNC4

[ 139](cc23x0-pinctrl_8h.md#acec3eda273c31b29324b3bfe2afdc070)#define DIO13\_T1\_F IOC\_PORTCFG\_PFUNC5

[ 140](cc23x0-pinctrl_8h.md#a9400a3fa8fc3e8d07191a9c72d551fb5)#define DIO13\_DTB4 IOC\_PORTCFG\_DTB

141

[ 142](cc23x0-pinctrl_8h.md#ae30591306137378af20de546bfbc402e)#define DIO14\_GPIO14 IOC\_PORTCFG\_BASE

[ 143](cc23x0-pinctrl_8h.md#a0c7457a723d316668a3aabd0404a0a65)#define DIO14\_T3\_C2 IOC\_PORTCFG\_PFUNC1

[ 144](cc23x0-pinctrl_8h.md#abc3f5cb7c0f595fc80d3285d902ba829)#define DIO14\_T1\_C2N IOC\_PORTCFG\_PFUNC2

[ 145](cc23x0-pinctrl_8h.md#af9774a009ad29c47036e7b07960ae463)#define DIO14\_LRFD5 IOC\_PORTCFG\_PFUNC3

[ 146](cc23x0-pinctrl_8h.md#a696088726823aa9e47180eadf02d3313)#define DIO14\_T1\_F IOC\_PORTCFG\_PFUNC4

147

[ 148](cc23x0-pinctrl_8h.md#a7b466888d002460d0428519529ea5801)#define DIO15\_GPIO15 IOC\_PORTCFG\_BASE

[ 149](cc23x0-pinctrl_8h.md#a7af48be34e0d425d8ccc4fceb79d94d6)#define DIO15\_UART0\_RXD IOC\_PORTCFG\_PFUNC1

[ 150](cc23x0-pinctrl_8h.md#acebedef69b351c4431523381334adcb1)#define DIO15\_T2\_C0N IOC\_PORTCFG\_PFUNC2

[ 151](cc23x0-pinctrl_8h.md#afddb1472afadde08d88f6abd1dc5d5ff)#define DIO15\_CKMIN IOC\_PORTCFG\_PFUNC3

152

[ 153](cc23x0-pinctrl_8h.md#a076f8c5d1093fd600d3e9ba2edad8431)#define DIO16\_GPIO16 IOC\_PORTCFG\_BASE

[ 154](cc23x0-pinctrl_8h.md#a603eb2c90c89a84edd7eb73290defd91)#define DIO16\_SPI0\_MOSI IOC\_PORTCFG\_PFUNC1

[ 155](cc23x0-pinctrl_8h.md#a04c17e95330f4aaa17d886d2f5053cc9)#define DIO16\_UART0\_RXD IOC\_PORTCFG\_PFUNC2

[ 156](cc23x0-pinctrl_8h.md#a68ae64d639cab3dbadcaf50c92a13fbd)#define DIO16\_I2C0\_SDA IOC\_PORTCFG\_PFUNC3

[ 157](cc23x0-pinctrl_8h.md#a280b489d7c4528ec5a0775c3b83ba551)#define DIO16\_T1\_C2 IOC\_PORTCFG\_PFUNC4

[ 158](cc23x0-pinctrl_8h.md#aa1e519e01cb798538022755aaf81574a)#define DIO16\_T1\_C0N IOC\_PORTCFG\_PFUNC5

[ 159](cc23x0-pinctrl_8h.md#ab14227b4703363152450eefdfe5f0186)#define DIO16\_DTB10 IOC\_PORTCFG\_DTB

160

[ 161](cc23x0-pinctrl_8h.md#aa6695223061a1bf458e6b5cf667a4ef3)#define DIO17\_GPIO17 IOC\_PORTCFG\_BASE

[ 162](cc23x0-pinctrl_8h.md#a01082d3bb0958749c3a705ebd381d304)#define DIO17\_SPI0\_SCLK IOC\_PORTCFG\_PFUNC1

[ 163](cc23x0-pinctrl_8h.md#a6af94601226f5b9da48be2449edf12c3)#define DIO17\_UART0\_TXD IOC\_PORTCFG\_PFUNC2

[ 164](cc23x0-pinctrl_8h.md#a724128f152f9c8153925c0b433aa46aa)#define DIO17\_I2C0\_SCL IOC\_PORTCFG\_PFUNC3

[ 165](cc23x0-pinctrl_8h.md#ad690f4824516a3f08fd8cbb1e4baec5e)#define DIO17\_T1\_C1N IOC\_PORTCFG\_PFUNC4

[ 166](cc23x0-pinctrl_8h.md#a885ff00b679ea6922cb8177310871aee)#define DIO17\_T0\_C2 IOC\_PORTCFG\_PFUNC5

[ 167](cc23x0-pinctrl_8h.md#a79ba035326c60d89c4ab8b8de50eee6b)#define DIO17\_DTB11 IOC\_PORTCFG\_DTB

168

[ 169](cc23x0-pinctrl_8h.md#abbcd9337ffa2c9120d74cf17bcc7092f)#define DIO18\_GPIO18 IOC\_PORTCFG\_BASE

[ 170](cc23x0-pinctrl_8h.md#a5e9c6406866d7aaa23929a4cec8fc828)#define DIO18\_T3\_C0 IOC\_PORTCFG\_PFUNC1

[ 171](cc23x0-pinctrl_8h.md#a3944baa4569ea0dccccedf1729c962f7)#define DIO18\_LPC0 IOC\_PORTCFG\_PFUNC2

[ 172](cc23x0-pinctrl_8h.md#ab9c8fac3f7501cf6303771c87040cb78)#define DIO18\_UART0\_TXD IOC\_PORTCFG\_PFUNC3

[ 173](cc23x0-pinctrl_8h.md#a2751e01acf954ff4bb4a10bab7d39153)#define DIO18\_SPI0\_SCLK IOC\_PORTCFG\_PFUNC4

[ 174](cc23x0-pinctrl_8h.md#afe75a43f8da9e6ac26d98d11e62a7f0f)#define DIO18\_DTB12 IOC\_PORTCFG\_DTB

175

[ 176](cc23x0-pinctrl_8h.md#a7c21093db3bdff8c498afd0564a58ff8)#define DIO19\_GPIO19 IOC\_PORTCFG\_BASE

[ 177](cc23x0-pinctrl_8h.md#a516468dc4fd432493b9686d9c295c1a0)#define DIO19\_T3\_C1 IOC\_PORTCFG\_PFUNC1

[ 178](cc23x0-pinctrl_8h.md#aa055d07c9295649e85dbc84e210bfe8a)#define DIO19\_T2\_PE IOC\_PORTCFG\_PFUNC2

[ 179](cc23x0-pinctrl_8h.md#a79de211a3fc81572d675791c8eab515d)#define DIO19\_SPI0\_MOSI IOC\_PORTCFG\_PFUNC4

[ 180](cc23x0-pinctrl_8h.md#accad3142e44944f617f4b6ade2f07c1e)#define DIO19\_DTB0 IOC\_PORTCFG\_DTB

181

[ 182](cc23x0-pinctrl_8h.md#a9dde4d0ddc64a4c2e78c050210e467dc)#define DIO20\_GPIO20 IOC\_PORTCFG\_BASE

[ 183](cc23x0-pinctrl_8h.md#ab590e7f2abe46b464f1e9d6a89059e25)#define DIO20\_LPC0 IOC\_PORTCFG\_PFUNC1

[ 184](cc23x0-pinctrl_8h.md#aa68e87bb88d59212e0768800c7aa7f48)#define DIO20\_UART0\_TXD IOC\_PORTCFG\_PFUNC2

[ 185](cc23x0-pinctrl_8h.md#a0ae35f4a7376bb6980832c871ab714d5)#define DIO20\_UART0\_RXD IOC\_PORTCFG\_PFUNC3

[ 186](cc23x0-pinctrl_8h.md#a032c884bb4ad0772aa26e2f41f49310f)#define DIO20\_T1\_C0 IOC\_PORTCFG\_PFUNC4

[ 187](cc23x0-pinctrl_8h.md#aa78b09deb2e32131c51af0aa2cf186a4)#define DIO20\_SPI0\_MISO IOC\_PORTCFG\_PFUNC5

[ 188](cc23x0-pinctrl_8h.md#af160531047627880d2c9a45fc4e78d3c)#define DIO20\_ADC11 IOC\_PORTCFG\_ANA

[ 189](cc23x0-pinctrl_8h.md#ad45e111439f668b6b3b2c2a8dc197685)#define DIO20\_DTB14 IOC\_PORTCFG\_DTB

190

[ 191](cc23x0-pinctrl_8h.md#a3543027e96dd24a8f423642793f9231f)#define DIO21\_GPIO21 IOC\_PORTCFG\_BASE

[ 192](cc23x0-pinctrl_8h.md#aeda0333fb8765d7a24d514ee25d1b4b2)#define DIO21\_UART0\_CTS IOC\_PORTCFG\_PFUNC1

[ 193](cc23x0-pinctrl_8h.md#a938311835000f5598aa29b4140fe6886)#define DIO21\_T1\_C1N IOC\_PORTCFG\_PFUNC2

[ 194](cc23x0-pinctrl_8h.md#ae217ff4c8cf56f66ad3bec48d95ea87f)#define DIO21\_T0\_C1 IOC\_PORTCFG\_PFUNC3

[ 195](cc23x0-pinctrl_8h.md#a8d66bd3f2da6e8e38b7d464d2e8fbe2e)#define DIO21\_SPI0\_MISO IOC\_PORTCFG\_PFUNC4

[ 196](cc23x0-pinctrl_8h.md#adc4c2c233df06c2f52ccd24dee3c6664)#define DIO21\_LRFD1 IOC\_PORTCFG\_PFUNC5

[ 197](cc23x0-pinctrl_8h.md#a9351b7540ddc91c96c7eb06c6e3160e9)#define DIO21\_ADC10\_LPCP IOC\_PORTCFG\_ANA

[ 198](cc23x0-pinctrl_8h.md#a58b92ea2552dd70802efc1c996e47db7)#define DIO21\_DTB15 IOC\_PORTCFG\_DTB

199

[ 200](cc23x0-pinctrl_8h.md#a0a59e5293cbce628fb9ed582ed8640f5)#define DIO22\_GPIO22 IOC\_PORTCFG\_BASE

[ 201](cc23x0-pinctrl_8h.md#ab4318e5a3f89c6d0a09e11f5cba9938a)#define DIO22\_T2\_C0 IOC\_PORTCFG\_PFUNC1

[ 202](cc23x0-pinctrl_8h.md#af1e0eff63be94a61ba5910793796f2eb)#define DIO22\_UART0\_RXD IOC\_PORTCFG\_PFUNC2

[ 203](cc23x0-pinctrl_8h.md#af2086537e03f4e02f8edbfab24e1e0cc)#define DIO22\_T3\_C1N IOC\_PORTCFG\_PFUNC3

[ 204](cc23x0-pinctrl_8h.md#a124a45cbc60d6e3b80d2242483a4e48e)#define DIO22\_ADC9 IOC\_PORTCFG\_ANA

[ 205](cc23x0-pinctrl_8h.md#aee614c39986f53d769971914fe0f09bf)#define DIO22\_DTB1 IOC\_PORTCFG\_DTB

206

[ 207](cc23x0-pinctrl_8h.md#a7b6e8fc88c08014e5f55fb61b631f630)#define DIO23\_GPIO23 IOC\_PORTCFG\_BASE

[ 208](cc23x0-pinctrl_8h.md#a458eb72bee3bc88ae42b099da2a8d8b5)#define DIO23\_T2\_C1 IOC\_PORTCFG\_PFUNC1

[ 209](cc23x0-pinctrl_8h.md#a24e0baa35ebf15509fa6df01161b550c)#define DIO23\_T3\_C2N IOC\_PORTCFG\_PFUNC3

[ 210](cc23x0-pinctrl_8h.md#a3680907697a966084193c02a0a9b092b)#define DIO23\_ADC8\_LPCP\_LPCM IOC\_PORTCFG\_ANA

211

[ 212](cc23x0-pinctrl_8h.md#ab007c4540993b710800e31b01c59ac45)#define DIO24\_GPIO24 IOC\_PORTCFG\_BASE

[ 213](cc23x0-pinctrl_8h.md#a449c49cd104260e5c8d8af85121d3a1e)#define DIO24\_SPI0\_SCLK IOC\_PORTCFG\_PFUNC1

[ 214](cc23x0-pinctrl_8h.md#aee83a92878c7892d370985a85f49982f)#define DIO24\_T1\_C0 IOC\_PORTCFG\_PFUNC2

[ 215](cc23x0-pinctrl_8h.md#a9ada17b86400635fe102fc2525d792fc)#define DIO24\_T3\_C0 IOC\_PORTCFG\_PFUNC3

[ 216](cc23x0-pinctrl_8h.md#a0fb7b862a44272d6fd564d472ea31e21)#define DIO24\_T0\_PE IOC\_PORTCFG\_PFUNC4

[ 217](cc23x0-pinctrl_8h.md#a110d85e1d37be48932cbf1d89c0be29e)#define DIO24\_I2C0\_SCL IOC\_PORTCFG\_PFUNC5

[ 218](cc23x0-pinctrl_8h.md#a8ac3818f8c180ff363102c1037a39bb3)#define DIO24\_ADC7\_LPCP\_LPCM IOC\_PORTCFG\_ANA

[ 219](cc23x0-pinctrl_8h.md#a90d085bab2b84b19d92eee13c3760f97)#define DIO24\_DTB5 IOC\_PORTCFG\_DTB

220

[ 221](cc23x0-pinctrl_8h.md#ae8f1ccd4414f0b0bf1724eb52fc5e2f4)#define DIO25\_GPIO25 IOC\_PORTCFG\_BASE

[ 222](cc23x0-pinctrl_8h.md#ad7f714f27470179ac1653fa13d4b6f3a)#define DIO25\_SPI0\_MISO IOC\_PORTCFG\_PFUNC1

[ 223](cc23x0-pinctrl_8h.md#a2b4cca3f5437f8e8f7889194b566a21f)#define DIO25\_I2C0\_SCL IOC\_PORTCFG\_PFUNC2

[ 224](cc23x0-pinctrl_8h.md#a5d80e2f09069929f0fd4801a953a7684)#define DIO25\_T2\_C2N IOC\_PORTCFG\_PFUNC3

[ 225](cc23x0-pinctrl_8h.md#a1646bb58bfa079d72088be6dbacf1699)#define DIO25\_ADC6 IOC\_PORTCFG\_ANA

226

227#endif /\* CC23X0\_PINCTRL\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [cc23x0-pinctrl.h](cc23x0-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
