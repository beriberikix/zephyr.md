---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/numaker__m46x__clock_8h_source.html
original_path: doxygen/html/numaker__m46x__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numaker\_m46x\_clock.h

[Go to the documentation of this file.](numaker__m46x__clock_8h.md)

1/\*

2 \* Copyright (c) 2023 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NUMAKER\_M46X\_CLOCK\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NUMAKER\_M46X\_CLOCK\_H

9

10/\* Beginning of M460 BSP clk\_reg.h copy \*/

11

[ 12](numaker__m46x__clock_8h.md#a58b51925b1e326fcf1b44c78c9aac0bc)#define NUMAKER\_CLK\_AHBCLK0\_PDMA0CKEN\_Pos (1)

[ 13](numaker__m46x__clock_8h.md#a38d9951e8a71b2f89bdf7b016feb09cb)#define NUMAKER\_CLK\_AHBCLK0\_ISPCKEN\_Pos (2)

[ 14](numaker__m46x__clock_8h.md#abe3b51583a6c3b5e7fac4502c29a15c5)#define NUMAKER\_CLK\_AHBCLK0\_EBICKEN\_Pos (3)

[ 15](numaker__m46x__clock_8h.md#a59c032586da81c2128ecfe553e779560)#define NUMAKER\_CLK\_AHBCLK0\_STCKEN\_Pos (4)

[ 16](numaker__m46x__clock_8h.md#af00c90db38b73bed47ef5a00cfe92a87)#define NUMAKER\_CLK\_AHBCLK0\_EMAC0CKEN\_Pos (5)

[ 17](numaker__m46x__clock_8h.md#a34b8dd1f5a2a514eec3ee4ff2376126d)#define NUMAKER\_CLK\_AHBCLK0\_SDH0CKEN\_Pos (6)

[ 18](numaker__m46x__clock_8h.md#a43961045e5cfb5bfd8e3f25ca0d3de38)#define NUMAKER\_CLK\_AHBCLK0\_CRCCKEN\_Pos (7)

[ 19](numaker__m46x__clock_8h.md#a7e8862c4f20298f950b253c0ab613fec)#define NUMAKER\_CLK\_AHBCLK0\_CCAPCKEN\_Pos (8)

[ 20](numaker__m46x__clock_8h.md#a5de977a2fd728aa7a12e0a667b639bca)#define NUMAKER\_CLK\_AHBCLK0\_SENCKEN\_Pos (9)

[ 21](numaker__m46x__clock_8h.md#afd7bb1592e766086bf5c4f2f2d6224cd)#define NUMAKER\_CLK\_AHBCLK0\_HSUSBDCKEN\_Pos (10)

[ 22](numaker__m46x__clock_8h.md#a806485d7f3f8924d91f8daedb53faecf)#define NUMAKER\_CLK\_AHBCLK0\_HBICKEN\_Pos (11)

[ 23](numaker__m46x__clock_8h.md#a31f1a197a3b5093f006feb37b424b1d7)#define NUMAKER\_CLK\_AHBCLK0\_CRPTCKEN\_Pos (12)

[ 24](numaker__m46x__clock_8h.md#a3d2f1af1de01e7d4459d16e92f1c73a4)#define NUMAKER\_CLK\_AHBCLK0\_KSCKEN\_Pos (13)

[ 25](numaker__m46x__clock_8h.md#af224d39ec0080a0d4f0776098ed240a6)#define NUMAKER\_CLK\_AHBCLK0\_SPIMCKEN\_Pos (14)

[ 26](numaker__m46x__clock_8h.md#aa1b458c17c208504e2736af420016fe9)#define NUMAKER\_CLK\_AHBCLK0\_FMCIDLE\_Pos (15)

[ 27](numaker__m46x__clock_8h.md#a69bca44bfebe798d128021f12a902367)#define NUMAKER\_CLK\_AHBCLK0\_USBHCKEN\_Pos (16)

[ 28](numaker__m46x__clock_8h.md#a76947087379239ccbc5e822d45667dc4)#define NUMAKER\_CLK\_AHBCLK0\_SDH1CKEN\_Pos (17)

[ 29](numaker__m46x__clock_8h.md#a0067d71da4392dcafde9dc0b4c3a7fe9)#define NUMAKER\_CLK\_AHBCLK0\_PDMA1CKEN\_Pos (18)

[ 30](numaker__m46x__clock_8h.md#ab06c990333e66d787fe5e08e749f2f0d)#define NUMAKER\_CLK\_AHBCLK0\_TRACECKEN\_Pos (19)

[ 31](numaker__m46x__clock_8h.md#a61792f0f11c9f76016d1a89ce71b74f7)#define NUMAKER\_CLK\_AHBCLK0\_GPACKEN\_Pos (24)

[ 32](numaker__m46x__clock_8h.md#af8cd5804e7ae8676e0245ccd9e6a4c74)#define NUMAKER\_CLK\_AHBCLK0\_GPBCKEN\_Pos (25)

[ 33](numaker__m46x__clock_8h.md#ad5dc0793b20ab18ddba5e972f71caedb)#define NUMAKER\_CLK\_AHBCLK0\_GPCCKEN\_Pos (26)

[ 34](numaker__m46x__clock_8h.md#ab150c51327c505db2217f90e5f8fd028)#define NUMAKER\_CLK\_AHBCLK0\_GPDCKEN\_Pos (27)

[ 35](numaker__m46x__clock_8h.md#a8be4ace7190b0947707eaa8d99fc63b0)#define NUMAKER\_CLK\_AHBCLK0\_GPECKEN\_Pos (28)

[ 36](numaker__m46x__clock_8h.md#a33270f5ef0594fe4960eabd4d135e612)#define NUMAKER\_CLK\_AHBCLK0\_GPFCKEN\_Pos (29)

[ 37](numaker__m46x__clock_8h.md#a7b443fbeff14a12542f89e445ea2f2d3)#define NUMAKER\_CLK\_AHBCLK0\_GPGCKEN\_Pos (30)

[ 38](numaker__m46x__clock_8h.md#ae1e54f46825a4fa27f526ba7de0c8607)#define NUMAKER\_CLK\_AHBCLK0\_GPHCKEN\_Pos (31)

39

[ 40](numaker__m46x__clock_8h.md#ab2ec740c5cb44791065972a2de785cbe)#define NUMAKER\_CLK\_APBCLK0\_WDTCKEN\_Pos (0)

[ 41](numaker__m46x__clock_8h.md#a8c3c6a3361689ff6f7737ccdff117bc6)#define NUMAKER\_CLK\_APBCLK0\_RTCCKEN\_Pos (1)

[ 42](numaker__m46x__clock_8h.md#aa3854ff57bfbbaecfe7e23d2771d7333)#define NUMAKER\_CLK\_APBCLK0\_TMR0CKEN\_Pos (2)

[ 43](numaker__m46x__clock_8h.md#afb30c612fbf094fc60c811ccbaa22df0)#define NUMAKER\_CLK\_APBCLK0\_TMR1CKEN\_Pos (3)

[ 44](numaker__m46x__clock_8h.md#a70e54a13473d4ec204f354d2a8e120c8)#define NUMAKER\_CLK\_APBCLK0\_TMR2CKEN\_Pos (4)

[ 45](numaker__m46x__clock_8h.md#a8588ec96cf9ba5a541372b886310e31f)#define NUMAKER\_CLK\_APBCLK0\_TMR3CKEN\_Pos (5)

[ 46](numaker__m46x__clock_8h.md#a20f966cae9fa1c3ffd7533892c014af9)#define NUMAKER\_CLK\_APBCLK0\_CLKOCKEN\_Pos (6)

[ 47](numaker__m46x__clock_8h.md#a51a8258755b28e0f0c6d147cb169ee95)#define NUMAKER\_CLK\_APBCLK0\_ACMP01CKEN\_Pos (7)

[ 48](numaker__m46x__clock_8h.md#a8e959e2086ca96c0da9ed6e8a8426dad)#define NUMAKER\_CLK\_APBCLK0\_I2C0CKEN\_Pos (8)

[ 49](numaker__m46x__clock_8h.md#ae9cacf97bbdb9935315aef7d852da0b8)#define NUMAKER\_CLK\_APBCLK0\_I2C1CKEN\_Pos (9)

[ 50](numaker__m46x__clock_8h.md#a896126d0a6312d382ebd1054216c73d7)#define NUMAKER\_CLK\_APBCLK0\_I2C2CKEN\_Pos (10)

[ 51](numaker__m46x__clock_8h.md#ad616218273d67669884e19ef3ee5234e)#define NUMAKER\_CLK\_APBCLK0\_I2C3CKEN\_Pos (11)

[ 52](numaker__m46x__clock_8h.md#aabf3594b4f7e6224a88d5edc89afbfe0)#define NUMAKER\_CLK\_APBCLK0\_QSPI0CKEN\_Pos (12)

[ 53](numaker__m46x__clock_8h.md#a367f258ea5537b3948adedc307b90e2b)#define NUMAKER\_CLK\_APBCLK0\_SPI0CKEN\_Pos (13)

[ 54](numaker__m46x__clock_8h.md#acbab43558f5e2ca3ab88245ddb009f3f)#define NUMAKER\_CLK\_APBCLK0\_SPI1CKEN\_Pos (14)

[ 55](numaker__m46x__clock_8h.md#a1fdb03816fc8bdaed6f207be2ab47548)#define NUMAKER\_CLK\_APBCLK0\_SPI2CKEN\_Pos (15)

[ 56](numaker__m46x__clock_8h.md#a5c2df8fa94c924887ecdb20e8c664f5c)#define NUMAKER\_CLK\_APBCLK0\_UART0CKEN\_Pos (16)

[ 57](numaker__m46x__clock_8h.md#a61fc05731dec14cd6bdf6c16d8ddd0cb)#define NUMAKER\_CLK\_APBCLK0\_UART1CKEN\_Pos (17)

[ 58](numaker__m46x__clock_8h.md#a1ffeeb21492fe1cae89a23e3809056ce)#define NUMAKER\_CLK\_APBCLK0\_UART2CKEN\_Pos (18)

[ 59](numaker__m46x__clock_8h.md#afa7a7b670568bbed4613ac860ac764d4)#define NUMAKER\_CLK\_APBCLK0\_UART3CKEN\_Pos (19)

[ 60](numaker__m46x__clock_8h.md#af2b11ee30e0ee2608d2550656aa38c26)#define NUMAKER\_CLK\_APBCLK0\_UART4CKEN\_Pos (20)

[ 61](numaker__m46x__clock_8h.md#adb4a2eb99fa2c5646866a5d55b97534e)#define NUMAKER\_CLK\_APBCLK0\_UART5CKEN\_Pos (21)

[ 62](numaker__m46x__clock_8h.md#a34c0f3828864c8e740190bc3a094a5de)#define NUMAKER\_CLK\_APBCLK0\_UART6CKEN\_Pos (22)

[ 63](numaker__m46x__clock_8h.md#ae1a1383fc645274edfb35e3f603e559f)#define NUMAKER\_CLK\_APBCLK0\_UART7CKEN\_Pos (23)

[ 64](numaker__m46x__clock_8h.md#ac2c53fe5cfb83b42bebaea1140368cc7)#define NUMAKER\_CLK\_APBCLK0\_OTGCKEN\_Pos (26)

[ 65](numaker__m46x__clock_8h.md#a03fba41df5559e507195dfa734d6ce0e)#define NUMAKER\_CLK\_APBCLK0\_USBDCKEN\_Pos (27)

[ 66](numaker__m46x__clock_8h.md#a58adbfadda83fb8b1d9a50578ee64409)#define NUMAKER\_CLK\_APBCLK0\_EADC0CKEN\_Pos (28)

[ 67](numaker__m46x__clock_8h.md#a0dda3ed1ac9a4473df221a3c7602d789)#define NUMAKER\_CLK\_APBCLK0\_I2S0CKEN\_Pos (29)

[ 68](numaker__m46x__clock_8h.md#a1b8069d895df60e4dc9269adc36602c8)#define NUMAKER\_CLK\_APBCLK0\_HSOTGCKEN\_Pos (30)

[ 69](numaker__m46x__clock_8h.md#a572eca05a9b8478a29f63e9401145bd4)#define NUMAKER\_CLK\_APBCLK1\_SC0CKEN\_Pos (0)

[ 70](numaker__m46x__clock_8h.md#a59ba15908e8db725b14dc000fbb17318)#define NUMAKER\_CLK\_APBCLK1\_SC1CKEN\_Pos (1)

[ 71](numaker__m46x__clock_8h.md#aa1cb79620df2a7aa170b83b9f0837294)#define NUMAKER\_CLK\_APBCLK1\_SC2CKEN\_Pos (2)

[ 72](numaker__m46x__clock_8h.md#ab2e9eda6c9cf544ee895d2c238241dd4)#define NUMAKER\_CLK\_APBCLK1\_I2C4CKEN\_Pos (3)

[ 73](numaker__m46x__clock_8h.md#a069cd6290f117eded4bfc7db70dd3c50)#define NUMAKER\_CLK\_APBCLK1\_QSPI1CKEN\_Pos (4)

[ 74](numaker__m46x__clock_8h.md#a386c818d9955a72ee48ceb19e4f91927)#define NUMAKER\_CLK\_APBCLK1\_SPI3CKEN\_Pos (6)

[ 75](numaker__m46x__clock_8h.md#a1d8508e63ddc549f0cdbd58e7f2fecac)#define NUMAKER\_CLK\_APBCLK1\_SPI4CKEN\_Pos (7)

[ 76](numaker__m46x__clock_8h.md#a789f8b30f0fc9e2713b025d3e56a78ad)#define NUMAKER\_CLK\_APBCLK1\_USCI0CKEN\_Pos (8)

[ 77](numaker__m46x__clock_8h.md#a5f14b1218cc23b5ae4a5febf2ab3f231)#define NUMAKER\_CLK\_APBCLK1\_PSIOCKEN\_Pos (10)

[ 78](numaker__m46x__clock_8h.md#ac4bb6f1b74c5ae9e8c25a2c4accf3e91)#define NUMAKER\_CLK\_APBCLK1\_DACCKEN\_Pos (12)

[ 79](numaker__m46x__clock_8h.md#a4187ddb711d9b621ffd100f693ecab87)#define NUMAKER\_CLK\_APBCLK1\_ECAP2CKEN\_Pos (13)

[ 80](numaker__m46x__clock_8h.md#a2303b958de0df016987f93b1bf3ab085)#define NUMAKER\_CLK\_APBCLK1\_ECAP3CKEN\_Pos (14)

[ 81](numaker__m46x__clock_8h.md#aa26749ba77ea33d82dac563913f91631)#define NUMAKER\_CLK\_APBCLK1\_EPWM0CKEN\_Pos (16)

[ 82](numaker__m46x__clock_8h.md#a1030ba160597af2055aa8bc8cf1e783f)#define NUMAKER\_CLK\_APBCLK1\_EPWM1CKEN\_Pos (17)

[ 83](numaker__m46x__clock_8h.md#a7748917fa5664552d90ad85fd3ac6253)#define NUMAKER\_CLK\_APBCLK1\_BPWM0CKEN\_Pos (18)

[ 84](numaker__m46x__clock_8h.md#ac240fa173fd611698a50e18acacc7e8b)#define NUMAKER\_CLK\_APBCLK1\_BPWM1CKEN\_Pos (19)

[ 85](numaker__m46x__clock_8h.md#a8159e95120dff6946e93d12bb9c2e103)#define NUMAKER\_CLK\_APBCLK1\_EQEI2CKEN\_Pos (20)

[ 86](numaker__m46x__clock_8h.md#af4ba87fd1820c165e405c025bc1c6e1f)#define NUMAKER\_CLK\_APBCLK1\_EQEI3CKEN\_Pos (21)

[ 87](numaker__m46x__clock_8h.md#a96f335c83be01e4d323ff1050f55af19)#define NUMAKER\_CLK\_APBCLK1\_EQEI0CKEN\_Pos (22)

[ 88](numaker__m46x__clock_8h.md#a3f26ee3e388e1bad4752c264e706d34f)#define NUMAKER\_CLK\_APBCLK1\_EQEI1CKEN\_Pos (23)

[ 89](numaker__m46x__clock_8h.md#a453287405a43aaa6e2215c1d1d20b079)#define NUMAKER\_CLK\_APBCLK1\_TRNGCKEN\_Pos (25)

[ 90](numaker__m46x__clock_8h.md#a93061f89415f32df54b3d386a85608d8)#define NUMAKER\_CLK\_APBCLK1\_ECAP0CKEN\_Pos (26)

[ 91](numaker__m46x__clock_8h.md#a68b041451f3023be8d47f78c56c64875)#define NUMAKER\_CLK\_APBCLK1\_ECAP1CKEN\_Pos (27)

[ 92](numaker__m46x__clock_8h.md#a327ba049d422169d52fabb8296f204c1)#define NUMAKER\_CLK\_APBCLK1\_I2S1CKEN\_Pos (29)

[ 93](numaker__m46x__clock_8h.md#a87a961c8e77c418e7df428ff03974d15)#define NUMAKER\_CLK\_APBCLK1\_EADC1CKEN\_Pos (31)

94

[ 95](numaker__m46x__clock_8h.md#a222c77f1b55f0230c37bd5335616e31c)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_Pos (0)

[ 96](numaker__m46x__clock_8h.md#a08af6458eb9ad7f8e6d66c0e51625585)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_Pos (3)

[ 97](numaker__m46x__clock_8h.md#a04d6c39e779459221829cc06c880a3be)#define NUMAKER\_CLK\_CLKSEL0\_USBSEL\_Pos (8)

[ 98](numaker__m46x__clock_8h.md#aaed2bedbc7da8190be001522a8b0fda3)#define NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_Pos (10)

[ 99](numaker__m46x__clock_8h.md#a4aabc45f1e6d05ed3882752d3d9cd0bc)#define NUMAKER\_CLK\_CLKSEL0\_EADC1SEL\_Pos (12)

[ 100](numaker__m46x__clock_8h.md#a0cc1044cebda8f140387cd6668c1d28b)#define NUMAKER\_CLK\_CLKSEL0\_EADC2SEL\_Pos (14)

[ 101](numaker__m46x__clock_8h.md#a26fbf9452f88cd3c9d56da527bcf9701)#define NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_Pos (16)

[ 102](numaker__m46x__clock_8h.md#ad511a487821a9fce9bb9f3ba370d2a88)#define NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_Pos (20)

[ 103](numaker__m46x__clock_8h.md#a43fe53773587485494ee0658e7191db6)#define NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_Pos (22)

[ 104](numaker__m46x__clock_8h.md#ae8a431223539932fdb7f76dd696dc660)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_Pos (24)

[ 105](numaker__m46x__clock_8h.md#ac37d09c55ca74d2b3b07f1c9528589b9)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_Pos (26)

[ 106](numaker__m46x__clock_8h.md#aa8b514cd21320d7554a07793f8a275dc)#define NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_Pos (28)

[ 107](numaker__m46x__clock_8h.md#a58f6dd49a1d6ea3f453ec352e2ad3d31)#define NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_Pos (30)

[ 108](numaker__m46x__clock_8h.md#ae766e87b0198cd6d632efc6ad6c90f2f)#define NUMAKER\_CLK\_CLKSEL1\_WDTSEL\_Pos (0)

[ 109](numaker__m46x__clock_8h.md#a173d950f779cd43bcbc19ab59bcfdb9f)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_Pos (4)

[ 110](numaker__m46x__clock_8h.md#a5267afb76d8c7121ae916d16bd11beba)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_Pos (8)

[ 111](numaker__m46x__clock_8h.md#acc9cb2446eb710fd02622388b038cb80)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_Pos (12)

[ 112](numaker__m46x__clock_8h.md#a434692498a750b11be1cc4fb23f15d25)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_Pos (16)

[ 113](numaker__m46x__clock_8h.md#a6431caf24c465342f811c99c46beec23)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_Pos (20)

[ 114](numaker__m46x__clock_8h.md#a59454cdc6f895e4870f36409d2bae4ec)#define NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_Pos (24)

[ 115](numaker__m46x__clock_8h.md#af7249c7982a7b0aecb14ad23d4d69177)#define NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_Pos (26)

[ 116](numaker__m46x__clock_8h.md#abde910c3bea13e43a62ea0f308a3d67d)#define NUMAKER\_CLK\_CLKSEL1\_WWDTSEL\_Pos (30)

[ 117](numaker__m46x__clock_8h.md#a7c7e4439cb2a5ea61d131ca5aa34c13f)#define NUMAKER\_CLK\_CLKSEL2\_EPWM0SEL\_Pos (0)

[ 118](numaker__m46x__clock_8h.md#a789a88e5c5bb82243395ab44d9150f2f)#define NUMAKER\_CLK\_CLKSEL2\_EPWM1SEL\_Pos (1)

[ 119](numaker__m46x__clock_8h.md#afd2bdefddd574beef75f27fe63235b71)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_Pos (2)

[ 120](numaker__m46x__clock_8h.md#a3f3697e0e6786758e2d558704c1ae95b)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_Pos (4)

[ 121](numaker__m46x__clock_8h.md#a468889c86406ba0ac19dc13ea3676819)#define NUMAKER\_CLK\_CLKSEL2\_BPWM0SEL\_Pos (8)

[ 122](numaker__m46x__clock_8h.md#ac1482052fb0001105c872760676e9b85)#define NUMAKER\_CLK\_CLKSEL2\_BPWM1SEL\_Pos (9)

[ 123](numaker__m46x__clock_8h.md#abaa371d43c61b5eac6209c49450be2bb)#define NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_Pos (10)

[ 124](numaker__m46x__clock_8h.md#a00200de5091f4a3e3eb6205a3eb2710e)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_Pos (12)

[ 125](numaker__m46x__clock_8h.md#a62b60bef47ebaa4283c592cf1befd06a)#define NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_Pos (16)

[ 126](numaker__m46x__clock_8h.md#a77c6617ce411e7d7c1c844b5d759ea81)#define NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_Pos (20)

[ 127](numaker__m46x__clock_8h.md#aa0d54fd960a54667ebd1648e3ff59372)#define NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_Pos (22)

[ 128](numaker__m46x__clock_8h.md#ae64e22341ff5a80754b972cc939499f2)#define NUMAKER\_CLK\_CLKSEL2\_TRNGSEL\_Pos (27)

[ 129](numaker__m46x__clock_8h.md#a3dd2bba6fd135bb75d81ba88307145ad)#define NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_Pos (28)

[ 130](numaker__m46x__clock_8h.md#a19c633148ca7ea93e9614e49d2e143e5)#define NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_Pos (0)

[ 131](numaker__m46x__clock_8h.md#a6fd49b4bc34a81053e90d06014081b29)#define NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_Pos (2)

[ 132](numaker__m46x__clock_8h.md#a0937060d13a67d6c6b6b440b160bce78)#define NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_Pos (4)

[ 133](numaker__m46x__clock_8h.md#ab62463cdd14a928e8d9981d10bb58c5d)#define NUMAKER\_CLK\_CLKSEL3\_KPISEL\_Pos (6)

[ 134](numaker__m46x__clock_8h.md#a34f8358a68834ea06c779d8554990ab1)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_Pos (9)

[ 135](numaker__m46x__clock_8h.md#a8544ff20404a07e93d2dbcd170da2806)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_Pos (12)

[ 136](numaker__m46x__clock_8h.md#a8998c20d1845afb0936f18a3ffdd277e)#define NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_Pos (16)

[ 137](numaker__m46x__clock_8h.md#a0fa73839deb734011ed856ab1b3d29f3)#define NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_Pos (20)

[ 138](numaker__m46x__clock_8h.md#a19cd6b3c40c825dfe2a8193ad3d530ca)#define NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_Pos (22)

[ 139](numaker__m46x__clock_8h.md#aa1f1fc552a722bafea8f9177ed609877)#define NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_Pos (24)

[ 140](numaker__m46x__clock_8h.md#acf28a2139435cc793c0b712e8e8a0806)#define NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_Pos (26)

[ 141](numaker__m46x__clock_8h.md#a3b8ea6d3069dfc8d3727f0bb4cdf6600)#define NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_Pos (28)

[ 142](numaker__m46x__clock_8h.md#aac88d611ffa6b1f45c123b1af12b0d6d)#define NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_Pos (30)

143

[ 144](numaker__m46x__clock_8h.md#a97fa36df7672c2dd77d953d8c52179c3)#define NUMAKER\_CLK\_CLKDIV0\_HCLKDIV\_Pos (0)

[ 145](numaker__m46x__clock_8h.md#a9c6fa39e37ec8da8ef2de45a01669724)#define NUMAKER\_CLK\_CLKDIV0\_USBDIV\_Pos (4)

[ 146](numaker__m46x__clock_8h.md#a5c6e1b8ff6fc666f729c456ced30ed2d)#define NUMAKER\_CLK\_CLKDIV0\_UART0DIV\_Pos (8)

[ 147](numaker__m46x__clock_8h.md#a079560398552b7e309109dea93758098)#define NUMAKER\_CLK\_CLKDIV0\_UART1DIV\_Pos (12)

[ 148](numaker__m46x__clock_8h.md#a6b2cf403f52fd1a62f33611ddff65ccb)#define NUMAKER\_CLK\_CLKDIV0\_EADC0DIV\_Pos (16)

[ 149](numaker__m46x__clock_8h.md#a308fbc20ea60cfcc3a64aba7f83336df)#define NUMAKER\_CLK\_CLKDIV0\_SDH0DIV\_Pos (24)

[ 150](numaker__m46x__clock_8h.md#a26f255ab6373c7db56f9541ffcaf9137)#define NUMAKER\_CLK\_CLKDIV1\_SC0DIV\_Pos (0)

[ 151](numaker__m46x__clock_8h.md#afdc1213b38b64f09f75e5d59d9bd343b)#define NUMAKER\_CLK\_CLKDIV1\_SC1DIV\_Pos (8)

[ 152](numaker__m46x__clock_8h.md#ac1aea552215c5515caa825405d3d3926)#define NUMAKER\_CLK\_CLKDIV1\_SC2DIV\_Pos (16)

[ 153](numaker__m46x__clock_8h.md#abb507dbd18f953fc72e539c44957d43b)#define NUMAKER\_CLK\_CLKDIV1\_PSIODIV\_Pos (24)

[ 154](numaker__m46x__clock_8h.md#a15546e5819aea803f07b0be19fe156fe)#define NUMAKER\_CLK\_CLKDIV2\_I2S0DIV\_Pos (0)

[ 155](numaker__m46x__clock_8h.md#a4ee0df1038a212dc2c943d3b66af8849)#define NUMAKER\_CLK\_CLKDIV2\_I2S1DIV\_Pos (4)

[ 156](numaker__m46x__clock_8h.md#ad29157a28b15201dcda03bbb484d4e17)#define NUMAKER\_CLK\_CLKDIV2\_KPIDIV\_Pos (8)

[ 157](numaker__m46x__clock_8h.md#ac3630dbacd1ad31365cf658614529810)#define NUMAKER\_CLK\_CLKDIV2\_EADC1DIV\_Pos (24)

[ 158](numaker__m46x__clock_8h.md#ad9ad999a5cf04196d30a8d91d3938f0a)#define NUMAKER\_CLK\_CLKDIV3\_VSENSEDIV\_Pos (8)

[ 159](numaker__m46x__clock_8h.md#a2b55d1154a5c7723e7ddfcf35565b542)#define NUMAKER\_CLK\_CLKDIV3\_EMAC0DIV\_Pos (16)

[ 160](numaker__m46x__clock_8h.md#aedc4fed5c50badc54edef17ec075ecc4)#define NUMAKER\_CLK\_CLKDIV3\_SDH1DIV\_Pos (24)

[ 161](numaker__m46x__clock_8h.md#a4ea4427d406d1eb1078c209177e42f73)#define NUMAKER\_CLK\_CLKDIV4\_UART2DIV\_Pos (0)

[ 162](numaker__m46x__clock_8h.md#acfdd626271018f3f1432ce7e2d9d7376)#define NUMAKER\_CLK\_CLKDIV4\_UART3DIV\_Pos (4)

[ 163](numaker__m46x__clock_8h.md#a3624622b04d58420cc034e869c932928)#define NUMAKER\_CLK\_CLKDIV4\_UART4DIV\_Pos (8)

[ 164](numaker__m46x__clock_8h.md#afc690368ba8774739f034d404e3c5401)#define NUMAKER\_CLK\_CLKDIV4\_UART5DIV\_Pos (12)

[ 165](numaker__m46x__clock_8h.md#ab72e30643c1e14a66d5e5a19aa3e0b3c)#define NUMAKER\_CLK\_CLKDIV4\_UART6DIV\_Pos (16)

[ 166](numaker__m46x__clock_8h.md#ace495a935bbfe7dba9c4101d10ed7ff4)#define NUMAKER\_CLK\_CLKDIV4\_UART7DIV\_Pos (20)

167

[ 168](numaker__m46x__clock_8h.md#a254f625e23596b631a3b9ee7e2d23d7c)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos (0)

[ 169](numaker__m46x__clock_8h.md#ab1bcb755f780777114d690945f00cce6)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos (4)

170

[ 171](numaker__m46x__clock_8h.md#a8a2c2a4f9e6d38bb5198f0bf78b123ed)#define NUMAKER\_CLK\_APBCLK2\_KPICKEN\_Pos (0)

[ 172](numaker__m46x__clock_8h.md#a1074ea1f3692cf7c3c263cf409624cba)#define NUMAKER\_CLK\_APBCLK2\_EADC2CKEN\_Pos (6)

[ 173](numaker__m46x__clock_8h.md#a27e7054840a6130eb6a91160e9294a85)#define NUMAKER\_CLK\_APBCLK2\_ACMP23CKEN\_Pos (7)

[ 174](numaker__m46x__clock_8h.md#ab31f85d74e996dff00563e13de27cfb9)#define NUMAKER\_CLK\_APBCLK2\_SPI5CKEN\_Pos (8)

[ 175](numaker__m46x__clock_8h.md#a831afd6bae798caf0303159b748d62bf)#define NUMAKER\_CLK\_APBCLK2\_SPI6CKEN\_Pos (9)

[ 176](numaker__m46x__clock_8h.md#a16689092a9fde746dcfb179af8c07470)#define NUMAKER\_CLK\_APBCLK2\_SPI7CKEN\_Pos (10)

[ 177](numaker__m46x__clock_8h.md#abbff3536dfcc434dedd936ef17fae208)#define NUMAKER\_CLK\_APBCLK2\_SPI8CKEN\_Pos (11)

[ 178](numaker__m46x__clock_8h.md#affa49b7c031d534acb6d6989da9611c1)#define NUMAKER\_CLK\_APBCLK2\_SPI9CKEN\_Pos (12)

[ 179](numaker__m46x__clock_8h.md#a998500f8ff7b225099aabfc56dea74e7)#define NUMAKER\_CLK\_APBCLK2\_SPI10CKEN\_Pos (13)

[ 180](numaker__m46x__clock_8h.md#aa27014b1c91ab54b8a60401be51e86be)#define NUMAKER\_CLK\_APBCLK2\_UART8CKEN\_Pos (16)

[ 181](numaker__m46x__clock_8h.md#ae25c9ea6caa15b827fc92cad41b1d2c4)#define NUMAKER\_CLK\_APBCLK2\_UART9CKEN\_Pos (17)

182

[ 183](numaker__m46x__clock_8h.md#ac5847065a5b666a23ad5ab459cab206e)#define NUMAKER\_CLK\_CLKDIV5\_CANFD0DIV\_Pos (0)

[ 184](numaker__m46x__clock_8h.md#ab9f0662feaf58f785abb509007878ac8)#define NUMAKER\_CLK\_CLKDIV5\_CANFD1DIV\_Pos (4)

[ 185](numaker__m46x__clock_8h.md#a74ebf455bde77e81cb6885a3f8ee644c)#define NUMAKER\_CLK\_CLKDIV5\_CANFD2DIV\_Pos (8)

[ 186](numaker__m46x__clock_8h.md#a38f53a703ceeb17e3e1794004b79cea1)#define NUMAKER\_CLK\_CLKDIV5\_CANFD3DIV\_Pos (12)

[ 187](numaker__m46x__clock_8h.md#a7295d4b8918c0eb234826e2e3c86695d)#define NUMAKER\_CLK\_CLKDIV5\_UART8DIV\_Pos (16)

[ 188](numaker__m46x__clock_8h.md#af9e916e5c92262fc8f7dc79dfd51da11)#define NUMAKER\_CLK\_CLKDIV5\_UART9DIV\_Pos (20)

[ 189](numaker__m46x__clock_8h.md#af968f32399159b10da33c64b8b73ab2c)#define NUMAKER\_CLK\_CLKDIV5\_EADC2DIV\_Pos (24)

190

[ 191](numaker__m46x__clock_8h.md#a08b8216298f1ab185b96159bfd0d68e7)#define NUMAKER\_CLK\_AHBCLK1\_CANFD0CKEN\_Pos (20)

[ 192](numaker__m46x__clock_8h.md#a010bc688f8ac881039b1c74297017492)#define NUMAKER\_CLK\_AHBCLK1\_CANFD1CKEN\_Pos (21)

[ 193](numaker__m46x__clock_8h.md#a90bfed7241959b097624838c56fd05fb)#define NUMAKER\_CLK\_AHBCLK1\_CANFD2CKEN\_Pos (22)

[ 194](numaker__m46x__clock_8h.md#a8fbabf2f5b8be3af891ea039e533dd3e)#define NUMAKER\_CLK\_AHBCLK1\_CANFD3CKEN\_Pos (23)

[ 195](numaker__m46x__clock_8h.md#a32f4d5437f7724cdf93bbde025c0825a)#define NUMAKER\_CLK\_AHBCLK1\_GPICKEN\_Pos (24)

[ 196](numaker__m46x__clock_8h.md#a48e8655610a9b5e7f0548d0d02467d22)#define NUMAKER\_CLK\_AHBCLK1\_GPJCKEN\_Pos (25)

[ 197](numaker__m46x__clock_8h.md#a824b2bde29f8f7374bed1bec0d7f114d)#define NUMAKER\_CLK\_AHBCLK1\_BMCCKEN\_Pos (28)

198

[ 199](numaker__m46x__clock_8h.md#a09bd54b91ecd5c6729d6dd2270d1f538)#define NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_Pos (0)

[ 200](numaker__m46x__clock_8h.md#a7f314d8e78add81c86d07bf9bbf3d4c4)#define NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_Pos (4)

[ 201](numaker__m46x__clock_8h.md#ac2232b05fd8986cf75aaba710c42d257)#define NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_Pos (8)

[ 202](numaker__m46x__clock_8h.md#afb315f157e0a04e14fd5962844c099e4)#define NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_Pos (12)

[ 203](numaker__m46x__clock_8h.md#a4781a6db591eb9488391fc9ee8711041)#define NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_Pos (16)

[ 204](numaker__m46x__clock_8h.md#a140802fd7bd3257bc125d6a32ad3a1b8)#define NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_Pos (20)

[ 205](numaker__m46x__clock_8h.md#a7a92cd1f644926d955409b49b785c738)#define NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_Pos (24)

206

207/\* End of M460 BSP clk\_reg.h copy \*/

208

209/\* Beginning of M460 BSP clk.h copy \*/

210

211/\* CLKSEL0 constant definitions. (Write-protection) \*/

212

[ 213](numaker__m46x__clock_8h.md#aaf5b579f16bb170913264beb84939aa2)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_Pos)

[ 214](numaker__m46x__clock_8h.md#a53e9db59708390ee4ff22e11f554fc5e)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_Pos)

[ 215](numaker__m46x__clock_8h.md#ae98f1f84fa81ed435a46eccaab5bb66b)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_PLL (0x2UL << NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_Pos)

[ 216](numaker__m46x__clock_8h.md#a88a9e37b2360e0f703c0c469468adb1e)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_LIRC (0x3UL << NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_Pos)

[ 217](numaker__m46x__clock_8h.md#a35a5144f4df0ca09710fbc8d86377537)#define NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_HIRC (0x7UL << NUMAKER\_CLK\_CLKSEL0\_HCLKSEL\_Pos)

218

[ 219](numaker__m46x__clock_8h.md#a937c9db689672d3f6e53e6b0f5a680ae)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_Pos)

[ 220](numaker__m46x__clock_8h.md#a7195fd0da5b897cf2c1e5df46205198d)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_Pos)

[ 221](numaker__m46x__clock_8h.md#a1afd0ea4fb7e6bbc5f36a7845121b5bb)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HXT\_DIV2 (0x2UL << NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_Pos)

[ 222](numaker__m46x__clock_8h.md#a6e4942ca524470a1dbfd9c1012c3d6fc)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HCLK\_DIV2 (0x3UL << NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_Pos)

[ 223](numaker__m46x__clock_8h.md#aee56f494a2a1028b579aee48a229bd62)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HIRC\_DIV2 (0x7UL << NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_Pos)

[ 224](numaker__m46x__clock_8h.md#a80331a452e4606a3ea97a6e8271c879f)#define NUMAKER\_CLK\_CLKSEL0\_STCLKSEL\_HCLK (0x1UL << SysTick\_CTRL\_CLKSOURCE\_Pos)

225

[ 226](numaker__m46x__clock_8h.md#a4324fd407c6e6dbb86e84810094030fb)#define NUMAKER\_CLK\_CLKSEL0\_USBSEL\_HIRC48M (0x0UL << NUMAKER\_CLK\_CLKSEL0\_USBSEL\_Pos)

[ 227](numaker__m46x__clock_8h.md#ae3285c43e19c374c1bf08c3a4c76dd4a)#define NUMAKER\_CLK\_CLKSEL0\_USBSEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_USBSEL\_Pos)

228

[ 229](numaker__m46x__clock_8h.md#ae1a84816773eaaedd0e9ec34f9601c49)#define NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_PLLFN\_DIV2 (0x0UL << NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_Pos)

[ 230](numaker__m46x__clock_8h.md#a334d6fe725e38ef14aa66f5811f154b0)#define NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_Pos)

[ 231](numaker__m46x__clock_8h.md#a8f1802b4d8c733d098e6f457ea9ca0a8)#define NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_EADC0SEL\_Pos)

232

[ 233](numaker__m46x__clock_8h.md#ae53479d1a845ca065c134e9acb69d490)#define NUMAKER\_CLK\_CLKSEL0\_EADC1SEL\_PLLFN\_DIV2 (0x0UL << NUMAKER\_CLK\_CLKSEL0\_EADC1SEL\_Pos)

[ 234](numaker__m46x__clock_8h.md#a23ff9c30be18f670d0830c9565f51b21)#define NUMAKER\_CLK\_CLKSEL0\_EADC1SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_EADC1SEL\_Pos)

[ 235](numaker__m46x__clock_8h.md#ae200cb9323674a161a17a687e820dd0d)#define NUMAKER\_CLK\_CLKSEL0\_EADC1SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_EADC1SEL\_Pos)

236

[ 237](numaker__m46x__clock_8h.md#ad0975703b1f9d5446601410f2a45cf69)#define NUMAKER\_CLK\_CLKSEL0\_EADC2SEL\_PLLFN\_DIV2 (0x0UL << NUMAKER\_CLK\_CLKSEL0\_EADC2SEL\_Pos)

[ 238](numaker__m46x__clock_8h.md#ac21c81c36e2b66261e6cc7642cac3051)#define NUMAKER\_CLK\_CLKSEL0\_EADC2SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_EADC2SEL\_Pos)

[ 239](numaker__m46x__clock_8h.md#adaf33eed919c5f3bfcc9d98bb6ce7025)#define NUMAKER\_CLK\_CLKSEL0\_EADC2SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_EADC2SEL\_Pos)

240

[ 241](numaker__m46x__clock_8h.md#a19564616e7f7cb594daede7dde7d60e7)#define NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_Pos)

[ 242](numaker__m46x__clock_8h.md#afb6a8f7e4181068fd138c948a1c84343)#define NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_Pos)

[ 243](numaker__m46x__clock_8h.md#a6e7fe24e1cfdc83fc916636c5d50dc0e)#define NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_Pos)

[ 244](numaker__m46x__clock_8h.md#a5bcbdba224ba0863fdd1ff02e5cf0adc)#define NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL0\_CCAPSEL\_Pos)

245

[ 246](numaker__m46x__clock_8h.md#a8787763bb8d1de77dba37b5f1d7fab5c)#define NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_Pos)

[ 247](numaker__m46x__clock_8h.md#aa07cf8396225f74e82b25c19064855f1)#define NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_Pos)

[ 248](numaker__m46x__clock_8h.md#a9946b9c0f363e64e4e71b4cd12baa129)#define NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_Pos)

[ 249](numaker__m46x__clock_8h.md#a3a5b94ee47a9439e2f17b182eec68fe2)#define NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL0\_SDH0SEL\_Pos)

250

[ 251](numaker__m46x__clock_8h.md#a4a793ae5ae068f7da0a955f5059cbabc)#define NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_Pos)

[ 252](numaker__m46x__clock_8h.md#ac7348489c232f20a0aedd88e668b6b01)#define NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_Pos)

[ 253](numaker__m46x__clock_8h.md#a18c3b00a9fa924d2c5ade2623fda2e38)#define NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_Pos)

[ 254](numaker__m46x__clock_8h.md#a979cf701d7e4950ef37cd897e627e994)#define NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL0\_SDH1SEL\_Pos)

255

[ 256](numaker__m46x__clock_8h.md#a097628cbacc57dad0410c5330b6385b8)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_Pos)

[ 257](numaker__m46x__clock_8h.md#aa708753d71c526051cf157266060a2b0)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_Pos)

[ 258](numaker__m46x__clock_8h.md#ae369ded35f04609db7e2a5a6922a5e1a)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_Pos)

[ 259](numaker__m46x__clock_8h.md#aba0fe8b523048854cd02b4825e59f1c0)#define NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL0\_CANFD0SEL\_Pos)

260

[ 261](numaker__m46x__clock_8h.md#a3cc669c6de091303d9c65853000637e2)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_Pos)

[ 262](numaker__m46x__clock_8h.md#a0273d49ae0ae0c27533a83ab1d8b4689)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_Pos)

[ 263](numaker__m46x__clock_8h.md#a1752cabeb909b64b92adbdc61215f3f9)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_Pos)

[ 264](numaker__m46x__clock_8h.md#a43849c77be4cb2dd288f1d0b81bb18c8)#define NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL0\_CANFD1SEL\_Pos)

265

[ 266](numaker__m46x__clock_8h.md#acfc10476765f4bf15d8b2b1fc0f765a4)#define NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_Pos)

[ 267](numaker__m46x__clock_8h.md#a317f7eea8e7c25f610828a7d27bc28eb)#define NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_Pos)

[ 268](numaker__m46x__clock_8h.md#a2aa1ee270857376418300d41da66266f)#define NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_Pos)

[ 269](numaker__m46x__clock_8h.md#ac2013365641d14ee89cb3971297f9858)#define NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL0\_CANFD2SEL\_Pos)

270

[ 271](numaker__m46x__clock_8h.md#ac9556b696bec169814058c9d8c8834ec)#define NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_Pos)

[ 272](numaker__m46x__clock_8h.md#a28328552ec42974273d5fda9ddaf1236)#define NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_Pos)

[ 273](numaker__m46x__clock_8h.md#a354084c66cd641682a67230fcdd4a869)#define NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_Pos)

[ 274](numaker__m46x__clock_8h.md#a8c5085efce1104852894e1e00e6d4ddf)#define NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL0\_CANFD3SEL\_Pos)

275

276/\* CLKSEL1 constant definitions. \*/

277

[ 278](numaker__m46x__clock_8h.md#a7c7748061529c4f6552bc9394b90c701)#define NUMAKER\_CLK\_CLKSEL1\_WDTSEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL1\_WDTSEL\_Pos)

[ 279](numaker__m46x__clock_8h.md#a7feb3eb8a79e72de8dce4bb1a0fe1f75)#define NUMAKER\_CLK\_CLKSEL1\_WDTSEL\_HCLK\_DIV2048 (0x2UL << NUMAKER\_CLK\_CLKSEL1\_WDTSEL\_Pos)

[ 280](numaker__m46x__clock_8h.md#ac746e9a7ac0032e91032d8e4f3286040)#define NUMAKER\_CLK\_CLKSEL1\_WDTSEL\_LIRC (0x3UL << NUMAKER\_CLK\_CLKSEL1\_WDTSEL\_Pos)

281

[ 282](numaker__m46x__clock_8h.md#a2dba089a2c9a8780fa15705ce58719e4)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_Pos)

[ 283](numaker__m46x__clock_8h.md#a0b6ad7b069802aead804d11668cab813)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_Pos)

[ 284](numaker__m46x__clock_8h.md#a9cc286fd7b086fa05e00d24e2d7e5846)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_HCLK (0x2UL << NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_Pos)

[ 285](numaker__m46x__clock_8h.md#a33998b80d4139f5cfd5aa6dc02c762c8)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_Pos)

[ 286](numaker__m46x__clock_8h.md#ade649734a0c7017a8ddf62fdde78873b)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_LIRC (0x4UL << NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_Pos)

[ 287](numaker__m46x__clock_8h.md#a9e71ef0e2022fe9445aae65f908461cc)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_PLLFN\_DIV2 (0x5UL << NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_Pos)

[ 288](numaker__m46x__clock_8h.md#a221299347ceccbd32f2fa331685b869a)#define NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_PLL\_DIV2 (0x6UL << NUMAKER\_CLK\_CLKSEL1\_CLKOSEL\_Pos)

289

[ 290](numaker__m46x__clock_8h.md#a269fe710118dddabc1d17f2d1386835c)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_Pos)

[ 291](numaker__m46x__clock_8h.md#a37317151b25b9c7563a6e572e0199acc)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_Pos)

[ 292](numaker__m46x__clock_8h.md#afe9eadbd094da1c48851507719485200)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_Pos)

[ 293](numaker__m46x__clock_8h.md#ab4b9c993b869f23701052ef27c88cc3b)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_EXT (0x3UL << NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_Pos)

[ 294](numaker__m46x__clock_8h.md#a7f4fd7330e7ff33c4bcd4b8e666f01c1)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_LIRC (0x5UL << NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_Pos)

[ 295](numaker__m46x__clock_8h.md#ac7913ee7fe365daa500f7e1175bda470)#define NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_HIRC (0x7UL << NUMAKER\_CLK\_CLKSEL1\_TMR0SEL\_Pos)

296

[ 297](numaker__m46x__clock_8h.md#a1a6d0e60fd711d553ac0b0bf78ea6d54)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_Pos)

[ 298](numaker__m46x__clock_8h.md#a425b5c7e0d424c13328840437f9a0bb9)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_Pos)

[ 299](numaker__m46x__clock_8h.md#a54f24cfa94c28f844f428bd06e68eb8e)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_Pos)

[ 300](numaker__m46x__clock_8h.md#a208dcc5b1095e5cf4c2dec3c312a62ac)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_EXT (0x3UL << NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_Pos)

[ 301](numaker__m46x__clock_8h.md#a1f9fde3db711f618393435af9dcdd621)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_LIRC (0x5UL << NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_Pos)

[ 302](numaker__m46x__clock_8h.md#acb979acb614600a7126e12eefc181c8c)#define NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_HIRC (0x7UL << NUMAKER\_CLK\_CLKSEL1\_TMR1SEL\_Pos)

303

[ 304](numaker__m46x__clock_8h.md#ad0ac4ff4a21c3469c892dca5f6a7d469)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_Pos)

[ 305](numaker__m46x__clock_8h.md#afc8fb6c4fa6138465928926044fadd86)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_Pos)

[ 306](numaker__m46x__clock_8h.md#af5d0ba5a62dbc29d7e5e2d0ebf026584)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_Pos)

[ 307](numaker__m46x__clock_8h.md#a6cd38e0106ba70158dce964022d1ff93)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_EXT (0x3UL << NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_Pos)

[ 308](numaker__m46x__clock_8h.md#a868569fb4688e0c5399d753f751b71f4)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_LIRC (0x5UL << NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_Pos)

[ 309](numaker__m46x__clock_8h.md#aa19a857602df260f1c5715008dd7cedf)#define NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_HIRC (0x7UL << NUMAKER\_CLK\_CLKSEL1\_TMR2SEL\_Pos)

310

[ 311](numaker__m46x__clock_8h.md#a41fd2a33360832aa6de1ff87d1a8d1a4)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_Pos)

[ 312](numaker__m46x__clock_8h.md#a20ba7b5a926c9a4686e452a209221336)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_Pos)

[ 313](numaker__m46x__clock_8h.md#a597126647f0c72cddca37488818158f1)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_Pos)

[ 314](numaker__m46x__clock_8h.md#a6173a75df6e455a46b27486fa74d1b97)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_EXT (0x3UL << NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_Pos)

[ 315](numaker__m46x__clock_8h.md#a3c686b34710b45462347705592e74cb7)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_LIRC (0x5UL << NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_Pos)

[ 316](numaker__m46x__clock_8h.md#a59c5904ed60fd6aff34f2d90cebdf906)#define NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_HIRC (0x7UL << NUMAKER\_CLK\_CLKSEL1\_TMR3SEL\_Pos)

317

[ 318](numaker__m46x__clock_8h.md#ab90957a31d553a527d3810f1e7f5d55a)#define NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_Pos)

[ 319](numaker__m46x__clock_8h.md#ab9b28d741c7058b1f9e37a599f7d0c2e)#define NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_Pos)

[ 320](numaker__m46x__clock_8h.md#a991726670d9ec0108ff6b944d372f469)#define NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_Pos)

[ 321](numaker__m46x__clock_8h.md#a19ac2326e82a127d9e946465a27e0f4f)#define NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL1\_UART0SEL\_Pos)

322

[ 323](numaker__m46x__clock_8h.md#aaa3e59f75b64a5b1c10367b583359f6b)#define NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_Pos)

[ 324](numaker__m46x__clock_8h.md#ac198c6857f66747fe5f776fa78b10aa1)#define NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_Pos)

[ 325](numaker__m46x__clock_8h.md#a4b7f0550827dab6d2a46dc5511526246)#define NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_Pos)

[ 326](numaker__m46x__clock_8h.md#ab5931f2210f1de1ac7f49309a55ce8b8)#define NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL1\_UART1SEL\_Pos)

327

[ 328](numaker__m46x__clock_8h.md#a7d55fac6b093ac281eb9a0bf0762ade4)#define NUMAKER\_CLK\_CLKSEL1\_WWDTSEL\_HCLK\_DIV2048 (0x2UL << NUMAKER\_CLK\_CLKSEL1\_WWDTSEL\_Pos)

[ 329](numaker__m46x__clock_8h.md#a838ca0acbf99746d596456f32ea411e1)#define NUMAKER\_CLK\_CLKSEL1\_WWDTSEL\_LIRC (0x3UL << NUMAKER\_CLK\_CLKSEL1\_WWDTSEL\_Pos)

330

331/\* CLKSEL2 constant definitions. \*/

332

[ 333](numaker__m46x__clock_8h.md#a066b7281b9e714d8e30af62b3df99fb1)#define NUMAKER\_CLK\_CLKSEL2\_EPWM0SEL\_HCLK (0x0UL << NUMAKER\_CLK\_CLKSEL2\_EPWM0SEL\_Pos)

[ 334](numaker__m46x__clock_8h.md#a5886a5009f7f0ef41f04bff54c2f4781)#define NUMAKER\_CLK\_CLKSEL2\_EPWM0SEL\_PCLK0 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_EPWM0SEL\_Pos)

335

[ 336](numaker__m46x__clock_8h.md#a6ed53fbec964b2d85b10b8be7d3d5063)#define NUMAKER\_CLK\_CLKSEL2\_EPWM1SEL\_HCLK (0x0UL << NUMAKER\_CLK\_CLKSEL2\_EPWM1SEL\_Pos)

[ 337](numaker__m46x__clock_8h.md#a84f8299574ba19909d135d6958655a67)#define NUMAKER\_CLK\_CLKSEL2\_EPWM1SEL\_PCLK1 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_EPWM1SEL\_Pos)

338

[ 339](numaker__m46x__clock_8h.md#ab2035f3ef4f5dfa4dbd629b928729114)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_Pos)

[ 340](numaker__m46x__clock_8h.md#a33885ea70f6c99f43f6b814090ce695c)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_Pos)

[ 341](numaker__m46x__clock_8h.md#a7e185755d01c123d2b05e7657f50b87f)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_Pos)

[ 342](numaker__m46x__clock_8h.md#ab8f6509882bb312a7bb5f215e21556be)#define NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL2\_QSPI0SEL\_Pos)

343

[ 344](numaker__m46x__clock_8h.md#aa8fea6d4d392fbb12385bd3dc3d7e41d)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_Pos)

[ 345](numaker__m46x__clock_8h.md#a1f155d341a87fdac387ea48a5778d4ed)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_Pos)

[ 346](numaker__m46x__clock_8h.md#a7f6f7f591f7b3ce3522fa63abe564fe5)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_Pos)

[ 347](numaker__m46x__clock_8h.md#a5490e8ae6a82a281d81026b37ad5dfb7)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_Pos)

[ 348](numaker__m46x__clock_8h.md#ad8b1a5339bf72877ac1eee28e35cdc76)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_HIRC48M (0x4UL << NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_Pos)

[ 349](numaker__m46x__clock_8h.md#a738bbbfabacb6342c8b257b1ece00ebe)#define NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_PLLFN\_DIV2 (0x5UL << NUMAKER\_CLK\_CLKSEL2\_SPI0SEL\_Pos)

350

[ 351](numaker__m46x__clock_8h.md#a055b9b799418142db0c31e371b9753fa)#define NUMAKER\_CLK\_CLKSEL2\_BPWM0SEL\_HCLK (0x0UL << NUMAKER\_CLK\_CLKSEL2\_BPWM0SEL\_Pos)

[ 352](numaker__m46x__clock_8h.md#ae7a979646d487520cae4eb025deb3d88)#define NUMAKER\_CLK\_CLKSEL2\_BPWM0SEL\_PCLK0 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_BPWM0SEL\_Pos)

353

[ 354](numaker__m46x__clock_8h.md#a31696dd1f857e3a56b70cf752aabe8f0)#define NUMAKER\_CLK\_CLKSEL2\_BPWM1SEL\_HCLK (0x0UL << NUMAKER\_CLK\_CLKSEL2\_BPWM1SEL\_Pos)

[ 355](numaker__m46x__clock_8h.md#aae05c896f4800dc75fcb0f400d304f62)#define NUMAKER\_CLK\_CLKSEL2\_BPWM1SEL\_PCLK1 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_BPWM1SEL\_Pos)

356

[ 357](numaker__m46x__clock_8h.md#a9d983236876b97094c0b0198bf362da0)#define NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_Pos)

[ 358](numaker__m46x__clock_8h.md#a0d4eceb83b11d248d984cae5286c14cc)#define NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_Pos)

[ 359](numaker__m46x__clock_8h.md#a92310f4949beba40270a3b7056b768a8)#define NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_Pos)

[ 360](numaker__m46x__clock_8h.md#a18b75ffb5e2247daa96bad18e29ac504)#define NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL2\_QSPI1SEL\_Pos)

361

[ 362](numaker__m46x__clock_8h.md#a02ec8188dc04f486240c9534ecbd2f76)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_Pos)

[ 363](numaker__m46x__clock_8h.md#aa7b96f0cab55a160ffb9c13cbe8af877)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_Pos)

[ 364](numaker__m46x__clock_8h.md#ac6fe2e428168fde50cdc9d7accebba31)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_Pos)

[ 365](numaker__m46x__clock_8h.md#a62209956eeaf9174960a476a2514b72d)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_Pos)

[ 366](numaker__m46x__clock_8h.md#a14000a6d12ea314b48c738e39ae5e6c2)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_HIRC48M (0x4UL << NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_Pos)

[ 367](numaker__m46x__clock_8h.md#ade1874823eacddebee27346428929ede)#define NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_PLLFN\_DIV2 (0x5UL << NUMAKER\_CLK\_CLKSEL2\_SPI1SEL\_Pos)

368

[ 369](numaker__m46x__clock_8h.md#aa344af8b6f18787fac24b160e68cdc43)#define NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_Pos)

[ 370](numaker__m46x__clock_8h.md#a5781d8776f1f0639e61db3ff3f18308d)#define NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_Pos)

[ 371](numaker__m46x__clock_8h.md#adb1533714b11dbf4c4bc7346a47c127b)#define NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_Pos)

[ 372](numaker__m46x__clock_8h.md#acd9a0f64bd383507c174cfb15e840d2b)#define NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_Pos)

[ 373](numaker__m46x__clock_8h.md#af62a05371d707939ecf9b2297cdb8bf8)#define NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_HIRC48M (0x4UL << NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_Pos)

[ 374](numaker__m46x__clock_8h.md#a0e4f643aa45c97deec5cd470a02fc394)#define NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_PLLFN\_DIV2 (0x5UL << NUMAKER\_CLK\_CLKSEL2\_I2S1SEL\_Pos)

375

[ 376](numaker__m46x__clock_8h.md#a9bf2e582bee931751b74b2a548646270)#define NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_Pos)

[ 377](numaker__m46x__clock_8h.md#af1287ca664d3787fc7d43045461c0f80)#define NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_Pos)

[ 378](numaker__m46x__clock_8h.md#af1f34545d01798605d3121d673c246ba)#define NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_Pos)

[ 379](numaker__m46x__clock_8h.md#aab4cb19bf0ad8e6104c8db8a8e8b4660)#define NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL2\_UART8SEL\_Pos)

380

[ 381](numaker__m46x__clock_8h.md#a585a3db6c47f759efec73a4ed7fa22ea)#define NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_Pos)

[ 382](numaker__m46x__clock_8h.md#ad6255ce889f6dbd8a9329bde314aae09)#define NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_Pos)

[ 383](numaker__m46x__clock_8h.md#a3e8c5f032ac973a2c6e97f5233d41d2e)#define NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_Pos)

[ 384](numaker__m46x__clock_8h.md#aac3144fb15ccfb78bd7fc83af15b514a)#define NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL2\_UART9SEL\_Pos)

385

[ 386](numaker__m46x__clock_8h.md#a30bf76b4a03d61b0f0f8365cb6b9639c)#define NUMAKER\_CLK\_CLKSEL2\_TRNGSEL\_LXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_TRNGSEL\_Pos)

[ 387](numaker__m46x__clock_8h.md#a3f961d2f6e112240fc930fd43f0a6e88)#define NUMAKER\_CLK\_CLKSEL2\_TRNGSEL\_LIRC (0x1UL << NUMAKER\_CLK\_CLKSEL2\_TRNGSEL\_Pos)

388

[ 389](numaker__m46x__clock_8h.md#a9aa23bab20b1b4468a8743302dd1c7ab)#define NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_Pos)

[ 390](numaker__m46x__clock_8h.md#ae6720ec8079ccfd3034fa74f8aa8ed18)#define NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_LXT (0x1UL << NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_Pos)

[ 391](numaker__m46x__clock_8h.md#a14234fa9d410f13ce14866ae0347a882)#define NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_Pos)

[ 392](numaker__m46x__clock_8h.md#a7b56de33f223091c59782a86eea91f56)#define NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_PLL\_DIV2 (0x3UL << NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_Pos)

[ 393](numaker__m46x__clock_8h.md#af2a0cf63f7a2af7aa989963c4f90abc2)#define NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_LIRC (0x4UL << NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_Pos)

[ 394](numaker__m46x__clock_8h.md#af34cb3673e0ad70480a5a24ce26ca9a3)#define NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_HIRC (0x5UL << NUMAKER\_CLK\_CLKSEL2\_PSIOSEL\_Pos)

395

396/\* CLKSEL3 constant definitions. \*/

397

[ 398](numaker__m46x__clock_8h.md#a51a3f59da3bb773b180df7ffb8f6e062)#define NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_Pos)

[ 399](numaker__m46x__clock_8h.md#afd2366fc3ed2750af1224ff94b4f4473)#define NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_Pos)

[ 400](numaker__m46x__clock_8h.md#aa2f306a6f8133c48b65e9296b9252def)#define NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_Pos)

[ 401](numaker__m46x__clock_8h.md#ab7a71f01a8340762103de86a4485501b)#define NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_SC0SEL\_Pos)

402

[ 403](numaker__m46x__clock_8h.md#a48d1214da483d0510aba9b06c0e9c8ef)#define NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_Pos)

[ 404](numaker__m46x__clock_8h.md#a6c43b7837b4ebaf01d6ab8f6d441de9c)#define NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_Pos)

[ 405](numaker__m46x__clock_8h.md#aaac8336fe0aad8115a1f1c8f9c985d87)#define NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_Pos)

[ 406](numaker__m46x__clock_8h.md#a40d22aade311a018b9f95336cb0baaa6)#define NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_SC1SEL\_Pos)

407

[ 408](numaker__m46x__clock_8h.md#a41a42c3b21866a058623ac46b20f01a3)#define NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_Pos)

[ 409](numaker__m46x__clock_8h.md#a8a2981c9b91c13a2cbdfe6161ee5f890)#define NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_Pos)

[ 410](numaker__m46x__clock_8h.md#aa5675f4749b15655a31586dd4aac26b8)#define NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_Pos)

[ 411](numaker__m46x__clock_8h.md#a50f0041607bf3863c8df920fedf96ea0)#define NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_SC2SEL\_Pos)

412

[ 413](numaker__m46x__clock_8h.md#abae76078aade03ef47ac19c1ad20bae7)#define NUMAKER\_CLK\_CLKSEL3\_KPISEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_KPISEL\_Pos)

[ 414](numaker__m46x__clock_8h.md#a8b046263c9ff1d8fbe51fa377b048119)#define NUMAKER\_CLK\_CLKSEL3\_KPISEL\_LIRC (0x1UL << NUMAKER\_CLK\_CLKSEL3\_KPISEL\_Pos)

[ 415](numaker__m46x__clock_8h.md#ad0d8e9747739d59ec078ed6c9d24bb85)#define NUMAKER\_CLK\_CLKSEL3\_KPISEL\_HIRC (0x2UL << NUMAKER\_CLK\_CLKSEL3\_KPISEL\_Pos)

416

[ 417](numaker__m46x__clock_8h.md#abfae567f85ec08381bb0db7c81fd74d3)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_Pos)

[ 418](numaker__m46x__clock_8h.md#a0f678617a8bd348b9587a04609be7548)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_Pos)

[ 419](numaker__m46x__clock_8h.md#a13a781d3f27119fb8067191f981fc52b)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_Pos)

[ 420](numaker__m46x__clock_8h.md#ab087f54ea6ea67e1f41aeaf948782c1f)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_Pos)

[ 421](numaker__m46x__clock_8h.md#a3e5c5f8daec012d060843a800802fea1)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_HIRC48M (0x4UL << NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_Pos)

[ 422](numaker__m46x__clock_8h.md#aecd6af9356ecdeead2b9daa599628f69)#define NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_PLLFN\_DIV2 (0x5UL << NUMAKER\_CLK\_CLKSEL3\_SPI2SEL\_Pos)

423

[ 424](numaker__m46x__clock_8h.md#a3b87db844ad61714826adc34da9ec7b0)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_Pos)

[ 425](numaker__m46x__clock_8h.md#a63ae5b13f3280b5f9842a994fb017263)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_Pos)

[ 426](numaker__m46x__clock_8h.md#a38d7de1142dbcbb41efc14ff3a509e6a)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_Pos)

[ 427](numaker__m46x__clock_8h.md#a013d56f4921687d6417e06944e0604f4)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_Pos)

[ 428](numaker__m46x__clock_8h.md#a97eb5cf29a9fdf172288db3696a9c690)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_HIRC48M (0x4UL << NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_Pos)

[ 429](numaker__m46x__clock_8h.md#a583b38aa35525e5f4262d79c2f74142a)#define NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_PLLFN\_DIV2 (0x5UL << NUMAKER\_CLK\_CLKSEL3\_SPI3SEL\_Pos)

430

[ 431](numaker__m46x__clock_8h.md#a5974644957888fce996694a23d0c8974)#define NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_Pos)

[ 432](numaker__m46x__clock_8h.md#a6f43b5f162e778c82096ba88e61c3bab)#define NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_Pos)

[ 433](numaker__m46x__clock_8h.md#a19fae5fa37ea497e8cbbc4e35fcc7a1c)#define NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_Pos)

[ 434](numaker__m46x__clock_8h.md#ae6167fdcb715fdab8590115d08732a52)#define NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_Pos)

[ 435](numaker__m46x__clock_8h.md#a05f172005696ffe09d09e2419ec4a0c2)#define NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_HIRC48M (0x4UL << NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_Pos)

[ 436](numaker__m46x__clock_8h.md#af4fa24cf94713ff0cc30c3f75fd9a1c7)#define NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_PLLFN\_DIV2 (0x5UL << NUMAKER\_CLK\_CLKSEL3\_I2S0SEL\_Pos)

437

[ 438](numaker__m46x__clock_8h.md#a5750431bef8248dbf0400bc304c28e83)#define NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_Pos)

[ 439](numaker__m46x__clock_8h.md#a8ced2c03a1e88b125372539afef7d6fb)#define NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_Pos)

[ 440](numaker__m46x__clock_8h.md#a7c12327af81e305e8daee591c40a6e29)#define NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_Pos)

[ 441](numaker__m46x__clock_8h.md#acfe7822fd07115a0361d50dd2c1b158a)#define NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_UART6SEL\_Pos)

442

[ 443](numaker__m46x__clock_8h.md#ae826f6a8852e0768e4b68300e24cc298)#define NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_Pos)

[ 444](numaker__m46x__clock_8h.md#ae1d938ba5b4aa9838f1a860db7591f60)#define NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_Pos)

[ 445](numaker__m46x__clock_8h.md#a2992f14efbae61aaa34af5b854c70c24)#define NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_Pos)

[ 446](numaker__m46x__clock_8h.md#a3d6df478f726baa83aa0ed72a41e14b2)#define NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_UART7SEL\_Pos)

447

[ 448](numaker__m46x__clock_8h.md#aa4cf778724c945fbdf5ce101d53db019)#define NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_Pos)

[ 449](numaker__m46x__clock_8h.md#a6b98bb87b62119444fe455d2061d85c2)#define NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_Pos)

[ 450](numaker__m46x__clock_8h.md#a64e775dfda0f36499d1d357c301a517d)#define NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_Pos)

[ 451](numaker__m46x__clock_8h.md#a240355ff578cb006df6b963071fe1151)#define NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_UART2SEL\_Pos)

452

[ 453](numaker__m46x__clock_8h.md#a435f628f7f8ed83c7919590dab30d723)#define NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_Pos)

[ 454](numaker__m46x__clock_8h.md#a5685fa5b106626b8bd39e12591a8e6e4)#define NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_Pos)

[ 455](numaker__m46x__clock_8h.md#ab7ba7823db4fb9e9573c5022993e658c)#define NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_Pos)

[ 456](numaker__m46x__clock_8h.md#abc297ff0ee39a512baccea1b84d31743)#define NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_UART3SEL\_Pos)

457

[ 458](numaker__m46x__clock_8h.md#ad1bd01284da31bc01fd795e9008ba940)#define NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_Pos)

[ 459](numaker__m46x__clock_8h.md#a4cde53577fb97204f462d44532a6a44c)#define NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_Pos)

[ 460](numaker__m46x__clock_8h.md#a0668601d9c207300251ea1cb4d88af80)#define NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_Pos)

[ 461](numaker__m46x__clock_8h.md#a5caa47dd6f666aba29f1c1fbf2d39733)#define NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_UART4SEL\_Pos)

462

[ 463](numaker__m46x__clock_8h.md#a3883f4f7ad84d8fccef42a0ae9c83fb5)#define NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_Pos)

[ 464](numaker__m46x__clock_8h.md#a109f1c70fbd27a2b92abf64be1741447)#define NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_Pos)

[ 465](numaker__m46x__clock_8h.md#a0c55bde547ef28bac6c322ccb530221a)#define NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_LXT (0x2UL << NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_Pos)

[ 466](numaker__m46x__clock_8h.md#a9069b1ca1a84527ca21ef310cc7b2245)#define NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL3\_UART5SEL\_Pos)

467

468/\* CLKSEL4 constant definitions. \*/

469

[ 470](numaker__m46x__clock_8h.md#ac8514600296c9b7ecd74022cd9b7c874)#define NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_Pos)

[ 471](numaker__m46x__clock_8h.md#ab2938006eaeb574908b87e912aadddc3)#define NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_Pos)

[ 472](numaker__m46x__clock_8h.md#acb56dc94227bcbee031f1431c9683d1a)#define NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_Pos)

[ 473](numaker__m46x__clock_8h.md#a93a489bf85281241c2d0a287ad57fb79)#define NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL4\_SPI4SEL\_Pos)

474

[ 475](numaker__m46x__clock_8h.md#a69728a9cc0cdad59f4c835881bcb7a62)#define NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_Pos)

[ 476](numaker__m46x__clock_8h.md#a4551497e4f38af0723198c4e037bc982)#define NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_Pos)

[ 477](numaker__m46x__clock_8h.md#a24e622934d9093ef32b4b5babbcb7a18)#define NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_Pos)

[ 478](numaker__m46x__clock_8h.md#aec58f9c54807426347ead63e3277f15b)#define NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL4\_SPI5SEL\_Pos)

479

[ 480](numaker__m46x__clock_8h.md#a6f02c1ae7c7b709df8af90b8b32ebc73)#define NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_Pos)

[ 481](numaker__m46x__clock_8h.md#adc13b50c748385eb7d681d17dc11b2cc)#define NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_Pos)

[ 482](numaker__m46x__clock_8h.md#a4436fbda0d2fde16132e7f9c5b70ccfe)#define NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_Pos)

[ 483](numaker__m46x__clock_8h.md#a86134de3e0dd4a7f52f9952ec9cc9a54)#define NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL4\_SPI6SEL\_Pos)

484

[ 485](numaker__m46x__clock_8h.md#a49037df2c9b78d760a2eebf420fe6c8b)#define NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_Pos)

[ 486](numaker__m46x__clock_8h.md#ab532a55008e2e83147359909cf361107)#define NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_Pos)

[ 487](numaker__m46x__clock_8h.md#a53a4e1dee4e38b93e38a030466edf424)#define NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_Pos)

[ 488](numaker__m46x__clock_8h.md#aadde00be68631599399d380b29c7857f)#define NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL4\_SPI7SEL\_Pos)

489

[ 490](numaker__m46x__clock_8h.md#a427cb59c0f6dcb39cf08797c59c59256)#define NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_Pos)

[ 491](numaker__m46x__clock_8h.md#a46202f0420f33fe19aad2bd045d27585)#define NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_Pos)

[ 492](numaker__m46x__clock_8h.md#a8982cb3b8f566d0ed6e10382bd6d68e6)#define NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_Pos)

[ 493](numaker__m46x__clock_8h.md#accbf0d3921f7911520a406fbe1daa61a)#define NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL4\_SPI8SEL\_Pos)

494

[ 495](numaker__m46x__clock_8h.md#a31eae63ea888b7b147036a232e4465f8)#define NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_Pos)

[ 496](numaker__m46x__clock_8h.md#a5e568453ae38a4a3f1437189006d80e0)#define NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_Pos)

[ 497](numaker__m46x__clock_8h.md#a0e98bd4c3e1f06670e350b7d30a3edb7)#define NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_PCLK0 (0x2UL << NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_Pos)

[ 498](numaker__m46x__clock_8h.md#a8e8843f0cbd75f81bf4eaebe696f67bf)#define NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL4\_SPI9SEL\_Pos)

499

[ 500](numaker__m46x__clock_8h.md#ae4bc5a2e0d464d59fcd67f1b8768e9a0)#define NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_HXT (0x0UL << NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_Pos)

[ 501](numaker__m46x__clock_8h.md#a6830b1a49c4937b7f8a4ab5771e915b4)#define NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_PLL\_DIV2 (0x1UL << NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_Pos)

[ 502](numaker__m46x__clock_8h.md#a755c1325d17f55e0de754c687dbbc322)#define NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_PCLK1 (0x2UL << NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_Pos)

[ 503](numaker__m46x__clock_8h.md#a13fdfeb9c81a6794461c1e3e022780a0)#define NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_HIRC (0x3UL << NUMAKER\_CLK\_CLKSEL4\_SPI10SEL\_Pos)

504

505/\* CLKDIV0 constant definitions. \*/

506

[ 507](numaker__m46x__clock_8h.md#a7791710203e4af03f6f76b909c7b467c)#define NUMAKER\_CLK\_CLKDIV0\_HCLK(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV0\_HCLKDIV\_Pos)

[ 508](numaker__m46x__clock_8h.md#a6ea0c7b58fdbfff2d813f7859a3ac1cd)#define NUMAKER\_CLK\_CLKDIV0\_USB(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV0\_USBDIV\_Pos)

[ 509](numaker__m46x__clock_8h.md#a76b9c597c2cc89d992f2b705a1a9ec18)#define NUMAKER\_CLK\_CLKDIV0\_SDH0(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV0\_SDH0DIV\_Pos)

[ 510](numaker__m46x__clock_8h.md#a3c7cfbdf43433e075643b8e5f7d8dc5f)#define NUMAKER\_CLK\_CLKDIV0\_UART0(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV0\_UART0DIV\_Pos)

[ 511](numaker__m46x__clock_8h.md#aa44610811c5e62ed93cf91dc7925eb10)#define NUMAKER\_CLK\_CLKDIV0\_UART1(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV0\_UART1DIV\_Pos)

[ 512](numaker__m46x__clock_8h.md#a84bca9b50b18d2f260f637d7e58cb369)#define NUMAKER\_CLK\_CLKDIV0\_EADC0(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV0\_EADC0DIV\_Pos)

513

514/\* CLKDIV1 constant definitions. \*/

515

[ 516](numaker__m46x__clock_8h.md#aa32657011255cdbb44af8ebf41d38657)#define NUMAKER\_CLK\_CLKDIV1\_SC0(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV1\_SC0DIV\_Pos)

[ 517](numaker__m46x__clock_8h.md#ad9b81e35b2cafac307babbcf455244b0)#define NUMAKER\_CLK\_CLKDIV1\_SC1(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV1\_SC1DIV\_Pos)

[ 518](numaker__m46x__clock_8h.md#a038a62342904de71e466bef93b8efe27)#define NUMAKER\_CLK\_CLKDIV1\_SC2(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV1\_SC2DIV\_Pos)

[ 519](numaker__m46x__clock_8h.md#ab8b2208d1408ce0cd72763565a63092c)#define NUMAKER\_CLK\_CLKDIV1\_PSIO(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV1\_PSIODIV\_Pos)

520

521/\* CLKDIV2 constant definitions. \*/

522

[ 523](numaker__m46x__clock_8h.md#ad25d8e0adda00ccd42aa4debbd9a9042)#define NUMAKER\_CLK\_CLKDIV2\_I2S0(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV2\_I2S0DIV\_Pos)

[ 524](numaker__m46x__clock_8h.md#a51148f92b0b67a16fb270fd551ea89aa)#define NUMAKER\_CLK\_CLKDIV2\_I2S1(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV2\_I2S1DIV\_Pos)

[ 525](numaker__m46x__clock_8h.md#ab03c15f49e0ac48901c8e862b67ad91f)#define NUMAKER\_CLK\_CLKDIV2\_KPI(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV2\_KPIDIV\_Pos)

[ 526](numaker__m46x__clock_8h.md#aacfc89cba45ef5942a7316828ad8c670)#define NUMAKER\_CLK\_CLKDIV2\_EADC1(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV2\_EADC1DIV\_Pos)

527

528/\* CLKDIV3 constant definitions. \*/

529

[ 530](numaker__m46x__clock_8h.md#ac341868a272b7f0bfd246f5a665b4ffe)#define NUMAKER\_CLK\_CLKDIV3\_VSENSE(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV3\_VSENSEDIV\_Pos)

[ 531](numaker__m46x__clock_8h.md#afb15d4e0ae420f44430b07f2453dbcc5)#define NUMAKER\_CLK\_CLKDIV3\_EMAC0(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV3\_EMAC0DIV\_Pos)

[ 532](numaker__m46x__clock_8h.md#adb949fa1266754742211dab64b971a09)#define NUMAKER\_CLK\_CLKDIV3\_SDH1(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV3\_SDH1DIV\_Pos)

533

534/\* CLKDIV4 constant definitions. \*/

535

[ 536](numaker__m46x__clock_8h.md#a5a548de5d860e906f139858512608955)#define NUMAKER\_CLK\_CLKDIV4\_UART2(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV4\_UART2DIV\_Pos)

[ 537](numaker__m46x__clock_8h.md#aa10601c99a3fc178163dfa652bd2d934)#define NUMAKER\_CLK\_CLKDIV4\_UART3(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV4\_UART3DIV\_Pos)

[ 538](numaker__m46x__clock_8h.md#a2aaecc74fc40ead21b8ad38bf14fcd81)#define NUMAKER\_CLK\_CLKDIV4\_UART4(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV4\_UART4DIV\_Pos)

[ 539](numaker__m46x__clock_8h.md#a9444b25128c546730f2f95651d6a6d78)#define NUMAKER\_CLK\_CLKDIV4\_UART5(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV4\_UART5DIV\_Pos)

[ 540](numaker__m46x__clock_8h.md#a12b519bee17127c49d6aece4dcf9360a)#define NUMAKER\_CLK\_CLKDIV4\_UART6(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV4\_UART6DIV\_Pos)

[ 541](numaker__m46x__clock_8h.md#acadcdbe15918ca5478c17f30d417aa4a)#define NUMAKER\_CLK\_CLKDIV4\_UART7(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV4\_UART7DIV\_Pos)

542

543/\* CLKDIV5 constant definitions. \*/

544

[ 545](numaker__m46x__clock_8h.md#a225dfb2e0f8ce7ae299746ee4242e22f)#define NUMAKER\_CLK\_CLKDIV5\_CANFD0(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV5\_CANFD0DIV\_Pos)

[ 546](numaker__m46x__clock_8h.md#a67f5c63a1322683d74d56ee68c193cb4)#define NUMAKER\_CLK\_CLKDIV5\_CANFD1(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV5\_CANFD1DIV\_Pos)

[ 547](numaker__m46x__clock_8h.md#a5b10f7af05c3b67935a6f6eaa2aa6401)#define NUMAKER\_CLK\_CLKDIV5\_CANFD2(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV5\_CANFD2DIV\_Pos)

[ 548](numaker__m46x__clock_8h.md#ab857a9380f45415ee55b36cb57f7a835)#define NUMAKER\_CLK\_CLKDIV5\_CANFD3(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV5\_CANFD3DIV\_Pos)

[ 549](numaker__m46x__clock_8h.md#ae0ec95d4d59e16f2f2522ac750c06609)#define NUMAKER\_CLK\_CLKDIV5\_UART8(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV5\_UART8DIV\_Pos)

[ 550](numaker__m46x__clock_8h.md#a907216283187fc94ff9e36c7300f615f)#define NUMAKER\_CLK\_CLKDIV5\_UART9(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV5\_UART9DIV\_Pos)

[ 551](numaker__m46x__clock_8h.md#a1d34513b627cf8077fc0b9eb27d7d86a)#define NUMAKER\_CLK\_CLKDIV5\_EADC2(x) (((x)-1UL) << NUMAKER\_CLK\_CLKDIV5\_EADC2DIV\_Pos)

552

553/\* PCLKDIV constant definitions. \*/

554

[ 555](numaker__m46x__clock_8h.md#a4cd3514d3e28ef6e766c5f1f82282440)#define NUMAKER\_CLK\_PCLKDIV\_PCLK0DIV1 (0x0UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 556](numaker__m46x__clock_8h.md#afff3e78da346a4cfc396106aea619a84)#define NUMAKER\_CLK\_PCLKDIV\_PCLK0DIV2 (0x1UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 557](numaker__m46x__clock_8h.md#aca64a8e2c1414cc2448c51ae7e94db02)#define NUMAKER\_CLK\_PCLKDIV\_PCLK0DIV4 (0x2UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 558](numaker__m46x__clock_8h.md#af12f5adad50c241bb35e5846e3ddcc94)#define NUMAKER\_CLK\_PCLKDIV\_PCLK0DIV8 (0x3UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 559](numaker__m46x__clock_8h.md#a067cb901b89bf0940ac01236cd6ee514)#define NUMAKER\_CLK\_PCLKDIV\_PCLK0DIV16 (0x4UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 560](numaker__m46x__clock_8h.md#ab0a16daad92a2ffed7d37d8813053e5e)#define NUMAKER\_CLK\_PCLKDIV\_PCLK1DIV1 (0x0UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

[ 561](numaker__m46x__clock_8h.md#a19155e2c85834e6d67e884b8a541f98a)#define NUMAKER\_CLK\_PCLKDIV\_PCLK1DIV2 (0x1UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

[ 562](numaker__m46x__clock_8h.md#a657b489628d7d9cc801736b2da2087cc)#define NUMAKER\_CLK\_PCLKDIV\_PCLK1DIV4 (0x2UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

[ 563](numaker__m46x__clock_8h.md#a4fca0206e3bbfc0c52f0fd43aa733fcb)#define NUMAKER\_CLK\_PCLKDIV\_PCLK1DIV8 (0x3UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

[ 564](numaker__m46x__clock_8h.md#ac37e48036b1fcbd5f39acaf01316e840)#define NUMAKER\_CLK\_PCLKDIV\_PCLK1DIV16 (0x4UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

565

[ 566](numaker__m46x__clock_8h.md#a91226a1fd31413d76529f104d209823c)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV1 (0x0UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 567](numaker__m46x__clock_8h.md#a084853a709e714db6f49d45d45342d37)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV2 (0x1UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 568](numaker__m46x__clock_8h.md#a87a3393828150a62072a81dd58d2b80f)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV4 (0x2UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 569](numaker__m46x__clock_8h.md#a43013dc7b87074e5f7606a1e1ac14bce)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV8 (0x3UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 570](numaker__m46x__clock_8h.md#aac77daf4ae27aeab8c73177be5acdbe8)#define NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_DIV16 (0x4UL << NUMAKER\_CLK\_PCLKDIV\_APB0DIV\_Pos)

[ 571](numaker__m46x__clock_8h.md#af5199c68008764c41a3ce9ba27ea24e9)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV1 (0x0UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

[ 572](numaker__m46x__clock_8h.md#af6cb3de51e49729e92044287ed499105)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV2 (0x1UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

[ 573](numaker__m46x__clock_8h.md#a8e63b55ca8e84958230453a54f3983b2)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV4 (0x2UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

[ 574](numaker__m46x__clock_8h.md#a8e59ceb6473e9a050af9efeeeb79c72a)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV8 (0x3UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

[ 575](numaker__m46x__clock_8h.md#a8e7dec640447de9b571147cbe7fe6e26)#define NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_DIV16 (0x4UL << NUMAKER\_CLK\_PCLKDIV\_APB1DIV\_Pos)

576

577/\* MODULE constant definitions. \*/

578

579/\*

580 \* APBCLK(31:29)|CLKSEL(28:26)|CLKSEL\_Msk(25:22)|CLKSEL\_Pos(21:17)|CLKDIV(16:14)|

581 \* CLKDIV\_Msk(13:10)|CLKDIV\_Pos(9:5)|IP\_EN\_Pos(4:0)

582 \*/

583

[ 584](numaker__m46x__clock_8h.md#a6dd2c25defa8fa66e7e72aa111f1ee02)#define NUMAKER\_MODULE\_NoMsk 0x0UL

[ 585](numaker__m46x__clock_8h.md#a922f9d60a8929a9ea5139e1da86d5387)#define NUMAKER\_NA NUMAKER\_MODULE\_NoMsk

586

[ 587](numaker__m46x__clock_8h.md#aafa8852333e620f24f98d98d27420788)#define NUMAKER\_MODULE\_APBCLK\_ENC(x) (((x)&0x07UL) << 29)

[ 588](numaker__m46x__clock_8h.md#ad1fc2bf50be3ade92c4d51aceb460890)#define NUMAKER\_MODULE\_CLKSEL\_ENC(x) (((x)&0x07UL) << 26)

[ 589](numaker__m46x__clock_8h.md#aa499dc56e839cf41404faa352c80a526)#define NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(x) (((x)&0x0fUL) << 22)

[ 590](numaker__m46x__clock_8h.md#a649f7ee2853b623d1b9479cbb191b260)#define NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(x) (((x)&0x1fUL) << 17)

[ 591](numaker__m46x__clock_8h.md#adc57f655a02127165185c3a6a5453541)#define NUMAKER\_MODULE\_CLKDIV\_ENC(x) (((x)&0x07UL) << 14)

[ 592](numaker__m46x__clock_8h.md#aa18f25c62b95c9b5691b23a8b3ce87a0)#define NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(x) (((x)&0x0fUL) << 10)

[ 593](numaker__m46x__clock_8h.md#abbf6921f1302337ed1a46886e6517285)#define NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(x) (((x)&0x1fUL) << 5)

[ 594](numaker__m46x__clock_8h.md#acdd40f56d4640d677c4001a6e9e35f63)#define NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(x) (((x)&0x1fUL) << 0)

595

596/\* AHBCLK0 \*/

[ 597](numaker__m46x__clock_8h.md#a81c0a35692befb3b0427efc7a1e2686e)#define NUMAKER\_PDMA0\_MODULE \

598 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

599 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_PDMA0CKEN\_Pos) | \

600 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

601 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

602 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

603

[ 604](numaker__m46x__clock_8h.md#a9e1a03d652040f0e3d9c0766bfdb2604)#define NUMAKER\_ISP\_MODULE \

605 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

606 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_ISPCKEN\_Pos) | \

607 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

608 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

609 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

610

[ 611](numaker__m46x__clock_8h.md#a4380f8998993e0ea2d85260fb9dd8200)#define NUMAKER\_EBI\_MODULE \

612 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

613 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_EBICKEN\_Pos) | \

614 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

615 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

616 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

617

[ 618](numaker__m46x__clock_8h.md#a3e379c3d426c06b772e848633767d2e5)#define NUMAKER\_ST\_MODULE \

619 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

620 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_STCKEN\_Pos) | \

621 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

622 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

623 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

624

[ 625](numaker__m46x__clock_8h.md#a982967caa2c7f9eac528120a94d10bf5)#define NUMAKER\_EMAC0\_MODULE \

626 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

627 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_EMAC0CKEN\_Pos) | \

628 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

629 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(3UL) | \

630 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(16UL))

631

[ 632](numaker__m46x__clock_8h.md#aac1289976a442b2fedb1233b15982ae0)#define NUMAKER\_SDH0\_MODULE \

633 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

634 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_SDH0CKEN\_Pos) | \

635 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

636 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(20UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(0UL) | \

637 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(24UL))

638

[ 639](numaker__m46x__clock_8h.md#af7f021090417dc8ba8eac4b2674cf8b8)#define NUMAKER\_CRC\_MODULE \

640 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

641 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_CRCCKEN\_Pos) | \

642 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

643 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

644 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

645

[ 646](numaker__m46x__clock_8h.md#acb6254a4cc244665d416934d3022128a)#define NUMAKER\_CCAP\_MODULE \

647 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

648 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_CCAPCKEN\_Pos) | \

649 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

650 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

651 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

652

[ 653](numaker__m46x__clock_8h.md#a05f1316adcadb329b721d688c122f765)#define NUMAKER\_SEN\_MODULE \

654 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

655 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_SENCKEN\_Pos) | \

656 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

657 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(16UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(3UL) | \

658 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(8UL))

659

[ 660](numaker__m46x__clock_8h.md#a94ca074cf142aae599f5061e25a0390f)#define NUMAKER\_HSUSBD\_MODULE \

661 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

662 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_HSUSBDCKEN\_Pos) | \

663 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

664 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

665 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

666

[ 667](numaker__m46x__clock_8h.md#a6cd417a41929491e83bed7bab4319e34)#define NUMAKER\_HBI\_MODULE \

668 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

669 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_HBICKEN\_Pos) | \

670 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

671 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

672 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

673

[ 674](numaker__m46x__clock_8h.md#a7a2da068169709e20c06f2962569bc46)#define NUMAKER\_CRPT\_MODULE \

675 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

676 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_CRPTCKEN\_Pos) | \

677 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

678 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

679 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

680

[ 681](numaker__m46x__clock_8h.md#a3b983a5a538bbf7b2e6288beacfb5427)#define NUMAKER\_KS\_MODULE \

682 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

683 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_KSCKEN\_Pos) | \

684 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

685 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

686 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

687

[ 688](numaker__m46x__clock_8h.md#a2aad906d9be605b1ed9877a203e01722)#define NUMAKER\_SPIM\_MODULE \

689 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

690 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_SPIMCKEN\_Pos) | \

691 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

692 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

693 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

694

[ 695](numaker__m46x__clock_8h.md#a5f0a8a97c7fa707043ff4f90837c218a)#define NUMAKER\_FMCIDLE\_MODULE \

696 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

697 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_FMCIDLE\_Pos) | \

698 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

699 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

700 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

701

[ 702](numaker__m46x__clock_8h.md#a43b0b287abedfd2b9c78857bb0004be9)#define NUMAKER\_USBH\_MODULE \

703 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

704 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_USBHCKEN\_Pos) | \

705 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(1UL) | \

706 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(8UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(0UL) | \

707 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0xFUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(4UL))

708

[ 709](numaker__m46x__clock_8h.md#a5ee10e118573a4c747d9c0712e5adede)#define NUMAKER\_SDH1\_MODULE \

710 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

711 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_SDH1CKEN\_Pos) | \

712 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

713 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(22UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(3UL) | \

714 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(24UL))

715

[ 716](numaker__m46x__clock_8h.md#a9bd6ce359c452c822a59a6f0da68c7d0)#define NUMAKER\_PDMA1\_MODULE \

717 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

718 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_PDMA1CKEN\_Pos) | \

719 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

720 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

721 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

722

[ 723](numaker__m46x__clock_8h.md#ab68674b62e1c8a26f80772a9add2fcf7)#define NUMAKER\_TRACE\_MODULE \

724 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

725 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_TRACECKEN\_Pos) | \

726 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

727 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

728 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

729

[ 730](numaker__m46x__clock_8h.md#a106a0eb0dac7825f2b6b05a0329c6a3a)#define NUMAKER\_GPA\_MODULE \

731 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

732 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_GPACKEN\_Pos) | \

733 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

734 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

735 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

736

[ 737](numaker__m46x__clock_8h.md#a922653d8eb98a7a175366566506834d6)#define NUMAKER\_GPB\_MODULE \

738 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

739 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_GPBCKEN\_Pos) | \

740 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

741 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

742 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

743

[ 744](numaker__m46x__clock_8h.md#a9daa2cdbc788c5e5f3e4cbe29169816f)#define NUMAKER\_GPC\_MODULE \

745 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

746 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_GPCCKEN\_Pos) | \

747 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

748 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

749 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

750

[ 751](numaker__m46x__clock_8h.md#a277e860c7fdd493a496900c32b6085f7)#define NUMAKER\_GPD\_MODULE \

752 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

753 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_GPDCKEN\_Pos) | \

754 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

755 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

756 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

757

[ 758](numaker__m46x__clock_8h.md#a7a5abf84843eb843233e2f24323559f3)#define NUMAKER\_GPE\_MODULE \

759 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

760 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_GPECKEN\_Pos) | \

761 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

762 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

763 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

764

[ 765](numaker__m46x__clock_8h.md#a19540c109f7a0e276ad7f7f52faf6c7e)#define NUMAKER\_GPF\_MODULE \

766 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

767 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_GPFCKEN\_Pos) | \

768 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

769 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

770 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

771

[ 772](numaker__m46x__clock_8h.md#ad377845a8b368f1b1b6d20f6629dcdd3)#define NUMAKER\_GPG\_MODULE \

773 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

774 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_GPGCKEN\_Pos) | \

775 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

776 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

777 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

778

[ 779](numaker__m46x__clock_8h.md#a74e2344ff20eec0e1ccbd137d75183fb)#define NUMAKER\_GPH\_MODULE \

780 (NUMAKER\_MODULE\_APBCLK\_ENC(0UL) | \

781 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK0\_GPHCKEN\_Pos) | \

782 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

783 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

784 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

785

786/\* AHBCLK1 \*/

[ 787](numaker__m46x__clock_8h.md#aec648b50b3e87890e01766e735130d34)#define NUMAKER\_CANFD0\_MODULE \

788 (NUMAKER\_MODULE\_APBCLK\_ENC(4UL) | \

789 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK1\_CANFD0CKEN\_Pos) | \

790 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

791 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(24UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(5UL) | \

792 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(0UL))

793

[ 794](numaker__m46x__clock_8h.md#a4cf36800f445d6eab593a8838285d913)#define NUMAKER\_CANFD1\_MODULE \

795 (NUMAKER\_MODULE\_APBCLK\_ENC(4UL) | \

796 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK1\_CANFD1CKEN\_Pos) | \

797 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

798 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(26UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(5UL) | \

799 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(4UL))

800

[ 801](numaker__m46x__clock_8h.md#a6385023e2b2d645f347a7d04f3686e65)#define NUMAKER\_CANFD2\_MODULE \

802 (NUMAKER\_MODULE\_APBCLK\_ENC(4UL) | \

803 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK1\_CANFD2CKEN\_Pos) | \

804 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

805 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(28UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(5UL) | \

806 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(8UL))

807

[ 808](numaker__m46x__clock_8h.md#af956a53c2db2138d4cc1625d48f065c5)#define NUMAKER\_CANFD3\_MODULE \

809 (NUMAKER\_MODULE\_APBCLK\_ENC(4UL) | \

810 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK1\_CANFD3CKEN\_Pos) | \

811 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

812 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(30UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(5UL) | \

813 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(12UL))

814

[ 815](numaker__m46x__clock_8h.md#a8fd7ed7ba36e7293edcd9f0fe511f5d2)#define NUMAKER\_GPI\_MODULE \

816 (NUMAKER\_MODULE\_APBCLK\_ENC(4UL) | \

817 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK1\_GPICKEN\_Pos) | \

818 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

819 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

820 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

821

[ 822](numaker__m46x__clock_8h.md#a67adfb2ff0a39fd0615a9a3fb562f2bc)#define NUMAKER\_GPJ\_MODULE \

823 (NUMAKER\_MODULE\_APBCLK\_ENC(4UL) | \

824 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK1\_GPJCKEN\_Pos) | \

825 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

826 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

827 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

828

[ 829](numaker__m46x__clock_8h.md#a63a4d8cb621e8c4ee32de0276c36085e)#define NUMAKER\_BMC\_MODULE \

830 (NUMAKER\_MODULE\_APBCLK\_ENC(4UL) | \

831 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_AHBCLK1\_BMCCKEN\_Pos) | \

832 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

833 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

834 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

835

836/\* APBCLK0 \*/

[ 837](numaker__m46x__clock_8h.md#a963952cad9b6b670e736875be75328e2)#define NUMAKER\_WDT\_MODULE \

838 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

839 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_WDTCKEN\_Pos) | \

840 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

841 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(0UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

842 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

843

[ 844](numaker__m46x__clock_8h.md#a531cdddd54f1c2a56d603b9135348e0f)#define NUMAKER\_WWDT\_MODULE \

845 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

846 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_WDTCKEN\_Pos) | \

847 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

848 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(30UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

849 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

850

[ 851](numaker__m46x__clock_8h.md#a6216a664ac302a57a0b632754c3fce5f)#define NUMAKER\_RTC\_MODULE \

852 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

853 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_RTCCKEN\_Pos) | \

854 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

855 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

856 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

857

[ 858](numaker__m46x__clock_8h.md#adaec43e184ed7f3c34f66b4e98041f62)#define NUMAKER\_TMR0\_MODULE \

859 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

860 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_TMR0CKEN\_Pos) | \

861 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

862 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(8UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

863 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

864

[ 865](numaker__m46x__clock_8h.md#a50c780a3f2c07cc2dfca1e647e83782d)#define NUMAKER\_TMR1\_MODULE \

866 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

867 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_TMR1CKEN\_Pos) | \

868 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

869 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(12UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

870 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

871

[ 872](numaker__m46x__clock_8h.md#a7a60853a52958a5c8a78e383f378f579)#define NUMAKER\_TMR2\_MODULE \

873 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

874 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_TMR2CKEN\_Pos) | \

875 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

876 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(16UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

877 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

878

[ 879](numaker__m46x__clock_8h.md#a42fd788548168d2b519f5d49d2eead47)#define NUMAKER\_TMR3\_MODULE \

880 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

881 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_TMR3CKEN\_Pos) | \

882 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

883 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(20UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

884 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

885

[ 886](numaker__m46x__clock_8h.md#a913b0eed144c8d228a461dec3f0b49e6)#define NUMAKER\_CLKO\_MODULE \

887 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

888 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_CLKOCKEN\_Pos) | \

889 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

890 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(4UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

891 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

892

[ 893](numaker__m46x__clock_8h.md#abe18bfc9e64be82d3734d80a69e2541c)#define NUMAKER\_ACMP01\_MODULE \

894 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

895 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_ACMP01CKEN\_Pos) | \

896 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

897 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

898 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

899

[ 900](numaker__m46x__clock_8h.md#a8241dce3f2329ef3561277656bd68e7f)#define NUMAKER\_I2C0\_MODULE \

901 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

902 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_I2C0CKEN\_Pos) | \

903 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

904 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

905 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

906

[ 907](numaker__m46x__clock_8h.md#a08413ee5eed011e452f7352a276b45af)#define NUMAKER\_I2C1\_MODULE \

908 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

909 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_I2C1CKEN\_Pos) | \

910 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

911 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

912 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

913

[ 914](numaker__m46x__clock_8h.md#a211a7c416249dad417b5971a4c8526fe)#define NUMAKER\_I2C2\_MODULE \

915 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

916 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_I2C2CKEN\_Pos) | \

917 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

918 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

919 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

920

[ 921](numaker__m46x__clock_8h.md#a0660bb6481a262632fdfd08f4c65c1db)#define NUMAKER\_I2C3\_MODULE \

922 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

923 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_I2C3CKEN\_Pos) | \

924 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

925 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

926 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

927

[ 928](numaker__m46x__clock_8h.md#a6dad02cb850ad26c2afde2291d669808)#define NUMAKER\_QSPI0\_MODULE \

929 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

930 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_QSPI0CKEN\_Pos) | \

931 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

932 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(2UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

933 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

934

[ 935](numaker__m46x__clock_8h.md#adaa689295a31e5b259a7c05b6611a125)#define NUMAKER\_SPI0\_MODULE \

936 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

937 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_SPI0CKEN\_Pos) | \

938 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

939 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(4UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

940 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

941

[ 942](numaker__m46x__clock_8h.md#a144be66983b8b45995a7b037681477e7)#define NUMAKER\_SPI1\_MODULE \

943 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

944 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_SPI1CKEN\_Pos) | \

945 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

946 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(12UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

947 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

948

[ 949](numaker__m46x__clock_8h.md#a227a44ce55b040227bfe3233cfd63467)#define NUMAKER\_SPI2\_MODULE \

950 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

951 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_SPI2CKEN\_Pos) | \

952 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

953 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(9UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

954 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

955

[ 956](numaker__m46x__clock_8h.md#aaf0220a2af6dd7368761bf753ae7b73e)#define NUMAKER\_UART0\_MODULE \

957 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

958 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_UART0CKEN\_Pos) | \

959 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

960 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(24UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(0UL) | \

961 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(8UL))

962

[ 963](numaker__m46x__clock_8h.md#a38d069ddfd9912c38c42a8f7e3ead763)#define NUMAKER\_UART1\_MODULE \

964 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

965 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_UART1CKEN\_Pos) | \

966 NUMAKER\_MODULE\_CLKSEL\_ENC(1UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

967 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(26UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(0UL) | \

968 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(12UL))

969

[ 970](numaker__m46x__clock_8h.md#aa6dbc85be07f392f38a88bc074f11046)#define NUMAKER\_UART2\_MODULE \

971 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

972 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_UART2CKEN\_Pos) | \

973 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

974 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(24UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(4UL) | \

975 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(0UL))

976

[ 977](numaker__m46x__clock_8h.md#a98c5368b7868f6bc68e09df7f479be73)#define NUMAKER\_UART3\_MODULE \

978 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

979 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_UART3CKEN\_Pos) | \

980 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

981 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(26UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(4UL) | \

982 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(4UL))

983

[ 984](numaker__m46x__clock_8h.md#a0045544d52c292c13edb09e90f4b16c8)#define NUMAKER\_UART4\_MODULE \

985 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

986 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_UART4CKEN\_Pos) | \

987 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

988 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(28UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(4UL) | \

989 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(8UL))

990

[ 991](numaker__m46x__clock_8h.md#a0fdf72d7961da9c046d7d4bb9e19cf1f)#define NUMAKER\_UART5\_MODULE \

992 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

993 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_UART5CKEN\_Pos) | \

994 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

995 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(30UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(4UL) | \

996 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(12UL))

997

[ 998](numaker__m46x__clock_8h.md#aa4081c973118f02b92299ea8d775a1e5)#define NUMAKER\_UART6\_MODULE \

999 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

1000 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_UART6CKEN\_Pos) | \

1001 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1002 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(20UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(4UL) | \

1003 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(16UL))

1004

[ 1005](numaker__m46x__clock_8h.md#a86caba0b690236e26e440bc39e4bf4c9)#define NUMAKER\_UART7\_MODULE \

1006 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

1007 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_UART7CKEN\_Pos) | \

1008 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1009 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(22UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(4UL) | \

1010 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(20UL))

1011

[ 1012](numaker__m46x__clock_8h.md#ac504259898b6070a12ca5a8eed921e17)#define NUMAKER\_OTG\_MODULE \

1013 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

1014 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_OTGCKEN\_Pos) | \

1015 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(1UL) | \

1016 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(8UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(0UL) | \

1017 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0xFUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(4UL))

1018

[ 1019](numaker__m46x__clock_8h.md#aa751a53c366beda2ac9b3f5169cd4ace)#define NUMAKER\_USBD\_MODULE \

1020 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

1021 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_USBDCKEN\_Pos) | \

1022 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(1UL) | \

1023 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(8UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(0UL) | \

1024 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0xFUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(4UL))

1025

[ 1026](numaker__m46x__clock_8h.md#a46a5cffa974b2f1425d2ced8e678c3e2)#define NUMAKER\_EADC0\_MODULE \

1027 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

1028 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_EADC0CKEN\_Pos) | \

1029 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1030 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(10UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(0UL) | \

1031 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(16UL))

1032

[ 1033](numaker__m46x__clock_8h.md#a93460f284274121252ffaf3ca48510e5)#define NUMAKER\_I2S0\_MODULE \

1034 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

1035 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_I2S0CKEN\_Pos) | \

1036 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1037 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(16UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(2UL) | \

1038 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(0UL))

1039

[ 1040](numaker__m46x__clock_8h.md#a4a0086f1b2bed74585826d07d8fdc971)#define NUMAKER\_HSOTG\_MODULE \

1041 (NUMAKER\_MODULE\_APBCLK\_ENC(1UL) | \

1042 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK0\_HSOTGCKEN\_Pos) | \

1043 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1044 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1045 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1046

1047/\* APBCLK1 \*/

[ 1048](numaker__m46x__clock_8h.md#ade881cb3ef71ab90bc655c5775f4b5f2)#define NUMAKER\_SC0\_MODULE \

1049 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1050 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_SC0CKEN\_Pos) | \

1051 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1052 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(0UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(1UL) | \

1053 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(0UL))

1054

[ 1055](numaker__m46x__clock_8h.md#a183b62952b0a65cd91e9f8f43bbc85d5)#define NUMAKER\_SC1\_MODULE \

1056 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1057 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_SC1CKEN\_Pos) | \

1058 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1059 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(2UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(1UL) | \

1060 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(8UL))

1061

[ 1062](numaker__m46x__clock_8h.md#aac46396a96d07b982ea79848109c8df5)#define NUMAKER\_SC2\_MODULE \

1063 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1064 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_SC2CKEN\_Pos) | \

1065 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1066 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(4UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(1UL) | \

1067 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(16UL))

1068

[ 1069](numaker__m46x__clock_8h.md#a39ddacc5770039457425f67567bfbf0b)#define NUMAKER\_I2C4\_MODULE \

1070 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1071 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_I2C4CKEN\_Pos) | \

1072 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1073 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1074 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1075

[ 1076](numaker__m46x__clock_8h.md#a38cb7b22e41b081d55f594b4b5812fc4)#define NUMAKER\_QSPI1\_MODULE \

1077 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1078 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_QSPI1CKEN\_Pos) | \

1079 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1080 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(10UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1081 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1082

[ 1083](numaker__m46x__clock_8h.md#aa251c8b6a225d24b4e3f20dd22498b79)#define NUMAKER\_SPI3\_MODULE \

1084 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1085 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_SPI3CKEN\_Pos) | \

1086 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1087 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(12UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1088 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1089

[ 1090](numaker__m46x__clock_8h.md#a56a76adf61a24f812f18e13534405106)#define NUMAKER\_SPI4\_MODULE \

1091 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1092 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_SPI4CKEN\_Pos) | \

1093 NUMAKER\_MODULE\_CLKSEL\_ENC(4UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1094 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(0UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1095 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1096

[ 1097](numaker__m46x__clock_8h.md#a96da4a8ec09af3cbf8ab34e1bccb7819)#define NUMAKER\_USCI0\_MODULE \

1098 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1099 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_USCI0CKEN\_Pos) | \

1100 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1101 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1102 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1103

[ 1104](numaker__m46x__clock_8h.md#aa1455b010fdbd2f07815cdeeaf49907a)#define NUMAKER\_PSIO\_MODULE \

1105 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1106 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_PSIOCKEN\_Pos) | \

1107 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1108 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(28UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(1UL) | \

1109 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(24UL))

1110

[ 1111](numaker__m46x__clock_8h.md#a9a5f7dc5dfa877dd92f3952ce7315ba8)#define NUMAKER\_DAC\_MODULE \

1112 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1113 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_DACCKEN\_Pos) | \

1114 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1115 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1116 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1117

[ 1118](numaker__m46x__clock_8h.md#a6f1eccd8218399311b9854c7b84185ea)#define NUMAKER\_ECAP2\_MODULE \

1119 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1120 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_ECAP2CKEN\_Pos) | \

1121 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1122 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1123 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1124

[ 1125](numaker__m46x__clock_8h.md#a2cd99780f8545b94483180123aedb756)#define NUMAKER\_ECAP3\_MODULE \

1126 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1127 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_ECAP3CKEN\_Pos) | \

1128 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1129 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1130 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1131

[ 1132](numaker__m46x__clock_8h.md#ab42a9a75250104163dab040657beb440)#define NUMAKER\_EPWM0\_MODULE \

1133 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1134 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_EPWM0CKEN\_Pos) | \

1135 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(1UL) | \

1136 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(0UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1137 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1138

[ 1139](numaker__m46x__clock_8h.md#a686fa9f9995ef124c47ce20de165b74d)#define NUMAKER\_EPWM1\_MODULE \

1140 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1141 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_EPWM1CKEN\_Pos) | \

1142 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(1UL) | \

1143 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(1UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1144 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1145

[ 1146](numaker__m46x__clock_8h.md#a357c036321109c1962abd936c52bc241)#define NUMAKER\_BPWM0\_MODULE \

1147 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1148 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_BPWM0CKEN\_Pos) | \

1149 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(1UL) | \

1150 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(8UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1151 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1152

[ 1153](numaker__m46x__clock_8h.md#a0e2a179864ee42ef88d014d068712aee)#define NUMAKER\_BPWM1\_MODULE \

1154 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1155 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_BPWM1CKEN\_Pos) | \

1156 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(1UL) | \

1157 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(9UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1158 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1159

[ 1160](numaker__m46x__clock_8h.md#a4fe52c877b603a575a230d3de64d2f45)#define NUMAKER\_EQEI0\_MODULE \

1161 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1162 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_EQEI0CKEN\_Pos) | \

1163 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1164 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1165 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1166

[ 1167](numaker__m46x__clock_8h.md#a446b5934e374a30377594e63423018b1)#define NUMAKER\_EQEI1\_MODULE \

1168 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1169 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_EQEI1CKEN\_Pos) | \

1170 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1171 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1172 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1173

[ 1174](numaker__m46x__clock_8h.md#a062009660b6134f8b288eff5a498566c)#define NUMAKER\_EQEI2\_MODULE \

1175 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1176 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_EQEI2CKEN\_Pos) | \

1177 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1178 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1179 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1180

[ 1181](numaker__m46x__clock_8h.md#ab2f4ab88554aee61bdd944ea3d4edd3f)#define NUMAKER\_EQEI3\_MODULE \

1182 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1183 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_EQEI3CKEN\_Pos) | \

1184 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1185 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1186 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1187

[ 1188](numaker__m46x__clock_8h.md#a7b544eadd5c042e91ea89541fd9431f6)#define NUMAKER\_TRNG\_MODULE \

1189 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1190 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_TRNGCKEN\_Pos) | \

1191 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(1UL) | \

1192 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(27UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1193 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1194

[ 1195](numaker__m46x__clock_8h.md#afcd2263655b3f52378ee24f2f8bfc0d6)#define NUMAKER\_ECAP0\_MODULE \

1196 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1197 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_ECAP0CKEN\_Pos) | \

1198 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1199 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1200 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1201

[ 1202](numaker__m46x__clock_8h.md#a43cc65940b5464683c572c94650a58e9)#define NUMAKER\_ECAP1\_MODULE \

1203 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1204 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_ECAP1CKEN\_Pos) | \

1205 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1206 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1207 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1208

[ 1209](numaker__m46x__clock_8h.md#aa1bcd301211aae3a1ae668af74ee58f6)#define NUMAKER\_I2S1\_MODULE \

1210 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1211 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_I2S1CKEN\_Pos) | \

1212 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1213 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(16UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(2UL) | \

1214 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(4UL))

1215

[ 1216](numaker__m46x__clock_8h.md#afe88f0224f22993a2e38a57b0cbc3e4f)#define NUMAKER\_EADC1\_MODULE \

1217 (NUMAKER\_MODULE\_APBCLK\_ENC(2UL) | \

1218 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK1\_EADC1CKEN\_Pos) | \

1219 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1220 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(12UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1221 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1222

1223/\* APBCLK2 \*/

[ 1224](numaker__m46x__clock_8h.md#ad194e1ddf64d6d4e59ee7c62ab3330a9)#define NUMAKER\_KPI\_MODULE \

1225 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1226 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_KPICKEN\_Pos) | \

1227 NUMAKER\_MODULE\_CLKSEL\_ENC(3UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1228 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(6UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(2UL) | \

1229 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(8UL))

1230

[ 1231](numaker__m46x__clock_8h.md#a77f267351914a668aa66e1e20bdd76c6)#define NUMAKER\_EADC2\_MODULE \

1232 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1233 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_EADC2CKEN\_Pos) | \

1234 NUMAKER\_MODULE\_CLKSEL\_ENC(0UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1235 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(14UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(2UL) | \

1236 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(24UL))

1237

[ 1238](numaker__m46x__clock_8h.md#a655d49dd28c77605c8a071b78eee9e15)#define NUMAKER\_ACMP23\_MODULE \

1239 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1240 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_ACMP23CKEN\_Pos) | \

1241 NUMAKER\_MODULE\_CLKSEL\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(NUMAKER\_NA) | \

1242 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1243 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1244

[ 1245](numaker__m46x__clock_8h.md#a57178e2899985344ea021f32efa43c20)#define NUMAKER\_SPI5\_MODULE \

1246 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1247 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_SPI5CKEN\_Pos) | \

1248 NUMAKER\_MODULE\_CLKSEL\_ENC(4UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1249 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(4UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1250 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1251

[ 1252](numaker__m46x__clock_8h.md#a39bbcd5b0f7175757fcc6dd523df1eb6)#define NUMAKER\_SPI6\_MODULE \

1253 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1254 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_SPI6CKEN\_Pos) | \

1255 NUMAKER\_MODULE\_CLKSEL\_ENC(4UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1256 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(8UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1257 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1258

[ 1259](numaker__m46x__clock_8h.md#ace0d844db14edd1e5f4b250281438206)#define NUMAKER\_SPI7\_MODULE \

1260 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1261 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_SPI7CKEN\_Pos) | \

1262 NUMAKER\_MODULE\_CLKSEL\_ENC(4UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1263 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(12UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1264 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1265

[ 1266](numaker__m46x__clock_8h.md#a47f43cb3ccd9192fa3d0f34b365fd81e)#define NUMAKER\_SPI8\_MODULE \

1267 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1268 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_SPI8CKEN\_Pos) | \

1269 NUMAKER\_MODULE\_CLKSEL\_ENC(4UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1270 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(16UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1271 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1272

[ 1273](numaker__m46x__clock_8h.md#abaf1f5fc92d1f9502fffbef8cf1715bd)#define NUMAKER\_SPI9\_MODULE \

1274 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1275 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_SPI9CKEN\_Pos) | \

1276 NUMAKER\_MODULE\_CLKSEL\_ENC(4UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1277 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(20UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1278 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1279

[ 1280](numaker__m46x__clock_8h.md#a9c5987ca481ecfbf505082335630402d)#define NUMAKER\_SPI10\_MODULE \

1281 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1282 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_SPI10CKEN\_Pos) | \

1283 NUMAKER\_MODULE\_CLKSEL\_ENC(4UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(7UL) | \

1284 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(24UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(NUMAKER\_NA) | \

1285 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(NUMAKER\_NA) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(NUMAKER\_NA))

1286

[ 1287](numaker__m46x__clock_8h.md#a30c536594814a2d4c58d383469a91081)#define NUMAKER\_UART8\_MODULE \

1288 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1289 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_UART8CKEN\_Pos) | \

1290 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1291 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(20UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(5UL) | \

1292 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(16UL))

1293

[ 1294](numaker__m46x__clock_8h.md#a87e45a8420e6329f101f564e08f896b2)#define NUMAKER\_UART9\_MODULE \

1295 (NUMAKER\_MODULE\_APBCLK\_ENC(3UL) | \

1296 NUMAKER\_MODULE\_IP\_EN\_Pos\_ENC(NUMAKER\_CLK\_APBCLK2\_UART9CKEN\_Pos) | \

1297 NUMAKER\_MODULE\_CLKSEL\_ENC(2UL) | NUMAKER\_MODULE\_CLKSEL\_Msk\_ENC(3UL) | \

1298 NUMAKER\_MODULE\_CLKSEL\_Pos\_ENC(22UL) | NUMAKER\_MODULE\_CLKDIV\_ENC(5UL) | \

1299 NUMAKER\_MODULE\_CLKDIV\_Msk\_ENC(0x0FUL) | NUMAKER\_MODULE\_CLKDIV\_Pos\_ENC(20UL))

1300

1301/\* End of M460 BSP clk.h copy \*/

1302

1303#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [numaker\_m46x\_clock.h](numaker__m46x__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
