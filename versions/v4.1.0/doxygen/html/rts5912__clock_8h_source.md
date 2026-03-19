---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rts5912__clock_8h_source.html
original_path: doxygen/html/rts5912__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rts5912\_clock.h

[Go to the documentation of this file.](rts5912__clock_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright (c) 2024 Realtek Semiconductor Corporation, SIBG-SD7

5 \* Author: Lin Yu-Cheng <lin\_yu\_cheng@realtek.com>

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RTS5912\_CLOCK\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RTS5912\_CLOCK\_H\_

10

11/\* ====================================================================================== \*/

12/\* ===================================== I2CCLK ======================================= \*/

[ 13](rts5912__clock_8h.md#a293372799ec2aec73a289db099e599da)#define I2CCLK\_I2C0CLKPWR\_Pos (0)

[ 14](rts5912__clock_8h.md#a1d96722d1f0fc9c46e474058fccfb867)#define I2CCLK\_I2C0CLKPWR\_Msk (0x1)

[ 15](rts5912__clock_8h.md#a7ac59a0177620abca7983af294474068)#define I2CCLK\_I2C0CLKSRC\_Pos (1)

[ 16](rts5912__clock_8h.md#a700beb58084c1dc8fcc37c2631e7b9df)#define I2CCLK\_I2C0CLKSRC\_Msk (0x2)

[ 17](rts5912__clock_8h.md#a021a4a49b52a41d2808ce017b57efe86)#define I2CCLK\_I2C0CLKDIV\_Pos (2)

[ 18](rts5912__clock_8h.md#af05403fa53b6499e8231c8be56242b02)#define I2CCLK\_I2C0CLKDIV\_Msk (0xc)

[ 19](rts5912__clock_8h.md#a7d7e0316ba63aebaddcca1e706db7ac6)#define I2CCLK\_I2C1CLKPWR\_Pos (4)

[ 20](rts5912__clock_8h.md#a4afd8e1d368965fbda413c33da71df34)#define I2CCLK\_I2C1CLKPWR\_Msk (0x10)

[ 21](rts5912__clock_8h.md#a25dd25c19c88b48e6a9983de03581165)#define I2CCLK\_I2C1CLKSRC\_Pos (5)

[ 22](rts5912__clock_8h.md#aede8d4f2e9f4e380bb3323a1bd66dbdf)#define I2CCLK\_I2C1CLKSRC\_Msk (0x20)

[ 23](rts5912__clock_8h.md#a647cecadd4a65dd586445da1bf9207a7)#define I2CCLK\_I2C1CLKDIV\_Pos (6)

[ 24](rts5912__clock_8h.md#ae5e279a894de25598f9ea60f19f8eb00)#define I2CCLK\_I2C1CLKDIV\_Msk (0xc0)

[ 25](rts5912__clock_8h.md#aeb67ef4fdc73570f196f7bc81e31724e)#define I2CCLK\_I2C2CLKPWR\_Pos (8)

[ 26](rts5912__clock_8h.md#aeb36c1343798cd4388a35f544bd09bd0)#define I2CCLK\_I2C2CLKPWR\_Msk (0x100)

[ 27](rts5912__clock_8h.md#ae1cc0cf4d2c2e1aecf41162da1e6ffcb)#define I2CCLK\_I2C2CLKSRC\_Pos (9)

[ 28](rts5912__clock_8h.md#aa5f6af96b2107b17171039999a00d1ab)#define I2CCLK\_I2C2CLKSRC\_Msk (0x200)

[ 29](rts5912__clock_8h.md#af9fb4381923f905272b2ab51d3087abc)#define I2CCLK\_I2C2CLKDIV\_Pos (10)

[ 30](rts5912__clock_8h.md#ae8fe21965d6efd0ec977947553c756ad)#define I2CCLK\_I2C2CLKDIV\_Msk (0xc00)

[ 31](rts5912__clock_8h.md#ace7fa53163633936415eda8efab73ac4)#define I2CCLK\_I2C3CLKPWR\_Pos (12)

[ 32](rts5912__clock_8h.md#a6309310616727c437651cca0ef26d9ad)#define I2CCLK\_I2C3CLKPWR\_Msk (0x1000)

[ 33](rts5912__clock_8h.md#af5e9e0f92ae4294c687e88583d68177a)#define I2CCLK\_I2C3CLKSRC\_Pos (13)

[ 34](rts5912__clock_8h.md#a4656864eabb157ba660108d0398eb188)#define I2CCLK\_I2C3CLKSRC\_Msk (0x2000)

[ 35](rts5912__clock_8h.md#a7768c4341413e5a5edd3fba4a8e55d9d)#define I2CCLK\_I2C3CLKDIV\_Pos (14)

[ 36](rts5912__clock_8h.md#a8a295e3ddbebeddd82ade4aac4893e6e)#define I2CCLK\_I2C3CLKDIV\_Msk (0xc000)

[ 37](rts5912__clock_8h.md#a3d07445fabf1b88f023ec95af1821b58)#define I2CCLK\_I2C4CLKPWR\_Pos (16)

[ 38](rts5912__clock_8h.md#a6ba8d0296230557c8ef8ea14a0ec56d2)#define I2CCLK\_I2C4CLKPWR\_Msk (0x10000)

[ 39](rts5912__clock_8h.md#a50d8d0a824b611f9be58e987222817c2)#define I2CCLK\_I2C4CLKSRC\_Pos (17)

[ 40](rts5912__clock_8h.md#ab6dc463b89798683d5307a90527abe62)#define I2CCLK\_I2C4CLKSRC\_Msk (0x20000)

[ 41](rts5912__clock_8h.md#a5a648fce01f85e9623c95eca5c06fea5)#define I2CCLK\_I2C4CLKDIV\_Pos (18)

[ 42](rts5912__clock_8h.md#a983d30d665e0b15a1e57f3bf73d65873)#define I2CCLK\_I2C4CLKDIV\_Msk (0xc0000)

[ 43](rts5912__clock_8h.md#ae3b0b16ed2edd9ea70434ee15030b96a)#define I2CCLK\_I2C5CLKPWR\_Pos (20)

[ 44](rts5912__clock_8h.md#a35f35df3d6852c4c8c913cd14e506add)#define I2CCLK\_I2C5CLKPWR\_Msk (0x100000)

[ 45](rts5912__clock_8h.md#a0a8d342bec05aa16a473a2bce16463b5)#define I2CCLK\_I2C5CLKSRC\_Pos (21)

[ 46](rts5912__clock_8h.md#a8f7d12ed9ef9f362174398bdffed6ded)#define I2CCLK\_I2C5CLKSRC\_Msk (0x200000)

[ 47](rts5912__clock_8h.md#af619385f4ebce780361bbf93e05e41b3)#define I2CCLK\_I2C5CLKDIV\_Pos (22)

[ 48](rts5912__clock_8h.md#a29db0a549a8e40c67d1e3f13b1a9f0cf)#define I2CCLK\_I2C5CLKDIV\_Msk (0xc00000)

[ 49](rts5912__clock_8h.md#a17b5457b2b1aa8f8182956acabb5825d)#define I2CCLK\_I2C6CLKPWR\_Pos (24)

[ 50](rts5912__clock_8h.md#abdcfcbe664e1defbc854ccf22e0174dc)#define I2CCLK\_I2C6CLKPWR\_Msk (0x1000000)

[ 51](rts5912__clock_8h.md#a69545be89c3ba1c1f33c806ff9545f97)#define I2CCLK\_I2C6CLKSRC\_Pos (25)

[ 52](rts5912__clock_8h.md#aeac7a0c342fa5523b0bc9bc52ca1aa47)#define I2CCLK\_I2C6CLKSRC\_Msk (0x2000000)

[ 53](rts5912__clock_8h.md#ad576c7484520dff7aa1fc03c4cbd3a57)#define I2CCLK\_I2C6CLKDIV\_Pos (26)

[ 54](rts5912__clock_8h.md#a21603148a431e7ba3027dd3ad9bdc6eb)#define I2CCLK\_I2C6CLKDIV\_Msk (0xc000000)

[ 55](rts5912__clock_8h.md#a2954644e0210b8eed4c6427aea25ec5f)#define I2CCLK\_I2C7CLKPWR\_Pos (28)

[ 56](rts5912__clock_8h.md#af44b6db84e02df6f9a554884c4cd0a21)#define I2CCLK\_I2C7CLKPWR\_Msk (0x10000000)

[ 57](rts5912__clock_8h.md#a011162941202f6d0f96b8372b5b11172)#define I2CCLK\_I2C7CLKSRC\_Pos (29)

[ 58](rts5912__clock_8h.md#a0639263976681b41aa3a5550f7c93006)#define I2CCLK\_I2C7CLKSRC\_Msk (0x20000000)

[ 59](rts5912__clock_8h.md#a9fa5e1d982f2771b5a654a95f1560461)#define I2CCLK\_I2C7CLKDIV\_Pos (30)

[ 60](rts5912__clock_8h.md#a0dd1b33f5d6cc789e8694da9a20bd056)#define I2CCLK\_I2C7CLKDIV\_Msk (0xc0000000)

61/\* =================================== PERICLKPWR0 ==================================== \*/

[ 62](rts5912__clock_8h.md#a68ad954b9caa13f068b969efa1292867)#define PERICLKPWR0\_GPIOCLKPWR\_Pos (0)

[ 63](rts5912__clock_8h.md#a264912d32a67561a98ad5e2d40bb1fec)#define PERICLKPWR0\_GPIOCLKPWR\_Msk (0x1)

[ 64](rts5912__clock_8h.md#a10458716a18652178a2f44d6cad5f19d)#define PERICLKPWR0\_TACHO0CLKPWR\_Pos (1)

[ 65](rts5912__clock_8h.md#afa62797e2ffbaaf21f0914d287a1c23f)#define PERICLKPWR0\_TACHO0CLKPWR\_Msk (0x2)

[ 66](rts5912__clock_8h.md#ab98c35607ad4a583bbe88829c30bd6cb)#define PERICLKPWR0\_TACHO1CLKPWR\_Pos (2)

[ 67](rts5912__clock_8h.md#a5c457e6643a80bd00ebbd608a9571267)#define PERICLKPWR0\_TACHO1CLKPWR\_Msk (0x4)

[ 68](rts5912__clock_8h.md#a6ba3c7705b7248351e2297f818fd7c31)#define PERICLKPWR0\_TACHO2CLKPWR\_Pos (3)

[ 69](rts5912__clock_8h.md#a6c0039d2914fb6024d85268b254e0b5a)#define PERICLKPWR0\_TACHO2CLKPWR\_Msk (0x8)

[ 70](rts5912__clock_8h.md#a467aafca922d2677f9922fadcf2d3390)#define PERICLKPWR0\_TACHO3CLKPWR\_Pos (4)

[ 71](rts5912__clock_8h.md#a9921b793bcc240b8437bf9a486fb7041)#define PERICLKPWR0\_TACHO3CLKPWR\_Msk (0x10)

[ 72](rts5912__clock_8h.md#a149c7980d5c4d35ec11ce8c57d1e2be4)#define PERICLKPWR0\_PS2CLKPWR\_Pos (5)

[ 73](rts5912__clock_8h.md#a63cee7cf08029ee6853e1a05701103b9)#define PERICLKPWR0\_PS2CLKPWR\_Msk (0x20)

[ 74](rts5912__clock_8h.md#a70503aeb6441f116e57aea28b8a33dd7)#define PERICLKPWR0\_KBMCLKPWR\_Pos (6)

[ 75](rts5912__clock_8h.md#aee1607675f04f1eff7c831c27d1c7868)#define PERICLKPWR0\_KBMCLKPWR\_Msk (0x40)

[ 76](rts5912__clock_8h.md#aeaebc8966b4687661d83a01a9f3a1c54)#define PERICLKPWR0\_PECICLKPWR\_Pos (7)

[ 77](rts5912__clock_8h.md#a5d1a0650fe4cbba249a3755bf6cca257)#define PERICLKPWR0\_PECICLKPWR\_Msk (0x80)

[ 78](rts5912__clock_8h.md#a55018caa877953a6ed5f8bd2ff8b83df)#define PERICLKPWR0\_PL0CLKPWR\_Pos (8)

[ 79](rts5912__clock_8h.md#a8015f809b0becd59795b918e002eeb07)#define PERICLKPWR0\_PL0CLKPWR\_Msk (0x100)

[ 80](rts5912__clock_8h.md#a217c850492873aaf53e601a4e79af6d6)#define PERICLKPWR0\_PL1CLKPWR\_Pos (9)

[ 81](rts5912__clock_8h.md#a8fffb2f638d16443509ee44c135d2d48)#define PERICLKPWR0\_PL1CLKPWR\_Msk (0x200)

[ 82](rts5912__clock_8h.md#adffd960d901a63ec55d759e15ab963a7)#define PERICLKPWR0\_PWM0CLKPWR\_Pos (10)

[ 83](rts5912__clock_8h.md#aca6d6b417e766518c6e27f729de70cb8)#define PERICLKPWR0\_PWM0CLKPWR\_Msk (0x400)

[ 84](rts5912__clock_8h.md#a96c9103bd180f2b111627976a8f9fc66)#define PERICLKPWR0\_PWM1CLKPWR\_Pos (11)

[ 85](rts5912__clock_8h.md#abc509a58a019321c1921833c1cc7f996)#define PERICLKPWR0\_PWM1CLKPWR\_Msk (0x800)

[ 86](rts5912__clock_8h.md#a1f9a9d40d76c84bd521ae187ac1079dc)#define PERICLKPWR0\_PWM2CLKPWR\_Pos (12)

[ 87](rts5912__clock_8h.md#a93121e0e5846f96a1fd84714f973f3fd)#define PERICLKPWR0\_PWM2CLKPWR\_Msk (0x1000)

[ 88](rts5912__clock_8h.md#ada57e5edeae1957e000cc72dfc5a83a4)#define PERICLKPWR0\_PWM3CLKPWR\_Pos (13)

[ 89](rts5912__clock_8h.md#a41d1449c465010f3c6d4f6ee0c470372)#define PERICLKPWR0\_PWM3CLKPWR\_Msk (0x2000)

[ 90](rts5912__clock_8h.md#a6aecc72c5abfc97902d5b2cda13eefd3)#define PERICLKPWR0\_PWM4CLKPWR\_Pos (14)

[ 91](rts5912__clock_8h.md#a031c7cf05f42bdf3b1fd8b59c1d86062)#define PERICLKPWR0\_PWM4CLKPWR\_Msk (0x4000)

[ 92](rts5912__clock_8h.md#a16f1fec59d9a2ad9b4c097f9d9b352c9)#define PERICLKPWR0\_PWM5CLKPWR\_Pos (15)

[ 93](rts5912__clock_8h.md#a8389c811aeedae89916468e442652fdb)#define PERICLKPWR0\_PWM5CLKPWR\_Msk (0x8000)

[ 94](rts5912__clock_8h.md#ac51b8eb3318c758d9ab5bf0fad585350)#define PERICLKPWR0\_PWM6CLKPWR\_Pos (16)

[ 95](rts5912__clock_8h.md#af1a2ad940eaa237f905677f5c2dc4c21)#define PERICLKPWR0\_PWM6CLKPWR\_Msk (0x10000)

[ 96](rts5912__clock_8h.md#a47997ed09270dbd13c12d5abc953874d)#define PERICLKPWR0\_PWM7CLKPWR\_Pos (17)

[ 97](rts5912__clock_8h.md#a0decef63cc50a43a67894e1b2ace21fb)#define PERICLKPWR0\_PWM7CLKPWR\_Msk (0x20000)

[ 98](rts5912__clock_8h.md#af6e0518164e44f44401f067611a5f9e4)#define PERICLKPWR0\_PWM8CLKPWR\_Pos (18)

[ 99](rts5912__clock_8h.md#a67678d7554346479a3d23c2b12a3ea10)#define PERICLKPWR0\_PWM8CLKPWR\_Msk (0x40000)

[ 100](rts5912__clock_8h.md#a2048da0d97cec3be1570b47169d8d3e5)#define PERICLKPWR0\_PWM9CLKPWR\_Pos (19)

[ 101](rts5912__clock_8h.md#a31381661998a807e69875508675a8ff9)#define PERICLKPWR0\_PWM9CLKPWR\_Msk (0x80000)

[ 102](rts5912__clock_8h.md#a051a2068e01e322306cbc56b05b089cc)#define PERICLKPWR0\_PWM10CLKPWR\_Pos (20)

[ 103](rts5912__clock_8h.md#ab4f78d91691efa656bc893d89a5f6255)#define PERICLKPWR0\_PWM10CLKPWR\_Msk (0x100000)

[ 104](rts5912__clock_8h.md#a7ad76f5c13fa379c5d7d8fcf1d6b3cb8)#define PERICLKPWR0\_PWM11CLKPWR\_Pos (21)

[ 105](rts5912__clock_8h.md#a4ef2a516eb2493557767220b40d77c99)#define PERICLKPWR0\_PWM11CLKPWR\_Msk (0x200000)

[ 106](rts5912__clock_8h.md#aafb98c01f008dd4f4306aa1d0428f249)#define PERICLKPWR0\_ESPICLKPWR\_Pos (22)

[ 107](rts5912__clock_8h.md#a3fb2008fcedcf0d5ae5fe8d4392d8c6f)#define PERICLKPWR0\_ESPICLKPWR\_Msk (0x400000)

[ 108](rts5912__clock_8h.md#a750aecc0f3488ecf1fb5b0d7394b073a)#define PERICLKPWR0\_KBCCLKPWR\_Pos (23)

[ 109](rts5912__clock_8h.md#a47fee9b6dfbb8e7d35fb98e677105f53)#define PERICLKPWR0\_KBCCLKPWR\_Msk (0x800000)

[ 110](rts5912__clock_8h.md#ae44a46fbb619c15e956b313583cf941b)#define PERICLKPWR0\_ACPICLKPWR\_Pos (24)

[ 111](rts5912__clock_8h.md#a09eed17e8a3c52d1df0bf9de18383b72)#define PERICLKPWR0\_ACPICLKPWR\_Msk (0x1000000)

[ 112](rts5912__clock_8h.md#a734cf0cd60091173782f10010ebd8569)#define PERICLKPWR0\_PMPORT0CLKPWR\_Pos (25)

[ 113](rts5912__clock_8h.md#ac0d5738357e845d9733768c59400549d)#define PERICLKPWR0\_PMPORT0CLKPWR\_Msk (0x2000000)

[ 114](rts5912__clock_8h.md#a2d95a01d23600e95b3428f3d0b35d8db)#define PERICLKPWR0\_PMPORT1CLKPWR\_Pos (26)

[ 115](rts5912__clock_8h.md#a65c65eb7cfd0624c089c6baf56666149)#define PERICLKPWR0\_PMPORT1CLKPWR\_Msk (0x4000000)

[ 116](rts5912__clock_8h.md#ae127cce09cfb7b6f5fe2c8d10dea5483)#define PERICLKPWR0\_PMPORT2CLKPWR\_Pos (27)

[ 117](rts5912__clock_8h.md#ae3fb805cfbf18bfe7ac08aef0f692989)#define PERICLKPWR0\_PMPORT2CLKPWR\_Msk (0x8000000)

[ 118](rts5912__clock_8h.md#ad82d0624f20a554db6b93da6a72f7988)#define PERICLKPWR0\_PMPORT3CLKPWR\_Pos (28)

[ 119](rts5912__clock_8h.md#ab0809298eb02acf0a8a59b0f23d7cdc2)#define PERICLKPWR0\_PMPORT3CLKPWR\_Msk (0x10000000)

[ 120](rts5912__clock_8h.md#a706d7af9bf4c69bbc67963e242fa53e6)#define PERICLKPWR0\_P80CLKPWR\_Pos (29)

[ 121](rts5912__clock_8h.md#a7095f6d2626aad22bc15a16fb8fca69d)#define PERICLKPWR0\_P80CLKPWR\_Msk (0x20000000)

[ 122](rts5912__clock_8h.md#afe24d0c27cd81409889e4031f6eab075)#define PERICLKPWR0\_EMI0CLKPWR\_Pos (30)

[ 123](rts5912__clock_8h.md#af84f838b87824f35d49fb5bfabf1e291)#define PERICLKPWR0\_EMI0CLKPWR\_Msk (0x40000000)

[ 124](rts5912__clock_8h.md#a5829b388044189ad166f5dc121e0fecf)#define PERICLKPWR0\_EMI1CLKPWR\_Pos (31)

[ 125](rts5912__clock_8h.md#a208d481f001b73b861880ebfb066fd7f)#define PERICLKPWR0\_EMI1CLKPWR\_Msk (0x80000000)

126/\* ===================================== UARTCLK ====================================== \*/

[ 127](rts5912__clock_8h.md#a497e3c4ffbc50ca0d8ef2d05415dcdf4)#define UARTCLK\_PWR\_Pos (0)

[ 128](rts5912__clock_8h.md#ad48f583a1e5bc587c42f80cced23f4ab)#define UARTCLK\_PWR\_Msk (0x1)

[ 129](rts5912__clock_8h.md#aa746ee28293fc2ece72b306ee9624a9a)#define UARTCLK\_SRC\_Pos (1)

[ 130](rts5912__clock_8h.md#accc877f41b4c6ce41171027f85350b7a)#define UARTCLK\_SRC\_Msk (0x2)

[ 131](rts5912__clock_8h.md#a1ecac62c4b19a33d6bf2cbea2243152e)#define UARTCLK\_DIV\_Pos (2)

[ 132](rts5912__clock_8h.md#ab99672ca2af237200c25815478e9d20f)#define UARTCLK\_DIV\_Msk (0xc)

133/\* ===================================== ADCCLK ======================================= \*/

[ 134](rts5912__clock_8h.md#a7bc75030f1bfb559a98f1754e01f3a28)#define ADCCLK\_PWR\_Pos (0)

[ 135](rts5912__clock_8h.md#a012fcdb8715e741f58985f46a1fef35b)#define ADCCLK\_PWR\_Msk (0x1)

[ 136](rts5912__clock_8h.md#a85a2eecd19179a62f7385ff33b2b5033)#define ADCCLK\_SRC\_Pos (1)

[ 137](rts5912__clock_8h.md#a25f0b37eafa85860837a1798c0629e60)#define ADCCLK\_SRC\_Msk (0x2)

[ 138](rts5912__clock_8h.md#a0d09ffc796e84ee2baa109003f5a7e6d)#define ADCCLK\_DIV\_Pos (2)

[ 139](rts5912__clock_8h.md#ad363c718f522ffd681793b278d15a1af)#define ADCCLK\_DIV\_Msk (0x1c)

140/\* =================================== PERICLKPWR1 ==================================== \*/

[ 141](rts5912__clock_8h.md#a42352dbb675883a5de4c0efb9bbd5b3d)#define PERICLKPWR1\_EMI2CLKPWR\_Pos (0)

[ 142](rts5912__clock_8h.md#a674bb7aec965f48320f163a3863690b9)#define PERICLKPWR1\_EMI2CLKPWR\_Msk (0x1)

[ 143](rts5912__clock_8h.md#a0d33d3a5d0e62ef2f14e530de065033e)#define PERICLKPWR1\_EMI3CLKPWR\_Pos (1)

[ 144](rts5912__clock_8h.md#a85e8a14156d4094e0e3781435d54af16)#define PERICLKPWR1\_EMI3CLKPWR\_Msk (0x2)

[ 145](rts5912__clock_8h.md#ac87ebf1f525c097cdb5302db72daaf84)#define PERICLKPWR1\_EMI4CLKPWR\_Pos (2)

[ 146](rts5912__clock_8h.md#a1bca91fc5aeec008178a11d0b09db08b)#define PERICLKPWR1\_EMI4CLKPWR\_Msk (0x4)

[ 147](rts5912__clock_8h.md#a790c3007c3eaea590750adb77f83d856)#define PERICLKPWR1\_EMI5CLKPWR\_Pos (3)

[ 148](rts5912__clock_8h.md#a358a7cff651fea2da13ca0927fdc96c5)#define PERICLKPWR1\_EMI5CLKPWR\_Msk (0x8)

[ 149](rts5912__clock_8h.md#ab8c0f7a7c51bbaf75da5c18bc8cd11a9)#define PERICLKPWR1\_EMI6CLKPWR\_Pos (4)

[ 150](rts5912__clock_8h.md#a8882e68bbe234a434d1b13fee5caacca)#define PERICLKPWR1\_EMI6CLKPWR\_Msk (0x10)

[ 151](rts5912__clock_8h.md#a64f9c26ca3cd4c3fa88c90223c487ef8)#define PERICLKPWR1\_EMI7CLKPWR\_Pos (5)

[ 152](rts5912__clock_8h.md#a6c2167a4e765dfafb1c1e44bf9fb26d9)#define PERICLKPWR1\_EMI7CLKPWR\_Msk (0x20)

[ 153](rts5912__clock_8h.md#a877addd70fc90f0b070fa6608ebdbad5)#define PERICLKPWR1\_I3C0CLKPWR\_Pos (9)

[ 154](rts5912__clock_8h.md#af6c22d4525780ad5e590a8ec83470ad2)#define PERICLKPWR1\_I3C0CLKPWR\_Msk (0x200)

[ 155](rts5912__clock_8h.md#a34c58fb181e4c06140027325632e286c)#define PERICLKPWR1\_I3C1CLKPWR\_Pos (10)

[ 156](rts5912__clock_8h.md#a1b70dfc81a7c4c11f309a1239381fe64)#define PERICLKPWR1\_I3C1CLKPWR\_Msk (0x400)

[ 157](rts5912__clock_8h.md#ae021aac70b85a0212b9321642cb33cbc)#define PERICLKPWR1\_I2CAUTOCLKPWR\_Pos (11)

[ 158](rts5912__clock_8h.md#ac19d43fe7927275ca8e7a2ef079fc3db)#define PERICLKPWR1\_I2CAUTOCLKPWR\_Msk (0x800)

[ 159](rts5912__clock_8h.md#a5184f3d8546edf123203119892c1abc2)#define PERICLKPWR1\_MCCLKPWR\_Pos (12)

[ 160](rts5912__clock_8h.md#a07a7b82adb29e5758c5be8c5d4b5ee54)#define PERICLKPWR1\_MCCLKPWR\_Msk (0x1000)

[ 161](rts5912__clock_8h.md#a7152ddaf9d7ba3aa973eaf13e52b3284)#define PERICLKPWR1\_TMR0CLKPWR\_Pos (13)

[ 162](rts5912__clock_8h.md#aef047826d336f3a5d6d003efce49e65f)#define PERICLKPWR1\_TMR0CLKPWR\_Msk (0x2000)

[ 163](rts5912__clock_8h.md#ac74065c23120616b9e2a3d77ba5a0cd5)#define PERICLKPWR1\_TMR1CLKPWR\_Pos (14)

[ 164](rts5912__clock_8h.md#a3285256a9a5ce4acb4a4efed88574b6a)#define PERICLKPWR1\_TMR1CLKPWR\_Msk (0x4000)

[ 165](rts5912__clock_8h.md#a49228bb422e24c1d5606d0b242ac6096)#define PERICLKPWR1\_TMR2CLKPWR\_Pos (15)

[ 166](rts5912__clock_8h.md#ad5af150a9258c753e20c5ae32a623b0e)#define PERICLKPWR1\_TMR2CLKPWR\_Msk (0x8000)

[ 167](rts5912__clock_8h.md#a0174d10010efc0d79305cddcc4950875)#define PERICLKPWR1\_TMR3CLKPWR\_Pos (16)

[ 168](rts5912__clock_8h.md#a9b783bb38cdd6c88d91036989ef25f6c)#define PERICLKPWR1\_TMR3CLKPWR\_Msk (0x10000)

[ 169](rts5912__clock_8h.md#ae401e4deb5a2f2996021d52aaf5adfdd)#define PERICLKPWR1\_TMR4CLKPWR\_Pos (17)

[ 170](rts5912__clock_8h.md#ac802905d474b7cf9e4b6de02fe4f07a2)#define PERICLKPWR1\_TMR4CLKPWR\_Msk (0x20000)

[ 171](rts5912__clock_8h.md#a49b20cc1e4048f8d855939a2b082a9da)#define PERICLKPWR1\_TMR5CLKPWR\_Pos (18)

[ 172](rts5912__clock_8h.md#a0e55de4eb342018bfd54b6b70fe750a4)#define PERICLKPWR1\_TMR5CLKPWR\_Msk (0x40000)

[ 173](rts5912__clock_8h.md#a2c72d5c5e9cd01219afdd725d1b7242c)#define PERICLKPWR1\_RTMRCLKPWR\_Pos (19)

[ 174](rts5912__clock_8h.md#ab03c840314363cd437339b27f90e5a82)#define PERICLKPWR1\_RTMRCLKPWR\_Msk (0x80000)

[ 175](rts5912__clock_8h.md#adcdce5e3ba869c9bfaddb9ae227a8a4e)#define PERICLKPWR1\_SLWTMR0CLKPWR\_Pos (20)

[ 176](rts5912__clock_8h.md#a263795d3da25d88872e5c64f54f8f369)#define PERICLKPWR1\_SLWTMR0CLKPWR\_Msk (0x100000)

[ 177](rts5912__clock_8h.md#a22571763b002ce25ca0a52ea39ff7f19)#define PERICLKPWR1\_SLWTMR1CLKPWR\_Pos (21)

[ 178](rts5912__clock_8h.md#a9534643f7d9e365370c4f74a3608a0cd)#define PERICLKPWR1\_SLWTMR1CLKPWR\_Msk (0x200000)

179/\* =================================== PERICLKPWR2 ==================================== \*/

[ 180](rts5912__clock_8h.md#ab6180f6d4d67cc14a9d74da56a491337)#define PERICLKPWR2\_RTCCLKPWR\_Pos (0)

[ 181](rts5912__clock_8h.md#ab4fe1737e2bc3c26fb146cbf9473565f)#define PERICLKPWR2\_RTCCLKPWR\_Msk (0x1)

[ 182](rts5912__clock_8h.md#a4512f6316012a2cd561a546488bee277)#define PERICLKPWR2\_WDTCLKPWR\_Pos (1)

[ 183](rts5912__clock_8h.md#aaa87b445a5329547c8e482d2132d35c5)#define PERICLKPWR2\_WDTCLKPWR\_Msk (0x2)

[ 184](rts5912__clock_8h.md#a473a81395efde90a543e2bc0cae77ee6)#define PERICLKPWR2\_PWRBTNCLKPWR\_Pos (2)

[ 185](rts5912__clock_8h.md#a15cc00e88f7172dcc2a0dfe2bcc73bea)#define PERICLKPWR2\_PWRBTNCLKPWR\_Msk (0x4)

[ 186](rts5912__clock_8h.md#a4ad1ec18abae6c3cc6ea5307ac0c03b4)#define PERICLKPWR2\_RC32KSRC\_Pos (30)

[ 187](rts5912__clock_8h.md#a49ccced75f063f245e6c2fcf3c39e188)#define PERICLKPWR2\_RC32KSRC\_Msk (0xc0000000)

188/\* ====================================================================================== \*/

189

[ 190](rts5912__clock_8h.md#a20c1bd0d7236f29627e877728097c168)#define RTS5912\_SCCON\_SYS (0)

[ 191](rts5912__clock_8h.md#aef4674ccf655c8f17b6bf1b194a7a755)#define RTS5912\_SCCON\_I2C (2)

[ 192](rts5912__clock_8h.md#a0edee3323e6b9dcfebd89026790493c3)#define RTS5912\_SCCON\_UART (3)

[ 193](rts5912__clock_8h.md#ad7a0cdbe390670312c2bd961060fce22)#define RTS5912\_SCCON\_ADC (4)

[ 194](rts5912__clock_8h.md#aabc957e7abaaa839cce5aa1bf746a904)#define RTS5912\_SCCON\_PERIPH\_GRP0 (5)

[ 195](rts5912__clock_8h.md#a65b9b8aaee5106615d202e7097f9d7ac)#define RTS5912\_SCCON\_PERIPH\_GRP1 (6)

[ 196](rts5912__clock_8h.md#a8163cc150dc2a2cd704b6adcfac3e6d3)#define RTS5912\_SCCON\_PERIPH\_GRP2 (7)

197

[ 198](rts5912__clock_8h.md#a2e918bbdee70d098465a6078b669057b)#define I2C0\_CLKPWR (I2CCLK\_I2C0CLKPWR\_Pos)

[ 199](rts5912__clock_8h.md#a8c5c57722186e059e84f3a26053a3424)#define I2C1\_CLKPWR (I2CCLK\_I2C1CLKPWR\_Pos)

[ 200](rts5912__clock_8h.md#a10e56c6a2358222e0f3f8543bfad7b39)#define I2C2\_CLKPWR (I2CCLK\_I2C2CLKPWR\_Pos)

[ 201](rts5912__clock_8h.md#adb8f4a5e8fe7144dc1ecc05c2752d944)#define I2C3\_CLKPWR (I2CCLK\_I2C3CLKPWR\_Pos)

[ 202](rts5912__clock_8h.md#aff5256da515d809ce8fd340e127934be)#define I2C4\_CLKPWR (I2CCLK\_I2C4CLKPWR\_Pos)

[ 203](rts5912__clock_8h.md#a503691fbc9dca417b058e5d5d5545e40)#define I2C5\_CLKPWR (I2CCLK\_I2C5CLKPWR\_Pos)

[ 204](rts5912__clock_8h.md#a81231678bb6f9076eb84404a95987230)#define I2C6\_CLKPWR (I2CCLK\_I2C6CLKPWR\_Pos)

[ 205](rts5912__clock_8h.md#ae39742939339aa308c1456d4ce7a01ef)#define I2C7\_CLKPWR (I2CCLK\_I2C7CLKPWR\_Pos)

206

[ 207](rts5912__clock_8h.md#aac6daa9bbff0e8bae9d5f3e7c053daac)#define I2C0\_PLL (0x0 << I2CCLK\_I2C0CLKSRC\_Pos)

[ 208](rts5912__clock_8h.md#a8aefc2943d4d5927792cbc8f8bc52e75)#define I2C0\_RC25M (0x1 << I2CCLK\_I2C0CLKSRC\_Pos)

[ 209](rts5912__clock_8h.md#aeff2120fd39199008fb436e8fb632cff)#define I2C1\_PLL (0x0 << I2CCLK\_I2C1CLKSRC\_Pos)

[ 210](rts5912__clock_8h.md#ac58db6da0c246d17e7714fdcce446410)#define I2C1\_RC25M (0x1 << I2CCLK\_I2C1CLKSRC\_Pos)

[ 211](rts5912__clock_8h.md#a78824bc292a9a6a1917132a9a2d8ff8f)#define I2C2\_PLL (0x0 << I2CCLK\_I2C2CLKSRC\_Pos)

[ 212](rts5912__clock_8h.md#ac14c7fc9331a050072596d7e681cee3c)#define I2C2\_RC25M (0x1 << I2CCLK\_I2C2CLKSRC\_Pos)

[ 213](rts5912__clock_8h.md#a866e836421e90a8d4f143958add81996)#define I2C3\_PLL (0x0 << I2CCLK\_I2C3CLKSRC\_Pos)

[ 214](rts5912__clock_8h.md#ab9b6fcaba97bd2855e3708a00595b5a5)#define I2C3\_RC25M (0x1 << I2CCLK\_I2C3CLKSRC\_Pos)

[ 215](rts5912__clock_8h.md#a5ea8025ed8ad2ae42280a24802641263)#define I2C4\_PLL (0x0 << I2CCLK\_I2C4CLKSRC\_Pos)

[ 216](rts5912__clock_8h.md#acc0e18716e941cccdbf6862c79e93364)#define I2C4\_RC25M (0x1 << I2CCLK\_I2C4CLKSRC\_Pos)

[ 217](rts5912__clock_8h.md#ad941eee5fb5b426eb6042577ac856e13)#define I2C5\_PLL (0x0 << I2CCLK\_I2C5CLKSRC\_Pos)

[ 218](rts5912__clock_8h.md#a6f8d9f300d67003741b6fdd02f1b7974)#define I2C5\_RC25M (0x1 << I2CCLK\_I2C5CLKSRC\_Pos)

[ 219](rts5912__clock_8h.md#a37cf2e34bc4b8fc6e6a0c1889a584b61)#define I2C6\_PLL (0x0 << I2CCLK\_I2C6CLKSRC\_Pos)

[ 220](rts5912__clock_8h.md#a6b1dc468fae8385fefba211fb7398be0)#define I2C6\_RC25M (0x1 << I2CCLK\_I2C6CLKSRC\_Pos)

[ 221](rts5912__clock_8h.md#a6403715406de487ce2f7115f99ba1f1f)#define I2C7\_PLL (0x0 << I2CCLK\_I2C7CLKSRC\_Pos)

[ 222](rts5912__clock_8h.md#a1d18282006780fec2589dba99839f067)#define I2C7\_RC25M (0x1 << I2CCLK\_I2C7CLKSRC\_Pos)

223

[ 224](rts5912__clock_8h.md#a50f850a49c16983af6c54db7b6e8090b)#define I2C0\_CLKDIV1 (0 << I2CCLK\_I2C0CLKDIV\_Pos)

[ 225](rts5912__clock_8h.md#af931ad286cec12f32a87c3ba9b3cb4b5)#define I2C0\_CLKDIV2 (1 << I2CCLK\_I2C0CLKDIV\_Pos)

[ 226](rts5912__clock_8h.md#ae6eb059de7ef8646d012ebe84d36c4cf)#define I2C0\_CLKDIV4 (2 << I2CCLK\_I2C0CLKDIV\_Pos)

[ 227](rts5912__clock_8h.md#a0874e67f440b74949ff812a87a461cb4)#define I2C0\_CLKDIV8 (3 << I2CCLK\_I2C0CLKDIV\_Pos)

228

[ 229](rts5912__clock_8h.md#a4779320bbe8f19d20f6d6d4a361b8078)#define I2C1\_CLKDIV1 (0 << I2CCLK\_I2C1CLKDIV\_Pos)

[ 230](rts5912__clock_8h.md#a0fb87d189c67dceb98ec0aa34f9f0af2)#define I2C1\_CLKDIV2 (1 << I2CCLK\_I2C1CLKDIV\_Pos)

[ 231](rts5912__clock_8h.md#a85a68c3bfbca4af78c8c0a14a4fb4613)#define I2C1\_CLKDIV4 (2 << I2CCLK\_I2C1CLKDIV\_Pos)

[ 232](rts5912__clock_8h.md#a9f0b1ee3d02cbb0571644b65d593246e)#define I2C1\_CLKDIV8 (3 << I2CCLK\_I2C1CLKDIV\_Pos)

233

[ 234](rts5912__clock_8h.md#a69fe4c28ef6d560f7d4a6f110ec156ea)#define I2C2\_CLKDIV1 (0 << I2CCLK\_I2C2CLKDIV\_Pos)

[ 235](rts5912__clock_8h.md#a6751f460ec986185fb3f4381027f7c45)#define I2C2\_CLKDIV2 (1 << I2CCLK\_I2C2CLKDIV\_Pos)

[ 236](rts5912__clock_8h.md#a67aa18aeb0e92aa536c65c3a9434b484)#define I2C2\_CLKDIV4 (2 << I2CCLK\_I2C2CLKDIV\_Pos)

[ 237](rts5912__clock_8h.md#a0c0d94bb46e10204e05f7a39c384eda4)#define I2C2\_CLKDIV8 (3 << I2CCLK\_I2C2CLKDIV\_Pos)

238

[ 239](rts5912__clock_8h.md#ac44d0bad39b5cc291e9468b7b11e2ec9)#define I2C3\_CLKDIV1 (0 << I2CCLK\_I2C3CLKDIV\_Pos)

[ 240](rts5912__clock_8h.md#a66adbff3e9e5a580448209bb4ff27c71)#define I2C3\_CLKDIV2 (1 << I2CCLK\_I2C3CLKDIV\_Pos)

[ 241](rts5912__clock_8h.md#a68fab78de140d9123e3fa97eca683bf7)#define I2C3\_CLKDIV4 (2 << I2CCLK\_I2C3CLKDIV\_Pos)

[ 242](rts5912__clock_8h.md#ab01dd898b26198ef80c19fa47c3b5fd5)#define I2C3\_CLKDIV8 (3 << I2CCLK\_I2C3CLKDIV\_Pos)

243

[ 244](rts5912__clock_8h.md#a564924cb4c870ede849f71732552adae)#define I2C4\_CLKDIV1 (0 << I2CCLK\_I2C4CLKDIV\_Pos)

[ 245](rts5912__clock_8h.md#a9c23c3466528d04b487d654815c3739f)#define I2C4\_CLKDIV2 (1 << I2CCLK\_I2C4CLKDIV\_Pos)

[ 246](rts5912__clock_8h.md#a40c8259f73098f8a5b38a93c4ff29351)#define I2C4\_CLKDIV4 (2 << I2CCLK\_I2C4CLKDIV\_Pos)

[ 247](rts5912__clock_8h.md#a4b8bd16a17e6a601fa7735cfa57b68b7)#define I2C4\_CLKDIV8 (3 << I2CCLK\_I2C4CLKDIV\_Pos)

248

[ 249](rts5912__clock_8h.md#acf95bbe9326695a49f897a2dd7e11b14)#define I2C5\_CLKDIV1 (0 << I2CCLK\_I2C5CLKDIV\_Pos)

[ 250](rts5912__clock_8h.md#ad61ebbe3026d149546c39d15d96ae11b)#define I2C5\_CLKDIV2 (1 << I2CCLK\_I2C5CLKDIV\_Pos)

[ 251](rts5912__clock_8h.md#a9b51ec0a5133b57857067dea993714d6)#define I2C5\_CLKDIV4 (2 << I2CCLK\_I2C5CLKDIV\_Pos)

[ 252](rts5912__clock_8h.md#af5b489a200b010621aefec7ab07f8769)#define I2C5\_CLKDIV8 (3 << I2CCLK\_I2C5CLKDIV\_Pos)

253

[ 254](rts5912__clock_8h.md#a03e9d04cefb22b42b4e0909f6636202f)#define I2C6\_CLKDIV1 (0 << I2CCLK\_I2C6CLKDIV\_Pos)

[ 255](rts5912__clock_8h.md#ae950bb2ad2e75e6832cb8f5b1ba38afa)#define I2C6\_CLKDIV2 (1 << I2CCLK\_I2C6CLKDIV\_Pos)

[ 256](rts5912__clock_8h.md#acefe054b89134e7c645b766a2936fbdc)#define I2C6\_CLKDIV4 (2 << I2CCLK\_I2C6CLKDIV\_Pos)

[ 257](rts5912__clock_8h.md#a7e0e1781c79225a6c2b12d1d4f8b889c)#define I2C6\_CLKDIV8 (3 << I2CCLK\_I2C6CLKDIV\_Pos)

258

[ 259](rts5912__clock_8h.md#a6f29587885716f3db981f4617fd0f3a9)#define I2C7\_CLKDIV1 (0 << I2CCLK\_I2C7CLKDIV\_Pos)

[ 260](rts5912__clock_8h.md#ac1f98e1a51fa5b8ccb1fcd8fc30992c4)#define I2C7\_CLKDIV2 (1 << I2CCLK\_I2C7CLKDIV\_Pos)

[ 261](rts5912__clock_8h.md#a8e2b6e860b4ba0b90e0eabbcae880154)#define I2C7\_CLKDIV4 (2 << I2CCLK\_I2C7CLKDIV\_Pos)

[ 262](rts5912__clock_8h.md#a5630fbe7402f42ee5e9df3fbe1bcbe3c)#define I2C7\_CLKDIV8 (3 << I2CCLK\_I2C7CLKDIV\_Pos)

263

[ 264](rts5912__clock_8h.md#a145ede7e3d754c7b3993453aaa21bc4d)#define UART0\_CLKPWR (UARTCLK\_PWR\_Pos)

265

[ 266](rts5912__clock_8h.md#a37d40af1ccce1ceafd427bffc7a189dd)#define UART0\_RC25M (0x0 << UARTCLK\_SRC\_Pos)

[ 267](rts5912__clock_8h.md#ae347cd992a47d5bfa9f9fc2ef7e05e94)#define UART0\_PLL (0x1 << UARTCLK\_SRC\_Pos)

268

[ 269](rts5912__clock_8h.md#a6691d650f95e5f7601f69e154078529a)#define UART0\_CLKDIV1 (0 << UARTCLK\_DIV\_Pos)

[ 270](rts5912__clock_8h.md#ae10ec40d35a08f5025de607236785cd9)#define UART0\_CLKDIV2 (1 << UARTCLK\_DIV\_Pos)

[ 271](rts5912__clock_8h.md#aa6adcd1b2521feec6c149d8b4a083eb0)#define UART0\_CLKDIV4 (2 << UARTCLK\_DIV\_Pos)

[ 272](rts5912__clock_8h.md#a7aeaf8064adc5b0fcfc48283e01f528e)#define UART0\_CLKDIV8 (3 << UARTCLK\_DIV\_Pos)

273

[ 274](rts5912__clock_8h.md#a2059e90ecf961a992b5d027098060444)#define ADC0\_CLKPWR (ADCCLK\_PWR\_Pos)

275

[ 276](rts5912__clock_8h.md#a0f20bd2b6ea7e02ade572f71a63bfdc1)#define ADC0\_RC25M (0x0 << ADCCLK\_SRC\_Pos)

[ 277](rts5912__clock_8h.md#a0bc403bdba53b54d8a2ef8ef7e8e7706)#define ADC0\_PLL (0x1 << ADCCLK\_SRC\_Pos)

278

[ 279](rts5912__clock_8h.md#a320cef0e1249b5db51975da365735731)#define ADC0\_CLKDIV1 (0 << ADCCLK\_DIV\_Pos)

[ 280](rts5912__clock_8h.md#addae3d7ff0f17ae11dab578c11fbbc9b)#define ADC0\_CLKDIV2 (1 << ADCCLK\_DIV\_Pos)

[ 281](rts5912__clock_8h.md#a7dabd09829ace5dd9b45cc85dbde9262)#define ADC0\_CLKDIV3 (2 << ADCCLK\_DIV\_Pos)

[ 282](rts5912__clock_8h.md#a0d94458ddc5be16301f7840649e75667)#define ADC0\_CLKDIV4 (3 << ADCCLK\_DIV\_Pos)

[ 283](rts5912__clock_8h.md#a895f3042a4e137212a8cf696a34224bf)#define ADC0\_CLKDIV6 (4 << ADCCLK\_DIV\_Pos)

[ 284](rts5912__clock_8h.md#ac91254b5c9807a60c59ecb439b846021)#define ADC0\_CLKDIV8 (5 << ADCCLK\_DIV\_Pos)

285

[ 286](rts5912__clock_8h.md#ad3343829fb4d87d6f99e6e8bf875bfcd)#define PERIPH\_GRP0\_GPIO\_CLKPWR (PERICLKPWR0\_GPIOCLKPWR\_Pos)

[ 287](rts5912__clock_8h.md#a78da25d3317327eca58216966640d948)#define PERIPH\_GRP0\_TACH0\_CLKPWR (PERICLKPWR0\_TACHO0CLKPWR\_Pos)

[ 288](rts5912__clock_8h.md#accf88b2ee276192ae430dfe812f59010)#define PERIPH\_GRP0\_TACH1\_CLKPWR (PERICLKPWR0\_TACHO1CLKPWR\_Pos)

[ 289](rts5912__clock_8h.md#a99ab9a12ae2aecafee476a9051245ef4)#define PERIPH\_GRP0\_TACH2\_CLKPWR (PERICLKPWR0\_TACHO2CLKPWR\_Pos)

[ 290](rts5912__clock_8h.md#ab3160876f94373ee70e919d679792b2b)#define PERIPH\_GRP0\_TACH3\_CLKPWR (PERICLKPWR0\_TACHO3CLKPWR\_Pos)

[ 291](rts5912__clock_8h.md#a840aa9db71ddf1bc9e105364257e1f6a)#define PERIPH\_GRP0\_PS2\_CLKPWR (PERICLKPWR0\_PS2CLKPWR\_Pos)

[ 292](rts5912__clock_8h.md#a54ac26f30c57fbc635240710ca43f11b)#define PERIPH\_GRP0\_KBM\_CLKPWR (PERICLKPWR0\_KBMCLKPWR\_Pos)

[ 293](rts5912__clock_8h.md#a3c1907b516b23e11999d154199454b99)#define PERIPH\_GRP0\_PECI\_CLKPWR (PERICLKPWR0\_PECICLKPWR\_Pos)

[ 294](rts5912__clock_8h.md#ac34f2b077682cb398ba688b6208069e3)#define PERIPH\_GRP0\_LEDPWM0\_CLKPWR (PERICLKPWR0\_PL0CLKPWR\_Pos)

[ 295](rts5912__clock_8h.md#aa4c6701ba285b9c7ba65f6ed9059b32f)#define PERIPH\_GRP0\_LEDPWM1\_CLKPWR (PERICLKPWR0\_PL1CLKPWR\_Pos)

[ 296](rts5912__clock_8h.md#a43b5c30fcdc52ad5100507ed3e9b6f08)#define PERIPH\_GRP0\_PWM0\_CLKPWR (PERICLKPWR0\_PWM0CLKPWR\_Pos)

[ 297](rts5912__clock_8h.md#a163f0cc7f9f51ab8418f311b35cf36f9)#define PERIPH\_GRP0\_PWM1\_CLKPWR (PERICLKPWR0\_PWM1CLKPWR\_Pos)

[ 298](rts5912__clock_8h.md#a4cf47a6005f191e74a0925a93e13fe29)#define PERIPH\_GRP0\_PWM2\_CLKPWR (PERICLKPWR0\_PWM2CLKPWR\_Pos)

[ 299](rts5912__clock_8h.md#a3ffdc99f9e76274346fa9b92b831499c)#define PERIPH\_GRP0\_PWM3\_CLKPWR (PERICLKPWR0\_PWM3CLKPWR\_Pos)

[ 300](rts5912__clock_8h.md#ad3ca72ce0723e859602fc0e773753335)#define PERIPH\_GRP0\_PWM4\_CLKPWR (PERICLKPWR0\_PWM4CLKPWR\_Pos)

[ 301](rts5912__clock_8h.md#a6444d5fc503e5d0db90e89eda2929c94)#define PERIPH\_GRP0\_PWM5\_CLKPWR (PERICLKPWR0\_PWM5CLKPWR\_Pos)

[ 302](rts5912__clock_8h.md#af2f1ed162e35c6897efc6df94a16ffa0)#define PERIPH\_GRP0\_PWM6\_CLKPWR (PERICLKPWR0\_PWM6CLKPWR\_Pos)

[ 303](rts5912__clock_8h.md#a16dd75c3ffb1ec9ab3b5181d490900a4)#define PERIPH\_GRP0\_PWM7\_CLKPWR (PERICLKPWR0\_PWM7CLKPWR\_Pos)

[ 304](rts5912__clock_8h.md#aead999a907ebc3c4a34604dee52d1b5b)#define PERIPH\_GRP0\_PWM8\_CLKPWR (PERICLKPWR0\_PWM8CLKPWR\_Pos)

[ 305](rts5912__clock_8h.md#af99af1dc611317517e78604d2b523a54)#define PERIPH\_GRP0\_PWM9\_CLKPWR (PERICLKPWR0\_PWM9CLKPWR\_Pos)

[ 306](rts5912__clock_8h.md#a208d593e65b22b4c167e4b1943da8f34)#define PERIPH\_GRP0\_PWM10\_CLKPWR (PERICLKPWR0\_PWM10CLKPWR\_Pos)

[ 307](rts5912__clock_8h.md#aa4cbef537d29fb77f56ebbf9e6e06a8c)#define PERIPH\_GRP0\_PWM11\_CLKPWR (PERICLKPWR0\_PWM11CLKPWR\_Pos)

[ 308](rts5912__clock_8h.md#a38bc7433eed46e9b3887ad842f30ef7e)#define PERIPH\_GRP0\_ESPI\_CLKPWR (PERICLKPWR0\_ESPICLKPWR\_Pos)

[ 309](rts5912__clock_8h.md#a1cd10b2f654ee376fd9c0d2064421db3)#define PERIPH\_GRP0\_KBC\_CLKPWR (PERICLKPWR0\_KBCCLKPWR\_Pos)

[ 310](rts5912__clock_8h.md#abb6a3fa7acad1c9e01862bda9ca8a37a)#define PERIPH\_GRP0\_ACPI\_CLKPWR (PERICLKPWR0\_ACPICLKPWR\_Pos)

[ 311](rts5912__clock_8h.md#a3b47219dd49a6d8e71c2179296ae888e)#define PERIPH\_GRP0\_PMPORT0\_CLKPWR (PERICLKPWR0\_PMPORT0CLKPWR\_Pos)

[ 312](rts5912__clock_8h.md#a2a49a86b73810142fc9c1fbbbe859151)#define PERIPH\_GRP0\_PMPORT1\_CLKPWR (PERICLKPWR0\_PMPORT1CLKPWR\_Pos)

[ 313](rts5912__clock_8h.md#a2a9917b5954423cd18ac64e2adae8571)#define PERIPH\_GRP0\_PMPORT2\_CLKPWR (PERICLKPWR0\_PMPORT2CLKPWR\_Pos)

[ 314](rts5912__clock_8h.md#afd52ad266d92ad1cf712d515b91d551f)#define PERIPH\_GRP0\_PMPORT3\_CLKPWR (PERICLKPWR0\_PMPORT3CLKPWR\_Pos)

[ 315](rts5912__clock_8h.md#a9d0e89365f15fe0c0fbf309297baa2e3)#define PERIPH\_GRP0\_P80\_CLKPWR (PERICLKPWR0\_P80CLKPWR\_Pos)

[ 316](rts5912__clock_8h.md#a814598397e2615264691660d5b963bfe)#define PERIPH\_GRP0\_EMI0\_CLKPWR (PERICLKPWR0\_EMI0CLKPWR\_Pos)

[ 317](rts5912__clock_8h.md#af534c1a2974fed9032d0402af5781ea1)#define PERIPH\_GRP0\_EMI1\_CLKPWR (PERICLKPWR0\_EMI1CLKPWR\_Pos)

318

[ 319](rts5912__clock_8h.md#acd12698f2eac0f6fc22733703cf5b4ea)#define PERIPH\_GRP1\_EMI2\_CLKPWR (PERICLKPWR1\_EMI2CLKPWR\_Pos)

[ 320](rts5912__clock_8h.md#a5c75cc16e9bc7f539c8ed68dbbbea7a7)#define PERIPH\_GRP1\_EMI3\_CLKPWR (PERICLKPWR1\_EMI3CLKPWR\_Pos)

[ 321](rts5912__clock_8h.md#ae32a7704a36e1e5b962eb71964c008bd)#define PERIPH\_GRP1\_EMI4\_CLKPWR (PERICLKPWR1\_EMI4CLKPWR\_Pos)

[ 322](rts5912__clock_8h.md#a994bb9ff6ca836ed8373e042feeb45f8)#define PERIPH\_GRP1\_EMI5\_CLKPWR (PERICLKPWR1\_EMI5CLKPWR\_Pos)

[ 323](rts5912__clock_8h.md#a864bcd8c9ac0c400ac9c5df2a51ab44d)#define PERIPH\_GRP1\_EMI6\_CLKPWR (PERICLKPWR1\_EMI6CLKPWR\_Pos)

[ 324](rts5912__clock_8h.md#a4f793d3d610cd2aa5f3116154e588f39)#define PERIPH\_GRP1\_EMI7\_CLKPWR (PERICLKPWR1\_EMI7CLKPWR\_Pos)

[ 325](rts5912__clock_8h.md#a997ceb27c635ab953fad7a40cf643e15)#define PERIPH\_GRP1\_I3C0\_CLKPWR (PERICLKPWR1\_I3C0CLKPWR\_Pos)

[ 326](rts5912__clock_8h.md#a42d82dee683eb5a7e98d7784aa4683fa)#define PERIPH\_GRP1\_I3C1\_CLKPWR (PERICLKPWR1\_I3C1CLKPWR\_Pos)

[ 327](rts5912__clock_8h.md#a0cdfd26988a90bfb29acc19586b6fa98)#define PERIPH\_GRP1\_I2CAUTO\_CLKPWR (PERICLKPWR1\_I2CAUTOCLKPWR\_Pos)

[ 328](rts5912__clock_8h.md#acff16879940fa5e8d68812bd40efa9e2)#define PERIPH\_GRP1\_MC\_CLKPWR (PERICLKPWR1\_MCCLKPWR\_Pos)

[ 329](rts5912__clock_8h.md#aa84f600aba3bf0884b54eada9adcb4b1)#define PERIPH\_GRP1\_TMR0\_CLKPWR (PERICLKPWR1\_TMR0CLKPWR\_Pos)

[ 330](rts5912__clock_8h.md#a4a6118696df5e86a0c2ead7876692ac9)#define PERIPH\_GRP1\_TMR1\_CLKPWR (PERICLKPWR1\_TMR1CLKPWR\_Pos)

[ 331](rts5912__clock_8h.md#a0fa9e52e4a847a40d660cbd9990d273c)#define PERIPH\_GRP1\_TMR2\_CLKPWR (PERICLKPWR1\_TMR2CLKPWR\_Pos)

[ 332](rts5912__clock_8h.md#a937f4bd41146f73c26d3cc17b6ba5eea)#define PERIPH\_GRP1\_TMR3\_CLKPWR (PERICLKPWR1\_TMR3CLKPWR\_Pos)

[ 333](rts5912__clock_8h.md#ad3b4e09be7fd60cb306e01892dbdefb2)#define PERIPH\_GRP1\_TMR4\_CLKPWR (PERICLKPWR1\_TMR4CLKPWR\_Pos)

[ 334](rts5912__clock_8h.md#a67769a3fec74cfe1eb5216de19b26695)#define PERIPH\_GRP1\_TMR5\_CLKPWR (PERICLKPWR1\_TMR5CLKPWR\_Pos)

[ 335](rts5912__clock_8h.md#ace804f0e0a45ac545687cbc3268ca1c2)#define PERIPH\_GRP1\_RTMR\_CLKPWR (PERICLKPWR1\_RTMRCLKPWR\_Pos)

[ 336](rts5912__clock_8h.md#a8153770ff686afc4a10a338f872e91d2)#define PERIPH\_GRP1\_SLWTMR0\_CLKPWR (PERICLKPWR1\_SLWTMR0CLKPWR\_Pos)

[ 337](rts5912__clock_8h.md#ac2140eecbb5c1c335ca3c80ca65e2c53)#define PERIPH\_GRP1\_SLWTMR1\_CLKPWR (PERICLKPWR1\_SLWTMR1CLKPWR\_Pos)

338

[ 339](rts5912__clock_8h.md#a14112702594e9e6cd023112b684fee36)#define PERIPH\_GRP2\_RTC\_CLKPWR (PERICLKPWR2\_RTCCLKPWR\_Pos)

[ 340](rts5912__clock_8h.md#ae864db6acb1dfa187f3427d780826935)#define PERIPH\_GRP2\_WDT\_CLKPWR (PERICLKPWR2\_WDTCLKPWR\_Pos)

[ 341](rts5912__clock_8h.md#a97e7326ae7da8cc26c6f5251d88ca136)#define PERIPH\_GRP2\_WDTPWRBTN\_CLKPWR (PERICLKPWR2\_PWRBTNCLKPWR\_Pos)

342

343#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RTS5912\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [rts5912\_clock.h](rts5912__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
