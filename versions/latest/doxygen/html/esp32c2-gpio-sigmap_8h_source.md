---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp32c2-gpio-sigmap_8h_source.html
original_path: doxygen/html/esp32c2-gpio-sigmap_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c2-gpio-sigmap.h

[Go to the documentation of this file.](esp32c2-gpio-sigmap_8h.md)

1/\*

2 \* Copyright (c) 2024 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C2\_GPIO\_SIGMAP\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C2\_GPIO\_SIGMAP\_H\_

9

[ 10](esp32c2-gpio-sigmap_8h.md#af80260535bc3aee44c28c972a29483e0)#define ESP\_NOSIG ESP\_SIG\_INVAL

11

[ 12](esp32c2-gpio-sigmap_8h.md#aaf157f6b85a07f18b181876a7a04f142)#define ESP\_SPICLK\_OUT\_MUX ESP\_SPICLK\_OUT

[ 13](esp32c2-gpio-sigmap_8h.md#aec51ff955c6be50e529affc87ec9d5cb)#define ESP\_SPIQ\_IN 0

[ 14](esp32c2-gpio-sigmap_8h.md#a5816deeca8853397a830a8eb251704ee)#define ESP\_SPIQ\_OUT 0

[ 15](esp32c2-gpio-sigmap_8h.md#a26c603fd58dbd7526d2be3bb3e37758a)#define ESP\_SPID\_IN 1

[ 16](esp32c2-gpio-sigmap_8h.md#af81b2fc65b68ed2238ab3367a8731102)#define ESP\_SPID\_OUT 1

[ 17](esp32c2-gpio-sigmap_8h.md#a49783f877b666aff9362cf605590b991)#define ESP\_SPIHD\_IN 2

[ 18](esp32c2-gpio-sigmap_8h.md#a8851b5256482790f3304efecafc13afd)#define ESP\_SPIHD\_OUT 2

[ 19](esp32c2-gpio-sigmap_8h.md#aa74adc2812d9c6bd143c679fa4d9ca8d)#define ESP\_SPIWP\_IN 3

[ 20](esp32c2-gpio-sigmap_8h.md#a470408f8102937dc017336e320e6147b)#define ESP\_SPIWP\_OUT 3

[ 21](esp32c2-gpio-sigmap_8h.md#a5f440c922a53085bb7b28f469c2a14b0)#define ESP\_SPICLK\_OUT 4

[ 22](esp32c2-gpio-sigmap_8h.md#a5d97c07ba0d8cda594d52310e90fa6a4)#define ESP\_SPICS0\_OUT 5

[ 23](esp32c2-gpio-sigmap_8h.md#aca502efa55ce2286dc9eba28192681fd)#define ESP\_U0RXD\_IN 6

[ 24](esp32c2-gpio-sigmap_8h.md#af1e58fb8e7ef86a92171eca7bb1671af)#define ESP\_U0TXD\_OUT 6

[ 25](esp32c2-gpio-sigmap_8h.md#a530d7a918a97cd1fff1acf2f90edd4ca)#define ESP\_U0CTS\_IN 7

[ 26](esp32c2-gpio-sigmap_8h.md#a4257bbc044af6ea3612313e3a0b7e7c9)#define ESP\_U0RTS\_OUT 7

[ 27](esp32c2-gpio-sigmap_8h.md#a53e3a4557a4eb1f7f98250abef03c02a)#define ESP\_U0DSR\_IN 8

[ 28](esp32c2-gpio-sigmap_8h.md#acc8716af947169c9f167bdf215c5314c)#define ESP\_U0DTR\_OUT 8

[ 29](esp32c2-gpio-sigmap_8h.md#a2293e0646e0ad2f76d62f76425ae6770)#define ESP\_U1RXD\_IN 9

[ 30](esp32c2-gpio-sigmap_8h.md#a6053b38147e28e3a7479b38e7d195136)#define ESP\_U1TXD\_OUT 9

[ 31](esp32c2-gpio-sigmap_8h.md#a3c005e616da21a058960d6aed79427b3)#define ESP\_U1CTS\_IN 10

[ 32](esp32c2-gpio-sigmap_8h.md#a8f6399745566bd5caa2020e4dcb2bb3b)#define ESP\_U1RTS\_OUT 10

[ 33](esp32c2-gpio-sigmap_8h.md#a5f29b138691540598d0b977dc4bd5971)#define ESP\_U1DSR\_IN 11

[ 34](esp32c2-gpio-sigmap_8h.md#a1f7df042d40ec6f20b559ef6778d7497)#define ESP\_U1DTR\_OUT 11

[ 35](esp32c2-gpio-sigmap_8h.md#a6abe131ab233461292f2987aadfee11a)#define ESP\_SPIQ\_MONITOR 15

[ 36](esp32c2-gpio-sigmap_8h.md#a6292a461f60010aec29fcc8356d514fd)#define ESP\_SPID\_MONITOR 16

[ 37](esp32c2-gpio-sigmap_8h.md#aff145e44d8e8e506225362072c6c6710)#define ESP\_SPIHD\_MONITOR 17

[ 38](esp32c2-gpio-sigmap_8h.md#a610bf782c52a09f754e16890a13851da)#define ESP\_SPIWP\_MONITOR 18

[ 39](esp32c2-gpio-sigmap_8h.md#aa4a67a38b97a3d466783c0617aa6a0c8)#define ESP\_SPICS1\_OUT 19

[ 40](esp32c2-gpio-sigmap_8h.md#a944cd61f21b48eb29d6a02dd36cadccf)#define ESP\_CPU\_TESTBUS0 20

[ 41](esp32c2-gpio-sigmap_8h.md#a2410d405f9a5a5ce1540eb9aea9b9f9e)#define ESP\_CPU\_TESTBUS1 21

[ 42](esp32c2-gpio-sigmap_8h.md#ae2f12f49b45db8f086ed1aa16fdb2e1b)#define ESP\_CPU\_TESTBUS2 22

[ 43](esp32c2-gpio-sigmap_8h.md#a225737984d07250e17b56aaf8e60289f)#define ESP\_CPU\_TESTBUS3 23

[ 44](esp32c2-gpio-sigmap_8h.md#ae3fbd8b602f8b71f7e8961442d38b720)#define ESP\_CPU\_TESTBUS4 24

[ 45](esp32c2-gpio-sigmap_8h.md#a5ce40632a364fdbfd94369806fc8dabc)#define ESP\_CPU\_TESTBUS5 25

[ 46](esp32c2-gpio-sigmap_8h.md#ae90382a0bb5727cf4981518b04e7b339)#define ESP\_CPU\_TESTBUS6 26

[ 47](esp32c2-gpio-sigmap_8h.md#ad21e1f7daa92fd691e1be1d9079e7cc2)#define ESP\_CPU\_TESTBUS7 27

[ 48](esp32c2-gpio-sigmap_8h.md#ac0df832ec7feeb3042f50c1eb1617f53)#define ESP\_CPU\_GPIO\_IN0 28

[ 49](esp32c2-gpio-sigmap_8h.md#aef48b51b644720c53dacdc6037ec7bc0)#define ESP\_CPU\_GPIO\_OUT0 28

[ 50](esp32c2-gpio-sigmap_8h.md#a0cc3cac4ad6eeb0c8c3cf0105f118554)#define ESP\_CPU\_GPIO\_IN1 29

[ 51](esp32c2-gpio-sigmap_8h.md#a8c9087d7ac05fa248d42b86997d79f01)#define ESP\_CPU\_GPIO\_OUT1 29

[ 52](esp32c2-gpio-sigmap_8h.md#ad7bce49dbf1ed089e8695d5a1ae99861)#define ESP\_CPU\_GPIO\_IN2 30

[ 53](esp32c2-gpio-sigmap_8h.md#a6d7108dcd0de2f3a6bbb84c6703baa3f)#define ESP\_CPU\_GPIO\_OUT2 30

[ 54](esp32c2-gpio-sigmap_8h.md#a553b001f496ac3689979841a04a7a862)#define ESP\_CPU\_GPIO\_IN3 31

[ 55](esp32c2-gpio-sigmap_8h.md#ad3d027b5581594073ea70b1955bb5733)#define ESP\_CPU\_GPIO\_OUT3 31

[ 56](esp32c2-gpio-sigmap_8h.md#a848b0915100b8e3b75089854d32910ee)#define ESP\_CPU\_GPIO\_IN4 32

[ 57](esp32c2-gpio-sigmap_8h.md#ac761dfb305a0e44a2447789680fd0ff9)#define ESP\_CPU\_GPIO\_OUT4 32

[ 58](esp32c2-gpio-sigmap_8h.md#abb64fd2a84298157b6071cc127a3c0ca)#define ESP\_CPU\_GPIO\_IN5 33

[ 59](esp32c2-gpio-sigmap_8h.md#add1c492755091bcdeafabe38cb65617b)#define ESP\_CPU\_GPIO\_OUT5 33

[ 60](esp32c2-gpio-sigmap_8h.md#a1695bafbd25037bcd848c5b58bdae422)#define ESP\_CPU\_GPIO\_IN6 34

[ 61](esp32c2-gpio-sigmap_8h.md#a929fc17e60b97257fef693b9ac1682ad)#define ESP\_CPU\_GPIO\_OUT6 34

[ 62](esp32c2-gpio-sigmap_8h.md#a10dc617c0b532ee5a8ae3d913a984007)#define ESP\_CPU\_GPIO\_IN7 35

[ 63](esp32c2-gpio-sigmap_8h.md#ad54946b60e601390d863b20dd1c13e32)#define ESP\_CPU\_GPIO\_OUT7 35

[ 64](esp32c2-gpio-sigmap_8h.md#ae49b4527d8fbd0f5c8e3edc72704c54a)#define ESP\_EXT\_ADC\_START 45

[ 65](esp32c2-gpio-sigmap_8h.md#a62dfcd88747c61acb53dc85c1751f1d3)#define ESP\_LEDC\_LS\_SIG\_OUT0 45

[ 66](esp32c2-gpio-sigmap_8h.md#a5cad9206cfeea93b42e5456228c7d580)#define ESP\_LEDC\_LS\_SIG\_OUT1 46

[ 67](esp32c2-gpio-sigmap_8h.md#ab408070e7c700805db165c3876b6c588)#define ESP\_LEDC\_LS\_SIG\_OUT2 47

[ 68](esp32c2-gpio-sigmap_8h.md#a438aee217c6c94a2962a3d98935b5717)#define ESP\_LEDC\_LS\_SIG\_OUT3 48

[ 69](esp32c2-gpio-sigmap_8h.md#ada93dcffffc15362be4b7432a8033559)#define ESP\_LEDC\_LS\_SIG\_OUT4 49

[ 70](esp32c2-gpio-sigmap_8h.md#a34fc029ec45756ca7064580f57db1cc7)#define ESP\_LEDC\_LS\_SIG\_OUT5 50

[ 71](esp32c2-gpio-sigmap_8h.md#ad9bae9b4884a356e465656d1ee8d61cd)#define ESP\_RMT\_SIG\_IN0 51

[ 72](esp32c2-gpio-sigmap_8h.md#a25343fbc20a0c542bcdc21cdfade867b)#define ESP\_RMT\_SIG\_OUT0 51

[ 73](esp32c2-gpio-sigmap_8h.md#ab6c6293e6845ba4bf4d05b84102ffdcf)#define ESP\_RMT\_SIG\_IN1 52

[ 74](esp32c2-gpio-sigmap_8h.md#a6d082fb1c7397d784a3075108e0dea73)#define ESP\_RMT\_SIG\_OUT1 52

[ 75](esp32c2-gpio-sigmap_8h.md#ab607ce367da34ab0f1bd7fa648273cf1)#define ESP\_I2CEXT0\_SCL\_IN 53

[ 76](esp32c2-gpio-sigmap_8h.md#a2144cc62df795547ccf2bbe3ee4c629f)#define ESP\_I2CEXT0\_SCL\_OUT 53

[ 77](esp32c2-gpio-sigmap_8h.md#afa7061c87135b9dabe5c54f5f4ce16e6)#define ESP\_I2CEXT0\_SDA\_IN 54

[ 78](esp32c2-gpio-sigmap_8h.md#aabf1378b0ad2028c36c3bb74c81d7049)#define ESP\_I2CEXT0\_SDA\_OUT 54

[ 79](esp32c2-gpio-sigmap_8h.md#ade88988460c131e8c6775794588b0eb8)#define ESP\_FSPICLK\_IN 63

[ 80](esp32c2-gpio-sigmap_8h.md#ab8c5397dc530f6326c3d10b31e59e168)#define ESP\_FSPICLK\_OUT 63

[ 81](esp32c2-gpio-sigmap_8h.md#ab603b7bf7d016e85653a5c3be5c01293)#define ESP\_FSPIQ\_IN 64

[ 82](esp32c2-gpio-sigmap_8h.md#a8b3ea6ad374fa010b46b48072fa87ccb)#define ESP\_FSPIQ\_OUT 64

[ 83](esp32c2-gpio-sigmap_8h.md#a7910521af840d42edd3c0a667cf90c5f)#define ESP\_FSPID\_IN 65

[ 84](esp32c2-gpio-sigmap_8h.md#a02bd34821e8a4bf0038b9af417ec161a)#define ESP\_FSPID\_OUT 65

[ 85](esp32c2-gpio-sigmap_8h.md#a60ff087a3d85a356d77f060a6698d00b)#define ESP\_FSPIHD\_IN 66

[ 86](esp32c2-gpio-sigmap_8h.md#ac71bc137b93bd6c0c8a1ebe24a70a613)#define ESP\_FSPIHD\_OUT 66

[ 87](esp32c2-gpio-sigmap_8h.md#a4d4c4a13b820cab6d94da8fe08120a2f)#define ESP\_FSPIWP\_IN 67

[ 88](esp32c2-gpio-sigmap_8h.md#a83c4f18d726984cc98caeea9b7677ca1)#define ESP\_FSPIWP\_OUT 67

[ 89](esp32c2-gpio-sigmap_8h.md#a96ca1328e76337d289f6e65faf33d75c)#define ESP\_FSPICS0\_IN 68

[ 90](esp32c2-gpio-sigmap_8h.md#ad1be1401b282275eaef46b9a598c6a40)#define ESP\_FSPICS0\_OUT 68

[ 91](esp32c2-gpio-sigmap_8h.md#a44ade9179a7ea00586359a009799661d)#define ESP\_FSPICS1\_OUT 69

[ 92](esp32c2-gpio-sigmap_8h.md#af991963f29c5b268a5f8fead8fd15348)#define ESP\_FSPICS2\_OUT 70

[ 93](esp32c2-gpio-sigmap_8h.md#a65d1170c5a68ac7f6a4457c3380ddfde)#define ESP\_FSPICS3\_OUT 71

[ 94](esp32c2-gpio-sigmap_8h.md#a83dafe68703c701dcd07d7ff0aadad01)#define ESP\_FSPICS4\_OUT 72

[ 95](esp32c2-gpio-sigmap_8h.md#ad8fab64bb220fd198a6cd931f4ea1e8e)#define ESP\_FSPICS5\_OUT 73

[ 96](esp32c2-gpio-sigmap_8h.md#a39627b897d55107e1ecee725bd662ec2)#define ESP\_EXTERN\_PRIORITY\_I 77

[ 97](esp32c2-gpio-sigmap_8h.md#ab50a3b95442a89e070163c623a261578)#define ESP\_EXTERN\_PRIORITY\_O 77

[ 98](esp32c2-gpio-sigmap_8h.md#a533fcce69d815e97b58d7f1af1d4505c)#define ESP\_EXTERN\_ACTIVE\_I 78

[ 99](esp32c2-gpio-sigmap_8h.md#a198d1c07a648c5353e1c127e855d47c9)#define ESP\_EXTERN\_ACTIVE\_O 78

[ 100](esp32c2-gpio-sigmap_8h.md#a2af8dc70a06105740ae181a616186624)#define ESP\_GPIO\_EVENT\_MATRIX\_IN0 79

[ 101](esp32c2-gpio-sigmap_8h.md#aeee7dc180a750016e7711282b252ccf6)#define ESP\_GPIO\_TASK\_MATRIX\_OUT0 79

[ 102](esp32c2-gpio-sigmap_8h.md#a7a2ce6558a5368d1fc0325ce37487d1a)#define ESP\_GPIO\_EVENT\_MATRIX\_IN1 80

[ 103](esp32c2-gpio-sigmap_8h.md#a4ce0ef64cebc11e961d73fc58d8bb954)#define ESP\_GPIO\_TASK\_MATRIX\_OUT1 80

[ 104](esp32c2-gpio-sigmap_8h.md#a2ae077cc87f156e9545eca4a091890e3)#define ESP\_GPIO\_EVENT\_MATRIX\_IN2 81

[ 105](esp32c2-gpio-sigmap_8h.md#a0ac11865f0be99e81bebeb7dfbe1424b)#define ESP\_GPIO\_TASK\_MATRIX\_OUT2 81

[ 106](esp32c2-gpio-sigmap_8h.md#a97d8c86a5d7ba47196816c7d04ef7efb)#define ESP\_GPIO\_EVENT\_MATRIX\_IN3 82

[ 107](esp32c2-gpio-sigmap_8h.md#a165323f111794aeff16e7073501ff16e)#define ESP\_GPIO\_TASK\_MATRIX\_OUT3 82

[ 108](esp32c2-gpio-sigmap_8h.md#af142a270dafe58997f617efb61512d30)#define ESP\_BB\_DIAG8\_OUT 83

[ 109](esp32c2-gpio-sigmap_8h.md#a617d3a75257f691b0797e50de7a7b465)#define ESP\_BB\_DIAG9\_OUT 84

[ 110](esp32c2-gpio-sigmap_8h.md#aab71da6e85a906a438d27e2b6bd9a921)#define ESP\_BB\_DIAG10\_OUT 85

[ 111](esp32c2-gpio-sigmap_8h.md#a189e37f0d904a0ba97354a7c3a54ca40)#define ESP\_BB\_DIAG11\_OUT 86

[ 112](esp32c2-gpio-sigmap_8h.md#a0d59630bc17c91a35eb36a5c5aa0a80c)#define ESP\_BB\_DIAG12\_OUT 87

[ 113](esp32c2-gpio-sigmap_8h.md#ac851f634048c53a550a07e6bec6c6b8a)#define ESP\_BB\_DIAG13\_OUT 88

[ 114](esp32c2-gpio-sigmap_8h.md#aec2dfb198f69d923686404a0a6330833)#define ESP\_ANT\_SEL0 89

[ 115](esp32c2-gpio-sigmap_8h.md#a15c080ea1e4c8e2db9f1640e9b8c4f0a)#define ESP\_ANT\_SEL1 90

[ 116](esp32c2-gpio-sigmap_8h.md#ae3042ff86ecc0f2e78ebe9477055e819)#define ESP\_ANT\_SEL2 91

[ 117](esp32c2-gpio-sigmap_8h.md#ab8e5cca4b9eb1a7bda7868ecd792c76d)#define ESP\_ANT\_SEL3 92

[ 118](esp32c2-gpio-sigmap_8h.md#a821cc4b81f76043b1ecb751118a2f416)#define ESP\_ANT\_SEL4 93

[ 119](esp32c2-gpio-sigmap_8h.md#a28a954881fd9d5f5e7ff25d715f0bcc2)#define ESP\_ANT\_SEL5 94

[ 120](esp32c2-gpio-sigmap_8h.md#a2122dad1966cbe214e9c82cb9a46bd8a)#define ESP\_ANT\_SEL6 95

[ 121](esp32c2-gpio-sigmap_8h.md#a8f9cedf15c49cee3fbac2a22df7675ec)#define ESP\_ANT\_SEL7 96

[ 122](esp32c2-gpio-sigmap_8h.md#a66890ae0c0e6a875c19099abb1918ca1)#define ESP\_SIG\_IN\_FUNC\_97 97

[ 123](esp32c2-gpio-sigmap_8h.md#a919b1b0e57d8785970c702fcd49d5563)#define ESP\_SIG\_IN\_FUNC97 97

[ 124](esp32c2-gpio-sigmap_8h.md#a848f955ed1b3b04d0a3d90f8c0acedec)#define ESP\_SIG\_IN\_FUNC\_98 98

[ 125](esp32c2-gpio-sigmap_8h.md#ae6043332289b10b68dc1d278681f3df1)#define ESP\_SIG\_IN\_FUNC98 98

[ 126](esp32c2-gpio-sigmap_8h.md#ab6956182e8d06463813e94843398a45f)#define ESP\_SIG\_IN\_FUNC\_99 99

[ 127](esp32c2-gpio-sigmap_8h.md#a11dcdffc24ff5d98c7c8d0f609a0c7b9)#define ESP\_SIG\_IN\_FUNC99 99

[ 128](esp32c2-gpio-sigmap_8h.md#a6684d495dfe99d0798f576018ffe0aba)#define ESP\_SIG\_IN\_FUNC\_100 100

[ 129](esp32c2-gpio-sigmap_8h.md#a33f1fad3bde9b252dfb3a291d600c019)#define ESP\_SIG\_IN\_FUNC100 100

[ 130](esp32c2-gpio-sigmap_8h.md#aa80adfd043a26d791a5e9c31de201164)#define ESP\_BLE\_DBG\_SYNCERR 101

[ 131](esp32c2-gpio-sigmap_8h.md#a8f7e3cba06744a8a0fa588630928d423)#define ESP\_BLE\_DBG\_SYNC\_FOUND 102

[ 132](esp32c2-gpio-sigmap_8h.md#aa46207fab7ed6822b75880b531879190)#define ESP\_BLE\_DBG\_CH\_IDX 103

[ 133](esp32c2-gpio-sigmap_8h.md#afa25c4867b6f4f78e32618d2ed804ccb)#define ESP\_BLE\_DBG\_SYNC\_WINDOW 104

[ 134](esp32c2-gpio-sigmap_8h.md#afa5cc2bba649ccc7532eca43c80c31bf)#define ESP\_BLE\_DBG\_DATA\_EN 105

[ 135](esp32c2-gpio-sigmap_8h.md#a1c9ccf8879588f15c83be60de6c2a9ca)#define ESP\_BLE\_DBG\_DATA 106

[ 136](esp32c2-gpio-sigmap_8h.md#a5b9f79d6c4a300f6949ee075fb462814)#define ESP\_BLE\_DBG\_PKT\_TX\_ON 107

[ 137](esp32c2-gpio-sigmap_8h.md#a0592bcc99eb7e739a1daf53fbae72965)#define ESP\_BLE\_DBG\_PKT\_RX\_ON 108

[ 138](esp32c2-gpio-sigmap_8h.md#a81d7d01938d7b4a840f21b48bc702d95)#define ESP\_BLE\_DBG\_TXRU\_ON 109

[ 139](esp32c2-gpio-sigmap_8h.md#a3766af70b405de3b991e90996a758d83)#define ESP\_BLE\_DBG\_RXRU\_ON 110

[ 140](esp32c2-gpio-sigmap_8h.md#ab87a5364ee77e3c700f6180ac45d4bf2)#define ESP\_BLE\_DBG\_LELC\_ST0 111

[ 141](esp32c2-gpio-sigmap_8h.md#ad4560183706658c3c6a41e6e705fb804)#define ESP\_BLE\_DBG\_LELC\_ST1 112

[ 142](esp32c2-gpio-sigmap_8h.md#af4a076c4f02e0d5eb390aa148e51c1f7)#define ESP\_BLE\_DBG\_LELC\_ST2 113

[ 143](esp32c2-gpio-sigmap_8h.md#ada8272aaa110794ae2214bb1fd2b44b0)#define ESP\_BLE\_DBG\_LELC\_ST3 114

[ 144](esp32c2-gpio-sigmap_8h.md#a65b96d0f1327dcc17316f45d4286ce91)#define ESP\_BLE\_DBG\_CRCOK 115

[ 145](esp32c2-gpio-sigmap_8h.md#aeec8db4ffecedcc300f5961a55a48cc3)#define ESP\_BLE\_DBG\_CLK\_GPIO 116

[ 146](esp32c2-gpio-sigmap_8h.md#ae2cec5790ab61dd15dde088619708c2c)#define ESP\_BLE\_DBG\_RADIO\_START 117

[ 147](esp32c2-gpio-sigmap_8h.md#ad93ceefefe24132e4a194b322b20bccf)#define ESP\_BLE\_DBG\_SEQUENCE\_ON 118

[ 148](esp32c2-gpio-sigmap_8h.md#a9bca795190774e353d52eec0d90574bc)#define ESP\_BLE\_DBG\_COEX\_BT\_ON 119

[ 149](esp32c2-gpio-sigmap_8h.md#aa342f766b48aae7b5444505888673923)#define ESP\_BLE\_DBG\_COEX\_WIFI\_ON 120

[ 150](esp32c2-gpio-sigmap_8h.md#a12a2380f8bcbf158e7c114b7dc1701a5)#define ESP\_CLK\_OUT\_OUT1 123

[ 151](esp32c2-gpio-sigmap_8h.md#adf7a9c85596f3a536ddb603d3218cee2)#define ESP\_CLK\_OUT\_OUT2 124

[ 152](esp32c2-gpio-sigmap_8h.md#af421f62c654ecca5136b7b526f168377)#define ESP\_CLK\_OUT\_OUT3 125

[ 153](esp32c2-gpio-sigmap_8h.md#a645411759ffdc63f51f2cd42632d2720)#define ESP\_SIG\_GPIO\_OUT 128

[ 154](esp32c2-gpio-sigmap_8h.md#afe5c166b887709cdd27bd37df85c45b9)#define ESP\_GPIO\_MAP\_DATE 0x2106190

155

156#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C2\_GPIO\_SIGMAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32c2-gpio-sigmap.h](esp32c2-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
