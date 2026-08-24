---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ra8d1-elc_8h.html
original_path: doxygen/html/ra8d1-elc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ra8d1-elc.h File Reference

[Go to the source code of this file.](ra8d1-elc_8h_source.md)

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
| #define | [RA\_ELC\_EVENT\_ICU\_IRQ15](#afab294cf0d58a5bb4dd578774b0ad9aa)   0x010 |
| #define | [RA\_ELC\_EVENT\_DMAC0\_INT](#a906929a9ae7dd7de44d21a32d3635080)   0x011 |
| #define | [RA\_ELC\_EVENT\_DMAC1\_INT](#a76b9d9fa8af16a1480fcc8d8ec12572f)   0x012 |
| #define | [RA\_ELC\_EVENT\_DMAC2\_INT](#ab6e39dbf43a7b7c8c26afbebbcd1a2ed)   0x013 |
| #define | [RA\_ELC\_EVENT\_DMAC3\_INT](#a0b9d72a41fd7c5b27e6c31967645b907)   0x014 |
| #define | [RA\_ELC\_EVENT\_DMAC4\_INT](#a4cae5afbbe49719555bbbfa12b8727f5)   0x015 |
| #define | [RA\_ELC\_EVENT\_DMAC5\_INT](#a000e31aba8a821f4358a435d280b3a7b)   0x016 |
| #define | [RA\_ELC\_EVENT\_DMAC6\_INT](#a2d1f6d1c797a0d787a5d5c08b0fc18ad)   0x017 |
| #define | [RA\_ELC\_EVENT\_DMAC7\_INT](#ae8caef45a510d4c4f1c55f923e01799e)   0x018 |
| #define | [RA\_ELC\_EVENT\_DTC\_END](#a5ab484cdaf470b47e95005d83d60394f)   0x021 |
| #define | [RA\_ELC\_EVENT\_DTC\_COMPLETE](#a9a58e3a2c10447906aaf35bab5664d24)   0x022 |
| #define | [RA\_ELC\_EVENT\_DMA\_TRANSERR](#a54d8c74eefe8f9b237ea23e18033d947)   0x027 |
| #define | [RA\_ELC\_EVENT\_DBG\_CTIIRQ0](#a0d740efcf6ca4778a2f8a9e9bd7c11c9)   0x029 |
| #define | [RA\_ELC\_EVENT\_DBG\_CTIIRQ1](#ab33d581df4d34b8ee361ea4e1e690ed3)   0x02A |
| #define | [RA\_ELC\_EVENT\_DBG\_JBRXI](#a0494be0bf55e1e687e2f4c0e0f0d93aa)   0x02B |
| #define | [RA\_ELC\_EVENT\_FCU\_FIFERR](#a5c7545a2f69856b7b637ad690f158b77)   0x030 |
| #define | [RA\_ELC\_EVENT\_FCU\_FRDYI](#a535af54c8bcfff47cc90ba1226044d71)   0x031 |
| #define | [RA\_ELC\_EVENT\_LVD\_LVD1](#a7ab275777147d06315a04abb3f2f6d51)   0x038 |
| #define | [RA\_ELC\_EVENT\_LVD\_LVD2](#ad52acadba107b7f907d678f44769a4cb)   0x039 |
| #define | [RA\_ELC\_EVENT\_VBATT\_TADI](#a61f5922105d7d213f9c4dba773a1252f)   0x03D |
| #define | [RA\_ELC\_EVENT\_CGC\_MOSC\_STOP](#a290decf4254396cbce267cb52a619717)   0x03E |
| #define | [RA\_ELC\_EVENT\_ULPT0\_INT](#aecaa6cbbfd3a5e0007a00fd11edc204d)   0x040 |
| #define | [RA\_ELC\_EVENT\_ULPT0\_COMPARE\_A](#a69ec3e618136c55cebeb2d76fc2e88ba)   0x041 |
| #define | [RA\_ELC\_EVENT\_ULPT0\_COMPARE\_B](#ac954387c6092e77e6002997f93e4d10e)   0x042 |
| #define | [RA\_ELC\_EVENT\_ULPT1\_INT](#ac313fdd1b0179ee96d36532504592305)   0x043 |
| #define | [RA\_ELC\_EVENT\_ULPT1\_COMPARE\_A](#a77531873ba01d812a3f5614059016cf6)   0x044 |
| #define | [RA\_ELC\_EVENT\_ULPT1\_COMPARE\_B](#aadb4d755431beb28984de1e962402a39)   0x045 |
| #define | [RA\_ELC\_EVENT\_AGT0\_INT](#a4c3604a42ead1d43f472e901087ec148)   0x046 |
| #define | [RA\_ELC\_EVENT\_AGT0\_COMPARE\_A](#a015e6f8aed4b467f4554e6887b4d9ec9)   0x047 |
| #define | [RA\_ELC\_EVENT\_AGT0\_COMPARE\_B](#ada1ad302dc5b987a6f7c972afae729f2)   0x048 |
| #define | [RA\_ELC\_EVENT\_AGT1\_INT](#a635180e38c932579072f4eebd665592f)   0x049 |
| #define | [RA\_ELC\_EVENT\_AGT1\_COMPARE\_A](#aeb2399818b6b141ab4a37e257dba22be)   0x04A |
| #define | [RA\_ELC\_EVENT\_AGT1\_COMPARE\_B](#a1d660c78348b48ea7a072225491ae44b)   0x04B |
| #define | [RA\_ELC\_EVENT\_IWDT\_UNDERFLOW](#abc837f1fcfffeb2ec231c79336379dda)   0x052 |
| #define | [RA\_ELC\_EVENT\_WDT0\_UNDERFLOW](#aef90868206c735f311c2f95644f562b1)   0x053 |
| #define | [RA\_ELC\_EVENT\_RTC\_ALARM](#a76fd68b555574159d563d2dfd68d90b9)   0x055 |
| #define | [RA\_ELC\_EVENT\_RTC\_PERIOD](#a144901ee7b31b96eba18a39d98c4b953)   0x056 |
| #define | [RA\_ELC\_EVENT\_RTC\_CARRY](#a241cd3c65033b46a1160d5815cc86fd7)   0x057 |
| #define | [RA\_ELC\_EVENT\_USBFS\_FIFO\_0](#ae4dbb89c58220f72818cc9c28d97905b)   0x058 |
| #define | [RA\_ELC\_EVENT\_USBFS\_FIFO\_1](#a0ef2efa2ea339cad7598f11fe549cdd9)   0x059 |
| #define | [RA\_ELC\_EVENT\_USBFS\_INT](#aac8d97813e8a3276bdac764faf7b580d)   0x05A |
| #define | [RA\_ELC\_EVENT\_USBFS\_RESUME](#a9458dbf2b1da6fc51ca2c2933dcb6b37)   0x05B |
| #define | [RA\_ELC\_EVENT\_IIC0\_RXI](#a7271a25cdc3c987313efbafcd2a746cf)   0x05C |
| #define | [RA\_ELC\_EVENT\_IIC0\_TXI](#a7843f8a23feb383202fa6ad3be8fae5c)   0x05D |
| #define | [RA\_ELC\_EVENT\_IIC0\_TEI](#a52270344b26073c127a0269c5ec4e228)   0x05E |
| #define | [RA\_ELC\_EVENT\_IIC0\_ERI](#a667eb763b55f973b141837e82dbbae6e)   0x05F |
| #define | [RA\_ELC\_EVENT\_IIC0\_WUI](#a2a074dab614a1639ea5fa4f6d3baffd3)   0x060 |
| #define | [RA\_ELC\_EVENT\_IIC1\_RXI](#ad03e6b81d0e7ce53737e5c3022f8d951)   0x061 |
| #define | [RA\_ELC\_EVENT\_IIC1\_TXI](#a641c91157c98f41d3cf5ff6bbe25192d)   0x062 |
| #define | [RA\_ELC\_EVENT\_IIC1\_TEI](#a45ed226ccaace8813aa653276a52999d)   0x063 |
| #define | [RA\_ELC\_EVENT\_IIC1\_ERI](#a2221a129f0e323fa5b96bfe5ed0e007f)   0x064 |
| #define | [RA\_ELC\_EVENT\_SDHIMMC0\_ACCS](#a5d9c7d15a5c040aa9dfe002cf9df0657)   0x06B |
| #define | [RA\_ELC\_EVENT\_SDHIMMC0\_SDIO](#a93465058fd23dad3a735a53ad8689473)   0x06C |
| #define | [RA\_ELC\_EVENT\_SDHIMMC0\_CARD](#a2bf8474e011e2ec0360e9e46deb7e960)   0x06D |
| #define | [RA\_ELC\_EVENT\_SDHIMMC0\_DMA\_REQ](#a937bfe3314fb8d78775078db983ea473)   0x06E |
| #define | [RA\_ELC\_EVENT\_SDHIMMC1\_ACCS](#a7195add88b927dd230e66a931713f4e0)   0x06F |
| #define | [RA\_ELC\_EVENT\_SDHIMMC1\_SDIO](#a2dff7e869fad7918164e954bcb0a46bf)   0x070 |
| #define | [RA\_ELC\_EVENT\_SDHIMMC1\_CARD](#ae8b2102091696bca7f60b008b9839444)   0x071 |
| #define | [RA\_ELC\_EVENT\_SDHIMMC1\_DMA\_REQ](#a3b619f3e51ddcf2add17abd434bbf948)   0x072 |
| #define | [RA\_ELC\_EVENT\_SSI0\_TXI](#ac65193048ce5734b46bc2bf77b84cb4e)   0x073 |
| #define | [RA\_ELC\_EVENT\_SSI0\_RXI](#ab736656ae0b06de8383189075cbb2f27)   0x074 |
| #define | [RA\_ELC\_EVENT\_SSI0\_INT](#a1a89e9ab6abb3834992ee3ea3ebaf9c4)   0x076 |
| #define | [RA\_ELC\_EVENT\_SSI1\_TXI\_RXI](#a202b4f22442dfef11d4402c41cdbb978)   0x079 |
| #define | [RA\_ELC\_EVENT\_SSI1\_TXI](#a209699f601f2f9f29a44b2d1ee33713d)   0x079 |
| #define | [RA\_ELC\_EVENT\_SSI1\_RXI](#a6c41f242f807ea904423f537d87b4df2)   0x079 |
| #define | [RA\_ELC\_EVENT\_SSI1\_INT](#a79f16ecce139415dc0c4b975bccc7f11)   0x07A |
| #define | [RA\_ELC\_EVENT\_ACMPHS0\_INT](#a3bbee94907736c0c435cc5ff64d1e7ef)   0x07B |
| #define | [RA\_ELC\_EVENT\_ACMPHS1\_INT](#ab1a4d1aee4743a0ee8bd194052a6c840)   0x07C |
| #define | [RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0](#ae5c28618f4e68eef6ca83bdcec515abb)   0x083 |
| #define | [RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1](#a9f0b82bfff5ea2ba414ac0bccad9a34d)   0x084 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_1](#aee58e9a0c4313f0ec08f0652e5002008)   0x088 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_2](#a36d858520d28847eead0fbfe7950be2d)   0x089 |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_3](#a545dadce70bbcea1116cd13490fe2571)   0x08A |
| #define | [RA\_ELC\_EVENT\_IOPORT\_EVENT\_4](#a4e478b84ef99ae71c102ad3d5c71089a)   0x08B |
| #define | [RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR](#a6ec3edb5e4de5bca1171ade1aa9ca19f)   0x08C |
| #define | [RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END](#a1390ee9467a9d093de1532f0703ec35f)   0x08D |
| #define | [RA\_ELC\_EVENT\_CAC\_OVERFLOW](#a3463c1e202ab7891521eda7196e1be80)   0x08E |
| #define | [RA\_ELC\_EVENT\_POEG0\_EVENT](#a81e18423a1f61e34f0daab6f7367eae2)   0x08F |
| #define | [RA\_ELC\_EVENT\_POEG1\_EVENT](#a2a43c2ce461fde766e66a4451929a875)   0x090 |
| #define | [RA\_ELC\_EVENT\_POEG2\_EVENT](#a7b5c16202b2491ba77319a180bcaa107)   0x091 |
| #define | [RA\_ELC\_EVENT\_POEG3\_EVENT](#ab39d06b130b93348c5fab589f1e0074e)   0x092 |
| #define | [RA\_ELC\_EVENT\_OPS\_UVW\_EDGE](#a8438d8d92e1950681388b40385a2c354)   0x0A0 |
| #define | [RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A](#aec8a8b590cc124ca12425f34b5a61020)   0x0A1 |
| #define | [RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B](#ae1ed91479f405ac965da868e86bce533)   0x0A2 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_C](#a6d7c9090c21a8a0c497356050d649ec6)   0x0A3 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_D](#af5b8ca097747bd987e81d8d81263aa81)   0x0A4 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_E](#a9ebec21375578c0e52d953773373bf1e)   0x0A5 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COMPARE\_F](#ad503a55a4548ff6ffd58e2b74d9eaf00)   0x0A6 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW](#a76692948000993fde4d286f1a521a6d2)   0x0A7 |
| #define | [RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW](#a9edde37b8c0835978aa55d58d77c5ad5)   0x0A8 |
| #define | [RA\_ELC\_EVENT\_GPT0\_PC](#a21a934c940f85a7e4e592167eb468fd3)   0x0A9 |
| #define | [RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A](#a33a428565bfa3237aa4eda10b982fc65)   0x0AA |
| #define | [RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B](#a5326aaf270290b524f8cb2e126d06602)   0x0AB |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_C](#a2e55bae34ab30f2d802b8eaf93dd3cfd)   0x0AC |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_D](#ada3870f40beeec10e9366e908ed980d0)   0x0AD |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_E](#a5d4f72e95b7bb76315b9ffa059730620)   0x0AE |
| #define | [RA\_ELC\_EVENT\_GPT1\_COMPARE\_F](#a548923b7385648e4f15fef4ecb315478)   0x0AF |
| #define | [RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW](#aa6eac7cf283073eea62fbaa1df2017f2)   0x0B0 |
| #define | [RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW](#ae8cefd5f23897d43cffba4e91b7c8b5c)   0x0B1 |
| #define | [RA\_ELC\_EVENT\_GPT1\_PC](#aa0208084abba3e2601c8cf7bb42837fd)   0x0B2 |
| #define | [RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A](#ad1a5796e0c70a988165765f2ce8c1e80)   0x0B3 |
| #define | [RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B](#a73776ba7d66a478c92c6cb3dfed50af4)   0x0B4 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_C](#aa391fa888ded57351c9b62f54df1ce36)   0x0B5 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_D](#a90c7aa7bbddb04e6ae4b6eccb64a0e93)   0x0B6 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_E](#adbfb562e616a86a3e28f8c3f09553db9)   0x0B7 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COMPARE\_F](#a6f07945c82efae23754e34dc09bee884)   0x0B8 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW](#aede7879166ef812139641122782d873b)   0x0B9 |
| #define | [RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW](#ad71d20ad5434f219a61e0f0aded090d1)   0x0BA |
| #define | [RA\_ELC\_EVENT\_GPT2\_PC](#a3a03431df622c2be648d0450d88facc7)   0x0BB |
| #define | [RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A](#a74526500dfb573fe21fbca739b1698e1)   0x0BC |
| #define | [RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B](#ac6cfac3496e4ab71c9bf84b43e06486a)   0x0BD |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_C](#a1af4840d468eb4c4e1672a34652ef583)   0x0BE |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_D](#a263e6b02601dd37d6eedaab56a2e6fcd)   0x0BF |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_E](#a9035e080d39d60ecc898a596b9902aa6)   0x0C0 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COMPARE\_F](#a9cffb5aca60a4c7349789fc23fb197fb)   0x0C1 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW](#a546eff128c44a29f56fe90952cef475d)   0x0C2 |
| #define | [RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW](#ab30a5683e48535abbf0c400a5a0d8946)   0x0C3 |
| #define | [RA\_ELC\_EVENT\_GPT3\_PC](#ac39dad31699579a5ee3deebf4fc57cb4)   0x0C4 |
| #define | [RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A](#a8130aa176d9d5dd698c62708111515e0)   0x0C5 |
| #define | [RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B](#aa77a30a219070d15e358a43fbbd89728)   0x0C6 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_C](#af6c1cb172b343baa8d8bbe01d1674922)   0x0C7 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_D](#ae8c7945c641045c615922a3f82329c56)   0x0C8 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_E](#afcb271a94d9b07b7b1a204f325b80d52)   0x0C9 |
| #define | [RA\_ELC\_EVENT\_GPT4\_COMPARE\_F](#a906eb0e1ed2786ed2b14e4608489b2cc)   0x0CA |
| #define | [RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW](#abb820eb80ad8afc5c12dc3581fc7a0b9)   0x0CB |
| #define | [RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW](#a65831ae6b037607dc55a2b1e8aa296a7)   0x0CC |
| #define | [RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A](#adc4aceff99f296b06938254f9dcc1f2f)   0x0CE |
| #define | [RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B](#aad1fc8b32dffaaa64f9908951f8b1c64)   0x0CF |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_C](#aebaa50f4643efe5b87798777cee578bc)   0x0D0 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_D](#a21965e21bd4045aa5010925620b4d827)   0x0D1 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_E](#a51a7cb146f0efbb7bc9f7336031006a4)   0x0D2 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COMPARE\_F](#abbd0bd21af2bd1679d6d7bc36001b97d)   0x0D3 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW](#a038e7580f03fbdd74f417108cd2a8b4d)   0x0D4 |
| #define | [RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW](#ac38b8f1154d6a699923b2bbf249e38fd)   0x0D5 |
| #define | [RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A](#acad1c37929903ddee569f40a3c5c59e3)   0x0D7 |
| #define | [RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B](#aa0fc9b447efbcba0bb6800f785daeb96)   0x0D8 |
| #define | [RA\_ELC\_EVENT\_GPT6\_COMPARE\_C](#a01f586bd98832ea9b8aa58741b61a319)   0x0D9 |
| #define | [RA\_ELC\_EVENT\_GPT6\_COMPARE\_D](#acd71c3b8e8e1d96aa3ff6affb93f5000)   0x0DA |
| #define | [RA\_ELC\_EVENT\_GPT6\_COMPARE\_E](#a6abdcc7a6331a8283cfe0c1ac06b7d83)   0x0DB |
| #define | [RA\_ELC\_EVENT\_GPT6\_COMPARE\_F](#a28b6b55ad533e3cb606b2b0937c916b3)   0x0DC |
| #define | [RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW](#ac3c8dd6a5b7f95dccc58e7ec4e235a40)   0x0DD |
| #define | [RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW](#acdece33585a75fccba962e4f764058fb)   0x0DE |
| #define | [RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A](#afe1b39e5d37a5ed631dd18869cfbac8a)   0x0E0 |
| #define | [RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B](#a53b7cfc8d0a000bd57f159b09b0a9c26)   0x0E1 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COMPARE\_C](#add91262eba9ec860b788030af153161a)   0x0E2 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COMPARE\_D](#a9310fd708ca6f0afcf374bfc96e22e6e)   0x0E3 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COMPARE\_E](#a8d18bd54c972d1de01c2a9f86e832cd0)   0x0E4 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COMPARE\_F](#aca89f90e8afa3f656e76f5960717543c)   0x0E5 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW](#aac0ed7abde81cf4bcc7588bf64b53c04)   0x0E6 |
| #define | [RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW](#ab1935670b6c0a5b5629ef8ba9d854f6c)   0x0E7 |
| #define | [RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_A](#acbe756d66c556dab820bbba06e67248c)   0x0E9 |
| #define | [RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_B](#a86965f2d57f55861ddb995b2b1381aae)   0x0EA |
| #define | [RA\_ELC\_EVENT\_GPT8\_COMPARE\_C](#af58a21982c9fb458bd12cf1d3922ffd2)   0x0EB |
| #define | [RA\_ELC\_EVENT\_GPT8\_COMPARE\_D](#a9d76f5a9c5546d1410b741ec7862713c)   0x0EC |
| #define | [RA\_ELC\_EVENT\_GPT8\_COMPARE\_E](#a9d6cf6e4081dd7ef14196fd754838224)   0x0ED |
| #define | [RA\_ELC\_EVENT\_GPT8\_COMPARE\_F](#abac4f8da4010bc5753188cc9bbce4feb)   0x0EE |
| #define | [RA\_ELC\_EVENT\_GPT8\_COUNTER\_OVERFLOW](#a560a2f23d31c99d46b5de3fb65b3c066)   0x0EF |
| #define | [RA\_ELC\_EVENT\_GPT8\_COUNTER\_UNDERFLOW](#a217a7f7cdd39114472fc4276fc2337a2)   0x0F0 |
| #define | [RA\_ELC\_EVENT\_GPT8\_PC](#a2170a5524be189decf2d098d082e24fe)   0x0F1 |
| #define | [RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_A](#a1b1bc8aa177575a9928b87d4270d3293)   0x0F2 |
| #define | [RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_B](#a9d37d2fabd4ff799c0b6a1f2e7131b50)   0x0F3 |
| #define | [RA\_ELC\_EVENT\_GPT9\_COMPARE\_C](#a0654be705490f32e47348cb31dea046d)   0x0F4 |
| #define | [RA\_ELC\_EVENT\_GPT9\_COMPARE\_D](#af204da0f122a67c5374ebdcd231684b0)   0x0F5 |
| #define | [RA\_ELC\_EVENT\_GPT9\_COMPARE\_E](#a7af6cbe91bfe594230d36a60a684877c)   0x0F6 |
| #define | [RA\_ELC\_EVENT\_GPT9\_COMPARE\_F](#ad2ad78dddd8c2b7dc560ec75439870ce)   0x0F7 |
| #define | [RA\_ELC\_EVENT\_GPT9\_COUNTER\_OVERFLOW](#ab5599f7f5509cbdae09668ec09078625)   0x0F8 |
| #define | [RA\_ELC\_EVENT\_GPT9\_COUNTER\_UNDERFLOW](#aab44882a60fd898b847597a64ad1ec05)   0x0F9 |
| #define | [RA\_ELC\_EVENT\_GPT9\_PC](#acdae0456188e411e857278f0e543798d)   0x0FA |
| #define | [RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_A](#a3e446393f52c0b25041942b552e74816)   0x0FB |
| #define | [RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_B](#a2333e30317873b25420483f93f9039e7)   0x0FC |
| #define | [RA\_ELC\_EVENT\_GPT10\_COMPARE\_C](#aae47fb3196b5989c45883943619dbe02)   0x0FD |
| #define | [RA\_ELC\_EVENT\_GPT10\_COMPARE\_D](#a7210f910c16be4bdeae56e5d10b9ab94)   0x0FE |
| #define | [RA\_ELC\_EVENT\_GPT10\_COMPARE\_E](#a7d195f17c9da519dae057c9d337e0443)   0x0FF |
| #define | [RA\_ELC\_EVENT\_GPT10\_COMPARE\_F](#ae2ad03f6c166fc2470e3b76623f81444)   0x100 |
| #define | [RA\_ELC\_EVENT\_GPT10\_COUNTER\_OVERFLOW](#abbdcc7f1ec056632b1f162527570ebd4)   0x101 |
| #define | [RA\_ELC\_EVENT\_GPT10\_COUNTER\_UNDERFLOW](#a7475c7d51460f60c7f1ace0e744b1e7f)   0x102 |
| #define | [RA\_ELC\_EVENT\_GPT10\_PC](#a0f8cedfe7e3331d74adbee4ff6aa4dcc)   0x103 |
| #define | [RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_A](#a71d10e75f9dc2beef51e422160a9b600)   0x104 |
| #define | [RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_B](#af45005c2897b2d3e17652426e7ba0ffb)   0x105 |
| #define | [RA\_ELC\_EVENT\_GPT11\_COMPARE\_C](#af329a1e7556fc745376fb9912af82e85)   0x106 |
| #define | [RA\_ELC\_EVENT\_GPT11\_COMPARE\_D](#a38b26e657a05bf629e023e2cc18fec6d)   0x107 |
| #define | [RA\_ELC\_EVENT\_GPT11\_COMPARE\_E](#aa6967c733b94450076f0468049f8a580)   0x108 |
| #define | [RA\_ELC\_EVENT\_GPT11\_COMPARE\_F](#a5c504ecc48d5beb357cdd42292af6072)   0x109 |
| #define | [RA\_ELC\_EVENT\_GPT11\_COUNTER\_OVERFLOW](#a65114b19113928d597ea9e1040c63e86)   0x10A |
| #define | [RA\_ELC\_EVENT\_GPT11\_COUNTER\_UNDERFLOW](#ad17299e05623683967d4b3652df71050)   0x10B |
| #define | [RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_A](#af703c7f5148f647cf99f15f5017b9b8e)   0x10D |
| #define | [RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_B](#ab61dcfc42e758bd67fff2e3e0cc7462e)   0x10E |
| #define | [RA\_ELC\_EVENT\_GPT12\_COMPARE\_C](#a70cbb57f4225aa5064043caaeb34f14c)   0x10F |
| #define | [RA\_ELC\_EVENT\_GPT12\_COMPARE\_D](#aac6e70fd9c5806050ca602cdfaff94af)   0x110 |
| #define | [RA\_ELC\_EVENT\_GPT12\_COMPARE\_E](#a542befd78aec05f096611817a090d542)   0x111 |
| #define | [RA\_ELC\_EVENT\_GPT12\_COMPARE\_F](#ac51ca6a913774b5dbb991a15fb37cf98)   0x112 |
| #define | [RA\_ELC\_EVENT\_GPT12\_COUNTER\_OVERFLOW](#ae3c96e8c252ccaf26b2059bd39d7de3a)   0x113 |
| #define | [RA\_ELC\_EVENT\_GPT12\_COUNTER\_UNDERFLOW](#ad9d2590f2cfd624f475718d459fb3d45)   0x114 |
| #define | [RA\_ELC\_EVENT\_GPT13\_CAPTURE\_COMPARE\_A](#a7a9e3e3d3c2c815e1a4696068ae4a1b4)   0x116 |
| #define | [RA\_ELC\_EVENT\_GPT13\_CAPTURE\_COMPARE\_B](#a516b477a84886d2b3bafb0445a5e058e)   0x117 |
| #define | [RA\_ELC\_EVENT\_GPT13\_COMPARE\_C](#aca23b053b565b5c46b09f58b2f9310bf)   0x118 |
| #define | [RA\_ELC\_EVENT\_GPT13\_COMPARE\_D](#a8dc369d2e6fa7ad1b6a9ce5cb1b43865)   0x119 |
| #define | [RA\_ELC\_EVENT\_GPT13\_COMPARE\_E](#afa734348cb5498039e88bc35dbf15d3e)   0x11A |
| #define | [RA\_ELC\_EVENT\_GPT13\_COMPARE\_F](#a2366ee4fc54ba1c95e71f6c97af8052a)   0x11B |
| #define | [RA\_ELC\_EVENT\_GPT13\_COUNTER\_OVERFLOW](#ac4f91952df6d2badfc33a314615d6326)   0x11C |
| #define | [RA\_ELC\_EVENT\_GPT13\_COUNTER\_UNDERFLOW](#a44d75ba5e9ebcb3cd3056f5205957370)   0x11D |
| #define | [RA\_ELC\_EVENT\_EDMAC0\_EINT](#aea1fab1522d24393ee7292213df7d452)   0x120 |
| #define | [RA\_ELC\_EVENT\_USBHS\_FIFO\_0](#a1f824a01b81720cfd0fd63603f446567)   0x121 |
| #define | [RA\_ELC\_EVENT\_USBHS\_FIFO\_1](#a39b1f6234c0f4e3a27663410e748b2c4)   0x122 |
| #define | [RA\_ELC\_EVENT\_USBHS\_USB\_INT\_RESUME](#a650605a9b87c871a6f29efb4d029f346)   0x123 |
| #define | [RA\_ELC\_EVENT\_SCI0\_RXI](#ad9e9a8451a683c5b5bc8a2ace8264c27)   0x124 |
| #define | [RA\_ELC\_EVENT\_SCI0\_TXI](#aecc4fdda2a7eeb2bab0b894f2e5047d9)   0x125 |
| #define | [RA\_ELC\_EVENT\_SCI0\_TEI](#ae845a850ab730c651badc5c857e28ee9)   0x126 |
| #define | [RA\_ELC\_EVENT\_SCI0\_ERI](#ad4580e769bae423298276e31ee2ee071)   0x127 |
| #define | [RA\_ELC\_EVENT\_SCI0\_AED](#ad8c85ee25e4bbc5563d9878156232f8e)   0x128 |
| #define | [RA\_ELC\_EVENT\_SCI0\_BFD](#a624bb86f4c26e04cc4b044b2f3f4aec9)   0x129 |
| #define | [RA\_ELC\_EVENT\_SCI0\_AM](#ae2373b571584dae4d1c7fc57142ecb3c)   0x12A |
| #define | [RA\_ELC\_EVENT\_SCI1\_RXI](#ae936e9aa971a376cb4ea3405c68d57f0)   0x12B |
| #define | [RA\_ELC\_EVENT\_SCI1\_TXI](#abd1c6187f97f2817dc5eb59278a996b1)   0x12C |
| #define | [RA\_ELC\_EVENT\_SCI1\_TEI](#aae0ca4a1031af4c490fbb1ecbe201662)   0x12D |
| #define | [RA\_ELC\_EVENT\_SCI1\_ERI](#a6a673466eb5261d23ee06be132ca9cde)   0x12E |
| #define | [RA\_ELC\_EVENT\_SCI1\_AED](#a85f1cff0bee1f3394e53dc4180fecbda)   0x12F |
| #define | [RA\_ELC\_EVENT\_SCI1\_BFD](#ae20f8922e54edb56904b397b6e77fda2)   0x130 |
| #define | [RA\_ELC\_EVENT\_SCI1\_AM](#ad9ca7dbcac36bb7f921cd8b8db761623)   0x131 |
| #define | [RA\_ELC\_EVENT\_SCI2\_RXI](#a484b0928fab1e96f3008b9e7b12bab07)   0x132 |
| #define | [RA\_ELC\_EVENT\_SCI2\_TXI](#a5991f7636af52ea3285cf17d300f62bb)   0x133 |
| #define | [RA\_ELC\_EVENT\_SCI2\_TEI](#a9bbdd2f449bfd5709f6c8b77b8378ca4)   0x134 |
| #define | [RA\_ELC\_EVENT\_SCI2\_ERI](#ad31428c7900c978dba266761df793f4c)   0x135 |
| #define | [RA\_ELC\_EVENT\_SCI2\_AM](#a023110baac3b030238844ab6a8999652)   0x138 |
| #define | [RA\_ELC\_EVENT\_SCI3\_RXI](#a87a1f07a2b420f9ce8d7ebcc1c505986)   0x139 |
| #define | [RA\_ELC\_EVENT\_SCI3\_TXI](#aee0548d7714ebd04748eadf9e9dbb97c)   0x13A |
| #define | [RA\_ELC\_EVENT\_SCI3\_TEI](#a6f9d20424191f026030159511647f913)   0x13B |
| #define | [RA\_ELC\_EVENT\_SCI3\_ERI](#ab7a6ad3ccc6279863a491a3787fd5c5e)   0x13C |
| #define | [RA\_ELC\_EVENT\_SCI3\_AM](#a075f80d14abaa63627574519b9ebf36b)   0x13F |
| #define | [RA\_ELC\_EVENT\_SCI4\_RXI](#afe86466482eb03b85da9feb17bdccfc0)   0x140 |
| #define | [RA\_ELC\_EVENT\_SCI4\_TXI](#a89f26e1bfd92cb7c9a2bad9acd80e553)   0x141 |
| #define | [RA\_ELC\_EVENT\_SCI4\_TEI](#a2554192500a5ac058fbd338d3018f6cc)   0x142 |
| #define | [RA\_ELC\_EVENT\_SCI4\_ERI](#ac6f2b3938cde7ba80faf523548dfa6c2)   0x143 |
| #define | [RA\_ELC\_EVENT\_SCI4\_AM](#abddf2cbec24fd59c9330b0328a21f82e)   0x146 |
| #define | [RA\_ELC\_EVENT\_SCI9\_RXI](#ac01e51a9360f409e430642d86818bf98)   0x163 |
| #define | [RA\_ELC\_EVENT\_SCI9\_TXI](#a8c628c59b08ed53781fd406ea22da796)   0x164 |
| #define | [RA\_ELC\_EVENT\_SCI9\_TEI](#ac3a064375ff90f3a6a35c5fdda680f95)   0x165 |
| #define | [RA\_ELC\_EVENT\_SCI9\_ERI](#af2e4d2d6b59c512e536d901789b3c1a2)   0x166 |
| #define | [RA\_ELC\_EVENT\_SCI9\_AM](#a2bfc7def09c933262aa530227a45af7d)   0x169 |
| #define | [RA\_ELC\_EVENT\_SPI0\_RXI](#af77608914a79bea7797b63674c71db31)   0x178 |
| #define | [RA\_ELC\_EVENT\_SPI0\_TXI](#a82d87016b5d694884bba33bf71e93e92)   0x179 |
| #define | [RA\_ELC\_EVENT\_SPI0\_IDLE](#a920575ee3a202b0d7202cd053f1e235b)   0x17A |
| #define | [RA\_ELC\_EVENT\_SPI0\_ERI](#ab588fafc974153bcf94087cdb1a71d73)   0x17B |
| #define | [RA\_ELC\_EVENT\_SPI0\_TEI](#a368a0ece3d89efe3ed8ab274471849b9)   0x17C |
| #define | [RA\_ELC\_EVENT\_SPI1\_RXI](#a2f5e3b5957e42c572fda94ec535b401b)   0x17D |
| #define | [RA\_ELC\_EVENT\_SPI1\_TXI](#a0aab8e60c14b34bccb74400a818524ac)   0x17E |
| #define | [RA\_ELC\_EVENT\_SPI1\_IDLE](#a73da76e435d9de6b6b7ad48190d2c0a2)   0x17F |
| #define | [RA\_ELC\_EVENT\_SPI1\_ERI](#aedf36efaaba39c4001386536d21f81e2)   0x180 |
| #define | [RA\_ELC\_EVENT\_SPI1\_TEI](#a60f40983e3c6344a257bd157b40069d5)   0x181 |
| #define | [RA\_ELC\_EVENT\_XSPI\_ERR](#a88aee6cf6092e69ee117b12f000d83d9)   0x182 |
| #define | [RA\_ELC\_EVENT\_XSPI\_CMP](#a8209ca1ee92cb61da174f6d0c48b5220)   0x183 |
| #define | [RA\_ELC\_EVENT\_CAN\_RXF](#a381d0e6b749cb12add2dfcb129f80468)   0x185 |
| #define | [RA\_ELC\_EVENT\_CAN\_GLERR](#a05a66b601667344eff54e86b13a820d5)   0x186 |
| #define | [RA\_ELC\_EVENT\_CAN0\_DMAREQ0](#a92c3913b5074214a5468bc04672fa810)   0x187 |
| #define | [RA\_ELC\_EVENT\_CAN0\_DMAREQ1](#abb607aea1165ee35308c39315bbf028c)   0x188 |
| #define | [RA\_ELC\_EVENT\_CAN1\_DMAREQ0](#a5706bcde62bd7ac9270c238e329cd15b)   0x18B |
| #define | [RA\_ELC\_EVENT\_CAN1\_DMAREQ1](#a78395b5c4124a198b660c1da53539655)   0x18C |
| #define | [RA\_ELC\_EVENT\_CAN0\_TX](#a31b33463c8527b56ad5760d86f066c6c)   0x18F |
| #define | [RA\_ELC\_EVENT\_CAN0\_CHERR](#a0c01b6adbdd0b29b4390a34acfee339b)   0x190 |
| #define | [RA\_ELC\_EVENT\_CAN0\_COMFRX](#a84cb35e4a3dfad95529937db4966c63f)   0x191 |
| #define | [RA\_ELC\_EVENT\_CAN0\_CF\_DMAREQ](#a5d73e70c306cc7cd5d89a9963b9075f5)   0x192 |
| #define | [RA\_ELC\_EVENT\_CAN0\_RXMB](#aa7871b154ba1e9bbb8a48aeeec65e416)   0x193 |
| #define | [RA\_ELC\_EVENT\_CAN1\_TX](#ab669f854f92ae61862b1c7a49f857426)   0x194 |
| #define | [RA\_ELC\_EVENT\_CAN1\_CHERR](#a98005eb9ea9f3a087cb9fbcbdd842bed)   0x195 |
| #define | [RA\_ELC\_EVENT\_CAN1\_COMFRX](#a0a8fe1d10e62f54b4b87568686bc1f64)   0x196 |
| #define | [RA\_ELC\_EVENT\_CAN1\_CF\_DMAREQ](#a3da879a9c8eb950aeca9041cb8ff8fc9)   0x197 |
| #define | [RA\_ELC\_EVENT\_CAN1\_RXMB](#abb9be46f4f5af6e6731c40bf8229e811)   0x198 |
| #define | [RA\_ELC\_EVENT\_CAN0\_MRAM\_ERI](#adf49b7c6aecfae965cd0040817b11a5d)   0x19B |
| #define | [RA\_ELC\_EVENT\_CAN1\_MRAM\_ERI](#a5d5dc4797ff132feaa1dbeb0d18620a4)   0x19C |
| #define | [RA\_ELC\_EVENT\_I3C0\_RESPONSE](#a3080239b71b12d15d9cd78d78a0b65e6)   0x19D |
| #define | [RA\_ELC\_EVENT\_I3C0\_COMMAND](#a92a8148f568fcf39ccde3817aef8ae9d)   0x19E |
| #define | [RA\_ELC\_EVENT\_I3C0\_IBI](#a2060363167f356732fb5b817e4dbcdb5)   0x19F |
| #define | [RA\_ELC\_EVENT\_I3C0\_RX](#a3b2265686fb51c1ae5cdc549cac4b3fd)   0x1A0 |
| #define | [RA\_ELC\_EVENT\_IICB0\_RXI](#ac12a24178c5964cdd58666f7d57a1b1b)   0x1A0 |
| #define | [RA\_ELC\_EVENT\_I3C0\_TX](#a6bd966e36dba524e3e5ad37250d9a2fe)   0x1A1 |
| #define | [RA\_ELC\_EVENT\_IICB0\_TXI](#ac3f18d838eb617f5022034a38238b3da)   0x1A1 |
| #define | [RA\_ELC\_EVENT\_I3C0\_RCV\_STATUS](#a0fe2a3ad8bf5bc9f9fbe79c2e3142a82)   0x1A2 |
| #define | [RA\_ELC\_EVENT\_I3C0\_HRESP](#ad03e0236533be6c8a679f45dae45b5f3)   0x1A3 |
| #define | [RA\_ELC\_EVENT\_I3C0\_HCMD](#a41c98f2bad994edd460738fc681d1915)   0x1A4 |
| #define | [RA\_ELC\_EVENT\_I3C0\_HRX](#a6944a47bc40eaf5be0bcd9a8ea3f61b3)   0x1A5 |
| #define | [RA\_ELC\_EVENT\_I3C0\_HTX](#a79b1703b94f1d6a62c589cd442d6c285)   0x1A6 |
| #define | [RA\_ELC\_EVENT\_I3C0\_TEND](#a263d9beac3bda75a81b657995262df84)   0x1A7 |
| #define | [RA\_ELC\_EVENT\_IICB0\_TEI](#accb1b88c154566410d539b20c64f67cc)   0x1A7 |
| #define | [RA\_ELC\_EVENT\_I3C0\_EEI](#a7031d655983b5a153dec583b24df13fe)   0x1A8 |
| #define | [RA\_ELC\_EVENT\_IICB0\_ERI](#ac0d8b1e8f379ef983dfd2004ed02e65e)   0x1A8 |
| #define | [RA\_ELC\_EVENT\_I3C0\_STEV](#a57e6e464e10dc72ef057cb24530f26cc)   0x1A9 |
| #define | [RA\_ELC\_EVENT\_I3C0\_MREFOVF](#a80adbdbcc1c63c9623763c8aa595c3ca)   0x1AA |
| #define | [RA\_ELC\_EVENT\_I3C0\_MREFCPT](#a53d989fdbde5fa99dfcb6226c3419ab9)   0x1AB |
| #define | [RA\_ELC\_EVENT\_I3C0\_AMEV](#a1fdeb36ba55249ba92f2bdb425f18d74)   0x1AC |
| #define | [RA\_ELC\_EVENT\_I3C0\_WU](#a979332348cebe774723bfd610b02c36b)   0x1AD |
| #define | [RA\_ELC\_EVENT\_ADC0\_SCAN\_END](#ad7284976213551f7d4fa450bf2bf8c7c)   0x1AE |
| #define | [RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B](#aecbe4efa29972b832e35ebb00d7499ad)   0x1AF |
| #define | [RA\_ELC\_EVENT\_ADC0\_WINDOW\_A](#aa4feb2c3e29ba84d1397c618b7b860bf)   0x1B0 |
| #define | [RA\_ELC\_EVENT\_ADC0\_WINDOW\_B](#ab59c8ec4f20de5cf4709efe0a7ee70a1)   0x1B1 |
| #define | [RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH](#af187c78a1f05fc4be81aa3af36e4cde5)   0x1B2 |
| #define | [RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH](#a65d6c499a6852434b4802f8ef7066eb4)   0x1B3 |
| #define | [RA\_ELC\_EVENT\_ADC1\_SCAN\_END](#aa02ddf9a93b64b5fb5c6d60b51bc24ed)   0x1B4 |
| #define | [RA\_ELC\_EVENT\_ADC1\_SCAN\_END\_B](#a1c3786e7e0f56f55d45ed55901a14bb4)   0x1B5 |
| #define | [RA\_ELC\_EVENT\_ADC1\_WINDOW\_A](#aef02cb8109fd68b4c4a1a5efca255583)   0x1B6 |
| #define | [RA\_ELC\_EVENT\_ADC1\_WINDOW\_B](#a283756acfcfe4c208cbaa5a3edd4d2cc)   0x1B7 |
| #define | [RA\_ELC\_EVENT\_ADC1\_COMPARE\_MATCH](#adbc3a9f438323aed719c7e210829a78f)   0x1B8 |
| #define | [RA\_ELC\_EVENT\_ADC1\_COMPARE\_MISMATCH](#a12123fbc57d65b4ab932495bf0726d57)   0x1B9 |
| #define | [RA\_ELC\_EVENT\_DOC\_INT](#ab6c210d6481294137fd4bc32c39e5de1)   0x1BA |
| #define | [RA\_ELC\_EVENT\_RSIP\_TADI](#a0b76751d4c1e7f98ec6de2633cca4057)   0x1BC |
| #define | [RA\_ELC\_EVENT\_GLCDC\_LINE\_DETECT](#aead68e97be199ad080f12a2cd4b81931)   0x1CD |
| #define | [RA\_ELC\_EVENT\_GLCDC\_UNDERFLOW\_1](#a84b0f18def7879017570b500ca5ce011)   0x1CE |
| #define | [RA\_ELC\_EVENT\_GLCDC\_UNDERFLOW\_2](#a33151eca38369811748a527c9beb6b01)   0x1CF |
| #define | [RA\_ELC\_EVENT\_DRW\_INT](#a2c5dc536bea0cad911c2c89cac571957)   0x1D0 |
| #define | [RA\_ELC\_EVENT\_MIPIDSI\_SEQ0](#ac331540e98f0405e5d1a03b9c7b85006)   0x1D3 |
| #define | [RA\_ELC\_EVENT\_MIPIDSI\_SEQ1](#abb3a66beb2d4902bcd8495577d1ae54f)   0x1D4 |
| #define | [RA\_ELC\_EVENT\_MIPIDSI\_VIN1](#aa20efc3b9e2d2f8ebab178eae2b0df5d)   0x1D5 |
| #define | [RA\_ELC\_EVENT\_MIPIDSI\_RCV](#a3698b91ae9aef8085388be626b134d56)   0x1D6 |
| #define | [RA\_ELC\_EVENT\_MIPIDSI\_FERR](#a45075f80238882f18a0f4bcaf37bfd58)   0x1D7 |
| #define | [RA\_ELC\_EVENT\_MIPIDSI\_PPI](#a2658eba6f63e4ca5c2f3a45c7b5c791d)   0x1D8 |
| #define | [RA\_ELC\_EVENT\_CEU\_CEUI](#af5bab3483cd8c70b62936607b929f21a)   0x1DA |
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
| #define | [RA\_ELC\_PERIPHERAL\_ADC1](#aea69e6e72e14f53afeb85aa4a9349bcb)   10 |
| #define | [RA\_ELC\_PERIPHERAL\_ADC1\_B](#adbd2118aea6d1ba6ca67de192f0033fc)   11 |
| #define | [RA\_ELC\_PERIPHERAL\_DAC0](#a9a32ba5817467743fbcf24b698124b02)   12 |
| #define | [RA\_ELC\_PERIPHERAL\_DAC1](#a84aa20e3793499f427f6c9ccb7a20566)   13 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT1](#a5830e830b7b10cd68441de2648edd6a0)   14 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT2](#a42d4feb2c854cc1964455297e6d7eb72)   15 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT3](#a349933f20d7b6f768e49239724d0c5f7)   16 |
| #define | [RA\_ELC\_PERIPHERAL\_IOPORT4](#a6d08d1db64f903fa2dacfc81568b004d)   17 |
| #define | [RA\_ELC\_PERIPHERAL\_I3C](#a44df9c541681520b5fb529348b8deb81)   30 |

## Macro Definition Documentation

## [◆ ](#a3bbee94907736c0c435cc5ff64d1e7ef)RA\_ELC\_EVENT\_ACMPHS0\_INT

| #define RA\_ELC\_EVENT\_ACMPHS0\_INT   0x07B |
| --- |

## [◆ ](#ab1a4d1aee4743a0ee8bd194052a6c840)RA\_ELC\_EVENT\_ACMPHS1\_INT

| #define RA\_ELC\_EVENT\_ACMPHS1\_INT   0x07C |
| --- |

## [◆ ](#af187c78a1f05fc4be81aa3af36e4cde5)RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH

| #define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MATCH   0x1B2 |
| --- |

## [◆ ](#a65d6c499a6852434b4802f8ef7066eb4)RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH

| #define RA\_ELC\_EVENT\_ADC0\_COMPARE\_MISMATCH   0x1B3 |
| --- |

## [◆ ](#ad7284976213551f7d4fa450bf2bf8c7c)RA\_ELC\_EVENT\_ADC0\_SCAN\_END

| #define RA\_ELC\_EVENT\_ADC0\_SCAN\_END   0x1AE |
| --- |

## [◆ ](#aecbe4efa29972b832e35ebb00d7499ad)RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B

| #define RA\_ELC\_EVENT\_ADC0\_SCAN\_END\_B   0x1AF |
| --- |

## [◆ ](#aa4feb2c3e29ba84d1397c618b7b860bf)RA\_ELC\_EVENT\_ADC0\_WINDOW\_A

| #define RA\_ELC\_EVENT\_ADC0\_WINDOW\_A   0x1B0 |
| --- |

## [◆ ](#ab59c8ec4f20de5cf4709efe0a7ee70a1)RA\_ELC\_EVENT\_ADC0\_WINDOW\_B

| #define RA\_ELC\_EVENT\_ADC0\_WINDOW\_B   0x1B1 |
| --- |

## [◆ ](#adbc3a9f438323aed719c7e210829a78f)RA\_ELC\_EVENT\_ADC1\_COMPARE\_MATCH

| #define RA\_ELC\_EVENT\_ADC1\_COMPARE\_MATCH   0x1B8 |
| --- |

## [◆ ](#a12123fbc57d65b4ab932495bf0726d57)RA\_ELC\_EVENT\_ADC1\_COMPARE\_MISMATCH

| #define RA\_ELC\_EVENT\_ADC1\_COMPARE\_MISMATCH   0x1B9 |
| --- |

## [◆ ](#aa02ddf9a93b64b5fb5c6d60b51bc24ed)RA\_ELC\_EVENT\_ADC1\_SCAN\_END

| #define RA\_ELC\_EVENT\_ADC1\_SCAN\_END   0x1B4 |
| --- |

## [◆ ](#a1c3786e7e0f56f55d45ed55901a14bb4)RA\_ELC\_EVENT\_ADC1\_SCAN\_END\_B

| #define RA\_ELC\_EVENT\_ADC1\_SCAN\_END\_B   0x1B5 |
| --- |

## [◆ ](#aef02cb8109fd68b4c4a1a5efca255583)RA\_ELC\_EVENT\_ADC1\_WINDOW\_A

| #define RA\_ELC\_EVENT\_ADC1\_WINDOW\_A   0x1B6 |
| --- |

## [◆ ](#a283756acfcfe4c208cbaa5a3edd4d2cc)RA\_ELC\_EVENT\_ADC1\_WINDOW\_B

| #define RA\_ELC\_EVENT\_ADC1\_WINDOW\_B   0x1B7 |
| --- |

## [◆ ](#a015e6f8aed4b467f4554e6887b4d9ec9)RA\_ELC\_EVENT\_AGT0\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT0\_COMPARE\_A   0x047 |
| --- |

## [◆ ](#ada1ad302dc5b987a6f7c972afae729f2)RA\_ELC\_EVENT\_AGT0\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT0\_COMPARE\_B   0x048 |
| --- |

## [◆ ](#a4c3604a42ead1d43f472e901087ec148)RA\_ELC\_EVENT\_AGT0\_INT

| #define RA\_ELC\_EVENT\_AGT0\_INT   0x046 |
| --- |

## [◆ ](#aeb2399818b6b141ab4a37e257dba22be)RA\_ELC\_EVENT\_AGT1\_COMPARE\_A

| #define RA\_ELC\_EVENT\_AGT1\_COMPARE\_A   0x04A |
| --- |

## [◆ ](#a1d660c78348b48ea7a072225491ae44b)RA\_ELC\_EVENT\_AGT1\_COMPARE\_B

| #define RA\_ELC\_EVENT\_AGT1\_COMPARE\_B   0x04B |
| --- |

## [◆ ](#a635180e38c932579072f4eebd665592f)RA\_ELC\_EVENT\_AGT1\_INT

| #define RA\_ELC\_EVENT\_AGT1\_INT   0x049 |
| --- |

## [◆ ](#a6ec3edb5e4de5bca1171ade1aa9ca19f)RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR

| #define RA\_ELC\_EVENT\_CAC\_FREQUENCY\_ERROR   0x08C |
| --- |

## [◆ ](#a1390ee9467a9d093de1532f0703ec35f)RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END

| #define RA\_ELC\_EVENT\_CAC\_MEASUREMENT\_END   0x08D |
| --- |

## [◆ ](#a3463c1e202ab7891521eda7196e1be80)RA\_ELC\_EVENT\_CAC\_OVERFLOW

| #define RA\_ELC\_EVENT\_CAC\_OVERFLOW   0x08E |
| --- |

## [◆ ](#a5d73e70c306cc7cd5d89a9963b9075f5)RA\_ELC\_EVENT\_CAN0\_CF\_DMAREQ

| #define RA\_ELC\_EVENT\_CAN0\_CF\_DMAREQ   0x192 |
| --- |

## [◆ ](#a0c01b6adbdd0b29b4390a34acfee339b)RA\_ELC\_EVENT\_CAN0\_CHERR

| #define RA\_ELC\_EVENT\_CAN0\_CHERR   0x190 |
| --- |

## [◆ ](#a84cb35e4a3dfad95529937db4966c63f)RA\_ELC\_EVENT\_CAN0\_COMFRX

| #define RA\_ELC\_EVENT\_CAN0\_COMFRX   0x191 |
| --- |

## [◆ ](#a92c3913b5074214a5468bc04672fa810)RA\_ELC\_EVENT\_CAN0\_DMAREQ0

| #define RA\_ELC\_EVENT\_CAN0\_DMAREQ0   0x187 |
| --- |

## [◆ ](#abb607aea1165ee35308c39315bbf028c)RA\_ELC\_EVENT\_CAN0\_DMAREQ1

| #define RA\_ELC\_EVENT\_CAN0\_DMAREQ1   0x188 |
| --- |

## [◆ ](#adf49b7c6aecfae965cd0040817b11a5d)RA\_ELC\_EVENT\_CAN0\_MRAM\_ERI

| #define RA\_ELC\_EVENT\_CAN0\_MRAM\_ERI   0x19B |
| --- |

## [◆ ](#aa7871b154ba1e9bbb8a48aeeec65e416)RA\_ELC\_EVENT\_CAN0\_RXMB

| #define RA\_ELC\_EVENT\_CAN0\_RXMB   0x193 |
| --- |

## [◆ ](#a31b33463c8527b56ad5760d86f066c6c)RA\_ELC\_EVENT\_CAN0\_TX

| #define RA\_ELC\_EVENT\_CAN0\_TX   0x18F |
| --- |

## [◆ ](#a3da879a9c8eb950aeca9041cb8ff8fc9)RA\_ELC\_EVENT\_CAN1\_CF\_DMAREQ

| #define RA\_ELC\_EVENT\_CAN1\_CF\_DMAREQ   0x197 |
| --- |

## [◆ ](#a98005eb9ea9f3a087cb9fbcbdd842bed)RA\_ELC\_EVENT\_CAN1\_CHERR

| #define RA\_ELC\_EVENT\_CAN1\_CHERR   0x195 |
| --- |

## [◆ ](#a0a8fe1d10e62f54b4b87568686bc1f64)RA\_ELC\_EVENT\_CAN1\_COMFRX

| #define RA\_ELC\_EVENT\_CAN1\_COMFRX   0x196 |
| --- |

## [◆ ](#a5706bcde62bd7ac9270c238e329cd15b)RA\_ELC\_EVENT\_CAN1\_DMAREQ0

| #define RA\_ELC\_EVENT\_CAN1\_DMAREQ0   0x18B |
| --- |

## [◆ ](#a78395b5c4124a198b660c1da53539655)RA\_ELC\_EVENT\_CAN1\_DMAREQ1

| #define RA\_ELC\_EVENT\_CAN1\_DMAREQ1   0x18C |
| --- |

## [◆ ](#a5d5dc4797ff132feaa1dbeb0d18620a4)RA\_ELC\_EVENT\_CAN1\_MRAM\_ERI

| #define RA\_ELC\_EVENT\_CAN1\_MRAM\_ERI   0x19C |
| --- |

## [◆ ](#abb9be46f4f5af6e6731c40bf8229e811)RA\_ELC\_EVENT\_CAN1\_RXMB

| #define RA\_ELC\_EVENT\_CAN1\_RXMB   0x198 |
| --- |

## [◆ ](#ab669f854f92ae61862b1c7a49f857426)RA\_ELC\_EVENT\_CAN1\_TX

| #define RA\_ELC\_EVENT\_CAN1\_TX   0x194 |
| --- |

## [◆ ](#a05a66b601667344eff54e86b13a820d5)RA\_ELC\_EVENT\_CAN\_GLERR

| #define RA\_ELC\_EVENT\_CAN\_GLERR   0x186 |
| --- |

## [◆ ](#a381d0e6b749cb12add2dfcb129f80468)RA\_ELC\_EVENT\_CAN\_RXF

| #define RA\_ELC\_EVENT\_CAN\_RXF   0x185 |
| --- |

## [◆ ](#af5bab3483cd8c70b62936607b929f21a)RA\_ELC\_EVENT\_CEU\_CEUI

| #define RA\_ELC\_EVENT\_CEU\_CEUI   0x1DA |
| --- |

## [◆ ](#a290decf4254396cbce267cb52a619717)RA\_ELC\_EVENT\_CGC\_MOSC\_STOP

| #define RA\_ELC\_EVENT\_CGC\_MOSC\_STOP   0x03E |
| --- |

## [◆ ](#a0d740efcf6ca4778a2f8a9e9bd7c11c9)RA\_ELC\_EVENT\_DBG\_CTIIRQ0

| #define RA\_ELC\_EVENT\_DBG\_CTIIRQ0   0x029 |
| --- |

## [◆ ](#ab33d581df4d34b8ee361ea4e1e690ed3)RA\_ELC\_EVENT\_DBG\_CTIIRQ1

| #define RA\_ELC\_EVENT\_DBG\_CTIIRQ1   0x02A |
| --- |

## [◆ ](#a0494be0bf55e1e687e2f4c0e0f0d93aa)RA\_ELC\_EVENT\_DBG\_JBRXI

| #define RA\_ELC\_EVENT\_DBG\_JBRXI   0x02B |
| --- |

## [◆ ](#a54d8c74eefe8f9b237ea23e18033d947)RA\_ELC\_EVENT\_DMA\_TRANSERR

| #define RA\_ELC\_EVENT\_DMA\_TRANSERR   0x027 |
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

## [◆ ](#a4cae5afbbe49719555bbbfa12b8727f5)RA\_ELC\_EVENT\_DMAC4\_INT

| #define RA\_ELC\_EVENT\_DMAC4\_INT   0x015 |
| --- |

## [◆ ](#a000e31aba8a821f4358a435d280b3a7b)RA\_ELC\_EVENT\_DMAC5\_INT

| #define RA\_ELC\_EVENT\_DMAC5\_INT   0x016 |
| --- |

## [◆ ](#a2d1f6d1c797a0d787a5d5c08b0fc18ad)RA\_ELC\_EVENT\_DMAC6\_INT

| #define RA\_ELC\_EVENT\_DMAC6\_INT   0x017 |
| --- |

## [◆ ](#ae8caef45a510d4c4f1c55f923e01799e)RA\_ELC\_EVENT\_DMAC7\_INT

| #define RA\_ELC\_EVENT\_DMAC7\_INT   0x018 |
| --- |

## [◆ ](#ab6c210d6481294137fd4bc32c39e5de1)RA\_ELC\_EVENT\_DOC\_INT

| #define RA\_ELC\_EVENT\_DOC\_INT   0x1BA |
| --- |

## [◆ ](#a2c5dc536bea0cad911c2c89cac571957)RA\_ELC\_EVENT\_DRW\_INT

| #define RA\_ELC\_EVENT\_DRW\_INT   0x1D0 |
| --- |

## [◆ ](#a9a58e3a2c10447906aaf35bab5664d24)RA\_ELC\_EVENT\_DTC\_COMPLETE

| #define RA\_ELC\_EVENT\_DTC\_COMPLETE   0x022 |
| --- |

## [◆ ](#a5ab484cdaf470b47e95005d83d60394f)RA\_ELC\_EVENT\_DTC\_END

| #define RA\_ELC\_EVENT\_DTC\_END   0x021 |
| --- |

## [◆ ](#aea1fab1522d24393ee7292213df7d452)RA\_ELC\_EVENT\_EDMAC0\_EINT

| #define RA\_ELC\_EVENT\_EDMAC0\_EINT   0x120 |
| --- |

## [◆ ](#ae5c28618f4e68eef6ca83bdcec515abb)RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0

| #define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_0   0x083 |
| --- |

## [◆ ](#a9f0b82bfff5ea2ba414ac0bccad9a34d)RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1

| #define RA\_ELC\_EVENT\_ELC\_SOFTWARE\_EVENT\_1   0x084 |
| --- |

## [◆ ](#a5c7545a2f69856b7b637ad690f158b77)RA\_ELC\_EVENT\_FCU\_FIFERR

| #define RA\_ELC\_EVENT\_FCU\_FIFERR   0x030 |
| --- |

## [◆ ](#a535af54c8bcfff47cc90ba1226044d71)RA\_ELC\_EVENT\_FCU\_FRDYI

| #define RA\_ELC\_EVENT\_FCU\_FRDYI   0x031 |
| --- |

## [◆ ](#aead68e97be199ad080f12a2cd4b81931)RA\_ELC\_EVENT\_GLCDC\_LINE\_DETECT

| #define RA\_ELC\_EVENT\_GLCDC\_LINE\_DETECT   0x1CD |
| --- |

## [◆ ](#a84b0f18def7879017570b500ca5ce011)RA\_ELC\_EVENT\_GLCDC\_UNDERFLOW\_1

| #define RA\_ELC\_EVENT\_GLCDC\_UNDERFLOW\_1   0x1CE |
| --- |

## [◆ ](#a33151eca38369811748a527c9beb6b01)RA\_ELC\_EVENT\_GLCDC\_UNDERFLOW\_2

| #define RA\_ELC\_EVENT\_GLCDC\_UNDERFLOW\_2   0x1CF |
| --- |

## [◆ ](#aec8a8b590cc124ca12425f34b5a61020)RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_A   0x0A1 |
| --- |

## [◆ ](#ae1ed91479f405ac965da868e86bce533)RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT0\_CAPTURE\_COMPARE\_B   0x0A2 |
| --- |

## [◆ ](#a6d7c9090c21a8a0c497356050d649ec6)RA\_ELC\_EVENT\_GPT0\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_C   0x0A3 |
| --- |

## [◆ ](#af5b8ca097747bd987e81d8d81263aa81)RA\_ELC\_EVENT\_GPT0\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_D   0x0A4 |
| --- |

## [◆ ](#a9ebec21375578c0e52d953773373bf1e)RA\_ELC\_EVENT\_GPT0\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_E   0x0A5 |
| --- |

## [◆ ](#ad503a55a4548ff6ffd58e2b74d9eaf00)RA\_ELC\_EVENT\_GPT0\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT0\_COMPARE\_F   0x0A6 |
| --- |

## [◆ ](#a76692948000993fde4d286f1a521a6d2)RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT0\_COUNTER\_OVERFLOW   0x0A7 |
| --- |

## [◆ ](#a9edde37b8c0835978aa55d58d77c5ad5)RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT0\_COUNTER\_UNDERFLOW   0x0A8 |
| --- |

## [◆ ](#a21a934c940f85a7e4e592167eb468fd3)RA\_ELC\_EVENT\_GPT0\_PC

| #define RA\_ELC\_EVENT\_GPT0\_PC   0x0A9 |
| --- |

## [◆ ](#a3e446393f52c0b25041942b552e74816)RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_A   0x0FB |
| --- |

## [◆ ](#a2333e30317873b25420483f93f9039e7)RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT10\_CAPTURE\_COMPARE\_B   0x0FC |
| --- |

## [◆ ](#aae47fb3196b5989c45883943619dbe02)RA\_ELC\_EVENT\_GPT10\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT10\_COMPARE\_C   0x0FD |
| --- |

## [◆ ](#a7210f910c16be4bdeae56e5d10b9ab94)RA\_ELC\_EVENT\_GPT10\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT10\_COMPARE\_D   0x0FE |
| --- |

## [◆ ](#a7d195f17c9da519dae057c9d337e0443)RA\_ELC\_EVENT\_GPT10\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT10\_COMPARE\_E   0x0FF |
| --- |

## [◆ ](#ae2ad03f6c166fc2470e3b76623f81444)RA\_ELC\_EVENT\_GPT10\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT10\_COMPARE\_F   0x100 |
| --- |

## [◆ ](#abbdcc7f1ec056632b1f162527570ebd4)RA\_ELC\_EVENT\_GPT10\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT10\_COUNTER\_OVERFLOW   0x101 |
| --- |

## [◆ ](#a7475c7d51460f60c7f1ace0e744b1e7f)RA\_ELC\_EVENT\_GPT10\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT10\_COUNTER\_UNDERFLOW   0x102 |
| --- |

## [◆ ](#a0f8cedfe7e3331d74adbee4ff6aa4dcc)RA\_ELC\_EVENT\_GPT10\_PC

| #define RA\_ELC\_EVENT\_GPT10\_PC   0x103 |
| --- |

## [◆ ](#a71d10e75f9dc2beef51e422160a9b600)RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_A   0x104 |
| --- |

## [◆ ](#af45005c2897b2d3e17652426e7ba0ffb)RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT11\_CAPTURE\_COMPARE\_B   0x105 |
| --- |

## [◆ ](#af329a1e7556fc745376fb9912af82e85)RA\_ELC\_EVENT\_GPT11\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT11\_COMPARE\_C   0x106 |
| --- |

## [◆ ](#a38b26e657a05bf629e023e2cc18fec6d)RA\_ELC\_EVENT\_GPT11\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT11\_COMPARE\_D   0x107 |
| --- |

## [◆ ](#aa6967c733b94450076f0468049f8a580)RA\_ELC\_EVENT\_GPT11\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT11\_COMPARE\_E   0x108 |
| --- |

## [◆ ](#a5c504ecc48d5beb357cdd42292af6072)RA\_ELC\_EVENT\_GPT11\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT11\_COMPARE\_F   0x109 |
| --- |

## [◆ ](#a65114b19113928d597ea9e1040c63e86)RA\_ELC\_EVENT\_GPT11\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT11\_COUNTER\_OVERFLOW   0x10A |
| --- |

## [◆ ](#ad17299e05623683967d4b3652df71050)RA\_ELC\_EVENT\_GPT11\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT11\_COUNTER\_UNDERFLOW   0x10B |
| --- |

## [◆ ](#af703c7f5148f647cf99f15f5017b9b8e)RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_A   0x10D |
| --- |

## [◆ ](#ab61dcfc42e758bd67fff2e3e0cc7462e)RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT12\_CAPTURE\_COMPARE\_B   0x10E |
| --- |

## [◆ ](#a70cbb57f4225aa5064043caaeb34f14c)RA\_ELC\_EVENT\_GPT12\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT12\_COMPARE\_C   0x10F |
| --- |

## [◆ ](#aac6e70fd9c5806050ca602cdfaff94af)RA\_ELC\_EVENT\_GPT12\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT12\_COMPARE\_D   0x110 |
| --- |

## [◆ ](#a542befd78aec05f096611817a090d542)RA\_ELC\_EVENT\_GPT12\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT12\_COMPARE\_E   0x111 |
| --- |

## [◆ ](#ac51ca6a913774b5dbb991a15fb37cf98)RA\_ELC\_EVENT\_GPT12\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT12\_COMPARE\_F   0x112 |
| --- |

## [◆ ](#ae3c96e8c252ccaf26b2059bd39d7de3a)RA\_ELC\_EVENT\_GPT12\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT12\_COUNTER\_OVERFLOW   0x113 |
| --- |

## [◆ ](#ad9d2590f2cfd624f475718d459fb3d45)RA\_ELC\_EVENT\_GPT12\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT12\_COUNTER\_UNDERFLOW   0x114 |
| --- |

## [◆ ](#a7a9e3e3d3c2c815e1a4696068ae4a1b4)RA\_ELC\_EVENT\_GPT13\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT13\_CAPTURE\_COMPARE\_A   0x116 |
| --- |

## [◆ ](#a516b477a84886d2b3bafb0445a5e058e)RA\_ELC\_EVENT\_GPT13\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT13\_CAPTURE\_COMPARE\_B   0x117 |
| --- |

## [◆ ](#aca23b053b565b5c46b09f58b2f9310bf)RA\_ELC\_EVENT\_GPT13\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT13\_COMPARE\_C   0x118 |
| --- |

## [◆ ](#a8dc369d2e6fa7ad1b6a9ce5cb1b43865)RA\_ELC\_EVENT\_GPT13\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT13\_COMPARE\_D   0x119 |
| --- |

## [◆ ](#afa734348cb5498039e88bc35dbf15d3e)RA\_ELC\_EVENT\_GPT13\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT13\_COMPARE\_E   0x11A |
| --- |

## [◆ ](#a2366ee4fc54ba1c95e71f6c97af8052a)RA\_ELC\_EVENT\_GPT13\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT13\_COMPARE\_F   0x11B |
| --- |

## [◆ ](#ac4f91952df6d2badfc33a314615d6326)RA\_ELC\_EVENT\_GPT13\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT13\_COUNTER\_OVERFLOW   0x11C |
| --- |

## [◆ ](#a44d75ba5e9ebcb3cd3056f5205957370)RA\_ELC\_EVENT\_GPT13\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT13\_COUNTER\_UNDERFLOW   0x11D |
| --- |

## [◆ ](#a33a428565bfa3237aa4eda10b982fc65)RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_A   0x0AA |
| --- |

## [◆ ](#a5326aaf270290b524f8cb2e126d06602)RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT1\_CAPTURE\_COMPARE\_B   0x0AB |
| --- |

## [◆ ](#a2e55bae34ab30f2d802b8eaf93dd3cfd)RA\_ELC\_EVENT\_GPT1\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_C   0x0AC |
| --- |

## [◆ ](#ada3870f40beeec10e9366e908ed980d0)RA\_ELC\_EVENT\_GPT1\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_D   0x0AD |
| --- |

## [◆ ](#a5d4f72e95b7bb76315b9ffa059730620)RA\_ELC\_EVENT\_GPT1\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_E   0x0AE |
| --- |

## [◆ ](#a548923b7385648e4f15fef4ecb315478)RA\_ELC\_EVENT\_GPT1\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT1\_COMPARE\_F   0x0AF |
| --- |

## [◆ ](#aa6eac7cf283073eea62fbaa1df2017f2)RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT1\_COUNTER\_OVERFLOW   0x0B0 |
| --- |

## [◆ ](#ae8cefd5f23897d43cffba4e91b7c8b5c)RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT1\_COUNTER\_UNDERFLOW   0x0B1 |
| --- |

## [◆ ](#aa0208084abba3e2601c8cf7bb42837fd)RA\_ELC\_EVENT\_GPT1\_PC

| #define RA\_ELC\_EVENT\_GPT1\_PC   0x0B2 |
| --- |

## [◆ ](#ad1a5796e0c70a988165765f2ce8c1e80)RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_A   0x0B3 |
| --- |

## [◆ ](#a73776ba7d66a478c92c6cb3dfed50af4)RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT2\_CAPTURE\_COMPARE\_B   0x0B4 |
| --- |

## [◆ ](#aa391fa888ded57351c9b62f54df1ce36)RA\_ELC\_EVENT\_GPT2\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_C   0x0B5 |
| --- |

## [◆ ](#a90c7aa7bbddb04e6ae4b6eccb64a0e93)RA\_ELC\_EVENT\_GPT2\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_D   0x0B6 |
| --- |

## [◆ ](#adbfb562e616a86a3e28f8c3f09553db9)RA\_ELC\_EVENT\_GPT2\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_E   0x0B7 |
| --- |

## [◆ ](#a6f07945c82efae23754e34dc09bee884)RA\_ELC\_EVENT\_GPT2\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT2\_COMPARE\_F   0x0B8 |
| --- |

## [◆ ](#aede7879166ef812139641122782d873b)RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT2\_COUNTER\_OVERFLOW   0x0B9 |
| --- |

## [◆ ](#ad71d20ad5434f219a61e0f0aded090d1)RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT2\_COUNTER\_UNDERFLOW   0x0BA |
| --- |

## [◆ ](#a3a03431df622c2be648d0450d88facc7)RA\_ELC\_EVENT\_GPT2\_PC

| #define RA\_ELC\_EVENT\_GPT2\_PC   0x0BB |
| --- |

## [◆ ](#a74526500dfb573fe21fbca739b1698e1)RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_A   0x0BC |
| --- |

## [◆ ](#ac6cfac3496e4ab71c9bf84b43e06486a)RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT3\_CAPTURE\_COMPARE\_B   0x0BD |
| --- |

## [◆ ](#a1af4840d468eb4c4e1672a34652ef583)RA\_ELC\_EVENT\_GPT3\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_C   0x0BE |
| --- |

## [◆ ](#a263e6b02601dd37d6eedaab56a2e6fcd)RA\_ELC\_EVENT\_GPT3\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_D   0x0BF |
| --- |

## [◆ ](#a9035e080d39d60ecc898a596b9902aa6)RA\_ELC\_EVENT\_GPT3\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_E   0x0C0 |
| --- |

## [◆ ](#a9cffb5aca60a4c7349789fc23fb197fb)RA\_ELC\_EVENT\_GPT3\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT3\_COMPARE\_F   0x0C1 |
| --- |

## [◆ ](#a546eff128c44a29f56fe90952cef475d)RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT3\_COUNTER\_OVERFLOW   0x0C2 |
| --- |

## [◆ ](#ab30a5683e48535abbf0c400a5a0d8946)RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT3\_COUNTER\_UNDERFLOW   0x0C3 |
| --- |

## [◆ ](#ac39dad31699579a5ee3deebf4fc57cb4)RA\_ELC\_EVENT\_GPT3\_PC

| #define RA\_ELC\_EVENT\_GPT3\_PC   0x0C4 |
| --- |

## [◆ ](#a8130aa176d9d5dd698c62708111515e0)RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_A   0x0C5 |
| --- |

## [◆ ](#aa77a30a219070d15e358a43fbbd89728)RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT4\_CAPTURE\_COMPARE\_B   0x0C6 |
| --- |

## [◆ ](#af6c1cb172b343baa8d8bbe01d1674922)RA\_ELC\_EVENT\_GPT4\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_C   0x0C7 |
| --- |

## [◆ ](#ae8c7945c641045c615922a3f82329c56)RA\_ELC\_EVENT\_GPT4\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_D   0x0C8 |
| --- |

## [◆ ](#afcb271a94d9b07b7b1a204f325b80d52)RA\_ELC\_EVENT\_GPT4\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_E   0x0C9 |
| --- |

## [◆ ](#a906eb0e1ed2786ed2b14e4608489b2cc)RA\_ELC\_EVENT\_GPT4\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT4\_COMPARE\_F   0x0CA |
| --- |

## [◆ ](#abb820eb80ad8afc5c12dc3581fc7a0b9)RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT4\_COUNTER\_OVERFLOW   0x0CB |
| --- |

## [◆ ](#a65831ae6b037607dc55a2b1e8aa296a7)RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT4\_COUNTER\_UNDERFLOW   0x0CC |
| --- |

## [◆ ](#adc4aceff99f296b06938254f9dcc1f2f)RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_A   0x0CE |
| --- |

## [◆ ](#aad1fc8b32dffaaa64f9908951f8b1c64)RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT5\_CAPTURE\_COMPARE\_B   0x0CF |
| --- |

## [◆ ](#aebaa50f4643efe5b87798777cee578bc)RA\_ELC\_EVENT\_GPT5\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_C   0x0D0 |
| --- |

## [◆ ](#a21965e21bd4045aa5010925620b4d827)RA\_ELC\_EVENT\_GPT5\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_D   0x0D1 |
| --- |

## [◆ ](#a51a7cb146f0efbb7bc9f7336031006a4)RA\_ELC\_EVENT\_GPT5\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_E   0x0D2 |
| --- |

## [◆ ](#abbd0bd21af2bd1679d6d7bc36001b97d)RA\_ELC\_EVENT\_GPT5\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT5\_COMPARE\_F   0x0D3 |
| --- |

## [◆ ](#a038e7580f03fbdd74f417108cd2a8b4d)RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT5\_COUNTER\_OVERFLOW   0x0D4 |
| --- |

## [◆ ](#ac38b8f1154d6a699923b2bbf249e38fd)RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT5\_COUNTER\_UNDERFLOW   0x0D5 |
| --- |

## [◆ ](#acad1c37929903ddee569f40a3c5c59e3)RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_A   0x0D7 |
| --- |

## [◆ ](#aa0fc9b447efbcba0bb6800f785daeb96)RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT6\_CAPTURE\_COMPARE\_B   0x0D8 |
| --- |

## [◆ ](#a01f586bd98832ea9b8aa58741b61a319)RA\_ELC\_EVENT\_GPT6\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT6\_COMPARE\_C   0x0D9 |
| --- |

## [◆ ](#acd71c3b8e8e1d96aa3ff6affb93f5000)RA\_ELC\_EVENT\_GPT6\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT6\_COMPARE\_D   0x0DA |
| --- |

## [◆ ](#a6abdcc7a6331a8283cfe0c1ac06b7d83)RA\_ELC\_EVENT\_GPT6\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT6\_COMPARE\_E   0x0DB |
| --- |

## [◆ ](#a28b6b55ad533e3cb606b2b0937c916b3)RA\_ELC\_EVENT\_GPT6\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT6\_COMPARE\_F   0x0DC |
| --- |

## [◆ ](#ac3c8dd6a5b7f95dccc58e7ec4e235a40)RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT6\_COUNTER\_OVERFLOW   0x0DD |
| --- |

## [◆ ](#acdece33585a75fccba962e4f764058fb)RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT6\_COUNTER\_UNDERFLOW   0x0DE |
| --- |

## [◆ ](#afe1b39e5d37a5ed631dd18869cfbac8a)RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_A   0x0E0 |
| --- |

## [◆ ](#a53b7cfc8d0a000bd57f159b09b0a9c26)RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT7\_CAPTURE\_COMPARE\_B   0x0E1 |
| --- |

## [◆ ](#add91262eba9ec860b788030af153161a)RA\_ELC\_EVENT\_GPT7\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT7\_COMPARE\_C   0x0E2 |
| --- |

## [◆ ](#a9310fd708ca6f0afcf374bfc96e22e6e)RA\_ELC\_EVENT\_GPT7\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT7\_COMPARE\_D   0x0E3 |
| --- |

## [◆ ](#a8d18bd54c972d1de01c2a9f86e832cd0)RA\_ELC\_EVENT\_GPT7\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT7\_COMPARE\_E   0x0E4 |
| --- |

## [◆ ](#aca89f90e8afa3f656e76f5960717543c)RA\_ELC\_EVENT\_GPT7\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT7\_COMPARE\_F   0x0E5 |
| --- |

## [◆ ](#aac0ed7abde81cf4bcc7588bf64b53c04)RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT7\_COUNTER\_OVERFLOW   0x0E6 |
| --- |

## [◆ ](#ab1935670b6c0a5b5629ef8ba9d854f6c)RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT7\_COUNTER\_UNDERFLOW   0x0E7 |
| --- |

## [◆ ](#acbe756d66c556dab820bbba06e67248c)RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_A   0x0E9 |
| --- |

## [◆ ](#a86965f2d57f55861ddb995b2b1381aae)RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT8\_CAPTURE\_COMPARE\_B   0x0EA |
| --- |

## [◆ ](#af58a21982c9fb458bd12cf1d3922ffd2)RA\_ELC\_EVENT\_GPT8\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT8\_COMPARE\_C   0x0EB |
| --- |

## [◆ ](#a9d76f5a9c5546d1410b741ec7862713c)RA\_ELC\_EVENT\_GPT8\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT8\_COMPARE\_D   0x0EC |
| --- |

## [◆ ](#a9d6cf6e4081dd7ef14196fd754838224)RA\_ELC\_EVENT\_GPT8\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT8\_COMPARE\_E   0x0ED |
| --- |

## [◆ ](#abac4f8da4010bc5753188cc9bbce4feb)RA\_ELC\_EVENT\_GPT8\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT8\_COMPARE\_F   0x0EE |
| --- |

## [◆ ](#a560a2f23d31c99d46b5de3fb65b3c066)RA\_ELC\_EVENT\_GPT8\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT8\_COUNTER\_OVERFLOW   0x0EF |
| --- |

## [◆ ](#a217a7f7cdd39114472fc4276fc2337a2)RA\_ELC\_EVENT\_GPT8\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT8\_COUNTER\_UNDERFLOW   0x0F0 |
| --- |

## [◆ ](#a2170a5524be189decf2d098d082e24fe)RA\_ELC\_EVENT\_GPT8\_PC

| #define RA\_ELC\_EVENT\_GPT8\_PC   0x0F1 |
| --- |

## [◆ ](#a1b1bc8aa177575a9928b87d4270d3293)RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_A

| #define RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_A   0x0F2 |
| --- |

## [◆ ](#a9d37d2fabd4ff799c0b6a1f2e7131b50)RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_B

| #define RA\_ELC\_EVENT\_GPT9\_CAPTURE\_COMPARE\_B   0x0F3 |
| --- |

## [◆ ](#a0654be705490f32e47348cb31dea046d)RA\_ELC\_EVENT\_GPT9\_COMPARE\_C

| #define RA\_ELC\_EVENT\_GPT9\_COMPARE\_C   0x0F4 |
| --- |

## [◆ ](#af204da0f122a67c5374ebdcd231684b0)RA\_ELC\_EVENT\_GPT9\_COMPARE\_D

| #define RA\_ELC\_EVENT\_GPT9\_COMPARE\_D   0x0F5 |
| --- |

## [◆ ](#a7af6cbe91bfe594230d36a60a684877c)RA\_ELC\_EVENT\_GPT9\_COMPARE\_E

| #define RA\_ELC\_EVENT\_GPT9\_COMPARE\_E   0x0F6 |
| --- |

## [◆ ](#ad2ad78dddd8c2b7dc560ec75439870ce)RA\_ELC\_EVENT\_GPT9\_COMPARE\_F

| #define RA\_ELC\_EVENT\_GPT9\_COMPARE\_F   0x0F7 |
| --- |

## [◆ ](#ab5599f7f5509cbdae09668ec09078625)RA\_ELC\_EVENT\_GPT9\_COUNTER\_OVERFLOW

| #define RA\_ELC\_EVENT\_GPT9\_COUNTER\_OVERFLOW   0x0F8 |
| --- |

## [◆ ](#aab44882a60fd898b847597a64ad1ec05)RA\_ELC\_EVENT\_GPT9\_COUNTER\_UNDERFLOW

| #define RA\_ELC\_EVENT\_GPT9\_COUNTER\_UNDERFLOW   0x0F9 |
| --- |

## [◆ ](#acdae0456188e411e857278f0e543798d)RA\_ELC\_EVENT\_GPT9\_PC

| #define RA\_ELC\_EVENT\_GPT9\_PC   0x0FA |
| --- |

## [◆ ](#a1fdeb36ba55249ba92f2bdb425f18d74)RA\_ELC\_EVENT\_I3C0\_AMEV

| #define RA\_ELC\_EVENT\_I3C0\_AMEV   0x1AC |
| --- |

## [◆ ](#a92a8148f568fcf39ccde3817aef8ae9d)RA\_ELC\_EVENT\_I3C0\_COMMAND

| #define RA\_ELC\_EVENT\_I3C0\_COMMAND   0x19E |
| --- |

## [◆ ](#a7031d655983b5a153dec583b24df13fe)RA\_ELC\_EVENT\_I3C0\_EEI

| #define RA\_ELC\_EVENT\_I3C0\_EEI   0x1A8 |
| --- |

## [◆ ](#a41c98f2bad994edd460738fc681d1915)RA\_ELC\_EVENT\_I3C0\_HCMD

| #define RA\_ELC\_EVENT\_I3C0\_HCMD   0x1A4 |
| --- |

## [◆ ](#ad03e0236533be6c8a679f45dae45b5f3)RA\_ELC\_EVENT\_I3C0\_HRESP

| #define RA\_ELC\_EVENT\_I3C0\_HRESP   0x1A3 |
| --- |

## [◆ ](#a6944a47bc40eaf5be0bcd9a8ea3f61b3)RA\_ELC\_EVENT\_I3C0\_HRX

| #define RA\_ELC\_EVENT\_I3C0\_HRX   0x1A5 |
| --- |

## [◆ ](#a79b1703b94f1d6a62c589cd442d6c285)RA\_ELC\_EVENT\_I3C0\_HTX

| #define RA\_ELC\_EVENT\_I3C0\_HTX   0x1A6 |
| --- |

## [◆ ](#a2060363167f356732fb5b817e4dbcdb5)RA\_ELC\_EVENT\_I3C0\_IBI

| #define RA\_ELC\_EVENT\_I3C0\_IBI   0x19F |
| --- |

## [◆ ](#a53d989fdbde5fa99dfcb6226c3419ab9)RA\_ELC\_EVENT\_I3C0\_MREFCPT

| #define RA\_ELC\_EVENT\_I3C0\_MREFCPT   0x1AB |
| --- |

## [◆ ](#a80adbdbcc1c63c9623763c8aa595c3ca)RA\_ELC\_EVENT\_I3C0\_MREFOVF

| #define RA\_ELC\_EVENT\_I3C0\_MREFOVF   0x1AA |
| --- |

## [◆ ](#a0fe2a3ad8bf5bc9f9fbe79c2e3142a82)RA\_ELC\_EVENT\_I3C0\_RCV\_STATUS

| #define RA\_ELC\_EVENT\_I3C0\_RCV\_STATUS   0x1A2 |
| --- |

## [◆ ](#a3080239b71b12d15d9cd78d78a0b65e6)RA\_ELC\_EVENT\_I3C0\_RESPONSE

| #define RA\_ELC\_EVENT\_I3C0\_RESPONSE   0x19D |
| --- |

## [◆ ](#a3b2265686fb51c1ae5cdc549cac4b3fd)RA\_ELC\_EVENT\_I3C0\_RX

| #define RA\_ELC\_EVENT\_I3C0\_RX   0x1A0 |
| --- |

## [◆ ](#a57e6e464e10dc72ef057cb24530f26cc)RA\_ELC\_EVENT\_I3C0\_STEV

| #define RA\_ELC\_EVENT\_I3C0\_STEV   0x1A9 |
| --- |

## [◆ ](#a263d9beac3bda75a81b657995262df84)RA\_ELC\_EVENT\_I3C0\_TEND

| #define RA\_ELC\_EVENT\_I3C0\_TEND   0x1A7 |
| --- |

## [◆ ](#a6bd966e36dba524e3e5ad37250d9a2fe)RA\_ELC\_EVENT\_I3C0\_TX

| #define RA\_ELC\_EVENT\_I3C0\_TX   0x1A1 |
| --- |

## [◆ ](#a979332348cebe774723bfd610b02c36b)RA\_ELC\_EVENT\_I3C0\_WU

| #define RA\_ELC\_EVENT\_I3C0\_WU   0x1AD |
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

## [◆ ](#a667eb763b55f973b141837e82dbbae6e)RA\_ELC\_EVENT\_IIC0\_ERI

| #define RA\_ELC\_EVENT\_IIC0\_ERI   0x05F |
| --- |

## [◆ ](#a7271a25cdc3c987313efbafcd2a746cf)RA\_ELC\_EVENT\_IIC0\_RXI

| #define RA\_ELC\_EVENT\_IIC0\_RXI   0x05C |
| --- |

## [◆ ](#a52270344b26073c127a0269c5ec4e228)RA\_ELC\_EVENT\_IIC0\_TEI

| #define RA\_ELC\_EVENT\_IIC0\_TEI   0x05E |
| --- |

## [◆ ](#a7843f8a23feb383202fa6ad3be8fae5c)RA\_ELC\_EVENT\_IIC0\_TXI

| #define RA\_ELC\_EVENT\_IIC0\_TXI   0x05D |
| --- |

## [◆ ](#a2a074dab614a1639ea5fa4f6d3baffd3)RA\_ELC\_EVENT\_IIC0\_WUI

| #define RA\_ELC\_EVENT\_IIC0\_WUI   0x060 |
| --- |

## [◆ ](#a2221a129f0e323fa5b96bfe5ed0e007f)RA\_ELC\_EVENT\_IIC1\_ERI

| #define RA\_ELC\_EVENT\_IIC1\_ERI   0x064 |
| --- |

## [◆ ](#ad03e6b81d0e7ce53737e5c3022f8d951)RA\_ELC\_EVENT\_IIC1\_RXI

| #define RA\_ELC\_EVENT\_IIC1\_RXI   0x061 |
| --- |

## [◆ ](#a45ed226ccaace8813aa653276a52999d)RA\_ELC\_EVENT\_IIC1\_TEI

| #define RA\_ELC\_EVENT\_IIC1\_TEI   0x063 |
| --- |

## [◆ ](#a641c91157c98f41d3cf5ff6bbe25192d)RA\_ELC\_EVENT\_IIC1\_TXI

| #define RA\_ELC\_EVENT\_IIC1\_TXI   0x062 |
| --- |

## [◆ ](#ac0d8b1e8f379ef983dfd2004ed02e65e)RA\_ELC\_EVENT\_IICB0\_ERI

| #define RA\_ELC\_EVENT\_IICB0\_ERI   0x1A8 |
| --- |

## [◆ ](#ac12a24178c5964cdd58666f7d57a1b1b)RA\_ELC\_EVENT\_IICB0\_RXI

| #define RA\_ELC\_EVENT\_IICB0\_RXI   0x1A0 |
| --- |

## [◆ ](#accb1b88c154566410d539b20c64f67cc)RA\_ELC\_EVENT\_IICB0\_TEI

| #define RA\_ELC\_EVENT\_IICB0\_TEI   0x1A7 |
| --- |

## [◆ ](#ac3f18d838eb617f5022034a38238b3da)RA\_ELC\_EVENT\_IICB0\_TXI

| #define RA\_ELC\_EVENT\_IICB0\_TXI   0x1A1 |
| --- |

## [◆ ](#aee58e9a0c4313f0ec08f0652e5002008)RA\_ELC\_EVENT\_IOPORT\_EVENT\_1

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_1   0x088 |
| --- |

## [◆ ](#a36d858520d28847eead0fbfe7950be2d)RA\_ELC\_EVENT\_IOPORT\_EVENT\_2

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_2   0x089 |
| --- |

## [◆ ](#a545dadce70bbcea1116cd13490fe2571)RA\_ELC\_EVENT\_IOPORT\_EVENT\_3

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_3   0x08A |
| --- |

## [◆ ](#a4e478b84ef99ae71c102ad3d5c71089a)RA\_ELC\_EVENT\_IOPORT\_EVENT\_4

| #define RA\_ELC\_EVENT\_IOPORT\_EVENT\_4   0x08B |
| --- |

## [◆ ](#abc837f1fcfffeb2ec231c79336379dda)RA\_ELC\_EVENT\_IWDT\_UNDERFLOW

| #define RA\_ELC\_EVENT\_IWDT\_UNDERFLOW   0x052 |
| --- |

## [◆ ](#a7ab275777147d06315a04abb3f2f6d51)RA\_ELC\_EVENT\_LVD\_LVD1

| #define RA\_ELC\_EVENT\_LVD\_LVD1   0x038 |
| --- |

## [◆ ](#ad52acadba107b7f907d678f44769a4cb)RA\_ELC\_EVENT\_LVD\_LVD2

| #define RA\_ELC\_EVENT\_LVD\_LVD2   0x039 |
| --- |

## [◆ ](#a45075f80238882f18a0f4bcaf37bfd58)RA\_ELC\_EVENT\_MIPIDSI\_FERR

| #define RA\_ELC\_EVENT\_MIPIDSI\_FERR   0x1D7 |
| --- |

## [◆ ](#a2658eba6f63e4ca5c2f3a45c7b5c791d)RA\_ELC\_EVENT\_MIPIDSI\_PPI

| #define RA\_ELC\_EVENT\_MIPIDSI\_PPI   0x1D8 |
| --- |

## [◆ ](#a3698b91ae9aef8085388be626b134d56)RA\_ELC\_EVENT\_MIPIDSI\_RCV

| #define RA\_ELC\_EVENT\_MIPIDSI\_RCV   0x1D6 |
| --- |

## [◆ ](#ac331540e98f0405e5d1a03b9c7b85006)RA\_ELC\_EVENT\_MIPIDSI\_SEQ0

| #define RA\_ELC\_EVENT\_MIPIDSI\_SEQ0   0x1D3 |
| --- |

## [◆ ](#abb3a66beb2d4902bcd8495577d1ae54f)RA\_ELC\_EVENT\_MIPIDSI\_SEQ1

| #define RA\_ELC\_EVENT\_MIPIDSI\_SEQ1   0x1D4 |
| --- |

## [◆ ](#aa20efc3b9e2d2f8ebab178eae2b0df5d)RA\_ELC\_EVENT\_MIPIDSI\_VIN1

| #define RA\_ELC\_EVENT\_MIPIDSI\_VIN1   0x1D5 |
| --- |

## [◆ ](#a11b5cec97472328120a8d6381f1e8809)RA\_ELC\_EVENT\_NONE

| #define RA\_ELC\_EVENT\_NONE   0x0 |
| --- |

## [◆ ](#a8438d8d92e1950681388b40385a2c354)RA\_ELC\_EVENT\_OPS\_UVW\_EDGE

| #define RA\_ELC\_EVENT\_OPS\_UVW\_EDGE   0x0A0 |
| --- |

## [◆ ](#a81e18423a1f61e34f0daab6f7367eae2)RA\_ELC\_EVENT\_POEG0\_EVENT

| #define RA\_ELC\_EVENT\_POEG0\_EVENT   0x08F |
| --- |

## [◆ ](#a2a43c2ce461fde766e66a4451929a875)RA\_ELC\_EVENT\_POEG1\_EVENT

| #define RA\_ELC\_EVENT\_POEG1\_EVENT   0x090 |
| --- |

## [◆ ](#a7b5c16202b2491ba77319a180bcaa107)RA\_ELC\_EVENT\_POEG2\_EVENT

| #define RA\_ELC\_EVENT\_POEG2\_EVENT   0x091 |
| --- |

## [◆ ](#ab39d06b130b93348c5fab589f1e0074e)RA\_ELC\_EVENT\_POEG3\_EVENT

| #define RA\_ELC\_EVENT\_POEG3\_EVENT   0x092 |
| --- |

## [◆ ](#a0b76751d4c1e7f98ec6de2633cca4057)RA\_ELC\_EVENT\_RSIP\_TADI

| #define RA\_ELC\_EVENT\_RSIP\_TADI   0x1BC |
| --- |

## [◆ ](#a76fd68b555574159d563d2dfd68d90b9)RA\_ELC\_EVENT\_RTC\_ALARM

| #define RA\_ELC\_EVENT\_RTC\_ALARM   0x055 |
| --- |

## [◆ ](#a241cd3c65033b46a1160d5815cc86fd7)RA\_ELC\_EVENT\_RTC\_CARRY

| #define RA\_ELC\_EVENT\_RTC\_CARRY   0x057 |
| --- |

## [◆ ](#a144901ee7b31b96eba18a39d98c4b953)RA\_ELC\_EVENT\_RTC\_PERIOD

| #define RA\_ELC\_EVENT\_RTC\_PERIOD   0x056 |
| --- |

## [◆ ](#ad8c85ee25e4bbc5563d9878156232f8e)RA\_ELC\_EVENT\_SCI0\_AED

| #define RA\_ELC\_EVENT\_SCI0\_AED   0x128 |
| --- |

## [◆ ](#ae2373b571584dae4d1c7fc57142ecb3c)RA\_ELC\_EVENT\_SCI0\_AM

| #define RA\_ELC\_EVENT\_SCI0\_AM   0x12A |
| --- |

## [◆ ](#a624bb86f4c26e04cc4b044b2f3f4aec9)RA\_ELC\_EVENT\_SCI0\_BFD

| #define RA\_ELC\_EVENT\_SCI0\_BFD   0x129 |
| --- |

## [◆ ](#ad4580e769bae423298276e31ee2ee071)RA\_ELC\_EVENT\_SCI0\_ERI

| #define RA\_ELC\_EVENT\_SCI0\_ERI   0x127 |
| --- |

## [◆ ](#ad9e9a8451a683c5b5bc8a2ace8264c27)RA\_ELC\_EVENT\_SCI0\_RXI

| #define RA\_ELC\_EVENT\_SCI0\_RXI   0x124 |
| --- |

## [◆ ](#ae845a850ab730c651badc5c857e28ee9)RA\_ELC\_EVENT\_SCI0\_TEI

| #define RA\_ELC\_EVENT\_SCI0\_TEI   0x126 |
| --- |

## [◆ ](#aecc4fdda2a7eeb2bab0b894f2e5047d9)RA\_ELC\_EVENT\_SCI0\_TXI

| #define RA\_ELC\_EVENT\_SCI0\_TXI   0x125 |
| --- |

## [◆ ](#a85f1cff0bee1f3394e53dc4180fecbda)RA\_ELC\_EVENT\_SCI1\_AED

| #define RA\_ELC\_EVENT\_SCI1\_AED   0x12F |
| --- |

## [◆ ](#ad9ca7dbcac36bb7f921cd8b8db761623)RA\_ELC\_EVENT\_SCI1\_AM

| #define RA\_ELC\_EVENT\_SCI1\_AM   0x131 |
| --- |

## [◆ ](#ae20f8922e54edb56904b397b6e77fda2)RA\_ELC\_EVENT\_SCI1\_BFD

| #define RA\_ELC\_EVENT\_SCI1\_BFD   0x130 |
| --- |

## [◆ ](#a6a673466eb5261d23ee06be132ca9cde)RA\_ELC\_EVENT\_SCI1\_ERI

| #define RA\_ELC\_EVENT\_SCI1\_ERI   0x12E |
| --- |

## [◆ ](#ae936e9aa971a376cb4ea3405c68d57f0)RA\_ELC\_EVENT\_SCI1\_RXI

| #define RA\_ELC\_EVENT\_SCI1\_RXI   0x12B |
| --- |

## [◆ ](#aae0ca4a1031af4c490fbb1ecbe201662)RA\_ELC\_EVENT\_SCI1\_TEI

| #define RA\_ELC\_EVENT\_SCI1\_TEI   0x12D |
| --- |

## [◆ ](#abd1c6187f97f2817dc5eb59278a996b1)RA\_ELC\_EVENT\_SCI1\_TXI

| #define RA\_ELC\_EVENT\_SCI1\_TXI   0x12C |
| --- |

## [◆ ](#a023110baac3b030238844ab6a8999652)RA\_ELC\_EVENT\_SCI2\_AM

| #define RA\_ELC\_EVENT\_SCI2\_AM   0x138 |
| --- |

## [◆ ](#ad31428c7900c978dba266761df793f4c)RA\_ELC\_EVENT\_SCI2\_ERI

| #define RA\_ELC\_EVENT\_SCI2\_ERI   0x135 |
| --- |

## [◆ ](#a484b0928fab1e96f3008b9e7b12bab07)RA\_ELC\_EVENT\_SCI2\_RXI

| #define RA\_ELC\_EVENT\_SCI2\_RXI   0x132 |
| --- |

## [◆ ](#a9bbdd2f449bfd5709f6c8b77b8378ca4)RA\_ELC\_EVENT\_SCI2\_TEI

| #define RA\_ELC\_EVENT\_SCI2\_TEI   0x134 |
| --- |

## [◆ ](#a5991f7636af52ea3285cf17d300f62bb)RA\_ELC\_EVENT\_SCI2\_TXI

| #define RA\_ELC\_EVENT\_SCI2\_TXI   0x133 |
| --- |

## [◆ ](#a075f80d14abaa63627574519b9ebf36b)RA\_ELC\_EVENT\_SCI3\_AM

| #define RA\_ELC\_EVENT\_SCI3\_AM   0x13F |
| --- |

## [◆ ](#ab7a6ad3ccc6279863a491a3787fd5c5e)RA\_ELC\_EVENT\_SCI3\_ERI

| #define RA\_ELC\_EVENT\_SCI3\_ERI   0x13C |
| --- |

## [◆ ](#a87a1f07a2b420f9ce8d7ebcc1c505986)RA\_ELC\_EVENT\_SCI3\_RXI

| #define RA\_ELC\_EVENT\_SCI3\_RXI   0x139 |
| --- |

## [◆ ](#a6f9d20424191f026030159511647f913)RA\_ELC\_EVENT\_SCI3\_TEI

| #define RA\_ELC\_EVENT\_SCI3\_TEI   0x13B |
| --- |

## [◆ ](#aee0548d7714ebd04748eadf9e9dbb97c)RA\_ELC\_EVENT\_SCI3\_TXI

| #define RA\_ELC\_EVENT\_SCI3\_TXI   0x13A |
| --- |

## [◆ ](#abddf2cbec24fd59c9330b0328a21f82e)RA\_ELC\_EVENT\_SCI4\_AM

| #define RA\_ELC\_EVENT\_SCI4\_AM   0x146 |
| --- |

## [◆ ](#ac6f2b3938cde7ba80faf523548dfa6c2)RA\_ELC\_EVENT\_SCI4\_ERI

| #define RA\_ELC\_EVENT\_SCI4\_ERI   0x143 |
| --- |

## [◆ ](#afe86466482eb03b85da9feb17bdccfc0)RA\_ELC\_EVENT\_SCI4\_RXI

| #define RA\_ELC\_EVENT\_SCI4\_RXI   0x140 |
| --- |

## [◆ ](#a2554192500a5ac058fbd338d3018f6cc)RA\_ELC\_EVENT\_SCI4\_TEI

| #define RA\_ELC\_EVENT\_SCI4\_TEI   0x142 |
| --- |

## [◆ ](#a89f26e1bfd92cb7c9a2bad9acd80e553)RA\_ELC\_EVENT\_SCI4\_TXI

| #define RA\_ELC\_EVENT\_SCI4\_TXI   0x141 |
| --- |

## [◆ ](#a2bfc7def09c933262aa530227a45af7d)RA\_ELC\_EVENT\_SCI9\_AM

| #define RA\_ELC\_EVENT\_SCI9\_AM   0x169 |
| --- |

## [◆ ](#af2e4d2d6b59c512e536d901789b3c1a2)RA\_ELC\_EVENT\_SCI9\_ERI

| #define RA\_ELC\_EVENT\_SCI9\_ERI   0x166 |
| --- |

## [◆ ](#ac01e51a9360f409e430642d86818bf98)RA\_ELC\_EVENT\_SCI9\_RXI

| #define RA\_ELC\_EVENT\_SCI9\_RXI   0x163 |
| --- |

## [◆ ](#ac3a064375ff90f3a6a35c5fdda680f95)RA\_ELC\_EVENT\_SCI9\_TEI

| #define RA\_ELC\_EVENT\_SCI9\_TEI   0x165 |
| --- |

## [◆ ](#a8c628c59b08ed53781fd406ea22da796)RA\_ELC\_EVENT\_SCI9\_TXI

| #define RA\_ELC\_EVENT\_SCI9\_TXI   0x164 |
| --- |

## [◆ ](#a5d9c7d15a5c040aa9dfe002cf9df0657)RA\_ELC\_EVENT\_SDHIMMC0\_ACCS

| #define RA\_ELC\_EVENT\_SDHIMMC0\_ACCS   0x06B |
| --- |

## [◆ ](#a2bf8474e011e2ec0360e9e46deb7e960)RA\_ELC\_EVENT\_SDHIMMC0\_CARD

| #define RA\_ELC\_EVENT\_SDHIMMC0\_CARD   0x06D |
| --- |

## [◆ ](#a937bfe3314fb8d78775078db983ea473)RA\_ELC\_EVENT\_SDHIMMC0\_DMA\_REQ

| #define RA\_ELC\_EVENT\_SDHIMMC0\_DMA\_REQ   0x06E |
| --- |

## [◆ ](#a93465058fd23dad3a735a53ad8689473)RA\_ELC\_EVENT\_SDHIMMC0\_SDIO

| #define RA\_ELC\_EVENT\_SDHIMMC0\_SDIO   0x06C |
| --- |

## [◆ ](#a7195add88b927dd230e66a931713f4e0)RA\_ELC\_EVENT\_SDHIMMC1\_ACCS

| #define RA\_ELC\_EVENT\_SDHIMMC1\_ACCS   0x06F |
| --- |

## [◆ ](#ae8b2102091696bca7f60b008b9839444)RA\_ELC\_EVENT\_SDHIMMC1\_CARD

| #define RA\_ELC\_EVENT\_SDHIMMC1\_CARD   0x071 |
| --- |

## [◆ ](#a3b619f3e51ddcf2add17abd434bbf948)RA\_ELC\_EVENT\_SDHIMMC1\_DMA\_REQ

| #define RA\_ELC\_EVENT\_SDHIMMC1\_DMA\_REQ   0x072 |
| --- |

## [◆ ](#a2dff7e869fad7918164e954bcb0a46bf)RA\_ELC\_EVENT\_SDHIMMC1\_SDIO

| #define RA\_ELC\_EVENT\_SDHIMMC1\_SDIO   0x070 |
| --- |

## [◆ ](#ab588fafc974153bcf94087cdb1a71d73)RA\_ELC\_EVENT\_SPI0\_ERI

| #define RA\_ELC\_EVENT\_SPI0\_ERI   0x17B |
| --- |

## [◆ ](#a920575ee3a202b0d7202cd053f1e235b)RA\_ELC\_EVENT\_SPI0\_IDLE

| #define RA\_ELC\_EVENT\_SPI0\_IDLE   0x17A |
| --- |

## [◆ ](#af77608914a79bea7797b63674c71db31)RA\_ELC\_EVENT\_SPI0\_RXI

| #define RA\_ELC\_EVENT\_SPI0\_RXI   0x178 |
| --- |

## [◆ ](#a368a0ece3d89efe3ed8ab274471849b9)RA\_ELC\_EVENT\_SPI0\_TEI

| #define RA\_ELC\_EVENT\_SPI0\_TEI   0x17C |
| --- |

## [◆ ](#a82d87016b5d694884bba33bf71e93e92)RA\_ELC\_EVENT\_SPI0\_TXI

| #define RA\_ELC\_EVENT\_SPI0\_TXI   0x179 |
| --- |

## [◆ ](#aedf36efaaba39c4001386536d21f81e2)RA\_ELC\_EVENT\_SPI1\_ERI

| #define RA\_ELC\_EVENT\_SPI1\_ERI   0x180 |
| --- |

## [◆ ](#a73da76e435d9de6b6b7ad48190d2c0a2)RA\_ELC\_EVENT\_SPI1\_IDLE

| #define RA\_ELC\_EVENT\_SPI1\_IDLE   0x17F |
| --- |

## [◆ ](#a2f5e3b5957e42c572fda94ec535b401b)RA\_ELC\_EVENT\_SPI1\_RXI

| #define RA\_ELC\_EVENT\_SPI1\_RXI   0x17D |
| --- |

## [◆ ](#a60f40983e3c6344a257bd157b40069d5)RA\_ELC\_EVENT\_SPI1\_TEI

| #define RA\_ELC\_EVENT\_SPI1\_TEI   0x181 |
| --- |

## [◆ ](#a0aab8e60c14b34bccb74400a818524ac)RA\_ELC\_EVENT\_SPI1\_TXI

| #define RA\_ELC\_EVENT\_SPI1\_TXI   0x17E |
| --- |

## [◆ ](#a1a89e9ab6abb3834992ee3ea3ebaf9c4)RA\_ELC\_EVENT\_SSI0\_INT

| #define RA\_ELC\_EVENT\_SSI0\_INT   0x076 |
| --- |

## [◆ ](#ab736656ae0b06de8383189075cbb2f27)RA\_ELC\_EVENT\_SSI0\_RXI

| #define RA\_ELC\_EVENT\_SSI0\_RXI   0x074 |
| --- |

## [◆ ](#ac65193048ce5734b46bc2bf77b84cb4e)RA\_ELC\_EVENT\_SSI0\_TXI

| #define RA\_ELC\_EVENT\_SSI0\_TXI   0x073 |
| --- |

## [◆ ](#a79f16ecce139415dc0c4b975bccc7f11)RA\_ELC\_EVENT\_SSI1\_INT

| #define RA\_ELC\_EVENT\_SSI1\_INT   0x07A |
| --- |

## [◆ ](#a6c41f242f807ea904423f537d87b4df2)RA\_ELC\_EVENT\_SSI1\_RXI

| #define RA\_ELC\_EVENT\_SSI1\_RXI   0x079 |
| --- |

## [◆ ](#a209699f601f2f9f29a44b2d1ee33713d)RA\_ELC\_EVENT\_SSI1\_TXI

| #define RA\_ELC\_EVENT\_SSI1\_TXI   0x079 |
| --- |

## [◆ ](#a202b4f22442dfef11d4402c41cdbb978)RA\_ELC\_EVENT\_SSI1\_TXI\_RXI

| #define RA\_ELC\_EVENT\_SSI1\_TXI\_RXI   0x079 |
| --- |

## [◆ ](#a69ec3e618136c55cebeb2d76fc2e88ba)RA\_ELC\_EVENT\_ULPT0\_COMPARE\_A

| #define RA\_ELC\_EVENT\_ULPT0\_COMPARE\_A   0x041 |
| --- |

## [◆ ](#ac954387c6092e77e6002997f93e4d10e)RA\_ELC\_EVENT\_ULPT0\_COMPARE\_B

| #define RA\_ELC\_EVENT\_ULPT0\_COMPARE\_B   0x042 |
| --- |

## [◆ ](#aecaa6cbbfd3a5e0007a00fd11edc204d)RA\_ELC\_EVENT\_ULPT0\_INT

| #define RA\_ELC\_EVENT\_ULPT0\_INT   0x040 |
| --- |

## [◆ ](#a77531873ba01d812a3f5614059016cf6)RA\_ELC\_EVENT\_ULPT1\_COMPARE\_A

| #define RA\_ELC\_EVENT\_ULPT1\_COMPARE\_A   0x044 |
| --- |

## [◆ ](#aadb4d755431beb28984de1e962402a39)RA\_ELC\_EVENT\_ULPT1\_COMPARE\_B

| #define RA\_ELC\_EVENT\_ULPT1\_COMPARE\_B   0x045 |
| --- |

## [◆ ](#ac313fdd1b0179ee96d36532504592305)RA\_ELC\_EVENT\_ULPT1\_INT

| #define RA\_ELC\_EVENT\_ULPT1\_INT   0x043 |
| --- |

## [◆ ](#ae4dbb89c58220f72818cc9c28d97905b)RA\_ELC\_EVENT\_USBFS\_FIFO\_0

| #define RA\_ELC\_EVENT\_USBFS\_FIFO\_0   0x058 |
| --- |

## [◆ ](#a0ef2efa2ea339cad7598f11fe549cdd9)RA\_ELC\_EVENT\_USBFS\_FIFO\_1

| #define RA\_ELC\_EVENT\_USBFS\_FIFO\_1   0x059 |
| --- |

## [◆ ](#aac8d97813e8a3276bdac764faf7b580d)RA\_ELC\_EVENT\_USBFS\_INT

| #define RA\_ELC\_EVENT\_USBFS\_INT   0x05A |
| --- |

## [◆ ](#a9458dbf2b1da6fc51ca2c2933dcb6b37)RA\_ELC\_EVENT\_USBFS\_RESUME

| #define RA\_ELC\_EVENT\_USBFS\_RESUME   0x05B |
| --- |

## [◆ ](#a1f824a01b81720cfd0fd63603f446567)RA\_ELC\_EVENT\_USBHS\_FIFO\_0

| #define RA\_ELC\_EVENT\_USBHS\_FIFO\_0   0x121 |
| --- |

## [◆ ](#a39b1f6234c0f4e3a27663410e748b2c4)RA\_ELC\_EVENT\_USBHS\_FIFO\_1

| #define RA\_ELC\_EVENT\_USBHS\_FIFO\_1   0x122 |
| --- |

## [◆ ](#a650605a9b87c871a6f29efb4d029f346)RA\_ELC\_EVENT\_USBHS\_USB\_INT\_RESUME

| #define RA\_ELC\_EVENT\_USBHS\_USB\_INT\_RESUME   0x123 |
| --- |

## [◆ ](#a61f5922105d7d213f9c4dba773a1252f)RA\_ELC\_EVENT\_VBATT\_TADI

| #define RA\_ELC\_EVENT\_VBATT\_TADI   0x03D |
| --- |

## [◆ ](#aef90868206c735f311c2f95644f562b1)RA\_ELC\_EVENT\_WDT0\_UNDERFLOW

| #define RA\_ELC\_EVENT\_WDT0\_UNDERFLOW   0x053 |
| --- |

## [◆ ](#a8209ca1ee92cb61da174f6d0c48b5220)RA\_ELC\_EVENT\_XSPI\_CMP

| #define RA\_ELC\_EVENT\_XSPI\_CMP   0x183 |
| --- |

## [◆ ](#a88aee6cf6092e69ee117b12f000d83d9)RA\_ELC\_EVENT\_XSPI\_ERR

| #define RA\_ELC\_EVENT\_XSPI\_ERR   0x182 |
| --- |

## [◆ ](#a2b5a9232a4ad9d199dc9baa510d0ed54)RA\_ELC\_PERIPHERAL\_ADC0

| #define RA\_ELC\_PERIPHERAL\_ADC0   8 |
| --- |

## [◆ ](#afaf4059726139d62e2c09010cfa1148a)RA\_ELC\_PERIPHERAL\_ADC0\_B

| #define RA\_ELC\_PERIPHERAL\_ADC0\_B   9 |
| --- |

## [◆ ](#aea69e6e72e14f53afeb85aa4a9349bcb)RA\_ELC\_PERIPHERAL\_ADC1

| #define RA\_ELC\_PERIPHERAL\_ADC1   10 |
| --- |

## [◆ ](#adbd2118aea6d1ba6ca67de192f0033fc)RA\_ELC\_PERIPHERAL\_ADC1\_B

| #define RA\_ELC\_PERIPHERAL\_ADC1\_B   11 |
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

| #define RA\_ELC\_PERIPHERAL\_I3C   30 |
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
- [ra8d1-elc.h](ra8d1-elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
