---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/numaker__m55m1x__reset_8h_source.html
original_path: doxygen/html/numaker__m55m1x__reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numaker\_m55m1x\_reset.h

[Go to the documentation of this file.](numaker__m55m1x__reset_8h.md)

1/\*

2 \* Copyright (c) 2025 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_NUMAKER\_M55M1X\_RESET\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_NUMAKER\_M55M1X\_RESET\_H

9

10/\* Beginning of M55M1 BSP sys\_reg.h reset module copy \*/

11

[ 12](numaker__m55m1x__reset_8h.md#ab1a685bdef3c4e5cf4327378adb5737d)#define SYS\_RSTCTL\_CHIPRST\_Pos 0

[ 13](numaker__m55m1x__reset_8h.md#a1972f4ed665ff92a72a0566bd7125210)#define SYS\_RSTCTL\_NPURST\_Pos 6

[ 14](numaker__m55m1x__reset_8h.md#a36614300b2f69d972df9565173dd86eb)#define SYS\_ACMPRST\_ACMP01RST\_Pos 0

[ 15](numaker__m55m1x__reset_8h.md#a3d61d720f617e643f1a5f7079dfc76c6)#define SYS\_ACMPRST\_ACMP23RST\_Pos 1

[ 16](numaker__m55m1x__reset_8h.md#a760764e2b514e1876484e2148c3bd331)#define SYS\_AWFRST\_AWF0RST\_Pos 0

[ 17](numaker__m55m1x__reset_8h.md#a4caa0c3f290a946db23f70d9b80fb910)#define SYS\_BPWMRST\_BPWM0RST\_Pos 0

[ 18](numaker__m55m1x__reset_8h.md#ad32601470a8f84870d57c39107e0865a)#define SYS\_BPWMRST\_BPWM1RST\_Pos 1

[ 19](numaker__m55m1x__reset_8h.md#a260364dbed1e2a97a97810bc3cc837ce)#define SYS\_CANFDRST\_CANFD0RST\_Pos 0

[ 20](numaker__m55m1x__reset_8h.md#a507cd169914f0b69118fc016a6e5c42b)#define SYS\_CANFDRST\_CANFD1RST\_Pos 1

[ 21](numaker__m55m1x__reset_8h.md#a2cbd88aca74b261df6c1a67ef7a6f3c3)#define SYS\_CCAPRST\_CCAP0RST\_Pos 0

[ 22](numaker__m55m1x__reset_8h.md#a537c57906402650a38f16f6b80e39159)#define SYS\_CRCRST\_CRC0RST\_Pos 0

[ 23](numaker__m55m1x__reset_8h.md#a7c8108d9b3bdad2ba8ae6e828f453ec7)#define SYS\_CRYPTORST\_CRYPTO0RST\_Pos 0

[ 24](numaker__m55m1x__reset_8h.md#a2ae3938b2eed93c64b6050a8a05af94f)#define SYS\_DACRST\_DAC01RST\_Pos 0

[ 25](numaker__m55m1x__reset_8h.md#a5156a4e3f87c8a94399538cc241a9ce5)#define SYS\_DMICRST\_DMIC0RST\_Pos 0

[ 26](numaker__m55m1x__reset_8h.md#a3a1b16465cf075e0179cf07be4301b10)#define SYS\_EADCRST\_EADC0RST\_Pos 0

[ 27](numaker__m55m1x__reset_8h.md#a41627e562c99006a8a195746c57fe15e)#define SYS\_EBIRST\_EBI0RST\_Pos 0

[ 28](numaker__m55m1x__reset_8h.md#a8d3dd837315f3e54df889cb824e72b04)#define SYS\_ECAPRST\_ECAP0RST\_Pos 0

[ 29](numaker__m55m1x__reset_8h.md#aa2d7ba969247e520e7a572d3cf756464)#define SYS\_ECAPRST\_ECAP1RST\_Pos 1

[ 30](numaker__m55m1x__reset_8h.md#a3f166a02efd57f96f188632cb5c0326b)#define SYS\_ECAPRST\_ECAP2RST\_Pos 2

[ 31](numaker__m55m1x__reset_8h.md#a95eb5cb0d95024b4249f4045fd70caa9)#define SYS\_ECAPRST\_ECAP3RST\_Pos 3

[ 32](numaker__m55m1x__reset_8h.md#a52f7c19539146e9af27a0e84ceb3cb01)#define SYS\_EMACRST\_EMAC0RST\_Pos 0

[ 33](numaker__m55m1x__reset_8h.md#a54c684adb0e6531250b6d97699f52118)#define SYS\_EPWMRST\_EPWM0RST\_Pos 0

[ 34](numaker__m55m1x__reset_8h.md#ae8987d6b648c794923778c5dc35b884a)#define SYS\_EPWMRST\_EPWM1RST\_Pos 1

[ 35](numaker__m55m1x__reset_8h.md#a28b4919d1a65082e32f0c1c46158d2e3)#define SYS\_EQEIRST\_EQEI0RST\_Pos 0

[ 36](numaker__m55m1x__reset_8h.md#a87708ded049f7a9e9f4904bfdab860d5)#define SYS\_EQEIRST\_EQEI1RST\_Pos 1

[ 37](numaker__m55m1x__reset_8h.md#ac6f2edbd83266d852a5f6d62aa000cc0)#define SYS\_EQEIRST\_EQEI2RST\_Pos 2

[ 38](numaker__m55m1x__reset_8h.md#a01d04266f754a8d7deba6b72fa315d81)#define SYS\_EQEIRST\_EQEI3RST\_Pos 3

[ 39](numaker__m55m1x__reset_8h.md#a1cb506d98b12488785c8cad8584611dc)#define SYS\_FMCRST\_FMC0RST\_Pos 0

[ 40](numaker__m55m1x__reset_8h.md#a1eeb8a95d51b69e82e7dd66c3a4f18b6)#define SYS\_GDMARST\_GDMA0RST\_Pos 0

[ 41](numaker__m55m1x__reset_8h.md#af62ded9dcdbaa78c16b0a17f3295084f)#define SYS\_GPIORST\_GPIO0RST\_Pos 0

[ 42](numaker__m55m1x__reset_8h.md#a65250c346038357fc6447f3d785d137c)#define SYS\_HSOTGRST\_HSOTG0RST\_Pos 0

[ 43](numaker__m55m1x__reset_8h.md#a5fa9b4df09b9f1535f7f349c7f3cdf86)#define SYS\_HSUSBDRST\_HSUSBD0RST\_Pos 0

[ 44](numaker__m55m1x__reset_8h.md#a62b7898c564657b4d6e0017272916f7c)#define SYS\_HSUSBHRST\_HSUSBH0RST\_Pos 0

[ 45](numaker__m55m1x__reset_8h.md#a09a758385a0335509e01dcc5710383d8)#define SYS\_I2CRST\_I2C0RST\_Pos 0

[ 46](numaker__m55m1x__reset_8h.md#a3663016957565ee254929d54b387e8ad)#define SYS\_I2CRST\_I2C1RST\_Pos 1

[ 47](numaker__m55m1x__reset_8h.md#a04be7c6e99d5def61a05e6f7b440d6c3)#define SYS\_I2CRST\_I2C2RST\_Pos 2

[ 48](numaker__m55m1x__reset_8h.md#ac69aa84fcc3fccbb3918e589310b9075)#define SYS\_I2CRST\_I2C3RST\_Pos 3

[ 49](numaker__m55m1x__reset_8h.md#a2b0b2a9e78146a3cdadce7274c39ced5)#define SYS\_I2SRST\_I2S0RST\_Pos 0

[ 50](numaker__m55m1x__reset_8h.md#aec09db46dce2e882ab8e2859bf4ec248)#define SYS\_I2SRST\_I2S1RST\_Pos 1

[ 51](numaker__m55m1x__reset_8h.md#a2e479e909eb19f644108b2236116c86b)#define SYS\_I3CRST\_I3C0RST\_Pos 0

[ 52](numaker__m55m1x__reset_8h.md#aa2e813d1bae86d7cf6f2e9d2a2d3cb20)#define SYS\_KDFRST\_KDF0RST\_Pos 0

[ 53](numaker__m55m1x__reset_8h.md#a1e36dddf229abbff26aebdf4edd28950)#define SYS\_KPIRST\_KPI0RST\_Pos 0

[ 54](numaker__m55m1x__reset_8h.md#a5309877783f002f84aa66f839df5d8d9)#define SYS\_KSRST\_KS0RST\_Pos 0

[ 55](numaker__m55m1x__reset_8h.md#a29ad8a6c5bc15aa3da9ddf08ae6d9030)#define SYS\_LPADCRST\_LPADC0RST\_Pos 0

[ 56](numaker__m55m1x__reset_8h.md#a3a0d90d59372621bf300bf98f4e06505)#define SYS\_LPPDMARST\_LPPDMA0RST\_Pos 0

[ 57](numaker__m55m1x__reset_8h.md#a06cb8b332e821121023d821b6beba79a)#define SYS\_LPGPIORST\_LPGPIO0RST\_Pos 0

[ 58](numaker__m55m1x__reset_8h.md#aac272a45e4d23de235c84e6d0d284dfd)#define SYS\_LPI2CRST\_LPI2C0RST\_Pos 0

[ 59](numaker__m55m1x__reset_8h.md#ae2d1f6a7660c7a9b5dcee3032e10001c)#define SYS\_LPSPIRST\_LPSPI0RST\_Pos 0

[ 60](numaker__m55m1x__reset_8h.md#a42c0e506f593e38d31f61a52b3ddd15f)#define SYS\_LPTMRRST\_LPTMR0RST\_Pos 0

[ 61](numaker__m55m1x__reset_8h.md#a441782fe457c663faebf776625f1362e)#define SYS\_LPTMRRST\_LPTMR1RST\_Pos 1

[ 62](numaker__m55m1x__reset_8h.md#add63a360112fa344ec2ab4253df6404c)#define SYS\_LPUARTRST\_LPUART0RST\_Pos 0

[ 63](numaker__m55m1x__reset_8h.md#a0bfcec65941de79b637d35545f5d995d)#define SYS\_OTFCRST\_OTFC0RST\_Pos 0

[ 64](numaker__m55m1x__reset_8h.md#ade9d09c59368039ccb3817e8c959391d)#define SYS\_OTGRST\_OTG0RST\_Pos 0

[ 65](numaker__m55m1x__reset_8h.md#a0693c016c159ddbbe59d449a485431e9)#define SYS\_PDMARST\_PDMA0RST\_Pos 0

[ 66](numaker__m55m1x__reset_8h.md#aa578464df3a3ae8e31e0916a4c59e634)#define SYS\_PDMARST\_PDMA1RST\_Pos 1

[ 67](numaker__m55m1x__reset_8h.md#a07544808b8e6dce0eb4e9e982e5da5b0)#define SYS\_PSIORST\_PSIO0RST\_Pos 0

[ 68](numaker__m55m1x__reset_8h.md#ac13409d1fbf5f35fc692ef8720dcc5fe)#define SYS\_QSPIRST\_QSPI0RST\_Pos 0

[ 69](numaker__m55m1x__reset_8h.md#afa4bf068e8720e9fecc41fc9b1e81165)#define SYS\_QSPIRST\_QSPI1RST\_Pos 1

[ 70](numaker__m55m1x__reset_8h.md#a83568e5adda8737a41c9175ae860fc54)#define SYS\_RTCRST\_RTC0RST\_Pos 0

[ 71](numaker__m55m1x__reset_8h.md#a4b2b8c07e03476d3aaf6bbe31a72423c)#define SYS\_SCRST\_SC0RST\_Pos 0

[ 72](numaker__m55m1x__reset_8h.md#aab3ea5b1d05eb0dacb5b0b600eec45bb)#define SYS\_SCRST\_SC1RST\_Pos 1

[ 73](numaker__m55m1x__reset_8h.md#a11f445d2804a5fe32049c4665b68b257)#define SYS\_SCRST\_SC2RST\_Pos 2

[ 74](numaker__m55m1x__reset_8h.md#a30cdab2c7ee2b8fa640183d214754ffd)#define SYS\_SCURST\_SCU0RST\_Pos 0

[ 75](numaker__m55m1x__reset_8h.md#a0eedbcf30c580744e8dd7cdd54524d82)#define SYS\_SDHRST\_SDH0RST\_Pos 0

[ 76](numaker__m55m1x__reset_8h.md#ae96d41260fdb308cb88e23180c3c736b)#define SYS\_SDHRST\_SDH1RST\_Pos 1

[ 77](numaker__m55m1x__reset_8h.md#a8d2bb00e242ea780d86b0499883838f0)#define SYS\_SPIRST\_SPI0RST\_Pos 0

[ 78](numaker__m55m1x__reset_8h.md#ab6f953013a96a85bd1e527480e99b2eb)#define SYS\_SPIRST\_SPI1RST\_Pos 1

[ 79](numaker__m55m1x__reset_8h.md#a82ed6cc0052ce7880f5a19c385d935d2)#define SYS\_SPIRST\_SPI2RST\_Pos 2

[ 80](numaker__m55m1x__reset_8h.md#a76bbb162e93707d01d3dc9c60303ea3b)#define SYS\_SPIRST\_SPI3RST\_Pos 3

[ 81](numaker__m55m1x__reset_8h.md#ac88a3d4addd692cbe2c83184a0f322d7)#define SYS\_SPIMRST\_SPIM0RST\_Pos 0

[ 82](numaker__m55m1x__reset_8h.md#a85a5a04c531f16ec050a4ec4d4336c28)#define SYS\_TMRRST\_TMR0RST\_Pos 0

[ 83](numaker__m55m1x__reset_8h.md#aa1a89efd0953b3dcaa994b898ea624e1)#define SYS\_TMRRST\_TMR1RST\_Pos 1

[ 84](numaker__m55m1x__reset_8h.md#ad0a1cf910fb506dc83302ae03b5870a5)#define SYS\_TMRRST\_TMR2RST\_Pos 2

[ 85](numaker__m55m1x__reset_8h.md#a959b82db6a1420f13ca5a1139b5af2c2)#define SYS\_TMRRST\_TMR3RST\_Pos 3

[ 86](numaker__m55m1x__reset_8h.md#a51a346541e6458b4493205fe4945c78a)#define SYS\_TRNGRST\_TRNG0RST\_Pos 0

[ 87](numaker__m55m1x__reset_8h.md#a3e3b7bca8cfe63f45fc3dd2bf188a99a)#define SYS\_TTMRRST\_TTMR0RST\_Pos 0

[ 88](numaker__m55m1x__reset_8h.md#a4ee6877c3f4b8c7494acf55f95ae301d)#define SYS\_TTMRRST\_TTMR1RST\_Pos 1

[ 89](numaker__m55m1x__reset_8h.md#a81c856500be0fd1414e7780663585dfe)#define SYS\_UARTRST\_UART0RST\_Pos 0

[ 90](numaker__m55m1x__reset_8h.md#ac2460e49c97bc57a403a0682c9b2ae53)#define SYS\_UARTRST\_UART1RST\_Pos 1

[ 91](numaker__m55m1x__reset_8h.md#aaa051807990f9a008d91e63eb50a0d62)#define SYS\_UARTRST\_UART2RST\_Pos 2

[ 92](numaker__m55m1x__reset_8h.md#a13f04ef940da46d4fadbf4883cf8fd8a)#define SYS\_UARTRST\_UART3RST\_Pos 3

[ 93](numaker__m55m1x__reset_8h.md#ac0afb4b0c00421f4798f282cc315d025)#define SYS\_UARTRST\_UART4RST\_Pos 4

[ 94](numaker__m55m1x__reset_8h.md#a9b8d02b5a8f16f874ca9f5e5971642ff)#define SYS\_UARTRST\_UART5RST\_Pos 5

[ 95](numaker__m55m1x__reset_8h.md#a9c1528cdc603da543b9adfaef200ddc0)#define SYS\_UARTRST\_UART6RST\_Pos 6

[ 96](numaker__m55m1x__reset_8h.md#af62b4aba699717dd70315a1a27a59772)#define SYS\_UARTRST\_UART7RST\_Pos 7

[ 97](numaker__m55m1x__reset_8h.md#a7a0de863694faa172d2d4b13d1f4b853)#define SYS\_UARTRST\_UART8RST\_Pos 8

[ 98](numaker__m55m1x__reset_8h.md#a3bfd42f6290bccd453cf21bc08169c89)#define SYS\_UARTRST\_UART9RST\_Pos 9

[ 99](numaker__m55m1x__reset_8h.md#a2310e7e721ccb307e62da1501d91c47e)#define SYS\_USBDRST\_USBD0RST\_Pos 0

[ 100](numaker__m55m1x__reset_8h.md#aeb7b29dafb237e1b44ff24cca356b7a6)#define SYS\_USBHRST\_USBH0RST\_Pos 0

[ 101](numaker__m55m1x__reset_8h.md#af75a509ca17a1cc83be626207c40552b)#define SYS\_USCIRST\_USCI0RST\_Pos 0

[ 102](numaker__m55m1x__reset_8h.md#aa200217c523a943c65926cd41b9b22be)#define SYS\_UTCPDRST\_UTCPD0RST\_Pos 0

[ 103](numaker__m55m1x__reset_8h.md#ab422247f1f299a04b6936b294827cf8a)#define SYS\_WWDTRST\_WWDT0RST\_Pos 0

[ 104](numaker__m55m1x__reset_8h.md#a4f665c00708d43760792d1bb53dd9844)#define SYS\_WWDTRST\_WWDT1RST\_Pos 1

105

106/\* End of M55M1 BSP sys\_reg.h reset module copy \*/

107

108/\* Beginning of M55M1 BSP sys.h reset module copy \*/

109

110/\*---------------------------------------------------------------------

111 \* Module Reset Control Resister constant definitions.

112 \*---------------------------------------------------------------------

113 \*/

114

[ 115](numaker__m55m1x__reset_8h.md#a8c190e848c70443af1aea085891350dc)#define NUMAKER\_SYS\_ACMP01RST ((0x200UL<<20) | SYS\_ACMPRST\_ACMP01RST\_Pos)

[ 116](numaker__m55m1x__reset_8h.md#a3986c85ef5f0cd64588ce142796a0b75)#define NUMAKER\_SYS\_ACMP23RST ((0x200UL<<20) | SYS\_ACMPRST\_ACMP23RST\_Pos)

[ 117](numaker__m55m1x__reset_8h.md#a9cc03b176f4b802ff81e49dd46c98cf9)#define NUMAKER\_SYS\_AWF0RST ((0x204UL<<20) | SYS\_AWFRST\_AWF0RST\_Pos)

[ 118](numaker__m55m1x__reset_8h.md#a1ce5bab4aae4fe46765f489538ac3e5f)#define NUMAKER\_SYS\_BPWM0RST ((0x208UL<<20) | SYS\_BPWMRST\_BPWM0RST\_Pos)

[ 119](numaker__m55m1x__reset_8h.md#a6e3cf0a2d3eb529484b965880e571eed)#define NUMAKER\_SYS\_BPWM1RST ((0x208UL<<20) | SYS\_BPWMRST\_BPWM1RST\_Pos)

[ 120](numaker__m55m1x__reset_8h.md#a42be68efb0af0df536a954e7736ecb98)#define NUMAKER\_SYS\_CANFD0RST ((0x20CUL<<20) | SYS\_CANFDRST\_CANFD0RST\_Pos)

[ 121](numaker__m55m1x__reset_8h.md#ae7da75dffc2eec9360a4936c53106380)#define NUMAKER\_SYS\_CANFD1RST ((0x20CUL<<20) | SYS\_CANFDRST\_CANFD1RST\_Pos)

[ 122](numaker__m55m1x__reset_8h.md#ac9892c38048a56a889f02bb99047d18b)#define NUMAKER\_SYS\_CCAP0RST ((0x210UL<<20) | SYS\_CCAPRST\_CCAP0RST\_Pos)

[ 123](numaker__m55m1x__reset_8h.md#a8a93573dba98e2efbeb65c6f5bfb80a9)#define NUMAKER\_SYS\_CRC0RST ((0x214UL<<20) | SYS\_CRCRST\_CRC0RST\_Pos)

[ 124](numaker__m55m1x__reset_8h.md#adc80007ac2eae87ab5b85d1173bbd186)#define NUMAKER\_SYS\_CRYPTO0RST ((0x218UL<<20) | SYS\_CRYPTORST\_CRYPTO0RST\_Pos)

[ 125](numaker__m55m1x__reset_8h.md#aca18900a628a5478dba2dfe8b1555e14)#define NUMAKER\_SYS\_DAC01RST ((0x21CUL<<20) | SYS\_DACRST\_DAC01RST\_Pos)

[ 126](numaker__m55m1x__reset_8h.md#a40ed20984bfb8558d414e18af2c4d871)#define NUMAKER\_SYS\_DMIC0RST ((0x220UL<<20) | SYS\_DMICRST\_DMIC0RST\_Pos)

[ 127](numaker__m55m1x__reset_8h.md#a88b5456b8227b47071ca81606a64c50a)#define NUMAKER\_SYS\_EADC0RST ((0x224UL<<20) | SYS\_EADCRST\_EADC0RST\_Pos)

[ 128](numaker__m55m1x__reset_8h.md#ae039ba0ea7e08c519dd2ae5feb6b929d)#define NUMAKER\_SYS\_EBI0RST ((0x228UL<<20) | SYS\_EBIRST\_EBI0RST\_Pos)

[ 129](numaker__m55m1x__reset_8h.md#ad590065f2e48957bd844f07481078edc)#define NUMAKER\_SYS\_ECAP0RST ((0x22CUL<<20) | SYS\_ECAPRST\_ECAP0RST\_Pos)

[ 130](numaker__m55m1x__reset_8h.md#ab8a3073e8c3998670cd3f1379b9e0aca)#define NUMAKER\_SYS\_ECAP1RST ((0x22CUL<<20) | SYS\_ECAPRST\_ECAP1RST\_Pos)

[ 131](numaker__m55m1x__reset_8h.md#a4a8ef449a9580b4f9cc2e48de6de1e35)#define NUMAKER\_SYS\_ECAP2RST ((0x22CUL<<20) | SYS\_ECAPRST\_ECAP2RST\_Pos)

[ 132](numaker__m55m1x__reset_8h.md#a16c565a8a9bf9a858f4b4d16b99d5cf1)#define NUMAKER\_SYS\_ECAP3RST ((0x22CUL<<20) | SYS\_ECAPRST\_ECAP3RST\_Pos)

[ 133](numaker__m55m1x__reset_8h.md#ac59bc870dad68a3e461371f466051196)#define NUMAKER\_SYS\_EMAC0RST ((0x230UL<<20) | SYS\_EMACRST\_EMAC0RST\_Pos)

[ 134](numaker__m55m1x__reset_8h.md#a24d6639d3b8f20f875274a3220eb48e4)#define NUMAKER\_SYS\_EPWM0RST ((0x234UL<<20) | SYS\_EPWMRST\_EPWM0RST\_Pos)

[ 135](numaker__m55m1x__reset_8h.md#a9c7c469dfc73165540932027f1a6d659)#define NUMAKER\_SYS\_EPWM1RST ((0x234UL<<20) | SYS\_EPWMRST\_EPWM1RST\_Pos)

[ 136](numaker__m55m1x__reset_8h.md#a5ddd9534d0bf70f4316b2626bd3424bf)#define NUMAKER\_SYS\_EQEI0RST ((0x238UL<<20) | SYS\_EQEIRST\_EQEI0RST\_Pos)

[ 137](numaker__m55m1x__reset_8h.md#a6c7da847d65d78630e7235fdf6f53409)#define NUMAKER\_SYS\_EQEI1RST ((0x238UL<<20) | SYS\_EQEIRST\_EQEI1RST\_Pos)

[ 138](numaker__m55m1x__reset_8h.md#a09f274d2f8f0baf2f782f0bb55fd5644)#define NUMAKER\_SYS\_EQEI2RST ((0x238UL<<20) | SYS\_EQEIRST\_EQEI2RST\_Pos)

[ 139](numaker__m55m1x__reset_8h.md#a289561eee6ad7af3afe82d013ab3454e)#define NUMAKER\_SYS\_EQEI3RST ((0x238UL<<20) | SYS\_EQEIRST\_EQEI3RST\_Pos)

[ 140](numaker__m55m1x__reset_8h.md#a40c4362563ae4e00b2cf39b3f0cc68a9)#define NUMAKER\_SYS\_FMC0RST ((0x23CUL<<20) | SYS\_FMCRST\_FMC0RST\_Pos)

[ 141](numaker__m55m1x__reset_8h.md#a0f3dd5b68e1fd86b2a5aae3170b16051)#define NUMAKER\_SYS\_GDMA0RST ((0x240UL<<20) | SYS\_GDMARST\_GDMA0RST\_Pos)

[ 142](numaker__m55m1x__reset_8h.md#a15c9ce3ac0688f31663bb6c58cc8930b)#define NUMAKER\_SYS\_GPIO0RST ((0x244UL<<20) | SYS\_GPIORST\_GPIO0RST\_Pos)

[ 143](numaker__m55m1x__reset_8h.md#a78e535d6796e5919c496f59f346e151c)#define NUMAKER\_SYS\_HSOTG0RST ((0x248UL<<20) | SYS\_HSOTGRST\_HSOTG0RST\_Pos)

[ 144](numaker__m55m1x__reset_8h.md#a277c1258f080dc1da598036657dadb2e)#define NUMAKER\_SYS\_HSUSBD0RST ((0x24CUL<<20) | SYS\_HSUSBDRST\_HSUSBD0RST\_Pos)

[ 145](numaker__m55m1x__reset_8h.md#ac19310d993d3b00ea3475ef7f461cf6a)#define NUMAKER\_SYS\_HSUSBH0RST ((0x250UL<<20) | SYS\_HSUSBHRST\_HSUSBH0RST\_Pos)

[ 146](numaker__m55m1x__reset_8h.md#af71b5c74cfe68bd05bfe9a80016b2c16)#define NUMAKER\_SYS\_I2C0RST ((0x254UL<<20) | SYS\_I2CRST\_I2C0RST\_Pos)

[ 147](numaker__m55m1x__reset_8h.md#af27af4419eace44b396139809560b3a6)#define NUMAKER\_SYS\_I2C1RST ((0x254UL<<20) | SYS\_I2CRST\_I2C1RST\_Pos)

[ 148](numaker__m55m1x__reset_8h.md#a056d4faac0a4592a9af8a02cc3340247)#define NUMAKER\_SYS\_I2C2RST ((0x254UL<<20) | SYS\_I2CRST\_I2C2RST\_Pos)

[ 149](numaker__m55m1x__reset_8h.md#a20b4eabb4329af14f010a9f27ef7f433)#define NUMAKER\_SYS\_I2C3RST ((0x254UL<<20) | SYS\_I2CRST\_I2C3RST\_Pos)

[ 150](numaker__m55m1x__reset_8h.md#a9279f3753a089e4ef1565e895320e6e5)#define NUMAKER\_SYS\_I2S0RST ((0x258UL<<20) | SYS\_I2SRST\_I2S0RST\_Pos)

[ 151](numaker__m55m1x__reset_8h.md#a90f02b39519f077219cba3622c82337a)#define NUMAKER\_SYS\_I2S1RST ((0x258UL<<20) | SYS\_I2SRST\_I2S1RST\_Pos)

[ 152](numaker__m55m1x__reset_8h.md#a3340eff52a9a8c937ae2fe1f19003564)#define NUMAKER\_SYS\_I3C0RST ((0x25CUL<<20) | SYS\_I3CRST\_I3C0RST\_Pos)

[ 153](numaker__m55m1x__reset_8h.md#ae02b61dcaed6733e6fee142c420796e9)#define NUMAKER\_SYS\_KDF0RST ((0x260UL<<20) | SYS\_KDFRST\_KDF0RST\_Pos)

[ 154](numaker__m55m1x__reset_8h.md#aa600bd0df70d6460dae57c5347019d36)#define NUMAKER\_SYS\_KPI0RST ((0x264UL<<20) | SYS\_KPIRST\_KPI0RST\_Pos)

[ 155](numaker__m55m1x__reset_8h.md#a77618e7e89294e8c009809a07ae175b9)#define NUMAKER\_SYS\_KS0RST ((0x268UL<<20) | SYS\_KSRST\_KS0RST\_Pos)

[ 156](numaker__m55m1x__reset_8h.md#acc32018760e80ad9f14bbd09759c7a4d)#define NUMAKER\_SYS\_LPADC0RST ((0x26CUL<<20) | SYS\_LPADCRST\_LPADC0RST\_Pos)

[ 157](numaker__m55m1x__reset_8h.md#ae92c3f0b6daa0b89879809a9b12c8799)#define NUMAKER\_SYS\_LPPDMA0RST ((0x270UL<<20) | SYS\_LPPDMARST\_LPPDMA0RST\_Pos)

[ 158](numaker__m55m1x__reset_8h.md#acde1913aa01bfd4032b81a9307dd0c1d)#define NUMAKER\_SYS\_LPGPIO0RST ((0x274UL<<20) | SYS\_LPGPIORST\_LPGPIO0RST\_Pos)

[ 159](numaker__m55m1x__reset_8h.md#a5a075f5c1aa06640d8ce2888bde37f97)#define NUMAKER\_SYS\_LPI2C0RST ((0x278UL<<20) | SYS\_LPI2CRST\_LPI2C0RST\_Pos)

[ 160](numaker__m55m1x__reset_8h.md#aa3790cec6410226a7a11d6b00c3b2f9d)#define NUMAKER\_SYS\_LPSPI0RST ((0x27CUL<<20) | SYS\_LPSPIRST\_LPSPI0RST\_Pos)

[ 161](numaker__m55m1x__reset_8h.md#ac1a9387997f89f4d6d9d326a19fbdb71)#define NUMAKER\_SYS\_LPTMR0RST ((0x280UL<<20) | SYS\_LPTMRRST\_LPTMR0RST\_Pos)

[ 162](numaker__m55m1x__reset_8h.md#a54cc630360345f3f5fa7b432c900a373)#define NUMAKER\_SYS\_LPTMR1RST ((0x280UL<<20) | SYS\_LPTMRRST\_LPTMR1RST\_Pos)

[ 163](numaker__m55m1x__reset_8h.md#ac9c18b0e4f86db0570dc45a3fbf3ce32)#define NUMAKER\_SYS\_LPUART0RST ((0x284UL<<20) | SYS\_LPUARTRST\_LPUART0RST\_Pos)

[ 164](numaker__m55m1x__reset_8h.md#ac7a8edd6e27d263327a29f34d86cd7ed)#define NUMAKER\_SYS\_NPURST ((0x004UL<<20) | SYS\_RSTCTL\_NPURST\_Pos)

[ 165](numaker__m55m1x__reset_8h.md#ab1872acf386b4506a52a107c04b9d125)#define NUMAKER\_SYS\_OTFC0RST ((0x288UL<<20) | SYS\_OTFCRST\_OTFC0RST\_Pos)

[ 166](numaker__m55m1x__reset_8h.md#a956c139ed38d275333052fc9f4215884)#define NUMAKER\_SYS\_OTG0RST ((0x28CUL<<20) | SYS\_OTGRST\_OTG0RST\_Pos)

[ 167](numaker__m55m1x__reset_8h.md#aa1c936e0d8267bcfb2811a5eb86d46aa)#define NUMAKER\_SYS\_PDMA0RST ((0x290UL<<20) | SYS\_PDMARST\_PDMA0RST\_Pos)

[ 168](numaker__m55m1x__reset_8h.md#a66aab4cbe715dba5172dceaf4feff209)#define NUMAKER\_SYS\_PDMA1RST ((0x290UL<<20) | SYS\_PDMARST\_PDMA1RST\_Pos)

[ 169](numaker__m55m1x__reset_8h.md#a366b95a4088a6d18647c204ba0168813)#define NUMAKER\_SYS\_PSIO0RST ((0x294UL<<20) | SYS\_PSIORST\_PSIO0RST\_Pos)

[ 170](numaker__m55m1x__reset_8h.md#a5a02332ec587e8b7637cae1777a8dbf8)#define NUMAKER\_SYS\_QSPI0RST ((0x298UL<<20) | SYS\_QSPIRST\_QSPI0RST\_Pos)

[ 171](numaker__m55m1x__reset_8h.md#aacb040d7abb0ee633e562fa8f0d61fcd)#define NUMAKER\_SYS\_QSPI1RST ((0x298UL<<20) | SYS\_QSPIRST\_QSPI1RST\_Pos)

[ 172](numaker__m55m1x__reset_8h.md#a5655e767b9a67d2500ed9c3bd6699658)#define NUMAKER\_SYS\_RTC0RST ((0x29CUL<<20) | SYS\_RTCRST\_RTC0RST\_Pos)

[ 173](numaker__m55m1x__reset_8h.md#af35bb89eea34091304812286cf9207df)#define NUMAKER\_SYS\_SC0RST ((0x2A0UL<<20) | SYS\_SCRST\_SC0RST\_Pos)

[ 174](numaker__m55m1x__reset_8h.md#a6f5c04ca1eb183c1d04f7c15937f7c97)#define NUMAKER\_SYS\_SC1RST ((0x2A0UL<<20) | SYS\_SCRST\_SC1RST\_Pos)

[ 175](numaker__m55m1x__reset_8h.md#a86be7cc834bba894c750540562552fff)#define NUMAKER\_SYS\_SC2RST ((0x2A0UL<<20) | SYS\_SCRST\_SC2RST\_Pos)

[ 176](numaker__m55m1x__reset_8h.md#a00e397d9c4d8b1e20e72b21ce2057c73)#define NUMAKER\_SYS\_SCU0RST ((0x2A4UL<<20) | SYS\_SCURST\_SCU0RST\_Pos)

[ 177](numaker__m55m1x__reset_8h.md#a905b13a6cae73ba7dd26e3d3edc97196)#define NUMAKER\_SYS\_SDH0RST ((0x2A8UL<<20) | SYS\_SDHRST\_SDH0RST\_Pos)

[ 178](numaker__m55m1x__reset_8h.md#a24cfd1c941a1e4fdb44547fe221cbe08)#define NUMAKER\_SYS\_SDH1RST ((0x2A8UL<<20) | SYS\_SDHRST\_SDH1RST\_Pos)

[ 179](numaker__m55m1x__reset_8h.md#ae9e926c108461af140ff4ca87e6e0461)#define NUMAKER\_SYS\_SPI0RST ((0x2ACUL<<20) | SYS\_SPIRST\_SPI0RST\_Pos)

[ 180](numaker__m55m1x__reset_8h.md#a9c33572035c2492035197df07c35da5d)#define NUMAKER\_SYS\_SPI1RST ((0x2ACUL<<20) | SYS\_SPIRST\_SPI1RST\_Pos)

[ 181](numaker__m55m1x__reset_8h.md#ab766153b7a9d90598bec08ab671423d8)#define NUMAKER\_SYS\_SPI2RST ((0x2ACUL<<20) | SYS\_SPIRST\_SPI2RST\_Pos)

[ 182](numaker__m55m1x__reset_8h.md#ac2a5330dd3bc6e2fd7110bb6c801a88a)#define NUMAKER\_SYS\_SPI3RST ((0x2ACUL<<20) | SYS\_SPIRST\_SPI3RST\_Pos)

[ 183](numaker__m55m1x__reset_8h.md#ae40fc7a1a348f2124789202a61731a43)#define NUMAKER\_SYS\_SPIM0RST ((0x2B0UL<<20) | SYS\_SPIMRST\_SPIM0RST\_Pos)

[ 184](numaker__m55m1x__reset_8h.md#af69b236718c2d05e79a93287c1320ee3)#define NUMAKER\_SYS\_TMR0RST ((0x2C0UL<<20) | SYS\_TMRRST\_TMR0RST\_Pos)

[ 185](numaker__m55m1x__reset_8h.md#a4c880ab7cfbdff38ebd8298a731c4a5b)#define NUMAKER\_SYS\_TMR1RST ((0x2C0UL<<20) | SYS\_TMRRST\_TMR1RST\_Pos)

[ 186](numaker__m55m1x__reset_8h.md#af232cec3ae0661b5a3347287898a1ffe)#define NUMAKER\_SYS\_TMR2RST ((0x2C0UL<<20) | SYS\_TMRRST\_TMR2RST\_Pos)

[ 187](numaker__m55m1x__reset_8h.md#a28d1d74b3a4b4672dfaede49d5d8d154)#define NUMAKER\_SYS\_TMR3RST ((0x2C0UL<<20) | SYS\_TMRRST\_TMR3RST\_Pos)

[ 188](numaker__m55m1x__reset_8h.md#aacfac9e96acba24fc4ca9ec300c72a6d)#define NUMAKER\_SYS\_TRNG0RST ((0x2C4UL<<20) | SYS\_TRNGRST\_TRNG0RST\_Pos)

[ 189](numaker__m55m1x__reset_8h.md#acc34a1629b31a117a90dd00d9a524ea3)#define NUMAKER\_SYS\_TTMR0RST ((0x2C8UL<<20) | SYS\_TTMRRST\_TTMR0RST\_Pos)

[ 190](numaker__m55m1x__reset_8h.md#a906d4db5ba21b29bc1c327269a649a71)#define NUMAKER\_SYS\_TTMR1RST ((0x2C8UL<<20) | SYS\_TTMRRST\_TTMR1RST\_Pos)

[ 191](numaker__m55m1x__reset_8h.md#a219fe06bfa5008806f53e79a1bcc9fa0)#define NUMAKER\_SYS\_UART0RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART0RST\_Pos)

[ 192](numaker__m55m1x__reset_8h.md#a82c22d2919f017c42a846edd1b0c0682)#define NUMAKER\_SYS\_UART1RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART1RST\_Pos)

[ 193](numaker__m55m1x__reset_8h.md#aa8f97b0648025c01c6a425f9fb87d096)#define NUMAKER\_SYS\_UART2RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART2RST\_Pos)

[ 194](numaker__m55m1x__reset_8h.md#a7b385d8a50b6734f8065a180243fa4f5)#define NUMAKER\_SYS\_UART3RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART3RST\_Pos)

[ 195](numaker__m55m1x__reset_8h.md#a2cebf05be30230a7fee4cb7825c453c2)#define NUMAKER\_SYS\_UART4RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART4RST\_Pos)

[ 196](numaker__m55m1x__reset_8h.md#ad953d0f0d573aad4ff6244c0c7fd53d6)#define NUMAKER\_SYS\_UART5RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART5RST\_Pos)

[ 197](numaker__m55m1x__reset_8h.md#abc09c8dde4ade8582b7750bf8627d176)#define NUMAKER\_SYS\_UART6RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART6RST\_Pos)

[ 198](numaker__m55m1x__reset_8h.md#ab2061644295df12b532e239b16d2f812)#define NUMAKER\_SYS\_UART7RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART7RST\_Pos)

[ 199](numaker__m55m1x__reset_8h.md#aeddbb0475f669030445eb846ed78121f)#define NUMAKER\_SYS\_UART8RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART8RST\_Pos)

[ 200](numaker__m55m1x__reset_8h.md#ac3bafb3fc30379b30c9ea93c8e1b6c4e)#define NUMAKER\_SYS\_UART9RST ((0x2CCUL<<20) | SYS\_UARTRST\_UART9RST\_Pos)

[ 201](numaker__m55m1x__reset_8h.md#ae1f872af98f0f5ba7dc33cd528094e42)#define NUMAKER\_SYS\_USBD0RST ((0x2D0UL<<20) | SYS\_USBDRST\_USBD0RST\_Pos)

[ 202](numaker__m55m1x__reset_8h.md#ac9a03322b226e8cf0e6dc37bd46f69ee)#define NUMAKER\_SYS\_USBH0RST ((0x2D4UL<<20) | SYS\_USBHRST\_USBH0RST\_Pos)

[ 203](numaker__m55m1x__reset_8h.md#a182358f5c4a0763164dfeb36d05fcf50)#define NUMAKER\_SYS\_USCI0RST ((0x2D8UL<<20) | SYS\_USCIRST\_USCI0RST\_Pos)

[ 204](numaker__m55m1x__reset_8h.md#ae119a7785f517696f99fc26b921da2c6)#define NUMAKER\_SYS\_UTCPD0RST ((0x2DCUL<<20) | SYS\_UTCPDRST\_UTCPD0RST\_Pos)

[ 205](numaker__m55m1x__reset_8h.md#a794708ce7d8df10df327baa0cafbb7f1)#define NUMAKER\_SYS\_WWDT0RST ((0x2E0UL<<20) | SYS\_WWDTRST\_WWDT0RST\_Pos)

[ 206](numaker__m55m1x__reset_8h.md#a0db488b63a7e0f8a7157db924052ddd9)#define NUMAKER\_SYS\_WWDT1RST ((0x2E0UL<<20) | SYS\_WWDTRST\_WWDT1RST\_Pos)

207

208/\* End of M55M1 BSP sys.h reset module copy \*/

209

210#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [numaker\_m55m1x\_reset.h](numaker__m55m1x__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
