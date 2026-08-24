---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra4m1-elc_8h.html
original_path: doxygen/html/ra4m1-elc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra4m1-elc.h File Reference

[Go to the source code of this file.](ra4m1-elc_8h_source.md)

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
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ14](#ada7702d0ac50f9b3e82ef50d6be50470)   0x00F |
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ15](#afab294cf0d58a5bb4dd578774b0ad9aa)   0x010 |
| #define | [RA\_ELC\_EVENT\_DMAC0\_INT](#a906929a9ae7dd7de44d21a32d3635080)   0x011 |
| #define | [RA\_ELC\_EVENT\_DMAC1\_INT](#a76b9d9fa8af16a1480fcc8d8ec12572f)   0x012 |
| #define | [RA\_ELC\_EVENT\_DMAC2\_INT](#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)   0x013 |
| #define | [RA\_ELC\_EVENT\_DMAC3\_INT](#a0b9d72a41fd7c5b27e6c31967645b907)   0x014 |
| #define | [RA\_ELC\_EVENT\_DTC\_COMPLETE](#a9a58e3a2c10447906aaf35bab5664d24)   0x015 |
| #define | [RA\_ELC\_EVENT\_DTC\_END](#a5ab484cdaf470b47e95005d83d60394f)   0x016 |
| #define | [RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL](#a26e0aaa4a17196ada130bbb714a6d3bd)   0x017 |
| #define | [RA\_ELC\_EVENT\_FCU\_FRDYI](#a535af54c8bcfff47cc90ba1226044d71)   0x018 |
| #define | [RA\_ELC\_EVENT\_LVD\_LVD1](#a7ab275777147d06315a04abb3f2f6d51)   0x019 |
| #define | [RA\_ELC\_EVENT\_LVD\_LVD2](#ad52acadba107b7f907d678f44769a4cb)   0x01A |
| #define | [RA\_ELC\_EVENT\_LVD\_VBATT](#a1ab4e1434620d962450d98c0fee2f89c)   0x01B |
| #define | [RA\_ELC\_EVENT\_CGC\_MOSC\_STOP](#a290decf4254396cbce267cb52a619717)   0x01C |
| #define | [RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST](#ac6953f0c8caa6b5ef8c9893c7ff4baa1)   0x01D |
| #define | [RA\_ELC\_EVENT\_AGT0\_INT](#a4c3604a42ead1d43f472e901087ec148)   0x01E |
| #define | [RA\_ELC\_EVENT\_AGT0\_COMPARE\_A](#a015e6f8aed4b467f4554e6887b4d9ec9)   0x01F |
| #define | [RA\_ELC\_EVENT\_AGT0\_COMPARE\_B](#ada1ad302dc5b987a6f7c972afae729f2)   0x020 |
| #define | [RA\_ELC\_EVENT\_AGT1\_INT](#a635180e38c932579072f4eebd665592f)   0x021 |
| #define | [RA\_ELC\_EVENT\_AGT1\_COMPARE\_A](#aeb2399818b6b141ab4a37e257dba22be)   0x022 |
| #define | [RA\_ELC\_EVENT\_AGT1\_COMPARE\_B](#a1d660c78348b48ea7a072225491ae44b)   0x023 |
| #define | [RA\_ELC\_EVENT\_IWDT\_UNDERFLOW](#abc837f1fcfffeb2ec231c79336379dda)   0x024 |
| #define | [RA\_ELC\_EVENT\_WDT\_UNDERFLOW](#a6cdb7a60a850f9ec23f19c548a6cc544)   0x025 |
| #define | [RA\_ELC\_EVENT\_RTC\_ALARM](#a76fd68b555574159d563d2dfd68d90b9)   0x026 |
| #define | [RA\_ELC\_EVENT\_RTC\_PERIOD](#a144901ee7b31b96eba18a39d98c4b953)   0x027 |
| #define | [RA\_ELC\_EVENT\_RTC\_CARRY](#a241cd3c65033b46a1160d5815cc86fd7)   0x028 |
| #define | [RA\_ELC\_EVENT\_ADC0\_SCAN\_END](#ad7284976213551f7d4fa450bf2bf8c7c)   0x029 |
| #define | [RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B](#aecbe4efa29972b832e35ebb00d7499ad)   0x02A |
| #define | [RA\_ELC\_EVENT\_ADC0\_WINDOW\_A](#aa4feb2c3e29ba84d1397c618b7b860bf)   0x02B |
| #define | [RA\_ELC\_EVENT\_ADC0\_WINDOW\_B](#ab59c8ec4f20de5cf4709efe0a7ee70a1)   0x02C |
| #define | [RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH](#af187c78a1f05fc4be81aa3af36e4cde5)   0x02D |
| #define | [RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH](#a65d6c499a6852434b4802f8ef7066eb4)   0x02E |
| #define | [RA\_ELC\_EVENT\_ACMPLP0\_INT](#a46ba8b903950b3ff8b04c8176e7844b5)   0x02F |
| #define | [RA\_ELC\_EVENT\_ACMPLP1\_INT](#a377a3e92bcdf0e45d2b12223ddd85666)   0x030 |
| #define | [RA\_ELC\_EVENT\_USBFS\_FIFO\_0](#ae4dbb89c58220f72818cc9c28d97905b)   0x031 |
| #define | [RA\_ELC\_EVENT\_USBFS\_FIFO\_1](#a0ef2efa2ea339cad7598f11fe549cdd9)   0x032 |
| #define | [RA\_ELC\_EVENT\_USBFS\_INT](#aac8d97813e8a3276bdac764faf7b580d)   0x033 |
| #define | [RA\_ELC\_EVENT\_USBFS\_RESUME](#a9458dbf2b1da6fc51ca2c2933dcb6b37)   0x034 |
| #define | [RA\_ELC\_EVENT\_IIC0\_RXI](#a7271a25cdc3c987313efbafcd2a746cf)   0x035 |
| #define | [RA\_ELC\_EVENT\_IIC0\_TXI](#a7843f8a23feb383202fa6ad3be8fae5c)   0x036 |
| #define | [RA\_ELC\_EVENT\_IIC0\_TEI](#a52270344b26073c127a0269c5ec4e228)   0x037 |
| #define | [RA\_ELC\_EVENT\_IIC0\_ERI](#a667eb763b55f973b141837e82dbbae6e)   0x038 |
| #define | [RA\_ELC\_EVENT\_IIC0\_WUI](#a2a074dab614a1639ea5fa4f6d3baffd3)   0x039 |
| #define | [RA\_ELC\_EVENT\_IIC1\_RXI](#ad03e6b81d0e7ce53737e5c3022f8d951)   0x03A |
| #define | [RA\_ELC\_EVENT\_IIC1\_TXI](#a641c91157c98f41d3cf5ff6bbe25192d)   0x03B |
| #define | [RA\_ELC\_EVENT\_IIC1\_TEI](#a45ed226ccaace8813aa653276a52999d)   0x03C |
| #define | [RA\_ELC\_EVENT\_IIC1\_ERI](#a2221a129f0e323fa5b96bfe5ed0e007f)   0x03D |
| #define | [RA\_ELC\_EVENT\_SSI0\_TXI](#ac65193048ce5734b46bc2bf77b84cb4e)   0x03E |
| #define | [RA\_ELC\_EVENT\_SSI0\_RXI](#ab736656ae0b06de8383189075cbb2f27)   0x03F |
| #define | [RA\_ELC\_EVENT\_SSI0\_INT](#a1a89e9ab6abb3834992ee3ea3ebaf9c4)   0x041 |
| #define | [RA\_ELC\_EVENT\_CTSU\_WRITE](#a2faf033bad7b355f8beb9386a2d0e93b)   0x042 |
| #define | [RA\_ELC\_EVENT\_CTSU\_READ](#ad7cd21f5db3e117b87ffab8a6cb47272)   0x043 |
| #define | [RA\_ELC\_EVENT\_CTSU\_END](#acfe8138822bcd3f02fe50316e40c7641)   0x044 |
| #define | [RA\_ELC\_EVENT\_KEY\_INT](#a4412a0ec84a10d14d131754c5f9eb509)   0x045 |
| #define | [RA\_ELC\_EVENT\_DOC\_INT](#ab6c210d6481294137fd4bc32c39e5de1)   0x046 |
| #define | [RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR](#a6ec3edb5e4de5bca1171ade1aa9ca19f)   0x047 |
| #define | [RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END](#a1390ee9467a9d093de1532f0703ec35f)   0x048 |
| #define | [RA\_ELC\_EVENT\_CAC\_OVERFLOW](#a3463c1e202ab7891521eda7196e1be80)   0x049 |
| #define | [RA\_ELC\_EVENT\_CAN0\_ERROR](#aa4f3b915e26ee83dcc8c383a1fdb2425)   0x04A |
| #define | [RA\_ELC\_EVENT\_CAN0\_FIFO\_RX](#ad6e2ac69f8d10baa2d023e680e2f4c2f)   0x04B |
| #define | [RA\_ELC\_EVENT\_CAN0\_FIFO\_TX](#a52d0f15f6d388658ae060aec6302b448)   0x04C |
| #define | [RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX](#a0b017dad5f8642aa70f6f96c45e84a72)   0x04D |
| #define | [RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX](#a71880c5fc6363d67d8d126fd63a5354c)   0x04E |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_1](#aee58e9a0c4313f0ec08f0652e5002008)   0x04F |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_2](#a36d858520d28847eead0fbfe7950be2d)   0x050 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_3](#a545dadce70bbcea1116cd13490fe2571)   0x051 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_4](#a4e478b84ef99ae71c102ad3d5c71089a)   0x052 |
| #define | [RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0](#ae5c28618f4e68eef6ca83bdcec515abb)   0x053 |
| #define | [RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1](#a9f0b82bfff5ea2ba414ac0bccad9a34d)   0x054 |
| #define | [RA\_ELC\_EVENT\_POEG0\_EVENT](#a81e18423a1f61e34f0daab6f7367eae2)   0x055 |
| #define | [RA\_ELC\_EVENT\_POEG1\_EVENT](#a2a43c2ce461fde766e66a4451929a875)   0x056 |
| #define | [RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A](#aec8a8b590cc124ca12425f34b5a61020)   0x057 |
| #define | [RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B](#ae1ed91479f405ac965da868e86bce533)   0x058 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_C](#a6d7c9090c21a8a0c497356050d649ec6)   0x059 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_D](#af5b8ca097747bd987e81d8d81263aa81)   0x05A |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_E](#a9ebec21375578c0e52d953773373bf1e)   0x05B |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_F](#ad503a55a4548ff6ffd58e2b74d9eaf00)   0x05C |
| #define | [RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW](#a76692948000993fde4d286f1a521a6d2)   0x05D |
| #define | [RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW](#a9edde37b8c0835978aa55d58d77c5ad5)   0x05E |
| #define | [RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A](#a33a428565bfa3237aa4eda10b982fc65)   0x05F |
| #define | [RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B](#a5326aaf270290b524f8cb2e126d06602)   0x060 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_C](#a2e55bae34ab30f2d802b8eaf93dd3cfd)   0x061 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_D](#ada3870f40beeec10e9366e908ed980d0)   0x062 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_E](#a5d4f72e95b7bb76315b9ffa059730620)   0x063 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_F](#a548923b7385648e4f15fef4ecb315478)   0x064 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW](#aa6eac7cf283073eea62fbaa1df2017f2)   0x065 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW](#ae8cefd5f23897d43cffba4e91b7c8b5c)   0x066 |
| #define | [RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A](#ad1a5796e0c70a988165765f2ce8c1e80)   0x067 |
| #define | [RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B](#a73776ba7d66a478c92c6cb3dfed50af4)   0x068 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_C](#aa391fa888ded57351c9b62f54df1ce36)   0x069 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_D](#a90c7aa7bbddb04e6ae4b6eccb64a0e93)   0x06A |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_E](#adbfb562e616a86a3e28f8c3f09553db9)   0x06B |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_F](#a6f07945c82efae23754e34dc09bee884)   0x06C |
| #define | [RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW](#aede7879166ef812139641122782d873b)   0x06D |
| #define | [RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW](#ad71d20ad5434f219a61e0f0aded090d1)   0x06E |
| #define | [RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A](#a74526500dfb573fe21fbca739b1698e1)   0x06F |
| #define | [RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B](#ac6cfac3496e4ab71c9bf84b43e06486a)   0x070 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_C](#a1af4840d468eb4c4e1672a34652ef583)   0x071 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_D](#a263e6b02601dd37d6eedaab56a2e6fcd)   0x072 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_E](#a9035e080d39d60ecc898a596b9902aa6)   0x073 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_F](#a9cffb5aca60a4c7349789fc23fb197fb)   0x074 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW](#a546eff128c44a29f56fe90952cef475d)   0x075 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW](#ab30a5683e48535abbf0c400a5a0d8946)   0x076 |
| #define | [RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A](#a8130aa176d9d5dd698c62708111515e0)   0x077 |
| #define | [RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B](#aa77a30a219070d15e358a43fbbd89728)   0x078 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_C](#af6c1cb172b343baa8d8bbe01d1674922)   0x079 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_D](#ae8c7945c641045c615922a3f82329c56)   0x07A |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_E](#afcb271a94d9b07b7b1a204f325b80d52)   0x07B |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_F](#a906eb0e1ed2786ed2b14e4608489b2cc)   0x07C |
| #define | [RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW](#abb820eb80ad8afc5c12dc3581fc7a0b9)   0x07D |
| #define | [RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW](#a65831ae6b037607dc55a2b1e8aa296a7)   0x07E |
| #define | [RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A](#adc4aceff99f296b06938254f9dcc1f2f)   0x07F |
| #define | [RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B](#aad1fc8b32dffaaa64f9908951f8b1c64)   0x080 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_C](#aebaa50f4643efe5b87798777cee578bc)   0x081 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_D](#a21965e21bd4045aa5010925620b4d827)   0x082 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_E](#a51a7cb146f0efbb7bc9f7336031006a4)   0x083 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_F](#abbd0bd21af2bd1679d6d7bc36001b97d)   0x084 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW](#a038e7580f03fbdd74f417108cd2a8b4d)   0x085 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW](#ac38b8f1154d6a699923b2bbf249e38fd)   0x086 |
| #define | [RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A](#acad1c37929903ddee569f40a3c5c59e3)   0x087 |
| #define | [RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B](#aa0fc9b447efbcba0bb6800f785daeb96)   0x088 |
| #define | [RA\_ELC\_EVENT\_GPT6\_COMPARE\_C](#a01f586bd98832ea9b8aa58741b61a319)   0x089 |
| #define | [RA\_ELC\_EVENT\_GPT6\_COMPARE\_D](#acd71c3b8e8e1d96aa3ff6affb93f5000)   0x08A |
| #define | [RA\_ELC\_EVENT\_GPT6\_COMPARE\_E](#a6abdcc7a6331a8283cfe0c1ac06b7d83)   0x08B |
| #define | [RA\_ELC\_EVENT\_GPT6\_COMPARE\_F](#a28b6b55ad533e3cb606b2b0937c916b3)   0x08C |
| #define | [RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW](#ac3c8dd6a5b7f95dccc58e7ec4e235a40)   0x08D |
| #define | [RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW](#acdece33585a75fccba962e4f764058fb)   0x08E |
| #define | [RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A](#afe1b39e5d37a5ed631dd18869cfbac8a)   0x08F |
| #define | [RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B](#a53b7cfc8d0a000bd57f159b09b0a9c26)   0x090 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COMPARE\_C](#add91262eba9ec860b788030af153161a)   0x091 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COMPARE\_D](#a9310fd708ca6f0afcf374bfc96e22e6e)   0x092 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COMPARE\_E](#a8d18bd54c972d1de01c2a9f86e832cd0)   0x093 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COMPARE\_F](#aca89f90e8afa3f656e76f5960717543c)   0x094 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW](#aac0ed7abde81cf4bcc7588bf64b53c04)   0x095 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW](#ab1935670b6c0a5b5629ef8ba9d854f6c)   0x096 |
| #define | [RA\_ELC\_EVENT\_OPS\_UVW\_EDGE](#a8438d8d92e1950681388b40385a2c354)   0x097 |
| #define | [RA\_ELC\_EVENT\_SCI0\_RXI](#ad9e9a8451a683c5b5bc8a2ace8264c27)   0x098 |
| #define | [RA\_ELC\_EVENT\_SCI0\_TXI](#aecc4fdda2a7eeb2bab0b894f2e5047d9)   0x099 |
| #define | [RA\_ELC\_EVENT\_SCI0\_TEI](#ae845a850ab730c651badc5c857e28ee9)   0x09A |
| #define | [RA\_ELC\_EVENT\_SCI0\_ERI](#ad4580e769bae423298276e31ee2ee071)   0x09B |
| #define | [RA\_ELC\_EVENT\_SCI0\_AM](#ae2373b571584dae4d1c7fc57142ecb3c)   0x09C |
| #define | [RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI](#ad52a4c7660a4e609976f7045305f8ca7)   0x09D |
| #define | [RA\_ELC\_EVENT\_SCI1\_RXI](#ae936e9aa971a376cb4ea3405c68d57f0)   0x09E |
| #define | [RA\_ELC\_EVENT\_SCI1\_TXI](#abd1c6187f97f2817dc5eb59278a996b1)   0x09F |
| #define | [RA\_ELC\_EVENT\_SCI1\_TEI](#aae0ca4a1031af4c490fbb1ecbe201662)   0x0A0 |
| #define | [RA\_ELC\_EVENT\_SCI1\_ERI](#a6a673466eb5261d23ee06be132ca9cde)   0x0A1 |
| #define | [RA\_ELC\_EVENT\_SCI1\_AM](#ad9ca7dbcac36bb7f921cd8b8db761623)   0x0A2 |
| #define | [RA\_ELC\_EVENT\_SCI2\_RXI](#a484b0928fab1e96f3008b9e7b12bab07)   0x0A3 |
| #define | [RA\_ELC\_EVENT\_SCI2\_TXI](#a5991f7636af52ea3285cf17d300f62bb)   0x0A4 |
| #define | [RA\_ELC\_EVENT\_SCI2\_TEI](#a9bbdd2f449bfd5709f6c8b77b8378ca4)   0x0A5 |
| #define | [RA\_ELC\_EVENT\_SCI2\_ERI](#ad31428c7900c978dba266761df793f4c)   0x0A6 |
| #define | [RA\_ELC\_EVENT\_SCI2\_AM](#a023110baac3b030238844ab6a8999652)   0x0A7 |
| #define | [RA\_ELC\_EVENT\_SCI9\_RXI](#ac01e51a9360f409e430642d86818bf98)   0x0A8 |
| #define | [RA\_ELC\_EVENT\_SCI9\_TXI](#a8c628c59b08ed53781fd406ea22da796)   0x0A9 |
| #define | [RA\_ELC\_EVENT\_SCI9\_TEI](#ac3a064375ff90f3a6a35c5fdda680f95)   0x0AA |
| #define | [RA\_ELC\_EVENT\_SCI9\_ERI](#af2e4d2d6b59c512e536d901789b3c1a2)   0x0AB |
| #define | [RA\_ELC\_EVENT\_SCI9\_AM](#a2bfc7def09c933262aa530227a45af7d)   0x0AC |
| #define | [RA\_ELC\_EVENT\_SPI0\_RXI](#af77608914a79bea7797b63674c71db31)   0x0AD |
| #define | [RA\_ELC\_EVENT\_SPI0\_TXI](#a82d87016b5d694884bba33bf71e93e92)   0x0AE |
| #define | [RA\_ELC\_EVENT\_SPI0\_IDLE](#a920575ee3a202b0d7202cd053f1e235b)   0x0AF |
| #define | [RA\_ELC\_EVENT\_SPI0\_ERI](#ab588fafc974153bcf94087cdb1a71d73)   0x0B0 |
| #define | [RA\_ELC\_EVENT\_SPI0\_TEI](#a368a0ece3d89efe3ed8ab274471849b9)   0x0B1 |
| #define | [RA\_ELC\_EVENT\_SPI1\_RXI](#a2f5e3b5957e42c572fda94ec535b401b)   0x0B2 |
| #define | [RA\_ELC\_EVENT\_SPI1\_TXI](#a0aab8e60c14b34bccb74400a818524ac)   0x0B3 |
| #define | [RA\_ELC\_EVENT\_SPI1\_IDLE](#a73da76e435d9de6b6b7ad48190d2c0a2)   0x0B4 |
| #define | [RA\_ELC\_EVENT\_SPI1\_ERI](#aedf36efaaba39c4001386536d21f81e2)   0x0B5 |
| #define | [RA\_ELC\_EVENT\_SPI1\_TEI](#a60f40983e3c6344a257bd157b40069d5)   0x0B6 |
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
| #define | [RA\_ELC\_PERIPHERAL\_CTSU](#a66a60a7a3469054498a247253cea97c0)   18 |

## Macro Definition Documentation

## [◆ ](#a46ba8b903950b3ff8b04c8176e7844b5)RA\_ELC\_EVENT\_ACMPLP0\_INT

| #define RA\_ELC\_EVENT\_ACMPLP0\_INT   0x02F |
| --- |

## [◆ ](#a377a3e92bcdf0e45d2b12223ddd85666)RA\_ELC\_EVENT\_ACMPLP1\_INT

| #define RA\_ELC\_EVENT\_ACMPLP1\_INT   0x030 |
| --- |

## [◆ ](#af187c78a1f05fc4be81aa3af36e4cde5)RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH

| #define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH   0x02D |
| --- |

## [◆ ](#a65d6c499a6852434b4802f8ef7066eb4)RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH

| #define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH   0x02E |
| --- |

## [◆ ](#ad7284976213551f7d4fa450bf2bf8c7c)RA\_ELC\_EVENT\_ADC0\_SCAN\_END

| #define RA\_ELC\_EVENT\_ADC0\_SCAN\_END   0x029 |
| --- |

## [◆ ](#aecbe4efa29972b832e35ebb00d7499ad)RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B

| #define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B   0x02A |
| --- |

## [◆ ](#aa4feb2c3e29ba84d1397c618b7b860bf)RA\_ELC\_EVENT\_ADC0\_WINDOW\_A

| #define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A   0x02B |
| --- |

## [◆ ](#ab59c8ec4f20de5cf4709efe0a7ee70a1)RA\_ELC\_EVENT\_ADC0\_WINDOW\_B

| #define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B   0x02C |
| --- |

## [◆ ](#a015e6f8aed4b467f4554e6887b4d9ec9)RA\_ELC\_EVENT\_AGT0\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A   0x01F |
| --- |

## [◆ ](#ada1ad302dc5b987a6f7c972afae729f2)RA\_ELC\_EVENT\_AGT0\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B   0x020 |
| --- |

## [◆ ](#a4c3604a42ead1d43f472e901087ec148)RA\_ELC\_EVENT\_AGT0\_INT

| #define RA\_ELC\_EVENT\_AGT0\_INT   0x01E |
| --- |

## [◆ ](#aeb2399818b6b141ab4a37e257dba22be)RA\_ELC\_EVENT\_AGT1\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A   0x022 |
| --- |

## [◆ ](#a1d660c78348b48ea7a072225491ae44b)RA\_ELC\_EVENT\_AGT1\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B   0x023 |
| --- |

## [◆ ](#a635180e38c932579072f4eebd665592f)RA\_ELC\_EVENT\_AGT1\_INT

| #define RA\_ELC\_EVENT\_AGT1\_INT   0x021 |
| --- |

## [◆ ](#a6ec3edb5e4de5bca1171ade1aa9ca19f)RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR

| #define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR   0x047 |
| --- |

## [◆ ](#a1390ee9467a9d093de1532f0703ec35f)RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END

| #define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END   0x048 |
| --- |

## [◆ ](#a3463c1e202ab7891521eda7196e1be80)RA\_ELC\_EVENT\_CAC\_OVERFLOW

| #define RA\_ELC\_EVENT\_CAC\_OVERFLOW   0x049 |
| --- |

## [◆ ](#aa4f3b915e26ee83dcc8c383a1fdb2425)RA\_ELC\_EVENT\_CAN0\_ERROR

| #define RA\_ELC\_EVENT\_CAN0\_ERROR   0x04A |
| --- |

## [◆ ](#ad6e2ac69f8d10baa2d023e680e2f4c2f)RA\_ELC\_EVENT\_CAN0\_FIFO\_RX

| #define RA\_ELC\_EVENT\_CAN0\_FIFO\_RX   0x04B |
| --- |

## [◆ ](#a52d0f15f6d388658ae060aec6302b448)RA\_ELC\_EVENT\_CAN0\_FIFO\_TX

| #define RA\_ELC\_EVENT\_CAN0\_FIFO\_TX   0x04C |
| --- |

## [◆ ](#a0b017dad5f8642aa70f6f96c45e84a72)RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX

| #define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_RX   0x04D |
| --- |

## [◆ ](#a71880c5fc6363d67d8d126fd63a5354c)RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX

| #define RA\_ELC\_EVENT\_CAN0\_MAILBOX\_TX   0x04E |
| --- |

## [◆ ](#a290decf4254396cbce267cb52a619717)RA\_ELC\_EVENT\_CGC\_MOSC\_STOP

| #define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP   0x01C |
| --- |

## [◆ ](#acfe8138822bcd3f02fe50316e40c7641)RA\_ELC\_EVENT\_CTSU\_END

| #define RA\_ELC\_EVENT\_CTSU\_END   0x044 |
| --- |

## [◆ ](#ad7cd21f5db3e117b87ffab8a6cb47272)RA\_ELC\_EVENT\_CTSU\_READ

| #define RA\_ELC\_EVENT\_CTSU\_READ   0x043 |
| --- |

## [◆ ](#a2faf033bad7b355f8beb9386a2d0e93b)RA\_ELC\_EVENT\_CTSU\_WRITE

| #define RA\_ELC\_EVENT\_CTSU\_WRITE   0x042 |
| --- |

## [◆ ](#a906929a9ae7dd7de44d21a32d3635080)RA\_ELC\_EVENT\_DMAC0\_INT

| #define RA\_ELC\_EVENT\_DMAC0\_INT   0x011 |
| --- |

## [◆ ](#a76b9d9fa8af16a1480fcc8d8ec12572f)RA\_ELC\_EVENT\_DMAC1\_INT

| #define RA\_ELC\_EVENT\_DMAC1\_INT   0x012 |
| --- |

## [◆ ](#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)RA\_ELC\_EVENT\_DMAC2\_INT

| #define RA\_ELC\_EVENT\_DMAC2\_INT   0x013 |
| --- |

## [◆ ](#a0b9d72a41fd7c5b27e6c31967645b907)RA\_ELC\_EVENT\_DMAC3\_INT

| #define RA\_ELC\_EVENT\_DMAC3\_INT   0x014 |
| --- |

## [◆ ](#ab6c210d6481294137fd4bc32c39e5de1)RA\_ELC\_EVENT\_DOC\_INT

| #define RA\_ELC\_EVENT\_DOC\_INT   0x046 |
| --- |

## [◆ ](#a9a58e3a2c10447906aaf35bab5664d24)RA\_ELC\_EVENT\_DTC\_COMPLETE

| #define RA\_ELC\_EVENT\_DTC\_COMPLETE   0x015 |
| --- |

## [◆ ](#a5ab484cdaf470b47e95005d83d60394f)RA\_ELC\_EVENT\_DTC\_END

| #define RA\_ELC\_EVENT\_DTC\_END   0x016 |
| --- |

## [◆ ](#ae5c28618f4e68eef6ca83bdcec515abb)RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0

| #define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0   0x053 |
| --- |

## [◆ ](#a9f0b82bfff5ea2ba414ac0bccad9a34d)RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1

| #define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1   0x054 |
| --- |

## [◆ ](#a535af54c8bcfff47cc90ba1226044d71)RA\_ELC\_EVENT\_FCU\_FRDYI

| #define RA\_ELC\_EVENT\_FCU\_FRDYI   0x018 |
| --- |

## [◆ ](#aec8a8b590cc124ca12425f34b5a61020)RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A   0x057 |
| --- |

## [◆ ](#ae1ed91479f405ac965da868e86bce533)RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B   0x058 |
| --- |

## [◆ ](#a6d7c9090c21a8a0c497356050d649ec6)RA\_ELC\_EVENT\_GPT0\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_C   0x059 |
| --- |

## [◆ ](#af5b8ca097747bd987e81d8d81263aa81)RA\_ELC\_EVENT\_GPT0\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_D   0x05A |
| --- |

## [◆ ](#a9ebec21375578c0e52d953773373bf1e)RA\_ELC\_EVENT\_GPT0\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_E   0x05B |
| --- |

## [◆ ](#ad503a55a4548ff6ffd58e2b74d9eaf00)RA\_ELC\_EVENT\_GPT0\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_F   0x05C |
| --- |

## [◆ ](#a76692948000993fde4d286f1a521a6d2)RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW   0x05D |
| --- |

## [◆ ](#a9edde37b8c0835978aa55d58d77c5ad5)RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW   0x05E |
| --- |

## [◆ ](#a33a428565bfa3237aa4eda10b982fc65)RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A   0x05F |
| --- |

## [◆ ](#a5326aaf270290b524f8cb2e126d06602)RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B   0x060 |
| --- |

## [◆ ](#a2e55bae34ab30f2d802b8eaf93dd3cfd)RA\_ELC\_EVENT\_GPT1\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C   0x061 |
| --- |

## [◆ ](#ada3870f40beeec10e9366e908ed980d0)RA\_ELC\_EVENT\_GPT1\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D   0x062 |
| --- |

## [◆ ](#a5d4f72e95b7bb76315b9ffa059730620)RA\_ELC\_EVENT\_GPT1\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E   0x063 |
| --- |

## [◆ ](#a548923b7385648e4f15fef4ecb315478)RA\_ELC\_EVENT\_GPT1\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F   0x064 |
| --- |

## [◆ ](#aa6eac7cf283073eea62fbaa1df2017f2)RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW   0x065 |
| --- |

## [◆ ](#ae8cefd5f23897d43cffba4e91b7c8b5c)RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW   0x066 |
| --- |

## [◆ ](#ad1a5796e0c70a988165765f2ce8c1e80)RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A   0x067 |
| --- |

## [◆ ](#a73776ba7d66a478c92c6cb3dfed50af4)RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B   0x068 |
| --- |

## [◆ ](#aa391fa888ded57351c9b62f54df1ce36)RA\_ELC\_EVENT\_GPT2\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C   0x069 |
| --- |

## [◆ ](#a90c7aa7bbddb04e6ae4b6eccb64a0e93)RA\_ELC\_EVENT\_GPT2\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D   0x06A |
| --- |

## [◆ ](#adbfb562e616a86a3e28f8c3f09553db9)RA\_ELC\_EVENT\_GPT2\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E   0x06B |
| --- |

## [◆ ](#a6f07945c82efae23754e34dc09bee884)RA\_ELC\_EVENT\_GPT2\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F   0x06C |
| --- |

## [◆ ](#aede7879166ef812139641122782d873b)RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW   0x06D |
| --- |

## [◆ ](#ad71d20ad5434f219a61e0f0aded090d1)RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW   0x06E |
| --- |

## [◆ ](#a74526500dfb573fe21fbca739b1698e1)RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A   0x06F |
| --- |

## [◆ ](#ac6cfac3496e4ab71c9bf84b43e06486a)RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B   0x070 |
| --- |

## [◆ ](#a1af4840d468eb4c4e1672a34652ef583)RA\_ELC\_EVENT\_GPT3\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_C   0x071 |
| --- |

## [◆ ](#a263e6b02601dd37d6eedaab56a2e6fcd)RA\_ELC\_EVENT\_GPT3\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_D   0x072 |
| --- |

## [◆ ](#a9035e080d39d60ecc898a596b9902aa6)RA\_ELC\_EVENT\_GPT3\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_E   0x073 |
| --- |

## [◆ ](#a9cffb5aca60a4c7349789fc23fb197fb)RA\_ELC\_EVENT\_GPT3\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_F   0x074 |
| --- |

## [◆ ](#a546eff128c44a29f56fe90952cef475d)RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW   0x075 |
| --- |

## [◆ ](#ab30a5683e48535abbf0c400a5a0d8946)RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW   0x076 |
| --- |

## [◆ ](#a8130aa176d9d5dd698c62708111515e0)RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A   0x077 |
| --- |

## [◆ ](#aa77a30a219070d15e358a43fbbd89728)RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B   0x078 |
| --- |

## [◆ ](#af6c1cb172b343baa8d8bbe01d1674922)RA\_ELC\_EVENT\_GPT4\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C   0x079 |
| --- |

## [◆ ](#ae8c7945c641045c615922a3f82329c56)RA\_ELC\_EVENT\_GPT4\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D   0x07A |
| --- |

## [◆ ](#afcb271a94d9b07b7b1a204f325b80d52)RA\_ELC\_EVENT\_GPT4\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E   0x07B |
| --- |

## [◆ ](#a906eb0e1ed2786ed2b14e4608489b2cc)RA\_ELC\_EVENT\_GPT4\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F   0x07C |
| --- |

## [◆ ](#abb820eb80ad8afc5c12dc3581fc7a0b9)RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW   0x07D |
| --- |

## [◆ ](#a65831ae6b037607dc55a2b1e8aa296a7)RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW   0x07E |
| --- |

## [◆ ](#adc4aceff99f296b06938254f9dcc1f2f)RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A   0x07F |
| --- |

## [◆ ](#aad1fc8b32dffaaa64f9908951f8b1c64)RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B   0x080 |
| --- |

## [◆ ](#aebaa50f4643efe5b87798777cee578bc)RA\_ELC\_EVENT\_GPT5\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C   0x081 |
| --- |

## [◆ ](#a21965e21bd4045aa5010925620b4d827)RA\_ELC\_EVENT\_GPT5\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D   0x082 |
| --- |

## [◆ ](#a51a7cb146f0efbb7bc9f7336031006a4)RA\_ELC\_EVENT\_GPT5\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E   0x083 |
| --- |

## [◆ ](#abbd0bd21af2bd1679d6d7bc36001b97d)RA\_ELC\_EVENT\_GPT5\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F   0x084 |
| --- |

## [◆ ](#a038e7580f03fbdd74f417108cd2a8b4d)RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW   0x085 |
| --- |

## [◆ ](#ac38b8f1154d6a699923b2bbf249e38fd)RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW   0x086 |
| --- |

## [◆ ](#acad1c37929903ddee569f40a3c5c59e3)RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A   0x087 |
| --- |

## [◆ ](#aa0fc9b447efbcba0bb6800f785daeb96)RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B   0x088 |
| --- |

## [◆ ](#a01f586bd98832ea9b8aa58741b61a319)RA\_ELC\_EVENT\_GPT6\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT6\_COMPARE\_C   0x089 |
| --- |

## [◆ ](#acd71c3b8e8e1d96aa3ff6affb93f5000)RA\_ELC\_EVENT\_GPT6\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT6\_COMPARE\_D   0x08A |
| --- |

## [◆ ](#a6abdcc7a6331a8283cfe0c1ac06b7d83)RA\_ELC\_EVENT\_GPT6\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT6\_COMPARE\_E   0x08B |
| --- |

## [◆ ](#a28b6b55ad533e3cb606b2b0937c916b3)RA\_ELC\_EVENT\_GPT6\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT6\_COMPARE\_F   0x08C |
| --- |

## [◆ ](#ac3c8dd6a5b7f95dccc58e7ec4e235a40)RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW   0x08D |
| --- |

## [◆ ](#acdece33585a75fccba962e4f764058fb)RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW   0x08E |
| --- |

## [◆ ](#afe1b39e5d37a5ed631dd18869cfbac8a)RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A   0x08F |
| --- |

## [◆ ](#a53b7cfc8d0a000bd57f159b09b0a9c26)RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B   0x090 |
| --- |

## [◆ ](#add91262eba9ec860b788030af153161a)RA\_ELC\_EVENT\_GPT7\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT7\_COMPARE\_C   0x091 |
| --- |

## [◆ ](#a9310fd708ca6f0afcf374bfc96e22e6e)RA\_ELC\_EVENT\_GPT7\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT7\_COMPARE\_D   0x092 |
| --- |

## [◆ ](#a8d18bd54c972d1de01c2a9f86e832cd0)RA\_ELC\_EVENT\_GPT7\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT7\_COMPARE\_E   0x093 |
| --- |

## [◆ ](#aca89f90e8afa3f656e76f5960717543c)RA\_ELC\_EVENT\_GPT7\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT7\_COMPARE\_F   0x094 |
| --- |

## [◆ ](#aac0ed7abde81cf4bcc7588bf64b53c04)RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW   0x095 |
| --- |

## [◆ ](#ab1935670b6c0a5b5629ef8ba9d854f6c)RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW   0x096 |
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

## [◆ ](#ada7702d0ac50f9b3e82ef50d6be50470)RA\_ELC\_EVENT\_ICU\_IRQ14

| #define RA\_ELC\_EVENT\_ICU\_IRQ14   0x00F |
| --- |

## [◆ ](#afab294cf0d58a5bb4dd578774b0ad9aa)RA\_ELC\_EVENT\_ICU\_IRQ15

| #define RA\_ELC\_EVENT\_ICU\_IRQ15   0x010 |
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

| #define RA\_ELC\_EVENT\_ICU\_SNOOZE\_CANCEL   0x017 |
| --- |

## [◆ ](#a667eb763b55f973b141837e82dbbae6e)RA\_ELC\_EVENT\_IIC0\_ERI

| #define RA\_ELC\_EVENT\_IIC0\_ERI   0x038 |
| --- |

## [◆ ](#a7271a25cdc3c987313efbafcd2a746cf)RA\_ELC\_EVENT\_IIC0\_RXI

| #define RA\_ELC\_EVENT\_IIC0\_RXI   0x035 |
| --- |

## [◆ ](#a52270344b26073c127a0269c5ec4e228)RA\_ELC\_EVENT\_IIC0\_TEI

| #define RA\_ELC\_EVENT\_IIC0\_TEI   0x037 |
| --- |

## [◆ ](#a7843f8a23feb383202fa6ad3be8fae5c)RA\_ELC\_EVENT\_IIC0\_TXI

| #define RA\_ELC\_EVENT\_IIC0\_TXI   0x036 |
| --- |

## [◆ ](#a2a074dab614a1639ea5fa4f6d3baffd3)RA\_ELC\_EVENT\_IIC0\_WUI

| #define RA\_ELC\_EVENT\_IIC0\_WUI   0x039 |
| --- |

## [◆ ](#a2221a129f0e323fa5b96bfe5ed0e007f)RA\_ELC\_EVENT\_IIC1\_ERI

| #define RA\_ELC\_EVENT\_IIC1\_ERI   0x03D |
| --- |

## [◆ ](#ad03e6b81d0e7ce53737e5c3022f8d951)RA\_ELC\_EVENT\_IIC1\_RXI

| #define RA\_ELC\_EVENT\_IIC1\_RXI   0x03A |
| --- |

## [◆ ](#a45ed226ccaace8813aa653276a52999d)RA\_ELC\_EVENT\_IIC1\_TEI

| #define RA\_ELC\_EVENT\_IIC1\_TEI   0x03C |
| --- |

## [◆ ](#a641c91157c98f41d3cf5ff6bbe25192d)RA\_ELC\_EVENT\_IIC1\_TXI

| #define RA\_ELC\_EVENT\_IIC1\_TXI   0x03B |
| --- |

## [◆ ](#aee58e9a0c4313f0ec08f0652e5002008)RA\_ELC\_EVENT\_IOPORT\_EVENT\_1

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1   0x04F |
| --- |

## [◆ ](#a36d858520d28847eead0fbfe7950be2d)RA\_ELC\_EVENT\_IOPORT\_EVENT\_2

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2   0x050 |
| --- |

## [◆ ](#a545dadce70bbcea1116cd13490fe2571)RA\_ELC\_EVENT\_IOPORT\_EVENT\_3

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_3   0x051 |
| --- |

## [◆ ](#a4e478b84ef99ae71c102ad3d5c71089a)RA\_ELC\_EVENT\_IOPORT\_EVENT\_4

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_4   0x052 |
| --- |

## [◆ ](#abc837f1fcfffeb2ec231c79336379dda)RA\_ELC\_EVENT\_IWDT\_UNDERFLOW

| #define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW   0x024 |
| --- |

## [◆ ](#a4412a0ec84a10d14d131754c5f9eb509)RA\_ELC\_EVENT\_KEY\_INT

| #define RA\_ELC\_EVENT\_KEY\_INT   0x045 |
| --- |

## [◆ ](#ac6953f0c8caa6b5ef8c9893c7ff4baa1)RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST

| #define RA\_ELC\_EVENT\_LPM\_SNOOZE\_REQUEST   0x01D |
| --- |

## [◆ ](#a7ab275777147d06315a04abb3f2f6d51)RA\_ELC\_EVENT\_LVD\_LVD1

| #define RA\_ELC\_EVENT\_LVD\_LVD1   0x019 |
| --- |

## [◆ ](#ad52acadba107b7f907d678f44769a4cb)RA\_ELC\_EVENT\_LVD\_LVD2

| #define RA\_ELC\_EVENT\_LVD\_LVD2   0x01A |
| --- |

## [◆ ](#a1ab4e1434620d962450d98c0fee2f89c)RA\_ELC\_EVENT\_LVD\_VBATT

| #define RA\_ELC\_EVENT\_LVD\_VBATT   0x01B |
| --- |

## [◆ ](#a11b5cec97472328120a8d6381f1e8809)RA\_ELC\_EVENT\_NONE

| #define RA\_ELC\_EVENT\_NONE   0x0 |
| --- |

## [◆ ](#a8438d8d92e1950681388b40385a2c354)RA\_ELC\_EVENT\_OPS\_UVW\_EDGE

| #define RA\_ELC\_EVENT\_OPS\_UVW\_EDGE   0x097 |
| --- |

## [◆ ](#a81e18423a1f61e34f0daab6f7367eae2)RA\_ELC\_EVENT\_POEG0\_EVENT

| #define RA\_ELC\_EVENT\_POEG0\_EVENT   0x055 |
| --- |

## [◆ ](#a2a43c2ce461fde766e66a4451929a875)RA\_ELC\_EVENT\_POEG1\_EVENT

| #define RA\_ELC\_EVENT\_POEG1\_EVENT   0x056 |
| --- |

## [◆ ](#a76fd68b555574159d563d2dfd68d90b9)RA\_ELC\_EVENT\_RTC\_ALARM

| #define RA\_ELC\_EVENT\_RTC\_ALARM   0x026 |
| --- |

## [◆ ](#a241cd3c65033b46a1160d5815cc86fd7)RA\_ELC\_EVENT\_RTC\_CARRY

| #define RA\_ELC\_EVENT\_RTC\_CARRY   0x028 |
| --- |

## [◆ ](#a144901ee7b31b96eba18a39d98c4b953)RA\_ELC\_EVENT\_RTC\_PERIOD

| #define RA\_ELC\_EVENT\_RTC\_PERIOD   0x027 |
| --- |

## [◆ ](#ae2373b571584dae4d1c7fc57142ecb3c)RA\_ELC\_EVENT\_SCI0\_AM

| #define RA\_ELC\_EVENT\_SCI0\_AM   0x09C |
| --- |

## [◆ ](#ad4580e769bae423298276e31ee2ee071)RA\_ELC\_EVENT\_SCI0\_ERI

| #define RA\_ELC\_EVENT\_SCI0\_ERI   0x09B |
| --- |

## [◆ ](#ad9e9a8451a683c5b5bc8a2ace8264c27)RA\_ELC\_EVENT\_SCI0\_RXI

| #define RA\_ELC\_EVENT\_SCI0\_RXI   0x098 |
| --- |

## [◆ ](#ad52a4c7660a4e609976f7045305f8ca7)RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI

| #define RA\_ELC\_EVENT\_SCI0\_RXI\_OR\_ERI   0x09D |
| --- |

## [◆ ](#ae845a850ab730c651badc5c857e28ee9)RA\_ELC\_EVENT\_SCI0\_TEI

| #define RA\_ELC\_EVENT\_SCI0\_TEI   0x09A |
| --- |

## [◆ ](#aecc4fdda2a7eeb2bab0b894f2e5047d9)RA\_ELC\_EVENT\_SCI0\_TXI

| #define RA\_ELC\_EVENT\_SCI0\_TXI   0x099 |
| --- |

## [◆ ](#ad9ca7dbcac36bb7f921cd8b8db761623)RA\_ELC\_EVENT\_SCI1\_AM

| #define RA\_ELC\_EVENT\_SCI1\_AM   0x0A2 |
| --- |

## [◆ ](#a6a673466eb5261d23ee06be132ca9cde)RA\_ELC\_EVENT\_SCI1\_ERI

| #define RA\_ELC\_EVENT\_SCI1\_ERI   0x0A1 |
| --- |

## [◆ ](#ae936e9aa971a376cb4ea3405c68d57f0)RA\_ELC\_EVENT\_SCI1\_RXI

| #define RA\_ELC\_EVENT\_SCI1\_RXI   0x09E |
| --- |

## [◆ ](#aae0ca4a1031af4c490fbb1ecbe201662)RA\_ELC\_EVENT\_SCI1\_TEI

| #define RA\_ELC\_EVENT\_SCI1\_TEI   0x0A0 |
| --- |

## [◆ ](#abd1c6187f97f2817dc5eb59278a996b1)RA\_ELC\_EVENT\_SCI1\_TXI

| #define RA\_ELC\_EVENT\_SCI1\_TXI   0x09F |
| --- |

## [◆ ](#a023110baac3b030238844ab6a8999652)RA\_ELC\_EVENT\_SCI2\_AM

| #define RA\_ELC\_EVENT\_SCI2\_AM   0x0A7 |
| --- |

## [◆ ](#ad31428c7900c978dba266761df793f4c)RA\_ELC\_EVENT\_SCI2\_ERI

| #define RA\_ELC\_EVENT\_SCI2\_ERI   0x0A6 |
| --- |

## [◆ ](#a484b0928fab1e96f3008b9e7b12bab07)RA\_ELC\_EVENT\_SCI2\_RXI

| #define RA\_ELC\_EVENT\_SCI2\_RXI   0x0A3 |
| --- |

## [◆ ](#a9bbdd2f449bfd5709f6c8b77b8378ca4)RA\_ELC\_EVENT\_SCI2\_TEI

| #define RA\_ELC\_EVENT\_SCI2\_TEI   0x0A5 |
| --- |

## [◆ ](#a5991f7636af52ea3285cf17d300f62bb)RA\_ELC\_EVENT\_SCI2\_TXI

| #define RA\_ELC\_EVENT\_SCI2\_TXI   0x0A4 |
| --- |

## [◆ ](#a2bfc7def09c933262aa530227a45af7d)RA\_ELC\_EVENT\_SCI9\_AM

| #define RA\_ELC\_EVENT\_SCI9\_AM   0x0AC |
| --- |

## [◆ ](#af2e4d2d6b59c512e536d901789b3c1a2)RA\_ELC\_EVENT\_SCI9\_ERI

| #define RA\_ELC\_EVENT\_SCI9\_ERI   0x0AB |
| --- |

## [◆ ](#ac01e51a9360f409e430642d86818bf98)RA\_ELC\_EVENT\_SCI9\_RXI

| #define RA\_ELC\_EVENT\_SCI9\_RXI   0x0A8 |
| --- |

## [◆ ](#ac3a064375ff90f3a6a35c5fdda680f95)RA\_ELC\_EVENT\_SCI9\_TEI

| #define RA\_ELC\_EVENT\_SCI9\_TEI   0x0AA |
| --- |

## [◆ ](#a8c628c59b08ed53781fd406ea22da796)RA\_ELC\_EVENT\_SCI9\_TXI

| #define RA\_ELC\_EVENT\_SCI9\_TXI   0x0A9 |
| --- |

## [◆ ](#ab588fafc974153bcf94087cdb1a71d73)RA\_ELC\_EVENT\_SPI0\_ERI

| #define RA\_ELC\_EVENT\_SPI0\_ERI   0x0B0 |
| --- |

## [◆ ](#a920575ee3a202b0d7202cd053f1e235b)RA\_ELC\_EVENT\_SPI0\_IDLE

| #define RA\_ELC\_EVENT\_SPI0\_IDLE   0x0AF |
| --- |

## [◆ ](#af77608914a79bea7797b63674c71db31)RA\_ELC\_EVENT\_SPI0\_RXI

| #define RA\_ELC\_EVENT\_SPI0\_RXI   0x0AD |
| --- |

## [◆ ](#a368a0ece3d89efe3ed8ab274471849b9)RA\_ELC\_EVENT\_SPI0\_TEI

| #define RA\_ELC\_EVENT\_SPI0\_TEI   0x0B1 |
| --- |

## [◆ ](#a82d87016b5d694884bba33bf71e93e92)RA\_ELC\_EVENT\_SPI0\_TXI

| #define RA\_ELC\_EVENT\_SPI0\_TXI   0x0AE |
| --- |

## [◆ ](#aedf36efaaba39c4001386536d21f81e2)RA\_ELC\_EVENT\_SPI1\_ERI

| #define RA\_ELC\_EVENT\_SPI1\_ERI   0x0B5 |
| --- |

## [◆ ](#a73da76e435d9de6b6b7ad48190d2c0a2)RA\_ELC\_EVENT\_SPI1\_IDLE

| #define RA\_ELC\_EVENT\_SPI1\_IDLE   0x0B4 |
| --- |

## [◆ ](#a2f5e3b5957e42c572fda94ec535b401b)RA\_ELC\_EVENT\_SPI1\_RXI

| #define RA\_ELC\_EVENT\_SPI1\_RXI   0x0B2 |
| --- |

## [◆ ](#a60f40983e3c6344a257bd157b40069d5)RA\_ELC\_EVENT\_SPI1\_TEI

| #define RA\_ELC\_EVENT\_SPI1\_TEI   0x0B6 |
| --- |

## [◆ ](#a0aab8e60c14b34bccb74400a818524ac)RA\_ELC\_EVENT\_SPI1\_TXI

| #define RA\_ELC\_EVENT\_SPI1\_TXI   0x0B3 |
| --- |

## [◆ ](#a1a89e9ab6abb3834992ee3ea3ebaf9c4)RA\_ELC\_EVENT\_SSI0\_INT

| #define RA\_ELC\_EVENT\_SSI0\_INT   0x041 |
| --- |

## [◆ ](#ab736656ae0b06de8383189075cbb2f27)RA\_ELC\_EVENT\_SSI0\_RXI

| #define RA\_ELC\_EVENT\_SSI0\_RXI   0x03F |
| --- |

## [◆ ](#ac65193048ce5734b46bc2bf77b84cb4e)RA\_ELC\_EVENT\_SSI0\_TXI

| #define RA\_ELC\_EVENT\_SSI0\_TXI   0x03E |
| --- |

## [◆ ](#ae4dbb89c58220f72818cc9c28d97905b)RA\_ELC\_EVENT\_USBFS\_FIFO\_0

| #define RA\_ELC\_EVENT\_USBFS\_FIFO\_0   0x031 |
| --- |

## [◆ ](#a0ef2efa2ea339cad7598f11fe549cdd9)RA\_ELC\_EVENT\_USBFS\_FIFO\_1

| #define RA\_ELC\_EVENT\_USBFS\_FIFO\_1   0x032 |
| --- |

## [◆ ](#aac8d97813e8a3276bdac764faf7b580d)RA\_ELC\_EVENT\_USBFS\_INT

| #define RA\_ELC\_EVENT\_USBFS\_INT   0x033 |
| --- |

## [◆ ](#a9458dbf2b1da6fc51ca2c2933dcb6b37)RA\_ELC\_EVENT\_USBFS\_RESUME

| #define RA\_ELC\_EVENT\_USBFS\_RESUME   0x034 |
| --- |

## [◆ ](#a6cdb7a60a850f9ec23f19c548a6cc544)RA\_ELC\_EVENT\_WDT\_UNDERFLOW

| #define RA\_ELC\_EVENT\_WDT\_UNDERFLOW   0x025 |
| --- |

## [◆ ](#a2b5a9232a4ad9d199dc9baa510d0ed54)RA\_ELC\_PERIPHERAL\_ADC0

| #define RA\_ELC\_PERIPHERAL\_ADC0   8 |
| --- |

## [◆ ](#afaf4059726139d62e2c09010cfa1148a)RA\_ELC\_PERIPHERAL\_ADC0\_B

| #define RA\_ELC\_PERIPHERAL\_ADC0\_B   9 |
| --- |

## [◆ ](#a66a60a7a3469054498a247253cea97c0)RA\_ELC\_PERIPHERAL\_CTSU

| #define RA\_ELC\_PERIPHERAL\_CTSU   18 |
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
- [ra4m1-elc.h](ra4m1-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
