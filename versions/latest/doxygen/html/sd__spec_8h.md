---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sd__spec_8h.html
original_path: doxygen/html/sd__spec_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd\_spec.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](sd__spec_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sd\_switch\_caps](structsd__switch__caps.md) |
|  | SD switch capabilities. [More...](structsd__switch__caps.md#details) |
| struct | [sd\_cid](structsd__cid.md) |
|  | SD card identification register. [More...](structsd__cid.md#details) |
| struct | [sd\_csd](structsd__csd.md) |
|  | SD card specific data register. [More...](structsd__csd.md#details) |
| struct | [mmc\_device\_type](structmmc__device__type.md) |
|  | MMC Device Type. [More...](structmmc__device__type.md#details) |
| struct | [mmc\_ext\_csd](structmmc__ext__csd.md) |
|  | MMC extended card specific data register. [More...](structmmc__ext__csd.md#details) |
| struct | [sd\_scr](structsd__scr.md) |
|  | SD card configuration register. [More...](structsd__scr.md#details) |
| struct | [sdio\_cis](structsdio__cis.md) |
|  | SDIO common CIS tuple properties. [More...](structsdio__cis.md#details) |

| Macros | |
| --- | --- |
| #define | [SD\_R1\_CURRENT\_STATE](#ac104a7c39f61829092eaffd98663045b)(x) |
| #define | [SD\_SPI\_CMD\_SIZE](#aa841b78f5937f8499918cc977a36e90f)   6 |
| #define | [SD\_SPI\_CMD\_BODY\_SIZE](#a85e46f60c0ae5f21a4386009bbfaf0a3)   ([SD\_SPI\_CMD\_SIZE](#aa841b78f5937f8499918cc977a36e90f) - 1) |
| #define | [SD\_SPI\_CRC16\_SIZE](#aed67a9adbb001dad73eec4054ef6cbc1)   2 |
| #define | [SD\_SPI\_START](#a7da6535d451c1062f8d0c92f5688e178)   0x80 |
| #define | [SD\_SPI\_TX](#a2283409131ac9ede90773b256094b74c)   0x40 |
| #define | [SD\_SPI\_CMD](#a2d1dee775c3849a92dac9d179bd50a6c)   0x3F |
| #define | [SD\_SPI\_TOKEN\_SINGLE](#a7cd4fbf7d5ce2e8eba8c795a675486bb)   0xFE |
| #define | [SD\_SPI\_TOKEN\_MULTI\_WRITE](#ae34cf95537f2c0963ade18f1ba5d6e20)   0xFC |
| #define | [SD\_SPI\_TOKEN\_STOP\_TRAN](#a9d4f357ff29ee3b5483505404ba3c956)   0xFD |
| #define | [SD\_SPI\_RESPONSE\_ACCEPTED](#a5d36df2e0d1bd88aadc3673cdf12aea7)   0x05 |
| #define | [SD\_SPI\_RESPONSE\_CRC\_ERR](#a3a206f684b2c878f59a394b06abd9814)   0x0B |
| #define | [SD\_SPI\_RESPONSE\_WRITE\_ERR](#a498f76218e054dff0e524a83ac90ccd1)   0x0C |
| #define | [SD\_IF\_COND\_VHS\_MASK](#a0d10fc7ae53b5bfb6d7f448844820799)   (0x0F << 8) |
| #define | [SD\_IF\_COND\_VHS\_3V3](#a38157545a4a10dd4757ad1eb80487c60)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [SD\_IF\_COND\_CHECK](#aed6aacadb061a42993c59d8d69a2f2ab)   0xAA |
| #define | [SDIO\_OCR\_IO\_NUMBER\_SHIFT](#a23690672048afbc75ce2c2f4d9a74144)   28 |
| #define | [SDIO\_IO\_OCR\_MASK](#a0d98fd7cd6f67b28981c6e01f8805a01)   0xFFFFFF |
| #define | [SD\_PRODUCT\_NAME\_BYTES](#a947520a05fc99c25449fab98d0d02b1e)   5 |
| #define | [SDMMC\_DEFAULT\_BLOCK\_SIZE](#a523a28eeec3d0a71f0d7ca49ab397960)   512 |
| #define | [MMC\_EXT\_CSD\_BYTES](#ade9a798f584d431c86e172266394f41e)   512 |
| #define | [SDIO\_CMD\_ARG\_RW\_SHIFT](#a960ade30c404ebb08769c5870ac21b37)   31 |
|  | read/write flag shift |
| #define | [SDIO\_CMD\_ARG\_FUNC\_NUM\_SHIFT](#acd6e41030a8d16419cc22adf9f0a5509)   28 |
|  | function number shift |
| #define | [SDIO\_DIRECT\_CMD\_ARG\_RAW\_SHIFT](#afadddcc143b78325505a40544c04e3b0)   27 |
|  | direct raw flag shift |
| #define | [SDIO\_CMD\_ARG\_REG\_ADDR\_SHIFT](#aa74dbe588f1f5ca248cf0f5a2e8e8c81)   9 |
|  | direct reg addr shift |
| #define | [SDIO\_CMD\_ARG\_REG\_ADDR\_MASK](#a338e9606baa6937e0887e7a9b9372c23)   0x1FFFF |
|  | direct reg addr mask |
| #define | [SDIO\_DIRECT\_CMD\_DATA\_MASK](#a5ab9e1e0c96e7166b1ff7a208f90001d)   0xFF |
|  | data mask |
| #define | [SDIO\_EXTEND\_CMD\_ARG\_BLK\_SHIFT](#ac6c49ad6118debe7a9e64f412e597f22)   27 |
|  | extended write block mode |
| #define | [SDIO\_EXTEND\_CMD\_ARG\_OP\_CODE\_SHIFT](#a73ca83a4884f13fa5de8500f69252bef)   26 |
|  | op code (increment address) |
| #define | [SDIO\_CCCR\_CCCR](#ae211fa0bfa6809273b5f7267c95ce681)   0x00 |
|  | Card common control register definitions. |
| #define | [SDIO\_CCCR\_CCCR\_REV\_MASK](#accf473b0fcdc9e1e03329f91e588de1a)   0x0F |
| #define | [SDIO\_CCCR\_CCCR\_REV\_SHIFT](#af5db599ebd0748528e8369653a5e3929)   0x0 |
| #define | [SDIO\_CCCR\_CCCR\_REV\_1\_00](#ab240215a68f23ec69e901c0666b0dfe0)   0x0 |
|  | CCCR/FBR Version 1.00. |
| #define | [SDIO\_CCCR\_CCCR\_REV\_1\_10](#aace4672360d77085bec93b52e3ac05d9)   0x1 |
|  | CCCR/FBR Version 1.10. |
| #define | [SDIO\_CCCR\_CCCR\_REV\_2\_00](#a566200e9322e8e4c9b3edd21a2ced93c)   0x2 |
|  | CCCR/FBR Version 2.00. |
| #define | [SDIO\_CCCR\_CCCR\_REV\_3\_00](#aa90600f74ff69315e38ed1c10a3cde7c)   0x3 |
|  | CCCR/FBR Version 3.00. |
| #define | [SDIO\_CCCR\_SD](#aafc2b0c434dff4a0903e4910181f9e81)   0x01 |
|  | SD spec version register. |
| #define | [SDIO\_CCCR\_SD\_SPEC\_MASK](#aa425236b097f44a9721e7aedd203ff90)   0x0F |
| #define | [SDIO\_CCCR\_SD\_SPEC\_SHIFT](#a223defa20d223655d215065b222a6767)   0x0 |
| #define | [SDIO\_CCCR\_IO\_EN](#a0b2103011690e1d3f1daef4e45a11986)   0x02 |
|  | SDIO IO Enable register. |
| #define | [SDIO\_CCCR\_IO\_RD](#a6cfa2671e574650e6f35a65828cd459c)   0x03 |
|  | SDIO IO Ready register. |
| #define | [SDIO\_CCCR\_INT\_EN](#a15caca2936186b54c330b4a9050c9795)   0x04 |
|  | SDIO Interrupt enable register. |
| #define | [SDIO\_CCCR\_INT\_P](#a81b7523a76a1826a14c2cc1c242a49a9)   0x05 |
|  | SDIO Interrupt pending register. |
| #define | [SDIO\_CCCR\_ABORT](#a7e061818bc8f923d5342c38721a1a501)   0x06 |
|  | SDIO IO abort register. |
| #define | [SDIO\_CCCR\_BUS\_IF](#a283f2b2f2c28b3c8208f3d6aca3ca3d2)   0x07 |
|  | SDIO bus interface control register. |
| #define | [SDIO\_CCCR\_BUS\_IF\_WIDTH\_MASK](#a6c04dc28d7f39fda7cd0181421a13ea0)   0x3 |
|  | SDIO bus width setting mask. |
| #define | [SDIO\_CCCR\_BUS\_IF\_WIDTH\_1\_BIT](#aec58e3fcda2f792266fbd8ab1b75f98c)   0x00 |
|  | 1 bit SDIO bus setting |
| #define | [SDIO\_CCCR\_BUS\_IF\_WIDTH\_4\_BIT](#aeb23fa771a16f69fcb9d97b156f25ade)   0x02 |
|  | 4 bit SDIO bus setting |
| #define | [SDIO\_CCCR\_BUS\_IF\_WIDTH\_8\_BIT](#ade7a14837ee90c8ce24959926d81eaee)   0x03 |
|  | 8 bit SDIO bus setting |
| #define | [SDIO\_CCCR\_CAPS](#a0b878d7e794d3edd127c3f08633efbbc)   0x08 |
|  | SDIO card capabilities. |
| #define | [SDIO\_CCCR\_CAPS\_SDC](#affb9533b340f5424c1f42445c6f1002f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | support CMD52 while data transfer |
| #define | [SDIO\_CCCR\_CAPS\_SMB](#aaaf8d335a8d025b998feeb93c0899a99)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | support multiple block transfer |
| #define | [SDIO\_CCCR\_CAPS\_SRW](#a8011927f7b565304ec31a7e61d403d6e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | support read wait control |
| #define | [SDIO\_CCCR\_CAPS\_SBS](#a7550fe8aab011fc87baeb575463e27d9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | support bus control |
| #define | [SDIO\_CCCR\_CAPS\_S4MI](#a74082cfafdd9e8bfa37e92624ff75e80)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | support block gap interrupt |
| #define | [SDIO\_CCCR\_CAPS\_E4MI](#aa8281a65d0865fba8b85d91d00b90091)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | enable block gap interrupt |
| #define | [SDIO\_CCCR\_CAPS\_LSC](#aee93278e3c0ec4cbf0e3065d6a58f516)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | low speed card |
| #define | [SDIO\_CCCR\_CAPS\_BLS](#a7ba2dcf801f81ab53b418e59441000ae)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | low speed card with 4 bit support |
| #define | [SDIO\_CCCR\_CIS](#a8f97c16c091bd19b545bbe452581dfff)   0x09 |
|  | SDIO CIS tuples pointer. |
| #define | [SDIO\_CCCR\_SPEED](#a05edbcb4a98831cbeac509f26e881de8)   0x13 |
|  | SDIO bus speed select. |
| #define | [SDIO\_CCCR\_SPEED\_SHS](#a964759dc76bd2a9f9f9dce5c21dc2cb4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | high speed support |
| #define | [SDIO\_CCCR\_SPEED\_MASK](#a1a1817554f886a999484e2663432cd8b)   0xE |
|  | bus speed select mask |
| #define | [SDIO\_CCCR\_SPEED\_SHIFT](#a38d57134d99e2dfc5760fcf7312b6cd5)   0x1 |
|  | bus speed select shift |
| #define | [SDIO\_CCCR\_SPEED\_SDR12](#a9ee7aec8589aceb8555917971ab9afd3)   0x0 |
|  | select SDR12 |
| #define | [SDIO\_CCCR\_SPEED\_HS](#acb3bdd73bace425a94a357a2f0bff4ef)   0x1 |
|  | select High speed mode |
| #define | [SDIO\_CCCR\_SPEED\_SDR25](#afabf4bb10bed3295d1d051c113e61545)   0x1 |
|  | select SDR25 |
| #define | [SDIO\_CCCR\_SPEED\_SDR50](#a81bc96279a19618c9212674757abd141)   0x2 |
|  | select SDR50 |
| #define | [SDIO\_CCCR\_SPEED\_SDR104](#a0d51f98d56303dd55177245785748158)   0x3 |
|  | select SDR104 |
| #define | [SDIO\_CCCR\_SPEED\_DDR50](#ad3dc3009d2d78a6306c3247ab85ef48d)   0x4 |
|  | select DDR50 |
| #define | [SDIO\_CCCR\_UHS](#afb72ff0aa5b90446db296af16bf9bb02)   0x14 |
|  | SDIO UHS support. |
| #define | [SDIO\_CCCR\_UHS\_SDR50](#a9965d399115bca8574a9beaeac9b9f31)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | SDR50 support. |
| #define | [SDIO\_CCCR\_UHS\_SDR104](#aca4fee68fdf3480ec8cf7de7b46a8d4e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | SDR104 support. |
| #define | [SDIO\_CCCR\_UHS\_DDR50](#a2678ede1ac974a9670fdcaa393682aa6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | DDR50 support. |
| #define | [SDIO\_CCCR\_DRIVE\_STRENGTH](#a3a5d01e688b18109ad2f19bc5d017f26)   0x15 |
|  | SDIO drive strength. |
| #define | [SDIO\_CCCR\_DRIVE\_STRENGTH\_A](#a759a9dddc3aa08d0f11114637c5b69ff)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | drive type A |
| #define | [SDIO\_CCCR\_DRIVE\_STRENGTH\_C](#a8487f5a0a97e5f1f72500cf44cec89dc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | drive type C |
| #define | [SDIO\_CCCR\_DRIVE\_STRENGTH\_D](#abc1ed41094d9cdd300b1b3712bb082b2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | drive type D |
| #define | [SDIO\_FBR\_BASE](#a2ff95d19f7f60ce33b17b69e2672e7e5)(n) |
|  | Get function base register addr. |
| #define | [SDIO\_FBR\_CIS](#aea0ed052a9d94d2e2b96931752975858)   0x09 |
|  | SDIO function base register CIS pointer. |
| #define | [SDIO\_FBR\_CSA](#a28fb27484353eb075d501b1ad7a76112)   0x0C |
|  | SDIO function base register CSA pointer. |
| #define | [SDIO\_FBR\_BLK\_SIZE](#af1885023615980d5cbb930538cc201a6)   0x10 |
|  | SDIO function base register block size. |
| #define | [SDIO\_MAX\_IO\_NUMS](#a845866f4f88c280f8414b727e0d77edf)   7 |
|  | Maximum number of I/O functions for SDIO. |
| #define | [SDIO\_TPL\_CODE\_NULL](#afadae8a1db38d93b909b3f2c5b0e0110)   0x00 |
|  | NULL CIS tuple code. |
| #define | [SDIO\_TPL\_CODE\_MANIFID](#af1983253320b45a2a1a2aab28c09e08f)   0x20 |
|  | manufacturer ID CIS tuple code |
| #define | [SDIO\_TPL\_CODE\_FUNCID](#aae6f9377eccdbd5866f1a393e083c5e4)   0x21 |
|  | function ID CIS tuple code |
| #define | [SDIO\_TPL\_CODE\_FUNCE](#ac263bf61bcc750880bae34dde62d61e4)   0x22 |
|  | function extension CIS tuple code |
| #define | [SDIO\_TPL\_CODE\_END](#a21e0771f38a22f93c9f4167d8b36f608)   0xFF |
|  | End CIS tuple code. |

| Enumerations | |
| --- | --- |
| enum | [sd\_opcode](#a072705601a34c697515f74acb0474c99) {     [SD\_GO\_IDLE\_STATE](#a072705601a34c697515f74acb0474c99a9dcb2e5fb6a5a53c6cb02422fd1fef3c) = 0 , [MMC\_SEND\_OP\_COND](#a072705601a34c697515f74acb0474c99a54546b311e446754738a9b6f1e3eaea4) = 1 , [SD\_ALL\_SEND\_CID](#a072705601a34c697515f74acb0474c99affcc3d18f6bda30fb3fd34916d8f61fe) = 2 , [SD\_SEND\_RELATIVE\_ADDR](#a072705601a34c697515f74acb0474c99a35c39a93dfcc239fcb80db70449af99e) = 3 ,     [MMC\_SEND\_RELATIVE\_ADDR](#a072705601a34c697515f74acb0474c99a56c94068ecb32eb9ced47d4a3bf95481) = 3 , [SDIO\_SEND\_OP\_COND](#a072705601a34c697515f74acb0474c99af48c850f0aa9e9f9dbce8fc8855f6a2a) = 5 , [SD\_SWITCH](#a072705601a34c697515f74acb0474c99a400dc3acd2ae8320f130dbea80c81969) = 6 , [SD\_SELECT\_CARD](#a072705601a34c697515f74acb0474c99afa15c17b4fb95747b444616b085b4905) = 7 ,     [SD\_SEND\_IF\_COND](#a072705601a34c697515f74acb0474c99a0da09225692b10e51140d4f15ba1dd0a) = 8 , [MMC\_SEND\_EXT\_CSD](#a072705601a34c697515f74acb0474c99a7c9bfc788861214fae86e22443e9484a) = 8 , [SD\_SEND\_CSD](#a072705601a34c697515f74acb0474c99adc7e589c9352cddf856b2e868f93a097) = 9 , [SD\_SEND\_CID](#a072705601a34c697515f74acb0474c99a8c3edf14ca3a6e04c1949a40cd3fb135) = 10 ,     [SD\_VOL\_SWITCH](#a072705601a34c697515f74acb0474c99ad6d6f1ccdabc2970ac2ab6c7a853b37e) = 11 , [SD\_STOP\_TRANSMISSION](#a072705601a34c697515f74acb0474c99aa5f2d8c27d0b7ae780734cb4bedbf8a4) = 12 , [SD\_SEND\_STATUS](#a072705601a34c697515f74acb0474c99ad822462692847b4e8433157cd75eef70) = 13 , [MMC\_CHECK\_BUS\_TEST](#a072705601a34c697515f74acb0474c99a45bc2d4b117d144ef5191719f9b6c297) = 14 ,     [SD\_GO\_INACTIVE\_STATE](#a072705601a34c697515f74acb0474c99a5c85e3208bb686d8ded9ae0fe7bd9d53) = 15 , [SD\_SET\_BLOCK\_SIZE](#a072705601a34c697515f74acb0474c99abd97c835c80320637579c692d6f57878) = 16 , [SD\_READ\_SINGLE\_BLOCK](#a072705601a34c697515f74acb0474c99a99c20a704cce28fee37b9b0f14b2ff15) = 17 , [SD\_READ\_MULTIPLE\_BLOCK](#a072705601a34c697515f74acb0474c99aa58b1d9f75b639dc1b28163988bc8aa3) = 18 ,     [SD\_SEND\_TUNING\_BLOCK](#a072705601a34c697515f74acb0474c99af48292861388f111b0afad64f0352664) = 19 , [MMC\_SEND\_BUS\_TEST](#a072705601a34c697515f74acb0474c99a35b942802a4238882440f2e470f2555f) = 19 , [MMC\_SEND\_TUNING\_BLOCK](#a072705601a34c697515f74acb0474c99a0378338c2747ba8947d8ffcb18f77d51) = 21 , [SD\_SET\_BLOCK\_COUNT](#a072705601a34c697515f74acb0474c99a7e34ea8ce2a215c2a76f4184b84a06f2) = 23 ,     [SD\_WRITE\_SINGLE\_BLOCK](#a072705601a34c697515f74acb0474c99adca664fbf5ff0b4d174ca21641e01004) = 24 , [SD\_WRITE\_MULTIPLE\_BLOCK](#a072705601a34c697515f74acb0474c99a9cd6e9c88c3989531a71015147496895) = 25 , [SD\_ERASE\_BLOCK\_START](#a072705601a34c697515f74acb0474c99aa7c628982851eba38074d02e9e335b57) = 32 , [SD\_ERASE\_BLOCK\_END](#a072705601a34c697515f74acb0474c99a753b0fc3e44a4376998e5887ed2c5901) = 33 ,     [SD\_ERASE\_BLOCK\_OPERATION](#a072705601a34c697515f74acb0474c99a4aa36f7d8ceaa3cdab300915453b64b5) = 38 , [SDIO\_RW\_DIRECT](#a072705601a34c697515f74acb0474c99a7ef64e231154de2e461005af29918b86) = 52 , [SDIO\_RW\_EXTENDED](#a072705601a34c697515f74acb0474c99a7ccf37711e67b58534689997ac1375df) = 53 , [SD\_APP\_CMD](#a072705601a34c697515f74acb0474c99aef4ee3246cd66cd7d48f1dabf3fcd7ef) = 55 ,     [SD\_SPI\_READ\_OCR](#a072705601a34c697515f74acb0474c99aa3183436decfa0e42ac0461629258ba3) = 58 , [SD\_SPI\_CRC\_ON\_OFF](#a072705601a34c697515f74acb0474c99ab590e9d9b3213f31a2399ef379d066aa) = 59   } |
|  | SD specification command opcodes. [More...](#a072705601a34c697515f74acb0474c99) |
| enum | [sd\_app\_cmd](#a1c77191f9cb8c50e8e2a03cda2984dbc) {     [SD\_APP\_SET\_BUS\_WIDTH](#a1c77191f9cb8c50e8e2a03cda2984dbcaca51b75cde3505fd672391b9d7a7997a) = 6 , [SD\_APP\_SEND\_STATUS](#a1c77191f9cb8c50e8e2a03cda2984dbca36f78cdbd8fcc962c2247d7fc1f33f9b) = 13 , [SD\_APP\_SEND\_NUM\_WRITTEN\_BLK](#a1c77191f9cb8c50e8e2a03cda2984dbca03fc81eeed7047ad914ce6590511dfa3) = 22 , [SD\_APP\_SET\_WRITE\_BLK\_ERASE\_CNT](#a1c77191f9cb8c50e8e2a03cda2984dbcacf330302cc8ef7f55d76c2cace40649e) = 23 ,     [SD\_APP\_SEND\_OP\_COND](#a1c77191f9cb8c50e8e2a03cda2984dbca2a4278c079a227145f63f5f2d860146a) = 41 , [SD\_APP\_CLEAR\_CARD\_DETECT](#a1c77191f9cb8c50e8e2a03cda2984dbcaa4a44bb015be3cbcf180f34a39ba8e05) = 42 , [SD\_APP\_SEND\_SCR](#a1c77191f9cb8c50e8e2a03cda2984dbca305b2fb720b5191c762b77b886152ca8) = 51   } |
|  | SD application command opcodes. [More...](#a1c77191f9cb8c50e8e2a03cda2984dbc) |
| enum | [sd\_r1\_status](#ad38162e32b87d3c01f1ae46d3423155a) {     [SD\_R1\_AUTH\_ERR](#ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5) = BIT(3) , [SD\_R1\_APP\_CMD](#ad38162e32b87d3c01f1ae46d3423155aa72c5d7592912c25f0440fa38664dfc13) = BIT(5) , [SD\_R1\_FX\_EVENT](#ad38162e32b87d3c01f1ae46d3423155aab852db2cfe8d7581e1ad7a1c2aee5406) = BIT(6) , [SD\_R1\_RDY\_DATA](#ad38162e32b87d3c01f1ae46d3423155aac99e88e470b5ecb04885b0289a96a2c8) = BIT(8) ,     [SD\_R1\_CUR\_STATE](#ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65) = (0xFU << 9) , [SD\_R1\_ERASE\_RESET](#ad38162e32b87d3c01f1ae46d3423155aa3c9f8c1239694b9bda4aca0d7f40a929) = BIT(13) , [SD\_R1\_ECC\_DISABLED](#ad38162e32b87d3c01f1ae46d3423155aa4cf46d638fd781b73edd03b61dd5d1a2) = BIT(14) , [SD\_R1\_ERASE\_SKIP](#ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837) = BIT(15) ,     [SD\_R1\_CSD\_OVERWRITE](#ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2) = BIT(16) , [SD\_R1\_ERR](#ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2) = BIT(19) , [SD\_R1\_CC\_ERR](#ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d) = BIT(20) , [SD\_R1\_ECC\_FAIL](#ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870) = BIT(21) ,     [SD\_R1\_ILLEGAL\_CMD](#ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc) = BIT(22) , [SD\_R1\_CRC\_ERR](#ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2) = BIT(23) , [SD\_R1\_UNLOCK\_FAIL](#ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65) = BIT(24) , [SD\_R1\_CARD\_LOCKED](#ad38162e32b87d3c01f1ae46d3423155aa02d458f5c51dfb7554e17bad1acb591a) = BIT(25) ,     [SD\_R1\_WP\_VIOLATION](#ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab) = BIT(26) , [SD\_R1\_ERASE\_PARAM](#ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21) = BIT(27) , [SD\_R1\_ERASE\_SEQ\_ERR](#ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae) = BIT(28) , [SD\_R1\_BLOCK\_LEN\_ERR](#ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254) = BIT(29) ,     [SD\_R1\_ADDR\_ERR](#ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4) = BIT(30) , [SD\_R1\_OUT\_OF\_RANGE](#ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf) = BIT(31) , [SD\_R1\_ERR\_FLAGS](#ad38162e32b87d3c01f1ae46d3423155aab6413ec799d46c7341e48f0b5146f400) , [SD\_R1ERR\_NONE](#ad38162e32b87d3c01f1ae46d3423155aab8635ae93d3d927f662e88c9e55305eb) = 0   } |
|  | Native SD mode R1 response status flags. [More...](#ad38162e32b87d3c01f1ae46d3423155a) |
| enum | [sd\_r1\_current\_state](#aa0686c333989b0551d3af5eb01de4065) {     [SDMMC\_R1\_IDLE](#aa0686c333989b0551d3af5eb01de4065a081f03ba34d8cd168ab5d4172d3c8d6a) = 0U , [SDMMC\_R1\_READY](#aa0686c333989b0551d3af5eb01de4065a135f072a7d9ee5967a49f7a164816854) = 1U , [SDMMC\_R1\_IDENTIFY](#aa0686c333989b0551d3af5eb01de4065a1ddcc2a60e6f83538151fc93ad434ddf) = 2U , [SDMMC\_R1\_STANDBY](#aa0686c333989b0551d3af5eb01de4065ac906ebc564bfc63a7f4ce0350db6667b) = 3U ,     [SDMMC\_R1\_TRANSFER](#aa0686c333989b0551d3af5eb01de4065a59ead4a70e76c9b2d6c817f4e2847998) = 4U , [SDMMC\_R1\_SEND\_DATA](#aa0686c333989b0551d3af5eb01de4065a5d6d02968e18dd84af3583d282179e64) = 5U , [SDMMC\_R1\_RECIVE\_DATA](#aa0686c333989b0551d3af5eb01de4065a3feb7a1594dc32703d2fbf6e43e77c0c) = 6U , [SDMMC\_R1\_PROGRAM](#aa0686c333989b0551d3af5eb01de4065acccc283c3dc4a36992e76ea0b6f4d68b) = 7U ,     [SDMMC\_R1\_DISCONNECT](#aa0686c333989b0551d3af5eb01de4065abebe32c9b1e107c729f4e6ecf501ee1e) = 8U   } |
|  | SD current state values. [More...](#aa0686c333989b0551d3af5eb01de4065) |
| enum | [sd\_spi\_r1\_error\_flag](#aaf06bb2dcb6e359e08bae37d2f36bbc3) {     [SD\_SPI\_R1PARAMETER\_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3aae5e5c58313c1216448474da513ca2b6) = BIT(6) , [SD\_SPI\_R1ADDRESS\_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3ae50961a0eb0f59776a156facf51e4620) = BIT(5) , [SD\_SPI\_R1ERASE\_SEQ\_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3aa07d3031debe394b369d93fde728d406) = BIT(4) , [SD\_SPI\_R1CMD\_CRC\_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3ae4785671c3a4dca332c10c9bc0a72fba) = BIT(3) ,     [SD\_SPI\_R1ILLEGAL\_CMD\_ERR](#aaf06bb2dcb6e359e08bae37d2f36bbc3a0a59356a4db1abd3f72a8c9778b04e66) = BIT(2) , [SD\_SPI\_R1ERASE\_RESET](#aaf06bb2dcb6e359e08bae37d2f36bbc3a4eb47f187f4aee8228b09a37d4669a4f) = BIT(1) , [SD\_SPI\_R1IDLE\_STATE](#aaf06bb2dcb6e359e08bae37d2f36bbc3a9c77ef6b4da1f8ac56ebe8be03504b69) = BIT(0)   } |
|  | SPI SD mode R1 response status flags. [More...](#aaf06bb2dcb6e359e08bae37d2f36bbc3) |
| enum | [sd\_spi\_r2\_status](#aa1b9e80034c783cc7ff43dc79ac5878f) {     [SDHC\_SPI\_R2\_CARD\_LOCKED](#aa1b9e80034c783cc7ff43dc79ac5878fa8f693e2ff4acfb3d652106fc25f8758f) = BIT(8) , [SDHC\_SPI\_R2\_UNLOCK\_FAIL](#aa1b9e80034c783cc7ff43dc79ac5878fa3f8fde9c17c04f4500f5a86cf4d9e7df) = BIT(9) , [SDHC\_SPI\_R2\_ERR](#aa1b9e80034c783cc7ff43dc79ac5878faf74a4730cc3507a35179fe09da721a19) = BIT(10) , [SDHC\_SPI\_R2\_CC\_ERR](#aa1b9e80034c783cc7ff43dc79ac5878fad33e5499a36259f5b881ce524a1f4159) = BIT(11) ,     [SDHC\_SPI\_R2\_ECC\_FAIL](#aa1b9e80034c783cc7ff43dc79ac5878fac853010c32e85d30f9f5936851ac4ddb) = BIT(12) , [SDHC\_SPI\_R2\_WP\_VIOLATION](#aa1b9e80034c783cc7ff43dc79ac5878fa92bcd0ee78ddba8dc551c7917a37a792) = BIT(13) , [SDHC\_SPI\_R2\_ERASE\_PARAM](#aa1b9e80034c783cc7ff43dc79ac5878fa47bb6389f20ceb840612266fedac0f7a) = BIT(14) , [SDHC\_SPI\_R2\_OUT\_OF\_RANGE](#aa1b9e80034c783cc7ff43dc79ac5878faedbd66fd01bb87a4f55291c299589db7) = BIT(15)   } |
|  | SPI SD mode R2 response status flags. [More...](#aa1b9e80034c783cc7ff43dc79ac5878f) |
| enum | [sd\_rsp\_type](#a1cfd2df5ec76eeb915fd3689408a65d6) {     [SD\_RSP\_TYPE\_NONE](#a1cfd2df5ec76eeb915fd3689408a65d6ad74407536823c1ea3afdf41d4b858b1c) = 0U , [SD\_RSP\_TYPE\_R1](#a1cfd2df5ec76eeb915fd3689408a65d6a92718e4bd4bccaa2fe4a8780228004d7) = 1U , [SD\_RSP\_TYPE\_R1b](#a1cfd2df5ec76eeb915fd3689408a65d6ae64496ba1520651f8bac35af2531eaf8) = 2U , [SD\_RSP\_TYPE\_R2](#a1cfd2df5ec76eeb915fd3689408a65d6a96e26220a32f9b6e9e0bdd8c94d48eaf) = 3U ,     [SD\_RSP\_TYPE\_R3](#a1cfd2df5ec76eeb915fd3689408a65d6af779f08bfb2fd73a717ea3789ccad509) = 4U , [SD\_RSP\_TYPE\_R4](#a1cfd2df5ec76eeb915fd3689408a65d6a34b03331e8f7a9ea6b67da6b68c7e0ed) = 5U , [SD\_RSP\_TYPE\_R5](#a1cfd2df5ec76eeb915fd3689408a65d6a91e216f8a1753b4719ee91819a926dde) = 6U , [SD\_RSP\_TYPE\_R5b](#a1cfd2df5ec76eeb915fd3689408a65d6a5dcd82e4fe5a34646a617a5031fdc638) = 7U ,     [SD\_RSP\_TYPE\_R6](#a1cfd2df5ec76eeb915fd3689408a65d6a3532733bc007df5009801bd6f09e45c9) = 8U , [SD\_RSP\_TYPE\_R7](#a1cfd2df5ec76eeb915fd3689408a65d6aa5657942fb906d58ef2b7bed05137f23) = 9U , [SD\_SPI\_RSP\_TYPE\_R1](#a1cfd2df5ec76eeb915fd3689408a65d6a32b2c65c90d0d5b8df5e4a82e9b95a6d) = (1U << 4) , [SD\_SPI\_RSP\_TYPE\_R1b](#a1cfd2df5ec76eeb915fd3689408a65d6a22413680849a7645c7e8c585b5184203) = (2U << 4) ,     [SD\_SPI\_RSP\_TYPE\_R2](#a1cfd2df5ec76eeb915fd3689408a65d6a855f8e4399cf3ce0c05c6089f3439ec2) = (3U << 4) , [SD\_SPI\_RSP\_TYPE\_R3](#a1cfd2df5ec76eeb915fd3689408a65d6a7c44711a51e8175ebcaf4be24e2daec3) = (4U << 4) , [SD\_SPI\_RSP\_TYPE\_R4](#a1cfd2df5ec76eeb915fd3689408a65d6a4c35ca3a8db652008204cf0cfc8e2339) = (5U << 4) , [SD\_SPI\_RSP\_TYPE\_R5](#a1cfd2df5ec76eeb915fd3689408a65d6a0d82c7d93c187de5c40c0ff83fe8a478) = (6U << 4) ,     [SD\_SPI\_RSP\_TYPE\_R7](#a1cfd2df5ec76eeb915fd3689408a65d6a78472618e8523bf73ca65aee6b0a8318) = (7U << 4)   } |
|  | SD response types. [More...](#a1cfd2df5ec76eeb915fd3689408a65d6) |
| enum | [sd\_support\_flag](#afeec7c838fcf2d5c01cf653e305c749a) {     [SD\_HIGH\_CAPACITY\_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa104798e5266441d5a2f356f50b01cb35) = BIT(1) , [SD\_4BITS\_WIDTH](#afeec7c838fcf2d5c01cf653e305c749aa2511277c6c4ebe38bc7179312292710b) = BIT(2) , [SD\_SDHC\_FLAG](#afeec7c838fcf2d5c01cf653e305c749aad9777c04b150a28916f894f54417286c) = BIT(3) , [SD\_SDXC\_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa0558ef06a64c10456d220e66a5bc0f8b) = BIT(4) ,     [SD\_1800MV\_FLAG](#afeec7c838fcf2d5c01cf653e305c749aab78269976cbb673b4e00d6059ec38f80) = BIT(5) , [SD\_3000MV\_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa5458d4988d7076d854bd695307771858) = BIT(6) , [SD\_CMD23\_FLAG](#afeec7c838fcf2d5c01cf653e305c749aac1f502da56d7d50b70898329da1ad21a) = BIT(7) , [SD\_SPEED\_CLASS\_CONTROL\_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa02b4afca69adad8d7f220b8e4a76db45) = BIT(8) ,     [SD\_MEM\_PRESENT\_FLAG](#afeec7c838fcf2d5c01cf653e305c749aa923c57b4134ad360ed3f6abbabfa87f1) = BIT(9)   } |
|  | SD support flags. [More...](#afeec7c838fcf2d5c01cf653e305c749a) |
| enum | [sd\_ocr\_flag](#a7b20cc85df2d9f5ce6c010907d7d5c61) {     [SD\_OCR\_PWR\_BUSY\_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a5f680f7a518294d7a706b73bbecbdb73) = BIT(31) , [SD\_OCR\_HOST\_CAP\_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a) = BIT(30) , [SD\_OCR\_CARD\_CAP\_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a4cfc3b5856c525eda63b3a8b5fce5ae2) = SD\_OCR\_HOST\_CAP\_FLAG , [SD\_OCR\_SWITCH\_18\_REQ\_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d) = BIT(24) ,     [SD\_OCR\_SWITCH\_18\_ACCEPT\_FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a541be7abf94851538a38f69c2ecb6b5f) = SD\_OCR\_SWITCH\_18\_REQ\_FLAG , [SD\_OCR\_VDD27\_28FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61acd85dd4f874ed9088e6d7a2260d7bc50) = BIT(15) , [SD\_OCR\_VDD28\_29FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a76356316ead27df98dac310eed775707) = BIT(16) , [SD\_OCR\_VDD29\_30FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a624191bea93e1a350073fe2e5d5adaf1) = BIT(17) ,     [SD\_OCR\_VDD30\_31FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a98c205ed0f08df1a2f9e2801f02bbe7f) = BIT(18) , [SD\_OCR\_VDD31\_32FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a8ae4a104d50c0bdcae4722de0d5ee605) = BIT(19) , [SD\_OCR\_VDD32\_33FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a0c8a74f1b50f574b64184bf1cdc1458f) = BIT(20) , [SD\_OCR\_VDD33\_34FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61aca49de7bd24df65fd6448a7e570b04a8) = BIT(21) ,     [SD\_OCR\_VDD34\_35FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61ae5e13b78bf3fdece36190e48136927bf) = BIT(22) , [SD\_OCR\_VDD35\_36FLAG](#a7b20cc85df2d9f5ce6c010907d7d5c61a83a9f603da11b75f200d3bb62528cda4) = BIT(23)   } |
|  | SD OCR bit flags. [More...](#a7b20cc85df2d9f5ce6c010907d7d5c61) |
| enum | [mmc\_ocr\_flag](#a0769bcc2f15d43383f4e5a6c845c51aa) {     [MMC\_OCR\_VDD170\_195FLAG](#a0769bcc2f15d43383f4e5a6c845c51aaa01aef2529fc39dc455c0fb8f2e9cc434) = BIT(7) , [MMC\_OCR\_VDD20\_26FLAG](#a0769bcc2f15d43383f4e5a6c845c51aaa984a5e7f75a4418ca29141f5c6031d1e) = 0x7F << 8 , [MMC\_OCR\_VDD27\_36FLAG](#a0769bcc2f15d43383f4e5a6c845c51aaa239f02ae958dc3e25032825bb4c067e7) = 0x1FF << 15 , [MMC\_OCR\_SECTOR\_MODE](#a0769bcc2f15d43383f4e5a6c845c51aaa669934175190e5416a0d04c3c94acb4b) = BIT(30) ,     [MMC\_OCR\_PWR\_BUSY\_FLAG](#a0769bcc2f15d43383f4e5a6c845c51aaa7127f5d946ea6bb4ec19b96033aafc4b) = BIT(31)   } |
|  | MMC OCR bit flags. [More...](#a0769bcc2f15d43383f4e5a6c845c51aa) |
| enum | [sdio\_ocr\_flag](#a296cbe236e9e36dc79ca30eb54e6bcc6) {     [SDIO\_OCR\_IO\_READY\_FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6adb3e45e84da812297359d6054baa69ba) = BIT(31) , [SDIO\_OCR\_IO\_NUMBER](#a296cbe236e9e36dc79ca30eb54e6bcc6a17007c3d37f047e6db56491a4230e8a8) = (7U << 28U) , [SDIO\_OCR\_MEM\_PRESENT\_FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6ae923fdf459570657220ec225cbed7336) = BIT(27) , [SDIO\_OCR\_180\_VOL\_FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a3f6ebe270ba873bab3407ee7d655b53d) = BIT(24) ,     [SDIO\_OCR\_VDD20\_21FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6aa7a656a21495fbf64666b2b80236e4e4) = BIT(8) , [SDIO\_OCR\_VDD21\_22FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6ad75d7d47a3d5fcc39a68c08546e9793b) = BIT(9) , [SDIO\_OCR\_VDD22\_23FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a560f91eb371bfea5cf6c5c036cc9c096) = BIT(10) , [SDIO\_OCR\_VDD23\_24FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a89c4025349ece0021cd627101f0efdd1) = BIT(11) ,     [SDIO\_OCR\_VDD24\_25FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a6323aa0a8cbfb59f8209a37c8135079c) = BIT(12) , [SDIO\_OCR\_VDD25\_26FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6ac0aa0897e1bbf45b0f5f4de73d733477) = BIT(13) , [SDIO\_OCR\_VDD26\_27FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a4d32525a631342d78f73b6296e148666) = BIT(14) , [SDIO\_OCR\_VDD27\_28FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a1f043936c614ac39b75f3835dc498b94) = BIT(15) ,     [SDIO\_OCR\_VDD28\_29FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a1071312f18c64077e6964e421ef00ead) = BIT(16) , [SDIO\_OCR\_VDD29\_30FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a246619651470476238452550068db8a0) = BIT(17) , [SDIO\_OCR\_VDD30\_31FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a4cb1cc23687e7a1854d8af0c76876a20) = BIT(18) , [SDIO\_OCR\_VDD31\_32FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a018af73c25e22c6e5313e5e3cff57e92) = BIT(19) ,     [SDIO\_OCR\_VDD32\_33FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6ac5613e6858d2c9217165ab4cbb240012) = BIT(20) , [SDIO\_OCR\_VDD33\_34FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a6673f837fa5a98b573886c5e6429c644) = BIT(21) , [SDIO\_OCR\_VDD34\_35FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6a3d791855e6df402d5bfd92ce216a9a4b) = BIT(22) , [SDIO\_OCR\_VDD35\_36FLAG](#a296cbe236e9e36dc79ca30eb54e6bcc6af0baaa7f71d144c7e5edade4b2445813) = BIT(23)   } |
|  | SDIO OCR bit flags. [More...](#a296cbe236e9e36dc79ca30eb54e6bcc6) |
| enum | [sd\_switch\_arg](#a76f7ea4b395028ad5d8cc5eee32656e3) { [SD\_SWITCH\_CHECK](#a76f7ea4b395028ad5d8cc5eee32656e3ae126f56fd639cbd686321a088d1e05e6) = 0U , [SD\_SWITCH\_SET](#a76f7ea4b395028ad5d8cc5eee32656e3a72c39e3140ddd3990c3cbe7c6c867bb1) = 1U } |
|  | SD switch arguments. [More...](#a76f7ea4b395028ad5d8cc5eee32656e3) |
| enum | [sd\_group\_num](#a97f4810585247f5fed41110413e49853) { [SD\_GRP\_TIMING\_MODE](#a97f4810585247f5fed41110413e49853a488b1aac4a0658c8b04b94b7556a2c5b) = 0U , [SD\_GRP\_CMD\_SYS\_MODE](#a97f4810585247f5fed41110413e49853a8c620d198b195d913ad3ff913434d764) = 1U , [SD\_GRP\_DRIVER\_STRENGTH\_MODE](#a97f4810585247f5fed41110413e49853a5e617dd9de3620481b89e517bd2c3a4b) = 2U , [SD\_GRP\_CURRENT\_LIMIT\_MODE](#a97f4810585247f5fed41110413e49853aa38ef885442708891b4ddc4a83c6ff66) = 3U } |
|  | SD switch group numbers. [More...](#a97f4810585247f5fed41110413e49853) |
| enum | [hs\_max\_data\_rate](#a2093143614e52f69e173289391d7e91c) { [HS\_MAX\_DTR](#a2093143614e52f69e173289391d7e91ca10f805e3f66366474428718cb4569da0) = 50000000 } |
| enum | [sd\_bus\_speed](#a6b42b86d8f2ba4f29787c7c6f3d97f36) {     [UHS\_SDR12\_BUS\_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a30f38c9e54bed572ca315fdeb9122103) = BIT(0) , [HIGH\_SPEED\_BUS\_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a5593992de690adb1022b7926d1508ab3) = BIT(1) , [UHS\_SDR25\_BUS\_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36ae07a7ef1ffce64bab52c5f6612a96716) = BIT(1) , [UHS\_SDR50\_BUS\_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a360c72912e023e5b21363f3701deaa50) = BIT(2) ,     [UHS\_SDR104\_BUS\_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36aef2ef100dab4187c8600ea721e8726dd) = BIT(3) , [UHS\_DDR50\_BUS\_SPEED](#a6b42b86d8f2ba4f29787c7c6f3d97f36a022acb9d379c5ecf9935150ec6f51ffc) = BIT(4)   } |
|  | SD bus speed support bit flags. [More...](#a6b42b86d8f2ba4f29787c7c6f3d97f36) |
| enum | [sd\_timing\_mode](#ae82da8038d71cf36ce2237504b498930) {     [SD\_TIMING\_SDR12](#ae82da8038d71cf36ce2237504b498930aea7ebe2a07e1ed7727262d522815355b) = 0U , [SD\_TIMING\_SDR25](#ae82da8038d71cf36ce2237504b498930a433d8a39f77a612dd8104ca49c71a76f) = 1U , [SD\_TIMING\_SDR50](#ae82da8038d71cf36ce2237504b498930a787fb937df1275cb3d169e1dade2fb37) = 2U , [SD\_TIMING\_SDR104](#ae82da8038d71cf36ce2237504b498930aad980a4d433ffcf189a2e77b5d765861) = 3U ,     [SD\_TIMING\_DDR50](#ae82da8038d71cf36ce2237504b498930a88f373b6ac9335667eb8adab49a04e10) = 4U   } |
|  | SD timing mode function selection values. [More...](#ae82da8038d71cf36ce2237504b498930) |
| enum | [sdhc\_clock\_speed](#a9660a61775e481ae4093e11ce9336539) {     [SDMMC\_CLOCK\_400KHZ](#a9660a61775e481ae4093e11ce9336539a16c56ed964cc6bbb5cc6f0cb857d4f10) = 400000U , [SD\_CLOCK\_25MHZ](#a9660a61775e481ae4093e11ce9336539ad5e9d57ee155e1b919f6cc213b05424f) = 25000000U , [SD\_CLOCK\_50MHZ](#a9660a61775e481ae4093e11ce9336539a39e410f7f5c51753bf415f727551b9fb) = 50000000U , [SD\_CLOCK\_100MHZ](#a9660a61775e481ae4093e11ce9336539a66ef44acd4ff3fafc2d49120df4b3c10) = 100000000U ,     [SD\_CLOCK\_208MHZ](#a9660a61775e481ae4093e11ce9336539a9570bb04b0181b4fbdc96cace060d187) = 208000000U , [MMC\_CLOCK\_26MHZ](#a9660a61775e481ae4093e11ce9336539ae9369c1cd7595ab83289fc356e9cc1b6) = 26000000U , [MMC\_CLOCK\_52MHZ](#a9660a61775e481ae4093e11ce9336539a5c37aeeb3c68d7b3dbe8b9001a00507c) = 52000000U , [MMC\_CLOCK\_DDR52](#a9660a61775e481ae4093e11ce9336539a66ecc8c1a73181d70e23424cf718728d) = 52000000U ,     [MMC\_CLOCK\_HS200](#a9660a61775e481ae4093e11ce9336539a14dec2b314ed13974dbba31f33a5eab9) = 200000000U , [MMC\_CLOCK\_HS400](#a9660a61775e481ae4093e11ce9336539a788a77f1e7a468c14ef57319ef8938f3) = 200000000U   } |
|  | SD host controller clock speed. [More...](#a9660a61775e481ae4093e11ce9336539) |
| enum | [sd\_current\_setting](#a5ac0e70389dc6ccec515530df4eab972) { [SD\_SET\_CURRENT\_200MA](#a5ac0e70389dc6ccec515530df4eab972a134ed84475be6f55a0f3d3ae9201cbe9) = 0 , [SD\_SET\_CURRENT\_400MA](#a5ac0e70389dc6ccec515530df4eab972ad548c59ebbb5045e437157cb9186de19) = 1 , [SD\_SET\_CURRENT\_600MA](#a5ac0e70389dc6ccec515530df4eab972a83f1d375e4c5aa645759cc4e4462f8e0) = 2 , [SD\_SET\_CURRENT\_800MA](#a5ac0e70389dc6ccec515530df4eab972af44faa0f33705ecbd37b5f3544105e34) = 3 } |
|  | SD current setting values. [More...](#a5ac0e70389dc6ccec515530df4eab972) |
| enum | [sd\_current\_limit](#a238de48c0cb55d173b6b874f4930c537) { [SD\_MAX\_CURRENT\_200MA](#a238de48c0cb55d173b6b874f4930c537a18b21e5e76bea0263f475ecc228c0301) = BIT(0) , [SD\_MAX\_CURRENT\_400MA](#a238de48c0cb55d173b6b874f4930c537ae0605a0d9fc89e094a40b03e96c02339) = BIT(1) , [SD\_MAX\_CURRENT\_600MA](#a238de48c0cb55d173b6b874f4930c537af82a5f23e51bf3ac3b7bec137269f540) = BIT(2) , [SD\_MAX\_CURRENT\_800MA](#a238de48c0cb55d173b6b874f4930c537a2e3c01bc8d16641d7b500ce1244dbb03) = BIT(3) } |
|  | SD current support bitfield. [More...](#a238de48c0cb55d173b6b874f4930c537) |
| enum | [sd\_driver\_type](#a314c38b1b0603c003e67b5dec2228d4b) { [SD\_DRIVER\_TYPE\_B](#a314c38b1b0603c003e67b5dec2228d4ba32ad0894344bc4980f9206022ed0f877) = 0x1 , [SD\_DRIVER\_TYPE\_A](#a314c38b1b0603c003e67b5dec2228d4ba9eec5ff6f7d4c7512212cb48719dcabf) = 0x2 , [SD\_DRIVER\_TYPE\_C](#a314c38b1b0603c003e67b5dec2228d4ba0cd41f5198ce06ce5925b3f52d48b0a2) = 0x4 , [SD\_DRIVER\_TYPE\_D](#a314c38b1b0603c003e67b5dec2228d4ba435b458d33f1568cb76b77a3ea2e1eb8) = 0x8 } |
|  | SD driver types. [More...](#a314c38b1b0603c003e67b5dec2228d4b) |
| enum | [sd\_driver\_strength](#a66c69cd7d7818af86b6a91fad68334c2) { [SD\_DRV\_STRENGTH\_TYPEB](#a66c69cd7d7818af86b6a91fad68334c2a1b1e411f733ad6c1dc41896744441a48) = 0U , [SD\_DRV\_STRENGTH\_TYPEA](#a66c69cd7d7818af86b6a91fad68334c2ad870ea9b9fc07a4af81bce3c82330441) = 1U , [SD\_DRV\_STRENGTH\_TYPEC](#a66c69cd7d7818af86b6a91fad68334c2aa3e190aa6edb9f6eb7e29b78fc6f1a8a) = 2U , [SD\_DRV\_STRENGTH\_TYPED](#a66c69cd7d7818af86b6a91fad68334c2ad5753bf6fae3f43ef8ce7cb7eb169b61) = 3U } |
|  | SD switch drive type selection. [More...](#a66c69cd7d7818af86b6a91fad68334c2) |
| enum | [mmc\_csd\_freq](#a313c45576db4ae219288fb4fbaad4bd8) {     [MMC\_MAXFREQ\_100KHZ](#a313c45576db4ae219288fb4fbaad4bd8a221dc45c7b73f6f96a63acbeb3e5e121) = 0U << 0U , [MMC\_MAXFREQ\_1MHZ](#a313c45576db4ae219288fb4fbaad4bd8a32c9f5017cd49c9ca4b352269de6eeff) = 1U << 0U , [MMC\_MAXFREQ\_10MHZ](#a313c45576db4ae219288fb4fbaad4bd8af63af4938d5aad64bac19fac42aedd10) = 2U << 0U , [MMC\_MAXFREQ\_100MHZ](#a313c45576db4ae219288fb4fbaad4bd8a13c703d344a1e03c1aa5881a77980085) = 3U << 0U ,     [MMC\_MAXFREQ\_MULT\_10](#a313c45576db4ae219288fb4fbaad4bd8a74d01430b854f42ea84dba9d3ce45b16) = 1U << 3U , [MMC\_MAXFREQ\_MULT\_12](#a313c45576db4ae219288fb4fbaad4bd8a4a3b8dc88c6349fb5f49ed3062a39a17) = 2U << 3U , [MMC\_MAXFREQ\_MULT\_13](#a313c45576db4ae219288fb4fbaad4bd8a2c639715b63769e9a431a93e636f007e) = 3U << 3U , [MMC\_MAXFREQ\_MULT\_15](#a313c45576db4ae219288fb4fbaad4bd8ac988a54239b7d9e182f1b2f480567e66) = 4U << 3U ,     [MMC\_MAXFREQ\_MULT\_20](#a313c45576db4ae219288fb4fbaad4bd8ac8848c5cdf177737744da3283f7140d5) = 5U << 3U , [MMC\_MAXFREQ\_MULT\_26](#a313c45576db4ae219288fb4fbaad4bd8ab1ff3da74a0dea49ffe7ac1d945ec4e6) = 6U << 3U , [MMC\_MAXFREQ\_MULT\_30](#a313c45576db4ae219288fb4fbaad4bd8a69e1d369d668d63071410078a31099a0) = 7U << 3U , [MMC\_MAXFREQ\_MULT\_35](#a313c45576db4ae219288fb4fbaad4bd8a63c0eee223946b1ae2b187bb585dfde4) = 8U << 3U ,     [MMC\_MAXFREQ\_MULT\_40](#a313c45576db4ae219288fb4fbaad4bd8a572d53afafb39341e0cdb80d2d041d2c) = 9U << 3U , [MMC\_MAXFREQ\_MULT\_45](#a313c45576db4ae219288fb4fbaad4bd8a5bd0506d7efbecdc42eb8fae1427dc37) = 0xAU << 3U , [MMC\_MAXFREQ\_MULT\_52](#a313c45576db4ae219288fb4fbaad4bd8a988f18b9f418744721b0fc91f2432449) = 0xBU << 3U , [MMC\_MAXFREQ\_MULT\_55](#a313c45576db4ae219288fb4fbaad4bd8abecfcd6d212185c74b57941c3fa58233) = 0xCU << 3U ,     [MMC\_MAXFREQ\_MULT\_60](#a313c45576db4ae219288fb4fbaad4bd8adf578325509923b46e3ff4fbd74889ad) = 0xDU << 3U , [MMC\_MAXFREQ\_MULT\_70](#a313c45576db4ae219288fb4fbaad4bd8aee24df1d628479fe2d920839a0bf5012) = 0xEU << 3U , [MMC\_MAXFREQ\_MULT\_80](#a313c45576db4ae219288fb4fbaad4bd8a24ea8c9db5531b5404bb667da26ac5d0) = 0xFU << 3u   } |
|  | MMC Maximum Frequency. [More...](#a313c45576db4ae219288fb4fbaad4bd8) |
| enum | [mmc\_timing\_mode](#ae1956c4b374e2c8b6a585596e93ac345) { [MMC\_LEGACY\_TIMING](#ae1956c4b374e2c8b6a585596e93ac345ae51a5474387816c03970aa0f8058b002) = 0U , [MMC\_HS\_TIMING](#ae1956c4b374e2c8b6a585596e93ac345a17160707005c580fbd52dbd6b99699dd) = 1U , [MMC\_HS200\_TIMING](#ae1956c4b374e2c8b6a585596e93ac345a39200c50c7e22c096db3ce1dd3fe78d5) = 2U , [MMC\_HS400\_TIMING](#ae1956c4b374e2c8b6a585596e93ac345a4ea17060afbcd026387172c1af57bb43) = 3U } |
|  | MMC Timing Modes. [More...](#ae1956c4b374e2c8b6a585596e93ac345) |
| enum | [mmc\_driver\_strengths](#af9783799f316cbaed12e18ce9944b09d) {     [mmc\_driv\_type0](#af9783799f316cbaed12e18ce9944b09dabd4f3ffac3f52efe797ce3ee3c31a03f) = 0U , [mmc\_driv\_type1](#af9783799f316cbaed12e18ce9944b09da2cedd0b40bf81afb35792150b2d4964a) = 1U , [mmc\_driv\_type2](#af9783799f316cbaed12e18ce9944b09dafed77d2aed13d59fa6645cb06fc21c43) = 2U , [mmc\_driv\_type3](#af9783799f316cbaed12e18ce9944b09dacf4d28d56a6c4925944ffc99072d46e9) = 3U ,     [mmc\_driv\_type4](#af9783799f316cbaed12e18ce9944b09daf5448a25c8b5a8411f059469112ef2be) = 4U   } |
|  | MMC Driver Strengths. [More...](#af9783799f316cbaed12e18ce9944b09d) |
| enum | [mmc\_ext\_csd\_rev](#ac86d8a44f37c771cb666f69a516dff81) {     [MMC\_5\_1](#ac86d8a44f37c771cb666f69a516dff81ad49da8223b68d35a4d95d6b48bb8a3f7) = 8U , [MMC\_5\_0](#ac86d8a44f37c771cb666f69a516dff81a87a4c0efb7e10cccce939af5f60343ad) = 7U , [MMC\_4\_5](#ac86d8a44f37c771cb666f69a516dff81aa0d4721b24d0cd71d6a8fbfc666a6e7c) = 6U , [MMC\_4\_4](#ac86d8a44f37c771cb666f69a516dff81a43b7acda3747eb2233c2f2a433ff71c7) = 5U ,     [MMC\_4\_3](#ac86d8a44f37c771cb666f69a516dff81a0f4fc7047a7c813b9ada618ed05e09a4) = 3U , [MMC\_4\_2](#ac86d8a44f37c771cb666f69a516dff81a9a960567b8ecbd6feff7e6337fc98567) = 2U , [MMC\_4\_1](#ac86d8a44f37c771cb666f69a516dff81ab84ae4edfcca8ccae2a0df0643d04ca2) = 1U , [MMC\_4\_0](#ac86d8a44f37c771cb666f69a516dff81aba4f3f30eaa7d3368743f78f3c355269) = 0U   } |
|  | CSD Revision. [More...](#ac86d8a44f37c771cb666f69a516dff81) |
| enum | [sd\_csd\_flag](#a98c4f218acfa21e124aa22e9fe209437) {     [SD\_CSD\_READ\_BLK\_PARTIAL\_FLAG](#a98c4f218acfa21e124aa22e9fe209437ac353a0c3c1ac62920efdc42879a81cff) = BIT(0) , [SD\_CSD\_WRITE\_BLK\_MISALIGN\_FLAG](#a98c4f218acfa21e124aa22e9fe209437a16d3fd179853f1f15b980d2b82b572be) = BIT(1) , [SD\_CSD\_READ\_BLK\_MISALIGN\_FLAG](#a98c4f218acfa21e124aa22e9fe209437aca7d98319db6a23b30625828807e2143) = BIT(2) , [SD\_CSD\_DSR\_IMPLEMENTED\_FLAG](#a98c4f218acfa21e124aa22e9fe209437a1258364107909d0c4f8e9b7dba59300c) = BIT(3) ,     [SD\_CSD\_ERASE\_BLK\_EN\_FLAG](#a98c4f218acfa21e124aa22e9fe209437a0d907c1a9e69435433c5bf19bfacbd73) = BIT(4) , [SD\_CSD\_WRITE\_PROTECT\_GRP\_EN\_FLAG](#a98c4f218acfa21e124aa22e9fe209437af85839612e4fcc94eb2bd0986bd1740c) = BIT(5) , [SD\_CSD\_WRITE\_BLK\_PARTIAL\_FLAG](#a98c4f218acfa21e124aa22e9fe209437aa8b8f850196e47799cb9b2cd06650520) = BIT(6) , [SD\_CSD\_FILE\_FMT\_GRP\_FLAG](#a98c4f218acfa21e124aa22e9fe209437a2e75506280c1b4d5866f4dd8f2518be8) = BIT(7) ,     [SD\_CSD\_COPY\_FLAG](#a98c4f218acfa21e124aa22e9fe209437a988758fe0720e6fc33564076e3bc51bf) = BIT(8) , [SD\_CSD\_PERMANENT\_WRITE\_PROTECT\_FLAG](#a98c4f218acfa21e124aa22e9fe209437a7496edd5c7ec694d2d175bf751de1458) = BIT(9) , [SD\_CSD\_TMP\_WRITE\_PROTECT\_FLAG](#a98c4f218acfa21e124aa22e9fe209437aa0c70fee97e29875394efc2a4c2fa274) = BIT(10)   } |
|  | SD card specific data flags. [More...](#a98c4f218acfa21e124aa22e9fe209437) |
| enum | [sd\_scr\_flag](#a476ec98763d90a5cba336cbf22d6d553) { [SD\_SCR\_DATA\_STATUS\_AFTER\_ERASE](#a476ec98763d90a5cba336cbf22d6d553a759c63670d0dd41590fdb940a48ac4dd) = BIT(0) , [SD\_SCR\_SPEC3](#a476ec98763d90a5cba336cbf22d6d553a59fb3a34a7dba6ed1c86bca21cf97871) = BIT(1) } |
|  | SD card configuration register. [More...](#a476ec98763d90a5cba336cbf22d6d553) |
| enum | [sd\_spec\_version](#abf77ec1ad65cc9c99dc930ed7a96301a) { [SD\_SPEC\_VER1\_0](#abf77ec1ad65cc9c99dc930ed7a96301aa39605b86ccfad6196721ddfbb84b33d6) = BIT(0) , [SD\_SPEC\_VER1\_1](#abf77ec1ad65cc9c99dc930ed7a96301aac09ddfacee85353e243d6a8cfe7eeba8) = BIT(1) , [SD\_SPEC\_VER2\_0](#abf77ec1ad65cc9c99dc930ed7a96301aa3525ee751a482ae1cd816e2674ac3160) = BIT(2) , [SD\_SPEC\_VER3\_0](#abf77ec1ad65cc9c99dc930ed7a96301aa9e3d0d084a7d8ad1b9d08e6b699084e6) = BIT(3) } |
|  | SD specification version. [More...](#abf77ec1ad65cc9c99dc930ed7a96301a) |
| enum | [sdio\_func\_num](#a3a542344967c5c1912bde216559e7cd6) {     [SDIO\_FUNC\_NUM\_0](#a3a542344967c5c1912bde216559e7cd6ad7a10f97094ddb96f26ab44fc34de12a) = 0 , [SDIO\_FUNC\_NUM\_1](#a3a542344967c5c1912bde216559e7cd6a900536b934da03f8e8590de3e3d56296) = 1 , [SDIO\_FUNC\_NUM\_2](#a3a542344967c5c1912bde216559e7cd6ac2cc5967daee0a3e9ef61c9c486b3a6c) = 2 , [SDIO\_FUNC\_NUM\_3](#a3a542344967c5c1912bde216559e7cd6adef5748e2622dab22da33504bbafa149) = 3 ,     [SDIO\_FUNC\_NUM\_4](#a3a542344967c5c1912bde216559e7cd6a9b69d64108c6564bc313e4fb2b53f61c) = 4 , [SDIO\_FUNC\_NUM\_5](#a3a542344967c5c1912bde216559e7cd6ac62397290371f5fb3fdf8d4b52fb3575) = 5 , [SDIO\_FUNC\_NUM\_6](#a3a542344967c5c1912bde216559e7cd6a2a9baef178307d6e6006ea88b4da383c) = 6 , [SDIO\_FUNC\_NUM\_7](#a3a542344967c5c1912bde216559e7cd6a617d1991d70033df3b39eef7ccb98b48) = 7 ,     [SDIO\_FUNC\_MEMORY](#a3a542344967c5c1912bde216559e7cd6a075731d15b2f4b7c7448d6d4ee059880) = 8   } |
|  | SDIO function number. [More...](#a3a542344967c5c1912bde216559e7cd6) |
| enum | [sdio\_io\_dir](#a250ae2ce54e941895a720b565632350e) { [SDIO\_IO\_READ](#a250ae2ce54e941895a720b565632350eac1212149d096232e75d1d090abb4974c) = 0 , [SDIO\_IO\_WRITE](#a250ae2ce54e941895a720b565632350eabd26fc6f76267231c78eae8be9ebb885) = 1 } |
|  | SDIO I/O direction. [More...](#a250ae2ce54e941895a720b565632350e) |
| enum | [sdio\_cccr\_flags](#ac12657ae7d3b8abc562d4d7929a86b65) {     [SDIO\_SUPPORT\_HS](#ac12657ae7d3b8abc562d4d7929a86b65aa23a07a4fe6f6dd8292215221d97d5e2) = BIT(0) , [SDIO\_SUPPORT\_SDR50](#ac12657ae7d3b8abc562d4d7929a86b65acc46ce7f993b3eb81c6a2a2daad84c34) = BIT(1) , [SDIO\_SUPPORT\_SDR104](#ac12657ae7d3b8abc562d4d7929a86b65a9b12d90cd1590f68fc1031449c4560ec) = BIT(2) , [SDIO\_SUPPORT\_DDR50](#ac12657ae7d3b8abc562d4d7929a86b65a6d2084ba4c729c2cb019582b975f652f) = BIT(3) ,     [SDIO\_SUPPORT\_4BIT\_LS\_BUS](#ac12657ae7d3b8abc562d4d7929a86b65a6cd553669599181b3677cea94687f025) = BIT(4) , [SDIO\_SUPPORT\_MULTIBLOCK](#ac12657ae7d3b8abc562d4d7929a86b65a364c7067e73960bae74ed80320adb223) = BIT(5)   } |
|  | Card common control register flags. [More...](#ac12657ae7d3b8abc562d4d7929a86b65) |

## Macro Definition Documentation

## [◆ ](#ade9a798f584d431c86e172266394f41e)MMC\_EXT\_CSD\_BYTES

| #define MMC\_EXT\_CSD\_BYTES   512 |
| --- |

## [◆ ](#aed6aacadb061a42993c59d8d69a2f2ab)SD\_IF\_COND\_CHECK

| #define SD\_IF\_COND\_CHECK   0xAA |
| --- |

## [◆ ](#a38157545a4a10dd4757ad1eb80487c60)SD\_IF\_COND\_VHS\_3V3

| #define SD\_IF\_COND\_VHS\_3V3   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a0d10fc7ae53b5bfb6d7f448844820799)SD\_IF\_COND\_VHS\_MASK

| #define SD\_IF\_COND\_VHS\_MASK   (0x0F << 8) |
| --- |

## [◆ ](#a947520a05fc99c25449fab98d0d02b1e)SD\_PRODUCT\_NAME\_BYTES

| #define SD\_PRODUCT\_NAME\_BYTES   5 |
| --- |

## [◆ ](#ac104a7c39f61829092eaffd98663045b)SD\_R1\_CURRENT\_STATE

| #define SD\_R1\_CURRENT\_STATE | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((x) & [SD\_R1\_CUR\_STATE](#ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65)) >> 9U)

[SD\_R1\_CUR\_STATE](#ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65)

@ SD\_R1\_CUR\_STATE

**Definition** sd\_spec.h:93

## [◆ ](#a2d1dee775c3849a92dac9d179bd50a6c)SD\_SPI\_CMD

| #define SD\_SPI\_CMD   0x3F |
| --- |

## [◆ ](#a85e46f60c0ae5f21a4386009bbfaf0a3)SD\_SPI\_CMD\_BODY\_SIZE

| #define SD\_SPI\_CMD\_BODY\_SIZE   ([SD\_SPI\_CMD\_SIZE](#aa841b78f5937f8499918cc977a36e90f) - 1) |
| --- |

## [◆ ](#aa841b78f5937f8499918cc977a36e90f)SD\_SPI\_CMD\_SIZE

| #define SD\_SPI\_CMD\_SIZE   6 |
| --- |

## [◆ ](#aed67a9adbb001dad73eec4054ef6cbc1)SD\_SPI\_CRC16\_SIZE

| #define SD\_SPI\_CRC16\_SIZE   2 |
| --- |

## [◆ ](#a5d36df2e0d1bd88aadc3673cdf12aea7)SD\_SPI\_RESPONSE\_ACCEPTED

| #define SD\_SPI\_RESPONSE\_ACCEPTED   0x05 |
| --- |

## [◆ ](#a3a206f684b2c878f59a394b06abd9814)SD\_SPI\_RESPONSE\_CRC\_ERR

| #define SD\_SPI\_RESPONSE\_CRC\_ERR   0x0B |
| --- |

## [◆ ](#a498f76218e054dff0e524a83ac90ccd1)SD\_SPI\_RESPONSE\_WRITE\_ERR

| #define SD\_SPI\_RESPONSE\_WRITE\_ERR   0x0C |
| --- |

## [◆ ](#a7da6535d451c1062f8d0c92f5688e178)SD\_SPI\_START

| #define SD\_SPI\_START   0x80 |
| --- |

## [◆ ](#ae34cf95537f2c0963ade18f1ba5d6e20)SD\_SPI\_TOKEN\_MULTI\_WRITE

| #define SD\_SPI\_TOKEN\_MULTI\_WRITE   0xFC |
| --- |

## [◆ ](#a7cd4fbf7d5ce2e8eba8c795a675486bb)SD\_SPI\_TOKEN\_SINGLE

| #define SD\_SPI\_TOKEN\_SINGLE   0xFE |
| --- |

## [◆ ](#a9d4f357ff29ee3b5483505404ba3c956)SD\_SPI\_TOKEN\_STOP\_TRAN

| #define SD\_SPI\_TOKEN\_STOP\_TRAN   0xFD |
| --- |

## [◆ ](#a2283409131ac9ede90773b256094b74c)SD\_SPI\_TX

| #define SD\_SPI\_TX   0x40 |
| --- |

## [◆ ](#a7e061818bc8f923d5342c38721a1a501)SDIO\_CCCR\_ABORT

| #define SDIO\_CCCR\_ABORT   0x06 |
| --- |

SDIO IO abort register.

## [◆ ](#a283f2b2f2c28b3c8208f3d6aca3ca3d2)SDIO\_CCCR\_BUS\_IF

| #define SDIO\_CCCR\_BUS\_IF   0x07 |
| --- |

SDIO bus interface control register.

## [◆ ](#aec58e3fcda2f792266fbd8ab1b75f98c)SDIO\_CCCR\_BUS\_IF\_WIDTH\_1\_BIT

| #define SDIO\_CCCR\_BUS\_IF\_WIDTH\_1\_BIT   0x00 |
| --- |

1 bit SDIO bus setting

## [◆ ](#aeb23fa771a16f69fcb9d97b156f25ade)SDIO\_CCCR\_BUS\_IF\_WIDTH\_4\_BIT

| #define SDIO\_CCCR\_BUS\_IF\_WIDTH\_4\_BIT   0x02 |
| --- |

4 bit SDIO bus setting

## [◆ ](#ade7a14837ee90c8ce24959926d81eaee)SDIO\_CCCR\_BUS\_IF\_WIDTH\_8\_BIT

| #define SDIO\_CCCR\_BUS\_IF\_WIDTH\_8\_BIT   0x03 |
| --- |

8 bit SDIO bus setting

## [◆ ](#a6c04dc28d7f39fda7cd0181421a13ea0)SDIO\_CCCR\_BUS\_IF\_WIDTH\_MASK

| #define SDIO\_CCCR\_BUS\_IF\_WIDTH\_MASK   0x3 |
| --- |

SDIO bus width setting mask.

## [◆ ](#a0b878d7e794d3edd127c3f08633efbbc)SDIO\_CCCR\_CAPS

| #define SDIO\_CCCR\_CAPS   0x08 |
| --- |

SDIO card capabilities.

## [◆ ](#a7ba2dcf801f81ab53b418e59441000ae)SDIO\_CCCR\_CAPS\_BLS

| #define SDIO\_CCCR\_CAPS\_BLS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

low speed card with 4 bit support

## [◆ ](#aa8281a65d0865fba8b85d91d00b90091)SDIO\_CCCR\_CAPS\_E4MI

| #define SDIO\_CCCR\_CAPS\_E4MI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

enable block gap interrupt

## [◆ ](#aee93278e3c0ec4cbf0e3065d6a58f516)SDIO\_CCCR\_CAPS\_LSC

| #define SDIO\_CCCR\_CAPS\_LSC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

low speed card

## [◆ ](#a74082cfafdd9e8bfa37e92624ff75e80)SDIO\_CCCR\_CAPS\_S4MI

| #define SDIO\_CCCR\_CAPS\_S4MI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

support block gap interrupt

## [◆ ](#a7550fe8aab011fc87baeb575463e27d9)SDIO\_CCCR\_CAPS\_SBS

| #define SDIO\_CCCR\_CAPS\_SBS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

support bus control

## [◆ ](#affb9533b340f5424c1f42445c6f1002f)SDIO\_CCCR\_CAPS\_SDC

| #define SDIO\_CCCR\_CAPS\_SDC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

support CMD52 while data transfer

## [◆ ](#aaaf8d335a8d025b998feeb93c0899a99)SDIO\_CCCR\_CAPS\_SMB

| #define SDIO\_CCCR\_CAPS\_SMB   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

support multiple block transfer

## [◆ ](#a8011927f7b565304ec31a7e61d403d6e)SDIO\_CCCR\_CAPS\_SRW

| #define SDIO\_CCCR\_CAPS\_SRW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

support read wait control

## [◆ ](#ae211fa0bfa6809273b5f7267c95ce681)SDIO\_CCCR\_CCCR

| #define SDIO\_CCCR\_CCCR   0x00 |
| --- |

Card common control register definitions.

Card common control registers, present on all SDIO cards SDIO CCCR revision register

## [◆ ](#ab240215a68f23ec69e901c0666b0dfe0)SDIO\_CCCR\_CCCR\_REV\_1\_00

| #define SDIO\_CCCR\_CCCR\_REV\_1\_00   0x0 |
| --- |

CCCR/FBR Version 1.00.

## [◆ ](#aace4672360d77085bec93b52e3ac05d9)SDIO\_CCCR\_CCCR\_REV\_1\_10

| #define SDIO\_CCCR\_CCCR\_REV\_1\_10   0x1 |
| --- |

CCCR/FBR Version 1.10.

## [◆ ](#a566200e9322e8e4c9b3edd21a2ced93c)SDIO\_CCCR\_CCCR\_REV\_2\_00

| #define SDIO\_CCCR\_CCCR\_REV\_2\_00   0x2 |
| --- |

CCCR/FBR Version 2.00.

## [◆ ](#aa90600f74ff69315e38ed1c10a3cde7c)SDIO\_CCCR\_CCCR\_REV\_3\_00

| #define SDIO\_CCCR\_CCCR\_REV\_3\_00   0x3 |
| --- |

CCCR/FBR Version 3.00.

## [◆ ](#accf473b0fcdc9e1e03329f91e588de1a)SDIO\_CCCR\_CCCR\_REV\_MASK

| #define SDIO\_CCCR\_CCCR\_REV\_MASK   0x0F |
| --- |

## [◆ ](#af5db599ebd0748528e8369653a5e3929)SDIO\_CCCR\_CCCR\_REV\_SHIFT

| #define SDIO\_CCCR\_CCCR\_REV\_SHIFT   0x0 |
| --- |

## [◆ ](#a8f97c16c091bd19b545bbe452581dfff)SDIO\_CCCR\_CIS

| #define SDIO\_CCCR\_CIS   0x09 |
| --- |

SDIO CIS tuples pointer.

## [◆ ](#a3a5d01e688b18109ad2f19bc5d017f26)SDIO\_CCCR\_DRIVE\_STRENGTH

| #define SDIO\_CCCR\_DRIVE\_STRENGTH   0x15 |
| --- |

SDIO drive strength.

## [◆ ](#a759a9dddc3aa08d0f11114637c5b69ff)SDIO\_CCCR\_DRIVE\_STRENGTH\_A

| #define SDIO\_CCCR\_DRIVE\_STRENGTH\_A   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

drive type A

## [◆ ](#a8487f5a0a97e5f1f72500cf44cec89dc)SDIO\_CCCR\_DRIVE\_STRENGTH\_C

| #define SDIO\_CCCR\_DRIVE\_STRENGTH\_C   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

drive type C

## [◆ ](#abc1ed41094d9cdd300b1b3712bb082b2)SDIO\_CCCR\_DRIVE\_STRENGTH\_D

| #define SDIO\_CCCR\_DRIVE\_STRENGTH\_D   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

drive type D

## [◆ ](#a15caca2936186b54c330b4a9050c9795)SDIO\_CCCR\_INT\_EN

| #define SDIO\_CCCR\_INT\_EN   0x04 |
| --- |

SDIO Interrupt enable register.

## [◆ ](#a81b7523a76a1826a14c2cc1c242a49a9)SDIO\_CCCR\_INT\_P

| #define SDIO\_CCCR\_INT\_P   0x05 |
| --- |

SDIO Interrupt pending register.

## [◆ ](#a0b2103011690e1d3f1daef4e45a11986)SDIO\_CCCR\_IO\_EN

| #define SDIO\_CCCR\_IO\_EN   0x02 |
| --- |

SDIO IO Enable register.

## [◆ ](#a6cfa2671e574650e6f35a65828cd459c)SDIO\_CCCR\_IO\_RD

| #define SDIO\_CCCR\_IO\_RD   0x03 |
| --- |

SDIO IO Ready register.

## [◆ ](#aafc2b0c434dff4a0903e4910181f9e81)SDIO\_CCCR\_SD

| #define SDIO\_CCCR\_SD   0x01 |
| --- |

SD spec version register.

## [◆ ](#aa425236b097f44a9721e7aedd203ff90)SDIO\_CCCR\_SD\_SPEC\_MASK

| #define SDIO\_CCCR\_SD\_SPEC\_MASK   0x0F |
| --- |

## [◆ ](#a223defa20d223655d215065b222a6767)SDIO\_CCCR\_SD\_SPEC\_SHIFT

| #define SDIO\_CCCR\_SD\_SPEC\_SHIFT   0x0 |
| --- |

## [◆ ](#a05edbcb4a98831cbeac509f26e881de8)SDIO\_CCCR\_SPEED

| #define SDIO\_CCCR\_SPEED   0x13 |
| --- |

SDIO bus speed select.

## [◆ ](#ad3dc3009d2d78a6306c3247ab85ef48d)SDIO\_CCCR\_SPEED\_DDR50

| #define SDIO\_CCCR\_SPEED\_DDR50   0x4 |
| --- |

select DDR50

## [◆ ](#acb3bdd73bace425a94a357a2f0bff4ef)SDIO\_CCCR\_SPEED\_HS

| #define SDIO\_CCCR\_SPEED\_HS   0x1 |
| --- |

select High speed mode

## [◆ ](#a1a1817554f886a999484e2663432cd8b)SDIO\_CCCR\_SPEED\_MASK

| #define SDIO\_CCCR\_SPEED\_MASK   0xE |
| --- |

bus speed select mask

## [◆ ](#a0d51f98d56303dd55177245785748158)SDIO\_CCCR\_SPEED\_SDR104

| #define SDIO\_CCCR\_SPEED\_SDR104   0x3 |
| --- |

select SDR104

## [◆ ](#a9ee7aec8589aceb8555917971ab9afd3)SDIO\_CCCR\_SPEED\_SDR12

| #define SDIO\_CCCR\_SPEED\_SDR12   0x0 |
| --- |

select SDR12

## [◆ ](#afabf4bb10bed3295d1d051c113e61545)SDIO\_CCCR\_SPEED\_SDR25

| #define SDIO\_CCCR\_SPEED\_SDR25   0x1 |
| --- |

select SDR25

## [◆ ](#a81bc96279a19618c9212674757abd141)SDIO\_CCCR\_SPEED\_SDR50

| #define SDIO\_CCCR\_SPEED\_SDR50   0x2 |
| --- |

select SDR50

## [◆ ](#a38d57134d99e2dfc5760fcf7312b6cd5)SDIO\_CCCR\_SPEED\_SHIFT

| #define SDIO\_CCCR\_SPEED\_SHIFT   0x1 |
| --- |

bus speed select shift

## [◆ ](#a964759dc76bd2a9f9f9dce5c21dc2cb4)SDIO\_CCCR\_SPEED\_SHS

| #define SDIO\_CCCR\_SPEED\_SHS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

high speed support

## [◆ ](#afb72ff0aa5b90446db296af16bf9bb02)SDIO\_CCCR\_UHS

| #define SDIO\_CCCR\_UHS   0x14 |
| --- |

SDIO UHS support.

## [◆ ](#a2678ede1ac974a9670fdcaa393682aa6)SDIO\_CCCR\_UHS\_DDR50

| #define SDIO\_CCCR\_UHS\_DDR50   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

DDR50 support.

## [◆ ](#aca4fee68fdf3480ec8cf7de7b46a8d4e)SDIO\_CCCR\_UHS\_SDR104

| #define SDIO\_CCCR\_UHS\_SDR104   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

SDR104 support.

## [◆ ](#a9965d399115bca8574a9beaeac9b9f31)SDIO\_CCCR\_UHS\_SDR50

| #define SDIO\_CCCR\_UHS\_SDR50   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

SDR50 support.

## [◆ ](#acd6e41030a8d16419cc22adf9f0a5509)SDIO\_CMD\_ARG\_FUNC\_NUM\_SHIFT

| #define SDIO\_CMD\_ARG\_FUNC\_NUM\_SHIFT   28 |
| --- |

function number shift

## [◆ ](#a338e9606baa6937e0887e7a9b9372c23)SDIO\_CMD\_ARG\_REG\_ADDR\_MASK

| #define SDIO\_CMD\_ARG\_REG\_ADDR\_MASK   0x1FFFF |
| --- |

direct reg addr mask

## [◆ ](#aa74dbe588f1f5ca248cf0f5a2e8e8c81)SDIO\_CMD\_ARG\_REG\_ADDR\_SHIFT

| #define SDIO\_CMD\_ARG\_REG\_ADDR\_SHIFT   9 |
| --- |

direct reg addr shift

## [◆ ](#a960ade30c404ebb08769c5870ac21b37)SDIO\_CMD\_ARG\_RW\_SHIFT

| #define SDIO\_CMD\_ARG\_RW\_SHIFT   31 |
| --- |

read/write flag shift

## [◆ ](#afadddcc143b78325505a40544c04e3b0)SDIO\_DIRECT\_CMD\_ARG\_RAW\_SHIFT

| #define SDIO\_DIRECT\_CMD\_ARG\_RAW\_SHIFT   27 |
| --- |

direct raw flag shift

## [◆ ](#a5ab9e1e0c96e7166b1ff7a208f90001d)SDIO\_DIRECT\_CMD\_DATA\_MASK

| #define SDIO\_DIRECT\_CMD\_DATA\_MASK   0xFF |
| --- |

data mask

## [◆ ](#ac6c49ad6118debe7a9e64f412e597f22)SDIO\_EXTEND\_CMD\_ARG\_BLK\_SHIFT

| #define SDIO\_EXTEND\_CMD\_ARG\_BLK\_SHIFT   27 |
| --- |

extended write block mode

## [◆ ](#a73ca83a4884f13fa5de8500f69252bef)SDIO\_EXTEND\_CMD\_ARG\_OP\_CODE\_SHIFT

| #define SDIO\_EXTEND\_CMD\_ARG\_OP\_CODE\_SHIFT   26 |
| --- |

op code (increment address)

## [◆ ](#a2ff95d19f7f60ce33b17b69e2672e7e5)SDIO\_FBR\_BASE

| #define SDIO\_FBR\_BASE | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((n) \* 0x100)

Get function base register addr.

## [◆ ](#af1885023615980d5cbb930538cc201a6)SDIO\_FBR\_BLK\_SIZE

| #define SDIO\_FBR\_BLK\_SIZE   0x10 |
| --- |

SDIO function base register block size.

## [◆ ](#aea0ed052a9d94d2e2b96931752975858)SDIO\_FBR\_CIS

| #define SDIO\_FBR\_CIS   0x09 |
| --- |

SDIO function base register CIS pointer.

## [◆ ](#a28fb27484353eb075d501b1ad7a76112)SDIO\_FBR\_CSA

| #define SDIO\_FBR\_CSA   0x0C |
| --- |

SDIO function base register CSA pointer.

## [◆ ](#a0d98fd7cd6f67b28981c6e01f8805a01)SDIO\_IO\_OCR\_MASK

| #define SDIO\_IO\_OCR\_MASK   0xFFFFFF |
| --- |

## [◆ ](#a845866f4f88c280f8414b727e0d77edf)SDIO\_MAX\_IO\_NUMS

| #define SDIO\_MAX\_IO\_NUMS   7 |
| --- |

Maximum number of I/O functions for SDIO.

## [◆ ](#a23690672048afbc75ce2c2f4d9a74144)SDIO\_OCR\_IO\_NUMBER\_SHIFT

| #define SDIO\_OCR\_IO\_NUMBER\_SHIFT   28 |
| --- |

## [◆ ](#a21e0771f38a22f93c9f4167d8b36f608)SDIO\_TPL\_CODE\_END

| #define SDIO\_TPL\_CODE\_END   0xFF |
| --- |

End CIS tuple code.

## [◆ ](#ac263bf61bcc750880bae34dde62d61e4)SDIO\_TPL\_CODE\_FUNCE

| #define SDIO\_TPL\_CODE\_FUNCE   0x22 |
| --- |

function extension CIS tuple code

## [◆ ](#aae6f9377eccdbd5866f1a393e083c5e4)SDIO\_TPL\_CODE\_FUNCID

| #define SDIO\_TPL\_CODE\_FUNCID   0x21 |
| --- |

function ID CIS tuple code

## [◆ ](#af1983253320b45a2a1a2aab28c09e08f)SDIO\_TPL\_CODE\_MANIFID

| #define SDIO\_TPL\_CODE\_MANIFID   0x20 |
| --- |

manufacturer ID CIS tuple code

## [◆ ](#afadae8a1db38d93b909b3f2c5b0e0110)SDIO\_TPL\_CODE\_NULL

| #define SDIO\_TPL\_CODE\_NULL   0x00 |
| --- |

NULL CIS tuple code.

## [◆ ](#a523a28eeec3d0a71f0d7ca49ab397960)SDMMC\_DEFAULT\_BLOCK\_SIZE

| #define SDMMC\_DEFAULT\_BLOCK\_SIZE   512 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a2093143614e52f69e173289391d7e91c)hs\_max\_data\_rate

| enum [hs\_max\_data\_rate](#a2093143614e52f69e173289391d7e91c) |
| --- |

| Enumerator | |
| --- | --- |
| HS\_MAX\_DTR |  |

## [◆ ](#a313c45576db4ae219288fb4fbaad4bd8)mmc\_csd\_freq

| enum [mmc\_csd\_freq](#a313c45576db4ae219288fb4fbaad4bd8) |
| --- |

MMC Maximum Frequency.

Max freq in MMC csd

| Enumerator | |
| --- | --- |
| MMC\_MAXFREQ\_100KHZ |  |
| MMC\_MAXFREQ\_1MHZ |  |
| MMC\_MAXFREQ\_10MHZ |  |
| MMC\_MAXFREQ\_100MHZ |  |
| MMC\_MAXFREQ\_MULT\_10 |  |
| MMC\_MAXFREQ\_MULT\_12 |  |
| MMC\_MAXFREQ\_MULT\_13 |  |
| MMC\_MAXFREQ\_MULT\_15 |  |
| MMC\_MAXFREQ\_MULT\_20 |  |
| MMC\_MAXFREQ\_MULT\_26 |  |
| MMC\_MAXFREQ\_MULT\_30 |  |
| MMC\_MAXFREQ\_MULT\_35 |  |
| MMC\_MAXFREQ\_MULT\_40 |  |
| MMC\_MAXFREQ\_MULT\_45 |  |
| MMC\_MAXFREQ\_MULT\_52 |  |
| MMC\_MAXFREQ\_MULT\_55 |  |
| MMC\_MAXFREQ\_MULT\_60 |  |
| MMC\_MAXFREQ\_MULT\_70 |  |
| MMC\_MAXFREQ\_MULT\_80 |  |

## [◆ ](#af9783799f316cbaed12e18ce9944b09d)mmc\_driver\_strengths

| enum [mmc\_driver\_strengths](#af9783799f316cbaed12e18ce9944b09d) |
| --- |

MMC Driver Strengths.

Encoded in EXT\_CSD

| Enumerator | |
| --- | --- |
| mmc\_driv\_type0 |  |
| mmc\_driv\_type1 |  |
| mmc\_driv\_type2 |  |
| mmc\_driv\_type3 |  |
| mmc\_driv\_type4 |  |

## [◆ ](#ac86d8a44f37c771cb666f69a516dff81)mmc\_ext\_csd\_rev

| enum [mmc\_ext\_csd\_rev](#ac86d8a44f37c771cb666f69a516dff81) |
| --- |

CSD Revision.

Value of CSD rev in EXT\_CSD

| Enumerator | |
| --- | --- |
| MMC\_5\_1 |  |
| MMC\_5\_0 |  |
| MMC\_4\_5 |  |
| MMC\_4\_4 |  |
| MMC\_4\_3 |  |
| MMC\_4\_2 |  |
| MMC\_4\_1 |  |
| MMC\_4\_0 |  |

## [◆ ](#a0769bcc2f15d43383f4e5a6c845c51aa)mmc\_ocr\_flag

| enum [mmc\_ocr\_flag](#a0769bcc2f15d43383f4e5a6c845c51aa) |
| --- |

MMC OCR bit flags.

bit flags present in MMC OCR response. Used to determine status and supported functions of MMC card.

| Enumerator | |
| --- | --- |
| MMC\_OCR\_VDD170\_195FLAG |  |
| MMC\_OCR\_VDD20\_26FLAG |  |
| MMC\_OCR\_VDD27\_36FLAG |  |
| MMC\_OCR\_SECTOR\_MODE |  |
| MMC\_OCR\_PWR\_BUSY\_FLAG |  |

## [◆ ](#ae1956c4b374e2c8b6a585596e93ac345)mmc\_timing\_mode

| enum [mmc\_timing\_mode](#ae1956c4b374e2c8b6a585596e93ac345) |
| --- |

MMC Timing Modes.

MMC Timing Mode, encoded in EXT\_CSD

| Enumerator | |
| --- | --- |
| MMC\_LEGACY\_TIMING |  |
| MMC\_HS\_TIMING |  |
| MMC\_HS200\_TIMING |  |
| MMC\_HS400\_TIMING |  |

## [◆ ](#a1c77191f9cb8c50e8e2a03cda2984dbc)sd\_app\_cmd

| enum [sd\_app\_cmd](#a1c77191f9cb8c50e8e2a03cda2984dbc) |
| --- |

SD application command opcodes.

all application command opcodes must be prefixed with a CMD55 command to inform the SD card the next command is an application-specific one.

| Enumerator | |
| --- | --- |
| SD\_APP\_SET\_BUS\_WIDTH |  |
| SD\_APP\_SEND\_STATUS |  |
| SD\_APP\_SEND\_NUM\_WRITTEN\_BLK |  |
| SD\_APP\_SET\_WRITE\_BLK\_ERASE\_CNT |  |
| SD\_APP\_SEND\_OP\_COND |  |
| SD\_APP\_CLEAR\_CARD\_DETECT |  |
| SD\_APP\_SEND\_SCR |  |

## [◆ ](#a6b42b86d8f2ba4f29787c7c6f3d97f36)sd\_bus\_speed

| enum [sd\_bus\_speed](#a6b42b86d8f2ba4f29787c7c6f3d97f36) |
| --- |

SD bus speed support bit flags.

Bit flags indicating support for SD bus speeds. these bit flags are provided as a response to CMD6 by the card

| Enumerator | |
| --- | --- |
| UHS\_SDR12\_BUS\_SPEED |  |
| HIGH\_SPEED\_BUS\_SPEED |  |
| UHS\_SDR25\_BUS\_SPEED |  |
| UHS\_SDR50\_BUS\_SPEED |  |
| UHS\_SDR104\_BUS\_SPEED |  |
| UHS\_DDR50\_BUS\_SPEED |  |

## [◆ ](#a98c4f218acfa21e124aa22e9fe209437)sd\_csd\_flag

| enum [sd\_csd\_flag](#a98c4f218acfa21e124aa22e9fe209437) |
| --- |

SD card specific data flags.

flags used in decoding the SD card specific data register

| Enumerator | |
| --- | --- |
| SD\_CSD\_READ\_BLK\_PARTIAL\_FLAG | Partial blocks for read allowed [79:79]. |
| SD\_CSD\_WRITE\_BLK\_MISALIGN\_FLAG | Write block misalignment [78:78]. |
| SD\_CSD\_READ\_BLK\_MISALIGN\_FLAG | Read block misalignment [77:77]. |
| SD\_CSD\_DSR\_IMPLEMENTED\_FLAG | DSR implemented [76:76]. |
| SD\_CSD\_ERASE\_BLK\_EN\_FLAG | Erase single block enabled [46:46]. |
| SD\_CSD\_WRITE\_PROTECT\_GRP\_EN\_FLAG | Write protect group enabled [31:31]. |
| SD\_CSD\_WRITE\_BLK\_PARTIAL\_FLAG | Partial blocks for write allowed [21:21]. |
| SD\_CSD\_FILE\_FMT\_GRP\_FLAG | File format group [15:15]. |
| SD\_CSD\_COPY\_FLAG | Copy flag [14:14]. |
| SD\_CSD\_PERMANENT\_WRITE\_PROTECT\_FLAG | Permanent write protection [13:13]. |
| SD\_CSD\_TMP\_WRITE\_PROTECT\_FLAG | Temporary write protection [12:12]. |

## [◆ ](#a238de48c0cb55d173b6b874f4930c537)sd\_current\_limit

| enum [sd\_current\_limit](#a238de48c0cb55d173b6b874f4930c537) |
| --- |

SD current support bitfield.

Used with CMD6 to determine the maximum current the card will draw.

| Enumerator | |
| --- | --- |
| SD\_MAX\_CURRENT\_200MA | default current limit |
| SD\_MAX\_CURRENT\_400MA | current limit to 400MA |
| SD\_MAX\_CURRENT\_600MA | current limit to 600MA |
| SD\_MAX\_CURRENT\_800MA | current limit to 800MA |

## [◆ ](#a5ac0e70389dc6ccec515530df4eab972)sd\_current\_setting

| enum [sd\_current\_setting](#a5ac0e70389dc6ccec515530df4eab972) |
| --- |

SD current setting values.

Used with CMD6 to inform the card what its maximum current draw is.

| Enumerator | |
| --- | --- |
| SD\_SET\_CURRENT\_200MA |  |
| SD\_SET\_CURRENT\_400MA |  |
| SD\_SET\_CURRENT\_600MA |  |
| SD\_SET\_CURRENT\_800MA |  |

## [◆ ](#a66c69cd7d7818af86b6a91fad68334c2)sd\_driver\_strength

| enum [sd\_driver\_strength](#a66c69cd7d7818af86b6a91fad68334c2) |
| --- |

SD switch drive type selection.

These values are used to select the preferred driver type for an SD card.

| Enumerator | |
| --- | --- |
| SD\_DRV\_STRENGTH\_TYPEB | default driver strength |
| SD\_DRV\_STRENGTH\_TYPEA | driver strength TYPE A |
| SD\_DRV\_STRENGTH\_TYPEC | driver strength TYPE C |
| SD\_DRV\_STRENGTH\_TYPED | driver strength TYPE D |

## [◆ ](#a314c38b1b0603c003e67b5dec2228d4b)sd\_driver\_type

| enum [sd\_driver\_type](#a314c38b1b0603c003e67b5dec2228d4b) |
| --- |

SD driver types.

Used with CMD6 to determine the driver type the card should use.

| Enumerator | |
| --- | --- |
| SD\_DRIVER\_TYPE\_B |  |
| SD\_DRIVER\_TYPE\_A |  |
| SD\_DRIVER\_TYPE\_C |  |
| SD\_DRIVER\_TYPE\_D |  |

## [◆ ](#a97f4810585247f5fed41110413e49853)sd\_group\_num

| enum [sd\_group\_num](#a97f4810585247f5fed41110413e49853) |
| --- |

SD switch group numbers.

SD CMD6 has multiple function groups it can check/set. These indicies are used to determine which group CMD6 will interact with.

| Enumerator | |
| --- | --- |
| SD\_GRP\_TIMING\_MODE | access mode group |
| SD\_GRP\_CMD\_SYS\_MODE | command system group |
| SD\_GRP\_DRIVER\_STRENGTH\_MODE | driver strength group |
| SD\_GRP\_CURRENT\_LIMIT\_MODE | current limit group |

## [◆ ](#a7b20cc85df2d9f5ce6c010907d7d5c61)sd\_ocr\_flag

| enum [sd\_ocr\_flag](#a7b20cc85df2d9f5ce6c010907d7d5c61) |
| --- |

SD OCR bit flags.

bit flags present in SD OCR response. Used to determine status and supported functions of SD card.

| Enumerator | |
| --- | --- |
| SD\_OCR\_PWR\_BUSY\_FLAG | Power up busy status. |
| SD\_OCR\_HOST\_CAP\_FLAG | Card capacity status. |
| SD\_OCR\_CARD\_CAP\_FLAG | Card capacity status. |
| SD\_OCR\_SWITCH\_18\_REQ\_FLAG | Switch to 1.8V request. |
| SD\_OCR\_SWITCH\_18\_ACCEPT\_FLAG | Switch to 1.8V accepted. |
| SD\_OCR\_VDD27\_28FLAG | VDD 2.7-2.8. |
| SD\_OCR\_VDD28\_29FLAG | VDD 2.8-2.9. |
| SD\_OCR\_VDD29\_30FLAG | VDD 2.9-3.0. |
| SD\_OCR\_VDD30\_31FLAG | VDD 2.9-3.0. |
| SD\_OCR\_VDD31\_32FLAG | VDD 3.0-3.1. |
| SD\_OCR\_VDD32\_33FLAG | VDD 3.1-3.2. |
| SD\_OCR\_VDD33\_34FLAG | VDD 3.2-3.3. |
| SD\_OCR\_VDD34\_35FLAG | VDD 3.3-3.4. |
| SD\_OCR\_VDD35\_36FLAG | VDD 3.4-3.5. |

## [◆ ](#a072705601a34c697515f74acb0474c99)sd\_opcode

| enum [sd\_opcode](#a072705601a34c697515f74acb0474c99) |
| --- |

SD specification command opcodes.

SD specification command opcodes. Note that some command opcodes are specific to SDIO cards, or cards running in SPI mode instead of native SD mode.

| Enumerator | |
| --- | --- |
| SD\_GO\_IDLE\_STATE |  |
| MMC\_SEND\_OP\_COND |  |
| SD\_ALL\_SEND\_CID |  |
| SD\_SEND\_RELATIVE\_ADDR |  |
| MMC\_SEND\_RELATIVE\_ADDR |  |
| SDIO\_SEND\_OP\_COND |  |
| SD\_SWITCH |  |
| SD\_SELECT\_CARD |  |
| SD\_SEND\_IF\_COND |  |
| MMC\_SEND\_EXT\_CSD |  |
| SD\_SEND\_CSD |  |
| SD\_SEND\_CID |  |
| SD\_VOL\_SWITCH |  |
| SD\_STOP\_TRANSMISSION |  |
| SD\_SEND\_STATUS |  |
| MMC\_CHECK\_BUS\_TEST |  |
| SD\_GO\_INACTIVE\_STATE |  |
| SD\_SET\_BLOCK\_SIZE |  |
| SD\_READ\_SINGLE\_BLOCK |  |
| SD\_READ\_MULTIPLE\_BLOCK |  |
| SD\_SEND\_TUNING\_BLOCK |  |
| MMC\_SEND\_BUS\_TEST |  |
| MMC\_SEND\_TUNING\_BLOCK |  |
| SD\_SET\_BLOCK\_COUNT |  |
| SD\_WRITE\_SINGLE\_BLOCK |  |
| SD\_WRITE\_MULTIPLE\_BLOCK |  |
| SD\_ERASE\_BLOCK\_START |  |
| SD\_ERASE\_BLOCK\_END |  |
| SD\_ERASE\_BLOCK\_OPERATION |  |
| SDIO\_RW\_DIRECT |  |
| SDIO\_RW\_EXTENDED |  |
| SD\_APP\_CMD |  |
| SD\_SPI\_READ\_OCR |  |
| SD\_SPI\_CRC\_ON\_OFF |  |

## [◆ ](#aa0686c333989b0551d3af5eb01de4065)sd\_r1\_current\_state

| enum [sd\_r1\_current\_state](#aa0686c333989b0551d3af5eb01de4065) |
| --- |

SD current state values.

SD current state values, contained in R1 response data.

| Enumerator | |
| --- | --- |
| SDMMC\_R1\_IDLE |  |
| SDMMC\_R1\_READY |  |
| SDMMC\_R1\_IDENTIFY |  |
| SDMMC\_R1\_STANDBY |  |
| SDMMC\_R1\_TRANSFER |  |
| SDMMC\_R1\_SEND\_DATA |  |
| SDMMC\_R1\_RECIVE\_DATA |  |
| SDMMC\_R1\_PROGRAM |  |
| SDMMC\_R1\_DISCONNECT |  |

## [◆ ](#ad38162e32b87d3c01f1ae46d3423155a)sd\_r1\_status

| enum [sd\_r1\_status](#ad38162e32b87d3c01f1ae46d3423155a) |
| --- |

Native SD mode R1 response status flags.

Native response flags for SD R1 response, used to check for error in command.

| Enumerator | |
| --- | --- |
| SD\_R1\_AUTH\_ERR |  |
| SD\_R1\_APP\_CMD |  |
| SD\_R1\_FX\_EVENT |  |
| SD\_R1\_RDY\_DATA |  |
| SD\_R1\_CUR\_STATE |  |
| SD\_R1\_ERASE\_RESET |  |
| SD\_R1\_ECC\_DISABLED |  |
| SD\_R1\_ERASE\_SKIP |  |
| SD\_R1\_CSD\_OVERWRITE |  |
| SD\_R1\_ERR |  |
| SD\_R1\_CC\_ERR |  |
| SD\_R1\_ECC\_FAIL |  |
| SD\_R1\_ILLEGAL\_CMD |  |
| SD\_R1\_CRC\_ERR |  |
| SD\_R1\_UNLOCK\_FAIL |  |
| SD\_R1\_CARD\_LOCKED |  |
| SD\_R1\_WP\_VIOLATION |  |
| SD\_R1\_ERASE\_PARAM |  |
| SD\_R1\_ERASE\_SEQ\_ERR |  |
| SD\_R1\_BLOCK\_LEN\_ERR |  |
| SD\_R1\_ADDR\_ERR |  |
| SD\_R1\_OUT\_OF\_RANGE |  |
| SD\_R1\_ERR\_FLAGS |  |
| SD\_R1ERR\_NONE |  |

## [◆ ](#a1cfd2df5ec76eeb915fd3689408a65d6)sd\_rsp\_type

| enum [sd\_rsp\_type](#a1cfd2df5ec76eeb915fd3689408a65d6) |
| --- |

SD response types.

SD response types. Note that SPI mode has difference response types than cards in native SD mode.

| Enumerator | |
| --- | --- |
| SD\_RSP\_TYPE\_NONE |  |
| SD\_RSP\_TYPE\_R1 |  |
| SD\_RSP\_TYPE\_R1b |  |
| SD\_RSP\_TYPE\_R2 |  |
| SD\_RSP\_TYPE\_R3 |  |
| SD\_RSP\_TYPE\_R4 |  |
| SD\_RSP\_TYPE\_R5 |  |
| SD\_RSP\_TYPE\_R5b |  |
| SD\_RSP\_TYPE\_R6 |  |
| SD\_RSP\_TYPE\_R7 |  |
| SD\_SPI\_RSP\_TYPE\_R1 |  |
| SD\_SPI\_RSP\_TYPE\_R1b |  |
| SD\_SPI\_RSP\_TYPE\_R2 |  |
| SD\_SPI\_RSP\_TYPE\_R3 |  |
| SD\_SPI\_RSP\_TYPE\_R4 |  |
| SD\_SPI\_RSP\_TYPE\_R5 |  |
| SD\_SPI\_RSP\_TYPE\_R7 |  |

## [◆ ](#a476ec98763d90a5cba336cbf22d6d553)sd\_scr\_flag

| enum [sd\_scr\_flag](#a476ec98763d90a5cba336cbf22d6d553) |
| --- |

SD card configuration register.

flags used in decoding the SD card configuration register

| Enumerator | |
| --- | --- |
| SD\_SCR\_DATA\_STATUS\_AFTER\_ERASE | Data status after erases [55:55]. |
| SD\_SCR\_SPEC3 | Specification version 3.00 or higher [47:47]. |

## [◆ ](#abf77ec1ad65cc9c99dc930ed7a96301a)sd\_spec\_version

| enum [sd\_spec\_version](#abf77ec1ad65cc9c99dc930ed7a96301a) |
| --- |

SD specification version.

SD spec version flags used in decoding the SD card configuration register

| Enumerator | |
| --- | --- |
| SD\_SPEC\_VER1\_0 | SD card version 1.0-1.01. |
| SD\_SPEC\_VER1\_1 | SD card version 1.10. |
| SD\_SPEC\_VER2\_0 | SD card version 2.00. |
| SD\_SPEC\_VER3\_0 | SD card version 3.0. |

## [◆ ](#aaf06bb2dcb6e359e08bae37d2f36bbc3)sd\_spi\_r1\_error\_flag

| enum [sd\_spi\_r1\_error\_flag](#aaf06bb2dcb6e359e08bae37d2f36bbc3) |
| --- |

SPI SD mode R1 response status flags.

SPI mode R1 response flags. Used to check for error in SD SPI mode command.

| Enumerator | |
| --- | --- |
| SD\_SPI\_R1PARAMETER\_ERR |  |
| SD\_SPI\_R1ADDRESS\_ERR |  |
| SD\_SPI\_R1ERASE\_SEQ\_ERR |  |
| SD\_SPI\_R1CMD\_CRC\_ERR |  |
| SD\_SPI\_R1ILLEGAL\_CMD\_ERR |  |
| SD\_SPI\_R1ERASE\_RESET |  |
| SD\_SPI\_R1IDLE\_STATE |  |

## [◆ ](#aa1b9e80034c783cc7ff43dc79ac5878f)sd\_spi\_r2\_status

| enum [sd\_spi\_r2\_status](#aa1b9e80034c783cc7ff43dc79ac5878f) |
| --- |

SPI SD mode R2 response status flags.

SPI mode R2 response flags. Sent in response to SEND\_STATUS command. Used to check status of SD card.

| Enumerator | |
| --- | --- |
| SDHC\_SPI\_R2\_CARD\_LOCKED |  |
| SDHC\_SPI\_R2\_UNLOCK\_FAIL |  |
| SDHC\_SPI\_R2\_ERR |  |
| SDHC\_SPI\_R2\_CC\_ERR |  |
| SDHC\_SPI\_R2\_ECC\_FAIL |  |
| SDHC\_SPI\_R2\_WP\_VIOLATION |  |
| SDHC\_SPI\_R2\_ERASE\_PARAM |  |
| SDHC\_SPI\_R2\_OUT\_OF\_RANGE |  |

## [◆ ](#afeec7c838fcf2d5c01cf653e305c749a)sd\_support\_flag

| enum [sd\_support\_flag](#afeec7c838fcf2d5c01cf653e305c749a) |
| --- |

SD support flags.

flags used by SD subsystem to determine support for SD card features.

| Enumerator | |
| --- | --- |
| SD\_HIGH\_CAPACITY\_FLAG |  |
| SD\_4BITS\_WIDTH |  |
| SD\_SDHC\_FLAG |  |
| SD\_SDXC\_FLAG |  |
| SD\_1800MV\_FLAG |  |
| SD\_3000MV\_FLAG |  |
| SD\_CMD23\_FLAG |  |
| SD\_SPEED\_CLASS\_CONTROL\_FLAG |  |
| SD\_MEM\_PRESENT\_FLAG |  |

## [◆ ](#a76f7ea4b395028ad5d8cc5eee32656e3)sd\_switch\_arg

| enum [sd\_switch\_arg](#a76f7ea4b395028ad5d8cc5eee32656e3) |
| --- |

SD switch arguments.

SD CMD6 can either check or set a function. Bitfields are used to indicate feature support when checking a function, and when setting a function an integer value is used to select it.

| Enumerator | |
| --- | --- |
| SD\_SWITCH\_CHECK | SD switch mode 0: check function. |
| SD\_SWITCH\_SET | SD switch mode 1: set function. |

## [◆ ](#ae82da8038d71cf36ce2237504b498930)sd\_timing\_mode

| enum [sd\_timing\_mode](#ae82da8038d71cf36ce2237504b498930) |
| --- |

SD timing mode function selection values.

sent to the card via CMD6 to select a card speed, and used by SD host controller to identify timing of card.

| Enumerator | |
| --- | --- |
| SD\_TIMING\_SDR12 | Default mode & SDR12. |
| SD\_TIMING\_SDR25 | High speed mode & SDR25. |
| SD\_TIMING\_SDR50 | SDR50 mode. |
| SD\_TIMING\_SDR104 | SDR104 mode. |
| SD\_TIMING\_DDR50 | DDR50 mode. |

## [◆ ](#a9660a61775e481ae4093e11ce9336539)sdhc\_clock\_speed

| enum [sdhc\_clock\_speed](#a9660a61775e481ae4093e11ce9336539) |
| --- |

SD host controller clock speed.

Controls the SD host controller clock speed on the SD bus.

| Enumerator | |
| --- | --- |
| SDMMC\_CLOCK\_400KHZ |  |
| SD\_CLOCK\_25MHZ |  |
| SD\_CLOCK\_50MHZ |  |
| SD\_CLOCK\_100MHZ |  |
| SD\_CLOCK\_208MHZ |  |
| MMC\_CLOCK\_26MHZ |  |
| MMC\_CLOCK\_52MHZ |  |
| MMC\_CLOCK\_DDR52 |  |
| MMC\_CLOCK\_HS200 |  |
| MMC\_CLOCK\_HS400 |  |

## [◆ ](#ac12657ae7d3b8abc562d4d7929a86b65)sdio\_cccr\_flags

| enum [sdio\_cccr\_flags](#ac12657ae7d3b8abc562d4d7929a86b65) |
| --- |

Card common control register flags.

flags to indicate capabilities supported by an SDIO card, read from the CCCR registers

| Enumerator | |
| --- | --- |
| SDIO\_SUPPORT\_HS |  |
| SDIO\_SUPPORT\_SDR50 |  |
| SDIO\_SUPPORT\_SDR104 |  |
| SDIO\_SUPPORT\_DDR50 |  |
| SDIO\_SUPPORT\_4BIT\_LS\_BUS |  |
| SDIO\_SUPPORT\_MULTIBLOCK |  |

## [◆ ](#a3a542344967c5c1912bde216559e7cd6)sdio\_func\_num

| enum [sdio\_func\_num](#a3a542344967c5c1912bde216559e7cd6) |
| --- |

SDIO function number.

SDIO function number used to select function when performing I/O on SDIO card

| Enumerator | |
| --- | --- |
| SDIO\_FUNC\_NUM\_0 |  |
| SDIO\_FUNC\_NUM\_1 |  |
| SDIO\_FUNC\_NUM\_2 |  |
| SDIO\_FUNC\_NUM\_3 |  |
| SDIO\_FUNC\_NUM\_4 |  |
| SDIO\_FUNC\_NUM\_5 |  |
| SDIO\_FUNC\_NUM\_6 |  |
| SDIO\_FUNC\_NUM\_7 |  |
| SDIO\_FUNC\_MEMORY |  |

## [◆ ](#a250ae2ce54e941895a720b565632350e)sdio\_io\_dir

| enum [sdio\_io\_dir](#a250ae2ce54e941895a720b565632350e) |
| --- |

SDIO I/O direction.

SDIO I/O direction (read or write)

| Enumerator | |
| --- | --- |
| SDIO\_IO\_READ |  |
| SDIO\_IO\_WRITE |  |

## [◆ ](#a296cbe236e9e36dc79ca30eb54e6bcc6)sdio\_ocr\_flag

| enum [sdio\_ocr\_flag](#a296cbe236e9e36dc79ca30eb54e6bcc6) |
| --- |

SDIO OCR bit flags.

bit flags present in SDIO OCR response. Used to determine status and supported functions of SDIO card.

| Enumerator | |
| --- | --- |
| SDIO\_OCR\_IO\_READY\_FLAG |  |
| SDIO\_OCR\_IO\_NUMBER | Number of io function. |
| SDIO\_OCR\_MEM\_PRESENT\_FLAG | Memory present flag. |
| SDIO\_OCR\_180\_VOL\_FLAG | Switch to 1.8v signalling. |
| SDIO\_OCR\_VDD20\_21FLAG | VDD 2.0-2.1. |
| SDIO\_OCR\_VDD21\_22FLAG | VDD 2.1-2.2. |
| SDIO\_OCR\_VDD22\_23FLAG | VDD 2.2-2.3. |
| SDIO\_OCR\_VDD23\_24FLAG | VDD 2.3-2.4. |
| SDIO\_OCR\_VDD24\_25FLAG | VDD 2.4-2.5. |
| SDIO\_OCR\_VDD25\_26FLAG | VDD 2.5-2.6. |
| SDIO\_OCR\_VDD26\_27FLAG | VDD 2.6-2.7. |
| SDIO\_OCR\_VDD27\_28FLAG | VDD 2.7-2.8. |
| SDIO\_OCR\_VDD28\_29FLAG | VDD 2.8-2.9. |
| SDIO\_OCR\_VDD29\_30FLAG | VDD 2.9-3.0. |
| SDIO\_OCR\_VDD30\_31FLAG | VDD 2.9-3.0. |
| SDIO\_OCR\_VDD31\_32FLAG | VDD 3.0-3.1. |
| SDIO\_OCR\_VDD32\_33FLAG | VDD 3.1-3.2. |
| SDIO\_OCR\_VDD33\_34FLAG | VDD 3.2-3.3. |
| SDIO\_OCR\_VDD34\_35FLAG | VDD 3.3-3.4. |
| SDIO\_OCR\_VDD35\_36FLAG | VDD 3.4-3.5. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sd](dir_ff091b3f4b9505cc58dad89321d1c232.md)
- [sd\_spec.h](sd__spec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
