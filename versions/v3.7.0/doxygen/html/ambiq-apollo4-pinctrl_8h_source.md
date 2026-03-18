---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ambiq-apollo4-pinctrl_8h_source.html
original_path: doxygen/html/ambiq-apollo4-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ambiq-apollo4-pinctrl.h

[Go to the documentation of this file.](ambiq-apollo4-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2023 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_APOLLO4\_PINCTRL\_H\_\_

8#define \_\_APOLLO4\_PINCTRL\_H\_\_

9

[ 10](ambiq-apollo4-pinctrl_8h.md#aad69bd7372283ab49bae2478e2695832)#define APOLLO4\_ALT\_FUNC\_POS 0

[ 11](ambiq-apollo4-pinctrl_8h.md#abfa1ad75be5bb9dbe60ce4f82fb669d5)#define APOLLO4\_ALT\_FUNC\_MASK 0xf

12

[ 13](ambiq-apollo4-pinctrl_8h.md#ab9b66c304105a703bf9beb8b01246aa3)#define APOLLO4\_PIN\_NUM\_POS 4

[ 14](ambiq-apollo4-pinctrl_8h.md#aca5be2343303d2e76533d2d3b0016a2f)#define APOLLO4\_PIN\_NUM\_MASK 0x7f

15

[ 16](ambiq-apollo4-pinctrl_8h.md#a0bb5466111e8e39af5d54e3a713a660d)#define APOLLO4\_PINMUX(pin\_num, alt\_func) (pin\_num << APOLLO4\_PIN\_NUM\_POS | \

17 alt\_func << APOLLO4\_ALT\_FUNC\_POS)

18

[ 19](ambiq-apollo4-pinctrl_8h.md#aa712953fa0a32e5f2f187a7afd8cefc2)#define SWTRACECLK\_P0 APOLLO4\_PINMUX(0, 0)

[ 20](ambiq-apollo4-pinctrl_8h.md#a3a72f1023828af4b3766cc0714c404b2)#define SLSCL\_P0 APOLLO4\_PINMUX(0, 1)

[ 21](ambiq-apollo4-pinctrl_8h.md#ae72cb1519562643c48a8ffff88dc9d00)#define SLSCK\_P0 APOLLO4\_PINMUX(0, 2)

[ 22](ambiq-apollo4-pinctrl_8h.md#ada3eedfe2cf44d8f0f1c21d10fc7c81a)#define GPIO\_P0 APOLLO4\_PINMUX(0, 3)

[ 23](ambiq-apollo4-pinctrl_8h.md#ae4a9368b338c1901ddc143cfe6d9a0ad)#define UART0TX\_P0 APOLLO4\_PINMUX(0, 4)

[ 24](ambiq-apollo4-pinctrl_8h.md#aae553db761d57d01e4608d7cf37cc09c)#define UART1TX\_P0 APOLLO4\_PINMUX(0, 5)

[ 25](ambiq-apollo4-pinctrl_8h.md#adb1a8c7b38b4911880451d58c9545c65)#define CT0\_P0 APOLLO4\_PINMUX(0, 6)

[ 26](ambiq-apollo4-pinctrl_8h.md#a2f7a5ec8bae150c5d845a85d65991107)#define NCE0\_P0 APOLLO4\_PINMUX(0, 7)

[ 27](ambiq-apollo4-pinctrl_8h.md#adbfd549022c7a945371d2d5180d488ed)#define OBSBUS0\_P0 APOLLO4\_PINMUX(0, 8)

[ 28](ambiq-apollo4-pinctrl_8h.md#af73c0cefc9dcb548664882050a0316b8)#define VCMPO\_P0 APOLLO4\_PINMUX(0, 9)

[ 29](ambiq-apollo4-pinctrl_8h.md#a76fa068540c84fbe51d453856dd77423)#define FPIO\_P0 APOLLO4\_PINMUX(0, 11)

[ 30](ambiq-apollo4-pinctrl_8h.md#ac812904e17f8134b1849b8d3d9c14a10)#define SWTRACE0\_P1 APOLLO4\_PINMUX(1, 0)

[ 31](ambiq-apollo4-pinctrl_8h.md#ae5b84a6fa44069d704c6c87113bef6e7)#define SLSDAWIR3\_P1 APOLLO4\_PINMUX(1, 1)

[ 32](ambiq-apollo4-pinctrl_8h.md#a4fd87e65fcf8776a98224ca1d468b0ad)#define SLMOSI\_P1 APOLLO4\_PINMUX(1, 2)

[ 33](ambiq-apollo4-pinctrl_8h.md#af7a3fb155e6285875e885d5a6344041d)#define GPIO\_P1 APOLLO4\_PINMUX(1, 3)

[ 34](ambiq-apollo4-pinctrl_8h.md#ac35c1ebef7c2d98d418bfa9fe55152f9)#define UART2TX\_P1 APOLLO4\_PINMUX(1, 4)

[ 35](ambiq-apollo4-pinctrl_8h.md#a1b8835718a0c3b296d37a0f6fdcbb030)#define UART3TX\_P1 APOLLO4\_PINMUX(1, 5)

[ 36](ambiq-apollo4-pinctrl_8h.md#adbd4a7fb3796ca8b22dc91a39f64676a)#define CT1\_P1 APOLLO4\_PINMUX(1, 6)

[ 37](ambiq-apollo4-pinctrl_8h.md#aad38da06e56246b4ed48ddbf43f1aaca)#define NCE1\_P1 APOLLO4\_PINMUX(1, 7)

[ 38](ambiq-apollo4-pinctrl_8h.md#a4e9efe5ed8ce7a01d2c56a81d42b482e)#define OBSBUS1\_P1 APOLLO4\_PINMUX(1, 8)

[ 39](ambiq-apollo4-pinctrl_8h.md#a30f453f721382fa84e37a82dc56a5071)#define VCMPO\_P1 APOLLO4\_PINMUX(1, 9)

[ 40](ambiq-apollo4-pinctrl_8h.md#a03f6c799958d3076337d1fcdcc6c6be3)#define FPIO\_P1 APOLLO4\_PINMUX(1, 11)

[ 41](ambiq-apollo4-pinctrl_8h.md#a35316119c93c5f145ac68aa209133b87)#define SCANIN4\_P1 APOLLO4\_PINMUX(1, 15)

[ 42](ambiq-apollo4-pinctrl_8h.md#ababa73c9fe1c5e8657cce61446e2e2d3)#define SWTRACE1\_P2 APOLLO4\_PINMUX(2, 0)

[ 43](ambiq-apollo4-pinctrl_8h.md#a06beb22570d100e28198606d21909a6c)#define SLMISO\_P2 APOLLO4\_PINMUX(2, 1)

[ 44](ambiq-apollo4-pinctrl_8h.md#a557619ff079bacadd982d560243550fd)#define TRIG1\_P2 APOLLO4\_PINMUX(2, 2)

[ 45](ambiq-apollo4-pinctrl_8h.md#aea5b197be9a863a6db90cb9d42b8a9f2)#define GPIO\_P2 APOLLO4\_PINMUX(2, 3)

[ 46](ambiq-apollo4-pinctrl_8h.md#aeb4da21d8f3fdb747865ff6b6a7ea49e)#define UART0RX\_P2 APOLLO4\_PINMUX(2, 4)

[ 47](ambiq-apollo4-pinctrl_8h.md#a3795e6445756b68c436b6d0fb1c7813b)#define UART1RX\_P2 APOLLO4\_PINMUX(2, 5)

[ 48](ambiq-apollo4-pinctrl_8h.md#a63413b9cd6e926e1aa678ad092b34c80)#define CT2\_P2 APOLLO4\_PINMUX(2, 6)

[ 49](ambiq-apollo4-pinctrl_8h.md#a41c7834b7cc3a8f2f75021ec9ebedf6a)#define NCE2\_P2 APOLLO4\_PINMUX(2, 7)

[ 50](ambiq-apollo4-pinctrl_8h.md#a90482534a21cc6ff8b40308e6295b296)#define OBSBUS2\_P2 APOLLO4\_PINMUX(2, 8)

[ 51](ambiq-apollo4-pinctrl_8h.md#a311cd1025e9151407e913334a660ec18)#define VCMPO\_P2 APOLLO4\_PINMUX(2, 9)

[ 52](ambiq-apollo4-pinctrl_8h.md#aa946ad718c6556b8026c5ed4ab993f1a)#define FPIO\_P2 APOLLO4\_PINMUX(2, 11)

[ 53](ambiq-apollo4-pinctrl_8h.md#a41cc65ed8cda3f1891815b70ae42d8e6)#define SCANRSTN\_P2 APOLLO4\_PINMUX(2, 15)

[ 54](ambiq-apollo4-pinctrl_8h.md#af12a5e0d7aee243897c901b4d632b481)#define SWTRACE2\_P3 APOLLO4\_PINMUX(3, 0)

[ 55](ambiq-apollo4-pinctrl_8h.md#a42fc82a09d814a6774ee02b1b0228cd8)#define SLNCE\_P3 APOLLO4\_PINMUX(3, 1)

[ 56](ambiq-apollo4-pinctrl_8h.md#a54478891a88b718aecef7230bb440a51)#define SWO\_P3 APOLLO4\_PINMUX(3, 2)

[ 57](ambiq-apollo4-pinctrl_8h.md#af4024d1ac41ed0426ca701ea851dcd82)#define GPIO\_P3 APOLLO4\_PINMUX(3, 3)

[ 58](ambiq-apollo4-pinctrl_8h.md#ae04c623f892eeb17da6a4f4a559a7c1b)#define UART2RX\_P3 APOLLO4\_PINMUX(3, 4)

[ 59](ambiq-apollo4-pinctrl_8h.md#a65d7b7a3b983b8f76996c6f62a0e8dd8)#define UART3RX\_P3 APOLLO4\_PINMUX(3, 5)

[ 60](ambiq-apollo4-pinctrl_8h.md#a83fcb824ba562db420849bbaf24bb98c)#define CT3\_P3 APOLLO4\_PINMUX(3, 6)

[ 61](ambiq-apollo4-pinctrl_8h.md#a49fa96fac299d83fe34b116fc2e8d586)#define NCE3\_P3 APOLLO4\_PINMUX(3, 7)

[ 62](ambiq-apollo4-pinctrl_8h.md#a24aa30cfa37200847e241fb3d872c3ba)#define OBSBUS3\_P3 APOLLO4\_PINMUX(3, 8)

[ 63](ambiq-apollo4-pinctrl_8h.md#af7a1d6f9316d7fc87485ade560109969)#define FPIO\_P3 APOLLO4\_PINMUX(3, 11)

[ 64](ambiq-apollo4-pinctrl_8h.md#a4b6895f935a874d89d75652fc3622da9)#define SCANIN5\_P3 APOLLO4\_PINMUX(3, 15)

[ 65](ambiq-apollo4-pinctrl_8h.md#a80141a6c29ac589a8bc520e9ffd1f920)#define SWTRACE3\_P4 APOLLO4\_PINMUX(4, 0)

[ 66](ambiq-apollo4-pinctrl_8h.md#a29c616828e653cb4f0cecaca1f0bc8f1)#define SLINT\_P4 APOLLO4\_PINMUX(4, 1)

[ 67](ambiq-apollo4-pinctrl_8h.md#ad00e0aa91708b761cc5d65e5419273a8)#define XT32KHZ\_P4 APOLLO4\_PINMUX(4, 2)

[ 68](ambiq-apollo4-pinctrl_8h.md#aea71dd1d14466cec98ab057ece573f75)#define GPIO\_P4 APOLLO4\_PINMUX(4, 3)

[ 69](ambiq-apollo4-pinctrl_8h.md#a2c947213b6bacdc9fc49bf27c22442cb)#define UART0RTS\_P4 APOLLO4\_PINMUX(4, 4)

[ 70](ambiq-apollo4-pinctrl_8h.md#aa6ee11936e8fb9604386be28d7079295)#define UART1RTS\_P4 APOLLO4\_PINMUX(4, 5)

[ 71](ambiq-apollo4-pinctrl_8h.md#afec1f8636fcb3f5745523847901361fa)#define CT4\_P4 APOLLO4\_PINMUX(4, 6)

[ 72](ambiq-apollo4-pinctrl_8h.md#a3019076e21641ad28be64b29a4b2c671)#define NCE4\_P4 APOLLO4\_PINMUX(4, 7)

[ 73](ambiq-apollo4-pinctrl_8h.md#aef633955e81dca4d6ebfb9f7a098789f)#define OBSBUS4\_P4 APOLLO4\_PINMUX(4, 8)

[ 74](ambiq-apollo4-pinctrl_8h.md#a64f37706686ee4643f067324b433e756)#define I2S0\_SDIN\_P4 APOLLO4\_PINMUX(4, 9)

[ 75](ambiq-apollo4-pinctrl_8h.md#a1cc409edd73a8e80be63d7ce63e17f05)#define I2S1\_SDIN\_P4 APOLLO4\_PINMUX(4, 10)

[ 76](ambiq-apollo4-pinctrl_8h.md#a043b4dda39f804254555d52a169dbf3d)#define FPIO\_P4 APOLLO4\_PINMUX(4, 11)

[ 77](ambiq-apollo4-pinctrl_8h.md#a110fe23686526743c97731fd9a3a4c43)#define FLB\_TDO\_P4 APOLLO4\_PINMUX(4, 12)

[ 78](ambiq-apollo4-pinctrl_8h.md#a1993eaa6d819da48df34bfb7ac8dff6b)#define FLLOAD\_DIR\_P4 APOLLO4\_PINMUX(4, 13)

[ 79](ambiq-apollo4-pinctrl_8h.md#a0c74f8d376e2d7d7b3b07f75b5656acd)#define MDA\_TDO\_P4 APOLLO4\_PINMUX(4, 14)

[ 80](ambiq-apollo4-pinctrl_8h.md#a241b7dbfcfc91ced94957ea1cbf2992d)#define OPCG\_TRIG\_P4 APOLLO4\_PINMUX(4, 15)

[ 81](ambiq-apollo4-pinctrl_8h.md#a89285a703eabc9b9cc9c962dd7f8856c)#define M0SCL\_P5 APOLLO4\_PINMUX(5, 0)

[ 82](ambiq-apollo4-pinctrl_8h.md#abf59b5c6ff03c8a2652d3bc72b872295)#define M0SCK\_P5 APOLLO4\_PINMUX(5, 1)

[ 83](ambiq-apollo4-pinctrl_8h.md#a31ed8eee5a314d9354b12264b30fcbad)#define I2S0\_CLK\_P5 APOLLO4\_PINMUX(5, 2)

[ 84](ambiq-apollo4-pinctrl_8h.md#a8b6393ba023af44294a82048f4d7b7fb)#define GPIO\_P5 APOLLO4\_PINMUX(5, 3)

[ 85](ambiq-apollo4-pinctrl_8h.md#a850dea18da3b36c74c869b77d888f3c0)#define UART2RTS\_P5 APOLLO4\_PINMUX(5, 4)

[ 86](ambiq-apollo4-pinctrl_8h.md#a5c4e2b9b7c045a494e9c44274b506692)#define UART3RTS\_P5 APOLLO4\_PINMUX(5, 5)

[ 87](ambiq-apollo4-pinctrl_8h.md#a9a1bf214635deb6e084f8c7188992c02)#define CT5\_P5 APOLLO4\_PINMUX(5, 6)

[ 88](ambiq-apollo4-pinctrl_8h.md#a81570665b8a85bc441414b8e7fc455af)#define NCE5\_P5 APOLLO4\_PINMUX(5, 7)

[ 89](ambiq-apollo4-pinctrl_8h.md#ac8300e420fce3bf25795df53cd2e9348)#define OBSBUS5\_P5 APOLLO4\_PINMUX(5, 8)

[ 90](ambiq-apollo4-pinctrl_8h.md#ac8e360737e7553fda96f9af30dc1d07c)#define I2S1\_CLK\_P5 APOLLO4\_PINMUX(5, 10)

[ 91](ambiq-apollo4-pinctrl_8h.md#aa1aa98f4748159111cae90499d234a3d)#define FPIO\_P5 APOLLO4\_PINMUX(5, 11)

[ 92](ambiq-apollo4-pinctrl_8h.md#a1813bd8a8efce2322c0cc685da5b9499)#define FLB\_TDI\_P5 APOLLO4\_PINMUX(5, 12)

[ 93](ambiq-apollo4-pinctrl_8h.md#aa68864c31d6e429b8127e44827213ead)#define FLLOAD\_DATA\_P5 APOLLO4\_PINMUX(5, 13)

[ 94](ambiq-apollo4-pinctrl_8h.md#adb3d721ff3a10bc7dcccb850238b5537)#define MDA\_SRST\_P5 APOLLO4\_PINMUX(5, 14)

[ 95](ambiq-apollo4-pinctrl_8h.md#a092058870863de95f94adbea76c61220)#define DFT\_ISO\_P5 APOLLO4\_PINMUX(5, 15)

[ 96](ambiq-apollo4-pinctrl_8h.md#a70ecddbefb03c277a58ab1f8c6f4972c)#define M0SDAWIR3\_P6 APOLLO4\_PINMUX(6, 0)

[ 97](ambiq-apollo4-pinctrl_8h.md#a4d4e7aae6f9ab5902da5150fe5fcde12)#define M0MOSI\_P6 APOLLO4\_PINMUX(6, 1)

[ 98](ambiq-apollo4-pinctrl_8h.md#a2926302a00d48d49af9d0d96d58c30df)#define I2S0\_DATA\_P6 APOLLO4\_PINMUX(6, 2)

[ 99](ambiq-apollo4-pinctrl_8h.md#ab92e5b2728491c7718e22490337a877c)#define GPIO\_P6 APOLLO4\_PINMUX(6, 3)

[ 100](ambiq-apollo4-pinctrl_8h.md#a65b79279c0903c662779e6b320234842)#define UART0CTS\_P6 APOLLO4\_PINMUX(6, 4)

[ 101](ambiq-apollo4-pinctrl_8h.md#aff62a9a507269dae303ffcba3ee117ef)#define UART1CTS\_P6 APOLLO4\_PINMUX(6, 5)

[ 102](ambiq-apollo4-pinctrl_8h.md#a037fb06915bcd4dd5cb7de89977fbe89)#define CT6\_P6 APOLLO4\_PINMUX(6, 6)

[ 103](ambiq-apollo4-pinctrl_8h.md#a5545d8bb20f41310c0ce3f67f148f28b)#define NCE6\_P6 APOLLO4\_PINMUX(6, 7)

[ 104](ambiq-apollo4-pinctrl_8h.md#ac7b99eca53b82adbb09ffd032179b198)#define OBSBUS6\_P6 APOLLO4\_PINMUX(6, 8)

[ 105](ambiq-apollo4-pinctrl_8h.md#a3c7a408d7a9883829490863e6a67ff29)#define I2S0\_SDOUT\_P6 APOLLO4\_PINMUX(6, 9)

[ 106](ambiq-apollo4-pinctrl_8h.md#a4952c05634c4ee1dd74c6763ef70e763)#define I2S1\_SDOUT\_P6 APOLLO4\_PINMUX(6, 10)

[ 107](ambiq-apollo4-pinctrl_8h.md#a0a8c08d5d84a7ca451b239feb2b1f324)#define FPIO\_P6 APOLLO4\_PINMUX(6, 11)

[ 108](ambiq-apollo4-pinctrl_8h.md#a1d5598069206acd9a817dc6c049a6ab1)#define SCANIN6\_P6 APOLLO4\_PINMUX(6, 15)

[ 109](ambiq-apollo4-pinctrl_8h.md#a2eaa68aa736da8dc85ed826ed1cfb9b3)#define M0MISO\_P7 APOLLO4\_PINMUX(7, 0)

[ 110](ambiq-apollo4-pinctrl_8h.md#a00614cfc545401d5e8cb9f1e51848571)#define TRIG0\_P7 APOLLO4\_PINMUX(7, 1)

[ 111](ambiq-apollo4-pinctrl_8h.md#a026783aafb41f25f522da6e6d407a5d0)#define I2S0\_WS\_P7 APOLLO4\_PINMUX(7, 2)

[ 112](ambiq-apollo4-pinctrl_8h.md#a56c293ec75689c3c233d7a0ad4d7428e)#define GPIO\_P7 APOLLO4\_PINMUX(7, 3)

[ 113](ambiq-apollo4-pinctrl_8h.md#a70bacd644c1f6bd5761fd9826344dc2d)#define UART2CTS\_P7 APOLLO4\_PINMUX(7, 4)

[ 114](ambiq-apollo4-pinctrl_8h.md#a91197ebfabd794f5f0653f085249a8c9)#define UART3CTS\_P7 APOLLO4\_PINMUX(7, 5)

[ 115](ambiq-apollo4-pinctrl_8h.md#a45c9bca3d0fcefa7af6d33d39e4b96eb)#define CT7\_P7 APOLLO4\_PINMUX(7, 6)

[ 116](ambiq-apollo4-pinctrl_8h.md#ac34242faa4992e4acc075a36264d7187)#define NCE7\_P7 APOLLO4\_PINMUX(7, 7)

[ 117](ambiq-apollo4-pinctrl_8h.md#a6a00216d761ecb9a4127476daa412ce5)#define OBSBUS7\_P7 APOLLO4\_PINMUX(7, 8)

[ 118](ambiq-apollo4-pinctrl_8h.md#a79eebce5d895931c9ea032d9a24012b0)#define I2S1\_WS\_P7 APOLLO4\_PINMUX(7, 10)

[ 119](ambiq-apollo4-pinctrl_8h.md#a2e5cc66b06c8912f1e69db9867705931)#define FPIO\_P7 APOLLO4\_PINMUX(7, 11)

[ 120](ambiq-apollo4-pinctrl_8h.md#a1731543230a53064b63468a464660b09)#define SCANIN7\_P7 APOLLO4\_PINMUX(7, 15)

[ 121](ambiq-apollo4-pinctrl_8h.md#adb017ff6ee9e3ee6514e970fae370a43)#define CMPRF1\_P8 APOLLO4\_PINMUX(8, 0)

[ 122](ambiq-apollo4-pinctrl_8h.md#a74ddacb536c2f97254f468eb3de59113)#define TRIG1\_P8 APOLLO4\_PINMUX(8, 1)

[ 123](ambiq-apollo4-pinctrl_8h.md#a98e2e72127f9d8302c72d588b005ad43)#define GPIO\_P8 APOLLO4\_PINMUX(8, 3)

[ 124](ambiq-apollo4-pinctrl_8h.md#a78f6a3daba1c3af73d6f56e201716c9d)#define M1SCL\_P8 APOLLO4\_PINMUX(8, 4)

[ 125](ambiq-apollo4-pinctrl_8h.md#aeca27870849b7a78edc8fe37b9966f23)#define M1SCK\_P8 APOLLO4\_PINMUX(8, 5)

[ 126](ambiq-apollo4-pinctrl_8h.md#a94f102cd8f4501e94b77973e459c1c14)#define CT8\_P8 APOLLO4\_PINMUX(8, 6)

[ 127](ambiq-apollo4-pinctrl_8h.md#a6c400fdb4e2e68a5a28f2aade3509822)#define NCE8\_P8 APOLLO4\_PINMUX(8, 7)

[ 128](ambiq-apollo4-pinctrl_8h.md#a45a4bb0b3ede6c90f5d9b0a698fd02c2)#define OBSBUS8\_P8 APOLLO4\_PINMUX(8, 8)

[ 129](ambiq-apollo4-pinctrl_8h.md#a30675113fa36529db612ee3440a912cc)#define FPIO\_P8 APOLLO4\_PINMUX(8, 11)

[ 130](ambiq-apollo4-pinctrl_8h.md#a07066d84db8da27ced2be27f8cda6571)#define SCANOUT4\_P8 APOLLO4\_PINMUX(8, 15)

[ 131](ambiq-apollo4-pinctrl_8h.md#a6a61c02e81421a98561de18f48c5d7c1)#define CMPRF0\_P9 APOLLO4\_PINMUX(9, 0)

[ 132](ambiq-apollo4-pinctrl_8h.md#ade7ec84df92ce9638b0dd5a7d455b50c)#define TRIG2\_P9 APOLLO4\_PINMUX(9, 1)

[ 133](ambiq-apollo4-pinctrl_8h.md#a62ba7982361959a0ff4013c825611344)#define GPIO\_P9 APOLLO4\_PINMUX(9, 3)

[ 134](ambiq-apollo4-pinctrl_8h.md#a8a5ee0496cfaf6fe7c0475459ab7ee23)#define M1SDAWIR3\_P9 APOLLO4\_PINMUX(9, 4)

[ 135](ambiq-apollo4-pinctrl_8h.md#a6970a506d3ae40f58819407df0b702ef)#define M1MOSI\_P9 APOLLO4\_PINMUX(9, 5)

[ 136](ambiq-apollo4-pinctrl_8h.md#a822612157497cc4f96c9da3e14bd4e9b)#define CT9\_P9 APOLLO4\_PINMUX(9, 6)

[ 137](ambiq-apollo4-pinctrl_8h.md#aa92d1c97c14770e3e29a271706d76a28)#define NCE9\_P9 APOLLO4\_PINMUX(9, 7)

[ 138](ambiq-apollo4-pinctrl_8h.md#a8d599c9c94f22138efa4e7933436d4ac)#define OBSBUS9\_P9 APOLLO4\_PINMUX(9, 8)

[ 139](ambiq-apollo4-pinctrl_8h.md#aa357814dfe944dd462b25690ec80fff1)#define FPIO\_P9 APOLLO4\_PINMUX(9, 11)

[ 140](ambiq-apollo4-pinctrl_8h.md#aa6aa4639835abb201973be3696114755)#define SCANOUT5\_P9 APOLLO4\_PINMUX(9, 15)

[ 141](ambiq-apollo4-pinctrl_8h.md#a7a9a5e45cb055414a1839a2d685ad4eb)#define CMPIN0\_P10 APOLLO4\_PINMUX(10, 0)

[ 142](ambiq-apollo4-pinctrl_8h.md#a8c57665998a735452492121e4dac55c1)#define TRIG3\_P10 APOLLO4\_PINMUX(10, 1)

[ 143](ambiq-apollo4-pinctrl_8h.md#aeae1f6c04e5fc3c420c3c2311e91c0fb)#define GPIO\_P10 APOLLO4\_PINMUX(10, 3)

[ 144](ambiq-apollo4-pinctrl_8h.md#a30ab835d51d600eb059631828c323f67)#define M1MISO\_P10 APOLLO4\_PINMUX(10, 4)

[ 145](ambiq-apollo4-pinctrl_8h.md#a21325f84d5a680dee55253bbe2871a72)#define CT10\_P10 APOLLO4\_PINMUX(10, 6)

[ 146](ambiq-apollo4-pinctrl_8h.md#aad947baa0652e59cb21735eae01eca09)#define NCE10\_P10 APOLLO4\_PINMUX(10, 7)

[ 147](ambiq-apollo4-pinctrl_8h.md#a2d270a862d5c76f63b73b104f9370a2e)#define OBSBUS10\_P10 APOLLO4\_PINMUX(10, 8)

[ 148](ambiq-apollo4-pinctrl_8h.md#aa40251425bc0fda45922f9d141f79b00)#define DISP\_TE\_P10 APOLLO4\_PINMUX(10, 9)

[ 149](ambiq-apollo4-pinctrl_8h.md#ac6a2a59ac46d434922ae5c3030a2c34e)#define FPIO\_P10 APOLLO4\_PINMUX(10, 11)

[ 150](ambiq-apollo4-pinctrl_8h.md#aae654852343169b655a996c9245a514d)#define OPCG\_LOAD\_P10 APOLLO4\_PINMUX(10, 15)

[ 151](ambiq-apollo4-pinctrl_8h.md#a2dffa369fa8a4ce9f07e055ea51957a2)#define CMPIN1\_P11 APOLLO4\_PINMUX(11, 0)

[ 152](ambiq-apollo4-pinctrl_8h.md#a7c7901d889823da0362d5dc5029912c7)#define TRIG0\_P11 APOLLO4\_PINMUX(11, 1)

[ 153](ambiq-apollo4-pinctrl_8h.md#a260768f49d30c053b7dbef6c14a61fc0)#define I2S0\_CLK\_P11 APOLLO4\_PINMUX(11, 2)

[ 154](ambiq-apollo4-pinctrl_8h.md#a1e2a5bd418526ffe665b93088178edc3)#define GPIO\_P11 APOLLO4\_PINMUX(11, 3)

[ 155](ambiq-apollo4-pinctrl_8h.md#a6612e178c09030d75a9fd2724be0781a)#define UART2RX\_P11 APOLLO4\_PINMUX(11, 4)

[ 156](ambiq-apollo4-pinctrl_8h.md#a5687894dd2bcd477c016da283500a93f)#define UART3RX\_P11 APOLLO4\_PINMUX(11, 5)

[ 157](ambiq-apollo4-pinctrl_8h.md#a412e5bacd5202a8c67d3405356e00a40)#define CT11\_P11 APOLLO4\_PINMUX(11, 6)

[ 158](ambiq-apollo4-pinctrl_8h.md#ab635978b874de8fbe6f96506b06ae5f1)#define NCE11\_P11 APOLLO4\_PINMUX(11, 7)

[ 159](ambiq-apollo4-pinctrl_8h.md#a46f284c12934bd31286e1fa32ed9e30f)#define OBSBUS11\_P11 APOLLO4\_PINMUX(11, 8)

[ 160](ambiq-apollo4-pinctrl_8h.md#a7168a447d080382cd6a48f80fbfd29ce)#define FPIO\_P11 APOLLO4\_PINMUX(11, 11)

[ 161](ambiq-apollo4-pinctrl_8h.md#a0ed3ae42d88110a9368df57708c08566)#define FLB\_TCLK\_P11 APOLLO4\_PINMUX(11, 12)

[ 162](ambiq-apollo4-pinctrl_8h.md#afab67c2cf8341df4b9307c78eafe0280)#define FLLOAD\_ADDR\_P11 APOLLO4\_PINMUX(11, 13)

[ 163](ambiq-apollo4-pinctrl_8h.md#a2e8a0b8461e3beee7cb7f2b2049d10be)#define MDA\_TCK\_P11 APOLLO4\_PINMUX(11, 14)

[ 164](ambiq-apollo4-pinctrl_8h.md#af6e6f967f6e8092396ccc034e0b57776)#define SCANIN0\_P11 APOLLO4\_PINMUX(11, 15)

[ 165](ambiq-apollo4-pinctrl_8h.md#a62e8082b44b7aa372783ebcfab497ebe)#define ADCSE7\_P12 APOLLO4\_PINMUX(12, 0)

[ 166](ambiq-apollo4-pinctrl_8h.md#a1b0719c77a932de39131519a93b95746)#define TRIG1\_P12 APOLLO4\_PINMUX(12, 1)

[ 167](ambiq-apollo4-pinctrl_8h.md#a704ba0251631993bd657c16edcb172b4)#define I2S0\_DATA\_P12 APOLLO4\_PINMUX(12, 2)

[ 168](ambiq-apollo4-pinctrl_8h.md#a2b368e24e962e0bdb34a68dc81a9e929)#define GPIO\_P12 APOLLO4\_PINMUX(12, 3)

[ 169](ambiq-apollo4-pinctrl_8h.md#a070b73ebb07cf49cf4475a61a19f35c8)#define UART0TX\_P12 APOLLO4\_PINMUX(12, 4)

[ 170](ambiq-apollo4-pinctrl_8h.md#ae86cb0f42ab5ae4105b89838173e7c4f)#define UART1TX\_P12 APOLLO4\_PINMUX(12, 5)

[ 171](ambiq-apollo4-pinctrl_8h.md#ab1ce41ea5c9a41e258d035d5517675cf)#define CT12\_P12 APOLLO4\_PINMUX(12, 6)

[ 172](ambiq-apollo4-pinctrl_8h.md#aeeea37f1af4c943883760c8e273f26a1)#define NCE12\_P12 APOLLO4\_PINMUX(12, 7)

[ 173](ambiq-apollo4-pinctrl_8h.md#a8c23805d9ce7ac260560d7273a27bcf8)#define OBSBUS12\_P12 APOLLO4\_PINMUX(12, 8)

[ 174](ambiq-apollo4-pinctrl_8h.md#a24e9377e2ed58935b734473315a13309)#define CMPRF2\_P12 APOLLO4\_PINMUX(12, 9)

[ 175](ambiq-apollo4-pinctrl_8h.md#aee652b7a2bec14d80b9d6985d8b71629)#define I2S0\_SDOUT\_P12 APOLLO4\_PINMUX(12, 10)

[ 176](ambiq-apollo4-pinctrl_8h.md#ab9b4efd45e891726c0a20828d2aeb6b7)#define FPIO\_P12 APOLLO4\_PINMUX(12, 11)

[ 177](ambiq-apollo4-pinctrl_8h.md#aadc57528b23c64b78cbf23954f6c8ef3)#define SCANOUT3\_P12 APOLLO4\_PINMUX(12, 15)

[ 178](ambiq-apollo4-pinctrl_8h.md#adb7003240592a4deb555a42bb235995f)#define ADCSE6\_P13 APOLLO4\_PINMUX(13, 0)

[ 179](ambiq-apollo4-pinctrl_8h.md#abfcc5faf81a1d35e95d9303c29eccd38)#define TRIG2\_P13 APOLLO4\_PINMUX(13, 1)

[ 180](ambiq-apollo4-pinctrl_8h.md#a2d99eb33fee726a7743d0bd188ad3aa9)#define I2S0\_WS\_P13 APOLLO4\_PINMUX(13, 2)

[ 181](ambiq-apollo4-pinctrl_8h.md#a9519265fbdd9fb2adfe818baa0ef933f)#define GPIO\_P13 APOLLO4\_PINMUX(13, 3)

[ 182](ambiq-apollo4-pinctrl_8h.md#aa6ddeaff720135edc990992e8a288a86)#define UART2TX\_P13 APOLLO4\_PINMUX(13, 4)

[ 183](ambiq-apollo4-pinctrl_8h.md#a2ed09c5389a4267fe3ffbadd4b614850)#define UART3TX\_P13 APOLLO4\_PINMUX(13, 5)

[ 184](ambiq-apollo4-pinctrl_8h.md#a623633e71ac60049761b8c65534a970f)#define CT13\_P13 APOLLO4\_PINMUX(13, 6)

[ 185](ambiq-apollo4-pinctrl_8h.md#a03383f0fcb11b35cac08703aa51cdb56)#define NCE13\_P13 APOLLO4\_PINMUX(13, 7)

[ 186](ambiq-apollo4-pinctrl_8h.md#a7464ef92fcda71c3ef718173a5170ef9)#define OBSBUS13\_P13 APOLLO4\_PINMUX(13, 8)

[ 187](ambiq-apollo4-pinctrl_8h.md#a53f7f23a97ca4f3ef32b232fb5f7ff29)#define FPIO\_P13 APOLLO4\_PINMUX(13, 11)

[ 188](ambiq-apollo4-pinctrl_8h.md#ab7c14e9429bc23c041605ff2444a2e6a)#define FLB\_FCLK\_P13 APOLLO4\_PINMUX(13, 12)

[ 189](ambiq-apollo4-pinctrl_8h.md#a323aa3ff7b396c9c2fb0c8f8d06e860b)#define FLLOAD\_DATA\_P13 APOLLO4\_PINMUX(13, 13)

[ 190](ambiq-apollo4-pinctrl_8h.md#a56d8ae53d9a0281d042bf7b6fefe55be)#define MDA\_TDI\_P13 APOLLO4\_PINMUX(13, 14)

[ 191](ambiq-apollo4-pinctrl_8h.md#a4bdc50605b78d8153edd62a32fc74eaf)#define SCANOUT0\_P13 APOLLO4\_PINMUX(13, 15)

[ 192](ambiq-apollo4-pinctrl_8h.md#ae41e0ec777697773a0ad22e174d46d00)#define ADCSE5\_P14 APOLLO4\_PINMUX(14, 0)

[ 193](ambiq-apollo4-pinctrl_8h.md#a4a91a2ae39a90a5b5949d54d1768101a)#define TRIG3\_P14 APOLLO4\_PINMUX(14, 1)

[ 194](ambiq-apollo4-pinctrl_8h.md#af24f89fe6d38c0db5d7f774e07228678)#define GPIO\_P14 APOLLO4\_PINMUX(14, 3)

[ 195](ambiq-apollo4-pinctrl_8h.md#a660dcc362f2a58e94df88e652e874511)#define MILLI\_CLK\_P14 APOLLO4\_PINMUX(14, 4)

[ 196](ambiq-apollo4-pinctrl_8h.md#a4554329d3be7f67eb0316ceb84af5b48)#define UART1RX\_P14 APOLLO4\_PINMUX(14, 5)

[ 197](ambiq-apollo4-pinctrl_8h.md#ae18e4a6bc36b1a56c05ba439778e3224)#define CT14\_P14 APOLLO4\_PINMUX(14, 6)

[ 198](ambiq-apollo4-pinctrl_8h.md#a39f9f5d31b34dd21c12439c0a9fd032f)#define NCE14\_P14 APOLLO4\_PINMUX(14, 7)

[ 199](ambiq-apollo4-pinctrl_8h.md#a0ec1384f9acdfedab8ee95078be3abcf)#define OBSBUS14\_P14 APOLLO4\_PINMUX(14, 8)

[ 200](ambiq-apollo4-pinctrl_8h.md#a7df04d3ab899525fdebf3e53fce06aa2)#define I2S0\_SDIN\_P14 APOLLO4\_PINMUX(14, 10)

[ 201](ambiq-apollo4-pinctrl_8h.md#a4e439c4b95e462d3591573c6bd125072)#define FPIO\_P14 APOLLO4\_PINMUX(14, 11)

[ 202](ambiq-apollo4-pinctrl_8h.md#ae54e476273bf80528bb2bc7de597eba6)#define FLLOAD\_ADDR\_P14 APOLLO4\_PINMUX(14, 13)

[ 203](ambiq-apollo4-pinctrl_8h.md#a403bd9e7bb8424f35603e0c0de3b7e0d)#define MDA\_TRSTN\_P14 APOLLO4\_PINMUX(14, 14)

[ 204](ambiq-apollo4-pinctrl_8h.md#af5d8b18ded6665365213c552e28a7018)#define SCANOUT2\_P14 APOLLO4\_PINMUX(14, 15)

[ 205](ambiq-apollo4-pinctrl_8h.md#a5b32fbcf64f253108c32cc00d1c553c6)#define ADCSE4\_P15 APOLLO4\_PINMUX(15, 0)

[ 206](ambiq-apollo4-pinctrl_8h.md#afead554f8da2be61c1046a58a9ee07d1)#define TRIG0\_P15 APOLLO4\_PINMUX(15, 1)

[ 207](ambiq-apollo4-pinctrl_8h.md#a9147a6e2b351214ab5fe7e5d4f6355d7)#define GPIO\_P15 APOLLO4\_PINMUX(15, 3)

[ 208](ambiq-apollo4-pinctrl_8h.md#a3130b9f3d60c2f7c5feb4a8733fcfb3a)#define MILLI\_REC\_DAT\_P15 APOLLO4\_PINMUX(15, 4)

[ 209](ambiq-apollo4-pinctrl_8h.md#a44bf7f5a18f73cae89bd0d2ef28084b1)#define UART3RX\_P15 APOLLO4\_PINMUX(15, 5)

[ 210](ambiq-apollo4-pinctrl_8h.md#a4a8aa656d717bb0ac089fb049bc287aa)#define CT15\_P15 APOLLO4\_PINMUX(15, 6)

[ 211](ambiq-apollo4-pinctrl_8h.md#ab6136185e31fbbb173391d77723de46a)#define NCE15\_P15 APOLLO4\_PINMUX(15, 7)

[ 212](ambiq-apollo4-pinctrl_8h.md#a273a9f2211fdc7cfbf62698dc3c44c80)#define OBSBUS15\_P15 APOLLO4\_PINMUX(15, 8)

[ 213](ambiq-apollo4-pinctrl_8h.md#aa72175aa66e768078f9c9c0a2ea8053f)#define REFCLK\_EXT\_P15 APOLLO4\_PINMUX(15, 10)

[ 214](ambiq-apollo4-pinctrl_8h.md#a50ceceada5739e0c6a9f407e23f282aa)#define FPIO\_P15 APOLLO4\_PINMUX(15, 11)

[ 215](ambiq-apollo4-pinctrl_8h.md#a5801b0865263e375627c387639c9fb01)#define FLLOAD\_DATA\_P15 APOLLO4\_PINMUX(15, 13)

[ 216](ambiq-apollo4-pinctrl_8h.md#aba9b264c669f13d662615d7d1464d948)#define SCANOUT1\_P15 APOLLO4\_PINMUX(15, 15)

[ 217](ambiq-apollo4-pinctrl_8h.md#a18ae21d0fe862b05c6df490a45168581)#define ADCSE3\_P16 APOLLO4\_PINMUX(16, 0)

[ 218](ambiq-apollo4-pinctrl_8h.md#ad6b62ac3ae8822bb6e1783b9e49dc9ba)#define TRIG1\_P16 APOLLO4\_PINMUX(16, 1)

[ 219](ambiq-apollo4-pinctrl_8h.md#ada511f03b31013b0e3ac7a28d7b12008)#define I2S1\_CLK\_P16 APOLLO4\_PINMUX(16, 2)

[ 220](ambiq-apollo4-pinctrl_8h.md#a9c21bf7bc952df6b78d19f89f3638833)#define GPIO\_P16 APOLLO4\_PINMUX(16, 3)

[ 221](ambiq-apollo4-pinctrl_8h.md#a0257a1173b7bd81c15dc0b4cf1130bec)#define MILLI\_PBDATA1\_P16 APOLLO4\_PINMUX(16, 4)

[ 222](ambiq-apollo4-pinctrl_8h.md#a7861db1e000bc1fa296754fcb73475ef)#define UART1RTS\_P16 APOLLO4\_PINMUX(16, 5)

[ 223](ambiq-apollo4-pinctrl_8h.md#ab725f704e28ac66b66fd9117dc14d0d2)#define CT16\_P16 APOLLO4\_PINMUX(16, 6)

[ 224](ambiq-apollo4-pinctrl_8h.md#a5da8200119b0e8a2e6fec1097896edd1)#define NCE16\_P16 APOLLO4\_PINMUX(16, 7)

[ 225](ambiq-apollo4-pinctrl_8h.md#a2cfeac9755d9b17cef91970dab75fdfd)#define OBSBUS0\_P16 APOLLO4\_PINMUX(16, 8)

[ 226](ambiq-apollo4-pinctrl_8h.md#a9c5272a00ee79a2ac1c23217fb9f2874)#define FPIO\_P16 APOLLO4\_PINMUX(16, 11)

[ 227](ambiq-apollo4-pinctrl_8h.md#a7543488d62c7c290d8851e3fbfa14096)#define DFT\_RET\_P16 APOLLO4\_PINMUX(16, 15)

[ 228](ambiq-apollo4-pinctrl_8h.md#aeec6ebbab4daa604f39069d8f4f4c8bd)#define ADCSE2\_P17 APOLLO4\_PINMUX(17, 0)

[ 229](ambiq-apollo4-pinctrl_8h.md#a495d9988e327b4f8442676e25e49d71d)#define TRIG2\_P17 APOLLO4\_PINMUX(17, 1)

[ 230](ambiq-apollo4-pinctrl_8h.md#aed0abc0709d7d5b08345caf0546a3aab)#define I2S1\_DATA\_P17 APOLLO4\_PINMUX(17, 2)

[ 231](ambiq-apollo4-pinctrl_8h.md#a6a5de6dce7def318bec4f73dd614ec22)#define GPIO\_P17 APOLLO4\_PINMUX(17, 3)

[ 232](ambiq-apollo4-pinctrl_8h.md#ab9e30c743edc76eb65c80d39d1f28133)#define MILLI\_PBDATA2\_P17 APOLLO4\_PINMUX(17, 4)

[ 233](ambiq-apollo4-pinctrl_8h.md#a41a420e4f69793906e8bcf143a879d03)#define UART3RTS\_P17 APOLLO4\_PINMUX(17, 5)

[ 234](ambiq-apollo4-pinctrl_8h.md#aaf4dfd1eed7dd77ea6d6639142c7e84f)#define CT17\_P17 APOLLO4\_PINMUX(17, 6)

[ 235](ambiq-apollo4-pinctrl_8h.md#ab89d7eb6aa6e611a3a95cc1ee913731c)#define NCE17\_P17 APOLLO4\_PINMUX(17, 7)

[ 236](ambiq-apollo4-pinctrl_8h.md#aa657ca13684a441999e3d45893037f31)#define OBSBUS1\_P17 APOLLO4\_PINMUX(17, 8)

[ 237](ambiq-apollo4-pinctrl_8h.md#ac1f82e9af4b82e26c36254ba00a9458c)#define I2S1\_SDOUT\_P17 APOLLO4\_PINMUX(17, 9)

[ 238](ambiq-apollo4-pinctrl_8h.md#a76892e7b5359c6ddac5cea94ee854cbd)#define FPIO\_P17 APOLLO4\_PINMUX(17, 11)

[ 239](ambiq-apollo4-pinctrl_8h.md#a5b37bcf9ffa360391441dc5e44c03ef7)#define FLLOAD\_STRB\_P17 APOLLO4\_PINMUX(17, 13)

[ 240](ambiq-apollo4-pinctrl_8h.md#a1d7a76fc0a3c73e16e77b7f5deaf7ee6)#define MDA\_TMS\_P17 APOLLO4\_PINMUX(17, 14)

[ 241](ambiq-apollo4-pinctrl_8h.md#ae51f5bbea7713d91af701162275abef4)#define OPCG\_CLK\_P17 APOLLO4\_PINMUX(17, 15)

[ 242](ambiq-apollo4-pinctrl_8h.md#a8881b3e9c0c3ddf1bb99ad1eb93fbc6d)#define ADCSE1\_P18 APOLLO4\_PINMUX(18, 0)

[ 243](ambiq-apollo4-pinctrl_8h.md#a737f3e858868beb587b9768f55261a92)#define ANATEST2\_P18 APOLLO4\_PINMUX(18, 1)

[ 244](ambiq-apollo4-pinctrl_8h.md#aa27946815e942edc686c9707426ebbd0)#define I2S1\_WS\_P18 APOLLO4\_PINMUX(18, 2)

[ 245](ambiq-apollo4-pinctrl_8h.md#a8b325ebb0010179509a1a32450ea72af)#define GPIO\_P18 APOLLO4\_PINMUX(18, 3)

[ 246](ambiq-apollo4-pinctrl_8h.md#ac4975731863613597aa2d245f4d87627)#define UART0CTS\_P18 APOLLO4\_PINMUX(18, 4)

[ 247](ambiq-apollo4-pinctrl_8h.md#ae4168448d573915c45e2120e7d3579ce)#define UART1CTS\_P18 APOLLO4\_PINMUX(18, 5)

[ 248](ambiq-apollo4-pinctrl_8h.md#a26eeeae474d79a2028359e9a03e1a063)#define CT18\_P18 APOLLO4\_PINMUX(18, 6)

[ 249](ambiq-apollo4-pinctrl_8h.md#a566a450bf9afa441315c83bf4d0ce580)#define NCE18\_P18 APOLLO4\_PINMUX(18, 7)

[ 250](ambiq-apollo4-pinctrl_8h.md#aa7598e1cf4105c96862ff2c9912f5468)#define OBSBUS2\_P18 APOLLO4\_PINMUX(18, 8)

[ 251](ambiq-apollo4-pinctrl_8h.md#a3da1828385f168f65f395c073bf55153)#define FPIO\_P18 APOLLO4\_PINMUX(18, 11)

[ 252](ambiq-apollo4-pinctrl_8h.md#a793c16096bf305da2603b4298b6c066d)#define FLB\_TMS\_P18 APOLLO4\_PINMUX(18, 12)

[ 253](ambiq-apollo4-pinctrl_8h.md#ad750c21f0ab427619f8cfd9b3c79a361)#define FLLOAD\_DATA\_P18 APOLLO4\_PINMUX(18, 13)

[ 254](ambiq-apollo4-pinctrl_8h.md#a5baebe401039d38e10488166e7fa6b34)#define MDA\_HFRC\_EXT\_P18 APOLLO4\_PINMUX(18, 14)

[ 255](ambiq-apollo4-pinctrl_8h.md#a11c8c53d8b3f17143ba4d050d4a13722)#define SCANIN1\_P18 APOLLO4\_PINMUX(18, 15)

[ 256](ambiq-apollo4-pinctrl_8h.md#aa330f5f3b31003e45049beadcd4637fa)#define ADCSE0\_P19 APOLLO4\_PINMUX(19, 0)

[ 257](ambiq-apollo4-pinctrl_8h.md#a4af84142986af9004f682cfb85a65ecf)#define ANATEST1\_P19 APOLLO4\_PINMUX(19, 1)

[ 258](ambiq-apollo4-pinctrl_8h.md#afcadccc574cc0d3c7820ba6b0511612e)#define GPIO\_P19 APOLLO4\_PINMUX(19, 3)

[ 259](ambiq-apollo4-pinctrl_8h.md#a5cc3c23ef8d295ea3a22e3e6e0a9275b)#define UART2CTS\_P19 APOLLO4\_PINMUX(19, 4)

[ 260](ambiq-apollo4-pinctrl_8h.md#a8591dd0c023d6a14db2018f5d71d3c71)#define UART3CTS\_P19 APOLLO4\_PINMUX(19, 5)

[ 261](ambiq-apollo4-pinctrl_8h.md#acd2baace3747e5ff4907e3bcdb33b424)#define CT19\_P19 APOLLO4\_PINMUX(19, 6)

[ 262](ambiq-apollo4-pinctrl_8h.md#af9d50128143543f345b8db2d2e3e0918)#define NCE19\_P19 APOLLO4\_PINMUX(19, 7)

[ 263](ambiq-apollo4-pinctrl_8h.md#ac950a0d57ead9b5a57a76bc68c516d95)#define OBSBUS3\_P19 APOLLO4\_PINMUX(19, 8)

[ 264](ambiq-apollo4-pinctrl_8h.md#a9e6001fe219e3fe85e8410abba114263)#define I2S1\_SDIN\_P19 APOLLO4\_PINMUX(19, 9)

[ 265](ambiq-apollo4-pinctrl_8h.md#a617c07d6fe47dacb27878e8e613b9233)#define FPIO\_P19 APOLLO4\_PINMUX(19, 11)

[ 266](ambiq-apollo4-pinctrl_8h.md#abb3f5cf1dd484760f759750b7ecc1b82)#define FLB\_TRSTN\_P19 APOLLO4\_PINMUX(19, 12)

[ 267](ambiq-apollo4-pinctrl_8h.md#a508b61b433b736e3c345c480f4e6a9a8)#define FLLOAD\_ADDR\_P19 APOLLO4\_PINMUX(19, 13)

[ 268](ambiq-apollo4-pinctrl_8h.md#a9379fc1ebd65b8225d86a616749c5438)#define SCANIN2\_P19 APOLLO4\_PINMUX(19, 15)

[ 269](ambiq-apollo4-pinctrl_8h.md#a3885c97e098dfed018491c67065e696c)#define SWDCK\_P20 APOLLO4\_PINMUX(20, 0)

[ 270](ambiq-apollo4-pinctrl_8h.md#adabe25797cbaba1cc8e04f88619aa9b8)#define TRIG1\_P20 APOLLO4\_PINMUX(20, 1)

[ 271](ambiq-apollo4-pinctrl_8h.md#afcd63445d3ccf972c95c365f95e30039)#define GPIO\_P20 APOLLO4\_PINMUX(20, 3)

[ 272](ambiq-apollo4-pinctrl_8h.md#af9acded122c3567a0f7fae29561351e5)#define UART0TX\_P20 APOLLO4\_PINMUX(20, 4)

[ 273](ambiq-apollo4-pinctrl_8h.md#a8d38e7930ecd6a6b51e0da8bdf0b5792)#define UART1TX\_P20 APOLLO4\_PINMUX(20, 5)

[ 274](ambiq-apollo4-pinctrl_8h.md#ac9b840d765492105d79f293b9d1baeb9)#define CT20\_P20 APOLLO4\_PINMUX(20, 6)

[ 275](ambiq-apollo4-pinctrl_8h.md#a8c4f0230a390d43b9a408ec438b5dbe6)#define NCE20\_P20 APOLLO4\_PINMUX(20, 7)

[ 276](ambiq-apollo4-pinctrl_8h.md#a415b74c3f9d40868278d8378172b1d68)#define OBSBUS4\_P20 APOLLO4\_PINMUX(20, 8)

[ 277](ambiq-apollo4-pinctrl_8h.md#a349761718d2b98f4daeea11870971962)#define FPIO\_P20 APOLLO4\_PINMUX(20, 11)

[ 278](ambiq-apollo4-pinctrl_8h.md#a0fc3559794f6075f464649bf9c9e9f24)#define SCANCLK\_P20 APOLLO4\_PINMUX(20, 15)

[ 279](ambiq-apollo4-pinctrl_8h.md#a184cab7037772c8ca8ecc296ea9c7e48)#define SWDIO\_P21 APOLLO4\_PINMUX(21, 0)

[ 280](ambiq-apollo4-pinctrl_8h.md#a3801d91685f11ef10e205ff52b1ec5e0)#define TRIG2\_P21 APOLLO4\_PINMUX(21, 1)

[ 281](ambiq-apollo4-pinctrl_8h.md#a03d53f3d221401ff02a702ef2c8e05c1)#define GPIO\_P21 APOLLO4\_PINMUX(21, 3)

[ 282](ambiq-apollo4-pinctrl_8h.md#a93d5447c0692131645ef36ecbd222589)#define UART2TX\_P21 APOLLO4\_PINMUX(21, 4)

[ 283](ambiq-apollo4-pinctrl_8h.md#a735d30d710b774c75202cf22f65cb65f)#define UART3TX\_P21 APOLLO4\_PINMUX(21, 5)

[ 284](ambiq-apollo4-pinctrl_8h.md#a52222ccb5238dffa6fc317bb3e0ee18f)#define CT21\_P21 APOLLO4\_PINMUX(21, 6)

[ 285](ambiq-apollo4-pinctrl_8h.md#a3a7292f75cecf7ac798212bbfef2ff3a)#define NCE21\_P21 APOLLO4\_PINMUX(21, 7)

[ 286](ambiq-apollo4-pinctrl_8h.md#aaf9c63c1756f5a2597b4fe3e6a7c8b3d)#define OBSBUS5\_P21 APOLLO4\_PINMUX(21, 8)

[ 287](ambiq-apollo4-pinctrl_8h.md#ad3b74df7b4440b8fb5c3b13b2e18e44d)#define FPIO\_P21 APOLLO4\_PINMUX(21, 11)

[ 288](ambiq-apollo4-pinctrl_8h.md#a40ea137ce49815d434a55da16dee78f5)#define SCANSHFT\_P21 APOLLO4\_PINMUX(21, 15)

[ 289](ambiq-apollo4-pinctrl_8h.md#a9f7222ad820edf97ba6edfe102b85f1a)#define M7SCL\_P22 APOLLO4\_PINMUX(22, 0)

[ 290](ambiq-apollo4-pinctrl_8h.md#a1dd58bf7a7bca6fffdc549992292f566)#define M7SCK\_P22 APOLLO4\_PINMUX(22, 1)

[ 291](ambiq-apollo4-pinctrl_8h.md#af2e7742c9a96fe5ac1a2de402bd5f72f)#define SWO\_P22 APOLLO4\_PINMUX(22, 2)

[ 292](ambiq-apollo4-pinctrl_8h.md#ad0b28de3a514755dfa6b00fe82579f3d)#define GPIO\_P22 APOLLO4\_PINMUX(22, 3)

[ 293](ambiq-apollo4-pinctrl_8h.md#a220b191299c8662f9f0c7ea17a73b0dc)#define UART0RX\_P22 APOLLO4\_PINMUX(22, 4)

[ 294](ambiq-apollo4-pinctrl_8h.md#a2d7c4d976c4d1cfbb59313b05d5d2f06)#define UART1RX\_P22 APOLLO4\_PINMUX(22, 5)

[ 295](ambiq-apollo4-pinctrl_8h.md#ab063d6d6d1817a68f0f9c593ac53e04c)#define CT22\_P22 APOLLO4\_PINMUX(22, 6)

[ 296](ambiq-apollo4-pinctrl_8h.md#a775bbd5124031418e8f5b723e99ac9ab)#define NCE22\_P22 APOLLO4\_PINMUX(22, 7)

[ 297](ambiq-apollo4-pinctrl_8h.md#a857869244419f625e694edf76ac8256e)#define OBSBUS6\_P22 APOLLO4\_PINMUX(22, 8)

[ 298](ambiq-apollo4-pinctrl_8h.md#a111f3f328e433b185b9dae30cb8256e5)#define VCMPO\_P22 APOLLO4\_PINMUX(22, 9)

[ 299](ambiq-apollo4-pinctrl_8h.md#a4dea5dc675840bb09bb55bfad7b49bea)#define I3CM1\_SCL\_P22 APOLLO4\_PINMUX(22, 10)

[ 300](ambiq-apollo4-pinctrl_8h.md#a14f08399d9c0d455f4f7148311116fd8)#define FPIO\_P22 APOLLO4\_PINMUX(22, 11)

[ 301](ambiq-apollo4-pinctrl_8h.md#aa9d30f461fe84a18f5c432e91968c524)#define SCANIN3\_P22 APOLLO4\_PINMUX(22, 15)

[ 302](ambiq-apollo4-pinctrl_8h.md#ac2555f6261815706ecbf7e97d6597409)#define M7SDAWIR3\_P23 APOLLO4\_PINMUX(23, 0)

[ 303](ambiq-apollo4-pinctrl_8h.md#a5df9e6c9066ccd77e4d9171c476b1590)#define M7MOSI\_P23 APOLLO4\_PINMUX(23, 1)

[ 304](ambiq-apollo4-pinctrl_8h.md#a6bd1299c3e642adf36a224981aad26ec)#define SWO\_P23 APOLLO4\_PINMUX(23, 2)

[ 305](ambiq-apollo4-pinctrl_8h.md#a8742762c7c46596977c17898e55f7df0)#define GPIO\_P23 APOLLO4\_PINMUX(23, 3)

[ 306](ambiq-apollo4-pinctrl_8h.md#acaf148e1c231f89b0dde8dd42768be19)#define UART2RX\_P23 APOLLO4\_PINMUX(23, 4)

[ 307](ambiq-apollo4-pinctrl_8h.md#a5c1cffa70e7c7512bdff57c3453c958a)#define UART3RX\_P23 APOLLO4\_PINMUX(23, 5)

[ 308](ambiq-apollo4-pinctrl_8h.md#a02a0ee207d24a97a11717850378d910d)#define CT23\_P23 APOLLO4\_PINMUX(23, 6)

[ 309](ambiq-apollo4-pinctrl_8h.md#a0a52f7e779022ce90fe4d7ce7b200f6d)#define NCE23\_P23 APOLLO4\_PINMUX(23, 7)

[ 310](ambiq-apollo4-pinctrl_8h.md#a6719ff7f6b60aa733a7250c1e53cf46f)#define OBSBUS7\_P23 APOLLO4\_PINMUX(23, 8)

[ 311](ambiq-apollo4-pinctrl_8h.md#af329d82835e17e9ffe85e05cdbd54699)#define VCMPO\_P23 APOLLO4\_PINMUX(23, 9)

[ 312](ambiq-apollo4-pinctrl_8h.md#a5be66878d9a9e5b200c1e0fec15cf8c7)#define I3CM1\_SDA\_P23 APOLLO4\_PINMUX(23, 10)

[ 313](ambiq-apollo4-pinctrl_8h.md#a01d19c0e2ee859756d57974be6e81821)#define FPIO\_P23 APOLLO4\_PINMUX(23, 11)

[ 314](ambiq-apollo4-pinctrl_8h.md#a1d8dfee4c9c388a04609d93f92860d3d)#define SCANOUT6\_P23 APOLLO4\_PINMUX(23, 15)

[ 315](ambiq-apollo4-pinctrl_8h.md#a5b06b54b195f48e66ba5596ecb9397da)#define M7MISO\_P24 APOLLO4\_PINMUX(24, 0)

[ 316](ambiq-apollo4-pinctrl_8h.md#a27973580413dbaff1e8f6ca6a42fadbf)#define TRIG3\_P24 APOLLO4\_PINMUX(24, 1)

[ 317](ambiq-apollo4-pinctrl_8h.md#acc4f37955d3cc5567dddb283275cd791)#define SWO\_P24 APOLLO4\_PINMUX(24, 2)

[ 318](ambiq-apollo4-pinctrl_8h.md#a38b0fad90fac621ae3056e0890e5db18)#define GPIO\_P24 APOLLO4\_PINMUX(24, 3)

[ 319](ambiq-apollo4-pinctrl_8h.md#a1aa1afa7840b2205afd9404a784af4e6)#define UART0RTS\_P24 APOLLO4\_PINMUX(24, 4)

[ 320](ambiq-apollo4-pinctrl_8h.md#a03a4f0e4edb98dda263612cc17d48b4e)#define UART1RTS\_P24 APOLLO4\_PINMUX(24, 5)

[ 321](ambiq-apollo4-pinctrl_8h.md#a772e63738b3767e4b07ce2ca94c0b167)#define CT24\_P24 APOLLO4\_PINMUX(24, 6)

[ 322](ambiq-apollo4-pinctrl_8h.md#aef5c8fe782ba1f615e0ea35d44a942ce)#define NCE24\_P24 APOLLO4\_PINMUX(24, 7)

[ 323](ambiq-apollo4-pinctrl_8h.md#aa5288e590178498d56e2993e86809a87)#define OBSBUS8\_P24 APOLLO4\_PINMUX(24, 8)

[ 324](ambiq-apollo4-pinctrl_8h.md#ac364dbd0374a9c2ad54933e116dc25e3)#define FPIO\_P24 APOLLO4\_PINMUX(24, 11)

[ 325](ambiq-apollo4-pinctrl_8h.md#a25eb12f208b82b2c46a13b32a27ce142)#define SCANOUT7\_P24 APOLLO4\_PINMUX(24, 15)

[ 326](ambiq-apollo4-pinctrl_8h.md#a0f03c5c7c19343ea614c42032ef30dcd)#define M2SCL\_P25 APOLLO4\_PINMUX(25, 0)

[ 327](ambiq-apollo4-pinctrl_8h.md#a1e2d1b94cf32aee7e6f37fc4868d2605)#define M2SCK\_P25 APOLLO4\_PINMUX(25, 1)

[ 328](ambiq-apollo4-pinctrl_8h.md#a70eeb3da2737dc1f88ef0d6b033ba31b)#define GPIO\_P25 APOLLO4\_PINMUX(25, 3)

[ 329](ambiq-apollo4-pinctrl_8h.md#ab9c306d7b877bb6f7092fe68d3e18069)#define LFRC\_EXT\_P25 APOLLO4\_PINMUX(25, 4)

[ 330](ambiq-apollo4-pinctrl_8h.md#ad99d366fc2fba6965a2b4bb2fbbe1387)#define DSP\_TMS\_P25 APOLLO4\_PINMUX(25, 5)

[ 331](ambiq-apollo4-pinctrl_8h.md#a2b3c7a7f7e43cf8998b1c1b4ec07fa6e)#define CT25\_P25 APOLLO4\_PINMUX(25, 6)

[ 332](ambiq-apollo4-pinctrl_8h.md#a6c08788db3454db63bc8e5bca88b61a1)#define NCE25\_P25 APOLLO4\_PINMUX(25, 7)

[ 333](ambiq-apollo4-pinctrl_8h.md#af463b723028bac12dd7e259e5e59ae07)#define OBSBUS9\_P25 APOLLO4\_PINMUX(25, 8)

[ 334](ambiq-apollo4-pinctrl_8h.md#a6b82fb9c8326c269ee20a6dfe817afae)#define FPIO\_P25 APOLLO4\_PINMUX(25, 11)

[ 335](ambiq-apollo4-pinctrl_8h.md#a6f9b49f0935bfeb0967abc274cd5347a)#define SCANIN8\_P25 APOLLO4\_PINMUX(25, 15)

[ 336](ambiq-apollo4-pinctrl_8h.md#a7e9ed67deb828c83cbf374049cf7f625)#define M2SDAWIR3\_P26 APOLLO4\_PINMUX(26, 0)

[ 337](ambiq-apollo4-pinctrl_8h.md#a300e18bdb724fa67e13efff769b3cec9)#define M2MOSI\_P26 APOLLO4\_PINMUX(26, 1)

[ 338](ambiq-apollo4-pinctrl_8h.md#a70cc23730a6021ba52d4b46466bf7ec8)#define GPIO\_P26 APOLLO4\_PINMUX(26, 3)

[ 339](ambiq-apollo4-pinctrl_8h.md#a22151075c9c0c0d69cc8141839f1a310)#define HFRC\_EXT\_P26 APOLLO4\_PINMUX(26, 4)

[ 340](ambiq-apollo4-pinctrl_8h.md#a28f46cd447d18f9742979531252a0e69)#define CT26\_P26 APOLLO4\_PINMUX(26, 6)

[ 341](ambiq-apollo4-pinctrl_8h.md#a498a5dcaa37b5a972e8eea27c29617ef)#define NCE26\_P26 APOLLO4\_PINMUX(26, 7)

[ 342](ambiq-apollo4-pinctrl_8h.md#a8e9e7fc1ba07004d0915b300e2cf8efb)#define OBSBUS10\_P26 APOLLO4\_PINMUX(26, 8)

[ 343](ambiq-apollo4-pinctrl_8h.md#a28e401ddafb5476b147d6407270dbdb7)#define VCMPO\_P26 APOLLO4\_PINMUX(26, 9)

[ 344](ambiq-apollo4-pinctrl_8h.md#a99fc669fe4fffd12615bb4cabec7c305)#define FPIO\_P26 APOLLO4\_PINMUX(26, 11)

[ 345](ambiq-apollo4-pinctrl_8h.md#afd284dcd8de7c10f112066b4c4719655)#define SCANIN9\_P26 APOLLO4\_PINMUX(26, 15)

[ 346](ambiq-apollo4-pinctrl_8h.md#a5f1701b46129777873b5790a9dbd395a)#define M2MISO\_P27 APOLLO4\_PINMUX(27, 0)

[ 347](ambiq-apollo4-pinctrl_8h.md#a64715c628085a4776bca079710373d68)#define TRIG0\_P27 APOLLO4\_PINMUX(27, 1)

[ 348](ambiq-apollo4-pinctrl_8h.md#a9e3eb9ba4f0604f735fc0da2298dc150)#define GPIO\_P27 APOLLO4\_PINMUX(27, 3)

[ 349](ambiq-apollo4-pinctrl_8h.md#a5acb2c796482e9b513ef217e23a18242)#define XT\_EXT\_P27 APOLLO4\_PINMUX(27, 4)

[ 350](ambiq-apollo4-pinctrl_8h.md#ac0bcd00f8f7d1f045f8206d6824f403d)#define DSP\_TCK\_P27 APOLLO4\_PINMUX(27, 5)

[ 351](ambiq-apollo4-pinctrl_8h.md#af8bc20240ac3dcce77516860e025391a)#define CT27\_P27 APOLLO4\_PINMUX(27, 6)

[ 352](ambiq-apollo4-pinctrl_8h.md#a4b0b9c08da925a4a55bf9cd8342e275d)#define NCE27\_P27 APOLLO4\_PINMUX(27, 7)

[ 353](ambiq-apollo4-pinctrl_8h.md#a5e3d8cb5fdd767c4657ab628a930a547)#define OBSBUS11\_P27 APOLLO4\_PINMUX(27, 8)

[ 354](ambiq-apollo4-pinctrl_8h.md#a32e5913e70bef085a1bbcd49de4be39d)#define I2S0\_SDIN\_P27 APOLLO4\_PINMUX(27, 9)

[ 355](ambiq-apollo4-pinctrl_8h.md#a1dcc0fbd0c4ebf62e66ec8f3a139617d)#define FPIO\_P27 APOLLO4\_PINMUX(27, 11)

[ 356](ambiq-apollo4-pinctrl_8h.md#a48818b20cf48582e3b4279c4c490a126)#define SCANIN10\_P27 APOLLO4\_PINMUX(27, 15)

[ 357](ambiq-apollo4-pinctrl_8h.md#a88c3bdc960cd3a0b6aafe272d99ef86a)#define SWO\_P28 APOLLO4\_PINMUX(28, 0)

[ 358](ambiq-apollo4-pinctrl_8h.md#a019a0aefc6fc837b16f6b1065a4e430f)#define VCMPO\_P28 APOLLO4\_PINMUX(28, 1)

[ 359](ambiq-apollo4-pinctrl_8h.md#ae9bb20099b56598de34285c27c2e33a1)#define I2S0\_CLK\_P28 APOLLO4\_PINMUX(28, 2)

[ 360](ambiq-apollo4-pinctrl_8h.md#a6f6f8847e0069b5fefc4a6a54851c99b)#define GPIO\_P28 APOLLO4\_PINMUX(28, 3)

[ 361](ambiq-apollo4-pinctrl_8h.md#a2e1798c2a471fef301e6bede3506f9c6)#define UART2CTS\_P28 APOLLO4\_PINMUX(28, 4)

[ 362](ambiq-apollo4-pinctrl_8h.md#ae556da3d99b894e8eb26cdf95405358f)#define DSP\_TDO\_P28 APOLLO4\_PINMUX(28, 5)

[ 363](ambiq-apollo4-pinctrl_8h.md#a66ee141fcbbcacf659ca7f0b730234a2)#define CT28\_P28 APOLLO4\_PINMUX(28, 6)

[ 364](ambiq-apollo4-pinctrl_8h.md#ac975e39671e4884de16995b831c3bc52)#define NCE28\_P28 APOLLO4\_PINMUX(28, 7)

[ 365](ambiq-apollo4-pinctrl_8h.md#ab82b48ad1825299308445886b56ed22b)#define OBSBUS12\_P28 APOLLO4\_PINMUX(28, 8)

[ 366](ambiq-apollo4-pinctrl_8h.md#a02655dd3f016528765d618d31c3eea6e)#define FPIO\_P28 APOLLO4\_PINMUX(28, 11)

[ 367](ambiq-apollo4-pinctrl_8h.md#aac22e6c2cec877d3aa1c9aa3f45e79e0)#define CME\_P28 APOLLO4\_PINMUX(28, 15)

[ 368](ambiq-apollo4-pinctrl_8h.md#a3b19a49c2f1a46569aa9e47fc56c46bc)#define TRIG0\_P29 APOLLO4\_PINMUX(29, 0)

[ 369](ambiq-apollo4-pinctrl_8h.md#a671f7038ce6c70083ec9d090c0ac350c)#define VCMPO\_P29 APOLLO4\_PINMUX(29, 1)

[ 370](ambiq-apollo4-pinctrl_8h.md#a23bf0a86006e1feb34684f7c026affd2)#define I2S0\_DATA\_P29 APOLLO4\_PINMUX(29, 2)

[ 371](ambiq-apollo4-pinctrl_8h.md#a0c8d4306be59368e181736d98c9d6b4b)#define GPIO\_P29 APOLLO4\_PINMUX(29, 3)

[ 372](ambiq-apollo4-pinctrl_8h.md#a2c3ff90c1c45bad588a4504eb8dc6e19)#define UART1CTS\_P29 APOLLO4\_PINMUX(29, 4)

[ 373](ambiq-apollo4-pinctrl_8h.md#a7d58e7d0ce35193a8fdeda4b4e9fd65f)#define DSP\_TRSTN\_P29 APOLLO4\_PINMUX(29, 5)

[ 374](ambiq-apollo4-pinctrl_8h.md#a43465522bf8ba8453e4d2c48740e33c7)#define CT29\_P29 APOLLO4\_PINMUX(29, 6)

[ 375](ambiq-apollo4-pinctrl_8h.md#ac7c4f18c7b072968ce9048bb9057356c)#define NCE29\_P29 APOLLO4\_PINMUX(29, 7)

[ 376](ambiq-apollo4-pinctrl_8h.md#a5f8ef644d94563044872bab54bd59e62)#define OBSBUS13\_P29 APOLLO4\_PINMUX(29, 8)

[ 377](ambiq-apollo4-pinctrl_8h.md#ade86b9ab2563145341a593e7e23da0d5)#define I2S0\_SDOUT\_P29 APOLLO4\_PINMUX(29, 9)

[ 378](ambiq-apollo4-pinctrl_8h.md#ac6084cb9acc8f3a3e16e261740adf48c)#define FPIO\_P29 APOLLO4\_PINMUX(29, 11)

[ 379](ambiq-apollo4-pinctrl_8h.md#a27e4bef1ce2a4a408b1fd4ecd2d1f58c)#define CMLE\_P29 APOLLO4\_PINMUX(29, 15)

[ 380](ambiq-apollo4-pinctrl_8h.md#a798d48fe7ba86dea06f9e70210a91dd0)#define TRIG1\_P30 APOLLO4\_PINMUX(30, 0)

[ 381](ambiq-apollo4-pinctrl_8h.md#a520ad3a45e554a5ababd0d35a5e040a1)#define VCMPO\_P30 APOLLO4\_PINMUX(30, 1)

[ 382](ambiq-apollo4-pinctrl_8h.md#ae789d1776efe058e8dd1580545315ad1)#define I2S0\_WS\_P30 APOLLO4\_PINMUX(30, 2)

[ 383](ambiq-apollo4-pinctrl_8h.md#a96753b0a1e5a99e644c3bf21aee043b9)#define GPIO\_P30 APOLLO4\_PINMUX(30, 3)

[ 384](ambiq-apollo4-pinctrl_8h.md#aa507368219464308827240872d0eab11)#define UART0TX\_P30 APOLLO4\_PINMUX(30, 4)

[ 385](ambiq-apollo4-pinctrl_8h.md#ac6aeda0b949e42e0148850e45a7dc06f)#define DSP\_TDI\_P30 APOLLO4\_PINMUX(30, 5)

[ 386](ambiq-apollo4-pinctrl_8h.md#a1da181a52688c0441577a555529efb1b)#define CT30\_P30 APOLLO4\_PINMUX(30, 6)

[ 387](ambiq-apollo4-pinctrl_8h.md#a6d9a17fecc9e2687ede485e719c5e616)#define NCE30\_P30 APOLLO4\_PINMUX(30, 7)

[ 388](ambiq-apollo4-pinctrl_8h.md#a8c8d8d8d590462604d81a8eda4714dcd)#define OBSBUS14\_P30 APOLLO4\_PINMUX(30, 8)

[ 389](ambiq-apollo4-pinctrl_8h.md#a7da4abc9b97fd6536a65f92e71ebcf40)#define FPIO\_P30 APOLLO4\_PINMUX(30, 11)

[ 390](ambiq-apollo4-pinctrl_8h.md#a5102811c15a97da72a3de2e48510e884)#define SCANOUT8\_P30 APOLLO4\_PINMUX(30, 15)

[ 391](ambiq-apollo4-pinctrl_8h.md#a79364687d6b38e1f45a94cd890ceb0d0)#define M3SCL\_P31 APOLLO4\_PINMUX(31, 0)

[ 392](ambiq-apollo4-pinctrl_8h.md#a1297e36013743045181ffcea6a49f3ce)#define M3SCK\_P31 APOLLO4\_PINMUX(31, 1)

[ 393](ambiq-apollo4-pinctrl_8h.md#a2d700f518a2e57f3741c50e0403c471a)#define GPIO\_P31 APOLLO4\_PINMUX(31, 3)

[ 394](ambiq-apollo4-pinctrl_8h.md#a82139a51b8e6d3702ee0cf8108d503de)#define UART2TX\_P31 APOLLO4\_PINMUX(31, 4)

[ 395](ambiq-apollo4-pinctrl_8h.md#ac22aba27ebc97b7f6a46ac7342f3a13f)#define CT31\_P31 APOLLO4\_PINMUX(31, 6)

[ 396](ambiq-apollo4-pinctrl_8h.md#aa1001078fb5a05925a8b02e6ecca70c5)#define NCE31\_P31 APOLLO4\_PINMUX(31, 7)

[ 397](ambiq-apollo4-pinctrl_8h.md#a12bb593d871fdcd8ca681fb14c0dae08)#define OBSBUS15\_P31 APOLLO4\_PINMUX(31, 8)

[ 398](ambiq-apollo4-pinctrl_8h.md#ab11c6316bb1fda43f3bb74e458b49fbe)#define VCMPO\_P31 APOLLO4\_PINMUX(31, 9)

[ 399](ambiq-apollo4-pinctrl_8h.md#a232a4d274cb24993ef018d17458c05de)#define FPIO\_P31 APOLLO4\_PINMUX(31, 11)

[ 400](ambiq-apollo4-pinctrl_8h.md#acf72867d3e37e0fe59f90ea9d494ff27)#define SCANOUT9\_P31 APOLLO4\_PINMUX(31, 15)

[ 401](ambiq-apollo4-pinctrl_8h.md#a5c3779cac6842e7e4c6f47d84c715c50)#define M3SDAWIR3\_P32 APOLLO4\_PINMUX(32, 0)

[ 402](ambiq-apollo4-pinctrl_8h.md#a32bf3ef77a53de7b95d46bef0bfcb9ca)#define M3MOSI\_P32 APOLLO4\_PINMUX(32, 1)

[ 403](ambiq-apollo4-pinctrl_8h.md#a2a97e46858bf930945c2e03effcc035e)#define GPIO\_P32 APOLLO4\_PINMUX(32, 3)

[ 404](ambiq-apollo4-pinctrl_8h.md#a10e604606b02d173fa3706c340768e9a)#define UART0RX\_P32 APOLLO4\_PINMUX(32, 4)

[ 405](ambiq-apollo4-pinctrl_8h.md#a310ac1b99ab7056e1e9666ff1f50bc0c)#define CT32\_P32 APOLLO4\_PINMUX(32, 6)

[ 406](ambiq-apollo4-pinctrl_8h.md#afb0f804646a6e3557dd4341eb7d72a74)#define NCE32\_P32 APOLLO4\_PINMUX(32, 7)

[ 407](ambiq-apollo4-pinctrl_8h.md#ad28d4591e51ea1cdff065c03bfefcc3c)#define OBSBUS0\_P32 APOLLO4\_PINMUX(32, 8)

[ 408](ambiq-apollo4-pinctrl_8h.md#a0f08f8ad94bd78261fb1e9a6f8776b94)#define FPIO\_P32 APOLLO4\_PINMUX(32, 11)

[ 409](ambiq-apollo4-pinctrl_8h.md#af0e4303e8478039aa98b52f48898e70b)#define SCANOUT10\_P32 APOLLO4\_PINMUX(32, 15)

[ 410](ambiq-apollo4-pinctrl_8h.md#ac814b246165e0db7c1525778d2aa8ef2)#define M3MISO\_P33 APOLLO4\_PINMUX(33, 0)

[ 411](ambiq-apollo4-pinctrl_8h.md#aa6c930d3ebb724b9c95ad85943ce744f)#define CLKOUT\_P33 APOLLO4\_PINMUX(33, 1)

[ 412](ambiq-apollo4-pinctrl_8h.md#aa9c2e434db6bed47b117a0764e28889e)#define GPIO\_P33 APOLLO4\_PINMUX(33, 3)

[ 413](ambiq-apollo4-pinctrl_8h.md#a493e5698d9b312cdcfc16f26ce242f1c)#define UART2RX\_P33 APOLLO4\_PINMUX(33, 4)

[ 414](ambiq-apollo4-pinctrl_8h.md#aabedb9dfb8a70deb7667d64244a31549)#define CT33\_P33 APOLLO4\_PINMUX(33, 6)

[ 415](ambiq-apollo4-pinctrl_8h.md#aa91f920fb637bf393393bac80a9e49ba)#define NCE33\_P33 APOLLO4\_PINMUX(33, 7)

[ 416](ambiq-apollo4-pinctrl_8h.md#a7b23495cdc7569782a6bcea9b05d1b1f)#define OBSBUS1\_P33 APOLLO4\_PINMUX(33, 8)

[ 417](ambiq-apollo4-pinctrl_8h.md#adde35e42662a003e4236f867cab0d070)#define DISP\_TE\_P33 APOLLO4\_PINMUX(33, 9)

[ 418](ambiq-apollo4-pinctrl_8h.md#aa9063128367d3c72e4bdc77604ffa6b9)#define FPIO\_P33 APOLLO4\_PINMUX(33, 11)

[ 419](ambiq-apollo4-pinctrl_8h.md#ae0bac3eab7966981b3ca27cfa689feaa)#define SCANOUT11\_P33 APOLLO4\_PINMUX(33, 15)

[ 420](ambiq-apollo4-pinctrl_8h.md#a59acbd2efc1286dd2d65c0895a8040bf)#define M4SCL\_P34 APOLLO4\_PINMUX(34, 0)

[ 421](ambiq-apollo4-pinctrl_8h.md#ae475a8b47c089cd345d2d9425a607e26)#define M4SCK\_P34 APOLLO4\_PINMUX(34, 1)

[ 422](ambiq-apollo4-pinctrl_8h.md#ab0b9fd05273a89341894eaf25602daf9)#define SWO\_P34 APOLLO4\_PINMUX(34, 2)

[ 423](ambiq-apollo4-pinctrl_8h.md#a0b5e8a841aa9e129351ec258cd5849f2)#define GPIO\_P34 APOLLO4\_PINMUX(34, 3)

[ 424](ambiq-apollo4-pinctrl_8h.md#a66f20e3d139190966f84abf4881772bf)#define UART0TX\_P34 APOLLO4\_PINMUX(34, 4)

[ 425](ambiq-apollo4-pinctrl_8h.md#a107d787f5a9ebb73e0f4dfa2798bf02a)#define CT34\_P34 APOLLO4\_PINMUX(34, 6)

[ 426](ambiq-apollo4-pinctrl_8h.md#a4f042898a506cccce60699375b16bf85)#define NCE34\_P34 APOLLO4\_PINMUX(34, 7)

[ 427](ambiq-apollo4-pinctrl_8h.md#a0255f59820660cfbf6b00e0d72ec4de0)#define OBSBUS2\_P34 APOLLO4\_PINMUX(34, 8)

[ 428](ambiq-apollo4-pinctrl_8h.md#a176c774836a2534c644c9f9c9a1237e2)#define VCMPO\_P34 APOLLO4\_PINMUX(34, 9)

[ 429](ambiq-apollo4-pinctrl_8h.md#aa6c5ebd8542897dfc6c7cb2c653e1b1e)#define FPIO\_P34 APOLLO4\_PINMUX(34, 11)

[ 430](ambiq-apollo4-pinctrl_8h.md#af93b127a02208bc90ede05855b2db8ae)#define M4SDAWIR3\_P35 APOLLO4\_PINMUX(35, 0)

[ 431](ambiq-apollo4-pinctrl_8h.md#af826efe82f56280cff971e05bf95daa9)#define M4MOSI\_P35 APOLLO4\_PINMUX(35, 1)

[ 432](ambiq-apollo4-pinctrl_8h.md#a761100bc7b4be900b65bd26e530a6615)#define SWO\_P35 APOLLO4\_PINMUX(35, 2)

[ 433](ambiq-apollo4-pinctrl_8h.md#a26e70a3f976c854799b2451f085ca761)#define GPIO\_P35 APOLLO4\_PINMUX(35, 3)

[ 434](ambiq-apollo4-pinctrl_8h.md#a7b3f2cd7a89d7d941d7506512d773c22)#define UART2TX\_P35 APOLLO4\_PINMUX(35, 4)

[ 435](ambiq-apollo4-pinctrl_8h.md#aceea37cfd2a7f1492f1ef771112bd9d4)#define UART3TX\_P35 APOLLO4\_PINMUX(35, 5)

[ 436](ambiq-apollo4-pinctrl_8h.md#aa2a14fa3ee7447b394c246991a8426b7)#define CT35\_P35 APOLLO4\_PINMUX(35, 6)

[ 437](ambiq-apollo4-pinctrl_8h.md#ad2cdd6497fb562ea4738beb637e044d1)#define NCE35\_P35 APOLLO4\_PINMUX(35, 7)

[ 438](ambiq-apollo4-pinctrl_8h.md#a4f7fbc744f7889cee7bef1b38f4d070e)#define OBSBUS3\_P35 APOLLO4\_PINMUX(35, 8)

[ 439](ambiq-apollo4-pinctrl_8h.md#abf1ef5958d413bc7fe7749164f48a756)#define VCMPO\_P35 APOLLO4\_PINMUX(35, 9)

[ 440](ambiq-apollo4-pinctrl_8h.md#a14513e0e8cdf59a2c0934bc624b8ff67)#define FPIO\_P35 APOLLO4\_PINMUX(35, 11)

[ 441](ambiq-apollo4-pinctrl_8h.md#ac18778ef23d78b19fa9ca94e7138c4b9)#define M4MISO\_P36 APOLLO4\_PINMUX(36, 0)

[ 442](ambiq-apollo4-pinctrl_8h.md#a3fded6796e26433817783887ff53b684)#define TRIG0\_P36 APOLLO4\_PINMUX(36, 1)

[ 443](ambiq-apollo4-pinctrl_8h.md#a863af372de1beecabf79e66d16ff1167)#define SWO\_P36 APOLLO4\_PINMUX(36, 2)

[ 444](ambiq-apollo4-pinctrl_8h.md#a3050173d1ff33494b4b047fd11aff68d)#define GPIO\_P36 APOLLO4\_PINMUX(36, 3)

[ 445](ambiq-apollo4-pinctrl_8h.md#a83d321c741de265c2f5e9c28c68a2b09)#define UART0RX\_P36 APOLLO4\_PINMUX(36, 4)

[ 446](ambiq-apollo4-pinctrl_8h.md#abe283e2a79b535f5afb8c82ebba32fce)#define UART1RX\_P36 APOLLO4\_PINMUX(36, 5)

[ 447](ambiq-apollo4-pinctrl_8h.md#a9e7574ba271fb020107f84bc1f447fcf)#define CT36\_P36 APOLLO4\_PINMUX(36, 6)

[ 448](ambiq-apollo4-pinctrl_8h.md#aae112b0ebd7c6f448b1ce24b772910a4)#define NCE36\_P36 APOLLO4\_PINMUX(36, 7)

[ 449](ambiq-apollo4-pinctrl_8h.md#a50acd2c92cccad4cee9ddb3638632bc9)#define OBSBUS4\_P36 APOLLO4\_PINMUX(36, 8)

[ 450](ambiq-apollo4-pinctrl_8h.md#a767bf3c415edf27ddb69504b468e105b)#define FPIO\_P36 APOLLO4\_PINMUX(36, 11)

[ 451](ambiq-apollo4-pinctrl_8h.md#af9d223615c633da3011b98e102826f75)#define MSPI1\_0\_P37 APOLLO4\_PINMUX(37, 0)

[ 452](ambiq-apollo4-pinctrl_8h.md#a50c552c7588ad8f3c70de98bfce31268)#define TRIG1\_P37 APOLLO4\_PINMUX(37, 1)

[ 453](ambiq-apollo4-pinctrl_8h.md#a1e80ca77d6b1b6474a8a8995ba882dff)#define XT32KHZ\_P37 APOLLO4\_PINMUX(37, 2)

[ 454](ambiq-apollo4-pinctrl_8h.md#a5895dbfee43e62831294b162bde44b9e)#define GPIO\_P37 APOLLO4\_PINMUX(37, 3)

[ 455](ambiq-apollo4-pinctrl_8h.md#a9860e9632664d8bb08dbfcfc3ec99088)#define UART2RX\_P37 APOLLO4\_PINMUX(37, 4)

[ 456](ambiq-apollo4-pinctrl_8h.md#aa73115e9ca9840c3b6133665e0e1bced)#define DISP\_D15\_P37 APOLLO4\_PINMUX(37, 5)

[ 457](ambiq-apollo4-pinctrl_8h.md#a9c970979a0e36d1271a49247099645db)#define CT37\_P37 APOLLO4\_PINMUX(37, 6)

[ 458](ambiq-apollo4-pinctrl_8h.md#a736adccb71d5a32e0519cbd8c89d6b77)#define NCE37\_P37 APOLLO4\_PINMUX(37, 7)

[ 459](ambiq-apollo4-pinctrl_8h.md#ac5ea679002c650a430ee4657e4196d9b)#define OBSBUS5\_P37 APOLLO4\_PINMUX(37, 8)

[ 460](ambiq-apollo4-pinctrl_8h.md#ae8d451b5faa3f40d0a30f8e3e9e9f12c)#define FPIO\_P37 APOLLO4\_PINMUX(37, 11)

[ 461](ambiq-apollo4-pinctrl_8h.md#af0bd0a947cea2c08ab04b7b392017199)#define MSPI1\_1\_P38 APOLLO4\_PINMUX(38, 0)

[ 462](ambiq-apollo4-pinctrl_8h.md#a38d67bfea223103f0bef9f8f054a334f)#define TRIG2\_P38 APOLLO4\_PINMUX(38, 1)

[ 463](ambiq-apollo4-pinctrl_8h.md#a39d6c36f186cab59c810bfe998cf7bee)#define SWTRACECLK\_P38 APOLLO4\_PINMUX(38, 2)

[ 464](ambiq-apollo4-pinctrl_8h.md#a8786cdf36cc244ccb754406e7091dc31)#define GPIO\_P38 APOLLO4\_PINMUX(38, 3)

[ 465](ambiq-apollo4-pinctrl_8h.md#a53a05ce5dd219bd65695276981a7a65b)#define UART0RTS\_P38 APOLLO4\_PINMUX(38, 4)

[ 466](ambiq-apollo4-pinctrl_8h.md#af892301f94d2b9436399612e7ed92cd4)#define DISP\_D16\_P38 APOLLO4\_PINMUX(38, 5)

[ 467](ambiq-apollo4-pinctrl_8h.md#a46132a07b6ecc49da9bb3eb8aa2961d1)#define CT38\_P38 APOLLO4\_PINMUX(38, 6)

[ 468](ambiq-apollo4-pinctrl_8h.md#a7eb51c6fb1bdaabcd854928f0fc53365)#define NCE38\_P38 APOLLO4\_PINMUX(38, 7)

[ 469](ambiq-apollo4-pinctrl_8h.md#ad9f471a7abe120a40c875d1d9c6f258e)#define OBSBUS6\_P38 APOLLO4\_PINMUX(38, 8)

[ 470](ambiq-apollo4-pinctrl_8h.md#acdf9ddc7aad4a3480b94c9750f76e95a)#define FPIO\_P38 APOLLO4\_PINMUX(38, 11)

[ 471](ambiq-apollo4-pinctrl_8h.md#a8a6ef9ae62f2a75e1da40583458ee62a)#define MSPI1\_2\_P39 APOLLO4\_PINMUX(39, 0)

[ 472](ambiq-apollo4-pinctrl_8h.md#ac552738f2fda8a5570ceb3d68eec6ee8)#define TRIG3\_P39 APOLLO4\_PINMUX(39, 1)

[ 473](ambiq-apollo4-pinctrl_8h.md#a13473a9eadb60e1d2caa18c168652cf5)#define SWTRACE0\_P39 APOLLO4\_PINMUX(39, 2)

[ 474](ambiq-apollo4-pinctrl_8h.md#a5a4c89d2f63802373c28dc64010cd6c8)#define GPIO\_P39 APOLLO4\_PINMUX(39, 3)

[ 475](ambiq-apollo4-pinctrl_8h.md#a36cab239ae69eddbc229f7582a5334c1)#define UART2RTS\_P39 APOLLO4\_PINMUX(39, 4)

[ 476](ambiq-apollo4-pinctrl_8h.md#acdb641cd98e02c01eb27200f14b37d6c)#define DISP\_D17\_P39 APOLLO4\_PINMUX(39, 5)

[ 477](ambiq-apollo4-pinctrl_8h.md#adb24a666ead570eca8fa756d4e268b1d)#define CT39\_P39 APOLLO4\_PINMUX(39, 6)

[ 478](ambiq-apollo4-pinctrl_8h.md#a19f65e640f83c7b7858f2520302ae658)#define NCE39\_P39 APOLLO4\_PINMUX(39, 7)

[ 479](ambiq-apollo4-pinctrl_8h.md#a662633fabc70c777fe91bed65808c4c6)#define OBSBUS7\_P39 APOLLO4\_PINMUX(39, 8)

[ 480](ambiq-apollo4-pinctrl_8h.md#abe73dd787f40f23cf5f42a94e7b2c492)#define FPIO\_P39 APOLLO4\_PINMUX(39, 11)

[ 481](ambiq-apollo4-pinctrl_8h.md#afe3f3ffa3aef79c3d54b3f6fba1a8369)#define MSPI1\_3\_P40 APOLLO4\_PINMUX(40, 0)

[ 482](ambiq-apollo4-pinctrl_8h.md#a845a19ab8077a08d7dc902f8e022c2d6)#define TRIG1\_P40 APOLLO4\_PINMUX(40, 1)

[ 483](ambiq-apollo4-pinctrl_8h.md#a8fd31b228fd81a8786542f4252d3735d)#define SWTRACE1\_P40 APOLLO4\_PINMUX(40, 2)

[ 484](ambiq-apollo4-pinctrl_8h.md#a388d84a144f3522f0fa9a6d5f860219c)#define GPIO\_P40 APOLLO4\_PINMUX(40, 3)

[ 485](ambiq-apollo4-pinctrl_8h.md#a77ecdea6ff651d03aeffdc62063642b0)#define UART0CTS\_P40 APOLLO4\_PINMUX(40, 4)

[ 486](ambiq-apollo4-pinctrl_8h.md#ac129b60cff598256240e646fc587115d)#define DISP\_D18\_P40 APOLLO4\_PINMUX(40, 5)

[ 487](ambiq-apollo4-pinctrl_8h.md#acad336b462e6e70e161d765727e8e08a)#define CT40\_P40 APOLLO4\_PINMUX(40, 6)

[ 488](ambiq-apollo4-pinctrl_8h.md#af9880fd4347b1bd29e5415a74d02dc94)#define NCE40\_P40 APOLLO4\_PINMUX(40, 7)

[ 489](ambiq-apollo4-pinctrl_8h.md#a62470a0912d3be6df66e11564b731bfb)#define OBSBUS8\_P40 APOLLO4\_PINMUX(40, 8)

[ 490](ambiq-apollo4-pinctrl_8h.md#a6e09620e8ef38a74d7c21a1d741af3f0)#define FPIO\_P40 APOLLO4\_PINMUX(40, 11)

[ 491](ambiq-apollo4-pinctrl_8h.md#a4884ccaba7f1a929a5d7b8689fd5a9c6)#define MSPI1\_4\_P41 APOLLO4\_PINMUX(41, 0)

[ 492](ambiq-apollo4-pinctrl_8h.md#a401aefb6bfdd2f5c0e7de9e6782cc8e1)#define TRIG0\_P41 APOLLO4\_PINMUX(41, 1)

[ 493](ambiq-apollo4-pinctrl_8h.md#a98bdfed44757f260f250ae4475739b5d)#define SWTRACE2\_P41 APOLLO4\_PINMUX(41, 2)

[ 494](ambiq-apollo4-pinctrl_8h.md#a8c96f8b549c1d2739c024137286035e1)#define GPIO\_P41 APOLLO4\_PINMUX(41, 3)

[ 495](ambiq-apollo4-pinctrl_8h.md#a2b7dc7334200258b20a08422ea361f70)#define UART0TX\_P41 APOLLO4\_PINMUX(41, 4)

[ 496](ambiq-apollo4-pinctrl_8h.md#afc71fb9ad919e14dbc19c89f19f19db0)#define DISP\_D19\_P41 APOLLO4\_PINMUX(41, 5)

[ 497](ambiq-apollo4-pinctrl_8h.md#affa06bbeb38d8b01d54a6457f58c2733)#define CT41\_P41 APOLLO4\_PINMUX(41, 6)

[ 498](ambiq-apollo4-pinctrl_8h.md#aaaf74f87cd67b25b654c92e58311d818)#define NCE41\_P41 APOLLO4\_PINMUX(41, 7)

[ 499](ambiq-apollo4-pinctrl_8h.md#a56e25a84951a00958c81c3f2c89e161c)#define OBSBUS9\_P41 APOLLO4\_PINMUX(41, 8)

[ 500](ambiq-apollo4-pinctrl_8h.md#a7d5cbbcd03000b54af3d06566fd3b659)#define SWO\_P41 APOLLO4\_PINMUX(41, 9)

[ 501](ambiq-apollo4-pinctrl_8h.md#aef07340f5eef96eedc1880d1924e09fe)#define FPIO\_P41 APOLLO4\_PINMUX(41, 11)

[ 502](ambiq-apollo4-pinctrl_8h.md#ace7774f452ddc11813ee5d72ab48d228)#define MSPI1\_5\_P42 APOLLO4\_PINMUX(42, 0)

[ 503](ambiq-apollo4-pinctrl_8h.md#a03de270db732892d4bb6af06ccb3b8b0)#define TRIG2\_P42 APOLLO4\_PINMUX(42, 1)

[ 504](ambiq-apollo4-pinctrl_8h.md#a303a3c81512c32f9f20ebcc051681794)#define SWTRACE3\_P42 APOLLO4\_PINMUX(42, 2)

[ 505](ambiq-apollo4-pinctrl_8h.md#ad2ddbd7fd0001abfcf1416caa9f56496)#define GPIO\_P42 APOLLO4\_PINMUX(42, 3)

[ 506](ambiq-apollo4-pinctrl_8h.md#a1dd8b951fe3e551fbeab75902c6bdae0)#define UART2TX\_P42 APOLLO4\_PINMUX(42, 4)

[ 507](ambiq-apollo4-pinctrl_8h.md#a567098441d6eb14be84cba3da16cb805)#define DISP\_D20\_P42 APOLLO4\_PINMUX(42, 5)

[ 508](ambiq-apollo4-pinctrl_8h.md#a99e035619a6259703841dafaaa86f9d7)#define CT42\_P42 APOLLO4\_PINMUX(42, 6)

[ 509](ambiq-apollo4-pinctrl_8h.md#ae5399f9d5357e096d59283bfea4fd6ee)#define NCE42\_P42 APOLLO4\_PINMUX(42, 7)

[ 510](ambiq-apollo4-pinctrl_8h.md#ab913e0fe787ff2c6a9483a437e0fa0c5)#define OBSBUS10\_P42 APOLLO4\_PINMUX(42, 8)

[ 511](ambiq-apollo4-pinctrl_8h.md#a67712803c78ffdea03fc1c83c6996655)#define FPIO\_P42 APOLLO4\_PINMUX(42, 11)

[ 512](ambiq-apollo4-pinctrl_8h.md#acaf88c6546206d22b4c16bbe9b6962bf)#define MSPI1\_6\_P43 APOLLO4\_PINMUX(43, 0)

[ 513](ambiq-apollo4-pinctrl_8h.md#a9c46d46c4cd95f872c311f0df182bdca)#define TRIG3\_P43 APOLLO4\_PINMUX(43, 1)

[ 514](ambiq-apollo4-pinctrl_8h.md#a8f9ce3ccad4f733d4a86a47de42fc745)#define SWTRACECTL\_P43 APOLLO4\_PINMUX(43, 2)

[ 515](ambiq-apollo4-pinctrl_8h.md#aab2f5553d3ce7da8f585c493f82da02f)#define GPIO\_P43 APOLLO4\_PINMUX(43, 3)

[ 516](ambiq-apollo4-pinctrl_8h.md#aa92c55f43fa3df211ad8a10c01c44836)#define UART0RX\_P43 APOLLO4\_PINMUX(43, 4)

[ 517](ambiq-apollo4-pinctrl_8h.md#adf34a633441da303a6894de7f1143806)#define DISP\_D21\_P43 APOLLO4\_PINMUX(43, 5)

[ 518](ambiq-apollo4-pinctrl_8h.md#ace3bad9668e224264d49d764159b4e16)#define CT43\_P43 APOLLO4\_PINMUX(43, 6)

[ 519](ambiq-apollo4-pinctrl_8h.md#a93e018507d62174c89e7fa137dde36cd)#define NCE43\_P43 APOLLO4\_PINMUX(43, 7)

[ 520](ambiq-apollo4-pinctrl_8h.md#ac4e97552126e4b7862e234ac07e3194a)#define OBSBUS11\_P43 APOLLO4\_PINMUX(43, 8)

[ 521](ambiq-apollo4-pinctrl_8h.md#a8cda8cb936bbb51c64fb7b7368a03d20)#define FPIO\_P43 APOLLO4\_PINMUX(43, 11)

[ 522](ambiq-apollo4-pinctrl_8h.md#aca8aa18c44d95794960cfac2fa137f2c)#define MSPI1\_7\_P44 APOLLO4\_PINMUX(44, 0)

[ 523](ambiq-apollo4-pinctrl_8h.md#aabc03e3a212209cb02c0d7505027cc96)#define TRIG1\_P44 APOLLO4\_PINMUX(44, 1)

[ 524](ambiq-apollo4-pinctrl_8h.md#a090967f1db53f7ab68aba6760b35807b)#define SWO\_P44 APOLLO4\_PINMUX(44, 2)

[ 525](ambiq-apollo4-pinctrl_8h.md#accbd9b4f6fa257af91af9a533ba856ea)#define GPIO\_P44 APOLLO4\_PINMUX(44, 3)

[ 526](ambiq-apollo4-pinctrl_8h.md#a462458462b185a884285eec13d748322)#define UART2RX\_P44 APOLLO4\_PINMUX(44, 4)

[ 527](ambiq-apollo4-pinctrl_8h.md#ab2f8e726a5147416b96591ec82c1848f)#define DISP\_D22\_P44 APOLLO4\_PINMUX(44, 5)

[ 528](ambiq-apollo4-pinctrl_8h.md#a307ecf8a8c68f0c82b854f2391bc4db6)#define CT44\_P44 APOLLO4\_PINMUX(44, 6)

[ 529](ambiq-apollo4-pinctrl_8h.md#a3ed79603ebbdb77c08f3d793c0f361d7)#define NCE44\_P44 APOLLO4\_PINMUX(44, 7)

[ 530](ambiq-apollo4-pinctrl_8h.md#ac805c9137dc8c4abe8cf21f8af7d1fb1)#define OBSBUS12\_P44 APOLLO4\_PINMUX(44, 8)

[ 531](ambiq-apollo4-pinctrl_8h.md#a663ea6c000c8498e9895b7c0611137de)#define VCMPO\_P44 APOLLO4\_PINMUX(44, 9)

[ 532](ambiq-apollo4-pinctrl_8h.md#abff6387be48023927767504d216f7fbc)#define FPIO\_P44 APOLLO4\_PINMUX(44, 11)

[ 533](ambiq-apollo4-pinctrl_8h.md#a9a6ccc54b6b4bb1580a2b692dfe2da93)#define MSPI1\_8\_P45 APOLLO4\_PINMUX(45, 0)

[ 534](ambiq-apollo4-pinctrl_8h.md#a757a2dfe0d45bc7757a5db858f7c9350)#define TRIG2\_P45 APOLLO4\_PINMUX(45, 1)

[ 535](ambiq-apollo4-pinctrl_8h.md#a508cfcad47c0b4eceac816703569af1e)#define XT32KHZ\_P45 APOLLO4\_PINMUX(45, 2)

[ 536](ambiq-apollo4-pinctrl_8h.md#afda67e6b2d71c41df2c9384829780eaf)#define GPIO\_P45 APOLLO4\_PINMUX(45, 3)

[ 537](ambiq-apollo4-pinctrl_8h.md#a270d8fef46f16beef161343defec0f6d)#define UART0TX\_P45 APOLLO4\_PINMUX(45, 4)

[ 538](ambiq-apollo4-pinctrl_8h.md#a9db7c71cfaf945afc821f0018637f7d2)#define DISP\_D23\_P45 APOLLO4\_PINMUX(45, 5)

[ 539](ambiq-apollo4-pinctrl_8h.md#a38d8e31a202a282fb68595de3e2ede58)#define CT45\_P45 APOLLO4\_PINMUX(45, 6)

[ 540](ambiq-apollo4-pinctrl_8h.md#a8b9c9c5513d7098d3772bf031eefdc34)#define NCE45\_P45 APOLLO4\_PINMUX(45, 7)

[ 541](ambiq-apollo4-pinctrl_8h.md#ae8286cb032fcc68ff9ee312d7ac839fa)#define OBSBUS13\_P45 APOLLO4\_PINMUX(45, 8)

[ 542](ambiq-apollo4-pinctrl_8h.md#ae0da20784c809dc66c53076a15019f92)#define FPIO\_P45 APOLLO4\_PINMUX(45, 11)

[ 543](ambiq-apollo4-pinctrl_8h.md#aad2389dd65eee1688eb0f2b0144ff18e)#define MSPI1\_9\_P46 APOLLO4\_PINMUX(46, 0)

[ 544](ambiq-apollo4-pinctrl_8h.md#a631c1e6711fd9a06d46f65e69754b978)#define TRIG3\_P46 APOLLO4\_PINMUX(46, 1)

[ 545](ambiq-apollo4-pinctrl_8h.md#abe0d7009ca2a6f4ef89a931472bf91eb)#define CLKOUT\_32M\_P46 APOLLO4\_PINMUX(46, 2)

[ 546](ambiq-apollo4-pinctrl_8h.md#af5d342a38a441738d343eeef58c1cdb3)#define GPIO\_P46 APOLLO4\_PINMUX(46, 3)

[ 547](ambiq-apollo4-pinctrl_8h.md#a455cbde0d1752a2502326edf30e3da40)#define UART2TX\_P46 APOLLO4\_PINMUX(46, 4)

[ 548](ambiq-apollo4-pinctrl_8h.md#a96e2a89a72f95dfaaca43d19c3f3d2f1)#define UART3TX\_P46 APOLLO4\_PINMUX(46, 5)

[ 549](ambiq-apollo4-pinctrl_8h.md#a5b91464bc0151a9faa1f0fb07b832dd2)#define CT46\_P46 APOLLO4\_PINMUX(46, 6)

[ 550](ambiq-apollo4-pinctrl_8h.md#a5b0e939354b2c232bdc48a3dcb9a1607)#define NCE46\_P46 APOLLO4\_PINMUX(46, 7)

[ 551](ambiq-apollo4-pinctrl_8h.md#a4204bbc003ee331aa4208d9adfd14d0d)#define OBSBUS14\_P46 APOLLO4\_PINMUX(46, 8)

[ 552](ambiq-apollo4-pinctrl_8h.md#a0cd4d0d53c51d869e74fc6da2849e1d8)#define I2S1\_SDIN\_P46 APOLLO4\_PINMUX(46, 9)

[ 553](ambiq-apollo4-pinctrl_8h.md#a7d2c242295e85abf9ed7a4a6867263fd)#define I2S0\_SDIN\_P46 APOLLO4\_PINMUX(46, 10)

[ 554](ambiq-apollo4-pinctrl_8h.md#a0b30928501fcdc60d9521241f25af55f)#define FPIO\_P46 APOLLO4\_PINMUX(46, 11)

[ 555](ambiq-apollo4-pinctrl_8h.md#a902c3629eb928ee341b7509152aa6956)#define M5SCL\_P47 APOLLO4\_PINMUX(47, 0)

[ 556](ambiq-apollo4-pinctrl_8h.md#ac185a180c26fb1be903475b1f55352c5)#define M5SCK\_P47 APOLLO4\_PINMUX(47, 1)

[ 557](ambiq-apollo4-pinctrl_8h.md#a22679fcb7d227d528ad6737ce29bbb8a)#define I2S1\_CLK\_P47 APOLLO4\_PINMUX(47, 2)

[ 558](ambiq-apollo4-pinctrl_8h.md#a1eb20e4fdae76831bf870bff406c346e)#define GPIO\_P47 APOLLO4\_PINMUX(47, 3)

[ 559](ambiq-apollo4-pinctrl_8h.md#a543da39eb9f9117a50fba3d1d970149b)#define UART0RX\_P47 APOLLO4\_PINMUX(47, 4)

[ 560](ambiq-apollo4-pinctrl_8h.md#a45c38170a7a3b57c6576ebfa6f52b35c)#define UART1RX\_P47 APOLLO4\_PINMUX(47, 5)

[ 561](ambiq-apollo4-pinctrl_8h.md#a70606c0a3f6d3f013b4cfbad6f7f1358)#define CT47\_P47 APOLLO4\_PINMUX(47, 6)

[ 562](ambiq-apollo4-pinctrl_8h.md#a1f411d730489dee140ae375049d449fd)#define NCE47\_P47 APOLLO4\_PINMUX(47, 7)

[ 563](ambiq-apollo4-pinctrl_8h.md#a70cb524641601aae5a49e45af2295a3d)#define OBSBUS15\_P47 APOLLO4\_PINMUX(47, 8)

[ 564](ambiq-apollo4-pinctrl_8h.md#a09e14546b5ebc2193fc453b0aabc63d1)#define I2S0\_CLK\_P47 APOLLO4\_PINMUX(47, 10)

[ 565](ambiq-apollo4-pinctrl_8h.md#ad6ad32660b46edee36c0a23e6768fdac)#define FPIO\_P47 APOLLO4\_PINMUX(47, 11)

[ 566](ambiq-apollo4-pinctrl_8h.md#ae95e8cdcccb1d21c16440e8bcc1f3d08)#define M5SDAWIR3\_P48 APOLLO4\_PINMUX(48, 0)

[ 567](ambiq-apollo4-pinctrl_8h.md#a5151c680f3a59a7877316a478114f77a)#define M5MOSI\_P48 APOLLO4\_PINMUX(48, 1)

[ 568](ambiq-apollo4-pinctrl_8h.md#aeb2ab47123e747c0ded26c6abbfacd07)#define I2S1\_DATA\_P48 APOLLO4\_PINMUX(48, 2)

[ 569](ambiq-apollo4-pinctrl_8h.md#af730366def18c0d1bf2e4c00fe3c1ab8)#define GPIO\_P48 APOLLO4\_PINMUX(48, 3)

[ 570](ambiq-apollo4-pinctrl_8h.md#a41dc586180eaac42afe9f9b720ed7a4e)#define UART2RX\_P48 APOLLO4\_PINMUX(48, 4)

[ 571](ambiq-apollo4-pinctrl_8h.md#a2d86dfd304b8fc726bebcaa1d5198998)#define UART3RX\_P48 APOLLO4\_PINMUX(48, 5)

[ 572](ambiq-apollo4-pinctrl_8h.md#a827095d5558cc5e18595bead0110248b)#define CT48\_P48 APOLLO4\_PINMUX(48, 6)

[ 573](ambiq-apollo4-pinctrl_8h.md#ad2333f40db7fb9ecfbd1392e9554ffa3)#define NCE48\_P48 APOLLO4\_PINMUX(48, 7)

[ 574](ambiq-apollo4-pinctrl_8h.md#a4fac1541ce6af57cbf93c77f1a4bc992)#define OBSBUS0\_P48 APOLLO4\_PINMUX(48, 8)

[ 575](ambiq-apollo4-pinctrl_8h.md#a4148b6126bd9b4f94c5db9676e0a31c4)#define I2S1\_SDOUT\_P48 APOLLO4\_PINMUX(48, 9)

[ 576](ambiq-apollo4-pinctrl_8h.md#ae22565f677c08fad32c77b90d3dc300c)#define I2S0\_SDOUT\_P48 APOLLO4\_PINMUX(48, 10)

[ 577](ambiq-apollo4-pinctrl_8h.md#a2b78d51505886bdb9b0c021439b04694)#define FPIO\_P48 APOLLO4\_PINMUX(48, 11)

[ 578](ambiq-apollo4-pinctrl_8h.md#a9393e54fe2a906feb32275d905db7465)#define M5MISO\_P49 APOLLO4\_PINMUX(49, 0)

[ 579](ambiq-apollo4-pinctrl_8h.md#ae417f428aa307fa38355ef8da2d16204)#define TRIG0\_P49 APOLLO4\_PINMUX(49, 1)

[ 580](ambiq-apollo4-pinctrl_8h.md#a6e0965dfe3a43f8db69c5189c83920ca)#define I2S1\_WS\_P49 APOLLO4\_PINMUX(49, 2)

[ 581](ambiq-apollo4-pinctrl_8h.md#a4b290382e034342af84424e34cb6d297)#define GPIO\_P49 APOLLO4\_PINMUX(49, 3)

[ 582](ambiq-apollo4-pinctrl_8h.md#afa660e4cf4e803dd0493805482032278)#define UART0RTS\_P49 APOLLO4\_PINMUX(49, 4)

[ 583](ambiq-apollo4-pinctrl_8h.md#aa3bba038358012f9b977c4472e0e952e)#define UART1RTS\_P49 APOLLO4\_PINMUX(49, 5)

[ 584](ambiq-apollo4-pinctrl_8h.md#a0eae6844c2d978c75c9cdb0f072f6e9e)#define CT49\_P49 APOLLO4\_PINMUX(49, 6)

[ 585](ambiq-apollo4-pinctrl_8h.md#a339781c28180de2027fc9295189463e1)#define NCE49\_P49 APOLLO4\_PINMUX(49, 7)

[ 586](ambiq-apollo4-pinctrl_8h.md#a9e3d456cb4258379d0fb21d0330551a3)#define OBSBUS1\_P49 APOLLO4\_PINMUX(49, 8)

[ 587](ambiq-apollo4-pinctrl_8h.md#aff1741cb4f6d3a03f310e1dfc9c87b8a)#define I2S0\_WS\_P49 APOLLO4\_PINMUX(49, 10)

[ 588](ambiq-apollo4-pinctrl_8h.md#adabcc3e2028551c518ae75edb032201d)#define FPIO\_P49 APOLLO4\_PINMUX(49, 11)

[ 589](ambiq-apollo4-pinctrl_8h.md#aa50f07d7f5f02b819ec18624e7c6bc57)#define PDM0\_CLK\_P50 APOLLO4\_PINMUX(50, 0)

[ 590](ambiq-apollo4-pinctrl_8h.md#a00ddebe74fab96104c726ad3724f5d01)#define TRIG0\_P50 APOLLO4\_PINMUX(50, 1)

[ 591](ambiq-apollo4-pinctrl_8h.md#a0277a0212f65af4305e9ea85a8ce29c2)#define SWTRACECLK\_P50 APOLLO4\_PINMUX(50, 2)

[ 592](ambiq-apollo4-pinctrl_8h.md#a44de537cf2f84b012dc099c000d47eee)#define GPIO\_P50 APOLLO4\_PINMUX(50, 3)

[ 593](ambiq-apollo4-pinctrl_8h.md#a73831155bc45305a597892c3d55d559f)#define UART2RTS\_P50 APOLLO4\_PINMUX(50, 4)

[ 594](ambiq-apollo4-pinctrl_8h.md#ac7d40eee5d6acf28b37849191f6bc9ce)#define UART3RTS\_P50 APOLLO4\_PINMUX(50, 5)

[ 595](ambiq-apollo4-pinctrl_8h.md#abcfe829a5fb2061461bd25d952e886e9)#define CT50\_P50 APOLLO4\_PINMUX(50, 6)

[ 596](ambiq-apollo4-pinctrl_8h.md#ab7492256a637deef5ea4943b4b701110)#define NCE50\_P50 APOLLO4\_PINMUX(50, 7)

[ 597](ambiq-apollo4-pinctrl_8h.md#a57bd2b14b2ea2d5a659eb460fde52832)#define OBSBUS2\_P50 APOLLO4\_PINMUX(50, 8)

[ 598](ambiq-apollo4-pinctrl_8h.md#a0c4cc83ff342181fb5d0fb4161f23a53)#define DISP\_TE\_P50 APOLLO4\_PINMUX(50, 9)

[ 599](ambiq-apollo4-pinctrl_8h.md#ace8657a095be6f8f96cc55530896f12f)#define FPIO\_P50 APOLLO4\_PINMUX(50, 11)

[ 600](ambiq-apollo4-pinctrl_8h.md#af337c19364ebe5cdc93f3455bdbdc34f)#define PDM0\_DATA\_P51 APOLLO4\_PINMUX(51, 0)

[ 601](ambiq-apollo4-pinctrl_8h.md#a9e3291a44b5b7a7f76d91aa936c01bdc)#define TRIG1\_P51 APOLLO4\_PINMUX(51, 1)

[ 602](ambiq-apollo4-pinctrl_8h.md#ac079572719cd1da1f98901a6e84d990c)#define SWTRACE0\_P51 APOLLO4\_PINMUX(51, 2)

[ 603](ambiq-apollo4-pinctrl_8h.md#a78a6a9fa2e9eb9ba6ff803a5810de263)#define GPIO\_P51 APOLLO4\_PINMUX(51, 3)

[ 604](ambiq-apollo4-pinctrl_8h.md#ae435e9bbde08cbabdc20ae8f42f5ef99)#define UART0CTS\_P51 APOLLO4\_PINMUX(51, 4)

[ 605](ambiq-apollo4-pinctrl_8h.md#a92c86ddd6c1cb0632009df0dc819276b)#define UART1CTS\_P51 APOLLO4\_PINMUX(51, 5)

[ 606](ambiq-apollo4-pinctrl_8h.md#a518ed14db5018e3b2ab50466909443a8)#define CT51\_P51 APOLLO4\_PINMUX(51, 6)

[ 607](ambiq-apollo4-pinctrl_8h.md#aeca26feeace6bc79995c2e619b1a9c18)#define NCE51\_P51 APOLLO4\_PINMUX(51, 7)

[ 608](ambiq-apollo4-pinctrl_8h.md#a4886f7addf80e5033f316ae75dac2716)#define OBSBUS3\_P51 APOLLO4\_PINMUX(51, 8)

[ 609](ambiq-apollo4-pinctrl_8h.md#aee6c77367a6681e682aa54ccfd560eea)#define FPIO\_P51 APOLLO4\_PINMUX(51, 11)

[ 610](ambiq-apollo4-pinctrl_8h.md#a000e4409db1191da5975b778d79987ff)#define PDM1\_CLK\_P52 APOLLO4\_PINMUX(52, 0)

[ 611](ambiq-apollo4-pinctrl_8h.md#aeb359b5253c0fefc6a4611e00cb6a918)#define TRIG2\_P52 APOLLO4\_PINMUX(52, 1)

[ 612](ambiq-apollo4-pinctrl_8h.md#a7155df37132184e182ebff7742c7cc37)#define SWTRACE1\_P52 APOLLO4\_PINMUX(52, 2)

[ 613](ambiq-apollo4-pinctrl_8h.md#aa8fc5cd8e841cc12ee97736b5d5b2637)#define GPIO\_P52 APOLLO4\_PINMUX(52, 3)

[ 614](ambiq-apollo4-pinctrl_8h.md#a847de0997e0238e541d8ef6d381331f8)#define UART2CTS\_P52 APOLLO4\_PINMUX(52, 4)

[ 615](ambiq-apollo4-pinctrl_8h.md#a7e0b509cc6521128570d0e5822d6029b)#define UART3CTS\_P52 APOLLO4\_PINMUX(52, 5)

[ 616](ambiq-apollo4-pinctrl_8h.md#a61e3360904a8d0ace027450f1e34d59d)#define CT52\_P52 APOLLO4\_PINMUX(52, 6)

[ 617](ambiq-apollo4-pinctrl_8h.md#ae86416562248f70f8fddcbfda85a3ae3)#define NCE52\_P52 APOLLO4\_PINMUX(52, 7)

[ 618](ambiq-apollo4-pinctrl_8h.md#ab77156824b7b5e6c3a1d077f18a702bb)#define OBSBUS4\_P52 APOLLO4\_PINMUX(52, 8)

[ 619](ambiq-apollo4-pinctrl_8h.md#a97689e19a50cef3cb32294b79bc9313f)#define VCMPO\_P52 APOLLO4\_PINMUX(52, 9)

[ 620](ambiq-apollo4-pinctrl_8h.md#ae977b5c8f4df091d43a5452d0f22aff9)#define FPIO\_P52 APOLLO4\_PINMUX(52, 11)

[ 621](ambiq-apollo4-pinctrl_8h.md#a9d82ae7764f493b17911c99b1ef66b13)#define PDM1\_DATA\_P53 APOLLO4\_PINMUX(53, 0)

[ 622](ambiq-apollo4-pinctrl_8h.md#acd888267b2838dd9cda1d426350ee08f)#define TRIG3\_P53 APOLLO4\_PINMUX(53, 1)

[ 623](ambiq-apollo4-pinctrl_8h.md#a532d8ae88d884355cffc1b38f79b5787)#define SWTRACE2\_P53 APOLLO4\_PINMUX(53, 2)

[ 624](ambiq-apollo4-pinctrl_8h.md#aa41e6f073ae876d1486552a07ace93a3)#define GPIO\_P53 APOLLO4\_PINMUX(53, 3)

[ 625](ambiq-apollo4-pinctrl_8h.md#a5737a37353ddba9779853ccb77a82f41)#define UART0TX\_P53 APOLLO4\_PINMUX(53, 4)

[ 626](ambiq-apollo4-pinctrl_8h.md#ac0e61a543d32ac51dc41ffe61171e620)#define UART1TX\_P53 APOLLO4\_PINMUX(53, 5)

[ 627](ambiq-apollo4-pinctrl_8h.md#aa018ac3d8dddda809a4a01c072b8b7f6)#define CT53\_P53 APOLLO4\_PINMUX(53, 6)

[ 628](ambiq-apollo4-pinctrl_8h.md#aae0ee7affb647cfd3d54d168868ef485)#define NCE53\_P53 APOLLO4\_PINMUX(53, 7)

[ 629](ambiq-apollo4-pinctrl_8h.md#aef8b55cb9f1bab911cd8b95e41121d15)#define OBSBUS5\_P53 APOLLO4\_PINMUX(53, 8)

[ 630](ambiq-apollo4-pinctrl_8h.md#a076abaf60713d10d1a40223a2ccddfcb)#define FPIO\_P53 APOLLO4\_PINMUX(53, 11)

[ 631](ambiq-apollo4-pinctrl_8h.md#ab679e24b6deacb7b2332c5a00df122a5)#define PDM2\_CLK\_P54 APOLLO4\_PINMUX(54, 0)

[ 632](ambiq-apollo4-pinctrl_8h.md#a0aba00320e45884349101d67e9a9c1a0)#define TRIG0\_P54 APOLLO4\_PINMUX(54, 1)

[ 633](ambiq-apollo4-pinctrl_8h.md#af40155dade162b3e5436075eb214fdbb)#define SWTRACE3\_P54 APOLLO4\_PINMUX(54, 2)

[ 634](ambiq-apollo4-pinctrl_8h.md#a8b614afb4941fbe9036fa20421a55820)#define GPIO\_P54 APOLLO4\_PINMUX(54, 3)

[ 635](ambiq-apollo4-pinctrl_8h.md#a7d6c90ad937dd7d7a62978f773936980)#define UART2TX\_P54 APOLLO4\_PINMUX(54, 4)

[ 636](ambiq-apollo4-pinctrl_8h.md#a45581cbe496bf559eaa6ac7b22b95bd5)#define UART3TX\_P54 APOLLO4\_PINMUX(54, 5)

[ 637](ambiq-apollo4-pinctrl_8h.md#acfaa87df52dc894034c4f4951d9dd3f9)#define CT54\_P54 APOLLO4\_PINMUX(54, 6)

[ 638](ambiq-apollo4-pinctrl_8h.md#a6318a96c1367922e5ecd0f682d432630)#define NCE54\_P54 APOLLO4\_PINMUX(54, 7)

[ 639](ambiq-apollo4-pinctrl_8h.md#a4a8eb44700f156a737d33749e5c2ace0)#define OBSBUS6\_P54 APOLLO4\_PINMUX(54, 8)

[ 640](ambiq-apollo4-pinctrl_8h.md#a68c5a8095a20e1d5a735d23e34559aa5)#define FPIO\_P54 APOLLO4\_PINMUX(54, 11)

[ 641](ambiq-apollo4-pinctrl_8h.md#a2ae09c0bc18498f451175862a77d99d1)#define PDM2\_DATA\_P55 APOLLO4\_PINMUX(55, 0)

[ 642](ambiq-apollo4-pinctrl_8h.md#a20444a5b8214c9bd7441f61e41a79be3)#define TRIG1\_P55 APOLLO4\_PINMUX(55, 1)

[ 643](ambiq-apollo4-pinctrl_8h.md#a2497656a2ac1a80c20e22b7897ad805b)#define SWTRACECTL\_P55 APOLLO4\_PINMUX(55, 2)

[ 644](ambiq-apollo4-pinctrl_8h.md#a2fcffaace9255d9e639de6c2596603c8)#define GPIO\_P55 APOLLO4\_PINMUX(55, 3)

[ 645](ambiq-apollo4-pinctrl_8h.md#a21c1ad5983748d43e07381c1ef2e7c69)#define UART0RX\_P55 APOLLO4\_PINMUX(55, 4)

[ 646](ambiq-apollo4-pinctrl_8h.md#aff795eeb66938fb5c19b3ada22322192)#define UART1RX\_P55 APOLLO4\_PINMUX(55, 5)

[ 647](ambiq-apollo4-pinctrl_8h.md#a519357ea5e08da07f89584a7c38d6cf3)#define CT55\_P55 APOLLO4\_PINMUX(55, 6)

[ 648](ambiq-apollo4-pinctrl_8h.md#ad5438399e3ff56c263631991b09dd460)#define NCE55\_P55 APOLLO4\_PINMUX(55, 7)

[ 649](ambiq-apollo4-pinctrl_8h.md#a50c5ec35134d0026560aaaa385d7187d)#define OBSBUS7\_P55 APOLLO4\_PINMUX(55, 8)

[ 650](ambiq-apollo4-pinctrl_8h.md#a75c782682f9cbd1500400881dd4b1c3d)#define FPIO\_P55 APOLLO4\_PINMUX(55, 11)

[ 651](ambiq-apollo4-pinctrl_8h.md#aa01f5915dd35838e6944eb1dbfe3ebe4)#define PDM3\_CLK\_P56 APOLLO4\_PINMUX(56, 0)

[ 652](ambiq-apollo4-pinctrl_8h.md#ac80e2bbb6824d28aa989a71b9fcdbc4c)#define TRIG2\_P56 APOLLO4\_PINMUX(56, 1)

[ 653](ambiq-apollo4-pinctrl_8h.md#a068d73a4cad98ec481a16b4e9968bf29)#define SWO\_P56 APOLLO4\_PINMUX(56, 2)

[ 654](ambiq-apollo4-pinctrl_8h.md#ad9c517c0112a8c8634b9ad46ee32dd45)#define GPIO\_P56 APOLLO4\_PINMUX(56, 3)

[ 655](ambiq-apollo4-pinctrl_8h.md#a7cffb59223ce4cb44d9aaeaeffe18c2e)#define UART2RX\_P56 APOLLO4\_PINMUX(56, 4)

[ 656](ambiq-apollo4-pinctrl_8h.md#ac5d7c44f0030d6c24cb165cda050ab0b)#define UART3RX\_P56 APOLLO4\_PINMUX(56, 5)

[ 657](ambiq-apollo4-pinctrl_8h.md#a7704961de44060405b780e8c6a8f7be1)#define CT56\_P56 APOLLO4\_PINMUX(56, 6)

[ 658](ambiq-apollo4-pinctrl_8h.md#ad8e09cff85610b1bfb03403771360685)#define NCE56\_P56 APOLLO4\_PINMUX(56, 7)

[ 659](ambiq-apollo4-pinctrl_8h.md#acb43e66d36063e531a99be61d5c0581d)#define OBSBUS8\_P56 APOLLO4\_PINMUX(56, 8)

[ 660](ambiq-apollo4-pinctrl_8h.md#ad839f93b67f38d8356c45e36466fa0a6)#define FPIO\_P56 APOLLO4\_PINMUX(56, 11)

[ 661](ambiq-apollo4-pinctrl_8h.md#a564258d69dabf2a58e709c68a71435ae)#define PDM3\_DATA\_P57 APOLLO4\_PINMUX(57, 0)

[ 662](ambiq-apollo4-pinctrl_8h.md#a46155f21a9c6a4e7ff955d15a3461686)#define TRIG3\_P57 APOLLO4\_PINMUX(57, 1)

[ 663](ambiq-apollo4-pinctrl_8h.md#ae105fe5c598952b09b7bd714e73b46e9)#define SWO\_P57 APOLLO4\_PINMUX(57, 2)

[ 664](ambiq-apollo4-pinctrl_8h.md#a83be188c573c4f64966aae37f47caf5b)#define GPIO\_P57 APOLLO4\_PINMUX(57, 3)

[ 665](ambiq-apollo4-pinctrl_8h.md#ae1d748a935aa40f21b9e722ea2e05813)#define UART0RTS\_P57 APOLLO4\_PINMUX(57, 4)

[ 666](ambiq-apollo4-pinctrl_8h.md#aea0bf50505dba102ea3231261248a2ec)#define UART1RTS\_P57 APOLLO4\_PINMUX(57, 5)

[ 667](ambiq-apollo4-pinctrl_8h.md#ac25056b4bd9749812a027c030bc39e76)#define CT57\_P57 APOLLO4\_PINMUX(57, 6)

[ 668](ambiq-apollo4-pinctrl_8h.md#a98fb369e6acd52cc5aae8e6730ed9758)#define NCE57\_P57 APOLLO4\_PINMUX(57, 7)

[ 669](ambiq-apollo4-pinctrl_8h.md#a73074d9fbbd7340a50caf05827eb6d7c)#define OBSBUS9\_P57 APOLLO4\_PINMUX(57, 8)

[ 670](ambiq-apollo4-pinctrl_8h.md#a34e60567a7201133b0c4df3cc52f2e2a)#define VCMPO\_P57 APOLLO4\_PINMUX(57, 9)

[ 671](ambiq-apollo4-pinctrl_8h.md#a1275e59ef48b90d62c9e73177767cd81)#define FPIO\_P57 APOLLO4\_PINMUX(57, 11)

[ 672](ambiq-apollo4-pinctrl_8h.md#a876dd6e6770f3c605b06c61e9a6640ac)#define GPIO\_P58 APOLLO4\_PINMUX(58, 3)

[ 673](ambiq-apollo4-pinctrl_8h.md#a5e4285289694d18f2df4250b3a4fbedb)#define UART0RTS\_P58 APOLLO4\_PINMUX(58, 4)

[ 674](ambiq-apollo4-pinctrl_8h.md#aa31491c874b969694a5bfd8c58dd8ed0)#define UART3RTS\_P58 APOLLO4\_PINMUX(58, 5)

[ 675](ambiq-apollo4-pinctrl_8h.md#a6c4c543f61301d57c50acfba3ff456c6)#define CT58\_P58 APOLLO4\_PINMUX(58, 6)

[ 676](ambiq-apollo4-pinctrl_8h.md#aac11c1a52fc64f3c2684b4323e28bdb4)#define NCE58\_P58 APOLLO4\_PINMUX(58, 7)

[ 677](ambiq-apollo4-pinctrl_8h.md#a2d0f34dc3bf65650d7e82a622158e551)#define OBSBUS10\_P58 APOLLO4\_PINMUX(58, 8)

[ 678](ambiq-apollo4-pinctrl_8h.md#a344d3b2fab67b0cab94c63155a292026)#define FPIO\_P58 APOLLO4\_PINMUX(58, 11)

[ 679](ambiq-apollo4-pinctrl_8h.md#aa12c28c05788785d686946947b94d8bc)#define TRIG0\_P59 APOLLO4\_PINMUX(59, 1)

[ 680](ambiq-apollo4-pinctrl_8h.md#ab5b877868310ab0269c468edcac715f7)#define GPIO\_P59 APOLLO4\_PINMUX(59, 3)

[ 681](ambiq-apollo4-pinctrl_8h.md#a827cf63891bdd4f7730a3d7986083446)#define UART0CTS\_P59 APOLLO4\_PINMUX(59, 4)

[ 682](ambiq-apollo4-pinctrl_8h.md#ac4b4fad30f436d2ce2ddaae13c3ea883)#define UART1CTS\_P59 APOLLO4\_PINMUX(59, 5)

[ 683](ambiq-apollo4-pinctrl_8h.md#a157816737f84f410c4c559189eede01d)#define CT59\_P59 APOLLO4\_PINMUX(59, 6)

[ 684](ambiq-apollo4-pinctrl_8h.md#ab437cea609c7b3dbdec00e17f674ee6c)#define NCE59\_P59 APOLLO4\_PINMUX(59, 7)

[ 685](ambiq-apollo4-pinctrl_8h.md#aa1929a618c3f4373fd5a8eb621e81697)#define OBSBUS11\_P59 APOLLO4\_PINMUX(59, 8)

[ 686](ambiq-apollo4-pinctrl_8h.md#a8ddd1b3eb121cec1520b2bcf49bed5ce)#define FPIO\_P59 APOLLO4\_PINMUX(59, 11)

[ 687](ambiq-apollo4-pinctrl_8h.md#ac8b2c40bd5a296c36535a2ad34006402)#define TRIG1\_P60 APOLLO4\_PINMUX(60, 1)

[ 688](ambiq-apollo4-pinctrl_8h.md#ac3a637135617760fba12cf98aeb107c2)#define GPIO\_P60 APOLLO4\_PINMUX(60, 3)

[ 689](ambiq-apollo4-pinctrl_8h.md#a9e6048bb72b44fa3b025619745aa057c)#define UART0TX\_P60 APOLLO4\_PINMUX(60, 4)

[ 690](ambiq-apollo4-pinctrl_8h.md#ad1984df5eedeea1a31dd581e8ffb4b82)#define UART3CTS\_P60 APOLLO4\_PINMUX(60, 5)

[ 691](ambiq-apollo4-pinctrl_8h.md#a0764d1e1564307ce8a345654aad28fb5)#define CT60\_P60 APOLLO4\_PINMUX(60, 6)

[ 692](ambiq-apollo4-pinctrl_8h.md#af5a0f373987f9e093d0be1e96fc422e0)#define NCE60\_P60 APOLLO4\_PINMUX(60, 7)

[ 693](ambiq-apollo4-pinctrl_8h.md#acb91ece35c59b0089f282107812307fd)#define OBSBUS12\_P60 APOLLO4\_PINMUX(60, 8)

[ 694](ambiq-apollo4-pinctrl_8h.md#ab9082f35b47c7cf2a2f50928224568d2)#define FPIO\_P60 APOLLO4\_PINMUX(60, 11)

[ 695](ambiq-apollo4-pinctrl_8h.md#aae16c7af0220e50776497899346da1ee)#define M6SCL\_P61 APOLLO4\_PINMUX(61, 0)

[ 696](ambiq-apollo4-pinctrl_8h.md#ab0279edf2356c9a61a3b5837f7c79c69)#define M6SCK\_P61 APOLLO4\_PINMUX(61, 1)

[ 697](ambiq-apollo4-pinctrl_8h.md#abe1e56fde90420402c996bc8dd0192de)#define I2S1\_CLK\_P61 APOLLO4\_PINMUX(61, 2)

[ 698](ambiq-apollo4-pinctrl_8h.md#a5cc6477cb81b8e732013eee58ce0183d)#define GPIO\_P61 APOLLO4\_PINMUX(61, 3)

[ 699](ambiq-apollo4-pinctrl_8h.md#a7b9c272c4ed7b8e93a28e4cc570a4497)#define UART2TX\_P61 APOLLO4\_PINMUX(61, 4)

[ 700](ambiq-apollo4-pinctrl_8h.md#a9ea1de5c6d00b00178abd669781f0050)#define UART3TX\_P61 APOLLO4\_PINMUX(61, 5)

[ 701](ambiq-apollo4-pinctrl_8h.md#a59d595e89768ffa49adb1421f657f2eb)#define CT61\_P61 APOLLO4\_PINMUX(61, 6)

[ 702](ambiq-apollo4-pinctrl_8h.md#ab5911745a6c23c3a7ded39e214324a1b)#define NCE61\_P61 APOLLO4\_PINMUX(61, 7)

[ 703](ambiq-apollo4-pinctrl_8h.md#ac6f8e5a69355a29de1e8125dfc0b5bc0)#define OBSBUS13\_P61 APOLLO4\_PINMUX(61, 8)

[ 704](ambiq-apollo4-pinctrl_8h.md#aaea3a9facf6d60d3ac7b6a6b8f20da15)#define I3CM0\_SCL\_P61 APOLLO4\_PINMUX(61, 10)

[ 705](ambiq-apollo4-pinctrl_8h.md#acdad2b55909849a8c2d68baa82d93c29)#define FPIO\_P61 APOLLO4\_PINMUX(61, 11)

[ 706](ambiq-apollo4-pinctrl_8h.md#a90f533d7e297f68fc57deb7230eb5caa)#define M6SDAWIR3\_P62 APOLLO4\_PINMUX(62, 0)

[ 707](ambiq-apollo4-pinctrl_8h.md#a35532f3f55d26f917f35f8c869b2da8f)#define M6MOSI\_P62 APOLLO4\_PINMUX(62, 1)

[ 708](ambiq-apollo4-pinctrl_8h.md#a9fe9215f57faf78c3900b17abaa75060)#define I2S1\_DATA\_P62 APOLLO4\_PINMUX(62, 2)

[ 709](ambiq-apollo4-pinctrl_8h.md#ad8ad98d7206b4d60e9a785270cb6bebd)#define GPIO\_P62 APOLLO4\_PINMUX(62, 3)

[ 710](ambiq-apollo4-pinctrl_8h.md#a4bbc7fa9117624c871eeaf5542f9a6ef)#define UART0RX\_P62 APOLLO4\_PINMUX(62, 4)

[ 711](ambiq-apollo4-pinctrl_8h.md#a3aae4396e8bbda143957f241cb29c3d5)#define UART1RX\_P62 APOLLO4\_PINMUX(62, 5)

[ 712](ambiq-apollo4-pinctrl_8h.md#aeee85894e77cef65275c423c022c7cfb)#define CT62\_P62 APOLLO4\_PINMUX(62, 6)

[ 713](ambiq-apollo4-pinctrl_8h.md#acff3d4c76b5032bc61e0757224cf5c30)#define NCE62\_P62 APOLLO4\_PINMUX(62, 7)

[ 714](ambiq-apollo4-pinctrl_8h.md#abe74dfbe4d685e7867faf149543d7f95)#define OBSBUS14\_P62 APOLLO4\_PINMUX(62, 8)

[ 715](ambiq-apollo4-pinctrl_8h.md#a65dd81097a1b5d661a68f4d6ebc12ffc)#define I2S1\_SDOUT\_P62 APOLLO4\_PINMUX(62, 9)

[ 716](ambiq-apollo4-pinctrl_8h.md#a4d46a4ff07302082e0c37f7126975290)#define I3CM0\_SDA\_P62 APOLLO4\_PINMUX(62, 10)

[ 717](ambiq-apollo4-pinctrl_8h.md#a6d9642f5c84b6e7e2137392ab33c17a2)#define FPIO\_P62 APOLLO4\_PINMUX(62, 11)

[ 718](ambiq-apollo4-pinctrl_8h.md#aa90b1ed2ee15c152674ff9ab0fcc8751)#define M6MISO\_P63 APOLLO4\_PINMUX(63, 0)

[ 719](ambiq-apollo4-pinctrl_8h.md#a6404194582478efd82013055cc616465)#define CLKOUT\_P63 APOLLO4\_PINMUX(63, 1)

[ 720](ambiq-apollo4-pinctrl_8h.md#a1d1ade51f66d32f7e300d9c9ef8e8c22)#define I2S1\_WS\_P63 APOLLO4\_PINMUX(63, 2)

[ 721](ambiq-apollo4-pinctrl_8h.md#a9e7881322451f9c064a827bd26c16aa0)#define GPIO\_P63 APOLLO4\_PINMUX(63, 3)

[ 722](ambiq-apollo4-pinctrl_8h.md#a6f5714bd400231a6e0c3486a366429be)#define UART2RX\_P63 APOLLO4\_PINMUX(63, 4)

[ 723](ambiq-apollo4-pinctrl_8h.md#a57a37a5538bb060040b8ce677a5a0acf)#define UART3RX\_P63 APOLLO4\_PINMUX(63, 5)

[ 724](ambiq-apollo4-pinctrl_8h.md#acaa6fd1a3d6d48343ce736804a829dcd)#define CT63\_P63 APOLLO4\_PINMUX(63, 6)

[ 725](ambiq-apollo4-pinctrl_8h.md#acd4dd1d3133002f0c60426e542702dd3)#define NCE63\_P63 APOLLO4\_PINMUX(63, 7)

[ 726](ambiq-apollo4-pinctrl_8h.md#aa477eb0f144f44127342fe79876eb312)#define OBSBUS15\_P63 APOLLO4\_PINMUX(63, 8)

[ 727](ambiq-apollo4-pinctrl_8h.md#a2b0af95f415445c0dcdf0de6141dbe18)#define DISP\_TE\_P63 APOLLO4\_PINMUX(63, 9)

[ 728](ambiq-apollo4-pinctrl_8h.md#af9399d8ee9ebcd5de28223e054ec9c7c)#define FPIO\_P63 APOLLO4\_PINMUX(63, 11)

[ 729](ambiq-apollo4-pinctrl_8h.md#a5eb14a65a665bd5c304a4953c197b3df)#define MSPI0\_0\_P64 APOLLO4\_PINMUX(64, 0)

[ 730](ambiq-apollo4-pinctrl_8h.md#a445a906a3797a052225c6034214dfe3d)#define XT32KHZ\_P64 APOLLO4\_PINMUX(64, 1)

[ 731](ambiq-apollo4-pinctrl_8h.md#af32f1099cfc946b68a942807b47b07da)#define SWO\_P64 APOLLO4\_PINMUX(64, 2)

[ 732](ambiq-apollo4-pinctrl_8h.md#ac031a8b0e6fe953a329bccae5138864c)#define GPIO\_P64 APOLLO4\_PINMUX(64, 3)

[ 733](ambiq-apollo4-pinctrl_8h.md#a642add8b9bf4332b02893bd170e15a1d)#define UART0RTS\_P64 APOLLO4\_PINMUX(64, 4)

[ 734](ambiq-apollo4-pinctrl_8h.md#aa8caf83f7caf06f55548726c93502081)#define DISP\_D0\_P64 APOLLO4\_PINMUX(64, 5)

[ 735](ambiq-apollo4-pinctrl_8h.md#ab037738d8bf4a5445ad480d872472526)#define CT64\_P64 APOLLO4\_PINMUX(64, 6)

[ 736](ambiq-apollo4-pinctrl_8h.md#af279b091bf1b2e9854cb240fb07d7411)#define NCE64\_P64 APOLLO4\_PINMUX(64, 7)

[ 737](ambiq-apollo4-pinctrl_8h.md#a7046ce33beecfb8727c857baa8ec72b5)#define OBSBUS0\_P64 APOLLO4\_PINMUX(64, 8)

[ 738](ambiq-apollo4-pinctrl_8h.md#affd61d85e8a9701087d1967b9c9b51fd)#define I2S1\_SDIN\_P64 APOLLO4\_PINMUX(64, 9)

[ 739](ambiq-apollo4-pinctrl_8h.md#adf3bd0a15f645a082fd03b74f20d88a1)#define FPIO\_P64 APOLLO4\_PINMUX(64, 11)

[ 740](ambiq-apollo4-pinctrl_8h.md#a9a6887c52100d64cacfef372daa49784)#define MSPI0\_1\_P65 APOLLO4\_PINMUX(65, 0)

[ 741](ambiq-apollo4-pinctrl_8h.md#a90c257cc7e3c833d282e1deb95ffd4c1)#define XT32KHZ\_P65 APOLLO4\_PINMUX(65, 1)

[ 742](ambiq-apollo4-pinctrl_8h.md#aba5cc58aeeebd542cc0c0a3c9cd1faa9)#define SWO\_P65 APOLLO4\_PINMUX(65, 2)

[ 743](ambiq-apollo4-pinctrl_8h.md#ae9af3264c78732b1bc79b552d68dfa6a)#define GPIO\_P65 APOLLO4\_PINMUX(65, 3)

[ 744](ambiq-apollo4-pinctrl_8h.md#a88485f38b483ff295a6865070d6aeaf2)#define UART0CTS\_P65 APOLLO4\_PINMUX(65, 4)

[ 745](ambiq-apollo4-pinctrl_8h.md#a742b70e2ea150b7d33a33a9f12a56cec)#define DISP\_D1\_P65 APOLLO4\_PINMUX(65, 5)

[ 746](ambiq-apollo4-pinctrl_8h.md#a0d16e5df648b12ee088736b9b0cc7a99)#define CT65\_P65 APOLLO4\_PINMUX(65, 6)

[ 747](ambiq-apollo4-pinctrl_8h.md#a4913e8e909a5f53078ec4f73eda5c112)#define NCE65\_P65 APOLLO4\_PINMUX(65, 7)

[ 748](ambiq-apollo4-pinctrl_8h.md#ae32c8688bca5ee426871846ee754feee)#define OBSBUS1\_P65 APOLLO4\_PINMUX(65, 8)

[ 749](ambiq-apollo4-pinctrl_8h.md#a0d737cccfac7769dff176dbee7ece035)#define FPIO\_P65 APOLLO4\_PINMUX(65, 11)

[ 750](ambiq-apollo4-pinctrl_8h.md#a2f0c55cfe304317d856d38b5f42017fb)#define MSPI0\_2\_P66 APOLLO4\_PINMUX(66, 0)

[ 751](ambiq-apollo4-pinctrl_8h.md#a25dea0b9f7b3c72fdd7545a8deef8979)#define CLKOUT\_P66 APOLLO4\_PINMUX(66, 1)

[ 752](ambiq-apollo4-pinctrl_8h.md#a1030cf6dfeae1466daf40e25f9588a65)#define SWO\_P66 APOLLO4\_PINMUX(66, 2)

[ 753](ambiq-apollo4-pinctrl_8h.md#ac82bb9747100752447c61e008d0aed46)#define GPIO\_P66 APOLLO4\_PINMUX(66, 3)

[ 754](ambiq-apollo4-pinctrl_8h.md#a0121e886cde60411b5e993bdb313666d)#define UART0TX\_P66 APOLLO4\_PINMUX(66, 4)

[ 755](ambiq-apollo4-pinctrl_8h.md#aae2a16467e9efa533c27db55b8b75018)#define DISP\_D2\_P66 APOLLO4\_PINMUX(66, 5)

[ 756](ambiq-apollo4-pinctrl_8h.md#a8141663c73d4e99d2771af911744d895)#define CT66\_P66 APOLLO4\_PINMUX(66, 6)

[ 757](ambiq-apollo4-pinctrl_8h.md#acff679577d81e687a56906eebf769bf6)#define NCE66\_P66 APOLLO4\_PINMUX(66, 7)

[ 758](ambiq-apollo4-pinctrl_8h.md#aca89e15806ac74473a750140e063a768)#define OBSBUS2\_P66 APOLLO4\_PINMUX(66, 8)

[ 759](ambiq-apollo4-pinctrl_8h.md#aca6b469fa3310773c34b04cd66d83a3b)#define FPIO\_P66 APOLLO4\_PINMUX(66, 11)

[ 760](ambiq-apollo4-pinctrl_8h.md#ab12e2460e08787e91bf8d83ed001e751)#define MSPI0\_3\_P67 APOLLO4\_PINMUX(67, 0)

[ 761](ambiq-apollo4-pinctrl_8h.md#a3da5a10973565826642c6a4f8b0d9fde)#define CLKOUT\_P67 APOLLO4\_PINMUX(67, 1)

[ 762](ambiq-apollo4-pinctrl_8h.md#aefa221eea5534b3fe844a82ddd059368)#define SWO\_P67 APOLLO4\_PINMUX(67, 2)

[ 763](ambiq-apollo4-pinctrl_8h.md#aa9a6029306499ec2cccbb76899488bf3)#define GPIO\_P67 APOLLO4\_PINMUX(67, 3)

[ 764](ambiq-apollo4-pinctrl_8h.md#a67ed914a3898064c3bef85da1fab7043)#define UART2TX\_P67 APOLLO4\_PINMUX(67, 4)

[ 765](ambiq-apollo4-pinctrl_8h.md#aea9c9aa658bee0a255357dc7a341d670)#define DISP\_D3\_P67 APOLLO4\_PINMUX(67, 5)

[ 766](ambiq-apollo4-pinctrl_8h.md#aba43afb9344060ed13c182be45c83664)#define CT67\_P67 APOLLO4\_PINMUX(67, 6)

[ 767](ambiq-apollo4-pinctrl_8h.md#a94cc174e483db8110ca76fff12629c6d)#define NCE67\_P67 APOLLO4\_PINMUX(67, 7)

[ 768](ambiq-apollo4-pinctrl_8h.md#a81e49f6c74fd26278133b54130301c98)#define OBSBUS3\_P67 APOLLO4\_PINMUX(67, 8)

[ 769](ambiq-apollo4-pinctrl_8h.md#a5b19cb46a8fd13195963c55389bd129f)#define FPIO\_P67 APOLLO4\_PINMUX(67, 11)

[ 770](ambiq-apollo4-pinctrl_8h.md#a42eff1c815d90808aa51ffa788567cde)#define MSPI0\_4\_P68 APOLLO4\_PINMUX(68, 0)

[ 771](ambiq-apollo4-pinctrl_8h.md#a3e3ccb44c9b7b5c6f6fbec5013918444)#define SWO\_P68 APOLLO4\_PINMUX(68, 1)

[ 772](ambiq-apollo4-pinctrl_8h.md#a3e315d2425fb95945b68e7c4e2fe954a)#define GPIO\_P68 APOLLO4\_PINMUX(68, 3)

[ 773](ambiq-apollo4-pinctrl_8h.md#a6400e4e33ad937bb9fa2d8eea2e95b80)#define UART0RX\_P68 APOLLO4\_PINMUX(68, 4)

[ 774](ambiq-apollo4-pinctrl_8h.md#a95cb5744b8fc2cc94bdebe25ce907f2e)#define DISP\_D4\_P68 APOLLO4\_PINMUX(68, 5)

[ 775](ambiq-apollo4-pinctrl_8h.md#a587bb42465e4bc3a702b17ef81763f2d)#define CT68\_P68 APOLLO4\_PINMUX(68, 6)

[ 776](ambiq-apollo4-pinctrl_8h.md#a43db97f86803b04b80140c3c12f096d5)#define NCE68\_P68 APOLLO4\_PINMUX(68, 7)

[ 777](ambiq-apollo4-pinctrl_8h.md#a66e352fbe264a7ff8832be0f12dd8c47)#define OBSBUS4\_P68 APOLLO4\_PINMUX(68, 8)

[ 778](ambiq-apollo4-pinctrl_8h.md#a9453851e39c3b24a0914538e9768930c)#define FPIO\_P68 APOLLO4\_PINMUX(68, 11)

[ 779](ambiq-apollo4-pinctrl_8h.md#a7f7b4970c4a42e5a57b38dc4506c557d)#define MSPI0\_5\_P69 APOLLO4\_PINMUX(69, 0)

[ 780](ambiq-apollo4-pinctrl_8h.md#ab4597feb25612a79db1d271c15ea5a64)#define XT32KHZ\_P69 APOLLO4\_PINMUX(69, 1)

[ 781](ambiq-apollo4-pinctrl_8h.md#a5fa4920fa2af91403279165ec14471c3)#define SWO\_P69 APOLLO4\_PINMUX(69, 2)

[ 782](ambiq-apollo4-pinctrl_8h.md#a5602b2af723fb7fe3bf1121b0577c2e7)#define GPIO\_P69 APOLLO4\_PINMUX(69, 3)

[ 783](ambiq-apollo4-pinctrl_8h.md#ad0e6037b12ce432479dea6c527139ef9)#define UART2RX\_P69 APOLLO4\_PINMUX(69, 4)

[ 784](ambiq-apollo4-pinctrl_8h.md#ad0d9ddca0aa2f26d0f9d11c839540eeb)#define DISP\_D5\_P69 APOLLO4\_PINMUX(69, 5)

[ 785](ambiq-apollo4-pinctrl_8h.md#a3a2e93c32aa06d51b821a71ea38610f9)#define CT69\_P69 APOLLO4\_PINMUX(69, 6)

[ 786](ambiq-apollo4-pinctrl_8h.md#a8e86b1f165b06bde1344f2a0591591f6)#define NCE69\_P69 APOLLO4\_PINMUX(69, 7)

[ 787](ambiq-apollo4-pinctrl_8h.md#a502eecad3a6ae367a857f7c11d9056aa)#define OBSBUS5\_P69 APOLLO4\_PINMUX(69, 8)

[ 788](ambiq-apollo4-pinctrl_8h.md#a9926b5fac2af7c0cd5b4353f2f97c290)#define FPIO\_P69 APOLLO4\_PINMUX(69, 11)

[ 789](ambiq-apollo4-pinctrl_8h.md#a79df6b22d50727502119a1497c2a3bc5)#define MSPI0\_6\_P70 APOLLO4\_PINMUX(70, 0)

[ 790](ambiq-apollo4-pinctrl_8h.md#adc16088791f6cfac9094ea7b1541c1fe)#define XT32KHZ\_P70 APOLLO4\_PINMUX(70, 1)

[ 791](ambiq-apollo4-pinctrl_8h.md#a156872c8ae579fd7eb414864f5e59d3c)#define SWTRACE0\_P70 APOLLO4\_PINMUX(70, 2)

[ 792](ambiq-apollo4-pinctrl_8h.md#af1f938f04fe3670874c371bfff680c41)#define GPIO\_P70 APOLLO4\_PINMUX(70, 3)

[ 793](ambiq-apollo4-pinctrl_8h.md#a82bf8761043125656dfdf51377e60659)#define UART0RTS\_P70 APOLLO4\_PINMUX(70, 4)

[ 794](ambiq-apollo4-pinctrl_8h.md#a22557582f75a08d1cdfc4f1230897b95)#define DISP\_D6\_P70 APOLLO4\_PINMUX(70, 5)

[ 795](ambiq-apollo4-pinctrl_8h.md#a2511ff178000fcb8fe549dde05a865be)#define CT70\_P70 APOLLO4\_PINMUX(70, 6)

[ 796](ambiq-apollo4-pinctrl_8h.md#a154b9a05cda9e8a41f84f82417a60d81)#define NCE70\_P70 APOLLO4\_PINMUX(70, 7)

[ 797](ambiq-apollo4-pinctrl_8h.md#a213ad33569c9e4b5b885ebc32d2c6eb8)#define OBSBUS6\_P70 APOLLO4\_PINMUX(70, 8)

[ 798](ambiq-apollo4-pinctrl_8h.md#aedba8e337254fdf90ca0153f140b7fea)#define FPIO\_P70 APOLLO4\_PINMUX(70, 11)

[ 799](ambiq-apollo4-pinctrl_8h.md#aa3fc9a751395095d0ae7bddb4fcf3a08)#define MSPI0\_7\_P71 APOLLO4\_PINMUX(71, 0)

[ 800](ambiq-apollo4-pinctrl_8h.md#a84da102239574c1e60383e757ea29320)#define CLKOUT\_P71 APOLLO4\_PINMUX(71, 1)

[ 801](ambiq-apollo4-pinctrl_8h.md#ae2c888114aaca99a8da964b17ebef8f2)#define SWTRACE1\_P71 APOLLO4\_PINMUX(71, 2)

[ 802](ambiq-apollo4-pinctrl_8h.md#a88cfa6b114b0efb7bfeec35a4110727d)#define GPIO\_P71 APOLLO4\_PINMUX(71, 3)

[ 803](ambiq-apollo4-pinctrl_8h.md#a395a4af5545ed53aed51c27256767f18)#define UART0CTS\_P71 APOLLO4\_PINMUX(71, 4)

[ 804](ambiq-apollo4-pinctrl_8h.md#a7f7e778c6f74e2ac5749c64ebc5b1242)#define DISP\_D7\_P71 APOLLO4\_PINMUX(71, 5)

[ 805](ambiq-apollo4-pinctrl_8h.md#a4c85eaf43ab70722fdcaa03da0d765ba)#define CT71\_P71 APOLLO4\_PINMUX(71, 6)

[ 806](ambiq-apollo4-pinctrl_8h.md#a04df6aa292fc65e77cc4de70b36d3d95)#define NCE71\_P71 APOLLO4\_PINMUX(71, 7)

[ 807](ambiq-apollo4-pinctrl_8h.md#aa6124c105b0f3a3212153357f20372fd)#define OBSBUS7\_P71 APOLLO4\_PINMUX(71, 8)

[ 808](ambiq-apollo4-pinctrl_8h.md#a09ec357d810ff4a1ad2b568f228fa517)#define FPIO\_P71 APOLLO4\_PINMUX(71, 11)

[ 809](ambiq-apollo4-pinctrl_8h.md#a7ae06a213537e3b83509f03f3fe2e23f)#define MSPI0\_8\_P72 APOLLO4\_PINMUX(72, 0)

[ 810](ambiq-apollo4-pinctrl_8h.md#aa309036617b1c7cbe5ab264f09d346d3)#define CLKOUT\_P72 APOLLO4\_PINMUX(72, 1)

[ 811](ambiq-apollo4-pinctrl_8h.md#a646bb647854f3cdd1993cf4d5d6d2c8e)#define SWTRACE2\_P72 APOLLO4\_PINMUX(72, 2)

[ 812](ambiq-apollo4-pinctrl_8h.md#adcf84a78ff2d8532d87482678ba2df80)#define GPIO\_P72 APOLLO4\_PINMUX(72, 3)

[ 813](ambiq-apollo4-pinctrl_8h.md#ae68adb841018f98375b7022e370aba0c)#define UART0TX\_P72 APOLLO4\_PINMUX(72, 4)

[ 814](ambiq-apollo4-pinctrl_8h.md#a77f962529828b50b6d49b9fc963f0915)#define DISP\_D8\_P72 APOLLO4\_PINMUX(72, 5)

[ 815](ambiq-apollo4-pinctrl_8h.md#a1ece747b9f8bbc75833d31a85d14cb57)#define CT72\_P72 APOLLO4\_PINMUX(72, 6)

[ 816](ambiq-apollo4-pinctrl_8h.md#a89192a0beda2cecdd53e4fd7174302e5)#define NCE72\_P72 APOLLO4\_PINMUX(72, 7)

[ 817](ambiq-apollo4-pinctrl_8h.md#a239f7846dcaf72a6023075cf8b0e2a4d)#define OBSBUS8\_P72 APOLLO4\_PINMUX(72, 8)

[ 818](ambiq-apollo4-pinctrl_8h.md#af7e3a29ea173aad99e2547fd40411324)#define VCMPO\_P72 APOLLO4\_PINMUX(72, 9)

[ 819](ambiq-apollo4-pinctrl_8h.md#a5579afd18de209160b6a138f4379ae91)#define FPIO\_P72 APOLLO4\_PINMUX(72, 11)

[ 820](ambiq-apollo4-pinctrl_8h.md#a962c3342715fb4b5377b15020ef14f3a)#define MSPI0\_9\_P73 APOLLO4\_PINMUX(73, 0)

[ 821](ambiq-apollo4-pinctrl_8h.md#af1b54837328f5f53e4d078bc84dd2081)#define SWTRACE3\_P73 APOLLO4\_PINMUX(73, 2)

[ 822](ambiq-apollo4-pinctrl_8h.md#a284f44425e1437643fad644c5f538b09)#define GPIO\_P73 APOLLO4\_PINMUX(73, 3)

[ 823](ambiq-apollo4-pinctrl_8h.md#a0bf298468957f997dfbf8f836a113359)#define UART2TX\_P73 APOLLO4\_PINMUX(73, 4)

[ 824](ambiq-apollo4-pinctrl_8h.md#a31c1a6680673ebe90be059efdd42f723)#define DISP\_D9\_P73 APOLLO4\_PINMUX(73, 5)

[ 825](ambiq-apollo4-pinctrl_8h.md#a0051d3c2e8f4a00b331fd04400a3fe12)#define CT73\_P73 APOLLO4\_PINMUX(73, 6)

[ 826](ambiq-apollo4-pinctrl_8h.md#a86228f8d9adc8065f76ca1f0af512d50)#define NCE73\_P73 APOLLO4\_PINMUX(73, 7)

[ 827](ambiq-apollo4-pinctrl_8h.md#a61ae81253439e142027c2bf80052ff79)#define OBSBUS9\_P73 APOLLO4\_PINMUX(73, 8)

[ 828](ambiq-apollo4-pinctrl_8h.md#a8ecf38aa17aec0cf39ee7060fa2e7a69)#define FPIO\_P73 APOLLO4\_PINMUX(73, 11)

[ 829](ambiq-apollo4-pinctrl_8h.md#ab429b2ec54bc0715dbb3f94a9da408b6)#define MSPI2\_0\_P74 APOLLO4\_PINMUX(74, 0)

[ 830](ambiq-apollo4-pinctrl_8h.md#a2b2f9e4968017262cb690e00f32471c7)#define DISP\_QSPI\_D0\_OUT\_P74 APOLLO4\_PINMUX(74, 1)

[ 831](ambiq-apollo4-pinctrl_8h.md#a726c9698937d4fed1c5db076eaa914fe)#define DISP\_QSPI\_D0\_P74 APOLLO4\_PINMUX(74, 2)

[ 832](ambiq-apollo4-pinctrl_8h.md#a996341cb730ac8810838e3b45a46fd3f)#define GPIO\_P74 APOLLO4\_PINMUX(74, 3)

[ 833](ambiq-apollo4-pinctrl_8h.md#a69bcd0a4f24a6d766cba9a4f5035ced1)#define UART0RX\_P74 APOLLO4\_PINMUX(74, 4)

[ 834](ambiq-apollo4-pinctrl_8h.md#af78787da15205378db0431cf38a2fe19)#define DISP\_D10\_P74 APOLLO4\_PINMUX(74, 5)

[ 835](ambiq-apollo4-pinctrl_8h.md#a61fde9f72bcc561db7bb000cde08f1dd)#define CT74\_P74 APOLLO4\_PINMUX(74, 6)

[ 836](ambiq-apollo4-pinctrl_8h.md#ad28d500779368b859fbc6975ad09cbac)#define NCE74\_P74 APOLLO4\_PINMUX(74, 7)

[ 837](ambiq-apollo4-pinctrl_8h.md#a3bf2acee5564563d94e424ca119e8ddc)#define OBSBUS10\_P74 APOLLO4\_PINMUX(74, 8)

[ 838](ambiq-apollo4-pinctrl_8h.md#a4d954181a328dd4f1bb6959c04f43567)#define DISP\_SPI\_SD\_P74 APOLLO4\_PINMUX(74, 9)

[ 839](ambiq-apollo4-pinctrl_8h.md#a6e6032ce71d5c93f2bd7166f74ab561e)#define DISP\_SPI\_SDO\_P74 APOLLO4\_PINMUX(74, 10)

[ 840](ambiq-apollo4-pinctrl_8h.md#adad0a7ce06abec5ac1309105e7f99a14)#define FPIO\_P74 APOLLO4\_PINMUX(74, 11)

[ 841](ambiq-apollo4-pinctrl_8h.md#a042bfeb9f98def18e11885ebca1ac88b)#define MSPI2\_1\_P75 APOLLO4\_PINMUX(75, 0)

[ 842](ambiq-apollo4-pinctrl_8h.md#a6ad643261b65f7d941abda1f46f44773)#define XT32KHZ\_P75 APOLLO4\_PINMUX(75, 1)

[ 843](ambiq-apollo4-pinctrl_8h.md#a8f0a91961665fb0256f6f456d6311a46)#define DISP\_QSPI\_D1\_P75 APOLLO4\_PINMUX(75, 2)

[ 844](ambiq-apollo4-pinctrl_8h.md#adc0f2e9ef00c8e7ef5a2280d80b96c15)#define GPIO\_P75 APOLLO4\_PINMUX(75, 3)

[ 845](ambiq-apollo4-pinctrl_8h.md#a0dff38c9b31213c0d4d295bf3e958977)#define UART2RX\_P75 APOLLO4\_PINMUX(75, 4)

[ 846](ambiq-apollo4-pinctrl_8h.md#a4e06aed320070c12ddd60dbdaf9fb199)#define DISP\_D11\_P75 APOLLO4\_PINMUX(75, 5)

[ 847](ambiq-apollo4-pinctrl_8h.md#a742d7c73593541029d2d54cce6475a74)#define CT75\_P75 APOLLO4\_PINMUX(75, 6)

[ 848](ambiq-apollo4-pinctrl_8h.md#a9d5c69924941be438cb5f8e2dc7d9621)#define NCE75\_P75 APOLLO4\_PINMUX(75, 7)

[ 849](ambiq-apollo4-pinctrl_8h.md#ac97fe090926d45f3225440ac08ceaf0d)#define OBSBUS11\_P75 APOLLO4\_PINMUX(75, 8)

[ 850](ambiq-apollo4-pinctrl_8h.md#a0594228a171ecb21ec08bc24c30485fc)#define DISP\_SPI\_DCX\_P75 APOLLO4\_PINMUX(75, 9)

[ 851](ambiq-apollo4-pinctrl_8h.md#a82c10a35b735878245c09519fb1ae9ef)#define FPIO\_P75 APOLLO4\_PINMUX(75, 11)

[ 852](ambiq-apollo4-pinctrl_8h.md#aae49a256d809efd10fcc56e730229417)#define MSPI2\_2\_P76 APOLLO4\_PINMUX(76, 0)

[ 853](ambiq-apollo4-pinctrl_8h.md#a2051e97aa7c29746bc79cc6c069255d7)#define XT32KHZ\_P76 APOLLO4\_PINMUX(76, 1)

[ 854](ambiq-apollo4-pinctrl_8h.md#a9b14276a635d685cd45fd501541ff535)#define DISP\_QSPI\_D2\_P76 APOLLO4\_PINMUX(76, 2)

[ 855](ambiq-apollo4-pinctrl_8h.md#a43ba9ebbf5246036129b77e0dd3bc991)#define GPIO\_P76 APOLLO4\_PINMUX(76, 3)

[ 856](ambiq-apollo4-pinctrl_8h.md#ac26b9423d352238ebb0ad939ce54eb8b)#define UART0RTS\_P76 APOLLO4\_PINMUX(76, 4)

[ 857](ambiq-apollo4-pinctrl_8h.md#a7ba66e271f8c8572fe3b68cd7a0b4e89)#define DISP\_D12\_P76 APOLLO4\_PINMUX(76, 5)

[ 858](ambiq-apollo4-pinctrl_8h.md#a4af157a2b3a2154dfbe4393b8b53aa6b)#define CT76\_P76 APOLLO4\_PINMUX(76, 6)

[ 859](ambiq-apollo4-pinctrl_8h.md#af6c8fade1d21768d9efa32b01ae4ef38)#define NCE76\_P76 APOLLO4\_PINMUX(76, 7)

[ 860](ambiq-apollo4-pinctrl_8h.md#aecda03e317007759a513adf403d67646)#define OBSBUS12\_P76 APOLLO4\_PINMUX(76, 8)

[ 861](ambiq-apollo4-pinctrl_8h.md#a3aed33db5d85afb482c04742ab16141a)#define FPIO\_P76 APOLLO4\_PINMUX(76, 11)

[ 862](ambiq-apollo4-pinctrl_8h.md#a9799e2d60b3a196b88b5d651a7310e0f)#define MSPI2\_3\_P77 APOLLO4\_PINMUX(77, 0)

[ 863](ambiq-apollo4-pinctrl_8h.md#a39dbe080b7a91e8b928fd8d7e4b5859d)#define DISP\_QSPI\_D3\_P77 APOLLO4\_PINMUX(77, 2)

[ 864](ambiq-apollo4-pinctrl_8h.md#ad493f67ac5b8d7c2c38fc6342fcb0668)#define GPIO\_P77 APOLLO4\_PINMUX(77, 3)

[ 865](ambiq-apollo4-pinctrl_8h.md#ae9530f48132c5c9b79922fa1cb001ece)#define UART0CTS\_P77 APOLLO4\_PINMUX(77, 4)

[ 866](ambiq-apollo4-pinctrl_8h.md#afe485208797cb04fbe47699eec54b878)#define DISP\_D13\_P77 APOLLO4\_PINMUX(77, 5)

[ 867](ambiq-apollo4-pinctrl_8h.md#af7431368e4bb3ab5b787aff193c4f08f)#define CT77\_P77 APOLLO4\_PINMUX(77, 6)

[ 868](ambiq-apollo4-pinctrl_8h.md#a7a76a1afd802628cacf13dcb518c2e91)#define NCE77\_P77 APOLLO4\_PINMUX(77, 7)

[ 869](ambiq-apollo4-pinctrl_8h.md#a8715730c82c93d1f675a4a598ba63eb3)#define OBSBUS13\_P77 APOLLO4\_PINMUX(77, 8)

[ 870](ambiq-apollo4-pinctrl_8h.md#ad2ad7702451f3e6adeb0e0824d539817)#define FPIO\_P77 APOLLO4\_PINMUX(77, 11)

[ 871](ambiq-apollo4-pinctrl_8h.md#a73af6a563f3ae083f0009526440af410)#define MSPI2\_4\_P78 APOLLO4\_PINMUX(78, 0)

[ 872](ambiq-apollo4-pinctrl_8h.md#a6a20564839564695461d313a9a2a94ed)#define DISP\_QSPI\_SCK\_P78 APOLLO4\_PINMUX(78, 2)

[ 873](ambiq-apollo4-pinctrl_8h.md#af34a3c1e8708263d26bd473382a9161f)#define GPIO\_P78 APOLLO4\_PINMUX(78, 3)

[ 874](ambiq-apollo4-pinctrl_8h.md#a2980e3d0fe5a476b5e49072e633a4036)#define UART0TX\_P78 APOLLO4\_PINMUX(78, 4)

[ 875](ambiq-apollo4-pinctrl_8h.md#a6788dd9813d1c3a12e0a06b9931c922f)#define DISP\_D14\_P78 APOLLO4\_PINMUX(78, 5)

[ 876](ambiq-apollo4-pinctrl_8h.md#a1e9004d8a0a08b76b962fb3cc5b1b403)#define CT78\_P78 APOLLO4\_PINMUX(78, 6)

[ 877](ambiq-apollo4-pinctrl_8h.md#a34e6442dbe0e9716b0e7b2c4557ad3ec)#define NCE78\_P78 APOLLO4\_PINMUX(78, 7)

[ 878](ambiq-apollo4-pinctrl_8h.md#a279e5af6103ccf038765c3982cd1cacd)#define OBSBUS14\_P78 APOLLO4\_PINMUX(78, 8)

[ 879](ambiq-apollo4-pinctrl_8h.md#af21d007424f12a9a410dcdf0609a35a5)#define DISP\_SPI\_SCK\_P78 APOLLO4\_PINMUX(78, 9)

[ 880](ambiq-apollo4-pinctrl_8h.md#a2b920e7396f4592485c70c51a431cc57)#define FPIO\_P78 APOLLO4\_PINMUX(78, 11)

[ 881](ambiq-apollo4-pinctrl_8h.md#a46e4ed9ab4b3314025fa9ef881bb5ef8)#define MSPI2\_5\_P79 APOLLO4\_PINMUX(79, 0)

[ 882](ambiq-apollo4-pinctrl_8h.md#aec99fc5f46a3bfd34514de5506d64d60)#define SDIF\_DAT4\_P79 APOLLO4\_PINMUX(79, 2)

[ 883](ambiq-apollo4-pinctrl_8h.md#a7e260d85e5509a68d6b6ac9c9469cbed)#define GPIO\_P79 APOLLO4\_PINMUX(79, 3)

[ 884](ambiq-apollo4-pinctrl_8h.md#a8b880883280de9fd8eb956bfc4c8f4e5)#define SWO\_P79 APOLLO4\_PINMUX(79, 4)

[ 885](ambiq-apollo4-pinctrl_8h.md#a11f9a4a1e251e329ccb6ddf410243d5d)#define DISP\_VS\_P79 APOLLO4\_PINMUX(79, 5)

[ 886](ambiq-apollo4-pinctrl_8h.md#a989b7a09a00a487a2ed1e98efeda422c)#define CT79\_P79 APOLLO4\_PINMUX(79, 6)

[ 887](ambiq-apollo4-pinctrl_8h.md#a0c3722570b48a0e84fd6e599d765b14e)#define NCE79\_P79 APOLLO4\_PINMUX(79, 7)

[ 888](ambiq-apollo4-pinctrl_8h.md#a072360a1c54d1af1c4046d7af0fa9793)#define OBSBUS15\_P79 APOLLO4\_PINMUX(79, 8)

[ 889](ambiq-apollo4-pinctrl_8h.md#a4692635f820f5fdef8d0cb4dced9cd31)#define DISP\_SPI\_SDI\_P79 APOLLO4\_PINMUX(79, 9)

[ 890](ambiq-apollo4-pinctrl_8h.md#a6dc87fd84b1b165c57ae59cf2abf88b0)#define FPIO\_P79 APOLLO4\_PINMUX(79, 11)

[ 891](ambiq-apollo4-pinctrl_8h.md#a202daf7f1a802ffd9302bd4a944f6dde)#define MSPI2\_6\_P80 APOLLO4\_PINMUX(80, 0)

[ 892](ambiq-apollo4-pinctrl_8h.md#a0bffd06032dfd164774068791da00b37)#define CLKOUT\_P80 APOLLO4\_PINMUX(80, 1)

[ 893](ambiq-apollo4-pinctrl_8h.md#a868de6af380160672994dbb1eeb31dc7)#define SDIF\_DAT5\_P80 APOLLO4\_PINMUX(80, 2)

[ 894](ambiq-apollo4-pinctrl_8h.md#ab1e4fc0335724412d83c0d6eb7cc5a9c)#define GPIO\_P80 APOLLO4\_PINMUX(80, 3)

[ 895](ambiq-apollo4-pinctrl_8h.md#a4267aa4aa88cf6ece0dc73cd3d5966f7)#define SWTRACE0\_P80 APOLLO4\_PINMUX(80, 4)

[ 896](ambiq-apollo4-pinctrl_8h.md#a49ac25c33fbb5b9c01860883b74122a3)#define DISP\_HS\_P80 APOLLO4\_PINMUX(80, 5)

[ 897](ambiq-apollo4-pinctrl_8h.md#a83df0f39280b02d67afd15fa6d6dbdb0)#define CT80\_P80 APOLLO4\_PINMUX(80, 6)

[ 898](ambiq-apollo4-pinctrl_8h.md#a819fac8206d6216a1b407ea4980b3092)#define NCE80\_P80 APOLLO4\_PINMUX(80, 7)

[ 899](ambiq-apollo4-pinctrl_8h.md#a8b3bda5935f620002b707dfe3fc43d67)#define OBSBUS0\_P80 APOLLO4\_PINMUX(80, 8)

[ 900](ambiq-apollo4-pinctrl_8h.md#a0f875414131055069b01d6d5025b837c)#define FPIO\_P80 APOLLO4\_PINMUX(80, 11)

[ 901](ambiq-apollo4-pinctrl_8h.md#a0c3eb645bf396166df81c3f0f08d8ea6)#define MSPI2\_7\_P81 APOLLO4\_PINMUX(81, 0)

[ 902](ambiq-apollo4-pinctrl_8h.md#a043869863b36fd65b0d0c5cb2881e122)#define CLKOUT\_P81 APOLLO4\_PINMUX(81, 1)

[ 903](ambiq-apollo4-pinctrl_8h.md#af192ae3617afab97e4dd5ded499c8344)#define SDIF\_DAT6\_P81 APOLLO4\_PINMUX(81, 2)

[ 904](ambiq-apollo4-pinctrl_8h.md#a7a6a5da8b3f9cc85ec70d3497610bd5e)#define GPIO\_P81 APOLLO4\_PINMUX(81, 3)

[ 905](ambiq-apollo4-pinctrl_8h.md#a0ac68a5b46d8ad1fb4ab214d8ec9fa84)#define SWTRACE1\_P81 APOLLO4\_PINMUX(81, 4)

[ 906](ambiq-apollo4-pinctrl_8h.md#a7eb02d24661e40d91611e52ffe499ef3)#define DISP\_DE\_P81 APOLLO4\_PINMUX(81, 5)

[ 907](ambiq-apollo4-pinctrl_8h.md#af0ef505a22d0108767ee34c3617faff4)#define CT81\_P81 APOLLO4\_PINMUX(81, 6)

[ 908](ambiq-apollo4-pinctrl_8h.md#aac5895b6ef5a4f303753c105753808f6)#define NCE81\_P81 APOLLO4\_PINMUX(81, 7)

[ 909](ambiq-apollo4-pinctrl_8h.md#a6ea1025d519788d428f2c04a00e65571)#define OBSBUS1\_P81 APOLLO4\_PINMUX(81, 8)

[ 910](ambiq-apollo4-pinctrl_8h.md#a9ad3fba98038e31f8161083f72649a82)#define FPIO\_P81 APOLLO4\_PINMUX(81, 11)

[ 911](ambiq-apollo4-pinctrl_8h.md#a3b8f85ab84354877defc9b8bbef391ac)#define MSPI2\_8\_P82 APOLLO4\_PINMUX(82, 0)

[ 912](ambiq-apollo4-pinctrl_8h.md#a6155820134a9cac0de16e4d2bd4c7870)#define XT32KHZ\_P82 APOLLO4\_PINMUX(82, 1)

[ 913](ambiq-apollo4-pinctrl_8h.md#aaffc5f5fc338ea01a7ce96bb717c6808)#define SDIF\_DAT7\_P82 APOLLO4\_PINMUX(82, 2)

[ 914](ambiq-apollo4-pinctrl_8h.md#ae38ce053d72e62b1a1299b1f71c9bf17)#define GPIO\_P82 APOLLO4\_PINMUX(82, 3)

[ 915](ambiq-apollo4-pinctrl_8h.md#ad7593ef212f9442924c8ea4cc090a7b2)#define SWTRACE2\_P82 APOLLO4\_PINMUX(82, 4)

[ 916](ambiq-apollo4-pinctrl_8h.md#aea6d285f4dfb7bf759c8b721657e15cc)#define DISP\_PCLK\_P82 APOLLO4\_PINMUX(82, 5)

[ 917](ambiq-apollo4-pinctrl_8h.md#aca3c69e423a090dc53ec24aeaa505ad2)#define CT82\_P82 APOLLO4\_PINMUX(82, 6)

[ 918](ambiq-apollo4-pinctrl_8h.md#ae92d0afe9ae9105a683ad94a2a7a3a5a)#define NCE82\_P82 APOLLO4\_PINMUX(82, 7)

[ 919](ambiq-apollo4-pinctrl_8h.md#a7e3f42512acdce4b95988393e3c0dd45)#define OBSBUS2\_P82 APOLLO4\_PINMUX(82, 8)

[ 920](ambiq-apollo4-pinctrl_8h.md#a368dd58caea0911496e241839b6eb995)#define FPIO\_P82 APOLLO4\_PINMUX(82, 11)

[ 921](ambiq-apollo4-pinctrl_8h.md#a9f193819c40a1d926cff4bcbd2e452e9)#define MSPI2\_9\_P83 APOLLO4\_PINMUX(83, 0)

[ 922](ambiq-apollo4-pinctrl_8h.md#ad2320c1a312f5cb681ee8f0db3dd9e2e)#define XT32KHZ\_P83 APOLLO4\_PINMUX(83, 1)

[ 923](ambiq-apollo4-pinctrl_8h.md#a54f85a328014c0a520e7208f0929aaf5)#define SDIF\_CMD\_P83 APOLLO4\_PINMUX(83, 2)

[ 924](ambiq-apollo4-pinctrl_8h.md#afe99b060d26eac1dc20ebb8ef0af5c42)#define GPIO\_P83 APOLLO4\_PINMUX(83, 3)

[ 925](ambiq-apollo4-pinctrl_8h.md#a4e0957f0ea1ca7f5b4a71d857204dc20)#define SWTRACE3\_P83 APOLLO4\_PINMUX(83, 4)

[ 926](ambiq-apollo4-pinctrl_8h.md#aa1e56bca4c78e91f8efdb4dc6b60db1e)#define DISP\_SD\_P83 APOLLO4\_PINMUX(83, 5)

[ 927](ambiq-apollo4-pinctrl_8h.md#a2d84fe4db603ea92ae308b70297760bb)#define CT83\_P83 APOLLO4\_PINMUX(83, 6)

[ 928](ambiq-apollo4-pinctrl_8h.md#a76fae66ad8df2a195a5014967a85669f)#define NCE83\_P83 APOLLO4\_PINMUX(83, 7)

[ 929](ambiq-apollo4-pinctrl_8h.md#afb9a42fcf793d644a541995bc644ad67)#define OBSBUS3\_P83 APOLLO4\_PINMUX(83, 8)

[ 930](ambiq-apollo4-pinctrl_8h.md#ae0078abf6d34523cb0765b7c5f688a48)#define FPIO\_P83 APOLLO4\_PINMUX(83, 11)

[ 931](ambiq-apollo4-pinctrl_8h.md#ad5d30bd7ebb26460a8ed862789bcbbd0)#define SDIF\_DAT0\_P84 APOLLO4\_PINMUX(84, 2)

[ 932](ambiq-apollo4-pinctrl_8h.md#a71d2d5931c4faa1288218304835176cf)#define GPIO\_P84 APOLLO4\_PINMUX(84, 3)

[ 933](ambiq-apollo4-pinctrl_8h.md#a4c39c3696fd1f9d5246cd90b0dadd78f)#define CT84\_P84 APOLLO4\_PINMUX(84, 6)

[ 934](ambiq-apollo4-pinctrl_8h.md#a7144de3b3ddef6cb618fc5ee9ce9870c)#define NCE84\_P84 APOLLO4\_PINMUX(84, 7)

[ 935](ambiq-apollo4-pinctrl_8h.md#a9fbd5b572f01c8c432af528e449b6e80)#define OBSBUS4\_P84 APOLLO4\_PINMUX(84, 8)

[ 936](ambiq-apollo4-pinctrl_8h.md#ae42723727fdb6b29d7e2c5ab5dd47b21)#define FPIO\_P84 APOLLO4\_PINMUX(84, 11)

[ 937](ambiq-apollo4-pinctrl_8h.md#a35166c0f14e8ba3572dcc0e8e5148ac7)#define SDIF\_DAT1\_P85 APOLLO4\_PINMUX(85, 2)

[ 938](ambiq-apollo4-pinctrl_8h.md#a7ca8aa76d3e5db937e1f050bd65339d3)#define GPIO\_P85 APOLLO4\_PINMUX(85, 3)

[ 939](ambiq-apollo4-pinctrl_8h.md#a9b1a31f9e2beaf79d382f50774b6f451)#define CT85\_P85 APOLLO4\_PINMUX(85, 6)

[ 940](ambiq-apollo4-pinctrl_8h.md#ae0aa674f66c6228d09d87413ac3490e7)#define NCE85\_P85 APOLLO4\_PINMUX(85, 7)

[ 941](ambiq-apollo4-pinctrl_8h.md#acbc47bad7dfa118491ce64f06d8008eb)#define OBSBUS5\_P85 APOLLO4\_PINMUX(85, 8)

[ 942](ambiq-apollo4-pinctrl_8h.md#a478611851ac85fa78bef6a9a73780cd3)#define FPIO\_P85 APOLLO4\_PINMUX(85, 11)

[ 943](ambiq-apollo4-pinctrl_8h.md#a8cfb55519858ed8e93889136a7119122)#define SDIF\_DAT2\_P86 APOLLO4\_PINMUX(86, 2)

[ 944](ambiq-apollo4-pinctrl_8h.md#a07bb8ce75d69d33dd79dd9fd49af2bbb)#define GPIO\_P86 APOLLO4\_PINMUX(86, 3)

[ 945](ambiq-apollo4-pinctrl_8h.md#af65646d399d3bdef24735a66989b8a55)#define CT86\_P86 APOLLO4\_PINMUX(86, 6)

[ 946](ambiq-apollo4-pinctrl_8h.md#a0aeb22d3f8580cead72f932f2726ed71)#define NCE86\_P86 APOLLO4\_PINMUX(86, 7)

[ 947](ambiq-apollo4-pinctrl_8h.md#a09910b22007c3fabe7cec24ba486c52f)#define OBSBUS6\_P86 APOLLO4\_PINMUX(86, 8)

[ 948](ambiq-apollo4-pinctrl_8h.md#a746cf9aa7d3e536e57dffb7295bd89ae)#define FPIO\_P86 APOLLO4\_PINMUX(86, 11)

[ 949](ambiq-apollo4-pinctrl_8h.md#a480616a38a9c88b7f4e3f78d0eb1c018)#define SDIF\_DAT3\_P87 APOLLO4\_PINMUX(87, 2)

[ 950](ambiq-apollo4-pinctrl_8h.md#a122af08a785e25c1a3010861cbfc528b)#define GPIO\_P87 APOLLO4\_PINMUX(87, 3)

[ 951](ambiq-apollo4-pinctrl_8h.md#a6957b23da3c4735a87edc97cabc48dc7)#define CT87\_P87 APOLLO4\_PINMUX(87, 6)

[ 952](ambiq-apollo4-pinctrl_8h.md#a1aefe32ebc07be0719faee0cc28a0c0e)#define NCE87\_P87 APOLLO4\_PINMUX(87, 7)

[ 953](ambiq-apollo4-pinctrl_8h.md#a089d5d74bcef41deeaf6bb9f7c2e5d19)#define OBSBUS7\_P87 APOLLO4\_PINMUX(87, 8)

[ 954](ambiq-apollo4-pinctrl_8h.md#a9f8db20a0209362b20eaab5cb1be1cf8)#define DISP\_TE\_P87 APOLLO4\_PINMUX(87, 9)

[ 955](ambiq-apollo4-pinctrl_8h.md#a3e013b97f1f69465452a044471fa1d1b)#define FPIO\_P87 APOLLO4\_PINMUX(87, 11)

[ 956](ambiq-apollo4-pinctrl_8h.md#acba7f60ff4a91e8b53d7072576a6a883)#define SDIF\_CLKOUT\_P88 APOLLO4\_PINMUX(88, 2)

[ 957](ambiq-apollo4-pinctrl_8h.md#a7d34e0e921ee68ab8f8ee8beeb83f6ce)#define GPIO\_P88 APOLLO4\_PINMUX(88, 3)

[ 958](ambiq-apollo4-pinctrl_8h.md#aebd1f6e78f461f2a14b72214d12806a3)#define CT88\_P88 APOLLO4\_PINMUX(88, 6)

[ 959](ambiq-apollo4-pinctrl_8h.md#abd43111df13f60681904f903f8328a47)#define NCE88\_P88 APOLLO4\_PINMUX(88, 7)

[ 960](ambiq-apollo4-pinctrl_8h.md#adfe02ce3348e9f69e9ca7186ec9697e3)#define OBSBUS8\_P88 APOLLO4\_PINMUX(88, 8)

[ 961](ambiq-apollo4-pinctrl_8h.md#adc5cedfdd914333ff5005c42876088b3)#define FPIO\_P88 APOLLO4\_PINMUX(88, 11)

[ 962](ambiq-apollo4-pinctrl_8h.md#a0843dced9589590510aca3a9aa4948c8)#define GPIO\_P89 APOLLO4\_PINMUX(89, 3)

[ 963](ambiq-apollo4-pinctrl_8h.md#a4c28cda0cc8772fcd8e750971c3fe9f2)#define DISP\_CM\_P89 APOLLO4\_PINMUX(89, 5)

[ 964](ambiq-apollo4-pinctrl_8h.md#a35db12c3877d9665862b8f7924080d5c)#define CT89\_P89 APOLLO4\_PINMUX(89, 6)

[ 965](ambiq-apollo4-pinctrl_8h.md#a11921dee98c8f08895863aa91ec12f95)#define NCE89\_P89 APOLLO4\_PINMUX(89, 7)

[ 966](ambiq-apollo4-pinctrl_8h.md#a9e8a50ad70a9c3e4ee75bfbcb4928bb9)#define OBSBUS9\_P89 APOLLO4\_PINMUX(89, 8)

[ 967](ambiq-apollo4-pinctrl_8h.md#af1c6acb635f837aeea6c17ec6eabba03)#define FPIO\_P89 APOLLO4\_PINMUX(89, 11)

[ 968](ambiq-apollo4-pinctrl_8h.md#ab8b8687ee25b90a1bab3c68edb40320b)#define GPIO\_P90 APOLLO4\_PINMUX(90, 3)

[ 969](ambiq-apollo4-pinctrl_8h.md#a046031e442a2d4d594f8decbe5a0e7ed)#define CT90\_P90 APOLLO4\_PINMUX(90, 6)

[ 970](ambiq-apollo4-pinctrl_8h.md#ab5a27a871d48cc1db46a2cd8a9e8d84f)#define NCE90\_P90 APOLLO4\_PINMUX(90, 7)

[ 971](ambiq-apollo4-pinctrl_8h.md#a753f69a7807fd22c17becf9efcb95091)#define OBSBUS10\_P90 APOLLO4\_PINMUX(90, 8)

[ 972](ambiq-apollo4-pinctrl_8h.md#a26e9b386464a6b9c2ea98a7ac26749ba)#define VCMPO\_P90 APOLLO4\_PINMUX(90, 9)

[ 973](ambiq-apollo4-pinctrl_8h.md#a9c1858783135de4b3bfa818ebaa0fd16)#define FPIO\_P90 APOLLO4\_PINMUX(90, 11)

[ 974](ambiq-apollo4-pinctrl_8h.md#aab06874417401af755658adcde9d471b)#define GPIO\_P91 APOLLO4\_PINMUX(91, 3)

[ 975](ambiq-apollo4-pinctrl_8h.md#a422e463f883a72771b7ff85ea0737d73)#define CT91\_P91 APOLLO4\_PINMUX(91, 6)

[ 976](ambiq-apollo4-pinctrl_8h.md#a7749829f0bf0c121adc56d86642d89ce)#define NCE91\_P91 APOLLO4\_PINMUX(91, 7)

[ 977](ambiq-apollo4-pinctrl_8h.md#ac46b789266d9702e649b32374d252f04)#define OBSBUS11\_P91 APOLLO4\_PINMUX(91, 8)

[ 978](ambiq-apollo4-pinctrl_8h.md#af3019c7b40a96a23cddc36a872fa42a1)#define VCMPO\_P91 APOLLO4\_PINMUX(91, 9)

[ 979](ambiq-apollo4-pinctrl_8h.md#a4c64ae4cc7d61e75dbc3e9e462938704)#define FPIO\_P91 APOLLO4\_PINMUX(91, 11)

[ 980](ambiq-apollo4-pinctrl_8h.md#a144e5836d0f84d41a415f0c0e62aaa20)#define GPIO\_P92 APOLLO4\_PINMUX(92, 3)

[ 981](ambiq-apollo4-pinctrl_8h.md#a74fe2bc1ce57aafa5c709b4bede05fe1)#define CT92\_P92 APOLLO4\_PINMUX(92, 6)

[ 982](ambiq-apollo4-pinctrl_8h.md#a17f1a74051dcc5365f3d2ad8a4415b3e)#define NCE92\_P92 APOLLO4\_PINMUX(92, 7)

[ 983](ambiq-apollo4-pinctrl_8h.md#a97e8d866ebe202069a46865303da4c6b)#define OBSBUS12\_P92 APOLLO4\_PINMUX(92, 8)

[ 984](ambiq-apollo4-pinctrl_8h.md#a7123f95d9a3d4eeddb7f594b03bb0d46)#define VCMPO\_P92 APOLLO4\_PINMUX(92, 9)

[ 985](ambiq-apollo4-pinctrl_8h.md#aa206ca029751284ee3f83b2b83427491)#define FPIO\_P92 APOLLO4\_PINMUX(92, 11)

[ 986](ambiq-apollo4-pinctrl_8h.md#ad58f6352b7ecec983b7a85fd8c8eea10)#define MSPI2\_9\_P93 APOLLO4\_PINMUX(93, 0)

[ 987](ambiq-apollo4-pinctrl_8h.md#a4c716f07f12db46c1ae4d1429f29d062)#define GPIO\_P93 APOLLO4\_PINMUX(93, 3)

[ 988](ambiq-apollo4-pinctrl_8h.md#a006c28dc03ff088f3a09e4d413cf738a)#define CT93\_P93 APOLLO4\_PINMUX(93, 6)

[ 989](ambiq-apollo4-pinctrl_8h.md#aea82da9429fff4ec9508651b4b24eaa8)#define NCE93\_P93 APOLLO4\_PINMUX(93, 7)

[ 990](ambiq-apollo4-pinctrl_8h.md#a00fe997cf76f4842b74ca239c362cf6a)#define OBSBUS13\_P93 APOLLO4\_PINMUX(93, 8)

[ 991](ambiq-apollo4-pinctrl_8h.md#a652adf8b14771e0be22a92e18c0eff7b)#define VCMPO\_P93 APOLLO4\_PINMUX(93, 9)

[ 992](ambiq-apollo4-pinctrl_8h.md#a0016ead5ab7c0b4cc26d22a7d32b61da)#define FPIO\_P93 APOLLO4\_PINMUX(93, 11)

[ 993](ambiq-apollo4-pinctrl_8h.md#a8db81e09a632736dfa6f50698afc9ed1)#define GPIO\_P94 APOLLO4\_PINMUX(94, 3)

[ 994](ambiq-apollo4-pinctrl_8h.md#a60a0ada673e441a40fbd7e2d2fb75e0d)#define CT94\_P94 APOLLO4\_PINMUX(94, 6)

[ 995](ambiq-apollo4-pinctrl_8h.md#a5b0f62d51708beda25e83ee287865c6f)#define NCE94\_P94 APOLLO4\_PINMUX(94, 7)

[ 996](ambiq-apollo4-pinctrl_8h.md#a9ff7d5ecbe4a32b8d30031c880833bd8)#define OBSBUS14\_P94 APOLLO4\_PINMUX(94, 8)

[ 997](ambiq-apollo4-pinctrl_8h.md#a440777738e6ccc6712dcb2cb1eebcbe5)#define VCMPO\_P94 APOLLO4\_PINMUX(94, 9)

[ 998](ambiq-apollo4-pinctrl_8h.md#aa817b87e0657b6fa63b4919fe61ed876)#define FPIO\_P94 APOLLO4\_PINMUX(94, 11)

[ 999](ambiq-apollo4-pinctrl_8h.md#a2283229756c035109463d3d086582a4c)#define GPIO\_P95 APOLLO4\_PINMUX(95, 3)

[ 1000](ambiq-apollo4-pinctrl_8h.md#ae71ce7068e7d3ac32b1b6eebd0cfb400)#define CT95\_P95 APOLLO4\_PINMUX(95, 6)

[ 1001](ambiq-apollo4-pinctrl_8h.md#acaf4d61c68b05c399590dc1c177014dd)#define NCE95\_P95 APOLLO4\_PINMUX(95, 7)

[ 1002](ambiq-apollo4-pinctrl_8h.md#aef31fb5f1595fe68bec72bcc78b94a8a)#define OBSBUS15\_P95 APOLLO4\_PINMUX(95, 8)

[ 1003](ambiq-apollo4-pinctrl_8h.md#a3c0115620b0dc9429c13ae229c98b7d0)#define FPIO\_P95 APOLLO4\_PINMUX(95, 11)

[ 1004](ambiq-apollo4-pinctrl_8h.md#a744109b2f92205a205569b252db6b3ec)#define GPIO\_P96 APOLLO4\_PINMUX(96, 3)

[ 1005](ambiq-apollo4-pinctrl_8h.md#abbadbd046aeb79293ec1b2dbdbb2748a)#define CT96\_P96 APOLLO4\_PINMUX(96, 6)

[ 1006](ambiq-apollo4-pinctrl_8h.md#a362eecfc9f473fd094b16773846a5578)#define NCE96\_P96 APOLLO4\_PINMUX(96, 7)

[ 1007](ambiq-apollo4-pinctrl_8h.md#a80a8a9f4918f158e0fef07b9eb64ea21)#define OBSBUS0\_P96 APOLLO4\_PINMUX(96, 8)

[ 1008](ambiq-apollo4-pinctrl_8h.md#a5bd8f59861d051e3c4d4c860e7d0ead4)#define FPIO\_P96 APOLLO4\_PINMUX(96, 11)

[ 1009](ambiq-apollo4-pinctrl_8h.md#a1f68c6c2de92055f1e58b2b5ff831802)#define GPIO\_P97 APOLLO4\_PINMUX(97, 3)

[ 1010](ambiq-apollo4-pinctrl_8h.md#a5fdca54d638c3aed7958b69dc1282102)#define CT97\_P97 APOLLO4\_PINMUX(97, 6)

[ 1011](ambiq-apollo4-pinctrl_8h.md#a1e9424b233ff8b2227314bd89d409b40)#define NCE97\_P97 APOLLO4\_PINMUX(97, 7)

[ 1012](ambiq-apollo4-pinctrl_8h.md#ad38d0b218eaaedbd9c878255f07a31bd)#define OBSBUS1\_P97 APOLLO4\_PINMUX(97, 8)

[ 1013](ambiq-apollo4-pinctrl_8h.md#a457ccfb0fbd0a8524bc259825d81f5c0)#define FPIO\_P97 APOLLO4\_PINMUX(97, 11)

[ 1014](ambiq-apollo4-pinctrl_8h.md#abede61e4093d748c22fb132c323f5b99)#define GPIO\_P98 APOLLO4\_PINMUX(98, 3)

[ 1015](ambiq-apollo4-pinctrl_8h.md#a654eacc45e53700ade8cb99763bd72ac)#define CT98\_P98 APOLLO4\_PINMUX(98, 6)

[ 1016](ambiq-apollo4-pinctrl_8h.md#a7e6217c20c01b1e809e2a54b2548e95b)#define NCE98\_P98 APOLLO4\_PINMUX(98, 7)

[ 1017](ambiq-apollo4-pinctrl_8h.md#a4d971d146729a0542420753cad44fd29)#define OBSBUS2\_P98 APOLLO4\_PINMUX(98, 8)

[ 1018](ambiq-apollo4-pinctrl_8h.md#ac51bd12e74f32f11dd4b89682985d6c8)#define FPIO\_P98 APOLLO4\_PINMUX(98, 11)

[ 1019](ambiq-apollo4-pinctrl_8h.md#a13b61df55734791cea16481cfb7feb28)#define GPIO\_P99 APOLLO4\_PINMUX(99, 3)

[ 1020](ambiq-apollo4-pinctrl_8h.md#a6bce64b43d86b2cb621d3d0a30fa6afc)#define CT99\_P99 APOLLO4\_PINMUX(99, 6)

[ 1021](ambiq-apollo4-pinctrl_8h.md#a7aea7b2c935bbea8e90d888591611d04)#define NCE99\_P99 APOLLO4\_PINMUX(99, 7)

[ 1022](ambiq-apollo4-pinctrl_8h.md#aa564e30369a60ba141e2a6bf77d41d7e)#define OBSBUS3\_P99 APOLLO4\_PINMUX(99, 8)

[ 1023](ambiq-apollo4-pinctrl_8h.md#a6ae4b6e6283b943c0be7501023abd4d4)#define FPIO\_P99 APOLLO4\_PINMUX(99, 11)

[ 1024](ambiq-apollo4-pinctrl_8h.md#a9ab81ecbf987d4a17bb9d91e3f658a2a)#define GPIO\_P100 APOLLO4\_PINMUX(100, 3)

[ 1025](ambiq-apollo4-pinctrl_8h.md#ae1261dddbff12162f0307d79a770f0e8)#define CT100\_P100 APOLLO4\_PINMUX(100, 6)

[ 1026](ambiq-apollo4-pinctrl_8h.md#a68e895545bb3ad6813d57a986946892f)#define NCE100\_P100 APOLLO4\_PINMUX(100, 7)

[ 1027](ambiq-apollo4-pinctrl_8h.md#a13f1adff3495879c572f519160a6ea5d)#define OBSBUS4\_P100 APOLLO4\_PINMUX(100, 8)

[ 1028](ambiq-apollo4-pinctrl_8h.md#a7c7c997ec5f5b9232fe3495d928cdf84)#define FPIO\_P100 APOLLO4\_PINMUX(100, 11)

[ 1029](ambiq-apollo4-pinctrl_8h.md#ae8f79fcc6ba05000e230b3447f50abee)#define GPIO\_P101 APOLLO4\_PINMUX(101, 3)

[ 1030](ambiq-apollo4-pinctrl_8h.md#aaff5c666593ec9666aa9f18a7c970824)#define CT101\_P101 APOLLO4\_PINMUX(101, 6)

[ 1031](ambiq-apollo4-pinctrl_8h.md#ab67793e6aa1739f804dc3ba6ba444b0b)#define NCE101\_P101 APOLLO4\_PINMUX(101, 7)

[ 1032](ambiq-apollo4-pinctrl_8h.md#adf194bba4fea1138b06905786db5cec3)#define OBSBUS5\_P101 APOLLO4\_PINMUX(101, 8)

[ 1033](ambiq-apollo4-pinctrl_8h.md#a4ea2462d1f3042c57d49ade116e99ac0)#define FPIO\_P101 APOLLO4\_PINMUX(101, 11)

[ 1034](ambiq-apollo4-pinctrl_8h.md#a429495dc05fa4b8afdbc549baad3967e)#define GPIO\_P102 APOLLO4\_PINMUX(102, 3)

[ 1035](ambiq-apollo4-pinctrl_8h.md#aab951ecc1c664e195dde8c8aad480c30)#define CT102\_P102 APOLLO4\_PINMUX(102, 6)

[ 1036](ambiq-apollo4-pinctrl_8h.md#a1519f2c89072ad5ab19d87c4ac0dc363)#define NCE102\_P102 APOLLO4\_PINMUX(102, 7)

[ 1037](ambiq-apollo4-pinctrl_8h.md#a3094facd381a2e6cb4213b9a89cfc509)#define OBSBUS6\_P102 APOLLO4\_PINMUX(102, 8)

[ 1038](ambiq-apollo4-pinctrl_8h.md#a6f90e672295eba8d98dd404038f44144)#define FPIO\_P102 APOLLO4\_PINMUX(102, 11)

[ 1039](ambiq-apollo4-pinctrl_8h.md#aeeec5247b0e21195779b789ae5f59478)#define GPIO\_P103 APOLLO4\_PINMUX(103, 3)

[ 1040](ambiq-apollo4-pinctrl_8h.md#a02d173212c0d1b6513d918a133c13f06)#define CT103\_P103 APOLLO4\_PINMUX(103, 6)

[ 1041](ambiq-apollo4-pinctrl_8h.md#a462f13fedba110596e4cbdf3a4485746)#define NCE103\_P103 APOLLO4\_PINMUX(103, 7)

[ 1042](ambiq-apollo4-pinctrl_8h.md#a6452ad42a5a7620093c30c47b5ff9c06)#define OBSBUS7\_P103 APOLLO4\_PINMUX(103, 8)

[ 1043](ambiq-apollo4-pinctrl_8h.md#ae196b640e55889a5ef5c52de8d564afc)#define FPIO\_P103 APOLLO4\_PINMUX(103, 11)

[ 1044](ambiq-apollo4-pinctrl_8h.md#a23c8cd42acd5ea8dd60cf66fb6873e3e)#define MSPI1\_9\_P104 APOLLO4\_PINMUX(104, 0)

[ 1045](ambiq-apollo4-pinctrl_8h.md#a0cb559b7d83551d459930c7748dcbe99)#define GPIO\_P104 APOLLO4\_PINMUX(104, 3)

[ 1046](ambiq-apollo4-pinctrl_8h.md#a5d0ab77fe5a9938bdd66970dc907ff45)#define CT104\_P104 APOLLO4\_PINMUX(104, 6)

[ 1047](ambiq-apollo4-pinctrl_8h.md#aac29313bdccd90db62741271383f98b5)#define NCE104\_P104 APOLLO4\_PINMUX(104, 7)

[ 1048](ambiq-apollo4-pinctrl_8h.md#a36160355e284841b90e840d70376763a)#define OBSBUS8\_P104 APOLLO4\_PINMUX(104, 8)

[ 1049](ambiq-apollo4-pinctrl_8h.md#a66835aeb47af612660aa96cb2b6153b4)#define FPIO\_P104 APOLLO4\_PINMUX(104, 11)

[ 1050](ambiq-apollo4-pinctrl_8h.md#aeaab53c7a9723b7ff908620124f1b163)#define GPIO\_P105 APOLLO4\_PINMUX(105, 3)

[ 1051](ambiq-apollo4-pinctrl_8h.md#a39473e56d0fe34ec5fc9a151aaf21305)#define CT105\_P105 APOLLO4\_PINMUX(105, 6)

[ 1052](ambiq-apollo4-pinctrl_8h.md#a6b99ff82f6dbe1b1e59c717d455920ee)#define OBSBUS9\_P105 APOLLO4\_PINMUX(105, 8)

[ 1053](ambiq-apollo4-pinctrl_8h.md#a39ab9b460a73b85069a6e03783c65b2f)#define GPIO\_P106 APOLLO4\_PINMUX(106, 3)

[ 1054](ambiq-apollo4-pinctrl_8h.md#aa1ce0292d9ae6b2b143217d22656fe64)#define CT106\_P106 APOLLO4\_PINMUX(106, 6)

[ 1055](ambiq-apollo4-pinctrl_8h.md#a4309d6d3d8a6e6a21b69286a1ef7acc4)#define OBSBUS10\_P106 APOLLO4\_PINMUX(106, 8)

[ 1056](ambiq-apollo4-pinctrl_8h.md#acb70de969b0a5108f6fbc777078a9e24)#define GPIO\_P107 APOLLO4\_PINMUX(107, 3)

[ 1057](ambiq-apollo4-pinctrl_8h.md#a6aa7445d490bdbce41b645efabe34cfa)#define CT107\_P107 APOLLO4\_PINMUX(107, 6)

[ 1058](ambiq-apollo4-pinctrl_8h.md#a49b86305365ebe26e0d39f74e225b9f8)#define OBSBUS11\_P107 APOLLO4\_PINMUX(107, 8)

[ 1059](ambiq-apollo4-pinctrl_8h.md#a164238b66f0923862a9eca74f322726e)#define GPIO\_P108 APOLLO4\_PINMUX(108, 3)

[ 1060](ambiq-apollo4-pinctrl_8h.md#ac474dad92a0d20b3b2107c99c3a17448)#define CT108\_P108 APOLLO4\_PINMUX(108, 6)

[ 1061](ambiq-apollo4-pinctrl_8h.md#a1c7a0d5b51002d848539c85f4b7a5194)#define OBSBUS12\_P108 APOLLO4\_PINMUX(108, 8)

[ 1062](ambiq-apollo4-pinctrl_8h.md#a71af641eab2184ed0e13b64a95b2b879)#define GPIO\_P109 APOLLO4\_PINMUX(109, 3)

[ 1063](ambiq-apollo4-pinctrl_8h.md#a4b8549e72389423236d8d56bd2d35842)#define CT109\_P109 APOLLO4\_PINMUX(109, 6)

[ 1064](ambiq-apollo4-pinctrl_8h.md#a77f69ef04921cc3126c8fd6154163d54)#define OBSBUS13\_P109 APOLLO4\_PINMUX(109, 8)

[ 1065](ambiq-apollo4-pinctrl_8h.md#ad35c5f6d749b055838a681c3a1cb4e52)#define GPIO\_P110 APOLLO4\_PINMUX(110, 3)

[ 1066](ambiq-apollo4-pinctrl_8h.md#a98bbdada1f838c7a35b08affe1a6b810)#define CT110\_P110 APOLLO4\_PINMUX(110, 6)

[ 1067](ambiq-apollo4-pinctrl_8h.md#a3fe2e2e83eb50ea36b2f4ed9b6430122)#define OBSBUS14\_P110 APOLLO4\_PINMUX(110, 8)

[ 1068](ambiq-apollo4-pinctrl_8h.md#aee4a938bfb63aa1d1b26da9794c5c5f2)#define GPIO\_P111 APOLLO4\_PINMUX(111, 3)

[ 1069](ambiq-apollo4-pinctrl_8h.md#ac0bdeafcda2b64f1746c1571cef4351d)#define CT111\_P111 APOLLO4\_PINMUX(111, 6)

[ 1070](ambiq-apollo4-pinctrl_8h.md#adb39cabccc480340cd81cfd7bbfeb723)#define OBSBUS15\_P111 APOLLO4\_PINMUX(111, 8)

[ 1071](ambiq-apollo4-pinctrl_8h.md#a572f3e2b94a6e42db53cdbf356497306)#define GPIO\_P112 APOLLO4\_PINMUX(112, 3)

[ 1072](ambiq-apollo4-pinctrl_8h.md#aca4f42e4da04c8f79ca8d83098e67e64)#define CT112\_P112 APOLLO4\_PINMUX(112, 6)

[ 1073](ambiq-apollo4-pinctrl_8h.md#aadee62a393b91033e41095727346cc88)#define OBSBUS0\_P112 APOLLO4\_PINMUX(112, 8)

[ 1074](ambiq-apollo4-pinctrl_8h.md#ac40a477450b226060c72ad92b7c560eb)#define GPIO\_P113 APOLLO4\_PINMUX(113, 3)

[ 1075](ambiq-apollo4-pinctrl_8h.md#ab00f9f07eca7893327f0b8f85e00e470)#define CT113\_P113 APOLLO4\_PINMUX(113, 6)

[ 1076](ambiq-apollo4-pinctrl_8h.md#a8f78f738a7a8080d9b05ff52ab5fda5e)#define OBSBUS1\_P113 APOLLO4\_PINMUX(113, 8)

[ 1077](ambiq-apollo4-pinctrl_8h.md#aa283606711147724582f3b03cf8b1398)#define GPIO\_P114 APOLLO4\_PINMUX(114, 3)

[ 1078](ambiq-apollo4-pinctrl_8h.md#a229c9c338e8dd3ff59a164502fd229e6)#define CT114\_P114 APOLLO4\_PINMUX(114, 6)

[ 1079](ambiq-apollo4-pinctrl_8h.md#a55e84bc1a41686c49794738bd80e0efb)#define OBSBUS2\_P114 APOLLO4\_PINMUX(114, 8)

[ 1080](ambiq-apollo4-pinctrl_8h.md#a5c47768de9647b5b38287f17af6d6b61)#define GPIO\_P115 APOLLO4\_PINMUX(115, 3)

[ 1081](ambiq-apollo4-pinctrl_8h.md#af5a3f734493f73b8015aa4a9104aee83)#define CT115\_P115 APOLLO4\_PINMUX(115, 6)

[ 1082](ambiq-apollo4-pinctrl_8h.md#a488c2406b9a6c4473ca3786ec97e5810)#define OBSBUS3\_P115 APOLLO4\_PINMUX(115, 8)

[ 1083](ambiq-apollo4-pinctrl_8h.md#adaeb78e4671e35869b708bf0bbfcf457)#define GPIO\_P116 APOLLO4\_PINMUX(116, 3)

[ 1084](ambiq-apollo4-pinctrl_8h.md#a17e12458a3ec55b306ba93ea89931f70)#define CT116\_P116 APOLLO4\_PINMUX(116, 6)

[ 1085](ambiq-apollo4-pinctrl_8h.md#ae50804e0df20140202f1d44235b2ec18)#define OBSBUS4\_P116 APOLLO4\_PINMUX(116, 8)

[ 1086](ambiq-apollo4-pinctrl_8h.md#af0ed15e125be989834a567bba654524c)#define GPIO\_P117 APOLLO4\_PINMUX(117, 3)

[ 1087](ambiq-apollo4-pinctrl_8h.md#ab43d32d1727ef2246d1884a628dc3b4d)#define CT117\_P117 APOLLO4\_PINMUX(117, 6)

[ 1088](ambiq-apollo4-pinctrl_8h.md#a34910ee56802a8938145d9a6befa3bb5)#define OBSBUS5\_P117 APOLLO4\_PINMUX(117, 8)

[ 1089](ambiq-apollo4-pinctrl_8h.md#a1ee83bcc41acb8f1a23d0a6d6d3cc0e5)#define GPIO\_P118 APOLLO4\_PINMUX(118, 3)

[ 1090](ambiq-apollo4-pinctrl_8h.md#acbf9910d06e1557687275601ebe5bf94)#define CT118\_P118 APOLLO4\_PINMUX(118, 6)

[ 1091](ambiq-apollo4-pinctrl_8h.md#a7d064c39647ce86941c589eb29e927bf)#define OBSBUS6\_P118 APOLLO4\_PINMUX(118, 8)

[ 1092](ambiq-apollo4-pinctrl_8h.md#a04680e018f06ea3621221abaa475908c)#define GPIO\_P119 APOLLO4\_PINMUX(119, 3)

[ 1093](ambiq-apollo4-pinctrl_8h.md#a6fd493a53a6311a5a296288ca95e3248)#define CT119\_P119 APOLLO4\_PINMUX(119, 6)

[ 1094](ambiq-apollo4-pinctrl_8h.md#ab91d5ef9bd20959272028ca6a8cf2793)#define OBSBUS7\_P119 APOLLO4\_PINMUX(119, 8)

[ 1095](ambiq-apollo4-pinctrl_8h.md#aa2cc4a69737a9e04d46bf0de36281e34)#define GPIO\_P120 APOLLO4\_PINMUX(120, 3)

[ 1096](ambiq-apollo4-pinctrl_8h.md#afa7931091f087b68aa31dc0a64e4dfff)#define CT120\_P120 APOLLO4\_PINMUX(120, 6)

[ 1097](ambiq-apollo4-pinctrl_8h.md#a6919e05a651ba3e0c99328aadee160df)#define OBSBUS8\_P120 APOLLO4\_PINMUX(120, 8)

[ 1098](ambiq-apollo4-pinctrl_8h.md#a9f80ede94a97fedbb861f6f40f98c55f)#define GPIO\_P121 APOLLO4\_PINMUX(121, 3)

[ 1099](ambiq-apollo4-pinctrl_8h.md#a63b7da084ddf5c863c05578be2e1dcea)#define CT121\_P121 APOLLO4\_PINMUX(121, 6)

[ 1100](ambiq-apollo4-pinctrl_8h.md#ad737c518cbfa1dd508d0f5d6e1aa37a7)#define OBSBUS9\_P121 APOLLO4\_PINMUX(121, 8)

[ 1101](ambiq-apollo4-pinctrl_8h.md#a16010fd967c62600811d2356673f33e7)#define GPIO\_P122 APOLLO4\_PINMUX(122, 3)

[ 1102](ambiq-apollo4-pinctrl_8h.md#ab70f929b3caf2b958756e6b518f53ca0)#define CT122\_P122 APOLLO4\_PINMUX(122, 6)

[ 1103](ambiq-apollo4-pinctrl_8h.md#adda059280c2f53c16706821fec244b21)#define OBSBUS10\_P122 APOLLO4\_PINMUX(122, 8)

[ 1104](ambiq-apollo4-pinctrl_8h.md#abf88890980284a5e148e97dff70f8199)#define GPIO\_P123 APOLLO4\_PINMUX(123, 3)

[ 1105](ambiq-apollo4-pinctrl_8h.md#acbff21ec4c4875777bfc2fbd36d838f4)#define CT123\_P123 APOLLO4\_PINMUX(123, 6)

[ 1106](ambiq-apollo4-pinctrl_8h.md#aaefecf8c9b0c73241ea184511542a25e)#define OBSBUS11\_P123 APOLLO4\_PINMUX(123, 8)

[ 1107](ambiq-apollo4-pinctrl_8h.md#ae61e820bfa0add39feaca784161fd639)#define GPIO\_P124 APOLLO4\_PINMUX(124, 3)

[ 1108](ambiq-apollo4-pinctrl_8h.md#a9bcc7bb178a5ec5e0ab58ebc818b58e0)#define CT124\_P124 APOLLO4\_PINMUX(124, 6)

[ 1109](ambiq-apollo4-pinctrl_8h.md#a7b925c76ec1c64561103feb855a32245)#define OBSBUS12\_P124 APOLLO4\_PINMUX(124, 8)

[ 1110](ambiq-apollo4-pinctrl_8h.md#a40f0cf62983ee0e3056960276eb07b14)#define GPIO\_P125 APOLLO4\_PINMUX(125, 3)

[ 1111](ambiq-apollo4-pinctrl_8h.md#a4b31b8cef3e3d0c242a62f2618e80b6c)#define CT125\_P125 APOLLO4\_PINMUX(125, 6)

[ 1112](ambiq-apollo4-pinctrl_8h.md#a1649abcd2e3a8156e8eb6e1a4dce3bdc)#define OBSBUS13\_P125 APOLLO4\_PINMUX(125, 8)

[ 1113](ambiq-apollo4-pinctrl_8h.md#a3f88e95632900d55ad898c7d3c3c2dd4)#define GPIO\_P126 APOLLO4\_PINMUX(126, 3)

[ 1114](ambiq-apollo4-pinctrl_8h.md#af8d6dcd0499d8da5782f50e5502dedfa)#define CT126\_P126 APOLLO4\_PINMUX(126, 6)

[ 1115](ambiq-apollo4-pinctrl_8h.md#a7a9e4213af51b8097f92ea486ec995d9)#define OBSBUS14\_P126 APOLLO4\_PINMUX(126, 8)

[ 1116](ambiq-apollo4-pinctrl_8h.md#a0392a6c3a45b9bf9061b9fec0bb6d6c5)#define GPIO\_P127 APOLLO4\_PINMUX(127, 3)

[ 1117](ambiq-apollo4-pinctrl_8h.md#a940ea1e931610bb087b11d25811bb782)#define CT127\_P127 APOLLO4\_PINMUX(127, 6)

[ 1118](ambiq-apollo4-pinctrl_8h.md#aafee083e9c35046ad1075c5c069dec13)#define OBSBUS15\_P127 APOLLO4\_PINMUX(127, 8)

1119

1120#endif /\* \_\_APOLLO4\_PINCTRL\_H\_\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ambiq-apollo4-pinctrl.h](ambiq-apollo4-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
