---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/npcm__clock_8h_source.html
original_path: doxygen/html/npcm__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcm\_clock.h

[Go to the documentation of this file.](npcm__clock_8h.md)

1/\*

2 \* Copyright (c) 2024 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCM\_CLOCK\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCM\_CLOCK\_H\_

8

9/\* clock bus references \*/

[ 10](npcm__clock_8h.md#aedf3c4059e2dba237097428dd3d17c86)#define NPCM\_CLOCK\_GROUP\_OFFSET(N) ((N) << 3)

11

[ 12](npcm__clock_8h.md#a63e02592f717f0575db06065c5abf7f9)#define NPCM\_CLOCK\_PWM\_I (NPCM\_CLOCK\_GROUP\_OFFSET(0) + 0)

[ 13](npcm__clock_8h.md#a34ece572167371f620570db82dc99a0e)#define NPCM\_CLOCK\_PWM\_J (NPCM\_CLOCK\_GROUP\_OFFSET(0) + 1)

[ 14](npcm__clock_8h.md#a67cdf00a70f0ba34a91540895c2b0e77)#define NPCM\_CLOCK\_I3CI (NPCM\_CLOCK\_GROUP\_OFFSET(0) + 2)

[ 15](npcm__clock_8h.md#a8070523598b622f82e7c4aa61fa113a2)#define NPCM\_CLOCK\_UART3 (NPCM\_CLOCK\_GROUP\_OFFSET(0) + 5)

[ 16](npcm__clock_8h.md#a2595c240f8bd2e046a8b4e06834289bb)#define NPCM\_CLOCK\_UART2 (NPCM\_CLOCK\_GROUP\_OFFSET(0) + 6)

[ 17](npcm__clock_8h.md#a2f2f35b3ac73ed602668b418dbbc6076)#define NPCM\_CLOCK\_SPIM (NPCM\_CLOCK\_GROUP\_OFFSET(1) + 0)

[ 18](npcm__clock_8h.md#a7b00badf4c99ff49e9babf170f6213a0)#define NPCM\_CLOCK\_FIU (NPCM\_CLOCK\_GROUP\_OFFSET(1) + 2)

[ 19](npcm__clock_8h.md#afb2fb08d08717664793a3179e87a96c8)#define NPCM\_CLOCK\_USB20 (NPCM\_CLOCK\_GROUP\_OFFSET(1) + 3)

[ 20](npcm__clock_8h.md#a94aa8507b21fc4fd4d9fd14844f03153)#define NPCM\_CLOCK\_UART (NPCM\_CLOCK\_GROUP\_OFFSET(1) + 4)

[ 21](npcm__clock_8h.md#a32de4522569dae6c3b8d5c7d8ea1f705)#define NPCM\_CLOCK\_MFT1 (NPCM\_CLOCK\_GROUP\_OFFSET(1) + 5)

[ 22](npcm__clock_8h.md#a011119434180ff4f782a1dada942f1fd)#define NPCM\_CLOCK\_MFT2 (NPCM\_CLOCK\_GROUP\_OFFSET(1) + 6)

[ 23](npcm__clock_8h.md#ae6526a686b1a3761dcde981f19469476)#define NPCM\_CLOCK\_MFT3 (NPCM\_CLOCK\_GROUP\_OFFSET(1) + 7)

[ 24](npcm__clock_8h.md#ae57d8b61165a095ec4b19aaa67b02156)#define NPCM\_CLOCK\_PWM\_A (NPCM\_CLOCK\_GROUP\_OFFSET(2) + 0)

[ 25](npcm__clock_8h.md#acf2e8eefaf16ae166307b5cb0c9706d0)#define NPCM\_CLOCK\_PWM\_B (NPCM\_CLOCK\_GROUP\_OFFSET(2) + 1)

[ 26](npcm__clock_8h.md#a22bd19514fb8140afb3652c1cc131e81)#define NPCM\_CLOCK\_PWM\_C (NPCM\_CLOCK\_GROUP\_OFFSET(2) + 2)

[ 27](npcm__clock_8h.md#afb2ca7ea81c2f43e7576ff80e0aa2b0b)#define NPCM\_CLOCK\_PWM\_D (NPCM\_CLOCK\_GROUP\_OFFSET(2) + 3)

[ 28](npcm__clock_8h.md#afd75d18a0f1f0743625b8114fea9d8dd)#define NPCM\_CLOCK\_PWM\_E (NPCM\_CLOCK\_GROUP\_OFFSET(2) + 4)

[ 29](npcm__clock_8h.md#ae2357132f9cb282171562e8a022c444f)#define NPCM\_CLOCK\_PWM\_F (NPCM\_CLOCK\_GROUP\_OFFSET(2) + 5)

[ 30](npcm__clock_8h.md#a9e3a29585ee19d46f0a59cbd821e1f04)#define NPCM\_CLOCK\_PWM\_G (NPCM\_CLOCK\_GROUP\_OFFSET(2) + 6)

[ 31](npcm__clock_8h.md#a2573f4ffb1e16de8e68cd0ed4da20085)#define NPCM\_CLOCK\_PWM\_H (NPCM\_CLOCK\_GROUP\_OFFSET(2) + 7)

[ 32](npcm__clock_8h.md#aaba6ccd3affdf2d2e423e8be6f5b4fee)#define NPCM\_CLOCK\_SMB1 (NPCM\_CLOCK\_GROUP\_OFFSET(3) + 0)

[ 33](npcm__clock_8h.md#a029f41a64d84585ee2fc8f80d9fc30fb)#define NPCM\_CLOCK\_SMB2 (NPCM\_CLOCK\_GROUP\_OFFSET(3) + 1)

[ 34](npcm__clock_8h.md#a556e5bde2edcaacacdfd6cd82fe03efa)#define NPCM\_CLOCK\_SMB3 (NPCM\_CLOCK\_GROUP\_OFFSET(3) + 2)

[ 35](npcm__clock_8h.md#acd9b598f8757e298bdbef6b13114099e)#define NPCM\_CLOCK\_SMB4 (NPCM\_CLOCK\_GROUP\_OFFSET(3) + 3)

[ 36](npcm__clock_8h.md#a934ed236e7462eedf1e58f98c5e90dfb)#define NPCM\_CLOCK\_SMB5 (NPCM\_CLOCK\_GROUP\_OFFSET(3) + 4)

[ 37](npcm__clock_8h.md#a49989ff0da3f5807b7e1a045b1568429)#define NPCM\_CLOCK\_SMB6 (NPCM\_CLOCK\_GROUP\_OFFSET(3) + 5)

[ 38](npcm__clock_8h.md#af437c95f765f9060b061ca3511c89dd7)#define NPCM\_CLOCK\_GDMA (NPCM\_CLOCK\_GROUP\_OFFSET(3) + 7)

[ 39](npcm__clock_8h.md#adc9d8de8a2f2847c66288050cd30a6fd)#define NPCM\_CLOCK\_ITIM1 (NPCM\_CLOCK\_GROUP\_OFFSET(4) + 0)

[ 40](npcm__clock_8h.md#a51720bbd7c55c99fbc72adb80a707617)#define NPCM\_CLOCK\_ITIM2 (NPCM\_CLOCK\_GROUP\_OFFSET(4) + 1)

[ 41](npcm__clock_8h.md#a41bb9d31b946f991f8c1970674174601)#define NPCM\_CLOCK\_ITIM3 (NPCM\_CLOCK\_GROUP\_OFFSET(4) + 2)

[ 42](npcm__clock_8h.md#af96d5c1e939aa5fa9128173d4f545081)#define NPCM\_CLOCK\_SMB\_DMA (NPCM\_CLOCK\_GROUP\_OFFSET(4) + 3)

[ 43](npcm__clock_8h.md#adf45628a0f330eb1b4d74aab9e9a9ef8)#define NPCM\_CLOCK\_ADC (NPCM\_CLOCK\_GROUP\_OFFSET(4) + 4)

[ 44](npcm__clock_8h.md#ae38fb3273e3a5fcabac782e65533734a)#define NPCM\_CLOCK\_PECI (NPCM\_CLOCK\_GROUP\_OFFSET(4) + 5)

[ 45](npcm__clock_8h.md#a8b3833a37e4e09cc75dbdbcfa045d358)#define NPCM\_CLOCK\_SPIP1 (NPCM\_CLOCK\_GROUP\_OFFSET(4) + 7)

[ 46](npcm__clock_8h.md#a1c86b295d71f8fd761f3c8fefd86d3e5)#define NPCM\_CLOCK\_UART4 (NPCM\_CLOCK\_GROUP\_OFFSET(5) + 0)

[ 47](npcm__clock_8h.md#aa832699b710f1cd9923a76d955ec1339)#define NPCM\_CLOCK\_C2HACC (NPCM\_CLOCK\_GROUP\_OFFSET(5) + 3)

[ 48](npcm__clock_8h.md#a443a40fca1ed3567c0c01e3ff339921b)#define NPCM\_CLOCK\_SHM\_REG (NPCM\_CLOCK\_GROUP\_OFFSET(5) + 4)

[ 49](npcm__clock_8h.md#adf9c6f59ed292bec420e09a27e9f1dcf)#define NPCM\_CLOCK\_SHM (NPCM\_CLOCK\_GROUP\_OFFSET(5) + 5)

[ 50](npcm__clock_8h.md#a24df8c7fe6d010cf4fc2105d7f9be99f)#define NPCM\_CLOCK\_DP80 (NPCM\_CLOCK\_GROUP\_OFFSET(5) + 6)

[ 51](npcm__clock_8h.md#a3c3df6e489aeb633b6108e1972071495)#define NPCM\_CLOCK\_MSWC (NPCM\_CLOCK\_GROUP\_OFFSET(5) + 7)

[ 52](npcm__clock_8h.md#a673d71f42575f480d596e2d75c72694d)#define NPCM\_CLOCK\_ITIM4 (NPCM\_CLOCK\_GROUP\_OFFSET(6) + 0)

[ 53](npcm__clock_8h.md#a142e5fd523ea4e5a88539e2c90d4cb3a)#define NPCM\_CLOCK\_ITIM5 (NPCM\_CLOCK\_GROUP\_OFFSET(6) + 1)

[ 54](npcm__clock_8h.md#ae8d5a71630b1727200508fa785030184)#define NPCM\_CLOCK\_ITIM6 (NPCM\_CLOCK\_GROUP\_OFFSET(6) + 2)

[ 55](npcm__clock_8h.md#aa4641068fa6c9aca20589f682c7e36a8)#define NPCM\_CLOCK\_RNG (NPCM\_CLOCK\_GROUP\_OFFSET(6) + 3)

[ 56](npcm__clock_8h.md#adec2955e9224587cdaa61aa20c6a1b7d)#define NPCM\_CLOCK\_SHA (NPCM\_CLOCK\_GROUP\_OFFSET(6) + 5)

[ 57](npcm__clock_8h.md#ac24765ff08e97f4747aa34b03e94eab6)#define NPCM\_CLOCK\_ESPI (NPCM\_CLOCK\_GROUP\_OFFSET(6) + 7)

[ 58](npcm__clock_8h.md#a5361334cef2fe6f4a0f93316c9fba60e)#define NPCM\_CLOCK\_SMB7 (NPCM\_CLOCK\_GROUP\_OFFSET(7) + 0)

[ 59](npcm__clock_8h.md#afa82d31834ccfb0e1766b4645174aa1b)#define NPCM\_CLOCK\_SMB8 (NPCM\_CLOCK\_GROUP\_OFFSET(7) + 1)

[ 60](npcm__clock_8h.md#af6b642aababfe104bdd8bb6a5b6a0673)#define NPCM\_CLOCK\_SMB9 (NPCM\_CLOCK\_GROUP\_OFFSET(7) + 2)

[ 61](npcm__clock_8h.md#a4124b07f5ae3f17d7bb2e8f3b12ca6e7)#define NPCM\_CLOCK\_SMB10 (NPCM\_CLOCK\_GROUP\_OFFSET(7) + 3)

[ 62](npcm__clock_8h.md#a290a1b7f611034ada1a8acff7ab7b9f5)#define NPCM\_CLOCK\_SMB11 (NPCM\_CLOCK\_GROUP\_OFFSET(7) + 4)

[ 63](npcm__clock_8h.md#aab56086cca52095241274b00809516fa)#define NPCM\_CLOCK\_SMB12 (NPCM\_CLOCK\_GROUP\_OFFSET(7) + 5)

[ 64](npcm__clock_8h.md#a19a8155a21eae0ee40333fda238d537c)#define NPCM\_CLOCK\_SIOX2 (NPCM\_CLOCK\_GROUP\_OFFSET(7) + 6)

[ 65](npcm__clock_8h.md#ae308b41f2790143c822d731a8be49d95)#define NPCM\_CLOCK\_SIOX1 (NPCM\_CLOCK\_GROUP\_OFFSET(7) + 7)

[ 66](npcm__clock_8h.md#a39eca824a82d5d5f0e702b530670ce31)#define NPCM\_CLOCK\_I3CI2 (NPCM\_CLOCK\_GROUP\_OFFSET(8) + 0)

[ 67](npcm__clock_8h.md#a0fc3291804815adf6f6d1597dfc8e6da)#define NPCM\_CLOCK\_I3CI3 (NPCM\_CLOCK\_GROUP\_OFFSET(8) + 1)

[ 68](npcm__clock_8h.md#a28ec70f9e4b74d67e0c752bf3a6f2a46)#define NPCM\_CLOCK\_I3CI4 (NPCM\_CLOCK\_GROUP\_OFFSET(8) + 2)

[ 69](npcm__clock_8h.md#a838cf34ea43962d47e970ca40bb2b02f)#define NPCM\_CLOCK\_I3CI5 (NPCM\_CLOCK\_GROUP\_OFFSET(8) + 3)

[ 70](npcm__clock_8h.md#af4f55aeda364edb025307aea4fff3431)#define NPCM\_CLOCK\_I3CI6 (NPCM\_CLOCK\_GROUP\_OFFSET(8) + 4)

71

72#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NPCM\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [npcm\_clock.h](npcm__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
