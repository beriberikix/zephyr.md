---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp__s32z2__clock_8h.html
original_path: doxygen/html/nxp__s32z2__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_s32z2\_clock.h File Reference

[Go to the source code of this file.](nxp__s32z2__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NXP\_S32\_FIRC\_CLK](#a8f4673a159fb26c90ae29761784395e9)   1U |
| #define | [NXP\_S32\_FXOSC\_CLK](#ab748e7ec615dc5fe10cafc723cc289fe)   2U |
| #define | [NXP\_S32\_SIRC\_CLK](#adc1da7bf433a80a3a975e172a30abbbc)   3U |
| #define | [NXP\_S32\_COREPLL\_CLK](#a3adcd5e43f56ff0c41093ae141efac06)   4U |
| #define | [NXP\_S32\_PERIPHPLL\_CLK](#a64b593be74cbcacec88f6f4aa513e959)   5U |
| #define | [NXP\_S32\_DDRPLL\_CLK](#a7cb52f27a12b3f96f09eb351d93132cb)   6U |
| #define | [NXP\_S32\_LFAST0\_PLL\_CLK](#a2cb385d2116bc56f05be3bde7b83e718)   7U |
| #define | [NXP\_S32\_LFAST1\_PLL\_CLK](#a2bce68111fdacf004a33b94c0c898c02)   8U |
| #define | [NXP\_S32\_COREPLL\_PHI0\_CLK](#acf8fe39109c8d74a1ed277866460b3fb)   9U |
| #define | [NXP\_S32\_COREPLL\_DFS0\_CLK](#a3aed8d0791095ec97ec68dd5a31d5a16)   10U |
| #define | [NXP\_S32\_COREPLL\_DFS1\_CLK](#ada9b9b2fcb4e577e0c04b5ec841cc73a)   11U |
| #define | [NXP\_S32\_COREPLL\_DFS2\_CLK](#a1012a8d0b7baf417fede47e819ac03bc)   12U |
| #define | [NXP\_S32\_COREPLL\_DFS3\_CLK](#a1e2cb85e953429dfd3b18af9c67a45ce)   13U |
| #define | [NXP\_S32\_COREPLL\_DFS4\_CLK](#a50c5562659befb1e3a6633ca5f383265)   14U |
| #define | [NXP\_S32\_COREPLL\_DFS5\_CLK](#a52c61d4e6b7907dcf5478c347cfc2f88)   15U |
| #define | [NXP\_S32\_PERIPHPLL\_PHI0\_CLK](#aa786b49d448f96193ccf372ed28b8892)   16U |
| #define | [NXP\_S32\_PERIPHPLL\_PHI1\_CLK](#a7c956a57231bdbe242b41fbf837512d7)   17U |
| #define | [NXP\_S32\_PERIPHPLL\_PHI2\_CLK](#a5a42cf11ac2ba5bfb697be28b3f7868c)   18U |
| #define | [NXP\_S32\_PERIPHPLL\_PHI3\_CLK](#ae3ecaa42d02bbdefe504c62d3dc3d5b3)   19U |
| #define | [NXP\_S32\_PERIPHPLL\_PHI4\_CLK](#a2550e0d2500a0c7d6a9af4aee6d2c0fb)   20U |
| #define | [NXP\_S32\_PERIPHPLL\_PHI5\_CLK](#acf1ad3c3de2d0f3db3110907b3a7f5de)   21U |
| #define | [NXP\_S32\_PERIPHPLL\_PHI6\_CLK](#afcea8aabd3d25ae13be9e50fa8c84b12)   22U |
| #define | [NXP\_S32\_PERIPHPLL\_DFS0\_CLK](#a6d1b5a86631e390202f9b02554815468)   23U |
| #define | [NXP\_S32\_PERIPHPLL\_DFS1\_CLK](#a2e3dc5289e03199416edfd3df835f183)   24U |
| #define | [NXP\_S32\_PERIPHPLL\_DFS2\_CLK](#a9a5e64bade06d1ee1202b61387d8a17c)   25U |
| #define | [NXP\_S32\_PERIPHPLL\_DFS3\_CLK](#ad282337933262b0c42430b35a33d7507)   26U |
| #define | [NXP\_S32\_PERIPHPLL\_DFS4\_CLK](#a594165bad79d57a3efce555cb9ac5bff)   27U |
| #define | [NXP\_S32\_PERIPHPLL\_DFS5\_CLK](#aba43a681b81004967aa5827c55b24a5d)   28U |
| #define | [NXP\_S32\_DDRPLL\_PHI0\_CLK](#a6bc7d24858e5aacb50495395ca368695)   29U |
| #define | [NXP\_S32\_LFAST0\_PLL\_PH0\_CLK](#aaf01394fcd23fdcff4792684b1a970d8)   30U |
| #define | [NXP\_S32\_LFAST1\_PLL\_PH0\_CLK](#a3d00b3751ab9bccaf4471bfab3d5d522)   31U |
| #define | [NXP\_S32\_ETH\_RGMII\_REF\_CLK](#a25c75209f8f1f75734aede68aa358744)   32U |
| #define | [NXP\_S32\_TMR\_1588\_CLK](#a9540744a0ace0989f2c3cc968f3713af)   33U |
| #define | [NXP\_S32\_ETH0\_EXT\_RX\_CLK](#a12a72ae64ce2fca3bb59cbddde7f8ae4)   34U |
| #define | [NXP\_S32\_ETH0\_EXT\_TX\_CLK](#a564bf352a181cf965b34b5da9b00a18d)   35U |
| #define | [NXP\_S32\_ETH1\_EXT\_RX\_CLK](#a4e3c08a9d415372a3884f8e1658f4de3)   36U |
| #define | [NXP\_S32\_ETH1\_EXT\_TX\_CLK](#a5e2a62c4e47330fcd4d9e380ed0107ea)   37U |
| #define | [NXP\_S32\_LFAST0\_EXT\_REF\_CLK](#a08658b7dbf05f325c8dcad2f609b714d)   38U |
| #define | [NXP\_S32\_LFAST1\_EXT\_REF\_CLK](#a84b1c38882e6af516c04909671427d4a)   39U |
| #define | [NXP\_S32\_DDR\_CLK](#a28cbe95441f2e1691795ca86d29e5c0f)   40U |
| #define | [NXP\_S32\_P0\_SYS\_CLK](#abc6c662bf88c9a922478bf368ef7416c)   41U |
| #define | [NXP\_S32\_P1\_SYS\_CLK](#ab65e705e34df2a7428493b1c232fc6fd)   42U |
| #define | [NXP\_S32\_P1\_SYS\_DIV2\_CLK](#a4e44f6e2575430b847296bb0336a555f)   43U |
| #define | [NXP\_S32\_P1\_SYS\_DIV4\_CLK](#a725ad3fb6496a459f4719f64658478a1)   44U |
| #define | [NXP\_S32\_P2\_SYS\_CLK](#aa5d06e65e92b43483cecfa7608abb8d6)   45U |
| #define | [NXP\_S32\_CORE\_M33\_CLK](#ac66e693079884870e56f2b380a55eaed)   46U |
| #define | [NXP\_S32\_P2\_SYS\_DIV2\_CLK](#a0f5ffbc3acf02add006d35efa94ca3a6)   47U |
| #define | [NXP\_S32\_P2\_SYS\_DIV4\_CLK](#abb48ce40572d7f0f174b644930d949cc)   48U |
| #define | [NXP\_S32\_P3\_SYS\_CLK](#a5557d1a39d866ddc1e7baa7c8e6ff9f0)   49U |
| #define | [NXP\_S32\_CE\_SYS\_DIV2\_CLK](#ab6eb18cde38b8ca9dfa2b7181c41d6c0)   50U |
| #define | [NXP\_S32\_CE\_SYS\_DIV4\_CLK](#a65a5ce3703f0c3c99e85654004783e88)   51U |
| #define | [NXP\_S32\_P3\_SYS\_DIV2\_NOC\_CLK](#a47d136a5e21ff3031bd7b9eb0075d8f6)   52U |
| #define | [NXP\_S32\_P3\_SYS\_DIV4\_CLK](#a07633bb8f64c1125935a2b28ad5bf485)   53U |
| #define | [NXP\_S32\_P4\_SYS\_CLK](#ac81524f01ee44bab50879663fc242211)   54U |
| #define | [NXP\_S32\_P4\_SYS\_DIV2\_CLK](#ac2cd9425cd2eb8e8c29d5716259034df)   55U |
| #define | [NXP\_S32\_HSE\_SYS\_DIV2\_CLK](#af36e2f8d5d39189013c65589eaaf3da2)   56U |
| #define | [NXP\_S32\_P5\_SYS\_CLK](#a8fdb0b99d90aa47b3a16aa8df92a23ba)   57U |
| #define | [NXP\_S32\_P5\_SYS\_DIV2\_CLK](#ad324b9f48cffa750d35a1b3625e41d78)   58U |
| #define | [NXP\_S32\_P5\_SYS\_DIV4\_CLK](#afa536c5aa9044ad45772be1330568ef5)   59U |
| #define | [NXP\_S32\_P2\_MATH\_CLK](#afdd0087c9c7473debe2c36f9c4b3b9eb)   60U |
| #define | [NXP\_S32\_P2\_MATH\_DIV3\_CLK](#a43b5a621c2e3a2ed9b3b5b6a5742c5fa)   61U |
| #define | [NXP\_S32\_GLB\_LBIST\_CLK](#a8eca101146810d0b95493c66a19b7b16)   62U |
| #define | [NXP\_S32\_RTU0\_CORE\_CLK](#a480e71b89b05bc9e36526d87a995d0df)   63U |
| #define | [NXP\_S32\_RTU0\_CORE\_DIV2\_CLK](#a29df359bdd3589eedc4d973619789304)   64U |
| #define | [NXP\_S32\_RTU1\_CORE\_CLK](#aa1497392847306b62614e7c3b653048f)   65U |
| #define | [NXP\_S32\_RTU1\_CORE\_DIV2\_CLK](#adbce190d535e203b6a3d04369a316d4e)   66U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_UTIL\_CLK](#a522a9b1e7ba5816155bf057ffbb4f2fe)   67U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_UTIL\_CLK](#ad0e0022e42d0b941e0edd976837d1b00)   68U |
| #define | [NXP\_S32\_ADC0\_CLK](#a89fe6bb1365a3895449da72ccd517223)   70U |
| #define | [NXP\_S32\_ADC1\_CLK](#ace9575b4ed012fe344884b0b1fa2ef58)   71U |
| #define | [NXP\_S32\_CE\_EDMA\_CLK](#ac81ef4f7bd981576b69426f195b010e3)   72U |
| #define | [NXP\_S32\_CE\_PIT0\_CLK](#a896f8242ee6ca821d912706775169ff4)   73U |
| #define | [NXP\_S32\_CE\_PIT1\_CLK](#a8fa4590c34477b07d6d902db44a28387)   74U |
| #define | [NXP\_S32\_CE\_PIT2\_CLK](#a02ddfc31f0ec38b341adb47bbfcfe43b)   75U |
| #define | [NXP\_S32\_CE\_PIT3\_CLK](#a7ad3dabd64d6358362e3ce6102542709)   76U |
| #define | [NXP\_S32\_CE\_PIT4\_CLK](#aa162dfc6ae281d398bd30efbb9d23eeb)   77U |
| #define | [NXP\_S32\_CE\_PIT5\_CLK](#a6bc8443e520ace278124978cc00080d6)   78U |
| #define | [NXP\_S32\_CLKOUT0\_CLK](#a63aca9fbcdae28cd448e62e9dcf41da9)   79U |
| #define | [NXP\_S32\_CLKOUT1\_CLK](#aed622cb6ba9b009aa0913c0e7d8f727f)   80U |
| #define | [NXP\_S32\_CLKOUT2\_CLK](#a93cd425d58dd7d2ef73139487816b0f2)   81U |
| #define | [NXP\_S32\_CLKOUT3\_CLK](#a24fc740cdbf049289b845e7c57f3653b)   82U |
| #define | [NXP\_S32\_CLKOUT4\_CLK](#a0218b218e1ea001888490a74e824c5fa)   83U |
| #define | [NXP\_S32\_CTU\_CLK](#a31bde6eec68fcfd8e76a497363276288)   84U |
| #define | [NXP\_S32\_DMACRC0\_CLK](#abf95474bbeb9969a520edd298172941e)   85U |
| #define | [NXP\_S32\_DMACRC1\_CLK](#a0960ae83fd592bd62c12dbffb212f02a)   86U |
| #define | [NXP\_S32\_DMACRC4\_CLK](#aa486c18a096eebeec8afeb4d1ac98e91)   87U |
| #define | [NXP\_S32\_DMACRC5\_CLK](#a7ed644aafa5cec6aa0ad1521c29d9589)   88U |
| #define | [NXP\_S32\_DMAMUX0\_CLK](#a97a3ff5238f4878784ee1bee4cfc7522)   89U |
| #define | [NXP\_S32\_DMAMUX1\_CLK](#a708913d2bb71ec975caad705a10b8421)   90U |
| #define | [NXP\_S32\_DMAMUX4\_CLK](#ae0650d4cdd3cca6a08666f0a0173a567)   91U |
| #define | [NXP\_S32\_DMAMUX5\_CLK](#ad6fd147a074209f370ff0761b49c64a2)   92U |
| #define | [NXP\_S32\_EDMA0\_CLK](#ae8b13f1f1803f214f7c7ba371679ee6f)   93U |
| #define | [NXP\_S32\_EDMA1\_CLK](#a572adbd504ff44b0756578d38d8a9a7e)   94U |
| #define | [NXP\_S32\_EDMA3\_CLK](#adc7573ce484dfda1662645ee5b959d86)   95U |
| #define | [NXP\_S32\_EDMA4\_CLK](#a70e0508f328066120600422e31dd9bd6)   96U |
| #define | [NXP\_S32\_EDMA5\_CLK](#ada44bb4bde41cfae4cbb5a30e615c27f)   97U |
| #define | [NXP\_S32\_ETH0\_TX\_MII\_CLK](#ac6cae2e8c1e0e49d24143da01bedbfd4)   98U |
| #define | [NXP\_S32\_ENET0\_CLK](#a42812f12a9d19b18a532ab3609829aa1)   99U |
| #define | [NXP\_S32\_P3\_CAN\_PE\_CLK](#af42ddf0adf09c31916350082dc472cba)   100U |
| #define | [NXP\_S32\_FLEXCAN0\_CLK](#a308e74a366725070c56a4ab4fc7c300a)   101U |
| #define | [NXP\_S32\_FLEXCAN1\_CLK](#ad353c07d914cfa8c45ed3b7b586c2b00)   102U |
| #define | [NXP\_S32\_FLEXCAN2\_CLK](#a54467688a58d9be77849eddd031f126e)   103U |
| #define | [NXP\_S32\_FLEXCAN3\_CLK](#a0fcf00296138cd26e845ab524054fd3b)   104U |
| #define | [NXP\_S32\_FLEXCAN4\_CLK](#a6106f0f8b5e0f5230b75e43b5ccdbf0e)   105U |
| #define | [NXP\_S32\_FLEXCAN5\_CLK](#a4f3b1864f3f5bcc6a1fd66e27eb12a52)   106U |
| #define | [NXP\_S32\_FLEXCAN6\_CLK](#aab3b5b178be344b18c4c9ca27786eb03)   107U |
| #define | [NXP\_S32\_FLEXCAN7\_CLK](#a5c239f32216a44b5282e5ffd9fdd214f)   108U |
| #define | [NXP\_S32\_FLEXCAN8\_CLK](#afb62f9c88f6652a3382197c10456c8b9)   109U |
| #define | [NXP\_S32\_FLEXCAN9\_CLK](#a3f8baea9230234e8e9dafdbe1dadc005)   110U |
| #define | [NXP\_S32\_FLEXCAN10\_CLK](#a8fff5e2c245578e94f4e9ed4eddfc19b)   111U |
| #define | [NXP\_S32\_FLEXCAN11\_CLK](#a875232291fcb4035ea178013d1996300)   112U |
| #define | [NXP\_S32\_FLEXCAN12\_CLK](#a0149861a754ec061781b59813e9bb5ea)   113U |
| #define | [NXP\_S32\_FLEXCAN13\_CLK](#af92372e349573e82108e2d858d7bed52)   114U |
| #define | [NXP\_S32\_FLEXCAN14\_CLK](#adc7b3ae5cfc1fe779b0075626fae2328)   115U |
| #define | [NXP\_S32\_FLEXCAN15\_CLK](#a55351634b1b77419c5f2aeccdd917ebe)   116U |
| #define | [NXP\_S32\_FLEXCAN16\_CLK](#aa95b2f2eceb55537b99e6a14f84f17d1)   117U |
| #define | [NXP\_S32\_FLEXCAN17\_CLK](#acaed7d12a46279f9a3a5af4fde4e5693)   118U |
| #define | [NXP\_S32\_FLEXCAN18\_CLK](#a204e919465814538dd49dd775eb2f8f6)   119U |
| #define | [NXP\_S32\_FLEXCAN19\_CLK](#a3421175f2c69e71bfa90cf8b34e69c5b)   120U |
| #define | [NXP\_S32\_FLEXCAN20\_CLK](#a4f44e36a65a4e2422fd3b72e246b7170)   121U |
| #define | [NXP\_S32\_FLEXCAN21\_CLK](#a9c6e9291e6d310a4a41f0ea3d6810b79)   122U |
| #define | [NXP\_S32\_FLEXCAN22\_CLK](#a0890c9d64890e95b8de85914eb773986)   123U |
| #define | [NXP\_S32\_FLEXCAN23\_CLK](#a98a67a530a8ab4602974248029953934)   124U |
| #define | [NXP\_S32\_P0\_FR\_PE\_CLK](#a359bad70140a01914fbb90541c178226)   125U |
| #define | [NXP\_S32\_FRAY0\_CLK](#ae1a59aa87c82395e1badae9f62a8345a)   126U |
| #define | [NXP\_S32\_FRAY1\_CLK](#abe6b9172ef85c386ab5ad017533ba1ee)   127U |
| #define | [NXP\_S32\_GTM\_CLK](#af5f8881fdd6fc0b160ecbbccfc34df88)   128U |
| #define | [NXP\_S32\_IIIC0\_CLK](#afa13966ea5003a4018851341485db5c7)   129U |
| #define | [NXP\_S32\_IIIC1\_CLK](#ac18c5d32153412256754f0a8871a3613)   130U |
| #define | [NXP\_S32\_IIIC2\_CLK](#a56d46603e3275969d77401c2404f1105)   131U |
| #define | [NXP\_S32\_P0\_LIN\_BAUD\_CLK](#a71af2c2cf427a16f1b8d0d1ef6d5c5c5)   132U |
| #define | [NXP\_S32\_LIN0\_CLK](#ab398d341ee088a2913a096ec2b9b6545)   133U |
| #define | [NXP\_S32\_LIN1\_CLK](#ae4867ba422c49414a6e32b7170f19398)   134U |
| #define | [NXP\_S32\_LIN2\_CLK](#a7138bcb68270ae9f46539ffc65cd34dd)   135U |
| #define | [NXP\_S32\_P1\_LIN\_BAUD\_CLK](#a9b0b135bf98d9982e26547801c0452cd)   136U |
| #define | [NXP\_S32\_LIN3\_CLK](#aae3a89eaeca09ae97ad3ba0132632b7b)   137U |
| #define | [NXP\_S32\_LIN4\_CLK](#a0953f6ad3c2f2f84a82927d8ed979d2e)   138U |
| #define | [NXP\_S32\_LIN5\_CLK](#a2f1405a5d9a3e3e03d2b607f064c9c49)   139U |
| #define | [NXP\_S32\_P4\_LIN\_BAUD\_CLK](#a34da0d2172d9eff2f9edf40e980bd980)   140U |
| #define | [NXP\_S32\_LIN6\_CLK](#a8f0dc1e8fa2449e42f1e1371ed3526bc)   141U |
| #define | [NXP\_S32\_LIN7\_CLK](#a0e14ecb12403a221a992eb6f6970d324)   142U |
| #define | [NXP\_S32\_LIN8\_CLK](#a6d8815173be045f717ee61f5770dd2ca)   143U |
| #define | [NXP\_S32\_P5\_LIN\_BAUD\_CLK](#a5e3508c56acc88ca6a4fb04f5b59f7bc)   144U |
| #define | [NXP\_S32\_LIN9\_CLK](#a3d55f195f31e6fdfeecdb2d712564e82)   145U |
| #define | [NXP\_S32\_LIN10\_CLK](#a926d082c5223bcdc027e220190ec2e41)   146U |
| #define | [NXP\_S32\_LIN11\_CLK](#a9475a59878a242d95a90c69c1e5b78d9)   147U |
| #define | [NXP\_S32\_MSCDSPI\_CLK](#ad98b9a2b348c6e58f41420a47a5e2ba8)   148U |
| #define | [NXP\_S32\_MSCLIN\_CLK](#a0d21ae71b95bcfc407f67053dd202288)   149U |
| #define | [NXP\_S32\_NANO\_CLK](#a962245016be6213059cefaabe2c5d96e)   150U |
| #define | [NXP\_S32\_P0\_CLKOUT\_SRC\_CLK](#ab82b29897283f400bd543368f8b1fc73)   151U |
| #define | [NXP\_S32\_P0\_CTU\_PER\_CLK](#af80cf625f75ceb16fabb4f3a52e8154c)   152U |
| #define | [NXP\_S32\_P0\_DSPI\_MSC\_CLK](#a714fae0bdcbe4980f167cb222d008da5)   153U |
| #define | [NXP\_S32\_P0\_EMIOS\_LCU\_CLK](#a16ffc4b60ef57064c790dbe9c0bca6b9)   154U |
| #define | [NXP\_S32\_P0\_GTM\_CLK](#a686525770665c07bd423523d3a36b3ac)   155U |
| #define | [NXP\_S32\_P0\_GTM\_NOC\_CLK](#afbdfad00c82da171e55148b6239e42d3)   156U |
| #define | [NXP\_S32\_P0\_GTM\_TS\_CLK](#a23a8ea48e3fd40e86ba10a26c50729cb)   157U |
| #define | [NXP\_S32\_P0\_LIN\_CLK](#a25b98ce36a908555b566240eef0eeb32)   158U |
| #define | [NXP\_S32\_P0\_NANO\_CLK](#a58a1b67087d393bcd87aa1021a602610)   159U |
| #define | [NXP\_S32\_P0\_PSI5\_125K\_CLK](#ad26f0c08b0ba71b1322bd0d96f39d088)   160U |
| #define | [NXP\_S32\_P0\_PSI5\_189K\_CLK](#a26c4eb3cc201d79da9e694fc9978db99)   161U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_BAUD\_CLK](#a459ee3a15bc7a5c9fe51e6005643afd6)   162U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_CORE\_CLK](#a8cd9818e35f2504faae149799a0d9638)   163U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_TRIG0\_CLK](#a19696ed6e7de7562c5a8b4986860ad82)   164U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_TRIG1\_CLK](#aedbd34b2064ac95af9c17a5456ff3855)   165U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_TRIG2\_CLK](#a36af4e664ef882746b52c50e1a360d41)   166U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_TRIG3\_CLK](#a8b9934ce90c2fe91e6b0eeebe3c8459f)   167U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_UART\_CLK](#a068a54a8fbe24cec08b1fd50a08a22c6)   168U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_WDOG0\_CLK](#a01ae4eeb18f55302d7a71720cc51ae66)   169U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_WDOG1\_CLK](#a1982f9aa465e31f26a744b84f62ef1b0)   170U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_WDOG2\_CLK](#a8673cb557d9e66cad14e8b39f5ade479)   171U |
| #define | [NXP\_S32\_P0\_PSI5\_S\_WDOG3\_CLK](#ad85a63ab4506c854ebaf56be3cd1ff1f)   172U |
| #define | [NXP\_S32\_P0\_REG\_INTF\_2X\_CLK](#ae8de22703b3e0dd10b9825da9fab7bf6)   173U |
| #define | [NXP\_S32\_P0\_REG\_INTF\_CLK](#a2ff5e51b07be18df4010f50c24e2a17a)   174U |
| #define | [NXP\_S32\_P1\_CLKOUT\_SRC\_CLK](#a90a14473f0c5fc9ea47849d8d225dfe0)   175U |
| #define | [NXP\_S32\_P1\_DSPI60\_CLK](#a5550b2018e416e7b4077b11cbee0454a)   176U |
| #define | [NXP\_S32\_ETH\_TS\_CLK](#a88a8f9a494f68937d827887eb881a186)   177U |
| #define | [NXP\_S32\_ETH\_TS\_DIV4\_CLK](#aaac96cff7479ae5452aa5faecf8c24fd)   178U |
| #define | [NXP\_S32\_ETH0\_REF\_RMII\_CLK](#a66c5b71fe9de0e186911cdd3236ba930)   179U |
| #define | [NXP\_S32\_ETH0\_RX\_MII\_CLK](#acfefa0d9f76ac3429745527bccbdf712)   180U |
| #define | [NXP\_S32\_ETH0\_RX\_RGMII\_CLK](#ae7514957790fdbef6acfd5e637769e07)   181U |
| #define | [NXP\_S32\_ETH0\_TX\_RGMII\_CLK](#a2a7270a54cff6f0fd981b1892928d2d3)   182U |
| #define | [NXP\_S32\_ETH0\_PS\_TX\_CLK](#a18158dcfbe35defc6ac3ddec5663f3d5)   183U |
| #define | [NXP\_S32\_ETH1\_REF\_RMII\_CLK](#a42ffe11005c05602e7c5f32c5cf31840)   184U |
| #define | [NXP\_S32\_ETH1\_RX\_MII\_CLK](#a8c70c175327045d0dc20f9934e9c2bcb)   185U |
| #define | [NXP\_S32\_ETH1\_RX\_RGMII\_CLK](#a00adcfabd053d720460129a0f75a7528)   186U |
| #define | [NXP\_S32\_ETH1\_TX\_MII\_CLK](#a456af1ef69789bb71b922462520d4bed)   187U |
| #define | [NXP\_S32\_ETH1\_TX\_RGMII\_CLK](#a614779666ceeb1d9dadf0aa64280f19c)   188U |
| #define | [NXP\_S32\_ETH1\_PS\_TX\_CLK](#afb6c78fbfef3c83f07c3a13742bb0de6)   189U |
| #define | [NXP\_S32\_P1\_LFAST0\_REF\_CLK](#ac2b71011cd7efab96ed82e0dec53ebbf)   190U |
| #define | [NXP\_S32\_P1\_LFAST1\_REF\_CLK](#a8f7fa9b6fc70d559f42c100ab043ed0b)   191U |
| #define | [NXP\_S32\_P1\_NETC\_AXI\_CLK](#adbda03e5f3ec46eeeb4d80037fcee6ec)   192U |
| #define | [NXP\_S32\_P1\_LIN\_CLK](#a2d9be627f771273bd7153ffc2f67de49)   193U |
| #define | [NXP\_S32\_P1\_REG\_INTF\_CLK](#a4b289b2abb24d96be3154a0d708c47a2)   194U |
| #define | [NXP\_S32\_P2\_DBG\_ATB\_CLK](#a5c1ed5c4139f5bb21fd516b34c470a84)   195U |
| #define | [NXP\_S32\_P2\_REG\_INTF\_CLK](#a094ca57b0793143a9c556793653c4b2a)   196U |
| #define | [NXP\_S32\_P3\_AES\_CLK](#aa57d5790115ef7ac68418adeef94fa0c)   197U |
| #define | [NXP\_S32\_P3\_CLKOUT\_SRC\_CLK](#a930fe7099338293129386fe6cc6411fa)   198U |
| #define | [NXP\_S32\_P3\_DBG\_TS\_CLK](#acecb11af2da42a7e30e6db63da1fdca9)   199U |
| #define | [NXP\_S32\_P3\_REG\_INTF\_CLK](#a2c1da162ffec0cf4c6c384c95fba1bc9)   200U |
| #define | [NXP\_S32\_P3\_SYS\_MON1\_CLK](#afef936923819e2b7d5b47e1dbbcdb20a)   201U |
| #define | [NXP\_S32\_P3\_SYS\_MON2\_CLK](#adcee0fba1f18ea4a638cd925fe6a6cd1)   202U |
| #define | [NXP\_S32\_P3\_SYS\_MON3\_CLK](#a8bf6a442c62a58bb30dea1690b672f02)   203U |
| #define | [NXP\_S32\_P4\_CLKOUT\_SRC\_CLK](#afeaf9f77f9b1c38c85a5929d1de41c29)   204U |
| #define | [NXP\_S32\_P4\_DSPI60\_CLK](#a56310949c10c299c71459ae2519d983a)   205U |
| #define | [NXP\_S32\_P4\_EMIOS\_LCU\_CLK](#ae42588a847179f18a866d6a8d783d109)   206U |
| #define | [NXP\_S32\_P4\_LIN\_CLK](#ac4a8f99f98db71f920c138949623d4bc)   207U |
| #define | [NXP\_S32\_P4\_PSI5\_125K\_CLK](#a6a643398df1a3d6dc1400e276ac6b834)   208U |
| #define | [NXP\_S32\_P4\_PSI5\_189K\_CLK](#ad48ea0e82a482982976fcc0751613e70)   209U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_BAUD\_CLK](#a00a480f922125287f141c90425884bbb)   210U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_CORE\_CLK](#a51ebed20f61106859cbfda8512746c82)   211U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_TRIG0\_CLK](#abeb2096f22a4bb8cd17e44afc43e21cf)   212U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_TRIG1\_CLK](#a3e458ecf52aba2c8023558b205722d1e)   213U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_TRIG2\_CLK](#a1e41cc7c6d18670e678c41f8054e4955)   214U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_TRIG3\_CLK](#a3306bde399a946b4acb0e8a8422e8a5e)   215U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_UART\_CLK](#a7363852a4dbae0d1dce3c1e1ca69c942)   216U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_WDOG0\_CLK](#ae8f7f8894849326fd7de463c28eb2750)   217U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_WDOG1\_CLK](#a4503412c69019cbe9e1f360e730021c5)   218U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_WDOG2\_CLK](#a7b746bc4545d654e80d34737e35294d8)   219U |
| #define | [NXP\_S32\_P4\_PSI5\_S\_WDOG3\_CLK](#a29c1b1fc11a2bd4a56589ad261e1ef0b)   220U |
| #define | [NXP\_S32\_P4\_QSPI0\_2X\_CLK](#a7a57d71043cdaf8592eef030151feca1)   221U |
| #define | [NXP\_S32\_P4\_QSPI0\_1X\_CLK](#abcc5e81770a40ab5c14a11ab61325405)   222U |
| #define | [NXP\_S32\_P4\_QSPI1\_2X\_CLK](#aba7b321632d765a70826933e169f1d51)   223U |
| #define | [NXP\_S32\_P4\_QSPI1\_1X\_CLK](#ab03050d789f565fdb401ccb60d7b58a5)   224U |
| #define | [NXP\_S32\_P4\_REG\_INTF\_2X\_CLK](#a74e0d39f05366c27f26a157e2b4d4b76)   225U |
| #define | [NXP\_S32\_P4\_REG\_INTF\_CLK](#a9c2dd8c4e369a43d53a0884bb9e42c2b)   226U |
| #define | [NXP\_S32\_P4\_SDHC\_IP\_CLK](#a74fdff2722d49e0dcb913e7189f51377)   227U |
| #define | [NXP\_S32\_P4\_SDHC\_IP\_DIV2\_CLK](#a6ab6b60ac5091add4e31b72cc09599f1)   228U |
| #define | [NXP\_S32\_P5\_DIPORT\_CLK](#ad464e90d729864b48a331e74293060e0)   229U |
| #define | [NXP\_S32\_P5\_AE\_CLK](#abd484d3b8a562990e7656841269bfa28)   230U |
| #define | [NXP\_S32\_P5\_CANXL\_PE\_CLK](#aa95a8c461eb4dff35ff6437107da575d)   231U |
| #define | [NXP\_S32\_P5\_CANXL\_CHI\_CLK](#a839ce35505017fbb12ace1f0b897e036)   232U |
| #define | [NXP\_S32\_P5\_CLKOUT\_SRC\_CLK](#a3994f4206e051b06c788dae82b02c7c2)   233U |
| #define | [NXP\_S32\_P5\_LIN\_CLK](#a758bf0b991fa5d9fed76f93276e829fa)   234U |
| #define | [NXP\_S32\_P5\_REG\_INTF\_CLK](#a49d5460d77183f7a98a4a236bc6f2b5a)   235U |
| #define | [NXP\_S32\_P6\_REG\_INTF\_CLK](#a75d9a7d4beda3a17dc0f07bd63fa368d)   236U |
| #define | [NXP\_S32\_PIT0\_CLK](#a0352473aa201738f3c6476dee1551956)   237U |
| #define | [NXP\_S32\_PIT1\_CLK](#a8005e37da1d529a8340afe773fcb5291)   238U |
| #define | [NXP\_S32\_PIT4\_CLK](#a95d4be21a23722d68155ccb246971999)   239U |
| #define | [NXP\_S32\_PIT5\_CLK](#ae5252f32a9e3f0b0587bf0ac9c8e6ba4)   240U |
| #define | [NXP\_S32\_P0\_PSI5\_1US\_CLK](#ac6dffda41839ba589fe4d47bdbf12651)   241U |
| #define | [NXP\_S32\_PSI5\_0\_CLK](#a45288996c043d9c843d699fc32c63ed4)   242U |
| #define | [NXP\_S32\_P4\_PSI5\_1US\_CLK](#add87638b86bfb3519aa0f225f6490035)   243U |
| #define | [NXP\_S32\_PSI5\_1\_CLK](#a50e530ccf9ee1ca47c1bb83662dc6099)   244U |
| #define | [NXP\_S32\_PSI5S\_0\_CLK](#a9a237fb6c9a8f8b54103a2df4cbf4035)   245U |
| #define | [NXP\_S32\_PSI5S\_1\_CLK](#a9dc67efa8d4c150c887cf0ffc1645776)   246U |
| #define | [NXP\_S32\_QSPI0\_CLK](#a99dcc3421a01f3c684be71561e305421)   247U |
| #define | [NXP\_S32\_QSPI1\_CLK](#a34b5af84c9e7acbebd49869f3b351899)   248U |
| #define | [NXP\_S32\_RTU0\_CORE\_MON1\_CLK](#a9382cafe97d5ef2b77f0c56223523d03)   249U |
| #define | [NXP\_S32\_RTU0\_CORE\_MON2\_CLK](#a7d9bc68ad0596d370551738282b3aa47)   250U |
| #define | [NXP\_S32\_RTU0\_CORE\_DIV2\_MON1\_CLK](#a3b5861829dcdae5c4ba9eca8bf07803d)   251U |
| #define | [NXP\_S32\_RTU0\_CORE\_DIV2\_MON2\_CLK](#a25056829910865ceb57868499dbf5b1c)   252U |
| #define | [NXP\_S32\_RTU0\_CORE\_DIV2\_MON3\_CLK](#aa007c8ba96e292d6b0ee9ac9124997d7)   253U |
| #define | [NXP\_S32\_RTU0\_REG\_INTF\_CLK](#a3aa44fc0bd3ebace5f0f5961614e9e6c)   254U |
| #define | [NXP\_S32\_RTU1\_CORE\_MON1\_CLK](#afea4fe7c9d2a5a9bf8f1a67069f2562c)   255U |
| #define | [NXP\_S32\_RTU1\_CORE\_MON2\_CLK](#a0a2defc0b7e131537b5b9290f79910f6)   256U |
| #define | [NXP\_S32\_RTU1\_CORE\_DIV2\_MON1\_CLK](#ad10ef71c5464e922717e0c753a7fe676)   257U |
| #define | [NXP\_S32\_RTU1\_CORE\_DIV2\_MON2\_CLK](#a52a42685006ebf3ed9f9c5c119ffa609)   258U |
| #define | [NXP\_S32\_RTU1\_CORE\_DIV2\_MON3\_CLK](#a2a60767a23cdab4da560040ef15e71fd)   259U |
| #define | [NXP\_S32\_RTU1\_REG\_INTF\_CLK](#adec5a3a5f480d49b032f0a9de9d2e570)   260U |
| #define | [NXP\_S32\_P4\_SDHC\_CLK](#af22478974ea14d932259e929cf524c3b)   261U |
| #define | [NXP\_S32\_RXLUT\_CLK](#a2fa48a84b2413d6873ec5c08945117b1)   262U |
| #define | [NXP\_S32\_SDHC0\_CLK](#adff8c8043444ba4e5f11e20141792a71)   263U |
| #define | [NXP\_S32\_SINC\_CLK](#a76b134b000c9a4b009a9ddd7a530dcba)   264U |
| #define | [NXP\_S32\_SIPI0\_CLK](#a4d8673a3b814bc9f14e15d50b57a7d2b)   265U |
| #define | [NXP\_S32\_SIPI1\_CLK](#a60c30b39d2e89c80fa211b43342ca99f)   266U |
| #define | [NXP\_S32\_SIUL2\_0\_CLK](#a89f492994987302439850a892121c9bc)   267U |
| #define | [NXP\_S32\_SIUL2\_1\_CLK](#a106bdd661bd1dfe6cad2159566a1d58b)   268U |
| #define | [NXP\_S32\_SIUL2\_4\_CLK](#a26724e2b1db403ef5358a59979a4817e)   269U |
| #define | [NXP\_S32\_SIUL2\_5\_CLK](#adc51aa185a667c281505c668ba927ada)   270U |
| #define | [NXP\_S32\_P0\_DSPI\_CLK](#a59f5b4f73193b3b1e85929f1a7de9b80)   271U |
| #define | [NXP\_S32\_SPI0\_CLK](#a2c652648965f6c8e327ef712df2d5c98)   272U |
| #define | [NXP\_S32\_SPI1\_CLK](#acd656ebd78f6fe746576be80a5d24f05)   273U |
| #define | [NXP\_S32\_P1\_DSPI\_CLK](#aac83716126559636a7cd20141299c36d)   274U |
| #define | [NXP\_S32\_SPI2\_CLK](#aeb3dd4f8dc24715c3b229fd65ea9456f)   275U |
| #define | [NXP\_S32\_SPI3\_CLK](#a09fc0d6d2b75ab6e248e21b2542e273f)   276U |
| #define | [NXP\_S32\_SPI4\_CLK](#aefb565e2a703339f27aae4b7b26d467d)   277U |
| #define | [NXP\_S32\_P4\_DSPI\_CLK](#a66ee0c09316a60b6e5232ff367d40c70)   278U |
| #define | [NXP\_S32\_SPI5\_CLK](#a5a28541a5df280d0d685098be4d78c83)   279U |
| #define | [NXP\_S32\_SPI6\_CLK](#a340ee2dfb7907910aa7bd846e78cf32c)   280U |
| #define | [NXP\_S32\_SPI7\_CLK](#a9a6f4147c148f3e1f429d10cf5747206)   281U |
| #define | [NXP\_S32\_P5\_DSPI\_CLK](#ac6ee2ed42df2274bf355662f940508dc)   282U |
| #define | [NXP\_S32\_SPI8\_CLK](#a6b7ab2e57f263ca785d2356c89d0f466)   283U |
| #define | [NXP\_S32\_SPI9\_CLK](#a150b128b301b737cc3cf00248d2ac9e3)   284U |
| #define | [NXP\_S32\_SRX0\_CLK](#af5454d5392cc7b9fa4bc2d846b2da80e)   285U |
| #define | [NXP\_S32\_SRX1\_CLK](#af014a5ddb774fe7c342e2ee3c3734487)   286U |

## Macro Definition Documentation

## [◆ ](#a89fe6bb1365a3895449da72ccd517223)NXP\_S32\_ADC0\_CLK

| #define NXP\_S32\_ADC0\_CLK   70U |
| --- |

## [◆ ](#ace9575b4ed012fe344884b0b1fa2ef58)NXP\_S32\_ADC1\_CLK

| #define NXP\_S32\_ADC1\_CLK   71U |
| --- |

## [◆ ](#ac81ef4f7bd981576b69426f195b010e3)NXP\_S32\_CE\_EDMA\_CLK

| #define NXP\_S32\_CE\_EDMA\_CLK   72U |
| --- |

## [◆ ](#a896f8242ee6ca821d912706775169ff4)NXP\_S32\_CE\_PIT0\_CLK

| #define NXP\_S32\_CE\_PIT0\_CLK   73U |
| --- |

## [◆ ](#a8fa4590c34477b07d6d902db44a28387)NXP\_S32\_CE\_PIT1\_CLK

| #define NXP\_S32\_CE\_PIT1\_CLK   74U |
| --- |

## [◆ ](#a02ddfc31f0ec38b341adb47bbfcfe43b)NXP\_S32\_CE\_PIT2\_CLK

| #define NXP\_S32\_CE\_PIT2\_CLK   75U |
| --- |

## [◆ ](#a7ad3dabd64d6358362e3ce6102542709)NXP\_S32\_CE\_PIT3\_CLK

| #define NXP\_S32\_CE\_PIT3\_CLK   76U |
| --- |

## [◆ ](#aa162dfc6ae281d398bd30efbb9d23eeb)NXP\_S32\_CE\_PIT4\_CLK

| #define NXP\_S32\_CE\_PIT4\_CLK   77U |
| --- |

## [◆ ](#a6bc8443e520ace278124978cc00080d6)NXP\_S32\_CE\_PIT5\_CLK

| #define NXP\_S32\_CE\_PIT5\_CLK   78U |
| --- |

## [◆ ](#ab6eb18cde38b8ca9dfa2b7181c41d6c0)NXP\_S32\_CE\_SYS\_DIV2\_CLK

| #define NXP\_S32\_CE\_SYS\_DIV2\_CLK   50U |
| --- |

## [◆ ](#a65a5ce3703f0c3c99e85654004783e88)NXP\_S32\_CE\_SYS\_DIV4\_CLK

| #define NXP\_S32\_CE\_SYS\_DIV4\_CLK   51U |
| --- |

## [◆ ](#a63aca9fbcdae28cd448e62e9dcf41da9)NXP\_S32\_CLKOUT0\_CLK

| #define NXP\_S32\_CLKOUT0\_CLK   79U |
| --- |

## [◆ ](#aed622cb6ba9b009aa0913c0e7d8f727f)NXP\_S32\_CLKOUT1\_CLK

| #define NXP\_S32\_CLKOUT1\_CLK   80U |
| --- |

## [◆ ](#a93cd425d58dd7d2ef73139487816b0f2)NXP\_S32\_CLKOUT2\_CLK

| #define NXP\_S32\_CLKOUT2\_CLK   81U |
| --- |

## [◆ ](#a24fc740cdbf049289b845e7c57f3653b)NXP\_S32\_CLKOUT3\_CLK

| #define NXP\_S32\_CLKOUT3\_CLK   82U |
| --- |

## [◆ ](#a0218b218e1ea001888490a74e824c5fa)NXP\_S32\_CLKOUT4\_CLK

| #define NXP\_S32\_CLKOUT4\_CLK   83U |
| --- |

## [◆ ](#ac66e693079884870e56f2b380a55eaed)NXP\_S32\_CORE\_M33\_CLK

| #define NXP\_S32\_CORE\_M33\_CLK   46U |
| --- |

## [◆ ](#a3adcd5e43f56ff0c41093ae141efac06)NXP\_S32\_COREPLL\_CLK

| #define NXP\_S32\_COREPLL\_CLK   4U |
| --- |

## [◆ ](#a3aed8d0791095ec97ec68dd5a31d5a16)NXP\_S32\_COREPLL\_DFS0\_CLK

| #define NXP\_S32\_COREPLL\_DFS0\_CLK   10U |
| --- |

## [◆ ](#ada9b9b2fcb4e577e0c04b5ec841cc73a)NXP\_S32\_COREPLL\_DFS1\_CLK

| #define NXP\_S32\_COREPLL\_DFS1\_CLK   11U |
| --- |

## [◆ ](#a1012a8d0b7baf417fede47e819ac03bc)NXP\_S32\_COREPLL\_DFS2\_CLK

| #define NXP\_S32\_COREPLL\_DFS2\_CLK   12U |
| --- |

## [◆ ](#a1e2cb85e953429dfd3b18af9c67a45ce)NXP\_S32\_COREPLL\_DFS3\_CLK

| #define NXP\_S32\_COREPLL\_DFS3\_CLK   13U |
| --- |

## [◆ ](#a50c5562659befb1e3a6633ca5f383265)NXP\_S32\_COREPLL\_DFS4\_CLK

| #define NXP\_S32\_COREPLL\_DFS4\_CLK   14U |
| --- |

## [◆ ](#a52c61d4e6b7907dcf5478c347cfc2f88)NXP\_S32\_COREPLL\_DFS5\_CLK

| #define NXP\_S32\_COREPLL\_DFS5\_CLK   15U |
| --- |

## [◆ ](#acf8fe39109c8d74a1ed277866460b3fb)NXP\_S32\_COREPLL\_PHI0\_CLK

| #define NXP\_S32\_COREPLL\_PHI0\_CLK   9U |
| --- |

## [◆ ](#a31bde6eec68fcfd8e76a497363276288)NXP\_S32\_CTU\_CLK

| #define NXP\_S32\_CTU\_CLK   84U |
| --- |

## [◆ ](#a28cbe95441f2e1691795ca86d29e5c0f)NXP\_S32\_DDR\_CLK

| #define NXP\_S32\_DDR\_CLK   40U |
| --- |

## [◆ ](#a7cb52f27a12b3f96f09eb351d93132cb)NXP\_S32\_DDRPLL\_CLK

| #define NXP\_S32\_DDRPLL\_CLK   6U |
| --- |

## [◆ ](#a6bc7d24858e5aacb50495395ca368695)NXP\_S32\_DDRPLL\_PHI0\_CLK

| #define NXP\_S32\_DDRPLL\_PHI0\_CLK   29U |
| --- |

## [◆ ](#abf95474bbeb9969a520edd298172941e)NXP\_S32\_DMACRC0\_CLK

| #define NXP\_S32\_DMACRC0\_CLK   85U |
| --- |

## [◆ ](#a0960ae83fd592bd62c12dbffb212f02a)NXP\_S32\_DMACRC1\_CLK

| #define NXP\_S32\_DMACRC1\_CLK   86U |
| --- |

## [◆ ](#aa486c18a096eebeec8afeb4d1ac98e91)NXP\_S32\_DMACRC4\_CLK

| #define NXP\_S32\_DMACRC4\_CLK   87U |
| --- |

## [◆ ](#a7ed644aafa5cec6aa0ad1521c29d9589)NXP\_S32\_DMACRC5\_CLK

| #define NXP\_S32\_DMACRC5\_CLK   88U |
| --- |

## [◆ ](#a97a3ff5238f4878784ee1bee4cfc7522)NXP\_S32\_DMAMUX0\_CLK

| #define NXP\_S32\_DMAMUX0\_CLK   89U |
| --- |

## [◆ ](#a708913d2bb71ec975caad705a10b8421)NXP\_S32\_DMAMUX1\_CLK

| #define NXP\_S32\_DMAMUX1\_CLK   90U |
| --- |

## [◆ ](#ae0650d4cdd3cca6a08666f0a0173a567)NXP\_S32\_DMAMUX4\_CLK

| #define NXP\_S32\_DMAMUX4\_CLK   91U |
| --- |

## [◆ ](#ad6fd147a074209f370ff0761b49c64a2)NXP\_S32\_DMAMUX5\_CLK

| #define NXP\_S32\_DMAMUX5\_CLK   92U |
| --- |

## [◆ ](#ae8b13f1f1803f214f7c7ba371679ee6f)NXP\_S32\_EDMA0\_CLK

| #define NXP\_S32\_EDMA0\_CLK   93U |
| --- |

## [◆ ](#a572adbd504ff44b0756578d38d8a9a7e)NXP\_S32\_EDMA1\_CLK

| #define NXP\_S32\_EDMA1\_CLK   94U |
| --- |

## [◆ ](#adc7573ce484dfda1662645ee5b959d86)NXP\_S32\_EDMA3\_CLK

| #define NXP\_S32\_EDMA3\_CLK   95U |
| --- |

## [◆ ](#a70e0508f328066120600422e31dd9bd6)NXP\_S32\_EDMA4\_CLK

| #define NXP\_S32\_EDMA4\_CLK   96U |
| --- |

## [◆ ](#ada44bb4bde41cfae4cbb5a30e615c27f)NXP\_S32\_EDMA5\_CLK

| #define NXP\_S32\_EDMA5\_CLK   97U |
| --- |

## [◆ ](#a42812f12a9d19b18a532ab3609829aa1)NXP\_S32\_ENET0\_CLK

| #define NXP\_S32\_ENET0\_CLK   99U |
| --- |

## [◆ ](#a12a72ae64ce2fca3bb59cbddde7f8ae4)NXP\_S32\_ETH0\_EXT\_RX\_CLK

| #define NXP\_S32\_ETH0\_EXT\_RX\_CLK   34U |
| --- |

## [◆ ](#a564bf352a181cf965b34b5da9b00a18d)NXP\_S32\_ETH0\_EXT\_TX\_CLK

| #define NXP\_S32\_ETH0\_EXT\_TX\_CLK   35U |
| --- |

## [◆ ](#a18158dcfbe35defc6ac3ddec5663f3d5)NXP\_S32\_ETH0\_PS\_TX\_CLK

| #define NXP\_S32\_ETH0\_PS\_TX\_CLK   183U |
| --- |

## [◆ ](#a66c5b71fe9de0e186911cdd3236ba930)NXP\_S32\_ETH0\_REF\_RMII\_CLK

| #define NXP\_S32\_ETH0\_REF\_RMII\_CLK   179U |
| --- |

## [◆ ](#acfefa0d9f76ac3429745527bccbdf712)NXP\_S32\_ETH0\_RX\_MII\_CLK

| #define NXP\_S32\_ETH0\_RX\_MII\_CLK   180U |
| --- |

## [◆ ](#ae7514957790fdbef6acfd5e637769e07)NXP\_S32\_ETH0\_RX\_RGMII\_CLK

| #define NXP\_S32\_ETH0\_RX\_RGMII\_CLK   181U |
| --- |

## [◆ ](#ac6cae2e8c1e0e49d24143da01bedbfd4)NXP\_S32\_ETH0\_TX\_MII\_CLK

| #define NXP\_S32\_ETH0\_TX\_MII\_CLK   98U |
| --- |

## [◆ ](#a2a7270a54cff6f0fd981b1892928d2d3)NXP\_S32\_ETH0\_TX\_RGMII\_CLK

| #define NXP\_S32\_ETH0\_TX\_RGMII\_CLK   182U |
| --- |

## [◆ ](#a4e3c08a9d415372a3884f8e1658f4de3)NXP\_S32\_ETH1\_EXT\_RX\_CLK

| #define NXP\_S32\_ETH1\_EXT\_RX\_CLK   36U |
| --- |

## [◆ ](#a5e2a62c4e47330fcd4d9e380ed0107ea)NXP\_S32\_ETH1\_EXT\_TX\_CLK

| #define NXP\_S32\_ETH1\_EXT\_TX\_CLK   37U |
| --- |

## [◆ ](#afb6c78fbfef3c83f07c3a13742bb0de6)NXP\_S32\_ETH1\_PS\_TX\_CLK

| #define NXP\_S32\_ETH1\_PS\_TX\_CLK   189U |
| --- |

## [◆ ](#a42ffe11005c05602e7c5f32c5cf31840)NXP\_S32\_ETH1\_REF\_RMII\_CLK

| #define NXP\_S32\_ETH1\_REF\_RMII\_CLK   184U |
| --- |

## [◆ ](#a8c70c175327045d0dc20f9934e9c2bcb)NXP\_S32\_ETH1\_RX\_MII\_CLK

| #define NXP\_S32\_ETH1\_RX\_MII\_CLK   185U |
| --- |

## [◆ ](#a00adcfabd053d720460129a0f75a7528)NXP\_S32\_ETH1\_RX\_RGMII\_CLK

| #define NXP\_S32\_ETH1\_RX\_RGMII\_CLK   186U |
| --- |

## [◆ ](#a456af1ef69789bb71b922462520d4bed)NXP\_S32\_ETH1\_TX\_MII\_CLK

| #define NXP\_S32\_ETH1\_TX\_MII\_CLK   187U |
| --- |

## [◆ ](#a614779666ceeb1d9dadf0aa64280f19c)NXP\_S32\_ETH1\_TX\_RGMII\_CLK

| #define NXP\_S32\_ETH1\_TX\_RGMII\_CLK   188U |
| --- |

## [◆ ](#a25c75209f8f1f75734aede68aa358744)NXP\_S32\_ETH\_RGMII\_REF\_CLK

| #define NXP\_S32\_ETH\_RGMII\_REF\_CLK   32U |
| --- |

## [◆ ](#a88a8f9a494f68937d827887eb881a186)NXP\_S32\_ETH\_TS\_CLK

| #define NXP\_S32\_ETH\_TS\_CLK   177U |
| --- |

## [◆ ](#aaac96cff7479ae5452aa5faecf8c24fd)NXP\_S32\_ETH\_TS\_DIV4\_CLK

| #define NXP\_S32\_ETH\_TS\_DIV4\_CLK   178U |
| --- |

## [◆ ](#a8f4673a159fb26c90ae29761784395e9)NXP\_S32\_FIRC\_CLK

| #define NXP\_S32\_FIRC\_CLK   1U |
| --- |

## [◆ ](#a308e74a366725070c56a4ab4fc7c300a)NXP\_S32\_FLEXCAN0\_CLK

| #define NXP\_S32\_FLEXCAN0\_CLK   101U |
| --- |

## [◆ ](#a8fff5e2c245578e94f4e9ed4eddfc19b)NXP\_S32\_FLEXCAN10\_CLK

| #define NXP\_S32\_FLEXCAN10\_CLK   111U |
| --- |

## [◆ ](#a875232291fcb4035ea178013d1996300)NXP\_S32\_FLEXCAN11\_CLK

| #define NXP\_S32\_FLEXCAN11\_CLK   112U |
| --- |

## [◆ ](#a0149861a754ec061781b59813e9bb5ea)NXP\_S32\_FLEXCAN12\_CLK

| #define NXP\_S32\_FLEXCAN12\_CLK   113U |
| --- |

## [◆ ](#af92372e349573e82108e2d858d7bed52)NXP\_S32\_FLEXCAN13\_CLK

| #define NXP\_S32\_FLEXCAN13\_CLK   114U |
| --- |

## [◆ ](#adc7b3ae5cfc1fe779b0075626fae2328)NXP\_S32\_FLEXCAN14\_CLK

| #define NXP\_S32\_FLEXCAN14\_CLK   115U |
| --- |

## [◆ ](#a55351634b1b77419c5f2aeccdd917ebe)NXP\_S32\_FLEXCAN15\_CLK

| #define NXP\_S32\_FLEXCAN15\_CLK   116U |
| --- |

## [◆ ](#aa95b2f2eceb55537b99e6a14f84f17d1)NXP\_S32\_FLEXCAN16\_CLK

| #define NXP\_S32\_FLEXCAN16\_CLK   117U |
| --- |

## [◆ ](#acaed7d12a46279f9a3a5af4fde4e5693)NXP\_S32\_FLEXCAN17\_CLK

| #define NXP\_S32\_FLEXCAN17\_CLK   118U |
| --- |

## [◆ ](#a204e919465814538dd49dd775eb2f8f6)NXP\_S32\_FLEXCAN18\_CLK

| #define NXP\_S32\_FLEXCAN18\_CLK   119U |
| --- |

## [◆ ](#a3421175f2c69e71bfa90cf8b34e69c5b)NXP\_S32\_FLEXCAN19\_CLK

| #define NXP\_S32\_FLEXCAN19\_CLK   120U |
| --- |

## [◆ ](#ad353c07d914cfa8c45ed3b7b586c2b00)NXP\_S32\_FLEXCAN1\_CLK

| #define NXP\_S32\_FLEXCAN1\_CLK   102U |
| --- |

## [◆ ](#a4f44e36a65a4e2422fd3b72e246b7170)NXP\_S32\_FLEXCAN20\_CLK

| #define NXP\_S32\_FLEXCAN20\_CLK   121U |
| --- |

## [◆ ](#a9c6e9291e6d310a4a41f0ea3d6810b79)NXP\_S32\_FLEXCAN21\_CLK

| #define NXP\_S32\_FLEXCAN21\_CLK   122U |
| --- |

## [◆ ](#a0890c9d64890e95b8de85914eb773986)NXP\_S32\_FLEXCAN22\_CLK

| #define NXP\_S32\_FLEXCAN22\_CLK   123U |
| --- |

## [◆ ](#a98a67a530a8ab4602974248029953934)NXP\_S32\_FLEXCAN23\_CLK

| #define NXP\_S32\_FLEXCAN23\_CLK   124U |
| --- |

## [◆ ](#a54467688a58d9be77849eddd031f126e)NXP\_S32\_FLEXCAN2\_CLK

| #define NXP\_S32\_FLEXCAN2\_CLK   103U |
| --- |

## [◆ ](#a0fcf00296138cd26e845ab524054fd3b)NXP\_S32\_FLEXCAN3\_CLK

| #define NXP\_S32\_FLEXCAN3\_CLK   104U |
| --- |

## [◆ ](#a6106f0f8b5e0f5230b75e43b5ccdbf0e)NXP\_S32\_FLEXCAN4\_CLK

| #define NXP\_S32\_FLEXCAN4\_CLK   105U |
| --- |

## [◆ ](#a4f3b1864f3f5bcc6a1fd66e27eb12a52)NXP\_S32\_FLEXCAN5\_CLK

| #define NXP\_S32\_FLEXCAN5\_CLK   106U |
| --- |

## [◆ ](#aab3b5b178be344b18c4c9ca27786eb03)NXP\_S32\_FLEXCAN6\_CLK

| #define NXP\_S32\_FLEXCAN6\_CLK   107U |
| --- |

## [◆ ](#a5c239f32216a44b5282e5ffd9fdd214f)NXP\_S32\_FLEXCAN7\_CLK

| #define NXP\_S32\_FLEXCAN7\_CLK   108U |
| --- |

## [◆ ](#afb62f9c88f6652a3382197c10456c8b9)NXP\_S32\_FLEXCAN8\_CLK

| #define NXP\_S32\_FLEXCAN8\_CLK   109U |
| --- |

## [◆ ](#a3f8baea9230234e8e9dafdbe1dadc005)NXP\_S32\_FLEXCAN9\_CLK

| #define NXP\_S32\_FLEXCAN9\_CLK   110U |
| --- |

## [◆ ](#ae1a59aa87c82395e1badae9f62a8345a)NXP\_S32\_FRAY0\_CLK

| #define NXP\_S32\_FRAY0\_CLK   126U |
| --- |

## [◆ ](#abe6b9172ef85c386ab5ad017533ba1ee)NXP\_S32\_FRAY1\_CLK

| #define NXP\_S32\_FRAY1\_CLK   127U |
| --- |

## [◆ ](#ab748e7ec615dc5fe10cafc723cc289fe)NXP\_S32\_FXOSC\_CLK

| #define NXP\_S32\_FXOSC\_CLK   2U |
| --- |

## [◆ ](#a8eca101146810d0b95493c66a19b7b16)NXP\_S32\_GLB\_LBIST\_CLK

| #define NXP\_S32\_GLB\_LBIST\_CLK   62U |
| --- |

## [◆ ](#af5f8881fdd6fc0b160ecbbccfc34df88)NXP\_S32\_GTM\_CLK

| #define NXP\_S32\_GTM\_CLK   128U |
| --- |

## [◆ ](#af36e2f8d5d39189013c65589eaaf3da2)NXP\_S32\_HSE\_SYS\_DIV2\_CLK

| #define NXP\_S32\_HSE\_SYS\_DIV2\_CLK   56U |
| --- |

## [◆ ](#afa13966ea5003a4018851341485db5c7)NXP\_S32\_IIIC0\_CLK

| #define NXP\_S32\_IIIC0\_CLK   129U |
| --- |

## [◆ ](#ac18c5d32153412256754f0a8871a3613)NXP\_S32\_IIIC1\_CLK

| #define NXP\_S32\_IIIC1\_CLK   130U |
| --- |

## [◆ ](#a56d46603e3275969d77401c2404f1105)NXP\_S32\_IIIC2\_CLK

| #define NXP\_S32\_IIIC2\_CLK   131U |
| --- |

## [◆ ](#a08658b7dbf05f325c8dcad2f609b714d)NXP\_S32\_LFAST0\_EXT\_REF\_CLK

| #define NXP\_S32\_LFAST0\_EXT\_REF\_CLK   38U |
| --- |

## [◆ ](#a2cb385d2116bc56f05be3bde7b83e718)NXP\_S32\_LFAST0\_PLL\_CLK

| #define NXP\_S32\_LFAST0\_PLL\_CLK   7U |
| --- |

## [◆ ](#aaf01394fcd23fdcff4792684b1a970d8)NXP\_S32\_LFAST0\_PLL\_PH0\_CLK

| #define NXP\_S32\_LFAST0\_PLL\_PH0\_CLK   30U |
| --- |

## [◆ ](#a84b1c38882e6af516c04909671427d4a)NXP\_S32\_LFAST1\_EXT\_REF\_CLK

| #define NXP\_S32\_LFAST1\_EXT\_REF\_CLK   39U |
| --- |

## [◆ ](#a2bce68111fdacf004a33b94c0c898c02)NXP\_S32\_LFAST1\_PLL\_CLK

| #define NXP\_S32\_LFAST1\_PLL\_CLK   8U |
| --- |

## [◆ ](#a3d00b3751ab9bccaf4471bfab3d5d522)NXP\_S32\_LFAST1\_PLL\_PH0\_CLK

| #define NXP\_S32\_LFAST1\_PLL\_PH0\_CLK   31U |
| --- |

## [◆ ](#ab398d341ee088a2913a096ec2b9b6545)NXP\_S32\_LIN0\_CLK

| #define NXP\_S32\_LIN0\_CLK   133U |
| --- |

## [◆ ](#a926d082c5223bcdc027e220190ec2e41)NXP\_S32\_LIN10\_CLK

| #define NXP\_S32\_LIN10\_CLK   146U |
| --- |

## [◆ ](#a9475a59878a242d95a90c69c1e5b78d9)NXP\_S32\_LIN11\_CLK

| #define NXP\_S32\_LIN11\_CLK   147U |
| --- |

## [◆ ](#ae4867ba422c49414a6e32b7170f19398)NXP\_S32\_LIN1\_CLK

| #define NXP\_S32\_LIN1\_CLK   134U |
| --- |

## [◆ ](#a7138bcb68270ae9f46539ffc65cd34dd)NXP\_S32\_LIN2\_CLK

| #define NXP\_S32\_LIN2\_CLK   135U |
| --- |

## [◆ ](#aae3a89eaeca09ae97ad3ba0132632b7b)NXP\_S32\_LIN3\_CLK

| #define NXP\_S32\_LIN3\_CLK   137U |
| --- |

## [◆ ](#a0953f6ad3c2f2f84a82927d8ed979d2e)NXP\_S32\_LIN4\_CLK

| #define NXP\_S32\_LIN4\_CLK   138U |
| --- |

## [◆ ](#a2f1405a5d9a3e3e03d2b607f064c9c49)NXP\_S32\_LIN5\_CLK

| #define NXP\_S32\_LIN5\_CLK   139U |
| --- |

## [◆ ](#a8f0dc1e8fa2449e42f1e1371ed3526bc)NXP\_S32\_LIN6\_CLK

| #define NXP\_S32\_LIN6\_CLK   141U |
| --- |

## [◆ ](#a0e14ecb12403a221a992eb6f6970d324)NXP\_S32\_LIN7\_CLK

| #define NXP\_S32\_LIN7\_CLK   142U |
| --- |

## [◆ ](#a6d8815173be045f717ee61f5770dd2ca)NXP\_S32\_LIN8\_CLK

| #define NXP\_S32\_LIN8\_CLK   143U |
| --- |

## [◆ ](#a3d55f195f31e6fdfeecdb2d712564e82)NXP\_S32\_LIN9\_CLK

| #define NXP\_S32\_LIN9\_CLK   145U |
| --- |

## [◆ ](#ad98b9a2b348c6e58f41420a47a5e2ba8)NXP\_S32\_MSCDSPI\_CLK

| #define NXP\_S32\_MSCDSPI\_CLK   148U |
| --- |

## [◆ ](#a0d21ae71b95bcfc407f67053dd202288)NXP\_S32\_MSCLIN\_CLK

| #define NXP\_S32\_MSCLIN\_CLK   149U |
| --- |

## [◆ ](#a962245016be6213059cefaabe2c5d96e)NXP\_S32\_NANO\_CLK

| #define NXP\_S32\_NANO\_CLK   150U |
| --- |

## [◆ ](#ab82b29897283f400bd543368f8b1fc73)NXP\_S32\_P0\_CLKOUT\_SRC\_CLK

| #define NXP\_S32\_P0\_CLKOUT\_SRC\_CLK   151U |
| --- |

## [◆ ](#af80cf625f75ceb16fabb4f3a52e8154c)NXP\_S32\_P0\_CTU\_PER\_CLK

| #define NXP\_S32\_P0\_CTU\_PER\_CLK   152U |
| --- |

## [◆ ](#a59f5b4f73193b3b1e85929f1a7de9b80)NXP\_S32\_P0\_DSPI\_CLK

| #define NXP\_S32\_P0\_DSPI\_CLK   271U |
| --- |

## [◆ ](#a714fae0bdcbe4980f167cb222d008da5)NXP\_S32\_P0\_DSPI\_MSC\_CLK

| #define NXP\_S32\_P0\_DSPI\_MSC\_CLK   153U |
| --- |

## [◆ ](#a16ffc4b60ef57064c790dbe9c0bca6b9)NXP\_S32\_P0\_EMIOS\_LCU\_CLK

| #define NXP\_S32\_P0\_EMIOS\_LCU\_CLK   154U |
| --- |

## [◆ ](#a359bad70140a01914fbb90541c178226)NXP\_S32\_P0\_FR\_PE\_CLK

| #define NXP\_S32\_P0\_FR\_PE\_CLK   125U |
| --- |

## [◆ ](#a686525770665c07bd423523d3a36b3ac)NXP\_S32\_P0\_GTM\_CLK

| #define NXP\_S32\_P0\_GTM\_CLK   155U |
| --- |

## [◆ ](#afbdfad00c82da171e55148b6239e42d3)NXP\_S32\_P0\_GTM\_NOC\_CLK

| #define NXP\_S32\_P0\_GTM\_NOC\_CLK   156U |
| --- |

## [◆ ](#a23a8ea48e3fd40e86ba10a26c50729cb)NXP\_S32\_P0\_GTM\_TS\_CLK

| #define NXP\_S32\_P0\_GTM\_TS\_CLK   157U |
| --- |

## [◆ ](#a71af2c2cf427a16f1b8d0d1ef6d5c5c5)NXP\_S32\_P0\_LIN\_BAUD\_CLK

| #define NXP\_S32\_P0\_LIN\_BAUD\_CLK   132U |
| --- |

## [◆ ](#a25b98ce36a908555b566240eef0eeb32)NXP\_S32\_P0\_LIN\_CLK

| #define NXP\_S32\_P0\_LIN\_CLK   158U |
| --- |

## [◆ ](#a58a1b67087d393bcd87aa1021a602610)NXP\_S32\_P0\_NANO\_CLK

| #define NXP\_S32\_P0\_NANO\_CLK   159U |
| --- |

## [◆ ](#ad26f0c08b0ba71b1322bd0d96f39d088)NXP\_S32\_P0\_PSI5\_125K\_CLK

| #define NXP\_S32\_P0\_PSI5\_125K\_CLK   160U |
| --- |

## [◆ ](#a26c4eb3cc201d79da9e694fc9978db99)NXP\_S32\_P0\_PSI5\_189K\_CLK

| #define NXP\_S32\_P0\_PSI5\_189K\_CLK   161U |
| --- |

## [◆ ](#ac6dffda41839ba589fe4d47bdbf12651)NXP\_S32\_P0\_PSI5\_1US\_CLK

| #define NXP\_S32\_P0\_PSI5\_1US\_CLK   241U |
| --- |

## [◆ ](#a459ee3a15bc7a5c9fe51e6005643afd6)NXP\_S32\_P0\_PSI5\_S\_BAUD\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_BAUD\_CLK   162U |
| --- |

## [◆ ](#a8cd9818e35f2504faae149799a0d9638)NXP\_S32\_P0\_PSI5\_S\_CORE\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_CORE\_CLK   163U |
| --- |

## [◆ ](#a19696ed6e7de7562c5a8b4986860ad82)NXP\_S32\_P0\_PSI5\_S\_TRIG0\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_TRIG0\_CLK   164U |
| --- |

## [◆ ](#aedbd34b2064ac95af9c17a5456ff3855)NXP\_S32\_P0\_PSI5\_S\_TRIG1\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_TRIG1\_CLK   165U |
| --- |

## [◆ ](#a36af4e664ef882746b52c50e1a360d41)NXP\_S32\_P0\_PSI5\_S\_TRIG2\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_TRIG2\_CLK   166U |
| --- |

## [◆ ](#a8b9934ce90c2fe91e6b0eeebe3c8459f)NXP\_S32\_P0\_PSI5\_S\_TRIG3\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_TRIG3\_CLK   167U |
| --- |

## [◆ ](#a068a54a8fbe24cec08b1fd50a08a22c6)NXP\_S32\_P0\_PSI5\_S\_UART\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_UART\_CLK   168U |
| --- |

## [◆ ](#a522a9b1e7ba5816155bf057ffbb4f2fe)NXP\_S32\_P0\_PSI5\_S\_UTIL\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_UTIL\_CLK   67U |
| --- |

## [◆ ](#a01ae4eeb18f55302d7a71720cc51ae66)NXP\_S32\_P0\_PSI5\_S\_WDOG0\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_WDOG0\_CLK   169U |
| --- |

## [◆ ](#a1982f9aa465e31f26a744b84f62ef1b0)NXP\_S32\_P0\_PSI5\_S\_WDOG1\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_WDOG1\_CLK   170U |
| --- |

## [◆ ](#a8673cb557d9e66cad14e8b39f5ade479)NXP\_S32\_P0\_PSI5\_S\_WDOG2\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_WDOG2\_CLK   171U |
| --- |

## [◆ ](#ad85a63ab4506c854ebaf56be3cd1ff1f)NXP\_S32\_P0\_PSI5\_S\_WDOG3\_CLK

| #define NXP\_S32\_P0\_PSI5\_S\_WDOG3\_CLK   172U |
| --- |

## [◆ ](#ae8de22703b3e0dd10b9825da9fab7bf6)NXP\_S32\_P0\_REG\_INTF\_2X\_CLK

| #define NXP\_S32\_P0\_REG\_INTF\_2X\_CLK   173U |
| --- |

## [◆ ](#a2ff5e51b07be18df4010f50c24e2a17a)NXP\_S32\_P0\_REG\_INTF\_CLK

| #define NXP\_S32\_P0\_REG\_INTF\_CLK   174U |
| --- |

## [◆ ](#abc6c662bf88c9a922478bf368ef7416c)NXP\_S32\_P0\_SYS\_CLK

| #define NXP\_S32\_P0\_SYS\_CLK   41U |
| --- |

## [◆ ](#a90a14473f0c5fc9ea47849d8d225dfe0)NXP\_S32\_P1\_CLKOUT\_SRC\_CLK

| #define NXP\_S32\_P1\_CLKOUT\_SRC\_CLK   175U |
| --- |

## [◆ ](#a5550b2018e416e7b4077b11cbee0454a)NXP\_S32\_P1\_DSPI60\_CLK

| #define NXP\_S32\_P1\_DSPI60\_CLK   176U |
| --- |

## [◆ ](#aac83716126559636a7cd20141299c36d)NXP\_S32\_P1\_DSPI\_CLK

| #define NXP\_S32\_P1\_DSPI\_CLK   274U |
| --- |

## [◆ ](#ac2b71011cd7efab96ed82e0dec53ebbf)NXP\_S32\_P1\_LFAST0\_REF\_CLK

| #define NXP\_S32\_P1\_LFAST0\_REF\_CLK   190U |
| --- |

## [◆ ](#a8f7fa9b6fc70d559f42c100ab043ed0b)NXP\_S32\_P1\_LFAST1\_REF\_CLK

| #define NXP\_S32\_P1\_LFAST1\_REF\_CLK   191U |
| --- |

## [◆ ](#a9b0b135bf98d9982e26547801c0452cd)NXP\_S32\_P1\_LIN\_BAUD\_CLK

| #define NXP\_S32\_P1\_LIN\_BAUD\_CLK   136U |
| --- |

## [◆ ](#a2d9be627f771273bd7153ffc2f67de49)NXP\_S32\_P1\_LIN\_CLK

| #define NXP\_S32\_P1\_LIN\_CLK   193U |
| --- |

## [◆ ](#adbda03e5f3ec46eeeb4d80037fcee6ec)NXP\_S32\_P1\_NETC\_AXI\_CLK

| #define NXP\_S32\_P1\_NETC\_AXI\_CLK   192U |
| --- |

## [◆ ](#a4b289b2abb24d96be3154a0d708c47a2)NXP\_S32\_P1\_REG\_INTF\_CLK

| #define NXP\_S32\_P1\_REG\_INTF\_CLK   194U |
| --- |

## [◆ ](#ab65e705e34df2a7428493b1c232fc6fd)NXP\_S32\_P1\_SYS\_CLK

| #define NXP\_S32\_P1\_SYS\_CLK   42U |
| --- |

## [◆ ](#a4e44f6e2575430b847296bb0336a555f)NXP\_S32\_P1\_SYS\_DIV2\_CLK

| #define NXP\_S32\_P1\_SYS\_DIV2\_CLK   43U |
| --- |

## [◆ ](#a725ad3fb6496a459f4719f64658478a1)NXP\_S32\_P1\_SYS\_DIV4\_CLK

| #define NXP\_S32\_P1\_SYS\_DIV4\_CLK   44U |
| --- |

## [◆ ](#a5c1ed5c4139f5bb21fd516b34c470a84)NXP\_S32\_P2\_DBG\_ATB\_CLK

| #define NXP\_S32\_P2\_DBG\_ATB\_CLK   195U |
| --- |

## [◆ ](#afdd0087c9c7473debe2c36f9c4b3b9eb)NXP\_S32\_P2\_MATH\_CLK

| #define NXP\_S32\_P2\_MATH\_CLK   60U |
| --- |

## [◆ ](#a43b5a621c2e3a2ed9b3b5b6a5742c5fa)NXP\_S32\_P2\_MATH\_DIV3\_CLK

| #define NXP\_S32\_P2\_MATH\_DIV3\_CLK   61U |
| --- |

## [◆ ](#a094ca57b0793143a9c556793653c4b2a)NXP\_S32\_P2\_REG\_INTF\_CLK

| #define NXP\_S32\_P2\_REG\_INTF\_CLK   196U |
| --- |

## [◆ ](#aa5d06e65e92b43483cecfa7608abb8d6)NXP\_S32\_P2\_SYS\_CLK

| #define NXP\_S32\_P2\_SYS\_CLK   45U |
| --- |

## [◆ ](#a0f5ffbc3acf02add006d35efa94ca3a6)NXP\_S32\_P2\_SYS\_DIV2\_CLK

| #define NXP\_S32\_P2\_SYS\_DIV2\_CLK   47U |
| --- |

## [◆ ](#abb48ce40572d7f0f174b644930d949cc)NXP\_S32\_P2\_SYS\_DIV4\_CLK

| #define NXP\_S32\_P2\_SYS\_DIV4\_CLK   48U |
| --- |

## [◆ ](#aa57d5790115ef7ac68418adeef94fa0c)NXP\_S32\_P3\_AES\_CLK

| #define NXP\_S32\_P3\_AES\_CLK   197U |
| --- |

## [◆ ](#af42ddf0adf09c31916350082dc472cba)NXP\_S32\_P3\_CAN\_PE\_CLK

| #define NXP\_S32\_P3\_CAN\_PE\_CLK   100U |
| --- |

## [◆ ](#a930fe7099338293129386fe6cc6411fa)NXP\_S32\_P3\_CLKOUT\_SRC\_CLK

| #define NXP\_S32\_P3\_CLKOUT\_SRC\_CLK   198U |
| --- |

## [◆ ](#acecb11af2da42a7e30e6db63da1fdca9)NXP\_S32\_P3\_DBG\_TS\_CLK

| #define NXP\_S32\_P3\_DBG\_TS\_CLK   199U |
| --- |

## [◆ ](#a2c1da162ffec0cf4c6c384c95fba1bc9)NXP\_S32\_P3\_REG\_INTF\_CLK

| #define NXP\_S32\_P3\_REG\_INTF\_CLK   200U |
| --- |

## [◆ ](#a5557d1a39d866ddc1e7baa7c8e6ff9f0)NXP\_S32\_P3\_SYS\_CLK

| #define NXP\_S32\_P3\_SYS\_CLK   49U |
| --- |

## [◆ ](#a47d136a5e21ff3031bd7b9eb0075d8f6)NXP\_S32\_P3\_SYS\_DIV2\_NOC\_CLK

| #define NXP\_S32\_P3\_SYS\_DIV2\_NOC\_CLK   52U |
| --- |

## [◆ ](#a07633bb8f64c1125935a2b28ad5bf485)NXP\_S32\_P3\_SYS\_DIV4\_CLK

| #define NXP\_S32\_P3\_SYS\_DIV4\_CLK   53U |
| --- |

## [◆ ](#afef936923819e2b7d5b47e1dbbcdb20a)NXP\_S32\_P3\_SYS\_MON1\_CLK

| #define NXP\_S32\_P3\_SYS\_MON1\_CLK   201U |
| --- |

## [◆ ](#adcee0fba1f18ea4a638cd925fe6a6cd1)NXP\_S32\_P3\_SYS\_MON2\_CLK

| #define NXP\_S32\_P3\_SYS\_MON2\_CLK   202U |
| --- |

## [◆ ](#a8bf6a442c62a58bb30dea1690b672f02)NXP\_S32\_P3\_SYS\_MON3\_CLK

| #define NXP\_S32\_P3\_SYS\_MON3\_CLK   203U |
| --- |

## [◆ ](#afeaf9f77f9b1c38c85a5929d1de41c29)NXP\_S32\_P4\_CLKOUT\_SRC\_CLK

| #define NXP\_S32\_P4\_CLKOUT\_SRC\_CLK   204U |
| --- |

## [◆ ](#a56310949c10c299c71459ae2519d983a)NXP\_S32\_P4\_DSPI60\_CLK

| #define NXP\_S32\_P4\_DSPI60\_CLK   205U |
| --- |

## [◆ ](#a66ee0c09316a60b6e5232ff367d40c70)NXP\_S32\_P4\_DSPI\_CLK

| #define NXP\_S32\_P4\_DSPI\_CLK   278U |
| --- |

## [◆ ](#ae42588a847179f18a866d6a8d783d109)NXP\_S32\_P4\_EMIOS\_LCU\_CLK

| #define NXP\_S32\_P4\_EMIOS\_LCU\_CLK   206U |
| --- |

## [◆ ](#a34da0d2172d9eff2f9edf40e980bd980)NXP\_S32\_P4\_LIN\_BAUD\_CLK

| #define NXP\_S32\_P4\_LIN\_BAUD\_CLK   140U |
| --- |

## [◆ ](#ac4a8f99f98db71f920c138949623d4bc)NXP\_S32\_P4\_LIN\_CLK

| #define NXP\_S32\_P4\_LIN\_CLK   207U |
| --- |

## [◆ ](#a6a643398df1a3d6dc1400e276ac6b834)NXP\_S32\_P4\_PSI5\_125K\_CLK

| #define NXP\_S32\_P4\_PSI5\_125K\_CLK   208U |
| --- |

## [◆ ](#ad48ea0e82a482982976fcc0751613e70)NXP\_S32\_P4\_PSI5\_189K\_CLK

| #define NXP\_S32\_P4\_PSI5\_189K\_CLK   209U |
| --- |

## [◆ ](#add87638b86bfb3519aa0f225f6490035)NXP\_S32\_P4\_PSI5\_1US\_CLK

| #define NXP\_S32\_P4\_PSI5\_1US\_CLK   243U |
| --- |

## [◆ ](#a00a480f922125287f141c90425884bbb)NXP\_S32\_P4\_PSI5\_S\_BAUD\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_BAUD\_CLK   210U |
| --- |

## [◆ ](#a51ebed20f61106859cbfda8512746c82)NXP\_S32\_P4\_PSI5\_S\_CORE\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_CORE\_CLK   211U |
| --- |

## [◆ ](#abeb2096f22a4bb8cd17e44afc43e21cf)NXP\_S32\_P4\_PSI5\_S\_TRIG0\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_TRIG0\_CLK   212U |
| --- |

## [◆ ](#a3e458ecf52aba2c8023558b205722d1e)NXP\_S32\_P4\_PSI5\_S\_TRIG1\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_TRIG1\_CLK   213U |
| --- |

## [◆ ](#a1e41cc7c6d18670e678c41f8054e4955)NXP\_S32\_P4\_PSI5\_S\_TRIG2\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_TRIG2\_CLK   214U |
| --- |

## [◆ ](#a3306bde399a946b4acb0e8a8422e8a5e)NXP\_S32\_P4\_PSI5\_S\_TRIG3\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_TRIG3\_CLK   215U |
| --- |

## [◆ ](#a7363852a4dbae0d1dce3c1e1ca69c942)NXP\_S32\_P4\_PSI5\_S\_UART\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_UART\_CLK   216U |
| --- |

## [◆ ](#ad0e0022e42d0b941e0edd976837d1b00)NXP\_S32\_P4\_PSI5\_S\_UTIL\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_UTIL\_CLK   68U |
| --- |

## [◆ ](#ae8f7f8894849326fd7de463c28eb2750)NXP\_S32\_P4\_PSI5\_S\_WDOG0\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_WDOG0\_CLK   217U |
| --- |

## [◆ ](#a4503412c69019cbe9e1f360e730021c5)NXP\_S32\_P4\_PSI5\_S\_WDOG1\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_WDOG1\_CLK   218U |
| --- |

## [◆ ](#a7b746bc4545d654e80d34737e35294d8)NXP\_S32\_P4\_PSI5\_S\_WDOG2\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_WDOG2\_CLK   219U |
| --- |

## [◆ ](#a29c1b1fc11a2bd4a56589ad261e1ef0b)NXP\_S32\_P4\_PSI5\_S\_WDOG3\_CLK

| #define NXP\_S32\_P4\_PSI5\_S\_WDOG3\_CLK   220U |
| --- |

## [◆ ](#abcc5e81770a40ab5c14a11ab61325405)NXP\_S32\_P4\_QSPI0\_1X\_CLK

| #define NXP\_S32\_P4\_QSPI0\_1X\_CLK   222U |
| --- |

## [◆ ](#a7a57d71043cdaf8592eef030151feca1)NXP\_S32\_P4\_QSPI0\_2X\_CLK

| #define NXP\_S32\_P4\_QSPI0\_2X\_CLK   221U |
| --- |

## [◆ ](#ab03050d789f565fdb401ccb60d7b58a5)NXP\_S32\_P4\_QSPI1\_1X\_CLK

| #define NXP\_S32\_P4\_QSPI1\_1X\_CLK   224U |
| --- |

## [◆ ](#aba7b321632d765a70826933e169f1d51)NXP\_S32\_P4\_QSPI1\_2X\_CLK

| #define NXP\_S32\_P4\_QSPI1\_2X\_CLK   223U |
| --- |

## [◆ ](#a74e0d39f05366c27f26a157e2b4d4b76)NXP\_S32\_P4\_REG\_INTF\_2X\_CLK

| #define NXP\_S32\_P4\_REG\_INTF\_2X\_CLK   225U |
| --- |

## [◆ ](#a9c2dd8c4e369a43d53a0884bb9e42c2b)NXP\_S32\_P4\_REG\_INTF\_CLK

| #define NXP\_S32\_P4\_REG\_INTF\_CLK   226U |
| --- |

## [◆ ](#af22478974ea14d932259e929cf524c3b)NXP\_S32\_P4\_SDHC\_CLK

| #define NXP\_S32\_P4\_SDHC\_CLK   261U |
| --- |

## [◆ ](#a74fdff2722d49e0dcb913e7189f51377)NXP\_S32\_P4\_SDHC\_IP\_CLK

| #define NXP\_S32\_P4\_SDHC\_IP\_CLK   227U |
| --- |

## [◆ ](#a6ab6b60ac5091add4e31b72cc09599f1)NXP\_S32\_P4\_SDHC\_IP\_DIV2\_CLK

| #define NXP\_S32\_P4\_SDHC\_IP\_DIV2\_CLK   228U |
| --- |

## [◆ ](#ac81524f01ee44bab50879663fc242211)NXP\_S32\_P4\_SYS\_CLK

| #define NXP\_S32\_P4\_SYS\_CLK   54U |
| --- |

## [◆ ](#ac2cd9425cd2eb8e8c29d5716259034df)NXP\_S32\_P4\_SYS\_DIV2\_CLK

| #define NXP\_S32\_P4\_SYS\_DIV2\_CLK   55U |
| --- |

## [◆ ](#abd484d3b8a562990e7656841269bfa28)NXP\_S32\_P5\_AE\_CLK

| #define NXP\_S32\_P5\_AE\_CLK   230U |
| --- |

## [◆ ](#a839ce35505017fbb12ace1f0b897e036)NXP\_S32\_P5\_CANXL\_CHI\_CLK

| #define NXP\_S32\_P5\_CANXL\_CHI\_CLK   232U |
| --- |

## [◆ ](#aa95a8c461eb4dff35ff6437107da575d)NXP\_S32\_P5\_CANXL\_PE\_CLK

| #define NXP\_S32\_P5\_CANXL\_PE\_CLK   231U |
| --- |

## [◆ ](#a3994f4206e051b06c788dae82b02c7c2)NXP\_S32\_P5\_CLKOUT\_SRC\_CLK

| #define NXP\_S32\_P5\_CLKOUT\_SRC\_CLK   233U |
| --- |

## [◆ ](#ad464e90d729864b48a331e74293060e0)NXP\_S32\_P5\_DIPORT\_CLK

| #define NXP\_S32\_P5\_DIPORT\_CLK   229U |
| --- |

## [◆ ](#ac6ee2ed42df2274bf355662f940508dc)NXP\_S32\_P5\_DSPI\_CLK

| #define NXP\_S32\_P5\_DSPI\_CLK   282U |
| --- |

## [◆ ](#a5e3508c56acc88ca6a4fb04f5b59f7bc)NXP\_S32\_P5\_LIN\_BAUD\_CLK

| #define NXP\_S32\_P5\_LIN\_BAUD\_CLK   144U |
| --- |

## [◆ ](#a758bf0b991fa5d9fed76f93276e829fa)NXP\_S32\_P5\_LIN\_CLK

| #define NXP\_S32\_P5\_LIN\_CLK   234U |
| --- |

## [◆ ](#a49d5460d77183f7a98a4a236bc6f2b5a)NXP\_S32\_P5\_REG\_INTF\_CLK

| #define NXP\_S32\_P5\_REG\_INTF\_CLK   235U |
| --- |

## [◆ ](#a8fdb0b99d90aa47b3a16aa8df92a23ba)NXP\_S32\_P5\_SYS\_CLK

| #define NXP\_S32\_P5\_SYS\_CLK   57U |
| --- |

## [◆ ](#ad324b9f48cffa750d35a1b3625e41d78)NXP\_S32\_P5\_SYS\_DIV2\_CLK

| #define NXP\_S32\_P5\_SYS\_DIV2\_CLK   58U |
| --- |

## [◆ ](#afa536c5aa9044ad45772be1330568ef5)NXP\_S32\_P5\_SYS\_DIV4\_CLK

| #define NXP\_S32\_P5\_SYS\_DIV4\_CLK   59U |
| --- |

## [◆ ](#a75d9a7d4beda3a17dc0f07bd63fa368d)NXP\_S32\_P6\_REG\_INTF\_CLK

| #define NXP\_S32\_P6\_REG\_INTF\_CLK   236U |
| --- |

## [◆ ](#a64b593be74cbcacec88f6f4aa513e959)NXP\_S32\_PERIPHPLL\_CLK

| #define NXP\_S32\_PERIPHPLL\_CLK   5U |
| --- |

## [◆ ](#a6d1b5a86631e390202f9b02554815468)NXP\_S32\_PERIPHPLL\_DFS0\_CLK

| #define NXP\_S32\_PERIPHPLL\_DFS0\_CLK   23U |
| --- |

## [◆ ](#a2e3dc5289e03199416edfd3df835f183)NXP\_S32\_PERIPHPLL\_DFS1\_CLK

| #define NXP\_S32\_PERIPHPLL\_DFS1\_CLK   24U |
| --- |

## [◆ ](#a9a5e64bade06d1ee1202b61387d8a17c)NXP\_S32\_PERIPHPLL\_DFS2\_CLK

| #define NXP\_S32\_PERIPHPLL\_DFS2\_CLK   25U |
| --- |

## [◆ ](#ad282337933262b0c42430b35a33d7507)NXP\_S32\_PERIPHPLL\_DFS3\_CLK

| #define NXP\_S32\_PERIPHPLL\_DFS3\_CLK   26U |
| --- |

## [◆ ](#a594165bad79d57a3efce555cb9ac5bff)NXP\_S32\_PERIPHPLL\_DFS4\_CLK

| #define NXP\_S32\_PERIPHPLL\_DFS4\_CLK   27U |
| --- |

## [◆ ](#aba43a681b81004967aa5827c55b24a5d)NXP\_S32\_PERIPHPLL\_DFS5\_CLK

| #define NXP\_S32\_PERIPHPLL\_DFS5\_CLK   28U |
| --- |

## [◆ ](#aa786b49d448f96193ccf372ed28b8892)NXP\_S32\_PERIPHPLL\_PHI0\_CLK

| #define NXP\_S32\_PERIPHPLL\_PHI0\_CLK   16U |
| --- |

## [◆ ](#a7c956a57231bdbe242b41fbf837512d7)NXP\_S32\_PERIPHPLL\_PHI1\_CLK

| #define NXP\_S32\_PERIPHPLL\_PHI1\_CLK   17U |
| --- |

## [◆ ](#a5a42cf11ac2ba5bfb697be28b3f7868c)NXP\_S32\_PERIPHPLL\_PHI2\_CLK

| #define NXP\_S32\_PERIPHPLL\_PHI2\_CLK   18U |
| --- |

## [◆ ](#ae3ecaa42d02bbdefe504c62d3dc3d5b3)NXP\_S32\_PERIPHPLL\_PHI3\_CLK

| #define NXP\_S32\_PERIPHPLL\_PHI3\_CLK   19U |
| --- |

## [◆ ](#a2550e0d2500a0c7d6a9af4aee6d2c0fb)NXP\_S32\_PERIPHPLL\_PHI4\_CLK

| #define NXP\_S32\_PERIPHPLL\_PHI4\_CLK   20U |
| --- |

## [◆ ](#acf1ad3c3de2d0f3db3110907b3a7f5de)NXP\_S32\_PERIPHPLL\_PHI5\_CLK

| #define NXP\_S32\_PERIPHPLL\_PHI5\_CLK   21U |
| --- |

## [◆ ](#afcea8aabd3d25ae13be9e50fa8c84b12)NXP\_S32\_PERIPHPLL\_PHI6\_CLK

| #define NXP\_S32\_PERIPHPLL\_PHI6\_CLK   22U |
| --- |

## [◆ ](#a0352473aa201738f3c6476dee1551956)NXP\_S32\_PIT0\_CLK

| #define NXP\_S32\_PIT0\_CLK   237U |
| --- |

## [◆ ](#a8005e37da1d529a8340afe773fcb5291)NXP\_S32\_PIT1\_CLK

| #define NXP\_S32\_PIT1\_CLK   238U |
| --- |

## [◆ ](#a95d4be21a23722d68155ccb246971999)NXP\_S32\_PIT4\_CLK

| #define NXP\_S32\_PIT4\_CLK   239U |
| --- |

## [◆ ](#ae5252f32a9e3f0b0587bf0ac9c8e6ba4)NXP\_S32\_PIT5\_CLK

| #define NXP\_S32\_PIT5\_CLK   240U |
| --- |

## [◆ ](#a45288996c043d9c843d699fc32c63ed4)NXP\_S32\_PSI5\_0\_CLK

| #define NXP\_S32\_PSI5\_0\_CLK   242U |
| --- |

## [◆ ](#a50e530ccf9ee1ca47c1bb83662dc6099)NXP\_S32\_PSI5\_1\_CLK

| #define NXP\_S32\_PSI5\_1\_CLK   244U |
| --- |

## [◆ ](#a9a237fb6c9a8f8b54103a2df4cbf4035)NXP\_S32\_PSI5S\_0\_CLK

| #define NXP\_S32\_PSI5S\_0\_CLK   245U |
| --- |

## [◆ ](#a9dc67efa8d4c150c887cf0ffc1645776)NXP\_S32\_PSI5S\_1\_CLK

| #define NXP\_S32\_PSI5S\_1\_CLK   246U |
| --- |

## [◆ ](#a99dcc3421a01f3c684be71561e305421)NXP\_S32\_QSPI0\_CLK

| #define NXP\_S32\_QSPI0\_CLK   247U |
| --- |

## [◆ ](#a34b5af84c9e7acbebd49869f3b351899)NXP\_S32\_QSPI1\_CLK

| #define NXP\_S32\_QSPI1\_CLK   248U |
| --- |

## [◆ ](#a480e71b89b05bc9e36526d87a995d0df)NXP\_S32\_RTU0\_CORE\_CLK

| #define NXP\_S32\_RTU0\_CORE\_CLK   63U |
| --- |

## [◆ ](#a29df359bdd3589eedc4d973619789304)NXP\_S32\_RTU0\_CORE\_DIV2\_CLK

| #define NXP\_S32\_RTU0\_CORE\_DIV2\_CLK   64U |
| --- |

## [◆ ](#a3b5861829dcdae5c4ba9eca8bf07803d)NXP\_S32\_RTU0\_CORE\_DIV2\_MON1\_CLK

| #define NXP\_S32\_RTU0\_CORE\_DIV2\_MON1\_CLK   251U |
| --- |

## [◆ ](#a25056829910865ceb57868499dbf5b1c)NXP\_S32\_RTU0\_CORE\_DIV2\_MON2\_CLK

| #define NXP\_S32\_RTU0\_CORE\_DIV2\_MON2\_CLK   252U |
| --- |

## [◆ ](#aa007c8ba96e292d6b0ee9ac9124997d7)NXP\_S32\_RTU0\_CORE\_DIV2\_MON3\_CLK

| #define NXP\_S32\_RTU0\_CORE\_DIV2\_MON3\_CLK   253U |
| --- |

## [◆ ](#a9382cafe97d5ef2b77f0c56223523d03)NXP\_S32\_RTU0\_CORE\_MON1\_CLK

| #define NXP\_S32\_RTU0\_CORE\_MON1\_CLK   249U |
| --- |

## [◆ ](#a7d9bc68ad0596d370551738282b3aa47)NXP\_S32\_RTU0\_CORE\_MON2\_CLK

| #define NXP\_S32\_RTU0\_CORE\_MON2\_CLK   250U |
| --- |

## [◆ ](#a3aa44fc0bd3ebace5f0f5961614e9e6c)NXP\_S32\_RTU0\_REG\_INTF\_CLK

| #define NXP\_S32\_RTU0\_REG\_INTF\_CLK   254U |
| --- |

## [◆ ](#aa1497392847306b62614e7c3b653048f)NXP\_S32\_RTU1\_CORE\_CLK

| #define NXP\_S32\_RTU1\_CORE\_CLK   65U |
| --- |

## [◆ ](#adbce190d535e203b6a3d04369a316d4e)NXP\_S32\_RTU1\_CORE\_DIV2\_CLK

| #define NXP\_S32\_RTU1\_CORE\_DIV2\_CLK   66U |
| --- |

## [◆ ](#ad10ef71c5464e922717e0c753a7fe676)NXP\_S32\_RTU1\_CORE\_DIV2\_MON1\_CLK

| #define NXP\_S32\_RTU1\_CORE\_DIV2\_MON1\_CLK   257U |
| --- |

## [◆ ](#a52a42685006ebf3ed9f9c5c119ffa609)NXP\_S32\_RTU1\_CORE\_DIV2\_MON2\_CLK

| #define NXP\_S32\_RTU1\_CORE\_DIV2\_MON2\_CLK   258U |
| --- |

## [◆ ](#a2a60767a23cdab4da560040ef15e71fd)NXP\_S32\_RTU1\_CORE\_DIV2\_MON3\_CLK

| #define NXP\_S32\_RTU1\_CORE\_DIV2\_MON3\_CLK   259U |
| --- |

## [◆ ](#afea4fe7c9d2a5a9bf8f1a67069f2562c)NXP\_S32\_RTU1\_CORE\_MON1\_CLK

| #define NXP\_S32\_RTU1\_CORE\_MON1\_CLK   255U |
| --- |

## [◆ ](#a0a2defc0b7e131537b5b9290f79910f6)NXP\_S32\_RTU1\_CORE\_MON2\_CLK

| #define NXP\_S32\_RTU1\_CORE\_MON2\_CLK   256U |
| --- |

## [◆ ](#adec5a3a5f480d49b032f0a9de9d2e570)NXP\_S32\_RTU1\_REG\_INTF\_CLK

| #define NXP\_S32\_RTU1\_REG\_INTF\_CLK   260U |
| --- |

## [◆ ](#a2fa48a84b2413d6873ec5c08945117b1)NXP\_S32\_RXLUT\_CLK

| #define NXP\_S32\_RXLUT\_CLK   262U |
| --- |

## [◆ ](#adff8c8043444ba4e5f11e20141792a71)NXP\_S32\_SDHC0\_CLK

| #define NXP\_S32\_SDHC0\_CLK   263U |
| --- |

## [◆ ](#a76b134b000c9a4b009a9ddd7a530dcba)NXP\_S32\_SINC\_CLK

| #define NXP\_S32\_SINC\_CLK   264U |
| --- |

## [◆ ](#a4d8673a3b814bc9f14e15d50b57a7d2b)NXP\_S32\_SIPI0\_CLK

| #define NXP\_S32\_SIPI0\_CLK   265U |
| --- |

## [◆ ](#a60c30b39d2e89c80fa211b43342ca99f)NXP\_S32\_SIPI1\_CLK

| #define NXP\_S32\_SIPI1\_CLK   266U |
| --- |

## [◆ ](#adc1da7bf433a80a3a975e172a30abbbc)NXP\_S32\_SIRC\_CLK

| #define NXP\_S32\_SIRC\_CLK   3U |
| --- |

## [◆ ](#a89f492994987302439850a892121c9bc)NXP\_S32\_SIUL2\_0\_CLK

| #define NXP\_S32\_SIUL2\_0\_CLK   267U |
| --- |

## [◆ ](#a106bdd661bd1dfe6cad2159566a1d58b)NXP\_S32\_SIUL2\_1\_CLK

| #define NXP\_S32\_SIUL2\_1\_CLK   268U |
| --- |

## [◆ ](#a26724e2b1db403ef5358a59979a4817e)NXP\_S32\_SIUL2\_4\_CLK

| #define NXP\_S32\_SIUL2\_4\_CLK   269U |
| --- |

## [◆ ](#adc51aa185a667c281505c668ba927ada)NXP\_S32\_SIUL2\_5\_CLK

| #define NXP\_S32\_SIUL2\_5\_CLK   270U |
| --- |

## [◆ ](#a2c652648965f6c8e327ef712df2d5c98)NXP\_S32\_SPI0\_CLK

| #define NXP\_S32\_SPI0\_CLK   272U |
| --- |

## [◆ ](#acd656ebd78f6fe746576be80a5d24f05)NXP\_S32\_SPI1\_CLK

| #define NXP\_S32\_SPI1\_CLK   273U |
| --- |

## [◆ ](#aeb3dd4f8dc24715c3b229fd65ea9456f)NXP\_S32\_SPI2\_CLK

| #define NXP\_S32\_SPI2\_CLK   275U |
| --- |

## [◆ ](#a09fc0d6d2b75ab6e248e21b2542e273f)NXP\_S32\_SPI3\_CLK

| #define NXP\_S32\_SPI3\_CLK   276U |
| --- |

## [◆ ](#aefb565e2a703339f27aae4b7b26d467d)NXP\_S32\_SPI4\_CLK

| #define NXP\_S32\_SPI4\_CLK   277U |
| --- |

## [◆ ](#a5a28541a5df280d0d685098be4d78c83)NXP\_S32\_SPI5\_CLK

| #define NXP\_S32\_SPI5\_CLK   279U |
| --- |

## [◆ ](#a340ee2dfb7907910aa7bd846e78cf32c)NXP\_S32\_SPI6\_CLK

| #define NXP\_S32\_SPI6\_CLK   280U |
| --- |

## [◆ ](#a9a6f4147c148f3e1f429d10cf5747206)NXP\_S32\_SPI7\_CLK

| #define NXP\_S32\_SPI7\_CLK   281U |
| --- |

## [◆ ](#a6b7ab2e57f263ca785d2356c89d0f466)NXP\_S32\_SPI8\_CLK

| #define NXP\_S32\_SPI8\_CLK   283U |
| --- |

## [◆ ](#a150b128b301b737cc3cf00248d2ac9e3)NXP\_S32\_SPI9\_CLK

| #define NXP\_S32\_SPI9\_CLK   284U |
| --- |

## [◆ ](#af5454d5392cc7b9fa4bc2d846b2da80e)NXP\_S32\_SRX0\_CLK

| #define NXP\_S32\_SRX0\_CLK   285U |
| --- |

## [◆ ](#af014a5ddb774fe7c342e2ee3c3734487)NXP\_S32\_SRX1\_CLK

| #define NXP\_S32\_SRX1\_CLK   286U |
| --- |

## [◆ ](#a9540744a0ace0989f2c3cc968f3713af)NXP\_S32\_TMR\_1588\_CLK

| #define NXP\_S32\_TMR\_1588\_CLK   33U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [nxp\_s32z2\_clock.h](nxp__s32z2__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
