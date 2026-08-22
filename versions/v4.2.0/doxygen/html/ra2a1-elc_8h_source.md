---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra2a1-elc_8h_source.html
original_path: doxygen/html/ra2a1-elc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra2a1-elc.h

[Go to the documentation of this file.](ra2a1-elc_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA2A1\_ELC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA2A1\_ELC\_H\_

9

10/\* Sources of event signals to be linked to other peripherals or the CPU \*/

[ 11](ra2a1-elc_8h.md#a11b5cec97472328120a8d6381f1e8809)#define RA\_ELC\_EVENT\_NONE 0x0

[ 12](ra2a1-elc_8h.md#a04ee26d7188b7441627bb89249545cfa)#define RA\_ELC\_EVENT\_ICU\_IRQ0 0x001

[ 13](ra2a1-elc_8h.md#ac9f6681c03b50d8b3a24798b3e790170)#define RA\_ELC\_EVENT\_ICU\_IRQ1 0x002

[ 14](ra2a1-elc_8h.md#a136f93a17eea3f4233b0012c075fc904)#define RA\_ELC\_EVENT\_ICU\_IRQ2 0x003

[ 15](ra2a1-elc_8h.md#a65b92e543dfb43c213274652ae60314a)#define RA\_ELC\_EVENT\_ICU\_IRQ3 0x004

[ 16](ra2a1-elc_8h.md#a2b1930fc54010b7c4c00f286f690cb1e)#define RA\_ELC\_EVENT\_ICU\_IRQ4 0x005

[ 17](ra2a1-elc_8h.md#af3ecccfe646b6cac991310abe3e4b955)#define RA\_ELC\_EVENT\_ICU\_IRQ5 0x006

[ 18](ra2a1-elc_8h.md#a98b53eb7b5979403023805ba925c504c)#define RA\_ELC\_EVENT\_ICU\_IRQ6 0x007

[ 19](ra2a1-elc_8h.md#ab6f05849ddc30ceb693f57b522223bcf)#define RA\_ELC\_EVENT\_ICU\_IRQ7 0x008

[ 20](ra2a1-elc_8h.md#a9a58e3a2c10447906aaf35bab5664d24)#define RA\_ELC\_EVENT\_DTC\_COMPLETE 0x009

[ 21](ra2a1-elc_8h.md#a5ab484cdaf470b47e95005d83d60394f)#define RA\_ELC\_EVENT\_DTC\_END 0x00A

[ 22](ra2a1-elc_8h.md#a26e0aaa4a17196ada130bbb714a6d3bd)#define RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL 0x00B

[ 23](ra2a1-elc_8h.md#a535af54c8bcfff47cc90ba1226044d71)#define RA\_ELC\_EVENT\_FCU\_FRDYI 0x00C

[ 24](ra2a1-elc_8h.md#a7ab275777147d06315a04abb3f2f6d51)#define RA\_ELC\_EVENT\_LVD\_LVD1 0x00D

[ 25](ra2a1-elc_8h.md#ad52acadba107b7f907d678f44769a4cb)#define RA\_ELC\_EVENT\_LVD\_LVD2 0x00E

[ 26](ra2a1-elc_8h.md#a290decf4254396cbce267cb52a619717)#define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP 0x00F

[ 27](ra2a1-elc_8h.md#ac6953f0c8caa6b5ef8c9893c7ff4baa1)#define RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST 0x010

[ 28](ra2a1-elc_8h.md#a4c3604a42ead1d43f472e901087ec148)#define RA\_ELC\_EVENT\_AGT0\_INT 0x011

[ 29](ra2a1-elc_8h.md#a015e6f8aed4b467f4554e6887b4d9ec9)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A 0x012

[ 30](ra2a1-elc_8h.md#ada1ad302dc5b987a6f7c972afae729f2)#define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B 0x013

[ 31](ra2a1-elc_8h.md#a635180e38c932579072f4eebd665592f)#define RA\_ELC\_EVENT\_AGT1\_INT 0x014

[ 32](ra2a1-elc_8h.md#aeb2399818b6b141ab4a37e257dba22be)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A 0x015

[ 33](ra2a1-elc_8h.md#a1d660c78348b48ea7a072225491ae44b)#define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B 0x016

[ 34](ra2a1-elc_8h.md#abc837f1fcfffeb2ec231c79336379dda)#define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW 0x017

[ 35](ra2a1-elc_8h.md#a6cdb7a60a850f9ec23f19c548a6cc544)#define RA\_ELC\_EVENT\_WDT\_UNDERFLOW 0x018

[ 36](ra2a1-elc_8h.md#a76fd68b555574159d563d2dfd68d90b9)#define RA\_ELC\_EVENT\_RTC\_ALARM 0x019

[ 37](ra2a1-elc_8h.md#a144901ee7b31b96eba18a39d98c4b953)#define RA\_ELC\_EVENT\_RTC\_PERIOD 0x01A

[ 38](ra2a1-elc_8h.md#a241cd3c65033b46a1160d5815cc86fd7)#define RA\_ELC\_EVENT\_RTC\_CARRY 0x01B

[ 39](ra2a1-elc_8h.md#ad7284976213551f7d4fa450bf2bf8c7c)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END 0x01C

[ 40](ra2a1-elc_8h.md#aecbe4efa29972b832e35ebb00d7499ad)#define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B 0x01D

[ 41](ra2a1-elc_8h.md#aa4feb2c3e29ba84d1397c618b7b860bf)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A 0x01E

[ 42](ra2a1-elc_8h.md#ab59c8ec4f20de5cf4709efe0a7ee70a1)#define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B 0x01F

[ 43](ra2a1-elc_8h.md#af187c78a1f05fc4be81aa3af36e4cde5)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH 0x020

[ 44](ra2a1-elc_8h.md#a65d6c499a6852434b4802f8ef7066eb4)#define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH 0x021

[ 45](ra2a1-elc_8h.md#a3bbee94907736c0c435cc5ff64d1e7ef)#define RA\_ELC\_EVENT\_ACMPHS0\_INT 0x022

[ 46](ra2a1-elc_8h.md#a46ba8b903950b3ff8b04c8176e7844b5)#define RA\_ELC\_EVENT\_ACMPLP0\_INT 0x023

[ 47](ra2a1-elc_8h.md#a377a3e92bcdf0e45d2b12223ddd85666)#define RA\_ELC\_EVENT\_ACMPLP1\_INT 0x024

[ 48](ra2a1-elc_8h.md#aac8d97813e8a3276bdac764faf7b580d)#define RA\_ELC\_EVENT\_USBFS\_INT 0x025

[ 49](ra2a1-elc_8h.md#a9458dbf2b1da6fc51ca2c2933dcb6b37)#define RA\_ELC\_EVENT\_USBFS\_RESUME 0x026

[ 50](ra2a1-elc_8h.md#a7271a25cdc3c987313efbafcd2a746cf)#define RA\_ELC\_EVENT\_IIC0\_RXI 0x027

[ 51](ra2a1-elc_8h.md#a7843f8a23feb383202fa6ad3be8fae5c)#define RA\_ELC\_EVENT\_IIC0\_TXI 0x028

[ 52](ra2a1-elc_8h.md#a52270344b26073c127a0269c5ec4e228)#define RA\_ELC\_EVENT\_IIC0\_TEI 0x029

[ 53](ra2a1-elc_8h.md#a667eb763b55f973b141837e82dbbae6e)#define RA\_ELC\_EVENT\_IIC0\_ERI 0x02A

[ 54](ra2a1-elc_8h.md#a2a074dab614a1639ea5fa4f6d3baffd3)#define RA\_ELC\_EVENT\_IIC0\_WUI 0x02B

[ 55](ra2a1-elc_8h.md#ad03e6b81d0e7ce53737e5c3022f8d951)#define RA\_ELC\_EVENT\_IIC1\_RXI 0x02C

[ 56](ra2a1-elc_8h.md#a641c91157c98f41d3cf5ff6bbe25192d)#define RA\_ELC\_EVENT\_IIC1\_TXI 0x02D

[ 57](ra2a1-elc_8h.md#a45ed226ccaace8813aa653276a52999d)#define RA\_ELC\_EVENT\_IIC1\_TEI 0x02E

[ 58](ra2a1-elc_8h.md#a2221a129f0e323fa5b96bfe5ed0e007f)#define RA\_ELC\_EVENT\_IIC1\_ERI 0x02F

[ 59](ra2a1-elc_8h.md#a2faf033bad7b355f8beb9386a2d0e93b)#define RA\_ELC\_EVENT\_CTSU\_WRITE 0x030

[ 60](ra2a1-elc_8h.md#ad7cd21f5db3e117b87ffab8a6cb47272)#define RA\_ELC\_EVENT\_CTSU\_READ 0x031

[ 61](ra2a1-elc_8h.md#acfe8138822bcd3f02fe50316e40c7641)#define RA\_ELC\_EVENT\_CTSU\_END 0x032

[ 62](ra2a1-elc_8h.md#a4412a0ec84a10d14d131754c5f9eb509)#define RA\_ELC\_EVENT\_KEY\_INT 0x033

[ 63](ra2a1-elc_8h.md#ab6c210d6481294137fd4bc32c39e5de1)#define RA\_ELC\_EVENT\_DOC\_INT 0x034

[ 64](ra2a1-elc_8h.md#a6ec3edb5e4de5bca1171ade1aa9ca19f)#define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR 0x035

[ 65](ra2a1-elc_8h.md#a1390ee9467a9d093de1532f0703ec35f)#define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END 0x036

[ 66](ra2a1-elc_8h.md#a3463c1e202ab7891521eda7196e1be80)#define RA\_ELC\_EVENT\_CAC\_OVERFLOW 0x037

[ 67](ra2a1-elc_8h.md#aa4f3b915e26ee83dcc8c383a1fdb2425)#define RA\_ELC\_EVENT\_CAN0\_ERROR 0x038

[ 68](ra2a1-elc_8h.md#ad6e2ac69f8d10baa2d023e680e2f4c2f)#define RA\_ELC\_EVENT\_CAN0\_FIFO\_RX 0x039

[ 69](ra2a1-elc_8h.md#a52d0f15f6d388658ae060aec6302b448)#define RA\_ELC\_EVENT\_CAN0\_FIFO\_TX 0x03A

[ 70](ra2a1-elc_8h.md#a0b017dad5f8642aa70f6f96c45e84a72)#define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX 0x03B

[ 71](ra2a1-elc_8h.md#a71880c5fc6363d67d8d126fd63a5354c)#define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX 0x03C

[ 72](ra2a1-elc_8h.md#aee58e9a0c4313f0ec08f0652e5002008)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1 0x03D

[ 73](ra2a1-elc_8h.md#a36d858520d28847eead0fbfe7950be2d)#define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2 0x03E

[ 74](ra2a1-elc_8h.md#ae5c28618f4e68eef6ca83bdcec515abb)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0 0x03F

[ 75](ra2a1-elc_8h.md#a9f0b82bfff5ea2ba414ac0bccad9a34d)#define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1 0x040

[ 76](ra2a1-elc_8h.md#a81e18423a1f61e34f0daab6f7367eae2)#define RA\_ELC\_EVENT\_POEG0\_EVENT 0x041

[ 77](ra2a1-elc_8h.md#a2a43c2ce461fde766e66a4451929a875)#define RA\_ELC\_EVENT\_POEG1\_EVENT 0x042

[ 78](ra2a1-elc_8h.md#a92d5ee3e173bb0f1afab3fcdd4025f6e)#define RA\_ELC\_EVENT\_SDADC0\_ADI 0x043

[ 79](ra2a1-elc_8h.md#a44a06fc58b788d583842b224964b0588)#define RA\_ELC\_EVENT\_SDADC0\_SCANEND 0x044

[ 80](ra2a1-elc_8h.md#a46dbbc685c6f359db23c1f75ddcda0aa)#define RA\_ELC\_EVENT\_SDADC0\_CALIEND 0x045

[ 81](ra2a1-elc_8h.md#aec8a8b590cc124ca12425f34b5a61020)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A 0x046

[ 82](ra2a1-elc_8h.md#ae1ed91479f405ac965da868e86bce533)#define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B 0x047

[ 83](ra2a1-elc_8h.md#a6d7c9090c21a8a0c497356050d649ec6)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_C 0x048

[ 84](ra2a1-elc_8h.md#af5b8ca097747bd987e81d8d81263aa81)#define RA\_ELC\_EVENT\_GPT0\_COMPARE\_D 0x049

[ 85](ra2a1-elc_8h.md#a76692948000993fde4d286f1a521a6d2)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW 0x04A

[ 86](ra2a1-elc_8h.md#a9edde37b8c0835978aa55d58d77c5ad5)#define RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW 0x04B

[ 87](ra2a1-elc_8h.md#a33a428565bfa3237aa4eda10b982fc65)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A 0x04C

[ 88](ra2a1-elc_8h.md#a5326aaf270290b524f8cb2e126d06602)#define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B 0x04D

[ 89](ra2a1-elc_8h.md#a2e55bae34ab30f2d802b8eaf93dd3cfd)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C 0x04E

[ 90](ra2a1-elc_8h.md#ada3870f40beeec10e9366e908ed980d0)#define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D 0x04F

[ 91](ra2a1-elc_8h.md#aa6eac7cf283073eea62fbaa1df2017f2)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW 0x050

[ 92](ra2a1-elc_8h.md#ae8cefd5f23897d43cffba4e91b7c8b5c)#define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW 0x051

[ 93](ra2a1-elc_8h.md#ad1a5796e0c70a988165765f2ce8c1e80)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A 0x052

[ 94](ra2a1-elc_8h.md#a73776ba7d66a478c92c6cb3dfed50af4)#define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B 0x053

[ 95](ra2a1-elc_8h.md#aa391fa888ded57351c9b62f54df1ce36)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C 0x054

[ 96](ra2a1-elc_8h.md#a90c7aa7bbddb04e6ae4b6eccb64a0e93)#define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D 0x055

[ 97](ra2a1-elc_8h.md#aede7879166ef812139641122782d873b)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW 0x056

[ 98](ra2a1-elc_8h.md#ad71d20ad5434f219a61e0f0aded090d1)#define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW 0x057

[ 99](ra2a1-elc_8h.md#a74526500dfb573fe21fbca739b1698e1)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A 0x058

[ 100](ra2a1-elc_8h.md#ac6cfac3496e4ab71c9bf84b43e06486a)#define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B 0x059

[ 101](ra2a1-elc_8h.md#a1af4840d468eb4c4e1672a34652ef583)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_C 0x05A

[ 102](ra2a1-elc_8h.md#a263e6b02601dd37d6eedaab56a2e6fcd)#define RA\_ELC\_EVENT\_GPT3\_COMPARE\_D 0x05B

[ 103](ra2a1-elc_8h.md#a546eff128c44a29f56fe90952cef475d)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW 0x05C

[ 104](ra2a1-elc_8h.md#ab30a5683e48535abbf0c400a5a0d8946)#define RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW 0x05D

[ 105](ra2a1-elc_8h.md#a8130aa176d9d5dd698c62708111515e0)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A 0x05E

[ 106](ra2a1-elc_8h.md#aa77a30a219070d15e358a43fbbd89728)#define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B 0x05F

[ 107](ra2a1-elc_8h.md#af6c1cb172b343baa8d8bbe01d1674922)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C 0x060

[ 108](ra2a1-elc_8h.md#ae8c7945c641045c615922a3f82329c56)#define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D 0x061

[ 109](ra2a1-elc_8h.md#abb820eb80ad8afc5c12dc3581fc7a0b9)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW 0x062

[ 110](ra2a1-elc_8h.md#a65831ae6b037607dc55a2b1e8aa296a7)#define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW 0x063

[ 111](ra2a1-elc_8h.md#adc4aceff99f296b06938254f9dcc1f2f)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A 0x064

[ 112](ra2a1-elc_8h.md#aad1fc8b32dffaaa64f9908951f8b1c64)#define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B 0x065

[ 113](ra2a1-elc_8h.md#aebaa50f4643efe5b87798777cee578bc)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C 0x066

[ 114](ra2a1-elc_8h.md#a21965e21bd4045aa5010925620b4d827)#define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D 0x067

[ 115](ra2a1-elc_8h.md#a038e7580f03fbdd74f417108cd2a8b4d)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW 0x068

[ 116](ra2a1-elc_8h.md#ac38b8f1154d6a699923b2bbf249e38fd)#define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW 0x069

[ 117](ra2a1-elc_8h.md#acad1c37929903ddee569f40a3c5c59e3)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A 0x06A

[ 118](ra2a1-elc_8h.md#aa0fc9b447efbcba0bb6800f785daeb96)#define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B 0x06B

[ 119](ra2a1-elc_8h.md#a01f586bd98832ea9b8aa58741b61a319)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_C 0x06C

[ 120](ra2a1-elc_8h.md#acd71c3b8e8e1d96aa3ff6affb93f5000)#define RA\_ELC\_EVENT\_GPT6\_COMPARE\_D 0x06D

[ 121](ra2a1-elc_8h.md#ac3c8dd6a5b7f95dccc58e7ec4e235a40)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW 0x06E

[ 122](ra2a1-elc_8h.md#acdece33585a75fccba962e4f764058fb)#define RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW 0x06F

[ 123](ra2a1-elc_8h.md#a8438d8d92e1950681388b40385a2c354)#define RA\_ELC\_EVENT\_OPS\_UVW\_EDGE 0x070

[ 124](ra2a1-elc_8h.md#ad9e9a8451a683c5b5bc8a2ace8264c27)#define RA\_ELC\_EVENT\_SCI0\_RXI 0x071

[ 125](ra2a1-elc_8h.md#aecc4fdda2a7eeb2bab0b894f2e5047d9)#define RA\_ELC\_EVENT\_SCI0\_TXI 0x072

[ 126](ra2a1-elc_8h.md#ae845a850ab730c651badc5c857e28ee9)#define RA\_ELC\_EVENT\_SCI0\_TEI 0x073

[ 127](ra2a1-elc_8h.md#ad4580e769bae423298276e31ee2ee071)#define RA\_ELC\_EVENT\_SCI0\_ERI 0x074

[ 128](ra2a1-elc_8h.md#ae2373b571584dae4d1c7fc57142ecb3c)#define RA\_ELC\_EVENT\_SCI0\_AM 0x075

[ 129](ra2a1-elc_8h.md#ad52a4c7660a4e609976f7045305f8ca7)#define RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI 0x076

[ 130](ra2a1-elc_8h.md#ae936e9aa971a376cb4ea3405c68d57f0)#define RA\_ELC\_EVENT\_SCI1\_RXI 0x077

[ 131](ra2a1-elc_8h.md#abd1c6187f97f2817dc5eb59278a996b1)#define RA\_ELC\_EVENT\_SCI1\_TXI 0x078

[ 132](ra2a1-elc_8h.md#aae0ca4a1031af4c490fbb1ecbe201662)#define RA\_ELC\_EVENT\_SCI1\_TEI 0x079

[ 133](ra2a1-elc_8h.md#a6a673466eb5261d23ee06be132ca9cde)#define RA\_ELC\_EVENT\_SCI1\_ERI 0x07A

[ 134](ra2a1-elc_8h.md#ad9ca7dbcac36bb7f921cd8b8db761623)#define RA\_ELC\_EVENT\_SCI1\_AM 0x07B

[ 135](ra2a1-elc_8h.md#ac01e51a9360f409e430642d86818bf98)#define RA\_ELC\_EVENT\_SCI9\_RXI 0x07C

[ 136](ra2a1-elc_8h.md#a8c628c59b08ed53781fd406ea22da796)#define RA\_ELC\_EVENT\_SCI9\_TXI 0x07D

[ 137](ra2a1-elc_8h.md#ac3a064375ff90f3a6a35c5fdda680f95)#define RA\_ELC\_EVENT\_SCI9\_TEI 0x07E

[ 138](ra2a1-elc_8h.md#af2e4d2d6b59c512e536d901789b3c1a2)#define RA\_ELC\_EVENT\_SCI9\_ERI 0x07F

[ 139](ra2a1-elc_8h.md#a2bfc7def09c933262aa530227a45af7d)#define RA\_ELC\_EVENT\_SCI9\_AM 0x080

[ 140](ra2a1-elc_8h.md#af77608914a79bea7797b63674c71db31)#define RA\_ELC\_EVENT\_SPI0\_RXI 0x081

[ 141](ra2a1-elc_8h.md#a82d87016b5d694884bba33bf71e93e92)#define RA\_ELC\_EVENT\_SPI0\_TXI 0x082

[ 142](ra2a1-elc_8h.md#a920575ee3a202b0d7202cd053f1e235b)#define RA\_ELC\_EVENT\_SPI0\_IDLE 0x083

[ 143](ra2a1-elc_8h.md#ab588fafc974153bcf94087cdb1a71d73)#define RA\_ELC\_EVENT\_SPI0\_ERI 0x084

[ 144](ra2a1-elc_8h.md#a368a0ece3d89efe3ed8ab274471849b9)#define RA\_ELC\_EVENT\_SPI0\_TEI 0x085

[ 145](ra2a1-elc_8h.md#a2f5e3b5957e42c572fda94ec535b401b)#define RA\_ELC\_EVENT\_SPI1\_RXI 0x086

[ 146](ra2a1-elc_8h.md#a0aab8e60c14b34bccb74400a818524ac)#define RA\_ELC\_EVENT\_SPI1\_TXI 0x087

[ 147](ra2a1-elc_8h.md#a73da76e435d9de6b6b7ad48190d2c0a2)#define RA\_ELC\_EVENT\_SPI1\_IDLE 0x088

[ 148](ra2a1-elc_8h.md#aedf36efaaba39c4001386536d21f81e2)#define RA\_ELC\_EVENT\_SPI1\_ERI 0x089

[ 149](ra2a1-elc_8h.md#a60f40983e3c6344a257bd157b40069d5)#define RA\_ELC\_EVENT\_SPI1\_TEI 0x08A

[ 150](ra2a1-elc_8h.md#a27de8dfad25ac5ec920f295512814cfd)#define RA\_ELC\_EVENT\_AES\_WRREQ 0x08B

[ 151](ra2a1-elc_8h.md#aaaca0ada65165878e42c0cb9d5748ffb)#define RA\_ELC\_EVENT\_AES\_RDREQ 0x08C

[ 152](ra2a1-elc_8h.md#aa2fe16c7e0528b58f2d9f0e9e9053899)#define RA\_ELC\_EVENT\_TRNG\_RDREQ 0x08D

153

154/\* Possible peripherals to be linked to event signals \*/

[ 155](ra2a1-elc_8h.md#ad6bb2d32abfad10bd283894efb7fe968)#define RA\_ELC\_PERIPHERAL\_GPT\_A 0

[ 156](ra2a1-elc_8h.md#a8c4b99abfaa798b3b15f3435a73bad86)#define RA\_ELC\_PERIPHERAL\_GPT\_B 1

[ 157](ra2a1-elc_8h.md#af0000625eec82c9f4ebe20da1cec7c66)#define RA\_ELC\_PERIPHERAL\_GPT\_C 2

[ 158](ra2a1-elc_8h.md#ae9ae748233cce2fa65b334c2f8b2a6f7)#define RA\_ELC\_PERIPHERAL\_GPT\_D 3

[ 159](ra2a1-elc_8h.md#a2b5a9232a4ad9d199dc9baa510d0ed54)#define RA\_ELC\_PERIPHERAL\_ADC0 8

[ 160](ra2a1-elc_8h.md#afaf4059726139d62e2c09010cfa1148a)#define RA\_ELC\_PERIPHERAL\_ADC0\_B 9

[ 161](ra2a1-elc_8h.md#a9a32ba5817467743fbcf24b698124b02)#define RA\_ELC\_PERIPHERAL\_DAC0 12

[ 162](ra2a1-elc_8h.md#a5830e830b7b10cd68441de2648edd6a0)#define RA\_ELC\_PERIPHERAL\_IOPORT1 14

[ 163](ra2a1-elc_8h.md#a42d4feb2c854cc1964455297e6d7eb72)#define RA\_ELC\_PERIPHERAL\_IOPORT2 15

[ 164](ra2a1-elc_8h.md#a66a60a7a3469054498a247253cea97c0)#define RA\_ELC\_PERIPHERAL\_CTSU 18

[ 165](ra2a1-elc_8h.md#aee5b5d61d758c6481cad151c6de784b0)#define RA\_ELC\_PERIPHERAL\_DA8\_0 19

[ 166](ra2a1-elc_8h.md#a8d267a5a8a56e0f79b74bc1f145d5f52)#define RA\_ELC\_PERIPHERAL\_DA8\_1 20

[ 167](ra2a1-elc_8h.md#ae36d99e765f1bd11ff42c37ec75d6f6a)#define RA\_ELC\_PERIPHERAL\_SDADC0 22

168

169#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MISC\_RENESAS\_RA\_ELC\_RA2A1\_ELC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [misc](dir_b5927901ba0eeb0fdf9ca7870f5af60a.md)
- [renesas](dir_86b946318bd38151d049d676c19e4b11.md)
- [ra-elc](dir_fc824a581c07e3e227952b4fed9afa76.md)
- [ra2a1-elc.h](ra2a1-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
