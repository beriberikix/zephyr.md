---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-pinctrl-common_8h_source.html
original_path: doxygen/html/rpi-pico-pinctrl-common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-pinctrl-common.h

[Go to the documentation of this file.](rpi-pico-pinctrl-common_8h.md)

1/\*

2 \* Copyright (c) 2021, Yonatan Schachter

3 \* Copyright (c) 2024, Andrew Featherstone

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_PINCTRL\_COMMON\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_PINCTRL\_COMMON\_H\_

10

[ 11](rpi-pico-pinctrl-common_8h.md#a3c8cd426bbad83bf5d1e5c6cafc62973)#define RP2\_ALT\_FUNC\_POS 0

[ 12](rpi-pico-pinctrl-common_8h.md#a188e415c008682910e8a8c01e6f3f32d)#define RP2\_ALT\_FUNC\_MASK 0xf

13

[ 14](rpi-pico-pinctrl-common_8h.md#a3253a176e1b4c8c5dede3961fab2f41d)#define RP2\_PIN\_NUM\_POS 5

[ 15](rpi-pico-pinctrl-common_8h.md#a074accf1a042a46ea2f0aab2e8ec87c4)#define RP2\_PIN\_NUM\_MASK 0x1f

16

[ 17](rpi-pico-pinctrl-common_8h.md#aa6dcc174ff3aa7d2125fdc82c9cd8c09)#define RP2\_GPIO\_OVERRIDE\_NORMAL 0

[ 18](rpi-pico-pinctrl-common_8h.md#aef62ecba4d73301cb30535a56937e6bf)#define RP2\_GPIO\_OVERRIDE\_INVERT 1

[ 19](rpi-pico-pinctrl-common_8h.md#af8f66955467649bd1a532966ad8c8634)#define RP2\_GPIO\_OVERRIDE\_LOW 2

[ 20](rpi-pico-pinctrl-common_8h.md#a8008dee004f50da3097cca970711e462)#define RP2\_GPIO\_OVERRIDE\_HIGH 3

21

[ 22](rpi-pico-pinctrl-common_8h.md#a5072c7fc08cc1f5eee10ad37b9b58461)#define RP2XXX\_PINMUX(pin\_num, alt\_func) \

23 (((pin\_num) << RP2\_PIN\_NUM\_POS) | ((alt\_func) << RP2\_ALT\_FUNC\_POS))

24

25/\* These function are common. SoC-specific functions are defined in their

26 \* respective header file. Refer to table 279 and 642 in the RP2040 and RP2350

27 \* datasheets for the source of these numbers.

28 \*/

[ 29](rpi-pico-pinctrl-common_8h.md#acf91c96b0248cd224d53bc749413af3a)#define RP2\_PINCTRL\_GPIO\_FUNC\_SPI 1

[ 30](rpi-pico-pinctrl-common_8h.md#a6d0e859b4ce4260b7cfcfde281e65084)#define RP2\_PINCTRL\_GPIO\_FUNC\_UART 2

[ 31](rpi-pico-pinctrl-common_8h.md#a876a2765daebaa62ee992a24152e8237)#define RP2\_PINCTRL\_GPIO\_FUNC\_I2C 3

[ 32](rpi-pico-pinctrl-common_8h.md#a3fd77c4c38a8c1f2218a3c97c1a0c42f)#define RP2\_PINCTRL\_GPIO\_FUNC\_PWM 4

[ 33](rpi-pico-pinctrl-common_8h.md#a5ef87e319ae63c53d95f6841888629a3)#define RP2\_PINCTRL\_GPIO\_FUNC\_SIO 5

[ 34](rpi-pico-pinctrl-common_8h.md#ae315aecc07dbdbc5ffecd6c0fe0f542f)#define RP2\_PINCTRL\_GPIO\_FUNC\_PIO0 6

[ 35](rpi-pico-pinctrl-common_8h.md#ab6735a82d2be87261ca88c42a06fbb13)#define RP2\_PINCTRL\_GPIO\_FUNC\_PIO1 7

36

37/\* These pin assignments for each function are similarly common. \*/

[ 38](rpi-pico-pinctrl-common_8h.md#ac3a127a92bc0ba6452081185ccc05729)#define SPI0\_RX\_P0 RP2XXX\_PINMUX(0, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 39](rpi-pico-pinctrl-common_8h.md#a5571ee8854cfc9c54144c31b12af3b8a)#define SPI0\_CSN\_P1 RP2XXX\_PINMUX(1, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 40](rpi-pico-pinctrl-common_8h.md#af08b2f762d496c9573c205e9eaf2aeff)#define SPI0\_SCK\_P2 RP2XXX\_PINMUX(2, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 41](rpi-pico-pinctrl-common_8h.md#abe7dc3e1b3703ac9a2cf9ee44fc38335)#define SPI0\_TX\_P3 RP2XXX\_PINMUX(3, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 42](rpi-pico-pinctrl-common_8h.md#af99be0796cb71d4616afdfbd144085d4)#define SPI0\_RX\_P4 RP2XXX\_PINMUX(4, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 43](rpi-pico-pinctrl-common_8h.md#ad63b1bf26bf559040f59204b4c300a54)#define SPI0\_CSN\_P5 RP2XXX\_PINMUX(5, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 44](rpi-pico-pinctrl-common_8h.md#a431bbe203918068b67e33b314c49dda4)#define SPI0\_SCK\_P6 RP2XXX\_PINMUX(6, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 45](rpi-pico-pinctrl-common_8h.md#ac0e7538c84c6f66f37a0a1d99a3e05dc)#define SPI0\_TX\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 46](rpi-pico-pinctrl-common_8h.md#a527ac5788eb8d98737b3c857af2b4cc2)#define SPI1\_RX\_P8 RP2XXX\_PINMUX(8, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 47](rpi-pico-pinctrl-common_8h.md#a06564fb42069e2978b8e35a1b42ab581)#define SPI1\_CSN\_P9 RP2XXX\_PINMUX(9, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 48](rpi-pico-pinctrl-common_8h.md#af5ab397a45f0dc2ce4d93e0d2f8289d8)#define SPI1\_SCK\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 49](rpi-pico-pinctrl-common_8h.md#a7dc8d12507da0de0da66b7975b9265a3)#define SPI1\_TX\_P11 RP2XXX\_PINMUX(11, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 50](rpi-pico-pinctrl-common_8h.md#aeb089e870c0264605cfc89452acbdc94)#define SPI1\_RX\_P12 RP2XXX\_PINMUX(12, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 51](rpi-pico-pinctrl-common_8h.md#a9993cc1b70339d579e55ebba2b85b1e2)#define SPI1\_CSN\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 52](rpi-pico-pinctrl-common_8h.md#a57b342fc61474ba494f4a6450b633cdc)#define SPI1\_SCK\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 53](rpi-pico-pinctrl-common_8h.md#a00fa0f76c126531f5a8d09bb364932fe)#define SPI1\_TX\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 54](rpi-pico-pinctrl-common_8h.md#ae95322fdb81bf56f96d8ce8735176d56)#define SPI0\_RX\_P16 RP2XXX\_PINMUX(16, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 55](rpi-pico-pinctrl-common_8h.md#a36ba7445db4689cc7dd9f33cd008a241)#define SPI0\_CSN\_P17 RP2XXX\_PINMUX(17, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 56](rpi-pico-pinctrl-common_8h.md#aa25413e28da76c4e489de76737ce74ab)#define SPI0\_SCK\_P18 RP2XXX\_PINMUX(18, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 57](rpi-pico-pinctrl-common_8h.md#a3af179bd186dbe7bd76eddae5bca0759)#define SPI0\_TX\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 58](rpi-pico-pinctrl-common_8h.md#afaff3a4d60ac9b8182e0fb8ae5a24daf)#define SPI0\_RX\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 59](rpi-pico-pinctrl-common_8h.md#aab0f18ff3cc0d3af11811df927302f73)#define SPI0\_CSN\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 60](rpi-pico-pinctrl-common_8h.md#aad3355d9839ce0526791f6d8cb94b718)#define SPI0\_SCK\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 61](rpi-pico-pinctrl-common_8h.md#a0004517f8d3beca74ff8639a5446eda1)#define SPI0\_TX\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 62](rpi-pico-pinctrl-common_8h.md#ac4652211d636a7a6dd01e46ee6ee4348)#define SPI1\_RX\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 63](rpi-pico-pinctrl-common_8h.md#aa6a45fd051b50c2ca14041af2d6343b9)#define SPI1\_CSN\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 64](rpi-pico-pinctrl-common_8h.md#ae4ac43022cbfd4bf120709ada474878e)#define SPI1\_SCK\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 65](rpi-pico-pinctrl-common_8h.md#a1734f53da97e89eb94733e945806348d)#define SPI1\_TX\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 66](rpi-pico-pinctrl-common_8h.md#a188e9b8daf03864243c3c27157aca62d)#define SPI1\_RX\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

[ 67](rpi-pico-pinctrl-common_8h.md#acfe05ee846ac3453e1f6a3c749754498)#define SPI1\_CSN\_P29 RP2XXX\_PINMUX(29, RP2\_PINCTRL\_GPIO\_FUNC\_SPI)

68

[ 69](rpi-pico-pinctrl-common_8h.md#ab701f6451547135182ee858beafd467d)#define UART0\_TX\_P0 RP2XXX\_PINMUX(0, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 70](rpi-pico-pinctrl-common_8h.md#ab825857a3fd666047730e79e57a0337d)#define UART0\_RX\_P1 RP2XXX\_PINMUX(1, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 71](rpi-pico-pinctrl-common_8h.md#ae932f661454e4c242e827f78f15032a8)#define UART0\_CTS\_P2 RP2XXX\_PINMUX(2, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 72](rpi-pico-pinctrl-common_8h.md#abf693c03d4728087b3b7c1eb458ac089)#define UART0\_RTS\_P3 RP2XXX\_PINMUX(3, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 73](rpi-pico-pinctrl-common_8h.md#a5d8960b2daae52156888831ec8528c0a)#define UART1\_TX\_P4 RP2XXX\_PINMUX(4, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 74](rpi-pico-pinctrl-common_8h.md#ac1f921b5f0d9f81e93750d14edb375fe)#define UART1\_RX\_P5 RP2XXX\_PINMUX(5, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 75](rpi-pico-pinctrl-common_8h.md#a1fb554340e462892f301578c8d8e0f5d)#define UART1\_CTS\_P6 RP2XXX\_PINMUX(6, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 76](rpi-pico-pinctrl-common_8h.md#aae039fd4ddda17ef217c79e2cc87f52b)#define UART1\_RTS\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 77](rpi-pico-pinctrl-common_8h.md#ad1fbe6b83e13c1709602c7a4cb0546c5)#define UART1\_TX\_P8 RP2XXX\_PINMUX(8, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 78](rpi-pico-pinctrl-common_8h.md#a38dec6f54d9c71c5221cb5391be3a466)#define UART1\_RX\_P9 RP2XXX\_PINMUX(9, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 79](rpi-pico-pinctrl-common_8h.md#a9fc5db32678491fff19073f045a6068e)#define UART1\_CTS\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 80](rpi-pico-pinctrl-common_8h.md#a569515404fa662fce8e4359413e91696)#define UART1\_RTS\_P11 RP2XXX\_PINMUX(11, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 81](rpi-pico-pinctrl-common_8h.md#a455413fb24b21d1ff801d157a18857d0)#define UART0\_TX\_P12 RP2XXX\_PINMUX(12, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 82](rpi-pico-pinctrl-common_8h.md#abbe96b45bbd26e433f844569169085e7)#define UART0\_RX\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 83](rpi-pico-pinctrl-common_8h.md#a8af1f170b166fc866751637e6085b3a8)#define UART0\_CTS\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 84](rpi-pico-pinctrl-common_8h.md#a139ebf60b648af731d01c2a0d8dbee40)#define UART0\_RTS\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 85](rpi-pico-pinctrl-common_8h.md#a3b94598ef851604ac2ee3a995111ef56)#define UART0\_TX\_P16 RP2XXX\_PINMUX(16, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 86](rpi-pico-pinctrl-common_8h.md#a4d955d0fc3676ce27f764e2dc499bc77)#define UART0\_RX\_P17 RP2XXX\_PINMUX(17, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 87](rpi-pico-pinctrl-common_8h.md#a0766bad799526a6c7dd9a96eea3d640d)#define UART0\_CTS\_P18 RP2XXX\_PINMUX(18, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 88](rpi-pico-pinctrl-common_8h.md#a4501e7448b5dd7c1fe8b336a649bdc15)#define UART0\_RTS\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 89](rpi-pico-pinctrl-common_8h.md#a2ea1efe0310be35751c13de759fef772)#define UART1\_TX\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 90](rpi-pico-pinctrl-common_8h.md#abc118d4b0d4ec2c08a0fbc311ccc1318)#define UART1\_RX\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 91](rpi-pico-pinctrl-common_8h.md#a8f260a9db999002d78a95ae6aa7f9fca)#define UART1\_CTS\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 92](rpi-pico-pinctrl-common_8h.md#a4e50d3fce733cf6d76266db8a661c84f)#define UART1\_RTS\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 93](rpi-pico-pinctrl-common_8h.md#a9ab601625d83b4121469f81b50e327c3)#define UART1\_TX\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 94](rpi-pico-pinctrl-common_8h.md#ad9f79a08d6c94c61d6eecd014ac13294)#define UART1\_RX\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 95](rpi-pico-pinctrl-common_8h.md#a9d324adb2a17f1ea396a65b1027e899a)#define UART1\_CTS\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 96](rpi-pico-pinctrl-common_8h.md#a6870b209c2cd9b167b9b77d403f44fee)#define UART1\_RTS\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 97](rpi-pico-pinctrl-common_8h.md#a4e1816b13c5177cfbc855fff75860a4b)#define UART0\_TX\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

[ 98](rpi-pico-pinctrl-common_8h.md#afa215925108121954274d283ec75ba17)#define UART0\_RX\_P29 RP2XXX\_PINMUX(29, RP2\_PINCTRL\_GPIO\_FUNC\_UART)

99

[ 100](rpi-pico-pinctrl-common_8h.md#ae30e1260f72c5c6df77239af2099e303)#define I2C0\_SDA\_P0 RP2XXX\_PINMUX(0, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 101](rpi-pico-pinctrl-common_8h.md#a40af19eb953dce3b7dd7cccfd67242e6)#define I2C0\_SCL\_P1 RP2XXX\_PINMUX(1, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 102](rpi-pico-pinctrl-common_8h.md#aa35d0b355545f4bd5b82cea95fa829e3)#define I2C1\_SDA\_P2 RP2XXX\_PINMUX(2, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 103](rpi-pico-pinctrl-common_8h.md#ab3e4482a3aff639a1bba6dc45b366472)#define I2C1\_SCL\_P3 RP2XXX\_PINMUX(3, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 104](rpi-pico-pinctrl-common_8h.md#a17e868b2e215c856df0045f59b36f5dd)#define I2C0\_SDA\_P4 RP2XXX\_PINMUX(4, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 105](rpi-pico-pinctrl-common_8h.md#a63763d80d870458a30f465f9f349fc82)#define I2C0\_SCL\_P5 RP2XXX\_PINMUX(5, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 106](rpi-pico-pinctrl-common_8h.md#ab1b0376aa1eea3662dbcd4723c6c7754)#define I2C1\_SDA\_P6 RP2XXX\_PINMUX(6, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 107](rpi-pico-pinctrl-common_8h.md#a52bef8473a19a371b2b34cee3795dcc9)#define I2C1\_SCL\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 108](rpi-pico-pinctrl-common_8h.md#a1ae9321035cbb03e22aea88e575a8233)#define I2C0\_SDA\_P8 RP2XXX\_PINMUX(8, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 109](rpi-pico-pinctrl-common_8h.md#a3cded8d72cf258730fed84b49d8af23a)#define I2C0\_SCL\_P9 RP2XXX\_PINMUX(9, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 110](rpi-pico-pinctrl-common_8h.md#a93b728018be9548cea889bd9b1e46559)#define I2C1\_SDA\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 111](rpi-pico-pinctrl-common_8h.md#a3735b8b7807bc75d4ed69479cf4f2fea)#define I2C1\_SCL\_P11 RP2XXX\_PINMUX(11, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 112](rpi-pico-pinctrl-common_8h.md#a8bd073ab6670f5d24ed8eb732fc37498)#define I2C0\_SDA\_P12 RP2XXX\_PINMUX(12, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 113](rpi-pico-pinctrl-common_8h.md#a77866140a8312d66f413b62aa227f12d)#define I2C0\_SCL\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 114](rpi-pico-pinctrl-common_8h.md#a60d90a91688fc831361a09d9aeafa5bb)#define I2C1\_SDA\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 115](rpi-pico-pinctrl-common_8h.md#a4147939bdfa76fe02bbfc6e1af0ef544)#define I2C1\_SCL\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 116](rpi-pico-pinctrl-common_8h.md#a7ceaae716d415c0f61f73fbe56d0381f)#define I2C0\_SDA\_P16 RP2XXX\_PINMUX(16, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 117](rpi-pico-pinctrl-common_8h.md#a430a31bec6c57c12d338ce8cb8093700)#define I2C0\_SCL\_P17 RP2XXX\_PINMUX(17, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 118](rpi-pico-pinctrl-common_8h.md#a0067066f1e893e6908ecd4b15922094e)#define I2C1\_SDA\_P18 RP2XXX\_PINMUX(18, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 119](rpi-pico-pinctrl-common_8h.md#a568f559b264d01be71fbdbf3b974cbbb)#define I2C1\_SCL\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 120](rpi-pico-pinctrl-common_8h.md#a60a504fa6dfd8d5927c99ab8a19499e2)#define I2C0\_SDA\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 121](rpi-pico-pinctrl-common_8h.md#a62f28e0089a5570bf549219b152a0899)#define I2C0\_SCL\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 122](rpi-pico-pinctrl-common_8h.md#a3867f51bbf3e77cc5d43faa82ed6a031)#define I2C1\_SDA\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 123](rpi-pico-pinctrl-common_8h.md#acd2745f512813f7b385e1a255dc964fc)#define I2C1\_SCL\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 124](rpi-pico-pinctrl-common_8h.md#ab972fa47c807e57f9c40fceffb48bd73)#define I2C0\_SDA\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 125](rpi-pico-pinctrl-common_8h.md#ad259c34d3cda5272600c91ac29b58157)#define I2C0\_SCL\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 126](rpi-pico-pinctrl-common_8h.md#ac965583ec9aba86ec1d071e6f0741453)#define I2C1\_SDA\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 127](rpi-pico-pinctrl-common_8h.md#a52ad7e8658b01cb848f7a2f705e5fb56)#define I2C1\_SCL\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 128](rpi-pico-pinctrl-common_8h.md#af674e6195534e61b07286d33bc841004)#define I2C0\_SDA\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

[ 129](rpi-pico-pinctrl-common_8h.md#a29520fb3c34ec9c2f16827d80f5cfd22)#define I2C0\_SCL\_P29 RP2XXX\_PINMUX(29, RP2\_PINCTRL\_GPIO\_FUNC\_I2C)

130

[ 131](rpi-pico-pinctrl-common_8h.md#a8c0c1058a626d83ba5f7e18238aba150)#define PWM\_0A\_P0 RP2XXX\_PINMUX(0, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 132](rpi-pico-pinctrl-common_8h.md#a9ee0e7d4a2025d15777aca85bf196dbd)#define PWM\_0B\_P1 RP2XXX\_PINMUX(1, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 133](rpi-pico-pinctrl-common_8h.md#a2b722fe90807f95da5fd392588693cad)#define PWM\_1A\_P2 RP2XXX\_PINMUX(2, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 134](rpi-pico-pinctrl-common_8h.md#a9a3ac0fc2cac8bf8191be8a770068844)#define PWM\_1B\_P3 RP2XXX\_PINMUX(3, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 135](rpi-pico-pinctrl-common_8h.md#a9d8f2d1977f916d6fe822e6694bd1ab4)#define PWM\_2A\_P4 RP2XXX\_PINMUX(4, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 136](rpi-pico-pinctrl-common_8h.md#ad627091da0e7de4ae6b1b22b19c0cfe2)#define PWM\_2B\_P5 RP2XXX\_PINMUX(5, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 137](rpi-pico-pinctrl-common_8h.md#a6ea8b1671b9c196eedf45237337c1fe3)#define PWM\_3A\_P6 RP2XXX\_PINMUX(6, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 138](rpi-pico-pinctrl-common_8h.md#a59717f0a0b04713962994770a0f1ba46)#define PWM\_3B\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 139](rpi-pico-pinctrl-common_8h.md#af8806e562120b238c411b689493e7bc5)#define PWM\_4A\_P8 RP2XXX\_PINMUX(8, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 140](rpi-pico-pinctrl-common_8h.md#a571a0f7bfd41a53f184c31dde0530566)#define PWM\_4B\_P9 RP2XXX\_PINMUX(9, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 141](rpi-pico-pinctrl-common_8h.md#a5c7937ba0d514de8b6a08b4ecde4232f)#define PWM\_5A\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 142](rpi-pico-pinctrl-common_8h.md#ac1b6831c308bc76a6bd3afc9b83a292d)#define PWM\_5B\_P11 RP2XXX\_PINMUX(11, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 143](rpi-pico-pinctrl-common_8h.md#a6658f66fae2f5019a2f85d8cddff3d36)#define PWM\_6A\_P12 RP2XXX\_PINMUX(12, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 144](rpi-pico-pinctrl-common_8h.md#af510dfa645567dcb808eae9627cac8f7)#define PWM\_6B\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 145](rpi-pico-pinctrl-common_8h.md#abac1afd85ce599d294023209ba93e02e)#define PWM\_7A\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 146](rpi-pico-pinctrl-common_8h.md#a820d4fe0a968ad8530aff02df8652b45)#define PWM\_7B\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 147](rpi-pico-pinctrl-common_8h.md#a0e22f3c03be7a1ce254995f63e7ef987)#define PWM\_0A\_P16 RP2XXX\_PINMUX(16, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 148](rpi-pico-pinctrl-common_8h.md#aa7fcd5836c81762cb39963bbed3be5d9)#define PWM\_0B\_P17 RP2XXX\_PINMUX(17, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 149](rpi-pico-pinctrl-common_8h.md#aece83f07ba754d93b9ba855fcb748f80)#define PWM\_1A\_P18 RP2XXX\_PINMUX(18, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 150](rpi-pico-pinctrl-common_8h.md#a900a6c03fd80a1f735abb22ae8f0ec74)#define PWM\_1B\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 151](rpi-pico-pinctrl-common_8h.md#a55575285c17b736f2eca2b1a14f068d6)#define PWM\_2A\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 152](rpi-pico-pinctrl-common_8h.md#a65af9b7adca0cae2573b9fbf203b9719)#define PWM\_2B\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 153](rpi-pico-pinctrl-common_8h.md#aa18cf7518f3e8362f7403f66379722a0)#define PWM\_3A\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 154](rpi-pico-pinctrl-common_8h.md#a9bbaa5ee3c43ec70d10a0382d16200bc)#define PWM\_3B\_P22 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 155](rpi-pico-pinctrl-common_8h.md#ae6027bc734827d450b1ece9dfa927fef)#define PWM\_4A\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 156](rpi-pico-pinctrl-common_8h.md#abd53f235d29e3acaa6ab00bf92cb9700)#define PWM\_4B\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 157](rpi-pico-pinctrl-common_8h.md#a7c6c38dc56f295c72e32f3f24e5ede54)#define PWM\_5A\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 158](rpi-pico-pinctrl-common_8h.md#a74fad3f54a025e961d8f5cea2d560956)#define PWM\_5B\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 159](rpi-pico-pinctrl-common_8h.md#a75cb4a1fad02757aeea95e48b603573c)#define PWM\_6A\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

[ 160](rpi-pico-pinctrl-common_8h.md#a1ae95d7fc4825ad2d9a2574431f26575)#define PWM\_6B\_P29 RP2XXX\_PINMUX(29, RP2\_PINCTRL\_GPIO\_FUNC\_PWM)

161

[ 162](rpi-pico-pinctrl-common_8h.md#a9df9d81448954424e93843fd4342e84b)#define PIO0\_P0 RP2XXX\_PINMUX(0, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 163](rpi-pico-pinctrl-common_8h.md#a522d72a5b560f26317e100dc5aeff8cf)#define PIO0\_P1 RP2XXX\_PINMUX(1, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 164](rpi-pico-pinctrl-common_8h.md#a1a58d0bf99e8ab3b6fd2e3677bf6c7be)#define PIO0\_P2 RP2XXX\_PINMUX(2, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 165](rpi-pico-pinctrl-common_8h.md#a2ed112a2ef5fdb21ee3d3ff3f6d3d1c3)#define PIO0\_P3 RP2XXX\_PINMUX(3, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 166](rpi-pico-pinctrl-common_8h.md#a3b0e561ed8413e19f845f5c97d6dcd17)#define PIO0\_P4 RP2XXX\_PINMUX(4, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 167](rpi-pico-pinctrl-common_8h.md#a850f83cb267acfc49e63a169df7cc2d9)#define PIO0\_P5 RP2XXX\_PINMUX(5, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 168](rpi-pico-pinctrl-common_8h.md#ae088b77f2976b4355f8c561fd4317ff3)#define PIO0\_P6 RP2XXX\_PINMUX(6, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 169](rpi-pico-pinctrl-common_8h.md#a4ac80c9993d4f779648f0727e12c7acc)#define PIO0\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 170](rpi-pico-pinctrl-common_8h.md#a246c4a2e1a563b3aab8831bd4b4f58c9)#define PIO0\_P8 RP2XXX\_PINMUX(8, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 171](rpi-pico-pinctrl-common_8h.md#a1cf21096794956f9e6c0ed88731a3485)#define PIO0\_P9 RP2XXX\_PINMUX(9, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 172](rpi-pico-pinctrl-common_8h.md#ac4a6382e348136df655907da85b6c41b)#define PIO0\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 173](rpi-pico-pinctrl-common_8h.md#ab3f97552872ddc47e82161b90bf08131)#define PIO0\_P11 RP2XXX\_PINMUX(11, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 174](rpi-pico-pinctrl-common_8h.md#a45f90c03d4facf96ebdc8b0e233d9b00)#define PIO0\_P12 RP2XXX\_PINMUX(12, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 175](rpi-pico-pinctrl-common_8h.md#a00cbec3bb8d0ebb26b37c15e3e97e8e5)#define PIO0\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 176](rpi-pico-pinctrl-common_8h.md#a8482533738ec3b43848d7b399e8c22c3)#define PIO0\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 177](rpi-pico-pinctrl-common_8h.md#ad49d0e0e8ab99f1e4eefd7fc810f8b5e)#define PIO0\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 178](rpi-pico-pinctrl-common_8h.md#aefec8745f6cfb90046a3a62b41747172)#define PIO0\_P16 RP2XXX\_PINMUX(16, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 179](rpi-pico-pinctrl-common_8h.md#aee1732f27deaac4548aea7081ac215a0)#define PIO0\_P17 RP2XXX\_PINMUX(17, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 180](rpi-pico-pinctrl-common_8h.md#a1c8cf35638095e65b52a1aa99739c3d7)#define PIO0\_P18 RP2XXX\_PINMUX(18, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 181](rpi-pico-pinctrl-common_8h.md#a971e9bfe8986da8815828cafc0d452c0)#define PIO0\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 182](rpi-pico-pinctrl-common_8h.md#a18397bac799cf1c1f695990a85991285)#define PIO0\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 183](rpi-pico-pinctrl-common_8h.md#a215924b717018cdd26b0f85a6cc05885)#define PIO0\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 184](rpi-pico-pinctrl-common_8h.md#a9888a148ae74c09be083ec7e0ff119ea)#define PIO0\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 185](rpi-pico-pinctrl-common_8h.md#a029e7082733f92bd0493ae3faf2f425f)#define PIO0\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 186](rpi-pico-pinctrl-common_8h.md#af74b320b9466df4da0db01f21b9c9ef5)#define PIO0\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 187](rpi-pico-pinctrl-common_8h.md#a0aedb60bb7791248279d7ade4a34887a)#define PIO0\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 188](rpi-pico-pinctrl-common_8h.md#a1b63ef1fcc7c78b7a1f740ab649be12b)#define PIO0\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 189](rpi-pico-pinctrl-common_8h.md#ad0eba358f972950ba1b28f72f68b6ab3)#define PIO0\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 190](rpi-pico-pinctrl-common_8h.md#a097d8adac6a3c0523039b0b5507b5ed9)#define PIO0\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

[ 191](rpi-pico-pinctrl-common_8h.md#aa698f82b9b0e3bad97751a4a353ac859)#define PIO0\_P29 RP2XXX\_PINMUX(29, RP2\_PINCTRL\_GPIO\_FUNC\_PIO0)

192

[ 193](rpi-pico-pinctrl-common_8h.md#a55f4c7b92049b63934696a863e9ee4f1)#define PIO1\_P0 RP2XXX\_PINMUX(0, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 194](rpi-pico-pinctrl-common_8h.md#af07d1a63828e66f60953a9eef8a72b47)#define PIO1\_P1 RP2XXX\_PINMUX(1, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 195](rpi-pico-pinctrl-common_8h.md#a8dfa9800204f2d85e6ea053300187c0a)#define PIO1\_P2 RP2XXX\_PINMUX(2, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 196](rpi-pico-pinctrl-common_8h.md#a63b05db7532755f7aecdc982c6827d0f)#define PIO1\_P3 RP2XXX\_PINMUX(3, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 197](rpi-pico-pinctrl-common_8h.md#aa2e7f57939a019d768198990d2d095e5)#define PIO1\_P4 RP2XXX\_PINMUX(4, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 198](rpi-pico-pinctrl-common_8h.md#a517804b636fc3c7039c81b8bc37c868c)#define PIO1\_P5 RP2XXX\_PINMUX(5, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 199](rpi-pico-pinctrl-common_8h.md#ab9d33e4986d0afc32dee5c4b53748277)#define PIO1\_P6 RP2XXX\_PINMUX(6, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 200](rpi-pico-pinctrl-common_8h.md#a6a9eb8a6ef794b493f272d8e0a5dddf1)#define PIO1\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 201](rpi-pico-pinctrl-common_8h.md#aa84c1f4df860497918801f680a305234)#define PIO1\_P8 RP2XXX\_PINMUX(8, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 202](rpi-pico-pinctrl-common_8h.md#af3baee0a780c209dd959dcf806c6f2eb)#define PIO1\_P9 RP2XXX\_PINMUX(9, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 203](rpi-pico-pinctrl-common_8h.md#a119202f1f8886a0973eb6c7ea82c3b1c)#define PIO1\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 204](rpi-pico-pinctrl-common_8h.md#a3bf905b154c2f6bc6db57700f3069723)#define PIO1\_P11 RP2XXX\_PINMUX(11, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 205](rpi-pico-pinctrl-common_8h.md#aeb247672aa4ad06086cb0d6354d49c33)#define PIO1\_P12 RP2XXX\_PINMUX(12, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 206](rpi-pico-pinctrl-common_8h.md#acc6c5b402bacbabd102918bb0b206aad)#define PIO1\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 207](rpi-pico-pinctrl-common_8h.md#a302de2746e15868732148b08e0c1ab13)#define PIO1\_P14 RP2XXX\_PINMUX(14, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 208](rpi-pico-pinctrl-common_8h.md#a7d3f6f2babb16a57add6b4e3db36aef9)#define PIO1\_P15 RP2XXX\_PINMUX(15, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 209](rpi-pico-pinctrl-common_8h.md#adcc851425daace38c162390fe720afcc)#define PIO1\_P16 RP2XXX\_PINMUX(16, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 210](rpi-pico-pinctrl-common_8h.md#a151bbdb99bc454267f897ee7bd51e426)#define PIO1\_P17 RP2XXX\_PINMUX(17, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 211](rpi-pico-pinctrl-common_8h.md#a592dfc83285add152f4b8a3fc820ae11)#define PIO1\_P18 RP2XXX\_PINMUX(18, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 212](rpi-pico-pinctrl-common_8h.md#a4909477679ff66416513d452a472d9f5)#define PIO1\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 213](rpi-pico-pinctrl-common_8h.md#a54776977a2d7b9ab758582b0a38b8470)#define PIO1\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 214](rpi-pico-pinctrl-common_8h.md#a2bbee503294dd5fecf950e5cc1a6477b)#define PIO1\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 215](rpi-pico-pinctrl-common_8h.md#a8e2399ccd2309375cdcef8ffb41f40ac)#define PIO1\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 216](rpi-pico-pinctrl-common_8h.md#a3c3ce18d8001ff4a717fce9684fce95b)#define PIO1\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 217](rpi-pico-pinctrl-common_8h.md#a4778dd42ae57a25639329f576de4ed66)#define PIO1\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 218](rpi-pico-pinctrl-common_8h.md#a7c79ac48e47448326a391f06958e881c)#define PIO1\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 219](rpi-pico-pinctrl-common_8h.md#ac5d4a6126134665a0f51a75471978ec4)#define PIO1\_P26 RP2XXX\_PINMUX(26, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 220](rpi-pico-pinctrl-common_8h.md#a07350228748bd2adeb0b9b21585c28fd)#define PIO1\_P27 RP2XXX\_PINMUX(27, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 221](rpi-pico-pinctrl-common_8h.md#acf87fe7a26dd433fc4e0beb517d1c63d)#define PIO1\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

[ 222](rpi-pico-pinctrl-common_8h.md#ab911933d8c89279dfb26a2e3b7df3a01)#define PIO1\_P29 RP2XXX\_PINMUX(29, RP2\_PINCTRL\_GPIO\_FUNC\_PIO1)

223

[ 224](rpi-pico-pinctrl-common_8h.md#a2efc78dac5c496b6693cc3532bab1efa)#define GPIN0\_P20 RP2XXX\_PINMUX(20, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 225](rpi-pico-pinctrl-common_8h.md#a76830708cc725412e4eb590b0bfef92b)#define GPIN1\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 226](rpi-pico-pinctrl-common_8h.md#a2eb77da9874a4805e5e2074d35ac68bc)#define GPOUT0\_P21 RP2XXX\_PINMUX(21, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 227](rpi-pico-pinctrl-common_8h.md#acc636ccdd24b165e011d8fdac01e99fd)#define GPOUT1\_P23 RP2XXX\_PINMUX(23, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 228](rpi-pico-pinctrl-common_8h.md#a460cb689dcaef60f5cdfce840eb3a177)#define GPOUT2\_P24 RP2XXX\_PINMUX(24, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

[ 229](rpi-pico-pinctrl-common_8h.md#aff8298cc8dd9440de38800b8d06b9e2a)#define GPOUT3\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_GPCK)

230

[ 231](rpi-pico-pinctrl-common_8h.md#a7fdd710bbfbb284379372197c70c10ea)#define USB\_VBUS\_DET\_P1 RP2XXX\_PINMUX(1, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 232](rpi-pico-pinctrl-common_8h.md#a5ac68f804e0f2e2cd038df0f69caa1ed)#define USB\_VBUS\_DET\_P4 RP2XXX\_PINMUX(4, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 233](rpi-pico-pinctrl-common_8h.md#a7cde6cc86d718356349dc5270c3155c1)#define USB\_VBUS\_DET\_P7 RP2XXX\_PINMUX(7, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 234](rpi-pico-pinctrl-common_8h.md#a0761b4ab2aade15a2d18e1f27093b3b6)#define USB\_VBUS\_DET\_P10 RP2XXX\_PINMUX(10, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 235](rpi-pico-pinctrl-common_8h.md#a05b293f83aad166324c768d6efc7a944)#define USB\_VBUS\_DET\_P13 RP2XXX\_PINMUX(13, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 236](rpi-pico-pinctrl-common_8h.md#afb9b3b683e4c08c4442a652eacda1116)#define USB\_VBUS\_DET\_P16 RP2XXX\_PINMUX(16, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 237](rpi-pico-pinctrl-common_8h.md#a809b3e2bdede6e1487bbdcea88bf3556)#define USB\_VBUS\_DET\_P19 RP2XXX\_PINMUX(19, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 238](rpi-pico-pinctrl-common_8h.md#ae91b87294af3fbeffe7b2c198fdd267e)#define USB\_VBUS\_DET\_P22 RP2XXX\_PINMUX(22, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 239](rpi-pico-pinctrl-common_8h.md#a870e6aad81c9a7060d01cf96f7c5a5fb)#define USB\_VBUS\_DET\_P25 RP2XXX\_PINMUX(25, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

[ 240](rpi-pico-pinctrl-common_8h.md#ac6d9e8391de996cbfbb2b7cd7754af6c)#define USB\_VBUS\_DET\_P28 RP2XXX\_PINMUX(28, RP2\_PINCTRL\_GPIO\_FUNC\_USB)

241

242#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RPI\_PICO\_PINCTRL\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [rpi-pico-pinctrl-common.h](rpi-pico-pinctrl-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
