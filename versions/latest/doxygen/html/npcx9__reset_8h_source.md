---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/npcx9__reset_8h_source.html
original_path: doxygen/html/npcx9__reset_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcx9\_reset.h

[Go to the documentation of this file.](npcx9__reset_8h.md)

1/\*

2 \* Copyright (c) 2024 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_NPCX9\_RESET\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_NPCX9\_RESET\_H

9

[ 10](npcx9__reset_8h.md#a81f99303ed0a77ab0256f329def64dc0)#define NPCX\_RESET\_SWRST\_CTL1\_OFFSET 0

[ 11](npcx9__reset_8h.md#ade6e0a94c31cafc3eba6a7ae756bd415)#define NPCX\_RESET\_SWRST\_CTL2\_OFFSET 32

[ 12](npcx9__reset_8h.md#aa35a977186857d86835b66b28cb18398)#define NPCX\_RESET\_SWRST\_CTL3\_OFFSET 64

[ 13](npcx9__reset_8h.md#ad8d8645ad85b3afbc6f20db1396af64f)#define NPCX\_RESET\_SWRST\_CTL4\_OFFSET 96

14

[ 15](npcx9__reset_8h.md#a72fb56274a33e9cff09ab06d5423bed4)#define NPCX\_RESET\_GPIO0 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 0)

[ 16](npcx9__reset_8h.md#a52f3e5746d3a7bd36093de688d675b11)#define NPCX\_RESET\_GPIO1 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 1)

[ 17](npcx9__reset_8h.md#a85d59ac73b5bd58cbcd9cdd22f249930)#define NPCX\_RESET\_GPIO2 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 2)

[ 18](npcx9__reset_8h.md#ad37b02bc378a921ee1417ab34f7729a8)#define NPCX\_RESET\_GPIO3 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 3)

[ 19](npcx9__reset_8h.md#ae1a0e238df6a7b00a838d5fd06eb0122)#define NPCX\_RESET\_GPIO4 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 4)

[ 20](npcx9__reset_8h.md#aae315e45c7f74c5dd7ce0fef9d7d5bf0)#define NPCX\_RESET\_GPIO5 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 5)

[ 21](npcx9__reset_8h.md#a81b885d48bd16f069ad517eb0dab9dce)#define NPCX\_RESET\_GPIO6 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 6)

[ 22](npcx9__reset_8h.md#ad4ccfafdb862152b82dc3553e04a4cbb)#define NPCX\_RESET\_GPIO7 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 7)

[ 23](npcx9__reset_8h.md#a773bf3ad4d732de3c8a06527c7fca16b)#define NPCX\_RESET\_GPIO8 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 8)

[ 24](npcx9__reset_8h.md#ae7e14072ebcc3b112a31a4e7754bdafb)#define NPCX\_RESET\_GPIO9 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 9)

[ 25](npcx9__reset_8h.md#a4b0e5c4c30d117db298fd373b968f488)#define NPCX\_RESET\_GPIOA (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 10)

[ 26](npcx9__reset_8h.md#acf300d105c09ece32ff935e44f220ead)#define NPCX\_RESET\_GPIOB (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 11)

[ 27](npcx9__reset_8h.md#ac7abe8044520a99f8119a661bde3b5ed)#define NPCX\_RESET\_GPIOC (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 12)

[ 28](npcx9__reset_8h.md#aa3f774deebd1e94aca602f0586541e02)#define NPCX\_RESET\_GPIOD (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 13)

[ 29](npcx9__reset_8h.md#a4e1768f6f61654023f6383d9574aefd3)#define NPCX\_RESET\_GPIOE (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 14)

[ 30](npcx9__reset_8h.md#a490f13f39c29725894f91b1d12ab45b0)#define NPCX\_RESET\_GPIOF (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 15)

[ 31](npcx9__reset_8h.md#ac6da7a24b6672ce712c92cc5c9f5bbf8)#define NPCX\_RESET\_ITIM64 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 16)

[ 32](npcx9__reset_8h.md#a3fe5617a1dc9ac1958440213db3e5112)#define NPCX\_RESET\_ITIM32\_1 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 18)

[ 33](npcx9__reset_8h.md#ac44d5cdb5520fdfad96277e06d2d2dc7)#define NPCX\_RESET\_ITIM32\_2 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 19)

[ 34](npcx9__reset_8h.md#a12ef9e0eec9babc31971bea89b98bfa9)#define NPCX\_RESET\_ITIM32\_3 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 20)

[ 35](npcx9__reset_8h.md#adcc596fd448271982cce3f973545fd28)#define NPCX\_RESET\_ITIM32\_4 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 21)

[ 36](npcx9__reset_8h.md#a2dae7e23a8fba87e9935ffd40abe8d67)#define NPCX\_RESET\_ITIM32\_5 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 22)

[ 37](npcx9__reset_8h.md#a790348a62bb6f6659c969fe3386ba0c1)#define NPCX\_RESET\_ITIM32\_6 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 23)

[ 38](npcx9__reset_8h.md#aba5bb6ccc52bd1560822abb80a8fae49)#define NPCX\_RESET\_MTC (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 25)

[ 39](npcx9__reset_8h.md#af90deca338a25205bd19d2c80948f995)#define NPCX\_RESET\_MIWU0 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 26)

[ 40](npcx9__reset_8h.md#ab929e4dd3c03e65c86daf96210fa3838)#define NPCX\_RESET\_MIWU1 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 27)

[ 41](npcx9__reset_8h.md#ad1abd875719ae3bd9068b3269ff1febd)#define NPCX\_RESET\_MIWU2 (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 28)

[ 42](npcx9__reset_8h.md#a68541cbf091be9bb951d08695f01e0e1)#define NPCX\_RESET\_GDMA (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 29)

[ 43](npcx9__reset_8h.md#a8d0240b100a548ffdf6ba1a8b08ecfd2)#define NPCX\_RESET\_FIU (NPCX\_RESET\_SWRST\_CTL1\_OFFSET + 30)

44

[ 45](npcx9__reset_8h.md#a0be538fff0e589732b0c41f53ded10d6)#define NPCX\_RESET\_PMC (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 0)

[ 46](npcx9__reset_8h.md#aa41c81fd03e6c85ad468b060e70f8922)#define NPCX\_RESET\_SHI (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 2)

[ 47](npcx9__reset_8h.md#ae7a0b89c14bf40489c6890648de653dd)#define NPCX\_RESET\_SPIP (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 3)

[ 48](npcx9__reset_8h.md#a3570245c4c2ef9b048752e3edec42d8a)#define NPCX\_RESET\_PECI (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 5)

[ 49](npcx9__reset_8h.md#abcb39166e1d3e1325eb613f6def6f2fb)#define NPCX\_RESET\_CRUART2 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 6)

[ 50](npcx9__reset_8h.md#a73d09627ceb961b9e1153c2d77d5b5a4)#define NPCX\_RESET\_ADC (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 7)

[ 51](npcx9__reset_8h.md#a32c7de2186f89637edbf5f1693f85a5f)#define NPCX\_RESET\_SMB0 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 8)

[ 52](npcx9__reset_8h.md#a08bffb7ef7ecbd442048510b84cecf4b)#define NPCX\_RESET\_SMB1 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 9)

[ 53](npcx9__reset_8h.md#a512ac512d495628e6ba5536d81c10853)#define NPCX\_RESET\_SMB2 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 10)

[ 54](npcx9__reset_8h.md#ae7fdb811a0e332b57a3908c0439e3cf8)#define NPCX\_RESET\_SMB3 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 11)

[ 55](npcx9__reset_8h.md#a683f673ada07bf129b0b1d400a68dd17)#define NPCX\_RESET\_SMB4 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 12)

[ 56](npcx9__reset_8h.md#a203fcf319d24922b7d7e2b03b05ca355)#define NPCX\_RESET\_SMB5 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 13)

[ 57](npcx9__reset_8h.md#aead329ad433b7e977c89a054871b9ecf)#define NPCX\_RESET\_SMB6 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 14)

[ 58](npcx9__reset_8h.md#af278613275cbfc1aca870bc79cf663bb)#define NPCX\_RESET\_TWD (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 15)

[ 59](npcx9__reset_8h.md#a864e660a6904a5767340f759421832a6)#define NPCX\_RESET\_PWM0 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 16)

[ 60](npcx9__reset_8h.md#a0c88eff2699d437b12c1625f5043e588)#define NPCX\_RESET\_PWM1 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 17)

[ 61](npcx9__reset_8h.md#aefdc374f7e767763a1f851d58bce0816)#define NPCX\_RESET\_PWM2 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 18)

[ 62](npcx9__reset_8h.md#a4c1cddadce85ff79667e88a3a40ac548)#define NPCX\_RESET\_PWM3 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 19)

[ 63](npcx9__reset_8h.md#a19546720c7e51f472f74c8974f284d24)#define NPCX\_RESET\_PWM4 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 20)

[ 64](npcx9__reset_8h.md#a70b5a48b35e817f43a2add018c4bd20d)#define NPCX\_RESET\_PWM5 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 21)

[ 65](npcx9__reset_8h.md#ac75e76755957375a207d13d3725841b8)#define NPCX\_RESET\_PWM6 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 22)

[ 66](npcx9__reset_8h.md#a10f7cbfd0fc8a70c6a6cfa9a4bde2ecd)#define NPCX\_RESET\_PWM7 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 23)

[ 67](npcx9__reset_8h.md#a42a7c383914f69df8fb7aea0ca7c4b52)#define NPCX\_RESET\_MFT16\_1 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 24)

[ 68](npcx9__reset_8h.md#a2ce51edd20f4189900086416481bd3ff)#define NPCX\_RESET\_MFT16\_2 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 25)

[ 69](npcx9__reset_8h.md#a2b59b5781233b173031f8e3499c71101)#define NPCX\_RESET\_MFT16\_3 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 26)

[ 70](npcx9__reset_8h.md#a6fb388898107ceb8c59752e232e0e60e)#define NPCX\_RESET\_SMB7 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 27)

[ 71](npcx9__reset_8h.md#a1346e2104546d8b38cb79f4edd05fa1e)#define NPCX\_RESET\_CRUART1 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 28)

[ 72](npcx9__reset_8h.md#afe481ba45d061dd1d9a367e9d827e0aa)#define NPCX\_RESET\_PS2 (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 29)

[ 73](npcx9__reset_8h.md#a6ad3981c88eec0370e7977a6599dad75)#define NPCX\_RESET\_SDP (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 30)

[ 74](npcx9__reset_8h.md#aed372243bc063fd677df36fc7afb5470)#define NPCX\_RESET\_KBS (NPCX\_RESET\_SWRST\_CTL2\_OFFSET + 31)

75

[ 76](npcx9__reset_8h.md#ad883ccf60ae497034fa3b4ee8f0e2c0d)#define NPCX\_RESET\_SIOCFG (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 0)

[ 77](npcx9__reset_8h.md#a21a34b8d9f9bae378ded2af91e79cda8)#define NPCX\_RESET\_SERPORT (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 1)

[ 78](npcx9__reset_8h.md#ab4de3c5f08f3593b15dda6fb829621a2)#define NPCX\_RESET\_I3C (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 5)

[ 79](npcx9__reset_8h.md#a106e92b1dba738c457e3a7cfaff66874)#define NPCX\_RESET\_MSWC (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 8)

[ 80](npcx9__reset_8h.md#affb31b8183b8a0757cf9efd37ec22c29)#define NPCX\_RESET\_SHM (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 9)

[ 81](npcx9__reset_8h.md#a5ec2d6472107f931a40d71a3ef475f6a)#define NPCX\_RESET\_PMCH1 (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 10)

[ 82](npcx9__reset_8h.md#a47a04e729b12f398fa72f2c0bf9e3199)#define NPCX\_RESET\_PMCH2 (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 11)

[ 83](npcx9__reset_8h.md#a674e9c8df444e64751c8e427b5d83f6d)#define NPCX\_RESET\_PMCH3 (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 12)

[ 84](npcx9__reset_8h.md#aae912fd01a20d16fbbbb2a7afb3ccbcb)#define NPCX\_RESET\_PMCH4 (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 13)

[ 85](npcx9__reset_8h.md#af048869b54e84f87f9da15a5c7cc4018)#define NPCX\_RESET\_KBC (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 15)

[ 86](npcx9__reset_8h.md#a5c002638cac08f8c4dafeaffe9d14374)#define NPCX\_RESET\_C2HOST (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 16)

[ 87](npcx9__reset_8h.md#a5016e0c4fbf67b089bcd5084b79b516c)#define NPCX\_RESET\_CRUART3 (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 18)

[ 88](npcx9__reset_8h.md#a20f7fc489aad2a68b1cd3e8828a6277c)#define NPCX\_RESET\_CRUART4 (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 19)

[ 89](npcx9__reset_8h.md#a4e6b20cd682f2e213bd880e35f278596)#define NPCX\_RESET\_LFCG (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 20)

[ 90](npcx9__reset_8h.md#aad039116d3e8eeb7643f53eddfebd01a)#define NPCX\_RESET\_DEV (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 22)

[ 91](npcx9__reset_8h.md#a5a690a8277146999bc33e7cdb3425975)#define NPCX\_RESET\_SYSCFG (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 23)

[ 92](npcx9__reset_8h.md#a27c63907f4d53918dc5e06e957ce8654)#define NPCX\_RESET\_SBY (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 24)

[ 93](npcx9__reset_8h.md#a0becfe5b43cfa5b8bfe682d25dd6bd71)#define NPCX\_RESET\_BBRAM (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 25)

[ 94](npcx9__reset_8h.md#ad5dd9eb0c7772dcdca6efa1fa933322b)#define NPCX\_RESET\_SHA (NPCX\_RESET\_SWRST\_CTL3\_OFFSET + 29)

95

[ 96](npcx9__reset_8h.md#a838c9610f9e66a571cc62e9545149672)#define NPCX\_RESET\_MDMA1 (NPCX\_RESET\_SWRST\_CTL4\_OFFSET + 24)

[ 97](npcx9__reset_8h.md#a39bf10a9078ec7f6594c62cb0aa7e582)#define NPCX\_RESET\_MDMA2 (NPCX\_RESET\_SWRST\_CTL4\_OFFSET + 25)

[ 98](npcx9__reset_8h.md#a1753046ad47c66e3a1b62c0e83a8b2be)#define NPCX\_RESET\_MDMA3 (NPCX\_RESET\_SWRST\_CTL4\_OFFSET + 26)

[ 99](npcx9__reset_8h.md#a87133206a356006b43b849a24a145f18)#define NPCX\_RESET\_MDMA4 (NPCX\_RESET\_SWRST\_CTL4\_OFFSET + 27)

[ 100](npcx9__reset_8h.md#a1a801b84d37a87866b941151234305b8)#define NPCX\_RESET\_MDMA5 (NPCX\_RESET\_SWRST\_CTL4\_OFFSET + 28)

101

[ 102](npcx9__reset_8h.md#a0e8c75effca2fc27e91f92e5554714e0)#define NPCX\_RESET\_ID\_START NPCX\_RESET\_GPIO0

[ 103](npcx9__reset_8h.md#a6ea0ca8fc553b595907a7598856c4f7f)#define NPCX\_RESET\_ID\_END NPCX\_RESET\_MDMA5

104#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [npcx9\_reset.h](npcx9__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
