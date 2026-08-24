---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra6m5-elc_8h_source.html
original_path: doxygen/html/ra6m5-elc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra6m5-elc.h

[Go to the documentation of this file.](ra6m5-elc_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA6M5\_ELC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA6M5\_ELC\_H\_

9

10/\* Sources of event signals to be linked to other peripherals or the CPU \*/

[ 11](ra6m5-elc_8h.md#a11b5cec97472328120a8d6381f1e8809)#define RA\_ELC\_EVENT\_NONE 0x0

[ 12](ra6m5-elc_8h.md#a04ee26d7188b7441627bb89249545cfa)#define RA\_ELC\_EVENT\_ICU\_IRQ0 0x001

[ 13](ra6m5-elc_8h.md#ac9f6681c03b50d8b3a24798b3e790170)#define RA\_ELC\_EVENT\_ICU\_IRQ1 0x002

[ 14](ra6m5-elc_8h.md#a136f93a17eea3f4233b0012c075fc904)#define RA\_ELC\_EVENT\_ICU\_IRQ2 0x003

[ 15](ra6m5-elc_8h.md#a65b92e543dfb43c213274652ae60314a)#define RA\_ELC\_EVENT\_ICU\_IRQ3 0x004

[ 16](ra6m5-elc_8h.md#a2b1930fc54010b7c4c00f286f690cb1e)#define RA\_ELC\_EVENT\_ICU\_IRQ4 0x005

[ 17](ra6m5-elc_8h.md#af3ecccfe646b6cac991310abe3e4b955)#define RA\_ELC\_EVENT\_ICU\_IRQ5 0x006

[ 18](ra6m5-elc_8h.md#a98b53eb7b5979403023805ba925c504c)#define RA\_ELC\_EVENT\_ICU\_IRQ6 0x007

[ 19](ra6m5-elc_8h.md#ab6f05849ddc30ceb693f57b522223bcf)#define RA\_ELC\_EVENT\_ICU\_IRQ7 0x008

[ 20](ra6m5-elc_8h.md#acbcd1c55530c6cb8580b76bd55c73c90)#define RA\_ELC\_EVENT\_ICU\_IRQ8 0x009

[ 21](ra6m5-elc_8h.md#af04ed29327af6c108875334c24d98e43)#define RA\_ELC\_EVENT\_ICU\_IRQ9 0x00A

[ 22](ra6m5-elc_8h.md#a3e9a895c4855c3db6ac7fc5900b57807)#define RA\_ELC\_EVENT\_ICU\_IRQ10 0x00B

[ 23](ra6m5-elc_8h.md#a46f43f1dd26e006c26b11bd45e53a728)#define RA\_ELC\_EVENT\_ICU\_IRQ11 0x00C

[ 24](ra6m5-elc_8h.md#affb7ae86a41c8cc8582e6c6ef284a5d8)#define RA\_ELC\_EVENT\_ICU\_IRQ12 0x00D

[ 25](ra6m5-elc_8h.md#ad7435ed602899357eae0f46c09bf542c)#define RA\_ELC\_EVENT\_ICU\_IRQ13 0x00E

[ 26](ra6m5-elc_8h.md#ada7702d0ac50f9b3e82ef50d6be50470)#define RA\_ELC\_EVENT\_ICU\_IRQ14 0x00F

[ 27](ra6m5-elc_8h.md#afab294cf0d58a5bb4dd578774b0ad9aa)#define RA\_ELC\_EVENT\_ICU\_IRQ15 0x010

[ 28](ra6m5-elc_8h.md#a906929a9ae7dd7de44d21a32d3635080)#define RA\_ELC\_EVENT\_DMAC0\_INT 0x020

[ 29](ra6m5-elc_8h.md#a76b9d9fa8af16a1480fcc8d8ec12572f)#define RA\_ELC\_EVENT\_DMAC1\_INT 0x021

[ 30](ra6m5-elc_8h.md#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)#define RA\_ELC\_EVENT\_DMAC2\_INT 0x022

[ 31](ra6m5-elc_8h.md#a0b9d72a41fd7c5b27e6c31967645b907)#define RA\_ELC\_EVENT\_DMAC3\_INT 0x023

[ 32](ra6m5-elc_8h.md#a4cae5afbbe49719555bbbfa12b8727f5)#define RA\_ELC\_EVENT\_DMAC4\_INT 0x024

[ 33](ra6m5-elc_8h.md#a000e31aba8a821f4358a435d280b3a7b)#define RA\_ELC\_EVENT\_DMAC5\_INT 0x025

[ 34](ra6m5-elc_8h.md#a2d1f6d1c797a0d787a5d5c08b0fc18ad)#define RA\_ELC\_EVENT\_DMAC6\_INT 0x026

[ 35](ra6m5-elc_8h.md#ae8caef45a510d4c4f1c55f923e01799e)#define RA\_ELC\_EVENT\_DMAC7\_INT 0x027

[ 36](ra6m5-elc_8h.md#a9a58e3a2c10447906aaf35bab5664d24)#define RA\_ELC\_EVENT\_DTC\_COMPLETE 0x029

[ 37](ra6m5-elc_8h.md#a5ab484cdaf470b47e95005d83d60394f)#define RA\_ELC\_EVENT\_DTC\_END 0x02A

[ 38](ra6m5-elc_8h.md#a54d8c74eefe8f9b237ea23e18033d947)#define RA\_ELC\_EVENT\_DMA\_TRANSERR 0x02B

[ 39](ra6m5-elc_8h.md#a26e0aaa4a17196ada130bbb714a6d3bd)#define RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL 0x02D

[ 40](ra6m5-elc_8h.md#a5c7545a2f69856b7b637ad690f158b77)#define RA\_ELC\_EVENT\_FCU\_FIFERR 0x030

[ 41](ra6m5-elc_8h.md#a535af54c8bcfff47cc90ba1226044d71)#define RA\_ELC\_EVENT\_FCU\_FRDYI 0x031

[ 42](ra6m5-elc_8h.md#a7ab275777147d06315a04abb3f2f6d51)#define RA\_ELC\_EVENT\_LVD\_LVD1 0x038

[ 43](ra6m5-elc_8h.md#ad52acadba107b7f907d678f44769a4cb)#define RA\_ELC\_EVENT\_LVD\_LVD2 0x039

[ 44](ra6m5-elc_8h.md#a290decf4254396cbce267cb52a619717)#define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP 0x03B

[ 45](ra6m5-elc_8h.md#ac6953f0c8caa6b5ef8c9893c7ff4baa1)#define RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST 0x03C

[ 46](ra6m5-elc_8h.md#a4c3604a42ead1d43f472e901087ec148)#define RA\_ELC\_EVENT\_AGT0\_INT 0x040

[ 47](ra6m5-elc_8h.md#a015e6f8aed4b467f4554e6887b4d9ec9)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A 0x041

[ 48](ra6m5-elc_8h.md#ada1ad302dc5b987a6f7c972afae729f2)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B 0x042

[ 49](ra6m5-elc_8h.md#a635180e38c932579072f4eebd665592f)#define RA\_ELC\_EVENT\_AGT1\_INT 0x043

[ 50](ra6m5-elc_8h.md#aeb2399818b6b141ab4a37e257dba22be)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A 0x044

[ 51](ra6m5-elc_8h.md#a1d660c78348b48ea7a072225491ae44b)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B 0x045

[ 52](ra6m5-elc_8h.md#aace60e1ca05855c0838298c51510943d)#define RA\_ELC\_EVENT\_AGT2\_INT 0x046

[ 53](ra6m5-elc_8h.md#ac7d2ceb7c70898f96e4ef1606b96191f)#define RA\_ELC\_EVENT\_AGT2\_COMPARE\_A 0x047

[ 54](ra6m5-elc_8h.md#afa53449537c7ad67c71f495848781b9d)#define RA\_ELC\_EVENT\_AGT2\_COMPARE\_B 0x048

[ 55](ra6m5-elc_8h.md#a4a1e74d4c1ab5f1b6039550e3b518089)#define RA\_ELC\_EVENT\_AGT3\_INT 0x049

[ 56](ra6m5-elc_8h.md#a4500621826d716e3050e8e5e88d68a16)#define RA\_ELC\_EVENT\_AGT3\_COMPARE\_A 0x04A

[ 57](ra6m5-elc_8h.md#a93641e55a6c8db7ae55e3b83376d997d)#define RA\_ELC\_EVENT\_AGT3\_COMPARE\_B 0x04B

[ 58](ra6m5-elc_8h.md#a294a37bcea64966af82ba7d9d6abb9b2)#define RA\_ELC\_EVENT\_AGT4\_INT 0x04C

[ 59](ra6m5-elc_8h.md#a6de0e3ed42d1a72b0d65186aec0f876e)#define RA\_ELC\_EVENT\_AGT4\_COMPARE\_A 0x04D

[ 60](ra6m5-elc_8h.md#a8839f5e131612a48386381983e2d914f)#define RA\_ELC\_EVENT\_AGT4\_COMPARE\_B 0x04E

[ 61](ra6m5-elc_8h.md#acbb0c43bed869c27a8a90e8cb8166bb4)#define RA\_ELC\_EVENT\_AGT5\_INT 0x04F

[ 62](ra6m5-elc_8h.md#a7ab1f11da949fca8067e82cd437b142a)#define RA\_ELC\_EVENT\_AGT5\_COMPARE\_A 0x050

[ 63](ra6m5-elc_8h.md#a78b5abeca0f03176a19464f3c2d9508d)#define RA\_ELC\_EVENT\_AGT5\_COMPARE\_B 0x051

[ 64](ra6m5-elc_8h.md#abc837f1fcfffeb2ec231c79336379dda)#define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW 0x052

[ 65](ra6m5-elc_8h.md#a6cdb7a60a850f9ec23f19c548a6cc544)#define RA\_ELC\_EVENT\_WDT\_UNDERFLOW 0x053

[ 66](ra6m5-elc_8h.md#a76fd68b555574159d563d2dfd68d90b9)#define RA\_ELC\_EVENT\_RTC\_ALARM 0x054

[ 67](ra6m5-elc_8h.md#a144901ee7b31b96eba18a39d98c4b953)#define RA\_ELC\_EVENT\_RTC\_PERIOD 0x055

[ 68](ra6m5-elc_8h.md#a241cd3c65033b46a1160d5815cc86fd7)#define RA\_ELC\_EVENT\_RTC\_CARRY 0x056

[ 69](ra6m5-elc_8h.md#a381d0e6b749cb12add2dfcb129f80468)#define RA\_ELC\_EVENT\_CAN\_RXF 0x059

[ 70](ra6m5-elc_8h.md#a05a66b601667344eff54e86b13a820d5)#define RA\_ELC\_EVENT\_CAN\_GLERR 0x05A

[ 71](ra6m5-elc_8h.md#a3961be8854a154802e42c54ce6ae19d7)#define RA\_ELC\_EVENT\_CAN\_DMAREQ0 0x05B

[ 72](ra6m5-elc_8h.md#a9ba34879d45c552845396b0a86dfaa26)#define RA\_ELC\_EVENT\_CAN\_DMAREQ1 0x05C

[ 73](ra6m5-elc_8h.md#a08aea5a9c09b29338e8c0cff9829c33f)#define RA\_ELC\_EVENT\_CAN\_DMAREQ2 0x05D

[ 74](ra6m5-elc_8h.md#a1784b33d28a1dd91bcdea1bfff3a501d)#define RA\_ELC\_EVENT\_CAN\_DMAREQ3 0x05E

[ 75](ra6m5-elc_8h.md#aeb78ac72275efd1d184079ddb300cef8)#define RA\_ELC\_EVENT\_CAN\_DMAREQ4 0x05F

[ 76](ra6m5-elc_8h.md#aca57e8892543d75119a625da5f66c1f1)#define RA\_ELC\_EVENT\_CAN\_DMAREQ5 0x060

[ 77](ra6m5-elc_8h.md#acbb28c227297a0a756d2af78d2fae180)#define RA\_ELC\_EVENT\_CAN\_DMAREQ6 0x061

[ 78](ra6m5-elc_8h.md#afedbbe495dce9216dc4d2f44ebaa9373)#define RA\_ELC\_EVENT\_CAN\_DMAREQ7 0x062

[ 79](ra6m5-elc_8h.md#a31b33463c8527b56ad5760d86f066c6c)#define RA\_ELC\_EVENT\_CAN0\_TX 0x063

[ 80](ra6m5-elc_8h.md#a0c01b6adbdd0b29b4390a34acfee339b)#define RA\_ELC\_EVENT\_CAN0\_CHERR 0x064

[ 81](ra6m5-elc_8h.md#a84cb35e4a3dfad95529937db4966c63f)#define RA\_ELC\_EVENT\_CAN0\_COMFRX 0x065

[ 82](ra6m5-elc_8h.md#a5d73e70c306cc7cd5d89a9963b9075f5)#define RA\_ELC\_EVENT\_CAN0\_CF\_DMAREQ 0x066

[ 83](ra6m5-elc_8h.md#ab669f854f92ae61862b1c7a49f857426)#define RA\_ELC\_EVENT\_CAN1\_TX 0x067

[ 84](ra6m5-elc_8h.md#a98005eb9ea9f3a087cb9fbcbdd842bed)#define RA\_ELC\_EVENT\_CAN1\_CHERR 0x068

[ 85](ra6m5-elc_8h.md#a0a8fe1d10e62f54b4b87568686bc1f64)#define RA\_ELC\_EVENT\_CAN1\_COMFRX 0x069

[ 86](ra6m5-elc_8h.md#a3da879a9c8eb950aeca9041cb8ff8fc9)#define RA\_ELC\_EVENT\_CAN1\_CF\_DMAREQ 0x06A

[ 87](ra6m5-elc_8h.md#ae4dbb89c58220f72818cc9c28d97905b)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_0 0x06B

[ 88](ra6m5-elc_8h.md#a0ef2efa2ea339cad7598f11fe549cdd9)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_1 0x06C

[ 89](ra6m5-elc_8h.md#aac8d97813e8a3276bdac764faf7b580d)#define RA\_ELC\_EVENT\_USBFS\_INT 0x06D

[ 90](ra6m5-elc_8h.md#a9458dbf2b1da6fc51ca2c2933dcb6b37)#define RA\_ELC\_EVENT\_USBFS\_RESUME 0x06E

[ 91](ra6m5-elc_8h.md#a7271a25cdc3c987313efbafcd2a746cf)#define RA\_ELC\_EVENT\_IIC0\_RXI 0x073

[ 92](ra6m5-elc_8h.md#a7843f8a23feb383202fa6ad3be8fae5c)#define RA\_ELC\_EVENT\_IIC0\_TXI 0x074

[ 93](ra6m5-elc_8h.md#a52270344b26073c127a0269c5ec4e228)#define RA\_ELC\_EVENT\_IIC0\_TEI 0x075

[ 94](ra6m5-elc_8h.md#a667eb763b55f973b141837e82dbbae6e)#define RA\_ELC\_EVENT\_IIC0\_ERI 0x076

[ 95](ra6m5-elc_8h.md#a2a074dab614a1639ea5fa4f6d3baffd3)#define RA\_ELC\_EVENT\_IIC0\_WUI 0x077

[ 96](ra6m5-elc_8h.md#ad03e6b81d0e7ce53737e5c3022f8d951)#define RA\_ELC\_EVENT\_IIC1\_RXI 0x078

[ 97](ra6m5-elc_8h.md#a641c91157c98f41d3cf5ff6bbe25192d)#define RA\_ELC\_EVENT\_IIC1\_TXI 0x079

[ 98](ra6m5-elc_8h.md#a45ed226ccaace8813aa653276a52999d)#define RA\_ELC\_EVENT\_IIC1\_TEI 0x07A

[ 99](ra6m5-elc_8h.md#a2221a129f0e323fa5b96bfe5ed0e007f)#define RA\_ELC\_EVENT\_IIC1\_ERI 0x07B

[ 100](ra6m5-elc_8h.md#a9fa82701141f3b108a45ef78ba186dbb)#define RA\_ELC\_EVENT\_IIC2\_RXI 0x07D

[ 101](ra6m5-elc_8h.md#ab0acad4ad4d3c980f37e5cc665b08925)#define RA\_ELC\_EVENT\_IIC2\_TXI 0x07E

[ 102](ra6m5-elc_8h.md#ab47dd216ff1fe2799242bd81841e4bb4)#define RA\_ELC\_EVENT\_IIC2\_TEI 0x07F

[ 103](ra6m5-elc_8h.md#a63bb5f6fd1a17c813327061f9f3f8097)#define RA\_ELC\_EVENT\_IIC2\_ERI 0x080

[ 104](ra6m5-elc_8h.md#a5d9c7d15a5c040aa9dfe002cf9df0657)#define RA\_ELC\_EVENT\_SDHIMMC0\_ACCS 0x082

[ 105](ra6m5-elc_8h.md#a93465058fd23dad3a735a53ad8689473)#define RA\_ELC\_EVENT\_SDHIMMC0\_SDIO 0x083

[ 106](ra6m5-elc_8h.md#a2bf8474e011e2ec0360e9e46deb7e960)#define RA\_ELC\_EVENT\_SDHIMMC0\_CARD 0x084

[ 107](ra6m5-elc_8h.md#a937bfe3314fb8d78775078db983ea473)#define RA\_ELC\_EVENT\_SDHIMMC0\_DMA\_REQ 0x085

[ 108](ra6m5-elc_8h.md#ac65193048ce5734b46bc2bf77b84cb4e)#define RA\_ELC\_EVENT\_SSI0\_TXI 0x08A

[ 109](ra6m5-elc_8h.md#ab736656ae0b06de8383189075cbb2f27)#define RA\_ELC\_EVENT\_SSI0\_RXI 0x08B

[ 110](ra6m5-elc_8h.md#a1a89e9ab6abb3834992ee3ea3ebaf9c4)#define RA\_ELC\_EVENT\_SSI0\_INT 0x08D

[ 111](ra6m5-elc_8h.md#a2faf033bad7b355f8beb9386a2d0e93b)#define RA\_ELC\_EVENT\_CTSU\_WRITE 0x09A

[ 112](ra6m5-elc_8h.md#ad7cd21f5db3e117b87ffab8a6cb47272)#define RA\_ELC\_EVENT\_CTSU\_READ 0x09B

[ 113](ra6m5-elc_8h.md#acfe8138822bcd3f02fe50316e40c7641)#define RA\_ELC\_EVENT\_CTSU\_END 0x09C

[ 114](ra6m5-elc_8h.md#a6ec3edb5e4de5bca1171ade1aa9ca19f)#define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR 0x09E

[ 115](ra6m5-elc_8h.md#a1390ee9467a9d093de1532f0703ec35f)#define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END 0x09F

[ 116](ra6m5-elc_8h.md#a3463c1e202ab7891521eda7196e1be80)#define RA\_ELC\_EVENT\_CAC\_OVERFLOW 0x0A0

[ 117](ra6m5-elc_8h.md#a99b37093de561bf4289c57b65299946a)#define RA\_ELC\_EVENT\_CEC\_INTDA 0x0AB

[ 118](ra6m5-elc_8h.md#ae30dbb0a9aef9ad39e9c9998b3df27bd)#define RA\_ELC\_EVENT\_CEC\_INTCE 0x0AC

[ 119](ra6m5-elc_8h.md#aa07c92068ed7f5b00114c5f8ae26cf87)#define RA\_ELC\_EVENT\_CEC\_INTERR 0x0AD

[ 120](ra6m5-elc_8h.md#aee58e9a0c4313f0ec08f0652e5002008)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1 0x0B1

[ 121](ra6m5-elc_8h.md#a36d858520d28847eead0fbfe7950be2d)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2 0x0B2

[ 122](ra6m5-elc_8h.md#a545dadce70bbcea1116cd13490fe2571)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_3 0x0B3

[ 123](ra6m5-elc_8h.md#a4e478b84ef99ae71c102ad3d5c71089a)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_4 0x0B4

[ 124](ra6m5-elc_8h.md#ae5c28618f4e68eef6ca83bdcec515abb)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0 0x0B5

[ 125](ra6m5-elc_8h.md#a9f0b82bfff5ea2ba414ac0bccad9a34d)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1 0x0B6

[ 126](ra6m5-elc_8h.md#a81e18423a1f61e34f0daab6f7367eae2)#define RA\_ELC\_EVENT\_POEG0\_EVENT 0x0B7

[ 127](ra6m5-elc_8h.md#a2a43c2ce461fde766e66a4451929a875)#define RA\_ELC\_EVENT\_POEG1\_EVENT 0x0B8

[ 128](ra6m5-elc_8h.md#a7b5c16202b2491ba77319a180bcaa107)#define RA\_ELC\_EVENT\_POEG2\_EVENT 0x0B9

[ 129](ra6m5-elc_8h.md#ab39d06b130b93348c5fab589f1e0074e)#define RA\_ELC\_EVENT\_POEG3\_EVENT 0x0BA

[ 130](ra6m5-elc_8h.md#aec8a8b590cc124ca12425f34b5a61020)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A 0x0C0

[ 131](ra6m5-elc_8h.md#ae1ed91479f405ac965da868e86bce533)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B 0x0C1

[ 132](ra6m5-elc_8h.md#a6d7c9090c21a8a0c497356050d649ec6)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_C 0x0C2

[ 133](ra6m5-elc_8h.md#af5b8ca097747bd987e81d8d81263aa81)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_D 0x0C3

[ 134](ra6m5-elc_8h.md#a9ebec21375578c0e52d953773373bf1e)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_E 0x0C4

[ 135](ra6m5-elc_8h.md#ad503a55a4548ff6ffd58e2b74d9eaf00)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_F 0x0C5

[ 136](ra6m5-elc_8h.md#a76692948000993fde4d286f1a521a6d2)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW 0x0C6

[ 137](ra6m5-elc_8h.md#a9edde37b8c0835978aa55d58d77c5ad5)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW 0x0C7

[ 138](ra6m5-elc_8h.md#a21a934c940f85a7e4e592167eb468fd3)#define RA\_ELC\_EVENT\_GPT0\_PC 0x0C8

[ 139](ra6m5-elc_8h.md#a33a428565bfa3237aa4eda10b982fc65)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A 0x0C9

[ 140](ra6m5-elc_8h.md#a5326aaf270290b524f8cb2e126d06602)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B 0x0CA

[ 141](ra6m5-elc_8h.md#a2e55bae34ab30f2d802b8eaf93dd3cfd)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C 0x0CB

[ 142](ra6m5-elc_8h.md#ada3870f40beeec10e9366e908ed980d0)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D 0x0CC

[ 143](ra6m5-elc_8h.md#a5d4f72e95b7bb76315b9ffa059730620)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E 0x0CD

[ 144](ra6m5-elc_8h.md#a548923b7385648e4f15fef4ecb315478)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F 0x0CE

[ 145](ra6m5-elc_8h.md#aa6eac7cf283073eea62fbaa1df2017f2)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW 0x0CF

[ 146](ra6m5-elc_8h.md#ae8cefd5f23897d43cffba4e91b7c8b5c)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW 0x0D0

[ 147](ra6m5-elc_8h.md#aa0208084abba3e2601c8cf7bb42837fd)#define RA\_ELC\_EVENT\_GPT1\_PC 0x0D1

[ 148](ra6m5-elc_8h.md#ad1a5796e0c70a988165765f2ce8c1e80)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A 0x0D2

[ 149](ra6m5-elc_8h.md#a73776ba7d66a478c92c6cb3dfed50af4)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B 0x0D3

[ 150](ra6m5-elc_8h.md#aa391fa888ded57351c9b62f54df1ce36)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C 0x0D4

[ 151](ra6m5-elc_8h.md#a90c7aa7bbddb04e6ae4b6eccb64a0e93)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D 0x0D5

[ 152](ra6m5-elc_8h.md#adbfb562e616a86a3e28f8c3f09553db9)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E 0x0D6

[ 153](ra6m5-elc_8h.md#a6f07945c82efae23754e34dc09bee884)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F 0x0D7

[ 154](ra6m5-elc_8h.md#aede7879166ef812139641122782d873b)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW 0x0D8

[ 155](ra6m5-elc_8h.md#ad71d20ad5434f219a61e0f0aded090d1)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW 0x0D9

[ 156](ra6m5-elc_8h.md#a74526500dfb573fe21fbca739b1698e1)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A 0x0DB

[ 157](ra6m5-elc_8h.md#ac6cfac3496e4ab71c9bf84b43e06486a)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B 0x0DC

[ 158](ra6m5-elc_8h.md#a1af4840d468eb4c4e1672a34652ef583)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_C 0x0DD

[ 159](ra6m5-elc_8h.md#a263e6b02601dd37d6eedaab56a2e6fcd)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_D 0x0DE

[ 160](ra6m5-elc_8h.md#a9035e080d39d60ecc898a596b9902aa6)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_E 0x0DF

[ 161](ra6m5-elc_8h.md#a9cffb5aca60a4c7349789fc23fb197fb)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_F 0x0E0

[ 162](ra6m5-elc_8h.md#a546eff128c44a29f56fe90952cef475d)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW 0x0E1

[ 163](ra6m5-elc_8h.md#ab30a5683e48535abbf0c400a5a0d8946)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW 0x0E2

[ 164](ra6m5-elc_8h.md#a8130aa176d9d5dd698c62708111515e0)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A 0x0E4

[ 165](ra6m5-elc_8h.md#aa77a30a219070d15e358a43fbbd89728)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B 0x0E5

[ 166](ra6m5-elc_8h.md#af6c1cb172b343baa8d8bbe01d1674922)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C 0x0E6

[ 167](ra6m5-elc_8h.md#ae8c7945c641045c615922a3f82329c56)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D 0x0E7

[ 168](ra6m5-elc_8h.md#afcb271a94d9b07b7b1a204f325b80d52)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E 0x0E8

[ 169](ra6m5-elc_8h.md#a906eb0e1ed2786ed2b14e4608489b2cc)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F 0x0E9

[ 170](ra6m5-elc_8h.md#abb820eb80ad8afc5c12dc3581fc7a0b9)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW 0x0EA

[ 171](ra6m5-elc_8h.md#a65831ae6b037607dc55a2b1e8aa296a7)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW 0x0EB

[ 172](ra6m5-elc_8h.md#af3ae1988661f1d68bd7cd5e36fb387f6)#define RA\_ELC\_EVENT\_GPT4\_PC 0x0EC

[ 173](ra6m5-elc_8h.md#adc4aceff99f296b06938254f9dcc1f2f)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A 0x0ED

[ 174](ra6m5-elc_8h.md#aad1fc8b32dffaaa64f9908951f8b1c64)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B 0x0EE

[ 175](ra6m5-elc_8h.md#aebaa50f4643efe5b87798777cee578bc)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C 0x0EF

[ 176](ra6m5-elc_8h.md#a21965e21bd4045aa5010925620b4d827)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D 0x0F0

[ 177](ra6m5-elc_8h.md#a51a7cb146f0efbb7bc9f7336031006a4)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E 0x0F1

[ 178](ra6m5-elc_8h.md#abbd0bd21af2bd1679d6d7bc36001b97d)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F 0x0F2

[ 179](ra6m5-elc_8h.md#a038e7580f03fbdd74f417108cd2a8b4d)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW 0x0F3

[ 180](ra6m5-elc_8h.md#ac38b8f1154d6a699923b2bbf249e38fd)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW 0x0F4

[ 181](ra6m5-elc_8h.md#aa7e87dac91e6416a1b1a23ae5ee82b55)#define RA\_ELC\_EVENT\_GPT5\_PC 0x0F5

[ 182](ra6m5-elc_8h.md#acad1c37929903ddee569f40a3c5c59e3)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A 0x0F6

[ 183](ra6m5-elc_8h.md#aa0fc9b447efbcba0bb6800f785daeb96)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B 0x0F7

[ 184](ra6m5-elc_8h.md#a01f586bd98832ea9b8aa58741b61a319)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_C 0x0F8

[ 185](ra6m5-elc_8h.md#acd71c3b8e8e1d96aa3ff6affb93f5000)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_D 0x0F9

[ 186](ra6m5-elc_8h.md#a6abdcc7a6331a8283cfe0c1ac06b7d83)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_E 0x0FA

[ 187](ra6m5-elc_8h.md#a28b6b55ad533e3cb606b2b0937c916b3)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_F 0x0FB

[ 188](ra6m5-elc_8h.md#ac3c8dd6a5b7f95dccc58e7ec4e235a40)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW 0x0FC

[ 189](ra6m5-elc_8h.md#acdece33585a75fccba962e4f764058fb)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW 0x0FD

[ 190](ra6m5-elc_8h.md#ae3a504e2ac861f8ab94b28bbfcb803ea)#define RA\_ELC\_EVENT\_GPT6\_PC 0x0FE

[ 191](ra6m5-elc_8h.md#afe1b39e5d37a5ed631dd18869cfbac8a)#define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A 0x0FF

[ 192](ra6m5-elc_8h.md#a53b7cfc8d0a000bd57f159b09b0a9c26)#define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B 0x100

[ 193](ra6m5-elc_8h.md#add91262eba9ec860b788030af153161a)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_C 0x101

[ 194](ra6m5-elc_8h.md#a9310fd708ca6f0afcf374bfc96e22e6e)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_D 0x102

[ 195](ra6m5-elc_8h.md#a8d18bd54c972d1de01c2a9f86e832cd0)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_E 0x103

[ 196](ra6m5-elc_8h.md#aca89f90e8afa3f656e76f5960717543c)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_F 0x104

[ 197](ra6m5-elc_8h.md#aac0ed7abde81cf4bcc7588bf64b53c04)#define RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW 0x105

[ 198](ra6m5-elc_8h.md#ab1935670b6c0a5b5629ef8ba9d854f6c)#define RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW 0x106

[ 199](ra6m5-elc_8h.md#acbe756d66c556dab820bbba06e67248c)#define RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_A 0x108

[ 200](ra6m5-elc_8h.md#a86965f2d57f55861ddb995b2b1381aae)#define RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_B 0x109

[ 201](ra6m5-elc_8h.md#af58a21982c9fb458bd12cf1d3922ffd2)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_C 0x10A

[ 202](ra6m5-elc_8h.md#a9d76f5a9c5546d1410b741ec7862713c)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_D 0x10B

[ 203](ra6m5-elc_8h.md#a9d6cf6e4081dd7ef14196fd754838224)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_E 0x10C

[ 204](ra6m5-elc_8h.md#abac4f8da4010bc5753188cc9bbce4feb)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_F 0x10D

[ 205](ra6m5-elc_8h.md#a560a2f23d31c99d46b5de3fb65b3c066)#define RA\_ELC\_EVENT\_GPT8\_COUNTER\_OVERFLOW 0x10E

[ 206](ra6m5-elc_8h.md#a217a7f7cdd39114472fc4276fc2337a2)#define RA\_ELC\_EVENT\_GPT8\_COUNTER\_UNDERFLOW 0x10F

[ 207](ra6m5-elc_8h.md#a1b1bc8aa177575a9928b87d4270d3293)#define RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_A 0x111

[ 208](ra6m5-elc_8h.md#a9d37d2fabd4ff799c0b6a1f2e7131b50)#define RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_B 0x112

[ 209](ra6m5-elc_8h.md#a0654be705490f32e47348cb31dea046d)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_C 0x113

[ 210](ra6m5-elc_8h.md#af204da0f122a67c5374ebdcd231684b0)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_D 0x114

[ 211](ra6m5-elc_8h.md#a7af6cbe91bfe594230d36a60a684877c)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_E 0x115

[ 212](ra6m5-elc_8h.md#ad2ad78dddd8c2b7dc560ec75439870ce)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_F 0x116

[ 213](ra6m5-elc_8h.md#ab5599f7f5509cbdae09668ec09078625)#define RA\_ELC\_EVENT\_GPT9\_COUNTER\_OVERFLOW 0x117

[ 214](ra6m5-elc_8h.md#aab44882a60fd898b847597a64ad1ec05)#define RA\_ELC\_EVENT\_GPT9\_COUNTER\_UNDERFLOW 0x118

[ 215](ra6m5-elc_8h.md#a8438d8d92e1950681388b40385a2c354)#define RA\_ELC\_EVENT\_OPS\_UVW\_EDGE 0x150

[ 216](ra6m5-elc_8h.md#ad7284976213551f7d4fa450bf2bf8c7c)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END 0x160

[ 217](ra6m5-elc_8h.md#aecbe4efa29972b832e35ebb00d7499ad)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B 0x161

[ 218](ra6m5-elc_8h.md#aa4feb2c3e29ba84d1397c618b7b860bf)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A 0x162

[ 219](ra6m5-elc_8h.md#ab59c8ec4f20de5cf4709efe0a7ee70a1)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B 0x163

[ 220](ra6m5-elc_8h.md#af187c78a1f05fc4be81aa3af36e4cde5)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH 0x164

[ 221](ra6m5-elc_8h.md#a65d6c499a6852434b4802f8ef7066eb4)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH 0x165

[ 222](ra6m5-elc_8h.md#aa02ddf9a93b64b5fb5c6d60b51bc24ed)#define RA\_ELC\_EVENT\_ADC1\_SCAN\_END 0x166

[ 223](ra6m5-elc_8h.md#a1c3786e7e0f56f55d45ed55901a14bb4)#define RA\_ELC\_EVENT\_ADC1\_SCAN\_END\_B 0x167

[ 224](ra6m5-elc_8h.md#aef02cb8109fd68b4c4a1a5efca255583)#define RA\_ELC\_EVENT\_ADC1\_WINDOW\_A 0x168

[ 225](ra6m5-elc_8h.md#a283756acfcfe4c208cbaa5a3edd4d2cc)#define RA\_ELC\_EVENT\_ADC1\_WINDOW\_B 0x169

[ 226](ra6m5-elc_8h.md#adbc3a9f438323aed719c7e210829a78f)#define RA\_ELC\_EVENT\_ADC1\_COMPARE\_MATCH 0x16A

[ 227](ra6m5-elc_8h.md#a12123fbc57d65b4ab932495bf0726d57)#define RA\_ELC\_EVENT\_ADC1\_COMPARE\_MISMATCH 0x16B

[ 228](ra6m5-elc_8h.md#aea1fab1522d24393ee7292213df7d452)#define RA\_ELC\_EVENT\_EDMAC0\_EINT 0x16F

[ 229](ra6m5-elc_8h.md#a1f824a01b81720cfd0fd63603f446567)#define RA\_ELC\_EVENT\_USBHS\_FIFO\_0 0x17D

[ 230](ra6m5-elc_8h.md#a39b1f6234c0f4e3a27663410e748b2c4)#define RA\_ELC\_EVENT\_USBHS\_FIFO\_1 0x17E

[ 231](ra6m5-elc_8h.md#a650605a9b87c871a6f29efb4d029f346)#define RA\_ELC\_EVENT\_USBHS\_USB\_INT\_RESUME 0x17F

[ 232](ra6m5-elc_8h.md#ad9e9a8451a683c5b5bc8a2ace8264c27)#define RA\_ELC\_EVENT\_SCI0\_RXI 0x180

[ 233](ra6m5-elc_8h.md#aecc4fdda2a7eeb2bab0b894f2e5047d9)#define RA\_ELC\_EVENT\_SCI0\_TXI 0x181

[ 234](ra6m5-elc_8h.md#ae845a850ab730c651badc5c857e28ee9)#define RA\_ELC\_EVENT\_SCI0\_TEI 0x182

[ 235](ra6m5-elc_8h.md#ad4580e769bae423298276e31ee2ee071)#define RA\_ELC\_EVENT\_SCI0\_ERI 0x183

[ 236](ra6m5-elc_8h.md#ae2373b571584dae4d1c7fc57142ecb3c)#define RA\_ELC\_EVENT\_SCI0\_AM 0x184

[ 237](ra6m5-elc_8h.md#ad52a4c7660a4e609976f7045305f8ca7)#define RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI 0x185

[ 238](ra6m5-elc_8h.md#ae936e9aa971a376cb4ea3405c68d57f0)#define RA\_ELC\_EVENT\_SCI1\_RXI 0x186

[ 239](ra6m5-elc_8h.md#abd1c6187f97f2817dc5eb59278a996b1)#define RA\_ELC\_EVENT\_SCI1\_TXI 0x187

[ 240](ra6m5-elc_8h.md#aae0ca4a1031af4c490fbb1ecbe201662)#define RA\_ELC\_EVENT\_SCI1\_TEI 0x188

[ 241](ra6m5-elc_8h.md#a6a673466eb5261d23ee06be132ca9cde)#define RA\_ELC\_EVENT\_SCI1\_ERI 0x189

[ 242](ra6m5-elc_8h.md#a484b0928fab1e96f3008b9e7b12bab07)#define RA\_ELC\_EVENT\_SCI2\_RXI 0x18C

[ 243](ra6m5-elc_8h.md#a5991f7636af52ea3285cf17d300f62bb)#define RA\_ELC\_EVENT\_SCI2\_TXI 0x18D

[ 244](ra6m5-elc_8h.md#a9bbdd2f449bfd5709f6c8b77b8378ca4)#define RA\_ELC\_EVENT\_SCI2\_TEI 0x18E

[ 245](ra6m5-elc_8h.md#ad31428c7900c978dba266761df793f4c)#define RA\_ELC\_EVENT\_SCI2\_ERI 0x18F

[ 246](ra6m5-elc_8h.md#a87a1f07a2b420f9ce8d7ebcc1c505986)#define RA\_ELC\_EVENT\_SCI3\_RXI 0x192

[ 247](ra6m5-elc_8h.md#aee0548d7714ebd04748eadf9e9dbb97c)#define RA\_ELC\_EVENT\_SCI3\_TXI 0x193

[ 248](ra6m5-elc_8h.md#a6f9d20424191f026030159511647f913)#define RA\_ELC\_EVENT\_SCI3\_TEI 0x194

[ 249](ra6m5-elc_8h.md#ab7a6ad3ccc6279863a491a3787fd5c5e)#define RA\_ELC\_EVENT\_SCI3\_ERI 0x195

[ 250](ra6m5-elc_8h.md#a075f80d14abaa63627574519b9ebf36b)#define RA\_ELC\_EVENT\_SCI3\_AM 0x196

[ 251](ra6m5-elc_8h.md#afe86466482eb03b85da9feb17bdccfc0)#define RA\_ELC\_EVENT\_SCI4\_RXI 0x198

[ 252](ra6m5-elc_8h.md#a89f26e1bfd92cb7c9a2bad9acd80e553)#define RA\_ELC\_EVENT\_SCI4\_TXI 0x199

[ 253](ra6m5-elc_8h.md#a2554192500a5ac058fbd338d3018f6cc)#define RA\_ELC\_EVENT\_SCI4\_TEI 0x19A

[ 254](ra6m5-elc_8h.md#ac6f2b3938cde7ba80faf523548dfa6c2)#define RA\_ELC\_EVENT\_SCI4\_ERI 0x19B

[ 255](ra6m5-elc_8h.md#abddf2cbec24fd59c9330b0328a21f82e)#define RA\_ELC\_EVENT\_SCI4\_AM 0x19C

[ 256](ra6m5-elc_8h.md#a51740f23e6c28b09c16c0e2f581314fb)#define RA\_ELC\_EVENT\_SCI5\_RXI 0x19E

[ 257](ra6m5-elc_8h.md#af7bc39c6c12ba036d65b2bb0af51dbf8)#define RA\_ELC\_EVENT\_SCI5\_TXI 0x19F

[ 258](ra6m5-elc_8h.md#a4cec5a06fc28cef155af5b98c251bccc)#define RA\_ELC\_EVENT\_SCI5\_TEI 0x1A0

[ 259](ra6m5-elc_8h.md#a24438f7b2a2a39e5e0c0b791d8600b49)#define RA\_ELC\_EVENT\_SCI5\_ERI 0x1A1

[ 260](ra6m5-elc_8h.md#abcd8c1f9dea5b100f1dcb2c146fbb9ae)#define RA\_ELC\_EVENT\_SCI5\_AM 0x1A2

[ 261](ra6m5-elc_8h.md#aaaa4496b6388f9f1984d377b9218f273)#define RA\_ELC\_EVENT\_SCI6\_RXI 0x1A4

[ 262](ra6m5-elc_8h.md#a1f464f460630421ac7fac8d36f893541)#define RA\_ELC\_EVENT\_SCI6\_TXI 0x1A5

[ 263](ra6m5-elc_8h.md#af5cd0171f29206eefea5cc40e341e5af)#define RA\_ELC\_EVENT\_SCI6\_TEI 0x1A6

[ 264](ra6m5-elc_8h.md#ad3452bf919efa5d499d0789bda0c6813)#define RA\_ELC\_EVENT\_SCI6\_ERI 0x1A7

[ 265](ra6m5-elc_8h.md#a55e0390228ab1793329886478314b385)#define RA\_ELC\_EVENT\_SCI6\_AM 0x1A8

[ 266](ra6m5-elc_8h.md#a651065265cfc7bd513f2cba96a86b550)#define RA\_ELC\_EVENT\_SCI7\_RXI 0x1AA

[ 267](ra6m5-elc_8h.md#a32d0ee0a89fc1eb303df1284152249fc)#define RA\_ELC\_EVENT\_SCI7\_TXI 0x1AB

[ 268](ra6m5-elc_8h.md#a7cfd544a71b7a0baf3399eca5c294fc5)#define RA\_ELC\_EVENT\_SCI7\_TEI 0x1AC

[ 269](ra6m5-elc_8h.md#a838905f0a53f835294343cccb54bd320)#define RA\_ELC\_EVENT\_SCI7\_ERI 0x1AD

[ 270](ra6m5-elc_8h.md#afa1387a41202d99a37507bf05c0e3b79)#define RA\_ELC\_EVENT\_SCI7\_AM 0x1AE

[ 271](ra6m5-elc_8h.md#afd0fe00167d99961d779e4b042db872a)#define RA\_ELC\_EVENT\_SCI8\_RXI 0x1B0

[ 272](ra6m5-elc_8h.md#ab8cc1c2b5ba23fe5550852ac7aaa33c0)#define RA\_ELC\_EVENT\_SCI8\_TXI 0x1B1

[ 273](ra6m5-elc_8h.md#ae9b08fd3131d828f67dda3523a7703be)#define RA\_ELC\_EVENT\_SCI8\_TEI 0x1B2

[ 274](ra6m5-elc_8h.md#a00d75172222030ff4002afb25513fbb8)#define RA\_ELC\_EVENT\_SCI8\_ERI 0x1B3

[ 275](ra6m5-elc_8h.md#a53e9096dcd5e219f5bb989768cb0672b)#define RA\_ELC\_EVENT\_SCI8\_AM 0x1B4

[ 276](ra6m5-elc_8h.md#ac01e51a9360f409e430642d86818bf98)#define RA\_ELC\_EVENT\_SCI9\_RXI 0x1B6

[ 277](ra6m5-elc_8h.md#a8c628c59b08ed53781fd406ea22da796)#define RA\_ELC\_EVENT\_SCI9\_TXI 0x1B7

[ 278](ra6m5-elc_8h.md#ac3a064375ff90f3a6a35c5fdda680f95)#define RA\_ELC\_EVENT\_SCI9\_TEI 0x1B8

[ 279](ra6m5-elc_8h.md#af2e4d2d6b59c512e536d901789b3c1a2)#define RA\_ELC\_EVENT\_SCI9\_ERI 0x1B9

[ 280](ra6m5-elc_8h.md#a2bfc7def09c933262aa530227a45af7d)#define RA\_ELC\_EVENT\_SCI9\_AM 0x1BA

[ 281](ra6m5-elc_8h.md#a0868e2affd206180949c9e8a16512aeb)#define RA\_ELC\_EVENT\_SCIX0\_SCIX0 0x1BC

[ 282](ra6m5-elc_8h.md#a059e08dbeb3bf41f992ab33085d4b559)#define RA\_ELC\_EVENT\_SCI1\_SCIX0 0x1BC

[ 283](ra6m5-elc_8h.md#a673915ae3283591ccde1365a473b375b)#define RA\_ELC\_EVENT\_SCIX0\_SCIX1 0x1BD

[ 284](ra6m5-elc_8h.md#a7fa308e3efc8ede2c36793108a5fadc6)#define RA\_ELC\_EVENT\_SCI1\_SCIX1 0x1BD

[ 285](ra6m5-elc_8h.md#a8e4c0c4ebb64da86dcf10602c3aeeafa)#define RA\_ELC\_EVENT\_SCIX0\_SCIX2 0x1BE

[ 286](ra6m5-elc_8h.md#a4a02bfdadeac5d5aeeaa6f2ab61fce32)#define RA\_ELC\_EVENT\_SCI1\_SCIX2 0x1BE

[ 287](ra6m5-elc_8h.md#aefeb3afc94bc45f4d0685cd597a38f31)#define RA\_ELC\_EVENT\_SCIX0\_SCIX3 0x1BF

[ 288](ra6m5-elc_8h.md#a036591d072e2d946584f4b2e6c7b9c92)#define RA\_ELC\_EVENT\_SCI1\_SCIX3 0x1BF

[ 289](ra6m5-elc_8h.md#ac655b617ac0e0525d1af250e587360ed)#define RA\_ELC\_EVENT\_SCIX1\_SCIX0 0x1C0

[ 290](ra6m5-elc_8h.md#af6572c17d77fda88b9ffb4109607e4bd)#define RA\_ELC\_EVENT\_SCI2\_SCIX0 0x1C0

[ 291](ra6m5-elc_8h.md#ac95f008072c6c46bb05afdf7c32782e5)#define RA\_ELC\_EVENT\_SCIX1\_SCIX1 0x1C1

[ 292](ra6m5-elc_8h.md#a028d6552fe10ec34193fea052b622d52)#define RA\_ELC\_EVENT\_SCI2\_SCIX1 0x1C1

[ 293](ra6m5-elc_8h.md#a55df555fb23aea59bd27ac35e1960c5c)#define RA\_ELC\_EVENT\_SCIX1\_SCIX2 0x1C2

[ 294](ra6m5-elc_8h.md#aa451fc81b1c3d4c60534c64ebaf0a620)#define RA\_ELC\_EVENT\_SCI2\_SCIX2 0x1C2

[ 295](ra6m5-elc_8h.md#ac801b7e5b210f40ec6f1fdd561f1b304)#define RA\_ELC\_EVENT\_SCIX1\_SCIX3 0x1C3

[ 296](ra6m5-elc_8h.md#ac56c2bfc9f79e3534b9c54a89cd6a43a)#define RA\_ELC\_EVENT\_SCI2\_SCIX3 0x1C3

[ 297](ra6m5-elc_8h.md#af77608914a79bea7797b63674c71db31)#define RA\_ELC\_EVENT\_SPI0\_RXI 0x1C4

[ 298](ra6m5-elc_8h.md#a82d87016b5d694884bba33bf71e93e92)#define RA\_ELC\_EVENT\_SPI0\_TXI 0x1C5

[ 299](ra6m5-elc_8h.md#a920575ee3a202b0d7202cd053f1e235b)#define RA\_ELC\_EVENT\_SPI0\_IDLE 0x1C6

[ 300](ra6m5-elc_8h.md#ab588fafc974153bcf94087cdb1a71d73)#define RA\_ELC\_EVENT\_SPI0\_ERI 0x1C7

[ 301](ra6m5-elc_8h.md#a368a0ece3d89efe3ed8ab274471849b9)#define RA\_ELC\_EVENT\_SPI0\_TEI 0x1C8

[ 302](ra6m5-elc_8h.md#a2f5e3b5957e42c572fda94ec535b401b)#define RA\_ELC\_EVENT\_SPI1\_RXI 0x1C9

[ 303](ra6m5-elc_8h.md#a0aab8e60c14b34bccb74400a818524ac)#define RA\_ELC\_EVENT\_SPI1\_TXI 0x1CA

[ 304](ra6m5-elc_8h.md#a73da76e435d9de6b6b7ad48190d2c0a2)#define RA\_ELC\_EVENT\_SPI1\_IDLE 0x1CB

[ 305](ra6m5-elc_8h.md#aedf36efaaba39c4001386536d21f81e2)#define RA\_ELC\_EVENT\_SPI1\_ERI 0x1CC

[ 306](ra6m5-elc_8h.md#a60f40983e3c6344a257bd157b40069d5)#define RA\_ELC\_EVENT\_SPI1\_TEI 0x1CD

[ 307](ra6m5-elc_8h.md#a9b13480ffc153227ff16bda09bd99544)#define RA\_ELC\_EVENT\_CAN\_AFLRAM0\_ERI 0x1CE

[ 308](ra6m5-elc_8h.md#ad313fc1ca60c08eb45721c6ff56261a9)#define RA\_ELC\_EVENT\_CAN\_AFLRAM1\_ERI 0x1CF

[ 309](ra6m5-elc_8h.md#adf49b7c6aecfae965cd0040817b11a5d)#define RA\_ELC\_EVENT\_CAN0\_MRAM\_ERI 0x1D0

[ 310](ra6m5-elc_8h.md#a556dae1058709337c18914886941de95)#define RA\_ELC\_EVENT\_OSPI\_INT 0x1D9

[ 311](ra6m5-elc_8h.md#a344b216f0d5880b31e7c1a4e700c85a4)#define RA\_ELC\_EVENT\_QSPI\_INT 0x1DA

[ 312](ra6m5-elc_8h.md#ab6c210d6481294137fd4bc32c39e5de1)#define RA\_ELC\_EVENT\_DOC\_INT 0x1DB

313

314/\* Possible peripherals to be linked to event signals \*/

[ 315](ra6m5-elc_8h.md#ad6bb2d32abfad10bd283894efb7fe968)#define RA\_ELC\_PERIPHERAL\_GPT\_A 0

[ 316](ra6m5-elc_8h.md#a8c4b99abfaa798b3b15f3435a73bad86)#define RA\_ELC\_PERIPHERAL\_GPT\_B 1

[ 317](ra6m5-elc_8h.md#af0000625eec82c9f4ebe20da1cec7c66)#define RA\_ELC\_PERIPHERAL\_GPT\_C 2

[ 318](ra6m5-elc_8h.md#ae9ae748233cce2fa65b334c2f8b2a6f7)#define RA\_ELC\_PERIPHERAL\_GPT\_D 3

[ 319](ra6m5-elc_8h.md#aefc3deade612ed7aa53abd397d20af3b)#define RA\_ELC\_PERIPHERAL\_GPT\_E 4

[ 320](ra6m5-elc_8h.md#a4bb2ffb785a17a225d5eb6e80f0040bf)#define RA\_ELC\_PERIPHERAL\_GPT\_F 5

[ 321](ra6m5-elc_8h.md#a2ccd7f6730384fb8550054ea2195a67a)#define RA\_ELC\_PERIPHERAL\_GPT\_G 6

[ 322](ra6m5-elc_8h.md#a6e737df13755e4e0039e98610aa31f3c)#define RA\_ELC\_PERIPHERAL\_GPT\_H 7

[ 323](ra6m5-elc_8h.md#a2b5a9232a4ad9d199dc9baa510d0ed54)#define RA\_ELC\_PERIPHERAL\_ADC0 8

[ 324](ra6m5-elc_8h.md#afaf4059726139d62e2c09010cfa1148a)#define RA\_ELC\_PERIPHERAL\_ADC0\_B 9

[ 325](ra6m5-elc_8h.md#aea69e6e72e14f53afeb85aa4a9349bcb)#define RA\_ELC\_PERIPHERAL\_ADC1 10

[ 326](ra6m5-elc_8h.md#adbd2118aea6d1ba6ca67de192f0033fc)#define RA\_ELC\_PERIPHERAL\_ADC1\_B 11

[ 327](ra6m5-elc_8h.md#a9a32ba5817467743fbcf24b698124b02)#define RA\_ELC\_PERIPHERAL\_DAC0 12

[ 328](ra6m5-elc_8h.md#a84aa20e3793499f427f6c9ccb7a20566)#define RA\_ELC\_PERIPHERAL\_DAC1 13

[ 329](ra6m5-elc_8h.md#a5830e830b7b10cd68441de2648edd6a0)#define RA\_ELC\_PERIPHERAL\_IOPORT1 14

[ 330](ra6m5-elc_8h.md#a42d4feb2c854cc1964455297e6d7eb72)#define RA\_ELC\_PERIPHERAL\_IOPORT2 15

[ 331](ra6m5-elc_8h.md#a349933f20d7b6f768e49239724d0c5f7)#define RA\_ELC\_PERIPHERAL\_IOPORT3 16

[ 332](ra6m5-elc_8h.md#a6d08d1db64f903fa2dacfc81568b004d)#define RA\_ELC\_PERIPHERAL\_IOPORT4 17

[ 333](ra6m5-elc_8h.md#a66a60a7a3469054498a247253cea97c0)#define RA\_ELC\_PERIPHERAL\_CTSU 18

334

335#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA6M5\_ELC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [misc](dir_b5927901ba0eeb0fdf9ca7870f5af60a.md)
- [renesas](dir_86b946318bd38151d049d676c19e4b11.md)
- [ra-elc](dir_fc824a581c07e3e227952b4fed9afa76.md)
- [ra6m5-elc.h](ra6m5-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
