---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32c3-gpio-sigmap_8h_source.html
original_path: doxygen/html/esp32c3-gpio-sigmap_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c3-gpio-sigmap.h

[Go to the documentation of this file.](esp32c3-gpio-sigmap_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C3\_GPIO\_SIGMAP\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C3\_GPIO\_SIGMAP\_H\_

9

[ 10](esp32c3-gpio-sigmap_8h.md#af80260535bc3aee44c28c972a29483e0)#define ESP\_NOSIG ESP\_SIG\_INVAL

11

[ 12](esp32c3-gpio-sigmap_8h.md#aaf157f6b85a07f18b181876a7a04f142)#define ESP\_SPICLK\_OUT\_MUX ESP\_SPICLK\_OUT

[ 13](esp32c3-gpio-sigmap_8h.md#aec51ff955c6be50e529affc87ec9d5cb)#define ESP\_SPIQ\_IN 0

[ 14](esp32c3-gpio-sigmap_8h.md#a5816deeca8853397a830a8eb251704ee)#define ESP\_SPIQ\_OUT 0

[ 15](esp32c3-gpio-sigmap_8h.md#a26c603fd58dbd7526d2be3bb3e37758a)#define ESP\_SPID\_IN 1

[ 16](esp32c3-gpio-sigmap_8h.md#af81b2fc65b68ed2238ab3367a8731102)#define ESP\_SPID\_OUT 1

[ 17](esp32c3-gpio-sigmap_8h.md#a49783f877b666aff9362cf605590b991)#define ESP\_SPIHD\_IN 2

[ 18](esp32c3-gpio-sigmap_8h.md#a8851b5256482790f3304efecafc13afd)#define ESP\_SPIHD\_OUT 2

[ 19](esp32c3-gpio-sigmap_8h.md#aa74adc2812d9c6bd143c679fa4d9ca8d)#define ESP\_SPIWP\_IN 3

[ 20](esp32c3-gpio-sigmap_8h.md#a470408f8102937dc017336e320e6147b)#define ESP\_SPIWP\_OUT 3

[ 21](esp32c3-gpio-sigmap_8h.md#a5f440c922a53085bb7b28f469c2a14b0)#define ESP\_SPICLK\_OUT 4

[ 22](esp32c3-gpio-sigmap_8h.md#a5d97c07ba0d8cda594d52310e90fa6a4)#define ESP\_SPICS0\_OUT 5

[ 23](esp32c3-gpio-sigmap_8h.md#aca502efa55ce2286dc9eba28192681fd)#define ESP\_U0RXD\_IN 6

[ 24](esp32c3-gpio-sigmap_8h.md#af1e58fb8e7ef86a92171eca7bb1671af)#define ESP\_U0TXD\_OUT 6

[ 25](esp32c3-gpio-sigmap_8h.md#a530d7a918a97cd1fff1acf2f90edd4ca)#define ESP\_U0CTS\_IN 7

[ 26](esp32c3-gpio-sigmap_8h.md#a4257bbc044af6ea3612313e3a0b7e7c9)#define ESP\_U0RTS\_OUT 7

[ 27](esp32c3-gpio-sigmap_8h.md#a53e3a4557a4eb1f7f98250abef03c02a)#define ESP\_U0DSR\_IN 8

[ 28](esp32c3-gpio-sigmap_8h.md#acc8716af947169c9f167bdf215c5314c)#define ESP\_U0DTR\_OUT 8

[ 29](esp32c3-gpio-sigmap_8h.md#a2293e0646e0ad2f76d62f76425ae6770)#define ESP\_U1RXD\_IN 9

[ 30](esp32c3-gpio-sigmap_8h.md#a6053b38147e28e3a7479b38e7d195136)#define ESP\_U1TXD\_OUT 9

[ 31](esp32c3-gpio-sigmap_8h.md#a3c005e616da21a058960d6aed79427b3)#define ESP\_U1CTS\_IN 10

[ 32](esp32c3-gpio-sigmap_8h.md#a8f6399745566bd5caa2020e4dcb2bb3b)#define ESP\_U1RTS\_OUT 10

[ 33](esp32c3-gpio-sigmap_8h.md#a5f29b138691540598d0b977dc4bd5971)#define ESP\_U1DSR\_IN 11

[ 34](esp32c3-gpio-sigmap_8h.md#a1f7df042d40ec6f20b559ef6778d7497)#define ESP\_U1DTR\_OUT 11

[ 35](esp32c3-gpio-sigmap_8h.md#a0c2eefdd5846623d330a6437ecfec3ef)#define ESP\_I2S\_MCLK\_IN 12

[ 36](esp32c3-gpio-sigmap_8h.md#a89708f46a7a1e03c9a654e9a529ec36c)#define ESP\_I2S\_MCLK\_OUT 12

[ 37](esp32c3-gpio-sigmap_8h.md#aa4d5f8ce3cc15e7ab7b2d17c79da3b91)#define ESP\_I2SO\_BCK\_IN 13

[ 38](esp32c3-gpio-sigmap_8h.md#ab586cc1b4ae5da20703f469bb8ff5c0e)#define ESP\_I2SO\_BCK\_OUT 13

[ 39](esp32c3-gpio-sigmap_8h.md#a2f5d7f663b568a4a609f8c9315f6cf5c)#define ESP\_I2SO\_WS\_IN 14

[ 40](esp32c3-gpio-sigmap_8h.md#a4be8f5f82ae51e880973256e748ef0a3)#define ESP\_I2SO\_WS\_OUT 14

[ 41](esp32c3-gpio-sigmap_8h.md#ac2d5d005dd8d5d5487dd24e021f2d3d5)#define ESP\_I2SI\_SD\_IN 15

[ 42](esp32c3-gpio-sigmap_8h.md#a2815be93d2102f382e8ed5c5f7913257)#define ESP\_I2SO\_SD\_OUT 15

[ 43](esp32c3-gpio-sigmap_8h.md#a0bc2c2947bb51d411a677fc07806e3fe)#define ESP\_I2SI\_BCK\_IN 16

[ 44](esp32c3-gpio-sigmap_8h.md#aa58a3701e86830736ae9b0b3d60ac6b5)#define ESP\_I2SI\_BCK\_OUT 16

[ 45](esp32c3-gpio-sigmap_8h.md#af1e51d50da781c498cda9e45e603544f)#define ESP\_I2SI\_WS\_IN 17

[ 46](esp32c3-gpio-sigmap_8h.md#aa0c2097b8e33d93001180bc068b85d5c)#define ESP\_I2SI\_WS\_OUT 17

[ 47](esp32c3-gpio-sigmap_8h.md#ab8d0a9090c64518af59274603f035042)#define ESP\_GPIO\_BT\_PRIORITY 18

[ 48](esp32c3-gpio-sigmap_8h.md#adf2824b1611032a81fe7b3c41253c0d8)#define ESP\_GPIO\_WLAN\_PRIO 18

[ 49](esp32c3-gpio-sigmap_8h.md#a47d854bfae0f88dc023613e61e6be551)#define ESP\_GPIO\_BT\_ACTIVE 19

[ 50](esp32c3-gpio-sigmap_8h.md#af675ca03172d2dcee1e19ccb5236e087)#define ESP\_GPIO\_WLAN\_ACTIVE 19

[ 51](esp32c3-gpio-sigmap_8h.md#a304bc90cc758f90f6675fea611ab0cfe)#define ESP\_BB\_DIAG0 20

[ 52](esp32c3-gpio-sigmap_8h.md#ad236bf991329914d59c194ff9003974a)#define ESP\_BB\_DIAG1 21

[ 53](esp32c3-gpio-sigmap_8h.md#a26c20261a5e2f4293b81c802a0a33b19)#define ESP\_BB\_DIAG2 22

[ 54](esp32c3-gpio-sigmap_8h.md#a5124ef75b703e7805bccd8c93828faae)#define ESP\_BB\_DIAG3 23

[ 55](esp32c3-gpio-sigmap_8h.md#aebd2c37b71d18967bd394b32c820647f)#define ESP\_BB\_DIAG4 24

[ 56](esp32c3-gpio-sigmap_8h.md#ace166b18a74fb8a42f876d1aa7cfb059)#define ESP\_BB\_DIAG5 25

[ 57](esp32c3-gpio-sigmap_8h.md#ad5685b19c170cc428cea0ee91f9155b0)#define ESP\_BB\_DIAG6 26

[ 58](esp32c3-gpio-sigmap_8h.md#aedf32208932dfe4471f6a5a7feb652f8)#define ESP\_BB\_DIAG7 27

[ 59](esp32c3-gpio-sigmap_8h.md#a126e2108473183890c6a2e148f8fd2c7)#define ESP\_BB\_DIAG8 28

[ 60](esp32c3-gpio-sigmap_8h.md#a75b60b1b4d53e6fca02b3a4f14ea530e)#define ESP\_BB\_DIAG9 29

[ 61](esp32c3-gpio-sigmap_8h.md#aed67caee00b7ceaaaa33b2917aba60f2)#define ESP\_BB\_DIAG10 30

[ 62](esp32c3-gpio-sigmap_8h.md#aef4bb5d62b93dfc3f2834404b6945b90)#define ESP\_BB\_DIAG11 31

[ 63](esp32c3-gpio-sigmap_8h.md#acc6cd70ce139a5639022bec896a3ba5e)#define ESP\_BB\_DIAG12 32

[ 64](esp32c3-gpio-sigmap_8h.md#afa72089303bf662a4efc8c068b157f0d)#define ESP\_BB\_DIAG13 33

[ 65](esp32c3-gpio-sigmap_8h.md#a4ef00458e2547f7141741191b92854d8)#define ESP\_BB\_DIAG14 34

[ 66](esp32c3-gpio-sigmap_8h.md#aed7c06883c6a69303a341454aff409ed)#define ESP\_BB\_DIAG15 35

[ 67](esp32c3-gpio-sigmap_8h.md#a1acc29dd7c0517c30299e71c1a6ce7fa)#define ESP\_BB\_DIAG16 36

[ 68](esp32c3-gpio-sigmap_8h.md#a9abbf3178088e44d984b088f53c25ab1)#define ESP\_BB\_DIAG17 37

[ 69](esp32c3-gpio-sigmap_8h.md#af75798fba81841339510ecc5f94e542e)#define ESP\_BB\_DIAG18 38

[ 70](esp32c3-gpio-sigmap_8h.md#a4102e08a6e29f2164f5aafa109ab734b)#define ESP\_BB\_DIAG19 39

[ 71](esp32c3-gpio-sigmap_8h.md#a7c2bcf73d61315a0d8c71d68173f9860)#define ESP\_USB\_EXTPHY\_VP 40

[ 72](esp32c3-gpio-sigmap_8h.md#a28f381128449aed0ae738516df39790c)#define ESP\_USB\_EXTPHY\_OEN 40

[ 73](esp32c3-gpio-sigmap_8h.md#aeaa130d2e220f2ebd073983921ad3679)#define ESP\_USB\_EXTPHY\_VM 41

[ 74](esp32c3-gpio-sigmap_8h.md#aedb10271abe4c1969eefbc0425681652)#define ESP\_USB\_EXTPHY\_SPEED 41

[ 75](esp32c3-gpio-sigmap_8h.md#a095d83d616afb08c4b06d82c4d907fee)#define ESP\_USB\_EXTPHY\_RCV 42

[ 76](esp32c3-gpio-sigmap_8h.md#a88c6a9f957332dac96360dd3f631e59b)#define ESP\_USB\_EXTPHY\_VPO 42

[ 77](esp32c3-gpio-sigmap_8h.md#abaeb7b2bb8208db93655b442293976aa)#define ESP\_USB\_EXTPHY\_VMO 43

[ 78](esp32c3-gpio-sigmap_8h.md#a301551d0d524f785b3d0e2c35bc81ce5)#define ESP\_USB\_EXTPHY\_SUSPND 44

[ 79](esp32c3-gpio-sigmap_8h.md#ae49b4527d8fbd0f5c8e3edc72704c54a)#define ESP\_EXT\_ADC\_START 45

[ 80](esp32c3-gpio-sigmap_8h.md#a62dfcd88747c61acb53dc85c1751f1d3)#define ESP\_LEDC\_LS\_SIG\_OUT0 45

[ 81](esp32c3-gpio-sigmap_8h.md#a5cad9206cfeea93b42e5456228c7d580)#define ESP\_LEDC\_LS\_SIG\_OUT1 46

[ 82](esp32c3-gpio-sigmap_8h.md#ab408070e7c700805db165c3876b6c588)#define ESP\_LEDC\_LS\_SIG\_OUT2 47

[ 83](esp32c3-gpio-sigmap_8h.md#a438aee217c6c94a2962a3d98935b5717)#define ESP\_LEDC\_LS\_SIG\_OUT3 48

[ 84](esp32c3-gpio-sigmap_8h.md#ada93dcffffc15362be4b7432a8033559)#define ESP\_LEDC\_LS\_SIG\_OUT4 49

[ 85](esp32c3-gpio-sigmap_8h.md#a34fc029ec45756ca7064580f57db1cc7)#define ESP\_LEDC\_LS\_SIG\_OUT5 50

[ 86](esp32c3-gpio-sigmap_8h.md#ad9bae9b4884a356e465656d1ee8d61cd)#define ESP\_RMT\_SIG\_IN0 51

[ 87](esp32c3-gpio-sigmap_8h.md#a25343fbc20a0c542bcdc21cdfade867b)#define ESP\_RMT\_SIG\_OUT0 51

[ 88](esp32c3-gpio-sigmap_8h.md#ab6c6293e6845ba4bf4d05b84102ffdcf)#define ESP\_RMT\_SIG\_IN1 52

[ 89](esp32c3-gpio-sigmap_8h.md#a6d082fb1c7397d784a3075108e0dea73)#define ESP\_RMT\_SIG\_OUT1 52

[ 90](esp32c3-gpio-sigmap_8h.md#ab607ce367da34ab0f1bd7fa648273cf1)#define ESP\_I2CEXT0\_SCL\_IN 53

[ 91](esp32c3-gpio-sigmap_8h.md#a2144cc62df795547ccf2bbe3ee4c629f)#define ESP\_I2CEXT0\_SCL\_OUT 53

[ 92](esp32c3-gpio-sigmap_8h.md#afa7061c87135b9dabe5c54f5f4ce16e6)#define ESP\_I2CEXT0\_SDA\_IN 54

[ 93](esp32c3-gpio-sigmap_8h.md#aabf1378b0ad2028c36c3bb74c81d7049)#define ESP\_I2CEXT0\_SDA\_OUT 54

[ 94](esp32c3-gpio-sigmap_8h.md#ae59035f8269ccd564ba0d7b2b078b3ee)#define ESP\_GPIO\_SD0\_OUT 55

[ 95](esp32c3-gpio-sigmap_8h.md#a3fbed77581ed14fa077f314e812b9c36)#define ESP\_GPIO\_SD1\_OUT 56

[ 96](esp32c3-gpio-sigmap_8h.md#a2668d9083ce28563cc160fe1102e927d)#define ESP\_GPIO\_SD2\_OUT 57

[ 97](esp32c3-gpio-sigmap_8h.md#a9d34f616894f98d7175c41b4ba565f8d)#define ESP\_GPIO\_SD3\_OUT 58

[ 98](esp32c3-gpio-sigmap_8h.md#ade88988460c131e8c6775794588b0eb8)#define ESP\_FSPICLK\_IN 63

[ 99](esp32c3-gpio-sigmap_8h.md#ab8c5397dc530f6326c3d10b31e59e168)#define ESP\_FSPICLK\_OUT 63

[ 100](esp32c3-gpio-sigmap_8h.md#ab603b7bf7d016e85653a5c3be5c01293)#define ESP\_FSPIQ\_IN 64

[ 101](esp32c3-gpio-sigmap_8h.md#a8b3ea6ad374fa010b46b48072fa87ccb)#define ESP\_FSPIQ\_OUT 64

[ 102](esp32c3-gpio-sigmap_8h.md#a7910521af840d42edd3c0a667cf90c5f)#define ESP\_FSPID\_IN 65

[ 103](esp32c3-gpio-sigmap_8h.md#a02bd34821e8a4bf0038b9af417ec161a)#define ESP\_FSPID\_OUT 65

[ 104](esp32c3-gpio-sigmap_8h.md#a60ff087a3d85a356d77f060a6698d00b)#define ESP\_FSPIHD\_IN 66

[ 105](esp32c3-gpio-sigmap_8h.md#ac71bc137b93bd6c0c8a1ebe24a70a613)#define ESP\_FSPIHD\_OUT 66

[ 106](esp32c3-gpio-sigmap_8h.md#a4d4c4a13b820cab6d94da8fe08120a2f)#define ESP\_FSPIWP\_IN 67

[ 107](esp32c3-gpio-sigmap_8h.md#a83c4f18d726984cc98caeea9b7677ca1)#define ESP\_FSPIWP\_OUT 67

[ 108](esp32c3-gpio-sigmap_8h.md#a96ca1328e76337d289f6e65faf33d75c)#define ESP\_FSPICS0\_IN 68

[ 109](esp32c3-gpio-sigmap_8h.md#ad1be1401b282275eaef46b9a598c6a40)#define ESP\_FSPICS0\_OUT 68

[ 110](esp32c3-gpio-sigmap_8h.md#a44ade9179a7ea00586359a009799661d)#define ESP\_FSPICS1\_OUT 69

[ 111](esp32c3-gpio-sigmap_8h.md#af991963f29c5b268a5f8fead8fd15348)#define ESP\_FSPICS2\_OUT 70

[ 112](esp32c3-gpio-sigmap_8h.md#a65d1170c5a68ac7f6a4457c3380ddfde)#define ESP\_FSPICS3\_OUT 71

[ 113](esp32c3-gpio-sigmap_8h.md#a83dafe68703c701dcd07d7ff0aadad01)#define ESP\_FSPICS4\_OUT 72

[ 114](esp32c3-gpio-sigmap_8h.md#ad8fab64bb220fd198a6cd931f4ea1e8e)#define ESP\_FSPICS5\_OUT 73

[ 115](esp32c3-gpio-sigmap_8h.md#ab3da303c2f9226f9648669c17af8377a)#define ESP\_TWAI\_RX 74

[ 116](esp32c3-gpio-sigmap_8h.md#a3b13bb40583aaa0f85de982509247614)#define ESP\_TWAI\_TX 74

[ 117](esp32c3-gpio-sigmap_8h.md#a6d0d41d1ec0f6fc626861f5857684e6d)#define ESP\_TWAI\_BUS\_OFF\_ON 75

[ 118](esp32c3-gpio-sigmap_8h.md#a1c69791269fdbb2a11f66f33eb4066be)#define ESP\_TWAI\_CLKOUT 76

[ 119](esp32c3-gpio-sigmap_8h.md#a0ad409b608ef2a418098b4e51d0e7e9a)#define ESP\_PCMFSYNC\_IN 77

[ 120](esp32c3-gpio-sigmap_8h.md#afd2befcf5eb0c413c0f8447558dc4863)#define ESP\_BT\_AUDIO0\_IRQ 77

[ 121](esp32c3-gpio-sigmap_8h.md#abb4d1f28362c68cf3f1e9f1696602b03)#define ESP\_PCMCLK\_IN 78

[ 122](esp32c3-gpio-sigmap_8h.md#acfe665b9ff21a51b93819a3f123180ad)#define ESP\_BT\_AUDIO1\_IRQ 78

[ 123](esp32c3-gpio-sigmap_8h.md#ae94f8dfc2be2c0cf8863a33df76d5295)#define ESP\_PCMDIN 79

[ 124](esp32c3-gpio-sigmap_8h.md#a77ac554a2a10fc6fa77106e8af9dfc86)#define ESP\_BT\_AUDIO2\_IRQ 79

[ 125](esp32c3-gpio-sigmap_8h.md#a7abc844342f6483be73ea503d3f76d89)#define ESP\_RW\_WAKEUP\_REQ 80

[ 126](esp32c3-gpio-sigmap_8h.md#ab2e25b779a18acd66533795433291a3d)#define ESP\_BLE\_AUDIO0\_IRQ 80

[ 127](esp32c3-gpio-sigmap_8h.md#ab4b3d654c674536c2c63070210147372)#define ESP\_BLE\_AUDIO1\_IRQ 81

[ 128](esp32c3-gpio-sigmap_8h.md#a637ea6fcad7b2e5fe48cf9e3419fbed6)#define ESP\_BLE\_AUDIO2\_IRQ 82

[ 129](esp32c3-gpio-sigmap_8h.md#a8b79d6e15573a684058c9b933f469f09)#define ESP\_PCMFSYNC\_OUT 83

[ 130](esp32c3-gpio-sigmap_8h.md#a500651ca0d6daa86774a0f45190f8b38)#define ESP\_PCMCLK\_OUT 84

[ 131](esp32c3-gpio-sigmap_8h.md#ab3ecd7e5557112172c38bff3b2605e9c)#define ESP\_PCMDOUT 85

[ 132](esp32c3-gpio-sigmap_8h.md#aba2aea8feedc96a0a6b3bba007df49ac)#define ESP\_BLE\_AUDIO\_SYNC0\_P 86

[ 133](esp32c3-gpio-sigmap_8h.md#a21e5bf1c7c33a39f11d8bf6537ed85bb)#define ESP\_BLE\_AUDIO\_SYNC1\_P 87

[ 134](esp32c3-gpio-sigmap_8h.md#a961f37a0b2dcb9e183331ef5684f8504)#define ESP\_BLE\_AUDIO\_SYNC2\_P 88

[ 135](esp32c3-gpio-sigmap_8h.md#aec2dfb198f69d923686404a0a6330833)#define ESP\_ANT\_SEL0 89

[ 136](esp32c3-gpio-sigmap_8h.md#a15c080ea1e4c8e2db9f1640e9b8c4f0a)#define ESP\_ANT\_SEL1 90

[ 137](esp32c3-gpio-sigmap_8h.md#ae3042ff86ecc0f2e78ebe9477055e819)#define ESP\_ANT\_SEL2 91

[ 138](esp32c3-gpio-sigmap_8h.md#ab8e5cca4b9eb1a7bda7868ecd792c76d)#define ESP\_ANT\_SEL3 92

[ 139](esp32c3-gpio-sigmap_8h.md#a821cc4b81f76043b1ecb751118a2f416)#define ESP\_ANT\_SEL4 93

[ 140](esp32c3-gpio-sigmap_8h.md#a28a954881fd9d5f5e7ff25d715f0bcc2)#define ESP\_ANT\_SEL5 94

[ 141](esp32c3-gpio-sigmap_8h.md#a2122dad1966cbe214e9c82cb9a46bd8a)#define ESP\_ANT\_SEL6 95

[ 142](esp32c3-gpio-sigmap_8h.md#a8f9cedf15c49cee3fbac2a22df7675ec)#define ESP\_ANT\_SEL7 96

[ 143](esp32c3-gpio-sigmap_8h.md#a66890ae0c0e6a875c19099abb1918ca1)#define ESP\_SIG\_IN\_FUNC\_97 97

[ 144](esp32c3-gpio-sigmap_8h.md#a919b1b0e57d8785970c702fcd49d5563)#define ESP\_SIG\_IN\_FUNC97 97

[ 145](esp32c3-gpio-sigmap_8h.md#a848f955ed1b3b04d0a3d90f8c0acedec)#define ESP\_SIG\_IN\_FUNC\_98 98

[ 146](esp32c3-gpio-sigmap_8h.md#ae6043332289b10b68dc1d278681f3df1)#define ESP\_SIG\_IN\_FUNC98 98

[ 147](esp32c3-gpio-sigmap_8h.md#ab6956182e8d06463813e94843398a45f)#define ESP\_SIG\_IN\_FUNC\_99 99

[ 148](esp32c3-gpio-sigmap_8h.md#a11dcdffc24ff5d98c7c8d0f609a0c7b9)#define ESP\_SIG\_IN\_FUNC99 99

[ 149](esp32c3-gpio-sigmap_8h.md#a6684d495dfe99d0798f576018ffe0aba)#define ESP\_SIG\_IN\_FUNC\_100 100

[ 150](esp32c3-gpio-sigmap_8h.md#a33f1fad3bde9b252dfb3a291d600c019)#define ESP\_SIG\_IN\_FUNC100 100

[ 151](esp32c3-gpio-sigmap_8h.md#a0206456525cd6dc235ed6892e98731c6)#define ESP\_SYNCERR 101

[ 152](esp32c3-gpio-sigmap_8h.md#aa62bd8539c4d89abaa542d8bd4c91efd)#define ESP\_SYNCFOUND\_FLAG 102

[ 153](esp32c3-gpio-sigmap_8h.md#ade4ee47d8f72c009686b2454ee77ee60)#define ESP\_EVT\_CNTL\_IMMEDIATE\_ABORT 103

[ 154](esp32c3-gpio-sigmap_8h.md#ac5684072c6c5fbbdb6631d73270819dc)#define ESP\_LINKLBL 104

[ 155](esp32c3-gpio-sigmap_8h.md#a1029a66c0538d7eb1026ced27d54a59b)#define ESP\_DATA\_EN 105

[ 156](esp32c3-gpio-sigmap_8h.md#a04dc693cfec6739602b92e86a837c58d)#define ESP\_DATA 106

[ 157](esp32c3-gpio-sigmap_8h.md#aecac02e2195c5da81f63ed4c19bd06fb)#define ESP\_PKT\_TX\_ON 107

[ 158](esp32c3-gpio-sigmap_8h.md#a63f7ec6fc7927b0f0fb3bd0dc733de5a)#define ESP\_PKT\_RX\_ON 108

[ 159](esp32c3-gpio-sigmap_8h.md#a3b8a7f22861948aa8809aa58ecbdb0ef)#define ESP\_RW\_TX\_ON 109

[ 160](esp32c3-gpio-sigmap_8h.md#a5f93eee3354e5fd70d11fd26c9dd25bb)#define ESP\_RW\_RX\_ON 110

[ 161](esp32c3-gpio-sigmap_8h.md#af7d8fb5a97cb0e4f3dad1a73fb0610d5)#define ESP\_EVT\_REQ\_P 111

[ 162](esp32c3-gpio-sigmap_8h.md#a10fd19b9a6140fea7e88facaa02686be)#define ESP\_EVT\_STOP\_P 112

[ 163](esp32c3-gpio-sigmap_8h.md#a08a40a396cf075e77aa50acfb811885a)#define ESP\_BT\_MODE\_ON 113

[ 164](esp32c3-gpio-sigmap_8h.md#a80a3804720f2e69ac5caa52c0ade9d5b)#define ESP\_GPIO\_LC\_DIAG0 114

[ 165](esp32c3-gpio-sigmap_8h.md#ad842d1a31efaf5f3edc70326ac89df9b)#define ESP\_GPIO\_LC\_DIAG1 115

[ 166](esp32c3-gpio-sigmap_8h.md#ad23ea4680ce2cbf713bb456dae84e35b)#define ESP\_GPIO\_LC\_DIAG2 116

[ 167](esp32c3-gpio-sigmap_8h.md#a83ab157d422c3004c3dc287c0c804ec5)#define ESP\_CH 117

[ 168](esp32c3-gpio-sigmap_8h.md#a546d9b83cad2a5b2e64677be087b1f9d)#define ESP\_RX\_WINDOW 118

[ 169](esp32c3-gpio-sigmap_8h.md#a25d03cedd231864f508e405d0ae2fa4b)#define ESP\_UPDATE\_RX 119

[ 170](esp32c3-gpio-sigmap_8h.md#ac2450d1a096d1adf2386ba91e0a92f75)#define ESP\_RX\_STATUS 120

[ 171](esp32c3-gpio-sigmap_8h.md#ae27ee8b3a05b497ec7bea2ed69fc9230)#define ESP\_CLK\_GPIO 121

[ 172](esp32c3-gpio-sigmap_8h.md#a9aa8b294d23efae4cd5a6dd741829aad)#define ESP\_NBT\_BLE 122

[ 173](esp32c3-gpio-sigmap_8h.md#a12a2380f8bcbf158e7c114b7dc1701a5)#define ESP\_CLK\_OUT\_OUT1 123

[ 174](esp32c3-gpio-sigmap_8h.md#adf7a9c85596f3a536ddb603d3218cee2)#define ESP\_CLK\_OUT\_OUT2 124

[ 175](esp32c3-gpio-sigmap_8h.md#af421f62c654ecca5136b7b526f168377)#define ESP\_CLK\_OUT\_OUT3 125

[ 176](esp32c3-gpio-sigmap_8h.md#aa4a67a38b97a3d466783c0617aa6a0c8)#define ESP\_SPICS1\_OUT 126

[ 177](esp32c3-gpio-sigmap_8h.md#a645411759ffdc63f51f2cd42632d2720)#define ESP\_SIG\_GPIO\_OUT 128

[ 178](esp32c3-gpio-sigmap_8h.md#afe5c166b887709cdd27bd37df85c45b9)#define ESP\_GPIO\_MAP\_DATE 0x2006130

179

180#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32C3\_GPIO\_SIGMAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32c3-gpio-sigmap.h](esp32c3-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
