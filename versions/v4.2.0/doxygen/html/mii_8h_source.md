---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mii_8h_source.html
original_path: doxygen/html/mii_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

15#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

16

25

26/\* MII management registers \*/

[ 28](group__ethernet__mii.md#ga9137acedc42ff140f244da7473cff29e)#define MII\_BMCR 0x0

[ 30](group__ethernet__mii.md#gaa2f632686d6298a7c898b1c805586aab)#define MII\_BMSR 0x1

[ 32](group__ethernet__mii.md#ga87196e916598cea91b6ce400ad0cc34a)#define MII\_PHYID1R 0x2

[ 34](group__ethernet__mii.md#ga40766cdb8f9c3ffee64720f0f0ea2f15)#define MII\_PHYID2R 0x3

[ 36](group__ethernet__mii.md#gaacb2ab0ea5579b5d9e30b075991add1d)#define MII\_ANAR 0x4

[ 38](group__ethernet__mii.md#ga445e8381a9ea9724054bfacc10bb4c81)#define MII\_ANLPAR 0x5

[ 40](group__ethernet__mii.md#ga6e5634d8831e21f963ddc16b91d5f6b9)#define MII\_ANER 0x6

[ 42](group__ethernet__mii.md#ga3f3ed3ecfd22b34b840ff2473ca68490)#define MII\_ANNPTR 0x7

[ 44](group__ethernet__mii.md#gaf17d80457d4a609d16793870d4a76bdf)#define MII\_ANLPRNPR 0x8

[ 46](group__ethernet__mii.md#ga9e258e8e518579ac5f9a8809ddc6aedb)#define MII\_1KTCR 0x9

[ 48](group__ethernet__mii.md#ga49a74b346b13cc80c159c0f8f6b9c0f0)#define MII\_1KSTSR 0xa

[ 50](group__ethernet__mii.md#ga7d6687385994aac21782308af560b224)#define MII\_MMD\_ACR 0xd

[ 52](group__ethernet__mii.md#ga378832f55be1a03977c829f09dd1d364)#define MII\_MMD\_AADR 0xe

[ 54](group__ethernet__mii.md#gaa705f43dba50029d5395379e1f2b802d)#define MII\_ESTAT 0xf

55

56/\* Basic Mode Control Register (BMCR) bit definitions \*/

[ 57](group__ethernet__mii.md#ga54df4d055d02d507cf52eb1a2811f1de)#define MII\_BMCR\_RESET\_BIT 15

[ 58](group__ethernet__mii.md#ga6e79703869a5e6459a4cbf2c103b8ed1)#define MII\_BMCR\_LOOPBACK\_BIT 14

[ 59](group__ethernet__mii.md#ga689b3d9154d01a6cd2ac12ca252d5dc6)#define MII\_BMCR\_SPEED\_LSB\_BIT 13

[ 60](group__ethernet__mii.md#ga780566e06059ce969cf2c7149cd28560)#define MII\_BMCR\_AUTONEG\_ENABLE\_BIT 12

[ 61](group__ethernet__mii.md#gafc726725b78ff3aed31a7ec30e168831)#define MII\_BMCR\_POWER\_DOWN\_BIT 11

[ 62](group__ethernet__mii.md#ga0c5b114330969ddfeb8a042b33561bb4)#define MII\_BMCR\_ISOLATE\_BIT 10

[ 63](group__ethernet__mii.md#gaca9844340da91e466e7303e9f5b0425f)#define MII\_BMCR\_AUTONEG\_RESTART\_BIT 9

[ 64](group__ethernet__mii.md#ga728082a7fb53de09ed3259e14fe6a539)#define MII\_BMCR\_DUPLEX\_MODE\_BIT 8

[ 65](group__ethernet__mii.md#gad75a0984bdbebe75921c6986a5122f30)#define MII\_BMCR\_SPEED\_MSB\_BIT 6

[ 67](group__ethernet__mii.md#ga1001ac1540dc5bb6c4962f63b5fd6c3a)#define MII\_BMCR\_RESET BIT(MII\_BMCR\_RESET\_BIT)

[ 69](group__ethernet__mii.md#gaaade3d675167c736186a03dad857a7c9)#define MII\_BMCR\_LOOPBACK BIT(MII\_BMCR\_LOOPBACK\_BIT)

[ 71](group__ethernet__mii.md#ga19ef6d51e7bc231892635d856dd6a747)#define MII\_BMCR\_SPEED\_LSB BIT(MII\_BMCR\_SPEED\_LSB\_BIT)

[ 73](group__ethernet__mii.md#gaf58b450219ae18dfa2526c685a0402a7)#define MII\_BMCR\_AUTONEG\_ENABLE BIT(MII\_BMCR\_AUTONEG\_ENABLE\_BIT)

[ 75](group__ethernet__mii.md#ga2598b7655be14619dffc44b9a6db36b8)#define MII\_BMCR\_POWER\_DOWN BIT(MII\_BMCR\_POWER\_DOWN\_BIT)

[ 77](group__ethernet__mii.md#ga288b983fab32fb073cc42c3817b2c217)#define MII\_BMCR\_ISOLATE BIT(MII\_BMCR\_ISOLATE\_BIT)

[ 79](group__ethernet__mii.md#ga110d6e1bfdbb37aa95cf1b32c54d8fa0)#define MII\_BMCR\_AUTONEG\_RESTART BIT(MII\_BMCR\_AUTONEG\_RESTART\_BIT)

[ 81](group__ethernet__mii.md#ga288bc52d6545ec634e6c2da04dbe86d3)#define MII\_BMCR\_DUPLEX\_MODE BIT(MII\_BMCR\_DUPLEX\_MODE\_BIT)

[ 83](group__ethernet__mii.md#ga94e2ff6468b89371ec22a087ad5477d4)#define MII\_BMCR\_SPEED\_MSB BIT(MII\_BMCR\_SPEED\_MSB\_BIT)

[ 85](group__ethernet__mii.md#gaf562ae173424ea0d41afd68d11f87115)#define MII\_BMCR\_SPEED\_MASK (MII\_BMCR\_SPEED\_MSB | MII\_BMCR\_SPEED\_LSB)

[ 87](group__ethernet__mii.md#ga4d31aeaad35fe6a358aef1eef1c5b4cf)#define MII\_BMCR\_SPEED\_10 0

[ 89](group__ethernet__mii.md#gaf52c7fc2b468c142ae63605a201900d4)#define MII\_BMCR\_SPEED\_100 BIT(MII\_BMCR\_SPEED\_LSB\_BIT)

[ 91](group__ethernet__mii.md#gaae2f486072b95b3e829d0e1bd4b8d893)#define MII\_BMCR\_SPEED\_1000 BIT(MII\_BMCR\_SPEED\_MSB\_BIT)

92

93/\* Basic Mode Status Register (BMSR) bit definitions \*/

[ 95](group__ethernet__mii.md#gac8a404aa082745cb7699739bf58fc530)#define MII\_BMSR\_100BASE\_T4 BIT(15)

[ 97](group__ethernet__mii.md#ga090c828a41acfc824b56ec2a9a57082a)#define MII\_BMSR\_100BASE\_X\_FULL BIT(14)

[ 99](group__ethernet__mii.md#ga608ec5361c44f25c34ae6138ae7ffef9)#define MII\_BMSR\_100BASE\_X\_HALF BIT(13)

[ 101](group__ethernet__mii.md#ga4f085921a6b0f0586326b1bdc8f62b31)#define MII\_BMSR\_10\_FULL BIT(12)

[ 103](group__ethernet__mii.md#ga8505886511fef3ec2d8630a957de4478)#define MII\_BMSR\_10\_HALF BIT(11)

[ 105](group__ethernet__mii.md#ga93fb7b79b3da2ae1757fe98237dd2d6b)#define MII\_BMSR\_100BASE\_T2\_FULL BIT(10)

[ 107](group__ethernet__mii.md#gafb0d83d336eda611d45580be48f15d02)#define MII\_BMSR\_100BASE\_T2\_HALF BIT(9)

[ 109](group__ethernet__mii.md#ga24992988cde973ce2a954fe372a5ad0e)#define MII\_BMSR\_EXTEND\_STATUS BIT(8)

[ 111](group__ethernet__mii.md#gae85e29e0f9a50898f93ff6e5a5f763e4)#define MII\_BMSR\_MF\_PREAMB\_SUPPR BIT(6)

[ 113](group__ethernet__mii.md#gac5b9ac6b54ce146c91197660c2ccd207)#define MII\_BMSR\_AUTONEG\_COMPLETE BIT(5)

[ 115](group__ethernet__mii.md#ga0dd8421740c52ecd5e6a53e969d2e48a)#define MII\_BMSR\_REMOTE\_FAULT BIT(4)

[ 117](group__ethernet__mii.md#gafc344357c76d6a41c5fa432d55355fce)#define MII\_BMSR\_AUTONEG\_ABILITY BIT(3)

[ 119](group__ethernet__mii.md#ga884d39c456206cee38ce5a9a9ca01599)#define MII\_BMSR\_LINK\_STATUS BIT(2)

[ 121](group__ethernet__mii.md#gad9ef4a2223dfee6826b0fdc8b25802ea)#define MII\_BMSR\_JABBER\_DETECT BIT(1)

[ 123](group__ethernet__mii.md#gab225377deb09eb179b7efee199c7edd4)#define MII\_BMSR\_EXTEND\_CAPAB BIT(0)

124

125/\* Auto-negotiation Advertisement Register (ANAR) bit definitions \*/

126/\* Auto-negotiation Link Partner Ability Register (ANLPAR) bit definitions \*/

[ 127](group__ethernet__mii.md#ga22cb9fe314c187beee08d1c1e41d8373)#define MII\_ADVERTISE\_NEXT\_PAGE\_BIT 15

[ 128](group__ethernet__mii.md#gaf8344fb430b18d38d4abdc0143375df6)#define MII\_ADVERTISE\_LPACK\_BIT 14

[ 129](group__ethernet__mii.md#ga6bce3c2f70cddc50205a330158612f8c)#define MII\_ADVERTISE\_REMOTE\_FAULT\_BIT 13

[ 130](group__ethernet__mii.md#ga4c5ac54f1516343790181acfbf5529c8)#define MII\_ADVERTISE\_ASYM\_PAUSE\_BIT 11

[ 131](group__ethernet__mii.md#ga35994af1965ff3f9aa68d203241f97d3)#define MII\_ADVERTISE\_PAUSE\_BIT 10

[ 132](group__ethernet__mii.md#ga825049982099c0601da4f801fccb6e64)#define MII\_ADVERTISE\_100BASE\_T4\_BIT 9

[ 133](group__ethernet__mii.md#ga02d2b86da4062c296c154013b255d720)#define MII\_ADVERTISE\_100\_FULL\_BIT 8

[ 134](group__ethernet__mii.md#ga949f20431a0ccfef97e6d2b5ee0484c0)#define MII\_ADVERTISE\_100\_HALF\_BIT 7

[ 135](group__ethernet__mii.md#ga4ee2f6bdb657842db35e396839896cc8)#define MII\_ADVERTISE\_10\_FULL\_BIT 6

[ 136](group__ethernet__mii.md#ga622c65ecfadf01ff4bb4f9dd06393428)#define MII\_ADVERTISE\_10\_HALF\_BIT 5

[ 138](group__ethernet__mii.md#ga4e567fc428a19d55c13c6be38091ed59)#define MII\_ADVERTISE\_NEXT\_PAGE BIT(MII\_ADVERTISE\_NEXT\_PAGE\_BIT)

[ 140](group__ethernet__mii.md#gaca8ed07be80166e8abaefb4135008989)#define MII\_ADVERTISE\_LPACK BIT(MII\_ADVERTISE\_LPACK\_BIT)

[ 142](group__ethernet__mii.md#ga3e1cfef9ac347b86324d25c1d00a07ef)#define MII\_ADVERTISE\_REMOTE\_FAULT BIT(MII\_ADVERTISE\_REMOTE\_FAULT\_BIT)

[ 144](group__ethernet__mii.md#gaf8b5e7fc3226b89b875f46a50165e332)#define MII\_ADVERTISE\_ASYM\_PAUSE BIT(MII\_ADVERTISE\_ASYM\_PAUSE\_BIT)

[ 146](group__ethernet__mii.md#ga7b3dfbe50b37378cbf45d15f9ef88c7f)#define MII\_ADVERTISE\_PAUSE BIT(MII\_ADVERTISE\_PAUSE\_BIT)

[ 148](group__ethernet__mii.md#ga11a26530d734fb68be5538ac36019821)#define MII\_ADVERTISE\_100BASE\_T4 BIT(MII\_ADVERTISE\_100BASE\_T4\_BIT)

[ 150](group__ethernet__mii.md#ga72f632c88cf6c472b893c326d7a8d263)#define MII\_ADVERTISE\_100\_FULL BIT(MII\_ADVERTISE\_100\_FULL\_BIT)

[ 152](group__ethernet__mii.md#ga357539fe99d327cae0e76acd5059876f)#define MII\_ADVERTISE\_100\_HALF BIT(MII\_ADVERTISE\_100\_HALF\_BIT)

[ 154](group__ethernet__mii.md#ga44ee311ef785619a215de80fc0286a4c)#define MII\_ADVERTISE\_10\_FULL BIT(MII\_ADVERTISE\_10\_FULL\_BIT)

[ 156](group__ethernet__mii.md#gac5c508943ce4006fa2f934c25436fdb5)#define MII\_ADVERTISE\_10\_HALF BIT(MII\_ADVERTISE\_10\_HALF\_BIT)

[ 158](group__ethernet__mii.md#gac01baecf625bbb6d55a14ac0c2b181bd)#define MII\_ADVERTISE\_SEL\_MASK (0x1F << 0)

[ 160](group__ethernet__mii.md#ga9abdfc8110120f54612c712d86cab3ac)#define MII\_ADVERTISE\_SEL\_IEEE\_802\_3 0x01

161

162/\* 1000BASE-T Control Register bit definitions \*/

[ 163](group__ethernet__mii.md#gabeda2717f8c4d425ccf4562ff6fac4fb)#define MII\_ADVERTISE\_1000\_FULL\_BIT 9

[ 164](group__ethernet__mii.md#gaaeef419de1d90bfd58ba3452218e9004)#define MII\_ADVERTISE\_1000\_HALF\_BIT 8

[ 166](group__ethernet__mii.md#ga028ddaf632ced31e57249883c90ed921)#define MII\_ADVERTISE\_1000\_FULL BIT(MII\_ADVERTISE\_1000\_FULL\_BIT)

[ 168](group__ethernet__mii.md#ga5f36d375690560688185d1207687611b)#define MII\_ADVERTISE\_1000\_HALF BIT(MII\_ADVERTISE\_1000\_HALF\_BIT)

169

[ 171](group__ethernet__mii.md#gacac6f915a8d0e3f8244c571646b3fc92)#define MII\_ADVERTISE\_ALL (MII\_ADVERTISE\_10\_HALF | MII\_ADVERTISE\_10\_FULL |\

172 MII\_ADVERTISE\_100\_HALF | MII\_ADVERTISE\_100\_FULL |\

173 MII\_ADVERTISE\_SEL\_IEEE\_802\_3)

174

175/\* Extended Status Register bit definitions \*/

[ 177](group__ethernet__mii.md#ga846525a526aa9704a175c84771e48290)#define MII\_ESTAT\_1000BASE\_X\_FULL BIT(15)

[ 179](group__ethernet__mii.md#gabec9696aa599caca1131f869827bbc95)#define MII\_ESTAT\_1000BASE\_X\_HALF BIT(14)

[ 181](group__ethernet__mii.md#gada0831dbbb86ff717b40c23c73345731)#define MII\_ESTAT\_1000BASE\_T\_FULL BIT(13)

[ 183](group__ethernet__mii.md#ga42e8d732fd9806e218599871fd1291d5)#define MII\_ESTAT\_1000BASE\_T\_HALF BIT(12)

184

185/\* MMD Access Control Register (MII\_MMD\_ACR) Register bit definitions \*/

[ 187](group__ethernet__mii.md#gae4ac896c90a75cdc4869797708823673)#define MII\_MMD\_ACR\_DEVAD\_MASK (0x1F << 0)

[ 189](group__ethernet__mii.md#ga0f312eab9b4d51af4a72f7cb3898754a)#define MII\_MMD\_ACR\_ADDR (0x00 << 14)

[ 190](group__ethernet__mii.md#ga6cac36daf5db44274cd60a05b77819f4)#define MII\_MMD\_ACR\_DATA\_NO\_POS\_INC (0x01 << 14)

[ 191](group__ethernet__mii.md#ga3be4dced4eec405c42467ba51c5efb9c)#define MII\_MMD\_ACR\_DATA\_RW\_POS\_INC (0x10 << 14)

[ 192](group__ethernet__mii.md#ga48f56892c3e8d6ec7e90a7e36dd67309)#define MII\_MMD\_ACR\_DATA\_W\_POS\_INC (0x11 << 14)

193

197

198#endif /\* ZEPHYR\_INCLUDE\_NET\_MII\_H\_ \*/

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mii.h](mii_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
