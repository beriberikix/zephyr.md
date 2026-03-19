---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp__s32k146__clock_8h.html
original_path: doxygen/html/nxp__s32k146__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_s32k146\_clock.h File Reference

[Go to the source code of this file.](nxp__s32k146__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NXP\_S32\_LPO\_128K\_CLK](#ae5e10a14cc0f227d8c483d35c0df9cce)   1U |
| #define | [NXP\_S32\_SIRC\_CLK](#adc1da7bf433a80a3a975e172a30abbbc)   2U |
| #define | [NXP\_S32\_SIRC\_VLP\_CLK](#a7f7b85f65139224474cb6c3e867fe879)   3U |
| #define | [NXP\_S32\_SIRC\_STOP\_CLK](#a04e02db4c5466214e76b8323634a01a6)   4U |
| #define | [NXP\_S32\_FIRC\_CLK](#a8f4673a159fb26c90ae29761784395e9)   5U |
| #define | [NXP\_S32\_FIRC\_VLP\_CLK](#ada989b740d4d8f5c111fce02943b835c)   6U |
| #define | [NXP\_S32\_FIRC\_STOP\_CLK](#a688524357cead34820bc0122325b3e15)   7U |
| #define | [NXP\_S32\_SOSC\_CLK](#a49b53fcd4cf55c8a24b1670119392e24)   8U |
| #define | [NXP\_S32\_SPLL\_CLK](#a401c77f822de9ac078f1629cafb24a34)   9U |
| #define | [NXP\_S32\_SIRCDIV1\_CLK](#a1637b000e817e50ef4fd8c55b2327e1f)   10U |
| #define | [NXP\_S32\_SIRCDIV2\_CLK](#a670ed7e0f1b37ff5c6a33fee3fcee1fe)   11U |
| #define | [NXP\_S32\_FIRCDIV1\_CLK](#a5bbe7c5b5b576dc21dafdc4a9c16d83c)   12U |
| #define | [NXP\_S32\_FIRCDIV2\_CLK](#aa15bbe9eff8a09df5dda01324d1b0be9)   13U |
| #define | [NXP\_S32\_SOSCDIV1\_CLK](#a6764ee23b79692bffb464be0e4cd0a02)   14U |
| #define | [NXP\_S32\_SOSCDIV2\_CLK](#aa2371431504707419466f3392444e72e)   15U |
| #define | [NXP\_S32\_SPLLDIV1\_CLK](#aeae9584a1ba85fe28178748e0ded825f)   16U |
| #define | [NXP\_S32\_SPLLDIV2\_CLK](#ab553d243097da1d22834c00c743ac829)   17U |
| #define | [NXP\_S32\_LPO\_32K\_CLK](#a11db7a17fe6729120064ff68491aa99d)   18U |
| #define | [NXP\_S32\_LPO\_1K\_CLK](#a4b9330443edbddcaaf60595755888684)   19U |
| #define | [NXP\_S32\_TCLK0\_REF\_CLK](#a8c800a6a41f9a8d7463b44609bfc7b66)   20U |
| #define | [NXP\_S32\_TCLK1\_REF\_CLK](#aae61abdec779b428797e8b4dda8451a2)   21U |
| #define | [NXP\_S32\_TCLK2\_REF\_CLK](#a019249c31141a74cad5be9f68dde34b0)   22U |
| #define | [NXP\_S32\_SCS\_CLK](#a8839149b54e955dd82ffcd7d3165672f)   24U |
| #define | [NXP\_S32\_SCS\_RUN\_CLK](#a6b103eabec7835b65bb5f251d878b9eb)   25U |
| #define | [NXP\_S32\_SCS\_VLPR\_CLK](#ac55701d09adc15b66c4da17d89eb6e35)   26U |
| #define | [NXP\_S32\_SCS\_HSRUN\_CLK](#ab2fa7b71b2deed99ecb864574544b662)   27U |
| #define | [NXP\_S32\_CORE\_CLK](#a3addb6ad5d596e0b9739f34f00bc4ffc)   28U |
| #define | [NXP\_S32\_CORE\_RUN\_CLK](#aa11f09f442efee9a866297c81c8f284d)   29U |
| #define | [NXP\_S32\_CORE\_VLPR\_CLK](#adfc9b5f87de0f3588a42dd8867fa4d98)   30U |
| #define | [NXP\_S32\_CORE\_HSRUN\_CLK](#aaa0f0bdb41447451e575d5a72b4b0667)   31U |
| #define | [NXP\_S32\_BUS\_CLK](#aa53d8f3a4fed316c4b15f3d3470138ff)   32U |
| #define | [NXP\_S32\_BUS\_RUN\_CLK](#a33179b814af0974e3ee0e7deabb11b0b)   33U |
| #define | [NXP\_S32\_BUS\_VLPR\_CLK](#a816af3949d0ac497958447f70875eb6a)   34U |
| #define | [NXP\_S32\_BUS\_HSRUN\_CLK](#af04697ed35e63758f3cd51efa5aeeaea)   35U |
| #define | [NXP\_S32\_SLOW\_CLK](#ad6114a16219057fbc761de1254e8f0ed)   36U |
| #define | [NXP\_S32\_SLOW\_RUN\_CLK](#aa36a38d3a3a44cc3d96ce8da5edac484)   37U |
| #define | [NXP\_S32\_SLOW\_VLPR\_CLK](#a6382c0637bc32b870697c2cc0ac5b49d)   38U |
| #define | [NXP\_S32\_SLOW\_HSRUN\_CLK](#a2a615264b242a9115bc4b32b87cbf9bc)   39U |
| #define | [NXP\_S32\_RTC\_CLK](#a1ca20b16f6a430cddd8fc1d55fd7a840)   40U |
| #define | [NXP\_S32\_LPO\_CLK](#a2dca83f3da5ff6336bc65c0d55dfb980)   41U |
| #define | [NXP\_S32\_SCG\_CLKOUT\_CLK](#ad44809519c492290877741346f046f9f)   42U |
| #define | [NXP\_S32\_FTM0\_EXT\_CLK](#addc3582ba7517f6dea0ab5f8727c15de)   43U |
| #define | [NXP\_S32\_FTM1\_EXT\_CLK](#abae06e872b9f9b3926c49b1fdce854e1)   44U |
| #define | [NXP\_S32\_FTM2\_EXT\_CLK](#aefe843e849c2b0fb998e6725b040e566)   45U |
| #define | [NXP\_S32\_FTM3\_EXT\_CLK](#af674e053817be8fcaf9f959ea8ef7ba5)   46U |
| #define | [NXP\_S32\_FTM4\_EXT\_CLK](#a2fee6db6612f63f7ae2a0f12dba1fbdd)   47U |
| #define | [NXP\_S32\_FTM5\_EXT\_CLK](#aeca299c818cb5576d578daf8f8872bb7)   48U |
| #define | [NXP\_S32\_ADC0\_CLK](#a89fe6bb1365a3895449da72ccd517223)   50U |
| #define | [NXP\_S32\_ADC1\_CLK](#ace9575b4ed012fe344884b0b1fa2ef58)   51U |
| #define | [NXP\_S32\_CLKOUT0\_CLK](#a63aca9fbcdae28cd448e62e9dcf41da9)   52U |
| #define | [NXP\_S32\_CMP0\_CLK](#a44f6895b60c611c68da8d9674af0d474)   53U |
| #define | [NXP\_S32\_CRC0\_CLK](#a236cf04ea860d48a382096caea32d2b1)   54U |
| #define | [NXP\_S32\_DMA0\_CLK](#ad5b14f1c8c328d8293003cb0874523d7)   55U |
| #define | [NXP\_S32\_DMAMUX0\_CLK](#a97a3ff5238f4878784ee1bee4cfc7522)   56U |
| #define | [NXP\_S32\_EIM0\_CLK](#a73fd9c7c0b123b0b434097cce57b9b61)   57U |
| #define | [NXP\_S32\_ERM0\_CLK](#a5330dac04dd7c5b914f65920731472fd)   58U |
| #define | [NXP\_S32\_EWM0\_CLK](#adcb4cd2738c435bbd12ec0eb2de405b1)   59U |
| #define | [NXP\_S32\_FLEXCAN0\_CLK](#a308e74a366725070c56a4ab4fc7c300a)   60U |
| #define | [NXP\_S32\_FLEXCAN1\_CLK](#ad353c07d914cfa8c45ed3b7b586c2b00)   61U |
| #define | [NXP\_S32\_FLEXCAN2\_CLK](#a54467688a58d9be77849eddd031f126e)   62U |
| #define | [NXP\_S32\_FLEXIO\_CLK](#a0b7d5641dd840045a5c5c5dfc5642edf)   63U |
| #define | [NXP\_S32\_FTFC\_CLK](#af20dda1efa2e59c3665a7e2cb77022d1)   64U |
| #define | [NXP\_S32\_FTM0\_CLK](#a1fea1f63010c7e40e29c01ec795f7b3d)   65U |
| #define | [NXP\_S32\_FTM1\_CLK](#a008543228f51354a67e4ad973cb40391)   66U |
| #define | [NXP\_S32\_FTM2\_CLK](#abb38c0a85aa9d2e9cd4a3aa932dfd0c6)   67U |
| #define | [NXP\_S32\_FTM3\_CLK](#ac4151cc371cc1c0586e9ec0e47f17825)   68U |
| #define | [NXP\_S32\_FTM4\_CLK](#a05b9cef1f4544c696cd2513aa0430b89)   69U |
| #define | [NXP\_S32\_FTM5\_CLK](#a3909ae4f1d7951765436349272757f03)   70U |
| #define | [NXP\_S32\_LPI2C0\_CLK](#a381f2ad32adfa495e9020788f5211aee)   71U |
| #define | [NXP\_S32\_LPIT0\_CLK](#ab0729e1981aeddcc88a0acf65bb51cdf)   72U |
| #define | [NXP\_S32\_LPSPI0\_CLK](#a3c5548bea0bf573ee5c34064ccc5eb5f)   73U |
| #define | [NXP\_S32\_LPSPI1\_CLK](#a0d581a4df52c36546fe58e947d6b62ae)   74U |
| #define | [NXP\_S32\_LPSPI2\_CLK](#a8ae234050a66b6857bf34769d485c7e4)   75U |
| #define | [NXP\_S32\_LPTMR0\_CLK](#ac68d091023dccc7b22cef29e3edc4222)   76U |
| #define | [NXP\_S32\_LPUART0\_CLK](#a49beda273937c66398354636595e7d1c)   77U |
| #define | [NXP\_S32\_LPUART1\_CLK](#af5ca4a56001a2e39ed143adbd15d2219)   78U |
| #define | [NXP\_S32\_LPUART2\_CLK](#ad9303a366af8d2e1b160bf82adc894fe)   79U |
| #define | [NXP\_S32\_MPU0\_CLK](#a28473957dcf8e30cbbaaf7ae060edecd)   80U |
| #define | [NXP\_S32\_MSCM0\_CLK](#ae9c200098d78626d7aded5c5ec3e4b42)   81U |
| #define | [NXP\_S32\_PDB0\_CLK](#a0867a69871810e808c0db344eecdf195)   82U |
| #define | [NXP\_S32\_PDB1\_CLK](#aee318a638ded5f5cd6b3532c70fb63e0)   83U |
| #define | [NXP\_S32\_PORTA\_CLK](#ad58e205cab52e5a52034e9803a4035c6)   84U |
| #define | [NXP\_S32\_PORTB\_CLK](#a3a28efb4509dc2c948117e0a22f28d54)   85U |
| #define | [NXP\_S32\_PORTC\_CLK](#a6256c89a46979b8cadfcb8bc498e7031)   86U |
| #define | [NXP\_S32\_PORTD\_CLK](#a48a3606ca8fbe5ad6450c91bb5479581)   87U |
| #define | [NXP\_S32\_PORTE\_CLK](#abab81e2ff3a6bb642dc61ca7f7b09f37)   88U |
| #define | [NXP\_S32\_RTC0\_CLK](#ae883db6b1e83c7e5f43004c38a496b58)   89U |
| #define | [NXP\_S32\_TRACE\_CLK](#a6a6963b78096148b569b9e07cf82faaf)   90U |

## Macro Definition Documentation

## [◆ ](#a89fe6bb1365a3895449da72ccd517223)NXP\_S32\_ADC0\_CLK

| #define NXP\_S32\_ADC0\_CLK   50U |
| --- |

## [◆ ](#ace9575b4ed012fe344884b0b1fa2ef58)NXP\_S32\_ADC1\_CLK

| #define NXP\_S32\_ADC1\_CLK   51U |
| --- |

## [◆ ](#aa53d8f3a4fed316c4b15f3d3470138ff)NXP\_S32\_BUS\_CLK

| #define NXP\_S32\_BUS\_CLK   32U |
| --- |

## [◆ ](#af04697ed35e63758f3cd51efa5aeeaea)NXP\_S32\_BUS\_HSRUN\_CLK

| #define NXP\_S32\_BUS\_HSRUN\_CLK   35U |
| --- |

## [◆ ](#a33179b814af0974e3ee0e7deabb11b0b)NXP\_S32\_BUS\_RUN\_CLK

| #define NXP\_S32\_BUS\_RUN\_CLK   33U |
| --- |

## [◆ ](#a816af3949d0ac497958447f70875eb6a)NXP\_S32\_BUS\_VLPR\_CLK

| #define NXP\_S32\_BUS\_VLPR\_CLK   34U |
| --- |

## [◆ ](#a63aca9fbcdae28cd448e62e9dcf41da9)NXP\_S32\_CLKOUT0\_CLK

| #define NXP\_S32\_CLKOUT0\_CLK   52U |
| --- |

## [◆ ](#a44f6895b60c611c68da8d9674af0d474)NXP\_S32\_CMP0\_CLK

| #define NXP\_S32\_CMP0\_CLK   53U |
| --- |

## [◆ ](#a3addb6ad5d596e0b9739f34f00bc4ffc)NXP\_S32\_CORE\_CLK

| #define NXP\_S32\_CORE\_CLK   28U |
| --- |

## [◆ ](#aaa0f0bdb41447451e575d5a72b4b0667)NXP\_S32\_CORE\_HSRUN\_CLK

| #define NXP\_S32\_CORE\_HSRUN\_CLK   31U |
| --- |

## [◆ ](#aa11f09f442efee9a866297c81c8f284d)NXP\_S32\_CORE\_RUN\_CLK

| #define NXP\_S32\_CORE\_RUN\_CLK   29U |
| --- |

## [◆ ](#adfc9b5f87de0f3588a42dd8867fa4d98)NXP\_S32\_CORE\_VLPR\_CLK

| #define NXP\_S32\_CORE\_VLPR\_CLK   30U |
| --- |

## [◆ ](#a236cf04ea860d48a382096caea32d2b1)NXP\_S32\_CRC0\_CLK

| #define NXP\_S32\_CRC0\_CLK   54U |
| --- |

## [◆ ](#ad5b14f1c8c328d8293003cb0874523d7)NXP\_S32\_DMA0\_CLK

| #define NXP\_S32\_DMA0\_CLK   55U |
| --- |

## [◆ ](#a97a3ff5238f4878784ee1bee4cfc7522)NXP\_S32\_DMAMUX0\_CLK

| #define NXP\_S32\_DMAMUX0\_CLK   56U |
| --- |

## [◆ ](#a73fd9c7c0b123b0b434097cce57b9b61)NXP\_S32\_EIM0\_CLK

| #define NXP\_S32\_EIM0\_CLK   57U |
| --- |

## [◆ ](#a5330dac04dd7c5b914f65920731472fd)NXP\_S32\_ERM0\_CLK

| #define NXP\_S32\_ERM0\_CLK   58U |
| --- |

## [◆ ](#adcb4cd2738c435bbd12ec0eb2de405b1)NXP\_S32\_EWM0\_CLK

| #define NXP\_S32\_EWM0\_CLK   59U |
| --- |

## [◆ ](#a8f4673a159fb26c90ae29761784395e9)NXP\_S32\_FIRC\_CLK

| #define NXP\_S32\_FIRC\_CLK   5U |
| --- |

## [◆ ](#a688524357cead34820bc0122325b3e15)NXP\_S32\_FIRC\_STOP\_CLK

| #define NXP\_S32\_FIRC\_STOP\_CLK   7U |
| --- |

## [◆ ](#ada989b740d4d8f5c111fce02943b835c)NXP\_S32\_FIRC\_VLP\_CLK

| #define NXP\_S32\_FIRC\_VLP\_CLK   6U |
| --- |

## [◆ ](#a5bbe7c5b5b576dc21dafdc4a9c16d83c)NXP\_S32\_FIRCDIV1\_CLK

| #define NXP\_S32\_FIRCDIV1\_CLK   12U |
| --- |

## [◆ ](#aa15bbe9eff8a09df5dda01324d1b0be9)NXP\_S32\_FIRCDIV2\_CLK

| #define NXP\_S32\_FIRCDIV2\_CLK   13U |
| --- |

## [◆ ](#a308e74a366725070c56a4ab4fc7c300a)NXP\_S32\_FLEXCAN0\_CLK

| #define NXP\_S32\_FLEXCAN0\_CLK   60U |
| --- |

## [◆ ](#ad353c07d914cfa8c45ed3b7b586c2b00)NXP\_S32\_FLEXCAN1\_CLK

| #define NXP\_S32\_FLEXCAN1\_CLK   61U |
| --- |

## [◆ ](#a54467688a58d9be77849eddd031f126e)NXP\_S32\_FLEXCAN2\_CLK

| #define NXP\_S32\_FLEXCAN2\_CLK   62U |
| --- |

## [◆ ](#a0b7d5641dd840045a5c5c5dfc5642edf)NXP\_S32\_FLEXIO\_CLK

| #define NXP\_S32\_FLEXIO\_CLK   63U |
| --- |

## [◆ ](#af20dda1efa2e59c3665a7e2cb77022d1)NXP\_S32\_FTFC\_CLK

| #define NXP\_S32\_FTFC\_CLK   64U |
| --- |

## [◆ ](#a1fea1f63010c7e40e29c01ec795f7b3d)NXP\_S32\_FTM0\_CLK

| #define NXP\_S32\_FTM0\_CLK   65U |
| --- |

## [◆ ](#addc3582ba7517f6dea0ab5f8727c15de)NXP\_S32\_FTM0\_EXT\_CLK

| #define NXP\_S32\_FTM0\_EXT\_CLK   43U |
| --- |

## [◆ ](#a008543228f51354a67e4ad973cb40391)NXP\_S32\_FTM1\_CLK

| #define NXP\_S32\_FTM1\_CLK   66U |
| --- |

## [◆ ](#abae06e872b9f9b3926c49b1fdce854e1)NXP\_S32\_FTM1\_EXT\_CLK

| #define NXP\_S32\_FTM1\_EXT\_CLK   44U |
| --- |

## [◆ ](#abb38c0a85aa9d2e9cd4a3aa932dfd0c6)NXP\_S32\_FTM2\_CLK

| #define NXP\_S32\_FTM2\_CLK   67U |
| --- |

## [◆ ](#aefe843e849c2b0fb998e6725b040e566)NXP\_S32\_FTM2\_EXT\_CLK

| #define NXP\_S32\_FTM2\_EXT\_CLK   45U |
| --- |

## [◆ ](#ac4151cc371cc1c0586e9ec0e47f17825)NXP\_S32\_FTM3\_CLK

| #define NXP\_S32\_FTM3\_CLK   68U |
| --- |

## [◆ ](#af674e053817be8fcaf9f959ea8ef7ba5)NXP\_S32\_FTM3\_EXT\_CLK

| #define NXP\_S32\_FTM3\_EXT\_CLK   46U |
| --- |

## [◆ ](#a05b9cef1f4544c696cd2513aa0430b89)NXP\_S32\_FTM4\_CLK

| #define NXP\_S32\_FTM4\_CLK   69U |
| --- |

## [◆ ](#a2fee6db6612f63f7ae2a0f12dba1fbdd)NXP\_S32\_FTM4\_EXT\_CLK

| #define NXP\_S32\_FTM4\_EXT\_CLK   47U |
| --- |

## [◆ ](#a3909ae4f1d7951765436349272757f03)NXP\_S32\_FTM5\_CLK

| #define NXP\_S32\_FTM5\_CLK   70U |
| --- |

## [◆ ](#aeca299c818cb5576d578daf8f8872bb7)NXP\_S32\_FTM5\_EXT\_CLK

| #define NXP\_S32\_FTM5\_EXT\_CLK   48U |
| --- |

## [◆ ](#a381f2ad32adfa495e9020788f5211aee)NXP\_S32\_LPI2C0\_CLK

| #define NXP\_S32\_LPI2C0\_CLK   71U |
| --- |

## [◆ ](#ab0729e1981aeddcc88a0acf65bb51cdf)NXP\_S32\_LPIT0\_CLK

| #define NXP\_S32\_LPIT0\_CLK   72U |
| --- |

## [◆ ](#ae5e10a14cc0f227d8c483d35c0df9cce)NXP\_S32\_LPO\_128K\_CLK

| #define NXP\_S32\_LPO\_128K\_CLK   1U |
| --- |

## [◆ ](#a4b9330443edbddcaaf60595755888684)NXP\_S32\_LPO\_1K\_CLK

| #define NXP\_S32\_LPO\_1K\_CLK   19U |
| --- |

## [◆ ](#a11db7a17fe6729120064ff68491aa99d)NXP\_S32\_LPO\_32K\_CLK

| #define NXP\_S32\_LPO\_32K\_CLK   18U |
| --- |

## [◆ ](#a2dca83f3da5ff6336bc65c0d55dfb980)NXP\_S32\_LPO\_CLK

| #define NXP\_S32\_LPO\_CLK   41U |
| --- |

## [◆ ](#a3c5548bea0bf573ee5c34064ccc5eb5f)NXP\_S32\_LPSPI0\_CLK

| #define NXP\_S32\_LPSPI0\_CLK   73U |
| --- |

## [◆ ](#a0d581a4df52c36546fe58e947d6b62ae)NXP\_S32\_LPSPI1\_CLK

| #define NXP\_S32\_LPSPI1\_CLK   74U |
| --- |

## [◆ ](#a8ae234050a66b6857bf34769d485c7e4)NXP\_S32\_LPSPI2\_CLK

| #define NXP\_S32\_LPSPI2\_CLK   75U |
| --- |

## [◆ ](#ac68d091023dccc7b22cef29e3edc4222)NXP\_S32\_LPTMR0\_CLK

| #define NXP\_S32\_LPTMR0\_CLK   76U |
| --- |

## [◆ ](#a49beda273937c66398354636595e7d1c)NXP\_S32\_LPUART0\_CLK

| #define NXP\_S32\_LPUART0\_CLK   77U |
| --- |

## [◆ ](#af5ca4a56001a2e39ed143adbd15d2219)NXP\_S32\_LPUART1\_CLK

| #define NXP\_S32\_LPUART1\_CLK   78U |
| --- |

## [◆ ](#ad9303a366af8d2e1b160bf82adc894fe)NXP\_S32\_LPUART2\_CLK

| #define NXP\_S32\_LPUART2\_CLK   79U |
| --- |

## [◆ ](#a28473957dcf8e30cbbaaf7ae060edecd)NXP\_S32\_MPU0\_CLK

| #define NXP\_S32\_MPU0\_CLK   80U |
| --- |

## [◆ ](#ae9c200098d78626d7aded5c5ec3e4b42)NXP\_S32\_MSCM0\_CLK

| #define NXP\_S32\_MSCM0\_CLK   81U |
| --- |

## [◆ ](#a0867a69871810e808c0db344eecdf195)NXP\_S32\_PDB0\_CLK

| #define NXP\_S32\_PDB0\_CLK   82U |
| --- |

## [◆ ](#aee318a638ded5f5cd6b3532c70fb63e0)NXP\_S32\_PDB1\_CLK

| #define NXP\_S32\_PDB1\_CLK   83U |
| --- |

## [◆ ](#ad58e205cab52e5a52034e9803a4035c6)NXP\_S32\_PORTA\_CLK

| #define NXP\_S32\_PORTA\_CLK   84U |
| --- |

## [◆ ](#a3a28efb4509dc2c948117e0a22f28d54)NXP\_S32\_PORTB\_CLK

| #define NXP\_S32\_PORTB\_CLK   85U |
| --- |

## [◆ ](#a6256c89a46979b8cadfcb8bc498e7031)NXP\_S32\_PORTC\_CLK

| #define NXP\_S32\_PORTC\_CLK   86U |
| --- |

## [◆ ](#a48a3606ca8fbe5ad6450c91bb5479581)NXP\_S32\_PORTD\_CLK

| #define NXP\_S32\_PORTD\_CLK   87U |
| --- |

## [◆ ](#abab81e2ff3a6bb642dc61ca7f7b09f37)NXP\_S32\_PORTE\_CLK

| #define NXP\_S32\_PORTE\_CLK   88U |
| --- |

## [◆ ](#ae883db6b1e83c7e5f43004c38a496b58)NXP\_S32\_RTC0\_CLK

| #define NXP\_S32\_RTC0\_CLK   89U |
| --- |

## [◆ ](#a1ca20b16f6a430cddd8fc1d55fd7a840)NXP\_S32\_RTC\_CLK

| #define NXP\_S32\_RTC\_CLK   40U |
| --- |

## [◆ ](#ad44809519c492290877741346f046f9f)NXP\_S32\_SCG\_CLKOUT\_CLK

| #define NXP\_S32\_SCG\_CLKOUT\_CLK   42U |
| --- |

## [◆ ](#a8839149b54e955dd82ffcd7d3165672f)NXP\_S32\_SCS\_CLK

| #define NXP\_S32\_SCS\_CLK   24U |
| --- |

## [◆ ](#ab2fa7b71b2deed99ecb864574544b662)NXP\_S32\_SCS\_HSRUN\_CLK

| #define NXP\_S32\_SCS\_HSRUN\_CLK   27U |
| --- |

## [◆ ](#a6b103eabec7835b65bb5f251d878b9eb)NXP\_S32\_SCS\_RUN\_CLK

| #define NXP\_S32\_SCS\_RUN\_CLK   25U |
| --- |

## [◆ ](#ac55701d09adc15b66c4da17d89eb6e35)NXP\_S32\_SCS\_VLPR\_CLK

| #define NXP\_S32\_SCS\_VLPR\_CLK   26U |
| --- |

## [◆ ](#adc1da7bf433a80a3a975e172a30abbbc)NXP\_S32\_SIRC\_CLK

| #define NXP\_S32\_SIRC\_CLK   2U |
| --- |

## [◆ ](#a04e02db4c5466214e76b8323634a01a6)NXP\_S32\_SIRC\_STOP\_CLK

| #define NXP\_S32\_SIRC\_STOP\_CLK   4U |
| --- |

## [◆ ](#a7f7b85f65139224474cb6c3e867fe879)NXP\_S32\_SIRC\_VLP\_CLK

| #define NXP\_S32\_SIRC\_VLP\_CLK   3U |
| --- |

## [◆ ](#a1637b000e817e50ef4fd8c55b2327e1f)NXP\_S32\_SIRCDIV1\_CLK

| #define NXP\_S32\_SIRCDIV1\_CLK   10U |
| --- |

## [◆ ](#a670ed7e0f1b37ff5c6a33fee3fcee1fe)NXP\_S32\_SIRCDIV2\_CLK

| #define NXP\_S32\_SIRCDIV2\_CLK   11U |
| --- |

## [◆ ](#ad6114a16219057fbc761de1254e8f0ed)NXP\_S32\_SLOW\_CLK

| #define NXP\_S32\_SLOW\_CLK   36U |
| --- |

## [◆ ](#a2a615264b242a9115bc4b32b87cbf9bc)NXP\_S32\_SLOW\_HSRUN\_CLK

| #define NXP\_S32\_SLOW\_HSRUN\_CLK   39U |
| --- |

## [◆ ](#aa36a38d3a3a44cc3d96ce8da5edac484)NXP\_S32\_SLOW\_RUN\_CLK

| #define NXP\_S32\_SLOW\_RUN\_CLK   37U |
| --- |

## [◆ ](#a6382c0637bc32b870697c2cc0ac5b49d)NXP\_S32\_SLOW\_VLPR\_CLK

| #define NXP\_S32\_SLOW\_VLPR\_CLK   38U |
| --- |

## [◆ ](#a49b53fcd4cf55c8a24b1670119392e24)NXP\_S32\_SOSC\_CLK

| #define NXP\_S32\_SOSC\_CLK   8U |
| --- |

## [◆ ](#a6764ee23b79692bffb464be0e4cd0a02)NXP\_S32\_SOSCDIV1\_CLK

| #define NXP\_S32\_SOSCDIV1\_CLK   14U |
| --- |

## [◆ ](#aa2371431504707419466f3392444e72e)NXP\_S32\_SOSCDIV2\_CLK

| #define NXP\_S32\_SOSCDIV2\_CLK   15U |
| --- |

## [◆ ](#a401c77f822de9ac078f1629cafb24a34)NXP\_S32\_SPLL\_CLK

| #define NXP\_S32\_SPLL\_CLK   9U |
| --- |

## [◆ ](#aeae9584a1ba85fe28178748e0ded825f)NXP\_S32\_SPLLDIV1\_CLK

| #define NXP\_S32\_SPLLDIV1\_CLK   16U |
| --- |

## [◆ ](#ab553d243097da1d22834c00c743ac829)NXP\_S32\_SPLLDIV2\_CLK

| #define NXP\_S32\_SPLLDIV2\_CLK   17U |
| --- |

## [◆ ](#a8c800a6a41f9a8d7463b44609bfc7b66)NXP\_S32\_TCLK0\_REF\_CLK

| #define NXP\_S32\_TCLK0\_REF\_CLK   20U |
| --- |

## [◆ ](#aae61abdec779b428797e8b4dda8451a2)NXP\_S32\_TCLK1\_REF\_CLK

| #define NXP\_S32\_TCLK1\_REF\_CLK   21U |
| --- |

## [◆ ](#a019249c31141a74cad5be9f68dde34b0)NXP\_S32\_TCLK2\_REF\_CLK

| #define NXP\_S32\_TCLK2\_REF\_CLK   22U |
| --- |

## [◆ ](#a6a6963b78096148b569b9e07cf82faaf)NXP\_S32\_TRACE\_CLK

| #define NXP\_S32\_TRACE\_CLK   90U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [nxp\_s32k146\_clock.h](nxp__s32k146__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
