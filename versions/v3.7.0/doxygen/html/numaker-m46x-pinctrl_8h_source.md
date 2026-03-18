---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/numaker-m46x-pinctrl_8h_source.html
original_path: doxygen/html/numaker-m46x-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numaker-m46x-pinctrl.h

[Go to the documentation of this file.](numaker-m46x-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2023 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NUMAKER\_M46X\_PINCTRL\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NUMAKER\_M46X\_PINCTRL\_H

9

10/\* Beginning of M460 BSP sys\_reg.h pin-mux module copy \*/

11

[ 12](numaker-m46x-pinctrl_8h.md#a5d1bfd028ab555efc6d55bf80722158a)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos (0)

[ 13](numaker-m46x-pinctrl_8h.md#aae9b69d6daf1f32b051c9a391844877d)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos (8)

[ 14](numaker-m46x-pinctrl_8h.md#ab6cceb24dd6706c487968e0b8e58d13e)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos (16)

[ 15](numaker-m46x-pinctrl_8h.md#a06e4d6b5864c38522672cad66a1b5ccb)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos (24)

[ 16](numaker-m46x-pinctrl_8h.md#a42635b01064d1720c8ec7c4a462b4384)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos (0)

[ 17](numaker-m46x-pinctrl_8h.md#a37dc89534e8cebd55b4327b08425d01e)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos (8)

[ 18](numaker-m46x-pinctrl_8h.md#a695ddf7c7881c245613b09298c4982d7)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos (16)

[ 19](numaker-m46x-pinctrl_8h.md#a017f8ae11973f6ef6e6c851bcb030822)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos (24)

[ 20](numaker-m46x-pinctrl_8h.md#a2c4f4fb0d0e0704cbb0237d2496ddcac)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos (0)

[ 21](numaker-m46x-pinctrl_8h.md#ac89ab5555da1621120c5ab975ad206d2)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos (8)

[ 22](numaker-m46x-pinctrl_8h.md#a7e82c75e802c85d030f18202cd6d6175)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos (16)

[ 23](numaker-m46x-pinctrl_8h.md#a34ef120c2479ce30f2180662b519a877)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos (24)

[ 24](numaker-m46x-pinctrl_8h.md#a38b8ce945c8c9f7615ac0ab5369557ae)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos (0)

[ 25](numaker-m46x-pinctrl_8h.md#ab3d10091ecd136996c070a174c6c4506)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos (8)

[ 26](numaker-m46x-pinctrl_8h.md#a5e36317f39273758fd509e585652154c)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos (16)

[ 27](numaker-m46x-pinctrl_8h.md#af9c8cccdad43cce354e79bddbd238b09)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos (24)

28

[ 29](numaker-m46x-pinctrl_8h.md#a47b46e9a5dd9d181dc1212bfe5d8b8d5)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos (0)

[ 30](numaker-m46x-pinctrl_8h.md#a8ef6348929882badee728a9500756332)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos (8)

[ 31](numaker-m46x-pinctrl_8h.md#a6c90b77f3faabb0dd63665bc1f50fd61)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos (16)

[ 32](numaker-m46x-pinctrl_8h.md#ab6dc77d06bc6e9c5e792cd4c9d80e1c8)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos (24)

[ 33](numaker-m46x-pinctrl_8h.md#af1944a6b544ea5aa92b6f2c16734ea11)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos (0)

[ 34](numaker-m46x-pinctrl_8h.md#a1ce3cff3bbf25518c0007f5e7fdc002c)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos (8)

[ 35](numaker-m46x-pinctrl_8h.md#ad3e288b4ce1a8b8763601fdeb0470bb0)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos (16)

[ 36](numaker-m46x-pinctrl_8h.md#a68f325289d428efa7d5a2ea96ab095b2)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos (24)

[ 37](numaker-m46x-pinctrl_8h.md#a92fcb560f0e8982cc0161437817c6d27)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos (0)

[ 38](numaker-m46x-pinctrl_8h.md#a552b3acd0f55d55bb51b6030b3482222)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos (8)

[ 39](numaker-m46x-pinctrl_8h.md#a33589987830f42e32e1a17ad789c11af)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos (16)

[ 40](numaker-m46x-pinctrl_8h.md#a1bc729f348c44f66c172ee3e82225c62)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos (24)

[ 41](numaker-m46x-pinctrl_8h.md#a679121d68712657480a6a2b728269abb)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos (0)

[ 42](numaker-m46x-pinctrl_8h.md#ad38fb452238f2fb1b0a04b709a978f06)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos (8)

[ 43](numaker-m46x-pinctrl_8h.md#ac8f6085e7dbc65f04116b5de36f8fede)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos (16)

[ 44](numaker-m46x-pinctrl_8h.md#ae6adab2035f00ea8c34285e8dc975f70)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos (24)

45

[ 46](numaker-m46x-pinctrl_8h.md#a74dde0de2ab2a9d21ed1b221bc5707d1)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos (0)

[ 47](numaker-m46x-pinctrl_8h.md#a716f82bd1c216ad2f9b4b95125d074b3)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos (8)

[ 48](numaker-m46x-pinctrl_8h.md#a1bf98f4dcb83a2c2db42f519da0cb03b)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos (16)

[ 49](numaker-m46x-pinctrl_8h.md#af8b162b511a7efb6648711932be7aad2)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos (24)

[ 50](numaker-m46x-pinctrl_8h.md#afd0b77163bb2260de0530840110be3f2)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos (0)

[ 51](numaker-m46x-pinctrl_8h.md#ac733b240b3a3b74f07e2b57007663493)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos (8)

[ 52](numaker-m46x-pinctrl_8h.md#ad1aeaaac29fb0dd87a4f7c5702845bff)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos (16)

[ 53](numaker-m46x-pinctrl_8h.md#ad8943373e9743e124f03a5f97aec6abe)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos (24)

[ 54](numaker-m46x-pinctrl_8h.md#aebe51e1f01e90b84432840b88308ec0f)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos (0)

[ 55](numaker-m46x-pinctrl_8h.md#ad66cb959aa3d9def15649472fe8e4866)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos (8)

[ 56](numaker-m46x-pinctrl_8h.md#a849b9fc4fd7bc1b73c4f072daa14bc63)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos (16)

[ 57](numaker-m46x-pinctrl_8h.md#a4efab154edc53550e3923f08578f7d2f)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos (24)

[ 58](numaker-m46x-pinctrl_8h.md#ae66bc2272dac235eaf2f33f6e79b2228)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos (0)

[ 59](numaker-m46x-pinctrl_8h.md#abf0e63e9e8e111d0d9ed404fbb3d8ecc)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos (8)

[ 60](numaker-m46x-pinctrl_8h.md#a27258a4cfe450bc6c52c6854539e4adf)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos (16)

61

[ 62](numaker-m46x-pinctrl_8h.md#a6daec9b33bb5cc8044880add62a6df2b)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos (0)

[ 63](numaker-m46x-pinctrl_8h.md#a1ff6108d8ad02eb32748ac723e511256)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos (8)

[ 64](numaker-m46x-pinctrl_8h.md#a425e2676e7bc3cac3ddd0c47acdbe578)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos (16)

[ 65](numaker-m46x-pinctrl_8h.md#a4aa1cb16a09e5f97c2ee525c35e52d89)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos (24)

[ 66](numaker-m46x-pinctrl_8h.md#a23a9b1145d9af4e139d3bc49d744da19)#define NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_Pos (0)

[ 67](numaker-m46x-pinctrl_8h.md#ad25e1b0270636622629bf2ceacf51d26)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos (8)

[ 68](numaker-m46x-pinctrl_8h.md#a8261ad559c493b1643df57ea34e85156)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos (16)

[ 69](numaker-m46x-pinctrl_8h.md#ac8a46d07e124ed79b09ba4ceeee233ec)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos (24)

[ 70](numaker-m46x-pinctrl_8h.md#a75a66e358f41d8fd452ecbfbeaa5639d)#define NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_Pos (0)

[ 71](numaker-m46x-pinctrl_8h.md#ae37e71a8f6a61436e6198b96fd49c61d)#define NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_Pos (8)

[ 72](numaker-m46x-pinctrl_8h.md#a89040b48f58984607db70de3397946a2)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos (16)

[ 73](numaker-m46x-pinctrl_8h.md#a3fefc08cd37e32ae05069eef29172b13)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos (24)

[ 74](numaker-m46x-pinctrl_8h.md#a7d6cf50a505dd8fa225daf2afacebf28)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos (0)

[ 75](numaker-m46x-pinctrl_8h.md#a6d4b8c2788ae3caf05330790751ed31f)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos (8)

[ 76](numaker-m46x-pinctrl_8h.md#a6d356ff39707bf0af1d3559837f40047)#define NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_Pos (16)

77

[ 78](numaker-m46x-pinctrl_8h.md#a73459e5cbd133053a5ff6e10c8de2e00)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos (0)

[ 79](numaker-m46x-pinctrl_8h.md#a5880a21dc8ba634722b2542031f31b1d)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos (8)

[ 80](numaker-m46x-pinctrl_8h.md#a0f0e692fc93298c8581308de0022fe53)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos (16)

[ 81](numaker-m46x-pinctrl_8h.md#a0ce061624dbefa711bf8507f9c3f193a)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos (24)

[ 82](numaker-m46x-pinctrl_8h.md#a2ef55375dacd47ce64a350c5432e4174)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos (0)

[ 83](numaker-m46x-pinctrl_8h.md#a1736c2fe022dcf4193cb018287706da9)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos (8)

[ 84](numaker-m46x-pinctrl_8h.md#a0e6376093d5f2d1f38a382da9991f103)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos (16)

[ 85](numaker-m46x-pinctrl_8h.md#aa4a79486cac0f1f65111db4777759de2)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos (24)

[ 86](numaker-m46x-pinctrl_8h.md#a4a54fd52f7c0e45b6fb70276156ff442)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos (0)

[ 87](numaker-m46x-pinctrl_8h.md#afef18be8d0f64a164fef579903827cc0)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos (8)

[ 88](numaker-m46x-pinctrl_8h.md#a98fb7bd5175960f617fe5bb88d988c1e)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos (16)

[ 89](numaker-m46x-pinctrl_8h.md#a45b8ae18637a0fcf21b346498796a96e)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos (24)

[ 90](numaker-m46x-pinctrl_8h.md#add49972d8c5fbde5c3171f7c03b1e5aa)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos (0)

[ 91](numaker-m46x-pinctrl_8h.md#a2798fcf580095dc9efa869b66d870737)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos (8)

[ 92](numaker-m46x-pinctrl_8h.md#a4bb4a6ed5bc84e3bf9878b6b8555d48c)#define NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_Pos (16)

[ 93](numaker-m46x-pinctrl_8h.md#a6892cc5ca2ac877a3e31ce620bf4a896)#define NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_Pos (24)

94

[ 95](numaker-m46x-pinctrl_8h.md#a62fbc046a8fc50f1fdb3a1ca6d432597)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos (0)

[ 96](numaker-m46x-pinctrl_8h.md#a6d100b4070f223d7cf544456606bfa2d)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos (8)

[ 97](numaker-m46x-pinctrl_8h.md#a423bea5c504bac2082d004321bfa797e)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos (16)

[ 98](numaker-m46x-pinctrl_8h.md#a512c4f0da249b1ca565fed89358d0ef3)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos (24)

[ 99](numaker-m46x-pinctrl_8h.md#abd71ad3bfab83689d4e72bd20c921b57)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos (0)

[ 100](numaker-m46x-pinctrl_8h.md#a72c85e7a2d63926e4da26513feb74633)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos (8)

[ 101](numaker-m46x-pinctrl_8h.md#ac86a75c45a134a9ebd714e23b17f7b7d)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos (16)

[ 102](numaker-m46x-pinctrl_8h.md#acd072a4c624aba6bd74efdf02ae7a876)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos (24)

[ 103](numaker-m46x-pinctrl_8h.md#a486f449a6aea04a5694d860aa54be829)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos (0)

[ 104](numaker-m46x-pinctrl_8h.md#afcf04cd289b21efd959ec1177d809b75)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos (8)

[ 105](numaker-m46x-pinctrl_8h.md#aa07f881a8a58d61dc0a57049e45f85ea)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos (16)

[ 106](numaker-m46x-pinctrl_8h.md#ad4fc2ec61028c0288b5a3a5277394136)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos (24)

107

[ 108](numaker-m46x-pinctrl_8h.md#ab86fb2dab91852f6f09a8422fb194f9d)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos (0)

[ 109](numaker-m46x-pinctrl_8h.md#a07e5796acb0c14cd2c764e0027abbf4f)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos (8)

[ 110](numaker-m46x-pinctrl_8h.md#a5dd5e8cf854f4269114476b14655c5ca)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos (16)

[ 111](numaker-m46x-pinctrl_8h.md#acc225b1af36db509b7bb30ef41dd6e3a)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos (24)

[ 112](numaker-m46x-pinctrl_8h.md#a283f7e6f4c993483f3615a4e0c99b4ec)#define NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_Pos (0)

[ 113](numaker-m46x-pinctrl_8h.md#ac00acca82a72c0a42598ba4e182f1cec)#define NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_Pos (8)

[ 114](numaker-m46x-pinctrl_8h.md#a688eea5fb3d43f0ff453fca82eafba12)#define NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_Pos (16)

[ 115](numaker-m46x-pinctrl_8h.md#ae1b55376fb1832a2b1a89419a0982cb9)#define NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_Pos (24)

[ 116](numaker-m46x-pinctrl_8h.md#af4e1d2a4d0f3a9ef44a4755908e11613)#define NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_Pos (0)

[ 117](numaker-m46x-pinctrl_8h.md#a4c811c972126bd6e5ab5fd6a9d123f3a)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos (8)

[ 118](numaker-m46x-pinctrl_8h.md#a47f82eedfa164fdc970756cd8294b5db)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos (16)

[ 119](numaker-m46x-pinctrl_8h.md#a7c2f8a6cb80ee917be879c2d11b57c93)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos (24)

[ 120](numaker-m46x-pinctrl_8h.md#ae25fe9f16ca5a9d39a04ff07e5d6a63a)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos (0)

[ 121](numaker-m46x-pinctrl_8h.md#a5d9c88fe7264d5659d609a815653f9db)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos (8)

[ 122](numaker-m46x-pinctrl_8h.md#a0a8ab370742d878cf8773b91c61a41a4)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos (16)

[ 123](numaker-m46x-pinctrl_8h.md#a484c00e582f19715ed3f44439f712639)#define NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_Pos (24)

124

[ 125](numaker-m46x-pinctrl_8h.md#a1b218af59b5cb00ed1dcebf1a7913cfc)#define NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_Pos (0)

[ 126](numaker-m46x-pinctrl_8h.md#aec65c6afb7d33c49335280e82aa57f69)#define NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_Pos (8)

[ 127](numaker-m46x-pinctrl_8h.md#aabb87e2229b3c8d594b96370e5016dd0)#define NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_Pos (16)

[ 128](numaker-m46x-pinctrl_8h.md#a237b0cdd4da2446137659275cd913c37)#define NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_Pos (24)

[ 129](numaker-m46x-pinctrl_8h.md#a584164a01603e34a72db08125e60952b)#define NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_Pos (0)

[ 130](numaker-m46x-pinctrl_8h.md#a6832369f6871814a61707c68f03b3ad7)#define NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_Pos (8)

[ 131](numaker-m46x-pinctrl_8h.md#a1eb0d6e1f1464ae374ca6121e7d3579c)#define NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_Pos (16)

[ 132](numaker-m46x-pinctrl_8h.md#aa7e8461b0043ac1e0fae64bc40821ba1)#define NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_Pos (24)

[ 133](numaker-m46x-pinctrl_8h.md#a4f155142f78ea9cdf88ebdcb47feb8f3)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos (0)

[ 134](numaker-m46x-pinctrl_8h.md#ac6d7acb38f7021dc8414ea943bf0387b)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos (8)

[ 135](numaker-m46x-pinctrl_8h.md#af506bdae7e84fdbe490f25cab3cdfdfb)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos (16)

[ 136](numaker-m46x-pinctrl_8h.md#aebc0c745d837d1863875c0f817cbd5eb)#define NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_Pos (24)

[ 137](numaker-m46x-pinctrl_8h.md#a810083cf7901a957b85f9e0c77835239)#define NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_Pos (0)

[ 138](numaker-m46x-pinctrl_8h.md#a1e95e2f0d620b9ffb203bbf82733fe5a)#define NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_Pos (8)

[ 139](numaker-m46x-pinctrl_8h.md#a4ff881dfbe141a9fb1c0427fe7a575a4)#define NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_Pos (16)

[ 140](numaker-m46x-pinctrl_8h.md#a7b9ae28ce1da7575d7b08bad912be2d1)#define NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_Pos (24)

141

[ 142](numaker-m46x-pinctrl_8h.md#ab2f5d613a658a4e4d028413d48a1a660)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos (16)

[ 143](numaker-m46x-pinctrl_8h.md#a63ddc37c067f20daef92374324970863)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos (24)

[ 144](numaker-m46x-pinctrl_8h.md#a6e0ff19882e287fdbdec5cd7c028f010)#define NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_Pos (0)

[ 145](numaker-m46x-pinctrl_8h.md#aae7b70d636a207e3317e3567e7a5cec8)#define NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_Pos (8)

[ 146](numaker-m46x-pinctrl_8h.md#aefcd6bf1b562ceafd045165adfdee148)#define NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_Pos (16)

[ 147](numaker-m46x-pinctrl_8h.md#a04f7a36ce4a6416d94808dcec31ba64d)#define NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_Pos (24)

[ 148](numaker-m46x-pinctrl_8h.md#a13ee564383e379283af7bea227ad54f1)#define NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_Pos (0)

[ 149](numaker-m46x-pinctrl_8h.md#abbbc9e505988dc83b0f0ed34dd67e596)#define NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_Pos (8)

[ 150](numaker-m46x-pinctrl_8h.md#ae54c9317d89a207a819c26ebbc849667)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos (16)

[ 151](numaker-m46x-pinctrl_8h.md#a8f016636853e9d2cac098e899502fc8c)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos (24)

152

[ 153](numaker-m46x-pinctrl_8h.md#abec5d11eefe0709efeba9a545e13d517)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_Pos (0)

[ 154](numaker-m46x-pinctrl_8h.md#ad0779024dd16290576b8f819b2c88687)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_Pos (8)

[ 155](numaker-m46x-pinctrl_8h.md#a93cdd18830fbb47f23395605150443b7)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_Pos (16)

[ 156](numaker-m46x-pinctrl_8h.md#aa9d1f7b06c686789473436bb70fbb9db)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_Pos (24)

[ 157](numaker-m46x-pinctrl_8h.md#a8612e2478b96ce44473726385ee6103f)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_Pos (0)

[ 158](numaker-m46x-pinctrl_8h.md#aaa13a43dba5992b93779d1e47ef01baf)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_Pos (8)

[ 159](numaker-m46x-pinctrl_8h.md#aec7d5d5363cf86caafb0aa8b8fcc5aa6)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_Pos (16)

[ 160](numaker-m46x-pinctrl_8h.md#a8ec2331ad57ed5d8b34e896a19b445f0)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_Pos (24)

[ 161](numaker-m46x-pinctrl_8h.md#ae425896cf2d787d410be6204f043eb81)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_Pos (0)

[ 162](numaker-m46x-pinctrl_8h.md#ae00d01c61cac401c49e217d87e87b59e)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_Pos (8)

[ 163](numaker-m46x-pinctrl_8h.md#ad31bbef25890ed7a7c205c580c9d0b5b)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos (16)

[ 164](numaker-m46x-pinctrl_8h.md#a83b881063937a015cfa9e0ab1a228744)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos (24)

[ 165](numaker-m46x-pinctrl_8h.md#af9d775a41d92b1e4198d7e821892d98a)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos (0)

[ 166](numaker-m46x-pinctrl_8h.md#a4c1a223f41d6fa532b76ea99c453507b)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_Pos (8)

167

168/\* End of M460 BSP sys\_reg.h pin-mux module copy \*/

169

170/\* Beginning of M460 BSP sys.h pin-mux module copy \*/

171

172/\*

173 \*----------------------------------------------------------------------------

174 \* Multi-Function constant definitions.

175 \*----------------------------------------------------------------------------

176 \*/

177

178/\* PA.0 MFP \*/

[ 179](numaker-m46x-pinctrl_8h.md#a5b2d49d10600e5f78fe079ed8ee63498)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 180](numaker-m46x-pinctrl_8h.md#a31a63f5db7764fa8938d6db62e6a4c41)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_SPIM\_MOSI (0x02UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 181](numaker-m46x-pinctrl_8h.md#a1df14f42f95c1de96cd0d5f3a0ddd3d8)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_QSPI0\_MOSI0 (0x03UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 182](numaker-m46x-pinctrl_8h.md#a76da0b990f83a1dc84283e111612685c)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_SPI0\_MOSI (0x04UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 183](numaker-m46x-pinctrl_8h.md#a21fde9500f303de10888b52c4777dab3)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_SD1\_DAT0 (0x05UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 184](numaker-m46x-pinctrl_8h.md#a735c6706ba7a103f962223696dfe0f9d)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_SC0\_CLK (0x06UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 185](numaker-m46x-pinctrl_8h.md#aa5446acf1d1bb4035a0b29eedad48a05)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_UART0\_RXD (0x07UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 186](numaker-m46x-pinctrl_8h.md#a8526a16df6a03d6b2694327f8e42ca81)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_UART1\_nRTS (0x08UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 187](numaker-m46x-pinctrl_8h.md#a7a8c38cc25e62ce96ef1485a043162b2)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_I2C2\_SDA (0x09UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 188](numaker-m46x-pinctrl_8h.md#afe4910f27b3bc9874afedead08cd447b)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_CCAP\_DATA6 (0x0aUL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 189](numaker-m46x-pinctrl_8h.md#a337604e045c72617623c6453b08ee23c)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_BPWM0\_CH0 (0x0cUL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 190](numaker-m46x-pinctrl_8h.md#a16c81a869d27b53e19ce073a43589861)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_EPWM0\_CH5 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 191](numaker-m46x-pinctrl_8h.md#a944c8a98369fc2e630b9c96e4eeca81b)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_EQEI3\_B (0x0eUL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 192](numaker-m46x-pinctrl_8h.md#a1b42db44ac2aa62b30c2813b482de78c)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_DAC0\_ST (0x0fUL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 193](numaker-m46x-pinctrl_8h.md#a7d483203719bd67f90e053f93bd56982)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_PSIO0\_CH7 (0x11UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

[ 194](numaker-m46x-pinctrl_8h.md#a087ba8fff6efabb560428c5879ada97c)#define NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_BMC19 (0x14UL << NUMAKER\_SYS\_GPA\_MFP0\_PA0MFP\_Pos)

195

196/\* PA.1 MFP \*/

[ 197](numaker-m46x-pinctrl_8h.md#a479b908037de81364624fb1776e73fae)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 198](numaker-m46x-pinctrl_8h.md#afce584ee57d3ed2bbd87f3bbe6525fa6)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_SPIM\_MISO (0x02UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 199](numaker-m46x-pinctrl_8h.md#a6f10178fcf61daa4a9134b423633651b)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_QSPI0\_MISO0 (0x03UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 200](numaker-m46x-pinctrl_8h.md#aa2ae1c6d8b163faa335db9c7ffc72ec1)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_SPI0\_MISO (0x04UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 201](numaker-m46x-pinctrl_8h.md#a8dd0b7fd13d7cc909b2c6f87642e59eb)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_SD1\_DAT1 (0x05UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 202](numaker-m46x-pinctrl_8h.md#a40f8a5b468dd8aa2310269dd89f09e35)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_SC0\_DAT (0x06UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 203](numaker-m46x-pinctrl_8h.md#a98cdab6e58f4b4303ffd5650c1371bf9)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_UART0\_TXD (0x07UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 204](numaker-m46x-pinctrl_8h.md#a097b0e0f45d782993edc15c984156e68)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_UART1\_nCTS (0x08UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 205](numaker-m46x-pinctrl_8h.md#ae65f505046d861922a175d35db0ad471)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_I2C2\_SCL (0x09UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 206](numaker-m46x-pinctrl_8h.md#ac69cf0dddfc8583d84d77706ebbeae9a)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_CCAP\_DATA7 (0x0aUL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 207](numaker-m46x-pinctrl_8h.md#acf71b59cfb5ba52bdabc78df69f32ab4)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_BPWM0\_CH1 (0x0cUL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 208](numaker-m46x-pinctrl_8h.md#a9b988ccf775430b7b981de9517050ad5)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_EPWM0\_CH4 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 209](numaker-m46x-pinctrl_8h.md#a4986413eac2c4a257f9a82fde7d45124)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_EQEI3\_A (0x0eUL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 210](numaker-m46x-pinctrl_8h.md#a8cb5c18f390ba14aabb06bfdaaf843e0)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_DAC1\_ST (0x0fUL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 211](numaker-m46x-pinctrl_8h.md#a91b229686baddbb28a163ee0ed0d3c3b)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_PSIO0\_CH6 (0x11UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

[ 212](numaker-m46x-pinctrl_8h.md#a611037dcfae0e46167544aa9d1198194)#define NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_BMC18 (0x14UL << NUMAKER\_SYS\_GPA\_MFP0\_PA1MFP\_Pos)

213

214/\* PA.2 MFP \*/

[ 215](numaker-m46x-pinctrl_8h.md#a2822a90ca75f984aaa38021d14dad969)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 216](numaker-m46x-pinctrl_8h.md#a0cce5f0201fcfa2562da0dc006629e65)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_SPIM\_CLK (0x02UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 217](numaker-m46x-pinctrl_8h.md#aedf4742a4d625c3cdf33e986db8067ed)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_QSPI0\_CLK (0x03UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 218](numaker-m46x-pinctrl_8h.md#ac7f6b8daff53e17411a734ada1fae3e1)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_SPI0\_CLK (0x04UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 219](numaker-m46x-pinctrl_8h.md#a48dabb1e771bc131782941a2b4ea9c94)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_SD1\_DAT2 (0x05UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 220](numaker-m46x-pinctrl_8h.md#aeaaf7eabd3b5d4a21d4f5b33555f0ad3)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_SC0\_RST (0x06UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 221](numaker-m46x-pinctrl_8h.md#aaa161648bcb942b84519a6acfb58b234)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_UART4\_RXD (0x07UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 222](numaker-m46x-pinctrl_8h.md#ad6a3a19396b69c1b00e14028f013a8c7)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_UART1\_RXD (0x08UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 223](numaker-m46x-pinctrl_8h.md#a77fcc34cb3b86af88c16e9ec106012f8)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_I2C1\_SDA (0x09UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 224](numaker-m46x-pinctrl_8h.md#a2922687de9c7c46b0aaf8f860a59dc79)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_I2C0\_SMBSUS (0x0aUL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 225](numaker-m46x-pinctrl_8h.md#a40ce3c27af466b05871c98ec650fb6b2)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_BPWM0\_CH2 (0x0cUL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 226](numaker-m46x-pinctrl_8h.md#aded87cb9dfaa39a1873e68da10fd0495)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_EPWM0\_CH3 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 227](numaker-m46x-pinctrl_8h.md#aace1fa7d25790f66adf6dd3c202c34d0)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_EQEI3\_INDEX (0x0eUL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 228](numaker-m46x-pinctrl_8h.md#a5f89f9dd7f21ac73383a2f7c60255569)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_PSIO0\_CH5 (0x11UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

[ 229](numaker-m46x-pinctrl_8h.md#a0d5794f16885c48aa3543d8e16fe2510)#define NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_BMC17 (0x14UL << NUMAKER\_SYS\_GPA\_MFP0\_PA2MFP\_Pos)

230

231/\* PA.3 MFP \*/

[ 232](numaker-m46x-pinctrl_8h.md#a7ea858f6f973677bd96f06217aa577f5)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 233](numaker-m46x-pinctrl_8h.md#ab30b39c7e29ba7d827199c1168185c2c)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_SPIM\_SS (0x02UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 234](numaker-m46x-pinctrl_8h.md#a9891a42218f531ddf3e613815328fe70)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_QSPI0\_SS (0x03UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 235](numaker-m46x-pinctrl_8h.md#a1d5110b6625e2d2ed5f6da66e6695b77)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_SPI0\_SS (0x04UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 236](numaker-m46x-pinctrl_8h.md#a9556295fba0e9a785b5006549f8fe8cc)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_SD1\_DAT3 (0x05UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 237](numaker-m46x-pinctrl_8h.md#a8406b8da1558f4615a12c4bba194852f)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_SC0\_PWR (0x06UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 238](numaker-m46x-pinctrl_8h.md#a8cddcd1576ad26ddf0c7d716b9032d66)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_UART4\_TXD (0x07UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 239](numaker-m46x-pinctrl_8h.md#ae6ed11bb881aec2494a0feb8715dc43f)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_UART1\_TXD (0x08UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 240](numaker-m46x-pinctrl_8h.md#a39c547d840ce8d4577d567b9e0d2e1ca)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_I2C1\_SCL (0x09UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 241](numaker-m46x-pinctrl_8h.md#a505b29282362609366f190380fd21a49)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_I2C0\_SMBAL (0x0aUL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 242](numaker-m46x-pinctrl_8h.md#af31ebcf29423900f25386244f9ba59ee)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_BPWM0\_CH3 (0x0cUL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 243](numaker-m46x-pinctrl_8h.md#ae491129b55a3f48ef0db8615a5e03368)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_EPWM0\_CH2 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 244](numaker-m46x-pinctrl_8h.md#a90f91b948d17293d3d904903553c23ad)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_EQEI0\_B (0x0eUL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 245](numaker-m46x-pinctrl_8h.md#ab8e13fd29ba9b318d162a65a669c5d1a)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_EPWM1\_BRAKE1 (0x0fUL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 246](numaker-m46x-pinctrl_8h.md#a9c8a51a3c97f12fc25a3ddb3c7ea653d)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_PSIO0\_CH4 (0x11UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

[ 247](numaker-m46x-pinctrl_8h.md#ae75cb7ed3b968fa0ed387b32f01ebc15)#define NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_BMC16 (0x14UL << NUMAKER\_SYS\_GPA\_MFP0\_PA3MFP\_Pos)

248

249/\* PA.4 MFP \*/

[ 250](numaker-m46x-pinctrl_8h.md#a7f12bedc1c1693c4ff9a4ed827eb1a77)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 251](numaker-m46x-pinctrl_8h.md#a3be8a20fd812b8201a50892a9c10c25b)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_SPIM\_D3 (0x02UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 252](numaker-m46x-pinctrl_8h.md#a7b9d654e804281d59cb5775f0f188eb7)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_QSPI0\_MOSI1 (0x03UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 253](numaker-m46x-pinctrl_8h.md#a75ea6581e408aef2303d0f57c389891d)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_SPI0\_I2SMCLK (0x04UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 254](numaker-m46x-pinctrl_8h.md#abc98737e1ea61490eff80d10fcad37fc)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_SD1\_CLK (0x05UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 255](numaker-m46x-pinctrl_8h.md#a76db6de2982c27b8593f505aefd2e56b)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_SC0\_nCD (0x06UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 256](numaker-m46x-pinctrl_8h.md#a5a06c9c203c3f80a4fc98712f04b1a3f)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_UART0\_nRTS (0x07UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 257](numaker-m46x-pinctrl_8h.md#a43997ba215271027ad62a0d0343bad23)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_UART5\_RXD (0x08UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 258](numaker-m46x-pinctrl_8h.md#af58ee3fa0ce6aec4d7c3a81a96478a5d)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_I2C0\_SDA (0x09UL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 259](numaker-m46x-pinctrl_8h.md#a882a38f13a2a88a31246a34fac60300e)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_CAN0\_RXD (0x0aUL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 260](numaker-m46x-pinctrl_8h.md#a04db7e7b384afbbd53e6a8a123487b07)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_UART0\_RXD (0x0bUL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 261](numaker-m46x-pinctrl_8h.md#a458cf6d98554bcfc02dce3fcccd5b46c)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_BPWM0\_CH4 (0x0cUL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 262](numaker-m46x-pinctrl_8h.md#aa774deebb94de1e03f403cc6c2d3a3bc)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_EPWM0\_CH1 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

[ 263](numaker-m46x-pinctrl_8h.md#a7cee520e2a64e39ddfeb244b397d10e5)#define NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_EQEI0\_A (0x0eUL << NUMAKER\_SYS\_GPA\_MFP1\_PA4MFP\_Pos)

264

265/\* PA.5 MFP \*/

[ 266](numaker-m46x-pinctrl_8h.md#a3855a9adf01f5910825533bc6e6b1b10)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 267](numaker-m46x-pinctrl_8h.md#a63c797ff309e041725bf426c35ef81e8)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_SPIM\_D2 (0x02UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 268](numaker-m46x-pinctrl_8h.md#a45d1363b921fb52b6e775acbf7ea2909)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_QSPI0\_MISO1 (0x03UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 269](numaker-m46x-pinctrl_8h.md#a42d57ed7d546091718677045d80057e2)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_SPI1\_I2SMCLK (0x04UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 270](numaker-m46x-pinctrl_8h.md#a6378e1aaa292acaa5b582da4b91aef9c)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_SD1\_CMD (0x05UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 271](numaker-m46x-pinctrl_8h.md#a0949ff1e3c1cf8e5f47ddb17c0cf1c5a)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_SC2\_nCD (0x06UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 272](numaker-m46x-pinctrl_8h.md#a20dbf094ed48ed06f7dd02663151ca9d)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_UART0\_nCTS (0x07UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 273](numaker-m46x-pinctrl_8h.md#a9198c01fe37eccdb8ff4ad4f28c16c6a)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_UART5\_TXD (0x08UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 274](numaker-m46x-pinctrl_8h.md#adf660746e1f999399a036768d54573f3)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_I2C0\_SCL (0x09UL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 275](numaker-m46x-pinctrl_8h.md#a30178662ad32f14f629e25d92b627534)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_CAN0\_TXD (0x0aUL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 276](numaker-m46x-pinctrl_8h.md#ab85247553299b7886b4c8d035c9f562c)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_UART0\_TXD (0x0bUL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 277](numaker-m46x-pinctrl_8h.md#a0381d03b391b50b12345e08452ebf220)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_BPWM0\_CH5 (0x0cUL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 278](numaker-m46x-pinctrl_8h.md#a15200f1b67c710619de99c620054761b)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_EPWM0\_CH0 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

[ 279](numaker-m46x-pinctrl_8h.md#a6e9a7c7f6edeb1cbf5a3e9aab79f1216)#define NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_EQEI0\_INDEX (0x0eUL << NUMAKER\_SYS\_GPA\_MFP1\_PA5MFP\_Pos)

280

281/\* PA.6 MFP \*/

[ 282](numaker-m46x-pinctrl_8h.md#a31fd8ff46994786a052931ff001ebdba)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 283](numaker-m46x-pinctrl_8h.md#a6e13c8ef8d8690a2e11ad35bcbcc3b76)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_EBI\_AD6 (0x02UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 284](numaker-m46x-pinctrl_8h.md#abd2573b6ff21d6195ed8aeac87ece5a2)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_EMAC0\_RMII\_RXERR (0x03UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 285](numaker-m46x-pinctrl_8h.md#ab9f2838c923c98aa05664b164e88203f)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_SPI1\_SS (0x04UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 286](numaker-m46x-pinctrl_8h.md#a8ad8e9eddc079321ce9228663b09cc1f)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_SD1\_nCD (0x05UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 287](numaker-m46x-pinctrl_8h.md#a5b68e8bccb8af82d43ce272b23f20ef0)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_SC2\_CLK (0x06UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 288](numaker-m46x-pinctrl_8h.md#a0a08b7dcfe6bed947488a5add315ef5c)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_UART0\_RXD (0x07UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 289](numaker-m46x-pinctrl_8h.md#ab460409715529333c78a7a6068ebc3fb)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_I2C1\_SDA (0x08UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 290](numaker-m46x-pinctrl_8h.md#a1be7559bd81fa168f1dd77a3c1050eb2)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_QSPI1\_MOSI1 (0x09UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 291](numaker-m46x-pinctrl_8h.md#a2024ef6be7be83eba83354ddcc17b9da)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_EPWM1\_CH5 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 292](numaker-m46x-pinctrl_8h.md#abe8f2a00d6d6f2c05dcaef3acb8cbe45)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_BPWM1\_CH3 (0x0cUL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 293](numaker-m46x-pinctrl_8h.md#a6593502804f1d1595b421a4ea4dec14a)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_ACMP1\_WLAT (0x0dUL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 294](numaker-m46x-pinctrl_8h.md#a383f7451eb786b6368bb352ed232fd25)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_TM3 (0x0eUL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 295](numaker-m46x-pinctrl_8h.md#a20fec1e40e8f69d8c11db9b52517b688)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_INT0 (0x0fUL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 296](numaker-m46x-pinctrl_8h.md#a6e7aab68bf3af356c9e1ce97510a3896)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_SPI5\_CLK (0x11UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 297](numaker-m46x-pinctrl_8h.md#a94412c8cc8f84a235cc4661af7ffbe6f)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_KPI\_COL0 (0x12UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 298](numaker-m46x-pinctrl_8h.md#a0d6c6922f028550313f2dd14dd18badd)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_SPI6\_CLK (0x13UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

[ 299](numaker-m46x-pinctrl_8h.md#a33d72af68bde48b18acbad1f058f86dd)#define NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_BMC15 (0x14UL << NUMAKER\_SYS\_GPA\_MFP1\_PA6MFP\_Pos)

300

301/\* PA.7 MFP \*/

[ 302](numaker-m46x-pinctrl_8h.md#a60a43fe9003a1b0aedac7d9b9324a098)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 303](numaker-m46x-pinctrl_8h.md#a4806b8a3ada2a48b00b887fbee84b22c)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_EBI\_AD7 (0x02UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 304](numaker-m46x-pinctrl_8h.md#ad5a1302e9652eed9a4973d9402621571)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_EMAC0\_RMII\_CRSDV (0x03UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 305](numaker-m46x-pinctrl_8h.md#a413bd93302bf86681ffc9862fb5e9a1a)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_SPI1\_CLK (0x04UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 306](numaker-m46x-pinctrl_8h.md#a89ca52fa62fb1ecd36ae32699c30851d)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_SC2\_DAT (0x06UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 307](numaker-m46x-pinctrl_8h.md#a0a6750fb6f4f84f746fbb771989b3b1d)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_UART0\_TXD (0x07UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 308](numaker-m46x-pinctrl_8h.md#ae2976ff6e89aeebfb5f35cb455d46422)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_I2C1\_SCL (0x08UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 309](numaker-m46x-pinctrl_8h.md#a50271e1b87fa3ddb09a7e0bc58f59094)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_QSPI1\_MISO1 (0x09UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 310](numaker-m46x-pinctrl_8h.md#a3c756b270ef1aed9c5b9fb7650056f6f)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_EPWM1\_CH4 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 311](numaker-m46x-pinctrl_8h.md#adb780b2607d06094d0803f30e358e910)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_BPWM1\_CH2 (0x0cUL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 312](numaker-m46x-pinctrl_8h.md#a6a370b868b71909e07f52374b2c00131)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_ACMP0\_WLAT (0x0dUL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 313](numaker-m46x-pinctrl_8h.md#a93a8f6c5f22fd1667253e37ba113a3bd)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_TM2 (0x0eUL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 314](numaker-m46x-pinctrl_8h.md#a30c126a76574682291f009c63b56b93c)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_INT1 (0x0fUL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 315](numaker-m46x-pinctrl_8h.md#a93f41400418fdcee33cd54e6805cd588)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_SPI5\_SS (0x11UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 316](numaker-m46x-pinctrl_8h.md#a8cc86c65f80ad3ddd167ffad69c03c3b)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_KPI\_COL1 (0x12UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 317](numaker-m46x-pinctrl_8h.md#aab5becb392dadffa62f6ff322144ffd5)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_SPI6\_SS (0x13UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

[ 318](numaker-m46x-pinctrl_8h.md#ae6083e9bc80e0bfd66e694769af49182)#define NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_BMC14 (0x14UL << NUMAKER\_SYS\_GPA\_MFP1\_PA7MFP\_Pos)

319

320/\* PA.8 MFP \*/

[ 321](numaker-m46x-pinctrl_8h.md#aa2e29583c2919cf7141413953291102a)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 322](numaker-m46x-pinctrl_8h.md#a077c7ed8450291e9199ca69b4968e2d2)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_EADC1\_CH4 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 323](numaker-m46x-pinctrl_8h.md#a58db1d64218ba4f49e7162231df9136a)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_EADC2\_CH4 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 324](numaker-m46x-pinctrl_8h.md#a47754a1c57dfd20f267036d2599ffbd9)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_EBI\_ALE (0x02UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 325](numaker-m46x-pinctrl_8h.md#a5364eecfc6b60a90b3183883bc98db27)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_SC2\_CLK (0x03UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 326](numaker-m46x-pinctrl_8h.md#af4eedf680694784a8284028b7aec9000)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_SPI2\_MOSI (0x04UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 327](numaker-m46x-pinctrl_8h.md#a09309c3fd603fde4123ab5ee177be3a7)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_SD1\_DAT0 (0x05UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 328](numaker-m46x-pinctrl_8h.md#a35159b9bb86262b391bc585ce1113fa6)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_USCI0\_CTL1 (0x06UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 329](numaker-m46x-pinctrl_8h.md#ac4b216a02dcc75f9b97f3975dd9364fb)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_UART1\_RXD (0x07UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 330](numaker-m46x-pinctrl_8h.md#aa12b3890a9ac6901f18d1b4da7712e76)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_UART7\_RXD (0x08UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 331](numaker-m46x-pinctrl_8h.md#ac8d45853a5dcc8e77170f9c904bccc7e)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_BPWM0\_CH3 (0x09UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 332](numaker-m46x-pinctrl_8h.md#a6e5b74fb2213d1a8d0f8620e352953b1)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_EQEI1\_B (0x0aUL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 333](numaker-m46x-pinctrl_8h.md#a3d3db84ab5ffda710d7446fa9fc55a8c)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_ECAP0\_IC2 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 334](numaker-m46x-pinctrl_8h.md#ac93ca4fb97d0efe4878b7f488cf5f198)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_I2S1\_DO (0x0cUL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 335](numaker-m46x-pinctrl_8h.md#a4038682ee51fe5c52359afd238e42ffb)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_TM3\_EXT (0x0dUL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 336](numaker-m46x-pinctrl_8h.md#ab34a0eac2ee49ad24cf56c1440fbc875)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_INT4 (0x0fUL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

[ 337](numaker-m46x-pinctrl_8h.md#a63b724f94804c064f562434de344f84f)#define NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_BMC9 (0x14UL << NUMAKER\_SYS\_GPA\_MFP2\_PA8MFP\_Pos)

338

339/\* PA.9 MFP \*/

[ 340](numaker-m46x-pinctrl_8h.md#a3d4885c9f3b5f62d24031a7b584910eb)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 341](numaker-m46x-pinctrl_8h.md#ae69c1262fbc4d367e379987a1f9cf8bf)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_EADC1\_CH5 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 342](numaker-m46x-pinctrl_8h.md#abca47f723d38b01cdfbf8bfffeb9c005)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_EADC2\_CH5 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 343](numaker-m46x-pinctrl_8h.md#a343dfe20b828c36429c963c12c0531c2)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_EBI\_MCLK (0x02UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 344](numaker-m46x-pinctrl_8h.md#ab6745a0fe5d69199083884e6b15d2db6)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_SC2\_DAT (0x03UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 345](numaker-m46x-pinctrl_8h.md#a5aa67a8402ec3d7b631c1666bd0d2359)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_SPI2\_MISO (0x04UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 346](numaker-m46x-pinctrl_8h.md#ad331a3577b52857d595dba7af1423ea4)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_SD1\_DAT1 (0x05UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 347](numaker-m46x-pinctrl_8h.md#adb6bde9a781d94d629d7cb5ce264a5d9)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_USCI0\_DAT1 (0x06UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 348](numaker-m46x-pinctrl_8h.md#a68e5092e6f1fd26b1d1b54f270995020)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_UART1\_TXD (0x07UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 349](numaker-m46x-pinctrl_8h.md#a57ca10dbc98beea22e8d24ea368b8b7a)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_UART7\_TXD (0x08UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 350](numaker-m46x-pinctrl_8h.md#ab3d3dc2de29672006c4e346a4e60587c)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_BPWM0\_CH2 (0x09UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 351](numaker-m46x-pinctrl_8h.md#a3ed0424775933d19c6241f7cd329d426)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_EQEI1\_A (0x0aUL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 352](numaker-m46x-pinctrl_8h.md#a546348465d10afc62bcb6366dbd48317)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_ECAP0\_IC1 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 353](numaker-m46x-pinctrl_8h.md#a27868a60e7c51ed3acb070dd7e20dcd2)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_I2S1\_DI (0x0cUL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 354](numaker-m46x-pinctrl_8h.md#a770824e40aa27847a6933701f796ce2a)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_TM2\_EXT (0x0dUL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 355](numaker-m46x-pinctrl_8h.md#ada64e6a916705e66f2bf0b7a9cc38437)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_SWDH\_DAT (0x0fUL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

[ 356](numaker-m46x-pinctrl_8h.md#a2e5843cdc0d0370118306f9b8592b496)#define NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_BMC8 (0x14UL << NUMAKER\_SYS\_GPA\_MFP2\_PA9MFP\_Pos)

357

358/\* PA.10 MFP \*/

[ 359](numaker-m46x-pinctrl_8h.md#a3d09ee771e6b5a03df7f27c538d408b2)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 360](numaker-m46x-pinctrl_8h.md#aa0547c3d095ea8a10646f650cf7351a3)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_EADC1\_CH6 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 361](numaker-m46x-pinctrl_8h.md#a72db0cb297b025c448ca288e11a49e9e)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_EADC2\_CH6 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 362](numaker-m46x-pinctrl_8h.md#a80008d8582e98b9883f2910ede7f27a4)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_ACMP1\_P0 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 363](numaker-m46x-pinctrl_8h.md#aa861903708dcaa0b469a2c855ca453c5)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_EBI\_nWR (0x02UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 364](numaker-m46x-pinctrl_8h.md#a6ef05faea33eed0e18a93e83fb85443b)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_SC2\_RST (0x03UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 365](numaker-m46x-pinctrl_8h.md#ac4ac5479cc128a83153a591f2a1cb45a)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_SPI2\_CLK (0x04UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 366](numaker-m46x-pinctrl_8h.md#ae5886b891dbcd135edfd6e16c8d7364b)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_SD1\_DAT2 (0x05UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 367](numaker-m46x-pinctrl_8h.md#aa54dd3acf5eb258137cfb110dd203c20)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_USCI0\_DAT0 (0x06UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 368](numaker-m46x-pinctrl_8h.md#a495a3a97b736fb3ce150bca056c0afc2)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_I2C2\_SDA (0x07UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 369](numaker-m46x-pinctrl_8h.md#aa32af842f30cb3224475e9138f693a76)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_UART6\_RXD (0x08UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 370](numaker-m46x-pinctrl_8h.md#a426b8652ce42673fefd08f120f418321)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_BPWM0\_CH1 (0x09UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 371](numaker-m46x-pinctrl_8h.md#a2ddcf70bcaac1b7877433d860863ebf8)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_EQEI1\_INDEX (0x0aUL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 372](numaker-m46x-pinctrl_8h.md#a9d98ba985dc1151084b233beb02fc610)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_ECAP0\_IC0 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 373](numaker-m46x-pinctrl_8h.md#ad4bf1e0bd666645cb86f1b69da1b3140)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_I2S1\_MCLK (0x0cUL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 374](numaker-m46x-pinctrl_8h.md#a092fe1aebba3fa1be374c76c12cf9f58)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_TM1\_EXT (0x0dUL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 375](numaker-m46x-pinctrl_8h.md#aaec4262995f9f04f725223f6b84b0f9e)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_DAC0\_ST (0x0eUL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 376](numaker-m46x-pinctrl_8h.md#ad5e77247dcfc1f513bedd4801cfdcc8b)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_SWDH\_CLK (0x0fUL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 377](numaker-m46x-pinctrl_8h.md#aed2e9bcf5275bd41f6552c2f12fdef37)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_KPI\_ROW5 (0x12UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

[ 378](numaker-m46x-pinctrl_8h.md#a4649843c0d7d28d29104a9c1c6847400)#define NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_BMC7 (0x14UL << NUMAKER\_SYS\_GPA\_MFP2\_PA10MFP\_Pos)

379

380/\* PA.11 MFP \*/

[ 381](numaker-m46x-pinctrl_8h.md#ae7785da604ace6e7decc04b4961fbbfc)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 382](numaker-m46x-pinctrl_8h.md#ae5f2648ad44647d9cddec24246261852)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_EADC1\_CH7 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 383](numaker-m46x-pinctrl_8h.md#aabf37dd81d87ae075a8ac187d65b7e8d)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_EADC2\_CH7 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 384](numaker-m46x-pinctrl_8h.md#a08f6391c4a2e1d62ab28d8e176bec245)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_ACMP0\_P0 (0x01UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 385](numaker-m46x-pinctrl_8h.md#aeb11b134ae2e92b40734e0bd8b52e0b4)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_EBI\_nRD (0x02UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 386](numaker-m46x-pinctrl_8h.md#a12a8d550e1445b89e46c0c2a90c33058)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_SC2\_PWR (0x03UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 387](numaker-m46x-pinctrl_8h.md#a64ae32988ca437048f8f035074276b88)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_SPI2\_SS (0x04UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 388](numaker-m46x-pinctrl_8h.md#a6e0560264d5ef64e0089c2f3b7dd2c54)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_SD1\_DAT3 (0x05UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 389](numaker-m46x-pinctrl_8h.md#a2a7316aa54ce82ade86dcd38c7b31e00)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_USCI0\_CLK (0x06UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 390](numaker-m46x-pinctrl_8h.md#afa98dcc42c67c5808074cd9385111aad)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_I2C2\_SCL (0x07UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 391](numaker-m46x-pinctrl_8h.md#af1edcfd9cc4ce1f36b021c913225ef4f)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_UART6\_TXD (0x08UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 392](numaker-m46x-pinctrl_8h.md#aa672051a13332a18a831ac5aaf5b3e50)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_BPWM0\_CH0 (0x09UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 393](numaker-m46x-pinctrl_8h.md#a532f6a2b569efbf2425a3bc469fdc8c0)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_EPWM0\_SYNC\_OUT (0x0aUL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 394](numaker-m46x-pinctrl_8h.md#a29b691e33193159736e011ae4d525a52)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_I2S1\_BCLK (0x0cUL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 395](numaker-m46x-pinctrl_8h.md#a3044b5377c591081b6dda11d4571b612)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_TM0\_EXT (0x0dUL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 396](numaker-m46x-pinctrl_8h.md#ae368986ba2d41a1e713970dffac079b1)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_DAC1\_ST (0x0eUL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 397](numaker-m46x-pinctrl_8h.md#a28ce07138fde0eb8205ac2cf240ba816)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_KPI\_ROW4 (0x12UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

[ 398](numaker-m46x-pinctrl_8h.md#a7901217050526e85327566ab0397a14d)#define NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_BMC6 (0x14UL << NUMAKER\_SYS\_GPA\_MFP2\_PA11MFP\_Pos)

399

400/\* PA.12 MFP \*/

[ 401](numaker-m46x-pinctrl_8h.md#ac97e113f8a48e58793cf9bdad6dfb2b3)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 402](numaker-m46x-pinctrl_8h.md#a28b1d0f04a8dc1cd039d8a3f4350186d)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_I2S0\_BCLK (0x02UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 403](numaker-m46x-pinctrl_8h.md#a25f394e0016133f37f90e89eefbd0b06)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_UART4\_TXD (0x03UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 404](numaker-m46x-pinctrl_8h.md#ae04401011ef04e81cc4c5ab759f729aa)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_I2C1\_SCL (0x04UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 405](numaker-m46x-pinctrl_8h.md#ad7190c2239f14bf11f1cacd290526142)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_SPI2\_SS (0x05UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 406](numaker-m46x-pinctrl_8h.md#aa43a97a94f292b762e6e50663f889477)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_CAN0\_TXD (0x06UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 407](numaker-m46x-pinctrl_8h.md#ac249ea56fc89f0dbc0f24723fa8ba6c5)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_SC2\_PWR (0x07UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 408](numaker-m46x-pinctrl_8h.md#a3a5d2a58624e105dd9a7da276f884d12)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_SD1\_nCD (0x08UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 409](numaker-m46x-pinctrl_8h.md#a79c414e2ec6910472f4fa599c8f44746)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_SPI0\_SS (0x09UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 410](numaker-m46x-pinctrl_8h.md#a0f388cedee5e7e0518750b238a81d044)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_QSPI1\_MISO0 (0x0aUL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 411](numaker-m46x-pinctrl_8h.md#adc6fa54a33658158b85c653e199cc8f5)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_BPWM1\_CH2 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 412](numaker-m46x-pinctrl_8h.md#a1abde42efb2eefb84a7101337efbd8cc)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_EQEI1\_INDEX (0x0cUL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 413](numaker-m46x-pinctrl_8h.md#aac7c2bad863c101c3d4202a3c4f571fa)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_ECAP3\_IC0 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 414](numaker-m46x-pinctrl_8h.md#a48e5c0bd43729c1277125d3f6e5c74ef)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_USB\_VBUS (0x0eUL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 415](numaker-m46x-pinctrl_8h.md#a869e77caaf9ec7893b0ab45e10f1d422)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_PSIO0\_CH4 (0x11UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 416](numaker-m46x-pinctrl_8h.md#a868ec8636b95fc255fcd5be5354c8fb0)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_SPI10\_SS (0x13UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

[ 417](numaker-m46x-pinctrl_8h.md#a91492da0f65f4f4a4bdc5c7274d86b1a)#define NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_BMC12 (0x14UL << NUMAKER\_SYS\_GPA\_MFP3\_PA12MFP\_Pos)

418

419/\* PA.13 MFP \*/

[ 420](numaker-m46x-pinctrl_8h.md#a490691142988a88c40ac34f10da66291)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 421](numaker-m46x-pinctrl_8h.md#aa9ae32a6179fe4ff68b55cb7cc49748d)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_I2S0\_MCLK (0x02UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 422](numaker-m46x-pinctrl_8h.md#a15cd6e333e953187390e85dd2ae7e708)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_UART4\_RXD (0x03UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 423](numaker-m46x-pinctrl_8h.md#a31c664e0a4674d5b6e7d9de536d55594)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_I2C1\_SDA (0x04UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 424](numaker-m46x-pinctrl_8h.md#a44e0c70d7ff4b21c1ebb59ecfff945d1)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_SPI2\_CLK (0x05UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 425](numaker-m46x-pinctrl_8h.md#a3812c48ebb758f40c9948abd87893321)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_CAN0\_RXD (0x06UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 426](numaker-m46x-pinctrl_8h.md#ab87062f2d2bb3221d5028397d1078229)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_SC2\_RST (0x07UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 427](numaker-m46x-pinctrl_8h.md#a72cc1fe35f07f10dc47d8ce7de648a35)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_SPI0\_CLK (0x09UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 428](numaker-m46x-pinctrl_8h.md#ab113a9134d9847b0b44696fa78676a9b)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_QSPI1\_MOSI0 (0x0aUL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 429](numaker-m46x-pinctrl_8h.md#a9b38fd26d895d86600d5b403b68425b6)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_BPWM1\_CH3 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 430](numaker-m46x-pinctrl_8h.md#a81253ea7bf9e539474fcd4fb73f3c335)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_EQEI1\_A (0x0cUL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 431](numaker-m46x-pinctrl_8h.md#af3ff9d6f0491782f419d7c67b0a34893)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_ECAP3\_IC1 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 432](numaker-m46x-pinctrl_8h.md#a5837cd30e936e94a1c03961f46a98010)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_USB\_D\_N (0x0eUL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 433](numaker-m46x-pinctrl_8h.md#aad03d638e0bca2748d24da8bf35d6ee8)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_PSIO0\_CH5 (0x11UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 434](numaker-m46x-pinctrl_8h.md#ab1278022755f2451d366e5467669e529)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_SPI10\_CLK (0x13UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

[ 435](numaker-m46x-pinctrl_8h.md#a6dd2e17db71572d27c0a7e347a2e548a)#define NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_BMC13 (0x14UL << NUMAKER\_SYS\_GPA\_MFP3\_PA13MFP\_Pos)

436

437/\* PA.14 MFP \*/

[ 438](numaker-m46x-pinctrl_8h.md#a072f1ccae5fec090d10e16c8a0b616d0)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 439](numaker-m46x-pinctrl_8h.md#a8503e72dd647a449e028d89ee4a68ae8)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_I2S0\_DI (0x02UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 440](numaker-m46x-pinctrl_8h.md#a62a38ad31ca43c1b3521b72a2edce0a6)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_UART0\_TXD (0x03UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 441](numaker-m46x-pinctrl_8h.md#a00331a9a360fb1d556862d205807c86f)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_EBI\_AD5 (0x04UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 442](numaker-m46x-pinctrl_8h.md#ad2cf17dfa1ad369573064dfbae5cee2f)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_SPI2\_MISO (0x05UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 443](numaker-m46x-pinctrl_8h.md#a642f73a19157d4677271a57ebee3fadf)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_I2C2\_SCL (0x06UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 444](numaker-m46x-pinctrl_8h.md#af77d7de136d4f68a93c3857c87c10925)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_SC2\_DAT (0x07UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 445](numaker-m46x-pinctrl_8h.md#a9455c06d7d87d6dbc6d703a0f91e69b9)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_SPI0\_MISO (0x09UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 446](numaker-m46x-pinctrl_8h.md#a250372755370832250aa66f2b65ba123)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_BPWM1\_CH4 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 447](numaker-m46x-pinctrl_8h.md#a5727ab1f571489d4c840946b698fc3b9)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_EQEI1\_B (0x0cUL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 448](numaker-m46x-pinctrl_8h.md#abcce39696e1950b085643fd92051c5ac)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_ECAP3\_IC2 (0x0dUL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 449](numaker-m46x-pinctrl_8h.md#a38ebb8d90acbdbcd952a534d3acc960f)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_USB\_D\_P (0x0eUL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 450](numaker-m46x-pinctrl_8h.md#a725ea699cf6986ec2289c0d6f8dc8138)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_I2C0\_SCL (0x10UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 451](numaker-m46x-pinctrl_8h.md#a066cf83f4816d0ee24555e203b8ea63f)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_PSIO0\_CH6 (0x11UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 452](numaker-m46x-pinctrl_8h.md#a904c15e570cd05ad0a688ec6e1f734ff)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_SPI10\_MISO (0x13UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

[ 453](numaker-m46x-pinctrl_8h.md#af98150fc323d975cc3579ecc5a7b886e)#define NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_BMC14 (0x14UL << NUMAKER\_SYS\_GPA\_MFP3\_PA14MFP\_Pos)

454

455/\* PA.15 MFP \*/

[ 456](numaker-m46x-pinctrl_8h.md#a8bbcf29d68e029796fe70427f48aa29e)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 457](numaker-m46x-pinctrl_8h.md#a3756cab22b9ba59cdb5c8a870e68553f)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_I2S0\_DO (0x02UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 458](numaker-m46x-pinctrl_8h.md#a1e8e67d7ab08ec2cbe30e4ea6a934ea2)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_UART0\_RXD (0x03UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 459](numaker-m46x-pinctrl_8h.md#ad3102097d1ab4f65baab2adf0e8e7c24)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_SPIM\_MOSI (0x04UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 460](numaker-m46x-pinctrl_8h.md#a99b2d7c4042291ae101597fc9406872c)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_SPI2\_MOSI (0x05UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 461](numaker-m46x-pinctrl_8h.md#a905022e814edf78c6edc2e819cdc4047)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_I2C2\_SDA (0x06UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 462](numaker-m46x-pinctrl_8h.md#a38847a5f2b3378b1abfeeb715c2a6ead)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_SC2\_CLK (0x07UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 463](numaker-m46x-pinctrl_8h.md#a258e4722db9e0b1f9c2aef66680ca11b)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_SPI0\_MOSI (0x09UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 464](numaker-m46x-pinctrl_8h.md#ad016f55745998f03ee80b6f317477f07)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_BPWM1\_CH5 (0x0bUL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 465](numaker-m46x-pinctrl_8h.md#a26a58327aaf1a00c25bede2b88176413)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_EPWM0\_SYNC\_IN (0x0cUL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 466](numaker-m46x-pinctrl_8h.md#a9d5ad53845eec63a5b52acb8ddb186ce)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_EQEI3\_INDEX (0x0dUL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 467](numaker-m46x-pinctrl_8h.md#a90e6907074bca35b5be6de6fcd9a82e3)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_USB\_OTG\_ID (0x0eUL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 468](numaker-m46x-pinctrl_8h.md#a21f27536854ac2d9f2bb4de10852e21d)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_I2C0\_SDA (0x10UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 469](numaker-m46x-pinctrl_8h.md#a254a801be52c0d4a83aef01de3a4d0e0)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_PSIO0\_CH7 (0x11UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 470](numaker-m46x-pinctrl_8h.md#abbd76e2f973033b1aef3714ee82a0d68)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_SPI10\_MOSI (0x13UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

[ 471](numaker-m46x-pinctrl_8h.md#a2f3ea3b2450bd39b6a1804598db216c5)#define NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_BMC15 (0x14UL << NUMAKER\_SYS\_GPA\_MFP3\_PA15MFP\_Pos)

472

473/\* PB.0 MFP \*/

[ 474](numaker-m46x-pinctrl_8h.md#a53063851123c51da41e6b6ef1ff66322)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 475](numaker-m46x-pinctrl_8h.md#a8f12fb309d243d2da6c7f3835d204aa3)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_EADC0\_CH0 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 476](numaker-m46x-pinctrl_8h.md#ae524182b67baee733212edfa0a2e4304)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_EADC1\_CH8 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 477](numaker-m46x-pinctrl_8h.md#a0a001dcf9a633c93979c9f0a28fa0b96)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_EADC2\_CH8 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 478](numaker-m46x-pinctrl_8h.md#a6980f5e0a11c6916a2634dd117fd5aa1)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_ACMP3\_N (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 479](numaker-m46x-pinctrl_8h.md#a99736ae4381924f7f43310479b136176)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_EBI\_ADR9 (0x02UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 480](numaker-m46x-pinctrl_8h.md#a2b10a4d96ac1d987b524045a24f8f193)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_SD0\_CMD (0x03UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 481](numaker-m46x-pinctrl_8h.md#a8989d42ae9da434d758034020f89c8fd)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_SPI2\_I2SMCLK (0x04UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 482](numaker-m46x-pinctrl_8h.md#a53f078d996037db97b4da918eb38b821)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_USCI0\_CTL0 (0x06UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 483](numaker-m46x-pinctrl_8h.md#a4ea1a64fae6eb3d2c79e98451564e559)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_UART2\_RXD (0x07UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 484](numaker-m46x-pinctrl_8h.md#a5a7043ef74bd07bb1e8aee960c937ceb)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_SPI0\_I2SMCLK (0x08UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 485](numaker-m46x-pinctrl_8h.md#a9adb8786efbbb172653413ca9dfde0ca)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_I2C1\_SDA (0x09UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 486](numaker-m46x-pinctrl_8h.md#ac5d1d9d853f0892a3bce7ac0e9940cb9)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_I2S1\_LRCK (0x0aUL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 487](numaker-m46x-pinctrl_8h.md#a0aa2ef631c7069ea02bda1f1fa90d15a)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_EPWM0\_CH5 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 488](numaker-m46x-pinctrl_8h.md#aed181eed47c1646c3f6c0d49f3cdc653)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_EPWM1\_CH5 (0x0cUL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 489](numaker-m46x-pinctrl_8h.md#a90d687ec952227fbe9fd8f0d5faf0df4)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_EPWM0\_BRAKE1 (0x0dUL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 490](numaker-m46x-pinctrl_8h.md#a85ef1f9800ad7fdb254e2f98820d71cf)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_ACMP3\_O (0x0eUL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 491](numaker-m46x-pinctrl_8h.md#a496952e5a50821e66386a5453aa635c3)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_QSPI0\_MOSI1 (0x0fUL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 492](numaker-m46x-pinctrl_8h.md#a193bebefed3d836b69b8f932af77093a)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_KPI\_ROW3 (0x12UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 493](numaker-m46x-pinctrl_8h.md#a96dd2cc6bb4e44d3384a3dfc55f02ff4)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_SPI4\_MOSI (0x13UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

[ 494](numaker-m46x-pinctrl_8h.md#a40d5845ae484ded502bd09852ba27df3)#define NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_BMC5 (0x14UL << NUMAKER\_SYS\_GPB\_MFP0\_PB0MFP\_Pos)

495

496/\* PB.1 MFP \*/

[ 497](numaker-m46x-pinctrl_8h.md#a90ab4caf0cd78a66f20430f0ec4cc9f3)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 498](numaker-m46x-pinctrl_8h.md#a75f111d13af299a049299e89e3d486fe)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_EADC0\_CH1 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 499](numaker-m46x-pinctrl_8h.md#a2767a66a29c047ee31abbb96fbe0c79b)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_EADC1\_CH9 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 500](numaker-m46x-pinctrl_8h.md#ae394781f39cdf014dc507a3e8e78e87e)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_EADC2\_CH9 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 501](numaker-m46x-pinctrl_8h.md#a9b66484326dcd9b48de621a639815636)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_ACMP3\_P0 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 502](numaker-m46x-pinctrl_8h.md#ab5292f8d169751b2048cd3d4cd265e20)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_EBI\_ADR8 (0x02UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 503](numaker-m46x-pinctrl_8h.md#ac09b65fd6578261cc4e46b34287bd546)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_SD0\_CLK (0x03UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 504](numaker-m46x-pinctrl_8h.md#a9e2058a6461eba15f23e273fbd421b11)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_EMAC0\_RMII\_RXERR (0x04UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 505](numaker-m46x-pinctrl_8h.md#a7c01c7d8f5f7818495077f3e1ad8b712)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_SPI1\_I2SMCLK (0x05UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 506](numaker-m46x-pinctrl_8h.md#ad436ee2621b539aadfbff51fe7142cd6)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_SPI3\_I2SMCLK (0x06UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 507](numaker-m46x-pinctrl_8h.md#ae5f4e8e0f77b9f2922f962005ab0b16f)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_UART2\_TXD (0x07UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 508](numaker-m46x-pinctrl_8h.md#a33452812625d3b6f177dc02767ca053f)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_I2C1\_SCL (0x09UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 509](numaker-m46x-pinctrl_8h.md#aa0be139b5fef66734037f44509faa355)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_I2S0\_LRCK (0x0aUL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 510](numaker-m46x-pinctrl_8h.md#a0405a46cfa20bab896001a8c2da292e9)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_EPWM0\_CH4 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 511](numaker-m46x-pinctrl_8h.md#a2047f85c369e36611f690c5a772e9666)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_EPWM1\_CH4 (0x0cUL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 512](numaker-m46x-pinctrl_8h.md#a47378406c51faabdb411b1524f0a8385)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_EPWM0\_BRAKE0 (0x0dUL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 513](numaker-m46x-pinctrl_8h.md#a519e3ef61ce43a1f3ff9eeb1bb38c316)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_ACMP2\_O (0x0eUL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 514](numaker-m46x-pinctrl_8h.md#ac3a4daf1525b11b1d078b5d11a83cfed)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_QSPI0\_MISO1 (0x0fUL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 515](numaker-m46x-pinctrl_8h.md#a7b370b1865632ac486896eb76e9f3db4)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_KPI\_ROW2 (0x12UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 516](numaker-m46x-pinctrl_8h.md#a00044a9ac28842c6d078e9baf4010c00)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_SPI4\_MISO (0x13UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

[ 517](numaker-m46x-pinctrl_8h.md#ae2d677773369dab42fe1dbc558d0c5df)#define NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_BMC4 (0x14UL << NUMAKER\_SYS\_GPB\_MFP0\_PB1MFP\_Pos)

518

519/\* PB.2 MFP \*/

[ 520](numaker-m46x-pinctrl_8h.md#a43f974491fecba1dd17ba5b2a36f222e)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 521](numaker-m46x-pinctrl_8h.md#a5acf21abb35ebb1485c189cf1aa73fe9)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_EADC0\_CH2 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 522](numaker-m46x-pinctrl_8h.md#ae0dab6b3edb6dee4d72c73c054b01cdf)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_EADC1\_CH10 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 523](numaker-m46x-pinctrl_8h.md#af4b29ad4fe077ba771c493fe692e1b2b)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_ACMP0\_P1 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 524](numaker-m46x-pinctrl_8h.md#a961b6750364d79e9dfb942db8554d3dd)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_EBI\_ADR3 (0x02UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 525](numaker-m46x-pinctrl_8h.md#afe4674ceadffca5804757fd5cfbc62af)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_SD0\_DAT0 (0x03UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 526](numaker-m46x-pinctrl_8h.md#a9b226be3c0e3486fca6cdf1cd684888b)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_EMAC0\_RMII\_CRSDV (0x04UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 527](numaker-m46x-pinctrl_8h.md#a5523d004845f9d5a019fe80914dc54d3)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_SPI1\_SS (0x05UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 528](numaker-m46x-pinctrl_8h.md#a3a49705a3e20cd927b5e4faad4d6cc78)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_UART1\_RXD (0x06UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 529](numaker-m46x-pinctrl_8h.md#ac6369b9ec6e44f915cb2d9cf3b2c8f81)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_UART5\_nCTS (0x07UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 530](numaker-m46x-pinctrl_8h.md#a5582b94cd1fd99db4447f3a655a6eb6c)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_SC0\_PWR (0x09UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 531](numaker-m46x-pinctrl_8h.md#a01e0ff3679118ec4f4f1729be58060af)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_I2S0\_DO (0x0aUL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 532](numaker-m46x-pinctrl_8h.md#a8690716df4bee1172ac0fa8da2a91fe5)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_EPWM0\_CH3 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 533](numaker-m46x-pinctrl_8h.md#af8bfafa89ebb9fe05a4fd81a90ef57d7)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_I2C1\_SDA (0x0cUL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 534](numaker-m46x-pinctrl_8h.md#ad42eb203719c2243d8abd9d2cadd2cc0)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_TM3 (0x0eUL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 535](numaker-m46x-pinctrl_8h.md#acd61db045c225494477c788fe9495736)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_INT3 (0x0fUL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 536](numaker-m46x-pinctrl_8h.md#a5554cc5d006e67c550357c264d1f0542)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_PSIO0\_CH7 (0x11UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 537](numaker-m46x-pinctrl_8h.md#ae646fb06021c89ba975cc49caab337e5)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_KPI\_ROW1 (0x12UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 538](numaker-m46x-pinctrl_8h.md#a030fe39ce2ef75bdfe3bd6930de063eb)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_SPI4\_CLK (0x13UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

[ 539](numaker-m46x-pinctrl_8h.md#ac8ee03a36378c143358208a5322640b0)#define NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_BMC3 (0x14UL << NUMAKER\_SYS\_GPB\_MFP0\_PB2MFP\_Pos)

540

541/\* PB.3 MFP \*/

[ 542](numaker-m46x-pinctrl_8h.md#a56d5c8cc3e012a270d089422ec86772c)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 543](numaker-m46x-pinctrl_8h.md#adcd22573a8be02fac49531af62cdf926)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_EADC0\_CH3 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 544](numaker-m46x-pinctrl_8h.md#a81bc69045013d96c49e8f2df25b346b0)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_EADC1\_CH11 (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 545](numaker-m46x-pinctrl_8h.md#a870f4f3fbb3ed45d8408ebe53e72c52e)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_ACMP0\_N (0x01UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 546](numaker-m46x-pinctrl_8h.md#a41bfa4c4b118b00e356c2bff958d206c)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_EBI\_ADR2 (0x02UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 547](numaker-m46x-pinctrl_8h.md#af9ad3254af9ee8a84092334cf2b7013d)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_SD0\_DAT1 (0x03UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 548](numaker-m46x-pinctrl_8h.md#ae6e6351247a93ddb827c222561382071)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_EMAC0\_RMII\_RXD1 (0x04UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 549](numaker-m46x-pinctrl_8h.md#aa98bcf92787cc1c298e06a79df57141c)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_SPI1\_CLK (0x05UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 550](numaker-m46x-pinctrl_8h.md#a897306fa512ce76cf9c70c7042f7cd53)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_UART1\_TXD (0x06UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 551](numaker-m46x-pinctrl_8h.md#a5e5e5c004c67656ad7da3eacbd6e325d)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_UART5\_nRTS (0x07UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 552](numaker-m46x-pinctrl_8h.md#ab90cd989aa7696ae5933f88f9ddd05b0)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_SC0\_RST (0x09UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 553](numaker-m46x-pinctrl_8h.md#a0dd4316ae86de66a738fdad05436382d)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_I2S0\_DI (0x0aUL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 554](numaker-m46x-pinctrl_8h.md#a3986f1aa4ea89678c3bbd7e8ea370903)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_EPWM0\_CH2 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 555](numaker-m46x-pinctrl_8h.md#a2bfdf741f8ec08b7ed8c4c8925a46973)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_I2C1\_SCL (0x0cUL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 556](numaker-m46x-pinctrl_8h.md#a30f68a692adec557a4e252d960d5ca8d)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_TM2 (0x0eUL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 557](numaker-m46x-pinctrl_8h.md#adfe52dc6ddeb96f04977ff30e02535a0)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_INT2 (0x0fUL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 558](numaker-m46x-pinctrl_8h.md#aea77323dd2eec254fa6a198bf387627a)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_PSIO0\_CH6 (0x11UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 559](numaker-m46x-pinctrl_8h.md#a2dbf9af1e4770a6d6b63918d40a045e2)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_KPI\_ROW0 (0x12UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 560](numaker-m46x-pinctrl_8h.md#a8511464a82487d917fbbdf6b1d3b2786)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_SPI4\_SS (0x13UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

[ 561](numaker-m46x-pinctrl_8h.md#a2fb2753f886291440a33b7efa7b49293)#define NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_BMC2 (0x14UL << NUMAKER\_SYS\_GPB\_MFP0\_PB3MFP\_Pos)

562

563/\* PB.4 MFP \*/

[ 564](numaker-m46x-pinctrl_8h.md#a3890ef9db88092619beef01c3729d985)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 565](numaker-m46x-pinctrl_8h.md#a163c865b6c748729f98f17a2d3683e84)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_EADC0\_CH4 (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 566](numaker-m46x-pinctrl_8h.md#a11c3dd1d5510c6b1051937db50ae899e)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_ACMP1\_P1 (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 567](numaker-m46x-pinctrl_8h.md#a84bd10ee1233c7b75a1f96808592319c)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_EBI\_ADR1 (0x02UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 568](numaker-m46x-pinctrl_8h.md#ad2909a8a3f76eb637f88dc250f296a4b)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_SD0\_DAT2 (0x03UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 569](numaker-m46x-pinctrl_8h.md#a32ea0fd98fcd6d759f1badbef836dcc6)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_EMAC0\_RMII\_RXD0 (0x04UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 570](numaker-m46x-pinctrl_8h.md#ace40e76b84919051616b3091c58578fc)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_SPI1\_MOSI (0x05UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 571](numaker-m46x-pinctrl_8h.md#a3a1e3b021a76002676e2a7d5de08fd9f)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_I2C0\_SDA (0x06UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 572](numaker-m46x-pinctrl_8h.md#a07443c6507029abf23683b489529baef)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_UART5\_RXD (0x07UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 573](numaker-m46x-pinctrl_8h.md#a9f2efe575358fe02b4fe036489dd9e03)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_SC0\_DAT (0x09UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 574](numaker-m46x-pinctrl_8h.md#a67406a0360f5c7d81e0cc1b9836d8ca3)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_I2S0\_MCLK (0x0aUL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 575](numaker-m46x-pinctrl_8h.md#ad4d45c02d89be9bb95d5469ba91d1b9a)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_EPWM0\_CH1 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 576](numaker-m46x-pinctrl_8h.md#ace2cb10dc7ba29e0398ab7feac686608)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_UART2\_RXD (0x0cUL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 577](numaker-m46x-pinctrl_8h.md#a7f1febf1cc1cd68af16b43ae0c786b3b)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_TM1 (0x0eUL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 578](numaker-m46x-pinctrl_8h.md#a1718a22cac3d557585f3339eb7171376)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_INT1 (0x0fUL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 579](numaker-m46x-pinctrl_8h.md#a5e35a2a15cf30d4c72a70a74ab7a575b)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_PSIO0\_CH5 (0x11UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 580](numaker-m46x-pinctrl_8h.md#ac079d8fa59d8e4476cf5680771dd6756)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_KPI\_COL7 (0x12UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

[ 581](numaker-m46x-pinctrl_8h.md#abb9e9d0cc27da4596558d70e3847cf0c)#define NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_BMC1 (0x14UL << NUMAKER\_SYS\_GPB\_MFP1\_PB4MFP\_Pos)

582

583/\* PB.5 MFP \*/

[ 584](numaker-m46x-pinctrl_8h.md#a2962e0f9d045774b29fdb3a280af5b77)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 585](numaker-m46x-pinctrl_8h.md#a75cab2d7638b100d756031dba040e632)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_EADC0\_CH5 (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 586](numaker-m46x-pinctrl_8h.md#aa7c00aa145918aab700042b8c0ccd966)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_ACMP1\_N (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 587](numaker-m46x-pinctrl_8h.md#a1cd542f17685810f1e14c7177a76088d)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_EBI\_ADR0 (0x02UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 588](numaker-m46x-pinctrl_8h.md#ac829acdf50debf4acc5178a45e6dbf09)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_SD0\_DAT3 (0x03UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 589](numaker-m46x-pinctrl_8h.md#a92681fe6ac04e4a5f270c1985c859a3f)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_EMAC0\_RMII\_REFCLK (0x04UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 590](numaker-m46x-pinctrl_8h.md#a8970cf459603c03a9aab9fb4e1cd7623)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_SPI1\_MISO (0x05UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 591](numaker-m46x-pinctrl_8h.md#ab4e935f8832bbb1eb39df8bddc9e8dd6)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_I2C0\_SCL (0x06UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 592](numaker-m46x-pinctrl_8h.md#a75e7c9adea26d3a4f5a56c045f1f702e)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_UART5\_TXD (0x07UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 593](numaker-m46x-pinctrl_8h.md#a4a0d113f35b6966522af816d1f344b44)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_SC0\_CLK (0x09UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 594](numaker-m46x-pinctrl_8h.md#aa16b9b8129bb379bd3adfece538fce3b)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_I2S0\_BCLK (0x0aUL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 595](numaker-m46x-pinctrl_8h.md#a9b490371a24cf3cc664324b0c3d57bc7)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_EPWM0\_CH0 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 596](numaker-m46x-pinctrl_8h.md#a38bb22474feac7e01b6f9ff5b2126b9c)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_UART2\_TXD (0x0cUL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 597](numaker-m46x-pinctrl_8h.md#ab4aaa5905f3e75470bb779b44878384a)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_TM0 (0x0eUL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 598](numaker-m46x-pinctrl_8h.md#a67efbf729c46bec344c962f4bad15f2d)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_INT0 (0x0fUL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 599](numaker-m46x-pinctrl_8h.md#a757e13367e613524f956d0bc80868d65)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_PSIO0\_CH4 (0x11UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 600](numaker-m46x-pinctrl_8h.md#a12f21beea0a9621649511d22b18ad5dd)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_KPI\_COL6 (0x12UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

[ 601](numaker-m46x-pinctrl_8h.md#a4b37aa6043da2cb063924fb224da6f0e)#define NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_BMC0 (0x14UL << NUMAKER\_SYS\_GPB\_MFP1\_PB5MFP\_Pos)

602

603/\* PB.6 MFP \*/

[ 604](numaker-m46x-pinctrl_8h.md#aee8a1b26765c965c0d0c7fca7cbef30c)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 605](numaker-m46x-pinctrl_8h.md#aaa2c46daf694dd5dab5a2b368e7a33c1)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_EADC0\_CH6 (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 606](numaker-m46x-pinctrl_8h.md#a5bb827f91155afa23769be0aabd86f40)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_EADC2\_CH14 (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 607](numaker-m46x-pinctrl_8h.md#a65609aff8606a37eb5fd5c0bfa068694)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_ACMP2\_N (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 608](numaker-m46x-pinctrl_8h.md#a18f368fa5eaf7e5430cc15d40c5e4674)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_EBI\_nWRH (0x02UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 609](numaker-m46x-pinctrl_8h.md#a8ae43b70c120b2ed24ed04d11725a2d0)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_EMAC0\_PPS (0x03UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 610](numaker-m46x-pinctrl_8h.md#a48453188c0cd70f179dc6317ae775152)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_CAN1\_RXD (0x05UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 611](numaker-m46x-pinctrl_8h.md#ad08e6442c52ce389ca149314b8400230)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_UART1\_RXD (0x06UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 612](numaker-m46x-pinctrl_8h.md#a38dfe42eb85dad31284ac2fd16765082)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_SD1\_CLK (0x07UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 613](numaker-m46x-pinctrl_8h.md#a68ddfa78b32b702949caf3cb21ca2139)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_EBI\_nCS1 (0x08UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 614](numaker-m46x-pinctrl_8h.md#aa303a0df79944d6b512e26b82551c853)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_BPWM1\_CH5 (0x0aUL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 615](numaker-m46x-pinctrl_8h.md#a41d054e58a9e33ea5f3ac3ca75376c07)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_EPWM1\_BRAKE1 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 616](numaker-m46x-pinctrl_8h.md#a5ce5f60eb4cdbbcd3e22327b936f19fe)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_EPWM1\_CH5 (0x0cUL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 617](numaker-m46x-pinctrl_8h.md#a9ed4175903ec9868ddc46d8fa8a36b07)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_INT4 (0x0dUL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 618](numaker-m46x-pinctrl_8h.md#a168b0bda05ebfd57a0c898fe15b5c064)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_USB\_VBUS\_EN (0x0eUL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 619](numaker-m46x-pinctrl_8h.md#a76dc9b99cb3a6437cdb56952712f7642)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_ACMP1\_O (0x0fUL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 620](numaker-m46x-pinctrl_8h.md#a70f5366670505e5b80fd482cfe99d5eb)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_SPI3\_MOSI (0x10UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 621](numaker-m46x-pinctrl_8h.md#a74423eabaf49ed7065bc3ed00952fea3)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_KPI\_COL5 (0x12UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 622](numaker-m46x-pinctrl_8h.md#aef036e7aad142ea9ce8c3fd3b420d99f)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_SPI1\_SS (0x13UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

[ 623](numaker-m46x-pinctrl_8h.md#a16ceebeca9d77623aa4843a4904e93b3)#define NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_BMC31 (0x14UL << NUMAKER\_SYS\_GPB\_MFP1\_PB6MFP\_Pos)

624

625/\* PB.7 MFP \*/

[ 626](numaker-m46x-pinctrl_8h.md#a422608d3288675bf9542a2fdcb7b6a06)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 627](numaker-m46x-pinctrl_8h.md#a6c83df2e44f3b8b76d96d8163af716ac)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_EADC0\_CH7 (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 628](numaker-m46x-pinctrl_8h.md#a28c232cf0e86d85378f247a4395be035)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_EADC2\_CH15 (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 629](numaker-m46x-pinctrl_8h.md#af572298a5f4a0e0428dba332e1234102)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_ACMP2\_P0 (0x01UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 630](numaker-m46x-pinctrl_8h.md#a7b6a456fa3f76420329bdc4748407071)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_EBI\_nWRL (0x02UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 631](numaker-m46x-pinctrl_8h.md#a72d2955ceacac84d1355459bc9439d1c)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_EMAC0\_RMII\_TXEN (0x03UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 632](numaker-m46x-pinctrl_8h.md#aac1d94585f4e9753f6a7228cbbdb3c25)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_CAN1\_TXD (0x05UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 633](numaker-m46x-pinctrl_8h.md#a534aef31f2065b7c90f02a24a7ace813)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_UART1\_TXD (0x06UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 634](numaker-m46x-pinctrl_8h.md#a52a4832389d046504db786542d6e588b)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_SD1\_CMD (0x07UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 635](numaker-m46x-pinctrl_8h.md#ae207848dac81c572754bca0d242923fb)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_EBI\_nCS0 (0x08UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 636](numaker-m46x-pinctrl_8h.md#a04eb0adc237bdd1dd86fae93e0ec293e)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_BPWM1\_CH4 (0x0aUL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 637](numaker-m46x-pinctrl_8h.md#af5249874ea651db8f2cb083c672735c3)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_EPWM1\_BRAKE0 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 638](numaker-m46x-pinctrl_8h.md#af27f8d9feda60674c0fc3c274d4870fe)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_EPWM1\_CH4 (0x0cUL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 639](numaker-m46x-pinctrl_8h.md#ae19400c4917ddf03e779d634aacf99a3)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_INT5 (0x0dUL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 640](numaker-m46x-pinctrl_8h.md#a733314d38480c6a3a7ac18c3f9c40b9b)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_USB\_VBUS\_ST (0x0eUL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 641](numaker-m46x-pinctrl_8h.md#a1d42059c1ce20549ccf2c5353bb14bcb)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_ACMP0\_O (0x0fUL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 642](numaker-m46x-pinctrl_8h.md#aa6e64fa53de20b3ebbf6f8818a52d503)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_SPI3\_MISO (0x10UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 643](numaker-m46x-pinctrl_8h.md#a86d8f252542514d1ca5efcb8ab4e82e5)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_KPI\_COL4 (0x12UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 644](numaker-m46x-pinctrl_8h.md#ac1c06a4557ee3f1fc138698e63edf47b)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_SPI1\_CLK (0x13UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

[ 645](numaker-m46x-pinctrl_8h.md#a6a83ca806b2468367aa7772f690b7142)#define NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_BMC30 (0x14UL << NUMAKER\_SYS\_GPB\_MFP1\_PB7MFP\_Pos)

646

647/\* PB.8 MFP \*/

[ 648](numaker-m46x-pinctrl_8h.md#ae502103ada064e866740c48d785b319d)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 649](numaker-m46x-pinctrl_8h.md#aeca8ae3a90f09965db85467520d85f11)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_EADC0\_CH8 (0x01UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 650](numaker-m46x-pinctrl_8h.md#adf2419739ab3005ccb7ab93837da957e)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_ACMP2\_P1 (0x01UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 651](numaker-m46x-pinctrl_8h.md#a9d04e0b4a984041100fd0584c21ba3a4)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_EBI\_ADR19 (0x02UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 652](numaker-m46x-pinctrl_8h.md#a2612553099a8cc2b7c31748eea970635)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_EMAC0\_RMII\_TXD1 (0x03UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 653](numaker-m46x-pinctrl_8h.md#a3e3ba37843f0e5412d778a6dfdcaf59e)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_UART0\_RXD (0x05UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 654](numaker-m46x-pinctrl_8h.md#a6effabc011aabc9a17292d59a64094ef)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_UART1\_nRTS (0x06UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 655](numaker-m46x-pinctrl_8h.md#acf91e67b4f873993b7b946b929ef52ba)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_I2C1\_SMBSUS (0x07UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 656](numaker-m46x-pinctrl_8h.md#a7ce5752acaef586e89252d43847f43da)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_UART7\_RXD (0x08UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 657](numaker-m46x-pinctrl_8h.md#afb18c04b0e70eba72c0f8ef1914388bc)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_I2C0\_SDA (0x09UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 658](numaker-m46x-pinctrl_8h.md#a8c0a13f3d7556c0c3e039cf9ea97e5aa)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_BPWM1\_CH3 (0x0aUL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 659](numaker-m46x-pinctrl_8h.md#a93ee9e01564007e069a88846dc9f7e81)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_SPI3\_MOSI (0x0bUL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 660](numaker-m46x-pinctrl_8h.md#a303523df897f988f78ddcb0c2cfcfcb5)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_CAN2\_RXD (0x0cUL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 661](numaker-m46x-pinctrl_8h.md#a1abd0c1670116b41358e8dc68955cceb)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_INT6 (0x0dUL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 662](numaker-m46x-pinctrl_8h.md#a5a781fafe5d2f409db5b5975d9049ad4)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_EADC2\_ST (0x0eUL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

[ 663](numaker-m46x-pinctrl_8h.md#a18a302d0b8c232b663150c91853d118e)#define NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_BMC23 (0x14UL << NUMAKER\_SYS\_GPB\_MFP2\_PB8MFP\_Pos)

664

665/\* PB.9 MFP \*/

[ 666](numaker-m46x-pinctrl_8h.md#a23e2d84c31dfbc0c281a7138e52774ec)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 667](numaker-m46x-pinctrl_8h.md#ac5caa8adafb865ad6a5534c0667a4ad1)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_EADC0\_CH9 (0x01UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 668](numaker-m46x-pinctrl_8h.md#ad9edfeaab1f4b0add27d381ecf4e774c)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_ACMP2\_P2 (0x01UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 669](numaker-m46x-pinctrl_8h.md#ab14beda9de48e43c43d28549e178d61c)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_EBI\_ADR18 (0x02UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 670](numaker-m46x-pinctrl_8h.md#af5a9f22badb1101af60ec2dec40cbf49)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_EMAC0\_RMII\_TXD0 (0x03UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 671](numaker-m46x-pinctrl_8h.md#a665e9edaacb517048b42789c5ab7472c)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_UART0\_TXD (0x05UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 672](numaker-m46x-pinctrl_8h.md#acc750f7833ed2a602edd375069365900)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_UART1\_nCTS (0x06UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 673](numaker-m46x-pinctrl_8h.md#a03f36be31429b2ab60aae1e71c085673)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_I2C1\_SMBAL (0x07UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 674](numaker-m46x-pinctrl_8h.md#ae8775eb91252eec349b760ca671339eb)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_UART7\_TXD (0x08UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 675](numaker-m46x-pinctrl_8h.md#aac9ebbd58bde4ca8866950bc847ef59c)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_I2C0\_SCL (0x09UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 676](numaker-m46x-pinctrl_8h.md#ad008c5e06f60638ad8c19a401af35512)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_BPWM1\_CH2 (0x0aUL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 677](numaker-m46x-pinctrl_8h.md#ad803ed6a427559e9d4cc1e15626442d9)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_SPI3\_MISO (0x0bUL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 678](numaker-m46x-pinctrl_8h.md#ae84875cd21cd9088b9f227781341d4df)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_CAN2\_TXD (0x0cUL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 679](numaker-m46x-pinctrl_8h.md#abfcf0f895114b4ff32b48f017f08fb14)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_INT7 (0x0dUL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 680](numaker-m46x-pinctrl_8h.md#ae7d8bb361164ff7b790ee6dc03b8098b)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_CCAP\_HSYNC (0x0eUL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

[ 681](numaker-m46x-pinctrl_8h.md#a45efeb49a7c53c3190bb90f980e5a515)#define NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_BMC22 (0x14UL << NUMAKER\_SYS\_GPB\_MFP2\_PB9MFP\_Pos)

682

683/\* PB.10 MFP \*/

[ 684](numaker-m46x-pinctrl_8h.md#af158ce5aad92ba19f45bb9ec02552b9a)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 685](numaker-m46x-pinctrl_8h.md#a94eea4133e1e2593fe33d475359f45fb)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_EADC0\_CH10 (0x01UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 686](numaker-m46x-pinctrl_8h.md#a49276126a6cbba2406998f950293e395)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_ACMP2\_P3 (0x01UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 687](numaker-m46x-pinctrl_8h.md#ac6b5283859b5cc6b81badf3d53732ff0)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_EBI\_ADR17 (0x02UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 688](numaker-m46x-pinctrl_8h.md#a8f68856104b38f7e8ea5c0db4bd91185)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_EMAC0\_RMII\_MDIO (0x03UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 689](numaker-m46x-pinctrl_8h.md#a8c1c1f2ddaacea045c0f444397056078)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_UART0\_nRTS (0x05UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 690](numaker-m46x-pinctrl_8h.md#a431d99d057f69e712647a7f25743fb29)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_UART4\_RXD (0x06UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 691](numaker-m46x-pinctrl_8h.md#a1ae8a658c657e66ecb3325f37ebbe9bd)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_I2C1\_SDA (0x07UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 692](numaker-m46x-pinctrl_8h.md#a406dfcde42b75763cd8c82393176c51a)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_CAN0\_RXD (0x08UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 693](numaker-m46x-pinctrl_8h.md#a08790c7154ee3f06770f98f2cbb1d8f1)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_BPWM1\_CH1 (0x0aUL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 694](numaker-m46x-pinctrl_8h.md#a29f5c136418f7037f8cf5c2edb937fd2)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_SPI3\_SS (0x0bUL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 695](numaker-m46x-pinctrl_8h.md#a6b2ca36758c12e53b42a22fdba44af76)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_CCAP\_VSYNC (0x0cUL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 696](numaker-m46x-pinctrl_8h.md#a1c9ad6b014541c7b54423f77b233b405)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_HSUSB\_VBUS\_EN (0x0eUL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

[ 697](numaker-m46x-pinctrl_8h.md#a26cde0bf3061eae8055b706ffecf56e3)#define NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_BMC21 (0x14UL << NUMAKER\_SYS\_GPB\_MFP2\_PB10MFP\_Pos)

698

699/\* PB.11 MFP \*/

[ 700](numaker-m46x-pinctrl_8h.md#a7830e27a7814de86b8a09edb58d1aace)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 701](numaker-m46x-pinctrl_8h.md#a4916f6f9168ee9c4deb8545e62b9081b)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_EADC0\_CH11 (0x01UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 702](numaker-m46x-pinctrl_8h.md#abb65a461c074fe1d1b9483fdb3147ebd)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_EBI\_ADR16 (0x02UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 703](numaker-m46x-pinctrl_8h.md#a968f091440a7ad9ec8b1073e037be750)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_EMAC0\_RMII\_MDC (0x03UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 704](numaker-m46x-pinctrl_8h.md#af4e4e1761f0fbace7ebf5766316c4b4c)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_UART0\_nCTS (0x05UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 705](numaker-m46x-pinctrl_8h.md#a56827b9a7b91f1f7ef202da48ad9a131)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_UART4\_TXD (0x06UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 706](numaker-m46x-pinctrl_8h.md#aa0b13d03cd243438edf8a3849e432dff)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_I2C1\_SCL (0x07UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 707](numaker-m46x-pinctrl_8h.md#a15e2205708682a0698fdc0dd963cc0a0)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_CAN0\_TXD (0x08UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 708](numaker-m46x-pinctrl_8h.md#a7e832df0314f3da703f65ce23cd8cfa8)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_SPI0\_I2SMCLK (0x09UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 709](numaker-m46x-pinctrl_8h.md#aea9c8161a8d9e12a825768099e181796)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_BPWM1\_CH0 (0x0aUL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 710](numaker-m46x-pinctrl_8h.md#af67bb06e16a45fef38e8398cf68af7ec)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_SPI3\_CLK (0x0bUL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 711](numaker-m46x-pinctrl_8h.md#a91b648d48ecaefd7df30d6b7e210feba)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_CCAP\_SFIELD (0x0cUL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 712](numaker-m46x-pinctrl_8h.md#a05e93917a97778940fcfebc6e996d44b)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_HSUSB\_VBUS\_ST (0x0eUL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

[ 713](numaker-m46x-pinctrl_8h.md#a3c35db1660c0d845010aee3c6b2b4118)#define NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_BMC20 (0x14UL << NUMAKER\_SYS\_GPB\_MFP2\_PB11MFP\_Pos)

714

715/\* PB.12 MFP \*/

[ 716](numaker-m46x-pinctrl_8h.md#a46b829273b11790ebc9ef23f609484bc)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 717](numaker-m46x-pinctrl_8h.md#a0bf994e55c2257f510e6287248bf6c80)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_EADC0\_CH12 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 718](numaker-m46x-pinctrl_8h.md#a4488d08e0cd3df546b26cef54dd28650)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_EADC1\_CH12 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 719](numaker-m46x-pinctrl_8h.md#a489bc163fd493a7daee13b05d26e04c1)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_DAC0\_OUT (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 720](numaker-m46x-pinctrl_8h.md#add08a2bb8a5a73984a7466e44fc717f6)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_ACMP0\_P2 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 721](numaker-m46x-pinctrl_8h.md#a731e369519397ef3468b9e27177d5423)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_ACMP1\_P2 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 722](numaker-m46x-pinctrl_8h.md#a1c64b92f48655977a5ed17fc7677216f)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_EBI\_AD15 (0x02UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 723](numaker-m46x-pinctrl_8h.md#a229398008c6c6c39f684eeec5e76abc7)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_SC1\_CLK (0x03UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 724](numaker-m46x-pinctrl_8h.md#a30907743e6556762ba41888d71a9d5f6)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_SPI0\_MOSI (0x04UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 725](numaker-m46x-pinctrl_8h.md#a0b2b36bb193124b2bee5fff140dba768)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_USCI0\_CLK (0x05UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 726](numaker-m46x-pinctrl_8h.md#afc38245a8a62fb0ac1ca601085dcb8be)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_UART0\_RXD (0x06UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 727](numaker-m46x-pinctrl_8h.md#a8457a1646431b806dd2d33b6cb402497)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_UART3\_nCTS (0x07UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 728](numaker-m46x-pinctrl_8h.md#ab1638b9acdee11ce39fb050d29e36162)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_I2C2\_SDA (0x08UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 729](numaker-m46x-pinctrl_8h.md#a0474ebf1de2efd07aaf3b31bb107324f)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_SD0\_nCD (0x09UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 730](numaker-m46x-pinctrl_8h.md#a370c7efdc27b70148e369cdce7f5bb77)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_CCAP\_SCLK (0x0aUL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 731](numaker-m46x-pinctrl_8h.md#ad12e2e22d700f6e3a1f282c62284495b)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_EPWM1\_CH3 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 732](numaker-m46x-pinctrl_8h.md#a15f9b0c78010cce2686a5f9fdd360642)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_ETMC\_TRACE\_DATA3 (0x0cUL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 733](numaker-m46x-pinctrl_8h.md#a56bad338ee4c7f96303061c054982678)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_TM3\_EXT (0x0dUL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 734](numaker-m46x-pinctrl_8h.md#a0875a2c0f457f443a3bcc5259bab40d4)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_CAN3\_RXD (0x0eUL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 735](numaker-m46x-pinctrl_8h.md#ac1d061db0f172fe2a13b8ba65ee202f9)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_SPI3\_SS (0x10UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 736](numaker-m46x-pinctrl_8h.md#aeff25bc4a02d8dc06e0e0a3beee8fe9e)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_PSIO0\_CH3 (0x11UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 737](numaker-m46x-pinctrl_8h.md#a6f1c50d470fbc89c59472c78c9271fb8)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_KPI\_COL3 (0x12UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

[ 738](numaker-m46x-pinctrl_8h.md#a839ebf26efc85eb4a6dba949fad95d52)#define NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_BMC29 (0x14UL << NUMAKER\_SYS\_GPB\_MFP3\_PB12MFP\_Pos)

739

740/\* PB.13 MFP \*/

[ 741](numaker-m46x-pinctrl_8h.md#a6d5ad5bd8f83f794dc262dbdeacba74a)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 742](numaker-m46x-pinctrl_8h.md#ad744c19fef08bce3a29dffb02a221351)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_EADC0\_CH13 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 743](numaker-m46x-pinctrl_8h.md#a6bc743669ed0459698f1f63bf5b21739)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_EADC1\_CH13 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 744](numaker-m46x-pinctrl_8h.md#a1395d316afe809adeb8801d032ab6eff)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_DAC1\_OUT (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 745](numaker-m46x-pinctrl_8h.md#ac07e784c447c5cffbdd909d265de4bb4)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_ACMP0\_P3 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 746](numaker-m46x-pinctrl_8h.md#a2e5f8c847fb573009218050d74e78b9a)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_ACMP1\_P3 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 747](numaker-m46x-pinctrl_8h.md#a37fe411e52cd90848f330ce469b0b722)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_EBI\_AD14 (0x02UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 748](numaker-m46x-pinctrl_8h.md#a0c3d7d0b93cab8b90ec941218181acb2)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_SC1\_DAT (0x03UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 749](numaker-m46x-pinctrl_8h.md#a634b5bdbf7e7371800db51989bb70b12)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_SPI0\_MISO (0x04UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 750](numaker-m46x-pinctrl_8h.md#ae82524f1e945ac4f5768450ef96c26af)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_USCI0\_DAT0 (0x05UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 751](numaker-m46x-pinctrl_8h.md#aa9fe55ddab22e7f5b9456e5e52dc5f67)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_UART0\_TXD (0x06UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 752](numaker-m46x-pinctrl_8h.md#ac32616aec5a37e6921528611fd1daef2)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_UART3\_nRTS (0x07UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 753](numaker-m46x-pinctrl_8h.md#a9bfbdf98e06c813068345b89905d5fca)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_I2C2\_SCL (0x08UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 754](numaker-m46x-pinctrl_8h.md#a1bf0901c6ba01d9d131050ee6cafff1b)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_CCAP\_PIXCLK (0x0aUL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 755](numaker-m46x-pinctrl_8h.md#a6db90e568496043befc8f0b8bc7e9df9)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_EPWM1\_CH2 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 756](numaker-m46x-pinctrl_8h.md#aefa258444c83d2aab315e2c01a055805)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_ETMC\_TRACE\_DATA2 (0x0cUL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 757](numaker-m46x-pinctrl_8h.md#a4d9d059ecda14b35fa2b169a30646da3)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_TM2\_EXT (0x0dUL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 758](numaker-m46x-pinctrl_8h.md#a38dabc651ed9f7655e58137f905c6d83)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_CAN3\_TXD (0x0eUL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 759](numaker-m46x-pinctrl_8h.md#acf5c1ad71e9bba2ac2be8924a4cc1a89)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_SPI3\_CLK (0x10UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 760](numaker-m46x-pinctrl_8h.md#a990bc6e324ea2eb32d28a841d10775d3)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_PSIO0\_CH2 (0x11UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 761](numaker-m46x-pinctrl_8h.md#ac43b88b0a006aa84a7df480eb7682283)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_KPI\_COL2 (0x12UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 762](numaker-m46x-pinctrl_8h.md#ac23cdffd8fdc4840a244f686aa89494a)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_SPI9\_MISO (0x13UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

[ 763](numaker-m46x-pinctrl_8h.md#a4e1f3fa76716fc465ef989fc45e6afaf)#define NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_BMC28 (0x14UL << NUMAKER\_SYS\_GPB\_MFP3\_PB13MFP\_Pos)

764

765/\* PB.14 MFP \*/

[ 766](numaker-m46x-pinctrl_8h.md#abe9298e8a4c6dba6cba97ad486a4706e)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 767](numaker-m46x-pinctrl_8h.md#a435a473cec5ab62152e3664e61c51d45)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_EADC0\_CH14 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 768](numaker-m46x-pinctrl_8h.md#a3232c2ae5f019dd5fab0de6326ac8b3d)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_EADC1\_CH14 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 769](numaker-m46x-pinctrl_8h.md#aea3ffec5b3e4945f6e36a2b49de794e4)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_EBI\_AD13 (0x02UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 770](numaker-m46x-pinctrl_8h.md#a49297d952bfc1b7457e14dfdb8205a95)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_SC1\_RST (0x03UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 771](numaker-m46x-pinctrl_8h.md#a751929cf1278d0d2142cc3aaafde8168)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_SPI0\_CLK (0x04UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 772](numaker-m46x-pinctrl_8h.md#abcf1d6bf16a597b90e3fe3fd0bd23c1e)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_USCI0\_DAT1 (0x05UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 773](numaker-m46x-pinctrl_8h.md#adb0c6166e618ed7bf3878e025ec243c3)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_UART0\_nRTS (0x06UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 774](numaker-m46x-pinctrl_8h.md#a8e7d908919795e8465de671363c3303e)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_UART3\_RXD (0x07UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 775](numaker-m46x-pinctrl_8h.md#ab4cc935e7eb4f391ae7bb633979f7ed9)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_I2C2\_SMBSUS (0x08UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 776](numaker-m46x-pinctrl_8h.md#a95e693e8e89e0e00914d600213518739)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_CCAP\_DATA0 (0x09UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 777](numaker-m46x-pinctrl_8h.md#a19519246820b80d7a7ade29997720566)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_EPWM1\_CH1 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 778](numaker-m46x-pinctrl_8h.md#a0a555d51318766f8b8f91706eb864c01)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_ETMC\_TRACE\_DATA1 (0x0cUL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 779](numaker-m46x-pinctrl_8h.md#ad2759b03751a6d2242b949f342c7aa5d)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_TM1\_EXT (0x0dUL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 780](numaker-m46x-pinctrl_8h.md#acdbaa3f64bbef36e142903743165a52a)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_CLKO (0x0eUL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 781](numaker-m46x-pinctrl_8h.md#aaa0185df1096a130881e8c8a1abe4817)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_USB\_VBUS\_ST (0x0fUL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 782](numaker-m46x-pinctrl_8h.md#a6afe90de016438313a1599c7eb39fe65)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_PSIO0\_CH1 (0x11UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 783](numaker-m46x-pinctrl_8h.md#a2e6407fa2db138f0703b178114dc0ed0)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_KPI\_COL1 (0x12UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

[ 784](numaker-m46x-pinctrl_8h.md#a1de142ef4095b9a3182947c65cee701f)#define NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_SPI9\_SS (0x13UL << NUMAKER\_SYS\_GPB\_MFP3\_PB14MFP\_Pos)

785

786/\* PB.15 MFP \*/

[ 787](numaker-m46x-pinctrl_8h.md#aefaa7ae15b6b7a8247836bec48fdfcd9)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 788](numaker-m46x-pinctrl_8h.md#aadb90ebc6f3e6fc6d95f2969eeadefd5)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_EADC0\_CH15 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 789](numaker-m46x-pinctrl_8h.md#a0f257cd6008c5ec7db215183d640bfd4)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_EADC1\_CH15 (0x01UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 790](numaker-m46x-pinctrl_8h.md#a548be68ea7f1de026f8097a2ecd25f59)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_EBI\_AD12 (0x02UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 791](numaker-m46x-pinctrl_8h.md#a002a388d5b8fb913e1f6373f3230f19c)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_SC1\_PWR (0x03UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 792](numaker-m46x-pinctrl_8h.md#aa139287235f480ea0908cfc08b83ced8)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_SPI0\_SS (0x04UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 793](numaker-m46x-pinctrl_8h.md#a7360ece749a7f07e177d229d4bec8671)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_USCI0\_CTL1 (0x05UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 794](numaker-m46x-pinctrl_8h.md#a44acec993040d5abff4731693f15837b)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_UART0\_nCTS (0x06UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 795](numaker-m46x-pinctrl_8h.md#a8055567e869c0f6402ffa0161b8e4f2a)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_UART3\_TXD (0x07UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 796](numaker-m46x-pinctrl_8h.md#a311be9b7a6d8c5040387fb900996da6b)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_I2C2\_SMBAL (0x08UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 797](numaker-m46x-pinctrl_8h.md#aef84a25c2b89558d78d0baa52f154c8e)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_CCAP\_DATA1 (0x09UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 798](numaker-m46x-pinctrl_8h.md#a609205d6660bf7f934cdc8c84a91d525)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_EPWM0\_BRAKE1 (0x0aUL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 799](numaker-m46x-pinctrl_8h.md#a1a0ab295fa400266a0983a113bc7d968)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_EPWM1\_CH0 (0x0bUL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 800](numaker-m46x-pinctrl_8h.md#a84f807b139277ebb764e72ada175e444)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_ETMC\_TRACE\_DATA0 (0x0cUL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 801](numaker-m46x-pinctrl_8h.md#ad178adb847dd905cd7cb1ffa499f712b)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_TM0\_EXT (0x0dUL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 802](numaker-m46x-pinctrl_8h.md#a1f6aa592862bf3d0f758830dfe810cdf)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_USB\_VBUS\_EN (0x0eUL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 803](numaker-m46x-pinctrl_8h.md#aa11ec1bc451e65956de805a97fd3125e)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_HSUSB\_VBUS\_EN (0x0fUL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 804](numaker-m46x-pinctrl_8h.md#a563107189da7f8a3bbde735b13fe478c)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_PSIO0\_CH0 (0x11UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 805](numaker-m46x-pinctrl_8h.md#a9a44f6223fd97766cf08b8f6a074ae2b)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_KPI\_COL0 (0x12UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 806](numaker-m46x-pinctrl_8h.md#a31fdd01b766f1b68001668b1bd1f1d61)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_SPI9\_CLK (0x13UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

[ 807](numaker-m46x-pinctrl_8h.md#a45593f1518a0d452858e78e65b494da2)#define NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_BMC27 (0x14UL << NUMAKER\_SYS\_GPB\_MFP3\_PB15MFP\_Pos)

808

809/\* PC.0 MFP \*/

[ 810](numaker-m46x-pinctrl_8h.md#a99e03831f307c8c35fa8c62276758ba4)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 811](numaker-m46x-pinctrl_8h.md#afc58b38b6ca30c3a704916494448ab78)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_EBI\_AD0 (0x02UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 812](numaker-m46x-pinctrl_8h.md#a7c83a743e7810262d18d7eb0e842da64)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_SPIM\_MOSI (0x03UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 813](numaker-m46x-pinctrl_8h.md#aa3c7007d8477247e98c7ff630a2fa447)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_QSPI0\_MOSI0 (0x04UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 814](numaker-m46x-pinctrl_8h.md#ae0f76b3566ee979d28199fd6c901ec20)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_SC1\_CLK (0x05UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 815](numaker-m46x-pinctrl_8h.md#ad46f24b50ffbbfb83a7a561491fccc57)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_I2S0\_LRCK (0x06UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 816](numaker-m46x-pinctrl_8h.md#a7b6645095ee046aae66577f1a681004b)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_SPI1\_SS (0x07UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 817](numaker-m46x-pinctrl_8h.md#a48a7ff0a6b7b9a17f0e41f29706ec948)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_UART2\_RXD (0x08UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 818](numaker-m46x-pinctrl_8h.md#afff3e6700fd562e966ea366daadf338c)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_I2C0\_SDA (0x09UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 819](numaker-m46x-pinctrl_8h.md#a0382efc579b6e1045ec4b26d6e7ee907)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_CAN2\_RXD (0x0aUL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 820](numaker-m46x-pinctrl_8h.md#a33a72f533c57143aac9a44cadb2520e5)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_EPWM1\_CH5 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 821](numaker-m46x-pinctrl_8h.md#ab4de5b7f18ee3a78ac1e2bcbf8ec1680)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_CCAP\_DATA0 (0x0dUL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 822](numaker-m46x-pinctrl_8h.md#a432fe015e2f26d0a33863113ea4e7a70)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_ACMP1\_O (0x0eUL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 823](numaker-m46x-pinctrl_8h.md#a8bd5cd96a65f645663848435decfcb61)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_EADC1\_ST (0x0fUL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 824](numaker-m46x-pinctrl_8h.md#a37f7ad465be64e8e846c04df9cf8bdd2)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_HBI\_D2 (0x10UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 825](numaker-m46x-pinctrl_8h.md#a7adc43f7bbffa81fadc6f455f0a04f5d)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_QSPI1\_CLK (0x11UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 826](numaker-m46x-pinctrl_8h.md#a1905a670478d579be3bd28c6318cc774)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_KPI\_ROW5 (0x12UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 827](numaker-m46x-pinctrl_8h.md#a9466a251814256b169692113e4f7d28f)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_SPI7\_MOSI (0x13UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

[ 828](numaker-m46x-pinctrl_8h.md#aa6850a0373220bdcd3606791d5f9df96)#define NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_BMC25 (0x14UL << NUMAKER\_SYS\_GPC\_MFP0\_PC0MFP\_Pos)

829

830/\* PC.1 MFP \*/

[ 831](numaker-m46x-pinctrl_8h.md#a7bfb5e10df557d0af2212e59e1e7dbd4)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 832](numaker-m46x-pinctrl_8h.md#a1af184c877910fae471fbdf5aaeb7356)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_EBI\_AD1 (0x02UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 833](numaker-m46x-pinctrl_8h.md#acaaf5baec7fd7a7892ddb89e5d2b2c6d)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_SPIM\_MISO (0x03UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 834](numaker-m46x-pinctrl_8h.md#a054ae7cf97be34014524a57130bd91a2)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_QSPI0\_MISO0 (0x04UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 835](numaker-m46x-pinctrl_8h.md#ab6dfa0d2ea3838c8aa3086ac6b5057f4)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_SC1\_DAT (0x05UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 836](numaker-m46x-pinctrl_8h.md#a17941ee4c14619681b82796685153196)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_I2S0\_DO (0x06UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 837](numaker-m46x-pinctrl_8h.md#aa9861e86cf0a11ada457b3768ec93948)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_SPI1\_CLK (0x07UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 838](numaker-m46x-pinctrl_8h.md#add777046ba9e5b4f2daa2f4bbeaa8289)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_UART2\_TXD (0x08UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 839](numaker-m46x-pinctrl_8h.md#a4a458d4fca1354cf73c4513bbb4e5ce8)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_I2C0\_SCL (0x09UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 840](numaker-m46x-pinctrl_8h.md#a785c3c22301348e567e997240b193231)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_CAN2\_TXD (0x0aUL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 841](numaker-m46x-pinctrl_8h.md#a0ea832545e16a496c007f5ba3ca1e3fd)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_EPWM1\_CH4 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 842](numaker-m46x-pinctrl_8h.md#a2689a7f12cc224835932c34771f50937)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_CCAP\_DATA1 (0x0dUL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 843](numaker-m46x-pinctrl_8h.md#a2272be22b69a96ab38f44096ef267416)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_ACMP0\_O (0x0eUL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 844](numaker-m46x-pinctrl_8h.md#a39b58346d29e2db7db7ad13ebf92aaf2)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_EADC0\_ST (0x0fUL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 845](numaker-m46x-pinctrl_8h.md#a4b6a35beb29e7ac213d69b5cd64aa7c3)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_HBI\_RWDS (0x10UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 846](numaker-m46x-pinctrl_8h.md#a1ded0576e57bfaf795514e93be8aac76)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_QSPI1\_SS (0x11UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 847](numaker-m46x-pinctrl_8h.md#a26bf2b77fc96fe35bffb5a0a5326ab61)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_KPI\_ROW4 (0x12UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 848](numaker-m46x-pinctrl_8h.md#a37da741d1b0e74a56ac0f4b33fbd19a8)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_SPI7\_MISO (0x13UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

[ 849](numaker-m46x-pinctrl_8h.md#a39b928547bfc65abe932c3653e46e9a0)#define NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_BMC24 (0x14UL << NUMAKER\_SYS\_GPC\_MFP0\_PC1MFP\_Pos)

850

851/\* PC.2 MFP \*/

[ 852](numaker-m46x-pinctrl_8h.md#a16744a425cfa820338b6a97ad4cf4b38)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 853](numaker-m46x-pinctrl_8h.md#ab5b23c738e21ed568ee7749aa4e97492)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_EBI\_AD2 (0x02UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 854](numaker-m46x-pinctrl_8h.md#a9c804b48e4c8e5bd1223cc3d6c6cbe99)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_SPIM\_CLK (0x03UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 855](numaker-m46x-pinctrl_8h.md#abae1403fbe8429c16811ee7ca4391237)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_QSPI0\_CLK (0x04UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 856](numaker-m46x-pinctrl_8h.md#a008baa58a34832d8b49a5472f419b786)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_SC1\_RST (0x05UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 857](numaker-m46x-pinctrl_8h.md#aa98b906ac7aabf927a00e9d2927bc83c)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_I2S0\_DI (0x06UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 858](numaker-m46x-pinctrl_8h.md#ae757213c5dbba0bc8c22318d8b86cfbd)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_SPI1\_MOSI (0x07UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 859](numaker-m46x-pinctrl_8h.md#a7b9e1c7441dcd20c2083126a8862e655)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_UART2\_nCTS (0x08UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 860](numaker-m46x-pinctrl_8h.md#a9f8f9023421e65c13e7fece30e1d70f3)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_I2C0\_SMBSUS (0x09UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 861](numaker-m46x-pinctrl_8h.md#a406a7a088b56c418ee6b6167477af0c0)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_CAN1\_RXD (0x0aUL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 862](numaker-m46x-pinctrl_8h.md#af5fa0942882ec4d8603a630b9c34844a)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_UART3\_RXD (0x0bUL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 863](numaker-m46x-pinctrl_8h.md#a7535084e7ff7afbdf0660803e21dd20f)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_EPWM1\_CH3 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 864](numaker-m46x-pinctrl_8h.md#ac7b7e979ee6b3dcf32d1d9cc1a9c04bd)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_CCAP\_DATA2 (0x0dUL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 865](numaker-m46x-pinctrl_8h.md#a72e5940d4a3bbc727888a3932f003f37)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_QSPI1\_MOSI0 (0x0eUL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 866](numaker-m46x-pinctrl_8h.md#a3e3911ed3f89d3d472eee0dc8182fc77)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_I2C3\_SDA (0x0fUL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 867](numaker-m46x-pinctrl_8h.md#a6a59c02e2f3fe57452af4934f68778c4)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_HBI\_nRESET (0x10UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 868](numaker-m46x-pinctrl_8h.md#aac66342b6b5202f76dcba8c0a73d5da8)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_PSIO0\_CH3 (0x11UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 869](numaker-m46x-pinctrl_8h.md#a9b3bb2d07b233e35520dc89bae21ccf4)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_KPI\_ROW3 (0x12UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 870](numaker-m46x-pinctrl_8h.md#afc9122dfb6598976b3b274cb0f3cd1a3)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_SPI7\_CLK (0x13UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

[ 871](numaker-m46x-pinctrl_8h.md#a84871b14355d30b61d548f783de66558)#define NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_BMC23 (0x14UL << NUMAKER\_SYS\_GPC\_MFP0\_PC2MFP\_Pos)

872

873/\* PC.3 MFP \*/

[ 874](numaker-m46x-pinctrl_8h.md#ab66915b771d1ee58986feed97a2502fb)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 875](numaker-m46x-pinctrl_8h.md#ac65765c2c1283e6ea621eea32708c3e5)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_EBI\_AD3 (0x02UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 876](numaker-m46x-pinctrl_8h.md#a6cf5f210c0845b362328432c16a7fd15)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_SPIM\_SS (0x03UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 877](numaker-m46x-pinctrl_8h.md#ababa0a0ca6a5b1cf511608901b1e2ddd)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_QSPI0\_SS (0x04UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 878](numaker-m46x-pinctrl_8h.md#a49dbe222a9795c304b4ddb8abe6584a2)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_SC1\_PWR (0x05UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 879](numaker-m46x-pinctrl_8h.md#ad648fe6a98c5e53c2089604a0fc0ebfa)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_I2S0\_MCLK (0x06UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 880](numaker-m46x-pinctrl_8h.md#a895ad7ab43bf543d30713acc7acd265b)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_SPI1\_MISO (0x07UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 881](numaker-m46x-pinctrl_8h.md#a73258c7afae4034e523b28686d9583c0)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_UART2\_nRTS (0x08UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 882](numaker-m46x-pinctrl_8h.md#a091eb9b78a929194e16f08dc8fbde1d7)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_I2C0\_SMBAL (0x09UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 883](numaker-m46x-pinctrl_8h.md#a15c1c944551d99fb9db56766740988ed)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_CAN1\_TXD (0x0aUL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 884](numaker-m46x-pinctrl_8h.md#abbd90a3ded952093b9247a207c4e8f8b)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_UART3\_TXD (0x0bUL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 885](numaker-m46x-pinctrl_8h.md#ac330575927757a0ee865d21b03c23f3d)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_EPWM1\_CH2 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 886](numaker-m46x-pinctrl_8h.md#adce49f329dfaea3bd2bfd87bb90ae9b3)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_CCAP\_DATA3 (0x0dUL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 887](numaker-m46x-pinctrl_8h.md#a923d54f8c4b0f8080e647de5adaafd43)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_QSPI1\_MISO0 (0x0eUL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 888](numaker-m46x-pinctrl_8h.md#aa1e3f5467bbe51d1255d20cf8dd1d2c2)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_I2C3\_SCL (0x0fUL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 889](numaker-m46x-pinctrl_8h.md#a62319cda1e52949d8db12a2e311d7757)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_HBI\_nCS (0x10UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 890](numaker-m46x-pinctrl_8h.md#ab03c1fba7aa6bccdf663a0805308f2c4)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_PSIO0\_CH2 (0x11UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 891](numaker-m46x-pinctrl_8h.md#a42927aab3bc77d736f4b36c73cc34432)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_KPI\_ROW2 (0x12UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 892](numaker-m46x-pinctrl_8h.md#afcbf0c23fae0097544d64bf3fcbb7815)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_SPI7\_SS (0x13UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

[ 893](numaker-m46x-pinctrl_8h.md#a0fd44c4574206dfcf1f363b44268f329)#define NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_BMC22 (0x14UL << NUMAKER\_SYS\_GPC\_MFP0\_PC3MFP\_Pos)

894

895/\* PC.4 MFP \*/

[ 896](numaker-m46x-pinctrl_8h.md#a71d5de65cd71ae83c4c1397591da7692)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 897](numaker-m46x-pinctrl_8h.md#ab00c73524513c400cf28df5082dae21f)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_EBI\_AD4 (0x02UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 898](numaker-m46x-pinctrl_8h.md#adf6ad391e54402582e9861a2d7962187)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_SPIM\_D3 (0x03UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 899](numaker-m46x-pinctrl_8h.md#acb1fbb96f4f5906148560d5cc3398e44)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_QSPI0\_MOSI1 (0x04UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 900](numaker-m46x-pinctrl_8h.md#a116de9679251eaa2d427aaa50a4e06a9)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_SC1\_nCD (0x05UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 901](numaker-m46x-pinctrl_8h.md#abc472053b0ebdfacb00e98730368aa3d)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_I2S0\_BCLK (0x06UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 902](numaker-m46x-pinctrl_8h.md#a899fdd0d7d1494d9e7b3e5b7337670b4)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_SPI1\_I2SMCLK (0x07UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 903](numaker-m46x-pinctrl_8h.md#a4fb33cdba12e61f7841efda2913e785c)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_UART2\_RXD (0x08UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 904](numaker-m46x-pinctrl_8h.md#a4fa063662dc2c99f650595b984ea033c)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_I2C1\_SDA (0x09UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 905](numaker-m46x-pinctrl_8h.md#a46e783127f3885e8c25bb3540af5ebf5)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_CAN0\_RXD (0x0aUL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 906](numaker-m46x-pinctrl_8h.md#a0eb4978c4cc001da3c68db1e9572de3e)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_UART4\_RXD (0x0bUL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 907](numaker-m46x-pinctrl_8h.md#acad0f619876a237c6f78ced366792df7)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_EPWM1\_CH1 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 908](numaker-m46x-pinctrl_8h.md#a328ffb3a2e4f4ff0b0e2b49d1410c6a8)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_CCAP\_DATA4 (0x0dUL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 909](numaker-m46x-pinctrl_8h.md#a97a302ab607dad5fe4d704b8f7e76f15)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_QSPI1\_CLK (0x0eUL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 910](numaker-m46x-pinctrl_8h.md#a44981668d2d7fe2b05b895c9a633f555)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_I2C3\_SMBSUS (0x0fUL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 911](numaker-m46x-pinctrl_8h.md#a51da53d066182fc059b394b1622441f5)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_HBI\_CK (0x10UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 912](numaker-m46x-pinctrl_8h.md#a8283d7ff32a790876a0a5fe8acb29a29)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_PSIO0\_CH1 (0x11UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 913](numaker-m46x-pinctrl_8h.md#a6a730ee7805aeea9e9002355f43d7508)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_KPI\_ROW1 (0x12UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

[ 914](numaker-m46x-pinctrl_8h.md#a1f3adf46e410f7821ddab867a1f49d11)#define NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_BMC21 (0x14UL << NUMAKER\_SYS\_GPC\_MFP1\_PC4MFP\_Pos)

915

916/\* PC.5 MFP \*/

[ 917](numaker-m46x-pinctrl_8h.md#ae22b48a8504cc3aeef870d3a31646200)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 918](numaker-m46x-pinctrl_8h.md#a17924bf70de6d7c93b5e73d7b988cf80)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_EBI\_AD5 (0x02UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 919](numaker-m46x-pinctrl_8h.md#a105774e67ce3b37c59332aee4c2d0439)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_SPIM\_D2 (0x03UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 920](numaker-m46x-pinctrl_8h.md#affd6c46313d7196d928507f695ce0373)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_QSPI0\_MISO1 (0x04UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 921](numaker-m46x-pinctrl_8h.md#aa98e59fa914e8d2ca7bdcc07263646f8)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_UART2\_TXD (0x08UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 922](numaker-m46x-pinctrl_8h.md#a200562191177a6c679c3cb4927508b84)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_I2C1\_SCL (0x09UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 923](numaker-m46x-pinctrl_8h.md#a8e750f858bd1e6d5992478718fff6094)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_CAN0\_TXD (0x0aUL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 924](numaker-m46x-pinctrl_8h.md#a2dc51e671f53fe475c1d95fac83e25d0)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_UART4\_TXD (0x0bUL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 925](numaker-m46x-pinctrl_8h.md#a8649703bb4092c0c7fc6fc2c25845019)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_EPWM1\_CH0 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 926](numaker-m46x-pinctrl_8h.md#aada7183b49482363d91d9759ebedcb90)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_CCAP\_DATA5 (0x0dUL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 927](numaker-m46x-pinctrl_8h.md#a5590b99db6f35da78f16d6a8a63920aa)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_QSPI1\_SS (0x0eUL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 928](numaker-m46x-pinctrl_8h.md#a09d7b3baa56e564c7b4182830b603fae)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_I2C3\_SMBAL (0x0fUL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 929](numaker-m46x-pinctrl_8h.md#a45e448d1b55c13e056e9e5c2e92343fb)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_HBI\_nCK (0x10UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 930](numaker-m46x-pinctrl_8h.md#a75d85f323721a2fd1f8e0b6fc2247dd3)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_PSIO0\_CH0 (0x11UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 931](numaker-m46x-pinctrl_8h.md#a413a1c089c68b34fd91dd061c129e6f6)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_KPI\_ROW0 (0x12UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

[ 932](numaker-m46x-pinctrl_8h.md#a26ee96674e7e86c4dff57673f32c3672)#define NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_BMC20 (0x14UL << NUMAKER\_SYS\_GPC\_MFP1\_PC5MFP\_Pos)

933

934/\* PC.6 MFP \*/

[ 935](numaker-m46x-pinctrl_8h.md#a383b2faa4894dbd8911861dc0786af4e)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 936](numaker-m46x-pinctrl_8h.md#abdc42ad8c74fd9b81c1f60e5d8b8af45)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_EBI\_AD8 (0x02UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 937](numaker-m46x-pinctrl_8h.md#a133f44c52f0f070d7191646c7835c57d)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_EMAC0\_RMII\_RXD1 (0x03UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 938](numaker-m46x-pinctrl_8h.md#af277aca04f609992a569426075fb584b)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_SPI1\_MOSI (0x04UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 939](numaker-m46x-pinctrl_8h.md#ae7e65febdf6e20d9fe558e290b575187)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_UART4\_RXD (0x05UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 940](numaker-m46x-pinctrl_8h.md#a17a81ab0213692acf6788ff24bb2e116)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_SC2\_RST (0x06UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 941](numaker-m46x-pinctrl_8h.md#ab8375c82498391b1de77c91fb63693cd)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_UART0\_nRTS (0x07UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 942](numaker-m46x-pinctrl_8h.md#a0b1f7c8ab145fc60d8f4475057f81b4a)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_I2C1\_SMBSUS (0x08UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 943](numaker-m46x-pinctrl_8h.md#a52149502591292cb2c8238b9cdb2e81a)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_UART6\_RXD (0x09UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 944](numaker-m46x-pinctrl_8h.md#a377101c651a580616d09d265695bdfd9)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_ACMP3\_WLAT (0x0aUL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 945](numaker-m46x-pinctrl_8h.md#aeac135a0392790f505d42d00d4706364)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_EPWM1\_CH3 (0x0bUL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 946](numaker-m46x-pinctrl_8h.md#ae950841aee26a8757d50e9ea5a3085ca)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_BPWM1\_CH1 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 947](numaker-m46x-pinctrl_8h.md#a05973a5c861c77050b1250f5e9c8b03f)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_CAN3\_RXD (0x0dUL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 948](numaker-m46x-pinctrl_8h.md#a4bcdc9cf6e33ee5a21c1df1e1a31959c)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_TM1 (0x0eUL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 949](numaker-m46x-pinctrl_8h.md#a6544f10ea1c75f7b7fdfd87e0222fb3e)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_INT2 (0x0fUL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 950](numaker-m46x-pinctrl_8h.md#aeaa383ff9ce4e9cd40e5c776d159837c)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_KPI\_COL2 (0x12UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 951](numaker-m46x-pinctrl_8h.md#a0f59c9c425dbe85d9c214a8e4d03c804)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_SPI6\_MOSI (0x13UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

[ 952](numaker-m46x-pinctrl_8h.md#ade4c2c694baa1c162c66c00fa3a02f88)#define NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_BMC25 (0x14UL << NUMAKER\_SYS\_GPC\_MFP1\_PC6MFP\_Pos)

953

954/\* PC.7 MFP \*/

[ 955](numaker-m46x-pinctrl_8h.md#a504a78b8b948681e6a7e8204dd7ac6bf)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 956](numaker-m46x-pinctrl_8h.md#af1e50b5e74dc2062ecdd22909d104dde)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_EBI\_AD9 (0x02UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 957](numaker-m46x-pinctrl_8h.md#aae9ded7c911d9cf922b6dbe688cb21bf)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_EMAC0\_RMII\_RXD0 (0x03UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 958](numaker-m46x-pinctrl_8h.md#a41f4e87688d32ca77d91ff51968915c7)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_SPI1\_MISO (0x04UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 959](numaker-m46x-pinctrl_8h.md#afc19ce0c32a0c9e52566f83ec2c1fdb2)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_UART4\_TXD (0x05UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 960](numaker-m46x-pinctrl_8h.md#ae40ca3761687d655ea17d718bbb94951)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_SC2\_PWR (0x06UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 961](numaker-m46x-pinctrl_8h.md#a7a9d8eb2eccbeccedd32c766aca8c8eb)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_UART0\_nCTS (0x07UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 962](numaker-m46x-pinctrl_8h.md#a10dbff1858bcb05a4cbb23e6cac3cf15)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_I2C1\_SMBAL (0x08UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 963](numaker-m46x-pinctrl_8h.md#a1a7471b158133da1ac3d9f75438e55cf)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_UART6\_TXD (0x09UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 964](numaker-m46x-pinctrl_8h.md#a391eef7693b10f6d34c3d745d8c026fd)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_ACMP2\_WLAT (0x0aUL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 965](numaker-m46x-pinctrl_8h.md#a11cc4214ce467458f53ebfb87e078a33)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_EPWM1\_CH2 (0x0bUL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 966](numaker-m46x-pinctrl_8h.md#a46bce09b04d2afb527bf4efc33f24ebb)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_BPWM1\_CH0 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 967](numaker-m46x-pinctrl_8h.md#a612824b11583e8528e2a3e3c923d0efc)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_CAN3\_TXD (0x0dUL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 968](numaker-m46x-pinctrl_8h.md#a6353679fdc15a514db4a8e2e5ac24408)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_TM0 (0x0eUL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 969](numaker-m46x-pinctrl_8h.md#aeea668562cae157badff6789a3b79621)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_INT3 (0x0fUL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 970](numaker-m46x-pinctrl_8h.md#a7650b0cb7ac6a71c40c74d1c748de4f6)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_KPI\_COL3 (0x12UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 971](numaker-m46x-pinctrl_8h.md#a9ca2193e3c4233221aae2e99228dca0e)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_SPI6\_MISO (0x13UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

[ 972](numaker-m46x-pinctrl_8h.md#a25588ba188f98db11b874953859c7693)#define NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_BMC24 (0x14UL << NUMAKER\_SYS\_GPC\_MFP1\_PC7MFP\_Pos)

973

974/\* PC.8 MFP \*/

[ 975](numaker-m46x-pinctrl_8h.md#a32d5e39a08983708d1a8f5a6e6f447a1)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

[ 976](numaker-m46x-pinctrl_8h.md#ae953b3b65c99a0061712d9bdd59401a9)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_EBI\_ADR16 (0x02UL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

[ 977](numaker-m46x-pinctrl_8h.md#a3a7b2d46cd997ff75addc5374c96420a)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_EMAC0\_RMII\_REFCLK (0x03UL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

[ 978](numaker-m46x-pinctrl_8h.md#a9979c3e373dc16b522bb263cc3fcf491)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_I2C0\_SDA (0x04UL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

[ 979](numaker-m46x-pinctrl_8h.md#accc875b1b5c189295cbec20bc3f25070)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_UART4\_nCTS (0x05UL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

[ 980](numaker-m46x-pinctrl_8h.md#a67d33831bdde1644c8de0d0ce5f3a643)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_UART1\_RXD (0x08UL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

[ 981](numaker-m46x-pinctrl_8h.md#ad8f40c755546eb65bfe96bc6ba6a660e)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_EPWM1\_CH1 (0x0bUL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

[ 982](numaker-m46x-pinctrl_8h.md#ae8850947009115d4ea23ab10198af7ad)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_BPWM1\_CH4 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

[ 983](numaker-m46x-pinctrl_8h.md#a4ab5458dedb96c96319188e2072694ce)#define NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_KPI\_COL4 (0x12UL << NUMAKER\_SYS\_GPC\_MFP2\_PC8MFP\_Pos)

984

985/\* PC.9 MFP \*/

[ 986](numaker-m46x-pinctrl_8h.md#a576331dbe11028c2f207fb62c3785bc4)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 987](numaker-m46x-pinctrl_8h.md#a4e829c753c31d69df698b3bbf2f0300a)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_EADC2\_CH10 (0x01UL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 988](numaker-m46x-pinctrl_8h.md#a1f6119411b54d5d9f2ef7d1fdcd5473b)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_ACMP3\_P1 (0x01UL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 989](numaker-m46x-pinctrl_8h.md#a2d58d6adc79ff4eda681fad0af4390bc)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_EBI\_ADR7 (0x02UL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 990](numaker-m46x-pinctrl_8h.md#a262b4397678f5a9e773afced67398a0b)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_UART6\_nCTS (0x05UL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 991](numaker-m46x-pinctrl_8h.md#a0e3ee70b4c81a971a7f363a300feaeaf)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_SPI3\_SS (0x06UL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 992](numaker-m46x-pinctrl_8h.md#a3fe5938208a8f2b39e0358ccb1986716)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_UART3\_RXD (0x07UL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 993](numaker-m46x-pinctrl_8h.md#a90ec1d9f4f50f31aa6dbe45812624e19)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_CAN1\_RXD (0x09UL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 994](numaker-m46x-pinctrl_8h.md#a5aef01523d23abebf5dc136a7be74ea8)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_I2C4\_SMBSUS (0x0aUL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 995](numaker-m46x-pinctrl_8h.md#a38b73267459a0d94b86cf7d3c996d17b)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_EPWM1\_CH3 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

[ 996](numaker-m46x-pinctrl_8h.md#af793d735a8f9c7e9653902c36c9d21e7)#define NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_EADC1\_ST (0x0eUL << NUMAKER\_SYS\_GPC\_MFP2\_PC9MFP\_Pos)

997

998/\* PC.10 MFP \*/

[ 999](numaker-m46x-pinctrl_8h.md#a303955fcf141e7fb4bf82d6a0bce2aba)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1000](numaker-m46x-pinctrl_8h.md#ae96cf3fb5ba0377e6042613941df2b46)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_EADC2\_CH11 (0x01UL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1001](numaker-m46x-pinctrl_8h.md#a12a3b6605df256ceaf01a59fdfc3c3ee)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_ACMP3\_P2 (0x01UL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1002](numaker-m46x-pinctrl_8h.md#aa906b876cc32823a8cf5bf40d2c378d1)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_EBI\_ADR6 (0x02UL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1003](numaker-m46x-pinctrl_8h.md#a45d22695ecabb56576998565a3edb8bf)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_UART6\_nRTS (0x05UL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1004](numaker-m46x-pinctrl_8h.md#a7807ede50677998f9d01c90546a54acb)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_SPI3\_CLK (0x06UL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1005](numaker-m46x-pinctrl_8h.md#a8ab562d165c9479a1557ec5f23d907c0)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_UART3\_TXD (0x07UL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1006](numaker-m46x-pinctrl_8h.md#a08106e1dfb9c40d9d26677c94904b5ca)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_CAN1\_TXD (0x09UL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1007](numaker-m46x-pinctrl_8h.md#ac1301df6fe710ee25e091fcd202b0d4c)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_I2C4\_SMBAL (0x0aUL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1008](numaker-m46x-pinctrl_8h.md#a5ce900d385cb435ece546dc6e458f31e)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_ECAP1\_IC0 (0x0bUL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1009](numaker-m46x-pinctrl_8h.md#a8bbd953c6f063f79ee3cf1c449221f0e)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_EPWM1\_CH2 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

[ 1010](numaker-m46x-pinctrl_8h.md#a9c6af7e5a395371889d1688f3f5349b1)#define NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_EADC1\_ST (0x0eUL << NUMAKER\_SYS\_GPC\_MFP2\_PC10MFP\_Pos)

1011

1012/\* PC.11 MFP \*/

[ 1013](numaker-m46x-pinctrl_8h.md#a504730c0723b5ca66d02c733a6193885)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1014](numaker-m46x-pinctrl_8h.md#ab8f3c443c57f88e6a445b883efd87a5f)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_EADC2\_CH12 (0x01UL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1015](numaker-m46x-pinctrl_8h.md#a7a2664260748cf89add49b561feae3a8)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_ACMP3\_P3 (0x01UL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1016](numaker-m46x-pinctrl_8h.md#a37fd6ee44dd4a549064f8bddfb2b0727)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_EBI\_ADR5 (0x02UL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1017](numaker-m46x-pinctrl_8h.md#a89e73f554bdef4e96c6ece1365293d20)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_UART0\_RXD (0x03UL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1018](numaker-m46x-pinctrl_8h.md#ab68e797f27f1ef3f91dbd23ed61506d0)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_I2C0\_SDA (0x04UL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1019](numaker-m46x-pinctrl_8h.md#ac625d79612adc10ad282def3cba6e954)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_UART6\_RXD (0x05UL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1020](numaker-m46x-pinctrl_8h.md#adcfca8a7416f47738b141453685eb399)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_SPI3\_MOSI (0x06UL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1021](numaker-m46x-pinctrl_8h.md#a57ef95c60c1f93217741c341546bb525)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_I2C4\_SDA (0x0aUL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1022](numaker-m46x-pinctrl_8h.md#a29f82012ee6de871825b9523d55b9569)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_ECAP1\_IC1 (0x0bUL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1023](numaker-m46x-pinctrl_8h.md#af00a9bdff380139722323651a4539b39)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_EPWM1\_CH1 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

[ 1024](numaker-m46x-pinctrl_8h.md#a51e6991bce849be536eac91e1660cac1)#define NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_ACMP1\_O (0x0eUL << NUMAKER\_SYS\_GPC\_MFP2\_PC11MFP\_Pos)

1025

1026/\* PC.12 MFP \*/

[ 1027](numaker-m46x-pinctrl_8h.md#a2c4a82dc8d8524920603a1dff5a792f3)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1028](numaker-m46x-pinctrl_8h.md#ac8a6d1424d371d042a92b58ca67feadf)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_EADC2\_CH13 (0x01UL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1029](numaker-m46x-pinctrl_8h.md#a20761a7db4177a84a7f5fcfc2cdc0475)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_EBI\_ADR4 (0x02UL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1030](numaker-m46x-pinctrl_8h.md#a68c8b9e65d5d01e24cd093035a931e51)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_UART0\_TXD (0x03UL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1031](numaker-m46x-pinctrl_8h.md#a8794e55498dc07e4dfcc45c8ce6f280f)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_I2C0\_SCL (0x04UL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1032](numaker-m46x-pinctrl_8h.md#ae7bdf46bf18fc3dfc2679720430752ba)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_UART6\_TXD (0x05UL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1033](numaker-m46x-pinctrl_8h.md#aea13cac7dada1fbc8f824082d7bece70)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_SPI3\_MISO (0x06UL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1034](numaker-m46x-pinctrl_8h.md#a2e425249a11d6fc33a47138474addf45)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_SC0\_nCD (0x09UL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1035](numaker-m46x-pinctrl_8h.md#a7f90eafa7d347befd12a92ff477496b3)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_I2C4\_SCL (0x0aUL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1036](numaker-m46x-pinctrl_8h.md#a209d85f07fd6434ac97de118ef8dcffe)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_ECAP1\_IC2 (0x0bUL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1037](numaker-m46x-pinctrl_8h.md#a761875c4797140b1ec09dfcea6dd0cc3)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_EPWM1\_CH0 (0x0cUL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

[ 1038](numaker-m46x-pinctrl_8h.md#a947b43bd7506437f6ccf468bf69eca6c)#define NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_ACMP0\_O (0x0eUL << NUMAKER\_SYS\_GPC\_MFP3\_PC12MFP\_Pos)

1039

1040/\* PC.13 MFP \*/

[ 1041](numaker-m46x-pinctrl_8h.md#aebd03737ecaad8e0d186bf61462bc412)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1042](numaker-m46x-pinctrl_8h.md#a1d1606ed83ce0926de1d6ac0f0e89326)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_EADC1\_CH3 (0x01UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1043](numaker-m46x-pinctrl_8h.md#aa45b3317061032b73be04a0b0afed4dd)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_EADC2\_CH3 (0x01UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1044](numaker-m46x-pinctrl_8h.md#ad5be2ff03a21699b9bd7e25bd23c2fca)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_EBI\_ADR10 (0x02UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1045](numaker-m46x-pinctrl_8h.md#a38c3dbe570881ccb0d2a2e0409a3d0e9)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_SC2\_nCD (0x03UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1046](numaker-m46x-pinctrl_8h.md#a94723b6dc1b9a7784938278e1ac20246)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_SPI2\_I2SMCLK (0x04UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1047](numaker-m46x-pinctrl_8h.md#ad9ca4ce393d27315e8af2d2b46ef1283)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_CAN1\_TXD (0x05UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1048](numaker-m46x-pinctrl_8h.md#a74c40a94879c95de5c184cbe4fb96f71)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_USCI0\_CTL0 (0x06UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1049](numaker-m46x-pinctrl_8h.md#a16c98967a5382e5ce4b84663cae06edf)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_UART2\_TXD (0x07UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1050](numaker-m46x-pinctrl_8h.md#ab671d15206424a8241381a78d2cbef6b)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_UART8\_nCTS (0x08UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1051](numaker-m46x-pinctrl_8h.md#a1ead929978dba4803072cd9c7b45ed99)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_BPWM0\_CH4 (0x09UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1052](numaker-m46x-pinctrl_8h.md#a1c2b79d22bd4b065aed577ee01b4e3fb)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_CLKO (0x0dUL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1053](numaker-m46x-pinctrl_8h.md#a2f3cf9743c7db0126889e8accaa67d85)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_EADC0\_ST (0x0eUL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

[ 1054](numaker-m46x-pinctrl_8h.md#ab786fde1da192065ba8d0a00f45a9fb3)#define NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_SPI9\_SS (0x13UL << NUMAKER\_SYS\_GPC\_MFP3\_PC13MFP\_Pos)

1055

1056/\* PC.14 MFP \*/

[ 1057](numaker-m46x-pinctrl_8h.md#a51cea1d1b1564ba120666bb06e6aecea)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1058](numaker-m46x-pinctrl_8h.md#abf8a12bf384cda5c4e31e2a779dc0d11)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_EBI\_AD11 (0x02UL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1059](numaker-m46x-pinctrl_8h.md#a70eb17f0db41ed399f50aa68ba8f314b)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_SC1\_nCD (0x03UL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1060](numaker-m46x-pinctrl_8h.md#a75e05f30a174502645fdb2d18f38423c)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_SPI0\_I2SMCLK (0x04UL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1061](numaker-m46x-pinctrl_8h.md#a8bca68bb7dbf2724f7a2cc606ddc5d9c)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_USCI0\_CTL0 (0x05UL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1062](numaker-m46x-pinctrl_8h.md#a06c22818740eca58b87caa015fead700)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_QSPI0\_CLK (0x06UL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1063](numaker-m46x-pinctrl_8h.md#a24982847cd191970a325c2b99b09476d)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_TRACE\_SWO (0x0aUL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1064](numaker-m46x-pinctrl_8h.md#a3f383282320d58d8c249fc54373b45b9)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_EPWM0\_SYNC\_IN (0x0bUL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1065](numaker-m46x-pinctrl_8h.md#adf6f320bd10e2e0792fb81370ae696ba)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_ETMC\_TRACE\_CLK (0x0cUL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1066](numaker-m46x-pinctrl_8h.md#aeb70d44bf8602ca1a362d7e8e4b31ba1)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_TM1 (0x0dUL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1067](numaker-m46x-pinctrl_8h.md#a1a59bae9f5bdc9ffcd9895a165f431f8)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_USB\_VBUS\_ST (0x0eUL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1068](numaker-m46x-pinctrl_8h.md#aed557bc9cafaa769d6658be4aea3525c)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_HSUSB\_VBUS\_ST (0x0fUL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1069](numaker-m46x-pinctrl_8h.md#ae8c5d0bee374aca5075f8a947c41f250)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_SPI9\_MOSI (0x13UL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

[ 1070](numaker-m46x-pinctrl_8h.md#ac4fa886055649480380323497db231d5)#define NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_BMC26 (0x14UL << NUMAKER\_SYS\_GPC\_MFP3\_PC14MFP\_Pos)

1071

1072/\* PD.0 MFP \*/

[ 1073](numaker-m46x-pinctrl_8h.md#a238c4c1be8a35c8b4994143bf88160ca)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1074](numaker-m46x-pinctrl_8h.md#a8558c1f89d66bf3802b7ef3cbf56e89b)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_EBI\_AD13 (0x02UL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1075](numaker-m46x-pinctrl_8h.md#a0b75075c374f061ceafdbb07bb8b078d)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_USCI0\_CLK (0x03UL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1076](numaker-m46x-pinctrl_8h.md#a8b4d13ef1a5d2389413c2cb069eb9cb5)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_SPI0\_MOSI (0x04UL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1077](numaker-m46x-pinctrl_8h.md#a9f3e715945a55bb4ef42019167abbb2c)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_UART3\_RXD (0x05UL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1078](numaker-m46x-pinctrl_8h.md#afa1d408fcf607bd710256109909924fc)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_I2C2\_SDA (0x06UL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1079](numaker-m46x-pinctrl_8h.md#abaae96097499636f9eb54e232a99d0ca)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_SC2\_CLK (0x07UL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1080](numaker-m46x-pinctrl_8h.md#a87de3ed5176045dbeaff19fe4e574e4e)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_I2S1\_DO (0x0aUL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1081](numaker-m46x-pinctrl_8h.md#a0cfa2b601058f56867a2807c4a616829)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_EQEI2\_A (0x0cUL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1082](numaker-m46x-pinctrl_8h.md#a4c44b4e11c42e844345f0c12a4608afa)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_ECAP2\_IC1 (0x0dUL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

[ 1083](numaker-m46x-pinctrl_8h.md#a7f0c636fd444a48c4584de95cce13cdf)#define NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_TM2 (0x0eUL << NUMAKER\_SYS\_GPD\_MFP0\_PD0MFP\_Pos)

1084

1085/\* PD.1 MFP \*/

[ 1086](numaker-m46x-pinctrl_8h.md#a1efedf42629d270a4a127c6f382ac59a)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1087](numaker-m46x-pinctrl_8h.md#a839d7d405866e03df9037b4478eabd05)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_EBI\_AD12 (0x02UL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1088](numaker-m46x-pinctrl_8h.md#a8a07e4add47d2d8506f9ef840a9118c4)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_USCI0\_DAT0 (0x03UL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1089](numaker-m46x-pinctrl_8h.md#af3846b0caf238f9a3242a4d2e83691ec)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_SPI0\_MISO (0x04UL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1090](numaker-m46x-pinctrl_8h.md#aa5984935ffc67c403fb2c0fa7ddf89b1)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_UART3\_TXD (0x05UL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1091](numaker-m46x-pinctrl_8h.md#a2b047e5c689a6d89f1274f1d3236e4d8)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_I2C2\_SCL (0x06UL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1092](numaker-m46x-pinctrl_8h.md#a393c9f200545ded9e67da8ff0d66c496)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_SC2\_DAT (0x07UL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1093](numaker-m46x-pinctrl_8h.md#aa34d817e24847812d87f238e4e1e4210)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_I2S1\_DI (0x0aUL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1094](numaker-m46x-pinctrl_8h.md#a7c934840e5c9cd4f6cd849475c1825db)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_EQEI2\_INDEX (0x0cUL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

[ 1095](numaker-m46x-pinctrl_8h.md#a5fc20cdb0e95dec7e736bcec15891c5b)#define NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_ECAP2\_IC0 (0x0dUL << NUMAKER\_SYS\_GPD\_MFP0\_PD1MFP\_Pos)

1096

1097/\* PD.2 MFP \*/

[ 1098](numaker-m46x-pinctrl_8h.md#a71d07db7f4a91a6be8e24e3675c90a2f)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

[ 1099](numaker-m46x-pinctrl_8h.md#aeb0d2137757c3e3ee40769df4bbfafb6)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_EBI\_AD11 (0x02UL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

[ 1100](numaker-m46x-pinctrl_8h.md#a9ed35a381e0ce19fbe946d6d73db4581)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_USCI0\_DAT1 (0x03UL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

[ 1101](numaker-m46x-pinctrl_8h.md#a3ed6121ea815b2d5afff0d5e694c63da)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_SPI0\_CLK (0x04UL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

[ 1102](numaker-m46x-pinctrl_8h.md#a241c1fe878c3fbb63ff655f5d9c29bb2)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_UART3\_nCTS (0x05UL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

[ 1103](numaker-m46x-pinctrl_8h.md#ac1fea02ddcf18b01d52212a0390084f0)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_SC2\_RST (0x07UL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

[ 1104](numaker-m46x-pinctrl_8h.md#a719f8485a1a912a342a87750109ff9ed)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_UART0\_RXD (0x09UL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

[ 1105](numaker-m46x-pinctrl_8h.md#a073cab7303a30ad3bb95300fb28637ef)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_I2S1\_MCLK (0x0aUL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

[ 1106](numaker-m46x-pinctrl_8h.md#a98738a669ff4e4e53ba6662637496f60)#define NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_EQEI3\_B (0x0dUL << NUMAKER\_SYS\_GPD\_MFP0\_PD2MFP\_Pos)

1107

1108/\* PD.3 MFP \*/

[ 1109](numaker-m46x-pinctrl_8h.md#a1a3b21e934d32802df0518efccc479c5)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1110](numaker-m46x-pinctrl_8h.md#adacab16d293caeeb87a42b7ac44c43e9)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_EBI\_AD10 (0x02UL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1111](numaker-m46x-pinctrl_8h.md#a2e38902eaab9cd013914d9a7172ac9d6)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_USCI0\_CTL1 (0x03UL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1112](numaker-m46x-pinctrl_8h.md#a1d0c307dbcc578a77ab5dc4da31b73ce)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_SPI0\_SS (0x04UL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1113](numaker-m46x-pinctrl_8h.md#ad5ac7d622f10bc1e9f6071ff4a58b219)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_UART3\_nRTS (0x05UL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1114](numaker-m46x-pinctrl_8h.md#a9bf71a3a5e78c2c7de1e72b412add41d)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_SC2\_PWR (0x07UL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1115](numaker-m46x-pinctrl_8h.md#a35bd39a3eae2f45d7009270608431ce8)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_SC1\_nCD (0x08UL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1116](numaker-m46x-pinctrl_8h.md#a0d0b4620733c14bd834a2d0c05976ea4)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_UART0\_TXD (0x09UL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1117](numaker-m46x-pinctrl_8h.md#ae2a3a3461375ef56aea81a7f400db9e8)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_I2S1\_BCLK (0x0aUL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

[ 1118](numaker-m46x-pinctrl_8h.md#acce5eb0530ddbf7dcf8a380ada3657af)#define NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_EQEI3\_A (0x0dUL << NUMAKER\_SYS\_GPD\_MFP0\_PD3MFP\_Pos)

1119

1120/\* PD.4 MFP \*/

[ 1121](numaker-m46x-pinctrl_8h.md#aa1cf97d96d7724d7dfb376ec0a8009e7)#define NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_Pos)

[ 1122](numaker-m46x-pinctrl_8h.md#afc7f7f50aa3389287eca1dd16a413465)#define NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_USCI0\_CTL0 (0x03UL << NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_Pos)

[ 1123](numaker-m46x-pinctrl_8h.md#a5a28a98539bf0ff3d3a097379961f96b)#define NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_I2C1\_SDA (0x04UL << NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_Pos)

[ 1124](numaker-m46x-pinctrl_8h.md#a9717104382a99276a6941dacbece555a)#define NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_SPI1\_SS (0x05UL << NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_Pos)

[ 1125](numaker-m46x-pinctrl_8h.md#a5e272f94f86f3439ca4c5f7d8d7282f2)#define NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_SC1\_CLK (0x08UL << NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_Pos)

[ 1126](numaker-m46x-pinctrl_8h.md#ae50c268c5c258929252b908f871250fc)#define NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_USB\_VBUS\_ST (0x0eUL << NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_Pos)

[ 1127](numaker-m46x-pinctrl_8h.md#a9214d0b1563e522328cf9a708873bd19)#define NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_PSIO0\_CH7 (0x11UL << NUMAKER\_SYS\_GPD\_MFP1\_PD4MFP\_Pos)

1128

1129/\* PD.5 MFP \*/

[ 1130](numaker-m46x-pinctrl_8h.md#a63086174e9f0b83f6f1c5dd8121307ad)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos)

[ 1131](numaker-m46x-pinctrl_8h.md#a7d99e995159ad88073c4f4d80caf3d0b)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_I2C1\_SCL (0x04UL << NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos)

[ 1132](numaker-m46x-pinctrl_8h.md#a96a7dd7e21f241322080ae8883858274)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_SPI1\_CLK (0x05UL << NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos)

[ 1133](numaker-m46x-pinctrl_8h.md#a32bec26be85aff261478203fdd9c602f)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_SC1\_DAT (0x08UL << NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos)

[ 1134](numaker-m46x-pinctrl_8h.md#af17916b800d5a4e769f46c11c54e00e3)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_ACMP1\_O (0x0eUL << NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos)

[ 1135](numaker-m46x-pinctrl_8h.md#ae500f0718c864d4585894f02ac829d27)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_EADC1\_ST (0x0fUL << NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos)

[ 1136](numaker-m46x-pinctrl_8h.md#a63a0d736a4cc796544266d588e5d136d)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_HBI\_nRESET (0x10UL << NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos)

[ 1137](numaker-m46x-pinctrl_8h.md#a20cab55c98377499b9c6d7aadf1fa223)#define NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_PSIO0\_CH6 (0x11UL << NUMAKER\_SYS\_GPD\_MFP1\_PD5MFP\_Pos)

1138

1139/\* PD.6 MFP \*/

[ 1140](numaker-m46x-pinctrl_8h.md#a89d2b9459a979f8b57dd33ab44a222da)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1141](numaker-m46x-pinctrl_8h.md#a364258f1139a428c2b8e6f6e1e7eaa13)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_EBI\_AD5 (0x02UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1142](numaker-m46x-pinctrl_8h.md#acaa844b210eb879b3fd3bc0e37f39af0)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_UART1\_RXD (0x03UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1143](numaker-m46x-pinctrl_8h.md#a48d1b62c2e553e6564ee0843526a2de5)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_I2C0\_SDA (0x04UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1144](numaker-m46x-pinctrl_8h.md#af8fef48ee52e40c9e747759c31002936)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_SPI1\_MOSI (0x05UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1145](numaker-m46x-pinctrl_8h.md#ab2571e3d365a4c9199f2a8d1618b8a7a)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_QSPI1\_MOSI0 (0x06UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1146](numaker-m46x-pinctrl_8h.md#a24a243cb369c00414e01a3aaf92377af)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_SC1\_RST (0x08UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1147](numaker-m46x-pinctrl_8h.md#a159899cccf5a1c4c02705348d7547aa2)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_ACMP0\_O (0x0eUL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1148](numaker-m46x-pinctrl_8h.md#a1a60f953762c08f49c9f3962640f148f)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_EADC0\_ST (0x0fUL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1149](numaker-m46x-pinctrl_8h.md#a3e08194b3affc6f865328d2a4fd0899e)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_HBI\_D0 (0x10UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

[ 1150](numaker-m46x-pinctrl_8h.md#aa71503ba1cf9738e247ffc73d51f35ab)#define NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_PSIO0\_CH5 (0x11UL << NUMAKER\_SYS\_GPD\_MFP1\_PD6MFP\_Pos)

1151

1152/\* PD.7 MFP \*/

[ 1153](numaker-m46x-pinctrl_8h.md#a9a0a478153a9383482ff2bb03902decd)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1154](numaker-m46x-pinctrl_8h.md#aaaaa9d744a125b1fe7982cf61baff914)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_EBI\_AD4 (0x02UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1155](numaker-m46x-pinctrl_8h.md#a8b3964eb9fc5da22d1b5cddb27a2a5ed)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_UART1\_TXD (0x03UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1156](numaker-m46x-pinctrl_8h.md#a33833806bfa9e6c2e7ffbdfc9041876f)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_I2C0\_SCL (0x04UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1157](numaker-m46x-pinctrl_8h.md#a4f08a463c4de925eb3d3129f9da743f4)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_SPI1\_MISO (0x05UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1158](numaker-m46x-pinctrl_8h.md#a8f9aa856b2e97117b8c5d1c8113eade5)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_QSPI1\_MISO0 (0x06UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1159](numaker-m46x-pinctrl_8h.md#a8268c0b72d01fe1f618ca0b1703918d4)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_CCAP\_HSYNC (0x07UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1160](numaker-m46x-pinctrl_8h.md#ab9f940b9642a6553dd175631c0842899)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_SC1\_PWR (0x08UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1161](numaker-m46x-pinctrl_8h.md#a7a4eba68d08ede96c7c6e095805fedcd)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_HBI\_D1 (0x10UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

[ 1162](numaker-m46x-pinctrl_8h.md#aa2ca4a412ed77a1c75a104a0396f8d06)#define NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_PSIO0\_CH4 (0x11UL << NUMAKER\_SYS\_GPD\_MFP1\_PD7MFP\_Pos)

1163

1164/\* PD.8 MFP \*/

[ 1165](numaker-m46x-pinctrl_8h.md#a9eec9a34cd5d12dcb37dad5ae10fcf1b)#define NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_Pos)

[ 1166](numaker-m46x-pinctrl_8h.md#a9640c0d52bda03da90d39acd0cba1975)#define NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_EBI\_AD6 (0x02UL << NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_Pos)

[ 1167](numaker-m46x-pinctrl_8h.md#afef46b257624791c5afc4384f6e07fe3)#define NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_I2C2\_SDA (0x03UL << NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_Pos)

[ 1168](numaker-m46x-pinctrl_8h.md#a7f6b157c87977bd1b386523955ff1907)#define NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_UART2\_nRTS (0x04UL << NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_Pos)

[ 1169](numaker-m46x-pinctrl_8h.md#a93dabe726fda3364580771cbc8060469)#define NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_UART7\_RXD (0x05UL << NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_Pos)

[ 1170](numaker-m46x-pinctrl_8h.md#a696c3ac9cb6f5a9638807d0d7dc45e74)#define NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_CAN2\_RXD (0x06UL << NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_Pos)

[ 1171](numaker-m46x-pinctrl_8h.md#a27fc8599debe34ec81050b3ac6ac332d)#define NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_PSIO0\_CH3 (0x11UL << NUMAKER\_SYS\_GPD\_MFP2\_PD8MFP\_Pos)

1172

1173/\* PD.9 MFP \*/

[ 1174](numaker-m46x-pinctrl_8h.md#a9ab9db289b6cb48f9c7c5d57fb981f8f)#define NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_Pos)

[ 1175](numaker-m46x-pinctrl_8h.md#a2a076d5df62f36bc40c8b2bc963748a0)#define NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_EBI\_AD7 (0x02UL << NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_Pos)

[ 1176](numaker-m46x-pinctrl_8h.md#a676d294a5e6c6909fb53f833c9f5d265)#define NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_I2C2\_SCL (0x03UL << NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_Pos)

[ 1177](numaker-m46x-pinctrl_8h.md#a53de67bb5cad5e0aece7e3d94d417b04)#define NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_UART2\_nCTS (0x04UL << NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_Pos)

[ 1178](numaker-m46x-pinctrl_8h.md#adc47ba47266677b4d8593d0f924857cc)#define NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_UART7\_TXD (0x05UL << NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_Pos)

[ 1179](numaker-m46x-pinctrl_8h.md#a5b848d16bd4faae98ac8a33ee465ee26)#define NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_CAN2\_TXD (0x06UL << NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_Pos)

[ 1180](numaker-m46x-pinctrl_8h.md#a14bbf23901f34c47ccc7e43ef4b8a92e)#define NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_PSIO0\_CH2 (0x11UL << NUMAKER\_SYS\_GPD\_MFP2\_PD9MFP\_Pos)

1181

1182/\* PD.10 MFP \*/

[ 1183](numaker-m46x-pinctrl_8h.md#a38d6ed3254dd36dffbd8733b6a0c710d)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1184](numaker-m46x-pinctrl_8h.md#ac29d2d465f483e94bcaf22a40b47155f)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_EADC1\_CH0 (0x01UL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1185](numaker-m46x-pinctrl_8h.md#a92bbdfda0049e70749db6f20c43f7a16)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_EADC2\_CH0 (0x01UL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1186](numaker-m46x-pinctrl_8h.md#a00e78774d8944b97817f7a78bedbda63)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_EBI\_nCS2 (0x02UL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1187](numaker-m46x-pinctrl_8h.md#a6b899984d3b1f733df7a153a0b0f4e0c)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_UART1\_RXD (0x03UL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1188](numaker-m46x-pinctrl_8h.md#abe18d9005c59dfbf6bf4c69c1fc8e656)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_CAN0\_RXD (0x04UL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1189](numaker-m46x-pinctrl_8h.md#a8798f61f53eb902ccb8ea02d2a9fdf8f)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_UART8\_RXD (0x08UL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1190](numaker-m46x-pinctrl_8h.md#a4d4f50bb703d2ac5aad7d93d97fbc8fd)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_EQEI0\_B (0x0aUL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1191](numaker-m46x-pinctrl_8h.md#a03f1193154d65acd54f78ce3235e704a)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_ECAP3\_IC2 (0x0bUL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1192](numaker-m46x-pinctrl_8h.md#a0425f3bcebcffadad9bf62eb5b01f361)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_INT7 (0x0fUL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

[ 1193](numaker-m46x-pinctrl_8h.md#a49147da0a3ac328cf91ef288985d91af)#define NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_SPI9\_MOSI (0x13UL << NUMAKER\_SYS\_GPD\_MFP2\_PD10MFP\_Pos)

1194

1195/\* PD.11 MFP \*/

[ 1196](numaker-m46x-pinctrl_8h.md#ad6eaca5076fc21c245a5f93323b899f0)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1197](numaker-m46x-pinctrl_8h.md#a128bbb70da8d34a92f859390998f00b6)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_EADC1\_CH1 (0x01UL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1198](numaker-m46x-pinctrl_8h.md#af53e5e8244917c4ffea02aedb220cda3)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_EADC2\_CH1 (0x01UL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1199](numaker-m46x-pinctrl_8h.md#af22913d69ce420cef2f75db4b5f31dbb)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_EBI\_nCS1 (0x02UL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1200](numaker-m46x-pinctrl_8h.md#a1c1f78acd7ebe7aba7a3a6c16ab2da5f)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_UART1\_TXD (0x03UL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1201](numaker-m46x-pinctrl_8h.md#a244bab64b125bfd9873cebea493467f8)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_CAN0\_TXD (0x04UL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1202](numaker-m46x-pinctrl_8h.md#a9479a3b8387ad59bc783db27cb25b273)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_UART8\_TXD (0x08UL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1203](numaker-m46x-pinctrl_8h.md#a0ba88b4097e3324174e6218f6c5f43c3)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_EQEI0\_A (0x0aUL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1204](numaker-m46x-pinctrl_8h.md#ae0f2c411a1f0a6062e060dbbc02abad7)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_ECAP3\_IC1 (0x0bUL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1205](numaker-m46x-pinctrl_8h.md#a9cefbb7a3251e14734e9bcd86742ad6e)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_INT6 (0x0fUL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

[ 1206](numaker-m46x-pinctrl_8h.md#aa8f2e5e93aca0526ddeb1378b7e328b3)#define NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_SPI9\_MISO (0x13UL << NUMAKER\_SYS\_GPD\_MFP2\_PD11MFP\_Pos)

1207

1208/\* PD.12 MFP \*/

[ 1209](numaker-m46x-pinctrl_8h.md#a7777d5b6836c71f05f4a5a86f818fd88)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1210](numaker-m46x-pinctrl_8h.md#a8a69904d727051f3c990a3ce0f877eaf)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_EADC1\_CH2 (0x01UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1211](numaker-m46x-pinctrl_8h.md#a7f187c71c482dde6fdf1bb3232d5776f)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_EADC2\_CH2 (0x01UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1212](numaker-m46x-pinctrl_8h.md#a4219c5d2a3ea9c02d0c1c954e155accc)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_EBI\_nCS0 (0x02UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1213](numaker-m46x-pinctrl_8h.md#a582b057b15151ba968107ae24d67df9a)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_CAN1\_RXD (0x05UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1214](numaker-m46x-pinctrl_8h.md#a4959f76f0907ea5e2cea0321dfcdb310)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_UART2\_RXD (0x07UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1215](numaker-m46x-pinctrl_8h.md#aebb7862305c6d00747622cd8a72140a5)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_UART8\_nRTS (0x08UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1216](numaker-m46x-pinctrl_8h.md#a2c5b4609c285291cf913fb073547d74c)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_BPWM0\_CH5 (0x09UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1217](numaker-m46x-pinctrl_8h.md#aa21c5e73d74f02915f8c45911d326b57)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_EQEI0\_INDEX (0x0aUL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1218](numaker-m46x-pinctrl_8h.md#a6769ae109bce336850bd50b67ea3816c)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_ECAP3\_IC0 (0x0bUL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1219](numaker-m46x-pinctrl_8h.md#a9a7702506be2249c42eb9edd2cc8efae)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_CLKO (0x0dUL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1220](numaker-m46x-pinctrl_8h.md#ac8aa14bfa70c425a7c027c5120b90c3c)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_EADC0\_ST (0x0eUL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1221](numaker-m46x-pinctrl_8h.md#a681c792bf27e82fabc954830c50681ac)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_INT5 (0x0fUL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

[ 1222](numaker-m46x-pinctrl_8h.md#a5d1295bf846a2a5c0b931c2434bfc580)#define NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_SPI9\_CLK (0x13UL << NUMAKER\_SYS\_GPD\_MFP3\_PD12MFP\_Pos)

1223

1224/\* PD.13 MFP \*/

[ 1225](numaker-m46x-pinctrl_8h.md#aa1b6c92d461ac3935c245fd2defe56c5)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1226](numaker-m46x-pinctrl_8h.md#a237aca53a276b2ef88708f5ec88754ef)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_EBI\_AD10 (0x02UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1227](numaker-m46x-pinctrl_8h.md#a2afd118b8edf949098b803e302060577)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_SD0\_nCD (0x03UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1228](numaker-m46x-pinctrl_8h.md#a5694d0b6c6a132dc0960c321d7c2cca0)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_SPI0\_I2SMCLK (0x04UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1229](numaker-m46x-pinctrl_8h.md#a834b961e8d27815b9b65bf14a4d88121)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_SPI1\_I2SMCLK (0x05UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1230](numaker-m46x-pinctrl_8h.md#ab39c2b749995c058cff9d9feb0f2e0a9)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_QSPI1\_MOSI0 (0x06UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1231](numaker-m46x-pinctrl_8h.md#ac766180576cb3969879d5980760c867f)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_SC2\_nCD (0x07UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1232](numaker-m46x-pinctrl_8h.md#a599aa80455149c8231424c74d5d05eae)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_SD1\_CLK (0x08UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1233](numaker-m46x-pinctrl_8h.md#aaf09c13ce470465a4779b3e1ff96f536)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_UART6\_RXD (0x09UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1234](numaker-m46x-pinctrl_8h.md#adec75ef4835425195795af2e9b9b40dc)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_I2S1\_LRCK (0x0aUL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1235](numaker-m46x-pinctrl_8h.md#a8a498b5d24850f90ba97559f151b9387)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_BPWM0\_CH0 (0x0bUL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1236](numaker-m46x-pinctrl_8h.md#a5ea6a6f1f7dd515874da387869c1aab2)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_EQEI2\_B (0x0cUL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1237](numaker-m46x-pinctrl_8h.md#ac2ff86962ed0487cfc367340182626f3)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_ECAP2\_IC2 (0x0dUL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1238](numaker-m46x-pinctrl_8h.md#a4796cd0999e208d049dbb775b21f40cd)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_CLKO (0x0eUL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1239](numaker-m46x-pinctrl_8h.md#a04ce0dc96d8544c8d7e508f56a743a39)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_EADC0\_ST (0x0fUL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

[ 1240](numaker-m46x-pinctrl_8h.md#ac54ca2b96ace503c599d936a6b042ac4)#define NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_QSPI1\_MOSI1 (0x13UL << NUMAKER\_SYS\_GPD\_MFP3\_PD13MFP\_Pos)

1241

1242/\* PD.14 MFP \*/

[ 1243](numaker-m46x-pinctrl_8h.md#a879b393a24d57964bd373846390d03fa)#define NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_Pos)

[ 1244](numaker-m46x-pinctrl_8h.md#ab1848b2434830e0f632c50f641b8ff6f)#define NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_EBI\_nCS0 (0x02UL << NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_Pos)

[ 1245](numaker-m46x-pinctrl_8h.md#a2f250dc1f3d5174569d1fd797cab04b9)#define NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_SPI3\_I2SMCLK (0x03UL << NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_Pos)

[ 1246](numaker-m46x-pinctrl_8h.md#a3a00e0804b40c071b216a0f50ffb68f7)#define NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_SC1\_nCD (0x04UL << NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_Pos)

[ 1247](numaker-m46x-pinctrl_8h.md#a041c23e6f01146b0e4b2dce33de2ec52)#define NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_SPI0\_I2SMCLK (0x05UL << NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_Pos)

[ 1248](numaker-m46x-pinctrl_8h.md#aee02418d3e986dda4585dabf1bf99117)#define NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_I2S1\_BCLK (0x0aUL << NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_Pos)

[ 1249](numaker-m46x-pinctrl_8h.md#a157f2d511c86ec11cf2ff05a27233871)#define NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_EPWM0\_CH4 (0x0bUL << NUMAKER\_SYS\_GPD\_MFP3\_PD14MFP\_Pos)

1250

1251/\* PE.0 MFP \*/

[ 1252](numaker-m46x-pinctrl_8h.md#a2a931b06f89d402a958f98945230ea53)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1253](numaker-m46x-pinctrl_8h.md#a97f12fc698879d9529da5c2418ea8c67)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_EBI\_AD11 (0x02UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1254](numaker-m46x-pinctrl_8h.md#a29de59078a350ed759b8aec05f3eab22)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_QSPI0\_MOSI0 (0x03UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1255](numaker-m46x-pinctrl_8h.md#a04e0ca5ca291a9d8047eeb24ed24b1f4)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_SC2\_CLK (0x04UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1256](numaker-m46x-pinctrl_8h.md#a9b73cced79f89b9ae5952a668d944ad9)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_I2S0\_MCLK (0x05UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1257](numaker-m46x-pinctrl_8h.md#a37b7021e821728f5a09872c6420b1883)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_SPI1\_MOSI (0x06UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1258](numaker-m46x-pinctrl_8h.md#ad8cf8c8ae13a253770a99a99f3d402c8)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_UART3\_RXD (0x07UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1259](numaker-m46x-pinctrl_8h.md#ac18e546c120a6fd9694ab2e7a8da399a)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_I2C1\_SDA (0x08UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1260](numaker-m46x-pinctrl_8h.md#acb6f62c633409e11c663277369c2e553)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_UART4\_nRTS (0x09UL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

[ 1261](numaker-m46x-pinctrl_8h.md#a747b407ed82bfb08942512fc4538dc5d)#define NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_UART8\_RXD (0x0aUL << NUMAKER\_SYS\_GPE\_MFP0\_PE0MFP\_Pos)

1262

1263/\* PE.1 MFP \*/

[ 1264](numaker-m46x-pinctrl_8h.md#a83cdbe20c6a58db7f89f1a9ba5a28f32)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1265](numaker-m46x-pinctrl_8h.md#ad99fe50de4118e6e8d86c749efb6cf02)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_EBI\_AD10 (0x02UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1266](numaker-m46x-pinctrl_8h.md#a8a614cb7a33499ad16b21b8b147f99be)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_QSPI0\_MISO0 (0x03UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1267](numaker-m46x-pinctrl_8h.md#a57026953cc639e6d49a0605f37de4b7c)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_SC2\_DAT (0x04UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1268](numaker-m46x-pinctrl_8h.md#a41a396705cf1a1a0eb18b562fd43d697)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_I2S0\_BCLK (0x05UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1269](numaker-m46x-pinctrl_8h.md#aee9a052f2a867717ec83e6050f150c2c)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_SPI1\_MISO (0x06UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1270](numaker-m46x-pinctrl_8h.md#abc475845225dd871ecd48b4a2005062e)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_UART3\_TXD (0x07UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1271](numaker-m46x-pinctrl_8h.md#a09c5e51aed58eff43928d19a7d702ed6)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_I2C1\_SCL (0x08UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1272](numaker-m46x-pinctrl_8h.md#ae8b05a7617fe19cd3c9f31c85290c012)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_UART4\_nCTS (0x09UL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

[ 1273](numaker-m46x-pinctrl_8h.md#ad0a0d55425456935fea091d24507df4c)#define NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_UART8\_TXD (0x0aUL << NUMAKER\_SYS\_GPE\_MFP0\_PE1MFP\_Pos)

1274

1275/\* PE.2 MFP \*/

[ 1276](numaker-m46x-pinctrl_8h.md#af37f595d39a55902c84f0b924651e6c8)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1277](numaker-m46x-pinctrl_8h.md#aaed86cd9b8149b61af779d555143e985)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_EBI\_ALE (0x02UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1278](numaker-m46x-pinctrl_8h.md#a41df17fc962efeee3e70dfb78eafdb56)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_SD0\_DAT0 (0x03UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1279](numaker-m46x-pinctrl_8h.md#af516e5f3d68c01e188973d9d474f7db4)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_SPIM\_MOSI (0x04UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1280](numaker-m46x-pinctrl_8h.md#a02523f83598df71022ce4473185ad9bb)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_SPI3\_MOSI (0x05UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1281](numaker-m46x-pinctrl_8h.md#ad9d408d726d61e672b53c639f6489d77)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_SC0\_CLK (0x06UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1282](numaker-m46x-pinctrl_8h.md#ac846f41cbe77e2c3c5d3bd94903a31fa)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_USCI0\_CLK (0x07UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1283](numaker-m46x-pinctrl_8h.md#a8c0ecbdfd9a5e967eb82d2c24e97af4b)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_UART6\_nCTS (0x08UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1284](numaker-m46x-pinctrl_8h.md#a695ab712b9176820138bf1193145ee57)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_UART7\_RXD (0x09UL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1285](numaker-m46x-pinctrl_8h.md#ab84a79220803903beb5520eaa183fcba)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_UART8\_nRTS (0x0aUL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1286](numaker-m46x-pinctrl_8h.md#a6ec4889e2aa763e578a975f700001927)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_EQEI0\_B (0x0bUL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1287](numaker-m46x-pinctrl_8h.md#aaaeaf06072b31a577aa6cf051f917b05)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_EPWM0\_CH5 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

[ 1288](numaker-m46x-pinctrl_8h.md#adfbf3c0484433c20807ede670bcd6ffd)#define NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_BPWM0\_CH0 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP0\_PE2MFP\_Pos)

1289

1290/\* PE.3 MFP \*/

[ 1291](numaker-m46x-pinctrl_8h.md#a9cc5ed5e316be20d65bf70682c123c23)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1292](numaker-m46x-pinctrl_8h.md#a116f830fa8637e73a1fe36d7aca36b9c)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_EBI\_MCLK (0x02UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1293](numaker-m46x-pinctrl_8h.md#ab1a3779ee691f64a8b776c2c4475fcab)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_SD0\_DAT1 (0x03UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1294](numaker-m46x-pinctrl_8h.md#a37af3951c569800c26b6818eda53486e)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_SPIM\_MISO (0x04UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1295](numaker-m46x-pinctrl_8h.md#a7f7ef7e4e7565a0c485c319470132eb2)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_SPI3\_MISO (0x05UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1296](numaker-m46x-pinctrl_8h.md#a51b93e22ed31498cd2149a790c6f0c1d)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_SC0\_DAT (0x06UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1297](numaker-m46x-pinctrl_8h.md#accf45ea81500c845fc261af809874fc6)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_USCI0\_DAT0 (0x07UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1298](numaker-m46x-pinctrl_8h.md#a5471abc6c4d644bd31ebbc721045d4c0)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_UART6\_nRTS (0x08UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1299](numaker-m46x-pinctrl_8h.md#a96deecafe5e08ad23b2eb987681f495e)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_UART7\_TXD (0x09UL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1300](numaker-m46x-pinctrl_8h.md#a5128c4755a7098c2541a269d30540d48)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_UART8\_nCTS (0x0aUL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1301](numaker-m46x-pinctrl_8h.md#a1c0400df309851205b74400cf99160c7)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_EQEI0\_A (0x0bUL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1302](numaker-m46x-pinctrl_8h.md#a08f93c5821d5fa1900665909e708e788)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_EPWM0\_CH4 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

[ 1303](numaker-m46x-pinctrl_8h.md#a097c98b41be4b48ad78063b59da00212)#define NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_BPWM0\_CH1 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP0\_PE3MFP\_Pos)

1304

1305/\* PE.4 MFP \*/

[ 1306](numaker-m46x-pinctrl_8h.md#ad04bbc0b1561a27f30c5be605f7f7fdc)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1307](numaker-m46x-pinctrl_8h.md#a37d6bb970c6e2f59f5da0b008e780ca7)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_EBI\_nWR (0x02UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1308](numaker-m46x-pinctrl_8h.md#abdf60aa5d000fa187e1609c6910c4ccc)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_SD0\_DAT2 (0x03UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1309](numaker-m46x-pinctrl_8h.md#a0c16fa14728c781a95006056d95a7476)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_SPIM\_CLK (0x04UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1310](numaker-m46x-pinctrl_8h.md#a8f1485303823fcedb479f8ced38adf77)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_SPI3\_CLK (0x05UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1311](numaker-m46x-pinctrl_8h.md#a8540d5d3e0dca8f904238e42aa71acf6)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_SC0\_RST (0x06UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1312](numaker-m46x-pinctrl_8h.md#a5116db43b1c18833ebf9c3496355646a)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_USCI0\_DAT1 (0x07UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1313](numaker-m46x-pinctrl_8h.md#a8fa9ccf58617bd2a91274a8c71daf7a0)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_UART6\_RXD (0x08UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1314](numaker-m46x-pinctrl_8h.md#a9b23fce2a20afcd5675103ac5d977702)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_UART7\_nCTS (0x09UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1315](numaker-m46x-pinctrl_8h.md#a04fe8228f897335f292c4479ca172150)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_UART9\_RXD (0x0aUL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1316](numaker-m46x-pinctrl_8h.md#adc08cfe6d68cb00ba68ff39d45c3689a)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_EQEI0\_INDEX (0x0bUL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1317](numaker-m46x-pinctrl_8h.md#a615cce8a6529c9201b0340b0ce5f0066)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_EPWM0\_CH3 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1318](numaker-m46x-pinctrl_8h.md#a14d2e2e76e9f6e4aa1e7fd02880da6d4)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_BPWM0\_CH2 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

[ 1319](numaker-m46x-pinctrl_8h.md#ae65464f429626c72aa70a9eb6d6eca20)#define NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_PSIO0\_CH3 (0x11UL << NUMAKER\_SYS\_GPE\_MFP1\_PE4MFP\_Pos)

1320

1321/\* PE.5 MFP \*/

[ 1322](numaker-m46x-pinctrl_8h.md#a72a31c79d35f6b0d214bcf1e1df98f4a)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1323](numaker-m46x-pinctrl_8h.md#a2e0f070f399bd31d08e6ae96a2309afb)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_EBI\_nRD (0x02UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1324](numaker-m46x-pinctrl_8h.md#a6f8265213dd59dd3d91272e0905a7296)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_SD0\_DAT3 (0x03UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1325](numaker-m46x-pinctrl_8h.md#a48b4dfbd3e977adf27a801bf4b67aaa1)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_SPIM\_SS (0x04UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1326](numaker-m46x-pinctrl_8h.md#aef81473d4cb5deb7d4b482f3337f17ff)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_SPI3\_SS (0x05UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1327](numaker-m46x-pinctrl_8h.md#a15489373d989b0fc264c22dd956ca7c5)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_SC0\_PWR (0x06UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1328](numaker-m46x-pinctrl_8h.md#ab6758d503f5c81f71d660eb974d25f19)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_USCI0\_CTL1 (0x07UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1329](numaker-m46x-pinctrl_8h.md#a1d22dd768d38d6460d7add2e739c3b26)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_UART6\_TXD (0x08UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1330](numaker-m46x-pinctrl_8h.md#aea882ad29258085ee03cbc132091f5c2)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_UART7\_nRTS (0x09UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1331](numaker-m46x-pinctrl_8h.md#a788a4fb38dee31a08790d17645b81ddf)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_UART9\_TXD (0x0aUL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1332](numaker-m46x-pinctrl_8h.md#ae2734cae10e2cb91de569dec51355bed)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_EQEI1\_B (0x0bUL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1333](numaker-m46x-pinctrl_8h.md#a19067133346ba574979cda7eddf3b169)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_EPWM0\_CH2 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1334](numaker-m46x-pinctrl_8h.md#a6bef33303b9f1e5dc6c4a35fc4ba7354)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_BPWM0\_CH3 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

[ 1335](numaker-m46x-pinctrl_8h.md#aa860ab6d484ced3a673b3f2ac361fc97)#define NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_PSIO0\_CH2 (0x11UL << NUMAKER\_SYS\_GPE\_MFP1\_PE5MFP\_Pos)

1336

1337/\* PE.6 MFP \*/

[ 1338](numaker-m46x-pinctrl_8h.md#a2c3d8b39b23dde001a957b26e4d706e4)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1339](numaker-m46x-pinctrl_8h.md#a75e35046a04785c6984f30d4add68ed6)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_SD0\_CLK (0x03UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1340](numaker-m46x-pinctrl_8h.md#a2bb00a9fe7e0444e4328063b47dd8571)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_SPIM\_D3 (0x04UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1341](numaker-m46x-pinctrl_8h.md#a29c017fc07c743e5d6f123e80bb33f8f)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_SPI3\_I2SMCLK (0x05UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1342](numaker-m46x-pinctrl_8h.md#a166b3f02fa0c9b5c60ef6e1b3269058b)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_SC0\_nCD (0x06UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1343](numaker-m46x-pinctrl_8h.md#a7944c9a72d80c75ab221c00f3b8f2b45)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_USCI0\_CTL0 (0x07UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1344](numaker-m46x-pinctrl_8h.md#a9884190364c6a2b6f7b6bda995306ba0)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_UART5\_RXD (0x08UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1345](numaker-m46x-pinctrl_8h.md#ae26ebfcf7da6d310dc18d129b2277e15)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_CAN1\_RXD (0x09UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1346](numaker-m46x-pinctrl_8h.md#a74166bd21aa445056ade999c05429cca)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_UART9\_nRTS (0x0aUL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1347](numaker-m46x-pinctrl_8h.md#ac9443c8adf19e194a49154e7ffa7804f)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_EQEI1\_A (0x0bUL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1348](numaker-m46x-pinctrl_8h.md#aa74f2368cd5a8e467870c40dcfdb35e3)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_EPWM0\_CH1 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1349](numaker-m46x-pinctrl_8h.md#aead177bf165b86f7d270551eabaa7601)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_BPWM0\_CH4 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1350](numaker-m46x-pinctrl_8h.md#ae834967b8b803727303a1ab9328a4406)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_ACMP3\_O (0x0eUL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

[ 1351](numaker-m46x-pinctrl_8h.md#a51a63c325cba741b924dc7a211ffe075)#define NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_PSIO0\_CH1 (0x11UL << NUMAKER\_SYS\_GPE\_MFP1\_PE6MFP\_Pos)

1352

1353/\* PE.7 MFP \*/

[ 1354](numaker-m46x-pinctrl_8h.md#a500196bc80c67841b32daefc2fb7e6e3)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1355](numaker-m46x-pinctrl_8h.md#aeb7d8189791344ab0919baa3651ac525)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_SD0\_CMD (0x03UL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1356](numaker-m46x-pinctrl_8h.md#a3a468ce78ee151f0daf0128970355e79)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_SPIM\_D2 (0x04UL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1357](numaker-m46x-pinctrl_8h.md#a619e48e6b78188304257a2fe407fb524)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_UART5\_TXD (0x08UL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1358](numaker-m46x-pinctrl_8h.md#a7e67d70cd15257da6e3a4be45878aae1)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_CAN1\_TXD (0x09UL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1359](numaker-m46x-pinctrl_8h.md#a745a12caba2cf6c41d152288e5a0f206)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_UART9\_nCTS (0x0aUL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1360](numaker-m46x-pinctrl_8h.md#a1ae779030735e78362887b425ef888c1)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_EQEI1\_INDEX (0x0bUL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1361](numaker-m46x-pinctrl_8h.md#a7a287ed08e8d9b7985bba22ce8911dfd)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_EPWM0\_CH0 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1362](numaker-m46x-pinctrl_8h.md#af966a764a82c1534e0689cdd334a1d7a)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_BPWM0\_CH5 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1363](numaker-m46x-pinctrl_8h.md#a21db3cc0e3058282b0a8087edc16d57a)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_ACMP2\_O (0x0eUL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

[ 1364](numaker-m46x-pinctrl_8h.md#ad9ae6916905c811c9a82d7f5929958db)#define NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_PSIO0\_CH0 (0x11UL << NUMAKER\_SYS\_GPE\_MFP1\_PE7MFP\_Pos)

1365

1366/\* PE.8 MFP \*/

[ 1367](numaker-m46x-pinctrl_8h.md#a5e868d91fa6264101a903b271adc1e40)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1368](numaker-m46x-pinctrl_8h.md#ae4894c2bcc21330994fd5dc6f0728381)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_EBI\_ADR10 (0x02UL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1369](numaker-m46x-pinctrl_8h.md#a6f8ea45dfb449ad3420381d9e0458957)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_EMAC0\_RMII\_MDC (0x03UL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1370](numaker-m46x-pinctrl_8h.md#a05bfba009f7db32d5e9c0946c0a8a7b4)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_I2S0\_BCLK (0x04UL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1371](numaker-m46x-pinctrl_8h.md#a9103e4f4c2a3fca0c48ed34d2cb28b51)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_SPI2\_CLK (0x05UL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1372](numaker-m46x-pinctrl_8h.md#add5ccde146f05bfe6cded7637db0ccc8)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_UART2\_TXD (0x07UL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1373](numaker-m46x-pinctrl_8h.md#a20aca32e43d5838d97448f5d27a95d3c)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_EPWM0\_CH0 (0x0aUL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1374](numaker-m46x-pinctrl_8h.md#a28c165ffa9cced89370b47fcb85bbfb7)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_EPWM0\_BRAKE0 (0x0bUL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1375](numaker-m46x-pinctrl_8h.md#a8eef928f6b765d2886f4a1e31bb06c61)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_ECAP0\_IC0 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1376](numaker-m46x-pinctrl_8h.md#a24cd1cd7f799db822af61af7bb705c61)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_EQEI2\_INDEX (0x0dUL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1377](numaker-m46x-pinctrl_8h.md#a7a961a8b04058f1fb50f6ae54b8116bf)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_TRACE\_DATA3 (0x0eUL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

[ 1378](numaker-m46x-pinctrl_8h.md#a877baed8b746257b621503d6a411ec24)#define NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_ECAP3\_IC0 (0x0fUL << NUMAKER\_SYS\_GPE\_MFP2\_PE8MFP\_Pos)

1379

1380/\* PE.9 MFP \*/

[ 1381](numaker-m46x-pinctrl_8h.md#a3ed21a61a496b1d1ae8f98e000b726e0)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1382](numaker-m46x-pinctrl_8h.md#a6f08f971a2c80a614458bd22abfb71b5)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_EBI\_ADR11 (0x02UL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1383](numaker-m46x-pinctrl_8h.md#ad37bc264a7010be6600fe5e6442bf7fa)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_EMAC0\_RMII\_MDIO (0x03UL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1384](numaker-m46x-pinctrl_8h.md#a5fc4e99bb3cab1bfd76c4440d736b0d7)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_I2S0\_MCLK (0x04UL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1385](numaker-m46x-pinctrl_8h.md#a2b2a8d6e10f80ddef32903d8edd301e2)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_SPI2\_MISO (0x05UL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1386](numaker-m46x-pinctrl_8h.md#a486b3cb6860fa0bb987408a96e9b3bd4)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_UART2\_RXD (0x07UL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1387](numaker-m46x-pinctrl_8h.md#a884d305936f5b789ece85224cba1c49a)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_EPWM0\_CH1 (0x0aUL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1388](numaker-m46x-pinctrl_8h.md#a930add4aee7ed800a7b35598fcde5a31)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_EPWM0\_BRAKE1 (0x0bUL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1389](numaker-m46x-pinctrl_8h.md#a337d808fd4f8987c7ee7e1f302e9e360)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_ECAP0\_IC1 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1390](numaker-m46x-pinctrl_8h.md#acffd5e3643644f4e0ea28467f73df6c2)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_EQEI2\_A (0x0dUL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1391](numaker-m46x-pinctrl_8h.md#a011ba631ea1d7e5af527247d23c9af20)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_TRACE\_DATA2 (0x0eUL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

[ 1392](numaker-m46x-pinctrl_8h.md#ab3ca0581376fdd490b796126aa8125eb)#define NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_ECAP3\_IC1 (0x0fUL << NUMAKER\_SYS\_GPE\_MFP2\_PE9MFP\_Pos)

1393

1394/\* PE.10 MFP \*/

[ 1395](numaker-m46x-pinctrl_8h.md#abc71749256ec403692ac9c0feec8007c)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1396](numaker-m46x-pinctrl_8h.md#a5868de2d373417c39be0d3604a8dae08)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_EBI\_ADR12 (0x02UL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1397](numaker-m46x-pinctrl_8h.md#af49f3a789b7a4fa0c4eec7818aa9fc34)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_EMAC0\_RMII\_TXD0 (0x03UL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1398](numaker-m46x-pinctrl_8h.md#aae953acb7e1c88dae52fc917a2087e7f)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_I2S0\_DI (0x04UL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1399](numaker-m46x-pinctrl_8h.md#a7d8953b9c7c4b97102804b0b6eebb576)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_SPI2\_MOSI (0x05UL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1400](numaker-m46x-pinctrl_8h.md#ab8563b2fdce1f3fe46a7e607fe7e1706)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_UART3\_TXD (0x07UL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1401](numaker-m46x-pinctrl_8h.md#a4ac5c01578105c9b8fd0576794b6e112)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_EPWM0\_CH2 (0x0aUL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1402](numaker-m46x-pinctrl_8h.md#a5c0eba0876aec58cc9e9599d676ae1f6)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_EPWM1\_BRAKE0 (0x0bUL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1403](numaker-m46x-pinctrl_8h.md#aba61b29fd65c07bfb8da8194400b12d7)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_ECAP0\_IC2 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1404](numaker-m46x-pinctrl_8h.md#a4e7a1de8f8dc5864686a1fb7349859a8)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_EQEI2\_B (0x0dUL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1405](numaker-m46x-pinctrl_8h.md#a74f6454ef30bfa8f0afc05047948ebdf)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_TRACE\_DATA1 (0x0eUL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

[ 1406](numaker-m46x-pinctrl_8h.md#aa3f8adc326e3d76e33c1c9272069626d)#define NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_ECAP3\_IC2 (0x0fUL << NUMAKER\_SYS\_GPE\_MFP2\_PE10MFP\_Pos)

1407

1408/\* PE.11 MFP \*/

[ 1409](numaker-m46x-pinctrl_8h.md#a007c41b386214ccfabc4ae6755db2e7a)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1410](numaker-m46x-pinctrl_8h.md#a3dbe082a27c058661f65b553ed5ec2a8)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_EBI\_ADR13 (0x02UL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1411](numaker-m46x-pinctrl_8h.md#a36f2397dbcfdfdbaf156a9afd33ecdd8)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_EMAC0\_RMII\_TXD1 (0x03UL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1412](numaker-m46x-pinctrl_8h.md#a4981f23dea39867c703bf0513d26a3a6)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_I2S0\_DO (0x04UL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1413](numaker-m46x-pinctrl_8h.md#a823d4217b77c72b3969982cfeeff66f7)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_SPI2\_SS (0x05UL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1414](numaker-m46x-pinctrl_8h.md#ab0a903b196e67943e594076023e77934)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_UART3\_RXD (0x07UL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1415](numaker-m46x-pinctrl_8h.md#a4ac7511c61484e8afb9f54293e894ae1)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_UART1\_nCTS (0x08UL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1416](numaker-m46x-pinctrl_8h.md#a25a86e67d463836c5a04722fd5c32820)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_EPWM0\_CH3 (0x0aUL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1417](numaker-m46x-pinctrl_8h.md#a9fe70f1f3e0261c20dbc272c6960eb7c)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_EPWM1\_BRAKE1 (0x0bUL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1418](numaker-m46x-pinctrl_8h.md#a7d506613c5aa608984dc7cab38f69656)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_ECAP1\_IC2 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1419](numaker-m46x-pinctrl_8h.md#aa36772376e93233034cfccd6c9facdfb)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_TRACE\_DATA0 (0x0eUL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

[ 1420](numaker-m46x-pinctrl_8h.md#a3c5a6d531501fbe7de6520f81034f27e)#define NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_KPI\_COL7 (0x12UL << NUMAKER\_SYS\_GPE\_MFP2\_PE11MFP\_Pos)

1421

1422/\* PE.12 MFP \*/

[ 1423](numaker-m46x-pinctrl_8h.md#a52264cf70f80dd46a5f8844be2062519)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1424](numaker-m46x-pinctrl_8h.md#a05fd59a93c507d43de15fcb2ca709dc4)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_EBI\_ADR14 (0x02UL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1425](numaker-m46x-pinctrl_8h.md#a0f917e1fb33cb14c8278ebdda1c29f14)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_EMAC0\_RMII\_TXEN (0x03UL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1426](numaker-m46x-pinctrl_8h.md#ae93fb0e85969339b13b7cc396c1013b1)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_I2S0\_LRCK (0x04UL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1427](numaker-m46x-pinctrl_8h.md#acc1d6a669b44e3c0b0bf4e04b462c486)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_SPI2\_I2SMCLK (0x05UL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1428](numaker-m46x-pinctrl_8h.md#ab22d4ed35d18b3f9e8a0ed0cb1c10ec1)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_UART1\_nRTS (0x08UL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1429](numaker-m46x-pinctrl_8h.md#a2cb3dd44c61bd6d34bc4b37bdf0d34c6)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_EPWM0\_CH4 (0x0aUL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1430](numaker-m46x-pinctrl_8h.md#ac7d232eefbba046c52b294a7bffa155b)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_ECAP1\_IC1 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1431](numaker-m46x-pinctrl_8h.md#acf70a4f93a37bd49a0322d76258cbdbd)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_TRACE\_CLK (0x0eUL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

[ 1432](numaker-m46x-pinctrl_8h.md#a6994b796bf9fd7e88c00bf1a905bac06)#define NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_KPI\_COL6 (0x12UL << NUMAKER\_SYS\_GPE\_MFP3\_PE12MFP\_Pos)

1433

1434/\* PE.13 MFP \*/

[ 1435](numaker-m46x-pinctrl_8h.md#a4d4599803eda492d1414dfbb0b80a00e)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1436](numaker-m46x-pinctrl_8h.md#a770372713a2c8aae9d3aa874a92c9bcc)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_EBI\_ADR15 (0x02UL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1437](numaker-m46x-pinctrl_8h.md#a74194bfe4e6c4415aec244de05973cc8)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_EMAC0\_PPS (0x03UL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1438](numaker-m46x-pinctrl_8h.md#a217ad0163c550bc2f8c3ef31293c5430)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_I2C0\_SCL (0x04UL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1439](numaker-m46x-pinctrl_8h.md#a750bbcc56ca7a674e8a0a7797e6a3b21)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_UART4\_nRTS (0x05UL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1440](numaker-m46x-pinctrl_8h.md#af0a91f083a45a4a84292ec30d63f41cb)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_UART1\_TXD (0x08UL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1441](numaker-m46x-pinctrl_8h.md#ada391c232b91cce38050206b1e292135)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_EPWM0\_CH5 (0x0aUL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1442](numaker-m46x-pinctrl_8h.md#a1806fd7bb67e3fbc8f4730227f2c3d7c)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_EPWM1\_CH0 (0x0bUL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1443](numaker-m46x-pinctrl_8h.md#a10139681f113e62b042b66ef2e084ec4)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_BPWM1\_CH5 (0x0cUL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1444](numaker-m46x-pinctrl_8h.md#ac459ea3b936843e590b07cea56c77834)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_ECAP1\_IC0 (0x0dUL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1445](numaker-m46x-pinctrl_8h.md#a5af93661586f6bc270e7cdb7d8445e4e)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_TRACE\_SWO (0x0eUL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

[ 1446](numaker-m46x-pinctrl_8h.md#a3df0bd6a7563f2192f7abed6bd04b004)#define NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_KPI\_COL5 (0x12UL << NUMAKER\_SYS\_GPE\_MFP3\_PE13MFP\_Pos)

1447

1448/\* PE.14 MFP \*/

[ 1449](numaker-m46x-pinctrl_8h.md#a2ec176999330d68f0fbcca4ecd46aeae)#define NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_Pos)

[ 1450](numaker-m46x-pinctrl_8h.md#a9bdfb6a28627d8d4f8383bcbfd0a0c01)#define NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_EBI\_AD8 (0x02UL << NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_Pos)

[ 1451](numaker-m46x-pinctrl_8h.md#a38364265f0f95794d62322336cc69002)#define NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_UART2\_TXD (0x03UL << NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_Pos)

[ 1452](numaker-m46x-pinctrl_8h.md#a6e6f8f7db45a16be85ef24be1a24b586)#define NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_CAN0\_TXD (0x04UL << NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_Pos)

[ 1453](numaker-m46x-pinctrl_8h.md#ae6c480e9c1fae6b04c8be85715c115f4)#define NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_SD1\_nCD (0x05UL << NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_Pos)

[ 1454](numaker-m46x-pinctrl_8h.md#a437e2e50a470a99e9d95b5451d86f6de)#define NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_UART6\_TXD (0x06UL << NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_Pos)

[ 1455](numaker-m46x-pinctrl_8h.md#afaf0e74b1dc387bf723d72dd31cda0f2)#define NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_PSIO0\_CH0 (0x11UL << NUMAKER\_SYS\_GPE\_MFP3\_PE14MFP\_Pos)

1456

1457/\* PE.15 MFP \*/

[ 1458](numaker-m46x-pinctrl_8h.md#a7959311f07d841bb5ab6a342d1f57843)#define NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_Pos)

[ 1459](numaker-m46x-pinctrl_8h.md#a2b09da12f84914a6980c37ad6ea96b49)#define NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_EBI\_AD9 (0x02UL << NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_Pos)

[ 1460](numaker-m46x-pinctrl_8h.md#ac549d0119848445159a5dafd88138ec3)#define NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_UART2\_RXD (0x03UL << NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_Pos)

[ 1461](numaker-m46x-pinctrl_8h.md#ab144643e9e2818ed14eb25d07c57dd2e)#define NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_CAN0\_RXD (0x04UL << NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_Pos)

[ 1462](numaker-m46x-pinctrl_8h.md#ac090bb834d3b1e1fba10051301423b64)#define NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_UART6\_RXD (0x06UL << NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_Pos)

[ 1463](numaker-m46x-pinctrl_8h.md#afa62cbeb8523f88be222dfec7a81330e)#define NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_PSIO0\_CH1 (0x11UL << NUMAKER\_SYS\_GPE\_MFP3\_PE15MFP\_Pos)

1464

1465/\* PF.0 MFP \*/

[ 1466](numaker-m46x-pinctrl_8h.md#ae46cdab32f8ad624c2d684f62da9c81b)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1467](numaker-m46x-pinctrl_8h.md#afe1c80b3e0249c2c7697b235d93dd36b)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_UART1\_TXD (0x02UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1468](numaker-m46x-pinctrl_8h.md#a404ef8325172bfce91131a3a958592b8)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_I2C1\_SCL (0x03UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1469](numaker-m46x-pinctrl_8h.md#a3a8835da423dd87309cc5875e849277d)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_UART0\_TXD (0x04UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1470](numaker-m46x-pinctrl_8h.md#ad2cef3d5884acf6bf70c860e2f531ff1)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_SC1\_DAT (0x05UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1471](numaker-m46x-pinctrl_8h.md#a5e83bb284b6e739ff958b920363c5b4b)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_I2S0\_DO (0x06UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1472](numaker-m46x-pinctrl_8h.md#a18b7fce4855dee9cac362117c39f4064)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_UART2\_TXD (0x08UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1473](numaker-m46x-pinctrl_8h.md#ad39e2204bde3c720af0a8f799d9dc24c)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_I2C0\_SCL (0x09UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1474](numaker-m46x-pinctrl_8h.md#a1ae2350bb8b7bb0d1f550c06e47c4c98)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_CAN2\_TXD (0x0aUL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1475](numaker-m46x-pinctrl_8h.md#a758864c0eaba947409ffc49a3fb07452)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_EPWM1\_CH4 (0x0bUL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1476](numaker-m46x-pinctrl_8h.md#ad7d846080e9446f9476f791fc3ae9b71)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_BPWM1\_CH0 (0x0cUL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1477](numaker-m46x-pinctrl_8h.md#a01a1ea0ce6a8bcbd5cad7f694a59cb46)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_ACMP0\_O (0x0dUL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1478](numaker-m46x-pinctrl_8h.md#a006b8ef828c0c2cb1235938f5440f948)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_ICE\_DAT (0x0eUL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1479](numaker-m46x-pinctrl_8h.md#afa42e54243daaf75ba21910d531eb4bb)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_EADC0\_ST (0x0fUL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

[ 1480](numaker-m46x-pinctrl_8h.md#aacf10188db52698f4b45ed107b2dd93d)#define NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_QSPI1\_MISO0 (0x13UL << NUMAKER\_SYS\_GPF\_MFP0\_PF0MFP\_Pos)

1481

1482/\* PF.1 MFP \*/

[ 1483](numaker-m46x-pinctrl_8h.md#a7e85d8419867dbadfbe5506fac560c0e)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1484](numaker-m46x-pinctrl_8h.md#ac95ea22d2f9aaa11fc71dd1d44cd6a86)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_UART1\_RXD (0x02UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1485](numaker-m46x-pinctrl_8h.md#a621937c4496604372f24f33e93b86a23)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_I2C1\_SDA (0x03UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1486](numaker-m46x-pinctrl_8h.md#a30ebc3a63f0ff13ef75b55041c96579e)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_UART0\_RXD (0x04UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1487](numaker-m46x-pinctrl_8h.md#a8c342784734ac3cc690b833cd352f3a4)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_SC1\_CLK (0x05UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1488](numaker-m46x-pinctrl_8h.md#a5ed4e37e8205575d4da05d7abcb9a270)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_I2S0\_LRCK (0x06UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1489](numaker-m46x-pinctrl_8h.md#ade3a25b305ef5d7bb5430f28f9c14ab9)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_UART2\_RXD (0x08UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1490](numaker-m46x-pinctrl_8h.md#a534dec0220459b284db533fc051157a7)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_I2C0\_SDA (0x09UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1491](numaker-m46x-pinctrl_8h.md#acefa70a8675f784d65b6c8b7f8ac7ea8)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_CAN2\_RXD (0x0aUL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1492](numaker-m46x-pinctrl_8h.md#ab73b7b8814d0fb76bae266db29c9ffdf)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_EPWM1\_CH5 (0x0bUL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1493](numaker-m46x-pinctrl_8h.md#a66cc58223e2d216a9e74ca64e520004e)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_BPWM1\_CH1 (0x0cUL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1494](numaker-m46x-pinctrl_8h.md#ae144e6ecd6eeedae9eb722a6ef5e1128)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_ACMP1\_O (0x0dUL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1495](numaker-m46x-pinctrl_8h.md#a90ee9325fe5e097e080120ba60eb6af1)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_ICE\_CLK (0x0eUL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1496](numaker-m46x-pinctrl_8h.md#a7c66fee22773d733438bfd78ebd1f05b)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_EADC1\_ST (0x0fUL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

[ 1497](numaker-m46x-pinctrl_8h.md#a4d7c4db86a7455360058f5ad802b2547)#define NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_QSPI1\_MOSI0 (0x13UL << NUMAKER\_SYS\_GPF\_MFP0\_PF1MFP\_Pos)

1498

1499/\* PF.2 MFP \*/

[ 1500](numaker-m46x-pinctrl_8h.md#ae1859995298c71401181bc9644bcf497)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1501](numaker-m46x-pinctrl_8h.md#aa25de381334cce1dce6b571c4aed6cf3)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_EBI\_nCS1 (0x02UL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1502](numaker-m46x-pinctrl_8h.md#a7018125f26a83ac63dec26c063fbcf4f)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_UART0\_RXD (0x03UL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1503](numaker-m46x-pinctrl_8h.md#a43e4620a658c70151a289dc3d16263ed)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_I2C0\_SDA (0x04UL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1504](numaker-m46x-pinctrl_8h.md#a500c9b67647edb2d8ebe7e00a89ec824)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_QSPI0\_CLK (0x05UL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1505](numaker-m46x-pinctrl_8h.md#ad0991bf86fa5b64157108c4623a511ac)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_UART9\_RXD (0x07UL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1506](numaker-m46x-pinctrl_8h.md#ab788d08d3d6b532ea1ac0c57bc95dc6c)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_XT1\_OUT (0x0aUL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1507](numaker-m46x-pinctrl_8h.md#ac49cac93fced927de27a90c03b3662ee)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_BPWM1\_CH1 (0x0bUL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1508](numaker-m46x-pinctrl_8h.md#ad9c1fb0741921a5fb15539ebfd562476)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_I2C4\_SMBSUS (0x0cUL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1509](numaker-m46x-pinctrl_8h.md#a4332581b4134b13e3ead3325328ca144)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_ACMP3\_O (0x0dUL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

[ 1510](numaker-m46x-pinctrl_8h.md#a53426055439e01b887f78b2e326fbead)#define NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_BMC13 (0x14UL << NUMAKER\_SYS\_GPF\_MFP0\_PF2MFP\_Pos)

1511

1512/\* PF.3 MFP \*/

[ 1513](numaker-m46x-pinctrl_8h.md#a120d9dcb780928771af0244c1fc7755a)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1514](numaker-m46x-pinctrl_8h.md#a70853c1c9e70eeb6a0b07eac6d88f35c)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_EBI\_nCS0 (0x02UL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1515](numaker-m46x-pinctrl_8h.md#a4a7b8946dd1ed06b8d5e0dc6c54e1e4e)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_UART0\_TXD (0x03UL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1516](numaker-m46x-pinctrl_8h.md#ae375cc3e36908c27ae37b1251a3e05c6)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_I2C0\_SCL (0x04UL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1517](numaker-m46x-pinctrl_8h.md#a0d00983f3406ebdc539601e651fec39b)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_UART9\_TXD (0x07UL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1518](numaker-m46x-pinctrl_8h.md#a82cf2cd8be1603ce1a9aab4e35db65d4)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_XT1\_IN (0x0aUL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1519](numaker-m46x-pinctrl_8h.md#ab68cbb8f3e4e3506e8b67d7d4d5b98a4)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_BPWM1\_CH0 (0x0bUL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1520](numaker-m46x-pinctrl_8h.md#a73cc104547ab04999ff520a677305d76)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_I2C4\_SMBAL (0x0cUL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1521](numaker-m46x-pinctrl_8h.md#acdd139db62d1a1477551db91cae7b3af)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_ACMP2\_O (0x0dUL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1522](numaker-m46x-pinctrl_8h.md#a6084e7a0663d6a62ae24d1ccb7a508ce)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_EADC2\_ST (0x0fUL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

[ 1523](numaker-m46x-pinctrl_8h.md#ac4f9c28656f7bed1c10dca6af686e86f)#define NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_BMC12 (0x14UL << NUMAKER\_SYS\_GPF\_MFP0\_PF3MFP\_Pos)

1524

1525/\* PF.4 MFP \*/

[ 1526](numaker-m46x-pinctrl_8h.md#a556dd37ce4160f684d8cf0075535b50c)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1527](numaker-m46x-pinctrl_8h.md#a176558269bcd0145907625c82e94b61f)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_UART2\_TXD (0x02UL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1528](numaker-m46x-pinctrl_8h.md#ad415286af9258710cd75ee5175554ded)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_EBI\_AD0 (0x03UL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1529](numaker-m46x-pinctrl_8h.md#a958cdc7afe18acb76b8da9db33c45d98)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_UART2\_nRTS (0x04UL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1530](numaker-m46x-pinctrl_8h.md#abc21ee857eb391f75aae5ed52d9ce34b)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_EPWM0\_CH1 (0x07UL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1531](numaker-m46x-pinctrl_8h.md#aaf53f3a5e61c54a8caaf8979ad6e1486)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_BPWM0\_CH5 (0x08UL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1532](numaker-m46x-pinctrl_8h.md#a56e5264d48e1fc44523dc6cf3bc7b4ef)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_X32\_OUT (0x0aUL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1533](numaker-m46x-pinctrl_8h.md#a78d7131294320c4b65c07461363cf715)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_EADC1\_ST (0x0bUL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1534](numaker-m46x-pinctrl_8h.md#ac26cbabd85a61a6e05841425e6912b60)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_I2C4\_SDA (0x0cUL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1535](numaker-m46x-pinctrl_8h.md#a2095c32f17df267c874d2a97006205b8)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_EQEI2\_B (0x0dUL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1536](numaker-m46x-pinctrl_8h.md#a7ae766a1737aae14338eba465a19d733)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_SPI5\_MISO (0x13UL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

[ 1537](numaker-m46x-pinctrl_8h.md#aefe70e2dafd2f553c5a0c546df3a90d1)#define NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_BMC11 (0x14UL << NUMAKER\_SYS\_GPF\_MFP1\_PF4MFP\_Pos)

1538

1539/\* PF.5 MFP \*/

[ 1540](numaker-m46x-pinctrl_8h.md#acc4015fcd54dee2feaab093ba9a084aa)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1541](numaker-m46x-pinctrl_8h.md#a05f11c07bc4095a80db86b6124447ac7)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_UART2\_RXD (0x02UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1542](numaker-m46x-pinctrl_8h.md#ac049fcf3bed70c9e166cc88475b6bb58)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_EBI\_AD1 (0x03UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1543](numaker-m46x-pinctrl_8h.md#af985adcbd13befbca1d9c5f827b31584)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_UART2\_nCTS (0x04UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1544](numaker-m46x-pinctrl_8h.md#a460b7026076e9e3a327952d4a61cad9c)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_EPWM0\_CH0 (0x07UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1545](numaker-m46x-pinctrl_8h.md#a0a3239e3c4370d0d3ff1fb9e43dd33dd)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_BPWM0\_CH4 (0x08UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1546](numaker-m46x-pinctrl_8h.md#adf9153081fbb4c69182f02b75b27994d)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_EPWM0\_SYNC\_OUT (0x09UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1547](numaker-m46x-pinctrl_8h.md#a36588bc054dd3d54c427fd36bf115712)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_X32\_IN (0x0aUL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1548](numaker-m46x-pinctrl_8h.md#a2c9fc7fe06654ea0230f38456b779006)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_EADC0\_ST (0x0bUL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1549](numaker-m46x-pinctrl_8h.md#a4dc38b58f6d5dbf46719e40c456bea21)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_I2C4\_SCL (0x0cUL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1550](numaker-m46x-pinctrl_8h.md#a4a85ef1ffd1139b42581b72d622cb4f0)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_EQEI2\_A (0x0dUL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1551](numaker-m46x-pinctrl_8h.md#af8ac20faa897f64e6bd9269600105167)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_SPI5\_MOSI (0x13UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

[ 1552](numaker-m46x-pinctrl_8h.md#a6bbf7c6a38a6fe239cc14ce2f41be0a3)#define NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_BMC10 (0x14UL << NUMAKER\_SYS\_GPF\_MFP1\_PF5MFP\_Pos)

1553

1554/\* PF.6 MFP \*/

[ 1555](numaker-m46x-pinctrl_8h.md#ab5590bd69c0bc9dd75ce8a840bce5e69)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1556](numaker-m46x-pinctrl_8h.md#ac5fa240dc36b2efb8a1a7a33598bcfa4)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_EBI\_ADR19 (0x02UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1557](numaker-m46x-pinctrl_8h.md#a6b7f5543cb4f7596d521304423041e28)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_SC0\_CLK (0x03UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1558](numaker-m46x-pinctrl_8h.md#aac1d8cb3e3b0eb87f0bcd70202d90c40)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_I2S0\_LRCK (0x04UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1559](numaker-m46x-pinctrl_8h.md#a818fb00bf5f13f8336b7b11fa001c192)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_SPI0\_MOSI (0x05UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1560](numaker-m46x-pinctrl_8h.md#a3ca562827525fb3303da363e660309aa)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_UART4\_RXD (0x06UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1561](numaker-m46x-pinctrl_8h.md#a90237d911f9d32636b341125abb5b3d4)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_EBI\_nCS0 (0x07UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1562](numaker-m46x-pinctrl_8h.md#aba53822e7db5b8b5ce51a7c4cc8b3412)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_CAN2\_RXD (0x08UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1563](numaker-m46x-pinctrl_8h.md#a9fe52f6c5455da2cb4b76e5380b12685)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_SPI3\_I2SMCLK (0x09UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1564](numaker-m46x-pinctrl_8h.md#ac21cb5c85f144226d68f7fe6e8b81b27)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_TAMPER0 (0x0aUL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1565](numaker-m46x-pinctrl_8h.md#a9bc12a552da1b321f854f21377a72732)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_EQEI2\_INDEX (0x0dUL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1566](numaker-m46x-pinctrl_8h.md#a10d967d0a9e7d4763fcfaaf8092363d4)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_TRACE\_SWO (0x0eUL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

[ 1567](numaker-m46x-pinctrl_8h.md#a452c8d92ab5d9bef4c665f7e819849ad)#define NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_SPI5\_CLK (0x13UL << NUMAKER\_SYS\_GPF\_MFP1\_PF6MFP\_Pos)

1568

1569/\* PF.7 MFP \*/

[ 1570](numaker-m46x-pinctrl_8h.md#a9b77d9e03218197c67e8e71d62f4563c)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1571](numaker-m46x-pinctrl_8h.md#ac3a194e2e7e11d8271f80fe6cf14f51d)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_EBI\_ADR18 (0x02UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1572](numaker-m46x-pinctrl_8h.md#ad611b59ba90c98029e766165775d37bc)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_SC0\_DAT (0x03UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1573](numaker-m46x-pinctrl_8h.md#af56dc25eeee4b08f4e82dea8eec2c7fe)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_I2S0\_DO (0x04UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1574](numaker-m46x-pinctrl_8h.md#a848f13d29567ac9d3247c6eb428b22c7)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_SPI0\_MISO (0x05UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1575](numaker-m46x-pinctrl_8h.md#a1c9ad0daee77bf03bf8f00a6c741e09c)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_UART4\_TXD (0x06UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1576](numaker-m46x-pinctrl_8h.md#a66b3e7e3ac95ecf998687e9e20c2a75b)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_CCAP\_DATA0 (0x07UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1577](numaker-m46x-pinctrl_8h.md#ad5b7d041476d5c3a5e36d85ffe1af49c)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_CAN2\_TXD (0x08UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1578](numaker-m46x-pinctrl_8h.md#a5d1fe595bf420dc3ec8b794c4c9184b1)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_TAMPER1 (0x0aUL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

[ 1579](numaker-m46x-pinctrl_8h.md#a3dad7f9214fd95903272bf28bcf618cd)#define NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_SPI5\_SS (0x13UL << NUMAKER\_SYS\_GPF\_MFP1\_PF7MFP\_Pos)

1580

1581/\* PF.8 MFP \*/

[ 1582](numaker-m46x-pinctrl_8h.md#ac530a0fe9ee0020d55631734c0431ced)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1583](numaker-m46x-pinctrl_8h.md#afa3d31d91fb628ffb44bfe4ba07d8dbb)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_EBI\_ADR17 (0x02UL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1584](numaker-m46x-pinctrl_8h.md#ae0d6f25f594ca464d82a5d68870fc500)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_SC0\_RST (0x03UL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1585](numaker-m46x-pinctrl_8h.md#a273c5a486fb2138edfa54febf2cb301b)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_I2S0\_DI (0x04UL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1586](numaker-m46x-pinctrl_8h.md#a58dd99906835c8816a29fff8903e5171)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_SPI0\_CLK (0x05UL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1587](numaker-m46x-pinctrl_8h.md#ad3329dc8361902fd39b293e5a38f7bb3)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_UART5\_nCTS (0x06UL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1588](numaker-m46x-pinctrl_8h.md#a47e13fdddb1312c0fedd32f0370ac008)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_CCAP\_DATA1 (0x07UL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1589](numaker-m46x-pinctrl_8h.md#a531fbf3f5326252ec7ecf9156dbdb74d)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_CAN1\_RXD (0x08UL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1590](numaker-m46x-pinctrl_8h.md#a47bdda1dbef33635b37998779262b3cc)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_TAMPER2 (0x0aUL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

[ 1591](numaker-m46x-pinctrl_8h.md#a689f0e07803721e4e292f5bbcf1ffc6a)#define NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_UART9\_RXD (0x0bUL << NUMAKER\_SYS\_GPF\_MFP2\_PF8MFP\_Pos)

1592

1593/\* PF.9 MFP \*/

[ 1594](numaker-m46x-pinctrl_8h.md#a89dbca328d43b62adc0a5c50d153d7d3)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1595](numaker-m46x-pinctrl_8h.md#a5ffe6e0f41cd415fa0e01131bf322ca4)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_EBI\_ADR16 (0x02UL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1596](numaker-m46x-pinctrl_8h.md#a7b19ee17ab8dcb02367399e6b8f58622)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_SC0\_PWR (0x03UL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1597](numaker-m46x-pinctrl_8h.md#a64bcd78d49e07394db961acd79efa188)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_I2S0\_MCLK (0x04UL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1598](numaker-m46x-pinctrl_8h.md#a8101b9cd0122a13bc529c774612648d8)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_SPI0\_SS (0x05UL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1599](numaker-m46x-pinctrl_8h.md#ae72c2f69c760f5f453fa72c6d8c1e918)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_UART5\_nRTS (0x06UL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1600](numaker-m46x-pinctrl_8h.md#a2c8667ab970ad270d842bec59311b6e9)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_CCAP\_DATA2 (0x07UL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1601](numaker-m46x-pinctrl_8h.md#a0b29f76443553155d98ec8dac235fc34)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_CAN1\_TXD (0x08UL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1602](numaker-m46x-pinctrl_8h.md#a7f53d4b1779f2507c6f9b27d14669e22)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_TAMPER3 (0x0aUL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

[ 1603](numaker-m46x-pinctrl_8h.md#a0edd6aab0af315a93b4a4cc3fe009e39)#define NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_UART9\_TXD (0x0bUL << NUMAKER\_SYS\_GPF\_MFP2\_PF9MFP\_Pos)

1604

1605/\* PF.10 MFP \*/

[ 1606](numaker-m46x-pinctrl_8h.md#a836a3fa2e28d21e8c5b6c16182a4e1f9)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1607](numaker-m46x-pinctrl_8h.md#aa62126b74182627bfa5ef3cee0bf878b)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_EBI\_ADR15 (0x02UL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1608](numaker-m46x-pinctrl_8h.md#a96fcba156574f09178881fbeb62d65c6)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_SC0\_nCD (0x03UL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1609](numaker-m46x-pinctrl_8h.md#ad3cc53552ec81838b4c2c6a3635a8556)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_I2S0\_BCLK (0x04UL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1610](numaker-m46x-pinctrl_8h.md#a8a5989fe54697443d0eec3f627a24822)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_SPI0\_I2SMCLK (0x05UL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1611](numaker-m46x-pinctrl_8h.md#a1c0d412616aebf3e90aa78aa90811a14)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_UART5\_RXD (0x06UL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1612](numaker-m46x-pinctrl_8h.md#ae7e7904071ae3ef845b1cb5a3be34da0)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_CCAP\_DATA3 (0x07UL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1613](numaker-m46x-pinctrl_8h.md#a7e596662e4883e88c30f562b31001d62)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_CAN3\_RXD (0x08UL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1614](numaker-m46x-pinctrl_8h.md#a7709a4a3851c3292260316366d4d5fbf)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_TAMPER4 (0x0aUL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

[ 1615](numaker-m46x-pinctrl_8h.md#a875d0508648b3b14672a57a9c902debc)#define NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_UART9\_nRTS (0x0bUL << NUMAKER\_SYS\_GPF\_MFP2\_PF10MFP\_Pos)

1616

1617/\* PF.11 MFP \*/

[ 1618](numaker-m46x-pinctrl_8h.md#a11c11afd86a83fed6b183f91906f2d3b)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

[ 1619](numaker-m46x-pinctrl_8h.md#af384c656d4f128d502d9a1e24843f6cc)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_EBI\_ADR14 (0x02UL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

[ 1620](numaker-m46x-pinctrl_8h.md#abba0120d786080a2a1e7986c1b4b18bd)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_SPI2\_MOSI (0x03UL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

[ 1621](numaker-m46x-pinctrl_8h.md#ac28aa3e04a65b95c69fab337514f302e)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_UART5\_TXD (0x06UL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

[ 1622](numaker-m46x-pinctrl_8h.md#a2b0cee60d75d41bac15e23fc9ed26d55)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_CCAP\_DATA4 (0x07UL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

[ 1623](numaker-m46x-pinctrl_8h.md#aeacbeefcbc1d73ab13e73eefd9c18318)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_CAN3\_TXD (0x08UL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

[ 1624](numaker-m46x-pinctrl_8h.md#a3b37286a13ab1ebc0f2b6e0505d5a3a2)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_TAMPER5 (0x0aUL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

[ 1625](numaker-m46x-pinctrl_8h.md#aa44ac591c3197c7f86034105124682d3)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_UART9\_nCTS (0x0bUL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

[ 1626](numaker-m46x-pinctrl_8h.md#a825487fe9b2c4e60de46e274cc416b22)#define NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_TM3 (0x0dUL << NUMAKER\_SYS\_GPF\_MFP2\_PF11MFP\_Pos)

1627

1628/\* PG.0 MFP \*/

[ 1629](numaker-m46x-pinctrl_8h.md#afba749336566e94089be542a2b2c487f)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos)

[ 1630](numaker-m46x-pinctrl_8h.md#a1fbd631852b30e2f6f2d7b942dd79a1d)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_EBI\_ADR8 (0x02UL << NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos)

[ 1631](numaker-m46x-pinctrl_8h.md#a965fcfebde9666a8ca15fd78f24236fe)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_I2C0\_SCL (0x04UL << NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos)

[ 1632](numaker-m46x-pinctrl_8h.md#a5f5573e5a0f4dca4889283c5bdae68f9)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_I2C1\_SMBAL (0x05UL << NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos)

[ 1633](numaker-m46x-pinctrl_8h.md#ae4b429918e64ecbbf5a46df873313036)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_UART2\_RXD (0x06UL << NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos)

[ 1634](numaker-m46x-pinctrl_8h.md#a51afd8490c0716668379c34066b3a27d)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_CAN1\_TXD (0x07UL << NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos)

[ 1635](numaker-m46x-pinctrl_8h.md#ac918846ad69afe3a936a1928ea8ec53c)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_UART1\_TXD (0x08UL << NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos)

[ 1636](numaker-m46x-pinctrl_8h.md#a4a421b1fe42d0ffa48eff3391e5a9047)#define NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_I2C3\_SCL (0x09UL << NUMAKER\_SYS\_GPG\_MFP0\_PG0MFP\_Pos)

1637

1638/\* PG.1 MFP \*/

[ 1639](numaker-m46x-pinctrl_8h.md#a84e8c43bf6d08d88cd86a8577db175b3)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

[ 1640](numaker-m46x-pinctrl_8h.md#a66703f6af9270be2aa2fb7cff23d7d8e)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_EBI\_ADR9 (0x02UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

[ 1641](numaker-m46x-pinctrl_8h.md#addc908f13e8ac0c59544243a159ec1e3)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_SPI2\_I2SMCLK (0x03UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

[ 1642](numaker-m46x-pinctrl_8h.md#a5daca6ca892cb4004af21bdbe2859e8b)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_I2C0\_SDA (0x04UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

[ 1643](numaker-m46x-pinctrl_8h.md#a7ce55fc06c1f0000f1bb6655da3266b5)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_I2C1\_SMBSUS (0x05UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

[ 1644](numaker-m46x-pinctrl_8h.md#a944bbdbc06cec4dd898918ef2e16c1ad)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_UART2\_TXD (0x06UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

[ 1645](numaker-m46x-pinctrl_8h.md#ab4e8559998d024e9c3486c38d4bcd84d)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_CAN1\_RXD (0x07UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

[ 1646](numaker-m46x-pinctrl_8h.md#a7303e0298aabf185bf99b1ec57fc1f8d)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_UART1\_RXD (0x08UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

[ 1647](numaker-m46x-pinctrl_8h.md#ae21deaa2186b264998bd68cbead7f0a3)#define NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_I2C3\_SDA (0x09UL << NUMAKER\_SYS\_GPG\_MFP0\_PG1MFP\_Pos)

1648

1649/\* PG.2 MFP \*/

[ 1650](numaker-m46x-pinctrl_8h.md#ad89cad7ffb3916696b189dd5fc8b6d2f)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos)

[ 1651](numaker-m46x-pinctrl_8h.md#a4bfb076dd7c8100e3969a47c20eea50b)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_EBI\_ADR11 (0x02UL << NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos)

[ 1652](numaker-m46x-pinctrl_8h.md#ad15e7a67d1a5dd32cf10de4fb43345eb)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_SPI2\_SS (0x03UL << NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos)

[ 1653](numaker-m46x-pinctrl_8h.md#a574f7786dd99311ab90f72bdd4f726f4)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_I2C0\_SMBAL (0x04UL << NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos)

[ 1654](numaker-m46x-pinctrl_8h.md#a113360a74d395dedd2aeec744482e6da)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_I2C1\_SCL (0x05UL << NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos)

[ 1655](numaker-m46x-pinctrl_8h.md#ae8e2f1e3ff1e1b153dcccc7b8ac629fa)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_CCAP\_DATA7 (0x07UL << NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos)

[ 1656](numaker-m46x-pinctrl_8h.md#a6bc3b2f615f8b88265d17461ab6e37c9)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_I2C3\_SMBAL (0x09UL << NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos)

[ 1657](numaker-m46x-pinctrl_8h.md#a25546c5fe8dff48deb5d0a2bb59a1987)#define NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_TM0 (0x0dUL << NUMAKER\_SYS\_GPG\_MFP0\_PG2MFP\_Pos)

1658

1659/\* PG.3 MFP \*/

[ 1660](numaker-m46x-pinctrl_8h.md#a5bee5534bd19376d516c8c393d77c75c)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos)

[ 1661](numaker-m46x-pinctrl_8h.md#a963ce54b56a256d13552548747c2539b)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_EBI\_ADR12 (0x02UL << NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos)

[ 1662](numaker-m46x-pinctrl_8h.md#a79176d24a9b7bd3521d8ddf81344fced)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_SPI2\_CLK (0x03UL << NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos)

[ 1663](numaker-m46x-pinctrl_8h.md#a96b8164919fc6a0427212905c2e33ed8)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_I2C0\_SMBSUS (0x04UL << NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos)

[ 1664](numaker-m46x-pinctrl_8h.md#a062e7e8af56b39e519cbe4257fc799f7)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_I2C1\_SDA (0x05UL << NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos)

[ 1665](numaker-m46x-pinctrl_8h.md#a6d39929b92e0ffec497c1bbbd483eef0)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_CCAP\_DATA6 (0x07UL << NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos)

[ 1666](numaker-m46x-pinctrl_8h.md#a8ff4235465257b435f4d0655ab9a68ce)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_I2C3\_SMBSUS (0x09UL << NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos)

[ 1667](numaker-m46x-pinctrl_8h.md#a24cad5c1e27d3c90751f45187d6d284d)#define NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_TM1 (0x0dUL << NUMAKER\_SYS\_GPG\_MFP0\_PG3MFP\_Pos)

1668

1669/\* PG.4 MFP \*/

[ 1670](numaker-m46x-pinctrl_8h.md#a28ce95d1d2e96dc58ecbec2531baed57)#define NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_Pos)

[ 1671](numaker-m46x-pinctrl_8h.md#a3cc2f2ab4db778fb01ba9e79a35ab1ef)#define NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_EBI\_ADR13 (0x02UL << NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_Pos)

[ 1672](numaker-m46x-pinctrl_8h.md#a8490a2e1bedd7539a9e872e7e0d275bf)#define NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_SPI2\_MISO (0x03UL << NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_Pos)

[ 1673](numaker-m46x-pinctrl_8h.md#a2eef18ca839eab957eec3ebdb7050c56)#define NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_CCAP\_DATA5 (0x07UL << NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_Pos)

[ 1674](numaker-m46x-pinctrl_8h.md#a05e73158e6f66d8112aebf7fd8553604)#define NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_TM2 (0x0dUL << NUMAKER\_SYS\_GPG\_MFP1\_PG4MFP\_Pos)

1675

1676/\* PG.5 MFP \*/

[ 1677](numaker-m46x-pinctrl_8h.md#a0ab85087d32f4c5c1a1c33faf6cdf482)#define NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_Pos)

[ 1678](numaker-m46x-pinctrl_8h.md#a17490f91c8f57575b5315edaf466148e)#define NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_EBI\_nCS1 (0x02UL << NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_Pos)

[ 1679](numaker-m46x-pinctrl_8h.md#a909e798295a24dff7bd046d6a8a7629b)#define NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_SPI3\_SS (0x03UL << NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_Pos)

[ 1680](numaker-m46x-pinctrl_8h.md#a8f1fb82d3230b5664bb3e04b4deed0c2)#define NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_SC1\_PWR (0x04UL << NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_Pos)

[ 1681](numaker-m46x-pinctrl_8h.md#a2531da76a8fe99699f0498cafa9985cc)#define NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_I2C3\_SMBAL (0x08UL << NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_Pos)

[ 1682](numaker-m46x-pinctrl_8h.md#ab88ed1c0bf28197c18c3ef70d547ad47)#define NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_I2S1\_MCLK (0x0aUL << NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_Pos)

[ 1683](numaker-m46x-pinctrl_8h.md#a07bb735e26a2762ea40f617d5b39f235)#define NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_EPWM0\_CH3 (0x0bUL << NUMAKER\_SYS\_GPG\_MFP1\_PG5MFP\_Pos)

1684

1685/\* PG.6 MFP \*/

[ 1686](numaker-m46x-pinctrl_8h.md#a00819da3abf5ceb8659df7d6763246c5)#define NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_Pos)

[ 1687](numaker-m46x-pinctrl_8h.md#a425a264238e94d366629d305b655429a)#define NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_EBI\_nCS2 (0x02UL << NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_Pos)

[ 1688](numaker-m46x-pinctrl_8h.md#afc4d0a244635bdd4a608d74b489afd5e)#define NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_SPI3\_CLK (0x03UL << NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_Pos)

[ 1689](numaker-m46x-pinctrl_8h.md#a13ca31c1851c0f4446a2c9dc7ddc6bf7)#define NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_SC1\_RST (0x04UL << NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_Pos)

[ 1690](numaker-m46x-pinctrl_8h.md#aa4d7e3f2decb3ec6f5f0191f943ea5e4)#define NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_I2C3\_SMBSUS (0x08UL << NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_Pos)

[ 1691](numaker-m46x-pinctrl_8h.md#a54a42aacba506f4dc1eba0fefd619517)#define NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_I2S1\_DI (0x0aUL << NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_Pos)

[ 1692](numaker-m46x-pinctrl_8h.md#a76eacc6f8f9d97fd970f98b3f46a242b)#define NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_EPWM0\_CH2 (0x0bUL << NUMAKER\_SYS\_GPG\_MFP1\_PG6MFP\_Pos)

1693

1694/\* PG.7 MFP \*/

[ 1695](numaker-m46x-pinctrl_8h.md#aedbe5fa28b28ddf5c3ed03ce49f767eb)#define NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_Pos)

[ 1696](numaker-m46x-pinctrl_8h.md#afc50bb029328c5d6089a73ac6e46a79c)#define NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_EBI\_nWRL (0x02UL << NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_Pos)

[ 1697](numaker-m46x-pinctrl_8h.md#a75715bdfb776f2b7ef7260dd3ac52402)#define NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_SPI3\_MISO (0x03UL << NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_Pos)

[ 1698](numaker-m46x-pinctrl_8h.md#a20404fa9295a6caebb836f179d69c30a)#define NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_SC1\_DAT (0x04UL << NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_Pos)

[ 1699](numaker-m46x-pinctrl_8h.md#aba9cb6700ebcdac9a75a8ac81ddf39b1)#define NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_I2C3\_SCL (0x08UL << NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_Pos)

[ 1700](numaker-m46x-pinctrl_8h.md#a4832865be6a00b83ff182b9ca62f9847)#define NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_I2S1\_DO (0x0aUL << NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_Pos)

[ 1701](numaker-m46x-pinctrl_8h.md#aa1830173c8b72c5f6203ddbac9558fcc)#define NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_EPWM0\_CH1 (0x0bUL << NUMAKER\_SYS\_GPG\_MFP1\_PG7MFP\_Pos)

1702

1703/\* PG.8 MFP \*/

[ 1704](numaker-m46x-pinctrl_8h.md#af38bb2e4ce2b85d742b387ccdb6f68c5)#define NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_Pos)

[ 1705](numaker-m46x-pinctrl_8h.md#a5061020d0702eb54b4d536d07f0cd34b)#define NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_EBI\_nWRH (0x02UL << NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_Pos)

[ 1706](numaker-m46x-pinctrl_8h.md#a151d436fa512f36cd8b352892ca98277)#define NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_SPI3\_MOSI (0x03UL << NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_Pos)

[ 1707](numaker-m46x-pinctrl_8h.md#a74bfbc202c7cbfd2fa095d854e05c511)#define NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_SC1\_CLK (0x04UL << NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_Pos)

[ 1708](numaker-m46x-pinctrl_8h.md#a04258982028647585a5b1ac385234a9e)#define NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_I2C3\_SDA (0x08UL << NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_Pos)

[ 1709](numaker-m46x-pinctrl_8h.md#a9c6eca14908e19577720345cba134d4d)#define NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_I2S1\_LRCK (0x0aUL << NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_Pos)

[ 1710](numaker-m46x-pinctrl_8h.md#acc7cb16c3b040b21b37c6f60fff1c709)#define NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_EPWM0\_CH0 (0x0bUL << NUMAKER\_SYS\_GPG\_MFP2\_PG8MFP\_Pos)

1711

1712/\* PG.9 MFP \*/

[ 1713](numaker-m46x-pinctrl_8h.md#a2aa5b4b4e0ab7b64ede0df39e9a33f2f)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1714](numaker-m46x-pinctrl_8h.md#a5d0ed5999c6e5f50a124548f176e5b0e)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_EBI\_AD0 (0x02UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1715](numaker-m46x-pinctrl_8h.md#a41df481e385234694adb92d8401132f5)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_SD1\_DAT3 (0x03UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1716](numaker-m46x-pinctrl_8h.md#ab4ae75e7b168a1547a7a1b4a4e2b4482)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_SPIM\_D2 (0x04UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1717](numaker-m46x-pinctrl_8h.md#a5cfef2b5b10621a33d88231f439329cb)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_QSPI1\_MISO1 (0x05UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1718](numaker-m46x-pinctrl_8h.md#ac450d34930c1780aacde6baf09130b56)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_CCAP\_PIXCLK (0x07UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1719](numaker-m46x-pinctrl_8h.md#ac7456ddb7454df5626f6a60d6e995d21)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_I2C4\_SCL (0x08UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1720](numaker-m46x-pinctrl_8h.md#afbdbfe4b541f379e83750b2a67df23ad)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_ECAP2\_IC0 (0x09UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1721](numaker-m46x-pinctrl_8h.md#af5d9117cbd0e0aacdd0272065c280589)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_BPWM0\_CH5 (0x0cUL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1722](numaker-m46x-pinctrl_8h.md#a749c1761fd157e2432711b5a28536aab)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_HBI\_D4 (0x10UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1723](numaker-m46x-pinctrl_8h.md#a77c26596e5268aa62e37fe6ba87e664f)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_SPI8\_SS (0x13UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

[ 1724](numaker-m46x-pinctrl_8h.md#aa41268abfd456d41ea102cef309f7e6d)#define NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_BMC16 (0x14UL << NUMAKER\_SYS\_GPG\_MFP2\_PG9MFP\_Pos)

1725

1726/\* PG.10 MFP \*/

[ 1727](numaker-m46x-pinctrl_8h.md#aa91e82ed07ea7e85f624bacc761e382c)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1728](numaker-m46x-pinctrl_8h.md#aefd8502263a289eb23bbaf69b7733073)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_EBI\_AD1 (0x02UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1729](numaker-m46x-pinctrl_8h.md#a86fe1a54e211cf5a2deeab5cd19709df)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_SD1\_DAT2 (0x03UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1730](numaker-m46x-pinctrl_8h.md#a4c109a868d1087a7b8e216a18712f883)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_SPIM\_D3 (0x04UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1731](numaker-m46x-pinctrl_8h.md#a52a14ff480def2e0894be46342f80753)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_QSPI1\_MOSI1 (0x05UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1732](numaker-m46x-pinctrl_8h.md#ada2b3fe3005a4945ad2ec618e25169a9)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_CCAP\_SCLK (0x07UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1733](numaker-m46x-pinctrl_8h.md#a6b2e7ec3c0af2286cd5aafb4fda6fc18)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_I2C4\_SDA (0x08UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1734](numaker-m46x-pinctrl_8h.md#a2d3fb627ac79b2671da4e936122e1747)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_ECAP2\_IC1 (0x09UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1735](numaker-m46x-pinctrl_8h.md#ad01ffe612304e2105b80eaf50213adce)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_BPWM0\_CH4 (0x0cUL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1736](numaker-m46x-pinctrl_8h.md#af9ec55a441b6b5aec73289792bdaaa9e)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_HBI\_D3 (0x10UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1737](numaker-m46x-pinctrl_8h.md#a8964dca39b2014219c939cb5c78a39be)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_SPI8\_CLK (0x13UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

[ 1738](numaker-m46x-pinctrl_8h.md#a2c25013bd6201f4a9edbc84d6beac925)#define NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_BMC17 (0x14UL << NUMAKER\_SYS\_GPG\_MFP2\_PG10MFP\_Pos)

1739

1740/\* PG.11 MFP \*/

[ 1741](numaker-m46x-pinctrl_8h.md#a731d857c3bde3f17e57b59dfb01c6f97)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1742](numaker-m46x-pinctrl_8h.md#a2d34f2a4aa891ec2cc946f0f3a07f970)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_EBI\_AD2 (0x02UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1743](numaker-m46x-pinctrl_8h.md#a79c2265d6c1dc97deaef847e8df03297)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_SD1\_DAT1 (0x03UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1744](numaker-m46x-pinctrl_8h.md#a9608fbb07f60157457fe01069186493c)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_SPIM\_SS (0x04UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1745](numaker-m46x-pinctrl_8h.md#a5c3d431163e6b5dfad8588c52e0331d9)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_QSPI1\_SS (0x05UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1746](numaker-m46x-pinctrl_8h.md#a3fe5dd420018ca73634794b7779846a5)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_UART7\_TXD (0x06UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1747](numaker-m46x-pinctrl_8h.md#a5344eba07310b0d88256fefcd0cf9d47)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_CCAP\_SFIELD (0x07UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1748](numaker-m46x-pinctrl_8h.md#a690eceab4f0583d1e23b27d98f2b52f4)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_I2C4\_SMBAL (0x08UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1749](numaker-m46x-pinctrl_8h.md#aef6caa4d6cf676eb0535a8bf3aeec7bf)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_ECAP2\_IC2 (0x09UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1750](numaker-m46x-pinctrl_8h.md#ab17e1a68b0bc9edf7eb5ec3841339792)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_BPWM0\_CH3 (0x0cUL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1751](numaker-m46x-pinctrl_8h.md#a17f7bd46ce2db144ebed7e1597d6372c)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_HBI\_D0 (0x10UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1752](numaker-m46x-pinctrl_8h.md#ab50fef3b505cd996a40bee866e1d61cc)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_SPI8\_MOSI (0x13UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

[ 1753](numaker-m46x-pinctrl_8h.md#a78f07a59aabdb69cc6ac19ed2099eacf)#define NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_BMC18 (0x14UL << NUMAKER\_SYS\_GPG\_MFP2\_PG11MFP\_Pos)

1754

1755/\* PG.12 MFP \*/

[ 1756](numaker-m46x-pinctrl_8h.md#a14e5437490f58ccef7ae3705e4e0d1de)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1757](numaker-m46x-pinctrl_8h.md#ae0a2ad5368625c9afdc8b096511b6d5b)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_EBI\_AD3 (0x02UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1758](numaker-m46x-pinctrl_8h.md#aa4ee070919bab310016ec973430029a3)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_SD1\_DAT0 (0x03UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1759](numaker-m46x-pinctrl_8h.md#a38e96df9cf1fd2749d94f890d500ec94)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_SPIM\_CLK (0x04UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1760](numaker-m46x-pinctrl_8h.md#aaaa13e88957ed62eabf5145f6c92ea19)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_QSPI1\_CLK (0x05UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1761](numaker-m46x-pinctrl_8h.md#a36d2ba94983a99f124ab276ccb5bded3)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_UART7\_RXD (0x06UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1762](numaker-m46x-pinctrl_8h.md#a0cfb6925d7a139b1418ded5f8a8f3b39)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_CCAP\_VSYNC (0x07UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1763](numaker-m46x-pinctrl_8h.md#afde10b31915f8426d705f581c8b69b01)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_I2C4\_SMBSUS (0x08UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1764](numaker-m46x-pinctrl_8h.md#acb00b3a223f16d47ff0e6972a095b445)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_BPWM0\_CH2 (0x0cUL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1765](numaker-m46x-pinctrl_8h.md#a4e6e5bfd0b4ecd1545f2a52c5ca1f9b7)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_HBI\_D1 (0x10UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1766](numaker-m46x-pinctrl_8h.md#a49ca6571eb6c60e7c0af60ce2f98340c)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_SPI8\_MISO (0x13UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

[ 1767](numaker-m46x-pinctrl_8h.md#aa3b5eebbf441337a62219a21ac05e039)#define NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_BMC19 (0x14UL << NUMAKER\_SYS\_GPG\_MFP3\_PG12MFP\_Pos)

1768

1769/\* PG.13 MFP \*/

[ 1770](numaker-m46x-pinctrl_8h.md#a1ab5ff4ac5a7f8ff1498291b892c1f8a)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

[ 1771](numaker-m46x-pinctrl_8h.md#a9bea90b6da3ecd4f2ee568429313097d)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_EBI\_AD4 (0x02UL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

[ 1772](numaker-m46x-pinctrl_8h.md#ab9e6a1e486196d26f4703c9531487965)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_SD1\_CMD (0x03UL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

[ 1773](numaker-m46x-pinctrl_8h.md#ad660dfb9f48fd629aac157874aa2d8fd)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_SPIM\_MISO (0x04UL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

[ 1774](numaker-m46x-pinctrl_8h.md#a0ae96f7d44db4f4a4dcd8f5a7ce4556f)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_QSPI1\_MISO0 (0x05UL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

[ 1775](numaker-m46x-pinctrl_8h.md#a34dd50e0b9972cd621ba8b0ce231a1bf)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_UART6\_TXD (0x06UL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

[ 1776](numaker-m46x-pinctrl_8h.md#aec9cfea780da5349448c7523ab29e531)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_CCAP\_HSYNC (0x07UL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

[ 1777](numaker-m46x-pinctrl_8h.md#a81841960fd1ae920eb63a7cca5d4f5b5)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_BPWM0\_CH1 (0x0cUL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

[ 1778](numaker-m46x-pinctrl_8h.md#a208b84def6a9cc24a1297b64ecc9d384)#define NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_HBI\_D5 (0x10UL << NUMAKER\_SYS\_GPG\_MFP3\_PG13MFP\_Pos)

1779

1780/\* PG.14 MFP \*/

[ 1781](numaker-m46x-pinctrl_8h.md#aad45846fc1515ebf5df8fa09ce125025)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos)

[ 1782](numaker-m46x-pinctrl_8h.md#a2f1df2cb8c43e56289ee04863babfd9c)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_EBI\_AD5 (0x02UL << NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos)

[ 1783](numaker-m46x-pinctrl_8h.md#a83c3871991c9a269a35ca5fa6661c944)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_SD1\_CLK (0x03UL << NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos)

[ 1784](numaker-m46x-pinctrl_8h.md#ad6ac43bb38b7a704994a110ff14c2fd2)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_SPIM\_MOSI (0x04UL << NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos)

[ 1785](numaker-m46x-pinctrl_8h.md#a05478d4cda3b427f36c1b3dbe4dbacc8)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_QSPI1\_MOSI0 (0x05UL << NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos)

[ 1786](numaker-m46x-pinctrl_8h.md#ac7468ef185822b2f277e45563f195cd0)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_UART6\_RXD (0x06UL << NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos)

[ 1787](numaker-m46x-pinctrl_8h.md#ab160858054105c5b4e7f3880092e4927)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_BPWM0\_CH0 (0x0cUL << NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos)

[ 1788](numaker-m46x-pinctrl_8h.md#a463bd9fc17688f8eb14699ecec13cc03)#define NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_HBI\_D6 (0x10UL << NUMAKER\_SYS\_GPG\_MFP3\_PG14MFP\_Pos)

1789

1790/\* PG.15 MFP \*/

[ 1791](numaker-m46x-pinctrl_8h.md#a5ac113e978f1f7dcff71cc76a84faad8)#define NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_Pos)

[ 1792](numaker-m46x-pinctrl_8h.md#ad29162f5918481a0aca2b3c337d80b7e)#define NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_SD1\_nCD (0x03UL << NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_Pos)

[ 1793](numaker-m46x-pinctrl_8h.md#ad10e6b848c1a8e54bb86afb44f230724)#define NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_CLKO (0x0eUL << NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_Pos)

[ 1794](numaker-m46x-pinctrl_8h.md#aa35fce4f4e82e483b081556afe2204f0)#define NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_EADC0\_ST (0x0fUL << NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_Pos)

[ 1795](numaker-m46x-pinctrl_8h.md#ac7a08e798bac7847e60c094ebab8f731)#define NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_HBI\_D7 (0x10UL << NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_Pos)

[ 1796](numaker-m46x-pinctrl_8h.md#abb98f6af5642470e63e122323553a542)#define NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_QSPI1\_MISO1 (0x13UL << NUMAKER\_SYS\_GPG\_MFP3\_PG15MFP\_Pos)

1797

1798/\* PH.0 MFP \*/

[ 1799](numaker-m46x-pinctrl_8h.md#a8bbb61f9af008f2158d7fb6294332d93)#define NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_Pos)

[ 1800](numaker-m46x-pinctrl_8h.md#a4ca810d1343c33147147beed84209f24)#define NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_EBI\_ADR7 (0x02UL << NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_Pos)

[ 1801](numaker-m46x-pinctrl_8h.md#a5a6f3d6d458d4edcc63ae9b7eb3647c7)#define NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_UART5\_TXD (0x04UL << NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_Pos)

[ 1802](numaker-m46x-pinctrl_8h.md#a0e3f2e4f8a818f694e95edf27fe899cd)#define NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_TM0\_EXT (0x0dUL << NUMAKER\_SYS\_GPH\_MFP0\_PH0MFP\_Pos)

1803

1804/\* PH.1 MFP \*/

[ 1805](numaker-m46x-pinctrl_8h.md#a462be932f46ccdd898c1fa5a48de8fb4)#define NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_Pos)

[ 1806](numaker-m46x-pinctrl_8h.md#a552ceb0e05fc94b534db9c9b935b1175)#define NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_EBI\_ADR6 (0x02UL << NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_Pos)

[ 1807](numaker-m46x-pinctrl_8h.md#a24526688d3545a46e498e068ca3a9ad2)#define NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_UART5\_RXD (0x04UL << NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_Pos)

[ 1808](numaker-m46x-pinctrl_8h.md#ac022c5c8b84c6ac0ffb1877bd865d545)#define NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_TM1\_EXT (0x0dUL << NUMAKER\_SYS\_GPH\_MFP0\_PH1MFP\_Pos)

1809

1810/\* PH.2 MFP \*/

[ 1811](numaker-m46x-pinctrl_8h.md#a8568cc73ef2f08b3de58a0ac07a9ef81)#define NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_Pos)

[ 1812](numaker-m46x-pinctrl_8h.md#abe6b4a5bb917a35eda00d0528ca064cd)#define NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_EBI\_ADR5 (0x02UL << NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_Pos)

[ 1813](numaker-m46x-pinctrl_8h.md#a579912e78c7b1dc3afcbee2eac682392)#define NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_UART5\_nRTS (0x04UL << NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_Pos)

[ 1814](numaker-m46x-pinctrl_8h.md#aee958fd4d00135008b45e160c3831cab)#define NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_UART4\_TXD (0x05UL << NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_Pos)

[ 1815](numaker-m46x-pinctrl_8h.md#ae12fb3e474bf98365c9bfcb8c9c9a8ca)#define NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_I2C0\_SCL (0x06UL << NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_Pos)

[ 1816](numaker-m46x-pinctrl_8h.md#ab7d81151c033491cc164077823aa4207)#define NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_TM2\_EXT (0x0dUL << NUMAKER\_SYS\_GPH\_MFP0\_PH2MFP\_Pos)

1817

1818/\* PH.3 MFP \*/

[ 1819](numaker-m46x-pinctrl_8h.md#aeecbad3d2006e6270f9047ac15e5e799)#define NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_Pos)

[ 1820](numaker-m46x-pinctrl_8h.md#ae3662462256a7b97d90be912ebff8814)#define NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_EBI\_ADR4 (0x02UL << NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_Pos)

[ 1821](numaker-m46x-pinctrl_8h.md#a1e76a87cb53542234c19288ee3f462be)#define NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_SPI1\_I2SMCLK (0x03UL << NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_Pos)

[ 1822](numaker-m46x-pinctrl_8h.md#a89602fdc90b4b00568f923af91cec86b)#define NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_UART5\_nCTS (0x04UL << NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_Pos)

[ 1823](numaker-m46x-pinctrl_8h.md#a038940099b9666080c6ea87cbd72afad)#define NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_UART4\_RXD (0x05UL << NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_Pos)

[ 1824](numaker-m46x-pinctrl_8h.md#a18ed1727c0e4a81e726c2e4a83d57afa)#define NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_I2C0\_SDA (0x06UL << NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_Pos)

[ 1825](numaker-m46x-pinctrl_8h.md#ab611f171d3107d6745d60120037ed631)#define NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_TM3\_EXT (0x0dUL << NUMAKER\_SYS\_GPH\_MFP0\_PH3MFP\_Pos)

1826

1827/\* PH.4 MFP \*/

[ 1828](numaker-m46x-pinctrl_8h.md#a4dca5e560c420fce060d72167d078683)#define NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_Pos)

[ 1829](numaker-m46x-pinctrl_8h.md#ae9f3b1fa4a92756fa778999cbebd486b)#define NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_EBI\_ADR3 (0x02UL << NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_Pos)

[ 1830](numaker-m46x-pinctrl_8h.md#a5b1644fa6d23221543775a315aa24667)#define NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_SPI1\_MISO (0x03UL << NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_Pos)

[ 1831](numaker-m46x-pinctrl_8h.md#a30fe0971a2d1039cd343783440ad685b)#define NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_UART7\_nRTS (0x04UL << NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_Pos)

[ 1832](numaker-m46x-pinctrl_8h.md#a044892f11cf715f9611a976b15fdf749)#define NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_UART6\_TXD (0x05UL << NUMAKER\_SYS\_GPH\_MFP1\_PH4MFP\_Pos)

1833

1834/\* PH.5 MFP \*/

[ 1835](numaker-m46x-pinctrl_8h.md#aac8e6d10b284b07e743d6ba53593149a)#define NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_Pos)

[ 1836](numaker-m46x-pinctrl_8h.md#ab3af8fe4cd90bca521cbb18c320018d3)#define NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_EBI\_ADR2 (0x02UL << NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_Pos)

[ 1837](numaker-m46x-pinctrl_8h.md#a4c27a9078f2249fbf3cfd3b2ecaf008b)#define NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_SPI1\_MOSI (0x03UL << NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_Pos)

[ 1838](numaker-m46x-pinctrl_8h.md#ad7b0734d572e90a4e0828260a030544d)#define NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_UART7\_nCTS (0x04UL << NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_Pos)

[ 1839](numaker-m46x-pinctrl_8h.md#a8dec04b702e55d0e5b755777640f1db9)#define NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_UART6\_RXD (0x05UL << NUMAKER\_SYS\_GPH\_MFP1\_PH5MFP\_Pos)

1840

1841/\* PH.6 MFP \*/

[ 1842](numaker-m46x-pinctrl_8h.md#aff71de96b8d2ba29a0ed61813d9ae96d)#define NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_Pos)

[ 1843](numaker-m46x-pinctrl_8h.md#a6888e427b8ff90fe7be9abf447036bfd)#define NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_EBI\_ADR1 (0x02UL << NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_Pos)

[ 1844](numaker-m46x-pinctrl_8h.md#af30e0b32ff84e53f83453cf18bd5e64b)#define NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_SPI1\_CLK (0x03UL << NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_Pos)

[ 1845](numaker-m46x-pinctrl_8h.md#acd9f3b84d9ae7f9c70a97d06d006d33d)#define NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_UART7\_TXD (0x04UL << NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_Pos)

[ 1846](numaker-m46x-pinctrl_8h.md#ac81fa0d8304a5d9652a71793c19a172c)#define NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_UART9\_nCTS (0x07UL << NUMAKER\_SYS\_GPH\_MFP1\_PH6MFP\_Pos)

1847

1848/\* PH.7 MFP \*/

[ 1849](numaker-m46x-pinctrl_8h.md#a883ec73e0ad7a4869e9dfa85340675a1)#define NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_Pos)

[ 1850](numaker-m46x-pinctrl_8h.md#a87da067cc1997b1e17d9ddb4c881ff10)#define NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_EBI\_ADR0 (0x02UL << NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_Pos)

[ 1851](numaker-m46x-pinctrl_8h.md#a9b2ba228fe751bcc116e52dbe3348efb)#define NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_SPI1\_SS (0x03UL << NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_Pos)

[ 1852](numaker-m46x-pinctrl_8h.md#a1650f0d8f189310a675b6f3381f97ca0)#define NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_UART7\_RXD (0x04UL << NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_Pos)

[ 1853](numaker-m46x-pinctrl_8h.md#a79b6dcfc47032cce81d4a5f7253d653f)#define NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_UART9\_nRTS (0x07UL << NUMAKER\_SYS\_GPH\_MFP1\_PH7MFP\_Pos)

1854

1855/\* PH.8 MFP \*/

[ 1856](numaker-m46x-pinctrl_8h.md#a94ed0d134be95f9b9e9242772cd4a34a)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1857](numaker-m46x-pinctrl_8h.md#a77621be609f7a3c4940e745571dca05c)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_EBI\_AD12 (0x02UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1858](numaker-m46x-pinctrl_8h.md#aa18916b792015ddecef5bb8b0145b492)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_QSPI0\_CLK (0x03UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1859](numaker-m46x-pinctrl_8h.md#a46043312e4c2117f739b4ce670cf939a)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_SC2\_PWR (0x04UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1860](numaker-m46x-pinctrl_8h.md#ab2feb211fcdce2a22394fab39893d42b)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_I2S0\_DI (0x05UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1861](numaker-m46x-pinctrl_8h.md#ae80ea8fa0ed3b69fdb13dbb8520b1c6c)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_SPI1\_CLK (0x06UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1862](numaker-m46x-pinctrl_8h.md#a58a14b59e1d4a2d1ce65ca71bc481a24)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_UART3\_nRTS (0x07UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1863](numaker-m46x-pinctrl_8h.md#a17f998230e24f01460303f107f989ea7)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_I2C1\_SMBAL (0x08UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1864](numaker-m46x-pinctrl_8h.md#ad1dff461a339f38a544c67610e892017)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_I2C2\_SCL (0x09UL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1865](numaker-m46x-pinctrl_8h.md#a95a6c794dc35c6e3dc5229210f99cc29)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_UART1\_TXD (0x0aUL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

[ 1866](numaker-m46x-pinctrl_8h.md#a002c29c2859dd411427afb44e7900eb4)#define NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_UART9\_nCTS (0x0dUL << NUMAKER\_SYS\_GPH\_MFP2\_PH8MFP\_Pos)

1867

1868/\* PH.9 MFP \*/

[ 1869](numaker-m46x-pinctrl_8h.md#a1c3d16ba3ee71eb5bf7ddd803a2a7e4b)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1870](numaker-m46x-pinctrl_8h.md#ae9e21e4ff31d9ea069e82e30ba58f01d)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_EBI\_AD13 (0x02UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1871](numaker-m46x-pinctrl_8h.md#a9aac97448110e57ac5d07ac23e7b9c37)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_QSPI0\_SS (0x03UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1872](numaker-m46x-pinctrl_8h.md#a52e9ef67b3585253dd5e25e2de3459bc)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_SC2\_RST (0x04UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1873](numaker-m46x-pinctrl_8h.md#a28010fcc998629083741b37d89f260b5)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_I2S0\_DO (0x05UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1874](numaker-m46x-pinctrl_8h.md#a4337628e584646907853750e61ac32f2)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_SPI1\_SS (0x06UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1875](numaker-m46x-pinctrl_8h.md#a98b76f6425742a9dbf4d978cf9a58c4c)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_UART3\_nCTS (0x07UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1876](numaker-m46x-pinctrl_8h.md#a85b4a0ca80e3a679db6393a016b8a470)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_I2C1\_SMBSUS (0x08UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1877](numaker-m46x-pinctrl_8h.md#a41edb51b6ef1e51f2cfd631c5a98cd73)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_I2C2\_SDA (0x09UL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1878](numaker-m46x-pinctrl_8h.md#a1f7dc7ba07dec11e2239b2c16592eaf7)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_UART1\_RXD (0x0aUL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

[ 1879](numaker-m46x-pinctrl_8h.md#ab0a44c29ca59f4475dfb9f8b78c581a3)#define NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_UART9\_nRTS (0x0dUL << NUMAKER\_SYS\_GPH\_MFP2\_PH9MFP\_Pos)

1880

1881/\* PH.10 MFP \*/

[ 1882](numaker-m46x-pinctrl_8h.md#a33ca8d376eb794ddb7bbc46fb0a66b1a)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

[ 1883](numaker-m46x-pinctrl_8h.md#ac675f4fab38c152c1ffcd66b57b0bfbd)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_EBI\_AD14 (0x02UL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

[ 1884](numaker-m46x-pinctrl_8h.md#ae90ac6f26a3e2e6de1fe7ca8e4ba6ba0)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_QSPI0\_MISO1 (0x03UL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

[ 1885](numaker-m46x-pinctrl_8h.md#a12fb762f48e4ce089d8f08315a7de1e7)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_SC2\_nCD (0x04UL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

[ 1886](numaker-m46x-pinctrl_8h.md#ac02a1e6e86de3c4334db346a4c800a2a)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_I2S0\_LRCK (0x05UL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

[ 1887](numaker-m46x-pinctrl_8h.md#a9cc7e7226b64209e0f21e98dd651920f)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_SPI1\_I2SMCLK (0x06UL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

[ 1888](numaker-m46x-pinctrl_8h.md#a4ace76dc16687fc28d0b075b52cae0e7)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_UART4\_TXD (0x07UL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

[ 1889](numaker-m46x-pinctrl_8h.md#a38cb3ed61598b9c97273f87889ef09a3)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_UART0\_TXD (0x08UL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

[ 1890](numaker-m46x-pinctrl_8h.md#a67e7a35967df25f144269b1d5dd64af3)#define NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_UART9\_TXD (0x0dUL << NUMAKER\_SYS\_GPH\_MFP2\_PH10MFP\_Pos)

1891

1892/\* PH.11 MFP \*/

[ 1893](numaker-m46x-pinctrl_8h.md#a3e26a1aec2f1252580d7903a5a4127c5)#define NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_Pos)

[ 1894](numaker-m46x-pinctrl_8h.md#aa1edb80f2d4784c9cd3e00adfdf9fde1)#define NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_EBI\_AD15 (0x02UL << NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_Pos)

[ 1895](numaker-m46x-pinctrl_8h.md#aae49b6790e61b749a441d7287b2a3ece)#define NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_QSPI0\_MOSI1 (0x03UL << NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_Pos)

[ 1896](numaker-m46x-pinctrl_8h.md#aba0a7bbeb28ab0b2f538a6b81e3714d0)#define NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_UART4\_RXD (0x07UL << NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_Pos)

[ 1897](numaker-m46x-pinctrl_8h.md#a7feea31c65a82f04dd6f0dd3ce266145)#define NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_UART0\_RXD (0x08UL << NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_Pos)

[ 1898](numaker-m46x-pinctrl_8h.md#a8ec163ddd736af3374173bdea2950da4)#define NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_EPWM0\_CH5 (0x0bUL << NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_Pos)

[ 1899](numaker-m46x-pinctrl_8h.md#a86c153afc291ad2b088644f5b2ebb897)#define NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_UART9\_RXD (0x0dUL << NUMAKER\_SYS\_GPH\_MFP2\_PH11MFP\_Pos)

1900

1901/\* PH.12 MFP \*/

[ 1902](numaker-m46x-pinctrl_8h.md#ab3488b1742016a77caa7be64d945652f)#define NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_Pos)

[ 1903](numaker-m46x-pinctrl_8h.md#a28d9d1c4ffc95ef2340532a3dc81499f)#define NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_EBI\_AD0 (0x02UL << NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_Pos)

[ 1904](numaker-m46x-pinctrl_8h.md#a89ae94759c932858f97577730f8df1ac)#define NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_UART9\_TXD (0x03UL << NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_Pos)

[ 1905](numaker-m46x-pinctrl_8h.md#a3f2fbc67503fc55c89f120fe69e5d0ed)#define NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_QSPI1\_MISO1 (0x06UL << NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_Pos)

[ 1906](numaker-m46x-pinctrl_8h.md#a59f1092ebb2f79250be1a312b20b5b1e)#define NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_CCAP\_PIXCLK (0x07UL << NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_Pos)

[ 1907](numaker-m46x-pinctrl_8h.md#a5f6e320a396ca0ecae12be2cc71c55e3)#define NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_CAN3\_TXD (0x0aUL << NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_Pos)

[ 1908](numaker-m46x-pinctrl_8h.md#ae2fcd35195e34c0bd86369fb2a3590c4)#define NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_HBI\_nCK (0x10UL << NUMAKER\_SYS\_GPH\_MFP3\_PH12MFP\_Pos)

1909

1910/\* PH.13 MFP \*/

[ 1911](numaker-m46x-pinctrl_8h.md#a41222e35c10c861de36b84f4248d1f31)#define NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_Pos)

[ 1912](numaker-m46x-pinctrl_8h.md#a188ae787983b8cb9dc09deb0ff1c534b)#define NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_EBI\_AD1 (0x02UL << NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_Pos)

[ 1913](numaker-m46x-pinctrl_8h.md#a166a2a0b2530cfbbb8ec5fe46162c95c)#define NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_UART9\_RXD (0x03UL << NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_Pos)

[ 1914](numaker-m46x-pinctrl_8h.md#a571fd13455800719f95cf530ba3f76a4)#define NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_QSPI1\_MOSI1 (0x06UL << NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_Pos)

[ 1915](numaker-m46x-pinctrl_8h.md#a5418e7eca88915a6593adee2bdc4f70d)#define NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_CCAP\_SCLK (0x07UL << NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_Pos)

[ 1916](numaker-m46x-pinctrl_8h.md#ad0320daafd608966b31256d3ebd79f65)#define NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_CAN3\_RXD (0x0aUL << NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_Pos)

[ 1917](numaker-m46x-pinctrl_8h.md#a5f573220f0ec6df0faae44b834eb31cc)#define NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_HBI\_nCS (0x10UL << NUMAKER\_SYS\_GPH\_MFP3\_PH13MFP\_Pos)

1918

1919/\* PH.14 MFP \*/

[ 1920](numaker-m46x-pinctrl_8h.md#a9893d561de8bfe18e87768b5126a2381)#define NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_Pos)

[ 1921](numaker-m46x-pinctrl_8h.md#a6f18fd5fce681cc292e28d8fbb37c884)#define NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_EBI\_AD2 (0x02UL << NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_Pos)

[ 1922](numaker-m46x-pinctrl_8h.md#a8b0cf3eb555e949add852a06a3caad95)#define NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_QSPI1\_SS (0x06UL << NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_Pos)

[ 1923](numaker-m46x-pinctrl_8h.md#a987c7ed2451729688b4697563e74b790)#define NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_CCAP\_SFIELD (0x07UL << NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_Pos)

[ 1924](numaker-m46x-pinctrl_8h.md#abf7db8fe3fd65b951bb394a23e343a7a)#define NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_HBI\_D3 (0x10UL << NUMAKER\_SYS\_GPH\_MFP3\_PH14MFP\_Pos)

1925

1926/\* PH.15 MFP \*/

[ 1927](numaker-m46x-pinctrl_8h.md#a2d27fe6d07bf7c338d616ce09f53ce46)#define NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_Pos)

[ 1928](numaker-m46x-pinctrl_8h.md#a7e1c910155e969884e00b33a65714c96)#define NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_EBI\_AD3 (0x02UL << NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_Pos)

[ 1929](numaker-m46x-pinctrl_8h.md#a65f823c325819f533d8bd22b62e6a5fe)#define NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_QSPI1\_CLK (0x06UL << NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_Pos)

[ 1930](numaker-m46x-pinctrl_8h.md#af2688ecbf1bc2e385e68398d3111fb1d)#define NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_CCAP\_VSYNC (0x07UL << NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_Pos)

[ 1931](numaker-m46x-pinctrl_8h.md#a46ffc66e7f52a560174303b8260b0442)#define NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_HBI\_D2 (0x10UL << NUMAKER\_SYS\_GPH\_MFP3\_PH15MFP\_Pos)

1932

1933/\* PI.6 MFP \*/

[ 1934](numaker-m46x-pinctrl_8h.md#a73247d0d2424888ebcc4b4ce339edd11)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos)

[ 1935](numaker-m46x-pinctrl_8h.md#a15876c039cdf078ae2c927cf9702a279)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_SC1\_nCD (0x05UL << NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos)

[ 1936](numaker-m46x-pinctrl_8h.md#aeb0d3ed762ad1f931fac07a0c184640d)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_I2S0\_BCLK (0x06UL << NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos)

[ 1937](numaker-m46x-pinctrl_8h.md#a904be32eeda373f889d226679f40a7c1)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_SPI1\_I2SMCLK (0x07UL << NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos)

[ 1938](numaker-m46x-pinctrl_8h.md#a29f8aa1b49faae896f4508a515a82073)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_UART2\_TXD (0x08UL << NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos)

[ 1939](numaker-m46x-pinctrl_8h.md#ae5990bba6259fbf473c6335bac034f55)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_I2C1\_SCL (0x09UL << NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos)

[ 1940](numaker-m46x-pinctrl_8h.md#a9810984e5fff0880b676290805beee56)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_CAN3\_TXD (0x0dUL << NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos)

[ 1941](numaker-m46x-pinctrl_8h.md#a7d62c9bb50363de64966ef432d1c3ae0)#define NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_USB\_VBUS\_ST (0x0fUL << NUMAKER\_SYS\_GPI\_MFP1\_PI6MFP\_Pos)

1942

1943/\* PI.7 MFP \*/

[ 1944](numaker-m46x-pinctrl_8h.md#a6e63e5ad4981baa1ff352acf2d7d3516)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos)

[ 1945](numaker-m46x-pinctrl_8h.md#a60ea5844ea6aea5196fb585db7f4a2e1)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_SC1\_PWR (0x05UL << NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos)

[ 1946](numaker-m46x-pinctrl_8h.md#a907e6a4925f335a425daad9bda8f68f9)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_I2S0\_MCLK (0x06UL << NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos)

[ 1947](numaker-m46x-pinctrl_8h.md#a7c03169c6b7cfff8c7d21eb8c46939e1)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_SPI1\_MISO (0x07UL << NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos)

[ 1948](numaker-m46x-pinctrl_8h.md#af9ba8cc976bb8489346df85fa365eedb)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_UART2\_RXD (0x08UL << NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos)

[ 1949](numaker-m46x-pinctrl_8h.md#a04674366f7cd00d44b770c24daca7562)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_I2C1\_SDA (0x09UL << NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos)

[ 1950](numaker-m46x-pinctrl_8h.md#aec2248a8026b05602bed18b15af839b1)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_CAN3\_RXD (0x0dUL << NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos)

[ 1951](numaker-m46x-pinctrl_8h.md#a771e9ed76ae318b0ffa7c537e2c099de)#define NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_USB\_VBUS\_EN (0x0fUL << NUMAKER\_SYS\_GPI\_MFP1\_PI7MFP\_Pos)

1952

1953/\* PI.8 MFP \*/

[ 1954](numaker-m46x-pinctrl_8h.md#ae8beffc90cbd0fe0b97dc1209b922df8)#define NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_Pos)

[ 1955](numaker-m46x-pinctrl_8h.md#afc6cef0e1a40f2d43ca64ec37deae82d)#define NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_SC1\_RST (0x05UL << NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_Pos)

[ 1956](numaker-m46x-pinctrl_8h.md#aa4c4a313599cf78f799ad4ddc25c60b8)#define NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_I2S0\_DI (0x06UL << NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_Pos)

[ 1957](numaker-m46x-pinctrl_8h.md#a2a39ca5c107dd8292bce0b77ce5e2484)#define NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_SPI1\_MOSI (0x07UL << NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_Pos)

[ 1958](numaker-m46x-pinctrl_8h.md#ace8a9066801ab2c4c13a01c7c9bdff02)#define NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_UART2\_nRTS (0x08UL << NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_Pos)

[ 1959](numaker-m46x-pinctrl_8h.md#a67de982ac12b1288228a551ba6613191)#define NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_I2C0\_SMBAL (0x09UL << NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_Pos)

[ 1960](numaker-m46x-pinctrl_8h.md#a425eaf3c44b4e11a6a97f481c59f4a7e)#define NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_CAN2\_TXD (0x0dUL << NUMAKER\_SYS\_GPI\_MFP2\_PI8MFP\_Pos)

1961

1962/\* PI.9 MFP \*/

[ 1963](numaker-m46x-pinctrl_8h.md#a298d10091279134460311eef4de137b8)#define NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_Pos)

[ 1964](numaker-m46x-pinctrl_8h.md#a4285e33e4e0a03200b6d3736162b976b)#define NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_SC1\_DAT (0x05UL << NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_Pos)

[ 1965](numaker-m46x-pinctrl_8h.md#a3d801588d86690097452b1571a99e46a)#define NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_I2S0\_DO (0x06UL << NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_Pos)

[ 1966](numaker-m46x-pinctrl_8h.md#a66989948db847f580840a64a844ad23e)#define NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_SPI1\_CLK (0x07UL << NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_Pos)

[ 1967](numaker-m46x-pinctrl_8h.md#a3de7c5730c9a9ce45f0945790e03e356)#define NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_UART2\_nCTS (0x08UL << NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_Pos)

[ 1968](numaker-m46x-pinctrl_8h.md#ac472297fe8f5e49461731396478caf09)#define NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_I2C0\_SMBSUS (0x09UL << NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_Pos)

[ 1969](numaker-m46x-pinctrl_8h.md#a0466dab9585cdd71cd50d04c12ccc382)#define NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_CAN2\_RXD (0x0dUL << NUMAKER\_SYS\_GPI\_MFP2\_PI9MFP\_Pos)

1970

1971/\* PI.10 MFP \*/

[ 1972](numaker-m46x-pinctrl_8h.md#a40085cc58d9bb2222a005c785ff3109d)#define NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_Pos)

[ 1973](numaker-m46x-pinctrl_8h.md#a31a686ac207a1d6b5f32182d7c8ecfc2)#define NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_SC1\_CLK (0x05UL << NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_Pos)

[ 1974](numaker-m46x-pinctrl_8h.md#a0f40d6d3c8e89ce5edf4bf7761a66894)#define NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_I2S0\_LRCK (0x06UL << NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_Pos)

[ 1975](numaker-m46x-pinctrl_8h.md#ab5bf68a8e65c4e684b03010c18b6e610)#define NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_SPI1\_SS (0x07UL << NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_Pos)

[ 1976](numaker-m46x-pinctrl_8h.md#a6c6bfe63abb2f02f7daea6ddc5bd6681)#define NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_UART2\_TXD (0x08UL << NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_Pos)

[ 1977](numaker-m46x-pinctrl_8h.md#a779fa4cd08e030c76b1af618e1bcaece)#define NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_I2C0\_SCL (0x09UL << NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_Pos)

[ 1978](numaker-m46x-pinctrl_8h.md#ad098ad78c0d123b01d2a05eb5ccd1f32)#define NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_CAN3\_TXD (0x0dUL << NUMAKER\_SYS\_GPI\_MFP2\_PI10MFP\_Pos)

1979

1980/\* PI.11 MFP \*/

[ 1981](numaker-m46x-pinctrl_8h.md#ae0e67272ee8a76945111bbfa3c86e965)#define NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_Pos)

[ 1982](numaker-m46x-pinctrl_8h.md#a3fbf6d949119e70324dd0542512a1316)#define NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_UART2\_RXD (0x08UL << NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_Pos)

[ 1983](numaker-m46x-pinctrl_8h.md#a5c7e1b9fe96f12e12d0a2b4ca91dbc33)#define NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_I2C0\_SDA (0x09UL << NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_Pos)

[ 1984](numaker-m46x-pinctrl_8h.md#a311134bb693f19a43081a28393c85a71)#define NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_CAN3\_RXD (0x0dUL << NUMAKER\_SYS\_GPI\_MFP2\_PI11MFP\_Pos)

1985

1986/\* PI.12 MFP \*/

[ 1987](numaker-m46x-pinctrl_8h.md#abd8ad4a65ea87d93125b6c2efa5d80e6)#define NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_Pos)

[ 1988](numaker-m46x-pinctrl_8h.md#aa58ea84f98fa180940c33981a94a885f)#define NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_SPIM\_SS (0x03UL << NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_Pos)

[ 1989](numaker-m46x-pinctrl_8h.md#a4d4987cba4b357ece52f003179b5fe5e)#define NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_QSPI0\_MISO1 (0x04UL << NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_Pos)

[ 1990](numaker-m46x-pinctrl_8h.md#a296ffa395ba4ead41230b6c80b7c326d)#define NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_CAN0\_TXD (0x0aUL << NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_Pos)

[ 1991](numaker-m46x-pinctrl_8h.md#afca2305cce59439342dc3a86cb42cd51)#define NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_UART4\_TXD (0x0bUL << NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_Pos)

[ 1992](numaker-m46x-pinctrl_8h.md#a8f658ff06dc34b50644e8c4e9037a262)#define NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_EPWM1\_CH0 (0x0cUL << NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_Pos)

[ 1993](numaker-m46x-pinctrl_8h.md#a04f6853b7dd4ae59578b0e9bde994dc3)#define NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_I2C3\_SMBAL (0x0fUL << NUMAKER\_SYS\_GPI\_MFP3\_PI12MFP\_Pos)

1994

1995/\* PI.13 MFP \*/

[ 1996](numaker-m46x-pinctrl_8h.md#a176f66c6c66306e460eb5245e54bab96)#define NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_Pos)

[ 1997](numaker-m46x-pinctrl_8h.md#ae5832a1b18e7b670699916a6a6bfb768)#define NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_SPIM\_MISO (0x03UL << NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_Pos)

[ 1998](numaker-m46x-pinctrl_8h.md#a64a4a04093e9c195862dd8990eb3cfe5)#define NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_QSPI0\_MOSI1 (0x04UL << NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_Pos)

[ 1999](numaker-m46x-pinctrl_8h.md#a0cdd6586b1adb8cf721e3f15d0b68476)#define NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_CAN0\_RXD (0x0aUL << NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_Pos)

[ 2000](numaker-m46x-pinctrl_8h.md#a60571045948caa9cd2a68d98b420289b)#define NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_UART4\_RXD (0x0bUL << NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_Pos)

[ 2001](numaker-m46x-pinctrl_8h.md#a7df684b3e1e3fbcd4a884b68c5df4036)#define NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_EPWM1\_CH1 (0x0cUL << NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_Pos)

[ 2002](numaker-m46x-pinctrl_8h.md#acf0181000eb9aa3d6f9bcbad3ad8c0a7)#define NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_I2C3\_SMBSUS (0x0fUL << NUMAKER\_SYS\_GPI\_MFP3\_PI13MFP\_Pos)

2003

2004/\* PI.14 MFP \*/

[ 2005](numaker-m46x-pinctrl_8h.md#a2786827578dd58d7d8a6e4650ffff4fd)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos)

[ 2006](numaker-m46x-pinctrl_8h.md#a3419e9b5d49fb7663e8082660839adc1)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_SPIM\_D2 (0x03UL << NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos)

[ 2007](numaker-m46x-pinctrl_8h.md#add5ba5cb847d17f077bf703423604a94)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_QSPI0\_SS (0x04UL << NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos)

[ 2008](numaker-m46x-pinctrl_8h.md#a1891489fc0a4bb3c850f63bcd91da45f)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_UART8\_nCTS (0x07UL << NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos)

[ 2009](numaker-m46x-pinctrl_8h.md#a851e1508f1b8db42da08ebc2d3df0d43)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_CAN1\_TXD (0x0aUL << NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos)

[ 2010](numaker-m46x-pinctrl_8h.md#a651b9be4671d8576d17e091a61aa1c73)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_UART3\_TXD (0x0bUL << NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos)

[ 2011](numaker-m46x-pinctrl_8h.md#ae2cc31fc7d8f62b95c0f738fa43e6abe)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_EPWM1\_CH2 (0x0cUL << NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos)

[ 2012](numaker-m46x-pinctrl_8h.md#a6e23add53b5b4f9b2eb6a80ace641e24)#define NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_I2C3\_SCL (0x0fUL << NUMAKER\_SYS\_GPI\_MFP3\_PI14MFP\_Pos)

2013

2014/\* PI.15 MFP \*/

[ 2015](numaker-m46x-pinctrl_8h.md#a28310d2a2b681a77d21d589705fd2a1a)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos)

[ 2016](numaker-m46x-pinctrl_8h.md#a1d62b320694e6bd781ac91bc82ca6d62)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_SPIM\_D3 (0x03UL << NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos)

[ 2017](numaker-m46x-pinctrl_8h.md#abc7ac3f899ccbd5bac8a5d30520884e3)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_QSPI0\_CLK (0x04UL << NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos)

[ 2018](numaker-m46x-pinctrl_8h.md#aa8219cb1930f6e5d88303dd20705ef8e)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_UART8\_nRTS (0x07UL << NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos)

[ 2019](numaker-m46x-pinctrl_8h.md#a2ea81b9caed4af3630d2b206bfc8831a)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_CAN1\_RXD (0x0aUL << NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos)

[ 2020](numaker-m46x-pinctrl_8h.md#a80e31b7624a7fef4a6cca0bb685b47ca)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_UART3\_RXD (0x0bUL << NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos)

[ 2021](numaker-m46x-pinctrl_8h.md#af264e8fd4be6f715942b1be0a1c7f0e5)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_EPWM1\_CH3 (0x0cUL << NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos)

[ 2022](numaker-m46x-pinctrl_8h.md#a83c55f438877ad6c9fb840b874f0338a)#define NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_I2C3\_SDA (0x0fUL << NUMAKER\_SYS\_GPI\_MFP3\_PI15MFP\_Pos)

2023

2024/\* PJ.0 MFP \*/

[ 2025](numaker-m46x-pinctrl_8h.md#af4da87a1cf67758f85dc8e901a54bc18)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_Pos)

[ 2026](numaker-m46x-pinctrl_8h.md#a10627c77c894049d9cd89621e7ebc9e1)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_SPIM\_CLK (0x03UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_Pos)

[ 2027](numaker-m46x-pinctrl_8h.md#ad48d14f67d90f805333c8e6a82fa97c6)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_QSPI0\_MISO0 (0x04UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_Pos)

[ 2028](numaker-m46x-pinctrl_8h.md#ad48a19ac29098f370aeda3552d6b8873)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_UART8\_TXD (0x07UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_Pos)

[ 2029](numaker-m46x-pinctrl_8h.md#a61e775bf9f5e3976f060ff7ac5917bfb)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_CAN2\_TXD (0x0aUL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_Pos)

[ 2030](numaker-m46x-pinctrl_8h.md#acf03e28e1c4caa918660bf66e058a963)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_EPWM1\_CH4 (0x0cUL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ0MFP\_Pos)

2031

2032/\* PJ.1 MFP \*/

[ 2033](numaker-m46x-pinctrl_8h.md#a0010e970774d42d6e99e73b0037985a7)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_Pos)

[ 2034](numaker-m46x-pinctrl_8h.md#a8cf6f73524b8513f762bad3e80d4f083)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_SPIM\_MOSI (0x03UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_Pos)

[ 2035](numaker-m46x-pinctrl_8h.md#aa30be894d53f48b4dd7f097435cf07ad)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_QSPI0\_MOSI0 (0x04UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_Pos)

[ 2036](numaker-m46x-pinctrl_8h.md#a19cf3dae1ed7ba8df6561577c599f650)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_UART8\_RXD (0x07UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_Pos)

[ 2037](numaker-m46x-pinctrl_8h.md#a8f889450caccf9386b992eaa283f9a48)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_CAN2\_RXD (0x0aUL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_Pos)

[ 2038](numaker-m46x-pinctrl_8h.md#a735213f36403f44f2e9c4478430c6603)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_EPWM1\_CH5 (0x0cUL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ1MFP\_Pos)

2039

2040/\* PJ.2 MFP \*/

[ 2041](numaker-m46x-pinctrl_8h.md#a679655667e24251f620d4a55f5f345a9)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_Pos)

[ 2042](numaker-m46x-pinctrl_8h.md#adeef8b37f4d47df95c6c12395418401a)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_EBI\_AD5 (0x02UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_Pos)

[ 2043](numaker-m46x-pinctrl_8h.md#a85a4bda8d4d1c667e05a2432c1263231)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_UART8\_nCTS (0x03UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_Pos)

[ 2044](numaker-m46x-pinctrl_8h.md#aec0ff1bb8c69e062cd4bc3274acad83d)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_QSPI1\_SS (0x06UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_Pos)

[ 2045](numaker-m46x-pinctrl_8h.md#a1ca4ccf92833c323a15c55c489128191)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_CCAP\_DATA5 (0x07UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_Pos)

[ 2046](numaker-m46x-pinctrl_8h.md#a8112f508a307374011008ba6fed95fc8)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_CAN0\_TXD (0x0aUL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_Pos)

[ 2047](numaker-m46x-pinctrl_8h.md#a316f125b8a2b955c761ef12a9e427eaf)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_HBI\_RWDS (0x10UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ2MFP\_Pos)

2048

2049/\* PJ.3 MFP \*/

[ 2050](numaker-m46x-pinctrl_8h.md#a3e712e899ac18963838780cb3b9136d8)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_Pos)

[ 2051](numaker-m46x-pinctrl_8h.md#a4528102cc685dc793d1faead4ee9eb15)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_EBI\_AD4 (0x02UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_Pos)

[ 2052](numaker-m46x-pinctrl_8h.md#adc51701d01fae132ff8bd82b100b2877)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_UART8\_nRTS (0x03UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_Pos)

[ 2053](numaker-m46x-pinctrl_8h.md#a091af3ac07cbc83939986f15521254b8)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_QSPI1\_CLK (0x06UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_Pos)

[ 2054](numaker-m46x-pinctrl_8h.md#aaac933db83ff7d3d2be8582646409c1c)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_CCAP\_DATA4 (0x07UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_Pos)

[ 2055](numaker-m46x-pinctrl_8h.md#a5a9d7ae2b7f7d64a4436a09bd6c5330f)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_CAN0\_RXD (0x0aUL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_Pos)

[ 2056](numaker-m46x-pinctrl_8h.md#a80c38aa05b910cf78b5ea1bc062f488a)#define NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_HBI\_D7 (0x10UL << NUMAKER\_SYS\_GPJ\_MFP0\_PJ3MFP\_Pos)

2057

2058/\* PJ.4 MFP \*/

[ 2059](numaker-m46x-pinctrl_8h.md#a758d1ed19e789f7de0c2a930c506f5b9)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_Pos)

[ 2060](numaker-m46x-pinctrl_8h.md#a59eb20772e4e2ec93d8e1ac389a46096)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_EBI\_AD3 (0x02UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_Pos)

[ 2061](numaker-m46x-pinctrl_8h.md#a12ccf391ab3baacee4289fff28f44edc)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_UART8\_TXD (0x03UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_Pos)

[ 2062](numaker-m46x-pinctrl_8h.md#a9da99e86641ceef76f73fe18daf9c579)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_QSPI1\_MISO0 (0x06UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_Pos)

[ 2063](numaker-m46x-pinctrl_8h.md#a77d053fec738a27fd24a21fd4c08876a)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_CCAP\_DATA3 (0x07UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_Pos)

[ 2064](numaker-m46x-pinctrl_8h.md#a4454c0f9ae8807a35569cecae3787756)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_CAN1\_TXD (0x0aUL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_Pos)

[ 2065](numaker-m46x-pinctrl_8h.md#aacbe2528ea8df0e41be3a91838b77ea0)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_HBI\_D6 (0x10UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ4MFP\_Pos)

2066

2067/\* PJ.5 MFP \*/

[ 2068](numaker-m46x-pinctrl_8h.md#acc2c45fe4ef941774ea742019a71d75e)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_Pos)

[ 2069](numaker-m46x-pinctrl_8h.md#a68f8d4868b9da576e72221fe7c9dc6a0)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_EBI\_AD2 (0x02UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_Pos)

[ 2070](numaker-m46x-pinctrl_8h.md#adfd30dda0140bc7ca6f59ebc56ffc317)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_UART8\_RXD (0x03UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_Pos)

[ 2071](numaker-m46x-pinctrl_8h.md#ab05c8ac7222b0565c5fa6559d61bc844)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_QSPI1\_MOSI0 (0x06UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_Pos)

[ 2072](numaker-m46x-pinctrl_8h.md#a1ef146b48406f63afa3b9a223d362f32)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_CCAP\_DATA2 (0x07UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_Pos)

[ 2073](numaker-m46x-pinctrl_8h.md#a805226dff9a003188ba8dc6ebae29107)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_CAN1\_RXD (0x0aUL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_Pos)

[ 2074](numaker-m46x-pinctrl_8h.md#ae980fc45b49958b6b2c4e1e5b45c2a15)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_HBI\_D5 (0x10UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ5MFP\_Pos)

2075

2076/\* PJ.6 MFP \*/

[ 2077](numaker-m46x-pinctrl_8h.md#af830ebf0f803ee1980f402f726fe7750)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_Pos)

[ 2078](numaker-m46x-pinctrl_8h.md#a359212704531312f4dbbc30397382261)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_EBI\_AD1 (0x02UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_Pos)

[ 2079](numaker-m46x-pinctrl_8h.md#a38b2f9d43912706cd01c0cf33b495da9)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_UART9\_nCTS (0x03UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_Pos)

[ 2080](numaker-m46x-pinctrl_8h.md#a167a71eaa05d5c56f3162242699a0605)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_CCAP\_DATA1 (0x07UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_Pos)

[ 2081](numaker-m46x-pinctrl_8h.md#a088fdcfebd874a7e195dc0f83717419a)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_CAN2\_TXD (0x0aUL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_Pos)

[ 2082](numaker-m46x-pinctrl_8h.md#a232998c4af32dbaa401042044e025570)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_HBI\_D4 (0x10UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ6MFP\_Pos)

2083

2084/\* PJ.7 MFP \*/

[ 2085](numaker-m46x-pinctrl_8h.md#af0b623cd1b2e7aa89960e89738ff5f2f)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_Pos)

[ 2086](numaker-m46x-pinctrl_8h.md#a91af7363aad5879d84a59bca761c631c)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_EBI\_AD0 (0x02UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_Pos)

[ 2087](numaker-m46x-pinctrl_8h.md#a68ecf44e473d16ae7d89f074bfbf5021)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_UART9\_nRTS (0x03UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_Pos)

[ 2088](numaker-m46x-pinctrl_8h.md#a66e9d851d004f0f4741cd9e7de45bdcf)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_CCAP\_DATA0 (0x07UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_Pos)

[ 2089](numaker-m46x-pinctrl_8h.md#a2360c9ce776e169d62085c2abfc0e100)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_CAN2\_RXD (0x0aUL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_Pos)

[ 2090](numaker-m46x-pinctrl_8h.md#a03edf53b7d1e8ffd284861e97eca22cf)#define NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_HBI\_CK (0x10UL << NUMAKER\_SYS\_GPJ\_MFP1\_PJ7MFP\_Pos)

2091

2092/\* PJ.8 MFP \*/

[ 2093](numaker-m46x-pinctrl_8h.md#a33657588127045d7b969d3b7db25d143)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_Pos)

[ 2094](numaker-m46x-pinctrl_8h.md#af7e1557a26fe5d15c77ef2ed82b24e19)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_EBI\_nRD (0x02UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_Pos)

[ 2095](numaker-m46x-pinctrl_8h.md#a018dc1b5016865773602c4fc06785130)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_SD1\_DAT3 (0x03UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_Pos)

[ 2096](numaker-m46x-pinctrl_8h.md#a341bea0d6d402cc45bcfabb8a133da3f)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_SPIM\_SS (0x04UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_Pos)

[ 2097](numaker-m46x-pinctrl_8h.md#a18974cadae1f47efa7d1a45dbd6f1d11)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_UART7\_TXD (0x06UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_Pos)

[ 2098](numaker-m46x-pinctrl_8h.md#aed1cab60b3bebd0ad7dda2d6b7b419f1)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_CAN2\_TXD (0x0bUL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_Pos)

[ 2099](numaker-m46x-pinctrl_8h.md#a8dd679fc4420280c9bc05f8f991334af)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_BPWM0\_CH5 (0x0cUL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ8MFP\_Pos)

2100

2101/\* PJ.9 MFP \*/

[ 2102](numaker-m46x-pinctrl_8h.md#a11980e525c7f4447a465f21eb48724bd)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_Pos)

[ 2103](numaker-m46x-pinctrl_8h.md#a0b8b1abeac385c2d0a5573b870c6d533)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_EBI\_nWR (0x02UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_Pos)

[ 2104](numaker-m46x-pinctrl_8h.md#aa4bcaa23785f1a4253faf14e2e9d1129)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_SD1\_DAT2 (0x03UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_Pos)

[ 2105](numaker-m46x-pinctrl_8h.md#a499dd2559c844941a453d97e7160ab0e)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_SPIM\_MISO (0x04UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_Pos)

[ 2106](numaker-m46x-pinctrl_8h.md#ac75e25ef9f268b110c5d9962742018d5)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_UART7\_RXD (0x06UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_Pos)

[ 2107](numaker-m46x-pinctrl_8h.md#adc082d9255f1600cb2c8738c31cc2ff2)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_CAN2\_RXD (0x0bUL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_Pos)

[ 2108](numaker-m46x-pinctrl_8h.md#a56dd97306d989c5083ccbe4b92970daa)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_BPWM0\_CH4 (0x0cUL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ9MFP\_Pos)

2109

2110/\* PJ.10 MFP \*/

[ 2111](numaker-m46x-pinctrl_8h.md#a5b86e72714ed001c06678af7417cc997)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

[ 2112](numaker-m46x-pinctrl_8h.md#a52d0dc52a29fe7ec3fa97467a6f94bfa)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_EBI\_MCLK (0x02UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

[ 2113](numaker-m46x-pinctrl_8h.md#a360a8602906d50fd0bb959860182e8c7)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_SD1\_DAT1 (0x03UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

[ 2114](numaker-m46x-pinctrl_8h.md#ac67049740211970d9578cce453e6770d)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_SPIM\_D2 (0x04UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

[ 2115](numaker-m46x-pinctrl_8h.md#a96467c58113827ae72b32be95c34b477)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_UART6\_TXD (0x06UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

[ 2116](numaker-m46x-pinctrl_8h.md#ad2bf3c10b5b49d5b96d14e32a74db2a1)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_I2C4\_SCL (0x08UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

[ 2117](numaker-m46x-pinctrl_8h.md#adeaaf539ed37a1ab4522d30f382e91cb)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_ECAP2\_IC0 (0x09UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

[ 2118](numaker-m46x-pinctrl_8h.md#a83de8476a0e9f0fea9a3f75017e6ece1)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_CAN0\_TXD (0x0bUL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

[ 2119](numaker-m46x-pinctrl_8h.md#a6b6932f92fa9490a00faa203958ed2bf)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_BPWM0\_CH3 (0x0cUL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ10MFP\_Pos)

2120

2121/\* PJ.11 MFP \*/

[ 2122](numaker-m46x-pinctrl_8h.md#a9875fbe3faa6338d3e834fca882fc8d5)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

[ 2123](numaker-m46x-pinctrl_8h.md#af4f8560dae18ab7bb85a5ae1a48db6c8)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_EBI\_ALE (0x02UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

[ 2124](numaker-m46x-pinctrl_8h.md#ae1d973ec34e888810ba4e99bfa4cb594)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_SD1\_DAT0 (0x03UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

[ 2125](numaker-m46x-pinctrl_8h.md#aabf0f96204b5913f18d5f2f3f37a9e50)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_SPIM\_D3 (0x04UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

[ 2126](numaker-m46x-pinctrl_8h.md#a3cd1a118e5256102c382264d94fbb3a1)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_UART6\_RXD (0x06UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

[ 2127](numaker-m46x-pinctrl_8h.md#ab34136091eb24fae56829021368028f2)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_I2C4\_SDA (0x08UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

[ 2128](numaker-m46x-pinctrl_8h.md#a161781960a46c52d7abd76aa31c1ff96)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_ECAP2\_IC1 (0x09UL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

[ 2129](numaker-m46x-pinctrl_8h.md#a7b966205000e51b4bea773847c6d54ac)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_CAN0\_RXD (0x0bUL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

[ 2130](numaker-m46x-pinctrl_8h.md#a1f815117828ba636470aea30cc1e946b)#define NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_BPWM0\_CH2 (0x0cUL << NUMAKER\_SYS\_GPJ\_MFP2\_PJ11MFP\_Pos)

2131

2132/\* PJ.12 MFP \*/

[ 2133](numaker-m46x-pinctrl_8h.md#a2126ce63d99ed113949a90689e43dbf6)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

[ 2134](numaker-m46x-pinctrl_8h.md#a938361384fa77932f79e332abf2d325a)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_EBI\_nCS0 (0x02UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

[ 2135](numaker-m46x-pinctrl_8h.md#a0e38250fc56e2cd6b0581b48763c8c82)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_SD1\_CMD (0x03UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

[ 2136](numaker-m46x-pinctrl_8h.md#aedf0666adf4ba582201456619a471060)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_SPIM\_CLK (0x04UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

[ 2137](numaker-m46x-pinctrl_8h.md#a782a7813686f381a2001a51625af3c95)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_I2C4\_SMBAL (0x08UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

[ 2138](numaker-m46x-pinctrl_8h.md#a06585a7e5de4cb11df0350cd7172fa2e)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_ECAP2\_IC2 (0x09UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

[ 2139](numaker-m46x-pinctrl_8h.md#aa11fc046a34a940c4d61af1797d8d32e)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_CAN1\_TXD (0x0bUL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

[ 2140](numaker-m46x-pinctrl_8h.md#a297574ae8013f19c74909ea0038112e2)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_BPWM0\_CH1 (0x0cUL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

[ 2141](numaker-m46x-pinctrl_8h.md#a23da6b62b89289f1998e2794ddb969d0)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_HSUSB\_VBUS\_ST (0x0fUL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ12MFP\_Pos)

2142

2143/\* PJ.13 MFP \*/

[ 2144](numaker-m46x-pinctrl_8h.md#ae2449f0fbdd47d1159fd13af4886e4d3)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_GPIO (0x00UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_Pos)

[ 2145](numaker-m46x-pinctrl_8h.md#aebe226490c81c29c6a28a66adcdaa749)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_SD1\_CLK (0x03UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_Pos)

[ 2146](numaker-m46x-pinctrl_8h.md#ad3bd3dafef5bf896ec25ba2aaa9fa3fc)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_SPIM\_MOSI (0x04UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_Pos)

[ 2147](numaker-m46x-pinctrl_8h.md#a2d6cc69ba24d2e67cbbc8ad0acf9b52d)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_I2C4\_SMBSUS (0x08UL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_Pos)

[ 2148](numaker-m46x-pinctrl_8h.md#a8ac4fdb4d1522ec49011204efd45c305)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_CAN1\_RXD (0x0bUL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_Pos)

[ 2149](numaker-m46x-pinctrl_8h.md#ada2345a2126b3560b8432f5762ff4b03)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_BPWM0\_CH0 (0x0cUL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_Pos)

[ 2150](numaker-m46x-pinctrl_8h.md#aef4a790c5324ebe52bfcf854e430a6c8)#define NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_HSUSB\_VBUS\_EN (0x0fUL << NUMAKER\_SYS\_GPJ\_MFP3\_PJ13MFP\_Pos)

2151

2152/\* End of M460 BSP sys.h pin-mux module copy \*/

2153

2154#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [numaker-m46x-pinctrl.h](numaker-m46x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
