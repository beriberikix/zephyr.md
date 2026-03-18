---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/npcx__espi_8h_source.html
original_path: doxygen/html/npcx__espi_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

9/\* eSPI VW Master to Slave Register Index \*/

[ 10](npcx__espi_8h.md#adbdeaaf543bb993edbf967bd55aece35)#define NPCX\_VWEVMS0 0

[ 11](npcx__espi_8h.md#a24141b9cbae48d80e980675a5dfa1e23)#define NPCX\_VWEVMS1 1

[ 12](npcx__espi_8h.md#a3c4778cc5e5e46e76d38780894e656d6)#define NPCX\_VWEVMS2 2

[ 13](npcx__espi_8h.md#a00ac62fd94e17a2a04dddf90d388a2df)#define NPCX\_VWEVMS3 3

[ 14](npcx__espi_8h.md#a17164bf39cd92e5739f7271807575d63)#define NPCX\_VWEVMS4 4

[ 15](npcx__espi_8h.md#a9292b6d86c9c18bd1e75b4bfe269903f)#define NPCX\_VWEVMS5 5

[ 16](npcx__espi_8h.md#ab78bfbcf789ae6fc413b7de8f8beea77)#define NPCX\_VWEVMS6 6

[ 17](npcx__espi_8h.md#ab2db9086976932021f9b3722332f2ae0)#define NPCX\_VWEVMS7 7

[ 18](npcx__espi_8h.md#a676e4a19d39a0b75e5b725b906012b0a)#define NPCX\_VWEVMS8 8

[ 19](npcx__espi_8h.md#a26bca34214c80719fa9afe686d162dff)#define NPCX\_VWEVMS9 9

20

21/\* eSPI VW Slave to Master Register Index \*/

[ 22](npcx__espi_8h.md#a54d24297928a3f9b7deb6efcc1196cc4)#define NPCX\_VWEVSM0 0

[ 23](npcx__espi_8h.md#affac66095c38c2b225f55feaf3ad2e38)#define NPCX\_VWEVSM1 1

[ 24](npcx__espi_8h.md#a3a427ba40898d3cfbfe8ceed4c02598c)#define NPCX\_VWEVSM2 2

[ 25](npcx__espi_8h.md#a65522ce32ef1581dd752bc6f2c46ff8e)#define NPCX\_VWEVSM3 3

[ 26](npcx__espi_8h.md#ab9eb8ad58913c809b8425a727533418d)#define NPCX\_VWEVSM4 4

[ 27](npcx__espi_8h.md#a269ee52ab249b375c1fede6252b43604)#define NPCX\_VWEVSM5 5

[ 28](npcx__espi_8h.md#ab03c9ed65c5570fef4752a5dd61c2929)#define NPCX\_VWEVSM6 6

[ 29](npcx__espi_8h.md#ac30e34899487bc249f4efbb2bbf0d086)#define NPCX\_VWEVSM7 7

[ 30](npcx__espi_8h.md#a8c2b45892804abd0bdc3a8d6e8238331)#define NPCX\_VWEVSM8 8

[ 31](npcx__espi_8h.md#ac705a0827536a8eb5de93fe9cd690895)#define NPCX\_VWEVSM9 9

[ 32](npcx__espi_8h.md#a7ddf42d91d380b3a3ff4a513e6944873)#define NPCX\_VWEVSM10 10

[ 33](npcx__espi_8h.md#a89ea7d1d35017a9e2f123e1e3f13ce3b)#define NPCX\_VWEVSM11 11

34

35/\* eSPI VW GPIO Slave to Master Register Index \*/

[ 36](npcx__espi_8h.md#aac6e5d68d9c81f44654fab29c4ab358e)#define NPCX\_VWGPSM0 0

[ 37](npcx__espi_8h.md#a1e9c90475c895fdc9f902c39787dab6e)#define NPCX\_VWGPSM1 1

[ 38](npcx__espi_8h.md#a8aec14021e5a6c321c460bea60631ea7)#define NPCX\_VWGPSM2 2

[ 39](npcx__espi_8h.md#a5095293d104f0379d43e5adfbec4d8eb)#define NPCX\_VWGPSM3 3

[ 40](npcx__espi_8h.md#a1e531b5e80253d88787f8e2277dca6e0)#define NPCX\_VWGPSM4 4

[ 41](npcx__espi_8h.md#a2bb5ba01df0d1643be04d7ba14e3e536)#define NPCX\_VWGPSM5 5

[ 42](npcx__espi_8h.md#a90d7007053d60df3e567d5d169fb9a83)#define NPCX\_VWGPSM6 6

[ 43](npcx__espi_8h.md#af76ad624ebc99ff5a16841b3de78107f)#define NPCX\_VWGPSM7 7

[ 44](npcx__espi_8h.md#a1f8985b3f790f7442566909d9080c767)#define NPCX\_VWGPSM8 8

[ 45](npcx__espi_8h.md#a704fe2838fb81713b700db1abefdac24)#define NPCX\_VWGPSM9 9

[ 46](npcx__espi_8h.md#a426ed320a233b2afef1ecc919d4be958)#define NPCX\_VWGPSM10 10

[ 47](npcx__espi_8h.md#aed6b32181e21c17ee9c1118aeb68b266)#define NPCX\_VWGPSM11 11

[ 48](npcx__espi_8h.md#ab99e1d965b021e817db5619071445191)#define NPCX\_VWGPSM12 12

[ 49](npcx__espi_8h.md#a675569f4403b226bd1b794b9179cdffb)#define NPCX\_VWGPSM13 13

[ 50](npcx__espi_8h.md#a9017565937fd3fb8b975908a07a4f4ad)#define NPCX\_VWGPSM14 14

[ 51](npcx__espi_8h.md#aee52ed8c508c4a3b32df96f45e03ad82)#define NPCX\_VWGPSM15 15

52

53#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ESPI\_NPCX\_ESPI\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [espi](dir_c024b988744650ec655821cf6ff53a0b.md)
- [npcx\_espi.h](npcx__espi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
