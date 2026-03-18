---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nxp__s32k344__clock_8h_source.html
original_path: doxygen/html/nxp__s32k344__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_s32k344\_clock.h

[Go to the documentation of this file.](nxp__s32k344__clock_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32K344\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32K344\_CLOCK\_H\_

9

[ 10](nxp__s32k344__clock_8h.md#a8f4673a159fb26c90ae29761784395e9)#define NXP\_S32\_FIRC\_CLK 1U

[ 11](nxp__s32k344__clock_8h.md#adaf10ac3403cbc604411477959f968f7)#define NXP\_S32\_FIRC\_STANDBY\_CLK 2U

[ 12](nxp__s32k344__clock_8h.md#adc1da7bf433a80a3a975e172a30abbbc)#define NXP\_S32\_SIRC\_CLK 3U

[ 13](nxp__s32k344__clock_8h.md#a4d7d43fd0155026fa6e15624e3b2ec49)#define NXP\_S32\_SIRC\_STANDBY\_CLK 4U

[ 14](nxp__s32k344__clock_8h.md#ab748e7ec615dc5fe10cafc723cc289fe)#define NXP\_S32\_FXOSC\_CLK 5U

[ 15](nxp__s32k344__clock_8h.md#a93d90fef864ce343237f0698bc1637e4)#define NXP\_S32\_SXOSC\_CLK 6U

[ 16](nxp__s32k344__clock_8h.md#ad630b290fc45bb016fab33c63866c3f4)#define NXP\_S32\_PLL\_CLK 7U

[ 17](nxp__s32k344__clock_8h.md#a9776eee648f0ba77e662bc36e0f97395)#define NXP\_S32\_PLL\_POSTDIV\_CLK 8U

[ 18](nxp__s32k344__clock_8h.md#a7bac186b3f321194a8fbe568bcb42a01)#define NXP\_S32\_PLL\_PHI0\_CLK 9U

[ 19](nxp__s32k344__clock_8h.md#acba73923ac0927a9491e81fbe38806e2)#define NXP\_S32\_PLL\_PHI1\_CLK 10U

[ 20](nxp__s32k344__clock_8h.md#a685f8303272306ff9b6525f975818621)#define NXP\_S32\_EMAC\_MII\_RX\_CLK 11U

[ 21](nxp__s32k344__clock_8h.md#ae07fa6829614f632634b77db0bbed29d)#define NXP\_S32\_EMAC\_MII\_RMII\_TX\_CLK 12U

[ 22](nxp__s32k344__clock_8h.md#a8839149b54e955dd82ffcd7d3165672f)#define NXP\_S32\_SCS\_CLK 13U

[ 23](nxp__s32k344__clock_8h.md#a3addb6ad5d596e0b9739f34f00bc4ffc)#define NXP\_S32\_CORE\_CLK 14U

[ 24](nxp__s32k344__clock_8h.md#a66e65995472438ff7c81a50411a69a1a)#define NXP\_S32\_AIPS\_PLAT\_CLK 15U

[ 25](nxp__s32k344__clock_8h.md#a087daa0b5c6e9ffb3c19eab447e7f640)#define NXP\_S32\_AIPS\_SLOW\_CLK 16U

[ 26](nxp__s32k344__clock_8h.md#aed00182fc87a5dc5c2b5ede1ef42e70b)#define NXP\_S32\_HSE\_CLK 17U

[ 27](nxp__s32k344__clock_8h.md#a861f901e140d9a294b2eb16bcf215f73)#define NXP\_S32\_DCM\_CLK 18U

[ 28](nxp__s32k344__clock_8h.md#a15a7cd222d732219e2ee316118ff4687)#define NXP\_S32\_LBIST\_CLK 19U

[ 29](nxp__s32k344__clock_8h.md#a944dcec4426ee975d282486754cd63fb)#define NXP\_S32\_QSPI\_MEM\_CLK 20U

[ 30](nxp__s32k344__clock_8h.md#a4b24e8f3122d410d7f6ab4edbb3f0408)#define NXP\_S32\_CLKOUT\_RUN\_CLK 21U

[ 31](nxp__s32k344__clock_8h.md#a89fe6bb1365a3895449da72ccd517223)#define NXP\_S32\_ADC0\_CLK 23U

[ 32](nxp__s32k344__clock_8h.md#ace9575b4ed012fe344884b0b1fa2ef58)#define NXP\_S32\_ADC1\_CLK 24U

[ 33](nxp__s32k344__clock_8h.md#a439427d875a21738d142787685f3102d)#define NXP\_S32\_ADC2\_CLK 25U

[ 34](nxp__s32k344__clock_8h.md#a93297d4a6baae69c82ceb3c5dc6421d6)#define NXP\_S32\_BCTU0\_CLK 26U

[ 35](nxp__s32k344__clock_8h.md#a83be292b22509e1255e1fc07161ca0c6)#define NXP\_S32\_CLKOUT\_STANDBY\_CLK 27U

[ 36](nxp__s32k344__clock_8h.md#a44f6895b60c611c68da8d9674af0d474)#define NXP\_S32\_CMP0\_CLK 28U

[ 37](nxp__s32k344__clock_8h.md#a6cf084d9263d934093becb8348b83cd9)#define NXP\_S32\_CMP1\_CLK 29U

[ 38](nxp__s32k344__clock_8h.md#ac2fac23465983168709fbe481a49728b)#define NXP\_S32\_CMP2\_CLK 30U

[ 39](nxp__s32k344__clock_8h.md#a236cf04ea860d48a382096caea32d2b1)#define NXP\_S32\_CRC0\_CLK 31U

[ 40](nxp__s32k344__clock_8h.md#a263fcc4db494692b432edd667ae14b58)#define NXP\_S32\_DCM0\_CLK 32U

[ 41](nxp__s32k344__clock_8h.md#a97a3ff5238f4878784ee1bee4cfc7522)#define NXP\_S32\_DMAMUX0\_CLK 33U

[ 42](nxp__s32k344__clock_8h.md#a708913d2bb71ec975caad705a10b8421)#define NXP\_S32\_DMAMUX1\_CLK 34U

[ 43](nxp__s32k344__clock_8h.md#ae8b13f1f1803f214f7c7ba371679ee6f)#define NXP\_S32\_EDMA0\_CLK 35U

[ 44](nxp__s32k344__clock_8h.md#aa5ddb09ddd5067525ca580b8c4af5c36)#define NXP\_S32\_EDMA0\_TCD0\_CLK 36U

[ 45](nxp__s32k344__clock_8h.md#a7d24907ee4b061def55f9aa966adeeca)#define NXP\_S32\_EDMA0\_TCD1\_CLK 37U

[ 46](nxp__s32k344__clock_8h.md#a364079ab2d5d101d7ab9683ea0743568)#define NXP\_S32\_EDMA0\_TCD2\_CLK 38U

[ 47](nxp__s32k344__clock_8h.md#a345d2bc4db0dc7b1fcde0ec99ca73804)#define NXP\_S32\_EDMA0\_TCD3\_CLK 39U

[ 48](nxp__s32k344__clock_8h.md#a18bfc4a0f2141a579cb6860e58d4ae5a)#define NXP\_S32\_EDMA0\_TCD4\_CLK 40U

[ 49](nxp__s32k344__clock_8h.md#a09eaf35cc66d13dc07846b0dfa4700f5)#define NXP\_S32\_EDMA0\_TCD5\_CLK 41U

[ 50](nxp__s32k344__clock_8h.md#a2ff1d32586c02b3f2532c4259c070365)#define NXP\_S32\_EDMA0\_TCD6\_CLK 42U

[ 51](nxp__s32k344__clock_8h.md#a7da0580971ce98f3508afb7c13c6ff27)#define NXP\_S32\_EDMA0\_TCD7\_CLK 43U

[ 52](nxp__s32k344__clock_8h.md#a501fc394e4205f0469a82b7d91a118e3)#define NXP\_S32\_EDMA0\_TCD8\_CLK 44U

[ 53](nxp__s32k344__clock_8h.md#a970cf76b8d2002613e79239f7b914931)#define NXP\_S32\_EDMA0\_TCD9\_CLK 45U

[ 54](nxp__s32k344__clock_8h.md#ab0a57e5bb066e7a8703dfa74f71ed28f)#define NXP\_S32\_EDMA0\_TCD10\_CLK 46U

[ 55](nxp__s32k344__clock_8h.md#ab9d76bd6ef0a976bd637bef558ead505)#define NXP\_S32\_EDMA0\_TCD11\_CLK 47U

[ 56](nxp__s32k344__clock_8h.md#a83eac3871822e740be19b07cba0cfe88)#define NXP\_S32\_EDMA0\_TCD12\_CLK 48U

[ 57](nxp__s32k344__clock_8h.md#af67b7883216b5821efee3bd5dd83cc8e)#define NXP\_S32\_EDMA0\_TCD13\_CLK 49U

[ 58](nxp__s32k344__clock_8h.md#affb8b8d4898c93574b3e286ebb6a875d)#define NXP\_S32\_EDMA0\_TCD14\_CLK 50U

[ 59](nxp__s32k344__clock_8h.md#a8d1c96d3a35e0e8b3b01cdde4bea0bf4)#define NXP\_S32\_EDMA0\_TCD15\_CLK 51U

[ 60](nxp__s32k344__clock_8h.md#a179bafeddd54b29801ef5ea9f18dffd0)#define NXP\_S32\_EDMA0\_TCD16\_CLK 52U

[ 61](nxp__s32k344__clock_8h.md#a1a84b3f1413fb4850547f8016e173898)#define NXP\_S32\_EDMA0\_TCD17\_CLK 53U

[ 62](nxp__s32k344__clock_8h.md#a61d898070713033029178e1ad9434196)#define NXP\_S32\_EDMA0\_TCD18\_CLK 54U

[ 63](nxp__s32k344__clock_8h.md#a62e2b7d1584b456143bd4a9bb7a08b2f)#define NXP\_S32\_EDMA0\_TCD19\_CLK 55U

[ 64](nxp__s32k344__clock_8h.md#a08ed1758962b643d44bce3b7054d56f9)#define NXP\_S32\_EDMA0\_TCD20\_CLK 56U

[ 65](nxp__s32k344__clock_8h.md#ae35552f9675dff63a199b39cca13d97f)#define NXP\_S32\_EDMA0\_TCD21\_CLK 57U

[ 66](nxp__s32k344__clock_8h.md#a193891b8e165f2a005380e281d3cada6)#define NXP\_S32\_EDMA0\_TCD22\_CLK 58U

[ 67](nxp__s32k344__clock_8h.md#a5ea305b51c42cae9dc90ad96d68ecebd)#define NXP\_S32\_EDMA0\_TCD23\_CLK 59U

[ 68](nxp__s32k344__clock_8h.md#aafc4119cefe803821d14e0f246db143d)#define NXP\_S32\_EDMA0\_TCD24\_CLK 60U

[ 69](nxp__s32k344__clock_8h.md#a657ca4b3c6efd5892c60b5f3455b275d)#define NXP\_S32\_EDMA0\_TCD25\_CLK 61U

[ 70](nxp__s32k344__clock_8h.md#a79f4bff79205657e670e59e0aef52e28)#define NXP\_S32\_EDMA0\_TCD26\_CLK 62U

[ 71](nxp__s32k344__clock_8h.md#a801c12d831a651143705d3bf79c6db8e)#define NXP\_S32\_EDMA0\_TCD27\_CLK 63U

[ 72](nxp__s32k344__clock_8h.md#a17d3b0d7f197a02403dc67a5b56b5c33)#define NXP\_S32\_EDMA0\_TCD28\_CLK 64U

[ 73](nxp__s32k344__clock_8h.md#a064f390645ce062c028fbfe383299a10)#define NXP\_S32\_EDMA0\_TCD29\_CLK 65U

[ 74](nxp__s32k344__clock_8h.md#a48e3b322448916841208b11f89365c31)#define NXP\_S32\_EDMA0\_TCD30\_CLK 66U

[ 75](nxp__s32k344__clock_8h.md#a4e525a7e6ea34a5ab8b1f2d133fbe2e7)#define NXP\_S32\_EDMA0\_TCD31\_CLK 67U

[ 76](nxp__s32k344__clock_8h.md#ad2e33a9acd3a442b3036458795d1b0c5)#define NXP\_S32\_EIM\_CLK 68U

[ 77](nxp__s32k344__clock_8h.md#adf84198aec5f5182883113beea3615f8)#define NXP\_S32\_EMAC\_RX\_CLK 69U

[ 78](nxp__s32k344__clock_8h.md#aa59259703780d4cdff42589dbbcc49f3)#define NXP\_S32\_EMAC0\_RX\_CLK 70U

[ 79](nxp__s32k344__clock_8h.md#a2990ad5b6cfcbb88e301c0e6e4ea438b)#define NXP\_S32\_EMAC\_TS\_CLK 71U

[ 80](nxp__s32k344__clock_8h.md#a3bb76fd0f956c779da97ff36cbca3e98)#define NXP\_S32\_EMAC0\_TS\_CLK 72U

[ 81](nxp__s32k344__clock_8h.md#ae07e1cc028d1280610e0cd4831332e96)#define NXP\_S32\_EMAC\_TX\_CLK 73U

[ 82](nxp__s32k344__clock_8h.md#a10b3a801cfe769ff0ac0bdc2979b5e16)#define NXP\_S32\_EMAC0\_TX\_CLK 74U

[ 83](nxp__s32k344__clock_8h.md#abc50bd8ecae9ffac02421389575302cc)#define NXP\_S32\_EMIOS0\_CLK 75U

[ 84](nxp__s32k344__clock_8h.md#a93ae95e32c998bfe99ad03c4b953261e)#define NXP\_S32\_EMIOS1\_CLK 76U

[ 85](nxp__s32k344__clock_8h.md#ab808fbaa6e6a14d622fff1aceac04319)#define NXP\_S32\_EMIOS2\_CLK 77U

[ 86](nxp__s32k344__clock_8h.md#a5330dac04dd7c5b914f65920731472fd)#define NXP\_S32\_ERM0\_CLK 78U

[ 87](nxp__s32k344__clock_8h.md#accfc99304f1187d908296ac24eea41f1)#define NXP\_S32\_FLEXCANA\_CLK 79U

[ 88](nxp__s32k344__clock_8h.md#a308e74a366725070c56a4ab4fc7c300a)#define NXP\_S32\_FLEXCAN0\_CLK 80U

[ 89](nxp__s32k344__clock_8h.md#ad353c07d914cfa8c45ed3b7b586c2b00)#define NXP\_S32\_FLEXCAN1\_CLK 81U

[ 90](nxp__s32k344__clock_8h.md#a54467688a58d9be77849eddd031f126e)#define NXP\_S32\_FLEXCAN2\_CLK 82U

[ 91](nxp__s32k344__clock_8h.md#ab6f76cc8ee9a2d120dc048ae07b1ac31)#define NXP\_S32\_FLEXCANB\_CLK 83U

[ 92](nxp__s32k344__clock_8h.md#a0fcf00296138cd26e845ab524054fd3b)#define NXP\_S32\_FLEXCAN3\_CLK 84U

[ 93](nxp__s32k344__clock_8h.md#a6106f0f8b5e0f5230b75e43b5ccdbf0e)#define NXP\_S32\_FLEXCAN4\_CLK 85U

[ 94](nxp__s32k344__clock_8h.md#a4f3b1864f3f5bcc6a1fd66e27eb12a52)#define NXP\_S32\_FLEXCAN5\_CLK 86U

[ 95](nxp__s32k344__clock_8h.md#a3a15b5fc1e3242c0399c7dd46e46fdd4)#define NXP\_S32\_FLEXIO0\_CLK 87U

[ 96](nxp__s32k344__clock_8h.md#a5df33aea12ebef163135151c48c4e7cf)#define NXP\_S32\_INTM\_CLK 88U

[ 97](nxp__s32k344__clock_8h.md#acafd9bf768c57ddb9747ee65ce27598a)#define NXP\_S32\_LCU0\_CLK 89U

[ 98](nxp__s32k344__clock_8h.md#ab799c3834e9756bdea0e749aa9d88abd)#define NXP\_S32\_LCU1\_CLK 90U

[ 99](nxp__s32k344__clock_8h.md#a381f2ad32adfa495e9020788f5211aee)#define NXP\_S32\_LPI2C0\_CLK 91U

[ 100](nxp__s32k344__clock_8h.md#a3f1f16418e5055f7907508ff4d46c522)#define NXP\_S32\_LPI2C1\_CLK 92U

[ 101](nxp__s32k344__clock_8h.md#a3c5548bea0bf573ee5c34064ccc5eb5f)#define NXP\_S32\_LPSPI0\_CLK 93U

[ 102](nxp__s32k344__clock_8h.md#a0d581a4df52c36546fe58e947d6b62ae)#define NXP\_S32\_LPSPI1\_CLK 94U

[ 103](nxp__s32k344__clock_8h.md#a8ae234050a66b6857bf34769d485c7e4)#define NXP\_S32\_LPSPI2\_CLK 95U

[ 104](nxp__s32k344__clock_8h.md#a5b9440566cba4efa7904a00384310a2b)#define NXP\_S32\_LPSPI3\_CLK 96U

[ 105](nxp__s32k344__clock_8h.md#a46b7dfdff4ca08036ecc76031d987d2e)#define NXP\_S32\_LPSPI4\_CLK 97U

[ 106](nxp__s32k344__clock_8h.md#a968b718186547fc88bc290939792decf)#define NXP\_S32\_LPSPI5\_CLK 98U

[ 107](nxp__s32k344__clock_8h.md#a49beda273937c66398354636595e7d1c)#define NXP\_S32\_LPUART0\_CLK 99U

[ 108](nxp__s32k344__clock_8h.md#af5ca4a56001a2e39ed143adbd15d2219)#define NXP\_S32\_LPUART1\_CLK 100U

[ 109](nxp__s32k344__clock_8h.md#ad9303a366af8d2e1b160bf82adc894fe)#define NXP\_S32\_LPUART2\_CLK 101U

[ 110](nxp__s32k344__clock_8h.md#a696e0636cc8a6c3b6c7158f2fe221a80)#define NXP\_S32\_LPUART3\_CLK 102U

[ 111](nxp__s32k344__clock_8h.md#a55d4b1d4733bf6405b30e0bfdeb84a19)#define NXP\_S32\_LPUART4\_CLK 103U

[ 112](nxp__s32k344__clock_8h.md#a8986cf7bbabcfd33be679321ce7e6fa9)#define NXP\_S32\_LPUART5\_CLK 104U

[ 113](nxp__s32k344__clock_8h.md#a294d79027be7372f1b6b1f4afce99d91)#define NXP\_S32\_LPUART6\_CLK 105U

[ 114](nxp__s32k344__clock_8h.md#a01038ad550a11f12779d666364336e8d)#define NXP\_S32\_LPUART7\_CLK 106U

[ 115](nxp__s32k344__clock_8h.md#a327cb53647a534e3361ae7b208dde92e)#define NXP\_S32\_LPUART8\_CLK 107U

[ 116](nxp__s32k344__clock_8h.md#afd38741c6071e8489c579e80b9c17479)#define NXP\_S32\_LPUART9\_CLK 108U

[ 117](nxp__s32k344__clock_8h.md#aa8d39f79fc0afc065acdc78c29cd668c)#define NXP\_S32\_LPUART10\_CLK 109U

[ 118](nxp__s32k344__clock_8h.md#a4c398ddca86d95484584ef878beafa2b)#define NXP\_S32\_LPUART11\_CLK 110U

[ 119](nxp__s32k344__clock_8h.md#a3808a48039cbc4eb2b656df9ec4f8bfc)#define NXP\_S32\_LPUART12\_CLK 111U

[ 120](nxp__s32k344__clock_8h.md#ac9bbead64f9bf1df293da5f2e96c650d)#define NXP\_S32\_LPUART13\_CLK 112U

[ 121](nxp__s32k344__clock_8h.md#a32b9022da94a1891b83588c16c6c5373)#define NXP\_S32\_LPUART14\_CLK 113U

[ 122](nxp__s32k344__clock_8h.md#a3474c5a33569dc233c54e41990a8daf8)#define NXP\_S32\_LPUART15\_CLK 114U

[ 123](nxp__s32k344__clock_8h.md#a045348716b7d0c9f7c286226786a1587)#define NXP\_S32\_MSCM\_CLK 115U

[ 124](nxp__s32k344__clock_8h.md#a122abc9d70dcb3c4b4bc0082d874db43)#define NXP\_S32\_MU2A\_CLK 116U

[ 125](nxp__s32k344__clock_8h.md#a0c88a60820dbafe53eaf2badf443cd3c)#define NXP\_S32\_MU2B\_CLK 117U

[ 126](nxp__s32k344__clock_8h.md#a0352473aa201738f3c6476dee1551956)#define NXP\_S32\_PIT0\_CLK 118U

[ 127](nxp__s32k344__clock_8h.md#a8005e37da1d529a8340afe773fcb5291)#define NXP\_S32\_PIT1\_CLK 119U

[ 128](nxp__s32k344__clock_8h.md#a7a25f5a452598e9ec637f2b09c61f96b)#define NXP\_S32\_PIT2\_CLK 120U

[ 129](nxp__s32k344__clock_8h.md#a99dcc3421a01f3c684be71561e305421)#define NXP\_S32\_QSPI0\_CLK 121U

[ 130](nxp__s32k344__clock_8h.md#a2c02e14aa6e2f26676a9cbf3b9252764)#define NXP\_S32\_QSPI0\_RAM\_CLK 122U

[ 131](nxp__s32k344__clock_8h.md#ad69581caba8b97eab4fddf3a28a15dc9)#define NXP\_S32\_QSPI0\_TX\_MEM\_CLK 123U

[ 132](nxp__s32k344__clock_8h.md#a74842614cadb4868a08a71932a6eb60a)#define NXP\_S32\_QSPI\_SFCK\_CLK 124U

[ 133](nxp__s32k344__clock_8h.md#a1ca20b16f6a430cddd8fc1d55fd7a840)#define NXP\_S32\_RTC\_CLK 125U

[ 134](nxp__s32k344__clock_8h.md#ae883db6b1e83c7e5f43004c38a496b58)#define NXP\_S32\_RTC0\_CLK 126U

[ 135](nxp__s32k344__clock_8h.md#a816aa8f3387ee596c7f7409d1f546dec)#define NXP\_S32\_SAI0\_CLK 127U

[ 136](nxp__s32k344__clock_8h.md#a45d6b8b3a35d8a03a8f9a24dfda6acb6)#define NXP\_S32\_SAI1\_CLK 128U

[ 137](nxp__s32k344__clock_8h.md#a11238766b6cf870c9fe7e27565a963e8)#define NXP\_S32\_SEMA42\_CLK 129U

[ 138](nxp__s32k344__clock_8h.md#a2814540c94848acfbb49b2c8b9be4ad2)#define NXP\_S32\_SIUL2\_CLK 130U

[ 139](nxp__s32k344__clock_8h.md#a1589ff94052ec884cd173d896c2d2d3d)#define NXP\_S32\_STCU0\_CLK 131U

[ 140](nxp__s32k344__clock_8h.md#a951b5215866501d57a1231bdcbf6c937)#define NXP\_S32\_STMA\_CLK 132U

[ 141](nxp__s32k344__clock_8h.md#ac3cc906db4f46606943573ad6582bcaf)#define NXP\_S32\_STM0\_CLK 133U

[ 142](nxp__s32k344__clock_8h.md#a41ac38f92beac668afbcb88f049f6d83)#define NXP\_S32\_STMB\_CLK 134U

[ 143](nxp__s32k344__clock_8h.md#a605907a7a763a74e6b6c5b6f374f7469)#define NXP\_S32\_STM1\_CLK 135U

[ 144](nxp__s32k344__clock_8h.md#a21446770924672e8f9efb8becaf378fb)#define NXP\_S32\_SWT0\_CLK 136U

[ 145](nxp__s32k344__clock_8h.md#aeaf92d23687006556891f773b814340a)#define NXP\_S32\_TEMPSENSE\_CLK 137U

[ 146](nxp__s32k344__clock_8h.md#a6a6963b78096148b569b9e07cf82faaf)#define NXP\_S32\_TRACE\_CLK 138U

[ 147](nxp__s32k344__clock_8h.md#a3ea3b033b0b8662cf3320ee7cfd99581)#define NXP\_S32\_TRGMUX0\_CLK 139U

[ 148](nxp__s32k344__clock_8h.md#a8178328a4fb78be2204f7543eb786347)#define NXP\_S32\_TSENSE0\_CLK 140U

[ 149](nxp__s32k344__clock_8h.md#a2bbf381a7dc2b42c9867ab1336efc4bd)#define NXP\_S32\_WKPU0\_CLK 141U

150

151#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32K344\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [nxp\_s32k344\_clock.h](nxp__s32k344__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
