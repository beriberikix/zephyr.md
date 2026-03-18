---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mii_8h_source.html
original_path: doxygen/html/mii_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mii.h

[Go to the documentation of this file.](mii_8h.md)

1/\*

2 \* Copyright (c) 2016 Piotr Mienkowski

3 \* Copyright 2022 NXP

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_MII\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_MII\_H\_

14

21

22/\* MII management registers \*/

[ 24](group__ethernet__mii.md#ga9137acedc42ff140f244da7473cff29e)#define MII\_BMCR 0x0

[ 26](group__ethernet__mii.md#gaa2f632686d6298a7c898b1c805586aab)#define MII\_BMSR 0x1

[ 28](group__ethernet__mii.md#ga87196e916598cea91b6ce400ad0cc34a)#define MII\_PHYID1R 0x2

[ 30](group__ethernet__mii.md#ga40766cdb8f9c3ffee64720f0f0ea2f15)#define MII\_PHYID2R 0x3

[ 32](group__ethernet__mii.md#gaacb2ab0ea5579b5d9e30b075991add1d)#define MII\_ANAR 0x4

[ 34](group__ethernet__mii.md#ga445e8381a9ea9724054bfacc10bb4c81)#define MII\_ANLPAR 0x5

[ 36](group__ethernet__mii.md#ga6e5634d8831e21f963ddc16b91d5f6b9)#define MII\_ANER 0x6

[ 38](group__ethernet__mii.md#ga3f3ed3ecfd22b34b840ff2473ca68490)#define MII\_ANNPTR 0x7

[ 40](group__ethernet__mii.md#gaf17d80457d4a609d16793870d4a76bdf)#define MII\_ANLPRNPR 0x8

[ 42](group__ethernet__mii.md#ga9e258e8e518579ac5f9a8809ddc6aedb)#define MII\_1KTCR 0x9

[ 44](group__ethernet__mii.md#ga49a74b346b13cc80c159c0f8f6b9c0f0)#define MII\_1KSTSR 0xa

[ 46](group__ethernet__mii.md#ga7d6687385994aac21782308af560b224)#define MII\_MMD\_ACR 0xd

[ 48](group__ethernet__mii.md#ga378832f55be1a03977c829f09dd1d364)#define MII\_MMD\_AADR 0xe

[ 50](group__ethernet__mii.md#gaa705f43dba50029d5395379e1f2b802d)#define MII\_ESTAT 0xf

51

52/\* Basic Mode Control Register (BMCR) bit definitions \*/

[ 54](group__ethernet__mii.md#ga1001ac1540dc5bb6c4962f63b5fd6c3a)#define MII\_BMCR\_RESET (1 << 15)

[ 56](group__ethernet__mii.md#gaaade3d675167c736186a03dad857a7c9)#define MII\_BMCR\_LOOPBACK (1 << 14)

[ 58](group__ethernet__mii.md#ga19ef6d51e7bc231892635d856dd6a747)#define MII\_BMCR\_SPEED\_LSB (1 << 13)

[ 60](group__ethernet__mii.md#gaf58b450219ae18dfa2526c685a0402a7)#define MII\_BMCR\_AUTONEG\_ENABLE (1 << 12)

[ 62](group__ethernet__mii.md#ga2598b7655be14619dffc44b9a6db36b8)#define MII\_BMCR\_POWER\_DOWN (1 << 11)

[ 64](group__ethernet__mii.md#ga288b983fab32fb073cc42c3817b2c217)#define MII\_BMCR\_ISOLATE (1 << 10)

[ 66](group__ethernet__mii.md#ga110d6e1bfdbb37aa95cf1b32c54d8fa0)#define MII\_BMCR\_AUTONEG\_RESTART (1 << 9)

[ 68](group__ethernet__mii.md#ga288bc52d6545ec634e6c2da04dbe86d3)#define MII\_BMCR\_DUPLEX\_MODE (1 << 8)

[ 70](group__ethernet__mii.md#ga94e2ff6468b89371ec22a087ad5477d4)#define MII\_BMCR\_SPEED\_MSB (1 << 6)

[ 72](group__ethernet__mii.md#gaf562ae173424ea0d41afd68d11f87115)#define MII\_BMCR\_SPEED\_MASK (1 << 6 | 1 << 13)

[ 74](group__ethernet__mii.md#ga4d31aeaad35fe6a358aef1eef1c5b4cf)#define MII\_BMCR\_SPEED\_10 (0 << 6 | 0 << 13)

[ 76](group__ethernet__mii.md#gaf52c7fc2b468c142ae63605a201900d4)#define MII\_BMCR\_SPEED\_100 (0 << 6 | 1 << 13)

[ 78](group__ethernet__mii.md#gaae2f486072b95b3e829d0e1bd4b8d893)#define MII\_BMCR\_SPEED\_1000 (1 << 6 | 0 << 13)

79

80/\* Basic Mode Status Register (BMSR) bit definitions \*/

[ 82](group__ethernet__mii.md#gac8a404aa082745cb7699739bf58fc530)#define MII\_BMSR\_100BASE\_T4 (1 << 15)

[ 84](group__ethernet__mii.md#ga090c828a41acfc824b56ec2a9a57082a)#define MII\_BMSR\_100BASE\_X\_FULL (1 << 14)

[ 86](group__ethernet__mii.md#ga608ec5361c44f25c34ae6138ae7ffef9)#define MII\_BMSR\_100BASE\_X\_HALF (1 << 13)

[ 88](group__ethernet__mii.md#ga4f085921a6b0f0586326b1bdc8f62b31)#define MII\_BMSR\_10\_FULL (1 << 12)

[ 90](group__ethernet__mii.md#ga8505886511fef3ec2d8630a957de4478)#define MII\_BMSR\_10\_HALF (1 << 11)

[ 92](group__ethernet__mii.md#ga93fb7b79b3da2ae1757fe98237dd2d6b)#define MII\_BMSR\_100BASE\_T2\_FULL (1 << 10)

[ 94](group__ethernet__mii.md#gafb0d83d336eda611d45580be48f15d02)#define MII\_BMSR\_100BASE\_T2\_HALF (1 << 9)

[ 96](group__ethernet__mii.md#ga24992988cde973ce2a954fe372a5ad0e)#define MII\_BMSR\_EXTEND\_STATUS (1 << 8)

[ 98](group__ethernet__mii.md#gae85e29e0f9a50898f93ff6e5a5f763e4)#define MII\_BMSR\_MF\_PREAMB\_SUPPR (1 << 6)

[ 100](group__ethernet__mii.md#gac5b9ac6b54ce146c91197660c2ccd207)#define MII\_BMSR\_AUTONEG\_COMPLETE (1 << 5)

[ 102](group__ethernet__mii.md#ga0dd8421740c52ecd5e6a53e969d2e48a)#define MII\_BMSR\_REMOTE\_FAULT (1 << 4)

[ 104](group__ethernet__mii.md#gafc344357c76d6a41c5fa432d55355fce)#define MII\_BMSR\_AUTONEG\_ABILITY (1 << 3)

[ 106](group__ethernet__mii.md#ga884d39c456206cee38ce5a9a9ca01599)#define MII\_BMSR\_LINK\_STATUS (1 << 2)

[ 108](group__ethernet__mii.md#gad9ef4a2223dfee6826b0fdc8b25802ea)#define MII\_BMSR\_JABBER\_DETECT (1 << 1)

[ 110](group__ethernet__mii.md#gab225377deb09eb179b7efee199c7edd4)#define MII\_BMSR\_EXTEND\_CAPAB (1 << 0)

111

112/\* Auto-negotiation Advertisement Register (ANAR) bit definitions \*/

113/\* Auto-negotiation Link Partner Ability Register (ANLPAR) bit definitions \*/

[ 115](group__ethernet__mii.md#ga4e567fc428a19d55c13c6be38091ed59)#define MII\_ADVERTISE\_NEXT\_PAGE (1 << 15)

[ 117](group__ethernet__mii.md#gaca8ed07be80166e8abaefb4135008989)#define MII\_ADVERTISE\_LPACK (1 << 14)

[ 119](group__ethernet__mii.md#ga3e1cfef9ac347b86324d25c1d00a07ef)#define MII\_ADVERTISE\_REMOTE\_FAULT (1 << 13)

[ 121](group__ethernet__mii.md#gaf8b5e7fc3226b89b875f46a50165e332)#define MII\_ADVERTISE\_ASYM\_PAUSE (1 << 11)

[ 123](group__ethernet__mii.md#ga7b3dfbe50b37378cbf45d15f9ef88c7f)#define MII\_ADVERTISE\_PAUSE (1 << 10)

[ 125](group__ethernet__mii.md#ga11a26530d734fb68be5538ac36019821)#define MII\_ADVERTISE\_100BASE\_T4 (1 << 9)

[ 127](group__ethernet__mii.md#ga72f632c88cf6c472b893c326d7a8d263)#define MII\_ADVERTISE\_100\_FULL (1 << 8)

[ 129](group__ethernet__mii.md#ga357539fe99d327cae0e76acd5059876f)#define MII\_ADVERTISE\_100\_HALF (1 << 7)

[ 131](group__ethernet__mii.md#ga44ee311ef785619a215de80fc0286a4c)#define MII\_ADVERTISE\_10\_FULL (1 << 6)

[ 133](group__ethernet__mii.md#gac5c508943ce4006fa2f934c25436fdb5)#define MII\_ADVERTISE\_10\_HALF (1 << 5)

[ 135](group__ethernet__mii.md#gac01baecf625bbb6d55a14ac0c2b181bd)#define MII\_ADVERTISE\_SEL\_MASK (0x1F << 0)

[ 136](group__ethernet__mii.md#ga9abdfc8110120f54612c712d86cab3ac)#define MII\_ADVERTISE\_SEL\_IEEE\_802\_3 0x01

137

138/\* 1000BASE-T Control Register bit definitions \*/

[ 140](group__ethernet__mii.md#ga028ddaf632ced31e57249883c90ed921)#define MII\_ADVERTISE\_1000\_FULL (1 << 9)

[ 142](group__ethernet__mii.md#ga5f36d375690560688185d1207687611b)#define MII\_ADVERTISE\_1000\_HALF (1 << 8)

143

[ 144](group__ethernet__mii.md#gacac6f915a8d0e3f8244c571646b3fc92)#define MII\_ADVERTISE\_ALL (MII\_ADVERTISE\_10\_HALF | MII\_ADVERTISE\_10\_FULL |\

145 MII\_ADVERTISE\_100\_HALF | MII\_ADVERTISE\_100\_FULL |\

146 MII\_ADVERTISE\_SEL\_IEEE\_802\_3)

147

148/\* Extended Status Register bit definitions \*/

[ 150](group__ethernet__mii.md#ga846525a526aa9704a175c84771e48290)#define MII\_ESTAT\_1000BASE\_X\_FULL (1 << 15)

[ 152](group__ethernet__mii.md#gabec9696aa599caca1131f869827bbc95)#define MII\_ESTAT\_1000BASE\_X\_HALF (1 << 14)

[ 154](group__ethernet__mii.md#gada0831dbbb86ff717b40c23c73345731)#define MII\_ESTAT\_1000BASE\_T\_FULL (1 << 13)

[ 156](group__ethernet__mii.md#ga42e8d732fd9806e218599871fd1291d5)#define MII\_ESTAT\_1000BASE\_T\_HALF (1 << 12)

157

161

162#endif /\* ZEPHYR\_INCLUDE\_NET\_MII\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mii.h](mii_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
