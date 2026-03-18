---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/can__mcan_8h_source.html
original_path: doxygen/html/can__mcan_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan.h

[Go to the documentation of this file.](can__mcan_8h.md)

1/\*

2 \* Copyright (c) 2023 Vestas Wind Systems A/S

3 \* Copyright (c) 2020 Alexander Wachter

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_MCAN\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_MCAN\_H\_

11

12#include <[zephyr/cache.h](cache_8h.md)>

13#include <[zephyr/devicetree.h](devicetree_8h.md)>

14#include <[zephyr/drivers/can.h](drivers_2can_8h.md)>

15#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

16#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

17#include <[zephyr/sys/util.h](util_8h.md)>

18

19/\*

20 \* The Bosch M\_CAN register definitions correspond to those found in the Bosch M\_CAN Controller Area

21 \* Network User's Manual, Revision 3.3.0.

22 \*/

23

24/\* Core Release register \*/

[ 25](can__mcan_8h.md#acc741a42cb2d052ae773aebb95e44616)#define CAN\_MCAN\_CREL 0x000

[ 26](can__mcan_8h.md#a8cedb6b6ed4ace3a38f170fc4ce65647)#define CAN\_MCAN\_CREL\_REL GENMASK(31, 28)

[ 27](can__mcan_8h.md#a39282c299129a3a7e902c6a120568bce)#define CAN\_MCAN\_CREL\_STEP GENMASK(27, 24)

[ 28](can__mcan_8h.md#ac28c0effa82ad6fefad5dd5c9079800a)#define CAN\_MCAN\_CREL\_SUBSTEP GENMASK(23, 20)

[ 29](can__mcan_8h.md#a7139e7a57e58fe4f8572c5d7784e67d2)#define CAN\_MCAN\_CREL\_YEAR GENMASK(19, 16)

[ 30](can__mcan_8h.md#abc36710e20ac587cacf18e1e74434e6d)#define CAN\_MCAN\_CREL\_MON GENMASK(15, 8)

[ 31](can__mcan_8h.md#a89eebb76c2b98f12e56eaf3885cae9e5)#define CAN\_MCAN\_CREL\_DAY GENMASK(7, 0)

32

33/\* Endian register \*/

[ 34](can__mcan_8h.md#ae130ab74797ec4affc8052a334995dd8)#define CAN\_MCAN\_ENDN 0x004

[ 35](can__mcan_8h.md#a1dcceef7aa2e13c90551e677a32f836b)#define CAN\_MCAN\_ENDN\_ETV GENMASK(31, 0)

36

37/\* Customer register \*/

[ 38](can__mcan_8h.md#a60dab0513bb60fdaaeb3ad9eb8589b0b)#define CAN\_MCAN\_CUST 0x008

[ 39](can__mcan_8h.md#aa85321c44c2f8ce6f4e3abfecaac4309)#define CAN\_MCAN\_CUST\_CUST GENMASK(31, 0)

40

41/\* Data Bit Timing & Prescaler register \*/

[ 42](can__mcan_8h.md#a3643ab9ba53749dd417515e868005822)#define CAN\_MCAN\_DBTP 0x00C

[ 43](can__mcan_8h.md#a553232f28f3dcba55eb2e71619cceb10)#define CAN\_MCAN\_DBTP\_TDC BIT(23)

[ 44](can__mcan_8h.md#a1697f9a668977dae709f6f5c5c06cec0)#define CAN\_MCAN\_DBTP\_DBRP GENMASK(20, 16)

[ 45](can__mcan_8h.md#a79af67b99451850bbfb3b6fe3f9a1502)#define CAN\_MCAN\_DBTP\_DTSEG1 GENMASK(12, 8)

[ 46](can__mcan_8h.md#a4f6a9528366c7ed61d6b9e5c1fe6e52d)#define CAN\_MCAN\_DBTP\_DTSEG2 GENMASK(7, 4)

[ 47](can__mcan_8h.md#a010cfca29045f0f643cdacefb6560491)#define CAN\_MCAN\_DBTP\_DSJW GENMASK(3, 0)

48

49/\* Test register \*/

[ 50](can__mcan_8h.md#ad97d62d4799b07bc5a8405f7ace52708)#define CAN\_MCAN\_TEST 0x010

[ 51](can__mcan_8h.md#aa8ad1bcbf0ce358b91810f5349bab4db)#define CAN\_MCAN\_TEST\_SVAL BIT(21)

[ 52](can__mcan_8h.md#a28c34733629bef3c9e83add27ceca147)#define CAN\_MCAN\_TEST\_TXBNS GENMASK(20, 16)

[ 53](can__mcan_8h.md#a8210ab176d182b1b1fec7f5fc8f6e44e)#define CAN\_MCAN\_TEST\_PVAL BIT(13)

[ 54](can__mcan_8h.md#aaf9280049a3e2365f9ec7627009989f1)#define CAN\_MCAN\_TEST\_TXBNP GENMASK(12, 8)

[ 55](can__mcan_8h.md#ad4110c5f53f0632694aebef5eab54a54)#define CAN\_MCAN\_TEST\_RX BIT(7)

[ 56](can__mcan_8h.md#a207ba0562c9e4e4a10cdee1ad524a1c0)#define CAN\_MCAN\_TEST\_TX GENMASK(6, 5)

[ 57](can__mcan_8h.md#aee2a84f2613145af78c97da48781382e)#define CAN\_MCAN\_TEST\_LBCK BIT(4)

58

59/\* RAM Watchdog register \*/

[ 60](can__mcan_8h.md#ab646e1d2f8a14239b31e54a4728bad81)#define CAN\_MCAN\_RWD 0x014

[ 61](can__mcan_8h.md#a639a100e4d8438784faeafdb20df0d35)#define CAN\_MCAN\_RWD\_WDV GENMASK(15, 8)

[ 62](can__mcan_8h.md#a0a64ee92dd024b35047794c8cbb05f6a)#define CAN\_MCAN\_RWD\_WDC GENMASK(7, 0)

63

64/\* CC Control register \*/

[ 65](can__mcan_8h.md#a33d42748a911e6a337324652ac982c9b)#define CAN\_MCAN\_CCCR 0x018

[ 66](can__mcan_8h.md#a430a606d5de2f7cf5958fe1d88ce931e)#define CAN\_MCAN\_CCCR\_NISO BIT(15)

[ 67](can__mcan_8h.md#ae091024f68ea83d6f888bcadb99e137c)#define CAN\_MCAN\_CCCR\_TXP BIT(14)

[ 68](can__mcan_8h.md#ab773d5e87290745fb1958d23720cfbdb)#define CAN\_MCAN\_CCCR\_EFBI BIT(13)

[ 69](can__mcan_8h.md#ac5283b03eb7b498fd64e01477bfff300)#define CAN\_MCAN\_CCCR\_PXHD BIT(12)

[ 70](can__mcan_8h.md#aab0183fea6cd4dd560b83b2d2049bd75)#define CAN\_MCAN\_CCCR\_WMM BIT(11)

[ 71](can__mcan_8h.md#a7c424b839fd4ebe69fa9615bc3cb7268)#define CAN\_MCAN\_CCCR\_UTSU BIT(10)

[ 72](can__mcan_8h.md#ace20dbd7d279909999e19dd2a6a82ec9)#define CAN\_MCAN\_CCCR\_BRSE BIT(9)

[ 73](can__mcan_8h.md#a26154a84a6124bd8cceae4c0929d6937)#define CAN\_MCAN\_CCCR\_FDOE BIT(8)

[ 74](can__mcan_8h.md#af74a4cf81df6d88f8a69db622d71da83)#define CAN\_MCAN\_CCCR\_TEST BIT(7)

[ 75](can__mcan_8h.md#a2f4a7a67f69310b2470c2939cf7488d2)#define CAN\_MCAN\_CCCR\_DAR BIT(6)

[ 76](can__mcan_8h.md#a1057947a0482c69e67f32f79b0f0cf56)#define CAN\_MCAN\_CCCR\_MON BIT(5)

[ 77](can__mcan_8h.md#a39b308a89655c9a59050cffbd2ad3268)#define CAN\_MCAN\_CCCR\_CSR BIT(4)

[ 78](can__mcan_8h.md#a249d3b8483bb7869e2695ee56a8c40e9)#define CAN\_MCAN\_CCCR\_CSA BIT(3)

[ 79](can__mcan_8h.md#a40e186041bf0459f6d1fdf5736670e56)#define CAN\_MCAN\_CCCR\_ASM BIT(2)

[ 80](can__mcan_8h.md#ad36bcf2dfbe848fbcbd930055a442cca)#define CAN\_MCAN\_CCCR\_CCE BIT(1)

[ 81](can__mcan_8h.md#ab7fbe359b62fa11288390c0ed6b22d39)#define CAN\_MCAN\_CCCR\_INIT BIT(0)

82

83/\* Nominal Bit Timing & Prescaler register \*/

[ 84](can__mcan_8h.md#a308c60c14b65b3416d36a37e7b70a318)#define CAN\_MCAN\_NBTP 0x01C

[ 85](can__mcan_8h.md#abdd623bc3728e9e6c92d2b842c08d3e7)#define CAN\_MCAN\_NBTP\_NSJW GENMASK(31, 25)

[ 86](can__mcan_8h.md#a1285c541ff247a4bf26229e0b294af62)#define CAN\_MCAN\_NBTP\_NBRP GENMASK(24, 16)

[ 87](can__mcan_8h.md#a1c18b64cb2e4f22afbd16a61aeb31d42)#define CAN\_MCAN\_NBTP\_NTSEG1 GENMASK(15, 8)

[ 88](can__mcan_8h.md#a7c69e8e69f5b9bb61ad0342f8fde2d39)#define CAN\_MCAN\_NBTP\_NTSEG2 GENMASK(6, 0)

89

90/\* Timestamp Counter Configuration register \*/

[ 91](can__mcan_8h.md#a336430f9fd3a26e6c54deaf072bc1ad6)#define CAN\_MCAN\_TSCC 0x020

[ 92](can__mcan_8h.md#ad38c5e544217947bd4dd44ec53291e91)#define CAN\_MCAN\_TSCC\_TCP GENMASK(19, 16)

[ 93](can__mcan_8h.md#aefdf97284e7860342d550e0043c1b80c)#define CAN\_MCAN\_TSCC\_TSS GENMASK(1, 0)

94

95/\* Timestamp Counter Value register \*/

[ 96](can__mcan_8h.md#a8704135ca0f1a015b4f6527e6d9bafcd)#define CAN\_MCAN\_TSCV 0x024

[ 97](can__mcan_8h.md#a3ac6c1d5d964b1646d1a3e2a53d3206f)#define CAN\_MCAN\_TSCV\_TSC GENMASK(15, 0)

98

99/\* Timeout Counter Configuration register \*/

[ 100](can__mcan_8h.md#a8913873d251c86e2fee4842bb9c4951c)#define CAN\_MCAN\_TOCC 0x028

[ 101](can__mcan_8h.md#a4206bbc473216f1e68f7c6fb02cb27d3)#define CAN\_MCAN\_TOCC\_TOP GENMASK(31, 16)

[ 102](can__mcan_8h.md#a41d03bd4b12883207842512bde89f8e9)#define CAN\_MCAN\_TOCC\_TOS GENMASK(2, 1)

[ 103](can__mcan_8h.md#a63a2024085348c787e6dbc231aa47846)#define CAN\_MCAN\_TOCC\_ETOC BIT(1)

104

105/\* Timeout Counter Value register \*/

[ 106](can__mcan_8h.md#a2f4377ce56a8a38991fba9b2cc2d87c9)#define CAN\_MCAN\_TOCV 0x02C

[ 107](can__mcan_8h.md#aeb97ca070414b41a8de66bdf14f63d32)#define CAN\_MCAN\_TOCV\_TOC GENMASK(15, 0)

108

109/\* Error Counter register \*/

[ 110](can__mcan_8h.md#aee893904e384ad6b56311078d9546190)#define CAN\_MCAN\_ECR 0x040

[ 111](can__mcan_8h.md#a6df87229481d209acb54a719447dad47)#define CAN\_MCAN\_ECR\_CEL GENMASK(23, 16)

[ 112](can__mcan_8h.md#a0be04930627b22f80d548fd367cb847d)#define CAN\_MCAN\_ECR\_RP BIT(15)

[ 113](can__mcan_8h.md#ae0a477450ccd40c6a1de4c6bcd3a5997)#define CAN\_MCAN\_ECR\_REC GENMASK(14, 8)

[ 114](can__mcan_8h.md#afb635c07c2664e72c64ae614f2d60f94)#define CAN\_MCAN\_ECR\_TEC GENMASK(7, 0)

115

116/\* Protocol Status register \*/

[ 117](can__mcan_8h.md#a0e6bf5627ac886db479dd34693f8b7a6)#define CAN\_MCAN\_PSR 0x044

[ 118](can__mcan_8h.md#a2133840d3eab9f8a5a881e5c37c3fed2)#define CAN\_MCAN\_PSR\_TDCV GENMASK(22, 16)

[ 119](can__mcan_8h.md#a0769c5c4ee9f406eed816a1104793a0a)#define CAN\_MCAN\_PSR\_PXE BIT(14)

[ 120](can__mcan_8h.md#a1fb264bdd3e56b11224dc11e2703ac09)#define CAN\_MCAN\_PSR\_RFDF BIT(13)

[ 121](can__mcan_8h.md#ae6cc09fcf5145317c677294a6a8b888b)#define CAN\_MCAN\_PSR\_RBRS BIT(12)

[ 122](can__mcan_8h.md#acf2c2ff589d5e27335fa216a6df3abb6)#define CAN\_MCAN\_PSR\_RESI BIT(11)

[ 123](can__mcan_8h.md#a346aa3ec31690010401d1d120dda7e4e)#define CAN\_MCAN\_PSR\_DLEC GENMASK(10, 8)

[ 124](can__mcan_8h.md#a7b72bbe875c0b64e6c608ee2d0927658)#define CAN\_MCAN\_PSR\_BO BIT(7)

[ 125](can__mcan_8h.md#ac8bf022df308ce6bd8797c36d39e0d36)#define CAN\_MCAN\_PSR\_EW BIT(6)

[ 126](can__mcan_8h.md#a0cf95fc0ddc9b03b177730ae8f8a2128)#define CAN\_MCAN\_PSR\_EP BIT(5)

[ 127](can__mcan_8h.md#a6afc5e82af45896e01af32e2b2c69993)#define CAN\_MCAN\_PSR\_ACT GENMASK(4, 3)

[ 128](can__mcan_8h.md#ae49ca535c17a53562b7db3f897dc336a)#define CAN\_MCAN\_PSR\_LEC GENMASK(2, 0)

129

[ 130](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462)enum [can\_mcan\_psr\_lec](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462) {

[ 131](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462acab41a3d432b309d9b73a711d84b39e9) [CAN\_MCAN\_PSR\_LEC\_NO\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462acab41a3d432b309d9b73a711d84b39e9) = 0,

[ 132](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a0207d3347a4afc89d17fa6b954ae90d0) [CAN\_MCAN\_PSR\_LEC\_STUFF\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a0207d3347a4afc89d17fa6b954ae90d0) = 1,

[ 133](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462ac4bce840b2edcf97957d74e6debe9b03) [CAN\_MCAN\_PSR\_LEC\_FORM\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462ac4bce840b2edcf97957d74e6debe9b03) = 2,

[ 134](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a9e5414792478db5f57f1f270d0ceac13) [CAN\_MCAN\_PSR\_LEC\_ACK\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a9e5414792478db5f57f1f270d0ceac13) = 3,

[ 135](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a7de1a2f2ced1a52f01ee4d9f2b9b6b80) [CAN\_MCAN\_PSR\_LEC\_BIT1\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a7de1a2f2ced1a52f01ee4d9f2b9b6b80) = 4,

[ 136](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a4bca141d0a3056cbdfc379f49d60c651) [CAN\_MCAN\_PSR\_LEC\_BIT0\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a4bca141d0a3056cbdfc379f49d60c651) = 5,

[ 137](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a7a19af0809a0613a8becb016781b03dc) [CAN\_MCAN\_PSR\_LEC\_CRC\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a7a19af0809a0613a8becb016781b03dc) = 6,

[ 138](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a683c68657e49efd306f43be43bd3167e) [CAN\_MCAN\_PSR\_LEC\_NO\_CHANGE](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a683c68657e49efd306f43be43bd3167e) = 7

139};

140

141/\* Transmitter Delay Compensation register \*/

[ 142](can__mcan_8h.md#a52cea0ef00b1bf53a4f718104a3ad652)#define CAN\_MCAN\_TDCR 0x048

[ 143](can__mcan_8h.md#ab0a27684c90c1b5828206cd2f034802b)#define CAN\_MCAN\_TDCR\_TDCO GENMASK(14, 8)

[ 144](can__mcan_8h.md#ae2f0c4a34055d37e49710f594f1736cc)#define CAN\_MCAN\_TDCR\_TDCF GENMASK(6, 0)

145

146/\* Interrupt register \*/

[ 147](can__mcan_8h.md#acac62eeff461ebd9ac34b8d622dc8c6b)#define CAN\_MCAN\_IR 0x050

[ 148](can__mcan_8h.md#a732f9c3cb965a855c2e733bdadfcaa1e)#define CAN\_MCAN\_IR\_ARA BIT(29)

[ 149](can__mcan_8h.md#aa737557f70c4da0a7e5660208d6764df)#define CAN\_MCAN\_IR\_PED BIT(28)

[ 150](can__mcan_8h.md#a60f1b085bb9a26d5a211e56f86ac5e86)#define CAN\_MCAN\_IR\_PEA BIT(27)

[ 151](can__mcan_8h.md#a5adbd7ceb523237265ca3093bd921c20)#define CAN\_MCAN\_IR\_WDI BIT(26)

[ 152](can__mcan_8h.md#a62de51c28140a4e787363c2b579290f6)#define CAN\_MCAN\_IR\_BO BIT(25)

[ 153](can__mcan_8h.md#a5f8cf54fee2939bc2f31c9e414ba202e)#define CAN\_MCAN\_IR\_EW BIT(24)

[ 154](can__mcan_8h.md#ada6d4f670b522c7fd1036721ddc2931a)#define CAN\_MCAN\_IR\_EP BIT(23)

[ 155](can__mcan_8h.md#a4c88361aa6d63fee591a2010d882107e)#define CAN\_MCAN\_IR\_ELO BIT(22)

[ 156](can__mcan_8h.md#a20653377f1565e71de286858ca920d46)#define CAN\_MCAN\_IR\_BEU BIT(21)

[ 157](can__mcan_8h.md#a86431445f96ec66f93828d78ba1311d6)#define CAN\_MCAN\_IR\_BEC BIT(20)

[ 158](can__mcan_8h.md#ab82d152424a84de470bfe005b577368c)#define CAN\_MCAN\_IR\_DRX BIT(19)

[ 159](can__mcan_8h.md#ab5066977fa160d3ded392b054d858637)#define CAN\_MCAN\_IR\_TOO BIT(18)

[ 160](can__mcan_8h.md#a00b7078b20f2aa81356694b84a179446)#define CAN\_MCAN\_IR\_MRAF BIT(17)

[ 161](can__mcan_8h.md#a666e16b9ea27b83635067939aef62a31)#define CAN\_MCAN\_IR\_TSW BIT(16)

[ 162](can__mcan_8h.md#a090716d481b6e97d251aba9871ac0408)#define CAN\_MCAN\_IR\_TEFL BIT(15)

[ 163](can__mcan_8h.md#a59e276fb6412ba5447994615049cb8fd)#define CAN\_MCAN\_IR\_TEFF BIT(14)

[ 164](can__mcan_8h.md#a07fea07bd4ff7cfd4add4bedc0409e7a)#define CAN\_MCAN\_IR\_TEFW BIT(13)

[ 165](can__mcan_8h.md#a5f7fa6444d1afe343920fe4495f64da5)#define CAN\_MCAN\_IR\_TEFN BIT(12)

[ 166](can__mcan_8h.md#a481a7b485091a9b862ec48a75315e12c)#define CAN\_MCAN\_IR\_TFE BIT(11)

[ 167](can__mcan_8h.md#ace4b4fbac614a38e70248aba6df71068)#define CAN\_MCAN\_IR\_TCF BIT(10)

[ 168](can__mcan_8h.md#a880558d5672ef8d27bf232eeb739c3e0)#define CAN\_MCAN\_IR\_TC BIT(9)

[ 169](can__mcan_8h.md#aee45488e19c8bbf86ffed780cc3565c3)#define CAN\_MCAN\_IR\_HPM BIT(8)

[ 170](can__mcan_8h.md#ac37b42f53820384cc426b8b078572a35)#define CAN\_MCAN\_IR\_RF1L BIT(7)

[ 171](can__mcan_8h.md#a10193930b296827f124dc98e49c7db2a)#define CAN\_MCAN\_IR\_RF1F BIT(6)

[ 172](can__mcan_8h.md#a9bd64356ca32fef96e6680966e3d77b4)#define CAN\_MCAN\_IR\_RF1W BIT(5)

[ 173](can__mcan_8h.md#abed65c016f9adf3794a3fd0474fa84e3)#define CAN\_MCAN\_IR\_RF1N BIT(4)

[ 174](can__mcan_8h.md#a530db7342edd5f2f3254ce17745dcb88)#define CAN\_MCAN\_IR\_RF0L BIT(3)

[ 175](can__mcan_8h.md#a15214770d66f4bf0df92ed9457f5954f)#define CAN\_MCAN\_IR\_RF0F BIT(2)

[ 176](can__mcan_8h.md#ab737ca9c1a8a152f58dd9d1d2a02790e)#define CAN\_MCAN\_IR\_RF0W BIT(1)

[ 177](can__mcan_8h.md#aef7cfda9d78ed8294e744c3c024e7ce9)#define CAN\_MCAN\_IR\_RF0N BIT(0)

178

179/\* Interrupt Enable register \*/

[ 180](can__mcan_8h.md#a5efcfd38d911a09ba1a0e8546127d73e)#define CAN\_MCAN\_IE 0x054

[ 181](can__mcan_8h.md#a87e7dc8db720db25d80a9464ae0a9a0f)#define CAN\_MCAN\_IE\_ARAE BIT(29)

[ 182](can__mcan_8h.md#a5894eb34123a83e13763525c7725cacb)#define CAN\_MCAN\_IE\_PEDE BIT(28)

[ 183](can__mcan_8h.md#aec30af8e9ea090c3d896c8d815f5fb18)#define CAN\_MCAN\_IE\_PEAE BIT(27)

[ 184](can__mcan_8h.md#a80f67433f566f71224184fd6f4047096)#define CAN\_MCAN\_IE\_WDIE BIT(26)

[ 185](can__mcan_8h.md#a7adbce95af6bb9efbf20188ebf6584f7)#define CAN\_MCAN\_IE\_BOE BIT(25)

[ 186](can__mcan_8h.md#a5727d4efbe75dbbb022b3df9f64134ae)#define CAN\_MCAN\_IE\_EWE BIT(24)

[ 187](can__mcan_8h.md#aaf858f5603f46e886d2a255d027e2057)#define CAN\_MCAN\_IE\_EPE BIT(23)

[ 188](can__mcan_8h.md#aeb78e4ebe0c9522accc5836d2a9f33d1)#define CAN\_MCAN\_IE\_ELOE BIT(22)

[ 189](can__mcan_8h.md#a7748c310633b29084ff3673aff28e749)#define CAN\_MCAN\_IE\_BEUE BIT(21)

[ 190](can__mcan_8h.md#a8e2fc398be6df304991143af43ae4ed3)#define CAN\_MCAN\_IE\_BECE BIT(20)

[ 191](can__mcan_8h.md#a14f6823f3ee219eafc5370f6bd9cc839)#define CAN\_MCAN\_IE\_DRXE BIT(19)

[ 192](can__mcan_8h.md#adffa68a3e8e9186595f139e5b8f78025)#define CAN\_MCAN\_IE\_TOOE BIT(18)

[ 193](can__mcan_8h.md#a8570c8e17b23bd00f3d3e671ecdc0301)#define CAN\_MCAN\_IE\_MRAFE BIT(17)

[ 194](can__mcan_8h.md#a5d66c2cef0008cdb2b7faae4f838fde1)#define CAN\_MCAN\_IE\_TSWE BIT(16)

[ 195](can__mcan_8h.md#a2ebfaf6bf1f175917a20fd47b2d241f0)#define CAN\_MCAN\_IE\_TEFLE BIT(15)

[ 196](can__mcan_8h.md#a61e51933d46002e468e3965fdd3100ce)#define CAN\_MCAN\_IE\_TEFFE BIT(14)

[ 197](can__mcan_8h.md#aa983e0f26d5454b297866a5778c09915)#define CAN\_MCAN\_IE\_TEFWE BIT(13)

[ 198](can__mcan_8h.md#a5cca5bd86ccf8433b693daf805f150de)#define CAN\_MCAN\_IE\_TEFNE BIT(12)

[ 199](can__mcan_8h.md#a5fd83f7f8b769c493b2b99fae7cf3bcf)#define CAN\_MCAN\_IE\_TFEE BIT(11)

[ 200](can__mcan_8h.md#a3f1f30cfdbffdc698d7c6ad94d8617db)#define CAN\_MCAN\_IE\_TCFE BIT(10)

[ 201](can__mcan_8h.md#a7545997948206ff883a9f2cd9c327f35)#define CAN\_MCAN\_IE\_TCE BIT(9)

[ 202](can__mcan_8h.md#a626e0d5094618d3d45a3d614598c426a)#define CAN\_MCAN\_IE\_HPME BIT(8)

[ 203](can__mcan_8h.md#a7c535f93189d8d5f41320e6fa364a005)#define CAN\_MCAN\_IE\_RF1LE BIT(7)

[ 204](can__mcan_8h.md#a10bba01222375ae38f049ee8abc50973)#define CAN\_MCAN\_IE\_RF1FE BIT(6)

[ 205](can__mcan_8h.md#af399bd4422077374595d152dee4e7860)#define CAN\_MCAN\_IE\_RF1WE BIT(5)

[ 206](can__mcan_8h.md#a39f3b5000f6290513d723b3bf8869aba)#define CAN\_MCAN\_IE\_RF1NE BIT(4)

[ 207](can__mcan_8h.md#a72eb6ded2dcd94d3785887fef5f231a1)#define CAN\_MCAN\_IE\_RF0LE BIT(3)

[ 208](can__mcan_8h.md#a42b4e6e1a7138f356bdb2c5ed87eea95)#define CAN\_MCAN\_IE\_RF0FE BIT(2)

[ 209](can__mcan_8h.md#a85118c1d03eadd4a6a76cf935fbe17bc)#define CAN\_MCAN\_IE\_RF0WE BIT(1)

[ 210](can__mcan_8h.md#af31e0711f5628614ce69969c14c78fb8)#define CAN\_MCAN\_IE\_RF0NE BIT(0)

211

212/\* Interrupt Line Select register \*/

[ 213](can__mcan_8h.md#a6d2a927e67ecb7c01749d6a0fbc25363)#define CAN\_MCAN\_ILS 0x058

[ 214](can__mcan_8h.md#ac06e1958c3690032639849b9b291ca7f)#define CAN\_MCAN\_ILS\_ARAL BIT(29)

[ 215](can__mcan_8h.md#a1863554a941902bd0a585916b3016ec9)#define CAN\_MCAN\_ILS\_PEDL BIT(28)

[ 216](can__mcan_8h.md#a78ce183fb2e265f8b850c52b2e0b9b83)#define CAN\_MCAN\_ILS\_PEAL BIT(27)

[ 217](can__mcan_8h.md#a28b9d67835f409299a7dbfddce41674e)#define CAN\_MCAN\_ILS\_WDIL BIT(26)

[ 218](can__mcan_8h.md#a4be2c784e04021c28fb0bda474af2008)#define CAN\_MCAN\_ILS\_BOL BIT(25)

[ 219](can__mcan_8h.md#ac250560aafee73e83b7cc4db7333f037)#define CAN\_MCAN\_ILS\_EWL BIT(24)

[ 220](can__mcan_8h.md#a49654d0bbf4af7dabf2bf89805177fb9)#define CAN\_MCAN\_ILS\_EPL BIT(23)

[ 221](can__mcan_8h.md#a24400f4c04a26a183853dcd8c6401849)#define CAN\_MCAN\_ILS\_ELOL BIT(22)

[ 222](can__mcan_8h.md#a4992a22be098fa66ae40119f88ae9c42)#define CAN\_MCAN\_ILS\_BEUL BIT(21)

[ 223](can__mcan_8h.md#adb5a621d293f0bde671a9246f67af57d)#define CAN\_MCAN\_ILS\_BECL BIT(20)

[ 224](can__mcan_8h.md#a414c9f4b86e1f851b9f12356bc440236)#define CAN\_MCAN\_ILS\_DRXL BIT(19)

[ 225](can__mcan_8h.md#a3b37679278affda2b8b17a975c97a1cf)#define CAN\_MCAN\_ILS\_TOOL BIT(18)

[ 226](can__mcan_8h.md#a6a139692dcf97de3500d4692119610e3)#define CAN\_MCAN\_ILS\_MRAFL BIT(17)

[ 227](can__mcan_8h.md#af1815cb8b62a185a739e23d4bbcedbc0)#define CAN\_MCAN\_ILS\_TSWL BIT(16)

[ 228](can__mcan_8h.md#abbe6c6994e95786e081b110c6fec56b3)#define CAN\_MCAN\_ILS\_TEFLL BIT(15)

[ 229](can__mcan_8h.md#a0c60df858386dbde519d03f448282177)#define CAN\_MCAN\_ILS\_TEFFL BIT(14)

[ 230](can__mcan_8h.md#aa3418486b5bdee960076c03c6310b47d)#define CAN\_MCAN\_ILS\_TEFWL BIT(13)

[ 231](can__mcan_8h.md#af42996807b1747d5f08540b18c3fdf5a)#define CAN\_MCAN\_ILS\_TEFNL BIT(12)

[ 232](can__mcan_8h.md#a287b7fec7f9917f18011994dc3329f5f)#define CAN\_MCAN\_ILS\_TFEL BIT(11)

[ 233](can__mcan_8h.md#abfaf532cc23ba6f63149bc97dc3c855e)#define CAN\_MCAN\_ILS\_TCFL BIT(10)

[ 234](can__mcan_8h.md#ab294335aa5dff81c72d89f4e6c2f506a)#define CAN\_MCAN\_ILS\_TCL BIT(9)

[ 235](can__mcan_8h.md#a7922ad47535e02146816b07e0ee7c499)#define CAN\_MCAN\_ILS\_HPML BIT(8)

[ 236](can__mcan_8h.md#ad1868981fcc7e414c75e005e93859343)#define CAN\_MCAN\_ILS\_RF1LL BIT(7)

[ 237](can__mcan_8h.md#a0695d2cfd07a5717fb2e307b047567fe)#define CAN\_MCAN\_ILS\_RF1FL BIT(6)

[ 238](can__mcan_8h.md#ac70c241178121176bebdb4c13ec29c65)#define CAN\_MCAN\_ILS\_RF1WL BIT(5)

[ 239](can__mcan_8h.md#a182bc538b568b402370e02a969dd5bd9)#define CAN\_MCAN\_ILS\_RF1NL BIT(4)

[ 240](can__mcan_8h.md#ac7304d316f701ad6a0f66ca62cbbcf00)#define CAN\_MCAN\_ILS\_RF0LL BIT(3)

[ 241](can__mcan_8h.md#a061b5b7c74b8a0afc0a78f01b1374e28)#define CAN\_MCAN\_ILS\_RF0FL BIT(2)

[ 242](can__mcan_8h.md#a389d1fe76759d470fb8af80698b4708f)#define CAN\_MCAN\_ILS\_RF0WL BIT(1)

[ 243](can__mcan_8h.md#ad40a58d2e4240ce58f4da55ebf0756e5)#define CAN\_MCAN\_ILS\_RF0NL BIT(0)

244

245/\* Interrupt Line Enable register \*/

[ 246](can__mcan_8h.md#a32e14f45e1c85a73e816a7a78477b703)#define CAN\_MCAN\_ILE 0x05C

[ 247](can__mcan_8h.md#a9022d6b85f32310f57a8a711409b4beb)#define CAN\_MCAN\_ILE\_EINT1 BIT(1)

[ 248](can__mcan_8h.md#a10be46e7dbc334e014d3a5126d2d8832)#define CAN\_MCAN\_ILE\_EINT0 BIT(0)

249

250/\* Global filter configuration register \*/

[ 251](can__mcan_8h.md#acedea2dc6c2eaa750196ea330028137d)#define CAN\_MCAN\_GFC 0x080

[ 252](can__mcan_8h.md#ad8f1ee3bcf1ce148ecc604177777fe36)#define CAN\_MCAN\_GFC\_ANFS GENMASK(5, 4)

[ 253](can__mcan_8h.md#a1ecb99bb847bb0305ca2720c18f77ae1)#define CAN\_MCAN\_GFC\_ANFE GENMASK(3, 2)

[ 254](can__mcan_8h.md#a719015ab076274c8f71a574975a6a1c9)#define CAN\_MCAN\_GFC\_RRFS BIT(1)

[ 255](can__mcan_8h.md#af72ebd1644ee7651b6755dbc2d999da1)#define CAN\_MCAN\_GFC\_RRFE BIT(0)

256

257/\* Standard ID Filter Configuration register \*/

[ 258](can__mcan_8h.md#a27a0bbdaa9b9bfba7227dbe1350f2c74)#define CAN\_MCAN\_SIDFC 0x084

[ 259](can__mcan_8h.md#a906b8e66d3294d68ebdff6a7c5283526)#define CAN\_MCAN\_SIDFC\_LSS GENMASK(23, 16)

[ 260](can__mcan_8h.md#ac73011c520eea37b4ca36da8259b3f77)#define CAN\_MCAN\_SIDFC\_FLSSA GENMASK(15, 2)

261

262/\* Extended ID Filter Configuration register \*/

[ 263](can__mcan_8h.md#abc56cb7ea0b29dd3c813494cad7ba81c)#define CAN\_MCAN\_XIDFC 0x088

[ 264](can__mcan_8h.md#adc32a4719774acdac26727fc7910698a)#define CAN\_MCAN\_XIDFC\_LSS GENMASK(22, 16)

[ 265](can__mcan_8h.md#a43ad251923878baed62ab97ed44b0dc9)#define CAN\_MCAN\_XIDFC\_FLESA GENMASK(15, 2)

266

267/\* Extended ID AND Mask register \*/

[ 268](can__mcan_8h.md#a9c64c5bcc80f2bdaad64de5c370826db)#define CAN\_MCAN\_XIDAM 0x090

[ 269](can__mcan_8h.md#afd1f6383e81e4dfbc1a156bf5a3092bb)#define CAN\_MCAN\_XIDAM\_EIDM GENMASK(28, 0)

270

271/\* High Priority Message Status register \*/

[ 272](can__mcan_8h.md#a13f990a79472988c3b9b8f9b17795b93)#define CAN\_MCAN\_HPMS 0x094

[ 273](can__mcan_8h.md#a016ae0f271581c7f77fb3eede5866ab7)#define CAN\_MCAN\_HPMS\_FLST BIT(15)

[ 274](can__mcan_8h.md#a15a0a60646ea281d06aeebf4f94655c5)#define CAN\_MCAN\_HPMS\_FIDX GENMASK(14, 8)

[ 275](can__mcan_8h.md#a8d47e3cb602ffd092e7da40d2268bc87)#define CAN\_MCAN\_HPMS\_MSI GENMASK(7, 6)

[ 276](can__mcan_8h.md#a870c4e0a0829eb9ce24fb14c62383e44)#define CAN\_MCAN\_HPMS\_BIDX GENMASK(5, 0)

277

278/\* New Data 1 register \*/

[ 279](can__mcan_8h.md#a38c5b3177e25905cc78f7dbcee956f77)#define CAN\_MCAN\_NDAT1 0x098

[ 280](can__mcan_8h.md#ac533f25e977b0eeb37cb5e047a7dd7f6)#define CAN\_MCAN\_NDAT1\_ND GENMASK(31, 0)

281

282/\* New Data 2 register \*/

[ 283](can__mcan_8h.md#afce0263a9bbe5901e3d5e0020282efda)#define CAN\_MCAN\_NDAT2 0x09C

[ 284](can__mcan_8h.md#ac443c986084e5bc0b618049f20193715)#define CAN\_MCAN\_NDAT2\_ND GENMASK(31, 0)

285

286/\* Rx FIFO 0 Configuration register \*/

[ 287](can__mcan_8h.md#acafb4bdf5f41886fe05ab96ce9d3e40f)#define CAN\_MCAN\_RXF0C 0x0A0

[ 288](can__mcan_8h.md#aa60d7075af7dc69fe61f7c9ed26b4db8)#define CAN\_MCAN\_RXF0C\_F0OM BIT(31)

[ 289](can__mcan_8h.md#a407c6bb15b8f0c296004c5f2dffd1255)#define CAN\_MCAN\_RXF0C\_F0WM GENMASK(30, 24)

[ 290](can__mcan_8h.md#a36b805fdfa202f8ea7fc885a75f889a3)#define CAN\_MCAN\_RXF0C\_F0S GENMASK(22, 16)

[ 291](can__mcan_8h.md#a2be907b2a04b58df30f5a4e4d2c0cbc0)#define CAN\_MCAN\_RXF0C\_F0SA GENMASK(15, 2)

292

293/\* Rx FIFO 0 Status register \*/

[ 294](can__mcan_8h.md#a8af4d58a4ae713351c0c944bb4468359)#define CAN\_MCAN\_RXF0S 0x0A4

[ 295](can__mcan_8h.md#a2841566e304c9d151763000dbb5b2792)#define CAN\_MCAN\_RXF0S\_RF0L BIT(25)

[ 296](can__mcan_8h.md#aa8649180143ff827bc49a7789682b377)#define CAN\_MCAN\_RXF0S\_F0F BIT(24)

[ 297](can__mcan_8h.md#ae3b41edffd1a7a8e8ddf96b450aac3ec)#define CAN\_MCAN\_RXF0S\_F0PI GENMASK(21, 16)

[ 298](can__mcan_8h.md#acec1a9ead6d7e01e1178ea56a0d66b2e)#define CAN\_MCAN\_RXF0S\_F0GI GENMASK(13, 8)

[ 299](can__mcan_8h.md#ae8ab0a46f01834f07076750e909f099b)#define CAN\_MCAN\_RXF0S\_F0FL GENMASK(6, 0)

300

301/\* Rx FIFO 0 Acknowledge register \*/

[ 302](can__mcan_8h.md#addda3c98094c821fe63bf24782d140d1)#define CAN\_MCAN\_RXF0A 0x0A8

[ 303](can__mcan_8h.md#ab806cb88a0961da39319c8db90a0bfb6)#define CAN\_MCAN\_RXF0A\_F0AI GENMASK(5, 0)

304

305/\* Rx Buffer Configuration register \*/

[ 306](can__mcan_8h.md#a9cb2ddc82fcfb102484577307c88481b)#define CAN\_MCAN\_RXBC 0x0AC

[ 307](can__mcan_8h.md#ad7bf916dc45e84b85f6c895fefdb9e99)#define CAN\_MCAN\_RXBC\_RBSA GENMASK(15, 2)

308

309/\* Rx FIFO 1 Configuration register \*/

[ 310](can__mcan_8h.md#a4b0612f2b06cf3af04fe969d97106cb5)#define CAN\_MCAN\_RXF1C 0x0B0

[ 311](can__mcan_8h.md#a3f39ada97a9ebd6dcfe4d5bb9adfadee)#define CAN\_MCAN\_RXF1C\_F1OM BIT(31)

[ 312](can__mcan_8h.md#a65cd1948f37dbc67fa85dde655a997b3)#define CAN\_MCAN\_RXF1C\_F1WM GENMASK(30, 24)

[ 313](can__mcan_8h.md#a9f4dc18657f25ebd2463bf55af719f04)#define CAN\_MCAN\_RXF1C\_F1S GENMASK(22, 16)

[ 314](can__mcan_8h.md#a23131c2ea676b9a913be4fce2ca8cf9e)#define CAN\_MCAN\_RXF1C\_F1SA GENMASK(15, 2)

315

316/\* Rx FIFO 1 Status register \*/

[ 317](can__mcan_8h.md#a63a683d44b63affa919963adf94f755c)#define CAN\_MCAN\_RXF1S 0x0B4

[ 318](can__mcan_8h.md#a5f55e6eeff595af1f6f1eaeedfb9b62d)#define CAN\_MCAN\_RXF1S\_RF1L BIT(25)

[ 319](can__mcan_8h.md#a407843916f140d8bbd2546eb1f1955e6)#define CAN\_MCAN\_RXF1S\_F1F BIT(24)

[ 320](can__mcan_8h.md#a8bf02cc958131a3a25218058159bb2bf)#define CAN\_MCAN\_RXF1S\_F1PI GENMASK(21, 16)

[ 321](can__mcan_8h.md#aaed234ff229b28f3f0926468d9fd32af)#define CAN\_MCAN\_RXF1S\_F1GI GENMASK(13, 8)

[ 322](can__mcan_8h.md#aaf8df87b128358e2b211c6000b389d64)#define CAN\_MCAN\_RXF1S\_F1FL GENMASK(6, 0)

323

324/\* Rx FIFO 1 Acknowledge register \*/

[ 325](can__mcan_8h.md#af3101a1d476ed8304885c33367e19d0f)#define CAN\_MCAN\_RXF1A 0x0B8

[ 326](can__mcan_8h.md#a190b1df18ce88e67dd24145d6bb4d899)#define CAN\_MCAN\_RXF1A\_F1AI GENMASK(5, 0)

327

328/\* Rx Buffer/FIFO Element Size Configuration register \*/

[ 329](can__mcan_8h.md#a83c90feeec80071bc35b3dcce8f6be99)#define CAN\_MCAN\_RXESC 0x0BC

[ 330](can__mcan_8h.md#aff5420d9503e9ec130ad37a40021f738)#define CAN\_MCAN\_RXESC\_RBDS GENMASK(10, 8)

[ 331](can__mcan_8h.md#ad8600748ee89bec9c7efe76e4a743ed7)#define CAN\_MCAN\_RXESC\_F1DS GENMASK(6, 4)

[ 332](can__mcan_8h.md#a5e45adc0b6acba20391c6f5adc6c5ec3)#define CAN\_MCAN\_RXESC\_F0DS GENMASK(2, 0)

333

334/\* Tx Buffer Configuration register \*/

[ 335](can__mcan_8h.md#aabbf65d56f0aacdd26b22eb80b34721e)#define CAN\_MCAN\_TXBC 0x0C0

[ 336](can__mcan_8h.md#a4ff2da25354a95ae078951a3b8f0b1f0)#define CAN\_MCAN\_TXBC\_TFQM BIT(30)

[ 337](can__mcan_8h.md#a25144c814fa7ed19bd6c391cbb2244e6)#define CAN\_MCAN\_TXBC\_TFQS GENMASK(29, 24)

[ 338](can__mcan_8h.md#afe25b1f33b0a877b8e46d35a26b5db8e)#define CAN\_MCAN\_TXBC\_NDTB GENMASK(21, 16)

[ 339](can__mcan_8h.md#a54aa984e023137eb87aa8b00f59ea02c)#define CAN\_MCAN\_TXBC\_TBSA GENMASK(15, 2)

340

341/\* Tx FIFO/Queue Status register \*/

[ 342](can__mcan_8h.md#abdd2a49df8465eb55633f8707a46187e)#define CAN\_MCAN\_TXFQS 0x0C4

[ 343](can__mcan_8h.md#a37ef0318a42bba8b5fce6d9d9ca094df)#define CAN\_MCAN\_TXFQS\_TFQF BIT(21)

[ 344](can__mcan_8h.md#ae479a0770d5629198d3104a9729a777f)#define CAN\_MCAN\_TXFQS\_TFQPI GENMASK(20, 16)

[ 345](can__mcan_8h.md#aac92788e1f00b7af37d15cad4a660cfe)#define CAN\_MCAN\_TXFQS\_TFGI GENMASK(12, 8)

[ 346](can__mcan_8h.md#a47bcf7d8796c4b4442afc1e194dcf657)#define CAN\_MCAN\_TXFQS\_TFFL GENMASK(5, 0)

347

348/\* Tx Buffer Element Size Configuration register \*/

[ 349](can__mcan_8h.md#a4a862608de38135c9febbb6d75b153ef)#define CAN\_MCAN\_TXESC 0x0C8

[ 350](can__mcan_8h.md#ad20ed0d0615c7f4804cbb9324499f84d)#define CAN\_MCAN\_TXESC\_TBDS GENMASK(2, 0)

351

352/\* Tx Buffer Request Pending register \*/

[ 353](can__mcan_8h.md#a3c8dcbcf3921d5e51306cb8e5feb2cd1)#define CAN\_MCAN\_TXBRP 0x0CC

[ 354](can__mcan_8h.md#a8e4d1e69b827265adb8aff580ca01cde)#define CAN\_MCAN\_TXBRP\_TRP GENMASK(31, 0)

355

356/\* Tx Buffer Add Request register \*/

[ 357](can__mcan_8h.md#a547995f6d877963184992a5cc09fdcf3)#define CAN\_MCAN\_TXBAR 0x0D0

[ 358](can__mcan_8h.md#ae92b22867500ceb14a6e2035cbf6c8b1)#define CAN\_MCAN\_TXBAR\_AR GENMASK(31, 0)

359

360/\* Tx Buffer Cancellation Request register \*/

[ 361](can__mcan_8h.md#ad0f3bb0f2d096cff8e1e2ac4416c44e0)#define CAN\_MCAN\_TXBCR 0x0D4

[ 362](can__mcan_8h.md#a023ae0f402eb013e68d35a1e367ff710)#define CAN\_MCAN\_TXBCR\_CR GENMASK(31, 0)

363

364/\* Tx Buffer Transmission Occurred register \*/

[ 365](can__mcan_8h.md#ab8050da5ff162f638b7920cc80115a8a)#define CAN\_MCAN\_TXBTO 0x0D8

[ 366](can__mcan_8h.md#adf91c2d98d25bf2f2901e215a8715b9b)#define CAN\_MCAN\_TXBTO\_TO GENMASK(31, 0)

367

368/\* Tx Buffer Cancellation Finished register \*/

[ 369](can__mcan_8h.md#a6d671b8127c66b7e8a7e019b68201afd)#define CAN\_MCAN\_TXBCF 0x0DC

[ 370](can__mcan_8h.md#a027220d5bfd988da4716e5e89d9e7f9d)#define CAN\_MCAN\_TXBCF\_CF GENMASK(31, 0)

371

372/\* Tx Buffer Transmission Interrupt Enable register \*/

[ 373](can__mcan_8h.md#a8a4753541d28a7ff92d8b7ba844fa943)#define CAN\_MCAN\_TXBTIE 0x0E0

[ 374](can__mcan_8h.md#a7f99c9c844897923c02a1356af052ddf)#define CAN\_MCAN\_TXBTIE\_TIE GENMASK(31, 0)

375

376/\* Tx Buffer Cancellation Finished Interrupt Enable register \*/

[ 377](can__mcan_8h.md#aafe9d81dfa50841d20a1a6719b544017)#define CAN\_MCAN\_TXBCIE 0x0E4

[ 378](can__mcan_8h.md#a1b0214f3f897c6852e4fdbff3f8f21a2)#define CAN\_MCAN\_TXBCIE\_CFIE GENMASK(31, 0)

379

380/\* Tx Event FIFO Configuration register \*/

[ 381](can__mcan_8h.md#a68ea1bab6b687ad406f416c73441ff9c)#define CAN\_MCAN\_TXEFC 0x0F0

[ 382](can__mcan_8h.md#a7551e23d8ba589be55831268b69ce099)#define CAN\_MCAN\_TXEFC\_EFWM GENMASK(29, 24)

[ 383](can__mcan_8h.md#af2ade33b56998a19aeda8cb0f868324c)#define CAN\_MCAN\_TXEFC\_EFS GENMASK(21, 16)

[ 384](can__mcan_8h.md#a162a0b6fd08c65359afa9dc59fba9ed3)#define CAN\_MCAN\_TXEFC\_EFSA GENMASK(15, 2)

385

386/\* Tx Event FIFO Status register \*/

[ 387](can__mcan_8h.md#a48888433839c16389c97ab6a359667d1)#define CAN\_MCAN\_TXEFS 0x0F4

[ 388](can__mcan_8h.md#a6f4fdc1835216b1408796b9f541054b8)#define CAN\_MCAN\_TXEFS\_TEFL BIT(25)

[ 389](can__mcan_8h.md#ae430823894219a2e271310be16e484f4)#define CAN\_MCAN\_TXEFS\_EFF BIT(24)

[ 390](can__mcan_8h.md#a64ccc68de69d3d46367e05e46934225e)#define CAN\_MCAN\_TXEFS\_EFPI GENMASK(20, 16)

[ 391](can__mcan_8h.md#af69a4882448bb8cab8bee6c20f145e18)#define CAN\_MCAN\_TXEFS\_EFGI GENMASK(12, 8)

[ 392](can__mcan_8h.md#a94994438584cfdfa0a9c7bc91227ee7e)#define CAN\_MCAN\_TXEFS\_EFFL GENMASK(5, 0)

393

394/\* Tx Event FIFO Acknowledge register \*/

[ 395](can__mcan_8h.md#a3a0b6530cbff5e1661c6ad208cedff08)#define CAN\_MCAN\_TXEFA 0x0F8

[ 396](can__mcan_8h.md#a78b3604320fdc00e0fe734516f5e1db9)#define CAN\_MCAN\_TXEFA\_EFAI GENMASK(4, 0)

397

[ 407](can__mcan_8h.md#a1b2e247424c436244e795ef253840d58)#define CAN\_MCAN\_MRAM\_CFG\_OFFSET 0

[ 409](can__mcan_8h.md#a651e96118352208ff4a5b041f051d10f)#define CAN\_MCAN\_MRAM\_CFG\_STD\_FILTER 1

[ 411](can__mcan_8h.md#a9a43d8d379fee72d0c46841538b22e91)#define CAN\_MCAN\_MRAM\_CFG\_EXT\_FILTER 2

[ 413](can__mcan_8h.md#aacc3d7a9ace66c6322a07186a72324ef)#define CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO0 3

[ 415](can__mcan_8h.md#a6bdc1012af79c50869279a7caac4ff31)#define CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO1 4

[ 417](can__mcan_8h.md#aa1c3bbb17546a5c8daaf5c80e028e1bf)#define CAN\_MCAN\_MRAM\_CFG\_RX\_BUFFER 5

[ 419](can__mcan_8h.md#a35fbb5986ca2268dd650b00970da363d)#define CAN\_MCAN\_MRAM\_CFG\_TX\_EVENT\_FIFO 6

[ 421](can__mcan_8h.md#ab18faf8f17480060d0102bb9370378c1)#define CAN\_MCAN\_MRAM\_CFG\_TX\_BUFFER 7

[ 423](can__mcan_8h.md#abb4087b9c7ac31e8a1cb7003945dad97)#define CAN\_MCAN\_MRAM\_CFG\_NUM\_CELLS 8

424

426

[ 433](can__mcan_8h.md#a06194f088174c2634bd318aaaddca988)#define CAN\_MCAN\_DT\_MRAM\_OFFSET(node\_id) \

434 DT\_PROP\_BY\_IDX(node\_id, bosch\_mram\_cfg, CAN\_MCAN\_MRAM\_CFG\_OFFSET)

435

[ 442](can__mcan_8h.md#a87442fd647be89575fbd0e3a6a4f2540)#define CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(node\_id) \

443 DT\_PROP\_BY\_IDX(node\_id, bosch\_mram\_cfg, CAN\_MCAN\_MRAM\_CFG\_STD\_FILTER)

444

[ 451](can__mcan_8h.md#a8c5ca10a9d376f42cecdb4fcaa1c2f86)#define CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(node\_id) \

452 DT\_PROP\_BY\_IDX(node\_id, bosch\_mram\_cfg, CAN\_MCAN\_MRAM\_CFG\_EXT\_FILTER)

453

[ 460](can__mcan_8h.md#a5b814febb2893a33617455a070f1814f)#define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(node\_id) \

461 DT\_PROP\_BY\_IDX(node\_id, bosch\_mram\_cfg, CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO0)

462

[ 469](can__mcan_8h.md#a71941bfd0f048401fd1208d556260f32)#define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(node\_id) \

470 DT\_PROP\_BY\_IDX(node\_id, bosch\_mram\_cfg, CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO1)

471

[ 478](can__mcan_8h.md#ad2371b27de938b29f42d2991a3f1009f)#define CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(node\_id) \

479 DT\_PROP\_BY\_IDX(node\_id, bosch\_mram\_cfg, CAN\_MCAN\_MRAM\_CFG\_RX\_BUFFER)

480

[ 487](can__mcan_8h.md#abbdb679ab26eb135d43dcc2394bded71)#define CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(node\_id) \

488 DT\_PROP\_BY\_IDX(node\_id, bosch\_mram\_cfg, CAN\_MCAN\_MRAM\_CFG\_TX\_EVENT\_FIFO)

489

[ 496](can__mcan_8h.md#a7d725b5c696acbc394547800a5e729ae)#define CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(node\_id) \

497 DT\_PROP\_BY\_IDX(node\_id, bosch\_mram\_cfg, CAN\_MCAN\_MRAM\_CFG\_TX\_BUFFER)

498

[ 505](can__mcan_8h.md#a4c6c3b23eed2ae336882cbfbb69d8578)#define CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET(node\_id) (0U)

506

[ 513](can__mcan_8h.md#a71687f621eae0d9f930ede70cb99cff7)#define CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET(node\_id) \

514 (CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET(node\_id) + \

515 CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(node\_id) \* sizeof(struct can\_mcan\_std\_filter))

516

[ 523](can__mcan_8h.md#a79b1f334979e5d7f180b6f37fbcb772f)#define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET(node\_id) \

524 (CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET(node\_id) + \

525 CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(node\_id) \* sizeof(struct can\_mcan\_ext\_filter))

526

[ 533](can__mcan_8h.md#aa4c0f6e4696d3c82344bd099eb0dcd13)#define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET(node\_id) \

534 (CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET(node\_id) + \

535 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(node\_id) \* sizeof(struct can\_mcan\_rx\_fifo))

536

[ 543](can__mcan_8h.md#aa0d25966039a769edd9b8b4f31af2c9f)#define CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET(node\_id) \

544 (CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET(node\_id) + \

545 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(node\_id) \* sizeof(struct can\_mcan\_rx\_fifo))

546

[ 553](can__mcan_8h.md#a16ce04fda8d800582ccc1b6979d34ac4)#define CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(node\_id) \

554 (CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET(node\_id) + \

555 CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(node\_id) \* sizeof(struct can\_mcan\_rx\_fifo))

556

[ 563](can__mcan_8h.md#a1f3384686c23982de8acef2182597e69)#define CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET(node\_id) \

564 (CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(node\_id) + \

565 CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(node\_id) \* sizeof(struct can\_mcan\_tx\_event\_fifo))

566

[ 579](can__mcan_8h.md#aaed34aa27da9ac0948d8b6ab798c7170)#define CAN\_MCAN\_DT\_MCAN\_ADDR(node\_id) \

580 COND\_CODE\_1(DT\_NUM\_REGS(node\_id), ((mm\_reg\_t)DT\_REG\_ADDR(node\_id)), \

581 ((mm\_reg\_t)DT\_REG\_ADDR\_BY\_NAME(node\_id, m\_can)))

582

[ 592](can__mcan_8h.md#ad7d854278909e12accdef06f2dc7a490)#define CAN\_MCAN\_DT\_MRBA(node\_id) \

593 (mem\_addr\_t)DT\_REG\_ADDR\_BY\_NAME(node\_id, message\_ram)

594

[ 604](can__mcan_8h.md#acecc9210d2504ba1dda108a79a2afb78)#define CAN\_MCAN\_DT\_MRAM\_ADDR(node\_id) \

605 (mem\_addr\_t)(CAN\_MCAN\_DT\_MRBA(node\_id) + CAN\_MCAN\_DT\_MRAM\_OFFSET(node\_id))

606

[ 617](can__mcan_8h.md#a94743f60c64c64a1e2bfd78fcc864cf1)#define CAN\_MCAN\_DT\_MRAM\_SIZE(node\_id) \

618 (mem\_addr\_t)(DT\_REG\_SIZE\_BY\_NAME(node\_id, message\_ram) - CAN\_MCAN\_DT\_MRAM\_OFFSET(node\_id))

619

[ 627](can__mcan_8h.md#a47fa1c0ca484d6f891c4834071d421e4)#define CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE(node\_id) \

628 (CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET(node\_id) + \

629 CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(node\_id) \* sizeof(struct can\_mcan\_tx\_buffer))

630

[ 641](can__mcan_8h.md#a146911ec873fd653f8f9538a85202917)#define CAN\_MCAN\_DT\_MRAM\_DEFINE(node\_id, \_name) \

642 BUILD\_ASSERT(CAN\_MCAN\_DT\_MRAM\_OFFSET(node\_id) == 0, "offset must be 0"); \

643 static char \_\_nocache\_noinit \_\_aligned(4) \_name[CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE(node\_id)];

644

[ 650](can__mcan_8h.md#af277dd5f60b0620b3ffc5030f0c794f6)#define CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG(node\_id) \

651 BUILD\_ASSERT(CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(node\_id) <= 128, \

652 "Maximum Standard filter elements exceeded"); \

653 BUILD\_ASSERT(CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(node\_id) <= 64, \

654 "Maximum Extended filter elements exceeded"); \

655 BUILD\_ASSERT(CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(node\_id) <= 64, \

656 "Maximum Rx FIFO 0 elements exceeded"); \

657 BUILD\_ASSERT(CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(node\_id) <= 64, \

658 "Maximum Rx FIFO 1 elements exceeded"); \

659 BUILD\_ASSERT(CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(node\_id) <= 64, \

660 "Maximum Rx Buffer elements exceeded"); \

661 BUILD\_ASSERT(CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(node\_id) <= 32, \

662 "Maximum Tx Buffer elements exceeded"); \

663 BUILD\_ASSERT(CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(node\_id) <= 32, \

664 "Maximum Tx Buffer elements exceeded");

665

[ 672](can__mcan_8h.md#a3095ec5dd938ab990c71c06b5ba84d03)#define CAN\_MCAN\_DT\_INST\_MRAM\_OFFSET(inst) CAN\_MCAN\_DT\_MRAM\_OFFSET(DT\_DRV\_INST(inst))

673

[ 680](can__mcan_8h.md#a41d9d7f70dfedbe8eeacfd27a8610007)#define CAN\_MCAN\_DT\_INST\_MRAM\_STD\_FILTER\_ELEMENTS(inst) \

681 CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(DT\_DRV\_INST(inst))

682

[ 689](can__mcan_8h.md#aac3f321fee276c68e51073dfbcd81150)#define CAN\_MCAN\_DT\_INST\_MRAM\_EXT\_FILTER\_ELEMENTS(inst) \

690 CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(DT\_DRV\_INST(inst))

691

[ 698](can__mcan_8h.md#a393289abde09b6190964fe69f2529c27)#define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO0\_ELEMENTS(inst) \

699 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(DT\_DRV\_INST(inst))

700

[ 707](can__mcan_8h.md#a30eef08af0433049ed28c51d640d3679)#define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO1\_ELEMENTS(inst) \

708 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(DT\_DRV\_INST(inst))

709

[ 716](can__mcan_8h.md#aa2a372c40cce733d10d9b33651cfdb1c)#define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_BUFFER\_ELEMENTS(inst) \

717 CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(DT\_DRV\_INST(inst))

718

[ 725](can__mcan_8h.md#ae10a6c1414a951808e818728e5d74e52)#define CAN\_MCAN\_DT\_INST\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(inst) \

726 CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(DT\_DRV\_INST(inst))

727

[ 734](can__mcan_8h.md#aa4275ca727057cdf4a0fe486b87d238d)#define CAN\_MCAN\_DT\_INST\_MRAM\_TX\_BUFFER\_ELEMENTS(inst) \

735 CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(DT\_DRV\_INST(inst))

736

[ 743](can__mcan_8h.md#a9c7a3869df9defc3f466f8de89b86561)#define CAN\_MCAN\_DT\_INST\_MRAM\_STD\_FILTER\_OFFSET(inst) \

744 CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET(DT\_DRV\_INST(inst))

745

[ 752](can__mcan_8h.md#a8595df90a5c45639ae9e576dcc61ea0d)#define CAN\_MCAN\_DT\_INST\_MRAM\_EXT\_FILTER\_OFFSET(inst) \

753 CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET(DT\_DRV\_INST(inst))

754

[ 761](can__mcan_8h.md#a48fe93b1bd51cdb7dcb1312ee160eab7)#define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO0\_OFFSET(inst) \

762 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET(DT\_DRV\_INST(inst))

763

[ 770](can__mcan_8h.md#ad80049c12ef02f78736268f9abb7c303)#define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO1\_OFFSET(inst) \

771 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET(DT\_DRV\_INST(inst))

772

[ 779](can__mcan_8h.md#aea15c0e894fdbacaeead2d108c7c0b94)#define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_BUFFER\_OFFSET(inst) \

780 CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET(DT\_DRV\_INST(inst))

781

[ 788](can__mcan_8h.md#a63623852de6c5dd34509823446db1af9)#define CAN\_MCAN\_DT\_INST\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(inst) \

789 CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(DT\_DRV\_INST(inst))

790

[ 797](can__mcan_8h.md#a9bb9a0d6d8b3de3e24d533ec15c1215d)#define CAN\_MCAN\_DT\_INST\_MRAM\_TX\_BUFFER\_OFFSET(inst) \

798 CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET(DT\_DRV\_INST(inst))

799

[ 806](can__mcan_8h.md#affa0cab849e56fe5016bc4aa8b43a1d1)#define CAN\_MCAN\_DT\_INST\_MCAN\_ADDR(inst) CAN\_MCAN\_DT\_MCAN\_ADDR(DT\_DRV\_INST(inst))

807

[ 814](can__mcan_8h.md#a25b114591fdf1330865adfa7706cd62b)#define CAN\_MCAN\_DT\_INST\_MRBA(inst) CAN\_MCAN\_DT\_MRBA(DT\_DRV\_INST(inst))

815

[ 822](can__mcan_8h.md#a6fee1c336a0c7de5d8cda6bf2338ad3c)#define CAN\_MCAN\_DT\_INST\_MRAM\_ADDR(inst) CAN\_MCAN\_DT\_MRAM\_ADDR(DT\_DRV\_INST(inst))

823

[ 830](can__mcan_8h.md#a63e750530c43000bafa36a808582f9d4)#define CAN\_MCAN\_DT\_INST\_MRAM\_SIZE(inst) CAN\_MCAN\_DT\_MRAM\_SIZE(DT\_DRV\_INST(inst))

831

[ 838](can__mcan_8h.md#a5d0cc45852e301e4e38652218a5fc594)#define CAN\_MCAN\_DT\_INST\_MRAM\_ELEMENTS\_SIZE(inst) CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE(DT\_DRV\_INST(inst))

839

[ 846](can__mcan_8h.md#a6081976c4a78765061c3832253e2bcda)#define CAN\_MCAN\_DT\_INST\_MRAM\_DEFINE(inst, \_name) CAN\_MCAN\_DT\_MRAM\_DEFINE(DT\_DRV\_INST(inst), \_name)

847

[ 851](can__mcan_8h.md#aa0de1f9512dc3e3d44f06a2f7f2f4adf)#define CAN\_MCAN\_TIMING\_MIN\_INITIALIZER \

852 { \

853 .sjw = 1, \

854 .prop\_seg = 0, \

855 .phase\_seg1 = 2, \

856 .phase\_seg2 = 2, \

857 .prescaler = 1 \

858 }

859

[ 863](can__mcan_8h.md#aedef0bb36bcd204ee5000ae9528248b7)#define CAN\_MCAN\_TIMING\_MAX\_INITIALIZER \

864 { \

865 .sjw = 128, \

866 .prop\_seg = 0, \

867 .phase\_seg1 = 256, \

868 .phase\_seg2 = 128, \

869 .prescaler = 512 \

870 }

871

[ 875](can__mcan_8h.md#afd190643aa2435880769aef338f02d23)#define CAN\_MCAN\_TIMING\_DATA\_MIN\_INITIALIZER \

876 { \

877 .sjw = 1, \

878 .prop\_seg = 0, \

879 .phase\_seg1 = 1, \

880 .phase\_seg2 = 1, \

881 .prescaler = 1 \

882 }

883

[ 887](can__mcan_8h.md#aa0f79f1ce18146a1ad90609e4020308c)#define CAN\_MCAN\_TIMING\_DATA\_MAX\_INITIALIZER \

888 { \

889 .sjw = 16, \

890 .prop\_seg = 0, \

891 .phase\_seg1 = 32, \

892 .phase\_seg2 = 16, \

893 .prescaler = 32 \

894 }

895

[ 901](can__mcan_8h.md#a67daccd5aed8a4de6fc7489592a6b268)#define CAN\_MCAN\_DT\_INST\_BUILD\_ASSERT\_MRAM\_CFG(inst) \

902 CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG(DT\_DRV\_INST(inst))

903

[ 909](structcan__mcan__rx__fifo__hdr.md)struct [can\_mcan\_rx\_fifo\_hdr](structcan__mcan__rx__fifo__hdr.md) {

910 union {

911 struct {

[ 912](structcan__mcan__rx__fifo__hdr.md#acdea19720ee1d76254b6e9931ffeca07) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ext\_id](structcan__mcan__rx__fifo__hdr.md#acdea19720ee1d76254b6e9931ffeca07): 29;

[ 913](structcan__mcan__rx__fifo__hdr.md#aa315257f7f5dcb438ba70c22ced8b9fe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtr](structcan__mcan__rx__fifo__hdr.md#aa315257f7f5dcb438ba70c22ced8b9fe): 1;

[ 914](structcan__mcan__rx__fifo__hdr.md#ab75c330ef4724997f665a84c99ab2c57) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [xtd](structcan__mcan__rx__fifo__hdr.md#ab75c330ef4724997f665a84c99ab2c57): 1;

[ 915](structcan__mcan__rx__fifo__hdr.md#a746f7f80e30ac574fcb785e78cbcdf44) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esi](structcan__mcan__rx__fifo__hdr.md#a746f7f80e30ac574fcb785e78cbcdf44): 1;

916 };

917 struct {

[ 918](structcan__mcan__rx__fifo__hdr.md#afbdea1a9674af705a4954709e64ed45a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad1](structcan__mcan__rx__fifo__hdr.md#afbdea1a9674af705a4954709e64ed45a): 18;

[ 919](structcan__mcan__rx__fifo__hdr.md#ac97eacf0d6cf2ef9ae6454b7604b52b5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [std\_id](structcan__mcan__rx__fifo__hdr.md#ac97eacf0d6cf2ef9ae6454b7604b52b5): 11;

[ 920](structcan__mcan__rx__fifo__hdr.md#a03a015b8195efeda0287b1323de54b3c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad2](structcan__mcan__rx__fifo__hdr.md#a03a015b8195efeda0287b1323de54b3c): 3;

921 };

922 };

[ 923](structcan__mcan__rx__fifo__hdr.md#ace6229b7580d1954638d1469700f5ebd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rxts](structcan__mcan__rx__fifo__hdr.md#ace6229b7580d1954638d1469700f5ebd): 16;

[ 924](structcan__mcan__rx__fifo__hdr.md#a44564c3ab98be8cd92b6f17c9379d045) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dlc](structcan__mcan__rx__fifo__hdr.md#a44564c3ab98be8cd92b6f17c9379d045): 4;

[ 925](structcan__mcan__rx__fifo__hdr.md#a35d6a09669761d4b7d60c06e36f74e06) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [brs](structcan__mcan__rx__fifo__hdr.md#a35d6a09669761d4b7d60c06e36f74e06): 1;

[ 926](structcan__mcan__rx__fifo__hdr.md#a8beb206b8c5ef1dd7c25d17ef5045d55) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fdf](structcan__mcan__rx__fifo__hdr.md#a8beb206b8c5ef1dd7c25d17ef5045d55): 1;

[ 927](structcan__mcan__rx__fifo__hdr.md#a0f95cfa20e9a9e1c75da3afb1dd4542f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [res](structcan__mcan__rx__fifo__hdr.md#a0f95cfa20e9a9e1c75da3afb1dd4542f): 2;

[ 928](structcan__mcan__rx__fifo__hdr.md#ad6bcb3637d79f4e87371dd91fb7a5881) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fidx](structcan__mcan__rx__fifo__hdr.md#ad6bcb3637d79f4e87371dd91fb7a5881): 7;

[ 929](structcan__mcan__rx__fifo__hdr.md#a6256e635694330dc3428f30387838f96) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [anmf](structcan__mcan__rx__fifo__hdr.md#a6256e635694330dc3428f30387838f96): 1;

930} \_\_packed \_\_aligned(4);

931

[ 937](structcan__mcan__rx__fifo.md)struct [can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md) {

[ 938](structcan__mcan__rx__fifo.md#a8ddf6a5aa6f9847c3b5c0fce66631133) struct [can\_mcan\_rx\_fifo\_hdr](structcan__mcan__rx__fifo__hdr.md) [hdr](structcan__mcan__rx__fifo.md#a8ddf6a5aa6f9847c3b5c0fce66631133);

939 union {

[ 940](structcan__mcan__rx__fifo.md#aeafd55c4d4f637c66e5a57d329e42a2b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structcan__mcan__rx__fifo.md#aeafd55c4d4f637c66e5a57d329e42a2b)[64];

[ 941](structcan__mcan__rx__fifo.md#a9a5e7e970f2733b68894edcbaf98cc82) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_32](structcan__mcan__rx__fifo.md#a9a5e7e970f2733b68894edcbaf98cc82)[16];

942 };

943} \_\_packed \_\_aligned(4);

944

[ 950](structcan__mcan__tx__buffer__hdr.md)struct [can\_mcan\_tx\_buffer\_hdr](structcan__mcan__tx__buffer__hdr.md) {

951 union {

952 struct {

[ 953](structcan__mcan__tx__buffer__hdr.md#ab4800365c1f2cd76c2e19c27b8d72956) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ext\_id](structcan__mcan__tx__buffer__hdr.md#ab4800365c1f2cd76c2e19c27b8d72956): 29;

[ 954](structcan__mcan__tx__buffer__hdr.md#a6ef37c0a073550c2b99ec29fdb834ca1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtr](structcan__mcan__tx__buffer__hdr.md#a6ef37c0a073550c2b99ec29fdb834ca1): 1;

[ 955](structcan__mcan__tx__buffer__hdr.md#a0ee2e857b6f63c2d70179d89398ffb9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [xtd](structcan__mcan__tx__buffer__hdr.md#a0ee2e857b6f63c2d70179d89398ffb9a): 1;

[ 956](structcan__mcan__tx__buffer__hdr.md#ae30ffd52da3ea38188fa04ace20054ad) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esi](structcan__mcan__tx__buffer__hdr.md#ae30ffd52da3ea38188fa04ace20054ad): 1;

957 };

958 struct {

[ 959](structcan__mcan__tx__buffer__hdr.md#ac78c3e0f4dda2eddc25ae8066cc29134) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad1](structcan__mcan__tx__buffer__hdr.md#ac78c3e0f4dda2eddc25ae8066cc29134): 18;

[ 960](structcan__mcan__tx__buffer__hdr.md#a9b1f4f0f66d1de07cf6ed212baa713be) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [std\_id](structcan__mcan__tx__buffer__hdr.md#a9b1f4f0f66d1de07cf6ed212baa713be): 11;

[ 961](structcan__mcan__tx__buffer__hdr.md#aa43b5da1708dbf49794c586ca3af7365) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad2](structcan__mcan__tx__buffer__hdr.md#aa43b5da1708dbf49794c586ca3af7365): 3;

962 };

963 };

[ 964](structcan__mcan__tx__buffer__hdr.md#a4bd206867f0ba937b93888285ea4095a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [res1](structcan__mcan__tx__buffer__hdr.md#a4bd206867f0ba937b93888285ea4095a);

[ 965](structcan__mcan__tx__buffer__hdr.md#a9b96b8b75d4ff4c9df3192a244dabc82) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlc](structcan__mcan__tx__buffer__hdr.md#a9b96b8b75d4ff4c9df3192a244dabc82): 4;

[ 966](structcan__mcan__tx__buffer__hdr.md#af6554e36649326a1ee01757096e1c68f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [brs](structcan__mcan__tx__buffer__hdr.md#af6554e36649326a1ee01757096e1c68f): 1;

[ 967](structcan__mcan__tx__buffer__hdr.md#a7ac73d1c09b84267a4701b5d4fa7c920) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fdf](structcan__mcan__tx__buffer__hdr.md#a7ac73d1c09b84267a4701b5d4fa7c920): 1;

[ 968](structcan__mcan__tx__buffer__hdr.md#a053c1a8d986dd4537398c052712d394d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tsce](structcan__mcan__tx__buffer__hdr.md#a053c1a8d986dd4537398c052712d394d): 1;

[ 969](structcan__mcan__tx__buffer__hdr.md#a6f760970f0483dc16aa8ecc0715591d3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [efc](structcan__mcan__tx__buffer__hdr.md#a6f760970f0483dc16aa8ecc0715591d3): 1;

[ 970](structcan__mcan__tx__buffer__hdr.md#ac76ce5728912347d0193c4ed5f467c92) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mm](structcan__mcan__tx__buffer__hdr.md#ac76ce5728912347d0193c4ed5f467c92);

971} \_\_packed \_\_aligned(4);

972

[ 978](structcan__mcan__tx__buffer.md)struct [can\_mcan\_tx\_buffer](structcan__mcan__tx__buffer.md) {

[ 979](structcan__mcan__tx__buffer.md#a5b553813e69bf22565d2894e8137672d) struct [can\_mcan\_tx\_buffer\_hdr](structcan__mcan__tx__buffer__hdr.md) [hdr](structcan__mcan__tx__buffer.md#a5b553813e69bf22565d2894e8137672d);

980 union {

[ 981](structcan__mcan__tx__buffer.md#af69274236867987f069aa6dd29182f82) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structcan__mcan__tx__buffer.md#af69274236867987f069aa6dd29182f82)[64];

[ 982](structcan__mcan__tx__buffer.md#a4b1a8963e8da21c01843f20e9e01bb11) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_32](structcan__mcan__tx__buffer.md#a4b1a8963e8da21c01843f20e9e01bb11)[16];

983 };

984} \_\_packed \_\_aligned(4);

985

[ 991](structcan__mcan__tx__event__fifo.md)struct [can\_mcan\_tx\_event\_fifo](structcan__mcan__tx__event__fifo.md) {

992 union {

993 struct {

[ 994](structcan__mcan__tx__event__fifo.md#a3b4c61b9edcd1720235c3784131693d1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ext\_id](structcan__mcan__tx__event__fifo.md#a3b4c61b9edcd1720235c3784131693d1): 29;

[ 995](structcan__mcan__tx__event__fifo.md#a17d5b6caf6519bf199dc179c11550abb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtr](structcan__mcan__tx__event__fifo.md#a17d5b6caf6519bf199dc179c11550abb): 1;

[ 996](structcan__mcan__tx__event__fifo.md#aac19c259f3e966d771c0088a32cbe47d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [xtd](structcan__mcan__tx__event__fifo.md#aac19c259f3e966d771c0088a32cbe47d): 1;

[ 997](structcan__mcan__tx__event__fifo.md#a796967d04c60cd9cf423d904c6118944) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esi](structcan__mcan__tx__event__fifo.md#a796967d04c60cd9cf423d904c6118944): 1;

998 };

999 struct {

[ 1000](structcan__mcan__tx__event__fifo.md#a6be85a808788bd611055235b00a9b1f4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad1](structcan__mcan__tx__event__fifo.md#a6be85a808788bd611055235b00a9b1f4): 18;

[ 1001](structcan__mcan__tx__event__fifo.md#a7698679cf93c707b423e9c695209f072) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [std\_id](structcan__mcan__tx__event__fifo.md#a7698679cf93c707b423e9c695209f072): 11;

[ 1002](structcan__mcan__tx__event__fifo.md#a461d68069593b42d6961d6ff0525f783) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad2](structcan__mcan__tx__event__fifo.md#a461d68069593b42d6961d6ff0525f783): 3;

1003 };

1004 };

[ 1005](structcan__mcan__tx__event__fifo.md#aacc10d577c20325baf54d7bb20e32583) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [txts](structcan__mcan__tx__event__fifo.md#aacc10d577c20325baf54d7bb20e32583);

[ 1006](structcan__mcan__tx__event__fifo.md#a96aa98b30f603a5c5676e6a244f5d6c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlc](structcan__mcan__tx__event__fifo.md#a96aa98b30f603a5c5676e6a244f5d6c9): 4;

[ 1007](structcan__mcan__tx__event__fifo.md#ac3924771aeb8885b4ad8d59758131b1a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [brs](structcan__mcan__tx__event__fifo.md#ac3924771aeb8885b4ad8d59758131b1a): 1;

[ 1008](structcan__mcan__tx__event__fifo.md#a4075852d322da2eb4e3acb9d7c2e6d64) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fdf](structcan__mcan__tx__event__fifo.md#a4075852d322da2eb4e3acb9d7c2e6d64): 1;

[ 1009](structcan__mcan__tx__event__fifo.md#a23ff309d6fb887166da2290646df200c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [et](structcan__mcan__tx__event__fifo.md#a23ff309d6fb887166da2290646df200c): 2;

[ 1010](structcan__mcan__tx__event__fifo.md#a4a706b7da7d9354ffc559ec65e1701ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mm](structcan__mcan__tx__event__fifo.md#a4a706b7da7d9354ffc559ec65e1701ca);

1011} \_\_packed \_\_aligned(4);

1012

1013/\* Bosch M\_CAN Standard/Extended Filter Element Configuration (SFEC/EFEC) \*/

[ 1014](can__mcan_8h.md#ac336e47e175c4c54469ce58ca122195c)#define CAN\_MCAN\_XFEC\_DISABLE 0x0

[ 1015](can__mcan_8h.md#a7312f835309269943ff6b758521449b6)#define CAN\_MCAN\_XFEC\_FIFO0 0x1

[ 1016](can__mcan_8h.md#ad0570275343000c1af9a14e0589939c3)#define CAN\_MCAN\_XFEC\_FIFO1 0x2

[ 1017](can__mcan_8h.md#a2cd5607208221a6da2cf07e67ef00dde)#define CAN\_MCAN\_XFEC\_REJECT 0x3

[ 1018](can__mcan_8h.md#a95f862be638ce43223aebcd1f763be2d)#define CAN\_MCAN\_XFEC\_PRIO 0x4

[ 1019](can__mcan_8h.md#aec0a8173842cc5f1a13e84fb5ee38f19)#define CAN\_MCAN\_XFEC\_PRIO\_FIFO0 0x5

[ 1020](can__mcan_8h.md#a3073ff3bc20ef4a28af1d92f9d2e9a02)#define CAN\_MCAN\_XFEC\_PRIO\_FIFO1 0x7

1021

1022/\* Bosch M\_CAN Standard Filter Type (SFT) \*/

[ 1023](can__mcan_8h.md#a39fcb587e3a98e256fd70af2408d1fc4)#define CAN\_MCAN\_SFT\_RANGE 0x0

[ 1024](can__mcan_8h.md#aadfcd6a191d8eb4c2f0403cba4518a8e)#define CAN\_MCAN\_SFT\_DUAL 0x1

[ 1025](can__mcan_8h.md#a7d5274ba0f020deda315bd10da7787ce)#define CAN\_MCAN\_SFT\_CLASSIC 0x2

[ 1026](can__mcan_8h.md#ac64298dffd12e5f148438af6b2c9f578)#define CAN\_MCAN\_SFT\_DISABLED 0x3

1027

[ 1033](structcan__mcan__std__filter.md)struct [can\_mcan\_std\_filter](structcan__mcan__std__filter.md) {

[ 1034](structcan__mcan__std__filter.md#a050f5018825d3afa350b35d101569f50) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sfid2](structcan__mcan__std__filter.md#a050f5018825d3afa350b35d101569f50): 11;

[ 1035](structcan__mcan__std__filter.md#adb5bb096566c3fecf9727a800dbfe3cd) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [res](structcan__mcan__std__filter.md#adb5bb096566c3fecf9727a800dbfe3cd): 5;

[ 1036](structcan__mcan__std__filter.md#a7d80d641985ab67e09eb4d11015af2b3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sfid1](structcan__mcan__std__filter.md#a7d80d641985ab67e09eb4d11015af2b3): 11;

[ 1037](structcan__mcan__std__filter.md#ad943ff357a00cca569f164599b9f49e5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sfec](structcan__mcan__std__filter.md#ad943ff357a00cca569f164599b9f49e5): 3;

[ 1038](structcan__mcan__std__filter.md#afb89a40ac7c585c75d6bbaf3705e913a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sft](structcan__mcan__std__filter.md#afb89a40ac7c585c75d6bbaf3705e913a): 2;

1039} \_\_packed \_\_aligned(4);

1040

1041/\* Bosch M\_CAN Extended Filter Type (EFT) \*/

[ 1042](can__mcan_8h.md#a2391eb72cedd2f2cc17959c73bb1afb4)#define CAN\_MCAN\_EFT\_RANGE\_XIDAM 0x0

[ 1043](can__mcan_8h.md#aaa5fe73386232cef16ffb79561064200)#define CAN\_MCAN\_EFT\_DUAL 0x1

[ 1044](can__mcan_8h.md#aa04e5c32ec68157807013ae542339c34)#define CAN\_MCAN\_EFT\_CLASSIC 0x2

[ 1045](can__mcan_8h.md#ae0ebf402133070f34c942230f0ae9f6a)#define CAN\_MCAN\_EFT\_RANGE 0x3

1046

[ 1052](structcan__mcan__ext__filter.md)struct [can\_mcan\_ext\_filter](structcan__mcan__ext__filter.md) {

[ 1053](structcan__mcan__ext__filter.md#a54b3ac39e57cb02136a5d1bf5af1c75b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [efid1](structcan__mcan__ext__filter.md#a54b3ac39e57cb02136a5d1bf5af1c75b): 29;

[ 1054](structcan__mcan__ext__filter.md#a6a3042f7b236fb2d06334c4c5bc91530) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [efec](structcan__mcan__ext__filter.md#a6a3042f7b236fb2d06334c4c5bc91530): 3;

[ 1055](structcan__mcan__ext__filter.md#a12147937f9889e835cf89f5a99ab62d8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [efid2](structcan__mcan__ext__filter.md#a12147937f9889e835cf89f5a99ab62d8): 29;

[ 1056](structcan__mcan__ext__filter.md#a2e2c2d57015bf7aabbbe510660430bd7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [esync](structcan__mcan__ext__filter.md#a2e2c2d57015bf7aabbbe510660430bd7): 1;

[ 1057](structcan__mcan__ext__filter.md#aa94145f8e7f7d8668f383f174f6420b8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eft](structcan__mcan__ext__filter.md#aa94145f8e7f7d8668f383f174f6420b8): 2;

1058} \_\_packed \_\_aligned(4);

1059

[ 1063](structcan__mcan__data.md)struct [can\_mcan\_data](structcan__mcan__data.md) {

[ 1064](structcan__mcan__data.md#a486500387e6351f68d741f089d57f913) struct can\_driver\_data [common](structcan__mcan__data.md#a486500387e6351f68d741f089d57f913);

[ 1065](structcan__mcan__data.md#a27048362bd5d4288e3ea9018ccc210f6) struct [k\_mutex](structk__mutex.md) [lock](structcan__mcan__data.md#a27048362bd5d4288e3ea9018ccc210f6);

[ 1066](structcan__mcan__data.md#a5e0239c7ff45045d4f4ca5c83a41c4dd) struct k\_sem [tx\_sem](structcan__mcan__data.md#a5e0239c7ff45045d4f4ca5c83a41c4dd);

[ 1067](structcan__mcan__data.md#a535ad3150d0c64f11b4dd4e3010d4718) struct [k\_mutex](structk__mutex.md) [tx\_mtx](structcan__mcan__data.md#a535ad3150d0c64f11b4dd4e3010d4718);

[ 1068](structcan__mcan__data.md#a4211c8dce9704c43790ac354d124c3ab) void \*[custom](structcan__mcan__data.md#a4211c8dce9704c43790ac354d124c3ab);

1069} \_\_aligned(4);

1070

[ 1082](can__mcan_8h.md#a79941b7745919bb1bf7d7219555440a6)typedef int (\*[can\_mcan\_read\_reg\_t](can__mcan_8h.md#a79941b7745919bb1bf7d7219555440a6))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

1083

[ 1095](can__mcan_8h.md#acbb72b712e516fe923e6030a9d6b36c1)typedef int (\*[can\_mcan\_write\_reg\_t](can__mcan_8h.md#acbb72b712e516fe923e6030a9d6b36c1))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

1096

[ 1109](can__mcan_8h.md#a9532f0655c579f0ab091f85771b5d62d)typedef int (\*[can\_mcan\_read\_mram\_t](can__mcan_8h.md#a9532f0655c579f0ab091f85771b5d62d))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, void \*dst,

1110 size\_t len);

1111

[ 1124](can__mcan_8h.md#aaf2920e649f9671f09856a062ac4dc95)typedef int (\*[can\_mcan\_write\_mram\_t](can__mcan_8h.md#aaf2920e649f9671f09856a062ac4dc95))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*src,

1125 size\_t len);

1126

[ 1140](can__mcan_8h.md#a321813b4b3def118480a7a9eccb6d4aa)typedef int (\*[can\_mcan\_clear\_mram\_t](can__mcan_8h.md#a321813b4b3def118480a7a9eccb6d4aa))(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, size\_t len);

1141

[ 1145](structcan__mcan__ops.md)struct [can\_mcan\_ops](structcan__mcan__ops.md) {

[ 1146](structcan__mcan__ops.md#a0c9986b8fda47f3cc08128e2f951d1fb) [can\_mcan\_read\_reg\_t](can__mcan_8h.md#a79941b7745919bb1bf7d7219555440a6) [read\_reg](structcan__mcan__ops.md#a0c9986b8fda47f3cc08128e2f951d1fb);

[ 1147](structcan__mcan__ops.md#a2d977bb8a98e6f2f787723eb9104f949) [can\_mcan\_write\_reg\_t](can__mcan_8h.md#acbb72b712e516fe923e6030a9d6b36c1) [write\_reg](structcan__mcan__ops.md#a2d977bb8a98e6f2f787723eb9104f949);

[ 1148](structcan__mcan__ops.md#ac0f1adfa81042116f5da861c557562b2) [can\_mcan\_read\_mram\_t](can__mcan_8h.md#a9532f0655c579f0ab091f85771b5d62d) [read\_mram](structcan__mcan__ops.md#ac0f1adfa81042116f5da861c557562b2);

[ 1149](structcan__mcan__ops.md#ab040466ab26383567dac85c08b077250) [can\_mcan\_write\_mram\_t](can__mcan_8h.md#aaf2920e649f9671f09856a062ac4dc95) [write\_mram](structcan__mcan__ops.md#ab040466ab26383567dac85c08b077250);

[ 1150](structcan__mcan__ops.md#abde9d0a2aeece4545d7fa42f3cac3aad) [can\_mcan\_clear\_mram\_t](can__mcan_8h.md#a321813b4b3def118480a7a9eccb6d4aa) [clear\_mram](structcan__mcan__ops.md#abde9d0a2aeece4545d7fa42f3cac3aad);

1151};

1152

[ 1156](structcan__mcan__tx__callback.md)struct [can\_mcan\_tx\_callback](structcan__mcan__tx__callback.md) {

[ 1157](structcan__mcan__tx__callback.md#affda660bd76b14694f8f59d58c5f49f8) [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) [function](structcan__mcan__tx__callback.md#affda660bd76b14694f8f59d58c5f49f8);

[ 1158](structcan__mcan__tx__callback.md#a0af42dc41c9a7d4d0fe245ef78b857ad) void \*[user\_data](structcan__mcan__tx__callback.md#a0af42dc41c9a7d4d0fe245ef78b857ad);

1159};

1160

[ 1164](structcan__mcan__rx__callback.md)struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md) {

[ 1165](structcan__mcan__rx__callback.md#adc5ed2295bf18e2c5e4c806e1f488668) [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) [function](structcan__mcan__rx__callback.md#adc5ed2295bf18e2c5e4c806e1f488668);

[ 1166](structcan__mcan__rx__callback.md#ab6196a8d1f7a067c872d4d0fe7d7d00b) void \*[user\_data](structcan__mcan__rx__callback.md#ab6196a8d1f7a067c872d4d0fe7d7d00b);

1167};

1168

[ 1172](structcan__mcan__callbacks.md)struct [can\_mcan\_callbacks](structcan__mcan__callbacks.md) {

[ 1173](structcan__mcan__callbacks.md#ad2ee7f63634cc67160f4eb75f05babd2) struct [can\_mcan\_tx\_callback](structcan__mcan__tx__callback.md) \*[tx](structcan__mcan__callbacks.md#ad2ee7f63634cc67160f4eb75f05babd2);

[ 1174](structcan__mcan__callbacks.md#ae225638097e1ddb5270de06401490a7f) struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md) \*[std](structcan__mcan__callbacks.md#ae225638097e1ddb5270de06401490a7f);

[ 1175](structcan__mcan__callbacks.md#ab29bb0963a78fcc68677ff5e4589f004) struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md) \*[ext](structcan__mcan__callbacks.md#ab29bb0963a78fcc68677ff5e4589f004);

[ 1176](structcan__mcan__callbacks.md#aad1b8f0b76637e7a53ef5c88118d7bd1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_tx](structcan__mcan__callbacks.md#aad1b8f0b76637e7a53ef5c88118d7bd1);

[ 1177](structcan__mcan__callbacks.md#a0388e27fc1852d7e7c7ac6f062cab3e1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_std](structcan__mcan__callbacks.md#a0388e27fc1852d7e7c7ac6f062cab3e1);

[ 1178](structcan__mcan__callbacks.md#a9edfccadf0ef4006ac5eb7926772ca85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_ext](structcan__mcan__callbacks.md#a9edfccadf0ef4006ac5eb7926772ca85);

1179};

1180

[ 1197](can__mcan_8h.md#ab5e7cb2c8423200a929544a18ad66c2a)#define CAN\_MCAN\_CALLBACKS\_DEFINE(\_name, \_tx, \_std, \_ext) \

1198 static struct can\_mcan\_tx\_callback \_name##\_tx\_cbs[\_tx]; \

1199 static struct can\_mcan\_rx\_callback \_name##\_std\_cbs[\_std]; \

1200 static struct can\_mcan\_rx\_callback \_name##\_ext\_cbs[\_ext]; \

1201 static const struct can\_mcan\_callbacks \_name = { \

1202 .tx = \_name##\_tx\_cbs, \

1203 .std = \_name##\_std\_cbs, \

1204 .ext = \_name##\_ext\_cbs, \

1205 .num\_tx = \_tx, \

1206 .num\_std = \_std, \

1207 .num\_ext = \_ext, \

1208 }

1209

[ 1216](can__mcan_8h.md#a8264915913cfdb4cd7fe5d53cb6cf64b)#define CAN\_MCAN\_DT\_CALLBACKS\_DEFINE(node\_id, \_name) \

1217 CAN\_MCAN\_CALLBACKS\_DEFINE(\_name, CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(node\_id), \

1218 CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(node\_id), \

1219 CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(node\_id))

1220

[ 1227](can__mcan_8h.md#a93e84f959d380f927473ca3b9510d7bc)#define CAN\_MCAN\_DT\_INST\_CALLBACKS\_DEFINE(inst, \_name) \

1228 CAN\_MCAN\_DT\_CALLBACKS\_DEFINE(DT\_DRV\_INST(inst), \_name)

1229

[ 1233](structcan__mcan__config.md)struct [can\_mcan\_config](structcan__mcan__config.md) {

[ 1234](structcan__mcan__config.md#a86a6f9a19db54c7368f16f72513db327) const struct can\_driver\_config [common](structcan__mcan__config.md#a86a6f9a19db54c7368f16f72513db327);

[ 1235](structcan__mcan__config.md#aed10f9a4d2ddc0045bc6f37939973039) const struct [can\_mcan\_ops](structcan__mcan__ops.md) \*[ops](structcan__mcan__config.md#aed10f9a4d2ddc0045bc6f37939973039);

[ 1236](structcan__mcan__config.md#a0c8500180fb8113e7bc36d446e4c39bb) const struct [can\_mcan\_callbacks](structcan__mcan__callbacks.md) \*[callbacks](structcan__mcan__config.md#a0c8500180fb8113e7bc36d446e4c39bb);

[ 1237](structcan__mcan__config.md#ab196bf74bf41fba65c0d076ff9070202) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mram\_elements](structcan__mcan__config.md#ab196bf74bf41fba65c0d076ff9070202)[[CAN\_MCAN\_MRAM\_CFG\_NUM\_CELLS](can__mcan_8h.md#abb4087b9c7ac31e8a1cb7003945dad97)];

[ 1238](structcan__mcan__config.md#a412c0bb0b3d8158cd352d4c24a622401) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mram\_offsets](structcan__mcan__config.md#a412c0bb0b3d8158cd352d4c24a622401)[[CAN\_MCAN\_MRAM\_CFG\_NUM\_CELLS](can__mcan_8h.md#abb4087b9c7ac31e8a1cb7003945dad97)];

[ 1239](structcan__mcan__config.md#a10585712cd11d041829dca9c9c5446e1) size\_t [mram\_size](structcan__mcan__config.md#a10585712cd11d041829dca9c9c5446e1);

[ 1240](structcan__mcan__config.md#a99df753a7f1c7e135b3d69b1c376608b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sjw](structcan__mcan__config.md#a99df753a7f1c7e135b3d69b1c376608b);

[ 1241](structcan__mcan__config.md#a1800aadb04f6b670cb9d1fefed11c4f8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [prop\_ts1](structcan__mcan__config.md#a1800aadb04f6b670cb9d1fefed11c4f8);

[ 1242](structcan__mcan__config.md#a0e7f2499e657f71d7a05e0a5bb870eef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ts2](structcan__mcan__config.md#a0e7f2499e657f71d7a05e0a5bb870eef);

1243#ifdef CONFIG\_CAN\_FD\_MODE

1244 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sjw\_data;

1245 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prop\_ts1\_data;

1246 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ts2\_data;

1247 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_delay\_comp\_offset;

1248#endif

[ 1249](structcan__mcan__config.md#a7b2d696b6839a8f958f705fb13a0f63d) const void \*[custom](structcan__mcan__config.md#a7b2d696b6839a8f958f705fb13a0f63d);

1250};

1251

[ 1260](can__mcan_8h.md#a2e52150401d29533258224a14600b255)#define CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET(node\_id) \

1261 { \

1262 0, /\* offset cell \*/ \

1263 CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(node\_id), \

1264 CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(node\_id), \

1265 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(node\_id), \

1266 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(node\_id), \

1267 CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(node\_id), \

1268 CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(node\_id), \

1269 CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(node\_id) \

1270 }

1271

[ 1280](can__mcan_8h.md#a907c70d4c64353647bf1718c45e11c5a)#define CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET(node\_id) \

1281 { \

1282 0, /\* offset cell \*/ \

1283 CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET(node\_id), \

1284 CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET(node\_id), \

1285 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET(node\_id), \

1286 CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET(node\_id), \

1287 CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET(node\_id), \

1288 CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(node\_id), \

1289 CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET(node\_id) \

1290 }

1291

1300#ifdef CONFIG\_CAN\_FD\_MODE

1301#define CAN\_MCAN\_DT\_CONFIG\_GET(node\_id, \_custom, \_ops, \_cbs) \

1302 { \

1303 .common = CAN\_DT\_DRIVER\_CONFIG\_GET(node\_id, 8000000), \

1304 .ops = \_ops, \

1305 .callbacks = \_cbs, \

1306 .mram\_elements = CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET(node\_id), \

1307 .mram\_offsets = CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET(node\_id), \

1308 .mram\_size = CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE(node\_id), \

1309 .sjw = DT\_PROP(node\_id, sjw), \

1310 .prop\_ts1 = DT\_PROP\_OR(node\_id, prop\_seg, 0) + DT\_PROP\_OR(node\_id, phase\_seg1, 0), \

1311 .ts2 = DT\_PROP\_OR(node\_id, phase\_seg2, 0), \

1312 .sjw\_data = DT\_PROP(node\_id, sjw\_data), \

1313 .prop\_ts1\_data = DT\_PROP\_OR(node\_id, prop\_seg\_data, 0) + \

1314 DT\_PROP\_OR(node\_id, phase\_seg1\_data, 0), \

1315 .ts2\_data = DT\_PROP\_OR(node\_id, phase\_seg2\_data, 0), \

1316 .tx\_delay\_comp\_offset = DT\_PROP(node\_id, tx\_delay\_comp\_offset), \

1317 .custom = \_custom, \

1318 }

1319#else /\* CONFIG\_CAN\_FD\_MODE \*/

[ 1320](can__mcan_8h.md#a6ebe5c51c603b5b820682e291df06ac8)#define CAN\_MCAN\_DT\_CONFIG\_GET(node\_id, \_custom, \_ops, \_cbs) \

1321 { \

1322 .common = CAN\_DT\_DRIVER\_CONFIG\_GET(node\_id, 8000000), \

1323 .ops = \_ops, \

1324 .callbacks = \_cbs, \

1325 .mram\_elements = CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET(node\_id), \

1326 .mram\_offsets = CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET(node\_id), \

1327 .mram\_size = CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE(node\_id), \

1328 .sjw = DT\_PROP(node\_id, sjw), \

1329 .prop\_ts1 = DT\_PROP\_OR(node\_id, prop\_seg, 0) + DT\_PROP\_OR(node\_id, phase\_seg1, 0), \

1330 .ts2 = DT\_PROP\_OR(node\_id, phase\_seg2, 0), \

1331 .custom = \_custom, \

1332 }

1333#endif /\* !CONFIG\_CAN\_FD\_MODE \*/

1334

[ 1344](can__mcan_8h.md#af001b33da9876cbde179757687d25ec0)#define CAN\_MCAN\_DT\_CONFIG\_INST\_GET(inst, \_custom, \_ops, \_cbs) \

1345 CAN\_MCAN\_DT\_CONFIG\_GET(DT\_DRV\_INST(inst), \_custom, \_ops, \_cbs)

1346

[ 1351](can__mcan_8h.md#a0684e639e58ecd6e7f8188cea455d4d8)#define CAN\_MCAN\_DATA\_INITIALIZER(\_custom) \

1352 { \

1353 .custom = \_custom, \

1354 }

1355

[ 1365](can__mcan_8h.md#a2138e6f7c669bf8a1c1f04637ec9752c)static inline int [can\_mcan\_sys\_read\_reg](can__mcan_8h.md#a2138e6f7c669bf8a1c1f04637ec9752c)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val)

1366{

1367 \*val = [sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)(base + reg);

1368

1369 return 0;

1370}

1371

[ 1381](can__mcan_8h.md#ac1562291a74cc1f5b5e6d82fe31141bb)static inline int [can\_mcan\_sys\_write\_reg](can__mcan_8h.md#ac1562291a74cc1f5b5e6d82fe31141bb)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1382{

1383 [sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)(val, base + reg);

1384

1385 return 0;

1386}

1387

[ 1401](can__mcan_8h.md#a5d7d5e0bb88b661462fa01720d824610)static inline int [can\_mcan\_sys\_read\_mram](can__mcan_8h.md#a5d7d5e0bb88b661462fa01720d824610)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, void \*dst, size\_t len)

1402{

1403 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src32 = (volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)(base + offset);

1404 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst32 = ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)dst;

1405 size\_t len32 = len / sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f));

1406

1407 \_\_ASSERT(base % 4U == 0U, "base must be a multiple of 4");

1408 \_\_ASSERT(offset % 4U == 0U, "offset must be a multiple of 4");

1409 \_\_ASSERT([POINTER\_TO\_UINT](group__sys-util.md#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(dst) % 4U == 0U, "dst must be 32-bit aligned");

1410 \_\_ASSERT(len % 4U == 0U, "len must be a multiple of 4");

1411

1412#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

1413 int err;

1414

1415 err = [sys\_cache\_data\_invd\_range](group__cache__interface.md#ga578f2f926cbf5ad196765881c8c1265e)((void \*)(base + offset), len);

1416 if (err != 0) {

1417 return err;

1418 }

1419#endif /\* !defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE) \*/

1420

1421 while (len32-- > 0) {

1422 \*dst32++ = \*src32++;

1423 }

1424

1425 return 0;

1426}

1427

[ 1441](can__mcan_8h.md#a21e0977205bb9db1be83968fda99bf95)static inline int [can\_mcan\_sys\_write\_mram](can__mcan_8h.md#a21e0977205bb9db1be83968fda99bf95)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*src,

1442 size\_t len)

1443{

1444 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst32 = (volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)(base + offset);

1445 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src32 = (const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)src;

1446 size\_t len32 = len / sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f));

1447

1448 \_\_ASSERT(base % 4U == 0U, "base must be a multiple of 4");

1449 \_\_ASSERT(offset % 4U == 0U, "offset must be a multiple of 4");

1450 \_\_ASSERT([POINTER\_TO\_UINT](group__sys-util.md#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)(src) % 4U == 0U, "src must be 32-bit aligned");

1451 \_\_ASSERT(len % 4U == 0U, "len must be a multiple of 4");

1452

1453 while (len32-- > 0) {

1454 \*dst32++ = \*src32++;

1455 }

1456

1457#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

1458 return [sys\_cache\_data\_flush\_range](group__cache__interface.md#ga6b61424f0aa81e2893c915b096de0cdb)((void \*)(base + offset), len);

1459#else /\* defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE) \*/

1460 return 0;

1461#endif /\* !defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE) \*/

1462}

1463

[ 1478](can__mcan_8h.md#a65c59db492d1c3359d032b5f8a62af8b)static inline int [can\_mcan\_sys\_clear\_mram](can__mcan_8h.md#a65c59db492d1c3359d032b5f8a62af8b)([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, size\_t len)

1479{

1480 volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst32 = (volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)(base + offset);

1481 size\_t len32 = len / sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f));

1482

1483 \_\_ASSERT(base % 4U == 0U, "base must be a multiple of 4");

1484 \_\_ASSERT(offset % 4U == 0U, "offset must be a multiple of 4");

1485 \_\_ASSERT(len % 4U == 0U, "len must be a multiple of 4");

1486

1487 while (len32-- > 0) {

1488 \*dst32++ = 0U;

1489 }

1490

1491#if defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE)

1492 return [sys\_cache\_data\_flush\_range](group__cache__interface.md#ga6b61424f0aa81e2893c915b096de0cdb)((void \*)(base + offset), len);

1493#else /\* defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE) \*/

1494 return 0;

1495#endif /\* !defined(CONFIG\_CACHE\_MANAGEMENT) && defined(CONFIG\_DCACHE) \*/

1496}

1497

[ 1509](can__mcan_8h.md#a05e01d009f6cb08f7e8497c9e2ee83ef)int [can\_mcan\_read\_reg](can__mcan_8h.md#a05e01d009f6cb08f7e8497c9e2ee83ef)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

1510

[ 1522](can__mcan_8h.md#a3f3e4be50fbf2c7ffcba99a1ca5ca7e1)int [can\_mcan\_write\_reg](can__mcan_8h.md#a3f3e4be50fbf2c7ffcba99a1ca5ca7e1)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

1523

[ 1536](can__mcan_8h.md#a1705a740e811f1065538c733498fc16f)static inline int [can\_mcan\_read\_mram](can__mcan_8h.md#a1705a740e811f1065538c733498fc16f)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, void \*dst,

1537 size\_t len)

1538{

1539 const struct [can\_mcan\_config](structcan__mcan__config.md) \*config = dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1540

1541 return config->[ops](structcan__mcan__config.md#aed10f9a4d2ddc0045bc6f37939973039)->[read\_mram](structcan__mcan__ops.md#ac0f1adfa81042116f5da861c557562b2)(dev, offset, dst, len);

1542}

1543

[ 1556](can__mcan_8h.md#ad2b88658a2294af890c56a99fee4a999)static inline int [can\_mcan\_write\_mram](can__mcan_8h.md#ad2b88658a2294af890c56a99fee4a999)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*src,

1557 size\_t len)

1558{

1559 const struct [can\_mcan\_config](structcan__mcan__config.md) \*config = dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1560

1561 return config->[ops](structcan__mcan__config.md#aed10f9a4d2ddc0045bc6f37939973039)->[write\_mram](structcan__mcan__ops.md#ab040466ab26383567dac85c08b077250)(dev, offset, src, len);

1562}

1563

[ 1577](can__mcan_8h.md#aa330897ffad0a9e1b4f08aaaa22e5c70)static inline int [can\_mcan\_clear\_mram](can__mcan_8h.md#aa330897ffad0a9e1b4f08aaaa22e5c70)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, size\_t len)

1578{

1579 const struct [can\_mcan\_config](structcan__mcan__config.md) \*config = dev->[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc);

1580

1581 return config->[ops](structcan__mcan__config.md#aed10f9a4d2ddc0045bc6f37939973039)->[clear\_mram](structcan__mcan__ops.md#abde9d0a2aeece4545d7fa42f3cac3aad)(dev, offset, len);

1582}

1583

[ 1606](can__mcan_8h.md#a2f9186fc69fe80b76133ab0f82100fc8)int [can\_mcan\_configure\_mram](can__mcan_8h.md#a2f9186fc69fe80b76133ab0f82100fc8)(const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) mrba, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) mram);

1607

[ 1613](can__mcan_8h.md#a7d9006cb2e91f6b13c3d245612b175f0)int [can\_mcan\_init](can__mcan_8h.md#a7d9006cb2e91f6b13c3d245612b175f0)(const struct [device](structdevice.md) \*dev);

1614

[ 1620](can__mcan_8h.md#a004d1a9aabc5307e6ab51a477f33c070)void [can\_mcan\_line\_0\_isr](can__mcan_8h.md#a004d1a9aabc5307e6ab51a477f33c070)(const struct [device](structdevice.md) \*dev);

1621

[ 1627](can__mcan_8h.md#a41e134fc94a573622eac9314f87dd673)void [can\_mcan\_line\_1\_isr](can__mcan_8h.md#a41e134fc94a573622eac9314f87dd673)(const struct [device](structdevice.md) \*dev);

1628

[ 1634](can__mcan_8h.md#a54f0e66b1b1912d841e10e68e01331fa)void [can\_mcan\_enable\_configuration\_change](can__mcan_8h.md#a54f0e66b1b1912d841e10e68e01331fa)(const struct [device](structdevice.md) \*dev);

1635

[ 1640](can__mcan_8h.md#abc9c13ee4f4b47d4ff74ab4c6352bbe1)int [can\_mcan\_get\_capabilities](can__mcan_8h.md#abc9c13ee4f4b47d4ff74ab4c6352bbe1)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap);

1641

[ 1646](can__mcan_8h.md#abcbc1ab4765005ec8acfd15921b065fd)int [can\_mcan\_start](can__mcan_8h.md#abcbc1ab4765005ec8acfd15921b065fd)(const struct [device](structdevice.md) \*dev);

1647

[ 1652](can__mcan_8h.md#a47d2f53639584c8fb4d65995e98ad77f)int [can\_mcan\_stop](can__mcan_8h.md#a47d2f53639584c8fb4d65995e98ad77f)(const struct [device](structdevice.md) \*dev);

1653

[ 1658](can__mcan_8h.md#a1264c5d49f0eeee5e3656560e7b2fb65)int [can\_mcan\_set\_mode](can__mcan_8h.md#a1264c5d49f0eeee5e3656560e7b2fb65)(const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode);

1659

[ 1664](can__mcan_8h.md#a33156b2282136192117cb663a4e64ea3)int [can\_mcan\_set\_timing](can__mcan_8h.md#a33156b2282136192117cb663a4e64ea3)(const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing);

1665

[ 1670](can__mcan_8h.md#a1fd00ba6a4023631c8589763049e05e9)int [can\_mcan\_set\_timing\_data](can__mcan_8h.md#a1fd00ba6a4023631c8589763049e05e9)(const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing\_data);

1671

1672#ifndef CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY

[ 1677](can__mcan_8h.md#a8444e4415e377c6ab0756c80943e5b4b)int [can\_mcan\_recover](can__mcan_8h.md#a8444e4415e377c6ab0756c80943e5b4b)(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout);

1678#endif /\* !CONFIG\_CAN\_AUTO\_BUS\_OFF\_RECOVERY \*/

1679

[ 1680](can__mcan_8h.md#a906568f3922bf3cf39eb9ac9e78d58ae)int [can\_mcan\_send](can__mcan_8h.md#a906568f3922bf3cf39eb9ac9e78d58ae)(const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame, [k\_timeout\_t](structk__timeout__t.md) timeout,

1681 [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback, void \*user\_data);

1682

[ 1683](can__mcan_8h.md#ac627d35c23322c003fa846866cfb6419)int [can\_mcan\_get\_max\_filters](can__mcan_8h.md#ac627d35c23322c003fa846866cfb6419)(const struct [device](structdevice.md) \*dev, bool ide);

1684

[ 1689](can__mcan_8h.md#a6a215a77fada5caafd7fb0da72308d95)int [can\_mcan\_add\_rx\_filter](can__mcan_8h.md#a6a215a77fada5caafd7fb0da72308d95)(const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback, void \*user\_data,

1690 const struct [can\_filter](structcan__filter.md) \*filter);

1691

[ 1696](can__mcan_8h.md#ae1a44958756509d882d6202cc337197e)void [can\_mcan\_remove\_rx\_filter](can__mcan_8h.md#ae1a44958756509d882d6202cc337197e)(const struct [device](structdevice.md) \*dev, int filter\_id);

1697

[ 1702](can__mcan_8h.md#a40e0f8f7ec696c62dd132fed45a4da5d)int [can\_mcan\_get\_state](can__mcan_8h.md#a40e0f8f7ec696c62dd132fed45a4da5d)(const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90),

1703 struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt);

1704

[ 1709](can__mcan_8h.md#a324735380014b09f4e1fb33ff0c539cd)void [can\_mcan\_set\_state\_change\_callback](can__mcan_8h.md#a324735380014b09f4e1fb33ff0c539cd)(const struct [device](structdevice.md) \*dev,

1710 [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback, void \*user\_data);

1711

1712#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CAN\_CAN\_MCAN\_H\_ \*/

[cache.h](cache_8h.md)

cache API interface

[can\_mcan\_line\_0\_isr](can__mcan_8h.md#a004d1a9aabc5307e6ab51a477f33c070)

void can\_mcan\_line\_0\_isr(const struct device \*dev)

Bosch M\_CAN driver m\_can\_int0 IRQ handler.

[can\_mcan\_read\_reg](can__mcan_8h.md#a05e01d009f6cb08f7e8497c9e2ee83ef)

int can\_mcan\_read\_reg(const struct device \*dev, uint16\_t reg, uint32\_t \*val)

Read a Bosch M\_CAN register.

[can\_mcan\_set\_mode](can__mcan_8h.md#a1264c5d49f0eeee5e3656560e7b2fb65)

int can\_mcan\_set\_mode(const struct device \*dev, can\_mode\_t mode)

Bosch M\_CAN driver callback API upon setting CAN controller mode See can\_set\_mode() for argument desc...

[can\_mcan\_read\_mram](can__mcan_8h.md#a1705a740e811f1065538c733498fc16f)

static int can\_mcan\_read\_mram(const struct device \*dev, uint16\_t offset, void \*dst, size\_t len)

Read from Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:1536

[can\_mcan\_set\_timing\_data](can__mcan_8h.md#a1fd00ba6a4023631c8589763049e05e9)

int can\_mcan\_set\_timing\_data(const struct device \*dev, const struct can\_timing \*timing\_data)

Bosch M\_CAN driver callback API upon setting CAN bus data phase timing See can\_set\_timing\_data() for ...

[can\_mcan\_sys\_read\_reg](can__mcan_8h.md#a2138e6f7c669bf8a1c1f04637ec9752c)

static int can\_mcan\_sys\_read\_reg(mm\_reg\_t base, uint16\_t reg, uint32\_t \*val)

Bosch M\_CAN driver front-end callback helper for reading a memory mapped register.

**Definition** can\_mcan.h:1365

[can\_mcan\_sys\_write\_mram](can__mcan_8h.md#a21e0977205bb9db1be83968fda99bf95)

static int can\_mcan\_sys\_write\_mram(mem\_addr\_t base, uint16\_t offset, const void \*src, size\_t len)

Bosch M\_CAN driver front-end callback helper for writing to memory mapped Message RAM.

**Definition** can\_mcan.h:1441

[can\_mcan\_configure\_mram](can__mcan_8h.md#a2f9186fc69fe80b76133ab0f82100fc8)

int can\_mcan\_configure\_mram(const struct device \*dev, uintptr\_t mrba, uintptr\_t mram)

Configure Bosch M\_MCAN Message RAM start addresses.

[can\_mcan\_clear\_mram\_t](can__mcan_8h.md#a321813b4b3def118480a7a9eccb6d4aa)

int(\* can\_mcan\_clear\_mram\_t)(const struct device \*dev, uint16\_t offset, size\_t len)

Bosch M\_CAN driver front-end callback for clearing Message RAM.

**Definition** can\_mcan.h:1140

[can\_mcan\_set\_state\_change\_callback](can__mcan_8h.md#a324735380014b09f4e1fb33ff0c539cd)

void can\_mcan\_set\_state\_change\_callback(const struct device \*dev, can\_state\_change\_callback\_t callback, void \*user\_data)

Bosch M\_CAN driver callback API upon setting a state change callback See can\_set\_state\_change\_callbac...

[can\_mcan\_set\_timing](can__mcan_8h.md#a33156b2282136192117cb663a4e64ea3)

int can\_mcan\_set\_timing(const struct device \*dev, const struct can\_timing \*timing)

Bosch M\_CAN driver callback API upon setting CAN bus timing See can\_set\_timing() for argument descrip...

[can\_mcan\_write\_reg](can__mcan_8h.md#a3f3e4be50fbf2c7ffcba99a1ca5ca7e1)

int can\_mcan\_write\_reg(const struct device \*dev, uint16\_t reg, uint32\_t val)

Write a Bosch M\_CAN register.

[can\_mcan\_get\_state](can__mcan_8h.md#a40e0f8f7ec696c62dd132fed45a4da5d)

int can\_mcan\_get\_state(const struct device \*dev, enum can\_state \*state, struct can\_bus\_err\_cnt \*err\_cnt)

Bosch M\_CAN driver callback API upon getting the CAN controller state See can\_get\_state() for argumen...

[can\_mcan\_line\_1\_isr](can__mcan_8h.md#a41e134fc94a573622eac9314f87dd673)

void can\_mcan\_line\_1\_isr(const struct device \*dev)

Bosch M\_CAN driver m\_can\_int1 IRQ handler.

[can\_mcan\_stop](can__mcan_8h.md#a47d2f53639584c8fb4d65995e98ad77f)

int can\_mcan\_stop(const struct device \*dev)

Bosch M\_CAN driver callback API upon stopping CAN controller See can\_stop() for argument description.

[can\_mcan\_enable\_configuration\_change](can__mcan_8h.md#a54f0e66b1b1912d841e10e68e01331fa)

void can\_mcan\_enable\_configuration\_change(const struct device \*dev)

Enable Bosch M\_CAN configuration change.

[can\_mcan\_sys\_read\_mram](can__mcan_8h.md#a5d7d5e0bb88b661462fa01720d824610)

static int can\_mcan\_sys\_read\_mram(mem\_addr\_t base, uint16\_t offset, void \*dst, size\_t len)

Bosch M\_CAN driver front-end callback helper for reading from memory mapped Message RAM.

**Definition** can\_mcan.h:1401

[can\_mcan\_sys\_clear\_mram](can__mcan_8h.md#a65c59db492d1c3359d032b5f8a62af8b)

static int can\_mcan\_sys\_clear\_mram(mem\_addr\_t base, uint16\_t offset, size\_t len)

Bosch M\_CAN driver front-end callback helper for clearing memory mapped Message RAM.

**Definition** can\_mcan.h:1478

[can\_mcan\_add\_rx\_filter](can__mcan_8h.md#a6a215a77fada5caafd7fb0da72308d95)

int can\_mcan\_add\_rx\_filter(const struct device \*dev, can\_rx\_callback\_t callback, void \*user\_data, const struct can\_filter \*filter)

Bosch M\_CAN driver callback API upon adding an RX filter See can\_add\_rx\_callback() for argument descr...

[can\_mcan\_read\_reg\_t](can__mcan_8h.md#a79941b7745919bb1bf7d7219555440a6)

int(\* can\_mcan\_read\_reg\_t)(const struct device \*dev, uint16\_t reg, uint32\_t \*val)

Bosch M\_CAN driver front-end callback for reading a register value.

**Definition** can\_mcan.h:1082

[can\_mcan\_init](can__mcan_8h.md#a7d9006cb2e91f6b13c3d245612b175f0)

int can\_mcan\_init(const struct device \*dev)

Bosch M\_CAN driver initialization callback.

[can\_mcan\_recover](can__mcan_8h.md#a8444e4415e377c6ab0756c80943e5b4b)

int can\_mcan\_recover(const struct device \*dev, k\_timeout\_t timeout)

Bosch M\_CAN driver callback API upon recovering the CAN bus See can\_recover() for argument descriptio...

[can\_mcan\_psr\_lec](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462)

can\_mcan\_psr\_lec

**Definition** can\_mcan.h:130

[CAN\_MCAN\_PSR\_LEC\_STUFF\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a0207d3347a4afc89d17fa6b954ae90d0)

@ CAN\_MCAN\_PSR\_LEC\_STUFF\_ERROR

**Definition** can\_mcan.h:132

[CAN\_MCAN\_PSR\_LEC\_BIT0\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a4bca141d0a3056cbdfc379f49d60c651)

@ CAN\_MCAN\_PSR\_LEC\_BIT0\_ERROR

**Definition** can\_mcan.h:136

[CAN\_MCAN\_PSR\_LEC\_NO\_CHANGE](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a683c68657e49efd306f43be43bd3167e)

@ CAN\_MCAN\_PSR\_LEC\_NO\_CHANGE

**Definition** can\_mcan.h:138

[CAN\_MCAN\_PSR\_LEC\_CRC\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a7a19af0809a0613a8becb016781b03dc)

@ CAN\_MCAN\_PSR\_LEC\_CRC\_ERROR

**Definition** can\_mcan.h:137

[CAN\_MCAN\_PSR\_LEC\_BIT1\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a7de1a2f2ced1a52f01ee4d9f2b9b6b80)

@ CAN\_MCAN\_PSR\_LEC\_BIT1\_ERROR

**Definition** can\_mcan.h:135

[CAN\_MCAN\_PSR\_LEC\_ACK\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462a9e5414792478db5f57f1f270d0ceac13)

@ CAN\_MCAN\_PSR\_LEC\_ACK\_ERROR

**Definition** can\_mcan.h:134

[CAN\_MCAN\_PSR\_LEC\_FORM\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462ac4bce840b2edcf97957d74e6debe9b03)

@ CAN\_MCAN\_PSR\_LEC\_FORM\_ERROR

**Definition** can\_mcan.h:133

[CAN\_MCAN\_PSR\_LEC\_NO\_ERROR](can__mcan_8h.md#a888671da33c3ffc35ce94c8eba13d462acab41a3d432b309d9b73a711d84b39e9)

@ CAN\_MCAN\_PSR\_LEC\_NO\_ERROR

**Definition** can\_mcan.h:131

[can\_mcan\_send](can__mcan_8h.md#a906568f3922bf3cf39eb9ac9e78d58ae)

int can\_mcan\_send(const struct device \*dev, const struct can\_frame \*frame, k\_timeout\_t timeout, can\_tx\_callback\_t callback, void \*user\_data)

[can\_mcan\_read\_mram\_t](can__mcan_8h.md#a9532f0655c579f0ab091f85771b5d62d)

int(\* can\_mcan\_read\_mram\_t)(const struct device \*dev, uint16\_t offset, void \*dst, size\_t len)

Bosch M\_CAN driver front-end callback for reading from Message RAM.

**Definition** can\_mcan.h:1109

[can\_mcan\_clear\_mram](can__mcan_8h.md#aa330897ffad0a9e1b4f08aaaa22e5c70)

static int can\_mcan\_clear\_mram(const struct device \*dev, uint16\_t offset, size\_t len)

Clear Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:1577

[can\_mcan\_write\_mram\_t](can__mcan_8h.md#aaf2920e649f9671f09856a062ac4dc95)

int(\* can\_mcan\_write\_mram\_t)(const struct device \*dev, uint16\_t offset, const void \*src, size\_t len)

Bosch M\_CAN driver front-end callback for writing to Message RAM.

**Definition** can\_mcan.h:1124

[CAN\_MCAN\_MRAM\_CFG\_NUM\_CELLS](can__mcan_8h.md#abb4087b9c7ac31e8a1cb7003945dad97)

#define CAN\_MCAN\_MRAM\_CFG\_NUM\_CELLS

Total number of cells in bosch,mram-cfg property.

**Definition** can\_mcan.h:423

[can\_mcan\_get\_capabilities](can__mcan_8h.md#abc9c13ee4f4b47d4ff74ab4c6352bbe1)

int can\_mcan\_get\_capabilities(const struct device \*dev, can\_mode\_t \*cap)

Bosch M\_CAN driver callback API upon getting CAN controller capabilities See can\_get\_capabilities() f...

[can\_mcan\_start](can__mcan_8h.md#abcbc1ab4765005ec8acfd15921b065fd)

int can\_mcan\_start(const struct device \*dev)

Bosch M\_CAN driver callback API upon starting CAN controller See can\_start() for argument description...

[can\_mcan\_sys\_write\_reg](can__mcan_8h.md#ac1562291a74cc1f5b5e6d82fe31141bb)

static int can\_mcan\_sys\_write\_reg(mm\_reg\_t base, uint16\_t reg, uint32\_t val)

Bosch M\_CAN driver front-end callback helper for writing a memory mapped register.

**Definition** can\_mcan.h:1381

[can\_mcan\_get\_max\_filters](can__mcan_8h.md#ac627d35c23322c003fa846866cfb6419)

int can\_mcan\_get\_max\_filters(const struct device \*dev, bool ide)

[can\_mcan\_write\_reg\_t](can__mcan_8h.md#acbb72b712e516fe923e6030a9d6b36c1)

int(\* can\_mcan\_write\_reg\_t)(const struct device \*dev, uint16\_t reg, uint32\_t val)

Bosch M\_CAN driver front-end callback for writing a register value.

**Definition** can\_mcan.h:1095

[can\_mcan\_write\_mram](can__mcan_8h.md#ad2b88658a2294af890c56a99fee4a999)

static int can\_mcan\_write\_mram(const struct device \*dev, uint16\_t offset, const void \*src, size\_t len)

Write to Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:1556

[can\_mcan\_remove\_rx\_filter](can__mcan_8h.md#ae1a44958756509d882d6202cc337197e)

void can\_mcan\_remove\_rx\_filter(const struct device \*dev, int filter\_id)

Bosch M\_CAN driver callback API upon removing an RX filter See can\_remove\_rx\_filter() for argument de...

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[can.h](drivers_2can_8h.md)

Controller Area Network (CAN) driver API.

[sys\_cache\_data\_invd\_range](group__cache__interface.md#ga578f2f926cbf5ad196765881c8c1265e)

int sys\_cache\_data\_invd\_range(void \*addr, size\_t size)

Invalidate an address range in the d-cache.

[sys\_cache\_data\_flush\_range](group__cache__interface.md#ga6b61424f0aa81e2893c915b096de0cdb)

int sys\_cache\_data\_flush\_range(void \*addr, size\_t size)

Flush an address range in the d-cache.

[can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)

void(\* can\_state\_change\_callback\_t)(const struct device \*dev, enum can\_state state, struct can\_bus\_err\_cnt err\_cnt, void \*user\_data)

Defines the state change callback handler function signature.

**Definition** can.h:309

[can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7)

uint32\_t can\_mode\_t

Provides a type to hold CAN controller configuration flags.

**Definition** can.h:116

[can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)

void(\* can\_rx\_callback\_t)(const struct device \*dev, struct can\_frame \*frame, void \*user\_data)

Defines the application callback handler function signature for receiving.

**Definition** can.h:298

[can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)

void(\* can\_tx\_callback\_t)(const struct device \*dev, int error, void \*user\_data)

Defines the application callback handler function signature.

**Definition** can.h:289

[can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7)

can\_state

Defines the state of the CAN controller.

**Definition** can.h:121

[POINTER\_TO\_UINT](group__sys-util.md#gae4ed3d05bcfbe9c8f4a5d81d8c969f19)

#define POINTER\_TO\_UINT(x)

Cast x, a pointer, to an unsigned integer.

**Definition** util.h:45

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[can\_bus\_err\_cnt](structcan__bus__err__cnt.md)

CAN controller error counters.

**Definition** can.h:229

[can\_filter](structcan__filter.md)

CAN filter structure.

**Definition** can.h:212

[can\_frame](structcan__frame.md)

CAN frame structure.

**Definition** can.h:163

[can\_mcan\_callbacks](structcan__mcan__callbacks.md)

Bosch M\_CAN driver internal Tx + Rx callbacks structure.

**Definition** can\_mcan.h:1172

[can\_mcan\_callbacks::num\_std](structcan__mcan__callbacks.md#a0388e27fc1852d7e7c7ac6f062cab3e1)

uint8\_t num\_std

**Definition** can\_mcan.h:1177

[can\_mcan\_callbacks::num\_ext](structcan__mcan__callbacks.md#a9edfccadf0ef4006ac5eb7926772ca85)

uint8\_t num\_ext

**Definition** can\_mcan.h:1178

[can\_mcan\_callbacks::num\_tx](structcan__mcan__callbacks.md#aad1b8f0b76637e7a53ef5c88118d7bd1)

uint8\_t num\_tx

**Definition** can\_mcan.h:1176

[can\_mcan\_callbacks::ext](structcan__mcan__callbacks.md#ab29bb0963a78fcc68677ff5e4589f004)

struct can\_mcan\_rx\_callback \* ext

**Definition** can\_mcan.h:1175

[can\_mcan\_callbacks::tx](structcan__mcan__callbacks.md#ad2ee7f63634cc67160f4eb75f05babd2)

struct can\_mcan\_tx\_callback \* tx

**Definition** can\_mcan.h:1173

[can\_mcan\_callbacks::std](structcan__mcan__callbacks.md#ae225638097e1ddb5270de06401490a7f)

struct can\_mcan\_rx\_callback \* std

**Definition** can\_mcan.h:1174

[can\_mcan\_config](structcan__mcan__config.md)

Bosch M\_CAN driver internal configuration structure.

**Definition** can\_mcan.h:1233

[can\_mcan\_config::callbacks](structcan__mcan__config.md#a0c8500180fb8113e7bc36d446e4c39bb)

const struct can\_mcan\_callbacks \* callbacks

**Definition** can\_mcan.h:1236

[can\_mcan\_config::ts2](structcan__mcan__config.md#a0e7f2499e657f71d7a05e0a5bb870eef)

uint16\_t ts2

**Definition** can\_mcan.h:1242

[can\_mcan\_config::mram\_size](structcan__mcan__config.md#a10585712cd11d041829dca9c9c5446e1)

size\_t mram\_size

**Definition** can\_mcan.h:1239

[can\_mcan\_config::prop\_ts1](structcan__mcan__config.md#a1800aadb04f6b670cb9d1fefed11c4f8)

uint16\_t prop\_ts1

**Definition** can\_mcan.h:1241

[can\_mcan\_config::mram\_offsets](structcan__mcan__config.md#a412c0bb0b3d8158cd352d4c24a622401)

uint16\_t mram\_offsets[8]

**Definition** can\_mcan.h:1238

[can\_mcan\_config::custom](structcan__mcan__config.md#a7b2d696b6839a8f958f705fb13a0f63d)

const void \* custom

**Definition** can\_mcan.h:1249

[can\_mcan\_config::common](structcan__mcan__config.md#a86a6f9a19db54c7368f16f72513db327)

const struct can\_driver\_config common

**Definition** can\_mcan.h:1234

[can\_mcan\_config::sjw](structcan__mcan__config.md#a99df753a7f1c7e135b3d69b1c376608b)

uint16\_t sjw

**Definition** can\_mcan.h:1240

[can\_mcan\_config::mram\_elements](structcan__mcan__config.md#ab196bf74bf41fba65c0d076ff9070202)

uint16\_t mram\_elements[8]

**Definition** can\_mcan.h:1237

[can\_mcan\_config::ops](structcan__mcan__config.md#aed10f9a4d2ddc0045bc6f37939973039)

const struct can\_mcan\_ops \* ops

**Definition** can\_mcan.h:1235

[can\_mcan\_data](structcan__mcan__data.md)

Bosch M\_CAN driver internal data structure.

**Definition** can\_mcan.h:1063

[can\_mcan\_data::lock](structcan__mcan__data.md#a27048362bd5d4288e3ea9018ccc210f6)

struct k\_mutex lock

**Definition** can\_mcan.h:1065

[can\_mcan\_data::custom](structcan__mcan__data.md#a4211c8dce9704c43790ac354d124c3ab)

void \* custom

**Definition** can\_mcan.h:1068

[can\_mcan\_data::common](structcan__mcan__data.md#a486500387e6351f68d741f089d57f913)

struct can\_driver\_data common

**Definition** can\_mcan.h:1064

[can\_mcan\_data::tx\_mtx](structcan__mcan__data.md#a535ad3150d0c64f11b4dd4e3010d4718)

struct k\_mutex tx\_mtx

**Definition** can\_mcan.h:1067

[can\_mcan\_data::tx\_sem](structcan__mcan__data.md#a5e0239c7ff45045d4f4ca5c83a41c4dd)

struct k\_sem tx\_sem

**Definition** can\_mcan.h:1066

[can\_mcan\_ext\_filter](structcan__mcan__ext__filter.md)

Bosch M\_CAN Extended Message ID Filter Element.

**Definition** can\_mcan.h:1052

[can\_mcan\_ext\_filter::efid2](structcan__mcan__ext__filter.md#a12147937f9889e835cf89f5a99ab62d8)

uint32\_t efid2

**Definition** can\_mcan.h:1055

[can\_mcan\_ext\_filter::esync](structcan__mcan__ext__filter.md#a2e2c2d57015bf7aabbbe510660430bd7)

uint32\_t esync

**Definition** can\_mcan.h:1056

[can\_mcan\_ext\_filter::efid1](structcan__mcan__ext__filter.md#a54b3ac39e57cb02136a5d1bf5af1c75b)

uint32\_t efid1

**Definition** can\_mcan.h:1053

[can\_mcan\_ext\_filter::efec](structcan__mcan__ext__filter.md#a6a3042f7b236fb2d06334c4c5bc91530)

uint32\_t efec

**Definition** can\_mcan.h:1054

[can\_mcan\_ext\_filter::eft](structcan__mcan__ext__filter.md#aa94145f8e7f7d8668f383f174f6420b8)

uint32\_t eft

**Definition** can\_mcan.h:1057

[can\_mcan\_ops](structcan__mcan__ops.md)

Bosch M\_CAN driver front-end operations.

**Definition** can\_mcan.h:1145

[can\_mcan\_ops::read\_reg](structcan__mcan__ops.md#a0c9986b8fda47f3cc08128e2f951d1fb)

can\_mcan\_read\_reg\_t read\_reg

**Definition** can\_mcan.h:1146

[can\_mcan\_ops::write\_reg](structcan__mcan__ops.md#a2d977bb8a98e6f2f787723eb9104f949)

can\_mcan\_write\_reg\_t write\_reg

**Definition** can\_mcan.h:1147

[can\_mcan\_ops::write\_mram](structcan__mcan__ops.md#ab040466ab26383567dac85c08b077250)

can\_mcan\_write\_mram\_t write\_mram

**Definition** can\_mcan.h:1149

[can\_mcan\_ops::clear\_mram](structcan__mcan__ops.md#abde9d0a2aeece4545d7fa42f3cac3aad)

can\_mcan\_clear\_mram\_t clear\_mram

**Definition** can\_mcan.h:1150

[can\_mcan\_ops::read\_mram](structcan__mcan__ops.md#ac0f1adfa81042116f5da861c557562b2)

can\_mcan\_read\_mram\_t read\_mram

**Definition** can\_mcan.h:1148

[can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md)

Bosch M\_CAN driver internal Rx callback structure.

**Definition** can\_mcan.h:1164

[can\_mcan\_rx\_callback::user\_data](structcan__mcan__rx__callback.md#ab6196a8d1f7a067c872d4d0fe7d7d00b)

void \* user\_data

**Definition** can\_mcan.h:1166

[can\_mcan\_rx\_callback::function](structcan__mcan__rx__callback.md#adc5ed2295bf18e2c5e4c806e1f488668)

can\_rx\_callback\_t function

**Definition** can\_mcan.h:1165

[can\_mcan\_rx\_fifo\_hdr](structcan__mcan__rx__fifo__hdr.md)

Bosch M\_CAN Rx Buffer and FIFO Element header.

**Definition** can\_mcan.h:909

[can\_mcan\_rx\_fifo\_hdr::pad2](structcan__mcan__rx__fifo__hdr.md#a03a015b8195efeda0287b1323de54b3c)

uint32\_t pad2

**Definition** can\_mcan.h:920

[can\_mcan\_rx\_fifo\_hdr::res](structcan__mcan__rx__fifo__hdr.md#a0f95cfa20e9a9e1c75da3afb1dd4542f)

uint32\_t res

**Definition** can\_mcan.h:927

[can\_mcan\_rx\_fifo\_hdr::brs](structcan__mcan__rx__fifo__hdr.md#a35d6a09669761d4b7d60c06e36f74e06)

uint32\_t brs

**Definition** can\_mcan.h:925

[can\_mcan\_rx\_fifo\_hdr::dlc](structcan__mcan__rx__fifo__hdr.md#a44564c3ab98be8cd92b6f17c9379d045)

uint32\_t dlc

**Definition** can\_mcan.h:924

[can\_mcan\_rx\_fifo\_hdr::anmf](structcan__mcan__rx__fifo__hdr.md#a6256e635694330dc3428f30387838f96)

uint32\_t anmf

**Definition** can\_mcan.h:929

[can\_mcan\_rx\_fifo\_hdr::esi](structcan__mcan__rx__fifo__hdr.md#a746f7f80e30ac574fcb785e78cbcdf44)

uint32\_t esi

**Definition** can\_mcan.h:915

[can\_mcan\_rx\_fifo\_hdr::fdf](structcan__mcan__rx__fifo__hdr.md#a8beb206b8c5ef1dd7c25d17ef5045d55)

uint32\_t fdf

**Definition** can\_mcan.h:926

[can\_mcan\_rx\_fifo\_hdr::rtr](structcan__mcan__rx__fifo__hdr.md#aa315257f7f5dcb438ba70c22ced8b9fe)

uint32\_t rtr

**Definition** can\_mcan.h:913

[can\_mcan\_rx\_fifo\_hdr::xtd](structcan__mcan__rx__fifo__hdr.md#ab75c330ef4724997f665a84c99ab2c57)

uint32\_t xtd

**Definition** can\_mcan.h:914

[can\_mcan\_rx\_fifo\_hdr::std\_id](structcan__mcan__rx__fifo__hdr.md#ac97eacf0d6cf2ef9ae6454b7604b52b5)

uint32\_t std\_id

**Definition** can\_mcan.h:919

[can\_mcan\_rx\_fifo\_hdr::ext\_id](structcan__mcan__rx__fifo__hdr.md#acdea19720ee1d76254b6e9931ffeca07)

uint32\_t ext\_id

**Definition** can\_mcan.h:912

[can\_mcan\_rx\_fifo\_hdr::rxts](structcan__mcan__rx__fifo__hdr.md#ace6229b7580d1954638d1469700f5ebd)

uint32\_t rxts

**Definition** can\_mcan.h:923

[can\_mcan\_rx\_fifo\_hdr::fidx](structcan__mcan__rx__fifo__hdr.md#ad6bcb3637d79f4e87371dd91fb7a5881)

uint32\_t fidx

**Definition** can\_mcan.h:928

[can\_mcan\_rx\_fifo\_hdr::pad1](structcan__mcan__rx__fifo__hdr.md#afbdea1a9674af705a4954709e64ed45a)

uint32\_t pad1

**Definition** can\_mcan.h:918

[can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md)

Bosch M\_CAN Rx Buffer and FIFO Element.

**Definition** can\_mcan.h:937

[can\_mcan\_rx\_fifo::hdr](structcan__mcan__rx__fifo.md#a8ddf6a5aa6f9847c3b5c0fce66631133)

struct can\_mcan\_rx\_fifo\_hdr hdr

**Definition** can\_mcan.h:938

[can\_mcan\_rx\_fifo::data\_32](structcan__mcan__rx__fifo.md#a9a5e7e970f2733b68894edcbaf98cc82)

uint32\_t data\_32[16]

**Definition** can\_mcan.h:941

[can\_mcan\_rx\_fifo::data](structcan__mcan__rx__fifo.md#aeafd55c4d4f637c66e5a57d329e42a2b)

uint8\_t data[64]

**Definition** can\_mcan.h:940

[can\_mcan\_std\_filter](structcan__mcan__std__filter.md)

Bosch M\_CAN Standard Message ID Filter Element.

**Definition** can\_mcan.h:1033

[can\_mcan\_std\_filter::sfid2](structcan__mcan__std__filter.md#a050f5018825d3afa350b35d101569f50)

uint32\_t sfid2

**Definition** can\_mcan.h:1034

[can\_mcan\_std\_filter::sfid1](structcan__mcan__std__filter.md#a7d80d641985ab67e09eb4d11015af2b3)

uint32\_t sfid1

**Definition** can\_mcan.h:1036

[can\_mcan\_std\_filter::sfec](structcan__mcan__std__filter.md#ad943ff357a00cca569f164599b9f49e5)

uint32\_t sfec

**Definition** can\_mcan.h:1037

[can\_mcan\_std\_filter::res](structcan__mcan__std__filter.md#adb5bb096566c3fecf9727a800dbfe3cd)

uint32\_t res

**Definition** can\_mcan.h:1035

[can\_mcan\_std\_filter::sft](structcan__mcan__std__filter.md#afb89a40ac7c585c75d6bbaf3705e913a)

uint32\_t sft

**Definition** can\_mcan.h:1038

[can\_mcan\_tx\_buffer\_hdr](structcan__mcan__tx__buffer__hdr.md)

Bosch M\_CAN Tx Buffer Element header.

**Definition** can\_mcan.h:950

[can\_mcan\_tx\_buffer\_hdr::tsce](structcan__mcan__tx__buffer__hdr.md#a053c1a8d986dd4537398c052712d394d)

uint8\_t tsce

**Definition** can\_mcan.h:968

[can\_mcan\_tx\_buffer\_hdr::xtd](structcan__mcan__tx__buffer__hdr.md#a0ee2e857b6f63c2d70179d89398ffb9a)

uint32\_t xtd

**Definition** can\_mcan.h:955

[can\_mcan\_tx\_buffer\_hdr::res1](structcan__mcan__tx__buffer__hdr.md#a4bd206867f0ba937b93888285ea4095a)

uint16\_t res1

**Definition** can\_mcan.h:964

[can\_mcan\_tx\_buffer\_hdr::rtr](structcan__mcan__tx__buffer__hdr.md#a6ef37c0a073550c2b99ec29fdb834ca1)

uint32\_t rtr

**Definition** can\_mcan.h:954

[can\_mcan\_tx\_buffer\_hdr::efc](structcan__mcan__tx__buffer__hdr.md#a6f760970f0483dc16aa8ecc0715591d3)

uint8\_t efc

**Definition** can\_mcan.h:969

[can\_mcan\_tx\_buffer\_hdr::fdf](structcan__mcan__tx__buffer__hdr.md#a7ac73d1c09b84267a4701b5d4fa7c920)

uint8\_t fdf

**Definition** can\_mcan.h:967

[can\_mcan\_tx\_buffer\_hdr::std\_id](structcan__mcan__tx__buffer__hdr.md#a9b1f4f0f66d1de07cf6ed212baa713be)

uint32\_t std\_id

**Definition** can\_mcan.h:960

[can\_mcan\_tx\_buffer\_hdr::dlc](structcan__mcan__tx__buffer__hdr.md#a9b96b8b75d4ff4c9df3192a244dabc82)

uint8\_t dlc

**Definition** can\_mcan.h:965

[can\_mcan\_tx\_buffer\_hdr::pad2](structcan__mcan__tx__buffer__hdr.md#aa43b5da1708dbf49794c586ca3af7365)

uint32\_t pad2

**Definition** can\_mcan.h:961

[can\_mcan\_tx\_buffer\_hdr::ext\_id](structcan__mcan__tx__buffer__hdr.md#ab4800365c1f2cd76c2e19c27b8d72956)

uint32\_t ext\_id

**Definition** can\_mcan.h:953

[can\_mcan\_tx\_buffer\_hdr::mm](structcan__mcan__tx__buffer__hdr.md#ac76ce5728912347d0193c4ed5f467c92)

uint8\_t mm

**Definition** can\_mcan.h:970

[can\_mcan\_tx\_buffer\_hdr::pad1](structcan__mcan__tx__buffer__hdr.md#ac78c3e0f4dda2eddc25ae8066cc29134)

uint32\_t pad1

**Definition** can\_mcan.h:959

[can\_mcan\_tx\_buffer\_hdr::esi](structcan__mcan__tx__buffer__hdr.md#ae30ffd52da3ea38188fa04ace20054ad)

uint32\_t esi

**Definition** can\_mcan.h:956

[can\_mcan\_tx\_buffer\_hdr::brs](structcan__mcan__tx__buffer__hdr.md#af6554e36649326a1ee01757096e1c68f)

uint8\_t brs

**Definition** can\_mcan.h:966

[can\_mcan\_tx\_buffer](structcan__mcan__tx__buffer.md)

Bosch M\_CAN Tx Buffer Element.

**Definition** can\_mcan.h:978

[can\_mcan\_tx\_buffer::data\_32](structcan__mcan__tx__buffer.md#a4b1a8963e8da21c01843f20e9e01bb11)

uint32\_t data\_32[16]

**Definition** can\_mcan.h:982

[can\_mcan\_tx\_buffer::hdr](structcan__mcan__tx__buffer.md#a5b553813e69bf22565d2894e8137672d)

struct can\_mcan\_tx\_buffer\_hdr hdr

**Definition** can\_mcan.h:979

[can\_mcan\_tx\_buffer::data](structcan__mcan__tx__buffer.md#af69274236867987f069aa6dd29182f82)

uint8\_t data[64]

**Definition** can\_mcan.h:981

[can\_mcan\_tx\_callback](structcan__mcan__tx__callback.md)

Bosch M\_CAN driver internal Tx callback structure.

**Definition** can\_mcan.h:1156

[can\_mcan\_tx\_callback::user\_data](structcan__mcan__tx__callback.md#a0af42dc41c9a7d4d0fe245ef78b857ad)

void \* user\_data

**Definition** can\_mcan.h:1158

[can\_mcan\_tx\_callback::function](structcan__mcan__tx__callback.md#affda660bd76b14694f8f59d58c5f49f8)

can\_tx\_callback\_t function

**Definition** can\_mcan.h:1157

[can\_mcan\_tx\_event\_fifo](structcan__mcan__tx__event__fifo.md)

Bosch M\_CAN Tx Event FIFO Element.

**Definition** can\_mcan.h:991

[can\_mcan\_tx\_event\_fifo::rtr](structcan__mcan__tx__event__fifo.md#a17d5b6caf6519bf199dc179c11550abb)

uint32\_t rtr

**Definition** can\_mcan.h:995

[can\_mcan\_tx\_event\_fifo::et](structcan__mcan__tx__event__fifo.md#a23ff309d6fb887166da2290646df200c)

uint8\_t et

**Definition** can\_mcan.h:1009

[can\_mcan\_tx\_event\_fifo::ext\_id](structcan__mcan__tx__event__fifo.md#a3b4c61b9edcd1720235c3784131693d1)

uint32\_t ext\_id

**Definition** can\_mcan.h:994

[can\_mcan\_tx\_event\_fifo::fdf](structcan__mcan__tx__event__fifo.md#a4075852d322da2eb4e3acb9d7c2e6d64)

uint8\_t fdf

**Definition** can\_mcan.h:1008

[can\_mcan\_tx\_event\_fifo::pad2](structcan__mcan__tx__event__fifo.md#a461d68069593b42d6961d6ff0525f783)

uint32\_t pad2

**Definition** can\_mcan.h:1002

[can\_mcan\_tx\_event\_fifo::mm](structcan__mcan__tx__event__fifo.md#a4a706b7da7d9354ffc559ec65e1701ca)

uint8\_t mm

**Definition** can\_mcan.h:1010

[can\_mcan\_tx\_event\_fifo::pad1](structcan__mcan__tx__event__fifo.md#a6be85a808788bd611055235b00a9b1f4)

uint32\_t pad1

**Definition** can\_mcan.h:1000

[can\_mcan\_tx\_event\_fifo::std\_id](structcan__mcan__tx__event__fifo.md#a7698679cf93c707b423e9c695209f072)

uint32\_t std\_id

**Definition** can\_mcan.h:1001

[can\_mcan\_tx\_event\_fifo::esi](structcan__mcan__tx__event__fifo.md#a796967d04c60cd9cf423d904c6118944)

uint32\_t esi

**Definition** can\_mcan.h:997

[can\_mcan\_tx\_event\_fifo::dlc](structcan__mcan__tx__event__fifo.md#a96aa98b30f603a5c5676e6a244f5d6c9)

uint8\_t dlc

**Definition** can\_mcan.h:1006

[can\_mcan\_tx\_event\_fifo::xtd](structcan__mcan__tx__event__fifo.md#aac19c259f3e966d771c0088a32cbe47d)

uint32\_t xtd

**Definition** can\_mcan.h:996

[can\_mcan\_tx\_event\_fifo::txts](structcan__mcan__tx__event__fifo.md#aacc10d577c20325baf54d7bb20e32583)

uint16\_t txts

**Definition** can\_mcan.h:1005

[can\_mcan\_tx\_event\_fifo::brs](structcan__mcan__tx__event__fifo.md#ac3924771aeb8885b4ad8d59758131b1a)

uint8\_t brs

**Definition** can\_mcan.h:1007

[can\_timing](structcan__timing.md)

CAN bus timing structure.

**Definition** can.h:268

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:391

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[sys\_write32](sys-io-common_8h.md#a2d04bb22b0aacb66c62b040ca36cb03f)

static ALWAYS\_INLINE void sys\_write32(uint32\_t data, mem\_addr\_t addr)

**Definition** sys-io-common.h:70

[sys\_read32](sys-io-common_8h.md#a62f6066146f924b75015ae976b27866a)

static ALWAYS\_INLINE uint32\_t sys\_read32(mem\_addr\_t addr)

**Definition** sys-io-common.h:59

[sys\_io.h](sys_2sys__io_8h.md)

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

[mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d)

uintptr\_t mem\_addr\_t

**Definition** sys\_io.h:21

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can](dir_d26220086854d96f67fb3f45a38ba4bc.md)
- [can\_mcan.h](can__mcan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
