---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra4e1-elc_8h_source.html
original_path: doxygen/html/ra4e1-elc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra4e1-elc.h

[Go to the documentation of this file.](ra4e1-elc_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA4E1\_ELC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA4E1\_ELC\_H\_

9

10/\* Sources of event signals to be linked to other peripherals or the CPU \*/

[ 11](ra4e1-elc_8h.md#a11b5cec97472328120a8d6381f1e8809)#define RA\_ELC\_EVENT\_NONE 0x0

[ 12](ra4e1-elc_8h.md#a04ee26d7188b7441627bb89249545cfa)#define RA\_ELC\_EVENT\_ICU\_IRQ0 0x001

[ 13](ra4e1-elc_8h.md#ac9f6681c03b50d8b3a24798b3e790170)#define RA\_ELC\_EVENT\_ICU\_IRQ1 0x002

[ 14](ra4e1-elc_8h.md#a136f93a17eea3f4233b0012c075fc904)#define RA\_ELC\_EVENT\_ICU\_IRQ2 0x003

[ 15](ra4e1-elc_8h.md#a65b92e543dfb43c213274652ae60314a)#define RA\_ELC\_EVENT\_ICU\_IRQ3 0x004

[ 16](ra4e1-elc_8h.md#a2b1930fc54010b7c4c00f286f690cb1e)#define RA\_ELC\_EVENT\_ICU\_IRQ4 0x005

[ 17](ra4e1-elc_8h.md#af3ecccfe646b6cac991310abe3e4b955)#define RA\_ELC\_EVENT\_ICU\_IRQ5 0x006

[ 18](ra4e1-elc_8h.md#a98b53eb7b5979403023805ba925c504c)#define RA\_ELC\_EVENT\_ICU\_IRQ6 0x007

[ 19](ra4e1-elc_8h.md#ab6f05849ddc30ceb693f57b522223bcf)#define RA\_ELC\_EVENT\_ICU\_IRQ7 0x008

[ 20](ra4e1-elc_8h.md#acbcd1c55530c6cb8580b76bd55c73c90)#define RA\_ELC\_EVENT\_ICU\_IRQ8 0x009

[ 21](ra4e1-elc_8h.md#af04ed29327af6c108875334c24d98e43)#define RA\_ELC\_EVENT\_ICU\_IRQ9 0x00A

[ 22](ra4e1-elc_8h.md#ad7435ed602899357eae0f46c09bf542c)#define RA\_ELC\_EVENT\_ICU\_IRQ13 0x00E

[ 23](ra4e1-elc_8h.md#a906929a9ae7dd7de44d21a32d3635080)#define RA\_ELC\_EVENT\_DMAC0\_INT 0x020

[ 24](ra4e1-elc_8h.md#a76b9d9fa8af16a1480fcc8d8ec12572f)#define RA\_ELC\_EVENT\_DMAC1\_INT 0x021

[ 25](ra4e1-elc_8h.md#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)#define RA\_ELC\_EVENT\_DMAC2\_INT 0x022

[ 26](ra4e1-elc_8h.md#a0b9d72a41fd7c5b27e6c31967645b907)#define RA\_ELC\_EVENT\_DMAC3\_INT 0x023

[ 27](ra4e1-elc_8h.md#a4cae5afbbe49719555bbbfa12b8727f5)#define RA\_ELC\_EVENT\_DMAC4\_INT 0x024

[ 28](ra4e1-elc_8h.md#a000e31aba8a821f4358a435d280b3a7b)#define RA\_ELC\_EVENT\_DMAC5\_INT 0x025

[ 29](ra4e1-elc_8h.md#a2d1f6d1c797a0d787a5d5c08b0fc18ad)#define RA\_ELC\_EVENT\_DMAC6\_INT 0x026

[ 30](ra4e1-elc_8h.md#ae8caef45a510d4c4f1c55f923e01799e)#define RA\_ELC\_EVENT\_DMAC7\_INT 0x027

[ 31](ra4e1-elc_8h.md#a9a58e3a2c10447906aaf35bab5664d24)#define RA\_ELC\_EVENT\_DTC\_COMPLETE 0x029

[ 32](ra4e1-elc_8h.md#a5ab484cdaf470b47e95005d83d60394f)#define RA\_ELC\_EVENT\_DTC\_END 0x02A

[ 33](ra4e1-elc_8h.md#a54d8c74eefe8f9b237ea23e18033d947)#define RA\_ELC\_EVENT\_DMA\_TRANSERR 0x02B

[ 34](ra4e1-elc_8h.md#a26e0aaa4a17196ada130bbb714a6d3bd)#define RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL 0x02D

[ 35](ra4e1-elc_8h.md#a5c7545a2f69856b7b637ad690f158b77)#define RA\_ELC\_EVENT\_FCU\_FIFERR 0x030

[ 36](ra4e1-elc_8h.md#a535af54c8bcfff47cc90ba1226044d71)#define RA\_ELC\_EVENT\_FCU\_FRDYI 0x031

[ 37](ra4e1-elc_8h.md#a7ab275777147d06315a04abb3f2f6d51)#define RA\_ELC\_EVENT\_LVD\_LVD1 0x038

[ 38](ra4e1-elc_8h.md#ad52acadba107b7f907d678f44769a4cb)#define RA\_ELC\_EVENT\_LVD\_LVD2 0x039

[ 39](ra4e1-elc_8h.md#a290decf4254396cbce267cb52a619717)#define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP 0x03B

[ 40](ra4e1-elc_8h.md#ac6953f0c8caa6b5ef8c9893c7ff4baa1)#define RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST 0x03C

[ 41](ra4e1-elc_8h.md#a4c3604a42ead1d43f472e901087ec148)#define RA\_ELC\_EVENT\_AGT0\_INT 0x040

[ 42](ra4e1-elc_8h.md#a015e6f8aed4b467f4554e6887b4d9ec9)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A 0x041

[ 43](ra4e1-elc_8h.md#ada1ad302dc5b987a6f7c972afae729f2)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B 0x042

[ 44](ra4e1-elc_8h.md#a635180e38c932579072f4eebd665592f)#define RA\_ELC\_EVENT\_AGT1\_INT 0x043

[ 45](ra4e1-elc_8h.md#aeb2399818b6b141ab4a37e257dba22be)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A 0x044

[ 46](ra4e1-elc_8h.md#a1d660c78348b48ea7a072225491ae44b)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B 0x045

[ 47](ra4e1-elc_8h.md#aace60e1ca05855c0838298c51510943d)#define RA\_ELC\_EVENT\_AGT2\_INT 0x046

[ 48](ra4e1-elc_8h.md#ac7d2ceb7c70898f96e4ef1606b96191f)#define RA\_ELC\_EVENT\_AGT2\_COMPARE\_A 0x047

[ 49](ra4e1-elc_8h.md#afa53449537c7ad67c71f495848781b9d)#define RA\_ELC\_EVENT\_AGT2\_COMPARE\_B 0x048

[ 50](ra4e1-elc_8h.md#a4a1e74d4c1ab5f1b6039550e3b518089)#define RA\_ELC\_EVENT\_AGT3\_INT 0x049

[ 51](ra4e1-elc_8h.md#a4500621826d716e3050e8e5e88d68a16)#define RA\_ELC\_EVENT\_AGT3\_COMPARE\_A 0x04A

[ 52](ra4e1-elc_8h.md#a93641e55a6c8db7ae55e3b83376d997d)#define RA\_ELC\_EVENT\_AGT3\_COMPARE\_B 0x04B

[ 53](ra4e1-elc_8h.md#acbb0c43bed869c27a8a90e8cb8166bb4)#define RA\_ELC\_EVENT\_AGT5\_INT 0x04F

[ 54](ra4e1-elc_8h.md#a7ab1f11da949fca8067e82cd437b142a)#define RA\_ELC\_EVENT\_AGT5\_COMPARE\_A 0x050

[ 55](ra4e1-elc_8h.md#a78b5abeca0f03176a19464f3c2d9508d)#define RA\_ELC\_EVENT\_AGT5\_COMPARE\_B 0x051

[ 56](ra4e1-elc_8h.md#abc837f1fcfffeb2ec231c79336379dda)#define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW 0x052

[ 57](ra4e1-elc_8h.md#a6cdb7a60a850f9ec23f19c548a6cc544)#define RA\_ELC\_EVENT\_WDT\_UNDERFLOW 0x053

[ 58](ra4e1-elc_8h.md#a76fd68b555574159d563d2dfd68d90b9)#define RA\_ELC\_EVENT\_RTC\_ALARM 0x054

[ 59](ra4e1-elc_8h.md#a144901ee7b31b96eba18a39d98c4b953)#define RA\_ELC\_EVENT\_RTC\_PERIOD 0x055

[ 60](ra4e1-elc_8h.md#a241cd3c65033b46a1160d5815cc86fd7)#define RA\_ELC\_EVENT\_RTC\_CARRY 0x056

[ 61](ra4e1-elc_8h.md#ae4dbb89c58220f72818cc9c28d97905b)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_0 0x06B

[ 62](ra4e1-elc_8h.md#a0ef2efa2ea339cad7598f11fe549cdd9)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_1 0x06C

[ 63](ra4e1-elc_8h.md#aac8d97813e8a3276bdac764faf7b580d)#define RA\_ELC\_EVENT\_USBFS\_INT 0x06D

[ 64](ra4e1-elc_8h.md#a9458dbf2b1da6fc51ca2c2933dcb6b37)#define RA\_ELC\_EVENT\_USBFS\_RESUME 0x06E

[ 65](ra4e1-elc_8h.md#a7271a25cdc3c987313efbafcd2a746cf)#define RA\_ELC\_EVENT\_IIC0\_RXI 0x073

[ 66](ra4e1-elc_8h.md#a7843f8a23feb383202fa6ad3be8fae5c)#define RA\_ELC\_EVENT\_IIC0\_TXI 0x074

[ 67](ra4e1-elc_8h.md#a52270344b26073c127a0269c5ec4e228)#define RA\_ELC\_EVENT\_IIC0\_TEI 0x075

[ 68](ra4e1-elc_8h.md#a667eb763b55f973b141837e82dbbae6e)#define RA\_ELC\_EVENT\_IIC0\_ERI 0x076

[ 69](ra4e1-elc_8h.md#a2a074dab614a1639ea5fa4f6d3baffd3)#define RA\_ELC\_EVENT\_IIC0\_WUI 0x077

[ 70](ra4e1-elc_8h.md#a6ec3edb5e4de5bca1171ade1aa9ca19f)#define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR 0x09E

[ 71](ra4e1-elc_8h.md#a1390ee9467a9d093de1532f0703ec35f)#define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END 0x09F

[ 72](ra4e1-elc_8h.md#a3463c1e202ab7891521eda7196e1be80)#define RA\_ELC\_EVENT\_CAC\_OVERFLOW 0x0A0

[ 73](ra4e1-elc_8h.md#aa4f3b915e26ee83dcc8c383a1fdb2425)#define RA\_ELC\_EVENT\_CAN0\_ERROR 0x0A1

[ 74](ra4e1-elc_8h.md#ad6e2ac69f8d10baa2d023e680e2f4c2f)#define RA\_ELC\_EVENT\_CAN0\_FIFO\_RX 0x0A2

[ 75](ra4e1-elc_8h.md#a52d0f15f6d388658ae060aec6302b448)#define RA\_ELC\_EVENT\_CAN0\_FIFO\_TX 0x0A3

[ 76](ra4e1-elc_8h.md#a0b017dad5f8642aa70f6f96c45e84a72)#define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX 0x0A4

[ 77](ra4e1-elc_8h.md#a71880c5fc6363d67d8d126fd63a5354c)#define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX 0x0A5

[ 78](ra4e1-elc_8h.md#aee58e9a0c4313f0ec08f0652e5002008)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1 0x0B1

[ 79](ra4e1-elc_8h.md#a36d858520d28847eead0fbfe7950be2d)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2 0x0B2

[ 80](ra4e1-elc_8h.md#a545dadce70bbcea1116cd13490fe2571)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_3 0x0B3

[ 81](ra4e1-elc_8h.md#a4e478b84ef99ae71c102ad3d5c71089a)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_4 0x0B4

[ 82](ra4e1-elc_8h.md#ae5c28618f4e68eef6ca83bdcec515abb)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0 0x0B5

[ 83](ra4e1-elc_8h.md#a9f0b82bfff5ea2ba414ac0bccad9a34d)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1 0x0B6

[ 84](ra4e1-elc_8h.md#a81e18423a1f61e34f0daab6f7367eae2)#define RA\_ELC\_EVENT\_POEG0\_EVENT 0x0B7

[ 85](ra4e1-elc_8h.md#a2a43c2ce461fde766e66a4451929a875)#define RA\_ELC\_EVENT\_POEG1\_EVENT 0x0B8

[ 86](ra4e1-elc_8h.md#a7b5c16202b2491ba77319a180bcaa107)#define RA\_ELC\_EVENT\_POEG2\_EVENT 0x0B9

[ 87](ra4e1-elc_8h.md#ab39d06b130b93348c5fab589f1e0074e)#define RA\_ELC\_EVENT\_POEG3\_EVENT 0x0BA

[ 88](ra4e1-elc_8h.md#a33a428565bfa3237aa4eda10b982fc65)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A 0x0C9

[ 89](ra4e1-elc_8h.md#a5326aaf270290b524f8cb2e126d06602)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B 0x0CA

[ 90](ra4e1-elc_8h.md#a2e55bae34ab30f2d802b8eaf93dd3cfd)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C 0x0CB

[ 91](ra4e1-elc_8h.md#ada3870f40beeec10e9366e908ed980d0)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D 0x0CC

[ 92](ra4e1-elc_8h.md#a5d4f72e95b7bb76315b9ffa059730620)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E 0x0CD

[ 93](ra4e1-elc_8h.md#a548923b7385648e4f15fef4ecb315478)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F 0x0CE

[ 94](ra4e1-elc_8h.md#aa6eac7cf283073eea62fbaa1df2017f2)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW 0x0CF

[ 95](ra4e1-elc_8h.md#ae8cefd5f23897d43cffba4e91b7c8b5c)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW 0x0D0

[ 96](ra4e1-elc_8h.md#aa0208084abba3e2601c8cf7bb42837fd)#define RA\_ELC\_EVENT\_GPT1\_PC 0x0D1

[ 97](ra4e1-elc_8h.md#ad1a5796e0c70a988165765f2ce8c1e80)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A 0x0D2

[ 98](ra4e1-elc_8h.md#a73776ba7d66a478c92c6cb3dfed50af4)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B 0x0D3

[ 99](ra4e1-elc_8h.md#aa391fa888ded57351c9b62f54df1ce36)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C 0x0D4

[ 100](ra4e1-elc_8h.md#a90c7aa7bbddb04e6ae4b6eccb64a0e93)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D 0x0D5

[ 101](ra4e1-elc_8h.md#adbfb562e616a86a3e28f8c3f09553db9)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E 0x0D6

[ 102](ra4e1-elc_8h.md#a6f07945c82efae23754e34dc09bee884)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F 0x0D7

[ 103](ra4e1-elc_8h.md#aede7879166ef812139641122782d873b)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW 0x0D8

[ 104](ra4e1-elc_8h.md#ad71d20ad5434f219a61e0f0aded090d1)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW 0x0D9

[ 105](ra4e1-elc_8h.md#a8130aa176d9d5dd698c62708111515e0)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A 0x0E4

[ 106](ra4e1-elc_8h.md#aa77a30a219070d15e358a43fbbd89728)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B 0x0E5

[ 107](ra4e1-elc_8h.md#af6c1cb172b343baa8d8bbe01d1674922)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C 0x0E6

[ 108](ra4e1-elc_8h.md#ae8c7945c641045c615922a3f82329c56)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D 0x0E7

[ 109](ra4e1-elc_8h.md#afcb271a94d9b07b7b1a204f325b80d52)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E 0x0E8

[ 110](ra4e1-elc_8h.md#a906eb0e1ed2786ed2b14e4608489b2cc)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F 0x0E9

[ 111](ra4e1-elc_8h.md#abb820eb80ad8afc5c12dc3581fc7a0b9)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW 0x0EA

[ 112](ra4e1-elc_8h.md#a65831ae6b037607dc55a2b1e8aa296a7)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW 0x0EB

[ 113](ra4e1-elc_8h.md#af3ae1988661f1d68bd7cd5e36fb387f6)#define RA\_ELC\_EVENT\_GPT4\_PC 0x0EC

[ 114](ra4e1-elc_8h.md#adc4aceff99f296b06938254f9dcc1f2f)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A 0x0ED

[ 115](ra4e1-elc_8h.md#aad1fc8b32dffaaa64f9908951f8b1c64)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B 0x0EE

[ 116](ra4e1-elc_8h.md#aebaa50f4643efe5b87798777cee578bc)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C 0x0EF

[ 117](ra4e1-elc_8h.md#a21965e21bd4045aa5010925620b4d827)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D 0x0F0

[ 118](ra4e1-elc_8h.md#a51a7cb146f0efbb7bc9f7336031006a4)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E 0x0F1

[ 119](ra4e1-elc_8h.md#abbd0bd21af2bd1679d6d7bc36001b97d)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F 0x0F2

[ 120](ra4e1-elc_8h.md#a038e7580f03fbdd74f417108cd2a8b4d)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW 0x0F3

[ 121](ra4e1-elc_8h.md#ac38b8f1154d6a699923b2bbf249e38fd)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW 0x0F4

[ 122](ra4e1-elc_8h.md#aa7e87dac91e6416a1b1a23ae5ee82b55)#define RA\_ELC\_EVENT\_GPT5\_PC 0x0F5

[ 123](ra4e1-elc_8h.md#ad7284976213551f7d4fa450bf2bf8c7c)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END 0x160

[ 124](ra4e1-elc_8h.md#aecbe4efa29972b832e35ebb00d7499ad)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B 0x161

[ 125](ra4e1-elc_8h.md#aa4feb2c3e29ba84d1397c618b7b860bf)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A 0x162

[ 126](ra4e1-elc_8h.md#ab59c8ec4f20de5cf4709efe0a7ee70a1)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B 0x163

[ 127](ra4e1-elc_8h.md#af187c78a1f05fc4be81aa3af36e4cde5)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH 0x164

[ 128](ra4e1-elc_8h.md#a65d6c499a6852434b4802f8ef7066eb4)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH 0x165

[ 129](ra4e1-elc_8h.md#ad9e9a8451a683c5b5bc8a2ace8264c27)#define RA\_ELC\_EVENT\_SCI0\_RXI 0x180

[ 130](ra4e1-elc_8h.md#aecc4fdda2a7eeb2bab0b894f2e5047d9)#define RA\_ELC\_EVENT\_SCI0\_TXI 0x181

[ 131](ra4e1-elc_8h.md#ae845a850ab730c651badc5c857e28ee9)#define RA\_ELC\_EVENT\_SCI0\_TEI 0x182

[ 132](ra4e1-elc_8h.md#ad4580e769bae423298276e31ee2ee071)#define RA\_ELC\_EVENT\_SCI0\_ERI 0x183

[ 133](ra4e1-elc_8h.md#ae2373b571584dae4d1c7fc57142ecb3c)#define RA\_ELC\_EVENT\_SCI0\_AM 0x184

[ 134](ra4e1-elc_8h.md#ad52a4c7660a4e609976f7045305f8ca7)#define RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI 0x185

[ 135](ra4e1-elc_8h.md#a87a1f07a2b420f9ce8d7ebcc1c505986)#define RA\_ELC\_EVENT\_SCI3\_RXI 0x192

[ 136](ra4e1-elc_8h.md#aee0548d7714ebd04748eadf9e9dbb97c)#define RA\_ELC\_EVENT\_SCI3\_TXI 0x193

[ 137](ra4e1-elc_8h.md#a6f9d20424191f026030159511647f913)#define RA\_ELC\_EVENT\_SCI3\_TEI 0x194

[ 138](ra4e1-elc_8h.md#ab7a6ad3ccc6279863a491a3787fd5c5e)#define RA\_ELC\_EVENT\_SCI3\_ERI 0x195

[ 139](ra4e1-elc_8h.md#a075f80d14abaa63627574519b9ebf36b)#define RA\_ELC\_EVENT\_SCI3\_AM 0x196

[ 140](ra4e1-elc_8h.md#afe86466482eb03b85da9feb17bdccfc0)#define RA\_ELC\_EVENT\_SCI4\_RXI 0x198

[ 141](ra4e1-elc_8h.md#a89f26e1bfd92cb7c9a2bad9acd80e553)#define RA\_ELC\_EVENT\_SCI4\_TXI 0x199

[ 142](ra4e1-elc_8h.md#a2554192500a5ac058fbd338d3018f6cc)#define RA\_ELC\_EVENT\_SCI4\_TEI 0x19A

[ 143](ra4e1-elc_8h.md#ac6f2b3938cde7ba80faf523548dfa6c2)#define RA\_ELC\_EVENT\_SCI4\_ERI 0x19B

[ 144](ra4e1-elc_8h.md#abddf2cbec24fd59c9330b0328a21f82e)#define RA\_ELC\_EVENT\_SCI4\_AM 0x19C

[ 145](ra4e1-elc_8h.md#ac01e51a9360f409e430642d86818bf98)#define RA\_ELC\_EVENT\_SCI9\_RXI 0x1B6

[ 146](ra4e1-elc_8h.md#a8c628c59b08ed53781fd406ea22da796)#define RA\_ELC\_EVENT\_SCI9\_TXI 0x1B7

[ 147](ra4e1-elc_8h.md#ac3a064375ff90f3a6a35c5fdda680f95)#define RA\_ELC\_EVENT\_SCI9\_TEI 0x1B8

[ 148](ra4e1-elc_8h.md#af2e4d2d6b59c512e536d901789b3c1a2)#define RA\_ELC\_EVENT\_SCI9\_ERI 0x1B9

[ 149](ra4e1-elc_8h.md#a2bfc7def09c933262aa530227a45af7d)#define RA\_ELC\_EVENT\_SCI9\_AM 0x1BA

[ 150](ra4e1-elc_8h.md#af77608914a79bea7797b63674c71db31)#define RA\_ELC\_EVENT\_SPI0\_RXI 0x1C4

[ 151](ra4e1-elc_8h.md#a82d87016b5d694884bba33bf71e93e92)#define RA\_ELC\_EVENT\_SPI0\_TXI 0x1C5

[ 152](ra4e1-elc_8h.md#a920575ee3a202b0d7202cd053f1e235b)#define RA\_ELC\_EVENT\_SPI0\_IDLE 0x1C6

[ 153](ra4e1-elc_8h.md#ab588fafc974153bcf94087cdb1a71d73)#define RA\_ELC\_EVENT\_SPI0\_ERI 0x1C7

[ 154](ra4e1-elc_8h.md#a368a0ece3d89efe3ed8ab274471849b9)#define RA\_ELC\_EVENT\_SPI0\_TEI 0x1C8

[ 155](ra4e1-elc_8h.md#a344b216f0d5880b31e7c1a4e700c85a4)#define RA\_ELC\_EVENT\_QSPI\_INT 0x1DA

[ 156](ra4e1-elc_8h.md#ab6c210d6481294137fd4bc32c39e5de1)#define RA\_ELC\_EVENT\_DOC\_INT 0x1DB

157

158/\* Possible peripherals to be linked to event signals \*/

[ 159](ra4e1-elc_8h.md#ad6bb2d32abfad10bd283894efb7fe968)#define RA\_ELC\_PERIPHERAL\_GPT\_A 0

[ 160](ra4e1-elc_8h.md#a8c4b99abfaa798b3b15f3435a73bad86)#define RA\_ELC\_PERIPHERAL\_GPT\_B 1

[ 161](ra4e1-elc_8h.md#af0000625eec82c9f4ebe20da1cec7c66)#define RA\_ELC\_PERIPHERAL\_GPT\_C 2

[ 162](ra4e1-elc_8h.md#ae9ae748233cce2fa65b334c2f8b2a6f7)#define RA\_ELC\_PERIPHERAL\_GPT\_D 3

[ 163](ra4e1-elc_8h.md#aefc3deade612ed7aa53abd397d20af3b)#define RA\_ELC\_PERIPHERAL\_GPT\_E 4

[ 164](ra4e1-elc_8h.md#a4bb2ffb785a17a225d5eb6e80f0040bf)#define RA\_ELC\_PERIPHERAL\_GPT\_F 5

[ 165](ra4e1-elc_8h.md#a2ccd7f6730384fb8550054ea2195a67a)#define RA\_ELC\_PERIPHERAL\_GPT\_G 6

[ 166](ra4e1-elc_8h.md#a6e737df13755e4e0039e98610aa31f3c)#define RA\_ELC\_PERIPHERAL\_GPT\_H 7

[ 167](ra4e1-elc_8h.md#a2b5a9232a4ad9d199dc9baa510d0ed54)#define RA\_ELC\_PERIPHERAL\_ADC0 8

[ 168](ra4e1-elc_8h.md#afaf4059726139d62e2c09010cfa1148a)#define RA\_ELC\_PERIPHERAL\_ADC0\_B 9

[ 169](ra4e1-elc_8h.md#a9a32ba5817467743fbcf24b698124b02)#define RA\_ELC\_PERIPHERAL\_DAC0 12

[ 170](ra4e1-elc_8h.md#a5830e830b7b10cd68441de2648edd6a0)#define RA\_ELC\_PERIPHERAL\_IOPORT1 14

[ 171](ra4e1-elc_8h.md#a42d4feb2c854cc1964455297e6d7eb72)#define RA\_ELC\_PERIPHERAL\_IOPORT2 15

[ 172](ra4e1-elc_8h.md#a349933f20d7b6f768e49239724d0c5f7)#define RA\_ELC\_PERIPHERAL\_IOPORT3 16

[ 173](ra4e1-elc_8h.md#a6d08d1db64f903fa2dacfc81568b004d)#define RA\_ELC\_PERIPHERAL\_IOPORT4 17

174

175#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA4E1\_ELC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [misc](dir_b5927901ba0eeb0fdf9ca7870f5af60a.md)
- [renesas](dir_86b946318bd38151d049d676c19e4b11.md)
- [ra-elc](dir_fc824a581c07e3e227952b4fed9afa76.md)
- [ra4e1-elc.h](ra4e1-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
