---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra4e1-elc_8h.html
original_path: doxygen/html/ra4e1-elc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra4e1-elc.h File Reference

[Go to the source code of this file.](ra4e1-elc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RA\_ELC\_EVENT\_NONE](#a11b5cec97472328120a8d6381f1e8809)   0x0 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ0](#a04ee26d7188b7441627bb89249545cfa)   0x001 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ1](#ac9f6681c03b50d8b3a24798b3e790170)   0x002 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ2](#a136f93a17eea3f4233b0012c075fc904)   0x003 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ3](#a65b92e543dfb43c213274652ae60314a)   0x004 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ4](#a2b1930fc54010b7c4c00f286f690cb1e)   0x005 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ5](#af3ecccfe646b6cac991310abe3e4b955)   0x006 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ6](#a98b53eb7b5979403023805ba925c504c)   0x007 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ7](#ab6f05849ddc30ceb693f57b522223bcf)   0x008 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ8](#acbcd1c55530c6cb8580b76bd55c73c90)   0x009 |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ9](#af04ed29327af6c108875334c24d98e43)   0x00A |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ13](#ad7435ed602899357eae0f46c09bf542c)   0x00E |
| #define | [RA\_ELC\_EVENT\_DMAC0\_INT](#a906929a9ae7dd7de44d21a32d3635080)   0x020 |
| #define | [RA\_ELC\_EVENT\_DMAC1\_INT](#a76b9d9fa8af16a1480fcc8d8ec12572f)   0x021 |
| #define | [RA\_ELC\_EVENT\_DMAC2\_INT](#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)   0x022 |
| #define | [RA\_ELC\_EVENT\_DMAC3\_INT](#a0b9d72a41fd7c5b27e6c31967645b907)   0x023 |
| #define | [RA\_ELC\_EVENT\_DMAC4\_INT](#a4cae5afbbe49719555bbbfa12b8727f5)   0x024 |
| #define | [RA\_ELC\_EVENT\_DMAC5\_INT](#a000e31aba8a821f4358a435d280b3a7b)   0x025 |
| #define | [RA\_ELC\_EVENT\_DMAC6\_INT](#a2d1f6d1c797a0d787a5d5c08b0fc18ad)   0x026 |
| #define | [RA\_ELC\_EVENT\_DMAC7\_INT](#ae8caef45a510d4c4f1c55f923e01799e)   0x027 |
| #define | [RA\_ELC\_EVENT\_DTC\_COMPLETE](#a9a58e3a2c10447906aaf35bab5664d24)   0x029 |
| #define | [RA\_ELC\_EVENT\_DTC\_END](#a5ab484cdaf470b47e95005d83d60394f)   0x02A |
| #define | [RA\_ELC\_EVENT\_DMA\_TRANSERR](#a54d8c74eefe8f9b237ea23e18033d947)   0x02B |
| #define | [RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL](#a26e0aaa4a17196ada130bbb714a6d3bd)   0x02D |
| #define | [RA\_ELC\_EVENT\_FCU\_FIFERR](#a5c7545a2f69856b7b637ad690f158b77)   0x030 |
| #define | [RA\_ELC\_EVENT\_FCU\_FRDYI](#a535af54c8bcfff47cc90ba1226044d71)   0x031 |
| #define | [RA\_ELC\_EVENT\_LVD\_LVD1](#a7ab275777147d06315a04abb3f2f6d51)   0x038 |
| #define | [RA\_ELC\_EVENT\_LVD\_LVD2](#ad52acadba107b7f907d678f44769a4cb)   0x039 |
| #define | [RA\_ELC\_EVENT\_CGC\_MOSC\_STOP](#a290decf4254396cbce267cb52a619717)   0x03B |
| #define | [RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST](#ac6953f0c8caa6b5ef8c9893c7ff4baa1)   0x03C |
| #define | [RA\_ELC\_EVENT\_AGT0\_INT](#a4c3604a42ead1d43f472e901087ec148)   0x040 |
| #define | [RA\_ELC\_EVENT\_AGT0\_COMPARE\_A](#a015e6f8aed4b467f4554e6887b4d9ec9)   0x041 |
| #define | [RA\_ELC\_EVENT\_AGT0\_COMPARE\_B](#ada1ad302dc5b987a6f7c972afae729f2)   0x042 |
| #define | [RA\_ELC\_EVENT\_AGT1\_INT](#a635180e38c932579072f4eebd665592f)   0x043 |
| #define | [RA\_ELC\_EVENT\_AGT1\_COMPARE\_A](#aeb2399818b6b141ab4a37e257dba22be)   0x044 |
| #define | [RA\_ELC\_EVENT\_AGT1\_COMPARE\_B](#a1d660c78348b48ea7a072225491ae44b)   0x045 |
| #define | [RA\_ELC\_EVENT\_AGT2\_INT](#aace60e1ca05855c0838298c51510943d)   0x046 |
| #define | [RA\_ELC\_EVENT\_AGT2\_COMPARE\_A](#ac7d2ceb7c70898f96e4ef1606b96191f)   0x047 |
| #define | [RA\_ELC\_EVENT\_AGT2\_COMPARE\_B](#afa53449537c7ad67c71f495848781b9d)   0x048 |
| #define | [RA\_ELC\_EVENT\_AGT3\_INT](#a4a1e74d4c1ab5f1b6039550e3b518089)   0x049 |
| #define | [RA\_ELC\_EVENT\_AGT3\_COMPARE\_A](#a4500621826d716e3050e8e5e88d68a16)   0x04A |
| #define | [RA\_ELC\_EVENT\_AGT3\_COMPARE\_B](#a93641e55a6c8db7ae55e3b83376d997d)   0x04B |
| #define | [RA\_ELC\_EVENT\_AGT5\_INT](#acbb0c43bed869c27a8a90e8cb8166bb4)   0x04F |
| #define | [RA\_ELC\_EVENT\_AGT5\_COMPARE\_A](#a7ab1f11da949fca8067e82cd437b142a)   0x050 |
| #define | [RA\_ELC\_EVENT\_AGT5\_COMPARE\_B](#a78b5abeca0f03176a19464f3c2d9508d)   0x051 |
| #define | [RA\_ELC\_EVENT\_IWDT\_UNDERFLOW](#abc837f1fcfffeb2ec231c79336379dda)   0x052 |
| #define | [RA\_ELC\_EVENT\_WDT\_UNDERFLOW](#a6cdb7a60a850f9ec23f19c548a6cc544)   0x053 |
| #define | [RA\_ELC\_EVENT\_RTC\_ALARM](#a76fd68b555574159d563d2dfd68d90b9)   0x054 |
| #define | [RA\_ELC\_EVENT\_RTC\_PERIOD](#a144901ee7b31b96eba18a39d98c4b953)   0x055 |
| #define | [RA\_ELC\_EVENT\_RTC\_CARRY](#a241cd3c65033b46a1160d5815cc86fd7)   0x056 |
| #define | [RA\_ELC\_EVENT\_USBFS\_FIFO\_0](#ae4dbb89c58220f72818cc9c28d97905b)   0x06B |
| #define | [RA\_ELC\_EVENT\_USBFS\_FIFO\_1](#a0ef2efa2ea339cad7598f11fe549cdd9)   0x06C |
| #define | [RA\_ELC\_EVENT\_USBFS\_INT](#aac8d97813e8a3276bdac764faf7b580d)   0x06D |
| #define | [RA\_ELC\_EVENT\_USBFS\_RESUME](#a9458dbf2b1da6fc51ca2c2933dcb6b37)   0x06E |
| #define | [RA\_ELC\_EVENT\_IIC0\_RXI](#a7271a25cdc3c987313efbafcd2a746cf)   0x073 |
| #define | [RA\_ELC\_EVENT\_IIC0\_TXI](#a7843f8a23feb383202fa6ad3be8fae5c)   0x074 |
| #define | [RA\_ELC\_EVENT\_IIC0\_TEI](#a52270344b26073c127a0269c5ec4e228)   0x075 |
| #define | [RA\_ELC\_EVENT\_IIC0\_ERI](#a667eb763b55f973b141837e82dbbae6e)   0x076 |
| #define | [RA\_ELC\_EVENT\_IIC0\_WUI](#a2a074dab614a1639ea5fa4f6d3baffd3)   0x077 |
| #define | [RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR](#a6ec3edb5e4de5bca1171ade1aa9ca19f)   0x09E |
| #define | [RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END](#a1390ee9467a9d093de1532f0703ec35f)   0x09F |
| #define | [RA\_ELC\_EVENT\_CAC\_OVERFLOW](#a3463c1e202ab7891521eda7196e1be80)   0x0A0 |
| #define | [RA\_ELC\_EVENT\_CAN0\_ERROR](#aa4f3b915e26ee83dcc8c383a1fdb2425)   0x0A1 |
| #define | [RA\_ELC\_EVENT\_CAN0\_FIFO\_RX](#ad6e2ac69f8d10baa2d023e680e2f4c2f)   0x0A2 |
| #define | [RA\_ELC\_EVENT\_CAN0\_FIFO\_TX](#a52d0f15f6d388658ae060aec6302b448)   0x0A3 |
| #define | [RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX](#a0b017dad5f8642aa70f6f96c45e84a72)   0x0A4 |
| #define | [RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX](#a71880c5fc6363d67d8d126fd63a5354c)   0x0A5 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_1](#aee58e9a0c4313f0ec08f0652e5002008)   0x0B1 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_2](#a36d858520d28847eead0fbfe7950be2d)   0x0B2 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_3](#a545dadce70bbcea1116cd13490fe2571)   0x0B3 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_4](#a4e478b84ef99ae71c102ad3d5c71089a)   0x0B4 |
| #define | [RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0](#ae5c28618f4e68eef6ca83bdcec515abb)   0x0B5 |
| #define | [RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1](#a9f0b82bfff5ea2ba414ac0bccad9a34d)   0x0B6 |
| #define | [RA\_ELC\_EVENT\_POEG0\_EVENT](#a81e18423a1f61e34f0daab6f7367eae2)   0x0B7 |
| #define | [RA\_ELC\_EVENT\_POEG1\_EVENT](#a2a43c2ce461fde766e66a4451929a875)   0x0B8 |
| #define | [RA\_ELC\_EVENT\_POEG2\_EVENT](#a7b5c16202b2491ba77319a180bcaa107)   0x0B9 |
| #define | [RA\_ELC\_EVENT\_POEG3\_EVENT](#ab39d06b130b93348c5fab589f1e0074e)   0x0BA |
| #define | [RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A](#a33a428565bfa3237aa4eda10b982fc65)   0x0C9 |
| #define | [RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B](#a5326aaf270290b524f8cb2e126d06602)   0x0CA |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_C](#a2e55bae34ab30f2d802b8eaf93dd3cfd)   0x0CB |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_D](#ada3870f40beeec10e9366e908ed980d0)   0x0CC |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_E](#a5d4f72e95b7bb76315b9ffa059730620)   0x0CD |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_F](#a548923b7385648e4f15fef4ecb315478)   0x0CE |
| #define | [RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW](#aa6eac7cf283073eea62fbaa1df2017f2)   0x0CF |
| #define | [RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW](#ae8cefd5f23897d43cffba4e91b7c8b5c)   0x0D0 |
| #define | [RA\_ELC\_EVENT\_GPT1\_PC](#aa0208084abba3e2601c8cf7bb42837fd)   0x0D1 |
| #define | [RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A](#ad1a5796e0c70a988165765f2ce8c1e80)   0x0D2 |
| #define | [RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B](#a73776ba7d66a478c92c6cb3dfed50af4)   0x0D3 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_C](#aa391fa888ded57351c9b62f54df1ce36)   0x0D4 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_D](#a90c7aa7bbddb04e6ae4b6eccb64a0e93)   0x0D5 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_E](#adbfb562e616a86a3e28f8c3f09553db9)   0x0D6 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_F](#a6f07945c82efae23754e34dc09bee884)   0x0D7 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW](#aede7879166ef812139641122782d873b)   0x0D8 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW](#ad71d20ad5434f219a61e0f0aded090d1)   0x0D9 |
| #define | [RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A](#a8130aa176d9d5dd698c62708111515e0)   0x0E4 |
| #define | [RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B](#aa77a30a219070d15e358a43fbbd89728)   0x0E5 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_C](#af6c1cb172b343baa8d8bbe01d1674922)   0x0E6 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_D](#ae8c7945c641045c615922a3f82329c56)   0x0E7 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_E](#afcb271a94d9b07b7b1a204f325b80d52)   0x0E8 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_F](#a906eb0e1ed2786ed2b14e4608489b2cc)   0x0E9 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW](#abb820eb80ad8afc5c12dc3581fc7a0b9)   0x0EA |
| #define | [RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW](#a65831ae6b037607dc55a2b1e8aa296a7)   0x0EB |
| #define | [RA\_ELC\_EVENT\_GPT4\_PC](#af3ae1988661f1d68bd7cd5e36fb387f6)   0x0EC |
| #define | [RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A](#adc4aceff99f296b06938254f9dcc1f2f)   0x0ED |
| #define | [RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B](#aad1fc8b32dffaaa64f9908951f8b1c64)   0x0EE |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_C](#aebaa50f4643efe5b87798777cee578bc)   0x0EF |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_D](#a21965e21bd4045aa5010925620b4d827)   0x0F0 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_E](#a51a7cb146f0efbb7bc9f7336031006a4)   0x0F1 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_F](#abbd0bd21af2bd1679d6d7bc36001b97d)   0x0F2 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW](#a038e7580f03fbdd74f417108cd2a8b4d)   0x0F3 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW](#ac38b8f1154d6a699923b2bbf249e38fd)   0x0F4 |
| #define | [RA\_ELC\_EVENT\_GPT5\_PC](#aa7e87dac91e6416a1b1a23ae5ee82b55)   0x0F5 |
| #define | [RA\_ELC\_EVENT\_ADC0\_SCAN\_END](#ad7284976213551f7d4fa450bf2bf8c7c)   0x160 |
| #define | [RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B](#aecbe4efa29972b832e35ebb00d7499ad)   0x161 |
| #define | [RA\_ELC\_EVENT\_ADC0\_WINDOW\_A](#aa4feb2c3e29ba84d1397c618b7b860bf)   0x162 |
| #define | [RA\_ELC\_EVENT\_ADC0\_WINDOW\_B](#ab59c8ec4f20de5cf4709efe0a7ee70a1)   0x163 |
| #define | [RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH](#af187c78a1f05fc4be81aa3af36e4cde5)   0x164 |
| #define | [RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH](#a65d6c499a6852434b4802f8ef7066eb4)   0x165 |
| #define | [RA\_ELC\_EVENT\_SCI0\_RXI](#ad9e9a8451a683c5b5bc8a2ace8264c27)   0x180 |
| #define | [RA\_ELC\_EVENT\_SCI0\_TXI](#aecc4fdda2a7eeb2bab0b894f2e5047d9)   0x181 |
| #define | [RA\_ELC\_EVENT\_SCI0\_TEI](#ae845a850ab730c651badc5c857e28ee9)   0x182 |
| #define | [RA\_ELC\_EVENT\_SCI0\_ERI](#ad4580e769bae423298276e31ee2ee071)   0x183 |
| #define | [RA\_ELC\_EVENT\_SCI0\_AM](#ae2373b571584dae4d1c7fc57142ecb3c)   0x184 |
| #define | [RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI](#ad52a4c7660a4e609976f7045305f8ca7)   0x185 |
| #define | [RA\_ELC\_EVENT\_SCI3\_RXI](#a87a1f07a2b420f9ce8d7ebcc1c505986)   0x192 |
| #define | [RA\_ELC\_EVENT\_SCI3\_TXI](#aee0548d7714ebd04748eadf9e9dbb97c)   0x193 |
| #define | [RA\_ELC\_EVENT\_SCI3\_TEI](#a6f9d20424191f026030159511647f913)   0x194 |
| #define | [RA\_ELC\_EVENT\_SCI3\_ERI](#ab7a6ad3ccc6279863a491a3787fd5c5e)   0x195 |
| #define | [RA\_ELC\_EVENT\_SCI3\_AM](#a075f80d14abaa63627574519b9ebf36b)   0x196 |
| #define | [RA\_ELC\_EVENT\_SCI4\_RXI](#afe86466482eb03b85da9feb17bdccfc0)   0x198 |
| #define | [RA\_ELC\_EVENT\_SCI4\_TXI](#a89f26e1bfd92cb7c9a2bad9acd80e553)   0x199 |
| #define | [RA\_ELC\_EVENT\_SCI4\_TEI](#a2554192500a5ac058fbd338d3018f6cc)   0x19A |
| #define | [RA\_ELC\_EVENT\_SCI4\_ERI](#ac6f2b3938cde7ba80faf523548dfa6c2)   0x19B |
| #define | [RA\_ELC\_EVENT\_SCI4\_AM](#abddf2cbec24fd59c9330b0328a21f82e)   0x19C |
| #define | [RA\_ELC\_EVENT\_SCI9\_RXI](#ac01e51a9360f409e430642d86818bf98)   0x1B6 |
| #define | [RA\_ELC\_EVENT\_SCI9\_TXI](#a8c628c59b08ed53781fd406ea22da796)   0x1B7 |
| #define | [RA\_ELC\_EVENT\_SCI9\_TEI](#ac3a064375ff90f3a6a35c5fdda680f95)   0x1B8 |
| #define | [RA\_ELC\_EVENT\_SCI9\_ERI](#af2e4d2d6b59c512e536d901789b3c1a2)   0x1B9 |
| #define | [RA\_ELC\_EVENT\_SCI9\_AM](#a2bfc7def09c933262aa530227a45af7d)   0x1BA |
| #define | [RA\_ELC\_EVENT\_SPI0\_RXI](#af77608914a79bea7797b63674c71db31)   0x1C4 |
| #define | [RA\_ELC\_EVENT\_SPI0\_TXI](#a82d87016b5d694884bba33bf71e93e92)   0x1C5 |
| #define | [RA\_ELC\_EVENT\_SPI0\_IDLE](#a920575ee3a202b0d7202cd053f1e235b)   0x1C6 |
| #define | [RA\_ELC\_EVENT\_SPI0\_ERI](#ab588fafc974153bcf94087cdb1a71d73)   0x1C7 |
| #define | [RA\_ELC\_EVENT\_SPI0\_TEI](#a368a0ece3d89efe3ed8ab274471849b9)   0x1C8 |
| #define | [RA\_ELC\_EVENT\_QSPI\_INT](#a344b216f0d5880b31e7c1a4e700c85a4)   0x1DA |
| #define | [RA\_ELC\_EVENT\_DOC\_INT](#ab6c210d6481294137fd4bc32c39e5de1)   0x1DB |
| #define | [RA\_ELC\_PERIPHERAL\_GPT\_A](#ad6bb2d32abfad10bd283894efb7fe968)   0 |
| #define | [RA\_ELC\_PERIPHERAL\_GPT\_B](#a8c4b99abfaa798b3b15f3435a73bad86)   1 |
| #define | [RA\_ELC\_PERIPHERAL\_GPT\_C](#af0000625eec82c9f4ebe20da1cec7c66)   2 |
| #define | [RA\_ELC\_PERIPHERAL\_GPT\_D](#ae9ae748233cce2fa65b334c2f8b2a6f7)   3 |
| #define | [RA\_ELC\_PERIPHERAL\_GPT\_E](#aefc3deade612ed7aa53abd397d20af3b)   4 |
| #define | [RA\_ELC\_PERIPHERAL\_GPT\_F](#a4bb2ffb785a17a225d5eb6e80f0040bf)   5 |
| #define | [RA\_ELC\_PERIPHERAL\_GPT\_G](#a2ccd7f6730384fb8550054ea2195a67a)   6 |
| #define | [RA\_ELC\_PERIPHERAL\_GPT\_H](#a6e737df13755e4e0039e98610aa31f3c)   7 |
| #define | [RA\_ELC\_PERIPHERAL\_ADC0](#a2b5a9232a4ad9d199dc9baa510d0ed54)   8 |
| #define | [RA\_ELC\_PERIPHERAL\_ADC0\_B](#afaf4059726139d62e2c09010cfa1148a)   9 |
| #define | [RA\_ELC\_PERIPHERAL\_DAC0](#a9a32ba5817467743fbcf24b698124b02)   12 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT1](#a5830e830b7b10cd68441de2648edd6a0)   14 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT2](#a42d4feb2c854cc1964455297e6d7eb72)   15 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT3](#a349933f20d7b6f768e49239724d0c5f7)   16 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT4](#a6d08d1db64f903fa2dacfc81568b004d)   17 |

## Macro Definition Documentation

## [◆ ](#af187c78a1f05fc4be81aa3af36e4cde5)RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH

| #define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH   0x164 |
| --- |

## [◆ ](#a65d6c499a6852434b4802f8ef7066eb4)RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH

| #define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH   0x165 |
| --- |

## [◆ ](#ad7284976213551f7d4fa450bf2bf8c7c)RA\_ELC\_EVENT\_ADC0\_SCAN\_END

| #define RA\_ELC\_EVENT\_ADC0\_SCAN\_END   0x160 |
| --- |

## [◆ ](#aecbe4efa29972b832e35ebb00d7499ad)RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B

| #define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B   0x161 |
| --- |

## [◆ ](#aa4feb2c3e29ba84d1397c618b7b860bf)RA\_ELC\_EVENT\_ADC0\_WINDOW\_A

| #define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A   0x162 |
| --- |

## [◆ ](#ab59c8ec4f20de5cf4709efe0a7ee70a1)RA\_ELC\_EVENT\_ADC0\_WINDOW\_B

| #define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B   0x163 |
| --- |

## [◆ ](#a015e6f8aed4b467f4554e6887b4d9ec9)RA\_ELC\_EVENT\_AGT0\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A   0x041 |
| --- |

## [◆ ](#ada1ad302dc5b987a6f7c972afae729f2)RA\_ELC\_EVENT\_AGT0\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B   0x042 |
| --- |

## [◆ ](#a4c3604a42ead1d43f472e901087ec148)RA\_ELC\_EVENT\_AGT0\_INT

| #define RA\_ELC\_EVENT\_AGT0\_INT   0x040 |
| --- |

## [◆ ](#aeb2399818b6b141ab4a37e257dba22be)RA\_ELC\_EVENT\_AGT1\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A   0x044 |
| --- |

## [◆ ](#a1d660c78348b48ea7a072225491ae44b)RA\_ELC\_EVENT\_AGT1\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B   0x045 |
| --- |

## [◆ ](#a635180e38c932579072f4eebd665592f)RA\_ELC\_EVENT\_AGT1\_INT

| #define RA\_ELC\_EVENT\_AGT1\_INT   0x043 |
| --- |

## [◆ ](#ac7d2ceb7c70898f96e4ef1606b96191f)RA\_ELC\_EVENT\_AGT2\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT2\_COMPARE\_A   0x047 |
| --- |

## [◆ ](#afa53449537c7ad67c71f495848781b9d)RA\_ELC\_EVENT\_AGT2\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT2\_COMPARE\_B   0x048 |
| --- |

## [◆ ](#aace60e1ca05855c0838298c51510943d)RA\_ELC\_EVENT\_AGT2\_INT

| #define RA\_ELC\_EVENT\_AGT2\_INT   0x046 |
| --- |

## [◆ ](#a4500621826d716e3050e8e5e88d68a16)RA\_ELC\_EVENT\_AGT3\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT3\_COMPARE\_A   0x04A |
| --- |

## [◆ ](#a93641e55a6c8db7ae55e3b83376d997d)RA\_ELC\_EVENT\_AGT3\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT3\_COMPARE\_B   0x04B |
| --- |

## [◆ ](#a4a1e74d4c1ab5f1b6039550e3b518089)RA\_ELC\_EVENT\_AGT3\_INT

| #define RA\_ELC\_EVENT\_AGT3\_INT   0x049 |
| --- |

## [◆ ](#a7ab1f11da949fca8067e82cd437b142a)RA\_ELC\_EVENT\_AGT5\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT5\_COMPARE\_A   0x050 |
| --- |

## [◆ ](#a78b5abeca0f03176a19464f3c2d9508d)RA\_ELC\_EVENT\_AGT5\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT5\_COMPARE\_B   0x051 |
| --- |

## [◆ ](#acbb0c43bed869c27a8a90e8cb8166bb4)RA\_ELC\_EVENT\_AGT5\_INT

| #define RA\_ELC\_EVENT\_AGT5\_INT   0x04F |
| --- |

## [◆ ](#a6ec3edb5e4de5bca1171ade1aa9ca19f)RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR

| #define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR   0x09E |
| --- |

## [◆ ](#a1390ee9467a9d093de1532f0703ec35f)RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END

| #define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END   0x09F |
| --- |

## [◆ ](#a3463c1e202ab7891521eda7196e1be80)RA\_ELC\_EVENT\_CAC\_OVERFLOW

| #define RA\_ELC\_EVENT\_CAC\_OVERFLOW   0x0A0 |
| --- |

## [◆ ](#aa4f3b915e26ee83dcc8c383a1fdb2425)RA\_ELC\_EVENT\_CAN0\_ERROR

| #define RA\_ELC\_EVENT\_CAN0\_ERROR   0x0A1 |
| --- |

## [◆ ](#ad6e2ac69f8d10baa2d023e680e2f4c2f)RA\_ELC\_EVENT\_CAN0\_FIFO\_RX

| #define RA\_ELC\_EVENT\_CAN0\_FIFO\_RX   0x0A2 |
| --- |

## [◆ ](#a52d0f15f6d388658ae060aec6302b448)RA\_ELC\_EVENT\_CAN0\_FIFO\_TX

| #define RA\_ELC\_EVENT\_CAN0\_FIFO\_TX   0x0A3 |
| --- |

## [◆ ](#a0b017dad5f8642aa70f6f96c45e84a72)RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX

| #define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX   0x0A4 |
| --- |

## [◆ ](#a71880c5fc6363d67d8d126fd63a5354c)RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX

| #define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX   0x0A5 |
| --- |

## [◆ ](#a290decf4254396cbce267cb52a619717)RA\_ELC\_EVENT\_CGC\_MOSC\_STOP

| #define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP   0x03B |
| --- |

## [◆ ](#a54d8c74eefe8f9b237ea23e18033d947)RA\_ELC\_EVENT\_DMA\_TRANSERR

| #define RA\_ELC\_EVENT\_DMA\_TRANSERR   0x02B |
| --- |

## [◆ ](#a906929a9ae7dd7de44d21a32d3635080)RA\_ELC\_EVENT\_DMAC0\_INT

| #define RA\_ELC\_EVENT\_DMAC0\_INT   0x020 |
| --- |

## [◆ ](#a76b9d9fa8af16a1480fcc8d8ec12572f)RA\_ELC\_EVENT\_DMAC1\_INT

| #define RA\_ELC\_EVENT\_DMAC1\_INT   0x021 |
| --- |

## [◆ ](#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)RA\_ELC\_EVENT\_DMAC2\_INT

| #define RA\_ELC\_EVENT\_DMAC2\_INT   0x022 |
| --- |

## [◆ ](#a0b9d72a41fd7c5b27e6c31967645b907)RA\_ELC\_EVENT\_DMAC3\_INT

| #define RA\_ELC\_EVENT\_DMAC3\_INT   0x023 |
| --- |

## [◆ ](#a4cae5afbbe49719555bbbfa12b8727f5)RA\_ELC\_EVENT\_DMAC4\_INT

| #define RA\_ELC\_EVENT\_DMAC4\_INT   0x024 |
| --- |

## [◆ ](#a000e31aba8a821f4358a435d280b3a7b)RA\_ELC\_EVENT\_DMAC5\_INT

| #define RA\_ELC\_EVENT\_DMAC5\_INT   0x025 |
| --- |

## [◆ ](#a2d1f6d1c797a0d787a5d5c08b0fc18ad)RA\_ELC\_EVENT\_DMAC6\_INT

| #define RA\_ELC\_EVENT\_DMAC6\_INT   0x026 |
| --- |

## [◆ ](#ae8caef45a510d4c4f1c55f923e01799e)RA\_ELC\_EVENT\_DMAC7\_INT

| #define RA\_ELC\_EVENT\_DMAC7\_INT   0x027 |
| --- |

## [◆ ](#ab6c210d6481294137fd4bc32c39e5de1)RA\_ELC\_EVENT\_DOC\_INT

| #define RA\_ELC\_EVENT\_DOC\_INT   0x1DB |
| --- |

## [◆ ](#a9a58e3a2c10447906aaf35bab5664d24)RA\_ELC\_EVENT\_DTC\_COMPLETE

| #define RA\_ELC\_EVENT\_DTC\_COMPLETE   0x029 |
| --- |

## [◆ ](#a5ab484cdaf470b47e95005d83d60394f)RA\_ELC\_EVENT\_DTC\_END

| #define RA\_ELC\_EVENT\_DTC\_END   0x02A |
| --- |

## [◆ ](#ae5c28618f4e68eef6ca83bdcec515abb)RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0

| #define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0   0x0B5 |
| --- |

## [◆ ](#a9f0b82bfff5ea2ba414ac0bccad9a34d)RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1

| #define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1   0x0B6 |
| --- |

## [◆ ](#a5c7545a2f69856b7b637ad690f158b77)RA\_ELC\_EVENT\_FCU\_FIFERR

| #define RA\_ELC\_EVENT\_FCU\_FIFERR   0x030 |
| --- |

## [◆ ](#a535af54c8bcfff47cc90ba1226044d71)RA\_ELC\_EVENT\_FCU\_FRDYI

| #define RA\_ELC\_EVENT\_FCU\_FRDYI   0x031 |
| --- |

## [◆ ](#a33a428565bfa3237aa4eda10b982fc65)RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A   0x0C9 |
| --- |

## [◆ ](#a5326aaf270290b524f8cb2e126d06602)RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B   0x0CA |
| --- |

## [◆ ](#a2e55bae34ab30f2d802b8eaf93dd3cfd)RA\_ELC\_EVENT\_GPT1\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C   0x0CB |
| --- |

## [◆ ](#ada3870f40beeec10e9366e908ed980d0)RA\_ELC\_EVENT\_GPT1\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D   0x0CC |
| --- |

## [◆ ](#a5d4f72e95b7bb76315b9ffa059730620)RA\_ELC\_EVENT\_GPT1\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E   0x0CD |
| --- |

## [◆ ](#a548923b7385648e4f15fef4ecb315478)RA\_ELC\_EVENT\_GPT1\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F   0x0CE |
| --- |

## [◆ ](#aa6eac7cf283073eea62fbaa1df2017f2)RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW   0x0CF |
| --- |

## [◆ ](#ae8cefd5f23897d43cffba4e91b7c8b5c)RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW   0x0D0 |
| --- |

## [◆ ](#aa0208084abba3e2601c8cf7bb42837fd)RA\_ELC\_EVENT\_GPT1\_PC

| #define RA\_ELC\_EVENT\_GPT1\_PC   0x0D1 |
| --- |

## [◆ ](#ad1a5796e0c70a988165765f2ce8c1e80)RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A   0x0D2 |
| --- |

## [◆ ](#a73776ba7d66a478c92c6cb3dfed50af4)RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B   0x0D3 |
| --- |

## [◆ ](#aa391fa888ded57351c9b62f54df1ce36)RA\_ELC\_EVENT\_GPT2\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C   0x0D4 |
| --- |

## [◆ ](#a90c7aa7bbddb04e6ae4b6eccb64a0e93)RA\_ELC\_EVENT\_GPT2\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D   0x0D5 |
| --- |

## [◆ ](#adbfb562e616a86a3e28f8c3f09553db9)RA\_ELC\_EVENT\_GPT2\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E   0x0D6 |
| --- |

## [◆ ](#a6f07945c82efae23754e34dc09bee884)RA\_ELC\_EVENT\_GPT2\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F   0x0D7 |
| --- |

## [◆ ](#aede7879166ef812139641122782d873b)RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW   0x0D8 |
| --- |

## [◆ ](#ad71d20ad5434f219a61e0f0aded090d1)RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW   0x0D9 |
| --- |

## [◆ ](#a8130aa176d9d5dd698c62708111515e0)RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A   0x0E4 |
| --- |

## [◆ ](#aa77a30a219070d15e358a43fbbd89728)RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B   0x0E5 |
| --- |

## [◆ ](#af6c1cb172b343baa8d8bbe01d1674922)RA\_ELC\_EVENT\_GPT4\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C   0x0E6 |
| --- |

## [◆ ](#ae8c7945c641045c615922a3f82329c56)RA\_ELC\_EVENT\_GPT4\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D   0x0E7 |
| --- |

## [◆ ](#afcb271a94d9b07b7b1a204f325b80d52)RA\_ELC\_EVENT\_GPT4\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E   0x0E8 |
| --- |

## [◆ ](#a906eb0e1ed2786ed2b14e4608489b2cc)RA\_ELC\_EVENT\_GPT4\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F   0x0E9 |
| --- |

## [◆ ](#abb820eb80ad8afc5c12dc3581fc7a0b9)RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW   0x0EA |
| --- |

## [◆ ](#a65831ae6b037607dc55a2b1e8aa296a7)RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW   0x0EB |
| --- |

## [◆ ](#af3ae1988661f1d68bd7cd5e36fb387f6)RA\_ELC\_EVENT\_GPT4\_PC

| #define RA\_ELC\_EVENT\_GPT4\_PC   0x0EC |
| --- |

## [◆ ](#adc4aceff99f296b06938254f9dcc1f2f)RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A   0x0ED |
| --- |

## [◆ ](#aad1fc8b32dffaaa64f9908951f8b1c64)RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B   0x0EE |
| --- |

## [◆ ](#aebaa50f4643efe5b87798777cee578bc)RA\_ELC\_EVENT\_GPT5\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C   0x0EF |
| --- |

## [◆ ](#a21965e21bd4045aa5010925620b4d827)RA\_ELC\_EVENT\_GPT5\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D   0x0F0 |
| --- |

## [◆ ](#a51a7cb146f0efbb7bc9f7336031006a4)RA\_ELC\_EVENT\_GPT5\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E   0x0F1 |
| --- |

## [◆ ](#abbd0bd21af2bd1679d6d7bc36001b97d)RA\_ELC\_EVENT\_GPT5\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F   0x0F2 |
| --- |

## [◆ ](#a038e7580f03fbdd74f417108cd2a8b4d)RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW   0x0F3 |
| --- |

## [◆ ](#ac38b8f1154d6a699923b2bbf249e38fd)RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW   0x0F4 |
| --- |

## [◆ ](#aa7e87dac91e6416a1b1a23ae5ee82b55)RA\_ELC\_EVENT\_GPT5\_PC

| #define RA\_ELC\_EVENT\_GPT5\_PC   0x0F5 |
| --- |

## [◆ ](#a04ee26d7188b7441627bb89249545cfa)RA\_ELC\_EVENT\_ICU\_IRQ0

| #define RA\_ELC\_EVENT\_ICU\_IRQ0   0x001 |
| --- |

## [◆ ](#ac9f6681c03b50d8b3a24798b3e790170)RA\_ELC\_EVENT\_ICU\_IRQ1

| #define RA\_ELC\_EVENT\_ICU\_IRQ1   0x002 |
| --- |

## [◆ ](#ad7435ed602899357eae0f46c09bf542c)RA\_ELC\_EVENT\_ICU\_IRQ13

| #define RA\_ELC\_EVENT\_ICU\_IRQ13   0x00E |
| --- |

## [◆ ](#a136f93a17eea3f4233b0012c075fc904)RA\_ELC\_EVENT\_ICU\_IRQ2

| #define RA\_ELC\_EVENT\_ICU\_IRQ2   0x003 |
| --- |

## [◆ ](#a65b92e543dfb43c213274652ae60314a)RA\_ELC\_EVENT\_ICU\_IRQ3

| #define RA\_ELC\_EVENT\_ICU\_IRQ3   0x004 |
| --- |

## [◆ ](#a2b1930fc54010b7c4c00f286f690cb1e)RA\_ELC\_EVENT\_ICU\_IRQ4

| #define RA\_ELC\_EVENT\_ICU\_IRQ4   0x005 |
| --- |

## [◆ ](#af3ecccfe646b6cac991310abe3e4b955)RA\_ELC\_EVENT\_ICU\_IRQ5

| #define RA\_ELC\_EVENT\_ICU\_IRQ5   0x006 |
| --- |

## [◆ ](#a98b53eb7b5979403023805ba925c504c)RA\_ELC\_EVENT\_ICU\_IRQ6

| #define RA\_ELC\_EVENT\_ICU\_IRQ6   0x007 |
| --- |

## [◆ ](#ab6f05849ddc30ceb693f57b522223bcf)RA\_ELC\_EVENT\_ICU\_IRQ7

| #define RA\_ELC\_EVENT\_ICU\_IRQ7   0x008 |
| --- |

## [◆ ](#acbcd1c55530c6cb8580b76bd55c73c90)RA\_ELC\_EVENT\_ICU\_IRQ8

| #define RA\_ELC\_EVENT\_ICU\_IRQ8   0x009 |
| --- |

## [◆ ](#af04ed29327af6c108875334c24d98e43)RA\_ELC\_EVENT\_ICU\_IRQ9

| #define RA\_ELC\_EVENT\_ICU\_IRQ9   0x00A |
| --- |

## [◆ ](#a26e0aaa4a17196ada130bbb714a6d3bd)RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL

| #define RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL   0x02D |
| --- |

## [◆ ](#a667eb763b55f973b141837e82dbbae6e)RA\_ELC\_EVENT\_IIC0\_ERI

| #define RA\_ELC\_EVENT\_IIC0\_ERI   0x076 |
| --- |

## [◆ ](#a7271a25cdc3c987313efbafcd2a746cf)RA\_ELC\_EVENT\_IIC0\_RXI

| #define RA\_ELC\_EVENT\_IIC0\_RXI   0x073 |
| --- |

## [◆ ](#a52270344b26073c127a0269c5ec4e228)RA\_ELC\_EVENT\_IIC0\_TEI

| #define RA\_ELC\_EVENT\_IIC0\_TEI   0x075 |
| --- |

## [◆ ](#a7843f8a23feb383202fa6ad3be8fae5c)RA\_ELC\_EVENT\_IIC0\_TXI

| #define RA\_ELC\_EVENT\_IIC0\_TXI   0x074 |
| --- |

## [◆ ](#a2a074dab614a1639ea5fa4f6d3baffd3)RA\_ELC\_EVENT\_IIC0\_WUI

| #define RA\_ELC\_EVENT\_IIC0\_WUI   0x077 |
| --- |

## [◆ ](#aee58e9a0c4313f0ec08f0652e5002008)RA\_ELC\_EVENT\_IOPORT\_EVENT\_1

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1   0x0B1 |
| --- |

## [◆ ](#a36d858520d28847eead0fbfe7950be2d)RA\_ELC\_EVENT\_IOPORT\_EVENT\_2

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2   0x0B2 |
| --- |

## [◆ ](#a545dadce70bbcea1116cd13490fe2571)RA\_ELC\_EVENT\_IOPORT\_EVENT\_3

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_3   0x0B3 |
| --- |

## [◆ ](#a4e478b84ef99ae71c102ad3d5c71089a)RA\_ELC\_EVENT\_IOPORT\_EVENT\_4

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_4   0x0B4 |
| --- |

## [◆ ](#abc837f1fcfffeb2ec231c79336379dda)RA\_ELC\_EVENT\_IWDT\_UNDERFLOW

| #define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW   0x052 |
| --- |

## [◆ ](#ac6953f0c8caa6b5ef8c9893c7ff4baa1)RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST

| #define RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST   0x03C |
| --- |

## [◆ ](#a7ab275777147d06315a04abb3f2f6d51)RA\_ELC\_EVENT\_LVD\_LVD1

| #define RA\_ELC\_EVENT\_LVD\_LVD1   0x038 |
| --- |

## [◆ ](#ad52acadba107b7f907d678f44769a4cb)RA\_ELC\_EVENT\_LVD\_LVD2

| #define RA\_ELC\_EVENT\_LVD\_LVD2   0x039 |
| --- |

## [◆ ](#a11b5cec97472328120a8d6381f1e8809)RA\_ELC\_EVENT\_NONE

| #define RA\_ELC\_EVENT\_NONE   0x0 |
| --- |

## [◆ ](#a81e18423a1f61e34f0daab6f7367eae2)RA\_ELC\_EVENT\_POEG0\_EVENT

| #define RA\_ELC\_EVENT\_POEG0\_EVENT   0x0B7 |
| --- |

## [◆ ](#a2a43c2ce461fde766e66a4451929a875)RA\_ELC\_EVENT\_POEG1\_EVENT

| #define RA\_ELC\_EVENT\_POEG1\_EVENT   0x0B8 |
| --- |

## [◆ ](#a7b5c16202b2491ba77319a180bcaa107)RA\_ELC\_EVENT\_POEG2\_EVENT

| #define RA\_ELC\_EVENT\_POEG2\_EVENT   0x0B9 |
| --- |

## [◆ ](#ab39d06b130b93348c5fab589f1e0074e)RA\_ELC\_EVENT\_POEG3\_EVENT

| #define RA\_ELC\_EVENT\_POEG3\_EVENT   0x0BA |
| --- |

## [◆ ](#a344b216f0d5880b31e7c1a4e700c85a4)RA\_ELC\_EVENT\_QSPI\_INT

| #define RA\_ELC\_EVENT\_QSPI\_INT   0x1DA |
| --- |

## [◆ ](#a76fd68b555574159d563d2dfd68d90b9)RA\_ELC\_EVENT\_RTC\_ALARM

| #define RA\_ELC\_EVENT\_RTC\_ALARM   0x054 |
| --- |

## [◆ ](#a241cd3c65033b46a1160d5815cc86fd7)RA\_ELC\_EVENT\_RTC\_CARRY

| #define RA\_ELC\_EVENT\_RTC\_CARRY   0x056 |
| --- |

## [◆ ](#a144901ee7b31b96eba18a39d98c4b953)RA\_ELC\_EVENT\_RTC\_PERIOD

| #define RA\_ELC\_EVENT\_RTC\_PERIOD   0x055 |
| --- |

## [◆ ](#ae2373b571584dae4d1c7fc57142ecb3c)RA\_ELC\_EVENT\_SCI0\_AM

| #define RA\_ELC\_EVENT\_SCI0\_AM   0x184 |
| --- |

## [◆ ](#ad4580e769bae423298276e31ee2ee071)RA\_ELC\_EVENT\_SCI0\_ERI

| #define RA\_ELC\_EVENT\_SCI0\_ERI   0x183 |
| --- |

## [◆ ](#ad9e9a8451a683c5b5bc8a2ace8264c27)RA\_ELC\_EVENT\_SCI0\_RXI

| #define RA\_ELC\_EVENT\_SCI0\_RXI   0x180 |
| --- |

## [◆ ](#ad52a4c7660a4e609976f7045305f8ca7)RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI

| #define RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI   0x185 |
| --- |

## [◆ ](#ae845a850ab730c651badc5c857e28ee9)RA\_ELC\_EVENT\_SCI0\_TEI

| #define RA\_ELC\_EVENT\_SCI0\_TEI   0x182 |
| --- |

## [◆ ](#aecc4fdda2a7eeb2bab0b894f2e5047d9)RA\_ELC\_EVENT\_SCI0\_TXI

| #define RA\_ELC\_EVENT\_SCI0\_TXI   0x181 |
| --- |

## [◆ ](#a075f80d14abaa63627574519b9ebf36b)RA\_ELC\_EVENT\_SCI3\_AM

| #define RA\_ELC\_EVENT\_SCI3\_AM   0x196 |
| --- |

## [◆ ](#ab7a6ad3ccc6279863a491a3787fd5c5e)RA\_ELC\_EVENT\_SCI3\_ERI

| #define RA\_ELC\_EVENT\_SCI3\_ERI   0x195 |
| --- |

## [◆ ](#a87a1f07a2b420f9ce8d7ebcc1c505986)RA\_ELC\_EVENT\_SCI3\_RXI

| #define RA\_ELC\_EVENT\_SCI3\_RXI   0x192 |
| --- |

## [◆ ](#a6f9d20424191f026030159511647f913)RA\_ELC\_EVENT\_SCI3\_TEI

| #define RA\_ELC\_EVENT\_SCI3\_TEI   0x194 |
| --- |

## [◆ ](#aee0548d7714ebd04748eadf9e9dbb97c)RA\_ELC\_EVENT\_SCI3\_TXI

| #define RA\_ELC\_EVENT\_SCI3\_TXI   0x193 |
| --- |

## [◆ ](#abddf2cbec24fd59c9330b0328a21f82e)RA\_ELC\_EVENT\_SCI4\_AM

| #define RA\_ELC\_EVENT\_SCI4\_AM   0x19C |
| --- |

## [◆ ](#ac6f2b3938cde7ba80faf523548dfa6c2)RA\_ELC\_EVENT\_SCI4\_ERI

| #define RA\_ELC\_EVENT\_SCI4\_ERI   0x19B |
| --- |

## [◆ ](#afe86466482eb03b85da9feb17bdccfc0)RA\_ELC\_EVENT\_SCI4\_RXI

| #define RA\_ELC\_EVENT\_SCI4\_RXI   0x198 |
| --- |

## [◆ ](#a2554192500a5ac058fbd338d3018f6cc)RA\_ELC\_EVENT\_SCI4\_TEI

| #define RA\_ELC\_EVENT\_SCI4\_TEI   0x19A |
| --- |

## [◆ ](#a89f26e1bfd92cb7c9a2bad9acd80e553)RA\_ELC\_EVENT\_SCI4\_TXI

| #define RA\_ELC\_EVENT\_SCI4\_TXI   0x199 |
| --- |

## [◆ ](#a2bfc7def09c933262aa530227a45af7d)RA\_ELC\_EVENT\_SCI9\_AM

| #define RA\_ELC\_EVENT\_SCI9\_AM   0x1BA |
| --- |

## [◆ ](#af2e4d2d6b59c512e536d901789b3c1a2)RA\_ELC\_EVENT\_SCI9\_ERI

| #define RA\_ELC\_EVENT\_SCI9\_ERI   0x1B9 |
| --- |

## [◆ ](#ac01e51a9360f409e430642d86818bf98)RA\_ELC\_EVENT\_SCI9\_RXI

| #define RA\_ELC\_EVENT\_SCI9\_RXI   0x1B6 |
| --- |

## [◆ ](#ac3a064375ff90f3a6a35c5fdda680f95)RA\_ELC\_EVENT\_SCI9\_TEI

| #define RA\_ELC\_EVENT\_SCI9\_TEI   0x1B8 |
| --- |

## [◆ ](#a8c628c59b08ed53781fd406ea22da796)RA\_ELC\_EVENT\_SCI9\_TXI

| #define RA\_ELC\_EVENT\_SCI9\_TXI   0x1B7 |
| --- |

## [◆ ](#ab588fafc974153bcf94087cdb1a71d73)RA\_ELC\_EVENT\_SPI0\_ERI

| #define RA\_ELC\_EVENT\_SPI0\_ERI   0x1C7 |
| --- |

## [◆ ](#a920575ee3a202b0d7202cd053f1e235b)RA\_ELC\_EVENT\_SPI0\_IDLE

| #define RA\_ELC\_EVENT\_SPI0\_IDLE   0x1C6 |
| --- |

## [◆ ](#af77608914a79bea7797b63674c71db31)RA\_ELC\_EVENT\_SPI0\_RXI

| #define RA\_ELC\_EVENT\_SPI0\_RXI   0x1C4 |
| --- |

## [◆ ](#a368a0ece3d89efe3ed8ab274471849b9)RA\_ELC\_EVENT\_SPI0\_TEI

| #define RA\_ELC\_EVENT\_SPI0\_TEI   0x1C8 |
| --- |

## [◆ ](#a82d87016b5d694884bba33bf71e93e92)RA\_ELC\_EVENT\_SPI0\_TXI

| #define RA\_ELC\_EVENT\_SPI0\_TXI   0x1C5 |
| --- |

## [◆ ](#ae4dbb89c58220f72818cc9c28d97905b)RA\_ELC\_EVENT\_USBFS\_FIFO\_0

| #define RA\_ELC\_EVENT\_USBFS\_FIFO\_0   0x06B |
| --- |

## [◆ ](#a0ef2efa2ea339cad7598f11fe549cdd9)RA\_ELC\_EVENT\_USBFS\_FIFO\_1

| #define RA\_ELC\_EVENT\_USBFS\_FIFO\_1   0x06C |
| --- |

## [◆ ](#aac8d97813e8a3276bdac764faf7b580d)RA\_ELC\_EVENT\_USBFS\_INT

| #define RA\_ELC\_EVENT\_USBFS\_INT   0x06D |
| --- |

## [◆ ](#a9458dbf2b1da6fc51ca2c2933dcb6b37)RA\_ELC\_EVENT\_USBFS\_RESUME

| #define RA\_ELC\_EVENT\_USBFS\_RESUME   0x06E |
| --- |

## [◆ ](#a6cdb7a60a850f9ec23f19c548a6cc544)RA\_ELC\_EVENT\_WDT\_UNDERFLOW

| #define RA\_ELC\_EVENT\_WDT\_UNDERFLOW   0x053 |
| --- |

## [◆ ](#a2b5a9232a4ad9d199dc9baa510d0ed54)RA\_ELC\_PERIPHERAL\_ADC0

| #define RA\_ELC\_PERIPHERAL\_ADC0   8 |
| --- |

## [◆ ](#afaf4059726139d62e2c09010cfa1148a)RA\_ELC\_PERIPHERAL\_ADC0\_B

| #define RA\_ELC\_PERIPHERAL\_ADC0\_B   9 |
| --- |

## [◆ ](#a9a32ba5817467743fbcf24b698124b02)RA\_ELC\_PERIPHERAL\_DAC0

| #define RA\_ELC\_PERIPHERAL\_DAC0   12 |
| --- |

## [◆ ](#ad6bb2d32abfad10bd283894efb7fe968)RA\_ELC\_PERIPHERAL\_GPT\_A

| #define RA\_ELC\_PERIPHERAL\_GPT\_A   0 |
| --- |

## [◆ ](#a8c4b99abfaa798b3b15f3435a73bad86)RA\_ELC\_PERIPHERAL\_GPT\_B

| #define RA\_ELC\_PERIPHERAL\_GPT\_B   1 |
| --- |

## [◆ ](#af0000625eec82c9f4ebe20da1cec7c66)RA\_ELC\_PERIPHERAL\_GPT\_C

| #define RA\_ELC\_PERIPHERAL\_GPT\_C   2 |
| --- |

## [◆ ](#ae9ae748233cce2fa65b334c2f8b2a6f7)RA\_ELC\_PERIPHERAL\_GPT\_D

| #define RA\_ELC\_PERIPHERAL\_GPT\_D   3 |
| --- |

## [◆ ](#aefc3deade612ed7aa53abd397d20af3b)RA\_ELC\_PERIPHERAL\_GPT\_E

| #define RA\_ELC\_PERIPHERAL\_GPT\_E   4 |
| --- |

## [◆ ](#a4bb2ffb785a17a225d5eb6e80f0040bf)RA\_ELC\_PERIPHERAL\_GPT\_F

| #define RA\_ELC\_PERIPHERAL\_GPT\_F   5 |
| --- |

## [◆ ](#a2ccd7f6730384fb8550054ea2195a67a)RA\_ELC\_PERIPHERAL\_GPT\_G

| #define RA\_ELC\_PERIPHERAL\_GPT\_G   6 |
| --- |

## [◆ ](#a6e737df13755e4e0039e98610aa31f3c)RA\_ELC\_PERIPHERAL\_GPT\_H

| #define RA\_ELC\_PERIPHERAL\_GPT\_H   7 |
| --- |

## [◆ ](#a5830e830b7b10cd68441de2648edd6a0)RA\_ELC\_PERIPHERAL\_IOPORT1

| #define RA\_ELC\_PERIPHERAL\_IOPORT1   14 |
| --- |

## [◆ ](#a42d4feb2c854cc1964455297e6d7eb72)RA\_ELC\_PERIPHERAL\_IOPORT2

| #define RA\_ELC\_PERIPHERAL\_IOPORT2   15 |
| --- |

## [◆ ](#a349933f20d7b6f768e49239724d0c5f7)RA\_ELC\_PERIPHERAL\_IOPORT3

| #define RA\_ELC\_PERIPHERAL\_IOPORT3   16 |
| --- |

## [◆ ](#a6d08d1db64f903fa2dacfc81568b004d)RA\_ELC\_PERIPHERAL\_IOPORT4

| #define RA\_ELC\_PERIPHERAL\_IOPORT4   17 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [misc](dir_b5927901ba0eeb0fdf9ca7870f5af60a.md)
- [renesas](dir_86b946318bd38151d049d676c19e4b11.md)
- [ra-elc](dir_fc824a581c07e3e227952b4fed9afa76.md)
- [ra4e1-elc.h](ra4e1-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
