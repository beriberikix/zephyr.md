---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra8t1-elc_8h_source.html
original_path: doxygen/html/ra8t1-elc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra8t1-elc.h

[Go to the documentation of this file.](ra8t1-elc_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA8T1\_ELC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA8T1\_ELC\_H\_

9

10/\* Sources of event signals to be linked to other peripherals or the CPU \*/

[ 11](ra8t1-elc_8h.md#a11b5cec97472328120a8d6381f1e8809)#define RA\_ELC\_EVENT\_NONE 0x0

[ 12](ra8t1-elc_8h.md#a04ee26d7188b7441627bb89249545cfa)#define RA\_ELC\_EVENT\_ICU\_IRQ0 0x001

[ 13](ra8t1-elc_8h.md#ac9f6681c03b50d8b3a24798b3e790170)#define RA\_ELC\_EVENT\_ICU\_IRQ1 0x002

[ 14](ra8t1-elc_8h.md#a136f93a17eea3f4233b0012c075fc904)#define RA\_ELC\_EVENT\_ICU\_IRQ2 0x003

[ 15](ra8t1-elc_8h.md#a65b92e543dfb43c213274652ae60314a)#define RA\_ELC\_EVENT\_ICU\_IRQ3 0x004

[ 16](ra8t1-elc_8h.md#a2b1930fc54010b7c4c00f286f690cb1e)#define RA\_ELC\_EVENT\_ICU\_IRQ4 0x005

[ 17](ra8t1-elc_8h.md#af3ecccfe646b6cac991310abe3e4b955)#define RA\_ELC\_EVENT\_ICU\_IRQ5 0x006

[ 18](ra8t1-elc_8h.md#a98b53eb7b5979403023805ba925c504c)#define RA\_ELC\_EVENT\_ICU\_IRQ6 0x007

[ 19](ra8t1-elc_8h.md#ab6f05849ddc30ceb693f57b522223bcf)#define RA\_ELC\_EVENT\_ICU\_IRQ7 0x008

[ 20](ra8t1-elc_8h.md#acbcd1c55530c6cb8580b76bd55c73c90)#define RA\_ELC\_EVENT\_ICU\_IRQ8 0x009

[ 21](ra8t1-elc_8h.md#af04ed29327af6c108875334c24d98e43)#define RA\_ELC\_EVENT\_ICU\_IRQ9 0x00A

[ 22](ra8t1-elc_8h.md#a3e9a895c4855c3db6ac7fc5900b57807)#define RA\_ELC\_EVENT\_ICU\_IRQ10 0x00B

[ 23](ra8t1-elc_8h.md#a46f43f1dd26e006c26b11bd45e53a728)#define RA\_ELC\_EVENT\_ICU\_IRQ11 0x00C

[ 24](ra8t1-elc_8h.md#affb7ae86a41c8cc8582e6c6ef284a5d8)#define RA\_ELC\_EVENT\_ICU\_IRQ12 0x00D

[ 25](ra8t1-elc_8h.md#ad7435ed602899357eae0f46c09bf542c)#define RA\_ELC\_EVENT\_ICU\_IRQ13 0x00E

[ 26](ra8t1-elc_8h.md#ada7702d0ac50f9b3e82ef50d6be50470)#define RA\_ELC\_EVENT\_ICU\_IRQ14 0x00F

[ 27](ra8t1-elc_8h.md#afab294cf0d58a5bb4dd578774b0ad9aa)#define RA\_ELC\_EVENT\_ICU\_IRQ15 0x010

[ 28](ra8t1-elc_8h.md#a906929a9ae7dd7de44d21a32d3635080)#define RA\_ELC\_EVENT\_DMAC0\_INT 0x011

[ 29](ra8t1-elc_8h.md#a76b9d9fa8af16a1480fcc8d8ec12572f)#define RA\_ELC\_EVENT\_DMAC1\_INT 0x012

[ 30](ra8t1-elc_8h.md#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)#define RA\_ELC\_EVENT\_DMAC2\_INT 0x013

[ 31](ra8t1-elc_8h.md#a0b9d72a41fd7c5b27e6c31967645b907)#define RA\_ELC\_EVENT\_DMAC3\_INT 0x014

[ 32](ra8t1-elc_8h.md#a4cae5afbbe49719555bbbfa12b8727f5)#define RA\_ELC\_EVENT\_DMAC4\_INT 0x015

[ 33](ra8t1-elc_8h.md#a000e31aba8a821f4358a435d280b3a7b)#define RA\_ELC\_EVENT\_DMAC5\_INT 0x016

[ 34](ra8t1-elc_8h.md#a2d1f6d1c797a0d787a5d5c08b0fc18ad)#define RA\_ELC\_EVENT\_DMAC6\_INT 0x017

[ 35](ra8t1-elc_8h.md#ae8caef45a510d4c4f1c55f923e01799e)#define RA\_ELC\_EVENT\_DMAC7\_INT 0x018

[ 36](ra8t1-elc_8h.md#a5ab484cdaf470b47e95005d83d60394f)#define RA\_ELC\_EVENT\_DTC\_END 0x021

[ 37](ra8t1-elc_8h.md#a9a58e3a2c10447906aaf35bab5664d24)#define RA\_ELC\_EVENT\_DTC\_COMPLETE 0x022

[ 38](ra8t1-elc_8h.md#a54d8c74eefe8f9b237ea23e18033d947)#define RA\_ELC\_EVENT\_DMA\_TRANSERR 0x027

[ 39](ra8t1-elc_8h.md#a0d740efcf6ca4778a2f8a9e9bd7c11c9)#define RA\_ELC\_EVENT\_DBG\_CTIIRQ0 0x029

[ 40](ra8t1-elc_8h.md#ab33d581df4d34b8ee361ea4e1e690ed3)#define RA\_ELC\_EVENT\_DBG\_CTIIRQ1 0x02A

[ 41](ra8t1-elc_8h.md#a0494be0bf55e1e687e2f4c0e0f0d93aa)#define RA\_ELC\_EVENT\_DBG\_JBRXI 0x02B

[ 42](ra8t1-elc_8h.md#a5c7545a2f69856b7b637ad690f158b77)#define RA\_ELC\_EVENT\_FCU\_FIFERR 0x030

[ 43](ra8t1-elc_8h.md#a535af54c8bcfff47cc90ba1226044d71)#define RA\_ELC\_EVENT\_FCU\_FRDYI 0x031

[ 44](ra8t1-elc_8h.md#a7ab275777147d06315a04abb3f2f6d51)#define RA\_ELC\_EVENT\_LVD\_LVD1 0x038

[ 45](ra8t1-elc_8h.md#ad52acadba107b7f907d678f44769a4cb)#define RA\_ELC\_EVENT\_LVD\_LVD2 0x039

[ 46](ra8t1-elc_8h.md#a290decf4254396cbce267cb52a619717)#define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP 0x03E

[ 47](ra8t1-elc_8h.md#aecaa6cbbfd3a5e0007a00fd11edc204d)#define RA\_ELC\_EVENT\_ULPT0\_INT 0x040

[ 48](ra8t1-elc_8h.md#a69ec3e618136c55cebeb2d76fc2e88ba)#define RA\_ELC\_EVENT\_ULPT0\_COMPARE\_A 0x041

[ 49](ra8t1-elc_8h.md#ac954387c6092e77e6002997f93e4d10e)#define RA\_ELC\_EVENT\_ULPT0\_COMPARE\_B 0x042

[ 50](ra8t1-elc_8h.md#ac313fdd1b0179ee96d36532504592305)#define RA\_ELC\_EVENT\_ULPT1\_INT 0x043

[ 51](ra8t1-elc_8h.md#a77531873ba01d812a3f5614059016cf6)#define RA\_ELC\_EVENT\_ULPT1\_COMPARE\_A 0x044

[ 52](ra8t1-elc_8h.md#aadb4d755431beb28984de1e962402a39)#define RA\_ELC\_EVENT\_ULPT1\_COMPARE\_B 0x045

[ 53](ra8t1-elc_8h.md#a4c3604a42ead1d43f472e901087ec148)#define RA\_ELC\_EVENT\_AGT0\_INT 0x046

[ 54](ra8t1-elc_8h.md#a015e6f8aed4b467f4554e6887b4d9ec9)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A 0x047

[ 55](ra8t1-elc_8h.md#ada1ad302dc5b987a6f7c972afae729f2)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B 0x048

[ 56](ra8t1-elc_8h.md#a635180e38c932579072f4eebd665592f)#define RA\_ELC\_EVENT\_AGT1\_INT 0x049

[ 57](ra8t1-elc_8h.md#aeb2399818b6b141ab4a37e257dba22be)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A 0x04A

[ 58](ra8t1-elc_8h.md#a1d660c78348b48ea7a072225491ae44b)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B 0x04B

[ 59](ra8t1-elc_8h.md#abc837f1fcfffeb2ec231c79336379dda)#define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW 0x052

[ 60](ra8t1-elc_8h.md#aef90868206c735f311c2f95644f562b1)#define RA\_ELC\_EVENT\_WDT0\_UNDERFLOW 0x053

[ 61](ra8t1-elc_8h.md#ae4dbb89c58220f72818cc9c28d97905b)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_0 0x058

[ 62](ra8t1-elc_8h.md#a0ef2efa2ea339cad7598f11fe549cdd9)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_1 0x059

[ 63](ra8t1-elc_8h.md#aac8d97813e8a3276bdac764faf7b580d)#define RA\_ELC\_EVENT\_USBFS\_INT 0x05A

[ 64](ra8t1-elc_8h.md#a9458dbf2b1da6fc51ca2c2933dcb6b37)#define RA\_ELC\_EVENT\_USBFS\_RESUME 0x05B

[ 65](ra8t1-elc_8h.md#a7271a25cdc3c987313efbafcd2a746cf)#define RA\_ELC\_EVENT\_IIC0\_RXI 0x05C

[ 66](ra8t1-elc_8h.md#a7843f8a23feb383202fa6ad3be8fae5c)#define RA\_ELC\_EVENT\_IIC0\_TXI 0x05D

[ 67](ra8t1-elc_8h.md#a52270344b26073c127a0269c5ec4e228)#define RA\_ELC\_EVENT\_IIC0\_TEI 0x05E

[ 68](ra8t1-elc_8h.md#a667eb763b55f973b141837e82dbbae6e)#define RA\_ELC\_EVENT\_IIC0\_ERI 0x05F

[ 69](ra8t1-elc_8h.md#a2a074dab614a1639ea5fa4f6d3baffd3)#define RA\_ELC\_EVENT\_IIC0\_WUI 0x060

[ 70](ra8t1-elc_8h.md#ad03e6b81d0e7ce53737e5c3022f8d951)#define RA\_ELC\_EVENT\_IIC1\_RXI 0x061

[ 71](ra8t1-elc_8h.md#a641c91157c98f41d3cf5ff6bbe25192d)#define RA\_ELC\_EVENT\_IIC1\_TXI 0x062

[ 72](ra8t1-elc_8h.md#a45ed226ccaace8813aa653276a52999d)#define RA\_ELC\_EVENT\_IIC1\_TEI 0x063

[ 73](ra8t1-elc_8h.md#a2221a129f0e323fa5b96bfe5ed0e007f)#define RA\_ELC\_EVENT\_IIC1\_ERI 0x064

[ 74](ra8t1-elc_8h.md#a5d9c7d15a5c040aa9dfe002cf9df0657)#define RA\_ELC\_EVENT\_SDHIMMC0\_ACCS 0x06B

[ 75](ra8t1-elc_8h.md#a93465058fd23dad3a735a53ad8689473)#define RA\_ELC\_EVENT\_SDHIMMC0\_SDIO 0x06C

[ 76](ra8t1-elc_8h.md#a2bf8474e011e2ec0360e9e46deb7e960)#define RA\_ELC\_EVENT\_SDHIMMC0\_CARD 0x06D

[ 77](ra8t1-elc_8h.md#a937bfe3314fb8d78775078db983ea473)#define RA\_ELC\_EVENT\_SDHIMMC0\_DMA\_REQ 0x06E

[ 78](ra8t1-elc_8h.md#a7195add88b927dd230e66a931713f4e0)#define RA\_ELC\_EVENT\_SDHIMMC1\_ACCS 0x06F

[ 79](ra8t1-elc_8h.md#a2dff7e869fad7918164e954bcb0a46bf)#define RA\_ELC\_EVENT\_SDHIMMC1\_SDIO 0x070

[ 80](ra8t1-elc_8h.md#ae8b2102091696bca7f60b008b9839444)#define RA\_ELC\_EVENT\_SDHIMMC1\_CARD 0x071

[ 81](ra8t1-elc_8h.md#a3b619f3e51ddcf2add17abd434bbf948)#define RA\_ELC\_EVENT\_SDHIMMC1\_DMA\_REQ 0x072

[ 82](ra8t1-elc_8h.md#a3bbee94907736c0c435cc5ff64d1e7ef)#define RA\_ELC\_EVENT\_ACMPHS0\_INT 0x07B

[ 83](ra8t1-elc_8h.md#ab1a4d1aee4743a0ee8bd194052a6c840)#define RA\_ELC\_EVENT\_ACMPHS1\_INT 0x07C

[ 84](ra8t1-elc_8h.md#ae5c28618f4e68eef6ca83bdcec515abb)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0 0x083

[ 85](ra8t1-elc_8h.md#a9f0b82bfff5ea2ba414ac0bccad9a34d)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1 0x084

[ 86](ra8t1-elc_8h.md#aee58e9a0c4313f0ec08f0652e5002008)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1 0x088

[ 87](ra8t1-elc_8h.md#a36d858520d28847eead0fbfe7950be2d)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2 0x089

[ 88](ra8t1-elc_8h.md#a545dadce70bbcea1116cd13490fe2571)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_3 0x08A

[ 89](ra8t1-elc_8h.md#a4e478b84ef99ae71c102ad3d5c71089a)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_4 0x08B

[ 90](ra8t1-elc_8h.md#a6ec3edb5e4de5bca1171ade1aa9ca19f)#define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR 0x08C

[ 91](ra8t1-elc_8h.md#a1390ee9467a9d093de1532f0703ec35f)#define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END 0x08D

[ 92](ra8t1-elc_8h.md#a3463c1e202ab7891521eda7196e1be80)#define RA\_ELC\_EVENT\_CAC\_OVERFLOW 0x08E

[ 93](ra8t1-elc_8h.md#a81e18423a1f61e34f0daab6f7367eae2)#define RA\_ELC\_EVENT\_POEG0\_EVENT 0x08F

[ 94](ra8t1-elc_8h.md#a2a43c2ce461fde766e66a4451929a875)#define RA\_ELC\_EVENT\_POEG1\_EVENT 0x090

[ 95](ra8t1-elc_8h.md#a7b5c16202b2491ba77319a180bcaa107)#define RA\_ELC\_EVENT\_POEG2\_EVENT 0x091

[ 96](ra8t1-elc_8h.md#ab39d06b130b93348c5fab589f1e0074e)#define RA\_ELC\_EVENT\_POEG3\_EVENT 0x092

[ 97](ra8t1-elc_8h.md#a8438d8d92e1950681388b40385a2c354)#define RA\_ELC\_EVENT\_OPS\_UVW\_EDGE 0x0A0

[ 98](ra8t1-elc_8h.md#aec8a8b590cc124ca12425f34b5a61020)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A 0x0A1

[ 99](ra8t1-elc_8h.md#ae1ed91479f405ac965da868e86bce533)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B 0x0A2

[ 100](ra8t1-elc_8h.md#a6d7c9090c21a8a0c497356050d649ec6)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_C 0x0A3

[ 101](ra8t1-elc_8h.md#af5b8ca097747bd987e81d8d81263aa81)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_D 0x0A4

[ 102](ra8t1-elc_8h.md#a9ebec21375578c0e52d953773373bf1e)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_E 0x0A5

[ 103](ra8t1-elc_8h.md#ad503a55a4548ff6ffd58e2b74d9eaf00)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_F 0x0A6

[ 104](ra8t1-elc_8h.md#a76692948000993fde4d286f1a521a6d2)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW 0x0A7

[ 105](ra8t1-elc_8h.md#a9edde37b8c0835978aa55d58d77c5ad5)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW 0x0A8

[ 106](ra8t1-elc_8h.md#a21a934c940f85a7e4e592167eb468fd3)#define RA\_ELC\_EVENT\_GPT0\_PC 0x0A9

[ 107](ra8t1-elc_8h.md#a33a428565bfa3237aa4eda10b982fc65)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A 0x0AA

[ 108](ra8t1-elc_8h.md#a5326aaf270290b524f8cb2e126d06602)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B 0x0AB

[ 109](ra8t1-elc_8h.md#a2e55bae34ab30f2d802b8eaf93dd3cfd)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C 0x0AC

[ 110](ra8t1-elc_8h.md#ada3870f40beeec10e9366e908ed980d0)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D 0x0AD

[ 111](ra8t1-elc_8h.md#a5d4f72e95b7bb76315b9ffa059730620)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E 0x0AE

[ 112](ra8t1-elc_8h.md#a548923b7385648e4f15fef4ecb315478)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F 0x0AF

[ 113](ra8t1-elc_8h.md#aa6eac7cf283073eea62fbaa1df2017f2)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW 0x0B0

[ 114](ra8t1-elc_8h.md#ae8cefd5f23897d43cffba4e91b7c8b5c)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW 0x0B1

[ 115](ra8t1-elc_8h.md#aa0208084abba3e2601c8cf7bb42837fd)#define RA\_ELC\_EVENT\_GPT1\_PC 0x0B2

[ 116](ra8t1-elc_8h.md#ad1a5796e0c70a988165765f2ce8c1e80)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A 0x0B3

[ 117](ra8t1-elc_8h.md#a73776ba7d66a478c92c6cb3dfed50af4)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B 0x0B4

[ 118](ra8t1-elc_8h.md#aa391fa888ded57351c9b62f54df1ce36)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C 0x0B5

[ 119](ra8t1-elc_8h.md#a90c7aa7bbddb04e6ae4b6eccb64a0e93)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D 0x0B6

[ 120](ra8t1-elc_8h.md#adbfb562e616a86a3e28f8c3f09553db9)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E 0x0B7

[ 121](ra8t1-elc_8h.md#a6f07945c82efae23754e34dc09bee884)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F 0x0B8

[ 122](ra8t1-elc_8h.md#aede7879166ef812139641122782d873b)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW 0x0B9

[ 123](ra8t1-elc_8h.md#ad71d20ad5434f219a61e0f0aded090d1)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW 0x0BA

[ 124](ra8t1-elc_8h.md#a3a03431df622c2be648d0450d88facc7)#define RA\_ELC\_EVENT\_GPT2\_PC 0x0BB

[ 125](ra8t1-elc_8h.md#a74526500dfb573fe21fbca739b1698e1)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A 0x0BC

[ 126](ra8t1-elc_8h.md#ac6cfac3496e4ab71c9bf84b43e06486a)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B 0x0BD

[ 127](ra8t1-elc_8h.md#a1af4840d468eb4c4e1672a34652ef583)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_C 0x0BE

[ 128](ra8t1-elc_8h.md#a263e6b02601dd37d6eedaab56a2e6fcd)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_D 0x0BF

[ 129](ra8t1-elc_8h.md#a9035e080d39d60ecc898a596b9902aa6)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_E 0x0C0

[ 130](ra8t1-elc_8h.md#a9cffb5aca60a4c7349789fc23fb197fb)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_F 0x0C1

[ 131](ra8t1-elc_8h.md#a546eff128c44a29f56fe90952cef475d)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW 0x0C2

[ 132](ra8t1-elc_8h.md#ab30a5683e48535abbf0c400a5a0d8946)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW 0x0C3

[ 133](ra8t1-elc_8h.md#ac39dad31699579a5ee3deebf4fc57cb4)#define RA\_ELC\_EVENT\_GPT3\_PC 0x0C4

[ 134](ra8t1-elc_8h.md#a8130aa176d9d5dd698c62708111515e0)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A 0x0C5

[ 135](ra8t1-elc_8h.md#aa77a30a219070d15e358a43fbbd89728)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B 0x0C6

[ 136](ra8t1-elc_8h.md#af6c1cb172b343baa8d8bbe01d1674922)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C 0x0C7

[ 137](ra8t1-elc_8h.md#ae8c7945c641045c615922a3f82329c56)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D 0x0C8

[ 138](ra8t1-elc_8h.md#afcb271a94d9b07b7b1a204f325b80d52)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E 0x0C9

[ 139](ra8t1-elc_8h.md#a906eb0e1ed2786ed2b14e4608489b2cc)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F 0x0CA

[ 140](ra8t1-elc_8h.md#abb820eb80ad8afc5c12dc3581fc7a0b9)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW 0x0CB

[ 141](ra8t1-elc_8h.md#a65831ae6b037607dc55a2b1e8aa296a7)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW 0x0CC

[ 142](ra8t1-elc_8h.md#adc4aceff99f296b06938254f9dcc1f2f)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A 0x0CE

[ 143](ra8t1-elc_8h.md#aad1fc8b32dffaaa64f9908951f8b1c64)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B 0x0CF

[ 144](ra8t1-elc_8h.md#aebaa50f4643efe5b87798777cee578bc)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C 0x0D0

[ 145](ra8t1-elc_8h.md#a21965e21bd4045aa5010925620b4d827)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D 0x0D1

[ 146](ra8t1-elc_8h.md#a51a7cb146f0efbb7bc9f7336031006a4)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E 0x0D2

[ 147](ra8t1-elc_8h.md#abbd0bd21af2bd1679d6d7bc36001b97d)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F 0x0D3

[ 148](ra8t1-elc_8h.md#a038e7580f03fbdd74f417108cd2a8b4d)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW 0x0D4

[ 149](ra8t1-elc_8h.md#ac38b8f1154d6a699923b2bbf249e38fd)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW 0x0D5

[ 150](ra8t1-elc_8h.md#acad1c37929903ddee569f40a3c5c59e3)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A 0x0D7

[ 151](ra8t1-elc_8h.md#aa0fc9b447efbcba0bb6800f785daeb96)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B 0x0D8

[ 152](ra8t1-elc_8h.md#a01f586bd98832ea9b8aa58741b61a319)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_C 0x0D9

[ 153](ra8t1-elc_8h.md#acd71c3b8e8e1d96aa3ff6affb93f5000)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_D 0x0DA

[ 154](ra8t1-elc_8h.md#a6abdcc7a6331a8283cfe0c1ac06b7d83)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_E 0x0DB

[ 155](ra8t1-elc_8h.md#a28b6b55ad533e3cb606b2b0937c916b3)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_F 0x0DC

[ 156](ra8t1-elc_8h.md#ac3c8dd6a5b7f95dccc58e7ec4e235a40)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW 0x0DD

[ 157](ra8t1-elc_8h.md#acdece33585a75fccba962e4f764058fb)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW 0x0DE

[ 158](ra8t1-elc_8h.md#afe1b39e5d37a5ed631dd18869cfbac8a)#define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A 0x0E0

[ 159](ra8t1-elc_8h.md#a53b7cfc8d0a000bd57f159b09b0a9c26)#define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B 0x0E1

[ 160](ra8t1-elc_8h.md#add91262eba9ec860b788030af153161a)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_C 0x0E2

[ 161](ra8t1-elc_8h.md#a9310fd708ca6f0afcf374bfc96e22e6e)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_D 0x0E3

[ 162](ra8t1-elc_8h.md#a8d18bd54c972d1de01c2a9f86e832cd0)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_E 0x0E4

[ 163](ra8t1-elc_8h.md#aca89f90e8afa3f656e76f5960717543c)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_F 0x0E5

[ 164](ra8t1-elc_8h.md#aac0ed7abde81cf4bcc7588bf64b53c04)#define RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW 0x0E6

[ 165](ra8t1-elc_8h.md#ab1935670b6c0a5b5629ef8ba9d854f6c)#define RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW 0x0E7

[ 166](ra8t1-elc_8h.md#acbe756d66c556dab820bbba06e67248c)#define RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_A 0x0E9

[ 167](ra8t1-elc_8h.md#a86965f2d57f55861ddb995b2b1381aae)#define RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_B 0x0EA

[ 168](ra8t1-elc_8h.md#af58a21982c9fb458bd12cf1d3922ffd2)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_C 0x0EB

[ 169](ra8t1-elc_8h.md#a9d76f5a9c5546d1410b741ec7862713c)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_D 0x0EC

[ 170](ra8t1-elc_8h.md#a9d6cf6e4081dd7ef14196fd754838224)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_E 0x0ED

[ 171](ra8t1-elc_8h.md#abac4f8da4010bc5753188cc9bbce4feb)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_F 0x0EE

[ 172](ra8t1-elc_8h.md#a560a2f23d31c99d46b5de3fb65b3c066)#define RA\_ELC\_EVENT\_GPT8\_COUNTER\_OVERFLOW 0x0EF

[ 173](ra8t1-elc_8h.md#a217a7f7cdd39114472fc4276fc2337a2)#define RA\_ELC\_EVENT\_GPT8\_COUNTER\_UNDERFLOW 0x0F0

[ 174](ra8t1-elc_8h.md#a2170a5524be189decf2d098d082e24fe)#define RA\_ELC\_EVENT\_GPT8\_PC 0x0F1

[ 175](ra8t1-elc_8h.md#a1b1bc8aa177575a9928b87d4270d3293)#define RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_A 0x0F2

[ 176](ra8t1-elc_8h.md#a9d37d2fabd4ff799c0b6a1f2e7131b50)#define RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_B 0x0F3

[ 177](ra8t1-elc_8h.md#a0654be705490f32e47348cb31dea046d)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_C 0x0F4

[ 178](ra8t1-elc_8h.md#af204da0f122a67c5374ebdcd231684b0)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_D 0x0F5

[ 179](ra8t1-elc_8h.md#a7af6cbe91bfe594230d36a60a684877c)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_E 0x0F6

[ 180](ra8t1-elc_8h.md#ad2ad78dddd8c2b7dc560ec75439870ce)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_F 0x0F7

[ 181](ra8t1-elc_8h.md#ab5599f7f5509cbdae09668ec09078625)#define RA\_ELC\_EVENT\_GPT9\_COUNTER\_OVERFLOW 0x0F8

[ 182](ra8t1-elc_8h.md#aab44882a60fd898b847597a64ad1ec05)#define RA\_ELC\_EVENT\_GPT9\_COUNTER\_UNDERFLOW 0x0F9

[ 183](ra8t1-elc_8h.md#acdae0456188e411e857278f0e543798d)#define RA\_ELC\_EVENT\_GPT9\_PC 0x0FA

[ 184](ra8t1-elc_8h.md#a3e446393f52c0b25041942b552e74816)#define RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_A 0x0FB

[ 185](ra8t1-elc_8h.md#a2333e30317873b25420483f93f9039e7)#define RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_B 0x0FC

[ 186](ra8t1-elc_8h.md#aae47fb3196b5989c45883943619dbe02)#define RA\_ELC\_EVENT\_GPT10\_COMPARE\_C 0x0FD

[ 187](ra8t1-elc_8h.md#a7210f910c16be4bdeae56e5d10b9ab94)#define RA\_ELC\_EVENT\_GPT10\_COMPARE\_D 0x0FE

[ 188](ra8t1-elc_8h.md#a7d195f17c9da519dae057c9d337e0443)#define RA\_ELC\_EVENT\_GPT10\_COMPARE\_E 0x0FF

[ 189](ra8t1-elc_8h.md#ae2ad03f6c166fc2470e3b76623f81444)#define RA\_ELC\_EVENT\_GPT10\_COMPARE\_F 0x100

[ 190](ra8t1-elc_8h.md#abbdcc7f1ec056632b1f162527570ebd4)#define RA\_ELC\_EVENT\_GPT10\_COUNTER\_OVERFLOW 0x101

[ 191](ra8t1-elc_8h.md#a7475c7d51460f60c7f1ace0e744b1e7f)#define RA\_ELC\_EVENT\_GPT10\_COUNTER\_UNDERFLOW 0x102

[ 192](ra8t1-elc_8h.md#a0f8cedfe7e3331d74adbee4ff6aa4dcc)#define RA\_ELC\_EVENT\_GPT10\_PC 0x103

[ 193](ra8t1-elc_8h.md#a71d10e75f9dc2beef51e422160a9b600)#define RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_A 0x104

[ 194](ra8t1-elc_8h.md#af45005c2897b2d3e17652426e7ba0ffb)#define RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_B 0x105

[ 195](ra8t1-elc_8h.md#af329a1e7556fc745376fb9912af82e85)#define RA\_ELC\_EVENT\_GPT11\_COMPARE\_C 0x106

[ 196](ra8t1-elc_8h.md#a38b26e657a05bf629e023e2cc18fec6d)#define RA\_ELC\_EVENT\_GPT11\_COMPARE\_D 0x107

[ 197](ra8t1-elc_8h.md#aa6967c733b94450076f0468049f8a580)#define RA\_ELC\_EVENT\_GPT11\_COMPARE\_E 0x108

[ 198](ra8t1-elc_8h.md#a5c504ecc48d5beb357cdd42292af6072)#define RA\_ELC\_EVENT\_GPT11\_COMPARE\_F 0x109

[ 199](ra8t1-elc_8h.md#a65114b19113928d597ea9e1040c63e86)#define RA\_ELC\_EVENT\_GPT11\_COUNTER\_OVERFLOW 0x10A

[ 200](ra8t1-elc_8h.md#ad17299e05623683967d4b3652df71050)#define RA\_ELC\_EVENT\_GPT11\_COUNTER\_UNDERFLOW 0x10B

[ 201](ra8t1-elc_8h.md#af703c7f5148f647cf99f15f5017b9b8e)#define RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_A 0x10D

[ 202](ra8t1-elc_8h.md#ab61dcfc42e758bd67fff2e3e0cc7462e)#define RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_B 0x10E

[ 203](ra8t1-elc_8h.md#a70cbb57f4225aa5064043caaeb34f14c)#define RA\_ELC\_EVENT\_GPT12\_COMPARE\_C 0x10F

[ 204](ra8t1-elc_8h.md#aac6e70fd9c5806050ca602cdfaff94af)#define RA\_ELC\_EVENT\_GPT12\_COMPARE\_D 0x110

[ 205](ra8t1-elc_8h.md#a542befd78aec05f096611817a090d542)#define RA\_ELC\_EVENT\_GPT12\_COMPARE\_E 0x111

[ 206](ra8t1-elc_8h.md#ac51ca6a913774b5dbb991a15fb37cf98)#define RA\_ELC\_EVENT\_GPT12\_COMPARE\_F 0x112

[ 207](ra8t1-elc_8h.md#ae3c96e8c252ccaf26b2059bd39d7de3a)#define RA\_ELC\_EVENT\_GPT12\_COUNTER\_OVERFLOW 0x113

[ 208](ra8t1-elc_8h.md#ad9d2590f2cfd624f475718d459fb3d45)#define RA\_ELC\_EVENT\_GPT12\_COUNTER\_UNDERFLOW 0x114

[ 209](ra8t1-elc_8h.md#a7a9e3e3d3c2c815e1a4696068ae4a1b4)#define RA\_ELC\_EVENT\_GPT13\_CAPTURE\_COMPARE\_A 0x116

[ 210](ra8t1-elc_8h.md#a516b477a84886d2b3bafb0445a5e058e)#define RA\_ELC\_EVENT\_GPT13\_CAPTURE\_COMPARE\_B 0x117

[ 211](ra8t1-elc_8h.md#aca23b053b565b5c46b09f58b2f9310bf)#define RA\_ELC\_EVENT\_GPT13\_COMPARE\_C 0x118

[ 212](ra8t1-elc_8h.md#a8dc369d2e6fa7ad1b6a9ce5cb1b43865)#define RA\_ELC\_EVENT\_GPT13\_COMPARE\_D 0x119

[ 213](ra8t1-elc_8h.md#afa734348cb5498039e88bc35dbf15d3e)#define RA\_ELC\_EVENT\_GPT13\_COMPARE\_E 0x11A

[ 214](ra8t1-elc_8h.md#a2366ee4fc54ba1c95e71f6c97af8052a)#define RA\_ELC\_EVENT\_GPT13\_COMPARE\_F 0x11B

[ 215](ra8t1-elc_8h.md#ac4f91952df6d2badfc33a314615d6326)#define RA\_ELC\_EVENT\_GPT13\_COUNTER\_OVERFLOW 0x11C

[ 216](ra8t1-elc_8h.md#a44d75ba5e9ebcb3cd3056f5205957370)#define RA\_ELC\_EVENT\_GPT13\_COUNTER\_UNDERFLOW 0x11D

[ 217](ra8t1-elc_8h.md#aea1fab1522d24393ee7292213df7d452)#define RA\_ELC\_EVENT\_EDMAC0\_EINT 0x120

[ 218](ra8t1-elc_8h.md#ad9e9a8451a683c5b5bc8a2ace8264c27)#define RA\_ELC\_EVENT\_SCI0\_RXI 0x124

[ 219](ra8t1-elc_8h.md#aecc4fdda2a7eeb2bab0b894f2e5047d9)#define RA\_ELC\_EVENT\_SCI0\_TXI 0x125

[ 220](ra8t1-elc_8h.md#ae845a850ab730c651badc5c857e28ee9)#define RA\_ELC\_EVENT\_SCI0\_TEI 0x126

[ 221](ra8t1-elc_8h.md#ad4580e769bae423298276e31ee2ee071)#define RA\_ELC\_EVENT\_SCI0\_ERI 0x127

[ 222](ra8t1-elc_8h.md#ad8c85ee25e4bbc5563d9878156232f8e)#define RA\_ELC\_EVENT\_SCI0\_AED 0x128

[ 223](ra8t1-elc_8h.md#a624bb86f4c26e04cc4b044b2f3f4aec9)#define RA\_ELC\_EVENT\_SCI0\_BFD 0x129

[ 224](ra8t1-elc_8h.md#ae2373b571584dae4d1c7fc57142ecb3c)#define RA\_ELC\_EVENT\_SCI0\_AM 0x12A

[ 225](ra8t1-elc_8h.md#ae936e9aa971a376cb4ea3405c68d57f0)#define RA\_ELC\_EVENT\_SCI1\_RXI 0x12B

[ 226](ra8t1-elc_8h.md#abd1c6187f97f2817dc5eb59278a996b1)#define RA\_ELC\_EVENT\_SCI1\_TXI 0x12C

[ 227](ra8t1-elc_8h.md#aae0ca4a1031af4c490fbb1ecbe201662)#define RA\_ELC\_EVENT\_SCI1\_TEI 0x12D

[ 228](ra8t1-elc_8h.md#a6a673466eb5261d23ee06be132ca9cde)#define RA\_ELC\_EVENT\_SCI1\_ERI 0x12E

[ 229](ra8t1-elc_8h.md#a85f1cff0bee1f3394e53dc4180fecbda)#define RA\_ELC\_EVENT\_SCI1\_AED 0x12F

[ 230](ra8t1-elc_8h.md#ae20f8922e54edb56904b397b6e77fda2)#define RA\_ELC\_EVENT\_SCI1\_BFD 0x130

[ 231](ra8t1-elc_8h.md#ad9ca7dbcac36bb7f921cd8b8db761623)#define RA\_ELC\_EVENT\_SCI1\_AM 0x131

[ 232](ra8t1-elc_8h.md#a484b0928fab1e96f3008b9e7b12bab07)#define RA\_ELC\_EVENT\_SCI2\_RXI 0x132

[ 233](ra8t1-elc_8h.md#a5991f7636af52ea3285cf17d300f62bb)#define RA\_ELC\_EVENT\_SCI2\_TXI 0x133

[ 234](ra8t1-elc_8h.md#a9bbdd2f449bfd5709f6c8b77b8378ca4)#define RA\_ELC\_EVENT\_SCI2\_TEI 0x134

[ 235](ra8t1-elc_8h.md#ad31428c7900c978dba266761df793f4c)#define RA\_ELC\_EVENT\_SCI2\_ERI 0x135

[ 236](ra8t1-elc_8h.md#a023110baac3b030238844ab6a8999652)#define RA\_ELC\_EVENT\_SCI2\_AM 0x138

[ 237](ra8t1-elc_8h.md#a87a1f07a2b420f9ce8d7ebcc1c505986)#define RA\_ELC\_EVENT\_SCI3\_RXI 0x139

[ 238](ra8t1-elc_8h.md#aee0548d7714ebd04748eadf9e9dbb97c)#define RA\_ELC\_EVENT\_SCI3\_TXI 0x13A

[ 239](ra8t1-elc_8h.md#a6f9d20424191f026030159511647f913)#define RA\_ELC\_EVENT\_SCI3\_TEI 0x13B

[ 240](ra8t1-elc_8h.md#ab7a6ad3ccc6279863a491a3787fd5c5e)#define RA\_ELC\_EVENT\_SCI3\_ERI 0x13C

[ 241](ra8t1-elc_8h.md#a075f80d14abaa63627574519b9ebf36b)#define RA\_ELC\_EVENT\_SCI3\_AM 0x13F

[ 242](ra8t1-elc_8h.md#afe86466482eb03b85da9feb17bdccfc0)#define RA\_ELC\_EVENT\_SCI4\_RXI 0x140

[ 243](ra8t1-elc_8h.md#a89f26e1bfd92cb7c9a2bad9acd80e553)#define RA\_ELC\_EVENT\_SCI4\_TXI 0x141

[ 244](ra8t1-elc_8h.md#a2554192500a5ac058fbd338d3018f6cc)#define RA\_ELC\_EVENT\_SCI4\_TEI 0x142

[ 245](ra8t1-elc_8h.md#ac6f2b3938cde7ba80faf523548dfa6c2)#define RA\_ELC\_EVENT\_SCI4\_ERI 0x143

[ 246](ra8t1-elc_8h.md#abddf2cbec24fd59c9330b0328a21f82e)#define RA\_ELC\_EVENT\_SCI4\_AM 0x146

[ 247](ra8t1-elc_8h.md#ac01e51a9360f409e430642d86818bf98)#define RA\_ELC\_EVENT\_SCI9\_RXI 0x163

[ 248](ra8t1-elc_8h.md#a8c628c59b08ed53781fd406ea22da796)#define RA\_ELC\_EVENT\_SCI9\_TXI 0x164

[ 249](ra8t1-elc_8h.md#ac3a064375ff90f3a6a35c5fdda680f95)#define RA\_ELC\_EVENT\_SCI9\_TEI 0x165

[ 250](ra8t1-elc_8h.md#af2e4d2d6b59c512e536d901789b3c1a2)#define RA\_ELC\_EVENT\_SCI9\_ERI 0x166

[ 251](ra8t1-elc_8h.md#a2bfc7def09c933262aa530227a45af7d)#define RA\_ELC\_EVENT\_SCI9\_AM 0x169

[ 252](ra8t1-elc_8h.md#af77608914a79bea7797b63674c71db31)#define RA\_ELC\_EVENT\_SPI0\_RXI 0x178

[ 253](ra8t1-elc_8h.md#a82d87016b5d694884bba33bf71e93e92)#define RA\_ELC\_EVENT\_SPI0\_TXI 0x179

[ 254](ra8t1-elc_8h.md#a920575ee3a202b0d7202cd053f1e235b)#define RA\_ELC\_EVENT\_SPI0\_IDLE 0x17A

[ 255](ra8t1-elc_8h.md#ab588fafc974153bcf94087cdb1a71d73)#define RA\_ELC\_EVENT\_SPI0\_ERI 0x17B

[ 256](ra8t1-elc_8h.md#a368a0ece3d89efe3ed8ab274471849b9)#define RA\_ELC\_EVENT\_SPI0\_TEI 0x17C

[ 257](ra8t1-elc_8h.md#a2f5e3b5957e42c572fda94ec535b401b)#define RA\_ELC\_EVENT\_SPI1\_RXI 0x17D

[ 258](ra8t1-elc_8h.md#a0aab8e60c14b34bccb74400a818524ac)#define RA\_ELC\_EVENT\_SPI1\_TXI 0x17E

[ 259](ra8t1-elc_8h.md#a73da76e435d9de6b6b7ad48190d2c0a2)#define RA\_ELC\_EVENT\_SPI1\_IDLE 0x17F

[ 260](ra8t1-elc_8h.md#aedf36efaaba39c4001386536d21f81e2)#define RA\_ELC\_EVENT\_SPI1\_ERI 0x180

[ 261](ra8t1-elc_8h.md#a60f40983e3c6344a257bd157b40069d5)#define RA\_ELC\_EVENT\_SPI1\_TEI 0x181

[ 262](ra8t1-elc_8h.md#a381d0e6b749cb12add2dfcb129f80468)#define RA\_ELC\_EVENT\_CAN\_RXF 0x185

[ 263](ra8t1-elc_8h.md#a05a66b601667344eff54e86b13a820d5)#define RA\_ELC\_EVENT\_CAN\_GLERR 0x186

[ 264](ra8t1-elc_8h.md#a92c3913b5074214a5468bc04672fa810)#define RA\_ELC\_EVENT\_CAN0\_DMAREQ0 0x187

[ 265](ra8t1-elc_8h.md#abb607aea1165ee35308c39315bbf028c)#define RA\_ELC\_EVENT\_CAN0\_DMAREQ1 0x188

[ 266](ra8t1-elc_8h.md#a5706bcde62bd7ac9270c238e329cd15b)#define RA\_ELC\_EVENT\_CAN1\_DMAREQ0 0x18B

[ 267](ra8t1-elc_8h.md#a78395b5c4124a198b660c1da53539655)#define RA\_ELC\_EVENT\_CAN1\_DMAREQ1 0x18C

[ 268](ra8t1-elc_8h.md#a31b33463c8527b56ad5760d86f066c6c)#define RA\_ELC\_EVENT\_CAN0\_TX 0x18F

[ 269](ra8t1-elc_8h.md#a0c01b6adbdd0b29b4390a34acfee339b)#define RA\_ELC\_EVENT\_CAN0\_CHERR 0x190

[ 270](ra8t1-elc_8h.md#a84cb35e4a3dfad95529937db4966c63f)#define RA\_ELC\_EVENT\_CAN0\_COMFRX 0x191

[ 271](ra8t1-elc_8h.md#a5d73e70c306cc7cd5d89a9963b9075f5)#define RA\_ELC\_EVENT\_CAN0\_CF\_DMAREQ 0x192

[ 272](ra8t1-elc_8h.md#aa7871b154ba1e9bbb8a48aeeec65e416)#define RA\_ELC\_EVENT\_CAN0\_RXMB 0x193

[ 273](ra8t1-elc_8h.md#ab669f854f92ae61862b1c7a49f857426)#define RA\_ELC\_EVENT\_CAN1\_TX 0x194

[ 274](ra8t1-elc_8h.md#a98005eb9ea9f3a087cb9fbcbdd842bed)#define RA\_ELC\_EVENT\_CAN1\_CHERR 0x195

[ 275](ra8t1-elc_8h.md#a0a8fe1d10e62f54b4b87568686bc1f64)#define RA\_ELC\_EVENT\_CAN1\_COMFRX 0x196

[ 276](ra8t1-elc_8h.md#a3da879a9c8eb950aeca9041cb8ff8fc9)#define RA\_ELC\_EVENT\_CAN1\_CF\_DMAREQ 0x197

[ 277](ra8t1-elc_8h.md#abb9be46f4f5af6e6731c40bf8229e811)#define RA\_ELC\_EVENT\_CAN1\_RXMB 0x198

[ 278](ra8t1-elc_8h.md#adf49b7c6aecfae965cd0040817b11a5d)#define RA\_ELC\_EVENT\_CAN0\_MRAM\_ERI 0x19B

[ 279](ra8t1-elc_8h.md#a5d5dc4797ff132feaa1dbeb0d18620a4)#define RA\_ELC\_EVENT\_CAN1\_MRAM\_ERI 0x19C

[ 280](ra8t1-elc_8h.md#a3080239b71b12d15d9cd78d78a0b65e6)#define RA\_ELC\_EVENT\_I3C0\_RESPONSE 0x19D

[ 281](ra8t1-elc_8h.md#a92a8148f568fcf39ccde3817aef8ae9d)#define RA\_ELC\_EVENT\_I3C0\_COMMAND 0x19E

[ 282](ra8t1-elc_8h.md#a2060363167f356732fb5b817e4dbcdb5)#define RA\_ELC\_EVENT\_I3C0\_IBI 0x19F

[ 283](ra8t1-elc_8h.md#a3b2265686fb51c1ae5cdc549cac4b3fd)#define RA\_ELC\_EVENT\_I3C0\_RX 0x1A0

[ 284](ra8t1-elc_8h.md#ac12a24178c5964cdd58666f7d57a1b1b)#define RA\_ELC\_EVENT\_IICB0\_RXI 0x1A0

[ 285](ra8t1-elc_8h.md#a6bd966e36dba524e3e5ad37250d9a2fe)#define RA\_ELC\_EVENT\_I3C0\_TX 0x1A1

[ 286](ra8t1-elc_8h.md#ac3f18d838eb617f5022034a38238b3da)#define RA\_ELC\_EVENT\_IICB0\_TXI 0x1A1

[ 287](ra8t1-elc_8h.md#a0fe2a3ad8bf5bc9f9fbe79c2e3142a82)#define RA\_ELC\_EVENT\_I3C0\_RCV\_STATUS 0x1A2

[ 288](ra8t1-elc_8h.md#ad03e0236533be6c8a679f45dae45b5f3)#define RA\_ELC\_EVENT\_I3C0\_HRESP 0x1A3

[ 289](ra8t1-elc_8h.md#a41c98f2bad994edd460738fc681d1915)#define RA\_ELC\_EVENT\_I3C0\_HCMD 0x1A4

[ 290](ra8t1-elc_8h.md#a6944a47bc40eaf5be0bcd9a8ea3f61b3)#define RA\_ELC\_EVENT\_I3C0\_HRX 0x1A5

[ 291](ra8t1-elc_8h.md#a79b1703b94f1d6a62c589cd442d6c285)#define RA\_ELC\_EVENT\_I3C0\_HTX 0x1A6

[ 292](ra8t1-elc_8h.md#a263d9beac3bda75a81b657995262df84)#define RA\_ELC\_EVENT\_I3C0\_TEND 0x1A7

[ 293](ra8t1-elc_8h.md#accb1b88c154566410d539b20c64f67cc)#define RA\_ELC\_EVENT\_IICB0\_TEI 0x1A7

[ 294](ra8t1-elc_8h.md#a7031d655983b5a153dec583b24df13fe)#define RA\_ELC\_EVENT\_I3C0\_EEI 0x1A8

[ 295](ra8t1-elc_8h.md#ac0d8b1e8f379ef983dfd2004ed02e65e)#define RA\_ELC\_EVENT\_IICB0\_ERI 0x1A8

[ 296](ra8t1-elc_8h.md#a57e6e464e10dc72ef057cb24530f26cc)#define RA\_ELC\_EVENT\_I3C0\_STEV 0x1A9

[ 297](ra8t1-elc_8h.md#a80adbdbcc1c63c9623763c8aa595c3ca)#define RA\_ELC\_EVENT\_I3C0\_MREFOVF 0x1AA

[ 298](ra8t1-elc_8h.md#a53d989fdbde5fa99dfcb6226c3419ab9)#define RA\_ELC\_EVENT\_I3C0\_MREFCPT 0x1AB

[ 299](ra8t1-elc_8h.md#a1fdeb36ba55249ba92f2bdb425f18d74)#define RA\_ELC\_EVENT\_I3C0\_AMEV 0x1AC

[ 300](ra8t1-elc_8h.md#a979332348cebe774723bfd610b02c36b)#define RA\_ELC\_EVENT\_I3C0\_WU 0x1AD

[ 301](ra8t1-elc_8h.md#ad7284976213551f7d4fa450bf2bf8c7c)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END 0x1AE

[ 302](ra8t1-elc_8h.md#aecbe4efa29972b832e35ebb00d7499ad)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B 0x1AF

[ 303](ra8t1-elc_8h.md#aa4feb2c3e29ba84d1397c618b7b860bf)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A 0x1B0

[ 304](ra8t1-elc_8h.md#ab59c8ec4f20de5cf4709efe0a7ee70a1)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B 0x1B1

[ 305](ra8t1-elc_8h.md#af187c78a1f05fc4be81aa3af36e4cde5)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH 0x1B2

[ 306](ra8t1-elc_8h.md#a65d6c499a6852434b4802f8ef7066eb4)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH 0x1B3

[ 307](ra8t1-elc_8h.md#aa02ddf9a93b64b5fb5c6d60b51bc24ed)#define RA\_ELC\_EVENT\_ADC1\_SCAN\_END 0x1B4

[ 308](ra8t1-elc_8h.md#a1c3786e7e0f56f55d45ed55901a14bb4)#define RA\_ELC\_EVENT\_ADC1\_SCAN\_END\_B 0x1B5

[ 309](ra8t1-elc_8h.md#aef02cb8109fd68b4c4a1a5efca255583)#define RA\_ELC\_EVENT\_ADC1\_WINDOW\_A 0x1B6

[ 310](ra8t1-elc_8h.md#a283756acfcfe4c208cbaa5a3edd4d2cc)#define RA\_ELC\_EVENT\_ADC1\_WINDOW\_B 0x1B7

[ 311](ra8t1-elc_8h.md#adbc3a9f438323aed719c7e210829a78f)#define RA\_ELC\_EVENT\_ADC1\_COMPARE\_MATCH 0x1B8

[ 312](ra8t1-elc_8h.md#a12123fbc57d65b4ab932495bf0726d57)#define RA\_ELC\_EVENT\_ADC1\_COMPARE\_MISMATCH 0x1B9

[ 313](ra8t1-elc_8h.md#ab6c210d6481294137fd4bc32c39e5de1)#define RA\_ELC\_EVENT\_DOC\_INT 0x1BA

[ 314](ra8t1-elc_8h.md#a0b76751d4c1e7f98ec6de2633cca4057)#define RA\_ELC\_EVENT\_RSIP\_TADI 0x1BC

315

316/\* Possible peripherals to be linked to event signals \*/

[ 317](ra8t1-elc_8h.md#ad6bb2d32abfad10bd283894efb7fe968)#define RA\_ELC\_PERIPHERAL\_GPT\_A 0

[ 318](ra8t1-elc_8h.md#a8c4b99abfaa798b3b15f3435a73bad86)#define RA\_ELC\_PERIPHERAL\_GPT\_B 1

[ 319](ra8t1-elc_8h.md#af0000625eec82c9f4ebe20da1cec7c66)#define RA\_ELC\_PERIPHERAL\_GPT\_C 2

[ 320](ra8t1-elc_8h.md#ae9ae748233cce2fa65b334c2f8b2a6f7)#define RA\_ELC\_PERIPHERAL\_GPT\_D 3

[ 321](ra8t1-elc_8h.md#aefc3deade612ed7aa53abd397d20af3b)#define RA\_ELC\_PERIPHERAL\_GPT\_E 4

[ 322](ra8t1-elc_8h.md#a4bb2ffb785a17a225d5eb6e80f0040bf)#define RA\_ELC\_PERIPHERAL\_GPT\_F 5

[ 323](ra8t1-elc_8h.md#a2ccd7f6730384fb8550054ea2195a67a)#define RA\_ELC\_PERIPHERAL\_GPT\_G 6

[ 324](ra8t1-elc_8h.md#a6e737df13755e4e0039e98610aa31f3c)#define RA\_ELC\_PERIPHERAL\_GPT\_H 7

[ 325](ra8t1-elc_8h.md#a2b5a9232a4ad9d199dc9baa510d0ed54)#define RA\_ELC\_PERIPHERAL\_ADC0 8

[ 326](ra8t1-elc_8h.md#afaf4059726139d62e2c09010cfa1148a)#define RA\_ELC\_PERIPHERAL\_ADC0\_B 9

[ 327](ra8t1-elc_8h.md#aea69e6e72e14f53afeb85aa4a9349bcb)#define RA\_ELC\_PERIPHERAL\_ADC1 10

[ 328](ra8t1-elc_8h.md#adbd2118aea6d1ba6ca67de192f0033fc)#define RA\_ELC\_PERIPHERAL\_ADC1\_B 11

[ 329](ra8t1-elc_8h.md#a9a32ba5817467743fbcf24b698124b02)#define RA\_ELC\_PERIPHERAL\_DAC0 12

[ 330](ra8t1-elc_8h.md#a84aa20e3793499f427f6c9ccb7a20566)#define RA\_ELC\_PERIPHERAL\_DAC1 13

[ 331](ra8t1-elc_8h.md#a5830e830b7b10cd68441de2648edd6a0)#define RA\_ELC\_PERIPHERAL\_IOPORT1 14

[ 332](ra8t1-elc_8h.md#a42d4feb2c854cc1964455297e6d7eb72)#define RA\_ELC\_PERIPHERAL\_IOPORT2 15

[ 333](ra8t1-elc_8h.md#a349933f20d7b6f768e49239724d0c5f7)#define RA\_ELC\_PERIPHERAL\_IOPORT3 16

[ 334](ra8t1-elc_8h.md#a6d08d1db64f903fa2dacfc81568b004d)#define RA\_ELC\_PERIPHERAL\_IOPORT4 17

[ 335](ra8t1-elc_8h.md#a44df9c541681520b5fb529348b8deb81)#define RA\_ELC\_PERIPHERAL\_I3C 30

336

337#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA8T1\_ELC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [misc](dir_b5927901ba0eeb0fdf9ca7870f5af60a.md)
- [renesas](dir_86b946318bd38151d049d676c19e4b11.md)
- [ra-elc](dir_fc824a581c07e3e227952b4fed9afa76.md)
- [ra8t1-elc.h](ra8t1-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
