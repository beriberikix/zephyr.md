---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sd__spec_8h_source.html
original_path: doxygen/html/sd__spec_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd\_spec.h

[Go to the documentation of this file.](sd__spec_8h.md)

1/\*

2 \* Copyright 2022-2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* SD card specification

9 \*/

10

11#ifndef ZEPHYR\_SUBSYS\_SD\_SPEC\_H\_

12#define ZEPHYR\_SUBSYS\_SD\_SPEC\_H\_

13

14#include <[stdint.h](stdint_8h.md)>

15#include <[zephyr/sys/util.h](sys_2util_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 28](sd__spec_8h.md#a072705601a34c697515f74acb0474c99)enum [sd\_opcode](sd__spec_8h.md#a072705601a34c697515f74acb0474c99) {

[ 29](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a9dcb2e5fb6a5a53c6cb02422fd1fef3c) [SD\_GO\_IDLE\_STATE](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a9dcb2e5fb6a5a53c6cb02422fd1fef3c) = 0,

[ 30](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a54546b311e446754738a9b6f1e3eaea4) [MMC\_SEND\_OP\_COND](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a54546b311e446754738a9b6f1e3eaea4) = 1,

[ 31](sd__spec_8h.md#a072705601a34c697515f74acb0474c99affcc3d18f6bda30fb3fd34916d8f61fe) [SD\_ALL\_SEND\_CID](sd__spec_8h.md#a072705601a34c697515f74acb0474c99affcc3d18f6bda30fb3fd34916d8f61fe) = 2,

[ 32](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a35c39a93dfcc239fcb80db70449af99e) [SD\_SEND\_RELATIVE\_ADDR](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a35c39a93dfcc239fcb80db70449af99e) = 3,

[ 33](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a56c94068ecb32eb9ced47d4a3bf95481) [MMC\_SEND\_RELATIVE\_ADDR](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a56c94068ecb32eb9ced47d4a3bf95481) = 3,

[ 34](sd__spec_8h.md#a072705601a34c697515f74acb0474c99af48c850f0aa9e9f9dbce8fc8855f6a2a) [SDIO\_SEND\_OP\_COND](sd__spec_8h.md#a072705601a34c697515f74acb0474c99af48c850f0aa9e9f9dbce8fc8855f6a2a) = 5, /\* SDIO cards only \*/

[ 35](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a400dc3acd2ae8320f130dbea80c81969) [SD\_SWITCH](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a400dc3acd2ae8320f130dbea80c81969) = 6,

[ 36](sd__spec_8h.md#a072705601a34c697515f74acb0474c99afa15c17b4fb95747b444616b085b4905) [SD\_SELECT\_CARD](sd__spec_8h.md#a072705601a34c697515f74acb0474c99afa15c17b4fb95747b444616b085b4905) = 7,

[ 37](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a0da09225692b10e51140d4f15ba1dd0a) [SD\_SEND\_IF\_COND](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a0da09225692b10e51140d4f15ba1dd0a) = 8,

[ 38](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7c9bfc788861214fae86e22443e9484a) [MMC\_SEND\_EXT\_CSD](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7c9bfc788861214fae86e22443e9484a) = 8,

[ 39](sd__spec_8h.md#a072705601a34c697515f74acb0474c99adc7e589c9352cddf856b2e868f93a097) [SD\_SEND\_CSD](sd__spec_8h.md#a072705601a34c697515f74acb0474c99adc7e589c9352cddf856b2e868f93a097) = 9,

[ 40](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a8c3edf14ca3a6e04c1949a40cd3fb135) [SD\_SEND\_CID](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a8c3edf14ca3a6e04c1949a40cd3fb135) = 10,

[ 41](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ad6d6f1ccdabc2970ac2ab6c7a853b37e) [SD\_VOL\_SWITCH](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ad6d6f1ccdabc2970ac2ab6c7a853b37e) = 11,

[ 42](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa5f2d8c27d0b7ae780734cb4bedbf8a4) [SD\_STOP\_TRANSMISSION](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa5f2d8c27d0b7ae780734cb4bedbf8a4) = 12,

[ 43](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ad822462692847b4e8433157cd75eef70) [SD\_SEND\_STATUS](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ad822462692847b4e8433157cd75eef70) = 13,

[ 44](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a45bc2d4b117d144ef5191719f9b6c297) [MMC\_CHECK\_BUS\_TEST](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a45bc2d4b117d144ef5191719f9b6c297) = 14,

[ 45](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a5c85e3208bb686d8ded9ae0fe7bd9d53) [SD\_GO\_INACTIVE\_STATE](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a5c85e3208bb686d8ded9ae0fe7bd9d53) = 15,

[ 46](sd__spec_8h.md#a072705601a34c697515f74acb0474c99abd97c835c80320637579c692d6f57878) [SD\_SET\_BLOCK\_SIZE](sd__spec_8h.md#a072705601a34c697515f74acb0474c99abd97c835c80320637579c692d6f57878) = 16,

[ 47](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a99c20a704cce28fee37b9b0f14b2ff15) [SD\_READ\_SINGLE\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a99c20a704cce28fee37b9b0f14b2ff15) = 17,

[ 48](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa58b1d9f75b639dc1b28163988bc8aa3) [SD\_READ\_MULTIPLE\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa58b1d9f75b639dc1b28163988bc8aa3) = 18,

[ 49](sd__spec_8h.md#a072705601a34c697515f74acb0474c99af48292861388f111b0afad64f0352664) [SD\_SEND\_TUNING\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99af48292861388f111b0afad64f0352664) = 19,

[ 50](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a35b942802a4238882440f2e470f2555f) [MMC\_SEND\_BUS\_TEST](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a35b942802a4238882440f2e470f2555f) = 19,

[ 51](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a0378338c2747ba8947d8ffcb18f77d51) [MMC\_SEND\_TUNING\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a0378338c2747ba8947d8ffcb18f77d51) = 21,

[ 52](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7e34ea8ce2a215c2a76f4184b84a06f2) [SD\_SET\_BLOCK\_COUNT](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7e34ea8ce2a215c2a76f4184b84a06f2) = 23,

[ 53](sd__spec_8h.md#a072705601a34c697515f74acb0474c99adca664fbf5ff0b4d174ca21641e01004) [SD\_WRITE\_SINGLE\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99adca664fbf5ff0b4d174ca21641e01004) = 24,

[ 54](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a9cd6e9c88c3989531a71015147496895) [SD\_WRITE\_MULTIPLE\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a9cd6e9c88c3989531a71015147496895) = 25,

[ 55](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa7c628982851eba38074d02e9e335b57) [SD\_ERASE\_BLOCK\_START](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa7c628982851eba38074d02e9e335b57) = 32,

[ 56](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a753b0fc3e44a4376998e5887ed2c5901) [SD\_ERASE\_BLOCK\_END](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a753b0fc3e44a4376998e5887ed2c5901) = 33,

[ 57](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a4aa36f7d8ceaa3cdab300915453b64b5) [SD\_ERASE\_BLOCK\_OPERATION](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a4aa36f7d8ceaa3cdab300915453b64b5) = 38,

[ 58](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7ef64e231154de2e461005af29918b86) [SDIO\_RW\_DIRECT](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7ef64e231154de2e461005af29918b86) = 52,

[ 59](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7ccf37711e67b58534689997ac1375df) [SDIO\_RW\_EXTENDED](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7ccf37711e67b58534689997ac1375df) = 53,

[ 60](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aef4ee3246cd66cd7d48f1dabf3fcd7ef) [SD\_APP\_CMD](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aef4ee3246cd66cd7d48f1dabf3fcd7ef) = 55,

[ 61](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa3183436decfa0e42ac0461629258ba3) [SD\_SPI\_READ\_OCR](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa3183436decfa0e42ac0461629258ba3) = 58, /\* SPI mode only \*/

[ 62](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ab590e9d9b3213f31a2399ef379d066aa) [SD\_SPI\_CRC\_ON\_OFF](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ab590e9d9b3213f31a2399ef379d066aa) = 59, /\* SPI mode only \*/

63};

64

[ 71](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbc)enum [sd\_app\_cmd](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbc) {

[ 72](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcaca51b75cde3505fd672391b9d7a7997a) [SD\_APP\_SET\_BUS\_WIDTH](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcaca51b75cde3505fd672391b9d7a7997a) = 6,

[ 73](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca36f78cdbd8fcc962c2247d7fc1f33f9b) [SD\_APP\_SEND\_STATUS](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca36f78cdbd8fcc962c2247d7fc1f33f9b) = 13,

[ 74](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca03fc81eeed7047ad914ce6590511dfa3) [SD\_APP\_SEND\_NUM\_WRITTEN\_BLK](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca03fc81eeed7047ad914ce6590511dfa3) = 22,

[ 75](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcacf330302cc8ef7f55d76c2cace40649e) [SD\_APP\_SET\_WRITE\_BLK\_ERASE\_CNT](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcacf330302cc8ef7f55d76c2cace40649e) = 23,

[ 76](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca2a4278c079a227145f63f5f2d860146a) [SD\_APP\_SEND\_OP\_COND](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca2a4278c079a227145f63f5f2d860146a) = 41,

[ 77](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcaa4a44bb015be3cbcf180f34a39ba8e05) [SD\_APP\_CLEAR\_CARD\_DETECT](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcaa4a44bb015be3cbcf180f34a39ba8e05) = 42,

[ 78](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca305b2fb720b5191c762b77b886152ca8) [SD\_APP\_SEND\_SCR](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca305b2fb720b5191c762b77b886152ca8) = 51,

79};

80

[ 86](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155a)enum [sd\_r1\_status](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155a) {

87 /\* Bits 0-2 reserved \*/

[ 88](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5) [SD\_R1\_AUTH\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

89 /\* Bit 4 reserved for SDIO \*/

[ 90](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa72c5d7592912c25f0440fa38664dfc13) [SD\_R1\_APP\_CMD](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa72c5d7592912c25f0440fa38664dfc13) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 91](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab852db2cfe8d7581e1ad7a1c2aee5406) [SD\_R1\_FX\_EVENT](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab852db2cfe8d7581e1ad7a1c2aee5406) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

92 /\* Bit 7 reserved \*/

[ 93](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac99e88e470b5ecb04885b0289a96a2c8) [SD\_R1\_RDY\_DATA](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac99e88e470b5ecb04885b0289a96a2c8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 94](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65) [SD\_R1\_CUR\_STATE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65) = (0xFU << 9),

[ 95](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa3c9f8c1239694b9bda4aca0d7f40a929) [SD\_R1\_ERASE\_RESET](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa3c9f8c1239694b9bda4aca0d7f40a929) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

[ 96](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa4cf46d638fd781b73edd03b61dd5d1a2) [SD\_R1\_ECC\_DISABLED](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa4cf46d638fd781b73edd03b61dd5d1a2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

[ 97](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837) [SD\_R1\_ERASE\_SKIP](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

[ 98](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2) [SD\_R1\_CSD\_OVERWRITE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

99 /\* Bits 17-18 reserved \*/

[ 100](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2) [SD\_R1\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

[ 101](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d) [SD\_R1\_CC\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

[ 102](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870) [SD\_R1\_ECC\_FAIL](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21),

[ 103](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc) [SD\_R1\_ILLEGAL\_CMD](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22),

[ 104](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2) [SD\_R1\_CRC\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23),

[ 105](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65) [SD\_R1\_UNLOCK\_FAIL](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24),

[ 106](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa02d458f5c51dfb7554e17bad1acb591a) [SD\_R1\_CARD\_LOCKED](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa02d458f5c51dfb7554e17bad1acb591a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25),

[ 107](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab) [SD\_R1\_WP\_VIOLATION](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26),

[ 108](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21) [SD\_R1\_ERASE\_PARAM](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27),

[ 109](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae) [SD\_R1\_ERASE\_SEQ\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28),

[ 110](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254) [SD\_R1\_BLOCK\_LEN\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29),

[ 111](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4) [SD\_R1\_ADDR\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30),

[ 112](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf) [SD\_R1\_OUT\_OF\_RANGE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31),

[ 113](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab6413ec799d46c7341e48f0b5146f400) [SD\_R1\_ERR\_FLAGS](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab6413ec799d46c7341e48f0b5146f400) = ([SD\_R1\_AUTH\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5) |

114 [SD\_R1\_ERASE\_SKIP](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837) |

115 [SD\_R1\_CSD\_OVERWRITE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2) |

116 [SD\_R1\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2) |

117 [SD\_R1\_CC\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d) |

118 [SD\_R1\_ECC\_FAIL](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870) |

119 [SD\_R1\_ILLEGAL\_CMD](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc) |

120 [SD\_R1\_CRC\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2) |

121 [SD\_R1\_UNLOCK\_FAIL](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65) |

122 [SD\_R1\_WP\_VIOLATION](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab) |

123 [SD\_R1\_ERASE\_PARAM](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21) |

124 [SD\_R1\_ERASE\_SEQ\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae) |

125 [SD\_R1\_BLOCK\_LEN\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254) |

126 [SD\_R1\_ADDR\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4) |

127 [SD\_R1\_OUT\_OF\_RANGE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf)),

[ 128](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab8635ae93d3d927f662e88c9e55305eb) [SD\_R1ERR\_NONE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab8635ae93d3d927f662e88c9e55305eb) = 0,

129};

130

[ 131](sd__spec_8h.md#ac104a7c39f61829092eaffd98663045b)#define SD\_R1\_CURRENT\_STATE(x) (((x) & SD\_R1\_CUR\_STATE) >> 9U)

132

[ 138](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065)enum [sd\_r1\_current\_state](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065) {

[ 139](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a081f03ba34d8cd168ab5d4172d3c8d6a) [SDMMC\_R1\_IDLE](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a081f03ba34d8cd168ab5d4172d3c8d6a) = 0U,

[ 140](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a135f072a7d9ee5967a49f7a164816854) [SDMMC\_R1\_READY](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a135f072a7d9ee5967a49f7a164816854) = 1U,

[ 141](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a1ddcc2a60e6f83538151fc93ad434ddf) [SDMMC\_R1\_IDENTIFY](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a1ddcc2a60e6f83538151fc93ad434ddf) = 2U,

[ 142](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065ac906ebc564bfc63a7f4ce0350db6667b) [SDMMC\_R1\_STANDBY](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065ac906ebc564bfc63a7f4ce0350db6667b) = 3U,

[ 143](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a59ead4a70e76c9b2d6c817f4e2847998) [SDMMC\_R1\_TRANSFER](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a59ead4a70e76c9b2d6c817f4e2847998) = 4U,

[ 144](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a5d6d02968e18dd84af3583d282179e64) [SDMMC\_R1\_SEND\_DATA](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a5d6d02968e18dd84af3583d282179e64) = 5U,

[ 145](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a3feb7a1594dc32703d2fbf6e43e77c0c) [SDMMC\_R1\_RECIVE\_DATA](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a3feb7a1594dc32703d2fbf6e43e77c0c) = 6U,

[ 146](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065acccc283c3dc4a36992e76ea0b6f4d68b) [SDMMC\_R1\_PROGRAM](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065acccc283c3dc4a36992e76ea0b6f4d68b) = 7U,

[ 147](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065abebe32c9b1e107c729f4e6ecf501ee1e) [SDMMC\_R1\_DISCONNECT](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065abebe32c9b1e107c729f4e6ecf501ee1e) = 8U,

148};

149

[ 155](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3)enum [sd\_spi\_r1\_error\_flag](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3) {

[ 156](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3aae5e5c58313c1216448474da513ca2b6) [SD\_SPI\_R1PARAMETER\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3aae5e5c58313c1216448474da513ca2b6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 157](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3ae50961a0eb0f59776a156facf51e4620) [SD\_SPI\_R1ADDRESS\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3ae50961a0eb0f59776a156facf51e4620) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 158](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3aa07d3031debe394b369d93fde728d406) [SD\_SPI\_R1ERASE\_SEQ\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3aa07d3031debe394b369d93fde728d406) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 159](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3ae4785671c3a4dca332c10c9bc0a72fba) [SD\_SPI\_R1CMD\_CRC\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3ae4785671c3a4dca332c10c9bc0a72fba) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 160](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a0a59356a4db1abd3f72a8c9778b04e66) [SD\_SPI\_R1ILLEGAL\_CMD\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a0a59356a4db1abd3f72a8c9778b04e66) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 161](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a4eb47f187f4aee8228b09a37d4669a4f) [SD\_SPI\_R1ERASE\_RESET](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a4eb47f187f4aee8228b09a37d4669a4f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 162](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a9c77ef6b4da1f8ac56ebe8be03504b69) [SD\_SPI\_R1IDLE\_STATE](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a9c77ef6b4da1f8ac56ebe8be03504b69) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

163};

164

[ 171](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878f)enum [sd\_spi\_r2\_status](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878f) {

[ 172](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa8f693e2ff4acfb3d652106fc25f8758f) [SDHC\_SPI\_R2\_CARD\_LOCKED](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa8f693e2ff4acfb3d652106fc25f8758f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 173](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa3f8fde9c17c04f4500f5a86cf4d9e7df) [SDHC\_SPI\_R2\_UNLOCK\_FAIL](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa3f8fde9c17c04f4500f5a86cf4d9e7df) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 174](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878faf74a4730cc3507a35179fe09da721a19) [SDHC\_SPI\_R2\_ERR](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878faf74a4730cc3507a35179fe09da721a19) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 175](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fad33e5499a36259f5b881ce524a1f4159) [SDHC\_SPI\_R2\_CC\_ERR](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fad33e5499a36259f5b881ce524a1f4159) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

[ 176](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fac853010c32e85d30f9f5936851ac4ddb) [SDHC\_SPI\_R2\_ECC\_FAIL](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fac853010c32e85d30f9f5936851ac4ddb) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

[ 177](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa92bcd0ee78ddba8dc551c7917a37a792) [SDHC\_SPI\_R2\_WP\_VIOLATION](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa92bcd0ee78ddba8dc551c7917a37a792) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

[ 178](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa47bb6389f20ceb840612266fedac0f7a) [SDHC\_SPI\_R2\_ERASE\_PARAM](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa47bb6389f20ceb840612266fedac0f7a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

[ 179](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878faedbd66fd01bb87a4f55291c299589db7) [SDHC\_SPI\_R2\_OUT\_OF\_RANGE](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878faedbd66fd01bb87a4f55291c299589db7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

180};

181

182/\* Byte length of SD SPI mode command \*/

[ 183](sd__spec_8h.md#aa841b78f5937f8499918cc977a36e90f)#define SD\_SPI\_CMD\_SIZE 6

[ 184](sd__spec_8h.md#a85e46f60c0ae5f21a4386009bbfaf0a3)#define SD\_SPI\_CMD\_BODY\_SIZE (SD\_SPI\_CMD\_SIZE - 1)

185/\* Byte length of CRC16 appended to data blocks in SPI mode \*/

[ 186](sd__spec_8h.md#aed67a9adbb001dad73eec4054ef6cbc1)#define SD\_SPI\_CRC16\_SIZE 2

187

188/\* SPI Command flags \*/

[ 189](sd__spec_8h.md#a7da6535d451c1062f8d0c92f5688e178)#define SD\_SPI\_START 0x80

[ 190](sd__spec_8h.md#a2283409131ac9ede90773b256094b74c)#define SD\_SPI\_TX 0x40

[ 191](sd__spec_8h.md#a2d1dee775c3849a92dac9d179bd50a6c)#define SD\_SPI\_CMD 0x3F

192

193/\* SPI Data block tokens \*/

[ 194](sd__spec_8h.md#a7cd4fbf7d5ce2e8eba8c795a675486bb)#define SD\_SPI\_TOKEN\_SINGLE 0xFE

[ 195](sd__spec_8h.md#ae34cf95537f2c0963ade18f1ba5d6e20)#define SD\_SPI\_TOKEN\_MULTI\_WRITE 0xFC

[ 196](sd__spec_8h.md#a9d4f357ff29ee3b5483505404ba3c956)#define SD\_SPI\_TOKEN\_STOP\_TRAN 0xFD

197

198/\* SPI Data block responses \*/

[ 199](sd__spec_8h.md#a5d36df2e0d1bd88aadc3673cdf12aea7)#define SD\_SPI\_RESPONSE\_ACCEPTED 0x05

[ 200](sd__spec_8h.md#a3a206f684b2c878f59a394b06abd9814)#define SD\_SPI\_RESPONSE\_CRC\_ERR 0x0B

[ 201](sd__spec_8h.md#a498f76218e054dff0e524a83ac90ccd1)#define SD\_SPI\_RESPONSE\_WRITE\_ERR 0x0C

202

203/\* Masks used in SD interface condition query (CMD8) \*/

[ 204](sd__spec_8h.md#a0d10fc7ae53b5bfb6d7f448844820799)#define SD\_IF\_COND\_VHS\_MASK (0x0F << 8)

[ 205](sd__spec_8h.md#a38157545a4a10dd4757ad1eb80487c60)#define SD\_IF\_COND\_VHS\_3V3 BIT(8)

[ 206](sd__spec_8h.md#aed6aacadb061a42993c59d8d69a2f2ab)#define SD\_IF\_COND\_CHECK 0xAA

207

[ 214](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6)enum [sd\_rsp\_type](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6) {

215 /\* Native response types (lower 4 bits) \*/

[ 216](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6ad74407536823c1ea3afdf41d4b858b1c) [SD\_RSP\_TYPE\_NONE](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6ad74407536823c1ea3afdf41d4b858b1c) = 0U,

[ 217](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a92718e4bd4bccaa2fe4a8780228004d7) [SD\_RSP\_TYPE\_R1](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a92718e4bd4bccaa2fe4a8780228004d7) = 1U,

[ 218](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6ae64496ba1520651f8bac35af2531eaf8) [SD\_RSP\_TYPE\_R1b](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6ae64496ba1520651f8bac35af2531eaf8) = 2U,

[ 219](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a96e26220a32f9b6e9e0bdd8c94d48eaf) [SD\_RSP\_TYPE\_R2](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a96e26220a32f9b6e9e0bdd8c94d48eaf) = 3U,

[ 220](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6af779f08bfb2fd73a717ea3789ccad509) [SD\_RSP\_TYPE\_R3](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6af779f08bfb2fd73a717ea3789ccad509) = 4U,

[ 221](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a34b03331e8f7a9ea6b67da6b68c7e0ed) [SD\_RSP\_TYPE\_R4](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a34b03331e8f7a9ea6b67da6b68c7e0ed) = 5U,

[ 222](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a91e216f8a1753b4719ee91819a926dde) [SD\_RSP\_TYPE\_R5](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a91e216f8a1753b4719ee91819a926dde) = 6U,

[ 223](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a5dcd82e4fe5a34646a617a5031fdc638) [SD\_RSP\_TYPE\_R5b](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a5dcd82e4fe5a34646a617a5031fdc638) = 7U,

[ 224](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a3532733bc007df5009801bd6f09e45c9) [SD\_RSP\_TYPE\_R6](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a3532733bc007df5009801bd6f09e45c9) = 8U,

[ 225](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6aa5657942fb906d58ef2b7bed05137f23) [SD\_RSP\_TYPE\_R7](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6aa5657942fb906d58ef2b7bed05137f23) = 9U,

226 /\* SPI response types (bits [7:4]) \*/

[ 227](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a32b2c65c90d0d5b8df5e4a82e9b95a6d) [SD\_SPI\_RSP\_TYPE\_R1](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a32b2c65c90d0d5b8df5e4a82e9b95a6d) = (1U << 4),

[ 228](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a22413680849a7645c7e8c585b5184203) [SD\_SPI\_RSP\_TYPE\_R1b](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a22413680849a7645c7e8c585b5184203) = (2U << 4),

[ 229](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a855f8e4399cf3ce0c05c6089f3439ec2) [SD\_SPI\_RSP\_TYPE\_R2](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a855f8e4399cf3ce0c05c6089f3439ec2) = (3U << 4),

[ 230](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a7c44711a51e8175ebcaf4be24e2daec3) [SD\_SPI\_RSP\_TYPE\_R3](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a7c44711a51e8175ebcaf4be24e2daec3) = (4U << 4),

[ 231](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a4c35ca3a8db652008204cf0cfc8e2339) [SD\_SPI\_RSP\_TYPE\_R4](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a4c35ca3a8db652008204cf0cfc8e2339) = (5U << 4),

[ 232](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a0d82c7d93c187de5c40c0ff83fe8a478) [SD\_SPI\_RSP\_TYPE\_R5](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a0d82c7d93c187de5c40c0ff83fe8a478) = (6U << 4),

[ 233](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a78472618e8523bf73ca65aee6b0a8318) [SD\_SPI\_RSP\_TYPE\_R7](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a78472618e8523bf73ca65aee6b0a8318) = (7U << 4),

234};

235

[ 241](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749a)enum [sd\_support\_flag](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749a) {

[ 242](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa104798e5266441d5a2f356f50b01cb35) [SD\_HIGH\_CAPACITY\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa104798e5266441d5a2f356f50b01cb35) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 243](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa2511277c6c4ebe38bc7179312292710b) [SD\_4BITS\_WIDTH](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa2511277c6c4ebe38bc7179312292710b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 244](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aad9777c04b150a28916f894f54417286c) [SD\_SDHC\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aad9777c04b150a28916f894f54417286c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 245](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa0558ef06a64c10456d220e66a5bc0f8b) [SD\_SDXC\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa0558ef06a64c10456d220e66a5bc0f8b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 246](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aab78269976cbb673b4e00d6059ec38f80) [SD\_1800MV\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aab78269976cbb673b4e00d6059ec38f80) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 247](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa5458d4988d7076d854bd695307771858) [SD\_3000MV\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa5458d4988d7076d854bd695307771858) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 248](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aac1f502da56d7d50b70898329da1ad21a) [SD\_CMD23\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aac1f502da56d7d50b70898329da1ad21a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 249](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa02b4afca69adad8d7f220b8e4a76db45) [SD\_SPEED\_CLASS\_CONTROL\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa02b4afca69adad8d7f220b8e4a76db45) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 250](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa923c57b4134ad360ed3f6abbabfa87f1) [SD\_MEM\_PRESENT\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa923c57b4134ad360ed3f6abbabfa87f1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

251};

252

253

[ 260](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61)enum [sd\_ocr\_flag](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61) {

[ 262](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a5f680f7a518294d7a706b73bbecbdb73) [SD\_OCR\_PWR\_BUSY\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a5f680f7a518294d7a706b73bbecbdb73) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31),

[ 264](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a) [SD\_OCR\_HOST\_CAP\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30),

[ 266](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a4cfc3b5856c525eda63b3a8b5fce5ae2) [SD\_OCR\_CARD\_CAP\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a4cfc3b5856c525eda63b3a8b5fce5ae2) = [SD\_OCR\_HOST\_CAP\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a),

[ 268](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d) [SD\_OCR\_SWITCH\_18\_REQ\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24),

[ 270](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a541be7abf94851538a38f69c2ecb6b5f) [SD\_OCR\_SWITCH\_18\_ACCEPT\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a541be7abf94851538a38f69c2ecb6b5f) = [SD\_OCR\_SWITCH\_18\_REQ\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d),

[ 272](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61acd85dd4f874ed9088e6d7a2260d7bc50) [SD\_OCR\_VDD27\_28FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61acd85dd4f874ed9088e6d7a2260d7bc50) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

[ 274](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a76356316ead27df98dac310eed775707) [SD\_OCR\_VDD28\_29FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a76356316ead27df98dac310eed775707) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

[ 276](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a624191bea93e1a350073fe2e5d5adaf1) [SD\_OCR\_VDD29\_30FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a624191bea93e1a350073fe2e5d5adaf1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

[ 278](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a98c205ed0f08df1a2f9e2801f02bbe7f) [SD\_OCR\_VDD30\_31FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a98c205ed0f08df1a2f9e2801f02bbe7f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

[ 280](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a8ae4a104d50c0bdcae4722de0d5ee605) [SD\_OCR\_VDD31\_32FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a8ae4a104d50c0bdcae4722de0d5ee605) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

[ 282](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a0c8a74f1b50f574b64184bf1cdc1458f) [SD\_OCR\_VDD32\_33FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a0c8a74f1b50f574b64184bf1cdc1458f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

[ 284](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61aca49de7bd24df65fd6448a7e570b04a8) [SD\_OCR\_VDD33\_34FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61aca49de7bd24df65fd6448a7e570b04a8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21),

[ 286](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae5e13b78bf3fdece36190e48136927bf) [SD\_OCR\_VDD34\_35FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae5e13b78bf3fdece36190e48136927bf) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22),

[ 288](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a83a9f603da11b75f200d3bb62528cda4) [SD\_OCR\_VDD35\_36FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a83a9f603da11b75f200d3bb62528cda4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23),

289};

290

[ 297](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aa)enum [mmc\_ocr\_flag](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aa) {

[ 298](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa01aef2529fc39dc455c0fb8f2e9cc434) [MMC\_OCR\_VDD170\_195FLAG](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa01aef2529fc39dc455c0fb8f2e9cc434) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 299](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa984a5e7f75a4418ca29141f5c6031d1e) [MMC\_OCR\_VDD20\_26FLAG](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa984a5e7f75a4418ca29141f5c6031d1e) = 0x7F << 8,

[ 300](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa239f02ae958dc3e25032825bb4c067e7) [MMC\_OCR\_VDD27\_36FLAG](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa239f02ae958dc3e25032825bb4c067e7) = 0x1FF << 15,

[ 301](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa669934175190e5416a0d04c3c94acb4b) [MMC\_OCR\_SECTOR\_MODE](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa669934175190e5416a0d04c3c94acb4b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30),

[ 302](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa7127f5d946ea6bb4ec19b96033aafc4b) [MMC\_OCR\_PWR\_BUSY\_FLAG](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa7127f5d946ea6bb4ec19b96033aafc4b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31)

303};

304

[ 305](sd__spec_8h.md#a23690672048afbc75ce2c2f4d9a74144)#define SDIO\_OCR\_IO\_NUMBER\_SHIFT 28

306/\* Lower 24 bits hold SDIO I/O OCR \*/

[ 307](sd__spec_8h.md#a0d98fd7cd6f67b28981c6e01f8805a01)#define SDIO\_IO\_OCR\_MASK 0xFFFFFF

308

[ 315](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6)enum [sdio\_ocr\_flag](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6) {

[ 316](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6adb3e45e84da812297359d6054baa69ba) [SDIO\_OCR\_IO\_READY\_FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6adb3e45e84da812297359d6054baa69ba) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31),

[ 317](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a17007c3d37f047e6db56491a4230e8a8) [SDIO\_OCR\_IO\_NUMBER](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a17007c3d37f047e6db56491a4230e8a8) = (7U << 28U),

[ 318](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ae923fdf459570657220ec225cbed7336) [SDIO\_OCR\_MEM\_PRESENT\_FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ae923fdf459570657220ec225cbed7336) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27),

[ 319](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a3f6ebe270ba873bab3407ee7d655b53d) [SDIO\_OCR\_180\_VOL\_FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a3f6ebe270ba873bab3407ee7d655b53d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24),

[ 320](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6aa7a656a21495fbf64666b2b80236e4e4) [SDIO\_OCR\_VDD20\_21FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6aa7a656a21495fbf64666b2b80236e4e4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 321](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ad75d7d47a3d5fcc39a68c08546e9793b) [SDIO\_OCR\_VDD21\_22FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ad75d7d47a3d5fcc39a68c08546e9793b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 322](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a560f91eb371bfea5cf6c5c036cc9c096) [SDIO\_OCR\_VDD22\_23FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a560f91eb371bfea5cf6c5c036cc9c096) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 323](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a89c4025349ece0021cd627101f0efdd1) [SDIO\_OCR\_VDD23\_24FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a89c4025349ece0021cd627101f0efdd1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

[ 324](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a6323aa0a8cbfb59f8209a37c8135079c) [SDIO\_OCR\_VDD24\_25FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a6323aa0a8cbfb59f8209a37c8135079c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

[ 325](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ac0aa0897e1bbf45b0f5f4de73d733477) [SDIO\_OCR\_VDD25\_26FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ac0aa0897e1bbf45b0f5f4de73d733477) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

[ 326](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a4d32525a631342d78f73b6296e148666) [SDIO\_OCR\_VDD26\_27FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a4d32525a631342d78f73b6296e148666) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

[ 327](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a1f043936c614ac39b75f3835dc498b94) [SDIO\_OCR\_VDD27\_28FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a1f043936c614ac39b75f3835dc498b94) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

[ 328](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a1071312f18c64077e6964e421ef00ead) [SDIO\_OCR\_VDD28\_29FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a1071312f18c64077e6964e421ef00ead) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

[ 329](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a246619651470476238452550068db8a0) [SDIO\_OCR\_VDD29\_30FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a246619651470476238452550068db8a0) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

[ 330](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a4cb1cc23687e7a1854d8af0c76876a20) [SDIO\_OCR\_VDD30\_31FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a4cb1cc23687e7a1854d8af0c76876a20) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

[ 331](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a018af73c25e22c6e5313e5e3cff57e92) [SDIO\_OCR\_VDD31\_32FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a018af73c25e22c6e5313e5e3cff57e92) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

[ 332](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ac5613e6858d2c9217165ab4cbb240012) [SDIO\_OCR\_VDD32\_33FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ac5613e6858d2c9217165ab4cbb240012) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

[ 333](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a6673f837fa5a98b573886c5e6429c644) [SDIO\_OCR\_VDD33\_34FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a6673f837fa5a98b573886c5e6429c644) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21),

[ 334](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a3d791855e6df402d5bfd92ce216a9a4b) [SDIO\_OCR\_VDD34\_35FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a3d791855e6df402d5bfd92ce216a9a4b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22),

[ 335](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6af0baaa7f71d144c7e5edade4b2445813) [SDIO\_OCR\_VDD35\_36FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6af0baaa7f71d144c7e5edade4b2445813) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23),

336};

337

338

[ 346](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3)enum [sd\_switch\_arg](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3) {

[ 348](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3ae126f56fd639cbd686321a088d1e05e6) [SD\_SWITCH\_CHECK](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3ae126f56fd639cbd686321a088d1e05e6) = 0U,

[ 350](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3a72c39e3140ddd3990c3cbe7c6c867bb1) [SD\_SWITCH\_SET](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3a72c39e3140ddd3990c3cbe7c6c867bb1) = 1U,

351};

352

[ 359](sd__spec_8h.md#a97f4810585247f5fed41110413e49853)enum [sd\_group\_num](sd__spec_8h.md#a97f4810585247f5fed41110413e49853) {

[ 361](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a488b1aac4a0658c8b04b94b7556a2c5b) [SD\_GRP\_TIMING\_MODE](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a488b1aac4a0658c8b04b94b7556a2c5b) = 0U,

[ 363](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a8c620d198b195d913ad3ff913434d764) [SD\_GRP\_CMD\_SYS\_MODE](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a8c620d198b195d913ad3ff913434d764) = 1U,

[ 365](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a5e617dd9de3620481b89e517bd2c3a4b) [SD\_GRP\_DRIVER\_STRENGTH\_MODE](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a5e617dd9de3620481b89e517bd2c3a4b) = 2U,

[ 367](sd__spec_8h.md#a97f4810585247f5fed41110413e49853aa38ef885442708891b4ddc4a83c6ff66) [SD\_GRP\_CURRENT\_LIMIT\_MODE](sd__spec_8h.md#a97f4810585247f5fed41110413e49853aa38ef885442708891b4ddc4a83c6ff66) = 3U,

368};

369

370/\* Maximum data rate possible for SD high speed cards \*/

[ 371](sd__spec_8h.md#a2093143614e52f69e173289391d7e91c)enum [hs\_max\_data\_rate](sd__spec_8h.md#a2093143614e52f69e173289391d7e91c) {

[ 372](sd__spec_8h.md#a2093143614e52f69e173289391d7e91cac3e8d67442f59c35b57d19d81b5d0d66) [HS\_UNSUPPORTED](sd__spec_8h.md#a2093143614e52f69e173289391d7e91cac3e8d67442f59c35b57d19d81b5d0d66) = 0,

[ 373](sd__spec_8h.md#a2093143614e52f69e173289391d7e91ca10f805e3f66366474428718cb4569da0) [HS\_MAX\_DTR](sd__spec_8h.md#a2093143614e52f69e173289391d7e91ca10f805e3f66366474428718cb4569da0) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(50),

374};

375

376/\* Maximum data rate possible for SD uhs cards \*/

[ 377](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9a)enum [uhs\_max\_data\_rate](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9a) {

[ 378](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aaad6eabbee29e4ff07bdf93a9162aea6b) [UHS\_UNSUPPORTED](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aaad6eabbee29e4ff07bdf93a9162aea6b) = 0,

[ 379](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aad61b9d180a8de3c01be2e892c45504fb) [UHS\_SDR12\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aad61b9d180a8de3c01be2e892c45504fb) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(25),

[ 380](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa5c5c100c048986ecfed728690d05ac55) [UHS\_SDR25\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa5c5c100c048986ecfed728690d05ac55) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(50),

[ 381](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa72e9ad81edf54b7139a758d47fe54dd5) [UHS\_SDR50\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa72e9ad81edf54b7139a758d47fe54dd5) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(100),

[ 382](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa106c43d63c3b3c02d3835ccf542f3190) [UHS\_SDR104\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa106c43d63c3b3c02d3835ccf542f3190) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(208),

[ 383](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aaff651e04c107beb23e0bd76d03029b26) [UHS\_DDR50\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aaff651e04c107beb23e0bd76d03029b26) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(50),

384};

385

[ 392](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36)enum [sd\_bus\_speed](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36) {

[ 393](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a30f38c9e54bed572ca315fdeb9122103) [UHS\_SDR12\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a30f38c9e54bed572ca315fdeb9122103) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 394](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a90413fe7dfd8568eeac79709ece7a549) [DEFAULT\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a90413fe7dfd8568eeac79709ece7a549) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 395](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a5593992de690adb1022b7926d1508ab3) [HIGH\_SPEED\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a5593992de690adb1022b7926d1508ab3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 396](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36ae07a7ef1ffce64bab52c5f6612a96716) [UHS\_SDR25\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36ae07a7ef1ffce64bab52c5f6612a96716) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 397](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a360c72912e023e5b21363f3701deaa50) [UHS\_SDR50\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a360c72912e023e5b21363f3701deaa50) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 398](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36aef2ef100dab4187c8600ea721e8726dd) [UHS\_SDR104\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36aef2ef100dab4187c8600ea721e8726dd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 399](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a022acb9d379c5ecf9935150ec6f51ffc) [UHS\_DDR50\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a022acb9d379c5ecf9935150ec6f51ffc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

400};

401

[ 408](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930)enum [sd\_timing\_mode](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930) {

[ 410](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aa858c50e3f53d635857084ab5801a204) [SD\_TIMING\_DEFAULT](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aa858c50e3f53d635857084ab5801a204) = 0U,

[ 412](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aea7ebe2a07e1ed7727262d522815355b) [SD\_TIMING\_SDR12](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aea7ebe2a07e1ed7727262d522815355b) = 0U,

[ 414](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a7b6cef084cb3b83a91c05964951b05a6) [SD\_TIMING\_HIGH\_SPEED](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a7b6cef084cb3b83a91c05964951b05a6) = 1U,

[ 416](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a433d8a39f77a612dd8104ca49c71a76f) [SD\_TIMING\_SDR25](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a433d8a39f77a612dd8104ca49c71a76f) = 1U,

[ 418](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a787fb937df1275cb3d169e1dade2fb37) [SD\_TIMING\_SDR50](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a787fb937df1275cb3d169e1dade2fb37) = 2U,

[ 420](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aad980a4d433ffcf189a2e77b5d765861) [SD\_TIMING\_SDR104](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aad980a4d433ffcf189a2e77b5d765861) = 3U,

[ 422](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a88f373b6ac9335667eb8adab49a04e10) [SD\_TIMING\_DDR50](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a88f373b6ac9335667eb8adab49a04e10) = 4U,

423};

424

[ 430](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539)enum [sdhc\_clock\_speed](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539) {

[ 431](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a16c56ed964cc6bbb5cc6f0cb857d4f10) [SDMMC\_CLOCK\_400KHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a16c56ed964cc6bbb5cc6f0cb857d4f10) = [KHZ](group__sys-util.md#gaee55275295c076c6d23c994777623253)(400),

[ 432](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539ad5e9d57ee155e1b919f6cc213b05424f) [SD\_CLOCK\_25MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539ad5e9d57ee155e1b919f6cc213b05424f) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(25),

[ 433](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a39e410f7f5c51753bf415f727551b9fb) [SD\_CLOCK\_50MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a39e410f7f5c51753bf415f727551b9fb) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(50),

[ 434](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a66ef44acd4ff3fafc2d49120df4b3c10) [SD\_CLOCK\_100MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a66ef44acd4ff3fafc2d49120df4b3c10) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(100),

[ 435](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a9570bb04b0181b4fbdc96cace060d187) [SD\_CLOCK\_208MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a9570bb04b0181b4fbdc96cace060d187) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(208),

[ 436](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539ae9369c1cd7595ab83289fc356e9cc1b6) [MMC\_CLOCK\_26MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539ae9369c1cd7595ab83289fc356e9cc1b6) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(26),

[ 437](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a5c37aeeb3c68d7b3dbe8b9001a00507c) [MMC\_CLOCK\_52MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a5c37aeeb3c68d7b3dbe8b9001a00507c) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(52),

[ 438](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a66ecc8c1a73181d70e23424cf718728d) [MMC\_CLOCK\_DDR52](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a66ecc8c1a73181d70e23424cf718728d) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(52),

[ 439](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a14dec2b314ed13974dbba31f33a5eab9) [MMC\_CLOCK\_HS200](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a14dec2b314ed13974dbba31f33a5eab9) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(200),

[ 440](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a788a77f1e7a468c14ef57319ef8938f3) [MMC\_CLOCK\_HS400](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a788a77f1e7a468c14ef57319ef8938f3) = [MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)(200), /\* Same clock freq as HS200, just DDR \*/

441};

442

[ 448](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972)enum [sd\_current\_setting](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972) {

[ 449](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972a134ed84475be6f55a0f3d3ae9201cbe9) [SD\_SET\_CURRENT\_200MA](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972a134ed84475be6f55a0f3d3ae9201cbe9) = 0,

[ 450](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972ad548c59ebbb5045e437157cb9186de19) [SD\_SET\_CURRENT\_400MA](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972ad548c59ebbb5045e437157cb9186de19) = 1,

[ 451](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972a83f1d375e4c5aa645759cc4e4462f8e0) [SD\_SET\_CURRENT\_600MA](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972a83f1d375e4c5aa645759cc4e4462f8e0) = 2,

[ 452](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972af44faa0f33705ecbd37b5f3544105e34) [SD\_SET\_CURRENT\_800MA](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972af44faa0f33705ecbd37b5f3544105e34) = 3,

453};

454

[ 460](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537)enum [sd\_current\_limit](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537) {

[ 462](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537a18b21e5e76bea0263f475ecc228c0301) [SD\_MAX\_CURRENT\_200MA](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537a18b21e5e76bea0263f475ecc228c0301) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 464](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537ae0605a0d9fc89e094a40b03e96c02339) [SD\_MAX\_CURRENT\_400MA](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537ae0605a0d9fc89e094a40b03e96c02339) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 466](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537af82a5f23e51bf3ac3b7bec137269f540) [SD\_MAX\_CURRENT\_600MA](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537af82a5f23e51bf3ac3b7bec137269f540) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 468](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537a2e3c01bc8d16641d7b500ce1244dbb03) [SD\_MAX\_CURRENT\_800MA](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537a2e3c01bc8d16641d7b500ce1244dbb03) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

469};

470

[ 476](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b)enum [sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b) {

[ 477](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba32ad0894344bc4980f9206022ed0f877) [SD\_DRIVER\_TYPE\_B](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba32ad0894344bc4980f9206022ed0f877) = 0x1,

[ 478](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba9eec5ff6f7d4c7512212cb48719dcabf) [SD\_DRIVER\_TYPE\_A](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba9eec5ff6f7d4c7512212cb48719dcabf) = 0x2,

[ 479](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba0cd41f5198ce06ce5925b3f52d48b0a2) [SD\_DRIVER\_TYPE\_C](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba0cd41f5198ce06ce5925b3f52d48b0a2) = 0x4,

[ 480](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba435b458d33f1568cb76b77a3ea2e1eb8) [SD\_DRIVER\_TYPE\_D](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba435b458d33f1568cb76b77a3ea2e1eb8) = 0x8,

481};

482

[ 488](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2)enum [sd\_driver\_strength](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2) {

[ 490](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2a1b1e411f733ad6c1dc41896744441a48) [SD\_DRV\_STRENGTH\_TYPEB](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2a1b1e411f733ad6c1dc41896744441a48) = 0U,

[ 492](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2ad870ea9b9fc07a4af81bce3c82330441) [SD\_DRV\_STRENGTH\_TYPEA](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2ad870ea9b9fc07a4af81bce3c82330441) = 1U,

[ 494](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2aa3e190aa6edb9f6eb7e29b78fc6f1a8a) [SD\_DRV\_STRENGTH\_TYPEC](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2aa3e190aa6edb9f6eb7e29b78fc6f1a8a) = 2U,

[ 496](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2ad5753bf6fae3f43ef8ce7cb7eb169b61) [SD\_DRV\_STRENGTH\_TYPED](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2ad5753bf6fae3f43ef8ce7cb7eb169b61) = 3U,

497};

498

[ 505](structsd__switch__caps.md)struct [sd\_switch\_caps](structsd__switch__caps.md) {

[ 506](structsd__switch__caps.md#a7465b3fe6bd1f317eeb3283a25da7278) enum [hs\_max\_data\_rate](sd__spec_8h.md#a2093143614e52f69e173289391d7e91c) [hs\_max\_dtr](structsd__switch__caps.md#a7465b3fe6bd1f317eeb3283a25da7278);

[ 507](structsd__switch__caps.md#ab09d80f61bc79857ee39604959c8a578) enum [uhs\_max\_data\_rate](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9a) [uhs\_max\_dtr](structsd__switch__caps.md#ab09d80f61bc79857ee39604959c8a578);

[ 508](structsd__switch__caps.md#a29024de744d65fb3d8fe51c4d4424aee) enum [sd\_bus\_speed](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36) [bus\_speed](structsd__switch__caps.md#a29024de744d65fb3d8fe51c4d4424aee);

[ 509](structsd__switch__caps.md#a7262e4be5e3f59d047e569e1c24f04b3) enum [sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b) [sd\_drv\_type](structsd__switch__caps.md#a7262e4be5e3f59d047e569e1c24f04b3);

[ 510](structsd__switch__caps.md#a4b531af598bea14c90b8973daf1422dc) enum [sd\_current\_limit](structsd__switch__caps.md#a4b531af598bea14c90b8973daf1422dc) [sd\_current\_limit](structsd__switch__caps.md#a4b531af598bea14c90b8973daf1422dc);

511};

512

513

[ 514](sd__spec_8h.md#a947520a05fc99c25449fab98d0d02b1e)#define SD\_PRODUCT\_NAME\_BYTES 5

515

[ 521](structsd__cid.md)struct [sd\_cid](structsd__cid.md) {

[ 523](structsd__cid.md#a7d97bc0f58c766abd2501d923e163d40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [manufacturer](structsd__cid.md#a7d97bc0f58c766abd2501d923e163d40);

[ 525](structsd__cid.md#a11ec5fa23ae13ee084c093b27c1d381a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [application](structsd__cid.md#a11ec5fa23ae13ee084c093b27c1d381a);

[ 527](structsd__cid.md#a46f36abc3c2b1f3e9aa34c199d2bfcf3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [name](structsd__cid.md#a46f36abc3c2b1f3e9aa34c199d2bfcf3)[[SD\_PRODUCT\_NAME\_BYTES](sd__spec_8h.md#a947520a05fc99c25449fab98d0d02b1e)];

[ 529](structsd__cid.md#aba79f6a5bdf963772ac3c77ac209faf2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structsd__cid.md#aba79f6a5bdf963772ac3c77ac209faf2);

[ 531](structsd__cid.md#ace04f0f28cb7e058e69fbbc643f66052) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ser\_num](structsd__cid.md#ace04f0f28cb7e058e69fbbc643f66052);

[ 533](structsd__cid.md#a50fbbc6844a1fde29a25a803ed9d0df7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [date](structsd__cid.md#a50fbbc6844a1fde29a25a803ed9d0df7);

534};

535

[ 541](structsd__csd.md)struct [sd\_csd](structsd__csd.md) {

[ 543](structsd__csd.md#a37b15b70967c9317183b3e5e7837b228) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [csd\_structure](structsd__csd.md#a37b15b70967c9317183b3e5e7837b228);

[ 545](structsd__csd.md#a583c715045b5934ad94ab9cf61b25b06) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [read\_time1](structsd__csd.md#a583c715045b5934ad94ab9cf61b25b06);

[ 547](structsd__csd.md#a96bc4672222dece77d29ffc9287c59ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [read\_time2](structsd__csd.md#a96bc4672222dece77d29ffc9287c59ac);

[ 549](structsd__csd.md#ae39272173a5253d0d11ef04a2e129db6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [xfer\_rate](structsd__csd.md#ae39272173a5253d0d11ef04a2e129db6);

[ 551](structsd__csd.md#a8bfd2c42066d85058d01076fcaa7a32d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cmd\_class](structsd__csd.md#a8bfd2c42066d85058d01076fcaa7a32d);

[ 553](structsd__csd.md#a06f6aef4f4745a78bcf769df5415daa6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [read\_blk\_len](structsd__csd.md#a06f6aef4f4745a78bcf769df5415daa6);

[ 555](structsd__csd.md#ae10b32787aeedd4789d657eb1ef492eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structsd__csd.md#ae10b32787aeedd4789d657eb1ef492eb);

[ 557](structsd__csd.md#ad35b07abba80e9929c5eed40e37d25b3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [device\_size](structsd__csd.md#ad35b07abba80e9929c5eed40e37d25b3);

[ 559](structsd__csd.md#aa868cfc1db75eb2913d21bffeaf29fd9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [read\_current\_min](structsd__csd.md#aa868cfc1db75eb2913d21bffeaf29fd9);

[ 561](structsd__csd.md#ad2f31731d7ec0b101d911fe20b5d94db) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [read\_current\_max](structsd__csd.md#ad2f31731d7ec0b101d911fe20b5d94db);

[ 563](structsd__csd.md#a0d1efea12c467eacd0d0f98a0bb0ac91) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [write\_current\_min](structsd__csd.md#a0d1efea12c467eacd0d0f98a0bb0ac91);

[ 565](structsd__csd.md#a53b364ce0db06b9217259afeb625da44) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [write\_current\_max](structsd__csd.md#a53b364ce0db06b9217259afeb625da44);

[ 567](structsd__csd.md#a9d5a952bc6c2a6967e9a88cd93f19e89) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dev\_size\_mul](structsd__csd.md#a9d5a952bc6c2a6967e9a88cd93f19e89);

[ 569](structsd__csd.md#ab8d5ae38b19f7ea83b0856ad093c65cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [erase\_size](structsd__csd.md#ab8d5ae38b19f7ea83b0856ad093c65cb);

[ 571](structsd__csd.md#a029a893cdcd3765864c70476eb6dd64e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [write\_prtect\_size](structsd__csd.md#a029a893cdcd3765864c70476eb6dd64e);

[ 573](structsd__csd.md#a9c362eff38daf7d00776416ed064de24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [write\_speed\_factor](structsd__csd.md#a9c362eff38daf7d00776416ed064de24);

[ 575](structsd__csd.md#adff7d405662589ec44f4d0a6b3548760) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [write\_blk\_len](structsd__csd.md#adff7d405662589ec44f4d0a6b3548760);

[ 577](structsd__csd.md#af93239157610a6eeea420c29432d5412) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [file\_fmt](structsd__csd.md#af93239157610a6eeea420c29432d5412);

578};

579

[ 585](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8)enum [mmc\_csd\_freq](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8) {

[ 586](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a221dc45c7b73f6f96a63acbeb3e5e121) [MMC\_MAXFREQ\_100KHZ](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a221dc45c7b73f6f96a63acbeb3e5e121) = 0U << 0U,

[ 587](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a32c9f5017cd49c9ca4b352269de6eeff) [MMC\_MAXFREQ\_1MHZ](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a32c9f5017cd49c9ca4b352269de6eeff) = 1U << 0U,

[ 588](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8af63af4938d5aad64bac19fac42aedd10) [MMC\_MAXFREQ\_10MHZ](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8af63af4938d5aad64bac19fac42aedd10) = 2U << 0U,

[ 589](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a13c703d344a1e03c1aa5881a77980085) [MMC\_MAXFREQ\_100MHZ](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a13c703d344a1e03c1aa5881a77980085) = 3U << 0U,

[ 590](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a74d01430b854f42ea84dba9d3ce45b16) [MMC\_MAXFREQ\_MULT\_10](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a74d01430b854f42ea84dba9d3ce45b16) = 1U << 3U,

[ 591](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a4a3b8dc88c6349fb5f49ed3062a39a17) [MMC\_MAXFREQ\_MULT\_12](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a4a3b8dc88c6349fb5f49ed3062a39a17) = 2U << 3U,

[ 592](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a2c639715b63769e9a431a93e636f007e) [MMC\_MAXFREQ\_MULT\_13](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a2c639715b63769e9a431a93e636f007e) = 3U << 3U,

[ 593](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ac988a54239b7d9e182f1b2f480567e66) [MMC\_MAXFREQ\_MULT\_15](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ac988a54239b7d9e182f1b2f480567e66) = 4U << 3U,

[ 594](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ac8848c5cdf177737744da3283f7140d5) [MMC\_MAXFREQ\_MULT\_20](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ac8848c5cdf177737744da3283f7140d5) = 5U << 3U,

[ 595](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ab1ff3da74a0dea49ffe7ac1d945ec4e6) [MMC\_MAXFREQ\_MULT\_26](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ab1ff3da74a0dea49ffe7ac1d945ec4e6) = 6U << 3U,

[ 596](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a69e1d369d668d63071410078a31099a0) [MMC\_MAXFREQ\_MULT\_30](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a69e1d369d668d63071410078a31099a0) = 7U << 3U,

[ 597](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a63c0eee223946b1ae2b187bb585dfde4) [MMC\_MAXFREQ\_MULT\_35](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a63c0eee223946b1ae2b187bb585dfde4) = 8U << 3U,

[ 598](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a572d53afafb39341e0cdb80d2d041d2c) [MMC\_MAXFREQ\_MULT\_40](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a572d53afafb39341e0cdb80d2d041d2c) = 9U << 3U,

[ 599](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a5bd0506d7efbecdc42eb8fae1427dc37) [MMC\_MAXFREQ\_MULT\_45](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a5bd0506d7efbecdc42eb8fae1427dc37) = 0xAU << 3U,

[ 600](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a988f18b9f418744721b0fc91f2432449) [MMC\_MAXFREQ\_MULT\_52](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a988f18b9f418744721b0fc91f2432449) = 0xBU << 3U,

[ 601](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8abecfcd6d212185c74b57941c3fa58233) [MMC\_MAXFREQ\_MULT\_55](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8abecfcd6d212185c74b57941c3fa58233) = 0xCU << 3U,

[ 602](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8adf578325509923b46e3ff4fbd74889ad) [MMC\_MAXFREQ\_MULT\_60](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8adf578325509923b46e3ff4fbd74889ad) = 0xDU << 3U,

[ 603](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8aee24df1d628479fe2d920839a0bf5012) [MMC\_MAXFREQ\_MULT\_70](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8aee24df1d628479fe2d920839a0bf5012) = 0xEU << 3U,

[ 604](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a24ea8c9db5531b5404bb667da26ac5d0) [MMC\_MAXFREQ\_MULT\_80](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a24ea8c9db5531b5404bb667da26ac5d0) = 0xFU << 3u

605};

606

[ 612](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345)enum [mmc\_timing\_mode](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345) {

[ 613](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345ae51a5474387816c03970aa0f8058b002) [MMC\_LEGACY\_TIMING](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345ae51a5474387816c03970aa0f8058b002) = 0U,

[ 614](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a17160707005c580fbd52dbd6b99699dd) [MMC\_HS\_TIMING](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a17160707005c580fbd52dbd6b99699dd) = 1U,

[ 615](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a39200c50c7e22c096db3ce1dd3fe78d5) [MMC\_HS200\_TIMING](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a39200c50c7e22c096db3ce1dd3fe78d5) = 2U,

[ 616](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a4ea17060afbcd026387172c1af57bb43) [MMC\_HS400\_TIMING](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a4ea17060afbcd026387172c1af57bb43) = 3U

617};

618

[ 624](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09d)enum [mmc\_driver\_strengths](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09d) {

[ 625](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dabd4f3ffac3f52efe797ce3ee3c31a03f) [mmc\_driv\_type0](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dabd4f3ffac3f52efe797ce3ee3c31a03f) = 0U,

[ 626](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09da2cedd0b40bf81afb35792150b2d4964a) [mmc\_driv\_type1](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09da2cedd0b40bf81afb35792150b2d4964a) = 1U,

[ 627](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dafed77d2aed13d59fa6645cb06fc21c43) [mmc\_driv\_type2](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dafed77d2aed13d59fa6645cb06fc21c43) = 2U,

[ 628](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dacf4d28d56a6c4925944ffc99072d46e9) [mmc\_driv\_type3](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dacf4d28d56a6c4925944ffc99072d46e9) = 3U,

[ 629](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09daf5448a25c8b5a8411f059469112ef2be) [mmc\_driv\_type4](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09daf5448a25c8b5a8411f059469112ef2be) = 4U

630};

631

632

[ 638](structmmc__device__type.md)struct [mmc\_device\_type](structmmc__device__type.md) {

[ 639](structmmc__device__type.md#ab19f29678c18ba8740758ca136fd7744) bool [MMC\_HS400\_DDR\_1200MV](structmmc__device__type.md#ab19f29678c18ba8740758ca136fd7744);

[ 640](structmmc__device__type.md#a24bee6ea4bd6d209b53b05fb9e040b38) bool [MMC\_HS400\_DDR\_1800MV](structmmc__device__type.md#a24bee6ea4bd6d209b53b05fb9e040b38);

[ 641](structmmc__device__type.md#aaa7bb99717ecde9e6cf265a6c5bb33f0) bool [MMC\_HS200\_SDR\_1200MV](structmmc__device__type.md#aaa7bb99717ecde9e6cf265a6c5bb33f0);

[ 642](structmmc__device__type.md#a7027fdec8b21be17a2ba97b2b19a13da) bool [MMC\_HS200\_SDR\_1800MV](structmmc__device__type.md#a7027fdec8b21be17a2ba97b2b19a13da);

[ 643](structmmc__device__type.md#a65bc5ecdb11da48c08a06d4c5c386590) bool [MMC\_HS\_DDR\_1200MV](structmmc__device__type.md#a65bc5ecdb11da48c08a06d4c5c386590);

[ 644](structmmc__device__type.md#a5d338770aca6d893e094f57211b0339e) bool [MMC\_HS\_DDR\_1800MV](structmmc__device__type.md#a5d338770aca6d893e094f57211b0339e);

[ 645](structmmc__device__type.md#a3f4bbe853ef59313a84acb5737cafdf4) bool [MMC\_HS\_52\_DV](structmmc__device__type.md#a3f4bbe853ef59313a84acb5737cafdf4);

[ 646](structmmc__device__type.md#a12bb36ef4914b9182f08c4310c85d70d) bool [MMC\_HS\_26\_DV](structmmc__device__type.md#a12bb36ef4914b9182f08c4310c85d70d);

647};

648

[ 654](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81)enum [mmc\_ext\_csd\_rev](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81) {

[ 655](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81ad49da8223b68d35a4d95d6b48bb8a3f7) [MMC\_5\_1](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81ad49da8223b68d35a4d95d6b48bb8a3f7) = 8U,

[ 656](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a87a4c0efb7e10cccce939af5f60343ad) [MMC\_5\_0](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a87a4c0efb7e10cccce939af5f60343ad) = 7U,

[ 657](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81aa0d4721b24d0cd71d6a8fbfc666a6e7c) [MMC\_4\_5](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81aa0d4721b24d0cd71d6a8fbfc666a6e7c) = 6U,

[ 658](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a43b7acda3747eb2233c2f2a433ff71c7) [MMC\_4\_4](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a43b7acda3747eb2233c2f2a433ff71c7) = 5U,

[ 659](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a0f4fc7047a7c813b9ada618ed05e09a4) [MMC\_4\_3](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a0f4fc7047a7c813b9ada618ed05e09a4) = 3U,

[ 660](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a9a960567b8ecbd6feff7e6337fc98567) [MMC\_4\_2](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a9a960567b8ecbd6feff7e6337fc98567) = 2U,

[ 661](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81ab84ae4edfcca8ccae2a0df0643d04ca2) [MMC\_4\_1](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81ab84ae4edfcca8ccae2a0df0643d04ca2) = 1U,

[ 662](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81aba4f3f30eaa7d3368743f78f3c355269) [MMC\_4\_0](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81aba4f3f30eaa7d3368743f78f3c355269) = 0U

663};

664

[ 671](structmmc__ext__csd.md)struct [mmc\_ext\_csd](structmmc__ext__csd.md) {

[ 673](structmmc__ext__csd.md#a44aa7d6d1282a00a1875e92fb5b3c4b8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sec\_count](structmmc__ext__csd.md#a44aa7d6d1282a00a1875e92fb5b3c4b8);

[ 675](structmmc__ext__csd.md#a63545477058cce0c5727637bcbb06a47) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bus\_width](structmmc__ext__csd.md#a63545477058cce0c5727637bcbb06a47);

[ 677](structmmc__ext__csd.md#a25fe8f962635be3d40b449203e7d34a2) enum [mmc\_timing\_mode](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345) [hs\_timing](structmmc__ext__csd.md#a25fe8f962635be3d40b449203e7d34a2);

[ 679](structmmc__ext__csd.md#a4c26010052a69e060742e0a05b6ad98b) struct [mmc\_device\_type](structmmc__device__type.md) [device\_type](structmmc__ext__csd.md#a4c26010052a69e060742e0a05b6ad98b);

[ 681](structmmc__ext__csd.md#a3ee512cb3c0e3698d940c04eed3aa665) enum [mmc\_ext\_csd\_rev](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81) [rev](structmmc__ext__csd.md#a3ee512cb3c0e3698d940c04eed3aa665);

[ 683](structmmc__ext__csd.md#a286b2783ac15dbec6fa3953f0cd69af4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [power\_class](structmmc__ext__csd.md#a286b2783ac15dbec6fa3953f0cd69af4);

[ 685](structmmc__ext__csd.md#a29a7f7502e6e6d93e76392b8ac45356f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mmc\_driver\_strengths](structmmc__ext__csd.md#a29a7f7502e6e6d93e76392b8ac45356f);

[ 687](structmmc__ext__csd.md#acab002b3a28a3dc9bf58187e9e19a9fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pwr\_class\_200MHZ\_VCCQ195](structmmc__ext__csd.md#acab002b3a28a3dc9bf58187e9e19a9fe);

[ 689](structmmc__ext__csd.md#a3a38f805cac18f3429f57edc7cbf2134) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pwr\_class\_HS400](structmmc__ext__csd.md#a3a38f805cac18f3429f57edc7cbf2134);

[ 691](structmmc__ext__csd.md#a3aafc3e2b5b59cb79535411178a35efe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cache\_size](structmmc__ext__csd.md#a3aafc3e2b5b59cb79535411178a35efe);

692};

693

[ 699](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437)enum [sd\_csd\_flag](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437) {

[ 701](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437ac353a0c3c1ac62920efdc42879a81cff) [SD\_CSD\_READ\_BLK\_PARTIAL\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437ac353a0c3c1ac62920efdc42879a81cff) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 703](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a16d3fd179853f1f15b980d2b82b572be) [SD\_CSD\_WRITE\_BLK\_MISALIGN\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a16d3fd179853f1f15b980d2b82b572be) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 705](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aca7d98319db6a23b30625828807e2143) [SD\_CSD\_READ\_BLK\_MISALIGN\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aca7d98319db6a23b30625828807e2143) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 707](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a1258364107909d0c4f8e9b7dba59300c) [SD\_CSD\_DSR\_IMPLEMENTED\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a1258364107909d0c4f8e9b7dba59300c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 709](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a0d907c1a9e69435433c5bf19bfacbd73) [SD\_CSD\_ERASE\_BLK\_EN\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a0d907c1a9e69435433c5bf19bfacbd73) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 711](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437af85839612e4fcc94eb2bd0986bd1740c) [SD\_CSD\_WRITE\_PROTECT\_GRP\_EN\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437af85839612e4fcc94eb2bd0986bd1740c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 713](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aa8b8f850196e47799cb9b2cd06650520) [SD\_CSD\_WRITE\_BLK\_PARTIAL\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aa8b8f850196e47799cb9b2cd06650520) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 715](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a2e75506280c1b4d5866f4dd8f2518be8) [SD\_CSD\_FILE\_FMT\_GRP\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a2e75506280c1b4d5866f4dd8f2518be8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 717](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a988758fe0720e6fc33564076e3bc51bf) [SD\_CSD\_COPY\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a988758fe0720e6fc33564076e3bc51bf) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 719](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a7496edd5c7ec694d2d175bf751de1458) [SD\_CSD\_PERMANENT\_WRITE\_PROTECT\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a7496edd5c7ec694d2d175bf751de1458) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 721](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aa0c70fee97e29875394efc2a4c2fa274) [SD\_CSD\_TMP\_WRITE\_PROTECT\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aa0c70fee97e29875394efc2a4c2fa274) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

722};

723

[ 729](structsd__scr.md)struct [sd\_scr](structsd__scr.md) {

[ 731](structsd__scr.md#a3fc37c731dfb5c5596b6389152479c07) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [scr\_structure](structsd__scr.md#a3fc37c731dfb5c5596b6389152479c07);

[ 733](structsd__scr.md#ae6201af1083efa828cced000874bf197) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sd\_spec](structsd__scr.md#ae6201af1083efa828cced000874bf197);

[ 735](structsd__scr.md#abda65da85e20979a1fc71f2aea1f947b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structsd__scr.md#abda65da85e20979a1fc71f2aea1f947b);

[ 737](structsd__scr.md#a9f8254b5fe6911156bae727e29262f5a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sd\_sec](structsd__scr.md#a9f8254b5fe6911156bae727e29262f5a);

[ 739](structsd__scr.md#a40d30ccc4daf2c32f2ac162b402f3887) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sd\_width](structsd__scr.md#a40d30ccc4daf2c32f2ac162b402f3887);

[ 741](structsd__scr.md#a15f60bc2115b943ce938f3a96dd8e547) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sd\_ext\_sec](structsd__scr.md#a15f60bc2115b943ce938f3a96dd8e547);

[ 743](structsd__scr.md#a9016ca73a668499289c52355ebb83cb1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd\_support](structsd__scr.md#a9016ca73a668499289c52355ebb83cb1);

[ 745](structsd__scr.md#aba20efcf752335f1a86d0a86607d92d0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rsvd](structsd__scr.md#aba20efcf752335f1a86d0a86607d92d0);

746};

747

[ 753](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553)enum [sd\_scr\_flag](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553) {

[ 755](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553a759c63670d0dd41590fdb940a48ac4dd) [SD\_SCR\_DATA\_STATUS\_AFTER\_ERASE](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553a759c63670d0dd41590fdb940a48ac4dd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 757](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553a59fb3a34a7dba6ed1c86bca21cf97871) [SD\_SCR\_SPEC3](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553a59fb3a34a7dba6ed1c86bca21cf97871) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

758};

759

[ 765](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301a)enum [sd\_spec\_version](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301a) {

[ 767](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa39605b86ccfad6196721ddfbb84b33d6) [SD\_SPEC\_VER1\_0](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa39605b86ccfad6196721ddfbb84b33d6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 769](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aac09ddfacee85353e243d6a8cfe7eeba8) [SD\_SPEC\_VER1\_1](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aac09ddfacee85353e243d6a8cfe7eeba8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 771](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa3525ee751a482ae1cd816e2674ac3160) [SD\_SPEC\_VER2\_0](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa3525ee751a482ae1cd816e2674ac3160) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 773](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa9e3d0d084a7d8ad1b9d08e6b699084e6) [SD\_SPEC\_VER3\_0](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa9e3d0d084a7d8ad1b9d08e6b699084e6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

774};

775

776

[ 777](sd__spec_8h.md#a523a28eeec3d0a71f0d7ca49ab397960)#define SDMMC\_DEFAULT\_BLOCK\_SIZE 512

[ 778](sd__spec_8h.md#ade9a798f584d431c86e172266394f41e)#define MMC\_EXT\_CSD\_BYTES 512

[ 784](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6)enum [sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6) {

[ 785](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ad7a10f97094ddb96f26ab44fc34de12a) [SDIO\_FUNC\_NUM\_0](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ad7a10f97094ddb96f26ab44fc34de12a) = 0,

[ 786](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a900536b934da03f8e8590de3e3d56296) [SDIO\_FUNC\_NUM\_1](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a900536b934da03f8e8590de3e3d56296) = 1,

[ 787](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ac2cc5967daee0a3e9ef61c9c486b3a6c) [SDIO\_FUNC\_NUM\_2](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ac2cc5967daee0a3e9ef61c9c486b3a6c) = 2,

[ 788](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6adef5748e2622dab22da33504bbafa149) [SDIO\_FUNC\_NUM\_3](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6adef5748e2622dab22da33504bbafa149) = 3,

[ 789](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a9b69d64108c6564bc313e4fb2b53f61c) [SDIO\_FUNC\_NUM\_4](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a9b69d64108c6564bc313e4fb2b53f61c) = 4,

[ 790](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ac62397290371f5fb3fdf8d4b52fb3575) [SDIO\_FUNC\_NUM\_5](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ac62397290371f5fb3fdf8d4b52fb3575) = 5,

[ 791](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a2a9baef178307d6e6006ea88b4da383c) [SDIO\_FUNC\_NUM\_6](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a2a9baef178307d6e6006ea88b4da383c) = 6,

[ 792](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a617d1991d70033df3b39eef7ccb98b48) [SDIO\_FUNC\_NUM\_7](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a617d1991d70033df3b39eef7ccb98b48) = 7,

[ 793](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a075731d15b2f4b7c7448d6d4ee059880) [SDIO\_FUNC\_MEMORY](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a075731d15b2f4b7c7448d6d4ee059880) = 8,

794};

795

[ 801](sd__spec_8h.md#a250ae2ce54e941895a720b565632350e)enum [sdio\_io\_dir](sd__spec_8h.md#a250ae2ce54e941895a720b565632350e) {

[ 802](sd__spec_8h.md#a250ae2ce54e941895a720b565632350eac1212149d096232e75d1d090abb4974c) [SDIO\_IO\_READ](sd__spec_8h.md#a250ae2ce54e941895a720b565632350eac1212149d096232e75d1d090abb4974c) = 0,

[ 803](sd__spec_8h.md#a250ae2ce54e941895a720b565632350eabd26fc6f76267231c78eae8be9ebb885) [SDIO\_IO\_WRITE](sd__spec_8h.md#a250ae2ce54e941895a720b565632350eabd26fc6f76267231c78eae8be9ebb885) = 1,

804};

805

[ 806](sd__spec_8h.md#a960ade30c404ebb08769c5870ac21b37)#define SDIO\_CMD\_ARG\_RW\_SHIFT 31

[ 807](sd__spec_8h.md#acd6e41030a8d16419cc22adf9f0a5509)#define SDIO\_CMD\_ARG\_FUNC\_NUM\_SHIFT 28

[ 808](sd__spec_8h.md#afadddcc143b78325505a40544c04e3b0)#define SDIO\_DIRECT\_CMD\_ARG\_RAW\_SHIFT 27

[ 809](sd__spec_8h.md#aa74dbe588f1f5ca248cf0f5a2e8e8c81)#define SDIO\_CMD\_ARG\_REG\_ADDR\_SHIFT 9

[ 810](sd__spec_8h.md#a338e9606baa6937e0887e7a9b9372c23)#define SDIO\_CMD\_ARG\_REG\_ADDR\_MASK 0x1FFFF

[ 811](sd__spec_8h.md#a5ab9e1e0c96e7166b1ff7a208f90001d)#define SDIO\_DIRECT\_CMD\_DATA\_MASK 0xFF

812

[ 813](sd__spec_8h.md#ac6c49ad6118debe7a9e64f412e597f22)#define SDIO\_EXTEND\_CMD\_ARG\_BLK\_SHIFT 27

[ 814](sd__spec_8h.md#a73ca83a4884f13fa5de8500f69252bef)#define SDIO\_EXTEND\_CMD\_ARG\_OP\_CODE\_SHIFT 26

815

[ 821](sd__spec_8h.md#ae211fa0bfa6809273b5f7267c95ce681)#define SDIO\_CCCR\_CCCR 0x00

[ 822](sd__spec_8h.md#accf473b0fcdc9e1e03329f91e588de1a)#define SDIO\_CCCR\_CCCR\_REV\_MASK 0x0F

[ 823](sd__spec_8h.md#af5db599ebd0748528e8369653a5e3929)#define SDIO\_CCCR\_CCCR\_REV\_SHIFT 0x0

[ 824](sd__spec_8h.md#ab240215a68f23ec69e901c0666b0dfe0)#define SDIO\_CCCR\_CCCR\_REV\_1\_00 0x0

[ 825](sd__spec_8h.md#aace4672360d77085bec93b52e3ac05d9)#define SDIO\_CCCR\_CCCR\_REV\_1\_10 0x1

[ 826](sd__spec_8h.md#a566200e9322e8e4c9b3edd21a2ced93c)#define SDIO\_CCCR\_CCCR\_REV\_2\_00 0x2

[ 827](sd__spec_8h.md#aa90600f74ff69315e38ed1c10a3cde7c)#define SDIO\_CCCR\_CCCR\_REV\_3\_00 0x3

828

[ 829](sd__spec_8h.md#aafc2b0c434dff4a0903e4910181f9e81)#define SDIO\_CCCR\_SD 0x01

[ 830](sd__spec_8h.md#aa425236b097f44a9721e7aedd203ff90)#define SDIO\_CCCR\_SD\_SPEC\_MASK 0x0F

[ 831](sd__spec_8h.md#a223defa20d223655d215065b222a6767)#define SDIO\_CCCR\_SD\_SPEC\_SHIFT 0x0

832

[ 833](sd__spec_8h.md#a0b2103011690e1d3f1daef4e45a11986)#define SDIO\_CCCR\_IO\_EN 0x02

834

[ 835](sd__spec_8h.md#a6cfa2671e574650e6f35a65828cd459c)#define SDIO\_CCCR\_IO\_RD 0x03

836

[ 837](sd__spec_8h.md#a15caca2936186b54c330b4a9050c9795)#define SDIO\_CCCR\_INT\_EN 0x04

838

[ 839](sd__spec_8h.md#a81b7523a76a1826a14c2cc1c242a49a9)#define SDIO\_CCCR\_INT\_P 0x05

840

[ 841](sd__spec_8h.md#a7e061818bc8f923d5342c38721a1a501)#define SDIO\_CCCR\_ABORT 0x06

842

[ 843](sd__spec_8h.md#a283f2b2f2c28b3c8208f3d6aca3ca3d2)#define SDIO\_CCCR\_BUS\_IF 0x07

[ 844](sd__spec_8h.md#a6c04dc28d7f39fda7cd0181421a13ea0)#define SDIO\_CCCR\_BUS\_IF\_WIDTH\_MASK 0x3

[ 845](sd__spec_8h.md#aec58e3fcda2f792266fbd8ab1b75f98c)#define SDIO\_CCCR\_BUS\_IF\_WIDTH\_1\_BIT 0x00

[ 846](sd__spec_8h.md#aeb23fa771a16f69fcb9d97b156f25ade)#define SDIO\_CCCR\_BUS\_IF\_WIDTH\_4\_BIT 0x02

[ 847](sd__spec_8h.md#ade7a14837ee90c8ce24959926d81eaee)#define SDIO\_CCCR\_BUS\_IF\_WIDTH\_8\_BIT 0x03

848

[ 849](sd__spec_8h.md#a0b878d7e794d3edd127c3f08633efbbc)#define SDIO\_CCCR\_CAPS 0x08

[ 850](sd__spec_8h.md#affb9533b340f5424c1f42445c6f1002f)#define SDIO\_CCCR\_CAPS\_SDC BIT(0)

[ 851](sd__spec_8h.md#aaaf8d335a8d025b998feeb93c0899a99)#define SDIO\_CCCR\_CAPS\_SMB BIT(1)

[ 852](sd__spec_8h.md#a8011927f7b565304ec31a7e61d403d6e)#define SDIO\_CCCR\_CAPS\_SRW BIT(2)

[ 853](sd__spec_8h.md#a7550fe8aab011fc87baeb575463e27d9)#define SDIO\_CCCR\_CAPS\_SBS BIT(3)

[ 854](sd__spec_8h.md#a74082cfafdd9e8bfa37e92624ff75e80)#define SDIO\_CCCR\_CAPS\_S4MI BIT(4)

[ 855](sd__spec_8h.md#aa8281a65d0865fba8b85d91d00b90091)#define SDIO\_CCCR\_CAPS\_E4MI BIT(5)

[ 856](sd__spec_8h.md#aee93278e3c0ec4cbf0e3065d6a58f516)#define SDIO\_CCCR\_CAPS\_LSC BIT(6)

[ 857](sd__spec_8h.md#a7ba2dcf801f81ab53b418e59441000ae)#define SDIO\_CCCR\_CAPS\_BLS BIT(7)

858

[ 859](sd__spec_8h.md#a8f97c16c091bd19b545bbe452581dfff)#define SDIO\_CCCR\_CIS 0x09

860

[ 861](sd__spec_8h.md#a05edbcb4a98831cbeac509f26e881de8)#define SDIO\_CCCR\_SPEED 0x13

[ 862](sd__spec_8h.md#a964759dc76bd2a9f9f9dce5c21dc2cb4)#define SDIO\_CCCR\_SPEED\_SHS BIT(0)

[ 863](sd__spec_8h.md#a1a1817554f886a999484e2663432cd8b)#define SDIO\_CCCR\_SPEED\_MASK 0xE

[ 864](sd__spec_8h.md#a38d57134d99e2dfc5760fcf7312b6cd5)#define SDIO\_CCCR\_SPEED\_SHIFT 0x1

[ 865](sd__spec_8h.md#a9ee7aec8589aceb8555917971ab9afd3)#define SDIO\_CCCR\_SPEED\_SDR12 0x0

[ 866](sd__spec_8h.md#acb3bdd73bace425a94a357a2f0bff4ef)#define SDIO\_CCCR\_SPEED\_HS 0x1

[ 867](sd__spec_8h.md#afabf4bb10bed3295d1d051c113e61545)#define SDIO\_CCCR\_SPEED\_SDR25 0x1

[ 868](sd__spec_8h.md#a81bc96279a19618c9212674757abd141)#define SDIO\_CCCR\_SPEED\_SDR50 0x2

[ 869](sd__spec_8h.md#a0d51f98d56303dd55177245785748158)#define SDIO\_CCCR\_SPEED\_SDR104 0x3

[ 870](sd__spec_8h.md#ad3dc3009d2d78a6306c3247ab85ef48d)#define SDIO\_CCCR\_SPEED\_DDR50 0x4

871

[ 872](sd__spec_8h.md#afb72ff0aa5b90446db296af16bf9bb02)#define SDIO\_CCCR\_UHS 0x14

[ 873](sd__spec_8h.md#a9965d399115bca8574a9beaeac9b9f31)#define SDIO\_CCCR\_UHS\_SDR50 BIT(0)

[ 874](sd__spec_8h.md#aca4fee68fdf3480ec8cf7de7b46a8d4e)#define SDIO\_CCCR\_UHS\_SDR104 BIT(1)

[ 875](sd__spec_8h.md#a2678ede1ac974a9670fdcaa393682aa6)#define SDIO\_CCCR\_UHS\_DDR50 BIT(2)

876

[ 877](sd__spec_8h.md#a3a5d01e688b18109ad2f19bc5d017f26)#define SDIO\_CCCR\_DRIVE\_STRENGTH 0x15

[ 878](sd__spec_8h.md#a759a9dddc3aa08d0f11114637c5b69ff)#define SDIO\_CCCR\_DRIVE\_STRENGTH\_A BIT(0)

[ 879](sd__spec_8h.md#a8487f5a0a97e5f1f72500cf44cec89dc)#define SDIO\_CCCR\_DRIVE\_STRENGTH\_C BIT(1)

[ 880](sd__spec_8h.md#abc1ed41094d9cdd300b1b3712bb082b2)#define SDIO\_CCCR\_DRIVE\_STRENGTH\_D BIT(2)

881

[ 882](sd__spec_8h.md#a2ff95d19f7f60ce33b17b69e2672e7e5)#define SDIO\_FBR\_BASE(n) ((n) \* 0x100)

883

[ 884](sd__spec_8h.md#aea0ed052a9d94d2e2b96931752975858)#define SDIO\_FBR\_CIS 0x09

[ 885](sd__spec_8h.md#a28fb27484353eb075d501b1ad7a76112)#define SDIO\_FBR\_CSA 0x0C

[ 886](sd__spec_8h.md#af1885023615980d5cbb930538cc201a6)#define SDIO\_FBR\_BLK\_SIZE 0x10

887

888

[ 889](sd__spec_8h.md#a845866f4f88c280f8414b727e0d77edf)#define SDIO\_MAX\_IO\_NUMS 7

890

[ 891](sd__spec_8h.md#afadae8a1db38d93b909b3f2c5b0e0110)#define SDIO\_TPL\_CODE\_NULL 0x00

[ 892](sd__spec_8h.md#af1983253320b45a2a1a2aab28c09e08f)#define SDIO\_TPL\_CODE\_MANIFID 0x20

[ 893](sd__spec_8h.md#aae6f9377eccdbd5866f1a393e083c5e4)#define SDIO\_TPL\_CODE\_FUNCID 0x21

[ 894](sd__spec_8h.md#ac263bf61bcc750880bae34dde62d61e4)#define SDIO\_TPL\_CODE\_FUNCE 0x22

[ 895](sd__spec_8h.md#a21e0771f38a22f93c9f4167d8b36f608)#define SDIO\_TPL\_CODE\_END 0xFF

896

[ 903](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65)enum [sdio\_cccr\_flags](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65) {

[ 904](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65aa23a07a4fe6f6dd8292215221d97d5e2) [SDIO\_SUPPORT\_HS](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65aa23a07a4fe6f6dd8292215221d97d5e2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 905](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65acc46ce7f993b3eb81c6a2a2daad84c34) [SDIO\_SUPPORT\_SDR50](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65acc46ce7f993b3eb81c6a2a2daad84c34) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 906](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a9b12d90cd1590f68fc1031449c4560ec) [SDIO\_SUPPORT\_SDR104](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a9b12d90cd1590f68fc1031449c4560ec) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 907](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a6d2084ba4c729c2cb019582b975f652f) [SDIO\_SUPPORT\_DDR50](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a6d2084ba4c729c2cb019582b975f652f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 908](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a6cd553669599181b3677cea94687f025) [SDIO\_SUPPORT\_4BIT\_LS\_BUS](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a6cd553669599181b3677cea94687f025) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 909](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a364c7067e73960bae74ed80320adb223) [SDIO\_SUPPORT\_MULTIBLOCK](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a364c7067e73960bae74ed80320adb223) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

910};

911

[ 918](structsdio__cis.md)struct [sdio\_cis](structsdio__cis.md) {

919 /\* Manufacturer ID string tuple \*/

[ 920](structsdio__cis.md#a04c8a774c65f683185e5a32e15afb67c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [manf\_id](structsdio__cis.md#a04c8a774c65f683185e5a32e15afb67c);

[ 921](structsdio__cis.md#ad52e1df89176f728734ce0e69fb2b4c8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [manf\_code](structsdio__cis.md#ad52e1df89176f728734ce0e69fb2b4c8);

922 /\* Function identification tuple \*/

[ 923](structsdio__cis.md#ad38be5cade97ac92de62094d8e3b8549) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [func\_id](structsdio__cis.md#ad38be5cade97ac92de62094d8e3b8549);

924 /\* Function extension table \*/

[ 925](structsdio__cis.md#a1b340e20630994f91314be17dd9055ca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_blk\_size](structsdio__cis.md#a1b340e20630994f91314be17dd9055ca);

[ 926](structsdio__cis.md#a56d3ee1d6b8d0d87e0efdbda15b7076d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_speed](structsdio__cis.md#a56d3ee1d6b8d0d87e0efdbda15b7076d);

[ 927](structsdio__cis.md#a86a01890f31788ae5465b1c8dc47bcf2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rdy\_timeout](structsdio__cis.md#a86a01890f31788ae5465b1c8dc47bcf2);

928};

929

930#ifdef \_\_cplusplus

931}

932#endif

933

934#endif /\* ZEPHYR\_SUBSYS\_SD\_SPEC\_H\_ \*/

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[MHZ](group__sys-util.md#gab7b18750ddf0850461f926ae151ca7fa)

#define MHZ(x)

Number of Hz in x MHz.

**Definition** util.h:811

[KHZ](group__sys-util.md#gaee55275295c076c6d23c994777623253)

#define KHZ(x)

Number of Hz in x kHz.

**Definition** util.h:809

[sd\_opcode](sd__spec_8h.md#a072705601a34c697515f74acb0474c99)

sd\_opcode

SD specification command opcodes.

**Definition** sd\_spec.h:28

[MMC\_SEND\_TUNING\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a0378338c2747ba8947d8ffcb18f77d51)

@ MMC\_SEND\_TUNING\_BLOCK

**Definition** sd\_spec.h:51

[SD\_SEND\_IF\_COND](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a0da09225692b10e51140d4f15ba1dd0a)

@ SD\_SEND\_IF\_COND

**Definition** sd\_spec.h:37

[MMC\_SEND\_BUS\_TEST](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a35b942802a4238882440f2e470f2555f)

@ MMC\_SEND\_BUS\_TEST

**Definition** sd\_spec.h:50

[SD\_SEND\_RELATIVE\_ADDR](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a35c39a93dfcc239fcb80db70449af99e)

@ SD\_SEND\_RELATIVE\_ADDR

**Definition** sd\_spec.h:32

[SD\_SWITCH](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a400dc3acd2ae8320f130dbea80c81969)

@ SD\_SWITCH

**Definition** sd\_spec.h:35

[MMC\_CHECK\_BUS\_TEST](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a45bc2d4b117d144ef5191719f9b6c297)

@ MMC\_CHECK\_BUS\_TEST

**Definition** sd\_spec.h:44

[SD\_ERASE\_BLOCK\_OPERATION](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a4aa36f7d8ceaa3cdab300915453b64b5)

@ SD\_ERASE\_BLOCK\_OPERATION

**Definition** sd\_spec.h:57

[MMC\_SEND\_OP\_COND](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a54546b311e446754738a9b6f1e3eaea4)

@ MMC\_SEND\_OP\_COND

**Definition** sd\_spec.h:30

[MMC\_SEND\_RELATIVE\_ADDR](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a56c94068ecb32eb9ced47d4a3bf95481)

@ MMC\_SEND\_RELATIVE\_ADDR

**Definition** sd\_spec.h:33

[SD\_GO\_INACTIVE\_STATE](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a5c85e3208bb686d8ded9ae0fe7bd9d53)

@ SD\_GO\_INACTIVE\_STATE

**Definition** sd\_spec.h:45

[SD\_ERASE\_BLOCK\_END](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a753b0fc3e44a4376998e5887ed2c5901)

@ SD\_ERASE\_BLOCK\_END

**Definition** sd\_spec.h:56

[MMC\_SEND\_EXT\_CSD](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7c9bfc788861214fae86e22443e9484a)

@ MMC\_SEND\_EXT\_CSD

**Definition** sd\_spec.h:38

[SDIO\_RW\_EXTENDED](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7ccf37711e67b58534689997ac1375df)

@ SDIO\_RW\_EXTENDED

**Definition** sd\_spec.h:59

[SD\_SET\_BLOCK\_COUNT](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7e34ea8ce2a215c2a76f4184b84a06f2)

@ SD\_SET\_BLOCK\_COUNT

**Definition** sd\_spec.h:52

[SDIO\_RW\_DIRECT](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a7ef64e231154de2e461005af29918b86)

@ SDIO\_RW\_DIRECT

**Definition** sd\_spec.h:58

[SD\_SEND\_CID](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a8c3edf14ca3a6e04c1949a40cd3fb135)

@ SD\_SEND\_CID

**Definition** sd\_spec.h:40

[SD\_READ\_SINGLE\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a99c20a704cce28fee37b9b0f14b2ff15)

@ SD\_READ\_SINGLE\_BLOCK

**Definition** sd\_spec.h:47

[SD\_WRITE\_MULTIPLE\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a9cd6e9c88c3989531a71015147496895)

@ SD\_WRITE\_MULTIPLE\_BLOCK

**Definition** sd\_spec.h:54

[SD\_GO\_IDLE\_STATE](sd__spec_8h.md#a072705601a34c697515f74acb0474c99a9dcb2e5fb6a5a53c6cb02422fd1fef3c)

@ SD\_GO\_IDLE\_STATE

**Definition** sd\_spec.h:29

[SD\_SPI\_READ\_OCR](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa3183436decfa0e42ac0461629258ba3)

@ SD\_SPI\_READ\_OCR

**Definition** sd\_spec.h:61

[SD\_READ\_MULTIPLE\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa58b1d9f75b639dc1b28163988bc8aa3)

@ SD\_READ\_MULTIPLE\_BLOCK

**Definition** sd\_spec.h:48

[SD\_STOP\_TRANSMISSION](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa5f2d8c27d0b7ae780734cb4bedbf8a4)

@ SD\_STOP\_TRANSMISSION

**Definition** sd\_spec.h:42

[SD\_ERASE\_BLOCK\_START](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aa7c628982851eba38074d02e9e335b57)

@ SD\_ERASE\_BLOCK\_START

**Definition** sd\_spec.h:55

[SD\_SPI\_CRC\_ON\_OFF](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ab590e9d9b3213f31a2399ef379d066aa)

@ SD\_SPI\_CRC\_ON\_OFF

**Definition** sd\_spec.h:62

[SD\_SET\_BLOCK\_SIZE](sd__spec_8h.md#a072705601a34c697515f74acb0474c99abd97c835c80320637579c692d6f57878)

@ SD\_SET\_BLOCK\_SIZE

**Definition** sd\_spec.h:46

[SD\_VOL\_SWITCH](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ad6d6f1ccdabc2970ac2ab6c7a853b37e)

@ SD\_VOL\_SWITCH

**Definition** sd\_spec.h:41

[SD\_SEND\_STATUS](sd__spec_8h.md#a072705601a34c697515f74acb0474c99ad822462692847b4e8433157cd75eef70)

@ SD\_SEND\_STATUS

**Definition** sd\_spec.h:43

[SD\_SEND\_CSD](sd__spec_8h.md#a072705601a34c697515f74acb0474c99adc7e589c9352cddf856b2e868f93a097)

@ SD\_SEND\_CSD

**Definition** sd\_spec.h:39

[SD\_WRITE\_SINGLE\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99adca664fbf5ff0b4d174ca21641e01004)

@ SD\_WRITE\_SINGLE\_BLOCK

**Definition** sd\_spec.h:53

[SD\_APP\_CMD](sd__spec_8h.md#a072705601a34c697515f74acb0474c99aef4ee3246cd66cd7d48f1dabf3fcd7ef)

@ SD\_APP\_CMD

**Definition** sd\_spec.h:60

[SD\_SEND\_TUNING\_BLOCK](sd__spec_8h.md#a072705601a34c697515f74acb0474c99af48292861388f111b0afad64f0352664)

@ SD\_SEND\_TUNING\_BLOCK

**Definition** sd\_spec.h:49

[SDIO\_SEND\_OP\_COND](sd__spec_8h.md#a072705601a34c697515f74acb0474c99af48c850f0aa9e9f9dbce8fc8855f6a2a)

@ SDIO\_SEND\_OP\_COND

**Definition** sd\_spec.h:34

[SD\_SELECT\_CARD](sd__spec_8h.md#a072705601a34c697515f74acb0474c99afa15c17b4fb95747b444616b085b4905)

@ SD\_SELECT\_CARD

**Definition** sd\_spec.h:36

[SD\_ALL\_SEND\_CID](sd__spec_8h.md#a072705601a34c697515f74acb0474c99affcc3d18f6bda30fb3fd34916d8f61fe)

@ SD\_ALL\_SEND\_CID

**Definition** sd\_spec.h:31

[mmc\_ocr\_flag](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aa)

mmc\_ocr\_flag

MMC OCR bit flags.

**Definition** sd\_spec.h:297

[MMC\_OCR\_VDD170\_195FLAG](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa01aef2529fc39dc455c0fb8f2e9cc434)

@ MMC\_OCR\_VDD170\_195FLAG

**Definition** sd\_spec.h:298

[MMC\_OCR\_VDD27\_36FLAG](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa239f02ae958dc3e25032825bb4c067e7)

@ MMC\_OCR\_VDD27\_36FLAG

**Definition** sd\_spec.h:300

[MMC\_OCR\_SECTOR\_MODE](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa669934175190e5416a0d04c3c94acb4b)

@ MMC\_OCR\_SECTOR\_MODE

**Definition** sd\_spec.h:301

[MMC\_OCR\_PWR\_BUSY\_FLAG](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa7127f5d946ea6bb4ec19b96033aafc4b)

@ MMC\_OCR\_PWR\_BUSY\_FLAG

**Definition** sd\_spec.h:302

[MMC\_OCR\_VDD20\_26FLAG](sd__spec_8h.md#a0769bcc2f15d43383f4e5a6c845c51aaa984a5e7f75a4418ca29141f5c6031d1e)

@ MMC\_OCR\_VDD20\_26FLAG

**Definition** sd\_spec.h:299

[sd\_app\_cmd](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbc)

sd\_app\_cmd

SD application command opcodes.

**Definition** sd\_spec.h:71

[SD\_APP\_SEND\_NUM\_WRITTEN\_BLK](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca03fc81eeed7047ad914ce6590511dfa3)

@ SD\_APP\_SEND\_NUM\_WRITTEN\_BLK

**Definition** sd\_spec.h:74

[SD\_APP\_SEND\_OP\_COND](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca2a4278c079a227145f63f5f2d860146a)

@ SD\_APP\_SEND\_OP\_COND

**Definition** sd\_spec.h:76

[SD\_APP\_SEND\_SCR](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca305b2fb720b5191c762b77b886152ca8)

@ SD\_APP\_SEND\_SCR

**Definition** sd\_spec.h:78

[SD\_APP\_SEND\_STATUS](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbca36f78cdbd8fcc962c2247d7fc1f33f9b)

@ SD\_APP\_SEND\_STATUS

**Definition** sd\_spec.h:73

[SD\_APP\_CLEAR\_CARD\_DETECT](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcaa4a44bb015be3cbcf180f34a39ba8e05)

@ SD\_APP\_CLEAR\_CARD\_DETECT

**Definition** sd\_spec.h:77

[SD\_APP\_SET\_BUS\_WIDTH](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcaca51b75cde3505fd672391b9d7a7997a)

@ SD\_APP\_SET\_BUS\_WIDTH

**Definition** sd\_spec.h:72

[SD\_APP\_SET\_WRITE\_BLK\_ERASE\_CNT](sd__spec_8h.md#a1c77191f9cb8c50e8e2a03cda2984dbcacf330302cc8ef7f55d76c2cace40649e)

@ SD\_APP\_SET\_WRITE\_BLK\_ERASE\_CNT

**Definition** sd\_spec.h:75

[sd\_rsp\_type](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6)

sd\_rsp\_type

SD response types.

**Definition** sd\_spec.h:214

[SD\_SPI\_RSP\_TYPE\_R5](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a0d82c7d93c187de5c40c0ff83fe8a478)

@ SD\_SPI\_RSP\_TYPE\_R5

**Definition** sd\_spec.h:232

[SD\_SPI\_RSP\_TYPE\_R1b](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a22413680849a7645c7e8c585b5184203)

@ SD\_SPI\_RSP\_TYPE\_R1b

**Definition** sd\_spec.h:228

[SD\_SPI\_RSP\_TYPE\_R1](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a32b2c65c90d0d5b8df5e4a82e9b95a6d)

@ SD\_SPI\_RSP\_TYPE\_R1

**Definition** sd\_spec.h:227

[SD\_RSP\_TYPE\_R4](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a34b03331e8f7a9ea6b67da6b68c7e0ed)

@ SD\_RSP\_TYPE\_R4

**Definition** sd\_spec.h:221

[SD\_RSP\_TYPE\_R6](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a3532733bc007df5009801bd6f09e45c9)

@ SD\_RSP\_TYPE\_R6

**Definition** sd\_spec.h:224

[SD\_SPI\_RSP\_TYPE\_R4](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a4c35ca3a8db652008204cf0cfc8e2339)

@ SD\_SPI\_RSP\_TYPE\_R4

**Definition** sd\_spec.h:231

[SD\_RSP\_TYPE\_R5b](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a5dcd82e4fe5a34646a617a5031fdc638)

@ SD\_RSP\_TYPE\_R5b

**Definition** sd\_spec.h:223

[SD\_SPI\_RSP\_TYPE\_R7](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a78472618e8523bf73ca65aee6b0a8318)

@ SD\_SPI\_RSP\_TYPE\_R7

**Definition** sd\_spec.h:233

[SD\_SPI\_RSP\_TYPE\_R3](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a7c44711a51e8175ebcaf4be24e2daec3)

@ SD\_SPI\_RSP\_TYPE\_R3

**Definition** sd\_spec.h:230

[SD\_SPI\_RSP\_TYPE\_R2](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a855f8e4399cf3ce0c05c6089f3439ec2)

@ SD\_SPI\_RSP\_TYPE\_R2

**Definition** sd\_spec.h:229

[SD\_RSP\_TYPE\_R5](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a91e216f8a1753b4719ee91819a926dde)

@ SD\_RSP\_TYPE\_R5

**Definition** sd\_spec.h:222

[SD\_RSP\_TYPE\_R1](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a92718e4bd4bccaa2fe4a8780228004d7)

@ SD\_RSP\_TYPE\_R1

**Definition** sd\_spec.h:217

[SD\_RSP\_TYPE\_R2](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6a96e26220a32f9b6e9e0bdd8c94d48eaf)

@ SD\_RSP\_TYPE\_R2

**Definition** sd\_spec.h:219

[SD\_RSP\_TYPE\_R7](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6aa5657942fb906d58ef2b7bed05137f23)

@ SD\_RSP\_TYPE\_R7

**Definition** sd\_spec.h:225

[SD\_RSP\_TYPE\_NONE](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6ad74407536823c1ea3afdf41d4b858b1c)

@ SD\_RSP\_TYPE\_NONE

**Definition** sd\_spec.h:216

[SD\_RSP\_TYPE\_R1b](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6ae64496ba1520651f8bac35af2531eaf8)

@ SD\_RSP\_TYPE\_R1b

**Definition** sd\_spec.h:218

[SD\_RSP\_TYPE\_R3](sd__spec_8h.md#a1cfd2df5ec76eeb915fd3689408a65d6af779f08bfb2fd73a717ea3789ccad509)

@ SD\_RSP\_TYPE\_R3

**Definition** sd\_spec.h:220

[hs\_max\_data\_rate](sd__spec_8h.md#a2093143614e52f69e173289391d7e91c)

hs\_max\_data\_rate

**Definition** sd\_spec.h:371

[HS\_MAX\_DTR](sd__spec_8h.md#a2093143614e52f69e173289391d7e91ca10f805e3f66366474428718cb4569da0)

@ HS\_MAX\_DTR

**Definition** sd\_spec.h:373

[HS\_UNSUPPORTED](sd__spec_8h.md#a2093143614e52f69e173289391d7e91cac3e8d67442f59c35b57d19d81b5d0d66)

@ HS\_UNSUPPORTED

**Definition** sd\_spec.h:372

[sd\_current\_limit](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537)

sd\_current\_limit

SD current support bitfield.

**Definition** sd\_spec.h:460

[SD\_MAX\_CURRENT\_200MA](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537a18b21e5e76bea0263f475ecc228c0301)

@ SD\_MAX\_CURRENT\_200MA

default current limit

**Definition** sd\_spec.h:462

[SD\_MAX\_CURRENT\_800MA](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537a2e3c01bc8d16641d7b500ce1244dbb03)

@ SD\_MAX\_CURRENT\_800MA

current limit to 800MA

**Definition** sd\_spec.h:468

[SD\_MAX\_CURRENT\_400MA](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537ae0605a0d9fc89e094a40b03e96c02339)

@ SD\_MAX\_CURRENT\_400MA

current limit to 400MA

**Definition** sd\_spec.h:464

[SD\_MAX\_CURRENT\_600MA](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537af82a5f23e51bf3ac3b7bec137269f540)

@ SD\_MAX\_CURRENT\_600MA

current limit to 600MA

**Definition** sd\_spec.h:466

[sdio\_io\_dir](sd__spec_8h.md#a250ae2ce54e941895a720b565632350e)

sdio\_io\_dir

SDIO I/O direction.

**Definition** sd\_spec.h:801

[SDIO\_IO\_WRITE](sd__spec_8h.md#a250ae2ce54e941895a720b565632350eabd26fc6f76267231c78eae8be9ebb885)

@ SDIO\_IO\_WRITE

**Definition** sd\_spec.h:803

[SDIO\_IO\_READ](sd__spec_8h.md#a250ae2ce54e941895a720b565632350eac1212149d096232e75d1d090abb4974c)

@ SDIO\_IO\_READ

**Definition** sd\_spec.h:802

[sdio\_ocr\_flag](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6)

sdio\_ocr\_flag

SDIO OCR bit flags.

**Definition** sd\_spec.h:315

[SDIO\_OCR\_VDD31\_32FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a018af73c25e22c6e5313e5e3cff57e92)

@ SDIO\_OCR\_VDD31\_32FLAG

VDD 3.0-3.1.

**Definition** sd\_spec.h:331

[SDIO\_OCR\_VDD28\_29FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a1071312f18c64077e6964e421ef00ead)

@ SDIO\_OCR\_VDD28\_29FLAG

VDD 2.8-2.9.

**Definition** sd\_spec.h:328

[SDIO\_OCR\_IO\_NUMBER](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a17007c3d37f047e6db56491a4230e8a8)

@ SDIO\_OCR\_IO\_NUMBER

Number of io function.

**Definition** sd\_spec.h:317

[SDIO\_OCR\_VDD27\_28FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a1f043936c614ac39b75f3835dc498b94)

@ SDIO\_OCR\_VDD27\_28FLAG

VDD 2.7-2.8.

**Definition** sd\_spec.h:327

[SDIO\_OCR\_VDD29\_30FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a246619651470476238452550068db8a0)

@ SDIO\_OCR\_VDD29\_30FLAG

VDD 2.9-3.0.

**Definition** sd\_spec.h:329

[SDIO\_OCR\_VDD34\_35FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a3d791855e6df402d5bfd92ce216a9a4b)

@ SDIO\_OCR\_VDD34\_35FLAG

VDD 3.3-3.4.

**Definition** sd\_spec.h:334

[SDIO\_OCR\_180\_VOL\_FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a3f6ebe270ba873bab3407ee7d655b53d)

@ SDIO\_OCR\_180\_VOL\_FLAG

Switch to 1.8v signalling.

**Definition** sd\_spec.h:319

[SDIO\_OCR\_VDD30\_31FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a4cb1cc23687e7a1854d8af0c76876a20)

@ SDIO\_OCR\_VDD30\_31FLAG

VDD 2.9-3.0.

**Definition** sd\_spec.h:330

[SDIO\_OCR\_VDD26\_27FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a4d32525a631342d78f73b6296e148666)

@ SDIO\_OCR\_VDD26\_27FLAG

VDD 2.6-2.7.

**Definition** sd\_spec.h:326

[SDIO\_OCR\_VDD22\_23FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a560f91eb371bfea5cf6c5c036cc9c096)

@ SDIO\_OCR\_VDD22\_23FLAG

VDD 2.2-2.3.

**Definition** sd\_spec.h:322

[SDIO\_OCR\_VDD24\_25FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a6323aa0a8cbfb59f8209a37c8135079c)

@ SDIO\_OCR\_VDD24\_25FLAG

VDD 2.4-2.5.

**Definition** sd\_spec.h:324

[SDIO\_OCR\_VDD33\_34FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a6673f837fa5a98b573886c5e6429c644)

@ SDIO\_OCR\_VDD33\_34FLAG

VDD 3.2-3.3.

**Definition** sd\_spec.h:333

[SDIO\_OCR\_VDD23\_24FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6a89c4025349ece0021cd627101f0efdd1)

@ SDIO\_OCR\_VDD23\_24FLAG

VDD 2.3-2.4.

**Definition** sd\_spec.h:323

[SDIO\_OCR\_VDD20\_21FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6aa7a656a21495fbf64666b2b80236e4e4)

@ SDIO\_OCR\_VDD20\_21FLAG

VDD 2.0-2.1.

**Definition** sd\_spec.h:320

[SDIO\_OCR\_VDD25\_26FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ac0aa0897e1bbf45b0f5f4de73d733477)

@ SDIO\_OCR\_VDD25\_26FLAG

VDD 2.5-2.6.

**Definition** sd\_spec.h:325

[SDIO\_OCR\_VDD32\_33FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ac5613e6858d2c9217165ab4cbb240012)

@ SDIO\_OCR\_VDD32\_33FLAG

VDD 3.1-3.2.

**Definition** sd\_spec.h:332

[SDIO\_OCR\_VDD21\_22FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ad75d7d47a3d5fcc39a68c08546e9793b)

@ SDIO\_OCR\_VDD21\_22FLAG

VDD 2.1-2.2.

**Definition** sd\_spec.h:321

[SDIO\_OCR\_IO\_READY\_FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6adb3e45e84da812297359d6054baa69ba)

@ SDIO\_OCR\_IO\_READY\_FLAG

**Definition** sd\_spec.h:316

[SDIO\_OCR\_MEM\_PRESENT\_FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6ae923fdf459570657220ec225cbed7336)

@ SDIO\_OCR\_MEM\_PRESENT\_FLAG

Memory present flag.

**Definition** sd\_spec.h:318

[SDIO\_OCR\_VDD35\_36FLAG](sd__spec_8h.md#a296cbe236e9e36dc79ca30eb54e6bcc6af0baaa7f71d144c7e5edade4b2445813)

@ SDIO\_OCR\_VDD35\_36FLAG

VDD 3.4-3.5.

**Definition** sd\_spec.h:335

[mmc\_csd\_freq](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8)

mmc\_csd\_freq

MMC Maximum Frequency.

**Definition** sd\_spec.h:585

[MMC\_MAXFREQ\_100MHZ](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a13c703d344a1e03c1aa5881a77980085)

@ MMC\_MAXFREQ\_100MHZ

**Definition** sd\_spec.h:589

[MMC\_MAXFREQ\_100KHZ](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a221dc45c7b73f6f96a63acbeb3e5e121)

@ MMC\_MAXFREQ\_100KHZ

**Definition** sd\_spec.h:586

[MMC\_MAXFREQ\_MULT\_80](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a24ea8c9db5531b5404bb667da26ac5d0)

@ MMC\_MAXFREQ\_MULT\_80

**Definition** sd\_spec.h:604

[MMC\_MAXFREQ\_MULT\_13](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a2c639715b63769e9a431a93e636f007e)

@ MMC\_MAXFREQ\_MULT\_13

**Definition** sd\_spec.h:592

[MMC\_MAXFREQ\_1MHZ](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a32c9f5017cd49c9ca4b352269de6eeff)

@ MMC\_MAXFREQ\_1MHZ

**Definition** sd\_spec.h:587

[MMC\_MAXFREQ\_MULT\_12](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a4a3b8dc88c6349fb5f49ed3062a39a17)

@ MMC\_MAXFREQ\_MULT\_12

**Definition** sd\_spec.h:591

[MMC\_MAXFREQ\_MULT\_40](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a572d53afafb39341e0cdb80d2d041d2c)

@ MMC\_MAXFREQ\_MULT\_40

**Definition** sd\_spec.h:598

[MMC\_MAXFREQ\_MULT\_45](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a5bd0506d7efbecdc42eb8fae1427dc37)

@ MMC\_MAXFREQ\_MULT\_45

**Definition** sd\_spec.h:599

[MMC\_MAXFREQ\_MULT\_35](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a63c0eee223946b1ae2b187bb585dfde4)

@ MMC\_MAXFREQ\_MULT\_35

**Definition** sd\_spec.h:597

[MMC\_MAXFREQ\_MULT\_30](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a69e1d369d668d63071410078a31099a0)

@ MMC\_MAXFREQ\_MULT\_30

**Definition** sd\_spec.h:596

[MMC\_MAXFREQ\_MULT\_10](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a74d01430b854f42ea84dba9d3ce45b16)

@ MMC\_MAXFREQ\_MULT\_10

**Definition** sd\_spec.h:590

[MMC\_MAXFREQ\_MULT\_52](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8a988f18b9f418744721b0fc91f2432449)

@ MMC\_MAXFREQ\_MULT\_52

**Definition** sd\_spec.h:600

[MMC\_MAXFREQ\_MULT\_26](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ab1ff3da74a0dea49ffe7ac1d945ec4e6)

@ MMC\_MAXFREQ\_MULT\_26

**Definition** sd\_spec.h:595

[MMC\_MAXFREQ\_MULT\_55](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8abecfcd6d212185c74b57941c3fa58233)

@ MMC\_MAXFREQ\_MULT\_55

**Definition** sd\_spec.h:601

[MMC\_MAXFREQ\_MULT\_20](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ac8848c5cdf177737744da3283f7140d5)

@ MMC\_MAXFREQ\_MULT\_20

**Definition** sd\_spec.h:594

[MMC\_MAXFREQ\_MULT\_15](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8ac988a54239b7d9e182f1b2f480567e66)

@ MMC\_MAXFREQ\_MULT\_15

**Definition** sd\_spec.h:593

[MMC\_MAXFREQ\_MULT\_60](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8adf578325509923b46e3ff4fbd74889ad)

@ MMC\_MAXFREQ\_MULT\_60

**Definition** sd\_spec.h:602

[MMC\_MAXFREQ\_MULT\_70](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8aee24df1d628479fe2d920839a0bf5012)

@ MMC\_MAXFREQ\_MULT\_70

**Definition** sd\_spec.h:603

[MMC\_MAXFREQ\_10MHZ](sd__spec_8h.md#a313c45576db4ae219288fb4fbaad4bd8af63af4938d5aad64bac19fac42aedd10)

@ MMC\_MAXFREQ\_10MHZ

**Definition** sd\_spec.h:588

[sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b)

sd\_driver\_type

SD driver types.

**Definition** sd\_spec.h:476

[SD\_DRIVER\_TYPE\_C](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba0cd41f5198ce06ce5925b3f52d48b0a2)

@ SD\_DRIVER\_TYPE\_C

**Definition** sd\_spec.h:479

[SD\_DRIVER\_TYPE\_B](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba32ad0894344bc4980f9206022ed0f877)

@ SD\_DRIVER\_TYPE\_B

**Definition** sd\_spec.h:477

[SD\_DRIVER\_TYPE\_D](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba435b458d33f1568cb76b77a3ea2e1eb8)

@ SD\_DRIVER\_TYPE\_D

**Definition** sd\_spec.h:480

[SD\_DRIVER\_TYPE\_A](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4ba9eec5ff6f7d4c7512212cb48719dcabf)

@ SD\_DRIVER\_TYPE\_A

**Definition** sd\_spec.h:478

[sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6)

sdio\_func\_num

SDIO function number.

**Definition** sd\_spec.h:784

[SDIO\_FUNC\_MEMORY](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a075731d15b2f4b7c7448d6d4ee059880)

@ SDIO\_FUNC\_MEMORY

**Definition** sd\_spec.h:793

[SDIO\_FUNC\_NUM\_6](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a2a9baef178307d6e6006ea88b4da383c)

@ SDIO\_FUNC\_NUM\_6

**Definition** sd\_spec.h:791

[SDIO\_FUNC\_NUM\_7](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a617d1991d70033df3b39eef7ccb98b48)

@ SDIO\_FUNC\_NUM\_7

**Definition** sd\_spec.h:792

[SDIO\_FUNC\_NUM\_1](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a900536b934da03f8e8590de3e3d56296)

@ SDIO\_FUNC\_NUM\_1

**Definition** sd\_spec.h:786

[SDIO\_FUNC\_NUM\_4](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6a9b69d64108c6564bc313e4fb2b53f61c)

@ SDIO\_FUNC\_NUM\_4

**Definition** sd\_spec.h:789

[SDIO\_FUNC\_NUM\_2](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ac2cc5967daee0a3e9ef61c9c486b3a6c)

@ SDIO\_FUNC\_NUM\_2

**Definition** sd\_spec.h:787

[SDIO\_FUNC\_NUM\_5](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ac62397290371f5fb3fdf8d4b52fb3575)

@ SDIO\_FUNC\_NUM\_5

**Definition** sd\_spec.h:790

[SDIO\_FUNC\_NUM\_0](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6ad7a10f97094ddb96f26ab44fc34de12a)

@ SDIO\_FUNC\_NUM\_0

**Definition** sd\_spec.h:785

[SDIO\_FUNC\_NUM\_3](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6adef5748e2622dab22da33504bbafa149)

@ SDIO\_FUNC\_NUM\_3

**Definition** sd\_spec.h:788

[sd\_scr\_flag](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553)

sd\_scr\_flag

SD card configuration register.

**Definition** sd\_spec.h:753

[SD\_SCR\_SPEC3](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553a59fb3a34a7dba6ed1c86bca21cf97871)

@ SD\_SCR\_SPEC3

Specification version 3.00 or higher [47:47].

**Definition** sd\_spec.h:757

[SD\_SCR\_DATA\_STATUS\_AFTER\_ERASE](sd__spec_8h.md#a476ec98763d90a5cba336cbf22d6d553a759c63670d0dd41590fdb940a48ac4dd)

@ SD\_SCR\_DATA\_STATUS\_AFTER\_ERASE

Data status after erases [55:55].

**Definition** sd\_spec.h:755

[uhs\_max\_data\_rate](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9a)

uhs\_max\_data\_rate

**Definition** sd\_spec.h:377

[UHS\_SDR104\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa106c43d63c3b3c02d3835ccf542f3190)

@ UHS\_SDR104\_MAX\_DTR

**Definition** sd\_spec.h:382

[UHS\_SDR25\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa5c5c100c048986ecfed728690d05ac55)

@ UHS\_SDR25\_MAX\_DTR

**Definition** sd\_spec.h:380

[UHS\_SDR50\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aa72e9ad81edf54b7139a758d47fe54dd5)

@ UHS\_SDR50\_MAX\_DTR

**Definition** sd\_spec.h:381

[UHS\_UNSUPPORTED](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aaad6eabbee29e4ff07bdf93a9162aea6b)

@ UHS\_UNSUPPORTED

**Definition** sd\_spec.h:378

[UHS\_SDR12\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aad61b9d180a8de3c01be2e892c45504fb)

@ UHS\_SDR12\_MAX\_DTR

**Definition** sd\_spec.h:379

[UHS\_DDR50\_MAX\_DTR](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9aaff651e04c107beb23e0bd76d03029b26)

@ UHS\_DDR50\_MAX\_DTR

**Definition** sd\_spec.h:383

[sd\_current\_setting](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972)

sd\_current\_setting

SD current setting values.

**Definition** sd\_spec.h:448

[SD\_SET\_CURRENT\_200MA](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972a134ed84475be6f55a0f3d3ae9201cbe9)

@ SD\_SET\_CURRENT\_200MA

**Definition** sd\_spec.h:449

[SD\_SET\_CURRENT\_600MA](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972a83f1d375e4c5aa645759cc4e4462f8e0)

@ SD\_SET\_CURRENT\_600MA

**Definition** sd\_spec.h:451

[SD\_SET\_CURRENT\_400MA](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972ad548c59ebbb5045e437157cb9186de19)

@ SD\_SET\_CURRENT\_400MA

**Definition** sd\_spec.h:450

[SD\_SET\_CURRENT\_800MA](sd__spec_8h.md#a5ac0e70389dc6ccec515530df4eab972af44faa0f33705ecbd37b5f3544105e34)

@ SD\_SET\_CURRENT\_800MA

**Definition** sd\_spec.h:452

[sd\_driver\_strength](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2)

sd\_driver\_strength

SD switch drive type selection.

**Definition** sd\_spec.h:488

[SD\_DRV\_STRENGTH\_TYPEB](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2a1b1e411f733ad6c1dc41896744441a48)

@ SD\_DRV\_STRENGTH\_TYPEB

default driver strength

**Definition** sd\_spec.h:490

[SD\_DRV\_STRENGTH\_TYPEC](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2aa3e190aa6edb9f6eb7e29b78fc6f1a8a)

@ SD\_DRV\_STRENGTH\_TYPEC

driver strength TYPE C

**Definition** sd\_spec.h:494

[SD\_DRV\_STRENGTH\_TYPED](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2ad5753bf6fae3f43ef8ce7cb7eb169b61)

@ SD\_DRV\_STRENGTH\_TYPED

driver strength TYPE D

**Definition** sd\_spec.h:496

[SD\_DRV\_STRENGTH\_TYPEA](sd__spec_8h.md#a66c69cd7d7818af86b6a91fad68334c2ad870ea9b9fc07a4af81bce3c82330441)

@ SD\_DRV\_STRENGTH\_TYPEA

driver strength TYPE A

**Definition** sd\_spec.h:492

[sd\_bus\_speed](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36)

sd\_bus\_speed

SD bus speed support bit flags.

**Definition** sd\_spec.h:392

[UHS\_DDR50\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a022acb9d379c5ecf9935150ec6f51ffc)

@ UHS\_DDR50\_BUS\_SPEED

**Definition** sd\_spec.h:399

[UHS\_SDR12\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a30f38c9e54bed572ca315fdeb9122103)

@ UHS\_SDR12\_BUS\_SPEED

**Definition** sd\_spec.h:393

[UHS\_SDR50\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a360c72912e023e5b21363f3701deaa50)

@ UHS\_SDR50\_BUS\_SPEED

**Definition** sd\_spec.h:397

[HIGH\_SPEED\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a5593992de690adb1022b7926d1508ab3)

@ HIGH\_SPEED\_BUS\_SPEED

**Definition** sd\_spec.h:395

[DEFAULT\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36a90413fe7dfd8568eeac79709ece7a549)

@ DEFAULT\_BUS\_SPEED

**Definition** sd\_spec.h:394

[UHS\_SDR25\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36ae07a7ef1ffce64bab52c5f6612a96716)

@ UHS\_SDR25\_BUS\_SPEED

**Definition** sd\_spec.h:396

[UHS\_SDR104\_BUS\_SPEED](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36aef2ef100dab4187c8600ea721e8726dd)

@ UHS\_SDR104\_BUS\_SPEED

**Definition** sd\_spec.h:398

[sd\_switch\_arg](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3)

sd\_switch\_arg

SD switch arguments.

**Definition** sd\_spec.h:346

[SD\_SWITCH\_SET](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3a72c39e3140ddd3990c3cbe7c6c867bb1)

@ SD\_SWITCH\_SET

SD switch mode 1: set function.

**Definition** sd\_spec.h:350

[SD\_SWITCH\_CHECK](sd__spec_8h.md#a76f7ea4b395028ad5d8cc5eee32656e3ae126f56fd639cbd686321a088d1e05e6)

@ SD\_SWITCH\_CHECK

SD switch mode 0: check function.

**Definition** sd\_spec.h:348

[sd\_ocr\_flag](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61)

sd\_ocr\_flag

SD OCR bit flags.

**Definition** sd\_spec.h:260

[SD\_OCR\_VDD32\_33FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a0c8a74f1b50f574b64184bf1cdc1458f)

@ SD\_OCR\_VDD32\_33FLAG

VDD 3.2-3.3.

**Definition** sd\_spec.h:282

[SD\_OCR\_CARD\_CAP\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a4cfc3b5856c525eda63b3a8b5fce5ae2)

@ SD\_OCR\_CARD\_CAP\_FLAG

Card capacity status.

**Definition** sd\_spec.h:266

[SD\_OCR\_SWITCH\_18\_ACCEPT\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a541be7abf94851538a38f69c2ecb6b5f)

@ SD\_OCR\_SWITCH\_18\_ACCEPT\_FLAG

Switch to 1.8V accepted.

**Definition** sd\_spec.h:270

[SD\_OCR\_PWR\_BUSY\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a5f680f7a518294d7a706b73bbecbdb73)

@ SD\_OCR\_PWR\_BUSY\_FLAG

Power up busy status.

**Definition** sd\_spec.h:262

[SD\_OCR\_VDD29\_30FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a624191bea93e1a350073fe2e5d5adaf1)

@ SD\_OCR\_VDD29\_30FLAG

VDD 2.9-3.0.

**Definition** sd\_spec.h:276

[SD\_OCR\_SWITCH\_18\_REQ\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a69d58775148ae7daf65598d6cf90488d)

@ SD\_OCR\_SWITCH\_18\_REQ\_FLAG

Switch to 1.8V request.

**Definition** sd\_spec.h:268

[SD\_OCR\_VDD28\_29FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a76356316ead27df98dac310eed775707)

@ SD\_OCR\_VDD28\_29FLAG

VDD 2.8-2.9.

**Definition** sd\_spec.h:274

[SD\_OCR\_VDD35\_36FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a83a9f603da11b75f200d3bb62528cda4)

@ SD\_OCR\_VDD35\_36FLAG

VDD 3.5-3.6.

**Definition** sd\_spec.h:288

[SD\_OCR\_VDD31\_32FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a8ae4a104d50c0bdcae4722de0d5ee605)

@ SD\_OCR\_VDD31\_32FLAG

VDD 3.1-3.2.

**Definition** sd\_spec.h:280

[SD\_OCR\_VDD30\_31FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61a98c205ed0f08df1a2f9e2801f02bbe7f)

@ SD\_OCR\_VDD30\_31FLAG

VDD 3.0-3.1.

**Definition** sd\_spec.h:278

[SD\_OCR\_VDD33\_34FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61aca49de7bd24df65fd6448a7e570b04a8)

@ SD\_OCR\_VDD33\_34FLAG

VDD 3.3-3.4.

**Definition** sd\_spec.h:284

[SD\_OCR\_VDD27\_28FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61acd85dd4f874ed9088e6d7a2260d7bc50)

@ SD\_OCR\_VDD27\_28FLAG

VDD 2.7-2.8.

**Definition** sd\_spec.h:272

[SD\_OCR\_HOST\_CAP\_FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae344e23bbc73a6f2ed17d10618bf7a5a)

@ SD\_OCR\_HOST\_CAP\_FLAG

Card capacity status.

**Definition** sd\_spec.h:264

[SD\_OCR\_VDD34\_35FLAG](sd__spec_8h.md#a7b20cc85df2d9f5ce6c010907d7d5c61ae5e13b78bf3fdece36190e48136927bf)

@ SD\_OCR\_VDD34\_35FLAG

VDD 3.4-3.5.

**Definition** sd\_spec.h:286

[SD\_PRODUCT\_NAME\_BYTES](sd__spec_8h.md#a947520a05fc99c25449fab98d0d02b1e)

#define SD\_PRODUCT\_NAME\_BYTES

**Definition** sd\_spec.h:514

[sdhc\_clock\_speed](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539)

sdhc\_clock\_speed

SD host controller clock speed.

**Definition** sd\_spec.h:430

[MMC\_CLOCK\_HS200](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a14dec2b314ed13974dbba31f33a5eab9)

@ MMC\_CLOCK\_HS200

**Definition** sd\_spec.h:439

[SDMMC\_CLOCK\_400KHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a16c56ed964cc6bbb5cc6f0cb857d4f10)

@ SDMMC\_CLOCK\_400KHZ

**Definition** sd\_spec.h:431

[SD\_CLOCK\_50MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a39e410f7f5c51753bf415f727551b9fb)

@ SD\_CLOCK\_50MHZ

**Definition** sd\_spec.h:433

[MMC\_CLOCK\_52MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a5c37aeeb3c68d7b3dbe8b9001a00507c)

@ MMC\_CLOCK\_52MHZ

**Definition** sd\_spec.h:437

[MMC\_CLOCK\_DDR52](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a66ecc8c1a73181d70e23424cf718728d)

@ MMC\_CLOCK\_DDR52

**Definition** sd\_spec.h:438

[SD\_CLOCK\_100MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a66ef44acd4ff3fafc2d49120df4b3c10)

@ SD\_CLOCK\_100MHZ

**Definition** sd\_spec.h:434

[MMC\_CLOCK\_HS400](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a788a77f1e7a468c14ef57319ef8938f3)

@ MMC\_CLOCK\_HS400

**Definition** sd\_spec.h:440

[SD\_CLOCK\_208MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539a9570bb04b0181b4fbdc96cace060d187)

@ SD\_CLOCK\_208MHZ

**Definition** sd\_spec.h:435

[SD\_CLOCK\_25MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539ad5e9d57ee155e1b919f6cc213b05424f)

@ SD\_CLOCK\_25MHZ

**Definition** sd\_spec.h:432

[MMC\_CLOCK\_26MHZ](sd__spec_8h.md#a9660a61775e481ae4093e11ce9336539ae9369c1cd7595ab83289fc356e9cc1b6)

@ MMC\_CLOCK\_26MHZ

**Definition** sd\_spec.h:436

[sd\_group\_num](sd__spec_8h.md#a97f4810585247f5fed41110413e49853)

sd\_group\_num

SD switch group numbers.

**Definition** sd\_spec.h:359

[SD\_GRP\_TIMING\_MODE](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a488b1aac4a0658c8b04b94b7556a2c5b)

@ SD\_GRP\_TIMING\_MODE

access mode group

**Definition** sd\_spec.h:361

[SD\_GRP\_DRIVER\_STRENGTH\_MODE](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a5e617dd9de3620481b89e517bd2c3a4b)

@ SD\_GRP\_DRIVER\_STRENGTH\_MODE

driver strength group

**Definition** sd\_spec.h:365

[SD\_GRP\_CMD\_SYS\_MODE](sd__spec_8h.md#a97f4810585247f5fed41110413e49853a8c620d198b195d913ad3ff913434d764)

@ SD\_GRP\_CMD\_SYS\_MODE

command system group

**Definition** sd\_spec.h:363

[SD\_GRP\_CURRENT\_LIMIT\_MODE](sd__spec_8h.md#a97f4810585247f5fed41110413e49853aa38ef885442708891b4ddc4a83c6ff66)

@ SD\_GRP\_CURRENT\_LIMIT\_MODE

current limit group

**Definition** sd\_spec.h:367

[sd\_csd\_flag](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437)

sd\_csd\_flag

SD card specific data flags.

**Definition** sd\_spec.h:699

[SD\_CSD\_ERASE\_BLK\_EN\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a0d907c1a9e69435433c5bf19bfacbd73)

@ SD\_CSD\_ERASE\_BLK\_EN\_FLAG

Erase single block enabled [46:46].

**Definition** sd\_spec.h:709

[SD\_CSD\_DSR\_IMPLEMENTED\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a1258364107909d0c4f8e9b7dba59300c)

@ SD\_CSD\_DSR\_IMPLEMENTED\_FLAG

DSR implemented [76:76].

**Definition** sd\_spec.h:707

[SD\_CSD\_WRITE\_BLK\_MISALIGN\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a16d3fd179853f1f15b980d2b82b572be)

@ SD\_CSD\_WRITE\_BLK\_MISALIGN\_FLAG

Write block misalignment [78:78].

**Definition** sd\_spec.h:703

[SD\_CSD\_FILE\_FMT\_GRP\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a2e75506280c1b4d5866f4dd8f2518be8)

@ SD\_CSD\_FILE\_FMT\_GRP\_FLAG

File format group [15:15].

**Definition** sd\_spec.h:715

[SD\_CSD\_PERMANENT\_WRITE\_PROTECT\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a7496edd5c7ec694d2d175bf751de1458)

@ SD\_CSD\_PERMANENT\_WRITE\_PROTECT\_FLAG

Permanent write protection [13:13].

**Definition** sd\_spec.h:719

[SD\_CSD\_COPY\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437a988758fe0720e6fc33564076e3bc51bf)

@ SD\_CSD\_COPY\_FLAG

Copy flag [14:14].

**Definition** sd\_spec.h:717

[SD\_CSD\_TMP\_WRITE\_PROTECT\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aa0c70fee97e29875394efc2a4c2fa274)

@ SD\_CSD\_TMP\_WRITE\_PROTECT\_FLAG

Temporary write protection [12:12].

**Definition** sd\_spec.h:721

[SD\_CSD\_WRITE\_BLK\_PARTIAL\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aa8b8f850196e47799cb9b2cd06650520)

@ SD\_CSD\_WRITE\_BLK\_PARTIAL\_FLAG

Partial blocks for write allowed [21:21].

**Definition** sd\_spec.h:713

[SD\_CSD\_READ\_BLK\_PARTIAL\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437ac353a0c3c1ac62920efdc42879a81cff)

@ SD\_CSD\_READ\_BLK\_PARTIAL\_FLAG

Partial blocks for read allowed [79:79].

**Definition** sd\_spec.h:701

[SD\_CSD\_READ\_BLK\_MISALIGN\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437aca7d98319db6a23b30625828807e2143)

@ SD\_CSD\_READ\_BLK\_MISALIGN\_FLAG

Read block misalignment [77:77].

**Definition** sd\_spec.h:705

[SD\_CSD\_WRITE\_PROTECT\_GRP\_EN\_FLAG](sd__spec_8h.md#a98c4f218acfa21e124aa22e9fe209437af85839612e4fcc94eb2bd0986bd1740c)

@ SD\_CSD\_WRITE\_PROTECT\_GRP\_EN\_FLAG

Write protect group enabled [31:31].

**Definition** sd\_spec.h:711

[sd\_r1\_current\_state](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065)

sd\_r1\_current\_state

SD current state values.

**Definition** sd\_spec.h:138

[SDMMC\_R1\_IDLE](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a081f03ba34d8cd168ab5d4172d3c8d6a)

@ SDMMC\_R1\_IDLE

**Definition** sd\_spec.h:139

[SDMMC\_R1\_READY](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a135f072a7d9ee5967a49f7a164816854)

@ SDMMC\_R1\_READY

**Definition** sd\_spec.h:140

[SDMMC\_R1\_IDENTIFY](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a1ddcc2a60e6f83538151fc93ad434ddf)

@ SDMMC\_R1\_IDENTIFY

**Definition** sd\_spec.h:141

[SDMMC\_R1\_RECIVE\_DATA](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a3feb7a1594dc32703d2fbf6e43e77c0c)

@ SDMMC\_R1\_RECIVE\_DATA

**Definition** sd\_spec.h:145

[SDMMC\_R1\_TRANSFER](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a59ead4a70e76c9b2d6c817f4e2847998)

@ SDMMC\_R1\_TRANSFER

**Definition** sd\_spec.h:143

[SDMMC\_R1\_SEND\_DATA](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065a5d6d02968e18dd84af3583d282179e64)

@ SDMMC\_R1\_SEND\_DATA

**Definition** sd\_spec.h:144

[SDMMC\_R1\_DISCONNECT](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065abebe32c9b1e107c729f4e6ecf501ee1e)

@ SDMMC\_R1\_DISCONNECT

**Definition** sd\_spec.h:147

[SDMMC\_R1\_STANDBY](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065ac906ebc564bfc63a7f4ce0350db6667b)

@ SDMMC\_R1\_STANDBY

**Definition** sd\_spec.h:142

[SDMMC\_R1\_PROGRAM](sd__spec_8h.md#aa0686c333989b0551d3af5eb01de4065acccc283c3dc4a36992e76ea0b6f4d68b)

@ SDMMC\_R1\_PROGRAM

**Definition** sd\_spec.h:146

[sd\_spi\_r2\_status](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878f)

sd\_spi\_r2\_status

SPI SD mode R2 response status flags.

**Definition** sd\_spec.h:171

[SDHC\_SPI\_R2\_UNLOCK\_FAIL](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa3f8fde9c17c04f4500f5a86cf4d9e7df)

@ SDHC\_SPI\_R2\_UNLOCK\_FAIL

**Definition** sd\_spec.h:173

[SDHC\_SPI\_R2\_ERASE\_PARAM](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa47bb6389f20ceb840612266fedac0f7a)

@ SDHC\_SPI\_R2\_ERASE\_PARAM

**Definition** sd\_spec.h:178

[SDHC\_SPI\_R2\_CARD\_LOCKED](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa8f693e2ff4acfb3d652106fc25f8758f)

@ SDHC\_SPI\_R2\_CARD\_LOCKED

**Definition** sd\_spec.h:172

[SDHC\_SPI\_R2\_WP\_VIOLATION](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fa92bcd0ee78ddba8dc551c7917a37a792)

@ SDHC\_SPI\_R2\_WP\_VIOLATION

**Definition** sd\_spec.h:177

[SDHC\_SPI\_R2\_ECC\_FAIL](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fac853010c32e85d30f9f5936851ac4ddb)

@ SDHC\_SPI\_R2\_ECC\_FAIL

**Definition** sd\_spec.h:176

[SDHC\_SPI\_R2\_CC\_ERR](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878fad33e5499a36259f5b881ce524a1f4159)

@ SDHC\_SPI\_R2\_CC\_ERR

**Definition** sd\_spec.h:175

[SDHC\_SPI\_R2\_OUT\_OF\_RANGE](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878faedbd66fd01bb87a4f55291c299589db7)

@ SDHC\_SPI\_R2\_OUT\_OF\_RANGE

**Definition** sd\_spec.h:179

[SDHC\_SPI\_R2\_ERR](sd__spec_8h.md#aa1b9e80034c783cc7ff43dc79ac5878faf74a4730cc3507a35179fe09da721a19)

@ SDHC\_SPI\_R2\_ERR

**Definition** sd\_spec.h:174

[sd\_spi\_r1\_error\_flag](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3)

sd\_spi\_r1\_error\_flag

SPI SD mode R1 response status flags.

**Definition** sd\_spec.h:155

[SD\_SPI\_R1ILLEGAL\_CMD\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a0a59356a4db1abd3f72a8c9778b04e66)

@ SD\_SPI\_R1ILLEGAL\_CMD\_ERR

**Definition** sd\_spec.h:160

[SD\_SPI\_R1ERASE\_RESET](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a4eb47f187f4aee8228b09a37d4669a4f)

@ SD\_SPI\_R1ERASE\_RESET

**Definition** sd\_spec.h:161

[SD\_SPI\_R1IDLE\_STATE](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3a9c77ef6b4da1f8ac56ebe8be03504b69)

@ SD\_SPI\_R1IDLE\_STATE

**Definition** sd\_spec.h:162

[SD\_SPI\_R1ERASE\_SEQ\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3aa07d3031debe394b369d93fde728d406)

@ SD\_SPI\_R1ERASE\_SEQ\_ERR

**Definition** sd\_spec.h:158

[SD\_SPI\_R1PARAMETER\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3aae5e5c58313c1216448474da513ca2b6)

@ SD\_SPI\_R1PARAMETER\_ERR

**Definition** sd\_spec.h:156

[SD\_SPI\_R1CMD\_CRC\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3ae4785671c3a4dca332c10c9bc0a72fba)

@ SD\_SPI\_R1CMD\_CRC\_ERR

**Definition** sd\_spec.h:159

[SD\_SPI\_R1ADDRESS\_ERR](sd__spec_8h.md#aaf06bb2dcb6e359e08bae37d2f36bbc3ae50961a0eb0f59776a156facf51e4620)

@ SD\_SPI\_R1ADDRESS\_ERR

**Definition** sd\_spec.h:157

[sd\_spec\_version](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301a)

sd\_spec\_version

SD specification version.

**Definition** sd\_spec.h:765

[SD\_SPEC\_VER2\_0](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa3525ee751a482ae1cd816e2674ac3160)

@ SD\_SPEC\_VER2\_0

SD card version 2.00.

**Definition** sd\_spec.h:771

[SD\_SPEC\_VER1\_0](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa39605b86ccfad6196721ddfbb84b33d6)

@ SD\_SPEC\_VER1\_0

SD card version 1.0-1.01.

**Definition** sd\_spec.h:767

[SD\_SPEC\_VER3\_0](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aa9e3d0d084a7d8ad1b9d08e6b699084e6)

@ SD\_SPEC\_VER3\_0

SD card version 3.0.

**Definition** sd\_spec.h:773

[SD\_SPEC\_VER1\_1](sd__spec_8h.md#abf77ec1ad65cc9c99dc930ed7a96301aac09ddfacee85353e243d6a8cfe7eeba8)

@ SD\_SPEC\_VER1\_1

SD card version 1.10.

**Definition** sd\_spec.h:769

[sdio\_cccr\_flags](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65)

sdio\_cccr\_flags

Card common control register flags.

**Definition** sd\_spec.h:903

[SDIO\_SUPPORT\_MULTIBLOCK](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a364c7067e73960bae74ed80320adb223)

@ SDIO\_SUPPORT\_MULTIBLOCK

**Definition** sd\_spec.h:909

[SDIO\_SUPPORT\_4BIT\_LS\_BUS](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a6cd553669599181b3677cea94687f025)

@ SDIO\_SUPPORT\_4BIT\_LS\_BUS

**Definition** sd\_spec.h:908

[SDIO\_SUPPORT\_DDR50](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a6d2084ba4c729c2cb019582b975f652f)

@ SDIO\_SUPPORT\_DDR50

**Definition** sd\_spec.h:907

[SDIO\_SUPPORT\_SDR104](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65a9b12d90cd1590f68fc1031449c4560ec)

@ SDIO\_SUPPORT\_SDR104

**Definition** sd\_spec.h:906

[SDIO\_SUPPORT\_HS](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65aa23a07a4fe6f6dd8292215221d97d5e2)

@ SDIO\_SUPPORT\_HS

**Definition** sd\_spec.h:904

[SDIO\_SUPPORT\_SDR50](sd__spec_8h.md#ac12657ae7d3b8abc562d4d7929a86b65acc46ce7f993b3eb81c6a2a2daad84c34)

@ SDIO\_SUPPORT\_SDR50

**Definition** sd\_spec.h:905

[mmc\_ext\_csd\_rev](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81)

mmc\_ext\_csd\_rev

CSD Revision.

**Definition** sd\_spec.h:654

[MMC\_4\_3](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a0f4fc7047a7c813b9ada618ed05e09a4)

@ MMC\_4\_3

**Definition** sd\_spec.h:659

[MMC\_4\_4](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a43b7acda3747eb2233c2f2a433ff71c7)

@ MMC\_4\_4

**Definition** sd\_spec.h:658

[MMC\_5\_0](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a87a4c0efb7e10cccce939af5f60343ad)

@ MMC\_5\_0

**Definition** sd\_spec.h:656

[MMC\_4\_2](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81a9a960567b8ecbd6feff7e6337fc98567)

@ MMC\_4\_2

**Definition** sd\_spec.h:660

[MMC\_4\_5](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81aa0d4721b24d0cd71d6a8fbfc666a6e7c)

@ MMC\_4\_5

**Definition** sd\_spec.h:657

[MMC\_4\_1](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81ab84ae4edfcca8ccae2a0df0643d04ca2)

@ MMC\_4\_1

**Definition** sd\_spec.h:661

[MMC\_4\_0](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81aba4f3f30eaa7d3368743f78f3c355269)

@ MMC\_4\_0

**Definition** sd\_spec.h:662

[MMC\_5\_1](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81ad49da8223b68d35a4d95d6b48bb8a3f7)

@ MMC\_5\_1

**Definition** sd\_spec.h:655

[sd\_r1\_status](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155a)

sd\_r1\_status

Native SD mode R1 response status flags.

**Definition** sd\_spec.h:86

[SD\_R1\_CARD\_LOCKED](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa02d458f5c51dfb7554e17bad1acb591a)

@ SD\_R1\_CARD\_LOCKED

**Definition** sd\_spec.h:106

[SD\_R1\_CUR\_STATE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa0815a9749fc47ea398752e886e222b65)

@ SD\_R1\_CUR\_STATE

**Definition** sd\_spec.h:94

[SD\_R1\_CSD\_OVERWRITE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa0b9e2ded1a4aa629d698f3ba5584bcc2)

@ SD\_R1\_CSD\_OVERWRITE

**Definition** sd\_spec.h:98

[SD\_R1\_ERASE\_SKIP](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa1388a4a737946b04de90dcec9c719837)

@ SD\_R1\_ERASE\_SKIP

**Definition** sd\_spec.h:97

[SD\_R1\_ADDR\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa153195025c02879f23af882b6a4d7af4)

@ SD\_R1\_ADDR\_ERR

**Definition** sd\_spec.h:111

[SD\_R1\_WP\_VIOLATION](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa3ac808a14aa22446db1101fe5f2cbfab)

@ SD\_R1\_WP\_VIOLATION

**Definition** sd\_spec.h:107

[SD\_R1\_ERASE\_RESET](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa3c9f8c1239694b9bda4aca0d7f40a929)

@ SD\_R1\_ERASE\_RESET

**Definition** sd\_spec.h:95

[SD\_R1\_ERASE\_PARAM](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa4ad410b3a28df509ab875d26ae431e21)

@ SD\_R1\_ERASE\_PARAM

**Definition** sd\_spec.h:108

[SD\_R1\_ECC\_DISABLED](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa4cf46d638fd781b73edd03b61dd5d1a2)

@ SD\_R1\_ECC\_DISABLED

**Definition** sd\_spec.h:96

[SD\_R1\_UNLOCK\_FAIL](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa51199d1fa7c1cda33fde647843394d65)

@ SD\_R1\_UNLOCK\_FAIL

**Definition** sd\_spec.h:105

[SD\_R1\_ILLEGAL\_CMD](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa6e3c05c3b4a44c9ec63f89554850abbc)

@ SD\_R1\_ILLEGAL\_CMD

**Definition** sd\_spec.h:103

[SD\_R1\_APP\_CMD](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa72c5d7592912c25f0440fa38664dfc13)

@ SD\_R1\_APP\_CMD

**Definition** sd\_spec.h:90

[SD\_R1\_ERASE\_SEQ\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aa94c0a61d8f8aeb5ed7a13846eb81dfae)

@ SD\_R1\_ERASE\_SEQ\_ERR

**Definition** sd\_spec.h:109

[SD\_R1\_AUTH\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aaa33240a72b4aeff90e48d8dd3b9419c5)

@ SD\_R1\_AUTH\_ERR

**Definition** sd\_spec.h:88

[SD\_R1\_CC\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aaac890f2e8917f249f729e273f4180c8d)

@ SD\_R1\_CC\_ERR

**Definition** sd\_spec.h:101

[SD\_R1\_ERR\_FLAGS](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab6413ec799d46c7341e48f0b5146f400)

@ SD\_R1\_ERR\_FLAGS

**Definition** sd\_spec.h:113

[SD\_R1\_FX\_EVENT](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab852db2cfe8d7581e1ad7a1c2aee5406)

@ SD\_R1\_FX\_EVENT

**Definition** sd\_spec.h:91

[SD\_R1ERR\_NONE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aab8635ae93d3d927f662e88c9e55305eb)

@ SD\_R1ERR\_NONE

**Definition** sd\_spec.h:128

[SD\_R1\_BLOCK\_LEN\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aabb622edfda732a5fd3fec2b042951254)

@ SD\_R1\_BLOCK\_LEN\_ERR

**Definition** sd\_spec.h:110

[SD\_R1\_CRC\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac5fb430e08cbab9b2cbf2015202641e2)

@ SD\_R1\_CRC\_ERR

**Definition** sd\_spec.h:104

[SD\_R1\_ERR](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac6c818a2d7443a820c3f027e2d799ad2)

@ SD\_R1\_ERR

**Definition** sd\_spec.h:100

[SD\_R1\_OUT\_OF\_RANGE](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac7cb6855c33427bdf0a4e7d344281aaf)

@ SD\_R1\_OUT\_OF\_RANGE

**Definition** sd\_spec.h:112

[SD\_R1\_RDY\_DATA](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aac99e88e470b5ecb04885b0289a96a2c8)

@ SD\_R1\_RDY\_DATA

**Definition** sd\_spec.h:93

[SD\_R1\_ECC\_FAIL](sd__spec_8h.md#ad38162e32b87d3c01f1ae46d3423155aafe9dd6c272ec4d1c04efdfa4d7e12870)

@ SD\_R1\_ECC\_FAIL

**Definition** sd\_spec.h:102

[mmc\_timing\_mode](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345)

mmc\_timing\_mode

MMC Timing Modes.

**Definition** sd\_spec.h:612

[MMC\_HS\_TIMING](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a17160707005c580fbd52dbd6b99699dd)

@ MMC\_HS\_TIMING

**Definition** sd\_spec.h:614

[MMC\_HS200\_TIMING](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a39200c50c7e22c096db3ce1dd3fe78d5)

@ MMC\_HS200\_TIMING

**Definition** sd\_spec.h:615

[MMC\_HS400\_TIMING](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345a4ea17060afbcd026387172c1af57bb43)

@ MMC\_HS400\_TIMING

**Definition** sd\_spec.h:616

[MMC\_LEGACY\_TIMING](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345ae51a5474387816c03970aa0f8058b002)

@ MMC\_LEGACY\_TIMING

**Definition** sd\_spec.h:613

[sd\_timing\_mode](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930)

sd\_timing\_mode

SD timing mode function selection values.

**Definition** sd\_spec.h:408

[SD\_TIMING\_SDR25](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a433d8a39f77a612dd8104ca49c71a76f)

@ SD\_TIMING\_SDR25

SDR25 mode.

**Definition** sd\_spec.h:416

[SD\_TIMING\_SDR50](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a787fb937df1275cb3d169e1dade2fb37)

@ SD\_TIMING\_SDR50

SDR50 mode.

**Definition** sd\_spec.h:418

[SD\_TIMING\_HIGH\_SPEED](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a7b6cef084cb3b83a91c05964951b05a6)

@ SD\_TIMING\_HIGH\_SPEED

High speed mode.

**Definition** sd\_spec.h:414

[SD\_TIMING\_DDR50](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930a88f373b6ac9335667eb8adab49a04e10)

@ SD\_TIMING\_DDR50

DDR50 mode.

**Definition** sd\_spec.h:422

[SD\_TIMING\_DEFAULT](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aa858c50e3f53d635857084ab5801a204)

@ SD\_TIMING\_DEFAULT

Default Mode.

**Definition** sd\_spec.h:410

[SD\_TIMING\_SDR104](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aad980a4d433ffcf189a2e77b5d765861)

@ SD\_TIMING\_SDR104

SDR104 mode.

**Definition** sd\_spec.h:420

[SD\_TIMING\_SDR12](sd__spec_8h.md#ae82da8038d71cf36ce2237504b498930aea7ebe2a07e1ed7727262d522815355b)

@ SD\_TIMING\_SDR12

SDR12 mode.

**Definition** sd\_spec.h:412

[mmc\_driver\_strengths](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09d)

mmc\_driver\_strengths

MMC Driver Strengths.

**Definition** sd\_spec.h:624

[mmc\_driv\_type1](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09da2cedd0b40bf81afb35792150b2d4964a)

@ mmc\_driv\_type1

**Definition** sd\_spec.h:626

[mmc\_driv\_type0](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dabd4f3ffac3f52efe797ce3ee3c31a03f)

@ mmc\_driv\_type0

**Definition** sd\_spec.h:625

[mmc\_driv\_type3](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dacf4d28d56a6c4925944ffc99072d46e9)

@ mmc\_driv\_type3

**Definition** sd\_spec.h:628

[mmc\_driv\_type4](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09daf5448a25c8b5a8411f059469112ef2be)

@ mmc\_driv\_type4

**Definition** sd\_spec.h:629

[mmc\_driv\_type2](sd__spec_8h.md#af9783799f316cbaed12e18ce9944b09dafed77d2aed13d59fa6645cb06fc21c43)

@ mmc\_driv\_type2

**Definition** sd\_spec.h:627

[sd\_support\_flag](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749a)

sd\_support\_flag

SD support flags.

**Definition** sd\_spec.h:241

[SD\_SPEED\_CLASS\_CONTROL\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa02b4afca69adad8d7f220b8e4a76db45)

@ SD\_SPEED\_CLASS\_CONTROL\_FLAG

**Definition** sd\_spec.h:249

[SD\_SDXC\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa0558ef06a64c10456d220e66a5bc0f8b)

@ SD\_SDXC\_FLAG

**Definition** sd\_spec.h:245

[SD\_HIGH\_CAPACITY\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa104798e5266441d5a2f356f50b01cb35)

@ SD\_HIGH\_CAPACITY\_FLAG

**Definition** sd\_spec.h:242

[SD\_4BITS\_WIDTH](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa2511277c6c4ebe38bc7179312292710b)

@ SD\_4BITS\_WIDTH

**Definition** sd\_spec.h:243

[SD\_3000MV\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa5458d4988d7076d854bd695307771858)

@ SD\_3000MV\_FLAG

**Definition** sd\_spec.h:247

[SD\_MEM\_PRESENT\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aa923c57b4134ad360ed3f6abbabfa87f1)

@ SD\_MEM\_PRESENT\_FLAG

**Definition** sd\_spec.h:250

[SD\_1800MV\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aab78269976cbb673b4e00d6059ec38f80)

@ SD\_1800MV\_FLAG

**Definition** sd\_spec.h:246

[SD\_CMD23\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aac1f502da56d7d50b70898329da1ad21a)

@ SD\_CMD23\_FLAG

**Definition** sd\_spec.h:248

[SD\_SDHC\_FLAG](sd__spec_8h.md#afeec7c838fcf2d5c01cf653e305c749aad9777c04b150a28916f894f54417286c)

@ SD\_SDHC\_FLAG

**Definition** sd\_spec.h:244

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[mmc\_device\_type](structmmc__device__type.md)

MMC Device Type.

**Definition** sd\_spec.h:638

[mmc\_device\_type::MMC\_HS\_26\_DV](structmmc__device__type.md#a12bb36ef4914b9182f08c4310c85d70d)

bool MMC\_HS\_26\_DV

**Definition** sd\_spec.h:646

[mmc\_device\_type::MMC\_HS400\_DDR\_1800MV](structmmc__device__type.md#a24bee6ea4bd6d209b53b05fb9e040b38)

bool MMC\_HS400\_DDR\_1800MV

**Definition** sd\_spec.h:640

[mmc\_device\_type::MMC\_HS\_52\_DV](structmmc__device__type.md#a3f4bbe853ef59313a84acb5737cafdf4)

bool MMC\_HS\_52\_DV

**Definition** sd\_spec.h:645

[mmc\_device\_type::MMC\_HS\_DDR\_1800MV](structmmc__device__type.md#a5d338770aca6d893e094f57211b0339e)

bool MMC\_HS\_DDR\_1800MV

**Definition** sd\_spec.h:644

[mmc\_device\_type::MMC\_HS\_DDR\_1200MV](structmmc__device__type.md#a65bc5ecdb11da48c08a06d4c5c386590)

bool MMC\_HS\_DDR\_1200MV

**Definition** sd\_spec.h:643

[mmc\_device\_type::MMC\_HS200\_SDR\_1800MV](structmmc__device__type.md#a7027fdec8b21be17a2ba97b2b19a13da)

bool MMC\_HS200\_SDR\_1800MV

**Definition** sd\_spec.h:642

[mmc\_device\_type::MMC\_HS200\_SDR\_1200MV](structmmc__device__type.md#aaa7bb99717ecde9e6cf265a6c5bb33f0)

bool MMC\_HS200\_SDR\_1200MV

**Definition** sd\_spec.h:641

[mmc\_device\_type::MMC\_HS400\_DDR\_1200MV](structmmc__device__type.md#ab19f29678c18ba8740758ca136fd7744)

bool MMC\_HS400\_DDR\_1200MV

**Definition** sd\_spec.h:639

[mmc\_ext\_csd](structmmc__ext__csd.md)

MMC extended card specific data register.

**Definition** sd\_spec.h:671

[mmc\_ext\_csd::hs\_timing](structmmc__ext__csd.md#a25fe8f962635be3d40b449203e7d34a2)

enum mmc\_timing\_mode hs\_timing

High Speed Timing Mode [185].

**Definition** sd\_spec.h:677

[mmc\_ext\_csd::power\_class](structmmc__ext__csd.md#a286b2783ac15dbec6fa3953f0cd69af4)

uint8\_t power\_class

Selected power class [187].

**Definition** sd\_spec.h:683

[mmc\_ext\_csd::mmc\_driver\_strengths](structmmc__ext__csd.md#a29a7f7502e6e6d93e76392b8ac45356f)

uint8\_t mmc\_driver\_strengths

Driver strengths [197].

**Definition** sd\_spec.h:685

[mmc\_ext\_csd::pwr\_class\_HS400](structmmc__ext__csd.md#a3a38f805cac18f3429f57edc7cbf2134)

uint8\_t pwr\_class\_HS400

Power class information for HS400 [253].

**Definition** sd\_spec.h:689

[mmc\_ext\_csd::cache\_size](structmmc__ext__csd.md#a3aafc3e2b5b59cb79535411178a35efe)

uint32\_t cache\_size

Size of eMMC cache [252:249].

**Definition** sd\_spec.h:691

[mmc\_ext\_csd::rev](structmmc__ext__csd.md#a3ee512cb3c0e3698d940c04eed3aa665)

enum mmc\_ext\_csd\_rev rev

Extended CSD Revision [192].

**Definition** sd\_spec.h:681

[mmc\_ext\_csd::sec\_count](structmmc__ext__csd.md#a44aa7d6d1282a00a1875e92fb5b3c4b8)

uint32\_t sec\_count

Sector Count [215:212].

**Definition** sd\_spec.h:673

[mmc\_ext\_csd::device\_type](structmmc__ext__csd.md#a4c26010052a69e060742e0a05b6ad98b)

struct mmc\_device\_type device\_type

Device Type [196].

**Definition** sd\_spec.h:679

[mmc\_ext\_csd::bus\_width](structmmc__ext__csd.md#a63545477058cce0c5727637bcbb06a47)

uint8\_t bus\_width

Bus Width Mode [183].

**Definition** sd\_spec.h:675

[mmc\_ext\_csd::pwr\_class\_200MHZ\_VCCQ195](structmmc__ext__csd.md#acab002b3a28a3dc9bf58187e9e19a9fe)

uint8\_t pwr\_class\_200MHZ\_VCCQ195

Power class information for HS200 at VCC!=1.95V [237].

**Definition** sd\_spec.h:687

[sd\_cid](structsd__cid.md)

SD card identification register.

**Definition** sd\_spec.h:521

[sd\_cid::application](structsd__cid.md#a11ec5fa23ae13ee084c093b27c1d381a)

uint16\_t application

OEM/Application ID [119:104].

**Definition** sd\_spec.h:525

[sd\_cid::name](structsd__cid.md#a46f36abc3c2b1f3e9aa34c199d2bfcf3)

uint8\_t name[5]

Product name [103:64].

**Definition** sd\_spec.h:527

[sd\_cid::date](structsd__cid.md#a50fbbc6844a1fde29a25a803ed9d0df7)

uint16\_t date

Manufacturing date [19:8].

**Definition** sd\_spec.h:533

[sd\_cid::manufacturer](structsd__cid.md#a7d97bc0f58c766abd2501d923e163d40)

uint8\_t manufacturer

Manufacturer ID [127:120].

**Definition** sd\_spec.h:523

[sd\_cid::version](structsd__cid.md#aba79f6a5bdf963772ac3c77ac209faf2)

uint8\_t version

Product revision [63:56].

**Definition** sd\_spec.h:529

[sd\_cid::ser\_num](structsd__cid.md#ace04f0f28cb7e058e69fbbc643f66052)

uint32\_t ser\_num

Product serial number [55:24].

**Definition** sd\_spec.h:531

[sd\_csd](structsd__csd.md)

SD card specific data register.

**Definition** sd\_spec.h:541

[sd\_csd::write\_prtect\_size](structsd__csd.md#a029a893cdcd3765864c70476eb6dd64e)

uint8\_t write\_prtect\_size

Write protect group size [38:32].

**Definition** sd\_spec.h:571

[sd\_csd::read\_blk\_len](structsd__csd.md#a06f6aef4f4745a78bcf769df5415daa6)

uint8\_t read\_blk\_len

Maximum read data block length [83:80].

**Definition** sd\_spec.h:553

[sd\_csd::write\_current\_min](structsd__csd.md#a0d1efea12c467eacd0d0f98a0bb0ac91)

uint8\_t write\_current\_min

Maximum write current at VDD min [55:53].

**Definition** sd\_spec.h:563

[sd\_csd::csd\_structure](structsd__csd.md#a37b15b70967c9317183b3e5e7837b228)

uint8\_t csd\_structure

CSD structure [127:126].

**Definition** sd\_spec.h:543

[sd\_csd::write\_current\_max](structsd__csd.md#a53b364ce0db06b9217259afeb625da44)

uint8\_t write\_current\_max

Maximum write current at VDD max [52:50].

**Definition** sd\_spec.h:565

[sd\_csd::read\_time1](structsd__csd.md#a583c715045b5934ad94ab9cf61b25b06)

uint8\_t read\_time1

Data read access-time-1 [119:112].

**Definition** sd\_spec.h:545

[sd\_csd::cmd\_class](structsd__csd.md#a8bfd2c42066d85058d01076fcaa7a32d)

uint16\_t cmd\_class

Card command classes [95:84].

**Definition** sd\_spec.h:551

[sd\_csd::read\_time2](structsd__csd.md#a96bc4672222dece77d29ffc9287c59ac)

uint8\_t read\_time2

Data read access-time-2 in clock cycles (NSAC\*100) [111:104].

**Definition** sd\_spec.h:547

[sd\_csd::write\_speed\_factor](structsd__csd.md#a9c362eff38daf7d00776416ed064de24)

uint8\_t write\_speed\_factor

Write speed factor [28:26].

**Definition** sd\_spec.h:573

[sd\_csd::dev\_size\_mul](structsd__csd.md#a9d5a952bc6c2a6967e9a88cd93f19e89)

uint8\_t dev\_size\_mul

Device size multiplier [49:47].

**Definition** sd\_spec.h:567

[sd\_csd::read\_current\_min](structsd__csd.md#aa868cfc1db75eb2913d21bffeaf29fd9)

uint8\_t read\_current\_min

Maximum read current at VDD min [61:59].

**Definition** sd\_spec.h:559

[sd\_csd::erase\_size](structsd__csd.md#ab8d5ae38b19f7ea83b0856ad093c65cb)

uint8\_t erase\_size

Erase sector size [45:39].

**Definition** sd\_spec.h:569

[sd\_csd::read\_current\_max](structsd__csd.md#ad2f31731d7ec0b101d911fe20b5d94db)

uint8\_t read\_current\_max

Maximum read current at VDD max [58:56].

**Definition** sd\_spec.h:561

[sd\_csd::device\_size](structsd__csd.md#ad35b07abba80e9929c5eed40e37d25b3)

uint32\_t device\_size

Device size [73:62].

**Definition** sd\_spec.h:557

[sd\_csd::write\_blk\_len](structsd__csd.md#adff7d405662589ec44f4d0a6b3548760)

uint8\_t write\_blk\_len

Maximum write data block length [25:22].

**Definition** sd\_spec.h:575

[sd\_csd::flags](structsd__csd.md#ae10b32787aeedd4789d657eb1ef492eb)

uint16\_t flags

Flags in \_sd\_csd\_flag.

**Definition** sd\_spec.h:555

[sd\_csd::xfer\_rate](structsd__csd.md#ae39272173a5253d0d11ef04a2e129db6)

uint8\_t xfer\_rate

Maximum data transfer rate [103:96].

**Definition** sd\_spec.h:549

[sd\_csd::file\_fmt](structsd__csd.md#af93239157610a6eeea420c29432d5412)

uint8\_t file\_fmt

File format [11:10].

**Definition** sd\_spec.h:577

[sd\_scr](structsd__scr.md)

SD card configuration register.

**Definition** sd\_spec.h:729

[sd\_scr::sd\_ext\_sec](structsd__scr.md#a15f60bc2115b943ce938f3a96dd8e547)

uint8\_t sd\_ext\_sec

Extended security support [46:43].

**Definition** sd\_spec.h:741

[sd\_scr::scr\_structure](structsd__scr.md#a3fc37c731dfb5c5596b6389152479c07)

uint8\_t scr\_structure

SCR Structure [63:60].

**Definition** sd\_spec.h:731

[sd\_scr::sd\_width](structsd__scr.md#a40d30ccc4daf2c32f2ac162b402f3887)

uint8\_t sd\_width

Data bus widths supported [51:48].

**Definition** sd\_spec.h:739

[sd\_scr::cmd\_support](structsd__scr.md#a9016ca73a668499289c52355ebb83cb1)

uint8\_t cmd\_support

Command support bits [33:32] 33-support CMD23, 32-support cmd20.

**Definition** sd\_spec.h:743

[sd\_scr::sd\_sec](structsd__scr.md#a9f8254b5fe6911156bae727e29262f5a)

uint8\_t sd\_sec

Security specification supported [54:52].

**Definition** sd\_spec.h:737

[sd\_scr::rsvd](structsd__scr.md#aba20efcf752335f1a86d0a86607d92d0)

uint32\_t rsvd

reserved for manufacturer usage [31:0]

**Definition** sd\_spec.h:745

[sd\_scr::flags](structsd__scr.md#abda65da85e20979a1fc71f2aea1f947b)

uint16\_t flags

SCR flags in \_sd\_scr\_flag.

**Definition** sd\_spec.h:735

[sd\_scr::sd\_spec](structsd__scr.md#ae6201af1083efa828cced000874bf197)

uint8\_t sd\_spec

SD memory card specification version [59:56].

**Definition** sd\_spec.h:733

[sd\_switch\_caps](structsd__switch__caps.md)

SD switch capabilities.

**Definition** sd\_spec.h:505

[sd\_switch\_caps::bus\_speed](structsd__switch__caps.md#a29024de744d65fb3d8fe51c4d4424aee)

enum sd\_bus\_speed bus\_speed

**Definition** sd\_spec.h:508

[sd\_switch\_caps::sd\_current\_limit](structsd__switch__caps.md#a4b531af598bea14c90b8973daf1422dc)

enum sd\_current\_limit sd\_current\_limit

**Definition** sd\_spec.h:510

[sd\_switch\_caps::sd\_drv\_type](structsd__switch__caps.md#a7262e4be5e3f59d047e569e1c24f04b3)

enum sd\_driver\_type sd\_drv\_type

**Definition** sd\_spec.h:509

[sd\_switch\_caps::hs\_max\_dtr](structsd__switch__caps.md#a7465b3fe6bd1f317eeb3283a25da7278)

enum hs\_max\_data\_rate hs\_max\_dtr

**Definition** sd\_spec.h:506

[sd\_switch\_caps::uhs\_max\_dtr](structsd__switch__caps.md#ab09d80f61bc79857ee39604959c8a578)

enum uhs\_max\_data\_rate uhs\_max\_dtr

**Definition** sd\_spec.h:507

[sdio\_cis](structsdio__cis.md)

SDIO common CIS tuple properties.

**Definition** sd\_spec.h:918

[sdio\_cis::manf\_id](structsdio__cis.md#a04c8a774c65f683185e5a32e15afb67c)

uint16\_t manf\_id

manufacturer ID

**Definition** sd\_spec.h:920

[sdio\_cis::max\_blk\_size](structsdio__cis.md#a1b340e20630994f91314be17dd9055ca)

uint16\_t max\_blk\_size

Max transfer block size.

**Definition** sd\_spec.h:925

[sdio\_cis::max\_speed](structsdio__cis.md#a56d3ee1d6b8d0d87e0efdbda15b7076d)

uint8\_t max\_speed

Max transfer speed.

**Definition** sd\_spec.h:926

[sdio\_cis::rdy\_timeout](structsdio__cis.md#a86a01890f31788ae5465b1c8dc47bcf2)

uint16\_t rdy\_timeout

I/O ready timeout.

**Definition** sd\_spec.h:927

[sdio\_cis::func\_id](structsdio__cis.md#ad38be5cade97ac92de62094d8e3b8549)

uint8\_t func\_id

sdio device class function id

**Definition** sd\_spec.h:923

[sdio\_cis::manf\_code](structsdio__cis.md#ad52e1df89176f728734ce0e69fb2b4c8)

uint16\_t manf\_code

manufacturer code

**Definition** sd\_spec.h:921

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sd](dir_ff091b3f4b9505cc58dad89321d1c232.md)
- [sd\_spec.h](sd__spec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
