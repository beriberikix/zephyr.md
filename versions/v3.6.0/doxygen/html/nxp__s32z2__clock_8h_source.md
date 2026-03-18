---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nxp__s32z2__clock_8h_source.html
original_path: doxygen/html/nxp__s32z2__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_s32z2\_clock.h

[Go to the documentation of this file.](nxp__s32z2__clock_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32Z2\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32Z2\_CLOCK\_H\_

9

[ 10](nxp__s32z2__clock_8h.md#a8f4673a159fb26c90ae29761784395e9)#define NXP\_S32\_FIRC\_CLK 1U

[ 11](nxp__s32z2__clock_8h.md#ab748e7ec615dc5fe10cafc723cc289fe)#define NXP\_S32\_FXOSC\_CLK 2U

[ 12](nxp__s32z2__clock_8h.md#adc1da7bf433a80a3a975e172a30abbbc)#define NXP\_S32\_SIRC\_CLK 3U

[ 13](nxp__s32z2__clock_8h.md#a3adcd5e43f56ff0c41093ae141efac06)#define NXP\_S32\_COREPLL\_CLK 4U

[ 14](nxp__s32z2__clock_8h.md#a64b593be74cbcacec88f6f4aa513e959)#define NXP\_S32\_PERIPHPLL\_CLK 5U

[ 15](nxp__s32z2__clock_8h.md#a7cb52f27a12b3f96f09eb351d93132cb)#define NXP\_S32\_DDRPLL\_CLK 6U

[ 16](nxp__s32z2__clock_8h.md#a2cb385d2116bc56f05be3bde7b83e718)#define NXP\_S32\_LFAST0\_PLL\_CLK 7U

[ 17](nxp__s32z2__clock_8h.md#a2bce68111fdacf004a33b94c0c898c02)#define NXP\_S32\_LFAST1\_PLL\_CLK 8U

[ 18](nxp__s32z2__clock_8h.md#acf8fe39109c8d74a1ed277866460b3fb)#define NXP\_S32\_COREPLL\_PHI0\_CLK 9U

[ 19](nxp__s32z2__clock_8h.md#a3aed8d0791095ec97ec68dd5a31d5a16)#define NXP\_S32\_COREPLL\_DFS0\_CLK 10U

[ 20](nxp__s32z2__clock_8h.md#ada9b9b2fcb4e577e0c04b5ec841cc73a)#define NXP\_S32\_COREPLL\_DFS1\_CLK 11U

[ 21](nxp__s32z2__clock_8h.md#a1012a8d0b7baf417fede47e819ac03bc)#define NXP\_S32\_COREPLL\_DFS2\_CLK 12U

[ 22](nxp__s32z2__clock_8h.md#a1e2cb85e953429dfd3b18af9c67a45ce)#define NXP\_S32\_COREPLL\_DFS3\_CLK 13U

[ 23](nxp__s32z2__clock_8h.md#a50c5562659befb1e3a6633ca5f383265)#define NXP\_S32\_COREPLL\_DFS4\_CLK 14U

[ 24](nxp__s32z2__clock_8h.md#a52c61d4e6b7907dcf5478c347cfc2f88)#define NXP\_S32\_COREPLL\_DFS5\_CLK 15U

[ 25](nxp__s32z2__clock_8h.md#aa786b49d448f96193ccf372ed28b8892)#define NXP\_S32\_PERIPHPLL\_PHI0\_CLK 16U

[ 26](nxp__s32z2__clock_8h.md#a7c956a57231bdbe242b41fbf837512d7)#define NXP\_S32\_PERIPHPLL\_PHI1\_CLK 17U

[ 27](nxp__s32z2__clock_8h.md#a5a42cf11ac2ba5bfb697be28b3f7868c)#define NXP\_S32\_PERIPHPLL\_PHI2\_CLK 18U

[ 28](nxp__s32z2__clock_8h.md#ae3ecaa42d02bbdefe504c62d3dc3d5b3)#define NXP\_S32\_PERIPHPLL\_PHI3\_CLK 19U

[ 29](nxp__s32z2__clock_8h.md#a2550e0d2500a0c7d6a9af4aee6d2c0fb)#define NXP\_S32\_PERIPHPLL\_PHI4\_CLK 20U

[ 30](nxp__s32z2__clock_8h.md#acf1ad3c3de2d0f3db3110907b3a7f5de)#define NXP\_S32\_PERIPHPLL\_PHI5\_CLK 21U

[ 31](nxp__s32z2__clock_8h.md#afcea8aabd3d25ae13be9e50fa8c84b12)#define NXP\_S32\_PERIPHPLL\_PHI6\_CLK 22U

[ 32](nxp__s32z2__clock_8h.md#a6d1b5a86631e390202f9b02554815468)#define NXP\_S32\_PERIPHPLL\_DFS0\_CLK 23U

[ 33](nxp__s32z2__clock_8h.md#a2e3dc5289e03199416edfd3df835f183)#define NXP\_S32\_PERIPHPLL\_DFS1\_CLK 24U

[ 34](nxp__s32z2__clock_8h.md#a9a5e64bade06d1ee1202b61387d8a17c)#define NXP\_S32\_PERIPHPLL\_DFS2\_CLK 25U

[ 35](nxp__s32z2__clock_8h.md#ad282337933262b0c42430b35a33d7507)#define NXP\_S32\_PERIPHPLL\_DFS3\_CLK 26U

[ 36](nxp__s32z2__clock_8h.md#a594165bad79d57a3efce555cb9ac5bff)#define NXP\_S32\_PERIPHPLL\_DFS4\_CLK 27U

[ 37](nxp__s32z2__clock_8h.md#aba43a681b81004967aa5827c55b24a5d)#define NXP\_S32\_PERIPHPLL\_DFS5\_CLK 28U

[ 38](nxp__s32z2__clock_8h.md#a6bc7d24858e5aacb50495395ca368695)#define NXP\_S32\_DDRPLL\_PHI0\_CLK 29U

[ 39](nxp__s32z2__clock_8h.md#aaf01394fcd23fdcff4792684b1a970d8)#define NXP\_S32\_LFAST0\_PLL\_PH0\_CLK 30U

[ 40](nxp__s32z2__clock_8h.md#a3d00b3751ab9bccaf4471bfab3d5d522)#define NXP\_S32\_LFAST1\_PLL\_PH0\_CLK 31U

[ 41](nxp__s32z2__clock_8h.md#a25c75209f8f1f75734aede68aa358744)#define NXP\_S32\_ETH\_RGMII\_REF\_CLK 32U

[ 42](nxp__s32z2__clock_8h.md#a9540744a0ace0989f2c3cc968f3713af)#define NXP\_S32\_TMR\_1588\_CLK 33U

[ 43](nxp__s32z2__clock_8h.md#a12a72ae64ce2fca3bb59cbddde7f8ae4)#define NXP\_S32\_ETH0\_EXT\_RX\_CLK 34U

[ 44](nxp__s32z2__clock_8h.md#a564bf352a181cf965b34b5da9b00a18d)#define NXP\_S32\_ETH0\_EXT\_TX\_CLK 35U

[ 45](nxp__s32z2__clock_8h.md#a4e3c08a9d415372a3884f8e1658f4de3)#define NXP\_S32\_ETH1\_EXT\_RX\_CLK 36U

[ 46](nxp__s32z2__clock_8h.md#a5e2a62c4e47330fcd4d9e380ed0107ea)#define NXP\_S32\_ETH1\_EXT\_TX\_CLK 37U

[ 47](nxp__s32z2__clock_8h.md#a08658b7dbf05f325c8dcad2f609b714d)#define NXP\_S32\_LFAST0\_EXT\_REF\_CLK 38U

[ 48](nxp__s32z2__clock_8h.md#a84b1c38882e6af516c04909671427d4a)#define NXP\_S32\_LFAST1\_EXT\_REF\_CLK 39U

[ 49](nxp__s32z2__clock_8h.md#a28cbe95441f2e1691795ca86d29e5c0f)#define NXP\_S32\_DDR\_CLK 40U

[ 50](nxp__s32z2__clock_8h.md#abc6c662bf88c9a922478bf368ef7416c)#define NXP\_S32\_P0\_SYS\_CLK 41U

[ 51](nxp__s32z2__clock_8h.md#ab65e705e34df2a7428493b1c232fc6fd)#define NXP\_S32\_P1\_SYS\_CLK 42U

[ 52](nxp__s32z2__clock_8h.md#a4e44f6e2575430b847296bb0336a555f)#define NXP\_S32\_P1\_SYS\_DIV2\_CLK 43U

[ 53](nxp__s32z2__clock_8h.md#a725ad3fb6496a459f4719f64658478a1)#define NXP\_S32\_P1\_SYS\_DIV4\_CLK 44U

[ 54](nxp__s32z2__clock_8h.md#aa5d06e65e92b43483cecfa7608abb8d6)#define NXP\_S32\_P2\_SYS\_CLK 45U

[ 55](nxp__s32z2__clock_8h.md#ac66e693079884870e56f2b380a55eaed)#define NXP\_S32\_CORE\_M33\_CLK 46U

[ 56](nxp__s32z2__clock_8h.md#a0f5ffbc3acf02add006d35efa94ca3a6)#define NXP\_S32\_P2\_SYS\_DIV2\_CLK 47U

[ 57](nxp__s32z2__clock_8h.md#abb48ce40572d7f0f174b644930d949cc)#define NXP\_S32\_P2\_SYS\_DIV4\_CLK 48U

[ 58](nxp__s32z2__clock_8h.md#a5557d1a39d866ddc1e7baa7c8e6ff9f0)#define NXP\_S32\_P3\_SYS\_CLK 49U

[ 59](nxp__s32z2__clock_8h.md#ab6eb18cde38b8ca9dfa2b7181c41d6c0)#define NXP\_S32\_CE\_SYS\_DIV2\_CLK 50U

[ 60](nxp__s32z2__clock_8h.md#a65a5ce3703f0c3c99e85654004783e88)#define NXP\_S32\_CE\_SYS\_DIV4\_CLK 51U

[ 61](nxp__s32z2__clock_8h.md#a47d136a5e21ff3031bd7b9eb0075d8f6)#define NXP\_S32\_P3\_SYS\_DIV2\_NOC\_CLK 52U

[ 62](nxp__s32z2__clock_8h.md#a07633bb8f64c1125935a2b28ad5bf485)#define NXP\_S32\_P3\_SYS\_DIV4\_CLK 53U

[ 63](nxp__s32z2__clock_8h.md#ac81524f01ee44bab50879663fc242211)#define NXP\_S32\_P4\_SYS\_CLK 54U

[ 64](nxp__s32z2__clock_8h.md#ac2cd9425cd2eb8e8c29d5716259034df)#define NXP\_S32\_P4\_SYS\_DIV2\_CLK 55U

[ 65](nxp__s32z2__clock_8h.md#af36e2f8d5d39189013c65589eaaf3da2)#define NXP\_S32\_HSE\_SYS\_DIV2\_CLK 56U

[ 66](nxp__s32z2__clock_8h.md#a8fdb0b99d90aa47b3a16aa8df92a23ba)#define NXP\_S32\_P5\_SYS\_CLK 57U

[ 67](nxp__s32z2__clock_8h.md#ad324b9f48cffa750d35a1b3625e41d78)#define NXP\_S32\_P5\_SYS\_DIV2\_CLK 58U

[ 68](nxp__s32z2__clock_8h.md#afa536c5aa9044ad45772be1330568ef5)#define NXP\_S32\_P5\_SYS\_DIV4\_CLK 59U

[ 69](nxp__s32z2__clock_8h.md#afdd0087c9c7473debe2c36f9c4b3b9eb)#define NXP\_S32\_P2\_MATH\_CLK 60U

[ 70](nxp__s32z2__clock_8h.md#a43b5a621c2e3a2ed9b3b5b6a5742c5fa)#define NXP\_S32\_P2\_MATH\_DIV3\_CLK 61U

[ 71](nxp__s32z2__clock_8h.md#a8eca101146810d0b95493c66a19b7b16)#define NXP\_S32\_GLB\_LBIST\_CLK 62U

[ 72](nxp__s32z2__clock_8h.md#a480e71b89b05bc9e36526d87a995d0df)#define NXP\_S32\_RTU0\_CORE\_CLK 63U

[ 73](nxp__s32z2__clock_8h.md#a29df359bdd3589eedc4d973619789304)#define NXP\_S32\_RTU0\_CORE\_DIV2\_CLK 64U

[ 74](nxp__s32z2__clock_8h.md#aa1497392847306b62614e7c3b653048f)#define NXP\_S32\_RTU1\_CORE\_CLK 65U

[ 75](nxp__s32z2__clock_8h.md#adbce190d535e203b6a3d04369a316d4e)#define NXP\_S32\_RTU1\_CORE\_DIV2\_CLK 66U

[ 76](nxp__s32z2__clock_8h.md#a522a9b1e7ba5816155bf057ffbb4f2fe)#define NXP\_S32\_P0\_PSI5\_S\_UTIL\_CLK 67U

[ 77](nxp__s32z2__clock_8h.md#ad0e0022e42d0b941e0edd976837d1b00)#define NXP\_S32\_P4\_PSI5\_S\_UTIL\_CLK 68U

[ 78](nxp__s32z2__clock_8h.md#a89fe6bb1365a3895449da72ccd517223)#define NXP\_S32\_ADC0\_CLK 70U

[ 79](nxp__s32z2__clock_8h.md#ace9575b4ed012fe344884b0b1fa2ef58)#define NXP\_S32\_ADC1\_CLK 71U

[ 80](nxp__s32z2__clock_8h.md#ac81ef4f7bd981576b69426f195b010e3)#define NXP\_S32\_CE\_EDMA\_CLK 72U

[ 81](nxp__s32z2__clock_8h.md#a896f8242ee6ca821d912706775169ff4)#define NXP\_S32\_CE\_PIT0\_CLK 73U

[ 82](nxp__s32z2__clock_8h.md#a8fa4590c34477b07d6d902db44a28387)#define NXP\_S32\_CE\_PIT1\_CLK 74U

[ 83](nxp__s32z2__clock_8h.md#a02ddfc31f0ec38b341adb47bbfcfe43b)#define NXP\_S32\_CE\_PIT2\_CLK 75U

[ 84](nxp__s32z2__clock_8h.md#a7ad3dabd64d6358362e3ce6102542709)#define NXP\_S32\_CE\_PIT3\_CLK 76U

[ 85](nxp__s32z2__clock_8h.md#aa162dfc6ae281d398bd30efbb9d23eeb)#define NXP\_S32\_CE\_PIT4\_CLK 77U

[ 86](nxp__s32z2__clock_8h.md#a6bc8443e520ace278124978cc00080d6)#define NXP\_S32\_CE\_PIT5\_CLK 78U

[ 87](nxp__s32z2__clock_8h.md#a63aca9fbcdae28cd448e62e9dcf41da9)#define NXP\_S32\_CLKOUT0\_CLK 79U

[ 88](nxp__s32z2__clock_8h.md#aed622cb6ba9b009aa0913c0e7d8f727f)#define NXP\_S32\_CLKOUT1\_CLK 80U

[ 89](nxp__s32z2__clock_8h.md#a93cd425d58dd7d2ef73139487816b0f2)#define NXP\_S32\_CLKOUT2\_CLK 81U

[ 90](nxp__s32z2__clock_8h.md#a24fc740cdbf049289b845e7c57f3653b)#define NXP\_S32\_CLKOUT3\_CLK 82U

[ 91](nxp__s32z2__clock_8h.md#a0218b218e1ea001888490a74e824c5fa)#define NXP\_S32\_CLKOUT4\_CLK 83U

[ 92](nxp__s32z2__clock_8h.md#a31bde6eec68fcfd8e76a497363276288)#define NXP\_S32\_CTU\_CLK 84U

[ 93](nxp__s32z2__clock_8h.md#abf95474bbeb9969a520edd298172941e)#define NXP\_S32\_DMACRC0\_CLK 85U

[ 94](nxp__s32z2__clock_8h.md#a0960ae83fd592bd62c12dbffb212f02a)#define NXP\_S32\_DMACRC1\_CLK 86U

[ 95](nxp__s32z2__clock_8h.md#aa486c18a096eebeec8afeb4d1ac98e91)#define NXP\_S32\_DMACRC4\_CLK 87U

[ 96](nxp__s32z2__clock_8h.md#a7ed644aafa5cec6aa0ad1521c29d9589)#define NXP\_S32\_DMACRC5\_CLK 88U

[ 97](nxp__s32z2__clock_8h.md#a97a3ff5238f4878784ee1bee4cfc7522)#define NXP\_S32\_DMAMUX0\_CLK 89U

[ 98](nxp__s32z2__clock_8h.md#a708913d2bb71ec975caad705a10b8421)#define NXP\_S32\_DMAMUX1\_CLK 90U

[ 99](nxp__s32z2__clock_8h.md#ae0650d4cdd3cca6a08666f0a0173a567)#define NXP\_S32\_DMAMUX4\_CLK 91U

[ 100](nxp__s32z2__clock_8h.md#ad6fd147a074209f370ff0761b49c64a2)#define NXP\_S32\_DMAMUX5\_CLK 92U

[ 101](nxp__s32z2__clock_8h.md#ae8b13f1f1803f214f7c7ba371679ee6f)#define NXP\_S32\_EDMA0\_CLK 93U

[ 102](nxp__s32z2__clock_8h.md#a572adbd504ff44b0756578d38d8a9a7e)#define NXP\_S32\_EDMA1\_CLK 94U

[ 103](nxp__s32z2__clock_8h.md#adc7573ce484dfda1662645ee5b959d86)#define NXP\_S32\_EDMA3\_CLK 95U

[ 104](nxp__s32z2__clock_8h.md#a70e0508f328066120600422e31dd9bd6)#define NXP\_S32\_EDMA4\_CLK 96U

[ 105](nxp__s32z2__clock_8h.md#ada44bb4bde41cfae4cbb5a30e615c27f)#define NXP\_S32\_EDMA5\_CLK 97U

[ 106](nxp__s32z2__clock_8h.md#ac6cae2e8c1e0e49d24143da01bedbfd4)#define NXP\_S32\_ETH0\_TX\_MII\_CLK 98U

[ 107](nxp__s32z2__clock_8h.md#a42812f12a9d19b18a532ab3609829aa1)#define NXP\_S32\_ENET0\_CLK 99U

[ 108](nxp__s32z2__clock_8h.md#af42ddf0adf09c31916350082dc472cba)#define NXP\_S32\_P3\_CAN\_PE\_CLK 100U

[ 109](nxp__s32z2__clock_8h.md#a308e74a366725070c56a4ab4fc7c300a)#define NXP\_S32\_FLEXCAN0\_CLK 101U

[ 110](nxp__s32z2__clock_8h.md#ad353c07d914cfa8c45ed3b7b586c2b00)#define NXP\_S32\_FLEXCAN1\_CLK 102U

[ 111](nxp__s32z2__clock_8h.md#a54467688a58d9be77849eddd031f126e)#define NXP\_S32\_FLEXCAN2\_CLK 103U

[ 112](nxp__s32z2__clock_8h.md#a0fcf00296138cd26e845ab524054fd3b)#define NXP\_S32\_FLEXCAN3\_CLK 104U

[ 113](nxp__s32z2__clock_8h.md#a6106f0f8b5e0f5230b75e43b5ccdbf0e)#define NXP\_S32\_FLEXCAN4\_CLK 105U

[ 114](nxp__s32z2__clock_8h.md#a4f3b1864f3f5bcc6a1fd66e27eb12a52)#define NXP\_S32\_FLEXCAN5\_CLK 106U

[ 115](nxp__s32z2__clock_8h.md#aab3b5b178be344b18c4c9ca27786eb03)#define NXP\_S32\_FLEXCAN6\_CLK 107U

[ 116](nxp__s32z2__clock_8h.md#a5c239f32216a44b5282e5ffd9fdd214f)#define NXP\_S32\_FLEXCAN7\_CLK 108U

[ 117](nxp__s32z2__clock_8h.md#afb62f9c88f6652a3382197c10456c8b9)#define NXP\_S32\_FLEXCAN8\_CLK 109U

[ 118](nxp__s32z2__clock_8h.md#a3f8baea9230234e8e9dafdbe1dadc005)#define NXP\_S32\_FLEXCAN9\_CLK 110U

[ 119](nxp__s32z2__clock_8h.md#a8fff5e2c245578e94f4e9ed4eddfc19b)#define NXP\_S32\_FLEXCAN10\_CLK 111U

[ 120](nxp__s32z2__clock_8h.md#a875232291fcb4035ea178013d1996300)#define NXP\_S32\_FLEXCAN11\_CLK 112U

[ 121](nxp__s32z2__clock_8h.md#a0149861a754ec061781b59813e9bb5ea)#define NXP\_S32\_FLEXCAN12\_CLK 113U

[ 122](nxp__s32z2__clock_8h.md#af92372e349573e82108e2d858d7bed52)#define NXP\_S32\_FLEXCAN13\_CLK 114U

[ 123](nxp__s32z2__clock_8h.md#adc7b3ae5cfc1fe779b0075626fae2328)#define NXP\_S32\_FLEXCAN14\_CLK 115U

[ 124](nxp__s32z2__clock_8h.md#a55351634b1b77419c5f2aeccdd917ebe)#define NXP\_S32\_FLEXCAN15\_CLK 116U

[ 125](nxp__s32z2__clock_8h.md#aa95b2f2eceb55537b99e6a14f84f17d1)#define NXP\_S32\_FLEXCAN16\_CLK 117U

[ 126](nxp__s32z2__clock_8h.md#acaed7d12a46279f9a3a5af4fde4e5693)#define NXP\_S32\_FLEXCAN17\_CLK 118U

[ 127](nxp__s32z2__clock_8h.md#a204e919465814538dd49dd775eb2f8f6)#define NXP\_S32\_FLEXCAN18\_CLK 119U

[ 128](nxp__s32z2__clock_8h.md#a3421175f2c69e71bfa90cf8b34e69c5b)#define NXP\_S32\_FLEXCAN19\_CLK 120U

[ 129](nxp__s32z2__clock_8h.md#a4f44e36a65a4e2422fd3b72e246b7170)#define NXP\_S32\_FLEXCAN20\_CLK 121U

[ 130](nxp__s32z2__clock_8h.md#a9c6e9291e6d310a4a41f0ea3d6810b79)#define NXP\_S32\_FLEXCAN21\_CLK 122U

[ 131](nxp__s32z2__clock_8h.md#a0890c9d64890e95b8de85914eb773986)#define NXP\_S32\_FLEXCAN22\_CLK 123U

[ 132](nxp__s32z2__clock_8h.md#a98a67a530a8ab4602974248029953934)#define NXP\_S32\_FLEXCAN23\_CLK 124U

[ 133](nxp__s32z2__clock_8h.md#a359bad70140a01914fbb90541c178226)#define NXP\_S32\_P0\_FR\_PE\_CLK 125U

[ 134](nxp__s32z2__clock_8h.md#ae1a59aa87c82395e1badae9f62a8345a)#define NXP\_S32\_FRAY0\_CLK 126U

[ 135](nxp__s32z2__clock_8h.md#abe6b9172ef85c386ab5ad017533ba1ee)#define NXP\_S32\_FRAY1\_CLK 127U

[ 136](nxp__s32z2__clock_8h.md#af5f8881fdd6fc0b160ecbbccfc34df88)#define NXP\_S32\_GTM\_CLK 128U

[ 137](nxp__s32z2__clock_8h.md#afa13966ea5003a4018851341485db5c7)#define NXP\_S32\_IIIC0\_CLK 129U

[ 138](nxp__s32z2__clock_8h.md#ac18c5d32153412256754f0a8871a3613)#define NXP\_S32\_IIIC1\_CLK 130U

[ 139](nxp__s32z2__clock_8h.md#a56d46603e3275969d77401c2404f1105)#define NXP\_S32\_IIIC2\_CLK 131U

[ 140](nxp__s32z2__clock_8h.md#a71af2c2cf427a16f1b8d0d1ef6d5c5c5)#define NXP\_S32\_P0\_LIN\_BAUD\_CLK 132U

[ 141](nxp__s32z2__clock_8h.md#ab398d341ee088a2913a096ec2b9b6545)#define NXP\_S32\_LIN0\_CLK 133U

[ 142](nxp__s32z2__clock_8h.md#ae4867ba422c49414a6e32b7170f19398)#define NXP\_S32\_LIN1\_CLK 134U

[ 143](nxp__s32z2__clock_8h.md#a7138bcb68270ae9f46539ffc65cd34dd)#define NXP\_S32\_LIN2\_CLK 135U

[ 144](nxp__s32z2__clock_8h.md#a9b0b135bf98d9982e26547801c0452cd)#define NXP\_S32\_P1\_LIN\_BAUD\_CLK 136U

[ 145](nxp__s32z2__clock_8h.md#aae3a89eaeca09ae97ad3ba0132632b7b)#define NXP\_S32\_LIN3\_CLK 137U

[ 146](nxp__s32z2__clock_8h.md#a0953f6ad3c2f2f84a82927d8ed979d2e)#define NXP\_S32\_LIN4\_CLK 138U

[ 147](nxp__s32z2__clock_8h.md#a2f1405a5d9a3e3e03d2b607f064c9c49)#define NXP\_S32\_LIN5\_CLK 139U

[ 148](nxp__s32z2__clock_8h.md#a34da0d2172d9eff2f9edf40e980bd980)#define NXP\_S32\_P4\_LIN\_BAUD\_CLK 140U

[ 149](nxp__s32z2__clock_8h.md#a8f0dc1e8fa2449e42f1e1371ed3526bc)#define NXP\_S32\_LIN6\_CLK 141U

[ 150](nxp__s32z2__clock_8h.md#a0e14ecb12403a221a992eb6f6970d324)#define NXP\_S32\_LIN7\_CLK 142U

[ 151](nxp__s32z2__clock_8h.md#a6d8815173be045f717ee61f5770dd2ca)#define NXP\_S32\_LIN8\_CLK 143U

[ 152](nxp__s32z2__clock_8h.md#a5e3508c56acc88ca6a4fb04f5b59f7bc)#define NXP\_S32\_P5\_LIN\_BAUD\_CLK 144U

[ 153](nxp__s32z2__clock_8h.md#a3d55f195f31e6fdfeecdb2d712564e82)#define NXP\_S32\_LIN9\_CLK 145U

[ 154](nxp__s32z2__clock_8h.md#a926d082c5223bcdc027e220190ec2e41)#define NXP\_S32\_LIN10\_CLK 146U

[ 155](nxp__s32z2__clock_8h.md#a9475a59878a242d95a90c69c1e5b78d9)#define NXP\_S32\_LIN11\_CLK 147U

[ 156](nxp__s32z2__clock_8h.md#ad98b9a2b348c6e58f41420a47a5e2ba8)#define NXP\_S32\_MSCDSPI\_CLK 148U

[ 157](nxp__s32z2__clock_8h.md#a0d21ae71b95bcfc407f67053dd202288)#define NXP\_S32\_MSCLIN\_CLK 149U

[ 158](nxp__s32z2__clock_8h.md#a962245016be6213059cefaabe2c5d96e)#define NXP\_S32\_NANO\_CLK 150U

[ 159](nxp__s32z2__clock_8h.md#ab82b29897283f400bd543368f8b1fc73)#define NXP\_S32\_P0\_CLKOUT\_SRC\_CLK 151U

[ 160](nxp__s32z2__clock_8h.md#af80cf625f75ceb16fabb4f3a52e8154c)#define NXP\_S32\_P0\_CTU\_PER\_CLK 152U

[ 161](nxp__s32z2__clock_8h.md#a714fae0bdcbe4980f167cb222d008da5)#define NXP\_S32\_P0\_DSPI\_MSC\_CLK 153U

[ 162](nxp__s32z2__clock_8h.md#a16ffc4b60ef57064c790dbe9c0bca6b9)#define NXP\_S32\_P0\_EMIOS\_LCU\_CLK 154U

[ 163](nxp__s32z2__clock_8h.md#a686525770665c07bd423523d3a36b3ac)#define NXP\_S32\_P0\_GTM\_CLK 155U

[ 164](nxp__s32z2__clock_8h.md#afbdfad00c82da171e55148b6239e42d3)#define NXP\_S32\_P0\_GTM\_NOC\_CLK 156U

[ 165](nxp__s32z2__clock_8h.md#a23a8ea48e3fd40e86ba10a26c50729cb)#define NXP\_S32\_P0\_GTM\_TS\_CLK 157U

[ 166](nxp__s32z2__clock_8h.md#a25b98ce36a908555b566240eef0eeb32)#define NXP\_S32\_P0\_LIN\_CLK 158U

[ 167](nxp__s32z2__clock_8h.md#a58a1b67087d393bcd87aa1021a602610)#define NXP\_S32\_P0\_NANO\_CLK 159U

[ 168](nxp__s32z2__clock_8h.md#ad26f0c08b0ba71b1322bd0d96f39d088)#define NXP\_S32\_P0\_PSI5\_125K\_CLK 160U

[ 169](nxp__s32z2__clock_8h.md#a26c4eb3cc201d79da9e694fc9978db99)#define NXP\_S32\_P0\_PSI5\_189K\_CLK 161U

[ 170](nxp__s32z2__clock_8h.md#a459ee3a15bc7a5c9fe51e6005643afd6)#define NXP\_S32\_P0\_PSI5\_S\_BAUD\_CLK 162U

[ 171](nxp__s32z2__clock_8h.md#a8cd9818e35f2504faae149799a0d9638)#define NXP\_S32\_P0\_PSI5\_S\_CORE\_CLK 163U

[ 172](nxp__s32z2__clock_8h.md#a19696ed6e7de7562c5a8b4986860ad82)#define NXP\_S32\_P0\_PSI5\_S\_TRIG0\_CLK 164U

[ 173](nxp__s32z2__clock_8h.md#aedbd34b2064ac95af9c17a5456ff3855)#define NXP\_S32\_P0\_PSI5\_S\_TRIG1\_CLK 165U

[ 174](nxp__s32z2__clock_8h.md#a36af4e664ef882746b52c50e1a360d41)#define NXP\_S32\_P0\_PSI5\_S\_TRIG2\_CLK 166U

[ 175](nxp__s32z2__clock_8h.md#a8b9934ce90c2fe91e6b0eeebe3c8459f)#define NXP\_S32\_P0\_PSI5\_S\_TRIG3\_CLK 167U

[ 176](nxp__s32z2__clock_8h.md#a068a54a8fbe24cec08b1fd50a08a22c6)#define NXP\_S32\_P0\_PSI5\_S\_UART\_CLK 168U

[ 177](nxp__s32z2__clock_8h.md#a01ae4eeb18f55302d7a71720cc51ae66)#define NXP\_S32\_P0\_PSI5\_S\_WDOG0\_CLK 169U

[ 178](nxp__s32z2__clock_8h.md#a1982f9aa465e31f26a744b84f62ef1b0)#define NXP\_S32\_P0\_PSI5\_S\_WDOG1\_CLK 170U

[ 179](nxp__s32z2__clock_8h.md#a8673cb557d9e66cad14e8b39f5ade479)#define NXP\_S32\_P0\_PSI5\_S\_WDOG2\_CLK 171U

[ 180](nxp__s32z2__clock_8h.md#ad85a63ab4506c854ebaf56be3cd1ff1f)#define NXP\_S32\_P0\_PSI5\_S\_WDOG3\_CLK 172U

[ 181](nxp__s32z2__clock_8h.md#ae8de22703b3e0dd10b9825da9fab7bf6)#define NXP\_S32\_P0\_REG\_INTF\_2X\_CLK 173U

[ 182](nxp__s32z2__clock_8h.md#a2ff5e51b07be18df4010f50c24e2a17a)#define NXP\_S32\_P0\_REG\_INTF\_CLK 174U

[ 183](nxp__s32z2__clock_8h.md#a90a14473f0c5fc9ea47849d8d225dfe0)#define NXP\_S32\_P1\_CLKOUT\_SRC\_CLK 175U

[ 184](nxp__s32z2__clock_8h.md#a5550b2018e416e7b4077b11cbee0454a)#define NXP\_S32\_P1\_DSPI60\_CLK 176U

[ 185](nxp__s32z2__clock_8h.md#a88a8f9a494f68937d827887eb881a186)#define NXP\_S32\_ETH\_TS\_CLK 177U

[ 186](nxp__s32z2__clock_8h.md#aaac96cff7479ae5452aa5faecf8c24fd)#define NXP\_S32\_ETH\_TS\_DIV4\_CLK 178U

[ 187](nxp__s32z2__clock_8h.md#a66c5b71fe9de0e186911cdd3236ba930)#define NXP\_S32\_ETH0\_REF\_RMII\_CLK 179U

[ 188](nxp__s32z2__clock_8h.md#acfefa0d9f76ac3429745527bccbdf712)#define NXP\_S32\_ETH0\_RX\_MII\_CLK 180U

[ 189](nxp__s32z2__clock_8h.md#ae7514957790fdbef6acfd5e637769e07)#define NXP\_S32\_ETH0\_RX\_RGMII\_CLK 181U

[ 190](nxp__s32z2__clock_8h.md#a2a7270a54cff6f0fd981b1892928d2d3)#define NXP\_S32\_ETH0\_TX\_RGMII\_CLK 182U

[ 191](nxp__s32z2__clock_8h.md#a18158dcfbe35defc6ac3ddec5663f3d5)#define NXP\_S32\_ETH0\_PS\_TX\_CLK 183U

[ 192](nxp__s32z2__clock_8h.md#a42ffe11005c05602e7c5f32c5cf31840)#define NXP\_S32\_ETH1\_REF\_RMII\_CLK 184U

[ 193](nxp__s32z2__clock_8h.md#a8c70c175327045d0dc20f9934e9c2bcb)#define NXP\_S32\_ETH1\_RX\_MII\_CLK 185U

[ 194](nxp__s32z2__clock_8h.md#a00adcfabd053d720460129a0f75a7528)#define NXP\_S32\_ETH1\_RX\_RGMII\_CLK 186U

[ 195](nxp__s32z2__clock_8h.md#a456af1ef69789bb71b922462520d4bed)#define NXP\_S32\_ETH1\_TX\_MII\_CLK 187U

[ 196](nxp__s32z2__clock_8h.md#a614779666ceeb1d9dadf0aa64280f19c)#define NXP\_S32\_ETH1\_TX\_RGMII\_CLK 188U

[ 197](nxp__s32z2__clock_8h.md#afb6c78fbfef3c83f07c3a13742bb0de6)#define NXP\_S32\_ETH1\_PS\_TX\_CLK 189U

[ 198](nxp__s32z2__clock_8h.md#ac2b71011cd7efab96ed82e0dec53ebbf)#define NXP\_S32\_P1\_LFAST0\_REF\_CLK 190U

[ 199](nxp__s32z2__clock_8h.md#a8f7fa9b6fc70d559f42c100ab043ed0b)#define NXP\_S32\_P1\_LFAST1\_REF\_CLK 191U

[ 200](nxp__s32z2__clock_8h.md#adbda03e5f3ec46eeeb4d80037fcee6ec)#define NXP\_S32\_P1\_NETC\_AXI\_CLK 192U

[ 201](nxp__s32z2__clock_8h.md#a2d9be627f771273bd7153ffc2f67de49)#define NXP\_S32\_P1\_LIN\_CLK 193U

[ 202](nxp__s32z2__clock_8h.md#a4b289b2abb24d96be3154a0d708c47a2)#define NXP\_S32\_P1\_REG\_INTF\_CLK 194U

[ 203](nxp__s32z2__clock_8h.md#a5c1ed5c4139f5bb21fd516b34c470a84)#define NXP\_S32\_P2\_DBG\_ATB\_CLK 195U

[ 204](nxp__s32z2__clock_8h.md#a094ca57b0793143a9c556793653c4b2a)#define NXP\_S32\_P2\_REG\_INTF\_CLK 196U

[ 205](nxp__s32z2__clock_8h.md#aa57d5790115ef7ac68418adeef94fa0c)#define NXP\_S32\_P3\_AES\_CLK 197U

[ 206](nxp__s32z2__clock_8h.md#a930fe7099338293129386fe6cc6411fa)#define NXP\_S32\_P3\_CLKOUT\_SRC\_CLK 198U

[ 207](nxp__s32z2__clock_8h.md#acecb11af2da42a7e30e6db63da1fdca9)#define NXP\_S32\_P3\_DBG\_TS\_CLK 199U

[ 208](nxp__s32z2__clock_8h.md#a2c1da162ffec0cf4c6c384c95fba1bc9)#define NXP\_S32\_P3\_REG\_INTF\_CLK 200U

[ 209](nxp__s32z2__clock_8h.md#afef936923819e2b7d5b47e1dbbcdb20a)#define NXP\_S32\_P3\_SYS\_MON1\_CLK 201U

[ 210](nxp__s32z2__clock_8h.md#adcee0fba1f18ea4a638cd925fe6a6cd1)#define NXP\_S32\_P3\_SYS\_MON2\_CLK 202U

[ 211](nxp__s32z2__clock_8h.md#a8bf6a442c62a58bb30dea1690b672f02)#define NXP\_S32\_P3\_SYS\_MON3\_CLK 203U

[ 212](nxp__s32z2__clock_8h.md#afeaf9f77f9b1c38c85a5929d1de41c29)#define NXP\_S32\_P4\_CLKOUT\_SRC\_CLK 204U

[ 213](nxp__s32z2__clock_8h.md#a56310949c10c299c71459ae2519d983a)#define NXP\_S32\_P4\_DSPI60\_CLK 205U

[ 214](nxp__s32z2__clock_8h.md#ae42588a847179f18a866d6a8d783d109)#define NXP\_S32\_P4\_EMIOS\_LCU\_CLK 206U

[ 215](nxp__s32z2__clock_8h.md#ac4a8f99f98db71f920c138949623d4bc)#define NXP\_S32\_P4\_LIN\_CLK 207U

[ 216](nxp__s32z2__clock_8h.md#a6a643398df1a3d6dc1400e276ac6b834)#define NXP\_S32\_P4\_PSI5\_125K\_CLK 208U

[ 217](nxp__s32z2__clock_8h.md#ad48ea0e82a482982976fcc0751613e70)#define NXP\_S32\_P4\_PSI5\_189K\_CLK 209U

[ 218](nxp__s32z2__clock_8h.md#a00a480f922125287f141c90425884bbb)#define NXP\_S32\_P4\_PSI5\_S\_BAUD\_CLK 210U

[ 219](nxp__s32z2__clock_8h.md#a51ebed20f61106859cbfda8512746c82)#define NXP\_S32\_P4\_PSI5\_S\_CORE\_CLK 211U

[ 220](nxp__s32z2__clock_8h.md#abeb2096f22a4bb8cd17e44afc43e21cf)#define NXP\_S32\_P4\_PSI5\_S\_TRIG0\_CLK 212U

[ 221](nxp__s32z2__clock_8h.md#a3e458ecf52aba2c8023558b205722d1e)#define NXP\_S32\_P4\_PSI5\_S\_TRIG1\_CLK 213U

[ 222](nxp__s32z2__clock_8h.md#a1e41cc7c6d18670e678c41f8054e4955)#define NXP\_S32\_P4\_PSI5\_S\_TRIG2\_CLK 214U

[ 223](nxp__s32z2__clock_8h.md#a3306bde399a946b4acb0e8a8422e8a5e)#define NXP\_S32\_P4\_PSI5\_S\_TRIG3\_CLK 215U

[ 224](nxp__s32z2__clock_8h.md#a7363852a4dbae0d1dce3c1e1ca69c942)#define NXP\_S32\_P4\_PSI5\_S\_UART\_CLK 216U

[ 225](nxp__s32z2__clock_8h.md#ae8f7f8894849326fd7de463c28eb2750)#define NXP\_S32\_P4\_PSI5\_S\_WDOG0\_CLK 217U

[ 226](nxp__s32z2__clock_8h.md#a4503412c69019cbe9e1f360e730021c5)#define NXP\_S32\_P4\_PSI5\_S\_WDOG1\_CLK 218U

[ 227](nxp__s32z2__clock_8h.md#a7b746bc4545d654e80d34737e35294d8)#define NXP\_S32\_P4\_PSI5\_S\_WDOG2\_CLK 219U

[ 228](nxp__s32z2__clock_8h.md#a29c1b1fc11a2bd4a56589ad261e1ef0b)#define NXP\_S32\_P4\_PSI5\_S\_WDOG3\_CLK 220U

[ 229](nxp__s32z2__clock_8h.md#a7a57d71043cdaf8592eef030151feca1)#define NXP\_S32\_P4\_QSPI0\_2X\_CLK 221U

[ 230](nxp__s32z2__clock_8h.md#abcc5e81770a40ab5c14a11ab61325405)#define NXP\_S32\_P4\_QSPI0\_1X\_CLK 222U

[ 231](nxp__s32z2__clock_8h.md#aba7b321632d765a70826933e169f1d51)#define NXP\_S32\_P4\_QSPI1\_2X\_CLK 223U

[ 232](nxp__s32z2__clock_8h.md#ab03050d789f565fdb401ccb60d7b58a5)#define NXP\_S32\_P4\_QSPI1\_1X\_CLK 224U

[ 233](nxp__s32z2__clock_8h.md#a74e0d39f05366c27f26a157e2b4d4b76)#define NXP\_S32\_P4\_REG\_INTF\_2X\_CLK 225U

[ 234](nxp__s32z2__clock_8h.md#a9c2dd8c4e369a43d53a0884bb9e42c2b)#define NXP\_S32\_P4\_REG\_INTF\_CLK 226U

[ 235](nxp__s32z2__clock_8h.md#a74fdff2722d49e0dcb913e7189f51377)#define NXP\_S32\_P4\_SDHC\_IP\_CLK 227U

[ 236](nxp__s32z2__clock_8h.md#a6ab6b60ac5091add4e31b72cc09599f1)#define NXP\_S32\_P4\_SDHC\_IP\_DIV2\_CLK 228U

[ 237](nxp__s32z2__clock_8h.md#ad464e90d729864b48a331e74293060e0)#define NXP\_S32\_P5\_DIPORT\_CLK 229U

[ 238](nxp__s32z2__clock_8h.md#abd484d3b8a562990e7656841269bfa28)#define NXP\_S32\_P5\_AE\_CLK 230U

[ 239](nxp__s32z2__clock_8h.md#aa95a8c461eb4dff35ff6437107da575d)#define NXP\_S32\_P5\_CANXL\_PE\_CLK 231U

[ 240](nxp__s32z2__clock_8h.md#a839ce35505017fbb12ace1f0b897e036)#define NXP\_S32\_P5\_CANXL\_CHI\_CLK 232U

[ 241](nxp__s32z2__clock_8h.md#a3994f4206e051b06c788dae82b02c7c2)#define NXP\_S32\_P5\_CLKOUT\_SRC\_CLK 233U

[ 242](nxp__s32z2__clock_8h.md#a758bf0b991fa5d9fed76f93276e829fa)#define NXP\_S32\_P5\_LIN\_CLK 234U

[ 243](nxp__s32z2__clock_8h.md#a49d5460d77183f7a98a4a236bc6f2b5a)#define NXP\_S32\_P5\_REG\_INTF\_CLK 235U

[ 244](nxp__s32z2__clock_8h.md#a75d9a7d4beda3a17dc0f07bd63fa368d)#define NXP\_S32\_P6\_REG\_INTF\_CLK 236U

[ 245](nxp__s32z2__clock_8h.md#a0352473aa201738f3c6476dee1551956)#define NXP\_S32\_PIT0\_CLK 237U

[ 246](nxp__s32z2__clock_8h.md#a8005e37da1d529a8340afe773fcb5291)#define NXP\_S32\_PIT1\_CLK 238U

[ 247](nxp__s32z2__clock_8h.md#a95d4be21a23722d68155ccb246971999)#define NXP\_S32\_PIT4\_CLK 239U

[ 248](nxp__s32z2__clock_8h.md#ae5252f32a9e3f0b0587bf0ac9c8e6ba4)#define NXP\_S32\_PIT5\_CLK 240U

[ 249](nxp__s32z2__clock_8h.md#ac6dffda41839ba589fe4d47bdbf12651)#define NXP\_S32\_P0\_PSI5\_1US\_CLK 241U

[ 250](nxp__s32z2__clock_8h.md#a45288996c043d9c843d699fc32c63ed4)#define NXP\_S32\_PSI5\_0\_CLK 242U

[ 251](nxp__s32z2__clock_8h.md#add87638b86bfb3519aa0f225f6490035)#define NXP\_S32\_P4\_PSI5\_1US\_CLK 243U

[ 252](nxp__s32z2__clock_8h.md#a50e530ccf9ee1ca47c1bb83662dc6099)#define NXP\_S32\_PSI5\_1\_CLK 244U

[ 253](nxp__s32z2__clock_8h.md#a9a237fb6c9a8f8b54103a2df4cbf4035)#define NXP\_S32\_PSI5S\_0\_CLK 245U

[ 254](nxp__s32z2__clock_8h.md#a9dc67efa8d4c150c887cf0ffc1645776)#define NXP\_S32\_PSI5S\_1\_CLK 246U

[ 255](nxp__s32z2__clock_8h.md#a99dcc3421a01f3c684be71561e305421)#define NXP\_S32\_QSPI0\_CLK 247U

[ 256](nxp__s32z2__clock_8h.md#a34b5af84c9e7acbebd49869f3b351899)#define NXP\_S32\_QSPI1\_CLK 248U

[ 257](nxp__s32z2__clock_8h.md#a9382cafe97d5ef2b77f0c56223523d03)#define NXP\_S32\_RTU0\_CORE\_MON1\_CLK 249U

[ 258](nxp__s32z2__clock_8h.md#a7d9bc68ad0596d370551738282b3aa47)#define NXP\_S32\_RTU0\_CORE\_MON2\_CLK 250U

[ 259](nxp__s32z2__clock_8h.md#a3b5861829dcdae5c4ba9eca8bf07803d)#define NXP\_S32\_RTU0\_CORE\_DIV2\_MON1\_CLK 251U

[ 260](nxp__s32z2__clock_8h.md#a25056829910865ceb57868499dbf5b1c)#define NXP\_S32\_RTU0\_CORE\_DIV2\_MON2\_CLK 252U

[ 261](nxp__s32z2__clock_8h.md#aa007c8ba96e292d6b0ee9ac9124997d7)#define NXP\_S32\_RTU0\_CORE\_DIV2\_MON3\_CLK 253U

[ 262](nxp__s32z2__clock_8h.md#a3aa44fc0bd3ebace5f0f5961614e9e6c)#define NXP\_S32\_RTU0\_REG\_INTF\_CLK 254U

[ 263](nxp__s32z2__clock_8h.md#afea4fe7c9d2a5a9bf8f1a67069f2562c)#define NXP\_S32\_RTU1\_CORE\_MON1\_CLK 255U

[ 264](nxp__s32z2__clock_8h.md#a0a2defc0b7e131537b5b9290f79910f6)#define NXP\_S32\_RTU1\_CORE\_MON2\_CLK 256U

[ 265](nxp__s32z2__clock_8h.md#ad10ef71c5464e922717e0c753a7fe676)#define NXP\_S32\_RTU1\_CORE\_DIV2\_MON1\_CLK 257U

[ 266](nxp__s32z2__clock_8h.md#a52a42685006ebf3ed9f9c5c119ffa609)#define NXP\_S32\_RTU1\_CORE\_DIV2\_MON2\_CLK 258U

[ 267](nxp__s32z2__clock_8h.md#a2a60767a23cdab4da560040ef15e71fd)#define NXP\_S32\_RTU1\_CORE\_DIV2\_MON3\_CLK 259U

[ 268](nxp__s32z2__clock_8h.md#adec5a3a5f480d49b032f0a9de9d2e570)#define NXP\_S32\_RTU1\_REG\_INTF\_CLK 260U

[ 269](nxp__s32z2__clock_8h.md#af22478974ea14d932259e929cf524c3b)#define NXP\_S32\_P4\_SDHC\_CLK 261U

[ 270](nxp__s32z2__clock_8h.md#a2fa48a84b2413d6873ec5c08945117b1)#define NXP\_S32\_RXLUT\_CLK 262U

[ 271](nxp__s32z2__clock_8h.md#adff8c8043444ba4e5f11e20141792a71)#define NXP\_S32\_SDHC0\_CLK 263U

[ 272](nxp__s32z2__clock_8h.md#a76b134b000c9a4b009a9ddd7a530dcba)#define NXP\_S32\_SINC\_CLK 264U

[ 273](nxp__s32z2__clock_8h.md#a4d8673a3b814bc9f14e15d50b57a7d2b)#define NXP\_S32\_SIPI0\_CLK 265U

[ 274](nxp__s32z2__clock_8h.md#a60c30b39d2e89c80fa211b43342ca99f)#define NXP\_S32\_SIPI1\_CLK 266U

[ 275](nxp__s32z2__clock_8h.md#a89f492994987302439850a892121c9bc)#define NXP\_S32\_SIUL2\_0\_CLK 267U

[ 276](nxp__s32z2__clock_8h.md#a106bdd661bd1dfe6cad2159566a1d58b)#define NXP\_S32\_SIUL2\_1\_CLK 268U

[ 277](nxp__s32z2__clock_8h.md#a26724e2b1db403ef5358a59979a4817e)#define NXP\_S32\_SIUL2\_4\_CLK 269U

[ 278](nxp__s32z2__clock_8h.md#adc51aa185a667c281505c668ba927ada)#define NXP\_S32\_SIUL2\_5\_CLK 270U

[ 279](nxp__s32z2__clock_8h.md#a59f5b4f73193b3b1e85929f1a7de9b80)#define NXP\_S32\_P0\_DSPI\_CLK 271U

[ 280](nxp__s32z2__clock_8h.md#a2c652648965f6c8e327ef712df2d5c98)#define NXP\_S32\_SPI0\_CLK 272U

[ 281](nxp__s32z2__clock_8h.md#acd656ebd78f6fe746576be80a5d24f05)#define NXP\_S32\_SPI1\_CLK 273U

[ 282](nxp__s32z2__clock_8h.md#aac83716126559636a7cd20141299c36d)#define NXP\_S32\_P1\_DSPI\_CLK 274U

[ 283](nxp__s32z2__clock_8h.md#aeb3dd4f8dc24715c3b229fd65ea9456f)#define NXP\_S32\_SPI2\_CLK 275U

[ 284](nxp__s32z2__clock_8h.md#a09fc0d6d2b75ab6e248e21b2542e273f)#define NXP\_S32\_SPI3\_CLK 276U

[ 285](nxp__s32z2__clock_8h.md#aefb565e2a703339f27aae4b7b26d467d)#define NXP\_S32\_SPI4\_CLK 277U

[ 286](nxp__s32z2__clock_8h.md#a66ee0c09316a60b6e5232ff367d40c70)#define NXP\_S32\_P4\_DSPI\_CLK 278U

[ 287](nxp__s32z2__clock_8h.md#a5a28541a5df280d0d685098be4d78c83)#define NXP\_S32\_SPI5\_CLK 279U

[ 288](nxp__s32z2__clock_8h.md#a340ee2dfb7907910aa7bd846e78cf32c)#define NXP\_S32\_SPI6\_CLK 280U

[ 289](nxp__s32z2__clock_8h.md#a9a6f4147c148f3e1f429d10cf5747206)#define NXP\_S32\_SPI7\_CLK 281U

[ 290](nxp__s32z2__clock_8h.md#ac6ee2ed42df2274bf355662f940508dc)#define NXP\_S32\_P5\_DSPI\_CLK 282U

[ 291](nxp__s32z2__clock_8h.md#a6b7ab2e57f263ca785d2356c89d0f466)#define NXP\_S32\_SPI8\_CLK 283U

[ 292](nxp__s32z2__clock_8h.md#a150b128b301b737cc3cf00248d2ac9e3)#define NXP\_S32\_SPI9\_CLK 284U

[ 293](nxp__s32z2__clock_8h.md#af5454d5392cc7b9fa4bc2d846b2da80e)#define NXP\_S32\_SRX0\_CLK 285U

[ 294](nxp__s32z2__clock_8h.md#af014a5ddb774fe7c342e2ee3c3734487)#define NXP\_S32\_SRX1\_CLK 286U

[ 295](nxp__s32z2__clock_8h.md#ae47e4cfc88cb30cdecb9436060fbb786)#define NXP\_S32\_CORE\_PLL\_REFCLKOUT 287U

[ 296](nxp__s32z2__clock_8h.md#a5afd4e4b53358aba324c53884b63bfc0)#define NXP\_S32\_CORE\_PLL\_FBCLKOUT 288U

[ 297](nxp__s32z2__clock_8h.md#a7e773ed5885cebf03a2409dbc308b2a6)#define NXP\_S32\_PERIPH\_PLL\_REFCLKOUT 289U

[ 298](nxp__s32z2__clock_8h.md#a49538138367d8188d74422d9dae3e1bf)#define NXP\_S32\_PERIPH\_PLL\_FBCLKOUT 290U

299

300#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32Z2\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [nxp\_s32z2\_clock.h](nxp__s32z2__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
