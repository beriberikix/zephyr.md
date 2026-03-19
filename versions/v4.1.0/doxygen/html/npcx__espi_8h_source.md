---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/npcx__espi_8h_source.html
original_path: doxygen/html/npcx__espi_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcx\_espi.h

[Go to the documentation of this file.](npcx__espi_8h.md)

1/\*

2 \* Copyright (c) 2020 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ESPI\_NPCX\_ESPI\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ESPI\_NPCX\_ESPI\_H\_

8

9/\*

10 \* Encode virtual wire information into a 16-bit unsigned.

11 \* index = bits[7:0], Replacement index number

12 \* group = bits[11:8], Group number for VWEVMS or VWEVSM

13 \* dir = bits[13:12], Direction for controller to target or target to controller

14 \*/

[ 15](npcx__espi_8h.md#ac5bf7f75ecd869d2ed1d1209f5b46248)#define ESPI\_NPCX\_VW\_EX\_VAL(dir, group, index) \

16 (((dir & 0x1) << 12) + ((group & 0xf) << 8) + (index & 0xff))

17

18/\* extract specific information from encoded ESPI\_NPCX\_VW\_EX\_VAL \*/

[ 19](npcx__espi_8h.md#a014b58b053bd26e2a365cbe8520d0421)#define ESPI\_NPCX\_VW\_EX\_INDEX(e) ((e) & 0xff)

[ 20](npcx__espi_8h.md#ab992e56a785a9e60fcf3d92af0c94ea7)#define ESPI\_NPCX\_VW\_EX\_GROUP\_NUM(e) (((e) >> 8) & 0xf)

[ 21](npcx__espi_8h.md#a2dcad76fd6ebf24e755a741edc2719be)#define ESPI\_NPCX\_VW\_EX\_DIR(e) (((e) >> 12) & 0x1)

22

23/\* eSPI VW Master to Slave Register Index \*/

[ 24](npcx__espi_8h.md#adbdeaaf543bb993edbf967bd55aece35)#define NPCX\_VWEVMS0 0

[ 25](npcx__espi_8h.md#a24141b9cbae48d80e980675a5dfa1e23)#define NPCX\_VWEVMS1 1

[ 26](npcx__espi_8h.md#a3c4778cc5e5e46e76d38780894e656d6)#define NPCX\_VWEVMS2 2

[ 27](npcx__espi_8h.md#a00ac62fd94e17a2a04dddf90d388a2df)#define NPCX\_VWEVMS3 3

[ 28](npcx__espi_8h.md#a17164bf39cd92e5739f7271807575d63)#define NPCX\_VWEVMS4 4

[ 29](npcx__espi_8h.md#a9292b6d86c9c18bd1e75b4bfe269903f)#define NPCX\_VWEVMS5 5

[ 30](npcx__espi_8h.md#ab78bfbcf789ae6fc413b7de8f8beea77)#define NPCX\_VWEVMS6 6

[ 31](npcx__espi_8h.md#ab2db9086976932021f9b3722332f2ae0)#define NPCX\_VWEVMS7 7

[ 32](npcx__espi_8h.md#a676e4a19d39a0b75e5b725b906012b0a)#define NPCX\_VWEVMS8 8

[ 33](npcx__espi_8h.md#a26bca34214c80719fa9afe686d162dff)#define NPCX\_VWEVMS9 9

[ 34](npcx__espi_8h.md#a4dd1c25e9ecc3d39f2f13680ed6ed3cc)#define NPCX\_VWEVMS10 10

[ 35](npcx__espi_8h.md#aa5e8bc5f05deba6d7cf97a6b38c8cad7)#define NPCX\_VWEVMS11 11

[ 36](npcx__espi_8h.md#ade67d5bb648c7e7791e005c40f4330b2)#define NPCX\_VWEVMS\_MAX 12

37

38/\* eSPI VW Slave to Master Register Index \*/

[ 39](npcx__espi_8h.md#a54d24297928a3f9b7deb6efcc1196cc4)#define NPCX\_VWEVSM0 0

[ 40](npcx__espi_8h.md#affac66095c38c2b225f55feaf3ad2e38)#define NPCX\_VWEVSM1 1

[ 41](npcx__espi_8h.md#a3a427ba40898d3cfbfe8ceed4c02598c)#define NPCX\_VWEVSM2 2

[ 42](npcx__espi_8h.md#a65522ce32ef1581dd752bc6f2c46ff8e)#define NPCX\_VWEVSM3 3

[ 43](npcx__espi_8h.md#ab9eb8ad58913c809b8425a727533418d)#define NPCX\_VWEVSM4 4

[ 44](npcx__espi_8h.md#a269ee52ab249b375c1fede6252b43604)#define NPCX\_VWEVSM5 5

[ 45](npcx__espi_8h.md#ab03c9ed65c5570fef4752a5dd61c2929)#define NPCX\_VWEVSM6 6

[ 46](npcx__espi_8h.md#ac30e34899487bc249f4efbb2bbf0d086)#define NPCX\_VWEVSM7 7

[ 47](npcx__espi_8h.md#a8c2b45892804abd0bdc3a8d6e8238331)#define NPCX\_VWEVSM8 8

[ 48](npcx__espi_8h.md#ac705a0827536a8eb5de93fe9cd690895)#define NPCX\_VWEVSM9 9

[ 49](npcx__espi_8h.md#a459b9d699af40d316ecfcfd0ccd2fa46)#define NPCX\_VWEVSM\_MAX 10

50

51/\* eSPI VW GPIO Slave to Master Register Index \*/

[ 52](npcx__espi_8h.md#aac6e5d68d9c81f44654fab29c4ab358e)#define NPCX\_VWGPSM0 0

[ 53](npcx__espi_8h.md#a1e9c90475c895fdc9f902c39787dab6e)#define NPCX\_VWGPSM1 1

[ 54](npcx__espi_8h.md#a8aec14021e5a6c321c460bea60631ea7)#define NPCX\_VWGPSM2 2

[ 55](npcx__espi_8h.md#a5095293d104f0379d43e5adfbec4d8eb)#define NPCX\_VWGPSM3 3

[ 56](npcx__espi_8h.md#a1e531b5e80253d88787f8e2277dca6e0)#define NPCX\_VWGPSM4 4

[ 57](npcx__espi_8h.md#a2bb5ba01df0d1643be04d7ba14e3e536)#define NPCX\_VWGPSM5 5

[ 58](npcx__espi_8h.md#a90d7007053d60df3e567d5d169fb9a83)#define NPCX\_VWGPSM6 6

[ 59](npcx__espi_8h.md#af76ad624ebc99ff5a16841b3de78107f)#define NPCX\_VWGPSM7 7

[ 60](npcx__espi_8h.md#a1f8985b3f790f7442566909d9080c767)#define NPCX\_VWGPSM8 8

[ 61](npcx__espi_8h.md#a704fe2838fb81713b700db1abefdac24)#define NPCX\_VWGPSM9 9

[ 62](npcx__espi_8h.md#a426ed320a233b2afef1ecc919d4be958)#define NPCX\_VWGPSM10 10

[ 63](npcx__espi_8h.md#aed6b32181e21c17ee9c1118aeb68b266)#define NPCX\_VWGPSM11 11

[ 64](npcx__espi_8h.md#ab99e1d965b021e817db5619071445191)#define NPCX\_VWGPSM12 12

[ 65](npcx__espi_8h.md#a675569f4403b226bd1b794b9179cdffb)#define NPCX\_VWGPSM13 13

[ 66](npcx__espi_8h.md#a9017565937fd3fb8b975908a07a4f4ad)#define NPCX\_VWGPSM14 14

[ 67](npcx__espi_8h.md#aee52ed8c508c4a3b32df96f45e03ad82)#define NPCX\_VWGPSM15 15

68

69#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ESPI\_NPCX\_ESPI\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [espi](dir_c024b988744650ec655821cf6ff53a0b.md)
- [npcx\_espi.h](npcx__espi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
