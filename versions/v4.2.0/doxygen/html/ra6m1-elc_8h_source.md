---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra6m1-elc_8h_source.html
original_path: doxygen/html/ra6m1-elc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra6m1-elc.h

[Go to the documentation of this file.](ra6m1-elc_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA6M1\_ELC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA6M1\_ELC\_H\_

9

10/\* Sources of event signals to be linked to other peripherals or the CPU \*/

[ 11](ra6m1-elc_8h.md#a11b5cec97472328120a8d6381f1e8809)#define RA\_ELC\_EVENT\_NONE 0x0

[ 12](ra6m1-elc_8h.md#a04ee26d7188b7441627bb89249545cfa)#define RA\_ELC\_EVENT\_ICU\_IRQ0 0x001

[ 13](ra6m1-elc_8h.md#ac9f6681c03b50d8b3a24798b3e790170)#define RA\_ELC\_EVENT\_ICU\_IRQ1 0x002

[ 14](ra6m1-elc_8h.md#a136f93a17eea3f4233b0012c075fc904)#define RA\_ELC\_EVENT\_ICU\_IRQ2 0x003

[ 15](ra6m1-elc_8h.md#a65b92e543dfb43c213274652ae60314a)#define RA\_ELC\_EVENT\_ICU\_IRQ3 0x004

[ 16](ra6m1-elc_8h.md#a2b1930fc54010b7c4c00f286f690cb1e)#define RA\_ELC\_EVENT\_ICU\_IRQ4 0x005

[ 17](ra6m1-elc_8h.md#af3ecccfe646b6cac991310abe3e4b955)#define RA\_ELC\_EVENT\_ICU\_IRQ5 0x006

[ 18](ra6m1-elc_8h.md#a98b53eb7b5979403023805ba925c504c)#define RA\_ELC\_EVENT\_ICU\_IRQ6 0x007

[ 19](ra6m1-elc_8h.md#ab6f05849ddc30ceb693f57b522223bcf)#define RA\_ELC\_EVENT\_ICU\_IRQ7 0x008

[ 20](ra6m1-elc_8h.md#acbcd1c55530c6cb8580b76bd55c73c90)#define RA\_ELC\_EVENT\_ICU\_IRQ8 0x009

[ 21](ra6m1-elc_8h.md#af04ed29327af6c108875334c24d98e43)#define RA\_ELC\_EVENT\_ICU\_IRQ9 0x00A

[ 22](ra6m1-elc_8h.md#a3e9a895c4855c3db6ac7fc5900b57807)#define RA\_ELC\_EVENT\_ICU\_IRQ10 0x00B

[ 23](ra6m1-elc_8h.md#a46f43f1dd26e006c26b11bd45e53a728)#define RA\_ELC\_EVENT\_ICU\_IRQ11 0x00C

[ 24](ra6m1-elc_8h.md#affb7ae86a41c8cc8582e6c6ef284a5d8)#define RA\_ELC\_EVENT\_ICU\_IRQ12 0x00D

[ 25](ra6m1-elc_8h.md#ad7435ed602899357eae0f46c09bf542c)#define RA\_ELC\_EVENT\_ICU\_IRQ13 0x00E

[ 26](ra6m1-elc_8h.md#a906929a9ae7dd7de44d21a32d3635080)#define RA\_ELC\_EVENT\_DMAC0\_INT 0x020

[ 27](ra6m1-elc_8h.md#a76b9d9fa8af16a1480fcc8d8ec12572f)#define RA\_ELC\_EVENT\_DMAC1\_INT 0x021

[ 28](ra6m1-elc_8h.md#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)#define RA\_ELC\_EVENT\_DMAC2\_INT 0x022

[ 29](ra6m1-elc_8h.md#a0b9d72a41fd7c5b27e6c31967645b907)#define RA\_ELC\_EVENT\_DMAC3\_INT 0x023

[ 30](ra6m1-elc_8h.md#a4cae5afbbe49719555bbbfa12b8727f5)#define RA\_ELC\_EVENT\_DMAC4\_INT 0x024

[ 31](ra6m1-elc_8h.md#a000e31aba8a821f4358a435d280b3a7b)#define RA\_ELC\_EVENT\_DMAC5\_INT 0x025

[ 32](ra6m1-elc_8h.md#a2d1f6d1c797a0d787a5d5c08b0fc18ad)#define RA\_ELC\_EVENT\_DMAC6\_INT 0x026

[ 33](ra6m1-elc_8h.md#ae8caef45a510d4c4f1c55f923e01799e)#define RA\_ELC\_EVENT\_DMAC7\_INT 0x027

[ 34](ra6m1-elc_8h.md#a9a58e3a2c10447906aaf35bab5664d24)#define RA\_ELC\_EVENT\_DTC\_COMPLETE 0x029

[ 35](ra6m1-elc_8h.md#a5ab484cdaf470b47e95005d83d60394f)#define RA\_ELC\_EVENT\_DTC\_END 0x02A

[ 36](ra6m1-elc_8h.md#a26e0aaa4a17196ada130bbb714a6d3bd)#define RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL 0x02D

[ 37](ra6m1-elc_8h.md#a5c7545a2f69856b7b637ad690f158b77)#define RA\_ELC\_EVENT\_FCU\_FIFERR 0x030

[ 38](ra6m1-elc_8h.md#a535af54c8bcfff47cc90ba1226044d71)#define RA\_ELC\_EVENT\_FCU\_FRDYI 0x031

[ 39](ra6m1-elc_8h.md#a7ab275777147d06315a04abb3f2f6d51)#define RA\_ELC\_EVENT\_LVD\_LVD1 0x038

[ 40](ra6m1-elc_8h.md#ad52acadba107b7f907d678f44769a4cb)#define RA\_ELC\_EVENT\_LVD\_LVD2 0x039

[ 41](ra6m1-elc_8h.md#a290decf4254396cbce267cb52a619717)#define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP 0x03B

[ 42](ra6m1-elc_8h.md#ac6953f0c8caa6b5ef8c9893c7ff4baa1)#define RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST 0x03C

[ 43](ra6m1-elc_8h.md#a4c3604a42ead1d43f472e901087ec148)#define RA\_ELC\_EVENT\_AGT0\_INT 0x040

[ 44](ra6m1-elc_8h.md#a015e6f8aed4b467f4554e6887b4d9ec9)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A 0x041

[ 45](ra6m1-elc_8h.md#ada1ad302dc5b987a6f7c972afae729f2)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B 0x042

[ 46](ra6m1-elc_8h.md#a635180e38c932579072f4eebd665592f)#define RA\_ELC\_EVENT\_AGT1\_INT 0x043

[ 47](ra6m1-elc_8h.md#aeb2399818b6b141ab4a37e257dba22be)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A 0x044

[ 48](ra6m1-elc_8h.md#a1d660c78348b48ea7a072225491ae44b)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B 0x045

[ 49](ra6m1-elc_8h.md#abc837f1fcfffeb2ec231c79336379dda)#define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW 0x046

[ 50](ra6m1-elc_8h.md#a6cdb7a60a850f9ec23f19c548a6cc544)#define RA\_ELC\_EVENT\_WDT\_UNDERFLOW 0x047

[ 51](ra6m1-elc_8h.md#a76fd68b555574159d563d2dfd68d90b9)#define RA\_ELC\_EVENT\_RTC\_ALARM 0x048

[ 52](ra6m1-elc_8h.md#a144901ee7b31b96eba18a39d98c4b953)#define RA\_ELC\_EVENT\_RTC\_PERIOD 0x049

[ 53](ra6m1-elc_8h.md#a241cd3c65033b46a1160d5815cc86fd7)#define RA\_ELC\_EVENT\_RTC\_CARRY 0x04A

[ 54](ra6m1-elc_8h.md#ad7284976213551f7d4fa450bf2bf8c7c)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END 0x04B

[ 55](ra6m1-elc_8h.md#aecbe4efa29972b832e35ebb00d7499ad)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B 0x04C

[ 56](ra6m1-elc_8h.md#aa4feb2c3e29ba84d1397c618b7b860bf)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A 0x04D

[ 57](ra6m1-elc_8h.md#ab59c8ec4f20de5cf4709efe0a7ee70a1)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B 0x04E

[ 58](ra6m1-elc_8h.md#af187c78a1f05fc4be81aa3af36e4cde5)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH 0x04F

[ 59](ra6m1-elc_8h.md#a65d6c499a6852434b4802f8ef7066eb4)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH 0x050

[ 60](ra6m1-elc_8h.md#aa02ddf9a93b64b5fb5c6d60b51bc24ed)#define RA\_ELC\_EVENT\_ADC1\_SCAN\_END 0x051

[ 61](ra6m1-elc_8h.md#a1c3786e7e0f56f55d45ed55901a14bb4)#define RA\_ELC\_EVENT\_ADC1\_SCAN\_END\_B 0x052

[ 62](ra6m1-elc_8h.md#aef02cb8109fd68b4c4a1a5efca255583)#define RA\_ELC\_EVENT\_ADC1\_WINDOW\_A 0x053

[ 63](ra6m1-elc_8h.md#a283756acfcfe4c208cbaa5a3edd4d2cc)#define RA\_ELC\_EVENT\_ADC1\_WINDOW\_B 0x054

[ 64](ra6m1-elc_8h.md#adbc3a9f438323aed719c7e210829a78f)#define RA\_ELC\_EVENT\_ADC1\_COMPARE\_MATCH 0x055

[ 65](ra6m1-elc_8h.md#a12123fbc57d65b4ab932495bf0726d57)#define RA\_ELC\_EVENT\_ADC1\_COMPARE\_MISMATCH 0x056

[ 66](ra6m1-elc_8h.md#a3bbee94907736c0c435cc5ff64d1e7ef)#define RA\_ELC\_EVENT\_ACMPHS0\_INT 0x057

[ 67](ra6m1-elc_8h.md#ab1a4d1aee4743a0ee8bd194052a6c840)#define RA\_ELC\_EVENT\_ACMPHS1\_INT 0x058

[ 68](ra6m1-elc_8h.md#aa3f4964bbc1d37f3191ab5eed2e8b7c4)#define RA\_ELC\_EVENT\_ACMPHS2\_INT 0x059

[ 69](ra6m1-elc_8h.md#a544e4a1f321514c0fd56b03025760027)#define RA\_ELC\_EVENT\_ACMPHS3\_INT 0x05A

[ 70](ra6m1-elc_8h.md#a6fe63e96c5f7119e65f0a5940bb2b175)#define RA\_ELC\_EVENT\_ACMPHS4\_INT 0x05B

[ 71](ra6m1-elc_8h.md#a28342f5d9195feb3d7ab97faa7d2d41e)#define RA\_ELC\_EVENT\_ACMPHS5\_INT 0x05C

[ 72](ra6m1-elc_8h.md#ae4dbb89c58220f72818cc9c28d97905b)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_0 0x05F

[ 73](ra6m1-elc_8h.md#a0ef2efa2ea339cad7598f11fe549cdd9)#define RA\_ELC\_EVENT\_USBFS\_FIFO\_1 0x060

[ 74](ra6m1-elc_8h.md#aac8d97813e8a3276bdac764faf7b580d)#define RA\_ELC\_EVENT\_USBFS\_INT 0x061

[ 75](ra6m1-elc_8h.md#a9458dbf2b1da6fc51ca2c2933dcb6b37)#define RA\_ELC\_EVENT\_USBFS\_RESUME 0x062

[ 76](ra6m1-elc_8h.md#a7271a25cdc3c987313efbafcd2a746cf)#define RA\_ELC\_EVENT\_IIC0\_RXI 0x063

[ 77](ra6m1-elc_8h.md#a7843f8a23feb383202fa6ad3be8fae5c)#define RA\_ELC\_EVENT\_IIC0\_TXI 0x064

[ 78](ra6m1-elc_8h.md#a52270344b26073c127a0269c5ec4e228)#define RA\_ELC\_EVENT\_IIC0\_TEI 0x065

[ 79](ra6m1-elc_8h.md#a667eb763b55f973b141837e82dbbae6e)#define RA\_ELC\_EVENT\_IIC0\_ERI 0x066

[ 80](ra6m1-elc_8h.md#a2a074dab614a1639ea5fa4f6d3baffd3)#define RA\_ELC\_EVENT\_IIC0\_WUI 0x067

[ 81](ra6m1-elc_8h.md#ad03e6b81d0e7ce53737e5c3022f8d951)#define RA\_ELC\_EVENT\_IIC1\_RXI 0x068

[ 82](ra6m1-elc_8h.md#a641c91157c98f41d3cf5ff6bbe25192d)#define RA\_ELC\_EVENT\_IIC1\_TXI 0x069

[ 83](ra6m1-elc_8h.md#a45ed226ccaace8813aa653276a52999d)#define RA\_ELC\_EVENT\_IIC1\_TEI 0x06A

[ 84](ra6m1-elc_8h.md#a2221a129f0e323fa5b96bfe5ed0e007f)#define RA\_ELC\_EVENT\_IIC1\_ERI 0x06B

[ 85](ra6m1-elc_8h.md#ac65193048ce5734b46bc2bf77b84cb4e)#define RA\_ELC\_EVENT\_SSI0\_TXI 0x072

[ 86](ra6m1-elc_8h.md#ab736656ae0b06de8383189075cbb2f27)#define RA\_ELC\_EVENT\_SSI0\_RXI 0x073

[ 87](ra6m1-elc_8h.md#a1a89e9ab6abb3834992ee3ea3ebaf9c4)#define RA\_ELC\_EVENT\_SSI0\_INT 0x075

[ 88](ra6m1-elc_8h.md#a6bc6dfb405d829a193654f98153d3ea5)#define RA\_ELC\_EVENT\_SRC\_INPUT\_FIFO\_EMPTY 0x07A

[ 89](ra6m1-elc_8h.md#ae8986633c93b8e424e0d9b634f602cc8)#define RA\_ELC\_EVENT\_SRC\_OUTPUT\_FIFO\_FULL 0x07B

[ 90](ra6m1-elc_8h.md#aa9348e4eca59c627725caa4616de18ff)#define RA\_ELC\_EVENT\_SRC\_OUTPUT\_FIFO\_OVERFLOW 0x07C

[ 91](ra6m1-elc_8h.md#abd6b3f0e54dd128191a1ec112a768f02)#define RA\_ELC\_EVENT\_SRC\_OUTPUT\_FIFO\_UNDERFLOW 0x07D

[ 92](ra6m1-elc_8h.md#a965b3da128eb05bb4bab3758b7f5ac1d)#define RA\_ELC\_EVENT\_SRC\_CONVERSION\_END 0x07E

[ 93](ra6m1-elc_8h.md#a2faf033bad7b355f8beb9386a2d0e93b)#define RA\_ELC\_EVENT\_CTSU\_WRITE 0x082

[ 94](ra6m1-elc_8h.md#ad7cd21f5db3e117b87ffab8a6cb47272)#define RA\_ELC\_EVENT\_CTSU\_READ 0x083

[ 95](ra6m1-elc_8h.md#acfe8138822bcd3f02fe50316e40c7641)#define RA\_ELC\_EVENT\_CTSU\_END 0x084

[ 96](ra6m1-elc_8h.md#a4412a0ec84a10d14d131754c5f9eb509)#define RA\_ELC\_EVENT\_KEY\_INT 0x085

[ 97](ra6m1-elc_8h.md#ab6c210d6481294137fd4bc32c39e5de1)#define RA\_ELC\_EVENT\_DOC\_INT 0x086

[ 98](ra6m1-elc_8h.md#a6ec3edb5e4de5bca1171ade1aa9ca19f)#define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR 0x087

[ 99](ra6m1-elc_8h.md#a1390ee9467a9d093de1532f0703ec35f)#define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END 0x088

[ 100](ra6m1-elc_8h.md#a3463c1e202ab7891521eda7196e1be80)#define RA\_ELC\_EVENT\_CAC\_OVERFLOW 0x089

[ 101](ra6m1-elc_8h.md#aa4f3b915e26ee83dcc8c383a1fdb2425)#define RA\_ELC\_EVENT\_CAN0\_ERROR 0x08A

[ 102](ra6m1-elc_8h.md#ad6e2ac69f8d10baa2d023e680e2f4c2f)#define RA\_ELC\_EVENT\_CAN0\_FIFO\_RX 0x08B

[ 103](ra6m1-elc_8h.md#a52d0f15f6d388658ae060aec6302b448)#define RA\_ELC\_EVENT\_CAN0\_FIFO\_TX 0x08C

[ 104](ra6m1-elc_8h.md#a0b017dad5f8642aa70f6f96c45e84a72)#define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX 0x08D

[ 105](ra6m1-elc_8h.md#a71880c5fc6363d67d8d126fd63a5354c)#define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX 0x08E

[ 106](ra6m1-elc_8h.md#a3f2a843a1ec42fd602f4acff889d4cec)#define RA\_ELC\_EVENT\_CAN1\_ERROR 0x08F

[ 107](ra6m1-elc_8h.md#a2e6ba842099389207bc1ce23ff718022)#define RA\_ELC\_EVENT\_CAN1\_FIFO\_RX 0x090

[ 108](ra6m1-elc_8h.md#a147d136d3878246377f834aebb31fccc)#define RA\_ELC\_EVENT\_CAN1\_FIFO\_TX 0x091

[ 109](ra6m1-elc_8h.md#a56a7ecc9080083a858b934c007fd54ea)#define RA\_ELC\_EVENT\_CAN1\_MAILBOX\_RX 0x092

[ 110](ra6m1-elc_8h.md#aa59bee7f791007e76284a5466c845ed4)#define RA\_ELC\_EVENT\_CAN1\_MAILBOX\_TX 0x093

[ 111](ra6m1-elc_8h.md#aee58e9a0c4313f0ec08f0652e5002008)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1 0x094

[ 112](ra6m1-elc_8h.md#a36d858520d28847eead0fbfe7950be2d)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2 0x095

[ 113](ra6m1-elc_8h.md#a545dadce70bbcea1116cd13490fe2571)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_3 0x096

[ 114](ra6m1-elc_8h.md#a4e478b84ef99ae71c102ad3d5c71089a)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_4 0x097

[ 115](ra6m1-elc_8h.md#ae5c28618f4e68eef6ca83bdcec515abb)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0 0x098

[ 116](ra6m1-elc_8h.md#a9f0b82bfff5ea2ba414ac0bccad9a34d)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1 0x099

[ 117](ra6m1-elc_8h.md#a81e18423a1f61e34f0daab6f7367eae2)#define RA\_ELC\_EVENT\_POEG0\_EVENT 0x09A

[ 118](ra6m1-elc_8h.md#a2a43c2ce461fde766e66a4451929a875)#define RA\_ELC\_EVENT\_POEG1\_EVENT 0x09B

[ 119](ra6m1-elc_8h.md#a7b5c16202b2491ba77319a180bcaa107)#define RA\_ELC\_EVENT\_POEG2\_EVENT 0x09C

[ 120](ra6m1-elc_8h.md#ab39d06b130b93348c5fab589f1e0074e)#define RA\_ELC\_EVENT\_POEG3\_EVENT 0x09D

[ 121](ra6m1-elc_8h.md#aec8a8b590cc124ca12425f34b5a61020)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A 0x0B0

[ 122](ra6m1-elc_8h.md#ae1ed91479f405ac965da868e86bce533)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B 0x0B1

[ 123](ra6m1-elc_8h.md#a6d7c9090c21a8a0c497356050d649ec6)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_C 0x0B2

[ 124](ra6m1-elc_8h.md#af5b8ca097747bd987e81d8d81263aa81)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_D 0x0B3

[ 125](ra6m1-elc_8h.md#a9ebec21375578c0e52d953773373bf1e)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_E 0x0B4

[ 126](ra6m1-elc_8h.md#ad503a55a4548ff6ffd58e2b74d9eaf00)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_F 0x0B5

[ 127](ra6m1-elc_8h.md#a76692948000993fde4d286f1a521a6d2)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW 0x0B6

[ 128](ra6m1-elc_8h.md#a9edde37b8c0835978aa55d58d77c5ad5)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW 0x0B7

[ 129](ra6m1-elc_8h.md#a8c54ce860777032d9143077a5246c3d2)#define RA\_ELC\_EVENT\_GPT0\_AD\_TRIG\_A 0x0B8

[ 130](ra6m1-elc_8h.md#af3593fcaa05166f3993f9b136d1e1a71)#define RA\_ELC\_EVENT\_GPT0\_AD\_TRIG\_B 0x0B9

[ 131](ra6m1-elc_8h.md#a33a428565bfa3237aa4eda10b982fc65)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A 0x0BA

[ 132](ra6m1-elc_8h.md#a5326aaf270290b524f8cb2e126d06602)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B 0x0BB

[ 133](ra6m1-elc_8h.md#a2e55bae34ab30f2d802b8eaf93dd3cfd)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C 0x0BC

[ 134](ra6m1-elc_8h.md#ada3870f40beeec10e9366e908ed980d0)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D 0x0BD

[ 135](ra6m1-elc_8h.md#a5d4f72e95b7bb76315b9ffa059730620)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E 0x0BE

[ 136](ra6m1-elc_8h.md#a548923b7385648e4f15fef4ecb315478)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F 0x0BF

[ 137](ra6m1-elc_8h.md#aa6eac7cf283073eea62fbaa1df2017f2)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW 0x0C0

[ 138](ra6m1-elc_8h.md#ae8cefd5f23897d43cffba4e91b7c8b5c)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW 0x0C1

[ 139](ra6m1-elc_8h.md#aaa3f7fe99d60fc9891b9ef416ecbd698)#define RA\_ELC\_EVENT\_GPT1\_AD\_TRIG\_A 0x0C2

[ 140](ra6m1-elc_8h.md#aacf6ed4895b5a98bc67b109eb41d6d7b)#define RA\_ELC\_EVENT\_GPT1\_AD\_TRIG\_B 0x0C3

[ 141](ra6m1-elc_8h.md#ad1a5796e0c70a988165765f2ce8c1e80)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A 0x0C4

[ 142](ra6m1-elc_8h.md#a73776ba7d66a478c92c6cb3dfed50af4)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B 0x0C5

[ 143](ra6m1-elc_8h.md#aa391fa888ded57351c9b62f54df1ce36)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C 0x0C6

[ 144](ra6m1-elc_8h.md#a90c7aa7bbddb04e6ae4b6eccb64a0e93)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D 0x0C7

[ 145](ra6m1-elc_8h.md#adbfb562e616a86a3e28f8c3f09553db9)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E 0x0C8

[ 146](ra6m1-elc_8h.md#a6f07945c82efae23754e34dc09bee884)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F 0x0C9

[ 147](ra6m1-elc_8h.md#aede7879166ef812139641122782d873b)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW 0x0CA

[ 148](ra6m1-elc_8h.md#ad71d20ad5434f219a61e0f0aded090d1)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW 0x0CB

[ 149](ra6m1-elc_8h.md#a96bbd3418d8b51a80cef1d0a258095f0)#define RA\_ELC\_EVENT\_GPT2\_AD\_TRIG\_A 0x0CC

[ 150](ra6m1-elc_8h.md#ab465f8fec7d2c7dcc742f25215609d2f)#define RA\_ELC\_EVENT\_GPT2\_AD\_TRIG\_B 0x0CD

[ 151](ra6m1-elc_8h.md#a74526500dfb573fe21fbca739b1698e1)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A 0x0CE

[ 152](ra6m1-elc_8h.md#ac6cfac3496e4ab71c9bf84b43e06486a)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B 0x0CF

[ 153](ra6m1-elc_8h.md#a1af4840d468eb4c4e1672a34652ef583)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_C 0x0D0

[ 154](ra6m1-elc_8h.md#a263e6b02601dd37d6eedaab56a2e6fcd)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_D 0x0D1

[ 155](ra6m1-elc_8h.md#a9035e080d39d60ecc898a596b9902aa6)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_E 0x0D2

[ 156](ra6m1-elc_8h.md#a9cffb5aca60a4c7349789fc23fb197fb)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_F 0x0D3

[ 157](ra6m1-elc_8h.md#a546eff128c44a29f56fe90952cef475d)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW 0x0D4

[ 158](ra6m1-elc_8h.md#ab30a5683e48535abbf0c400a5a0d8946)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW 0x0D5

[ 159](ra6m1-elc_8h.md#a339cba7a0388f06c6c64ca31f790e2a6)#define RA\_ELC\_EVENT\_GPT3\_AD\_TRIG\_A 0x0D6

[ 160](ra6m1-elc_8h.md#a42c29ea80743756649f7b0ba64089844)#define RA\_ELC\_EVENT\_GPT3\_AD\_TRIG\_B 0x0D7

[ 161](ra6m1-elc_8h.md#a8130aa176d9d5dd698c62708111515e0)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A 0x0D8

[ 162](ra6m1-elc_8h.md#aa77a30a219070d15e358a43fbbd89728)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B 0x0D9

[ 163](ra6m1-elc_8h.md#af6c1cb172b343baa8d8bbe01d1674922)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C 0x0DA

[ 164](ra6m1-elc_8h.md#ae8c7945c641045c615922a3f82329c56)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D 0x0DB

[ 165](ra6m1-elc_8h.md#afcb271a94d9b07b7b1a204f325b80d52)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E 0x0DC

[ 166](ra6m1-elc_8h.md#a906eb0e1ed2786ed2b14e4608489b2cc)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F 0x0DD

[ 167](ra6m1-elc_8h.md#abb820eb80ad8afc5c12dc3581fc7a0b9)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW 0x0DE

[ 168](ra6m1-elc_8h.md#a65831ae6b037607dc55a2b1e8aa296a7)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW 0x0DF

[ 169](ra6m1-elc_8h.md#aeb0e1a8b6d75a81af57d8a3bb214ee1c)#define RA\_ELC\_EVENT\_GPT4\_AD\_TRIG\_A 0x0E0

[ 170](ra6m1-elc_8h.md#abb7899ca9b02154f712bdce109c1cc50)#define RA\_ELC\_EVENT\_GPT4\_AD\_TRIG\_B 0x0E1

[ 171](ra6m1-elc_8h.md#adc4aceff99f296b06938254f9dcc1f2f)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A 0x0E2

[ 172](ra6m1-elc_8h.md#aad1fc8b32dffaaa64f9908951f8b1c64)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B 0x0E3

[ 173](ra6m1-elc_8h.md#aebaa50f4643efe5b87798777cee578bc)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C 0x0E4

[ 174](ra6m1-elc_8h.md#a21965e21bd4045aa5010925620b4d827)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D 0x0E5

[ 175](ra6m1-elc_8h.md#a51a7cb146f0efbb7bc9f7336031006a4)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E 0x0E6

[ 176](ra6m1-elc_8h.md#abbd0bd21af2bd1679d6d7bc36001b97d)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F 0x0E7

[ 177](ra6m1-elc_8h.md#a038e7580f03fbdd74f417108cd2a8b4d)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW 0x0E8

[ 178](ra6m1-elc_8h.md#ac38b8f1154d6a699923b2bbf249e38fd)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW 0x0E9

[ 179](ra6m1-elc_8h.md#a484a2a98e228eb884dfa951ad5cc82b5)#define RA\_ELC\_EVENT\_GPT5\_AD\_TRIG\_A 0x0EA

[ 180](ra6m1-elc_8h.md#a1b966ae97beca35cc342d06ca8fed5fc)#define RA\_ELC\_EVENT\_GPT5\_AD\_TRIG\_B 0x0EB

[ 181](ra6m1-elc_8h.md#acad1c37929903ddee569f40a3c5c59e3)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A 0x0EC

[ 182](ra6m1-elc_8h.md#aa0fc9b447efbcba0bb6800f785daeb96)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B 0x0ED

[ 183](ra6m1-elc_8h.md#a01f586bd98832ea9b8aa58741b61a319)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_C 0x0EE

[ 184](ra6m1-elc_8h.md#acd71c3b8e8e1d96aa3ff6affb93f5000)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_D 0x0EF

[ 185](ra6m1-elc_8h.md#a6abdcc7a6331a8283cfe0c1ac06b7d83)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_E 0x0F0

[ 186](ra6m1-elc_8h.md#a28b6b55ad533e3cb606b2b0937c916b3)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_F 0x0F1

[ 187](ra6m1-elc_8h.md#ac3c8dd6a5b7f95dccc58e7ec4e235a40)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW 0x0F2

[ 188](ra6m1-elc_8h.md#acdece33585a75fccba962e4f764058fb)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW 0x0F3

[ 189](ra6m1-elc_8h.md#a7dc55b6e1fb765b8768c1b7aa36dc9d2)#define RA\_ELC\_EVENT\_GPT6\_AD\_TRIG\_A 0x0F4

[ 190](ra6m1-elc_8h.md#ae023d12652989d13bc908b7033cd900d)#define RA\_ELC\_EVENT\_GPT6\_AD\_TRIG\_B 0x0F5

[ 191](ra6m1-elc_8h.md#afe1b39e5d37a5ed631dd18869cfbac8a)#define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A 0x0F6

[ 192](ra6m1-elc_8h.md#a53b7cfc8d0a000bd57f159b09b0a9c26)#define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B 0x0F7

[ 193](ra6m1-elc_8h.md#add91262eba9ec860b788030af153161a)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_C 0x0F8

[ 194](ra6m1-elc_8h.md#a9310fd708ca6f0afcf374bfc96e22e6e)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_D 0x0F9

[ 195](ra6m1-elc_8h.md#a8d18bd54c972d1de01c2a9f86e832cd0)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_E 0x0FA

[ 196](ra6m1-elc_8h.md#aca89f90e8afa3f656e76f5960717543c)#define RA\_ELC\_EVENT\_GPT7\_COMPARE\_F 0x0FB

[ 197](ra6m1-elc_8h.md#aac0ed7abde81cf4bcc7588bf64b53c04)#define RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW 0x0FC

[ 198](ra6m1-elc_8h.md#ab1935670b6c0a5b5629ef8ba9d854f6c)#define RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW 0x0FD

[ 199](ra6m1-elc_8h.md#a51637040385d036cb2e7fa5f5e536932)#define RA\_ELC\_EVENT\_GPT7\_AD\_TRIG\_A 0x0FE

[ 200](ra6m1-elc_8h.md#acc19c67f793130fd6f8e48cfe43ee62d)#define RA\_ELC\_EVENT\_GPT7\_AD\_TRIG\_B 0x0FF

[ 201](ra6m1-elc_8h.md#acbe756d66c556dab820bbba06e67248c)#define RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_A 0x100

[ 202](ra6m1-elc_8h.md#a86965f2d57f55861ddb995b2b1381aae)#define RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_B 0x101

[ 203](ra6m1-elc_8h.md#af58a21982c9fb458bd12cf1d3922ffd2)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_C 0x102

[ 204](ra6m1-elc_8h.md#a9d76f5a9c5546d1410b741ec7862713c)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_D 0x103

[ 205](ra6m1-elc_8h.md#a9d6cf6e4081dd7ef14196fd754838224)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_E 0x104

[ 206](ra6m1-elc_8h.md#abac4f8da4010bc5753188cc9bbce4feb)#define RA\_ELC\_EVENT\_GPT8\_COMPARE\_F 0x105

[ 207](ra6m1-elc_8h.md#a560a2f23d31c99d46b5de3fb65b3c066)#define RA\_ELC\_EVENT\_GPT8\_COUNTER\_OVERFLOW 0x106

[ 208](ra6m1-elc_8h.md#a217a7f7cdd39114472fc4276fc2337a2)#define RA\_ELC\_EVENT\_GPT8\_COUNTER\_UNDERFLOW 0x107

[ 209](ra6m1-elc_8h.md#a1b1bc8aa177575a9928b87d4270d3293)#define RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_A 0x10A

[ 210](ra6m1-elc_8h.md#a9d37d2fabd4ff799c0b6a1f2e7131b50)#define RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_B 0x10B

[ 211](ra6m1-elc_8h.md#a0654be705490f32e47348cb31dea046d)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_C 0x10C

[ 212](ra6m1-elc_8h.md#af204da0f122a67c5374ebdcd231684b0)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_D 0x10D

[ 213](ra6m1-elc_8h.md#a7af6cbe91bfe594230d36a60a684877c)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_E 0x10E

[ 214](ra6m1-elc_8h.md#ad2ad78dddd8c2b7dc560ec75439870ce)#define RA\_ELC\_EVENT\_GPT9\_COMPARE\_F 0x10F

[ 215](ra6m1-elc_8h.md#ab5599f7f5509cbdae09668ec09078625)#define RA\_ELC\_EVENT\_GPT9\_COUNTER\_OVERFLOW 0x110

[ 216](ra6m1-elc_8h.md#aab44882a60fd898b847597a64ad1ec05)#define RA\_ELC\_EVENT\_GPT9\_COUNTER\_UNDERFLOW 0x111

[ 217](ra6m1-elc_8h.md#a3e446393f52c0b25041942b552e74816)#define RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_A 0x114

[ 218](ra6m1-elc_8h.md#a2333e30317873b25420483f93f9039e7)#define RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_B 0x115

[ 219](ra6m1-elc_8h.md#aae47fb3196b5989c45883943619dbe02)#define RA\_ELC\_EVENT\_GPT10\_COMPARE\_C 0x116

[ 220](ra6m1-elc_8h.md#a7210f910c16be4bdeae56e5d10b9ab94)#define RA\_ELC\_EVENT\_GPT10\_COMPARE\_D 0x117

[ 221](ra6m1-elc_8h.md#a7d195f17c9da519dae057c9d337e0443)#define RA\_ELC\_EVENT\_GPT10\_COMPARE\_E 0x118

[ 222](ra6m1-elc_8h.md#ae2ad03f6c166fc2470e3b76623f81444)#define RA\_ELC\_EVENT\_GPT10\_COMPARE\_F 0x119

[ 223](ra6m1-elc_8h.md#abbdcc7f1ec056632b1f162527570ebd4)#define RA\_ELC\_EVENT\_GPT10\_COUNTER\_OVERFLOW 0x11A

[ 224](ra6m1-elc_8h.md#a7475c7d51460f60c7f1ace0e744b1e7f)#define RA\_ELC\_EVENT\_GPT10\_COUNTER\_UNDERFLOW 0x11B

[ 225](ra6m1-elc_8h.md#a71d10e75f9dc2beef51e422160a9b600)#define RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_A 0x11E

[ 226](ra6m1-elc_8h.md#af45005c2897b2d3e17652426e7ba0ffb)#define RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_B 0x11F

[ 227](ra6m1-elc_8h.md#af329a1e7556fc745376fb9912af82e85)#define RA\_ELC\_EVENT\_GPT11\_COMPARE\_C 0x120

[ 228](ra6m1-elc_8h.md#a38b26e657a05bf629e023e2cc18fec6d)#define RA\_ELC\_EVENT\_GPT11\_COMPARE\_D 0x121

[ 229](ra6m1-elc_8h.md#aa6967c733b94450076f0468049f8a580)#define RA\_ELC\_EVENT\_GPT11\_COMPARE\_E 0x122

[ 230](ra6m1-elc_8h.md#a5c504ecc48d5beb357cdd42292af6072)#define RA\_ELC\_EVENT\_GPT11\_COMPARE\_F 0x123

[ 231](ra6m1-elc_8h.md#a65114b19113928d597ea9e1040c63e86)#define RA\_ELC\_EVENT\_GPT11\_COUNTER\_OVERFLOW 0x124

[ 232](ra6m1-elc_8h.md#ad17299e05623683967d4b3652df71050)#define RA\_ELC\_EVENT\_GPT11\_COUNTER\_UNDERFLOW 0x125

[ 233](ra6m1-elc_8h.md#af703c7f5148f647cf99f15f5017b9b8e)#define RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_A 0x128

[ 234](ra6m1-elc_8h.md#ab61dcfc42e758bd67fff2e3e0cc7462e)#define RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_B 0x129

[ 235](ra6m1-elc_8h.md#a70cbb57f4225aa5064043caaeb34f14c)#define RA\_ELC\_EVENT\_GPT12\_COMPARE\_C 0x12A

[ 236](ra6m1-elc_8h.md#aac6e70fd9c5806050ca602cdfaff94af)#define RA\_ELC\_EVENT\_GPT12\_COMPARE\_D 0x12B

[ 237](ra6m1-elc_8h.md#a542befd78aec05f096611817a090d542)#define RA\_ELC\_EVENT\_GPT12\_COMPARE\_E 0x12C

[ 238](ra6m1-elc_8h.md#ac51ca6a913774b5dbb991a15fb37cf98)#define RA\_ELC\_EVENT\_GPT12\_COMPARE\_F 0x12D

[ 239](ra6m1-elc_8h.md#ae3c96e8c252ccaf26b2059bd39d7de3a)#define RA\_ELC\_EVENT\_GPT12\_COUNTER\_OVERFLOW 0x12E

[ 240](ra6m1-elc_8h.md#ad9d2590f2cfd624f475718d459fb3d45)#define RA\_ELC\_EVENT\_GPT12\_COUNTER\_UNDERFLOW 0x12F

[ 241](ra6m1-elc_8h.md#a8438d8d92e1950681388b40385a2c354)#define RA\_ELC\_EVENT\_OPS\_UVW\_EDGE 0x150

[ 242](ra6m1-elc_8h.md#ad9e9a8451a683c5b5bc8a2ace8264c27)#define RA\_ELC\_EVENT\_SCI0\_RXI 0x174

[ 243](ra6m1-elc_8h.md#aecc4fdda2a7eeb2bab0b894f2e5047d9)#define RA\_ELC\_EVENT\_SCI0\_TXI 0x175

[ 244](ra6m1-elc_8h.md#ae845a850ab730c651badc5c857e28ee9)#define RA\_ELC\_EVENT\_SCI0\_TEI 0x176

[ 245](ra6m1-elc_8h.md#ad4580e769bae423298276e31ee2ee071)#define RA\_ELC\_EVENT\_SCI0\_ERI 0x177

[ 246](ra6m1-elc_8h.md#ae2373b571584dae4d1c7fc57142ecb3c)#define RA\_ELC\_EVENT\_SCI0\_AM 0x178

[ 247](ra6m1-elc_8h.md#ad52a4c7660a4e609976f7045305f8ca7)#define RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI 0x179

[ 248](ra6m1-elc_8h.md#ae936e9aa971a376cb4ea3405c68d57f0)#define RA\_ELC\_EVENT\_SCI1\_RXI 0x17A

[ 249](ra6m1-elc_8h.md#abd1c6187f97f2817dc5eb59278a996b1)#define RA\_ELC\_EVENT\_SCI1\_TXI 0x17B

[ 250](ra6m1-elc_8h.md#aae0ca4a1031af4c490fbb1ecbe201662)#define RA\_ELC\_EVENT\_SCI1\_TEI 0x17C

[ 251](ra6m1-elc_8h.md#a6a673466eb5261d23ee06be132ca9cde)#define RA\_ELC\_EVENT\_SCI1\_ERI 0x17D

[ 252](ra6m1-elc_8h.md#ad9ca7dbcac36bb7f921cd8b8db761623)#define RA\_ELC\_EVENT\_SCI1\_AM 0x17E

[ 253](ra6m1-elc_8h.md#a484b0928fab1e96f3008b9e7b12bab07)#define RA\_ELC\_EVENT\_SCI2\_RXI 0x180

[ 254](ra6m1-elc_8h.md#a5991f7636af52ea3285cf17d300f62bb)#define RA\_ELC\_EVENT\_SCI2\_TXI 0x181

[ 255](ra6m1-elc_8h.md#a9bbdd2f449bfd5709f6c8b77b8378ca4)#define RA\_ELC\_EVENT\_SCI2\_TEI 0x182

[ 256](ra6m1-elc_8h.md#ad31428c7900c978dba266761df793f4c)#define RA\_ELC\_EVENT\_SCI2\_ERI 0x183

[ 257](ra6m1-elc_8h.md#a023110baac3b030238844ab6a8999652)#define RA\_ELC\_EVENT\_SCI2\_AM 0x184

[ 258](ra6m1-elc_8h.md#a87a1f07a2b420f9ce8d7ebcc1c505986)#define RA\_ELC\_EVENT\_SCI3\_RXI 0x186

[ 259](ra6m1-elc_8h.md#aee0548d7714ebd04748eadf9e9dbb97c)#define RA\_ELC\_EVENT\_SCI3\_TXI 0x187

[ 260](ra6m1-elc_8h.md#a6f9d20424191f026030159511647f913)#define RA\_ELC\_EVENT\_SCI3\_TEI 0x188

[ 261](ra6m1-elc_8h.md#ab7a6ad3ccc6279863a491a3787fd5c5e)#define RA\_ELC\_EVENT\_SCI3\_ERI 0x189

[ 262](ra6m1-elc_8h.md#a075f80d14abaa63627574519b9ebf36b)#define RA\_ELC\_EVENT\_SCI3\_AM 0x18A

[ 263](ra6m1-elc_8h.md#afe86466482eb03b85da9feb17bdccfc0)#define RA\_ELC\_EVENT\_SCI4\_RXI 0x18C

[ 264](ra6m1-elc_8h.md#a89f26e1bfd92cb7c9a2bad9acd80e553)#define RA\_ELC\_EVENT\_SCI4\_TXI 0x18D

[ 265](ra6m1-elc_8h.md#a2554192500a5ac058fbd338d3018f6cc)#define RA\_ELC\_EVENT\_SCI4\_TEI 0x18E

[ 266](ra6m1-elc_8h.md#ac6f2b3938cde7ba80faf523548dfa6c2)#define RA\_ELC\_EVENT\_SCI4\_ERI 0x18F

[ 267](ra6m1-elc_8h.md#abddf2cbec24fd59c9330b0328a21f82e)#define RA\_ELC\_EVENT\_SCI4\_AM 0x190

[ 268](ra6m1-elc_8h.md#afd0fe00167d99961d779e4b042db872a)#define RA\_ELC\_EVENT\_SCI8\_RXI 0x1A4

[ 269](ra6m1-elc_8h.md#ab8cc1c2b5ba23fe5550852ac7aaa33c0)#define RA\_ELC\_EVENT\_SCI8\_TXI 0x1A5

[ 270](ra6m1-elc_8h.md#ae9b08fd3131d828f67dda3523a7703be)#define RA\_ELC\_EVENT\_SCI8\_TEI 0x1A6

[ 271](ra6m1-elc_8h.md#a00d75172222030ff4002afb25513fbb8)#define RA\_ELC\_EVENT\_SCI8\_ERI 0x1A7

[ 272](ra6m1-elc_8h.md#a53e9096dcd5e219f5bb989768cb0672b)#define RA\_ELC\_EVENT\_SCI8\_AM 0x1A8

[ 273](ra6m1-elc_8h.md#ac01e51a9360f409e430642d86818bf98)#define RA\_ELC\_EVENT\_SCI9\_RXI 0x1AA

[ 274](ra6m1-elc_8h.md#a8c628c59b08ed53781fd406ea22da796)#define RA\_ELC\_EVENT\_SCI9\_TXI 0x1AB

[ 275](ra6m1-elc_8h.md#ac3a064375ff90f3a6a35c5fdda680f95)#define RA\_ELC\_EVENT\_SCI9\_TEI 0x1AC

[ 276](ra6m1-elc_8h.md#af2e4d2d6b59c512e536d901789b3c1a2)#define RA\_ELC\_EVENT\_SCI9\_ERI 0x1AD

[ 277](ra6m1-elc_8h.md#a2bfc7def09c933262aa530227a45af7d)#define RA\_ELC\_EVENT\_SCI9\_AM 0x1AE

[ 278](ra6m1-elc_8h.md#af77608914a79bea7797b63674c71db31)#define RA\_ELC\_EVENT\_SPI0\_RXI 0x1BC

[ 279](ra6m1-elc_8h.md#a82d87016b5d694884bba33bf71e93e92)#define RA\_ELC\_EVENT\_SPI0\_TXI 0x1BD

[ 280](ra6m1-elc_8h.md#a920575ee3a202b0d7202cd053f1e235b)#define RA\_ELC\_EVENT\_SPI0\_IDLE 0x1BE

[ 281](ra6m1-elc_8h.md#ab588fafc974153bcf94087cdb1a71d73)#define RA\_ELC\_EVENT\_SPI0\_ERI 0x1BF

[ 282](ra6m1-elc_8h.md#a368a0ece3d89efe3ed8ab274471849b9)#define RA\_ELC\_EVENT\_SPI0\_TEI 0x1C0

[ 283](ra6m1-elc_8h.md#a2f5e3b5957e42c572fda94ec535b401b)#define RA\_ELC\_EVENT\_SPI1\_RXI 0x1C1

[ 284](ra6m1-elc_8h.md#a0aab8e60c14b34bccb74400a818524ac)#define RA\_ELC\_EVENT\_SPI1\_TXI 0x1C2

[ 285](ra6m1-elc_8h.md#a73da76e435d9de6b6b7ad48190d2c0a2)#define RA\_ELC\_EVENT\_SPI1\_IDLE 0x1C3

[ 286](ra6m1-elc_8h.md#aedf36efaaba39c4001386536d21f81e2)#define RA\_ELC\_EVENT\_SPI1\_ERI 0x1C4

[ 287](ra6m1-elc_8h.md#a60f40983e3c6344a257bd157b40069d5)#define RA\_ELC\_EVENT\_SPI1\_TEI 0x1C5

[ 288](ra6m1-elc_8h.md#a344b216f0d5880b31e7c1a4e700c85a4)#define RA\_ELC\_EVENT\_QSPI\_INT 0x1C6

[ 289](ra6m1-elc_8h.md#a5d9c7d15a5c040aa9dfe002cf9df0657)#define RA\_ELC\_EVENT\_SDHIMMC0\_ACCS 0x1C7

[ 290](ra6m1-elc_8h.md#a93465058fd23dad3a735a53ad8689473)#define RA\_ELC\_EVENT\_SDHIMMC0\_SDIO 0x1C8

[ 291](ra6m1-elc_8h.md#a2bf8474e011e2ec0360e9e46deb7e960)#define RA\_ELC\_EVENT\_SDHIMMC0\_CARD 0x1C9

[ 292](ra6m1-elc_8h.md#a937bfe3314fb8d78775078db983ea473)#define RA\_ELC\_EVENT\_SDHIMMC0\_DMA\_REQ 0x1CA

[ 293](ra6m1-elc_8h.md#a7195add88b927dd230e66a931713f4e0)#define RA\_ELC\_EVENT\_SDHIMMC1\_ACCS 0x1CB

[ 294](ra6m1-elc_8h.md#a2dff7e869fad7918164e954bcb0a46bf)#define RA\_ELC\_EVENT\_SDHIMMC1\_SDIO 0x1CC

[ 295](ra6m1-elc_8h.md#ae8b2102091696bca7f60b008b9839444)#define RA\_ELC\_EVENT\_SDHIMMC1\_CARD 0x1CD

[ 296](ra6m1-elc_8h.md#a3b619f3e51ddcf2add17abd434bbf948)#define RA\_ELC\_EVENT\_SDHIMMC1\_DMA\_REQ 0x1CE

297

298/\* Possible peripherals to be linked to event signals \*/

[ 299](ra6m1-elc_8h.md#ad6bb2d32abfad10bd283894efb7fe968)#define RA\_ELC\_PERIPHERAL\_GPT\_A 0

[ 300](ra6m1-elc_8h.md#a8c4b99abfaa798b3b15f3435a73bad86)#define RA\_ELC\_PERIPHERAL\_GPT\_B 1

[ 301](ra6m1-elc_8h.md#af0000625eec82c9f4ebe20da1cec7c66)#define RA\_ELC\_PERIPHERAL\_GPT\_C 2

[ 302](ra6m1-elc_8h.md#ae9ae748233cce2fa65b334c2f8b2a6f7)#define RA\_ELC\_PERIPHERAL\_GPT\_D 3

[ 303](ra6m1-elc_8h.md#aefc3deade612ed7aa53abd397d20af3b)#define RA\_ELC\_PERIPHERAL\_GPT\_E 4

[ 304](ra6m1-elc_8h.md#a4bb2ffb785a17a225d5eb6e80f0040bf)#define RA\_ELC\_PERIPHERAL\_GPT\_F 5

[ 305](ra6m1-elc_8h.md#a2ccd7f6730384fb8550054ea2195a67a)#define RA\_ELC\_PERIPHERAL\_GPT\_G 6

[ 306](ra6m1-elc_8h.md#a6e737df13755e4e0039e98610aa31f3c)#define RA\_ELC\_PERIPHERAL\_GPT\_H 7

[ 307](ra6m1-elc_8h.md#a2b5a9232a4ad9d199dc9baa510d0ed54)#define RA\_ELC\_PERIPHERAL\_ADC0 8

[ 308](ra6m1-elc_8h.md#afaf4059726139d62e2c09010cfa1148a)#define RA\_ELC\_PERIPHERAL\_ADC0\_B 9

[ 309](ra6m1-elc_8h.md#aea69e6e72e14f53afeb85aa4a9349bcb)#define RA\_ELC\_PERIPHERAL\_ADC1 10

[ 310](ra6m1-elc_8h.md#adbd2118aea6d1ba6ca67de192f0033fc)#define RA\_ELC\_PERIPHERAL\_ADC1\_B 11

[ 311](ra6m1-elc_8h.md#a9a32ba5817467743fbcf24b698124b02)#define RA\_ELC\_PERIPHERAL\_DAC0 12

[ 312](ra6m1-elc_8h.md#a84aa20e3793499f427f6c9ccb7a20566)#define RA\_ELC\_PERIPHERAL\_DAC1 13

[ 313](ra6m1-elc_8h.md#a5830e830b7b10cd68441de2648edd6a0)#define RA\_ELC\_PERIPHERAL\_IOPORT1 14

[ 314](ra6m1-elc_8h.md#a42d4feb2c854cc1964455297e6d7eb72)#define RA\_ELC\_PERIPHERAL\_IOPORT2 15

[ 315](ra6m1-elc_8h.md#a349933f20d7b6f768e49239724d0c5f7)#define RA\_ELC\_PERIPHERAL\_IOPORT3 16

[ 316](ra6m1-elc_8h.md#a6d08d1db64f903fa2dacfc81568b004d)#define RA\_ELC\_PERIPHERAL\_IOPORT4 17

[ 317](ra6m1-elc_8h.md#a66a60a7a3469054498a247253cea97c0)#define RA\_ELC\_PERIPHERAL\_CTSU 18

318

319#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA6M1\_ELC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [misc](dir_b5927901ba0eeb0fdf9ca7870f5af60a.md)
- [renesas](dir_86b946318bd38151d049d676c19e4b11.md)
- [ra-elc](dir_fc824a581c07e3e227952b4fed9afa76.md)
- [ra6m1-elc.h](ra6m1-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
