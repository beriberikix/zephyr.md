---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/microchip-xec-gpio_8h_source.html
original_path: doxygen/html/microchip-xec-gpio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

microchip-xec-gpio.h

[Go to the documentation of this file.](microchip-xec-gpio_8h.md)

1/\*

2 \* Copyright (c) 2022 Microchip Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_MICROCHIP\_XEC\_GPIO\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_MICROCHIP\_XEC\_GPIO\_H\_

8

24

[ 25](microchip-xec-gpio_8h.md#a69c98ccc691eadd9142b429436324393)#define XEC\_GPIO\_HELPER(gpio\_bank, gpio\_bitpos) gpio\_bank gpio\_bitpos

26

27/\* bank A \*/

[ 28](microchip-xec-gpio_8h.md#aa0f7a9481cc76c3a772611f4667e002a)#define MCHP\_GPIO\_DECODE\_000 XEC\_GPIO\_HELPER(&gpio\_000\_036, 0)

[ 29](microchip-xec-gpio_8h.md#a87098a7fbcebd0007441ae207447057f)#define MCHP\_GPIO\_DECODE\_001 XEC\_GPIO\_HELPER(&gpio\_000\_036, 1)

[ 30](microchip-xec-gpio_8h.md#ac04ab3fa9723df31ba3b70f67188faca)#define MCHP\_GPIO\_DECODE\_002 XEC\_GPIO\_HELPER(&gpio\_000\_036, 2)

[ 31](microchip-xec-gpio_8h.md#a28f8c7a9203b7bef7572b2df5ce589a4)#define MCHP\_GPIO\_DECODE\_003 XEC\_GPIO\_HELPER(&gpio\_000\_036, 3)

[ 32](microchip-xec-gpio_8h.md#a154887497f01954b53059b5b66cfc70f)#define MCHP\_GPIO\_DECODE\_004 XEC\_GPIO\_HELPER(&gpio\_000\_036, 4)

[ 33](microchip-xec-gpio_8h.md#a98b7317c7d523db4627a2de0560cdeca)#define MCHP\_GPIO\_DECODE\_005 XEC\_GPIO\_HELPER(&gpio\_000\_036, 5)

[ 34](microchip-xec-gpio_8h.md#a27d50c2e3c61a68b98ce3ee16b5568e0)#define MCHP\_GPIO\_DECODE\_006 XEC\_GPIO\_HELPER(&gpio\_000\_036, 6)

[ 35](microchip-xec-gpio_8h.md#a088920f061950553d93841ecd7d36276)#define MCHP\_GPIO\_DECODE\_007 XEC\_GPIO\_HELPER(&gpio\_000\_036, 7)

[ 36](microchip-xec-gpio_8h.md#a9c474cd63171ba19f7c49baf89adf3ab)#define MCHP\_GPIO\_DECODE\_010 XEC\_GPIO\_HELPER(&gpio\_000\_036, 8)

[ 37](microchip-xec-gpio_8h.md#ab633aa49870b2d0e44d97f8e895e1dee)#define MCHP\_GPIO\_DECODE\_011 XEC\_GPIO\_HELPER(&gpio\_000\_036, 9)

[ 38](microchip-xec-gpio_8h.md#a77791d566a3d298ab4e3e33a74aee75e)#define MCHP\_GPIO\_DECODE\_012 XEC\_GPIO\_HELPER(&gpio\_000\_036, 10)

[ 39](microchip-xec-gpio_8h.md#a967f91e5988e3bfceca1a30a5c49d57d)#define MCHP\_GPIO\_DECODE\_013 XEC\_GPIO\_HELPER(&gpio\_000\_036, 11)

[ 40](microchip-xec-gpio_8h.md#abb29103f77b886ff0f4906c507e00a19)#define MCHP\_GPIO\_DECODE\_014 XEC\_GPIO\_HELPER(&gpio\_000\_036, 12)

[ 41](microchip-xec-gpio_8h.md#a11ff7267f5d3e5f7e07293d4475c5db9)#define MCHP\_GPIO\_DECODE\_015 XEC\_GPIO\_HELPER(&gpio\_000\_036, 13)

[ 42](microchip-xec-gpio_8h.md#a383ed4e4bf32289ac4cb6853f94b587c)#define MCHP\_GPIO\_DECODE\_016 XEC\_GPIO\_HELPER(&gpio\_000\_036, 14)

[ 43](microchip-xec-gpio_8h.md#a710d26adfdf2f48ce6d114cf6fdb7694)#define MCHP\_GPIO\_DECODE\_017 XEC\_GPIO\_HELPER(&gpio\_000\_036, 15)

[ 44](microchip-xec-gpio_8h.md#a5601d1468c99faac26fb456d9e7e5e1c)#define MCHP\_GPIO\_DECODE\_020 XEC\_GPIO\_HELPER(&gpio\_000\_036, 16)

[ 45](microchip-xec-gpio_8h.md#a9d3e907e2911dadd8e78003f7a041d42)#define MCHP\_GPIO\_DECODE\_021 XEC\_GPIO\_HELPER(&gpio\_000\_036, 17)

[ 46](microchip-xec-gpio_8h.md#a6803a62f243ea184bd5cd37f6f5798bc)#define MCHP\_GPIO\_DECODE\_022 XEC\_GPIO\_HELPER(&gpio\_000\_036, 18)

[ 47](microchip-xec-gpio_8h.md#a7db838238a826a170b30b3ecd7dae127)#define MCHP\_GPIO\_DECODE\_023 XEC\_GPIO\_HELPER(&gpio\_000\_036, 19)

[ 48](microchip-xec-gpio_8h.md#afd0c2a7416d579d82f491fd2860f6939)#define MCHP\_GPIO\_DECODE\_024 XEC\_GPIO\_HELPER(&gpio\_000\_036, 20)

[ 49](microchip-xec-gpio_8h.md#a52271671fb3a6f8c6ee726d420c1b362)#define MCHP\_GPIO\_DECODE\_025 XEC\_GPIO\_HELPER(&gpio\_000\_036, 21)

[ 50](microchip-xec-gpio_8h.md#afd9b3bab23b7517e31af2f30ab17b020)#define MCHP\_GPIO\_DECODE\_026 XEC\_GPIO\_HELPER(&gpio\_000\_036, 22)

[ 51](microchip-xec-gpio_8h.md#aea2c921973f455fcd237ce2adf41cb77)#define MCHP\_GPIO\_DECODE\_027 XEC\_GPIO\_HELPER(&gpio\_000\_036, 23)

[ 52](microchip-xec-gpio_8h.md#a973028ac061f6e4d165bb31e3dfcd885)#define MCHP\_GPIO\_DECODE\_030 XEC\_GPIO\_HELPER(&gpio\_000\_036, 24)

[ 53](microchip-xec-gpio_8h.md#a4508738901e2152cd903e851fcf2de76)#define MCHP\_GPIO\_DECODE\_031 XEC\_GPIO\_HELPER(&gpio\_000\_036, 25)

[ 54](microchip-xec-gpio_8h.md#a924ec4aa19bc9855388d0c9f0953055f)#define MCHP\_GPIO\_DECODE\_032 XEC\_GPIO\_HELPER(&gpio\_000\_036, 26)

[ 55](microchip-xec-gpio_8h.md#a00603418923b177fcc2530ca380e98d9)#define MCHP\_GPIO\_DECODE\_033 XEC\_GPIO\_HELPER(&gpio\_000\_036, 27)

[ 56](microchip-xec-gpio_8h.md#ad9c002ac2d0cad1e2551b338eda45a88)#define MCHP\_GPIO\_DECODE\_034 XEC\_GPIO\_HELPER(&gpio\_000\_036, 28)

[ 57](microchip-xec-gpio_8h.md#a49efe11583be1a23932fa6ea8f34db71)#define MCHP\_GPIO\_DECODE\_035 XEC\_GPIO\_HELPER(&gpio\_000\_036, 29)

[ 58](microchip-xec-gpio_8h.md#a0ee1881cb77ef4a684faec75b19eb5a2)#define MCHP\_GPIO\_DECODE\_036 XEC\_GPIO\_HELPER(&gpio\_000\_036, 30)

59

60/\* bank B \*/

[ 61](microchip-xec-gpio_8h.md#a70927ebb1c2bc9ecfaf928456110f582)#define MCHP\_GPIO\_DECODE\_040 XEC\_GPIO\_HELPER(&gpio\_040\_076, 0)

[ 62](microchip-xec-gpio_8h.md#a9c04bf4304ad74ea2a1ae88381daaa8d)#define MCHP\_GPIO\_DECODE\_041 XEC\_GPIO\_HELPER(&gpio\_040\_076, 1)

[ 63](microchip-xec-gpio_8h.md#a8fce308269f9912e374da1d51c48f45b)#define MCHP\_GPIO\_DECODE\_042 XEC\_GPIO\_HELPER(&gpio\_040\_076, 2)

[ 64](microchip-xec-gpio_8h.md#aba0d86379c1d062d6f211557fd84f710)#define MCHP\_GPIO\_DECODE\_043 XEC\_GPIO\_HELPER(&gpio\_040\_076, 3)

[ 65](microchip-xec-gpio_8h.md#a7e076e60ae905d6cd3c7294a8956d1ce)#define MCHP\_GPIO\_DECODE\_044 XEC\_GPIO\_HELPER(&gpio\_040\_076, 4)

[ 66](microchip-xec-gpio_8h.md#aaefc331762ce067212400e866d0cbf8f)#define MCHP\_GPIO\_DECODE\_045 XEC\_GPIO\_HELPER(&gpio\_040\_076, 5)

[ 67](microchip-xec-gpio_8h.md#a8f89e272c8cd5a4828844ae85b3dd327)#define MCHP\_GPIO\_DECODE\_046 XEC\_GPIO\_HELPER(&gpio\_040\_076, 6)

[ 68](microchip-xec-gpio_8h.md#a988e250d5022d88189bfc15208fa92a0)#define MCHP\_GPIO\_DECODE\_047 XEC\_GPIO\_HELPER(&gpio\_040\_076, 7)

[ 69](microchip-xec-gpio_8h.md#af6ea093c200609d7478dd45e4c571546)#define MCHP\_GPIO\_DECODE\_050 XEC\_GPIO\_HELPER(&gpio\_040\_076, 8)

[ 70](microchip-xec-gpio_8h.md#a4ace253d330a95dbfdf48e303078a453)#define MCHP\_GPIO\_DECODE\_051 XEC\_GPIO\_HELPER(&gpio\_040\_076, 9)

[ 71](microchip-xec-gpio_8h.md#abfd53a3894d5caefdbee2fbba8358b5d)#define MCHP\_GPIO\_DECODE\_052 XEC\_GPIO\_HELPER(&gpio\_040\_076, 10)

[ 72](microchip-xec-gpio_8h.md#ae143d46a242204ff7b3791aab7a688da)#define MCHP\_GPIO\_DECODE\_053 XEC\_GPIO\_HELPER(&gpio\_040\_076, 11)

[ 73](microchip-xec-gpio_8h.md#aba980f57b624e7286cc4ab97626651db)#define MCHP\_GPIO\_DECODE\_054 XEC\_GPIO\_HELPER(&gpio\_040\_076, 12)

[ 74](microchip-xec-gpio_8h.md#a1e0dfdb10f3f40e50ae820fc213cec38)#define MCHP\_GPIO\_DECODE\_055 XEC\_GPIO\_HELPER(&gpio\_040\_076, 13)

[ 75](microchip-xec-gpio_8h.md#adc7831052a172c8070b5cb1ec5fb34ab)#define MCHP\_GPIO\_DECODE\_056 XEC\_GPIO\_HELPER(&gpio\_040\_076, 14)

[ 76](microchip-xec-gpio_8h.md#ae19d668ae0b87a3ec2b47c08c8709897)#define MCHP\_GPIO\_DECODE\_057 XEC\_GPIO\_HELPER(&gpio\_040\_076, 15)

[ 77](microchip-xec-gpio_8h.md#afa332a09f1ce9e2bb79252900d415d24)#define MCHP\_GPIO\_DECODE\_060 XEC\_GPIO\_HELPER(&gpio\_040\_076, 16)

[ 78](microchip-xec-gpio_8h.md#a65282755f50178864bdb5423c059fc9a)#define MCHP\_GPIO\_DECODE\_061 XEC\_GPIO\_HELPER(&gpio\_040\_076, 17)

[ 79](microchip-xec-gpio_8h.md#a9eb05d3e4e9194b80f95b1d00b58e8ac)#define MCHP\_GPIO\_DECODE\_062 XEC\_GPIO\_HELPER(&gpio\_040\_076, 18)

[ 80](microchip-xec-gpio_8h.md#aa8df2d343a7a51559229be5235d38f21)#define MCHP\_GPIO\_DECODE\_063 XEC\_GPIO\_HELPER(&gpio\_040\_076, 19)

[ 81](microchip-xec-gpio_8h.md#a46f28ee93abedda82071018c7261b104)#define MCHP\_GPIO\_DECODE\_064 XEC\_GPIO\_HELPER(&gpio\_040\_076, 20)

[ 82](microchip-xec-gpio_8h.md#ad60fc63de43e27793fc5df1fe1d9e946)#define MCHP\_GPIO\_DECODE\_065 XEC\_GPIO\_HELPER(&gpio\_040\_076, 21)

[ 83](microchip-xec-gpio_8h.md#a1f0005633f9221b1668785cd69a01166)#define MCHP\_GPIO\_DECODE\_066 XEC\_GPIO\_HELPER(&gpio\_040\_076, 22)

[ 84](microchip-xec-gpio_8h.md#aebd017c8fabeff9265f6eed41fa43a72)#define MCHP\_GPIO\_DECODE\_067 XEC\_GPIO\_HELPER(&gpio\_040\_076, 23)

[ 85](microchip-xec-gpio_8h.md#add80b8ed07f7d87c68a805c15c3da4b8)#define MCHP\_GPIO\_DECODE\_070 XEC\_GPIO\_HELPER(&gpio\_040\_076, 24)

[ 86](microchip-xec-gpio_8h.md#ab21aae4401bd0051aaf0b526b78ea964)#define MCHP\_GPIO\_DECODE\_071 XEC\_GPIO\_HELPER(&gpio\_040\_076, 25)

[ 87](microchip-xec-gpio_8h.md#aeb74ec1069ebdcd99d9698922d214dca)#define MCHP\_GPIO\_DECODE\_072 XEC\_GPIO\_HELPER(&gpio\_040\_076, 26)

[ 88](microchip-xec-gpio_8h.md#a12ad76aa553dd1bff71547e189f5d2bf)#define MCHP\_GPIO\_DECODE\_073 XEC\_GPIO\_HELPER(&gpio\_040\_076, 27)

[ 89](microchip-xec-gpio_8h.md#a780751e3203adc2556585ea3d1c6b41a)#define MCHP\_GPIO\_DECODE\_074 XEC\_GPIO\_HELPER(&gpio\_040\_076, 28)

[ 90](microchip-xec-gpio_8h.md#af53c7c4e8265a30c0a0aa83554b70816)#define MCHP\_GPIO\_DECODE\_075 XEC\_GPIO\_HELPER(&gpio\_040\_076, 29)

[ 91](microchip-xec-gpio_8h.md#aeae09d3e8185102fd82c647b11e398f2)#define MCHP\_GPIO\_DECODE\_076 XEC\_GPIO\_HELPER(&gpio\_040\_076, 30)

92

93/\* bank C \*/

[ 94](microchip-xec-gpio_8h.md#aa0ecec9c770e0b90c3a1b96df6a2ab98)#define MCHP\_GPIO\_DECODE\_100 XEC\_GPIO\_HELPER(&gpio\_100\_136, 0)

[ 95](microchip-xec-gpio_8h.md#ac423effd94fb4c7c50aecf0102d02347)#define MCHP\_GPIO\_DECODE\_101 XEC\_GPIO\_HELPER(&gpio\_100\_136, 1)

[ 96](microchip-xec-gpio_8h.md#a585e1d5ddb30b98acc187175cf8ca631)#define MCHP\_GPIO\_DECODE\_102 XEC\_GPIO\_HELPER(&gpio\_100\_136, 2)

[ 97](microchip-xec-gpio_8h.md#aeeed34c8c4bf617062bc3375bf521cc4)#define MCHP\_GPIO\_DECODE\_103 XEC\_GPIO\_HELPER(&gpio\_100\_136, 3)

[ 98](microchip-xec-gpio_8h.md#a76bbea75eac4cc2c72d8bb7938529df9)#define MCHP\_GPIO\_DECODE\_104 XEC\_GPIO\_HELPER(&gpio\_100\_136, 4)

[ 99](microchip-xec-gpio_8h.md#a2d0493301d1bab240fed6808134eb7d0)#define MCHP\_GPIO\_DECODE\_105 XEC\_GPIO\_HELPER(&gpio\_100\_136, 5)

[ 100](microchip-xec-gpio_8h.md#aa6274363015fc96b03421c33e8b5dea0)#define MCHP\_GPIO\_DECODE\_106 XEC\_GPIO\_HELPER(&gpio\_100\_136, 6)

[ 101](microchip-xec-gpio_8h.md#a35006c42934a7aaf1cdf1814a9fa0783)#define MCHP\_GPIO\_DECODE\_107 XEC\_GPIO\_HELPER(&gpio\_100\_136, 7)

[ 102](microchip-xec-gpio_8h.md#a7ce68013aa089e89579dcb8dca898b64)#define MCHP\_GPIO\_DECODE\_110 XEC\_GPIO\_HELPER(&gpio\_100\_136, 8)

[ 103](microchip-xec-gpio_8h.md#adb3e7195052858947bab5f1c893bd57c)#define MCHP\_GPIO\_DECODE\_111 XEC\_GPIO\_HELPER(&gpio\_100\_136, 9)

[ 104](microchip-xec-gpio_8h.md#a6611bde9d75e721a4d0f299f3003b4b7)#define MCHP\_GPIO\_DECODE\_112 XEC\_GPIO\_HELPER(&gpio\_100\_136, 10)

[ 105](microchip-xec-gpio_8h.md#a0aa0e8942cf567e876ae5936df08ae74)#define MCHP\_GPIO\_DECODE\_113 XEC\_GPIO\_HELPER(&gpio\_100\_136, 11)

[ 106](microchip-xec-gpio_8h.md#a688c8edaad7b3db35d7191d562424dc7)#define MCHP\_GPIO\_DECODE\_114 XEC\_GPIO\_HELPER(&gpio\_100\_136, 12)

[ 107](microchip-xec-gpio_8h.md#ae90ab1a3a3da2bde5c3d60e90dcfe7c3)#define MCHP\_GPIO\_DECODE\_115 XEC\_GPIO\_HELPER(&gpio\_100\_136, 13)

[ 108](microchip-xec-gpio_8h.md#a87e3f0330fbbd8c0771c6fe9873fc4db)#define MCHP\_GPIO\_DECODE\_116 XEC\_GPIO\_HELPER(&gpio\_100\_136, 14)

[ 109](microchip-xec-gpio_8h.md#ae46180de0032b0cbd57965723a907e58)#define MCHP\_GPIO\_DECODE\_117 XEC\_GPIO\_HELPER(&gpio\_100\_136, 15)

[ 110](microchip-xec-gpio_8h.md#ab57307a510dbfe4eaedcf4c3c0464300)#define MCHP\_GPIO\_DECODE\_120 XEC\_GPIO\_HELPER(&gpio\_100\_136, 16)

[ 111](microchip-xec-gpio_8h.md#aefdf175d1f9ddcee572fc04660182eb1)#define MCHP\_GPIO\_DECODE\_121 XEC\_GPIO\_HELPER(&gpio\_100\_136, 17)

[ 112](microchip-xec-gpio_8h.md#a3a041d5f345dc5abcce68ad4237fe993)#define MCHP\_GPIO\_DECODE\_122 XEC\_GPIO\_HELPER(&gpio\_100\_136, 18)

[ 113](microchip-xec-gpio_8h.md#a09064e65065f26bc736a22b73cf910ff)#define MCHP\_GPIO\_DECODE\_123 XEC\_GPIO\_HELPER(&gpio\_100\_136, 19)

[ 114](microchip-xec-gpio_8h.md#a4244a1eb54ae6f0a91cd1cd277aa169e)#define MCHP\_GPIO\_DECODE\_124 XEC\_GPIO\_HELPER(&gpio\_100\_136, 20)

[ 115](microchip-xec-gpio_8h.md#a0aef78141db0222a69e48913d1b7ebbe)#define MCHP\_GPIO\_DECODE\_125 XEC\_GPIO\_HELPER(&gpio\_100\_136, 21)

[ 116](microchip-xec-gpio_8h.md#a98cdd5de0fcfee8728fd441ce2673531)#define MCHP\_GPIO\_DECODE\_126 XEC\_GPIO\_HELPER(&gpio\_100\_136, 22)

[ 117](microchip-xec-gpio_8h.md#ad94188eb86cea0dd756e438b6f7fa4fe)#define MCHP\_GPIO\_DECODE\_127 XEC\_GPIO\_HELPER(&gpio\_100\_136, 23)

[ 118](microchip-xec-gpio_8h.md#aabe173a210ae6e39e643e3e64fe2d456)#define MCHP\_GPIO\_DECODE\_130 XEC\_GPIO\_HELPER(&gpio\_100\_136, 24)

[ 119](microchip-xec-gpio_8h.md#abc97c39d9efa6852e3c318d0d8134574)#define MCHP\_GPIO\_DECODE\_131 XEC\_GPIO\_HELPER(&gpio\_100\_136, 25)

[ 120](microchip-xec-gpio_8h.md#ae10f5b0678e2490d6de34c23a4bbb364)#define MCHP\_GPIO\_DECODE\_132 XEC\_GPIO\_HELPER(&gpio\_100\_136, 26)

[ 121](microchip-xec-gpio_8h.md#a81b9670bd3ad7b1c9f49cd0455f99b5e)#define MCHP\_GPIO\_DECODE\_133 XEC\_GPIO\_HELPER(&gpio\_100\_136, 27)

[ 122](microchip-xec-gpio_8h.md#a6a882eb1ff47ee44182f2d121fb57dc9)#define MCHP\_GPIO\_DECODE\_134 XEC\_GPIO\_HELPER(&gpio\_100\_136, 28)

[ 123](microchip-xec-gpio_8h.md#a14ea31e18f615f99a4eb829679d86952)#define MCHP\_GPIO\_DECODE\_135 XEC\_GPIO\_HELPER(&gpio\_100\_136, 29)

[ 124](microchip-xec-gpio_8h.md#ab101dcf3775af52717d98b251255238e)#define MCHP\_GPIO\_DECODE\_136 XEC\_GPIO\_HELPER(&gpio\_100\_136, 30)

125

126/\* bank D \*/

[ 127](microchip-xec-gpio_8h.md#af3641639b9c9a0e12d10afc59e888c75)#define MCHP\_GPIO\_DECODE\_140 XEC\_GPIO\_HELPER(&gpio\_140\_176, 0)

[ 128](microchip-xec-gpio_8h.md#a93d7c8305422b58bd02304350cc05a57)#define MCHP\_GPIO\_DECODE\_141 XEC\_GPIO\_HELPER(&gpio\_140\_176, 1)

[ 129](microchip-xec-gpio_8h.md#a73c788c00891484a1465485584b6618b)#define MCHP\_GPIO\_DECODE\_142 XEC\_GPIO\_HELPER(&gpio\_140\_176, 2)

[ 130](microchip-xec-gpio_8h.md#a7bf3114d1fdaa8027dc59ab744bbb5ca)#define MCHP\_GPIO\_DECODE\_143 XEC\_GPIO\_HELPER(&gpio\_140\_176, 3)

[ 131](microchip-xec-gpio_8h.md#aeb91799a5f77797395f708d2b694af9c)#define MCHP\_GPIO\_DECODE\_144 XEC\_GPIO\_HELPER(&gpio\_140\_176, 4)

[ 132](microchip-xec-gpio_8h.md#a7ad9362ce1125cd9bbdd70988af6a5b6)#define MCHP\_GPIO\_DECODE\_145 XEC\_GPIO\_HELPER(&gpio\_140\_176, 5)

[ 133](microchip-xec-gpio_8h.md#a8e68a03f59d33616428de1d8d83ede25)#define MCHP\_GPIO\_DECODE\_146 XEC\_GPIO\_HELPER(&gpio\_140\_176, 6)

[ 134](microchip-xec-gpio_8h.md#a7178d359db7762e03d6401edc86b7329)#define MCHP\_GPIO\_DECODE\_147 XEC\_GPIO\_HELPER(&gpio\_140\_176, 7)

[ 135](microchip-xec-gpio_8h.md#a621e6f9eb638be124576945f960ea9dd)#define MCHP\_GPIO\_DECODE\_150 XEC\_GPIO\_HELPER(&gpio\_140\_176, 8)

[ 136](microchip-xec-gpio_8h.md#a55747e32b0e979cf43e853087cf4be0c)#define MCHP\_GPIO\_DECODE\_151 XEC\_GPIO\_HELPER(&gpio\_140\_176, 9)

[ 137](microchip-xec-gpio_8h.md#aaf3836978c0c7536451c62fd40206683)#define MCHP\_GPIO\_DECODE\_152 XEC\_GPIO\_HELPER(&gpio\_140\_176, 10)

[ 138](microchip-xec-gpio_8h.md#aacd6bd495782155a8789e507d31fd422)#define MCHP\_GPIO\_DECODE\_153 XEC\_GPIO\_HELPER(&gpio\_140\_176, 11)

[ 139](microchip-xec-gpio_8h.md#afdbc9f3bbccbb817003b68bc8326dcda)#define MCHP\_GPIO\_DECODE\_154 XEC\_GPIO\_HELPER(&gpio\_140\_176, 12)

[ 140](microchip-xec-gpio_8h.md#a5be4dd30d8b81ce06543311118a415b1)#define MCHP\_GPIO\_DECODE\_155 XEC\_GPIO\_HELPER(&gpio\_140\_176, 13)

[ 141](microchip-xec-gpio_8h.md#a6d504e1f77cf43177618fae361261e8c)#define MCHP\_GPIO\_DECODE\_156 XEC\_GPIO\_HELPER(&gpio\_140\_176, 14)

[ 142](microchip-xec-gpio_8h.md#a5101274f08935c705f50697a0e2a1894)#define MCHP\_GPIO\_DECODE\_157 XEC\_GPIO\_HELPER(&gpio\_140\_176, 15)

[ 143](microchip-xec-gpio_8h.md#ad2e20c7cda4f3ed47e854b4c676fa6bb)#define MCHP\_GPIO\_DECODE\_160 XEC\_GPIO\_HELPER(&gpio\_140\_176, 16)

[ 144](microchip-xec-gpio_8h.md#a4c84d8f45ed10d5b57dd1bab411bae35)#define MCHP\_GPIO\_DECODE\_161 XEC\_GPIO\_HELPER(&gpio\_140\_176, 17)

[ 145](microchip-xec-gpio_8h.md#a9bbf8ea2fe678eac14837dda24455ee1)#define MCHP\_GPIO\_DECODE\_162 XEC\_GPIO\_HELPER(&gpio\_140\_176, 18)

[ 146](microchip-xec-gpio_8h.md#aed0081e7d859424249e7a54b21321bd7)#define MCHP\_GPIO\_DECODE\_163 XEC\_GPIO\_HELPER(&gpio\_140\_176, 19)

[ 147](microchip-xec-gpio_8h.md#a898d6142a3864d5640fd6ec96b2510a7)#define MCHP\_GPIO\_DECODE\_164 XEC\_GPIO\_HELPER(&gpio\_140\_176, 20)

[ 148](microchip-xec-gpio_8h.md#a80f62cf62430fd7309f07034d7798a40)#define MCHP\_GPIO\_DECODE\_165 XEC\_GPIO\_HELPER(&gpio\_140\_176, 21)

[ 149](microchip-xec-gpio_8h.md#a0b7336e747884732cd7dc76bbcf1a157)#define MCHP\_GPIO\_DECODE\_166 XEC\_GPIO\_HELPER(&gpio\_140\_176, 22)

[ 150](microchip-xec-gpio_8h.md#acfa144c14cb06800d483ffdf3ff69c7a)#define MCHP\_GPIO\_DECODE\_167 XEC\_GPIO\_HELPER(&gpio\_140\_176, 23)

[ 151](microchip-xec-gpio_8h.md#ac92ca8a4514a7e933124cb372db4bb5d)#define MCHP\_GPIO\_DECODE\_170 XEC\_GPIO\_HELPER(&gpio\_140\_176, 24)

[ 152](microchip-xec-gpio_8h.md#ae2fff1d8eba613786fb9cdcd74c0d495)#define MCHP\_GPIO\_DECODE\_171 XEC\_GPIO\_HELPER(&gpio\_140\_176, 25)

[ 153](microchip-xec-gpio_8h.md#a96a74b9c8017a426b6cdb6fc13be0698)#define MCHP\_GPIO\_DECODE\_172 XEC\_GPIO\_HELPER(&gpio\_140\_176, 26)

[ 154](microchip-xec-gpio_8h.md#a4b8cc3656e49db3a809f0e6a6967046f)#define MCHP\_GPIO\_DECODE\_173 XEC\_GPIO\_HELPER(&gpio\_140\_176, 27)

[ 155](microchip-xec-gpio_8h.md#af15d99dcdd17f9bf3dd528359e5190ee)#define MCHP\_GPIO\_DECODE\_174 XEC\_GPIO\_HELPER(&gpio\_140\_176, 28)

[ 156](microchip-xec-gpio_8h.md#a6eee564d7b986ac59536d30162b0bec7)#define MCHP\_GPIO\_DECODE\_175 XEC\_GPIO\_HELPER(&gpio\_140\_176, 29)

[ 157](microchip-xec-gpio_8h.md#af4ae4a060994aedbe60e9e121576eee4)#define MCHP\_GPIO\_DECODE\_176 XEC\_GPIO\_HELPER(&gpio\_140\_176, 30)

158

159/\* bank E \*/

[ 160](microchip-xec-gpio_8h.md#ad01d44d9911f7c3fbff0ad1434b4fcf7)#define MCHP\_GPIO\_DECODE\_200 XEC\_GPIO\_HELPER(&gpio\_200\_236, 0)

[ 161](microchip-xec-gpio_8h.md#a69ef26a4d2437e8557622ec68e46385a)#define MCHP\_GPIO\_DECODE\_201 XEC\_GPIO\_HELPER(&gpio\_200\_236, 1)

[ 162](microchip-xec-gpio_8h.md#aac66ae191e59d42550dd3d0dcf939de1)#define MCHP\_GPIO\_DECODE\_202 XEC\_GPIO\_HELPER(&gpio\_200\_236, 2)

[ 163](microchip-xec-gpio_8h.md#a081d7ae4c51f349583e0a11a2e0ae8ad)#define MCHP\_GPIO\_DECODE\_203 XEC\_GPIO\_HELPER(&gpio\_200\_236, 3)

[ 164](microchip-xec-gpio_8h.md#a0240abd6020c300377901c190ec9e42a)#define MCHP\_GPIO\_DECODE\_204 XEC\_GPIO\_HELPER(&gpio\_200\_236, 4)

[ 165](microchip-xec-gpio_8h.md#a6c8670db8e8f84a6b39a6ac26f04ca68)#define MCHP\_GPIO\_DECODE\_205 XEC\_GPIO\_HELPER(&gpio\_200\_236, 5)

[ 166](microchip-xec-gpio_8h.md#abbcc0cb13fc39093fca0392c32aed6bd)#define MCHP\_GPIO\_DECODE\_206 XEC\_GPIO\_HELPER(&gpio\_200\_236, 6)

[ 167](microchip-xec-gpio_8h.md#a58ed8c420a1db9a95c20c1a2778ca431)#define MCHP\_GPIO\_DECODE\_207 XEC\_GPIO\_HELPER(&gpio\_200\_236, 7)

[ 168](microchip-xec-gpio_8h.md#aa26ecbe5ea4b24b0710623a3082810ff)#define MCHP\_GPIO\_DECODE\_210 XEC\_GPIO\_HELPER(&gpio\_200\_236, 8)

[ 169](microchip-xec-gpio_8h.md#ad79f5be1aef6b9ebc1e11e51f6713917)#define MCHP\_GPIO\_DECODE\_211 XEC\_GPIO\_HELPER(&gpio\_200\_236, 9)

[ 170](microchip-xec-gpio_8h.md#aadb81465f8bd56e648f66c1df1c6a5c3)#define MCHP\_GPIO\_DECODE\_212 XEC\_GPIO\_HELPER(&gpio\_200\_236, 10)

[ 171](microchip-xec-gpio_8h.md#a8d035db275ad0371b00d46544b0a51b5)#define MCHP\_GPIO\_DECODE\_213 XEC\_GPIO\_HELPER(&gpio\_200\_236, 11)

[ 172](microchip-xec-gpio_8h.md#a074df94b41f46efdfd9e9d60599dca18)#define MCHP\_GPIO\_DECODE\_214 XEC\_GPIO\_HELPER(&gpio\_200\_236, 12)

[ 173](microchip-xec-gpio_8h.md#ad24890ab0e67d0336ef48abb652075d3)#define MCHP\_GPIO\_DECODE\_215 XEC\_GPIO\_HELPER(&gpio\_200\_236, 13)

[ 174](microchip-xec-gpio_8h.md#abe6ae6a64f1c3040e219a7ad74b9e0c6)#define MCHP\_GPIO\_DECODE\_216 XEC\_GPIO\_HELPER(&gpio\_200\_236, 14)

[ 175](microchip-xec-gpio_8h.md#a60529382213314feb37b6ee3a8ecfdf9)#define MCHP\_GPIO\_DECODE\_217 XEC\_GPIO\_HELPER(&gpio\_200\_236, 15)

[ 176](microchip-xec-gpio_8h.md#a0e8e0f2931fd3ce38e9d9a0251705c59)#define MCHP\_GPIO\_DECODE\_220 XEC\_GPIO\_HELPER(&gpio\_200\_236, 16)

[ 177](microchip-xec-gpio_8h.md#ac065df102a99bb07d0c9d3b2dac66efe)#define MCHP\_GPIO\_DECODE\_221 XEC\_GPIO\_HELPER(&gpio\_200\_236, 17)

[ 178](microchip-xec-gpio_8h.md#a6667ba3882bf5c3d0641e0a54e4d64dc)#define MCHP\_GPIO\_DECODE\_222 XEC\_GPIO\_HELPER(&gpio\_200\_236, 18)

[ 179](microchip-xec-gpio_8h.md#ab2b4229108700b060ab14e30077edcca)#define MCHP\_GPIO\_DECODE\_223 XEC\_GPIO\_HELPER(&gpio\_200\_236, 19)

[ 180](microchip-xec-gpio_8h.md#af06c852ef1742735c545671b0b836cd3)#define MCHP\_GPIO\_DECODE\_224 XEC\_GPIO\_HELPER(&gpio\_200\_236, 20)

[ 181](microchip-xec-gpio_8h.md#a1089350d0127edd9b70f7489fcab0216)#define MCHP\_GPIO\_DECODE\_225 XEC\_GPIO\_HELPER(&gpio\_200\_236, 21)

[ 182](microchip-xec-gpio_8h.md#ab068e15ec1b178b24ccc82b5fc9366a9)#define MCHP\_GPIO\_DECODE\_226 XEC\_GPIO\_HELPER(&gpio\_200\_236, 22)

[ 183](microchip-xec-gpio_8h.md#a419ece41a2e660bec0d500e82fec39d3)#define MCHP\_GPIO\_DECODE\_227 XEC\_GPIO\_HELPER(&gpio\_200\_236, 23)

[ 184](microchip-xec-gpio_8h.md#a4c14d910cbf8578aa36d6c7dc2691dc9)#define MCHP\_GPIO\_DECODE\_230 XEC\_GPIO\_HELPER(&gpio\_200\_236, 24)

[ 185](microchip-xec-gpio_8h.md#ae348591b8fbe1166502ded705f43614a)#define MCHP\_GPIO\_DECODE\_231 XEC\_GPIO\_HELPER(&gpio\_200\_236, 25)

[ 186](microchip-xec-gpio_8h.md#a68eb797554de2b3c92ed17732195aa0c)#define MCHP\_GPIO\_DECODE\_232 XEC\_GPIO\_HELPER(&gpio\_200\_236, 26)

[ 187](microchip-xec-gpio_8h.md#a6c42d0c8511c167cdad033f3169ad666)#define MCHP\_GPIO\_DECODE\_233 XEC\_GPIO\_HELPER(&gpio\_200\_236, 27)

[ 188](microchip-xec-gpio_8h.md#aaefaa02b60a3f5ac8f16807bdbaed9b1)#define MCHP\_GPIO\_DECODE\_234 XEC\_GPIO\_HELPER(&gpio\_200\_236, 28)

[ 189](microchip-xec-gpio_8h.md#aeee70dc28e54953d43e06130d836f919)#define MCHP\_GPIO\_DECODE\_235 XEC\_GPIO\_HELPER(&gpio\_200\_236, 29)

[ 190](microchip-xec-gpio_8h.md#afecb72e209ac2bfb41948ad87152c605)#define MCHP\_GPIO\_DECODE\_236 XEC\_GPIO\_HELPER(&gpio\_200\_236, 30)

191

192/\* bank F \*/

[ 193](microchip-xec-gpio_8h.md#a61112c5a82cfedbbafac79082d6a2f62)#define MCHP\_GPIO\_DECODE\_240 XEC\_GPIO\_HELPER(&gpio\_240\_276, 0)

[ 194](microchip-xec-gpio_8h.md#a04fcc8c2474ce86669720c06529da1c9)#define MCHP\_GPIO\_DECODE\_241 XEC\_GPIO\_HELPER(&gpio\_240\_276, 1)

[ 195](microchip-xec-gpio_8h.md#ab3fb5bdacffd509ea3a7fa6df3d10676)#define MCHP\_GPIO\_DECODE\_242 XEC\_GPIO\_HELPER(&gpio\_240\_276, 2)

[ 196](microchip-xec-gpio_8h.md#a45fa6f958b67d682d3d74fa05fa1925c)#define MCHP\_GPIO\_DECODE\_243 XEC\_GPIO\_HELPER(&gpio\_240\_276, 3)

[ 197](microchip-xec-gpio_8h.md#ab488285dd521cfe42a979e0a7be4cacb)#define MCHP\_GPIO\_DECODE\_244 XEC\_GPIO\_HELPER(&gpio\_240\_276, 4)

[ 198](microchip-xec-gpio_8h.md#ab99ba91fc85341ad6b99ca10b93026af)#define MCHP\_GPIO\_DECODE\_245 XEC\_GPIO\_HELPER(&gpio\_240\_276, 5)

[ 199](microchip-xec-gpio_8h.md#ac2897012f057854e06dca380bad5111a)#define MCHP\_GPIO\_DECODE\_246 XEC\_GPIO\_HELPER(&gpio\_240\_276, 6)

[ 200](microchip-xec-gpio_8h.md#a27c406ede84b243f45c8081dd6da8626)#define MCHP\_GPIO\_DECODE\_247 XEC\_GPIO\_HELPER(&gpio\_240\_276, 7)

[ 201](microchip-xec-gpio_8h.md#a3814f6531ca75f5e39c59315cdbafe54)#define MCHP\_GPIO\_DECODE\_250 XEC\_GPIO\_HELPER(&gpio\_240\_276, 8)

[ 202](microchip-xec-gpio_8h.md#a1e49d827da3638a6bed77313c1c8e774)#define MCHP\_GPIO\_DECODE\_251 XEC\_GPIO\_HELPER(&gpio\_240\_276, 9)

[ 203](microchip-xec-gpio_8h.md#a1c0868cb503de6283e3b6fe3d6e4ab3e)#define MCHP\_GPIO\_DECODE\_252 XEC\_GPIO\_HELPER(&gpio\_240\_276, 10)

[ 204](microchip-xec-gpio_8h.md#a4d2b3967218482c2c86badef1cf8fb7d)#define MCHP\_GPIO\_DECODE\_253 XEC\_GPIO\_HELPER(&gpio\_240\_276, 11)

[ 205](microchip-xec-gpio_8h.md#aad2a5bdb5cf1f9680191a9ad02cbe996)#define MCHP\_GPIO\_DECODE\_254 XEC\_GPIO\_HELPER(&gpio\_240\_276, 12)

[ 206](microchip-xec-gpio_8h.md#a2fb75fae177f3bb3efed994d4fc0b8e5)#define MCHP\_GPIO\_DECODE\_255 XEC\_GPIO\_HELPER(&gpio\_240\_276, 13)

[ 207](microchip-xec-gpio_8h.md#a52b5bbe922191cc2460edb7fd79fba20)#define MCHP\_GPIO\_DECODE\_256 XEC\_GPIO\_HELPER(&gpio\_240\_276, 14)

[ 208](microchip-xec-gpio_8h.md#a0b54c1e66fe2ebecc6b851f63e72a8c1)#define MCHP\_GPIO\_DECODE\_257 XEC\_GPIO\_HELPER(&gpio\_240\_276, 15)

[ 209](microchip-xec-gpio_8h.md#aabb4a8e34571b81d74fa9dbb93c8b01e)#define MCHP\_GPIO\_DECODE\_260 XEC\_GPIO\_HELPER(&gpio\_240\_276, 16)

[ 210](microchip-xec-gpio_8h.md#a6a3361eaad0cf9915c5bb3b8df2c0f80)#define MCHP\_GPIO\_DECODE\_261 XEC\_GPIO\_HELPER(&gpio\_240\_276, 17)

[ 211](microchip-xec-gpio_8h.md#af2cd3721efed2d6125990b469c2247a9)#define MCHP\_GPIO\_DECODE\_262 XEC\_GPIO\_HELPER(&gpio\_240\_276, 18)

[ 212](microchip-xec-gpio_8h.md#acec04013989cdc36dd9fc75d2a188e94)#define MCHP\_GPIO\_DECODE\_263 XEC\_GPIO\_HELPER(&gpio\_240\_276, 19)

[ 213](microchip-xec-gpio_8h.md#a5c920d140bf665aa4d52151201147759)#define MCHP\_GPIO\_DECODE\_264 XEC\_GPIO\_HELPER(&gpio\_240\_276, 20)

[ 214](microchip-xec-gpio_8h.md#a69780b1dea7c5ffca5954349149bd4fe)#define MCHP\_GPIO\_DECODE\_265 XEC\_GPIO\_HELPER(&gpio\_240\_276, 21)

[ 215](microchip-xec-gpio_8h.md#a4220201c686a34ba813413e3f9a8c339)#define MCHP\_GPIO\_DECODE\_266 XEC\_GPIO\_HELPER(&gpio\_240\_276, 22)

[ 216](microchip-xec-gpio_8h.md#aafa28dcb1edc9d915226194c78d780da)#define MCHP\_GPIO\_DECODE\_267 XEC\_GPIO\_HELPER(&gpio\_240\_276, 23)

[ 217](microchip-xec-gpio_8h.md#a95fbbd8c0ec9076b500ba336ac3fb893)#define MCHP\_GPIO\_DECODE\_270 XEC\_GPIO\_HELPER(&gpio\_240\_276, 24)

[ 218](microchip-xec-gpio_8h.md#ad55bb4807e360fd7f9f773bc556d6170)#define MCHP\_GPIO\_DECODE\_271 XEC\_GPIO\_HELPER(&gpio\_240\_276, 25)

[ 219](microchip-xec-gpio_8h.md#ac8c9fab2e36e54a5fa2a1fad061760eb)#define MCHP\_GPIO\_DECODE\_272 XEC\_GPIO\_HELPER(&gpio\_240\_276, 26)

[ 220](microchip-xec-gpio_8h.md#a580f6d6827ecf2a468a0588d10cf8a2f)#define MCHP\_GPIO\_DECODE\_273 XEC\_GPIO\_HELPER(&gpio\_240\_276, 27)

[ 221](microchip-xec-gpio_8h.md#ac250b49520a632b70cf98fc9c4d9d1c4)#define MCHP\_GPIO\_DECODE\_274 XEC\_GPIO\_HELPER(&gpio\_240\_276, 28)

[ 222](microchip-xec-gpio_8h.md#a9afb687008113c5cfe3a7a4d9eab3176)#define MCHP\_GPIO\_DECODE\_275 XEC\_GPIO\_HELPER(&gpio\_240\_276, 29)

[ 223](microchip-xec-gpio_8h.md#ade89090d55794aa8efa86580a72778ee)#define MCHP\_GPIO\_DECODE\_276 XEC\_GPIO\_HELPER(&gpio\_240\_276, 30)

224

226

227#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_GPIO\_MICROCHIP\_XEC\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [microchip-xec-gpio.h](microchip-xec-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
