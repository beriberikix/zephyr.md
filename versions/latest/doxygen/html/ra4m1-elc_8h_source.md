---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra4m1-elc_8h_source.html
original_path: doxygen/html/ra4m1-elc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra4m1-elc.h

[Go to the documentation of this file.](ra4m1-elc_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA4M1\_ELC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA4M1\_ELC\_H\_

9

10/\* Sources of event signals to be linked to other peripherals or the CPU \*/

[ 11](ra4m1-elc_8h.md#a11b5cec97472328120a8d6381f1e8809)#define RA\_ELC\_EVENT\_NONE 0x0

[ 12](ra4m1-elc_8h.md#a04ee26d7188b7441627bb89249545cfa)#define RA\_ELC\_EVENT\_ICU\_IRQ0 0x001

[ 13](ra4m1-elc_8h.md#ac9f6681c03b50d8b3a24798b3e790170)#define RA\_ELC\_EVENT\_ICU\_IRQ1 0x002

[ 14](ra4m1-elc_8h.md#a136f93a17eea3f4233b0012c075fc904)#define RA\_ELC\_EVENT\_ICU\_IRQ2 0x003

[ 15](ra4m1-elc_8h.md#a65b92e543dfb43c213274652ae60314a)#define RA\_ELC\_EVENT\_ICU\_IRQ3 0x004

[ 16](ra4m1-elc_8h.md#a2b1930fc54010b7c4c00f286f690cb1e)#define RA\_ELC\_EVENT\_ICU\_IRQ4 0x005

[ 17](ra4m1-elc_8h.md#af3ecccfe646b6cac991310abe3e4b955)#define RA\_ELC\_EVENT\_ICU\_IRQ5 0x006

[ 18](ra4m1-elc_8h.md#a98b53eb7b5979403023805ba925c504c)#define RA\_ELC\_EVENT\_ICU\_IRQ6 0x007

[ 19](ra4m1-elc_8h.md#ab6f05849ddc30ceb693f57b522223bcf)#define RA\_ELC\_EVENT\_ICU\_IRQ7 0x008

[ 20](ra4m1-elc_8h.md#acbcd1c55530c6cb8580b76bd55c73c90)#define RA\_ELC\_EVENT\_ICU\_IRQ8 0x009

[ 21](ra4m1-elc_8h.md#af04ed29327af6c108875334c24d98e43)#define RA\_ELC\_EVENT\_ICU\_IRQ9 0x00A

[ 22](ra4m1-elc_8h.md#a3e9a895c4855c3db6ac7fc5900b57807)#define RA\_ELC\_EVENT\_ICU\_IRQ10 0x00B

[ 23](ra4m1-elc_8h.md#a46f43f1dd26e006c26b11bd45e53a728)#define RA\_ELC\_EVENT\_ICU\_IRQ11 0x00C

[ 24](ra4m1-elc_8h.md#affb7ae86a41c8cc8582e6c6ef284a5d8)#define RA\_ELC\_EVENT\_ICU\_IRQ12 0x00D

[ 25](ra4m1-elc_8h.md#ada7702d0ac50f9b3e82ef50d6be50470)#define RA\_ELC\_EVENT\_ICU\_IRQ14 0x00F

[ 26](ra4m1-elc_8h.md#afab294cf0d58a5bb4dd578774b0ad9aa)#define RA\_ELC\_EVENT\_ICU\_IRQ15 0x010

[ 27](ra4m1-elc_8h.md#a906929a9ae7dd7de44d21a32d3635080)#define RA\_ELC\_EVENT\_DMAC0\_INT 0x011

[ 28](ra4m1-elc_8h.md#a76b9d9fa8af16a1480fcc8d8ec12572f)#define RA\_ELC\_EVENT\_DMAC1\_INT 0x012

[ 29](ra4m1-elc_8h.md#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)#define RA\_ELC\_EVENT\_DMAC2\_INT 0x013

[ 30](ra4m1-elc_8h.md#a0b9d72a41fd7c5b27e6c31967645b907)#define RA\_ELC\_EVENT\_DMAC3\_INT 0x014

[ 31](ra4m1-elc_8h.md#a9a58e3a2c10447906aaf35bab5664d24)#define RA\_ELC\_EVENT\_DTC\_COMPLETE 0x015

[ 32](ra4m1-elc_8h.md#a5ab484cdaf470b47e95005d83d60394f)#define RA\_ELC\_EVENT\_DTC\_END 0x016

[ 33](ra4m1-elc_8h.md#a26e0aaa4a17196ada130bbb714a6d3bd)#define RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL 0x017

[ 34](ra4m1-elc_8h.md#a535af54c8bcfff47cc90ba1226044d71)#define RA\_ELC\_EVENT\_FCU\_FRDYI 0x018

[ 35](ra4m1-elc_8h.md#a7ab275777147d06315a04abb3f2f6d51)#define RA\_ELC\_EVENT\_LVD\_LVD1 0x019

[ 36](ra4m1-elc_8h.md#ad52acadba107b7f907d678f44769a4cb)#define RA\_ELC\_EVENT\_LVD\_LVD2 0x01A

[ 37](ra4m1-elc_8h.md#a1ab4e1434620d962450d98c0fee2f89c)#define RA\_ELC\_EVENT\_LVD\_VBATT 0x01B

[ 38](ra4m1-elc_8h.md#a290decf4254396cbce267cb52a619717)#define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP 0x01C

[ 39](ra4m1-elc_8h.md#ac6953f0c8caa6b5ef8c9893c7ff4baa1)#define RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST 0x01D

[ 40](ra4m1-elc_8h.md#a4c3604a42ead1d43f472e901087ec148)#define RA\_ELC\_EVENT\_AGT0\_INT 0x01E

[ 41](ra4m1-elc_8h.md#a015e6f8aed4b467f4554e6887b4d9ec9)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A 0x01F

[ 42](ra4m1-elc_8h.md#ada1ad302dc5b987a6f7c972afae729f2)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B 0x020

[ 43](ra4m1-elc_8h.md#a635180e38c932579072f4eebd665592f)#define RA\_ELC\_EVENT\_AGT1\_INT 0x021

[ 44](ra4m1-elc_8h.md#aeb2399818b6b141ab4a37e257dba22be)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A 0x022

[ 45](ra4m1-elc_8h.md#a1d660c78348b48ea7a072225491ae44b)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B 0x023

[ 46](ra4m1-elc_8h.md#abc837f1fcfffeb2ec231c79336379dda)#define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW 0x024

[ 47](ra4m1-elc_8h.md#a6cdb7a60a850f9ec23f19c548a6cc544)#define RA\_ELC\_EVENT\_WDT\_UNDERFLOW 0x025

[ 48](ra4m1-elc_8h.md#a76fd68b555574159d563d2dfd68d90b9)#define RA\_ELC\_EVENT\_RTC\_ALARM 0x026

[ 49](ra4m1-elc_8h.md#a144901ee7b31b96eba18a39d98c4b953)#define RA\_ELC\_EVENT\_RTC\_PERIOD 0x027

[ 50](ra4m1-elc_8h.md#a241cd3c65033b46a1160d5815cc86fd7)#define RA\_ELC\_EVENT\_RTC\_CARRY 0x028

[ 51](ra4m1-elc_8h.md#ad7284976213551f7d4fa450bf2bf8c7c)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END 0x029

[ 52](ra4m1-elc_8h.md#aecbe4efa29972b832e35ebb00d7499ad)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B 0x02A

[ 53](ra4m1-elc_8h.md#aa4feb2c3e29ba84d1397c618b7b860bf)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A 0x02B

[ 54](ra4m1-elc_8h.md#ab59c8ec4f20de5cf4709efe0a7ee70a1)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B 0x02C

[ 55](ra4m1-elc_8h.md#af187c78a1f05fc4be81aa3af36e4cde5)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH 0x02D

[ 56](ra4m1-elc_8h.md#a65d6c499a6852434b4802f8ef7066eb4)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH 0x02E

[ 57](ra4m1-elc_8h.md#a46ba8b903950b3ff8b04c8176e7844b5)#define RA\_ELC\_EVENT\_ACMPLP0\_INT 0x02F

[ 58](ra4m1-elc_8h.md#a377a3e92bcdf0e45d2b12223ddd85666)#define RA\_ELC\_EVENT\_ACMPLP1\_INT 0x030

[ 59](ra4m1-elc_8h.md#ae4dbb89c58220f72818cc9c28d97905b)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_0 0x031

[ 60](ra4m1-elc_8h.md#a0ef2efa2ea339cad7598f11fe549cdd9)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_1 0x032

[ 61](ra4m1-elc_8h.md#aac8d97813e8a3276bdac764faf7b580d)#define RA\_ELC\_EVENT\_USBFS\_INT 0x033

[ 62](ra4m1-elc_8h.md#a9458dbf2b1da6fc51ca2c2933dcb6b37)#define RA\_ELC\_EVENT\_USBFS\_RESUME 0x034

[ 63](ra4m1-elc_8h.md#a7271a25cdc3c987313efbafcd2a746cf)#define RA\_ELC\_EVENT\_IIC0\_RXI 0x035

[ 64](ra4m1-elc_8h.md#a7843f8a23feb383202fa6ad3be8fae5c)#define RA\_ELC\_EVENT\_IIC0\_TXI 0x036

[ 65](ra4m1-elc_8h.md#a52270344b26073c127a0269c5ec4e228)#define RA\_ELC\_EVENT\_IIC0\_TEI 0x037

[ 66](ra4m1-elc_8h.md#a667eb763b55f973b141837e82dbbae6e)#define RA\_ELC\_EVENT\_IIC0\_ERI 0x038

[ 67](ra4m1-elc_8h.md#a2a074dab614a1639ea5fa4f6d3baffd3)#define RA\_ELC\_EVENT\_IIC0\_WUI 0x039

[ 68](ra4m1-elc_8h.md#ad03e6b81d0e7ce53737e5c3022f8d951)#define RA\_ELC\_EVENT\_IIC1\_RXI 0x03A

[ 69](ra4m1-elc_8h.md#a641c91157c98f41d3cf5ff6bbe25192d)#define RA\_ELC\_EVENT\_IIC1\_TXI 0x03B

[ 70](ra4m1-elc_8h.md#a45ed226ccaace8813aa653276a52999d)#define RA\_ELC\_EVENT\_IIC1\_TEI 0x03C

[ 71](ra4m1-elc_8h.md#a2221a129f0e323fa5b96bfe5ed0e007f)#define RA\_ELC\_EVENT\_IIC1\_ERI 0x03D

[ 72](ra4m1-elc_8h.md#ac65193048ce5734b46bc2bf77b84cb4e)#define RA\_ELC\_EVENT\_SSI0\_TXI 0x03E

[ 73](ra4m1-elc_8h.md#ab736656ae0b06de8383189075cbb2f27)#define RA\_ELC\_EVENT\_SSI0\_RXI 0x03F

[ 74](ra4m1-elc_8h.md#a1a89e9ab6abb3834992ee3ea3ebaf9c4)#define RA\_ELC\_EVENT\_SSI0\_INT 0x041

[ 75](ra4m1-elc_8h.md#a2faf033bad7b355f8beb9386a2d0e93b)#define RA\_ELC\_EVENT\_CTSU\_WRITE 0x042

[ 76](ra4m1-elc_8h.md#ad7cd21f5db3e117b87ffab8a6cb47272)#define RA\_ELC\_EVENT\_CTSU\_READ 0x043

[ 77](ra4m1-elc_8h.md#acfe8138822bcd3f02fe50316e40c7641)#define RA\_ELC\_EVENT\_CTSU\_END 0x044

[ 78](ra4m1-elc_8h.md#a4412a0ec84a10d14d131754c5f9eb509)#define RA\_ELC\_EVENT\_KEY\_INT 0x045

[ 79](ra4m1-elc_8h.md#ab6c210d6481294137fd4bc32c39e5de1)#define RA\_ELC\_EVENT\_DOC\_INT 0x046

[ 80](ra4m1-elc_8h.md#a6ec3edb5e4de5bca1171ade1aa9ca19f)#define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR 0x047

[ 81](ra4m1-elc_8h.md#a1390ee9467a9d093de1532f0703ec35f)#define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END 0x048

[ 82](ra4m1-elc_8h.md#a3463c1e202ab7891521eda7196e1be80)#define RA\_ELC\_EVENT\_CAC\_OVERFLOW 0x049

[ 83](ra4m1-elc_8h.md#aa4f3b915e26ee83dcc8c383a1fdb2425)#define RA\_ELC\_EVENT\_CAN0\_ERROR 0x04A

[ 84](ra4m1-elc_8h.md#ad6e2ac69f8d10baa2d023e680e2f4c2f)#define RA\_ELC\_EVENT\_CAN0\_FIFO\_RX 0x04B

[ 85](ra4m1-elc_8h.md#a52d0f15f6d388658ae060aec6302b448)#define RA\_ELC\_EVENT\_CAN0\_FIFO\_TX 0x04C

[ 86](ra4m1-elc_8h.md#a0b017dad5f8642aa70f6f96c45e84a72)#define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX 0x04D

[ 87](ra4m1-elc_8h.md#a71880c5fc6363d67d8d126fd63a5354c)#define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX 0x04E

[ 88](ra4m1-elc_8h.md#aee58e9a0c4313f0ec08f0652e5002008)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1 0x04F

[ 89](ra4m1-elc_8h.md#a36d858520d28847eead0fbfe7950be2d)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2 0x050

[ 90](ra4m1-elc_8h.md#a545dadce70bbcea1116cd13490fe2571)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_3 0x051

[ 91](ra4m1-elc_8h.md#a4e478b84ef99ae71c102ad3d5c71089a)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_4 0x052

[ 92](ra4m1-elc_8h.md#ae5c28618f4e68eef6ca83bdcec515abb)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0 0x053

[ 93](ra4m1-elc_8h.md#a9f0b82bfff5ea2ba414ac0bccad9a34d)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1 0x054

[ 94](ra4m1-elc_8h.md#a81e18423a1f61e34f0daab6f7367eae2)#define RA\_ELC\_EVENT\_POEG0\_EVENT 0x055

[ 95](ra4m1-elc_8h.md#a2a43c2ce461fde766e66a4451929a875)#define RA\_ELC\_EVENT\_POEG1\_EVENT 0x056

[ 96](ra4m1-elc_8h.md#aec8a8b590cc124ca12425f34b5a61020)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A 0x057

[ 97](ra4m1-elc_8h.md#ae1ed91479f405ac965da868e86bce533)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B 0x058

[ 98](ra4m1-elc_8h.md#a6d7c9090c21a8a0c497356050d649ec6)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_C 0x059

[ 99](ra4m1-elc_8h.md#af5b8ca097747bd987e81d8d81263aa81)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_D 0x05A

[ 100](ra4m1-elc_8h.md#a9ebec21375578c0e52d953773373bf1e)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_E 0x05B

[ 101](ra4m1-elc_8h.md#ad503a55a4548ff6ffd58e2b74d9eaf00)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_F 0x05C

[ 102](ra4m1-elc_8h.md#a76692948000993fde4d286f1a521a6d2)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW 0x05D

[ 103](ra4m1-elc_8h.md#a9edde37b8c0835978aa55d58d77c5ad5)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW 0x05E

[ 104](ra4m1-elc_8h.md#a33a428565bfa3237aa4eda10b982fc65)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A 0x05F

[ 105](ra4m1-elc_8h.md#a5326aaf270290b524f8cb2e126d06602)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B 0x060

[ 106](ra4m1-elc_8h.md#a2e55bae34ab30f2d802b8eaf93dd3cfd)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C 0x061

[ 107](ra4m1-elc_8h.md#ada3870f40beeec10e9366e908ed980d0)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D 0x062

[ 108](ra4m1-elc_8h.md#a5d4f72e95b7bb76315b9ffa059730620)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E 0x063

[ 109](ra4m1-elc_8h.md#a548923b7385648e4f15fef4ecb315478)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F 0x064

[ 110](ra4m1-elc_8h.md#aa6eac7cf283073eea62fbaa1df2017f2)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW 0x065

[ 111](ra4m1-elc_8h.md#ae8cefd5f23897d43cffba4e91b7c8b5c)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW 0x066

[ 112](ra4m1-elc_8h.md#ad1a5796e0c70a988165765f2ce8c1e80)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A 0x067

[ 113](ra4m1-elc_8h.md#a73776ba7d66a478c92c6cb3dfed50af4)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B 0x068

[ 114](ra4m1-elc_8h.md#aa391fa888ded57351c9b62f54df1ce36)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C 0x069

[ 115](ra4m1-elc_8h.md#a90c7aa7bbddb04e6ae4b6eccb64a0e93)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D 0x06A

[ 116](ra4m1-elc_8h.md#adbfb562e616a86a3e28f8c3f09553db9)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E 0x06B

[ 117](ra4m1-elc_8h.md#a6f07945c82efae23754e34dc09bee884)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F 0x06C

[ 118](ra4m1-elc_8h.md#aede7879166ef812139641122782d873b)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW 0x06D

[ 119](ra4m1-elc_8h.md#ad71d20ad5434f219a61e0f0aded090d1)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW 0x06E

[ 120](ra4m1-elc_8h.md#a74526500dfb573fe21fbca739b1698e1)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A 0x06F

[ 121](ra4m1-elc_8h.md#ac6cfac3496e4ab71c9bf84b43e06486a)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B 0x070

[ 122](ra4m1-elc_8h.md#a1af4840d468eb4c4e1672a34652ef583)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_C 0x071

[ 123](ra4m1-elc_8h.md#a263e6b02601dd37d6eedaab56a2e6fcd)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_D 0x072

[ 124](ra4m1-elc_8h.md#a9035e080d39d60ecc898a596b9902aa6)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_E 0x073

[ 125](ra4m1-elc_8h.md#a9cffb5aca60a4c7349789fc23fb197fb)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_F 0x074

[ 126](ra4m1-elc_8h.md#a546eff128c44a29f56fe90952cef475d)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW 0x075

[ 127](ra4m1-elc_8h.md#ab30a5683e48535abbf0c400a5a0d8946)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW 0x076

[ 128](ra4m1-elc_8h.md#a8130aa176d9d5dd698c62708111515e0)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A 0x077

[ 129](ra4m1-elc_8h.md#aa77a30a219070d15e358a43fbbd89728)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B 0x078

[ 130](ra4m1-elc_8h.md#af6c1cb172b343baa8d8bbe01d1674922)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C 0x079

[ 131](ra4m1-elc_8h.md#ae8c7945c641045c615922a3f82329c56)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D 0x07A

[ 132](ra4m1-elc_8h.md#afcb271a94d9b07b7b1a204f325b80d52)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E 0x07B

[ 133](ra4m1-elc_8h.md#a906eb0e1ed2786ed2b14e4608489b2cc)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F 0x07C

[ 134](ra4m1-elc_8h.md#abb820eb80ad8afc5c12dc3581fc7a0b9)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW 0x07D

[ 135](ra4m1-elc_8h.md#a65831ae6b037607dc55a2b1e8aa296a7)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW 0x07E

[ 136](ra4m1-elc_8h.md#adc4aceff99f296b06938254f9dcc1f2f)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A 0x07F

[ 137](ra4m1-elc_8h.md#aad1fc8b32dffaaa64f9908951f8b1c64)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B 0x080

[ 138](ra4m1-elc_8h.md#aebaa50f4643efe5b87798777cee578bc)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C 0x081

[ 139](ra4m1-elc_8h.md#a21965e21bd4045aa5010925620b4d827)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D 0x082

[ 140](ra4m1-elc_8h.md#a51a7cb146f0efbb7bc9f7336031006a4)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E 0x083

[ 141](ra4m1-elc_8h.md#abbd0bd21af2bd1679d6d7bc36001b97d)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F 0x084

[ 142](ra4m1-elc_8h.md#a038e7580f03fbdd74f417108cd2a8b4d)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW 0x085

[ 143](ra4m1-elc_8h.md#ac38b8f1154d6a699923b2bbf249e38fd)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW 0x086

[ 144](ra4m1-elc_8h.md#acad1c37929903ddee569f40a3c5c59e3)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A 0x087

[ 145](ra4m1-elc_8h.md#aa0fc9b447efbcba0bb6800f785daeb96)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B 0x088

[ 146](ra4m1-elc_8h.md#a01f586bd98832ea9b8aa58741b61a319)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_C 0x089

[ 147](ra4m1-elc_8h.md#acd71c3b8e8e1d96aa3ff6affb93f5000)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_D 0x08A

[ 148](ra4m1-elc_8h.md#a6abdcc7a6331a8283cfe0c1ac06b7d83)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_E 0x08B

[ 149](ra4m1-elc_8h.md#a28b6b55ad533e3cb606b2b0937c916b3)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_F 0x08C

[ 150](ra4m1-elc_8h.md#ac3c8dd6a5b7f95dccc58e7ec4e235a40)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW 0x08D

[ 151](ra4m1-elc_8h.md#acdece33585a75fccba962e4f764058fb)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW 0x08E

[ 152](ra4m1-elc_8h.md#afe1b39e5d37a5ed631dd18869cfbac8a)#define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A 0x08F

[ 153](ra4m1-elc_8h.md#a53b7cfc8d0a000bd57f159b09b0a9c26)#define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B 0x090

[ 154](ra4m1-elc_8h.md#add91262eba9ec860b788030af153161a)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_C 0x091

[ 155](ra4m1-elc_8h.md#a9310fd708ca6f0afcf374bfc96e22e6e)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_D 0x092

[ 156](ra4m1-elc_8h.md#a8d18bd54c972d1de01c2a9f86e832cd0)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_E 0x093

[ 157](ra4m1-elc_8h.md#aca89f90e8afa3f656e76f5960717543c)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_F 0x094

[ 158](ra4m1-elc_8h.md#aac0ed7abde81cf4bcc7588bf64b53c04)#define RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW 0x095

[ 159](ra4m1-elc_8h.md#ab1935670b6c0a5b5629ef8ba9d854f6c)#define RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW 0x096

[ 160](ra4m1-elc_8h.md#a8438d8d92e1950681388b40385a2c354)#define RA\_ELC\_EVENT\_OPS\_UVW\_EDGE 0x097

[ 161](ra4m1-elc_8h.md#ad9e9a8451a683c5b5bc8a2ace8264c27)#define RA\_ELC\_EVENT\_SCI0\_RXI 0x098

[ 162](ra4m1-elc_8h.md#aecc4fdda2a7eeb2bab0b894f2e5047d9)#define RA\_ELC\_EVENT\_SCI0\_TXI 0x099

[ 163](ra4m1-elc_8h.md#ae845a850ab730c651badc5c857e28ee9)#define RA\_ELC\_EVENT\_SCI0\_TEI 0x09A

[ 164](ra4m1-elc_8h.md#ad4580e769bae423298276e31ee2ee071)#define RA\_ELC\_EVENT\_SCI0\_ERI 0x09B

[ 165](ra4m1-elc_8h.md#ae2373b571584dae4d1c7fc57142ecb3c)#define RA\_ELC\_EVENT\_SCI0\_AM 0x09C

[ 166](ra4m1-elc_8h.md#ad52a4c7660a4e609976f7045305f8ca7)#define RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI 0x09D

[ 167](ra4m1-elc_8h.md#ae936e9aa971a376cb4ea3405c68d57f0)#define RA\_ELC\_EVENT\_SCI1\_RXI 0x09E

[ 168](ra4m1-elc_8h.md#abd1c6187f97f2817dc5eb59278a996b1)#define RA\_ELC\_EVENT\_SCI1\_TXI 0x09F

[ 169](ra4m1-elc_8h.md#aae0ca4a1031af4c490fbb1ecbe201662)#define RA\_ELC\_EVENT\_SCI1\_TEI 0x0A0

[ 170](ra4m1-elc_8h.md#a6a673466eb5261d23ee06be132ca9cde)#define RA\_ELC\_EVENT\_SCI1\_ERI 0x0A1

[ 171](ra4m1-elc_8h.md#ad9ca7dbcac36bb7f921cd8b8db761623)#define RA\_ELC\_EVENT\_SCI1\_AM 0x0A2

[ 172](ra4m1-elc_8h.md#a484b0928fab1e96f3008b9e7b12bab07)#define RA\_ELC\_EVENT\_SCI2\_RXI 0x0A3

[ 173](ra4m1-elc_8h.md#a5991f7636af52ea3285cf17d300f62bb)#define RA\_ELC\_EVENT\_SCI2\_TXI 0x0A4

[ 174](ra4m1-elc_8h.md#a9bbdd2f449bfd5709f6c8b77b8378ca4)#define RA\_ELC\_EVENT\_SCI2\_TEI 0x0A5

[ 175](ra4m1-elc_8h.md#ad31428c7900c978dba266761df793f4c)#define RA\_ELC\_EVENT\_SCI2\_ERI 0x0A6

[ 176](ra4m1-elc_8h.md#a023110baac3b030238844ab6a8999652)#define RA\_ELC\_EVENT\_SCI2\_AM 0x0A7

[ 177](ra4m1-elc_8h.md#ac01e51a9360f409e430642d86818bf98)#define RA\_ELC\_EVENT\_SCI9\_RXI 0x0A8

[ 178](ra4m1-elc_8h.md#a8c628c59b08ed53781fd406ea22da796)#define RA\_ELC\_EVENT\_SCI9\_TXI 0x0A9

[ 179](ra4m1-elc_8h.md#ac3a064375ff90f3a6a35c5fdda680f95)#define RA\_ELC\_EVENT\_SCI9\_TEI 0x0AA

[ 180](ra4m1-elc_8h.md#af2e4d2d6b59c512e536d901789b3c1a2)#define RA\_ELC\_EVENT\_SCI9\_ERI 0x0AB

[ 181](ra4m1-elc_8h.md#a2bfc7def09c933262aa530227a45af7d)#define RA\_ELC\_EVENT\_SCI9\_AM 0x0AC

[ 182](ra4m1-elc_8h.md#af77608914a79bea7797b63674c71db31)#define RA\_ELC\_EVENT\_SPI0\_RXI 0x0AD

[ 183](ra4m1-elc_8h.md#a82d87016b5d694884bba33bf71e93e92)#define RA\_ELC\_EVENT\_SPI0\_TXI 0x0AE

[ 184](ra4m1-elc_8h.md#a920575ee3a202b0d7202cd053f1e235b)#define RA\_ELC\_EVENT\_SPI0\_IDLE 0x0AF

[ 185](ra4m1-elc_8h.md#ab588fafc974153bcf94087cdb1a71d73)#define RA\_ELC\_EVENT\_SPI0\_ERI 0x0B0

[ 186](ra4m1-elc_8h.md#a368a0ece3d89efe3ed8ab274471849b9)#define RA\_ELC\_EVENT\_SPI0\_TEI 0x0B1

[ 187](ra4m1-elc_8h.md#a2f5e3b5957e42c572fda94ec535b401b)#define RA\_ELC\_EVENT\_SPI1\_RXI 0x0B2

[ 188](ra4m1-elc_8h.md#a0aab8e60c14b34bccb74400a818524ac)#define RA\_ELC\_EVENT\_SPI1\_TXI 0x0B3

[ 189](ra4m1-elc_8h.md#a73da76e435d9de6b6b7ad48190d2c0a2)#define RA\_ELC\_EVENT\_SPI1\_IDLE 0x0B4

[ 190](ra4m1-elc_8h.md#aedf36efaaba39c4001386536d21f81e2)#define RA\_ELC\_EVENT\_SPI1\_ERI 0x0B5

[ 191](ra4m1-elc_8h.md#a60f40983e3c6344a257bd157b40069d5)#define RA\_ELC\_EVENT\_SPI1\_TEI 0x0B6

192

193/\* Possible peripherals to be linked to event signals \*/

[ 194](ra4m1-elc_8h.md#ad6bb2d32abfad10bd283894efb7fe968)#define RA\_ELC\_PERIPHERAL\_GPT\_A 0

[ 195](ra4m1-elc_8h.md#a8c4b99abfaa798b3b15f3435a73bad86)#define RA\_ELC\_PERIPHERAL\_GPT\_B 1

[ 196](ra4m1-elc_8h.md#af0000625eec82c9f4ebe20da1cec7c66)#define RA\_ELC\_PERIPHERAL\_GPT\_C 2

[ 197](ra4m1-elc_8h.md#ae9ae748233cce2fa65b334c2f8b2a6f7)#define RA\_ELC\_PERIPHERAL\_GPT\_D 3

[ 198](ra4m1-elc_8h.md#aefc3deade612ed7aa53abd397d20af3b)#define RA\_ELC\_PERIPHERAL\_GPT\_E 4

[ 199](ra4m1-elc_8h.md#a4bb2ffb785a17a225d5eb6e80f0040bf)#define RA\_ELC\_PERIPHERAL\_GPT\_F 5

[ 200](ra4m1-elc_8h.md#a2ccd7f6730384fb8550054ea2195a67a)#define RA\_ELC\_PERIPHERAL\_GPT\_G 6

[ 201](ra4m1-elc_8h.md#a6e737df13755e4e0039e98610aa31f3c)#define RA\_ELC\_PERIPHERAL\_GPT\_H 7

[ 202](ra4m1-elc_8h.md#a2b5a9232a4ad9d199dc9baa510d0ed54)#define RA\_ELC\_PERIPHERAL\_ADC0 8

[ 203](ra4m1-elc_8h.md#afaf4059726139d62e2c09010cfa1148a)#define RA\_ELC\_PERIPHERAL\_ADC0\_B 9

[ 204](ra4m1-elc_8h.md#a9a32ba5817467743fbcf24b698124b02)#define RA\_ELC\_PERIPHERAL\_DAC0 12

[ 205](ra4m1-elc_8h.md#a5830e830b7b10cd68441de2648edd6a0)#define RA\_ELC\_PERIPHERAL\_IOPORT1 14

[ 206](ra4m1-elc_8h.md#a42d4feb2c854cc1964455297e6d7eb72)#define RA\_ELC\_PERIPHERAL\_IOPORT2 15

[ 207](ra4m1-elc_8h.md#a349933f20d7b6f768e49239724d0c5f7)#define RA\_ELC\_PERIPHERAL\_IOPORT3 16

[ 208](ra4m1-elc_8h.md#a6d08d1db64f903fa2dacfc81568b004d)#define RA\_ELC\_PERIPHERAL\_IOPORT4 17

[ 209](ra4m1-elc_8h.md#a66a60a7a3469054498a247253cea97c0)#define RA\_ELC\_PERIPHERAL\_CTSU 18

210

211#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA4M1\_ELC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [misc](dir_b5927901ba0eeb0fdf9ca7870f5af60a.md)
- [renesas](dir_86b946318bd38151d049d676c19e4b11.md)
- [ra-elc](dir_fc824a581c07e3e227952b4fed9afa76.md)
- [ra4m1-elc.h](ra4m1-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
