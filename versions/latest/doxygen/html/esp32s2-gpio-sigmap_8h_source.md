---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32s2-gpio-sigmap_8h_source.html
original_path: doxygen/html/esp32s2-gpio-sigmap_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s2-gpio-sigmap.h

[Go to the documentation of this file.](esp32s2-gpio-sigmap_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32S2\_GPIO\_SIGMAP\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32S2\_GPIO\_SIGMAP\_H\_

9

[ 10](esp32s2-gpio-sigmap_8h.md#af80260535bc3aee44c28c972a29483e0)#define ESP\_NOSIG ESP\_SIG\_INVAL

11

[ 12](esp32s2-gpio-sigmap_8h.md#a5f440c922a53085bb7b28f469c2a14b0)#define ESP\_SPICLK\_OUT ESP\_SPICLK\_OUT\_MUX

[ 13](esp32s2-gpio-sigmap_8h.md#a7f8cd1f168870c1cfa215fc1599ebf74)#define ESP\_CLK\_I2S ESP\_CLK\_I2S\_MUX

[ 14](esp32s2-gpio-sigmap_8h.md#ab8c5397dc530f6326c3d10b31e59e168)#define ESP\_FSPICLK\_OUT ESP\_FSPICLK\_OUT\_MUX

15

[ 16](esp32s2-gpio-sigmap_8h.md#aec51ff955c6be50e529affc87ec9d5cb)#define ESP\_SPIQ\_IN 0

[ 17](esp32s2-gpio-sigmap_8h.md#a5816deeca8853397a830a8eb251704ee)#define ESP\_SPIQ\_OUT 0

[ 18](esp32s2-gpio-sigmap_8h.md#a26c603fd58dbd7526d2be3bb3e37758a)#define ESP\_SPID\_IN 1

[ 19](esp32s2-gpio-sigmap_8h.md#af81b2fc65b68ed2238ab3367a8731102)#define ESP\_SPID\_OUT 1

[ 20](esp32s2-gpio-sigmap_8h.md#a49783f877b666aff9362cf605590b991)#define ESP\_SPIHD\_IN 2

[ 21](esp32s2-gpio-sigmap_8h.md#a8851b5256482790f3304efecafc13afd)#define ESP\_SPIHD\_OUT 2

[ 22](esp32s2-gpio-sigmap_8h.md#aa74adc2812d9c6bd143c679fa4d9ca8d)#define ESP\_SPIWP\_IN 3

[ 23](esp32s2-gpio-sigmap_8h.md#a470408f8102937dc017336e320e6147b)#define ESP\_SPIWP\_OUT 3

[ 24](esp32s2-gpio-sigmap_8h.md#aaf157f6b85a07f18b181876a7a04f142)#define ESP\_SPICLK\_OUT\_MUX 4

[ 25](esp32s2-gpio-sigmap_8h.md#a5d97c07ba0d8cda594d52310e90fa6a4)#define ESP\_SPICS0\_OUT 5

[ 26](esp32s2-gpio-sigmap_8h.md#aa4a67a38b97a3d466783c0617aa6a0c8)#define ESP\_SPICS1\_OUT 6

[ 27](esp32s2-gpio-sigmap_8h.md#ade124a5a82af0f49b122b32d69ee8d04)#define ESP\_SPID4\_IN 7

[ 28](esp32s2-gpio-sigmap_8h.md#a9bd0335c81e6828a5da77af387fbe845)#define ESP\_SPID4\_OUT 7

[ 29](esp32s2-gpio-sigmap_8h.md#ae8fa56cbc73756ff3895a937ab1374c2)#define ESP\_SPID5\_IN 8

[ 30](esp32s2-gpio-sigmap_8h.md#a61317dd1e2daf50f35240fd561180628)#define ESP\_SPID5\_OUT 8

[ 31](esp32s2-gpio-sigmap_8h.md#a2d850da0ce491f0049b9920cde48907e)#define ESP\_SPID6\_IN 9

[ 32](esp32s2-gpio-sigmap_8h.md#a918e6203f9d52d8d2606616a938faea8)#define ESP\_SPID6\_OUT 9

[ 33](esp32s2-gpio-sigmap_8h.md#a78073d0d570a71824e00bebe4bbd97d1)#define ESP\_SPID7\_IN 10

[ 34](esp32s2-gpio-sigmap_8h.md#a0802cd16128bd289444b670a827d0d31)#define ESP\_SPID7\_OUT 10

[ 35](esp32s2-gpio-sigmap_8h.md#ae891264c3a0289dad5851d44b18707d2)#define ESP\_SPIDQS\_IN 11

[ 36](esp32s2-gpio-sigmap_8h.md#a88309f7b84da7f6e461139ad137cfb97)#define ESP\_SPIDQS\_OUT 11

[ 37](esp32s2-gpio-sigmap_8h.md#aca502efa55ce2286dc9eba28192681fd)#define ESP\_U0RXD\_IN 14

[ 38](esp32s2-gpio-sigmap_8h.md#af1e58fb8e7ef86a92171eca7bb1671af)#define ESP\_U0TXD\_OUT 14

[ 39](esp32s2-gpio-sigmap_8h.md#a530d7a918a97cd1fff1acf2f90edd4ca)#define ESP\_U0CTS\_IN 15

[ 40](esp32s2-gpio-sigmap_8h.md#a4257bbc044af6ea3612313e3a0b7e7c9)#define ESP\_U0RTS\_OUT 15

[ 41](esp32s2-gpio-sigmap_8h.md#a53e3a4557a4eb1f7f98250abef03c02a)#define ESP\_U0DSR\_IN 16

[ 42](esp32s2-gpio-sigmap_8h.md#acc8716af947169c9f167bdf215c5314c)#define ESP\_U0DTR\_OUT 16

[ 43](esp32s2-gpio-sigmap_8h.md#a2293e0646e0ad2f76d62f76425ae6770)#define ESP\_U1RXD\_IN 17

[ 44](esp32s2-gpio-sigmap_8h.md#a6053b38147e28e3a7479b38e7d195136)#define ESP\_U1TXD\_OUT 17

[ 45](esp32s2-gpio-sigmap_8h.md#a3c005e616da21a058960d6aed79427b3)#define ESP\_U1CTS\_IN 18

[ 46](esp32s2-gpio-sigmap_8h.md#a8f6399745566bd5caa2020e4dcb2bb3b)#define ESP\_U1RTS\_OUT 18

[ 47](esp32s2-gpio-sigmap_8h.md#a5f29b138691540598d0b977dc4bd5971)#define ESP\_U1DSR\_IN 21

[ 48](esp32s2-gpio-sigmap_8h.md#a1f7df042d40ec6f20b559ef6778d7497)#define ESP\_U1DTR\_OUT 21

[ 49](esp32s2-gpio-sigmap_8h.md#af0b9626d6b7cfd5b5c42a8127897d565)#define ESP\_I2S0O\_BCK\_IN 23

[ 50](esp32s2-gpio-sigmap_8h.md#a2e76c532bd75a6af4790b30f58c4b8e9)#define ESP\_I2S0O\_BCK\_OUT 23

[ 51](esp32s2-gpio-sigmap_8h.md#aad13d05d8d50227859d484deaaf6e34b)#define ESP\_I2S0O\_WS\_IN 25

[ 52](esp32s2-gpio-sigmap_8h.md#a78693c10e4ac17973e7ac12c1bdf8c97)#define ESP\_I2S0O\_WS\_OUT 25

[ 53](esp32s2-gpio-sigmap_8h.md#a67905afbcda699d20d8a05a8a66411af)#define ESP\_I2S0I\_BCK\_IN 27

[ 54](esp32s2-gpio-sigmap_8h.md#abe571a9bad2c0e95049afd8e67c8d158)#define ESP\_I2S0I\_BCK\_OUT 27

[ 55](esp32s2-gpio-sigmap_8h.md#a4236f62ac75d5f2d56f7b1cc941d7509)#define ESP\_I2S0I\_WS\_IN 28

[ 56](esp32s2-gpio-sigmap_8h.md#af039bdc8eec9ec95d3ed2bbebabb22cb)#define ESP\_I2S0I\_WS\_OUT 28

[ 57](esp32s2-gpio-sigmap_8h.md#ab607ce367da34ab0f1bd7fa648273cf1)#define ESP\_I2CEXT0\_SCL\_IN 29

[ 58](esp32s2-gpio-sigmap_8h.md#a2144cc62df795547ccf2bbe3ee4c629f)#define ESP\_I2CEXT0\_SCL\_OUT 29

[ 59](esp32s2-gpio-sigmap_8h.md#afa7061c87135b9dabe5c54f5f4ce16e6)#define ESP\_I2CEXT0\_SDA\_IN 30

[ 60](esp32s2-gpio-sigmap_8h.md#aabf1378b0ad2028c36c3bb74c81d7049)#define ESP\_I2CEXT0\_SDA\_OUT 30

[ 61](esp32s2-gpio-sigmap_8h.md#aac3529b76d29e57ad20500c9d1da23f3)#define ESP\_SDIO\_TOHOST\_INT\_OUT 31

[ 62](esp32s2-gpio-sigmap_8h.md#a47d854bfae0f88dc023613e61e6be551)#define ESP\_GPIO\_BT\_ACTIVE 37

[ 63](esp32s2-gpio-sigmap_8h.md#ab8d0a9090c64518af59274603f035042)#define ESP\_GPIO\_BT\_PRIORITY 38

[ 64](esp32s2-gpio-sigmap_8h.md#acf123456a5b9d94f370309ad39672e34)#define ESP\_PCNT\_SIG\_CH0\_IN0 39

[ 65](esp32s2-gpio-sigmap_8h.md#adf2824b1611032a81fe7b3c41253c0d8)#define ESP\_GPIO\_WLAN\_PRIO 39

[ 66](esp32s2-gpio-sigmap_8h.md#a800813b2c23f7e4bb23e032e0802a459)#define ESP\_PCNT\_SIG\_CH1\_IN0 40

[ 67](esp32s2-gpio-sigmap_8h.md#af675ca03172d2dcee1e19ccb5236e087)#define ESP\_GPIO\_WLAN\_ACTIVE 40

[ 68](esp32s2-gpio-sigmap_8h.md#a7e3c939b0b32332a35f0bead0aa4a2a6)#define ESP\_PCNT\_CTRL\_CH0\_IN0 41

[ 69](esp32s2-gpio-sigmap_8h.md#a304bc90cc758f90f6675fea611ab0cfe)#define ESP\_BB\_DIAG0 41

[ 70](esp32s2-gpio-sigmap_8h.md#a88c5eb5c7f4169ce3e7f7056b42989a7)#define ESP\_PCNT\_CTRL\_CH1\_IN0 42

[ 71](esp32s2-gpio-sigmap_8h.md#ad236bf991329914d59c194ff9003974a)#define ESP\_BB\_DIAG1 42

[ 72](esp32s2-gpio-sigmap_8h.md#a99db3d1c4e07e11fc09a4024a54fcea6)#define ESP\_PCNT\_SIG\_CH0\_IN1 43

[ 73](esp32s2-gpio-sigmap_8h.md#a26c20261a5e2f4293b81c802a0a33b19)#define ESP\_BB\_DIAG2 43

[ 74](esp32s2-gpio-sigmap_8h.md#a730113779d69ca86b257060678f8cbec)#define ESP\_PCNT\_SIG\_CH1\_IN1 44

[ 75](esp32s2-gpio-sigmap_8h.md#a5124ef75b703e7805bccd8c93828faae)#define ESP\_BB\_DIAG3 44

[ 76](esp32s2-gpio-sigmap_8h.md#a9ec8d490316b9f043fe5e9160a7cf7e0)#define ESP\_PCNT\_CTRL\_CH0\_IN1 45

[ 77](esp32s2-gpio-sigmap_8h.md#aebd2c37b71d18967bd394b32c820647f)#define ESP\_BB\_DIAG4 45

[ 78](esp32s2-gpio-sigmap_8h.md#a0bbfffdef085eb6cedc3d1232766cb38)#define ESP\_PCNT\_CTRL\_CH1\_IN1 46

[ 79](esp32s2-gpio-sigmap_8h.md#ace166b18a74fb8a42f876d1aa7cfb059)#define ESP\_BB\_DIAG5 46

[ 80](esp32s2-gpio-sigmap_8h.md#a4f9e798a260fb6ac4c39262f20253244)#define ESP\_PCNT\_SIG\_CH0\_IN2 47

[ 81](esp32s2-gpio-sigmap_8h.md#ad5685b19c170cc428cea0ee91f9155b0)#define ESP\_BB\_DIAG6 47

[ 82](esp32s2-gpio-sigmap_8h.md#a38365b3f9a2b49ef2714c38d00d293c5)#define ESP\_PCNT\_SIG\_CH1\_IN2 48

[ 83](esp32s2-gpio-sigmap_8h.md#aedf32208932dfe4471f6a5a7feb652f8)#define ESP\_BB\_DIAG7 48

[ 84](esp32s2-gpio-sigmap_8h.md#a540cbfcd205911955effcc9814f9707c)#define ESP\_PCNT\_CTRL\_CH0\_IN2 49

[ 85](esp32s2-gpio-sigmap_8h.md#a126e2108473183890c6a2e148f8fd2c7)#define ESP\_BB\_DIAG8 49

[ 86](esp32s2-gpio-sigmap_8h.md#abf6c210e19582b06e3d6c546a009ef5b)#define ESP\_PCNT\_CTRL\_CH1\_IN2 50

[ 87](esp32s2-gpio-sigmap_8h.md#a75b60b1b4d53e6fca02b3a4f14ea530e)#define ESP\_BB\_DIAG9 50

[ 88](esp32s2-gpio-sigmap_8h.md#acd8d20d89508b532a4e2749499263de3)#define ESP\_PCNT\_SIG\_CH0\_IN3 51

[ 89](esp32s2-gpio-sigmap_8h.md#aed67caee00b7ceaaaa33b2917aba60f2)#define ESP\_BB\_DIAG10 51

[ 90](esp32s2-gpio-sigmap_8h.md#ac54a606ee7096db15cdb9453b04ac72d)#define ESP\_PCNT\_SIG\_CH1\_IN3 52

[ 91](esp32s2-gpio-sigmap_8h.md#aef4bb5d62b93dfc3f2834404b6945b90)#define ESP\_BB\_DIAG11 52

[ 92](esp32s2-gpio-sigmap_8h.md#a96e8bd4584ab671a1b0c3f0adb440943)#define ESP\_PCNT\_CTRL\_CH0\_IN3 53

[ 93](esp32s2-gpio-sigmap_8h.md#acc6cd70ce139a5639022bec896a3ba5e)#define ESP\_BB\_DIAG12 53

[ 94](esp32s2-gpio-sigmap_8h.md#a0a926d350fc11d737b545c53b3ba1671)#define ESP\_PCNT\_CTRL\_CH1\_IN3 54

[ 95](esp32s2-gpio-sigmap_8h.md#afa72089303bf662a4efc8c068b157f0d)#define ESP\_BB\_DIAG13 54

[ 96](esp32s2-gpio-sigmap_8h.md#a4ef00458e2547f7141741191b92854d8)#define ESP\_BB\_DIAG14 55

[ 97](esp32s2-gpio-sigmap_8h.md#aed7c06883c6a69303a341454aff409ed)#define ESP\_BB\_DIAG15 56

[ 98](esp32s2-gpio-sigmap_8h.md#a1acc29dd7c0517c30299e71c1a6ce7fa)#define ESP\_BB\_DIAG16 57

[ 99](esp32s2-gpio-sigmap_8h.md#a9abbf3178088e44d984b088f53c25ab1)#define ESP\_BB\_DIAG17 58

[ 100](esp32s2-gpio-sigmap_8h.md#af75798fba81841339510ecc5f94e542e)#define ESP\_BB\_DIAG18 59

[ 101](esp32s2-gpio-sigmap_8h.md#a4102e08a6e29f2164f5aafa109ab734b)#define ESP\_BB\_DIAG19 60

[ 102](esp32s2-gpio-sigmap_8h.md#a7c2bcf73d61315a0d8c71d68173f9860)#define ESP\_USB\_EXTPHY\_VP 61

[ 103](esp32s2-gpio-sigmap_8h.md#a28f381128449aed0ae738516df39790c)#define ESP\_USB\_EXTPHY\_OEN 61

[ 104](esp32s2-gpio-sigmap_8h.md#aeaa130d2e220f2ebd073983921ad3679)#define ESP\_USB\_EXTPHY\_VM 62

[ 105](esp32s2-gpio-sigmap_8h.md#aedb10271abe4c1969eefbc0425681652)#define ESP\_USB\_EXTPHY\_SPEED 62

[ 106](esp32s2-gpio-sigmap_8h.md#a095d83d616afb08c4b06d82c4d907fee)#define ESP\_USB\_EXTPHY\_RCV 63

[ 107](esp32s2-gpio-sigmap_8h.md#a88c6a9f957332dac96360dd3f631e59b)#define ESP\_USB\_EXTPHY\_VPO 63

[ 108](esp32s2-gpio-sigmap_8h.md#a22582585ff59bc29c3e011c4d869b1b8)#define ESP\_USB\_OTG\_IDDIG\_IN 64

[ 109](esp32s2-gpio-sigmap_8h.md#abaeb7b2bb8208db93655b442293976aa)#define ESP\_USB\_EXTPHY\_VMO 64

[ 110](esp32s2-gpio-sigmap_8h.md#a4d0c408fedb6ba35298c1398eccaa4e2)#define ESP\_USB\_OTG\_AVALID\_IN 65

[ 111](esp32s2-gpio-sigmap_8h.md#a301551d0d524f785b3d0e2c35bc81ce5)#define ESP\_USB\_EXTPHY\_SUSPND 65

[ 112](esp32s2-gpio-sigmap_8h.md#aaafaee30be8e3fed2eb1117ce381dd37)#define ESP\_USB\_SRP\_BVALID\_IN 66

[ 113](esp32s2-gpio-sigmap_8h.md#ab7335ddb7641fb62231adf289a7a74a8)#define ESP\_USB\_OTG\_IDPULLUP 66

[ 114](esp32s2-gpio-sigmap_8h.md#a4e3bd2577c74b857a74f1c367a235bad)#define ESP\_USB\_OTG\_VBUSVALID\_IN 67

[ 115](esp32s2-gpio-sigmap_8h.md#a04c49eae7bb25687d76a810ab6468353)#define ESP\_USB\_OTG\_DPPULLDOWN 67

[ 116](esp32s2-gpio-sigmap_8h.md#a8601c4fb546ff39782c0fbb14e68bfbd)#define ESP\_USB\_SRP\_SESSEND\_IN 68

[ 117](esp32s2-gpio-sigmap_8h.md#a852717f88ddb411d5b0dc49a3be83282)#define ESP\_USB\_OTG\_DMPULLDOWN 68

[ 118](esp32s2-gpio-sigmap_8h.md#a6f79de1e3bbc3758362426eecad93d3d)#define ESP\_USB\_OTG\_DRVVBUS 69

[ 119](esp32s2-gpio-sigmap_8h.md#a49b28cbc76c15cd1395f3b2e1a6ac4d9)#define ESP\_USB\_SRP\_CHRGVBUS 70

[ 120](esp32s2-gpio-sigmap_8h.md#a30f3abf038b27fa16a82bdf413eff14c)#define ESP\_USB\_SRP\_DISCHRGVBUS 71

[ 121](esp32s2-gpio-sigmap_8h.md#a0bff2051090f5eaea7edd6e9b4725a3c)#define ESP\_SPI3\_CLK\_IN 72

[ 122](esp32s2-gpio-sigmap_8h.md#ad58fe98667e0bc1b79849a7a974a8157)#define ESP\_SPI3\_CLK\_OUT\_MUX 72

[ 123](esp32s2-gpio-sigmap_8h.md#a05a9a2e5983b7895ca1fb05e5cd34709)#define ESP\_SPI3\_Q\_IN 73

[ 124](esp32s2-gpio-sigmap_8h.md#a6656c910c99e3de854064f4df24faa2d)#define ESP\_SPI3\_Q\_OUT 73

[ 125](esp32s2-gpio-sigmap_8h.md#ae7cf1730786ba95580b91b00066d3e25)#define ESP\_SPI3\_D\_IN 74

[ 126](esp32s2-gpio-sigmap_8h.md#aff4a1289beb94c9e23d7c1dd13d71d83)#define ESP\_SPI3\_D\_OUT 74

[ 127](esp32s2-gpio-sigmap_8h.md#a84dd16599428fb4c3da12c221219af40)#define ESP\_SPI3\_HD\_IN 75

[ 128](esp32s2-gpio-sigmap_8h.md#a73457a024aa63c16c2a5ef8ada2bf8b2)#define ESP\_SPI3\_HD\_OUT 75

[ 129](esp32s2-gpio-sigmap_8h.md#a485eded26f1b4bd7f03d916dcd4b0753)#define ESP\_SPI3\_CS0\_IN 76

[ 130](esp32s2-gpio-sigmap_8h.md#a8fc990a73f8fdc8d1004b3dad676a224)#define ESP\_SPI3\_CS0\_OUT 76

[ 131](esp32s2-gpio-sigmap_8h.md#a7f06d2db560a8cd511c9189cd6ed8980)#define ESP\_SPI3\_CS1\_OUT 77

[ 132](esp32s2-gpio-sigmap_8h.md#a9e4bf0b0eff43b1f56f17abe22ef24a5)#define ESP\_SPI3\_CS2\_OUT 78

[ 133](esp32s2-gpio-sigmap_8h.md#a62dfcd88747c61acb53dc85c1751f1d3)#define ESP\_LEDC\_LS\_SIG\_OUT0 79

[ 134](esp32s2-gpio-sigmap_8h.md#a5cad9206cfeea93b42e5456228c7d580)#define ESP\_LEDC\_LS\_SIG\_OUT1 80

[ 135](esp32s2-gpio-sigmap_8h.md#ab408070e7c700805db165c3876b6c588)#define ESP\_LEDC\_LS\_SIG\_OUT2 81

[ 136](esp32s2-gpio-sigmap_8h.md#a438aee217c6c94a2962a3d98935b5717)#define ESP\_LEDC\_LS\_SIG\_OUT3 82

[ 137](esp32s2-gpio-sigmap_8h.md#ad9bae9b4884a356e465656d1ee8d61cd)#define ESP\_RMT\_SIG\_IN0 83

[ 138](esp32s2-gpio-sigmap_8h.md#ada93dcffffc15362be4b7432a8033559)#define ESP\_LEDC\_LS\_SIG\_OUT4 83

[ 139](esp32s2-gpio-sigmap_8h.md#ab6c6293e6845ba4bf4d05b84102ffdcf)#define ESP\_RMT\_SIG\_IN1 84

[ 140](esp32s2-gpio-sigmap_8h.md#a34fc029ec45756ca7064580f57db1cc7)#define ESP\_LEDC\_LS\_SIG\_OUT5 84

[ 141](esp32s2-gpio-sigmap_8h.md#af88ebdd0d2d02ac58d720c001ccc155b)#define ESP\_RMT\_SIG\_IN2 85

[ 142](esp32s2-gpio-sigmap_8h.md#a28b01adea7e0bcc8b76fe05d58c1cbd0)#define ESP\_LEDC\_LS\_SIG\_OUT6 85

[ 143](esp32s2-gpio-sigmap_8h.md#a1f930cd82690248b839f16ff7738f32c)#define ESP\_RMT\_SIG\_IN3 86

[ 144](esp32s2-gpio-sigmap_8h.md#a2ea140f2da1a15b24dcaa3592909ca35)#define ESP\_LEDC\_LS\_SIG\_OUT7 86

[ 145](esp32s2-gpio-sigmap_8h.md#a25343fbc20a0c542bcdc21cdfade867b)#define ESP\_RMT\_SIG\_OUT0 87

[ 146](esp32s2-gpio-sigmap_8h.md#a6d082fb1c7397d784a3075108e0dea73)#define ESP\_RMT\_SIG\_OUT1 88

[ 147](esp32s2-gpio-sigmap_8h.md#ad657c1ddcf9c335ac7876464b80b2705)#define ESP\_RMT\_SIG\_OUT2 89

[ 148](esp32s2-gpio-sigmap_8h.md#ae60033bb70ca9ff7c2b52368d24a8ab8)#define ESP\_RMT\_SIG\_OUT3 90

[ 149](esp32s2-gpio-sigmap_8h.md#ae49b4527d8fbd0f5c8e3edc72704c54a)#define ESP\_EXT\_ADC\_START 93

[ 150](esp32s2-gpio-sigmap_8h.md#a1b6324b294e9e018a5909427f4f0ba36)#define ESP\_I2CEXT1\_SCL\_IN 95

[ 151](esp32s2-gpio-sigmap_8h.md#a3ac49ff21fcb59eeab6350821f9107e5)#define ESP\_I2CEXT1\_SCL\_OUT 95

[ 152](esp32s2-gpio-sigmap_8h.md#abb571ec9f2a59fc281837ca8bd3f2daa)#define ESP\_I2CEXT1\_SDA\_IN 96

[ 153](esp32s2-gpio-sigmap_8h.md#a3922109459dfd033147e4daf1ed4cd32)#define ESP\_I2CEXT1\_SDA\_OUT 96

[ 154](esp32s2-gpio-sigmap_8h.md#ae59035f8269ccd564ba0d7b2b078b3ee)#define ESP\_GPIO\_SD0\_OUT 100

[ 155](esp32s2-gpio-sigmap_8h.md#a3fbed77581ed14fa077f314e812b9c36)#define ESP\_GPIO\_SD1\_OUT 101

[ 156](esp32s2-gpio-sigmap_8h.md#a2668d9083ce28563cc160fe1102e927d)#define ESP\_GPIO\_SD2\_OUT 102

[ 157](esp32s2-gpio-sigmap_8h.md#a9d34f616894f98d7175c41b4ba565f8d)#define ESP\_GPIO\_SD3\_OUT 103

[ 158](esp32s2-gpio-sigmap_8h.md#aa88cedc2785b1e25a21ac70dd5603e68)#define ESP\_GPIO\_SD4\_OUT 104

[ 159](esp32s2-gpio-sigmap_8h.md#af0841a01cf24e79a447daa58a48db9f8)#define ESP\_GPIO\_SD5\_OUT 105

[ 160](esp32s2-gpio-sigmap_8h.md#a8c16952c92f5b28cd39b99771ccb983b)#define ESP\_GPIO\_SD6\_OUT 106

[ 161](esp32s2-gpio-sigmap_8h.md#a7fd22ae53413e708e4b75ad57e1be34a)#define ESP\_GPIO\_SD7\_OUT 107

[ 162](esp32s2-gpio-sigmap_8h.md#ade88988460c131e8c6775794588b0eb8)#define ESP\_FSPICLK\_IN 108

[ 163](esp32s2-gpio-sigmap_8h.md#a2054f4af1d18ebb83d9e3439a1b9326e)#define ESP\_FSPICLK\_OUT\_MUX 108

[ 164](esp32s2-gpio-sigmap_8h.md#ab603b7bf7d016e85653a5c3be5c01293)#define ESP\_FSPIQ\_IN 109

[ 165](esp32s2-gpio-sigmap_8h.md#a8b3ea6ad374fa010b46b48072fa87ccb)#define ESP\_FSPIQ\_OUT 109

[ 166](esp32s2-gpio-sigmap_8h.md#a7910521af840d42edd3c0a667cf90c5f)#define ESP\_FSPID\_IN 110

[ 167](esp32s2-gpio-sigmap_8h.md#a02bd34821e8a4bf0038b9af417ec161a)#define ESP\_FSPID\_OUT 110

[ 168](esp32s2-gpio-sigmap_8h.md#a60ff087a3d85a356d77f060a6698d00b)#define ESP\_FSPIHD\_IN 111

[ 169](esp32s2-gpio-sigmap_8h.md#ac71bc137b93bd6c0c8a1ebe24a70a613)#define ESP\_FSPIHD\_OUT 111

[ 170](esp32s2-gpio-sigmap_8h.md#a4d4c4a13b820cab6d94da8fe08120a2f)#define ESP\_FSPIWP\_IN 112

[ 171](esp32s2-gpio-sigmap_8h.md#a83c4f18d726984cc98caeea9b7677ca1)#define ESP\_FSPIWP\_OUT 112

[ 172](esp32s2-gpio-sigmap_8h.md#af751015894fa1cefd780d4c483ed4fe0)#define ESP\_FSPIIO4\_IN 113

[ 173](esp32s2-gpio-sigmap_8h.md#a5131d3b8c5f15927eb1ab5f5c5831fc7)#define ESP\_FSPIIO4\_OUT 113

[ 174](esp32s2-gpio-sigmap_8h.md#aa422ee46d7a699a5de5acfce23544f1b)#define ESP\_FSPIIO5\_IN 114

[ 175](esp32s2-gpio-sigmap_8h.md#a846120bb034a5178b719de7566af36e9)#define ESP\_FSPIIO5\_OUT 114

[ 176](esp32s2-gpio-sigmap_8h.md#afbba101fa32685cf54ff6579245c232b)#define ESP\_FSPIIO6\_IN 115

[ 177](esp32s2-gpio-sigmap_8h.md#acb72c9ac62375b2ef22c4895fd5c37e9)#define ESP\_FSPIIO6\_OUT 115

[ 178](esp32s2-gpio-sigmap_8h.md#a7be0c3215d8ab00a4a87dcf4798207d9)#define ESP\_FSPIIO7\_IN 116

[ 179](esp32s2-gpio-sigmap_8h.md#a796dc85ea60a5cce0d0c184805164587)#define ESP\_FSPIIO7\_OUT 116

[ 180](esp32s2-gpio-sigmap_8h.md#a96ca1328e76337d289f6e65faf33d75c)#define ESP\_FSPICS0\_IN 117

[ 181](esp32s2-gpio-sigmap_8h.md#ad1be1401b282275eaef46b9a598c6a40)#define ESP\_FSPICS0\_OUT 117

[ 182](esp32s2-gpio-sigmap_8h.md#a44ade9179a7ea00586359a009799661d)#define ESP\_FSPICS1\_OUT 118

[ 183](esp32s2-gpio-sigmap_8h.md#af991963f29c5b268a5f8fead8fd15348)#define ESP\_FSPICS2\_OUT 119

[ 184](esp32s2-gpio-sigmap_8h.md#a65d1170c5a68ac7f6a4457c3380ddfde)#define ESP\_FSPICS3\_OUT 120

[ 185](esp32s2-gpio-sigmap_8h.md#a83dafe68703c701dcd07d7ff0aadad01)#define ESP\_FSPICS4\_OUT 121

[ 186](esp32s2-gpio-sigmap_8h.md#ad8fab64bb220fd198a6cd931f4ea1e8e)#define ESP\_FSPICS5\_OUT 122

[ 187](esp32s2-gpio-sigmap_8h.md#ab3da303c2f9226f9648669c17af8377a)#define ESP\_TWAI\_RX 123

[ 188](esp32s2-gpio-sigmap_8h.md#a3b13bb40583aaa0f85de982509247614)#define ESP\_TWAI\_TX 123

[ 189](esp32s2-gpio-sigmap_8h.md#a6d0d41d1ec0f6fc626861f5857684e6d)#define ESP\_TWAI\_BUS\_OFF\_ON 124

[ 190](esp32s2-gpio-sigmap_8h.md#a1c69791269fdbb2a11f66f33eb4066be)#define ESP\_TWAI\_CLKOUT 125

[ 191](esp32s2-gpio-sigmap_8h.md#a0651dd050ec01b150a74bb1f8db2221f)#define ESP\_SUBSPICLK\_OUT\_MUX 126

[ 192](esp32s2-gpio-sigmap_8h.md#af80ecb5fcd6c02cb5b73478198abef3c)#define ESP\_SUBSPIQ\_IN 127

[ 193](esp32s2-gpio-sigmap_8h.md#ac75fd67f54d49449451c4924c0b7910a)#define ESP\_SUBSPIQ\_OUT 127

[ 194](esp32s2-gpio-sigmap_8h.md#a0c924000fccdb7ce112822db720dbd8d)#define ESP\_SUBSPID\_IN 128

[ 195](esp32s2-gpio-sigmap_8h.md#a3b9cab35f71697419266c71583f8a087)#define ESP\_SUBSPID\_OUT 128

[ 196](esp32s2-gpio-sigmap_8h.md#a9a04da28895e846359a3ea89391b21f6)#define ESP\_SUBSPIHD\_IN 129

[ 197](esp32s2-gpio-sigmap_8h.md#ab1f7e54d6230ceabc3fee083aab409d1)#define ESP\_SUBSPIHD\_OUT 129

[ 198](esp32s2-gpio-sigmap_8h.md#a3c4b2938ef6753d76a752bf9a973de52)#define ESP\_SUBSPIWP\_IN 130

[ 199](esp32s2-gpio-sigmap_8h.md#a7493ab9a1f0dc10902ce412055579842)#define ESP\_SUBSPIWP\_OUT 130

[ 200](esp32s2-gpio-sigmap_8h.md#a8925d5f830a4bc5ca6114dc06bae3b1f)#define ESP\_SUBSPICS0\_OUT 131

[ 201](esp32s2-gpio-sigmap_8h.md#add0fa80736d0fe196872bb0664c433d4)#define ESP\_SUBSPICS1\_OUT 132

[ 202](esp32s2-gpio-sigmap_8h.md#a83baa98d81f816f19e65aafb26f15a3c)#define ESP\_FSPIDQS\_OUT 133

[ 203](esp32s2-gpio-sigmap_8h.md#ac530545e4916a807a391986e544ecda6)#define ESP\_FSPI\_HSYNC\_OUT 134

[ 204](esp32s2-gpio-sigmap_8h.md#a4690fa15ab99eabd6fe2948704ad6255)#define ESP\_FSPI\_VSYNC\_OUT 135

[ 205](esp32s2-gpio-sigmap_8h.md#a68a2f09aae5e8b7d7207cc5c58b031c6)#define ESP\_FSPI\_DE\_OUT 136

[ 206](esp32s2-gpio-sigmap_8h.md#a4bd311f85d48eafbea4d0fd8cd877bc5)#define ESP\_FSPICD\_OUT 137

[ 207](esp32s2-gpio-sigmap_8h.md#a4212588a91a6a9dd44499aec13f9fe7a)#define ESP\_SPI3\_CD\_OUT 139

[ 208](esp32s2-gpio-sigmap_8h.md#aa9be8338dbdaecb13c5de0c38fbb12ab)#define ESP\_SPI3\_DQS\_OUT 140

[ 209](esp32s2-gpio-sigmap_8h.md#a433c8fb715a07f27d4b2bcea31b92129)#define ESP\_I2S0I\_DATA\_IN0 143

[ 210](esp32s2-gpio-sigmap_8h.md#a25101d2b16ca73d9e342a77f6c2fd517)#define ESP\_I2S0O\_DATA\_OUT0 143

[ 211](esp32s2-gpio-sigmap_8h.md#a8fdcb030022fc73f03b8b614ec031266)#define ESP\_I2S0I\_DATA\_IN1 144

[ 212](esp32s2-gpio-sigmap_8h.md#ac3656eb3c8ac2d66cc4f9099d486325b)#define ESP\_I2S0O\_DATA\_OUT1 144

[ 213](esp32s2-gpio-sigmap_8h.md#acb82a70ab66b67c43c3df4af940afd20)#define ESP\_I2S0I\_DATA\_IN2 145

[ 214](esp32s2-gpio-sigmap_8h.md#a87405dd9815c0e43d3dc865aa7459cae)#define ESP\_I2S0O\_DATA\_OUT2 145

[ 215](esp32s2-gpio-sigmap_8h.md#af5f006ccd7b9017a077cb19b7e8584a3)#define ESP\_I2S0I\_DATA\_IN3 146

[ 216](esp32s2-gpio-sigmap_8h.md#ad0e3c64912151b36169741ada3f5aa0b)#define ESP\_I2S0O\_DATA\_OUT3 146

[ 217](esp32s2-gpio-sigmap_8h.md#a580ec97414913d720035de8df140ce2e)#define ESP\_I2S0I\_DATA\_IN4 147

[ 218](esp32s2-gpio-sigmap_8h.md#abeb5e69293e78ceff31a7ed908864367)#define ESP\_I2S0O\_DATA\_OUT4 147

[ 219](esp32s2-gpio-sigmap_8h.md#a9d72aac34e99ec34569006dbe140f658)#define ESP\_I2S0I\_DATA\_IN5 148

[ 220](esp32s2-gpio-sigmap_8h.md#a93af307990b79a253c9be03d0831f175)#define ESP\_I2S0O\_DATA\_OUT5 148

[ 221](esp32s2-gpio-sigmap_8h.md#aed35437eb068e4ea079d8755928161c3)#define ESP\_I2S0I\_DATA\_IN6 149

[ 222](esp32s2-gpio-sigmap_8h.md#ace1b34e6050863a54792e6ac3c965ab8)#define ESP\_I2S0O\_DATA\_OUT6 149

[ 223](esp32s2-gpio-sigmap_8h.md#a0a04fda280abc577acf3e20d7a917cc8)#define ESP\_I2S0I\_DATA\_IN7 150

[ 224](esp32s2-gpio-sigmap_8h.md#a789d483001496ba193846e90fcc70e74)#define ESP\_I2S0O\_DATA\_OUT7 150

[ 225](esp32s2-gpio-sigmap_8h.md#ae144f14b04fff35537effc847a2a6520)#define ESP\_I2S0I\_DATA\_IN8 151

[ 226](esp32s2-gpio-sigmap_8h.md#a8360e859e714712978c0108b2fd7f8b3)#define ESP\_I2S0O\_DATA\_OUT8 151

[ 227](esp32s2-gpio-sigmap_8h.md#a54b5575c98e2b363e1cfd556421788d5)#define ESP\_I2S0I\_DATA\_IN9 152

[ 228](esp32s2-gpio-sigmap_8h.md#a0f347fca42d8d9e9bbf1f46a8c05ee84)#define ESP\_I2S0O\_DATA\_OUT9 152

[ 229](esp32s2-gpio-sigmap_8h.md#a36fd66f4834eb96ba5f1ab7560230065)#define ESP\_I2S0I\_DATA\_IN10 153

[ 230](esp32s2-gpio-sigmap_8h.md#a789443eb05c68f28a9fa99ff43bd3aa4)#define ESP\_I2S0O\_DATA\_OUT10 153

[ 231](esp32s2-gpio-sigmap_8h.md#a601911b70e67c09b0bee13be965ea023)#define ESP\_I2S0I\_DATA\_IN11 154

[ 232](esp32s2-gpio-sigmap_8h.md#ac8c4f8238d7ac8d3610ad7d817b59f0c)#define ESP\_I2S0O\_DATA\_OUT11 154

[ 233](esp32s2-gpio-sigmap_8h.md#a1d6581f56d31224a7fe2b2767c815e17)#define ESP\_I2S0I\_DATA\_IN12 155

[ 234](esp32s2-gpio-sigmap_8h.md#a1817a5bb7d7c6f81189d61844c9369d8)#define ESP\_I2S0O\_DATA\_OUT12 155

[ 235](esp32s2-gpio-sigmap_8h.md#a429e25483385ad62fb5d25e25ab16bd1)#define ESP\_I2S0I\_DATA\_IN13 156

[ 236](esp32s2-gpio-sigmap_8h.md#a4315e0aa620576457d3fe5543daf8a74)#define ESP\_I2S0O\_DATA\_OUT13 156

[ 237](esp32s2-gpio-sigmap_8h.md#ac9a9df57a89820c2eb0f3af2ca49fc71)#define ESP\_I2S0I\_DATA\_IN14 157

[ 238](esp32s2-gpio-sigmap_8h.md#a60cd35bc47b224db197844526ed31562)#define ESP\_I2S0O\_DATA\_OUT14 157

[ 239](esp32s2-gpio-sigmap_8h.md#a1c65e11dbd846847daad7fc716955e64)#define ESP\_I2S0I\_DATA\_IN15 158

[ 240](esp32s2-gpio-sigmap_8h.md#a39a667893007777d45fdcf3c9df17441)#define ESP\_I2S0O\_DATA\_OUT15 158

[ 241](esp32s2-gpio-sigmap_8h.md#a5f6c0a7cf37eec066127d6cfc6fc8558)#define ESP\_I2S0O\_DATA\_OUT16 159

[ 242](esp32s2-gpio-sigmap_8h.md#aaa92d37d180f429df167101a6bcde85f)#define ESP\_I2S0O\_DATA\_OUT17 160

[ 243](esp32s2-gpio-sigmap_8h.md#a1f4f2d0a3535c025d6581e4232bb7fd9)#define ESP\_I2S0O\_DATA\_OUT18 161

[ 244](esp32s2-gpio-sigmap_8h.md#a6676ad67342db70105683dddae6259a2)#define ESP\_I2S0O\_DATA\_OUT19 162

[ 245](esp32s2-gpio-sigmap_8h.md#a2d1be2072be7af3e41d25928de743b6e)#define ESP\_I2S0O\_DATA\_OUT20 163

[ 246](esp32s2-gpio-sigmap_8h.md#a934a97b4ba3f7729b93828fbcfe31c93)#define ESP\_I2S0O\_DATA\_OUT21 164

[ 247](esp32s2-gpio-sigmap_8h.md#a30d03be995708ac60420d0199d8b2b67)#define ESP\_I2S0O\_DATA\_OUT22 165

[ 248](esp32s2-gpio-sigmap_8h.md#a4fa877e0f38365b7f18fe4cb04c865a6)#define ESP\_I2S0O\_DATA\_OUT23 166

[ 249](esp32s2-gpio-sigmap_8h.md#aae7066cb62b74cf5e8f64f84bd76ee49)#define ESP\_SUBSPID4\_IN 167

[ 250](esp32s2-gpio-sigmap_8h.md#aa716d46da29da6affd5fa8851a730f3f)#define ESP\_SUBSPID4\_OUT 167

[ 251](esp32s2-gpio-sigmap_8h.md#a051cd2450520fd4abc6f288c8577a12c)#define ESP\_SUBSPID5\_IN 168

[ 252](esp32s2-gpio-sigmap_8h.md#aece7dc6fc4bca1bd73d9ba856eb0f3fe)#define ESP\_SUBSPID5\_OUT 168

[ 253](esp32s2-gpio-sigmap_8h.md#a6d49162b17a1a7cd3f2446c6ca8192ec)#define ESP\_SUBSPID6\_IN 169

[ 254](esp32s2-gpio-sigmap_8h.md#ab3e8db3219bf7aa7b2503a1fe759d60c)#define ESP\_SUBSPID6\_OUT 169

[ 255](esp32s2-gpio-sigmap_8h.md#a34b9a22e0f55a0534199e62b1eaff5b0)#define ESP\_SUBSPID7\_IN 170

[ 256](esp32s2-gpio-sigmap_8h.md#adb8c01bf2361a8b24e79cf048a7e6535)#define ESP\_SUBSPID7\_OUT 170

[ 257](esp32s2-gpio-sigmap_8h.md#a6ccb6e41ab48fba76302068ee4433fb8)#define ESP\_SUBSPIDQS\_IN 171

[ 258](esp32s2-gpio-sigmap_8h.md#a608345dcd6c90e4f19427bb38161501a)#define ESP\_SUBSPIDQS\_OUT 171

[ 259](esp32s2-gpio-sigmap_8h.md#aee6979fc359bc990dac8c49371243697)#define ESP\_I2S0I\_H\_SYNC 193

[ 260](esp32s2-gpio-sigmap_8h.md#a99829d36ae815041479b1327a03c9f0a)#define ESP\_I2S0I\_V\_SYNC 194

[ 261](esp32s2-gpio-sigmap_8h.md#a933b9ae19e0f6cc02bdb202f7cd95b8c)#define ESP\_I2S0I\_H\_ENABLE 195

[ 262](esp32s2-gpio-sigmap_8h.md#a0ad409b608ef2a418098b4e51d0e7e9a)#define ESP\_PCMFSYNC\_IN 203

[ 263](esp32s2-gpio-sigmap_8h.md#afd2befcf5eb0c413c0f8447558dc4863)#define ESP\_BT\_AUDIO0\_IRQ 203

[ 264](esp32s2-gpio-sigmap_8h.md#abb4d1f28362c68cf3f1e9f1696602b03)#define ESP\_PCMCLK\_IN 204

[ 265](esp32s2-gpio-sigmap_8h.md#acfe665b9ff21a51b93819a3f123180ad)#define ESP\_BT\_AUDIO1\_IRQ 204

[ 266](esp32s2-gpio-sigmap_8h.md#ae94f8dfc2be2c0cf8863a33df76d5295)#define ESP\_PCMDIN 205

[ 267](esp32s2-gpio-sigmap_8h.md#a77ac554a2a10fc6fa77106e8af9dfc86)#define ESP\_BT\_AUDIO2\_IRQ 205

[ 268](esp32s2-gpio-sigmap_8h.md#a7abc844342f6483be73ea503d3f76d89)#define ESP\_RW\_WAKEUP\_REQ 206

[ 269](esp32s2-gpio-sigmap_8h.md#ab2e25b779a18acd66533795433291a3d)#define ESP\_BLE\_AUDIO0\_IRQ 206

[ 270](esp32s2-gpio-sigmap_8h.md#ab4b3d654c674536c2c63070210147372)#define ESP\_BLE\_AUDIO1\_IRQ 207

[ 271](esp32s2-gpio-sigmap_8h.md#a637ea6fcad7b2e5fe48cf9e3419fbed6)#define ESP\_BLE\_AUDIO2\_IRQ 208

[ 272](esp32s2-gpio-sigmap_8h.md#a8b79d6e15573a684058c9b933f469f09)#define ESP\_PCMFSYNC\_OUT 209

[ 273](esp32s2-gpio-sigmap_8h.md#a500651ca0d6daa86774a0f45190f8b38)#define ESP\_PCMCLK\_OUT 210

[ 274](esp32s2-gpio-sigmap_8h.md#ab3ecd7e5557112172c38bff3b2605e9c)#define ESP\_PCMDOUT 211

[ 275](esp32s2-gpio-sigmap_8h.md#aba2aea8feedc96a0a6b3bba007df49ac)#define ESP\_BLE\_AUDIO\_SYNC0\_P 212

[ 276](esp32s2-gpio-sigmap_8h.md#a21e5bf1c7c33a39f11d8bf6537ed85bb)#define ESP\_BLE\_AUDIO\_SYNC1\_P 213

[ 277](esp32s2-gpio-sigmap_8h.md#a961f37a0b2dcb9e183331ef5684f8504)#define ESP\_BLE\_AUDIO\_SYNC2\_P 214

[ 278](esp32s2-gpio-sigmap_8h.md#aec2dfb198f69d923686404a0a6330833)#define ESP\_ANT\_SEL0 215

[ 279](esp32s2-gpio-sigmap_8h.md#a15c080ea1e4c8e2db9f1640e9b8c4f0a)#define ESP\_ANT\_SEL1 216

[ 280](esp32s2-gpio-sigmap_8h.md#ae3042ff86ecc0f2e78ebe9477055e819)#define ESP\_ANT\_SEL2 217

[ 281](esp32s2-gpio-sigmap_8h.md#ab8e5cca4b9eb1a7bda7868ecd792c76d)#define ESP\_ANT\_SEL3 218

[ 282](esp32s2-gpio-sigmap_8h.md#a821cc4b81f76043b1ecb751118a2f416)#define ESP\_ANT\_SEL4 219

[ 283](esp32s2-gpio-sigmap_8h.md#a28a954881fd9d5f5e7ff25d715f0bcc2)#define ESP\_ANT\_SEL5 220

[ 284](esp32s2-gpio-sigmap_8h.md#a2122dad1966cbe214e9c82cb9a46bd8a)#define ESP\_ANT\_SEL6 221

[ 285](esp32s2-gpio-sigmap_8h.md#a8f9cedf15c49cee3fbac2a22df7675ec)#define ESP\_ANT\_SEL7 222

[ 286](esp32s2-gpio-sigmap_8h.md#ae2b550fa907754322b00321e32da00d7)#define ESP\_SIG\_IN\_FUNC\_223 223

[ 287](esp32s2-gpio-sigmap_8h.md#ad18e273d813830572e425c4cf4abcb38)#define ESP\_SIG\_IN\_FUNC223 223

[ 288](esp32s2-gpio-sigmap_8h.md#a5022a9e30fdcf3183a1a44bd3e44496c)#define ESP\_SIG\_IN\_FUNC\_224 224

[ 289](esp32s2-gpio-sigmap_8h.md#a53d8822e6079bfdfa4f1e643af0c619e)#define ESP\_SIG\_IN\_FUNC224 224

[ 290](esp32s2-gpio-sigmap_8h.md#a8a152884133ebca3bd1d72b4f16974bc)#define ESP\_SIG\_IN\_FUNC\_225 225

[ 291](esp32s2-gpio-sigmap_8h.md#a3dc693b4e8606fc6ae6a7f576f3e5253)#define ESP\_SIG\_IN\_FUNC225 225

[ 292](esp32s2-gpio-sigmap_8h.md#adafe9a8c93ada007bf0e33a56ecdf657)#define ESP\_SIG\_IN\_FUNC\_226 226

[ 293](esp32s2-gpio-sigmap_8h.md#a358aff28052633bbaf7fd267c89310bc)#define ESP\_SIG\_IN\_FUNC226 226

[ 294](esp32s2-gpio-sigmap_8h.md#a00bccf8191e16c8fb59632b7ba63211d)#define ESP\_SIG\_IN\_FUNC\_227 227

[ 295](esp32s2-gpio-sigmap_8h.md#a5e67275e2c4feb45990232eb79856ae0)#define ESP\_SIG\_IN\_FUNC227 227

[ 296](esp32s2-gpio-sigmap_8h.md#a9023b22f85edc25ab88db9f3fb025c4e)#define ESP\_PRO\_ALONEGPIO\_IN0 235

[ 297](esp32s2-gpio-sigmap_8h.md#ae833440baa7073fbfb51ec80ff728ce5)#define ESP\_PRO\_ALONEGPIO\_OUT0 235

[ 298](esp32s2-gpio-sigmap_8h.md#a5e4c12a21678930c86e15cbb6d920767)#define ESP\_PRO\_ALONEGPIO\_IN1 236

[ 299](esp32s2-gpio-sigmap_8h.md#a5b3065b35c32286fe5ca8d68c033b162)#define ESP\_PRO\_ALONEGPIO\_OUT1 236

[ 300](esp32s2-gpio-sigmap_8h.md#a8b82dbe07c785060d2190a13e1fe21ee)#define ESP\_PRO\_ALONEGPIO\_IN2 237

[ 301](esp32s2-gpio-sigmap_8h.md#a287e800e3fb52dd3b6949e6d185f413c)#define ESP\_PRO\_ALONEGPIO\_OUT2 237

[ 302](esp32s2-gpio-sigmap_8h.md#a5f8a8f6143c1552eec5862ce248ca496)#define ESP\_PRO\_ALONEGPIO\_IN3 238

[ 303](esp32s2-gpio-sigmap_8h.md#a49f220c0a7cae6a580174355a80b2b56)#define ESP\_PRO\_ALONEGPIO\_OUT3 238

[ 304](esp32s2-gpio-sigmap_8h.md#ad8ca1006a71cdd738cca02eaf9f923d6)#define ESP\_PRO\_ALONEGPIO\_IN4 239

[ 305](esp32s2-gpio-sigmap_8h.md#ac1b762f9e0ad1cb60c1e16b0cf7aae0a)#define ESP\_PRO\_ALONEGPIO\_OUT4 239

[ 306](esp32s2-gpio-sigmap_8h.md#aa1b04ac7997451778d7fdbb4f00b0114)#define ESP\_PRO\_ALONEGPIO\_IN5 240

[ 307](esp32s2-gpio-sigmap_8h.md#a5f237780803395dd97bb8306a14dbc92)#define ESP\_PRO\_ALONEGPIO\_OUT5 240

[ 308](esp32s2-gpio-sigmap_8h.md#a525900ed7a103a14105afb6ef8caca69)#define ESP\_PRO\_ALONEGPIO\_IN6 241

[ 309](esp32s2-gpio-sigmap_8h.md#a4cbc6a3551e057f1d943b01c120317f4)#define ESP\_PRO\_ALONEGPIO\_OUT6 241

[ 310](esp32s2-gpio-sigmap_8h.md#af6ebbb44bcb763355964ac39293cd1c4)#define ESP\_PRO\_ALONEGPIO\_IN7 242

[ 311](esp32s2-gpio-sigmap_8h.md#a3d1993f51138a3ccf8ef913e1863f3bd)#define ESP\_PRO\_ALONEGPIO\_OUT7 242

[ 312](esp32s2-gpio-sigmap_8h.md#ae8f094f6bb8c6594dd56ac6365039f89)#define ESP\_CLK\_I2S\_MUX 251

[ 313](esp32s2-gpio-sigmap_8h.md#a645411759ffdc63f51f2cd42632d2720)#define ESP\_SIG\_GPIO\_OUT 256

[ 314](esp32s2-gpio-sigmap_8h.md#afe5c166b887709cdd27bd37df85c45b9)#define ESP\_GPIO\_MAP\_DATE 0x1904100

315

316#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32S2\_GPIO\_SIGMAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32s2-gpio-sigmap.h](esp32s2-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
