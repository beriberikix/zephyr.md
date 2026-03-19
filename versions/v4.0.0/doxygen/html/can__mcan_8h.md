---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/can__mcan_8h.html
original_path: doxygen/html/can__mcan_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_mcan.h File Reference

`#include <[zephyr/cache.h](cache_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/drivers/can.h](drivers_2can_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](can__mcan_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [can\_mcan\_rx\_fifo\_hdr](structcan__mcan__rx__fifo__hdr.md) |
|  | Bosch M\_CAN Rx Buffer and FIFO Element header. [More...](structcan__mcan__rx__fifo__hdr.md#details) |
| struct | [can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md) |
|  | Bosch M\_CAN Rx Buffer and FIFO Element. [More...](structcan__mcan__rx__fifo.md#details) |
| struct | [can\_mcan\_tx\_buffer\_hdr](structcan__mcan__tx__buffer__hdr.md) |
|  | Bosch M\_CAN Tx Buffer Element header. [More...](structcan__mcan__tx__buffer__hdr.md#details) |
| struct | [can\_mcan\_tx\_buffer](structcan__mcan__tx__buffer.md) |
|  | Bosch M\_CAN Tx Buffer Element. [More...](structcan__mcan__tx__buffer.md#details) |
| struct | [can\_mcan\_tx\_event\_fifo](structcan__mcan__tx__event__fifo.md) |
|  | Bosch M\_CAN Tx Event FIFO Element. [More...](structcan__mcan__tx__event__fifo.md#details) |
| struct | [can\_mcan\_std\_filter](structcan__mcan__std__filter.md) |
|  | Bosch M\_CAN Standard Message ID Filter Element. [More...](structcan__mcan__std__filter.md#details) |
| struct | [can\_mcan\_ext\_filter](structcan__mcan__ext__filter.md) |
|  | Bosch M\_CAN Extended Message ID Filter Element. [More...](structcan__mcan__ext__filter.md#details) |
| struct | [can\_mcan\_data](structcan__mcan__data.md) |
|  | Bosch M\_CAN driver internal data structure. [More...](structcan__mcan__data.md#details) |
| struct | [can\_mcan\_ops](structcan__mcan__ops.md) |
|  | Bosch M\_CAN driver front-end operations. [More...](structcan__mcan__ops.md#details) |
| struct | [can\_mcan\_tx\_callback](structcan__mcan__tx__callback.md) |
|  | Bosch M\_CAN driver internal Tx callback structure. [More...](structcan__mcan__tx__callback.md#details) |
| struct | [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md) |
|  | Bosch M\_CAN driver internal Rx callback structure. [More...](structcan__mcan__rx__callback.md#details) |
| struct | [can\_mcan\_callbacks](structcan__mcan__callbacks.md) |
|  | Bosch M\_CAN driver internal Tx + Rx callbacks structure. [More...](structcan__mcan__callbacks.md#details) |
| struct | [can\_mcan\_config](structcan__mcan__config.md) |
|  | Bosch M\_CAN driver internal configuration structure. [More...](structcan__mcan__config.md#details) |

| Macros | |
| --- | --- |
| #define | [CAN\_MCAN\_CREL](#acc741a42cb2d052ae773aebb95e44616)   0x000 |
| #define | [CAN\_MCAN\_CREL\_REL](#a8cedb6b6ed4ace3a38f170fc4ce65647)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 28) |
| #define | [CAN\_MCAN\_CREL\_STEP](#a39282c299129a3a7e902c6a120568bce)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(27, 24) |
| #define | [CAN\_MCAN\_CREL\_SUBSTEP](#ac28c0effa82ad6fefad5dd5c9079800a)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 20) |
| #define | [CAN\_MCAN\_CREL\_YEAR](#a7139e7a57e58fe4f8572c5d7784e67d2)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 16) |
| #define | [CAN\_MCAN\_CREL\_MON](#abc36710e20ac587cacf18e1e74434e6d)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8) |
| #define | [CAN\_MCAN\_CREL\_DAY](#a89eebb76c2b98f12e56eaf3885cae9e5)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| #define | [CAN\_MCAN\_ENDN](#ae130ab74797ec4affc8052a334995dd8)   0x004 |
| #define | [CAN\_MCAN\_ENDN\_ETV](#a1dcceef7aa2e13c90551e677a32f836b)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_CUST](#a60dab0513bb60fdaaeb3ad9eb8589b0b)   0x008 |
| #define | [CAN\_MCAN\_CUST\_CUST](#aa85321c44c2f8ce6f4e3abfecaac4309)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_DBTP](#a3643ab9ba53749dd417515e868005822)   0x00C |
| #define | [CAN\_MCAN\_DBTP\_TDC](#a553232f28f3dcba55eb2e71619cceb10)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| #define | [CAN\_MCAN\_DBTP\_DBRP](#a1697f9a668977dae709f6f5c5c06cec0)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(20, 16) |
| #define | [CAN\_MCAN\_DBTP\_DTSEG1](#a79af67b99451850bbfb3b6fe3f9a1502)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 8) |
| #define | [CAN\_MCAN\_DBTP\_DTSEG2](#a4f6a9528366c7ed61d6b9e5c1fe6e52d)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 4) |
| #define | [CAN\_MCAN\_DBTP\_DSJW](#a010cfca29045f0f643cdacefb6560491)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| #define | [CAN\_MCAN\_TEST](#ad97d62d4799b07bc5a8405f7ace52708)   0x010 |
| #define | [CAN\_MCAN\_TEST\_SVAL](#aa8ad1bcbf0ce358b91810f5349bab4db)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| #define | [CAN\_MCAN\_TEST\_TXBNS](#a28c34733629bef3c9e83add27ceca147)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(20, 16) |
| #define | [CAN\_MCAN\_TEST\_PVAL](#a8210ab176d182b1b1fec7f5fc8f6e44e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [CAN\_MCAN\_TEST\_TXBNP](#aaf9280049a3e2365f9ec7627009989f1)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 8) |
| #define | [CAN\_MCAN\_TEST\_RX](#ad4110c5f53f0632694aebef5eab54a54)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [CAN\_MCAN\_TEST\_TX](#a207ba0562c9e4e4a10cdee1ad524a1c0)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 5) |
| #define | [CAN\_MCAN\_TEST\_LBCK](#aee2a84f2613145af78c97da48781382e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [CAN\_MCAN\_RWD](#ab646e1d2f8a14239b31e54a4728bad81)   0x014 |
| #define | [CAN\_MCAN\_RWD\_WDV](#a639a100e4d8438784faeafdb20df0d35)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8) |
| #define | [CAN\_MCAN\_RWD\_WDC](#a0a64ee92dd024b35047794c8cbb05f6a)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| #define | [CAN\_MCAN\_CCCR](#a33d42748a911e6a337324652ac982c9b)   0x018 |
| #define | [CAN\_MCAN\_CCCR\_NISO](#a430a606d5de2f7cf5958fe1d88ce931e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [CAN\_MCAN\_CCCR\_TXP](#ae091024f68ea83d6f888bcadb99e137c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| #define | [CAN\_MCAN\_CCCR\_EFBI](#ab773d5e87290745fb1958d23720cfbdb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [CAN\_MCAN\_CCCR\_PXHD](#ac5283b03eb7b498fd64e01477bfff300)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [CAN\_MCAN\_CCCR\_WMM](#aab0183fea6cd4dd560b83b2d2049bd75)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [CAN\_MCAN\_CCCR\_UTSU](#a7c424b839fd4ebe69fa9615bc3cb7268)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [CAN\_MCAN\_CCCR\_BRSE](#ace20dbd7d279909999e19dd2a6a82ec9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [CAN\_MCAN\_CCCR\_FDOE](#a26154a84a6124bd8cceae4c0929d6937)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [CAN\_MCAN\_CCCR\_TEST](#af74a4cf81df6d88f8a69db622d71da83)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [CAN\_MCAN\_CCCR\_DAR](#a2f4a7a67f69310b2470c2939cf7488d2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAN\_MCAN\_CCCR\_MON](#a1057947a0482c69e67f32f79b0f0cf56)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [CAN\_MCAN\_CCCR\_CSR](#a39b308a89655c9a59050cffbd2ad3268)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [CAN\_MCAN\_CCCR\_CSA](#a249d3b8483bb7869e2695ee56a8c40e9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [CAN\_MCAN\_CCCR\_ASM](#a40e186041bf0459f6d1fdf5736670e56)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [CAN\_MCAN\_CCCR\_CCE](#ad36bcf2dfbe848fbcbd930055a442cca)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAN\_MCAN\_CCCR\_INIT](#ab7fbe359b62fa11288390c0ed6b22d39)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CAN\_MCAN\_NBTP](#a308c60c14b65b3416d36a37e7b70a318)   0x01C |
| #define | [CAN\_MCAN\_NBTP\_NSJW](#abdd623bc3728e9e6c92d2b842c08d3e7)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 25) |
| #define | [CAN\_MCAN\_NBTP\_NBRP](#a1285c541ff247a4bf26229e0b294af62)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(24, 16) |
| #define | [CAN\_MCAN\_NBTP\_NTSEG1](#a1c18b64cb2e4f22afbd16a61aeb31d42)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8) |
| #define | [CAN\_MCAN\_NBTP\_NTSEG2](#a7c69e8e69f5b9bb61ad0342f8fde2d39)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| #define | [CAN\_MCAN\_TSCC](#a336430f9fd3a26e6c54deaf072bc1ad6)   0x020 |
| #define | [CAN\_MCAN\_TSCC\_TCP](#ad38c5e544217947bd4dd44ec53291e91)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 16) |
| #define | [CAN\_MCAN\_TSCC\_TSS](#aefdf97284e7860342d550e0043c1b80c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| #define | [CAN\_MCAN\_TSCV](#a8704135ca0f1a015b4f6527e6d9bafcd)   0x024 |
| #define | [CAN\_MCAN\_TSCV\_TSC](#a3ac6c1d5d964b1646d1a3e2a53d3206f)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [CAN\_MCAN\_TOCC](#a8913873d251c86e2fee4842bb9c4951c)   0x028 |
| #define | [CAN\_MCAN\_TOCC\_TOP](#a4206bbc473216f1e68f7c6fb02cb27d3)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 16) |
| #define | [CAN\_MCAN\_TOCC\_TOS](#a41d03bd4b12883207842512bde89f8e9)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 1) |
| #define | [CAN\_MCAN\_TOCC\_ETOC](#a63a2024085348c787e6dbc231aa47846)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAN\_MCAN\_TOCV](#a2f4377ce56a8a38991fba9b2cc2d87c9)   0x02C |
| #define | [CAN\_MCAN\_TOCV\_TOC](#aeb97ca070414b41a8de66bdf14f63d32)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| #define | [CAN\_MCAN\_ECR](#aee893904e384ad6b56311078d9546190)   0x040 |
| #define | [CAN\_MCAN\_ECR\_CEL](#a6df87229481d209acb54a719447dad47)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 16) |
| #define | [CAN\_MCAN\_ECR\_RP](#a0be04930627b22f80d548fd367cb847d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [CAN\_MCAN\_ECR\_REC](#ae0a477450ccd40c6a1de4c6bcd3a5997)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(14, 8) |
| #define | [CAN\_MCAN\_ECR\_TEC](#afb635c07c2664e72c64ae614f2d60f94)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| #define | [CAN\_MCAN\_PSR](#a0e6bf5627ac886db479dd34693f8b7a6)   0x044 |
| #define | [CAN\_MCAN\_PSR\_TDCV](#a2133840d3eab9f8a5a881e5c37c3fed2)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 16) |
| #define | [CAN\_MCAN\_PSR\_PXE](#a0769c5c4ee9f406eed816a1104793a0a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| #define | [CAN\_MCAN\_PSR\_RFDF](#a1fb264bdd3e56b11224dc11e2703ac09)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [CAN\_MCAN\_PSR\_RBRS](#ae6cc09fcf5145317c677294a6a8b888b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [CAN\_MCAN\_PSR\_RESI](#acf2c2ff589d5e27335fa216a6df3abb6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [CAN\_MCAN\_PSR\_DLEC](#a346aa3ec31690010401d1d120dda7e4e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(10, 8) |
| #define | [CAN\_MCAN\_PSR\_BO](#a7b72bbe875c0b64e6c608ee2d0927658)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [CAN\_MCAN\_PSR\_EW](#ac8bf022df308ce6bd8797c36d39e0d36)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAN\_MCAN\_PSR\_EP](#a0cf95fc0ddc9b03b177730ae8f8a2128)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [CAN\_MCAN\_PSR\_ACT](#a6afc5e82af45896e01af32e2b2c69993)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 3) |
| #define | [CAN\_MCAN\_PSR\_LEC](#ae49ca535c17a53562b7db3f897dc336a)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| #define | [CAN\_MCAN\_TDCR](#a52cea0ef00b1bf53a4f718104a3ad652)   0x048 |
| #define | [CAN\_MCAN\_TDCR\_TDCO](#ab0a27684c90c1b5828206cd2f034802b)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(14, 8) |
| #define | [CAN\_MCAN\_TDCR\_TDCF](#ae2f0c4a34055d37e49710f594f1736cc)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| #define | [CAN\_MCAN\_IR](#acac62eeff461ebd9ac34b8d622dc8c6b)   0x050 |
| #define | [CAN\_MCAN\_IR\_ARA](#a732f9c3cb965a855c2e733bdadfcaa1e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) |
| #define | [CAN\_MCAN\_IR\_PED](#aa737557f70c4da0a7e5660208d6764df)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) |
| #define | [CAN\_MCAN\_IR\_PEA](#a60f1b085bb9a26d5a211e56f86ac5e86)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| #define | [CAN\_MCAN\_IR\_WDI](#a5adbd7ceb523237265ca3093bd921c20)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| #define | [CAN\_MCAN\_IR\_BO](#a62de51c28140a4e787363c2b579290f6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| #define | [CAN\_MCAN\_IR\_EW](#a5f8cf54fee2939bc2f31c9e414ba202e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| #define | [CAN\_MCAN\_IR\_EP](#ada6d4f670b522c7fd1036721ddc2931a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| #define | [CAN\_MCAN\_IR\_ELO](#a4c88361aa6d63fee591a2010d882107e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22) |
| #define | [CAN\_MCAN\_IR\_BEU](#a20653377f1565e71de286858ca920d46)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| #define | [CAN\_MCAN\_IR\_BEC](#a86431445f96ec66f93828d78ba1311d6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| #define | [CAN\_MCAN\_IR\_DRX](#ab82d152424a84de470bfe005b577368c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| #define | [CAN\_MCAN\_IR\_TOO](#ab5066977fa160d3ded392b054d858637)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| #define | [CAN\_MCAN\_IR\_MRAF](#a00b7078b20f2aa81356694b84a179446)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| #define | [CAN\_MCAN\_IR\_TSW](#a666e16b9ea27b83635067939aef62a31)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| #define | [CAN\_MCAN\_IR\_TEFL](#a090716d481b6e97d251aba9871ac0408)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [CAN\_MCAN\_IR\_TEFF](#a59e276fb6412ba5447994615049cb8fd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| #define | [CAN\_MCAN\_IR\_TEFW](#a07fea07bd4ff7cfd4add4bedc0409e7a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [CAN\_MCAN\_IR\_TEFN](#a5f7fa6444d1afe343920fe4495f64da5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [CAN\_MCAN\_IR\_TFE](#a481a7b485091a9b862ec48a75315e12c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [CAN\_MCAN\_IR\_TCF](#ace4b4fbac614a38e70248aba6df71068)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [CAN\_MCAN\_IR\_TC](#a880558d5672ef8d27bf232eeb739c3e0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [CAN\_MCAN\_IR\_HPM](#aee45488e19c8bbf86ffed780cc3565c3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [CAN\_MCAN\_IR\_RF1L](#ac37b42f53820384cc426b8b078572a35)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [CAN\_MCAN\_IR\_RF1F](#a10193930b296827f124dc98e49c7db2a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAN\_MCAN\_IR\_RF1W](#a9bd64356ca32fef96e6680966e3d77b4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [CAN\_MCAN\_IR\_RF1N](#abed65c016f9adf3794a3fd0474fa84e3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [CAN\_MCAN\_IR\_RF0L](#a530db7342edd5f2f3254ce17745dcb88)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [CAN\_MCAN\_IR\_RF0F](#a15214770d66f4bf0df92ed9457f5954f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [CAN\_MCAN\_IR\_RF0W](#ab737ca9c1a8a152f58dd9d1d2a02790e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAN\_MCAN\_IR\_RF0N](#aef7cfda9d78ed8294e744c3c024e7ce9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CAN\_MCAN\_IE](#a5efcfd38d911a09ba1a0e8546127d73e)   0x054 |
| #define | [CAN\_MCAN\_IE\_ARAE](#a87e7dc8db720db25d80a9464ae0a9a0f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) |
| #define | [CAN\_MCAN\_IE\_PEDE](#a5894eb34123a83e13763525c7725cacb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) |
| #define | [CAN\_MCAN\_IE\_PEAE](#aec30af8e9ea090c3d896c8d815f5fb18)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| #define | [CAN\_MCAN\_IE\_WDIE](#a80f67433f566f71224184fd6f4047096)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| #define | [CAN\_MCAN\_IE\_BOE](#a7adbce95af6bb9efbf20188ebf6584f7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| #define | [CAN\_MCAN\_IE\_EWE](#a5727d4efbe75dbbb022b3df9f64134ae)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| #define | [CAN\_MCAN\_IE\_EPE](#aaf858f5603f46e886d2a255d027e2057)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| #define | [CAN\_MCAN\_IE\_ELOE](#aeb78e4ebe0c9522accc5836d2a9f33d1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22) |
| #define | [CAN\_MCAN\_IE\_BEUE](#a7748c310633b29084ff3673aff28e749)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| #define | [CAN\_MCAN\_IE\_BECE](#a8e2fc398be6df304991143af43ae4ed3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| #define | [CAN\_MCAN\_IE\_DRXE](#a14f6823f3ee219eafc5370f6bd9cc839)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| #define | [CAN\_MCAN\_IE\_TOOE](#adffa68a3e8e9186595f139e5b8f78025)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| #define | [CAN\_MCAN\_IE\_MRAFE](#a8570c8e17b23bd00f3d3e671ecdc0301)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| #define | [CAN\_MCAN\_IE\_TSWE](#a5d66c2cef0008cdb2b7faae4f838fde1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| #define | [CAN\_MCAN\_IE\_TEFLE](#a2ebfaf6bf1f175917a20fd47b2d241f0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [CAN\_MCAN\_IE\_TEFFE](#a61e51933d46002e468e3965fdd3100ce)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| #define | [CAN\_MCAN\_IE\_TEFWE](#aa983e0f26d5454b297866a5778c09915)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [CAN\_MCAN\_IE\_TEFNE](#a5cca5bd86ccf8433b693daf805f150de)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [CAN\_MCAN\_IE\_TFEE](#a5fd83f7f8b769c493b2b99fae7cf3bcf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [CAN\_MCAN\_IE\_TCFE](#a3f1f30cfdbffdc698d7c6ad94d8617db)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [CAN\_MCAN\_IE\_TCE](#a7545997948206ff883a9f2cd9c327f35)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [CAN\_MCAN\_IE\_HPME](#a626e0d5094618d3d45a3d614598c426a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [CAN\_MCAN\_IE\_RF1LE](#a7c535f93189d8d5f41320e6fa364a005)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [CAN\_MCAN\_IE\_RF1FE](#a10bba01222375ae38f049ee8abc50973)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAN\_MCAN\_IE\_RF1WE](#af399bd4422077374595d152dee4e7860)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [CAN\_MCAN\_IE\_RF1NE](#a39f3b5000f6290513d723b3bf8869aba)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [CAN\_MCAN\_IE\_RF0LE](#a72eb6ded2dcd94d3785887fef5f231a1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [CAN\_MCAN\_IE\_RF0FE](#a42b4e6e1a7138f356bdb2c5ed87eea95)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [CAN\_MCAN\_IE\_RF0WE](#a85118c1d03eadd4a6a76cf935fbe17bc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAN\_MCAN\_IE\_RF0NE](#af31e0711f5628614ce69969c14c78fb8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CAN\_MCAN\_ILS](#a6d2a927e67ecb7c01749d6a0fbc25363)   0x058 |
| #define | [CAN\_MCAN\_ILS\_ARAL](#ac06e1958c3690032639849b9b291ca7f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) |
| #define | [CAN\_MCAN\_ILS\_PEDL](#a1863554a941902bd0a585916b3016ec9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) |
| #define | [CAN\_MCAN\_ILS\_PEAL](#a78ce183fb2e265f8b850c52b2e0b9b83)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| #define | [CAN\_MCAN\_ILS\_WDIL](#a28b9d67835f409299a7dbfddce41674e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| #define | [CAN\_MCAN\_ILS\_BOL](#a4be2c784e04021c28fb0bda474af2008)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| #define | [CAN\_MCAN\_ILS\_EWL](#ac250560aafee73e83b7cc4db7333f037)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| #define | [CAN\_MCAN\_ILS\_EPL](#a49654d0bbf4af7dabf2bf89805177fb9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| #define | [CAN\_MCAN\_ILS\_ELOL](#a24400f4c04a26a183853dcd8c6401849)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22) |
| #define | [CAN\_MCAN\_ILS\_BEUL](#a4992a22be098fa66ae40119f88ae9c42)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| #define | [CAN\_MCAN\_ILS\_BECL](#adb5a621d293f0bde671a9246f67af57d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| #define | [CAN\_MCAN\_ILS\_DRXL](#a414c9f4b86e1f851b9f12356bc440236)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| #define | [CAN\_MCAN\_ILS\_TOOL](#a3b37679278affda2b8b17a975c97a1cf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| #define | [CAN\_MCAN\_ILS\_MRAFL](#a6a139692dcf97de3500d4692119610e3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| #define | [CAN\_MCAN\_ILS\_TSWL](#af1815cb8b62a185a739e23d4bbcedbc0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| #define | [CAN\_MCAN\_ILS\_TEFLL](#abbe6c6994e95786e081b110c6fec56b3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [CAN\_MCAN\_ILS\_TEFFL](#a0c60df858386dbde519d03f448282177)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| #define | [CAN\_MCAN\_ILS\_TEFWL](#aa3418486b5bdee960076c03c6310b47d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| #define | [CAN\_MCAN\_ILS\_TEFNL](#af42996807b1747d5f08540b18c3fdf5a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [CAN\_MCAN\_ILS\_TFEL](#a287b7fec7f9917f18011994dc3329f5f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [CAN\_MCAN\_ILS\_TCFL](#abfaf532cc23ba6f63149bc97dc3c855e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [CAN\_MCAN\_ILS\_TCL](#ab294335aa5dff81c72d89f4e6c2f506a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [CAN\_MCAN\_ILS\_HPML](#a7922ad47535e02146816b07e0ee7c499)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [CAN\_MCAN\_ILS\_RF1LL](#ad1868981fcc7e414c75e005e93859343)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [CAN\_MCAN\_ILS\_RF1FL](#a0695d2cfd07a5717fb2e307b047567fe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CAN\_MCAN\_ILS\_RF1WL](#ac70c241178121176bebdb4c13ec29c65)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [CAN\_MCAN\_ILS\_RF1NL](#a182bc538b568b402370e02a969dd5bd9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [CAN\_MCAN\_ILS\_RF0LL](#ac7304d316f701ad6a0f66ca62cbbcf00)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [CAN\_MCAN\_ILS\_RF0FL](#a061b5b7c74b8a0afc0a78f01b1374e28)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [CAN\_MCAN\_ILS\_RF0WL](#a389d1fe76759d470fb8af80698b4708f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAN\_MCAN\_ILS\_RF0NL](#ad40a58d2e4240ce58f4da55ebf0756e5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CAN\_MCAN\_ILE](#a32e14f45e1c85a73e816a7a78477b703)   0x05C |
| #define | [CAN\_MCAN\_ILE\_EINT1](#a9022d6b85f32310f57a8a711409b4beb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAN\_MCAN\_ILE\_EINT0](#a10be46e7dbc334e014d3a5126d2d8832)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CAN\_MCAN\_GFC](#acedea2dc6c2eaa750196ea330028137d)   0x080 |
| #define | [CAN\_MCAN\_GFC\_ANFS](#ad8f1ee3bcf1ce148ecc604177777fe36)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 4) |
| #define | [CAN\_MCAN\_GFC\_ANFE](#a1ecb99bb847bb0305ca2720c18f77ae1)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 2) |
| #define | [CAN\_MCAN\_GFC\_RRFS](#a719015ab076274c8f71a574975a6a1c9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [CAN\_MCAN\_GFC\_RRFE](#af72ebd1644ee7651b6755dbc2d999da1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CAN\_MCAN\_SIDFC](#a27a0bbdaa9b9bfba7227dbe1350f2c74)   0x084 |
| #define | [CAN\_MCAN\_SIDFC\_LSS](#a906b8e66d3294d68ebdff6a7c5283526)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 16) |
| #define | [CAN\_MCAN\_SIDFC\_FLSSA](#ac73011c520eea37b4ca36da8259b3f77)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| #define | [CAN\_MCAN\_XIDFC](#abc56cb7ea0b29dd3c813494cad7ba81c)   0x088 |
| #define | [CAN\_MCAN\_XIDFC\_LSS](#adc32a4719774acdac26727fc7910698a)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 16) |
| #define | [CAN\_MCAN\_XIDFC\_FLESA](#a43ad251923878baed62ab97ed44b0dc9)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| #define | [CAN\_MCAN\_XIDAM](#a9c64c5bcc80f2bdaad64de5c370826db)   0x090 |
| #define | [CAN\_MCAN\_XIDAM\_EIDM](#afd1f6383e81e4dfbc1a156bf5a3092bb)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(28, 0) |
| #define | [CAN\_MCAN\_HPMS](#a13f990a79472988c3b9b8f9b17795b93)   0x094 |
| #define | [CAN\_MCAN\_HPMS\_FLST](#a016ae0f271581c7f77fb3eede5866ab7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| #define | [CAN\_MCAN\_HPMS\_FIDX](#a15a0a60646ea281d06aeebf4f94655c5)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(14, 8) |
| #define | [CAN\_MCAN\_HPMS\_MSI](#a8d47e3cb602ffd092e7da40d2268bc87)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 6) |
| #define | [CAN\_MCAN\_HPMS\_BIDX](#a870c4e0a0829eb9ce24fb14c62383e44)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| #define | [CAN\_MCAN\_NDAT1](#a38c5b3177e25905cc78f7dbcee956f77)   0x098 |
| #define | [CAN\_MCAN\_NDAT1\_ND](#ac533f25e977b0eeb37cb5e047a7dd7f6)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_NDAT2](#afce0263a9bbe5901e3d5e0020282efda)   0x09C |
| #define | [CAN\_MCAN\_NDAT2\_ND](#ac443c986084e5bc0b618049f20193715)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_RXF0C](#acafb4bdf5f41886fe05ab96ce9d3e40f)   0x0A0 |
| #define | [CAN\_MCAN\_RXF0C\_F0OM](#aa60d7075af7dc69fe61f7c9ed26b4db8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| #define | [CAN\_MCAN\_RXF0C\_F0WM](#a407c6bb15b8f0c296004c5f2dffd1255)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(30, 24) |
| #define | [CAN\_MCAN\_RXF0C\_F0S](#a36b805fdfa202f8ea7fc885a75f889a3)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 16) |
| #define | [CAN\_MCAN\_RXF0C\_F0SA](#a2be907b2a04b58df30f5a4e4d2c0cbc0)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| #define | [CAN\_MCAN\_RXF0S](#a8af4d58a4ae713351c0c944bb4468359)   0x0A4 |
| #define | [CAN\_MCAN\_RXF0S\_RF0L](#a2841566e304c9d151763000dbb5b2792)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| #define | [CAN\_MCAN\_RXF0S\_F0F](#aa8649180143ff827bc49a7789682b377)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| #define | [CAN\_MCAN\_RXF0S\_F0PI](#ae3b41edffd1a7a8e8ddf96b450aac3ec)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| #define | [CAN\_MCAN\_RXF0S\_F0GI](#acec1a9ead6d7e01e1178ea56a0d66b2e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(13, 8) |
| #define | [CAN\_MCAN\_RXF0S\_F0FL](#ae8ab0a46f01834f07076750e909f099b)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| #define | [CAN\_MCAN\_RXF0A](#addda3c98094c821fe63bf24782d140d1)   0x0A8 |
| #define | [CAN\_MCAN\_RXF0A\_F0AI](#ab806cb88a0961da39319c8db90a0bfb6)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| #define | [CAN\_MCAN\_RXBC](#a9cb2ddc82fcfb102484577307c88481b)   0x0AC |
| #define | [CAN\_MCAN\_RXBC\_RBSA](#ad7bf916dc45e84b85f6c895fefdb9e99)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| #define | [CAN\_MCAN\_RXF1C](#a4b0612f2b06cf3af04fe969d97106cb5)   0x0B0 |
| #define | [CAN\_MCAN\_RXF1C\_F1OM](#a3f39ada97a9ebd6dcfe4d5bb9adfadee)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| #define | [CAN\_MCAN\_RXF1C\_F1WM](#a65cd1948f37dbc67fa85dde655a997b3)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(30, 24) |
| #define | [CAN\_MCAN\_RXF1C\_F1S](#a9f4dc18657f25ebd2463bf55af719f04)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 16) |
| #define | [CAN\_MCAN\_RXF1C\_F1SA](#a23131c2ea676b9a913be4fce2ca8cf9e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| #define | [CAN\_MCAN\_RXF1S](#a63a683d44b63affa919963adf94f755c)   0x0B4 |
| #define | [CAN\_MCAN\_RXF1S\_RF1L](#a5f55e6eeff595af1f6f1eaeedfb9b62d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| #define | [CAN\_MCAN\_RXF1S\_F1F](#a407843916f140d8bbd2546eb1f1955e6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| #define | [CAN\_MCAN\_RXF1S\_F1PI](#a8bf02cc958131a3a25218058159bb2bf)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| #define | [CAN\_MCAN\_RXF1S\_F1GI](#aaed234ff229b28f3f0926468d9fd32af)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(13, 8) |
| #define | [CAN\_MCAN\_RXF1S\_F1FL](#aaf8df87b128358e2b211c6000b389d64)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| #define | [CAN\_MCAN\_RXF1A](#af3101a1d476ed8304885c33367e19d0f)   0x0B8 |
| #define | [CAN\_MCAN\_RXF1A\_F1AI](#a190b1df18ce88e67dd24145d6bb4d899)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| #define | [CAN\_MCAN\_RXESC](#a83c90feeec80071bc35b3dcce8f6be99)   0x0BC |
| #define | [CAN\_MCAN\_RXESC\_RBDS](#aff5420d9503e9ec130ad37a40021f738)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(10, 8) |
| #define | [CAN\_MCAN\_RXESC\_F1DS](#ad8600748ee89bec9c7efe76e4a743ed7)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 4) |
| #define | [CAN\_MCAN\_RXESC\_F0DS](#a5e45adc0b6acba20391c6f5adc6c5ec3)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| #define | [CAN\_MCAN\_TXBC](#aabbf65d56f0aacdd26b22eb80b34721e)   0x0C0 |
| #define | [CAN\_MCAN\_TXBC\_TFQM](#a4ff2da25354a95ae078951a3b8f0b1f0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30) |
| #define | [CAN\_MCAN\_TXBC\_TFQS](#a25144c814fa7ed19bd6c391cbb2244e6)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(29, 24) |
| #define | [CAN\_MCAN\_TXBC\_NDTB](#afe25b1f33b0a877b8e46d35a26b5db8e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| #define | [CAN\_MCAN\_TXBC\_TBSA](#a54aa984e023137eb87aa8b00f59ea02c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| #define | [CAN\_MCAN\_TXFQS](#abdd2a49df8465eb55633f8707a46187e)   0x0C4 |
| #define | [CAN\_MCAN\_TXFQS\_TFQF](#a37ef0318a42bba8b5fce6d9d9ca094df)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| #define | [CAN\_MCAN\_TXFQS\_TFQPI](#ae479a0770d5629198d3104a9729a777f)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(20, 16) |
| #define | [CAN\_MCAN\_TXFQS\_TFGI](#aac92788e1f00b7af37d15cad4a660cfe)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 8) |
| #define | [CAN\_MCAN\_TXFQS\_TFFL](#a47bcf7d8796c4b4442afc1e194dcf657)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| #define | [CAN\_MCAN\_TXESC](#a4a862608de38135c9febbb6d75b153ef)   0x0C8 |
| #define | [CAN\_MCAN\_TXESC\_TBDS](#ad20ed0d0615c7f4804cbb9324499f84d)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| #define | [CAN\_MCAN\_TXBRP](#a3c8dcbcf3921d5e51306cb8e5feb2cd1)   0x0CC |
| #define | [CAN\_MCAN\_TXBRP\_TRP](#a8e4d1e69b827265adb8aff580ca01cde)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_TXBAR](#a547995f6d877963184992a5cc09fdcf3)   0x0D0 |
| #define | [CAN\_MCAN\_TXBAR\_AR](#ae92b22867500ceb14a6e2035cbf6c8b1)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_TXBCR](#ad0f3bb0f2d096cff8e1e2ac4416c44e0)   0x0D4 |
| #define | [CAN\_MCAN\_TXBCR\_CR](#a023ae0f402eb013e68d35a1e367ff710)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_TXBTO](#ab8050da5ff162f638b7920cc80115a8a)   0x0D8 |
| #define | [CAN\_MCAN\_TXBTO\_TO](#adf91c2d98d25bf2f2901e215a8715b9b)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_TXBCF](#a6d671b8127c66b7e8a7e019b68201afd)   0x0DC |
| #define | [CAN\_MCAN\_TXBCF\_CF](#a027220d5bfd988da4716e5e89d9e7f9d)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_TXBTIE](#a8a4753541d28a7ff92d8b7ba844fa943)   0x0E0 |
| #define | [CAN\_MCAN\_TXBTIE\_TIE](#a7f99c9c844897923c02a1356af052ddf)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_TXBCIE](#aafe9d81dfa50841d20a1a6719b544017)   0x0E4 |
| #define | [CAN\_MCAN\_TXBCIE\_CFIE](#a1b0214f3f897c6852e4fdbff3f8f21a2)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| #define | [CAN\_MCAN\_TXEFC](#a68ea1bab6b687ad406f416c73441ff9c)   0x0F0 |
| #define | [CAN\_MCAN\_TXEFC\_EFWM](#a7551e23d8ba589be55831268b69ce099)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(29, 24) |
| #define | [CAN\_MCAN\_TXEFC\_EFS](#af2ade33b56998a19aeda8cb0f868324c)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| #define | [CAN\_MCAN\_TXEFC\_EFSA](#a162a0b6fd08c65359afa9dc59fba9ed3)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| #define | [CAN\_MCAN\_TXEFS](#a48888433839c16389c97ab6a359667d1)   0x0F4 |
| #define | [CAN\_MCAN\_TXEFS\_TEFL](#a6f4fdc1835216b1408796b9f541054b8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| #define | [CAN\_MCAN\_TXEFS\_EFF](#ae430823894219a2e271310be16e484f4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| #define | [CAN\_MCAN\_TXEFS\_EFPI](#a64ccc68de69d3d46367e05e46934225e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(20, 16) |
| #define | [CAN\_MCAN\_TXEFS\_EFGI](#af69a4882448bb8cab8bee6c20f145e18)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 8) |
| #define | [CAN\_MCAN\_TXEFS\_EFFL](#a94994438584cfdfa0a9c7bc91227ee7e)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| #define | [CAN\_MCAN\_TXEFA](#a3a0b6530cbff5e1661c6ad208cedff08)   0x0F8 |
| #define | [CAN\_MCAN\_TXEFA\_EFAI](#a78b3604320fdc00e0fe734516f5e1db9)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| #define | [CAN\_MCAN\_DT\_MRAM\_OFFSET](#a06194f088174c2634bd318aaaddca988)(node\_id) |
|  | Get the Bosch M\_CAN Message RAM offset. |
| #define | [CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS](#a87442fd647be89575fbd0e3a6a4f2540)(node\_id) |
|  | Get the number of standard (11-bit) filter elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS](#a8c5ca10a9d376f42cecdb4fcaa1c2f86)(node\_id) |
|  | Get the number of extended (29-bit) filter elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS](#a5b814febb2893a33617455a070f1814f)(node\_id) |
|  | Get the number of Rx FIFO 0 elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS](#a71941bfd0f048401fd1208d556260f32)(node\_id) |
|  | Get the number of Rx FIFO 1 elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS](#ad2371b27de938b29f42d2991a3f1009f)(node\_id) |
|  | Get the number of Rx Buffer elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS](#abbdb679ab26eb135d43dcc2394bded71)(node\_id) |
|  | Get the number of Tx Event FIFO elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS](#a7d725b5c696acbc394547800a5e729ae)(node\_id) |
|  | Get the number of Tx Buffer elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET](#a4c6c3b23eed2ae336882cbfbb69d8578)(node\_id) |
|  | Get the base offset of standard (11-bit) filter elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET](#a71687f621eae0d9f930ede70cb99cff7)(node\_id) |
|  | Get the base offset of extended (29-bit) filter elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET](#a79b1f334979e5d7f180b6f37fbcb772f)(node\_id) |
|  | Get the base offset of Rx FIFO 0 elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET](#aa4c0f6e4696d3c82344bd099eb0dcd13)(node\_id) |
|  | Get the base offset of Rx FIFO 1 elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET](#aa0d25966039a769edd9b8b4f31af2c9f)(node\_id) |
|  | Get the base offset of Rx Buffer elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET](#a16ce04fda8d800582ccc1b6979d34ac4)(node\_id) |
|  | Get the base offset of Tx Event FIFO elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET](#a1f3384686c23982de8acef2182597e69)(node\_id) |
|  | Get the base offset of Tx Buffer elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MCAN\_ADDR](#aaed34aa27da9ac0948d8b6ab798c7170)(node\_id) |
|  | Get the Bosch M\_CAN register base address. |
| #define | [CAN\_MCAN\_DT\_MRBA](#ad7d854278909e12accdef06f2dc7a490)(node\_id) |
|  | Get the Bosch M\_CAN Message RAM base address. |
| #define | [CAN\_MCAN\_DT\_MRAM\_ADDR](#acecc9210d2504ba1dda108a79a2afb78)(node\_id) |
|  | Get the Bosch M\_CAN Message RAM address. |
| #define | [CAN\_MCAN\_DT\_MRAM\_SIZE](#a94743f60c64c64a1e2bfd78fcc864cf1)(node\_id) |
|  | Get the Bosch M\_CAN Message RAM size. |
| #define | [CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE](#a47fa1c0ca484d6f891c4834071d421e4)(node\_id) |
|  | Get the total size of all Bosch M\_CAN Message RAM elements. |
| #define | [CAN\_MCAN\_DT\_MRAM\_DEFINE](#a146911ec873fd653f8f9538a85202917)(node\_id, \_name) |
|  | Define a RAM buffer for Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG](#af277dd5f60b0620b3ffc5030f0c794f6)(node\_id) |
|  | Assert that the Message RAM configuration meets the Bosch M\_CAN IP core restrictions. |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_OFFSET](#a3095ec5dd938ab990c71c06b5ba84d03)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_OFFSET(DT\_DRV\_INST(inst))](#a06194f088174c2634bd318aaaddca988). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_STD\_FILTER\_ELEMENTS](#a41d9d7f70dfedbe8eeacfd27a8610007)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(DT\_DRV\_INST(inst))](#a87442fd647be89575fbd0e3a6a4f2540). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_EXT\_FILTER\_ELEMENTS](#aac3f321fee276c68e51073dfbcd81150)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(DT\_DRV\_INST(inst))](#a8c5ca10a9d376f42cecdb4fcaa1c2f86). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO0\_ELEMENTS](#a393289abde09b6190964fe69f2529c27)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(DT\_DRV\_INST(inst))](#a5b814febb2893a33617455a070f1814f). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO1\_ELEMENTS](#a30eef08af0433049ed28c51d640d3679)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(DT\_DRV\_INST(inst))](#a71941bfd0f048401fd1208d556260f32). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_RX\_BUFFER\_ELEMENTS](#aa2a372c40cce733d10d9b33651cfdb1c)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(DT\_DRV\_INST(inst))](#ad2371b27de938b29f42d2991a3f1009f). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS](#ae10a6c1414a951808e818728e5d74e52)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(DT\_DRV\_INST(inst))](#abbdb679ab26eb135d43dcc2394bded71). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_TX\_BUFFER\_ELEMENTS](#aa4275ca727057cdf4a0fe486b87d238d)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(DT\_DRV\_INST(inst))](#a7d725b5c696acbc394547800a5e729ae). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_STD\_FILTER\_OFFSET](#a9c7a3869df9defc3f466f8de89b86561)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET(DT\_DRV\_INST(inst))](#a4c6c3b23eed2ae336882cbfbb69d8578). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_EXT\_FILTER\_OFFSET](#a8595df90a5c45639ae9e576dcc61ea0d)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET(DT\_DRV\_INST(inst))](#a71687f621eae0d9f930ede70cb99cff7). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO0\_OFFSET](#a48fe93b1bd51cdb7dcb1312ee160eab7)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET(DT\_DRV\_INST(inst))](#a79b1f334979e5d7f180b6f37fbcb772f). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO1\_OFFSET](#ad80049c12ef02f78736268f9abb7c303)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET(DT\_DRV\_INST(inst))](#aa4c0f6e4696d3c82344bd099eb0dcd13). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_RX\_BUFFER\_OFFSET](#aea15c0e894fdbacaeead2d108c7c0b94)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET(DT\_DRV\_INST(inst))](#aa0d25966039a769edd9b8b4f31af2c9f). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_TX\_EVENT\_FIFO\_OFFSET](#a63623852de6c5dd34509823446db1af9)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(DT\_DRV\_INST(inst))](#a16ce04fda8d800582ccc1b6979d34ac4). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_TX\_BUFFER\_OFFSET](#a9bb9a0d6d8b3de3e24d533ec15c1215d)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET(DT\_DRV\_INST(inst))](#a1f3384686c23982de8acef2182597e69). |
| #define | [CAN\_MCAN\_DT\_INST\_MCAN\_ADDR](#affa0cab849e56fe5016bc4aa8b43a1d1)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MCAN\_ADDR(DT\_DRV\_INST(inst))](#aaed34aa27da9ac0948d8b6ab798c7170). |
| #define | [CAN\_MCAN\_DT\_INST\_MRBA](#a25b114591fdf1330865adfa7706cd62b)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRBA(DT\_DRV\_INST(inst))](#ad7d854278909e12accdef06f2dc7a490). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_ADDR](#a6fee1c336a0c7de5d8cda6bf2338ad3c)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_ADDR(DT\_DRV\_INST(inst))](#acecc9210d2504ba1dda108a79a2afb78). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_SIZE](#a63e750530c43000bafa36a808582f9d4)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_SIZE(DT\_DRV\_INST(inst))](#a94743f60c64c64a1e2bfd78fcc864cf1). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_ELEMENTS\_SIZE](#a5d0cc45852e301e4e38652218a5fc594)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE(DT\_DRV\_INST(inst))](#a47fa1c0ca484d6f891c4834071d421e4). |
| #define | [CAN\_MCAN\_DT\_INST\_MRAM\_DEFINE](#a6081976c4a78765061c3832253e2bcda)(inst, \_name) |
|  | Equivalent to [CAN\_MCAN\_DT\_MRAM\_DEFINE(DT\_DRV\_INST(inst))](#a146911ec873fd653f8f9538a85202917). |
| #define | [CAN\_MCAN\_TIMING\_MIN\_INITIALIZER](#aa0de1f9512dc3e3d44f06a2f7f2f4adf) |
|  | Bosch M\_CAN specific static initializer for a minimum nominal `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct. |
| #define | [CAN\_MCAN\_TIMING\_MAX\_INITIALIZER](#aedef0bb36bcd204ee5000ae9528248b7) |
|  | Bosch M\_CAN specific static initializer for a maximum nominal `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct. |
| #define | [CAN\_MCAN\_TIMING\_DATA\_MIN\_INITIALIZER](#afd190643aa2435880769aef338f02d23) |
|  | Bosch M\_CAN specific static initializer for a minimum data phase `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct. |
| #define | [CAN\_MCAN\_TIMING\_DATA\_MAX\_INITIALIZER](#aa0f79f1ce18146a1ad90609e4020308c) |
|  | Bosch M\_CAN specific static initializer for a maximum data phase `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct. |
| #define | [CAN\_MCAN\_DT\_INST\_BUILD\_ASSERT\_MRAM\_CFG](#a67daccd5aed8a4de6fc7489592a6b268)(inst) |
|  | Equivalent to [CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG(DT\_DRV\_INST(inst))](#af277dd5f60b0620b3ffc5030f0c794f6). |
| #define | [CAN\_MCAN\_XFEC\_DISABLE](#ac336e47e175c4c54469ce58ca122195c)   0x0 |
| #define | [CAN\_MCAN\_XFEC\_FIFO0](#a7312f835309269943ff6b758521449b6)   0x1 |
| #define | [CAN\_MCAN\_XFEC\_FIFO1](#ad0570275343000c1af9a14e0589939c3)   0x2 |
| #define | [CAN\_MCAN\_XFEC\_REJECT](#a2cd5607208221a6da2cf07e67ef00dde)   0x3 |
| #define | [CAN\_MCAN\_XFEC\_PRIO](#a95f862be638ce43223aebcd1f763be2d)   0x4 |
| #define | [CAN\_MCAN\_XFEC\_PRIO\_FIFO0](#aec0a8173842cc5f1a13e84fb5ee38f19)   0x5 |
| #define | [CAN\_MCAN\_XFEC\_PRIO\_FIFO1](#a3073ff3bc20ef4a28af1d92f9d2e9a02)   0x7 |
| #define | [CAN\_MCAN\_SFT\_RANGE](#a39fcb587e3a98e256fd70af2408d1fc4)   0x0 |
| #define | [CAN\_MCAN\_SFT\_DUAL](#aadfcd6a191d8eb4c2f0403cba4518a8e)   0x1 |
| #define | [CAN\_MCAN\_SFT\_CLASSIC](#a7d5274ba0f020deda315bd10da7787ce)   0x2 |
| #define | [CAN\_MCAN\_SFT\_DISABLED](#ac64298dffd12e5f148438af6b2c9f578)   0x3 |
| #define | [CAN\_MCAN\_EFT\_RANGE\_XIDAM](#a2391eb72cedd2f2cc17959c73bb1afb4)   0x0 |
| #define | [CAN\_MCAN\_EFT\_DUAL](#aaa5fe73386232cef16ffb79561064200)   0x1 |
| #define | [CAN\_MCAN\_EFT\_CLASSIC](#aa04e5c32ec68157807013ae542339c34)   0x2 |
| #define | [CAN\_MCAN\_EFT\_RANGE](#ae0ebf402133070f34c942230f0ae9f6a)   0x3 |
| #define | [CAN\_MCAN\_CALLBACKS\_DEFINE](#ab5e7cb2c8423200a929544a18ad66c2a)(\_name, \_tx, \_std, \_ext) |
|  | Define Bosch M\_CAN TX and RX callbacks. |
| #define | [CAN\_MCAN\_DT\_CALLBACKS\_DEFINE](#a8264915913cfdb4cd7fe5d53cb6cf64b)(node\_id, \_name) |
|  | Define Bosch M\_CAN TX and RX callbacks. |
| #define | [CAN\_MCAN\_DT\_INST\_CALLBACKS\_DEFINE](#a93e84f959d380f927473ca3b9510d7bc)(inst, \_name) |
|  | Equivalent to [CAN\_MCAN\_DT\_CALLBACKS\_DEFINE(DT\_DRV\_INST(inst))](#a8264915913cfdb4cd7fe5d53cb6cf64b). |
| #define | [CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET](#a2e52150401d29533258224a14600b255)(node\_id) |
|  | Get an array containing the number of elements in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET](#a907c70d4c64353647bf1718c45e11c5a)(node\_id) |
|  | Get an array containing the base offsets for element in Bosch M\_CAN Message RAM. |
| #define | [CAN\_MCAN\_DT\_CONFIG\_GET](#a6ebe5c51c603b5b820682e291df06ac8)(node\_id, \_custom, \_ops, \_cbs) |
|  | Static initializer for `[can_mcan_config](structcan__mcan__config.md "Bosch M_CAN driver internal configuration structure.")` struct. |
| #define | [CAN\_MCAN\_DT\_CONFIG\_INST\_GET](#af001b33da9876cbde179757687d25ec0)(inst, \_custom, \_ops, \_cbs) |
|  | Static initializer for `[can_mcan_config](structcan__mcan__config.md "Bosch M_CAN driver internal configuration structure.")` struct from DT\_DRV\_COMPAT instance. |
| #define | [CAN\_MCAN\_DATA\_INITIALIZER](#a0684e639e58ecd6e7f8188cea455d4d8)(\_custom) |
|  | Initializer for a *[can\_mcan\_data](structcan__mcan__data.md "Bosch M_CAN driver internal data structure.")* struct. |
| Indexes for the cells in the devicetree bosch,mram-cfg property | |
| These match the description of the cells in the bosch,m\_can-base devicetree binding. | |
| #define | [CAN\_MCAN\_MRAM\_CFG\_OFFSET](#a1b2e247424c436244e795ef253840d58)   0 |
|  | offset cell index |
| #define | [CAN\_MCAN\_MRAM\_CFG\_STD\_FILTER](#a651e96118352208ff4a5b041f051d10f)   1 |
|  | std-filter-elements cell index |
| #define | [CAN\_MCAN\_MRAM\_CFG\_EXT\_FILTER](#a9a43d8d379fee72d0c46841538b22e91)   2 |
|  | ext-filter-elements cell index |
| #define | [CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO0](#aacc3d7a9ace66c6322a07186a72324ef)   3 |
|  | rx-fifo0-elements cell index |
| #define | [CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO1](#a6bdc1012af79c50869279a7caac4ff31)   4 |
|  | rx-fifo1-elements cell index |
| #define | [CAN\_MCAN\_MRAM\_CFG\_RX\_BUFFER](#aa1c3bbb17546a5c8daaf5c80e028e1bf)   5 |
|  | rx-buffer-elements cell index |
| #define | [CAN\_MCAN\_MRAM\_CFG\_TX\_EVENT\_FIFO](#a35fbb5986ca2268dd650b00970da363d)   6 |
|  | tx-event-fifo-elements cell index |
| #define | [CAN\_MCAN\_MRAM\_CFG\_TX\_BUFFER](#ab18faf8f17480060d0102bb9370378c1)   7 |
|  | tx-buffer-elements cell index |
| #define | [CAN\_MCAN\_MRAM\_CFG\_NUM\_CELLS](#abb4087b9c7ac31e8a1cb7003945dad97)   8 |
|  | Total number of cells in bosch,mram-cfg property. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [can\_mcan\_read\_reg\_t](#a79941b7745919bb1bf7d7219555440a6)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | Bosch M\_CAN driver front-end callback for reading a register value. |
| typedef int(\* | [can\_mcan\_write\_reg\_t](#acbb72b712e516fe923e6030a9d6b36c1)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Bosch M\_CAN driver front-end callback for writing a register value. |
| typedef int(\* | [can\_mcan\_read\_mram\_t](#a9532f0655c579f0ab091f85771b5d62d)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Bosch M\_CAN driver front-end callback for reading from Message RAM. |
| typedef int(\* | [can\_mcan\_write\_mram\_t](#aaf2920e649f9671f09856a062ac4dc95)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Bosch M\_CAN driver front-end callback for writing to Message RAM. |
| typedef int(\* | [can\_mcan\_clear\_mram\_t](#a321813b4b3def118480a7a9eccb6d4aa)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Bosch M\_CAN driver front-end callback for clearing Message RAM. |

| Enumerations | |
| --- | --- |
| enum | [can\_mcan\_psr\_lec](#a888671da33c3ffc35ce94c8eba13d462) {     [CAN\_MCAN\_PSR\_LEC\_NO\_ERROR](#a888671da33c3ffc35ce94c8eba13d462acab41a3d432b309d9b73a711d84b39e9) = 0 , [CAN\_MCAN\_PSR\_LEC\_STUFF\_ERROR](#a888671da33c3ffc35ce94c8eba13d462a0207d3347a4afc89d17fa6b954ae90d0) = 1 , [CAN\_MCAN\_PSR\_LEC\_FORM\_ERROR](#a888671da33c3ffc35ce94c8eba13d462ac4bce840b2edcf97957d74e6debe9b03) = 2 , [CAN\_MCAN\_PSR\_LEC\_ACK\_ERROR](#a888671da33c3ffc35ce94c8eba13d462a9e5414792478db5f57f1f270d0ceac13) = 3 ,     [CAN\_MCAN\_PSR\_LEC\_BIT1\_ERROR](#a888671da33c3ffc35ce94c8eba13d462a7de1a2f2ced1a52f01ee4d9f2b9b6b80) = 4 , [CAN\_MCAN\_PSR\_LEC\_BIT0\_ERROR](#a888671da33c3ffc35ce94c8eba13d462a4bca141d0a3056cbdfc379f49d60c651) = 5 , [CAN\_MCAN\_PSR\_LEC\_CRC\_ERROR](#a888671da33c3ffc35ce94c8eba13d462a7a19af0809a0613a8becb016781b03dc) = 6 , [CAN\_MCAN\_PSR\_LEC\_NO\_CHANGE](#a888671da33c3ffc35ce94c8eba13d462a683c68657e49efd306f43be43bd3167e) = 7   } |

| Functions | |
| --- | --- |
| static int | [can\_mcan\_sys\_read\_reg](#a2138e6f7c669bf8a1c1f04637ec9752c) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | Bosch M\_CAN driver front-end callback helper for reading a memory mapped register. |
| static int | [can\_mcan\_sys\_write\_reg](#ac1562291a74cc1f5b5e6d82fe31141bb) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Bosch M\_CAN driver front-end callback helper for writing a memory mapped register. |
| static int | [can\_mcan\_sys\_read\_mram](#a5d7d5e0bb88b661462fa01720d824610) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Bosch M\_CAN driver front-end callback helper for reading from memory mapped Message RAM. |
| static int | [can\_mcan\_sys\_write\_mram](#a21e0977205bb9db1be83968fda99bf95) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Bosch M\_CAN driver front-end callback helper for writing to memory mapped Message RAM. |
| static int | [can\_mcan\_sys\_clear\_mram](#a65c59db492d1c3359d032b5f8a62af8b) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) base, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Bosch M\_CAN driver front-end callback helper for clearing memory mapped Message RAM. |
| int | [can\_mcan\_read\_reg](#a05e01d009f6cb08f7e8497c9e2ee83ef) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | Read a Bosch M\_CAN register. |
| int | [can\_mcan\_write\_reg](#a3f3e4be50fbf2c7ffcba99a1ca5ca7e1) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Write a Bosch M\_CAN register. |
| static int | [can\_mcan\_read\_mram](#a1705a740e811f1065538c733498fc16f) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read from Bosch M\_CAN Message RAM. |
| static int | [can\_mcan\_write\_mram](#ad2b88658a2294af890c56a99fee4a999) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write to Bosch M\_CAN Message RAM. |
| static int | [can\_mcan\_clear\_mram](#aa330897ffad0a9e1b4f08aaaa22e5c70) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Clear Bosch M\_CAN Message RAM. |
| int | [can\_mcan\_configure\_mram](#a2f9186fc69fe80b76133ab0f82100fc8) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) mrba, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) mram) |
|  | Configure Bosch M\_MCAN Message RAM start addresses. |
| int | [can\_mcan\_init](#a7d9006cb2e91f6b13c3d245612b175f0) (const struct [device](structdevice.md) \*dev) |
|  | Bosch M\_CAN driver initialization callback. |
| void | [can\_mcan\_line\_0\_isr](#a004d1a9aabc5307e6ab51a477f33c070) (const struct [device](structdevice.md) \*dev) |
|  | Bosch M\_CAN driver m\_can\_int0 IRQ handler. |
| void | [can\_mcan\_line\_1\_isr](#a41e134fc94a573622eac9314f87dd673) (const struct [device](structdevice.md) \*dev) |
|  | Bosch M\_CAN driver m\_can\_int1 IRQ handler. |
| void | [can\_mcan\_enable\_configuration\_change](#a54f0e66b1b1912d841e10e68e01331fa) (const struct [device](structdevice.md) \*dev) |
|  | Enable Bosch M\_CAN configuration change. |
| int | [can\_mcan\_get\_capabilities](#abc9c13ee4f4b47d4ff74ab4c6352bbe1) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap) |
|  | Bosch M\_CAN driver callback API upon getting CAN controller capabilities See *[can\_get\_capabilities()](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168 "Get the supported modes of the CAN controller.")* for argument description. |
| int | [can\_mcan\_start](#abcbc1ab4765005ec8acfd15921b065fd) (const struct [device](structdevice.md) \*dev) |
|  | Bosch M\_CAN driver callback API upon starting CAN controller See *[can\_start()](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a "Start the CAN controller.")* for argument description. |
| int | [can\_mcan\_stop](#a47d2f53639584c8fb4d65995e98ad77f) (const struct [device](structdevice.md) \*dev) |
|  | Bosch M\_CAN driver callback API upon stopping CAN controller See *[can\_stop()](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5 "Stop the CAN controller.")* for argument description. |
| int | [can\_mcan\_set\_mode](#a1264c5d49f0eeee5e3656560e7b2fb65) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode) |
|  | Bosch M\_CAN driver callback API upon setting CAN controller mode See *[can\_set\_mode()](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f "Set the CAN controller to the given operation mode.")* for argument description. |
| int | [can\_mcan\_set\_timing](#a33156b2282136192117cb663a4e64ea3) (const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing) |
|  | Bosch M\_CAN driver callback API upon setting CAN bus timing See *[can\_set\_timing()](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da "Configure the bus timing of a CAN controller.")* for argument description. |
| int | [can\_mcan\_set\_timing\_data](#a1fd00ba6a4023631c8589763049e05e9) (const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing\_data) |
|  | Bosch M\_CAN driver callback API upon setting CAN bus data phase timing See *[can\_set\_timing\_data()](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2 "Configure the bus timing for the data phase of a CAN FD controller.")* for argument description. |
| int | [can\_mcan\_send](#a906568f3922bf3cf39eb9ac9e78d58ae) (const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame, [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback, void \*user\_data) |
| int | [can\_mcan\_get\_max\_filters](#ac627d35c23322c003fa846866cfb6419) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ide) |
| int | [can\_mcan\_add\_rx\_filter](#a6a215a77fada5caafd7fb0da72308d95) (const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback, void \*user\_data, const struct [can\_filter](structcan__filter.md) \*filter) |
|  | Bosch M\_CAN driver callback API upon adding an RX filter See *can\_add\_rx\_callback()* for argument description. |
| void | [can\_mcan\_remove\_rx\_filter](#ae1a44958756509d882d6202cc337197e) (const struct [device](structdevice.md) \*dev, int filter\_id) |
|  | Bosch M\_CAN driver callback API upon removing an RX filter See *[can\_remove\_rx\_filter()](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847 "Remove a CAN RX filter.")* for argument description. |
| int | [can\_mcan\_get\_state](#a40e0f8f7ec696c62dd132fed45a4da5d) (const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt) |
|  | Bosch M\_CAN driver callback API upon getting the CAN controller state See *[can\_get\_state()](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857 "Get current CAN controller state.")* for argument description. |
| void | [can\_mcan\_set\_state\_change\_callback](#a324735380014b09f4e1fb33ff0c539cd) (const struct [device](structdevice.md) \*dev, [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback, void \*user\_data) |
|  | Bosch M\_CAN driver callback API upon setting a state change callback See *[can\_set\_state\_change\_callback()](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e "Set a callback for CAN controller state change events.")* for argument description. |

## Macro Definition Documentation

## [◆ ](#ab5e7cb2c8423200a929544a18ad66c2a)CAN\_MCAN\_CALLBACKS\_DEFINE

| #define CAN\_MCAN\_CALLBACKS\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_tx*, |
|  |  |  | *\_std*, |
|  |  |  | *\_ext* ) |

**Value:**

static struct [can\_mcan\_tx\_callback](structcan__mcan__tx__callback.md) \_name##\_tx\_cbs[\_tx]; \

static struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md) \_name##\_std\_cbs[\_std]; \

static struct [can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md) \_name##\_ext\_cbs[\_ext]; \

static const struct [can\_mcan\_callbacks](structcan__mcan__callbacks.md) \_name = { \

.tx = \_name##\_tx\_cbs, \

.[std](structcan__mcan__callbacks.md#ae225638097e1ddb5270de06401490a7f) = \_name##\_std\_cbs, \

.[ext](structcan__mcan__callbacks.md#ab29bb0963a78fcc68677ff5e4589f004) = \_name##\_ext\_cbs, \

.[num\_tx](structcan__mcan__callbacks.md#aad1b8f0b76637e7a53ef5c88118d7bd1) = \_tx, \

.num\_std = \_std, \

.num\_ext = \_ext, \

}

[can\_mcan\_callbacks](structcan__mcan__callbacks.md)

Bosch M\_CAN driver internal Tx + Rx callbacks structure.

**Definition** can\_mcan.h:1172

[can\_mcan\_callbacks::num\_tx](structcan__mcan__callbacks.md#aad1b8f0b76637e7a53ef5c88118d7bd1)

uint8\_t num\_tx

**Definition** can\_mcan.h:1176

[can\_mcan\_callbacks::ext](structcan__mcan__callbacks.md#ab29bb0963a78fcc68677ff5e4589f004)

struct can\_mcan\_rx\_callback \* ext

**Definition** can\_mcan.h:1175

[can\_mcan\_callbacks::std](structcan__mcan__callbacks.md#ae225638097e1ddb5270de06401490a7f)

struct can\_mcan\_rx\_callback \* std

**Definition** can\_mcan.h:1174

[can\_mcan\_rx\_callback](structcan__mcan__rx__callback.md)

Bosch M\_CAN driver internal Rx callback structure.

**Definition** can\_mcan.h:1164

[can\_mcan\_tx\_callback](structcan__mcan__tx__callback.md)

Bosch M\_CAN driver internal Tx callback structure.

**Definition** can\_mcan.h:1156

Define Bosch M\_CAN TX and RX callbacks.

This macro allows a Bosch M\_CAN driver frontend using a fixed Message RAM configuration to limit the required software resources (e.g. limit the number of the standard (11-bit) or extended (29-bit) filters in use).

Frontend drivers supporting dynamic Message RAM configuration should use [CAN\_MCAN\_DT\_CALLBACKS\_DEFINE()](#a8264915913cfdb4cd7fe5d53cb6cf64b) or [CAN\_MCAN\_DT\_INST\_CALLBACKS\_DEFINE()](#a93e84f959d380f927473ca3b9510d7bc) instead.

Parameters
:   | \_name | callbacks variable name |
    | --- | --- |
    | \_tx | Number of Tx callbacks |
    | \_std | Number of standard (11-bit) filter callbacks |
    | \_ext | Number of extended (29-bit) filter callbacks |

See also
:   [CAN\_MCAN\_DT\_CALLBACKS\_DEFINE()](#a8264915913cfdb4cd7fe5d53cb6cf64b)

## [◆ ](#a33d42748a911e6a337324652ac982c9b)CAN\_MCAN\_CCCR

| #define CAN\_MCAN\_CCCR   0x018 |
| --- |

## [◆ ](#a40e186041bf0459f6d1fdf5736670e56)CAN\_MCAN\_CCCR\_ASM

| #define CAN\_MCAN\_CCCR\_ASM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ace20dbd7d279909999e19dd2a6a82ec9)CAN\_MCAN\_CCCR\_BRSE

| #define CAN\_MCAN\_CCCR\_BRSE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#ad36bcf2dfbe848fbcbd930055a442cca)CAN\_MCAN\_CCCR\_CCE

| #define CAN\_MCAN\_CCCR\_CCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a249d3b8483bb7869e2695ee56a8c40e9)CAN\_MCAN\_CCCR\_CSA

| #define CAN\_MCAN\_CCCR\_CSA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a39b308a89655c9a59050cffbd2ad3268)CAN\_MCAN\_CCCR\_CSR

| #define CAN\_MCAN\_CCCR\_CSR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a2f4a7a67f69310b2470c2939cf7488d2)CAN\_MCAN\_CCCR\_DAR

| #define CAN\_MCAN\_CCCR\_DAR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#ab773d5e87290745fb1958d23720cfbdb)CAN\_MCAN\_CCCR\_EFBI

| #define CAN\_MCAN\_CCCR\_EFBI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#a26154a84a6124bd8cceae4c0929d6937)CAN\_MCAN\_CCCR\_FDOE

| #define CAN\_MCAN\_CCCR\_FDOE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#ab7fbe359b62fa11288390c0ed6b22d39)CAN\_MCAN\_CCCR\_INIT

| #define CAN\_MCAN\_CCCR\_INIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a1057947a0482c69e67f32f79b0f0cf56)CAN\_MCAN\_CCCR\_MON

| #define CAN\_MCAN\_CCCR\_MON   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a430a606d5de2f7cf5958fe1d88ce931e)CAN\_MCAN\_CCCR\_NISO

| #define CAN\_MCAN\_CCCR\_NISO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#ac5283b03eb7b498fd64e01477bfff300)CAN\_MCAN\_CCCR\_PXHD

| #define CAN\_MCAN\_CCCR\_PXHD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#af74a4cf81df6d88f8a69db622d71da83)CAN\_MCAN\_CCCR\_TEST

| #define CAN\_MCAN\_CCCR\_TEST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#ae091024f68ea83d6f888bcadb99e137c)CAN\_MCAN\_CCCR\_TXP

| #define CAN\_MCAN\_CCCR\_TXP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

## [◆ ](#a7c424b839fd4ebe69fa9615bc3cb7268)CAN\_MCAN\_CCCR\_UTSU

| #define CAN\_MCAN\_CCCR\_UTSU   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#aab0183fea6cd4dd560b83b2d2049bd75)CAN\_MCAN\_CCCR\_WMM

| #define CAN\_MCAN\_CCCR\_WMM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#acc741a42cb2d052ae773aebb95e44616)CAN\_MCAN\_CREL

| #define CAN\_MCAN\_CREL   0x000 |
| --- |

## [◆ ](#a89eebb76c2b98f12e56eaf3885cae9e5)CAN\_MCAN\_CREL\_DAY

| #define CAN\_MCAN\_CREL\_DAY   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| --- |

## [◆ ](#abc36710e20ac587cacf18e1e74434e6d)CAN\_MCAN\_CREL\_MON

| #define CAN\_MCAN\_CREL\_MON   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8) |
| --- |

## [◆ ](#a8cedb6b6ed4ace3a38f170fc4ce65647)CAN\_MCAN\_CREL\_REL

| #define CAN\_MCAN\_CREL\_REL   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 28) |
| --- |

## [◆ ](#a39282c299129a3a7e902c6a120568bce)CAN\_MCAN\_CREL\_STEP

| #define CAN\_MCAN\_CREL\_STEP   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(27, 24) |
| --- |

## [◆ ](#ac28c0effa82ad6fefad5dd5c9079800a)CAN\_MCAN\_CREL\_SUBSTEP

| #define CAN\_MCAN\_CREL\_SUBSTEP   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 20) |
| --- |

## [◆ ](#a7139e7a57e58fe4f8572c5d7784e67d2)CAN\_MCAN\_CREL\_YEAR

| #define CAN\_MCAN\_CREL\_YEAR   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 16) |
| --- |

## [◆ ](#a60dab0513bb60fdaaeb3ad9eb8589b0b)CAN\_MCAN\_CUST

| #define CAN\_MCAN\_CUST   0x008 |
| --- |

## [◆ ](#aa85321c44c2f8ce6f4e3abfecaac4309)CAN\_MCAN\_CUST\_CUST

| #define CAN\_MCAN\_CUST\_CUST   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#a0684e639e58ecd6e7f8188cea455d4d8)CAN\_MCAN\_DATA\_INITIALIZER

| #define CAN\_MCAN\_DATA\_INITIALIZER | ( |  | *\_custom* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

.custom = \_custom, \

}

Initializer for a *[can\_mcan\_data](structcan__mcan__data.md "Bosch M_CAN driver internal data structure.")* struct.

Parameters
:   | \_custom | Pointer to custom driver frontend data structure |
    | --- | --- |

## [◆ ](#a3643ab9ba53749dd417515e868005822)CAN\_MCAN\_DBTP

| #define CAN\_MCAN\_DBTP   0x00C |
| --- |

## [◆ ](#a1697f9a668977dae709f6f5c5c06cec0)CAN\_MCAN\_DBTP\_DBRP

| #define CAN\_MCAN\_DBTP\_DBRP   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(20, 16) |
| --- |

## [◆ ](#a010cfca29045f0f643cdacefb6560491)CAN\_MCAN\_DBTP\_DSJW

| #define CAN\_MCAN\_DBTP\_DSJW   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| --- |

## [◆ ](#a79af67b99451850bbfb3b6fe3f9a1502)CAN\_MCAN\_DBTP\_DTSEG1

| #define CAN\_MCAN\_DBTP\_DTSEG1   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 8) |
| --- |

## [◆ ](#a4f6a9528366c7ed61d6b9e5c1fe6e52d)CAN\_MCAN\_DBTP\_DTSEG2

| #define CAN\_MCAN\_DBTP\_DTSEG2   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 4) |
| --- |

## [◆ ](#a553232f28f3dcba55eb2e71619cceb10)CAN\_MCAN\_DBTP\_TDC

| #define CAN\_MCAN\_DBTP\_TDC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| --- |

## [◆ ](#af277dd5f60b0620b3ffc5030f0c794f6)CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG

| #define CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

BUILD\_ASSERT([CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS](#a87442fd647be89575fbd0e3a6a4f2540)(node\_id) <= 128, \

"Maximum Standard filter elements exceeded"); \

BUILD\_ASSERT([CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS](#a8c5ca10a9d376f42cecdb4fcaa1c2f86)(node\_id) <= 64, \

"Maximum Extended filter elements exceeded"); \

BUILD\_ASSERT([CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS](#a5b814febb2893a33617455a070f1814f)(node\_id) <= 64, \

"Maximum Rx FIFO 0 elements exceeded"); \

BUILD\_ASSERT([CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS](#a71941bfd0f048401fd1208d556260f32)(node\_id) <= 64, \

"Maximum Rx FIFO 1 elements exceeded"); \

BUILD\_ASSERT([CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS](#ad2371b27de938b29f42d2991a3f1009f)(node\_id) <= 64, \

"Maximum Rx Buffer elements exceeded"); \

BUILD\_ASSERT([CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS](#abbdb679ab26eb135d43dcc2394bded71)(node\_id) <= 32, \

"Maximum Tx Buffer elements exceeded"); \

BUILD\_ASSERT([CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS](#a7d725b5c696acbc394547800a5e729ae)(node\_id) <= 32, \

"Maximum Tx Buffer elements exceeded");

[CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS](#a5b814febb2893a33617455a070f1814f)

#define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(node\_id)

Get the number of Rx FIFO 0 elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:460

[CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS](#a71941bfd0f048401fd1208d556260f32)

#define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(node\_id)

Get the number of Rx FIFO 1 elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:469

[CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS](#a7d725b5c696acbc394547800a5e729ae)

#define CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(node\_id)

Get the number of Tx Buffer elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:496

[CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS](#a87442fd647be89575fbd0e3a6a4f2540)

#define CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(node\_id)

Get the number of standard (11-bit) filter elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:442

[CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS](#a8c5ca10a9d376f42cecdb4fcaa1c2f86)

#define CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(node\_id)

Get the number of extended (29-bit) filter elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:451

[CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS](#abbdb679ab26eb135d43dcc2394bded71)

#define CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(node\_id)

Get the number of Tx Event FIFO elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:487

[CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS](#ad2371b27de938b29f42d2991a3f1009f)

#define CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(node\_id)

Get the number of Rx Buffer elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:478

Assert that the Message RAM configuration meets the Bosch M\_CAN IP core restrictions.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

## [◆ ](#a8264915913cfdb4cd7fe5d53cb6cf64b)CAN\_MCAN\_DT\_CALLBACKS\_DEFINE

| #define CAN\_MCAN\_DT\_CALLBACKS\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_name* ) |

**Value:**

[CAN\_MCAN\_CALLBACKS\_DEFINE](#ab5e7cb2c8423200a929544a18ad66c2a)(\_name, [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS](#a7d725b5c696acbc394547800a5e729ae)(node\_id), \

[CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS](#a87442fd647be89575fbd0e3a6a4f2540)(node\_id), \

[CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS](#a8c5ca10a9d376f42cecdb4fcaa1c2f86)(node\_id))

[CAN\_MCAN\_CALLBACKS\_DEFINE](#ab5e7cb2c8423200a929544a18ad66c2a)

#define CAN\_MCAN\_CALLBACKS\_DEFINE(\_name, \_tx, \_std, \_ext)

Define Bosch M\_CAN TX and RX callbacks.

**Definition** can\_mcan.h:1197

Define Bosch M\_CAN TX and RX callbacks.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | \_name | callbacks variable name |

See also
:   [CAN\_MCAN\_CALLBACKS\_DEFINE()](#ab5e7cb2c8423200a929544a18ad66c2a)

## [◆ ](#a6ebe5c51c603b5b820682e291df06ac8)CAN\_MCAN\_DT\_CONFIG\_GET

| #define CAN\_MCAN\_DT\_CONFIG\_GET | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_custom*, |
|  |  |  | *\_ops*, |
|  |  |  | *\_cbs* ) |

**Value:**

{ \

.common = CAN\_DT\_DRIVER\_CONFIG\_GET(node\_id, 0, 1000000), \

.ops = \_ops, \

.callbacks = \_cbs, \

.mram\_elements = [CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET](#a2e52150401d29533258224a14600b255)(node\_id), \

.mram\_offsets = [CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET](#a907c70d4c64353647bf1718c45e11c5a)(node\_id), \

.mram\_size = [CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE](#a47fa1c0ca484d6f891c4834071d421e4)(node\_id), \

.custom = \_custom, \

}

[CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET](#a2e52150401d29533258224a14600b255)

#define CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET(node\_id)

Get an array containing the number of elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:1251

[CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE](#a47fa1c0ca484d6f891c4834071d421e4)

#define CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE(node\_id)

Get the total size of all Bosch M\_CAN Message RAM elements.

**Definition** can\_mcan.h:627

[CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET](#a907c70d4c64353647bf1718c45e11c5a)

#define CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET(node\_id)

Get an array containing the base offsets for element in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:1271

Static initializer for `[can_mcan_config](structcan__mcan__config.md "Bosch M_CAN driver internal configuration structure.")` struct.

Parameters
:   | node\_id | Devicetree node identifier |
    | --- | --- |
    | \_custom | Pointer to custom driver frontend configuration structure |
    | \_ops | Pointer to front-end *[can\_mcan\_ops](structcan__mcan__ops.md "Bosch M_CAN driver front-end operations.")* |
    | \_cbs | Pointer to front-end *[can\_mcan\_callbacks](structcan__mcan__callbacks.md "Bosch M_CAN driver internal Tx + Rx callbacks structure.")* |

## [◆ ](#af001b33da9876cbde179757687d25ec0)CAN\_MCAN\_DT\_CONFIG\_INST\_GET

| #define CAN\_MCAN\_DT\_CONFIG\_INST\_GET | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *\_custom*, |
|  |  |  | *\_ops*, |
|  |  |  | *\_cbs* ) |

**Value:**

[CAN\_MCAN\_DT\_CONFIG\_GET](#a6ebe5c51c603b5b820682e291df06ac8)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_custom, \_ops, \_cbs)

[CAN\_MCAN\_DT\_CONFIG\_GET](#a6ebe5c51c603b5b820682e291df06ac8)

#define CAN\_MCAN\_DT\_CONFIG\_GET(node\_id, \_custom, \_ops, \_cbs)

Static initializer for can\_mcan\_config struct.

**Definition** can\_mcan.h:1303

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

Static initializer for `[can_mcan_config](structcan__mcan__config.md "Bosch M_CAN driver internal configuration structure.")` struct from DT\_DRV\_COMPAT instance.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | \_custom | Pointer to custom driver frontend configuration structure |
    | \_ops | Pointer to front-end *[can\_mcan\_ops](structcan__mcan__ops.md "Bosch M_CAN driver front-end operations.")* |
    | \_cbs | Pointer to front-end *[can\_mcan\_callbacks](structcan__mcan__callbacks.md "Bosch M_CAN driver internal Tx + Rx callbacks structure.")* |

See also
:   [CAN\_MCAN\_DT\_CONFIG\_GET()](#a6ebe5c51c603b5b820682e291df06ac8)

## [◆ ](#a67daccd5aed8a4de6fc7489592a6b268)CAN\_MCAN\_DT\_INST\_BUILD\_ASSERT\_MRAM\_CFG

| #define CAN\_MCAN\_DT\_INST\_BUILD\_ASSERT\_MRAM\_CFG | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG](#af277dd5f60b0620b3ffc5030f0c794f6)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG](#af277dd5f60b0620b3ffc5030f0c794f6)

#define CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG(node\_id)

Assert that the Message RAM configuration meets the Bosch M\_CAN IP core restrictions.

**Definition** can\_mcan.h:650

Equivalent to [CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG(DT\_DRV\_INST(inst))](#af277dd5f60b0620b3ffc5030f0c794f6).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

See also
:   [CAN\_MCAN\_DT\_BUILD\_ASSERT\_MRAM\_CFG()](#af277dd5f60b0620b3ffc5030f0c794f6)

## [◆ ](#a93e84f959d380f927473ca3b9510d7bc)CAN\_MCAN\_DT\_INST\_CALLBACKS\_DEFINE

| #define CAN\_MCAN\_DT\_INST\_CALLBACKS\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *\_name* ) |

**Value:**

[CAN\_MCAN\_DT\_CALLBACKS\_DEFINE](#a8264915913cfdb4cd7fe5d53cb6cf64b)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_name)

[CAN\_MCAN\_DT\_CALLBACKS\_DEFINE](#a8264915913cfdb4cd7fe5d53cb6cf64b)

#define CAN\_MCAN\_DT\_CALLBACKS\_DEFINE(node\_id, \_name)

Define Bosch M\_CAN TX and RX callbacks.

**Definition** can\_mcan.h:1216

Equivalent to [CAN\_MCAN\_DT\_CALLBACKS\_DEFINE(DT\_DRV\_INST(inst))](#a8264915913cfdb4cd7fe5d53cb6cf64b).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | \_name | callbacks variable name |

See also
:   [CAN\_MCAN\_DT\_CALLBACKS\_DEFINE()](#a8264915913cfdb4cd7fe5d53cb6cf64b)

## [◆ ](#affa0cab849e56fe5016bc4aa8b43a1d1)CAN\_MCAN\_DT\_INST\_MCAN\_ADDR

| #define CAN\_MCAN\_DT\_INST\_MCAN\_ADDR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MCAN\_ADDR](#aaed34aa27da9ac0948d8b6ab798c7170)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MCAN\_ADDR](#aaed34aa27da9ac0948d8b6ab798c7170)

#define CAN\_MCAN\_DT\_MCAN\_ADDR(node\_id)

Get the Bosch M\_CAN register base address.

**Definition** can\_mcan.h:579

Equivalent to [CAN\_MCAN\_DT\_MCAN\_ADDR(DT\_DRV\_INST(inst))](#aaed34aa27da9ac0948d8b6ab798c7170).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the Bosch M\_CAN register base address

See also
:   [CAN\_MCAN\_DT\_MRAM\_ADDR()](#acecc9210d2504ba1dda108a79a2afb78)

## [◆ ](#a6fee1c336a0c7de5d8cda6bf2338ad3c)CAN\_MCAN\_DT\_INST\_MRAM\_ADDR

| #define CAN\_MCAN\_DT\_INST\_MRAM\_ADDR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_ADDR](#acecc9210d2504ba1dda108a79a2afb78)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_ADDR](#acecc9210d2504ba1dda108a79a2afb78)

#define CAN\_MCAN\_DT\_MRAM\_ADDR(node\_id)

Get the Bosch M\_CAN Message RAM address.

**Definition** can\_mcan.h:604

Equivalent to [CAN\_MCAN\_DT\_MRAM\_ADDR(DT\_DRV\_INST(inst))](#acecc9210d2504ba1dda108a79a2afb78).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the Bosch M\_CAN Message RAM address

See also
:   [CAN\_MCAN\_DT\_MRAM\_ADDR()](#acecc9210d2504ba1dda108a79a2afb78)

## [◆ ](#a6081976c4a78765061c3832253e2bcda)CAN\_MCAN\_DT\_INST\_MRAM\_DEFINE

| #define CAN\_MCAN\_DT\_INST\_MRAM\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *\_name* ) |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_DEFINE](#a146911ec873fd653f8f9538a85202917)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_name)

[CAN\_MCAN\_DT\_MRAM\_DEFINE](#a146911ec873fd653f8f9538a85202917)

#define CAN\_MCAN\_DT\_MRAM\_DEFINE(node\_id, \_name)

Define a RAM buffer for Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:641

Equivalent to [CAN\_MCAN\_DT\_MRAM\_DEFINE(DT\_DRV\_INST(inst))](#a146911ec873fd653f8f9538a85202917).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | \_name | buffer variable name |

See also
:   [CAN\_MCAN\_DT\_MRAM\_DEFINE()](#a146911ec873fd653f8f9538a85202917)

## [◆ ](#a5d0cc45852e301e4e38652218a5fc594)CAN\_MCAN\_DT\_INST\_MRAM\_ELEMENTS\_SIZE

| #define CAN\_MCAN\_DT\_INST\_MRAM\_ELEMENTS\_SIZE | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE](#a47fa1c0ca484d6f891c4834071d421e4)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Equivalent to [CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE(DT\_DRV\_INST(inst))](#a47fa1c0ca484d6f891c4834071d421e4).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the total size of all Message RAM elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE()](#a47fa1c0ca484d6f891c4834071d421e4)

## [◆ ](#aac3f321fee276c68e51073dfbcd81150)CAN\_MCAN\_DT\_INST\_MRAM\_EXT\_FILTER\_ELEMENTS

| #define CAN\_MCAN\_DT\_INST\_MRAM\_EXT\_FILTER\_ELEMENTS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS](#a8c5ca10a9d376f42cecdb4fcaa1c2f86)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Equivalent to [CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(DT\_DRV\_INST(inst))](#a8c5ca10a9d376f42cecdb4fcaa1c2f86).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the number of extended (29-bit) elements

See also
:   [CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS()](#a8c5ca10a9d376f42cecdb4fcaa1c2f86)

## [◆ ](#a8595df90a5c45639ae9e576dcc61ea0d)CAN\_MCAN\_DT\_INST\_MRAM\_EXT\_FILTER\_OFFSET

| #define CAN\_MCAN\_DT\_INST\_MRAM\_EXT\_FILTER\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET](#a71687f621eae0d9f930ede70cb99cff7)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET](#a71687f621eae0d9f930ede70cb99cff7)

#define CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET(node\_id)

Get the base offset of extended (29-bit) filter elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:513

Equivalent to [CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET(DT\_DRV\_INST(inst))](#a71687f621eae0d9f930ede70cb99cff7).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the base offset of extended (29-bit) filter elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET()](#a71687f621eae0d9f930ede70cb99cff7)

## [◆ ](#a3095ec5dd938ab990c71c06b5ba84d03)CAN\_MCAN\_DT\_INST\_MRAM\_OFFSET

| #define CAN\_MCAN\_DT\_INST\_MRAM\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_OFFSET](#a06194f088174c2634bd318aaaddca988)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_OFFSET](#a06194f088174c2634bd318aaaddca988)

#define CAN\_MCAN\_DT\_MRAM\_OFFSET(node\_id)

Get the Bosch M\_CAN Message RAM offset.

**Definition** can\_mcan.h:433

Equivalent to [CAN\_MCAN\_DT\_MRAM\_OFFSET(DT\_DRV\_INST(inst))](#a06194f088174c2634bd318aaaddca988).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the Message RAM offset in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_OFFSET()](#a06194f088174c2634bd318aaaddca988)

## [◆ ](#aa2a372c40cce733d10d9b33651cfdb1c)CAN\_MCAN\_DT\_INST\_MRAM\_RX\_BUFFER\_ELEMENTS

| #define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_BUFFER\_ELEMENTS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS](#ad2371b27de938b29f42d2991a3f1009f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(DT\_DRV\_INST(inst))](#ad2371b27de938b29f42d2991a3f1009f).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the number of Rx Buffer elements

See also
:   [CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS()](#ad2371b27de938b29f42d2991a3f1009f)

## [◆ ](#aea15c0e894fdbacaeead2d108c7c0b94)CAN\_MCAN\_DT\_INST\_MRAM\_RX\_BUFFER\_OFFSET

| #define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_BUFFER\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET](#aa0d25966039a769edd9b8b4f31af2c9f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET](#aa0d25966039a769edd9b8b4f31af2c9f)

#define CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET(node\_id)

Get the base offset of Rx Buffer elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:543

Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET(DT\_DRV\_INST(inst))](#aa0d25966039a769edd9b8b4f31af2c9f).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the base offset of Rx Buffer elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET()](#aa0d25966039a769edd9b8b4f31af2c9f)

## [◆ ](#a393289abde09b6190964fe69f2529c27)CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO0\_ELEMENTS

| #define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO0\_ELEMENTS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS](#a5b814febb2893a33617455a070f1814f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(DT\_DRV\_INST(inst))](#a5b814febb2893a33617455a070f1814f).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the number of Rx FIFO 0 elements

See also
:   [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS()](#a5b814febb2893a33617455a070f1814f)

## [◆ ](#a48fe93b1bd51cdb7dcb1312ee160eab7)CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO0\_OFFSET

| #define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO0\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET](#a79b1f334979e5d7f180b6f37fbcb772f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET](#a79b1f334979e5d7f180b6f37fbcb772f)

#define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET(node\_id)

Get the base offset of Rx FIFO 0 elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:523

Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET(DT\_DRV\_INST(inst))](#a79b1f334979e5d7f180b6f37fbcb772f).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the base offset of Rx FIFO 0 elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET()](#a79b1f334979e5d7f180b6f37fbcb772f)

## [◆ ](#a30eef08af0433049ed28c51d640d3679)CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO1\_ELEMENTS

| #define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO1\_ELEMENTS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS](#a71941bfd0f048401fd1208d556260f32)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(DT\_DRV\_INST(inst))](#a71941bfd0f048401fd1208d556260f32).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the number of Rx FIFO 1 elements

See also
:   [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS()](#a71941bfd0f048401fd1208d556260f32)

## [◆ ](#ad80049c12ef02f78736268f9abb7c303)CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO1\_OFFSET

| #define CAN\_MCAN\_DT\_INST\_MRAM\_RX\_FIFO1\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET](#aa4c0f6e4696d3c82344bd099eb0dcd13)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET](#aa4c0f6e4696d3c82344bd099eb0dcd13)

#define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET(node\_id)

Get the base offset of Rx FIFO 1 elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:533

Equivalent to [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET(DT\_DRV\_INST(inst))](#aa4c0f6e4696d3c82344bd099eb0dcd13).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the base offset of Rx FIFO 1 elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET()](#aa4c0f6e4696d3c82344bd099eb0dcd13)

## [◆ ](#a63e750530c43000bafa36a808582f9d4)CAN\_MCAN\_DT\_INST\_MRAM\_SIZE

| #define CAN\_MCAN\_DT\_INST\_MRAM\_SIZE | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_SIZE](#a94743f60c64c64a1e2bfd78fcc864cf1)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_SIZE](#a94743f60c64c64a1e2bfd78fcc864cf1)

#define CAN\_MCAN\_DT\_MRAM\_SIZE(node\_id)

Get the Bosch M\_CAN Message RAM size.

**Definition** can\_mcan.h:617

Equivalent to [CAN\_MCAN\_DT\_MRAM\_SIZE(DT\_DRV\_INST(inst))](#a94743f60c64c64a1e2bfd78fcc864cf1).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the Bosch M\_CAN Message RAM size in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_SIZE()](#a94743f60c64c64a1e2bfd78fcc864cf1)

## [◆ ](#a41d9d7f70dfedbe8eeacfd27a8610007)CAN\_MCAN\_DT\_INST\_MRAM\_STD\_FILTER\_ELEMENTS

| #define CAN\_MCAN\_DT\_INST\_MRAM\_STD\_FILTER\_ELEMENTS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS](#a87442fd647be89575fbd0e3a6a4f2540)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Equivalent to [CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(DT\_DRV\_INST(inst))](#a87442fd647be89575fbd0e3a6a4f2540).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the number of standard (11-bit) elements

See also
:   [CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS()](#a87442fd647be89575fbd0e3a6a4f2540)

## [◆ ](#a9c7a3869df9defc3f466f8de89b86561)CAN\_MCAN\_DT\_INST\_MRAM\_STD\_FILTER\_OFFSET

| #define CAN\_MCAN\_DT\_INST\_MRAM\_STD\_FILTER\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET](#a4c6c3b23eed2ae336882cbfbb69d8578)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET](#a4c6c3b23eed2ae336882cbfbb69d8578)

#define CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET(node\_id)

Get the base offset of standard (11-bit) filter elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:505

Equivalent to [CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET(DT\_DRV\_INST(inst))](#a4c6c3b23eed2ae336882cbfbb69d8578).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the base offset of standard (11-bit) filter elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET()](#a4c6c3b23eed2ae336882cbfbb69d8578)

## [◆ ](#aa4275ca727057cdf4a0fe486b87d238d)CAN\_MCAN\_DT\_INST\_MRAM\_TX\_BUFFER\_ELEMENTS

| #define CAN\_MCAN\_DT\_INST\_MRAM\_TX\_BUFFER\_ELEMENTS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS](#a7d725b5c696acbc394547800a5e729ae)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Equivalent to [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(DT\_DRV\_INST(inst))](#a7d725b5c696acbc394547800a5e729ae).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the number of Tx Buffer elements

See also
:   [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS()](#a7d725b5c696acbc394547800a5e729ae)

## [◆ ](#a9bb9a0d6d8b3de3e24d533ec15c1215d)CAN\_MCAN\_DT\_INST\_MRAM\_TX\_BUFFER\_OFFSET

| #define CAN\_MCAN\_DT\_INST\_MRAM\_TX\_BUFFER\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET](#a1f3384686c23982de8acef2182597e69)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET](#a1f3384686c23982de8acef2182597e69)

#define CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET(node\_id)

Get the base offset of Tx Buffer elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:563

Equivalent to [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET(DT\_DRV\_INST(inst))](#a1f3384686c23982de8acef2182597e69).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the base offset of Tx Buffer elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET()](#a1f3384686c23982de8acef2182597e69)

## [◆ ](#ae10a6c1414a951808e818728e5d74e52)CAN\_MCAN\_DT\_INST\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS

| #define CAN\_MCAN\_DT\_INST\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS](#abbdb679ab26eb135d43dcc2394bded71)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Equivalent to [CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(DT\_DRV\_INST(inst))](#abbdb679ab26eb135d43dcc2394bded71).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the number of Tx Event FIFO elements

See also
:   [CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS()](#abbdb679ab26eb135d43dcc2394bded71)

## [◆ ](#a63623852de6c5dd34509823446db1af9)CAN\_MCAN\_DT\_INST\_MRAM\_TX\_EVENT\_FIFO\_OFFSET

| #define CAN\_MCAN\_DT\_INST\_MRAM\_TX\_EVENT\_FIFO\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET](#a16ce04fda8d800582ccc1b6979d34ac4)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET](#a16ce04fda8d800582ccc1b6979d34ac4)

#define CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(node\_id)

Get the base offset of Tx Event FIFO elements in Bosch M\_CAN Message RAM.

**Definition** can\_mcan.h:553

Equivalent to [CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(DT\_DRV\_INST(inst))](#a16ce04fda8d800582ccc1b6979d34ac4).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the base offset of Tx Event FIFO elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET()](#a16ce04fda8d800582ccc1b6979d34ac4)

## [◆ ](#a25b114591fdf1330865adfa7706cd62b)CAN\_MCAN\_DT\_INST\_MRBA

| #define CAN\_MCAN\_DT\_INST\_MRBA | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CAN\_MCAN\_DT\_MRBA](#ad7d854278909e12accdef06f2dc7a490)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[CAN\_MCAN\_DT\_MRBA](#ad7d854278909e12accdef06f2dc7a490)

#define CAN\_MCAN\_DT\_MRBA(node\_id)

Get the Bosch M\_CAN Message RAM base address.

**Definition** can\_mcan.h:592

Equivalent to [CAN\_MCAN\_DT\_MRBA(DT\_DRV\_INST(inst))](#ad7d854278909e12accdef06f2dc7a490).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the Bosch M\_CAN Message RAM Base Address (MRBA)

See also
:   [CAN\_MCAN\_DT\_MRBA()](#ad7d854278909e12accdef06f2dc7a490)

## [◆ ](#aaed34aa27da9ac0948d8b6ab798c7170)CAN\_MCAN\_DT\_MCAN\_ADDR

| #define CAN\_MCAN\_DT\_MCAN\_ADDR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NUM\_REGS](group__devicetree-reg-prop.md#ga6cdd22b6a2881b09ed63d9d262566a0a)(node\_id), (([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0))[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id)), \

(([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0))[DT\_REG\_ADDR\_BY\_NAME](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)(node\_id, m\_can)))

[DT\_NUM\_REGS](group__devicetree-reg-prop.md#ga6cdd22b6a2881b09ed63d9d262566a0a)

#define DT\_NUM\_REGS(node\_id)

Get the number of register blocks in the reg property.

**Definition** devicetree.h:2345

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2433

[DT\_REG\_ADDR\_BY\_NAME](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)

#define DT\_REG\_ADDR\_BY\_NAME(node\_id, name)

Get a register block's base address by name.

**Definition** devicetree.h:2462

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

Get the Bosch M\_CAN register base address.

For devicetree nodes with just one register block, this macro returns the base address of that register block.

If a devicetree node has more than one register block, this macros returns the base address of the register block named "m\_can".

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the Bosch M\_CAN register base address

## [◆ ](#acecc9210d2504ba1dda108a79a2afb78)CAN\_MCAN\_DT\_MRAM\_ADDR

| #define CAN\_MCAN\_DT\_MRAM\_ADDR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d))([CAN\_MCAN\_DT\_MRBA](#ad7d854278909e12accdef06f2dc7a490)(node\_id) + [CAN\_MCAN\_DT\_MRAM\_OFFSET](#a06194f088174c2634bd318aaaddca988)(node\_id))

[mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d)

uintptr\_t mem\_addr\_t

**Definition** sys\_io.h:21

Get the Bosch M\_CAN Message RAM address.

For devicetree nodes with dedicated Message RAM area defined via devicetree, this macro returns the address of the Message RAM, taking in the Message RAM offset into account.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the Bosch M\_CAN Message RAM address

## [◆ ](#a146911ec873fd653f8f9538a85202917)CAN\_MCAN\_DT\_MRAM\_DEFINE

| #define CAN\_MCAN\_DT\_MRAM\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_name* ) |

**Value:**

BUILD\_ASSERT([CAN\_MCAN\_DT\_MRAM\_OFFSET](#a06194f088174c2634bd318aaaddca988)(node\_id) == 0, "offset must be 0"); \

static char \_\_nocache\_noinit \_\_aligned(4) \_name[[CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE](#a47fa1c0ca484d6f891c4834071d421e4)(node\_id)];

Define a RAM buffer for Bosch M\_CAN Message RAM.

For devicetree nodes without dedicated Message RAM area, this macro defines a suitable RAM buffer to hold the Message RAM elements. Since this buffer cannot be shared between multiple Bosch M\_CAN instances, the Message RAM offset must be set to 0x0.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | \_name | buffer variable name |

## [◆ ](#a2e52150401d29533258224a14600b255)CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET

| #define CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

0, /\* offset cell \*/ \

CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(node\_id), \

CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(node\_id), \

CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(node\_id), \

CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(node\_id), \

CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(node\_id), \

CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(node\_id), \

CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(node\_id) \

}

Get an array containing the number of elements in Bosch M\_CAN Message RAM.

The order of the array entries is given by the [CAN\_MCAN\_MRAM\_CFG](#CAN_MCAN_MRAM_CFG) definitions.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   array of number of elements

## [◆ ](#a47fa1c0ca484d6f891c4834071d421e4)CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE

| #define CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET](#a1f3384686c23982de8acef2182597e69)(node\_id) + \

CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS(node\_id) \* sizeof(struct [can\_mcan\_tx\_buffer](structcan__mcan__tx__buffer.md)))

[can\_mcan\_tx\_buffer](structcan__mcan__tx__buffer.md)

Bosch M\_CAN Tx Buffer Element.

**Definition** can\_mcan.h:978

Get the total size of all Bosch M\_CAN Message RAM elements.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the total size of all Message RAM elements in bytes

See also
:   [CAN\_MCAN\_DT\_MRAM\_SIZE()](#a94743f60c64c64a1e2bfd78fcc864cf1)

## [◆ ](#a8c5ca10a9d376f42cecdb4fcaa1c2f86)CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS

| #define CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, bosch\_mram\_cfg, [CAN\_MCAN\_MRAM\_CFG\_EXT\_FILTER](#a9a43d8d379fee72d0c46841538b22e91))

[CAN\_MCAN\_MRAM\_CFG\_EXT\_FILTER](#a9a43d8d379fee72d0c46841538b22e91)

#define CAN\_MCAN\_MRAM\_CFG\_EXT\_FILTER

ext-filter-elements cell index

**Definition** can\_mcan.h:411

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:891

Get the number of extended (29-bit) filter elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the number of extended (29-bit) filter elements

## [◆ ](#a71687f621eae0d9f930ede70cb99cff7)CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET

| #define CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET](#a4c6c3b23eed2ae336882cbfbb69d8578)(node\_id) + \

CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS(node\_id) \* sizeof(struct [can\_mcan\_std\_filter](structcan__mcan__std__filter.md)))

[can\_mcan\_std\_filter](structcan__mcan__std__filter.md)

Bosch M\_CAN Standard Message ID Filter Element.

**Definition** can\_mcan.h:1033

Get the base offset of extended (29-bit) filter elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the base offset of extended (29-bit) filter elements in bytes

## [◆ ](#a06194f088174c2634bd318aaaddca988)CAN\_MCAN\_DT\_MRAM\_OFFSET

| #define CAN\_MCAN\_DT\_MRAM\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, bosch\_mram\_cfg, [CAN\_MCAN\_MRAM\_CFG\_OFFSET](#a1b2e247424c436244e795ef253840d58))

[CAN\_MCAN\_MRAM\_CFG\_OFFSET](#a1b2e247424c436244e795ef253840d58)

#define CAN\_MCAN\_MRAM\_CFG\_OFFSET

offset cell index

**Definition** can\_mcan.h:407

Get the Bosch M\_CAN Message RAM offset.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the Message RAM offset in bytes

## [◆ ](#a907c70d4c64353647bf1718c45e11c5a)CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET

| #define CAN\_MCAN\_DT\_MRAM\_OFFSETS\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

0, /\* offset cell \*/ \

CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET(node\_id), \

CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET(node\_id), \

CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET(node\_id), \

CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET(node\_id), \

CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET(node\_id), \

CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET(node\_id), \

CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET(node\_id) \

}

Get an array containing the base offsets for element in Bosch M\_CAN Message RAM.

The order of the array entries is given by the [CAN\_MCAN\_MRAM\_CFG](#CAN_MCAN_MRAM_CFG) definitions.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   array of base offsets for elements

## [◆ ](#ad2371b27de938b29f42d2991a3f1009f)CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS

| #define CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, bosch\_mram\_cfg, [CAN\_MCAN\_MRAM\_CFG\_RX\_BUFFER](#aa1c3bbb17546a5c8daaf5c80e028e1bf))

[CAN\_MCAN\_MRAM\_CFG\_RX\_BUFFER](#aa1c3bbb17546a5c8daaf5c80e028e1bf)

#define CAN\_MCAN\_MRAM\_CFG\_RX\_BUFFER

rx-buffer-elements cell index

**Definition** can\_mcan.h:417

Get the number of Rx Buffer elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the number of Rx Buffer elements

## [◆ ](#aa0d25966039a769edd9b8b4f31af2c9f)CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET

| #define CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET](#aa4c0f6e4696d3c82344bd099eb0dcd13)(node\_id) + \

CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS(node\_id) \* sizeof(struct [can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md)))

[can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md)

Bosch M\_CAN Rx Buffer and FIFO Element.

**Definition** can\_mcan.h:937

Get the base offset of Rx Buffer elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the base offset of Rx Buffer elements in bytes

## [◆ ](#a5b814febb2893a33617455a070f1814f)CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS

| #define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, bosch\_mram\_cfg, [CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO0](#aacc3d7a9ace66c6322a07186a72324ef))

[CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO0](#aacc3d7a9ace66c6322a07186a72324ef)

#define CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO0

rx-fifo0-elements cell index

**Definition** can\_mcan.h:413

Get the number of Rx FIFO 0 elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the number of Rx FIFO 0 elements

## [◆ ](#a79b1f334979e5d7f180b6f37fbcb772f)CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET

| #define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_OFFSET](#a71687f621eae0d9f930ede70cb99cff7)(node\_id) + \

CAN\_MCAN\_DT\_MRAM\_EXT\_FILTER\_ELEMENTS(node\_id) \* sizeof(struct [can\_mcan\_ext\_filter](structcan__mcan__ext__filter.md)))

[can\_mcan\_ext\_filter](structcan__mcan__ext__filter.md)

Bosch M\_CAN Extended Message ID Filter Element.

**Definition** can\_mcan.h:1052

Get the base offset of Rx FIFO 0 elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the base offset of Rx FIFO 0 elements in bytes

## [◆ ](#a71941bfd0f048401fd1208d556260f32)CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS

| #define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_ELEMENTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, bosch\_mram\_cfg, [CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO1](#a6bdc1012af79c50869279a7caac4ff31))

[CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO1](#a6bdc1012af79c50869279a7caac4ff31)

#define CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO1

rx-fifo1-elements cell index

**Definition** can\_mcan.h:415

Get the number of Rx FIFO 1 elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the number of Rx FIFO 1 elements

## [◆ ](#aa4c0f6e4696d3c82344bd099eb0dcd13)CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET

| #define CAN\_MCAN\_DT\_MRAM\_RX\_FIFO1\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_OFFSET](#a79b1f334979e5d7f180b6f37fbcb772f)(node\_id) + \

CAN\_MCAN\_DT\_MRAM\_RX\_FIFO0\_ELEMENTS(node\_id) \* sizeof(struct [can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md)))

Get the base offset of Rx FIFO 1 elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the base offset of Rx FIFO 1 elements in bytes

## [◆ ](#a94743f60c64c64a1e2bfd78fcc864cf1)CAN\_MCAN\_DT\_MRAM\_SIZE

| #define CAN\_MCAN\_DT\_MRAM\_SIZE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d))([DT\_REG\_SIZE\_BY\_NAME](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)(node\_id, message\_ram) - [CAN\_MCAN\_DT\_MRAM\_OFFSET](#a06194f088174c2634bd318aaaddca988)(node\_id))

[DT\_REG\_SIZE\_BY\_NAME](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)

#define DT\_REG\_SIZE\_BY\_NAME(node\_id, name)

Get a register block's size by name.

**Definition** devicetree.h:2498

Get the Bosch M\_CAN Message RAM size.

For devicetree nodes with dedicated Message RAM area defined via devicetree, this macro returns the size of the Message RAM, taking in the Message RAM offset into account.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the Bosch M\_CAN Message RAM base address

See also
:   [CAN\_MCAN\_DT\_MRAM\_ELEMENTS\_SIZE()](#a47fa1c0ca484d6f891c4834071d421e4)

## [◆ ](#a87442fd647be89575fbd0e3a6a4f2540)CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS

| #define CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_ELEMENTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, bosch\_mram\_cfg, [CAN\_MCAN\_MRAM\_CFG\_STD\_FILTER](#a651e96118352208ff4a5b041f051d10f))

[CAN\_MCAN\_MRAM\_CFG\_STD\_FILTER](#a651e96118352208ff4a5b041f051d10f)

#define CAN\_MCAN\_MRAM\_CFG\_STD\_FILTER

std-filter-elements cell index

**Definition** can\_mcan.h:409

Get the number of standard (11-bit) filter elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the number of standard (11-bit) filter elements

## [◆ ](#a4c6c3b23eed2ae336882cbfbb69d8578)CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET

| #define CAN\_MCAN\_DT\_MRAM\_STD\_FILTER\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(0U)

Get the base offset of standard (11-bit) filter elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the base offset of standard (11-bit) filter elements in bytes

## [◆ ](#a7d725b5c696acbc394547800a5e729ae)CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS

| #define CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_ELEMENTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, bosch\_mram\_cfg, [CAN\_MCAN\_MRAM\_CFG\_TX\_BUFFER](#ab18faf8f17480060d0102bb9370378c1))

[CAN\_MCAN\_MRAM\_CFG\_TX\_BUFFER](#ab18faf8f17480060d0102bb9370378c1)

#define CAN\_MCAN\_MRAM\_CFG\_TX\_BUFFER

tx-buffer-elements cell index

**Definition** can\_mcan.h:421

Get the number of Tx Buffer elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the number of Tx Buffer elements

## [◆ ](#a1f3384686c23982de8acef2182597e69)CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET

| #define CAN\_MCAN\_DT\_MRAM\_TX\_BUFFER\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET](#a16ce04fda8d800582ccc1b6979d34ac4)(node\_id) + \

CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS(node\_id) \* sizeof(struct [can\_mcan\_tx\_event\_fifo](structcan__mcan__tx__event__fifo.md)))

[can\_mcan\_tx\_event\_fifo](structcan__mcan__tx__event__fifo.md)

Bosch M\_CAN Tx Event FIFO Element.

**Definition** can\_mcan.h:991

Get the base offset of Tx Buffer elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the base offset of Tx Buffer elements in bytes

## [◆ ](#abbdb679ab26eb135d43dcc2394bded71)CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS

| #define CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_ELEMENTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, bosch\_mram\_cfg, [CAN\_MCAN\_MRAM\_CFG\_TX\_EVENT\_FIFO](#a35fbb5986ca2268dd650b00970da363d))

[CAN\_MCAN\_MRAM\_CFG\_TX\_EVENT\_FIFO](#a35fbb5986ca2268dd650b00970da363d)

#define CAN\_MCAN\_MRAM\_CFG\_TX\_EVENT\_FIFO

tx-event-fifo-elements cell index

**Definition** can\_mcan.h:419

Get the number of Tx Event FIFO elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the number of Tx Event FIFO elements

## [◆ ](#a16ce04fda8d800582ccc1b6979d34ac4)CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET

| #define CAN\_MCAN\_DT\_MRAM\_TX\_EVENT\_FIFO\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_OFFSET](#aa0d25966039a769edd9b8b4f31af2c9f)(node\_id) + \

CAN\_MCAN\_DT\_MRAM\_RX\_BUFFER\_ELEMENTS(node\_id) \* sizeof(struct [can\_mcan\_rx\_fifo](structcan__mcan__rx__fifo.md)))

Get the base offset of Tx Event FIFO elements in Bosch M\_CAN Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the base offset of Tx Event FIFO elements in bytes

## [◆ ](#ad7d854278909e12accdef06f2dc7a490)CAN\_MCAN\_DT\_MRBA

| #define CAN\_MCAN\_DT\_MRBA | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d))[DT\_REG\_ADDR\_BY\_NAME](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)(node\_id, message\_ram)

Get the Bosch M\_CAN Message RAM base address.

For devicetree nodes with dedicated Message RAM area defined via devicetree, this macro returns the base address of the Message RAM.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the Bosch M\_CAN Message RAM base address (MRBA)

## [◆ ](#aee893904e384ad6b56311078d9546190)CAN\_MCAN\_ECR

| #define CAN\_MCAN\_ECR   0x040 |
| --- |

## [◆ ](#a6df87229481d209acb54a719447dad47)CAN\_MCAN\_ECR\_CEL

| #define CAN\_MCAN\_ECR\_CEL   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 16) |
| --- |

## [◆ ](#ae0a477450ccd40c6a1de4c6bcd3a5997)CAN\_MCAN\_ECR\_REC

| #define CAN\_MCAN\_ECR\_REC   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(14, 8) |
| --- |

## [◆ ](#a0be04930627b22f80d548fd367cb847d)CAN\_MCAN\_ECR\_RP

| #define CAN\_MCAN\_ECR\_RP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#afb635c07c2664e72c64ae614f2d60f94)CAN\_MCAN\_ECR\_TEC

| #define CAN\_MCAN\_ECR\_TEC   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| --- |

## [◆ ](#aa04e5c32ec68157807013ae542339c34)CAN\_MCAN\_EFT\_CLASSIC

| #define CAN\_MCAN\_EFT\_CLASSIC   0x2 |
| --- |

## [◆ ](#aaa5fe73386232cef16ffb79561064200)CAN\_MCAN\_EFT\_DUAL

| #define CAN\_MCAN\_EFT\_DUAL   0x1 |
| --- |

## [◆ ](#ae0ebf402133070f34c942230f0ae9f6a)CAN\_MCAN\_EFT\_RANGE

| #define CAN\_MCAN\_EFT\_RANGE   0x3 |
| --- |

## [◆ ](#a2391eb72cedd2f2cc17959c73bb1afb4)CAN\_MCAN\_EFT\_RANGE\_XIDAM

| #define CAN\_MCAN\_EFT\_RANGE\_XIDAM   0x0 |
| --- |

## [◆ ](#ae130ab74797ec4affc8052a334995dd8)CAN\_MCAN\_ENDN

| #define CAN\_MCAN\_ENDN   0x004 |
| --- |

## [◆ ](#a1dcceef7aa2e13c90551e677a32f836b)CAN\_MCAN\_ENDN\_ETV

| #define CAN\_MCAN\_ENDN\_ETV   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#acedea2dc6c2eaa750196ea330028137d)CAN\_MCAN\_GFC

| #define CAN\_MCAN\_GFC   0x080 |
| --- |

## [◆ ](#a1ecb99bb847bb0305ca2720c18f77ae1)CAN\_MCAN\_GFC\_ANFE

| #define CAN\_MCAN\_GFC\_ANFE   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 2) |
| --- |

## [◆ ](#ad8f1ee3bcf1ce148ecc604177777fe36)CAN\_MCAN\_GFC\_ANFS

| #define CAN\_MCAN\_GFC\_ANFS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 4) |
| --- |

## [◆ ](#af72ebd1644ee7651b6755dbc2d999da1)CAN\_MCAN\_GFC\_RRFE

| #define CAN\_MCAN\_GFC\_RRFE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a719015ab076274c8f71a574975a6a1c9)CAN\_MCAN\_GFC\_RRFS

| #define CAN\_MCAN\_GFC\_RRFS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a13f990a79472988c3b9b8f9b17795b93)CAN\_MCAN\_HPMS

| #define CAN\_MCAN\_HPMS   0x094 |
| --- |

## [◆ ](#a870c4e0a0829eb9ce24fb14c62383e44)CAN\_MCAN\_HPMS\_BIDX

| #define CAN\_MCAN\_HPMS\_BIDX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| --- |

## [◆ ](#a15a0a60646ea281d06aeebf4f94655c5)CAN\_MCAN\_HPMS\_FIDX

| #define CAN\_MCAN\_HPMS\_FIDX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(14, 8) |
| --- |

## [◆ ](#a016ae0f271581c7f77fb3eede5866ab7)CAN\_MCAN\_HPMS\_FLST

| #define CAN\_MCAN\_HPMS\_FLST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#a8d47e3cb602ffd092e7da40d2268bc87)CAN\_MCAN\_HPMS\_MSI

| #define CAN\_MCAN\_HPMS\_MSI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 6) |
| --- |

## [◆ ](#a5efcfd38d911a09ba1a0e8546127d73e)CAN\_MCAN\_IE

| #define CAN\_MCAN\_IE   0x054 |
| --- |

## [◆ ](#a87e7dc8db720db25d80a9464ae0a9a0f)CAN\_MCAN\_IE\_ARAE

| #define CAN\_MCAN\_IE\_ARAE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) |
| --- |

## [◆ ](#a8e2fc398be6df304991143af43ae4ed3)CAN\_MCAN\_IE\_BECE

| #define CAN\_MCAN\_IE\_BECE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| --- |

## [◆ ](#a7748c310633b29084ff3673aff28e749)CAN\_MCAN\_IE\_BEUE

| #define CAN\_MCAN\_IE\_BEUE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| --- |

## [◆ ](#a7adbce95af6bb9efbf20188ebf6584f7)CAN\_MCAN\_IE\_BOE

| #define CAN\_MCAN\_IE\_BOE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| --- |

## [◆ ](#a14f6823f3ee219eafc5370f6bd9cc839)CAN\_MCAN\_IE\_DRXE

| #define CAN\_MCAN\_IE\_DRXE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| --- |

## [◆ ](#aeb78e4ebe0c9522accc5836d2a9f33d1)CAN\_MCAN\_IE\_ELOE

| #define CAN\_MCAN\_IE\_ELOE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22) |
| --- |

## [◆ ](#aaf858f5603f46e886d2a255d027e2057)CAN\_MCAN\_IE\_EPE

| #define CAN\_MCAN\_IE\_EPE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| --- |

## [◆ ](#a5727d4efbe75dbbb022b3df9f64134ae)CAN\_MCAN\_IE\_EWE

| #define CAN\_MCAN\_IE\_EWE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| --- |

## [◆ ](#a626e0d5094618d3d45a3d614598c426a)CAN\_MCAN\_IE\_HPME

| #define CAN\_MCAN\_IE\_HPME   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a8570c8e17b23bd00f3d3e671ecdc0301)CAN\_MCAN\_IE\_MRAFE

| #define CAN\_MCAN\_IE\_MRAFE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| --- |

## [◆ ](#aec30af8e9ea090c3d896c8d815f5fb18)CAN\_MCAN\_IE\_PEAE

| #define CAN\_MCAN\_IE\_PEAE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| --- |

## [◆ ](#a5894eb34123a83e13763525c7725cacb)CAN\_MCAN\_IE\_PEDE

| #define CAN\_MCAN\_IE\_PEDE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) |
| --- |

## [◆ ](#a42b4e6e1a7138f356bdb2c5ed87eea95)CAN\_MCAN\_IE\_RF0FE

| #define CAN\_MCAN\_IE\_RF0FE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a72eb6ded2dcd94d3785887fef5f231a1)CAN\_MCAN\_IE\_RF0LE

| #define CAN\_MCAN\_IE\_RF0LE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#af31e0711f5628614ce69969c14c78fb8)CAN\_MCAN\_IE\_RF0NE

| #define CAN\_MCAN\_IE\_RF0NE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a85118c1d03eadd4a6a76cf935fbe17bc)CAN\_MCAN\_IE\_RF0WE

| #define CAN\_MCAN\_IE\_RF0WE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a10bba01222375ae38f049ee8abc50973)CAN\_MCAN\_IE\_RF1FE

| #define CAN\_MCAN\_IE\_RF1FE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a7c535f93189d8d5f41320e6fa364a005)CAN\_MCAN\_IE\_RF1LE

| #define CAN\_MCAN\_IE\_RF1LE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a39f3b5000f6290513d723b3bf8869aba)CAN\_MCAN\_IE\_RF1NE

| #define CAN\_MCAN\_IE\_RF1NE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#af399bd4422077374595d152dee4e7860)CAN\_MCAN\_IE\_RF1WE

| #define CAN\_MCAN\_IE\_RF1WE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a7545997948206ff883a9f2cd9c327f35)CAN\_MCAN\_IE\_TCE

| #define CAN\_MCAN\_IE\_TCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a3f1f30cfdbffdc698d7c6ad94d8617db)CAN\_MCAN\_IE\_TCFE

| #define CAN\_MCAN\_IE\_TCFE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a61e51933d46002e468e3965fdd3100ce)CAN\_MCAN\_IE\_TEFFE

| #define CAN\_MCAN\_IE\_TEFFE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

## [◆ ](#a2ebfaf6bf1f175917a20fd47b2d241f0)CAN\_MCAN\_IE\_TEFLE

| #define CAN\_MCAN\_IE\_TEFLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#a5cca5bd86ccf8433b693daf805f150de)CAN\_MCAN\_IE\_TEFNE

| #define CAN\_MCAN\_IE\_TEFNE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#aa983e0f26d5454b297866a5778c09915)CAN\_MCAN\_IE\_TEFWE

| #define CAN\_MCAN\_IE\_TEFWE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#a5fd83f7f8b769c493b2b99fae7cf3bcf)CAN\_MCAN\_IE\_TFEE

| #define CAN\_MCAN\_IE\_TFEE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#adffa68a3e8e9186595f139e5b8f78025)CAN\_MCAN\_IE\_TOOE

| #define CAN\_MCAN\_IE\_TOOE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| --- |

## [◆ ](#a5d66c2cef0008cdb2b7faae4f838fde1)CAN\_MCAN\_IE\_TSWE

| #define CAN\_MCAN\_IE\_TSWE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| --- |

## [◆ ](#a80f67433f566f71224184fd6f4047096)CAN\_MCAN\_IE\_WDIE

| #define CAN\_MCAN\_IE\_WDIE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| --- |

## [◆ ](#a32e14f45e1c85a73e816a7a78477b703)CAN\_MCAN\_ILE

| #define CAN\_MCAN\_ILE   0x05C |
| --- |

## [◆ ](#a10be46e7dbc334e014d3a5126d2d8832)CAN\_MCAN\_ILE\_EINT0

| #define CAN\_MCAN\_ILE\_EINT0   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a9022d6b85f32310f57a8a711409b4beb)CAN\_MCAN\_ILE\_EINT1

| #define CAN\_MCAN\_ILE\_EINT1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a6d2a927e67ecb7c01749d6a0fbc25363)CAN\_MCAN\_ILS

| #define CAN\_MCAN\_ILS   0x058 |
| --- |

## [◆ ](#ac06e1958c3690032639849b9b291ca7f)CAN\_MCAN\_ILS\_ARAL

| #define CAN\_MCAN\_ILS\_ARAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) |
| --- |

## [◆ ](#adb5a621d293f0bde671a9246f67af57d)CAN\_MCAN\_ILS\_BECL

| #define CAN\_MCAN\_ILS\_BECL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| --- |

## [◆ ](#a4992a22be098fa66ae40119f88ae9c42)CAN\_MCAN\_ILS\_BEUL

| #define CAN\_MCAN\_ILS\_BEUL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| --- |

## [◆ ](#a4be2c784e04021c28fb0bda474af2008)CAN\_MCAN\_ILS\_BOL

| #define CAN\_MCAN\_ILS\_BOL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| --- |

## [◆ ](#a414c9f4b86e1f851b9f12356bc440236)CAN\_MCAN\_ILS\_DRXL

| #define CAN\_MCAN\_ILS\_DRXL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| --- |

## [◆ ](#a24400f4c04a26a183853dcd8c6401849)CAN\_MCAN\_ILS\_ELOL

| #define CAN\_MCAN\_ILS\_ELOL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22) |
| --- |

## [◆ ](#a49654d0bbf4af7dabf2bf89805177fb9)CAN\_MCAN\_ILS\_EPL

| #define CAN\_MCAN\_ILS\_EPL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| --- |

## [◆ ](#ac250560aafee73e83b7cc4db7333f037)CAN\_MCAN\_ILS\_EWL

| #define CAN\_MCAN\_ILS\_EWL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| --- |

## [◆ ](#a7922ad47535e02146816b07e0ee7c499)CAN\_MCAN\_ILS\_HPML

| #define CAN\_MCAN\_ILS\_HPML   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a6a139692dcf97de3500d4692119610e3)CAN\_MCAN\_ILS\_MRAFL

| #define CAN\_MCAN\_ILS\_MRAFL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| --- |

## [◆ ](#a78ce183fb2e265f8b850c52b2e0b9b83)CAN\_MCAN\_ILS\_PEAL

| #define CAN\_MCAN\_ILS\_PEAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| --- |

## [◆ ](#a1863554a941902bd0a585916b3016ec9)CAN\_MCAN\_ILS\_PEDL

| #define CAN\_MCAN\_ILS\_PEDL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) |
| --- |

## [◆ ](#a061b5b7c74b8a0afc0a78f01b1374e28)CAN\_MCAN\_ILS\_RF0FL

| #define CAN\_MCAN\_ILS\_RF0FL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ac7304d316f701ad6a0f66ca62cbbcf00)CAN\_MCAN\_ILS\_RF0LL

| #define CAN\_MCAN\_ILS\_RF0LL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#ad40a58d2e4240ce58f4da55ebf0756e5)CAN\_MCAN\_ILS\_RF0NL

| #define CAN\_MCAN\_ILS\_RF0NL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a389d1fe76759d470fb8af80698b4708f)CAN\_MCAN\_ILS\_RF0WL

| #define CAN\_MCAN\_ILS\_RF0WL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a0695d2cfd07a5717fb2e307b047567fe)CAN\_MCAN\_ILS\_RF1FL

| #define CAN\_MCAN\_ILS\_RF1FL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#ad1868981fcc7e414c75e005e93859343)CAN\_MCAN\_ILS\_RF1LL

| #define CAN\_MCAN\_ILS\_RF1LL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a182bc538b568b402370e02a969dd5bd9)CAN\_MCAN\_ILS\_RF1NL

| #define CAN\_MCAN\_ILS\_RF1NL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#ac70c241178121176bebdb4c13ec29c65)CAN\_MCAN\_ILS\_RF1WL

| #define CAN\_MCAN\_ILS\_RF1WL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#abfaf532cc23ba6f63149bc97dc3c855e)CAN\_MCAN\_ILS\_TCFL

| #define CAN\_MCAN\_ILS\_TCFL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#ab294335aa5dff81c72d89f4e6c2f506a)CAN\_MCAN\_ILS\_TCL

| #define CAN\_MCAN\_ILS\_TCL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a0c60df858386dbde519d03f448282177)CAN\_MCAN\_ILS\_TEFFL

| #define CAN\_MCAN\_ILS\_TEFFL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

## [◆ ](#abbe6c6994e95786e081b110c6fec56b3)CAN\_MCAN\_ILS\_TEFLL

| #define CAN\_MCAN\_ILS\_TEFLL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#af42996807b1747d5f08540b18c3fdf5a)CAN\_MCAN\_ILS\_TEFNL

| #define CAN\_MCAN\_ILS\_TEFNL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#aa3418486b5bdee960076c03c6310b47d)CAN\_MCAN\_ILS\_TEFWL

| #define CAN\_MCAN\_ILS\_TEFWL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#a287b7fec7f9917f18011994dc3329f5f)CAN\_MCAN\_ILS\_TFEL

| #define CAN\_MCAN\_ILS\_TFEL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#a3b37679278affda2b8b17a975c97a1cf)CAN\_MCAN\_ILS\_TOOL

| #define CAN\_MCAN\_ILS\_TOOL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| --- |

## [◆ ](#af1815cb8b62a185a739e23d4bbcedbc0)CAN\_MCAN\_ILS\_TSWL

| #define CAN\_MCAN\_ILS\_TSWL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| --- |

## [◆ ](#a28b9d67835f409299a7dbfddce41674e)CAN\_MCAN\_ILS\_WDIL

| #define CAN\_MCAN\_ILS\_WDIL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| --- |

## [◆ ](#acac62eeff461ebd9ac34b8d622dc8c6b)CAN\_MCAN\_IR

| #define CAN\_MCAN\_IR   0x050 |
| --- |

## [◆ ](#a732f9c3cb965a855c2e733bdadfcaa1e)CAN\_MCAN\_IR\_ARA

| #define CAN\_MCAN\_IR\_ARA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) |
| --- |

## [◆ ](#a86431445f96ec66f93828d78ba1311d6)CAN\_MCAN\_IR\_BEC

| #define CAN\_MCAN\_IR\_BEC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| --- |

## [◆ ](#a20653377f1565e71de286858ca920d46)CAN\_MCAN\_IR\_BEU

| #define CAN\_MCAN\_IR\_BEU   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| --- |

## [◆ ](#a62de51c28140a4e787363c2b579290f6)CAN\_MCAN\_IR\_BO

| #define CAN\_MCAN\_IR\_BO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| --- |

## [◆ ](#ab82d152424a84de470bfe005b577368c)CAN\_MCAN\_IR\_DRX

| #define CAN\_MCAN\_IR\_DRX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| --- |

## [◆ ](#a4c88361aa6d63fee591a2010d882107e)CAN\_MCAN\_IR\_ELO

| #define CAN\_MCAN\_IR\_ELO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22) |
| --- |

## [◆ ](#ada6d4f670b522c7fd1036721ddc2931a)CAN\_MCAN\_IR\_EP

| #define CAN\_MCAN\_IR\_EP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| --- |

## [◆ ](#a5f8cf54fee2939bc2f31c9e414ba202e)CAN\_MCAN\_IR\_EW

| #define CAN\_MCAN\_IR\_EW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| --- |

## [◆ ](#aee45488e19c8bbf86ffed780cc3565c3)CAN\_MCAN\_IR\_HPM

| #define CAN\_MCAN\_IR\_HPM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a00b7078b20f2aa81356694b84a179446)CAN\_MCAN\_IR\_MRAF

| #define CAN\_MCAN\_IR\_MRAF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| --- |

## [◆ ](#a60f1b085bb9a26d5a211e56f86ac5e86)CAN\_MCAN\_IR\_PEA

| #define CAN\_MCAN\_IR\_PEA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| --- |

## [◆ ](#aa737557f70c4da0a7e5660208d6764df)CAN\_MCAN\_IR\_PED

| #define CAN\_MCAN\_IR\_PED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) |
| --- |

## [◆ ](#a15214770d66f4bf0df92ed9457f5954f)CAN\_MCAN\_IR\_RF0F

| #define CAN\_MCAN\_IR\_RF0F   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a530db7342edd5f2f3254ce17745dcb88)CAN\_MCAN\_IR\_RF0L

| #define CAN\_MCAN\_IR\_RF0L   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#aef7cfda9d78ed8294e744c3c024e7ce9)CAN\_MCAN\_IR\_RF0N

| #define CAN\_MCAN\_IR\_RF0N   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#ab737ca9c1a8a152f58dd9d1d2a02790e)CAN\_MCAN\_IR\_RF0W

| #define CAN\_MCAN\_IR\_RF0W   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a10193930b296827f124dc98e49c7db2a)CAN\_MCAN\_IR\_RF1F

| #define CAN\_MCAN\_IR\_RF1F   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#ac37b42f53820384cc426b8b078572a35)CAN\_MCAN\_IR\_RF1L

| #define CAN\_MCAN\_IR\_RF1L   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#abed65c016f9adf3794a3fd0474fa84e3)CAN\_MCAN\_IR\_RF1N

| #define CAN\_MCAN\_IR\_RF1N   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a9bd64356ca32fef96e6680966e3d77b4)CAN\_MCAN\_IR\_RF1W

| #define CAN\_MCAN\_IR\_RF1W   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a880558d5672ef8d27bf232eeb739c3e0)CAN\_MCAN\_IR\_TC

| #define CAN\_MCAN\_IR\_TC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#ace4b4fbac614a38e70248aba6df71068)CAN\_MCAN\_IR\_TCF

| #define CAN\_MCAN\_IR\_TCF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a59e276fb6412ba5447994615049cb8fd)CAN\_MCAN\_IR\_TEFF

| #define CAN\_MCAN\_IR\_TEFF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

## [◆ ](#a090716d481b6e97d251aba9871ac0408)CAN\_MCAN\_IR\_TEFL

| #define CAN\_MCAN\_IR\_TEFL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

## [◆ ](#a5f7fa6444d1afe343920fe4495f64da5)CAN\_MCAN\_IR\_TEFN

| #define CAN\_MCAN\_IR\_TEFN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#a07fea07bd4ff7cfd4add4bedc0409e7a)CAN\_MCAN\_IR\_TEFW

| #define CAN\_MCAN\_IR\_TEFW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#a481a7b485091a9b862ec48a75315e12c)CAN\_MCAN\_IR\_TFE

| #define CAN\_MCAN\_IR\_TFE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#ab5066977fa160d3ded392b054d858637)CAN\_MCAN\_IR\_TOO

| #define CAN\_MCAN\_IR\_TOO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| --- |

## [◆ ](#a666e16b9ea27b83635067939aef62a31)CAN\_MCAN\_IR\_TSW

| #define CAN\_MCAN\_IR\_TSW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| --- |

## [◆ ](#a5adbd7ceb523237265ca3093bd921c20)CAN\_MCAN\_IR\_WDI

| #define CAN\_MCAN\_IR\_WDI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| --- |

## [◆ ](#a9a43d8d379fee72d0c46841538b22e91)CAN\_MCAN\_MRAM\_CFG\_EXT\_FILTER

| #define CAN\_MCAN\_MRAM\_CFG\_EXT\_FILTER   2 |
| --- |

ext-filter-elements cell index

## [◆ ](#abb4087b9c7ac31e8a1cb7003945dad97)CAN\_MCAN\_MRAM\_CFG\_NUM\_CELLS

| #define CAN\_MCAN\_MRAM\_CFG\_NUM\_CELLS   8 |
| --- |

Total number of cells in bosch,mram-cfg property.

## [◆ ](#a1b2e247424c436244e795ef253840d58)CAN\_MCAN\_MRAM\_CFG\_OFFSET

| #define CAN\_MCAN\_MRAM\_CFG\_OFFSET   0 |
| --- |

offset cell index

## [◆ ](#aa1c3bbb17546a5c8daaf5c80e028e1bf)CAN\_MCAN\_MRAM\_CFG\_RX\_BUFFER

| #define CAN\_MCAN\_MRAM\_CFG\_RX\_BUFFER   5 |
| --- |

rx-buffer-elements cell index

## [◆ ](#aacc3d7a9ace66c6322a07186a72324ef)CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO0

| #define CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO0   3 |
| --- |

rx-fifo0-elements cell index

## [◆ ](#a6bdc1012af79c50869279a7caac4ff31)CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO1

| #define CAN\_MCAN\_MRAM\_CFG\_RX\_FIFO1   4 |
| --- |

rx-fifo1-elements cell index

## [◆ ](#a651e96118352208ff4a5b041f051d10f)CAN\_MCAN\_MRAM\_CFG\_STD\_FILTER

| #define CAN\_MCAN\_MRAM\_CFG\_STD\_FILTER   1 |
| --- |

std-filter-elements cell index

## [◆ ](#ab18faf8f17480060d0102bb9370378c1)CAN\_MCAN\_MRAM\_CFG\_TX\_BUFFER

| #define CAN\_MCAN\_MRAM\_CFG\_TX\_BUFFER   7 |
| --- |

tx-buffer-elements cell index

## [◆ ](#a35fbb5986ca2268dd650b00970da363d)CAN\_MCAN\_MRAM\_CFG\_TX\_EVENT\_FIFO

| #define CAN\_MCAN\_MRAM\_CFG\_TX\_EVENT\_FIFO   6 |
| --- |

tx-event-fifo-elements cell index

## [◆ ](#a308c60c14b65b3416d36a37e7b70a318)CAN\_MCAN\_NBTP

| #define CAN\_MCAN\_NBTP   0x01C |
| --- |

## [◆ ](#a1285c541ff247a4bf26229e0b294af62)CAN\_MCAN\_NBTP\_NBRP

| #define CAN\_MCAN\_NBTP\_NBRP   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(24, 16) |
| --- |

## [◆ ](#abdd623bc3728e9e6c92d2b842c08d3e7)CAN\_MCAN\_NBTP\_NSJW

| #define CAN\_MCAN\_NBTP\_NSJW   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 25) |
| --- |

## [◆ ](#a1c18b64cb2e4f22afbd16a61aeb31d42)CAN\_MCAN\_NBTP\_NTSEG1

| #define CAN\_MCAN\_NBTP\_NTSEG1   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8) |
| --- |

## [◆ ](#a7c69e8e69f5b9bb61ad0342f8fde2d39)CAN\_MCAN\_NBTP\_NTSEG2

| #define CAN\_MCAN\_NBTP\_NTSEG2   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| --- |

## [◆ ](#a38c5b3177e25905cc78f7dbcee956f77)CAN\_MCAN\_NDAT1

| #define CAN\_MCAN\_NDAT1   0x098 |
| --- |

## [◆ ](#ac533f25e977b0eeb37cb5e047a7dd7f6)CAN\_MCAN\_NDAT1\_ND

| #define CAN\_MCAN\_NDAT1\_ND   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#afce0263a9bbe5901e3d5e0020282efda)CAN\_MCAN\_NDAT2

| #define CAN\_MCAN\_NDAT2   0x09C |
| --- |

## [◆ ](#ac443c986084e5bc0b618049f20193715)CAN\_MCAN\_NDAT2\_ND

| #define CAN\_MCAN\_NDAT2\_ND   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#a0e6bf5627ac886db479dd34693f8b7a6)CAN\_MCAN\_PSR

| #define CAN\_MCAN\_PSR   0x044 |
| --- |

## [◆ ](#a6afc5e82af45896e01af32e2b2c69993)CAN\_MCAN\_PSR\_ACT

| #define CAN\_MCAN\_PSR\_ACT   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 3) |
| --- |

## [◆ ](#a7b72bbe875c0b64e6c608ee2d0927658)CAN\_MCAN\_PSR\_BO

| #define CAN\_MCAN\_PSR\_BO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a346aa3ec31690010401d1d120dda7e4e)CAN\_MCAN\_PSR\_DLEC

| #define CAN\_MCAN\_PSR\_DLEC   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(10, 8) |
| --- |

## [◆ ](#a0cf95fc0ddc9b03b177730ae8f8a2128)CAN\_MCAN\_PSR\_EP

| #define CAN\_MCAN\_PSR\_EP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#ac8bf022df308ce6bd8797c36d39e0d36)CAN\_MCAN\_PSR\_EW

| #define CAN\_MCAN\_PSR\_EW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#ae49ca535c17a53562b7db3f897dc336a)CAN\_MCAN\_PSR\_LEC

| #define CAN\_MCAN\_PSR\_LEC   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| --- |

## [◆ ](#a0769c5c4ee9f406eed816a1104793a0a)CAN\_MCAN\_PSR\_PXE

| #define CAN\_MCAN\_PSR\_PXE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

## [◆ ](#ae6cc09fcf5145317c677294a6a8b888b)CAN\_MCAN\_PSR\_RBRS

| #define CAN\_MCAN\_PSR\_RBRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#acf2c2ff589d5e27335fa216a6df3abb6)CAN\_MCAN\_PSR\_RESI

| #define CAN\_MCAN\_PSR\_RESI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#a1fb264bdd3e56b11224dc11e2703ac09)CAN\_MCAN\_PSR\_RFDF

| #define CAN\_MCAN\_PSR\_RFDF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#a2133840d3eab9f8a5a881e5c37c3fed2)CAN\_MCAN\_PSR\_TDCV

| #define CAN\_MCAN\_PSR\_TDCV   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 16) |
| --- |

## [◆ ](#ab646e1d2f8a14239b31e54a4728bad81)CAN\_MCAN\_RWD

| #define CAN\_MCAN\_RWD   0x014 |
| --- |

## [◆ ](#a0a64ee92dd024b35047794c8cbb05f6a)CAN\_MCAN\_RWD\_WDC

| #define CAN\_MCAN\_RWD\_WDC   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| --- |

## [◆ ](#a639a100e4d8438784faeafdb20df0d35)CAN\_MCAN\_RWD\_WDV

| #define CAN\_MCAN\_RWD\_WDV   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8) |
| --- |

## [◆ ](#a9cb2ddc82fcfb102484577307c88481b)CAN\_MCAN\_RXBC

| #define CAN\_MCAN\_RXBC   0x0AC |
| --- |

## [◆ ](#ad7bf916dc45e84b85f6c895fefdb9e99)CAN\_MCAN\_RXBC\_RBSA

| #define CAN\_MCAN\_RXBC\_RBSA   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| --- |

## [◆ ](#a83c90feeec80071bc35b3dcce8f6be99)CAN\_MCAN\_RXESC

| #define CAN\_MCAN\_RXESC   0x0BC |
| --- |

## [◆ ](#a5e45adc0b6acba20391c6f5adc6c5ec3)CAN\_MCAN\_RXESC\_F0DS

| #define CAN\_MCAN\_RXESC\_F0DS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| --- |

## [◆ ](#ad8600748ee89bec9c7efe76e4a743ed7)CAN\_MCAN\_RXESC\_F1DS

| #define CAN\_MCAN\_RXESC\_F1DS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 4) |
| --- |

## [◆ ](#aff5420d9503e9ec130ad37a40021f738)CAN\_MCAN\_RXESC\_RBDS

| #define CAN\_MCAN\_RXESC\_RBDS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(10, 8) |
| --- |

## [◆ ](#addda3c98094c821fe63bf24782d140d1)CAN\_MCAN\_RXF0A

| #define CAN\_MCAN\_RXF0A   0x0A8 |
| --- |

## [◆ ](#ab806cb88a0961da39319c8db90a0bfb6)CAN\_MCAN\_RXF0A\_F0AI

| #define CAN\_MCAN\_RXF0A\_F0AI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| --- |

## [◆ ](#acafb4bdf5f41886fe05ab96ce9d3e40f)CAN\_MCAN\_RXF0C

| #define CAN\_MCAN\_RXF0C   0x0A0 |
| --- |

## [◆ ](#aa60d7075af7dc69fe61f7c9ed26b4db8)CAN\_MCAN\_RXF0C\_F0OM

| #define CAN\_MCAN\_RXF0C\_F0OM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| --- |

## [◆ ](#a36b805fdfa202f8ea7fc885a75f889a3)CAN\_MCAN\_RXF0C\_F0S

| #define CAN\_MCAN\_RXF0C\_F0S   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 16) |
| --- |

## [◆ ](#a2be907b2a04b58df30f5a4e4d2c0cbc0)CAN\_MCAN\_RXF0C\_F0SA

| #define CAN\_MCAN\_RXF0C\_F0SA   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| --- |

## [◆ ](#a407c6bb15b8f0c296004c5f2dffd1255)CAN\_MCAN\_RXF0C\_F0WM

| #define CAN\_MCAN\_RXF0C\_F0WM   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(30, 24) |
| --- |

## [◆ ](#a8af4d58a4ae713351c0c944bb4468359)CAN\_MCAN\_RXF0S

| #define CAN\_MCAN\_RXF0S   0x0A4 |
| --- |

## [◆ ](#aa8649180143ff827bc49a7789682b377)CAN\_MCAN\_RXF0S\_F0F

| #define CAN\_MCAN\_RXF0S\_F0F   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| --- |

## [◆ ](#ae8ab0a46f01834f07076750e909f099b)CAN\_MCAN\_RXF0S\_F0FL

| #define CAN\_MCAN\_RXF0S\_F0FL   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| --- |

## [◆ ](#acec1a9ead6d7e01e1178ea56a0d66b2e)CAN\_MCAN\_RXF0S\_F0GI

| #define CAN\_MCAN\_RXF0S\_F0GI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(13, 8) |
| --- |

## [◆ ](#ae3b41edffd1a7a8e8ddf96b450aac3ec)CAN\_MCAN\_RXF0S\_F0PI

| #define CAN\_MCAN\_RXF0S\_F0PI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| --- |

## [◆ ](#a2841566e304c9d151763000dbb5b2792)CAN\_MCAN\_RXF0S\_RF0L

| #define CAN\_MCAN\_RXF0S\_RF0L   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| --- |

## [◆ ](#af3101a1d476ed8304885c33367e19d0f)CAN\_MCAN\_RXF1A

| #define CAN\_MCAN\_RXF1A   0x0B8 |
| --- |

## [◆ ](#a190b1df18ce88e67dd24145d6bb4d899)CAN\_MCAN\_RXF1A\_F1AI

| #define CAN\_MCAN\_RXF1A\_F1AI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| --- |

## [◆ ](#a4b0612f2b06cf3af04fe969d97106cb5)CAN\_MCAN\_RXF1C

| #define CAN\_MCAN\_RXF1C   0x0B0 |
| --- |

## [◆ ](#a3f39ada97a9ebd6dcfe4d5bb9adfadee)CAN\_MCAN\_RXF1C\_F1OM

| #define CAN\_MCAN\_RXF1C\_F1OM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| --- |

## [◆ ](#a9f4dc18657f25ebd2463bf55af719f04)CAN\_MCAN\_RXF1C\_F1S

| #define CAN\_MCAN\_RXF1C\_F1S   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 16) |
| --- |

## [◆ ](#a23131c2ea676b9a913be4fce2ca8cf9e)CAN\_MCAN\_RXF1C\_F1SA

| #define CAN\_MCAN\_RXF1C\_F1SA   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| --- |

## [◆ ](#a65cd1948f37dbc67fa85dde655a997b3)CAN\_MCAN\_RXF1C\_F1WM

| #define CAN\_MCAN\_RXF1C\_F1WM   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(30, 24) |
| --- |

## [◆ ](#a63a683d44b63affa919963adf94f755c)CAN\_MCAN\_RXF1S

| #define CAN\_MCAN\_RXF1S   0x0B4 |
| --- |

## [◆ ](#a407843916f140d8bbd2546eb1f1955e6)CAN\_MCAN\_RXF1S\_F1F

| #define CAN\_MCAN\_RXF1S\_F1F   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| --- |

## [◆ ](#aaf8df87b128358e2b211c6000b389d64)CAN\_MCAN\_RXF1S\_F1FL

| #define CAN\_MCAN\_RXF1S\_F1FL   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| --- |

## [◆ ](#aaed234ff229b28f3f0926468d9fd32af)CAN\_MCAN\_RXF1S\_F1GI

| #define CAN\_MCAN\_RXF1S\_F1GI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(13, 8) |
| --- |

## [◆ ](#a8bf02cc958131a3a25218058159bb2bf)CAN\_MCAN\_RXF1S\_F1PI

| #define CAN\_MCAN\_RXF1S\_F1PI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| --- |

## [◆ ](#a5f55e6eeff595af1f6f1eaeedfb9b62d)CAN\_MCAN\_RXF1S\_RF1L

| #define CAN\_MCAN\_RXF1S\_RF1L   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| --- |

## [◆ ](#a7d5274ba0f020deda315bd10da7787ce)CAN\_MCAN\_SFT\_CLASSIC

| #define CAN\_MCAN\_SFT\_CLASSIC   0x2 |
| --- |

## [◆ ](#ac64298dffd12e5f148438af6b2c9f578)CAN\_MCAN\_SFT\_DISABLED

| #define CAN\_MCAN\_SFT\_DISABLED   0x3 |
| --- |

## [◆ ](#aadfcd6a191d8eb4c2f0403cba4518a8e)CAN\_MCAN\_SFT\_DUAL

| #define CAN\_MCAN\_SFT\_DUAL   0x1 |
| --- |

## [◆ ](#a39fcb587e3a98e256fd70af2408d1fc4)CAN\_MCAN\_SFT\_RANGE

| #define CAN\_MCAN\_SFT\_RANGE   0x0 |
| --- |

## [◆ ](#a27a0bbdaa9b9bfba7227dbe1350f2c74)CAN\_MCAN\_SIDFC

| #define CAN\_MCAN\_SIDFC   0x084 |
| --- |

## [◆ ](#ac73011c520eea37b4ca36da8259b3f77)CAN\_MCAN\_SIDFC\_FLSSA

| #define CAN\_MCAN\_SIDFC\_FLSSA   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| --- |

## [◆ ](#a906b8e66d3294d68ebdff6a7c5283526)CAN\_MCAN\_SIDFC\_LSS

| #define CAN\_MCAN\_SIDFC\_LSS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 16) |
| --- |

## [◆ ](#a52cea0ef00b1bf53a4f718104a3ad652)CAN\_MCAN\_TDCR

| #define CAN\_MCAN\_TDCR   0x048 |
| --- |

## [◆ ](#ae2f0c4a34055d37e49710f594f1736cc)CAN\_MCAN\_TDCR\_TDCF

| #define CAN\_MCAN\_TDCR\_TDCF   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| --- |

## [◆ ](#ab0a27684c90c1b5828206cd2f034802b)CAN\_MCAN\_TDCR\_TDCO

| #define CAN\_MCAN\_TDCR\_TDCO   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(14, 8) |
| --- |

## [◆ ](#ad97d62d4799b07bc5a8405f7ace52708)CAN\_MCAN\_TEST

| #define CAN\_MCAN\_TEST   0x010 |
| --- |

## [◆ ](#aee2a84f2613145af78c97da48781382e)CAN\_MCAN\_TEST\_LBCK

| #define CAN\_MCAN\_TEST\_LBCK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a8210ab176d182b1b1fec7f5fc8f6e44e)CAN\_MCAN\_TEST\_PVAL

| #define CAN\_MCAN\_TEST\_PVAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

## [◆ ](#ad4110c5f53f0632694aebef5eab54a54)CAN\_MCAN\_TEST\_RX

| #define CAN\_MCAN\_TEST\_RX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#aa8ad1bcbf0ce358b91810f5349bab4db)CAN\_MCAN\_TEST\_SVAL

| #define CAN\_MCAN\_TEST\_SVAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| --- |

## [◆ ](#a207ba0562c9e4e4a10cdee1ad524a1c0)CAN\_MCAN\_TEST\_TX

| #define CAN\_MCAN\_TEST\_TX   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 5) |
| --- |

## [◆ ](#aaf9280049a3e2365f9ec7627009989f1)CAN\_MCAN\_TEST\_TXBNP

| #define CAN\_MCAN\_TEST\_TXBNP   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 8) |
| --- |

## [◆ ](#a28c34733629bef3c9e83add27ceca147)CAN\_MCAN\_TEST\_TXBNS

| #define CAN\_MCAN\_TEST\_TXBNS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(20, 16) |
| --- |

## [◆ ](#aa0f79f1ce18146a1ad90609e4020308c)CAN\_MCAN\_TIMING\_DATA\_MAX\_INITIALIZER

| #define CAN\_MCAN\_TIMING\_DATA\_MAX\_INITIALIZER |
| --- |

**Value:**

{ \

.sjw = 16, \

.prop\_seg = 0, \

.phase\_seg1 = 32, \

.phase\_seg2 = 16, \

.prescaler = 32 \

}

Bosch M\_CAN specific static initializer for a maximum data phase `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct.

## [◆ ](#afd190643aa2435880769aef338f02d23)CAN\_MCAN\_TIMING\_DATA\_MIN\_INITIALIZER

| #define CAN\_MCAN\_TIMING\_DATA\_MIN\_INITIALIZER |
| --- |

**Value:**

{ \

.sjw = 1, \

.prop\_seg = 0, \

.phase\_seg1 = 1, \

.phase\_seg2 = 1, \

.prescaler = 1 \

}

Bosch M\_CAN specific static initializer for a minimum data phase `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct.

## [◆ ](#aedef0bb36bcd204ee5000ae9528248b7)CAN\_MCAN\_TIMING\_MAX\_INITIALIZER

| #define CAN\_MCAN\_TIMING\_MAX\_INITIALIZER |
| --- |

**Value:**

{ \

.sjw = 128, \

.prop\_seg = 0, \

.phase\_seg1 = 256, \

.phase\_seg2 = 128, \

.prescaler = 512 \

}

Bosch M\_CAN specific static initializer for a maximum nominal `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct.

## [◆ ](#aa0de1f9512dc3e3d44f06a2f7f2f4adf)CAN\_MCAN\_TIMING\_MIN\_INITIALIZER

| #define CAN\_MCAN\_TIMING\_MIN\_INITIALIZER |
| --- |

**Value:**

{ \

.sjw = 1, \

.prop\_seg = 0, \

.phase\_seg1 = 2, \

.phase\_seg2 = 2, \

.prescaler = 1 \

}

Bosch M\_CAN specific static initializer for a minimum nominal `[can_timing](structcan__timing.md "CAN bus timing structure.")` struct.

## [◆ ](#a8913873d251c86e2fee4842bb9c4951c)CAN\_MCAN\_TOCC

| #define CAN\_MCAN\_TOCC   0x028 |
| --- |

## [◆ ](#a63a2024085348c787e6dbc231aa47846)CAN\_MCAN\_TOCC\_ETOC

| #define CAN\_MCAN\_TOCC\_ETOC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a4206bbc473216f1e68f7c6fb02cb27d3)CAN\_MCAN\_TOCC\_TOP

| #define CAN\_MCAN\_TOCC\_TOP   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 16) |
| --- |

## [◆ ](#a41d03bd4b12883207842512bde89f8e9)CAN\_MCAN\_TOCC\_TOS

| #define CAN\_MCAN\_TOCC\_TOS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 1) |
| --- |

## [◆ ](#a2f4377ce56a8a38991fba9b2cc2d87c9)CAN\_MCAN\_TOCV

| #define CAN\_MCAN\_TOCV   0x02C |
| --- |

## [◆ ](#aeb97ca070414b41a8de66bdf14f63d32)CAN\_MCAN\_TOCV\_TOC

| #define CAN\_MCAN\_TOCV\_TOC   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

## [◆ ](#a336430f9fd3a26e6c54deaf072bc1ad6)CAN\_MCAN\_TSCC

| #define CAN\_MCAN\_TSCC   0x020 |
| --- |

## [◆ ](#ad38c5e544217947bd4dd44ec53291e91)CAN\_MCAN\_TSCC\_TCP

| #define CAN\_MCAN\_TSCC\_TCP   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(19, 16) |
| --- |

## [◆ ](#aefdf97284e7860342d550e0043c1b80c)CAN\_MCAN\_TSCC\_TSS

| #define CAN\_MCAN\_TSCC\_TSS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| --- |

## [◆ ](#a8704135ca0f1a015b4f6527e6d9bafcd)CAN\_MCAN\_TSCV

| #define CAN\_MCAN\_TSCV   0x024 |
| --- |

## [◆ ](#a3ac6c1d5d964b1646d1a3e2a53d3206f)CAN\_MCAN\_TSCV\_TSC

| #define CAN\_MCAN\_TSCV\_TSC   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 0) |
| --- |

## [◆ ](#a547995f6d877963184992a5cc09fdcf3)CAN\_MCAN\_TXBAR

| #define CAN\_MCAN\_TXBAR   0x0D0 |
| --- |

## [◆ ](#ae92b22867500ceb14a6e2035cbf6c8b1)CAN\_MCAN\_TXBAR\_AR

| #define CAN\_MCAN\_TXBAR\_AR   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#aabbf65d56f0aacdd26b22eb80b34721e)CAN\_MCAN\_TXBC

| #define CAN\_MCAN\_TXBC   0x0C0 |
| --- |

## [◆ ](#afe25b1f33b0a877b8e46d35a26b5db8e)CAN\_MCAN\_TXBC\_NDTB

| #define CAN\_MCAN\_TXBC\_NDTB   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| --- |

## [◆ ](#a54aa984e023137eb87aa8b00f59ea02c)CAN\_MCAN\_TXBC\_TBSA

| #define CAN\_MCAN\_TXBC\_TBSA   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| --- |

## [◆ ](#a4ff2da25354a95ae078951a3b8f0b1f0)CAN\_MCAN\_TXBC\_TFQM

| #define CAN\_MCAN\_TXBC\_TFQM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30) |
| --- |

## [◆ ](#a25144c814fa7ed19bd6c391cbb2244e6)CAN\_MCAN\_TXBC\_TFQS

| #define CAN\_MCAN\_TXBC\_TFQS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(29, 24) |
| --- |

## [◆ ](#a6d671b8127c66b7e8a7e019b68201afd)CAN\_MCAN\_TXBCF

| #define CAN\_MCAN\_TXBCF   0x0DC |
| --- |

## [◆ ](#a027220d5bfd988da4716e5e89d9e7f9d)CAN\_MCAN\_TXBCF\_CF

| #define CAN\_MCAN\_TXBCF\_CF   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#aafe9d81dfa50841d20a1a6719b544017)CAN\_MCAN\_TXBCIE

| #define CAN\_MCAN\_TXBCIE   0x0E4 |
| --- |

## [◆ ](#a1b0214f3f897c6852e4fdbff3f8f21a2)CAN\_MCAN\_TXBCIE\_CFIE

| #define CAN\_MCAN\_TXBCIE\_CFIE   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#ad0f3bb0f2d096cff8e1e2ac4416c44e0)CAN\_MCAN\_TXBCR

| #define CAN\_MCAN\_TXBCR   0x0D4 |
| --- |

## [◆ ](#a023ae0f402eb013e68d35a1e367ff710)CAN\_MCAN\_TXBCR\_CR

| #define CAN\_MCAN\_TXBCR\_CR   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#a3c8dcbcf3921d5e51306cb8e5feb2cd1)CAN\_MCAN\_TXBRP

| #define CAN\_MCAN\_TXBRP   0x0CC |
| --- |

## [◆ ](#a8e4d1e69b827265adb8aff580ca01cde)CAN\_MCAN\_TXBRP\_TRP

| #define CAN\_MCAN\_TXBRP\_TRP   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#a8a4753541d28a7ff92d8b7ba844fa943)CAN\_MCAN\_TXBTIE

| #define CAN\_MCAN\_TXBTIE   0x0E0 |
| --- |

## [◆ ](#a7f99c9c844897923c02a1356af052ddf)CAN\_MCAN\_TXBTIE\_TIE

| #define CAN\_MCAN\_TXBTIE\_TIE   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#ab8050da5ff162f638b7920cc80115a8a)CAN\_MCAN\_TXBTO

| #define CAN\_MCAN\_TXBTO   0x0D8 |
| --- |

## [◆ ](#adf91c2d98d25bf2f2901e215a8715b9b)CAN\_MCAN\_TXBTO\_TO

| #define CAN\_MCAN\_TXBTO\_TO   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 0) |
| --- |

## [◆ ](#a3a0b6530cbff5e1661c6ad208cedff08)CAN\_MCAN\_TXEFA

| #define CAN\_MCAN\_TXEFA   0x0F8 |
| --- |

## [◆ ](#a78b3604320fdc00e0fe734516f5e1db9)CAN\_MCAN\_TXEFA\_EFAI

| #define CAN\_MCAN\_TXEFA\_EFAI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| --- |

## [◆ ](#a68ea1bab6b687ad406f416c73441ff9c)CAN\_MCAN\_TXEFC

| #define CAN\_MCAN\_TXEFC   0x0F0 |
| --- |

## [◆ ](#af2ade33b56998a19aeda8cb0f868324c)CAN\_MCAN\_TXEFC\_EFS

| #define CAN\_MCAN\_TXEFC\_EFS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| --- |

## [◆ ](#a162a0b6fd08c65359afa9dc59fba9ed3)CAN\_MCAN\_TXEFC\_EFSA

| #define CAN\_MCAN\_TXEFC\_EFSA   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| --- |

## [◆ ](#a7551e23d8ba589be55831268b69ce099)CAN\_MCAN\_TXEFC\_EFWM

| #define CAN\_MCAN\_TXEFC\_EFWM   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(29, 24) |
| --- |

## [◆ ](#a48888433839c16389c97ab6a359667d1)CAN\_MCAN\_TXEFS

| #define CAN\_MCAN\_TXEFS   0x0F4 |
| --- |

## [◆ ](#ae430823894219a2e271310be16e484f4)CAN\_MCAN\_TXEFS\_EFF

| #define CAN\_MCAN\_TXEFS\_EFF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| --- |

## [◆ ](#a94994438584cfdfa0a9c7bc91227ee7e)CAN\_MCAN\_TXEFS\_EFFL

| #define CAN\_MCAN\_TXEFS\_EFFL   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| --- |

## [◆ ](#af69a4882448bb8cab8bee6c20f145e18)CAN\_MCAN\_TXEFS\_EFGI

| #define CAN\_MCAN\_TXEFS\_EFGI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 8) |
| --- |

## [◆ ](#a64ccc68de69d3d46367e05e46934225e)CAN\_MCAN\_TXEFS\_EFPI

| #define CAN\_MCAN\_TXEFS\_EFPI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(20, 16) |
| --- |

## [◆ ](#a6f4fdc1835216b1408796b9f541054b8)CAN\_MCAN\_TXEFS\_TEFL

| #define CAN\_MCAN\_TXEFS\_TEFL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25) |
| --- |

## [◆ ](#a4a862608de38135c9febbb6d75b153ef)CAN\_MCAN\_TXESC

| #define CAN\_MCAN\_TXESC   0x0C8 |
| --- |

## [◆ ](#ad20ed0d0615c7f4804cbb9324499f84d)CAN\_MCAN\_TXESC\_TBDS

| #define CAN\_MCAN\_TXESC\_TBDS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| --- |

## [◆ ](#abdd2a49df8465eb55633f8707a46187e)CAN\_MCAN\_TXFQS

| #define CAN\_MCAN\_TXFQS   0x0C4 |
| --- |

## [◆ ](#a47bcf7d8796c4b4442afc1e194dcf657)CAN\_MCAN\_TXFQS\_TFFL

| #define CAN\_MCAN\_TXFQS\_TFFL   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| --- |

## [◆ ](#aac92788e1f00b7af37d15cad4a660cfe)CAN\_MCAN\_TXFQS\_TFGI

| #define CAN\_MCAN\_TXFQS\_TFGI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(12, 8) |
| --- |

## [◆ ](#a37ef0318a42bba8b5fce6d9d9ca094df)CAN\_MCAN\_TXFQS\_TFQF

| #define CAN\_MCAN\_TXFQS\_TFQF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21) |
| --- |

## [◆ ](#ae479a0770d5629198d3104a9729a777f)CAN\_MCAN\_TXFQS\_TFQPI

| #define CAN\_MCAN\_TXFQS\_TFQPI   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(20, 16) |
| --- |

## [◆ ](#ac336e47e175c4c54469ce58ca122195c)CAN\_MCAN\_XFEC\_DISABLE

| #define CAN\_MCAN\_XFEC\_DISABLE   0x0 |
| --- |

## [◆ ](#a7312f835309269943ff6b758521449b6)CAN\_MCAN\_XFEC\_FIFO0

| #define CAN\_MCAN\_XFEC\_FIFO0   0x1 |
| --- |

## [◆ ](#ad0570275343000c1af9a14e0589939c3)CAN\_MCAN\_XFEC\_FIFO1

| #define CAN\_MCAN\_XFEC\_FIFO1   0x2 |
| --- |

## [◆ ](#a95f862be638ce43223aebcd1f763be2d)CAN\_MCAN\_XFEC\_PRIO

| #define CAN\_MCAN\_XFEC\_PRIO   0x4 |
| --- |

## [◆ ](#aec0a8173842cc5f1a13e84fb5ee38f19)CAN\_MCAN\_XFEC\_PRIO\_FIFO0

| #define CAN\_MCAN\_XFEC\_PRIO\_FIFO0   0x5 |
| --- |

## [◆ ](#a3073ff3bc20ef4a28af1d92f9d2e9a02)CAN\_MCAN\_XFEC\_PRIO\_FIFO1

| #define CAN\_MCAN\_XFEC\_PRIO\_FIFO1   0x7 |
| --- |

## [◆ ](#a2cd5607208221a6da2cf07e67ef00dde)CAN\_MCAN\_XFEC\_REJECT

| #define CAN\_MCAN\_XFEC\_REJECT   0x3 |
| --- |

## [◆ ](#a9c64c5bcc80f2bdaad64de5c370826db)CAN\_MCAN\_XIDAM

| #define CAN\_MCAN\_XIDAM   0x090 |
| --- |

## [◆ ](#afd1f6383e81e4dfbc1a156bf5a3092bb)CAN\_MCAN\_XIDAM\_EIDM

| #define CAN\_MCAN\_XIDAM\_EIDM   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(28, 0) |
| --- |

## [◆ ](#abc56cb7ea0b29dd3c813494cad7ba81c)CAN\_MCAN\_XIDFC

| #define CAN\_MCAN\_XIDFC   0x088 |
| --- |

## [◆ ](#a43ad251923878baed62ab97ed44b0dc9)CAN\_MCAN\_XIDFC\_FLESA

| #define CAN\_MCAN\_XIDFC\_FLESA   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 2) |
| --- |

## [◆ ](#adc32a4719774acdac26727fc7910698a)CAN\_MCAN\_XIDFC\_LSS

| #define CAN\_MCAN\_XIDFC\_LSS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(22, 16) |
| --- |

## Typedef Documentation

## [◆ ](#a321813b4b3def118480a7a9eccb6d4aa)can\_mcan\_clear\_mram\_t

| typedef int(\* can\_mcan\_clear\_mram\_t) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Bosch M\_CAN driver front-end callback for clearing Message RAM.

Clear Message RAM by writing 0 to all words.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | len | Number of bytes to clear. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#a9532f0655c579f0ab091f85771b5d62d)can\_mcan\_read\_mram\_t

| typedef int(\* can\_mcan\_read\_mram\_t) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Bosch M\_CAN driver front-end callback for reading from Message RAM.

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | [out] | dst | Destination for the data read. The destination address must be 32-bit aligned. |
    |  | len | Number of bytes to read. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#a79941b7745919bb1bf7d7219555440a6)can\_mcan\_read\_reg\_t

| typedef int(\* can\_mcan\_read\_reg\_t) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
| --- |

Bosch M\_CAN driver front-end callback for reading a register value.

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | reg | Register offset |
    | [out] | val | Register value |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | Register not supported. |
    | -EIO | General input/output error. |

## [◆ ](#aaf2920e649f9671f09856a062ac4dc95)can\_mcan\_write\_mram\_t

| typedef int(\* can\_mcan\_write\_mram\_t) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Bosch M\_CAN driver front-end callback for writing to Message RAM.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | src | Source for the data to be written. The source address must be 32-bit aligned. |
    | len | Number of bytes to write. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#acbb72b712e516fe923e6030a9d6b36c1)can\_mcan\_write\_reg\_t

| typedef int(\* can\_mcan\_write\_reg\_t) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| --- |

Bosch M\_CAN driver front-end callback for writing a register value.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | reg | Register offset |
    | val | Register value |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | Register not supported. |
    | -EIO | General input/output error. |

## Enumeration Type Documentation

## [◆ ](#a888671da33c3ffc35ce94c8eba13d462)can\_mcan\_psr\_lec

| enum [can\_mcan\_psr\_lec](#a888671da33c3ffc35ce94c8eba13d462) |
| --- |

| Enumerator | |
| --- | --- |
| CAN\_MCAN\_PSR\_LEC\_NO\_ERROR |  |
| CAN\_MCAN\_PSR\_LEC\_STUFF\_ERROR |  |
| CAN\_MCAN\_PSR\_LEC\_FORM\_ERROR |  |
| CAN\_MCAN\_PSR\_LEC\_ACK\_ERROR |  |
| CAN\_MCAN\_PSR\_LEC\_BIT1\_ERROR |  |
| CAN\_MCAN\_PSR\_LEC\_BIT0\_ERROR |  |
| CAN\_MCAN\_PSR\_LEC\_CRC\_ERROR |  |
| CAN\_MCAN\_PSR\_LEC\_NO\_CHANGE |  |

## Function Documentation

## [◆ ](#a6a215a77fada5caafd7fb0da72308d95)can\_mcan\_add\_rx\_filter()

| int can\_mcan\_add\_rx\_filter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) | *callback*, |
|  |  | void \* | *user\_data*, |
|  |  | const struct [can\_filter](structcan__filter.md) \* | *filter* ) |

Bosch M\_CAN driver callback API upon adding an RX filter See *can\_add\_rx\_callback()* for argument description.

## [◆ ](#aa330897ffad0a9e1b4f08aaaa22e5c70)can\_mcan\_clear\_mram()

| | int can\_mcan\_clear\_mram | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Clear Bosch M\_CAN Message RAM.

Clear Message RAM by writing 0 to all words.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | len | Number of bytes to clear. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#a2f9186fc69fe80b76133ab0f82100fc8)can\_mcan\_configure\_mram()

| int can\_mcan\_configure\_mram | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *mrba*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *mram* ) |

Configure Bosch M\_MCAN Message RAM start addresses.

Bosch M\_CAN driver front-end callback helper function for configuring the start addresses of the Bosch M\_CAN Rx FIFO0 (RXFOC), Rx FIFO1 (RXF1C), Rx Buffer (RXBCC), Tx Buffer (TXBC), and Tx Event FIFO (TXEFC) in Message RAM.

The start addresses (containing bits 15:2 since Bosch M\_CAN message RAM is accessed as 32 bit words) are calculated relative to the provided Message RAM Base Address (mrba).

Some Bosch M\_CAN implementations use a fixed Message RAM configuration, other use a fixed memory area and relative addressing, others again have custom registers for configuring the Message RAM. It is the responsibility of the front-end driver to call this function during driver initialization as needed.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | mrba | Message RAM Base Address. |
    | mram | Message RAM Address. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#a54f0e66b1b1912d841e10e68e01331fa)can\_mcan\_enable\_configuration\_change()

| void can\_mcan\_enable\_configuration\_change | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable Bosch M\_CAN configuration change.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#abc9c13ee4f4b47d4ff74ab4c6352bbe1)can\_mcan\_get\_capabilities()

| int can\_mcan\_get\_capabilities | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \* | *cap* ) |

Bosch M\_CAN driver callback API upon getting CAN controller capabilities See *[can\_get\_capabilities()](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168 "Get the supported modes of the CAN controller.")* for argument description.

## [◆ ](#ac627d35c23322c003fa846866cfb6419)can\_mcan\_get\_max\_filters()

| int can\_mcan\_get\_max\_filters | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *ide* ) |

## [◆ ](#a40e0f8f7ec696c62dd132fed45a4da5d)can\_mcan\_get\_state()

| int can\_mcan\_get\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \* | *state*, |
|  |  | struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \* | *err\_cnt* ) |

Bosch M\_CAN driver callback API upon getting the CAN controller state See *[can\_get\_state()](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857 "Get current CAN controller state.")* for argument description.

## [◆ ](#a7d9006cb2e91f6b13c3d245612b175f0)can\_mcan\_init()

| int can\_mcan\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver initialization callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#a004d1a9aabc5307e6ab51a477f33c070)can\_mcan\_line\_0\_isr()

| void can\_mcan\_line\_0\_isr | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver m\_can\_int0 IRQ handler.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#a41e134fc94a573622eac9314f87dd673)can\_mcan\_line\_1\_isr()

| void can\_mcan\_line\_1\_isr | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver m\_can\_int1 IRQ handler.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#a1705a740e811f1065538c733498fc16f)can\_mcan\_read\_mram()

| | int can\_mcan\_read\_mram | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, | |  |  | void \* | *dst*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Read from Bosch M\_CAN Message RAM.

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | [out] | dst | Destination for the data read. |
    |  | len | Number of bytes to read. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#a05e01d009f6cb08f7e8497c9e2ee83ef)can\_mcan\_read\_reg()

| int can\_mcan\_read\_reg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *val* ) |

Read a Bosch M\_CAN register.

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | reg | Register offset |
    | [out] | val | Register value |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | Register not supported. |
    | -EIO | General input/output error. |

## [◆ ](#ae1a44958756509d882d6202cc337197e)can\_mcan\_remove\_rx\_filter()

| void can\_mcan\_remove\_rx\_filter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *filter\_id* ) |

Bosch M\_CAN driver callback API upon removing an RX filter See *[can\_remove\_rx\_filter()](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847 "Remove a CAN RX filter.")* for argument description.

## [◆ ](#a906568f3922bf3cf39eb9ac9e78d58ae)can\_mcan\_send()

| int can\_mcan\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_frame](structcan__frame.md) \* | *frame*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) | *callback*, |
|  |  | void \* | *user\_data* ) |

## [◆ ](#a1264c5d49f0eeee5e3656560e7b2fb65)can\_mcan\_set\_mode()

| int can\_mcan\_set\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) | *mode* ) |

Bosch M\_CAN driver callback API upon setting CAN controller mode See *[can\_set\_mode()](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f "Set the CAN controller to the given operation mode.")* for argument description.

## [◆ ](#a324735380014b09f4e1fb33ff0c539cd)can\_mcan\_set\_state\_change\_callback()

| void can\_mcan\_set\_state\_change\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) | *callback*, |
|  |  | void \* | *user\_data* ) |

Bosch M\_CAN driver callback API upon setting a state change callback See *[can\_set\_state\_change\_callback()](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e "Set a callback for CAN controller state change events.")* for argument description.

## [◆ ](#a33156b2282136192117cb663a4e64ea3)can\_mcan\_set\_timing()

| int can\_mcan\_set\_timing | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_timing](structcan__timing.md) \* | *timing* ) |

Bosch M\_CAN driver callback API upon setting CAN bus timing See *[can\_set\_timing()](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da "Configure the bus timing of a CAN controller.")* for argument description.

## [◆ ](#a1fd00ba6a4023631c8589763049e05e9)can\_mcan\_set\_timing\_data()

| int can\_mcan\_set\_timing\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_timing](structcan__timing.md) \* | *timing\_data* ) |

Bosch M\_CAN driver callback API upon setting CAN bus data phase timing See *[can\_set\_timing\_data()](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2 "Configure the bus timing for the data phase of a CAN FD controller.")* for argument description.

## [◆ ](#abcbc1ab4765005ec8acfd15921b065fd)can\_mcan\_start()

| int can\_mcan\_start | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver callback API upon starting CAN controller See *[can\_start()](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a "Start the CAN controller.")* for argument description.

## [◆ ](#a47d2f53639584c8fb4d65995e98ad77f)can\_mcan\_stop()

| int can\_mcan\_stop | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver callback API upon stopping CAN controller See *[can\_stop()](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5 "Stop the CAN controller.")* for argument description.

## [◆ ](#a65c59db492d1c3359d032b5f8a62af8b)can\_mcan\_sys\_clear\_mram()

| | int can\_mcan\_sys\_clear\_mram | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *base*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver front-end callback helper for clearing memory mapped Message RAM.

Clear Message RAM by writing 0 to all words.

Parameters
:   | base | Base address of the Message RAM for the given Bosch M\_CAN instance. The base address must be 32-bit aligned. |
    | --- | --- |
    | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | len | Number of bytes to clear. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#a5d7d5e0bb88b661462fa01720d824610)can\_mcan\_sys\_read\_mram()

| | int can\_mcan\_sys\_read\_mram | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *base*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, | |  |  | void \* | *dst*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver front-end callback helper for reading from memory mapped Message RAM.

Parameters
:   |  | base | Base address of the Message RAM for the given Bosch M\_CAN instance. The base address must be 32-bit aligned. |
    | --- | --- | --- |
    |  | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | [out] | dst | Destination for the data read. The destination address must be 32-bit aligned. |
    |  | len | Number of bytes to read. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#a2138e6f7c669bf8a1c1f04637ec9752c)can\_mcan\_sys\_read\_reg()

| | int can\_mcan\_sys\_read\_reg | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *base*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver front-end callback helper for reading a memory mapped register.

Parameters
:   |  | base | Register base address |
    | --- | --- | --- |
    |  | reg | Register offset |
    | [out] | val | Register value |

Return values
:   | 0 | Memory mapped register read always succeeds. |
    | --- | --- |

## [◆ ](#a21e0977205bb9db1be83968fda99bf95)can\_mcan\_sys\_write\_mram()

| | int can\_mcan\_sys\_write\_mram | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *base*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, | |  |  | const void \* | *src*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver front-end callback helper for writing to memory mapped Message RAM.

Parameters
:   | base | Base address of the Message RAM for the given Bosch M\_CAN instance. The base address must be 32-bit aligned. |
    | --- | --- |
    | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | src | Source for the data to be written. The source address must be 32-bit aligned. |
    | len | Number of bytes to write. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#ac1562291a74cc1f5b5e6d82fe31141bb)can\_mcan\_sys\_write\_reg()

| | int can\_mcan\_sys\_write\_reg | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *base*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Bosch M\_CAN driver front-end callback helper for writing a memory mapped register.

Parameters
:   | base | Register base address |
    | --- | --- |
    | reg | Register offset |
    | val | Register value |

Return values
:   | 0 | Memory mapped register write always succeeds. |
    | --- | --- |

## [◆ ](#ad2b88658a2294af890c56a99fee4a999)can\_mcan\_write\_mram()

| | int can\_mcan\_write\_mram | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, | |  |  | const void \* | *src*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Write to Bosch M\_CAN Message RAM.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | offset | Offset from the start of the Message RAM for the given Bosch M\_CAN instance. The offset must be 32-bit aligned. |
    | src | Source for the data to be written |
    | len | Number of bytes to write. Must be a multiple of 4. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error. |

## [◆ ](#a3f3e4be50fbf2c7ffcba99a1ca5ca7e1)can\_mcan\_write\_reg()

| int can\_mcan\_write\_reg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* ) |

Write a Bosch M\_CAN register.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | reg | Register offset |
    | val | Register value |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | Register not supported. |
    | -EIO | General input/output error. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can](dir_d26220086854d96f67fb3f45a38ba4bc.md)
- [can\_mcan.h](can__mcan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
