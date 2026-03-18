---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp32-gpio-sigmap_8h_source.html
original_path: doxygen/html/esp32-gpio-sigmap_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32-gpio-sigmap.h

[Go to the documentation of this file.](esp32-gpio-sigmap_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32\_GPIO\_SIGMAP\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32\_GPIO\_SIGMAP\_H\_

9

[ 10](esp32-gpio-sigmap_8h.md#af80260535bc3aee44c28c972a29483e0)#define ESP\_NOSIG ESP\_SIG\_INVAL

11

[ 12](esp32-gpio-sigmap_8h.md#a89331a24c2b322eda2d32394ec1f08bc)#define ESP\_SPICLK\_IN 0

[ 13](esp32-gpio-sigmap_8h.md#a5f440c922a53085bb7b28f469c2a14b0)#define ESP\_SPICLK\_OUT 0

[ 14](esp32-gpio-sigmap_8h.md#aec51ff955c6be50e529affc87ec9d5cb)#define ESP\_SPIQ\_IN 1

[ 15](esp32-gpio-sigmap_8h.md#a5816deeca8853397a830a8eb251704ee)#define ESP\_SPIQ\_OUT 1

[ 16](esp32-gpio-sigmap_8h.md#a26c603fd58dbd7526d2be3bb3e37758a)#define ESP\_SPID\_IN 2

[ 17](esp32-gpio-sigmap_8h.md#af81b2fc65b68ed2238ab3367a8731102)#define ESP\_SPID\_OUT 2

[ 18](esp32-gpio-sigmap_8h.md#a49783f877b666aff9362cf605590b991)#define ESP\_SPIHD\_IN 3

[ 19](esp32-gpio-sigmap_8h.md#a8851b5256482790f3304efecafc13afd)#define ESP\_SPIHD\_OUT 3

[ 20](esp32-gpio-sigmap_8h.md#aa74adc2812d9c6bd143c679fa4d9ca8d)#define ESP\_SPIWP\_IN 4

[ 21](esp32-gpio-sigmap_8h.md#a470408f8102937dc017336e320e6147b)#define ESP\_SPIWP\_OUT 4

[ 22](esp32-gpio-sigmap_8h.md#a7bf90419c18c69d0438a4d349e9cbdb2)#define ESP\_SPICS0\_IN 5

[ 23](esp32-gpio-sigmap_8h.md#a5d97c07ba0d8cda594d52310e90fa6a4)#define ESP\_SPICS0\_OUT 5

[ 24](esp32-gpio-sigmap_8h.md#afe3e0ee1116416992306c25420ca6efa)#define ESP\_SPICS1\_IN 6

[ 25](esp32-gpio-sigmap_8h.md#aa4a67a38b97a3d466783c0617aa6a0c8)#define ESP\_SPICS1\_OUT 6

[ 26](esp32-gpio-sigmap_8h.md#abce40937f1557fdae2dce1a96a8aab3d)#define ESP\_SPICS2\_IN 7

[ 27](esp32-gpio-sigmap_8h.md#afdb41f1d4bc9948ea4e723e6f43a9363)#define ESP\_SPICS2\_OUT 7

[ 28](esp32-gpio-sigmap_8h.md#aa214d49ff0a9292fecc67fd8746a3201)#define ESP\_HSPICLK\_IN 8

[ 29](esp32-gpio-sigmap_8h.md#a028245349e09fe0dac8a5d16023d6884)#define ESP\_HSPICLK\_OUT 8

[ 30](esp32-gpio-sigmap_8h.md#ad73beba22fb7e7d4d2ddf56c0f260e96)#define ESP\_HSPIQ\_IN 9

[ 31](esp32-gpio-sigmap_8h.md#a0a3b5b9357369087ac3b4aea4065b277)#define ESP\_HSPIQ\_OUT 9

[ 32](esp32-gpio-sigmap_8h.md#a051bfe73e21998d1401febd110a98996)#define ESP\_HSPID\_IN 10

[ 33](esp32-gpio-sigmap_8h.md#ab91738160e1970f528b96c97cd71fbf4)#define ESP\_HSPID\_OUT 10

[ 34](esp32-gpio-sigmap_8h.md#a3cf30db72dad00ef614fdb2739dccfe6)#define ESP\_HSPICS0\_IN 11

[ 35](esp32-gpio-sigmap_8h.md#a5e584dd081acca27717085cc7cf901f8)#define ESP\_HSPICS0\_OUT 11

[ 36](esp32-gpio-sigmap_8h.md#a8f77392a0ce164e7b943c9cc80465b3f)#define ESP\_HSPIHD\_IN 12

[ 37](esp32-gpio-sigmap_8h.md#aecbf07e7ff7852bf6b45dd88a65aaa70)#define ESP\_HSPIHD\_OUT 12

[ 38](esp32-gpio-sigmap_8h.md#a34ead95b59d395722b17c73b0ce219d1)#define ESP\_HSPIWP\_IN 13

[ 39](esp32-gpio-sigmap_8h.md#a904860708852fdec4d3e29e7cc6192f7)#define ESP\_HSPIWP\_OUT 13

[ 40](esp32-gpio-sigmap_8h.md#aca502efa55ce2286dc9eba28192681fd)#define ESP\_U0RXD\_IN 14

[ 41](esp32-gpio-sigmap_8h.md#af1e58fb8e7ef86a92171eca7bb1671af)#define ESP\_U0TXD\_OUT 14

[ 42](esp32-gpio-sigmap_8h.md#a530d7a918a97cd1fff1acf2f90edd4ca)#define ESP\_U0CTS\_IN 15

[ 43](esp32-gpio-sigmap_8h.md#a4257bbc044af6ea3612313e3a0b7e7c9)#define ESP\_U0RTS\_OUT 15

[ 44](esp32-gpio-sigmap_8h.md#a53e3a4557a4eb1f7f98250abef03c02a)#define ESP\_U0DSR\_IN 16

[ 45](esp32-gpio-sigmap_8h.md#acc8716af947169c9f167bdf215c5314c)#define ESP\_U0DTR\_OUT 16

[ 46](esp32-gpio-sigmap_8h.md#a2293e0646e0ad2f76d62f76425ae6770)#define ESP\_U1RXD\_IN 17

[ 47](esp32-gpio-sigmap_8h.md#a6053b38147e28e3a7479b38e7d195136)#define ESP\_U1TXD\_OUT 17

[ 48](esp32-gpio-sigmap_8h.md#a3c005e616da21a058960d6aed79427b3)#define ESP\_U1CTS\_IN 18

[ 49](esp32-gpio-sigmap_8h.md#a8f6399745566bd5caa2020e4dcb2bb3b)#define ESP\_U1RTS\_OUT 18

[ 50](esp32-gpio-sigmap_8h.md#a3b913756d12daf98239924b1947d4717)#define ESP\_I2CM\_SCL\_O 19

[ 51](esp32-gpio-sigmap_8h.md#a367bd6cd5bfd5d5c7d751ee8e83cb74a)#define ESP\_I2CM\_SDA\_I 20

[ 52](esp32-gpio-sigmap_8h.md#a92f1f15e271687d72d19f3b1028f8a9e)#define ESP\_I2CM\_SDA\_O 20

[ 53](esp32-gpio-sigmap_8h.md#aadedd8576af305e1d6d56c8fa6dd30bc)#define ESP\_EXT\_I2C\_SCL\_O 21

[ 54](esp32-gpio-sigmap_8h.md#a55fa3484edd1c42124fc641667004506)#define ESP\_EXT\_I2C\_SDA\_O 22

[ 55](esp32-gpio-sigmap_8h.md#ae1190b3753881bd745085f76b9f6c165)#define ESP\_EXT\_I2C\_SDA\_I 22

[ 56](esp32-gpio-sigmap_8h.md#af0b9626d6b7cfd5b5c42a8127897d565)#define ESP\_I2S0O\_BCK\_IN 23

[ 57](esp32-gpio-sigmap_8h.md#a2e76c532bd75a6af4790b30f58c4b8e9)#define ESP\_I2S0O\_BCK\_OUT 23

[ 58](esp32-gpio-sigmap_8h.md#afffede35b0effa00a9d6e1077ac4aaa2)#define ESP\_I2S1O\_BCK\_IN 24

[ 59](esp32-gpio-sigmap_8h.md#afcd05d2cf345dcf816068b0b89ac5a72)#define ESP\_I2S1O\_BCK\_OUT 24

[ 60](esp32-gpio-sigmap_8h.md#aad13d05d8d50227859d484deaaf6e34b)#define ESP\_I2S0O\_WS\_IN 25

[ 61](esp32-gpio-sigmap_8h.md#a78693c10e4ac17973e7ac12c1bdf8c97)#define ESP\_I2S0O\_WS\_OUT 25

[ 62](esp32-gpio-sigmap_8h.md#a7ac95a35ee6001c340cddd1424f3fa5e)#define ESP\_I2S1O\_WS\_IN 26

[ 63](esp32-gpio-sigmap_8h.md#a84485bdfe1661269506f7ef1f70f4a87)#define ESP\_I2S1O\_WS\_OUT 26

[ 64](esp32-gpio-sigmap_8h.md#a67905afbcda699d20d8a05a8a66411af)#define ESP\_I2S0I\_BCK\_IN 27

[ 65](esp32-gpio-sigmap_8h.md#abe571a9bad2c0e95049afd8e67c8d158)#define ESP\_I2S0I\_BCK\_OUT 27

[ 66](esp32-gpio-sigmap_8h.md#a4236f62ac75d5f2d56f7b1cc941d7509)#define ESP\_I2S0I\_WS\_IN 28

[ 67](esp32-gpio-sigmap_8h.md#af039bdc8eec9ec95d3ed2bbebabb22cb)#define ESP\_I2S0I\_WS\_OUT 28

[ 68](esp32-gpio-sigmap_8h.md#ab607ce367da34ab0f1bd7fa648273cf1)#define ESP\_I2CEXT0\_SCL\_IN 29

[ 69](esp32-gpio-sigmap_8h.md#a2144cc62df795547ccf2bbe3ee4c629f)#define ESP\_I2CEXT0\_SCL\_OUT 29

[ 70](esp32-gpio-sigmap_8h.md#afa7061c87135b9dabe5c54f5f4ce16e6)#define ESP\_I2CEXT0\_SDA\_IN 30

[ 71](esp32-gpio-sigmap_8h.md#aabf1378b0ad2028c36c3bb74c81d7049)#define ESP\_I2CEXT0\_SDA\_OUT 30

[ 72](esp32-gpio-sigmap_8h.md#a60a3fe70a1bc5ba71cb46df782901087)#define ESP\_PWM0\_SYNC0\_IN 31

[ 73](esp32-gpio-sigmap_8h.md#aac3529b76d29e57ad20500c9d1da23f3)#define ESP\_SDIO\_TOHOST\_INT\_OUT 31

[ 74](esp32-gpio-sigmap_8h.md#aca616afbb64ed37982624503545a5a72)#define ESP\_PWM0\_SYNC1\_IN 32

[ 75](esp32-gpio-sigmap_8h.md#a9397a79a46feab488c88552013790dfc)#define ESP\_PWM0\_OUT0A 32

[ 76](esp32-gpio-sigmap_8h.md#a2017681d630abc75e7298c12b86a62ce)#define ESP\_PWM0\_SYNC2\_IN 33

[ 77](esp32-gpio-sigmap_8h.md#acb3badfaed73f7069ea23dde375db62a)#define ESP\_PWM0\_OUT0B 33

[ 78](esp32-gpio-sigmap_8h.md#a4a503a957b2fd76f257534b80069caa2)#define ESP\_PWM0\_F0\_IN 34

[ 79](esp32-gpio-sigmap_8h.md#ae52e5bd4be5563caeb9861267e41d947)#define ESP\_PWM0\_OUT1A 34

[ 80](esp32-gpio-sigmap_8h.md#af536ae867a3d8bcb7644b48c346b4b50)#define ESP\_PWM0\_F1\_IN 35

[ 81](esp32-gpio-sigmap_8h.md#a9fa8e944ff2d960c141f8375c9aa0b0e)#define ESP\_PWM0\_OUT1B 35

[ 82](esp32-gpio-sigmap_8h.md#a83f385e6b8a99314cc641083a203322b)#define ESP\_PWM0\_F2\_IN 36

[ 83](esp32-gpio-sigmap_8h.md#abf74a2a32a8c36431e2f21d6cd15a610)#define ESP\_PWM0\_OUT2A 36

[ 84](esp32-gpio-sigmap_8h.md#a47d854bfae0f88dc023613e61e6be551)#define ESP\_GPIO\_BT\_ACTIVE 37

[ 85](esp32-gpio-sigmap_8h.md#a563105deedf9f7ed6818ab9a8a8aecdc)#define ESP\_PWM0\_OUT2B 37

[ 86](esp32-gpio-sigmap_8h.md#ab8d0a9090c64518af59274603f035042)#define ESP\_GPIO\_BT\_PRIORITY 38

[ 87](esp32-gpio-sigmap_8h.md#acf123456a5b9d94f370309ad39672e34)#define ESP\_PCNT\_SIG\_CH0\_IN0 39

[ 88](esp32-gpio-sigmap_8h.md#a800813b2c23f7e4bb23e032e0802a459)#define ESP\_PCNT\_SIG\_CH1\_IN0 40

[ 89](esp32-gpio-sigmap_8h.md#af675ca03172d2dcee1e19ccb5236e087)#define ESP\_GPIO\_WLAN\_ACTIVE 40

[ 90](esp32-gpio-sigmap_8h.md#a7e3c939b0b32332a35f0bead0aa4a2a6)#define ESP\_PCNT\_CTRL\_CH0\_IN0 41

[ 91](esp32-gpio-sigmap_8h.md#a304bc90cc758f90f6675fea611ab0cfe)#define ESP\_BB\_DIAG0 41

[ 92](esp32-gpio-sigmap_8h.md#a88c5eb5c7f4169ce3e7f7056b42989a7)#define ESP\_PCNT\_CTRL\_CH1\_IN0 42

[ 93](esp32-gpio-sigmap_8h.md#ad236bf991329914d59c194ff9003974a)#define ESP\_BB\_DIAG1 42

[ 94](esp32-gpio-sigmap_8h.md#a99db3d1c4e07e11fc09a4024a54fcea6)#define ESP\_PCNT\_SIG\_CH0\_IN1 43

[ 95](esp32-gpio-sigmap_8h.md#a26c20261a5e2f4293b81c802a0a33b19)#define ESP\_BB\_DIAG2 43

[ 96](esp32-gpio-sigmap_8h.md#a730113779d69ca86b257060678f8cbec)#define ESP\_PCNT\_SIG\_CH1\_IN1 44

[ 97](esp32-gpio-sigmap_8h.md#a5124ef75b703e7805bccd8c93828faae)#define ESP\_BB\_DIAG3 44

[ 98](esp32-gpio-sigmap_8h.md#a9ec8d490316b9f043fe5e9160a7cf7e0)#define ESP\_PCNT\_CTRL\_CH0\_IN1 45

[ 99](esp32-gpio-sigmap_8h.md#aebd2c37b71d18967bd394b32c820647f)#define ESP\_BB\_DIAG4 45

[ 100](esp32-gpio-sigmap_8h.md#a0bbfffdef085eb6cedc3d1232766cb38)#define ESP\_PCNT\_CTRL\_CH1\_IN1 46

[ 101](esp32-gpio-sigmap_8h.md#ace166b18a74fb8a42f876d1aa7cfb059)#define ESP\_BB\_DIAG5 46

[ 102](esp32-gpio-sigmap_8h.md#a4f9e798a260fb6ac4c39262f20253244)#define ESP\_PCNT\_SIG\_CH0\_IN2 47

[ 103](esp32-gpio-sigmap_8h.md#ad5685b19c170cc428cea0ee91f9155b0)#define ESP\_BB\_DIAG6 47

[ 104](esp32-gpio-sigmap_8h.md#a38365b3f9a2b49ef2714c38d00d293c5)#define ESP\_PCNT\_SIG\_CH1\_IN2 48

[ 105](esp32-gpio-sigmap_8h.md#aedf32208932dfe4471f6a5a7feb652f8)#define ESP\_BB\_DIAG7 48

[ 106](esp32-gpio-sigmap_8h.md#a540cbfcd205911955effcc9814f9707c)#define ESP\_PCNT\_CTRL\_CH0\_IN2 49

[ 107](esp32-gpio-sigmap_8h.md#a126e2108473183890c6a2e148f8fd2c7)#define ESP\_BB\_DIAG8 49

[ 108](esp32-gpio-sigmap_8h.md#abf6c210e19582b06e3d6c546a009ef5b)#define ESP\_PCNT\_CTRL\_CH1\_IN2 50

[ 109](esp32-gpio-sigmap_8h.md#a75b60b1b4d53e6fca02b3a4f14ea530e)#define ESP\_BB\_DIAG9 50

[ 110](esp32-gpio-sigmap_8h.md#acd8d20d89508b532a4e2749499263de3)#define ESP\_PCNT\_SIG\_CH0\_IN3 51

[ 111](esp32-gpio-sigmap_8h.md#aed67caee00b7ceaaaa33b2917aba60f2)#define ESP\_BB\_DIAG10 51

[ 112](esp32-gpio-sigmap_8h.md#ac54a606ee7096db15cdb9453b04ac72d)#define ESP\_PCNT\_SIG\_CH1\_IN3 52

[ 113](esp32-gpio-sigmap_8h.md#aef4bb5d62b93dfc3f2834404b6945b90)#define ESP\_BB\_DIAG11 52

[ 114](esp32-gpio-sigmap_8h.md#a96e8bd4584ab671a1b0c3f0adb440943)#define ESP\_PCNT\_CTRL\_CH0\_IN3 53

[ 115](esp32-gpio-sigmap_8h.md#acc6cd70ce139a5639022bec896a3ba5e)#define ESP\_BB\_DIAG12 53

[ 116](esp32-gpio-sigmap_8h.md#a0a926d350fc11d737b545c53b3ba1671)#define ESP\_PCNT\_CTRL\_CH1\_IN3 54

[ 117](esp32-gpio-sigmap_8h.md#afa72089303bf662a4efc8c068b157f0d)#define ESP\_BB\_DIAG13 54

[ 118](esp32-gpio-sigmap_8h.md#a0db0b3f57cffafbd98a8ba3a17a6cbc0)#define ESP\_PCNT\_SIG\_CH0\_IN4 55

[ 119](esp32-gpio-sigmap_8h.md#a4ef00458e2547f7141741191b92854d8)#define ESP\_BB\_DIAG14 55

[ 120](esp32-gpio-sigmap_8h.md#a0d17b8a68ec65a03d73119f26a6811ab)#define ESP\_PCNT\_SIG\_CH1\_IN4 56

[ 121](esp32-gpio-sigmap_8h.md#aed7c06883c6a69303a341454aff409ed)#define ESP\_BB\_DIAG15 56

[ 122](esp32-gpio-sigmap_8h.md#ae5a4af55bcd763eab98fa85fe09c78df)#define ESP\_PCNT\_CTRL\_CH0\_IN4 57

[ 123](esp32-gpio-sigmap_8h.md#a1acc29dd7c0517c30299e71c1a6ce7fa)#define ESP\_BB\_DIAG16 57

[ 124](esp32-gpio-sigmap_8h.md#a0a1247ca451b38941f488721cc4df99d)#define ESP\_PCNT\_CTRL\_CH1\_IN4 58

[ 125](esp32-gpio-sigmap_8h.md#a9abbf3178088e44d984b088f53c25ab1)#define ESP\_BB\_DIAG17 58

[ 126](esp32-gpio-sigmap_8h.md#af75798fba81841339510ecc5f94e542e)#define ESP\_BB\_DIAG18 59

[ 127](esp32-gpio-sigmap_8h.md#a4102e08a6e29f2164f5aafa109ab734b)#define ESP\_BB\_DIAG19 60

[ 128](esp32-gpio-sigmap_8h.md#ae424fe3b3c2d6a48bdf3b9f72c0b3a3b)#define ESP\_HSPICS1\_IN 61

[ 129](esp32-gpio-sigmap_8h.md#a8180ffc727af6c61530679be1a33ddb6)#define ESP\_HSPICS1\_OUT 61

[ 130](esp32-gpio-sigmap_8h.md#aa718d7483400f89985652d1aa6b338d7)#define ESP\_HSPICS2\_IN 62

[ 131](esp32-gpio-sigmap_8h.md#ad5849b71710c8fa5799b230fe5f40c4c)#define ESP\_HSPICS2\_OUT 62

[ 132](esp32-gpio-sigmap_8h.md#ad86c783e1f7a935adc312d9a15894c9a)#define ESP\_VSPICLK\_IN 63

[ 133](esp32-gpio-sigmap_8h.md#ada1b28a229c5f3e37a2e3d729e3f8300)#define ESP\_VSPICLK\_OUT 63

[ 134](esp32-gpio-sigmap_8h.md#a4a68acaff9e8aa24b9ef3d2b1e349c10)#define ESP\_VSPIQ\_IN 64

[ 135](esp32-gpio-sigmap_8h.md#a9651cadb9acf4b9f436752504c113b84)#define ESP\_VSPIQ\_OUT 64

[ 136](esp32-gpio-sigmap_8h.md#aa22893d39ca3b946c7f5a36febc44a62)#define ESP\_VSPID\_IN 65

[ 137](esp32-gpio-sigmap_8h.md#a6b9b2395789e3afbfdbf9c2faaa90b84)#define ESP\_VSPID\_OUT 65

[ 138](esp32-gpio-sigmap_8h.md#a38c28112b8871b2f61021228961620ca)#define ESP\_VSPIHD\_IN 66

[ 139](esp32-gpio-sigmap_8h.md#ac3b80d593bb67b9bb55be918ea1ac07c)#define ESP\_VSPIHD\_OUT 66

[ 140](esp32-gpio-sigmap_8h.md#ae2f52f231a2faa56c586fd5c6afe6fc3)#define ESP\_VSPIWP\_IN 67

[ 141](esp32-gpio-sigmap_8h.md#a69a257fe558c166843ce24c03b0347c9)#define ESP\_VSPIWP\_OUT 67

[ 142](esp32-gpio-sigmap_8h.md#add4fa23bc4c1d3973d0656837c352385)#define ESP\_VSPICS0\_IN 68

[ 143](esp32-gpio-sigmap_8h.md#ac813c68db44d91d27f040722e4d49c72)#define ESP\_VSPICS0\_OUT 68

[ 144](esp32-gpio-sigmap_8h.md#a51ea9a0228493852dd9c38bfd91f102b)#define ESP\_VSPICS1\_IN 69

[ 145](esp32-gpio-sigmap_8h.md#aad60ac2b393861f7366213d682e1089e)#define ESP\_VSPICS1\_OUT 69

[ 146](esp32-gpio-sigmap_8h.md#a10f41168ec052c1414604b15bcb59d7e)#define ESP\_VSPICS2\_IN 70

[ 147](esp32-gpio-sigmap_8h.md#ac6aaeb62e6e1c246a7a07071b162f283)#define ESP\_VSPICS2\_OUT 70

[ 148](esp32-gpio-sigmap_8h.md#acd9159d1c2dd971ec52a4965a41651f9)#define ESP\_PCNT\_SIG\_CH0\_IN5 71

[ 149](esp32-gpio-sigmap_8h.md#a67c3c6dabfb9930fa544b339eb44b0c8)#define ESP\_LEDC\_HS\_SIG\_OUT0 71

[ 150](esp32-gpio-sigmap_8h.md#a2da313499920b543ac0645fd2fc15f89)#define ESP\_PCNT\_SIG\_CH1\_IN5 72

[ 151](esp32-gpio-sigmap_8h.md#a6c5eb01aeacb1b28fe6db3e2b86ac82d)#define ESP\_LEDC\_HS\_SIG\_OUT1 72

[ 152](esp32-gpio-sigmap_8h.md#aad99a4e2a52277508ba2ce89724acb7d)#define ESP\_PCNT\_CTRL\_CH0\_IN5 73

[ 153](esp32-gpio-sigmap_8h.md#a1ae7688b4ab2ce508465491840623f85)#define ESP\_LEDC\_HS\_SIG\_OUT2 73

[ 154](esp32-gpio-sigmap_8h.md#a9a0fede369d254f3a8be2fe8122f6b40)#define ESP\_PCNT\_CTRL\_CH1\_IN5 74

[ 155](esp32-gpio-sigmap_8h.md#a0bb8f5d68a451926a18807510b22ab82)#define ESP\_LEDC\_HS\_SIG\_OUT3 74

[ 156](esp32-gpio-sigmap_8h.md#a0bbe8fe0f0d42eb511cbde58704c2c52)#define ESP\_PCNT\_SIG\_CH0\_IN6 75

[ 157](esp32-gpio-sigmap_8h.md#a6b3461968ccad6864885f9e91678e233)#define ESP\_LEDC\_HS\_SIG\_OUT4 75

[ 158](esp32-gpio-sigmap_8h.md#acb6e28da094bab3c0a86c1ec9df8b304)#define ESP\_PCNT\_SIG\_CH1\_IN6 76

[ 159](esp32-gpio-sigmap_8h.md#a8b412e40a386c2350b0f48a76304d37a)#define ESP\_LEDC\_HS\_SIG\_OUT5 76

[ 160](esp32-gpio-sigmap_8h.md#a33b5a2894d2b4d566a9237361127cc38)#define ESP\_PCNT\_CTRL\_CH0\_IN6 77

[ 161](esp32-gpio-sigmap_8h.md#a59a5b060f9a7aa2c8a2288b1db64b399)#define ESP\_LEDC\_HS\_SIG\_OUT6 77

[ 162](esp32-gpio-sigmap_8h.md#ae345f6de908812d12034e2d0de82954c)#define ESP\_PCNT\_CTRL\_CH1\_IN6 78

[ 163](esp32-gpio-sigmap_8h.md#adc3771298c3367482d6bbc51da03efed)#define ESP\_LEDC\_HS\_SIG\_OUT7 78

[ 164](esp32-gpio-sigmap_8h.md#a43b536b3cbea05abb8637bf9e3b0942d)#define ESP\_PCNT\_SIG\_CH0\_IN7 79

[ 165](esp32-gpio-sigmap_8h.md#a62dfcd88747c61acb53dc85c1751f1d3)#define ESP\_LEDC\_LS\_SIG\_OUT0 79

[ 166](esp32-gpio-sigmap_8h.md#a79fd1b052af27cc9a3c7861cee7f564d)#define ESP\_PCNT\_SIG\_CH1\_IN7 80

[ 167](esp32-gpio-sigmap_8h.md#a5cad9206cfeea93b42e5456228c7d580)#define ESP\_LEDC\_LS\_SIG\_OUT1 80

[ 168](esp32-gpio-sigmap_8h.md#aef672312a16d80f9d72648642f301e27)#define ESP\_PCNT\_CTRL\_CH0\_IN7 81

[ 169](esp32-gpio-sigmap_8h.md#ab408070e7c700805db165c3876b6c588)#define ESP\_LEDC\_LS\_SIG\_OUT2 81

[ 170](esp32-gpio-sigmap_8h.md#a8e7561886c8adb74a97f9cf2e1bf9474)#define ESP\_PCNT\_CTRL\_CH1\_IN7 82

[ 171](esp32-gpio-sigmap_8h.md#a438aee217c6c94a2962a3d98935b5717)#define ESP\_LEDC\_LS\_SIG\_OUT3 82

[ 172](esp32-gpio-sigmap_8h.md#ad9bae9b4884a356e465656d1ee8d61cd)#define ESP\_RMT\_SIG\_IN0 83

[ 173](esp32-gpio-sigmap_8h.md#ada93dcffffc15362be4b7432a8033559)#define ESP\_LEDC\_LS\_SIG\_OUT4 83

[ 174](esp32-gpio-sigmap_8h.md#ab6c6293e6845ba4bf4d05b84102ffdcf)#define ESP\_RMT\_SIG\_IN1 84

[ 175](esp32-gpio-sigmap_8h.md#a34fc029ec45756ca7064580f57db1cc7)#define ESP\_LEDC\_LS\_SIG\_OUT5 84

[ 176](esp32-gpio-sigmap_8h.md#af88ebdd0d2d02ac58d720c001ccc155b)#define ESP\_RMT\_SIG\_IN2 85

[ 177](esp32-gpio-sigmap_8h.md#a28b01adea7e0bcc8b76fe05d58c1cbd0)#define ESP\_LEDC\_LS\_SIG\_OUT6 85

[ 178](esp32-gpio-sigmap_8h.md#a1f930cd82690248b839f16ff7738f32c)#define ESP\_RMT\_SIG\_IN3 86

[ 179](esp32-gpio-sigmap_8h.md#a2ea140f2da1a15b24dcaa3592909ca35)#define ESP\_LEDC\_LS\_SIG\_OUT7 86

[ 180](esp32-gpio-sigmap_8h.md#abb899bebca2479d2f3da6f125ecfee6d)#define ESP\_RMT\_SIG\_IN4 87

[ 181](esp32-gpio-sigmap_8h.md#a25343fbc20a0c542bcdc21cdfade867b)#define ESP\_RMT\_SIG\_OUT0 87

[ 182](esp32-gpio-sigmap_8h.md#a714a3df55af99e8661d4954d3f15b82b)#define ESP\_RMT\_SIG\_IN5 88

[ 183](esp32-gpio-sigmap_8h.md#a6d082fb1c7397d784a3075108e0dea73)#define ESP\_RMT\_SIG\_OUT1 88

[ 184](esp32-gpio-sigmap_8h.md#adbd91079070e29944373c581f0a71648)#define ESP\_RMT\_SIG\_IN6 89

[ 185](esp32-gpio-sigmap_8h.md#ad657c1ddcf9c335ac7876464b80b2705)#define ESP\_RMT\_SIG\_OUT2 89

[ 186](esp32-gpio-sigmap_8h.md#a5ebafc69aa5f118c0cc979e61e02a275)#define ESP\_RMT\_SIG\_IN7 90

[ 187](esp32-gpio-sigmap_8h.md#ae60033bb70ca9ff7c2b52368d24a8ab8)#define ESP\_RMT\_SIG\_OUT3 90

[ 188](esp32-gpio-sigmap_8h.md#a9c614eec345307660df0d575a388fc18)#define ESP\_RMT\_SIG\_OUT4 91

[ 189](esp32-gpio-sigmap_8h.md#a0d230c83605e61e777367c964e9adf50)#define ESP\_RMT\_SIG\_OUT5 92

[ 190](esp32-gpio-sigmap_8h.md#ae49b4527d8fbd0f5c8e3edc72704c54a)#define ESP\_EXT\_ADC\_START 93

[ 191](esp32-gpio-sigmap_8h.md#ac064d26fd0af1e07ff3e4f6a65eb96d6)#define ESP\_RMT\_SIG\_OUT6 93

[ 192](esp32-gpio-sigmap_8h.md#ab3da303c2f9226f9648669c17af8377a)#define ESP\_TWAI\_RX 94

[ 193](esp32-gpio-sigmap_8h.md#ae677e5752545b920c4ec1a1af2ba62d7)#define ESP\_CAN\_RX ESP\_TWAI\_RX

[ 194](esp32-gpio-sigmap_8h.md#acade07ae7ae28a41d56938238dbcb243)#define ESP\_RMT\_SIG\_OUT7 94

[ 195](esp32-gpio-sigmap_8h.md#a1b6324b294e9e018a5909427f4f0ba36)#define ESP\_I2CEXT1\_SCL\_IN 95

[ 196](esp32-gpio-sigmap_8h.md#a3ac49ff21fcb59eeab6350821f9107e5)#define ESP\_I2CEXT1\_SCL\_OUT 95

[ 197](esp32-gpio-sigmap_8h.md#abb571ec9f2a59fc281837ca8bd3f2daa)#define ESP\_I2CEXT1\_SDA\_IN 96

[ 198](esp32-gpio-sigmap_8h.md#a3922109459dfd033147e4daf1ed4cd32)#define ESP\_I2CEXT1\_SDA\_OUT 96

[ 199](esp32-gpio-sigmap_8h.md#a13ae6d0ee0d8ddf620510da5e798e891)#define ESP\_HOST\_CARD\_DETECT\_N\_1 97

[ 200](esp32-gpio-sigmap_8h.md#a9f4b256b7638344a20473c7c26636dc7)#define ESP\_HOST\_CCMD\_OD\_PULLUP\_EN\_N 97

[ 201](esp32-gpio-sigmap_8h.md#ade4729b566a4c2c832a904e25855ff6c)#define ESP\_HOST\_CARD\_DETECT\_N\_2 98

[ 202](esp32-gpio-sigmap_8h.md#ae508559cba27c21b34bcdbdde8996205)#define ESP\_HOST\_RST\_N\_1 98

[ 203](esp32-gpio-sigmap_8h.md#a3c789c83cee9adb9e7de20379e3e9920)#define ESP\_HOST\_CARD\_WRITE\_PRT\_1 99

[ 204](esp32-gpio-sigmap_8h.md#a3c6ce500141f358b2b646250eb08cf63)#define ESP\_HOST\_RST\_N\_2 99

[ 205](esp32-gpio-sigmap_8h.md#ab9a2b7cc8d56cf5e1b84ccc79b150777)#define ESP\_HOST\_CARD\_WRITE\_PRT\_2 100

[ 206](esp32-gpio-sigmap_8h.md#ae59035f8269ccd564ba0d7b2b078b3ee)#define ESP\_GPIO\_SD0\_OUT 100

[ 207](esp32-gpio-sigmap_8h.md#afcf037aca22111997331336e4e61b758)#define ESP\_HOST\_CARD\_INT\_N\_1 101

[ 208](esp32-gpio-sigmap_8h.md#a3fbed77581ed14fa077f314e812b9c36)#define ESP\_GPIO\_SD1\_OUT 101

[ 209](esp32-gpio-sigmap_8h.md#a2627ab7d6dfe0820ad06168d71b2c521)#define ESP\_HOST\_CARD\_INT\_N\_2 102

[ 210](esp32-gpio-sigmap_8h.md#a2668d9083ce28563cc160fe1102e927d)#define ESP\_GPIO\_SD2\_OUT 102

[ 211](esp32-gpio-sigmap_8h.md#a9f251384f8a6a10b0fb173c4bfda88ba)#define ESP\_PWM1\_SYNC0\_IN 103

[ 212](esp32-gpio-sigmap_8h.md#a9d34f616894f98d7175c41b4ba565f8d)#define ESP\_GPIO\_SD3\_OUT 103

[ 213](esp32-gpio-sigmap_8h.md#a646d7d644b5d4ec403eab7ff793cf7b2)#define ESP\_PWM1\_SYNC1\_IN 104

[ 214](esp32-gpio-sigmap_8h.md#aa88cedc2785b1e25a21ac70dd5603e68)#define ESP\_GPIO\_SD4\_OUT 104

[ 215](esp32-gpio-sigmap_8h.md#a56a67f8e168a4e7545e3ca4bcf7c8d89)#define ESP\_PWM1\_SYNC2\_IN 105

[ 216](esp32-gpio-sigmap_8h.md#af0841a01cf24e79a447daa58a48db9f8)#define ESP\_GPIO\_SD5\_OUT 105

[ 217](esp32-gpio-sigmap_8h.md#a09c262c332e65ccc9eb2d91d976958e3)#define ESP\_PWM1\_F0\_IN 106

[ 218](esp32-gpio-sigmap_8h.md#a8c16952c92f5b28cd39b99771ccb983b)#define ESP\_GPIO\_SD6\_OUT 106

[ 219](esp32-gpio-sigmap_8h.md#af4b1c0ff4e222f09eee18cbb85cedb67)#define ESP\_PWM1\_F1\_IN 107

[ 220](esp32-gpio-sigmap_8h.md#a7fd22ae53413e708e4b75ad57e1be34a)#define ESP\_GPIO\_SD7\_OUT 107

[ 221](esp32-gpio-sigmap_8h.md#ac911f11a68e10d359cffe49864739e2d)#define ESP\_PWM1\_F2\_IN 108

[ 222](esp32-gpio-sigmap_8h.md#a4f8f7187a2a8dbf4b104e3a7e7bd5dae)#define ESP\_PWM1\_OUT0A 108

[ 223](esp32-gpio-sigmap_8h.md#a421b59e20586b4f48b7e81bfa0ad4357)#define ESP\_PWM0\_CAP0\_IN 109

[ 224](esp32-gpio-sigmap_8h.md#a553561934aa817659a5c781dfeccfc3e)#define ESP\_PWM1\_OUT0B 109

[ 225](esp32-gpio-sigmap_8h.md#aea7a8712f1502df47721258470ff5b48)#define ESP\_PWM0\_CAP1\_IN 110

[ 226](esp32-gpio-sigmap_8h.md#a852f0b23fd2c3d2f90b6bcfccd5f375e)#define ESP\_PWM1\_OUT1A 110

[ 227](esp32-gpio-sigmap_8h.md#ab221240161be67a0f5af577494c8a5ad)#define ESP\_PWM0\_CAP2\_IN 111

[ 228](esp32-gpio-sigmap_8h.md#ab9bc2ae5e0e53935f8b58380dfd397e8)#define ESP\_PWM1\_OUT1B 111

[ 229](esp32-gpio-sigmap_8h.md#a8f2dcd1f46c2a5a5da3be188dca9e3a0)#define ESP\_PWM1\_CAP0\_IN 112

[ 230](esp32-gpio-sigmap_8h.md#a8beedf183380bfe83c435f9c5920215e)#define ESP\_PWM1\_OUT2A 112

[ 231](esp32-gpio-sigmap_8h.md#a8b97c639d66dcb8400aefc344bf490d1)#define ESP\_PWM1\_CAP1\_IN 113

[ 232](esp32-gpio-sigmap_8h.md#ae1976c33c4e94a76d09ee5c3aa93f04e)#define ESP\_PWM1\_OUT2B 113

[ 233](esp32-gpio-sigmap_8h.md#a23b8540974bcf9dbd5c0ff92d9b69ac9)#define ESP\_PWM1\_CAP2\_IN 114

[ 234](esp32-gpio-sigmap_8h.md#a753b38e12b1f85b784fde4a2e5fe32dd)#define ESP\_PWM2\_OUT1H 114

[ 235](esp32-gpio-sigmap_8h.md#a74f13800576db201b1fd1d7a9bb524a9)#define ESP\_PWM2\_FLTA 115

[ 236](esp32-gpio-sigmap_8h.md#a4c2fa0f40cee1cecdd005a59a425f6d6)#define ESP\_PWM2\_OUT1L 115

[ 237](esp32-gpio-sigmap_8h.md#a8c099a688fb38f70e0ccb612e06b9660)#define ESP\_PWM2\_FLTB 116

[ 238](esp32-gpio-sigmap_8h.md#ae4f80ffadc78379f72d144f2a11a0206)#define ESP\_PWM2\_OUT2H 116

[ 239](esp32-gpio-sigmap_8h.md#a8579ce8c805c3c716ae2cb5f25bbe97c)#define ESP\_PWM2\_CAP1\_IN 117

[ 240](esp32-gpio-sigmap_8h.md#a7e9a685c18803840ba071883c07f06d7)#define ESP\_PWM2\_OUT2L 117

[ 241](esp32-gpio-sigmap_8h.md#a9d82c3bacb9e2b5bcf91b6e4dd0fd4da)#define ESP\_PWM2\_CAP2\_IN 118

[ 242](esp32-gpio-sigmap_8h.md#ad88de44d7bb5029b3c1a03d3794daf00)#define ESP\_PWM2\_OUT3H 118

[ 243](esp32-gpio-sigmap_8h.md#a2d35b94ffe6f71ba30df8a8310617c40)#define ESP\_PWM2\_CAP3\_IN 119

[ 244](esp32-gpio-sigmap_8h.md#a859e4b24d8586d5da9eeab47728dd452)#define ESP\_PWM2\_OUT3L 119

[ 245](esp32-gpio-sigmap_8h.md#a631090142094c0bda20be7ffb1f02a8c)#define ESP\_PWM3\_FLTA 120

[ 246](esp32-gpio-sigmap_8h.md#ab063692b7281339c45df0073a320c42c)#define ESP\_PWM2\_OUT4H 120

[ 247](esp32-gpio-sigmap_8h.md#a70c73eb9e03c8a13c421853cff0e0e23)#define ESP\_PWM3\_FLTB 121

[ 248](esp32-gpio-sigmap_8h.md#a9fa3278b518d107120ccc4ac0921e8c0)#define ESP\_PWM2\_OUT4L 121

[ 249](esp32-gpio-sigmap_8h.md#a5a55904f853eb6093af945d111c386ff)#define ESP\_PWM3\_CAP1\_IN 122

[ 250](esp32-gpio-sigmap_8h.md#a5daa89c51257d2795ba15b7cb8dce579)#define ESP\_PWM3\_CAP2\_IN 123

[ 251](esp32-gpio-sigmap_8h.md#a3b13bb40583aaa0f85de982509247614)#define ESP\_TWAI\_TX 123

[ 252](esp32-gpio-sigmap_8h.md#a46ca3f4f0055cdf64523d8d41fcd1485)#define ESP\_CAN\_TX ESP\_TWAI\_TX

[ 253](esp32-gpio-sigmap_8h.md#a491b268fd8a94e272df6f8aac3c0035d)#define ESP\_PWM3\_CAP3\_IN 124

[ 254](esp32-gpio-sigmap_8h.md#a6d0d41d1ec0f6fc626861f5857684e6d)#define ESP\_TWAI\_BUS\_OFF\_ON 124

[ 255](esp32-gpio-sigmap_8h.md#a11d09cd4c1511f60cc4e62fd0d08cc14)#define ESP\_CAN\_BUS\_OFF\_ON ESP\_TWAI\_BUS\_OFF\_ON

[ 256](esp32-gpio-sigmap_8h.md#a1c69791269fdbb2a11f66f33eb4066be)#define ESP\_TWAI\_CLKOUT 125

[ 257](esp32-gpio-sigmap_8h.md#adcdcf8cf367f5e300a0ef24e5242e24e)#define ESP\_CAN\_CLKOUT ESP\_TWAI\_CLKOUT

[ 258](esp32-gpio-sigmap_8h.md#ade124a5a82af0f49b122b32d69ee8d04)#define ESP\_SPID4\_IN 128

[ 259](esp32-gpio-sigmap_8h.md#a9bd0335c81e6828a5da77af387fbe845)#define ESP\_SPID4\_OUT 128

[ 260](esp32-gpio-sigmap_8h.md#ae8fa56cbc73756ff3895a937ab1374c2)#define ESP\_SPID5\_IN 129

[ 261](esp32-gpio-sigmap_8h.md#a61317dd1e2daf50f35240fd561180628)#define ESP\_SPID5\_OUT 129

[ 262](esp32-gpio-sigmap_8h.md#a2d850da0ce491f0049b9920cde48907e)#define ESP\_SPID6\_IN 130

[ 263](esp32-gpio-sigmap_8h.md#a918e6203f9d52d8d2606616a938faea8)#define ESP\_SPID6\_OUT 130

[ 264](esp32-gpio-sigmap_8h.md#a78073d0d570a71824e00bebe4bbd97d1)#define ESP\_SPID7\_IN 131

[ 265](esp32-gpio-sigmap_8h.md#a0802cd16128bd289444b670a827d0d31)#define ESP\_SPID7\_OUT 131

[ 266](esp32-gpio-sigmap_8h.md#a505ba36f1599fde5e0d3fb3e7fee48e8)#define ESP\_HSPID4\_IN 132

[ 267](esp32-gpio-sigmap_8h.md#ab0b0a1c8b8853e8f0ee32520fda3e60a)#define ESP\_HSPID4\_OUT 132

[ 268](esp32-gpio-sigmap_8h.md#aff173225a50d084c8a2eba896bc1d997)#define ESP\_HSPID5\_IN 133

[ 269](esp32-gpio-sigmap_8h.md#a93e270e899394753396e1169788514fd)#define ESP\_HSPID5\_OUT 133

[ 270](esp32-gpio-sigmap_8h.md#ad4f964c0362c9bfa048ea9d088bd664b)#define ESP\_HSPID6\_IN 134

[ 271](esp32-gpio-sigmap_8h.md#acc7e51ae7ce29705de1b21fb73ce47b2)#define ESP\_HSPID6\_OUT 134

[ 272](esp32-gpio-sigmap_8h.md#a900bbb4a69611c3555229ecff07d6884)#define ESP\_HSPID7\_IN 135

[ 273](esp32-gpio-sigmap_8h.md#a3c4fef7fa93c2d8e58391867d08a76db)#define ESP\_HSPID7\_OUT 135

[ 274](esp32-gpio-sigmap_8h.md#a2b113b6c0e20b45e6d6eb46e68fffc61)#define ESP\_VSPID4\_IN 136

[ 275](esp32-gpio-sigmap_8h.md#a66a6ee40ae8cfe23fe1ebaf725dae520)#define ESP\_VSPID4\_OUT 136

[ 276](esp32-gpio-sigmap_8h.md#a8b992ce66e57278426a55c8a8eb8bfb4)#define ESP\_VSPID5\_IN 137

[ 277](esp32-gpio-sigmap_8h.md#afd44862cfff0e324ad97277f7a683f90)#define ESP\_VSPID5\_OUT 137

[ 278](esp32-gpio-sigmap_8h.md#a2bc2b10d868874d9425c7e14dc9ae8ae)#define ESP\_VSPID6\_IN 138

[ 279](esp32-gpio-sigmap_8h.md#ab715945639b250cd34d675c72b0dd3d0)#define ESP\_VSPID6\_OUT 138

[ 280](esp32-gpio-sigmap_8h.md#a27c874bce841f39f8341b5b86a5f319f)#define ESP\_VSPID7\_IN 139

[ 281](esp32-gpio-sigmap_8h.md#a6f0007738394059a68b7973b8f4c4b14)#define ESP\_VSPID7\_OUT 139

[ 282](esp32-gpio-sigmap_8h.md#a433c8fb715a07f27d4b2bcea31b92129)#define ESP\_I2S0I\_DATA\_IN0 140

[ 283](esp32-gpio-sigmap_8h.md#a25101d2b16ca73d9e342a77f6c2fd517)#define ESP\_I2S0O\_DATA\_OUT0 140

[ 284](esp32-gpio-sigmap_8h.md#a8fdcb030022fc73f03b8b614ec031266)#define ESP\_I2S0I\_DATA\_IN1 141

[ 285](esp32-gpio-sigmap_8h.md#ac3656eb3c8ac2d66cc4f9099d486325b)#define ESP\_I2S0O\_DATA\_OUT1 141

[ 286](esp32-gpio-sigmap_8h.md#acb82a70ab66b67c43c3df4af940afd20)#define ESP\_I2S0I\_DATA\_IN2 142

[ 287](esp32-gpio-sigmap_8h.md#a87405dd9815c0e43d3dc865aa7459cae)#define ESP\_I2S0O\_DATA\_OUT2 142

[ 288](esp32-gpio-sigmap_8h.md#af5f006ccd7b9017a077cb19b7e8584a3)#define ESP\_I2S0I\_DATA\_IN3 143

[ 289](esp32-gpio-sigmap_8h.md#ad0e3c64912151b36169741ada3f5aa0b)#define ESP\_I2S0O\_DATA\_OUT3 143

[ 290](esp32-gpio-sigmap_8h.md#a580ec97414913d720035de8df140ce2e)#define ESP\_I2S0I\_DATA\_IN4 144

[ 291](esp32-gpio-sigmap_8h.md#abeb5e69293e78ceff31a7ed908864367)#define ESP\_I2S0O\_DATA\_OUT4 144

[ 292](esp32-gpio-sigmap_8h.md#a9d72aac34e99ec34569006dbe140f658)#define ESP\_I2S0I\_DATA\_IN5 145

[ 293](esp32-gpio-sigmap_8h.md#a93af307990b79a253c9be03d0831f175)#define ESP\_I2S0O\_DATA\_OUT5 145

[ 294](esp32-gpio-sigmap_8h.md#aed35437eb068e4ea079d8755928161c3)#define ESP\_I2S0I\_DATA\_IN6 146

[ 295](esp32-gpio-sigmap_8h.md#ace1b34e6050863a54792e6ac3c965ab8)#define ESP\_I2S0O\_DATA\_OUT6 146

[ 296](esp32-gpio-sigmap_8h.md#a0a04fda280abc577acf3e20d7a917cc8)#define ESP\_I2S0I\_DATA\_IN7 147

[ 297](esp32-gpio-sigmap_8h.md#a789d483001496ba193846e90fcc70e74)#define ESP\_I2S0O\_DATA\_OUT7 147

[ 298](esp32-gpio-sigmap_8h.md#ae144f14b04fff35537effc847a2a6520)#define ESP\_I2S0I\_DATA\_IN8 148

[ 299](esp32-gpio-sigmap_8h.md#a8360e859e714712978c0108b2fd7f8b3)#define ESP\_I2S0O\_DATA\_OUT8 148

[ 300](esp32-gpio-sigmap_8h.md#a54b5575c98e2b363e1cfd556421788d5)#define ESP\_I2S0I\_DATA\_IN9 149

[ 301](esp32-gpio-sigmap_8h.md#a0f347fca42d8d9e9bbf1f46a8c05ee84)#define ESP\_I2S0O\_DATA\_OUT9 149

[ 302](esp32-gpio-sigmap_8h.md#a36fd66f4834eb96ba5f1ab7560230065)#define ESP\_I2S0I\_DATA\_IN10 150

[ 303](esp32-gpio-sigmap_8h.md#a789443eb05c68f28a9fa99ff43bd3aa4)#define ESP\_I2S0O\_DATA\_OUT10 150

[ 304](esp32-gpio-sigmap_8h.md#a601911b70e67c09b0bee13be965ea023)#define ESP\_I2S0I\_DATA\_IN11 151

[ 305](esp32-gpio-sigmap_8h.md#ac8c4f8238d7ac8d3610ad7d817b59f0c)#define ESP\_I2S0O\_DATA\_OUT11 151

[ 306](esp32-gpio-sigmap_8h.md#a1d6581f56d31224a7fe2b2767c815e17)#define ESP\_I2S0I\_DATA\_IN12 152

[ 307](esp32-gpio-sigmap_8h.md#a1817a5bb7d7c6f81189d61844c9369d8)#define ESP\_I2S0O\_DATA\_OUT12 152

[ 308](esp32-gpio-sigmap_8h.md#a429e25483385ad62fb5d25e25ab16bd1)#define ESP\_I2S0I\_DATA\_IN13 153

[ 309](esp32-gpio-sigmap_8h.md#a4315e0aa620576457d3fe5543daf8a74)#define ESP\_I2S0O\_DATA\_OUT13 153

[ 310](esp32-gpio-sigmap_8h.md#ac9a9df57a89820c2eb0f3af2ca49fc71)#define ESP\_I2S0I\_DATA\_IN14 154

[ 311](esp32-gpio-sigmap_8h.md#a60cd35bc47b224db197844526ed31562)#define ESP\_I2S0O\_DATA\_OUT14 154

[ 312](esp32-gpio-sigmap_8h.md#a1c65e11dbd846847daad7fc716955e64)#define ESP\_I2S0I\_DATA\_IN15 155

[ 313](esp32-gpio-sigmap_8h.md#a39a667893007777d45fdcf3c9df17441)#define ESP\_I2S0O\_DATA\_OUT15 155

[ 314](esp32-gpio-sigmap_8h.md#a5f6c0a7cf37eec066127d6cfc6fc8558)#define ESP\_I2S0O\_DATA\_OUT16 156

[ 315](esp32-gpio-sigmap_8h.md#aaa92d37d180f429df167101a6bcde85f)#define ESP\_I2S0O\_DATA\_OUT17 157

[ 316](esp32-gpio-sigmap_8h.md#a1f4f2d0a3535c025d6581e4232bb7fd9)#define ESP\_I2S0O\_DATA\_OUT18 158

[ 317](esp32-gpio-sigmap_8h.md#a6676ad67342db70105683dddae6259a2)#define ESP\_I2S0O\_DATA\_OUT19 159

[ 318](esp32-gpio-sigmap_8h.md#a2d1be2072be7af3e41d25928de743b6e)#define ESP\_I2S0O\_DATA\_OUT20 160

[ 319](esp32-gpio-sigmap_8h.md#a934a97b4ba3f7729b93828fbcfe31c93)#define ESP\_I2S0O\_DATA\_OUT21 161

[ 320](esp32-gpio-sigmap_8h.md#a30d03be995708ac60420d0199d8b2b67)#define ESP\_I2S0O\_DATA\_OUT22 162

[ 321](esp32-gpio-sigmap_8h.md#a4fa877e0f38365b7f18fe4cb04c865a6)#define ESP\_I2S0O\_DATA\_OUT23 163

[ 322](esp32-gpio-sigmap_8h.md#a537fd0715c03fd03d914d72d01191b9a)#define ESP\_I2S1I\_BCK\_IN 164

[ 323](esp32-gpio-sigmap_8h.md#a93d4d6602af3ba29121fef124145f4a5)#define ESP\_I2S1I\_BCK\_OUT 164

[ 324](esp32-gpio-sigmap_8h.md#a90b7c81877f6ab8ec1af498db7b8dc0e)#define ESP\_I2S1I\_WS\_IN 165

[ 325](esp32-gpio-sigmap_8h.md#a1ed428a9dd21d57a7311c24f192e032e)#define ESP\_I2S1I\_WS\_OUT 165

[ 326](esp32-gpio-sigmap_8h.md#a9d1dc7d4111b61424340211e781ea69f)#define ESP\_I2S1I\_DATA\_IN0 166

[ 327](esp32-gpio-sigmap_8h.md#ab84e1317095fb6bfa3430fe89bc224a5)#define ESP\_I2S1O\_DATA\_OUT0 166

[ 328](esp32-gpio-sigmap_8h.md#ae6785d70222fdbbafd35d071d0cdb0e4)#define ESP\_I2S1I\_DATA\_IN1 167

[ 329](esp32-gpio-sigmap_8h.md#aaa2d63ff218a8076af7f2b3660568ca8)#define ESP\_I2S1O\_DATA\_OUT1 167

[ 330](esp32-gpio-sigmap_8h.md#a5da7649d7b767380f6f2f71b77cf8bba)#define ESP\_I2S1I\_DATA\_IN2 168

[ 331](esp32-gpio-sigmap_8h.md#a784456ac7505866a951f95743eb64ad9)#define ESP\_I2S1O\_DATA\_OUT2 168

[ 332](esp32-gpio-sigmap_8h.md#aa558326938553d7c2d46e517e40c5d04)#define ESP\_I2S1I\_DATA\_IN3 169

[ 333](esp32-gpio-sigmap_8h.md#addfba96887c05f004e5269e4a4cd79cb)#define ESP\_I2S1O\_DATA\_OUT3 169

[ 334](esp32-gpio-sigmap_8h.md#acab17ad09415adc40ab1e667892083f9)#define ESP\_I2S1I\_DATA\_IN4 170

[ 335](esp32-gpio-sigmap_8h.md#ab64ac73a1315f81270960e63cb6ed03b)#define ESP\_I2S1O\_DATA\_OUT4 170

[ 336](esp32-gpio-sigmap_8h.md#ae2d0876f20d0de257d5eb09a359a6505)#define ESP\_I2S1I\_DATA\_IN5 171

[ 337](esp32-gpio-sigmap_8h.md#a51f7de3b3383b7aae4dd80d823d13de9)#define ESP\_I2S1O\_DATA\_OUT5 171

[ 338](esp32-gpio-sigmap_8h.md#a68f2324c96ea3232da52319d807914c6)#define ESP\_I2S1I\_DATA\_IN6 172

[ 339](esp32-gpio-sigmap_8h.md#ac62a71c9664aa54d9ff025e4b048f1e9)#define ESP\_I2S1O\_DATA\_OUT6 172

[ 340](esp32-gpio-sigmap_8h.md#a172ba0e7e04badee170f40ebe4de25f7)#define ESP\_I2S1I\_DATA\_IN7 173

[ 341](esp32-gpio-sigmap_8h.md#ac5b206725ee940c0fb263bab1d487beb)#define ESP\_I2S1O\_DATA\_OUT7 173

[ 342](esp32-gpio-sigmap_8h.md#a4618631d905b0e585889e096d33d2984)#define ESP\_I2S1I\_DATA\_IN8 174

[ 343](esp32-gpio-sigmap_8h.md#a1c2b0a187daf4c85eecacc7ec80d5390)#define ESP\_I2S1O\_DATA\_OUT8 174

[ 344](esp32-gpio-sigmap_8h.md#a1ddb0ee5a8bd7fe10c6751bd0f555b03)#define ESP\_I2S1I\_DATA\_IN9 175

[ 345](esp32-gpio-sigmap_8h.md#aa2b8df142ed103952ef28ecaa0b29211)#define ESP\_I2S1O\_DATA\_OUT9 175

[ 346](esp32-gpio-sigmap_8h.md#a7703547c6989806b67d55679bb49a4e2)#define ESP\_I2S1I\_DATA\_IN10 176

[ 347](esp32-gpio-sigmap_8h.md#a70bd885f98e86cbb8b6f902d50a7849b)#define ESP\_I2S1O\_DATA\_OUT10 176

[ 348](esp32-gpio-sigmap_8h.md#a5dca552908b449888450d37a1293bc38)#define ESP\_I2S1I\_DATA\_IN11 177

[ 349](esp32-gpio-sigmap_8h.md#a5b8850f0017ea7fc9400451ae6ddc5c9)#define ESP\_I2S1O\_DATA\_OUT11 177

[ 350](esp32-gpio-sigmap_8h.md#ae4667a8147f4134f4e7047336dd6b86e)#define ESP\_I2S1I\_DATA\_IN12 178

[ 351](esp32-gpio-sigmap_8h.md#a9ab14a7194f76ecd2098a20c4c9a7a85)#define ESP\_I2S1O\_DATA\_OUT12 178

[ 352](esp32-gpio-sigmap_8h.md#ad2144cf6647e3dbd41c6c39aa99774d7)#define ESP\_I2S1I\_DATA\_IN13 179

[ 353](esp32-gpio-sigmap_8h.md#ae55f123f6025af96f2080d712484b123)#define ESP\_I2S1O\_DATA\_OUT13 179

[ 354](esp32-gpio-sigmap_8h.md#abe0e8a8dd3b25ba528759f2d4a221648)#define ESP\_I2S1I\_DATA\_IN14 180

[ 355](esp32-gpio-sigmap_8h.md#ae5f72a0583f4c2493fbb3f05dff3ab9a)#define ESP\_I2S1O\_DATA\_OUT14 180

[ 356](esp32-gpio-sigmap_8h.md#a6efb5c5233ff10f5b78e2577d93b000a)#define ESP\_I2S1I\_DATA\_IN15 181

[ 357](esp32-gpio-sigmap_8h.md#ab0a2dc0591a1e75f00647ac61027cfc1)#define ESP\_I2S1O\_DATA\_OUT15 181

[ 358](esp32-gpio-sigmap_8h.md#a0e93229ac648d7a3f7669cceaead3d71)#define ESP\_I2S1O\_DATA\_OUT16 182

[ 359](esp32-gpio-sigmap_8h.md#a037301cb8f5f4ced97f0ff785e870bca)#define ESP\_I2S1O\_DATA\_OUT17 183

[ 360](esp32-gpio-sigmap_8h.md#ae8f469295056b0587b126a7145fff52a)#define ESP\_I2S1O\_DATA\_OUT18 184

[ 361](esp32-gpio-sigmap_8h.md#adfe0560be76144c27c19b1b5320fdd44)#define ESP\_I2S1O\_DATA\_OUT19 185

[ 362](esp32-gpio-sigmap_8h.md#a9d4d2f91b498ccdcae739eea987c5ab2)#define ESP\_I2S1O\_DATA\_OUT20 186

[ 363](esp32-gpio-sigmap_8h.md#ab9c22dce791b02172243e7c552d5844a)#define ESP\_I2S1O\_DATA\_OUT21 187

[ 364](esp32-gpio-sigmap_8h.md#aaf29fc7404162b609acda92d435137cd)#define ESP\_I2S1O\_DATA\_OUT22 188

[ 365](esp32-gpio-sigmap_8h.md#a8f70a80284b6d28c5946ae3fe3e6e523)#define ESP\_I2S1O\_DATA\_OUT23 189

[ 366](esp32-gpio-sigmap_8h.md#aee6979fc359bc990dac8c49371243697)#define ESP\_I2S0I\_H\_SYNC 190

[ 367](esp32-gpio-sigmap_8h.md#a05a84bb83d210e337787ff9c45c5cb61)#define ESP\_PWM3\_OUT1H 190

[ 368](esp32-gpio-sigmap_8h.md#a99829d36ae815041479b1327a03c9f0a)#define ESP\_I2S0I\_V\_SYNC 191

[ 369](esp32-gpio-sigmap_8h.md#aaf153ad217db09d6c01ad8819d5668e1)#define ESP\_PWM3\_OUT1L 191

[ 370](esp32-gpio-sigmap_8h.md#a933b9ae19e0f6cc02bdb202f7cd95b8c)#define ESP\_I2S0I\_H\_ENABLE 192

[ 371](esp32-gpio-sigmap_8h.md#a00bd2dcac50be50c6029d4de24a6f79e)#define ESP\_PWM3\_OUT2H 192

[ 372](esp32-gpio-sigmap_8h.md#a8687f02a776a320521c90879afbf5037)#define ESP\_I2S1I\_H\_SYNC 193

[ 373](esp32-gpio-sigmap_8h.md#a84e7640acf4ca35def262e9ea0b1a02e)#define ESP\_PWM3\_OUT2L 193

[ 374](esp32-gpio-sigmap_8h.md#a4de19b242ceb33bc1e5e40444a354794)#define ESP\_I2S1I\_V\_SYNC 194

[ 375](esp32-gpio-sigmap_8h.md#abcd90afa184c72bbc240e326701b2dc6)#define ESP\_PWM3\_OUT3H 194

[ 376](esp32-gpio-sigmap_8h.md#a9190b9d81f047f5f31fa11ea123a468e)#define ESP\_I2S1I\_H\_ENABLE 195

[ 377](esp32-gpio-sigmap_8h.md#aa792a2cc579f68ef0fff17978c02fb9d)#define ESP\_PWM3\_OUT3L 195

[ 378](esp32-gpio-sigmap_8h.md#ae01b405622ea50f62ba87d49d5fb4f82)#define ESP\_PWM3\_OUT4H 196

[ 379](esp32-gpio-sigmap_8h.md#aea0a96c204965f794806ce7c6013263b)#define ESP\_PWM3\_OUT4L 197

[ 380](esp32-gpio-sigmap_8h.md#abe46ead057c2b66d500ef07e8a84fe0f)#define ESP\_U2RXD\_IN 198

[ 381](esp32-gpio-sigmap_8h.md#a20baac10eb4b76603580e1ea7065213a)#define ESP\_U2TXD\_OUT 198

[ 382](esp32-gpio-sigmap_8h.md#a735a482aa723130ccb408f0fb7596a0a)#define ESP\_U2CTS\_IN 199

[ 383](esp32-gpio-sigmap_8h.md#a174b50e35d961ded056cea3848110b20)#define ESP\_U2RTS\_OUT 199

[ 384](esp32-gpio-sigmap_8h.md#a4569f8cb129de440a41616beff6b938b)#define ESP\_EMAC\_MDC\_I 200

[ 385](esp32-gpio-sigmap_8h.md#a2f2df30f4a55a81215948fdea44a04a7)#define ESP\_EMAC\_MDC\_O 200

[ 386](esp32-gpio-sigmap_8h.md#a12b04715f671516d1182830f5a725c8c)#define ESP\_EMAC\_MDI\_I 201

[ 387](esp32-gpio-sigmap_8h.md#a0451fae682abbbae4403c71563a0cc13)#define ESP\_EMAC\_MDO\_O 201

[ 388](esp32-gpio-sigmap_8h.md#a7502b28e820501ef7672eb073103bbca)#define ESP\_EMAC\_CRS\_I 202

[ 389](esp32-gpio-sigmap_8h.md#a639473ccf7cb6f4fb26cd16fa091be29)#define ESP\_EMAC\_CRS\_O 202

[ 390](esp32-gpio-sigmap_8h.md#af7dc8e7c55aa23adf5041c52066ba0f3)#define ESP\_EMAC\_COL\_I 203

[ 391](esp32-gpio-sigmap_8h.md#a35ee616dbcd0bad26525bbff33ffd72d)#define ESP\_EMAC\_COL\_O 203

[ 392](esp32-gpio-sigmap_8h.md#a0ad409b608ef2a418098b4e51d0e7e9a)#define ESP\_PCMFSYNC\_IN 204

[ 393](esp32-gpio-sigmap_8h.md#afd2befcf5eb0c413c0f8447558dc4863)#define ESP\_BT\_AUDIO0\_IRQ 204

[ 394](esp32-gpio-sigmap_8h.md#abb4d1f28362c68cf3f1e9f1696602b03)#define ESP\_PCMCLK\_IN 205

[ 395](esp32-gpio-sigmap_8h.md#acfe665b9ff21a51b93819a3f123180ad)#define ESP\_BT\_AUDIO1\_IRQ 205

[ 396](esp32-gpio-sigmap_8h.md#ae94f8dfc2be2c0cf8863a33df76d5295)#define ESP\_PCMDIN 206

[ 397](esp32-gpio-sigmap_8h.md#a77ac554a2a10fc6fa77106e8af9dfc86)#define ESP\_BT\_AUDIO2\_IRQ 206

[ 398](esp32-gpio-sigmap_8h.md#ab2e25b779a18acd66533795433291a3d)#define ESP\_BLE\_AUDIO0\_IRQ 207

[ 399](esp32-gpio-sigmap_8h.md#ab4b3d654c674536c2c63070210147372)#define ESP\_BLE\_AUDIO1\_IRQ 208

[ 400](esp32-gpio-sigmap_8h.md#a637ea6fcad7b2e5fe48cf9e3419fbed6)#define ESP\_BLE\_AUDIO2\_IRQ 209

[ 401](esp32-gpio-sigmap_8h.md#a8b79d6e15573a684058c9b933f469f09)#define ESP\_PCMFSYNC\_OUT 210

[ 402](esp32-gpio-sigmap_8h.md#a500651ca0d6daa86774a0f45190f8b38)#define ESP\_PCMCLK\_OUT 211

[ 403](esp32-gpio-sigmap_8h.md#ab3ecd7e5557112172c38bff3b2605e9c)#define ESP\_PCMDOUT 212

[ 404](esp32-gpio-sigmap_8h.md#aba2aea8feedc96a0a6b3bba007df49ac)#define ESP\_BLE\_AUDIO\_SYNC0\_P 213

[ 405](esp32-gpio-sigmap_8h.md#a21e5bf1c7c33a39f11d8bf6537ed85bb)#define ESP\_BLE\_AUDIO\_SYNC1\_P 214

[ 406](esp32-gpio-sigmap_8h.md#a961f37a0b2dcb9e183331ef5684f8504)#define ESP\_BLE\_AUDIO\_SYNC2\_P 215

[ 407](esp32-gpio-sigmap_8h.md#aec2dfb198f69d923686404a0a6330833)#define ESP\_ANT\_SEL0 216

[ 408](esp32-gpio-sigmap_8h.md#a15c080ea1e4c8e2db9f1640e9b8c4f0a)#define ESP\_ANT\_SEL1 217

[ 409](esp32-gpio-sigmap_8h.md#ae3042ff86ecc0f2e78ebe9477055e819)#define ESP\_ANT\_SEL2 218

[ 410](esp32-gpio-sigmap_8h.md#ab8e5cca4b9eb1a7bda7868ecd792c76d)#define ESP\_ANT\_SEL3 219

[ 411](esp32-gpio-sigmap_8h.md#a821cc4b81f76043b1ecb751118a2f416)#define ESP\_ANT\_SEL4 220

[ 412](esp32-gpio-sigmap_8h.md#a28a954881fd9d5f5e7ff25d715f0bcc2)#define ESP\_ANT\_SEL5 221

[ 413](esp32-gpio-sigmap_8h.md#a2122dad1966cbe214e9c82cb9a46bd8a)#define ESP\_ANT\_SEL6 222

[ 414](esp32-gpio-sigmap_8h.md#a8f9cedf15c49cee3fbac2a22df7675ec)#define ESP\_ANT\_SEL7 223

[ 415](esp32-gpio-sigmap_8h.md#a53d8822e6079bfdfa4f1e643af0c619e)#define ESP\_SIG\_IN\_FUNC224 224

[ 416](esp32-gpio-sigmap_8h.md#a3dc693b4e8606fc6ae6a7f576f3e5253)#define ESP\_SIG\_IN\_FUNC225 225

[ 417](esp32-gpio-sigmap_8h.md#a358aff28052633bbaf7fd267c89310bc)#define ESP\_SIG\_IN\_FUNC226 226

[ 418](esp32-gpio-sigmap_8h.md#a5e67275e2c4feb45990232eb79856ae0)#define ESP\_SIG\_IN\_FUNC227 227

[ 419](esp32-gpio-sigmap_8h.md#a58c1a730743d75abbf8967ec8edc02de)#define ESP\_SIG\_IN\_FUNC228 228

[ 420](esp32-gpio-sigmap_8h.md#a645411759ffdc63f51f2cd42632d2720)#define ESP\_SIG\_GPIO\_OUT 256

421

422/\* RTC-IO MUX \*/

[ 423](esp32-gpio-sigmap_8h.md#a8f9a1d5717dc093e1412c91bdab92b9c)#define ESP\_ADC1\_CH0 0

[ 424](esp32-gpio-sigmap_8h.md#a0daf4a421144f0121e0d28ca8dc7db34)#define ESP\_ADC1\_CH1 1

[ 425](esp32-gpio-sigmap_8h.md#a546eff66d04c69c705916a9707ad5699)#define ESP\_ADC1\_CH2 2

[ 426](esp32-gpio-sigmap_8h.md#a0f4c4c9e9ef0a49d3c855c537d296bc3)#define ESP\_ADC1\_CH3 3

[ 427](esp32-gpio-sigmap_8h.md#a3b8e642cc63f034ac2751aa7c8f50b4d)#define ESP\_ADC1\_CH6 4

[ 428](esp32-gpio-sigmap_8h.md#a3e1e8a6040fbf0a3bb7931c8e7c5a179)#define ESP\_ADC1\_CH7 5

[ 429](esp32-gpio-sigmap_8h.md#abb40001800391a6683f876ccf8dc1ab9)#define ESP\_ADC2\_CH8 6

[ 430](esp32-gpio-sigmap_8h.md#a4eb0d2ce846da9ab31ff7d96251a594d)#define ESP\_ADC2\_CH9 7

[ 431](esp32-gpio-sigmap_8h.md#aae161d452532910ddb4a916eb483358b)#define ESP\_DAC1\_OUT 6

[ 432](esp32-gpio-sigmap_8h.md#a7bff6832e7ea4df4dc5f3eb29601c7e7)#define ESP\_DAC2\_OUT 7

[ 433](esp32-gpio-sigmap_8h.md#af85ff915121094c9e7b78486c54db848)#define ESP\_ADC1\_CH5 8

[ 434](esp32-gpio-sigmap_8h.md#a60e74929edc167861259227292e64307)#define ESP\_ADC1\_CH4 9

[ 435](esp32-gpio-sigmap_8h.md#a7db119623e8c8434cb3d724b0d97391c)#define ESP\_ADC2\_CH0 10

[ 436](esp32-gpio-sigmap_8h.md#a597733c1b61ad742a28be41df9edc33e)#define ESP\_ADC2\_CH1 11

[ 437](esp32-gpio-sigmap_8h.md#aebb2be056176553f0102ec5f8dbec752)#define ESP\_ADC2\_CH2 12

[ 438](esp32-gpio-sigmap_8h.md#affd91511897a0013d19b58125eb7fcfe)#define ESP\_ADC2\_CH3 13

[ 439](esp32-gpio-sigmap_8h.md#a1a85c794198f40665d339118c74cc7e2)#define ESP\_ADC2\_CH4 14

[ 440](esp32-gpio-sigmap_8h.md#a1d8b7231d9b93934d78763ac64e59a09)#define ESP\_ADC2\_CH5 15

[ 441](esp32-gpio-sigmap_8h.md#a5a4861a6b871a91cd98d8c709d55a9b5)#define ESP\_ADC2\_CH6 16

[ 442](esp32-gpio-sigmap_8h.md#a3fa5b9a5dcb7661c47e309211d35fcb8)#define ESP\_ADC2\_CH7 17

443

444#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ESP32\_GPIO\_SIGMAP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32-gpio-sigmap.h](esp32-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
