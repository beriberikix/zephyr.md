---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp32c6-gpio-sigmap_8h_source.html
original_path: doxygen/html/esp32c6-gpio-sigmap_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c6-gpio-sigmap.h

[Go to the documentation of this file.](esp32c6-gpio-sigmap_8h.md)

1/\*

2 \* Copyright (c) 2023 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C6\_GPIO\_SIGMAP\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C6\_GPIO\_SIGMAP\_H\_

9

[ 10](esp32c6-gpio-sigmap_8h.md#af80260535bc3aee44c28c972a29483e0)#define ESP\_NOSIG ESP\_SIG\_INVAL

11

[ 12](esp32c6-gpio-sigmap_8h.md#ae49b4527d8fbd0f5c8e3edc72704c54a)#define ESP\_EXT\_ADC\_START 0

[ 13](esp32c6-gpio-sigmap_8h.md#a62dfcd88747c61acb53dc85c1751f1d3)#define ESP\_LEDC\_LS\_SIG\_OUT0 0

[ 14](esp32c6-gpio-sigmap_8h.md#a5cad9206cfeea93b42e5456228c7d580)#define ESP\_LEDC\_LS\_SIG\_OUT1 1

[ 15](esp32c6-gpio-sigmap_8h.md#ab408070e7c700805db165c3876b6c588)#define ESP\_LEDC\_LS\_SIG\_OUT2 2

[ 16](esp32c6-gpio-sigmap_8h.md#a438aee217c6c94a2962a3d98935b5717)#define ESP\_LEDC\_LS\_SIG\_OUT3 3

[ 17](esp32c6-gpio-sigmap_8h.md#ada93dcffffc15362be4b7432a8033559)#define ESP\_LEDC\_LS\_SIG\_OUT4 4

[ 18](esp32c6-gpio-sigmap_8h.md#a34fc029ec45756ca7064580f57db1cc7)#define ESP\_LEDC\_LS\_SIG\_OUT5 5

[ 19](esp32c6-gpio-sigmap_8h.md#aca502efa55ce2286dc9eba28192681fd)#define ESP\_U0RXD\_IN 6

[ 20](esp32c6-gpio-sigmap_8h.md#af1e58fb8e7ef86a92171eca7bb1671af)#define ESP\_U0TXD\_OUT 6

[ 21](esp32c6-gpio-sigmap_8h.md#a530d7a918a97cd1fff1acf2f90edd4ca)#define ESP\_U0CTS\_IN 7

[ 22](esp32c6-gpio-sigmap_8h.md#a4257bbc044af6ea3612313e3a0b7e7c9)#define ESP\_U0RTS\_OUT 7

[ 23](esp32c6-gpio-sigmap_8h.md#a53e3a4557a4eb1f7f98250abef03c02a)#define ESP\_U0DSR\_IN 8

[ 24](esp32c6-gpio-sigmap_8h.md#acc8716af947169c9f167bdf215c5314c)#define ESP\_U0DTR\_OUT 8

[ 25](esp32c6-gpio-sigmap_8h.md#a2293e0646e0ad2f76d62f76425ae6770)#define ESP\_U1RXD\_IN 9

[ 26](esp32c6-gpio-sigmap_8h.md#a6053b38147e28e3a7479b38e7d195136)#define ESP\_U1TXD\_OUT 9

[ 27](esp32c6-gpio-sigmap_8h.md#a3c005e616da21a058960d6aed79427b3)#define ESP\_U1CTS\_IN 10

[ 28](esp32c6-gpio-sigmap_8h.md#a8f6399745566bd5caa2020e4dcb2bb3b)#define ESP\_U1RTS\_OUT 10

[ 29](esp32c6-gpio-sigmap_8h.md#a5f29b138691540598d0b977dc4bd5971)#define ESP\_U1DSR\_IN 11

[ 30](esp32c6-gpio-sigmap_8h.md#a1f7df042d40ec6f20b559ef6778d7497)#define ESP\_U1DTR\_OUT 11

[ 31](esp32c6-gpio-sigmap_8h.md#a0c2eefdd5846623d330a6437ecfec3ef)#define ESP\_I2S\_MCLK\_IN 12

[ 32](esp32c6-gpio-sigmap_8h.md#a89708f46a7a1e03c9a654e9a529ec36c)#define ESP\_I2S\_MCLK\_OUT 12

[ 33](esp32c6-gpio-sigmap_8h.md#aa4d5f8ce3cc15e7ab7b2d17c79da3b91)#define ESP\_I2SO\_BCK\_IN 13

[ 34](esp32c6-gpio-sigmap_8h.md#ab586cc1b4ae5da20703f469bb8ff5c0e)#define ESP\_I2SO\_BCK\_OUT 13

[ 35](esp32c6-gpio-sigmap_8h.md#a2f5d7f663b568a4a609f8c9315f6cf5c)#define ESP\_I2SO\_WS\_IN 14

[ 36](esp32c6-gpio-sigmap_8h.md#a4be8f5f82ae51e880973256e748ef0a3)#define ESP\_I2SO\_WS\_OUT 14

[ 37](esp32c6-gpio-sigmap_8h.md#ac2d5d005dd8d5d5487dd24e021f2d3d5)#define ESP\_I2SI\_SD\_IN 15

[ 38](esp32c6-gpio-sigmap_8h.md#a2815be93d2102f382e8ed5c5f7913257)#define ESP\_I2SO\_SD\_OUT 15

[ 39](esp32c6-gpio-sigmap_8h.md#a0bc2c2947bb51d411a677fc07806e3fe)#define ESP\_I2SI\_BCK\_IN 16

[ 40](esp32c6-gpio-sigmap_8h.md#aa58a3701e86830736ae9b0b3d60ac6b5)#define ESP\_I2SI\_BCK\_OUT 16

[ 41](esp32c6-gpio-sigmap_8h.md#af1e51d50da781c498cda9e45e603544f)#define ESP\_I2SI\_WS\_IN 17

[ 42](esp32c6-gpio-sigmap_8h.md#aa0c2097b8e33d93001180bc068b85d5c)#define ESP\_I2SI\_WS\_OUT 17

[ 43](esp32c6-gpio-sigmap_8h.md#ad8ddad8dd3a5dc26e09f745499b02c7c)#define ESP\_I2SO\_SD1\_OUT 18

[ 44](esp32c6-gpio-sigmap_8h.md#a6b5babfcba4d025bdd1ab709b569fdf2)#define ESP\_USB\_JTAG\_TDO\_BRIDGE 19

[ 45](esp32c6-gpio-sigmap_8h.md#a4358434232f1f3515d8f5f4961d77520)#define ESP\_USB\_JTAG\_TRST 19

[ 46](esp32c6-gpio-sigmap_8h.md#a944cd61f21b48eb29d6a02dd36cadccf)#define ESP\_CPU\_TESTBUS0 20

[ 47](esp32c6-gpio-sigmap_8h.md#a2410d405f9a5a5ce1540eb9aea9b9f9e)#define ESP\_CPU\_TESTBUS1 21

[ 48](esp32c6-gpio-sigmap_8h.md#ae2f12f49b45db8f086ed1aa16fdb2e1b)#define ESP\_CPU\_TESTBUS2 22

[ 49](esp32c6-gpio-sigmap_8h.md#a225737984d07250e17b56aaf8e60289f)#define ESP\_CPU\_TESTBUS3 23

[ 50](esp32c6-gpio-sigmap_8h.md#ae3fbd8b602f8b71f7e8961442d38b720)#define ESP\_CPU\_TESTBUS4 24

[ 51](esp32c6-gpio-sigmap_8h.md#a5ce40632a364fdbfd94369806fc8dabc)#define ESP\_CPU\_TESTBUS5 25

[ 52](esp32c6-gpio-sigmap_8h.md#ae90382a0bb5727cf4981518b04e7b339)#define ESP\_CPU\_TESTBUS6 26

[ 53](esp32c6-gpio-sigmap_8h.md#ad21e1f7daa92fd691e1be1d9079e7cc2)#define ESP\_CPU\_TESTBUS7 27

[ 54](esp32c6-gpio-sigmap_8h.md#ac0df832ec7feeb3042f50c1eb1617f53)#define ESP\_CPU\_GPIO\_IN0 28

[ 55](esp32c6-gpio-sigmap_8h.md#aef48b51b644720c53dacdc6037ec7bc0)#define ESP\_CPU\_GPIO\_OUT0 28

[ 56](esp32c6-gpio-sigmap_8h.md#a0cc3cac4ad6eeb0c8c3cf0105f118554)#define ESP\_CPU\_GPIO\_IN1 29

[ 57](esp32c6-gpio-sigmap_8h.md#a8c9087d7ac05fa248d42b86997d79f01)#define ESP\_CPU\_GPIO\_OUT1 29

[ 58](esp32c6-gpio-sigmap_8h.md#ad7bce49dbf1ed089e8695d5a1ae99861)#define ESP\_CPU\_GPIO\_IN2 30

[ 59](esp32c6-gpio-sigmap_8h.md#a6d7108dcd0de2f3a6bbb84c6703baa3f)#define ESP\_CPU\_GPIO\_OUT2 30

[ 60](esp32c6-gpio-sigmap_8h.md#a553b001f496ac3689979841a04a7a862)#define ESP\_CPU\_GPIO\_IN3 31

[ 61](esp32c6-gpio-sigmap_8h.md#ad3d027b5581594073ea70b1955bb5733)#define ESP\_CPU\_GPIO\_OUT3 31

[ 62](esp32c6-gpio-sigmap_8h.md#a848b0915100b8e3b75089854d32910ee)#define ESP\_CPU\_GPIO\_IN4 32

[ 63](esp32c6-gpio-sigmap_8h.md#ac761dfb305a0e44a2447789680fd0ff9)#define ESP\_CPU\_GPIO\_OUT4 32

[ 64](esp32c6-gpio-sigmap_8h.md#abb64fd2a84298157b6071cc127a3c0ca)#define ESP\_CPU\_GPIO\_IN5 33

[ 65](esp32c6-gpio-sigmap_8h.md#add1c492755091bcdeafabe38cb65617b)#define ESP\_CPU\_GPIO\_OUT5 33

[ 66](esp32c6-gpio-sigmap_8h.md#a1695bafbd25037bcd848c5b58bdae422)#define ESP\_CPU\_GPIO\_IN6 34

[ 67](esp32c6-gpio-sigmap_8h.md#a929fc17e60b97257fef693b9ac1682ad)#define ESP\_CPU\_GPIO\_OUT6 34

[ 68](esp32c6-gpio-sigmap_8h.md#a10dc617c0b532ee5a8ae3d913a984007)#define ESP\_CPU\_GPIO\_IN7 35

[ 69](esp32c6-gpio-sigmap_8h.md#ad54946b60e601390d863b20dd1c13e32)#define ESP\_CPU\_GPIO\_OUT7 35

[ 70](esp32c6-gpio-sigmap_8h.md#ae39a7176534ecc35ed432e6b825cf1ee)#define ESP\_USB\_JTAG\_TCK 36

[ 71](esp32c6-gpio-sigmap_8h.md#aca9c05aba976c762c0ec5fa3603c76e1)#define ESP\_USB\_JTAG\_TMS 37

[ 72](esp32c6-gpio-sigmap_8h.md#ad92972ab672e468cc56c24733114d7db)#define ESP\_USB\_JTAG\_TDI 38

[ 73](esp32c6-gpio-sigmap_8h.md#a880f86e1452afee85e90589f74c17a4d)#define ESP\_USB\_JTAG\_TDO 39

[ 74](esp32c6-gpio-sigmap_8h.md#a7c2bcf73d61315a0d8c71d68173f9860)#define ESP\_USB\_EXTPHY\_VP 40

[ 75](esp32c6-gpio-sigmap_8h.md#a28f381128449aed0ae738516df39790c)#define ESP\_USB\_EXTPHY\_OEN 40

[ 76](esp32c6-gpio-sigmap_8h.md#aeaa130d2e220f2ebd073983921ad3679)#define ESP\_USB\_EXTPHY\_VM 41

[ 77](esp32c6-gpio-sigmap_8h.md#aedb10271abe4c1969eefbc0425681652)#define ESP\_USB\_EXTPHY\_SPEED 41

[ 78](esp32c6-gpio-sigmap_8h.md#a095d83d616afb08c4b06d82c4d907fee)#define ESP\_USB\_EXTPHY\_RCV 42

[ 79](esp32c6-gpio-sigmap_8h.md#a88c6a9f957332dac96360dd3f631e59b)#define ESP\_USB\_EXTPHY\_VPO 42

[ 80](esp32c6-gpio-sigmap_8h.md#abaeb7b2bb8208db93655b442293976aa)#define ESP\_USB\_EXTPHY\_VMO 43

[ 81](esp32c6-gpio-sigmap_8h.md#a301551d0d524f785b3d0e2c35bc81ce5)#define ESP\_USB\_EXTPHY\_SUSPND 44

[ 82](esp32c6-gpio-sigmap_8h.md#ab607ce367da34ab0f1bd7fa648273cf1)#define ESP\_I2CEXT0\_SCL\_IN 45

[ 83](esp32c6-gpio-sigmap_8h.md#a2144cc62df795547ccf2bbe3ee4c629f)#define ESP\_I2CEXT0\_SCL\_OUT 45

[ 84](esp32c6-gpio-sigmap_8h.md#afa7061c87135b9dabe5c54f5f4ce16e6)#define ESP\_I2CEXT0\_SDA\_IN 46

[ 85](esp32c6-gpio-sigmap_8h.md#aabf1378b0ad2028c36c3bb74c81d7049)#define ESP\_I2CEXT0\_SDA\_OUT 46

[ 86](esp32c6-gpio-sigmap_8h.md#af201b305da7adeecf46de78d69aab176)#define ESP\_PARL\_RX\_DATA0 47

[ 87](esp32c6-gpio-sigmap_8h.md#a9a2c5c2d86bb11fea57b3f443cea20f2)#define ESP\_PARL\_TX\_DATA0 47

[ 88](esp32c6-gpio-sigmap_8h.md#aab9f1503e5a9b5b4250bdc2d7716ccba)#define ESP\_PARL\_RX\_DATA1 48

[ 89](esp32c6-gpio-sigmap_8h.md#aa8d6d8a6c7d8852be84b8eee7e2d5298)#define ESP\_PARL\_TX\_DATA1 48

[ 90](esp32c6-gpio-sigmap_8h.md#a8317bb718beb926d845700237ee406f2)#define ESP\_PARL\_RX\_DATA2 49

[ 91](esp32c6-gpio-sigmap_8h.md#adaa9081a65eef7a6ae71ae27006c265f)#define ESP\_PARL\_TX\_DATA2 49

[ 92](esp32c6-gpio-sigmap_8h.md#a43d50c85e1acec92c85b64be6ad394c1)#define ESP\_PARL\_RX\_DATA3 50

[ 93](esp32c6-gpio-sigmap_8h.md#ab6b7e20f7f7cb058e417c0c44c7b1980)#define ESP\_PARL\_TX\_DATA3 50

[ 94](esp32c6-gpio-sigmap_8h.md#a671f7bc2fecc25e39455311f152449de)#define ESP\_PARL\_RX\_DATA4 51

[ 95](esp32c6-gpio-sigmap_8h.md#a224c79171493fa8e6bea88aa7d973418)#define ESP\_PARL\_TX\_DATA4 51

[ 96](esp32c6-gpio-sigmap_8h.md#a5ddd75868a46b4148d47950f592c957d)#define ESP\_PARL\_RX\_DATA5 52

[ 97](esp32c6-gpio-sigmap_8h.md#acaec50935260bb478a1fbbd92500e699)#define ESP\_PARL\_TX\_DATA5 52

[ 98](esp32c6-gpio-sigmap_8h.md#ad0486d571687d2333588ee992faabe68)#define ESP\_PARL\_RX\_DATA6 53

[ 99](esp32c6-gpio-sigmap_8h.md#ae20e6dfc6ceb3db062f5c6d1cb8c80a0)#define ESP\_PARL\_TX\_DATA6 53

[ 100](esp32c6-gpio-sigmap_8h.md#ae61c497a512e4c85dac4fccb91837144)#define ESP\_PARL\_RX\_DATA7 54

[ 101](esp32c6-gpio-sigmap_8h.md#ae4eba1f84896003a5f2365a1eb9fedd7)#define ESP\_PARL\_TX\_DATA7 54

[ 102](esp32c6-gpio-sigmap_8h.md#ae8215251915671f0a319536f1ce1be4b)#define ESP\_PARL\_RX\_DATA8 55

[ 103](esp32c6-gpio-sigmap_8h.md#a39cc4845a63bc8645da24951b583930b)#define ESP\_PARL\_TX\_DATA8 55

[ 104](esp32c6-gpio-sigmap_8h.md#ae8ef68bbf6034a2d88c521d11abd34fe)#define ESP\_PARL\_RX\_DATA9 56

[ 105](esp32c6-gpio-sigmap_8h.md#a554fa2ca7e29b925b9dec4bbc36e7eef)#define ESP\_PARL\_TX\_DATA9 56

[ 106](esp32c6-gpio-sigmap_8h.md#ac5ff5065b7e4d4e944175f0233bffad4)#define ESP\_PARL\_RX\_DATA10 57

[ 107](esp32c6-gpio-sigmap_8h.md#a07c711b42731234293169447c49d33e6)#define ESP\_PARL\_TX\_DATA10 57

[ 108](esp32c6-gpio-sigmap_8h.md#ab1bb7d79e0c0ddd06a1d1a7fa12a3a8b)#define ESP\_PARL\_RX\_DATA11 58

[ 109](esp32c6-gpio-sigmap_8h.md#a2fff12c555f9ea9220443fc3d49c8355)#define ESP\_PARL\_TX\_DATA11 58

[ 110](esp32c6-gpio-sigmap_8h.md#a63bafeea1cf67ce9cfe6ea61c231a457)#define ESP\_PARL\_RX\_DATA12 59

[ 111](esp32c6-gpio-sigmap_8h.md#a9c03392ed84dbab3d6299d4d109feb51)#define ESP\_PARL\_TX\_DATA12 59

[ 112](esp32c6-gpio-sigmap_8h.md#ad18b6f79222f2efebd9e36022a8783dd)#define ESP\_PARL\_RX\_DATA13 60

[ 113](esp32c6-gpio-sigmap_8h.md#a4454fc50212653bc0efa6f426f5ff4b5)#define ESP\_PARL\_TX\_DATA13 60

[ 114](esp32c6-gpio-sigmap_8h.md#ae6ee0185b85fc24425ce78145adf5d34)#define ESP\_PARL\_RX\_DATA14 61

[ 115](esp32c6-gpio-sigmap_8h.md#a04d2d762dedd9630de1423769776d41b)#define ESP\_PARL\_TX\_DATA14 61

[ 116](esp32c6-gpio-sigmap_8h.md#a8b586b1c2ea3a159e0e1756a0654cccd)#define ESP\_PARL\_RX\_DATA15 62

[ 117](esp32c6-gpio-sigmap_8h.md#a392956bc4bc11c591adf696b44a37b5f)#define ESP\_PARL\_TX\_DATA15 62

[ 118](esp32c6-gpio-sigmap_8h.md#ade88988460c131e8c6775794588b0eb8)#define ESP\_FSPICLK\_IN 63

[ 119](esp32c6-gpio-sigmap_8h.md#ab8c5397dc530f6326c3d10b31e59e168)#define ESP\_FSPICLK\_OUT 63

[ 120](esp32c6-gpio-sigmap_8h.md#ab603b7bf7d016e85653a5c3be5c01293)#define ESP\_FSPIQ\_IN 64

[ 121](esp32c6-gpio-sigmap_8h.md#a8b3ea6ad374fa010b46b48072fa87ccb)#define ESP\_FSPIQ\_OUT 64

[ 122](esp32c6-gpio-sigmap_8h.md#a7910521af840d42edd3c0a667cf90c5f)#define ESP\_FSPID\_IN 65

[ 123](esp32c6-gpio-sigmap_8h.md#a02bd34821e8a4bf0038b9af417ec161a)#define ESP\_FSPID\_OUT 65

[ 124](esp32c6-gpio-sigmap_8h.md#a60ff087a3d85a356d77f060a6698d00b)#define ESP\_FSPIHD\_IN 66

[ 125](esp32c6-gpio-sigmap_8h.md#ac71bc137b93bd6c0c8a1ebe24a70a613)#define ESP\_FSPIHD\_OUT 66

[ 126](esp32c6-gpio-sigmap_8h.md#a4d4c4a13b820cab6d94da8fe08120a2f)#define ESP\_FSPIWP\_IN 67

[ 127](esp32c6-gpio-sigmap_8h.md#a83c4f18d726984cc98caeea9b7677ca1)#define ESP\_FSPIWP\_OUT 67

[ 128](esp32c6-gpio-sigmap_8h.md#a96ca1328e76337d289f6e65faf33d75c)#define ESP\_FSPICS0\_IN 68

[ 129](esp32c6-gpio-sigmap_8h.md#ad1be1401b282275eaef46b9a598c6a40)#define ESP\_FSPICS0\_OUT 68

[ 130](esp32c6-gpio-sigmap_8h.md#ab1070767f3e3df17181d1a210469efac)#define ESP\_PARL\_RX\_CLK\_IN 69

[ 131](esp32c6-gpio-sigmap_8h.md#aac3529b76d29e57ad20500c9d1da23f3)#define ESP\_SDIO\_TOHOST\_INT\_OUT 69

[ 132](esp32c6-gpio-sigmap_8h.md#ab173d7fe92e586f414b1e1f514eb36c9)#define ESP\_PARL\_TX\_CLK\_IN 70

[ 133](esp32c6-gpio-sigmap_8h.md#a5eb62edb16f85cae370b6e10b5ab9cd9)#define ESP\_PARL\_TX\_CLK\_OUT 70

[ 134](esp32c6-gpio-sigmap_8h.md#ad9bae9b4884a356e465656d1ee8d61cd)#define ESP\_RMT\_SIG\_IN0 71

[ 135](esp32c6-gpio-sigmap_8h.md#a25343fbc20a0c542bcdc21cdfade867b)#define ESP\_RMT\_SIG\_OUT0 71

[ 136](esp32c6-gpio-sigmap_8h.md#a2f63c3092547a007e29d393dbb31e9e0)#define ESP\_MODEM\_DIAG0 71

[ 137](esp32c6-gpio-sigmap_8h.md#ab6c6293e6845ba4bf4d05b84102ffdcf)#define ESP\_RMT\_SIG\_IN1 72

[ 138](esp32c6-gpio-sigmap_8h.md#a6d082fb1c7397d784a3075108e0dea73)#define ESP\_RMT\_SIG\_OUT1 72

[ 139](esp32c6-gpio-sigmap_8h.md#a5e2292d0ce704c4c69f36602568be678)#define ESP\_MODEM\_DIAG1 72

[ 140](esp32c6-gpio-sigmap_8h.md#a5d9314d65cffc6a2af35b6d95e96d4a7)#define ESP\_TWAI0\_RX 73

[ 141](esp32c6-gpio-sigmap_8h.md#a861efcd37d8828dceffb156de3f1cced)#define ESP\_TWAI0\_TX 73

[ 142](esp32c6-gpio-sigmap_8h.md#ac6091fa0b02119d32c21628ca62e9809)#define ESP\_MODEM\_DIAG2 73

[ 143](esp32c6-gpio-sigmap_8h.md#a7b87a4c01e05eb8838865017f57e18ed)#define ESP\_TWAI0\_BUS\_OFF\_ON 74

[ 144](esp32c6-gpio-sigmap_8h.md#a83b3a33fe6c54216eb6b85ac99f57275)#define ESP\_MODEM\_DIAG3 74

[ 145](esp32c6-gpio-sigmap_8h.md#a9ae61611e2aa2467d37d2d39d3ceb7c0)#define ESP\_TWAI0\_CLKOUT 75

[ 146](esp32c6-gpio-sigmap_8h.md#a16257cbdc678b438612492133cb37706)#define ESP\_MODEM\_DIAG4 75

[ 147](esp32c6-gpio-sigmap_8h.md#afe3c57d9e86a34fe4509269529d25d07)#define ESP\_TWAI0\_STANDBY 76

[ 148](esp32c6-gpio-sigmap_8h.md#acdf070b0a479fdb921c49acbf85fef92)#define ESP\_MODEM\_DIAG5 76

[ 149](esp32c6-gpio-sigmap_8h.md#acb7f23161b4577b7897c3ddf6fc8c9ac)#define ESP\_TWAI1\_RX 77

[ 150](esp32c6-gpio-sigmap_8h.md#ae74556abcddfc37a6e98093cd485085e)#define ESP\_TWAI1\_TX 77

[ 151](esp32c6-gpio-sigmap_8h.md#a54cc19c89708ae84e573d4779b6882ac)#define ESP\_MODEM\_DIAG6 77

[ 152](esp32c6-gpio-sigmap_8h.md#a57865fd72f883b8525ced9d172608f88)#define ESP\_TWAI1\_BUS\_OFF\_ON 78

[ 153](esp32c6-gpio-sigmap_8h.md#a3872c2570b55af5dc912ef6767d8d1d5)#define ESP\_MODEM\_DIAG7 78

[ 154](esp32c6-gpio-sigmap_8h.md#abee49d2b8111da492779a84c19903b40)#define ESP\_TWAI1\_CLKOUT 79

[ 155](esp32c6-gpio-sigmap_8h.md#a7b68aee927fa44f0efc6e48801b5e68f)#define ESP\_MODEM\_DIAG8 79

[ 156](esp32c6-gpio-sigmap_8h.md#ac3dd15fd2c02c65488172f838a67df25)#define ESP\_TWAI1\_STANDBY 80

[ 157](esp32c6-gpio-sigmap_8h.md#a9efa61924e0577ab0e44b6d34aa72eaf)#define ESP\_MODEM\_DIAG9 80

[ 158](esp32c6-gpio-sigmap_8h.md#a39627b897d55107e1ecee725bd662ec2)#define ESP\_EXTERN\_PRIORITY\_I 81

[ 159](esp32c6-gpio-sigmap_8h.md#ab50a3b95442a89e070163c623a261578)#define ESP\_EXTERN\_PRIORITY\_O 81

[ 160](esp32c6-gpio-sigmap_8h.md#a533fcce69d815e97b58d7f1af1d4505c)#define ESP\_EXTERN\_ACTIVE\_I 82

[ 161](esp32c6-gpio-sigmap_8h.md#a198d1c07a648c5353e1c127e855d47c9)#define ESP\_EXTERN\_ACTIVE\_O 82

[ 162](esp32c6-gpio-sigmap_8h.md#ae59035f8269ccd564ba0d7b2b078b3ee)#define ESP\_GPIO\_SD0\_OUT 83

[ 163](esp32c6-gpio-sigmap_8h.md#a3fbed77581ed14fa077f314e812b9c36)#define ESP\_GPIO\_SD1\_OUT 84

[ 164](esp32c6-gpio-sigmap_8h.md#a2668d9083ce28563cc160fe1102e927d)#define ESP\_GPIO\_SD2\_OUT 85

[ 165](esp32c6-gpio-sigmap_8h.md#a9d34f616894f98d7175c41b4ba565f8d)#define ESP\_GPIO\_SD3\_OUT 86

[ 166](esp32c6-gpio-sigmap_8h.md#a60a3fe70a1bc5ba71cb46df782901087)#define ESP\_PWM0\_SYNC0\_IN 87

[ 167](esp32c6-gpio-sigmap_8h.md#a9397a79a46feab488c88552013790dfc)#define ESP\_PWM0\_OUT0A 87

[ 168](esp32c6-gpio-sigmap_8h.md#a1c27f723a8ccc46eca2c2edce7a7a650)#define ESP\_MODEM\_DIAG10 87

[ 169](esp32c6-gpio-sigmap_8h.md#aca616afbb64ed37982624503545a5a72)#define ESP\_PWM0\_SYNC1\_IN 88

[ 170](esp32c6-gpio-sigmap_8h.md#acb3badfaed73f7069ea23dde375db62a)#define ESP\_PWM0\_OUT0B 88

[ 171](esp32c6-gpio-sigmap_8h.md#a52a62190ade0aa92e72dbd193579690a)#define ESP\_MODEM\_DIAG11 88

[ 172](esp32c6-gpio-sigmap_8h.md#a2017681d630abc75e7298c12b86a62ce)#define ESP\_PWM0\_SYNC2\_IN 89

[ 173](esp32c6-gpio-sigmap_8h.md#ae52e5bd4be5563caeb9861267e41d947)#define ESP\_PWM0\_OUT1A 89

[ 174](esp32c6-gpio-sigmap_8h.md#a4f3534f7ad232f3dd5fefcbb110c0d3b)#define ESP\_MODEM\_DIAG12 89

[ 175](esp32c6-gpio-sigmap_8h.md#a4a503a957b2fd76f257534b80069caa2)#define ESP\_PWM0\_F0\_IN 90

[ 176](esp32c6-gpio-sigmap_8h.md#a9fa8e944ff2d960c141f8375c9aa0b0e)#define ESP\_PWM0\_OUT1B 90

[ 177](esp32c6-gpio-sigmap_8h.md#a19c695862a804d5725f2aeecb0b817cd)#define ESP\_MODEM\_DIAG13 90

[ 178](esp32c6-gpio-sigmap_8h.md#af536ae867a3d8bcb7644b48c346b4b50)#define ESP\_PWM0\_F1\_IN 91

[ 179](esp32c6-gpio-sigmap_8h.md#abf74a2a32a8c36431e2f21d6cd15a610)#define ESP\_PWM0\_OUT2A 91

[ 180](esp32c6-gpio-sigmap_8h.md#a67b153ab56537be68bb8eebd219d528e)#define ESP\_MODEM\_DIAG14 91

[ 181](esp32c6-gpio-sigmap_8h.md#a83f385e6b8a99314cc641083a203322b)#define ESP\_PWM0\_F2\_IN 92

[ 182](esp32c6-gpio-sigmap_8h.md#a563105deedf9f7ed6818ab9a8a8aecdc)#define ESP\_PWM0\_OUT2B 92

[ 183](esp32c6-gpio-sigmap_8h.md#af03c4a8fa544115297bcf03f280e3358)#define ESP\_MODEM\_DIAG15 92

[ 184](esp32c6-gpio-sigmap_8h.md#a421b59e20586b4f48b7e81bfa0ad4357)#define ESP\_PWM0\_CAP0\_IN 93

[ 185](esp32c6-gpio-sigmap_8h.md#aec2dfb198f69d923686404a0a6330833)#define ESP\_ANT\_SEL0 93

[ 186](esp32c6-gpio-sigmap_8h.md#aea7a8712f1502df47721258470ff5b48)#define ESP\_PWM0\_CAP1\_IN 94

[ 187](esp32c6-gpio-sigmap_8h.md#a15c080ea1e4c8e2db9f1640e9b8c4f0a)#define ESP\_ANT\_SEL1 94

[ 188](esp32c6-gpio-sigmap_8h.md#ab221240161be67a0f5af577494c8a5ad)#define ESP\_PWM0\_CAP2\_IN 95

[ 189](esp32c6-gpio-sigmap_8h.md#ae3042ff86ecc0f2e78ebe9477055e819)#define ESP\_ANT\_SEL2 95

[ 190](esp32c6-gpio-sigmap_8h.md#ab8e5cca4b9eb1a7bda7868ecd792c76d)#define ESP\_ANT\_SEL3 96

[ 191](esp32c6-gpio-sigmap_8h.md#a66890ae0c0e6a875c19099abb1918ca1)#define ESP\_SIG\_IN\_FUNC\_97 97

[ 192](esp32c6-gpio-sigmap_8h.md#a919b1b0e57d8785970c702fcd49d5563)#define ESP\_SIG\_IN\_FUNC97 97

[ 193](esp32c6-gpio-sigmap_8h.md#a848f955ed1b3b04d0a3d90f8c0acedec)#define ESP\_SIG\_IN\_FUNC\_98 98

[ 194](esp32c6-gpio-sigmap_8h.md#ae6043332289b10b68dc1d278681f3df1)#define ESP\_SIG\_IN\_FUNC98 98

[ 195](esp32c6-gpio-sigmap_8h.md#ab6956182e8d06463813e94843398a45f)#define ESP\_SIG\_IN\_FUNC\_99 99

[ 196](esp32c6-gpio-sigmap_8h.md#a11dcdffc24ff5d98c7c8d0f609a0c7b9)#define ESP\_SIG\_IN\_FUNC99 99

[ 197](esp32c6-gpio-sigmap_8h.md#a6684d495dfe99d0798f576018ffe0aba)#define ESP\_SIG\_IN\_FUNC\_100 100

[ 198](esp32c6-gpio-sigmap_8h.md#a33f1fad3bde9b252dfb3a291d600c019)#define ESP\_SIG\_IN\_FUNC100 100

[ 199](esp32c6-gpio-sigmap_8h.md#acf123456a5b9d94f370309ad39672e34)#define ESP\_PCNT\_SIG\_CH0\_IN0 101

[ 200](esp32c6-gpio-sigmap_8h.md#a44ade9179a7ea00586359a009799661d)#define ESP\_FSPICS1\_OUT 101

[ 201](esp32c6-gpio-sigmap_8h.md#ad9470b60b3e369abfc88c9f7545a7fd0)#define ESP\_MODEM\_DIAG16 101

[ 202](esp32c6-gpio-sigmap_8h.md#a800813b2c23f7e4bb23e032e0802a459)#define ESP\_PCNT\_SIG\_CH1\_IN0 102

[ 203](esp32c6-gpio-sigmap_8h.md#af991963f29c5b268a5f8fead8fd15348)#define ESP\_FSPICS2\_OUT 102

[ 204](esp32c6-gpio-sigmap_8h.md#a6c6ac8b6cb3f3e810057a185e59045c9)#define ESP\_MODEM\_DIAG17 102

[ 205](esp32c6-gpio-sigmap_8h.md#a7e3c939b0b32332a35f0bead0aa4a2a6)#define ESP\_PCNT\_CTRL\_CH0\_IN0 103

[ 206](esp32c6-gpio-sigmap_8h.md#a65d1170c5a68ac7f6a4457c3380ddfde)#define ESP\_FSPICS3\_OUT 103

[ 207](esp32c6-gpio-sigmap_8h.md#a9fcbb1d9a922b97ed8e2896042b7d20c)#define ESP\_MODEM\_DIAG18 103

[ 208](esp32c6-gpio-sigmap_8h.md#a88c5eb5c7f4169ce3e7f7056b42989a7)#define ESP\_PCNT\_CTRL\_CH1\_IN0 104

[ 209](esp32c6-gpio-sigmap_8h.md#a83dafe68703c701dcd07d7ff0aadad01)#define ESP\_FSPICS4\_OUT 104

[ 210](esp32c6-gpio-sigmap_8h.md#a9df3aaee6fdde85b29fd5449fea459d0)#define ESP\_MODEM\_DIAG19 104

[ 211](esp32c6-gpio-sigmap_8h.md#a99db3d1c4e07e11fc09a4024a54fcea6)#define ESP\_PCNT\_SIG\_CH0\_IN1 105

[ 212](esp32c6-gpio-sigmap_8h.md#ad8fab64bb220fd198a6cd931f4ea1e8e)#define ESP\_FSPICS5\_OUT 105

[ 213](esp32c6-gpio-sigmap_8h.md#a05fb209f68bced9280b3677579477b84)#define ESP\_MODEM\_DIAG20 105

[ 214](esp32c6-gpio-sigmap_8h.md#a730113779d69ca86b257060678f8cbec)#define ESP\_PCNT\_SIG\_CH1\_IN1 106

[ 215](esp32c6-gpio-sigmap_8h.md#a0f34d224d6a556b4fb39d1b219a2a3b2)#define ESP\_MODEM\_DIAG21 106

[ 216](esp32c6-gpio-sigmap_8h.md#a9ec8d490316b9f043fe5e9160a7cf7e0)#define ESP\_PCNT\_CTRL\_CH0\_IN1 107

[ 217](esp32c6-gpio-sigmap_8h.md#a879de7d116f35907ca915f52e172a87e)#define ESP\_MODEM\_DIAG22 107

[ 218](esp32c6-gpio-sigmap_8h.md#a0bbfffdef085eb6cedc3d1232766cb38)#define ESP\_PCNT\_CTRL\_CH1\_IN1 108

[ 219](esp32c6-gpio-sigmap_8h.md#a0b6177c482f983514e72f52b97d0cde4)#define ESP\_MODEM\_DIAG23 108

[ 220](esp32c6-gpio-sigmap_8h.md#a4f9e798a260fb6ac4c39262f20253244)#define ESP\_PCNT\_SIG\_CH0\_IN2 109

[ 221](esp32c6-gpio-sigmap_8h.md#a563e1402bd073956c4cb0885dc5c36f6)#define ESP\_MODEM\_DIAG24 109

[ 222](esp32c6-gpio-sigmap_8h.md#a38365b3f9a2b49ef2714c38d00d293c5)#define ESP\_PCNT\_SIG\_CH1\_IN2 110

[ 223](esp32c6-gpio-sigmap_8h.md#a68bbb9bc7afb5c46a0d835a47e06aaa7)#define ESP\_MODEM\_DIAG25 110

[ 224](esp32c6-gpio-sigmap_8h.md#a540cbfcd205911955effcc9814f9707c)#define ESP\_PCNT\_CTRL\_CH0\_IN2 111

[ 225](esp32c6-gpio-sigmap_8h.md#a1da463baa892c5c6869547bb2b1a2868)#define ESP\_MODEM\_DIAG26 111

[ 226](esp32c6-gpio-sigmap_8h.md#abf6c210e19582b06e3d6c546a009ef5b)#define ESP\_PCNT\_CTRL\_CH1\_IN2 112

[ 227](esp32c6-gpio-sigmap_8h.md#a13c42ca4cf26cd2970704c00980be6f4)#define ESP\_MODEM\_DIAG27 112

[ 228](esp32c6-gpio-sigmap_8h.md#acd8d20d89508b532a4e2749499263de3)#define ESP\_PCNT\_SIG\_CH0\_IN3 113

[ 229](esp32c6-gpio-sigmap_8h.md#a313b0ba2004de882f409442d50af0e46)#define ESP\_MODEM\_DIAG28 113

[ 230](esp32c6-gpio-sigmap_8h.md#ac54a606ee7096db15cdb9453b04ac72d)#define ESP\_PCNT\_SIG\_CH1\_IN3 114

[ 231](esp32c6-gpio-sigmap_8h.md#a5f440c922a53085bb7b28f469c2a14b0)#define ESP\_SPICLK\_OUT 114

[ 232](esp32c6-gpio-sigmap_8h.md#aead76bffdf1314cb8860f00fbc9e3d92)#define ESP\_MODEM\_DIAG29 114

[ 233](esp32c6-gpio-sigmap_8h.md#a96e8bd4584ab671a1b0c3f0adb440943)#define ESP\_PCNT\_CTRL\_CH0\_IN3 115

[ 234](esp32c6-gpio-sigmap_8h.md#a5d97c07ba0d8cda594d52310e90fa6a4)#define ESP\_SPICS0\_OUT 115

[ 235](esp32c6-gpio-sigmap_8h.md#a3cbbd2fcbc7a6bd7471889b8a960c404)#define ESP\_MODEM\_DIAG30 115

[ 236](esp32c6-gpio-sigmap_8h.md#a0a926d350fc11d737b545c53b3ba1671)#define ESP\_PCNT\_CTRL\_CH1\_IN3 116

[ 237](esp32c6-gpio-sigmap_8h.md#aa4a67a38b97a3d466783c0617aa6a0c8)#define ESP\_SPICS1\_OUT 116

[ 238](esp32c6-gpio-sigmap_8h.md#a36529137784bbb014406090cb1d7a1bd)#define ESP\_MODEM\_DIAG31 116

[ 239](esp32c6-gpio-sigmap_8h.md#a2af8dc70a06105740ae181a616186624)#define ESP\_GPIO\_EVENT\_MATRIX\_IN0 117

[ 240](esp32c6-gpio-sigmap_8h.md#aeee7dc180a750016e7711282b252ccf6)#define ESP\_GPIO\_TASK\_MATRIX\_OUT0 117

[ 241](esp32c6-gpio-sigmap_8h.md#a7a2ce6558a5368d1fc0325ce37487d1a)#define ESP\_GPIO\_EVENT\_MATRIX\_IN1 118

[ 242](esp32c6-gpio-sigmap_8h.md#a4ce0ef64cebc11e961d73fc58d8bb954)#define ESP\_GPIO\_TASK\_MATRIX\_OUT1 118

[ 243](esp32c6-gpio-sigmap_8h.md#a2ae077cc87f156e9545eca4a091890e3)#define ESP\_GPIO\_EVENT\_MATRIX\_IN2 119

[ 244](esp32c6-gpio-sigmap_8h.md#a0ac11865f0be99e81bebeb7dfbe1424b)#define ESP\_GPIO\_TASK\_MATRIX\_OUT2 119

[ 245](esp32c6-gpio-sigmap_8h.md#a97d8c86a5d7ba47196816c7d04ef7efb)#define ESP\_GPIO\_EVENT\_MATRIX\_IN3 120

[ 246](esp32c6-gpio-sigmap_8h.md#a165323f111794aeff16e7073501ff16e)#define ESP\_GPIO\_TASK\_MATRIX\_OUT3 120

[ 247](esp32c6-gpio-sigmap_8h.md#aec51ff955c6be50e529affc87ec9d5cb)#define ESP\_SPIQ\_IN 121

[ 248](esp32c6-gpio-sigmap_8h.md#a5816deeca8853397a830a8eb251704ee)#define ESP\_SPIQ\_OUT 121

[ 249](esp32c6-gpio-sigmap_8h.md#a26c603fd58dbd7526d2be3bb3e37758a)#define ESP\_SPID\_IN 122

[ 250](esp32c6-gpio-sigmap_8h.md#af81b2fc65b68ed2238ab3367a8731102)#define ESP\_SPID\_OUT 122

[ 251](esp32c6-gpio-sigmap_8h.md#a49783f877b666aff9362cf605590b991)#define ESP\_SPIHD\_IN 123

[ 252](esp32c6-gpio-sigmap_8h.md#a8851b5256482790f3304efecafc13afd)#define ESP\_SPIHD\_OUT 123

[ 253](esp32c6-gpio-sigmap_8h.md#aa74adc2812d9c6bd143c679fa4d9ca8d)#define ESP\_SPIWP\_IN 124

[ 254](esp32c6-gpio-sigmap_8h.md#a470408f8102937dc017336e320e6147b)#define ESP\_SPIWP\_OUT 124

[ 255](esp32c6-gpio-sigmap_8h.md#a12a2380f8bcbf158e7c114b7dc1701a5)#define ESP\_CLK\_OUT\_OUT1 125

[ 256](esp32c6-gpio-sigmap_8h.md#adf7a9c85596f3a536ddb603d3218cee2)#define ESP\_CLK\_OUT\_OUT2 126

[ 257](esp32c6-gpio-sigmap_8h.md#af421f62c654ecca5136b7b526f168377)#define ESP\_CLK\_OUT\_OUT3 127

[ 258](esp32c6-gpio-sigmap_8h.md#a645411759ffdc63f51f2cd42632d2720)#define ESP\_SIG\_GPIO\_OUT 128

[ 259](esp32c6-gpio-sigmap_8h.md#afe5c166b887709cdd27bd37df85c45b9)#define ESP\_GPIO\_MAP\_DATE 0x2201120

260

261#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C6\_GPIO\_SIGMAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32c6-gpio-sigmap.h](esp32c6-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
