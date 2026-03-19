---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-rp2350b-pinctrl_8h_source.html
original_path: doxygen/html/rpi-pico-rp2350b-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-rp2350b-pinctrl.h

[Go to the documentation of this file.](rpi-pico-rp2350b-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2024, Andrew Featherstone

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350B\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350B\_PINCTRL\_H\_

9

10#include "[rpi-pico-rp2350-pinctrl-common.h](rpi-pico-rp2350-pinctrl-common_8h.md)"

11

12/\* RP2350B is in a QFN-80 package, and extends the set of available pins

13 \* accordingly.

14 \*/

[ 15](rpi-pico-rp2350b-pinctrl_8h.md#ad5d0b3f75a32bb0a9c3e2abfb9429155)#define SPI1\_SCK\_P30 RP2XXX\_PINMUX(30, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 16](rpi-pico-rp2350b-pinctrl_8h.md#a4c9f1c7222c093b8d5edf6309449b01a)#define SPI1\_TX\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 17](rpi-pico-rp2350b-pinctrl_8h.md#a899258503856fc5caf14b6d18d65e49f)#define SPI0\_RX\_P32 RP2XXX\_PINMUX(32, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 18](rpi-pico-rp2350b-pinctrl_8h.md#a4d2750f9bf77de85a9f0bada2a4505e9)#define SPI0\_CSN\_P33 RP2XXX\_PINMUX(33, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 19](rpi-pico-rp2350b-pinctrl_8h.md#ac1ea9195dabf8cd1a250e9767d18111b)#define SPI0\_SCK\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 20](rpi-pico-rp2350b-pinctrl_8h.md#a5ad14f2549b5d1b724bdab9e4efd7449)#define SPI0\_TX\_P35 RP2XXX\_PINMUX(35, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 21](rpi-pico-rp2350b-pinctrl_8h.md#a42a37f64c1b4b7f28fab48b2f410f6c7)#define SPI0\_RX\_P36 RP2XXX\_PINMUX(36, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 22](rpi-pico-rp2350b-pinctrl_8h.md#adc5b0277694acddb6cea2167e730a17c)#define SPI0\_CSN\_P37 RP2XXX\_PINMUX(37, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 23](rpi-pico-rp2350b-pinctrl_8h.md#ac38f8fa40f233fc37053b501475ea2ad)#define SPI0\_SCK\_P38 RP2XXX\_PINMUX(38, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 24](rpi-pico-rp2350b-pinctrl_8h.md#a217dcd916c1a5afe0d16b45858e5b6ff)#define SPI0\_TX\_P39 RP2XXX\_PINMUX(39, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 25](rpi-pico-rp2350b-pinctrl_8h.md#a01bf1bbab8d7a19595ec80db2ff0ed64)#define SPI1\_RX\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 26](rpi-pico-rp2350b-pinctrl_8h.md#a191aa260e80ebc6565980b5222b22c2a)#define SPI1\_CSN\_P41 RP2XXX\_PINMUX(41, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 27](rpi-pico-rp2350b-pinctrl_8h.md#a49ea5f7c29273d1ec5c41d4baf5077aa)#define SPI1\_SCK\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 28](rpi-pico-rp2350b-pinctrl_8h.md#a914591547e6949987f1bb4ad702b875f)#define SPI1\_TX\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 29](rpi-pico-rp2350b-pinctrl_8h.md#aab41ff6333d39f683c72de23cfb210b0)#define SPI1\_RX\_P44 RP2XXX\_PINMUX(44, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 30](rpi-pico-rp2350b-pinctrl_8h.md#ad661bcd1e102b81cef0bde4b96046b6b)#define SPI1\_CSN\_P45 RP2XXX\_PINMUX(45, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 31](rpi-pico-rp2350b-pinctrl_8h.md#a96df05ca647f2ec77d4ad9429f195637)#define SPI1\_SCK\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 32](rpi-pico-rp2350b-pinctrl_8h.md#a5b905d7a6717f4793d5ae634bc90e95a)#define SPI1\_TX\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

33

[ 34](rpi-pico-rp2350b-pinctrl_8h.md#ace4aac066552328332f8eeed5941967a)#define UART1\_TX\_P30 RP2XXX\_PINMUX(30, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 35](rpi-pico-rp2350b-pinctrl_8h.md#aac830556ba23f71bf26944c020871e3c)#define UART1\_RX\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 36](rpi-pico-rp2350b-pinctrl_8h.md#a14cd5d0b530176314db1fede2c9dc35e)#define UART0\_TX\_P32 RP2XXX\_PINMUX(32, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 37](rpi-pico-rp2350b-pinctrl_8h.md#ace53e57831ed02f4a19d1e762cb3bb9a)#define UART0\_RX\_P33 RP2XXX\_PINMUX(33, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 38](rpi-pico-rp2350b-pinctrl_8h.md#a2c4a783e530fd7db22f5cea4ce1f0ed2)#define UART1\_TX\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 39](rpi-pico-rp2350b-pinctrl_8h.md#a4884bb98b842809559c5dfda7e2c9885)#define UART1\_RX\_P35 RP2XXX\_PINMUX(35, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 40](rpi-pico-rp2350b-pinctrl_8h.md#a2cf941bc91e3bfb3de8fc96dfa5fa420)#define UART0\_TX\_P36 RP2XXX\_PINMUX(36, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 41](rpi-pico-rp2350b-pinctrl_8h.md#aaef212cd6289e0b58b3402e2498608ed)#define UART0\_RX\_P37 RP2XXX\_PINMUX(37, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 42](rpi-pico-rp2350b-pinctrl_8h.md#adc93a71b93d16dc807f6d20d29e500c3)#define UART1\_TX\_P38 RP2XXX\_PINMUX(38, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 43](rpi-pico-rp2350b-pinctrl_8h.md#a92211ecbdc150be1494b0d8641da9539)#define UART1\_RX\_P39 RP2XXX\_PINMUX(39, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 44](rpi-pico-rp2350b-pinctrl_8h.md#ada639bb3195d4d2a1f4ef9a162354372)#define UART0\_TX\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 45](rpi-pico-rp2350b-pinctrl_8h.md#a775aa5c875e7e7a66af34e4e4fe19843)#define UART0\_RX\_P41 RP2XXX\_PINMUX(41, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 46](rpi-pico-rp2350b-pinctrl_8h.md#addf36c1b23c7b50ff1cdb5236317fd40)#define UART1\_TX\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 47](rpi-pico-rp2350b-pinctrl_8h.md#a2baa50464a888ff86badb4e1a5cbbfcf)#define UART1\_RX\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 48](rpi-pico-rp2350b-pinctrl_8h.md#a10a3a9d61574464b7a60d2e8d03129c8)#define UART0\_TX\_P44 RP2XXX\_PINMUX(44, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 49](rpi-pico-rp2350b-pinctrl_8h.md#aec30ecff2290ff162f4940376f092f77)#define UART0\_RX\_P45 RP2XXX\_PINMUX(45, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 50](rpi-pico-rp2350b-pinctrl_8h.md#a0d9aa7840d2e5f73dd4e9330219a6cd2)#define UART1\_TX\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 51](rpi-pico-rp2350b-pinctrl_8h.md#a9ba06deadbbb8f53c57e42097bd5cfb8)#define UART1\_RX\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

52

[ 53](rpi-pico-rp2350b-pinctrl_8h.md#aa45a418da0fa338318e81a6fd6b9ead4)#define I2C1\_SDA\_P30 RP2XXX\_PINMUX(30, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 54](rpi-pico-rp2350b-pinctrl_8h.md#a3c3a70423afbdb9b954c21271cb64bd3)#define I2C1\_SCL\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 55](rpi-pico-rp2350b-pinctrl_8h.md#a185015add569d82f6c39da049c4a9a78)#define I2C0\_SDA\_P32 RP2XXX\_PINMUX(32, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 56](rpi-pico-rp2350b-pinctrl_8h.md#adec124ea42b18f478783a3a43eca4516)#define I2C0\_SCL\_P33 RP2XXX\_PINMUX(33, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 57](rpi-pico-rp2350b-pinctrl_8h.md#af1d705eb5c74079240506ac1e8d236d2)#define I2C1\_SDA\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 58](rpi-pico-rp2350b-pinctrl_8h.md#ace898481159c8254d1189ecfe288e8e0)#define I2C1\_SCL\_P35 RP2XXX\_PINMUX(35, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 59](rpi-pico-rp2350b-pinctrl_8h.md#a67523b661dc40a6fc8456b8a940f6115)#define I2C0\_SDA\_P36 RP2XXX\_PINMUX(36, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 60](rpi-pico-rp2350b-pinctrl_8h.md#afa99858df29120beb3f153d75584b887)#define I2C0\_SCL\_P37 RP2XXX\_PINMUX(37, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 61](rpi-pico-rp2350b-pinctrl_8h.md#af1d79311eec4563883628fbaf1521df0)#define I2C1\_SDA\_P38 RP2XXX\_PINMUX(38, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 62](rpi-pico-rp2350b-pinctrl_8h.md#a56abbe8cbc57f4a42db9d23783b93526)#define I2C1\_SCL\_P39 RP2XXX\_PINMUX(39, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 63](rpi-pico-rp2350b-pinctrl_8h.md#a8b71949766a6b0384a52a1c15618127d)#define I2C0\_SDA\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 64](rpi-pico-rp2350b-pinctrl_8h.md#a34bd7ddd98d6715f0c6e38d51e19e341)#define I2C0\_SCL\_P41 RP2XXX\_PINMUX(41, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 65](rpi-pico-rp2350b-pinctrl_8h.md#a70f58127e100890f9de119a0dfba2e1e)#define I2C1\_SDA\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 66](rpi-pico-rp2350b-pinctrl_8h.md#a57a77a15b315637792d53b339154c4e4)#define I2C1\_SCL\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 67](rpi-pico-rp2350b-pinctrl_8h.md#afe3ed2b7953bf377cb4fd98b1f9430a3)#define I2C0\_SDA\_P44 RP2XXX\_PINMUX(44, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 68](rpi-pico-rp2350b-pinctrl_8h.md#a09e0c9c28e4c7273dc4d0c933c653f12)#define I2C0\_SCL\_P45 RP2XXX\_PINMUX(45, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 69](rpi-pico-rp2350b-pinctrl_8h.md#a084d5a889b1be2dad8fec98542df0326)#define I2C1\_SDA\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 70](rpi-pico-rp2350b-pinctrl_8h.md#a6984820bce327d74368d9acf0760fef4)#define I2C1\_SCL\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

71

[ 72](rpi-pico-rp2350b-pinctrl_8h.md#a795e9c58b531f92ce519722463aa1b17)#define PWM\_7A\_P30 RP2XXX\_PINMUX(30, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 73](rpi-pico-rp2350b-pinctrl_8h.md#ad3fbd98fa55b3d443cb41641388749d1)#define PWM\_7B\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 74](rpi-pico-rp2350b-pinctrl_8h.md#a30fbd82c8c53d8fff1772e28788c086b)#define PWM\_8A\_P32 RP2XXX\_PINMUX(32, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 75](rpi-pico-rp2350b-pinctrl_8h.md#a54416419517e7ad84b150ca91df4757c)#define PWM\_8B\_P33 RP2XXX\_PINMUX(33, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 76](rpi-pico-rp2350b-pinctrl_8h.md#a893925526a33563814f0e16f214c6ebb)#define PWM\_9A\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 77](rpi-pico-rp2350b-pinctrl_8h.md#a5a7cb33fc8bdc0db3a5deb4c593f639c)#define PWM\_9B\_P35 RP2XXX\_PINMUX(35, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 78](rpi-pico-rp2350b-pinctrl_8h.md#ad03dc1b0b93a2adfea80b3857cb750b2)#define PWM\_10A\_P36 RP2XXX\_PINMUX(36, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 79](rpi-pico-rp2350b-pinctrl_8h.md#aa79c21697d49c1148a36ac7846d3b36f)#define PWM\_10B\_P37 RP2XXX\_PINMUX(37, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 80](rpi-pico-rp2350b-pinctrl_8h.md#af102e8727a33c31858ef53a00a03516e)#define PWM\_11A\_P38 RP2XXX\_PINMUX(38, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 81](rpi-pico-rp2350b-pinctrl_8h.md#aedcf89716e0e2a0573c5897ed398305e)#define PWM\_11B\_P39 RP2XXX\_PINMUX(39, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 82](rpi-pico-rp2350b-pinctrl_8h.md#a00d21e9598fce009a9545efa8310749a)#define PWM\_12A\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 83](rpi-pico-rp2350b-pinctrl_8h.md#a4fc35dfa7016512e18f3998beb1eee09)#define PWM\_12B\_P41 RP2XXX\_PINMUX(41, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 84](rpi-pico-rp2350b-pinctrl_8h.md#a50af9a6b8d4cfd20cdfc31806ce84b5c)#define PWM\_13A\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 85](rpi-pico-rp2350b-pinctrl_8h.md#a24a769fb00ce331737dddfb8e188437a)#define PWM\_13B\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 86](rpi-pico-rp2350b-pinctrl_8h.md#ab7364ffdaa0b7f483d5d3ddc0527f035)#define PWM\_14A\_P44 RP2XXX\_PINMUX(44, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 87](rpi-pico-rp2350b-pinctrl_8h.md#ae9bd548abfe6562cae4b8247e2716da8)#define PWM\_14B\_P45 RP2XXX\_PINMUX(45, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 88](rpi-pico-rp2350b-pinctrl_8h.md#a7bbb7950f79a30bf7441a5a4e2a8439f)#define PWM\_15A\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 89](rpi-pico-rp2350b-pinctrl_8h.md#a5f9ef654d81f1ec3aa013cef6e0e0194)#define PWM\_15B\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

90

[ 91](rpi-pico-rp2350b-pinctrl_8h.md#a10e91a23c0f4e10977362cc158356202)#define PIO0\_P30 RP2XXX\_PINMUX(30, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 92](rpi-pico-rp2350b-pinctrl_8h.md#a6290a461265f2f5c2534fb71a3f381e8)#define PIO0\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 93](rpi-pico-rp2350b-pinctrl_8h.md#aa5797ab6cf0a9162e4c178fb10439590)#define PIO0\_P32 RP2XXX\_PINMUX(32, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 94](rpi-pico-rp2350b-pinctrl_8h.md#a891c8586d96ce789e135025c18be58d9)#define PIO0\_P33 RP2XXX\_PINMUX(33, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 95](rpi-pico-rp2350b-pinctrl_8h.md#adf0549ef90b6e00b422b53e6c3893d1d)#define PIO0\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 96](rpi-pico-rp2350b-pinctrl_8h.md#a92e836bb52ec159cab337f8644dab3f3)#define PIO0\_P35 RP2XXX\_PINMUX(35, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 97](rpi-pico-rp2350b-pinctrl_8h.md#a1c921e73166f5c0a624b085fab8aa597)#define PIO0\_P36 RP2XXX\_PINMUX(36, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 98](rpi-pico-rp2350b-pinctrl_8h.md#ada97e9022aa031a1c7bfe4c2f21089d9)#define PIO0\_P37 RP2XXX\_PINMUX(37, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 99](rpi-pico-rp2350b-pinctrl_8h.md#a7fc0aed0fcd92a1a00889a91774856b5)#define PIO0\_P38 RP2XXX\_PINMUX(38, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 100](rpi-pico-rp2350b-pinctrl_8h.md#a1fa1f546ab91aef8d1f01dc7f5bdbe99)#define PIO0\_P39 RP2XXX\_PINMUX(39, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 101](rpi-pico-rp2350b-pinctrl_8h.md#abd97e4f662cbce09a5c79bf0b63dc842)#define PIO0\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 102](rpi-pico-rp2350b-pinctrl_8h.md#aed714db4718a4e2879602d7d6c074ed1)#define PIO0\_P41 RP2XXX\_PINMUX(41, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 103](rpi-pico-rp2350b-pinctrl_8h.md#abee573521b00e9e30ac1ba7fccd36f89)#define PIO0\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 104](rpi-pico-rp2350b-pinctrl_8h.md#ade809a3e3575c0c813b834c0b20c66af)#define PIO0\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 105](rpi-pico-rp2350b-pinctrl_8h.md#acc3fcf0bc059fbabdedf5d5ad7110ab1)#define PIO0\_P44 RP2XXX\_PINMUX(44, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 106](rpi-pico-rp2350b-pinctrl_8h.md#aa7367f5f8517a804297d33d0dd9ff48e)#define PIO0\_P45 RP2XXX\_PINMUX(45, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 107](rpi-pico-rp2350b-pinctrl_8h.md#ae6dbcf24f06f5a00694b46d65cc6b872)#define PIO0\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 108](rpi-pico-rp2350b-pinctrl_8h.md#a0ea7a40b4e6616b196ac67dcb4939b04)#define PIO0\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

109

[ 110](rpi-pico-rp2350b-pinctrl_8h.md#a0181088bbee5271a9a5b9167b8d48fe7)#define PIO1\_P30 RP2XXX\_PINMUX(30, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 111](rpi-pico-rp2350b-pinctrl_8h.md#a637fe89bb76abf86fdb7e6c7fc034a38)#define PIO1\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 112](rpi-pico-rp2350b-pinctrl_8h.md#a937a09222ba5a56a23588ea87cfd192c)#define PIO1\_P32 RP2XXX\_PINMUX(32, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 113](rpi-pico-rp2350b-pinctrl_8h.md#ad516469f9638d2b0d7a4c1d721f58b55)#define PIO1\_P33 RP2XXX\_PINMUX(33, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 114](rpi-pico-rp2350b-pinctrl_8h.md#a916fd124ec1b1530e9e8e13961e57ab2)#define PIO1\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 115](rpi-pico-rp2350b-pinctrl_8h.md#ac10191d2d8363155012a834b23c5c89c)#define PIO1\_P35 RP2XXX\_PINMUX(35, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 116](rpi-pico-rp2350b-pinctrl_8h.md#a3e839e4b9cc30dcb3c5a509affa48d37)#define PIO1\_P36 RP2XXX\_PINMUX(36, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 117](rpi-pico-rp2350b-pinctrl_8h.md#ad1bf51f09d24c5b16905805a2c3073d4)#define PIO1\_P37 RP2XXX\_PINMUX(37, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 118](rpi-pico-rp2350b-pinctrl_8h.md#a2d6addcb48e7247f8c99d8c54f8f6516)#define PIO1\_P38 RP2XXX\_PINMUX(38, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 119](rpi-pico-rp2350b-pinctrl_8h.md#a71dceefa276c7bc1bfc9739e74a218fa)#define PIO1\_P39 RP2XXX\_PINMUX(39, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 120](rpi-pico-rp2350b-pinctrl_8h.md#ae67faaf09af01be71a6832a5d7dbe47c)#define PIO1\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 121](rpi-pico-rp2350b-pinctrl_8h.md#ae15f80eec48f9a7218b911e1e5c67ada)#define PIO1\_P41 RP2XXX\_PINMUX(41, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 122](rpi-pico-rp2350b-pinctrl_8h.md#abbcc6ba6d7ba8d0fe8f55e57398aa06a)#define PIO1\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 123](rpi-pico-rp2350b-pinctrl_8h.md#a6299b7d580afb1a176e295f38805bf91)#define PIO1\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 124](rpi-pico-rp2350b-pinctrl_8h.md#ab24e3cdf7002d7e1655cad27533c380a)#define PIO1\_P44 RP2XXX\_PINMUX(44, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 125](rpi-pico-rp2350b-pinctrl_8h.md#ae86ab7585445e7443175f169afb97ae7)#define PIO1\_P45 RP2XXX\_PINMUX(45, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 126](rpi-pico-rp2350b-pinctrl_8h.md#a975b3cc54859cedd8025434a91ea18b5)#define PIO1\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 127](rpi-pico-rp2350b-pinctrl_8h.md#a2d7047730853978210863660ab0f2873)#define PIO1\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

128

[ 129](rpi-pico-rp2350b-pinctrl_8h.md#a7ef952e0586519206776e72fe9af38db)#define PIO2\_P30 RP2XXX\_PINMUX(30, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 130](rpi-pico-rp2350b-pinctrl_8h.md#adc7f51d55a60998e2b5d905283d4b7cf)#define PIO2\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 131](rpi-pico-rp2350b-pinctrl_8h.md#af0c7f198fe63d236f16fc727ec2794b0)#define PIO2\_P32 RP2XXX\_PINMUX(32, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 132](rpi-pico-rp2350b-pinctrl_8h.md#a8372bdfa26dc5f78ab74f2d988e11b13)#define PIO2\_P33 RP2XXX\_PINMUX(33, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 133](rpi-pico-rp2350b-pinctrl_8h.md#a610c1c2bfe5713766402bd0c79b58ab4)#define PIO2\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 134](rpi-pico-rp2350b-pinctrl_8h.md#a492498fa258b232c78487fe951996f79)#define PIO2\_P35 RP2XXX\_PINMUX(35, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 135](rpi-pico-rp2350b-pinctrl_8h.md#a4f611b16a5a47bff6d030ce52ad276e6)#define PIO2\_P36 RP2XXX\_PINMUX(36, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 136](rpi-pico-rp2350b-pinctrl_8h.md#a67abc0013eb5c8e916f8356f71c962cb)#define PIO2\_P37 RP2XXX\_PINMUX(37, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 137](rpi-pico-rp2350b-pinctrl_8h.md#a8db27af5b489d2c000a927918a904821)#define PIO2\_P38 RP2XXX\_PINMUX(38, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 138](rpi-pico-rp2350b-pinctrl_8h.md#a77be011f8f0135be6f958a67a071ec16)#define PIO2\_P39 RP2XXX\_PINMUX(39, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 139](rpi-pico-rp2350b-pinctrl_8h.md#a177ae3e1dd062d45d5571b447776bbc3)#define PIO2\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 140](rpi-pico-rp2350b-pinctrl_8h.md#a33c9b3a6fc44a145cb4e421908f8e811)#define PIO2\_P41 RP2XXX\_PINMUX(41, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 141](rpi-pico-rp2350b-pinctrl_8h.md#a7ca3467ee99f9819b162f361d6e2321e)#define PIO2\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 142](rpi-pico-rp2350b-pinctrl_8h.md#a178dad19422f8aeed20cc821a71205e9)#define PIO2\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 143](rpi-pico-rp2350b-pinctrl_8h.md#ab27572203828c4af7782ad3351646259)#define PIO2\_P44 RP2XXX\_PINMUX(44, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 144](rpi-pico-rp2350b-pinctrl_8h.md#a63159dfd881c1215b56d86f5cdfbed79)#define PIO2\_P45 RP2XXX\_PINMUX(45, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 145](rpi-pico-rp2350b-pinctrl_8h.md#a1c853b2986160edbeaaaa56994feefbd)#define PIO2\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

[ 146](rpi-pico-rp2350b-pinctrl_8h.md#a854da0a0288c5ddfbda5c2ee2ba49cb1)#define PIO2\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_PIO2)

147

[ 148](rpi-pico-rp2350b-pinctrl_8h.md#a5ac3e74f8eb74d8fce8394ef4dbde545)#define GPIN0\_P12 RP2XXX\_PINMUX(12, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 149](rpi-pico-rp2350b-pinctrl_8h.md#a6ad89760a21cfec86df4b9761366a155)#define GPIN1\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 150](rpi-pico-rp2350b-pinctrl_8h.md#a2efc78dac5c496b6693cc3532bab1efa)#define GPIN0\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 151](rpi-pico-rp2350b-pinctrl_8h.md#a76830708cc725412e4eb590b0bfef92b)#define GPIN1\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 152](rpi-pico-rp2350b-pinctrl_8h.md#a33b8d8a9ae7341c4addace139b5c1542)#define GPOUT0\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 153](rpi-pico-rp2350b-pinctrl_8h.md#aa7041407a501b27c7854f9a3a2237f6d)#define GPOUT1\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 154](rpi-pico-rp2350b-pinctrl_8h.md#a2eb77da9874a4805e5e2074d35ac68bc)#define GPOUT0\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 155](rpi-pico-rp2350b-pinctrl_8h.md#acc636ccdd24b165e011d8fdac01e99fd)#define GPOUT1\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 156](rpi-pico-rp2350b-pinctrl_8h.md#a460cb689dcaef60f5cdfce840eb3a177)#define GPOUT2\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 157](rpi-pico-rp2350b-pinctrl_8h.md#aff8298cc8dd9440de38800b8d06b9e2a)#define GPOUT3\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

158

[ 159](rpi-pico-rp2350b-pinctrl_8h.md#a92b46cebafc0b3c5fc01208ac52e8380)#define USB\_VBUS\_DET\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 160](rpi-pico-rp2350b-pinctrl_8h.md#acd3966bc2b968d50fcc0786c6e5ed08c)#define USB\_VBUS\_DET\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 161](rpi-pico-rp2350b-pinctrl_8h.md#a8f58dedf848dadf7a12ea9839c036a7e)#define USB\_VBUS\_DET\_P37 RP2XXX\_PINMUX(37, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 162](rpi-pico-rp2350b-pinctrl_8h.md#a969877741d1955757f0807ce21aad7e7)#define USB\_VBUS\_DET\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 163](rpi-pico-rp2350b-pinctrl_8h.md#a228077e7bfd4d66d4806619b458b5cef)#define USB\_VBUS\_DET\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 164](rpi-pico-rp2350b-pinctrl_8h.md#a22c03e36421d3355a815d8246f06edec)#define USB\_VBUS\_DET\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

165

[ 166](rpi-pico-rp2350b-pinctrl_8h.md#aaa3cfc1bdd5c946c71623e7e253e5374)#define UART0\_TX\_P30 RP2XXX\_PINMUX(30, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 167](rpi-pico-rp2350b-pinctrl_8h.md#a1972bc7d810e8a4f9d46245eb54a0fbb)#define UART0\_RX\_P31 RP2XXX\_PINMUX(31, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 168](rpi-pico-rp2350b-pinctrl_8h.md#a94daed2e879ca7fe2518c9d1fbd22bce)#define UART0\_TX\_P34 RP2XXX\_PINMUX(34, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 169](rpi-pico-rp2350b-pinctrl_8h.md#af0347ef35adaf50a30c40d00102f0143)#define UART0\_RX\_P35 RP2XXX\_PINMUX(35, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

170#define UART1\_TX\_P38 RP2XXX\_PINMUX(38, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

171#define UART1\_RX\_P39 RP2XXX\_PINMUX(39, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

172#define UART1\_TX\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

173#define UART1\_RX\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 174](rpi-pico-rp2350b-pinctrl_8h.md#a09247e65b6435ff52353c7508e146184)#define UART0\_TX\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

[ 175](rpi-pico-rp2350b-pinctrl_8h.md#ac6184365c68e71574f7d101f77313f38)#define UART0\_RX\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_UART\_ALT)

176

177/\* ADC channel allocations differ between the RP2350A and RP2350B.

178 \* Refer to Table 1116 in the datasheet.

179 \*/

[ 180](rpi-pico-rp2350b-pinctrl_8h.md#adc84b06ddf9a5d091ce99a541b8d65e6)#define ADC\_CH0\_P40 RP2XXX\_PINMUX(40, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 181](rpi-pico-rp2350b-pinctrl_8h.md#a6b056fb480b564fc5e21e136d85890f1)#define ADC\_CH1\_P41 RP2XXX\_PINMUX(41, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 182](rpi-pico-rp2350b-pinctrl_8h.md#a5109d2265a6531798efd0ef8f76243fd)#define ADC\_CH2\_P42 RP2XXX\_PINMUX(42, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 183](rpi-pico-rp2350b-pinctrl_8h.md#a81bbdb5a18c4e7820c4286e6d5736bf7)#define ADC\_CH3\_P43 RP2XXX\_PINMUX(43, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 184](rpi-pico-rp2350b-pinctrl_8h.md#a0dbb96e472f8703a42ea2c4503f7eb8f)#define ADC\_CH4\_P44 RP2XXX\_PINMUX(44, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 185](rpi-pico-rp2350b-pinctrl_8h.md#a60d7962f0eda6d6d7ae06f3aff74f4ea)#define ADC\_CH5\_P45 RP2XXX\_PINMUX(45, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 186](rpi-pico-rp2350b-pinctrl_8h.md#a2e63b628da63ffdf87c2c948f7e42805)#define ADC\_CH6\_P46 RP2XXX\_PINMUX(46, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

[ 187](rpi-pico-rp2350b-pinctrl_8h.md#a4e65979ebb13994251585936235ec45f)#define ADC\_CH7\_P47 RP2XXX\_PINMUX(47, RP2\_PINCTRL\_GPIO\_FUNC\_NULL)

188

189#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_RP2350B\_PINCTRL\_H\_ \*/

[rpi-pico-rp2350-pinctrl-common.h](rpi-pico-rp2350-pinctrl-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [rpi-pico-rp2350b-pinctrl.h](rpi-pico-rp2350b-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
