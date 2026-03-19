---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/npcm__clock_8h.html
original_path: doxygen/html/npcm__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npcm\_clock.h File Reference

[Go to the source code of this file.](npcm__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(N) |
| #define | [NPCM\_CLOCK\_PWM\_I](#a63e02592f717f0575db06065c5abf7f9)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 0) |
| #define | [NPCM\_CLOCK\_PWM\_J](#a34ece572167371f620570db82dc99a0e)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 1) |
| #define | [NPCM\_CLOCK\_I3CI](#a67cdf00a70f0ba34a91540895c2b0e77)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 2) |
| #define | [NPCM\_CLOCK\_UART3](#a8070523598b622f82e7c4aa61fa113a2)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 5) |
| #define | [NPCM\_CLOCK\_UART2](#a2595c240f8bd2e046a8b4e06834289bb)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 6) |
| #define | [NPCM\_CLOCK\_SPIM](#a2f2f35b3ac73ed602668b418dbbc6076)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 0) |
| #define | [NPCM\_CLOCK\_FIU](#a7b00badf4c99ff49e9babf170f6213a0)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 2) |
| #define | [NPCM\_CLOCK\_USB20](#afb2fb08d08717664793a3179e87a96c8)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 3) |
| #define | [NPCM\_CLOCK\_UART](#a94aa8507b21fc4fd4d9fd14844f03153)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 4) |
| #define | [NPCM\_CLOCK\_MFT1](#a32de4522569dae6c3b8d5c7d8ea1f705)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 5) |
| #define | [NPCM\_CLOCK\_MFT2](#a011119434180ff4f782a1dada942f1fd)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 6) |
| #define | [NPCM\_CLOCK\_MFT3](#ae6526a686b1a3761dcde981f19469476)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 7) |
| #define | [NPCM\_CLOCK\_PWM\_A](#ae57d8b61165a095ec4b19aaa67b02156)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 0) |
| #define | [NPCM\_CLOCK\_PWM\_B](#acf2e8eefaf16ae166307b5cb0c9706d0)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 1) |
| #define | [NPCM\_CLOCK\_PWM\_C](#a22bd19514fb8140afb3652c1cc131e81)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 2) |
| #define | [NPCM\_CLOCK\_PWM\_D](#afb2ca7ea81c2f43e7576ff80e0aa2b0b)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 3) |
| #define | [NPCM\_CLOCK\_PWM\_E](#afd75d18a0f1f0743625b8114fea9d8dd)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 4) |
| #define | [NPCM\_CLOCK\_PWM\_F](#ae2357132f9cb282171562e8a022c444f)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 5) |
| #define | [NPCM\_CLOCK\_PWM\_G](#a9e3a29585ee19d46f0a59cbd821e1f04)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 6) |
| #define | [NPCM\_CLOCK\_PWM\_H](#a2573f4ffb1e16de8e68cd0ed4da20085)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 7) |
| #define | [NPCM\_CLOCK\_SMB1](#aaba6ccd3affdf2d2e423e8be6f5b4fee)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 0) |
| #define | [NPCM\_CLOCK\_SMB2](#a029f41a64d84585ee2fc8f80d9fc30fb)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 1) |
| #define | [NPCM\_CLOCK\_SMB3](#a556e5bde2edcaacacdfd6cd82fe03efa)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 2) |
| #define | [NPCM\_CLOCK\_SMB4](#acd9b598f8757e298bdbef6b13114099e)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 3) |
| #define | [NPCM\_CLOCK\_SMB5](#a934ed236e7462eedf1e58f98c5e90dfb)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 4) |
| #define | [NPCM\_CLOCK\_SMB6](#a49989ff0da3f5807b7e1a045b1568429)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 5) |
| #define | [NPCM\_CLOCK\_GDMA](#af437c95f765f9060b061ca3511c89dd7)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 7) |
| #define | [NPCM\_CLOCK\_ITIM1](#adc9d8de8a2f2847c66288050cd30a6fd)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 0) |
| #define | [NPCM\_CLOCK\_ITIM2](#a51720bbd7c55c99fbc72adb80a707617)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 1) |
| #define | [NPCM\_CLOCK\_ITIM3](#a41bb9d31b946f991f8c1970674174601)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 2) |
| #define | [NPCM\_CLOCK\_SMB\_DMA](#af96d5c1e939aa5fa9128173d4f545081)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 3) |
| #define | [NPCM\_CLOCK\_ADC](#adf45628a0f330eb1b4d74aab9e9a9ef8)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 4) |
| #define | [NPCM\_CLOCK\_PECI](#ae38fb3273e3a5fcabac782e65533734a)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 5) |
| #define | [NPCM\_CLOCK\_SPIP1](#a8b3833a37e4e09cc75dbdbcfa045d358)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 7) |
| #define | [NPCM\_CLOCK\_UART4](#a1c86b295d71f8fd761f3c8fefd86d3e5)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 0) |
| #define | [NPCM\_CLOCK\_C2HACC](#aa832699b710f1cd9923a76d955ec1339)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 3) |
| #define | [NPCM\_CLOCK\_SHM\_REG](#a443a40fca1ed3567c0c01e3ff339921b)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 4) |
| #define | [NPCM\_CLOCK\_SHM](#adf9c6f59ed292bec420e09a27e9f1dcf)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 5) |
| #define | [NPCM\_CLOCK\_DP80](#a24df8c7fe6d010cf4fc2105d7f9be99f)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 6) |
| #define | [NPCM\_CLOCK\_MSWC](#a3c3df6e489aeb633b6108e1972071495)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 7) |
| #define | [NPCM\_CLOCK\_ITIM4](#a673d71f42575f480d596e2d75c72694d)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 0) |
| #define | [NPCM\_CLOCK\_ITIM5](#a142e5fd523ea4e5a88539e2c90d4cb3a)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 1) |
| #define | [NPCM\_CLOCK\_ITIM6](#ae8d5a71630b1727200508fa785030184)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 2) |
| #define | [NPCM\_CLOCK\_RNG](#aa4641068fa6c9aca20589f682c7e36a8)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 3) |
| #define | [NPCM\_CLOCK\_SHA](#adec2955e9224587cdaa61aa20c6a1b7d)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 5) |
| #define | [NPCM\_CLOCK\_ESPI](#ac24765ff08e97f4747aa34b03e94eab6)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 7) |
| #define | [NPCM\_CLOCK\_SMB7](#a5361334cef2fe6f4a0f93316c9fba60e)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 0) |
| #define | [NPCM\_CLOCK\_SMB8](#afa82d31834ccfb0e1766b4645174aa1b)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 1) |
| #define | [NPCM\_CLOCK\_SMB9](#af6b642aababfe104bdd8bb6a5b6a0673)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 2) |
| #define | [NPCM\_CLOCK\_SMB10](#a4124b07f5ae3f17d7bb2e8f3b12ca6e7)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 3) |
| #define | [NPCM\_CLOCK\_SMB11](#a290a1b7f611034ada1a8acff7ab7b9f5)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 4) |
| #define | [NPCM\_CLOCK\_SMB12](#aab56086cca52095241274b00809516fa)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 5) |
| #define | [NPCM\_CLOCK\_SIOX2](#a19a8155a21eae0ee40333fda238d537c)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 6) |
| #define | [NPCM\_CLOCK\_SIOX1](#ae308b41f2790143c822d731a8be49d95)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 7) |
| #define | [NPCM\_CLOCK\_I3CI2](#a39eca824a82d5d5f0e702b530670ce31)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 0) |
| #define | [NPCM\_CLOCK\_I3CI3](#a0fc3291804815adf6f6d1597dfc8e6da)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 1) |
| #define | [NPCM\_CLOCK\_I3CI4](#a28ec70f9e4b74d67e0c752bf3a6f2a46)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 2) |
| #define | [NPCM\_CLOCK\_I3CI5](#a838cf34ea43962d47e970ca40bb2b02f)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 3) |
| #define | [NPCM\_CLOCK\_I3CI6](#af4f55aeda364edb025307aea4fff3431)   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 4) |

## Macro Definition Documentation

## [◆ ](#adf45628a0f330eb1b4d74aab9e9a9ef8)NPCM\_CLOCK\_ADC

| #define NPCM\_CLOCK\_ADC   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 4) |
| --- |

## [◆ ](#aa832699b710f1cd9923a76d955ec1339)NPCM\_CLOCK\_C2HACC

| #define NPCM\_CLOCK\_C2HACC   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 3) |
| --- |

## [◆ ](#a24df8c7fe6d010cf4fc2105d7f9be99f)NPCM\_CLOCK\_DP80

| #define NPCM\_CLOCK\_DP80   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 6) |
| --- |

## [◆ ](#ac24765ff08e97f4747aa34b03e94eab6)NPCM\_CLOCK\_ESPI

| #define NPCM\_CLOCK\_ESPI   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 7) |
| --- |

## [◆ ](#a7b00badf4c99ff49e9babf170f6213a0)NPCM\_CLOCK\_FIU

| #define NPCM\_CLOCK\_FIU   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 2) |
| --- |

## [◆ ](#af437c95f765f9060b061ca3511c89dd7)NPCM\_CLOCK\_GDMA

| #define NPCM\_CLOCK\_GDMA   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 7) |
| --- |

## [◆ ](#aedf3c4059e2dba237097428dd3d17c86)NPCM\_CLOCK\_GROUP\_OFFSET

| #define NPCM\_CLOCK\_GROUP\_OFFSET | ( |  | *N* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((N) << 3)

## [◆ ](#a67cdf00a70f0ba34a91540895c2b0e77)NPCM\_CLOCK\_I3CI

| #define NPCM\_CLOCK\_I3CI   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 2) |
| --- |

## [◆ ](#a39eca824a82d5d5f0e702b530670ce31)NPCM\_CLOCK\_I3CI2

| #define NPCM\_CLOCK\_I3CI2   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 0) |
| --- |

## [◆ ](#a0fc3291804815adf6f6d1597dfc8e6da)NPCM\_CLOCK\_I3CI3

| #define NPCM\_CLOCK\_I3CI3   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 1) |
| --- |

## [◆ ](#a28ec70f9e4b74d67e0c752bf3a6f2a46)NPCM\_CLOCK\_I3CI4

| #define NPCM\_CLOCK\_I3CI4   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 2) |
| --- |

## [◆ ](#a838cf34ea43962d47e970ca40bb2b02f)NPCM\_CLOCK\_I3CI5

| #define NPCM\_CLOCK\_I3CI5   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 3) |
| --- |

## [◆ ](#af4f55aeda364edb025307aea4fff3431)NPCM\_CLOCK\_I3CI6

| #define NPCM\_CLOCK\_I3CI6   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(8) + 4) |
| --- |

## [◆ ](#adc9d8de8a2f2847c66288050cd30a6fd)NPCM\_CLOCK\_ITIM1

| #define NPCM\_CLOCK\_ITIM1   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 0) |
| --- |

## [◆ ](#a51720bbd7c55c99fbc72adb80a707617)NPCM\_CLOCK\_ITIM2

| #define NPCM\_CLOCK\_ITIM2   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 1) |
| --- |

## [◆ ](#a41bb9d31b946f991f8c1970674174601)NPCM\_CLOCK\_ITIM3

| #define NPCM\_CLOCK\_ITIM3   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 2) |
| --- |

## [◆ ](#a673d71f42575f480d596e2d75c72694d)NPCM\_CLOCK\_ITIM4

| #define NPCM\_CLOCK\_ITIM4   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 0) |
| --- |

## [◆ ](#a142e5fd523ea4e5a88539e2c90d4cb3a)NPCM\_CLOCK\_ITIM5

| #define NPCM\_CLOCK\_ITIM5   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 1) |
| --- |

## [◆ ](#ae8d5a71630b1727200508fa785030184)NPCM\_CLOCK\_ITIM6

| #define NPCM\_CLOCK\_ITIM6   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 2) |
| --- |

## [◆ ](#a32de4522569dae6c3b8d5c7d8ea1f705)NPCM\_CLOCK\_MFT1

| #define NPCM\_CLOCK\_MFT1   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 5) |
| --- |

## [◆ ](#a011119434180ff4f782a1dada942f1fd)NPCM\_CLOCK\_MFT2

| #define NPCM\_CLOCK\_MFT2   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 6) |
| --- |

## [◆ ](#ae6526a686b1a3761dcde981f19469476)NPCM\_CLOCK\_MFT3

| #define NPCM\_CLOCK\_MFT3   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 7) |
| --- |

## [◆ ](#a3c3df6e489aeb633b6108e1972071495)NPCM\_CLOCK\_MSWC

| #define NPCM\_CLOCK\_MSWC   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 7) |
| --- |

## [◆ ](#ae38fb3273e3a5fcabac782e65533734a)NPCM\_CLOCK\_PECI

| #define NPCM\_CLOCK\_PECI   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 5) |
| --- |

## [◆ ](#ae57d8b61165a095ec4b19aaa67b02156)NPCM\_CLOCK\_PWM\_A

| #define NPCM\_CLOCK\_PWM\_A   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 0) |
| --- |

## [◆ ](#acf2e8eefaf16ae166307b5cb0c9706d0)NPCM\_CLOCK\_PWM\_B

| #define NPCM\_CLOCK\_PWM\_B   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 1) |
| --- |

## [◆ ](#a22bd19514fb8140afb3652c1cc131e81)NPCM\_CLOCK\_PWM\_C

| #define NPCM\_CLOCK\_PWM\_C   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 2) |
| --- |

## [◆ ](#afb2ca7ea81c2f43e7576ff80e0aa2b0b)NPCM\_CLOCK\_PWM\_D

| #define NPCM\_CLOCK\_PWM\_D   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 3) |
| --- |

## [◆ ](#afd75d18a0f1f0743625b8114fea9d8dd)NPCM\_CLOCK\_PWM\_E

| #define NPCM\_CLOCK\_PWM\_E   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 4) |
| --- |

## [◆ ](#ae2357132f9cb282171562e8a022c444f)NPCM\_CLOCK\_PWM\_F

| #define NPCM\_CLOCK\_PWM\_F   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 5) |
| --- |

## [◆ ](#a9e3a29585ee19d46f0a59cbd821e1f04)NPCM\_CLOCK\_PWM\_G

| #define NPCM\_CLOCK\_PWM\_G   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 6) |
| --- |

## [◆ ](#a2573f4ffb1e16de8e68cd0ed4da20085)NPCM\_CLOCK\_PWM\_H

| #define NPCM\_CLOCK\_PWM\_H   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(2) + 7) |
| --- |

## [◆ ](#a63e02592f717f0575db06065c5abf7f9)NPCM\_CLOCK\_PWM\_I

| #define NPCM\_CLOCK\_PWM\_I   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 0) |
| --- |

## [◆ ](#a34ece572167371f620570db82dc99a0e)NPCM\_CLOCK\_PWM\_J

| #define NPCM\_CLOCK\_PWM\_J   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 1) |
| --- |

## [◆ ](#aa4641068fa6c9aca20589f682c7e36a8)NPCM\_CLOCK\_RNG

| #define NPCM\_CLOCK\_RNG   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 3) |
| --- |

## [◆ ](#adec2955e9224587cdaa61aa20c6a1b7d)NPCM\_CLOCK\_SHA

| #define NPCM\_CLOCK\_SHA   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(6) + 5) |
| --- |

## [◆ ](#adf9c6f59ed292bec420e09a27e9f1dcf)NPCM\_CLOCK\_SHM

| #define NPCM\_CLOCK\_SHM   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 5) |
| --- |

## [◆ ](#a443a40fca1ed3567c0c01e3ff339921b)NPCM\_CLOCK\_SHM\_REG

| #define NPCM\_CLOCK\_SHM\_REG   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 4) |
| --- |

## [◆ ](#ae308b41f2790143c822d731a8be49d95)NPCM\_CLOCK\_SIOX1

| #define NPCM\_CLOCK\_SIOX1   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 7) |
| --- |

## [◆ ](#a19a8155a21eae0ee40333fda238d537c)NPCM\_CLOCK\_SIOX2

| #define NPCM\_CLOCK\_SIOX2   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 6) |
| --- |

## [◆ ](#aaba6ccd3affdf2d2e423e8be6f5b4fee)NPCM\_CLOCK\_SMB1

| #define NPCM\_CLOCK\_SMB1   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 0) |
| --- |

## [◆ ](#a4124b07f5ae3f17d7bb2e8f3b12ca6e7)NPCM\_CLOCK\_SMB10

| #define NPCM\_CLOCK\_SMB10   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 3) |
| --- |

## [◆ ](#a290a1b7f611034ada1a8acff7ab7b9f5)NPCM\_CLOCK\_SMB11

| #define NPCM\_CLOCK\_SMB11   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 4) |
| --- |

## [◆ ](#aab56086cca52095241274b00809516fa)NPCM\_CLOCK\_SMB12

| #define NPCM\_CLOCK\_SMB12   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 5) |
| --- |

## [◆ ](#a029f41a64d84585ee2fc8f80d9fc30fb)NPCM\_CLOCK\_SMB2

| #define NPCM\_CLOCK\_SMB2   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 1) |
| --- |

## [◆ ](#a556e5bde2edcaacacdfd6cd82fe03efa)NPCM\_CLOCK\_SMB3

| #define NPCM\_CLOCK\_SMB3   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 2) |
| --- |

## [◆ ](#acd9b598f8757e298bdbef6b13114099e)NPCM\_CLOCK\_SMB4

| #define NPCM\_CLOCK\_SMB4   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 3) |
| --- |

## [◆ ](#a934ed236e7462eedf1e58f98c5e90dfb)NPCM\_CLOCK\_SMB5

| #define NPCM\_CLOCK\_SMB5   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 4) |
| --- |

## [◆ ](#a49989ff0da3f5807b7e1a045b1568429)NPCM\_CLOCK\_SMB6

| #define NPCM\_CLOCK\_SMB6   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(3) + 5) |
| --- |

## [◆ ](#a5361334cef2fe6f4a0f93316c9fba60e)NPCM\_CLOCK\_SMB7

| #define NPCM\_CLOCK\_SMB7   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 0) |
| --- |

## [◆ ](#afa82d31834ccfb0e1766b4645174aa1b)NPCM\_CLOCK\_SMB8

| #define NPCM\_CLOCK\_SMB8   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 1) |
| --- |

## [◆ ](#af6b642aababfe104bdd8bb6a5b6a0673)NPCM\_CLOCK\_SMB9

| #define NPCM\_CLOCK\_SMB9   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(7) + 2) |
| --- |

## [◆ ](#af96d5c1e939aa5fa9128173d4f545081)NPCM\_CLOCK\_SMB\_DMA

| #define NPCM\_CLOCK\_SMB\_DMA   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 3) |
| --- |

## [◆ ](#a2f2f35b3ac73ed602668b418dbbc6076)NPCM\_CLOCK\_SPIM

| #define NPCM\_CLOCK\_SPIM   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 0) |
| --- |

## [◆ ](#a8b3833a37e4e09cc75dbdbcfa045d358)NPCM\_CLOCK\_SPIP1

| #define NPCM\_CLOCK\_SPIP1   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(4) + 7) |
| --- |

## [◆ ](#a94aa8507b21fc4fd4d9fd14844f03153)NPCM\_CLOCK\_UART

| #define NPCM\_CLOCK\_UART   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 4) |
| --- |

## [◆ ](#a2595c240f8bd2e046a8b4e06834289bb)NPCM\_CLOCK\_UART2

| #define NPCM\_CLOCK\_UART2   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 6) |
| --- |

## [◆ ](#a8070523598b622f82e7c4aa61fa113a2)NPCM\_CLOCK\_UART3

| #define NPCM\_CLOCK\_UART3   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(0) + 5) |
| --- |

## [◆ ](#a1c86b295d71f8fd761f3c8fefd86d3e5)NPCM\_CLOCK\_UART4

| #define NPCM\_CLOCK\_UART4   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(5) + 0) |
| --- |

## [◆ ](#afb2fb08d08717664793a3179e87a96c8)NPCM\_CLOCK\_USB20

| #define NPCM\_CLOCK\_USB20   ([NPCM\_CLOCK\_GROUP\_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)(1) + 3) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [npcm\_clock.h](npcm__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
