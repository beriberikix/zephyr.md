---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl-r8a77961_8h_source.html
original_path: doxygen/html/pinctrl-r8a77961_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-r8a77961.h

[Go to the documentation of this file.](pinctrl-r8a77961_8h.md)

1/\*

2 \* Copyright (c) 2023 EPAM Systems

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A77961\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A77961\_H\_

8

9#include "[pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)"

10

11/\* Pins declaration \*/

[ 12](pinctrl-r8a77961_8h.md#a61ae8c246db04e2ac956ccf175b217c6)#define PIN\_NONE -1

13

[ 14](pinctrl-r8a77961_8h.md#a9d19d7f5e5999cff224df0f2dbcf5e5a)#define PIN\_SD0\_CLK RCAR\_GP\_PIN(3, 0)

[ 15](pinctrl-r8a77961_8h.md#a83a34e8961aabdc22d2a9bae3b03ad08)#define PIN\_SD0\_CMD RCAR\_GP\_PIN(3, 1)

[ 16](pinctrl-r8a77961_8h.md#a5ae360d9210474bcff84f656f3948f72)#define PIN\_SD0\_DATA0 RCAR\_GP\_PIN(3, 2)

[ 17](pinctrl-r8a77961_8h.md#a1881ab8e61d6f878f29b608deb0505d4)#define PIN\_SD0\_DATA1 RCAR\_GP\_PIN(3, 3)

[ 18](pinctrl-r8a77961_8h.md#a310d4722e362453561d7acacf782306b)#define PIN\_SD0\_DATA2 RCAR\_GP\_PIN(3, 4)

[ 19](pinctrl-r8a77961_8h.md#ab4f9a2603e6a13616f9711415959fde0)#define PIN\_SD0\_DATA3 RCAR\_GP\_PIN(3, 5)

[ 20](pinctrl-r8a77961_8h.md#a803f5ff3e1f046d9020403c74188ee68)#define PIN\_SD0\_CD RCAR\_GP\_PIN(3, 12)

[ 21](pinctrl-r8a77961_8h.md#a6716be03dcd77fbb58e2633a6cfdcf8d)#define PIN\_SD0\_WP RCAR\_GP\_PIN(3, 13)

22

[ 23](pinctrl-r8a77961_8h.md#a02cb9d6acabda91eaaef7b0a691b2b99)#define PIN\_SD1\_CLK RCAR\_GP\_PIN(3, 6)

[ 24](pinctrl-r8a77961_8h.md#ac468f899d052bc342a25d80358c1a4d4)#define PIN\_SD1\_CMD RCAR\_GP\_PIN(3, 7)

25/\*

26 \* note: the next data pins shared with SD2,

27 \* and for SD2 they represent DATA4-DATA7

28 \*/

[ 29](pinctrl-r8a77961_8h.md#a28e1004c169a40387ad45215f9ea4d8f)#define PIN\_SD1\_DATA0 RCAR\_GP\_PIN(3, 8)

[ 30](pinctrl-r8a77961_8h.md#a8ef57ae45bd6b9460184d101f20c6ef0)#define PIN\_SD1\_DATA1 RCAR\_GP\_PIN(3, 9)

[ 31](pinctrl-r8a77961_8h.md#a1397bd3c2b618f6f5fcebb18a19a4072)#define PIN\_SD1\_DATA2 RCAR\_GP\_PIN(3, 10)

[ 32](pinctrl-r8a77961_8h.md#a886bf58616d323a7267a5c04339d7fba)#define PIN\_SD1\_DATA3 RCAR\_GP\_PIN(3, 11)

33

[ 34](pinctrl-r8a77961_8h.md#af0894972a37b87c0ac1fc6d4fb5a5e32)#define PIN\_SD1\_CD RCAR\_GP\_PIN(3, 14)

[ 35](pinctrl-r8a77961_8h.md#ae51dc75ff2098b33993bf32b3f9cc88c)#define PIN\_SD1\_WP RCAR\_GP\_PIN(3, 15)

36

[ 37](pinctrl-r8a77961_8h.md#a89f29aaee07e33195930c442446c0d45)#define PIN\_SD2\_CLK RCAR\_GP\_PIN(4, 0)

[ 38](pinctrl-r8a77961_8h.md#ac51dd59c00afeda80a8d2926317d309d)#define PIN\_SD2\_CMD RCAR\_GP\_PIN(4, 1)

[ 39](pinctrl-r8a77961_8h.md#a281deecd34ce02ae68e5ff6a2d471104)#define PIN\_SD2\_DATA0 RCAR\_GP\_PIN(4, 2)

[ 40](pinctrl-r8a77961_8h.md#a8982cea5c3de77b7f5b107e19bc668a8)#define PIN\_SD2\_DATA1 RCAR\_GP\_PIN(4, 3)

[ 41](pinctrl-r8a77961_8h.md#aa2236dad12d9be7a0441437d09cd4d13)#define PIN\_SD2\_DATA2 RCAR\_GP\_PIN(4, 4)

[ 42](pinctrl-r8a77961_8h.md#afc4f1a8655fceee48e5ddd5e54461942)#define PIN\_SD2\_DATA3 RCAR\_GP\_PIN(4, 5)

[ 43](pinctrl-r8a77961_8h.md#a5eecf0f15b5eefe1f462efa5bbaeba72)#define PIN\_SD2\_DS RCAR\_GP\_PIN(4, 6)

44

[ 45](pinctrl-r8a77961_8h.md#abe218411e9a47a116ab13205cd564211)#define PIN\_SD3\_CLK RCAR\_GP\_PIN(4, 7)

[ 46](pinctrl-r8a77961_8h.md#a1cae9fc15220519e3f69f2c1b613e2c2)#define PIN\_SD3\_CMD RCAR\_GP\_PIN(4, 8)

[ 47](pinctrl-r8a77961_8h.md#a413c125c77fb61a578fc2ad15f6e7c58)#define PIN\_SD3\_DATA0 RCAR\_GP\_PIN(4, 9)

[ 48](pinctrl-r8a77961_8h.md#aff3052402811c024f401fd20d1711c15)#define PIN\_SD3\_DATA1 RCAR\_GP\_PIN(4, 10)

[ 49](pinctrl-r8a77961_8h.md#a8c2f5f99f99d9712068b9f030d4bcfbb)#define PIN\_SD3\_DATA2 RCAR\_GP\_PIN(4, 11)

[ 50](pinctrl-r8a77961_8h.md#a0dde513760c3f51a132595cb115bd8d7)#define PIN\_SD3\_DATA3 RCAR\_GP\_PIN(4, 12)

[ 51](pinctrl-r8a77961_8h.md#afb26ab3d47ade897128f6fbf813194ce)#define PIN\_SD3\_DATA4 RCAR\_GP\_PIN(4, 13)

[ 52](pinctrl-r8a77961_8h.md#a208de44c488e295d9273b7aedcf9e8d1)#define PIN\_SD3\_DATA5 RCAR\_GP\_PIN(4, 14)

[ 53](pinctrl-r8a77961_8h.md#afbdd386ea39f7ea9fa385cf745275ac9)#define PIN\_SD3\_DATA6 RCAR\_GP\_PIN(4, 15)

[ 54](pinctrl-r8a77961_8h.md#a909dc2a05f2b88445369671a0847a852)#define PIN\_SD3\_DATA7 RCAR\_GP\_PIN(4, 16)

[ 55](pinctrl-r8a77961_8h.md#adde84de73e6374d40047ef3de995090e)#define PIN\_SD3\_DS RCAR\_GP\_PIN(4, 17)

56

[ 57](pinctrl-r8a77961_8h.md#a7a01627dcec544bd7e3e01d4996acea8)#define PIN\_TX2\_A RCAR\_GP\_PIN(5, 10)

[ 58](pinctrl-r8a77961_8h.md#a125cf5d4f3c7289781ff48f749769678)#define PIN\_RX2\_A RCAR\_GP\_PIN(5, 11)

59

60/\* Pinmux function declarations \*/

[ 61](pinctrl-r8a77961_8h.md#a5ce6a833bb0ad61190df883918cfdb90)#define FUNC\_SD0\_CLK IPSR(7, 12, 0)

[ 62](pinctrl-r8a77961_8h.md#af9797ea2cd593d5d977be6b159576295)#define FUNC\_SD0\_CMD IPSR(7, 16, 0)

[ 63](pinctrl-r8a77961_8h.md#abcf11d2e31a515ebb0694e7d16e2c187)#define FUNC\_SD0\_DAT0 IPSR(7, 20, 0)

[ 64](pinctrl-r8a77961_8h.md#a5c694af48f26214df863de31b91266ff)#define FUNC\_SD0\_DAT1 IPSR(7, 24, 0)

[ 65](pinctrl-r8a77961_8h.md#ad4a067fdab442ccac531e74fb19e9f53)#define FUNC\_SD0\_DAT2 IPSR(8, 0, 0)

[ 66](pinctrl-r8a77961_8h.md#aa3102eee3d55a85934f8e2c8a623130a)#define FUNC\_SD0\_DAT3 IPSR(8, 4, 0)

[ 67](pinctrl-r8a77961_8h.md#a46273200ef710e6b425b1510c34b62eb)#define FUNC\_SD0\_CD IPSR(11, 8, 0)

[ 68](pinctrl-r8a77961_8h.md#a690ab7efdc5833adfa278b9bb84d3fb5)#define FUNC\_SD0\_WP IPSR(11, 12, 0)

69

[ 70](pinctrl-r8a77961_8h.md#a81cf49d2922e723432c8076e65638fe2)#define FUNC\_SD1\_CLK IPSR(8, 8, 0)

[ 71](pinctrl-r8a77961_8h.md#a4d6984780c71b7fb7910101abe09c271)#define FUNC\_SD1\_CMD IPSR(8, 12, 0)

[ 72](pinctrl-r8a77961_8h.md#a568164086138248b2fdf66a2e43022dd)#define FUNC\_SD1\_DAT0 IPSR(8, 16, 0)

[ 73](pinctrl-r8a77961_8h.md#a51c01c73de6ebc9a98d4faadb1c63bad)#define FUNC\_SD1\_DAT1 IPSR(8, 20, 0)

[ 74](pinctrl-r8a77961_8h.md#a28015798be631661be2162ec8656248d)#define FUNC\_SD1\_DAT2 IPSR(8, 24, 0)

[ 75](pinctrl-r8a77961_8h.md#a4aaa9d8004912c1bd864937cbfe6e91c)#define FUNC\_SD1\_DAT3 IPSR(8, 28, 0)

[ 76](pinctrl-r8a77961_8h.md#a0f9556feb59f6c796cf6c32f737e1c31)#define FUNC\_SD1\_CD IPSR(11, 16, 0)

[ 77](pinctrl-r8a77961_8h.md#a7ac7926422eb6e6b31ec445538f324ad)#define FUNC\_SD1\_WP IPSR(11, 20, 0)

78

[ 79](pinctrl-r8a77961_8h.md#a6c2348ea9cf186dbccd49c1a2abd0da7)#define FUNC\_SD2\_CLK IPSR(9, 0, 0)

[ 80](pinctrl-r8a77961_8h.md#a88f0024cde0d50a32807dd8cdf5b4389)#define FUNC\_SD2\_CMD IPSR(9, 4, 0)

[ 81](pinctrl-r8a77961_8h.md#a3ea4683d67ce0b2d06822f16cbd3b59c)#define FUNC\_SD2\_DAT0 IPSR(9, 8, 0)

[ 82](pinctrl-r8a77961_8h.md#a8473ad838931442919e5b591c8f95796)#define FUNC\_SD2\_DAT1 IPSR(9, 12, 0)

[ 83](pinctrl-r8a77961_8h.md#acf0ab8033fac1d5758f6a5c753a32b33)#define FUNC\_SD2\_DAT2 IPSR(9, 16, 0)

[ 84](pinctrl-r8a77961_8h.md#a9210845a41b5832f681fbc4cb2aa5ff6)#define FUNC\_SD2\_DAT3 IPSR(9, 20, 0)

[ 85](pinctrl-r8a77961_8h.md#a4df55f6f90dd4bce5705ac24e9cc0600)#define FUNC\_SD2\_DAT4 IPSR(8, 16, 1)

[ 86](pinctrl-r8a77961_8h.md#ab37ea755a87ec6f89e93911184c1cd0c)#define FUNC\_SD2\_DAT5 IPSR(8, 20, 1)

[ 87](pinctrl-r8a77961_8h.md#af2768c877d254505756e9af28bd23f62)#define FUNC\_SD2\_DAT6 IPSR(8, 24, 1)

[ 88](pinctrl-r8a77961_8h.md#a01f47facca05a3c385ba51e869cd803c)#define FUNC\_SD2\_DAT7 IPSR(8, 28, 1)

[ 89](pinctrl-r8a77961_8h.md#a66c9aeb2657b3e386c8db786e6cea798)#define FUNC\_SD2\_CD\_A IPSR(10, 20, 1)

[ 90](pinctrl-r8a77961_8h.md#af2f2c5b456eaa714b42c418dde1f7985)#define FUNC\_SD2\_WP\_A IPSR(10, 24, 1)

[ 91](pinctrl-r8a77961_8h.md#aa7e62f7d5eb84bf5c5490ad292fb616d)#define FUNC\_SD2\_CD\_B IPSR(13, 0, 3)

[ 92](pinctrl-r8a77961_8h.md#aaa1589026a2e23785fd1fc73abadf52c)#define FUNC\_SD2\_WP\_B IPSR(13, 4, 3)

[ 93](pinctrl-r8a77961_8h.md#af5c3ef672078bb8a0bf237c05e35ee0f)#define FUNC\_SD2\_DS IPSR(9, 24, 0)

94

[ 95](pinctrl-r8a77961_8h.md#a8c59452a7b2dbbf5b4737a8081f49be4)#define FUNC\_SD3\_CLK IPSR(9, 28, 0)

[ 96](pinctrl-r8a77961_8h.md#a5f3c66f2700f82bbfbd22ac6800f1f59)#define FUNC\_SD3\_CMD IPSR(10, 0, 0)

[ 97](pinctrl-r8a77961_8h.md#a3cca6cc972949389b8db8a4150c0bb87)#define FUNC\_SD3\_DAT0 IPSR(10, 4, 0)

[ 98](pinctrl-r8a77961_8h.md#af8ef78275bb0d057a4ec922a415d843b)#define FUNC\_SD3\_DAT1 IPSR(10, 8, 0)

[ 99](pinctrl-r8a77961_8h.md#a94622685e54b4a633ec28ce1782af300)#define FUNC\_SD3\_DAT2 IPSR(10, 12, 0)

[ 100](pinctrl-r8a77961_8h.md#a89dc6f9c809b77d44566add576def4c2)#define FUNC\_SD3\_DAT3 IPSR(10, 16, 0)

[ 101](pinctrl-r8a77961_8h.md#af6e3d20c2bffdbaa334aecf57fec3a8f)#define FUNC\_SD3\_DAT4 IPSR(10, 20, 0)

[ 102](pinctrl-r8a77961_8h.md#a4f524dd2bda183bbe0d4a39b730c65d5)#define FUNC\_SD3\_DAT5 IPSR(10, 24, 0)

[ 103](pinctrl-r8a77961_8h.md#ad39374a725b9d136cc7ccfd1a8e40998)#define FUNC\_SD3\_DAT6 IPSR(10, 28, 0)

[ 104](pinctrl-r8a77961_8h.md#a19a39341ce73e57f2f24d7eef0903459)#define FUNC\_SD3\_DAT7 IPSR(11, 0, 0)

[ 105](pinctrl-r8a77961_8h.md#a21f1bae5fb412a38bd89d689f6faba0a)#define FUNC\_SD3\_CD IPSR(10, 28, 1)

[ 106](pinctrl-r8a77961_8h.md#adf1a84bb24f42fc4054c037dca07ebb5)#define FUNC\_SD3\_WP IPSR(11, 0, 1)

[ 107](pinctrl-r8a77961_8h.md#a5fb555e0e8b52101cbd9c3140910fa12)#define FUNC\_SD3\_DS IPSR(11, 4, 0)

108

[ 109](pinctrl-r8a77961_8h.md#a8dd586d735e01762fab43e1cfc847258)#define FUNC\_TX2\_A IPSR(13, 0, 0)

[ 110](pinctrl-r8a77961_8h.md#acc7ae012c901aafa196d7e39637985d6)#define FUNC\_RX2\_A IPSR(13, 4, 0)

111

112#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_R8A77961\_H\_ \*/

[pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-r8a77961.h](pinctrl-r8a77961_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
