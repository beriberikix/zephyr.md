---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nxp__s32k344__clock_8h.html
original_path: doxygen/html/nxp__s32k344__clock_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_s32k344\_clock.h File Reference

[Go to the source code of this file.](nxp__s32k344__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NXP\_S32\_FIRC\_CLK](#a8f4673a159fb26c90ae29761784395e9)   1U |
| #define | [NXP\_S32\_FIRC\_STANDBY\_CLK](#adaf10ac3403cbc604411477959f968f7)   2U |
| #define | [NXP\_S32\_SIRC\_CLK](#adc1da7bf433a80a3a975e172a30abbbc)   3U |
| #define | [NXP\_S32\_SIRC\_STANDBY\_CLK](#a4d7d43fd0155026fa6e15624e3b2ec49)   4U |
| #define | [NXP\_S32\_FXOSC\_CLK](#ab748e7ec615dc5fe10cafc723cc289fe)   5U |
| #define | [NXP\_S32\_SXOSC\_CLK](#a93d90fef864ce343237f0698bc1637e4)   6U |
| #define | [NXP\_S32\_PLL\_CLK](#ad630b290fc45bb016fab33c63866c3f4)   7U |
| #define | [NXP\_S32\_PLL\_POSTDIV\_CLK](#a9776eee648f0ba77e662bc36e0f97395)   8U |
| #define | [NXP\_S32\_PLL\_PHI0\_CLK](#a7bac186b3f321194a8fbe568bcb42a01)   9U |
| #define | [NXP\_S32\_PLL\_PHI1\_CLK](#acba73923ac0927a9491e81fbe38806e2)   10U |
| #define | [NXP\_S32\_EMAC\_MII\_RX\_CLK](#a685f8303272306ff9b6525f975818621)   11U |
| #define | [NXP\_S32\_EMAC\_MII\_RMII\_TX\_CLK](#ae07fa6829614f632634b77db0bbed29d)   12U |
| #define | [NXP\_S32\_SCS\_CLK](#a8839149b54e955dd82ffcd7d3165672f)   13U |
| #define | [NXP\_S32\_CORE\_CLK](#a3addb6ad5d596e0b9739f34f00bc4ffc)   14U |
| #define | [NXP\_S32\_AIPS\_PLAT\_CLK](#a66e65995472438ff7c81a50411a69a1a)   15U |
| #define | [NXP\_S32\_AIPS\_SLOW\_CLK](#a087daa0b5c6e9ffb3c19eab447e7f640)   16U |
| #define | [NXP\_S32\_HSE\_CLK](#aed00182fc87a5dc5c2b5ede1ef42e70b)   17U |
| #define | [NXP\_S32\_DCM\_CLK](#a861f901e140d9a294b2eb16bcf215f73)   18U |
| #define | [NXP\_S32\_LBIST\_CLK](#a15a7cd222d732219e2ee316118ff4687)   19U |
| #define | [NXP\_S32\_QSPI\_MEM\_CLK](#a944dcec4426ee975d282486754cd63fb)   20U |
| #define | [NXP\_S32\_CLKOUT\_RUN\_CLK](#a4b24e8f3122d410d7f6ab4edbb3f0408)   21U |
| #define | [NXP\_S32\_ADC0\_CLK](#a89fe6bb1365a3895449da72ccd517223)   23U |
| #define | [NXP\_S32\_ADC1\_CLK](#ace9575b4ed012fe344884b0b1fa2ef58)   24U |
| #define | [NXP\_S32\_ADC2\_CLK](#a439427d875a21738d142787685f3102d)   25U |
| #define | [NXP\_S32\_BCTU0\_CLK](#a93297d4a6baae69c82ceb3c5dc6421d6)   26U |
| #define | [NXP\_S32\_CLKOUT\_STANDBY\_CLK](#a83be292b22509e1255e1fc07161ca0c6)   27U |
| #define | [NXP\_S32\_CMP0\_CLK](#a44f6895b60c611c68da8d9674af0d474)   28U |
| #define | [NXP\_S32\_CMP1\_CLK](#a6cf084d9263d934093becb8348b83cd9)   29U |
| #define | [NXP\_S32\_CMP2\_CLK](#ac2fac23465983168709fbe481a49728b)   30U |
| #define | [NXP\_S32\_CRC0\_CLK](#a236cf04ea860d48a382096caea32d2b1)   31U |
| #define | [NXP\_S32\_DCM0\_CLK](#a263fcc4db494692b432edd667ae14b58)   32U |
| #define | [NXP\_S32\_DMAMUX0\_CLK](#a97a3ff5238f4878784ee1bee4cfc7522)   33U |
| #define | [NXP\_S32\_DMAMUX1\_CLK](#a708913d2bb71ec975caad705a10b8421)   34U |
| #define | [NXP\_S32\_EDMA0\_CLK](#ae8b13f1f1803f214f7c7ba371679ee6f)   35U |
| #define | [NXP\_S32\_EDMA0\_TCD0\_CLK](#aa5ddb09ddd5067525ca580b8c4af5c36)   36U |
| #define | [NXP\_S32\_EDMA0\_TCD1\_CLK](#a7d24907ee4b061def55f9aa966adeeca)   37U |
| #define | [NXP\_S32\_EDMA0\_TCD2\_CLK](#a364079ab2d5d101d7ab9683ea0743568)   38U |
| #define | [NXP\_S32\_EDMA0\_TCD3\_CLK](#a345d2bc4db0dc7b1fcde0ec99ca73804)   39U |
| #define | [NXP\_S32\_EDMA0\_TCD4\_CLK](#a18bfc4a0f2141a579cb6860e58d4ae5a)   40U |
| #define | [NXP\_S32\_EDMA0\_TCD5\_CLK](#a09eaf35cc66d13dc07846b0dfa4700f5)   41U |
| #define | [NXP\_S32\_EDMA0\_TCD6\_CLK](#a2ff1d32586c02b3f2532c4259c070365)   42U |
| #define | [NXP\_S32\_EDMA0\_TCD7\_CLK](#a7da0580971ce98f3508afb7c13c6ff27)   43U |
| #define | [NXP\_S32\_EDMA0\_TCD8\_CLK](#a501fc394e4205f0469a82b7d91a118e3)   44U |
| #define | [NXP\_S32\_EDMA0\_TCD9\_CLK](#a970cf76b8d2002613e79239f7b914931)   45U |
| #define | [NXP\_S32\_EDMA0\_TCD10\_CLK](#ab0a57e5bb066e7a8703dfa74f71ed28f)   46U |
| #define | [NXP\_S32\_EDMA0\_TCD11\_CLK](#ab9d76bd6ef0a976bd637bef558ead505)   47U |
| #define | [NXP\_S32\_EDMA0\_TCD12\_CLK](#a83eac3871822e740be19b07cba0cfe88)   48U |
| #define | [NXP\_S32\_EDMA0\_TCD13\_CLK](#af67b7883216b5821efee3bd5dd83cc8e)   49U |
| #define | [NXP\_S32\_EDMA0\_TCD14\_CLK](#affb8b8d4898c93574b3e286ebb6a875d)   50U |
| #define | [NXP\_S32\_EDMA0\_TCD15\_CLK](#a8d1c96d3a35e0e8b3b01cdde4bea0bf4)   51U |
| #define | [NXP\_S32\_EDMA0\_TCD16\_CLK](#a179bafeddd54b29801ef5ea9f18dffd0)   52U |
| #define | [NXP\_S32\_EDMA0\_TCD17\_CLK](#a1a84b3f1413fb4850547f8016e173898)   53U |
| #define | [NXP\_S32\_EDMA0\_TCD18\_CLK](#a61d898070713033029178e1ad9434196)   54U |
| #define | [NXP\_S32\_EDMA0\_TCD19\_CLK](#a62e2b7d1584b456143bd4a9bb7a08b2f)   55U |
| #define | [NXP\_S32\_EDMA0\_TCD20\_CLK](#a08ed1758962b643d44bce3b7054d56f9)   56U |
| #define | [NXP\_S32\_EDMA0\_TCD21\_CLK](#ae35552f9675dff63a199b39cca13d97f)   57U |
| #define | [NXP\_S32\_EDMA0\_TCD22\_CLK](#a193891b8e165f2a005380e281d3cada6)   58U |
| #define | [NXP\_S32\_EDMA0\_TCD23\_CLK](#a5ea305b51c42cae9dc90ad96d68ecebd)   59U |
| #define | [NXP\_S32\_EDMA0\_TCD24\_CLK](#aafc4119cefe803821d14e0f246db143d)   60U |
| #define | [NXP\_S32\_EDMA0\_TCD25\_CLK](#a657ca4b3c6efd5892c60b5f3455b275d)   61U |
| #define | [NXP\_S32\_EDMA0\_TCD26\_CLK](#a79f4bff79205657e670e59e0aef52e28)   62U |
| #define | [NXP\_S32\_EDMA0\_TCD27\_CLK](#a801c12d831a651143705d3bf79c6db8e)   63U |
| #define | [NXP\_S32\_EDMA0\_TCD28\_CLK](#a17d3b0d7f197a02403dc67a5b56b5c33)   64U |
| #define | [NXP\_S32\_EDMA0\_TCD29\_CLK](#a064f390645ce062c028fbfe383299a10)   65U |
| #define | [NXP\_S32\_EDMA0\_TCD30\_CLK](#a48e3b322448916841208b11f89365c31)   66U |
| #define | [NXP\_S32\_EDMA0\_TCD31\_CLK](#a4e525a7e6ea34a5ab8b1f2d133fbe2e7)   67U |
| #define | [NXP\_S32\_EIM\_CLK](#ad2e33a9acd3a442b3036458795d1b0c5)   68U |
| #define | [NXP\_S32\_EMAC\_RX\_CLK](#adf84198aec5f5182883113beea3615f8)   69U |
| #define | [NXP\_S32\_EMAC0\_RX\_CLK](#aa59259703780d4cdff42589dbbcc49f3)   70U |
| #define | [NXP\_S32\_EMAC\_TS\_CLK](#a2990ad5b6cfcbb88e301c0e6e4ea438b)   71U |
| #define | [NXP\_S32\_EMAC0\_TS\_CLK](#a3bb76fd0f956c779da97ff36cbca3e98)   72U |
| #define | [NXP\_S32\_EMAC\_TX\_CLK](#ae07e1cc028d1280610e0cd4831332e96)   73U |
| #define | [NXP\_S32\_EMAC0\_TX\_CLK](#a10b3a801cfe769ff0ac0bdc2979b5e16)   74U |
| #define | [NXP\_S32\_EMIOS0\_CLK](#abc50bd8ecae9ffac02421389575302cc)   75U |
| #define | [NXP\_S32\_EMIOS1\_CLK](#a93ae95e32c998bfe99ad03c4b953261e)   76U |
| #define | [NXP\_S32\_EMIOS2\_CLK](#ab808fbaa6e6a14d622fff1aceac04319)   77U |
| #define | [NXP\_S32\_ERM0\_CLK](#a5330dac04dd7c5b914f65920731472fd)   78U |
| #define | [NXP\_S32\_FLEXCANA\_CLK](#accfc99304f1187d908296ac24eea41f1)   79U |
| #define | [NXP\_S32\_FLEXCAN0\_CLK](#a308e74a366725070c56a4ab4fc7c300a)   80U |
| #define | [NXP\_S32\_FLEXCAN1\_CLK](#ad353c07d914cfa8c45ed3b7b586c2b00)   81U |
| #define | [NXP\_S32\_FLEXCAN2\_CLK](#a54467688a58d9be77849eddd031f126e)   82U |
| #define | [NXP\_S32\_FLEXCANB\_CLK](#ab6f76cc8ee9a2d120dc048ae07b1ac31)   83U |
| #define | [NXP\_S32\_FLEXCAN3\_CLK](#a0fcf00296138cd26e845ab524054fd3b)   84U |
| #define | [NXP\_S32\_FLEXCAN4\_CLK](#a6106f0f8b5e0f5230b75e43b5ccdbf0e)   85U |
| #define | [NXP\_S32\_FLEXCAN5\_CLK](#a4f3b1864f3f5bcc6a1fd66e27eb12a52)   86U |
| #define | [NXP\_S32\_FLEXIO0\_CLK](#a3a15b5fc1e3242c0399c7dd46e46fdd4)   87U |
| #define | [NXP\_S32\_INTM\_CLK](#a5df33aea12ebef163135151c48c4e7cf)   88U |
| #define | [NXP\_S32\_LCU0\_CLK](#acafd9bf768c57ddb9747ee65ce27598a)   89U |
| #define | [NXP\_S32\_LCU1\_CLK](#ab799c3834e9756bdea0e749aa9d88abd)   90U |
| #define | [NXP\_S32\_LPI2C0\_CLK](#a381f2ad32adfa495e9020788f5211aee)   91U |
| #define | [NXP\_S32\_LPI2C1\_CLK](#a3f1f16418e5055f7907508ff4d46c522)   92U |
| #define | [NXP\_S32\_LPSPI0\_CLK](#a3c5548bea0bf573ee5c34064ccc5eb5f)   93U |
| #define | [NXP\_S32\_LPSPI1\_CLK](#a0d581a4df52c36546fe58e947d6b62ae)   94U |
| #define | [NXP\_S32\_LPSPI2\_CLK](#a8ae234050a66b6857bf34769d485c7e4)   95U |
| #define | [NXP\_S32\_LPSPI3\_CLK](#a5b9440566cba4efa7904a00384310a2b)   96U |
| #define | [NXP\_S32\_LPSPI4\_CLK](#a46b7dfdff4ca08036ecc76031d987d2e)   97U |
| #define | [NXP\_S32\_LPSPI5\_CLK](#a968b718186547fc88bc290939792decf)   98U |
| #define | [NXP\_S32\_LPUART0\_CLK](#a49beda273937c66398354636595e7d1c)   99U |
| #define | [NXP\_S32\_LPUART1\_CLK](#af5ca4a56001a2e39ed143adbd15d2219)   100U |
| #define | [NXP\_S32\_LPUART2\_CLK](#ad9303a366af8d2e1b160bf82adc894fe)   101U |
| #define | [NXP\_S32\_LPUART3\_CLK](#a696e0636cc8a6c3b6c7158f2fe221a80)   102U |
| #define | [NXP\_S32\_LPUART4\_CLK](#a55d4b1d4733bf6405b30e0bfdeb84a19)   103U |
| #define | [NXP\_S32\_LPUART5\_CLK](#a8986cf7bbabcfd33be679321ce7e6fa9)   104U |
| #define | [NXP\_S32\_LPUART6\_CLK](#a294d79027be7372f1b6b1f4afce99d91)   105U |
| #define | [NXP\_S32\_LPUART7\_CLK](#a01038ad550a11f12779d666364336e8d)   106U |
| #define | [NXP\_S32\_LPUART8\_CLK](#a327cb53647a534e3361ae7b208dde92e)   107U |
| #define | [NXP\_S32\_LPUART9\_CLK](#afd38741c6071e8489c579e80b9c17479)   108U |
| #define | [NXP\_S32\_LPUART10\_CLK](#aa8d39f79fc0afc065acdc78c29cd668c)   109U |
| #define | [NXP\_S32\_LPUART11\_CLK](#a4c398ddca86d95484584ef878beafa2b)   110U |
| #define | [NXP\_S32\_LPUART12\_CLK](#a3808a48039cbc4eb2b656df9ec4f8bfc)   111U |
| #define | [NXP\_S32\_LPUART13\_CLK](#ac9bbead64f9bf1df293da5f2e96c650d)   112U |
| #define | [NXP\_S32\_LPUART14\_CLK](#a32b9022da94a1891b83588c16c6c5373)   113U |
| #define | [NXP\_S32\_LPUART15\_CLK](#a3474c5a33569dc233c54e41990a8daf8)   114U |
| #define | [NXP\_S32\_MSCM\_CLK](#a045348716b7d0c9f7c286226786a1587)   115U |
| #define | [NXP\_S32\_MU2A\_CLK](#a122abc9d70dcb3c4b4bc0082d874db43)   116U |
| #define | [NXP\_S32\_MU2B\_CLK](#a0c88a60820dbafe53eaf2badf443cd3c)   117U |
| #define | [NXP\_S32\_PIT0\_CLK](#a0352473aa201738f3c6476dee1551956)   118U |
| #define | [NXP\_S32\_PIT1\_CLK](#a8005e37da1d529a8340afe773fcb5291)   119U |
| #define | [NXP\_S32\_PIT2\_CLK](#a7a25f5a452598e9ec637f2b09c61f96b)   120U |
| #define | [NXP\_S32\_QSPI0\_CLK](#a99dcc3421a01f3c684be71561e305421)   121U |
| #define | [NXP\_S32\_QSPI0\_RAM\_CLK](#a2c02e14aa6e2f26676a9cbf3b9252764)   122U |
| #define | [NXP\_S32\_QSPI0\_TX\_MEM\_CLK](#ad69581caba8b97eab4fddf3a28a15dc9)   123U |
| #define | [NXP\_S32\_QSPI\_SFCK\_CLK](#a74842614cadb4868a08a71932a6eb60a)   124U |
| #define | [NXP\_S32\_RTC\_CLK](#a1ca20b16f6a430cddd8fc1d55fd7a840)   125U |
| #define | [NXP\_S32\_RTC0\_CLK](#ae883db6b1e83c7e5f43004c38a496b58)   126U |
| #define | [NXP\_S32\_SAI0\_CLK](#a816aa8f3387ee596c7f7409d1f546dec)   127U |
| #define | [NXP\_S32\_SAI1\_CLK](#a45d6b8b3a35d8a03a8f9a24dfda6acb6)   128U |
| #define | [NXP\_S32\_SEMA42\_CLK](#a11238766b6cf870c9fe7e27565a963e8)   129U |
| #define | [NXP\_S32\_SIUL2\_CLK](#a2814540c94848acfbb49b2c8b9be4ad2)   130U |
| #define | [NXP\_S32\_STCU0\_CLK](#a1589ff94052ec884cd173d896c2d2d3d)   131U |
| #define | [NXP\_S32\_STMA\_CLK](#a951b5215866501d57a1231bdcbf6c937)   132U |
| #define | [NXP\_S32\_STM0\_CLK](#ac3cc906db4f46606943573ad6582bcaf)   133U |
| #define | [NXP\_S32\_STMB\_CLK](#a41ac38f92beac668afbcb88f049f6d83)   134U |
| #define | [NXP\_S32\_STM1\_CLK](#a605907a7a763a74e6b6c5b6f374f7469)   135U |
| #define | [NXP\_S32\_SWT0\_CLK](#a21446770924672e8f9efb8becaf378fb)   136U |
| #define | [NXP\_S32\_TEMPSENSE\_CLK](#aeaf92d23687006556891f773b814340a)   137U |
| #define | [NXP\_S32\_TRACE\_CLK](#a6a6963b78096148b569b9e07cf82faaf)   138U |
| #define | [NXP\_S32\_TRGMUX0\_CLK](#a3ea3b033b0b8662cf3320ee7cfd99581)   139U |
| #define | [NXP\_S32\_TSENSE0\_CLK](#a8178328a4fb78be2204f7543eb786347)   140U |
| #define | [NXP\_S32\_WKPU0\_CLK](#a2bbf381a7dc2b42c9867ab1336efc4bd)   141U |

## Macro Definition Documentation

## [◆ ](#a89fe6bb1365a3895449da72ccd517223)NXP\_S32\_ADC0\_CLK

| #define NXP\_S32\_ADC0\_CLK   23U |
| --- |

## [◆ ](#ace9575b4ed012fe344884b0b1fa2ef58)NXP\_S32\_ADC1\_CLK

| #define NXP\_S32\_ADC1\_CLK   24U |
| --- |

## [◆ ](#a439427d875a21738d142787685f3102d)NXP\_S32\_ADC2\_CLK

| #define NXP\_S32\_ADC2\_CLK   25U |
| --- |

## [◆ ](#a66e65995472438ff7c81a50411a69a1a)NXP\_S32\_AIPS\_PLAT\_CLK

| #define NXP\_S32\_AIPS\_PLAT\_CLK   15U |
| --- |

## [◆ ](#a087daa0b5c6e9ffb3c19eab447e7f640)NXP\_S32\_AIPS\_SLOW\_CLK

| #define NXP\_S32\_AIPS\_SLOW\_CLK   16U |
| --- |

## [◆ ](#a93297d4a6baae69c82ceb3c5dc6421d6)NXP\_S32\_BCTU0\_CLK

| #define NXP\_S32\_BCTU0\_CLK   26U |
| --- |

## [◆ ](#a4b24e8f3122d410d7f6ab4edbb3f0408)NXP\_S32\_CLKOUT\_RUN\_CLK

| #define NXP\_S32\_CLKOUT\_RUN\_CLK   21U |
| --- |

## [◆ ](#a83be292b22509e1255e1fc07161ca0c6)NXP\_S32\_CLKOUT\_STANDBY\_CLK

| #define NXP\_S32\_CLKOUT\_STANDBY\_CLK   27U |
| --- |

## [◆ ](#a44f6895b60c611c68da8d9674af0d474)NXP\_S32\_CMP0\_CLK

| #define NXP\_S32\_CMP0\_CLK   28U |
| --- |

## [◆ ](#a6cf084d9263d934093becb8348b83cd9)NXP\_S32\_CMP1\_CLK

| #define NXP\_S32\_CMP1\_CLK   29U |
| --- |

## [◆ ](#ac2fac23465983168709fbe481a49728b)NXP\_S32\_CMP2\_CLK

| #define NXP\_S32\_CMP2\_CLK   30U |
| --- |

## [◆ ](#a3addb6ad5d596e0b9739f34f00bc4ffc)NXP\_S32\_CORE\_CLK

| #define NXP\_S32\_CORE\_CLK   14U |
| --- |

## [◆ ](#a236cf04ea860d48a382096caea32d2b1)NXP\_S32\_CRC0\_CLK

| #define NXP\_S32\_CRC0\_CLK   31U |
| --- |

## [◆ ](#a263fcc4db494692b432edd667ae14b58)NXP\_S32\_DCM0\_CLK

| #define NXP\_S32\_DCM0\_CLK   32U |
| --- |

## [◆ ](#a861f901e140d9a294b2eb16bcf215f73)NXP\_S32\_DCM\_CLK

| #define NXP\_S32\_DCM\_CLK   18U |
| --- |

## [◆ ](#a97a3ff5238f4878784ee1bee4cfc7522)NXP\_S32\_DMAMUX0\_CLK

| #define NXP\_S32\_DMAMUX0\_CLK   33U |
| --- |

## [◆ ](#a708913d2bb71ec975caad705a10b8421)NXP\_S32\_DMAMUX1\_CLK

| #define NXP\_S32\_DMAMUX1\_CLK   34U |
| --- |

## [◆ ](#ae8b13f1f1803f214f7c7ba371679ee6f)NXP\_S32\_EDMA0\_CLK

| #define NXP\_S32\_EDMA0\_CLK   35U |
| --- |

## [◆ ](#aa5ddb09ddd5067525ca580b8c4af5c36)NXP\_S32\_EDMA0\_TCD0\_CLK

| #define NXP\_S32\_EDMA0\_TCD0\_CLK   36U |
| --- |

## [◆ ](#ab0a57e5bb066e7a8703dfa74f71ed28f)NXP\_S32\_EDMA0\_TCD10\_CLK

| #define NXP\_S32\_EDMA0\_TCD10\_CLK   46U |
| --- |

## [◆ ](#ab9d76bd6ef0a976bd637bef558ead505)NXP\_S32\_EDMA0\_TCD11\_CLK

| #define NXP\_S32\_EDMA0\_TCD11\_CLK   47U |
| --- |

## [◆ ](#a83eac3871822e740be19b07cba0cfe88)NXP\_S32\_EDMA0\_TCD12\_CLK

| #define NXP\_S32\_EDMA0\_TCD12\_CLK   48U |
| --- |

## [◆ ](#af67b7883216b5821efee3bd5dd83cc8e)NXP\_S32\_EDMA0\_TCD13\_CLK

| #define NXP\_S32\_EDMA0\_TCD13\_CLK   49U |
| --- |

## [◆ ](#affb8b8d4898c93574b3e286ebb6a875d)NXP\_S32\_EDMA0\_TCD14\_CLK

| #define NXP\_S32\_EDMA0\_TCD14\_CLK   50U |
| --- |

## [◆ ](#a8d1c96d3a35e0e8b3b01cdde4bea0bf4)NXP\_S32\_EDMA0\_TCD15\_CLK

| #define NXP\_S32\_EDMA0\_TCD15\_CLK   51U |
| --- |

## [◆ ](#a179bafeddd54b29801ef5ea9f18dffd0)NXP\_S32\_EDMA0\_TCD16\_CLK

| #define NXP\_S32\_EDMA0\_TCD16\_CLK   52U |
| --- |

## [◆ ](#a1a84b3f1413fb4850547f8016e173898)NXP\_S32\_EDMA0\_TCD17\_CLK

| #define NXP\_S32\_EDMA0\_TCD17\_CLK   53U |
| --- |

## [◆ ](#a61d898070713033029178e1ad9434196)NXP\_S32\_EDMA0\_TCD18\_CLK

| #define NXP\_S32\_EDMA0\_TCD18\_CLK   54U |
| --- |

## [◆ ](#a62e2b7d1584b456143bd4a9bb7a08b2f)NXP\_S32\_EDMA0\_TCD19\_CLK

| #define NXP\_S32\_EDMA0\_TCD19\_CLK   55U |
| --- |

## [◆ ](#a7d24907ee4b061def55f9aa966adeeca)NXP\_S32\_EDMA0\_TCD1\_CLK

| #define NXP\_S32\_EDMA0\_TCD1\_CLK   37U |
| --- |

## [◆ ](#a08ed1758962b643d44bce3b7054d56f9)NXP\_S32\_EDMA0\_TCD20\_CLK

| #define NXP\_S32\_EDMA0\_TCD20\_CLK   56U |
| --- |

## [◆ ](#ae35552f9675dff63a199b39cca13d97f)NXP\_S32\_EDMA0\_TCD21\_CLK

| #define NXP\_S32\_EDMA0\_TCD21\_CLK   57U |
| --- |

## [◆ ](#a193891b8e165f2a005380e281d3cada6)NXP\_S32\_EDMA0\_TCD22\_CLK

| #define NXP\_S32\_EDMA0\_TCD22\_CLK   58U |
| --- |

## [◆ ](#a5ea305b51c42cae9dc90ad96d68ecebd)NXP\_S32\_EDMA0\_TCD23\_CLK

| #define NXP\_S32\_EDMA0\_TCD23\_CLK   59U |
| --- |

## [◆ ](#aafc4119cefe803821d14e0f246db143d)NXP\_S32\_EDMA0\_TCD24\_CLK

| #define NXP\_S32\_EDMA0\_TCD24\_CLK   60U |
| --- |

## [◆ ](#a657ca4b3c6efd5892c60b5f3455b275d)NXP\_S32\_EDMA0\_TCD25\_CLK

| #define NXP\_S32\_EDMA0\_TCD25\_CLK   61U |
| --- |

## [◆ ](#a79f4bff79205657e670e59e0aef52e28)NXP\_S32\_EDMA0\_TCD26\_CLK

| #define NXP\_S32\_EDMA0\_TCD26\_CLK   62U |
| --- |

## [◆ ](#a801c12d831a651143705d3bf79c6db8e)NXP\_S32\_EDMA0\_TCD27\_CLK

| #define NXP\_S32\_EDMA0\_TCD27\_CLK   63U |
| --- |

## [◆ ](#a17d3b0d7f197a02403dc67a5b56b5c33)NXP\_S32\_EDMA0\_TCD28\_CLK

| #define NXP\_S32\_EDMA0\_TCD28\_CLK   64U |
| --- |

## [◆ ](#a064f390645ce062c028fbfe383299a10)NXP\_S32\_EDMA0\_TCD29\_CLK

| #define NXP\_S32\_EDMA0\_TCD29\_CLK   65U |
| --- |

## [◆ ](#a364079ab2d5d101d7ab9683ea0743568)NXP\_S32\_EDMA0\_TCD2\_CLK

| #define NXP\_S32\_EDMA0\_TCD2\_CLK   38U |
| --- |

## [◆ ](#a48e3b322448916841208b11f89365c31)NXP\_S32\_EDMA0\_TCD30\_CLK

| #define NXP\_S32\_EDMA0\_TCD30\_CLK   66U |
| --- |

## [◆ ](#a4e525a7e6ea34a5ab8b1f2d133fbe2e7)NXP\_S32\_EDMA0\_TCD31\_CLK

| #define NXP\_S32\_EDMA0\_TCD31\_CLK   67U |
| --- |

## [◆ ](#a345d2bc4db0dc7b1fcde0ec99ca73804)NXP\_S32\_EDMA0\_TCD3\_CLK

| #define NXP\_S32\_EDMA0\_TCD3\_CLK   39U |
| --- |

## [◆ ](#a18bfc4a0f2141a579cb6860e58d4ae5a)NXP\_S32\_EDMA0\_TCD4\_CLK

| #define NXP\_S32\_EDMA0\_TCD4\_CLK   40U |
| --- |

## [◆ ](#a09eaf35cc66d13dc07846b0dfa4700f5)NXP\_S32\_EDMA0\_TCD5\_CLK

| #define NXP\_S32\_EDMA0\_TCD5\_CLK   41U |
| --- |

## [◆ ](#a2ff1d32586c02b3f2532c4259c070365)NXP\_S32\_EDMA0\_TCD6\_CLK

| #define NXP\_S32\_EDMA0\_TCD6\_CLK   42U |
| --- |

## [◆ ](#a7da0580971ce98f3508afb7c13c6ff27)NXP\_S32\_EDMA0\_TCD7\_CLK

| #define NXP\_S32\_EDMA0\_TCD7\_CLK   43U |
| --- |

## [◆ ](#a501fc394e4205f0469a82b7d91a118e3)NXP\_S32\_EDMA0\_TCD8\_CLK

| #define NXP\_S32\_EDMA0\_TCD8\_CLK   44U |
| --- |

## [◆ ](#a970cf76b8d2002613e79239f7b914931)NXP\_S32\_EDMA0\_TCD9\_CLK

| #define NXP\_S32\_EDMA0\_TCD9\_CLK   45U |
| --- |

## [◆ ](#ad2e33a9acd3a442b3036458795d1b0c5)NXP\_S32\_EIM\_CLK

| #define NXP\_S32\_EIM\_CLK   68U |
| --- |

## [◆ ](#aa59259703780d4cdff42589dbbcc49f3)NXP\_S32\_EMAC0\_RX\_CLK

| #define NXP\_S32\_EMAC0\_RX\_CLK   70U |
| --- |

## [◆ ](#a3bb76fd0f956c779da97ff36cbca3e98)NXP\_S32\_EMAC0\_TS\_CLK

| #define NXP\_S32\_EMAC0\_TS\_CLK   72U |
| --- |

## [◆ ](#a10b3a801cfe769ff0ac0bdc2979b5e16)NXP\_S32\_EMAC0\_TX\_CLK

| #define NXP\_S32\_EMAC0\_TX\_CLK   74U |
| --- |

## [◆ ](#ae07fa6829614f632634b77db0bbed29d)NXP\_S32\_EMAC\_MII\_RMII\_TX\_CLK

| #define NXP\_S32\_EMAC\_MII\_RMII\_TX\_CLK   12U |
| --- |

## [◆ ](#a685f8303272306ff9b6525f975818621)NXP\_S32\_EMAC\_MII\_RX\_CLK

| #define NXP\_S32\_EMAC\_MII\_RX\_CLK   11U |
| --- |

## [◆ ](#adf84198aec5f5182883113beea3615f8)NXP\_S32\_EMAC\_RX\_CLK

| #define NXP\_S32\_EMAC\_RX\_CLK   69U |
| --- |

## [◆ ](#a2990ad5b6cfcbb88e301c0e6e4ea438b)NXP\_S32\_EMAC\_TS\_CLK

| #define NXP\_S32\_EMAC\_TS\_CLK   71U |
| --- |

## [◆ ](#ae07e1cc028d1280610e0cd4831332e96)NXP\_S32\_EMAC\_TX\_CLK

| #define NXP\_S32\_EMAC\_TX\_CLK   73U |
| --- |

## [◆ ](#abc50bd8ecae9ffac02421389575302cc)NXP\_S32\_EMIOS0\_CLK

| #define NXP\_S32\_EMIOS0\_CLK   75U |
| --- |

## [◆ ](#a93ae95e32c998bfe99ad03c4b953261e)NXP\_S32\_EMIOS1\_CLK

| #define NXP\_S32\_EMIOS1\_CLK   76U |
| --- |

## [◆ ](#ab808fbaa6e6a14d622fff1aceac04319)NXP\_S32\_EMIOS2\_CLK

| #define NXP\_S32\_EMIOS2\_CLK   77U |
| --- |

## [◆ ](#a5330dac04dd7c5b914f65920731472fd)NXP\_S32\_ERM0\_CLK

| #define NXP\_S32\_ERM0\_CLK   78U |
| --- |

## [◆ ](#a8f4673a159fb26c90ae29761784395e9)NXP\_S32\_FIRC\_CLK

| #define NXP\_S32\_FIRC\_CLK   1U |
| --- |

## [◆ ](#adaf10ac3403cbc604411477959f968f7)NXP\_S32\_FIRC\_STANDBY\_CLK

| #define NXP\_S32\_FIRC\_STANDBY\_CLK   2U |
| --- |

## [◆ ](#a308e74a366725070c56a4ab4fc7c300a)NXP\_S32\_FLEXCAN0\_CLK

| #define NXP\_S32\_FLEXCAN0\_CLK   80U |
| --- |

## [◆ ](#ad353c07d914cfa8c45ed3b7b586c2b00)NXP\_S32\_FLEXCAN1\_CLK

| #define NXP\_S32\_FLEXCAN1\_CLK   81U |
| --- |

## [◆ ](#a54467688a58d9be77849eddd031f126e)NXP\_S32\_FLEXCAN2\_CLK

| #define NXP\_S32\_FLEXCAN2\_CLK   82U |
| --- |

## [◆ ](#a0fcf00296138cd26e845ab524054fd3b)NXP\_S32\_FLEXCAN3\_CLK

| #define NXP\_S32\_FLEXCAN3\_CLK   84U |
| --- |

## [◆ ](#a6106f0f8b5e0f5230b75e43b5ccdbf0e)NXP\_S32\_FLEXCAN4\_CLK

| #define NXP\_S32\_FLEXCAN4\_CLK   85U |
| --- |

## [◆ ](#a4f3b1864f3f5bcc6a1fd66e27eb12a52)NXP\_S32\_FLEXCAN5\_CLK

| #define NXP\_S32\_FLEXCAN5\_CLK   86U |
| --- |

## [◆ ](#accfc99304f1187d908296ac24eea41f1)NXP\_S32\_FLEXCANA\_CLK

| #define NXP\_S32\_FLEXCANA\_CLK   79U |
| --- |

## [◆ ](#ab6f76cc8ee9a2d120dc048ae07b1ac31)NXP\_S32\_FLEXCANB\_CLK

| #define NXP\_S32\_FLEXCANB\_CLK   83U |
| --- |

## [◆ ](#a3a15b5fc1e3242c0399c7dd46e46fdd4)NXP\_S32\_FLEXIO0\_CLK

| #define NXP\_S32\_FLEXIO0\_CLK   87U |
| --- |

## [◆ ](#ab748e7ec615dc5fe10cafc723cc289fe)NXP\_S32\_FXOSC\_CLK

| #define NXP\_S32\_FXOSC\_CLK   5U |
| --- |

## [◆ ](#aed00182fc87a5dc5c2b5ede1ef42e70b)NXP\_S32\_HSE\_CLK

| #define NXP\_S32\_HSE\_CLK   17U |
| --- |

## [◆ ](#a5df33aea12ebef163135151c48c4e7cf)NXP\_S32\_INTM\_CLK

| #define NXP\_S32\_INTM\_CLK   88U |
| --- |

## [◆ ](#a15a7cd222d732219e2ee316118ff4687)NXP\_S32\_LBIST\_CLK

| #define NXP\_S32\_LBIST\_CLK   19U |
| --- |

## [◆ ](#acafd9bf768c57ddb9747ee65ce27598a)NXP\_S32\_LCU0\_CLK

| #define NXP\_S32\_LCU0\_CLK   89U |
| --- |

## [◆ ](#ab799c3834e9756bdea0e749aa9d88abd)NXP\_S32\_LCU1\_CLK

| #define NXP\_S32\_LCU1\_CLK   90U |
| --- |

## [◆ ](#a381f2ad32adfa495e9020788f5211aee)NXP\_S32\_LPI2C0\_CLK

| #define NXP\_S32\_LPI2C0\_CLK   91U |
| --- |

## [◆ ](#a3f1f16418e5055f7907508ff4d46c522)NXP\_S32\_LPI2C1\_CLK

| #define NXP\_S32\_LPI2C1\_CLK   92U |
| --- |

## [◆ ](#a3c5548bea0bf573ee5c34064ccc5eb5f)NXP\_S32\_LPSPI0\_CLK

| #define NXP\_S32\_LPSPI0\_CLK   93U |
| --- |

## [◆ ](#a0d581a4df52c36546fe58e947d6b62ae)NXP\_S32\_LPSPI1\_CLK

| #define NXP\_S32\_LPSPI1\_CLK   94U |
| --- |

## [◆ ](#a8ae234050a66b6857bf34769d485c7e4)NXP\_S32\_LPSPI2\_CLK

| #define NXP\_S32\_LPSPI2\_CLK   95U |
| --- |

## [◆ ](#a5b9440566cba4efa7904a00384310a2b)NXP\_S32\_LPSPI3\_CLK

| #define NXP\_S32\_LPSPI3\_CLK   96U |
| --- |

## [◆ ](#a46b7dfdff4ca08036ecc76031d987d2e)NXP\_S32\_LPSPI4\_CLK

| #define NXP\_S32\_LPSPI4\_CLK   97U |
| --- |

## [◆ ](#a968b718186547fc88bc290939792decf)NXP\_S32\_LPSPI5\_CLK

| #define NXP\_S32\_LPSPI5\_CLK   98U |
| --- |

## [◆ ](#a49beda273937c66398354636595e7d1c)NXP\_S32\_LPUART0\_CLK

| #define NXP\_S32\_LPUART0\_CLK   99U |
| --- |

## [◆ ](#aa8d39f79fc0afc065acdc78c29cd668c)NXP\_S32\_LPUART10\_CLK

| #define NXP\_S32\_LPUART10\_CLK   109U |
| --- |

## [◆ ](#a4c398ddca86d95484584ef878beafa2b)NXP\_S32\_LPUART11\_CLK

| #define NXP\_S32\_LPUART11\_CLK   110U |
| --- |

## [◆ ](#a3808a48039cbc4eb2b656df9ec4f8bfc)NXP\_S32\_LPUART12\_CLK

| #define NXP\_S32\_LPUART12\_CLK   111U |
| --- |

## [◆ ](#ac9bbead64f9bf1df293da5f2e96c650d)NXP\_S32\_LPUART13\_CLK

| #define NXP\_S32\_LPUART13\_CLK   112U |
| --- |

## [◆ ](#a32b9022da94a1891b83588c16c6c5373)NXP\_S32\_LPUART14\_CLK

| #define NXP\_S32\_LPUART14\_CLK   113U |
| --- |

## [◆ ](#a3474c5a33569dc233c54e41990a8daf8)NXP\_S32\_LPUART15\_CLK

| #define NXP\_S32\_LPUART15\_CLK   114U |
| --- |

## [◆ ](#af5ca4a56001a2e39ed143adbd15d2219)NXP\_S32\_LPUART1\_CLK

| #define NXP\_S32\_LPUART1\_CLK   100U |
| --- |

## [◆ ](#ad9303a366af8d2e1b160bf82adc894fe)NXP\_S32\_LPUART2\_CLK

| #define NXP\_S32\_LPUART2\_CLK   101U |
| --- |

## [◆ ](#a696e0636cc8a6c3b6c7158f2fe221a80)NXP\_S32\_LPUART3\_CLK

| #define NXP\_S32\_LPUART3\_CLK   102U |
| --- |

## [◆ ](#a55d4b1d4733bf6405b30e0bfdeb84a19)NXP\_S32\_LPUART4\_CLK

| #define NXP\_S32\_LPUART4\_CLK   103U |
| --- |

## [◆ ](#a8986cf7bbabcfd33be679321ce7e6fa9)NXP\_S32\_LPUART5\_CLK

| #define NXP\_S32\_LPUART5\_CLK   104U |
| --- |

## [◆ ](#a294d79027be7372f1b6b1f4afce99d91)NXP\_S32\_LPUART6\_CLK

| #define NXP\_S32\_LPUART6\_CLK   105U |
| --- |

## [◆ ](#a01038ad550a11f12779d666364336e8d)NXP\_S32\_LPUART7\_CLK

| #define NXP\_S32\_LPUART7\_CLK   106U |
| --- |

## [◆ ](#a327cb53647a534e3361ae7b208dde92e)NXP\_S32\_LPUART8\_CLK

| #define NXP\_S32\_LPUART8\_CLK   107U |
| --- |

## [◆ ](#afd38741c6071e8489c579e80b9c17479)NXP\_S32\_LPUART9\_CLK

| #define NXP\_S32\_LPUART9\_CLK   108U |
| --- |

## [◆ ](#a045348716b7d0c9f7c286226786a1587)NXP\_S32\_MSCM\_CLK

| #define NXP\_S32\_MSCM\_CLK   115U |
| --- |

## [◆ ](#a122abc9d70dcb3c4b4bc0082d874db43)NXP\_S32\_MU2A\_CLK

| #define NXP\_S32\_MU2A\_CLK   116U |
| --- |

## [◆ ](#a0c88a60820dbafe53eaf2badf443cd3c)NXP\_S32\_MU2B\_CLK

| #define NXP\_S32\_MU2B\_CLK   117U |
| --- |

## [◆ ](#a0352473aa201738f3c6476dee1551956)NXP\_S32\_PIT0\_CLK

| #define NXP\_S32\_PIT0\_CLK   118U |
| --- |

## [◆ ](#a8005e37da1d529a8340afe773fcb5291)NXP\_S32\_PIT1\_CLK

| #define NXP\_S32\_PIT1\_CLK   119U |
| --- |

## [◆ ](#a7a25f5a452598e9ec637f2b09c61f96b)NXP\_S32\_PIT2\_CLK

| #define NXP\_S32\_PIT2\_CLK   120U |
| --- |

## [◆ ](#ad630b290fc45bb016fab33c63866c3f4)NXP\_S32\_PLL\_CLK

| #define NXP\_S32\_PLL\_CLK   7U |
| --- |

## [◆ ](#a7bac186b3f321194a8fbe568bcb42a01)NXP\_S32\_PLL\_PHI0\_CLK

| #define NXP\_S32\_PLL\_PHI0\_CLK   9U |
| --- |

## [◆ ](#acba73923ac0927a9491e81fbe38806e2)NXP\_S32\_PLL\_PHI1\_CLK

| #define NXP\_S32\_PLL\_PHI1\_CLK   10U |
| --- |

## [◆ ](#a9776eee648f0ba77e662bc36e0f97395)NXP\_S32\_PLL\_POSTDIV\_CLK

| #define NXP\_S32\_PLL\_POSTDIV\_CLK   8U |
| --- |

## [◆ ](#a99dcc3421a01f3c684be71561e305421)NXP\_S32\_QSPI0\_CLK

| #define NXP\_S32\_QSPI0\_CLK   121U |
| --- |

## [◆ ](#a2c02e14aa6e2f26676a9cbf3b9252764)NXP\_S32\_QSPI0\_RAM\_CLK

| #define NXP\_S32\_QSPI0\_RAM\_CLK   122U |
| --- |

## [◆ ](#ad69581caba8b97eab4fddf3a28a15dc9)NXP\_S32\_QSPI0\_TX\_MEM\_CLK

| #define NXP\_S32\_QSPI0\_TX\_MEM\_CLK   123U |
| --- |

## [◆ ](#a944dcec4426ee975d282486754cd63fb)NXP\_S32\_QSPI\_MEM\_CLK

| #define NXP\_S32\_QSPI\_MEM\_CLK   20U |
| --- |

## [◆ ](#a74842614cadb4868a08a71932a6eb60a)NXP\_S32\_QSPI\_SFCK\_CLK

| #define NXP\_S32\_QSPI\_SFCK\_CLK   124U |
| --- |

## [◆ ](#ae883db6b1e83c7e5f43004c38a496b58)NXP\_S32\_RTC0\_CLK

| #define NXP\_S32\_RTC0\_CLK   126U |
| --- |

## [◆ ](#a1ca20b16f6a430cddd8fc1d55fd7a840)NXP\_S32\_RTC\_CLK

| #define NXP\_S32\_RTC\_CLK   125U |
| --- |

## [◆ ](#a816aa8f3387ee596c7f7409d1f546dec)NXP\_S32\_SAI0\_CLK

| #define NXP\_S32\_SAI0\_CLK   127U |
| --- |

## [◆ ](#a45d6b8b3a35d8a03a8f9a24dfda6acb6)NXP\_S32\_SAI1\_CLK

| #define NXP\_S32\_SAI1\_CLK   128U |
| --- |

## [◆ ](#a8839149b54e955dd82ffcd7d3165672f)NXP\_S32\_SCS\_CLK

| #define NXP\_S32\_SCS\_CLK   13U |
| --- |

## [◆ ](#a11238766b6cf870c9fe7e27565a963e8)NXP\_S32\_SEMA42\_CLK

| #define NXP\_S32\_SEMA42\_CLK   129U |
| --- |

## [◆ ](#adc1da7bf433a80a3a975e172a30abbbc)NXP\_S32\_SIRC\_CLK

| #define NXP\_S32\_SIRC\_CLK   3U |
| --- |

## [◆ ](#a4d7d43fd0155026fa6e15624e3b2ec49)NXP\_S32\_SIRC\_STANDBY\_CLK

| #define NXP\_S32\_SIRC\_STANDBY\_CLK   4U |
| --- |

## [◆ ](#a2814540c94848acfbb49b2c8b9be4ad2)NXP\_S32\_SIUL2\_CLK

| #define NXP\_S32\_SIUL2\_CLK   130U |
| --- |

## [◆ ](#a1589ff94052ec884cd173d896c2d2d3d)NXP\_S32\_STCU0\_CLK

| #define NXP\_S32\_STCU0\_CLK   131U |
| --- |

## [◆ ](#ac3cc906db4f46606943573ad6582bcaf)NXP\_S32\_STM0\_CLK

| #define NXP\_S32\_STM0\_CLK   133U |
| --- |

## [◆ ](#a605907a7a763a74e6b6c5b6f374f7469)NXP\_S32\_STM1\_CLK

| #define NXP\_S32\_STM1\_CLK   135U |
| --- |

## [◆ ](#a951b5215866501d57a1231bdcbf6c937)NXP\_S32\_STMA\_CLK

| #define NXP\_S32\_STMA\_CLK   132U |
| --- |

## [◆ ](#a41ac38f92beac668afbcb88f049f6d83)NXP\_S32\_STMB\_CLK

| #define NXP\_S32\_STMB\_CLK   134U |
| --- |

## [◆ ](#a21446770924672e8f9efb8becaf378fb)NXP\_S32\_SWT0\_CLK

| #define NXP\_S32\_SWT0\_CLK   136U |
| --- |

## [◆ ](#a93d90fef864ce343237f0698bc1637e4)NXP\_S32\_SXOSC\_CLK

| #define NXP\_S32\_SXOSC\_CLK   6U |
| --- |

## [◆ ](#aeaf92d23687006556891f773b814340a)NXP\_S32\_TEMPSENSE\_CLK

| #define NXP\_S32\_TEMPSENSE\_CLK   137U |
| --- |

## [◆ ](#a6a6963b78096148b569b9e07cf82faaf)NXP\_S32\_TRACE\_CLK

| #define NXP\_S32\_TRACE\_CLK   138U |
| --- |

## [◆ ](#a3ea3b033b0b8662cf3320ee7cfd99581)NXP\_S32\_TRGMUX0\_CLK

| #define NXP\_S32\_TRGMUX0\_CLK   139U |
| --- |

## [◆ ](#a8178328a4fb78be2204f7543eb786347)NXP\_S32\_TSENSE0\_CLK

| #define NXP\_S32\_TSENSE0\_CLK   140U |
| --- |

## [◆ ](#a2bbf381a7dc2b42c9867ab1336efc4bd)NXP\_S32\_WKPU0\_CLK

| #define NXP\_S32\_WKPU0\_CLK   141U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [nxp\_s32k344\_clock.h](nxp__s32k344__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
