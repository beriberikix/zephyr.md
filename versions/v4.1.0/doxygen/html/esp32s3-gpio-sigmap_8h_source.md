---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp32s3-gpio-sigmap_8h_source.html
original_path: doxygen/html/esp32s3-gpio-sigmap_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s3-gpio-sigmap.h

[Go to the documentation of this file.](esp32s3-gpio-sigmap_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32S3\_GPIO\_SIGMAP\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32S3\_GPIO\_SIGMAP\_H\_

9

[ 10](esp32s3-gpio-sigmap_8h.md#af80260535bc3aee44c28c972a29483e0)#define ESP\_NOSIG ESP\_SIG\_INVAL

11

[ 12](esp32s3-gpio-sigmap_8h.md#aec51ff955c6be50e529affc87ec9d5cb)#define ESP\_SPIQ\_IN 0

[ 13](esp32s3-gpio-sigmap_8h.md#a5816deeca8853397a830a8eb251704ee)#define ESP\_SPIQ\_OUT 0

[ 14](esp32s3-gpio-sigmap_8h.md#a26c603fd58dbd7526d2be3bb3e37758a)#define ESP\_SPID\_IN 1

[ 15](esp32s3-gpio-sigmap_8h.md#af81b2fc65b68ed2238ab3367a8731102)#define ESP\_SPID\_OUT 1

[ 16](esp32s3-gpio-sigmap_8h.md#a49783f877b666aff9362cf605590b991)#define ESP\_SPIHD\_IN 2

[ 17](esp32s3-gpio-sigmap_8h.md#a8851b5256482790f3304efecafc13afd)#define ESP\_SPIHD\_OUT 2

[ 18](esp32s3-gpio-sigmap_8h.md#aa74adc2812d9c6bd143c679fa4d9ca8d)#define ESP\_SPIWP\_IN 3

[ 19](esp32s3-gpio-sigmap_8h.md#a470408f8102937dc017336e320e6147b)#define ESP\_SPIWP\_OUT 3

[ 20](esp32s3-gpio-sigmap_8h.md#a5f440c922a53085bb7b28f469c2a14b0)#define ESP\_SPICLK\_OUT 4

[ 21](esp32s3-gpio-sigmap_8h.md#a5d97c07ba0d8cda594d52310e90fa6a4)#define ESP\_SPICS0\_OUT 5

[ 22](esp32s3-gpio-sigmap_8h.md#aa4a67a38b97a3d466783c0617aa6a0c8)#define ESP\_SPICS1\_OUT 6

[ 23](esp32s3-gpio-sigmap_8h.md#ade124a5a82af0f49b122b32d69ee8d04)#define ESP\_SPID4\_IN 7

[ 24](esp32s3-gpio-sigmap_8h.md#a9bd0335c81e6828a5da77af387fbe845)#define ESP\_SPID4\_OUT 7

[ 25](esp32s3-gpio-sigmap_8h.md#ae8fa56cbc73756ff3895a937ab1374c2)#define ESP\_SPID5\_IN 8

[ 26](esp32s3-gpio-sigmap_8h.md#a61317dd1e2daf50f35240fd561180628)#define ESP\_SPID5\_OUT 8

[ 27](esp32s3-gpio-sigmap_8h.md#a2d850da0ce491f0049b9920cde48907e)#define ESP\_SPID6\_IN 9

[ 28](esp32s3-gpio-sigmap_8h.md#a918e6203f9d52d8d2606616a938faea8)#define ESP\_SPID6\_OUT 9

[ 29](esp32s3-gpio-sigmap_8h.md#a78073d0d570a71824e00bebe4bbd97d1)#define ESP\_SPID7\_IN 10

[ 30](esp32s3-gpio-sigmap_8h.md#a0802cd16128bd289444b670a827d0d31)#define ESP\_SPID7\_OUT 10

[ 31](esp32s3-gpio-sigmap_8h.md#ae891264c3a0289dad5851d44b18707d2)#define ESP\_SPIDQS\_IN 11

[ 32](esp32s3-gpio-sigmap_8h.md#a88309f7b84da7f6e461139ad137cfb97)#define ESP\_SPIDQS\_OUT 11

[ 33](esp32s3-gpio-sigmap_8h.md#aca502efa55ce2286dc9eba28192681fd)#define ESP\_U0RXD\_IN 12

[ 34](esp32s3-gpio-sigmap_8h.md#af1e58fb8e7ef86a92171eca7bb1671af)#define ESP\_U0TXD\_OUT 12

[ 35](esp32s3-gpio-sigmap_8h.md#a530d7a918a97cd1fff1acf2f90edd4ca)#define ESP\_U0CTS\_IN 13

[ 36](esp32s3-gpio-sigmap_8h.md#a4257bbc044af6ea3612313e3a0b7e7c9)#define ESP\_U0RTS\_OUT 13

[ 37](esp32s3-gpio-sigmap_8h.md#a53e3a4557a4eb1f7f98250abef03c02a)#define ESP\_U0DSR\_IN 14

[ 38](esp32s3-gpio-sigmap_8h.md#acc8716af947169c9f167bdf215c5314c)#define ESP\_U0DTR\_OUT 14

[ 39](esp32s3-gpio-sigmap_8h.md#a2293e0646e0ad2f76d62f76425ae6770)#define ESP\_U1RXD\_IN 15

[ 40](esp32s3-gpio-sigmap_8h.md#a6053b38147e28e3a7479b38e7d195136)#define ESP\_U1TXD\_OUT 15

[ 41](esp32s3-gpio-sigmap_8h.md#a3c005e616da21a058960d6aed79427b3)#define ESP\_U1CTS\_IN 16

[ 42](esp32s3-gpio-sigmap_8h.md#a8f6399745566bd5caa2020e4dcb2bb3b)#define ESP\_U1RTS\_OUT 16

[ 43](esp32s3-gpio-sigmap_8h.md#a5f29b138691540598d0b977dc4bd5971)#define ESP\_U1DSR\_IN 17

[ 44](esp32s3-gpio-sigmap_8h.md#a1f7df042d40ec6f20b559ef6778d7497)#define ESP\_U1DTR\_OUT 17

[ 45](esp32s3-gpio-sigmap_8h.md#abe46ead057c2b66d500ef07e8a84fe0f)#define ESP\_U2RXD\_IN 18

[ 46](esp32s3-gpio-sigmap_8h.md#a20baac10eb4b76603580e1ea7065213a)#define ESP\_U2TXD\_OUT 18

[ 47](esp32s3-gpio-sigmap_8h.md#a735a482aa723130ccb408f0fb7596a0a)#define ESP\_U2CTS\_IN 19

[ 48](esp32s3-gpio-sigmap_8h.md#a174b50e35d961ded056cea3848110b20)#define ESP\_U2RTS\_OUT 19

[ 49](esp32s3-gpio-sigmap_8h.md#a70d4f834bfd182c138257e36a4b04096)#define ESP\_U2DSR\_IN 20

[ 50](esp32s3-gpio-sigmap_8h.md#a783f6ee9ad46dfd9e34d1473b1e2ad9b)#define ESP\_U2DTR\_OUT 20

[ 51](esp32s3-gpio-sigmap_8h.md#af00f358d0012d5a4e85a0610f9da2ace)#define ESP\_I2S1\_MCLK\_IN 21

[ 52](esp32s3-gpio-sigmap_8h.md#aeeb2b00d8b3172832532d96b2282d4d2)#define ESP\_I2S1\_MCLK\_OUT 21

[ 53](esp32s3-gpio-sigmap_8h.md#af0b9626d6b7cfd5b5c42a8127897d565)#define ESP\_I2S0O\_BCK\_IN 22

[ 54](esp32s3-gpio-sigmap_8h.md#a2e76c532bd75a6af4790b30f58c4b8e9)#define ESP\_I2S0O\_BCK\_OUT 22

[ 55](esp32s3-gpio-sigmap_8h.md#a329858f11621f706f0a933886246e177)#define ESP\_I2S0\_MCLK\_IN 23

[ 56](esp32s3-gpio-sigmap_8h.md#acd2f3e9c21da61b98fdc86b8a264d9fd)#define ESP\_I2S0\_MCLK\_OUT 23

[ 57](esp32s3-gpio-sigmap_8h.md#aad13d05d8d50227859d484deaaf6e34b)#define ESP\_I2S0O\_WS\_IN 24

[ 58](esp32s3-gpio-sigmap_8h.md#a78693c10e4ac17973e7ac12c1bdf8c97)#define ESP\_I2S0O\_WS\_OUT 24

[ 59](esp32s3-gpio-sigmap_8h.md#a8e920eb744585bdec4b5ca8c6a6ec7b6)#define ESP\_I2S0I\_SD\_IN 25

[ 60](esp32s3-gpio-sigmap_8h.md#a9e263a786610ffa2b60051a03188b67b)#define ESP\_I2S0O\_SD\_OUT 25

[ 61](esp32s3-gpio-sigmap_8h.md#a67905afbcda699d20d8a05a8a66411af)#define ESP\_I2S0I\_BCK\_IN 26

[ 62](esp32s3-gpio-sigmap_8h.md#abe571a9bad2c0e95049afd8e67c8d158)#define ESP\_I2S0I\_BCK\_OUT 26

[ 63](esp32s3-gpio-sigmap_8h.md#a4236f62ac75d5f2d56f7b1cc941d7509)#define ESP\_I2S0I\_WS\_IN 27

[ 64](esp32s3-gpio-sigmap_8h.md#af039bdc8eec9ec95d3ed2bbebabb22cb)#define ESP\_I2S0I\_WS\_OUT 27

[ 65](esp32s3-gpio-sigmap_8h.md#afffede35b0effa00a9d6e1077ac4aaa2)#define ESP\_I2S1O\_BCK\_IN 28

[ 66](esp32s3-gpio-sigmap_8h.md#afcd05d2cf345dcf816068b0b89ac5a72)#define ESP\_I2S1O\_BCK\_OUT 28

[ 67](esp32s3-gpio-sigmap_8h.md#a7ac95a35ee6001c340cddd1424f3fa5e)#define ESP\_I2S1O\_WS\_IN 29

[ 68](esp32s3-gpio-sigmap_8h.md#a84485bdfe1661269506f7ef1f70f4a87)#define ESP\_I2S1O\_WS\_OUT 29

[ 69](esp32s3-gpio-sigmap_8h.md#a854ae55e42905b005332084451ddf0ba)#define ESP\_I2S1I\_SD\_IN 30

[ 70](esp32s3-gpio-sigmap_8h.md#aa97d280d714ad4284f617df4453bdcf6)#define ESP\_I2S1O\_SD\_OUT 30

[ 71](esp32s3-gpio-sigmap_8h.md#a537fd0715c03fd03d914d72d01191b9a)#define ESP\_I2S1I\_BCK\_IN 31

[ 72](esp32s3-gpio-sigmap_8h.md#a93d4d6602af3ba29121fef124145f4a5)#define ESP\_I2S1I\_BCK\_OUT 31

[ 73](esp32s3-gpio-sigmap_8h.md#a90b7c81877f6ab8ec1af498db7b8dc0e)#define ESP\_I2S1I\_WS\_IN 32

[ 74](esp32s3-gpio-sigmap_8h.md#a1ed428a9dd21d57a7311c24f192e032e)#define ESP\_I2S1I\_WS\_OUT 32

[ 75](esp32s3-gpio-sigmap_8h.md#acf123456a5b9d94f370309ad39672e34)#define ESP\_PCNT\_SIG\_CH0\_IN0 33

[ 76](esp32s3-gpio-sigmap_8h.md#adf2824b1611032a81fe7b3c41253c0d8)#define ESP\_GPIO\_WLAN\_PRIO 33

[ 77](esp32s3-gpio-sigmap_8h.md#a800813b2c23f7e4bb23e032e0802a459)#define ESP\_PCNT\_SIG\_CH1\_IN0 34

[ 78](esp32s3-gpio-sigmap_8h.md#af675ca03172d2dcee1e19ccb5236e087)#define ESP\_GPIO\_WLAN\_ACTIVE 34

[ 79](esp32s3-gpio-sigmap_8h.md#a7e3c939b0b32332a35f0bead0aa4a2a6)#define ESP\_PCNT\_CTRL\_CH0\_IN0 35

[ 80](esp32s3-gpio-sigmap_8h.md#a304bc90cc758f90f6675fea611ab0cfe)#define ESP\_BB\_DIAG0 35

[ 81](esp32s3-gpio-sigmap_8h.md#a88c5eb5c7f4169ce3e7f7056b42989a7)#define ESP\_PCNT\_CTRL\_CH1\_IN0 36

[ 82](esp32s3-gpio-sigmap_8h.md#ad236bf991329914d59c194ff9003974a)#define ESP\_BB\_DIAG1 36

[ 83](esp32s3-gpio-sigmap_8h.md#a99db3d1c4e07e11fc09a4024a54fcea6)#define ESP\_PCNT\_SIG\_CH0\_IN1 37

[ 84](esp32s3-gpio-sigmap_8h.md#a26c20261a5e2f4293b81c802a0a33b19)#define ESP\_BB\_DIAG2 37

[ 85](esp32s3-gpio-sigmap_8h.md#a730113779d69ca86b257060678f8cbec)#define ESP\_PCNT\_SIG\_CH1\_IN1 38

[ 86](esp32s3-gpio-sigmap_8h.md#a5124ef75b703e7805bccd8c93828faae)#define ESP\_BB\_DIAG3 38

[ 87](esp32s3-gpio-sigmap_8h.md#a9ec8d490316b9f043fe5e9160a7cf7e0)#define ESP\_PCNT\_CTRL\_CH0\_IN1 39

[ 88](esp32s3-gpio-sigmap_8h.md#aebd2c37b71d18967bd394b32c820647f)#define ESP\_BB\_DIAG4 39

[ 89](esp32s3-gpio-sigmap_8h.md#a0bbfffdef085eb6cedc3d1232766cb38)#define ESP\_PCNT\_CTRL\_CH1\_IN1 40

[ 90](esp32s3-gpio-sigmap_8h.md#ace166b18a74fb8a42f876d1aa7cfb059)#define ESP\_BB\_DIAG5 40

[ 91](esp32s3-gpio-sigmap_8h.md#a4f9e798a260fb6ac4c39262f20253244)#define ESP\_PCNT\_SIG\_CH0\_IN2 41

[ 92](esp32s3-gpio-sigmap_8h.md#ad5685b19c170cc428cea0ee91f9155b0)#define ESP\_BB\_DIAG6 41

[ 93](esp32s3-gpio-sigmap_8h.md#a38365b3f9a2b49ef2714c38d00d293c5)#define ESP\_PCNT\_SIG\_CH1\_IN2 42

[ 94](esp32s3-gpio-sigmap_8h.md#aedf32208932dfe4471f6a5a7feb652f8)#define ESP\_BB\_DIAG7 42

[ 95](esp32s3-gpio-sigmap_8h.md#a540cbfcd205911955effcc9814f9707c)#define ESP\_PCNT\_CTRL\_CH0\_IN2 43

[ 96](esp32s3-gpio-sigmap_8h.md#a126e2108473183890c6a2e148f8fd2c7)#define ESP\_BB\_DIAG8 43

[ 97](esp32s3-gpio-sigmap_8h.md#abf6c210e19582b06e3d6c546a009ef5b)#define ESP\_PCNT\_CTRL\_CH1\_IN2 44

[ 98](esp32s3-gpio-sigmap_8h.md#a75b60b1b4d53e6fca02b3a4f14ea530e)#define ESP\_BB\_DIAG9 44

[ 99](esp32s3-gpio-sigmap_8h.md#acd8d20d89508b532a4e2749499263de3)#define ESP\_PCNT\_SIG\_CH0\_IN3 45

[ 100](esp32s3-gpio-sigmap_8h.md#aed67caee00b7ceaaaa33b2917aba60f2)#define ESP\_BB\_DIAG10 45

[ 101](esp32s3-gpio-sigmap_8h.md#ac54a606ee7096db15cdb9453b04ac72d)#define ESP\_PCNT\_SIG\_CH1\_IN3 46

[ 102](esp32s3-gpio-sigmap_8h.md#aef4bb5d62b93dfc3f2834404b6945b90)#define ESP\_BB\_DIAG11 46

[ 103](esp32s3-gpio-sigmap_8h.md#a96e8bd4584ab671a1b0c3f0adb440943)#define ESP\_PCNT\_CTRL\_CH0\_IN3 47

[ 104](esp32s3-gpio-sigmap_8h.md#acc6cd70ce139a5639022bec896a3ba5e)#define ESP\_BB\_DIAG12 47

[ 105](esp32s3-gpio-sigmap_8h.md#a0a926d350fc11d737b545c53b3ba1671)#define ESP\_PCNT\_CTRL\_CH1\_IN3 48

[ 106](esp32s3-gpio-sigmap_8h.md#afa72089303bf662a4efc8c068b157f0d)#define ESP\_BB\_DIAG13 48

[ 107](esp32s3-gpio-sigmap_8h.md#a47d854bfae0f88dc023613e61e6be551)#define ESP\_GPIO\_BT\_ACTIVE 49

[ 108](esp32s3-gpio-sigmap_8h.md#a4ef00458e2547f7141741191b92854d8)#define ESP\_BB\_DIAG14 49

[ 109](esp32s3-gpio-sigmap_8h.md#ab8d0a9090c64518af59274603f035042)#define ESP\_GPIO\_BT\_PRIORITY 50

[ 110](esp32s3-gpio-sigmap_8h.md#aed7c06883c6a69303a341454aff409ed)#define ESP\_BB\_DIAG15 50

[ 111](esp32s3-gpio-sigmap_8h.md#a9ae165cac1d30c38270f8747caa18f00)#define ESP\_I2S0I\_SD1\_IN 51

[ 112](esp32s3-gpio-sigmap_8h.md#a1acc29dd7c0517c30299e71c1a6ce7fa)#define ESP\_BB\_DIAG16 51

[ 113](esp32s3-gpio-sigmap_8h.md#a5e4fdb79d8fefa835118c21fe6b05cb5)#define ESP\_I2S0I\_SD2\_IN 52

[ 114](esp32s3-gpio-sigmap_8h.md#a9abbf3178088e44d984b088f53c25ab1)#define ESP\_BB\_DIAG17 52

[ 115](esp32s3-gpio-sigmap_8h.md#a39f410a33a8ddc30a37de7d0b5ff821d)#define ESP\_I2S0I\_SD3\_IN 53

[ 116](esp32s3-gpio-sigmap_8h.md#af75798fba81841339510ecc5f94e542e)#define ESP\_BB\_DIAG18 53

[ 117](esp32s3-gpio-sigmap_8h.md#ae07a10a5b5f791d98034a0ffcaa0a5c1)#define ESP\_CORE1\_GPIO\_IN7 54

[ 118](esp32s3-gpio-sigmap_8h.md#ac9744120f941e282f182bf4b16b31a34)#define ESP\_CORE1\_GPIO\_OUT7 54

[ 119](esp32s3-gpio-sigmap_8h.md#a7c2bcf73d61315a0d8c71d68173f9860)#define ESP\_USB\_EXTPHY\_VP 55

[ 120](esp32s3-gpio-sigmap_8h.md#a28f381128449aed0ae738516df39790c)#define ESP\_USB\_EXTPHY\_OEN 55

[ 121](esp32s3-gpio-sigmap_8h.md#aeaa130d2e220f2ebd073983921ad3679)#define ESP\_USB\_EXTPHY\_VM 56

[ 122](esp32s3-gpio-sigmap_8h.md#aedb10271abe4c1969eefbc0425681652)#define ESP\_USB\_EXTPHY\_SPEED 56

[ 123](esp32s3-gpio-sigmap_8h.md#a095d83d616afb08c4b06d82c4d907fee)#define ESP\_USB\_EXTPHY\_RCV 57

[ 124](esp32s3-gpio-sigmap_8h.md#a88c6a9f957332dac96360dd3f631e59b)#define ESP\_USB\_EXTPHY\_VPO 57

[ 125](esp32s3-gpio-sigmap_8h.md#a22582585ff59bc29c3e011c4d869b1b8)#define ESP\_USB\_OTG\_IDDIG\_IN 58

[ 126](esp32s3-gpio-sigmap_8h.md#abaeb7b2bb8208db93655b442293976aa)#define ESP\_USB\_EXTPHY\_VMO 58

[ 127](esp32s3-gpio-sigmap_8h.md#a4d0c408fedb6ba35298c1398eccaa4e2)#define ESP\_USB\_OTG\_AVALID\_IN 59

[ 128](esp32s3-gpio-sigmap_8h.md#a301551d0d524f785b3d0e2c35bc81ce5)#define ESP\_USB\_EXTPHY\_SUSPND 59

[ 129](esp32s3-gpio-sigmap_8h.md#aaafaee30be8e3fed2eb1117ce381dd37)#define ESP\_USB\_SRP\_BVALID\_IN 60

[ 130](esp32s3-gpio-sigmap_8h.md#ab7335ddb7641fb62231adf289a7a74a8)#define ESP\_USB\_OTG\_IDPULLUP 60

[ 131](esp32s3-gpio-sigmap_8h.md#a4e3bd2577c74b857a74f1c367a235bad)#define ESP\_USB\_OTG\_VBUSVALID\_IN 61

[ 132](esp32s3-gpio-sigmap_8h.md#a04c49eae7bb25687d76a810ab6468353)#define ESP\_USB\_OTG\_DPPULLDOWN 61

[ 133](esp32s3-gpio-sigmap_8h.md#a8601c4fb546ff39782c0fbb14e68bfbd)#define ESP\_USB\_SRP\_SESSEND\_IN 62

[ 134](esp32s3-gpio-sigmap_8h.md#a852717f88ddb411d5b0dc49a3be83282)#define ESP\_USB\_OTG\_DMPULLDOWN 62

[ 135](esp32s3-gpio-sigmap_8h.md#a6f79de1e3bbc3758362426eecad93d3d)#define ESP\_USB\_OTG\_DRVVBUS 63

[ 136](esp32s3-gpio-sigmap_8h.md#a49b28cbc76c15cd1395f3b2e1a6ac4d9)#define ESP\_USB\_SRP\_CHRGVBUS 64

[ 137](esp32s3-gpio-sigmap_8h.md#a30f3abf038b27fa16a82bdf413eff14c)#define ESP\_USB\_SRP\_DISCHRGVBUS 65

[ 138](esp32s3-gpio-sigmap_8h.md#a0bff2051090f5eaea7edd6e9b4725a3c)#define ESP\_SPI3\_CLK\_IN 66

[ 139](esp32s3-gpio-sigmap_8h.md#a02cc6c3ead85cf6c4837f05807103521)#define ESP\_SPI3\_CLK\_OUT 66

[ 140](esp32s3-gpio-sigmap_8h.md#a05a9a2e5983b7895ca1fb05e5cd34709)#define ESP\_SPI3\_Q\_IN 67

[ 141](esp32s3-gpio-sigmap_8h.md#a6656c910c99e3de854064f4df24faa2d)#define ESP\_SPI3\_Q\_OUT 67

[ 142](esp32s3-gpio-sigmap_8h.md#ae7cf1730786ba95580b91b00066d3e25)#define ESP\_SPI3\_D\_IN 68

[ 143](esp32s3-gpio-sigmap_8h.md#aff4a1289beb94c9e23d7c1dd13d71d83)#define ESP\_SPI3\_D\_OUT 68

[ 144](esp32s3-gpio-sigmap_8h.md#a84dd16599428fb4c3da12c221219af40)#define ESP\_SPI3\_HD\_IN 69

[ 145](esp32s3-gpio-sigmap_8h.md#a73457a024aa63c16c2a5ef8ada2bf8b2)#define ESP\_SPI3\_HD\_OUT 69

[ 146](esp32s3-gpio-sigmap_8h.md#ae5ef053fe616dfb189a1a5bf28313647)#define ESP\_SPI3\_WP\_IN 70

[ 147](esp32s3-gpio-sigmap_8h.md#ab3c345085fafd95b7bd2f83d14a5317c)#define ESP\_SPI3\_WP\_OUT 70

[ 148](esp32s3-gpio-sigmap_8h.md#a485eded26f1b4bd7f03d916dcd4b0753)#define ESP\_SPI3\_CS0\_IN 71

[ 149](esp32s3-gpio-sigmap_8h.md#a8fc990a73f8fdc8d1004b3dad676a224)#define ESP\_SPI3\_CS0\_OUT 71

[ 150](esp32s3-gpio-sigmap_8h.md#a7f06d2db560a8cd511c9189cd6ed8980)#define ESP\_SPI3\_CS1\_OUT 72

[ 151](esp32s3-gpio-sigmap_8h.md#ae49b4527d8fbd0f5c8e3edc72704c54a)#define ESP\_EXT\_ADC\_START 73

[ 152](esp32s3-gpio-sigmap_8h.md#a62dfcd88747c61acb53dc85c1751f1d3)#define ESP\_LEDC\_LS\_SIG\_OUT0 73

[ 153](esp32s3-gpio-sigmap_8h.md#a5cad9206cfeea93b42e5456228c7d580)#define ESP\_LEDC\_LS\_SIG\_OUT1 74

[ 154](esp32s3-gpio-sigmap_8h.md#ab408070e7c700805db165c3876b6c588)#define ESP\_LEDC\_LS\_SIG\_OUT2 75

[ 155](esp32s3-gpio-sigmap_8h.md#a438aee217c6c94a2962a3d98935b5717)#define ESP\_LEDC\_LS\_SIG\_OUT3 76

[ 156](esp32s3-gpio-sigmap_8h.md#ada93dcffffc15362be4b7432a8033559)#define ESP\_LEDC\_LS\_SIG\_OUT4 77

[ 157](esp32s3-gpio-sigmap_8h.md#a34fc029ec45756ca7064580f57db1cc7)#define ESP\_LEDC\_LS\_SIG\_OUT5 78

[ 158](esp32s3-gpio-sigmap_8h.md#a28b01adea7e0bcc8b76fe05d58c1cbd0)#define ESP\_LEDC\_LS\_SIG\_OUT6 79

[ 159](esp32s3-gpio-sigmap_8h.md#a2ea140f2da1a15b24dcaa3592909ca35)#define ESP\_LEDC\_LS\_SIG\_OUT7 80

[ 160](esp32s3-gpio-sigmap_8h.md#ad9bae9b4884a356e465656d1ee8d61cd)#define ESP\_RMT\_SIG\_IN0 81

[ 161](esp32s3-gpio-sigmap_8h.md#a25343fbc20a0c542bcdc21cdfade867b)#define ESP\_RMT\_SIG\_OUT0 81

[ 162](esp32s3-gpio-sigmap_8h.md#ab6c6293e6845ba4bf4d05b84102ffdcf)#define ESP\_RMT\_SIG\_IN1 82

[ 163](esp32s3-gpio-sigmap_8h.md#a6d082fb1c7397d784a3075108e0dea73)#define ESP\_RMT\_SIG\_OUT1 82

[ 164](esp32s3-gpio-sigmap_8h.md#af88ebdd0d2d02ac58d720c001ccc155b)#define ESP\_RMT\_SIG\_IN2 83

[ 165](esp32s3-gpio-sigmap_8h.md#ad657c1ddcf9c335ac7876464b80b2705)#define ESP\_RMT\_SIG\_OUT2 83

[ 166](esp32s3-gpio-sigmap_8h.md#a1f930cd82690248b839f16ff7738f32c)#define ESP\_RMT\_SIG\_IN3 84

[ 167](esp32s3-gpio-sigmap_8h.md#ae60033bb70ca9ff7c2b52368d24a8ab8)#define ESP\_RMT\_SIG\_OUT3 84

[ 168](esp32s3-gpio-sigmap_8h.md#ae39a7176534ecc35ed432e6b825cf1ee)#define ESP\_USB\_JTAG\_TCK 85

[ 169](esp32s3-gpio-sigmap_8h.md#aca9c05aba976c762c0ec5fa3603c76e1)#define ESP\_USB\_JTAG\_TMS 86

[ 170](esp32s3-gpio-sigmap_8h.md#ad92972ab672e468cc56c24733114d7db)#define ESP\_USB\_JTAG\_TDI 87

[ 171](esp32s3-gpio-sigmap_8h.md#a880f86e1452afee85e90589f74c17a4d)#define ESP\_USB\_JTAG\_TDO 88

[ 172](esp32s3-gpio-sigmap_8h.md#ab607ce367da34ab0f1bd7fa648273cf1)#define ESP\_I2CEXT0\_SCL\_IN 89

[ 173](esp32s3-gpio-sigmap_8h.md#a2144cc62df795547ccf2bbe3ee4c629f)#define ESP\_I2CEXT0\_SCL\_OUT 89

[ 174](esp32s3-gpio-sigmap_8h.md#afa7061c87135b9dabe5c54f5f4ce16e6)#define ESP\_I2CEXT0\_SDA\_IN 90

[ 175](esp32s3-gpio-sigmap_8h.md#aabf1378b0ad2028c36c3bb74c81d7049)#define ESP\_I2CEXT0\_SDA\_OUT 90

[ 176](esp32s3-gpio-sigmap_8h.md#a1b6324b294e9e018a5909427f4f0ba36)#define ESP\_I2CEXT1\_SCL\_IN 91

[ 177](esp32s3-gpio-sigmap_8h.md#a3ac49ff21fcb59eeab6350821f9107e5)#define ESP\_I2CEXT1\_SCL\_OUT 91

[ 178](esp32s3-gpio-sigmap_8h.md#abb571ec9f2a59fc281837ca8bd3f2daa)#define ESP\_I2CEXT1\_SDA\_IN 92

[ 179](esp32s3-gpio-sigmap_8h.md#a3922109459dfd033147e4daf1ed4cd32)#define ESP\_I2CEXT1\_SDA\_OUT 92

[ 180](esp32s3-gpio-sigmap_8h.md#ae59035f8269ccd564ba0d7b2b078b3ee)#define ESP\_GPIO\_SD0\_OUT 93

[ 181](esp32s3-gpio-sigmap_8h.md#a3fbed77581ed14fa077f314e812b9c36)#define ESP\_GPIO\_SD1\_OUT 94

[ 182](esp32s3-gpio-sigmap_8h.md#a2668d9083ce28563cc160fe1102e927d)#define ESP\_GPIO\_SD2\_OUT 95

[ 183](esp32s3-gpio-sigmap_8h.md#a9d34f616894f98d7175c41b4ba565f8d)#define ESP\_GPIO\_SD3\_OUT 96

[ 184](esp32s3-gpio-sigmap_8h.md#aa88cedc2785b1e25a21ac70dd5603e68)#define ESP\_GPIO\_SD4\_OUT 97

[ 185](esp32s3-gpio-sigmap_8h.md#af0841a01cf24e79a447daa58a48db9f8)#define ESP\_GPIO\_SD5\_OUT 98

[ 186](esp32s3-gpio-sigmap_8h.md#a8c16952c92f5b28cd39b99771ccb983b)#define ESP\_GPIO\_SD6\_OUT 99

[ 187](esp32s3-gpio-sigmap_8h.md#a7fd22ae53413e708e4b75ad57e1be34a)#define ESP\_GPIO\_SD7\_OUT 100

[ 188](esp32s3-gpio-sigmap_8h.md#ade88988460c131e8c6775794588b0eb8)#define ESP\_FSPICLK\_IN 101

[ 189](esp32s3-gpio-sigmap_8h.md#ab8c5397dc530f6326c3d10b31e59e168)#define ESP\_FSPICLK\_OUT 101

[ 190](esp32s3-gpio-sigmap_8h.md#ab603b7bf7d016e85653a5c3be5c01293)#define ESP\_FSPIQ\_IN 102

[ 191](esp32s3-gpio-sigmap_8h.md#a8b3ea6ad374fa010b46b48072fa87ccb)#define ESP\_FSPIQ\_OUT 102

[ 192](esp32s3-gpio-sigmap_8h.md#a7910521af840d42edd3c0a667cf90c5f)#define ESP\_FSPID\_IN 103

[ 193](esp32s3-gpio-sigmap_8h.md#a02bd34821e8a4bf0038b9af417ec161a)#define ESP\_FSPID\_OUT 103

[ 194](esp32s3-gpio-sigmap_8h.md#a60ff087a3d85a356d77f060a6698d00b)#define ESP\_FSPIHD\_IN 104

[ 195](esp32s3-gpio-sigmap_8h.md#ac71bc137b93bd6c0c8a1ebe24a70a613)#define ESP\_FSPIHD\_OUT 104

[ 196](esp32s3-gpio-sigmap_8h.md#a4d4c4a13b820cab6d94da8fe08120a2f)#define ESP\_FSPIWP\_IN 105

[ 197](esp32s3-gpio-sigmap_8h.md#a83c4f18d726984cc98caeea9b7677ca1)#define ESP\_FSPIWP\_OUT 105

[ 198](esp32s3-gpio-sigmap_8h.md#af751015894fa1cefd780d4c483ed4fe0)#define ESP\_FSPIIO4\_IN 106

[ 199](esp32s3-gpio-sigmap_8h.md#a5131d3b8c5f15927eb1ab5f5c5831fc7)#define ESP\_FSPIIO4\_OUT 106

[ 200](esp32s3-gpio-sigmap_8h.md#aa422ee46d7a699a5de5acfce23544f1b)#define ESP\_FSPIIO5\_IN 107

[ 201](esp32s3-gpio-sigmap_8h.md#a846120bb034a5178b719de7566af36e9)#define ESP\_FSPIIO5\_OUT 107

[ 202](esp32s3-gpio-sigmap_8h.md#afbba101fa32685cf54ff6579245c232b)#define ESP\_FSPIIO6\_IN 108

[ 203](esp32s3-gpio-sigmap_8h.md#acb72c9ac62375b2ef22c4895fd5c37e9)#define ESP\_FSPIIO6\_OUT 108

[ 204](esp32s3-gpio-sigmap_8h.md#a7be0c3215d8ab00a4a87dcf4798207d9)#define ESP\_FSPIIO7\_IN 109

[ 205](esp32s3-gpio-sigmap_8h.md#a796dc85ea60a5cce0d0c184805164587)#define ESP\_FSPIIO7\_OUT 109

[ 206](esp32s3-gpio-sigmap_8h.md#a96ca1328e76337d289f6e65faf33d75c)#define ESP\_FSPICS0\_IN 110

[ 207](esp32s3-gpio-sigmap_8h.md#ad1be1401b282275eaef46b9a598c6a40)#define ESP\_FSPICS0\_OUT 110

[ 208](esp32s3-gpio-sigmap_8h.md#a44ade9179a7ea00586359a009799661d)#define ESP\_FSPICS1\_OUT 111

[ 209](esp32s3-gpio-sigmap_8h.md#af991963f29c5b268a5f8fead8fd15348)#define ESP\_FSPICS2\_OUT 112

[ 210](esp32s3-gpio-sigmap_8h.md#a65d1170c5a68ac7f6a4457c3380ddfde)#define ESP\_FSPICS3\_OUT 113

[ 211](esp32s3-gpio-sigmap_8h.md#a83dafe68703c701dcd07d7ff0aadad01)#define ESP\_FSPICS4\_OUT 114

[ 212](esp32s3-gpio-sigmap_8h.md#ad8fab64bb220fd198a6cd931f4ea1e8e)#define ESP\_FSPICS5\_OUT 115

[ 213](esp32s3-gpio-sigmap_8h.md#ab3da303c2f9226f9648669c17af8377a)#define ESP\_TWAI\_RX 116

[ 214](esp32s3-gpio-sigmap_8h.md#a3b13bb40583aaa0f85de982509247614)#define ESP\_TWAI\_TX 116

[ 215](esp32s3-gpio-sigmap_8h.md#a6d0d41d1ec0f6fc626861f5857684e6d)#define ESP\_TWAI\_BUS\_OFF\_ON 117

[ 216](esp32s3-gpio-sigmap_8h.md#a1c69791269fdbb2a11f66f33eb4066be)#define ESP\_TWAI\_CLKOUT 118

[ 217](esp32s3-gpio-sigmap_8h.md#a8fd6be50bb328dfd4ac0943f015b29ee)#define ESP\_SUBSPICLK\_OUT 119

[ 218](esp32s3-gpio-sigmap_8h.md#af80ecb5fcd6c02cb5b73478198abef3c)#define ESP\_SUBSPIQ\_IN 120

[ 219](esp32s3-gpio-sigmap_8h.md#ac75fd67f54d49449451c4924c0b7910a)#define ESP\_SUBSPIQ\_OUT 120

[ 220](esp32s3-gpio-sigmap_8h.md#a0c924000fccdb7ce112822db720dbd8d)#define ESP\_SUBSPID\_IN 121

[ 221](esp32s3-gpio-sigmap_8h.md#a3b9cab35f71697419266c71583f8a087)#define ESP\_SUBSPID\_OUT 121

[ 222](esp32s3-gpio-sigmap_8h.md#a9a04da28895e846359a3ea89391b21f6)#define ESP\_SUBSPIHD\_IN 122

[ 223](esp32s3-gpio-sigmap_8h.md#ab1f7e54d6230ceabc3fee083aab409d1)#define ESP\_SUBSPIHD\_OUT 122

[ 224](esp32s3-gpio-sigmap_8h.md#a3c4b2938ef6753d76a752bf9a973de52)#define ESP\_SUBSPIWP\_IN 123

[ 225](esp32s3-gpio-sigmap_8h.md#a7493ab9a1f0dc10902ce412055579842)#define ESP\_SUBSPIWP\_OUT 123

[ 226](esp32s3-gpio-sigmap_8h.md#a8925d5f830a4bc5ca6114dc06bae3b1f)#define ESP\_SUBSPICS0\_OUT 124

[ 227](esp32s3-gpio-sigmap_8h.md#add0fa80736d0fe196872bb0664c433d4)#define ESP\_SUBSPICS1\_OUT 125

[ 228](esp32s3-gpio-sigmap_8h.md#a83baa98d81f816f19e65aafb26f15a3c)#define ESP\_FSPIDQS\_OUT 126

[ 229](esp32s3-gpio-sigmap_8h.md#a9e4bf0b0eff43b1f56f17abe22ef24a5)#define ESP\_SPI3\_CS2\_OUT 127

[ 230](esp32s3-gpio-sigmap_8h.md#a6ab543889d74aa62a4ba609788223f0e)#define ESP\_I2S0O\_SD1\_OUT 128

[ 231](esp32s3-gpio-sigmap_8h.md#a214e2e05cf729479901dd03626ef045e)#define ESP\_CORE1\_GPIO\_IN0 129

[ 232](esp32s3-gpio-sigmap_8h.md#a1128c2ee52835afdd4ed37ddd94a7a4b)#define ESP\_CORE1\_GPIO\_OUT0 129

[ 233](esp32s3-gpio-sigmap_8h.md#a504eadf86e54f9b4c46461374691a567)#define ESP\_CORE1\_GPIO\_IN1 130

[ 234](esp32s3-gpio-sigmap_8h.md#a82296bbe122bc077945b4dbfd0b27f0d)#define ESP\_CORE1\_GPIO\_OUT1 130

[ 235](esp32s3-gpio-sigmap_8h.md#a0f84aadaf4ce6e95434bcd16402158e7)#define ESP\_CORE1\_GPIO\_IN2 131

[ 236](esp32s3-gpio-sigmap_8h.md#a8b92c91dce2faa4708790c5841c90697)#define ESP\_CORE1\_GPIO\_OUT2 131

[ 237](esp32s3-gpio-sigmap_8h.md#a53a3c23cc0db2b293fda78a6e24545f5)#define ESP\_LCD\_CS 132

[ 238](esp32s3-gpio-sigmap_8h.md#a257ff9bb2ab23b5c9437aa3ae5a8a3a8)#define ESP\_CAM\_DATA\_IN0 133

[ 239](esp32s3-gpio-sigmap_8h.md#a4f4ff1e21ce7c144e4de031bd42208df)#define ESP\_LCD\_DATA\_OUT0 133

[ 240](esp32s3-gpio-sigmap_8h.md#a07a2ceeafe386815dce64e074bc5170b)#define ESP\_CAM\_DATA\_IN1 134

[ 241](esp32s3-gpio-sigmap_8h.md#a50ed74e778b2a5d5609c29f02f7919d8)#define ESP\_LCD\_DATA\_OUT1 134

[ 242](esp32s3-gpio-sigmap_8h.md#ab505f36dbabfd33302db8e231506ec1f)#define ESP\_CAM\_DATA\_IN2 135

[ 243](esp32s3-gpio-sigmap_8h.md#ad32f77d444995d69e6097d67a5bfacc6)#define ESP\_LCD\_DATA\_OUT2 135

[ 244](esp32s3-gpio-sigmap_8h.md#a816bdba373a9d604c148465de08e5793)#define ESP\_CAM\_DATA\_IN3 136

[ 245](esp32s3-gpio-sigmap_8h.md#a5498b1c545ef91644eaf806325cf7b75)#define ESP\_LCD\_DATA\_OUT3 136

[ 246](esp32s3-gpio-sigmap_8h.md#af45144723ca836d01cc79653c4ed44db)#define ESP\_CAM\_DATA\_IN4 137

[ 247](esp32s3-gpio-sigmap_8h.md#aaa486e7766ddf6954395fdfa23a002bb)#define ESP\_LCD\_DATA\_OUT4 137

[ 248](esp32s3-gpio-sigmap_8h.md#af32e65a96dbdcc6f0fa8f17de746b083)#define ESP\_CAM\_DATA\_IN5 138

[ 249](esp32s3-gpio-sigmap_8h.md#a8f2afaff6454b563b4f6d451034b6bf0)#define ESP\_LCD\_DATA\_OUT5 138

[ 250](esp32s3-gpio-sigmap_8h.md#a50bc310217f80e7c592308b0f1e448db)#define ESP\_CAM\_DATA\_IN6 139

[ 251](esp32s3-gpio-sigmap_8h.md#a921738f261a92792cdaa2cd307502a82)#define ESP\_LCD\_DATA\_OUT6 139

[ 252](esp32s3-gpio-sigmap_8h.md#abf73b074dfa771a96a2814f7385c5488)#define ESP\_CAM\_DATA\_IN7 140

[ 253](esp32s3-gpio-sigmap_8h.md#a2d468c66d6983fbf32bfe0785430a061)#define ESP\_LCD\_DATA\_OUT7 140

[ 254](esp32s3-gpio-sigmap_8h.md#a1c77a6730f4bd3ea99b6c062fe801fe1)#define ESP\_CAM\_DATA\_IN8 141

[ 255](esp32s3-gpio-sigmap_8h.md#ab8d40e58dfd6843f6ddd8731bc3500a7)#define ESP\_LCD\_DATA\_OUT8 141

[ 256](esp32s3-gpio-sigmap_8h.md#ad998205ac3c496a8da706c36c6b03dab)#define ESP\_CAM\_DATA\_IN9 142

[ 257](esp32s3-gpio-sigmap_8h.md#a80649e927dfb699d57d1510d41c77dbf)#define ESP\_LCD\_DATA\_OUT9 142

[ 258](esp32s3-gpio-sigmap_8h.md#ad9fc1117b68eba7f5c68551ea1f654d4)#define ESP\_CAM\_DATA\_IN10 143

[ 259](esp32s3-gpio-sigmap_8h.md#a1181a8301f7b156843f2fa9fcde46ab6)#define ESP\_LCD\_DATA\_OUT10 143

[ 260](esp32s3-gpio-sigmap_8h.md#a277093423ffbc1a658d00e5c70edaf43)#define ESP\_CAM\_DATA\_IN11 144

[ 261](esp32s3-gpio-sigmap_8h.md#a9961daf1b1830c71d5219292ec0b3408)#define ESP\_LCD\_DATA\_OUT11 144

[ 262](esp32s3-gpio-sigmap_8h.md#a6be5ed7bad735d0b1f6d548e4baccdfe)#define ESP\_CAM\_DATA\_IN12 145

[ 263](esp32s3-gpio-sigmap_8h.md#a4ce4d9b69a4972d5811c7b786dd6a087)#define ESP\_LCD\_DATA\_OUT12 145

[ 264](esp32s3-gpio-sigmap_8h.md#af575322753a44a6d16bdc9ae057edf94)#define ESP\_CAM\_DATA\_IN13 146

[ 265](esp32s3-gpio-sigmap_8h.md#a10f62d5ec7fb095c718de9ffc25badac)#define ESP\_LCD\_DATA\_OUT13 146

[ 266](esp32s3-gpio-sigmap_8h.md#a5a532d5b315a7285e453988b6e4850da)#define ESP\_CAM\_DATA\_IN14 147

[ 267](esp32s3-gpio-sigmap_8h.md#aa5733e97bf116dcf3e824dd5ced97d86)#define ESP\_LCD\_DATA\_OUT14 147

[ 268](esp32s3-gpio-sigmap_8h.md#a85d788e027a99a1bd235b92919290c08)#define ESP\_CAM\_DATA\_IN15 148

[ 269](esp32s3-gpio-sigmap_8h.md#a680877bfb8fae097b7878c1547609f6e)#define ESP\_LCD\_DATA\_OUT15 148

[ 270](esp32s3-gpio-sigmap_8h.md#a692105d3da3d5b8c329052eb83822647)#define ESP\_CAM\_PCLK 149

[ 271](esp32s3-gpio-sigmap_8h.md#aaae230831f580a9da491c02880d27bed)#define ESP\_CAM\_CLK 149

[ 272](esp32s3-gpio-sigmap_8h.md#a61768a98e2410b1db7b1f7d6a1d899a2)#define ESP\_CAM\_H\_ENABLE 150

[ 273](esp32s3-gpio-sigmap_8h.md#a997c1262b9e18006dc512b22bef27c55)#define ESP\_LCD\_H\_ENABLE 150

[ 274](esp32s3-gpio-sigmap_8h.md#a7fe4c5732cae0c8744c8fe4dff9d8789)#define ESP\_CAM\_H\_SYNC 151

[ 275](esp32s3-gpio-sigmap_8h.md#a97e85278e1c6c4b9557608961aafa0db)#define ESP\_LCD\_H\_SYNC 151

[ 276](esp32s3-gpio-sigmap_8h.md#a360710b489ab8657418b55ec18f78281)#define ESP\_CAM\_V\_SYNC 152

[ 277](esp32s3-gpio-sigmap_8h.md#ac88307d440dd2d45896a25e89c8e7f82)#define ESP\_LCD\_V\_SYNC 152

[ 278](esp32s3-gpio-sigmap_8h.md#a6a8af909a6c89460fa74ca7c295b74d2)#define ESP\_LCD\_DC 153

[ 279](esp32s3-gpio-sigmap_8h.md#a39d94c85937af83a1bb2c32cc85dfd26)#define ESP\_LCD\_PCLK 154

[ 280](esp32s3-gpio-sigmap_8h.md#aae7066cb62b74cf5e8f64f84bd76ee49)#define ESP\_SUBSPID4\_IN 155

[ 281](esp32s3-gpio-sigmap_8h.md#aa716d46da29da6affd5fa8851a730f3f)#define ESP\_SUBSPID4\_OUT 155

[ 282](esp32s3-gpio-sigmap_8h.md#a051cd2450520fd4abc6f288c8577a12c)#define ESP\_SUBSPID5\_IN 156

[ 283](esp32s3-gpio-sigmap_8h.md#aece7dc6fc4bca1bd73d9ba856eb0f3fe)#define ESP\_SUBSPID5\_OUT 156

[ 284](esp32s3-gpio-sigmap_8h.md#a6d49162b17a1a7cd3f2446c6ca8192ec)#define ESP\_SUBSPID6\_IN 157

[ 285](esp32s3-gpio-sigmap_8h.md#ab3e8db3219bf7aa7b2503a1fe759d60c)#define ESP\_SUBSPID6\_OUT 157

[ 286](esp32s3-gpio-sigmap_8h.md#a34b9a22e0f55a0534199e62b1eaff5b0)#define ESP\_SUBSPID7\_IN 158

[ 287](esp32s3-gpio-sigmap_8h.md#adb8c01bf2361a8b24e79cf048a7e6535)#define ESP\_SUBSPID7\_OUT 158

[ 288](esp32s3-gpio-sigmap_8h.md#a6ccb6e41ab48fba76302068ee4433fb8)#define ESP\_SUBSPIDQS\_IN 159

[ 289](esp32s3-gpio-sigmap_8h.md#a608345dcd6c90e4f19427bb38161501a)#define ESP\_SUBSPIDQS\_OUT 159

[ 290](esp32s3-gpio-sigmap_8h.md#a60a3fe70a1bc5ba71cb46df782901087)#define ESP\_PWM0\_SYNC0\_IN 160

[ 291](esp32s3-gpio-sigmap_8h.md#a9397a79a46feab488c88552013790dfc)#define ESP\_PWM0\_OUT0A 160

[ 292](esp32s3-gpio-sigmap_8h.md#aca616afbb64ed37982624503545a5a72)#define ESP\_PWM0\_SYNC1\_IN 161

[ 293](esp32s3-gpio-sigmap_8h.md#acb3badfaed73f7069ea23dde375db62a)#define ESP\_PWM0\_OUT0B 161

[ 294](esp32s3-gpio-sigmap_8h.md#a2017681d630abc75e7298c12b86a62ce)#define ESP\_PWM0\_SYNC2\_IN 162

[ 295](esp32s3-gpio-sigmap_8h.md#ae52e5bd4be5563caeb9861267e41d947)#define ESP\_PWM0\_OUT1A 162

[ 296](esp32s3-gpio-sigmap_8h.md#a4a503a957b2fd76f257534b80069caa2)#define ESP\_PWM0\_F0\_IN 163

[ 297](esp32s3-gpio-sigmap_8h.md#a9fa8e944ff2d960c141f8375c9aa0b0e)#define ESP\_PWM0\_OUT1B 163

[ 298](esp32s3-gpio-sigmap_8h.md#af536ae867a3d8bcb7644b48c346b4b50)#define ESP\_PWM0\_F1\_IN 164

[ 299](esp32s3-gpio-sigmap_8h.md#abf74a2a32a8c36431e2f21d6cd15a610)#define ESP\_PWM0\_OUT2A 164

[ 300](esp32s3-gpio-sigmap_8h.md#a83f385e6b8a99314cc641083a203322b)#define ESP\_PWM0\_F2\_IN 165

[ 301](esp32s3-gpio-sigmap_8h.md#a563105deedf9f7ed6818ab9a8a8aecdc)#define ESP\_PWM0\_OUT2B 165

[ 302](esp32s3-gpio-sigmap_8h.md#a421b59e20586b4f48b7e81bfa0ad4357)#define ESP\_PWM0\_CAP0\_IN 166

[ 303](esp32s3-gpio-sigmap_8h.md#a4f8f7187a2a8dbf4b104e3a7e7bd5dae)#define ESP\_PWM1\_OUT0A 166

[ 304](esp32s3-gpio-sigmap_8h.md#aea7a8712f1502df47721258470ff5b48)#define ESP\_PWM0\_CAP1\_IN 167

[ 305](esp32s3-gpio-sigmap_8h.md#a553561934aa817659a5c781dfeccfc3e)#define ESP\_PWM1\_OUT0B 167

[ 306](esp32s3-gpio-sigmap_8h.md#ab221240161be67a0f5af577494c8a5ad)#define ESP\_PWM0\_CAP2\_IN 168

[ 307](esp32s3-gpio-sigmap_8h.md#a852f0b23fd2c3d2f90b6bcfccd5f375e)#define ESP\_PWM1\_OUT1A 168

[ 308](esp32s3-gpio-sigmap_8h.md#a9f251384f8a6a10b0fb173c4bfda88ba)#define ESP\_PWM1\_SYNC0\_IN 169

[ 309](esp32s3-gpio-sigmap_8h.md#ab9bc2ae5e0e53935f8b58380dfd397e8)#define ESP\_PWM1\_OUT1B 169

[ 310](esp32s3-gpio-sigmap_8h.md#a646d7d644b5d4ec403eab7ff793cf7b2)#define ESP\_PWM1\_SYNC1\_IN 170

[ 311](esp32s3-gpio-sigmap_8h.md#a8beedf183380bfe83c435f9c5920215e)#define ESP\_PWM1\_OUT2A 170

[ 312](esp32s3-gpio-sigmap_8h.md#a56a67f8e168a4e7545e3ca4bcf7c8d89)#define ESP\_PWM1\_SYNC2\_IN 171

[ 313](esp32s3-gpio-sigmap_8h.md#ae1976c33c4e94a76d09ee5c3aa93f04e)#define ESP\_PWM1\_OUT2B 171

[ 314](esp32s3-gpio-sigmap_8h.md#a09c262c332e65ccc9eb2d91d976958e3)#define ESP\_PWM1\_F0\_IN 172

[ 315](esp32s3-gpio-sigmap_8h.md#aff5857c7ef89e0ff32bbb49e393ea003)#define ESP\_SDHOST\_CCLK\_OUT\_1 172

[ 316](esp32s3-gpio-sigmap_8h.md#af4b1c0ff4e222f09eee18cbb85cedb67)#define ESP\_PWM1\_F1\_IN 173

[ 317](esp32s3-gpio-sigmap_8h.md#a00c0010ef6f14d2fa3b374f682dd0b46)#define ESP\_SDHOST\_CCLK\_OUT\_2 173

[ 318](esp32s3-gpio-sigmap_8h.md#ac911f11a68e10d359cffe49864739e2d)#define ESP\_PWM1\_F2\_IN 174

[ 319](esp32s3-gpio-sigmap_8h.md#abeb145776728098f097fd5a3a9b89132)#define ESP\_SDHOST\_RST\_N\_1 174

[ 320](esp32s3-gpio-sigmap_8h.md#a8f2dcd1f46c2a5a5da3be188dca9e3a0)#define ESP\_PWM1\_CAP0\_IN 175

[ 321](esp32s3-gpio-sigmap_8h.md#a0536f51d9a6adba1138304fa758db39a)#define ESP\_SDHOST\_RST\_N\_2 175

[ 322](esp32s3-gpio-sigmap_8h.md#a8b97c639d66dcb8400aefc344bf490d1)#define ESP\_PWM1\_CAP1\_IN 176

[ 323](esp32s3-gpio-sigmap_8h.md#ae9e1e3a249d4fa5f330de8b0d0920a75)#define ESP\_SDHOST\_CCMD\_OD\_PULLUP\_EN\_N176

[ 324](esp32s3-gpio-sigmap_8h.md#a23b8540974bcf9dbd5c0ff92d9b69ac9)#define ESP\_PWM1\_CAP2\_IN 177

[ 325](esp32s3-gpio-sigmap_8h.md#aac3529b76d29e57ad20500c9d1da23f3)#define ESP\_SDIO\_TOHOST\_INT\_OUT 177

[ 326](esp32s3-gpio-sigmap_8h.md#aa99bd561249d2e1eb4344f298873f503)#define ESP\_SDHOST\_CCMD\_IN\_1 178

[ 327](esp32s3-gpio-sigmap_8h.md#a5f1a59ccefd8e2388338627978e44059)#define ESP\_SDHOST\_CCMD\_OUT\_1 178

[ 328](esp32s3-gpio-sigmap_8h.md#a041fd8cb426a95f145725f246201dacd)#define ESP\_SDHOST\_CCMD\_IN\_2 179

[ 329](esp32s3-gpio-sigmap_8h.md#a3122a431d37d337935ce459ce2826a5e)#define ESP\_SDHOST\_CCMD\_OUT\_2 179

[ 330](esp32s3-gpio-sigmap_8h.md#aa202d8a403ae5dac9a51f66dcc899815)#define ESP\_SDHOST\_CDATA\_IN\_10 180

[ 331](esp32s3-gpio-sigmap_8h.md#a650be8be910f36d892d2af6b903abe6e)#define ESP\_SDHOST\_CDATA\_OUT\_10 180

[ 332](esp32s3-gpio-sigmap_8h.md#a4518625593104880441b0d405eeb9d79)#define ESP\_SDHOST\_CDATA\_IN\_11 181

[ 333](esp32s3-gpio-sigmap_8h.md#a4e2d79ab775783efc0cdf86115331447)#define ESP\_SDHOST\_CDATA\_OUT\_11 181

[ 334](esp32s3-gpio-sigmap_8h.md#abf24ff245054912561d51db5d248770b)#define ESP\_SDHOST\_CDATA\_IN\_12 182

[ 335](esp32s3-gpio-sigmap_8h.md#ace4ef14e4a0d7b0c28199eb8e837136e)#define ESP\_SDHOST\_CDATA\_OUT\_12 182

[ 336](esp32s3-gpio-sigmap_8h.md#a250805f95412af52d358f90ab2ff9cab)#define ESP\_SDHOST\_CDATA\_IN\_13 183

[ 337](esp32s3-gpio-sigmap_8h.md#a1b9425434296a84ae20e5138e99f3cc7)#define ESP\_SDHOST\_CDATA\_OUT\_13 183

[ 338](esp32s3-gpio-sigmap_8h.md#a5aec6c17086301750c3ff542f784c73c)#define ESP\_SDHOST\_CDATA\_IN\_14 184

[ 339](esp32s3-gpio-sigmap_8h.md#af720ace3a3c5109b440201c529ab9f68)#define ESP\_SDHOST\_CDATA\_OUT\_14 184

[ 340](esp32s3-gpio-sigmap_8h.md#a511407191c4f58e59f19d0cbd527f940)#define ESP\_SDHOST\_CDATA\_IN\_15 185

[ 341](esp32s3-gpio-sigmap_8h.md#a627e3a4e12df8e358d937bbabcaa8eb0)#define ESP\_SDHOST\_CDATA\_OUT\_15 185

[ 342](esp32s3-gpio-sigmap_8h.md#ada2bd9384398308507f1827c187e5dd6)#define ESP\_SDHOST\_CDATA\_IN\_16 186

[ 343](esp32s3-gpio-sigmap_8h.md#a502ca14944ee4d93aabcba4eafa0d900)#define ESP\_SDHOST\_CDATA\_OUT\_16 186

[ 344](esp32s3-gpio-sigmap_8h.md#af12e58d00a8085cbafcac751b5a90705)#define ESP\_SDHOST\_CDATA\_IN\_17 187

[ 345](esp32s3-gpio-sigmap_8h.md#ab695d377e135cac2283bc1c915396494)#define ESP\_SDHOST\_CDATA\_OUT\_17 187

[ 346](esp32s3-gpio-sigmap_8h.md#a0ad409b608ef2a418098b4e51d0e7e9a)#define ESP\_PCMFSYNC\_IN 188

[ 347](esp32s3-gpio-sigmap_8h.md#afd2befcf5eb0c413c0f8447558dc4863)#define ESP\_BT\_AUDIO0\_IRQ 188

[ 348](esp32s3-gpio-sigmap_8h.md#abb4d1f28362c68cf3f1e9f1696602b03)#define ESP\_PCMCLK\_IN 189

[ 349](esp32s3-gpio-sigmap_8h.md#acfe665b9ff21a51b93819a3f123180ad)#define ESP\_BT\_AUDIO1\_IRQ 189

[ 350](esp32s3-gpio-sigmap_8h.md#ae94f8dfc2be2c0cf8863a33df76d5295)#define ESP\_PCMDIN 190

[ 351](esp32s3-gpio-sigmap_8h.md#a77ac554a2a10fc6fa77106e8af9dfc86)#define ESP\_BT\_AUDIO2\_IRQ 190

[ 352](esp32s3-gpio-sigmap_8h.md#a7abc844342f6483be73ea503d3f76d89)#define ESP\_RW\_WAKEUP\_REQ 191

[ 353](esp32s3-gpio-sigmap_8h.md#ab2e25b779a18acd66533795433291a3d)#define ESP\_BLE\_AUDIO0\_IRQ 191

[ 354](esp32s3-gpio-sigmap_8h.md#a13b46bfbdddc6ceedbb30b0f0dc6be5d)#define ESP\_SDHOST\_DATA\_STROBE\_1 192

[ 355](esp32s3-gpio-sigmap_8h.md#ab4b3d654c674536c2c63070210147372)#define ESP\_BLE\_AUDIO1\_IRQ 192

[ 356](esp32s3-gpio-sigmap_8h.md#a209b7dd99039e60f032ac234c14e4c9d)#define ESP\_SDHOST\_DATA\_STROBE\_2 193

[ 357](esp32s3-gpio-sigmap_8h.md#a637ea6fcad7b2e5fe48cf9e3419fbed6)#define ESP\_BLE\_AUDIO2\_IRQ 193

[ 358](esp32s3-gpio-sigmap_8h.md#af3a093b62bef7d1da43e168abee9823b)#define ESP\_SDHOST\_CARD\_DETECT\_N\_1 194

[ 359](esp32s3-gpio-sigmap_8h.md#a8b79d6e15573a684058c9b933f469f09)#define ESP\_PCMFSYNC\_OUT 194

[ 360](esp32s3-gpio-sigmap_8h.md#ab42e6528593924d759ee03f41faa88e9)#define ESP\_SDHOST\_CARD\_DETECT\_N\_2 195

[ 361](esp32s3-gpio-sigmap_8h.md#a500651ca0d6daa86774a0f45190f8b38)#define ESP\_PCMCLK\_OUT 195

[ 362](esp32s3-gpio-sigmap_8h.md#a90ed679e9630feb28030c0c1995b85f7)#define ESP\_SDHOST\_CARD\_WRITE\_PRT\_1 196

[ 363](esp32s3-gpio-sigmap_8h.md#ab3ecd7e5557112172c38bff3b2605e9c)#define ESP\_PCMDOUT 196

[ 364](esp32s3-gpio-sigmap_8h.md#a1bc9c1d813aa85230ea95c190145d9bf)#define ESP\_SDHOST\_CARD\_WRITE\_PRT\_2 197

[ 365](esp32s3-gpio-sigmap_8h.md#aba2aea8feedc96a0a6b3bba007df49ac)#define ESP\_BLE\_AUDIO\_SYNC0\_P 197

[ 366](esp32s3-gpio-sigmap_8h.md#ad6288e71dadae26fee5cb658c967254e)#define ESP\_SDHOST\_CARD\_INT\_N\_1 198

[ 367](esp32s3-gpio-sigmap_8h.md#a21e5bf1c7c33a39f11d8bf6537ed85bb)#define ESP\_BLE\_AUDIO\_SYNC1\_P 198

[ 368](esp32s3-gpio-sigmap_8h.md#accd3ea038126b88448f33984bd058427)#define ESP\_SDHOST\_CARD\_INT\_N\_2 199

[ 369](esp32s3-gpio-sigmap_8h.md#a961f37a0b2dcb9e183331ef5684f8504)#define ESP\_BLE\_AUDIO\_SYNC2\_P 199

[ 370](esp32s3-gpio-sigmap_8h.md#aec2dfb198f69d923686404a0a6330833)#define ESP\_ANT\_SEL0 200

[ 371](esp32s3-gpio-sigmap_8h.md#a15c080ea1e4c8e2db9f1640e9b8c4f0a)#define ESP\_ANT\_SEL1 201

[ 372](esp32s3-gpio-sigmap_8h.md#ae3042ff86ecc0f2e78ebe9477055e819)#define ESP\_ANT\_SEL2 202

[ 373](esp32s3-gpio-sigmap_8h.md#ab8e5cca4b9eb1a7bda7868ecd792c76d)#define ESP\_ANT\_SEL3 203

[ 374](esp32s3-gpio-sigmap_8h.md#a821cc4b81f76043b1ecb751118a2f416)#define ESP\_ANT\_SEL4 204

[ 375](esp32s3-gpio-sigmap_8h.md#a28a954881fd9d5f5e7ff25d715f0bcc2)#define ESP\_ANT\_SEL5 205

[ 376](esp32s3-gpio-sigmap_8h.md#a2122dad1966cbe214e9c82cb9a46bd8a)#define ESP\_ANT\_SEL6 206

[ 377](esp32s3-gpio-sigmap_8h.md#a8f9cedf15c49cee3fbac2a22df7675ec)#define ESP\_ANT\_SEL7 207

[ 378](esp32s3-gpio-sigmap_8h.md#a5e192de902e66cccd6ec3c72ed8ef82a)#define ESP\_SIG\_IN\_FUNC\_208 208

[ 379](esp32s3-gpio-sigmap_8h.md#a0f6d8766907b91e60e62ae29c5e4b558)#define ESP\_SIG\_IN\_FUNC208 208

[ 380](esp32s3-gpio-sigmap_8h.md#a240123ea7ff1b64a70d1bb4866fe174b)#define ESP\_SIG\_IN\_FUNC\_209 209

[ 381](esp32s3-gpio-sigmap_8h.md#a8fe491023178ce16dd57edae3bdfe87f)#define ESP\_SIG\_IN\_FUNC209 209

[ 382](esp32s3-gpio-sigmap_8h.md#a09fe402e83b28df1927599b5daa0b700)#define ESP\_SIG\_IN\_FUNC\_210 210

[ 383](esp32s3-gpio-sigmap_8h.md#add709f3eecdbe328426cd93013c80c3e)#define ESP\_SIG\_IN\_FUNC210 210

[ 384](esp32s3-gpio-sigmap_8h.md#a38bfce1eb51e0913355a02e67d0d1496)#define ESP\_SIG\_IN\_FUNC\_211 211

[ 385](esp32s3-gpio-sigmap_8h.md#aa286ed797d5ab072404cda4eca929566)#define ESP\_SIG\_IN\_FUNC211 211

[ 386](esp32s3-gpio-sigmap_8h.md#ab5f2a06dab84e52c93b6a25172e7b2c4)#define ESP\_SIG\_IN\_FUNC\_212 212

[ 387](esp32s3-gpio-sigmap_8h.md#a8f25ba37edb68eb23e64395280ab791a)#define ESP\_SIG\_IN\_FUNC212 212

[ 388](esp32s3-gpio-sigmap_8h.md#a13ca361ff287a452bcdc24992448e59e)#define ESP\_SDHOST\_CDATA\_IN\_20 213

[ 389](esp32s3-gpio-sigmap_8h.md#a06f93230a36ef5287147a0564b1dfed1)#define ESP\_SDHOST\_CDATA\_OUT\_20 213

[ 390](esp32s3-gpio-sigmap_8h.md#ab4c0aef79106c2d286f6d4bce99bd9eb)#define ESP\_SDHOST\_CDATA\_IN\_21 214

[ 391](esp32s3-gpio-sigmap_8h.md#a6c9f531502c69bcd5889d60837ec0bdb)#define ESP\_SDHOST\_CDATA\_OUT\_21 214

[ 392](esp32s3-gpio-sigmap_8h.md#a5e4da4ac40cff37134d19032640fa253)#define ESP\_SDHOST\_CDATA\_IN\_22 215

[ 393](esp32s3-gpio-sigmap_8h.md#a786692b41d500d85fe88ee63d8e60fd5)#define ESP\_SDHOST\_CDATA\_OUT\_22 215

[ 394](esp32s3-gpio-sigmap_8h.md#aae5dec0fc3b263f26798bdfed1122a18)#define ESP\_SDHOST\_CDATA\_IN\_23 216

[ 395](esp32s3-gpio-sigmap_8h.md#a98324b90550b28d722cb38a3dd122532)#define ESP\_SDHOST\_CDATA\_OUT\_23 216

[ 396](esp32s3-gpio-sigmap_8h.md#a098ad3a54b47ed40202ae8c2a9b6f7ec)#define ESP\_SDHOST\_CDATA\_IN\_24 217

[ 397](esp32s3-gpio-sigmap_8h.md#a6898cbd2b727b76e5208cbc1a102b2a2)#define ESP\_SDHOST\_CDATA\_OUT\_24 217

[ 398](esp32s3-gpio-sigmap_8h.md#a22d372ec349ce449aba06bf85cc1c1b5)#define ESP\_SDHOST\_CDATA\_IN\_25 218

[ 399](esp32s3-gpio-sigmap_8h.md#a638507475f38120dbd76db6f53455f57)#define ESP\_SDHOST\_CDATA\_OUT\_25 218

[ 400](esp32s3-gpio-sigmap_8h.md#af78c9aa8fc70487f561271635ff63b64)#define ESP\_SDHOST\_CDATA\_IN\_26 219

[ 401](esp32s3-gpio-sigmap_8h.md#a492c8431649dc6c429347d9a041a23cd)#define ESP\_SDHOST\_CDATA\_OUT\_26 219

[ 402](esp32s3-gpio-sigmap_8h.md#a2177168014217dcc8625d64f4d79e7e2)#define ESP\_SDHOST\_CDATA\_IN\_27 220

[ 403](esp32s3-gpio-sigmap_8h.md#aece0df9752dd44b35534bda1251c484d)#define ESP\_SDHOST\_CDATA\_OUT\_27 220

[ 404](esp32s3-gpio-sigmap_8h.md#a9023b22f85edc25ab88db9f3fb025c4e)#define ESP\_PRO\_ALONEGPIO\_IN0 221

[ 405](esp32s3-gpio-sigmap_8h.md#ae833440baa7073fbfb51ec80ff728ce5)#define ESP\_PRO\_ALONEGPIO\_OUT0 221

[ 406](esp32s3-gpio-sigmap_8h.md#a5e4c12a21678930c86e15cbb6d920767)#define ESP\_PRO\_ALONEGPIO\_IN1 222

[ 407](esp32s3-gpio-sigmap_8h.md#a5b3065b35c32286fe5ca8d68c033b162)#define ESP\_PRO\_ALONEGPIO\_OUT1 222

[ 408](esp32s3-gpio-sigmap_8h.md#a8b82dbe07c785060d2190a13e1fe21ee)#define ESP\_PRO\_ALONEGPIO\_IN2 223

[ 409](esp32s3-gpio-sigmap_8h.md#a287e800e3fb52dd3b6949e6d185f413c)#define ESP\_PRO\_ALONEGPIO\_OUT2 223

[ 410](esp32s3-gpio-sigmap_8h.md#a5f8a8f6143c1552eec5862ce248ca496)#define ESP\_PRO\_ALONEGPIO\_IN3 224

[ 411](esp32s3-gpio-sigmap_8h.md#a49f220c0a7cae6a580174355a80b2b56)#define ESP\_PRO\_ALONEGPIO\_OUT3 224

[ 412](esp32s3-gpio-sigmap_8h.md#ad8ca1006a71cdd738cca02eaf9f923d6)#define ESP\_PRO\_ALONEGPIO\_IN4 225

[ 413](esp32s3-gpio-sigmap_8h.md#ac1b762f9e0ad1cb60c1e16b0cf7aae0a)#define ESP\_PRO\_ALONEGPIO\_OUT4 225

[ 414](esp32s3-gpio-sigmap_8h.md#aa1b04ac7997451778d7fdbb4f00b0114)#define ESP\_PRO\_ALONEGPIO\_IN5 226

[ 415](esp32s3-gpio-sigmap_8h.md#a5f237780803395dd97bb8306a14dbc92)#define ESP\_PRO\_ALONEGPIO\_OUT5 226

[ 416](esp32s3-gpio-sigmap_8h.md#a525900ed7a103a14105afb6ef8caca69)#define ESP\_PRO\_ALONEGPIO\_IN6 227

[ 417](esp32s3-gpio-sigmap_8h.md#a4cbc6a3551e057f1d943b01c120317f4)#define ESP\_PRO\_ALONEGPIO\_OUT6 227

[ 418](esp32s3-gpio-sigmap_8h.md#af6ebbb44bcb763355964ac39293cd1c4)#define ESP\_PRO\_ALONEGPIO\_IN7 228

[ 419](esp32s3-gpio-sigmap_8h.md#a3d1993f51138a3ccf8ef913e1863f3bd)#define ESP\_PRO\_ALONEGPIO\_OUT7 228

[ 420](esp32s3-gpio-sigmap_8h.md#a0206456525cd6dc235ed6892e98731c6)#define ESP\_SYNCERR 229

[ 421](esp32s3-gpio-sigmap_8h.md#aa62bd8539c4d89abaa542d8bd4c91efd)#define ESP\_SYNCFOUND\_FLAG 230

[ 422](esp32s3-gpio-sigmap_8h.md#ade4ee47d8f72c009686b2454ee77ee60)#define ESP\_EVT\_CNTL\_IMMEDIATE\_ABORT 231

[ 423](esp32s3-gpio-sigmap_8h.md#ac5684072c6c5fbbdb6631d73270819dc)#define ESP\_LINKLBL 232

[ 424](esp32s3-gpio-sigmap_8h.md#a1029a66c0538d7eb1026ced27d54a59b)#define ESP\_DATA\_EN 233

[ 425](esp32s3-gpio-sigmap_8h.md#a04dc693cfec6739602b92e86a837c58d)#define ESP\_DATA 234

[ 426](esp32s3-gpio-sigmap_8h.md#aecac02e2195c5da81f63ed4c19bd06fb)#define ESP\_PKT\_TX\_ON 235

[ 427](esp32s3-gpio-sigmap_8h.md#a63f7ec6fc7927b0f0fb3bd0dc733de5a)#define ESP\_PKT\_RX\_ON 236

[ 428](esp32s3-gpio-sigmap_8h.md#a3b8a7f22861948aa8809aa58ecbdb0ef)#define ESP\_RW\_TX\_ON 237

[ 429](esp32s3-gpio-sigmap_8h.md#a5f93eee3354e5fd70d11fd26c9dd25bb)#define ESP\_RW\_RX\_ON 238

[ 430](esp32s3-gpio-sigmap_8h.md#af7d8fb5a97cb0e4f3dad1a73fb0610d5)#define ESP\_EVT\_REQ\_P 239

[ 431](esp32s3-gpio-sigmap_8h.md#a10fd19b9a6140fea7e88facaa02686be)#define ESP\_EVT\_STOP\_P 240

[ 432](esp32s3-gpio-sigmap_8h.md#a08a40a396cf075e77aa50acfb811885a)#define ESP\_BT\_MODE\_ON 241

[ 433](esp32s3-gpio-sigmap_8h.md#a80a3804720f2e69ac5caa52c0ade9d5b)#define ESP\_GPIO\_LC\_DIAG0 242

[ 434](esp32s3-gpio-sigmap_8h.md#ad842d1a31efaf5f3edc70326ac89df9b)#define ESP\_GPIO\_LC\_DIAG1 243

[ 435](esp32s3-gpio-sigmap_8h.md#ad23ea4680ce2cbf713bb456dae84e35b)#define ESP\_GPIO\_LC\_DIAG2 244

[ 436](esp32s3-gpio-sigmap_8h.md#a83ab157d422c3004c3dc287c0c804ec5)#define ESP\_CH 245

[ 437](esp32s3-gpio-sigmap_8h.md#a546d9b83cad2a5b2e64677be087b1f9d)#define ESP\_RX\_WINDOW 246

[ 438](esp32s3-gpio-sigmap_8h.md#a25d03cedd231864f508e405d0ae2fa4b)#define ESP\_UPDATE\_RX 247

[ 439](esp32s3-gpio-sigmap_8h.md#ac2450d1a096d1adf2386ba91e0a92f75)#define ESP\_RX\_STATUS 248

[ 440](esp32s3-gpio-sigmap_8h.md#ae27ee8b3a05b497ec7bea2ed69fc9230)#define ESP\_CLK\_GPIO 249

[ 441](esp32s3-gpio-sigmap_8h.md#a9aa8b294d23efae4cd5a6dd741829aad)#define ESP\_NBT\_BLE 250

[ 442](esp32s3-gpio-sigmap_8h.md#a6b5babfcba4d025bdd1ab709b569fdf2)#define ESP\_USB\_JTAG\_TDO\_BRIDGE 251

[ 443](esp32s3-gpio-sigmap_8h.md#a4358434232f1f3515d8f5f4961d77520)#define ESP\_USB\_JTAG\_TRST 251

[ 444](esp32s3-gpio-sigmap_8h.md#af08fab550c96147c3b1c54ca41eac3b4)#define ESP\_CORE1\_GPIO\_IN3 252

[ 445](esp32s3-gpio-sigmap_8h.md#a132a8965b837c561f6ec1f0d15bf39cb)#define ESP\_CORE1\_GPIO\_OUT3 252

[ 446](esp32s3-gpio-sigmap_8h.md#a830e2f2adc5bf86a4080fa64e7435beb)#define ESP\_CORE1\_GPIO\_IN4 253

[ 447](esp32s3-gpio-sigmap_8h.md#af8e3c657135901ead83da1c58079bae5)#define ESP\_CORE1\_GPIO\_OUT4 253

[ 448](esp32s3-gpio-sigmap_8h.md#adb0166f5083f37eb82469fbab88eb21b)#define ESP\_CORE1\_GPIO\_IN5 254

[ 449](esp32s3-gpio-sigmap_8h.md#a09461b98dd020d78786ce01c244fda54)#define ESP\_CORE1\_GPIO\_OUT5 254

[ 450](esp32s3-gpio-sigmap_8h.md#a765b233e0f1e7dc50424e895dc7ba930)#define ESP\_CORE1\_GPIO\_IN6 255

[ 451](esp32s3-gpio-sigmap_8h.md#ac087a21dd9d6a84b6bd6f885d02bf0c9)#define ESP\_CORE1\_GPIO\_OUT6 255

[ 452](esp32s3-gpio-sigmap_8h.md#a645411759ffdc63f51f2cd42632d2720)#define ESP\_SIG\_GPIO\_OUT 256

[ 453](esp32s3-gpio-sigmap_8h.md#afe5c166b887709cdd27bd37df85c45b9)#define ESP\_GPIO\_MAP\_DATE 0x1907040

454

455#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32S3\_GPIO\_SIGMAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32s3-gpio-sigmap.h](esp32s3-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
