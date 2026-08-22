---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/numaker__m55m1x__clock_8h_source.html
original_path: doxygen/html/numaker__m55m1x__clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numaker\_m55m1x\_clock.h

[Go to the documentation of this file.](numaker__m55m1x__clock_8h.md)

1/\*

2 \* Copyright (c) 2025 Nuvoton Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NUMAKER\_M55M1X\_CLOCK\_H

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_NUMAKER\_M55M1X\_CLOCK\_H

9

[ 10](numaker__m55m1x__clock_8h.md#a3474a1b62d1742e4d684580947a939e0)#define NUMAKER\_CLK\_SCLKSEL\_SCLKSEL\_HIRC 0x00000000

[ 11](numaker__m55m1x__clock_8h.md#ab26276bfef5b9dfd8e056da0283197a1)#define NUMAKER\_CLK\_SCLKSEL\_SCLKSEL\_MIRC 0x00000001

[ 12](numaker__m55m1x__clock_8h.md#aea6b724a70e9042c15c491c5e2aa018c)#define NUMAKER\_CLK\_SCLKSEL\_SCLKSEL\_HIRC48M 0x00000002

[ 13](numaker__m55m1x__clock_8h.md#af31eb9dd7fd71f4c740850bf85addc36)#define NUMAKER\_CLK\_SCLKSEL\_SCLKSEL\_HXT 0x00000003

[ 14](numaker__m55m1x__clock_8h.md#a95415c44d8f00f259eb0b4c44a18d7a8)#define NUMAKER\_CLK\_SCLKSEL\_SCLKSEL\_APLL0 0x00000004

[ 15](numaker__m55m1x__clock_8h.md#a48bf1ac56646d8df80c4e7973dd03e9d)#define NUMAKER\_CLK\_BPWMSEL\_BPWM0SEL\_PCLK0 0x00000000

[ 16](numaker__m55m1x__clock_8h.md#a6b03d826f79368c4c49ad35df11cbf8a)#define NUMAKER\_CLK\_BPWMSEL\_BPWM0SEL\_HCLK0 0x00000001

[ 17](numaker__m55m1x__clock_8h.md#abe224fbf569f84950c32c603c76dfac6)#define NUMAKER\_CLK\_BPWMSEL\_BPWM1SEL\_PCLK2 0x00000000

[ 18](numaker__m55m1x__clock_8h.md#aafb44329422be3f51ebc8419eb0ab71a)#define NUMAKER\_CLK\_BPWMSEL\_BPWM1SEL\_HCLK0 0x00000010

[ 19](numaker__m55m1x__clock_8h.md#af2625310e0d0cec1f48fd5502f2136f6)#define NUMAKER\_CLK\_CANFDSEL\_CANFD0SEL\_HXT 0x00000000

[ 20](numaker__m55m1x__clock_8h.md#a5fb2b4ec66f1aab0c36fe91e1946d195)#define NUMAKER\_CLK\_CANFDSEL\_CANFD0SEL\_APLL0\_DIV2 0x00000001

[ 21](numaker__m55m1x__clock_8h.md#a8227891715affd039a670fd85e0826b3)#define NUMAKER\_CLK\_CANFDSEL\_CANFD0SEL\_HCLK0 0x00000002

[ 22](numaker__m55m1x__clock_8h.md#a4946bc6b78a96ddfe6262a154acbb48d)#define NUMAKER\_CLK\_CANFDSEL\_CANFD0SEL\_HIRC 0x00000003

[ 23](numaker__m55m1x__clock_8h.md#aa8608554902849754a8ac83e0c24b2c5)#define NUMAKER\_CLK\_CANFDSEL\_CANFD0SEL\_HIRC48M\_DIV4 0x00000004

[ 24](numaker__m55m1x__clock_8h.md#a337f6ea2b9b62d1c56f2af3e761480d7)#define NUMAKER\_CLK\_CANFDSEL\_CANFD1SEL\_HXT 0x00000000

[ 25](numaker__m55m1x__clock_8h.md#a72ca819c5300ce4326948318e4e957c8)#define NUMAKER\_CLK\_CANFDSEL\_CANFD1SEL\_APLL0\_DIV2 0x00000010

[ 26](numaker__m55m1x__clock_8h.md#a41b02afa83ddb119bbeb168f0c4c110a)#define NUMAKER\_CLK\_CANFDSEL\_CANFD1SEL\_HCLK0 0x00000020

[ 27](numaker__m55m1x__clock_8h.md#aabbe6462643fadd6dcaad7cf8d951914)#define NUMAKER\_CLK\_CANFDSEL\_CANFD1SEL\_HIRC 0x00000030

[ 28](numaker__m55m1x__clock_8h.md#af5c41bccc46ae11182b2b8ec378243c8)#define NUMAKER\_CLK\_CANFDSEL\_CANFD1SEL\_HIRC48M\_DIV4 0x00000040

[ 29](numaker__m55m1x__clock_8h.md#aa7b02442c3c4de77d0080d77978b4295)#define NUMAKER\_CLK\_CCAPSEL\_CCAP0SEL\_MIRC 0x00000000

[ 30](numaker__m55m1x__clock_8h.md#ac5b80c2e236d01d266b92249b9239789)#define NUMAKER\_CLK\_CCAPSEL\_CCAP0SEL\_HCLK2 0x00000001

[ 31](numaker__m55m1x__clock_8h.md#ad2ebf9305d48e214fa03a03ba78dc5fb)#define NUMAKER\_CLK\_CCAPSEL\_CCAP0SEL\_HIRC 0x00000002

[ 32](numaker__m55m1x__clock_8h.md#a2f870e58a3ae215bb7c919ec1c00dd8a)#define NUMAKER\_CLK\_CCAPSEL\_CCAP0SEL\_APLL0\_DIV2 0x00000003

[ 33](numaker__m55m1x__clock_8h.md#a0e170cedef831019d36084d0847083ea)#define NUMAKER\_CLK\_CCAPSEL\_CCAP0SEL\_HXT 0x00000004

[ 34](numaker__m55m1x__clock_8h.md#ae65b4e91555739f27055dbe3af5c6123)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_SYSCLK 0x00000000

[ 35](numaker__m55m1x__clock_8h.md#a5c32f4f2af3d5b85928951da8adbd681)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_ACLK 0x00000001

[ 36](numaker__m55m1x__clock_8h.md#acfaa1c07529a6bd4995f9c9f1601a22f)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_HCLK0 0x00000002

[ 37](numaker__m55m1x__clock_8h.md#a7f0e2ecff7f5ea682992239e7fde8224)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_HCLK1 0x00000003

[ 38](numaker__m55m1x__clock_8h.md#a524b14de614db3e3f4fd1b826324e9dd)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_HCLK2 0x00000004

[ 39](numaker__m55m1x__clock_8h.md#a5e9dbb1e08eff0974ab99c3485b60179)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_APLL0\_DIV2 0x00000005

[ 40](numaker__m55m1x__clock_8h.md#a72b87aebe471fb68fd50997c4dbfed36)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_APLL1\_DIV2 0x00000006

[ 41](numaker__m55m1x__clock_8h.md#a546060e8d60c3de0b79c961fcf4d0cb3)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_HIRC48M 0x00000007

[ 42](numaker__m55m1x__clock_8h.md#a76f55adb5b5eeaf3b0c630c1d8568c91)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_HXT 0x00000008

[ 43](numaker__m55m1x__clock_8h.md#a62ffc38e4f764c640ada69aceecb8522)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_HIRC 0x00000009

[ 44](numaker__m55m1x__clock_8h.md#a133e841019d3404de876c934e196900d)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_MIRC 0x0000000A

[ 45](numaker__m55m1x__clock_8h.md#a3fb23db0756f86fabf43481bd355ffbc)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_LXT 0x0000000B

[ 46](numaker__m55m1x__clock_8h.md#ad586ba7138b47512e01b229d2d49d637)#define NUMAKER\_CLK\_CLKOSEL\_CLKOSEL\_LIRC 0x0000000C

[ 47](numaker__m55m1x__clock_8h.md#a10c0bf170e1c6139eea2493ab8838f79)#define NUMAKER\_CLK\_DMICSEL\_DMIC0SEL\_HXT 0x00000000

[ 48](numaker__m55m1x__clock_8h.md#afc3e648c600544e026a284e1b5305e35)#define NUMAKER\_CLK\_DMICSEL\_DMIC0SEL\_APLL1\_DIV2 0x00000001

[ 49](numaker__m55m1x__clock_8h.md#a6a3da12d1ce97e934ac7118b0f9589b1)#define NUMAKER\_CLK\_DMICSEL\_DMIC0SEL\_MIRC 0x00000002

[ 50](numaker__m55m1x__clock_8h.md#a0a333055acbf00f480f02a029c576754)#define NUMAKER\_CLK\_DMICSEL\_DMIC0SEL\_HIRC 0x00000003

[ 51](numaker__m55m1x__clock_8h.md#a9657ed547f19cce5b4d62735805f0ed8)#define NUMAKER\_CLK\_DMICSEL\_DMIC0SEL\_HIRC48M 0x00000004

[ 52](numaker__m55m1x__clock_8h.md#a7162928c23abc1ce85ba3f2b3d9fa8cf)#define NUMAKER\_CLK\_DMICSEL\_DMIC0SEL\_PCLK4 0x00000005

[ 53](numaker__m55m1x__clock_8h.md#aab2f0abf6342fe08f25f197cd3d3b669)#define NUMAKER\_CLK\_DMICSEL\_VAD0SEL\_PCLK4 0x00000000

[ 54](numaker__m55m1x__clock_8h.md#a58b353b1c11ab4d40ae5dc2faa0e53fb)#define NUMAKER\_CLK\_DMICSEL\_VAD0SEL\_MIRC 0x00000010

[ 55](numaker__m55m1x__clock_8h.md#a255697b1884260e10baad28c6a9f0cf1)#define NUMAKER\_CLK\_DMICSEL\_VAD0SEL\_HIRC 0x00000020

[ 56](numaker__m55m1x__clock_8h.md#a7746a35b30cf8f62d57f4d592e0d11a8)#define NUMAKER\_CLK\_EADCSEL\_EADC0SEL\_APLL1\_DIV2 0x00000000

[ 57](numaker__m55m1x__clock_8h.md#a167b555ec88efe64b9444479fd5d9405)#define NUMAKER\_CLK\_EADCSEL\_EADC0SEL\_APLL0\_DIV2 0x00000001

[ 58](numaker__m55m1x__clock_8h.md#a1463fe1a1d23c79aa8cdb1678876ecc3)#define NUMAKER\_CLK\_EADCSEL\_EADC0SEL\_PCLK0 0x00000002

[ 59](numaker__m55m1x__clock_8h.md#ae0172e67dd234d7a0a95c0959c3bc966)#define NUMAKER\_CLK\_EPWMSEL\_EPWM0SEL\_PCLK0 0x00000000

[ 60](numaker__m55m1x__clock_8h.md#adaef169b703899fa5ecc2c50ee38f0fd)#define NUMAKER\_CLK\_EPWMSEL\_EPWM0SEL\_HCLK0 0x00000001

[ 61](numaker__m55m1x__clock_8h.md#a10a983521e61e3049852a333905988a4)#define NUMAKER\_CLK\_EPWMSEL\_EPWM1SEL\_PCLK2 0x00000000

[ 62](numaker__m55m1x__clock_8h.md#ad862f45c6f87ae69486b9159d15cfe09)#define NUMAKER\_CLK\_EPWMSEL\_EPWM1SEL\_HCLK0 0x00000010

[ 63](numaker__m55m1x__clock_8h.md#ac3dd8bdc17dfa6b08f03c69e6b15e296)#define NUMAKER\_CLK\_FMCSEL\_FMC0SEL\_HIRC 0x00000000

[ 64](numaker__m55m1x__clock_8h.md#a7a4b813638bfaed02f0c6737717a48a5)#define NUMAKER\_CLK\_FMCSEL\_FMC0SEL\_HIRC48M\_DIV4 0x00000001

[ 65](numaker__m55m1x__clock_8h.md#a20ba88135e1ca88450d432595645bbe7)#define NUMAKER\_CLK\_I2SSEL\_I2S0SEL\_HXT 0x00000000

[ 66](numaker__m55m1x__clock_8h.md#a38b8a584090fa1dc733dc4352e33e7c3)#define NUMAKER\_CLK\_I2SSEL\_I2S0SEL\_APLL1\_DIV2 0x00000001

[ 67](numaker__m55m1x__clock_8h.md#a5aa4fa4fdfadc95ee38e7d2d477adc85)#define NUMAKER\_CLK\_I2SSEL\_I2S0SEL\_APLL0\_DIV2 0x00000002

[ 68](numaker__m55m1x__clock_8h.md#ad09904512bf79a26db9525ca47bf7bc6)#define NUMAKER\_CLK\_I2SSEL\_I2S0SEL\_PCLK1 0x00000003

[ 69](numaker__m55m1x__clock_8h.md#a0016faffdbd3df96e81594e232e44f75)#define NUMAKER\_CLK\_I2SSEL\_I2S0SEL\_HIRC 0x00000004

[ 70](numaker__m55m1x__clock_8h.md#abc953ba50934ab60af33a3a0fd7216bd)#define NUMAKER\_CLK\_I2SSEL\_I2S0SEL\_HIRC48M 0x00000005

[ 71](numaker__m55m1x__clock_8h.md#aef7ca522b36419a2ebb92023717ab23b)#define NUMAKER\_CLK\_I2SSEL\_I2S1SEL\_HXT 0x00000000

[ 72](numaker__m55m1x__clock_8h.md#ae058051475f8c4e8c74a196f7b726bbc)#define NUMAKER\_CLK\_I2SSEL\_I2S1SEL\_APLL1\_DIV2 0x00000010

[ 73](numaker__m55m1x__clock_8h.md#a52bd36db22df6f7b242d365cc1f702c5)#define NUMAKER\_CLK\_I2SSEL\_I2S1SEL\_APLL0\_DIV2 0x00000020

[ 74](numaker__m55m1x__clock_8h.md#a2688e8183d4c5b7c42397f97b7b1f1a6)#define NUMAKER\_CLK\_I2SSEL\_I2S1SEL\_PCLK3 0x00000030

[ 75](numaker__m55m1x__clock_8h.md#aeb1e879e9ff814b29e89507fe350abee)#define NUMAKER\_CLK\_I2SSEL\_I2S1SEL\_HIRC 0x00000040

[ 76](numaker__m55m1x__clock_8h.md#a98584a2a0cdedb57f01a6a2cc6ef5dd7)#define NUMAKER\_CLK\_I2SSEL\_I2S1SEL\_HIRC48M 0x00000050

[ 77](numaker__m55m1x__clock_8h.md#a5b1fbf83fd2b44e30b5a233c9c20ee45)#define NUMAKER\_CLK\_I3CSEL\_I3C0SEL\_HCLK0 0x00000000

[ 78](numaker__m55m1x__clock_8h.md#af19ef4a43543bbf634b4841b5e80289d)#define NUMAKER\_CLK\_I3CSEL\_I3C0SEL\_APLL1 0x00000001

[ 79](numaker__m55m1x__clock_8h.md#a769a58cabb6a346b44fcaef6b2e9d6c2)#define NUMAKER\_CLK\_KPISEL\_KPI0SEL\_HIRC48M\_DIV4 0x00000000

[ 80](numaker__m55m1x__clock_8h.md#aec4c5667eea2d8424668a69943222e93)#define NUMAKER\_CLK\_KPISEL\_KPI0SEL\_HIRC 0x00000001

[ 81](numaker__m55m1x__clock_8h.md#a6de41138e3550341636983ab64b0aec1)#define NUMAKER\_CLK\_KPISEL\_KPI0SEL\_LIRC 0x00000002

[ 82](numaker__m55m1x__clock_8h.md#ab6fbdd77a78775b714e1c5a226eb57c8)#define NUMAKER\_CLK\_KPISEL\_KPI0SEL\_HXT 0x00000003

[ 83](numaker__m55m1x__clock_8h.md#a919405eb810e125fc0dc84d1f43b0da8)#define NUMAKER\_CLK\_LPADCSEL\_LPADC0SEL\_PCLK4 0x00000000

[ 84](numaker__m55m1x__clock_8h.md#a4037fd0ce0303ce4630f3962a5cdfec0)#define NUMAKER\_CLK\_LPADCSEL\_LPADC0SEL\_LXT 0x00000001

[ 85](numaker__m55m1x__clock_8h.md#a90f922e68fd8649928a9c7c0cbab8e93)#define NUMAKER\_CLK\_LPADCSEL\_LPADC0SEL\_MIRC 0x00000002

[ 86](numaker__m55m1x__clock_8h.md#aebf4cdfea75c120863c5c27c49a4ce63)#define NUMAKER\_CLK\_LPADCSEL\_LPADC0SEL\_HIRC 0x00000003

[ 87](numaker__m55m1x__clock_8h.md#a69eca43c71f9e79f059769e076441e33)#define NUMAKER\_CLK\_LPSPISEL\_LPSPI0SEL\_PCLK4 0x00000000

[ 88](numaker__m55m1x__clock_8h.md#a6a9d383b618aba2e16fc1981da27592b)#define NUMAKER\_CLK\_LPSPISEL\_LPSPI0SEL\_MIRC 0x00000001

[ 89](numaker__m55m1x__clock_8h.md#ae071deb3bd2d7ffc888c39ec798ca6c1)#define NUMAKER\_CLK\_LPSPISEL\_LPSPI0SEL\_HIRC 0x00000002

[ 90](numaker__m55m1x__clock_8h.md#a36978f4accb57bf65772d4e9ee1e5259)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR0SEL\_PCLK4 0x00000000

[ 91](numaker__m55m1x__clock_8h.md#adbff724e185f8fd4b43f10cefd808100)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR0SEL\_LXT 0x00000001

[ 92](numaker__m55m1x__clock_8h.md#a7e5e0dd4ce39e45393432a7ce7f14608)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR0SEL\_LIRC 0x00000002

[ 93](numaker__m55m1x__clock_8h.md#a17e86dc4a2c2f2065d33e93df98b9996)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR0SEL\_MIRC 0x00000003

[ 94](numaker__m55m1x__clock_8h.md#a3ce5756326882574d85a125a5bbf4827)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR0SEL\_HIRC 0x00000004

[ 95](numaker__m55m1x__clock_8h.md#aab616c551a8b3bfc4e8ccaccd3fe61f2)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR0SEL\_EXT 0x00000005

[ 96](numaker__m55m1x__clock_8h.md#ad27d8a6e4f5cebc5d2c9411f798c21fe)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR1SEL\_PCLK4 0x00000000

[ 97](numaker__m55m1x__clock_8h.md#a18e71871c11246b053247094db872043)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR1SEL\_LXT 0x00000010

[ 98](numaker__m55m1x__clock_8h.md#a9160e53006c8a4f10d691c78b57deccc)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR1SEL\_LIRC 0x00000020

[ 99](numaker__m55m1x__clock_8h.md#ac26f1973b7e29fc90a8f0acc33be2f65)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR1SEL\_MIRC 0x00000030

[ 100](numaker__m55m1x__clock_8h.md#a6e57247edb22002973d23e62c32d8510)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR1SEL\_HIRC 0x00000040

[ 101](numaker__m55m1x__clock_8h.md#a54348df2ab80cf27744718bf11a6c5cf)#define NUMAKER\_CLK\_LPTMRSEL\_LPTMR1SEL\_EXT 0x00000050

[ 102](numaker__m55m1x__clock_8h.md#a7ce55795a3d25b6eedf287802bf3923f)#define NUMAKER\_CLK\_LPUARTSEL\_LPUART0SEL\_PCLK4 0x00000000

[ 103](numaker__m55m1x__clock_8h.md#aa9c61c1ade7e1e69ec3661495d622ead)#define NUMAKER\_CLK\_LPUARTSEL\_LPUART0SEL\_LXT 0x00000001

[ 104](numaker__m55m1x__clock_8h.md#a682dadad57f5c7f2c59bc8323327fca3)#define NUMAKER\_CLK\_LPUARTSEL\_LPUART0SEL\_MIRC 0x00000002

[ 105](numaker__m55m1x__clock_8h.md#a9a5b994ba12df56db64e90911d5c453d)#define NUMAKER\_CLK\_LPUARTSEL\_LPUART0SEL\_HIRC 0x00000003

[ 106](numaker__m55m1x__clock_8h.md#aed05ddb08d8f6d96b5563e87d10f0c0e)#define NUMAKER\_CLK\_PSIOSEL\_PSIO0SEL\_LXT 0x00000000

[ 107](numaker__m55m1x__clock_8h.md#a3572c9c39c2093ca1beffc5e0f40ce67)#define NUMAKER\_CLK\_PSIOSEL\_PSIO0SEL\_HXT 0x00000001

[ 108](numaker__m55m1x__clock_8h.md#ae3ba428884b745c6656ea787b4a671ce)#define NUMAKER\_CLK\_PSIOSEL\_PSIO0SEL\_LIRC 0x00000002

[ 109](numaker__m55m1x__clock_8h.md#a1a4b34c0243934d1f911c8fb31b6c80c)#define NUMAKER\_CLK\_PSIOSEL\_PSIO0SEL\_HIRC 0x00000003

[ 110](numaker__m55m1x__clock_8h.md#a683b96bd8a44cbe35c30ae6162a57ab5)#define NUMAKER\_CLK\_PSIOSEL\_PSIO0SEL\_HIRC48M\_DIV4 0x00000004

[ 111](numaker__m55m1x__clock_8h.md#afe4f9a6539c132c3cd0a8b448a96bf7d)#define NUMAKER\_CLK\_PSIOSEL\_PSIO0SEL\_PCLK1 0x00000005

[ 112](numaker__m55m1x__clock_8h.md#a90bfad55423abc31951563d2d3c7da12)#define NUMAKER\_CLK\_PSIOSEL\_PSIO0SEL\_APLL0\_DIV2 0x00000006

[ 113](numaker__m55m1x__clock_8h.md#a4b72b8cba0733d024260cb93476bda2d)#define NUMAKER\_CLK\_QSPISEL\_QSPI0SEL\_HXT 0x00000000

[ 114](numaker__m55m1x__clock_8h.md#a203bfb6caa77fafc4c49947228e91ec8)#define NUMAKER\_CLK\_QSPISEL\_QSPI0SEL\_APLL0\_DIV2 0x00000001

[ 115](numaker__m55m1x__clock_8h.md#a40dadd6724ee58ff7856f132a3662aa9)#define NUMAKER\_CLK\_QSPISEL\_QSPI0SEL\_PCLK0 0x00000002

[ 116](numaker__m55m1x__clock_8h.md#aa5f5b3ffb1c46e3daa6c9924fbaf107b)#define NUMAKER\_CLK\_QSPISEL\_QSPI0SEL\_HIRC 0x00000003

[ 117](numaker__m55m1x__clock_8h.md#a68974f51150ca88b00e622c43da30a2b)#define NUMAKER\_CLK\_QSPISEL\_QSPI0SEL\_HIRC48M\_DIV4 0x00000004

[ 118](numaker__m55m1x__clock_8h.md#a861d8c3bb9ef15ab36d334507db01894)#define NUMAKER\_CLK\_QSPISEL\_QSPI1SEL\_HXT 0x00000000

[ 119](numaker__m55m1x__clock_8h.md#acdb49ccbff44b6d215fbb79280b29fbb)#define NUMAKER\_CLK\_QSPISEL\_QSPI1SEL\_APLL0\_DIV2 0x00000010

[ 120](numaker__m55m1x__clock_8h.md#a631006245d70de521b41485067cf1d99)#define NUMAKER\_CLK\_QSPISEL\_QSPI1SEL\_PCLK2 0x00000020

[ 121](numaker__m55m1x__clock_8h.md#aee054cbe94fe9d427343ed05f9636ed5)#define NUMAKER\_CLK\_QSPISEL\_QSPI1SEL\_HIRC 0x00000030

[ 122](numaker__m55m1x__clock_8h.md#a4a53bebe085c0fe5724a3f4a34f3a681)#define NUMAKER\_CLK\_QSPISEL\_QSPI1SEL\_HIRC48M\_DIV4 0x00000040

[ 123](numaker__m55m1x__clock_8h.md#abb986a13f60f8c8c25dbcda8925c3882)#define NUMAKER\_CLK\_SCSEL\_SC0SEL\_HXT 0x00000000

[ 124](numaker__m55m1x__clock_8h.md#aa4f1cc30ba693a2232817ee24841f9f6)#define NUMAKER\_CLK\_SCSEL\_SC0SEL\_APLL0\_DIV2 0x00000001

[ 125](numaker__m55m1x__clock_8h.md#a306d370a1995b73d99ba6e2c5fe20f54)#define NUMAKER\_CLK\_SCSEL\_SC0SEL\_PCLK1 0x00000002

[ 126](numaker__m55m1x__clock_8h.md#ac14959eab0ada365bc3cf9f45702b76c)#define NUMAKER\_CLK\_SCSEL\_SC0SEL\_HIRC 0x00000003

[ 127](numaker__m55m1x__clock_8h.md#a218606566925106f3e384686140bea96)#define NUMAKER\_CLK\_SCSEL\_SC0SEL\_HIRC48M\_DIV4 0x00000004

[ 128](numaker__m55m1x__clock_8h.md#af9041e95308d8a8a11818b061a417432)#define NUMAKER\_CLK\_SCSEL\_SC1SEL\_HXT 0x00000000

[ 129](numaker__m55m1x__clock_8h.md#a832b0dfc24ae4464fd7b9b85e465e456)#define NUMAKER\_CLK\_SCSEL\_SC1SEL\_APLL0\_DIV2 0x00000010

[ 130](numaker__m55m1x__clock_8h.md#a5661c2f95b0cd00a9e938e1802d33fc7)#define NUMAKER\_CLK\_SCSEL\_SC1SEL\_PCLK3 0x00000020

[ 131](numaker__m55m1x__clock_8h.md#a277ae9ca8a3f4e5d831eac4918cfc07f)#define NUMAKER\_CLK\_SCSEL\_SC1SEL\_HIRC 0x00000030

[ 132](numaker__m55m1x__clock_8h.md#aaaf1f6872e8a496f1cd2401da6592d9f)#define NUMAKER\_CLK\_SCSEL\_SC1SEL\_HIRC48M\_DIV4 0x00000040

[ 133](numaker__m55m1x__clock_8h.md#a8caae28bb16d750416f372eacabe60d1)#define NUMAKER\_CLK\_SCSEL\_SC2SEL\_HXT 0x00000000

[ 134](numaker__m55m1x__clock_8h.md#a7977239b2a7d60bc62152d8737990a0e)#define NUMAKER\_CLK\_SCSEL\_SC2SEL\_APLL0\_DIV2 0x00000100

[ 135](numaker__m55m1x__clock_8h.md#a202a647361f5fa087951c4a9389b0a51)#define NUMAKER\_CLK\_SCSEL\_SC2SEL\_PCLK1 0x00000200

[ 136](numaker__m55m1x__clock_8h.md#a65cb6e5d8fc6f41af90a2774cbbc03f6)#define NUMAKER\_CLK\_SCSEL\_SC2SEL\_HIRC 0x00000300

[ 137](numaker__m55m1x__clock_8h.md#ad9447041c08c5e690666d6376a5b227e)#define NUMAKER\_CLK\_SCSEL\_SC2SEL\_HIRC48M\_DIV4 0x00000400

[ 138](numaker__m55m1x__clock_8h.md#a8d5f1466515f32e4b868304010062757)#define NUMAKER\_CLK\_SDHSEL\_SDH0SEL\_HXT 0x00000000

[ 139](numaker__m55m1x__clock_8h.md#a52b72adee38d2bd8cb75702d5b15e768)#define NUMAKER\_CLK\_SDHSEL\_SDH0SEL\_APLL1\_DIV2 0x00000001

[ 140](numaker__m55m1x__clock_8h.md#a64e9f305002d92ca57c0fddf1205a55e)#define NUMAKER\_CLK\_SDHSEL\_SDH0SEL\_HCLK0 0x00000002

[ 141](numaker__m55m1x__clock_8h.md#a9ebd4a27ed4534ecec12218a4904a22b)#define NUMAKER\_CLK\_SDHSEL\_SDH0SEL\_HIRC 0x00000003

[ 142](numaker__m55m1x__clock_8h.md#a90702bd2cc1cd005055655cf306c43d5)#define NUMAKER\_CLK\_SDHSEL\_SDH0SEL\_HIRC48M\_DIV4 0x00000004

[ 143](numaker__m55m1x__clock_8h.md#aea0b66e0eb84d0238f3448ea01fbb1b3)#define NUMAKER\_CLK\_SDHSEL\_SDH1SEL\_HXT 0x00000000

[ 144](numaker__m55m1x__clock_8h.md#a3d5c9561d22ca98c08bd0782cf7c0df4)#define NUMAKER\_CLK\_SDHSEL\_SDH1SEL\_APLL1\_DIV2 0x00000010

[ 145](numaker__m55m1x__clock_8h.md#abb8013090e3bfcd0bb55b3e393c9a58a)#define NUMAKER\_CLK\_SDHSEL\_SDH1SEL\_HCLK0 0x00000020

[ 146](numaker__m55m1x__clock_8h.md#a463e7abee7d18d890906d092c6a26167)#define NUMAKER\_CLK\_SDHSEL\_SDH1SEL\_HIRC 0x00000030

[ 147](numaker__m55m1x__clock_8h.md#a826c4abb3fa456ca8e170b1b56b07079)#define NUMAKER\_CLK\_SDHSEL\_SDH1SEL\_HIRC48M\_DIV4 0x00000040

[ 148](numaker__m55m1x__clock_8h.md#a6f3918706728bd229ca8d329edce0eb4)#define NUMAKER\_CLK\_SPISEL\_SPI0SEL\_HXT 0x00000000

[ 149](numaker__m55m1x__clock_8h.md#a3fddb9568b10150784301a076d34333b)#define NUMAKER\_CLK\_SPISEL\_SPI0SEL\_APLL1\_DIV2 0x00000001

[ 150](numaker__m55m1x__clock_8h.md#a443dfce61d84a13bf0c2be32dcabc47f)#define NUMAKER\_CLK\_SPISEL\_SPI0SEL\_APLL0\_DIV2 0x00000002

[ 151](numaker__m55m1x__clock_8h.md#a0e9d4d82f273288d101642679e448791)#define NUMAKER\_CLK\_SPISEL\_SPI0SEL\_PCLK0 0x00000003

[ 152](numaker__m55m1x__clock_8h.md#aca786169f0daccc8e2b7f3d85a59b787)#define NUMAKER\_CLK\_SPISEL\_SPI0SEL\_HIRC 0x00000004

[ 153](numaker__m55m1x__clock_8h.md#ad67108a26262121acac8a4eca9edc8a9)#define NUMAKER\_CLK\_SPISEL\_SPI0SEL\_HIRC48M 0x00000005

[ 154](numaker__m55m1x__clock_8h.md#ac6b35c5f2cf4c222fd55a5dccbbb549f)#define NUMAKER\_CLK\_SPISEL\_SPI1SEL\_HXT 0x00000000

[ 155](numaker__m55m1x__clock_8h.md#ad9c2333ded4451cf36a6c9bef78cf261)#define NUMAKER\_CLK\_SPISEL\_SPI1SEL\_APLL1\_DIV2 0x00000010

[ 156](numaker__m55m1x__clock_8h.md#a6e4f8e1b51062b1b36b21014ecfa9551)#define NUMAKER\_CLK\_SPISEL\_SPI1SEL\_APLL0\_DIV2 0x00000020

[ 157](numaker__m55m1x__clock_8h.md#add6395c4bc6c2763537de8f937ec1603)#define NUMAKER\_CLK\_SPISEL\_SPI1SEL\_PCLK2 0x00000030

[ 158](numaker__m55m1x__clock_8h.md#a951b21bebfe76cdfa3d3ee47ae6dfb06)#define NUMAKER\_CLK\_SPISEL\_SPI1SEL\_HIRC 0x00000040

[ 159](numaker__m55m1x__clock_8h.md#a4ede8ace1216527e43a4eab34fd71011)#define NUMAKER\_CLK\_SPISEL\_SPI1SEL\_HIRC48M 0x00000050

[ 160](numaker__m55m1x__clock_8h.md#a462c8892b1694363a70a882c9d0e3a33)#define NUMAKER\_CLK\_SPISEL\_SPI2SEL\_HXT 0x00000000

[ 161](numaker__m55m1x__clock_8h.md#af2895b904746e28c08c8bda426cded0c)#define NUMAKER\_CLK\_SPISEL\_SPI2SEL\_APLL1\_DIV2 0x00000100

[ 162](numaker__m55m1x__clock_8h.md#aa35cc6ddbd67c6ac07ad4101d1db4960)#define NUMAKER\_CLK\_SPISEL\_SPI2SEL\_APLL0\_DIV2 0x00000200

[ 163](numaker__m55m1x__clock_8h.md#a89875763ffbe93513737e9c55c621eb5)#define NUMAKER\_CLK\_SPISEL\_SPI2SEL\_PCLK0 0x00000300

[ 164](numaker__m55m1x__clock_8h.md#a7c0bd82802b9138470fa05473af031bc)#define NUMAKER\_CLK\_SPISEL\_SPI2SEL\_HIRC 0x00000400

[ 165](numaker__m55m1x__clock_8h.md#ade5a8fab0ea03fecfa9b8bf715757896)#define NUMAKER\_CLK\_SPISEL\_SPI2SEL\_HIRC48M 0x00000500

[ 166](numaker__m55m1x__clock_8h.md#a0152f050ab60bdc03aade16c0b5f6a75)#define NUMAKER\_CLK\_SPISEL\_SPI3SEL\_HXT 0x00000000

[ 167](numaker__m55m1x__clock_8h.md#a1cfaa52a23ca643c1bbff385164dc46a)#define NUMAKER\_CLK\_SPISEL\_SPI3SEL\_APLL1\_DIV2 0x00001000

[ 168](numaker__m55m1x__clock_8h.md#a9345ff191969e4fc6eadcc800c181fbc)#define NUMAKER\_CLK\_SPISEL\_SPI3SEL\_APLL0\_DIV2 0x00002000

[ 169](numaker__m55m1x__clock_8h.md#a1f790de9c3ce3e3740f1bee3f9ba86a3)#define NUMAKER\_CLK\_SPISEL\_SPI3SEL\_PCLK2 0x00003000

[ 170](numaker__m55m1x__clock_8h.md#af96ebf5efd336c617dc94ee94e49aaeb)#define NUMAKER\_CLK\_SPISEL\_SPI3SEL\_HIRC 0x00004000

[ 171](numaker__m55m1x__clock_8h.md#af605815cc5ec117b6fa582f76627ad20)#define NUMAKER\_CLK\_SPISEL\_SPI3SEL\_HIRC48M 0x00005000

[ 172](numaker__m55m1x__clock_8h.md#aebbfdfe25bbc77c54800bd54889cb467)#define NUMAKER\_CLK\_STSEL\_ST0SEL\_HXT 0x00000000

[ 173](numaker__m55m1x__clock_8h.md#a538e63e1efb4839ef315224ff50ca530)#define NUMAKER\_CLK\_STSEL\_ST0SEL\_HXT\_DIV2 0x00000001

[ 174](numaker__m55m1x__clock_8h.md#a4595cf7c1cdda1c5c927e4a30ba40bb1)#define NUMAKER\_CLK\_STSEL\_ST0SEL\_ACLK\_DIV2 0x00000002

[ 175](numaker__m55m1x__clock_8h.md#a7f791b970c50ecf0e5a99354d0001e1c)#define NUMAKER\_CLK\_STSEL\_ST0SEL\_HIRC\_DIV2 0x00000003

[ 176](numaker__m55m1x__clock_8h.md#a3e7dad52af645c992b672f4da329c6d2)#define NUMAKER\_CLK\_STSEL\_ACLK 0x00000008

[ 177](numaker__m55m1x__clock_8h.md#a7479972c16658a834427f8be326e6196)#define NUMAKER\_CLK\_TMRSEL\_TMR0SEL\_HXT 0x00000000

[ 178](numaker__m55m1x__clock_8h.md#a9d2c8e278d6fff058b3ccf3f943db90c)#define NUMAKER\_CLK\_TMRSEL\_TMR0SEL\_LXT 0x00000001

[ 179](numaker__m55m1x__clock_8h.md#a902ab882e8a3ded2a954e6a780d1eda3)#define NUMAKER\_CLK\_TMRSEL\_TMR0SEL\_PCLK1 0x00000002

[ 180](numaker__m55m1x__clock_8h.md#ae7458255b035482bea2034572d0d131f)#define NUMAKER\_CLK\_TMRSEL\_TMR0SEL\_EXT 0x00000003

[ 181](numaker__m55m1x__clock_8h.md#ad40ace4a61bdab98d476065985cf1a46)#define NUMAKER\_CLK\_TMRSEL\_TMR0SEL\_LIRC 0x00000004

[ 182](numaker__m55m1x__clock_8h.md#a410d853d8521af2c1e8012ae26c1eaf4)#define NUMAKER\_CLK\_TMRSEL\_TMR0SEL\_HIRC 0x00000005

[ 183](numaker__m55m1x__clock_8h.md#a0ec025860b2e41e77b73643eec44aee0)#define NUMAKER\_CLK\_TMRSEL\_TMR0SEL\_HIRC48M\_DIV4 0x00000006

[ 184](numaker__m55m1x__clock_8h.md#a56d76dd1083920368357aa8be28e9932)#define NUMAKER\_CLK\_TMRSEL\_TMR1SEL\_HXT 0x00000000

[ 185](numaker__m55m1x__clock_8h.md#a4fc8652b295e0024d50496cde8eac27b)#define NUMAKER\_CLK\_TMRSEL\_TMR1SEL\_LXT 0x00000010

[ 186](numaker__m55m1x__clock_8h.md#a3d602caf13737631d5a50757628743ed)#define NUMAKER\_CLK\_TMRSEL\_TMR1SEL\_PCLK1 0x00000020

[ 187](numaker__m55m1x__clock_8h.md#a0c8e6e052647a1a5dfb1db2a030e897d)#define NUMAKER\_CLK\_TMRSEL\_TMR1SEL\_EXT 0x00000030

[ 188](numaker__m55m1x__clock_8h.md#a3efd70497950202fb13e5c32e3592674)#define NUMAKER\_CLK\_TMRSEL\_TMR1SEL\_LIRC 0x00000040

[ 189](numaker__m55m1x__clock_8h.md#ae0724ef33d55437de5cce7f3fd47121a)#define NUMAKER\_CLK\_TMRSEL\_TMR1SEL\_HIRC 0x00000050

[ 190](numaker__m55m1x__clock_8h.md#a9ffa782a8167c6fa4183e3e72f285e6e)#define NUMAKER\_CLK\_TMRSEL\_TMR1SEL\_HIRC48M\_DIV4 0x00000060

[ 191](numaker__m55m1x__clock_8h.md#a422bf5019213afada1bcc47e6dc5d329)#define NUMAKER\_CLK\_TMRSEL\_TMR2SEL\_HXT 0x00000000

[ 192](numaker__m55m1x__clock_8h.md#af349160f1622c07bcd27b1df82a767b4)#define NUMAKER\_CLK\_TMRSEL\_TMR2SEL\_LXT 0x00000100

[ 193](numaker__m55m1x__clock_8h.md#a20e439f5828d9943fe0992e812e56c6f)#define NUMAKER\_CLK\_TMRSEL\_TMR2SEL\_PCLK3 0x00000200

[ 194](numaker__m55m1x__clock_8h.md#a152eb734d42e71040a8a4c59130cfa10)#define NUMAKER\_CLK\_TMRSEL\_TMR2SEL\_EXT 0x00000300

[ 195](numaker__m55m1x__clock_8h.md#aa819aeadeb2e2627964a1a8b1acabe99)#define NUMAKER\_CLK\_TMRSEL\_TMR2SEL\_LIRC 0x00000400

[ 196](numaker__m55m1x__clock_8h.md#a7b2a0765ef135167b7d5a0bafeea8d31)#define NUMAKER\_CLK\_TMRSEL\_TMR2SEL\_HIRC 0x00000500

[ 197](numaker__m55m1x__clock_8h.md#aad73b2c2e7ee1997724c7f50038bd046)#define NUMAKER\_CLK\_TMRSEL\_TMR2SEL\_HIRC48M\_DIV4 0x00000600

[ 198](numaker__m55m1x__clock_8h.md#a6544ef23b9f8649dbb9e97c019de3956)#define NUMAKER\_CLK\_TMRSEL\_TMR3SEL\_HXT 0x00000000

[ 199](numaker__m55m1x__clock_8h.md#a68bab455f0d77a0da7e8849510595cc5)#define NUMAKER\_CLK\_TMRSEL\_TMR3SEL\_LXT 0x00001000

[ 200](numaker__m55m1x__clock_8h.md#ae1f0b8c9cc567a0d72a7ffe18070b93a)#define NUMAKER\_CLK\_TMRSEL\_TMR3SEL\_PCLK3 0x00002000

[ 201](numaker__m55m1x__clock_8h.md#a5472a1f001499fa0ecb2e2bb2bbde269)#define NUMAKER\_CLK\_TMRSEL\_TMR3SEL\_EXT 0x00003000

[ 202](numaker__m55m1x__clock_8h.md#a2a81602cd44f051a2f4b9fe6f941cabf)#define NUMAKER\_CLK\_TMRSEL\_TMR3SEL\_LIRC 0x00004000

[ 203](numaker__m55m1x__clock_8h.md#a3165f4f1e6937ddac859696f0f3fab55)#define NUMAKER\_CLK\_TMRSEL\_TMR3SEL\_HIRC 0x00005000

[ 204](numaker__m55m1x__clock_8h.md#ab9b92467192a0cfae08f539f234e1adf)#define NUMAKER\_CLK\_TMRSEL\_TMR3SEL\_HIRC48M\_DIV4 0x00006000

[ 205](numaker__m55m1x__clock_8h.md#a071441cf5d873815726162e9767c9cd7)#define NUMAKER\_CLK\_TTMRSEL\_TTMR0SEL\_PCLK4 0x00000000

[ 206](numaker__m55m1x__clock_8h.md#a5b526e6edd37f8230d7f8999285c7dec)#define NUMAKER\_CLK\_TTMRSEL\_TTMR0SEL\_LXT 0x00000001

[ 207](numaker__m55m1x__clock_8h.md#a996b033bf8fbdd128e12acc303b472b2)#define NUMAKER\_CLK\_TTMRSEL\_TTMR0SEL\_LIRC 0x00000002

[ 208](numaker__m55m1x__clock_8h.md#a9869f32a0377e724d620d7fbc18a27ed)#define NUMAKER\_CLK\_TTMRSEL\_TTMR0SEL\_MIRC 0x00000003

[ 209](numaker__m55m1x__clock_8h.md#a854705db004ece25c1ac751c37755b1c)#define NUMAKER\_CLK\_TTMRSEL\_TTMR0SEL\_HIRC 0x00000004

[ 210](numaker__m55m1x__clock_8h.md#ab44c006b7c248decf5ceeaa2e9c57935)#define NUMAKER\_CLK\_TTMRSEL\_TTMR1SEL\_PCLK4 0x00000000

[ 211](numaker__m55m1x__clock_8h.md#a0e0f6e8f9958f81ba15b57461a6fd116)#define NUMAKER\_CLK\_TTMRSEL\_TTMR1SEL\_LXT 0x00000010

[ 212](numaker__m55m1x__clock_8h.md#a6f5c30c07c646aad93c8867c0e7e4b24)#define NUMAKER\_CLK\_TTMRSEL\_TTMR1SEL\_LIRC 0x00000020

[ 213](numaker__m55m1x__clock_8h.md#a79897cd379b3c57512f1dcf769248c41)#define NUMAKER\_CLK\_TTMRSEL\_TTMR1SEL\_MIRC 0x00000030

[ 214](numaker__m55m1x__clock_8h.md#a38da917d592b62d90512f8438b7a61e3)#define NUMAKER\_CLK\_TTMRSEL\_TTMR1SEL\_HIRC 0x00000040

[ 215](numaker__m55m1x__clock_8h.md#aef038aaf60b4391ee86fdbaf993b1d17)#define NUMAKER\_CLK\_UARTSEL0\_UART0SEL\_HXT 0x00000000

[ 216](numaker__m55m1x__clock_8h.md#ac050620d18edc83942ae1a8a49fc09da)#define NUMAKER\_CLK\_UARTSEL0\_UART0SEL\_HIRC 0x00000001

[ 217](numaker__m55m1x__clock_8h.md#ac1b793a3f93ab0d9dcdf9b3bcbe0252a)#define NUMAKER\_CLK\_UARTSEL0\_UART0SEL\_LXT 0x00000002

[ 218](numaker__m55m1x__clock_8h.md#a553e88f82f580afd518fe6e9ce6d8a30)#define NUMAKER\_CLK\_UARTSEL0\_UART0SEL\_APLL0\_DIV2 0x00000003

[ 219](numaker__m55m1x__clock_8h.md#a6385cf588d4c083297249651207bf4e0)#define NUMAKER\_CLK\_UARTSEL0\_UART0SEL\_HIRC48M 0x00000004

[ 220](numaker__m55m1x__clock_8h.md#aabdff8ce62033fd3631155c0274e176e)#define NUMAKER\_CLK\_UARTSEL0\_UART1SEL\_HXT 0x00000000

[ 221](numaker__m55m1x__clock_8h.md#acdca6194855bd8c03f1d24101cf3fa0a)#define NUMAKER\_CLK\_UARTSEL0\_UART1SEL\_HIRC 0x00000010

[ 222](numaker__m55m1x__clock_8h.md#a2d2dbd2f96afe479b03f93115bce6601)#define NUMAKER\_CLK\_UARTSEL0\_UART1SEL\_LXT 0x00000020

[ 223](numaker__m55m1x__clock_8h.md#a70669b784c6b9f98fff3fe814b2906c8)#define NUMAKER\_CLK\_UARTSEL0\_UART1SEL\_APLL0\_DIV2 0x00000030

[ 224](numaker__m55m1x__clock_8h.md#ac348e5018ce60dc2d7c04de65fad41a7)#define NUMAKER\_CLK\_UARTSEL0\_UART1SEL\_HIRC48M 0x00000040

[ 225](numaker__m55m1x__clock_8h.md#a35c238d161d9c7983ebfc12e765c133f)#define NUMAKER\_CLK\_UARTSEL0\_UART2SEL\_HXT 0x00000000

[ 226](numaker__m55m1x__clock_8h.md#aabd5b04448c47c9c97aedf29c28ea2ac)#define NUMAKER\_CLK\_UARTSEL0\_UART2SEL\_HIRC 0x00000100

[ 227](numaker__m55m1x__clock_8h.md#ab283b75fb396165d8a82fdc989bd7fb1)#define NUMAKER\_CLK\_UARTSEL0\_UART2SEL\_LXT 0x00000200

[ 228](numaker__m55m1x__clock_8h.md#a081935bb3a4828cfd0f4866ffa57617a)#define NUMAKER\_CLK\_UARTSEL0\_UART2SEL\_APLL0\_DIV2 0x00000300

[ 229](numaker__m55m1x__clock_8h.md#a7ddbabe0e2b66585f8837840ac02b3cb)#define NUMAKER\_CLK\_UARTSEL0\_UART2SEL\_HIRC48M 0x00000400

[ 230](numaker__m55m1x__clock_8h.md#ac6ba8bcefc7a7a20c24d9e9ed25f241d)#define NUMAKER\_CLK\_UARTSEL0\_UART3SEL\_HXT 0x00000000

[ 231](numaker__m55m1x__clock_8h.md#ab534669fb5032b92176e5c11be8afd5b)#define NUMAKER\_CLK\_UARTSEL0\_UART3SEL\_HIRC 0x00001000

[ 232](numaker__m55m1x__clock_8h.md#ac42d21ad41b9d12b5916910506276984)#define NUMAKER\_CLK\_UARTSEL0\_UART3SEL\_LXT 0x00002000

[ 233](numaker__m55m1x__clock_8h.md#ab921438a8c3da0d91f863119378c02ae)#define NUMAKER\_CLK\_UARTSEL0\_UART3SEL\_APLL0\_DIV2 0x00003000

[ 234](numaker__m55m1x__clock_8h.md#a7b27c4da9ce892cc7c733a5089cee088)#define NUMAKER\_CLK\_UARTSEL0\_UART3SEL\_HIRC48M 0x00004000

[ 235](numaker__m55m1x__clock_8h.md#a4e137e0338df21700dd4430232e539cb)#define NUMAKER\_CLK\_UARTSEL0\_UART4SEL\_HXT 0x00000000

[ 236](numaker__m55m1x__clock_8h.md#a93d05733d5d6e70a5268ef9bfc65a8e0)#define NUMAKER\_CLK\_UARTSEL0\_UART4SEL\_HIRC 0x00010000

[ 237](numaker__m55m1x__clock_8h.md#a81f5e27ad8c27d10b568e69229ad1efa)#define NUMAKER\_CLK\_UARTSEL0\_UART4SEL\_LXT 0x00020000

[ 238](numaker__m55m1x__clock_8h.md#a65a94a0282db4c43b5c319033452ef97)#define NUMAKER\_CLK\_UARTSEL0\_UART4SEL\_APLL0\_DIV2 0x00030000

[ 239](numaker__m55m1x__clock_8h.md#a455c4604f53e267eb47aa62c612fa425)#define NUMAKER\_CLK\_UARTSEL0\_UART4SEL\_HIRC48M 0x00040000

[ 240](numaker__m55m1x__clock_8h.md#afcbda810e418de3fc432a85f57fffc23)#define NUMAKER\_CLK\_UARTSEL0\_UART5SEL\_HXT 0x00000000

[ 241](numaker__m55m1x__clock_8h.md#aeaed1a97e1f8a6dade951d1644c0e99a)#define NUMAKER\_CLK\_UARTSEL0\_UART5SEL\_HIRC 0x00100000

[ 242](numaker__m55m1x__clock_8h.md#a74610b465c4e083dcb29ab8b798e50ca)#define NUMAKER\_CLK\_UARTSEL0\_UART5SEL\_LXT 0x00200000

[ 243](numaker__m55m1x__clock_8h.md#a33e2e8239687ee30f3b329dfc96c9b7d)#define NUMAKER\_CLK\_UARTSEL0\_UART5SEL\_APLL0\_DIV2 0x00300000

[ 244](numaker__m55m1x__clock_8h.md#aff7c1078fca950f57c2ffbee5569029f)#define NUMAKER\_CLK\_UARTSEL0\_UART5SEL\_HIRC48M 0x00400000

[ 245](numaker__m55m1x__clock_8h.md#a8c4e2de704dee55097bcd14dac8575f6)#define NUMAKER\_CLK\_UARTSEL0\_UART6SEL\_HXT 0x00000000

[ 246](numaker__m55m1x__clock_8h.md#a9e7f2c6372b01f1290d0f26148082f73)#define NUMAKER\_CLK\_UARTSEL0\_UART6SEL\_HIRC 0x01000000

[ 247](numaker__m55m1x__clock_8h.md#a4a2c76c5b872ea76d5eec105e3f3c398)#define NUMAKER\_CLK\_UARTSEL0\_UART6SEL\_LXT 0x02000000

[ 248](numaker__m55m1x__clock_8h.md#a578ea0c715fe59eda8a89d2ac43bbf1c)#define NUMAKER\_CLK\_UARTSEL0\_UART6SEL\_APLL0\_DIV2 0x03000000

[ 249](numaker__m55m1x__clock_8h.md#ab709ce9e1b6726581c9d482882af0966)#define NUMAKER\_CLK\_UARTSEL0\_UART6SEL\_HIRC48M 0x04000000

[ 250](numaker__m55m1x__clock_8h.md#ad6c5399f946c9390e02d713a5539adad)#define NUMAKER\_CLK\_UARTSEL0\_UART7SEL\_HXT 0x00000000

[ 251](numaker__m55m1x__clock_8h.md#aba4966c04597a7d0a108fbb61c3db824)#define NUMAKER\_CLK\_UARTSEL0\_UART7SEL\_HIRC 0x10000000

[ 252](numaker__m55m1x__clock_8h.md#a8bc3910ce36b4f698e9b66dc62a4e69b)#define NUMAKER\_CLK\_UARTSEL0\_UART7SEL\_LXT 0x20000000

[ 253](numaker__m55m1x__clock_8h.md#aaddb721addad6c3c41d2a529ff2c9c55)#define NUMAKER\_CLK\_UARTSEL0\_UART7SEL\_APLL0\_DIV2 0x30000000

[ 254](numaker__m55m1x__clock_8h.md#a7bda3895e811fa16cc0e6206f6036d65)#define NUMAKER\_CLK\_UARTSEL0\_UART7SEL\_HIRC48M 0x40000000

[ 255](numaker__m55m1x__clock_8h.md#a5a28a4bdc5def1367a9aac90a4f919c0)#define NUMAKER\_CLK\_UARTSEL1\_UART8SEL\_HXT 0x00000000

[ 256](numaker__m55m1x__clock_8h.md#a88ad21678bfb29982adcdd03b83e13e7)#define NUMAKER\_CLK\_UARTSEL1\_UART8SEL\_HIRC 0x00000001

[ 257](numaker__m55m1x__clock_8h.md#afd6649f342983dd4f3d5be60c0407f3c)#define NUMAKER\_CLK\_UARTSEL1\_UART8SEL\_LXT 0x00000002

[ 258](numaker__m55m1x__clock_8h.md#ab235093364a9c823fe7e1608552d1ab0)#define NUMAKER\_CLK\_UARTSEL1\_UART8SEL\_APLL0\_DIV2 0x00000003

[ 259](numaker__m55m1x__clock_8h.md#a2b1d5bf5739e2c3f0dc6ab8e5ca10048)#define NUMAKER\_CLK\_UARTSEL1\_UART8SEL\_HIRC48M 0x00000004

[ 260](numaker__m55m1x__clock_8h.md#aec4aa2dfd5ea5f89b7df58170d58fe94)#define NUMAKER\_CLK\_UARTSEL1\_UART9SEL\_HXT 0x00000000

[ 261](numaker__m55m1x__clock_8h.md#a959891b9d1fc2f760bd12de99d6a3957)#define NUMAKER\_CLK\_UARTSEL1\_UART9SEL\_HIRC 0x00000010

[ 262](numaker__m55m1x__clock_8h.md#abf56caa621ce45b6daf248dc8eda7b2f)#define NUMAKER\_CLK\_UARTSEL1\_UART9SEL\_LXT 0x00000020

[ 263](numaker__m55m1x__clock_8h.md#af9897254f56d98df3b428e0819b24e0c)#define NUMAKER\_CLK\_UARTSEL1\_UART9SEL\_APLL0\_DIV2 0x00000030

[ 264](numaker__m55m1x__clock_8h.md#a548f9a1067a09b532dde4d2dd46e8d46)#define NUMAKER\_CLK\_UARTSEL1\_UART9SEL\_HIRC48M 0x00000040

[ 265](numaker__m55m1x__clock_8h.md#a2b1c421baa53da5a87a6494d7208cfd1)#define NUMAKER\_CLK\_USBSEL\_USBSEL\_HIRC48M 0x00000000

[ 266](numaker__m55m1x__clock_8h.md#aa2c817f9c9c733ab35c2f0893b2f3957)#define NUMAKER\_CLK\_USBSEL\_USBSEL\_APLL1\_DIV2 0x00000001

[ 267](numaker__m55m1x__clock_8h.md#a831409dbff35f6b2f678fa4f7acef85d)#define NUMAKER\_CLK\_WDTSEL\_WDT0SEL\_LXT 0x00000000

[ 268](numaker__m55m1x__clock_8h.md#ac537e6ae8cc11dab47da858c746ff5a5)#define NUMAKER\_CLK\_WDTSEL\_WDT0SEL\_LIRC 0x00000001

[ 269](numaker__m55m1x__clock_8h.md#ae828898e59ff009f9e1051437196bebc)#define NUMAKER\_CLK\_WDTSEL\_WDT1SEL\_LXT 0x00000000

[ 270](numaker__m55m1x__clock_8h.md#ac9499765f1c1ebe80f86d8e4e9b07071)#define NUMAKER\_CLK\_WDTSEL\_WDT1SEL\_LIRC 0x00000010

[ 271](numaker__m55m1x__clock_8h.md#a8bdac806121377a4ac50f48bcbda6458)#define NUMAKER\_CLK\_WWDTSEL\_WWDT0SEL\_LIRC 0x00000000

[ 272](numaker__m55m1x__clock_8h.md#a595f931a089fcc7f70b09d303384d4f6)#define NUMAKER\_CLK\_WWDTSEL\_WWDT0SEL\_LXT 0x00000001

[ 273](numaker__m55m1x__clock_8h.md#acd167e56a33ecd4a91e507396181a4d2)#define NUMAKER\_CLK\_WWDTSEL\_WWDT1SEL\_LIRC 0x00000000

[ 274](numaker__m55m1x__clock_8h.md#a7aff76914acf26b4028cc8aaa3eeaffd)#define NUMAKER\_CLK\_WWDTSEL\_WWDT1SEL\_LXT 0x00000010

[ 275](numaker__m55m1x__clock_8h.md#aad64583f85d937482af7cd44222cc0d2)#define NUMAKER\_CLK\_SCLKDIV\_SCLKDIV(x) (((x) - 1UL) << (0))

[ 276](numaker__m55m1x__clock_8h.md#a3a94d58404e42ec66b0f8c7e53917215)#define NUMAKER\_CLK\_HCLKDIV\_HCLK2DIV(x) (((x) - 1UL) << (8))

[ 277](numaker__m55m1x__clock_8h.md#a154c590f5cdb261444ce50f2bdf09811)#define NUMAKER\_CLK\_PCLKDIV\_PCLK0DIV(x) (((x) - 1UL) << (0))

[ 278](numaker__m55m1x__clock_8h.md#a0411f62e46592f78c751c0b113460d1d)#define NUMAKER\_CLK\_PCLKDIV\_PCLK1DIV(x) (((x) - 1UL) << (4))

[ 279](numaker__m55m1x__clock_8h.md#a2d5b99bdcf0a81c11cd60a6ceec528a2)#define NUMAKER\_CLK\_PCLKDIV\_PCLK2DIV(x) (((x) - 1UL) << (8))

[ 280](numaker__m55m1x__clock_8h.md#a46d17a17bfa3c983061b41ca7ae3e7a6)#define NUMAKER\_CLK\_PCLKDIV\_PCLK3DIV(x) (((x) - 1UL) << (12))

[ 281](numaker__m55m1x__clock_8h.md#a6afcb5cbb1ec80c3ac783266e4b12d70)#define NUMAKER\_CLK\_PCLKDIV\_PCLK4DIV(x) (((x) - 1UL) << (16))

[ 282](numaker__m55m1x__clock_8h.md#a47cebf5fcb9d8e85a1be62f9ea49f90d)#define NUMAKER\_CLK\_STDIV\_ST0DIV(x) (((x) - 1UL) << (0))

[ 283](numaker__m55m1x__clock_8h.md#aef2fe6f78e8cf26d19e087e1bf6ee770)#define NUMAKER\_CLK\_CANFDDIV\_CANFD0DIV(x) (((x) - 1UL) << (0))

[ 284](numaker__m55m1x__clock_8h.md#a64767c95d897e221cea61458e711d3b2)#define NUMAKER\_CLK\_CANFDDIV\_CANFD1DIV(x) (((x) - 1UL) << (8))

[ 285](numaker__m55m1x__clock_8h.md#a873ea853c23740277705838ca5f077c0)#define NUMAKER\_CLK\_DMICDIV\_DMIC0DIV(x) (((x) - 1UL) << (0))

[ 286](numaker__m55m1x__clock_8h.md#aec045e1f543cbdfa7a13fb532c1630e2)#define NUMAKER\_CLK\_EADCDIV\_EADC0DIV(x) (((x) - 1UL) << (0))

[ 287](numaker__m55m1x__clock_8h.md#a8596b1a8ab3006a4bc6aec843d9f3d10)#define NUMAKER\_CLK\_I2SDIV\_I2S0DIV(x) (((x) - 1UL) << (0))

[ 288](numaker__m55m1x__clock_8h.md#ac9f9c9e45b4e53ecd89bfcfdbd27378a)#define NUMAKER\_CLK\_I2SDIV\_I2S1DIV(x) (((x) - 1UL) << (8))

[ 289](numaker__m55m1x__clock_8h.md#aacc552a5528ba8a15fadd18894991543)#define NUMAKER\_CLK\_KPIDIV\_KPI0DIV(x) (((x) - 1UL) << (0))

[ 290](numaker__m55m1x__clock_8h.md#ac831608c4d169b1157faa9926b140f4f)#define NUMAKER\_CLK\_LPADCDIV\_LPADC0DIV(x) (((x) - 1UL) << (0))

[ 291](numaker__m55m1x__clock_8h.md#aaf1deef6b648bc1514db2d16ecd53de0)#define NUMAKER\_CLK\_LPUARTDIV\_LPUART0DIV(x) (((x) - 1UL) << (0))

[ 292](numaker__m55m1x__clock_8h.md#adea40775438f4b951962a87d3593a9d3)#define NUMAKER\_CLK\_PSIODIV\_PSIO0DIV(x) (((x) - 1UL) << (0))

[ 293](numaker__m55m1x__clock_8h.md#ac00939e7a6b870cefb4f419ed685684f)#define NUMAKER\_CLK\_SCDIV\_SC0DIV(x) (((x) - 1UL) << (0))

[ 294](numaker__m55m1x__clock_8h.md#a6e666a5a6ad3bac21f57e6a341dce3f0)#define NUMAKER\_CLK\_SCDIV\_SC1DIV(x) (((x) - 1UL) << (8))

[ 295](numaker__m55m1x__clock_8h.md#a72fd1d266c44c31cf4ed92ea341436d0)#define NUMAKER\_CLK\_SCDIV\_SC2DIV(x) (((x) - 1UL) << (16))

[ 296](numaker__m55m1x__clock_8h.md#af27ed2ed58fac68fac8cc16e7bf00ac2)#define NUMAKER\_CLK\_SDHDIV\_SDH0DIV(x) (((x) - 1UL) << (0))

[ 297](numaker__m55m1x__clock_8h.md#a076204afef4396946d0d0891453e6298)#define NUMAKER\_CLK\_SDHDIV\_SDH1DIV(x) (((x) - 1UL) << (8))

[ 298](numaker__m55m1x__clock_8h.md#ade4f521e5dc3d506292db99b53b99b89)#define NUMAKER\_CLK\_UARTDIV0\_UART0DIV(x) (((x) - 1UL) << (0))

[ 299](numaker__m55m1x__clock_8h.md#a5d6bcf9b5d605d9b8478fd6bdddeb10f)#define NUMAKER\_CLK\_UARTDIV0\_UART1DIV(x) (((x) - 1UL) << (4))

[ 300](numaker__m55m1x__clock_8h.md#a31894d1c6bf143f8745e6060592f952a)#define NUMAKER\_CLK\_UARTDIV0\_UART2DIV(x) (((x) - 1UL) << (8))

[ 301](numaker__m55m1x__clock_8h.md#a20b8f80de1bbb6e70942e8004ecb02b3)#define NUMAKER\_CLK\_UARTDIV0\_UART3DIV(x) (((x) - 1UL) << (12))

[ 302](numaker__m55m1x__clock_8h.md#ad67697d9d2a4445e1d99cddc0e8f2877)#define NUMAKER\_CLK\_UARTDIV0\_UART4DIV(x) (((x) - 1UL) << (16))

[ 303](numaker__m55m1x__clock_8h.md#a31726ac29a9f0bd8baf82fc93e2b1d7d)#define NUMAKER\_CLK\_UARTDIV0\_UART5DIV(x) (((x) - 1UL) << (20))

[ 304](numaker__m55m1x__clock_8h.md#a2a58ab49eb3beb7875bf892c6a188c0c)#define NUMAKER\_CLK\_UARTDIV0\_UART6DIV(x) (((x) - 1UL) << (24))

[ 305](numaker__m55m1x__clock_8h.md#af02163b7929fa0eaed9cdad39790b6a3)#define NUMAKER\_CLK\_UARTDIV0\_UART7DIV(x) (((x) - 1UL) << (28))

[ 306](numaker__m55m1x__clock_8h.md#a0d7c01b103f308a66d846558ba472335)#define NUMAKER\_CLK\_UARTDIV1\_UART8DIV(x) (((x) - 1UL) << (0))

[ 307](numaker__m55m1x__clock_8h.md#addb0af4d7dbb030f2c09407080d8d089)#define NUMAKER\_CLK\_UARTDIV1\_UART9DIV(x) (((x) - 1UL) << (4))

[ 308](numaker__m55m1x__clock_8h.md#af0c9f43d354f96c702160362b20cd5e7)#define NUMAKER\_CLK\_USBDIV\_USBDIV(x) (((x) - 1UL) << (0))

[ 309](numaker__m55m1x__clock_8h.md#a4df765c0b418308c1c933775b9f8c000)#define NUMAKER\_CLK\_VSENSEDIV\_VSENSEDIV(x) (((x) - 1UL) << (0))

[ 310](numaker__m55m1x__clock_8h.md#a1a5e3490329be893a174512ce6899a4b)#define NUMAKER\_CLK\_APLL0\_SELECT 0x00000000

[ 311](numaker__m55m1x__clock_8h.md#a8772f63af3ded3c68cd2a4be68e6dba2)#define NUMAKER\_CLK\_APLL1\_SELECT 0x00000001

[ 312](numaker__m55m1x__clock_8h.md#ab884578cf66392b0eacc1c3b2a2cd68a)#define NUMAKER\_CLK\_APLLCTL\_APLLSRC\_HXT 0x00000000

[ 313](numaker__m55m1x__clock_8h.md#a9edb250a4457de846e9d8607120f3edb)#define NUMAKER\_CLK\_APLLCTL\_APLLSRC\_HXT\_DIV2 0x00000001

[ 314](numaker__m55m1x__clock_8h.md#a0bcb0c38cb36df190eb7b1bfbdcf331a)#define NUMAKER\_CLK\_APLLCTL\_APLLSRC\_HIRC 0x00000002

[ 315](numaker__m55m1x__clock_8h.md#a5e04618f0781e39a40af00ad07068212)#define NUMAKER\_CLK\_APLLCTL\_APLLSRC\_HIRC48\_DIV4 0x00000003

[ 316](numaker__m55m1x__clock_8h.md#abe18bfc9e64be82d3734d80a69e2541c)#define NUMAKER\_ACMP01\_MODULE 0

[ 317](numaker__m55m1x__clock_8h.md#a655d49dd28c77605c8a071b78eee9e15)#define NUMAKER\_ACMP23\_MODULE 1

[ 318](numaker__m55m1x__clock_8h.md#acc34649b7f0322f8af679d3d31c98474)#define NUMAKER\_AWF0\_MODULE 2

[ 319](numaker__m55m1x__clock_8h.md#a357c036321109c1962abd936c52bc241)#define NUMAKER\_BPWM0\_MODULE 3

[ 320](numaker__m55m1x__clock_8h.md#a0e2a179864ee42ef88d014d068712aee)#define NUMAKER\_BPWM1\_MODULE 4

[ 321](numaker__m55m1x__clock_8h.md#aec648b50b3e87890e01766e735130d34)#define NUMAKER\_CANFD0\_MODULE 5

[ 322](numaker__m55m1x__clock_8h.md#a4cf36800f445d6eab593a8838285d913)#define NUMAKER\_CANFD1\_MODULE 6

[ 323](numaker__m55m1x__clock_8h.md#a86c60f833d287ab88ac1aafefd083abf)#define NUMAKER\_CCAP0\_MODULE 7

[ 324](numaker__m55m1x__clock_8h.md#af2a76ddbf3b52b74ebcae536424c55e8)#define NUMAKER\_CRC0\_MODULE 8

[ 325](numaker__m55m1x__clock_8h.md#a093ef2b82126ffaceb28609a56df08ad)#define NUMAKER\_CRYPTO0\_MODULE 9

[ 326](numaker__m55m1x__clock_8h.md#a75cbc7428cd1fcd647a9b9baa0c7e68f)#define NUMAKER\_DAC01\_MODULE 10

[ 327](numaker__m55m1x__clock_8h.md#ac8f1cf375265e9ae13a00706351c4137)#define NUMAKER\_DMIC0\_MODULE 11

[ 328](numaker__m55m1x__clock_8h.md#a9bd446858f6f36cc1b0480a8725ac10f)#define NUMAKER\_VAD0SEL\_MODULE 12

[ 329](numaker__m55m1x__clock_8h.md#a46a5cffa974b2f1425d2ced8e678c3e2)#define NUMAKER\_EADC0\_MODULE 13

[ 330](numaker__m55m1x__clock_8h.md#a65178b01f9e28658f5766daa023bd8fa)#define NUMAKER\_EBI0\_MODULE 14

[ 331](numaker__m55m1x__clock_8h.md#afcd2263655b3f52378ee24f2f8bfc0d6)#define NUMAKER\_ECAP0\_MODULE 15

[ 332](numaker__m55m1x__clock_8h.md#a43cc65940b5464683c572c94650a58e9)#define NUMAKER\_ECAP1\_MODULE 16

[ 333](numaker__m55m1x__clock_8h.md#a6f1eccd8218399311b9854c7b84185ea)#define NUMAKER\_ECAP2\_MODULE 17

[ 334](numaker__m55m1x__clock_8h.md#a2cd99780f8545b94483180123aedb756)#define NUMAKER\_ECAP3\_MODULE 18

[ 335](numaker__m55m1x__clock_8h.md#a982967caa2c7f9eac528120a94d10bf5)#define NUMAKER\_EMAC0\_MODULE 19

[ 336](numaker__m55m1x__clock_8h.md#ab42a9a75250104163dab040657beb440)#define NUMAKER\_EPWM0\_MODULE 20

[ 337](numaker__m55m1x__clock_8h.md#a686fa9f9995ef124c47ce20de165b74d)#define NUMAKER\_EPWM1\_MODULE 21

[ 338](numaker__m55m1x__clock_8h.md#a4fe52c877b603a575a230d3de64d2f45)#define NUMAKER\_EQEI0\_MODULE 22

[ 339](numaker__m55m1x__clock_8h.md#a446b5934e374a30377594e63423018b1)#define NUMAKER\_EQEI1\_MODULE 23

[ 340](numaker__m55m1x__clock_8h.md#a062009660b6134f8b288eff5a498566c)#define NUMAKER\_EQEI2\_MODULE 24

[ 341](numaker__m55m1x__clock_8h.md#ab2f4ab88554aee61bdd944ea3d4edd3f)#define NUMAKER\_EQEI3\_MODULE 25

[ 342](numaker__m55m1x__clock_8h.md#a532f3a1c7650c18c8d069fc509703c97)#define NUMAKER\_FMC0\_MODULE 26

[ 343](numaker__m55m1x__clock_8h.md#a7dbe1224b856466d5a01bf8b8825776d)#define NUMAKER\_ISP0\_MODULE 27

[ 344](numaker__m55m1x__clock_8h.md#a6613adb7bbdba2d4c96e4f07a7a2863a)#define NUMAKER\_GDMA0\_MODULE 28

[ 345](numaker__m55m1x__clock_8h.md#add6137567fa1e6d0b17313373c68b365)#define NUMAKER\_GPIOA\_MODULE 29

[ 346](numaker__m55m1x__clock_8h.md#a459b58a58d2f1529e02ffaf2793f198e)#define NUMAKER\_GPIOB\_MODULE 30

[ 347](numaker__m55m1x__clock_8h.md#a46caeb2c2a527bbaf3d99a98864407de)#define NUMAKER\_GPIOC\_MODULE 31

[ 348](numaker__m55m1x__clock_8h.md#abb5ededf113b8783b699761b7b698bf1)#define NUMAKER\_GPIOD\_MODULE 32

[ 349](numaker__m55m1x__clock_8h.md#ac42c82bcca75fd2b0f43b775ba959b76)#define NUMAKER\_GPIOE\_MODULE 33

[ 350](numaker__m55m1x__clock_8h.md#ac614992806a550fae8cbf3a1fd3848a1)#define NUMAKER\_GPIOF\_MODULE 34

[ 351](numaker__m55m1x__clock_8h.md#aa178c5f7c27f4517d62b2a1197cb2e78)#define NUMAKER\_GPIOG\_MODULE 35

[ 352](numaker__m55m1x__clock_8h.md#a6cc8fab48d64e1042be725f9d33ad7ff)#define NUMAKER\_GPIOH\_MODULE 36

[ 353](numaker__m55m1x__clock_8h.md#a9cbac6cf450b8ec8ed35b2cc08b4a2bd)#define NUMAKER\_GPIOI\_MODULE 37

[ 354](numaker__m55m1x__clock_8h.md#aa9747518600433c2db676230ee0e16e4)#define NUMAKER\_GPIOJ\_MODULE 38

[ 355](numaker__m55m1x__clock_8h.md#a1266b53f249a5d55d9cf80eaf54bbe66)#define NUMAKER\_HSOTG0\_MODULE 39

[ 356](numaker__m55m1x__clock_8h.md#a80f0a34b6134df101953eaf1a5bfcbf0)#define NUMAKER\_HSUSBD0\_MODULE 40

[ 357](numaker__m55m1x__clock_8h.md#a1a3f34086fc837669aa1da065a7eac5a)#define NUMAKER\_HSUSBH0\_MODULE 41

[ 358](numaker__m55m1x__clock_8h.md#a8241dce3f2329ef3561277656bd68e7f)#define NUMAKER\_I2C0\_MODULE 42

[ 359](numaker__m55m1x__clock_8h.md#a08413ee5eed011e452f7352a276b45af)#define NUMAKER\_I2C1\_MODULE 43

[ 360](numaker__m55m1x__clock_8h.md#a211a7c416249dad417b5971a4c8526fe)#define NUMAKER\_I2C2\_MODULE 44

[ 361](numaker__m55m1x__clock_8h.md#a0660bb6481a262632fdfd08f4c65c1db)#define NUMAKER\_I2C3\_MODULE 45

[ 362](numaker__m55m1x__clock_8h.md#a93460f284274121252ffaf3ca48510e5)#define NUMAKER\_I2S0\_MODULE 46

[ 363](numaker__m55m1x__clock_8h.md#aa1bcd301211aae3a1ae668af74ee58f6)#define NUMAKER\_I2S1\_MODULE 47

[ 364](numaker__m55m1x__clock_8h.md#ae48ce165c2d3d64f9299de3ea2491468)#define NUMAKER\_I3C0\_MODULE 48

[ 365](numaker__m55m1x__clock_8h.md#a3561a14964bf484b25f42c128884bce0)#define NUMAKER\_KDF0\_MODULE 49

[ 366](numaker__m55m1x__clock_8h.md#ae1dd827c7f5e303ef565b8de65cad94a)#define NUMAKER\_KPI0\_MODULE 50

[ 367](numaker__m55m1x__clock_8h.md#a661e42813c97c0dcfd2fcc94ac86dc21)#define NUMAKER\_KS0\_MODULE 51

[ 368](numaker__m55m1x__clock_8h.md#ace0ae8a2402639eb64dc3483ba70003d)#define NUMAKER\_LPADC0\_MODULE 52

[ 369](numaker__m55m1x__clock_8h.md#a64c1a7bdef90c48d7f143204b8868289)#define NUMAKER\_LPPDMA0\_MODULE 53

[ 370](numaker__m55m1x__clock_8h.md#a21668a6f3e2f4f235e2a7842b34bd704)#define NUMAKER\_LPGPIO0\_MODULE 54

[ 371](numaker__m55m1x__clock_8h.md#a8926f92760ed3299445fde66508c488d)#define NUMAKER\_LPI2C0\_MODULE 55

[ 372](numaker__m55m1x__clock_8h.md#a2cbc8d599f6f30f748c4b7983afadf35)#define NUMAKER\_LPSPI0\_MODULE 56

[ 373](numaker__m55m1x__clock_8h.md#a94c2a56e118d87fb0286385188120ef0)#define NUMAKER\_LPSRAM0\_MODULE 57

[ 374](numaker__m55m1x__clock_8h.md#a395998af6b48e4f44dc2896c9fffa4e6)#define NUMAKER\_LPTMR0\_MODULE 58

[ 375](numaker__m55m1x__clock_8h.md#a8a7f92bbf41ade96a93b0947b33bd5ff)#define NUMAKER\_LPTMR1\_MODULE 59

[ 376](numaker__m55m1x__clock_8h.md#acd05c73a03e017ba39c90635b54d4135)#define NUMAKER\_LPUART0\_MODULE 60

[ 377](numaker__m55m1x__clock_8h.md#a25f05e1b6d07b66289009336c5997b25)#define NUMAKER\_NPU0\_MODULE 61

[ 378](numaker__m55m1x__clock_8h.md#a1b6a2a57478010b0e9f06a2b0d6ecbaf)#define NUMAKER\_OTFC0\_MODULE 62

[ 379](numaker__m55m1x__clock_8h.md#a5616854f68e8c83ebf62e4dcf05579ab)#define NUMAKER\_OTG0\_MODULE 63

[ 380](numaker__m55m1x__clock_8h.md#a81c0a35692befb3b0427efc7a1e2686e)#define NUMAKER\_PDMA0\_MODULE 64

[ 381](numaker__m55m1x__clock_8h.md#a9bd6ce359c452c822a59a6f0da68c7d0)#define NUMAKER\_PDMA1\_MODULE 65

[ 382](numaker__m55m1x__clock_8h.md#a698423c108d8491d42666e5b9c062d64)#define NUMAKER\_PSIO0\_MODULE 66

[ 383](numaker__m55m1x__clock_8h.md#a6dad02cb850ad26c2afde2291d669808)#define NUMAKER\_QSPI0\_MODULE 67

[ 384](numaker__m55m1x__clock_8h.md#a38cb7b22e41b081d55f594b4b5812fc4)#define NUMAKER\_QSPI1\_MODULE 68

[ 385](numaker__m55m1x__clock_8h.md#ac11a7b3da7be7ccf5bfd8f181ddae855)#define NUMAKER\_RTC0\_MODULE 69

[ 386](numaker__m55m1x__clock_8h.md#ade881cb3ef71ab90bc655c5775f4b5f2)#define NUMAKER\_SC0\_MODULE 70

[ 387](numaker__m55m1x__clock_8h.md#a183b62952b0a65cd91e9f8f43bbc85d5)#define NUMAKER\_SC1\_MODULE 71

[ 388](numaker__m55m1x__clock_8h.md#aac46396a96d07b982ea79848109c8df5)#define NUMAKER\_SC2\_MODULE 72

[ 389](numaker__m55m1x__clock_8h.md#a6b1f000259b0837299b53e992799ed92)#define NUMAKER\_SCU0\_MODULE 73

[ 390](numaker__m55m1x__clock_8h.md#aac1289976a442b2fedb1233b15982ae0)#define NUMAKER\_SDH0\_MODULE 74

[ 391](numaker__m55m1x__clock_8h.md#a5ee10e118573a4c747d9c0712e5adede)#define NUMAKER\_SDH1\_MODULE 75

[ 392](numaker__m55m1x__clock_8h.md#adaa689295a31e5b259a7c05b6611a125)#define NUMAKER\_SPI0\_MODULE 76

[ 393](numaker__m55m1x__clock_8h.md#a144be66983b8b45995a7b037681477e7)#define NUMAKER\_SPI1\_MODULE 77

[ 394](numaker__m55m1x__clock_8h.md#a227a44ce55b040227bfe3233cfd63467)#define NUMAKER\_SPI2\_MODULE 78

[ 395](numaker__m55m1x__clock_8h.md#aa251c8b6a225d24b4e3f20dd22498b79)#define NUMAKER\_SPI3\_MODULE 79

[ 396](numaker__m55m1x__clock_8h.md#afb6a33f5f04cda1ec85cda65ddcc334b)#define NUMAKER\_SPIM0\_MODULE 80

[ 397](numaker__m55m1x__clock_8h.md#a4329f632f06a8837134c5c2161565caa)#define NUMAKER\_SRAM0\_MODULE 81

[ 398](numaker__m55m1x__clock_8h.md#aaff4b64254ad3bf38d5798ba751f0493)#define NUMAKER\_SRAM1\_MODULE 82

[ 399](numaker__m55m1x__clock_8h.md#af2a261bc14fb79d72db7a076a923e427)#define NUMAKER\_SRAM2\_MODULE 83

[ 400](numaker__m55m1x__clock_8h.md#a95680146b83a3f9efcb8fa0bdadcdc87)#define NUMAKER\_SRAM3\_MODULE 84

[ 401](numaker__m55m1x__clock_8h.md#a15099d4474147b51feb76c2858196d42)#define NUMAKER\_ST0\_MODULE 85

[ 402](numaker__m55m1x__clock_8h.md#adaec43e184ed7f3c34f66b4e98041f62)#define NUMAKER\_TMR0\_MODULE 86

[ 403](numaker__m55m1x__clock_8h.md#a50c780a3f2c07cc2dfca1e647e83782d)#define NUMAKER\_TMR1\_MODULE 87

[ 404](numaker__m55m1x__clock_8h.md#a7a60853a52958a5c8a78e383f378f579)#define NUMAKER\_TMR2\_MODULE 88

[ 405](numaker__m55m1x__clock_8h.md#a42fd788548168d2b519f5d49d2eead47)#define NUMAKER\_TMR3\_MODULE 89

[ 406](numaker__m55m1x__clock_8h.md#a697d810565979e7d1fe222a2d5e9a796)#define NUMAKER\_TRNG0\_MODULE 90

[ 407](numaker__m55m1x__clock_8h.md#a809f2eeb0f49edc25e8b306d7a3ec6f8)#define NUMAKER\_TTMR0\_MODULE 91

[ 408](numaker__m55m1x__clock_8h.md#a6256d13006c2c8ef0b5b646bab655047)#define NUMAKER\_TTMR1\_MODULE 92

[ 409](numaker__m55m1x__clock_8h.md#aaf0220a2af6dd7368761bf753ae7b73e)#define NUMAKER\_UART0\_MODULE 93

[ 410](numaker__m55m1x__clock_8h.md#a38d069ddfd9912c38c42a8f7e3ead763)#define NUMAKER\_UART1\_MODULE 94

[ 411](numaker__m55m1x__clock_8h.md#aa6dbc85be07f392f38a88bc074f11046)#define NUMAKER\_UART2\_MODULE 95

[ 412](numaker__m55m1x__clock_8h.md#a98c5368b7868f6bc68e09df7f479be73)#define NUMAKER\_UART3\_MODULE 96

[ 413](numaker__m55m1x__clock_8h.md#a0045544d52c292c13edb09e90f4b16c8)#define NUMAKER\_UART4\_MODULE 97

[ 414](numaker__m55m1x__clock_8h.md#a0fdf72d7961da9c046d7d4bb9e19cf1f)#define NUMAKER\_UART5\_MODULE 98

[ 415](numaker__m55m1x__clock_8h.md#aa4081c973118f02b92299ea8d775a1e5)#define NUMAKER\_UART6\_MODULE 99

[ 416](numaker__m55m1x__clock_8h.md#a86caba0b690236e26e440bc39e4bf4c9)#define NUMAKER\_UART7\_MODULE 100

[ 417](numaker__m55m1x__clock_8h.md#a30c536594814a2d4c58d383469a91081)#define NUMAKER\_UART8\_MODULE 101

[ 418](numaker__m55m1x__clock_8h.md#a87e45a8420e6329f101f564e08f896b2)#define NUMAKER\_UART9\_MODULE 102

[ 419](numaker__m55m1x__clock_8h.md#a4e44306971e40e814d738c60148aff06)#define NUMAKER\_USBD0\_MODULE 103

[ 420](numaker__m55m1x__clock_8h.md#a205d0a3b4b406cd3efc0135a374760af)#define NUMAKER\_USBH0\_MODULE 104

[ 421](numaker__m55m1x__clock_8h.md#a96da4a8ec09af3cbf8ab34e1bccb7819)#define NUMAKER\_USCI0\_MODULE 105

[ 422](numaker__m55m1x__clock_8h.md#ae81c1c919c104b891181d1ae5a1eadbf)#define NUMAKER\_UTCPD0\_MODULE 106

[ 423](numaker__m55m1x__clock_8h.md#af03d38271de5b8a1f26953547515098a)#define NUMAKER\_WDT0\_MODULE 107

[ 424](numaker__m55m1x__clock_8h.md#a3defcf41c22b0526afdd1049b4ac92ca)#define NUMAKER\_WDT1\_MODULE 108

[ 425](numaker__m55m1x__clock_8h.md#a0d8ee1ad55739b2afe2aea5e566e01e1)#define NUMAKER\_WWDT0\_MODULE 109

[ 426](numaker__m55m1x__clock_8h.md#ac3d4b0d9be20b3ae17ad1b32443f2542)#define NUMAKER\_WWDT1\_MODULE 110

[ 427](numaker__m55m1x__clock_8h.md#a828d0bf788e94877cc72093529d965f1)#define NUMAKER\_PMC\_NPD0 0x00000000

[ 428](numaker__m55m1x__clock_8h.md#a6f57ed6cd012585dab1bd095ede8541e)#define NUMAKER\_PMC\_NPD1 0x00000001

[ 429](numaker__m55m1x__clock_8h.md#aa3ec2fcbe779f6ef2a743ddbed189f22)#define NUMAKER\_PMC\_NPD2 0x00000002

[ 430](numaker__m55m1x__clock_8h.md#a72f42d744c54e090182ca435947d7f65)#define NUMAKER\_PMC\_NPD3 0x00000003

[ 431](numaker__m55m1x__clock_8h.md#ad315235eacb404c11eb62ae9fcc95880)#define NUMAKER\_PMC\_NPD4 0x00000004

[ 432](numaker__m55m1x__clock_8h.md#a30e1ce4d0a4329479d9f580ec3cd5b73)#define NUMAKER\_PMC\_SPD0 0x00000005

[ 433](numaker__m55m1x__clock_8h.md#ae7956ba83fb3ddcad2d4218cf91dcd1c)#define NUMAKER\_PMC\_SPD1 0x00000006

[ 434](numaker__m55m1x__clock_8h.md#a1987c2ee0f302d4a2868aa61ced13890)#define NUMAKER\_PMC\_DPD 0x00000007

435

436#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [numaker\_m55m1x\_clock.h](numaker__m55m1x__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
