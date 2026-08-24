---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra6e2-elc_8h.html
original_path: doxygen/html/ra6e2-elc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra6e2-elc.h File Reference

[Go to the source code of this file.](ra6e2-elc_8h_source.md)

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
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ10](#a3e9a895c4855c3db6ac7fc5900b57807)   0x00B |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ11](#a46f43f1dd26e006c26b11bd45e53a728)   0x00C |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ12](#affb7ae86a41c8cc8582e6c6ef284a5d8)   0x00D |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ13](#ad7435ed602899357eae0f46c09bf542c)   0x00E |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ14](#ada7702d0ac50f9b3e82ef50d6be50470)   0x00F |
| #define | [RA\_ELC\_EVENT\_DMAC0\_INT](#a906929a9ae7dd7de44d21a32d3635080)   0x020 |
| #define | [RA\_ELC\_EVENT\_DMAC1\_INT](#a76b9d9fa8af16a1480fcc8d8ec12572f)   0x021 |
| #define | [RA\_ELC\_EVENT\_DMAC2\_INT](#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)   0x022 |
| #define | [RA\_ELC\_EVENT\_DMAC3\_INT](#a0b9d72a41fd7c5b27e6c31967645b907)   0x023 |
| #define | [RA\_ELC\_EVENT\_DMAC4\_INT](#a4cae5afbbe49719555bbbfa12b8727f5)   0x024 |
| #define | [RA\_ELC\_EVENT\_DMAC5\_INT](#a000e31aba8a821f4358a435d280b3a7b)   0x025 |
| #define | [RA\_ELC\_EVENT\_DMAC6\_INT](#a2d1f6d1c797a0d787a5d5c08b0fc18ad)   0x026 |
| #define | [RA\_ELC\_EVENT\_DMAC7\_INT](#ae8caef45a510d4c4f1c55f923e01799e)   0x027 |
| #define | [RA\_ELC\_EVENT\_DTC\_COMPLETE](#a9a58e3a2c10447906aaf35bab5664d24)   0x029 |
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
| #define | [RA\_ELC\_EVENT\_IWDT\_UNDERFLOW](#abc837f1fcfffeb2ec231c79336379dda)   0x052 |
| #define | [RA\_ELC\_EVENT\_WDT\_UNDERFLOW](#a6cdb7a60a850f9ec23f19c548a6cc544)   0x053 |
| #define | [RA\_ELC\_EVENT\_RTC\_ALARM](#a76fd68b555574159d563d2dfd68d90b9)   0x054 |
| #define | [RA\_ELC\_EVENT\_RTC\_PERIOD](#a144901ee7b31b96eba18a39d98c4b953)   0x055 |
| #define | [RA\_ELC\_EVENT\_RTC\_CARRY](#a241cd3c65033b46a1160d5815cc86fd7)   0x056 |
| #define | [RA\_ELC\_EVENT\_CAN\_RXF](#a381d0e6b749cb12add2dfcb129f80468)   0x059 |
| #define | [RA\_ELC\_EVENT\_CAN\_GLERR](#a05a66b601667344eff54e86b13a820d5)   0x05A |
| #define | [RA\_ELC\_EVENT\_CAN\_DMAREQ0](#a3961be8854a154802e42c54ce6ae19d7)   0x05B |
| #define | [RA\_ELC\_EVENT\_CAN\_DMAREQ1](#a9ba34879d45c552845396b0a86dfaa26)   0x05C |
| #define | [RA\_ELC\_EVENT\_CAN0\_TX](#a31b33463c8527b56ad5760d86f066c6c)   0x063 |
| #define | [RA\_ELC\_EVENT\_CAN0\_CHERR](#a0c01b6adbdd0b29b4390a34acfee339b)   0x064 |
| #define | [RA\_ELC\_EVENT\_CAN0\_COMFRX](#a84cb35e4a3dfad95529937db4966c63f)   0x065 |
| #define | [RA\_ELC\_EVENT\_CAN0\_CF\_DMAREQ](#a5d73e70c306cc7cd5d89a9963b9075f5)   0x066 |
| #define | [RA\_ELC\_EVENT\_CAN0\_RXMB](#aa7871b154ba1e9bbb8a48aeeec65e416)   0x067 |
| #define | [RA\_ELC\_EVENT\_USBFS\_INT](#aac8d97813e8a3276bdac764faf7b580d)   0x06D |
| #define | [RA\_ELC\_EVENT\_USBFS\_RESUME](#a9458dbf2b1da6fc51ca2c2933dcb6b37)   0x06E |
| #define | [RA\_ELC\_EVENT\_SSI0\_TXI](#ac65193048ce5734b46bc2bf77b84cb4e)   0x08A |
| #define | [RA\_ELC\_EVENT\_SSI0\_RXI](#ab736656ae0b06de8383189075cbb2f27)   0x08B |
| #define | [RA\_ELC\_EVENT\_SSI0\_INT](#a1a89e9ab6abb3834992ee3ea3ebaf9c4)   0x08D |
| #define | [RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR](#a6ec3edb5e4de5bca1171ade1aa9ca19f)   0x09E |
| #define | [RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END](#a1390ee9467a9d093de1532f0703ec35f)   0x09F |
| #define | [RA\_ELC\_EVENT\_CAC\_OVERFLOW](#a3463c1e202ab7891521eda7196e1be80)   0x0A0 |
| #define | [RA\_ELC\_EVENT\_CEC\_INTDA](#a99b37093de561bf4289c57b65299946a)   0x0AB |
| #define | [RA\_ELC\_EVENT\_CEC\_INTCE](#ae30dbb0a9aef9ad39e9c9998b3df27bd)   0x0AC |
| #define | [RA\_ELC\_EVENT\_CEC\_INTERR](#aa07c92068ed7f5b00114c5f8ae26cf87)   0x0AD |
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
| #define | [RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A](#aec8a8b590cc124ca12425f34b5a61020)   0x0C0 |
| #define | [RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B](#ae1ed91479f405ac965da868e86bce533)   0x0C1 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_C](#a6d7c9090c21a8a0c497356050d649ec6)   0x0C2 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_D](#af5b8ca097747bd987e81d8d81263aa81)   0x0C3 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_E](#a9ebec21375578c0e52d953773373bf1e)   0x0C4 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_F](#ad503a55a4548ff6ffd58e2b74d9eaf00)   0x0C5 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW](#a76692948000993fde4d286f1a521a6d2)   0x0C6 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW](#a9edde37b8c0835978aa55d58d77c5ad5)   0x0C7 |
| #define | [RA\_ELC\_EVENT\_GPT0\_PC](#a21a934c940f85a7e4e592167eb468fd3)   0x0C8 |
| #define | [RA\_ELC\_EVENT\_GPT0\_AD\_TRIG\_A](#a8c54ce860777032d9143077a5246c3d2)   0x0C9 |
| #define | [RA\_ELC\_EVENT\_GPT0\_AD\_TRIG\_B](#af3593fcaa05166f3993f9b136d1e1a71)   0x0CA |
| #define | [RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A](#a33a428565bfa3237aa4eda10b982fc65)   0x0CB |
| #define | [RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B](#a5326aaf270290b524f8cb2e126d06602)   0x0CC |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_C](#a2e55bae34ab30f2d802b8eaf93dd3cfd)   0x0CD |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_D](#ada3870f40beeec10e9366e908ed980d0)   0x0CE |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_E](#a5d4f72e95b7bb76315b9ffa059730620)   0x0CF |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_F](#a548923b7385648e4f15fef4ecb315478)   0x0D0 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW](#aa6eac7cf283073eea62fbaa1df2017f2)   0x0D1 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW](#ae8cefd5f23897d43cffba4e91b7c8b5c)   0x0D2 |
| #define | [RA\_ELC\_EVENT\_GPT1\_PC](#aa0208084abba3e2601c8cf7bb42837fd)   0x0D3 |
| #define | [RA\_ELC\_EVENT\_GPT1\_AD\_TRIG\_A](#aaa3f7fe99d60fc9891b9ef416ecbd698)   0x0D4 |
| #define | [RA\_ELC\_EVENT\_GPT1\_AD\_TRIG\_B](#aacf6ed4895b5a98bc67b109eb41d6d7b)   0x0D5 |
| #define | [RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A](#ad1a5796e0c70a988165765f2ce8c1e80)   0x0D6 |
| #define | [RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B](#a73776ba7d66a478c92c6cb3dfed50af4)   0x0D7 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_C](#aa391fa888ded57351c9b62f54df1ce36)   0x0D8 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_D](#a90c7aa7bbddb04e6ae4b6eccb64a0e93)   0x0D9 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_E](#adbfb562e616a86a3e28f8c3f09553db9)   0x0DA |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_F](#a6f07945c82efae23754e34dc09bee884)   0x0DB |
| #define | [RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW](#aede7879166ef812139641122782d873b)   0x0DC |
| #define | [RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW](#ad71d20ad5434f219a61e0f0aded090d1)   0x0DD |
| #define | [RA\_ELC\_EVENT\_GPT2\_AD\_TRIG\_A](#a96bbd3418d8b51a80cef1d0a258095f0)   0x0DF |
| #define | [RA\_ELC\_EVENT\_GPT2\_AD\_TRIG\_B](#ab465f8fec7d2c7dcc742f25215609d2f)   0x0E0 |
| #define | [RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A](#a74526500dfb573fe21fbca739b1698e1)   0x0E1 |
| #define | [RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B](#ac6cfac3496e4ab71c9bf84b43e06486a)   0x0E2 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_C](#a1af4840d468eb4c4e1672a34652ef583)   0x0E3 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_D](#a263e6b02601dd37d6eedaab56a2e6fcd)   0x0E4 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_E](#a9035e080d39d60ecc898a596b9902aa6)   0x0E5 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_F](#a9cffb5aca60a4c7349789fc23fb197fb)   0x0E6 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW](#a546eff128c44a29f56fe90952cef475d)   0x0E7 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW](#ab30a5683e48535abbf0c400a5a0d8946)   0x0E8 |
| #define | [RA\_ELC\_EVENT\_GPT3\_AD\_TRIG\_A](#a339cba7a0388f06c6c64ca31f790e2a6)   0x0EA |
| #define | [RA\_ELC\_EVENT\_GPT3\_AD\_TRIG\_B](#a42c29ea80743756649f7b0ba64089844)   0x0EB |
| #define | [RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A](#a8130aa176d9d5dd698c62708111515e0)   0x0EC |
| #define | [RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B](#aa77a30a219070d15e358a43fbbd89728)   0x0ED |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_C](#af6c1cb172b343baa8d8bbe01d1674922)   0x0EE |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_D](#ae8c7945c641045c615922a3f82329c56)   0x0EF |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_E](#afcb271a94d9b07b7b1a204f325b80d52)   0x0F0 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_F](#a906eb0e1ed2786ed2b14e4608489b2cc)   0x0F1 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW](#abb820eb80ad8afc5c12dc3581fc7a0b9)   0x0F2 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW](#a65831ae6b037607dc55a2b1e8aa296a7)   0x0F3 |
| #define | [RA\_ELC\_EVENT\_GPT4\_PC](#af3ae1988661f1d68bd7cd5e36fb387f6)   0x0F4 |
| #define | [RA\_ELC\_EVENT\_GPT4\_AD\_TRIG\_A](#aeb0e1a8b6d75a81af57d8a3bb214ee1c)   0x0F5 |
| #define | [RA\_ELC\_EVENT\_GPT4\_AD\_TRIG\_B](#abb7899ca9b02154f712bdce109c1cc50)   0x0F6 |
| #define | [RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A](#adc4aceff99f296b06938254f9dcc1f2f)   0x0F7 |
| #define | [RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B](#aad1fc8b32dffaaa64f9908951f8b1c64)   0x0F8 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_C](#aebaa50f4643efe5b87798777cee578bc)   0x0F9 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_D](#a21965e21bd4045aa5010925620b4d827)   0x0FA |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_E](#a51a7cb146f0efbb7bc9f7336031006a4)   0x0FB |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_F](#abbd0bd21af2bd1679d6d7bc36001b97d)   0x0FC |
| #define | [RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW](#a038e7580f03fbdd74f417108cd2a8b4d)   0x0FD |
| #define | [RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW](#ac38b8f1154d6a699923b2bbf249e38fd)   0x0FE |
| #define | [RA\_ELC\_EVENT\_GPT5\_PC](#aa7e87dac91e6416a1b1a23ae5ee82b55)   0x0FF |
| #define | [RA\_ELC\_EVENT\_GPT5\_AD\_TRIG\_A](#a484a2a98e228eb884dfa951ad5cc82b5)   0x100 |
| #define | [RA\_ELC\_EVENT\_GPT5\_AD\_TRIG\_B](#a1b966ae97beca35cc342d06ca8fed5fc)   0x101 |
| #define | [RA\_ELC\_EVENT\_OPS\_UVW\_EDGE](#a8438d8d92e1950681388b40385a2c354)   0x15C |
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
| #define | [RA\_ELC\_EVENT\_SPI1\_RXI](#a2f5e3b5957e42c572fda94ec535b401b)   0x1C9 |
| #define | [RA\_ELC\_EVENT\_SPI1\_TXI](#a0aab8e60c14b34bccb74400a818524ac)   0x1CA |
| #define | [RA\_ELC\_EVENT\_SPI1\_IDLE](#a73da76e435d9de6b6b7ad48190d2c0a2)   0x1CB |
| #define | [RA\_ELC\_EVENT\_SPI1\_ERI](#aedf36efaaba39c4001386536d21f81e2)   0x1CC |
| #define | [RA\_ELC\_EVENT\_SPI1\_TEI](#a60f40983e3c6344a257bd157b40069d5)   0x1CD |
| #define | [RA\_ELC\_EVENT\_CAN0\_MRAM\_ERI](#adf49b7c6aecfae965cd0040817b11a5d)   0x1D0 |
| #define | [RA\_ELC\_EVENT\_QSPI\_INT](#a344b216f0d5880b31e7c1a4e700c85a4)   0x1DA |
| #define | [RA\_ELC\_EVENT\_DOC\_INT](#ab6c210d6481294137fd4bc32c39e5de1)   0x1DB |
| #define | [RA\_ELC\_EVENT\_I3C0\_RESPONSE](#a3080239b71b12d15d9cd78d78a0b65e6)   0x1DC |
| #define | [RA\_ELC\_EVENT\_I3C0\_COMMAND](#a92a8148f568fcf39ccde3817aef8ae9d)   0x1DD |
| #define | [RA\_ELC\_EVENT\_I3C0\_IBI](#a2060363167f356732fb5b817e4dbcdb5)   0x1DE |
| #define | [RA\_ELC\_EVENT\_I3C0\_RX](#a3b2265686fb51c1ae5cdc549cac4b3fd)   0x1DF |
| #define | [RA\_ELC\_EVENT\_IICB0\_RXI](#ac12a24178c5964cdd58666f7d57a1b1b)   0x1DF |
| #define | [RA\_ELC\_EVENT\_I3C0\_TX](#a6bd966e36dba524e3e5ad37250d9a2fe)   0x1E0 |
| #define | [RA\_ELC\_EVENT\_IICB0\_TXI](#ac3f18d838eb617f5022034a38238b3da)   0x1E0 |
| #define | [RA\_ELC\_EVENT\_I3C0\_RCV\_STATUS](#a0fe2a3ad8bf5bc9f9fbe79c2e3142a82)   0x1E1 |
| #define | [RA\_ELC\_EVENT\_I3C0\_HRESP](#ad03e0236533be6c8a679f45dae45b5f3)   0x1E2 |
| #define | [RA\_ELC\_EVENT\_I3C0\_HCMD](#a41c98f2bad994edd460738fc681d1915)   0x1E3 |
| #define | [RA\_ELC\_EVENT\_I3C0\_HRX](#a6944a47bc40eaf5be0bcd9a8ea3f61b3)   0x1E4 |
| #define | [RA\_ELC\_EVENT\_I3C0\_HTX](#a79b1703b94f1d6a62c589cd442d6c285)   0x1E5 |
| #define | [RA\_ELC\_EVENT\_I3C0\_TEND](#a263d9beac3bda75a81b657995262df84)   0x1E6 |
| #define | [RA\_ELC\_EVENT\_IICB0\_TEI](#accb1b88c154566410d539b20c64f67cc)   0x1E6 |
| #define | [RA\_ELC\_EVENT\_I3C0\_EEI](#a7031d655983b5a153dec583b24df13fe)   0x1E7 |
| #define | [RA\_ELC\_EVENT\_IICB0\_ERI](#ac0d8b1e8f379ef983dfd2004ed02e65e)   0x1E7 |
| #define | [RA\_ELC\_EVENT\_I3C0\_STEV](#a57e6e464e10dc72ef057cb24530f26cc)   0x1E8 |
| #define | [RA\_ELC\_EVENT\_I3C0\_MREFOVF](#a80adbdbcc1c63c9623763c8aa595c3ca)   0x1E9 |
| #define | [RA\_ELC\_EVENT\_I3C0\_MREFCPT](#a53d989fdbde5fa99dfcb6226c3419ab9)   0x1EA |
| #define | [RA\_ELC\_EVENT\_I3C0\_AMEV](#a1fdeb36ba55249ba92f2bdb425f18d74)   0x1EB |
| #define | [RA\_ELC\_EVENT\_I3C0\_WU](#a979332348cebe774723bfd610b02c36b)   0x1EC |
| #define | [RA\_ELC\_EVENT\_TRNG\_RDREQ](#aa2fe16c7e0528b58f2d9f0e9e9053899)   0x1F3 |
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
| #define | [RA\_ELC\_PERIPHERAL\_DAC1](#a84aa20e3793499f427f6c9ccb7a20566)   13 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT1](#a5830e830b7b10cd68441de2648edd6a0)   14 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT2](#a42d4feb2c854cc1964455297e6d7eb72)   15 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT3](#a349933f20d7b6f768e49239724d0c5f7)   16 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT4](#a6d08d1db64f903fa2dacfc81568b004d)   17 |
| #define | [RA\_ELC\_PERIPHERAL\_I3C](#a44df9c541681520b5fb529348b8deb81)   23 |

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

## [◆ ](#a6ec3edb5e4de5bca1171ade1aa9ca19f)RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR

| #define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR   0x09E |
| --- |

## [◆ ](#a1390ee9467a9d093de1532f0703ec35f)RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END

| #define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END   0x09F |
| --- |

## [◆ ](#a3463c1e202ab7891521eda7196e1be80)RA\_ELC\_EVENT\_CAC\_OVERFLOW

| #define RA\_ELC\_EVENT\_CAC\_OVERFLOW   0x0A0 |
| --- |

## [◆ ](#a5d73e70c306cc7cd5d89a9963b9075f5)RA\_ELC\_EVENT\_CAN0\_CF\_DMAREQ

| #define RA\_ELC\_EVENT\_CAN0\_CF\_DMAREQ   0x066 |
| --- |

## [◆ ](#a0c01b6adbdd0b29b4390a34acfee339b)RA\_ELC\_EVENT\_CAN0\_CHERR

| #define RA\_ELC\_EVENT\_CAN0\_CHERR   0x064 |
| --- |

## [◆ ](#a84cb35e4a3dfad95529937db4966c63f)RA\_ELC\_EVENT\_CAN0\_COMFRX

| #define RA\_ELC\_EVENT\_CAN0\_COMFRX   0x065 |
| --- |

## [◆ ](#adf49b7c6aecfae965cd0040817b11a5d)RA\_ELC\_EVENT\_CAN0\_MRAM\_ERI

| #define RA\_ELC\_EVENT\_CAN0\_MRAM\_ERI   0x1D0 |
| --- |

## [◆ ](#aa7871b154ba1e9bbb8a48aeeec65e416)RA\_ELC\_EVENT\_CAN0\_RXMB

| #define RA\_ELC\_EVENT\_CAN0\_RXMB   0x067 |
| --- |

## [◆ ](#a31b33463c8527b56ad5760d86f066c6c)RA\_ELC\_EVENT\_CAN0\_TX

| #define RA\_ELC\_EVENT\_CAN0\_TX   0x063 |
| --- |

## [◆ ](#a3961be8854a154802e42c54ce6ae19d7)RA\_ELC\_EVENT\_CAN\_DMAREQ0

| #define RA\_ELC\_EVENT\_CAN\_DMAREQ0   0x05B |
| --- |

## [◆ ](#a9ba34879d45c552845396b0a86dfaa26)RA\_ELC\_EVENT\_CAN\_DMAREQ1

| #define RA\_ELC\_EVENT\_CAN\_DMAREQ1   0x05C |
| --- |

## [◆ ](#a05a66b601667344eff54e86b13a820d5)RA\_ELC\_EVENT\_CAN\_GLERR

| #define RA\_ELC\_EVENT\_CAN\_GLERR   0x05A |
| --- |

## [◆ ](#a381d0e6b749cb12add2dfcb129f80468)RA\_ELC\_EVENT\_CAN\_RXF

| #define RA\_ELC\_EVENT\_CAN\_RXF   0x059 |
| --- |

## [◆ ](#ae30dbb0a9aef9ad39e9c9998b3df27bd)RA\_ELC\_EVENT\_CEC\_INTCE

| #define RA\_ELC\_EVENT\_CEC\_INTCE   0x0AC |
| --- |

## [◆ ](#a99b37093de561bf4289c57b65299946a)RA\_ELC\_EVENT\_CEC\_INTDA

| #define RA\_ELC\_EVENT\_CEC\_INTDA   0x0AB |
| --- |

## [◆ ](#aa07c92068ed7f5b00114c5f8ae26cf87)RA\_ELC\_EVENT\_CEC\_INTERR

| #define RA\_ELC\_EVENT\_CEC\_INTERR   0x0AD |
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

## [◆ ](#a8c54ce860777032d9143077a5246c3d2)RA\_ELC\_EVENT\_GPT0\_AD\_TRIG\_A

| #define RA\_ELC\_EVENT\_GPT0\_AD\_TRIG\_A   0x0C9 |
| --- |

## [◆ ](#af3593fcaa05166f3993f9b136d1e1a71)RA\_ELC\_EVENT\_GPT0\_AD\_TRIG\_B

| #define RA\_ELC\_EVENT\_GPT0\_AD\_TRIG\_B   0x0CA |
| --- |

## [◆ ](#aec8a8b590cc124ca12425f34b5a61020)RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A   0x0C0 |
| --- |

## [◆ ](#ae1ed91479f405ac965da868e86bce533)RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B   0x0C1 |
| --- |

## [◆ ](#a6d7c9090c21a8a0c497356050d649ec6)RA\_ELC\_EVENT\_GPT0\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_C   0x0C2 |
| --- |

## [◆ ](#af5b8ca097747bd987e81d8d81263aa81)RA\_ELC\_EVENT\_GPT0\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_D   0x0C3 |
| --- |

## [◆ ](#a9ebec21375578c0e52d953773373bf1e)RA\_ELC\_EVENT\_GPT0\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_E   0x0C4 |
| --- |

## [◆ ](#ad503a55a4548ff6ffd58e2b74d9eaf00)RA\_ELC\_EVENT\_GPT0\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_F   0x0C5 |
| --- |

## [◆ ](#a76692948000993fde4d286f1a521a6d2)RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW   0x0C6 |
| --- |

## [◆ ](#a9edde37b8c0835978aa55d58d77c5ad5)RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW   0x0C7 |
| --- |

## [◆ ](#a21a934c940f85a7e4e592167eb468fd3)RA\_ELC\_EVENT\_GPT0\_PC

| #define RA\_ELC\_EVENT\_GPT0\_PC   0x0C8 |
| --- |

## [◆ ](#aaa3f7fe99d60fc9891b9ef416ecbd698)RA\_ELC\_EVENT\_GPT1\_AD\_TRIG\_A

| #define RA\_ELC\_EVENT\_GPT1\_AD\_TRIG\_A   0x0D4 |
| --- |

## [◆ ](#aacf6ed4895b5a98bc67b109eb41d6d7b)RA\_ELC\_EVENT\_GPT1\_AD\_TRIG\_B

| #define RA\_ELC\_EVENT\_GPT1\_AD\_TRIG\_B   0x0D5 |
| --- |

## [◆ ](#a33a428565bfa3237aa4eda10b982fc65)RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A   0x0CB |
| --- |

## [◆ ](#a5326aaf270290b524f8cb2e126d06602)RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B   0x0CC |
| --- |

## [◆ ](#a2e55bae34ab30f2d802b8eaf93dd3cfd)RA\_ELC\_EVENT\_GPT1\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C   0x0CD |
| --- |

## [◆ ](#ada3870f40beeec10e9366e908ed980d0)RA\_ELC\_EVENT\_GPT1\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D   0x0CE |
| --- |

## [◆ ](#a5d4f72e95b7bb76315b9ffa059730620)RA\_ELC\_EVENT\_GPT1\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E   0x0CF |
| --- |

## [◆ ](#a548923b7385648e4f15fef4ecb315478)RA\_ELC\_EVENT\_GPT1\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F   0x0D0 |
| --- |

## [◆ ](#aa6eac7cf283073eea62fbaa1df2017f2)RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW   0x0D1 |
| --- |

## [◆ ](#ae8cefd5f23897d43cffba4e91b7c8b5c)RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW   0x0D2 |
| --- |

## [◆ ](#aa0208084abba3e2601c8cf7bb42837fd)RA\_ELC\_EVENT\_GPT1\_PC

| #define RA\_ELC\_EVENT\_GPT1\_PC   0x0D3 |
| --- |

## [◆ ](#a96bbd3418d8b51a80cef1d0a258095f0)RA\_ELC\_EVENT\_GPT2\_AD\_TRIG\_A

| #define RA\_ELC\_EVENT\_GPT2\_AD\_TRIG\_A   0x0DF |
| --- |

## [◆ ](#ab465f8fec7d2c7dcc742f25215609d2f)RA\_ELC\_EVENT\_GPT2\_AD\_TRIG\_B

| #define RA\_ELC\_EVENT\_GPT2\_AD\_TRIG\_B   0x0E0 |
| --- |

## [◆ ](#ad1a5796e0c70a988165765f2ce8c1e80)RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A   0x0D6 |
| --- |

## [◆ ](#a73776ba7d66a478c92c6cb3dfed50af4)RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B   0x0D7 |
| --- |

## [◆ ](#aa391fa888ded57351c9b62f54df1ce36)RA\_ELC\_EVENT\_GPT2\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C   0x0D8 |
| --- |

## [◆ ](#a90c7aa7bbddb04e6ae4b6eccb64a0e93)RA\_ELC\_EVENT\_GPT2\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D   0x0D9 |
| --- |

## [◆ ](#adbfb562e616a86a3e28f8c3f09553db9)RA\_ELC\_EVENT\_GPT2\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E   0x0DA |
| --- |

## [◆ ](#a6f07945c82efae23754e34dc09bee884)RA\_ELC\_EVENT\_GPT2\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F   0x0DB |
| --- |

## [◆ ](#aede7879166ef812139641122782d873b)RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW   0x0DC |
| --- |

## [◆ ](#ad71d20ad5434f219a61e0f0aded090d1)RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW   0x0DD |
| --- |

## [◆ ](#a339cba7a0388f06c6c64ca31f790e2a6)RA\_ELC\_EVENT\_GPT3\_AD\_TRIG\_A

| #define RA\_ELC\_EVENT\_GPT3\_AD\_TRIG\_A   0x0EA |
| --- |

## [◆ ](#a42c29ea80743756649f7b0ba64089844)RA\_ELC\_EVENT\_GPT3\_AD\_TRIG\_B

| #define RA\_ELC\_EVENT\_GPT3\_AD\_TRIG\_B   0x0EB |
| --- |

## [◆ ](#a74526500dfb573fe21fbca739b1698e1)RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A   0x0E1 |
| --- |

## [◆ ](#ac6cfac3496e4ab71c9bf84b43e06486a)RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B   0x0E2 |
| --- |

## [◆ ](#a1af4840d468eb4c4e1672a34652ef583)RA\_ELC\_EVENT\_GPT3\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_C   0x0E3 |
| --- |

## [◆ ](#a263e6b02601dd37d6eedaab56a2e6fcd)RA\_ELC\_EVENT\_GPT3\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_D   0x0E4 |
| --- |

## [◆ ](#a9035e080d39d60ecc898a596b9902aa6)RA\_ELC\_EVENT\_GPT3\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_E   0x0E5 |
| --- |

## [◆ ](#a9cffb5aca60a4c7349789fc23fb197fb)RA\_ELC\_EVENT\_GPT3\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_F   0x0E6 |
| --- |

## [◆ ](#a546eff128c44a29f56fe90952cef475d)RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW   0x0E7 |
| --- |

## [◆ ](#ab30a5683e48535abbf0c400a5a0d8946)RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW   0x0E8 |
| --- |

## [◆ ](#aeb0e1a8b6d75a81af57d8a3bb214ee1c)RA\_ELC\_EVENT\_GPT4\_AD\_TRIG\_A

| #define RA\_ELC\_EVENT\_GPT4\_AD\_TRIG\_A   0x0F5 |
| --- |

## [◆ ](#abb7899ca9b02154f712bdce109c1cc50)RA\_ELC\_EVENT\_GPT4\_AD\_TRIG\_B

| #define RA\_ELC\_EVENT\_GPT4\_AD\_TRIG\_B   0x0F6 |
| --- |

## [◆ ](#a8130aa176d9d5dd698c62708111515e0)RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A   0x0EC |
| --- |

## [◆ ](#aa77a30a219070d15e358a43fbbd89728)RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B   0x0ED |
| --- |

## [◆ ](#af6c1cb172b343baa8d8bbe01d1674922)RA\_ELC\_EVENT\_GPT4\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C   0x0EE |
| --- |

## [◆ ](#ae8c7945c641045c615922a3f82329c56)RA\_ELC\_EVENT\_GPT4\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D   0x0EF |
| --- |

## [◆ ](#afcb271a94d9b07b7b1a204f325b80d52)RA\_ELC\_EVENT\_GPT4\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E   0x0F0 |
| --- |

## [◆ ](#a906eb0e1ed2786ed2b14e4608489b2cc)RA\_ELC\_EVENT\_GPT4\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F   0x0F1 |
| --- |

## [◆ ](#abb820eb80ad8afc5c12dc3581fc7a0b9)RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW   0x0F2 |
| --- |

## [◆ ](#a65831ae6b037607dc55a2b1e8aa296a7)RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW   0x0F3 |
| --- |

## [◆ ](#af3ae1988661f1d68bd7cd5e36fb387f6)RA\_ELC\_EVENT\_GPT4\_PC

| #define RA\_ELC\_EVENT\_GPT4\_PC   0x0F4 |
| --- |

## [◆ ](#a484a2a98e228eb884dfa951ad5cc82b5)RA\_ELC\_EVENT\_GPT5\_AD\_TRIG\_A

| #define RA\_ELC\_EVENT\_GPT5\_AD\_TRIG\_A   0x100 |
| --- |

## [◆ ](#a1b966ae97beca35cc342d06ca8fed5fc)RA\_ELC\_EVENT\_GPT5\_AD\_TRIG\_B

| #define RA\_ELC\_EVENT\_GPT5\_AD\_TRIG\_B   0x101 |
| --- |

## [◆ ](#adc4aceff99f296b06938254f9dcc1f2f)RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A   0x0F7 |
| --- |

## [◆ ](#aad1fc8b32dffaaa64f9908951f8b1c64)RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B   0x0F8 |
| --- |

## [◆ ](#aebaa50f4643efe5b87798777cee578bc)RA\_ELC\_EVENT\_GPT5\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C   0x0F9 |
| --- |

## [◆ ](#a21965e21bd4045aa5010925620b4d827)RA\_ELC\_EVENT\_GPT5\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D   0x0FA |
| --- |

## [◆ ](#a51a7cb146f0efbb7bc9f7336031006a4)RA\_ELC\_EVENT\_GPT5\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E   0x0FB |
| --- |

## [◆ ](#abbd0bd21af2bd1679d6d7bc36001b97d)RA\_ELC\_EVENT\_GPT5\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F   0x0FC |
| --- |

## [◆ ](#a038e7580f03fbdd74f417108cd2a8b4d)RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW   0x0FD |
| --- |

## [◆ ](#ac38b8f1154d6a699923b2bbf249e38fd)RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW   0x0FE |
| --- |

## [◆ ](#aa7e87dac91e6416a1b1a23ae5ee82b55)RA\_ELC\_EVENT\_GPT5\_PC

| #define RA\_ELC\_EVENT\_GPT5\_PC   0x0FF |
| --- |

## [◆ ](#a1fdeb36ba55249ba92f2bdb425f18d74)RA\_ELC\_EVENT\_I3C0\_AMEV

| #define RA\_ELC\_EVENT\_I3C0\_AMEV   0x1EB |
| --- |

## [◆ ](#a92a8148f568fcf39ccde3817aef8ae9d)RA\_ELC\_EVENT\_I3C0\_COMMAND

| #define RA\_ELC\_EVENT\_I3C0\_COMMAND   0x1DD |
| --- |

## [◆ ](#a7031d655983b5a153dec583b24df13fe)RA\_ELC\_EVENT\_I3C0\_EEI

| #define RA\_ELC\_EVENT\_I3C0\_EEI   0x1E7 |
| --- |

## [◆ ](#a41c98f2bad994edd460738fc681d1915)RA\_ELC\_EVENT\_I3C0\_HCMD

| #define RA\_ELC\_EVENT\_I3C0\_HCMD   0x1E3 |
| --- |

## [◆ ](#ad03e0236533be6c8a679f45dae45b5f3)RA\_ELC\_EVENT\_I3C0\_HRESP

| #define RA\_ELC\_EVENT\_I3C0\_HRESP   0x1E2 |
| --- |

## [◆ ](#a6944a47bc40eaf5be0bcd9a8ea3f61b3)RA\_ELC\_EVENT\_I3C0\_HRX

| #define RA\_ELC\_EVENT\_I3C0\_HRX   0x1E4 |
| --- |

## [◆ ](#a79b1703b94f1d6a62c589cd442d6c285)RA\_ELC\_EVENT\_I3C0\_HTX

| #define RA\_ELC\_EVENT\_I3C0\_HTX   0x1E5 |
| --- |

## [◆ ](#a2060363167f356732fb5b817e4dbcdb5)RA\_ELC\_EVENT\_I3C0\_IBI

| #define RA\_ELC\_EVENT\_I3C0\_IBI   0x1DE |
| --- |

## [◆ ](#a53d989fdbde5fa99dfcb6226c3419ab9)RA\_ELC\_EVENT\_I3C0\_MREFCPT

| #define RA\_ELC\_EVENT\_I3C0\_MREFCPT   0x1EA |
| --- |

## [◆ ](#a80adbdbcc1c63c9623763c8aa595c3ca)RA\_ELC\_EVENT\_I3C0\_MREFOVF

| #define RA\_ELC\_EVENT\_I3C0\_MREFOVF   0x1E9 |
| --- |

## [◆ ](#a0fe2a3ad8bf5bc9f9fbe79c2e3142a82)RA\_ELC\_EVENT\_I3C0\_RCV\_STATUS

| #define RA\_ELC\_EVENT\_I3C0\_RCV\_STATUS   0x1E1 |
| --- |

## [◆ ](#a3080239b71b12d15d9cd78d78a0b65e6)RA\_ELC\_EVENT\_I3C0\_RESPONSE

| #define RA\_ELC\_EVENT\_I3C0\_RESPONSE   0x1DC |
| --- |

## [◆ ](#a3b2265686fb51c1ae5cdc549cac4b3fd)RA\_ELC\_EVENT\_I3C0\_RX

| #define RA\_ELC\_EVENT\_I3C0\_RX   0x1DF |
| --- |

## [◆ ](#a57e6e464e10dc72ef057cb24530f26cc)RA\_ELC\_EVENT\_I3C0\_STEV

| #define RA\_ELC\_EVENT\_I3C0\_STEV   0x1E8 |
| --- |

## [◆ ](#a263d9beac3bda75a81b657995262df84)RA\_ELC\_EVENT\_I3C0\_TEND

| #define RA\_ELC\_EVENT\_I3C0\_TEND   0x1E6 |
| --- |

## [◆ ](#a6bd966e36dba524e3e5ad37250d9a2fe)RA\_ELC\_EVENT\_I3C0\_TX

| #define RA\_ELC\_EVENT\_I3C0\_TX   0x1E0 |
| --- |

## [◆ ](#a979332348cebe774723bfd610b02c36b)RA\_ELC\_EVENT\_I3C0\_WU

| #define RA\_ELC\_EVENT\_I3C0\_WU   0x1EC |
| --- |

## [◆ ](#a04ee26d7188b7441627bb89249545cfa)RA\_ELC\_EVENT\_ICU\_IRQ0

| #define RA\_ELC\_EVENT\_ICU\_IRQ0   0x001 |
| --- |

## [◆ ](#ac9f6681c03b50d8b3a24798b3e790170)RA\_ELC\_EVENT\_ICU\_IRQ1

| #define RA\_ELC\_EVENT\_ICU\_IRQ1   0x002 |
| --- |

## [◆ ](#a3e9a895c4855c3db6ac7fc5900b57807)RA\_ELC\_EVENT\_ICU\_IRQ10

| #define RA\_ELC\_EVENT\_ICU\_IRQ10   0x00B |
| --- |

## [◆ ](#a46f43f1dd26e006c26b11bd45e53a728)RA\_ELC\_EVENT\_ICU\_IRQ11

| #define RA\_ELC\_EVENT\_ICU\_IRQ11   0x00C |
| --- |

## [◆ ](#affb7ae86a41c8cc8582e6c6ef284a5d8)RA\_ELC\_EVENT\_ICU\_IRQ12

| #define RA\_ELC\_EVENT\_ICU\_IRQ12   0x00D |
| --- |

## [◆ ](#ad7435ed602899357eae0f46c09bf542c)RA\_ELC\_EVENT\_ICU\_IRQ13

| #define RA\_ELC\_EVENT\_ICU\_IRQ13   0x00E |
| --- |

## [◆ ](#ada7702d0ac50f9b3e82ef50d6be50470)RA\_ELC\_EVENT\_ICU\_IRQ14

| #define RA\_ELC\_EVENT\_ICU\_IRQ14   0x00F |
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

## [◆ ](#ac0d8b1e8f379ef983dfd2004ed02e65e)RA\_ELC\_EVENT\_IICB0\_ERI

| #define RA\_ELC\_EVENT\_IICB0\_ERI   0x1E7 |
| --- |

## [◆ ](#ac12a24178c5964cdd58666f7d57a1b1b)RA\_ELC\_EVENT\_IICB0\_RXI

| #define RA\_ELC\_EVENT\_IICB0\_RXI   0x1DF |
| --- |

## [◆ ](#accb1b88c154566410d539b20c64f67cc)RA\_ELC\_EVENT\_IICB0\_TEI

| #define RA\_ELC\_EVENT\_IICB0\_TEI   0x1E6 |
| --- |

## [◆ ](#ac3f18d838eb617f5022034a38238b3da)RA\_ELC\_EVENT\_IICB0\_TXI

| #define RA\_ELC\_EVENT\_IICB0\_TXI   0x1E0 |
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

## [◆ ](#a8438d8d92e1950681388b40385a2c354)RA\_ELC\_EVENT\_OPS\_UVW\_EDGE

| #define RA\_ELC\_EVENT\_OPS\_UVW\_EDGE   0x15C |
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

## [◆ ](#aedf36efaaba39c4001386536d21f81e2)RA\_ELC\_EVENT\_SPI1\_ERI

| #define RA\_ELC\_EVENT\_SPI1\_ERI   0x1CC |
| --- |

## [◆ ](#a73da76e435d9de6b6b7ad48190d2c0a2)RA\_ELC\_EVENT\_SPI1\_IDLE

| #define RA\_ELC\_EVENT\_SPI1\_IDLE   0x1CB |
| --- |

## [◆ ](#a2f5e3b5957e42c572fda94ec535b401b)RA\_ELC\_EVENT\_SPI1\_RXI

| #define RA\_ELC\_EVENT\_SPI1\_RXI   0x1C9 |
| --- |

## [◆ ](#a60f40983e3c6344a257bd157b40069d5)RA\_ELC\_EVENT\_SPI1\_TEI

| #define RA\_ELC\_EVENT\_SPI1\_TEI   0x1CD |
| --- |

## [◆ ](#a0aab8e60c14b34bccb74400a818524ac)RA\_ELC\_EVENT\_SPI1\_TXI

| #define RA\_ELC\_EVENT\_SPI1\_TXI   0x1CA |
| --- |

## [◆ ](#a1a89e9ab6abb3834992ee3ea3ebaf9c4)RA\_ELC\_EVENT\_SSI0\_INT

| #define RA\_ELC\_EVENT\_SSI0\_INT   0x08D |
| --- |

## [◆ ](#ab736656ae0b06de8383189075cbb2f27)RA\_ELC\_EVENT\_SSI0\_RXI

| #define RA\_ELC\_EVENT\_SSI0\_RXI   0x08B |
| --- |

## [◆ ](#ac65193048ce5734b46bc2bf77b84cb4e)RA\_ELC\_EVENT\_SSI0\_TXI

| #define RA\_ELC\_EVENT\_SSI0\_TXI   0x08A |
| --- |

## [◆ ](#aa2fe16c7e0528b58f2d9f0e9e9053899)RA\_ELC\_EVENT\_TRNG\_RDREQ

| #define RA\_ELC\_EVENT\_TRNG\_RDREQ   0x1F3 |
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

## [◆ ](#a84aa20e3793499f427f6c9ccb7a20566)RA\_ELC\_PERIPHERAL\_DAC1

| #define RA\_ELC\_PERIPHERAL\_DAC1   13 |
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

## [◆ ](#a44df9c541681520b5fb529348b8deb81)RA\_ELC\_PERIPHERAL\_I3C

| #define RA\_ELC\_PERIPHERAL\_I3C   23 |
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
- [ra6e2-elc.h](ra6e2-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
