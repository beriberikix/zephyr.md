---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp__s32k146__clock_8h_source.html
original_path: doxygen/html/nxp__s32k146__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_s32k146\_clock.h

[Go to the documentation of this file.](nxp__s32k146__clock_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32K146\_CLOCK\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32K146\_CLOCK\_H\_

9

[ 10](nxp__s32k146__clock_8h.md#ae5e10a14cc0f227d8c483d35c0df9cce)#define NXP\_S32\_LPO\_128K\_CLK 1U

[ 11](nxp__s32k146__clock_8h.md#adc1da7bf433a80a3a975e172a30abbbc)#define NXP\_S32\_SIRC\_CLK 2U

[ 12](nxp__s32k146__clock_8h.md#a7f7b85f65139224474cb6c3e867fe879)#define NXP\_S32\_SIRC\_VLP\_CLK 3U

[ 13](nxp__s32k146__clock_8h.md#a04e02db4c5466214e76b8323634a01a6)#define NXP\_S32\_SIRC\_STOP\_CLK 4U

[ 14](nxp__s32k146__clock_8h.md#a8f4673a159fb26c90ae29761784395e9)#define NXP\_S32\_FIRC\_CLK 5U

[ 15](nxp__s32k146__clock_8h.md#ada989b740d4d8f5c111fce02943b835c)#define NXP\_S32\_FIRC\_VLP\_CLK 6U

[ 16](nxp__s32k146__clock_8h.md#a688524357cead34820bc0122325b3e15)#define NXP\_S32\_FIRC\_STOP\_CLK 7U

[ 17](nxp__s32k146__clock_8h.md#a49b53fcd4cf55c8a24b1670119392e24)#define NXP\_S32\_SOSC\_CLK 8U

[ 18](nxp__s32k146__clock_8h.md#a401c77f822de9ac078f1629cafb24a34)#define NXP\_S32\_SPLL\_CLK 9U

[ 19](nxp__s32k146__clock_8h.md#a1637b000e817e50ef4fd8c55b2327e1f)#define NXP\_S32\_SIRCDIV1\_CLK 10U

[ 20](nxp__s32k146__clock_8h.md#a670ed7e0f1b37ff5c6a33fee3fcee1fe)#define NXP\_S32\_SIRCDIV2\_CLK 11U

[ 21](nxp__s32k146__clock_8h.md#a5bbe7c5b5b576dc21dafdc4a9c16d83c)#define NXP\_S32\_FIRCDIV1\_CLK 12U

[ 22](nxp__s32k146__clock_8h.md#aa15bbe9eff8a09df5dda01324d1b0be9)#define NXP\_S32\_FIRCDIV2\_CLK 13U

[ 23](nxp__s32k146__clock_8h.md#a6764ee23b79692bffb464be0e4cd0a02)#define NXP\_S32\_SOSCDIV1\_CLK 14U

[ 24](nxp__s32k146__clock_8h.md#aa2371431504707419466f3392444e72e)#define NXP\_S32\_SOSCDIV2\_CLK 15U

[ 25](nxp__s32k146__clock_8h.md#aeae9584a1ba85fe28178748e0ded825f)#define NXP\_S32\_SPLLDIV1\_CLK 16U

[ 26](nxp__s32k146__clock_8h.md#ab553d243097da1d22834c00c743ac829)#define NXP\_S32\_SPLLDIV2\_CLK 17U

[ 27](nxp__s32k146__clock_8h.md#a11db7a17fe6729120064ff68491aa99d)#define NXP\_S32\_LPO\_32K\_CLK 18U

[ 28](nxp__s32k146__clock_8h.md#a4b9330443edbddcaaf60595755888684)#define NXP\_S32\_LPO\_1K\_CLK 19U

[ 29](nxp__s32k146__clock_8h.md#a8c800a6a41f9a8d7463b44609bfc7b66)#define NXP\_S32\_TCLK0\_REF\_CLK 20U

[ 30](nxp__s32k146__clock_8h.md#aae61abdec779b428797e8b4dda8451a2)#define NXP\_S32\_TCLK1\_REF\_CLK 21U

[ 31](nxp__s32k146__clock_8h.md#a019249c31141a74cad5be9f68dde34b0)#define NXP\_S32\_TCLK2\_REF\_CLK 22U

[ 32](nxp__s32k146__clock_8h.md#a8839149b54e955dd82ffcd7d3165672f)#define NXP\_S32\_SCS\_CLK 24U

[ 33](nxp__s32k146__clock_8h.md#a6b103eabec7835b65bb5f251d878b9eb)#define NXP\_S32\_SCS\_RUN\_CLK 25U

[ 34](nxp__s32k146__clock_8h.md#ac55701d09adc15b66c4da17d89eb6e35)#define NXP\_S32\_SCS\_VLPR\_CLK 26U

[ 35](nxp__s32k146__clock_8h.md#ab2fa7b71b2deed99ecb864574544b662)#define NXP\_S32\_SCS\_HSRUN\_CLK 27U

[ 36](nxp__s32k146__clock_8h.md#a3addb6ad5d596e0b9739f34f00bc4ffc)#define NXP\_S32\_CORE\_CLK 28U

[ 37](nxp__s32k146__clock_8h.md#aa11f09f442efee9a866297c81c8f284d)#define NXP\_S32\_CORE\_RUN\_CLK 29U

[ 38](nxp__s32k146__clock_8h.md#adfc9b5f87de0f3588a42dd8867fa4d98)#define NXP\_S32\_CORE\_VLPR\_CLK 30U

[ 39](nxp__s32k146__clock_8h.md#aaa0f0bdb41447451e575d5a72b4b0667)#define NXP\_S32\_CORE\_HSRUN\_CLK 31U

[ 40](nxp__s32k146__clock_8h.md#aa53d8f3a4fed316c4b15f3d3470138ff)#define NXP\_S32\_BUS\_CLK 32U

[ 41](nxp__s32k146__clock_8h.md#a33179b814af0974e3ee0e7deabb11b0b)#define NXP\_S32\_BUS\_RUN\_CLK 33U

[ 42](nxp__s32k146__clock_8h.md#a816af3949d0ac497958447f70875eb6a)#define NXP\_S32\_BUS\_VLPR\_CLK 34U

[ 43](nxp__s32k146__clock_8h.md#af04697ed35e63758f3cd51efa5aeeaea)#define NXP\_S32\_BUS\_HSRUN\_CLK 35U

[ 44](nxp__s32k146__clock_8h.md#ad6114a16219057fbc761de1254e8f0ed)#define NXP\_S32\_SLOW\_CLK 36U

[ 45](nxp__s32k146__clock_8h.md#aa36a38d3a3a44cc3d96ce8da5edac484)#define NXP\_S32\_SLOW\_RUN\_CLK 37U

[ 46](nxp__s32k146__clock_8h.md#a6382c0637bc32b870697c2cc0ac5b49d)#define NXP\_S32\_SLOW\_VLPR\_CLK 38U

[ 47](nxp__s32k146__clock_8h.md#a2a615264b242a9115bc4b32b87cbf9bc)#define NXP\_S32\_SLOW\_HSRUN\_CLK 39U

[ 48](nxp__s32k146__clock_8h.md#a1ca20b16f6a430cddd8fc1d55fd7a840)#define NXP\_S32\_RTC\_CLK 40U

[ 49](nxp__s32k146__clock_8h.md#a2dca83f3da5ff6336bc65c0d55dfb980)#define NXP\_S32\_LPO\_CLK 41U

[ 50](nxp__s32k146__clock_8h.md#ad44809519c492290877741346f046f9f)#define NXP\_S32\_SCG\_CLKOUT\_CLK 42U

[ 51](nxp__s32k146__clock_8h.md#addc3582ba7517f6dea0ab5f8727c15de)#define NXP\_S32\_FTM0\_EXT\_CLK 43U

[ 52](nxp__s32k146__clock_8h.md#abae06e872b9f9b3926c49b1fdce854e1)#define NXP\_S32\_FTM1\_EXT\_CLK 44U

[ 53](nxp__s32k146__clock_8h.md#aefe843e849c2b0fb998e6725b040e566)#define NXP\_S32\_FTM2\_EXT\_CLK 45U

[ 54](nxp__s32k146__clock_8h.md#af674e053817be8fcaf9f959ea8ef7ba5)#define NXP\_S32\_FTM3\_EXT\_CLK 46U

[ 55](nxp__s32k146__clock_8h.md#a2fee6db6612f63f7ae2a0f12dba1fbdd)#define NXP\_S32\_FTM4\_EXT\_CLK 47U

[ 56](nxp__s32k146__clock_8h.md#aeca299c818cb5576d578daf8f8872bb7)#define NXP\_S32\_FTM5\_EXT\_CLK 48U

[ 57](nxp__s32k146__clock_8h.md#a89fe6bb1365a3895449da72ccd517223)#define NXP\_S32\_ADC0\_CLK 50U

[ 58](nxp__s32k146__clock_8h.md#ace9575b4ed012fe344884b0b1fa2ef58)#define NXP\_S32\_ADC1\_CLK 51U

[ 59](nxp__s32k146__clock_8h.md#a63aca9fbcdae28cd448e62e9dcf41da9)#define NXP\_S32\_CLKOUT0\_CLK 52U

[ 60](nxp__s32k146__clock_8h.md#a44f6895b60c611c68da8d9674af0d474)#define NXP\_S32\_CMP0\_CLK 53U

[ 61](nxp__s32k146__clock_8h.md#a236cf04ea860d48a382096caea32d2b1)#define NXP\_S32\_CRC0\_CLK 54U

[ 62](nxp__s32k146__clock_8h.md#ad5b14f1c8c328d8293003cb0874523d7)#define NXP\_S32\_DMA0\_CLK 55U

[ 63](nxp__s32k146__clock_8h.md#a97a3ff5238f4878784ee1bee4cfc7522)#define NXP\_S32\_DMAMUX0\_CLK 56U

[ 64](nxp__s32k146__clock_8h.md#a73fd9c7c0b123b0b434097cce57b9b61)#define NXP\_S32\_EIM0\_CLK 57U

[ 65](nxp__s32k146__clock_8h.md#a5330dac04dd7c5b914f65920731472fd)#define NXP\_S32\_ERM0\_CLK 58U

[ 66](nxp__s32k146__clock_8h.md#adcb4cd2738c435bbd12ec0eb2de405b1)#define NXP\_S32\_EWM0\_CLK 59U

[ 67](nxp__s32k146__clock_8h.md#a308e74a366725070c56a4ab4fc7c300a)#define NXP\_S32\_FLEXCAN0\_CLK 60U

[ 68](nxp__s32k146__clock_8h.md#ad353c07d914cfa8c45ed3b7b586c2b00)#define NXP\_S32\_FLEXCAN1\_CLK 61U

[ 69](nxp__s32k146__clock_8h.md#a54467688a58d9be77849eddd031f126e)#define NXP\_S32\_FLEXCAN2\_CLK 62U

[ 70](nxp__s32k146__clock_8h.md#a0b7d5641dd840045a5c5c5dfc5642edf)#define NXP\_S32\_FLEXIO\_CLK 63U

[ 71](nxp__s32k146__clock_8h.md#af20dda1efa2e59c3665a7e2cb77022d1)#define NXP\_S32\_FTFC\_CLK 64U

[ 72](nxp__s32k146__clock_8h.md#a1fea1f63010c7e40e29c01ec795f7b3d)#define NXP\_S32\_FTM0\_CLK 65U

[ 73](nxp__s32k146__clock_8h.md#a008543228f51354a67e4ad973cb40391)#define NXP\_S32\_FTM1\_CLK 66U

[ 74](nxp__s32k146__clock_8h.md#abb38c0a85aa9d2e9cd4a3aa932dfd0c6)#define NXP\_S32\_FTM2\_CLK 67U

[ 75](nxp__s32k146__clock_8h.md#ac4151cc371cc1c0586e9ec0e47f17825)#define NXP\_S32\_FTM3\_CLK 68U

[ 76](nxp__s32k146__clock_8h.md#a05b9cef1f4544c696cd2513aa0430b89)#define NXP\_S32\_FTM4\_CLK 69U

[ 77](nxp__s32k146__clock_8h.md#a3909ae4f1d7951765436349272757f03)#define NXP\_S32\_FTM5\_CLK 70U

[ 78](nxp__s32k146__clock_8h.md#a381f2ad32adfa495e9020788f5211aee)#define NXP\_S32\_LPI2C0\_CLK 71U

[ 79](nxp__s32k146__clock_8h.md#ab0729e1981aeddcc88a0acf65bb51cdf)#define NXP\_S32\_LPIT0\_CLK 72U

[ 80](nxp__s32k146__clock_8h.md#a3c5548bea0bf573ee5c34064ccc5eb5f)#define NXP\_S32\_LPSPI0\_CLK 73U

[ 81](nxp__s32k146__clock_8h.md#a0d581a4df52c36546fe58e947d6b62ae)#define NXP\_S32\_LPSPI1\_CLK 74U

[ 82](nxp__s32k146__clock_8h.md#a8ae234050a66b6857bf34769d485c7e4)#define NXP\_S32\_LPSPI2\_CLK 75U

[ 83](nxp__s32k146__clock_8h.md#ac68d091023dccc7b22cef29e3edc4222)#define NXP\_S32\_LPTMR0\_CLK 76U

[ 84](nxp__s32k146__clock_8h.md#a49beda273937c66398354636595e7d1c)#define NXP\_S32\_LPUART0\_CLK 77U

[ 85](nxp__s32k146__clock_8h.md#af5ca4a56001a2e39ed143adbd15d2219)#define NXP\_S32\_LPUART1\_CLK 78U

[ 86](nxp__s32k146__clock_8h.md#ad9303a366af8d2e1b160bf82adc894fe)#define NXP\_S32\_LPUART2\_CLK 79U

[ 87](nxp__s32k146__clock_8h.md#a28473957dcf8e30cbbaaf7ae060edecd)#define NXP\_S32\_MPU0\_CLK 80U

[ 88](nxp__s32k146__clock_8h.md#ae9c200098d78626d7aded5c5ec3e4b42)#define NXP\_S32\_MSCM0\_CLK 81U

[ 89](nxp__s32k146__clock_8h.md#a0867a69871810e808c0db344eecdf195)#define NXP\_S32\_PDB0\_CLK 82U

[ 90](nxp__s32k146__clock_8h.md#aee318a638ded5f5cd6b3532c70fb63e0)#define NXP\_S32\_PDB1\_CLK 83U

[ 91](nxp__s32k146__clock_8h.md#ad58e205cab52e5a52034e9803a4035c6)#define NXP\_S32\_PORTA\_CLK 84U

[ 92](nxp__s32k146__clock_8h.md#a3a28efb4509dc2c948117e0a22f28d54)#define NXP\_S32\_PORTB\_CLK 85U

[ 93](nxp__s32k146__clock_8h.md#a6256c89a46979b8cadfcb8bc498e7031)#define NXP\_S32\_PORTC\_CLK 86U

[ 94](nxp__s32k146__clock_8h.md#a48a3606ca8fbe5ad6450c91bb5479581)#define NXP\_S32\_PORTD\_CLK 87U

[ 95](nxp__s32k146__clock_8h.md#abab81e2ff3a6bb642dc61ca7f7b09f37)#define NXP\_S32\_PORTE\_CLK 88U

[ 96](nxp__s32k146__clock_8h.md#ae883db6b1e83c7e5f43004c38a496b58)#define NXP\_S32\_RTC0\_CLK 89U

[ 97](nxp__s32k146__clock_8h.md#a6a6963b78096148b569b9e07cf82faaf)#define NXP\_S32\_TRACE\_CLK 90U

98

99#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NXP\_S32K146\_CLOCK\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [nxp\_s32k146\_clock.h](nxp__s32k146__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
