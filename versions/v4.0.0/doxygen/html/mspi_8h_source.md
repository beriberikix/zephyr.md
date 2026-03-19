---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mspi_8h_source.html
original_path: doxygen/html/mspi_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi.h

[Go to the documentation of this file.](mspi_8h.md)

1/\*

2 \* Copyright (c) 2024, Ambiq Micro Inc. <www.ambiq.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_MSPI\_H\_

15#define ZEPHYR\_INCLUDE\_MSPI\_H\_

16

17#include <[errno.h](errno_8h.md)>

18

19#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

20#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

21#include <[zephyr/kernel.h](kernel_8h.md)>

22#include <[zephyr/device.h](device_8h.md)>

23#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

35

[ 39](group__mspi__interface.md#ga3f211cd81e05cb9ee073a2722f6b22d8)enum [mspi\_op\_mode](group__mspi__interface.md#ga3f211cd81e05cb9ee073a2722f6b22d8) {

[ 40](group__mspi__interface.md#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a) [MSPI\_OP\_MODE\_CONTROLLER](group__mspi__interface.md#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a) = 0,

[ 41](group__mspi__interface.md#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83) [MSPI\_OP\_MODE\_PERIPHERAL](group__mspi__interface.md#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83) = 1,

42};

43

[ 47](group__mspi__interface.md#ga20e348d7a9f1f9b32078a3bf6c4e82b9)enum [mspi\_duplex](group__mspi__interface.md#ga20e348d7a9f1f9b32078a3bf6c4e82b9) {

[ 48](group__mspi__interface.md#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3) [MSPI\_HALF\_DUPLEX](group__mspi__interface.md#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3) = 0,

[ 49](group__mspi__interface.md#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c) [MSPI\_FULL\_DUPLEX](group__mspi__interface.md#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c) = 1,

50};

51

[ 58](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5)enum [mspi\_io\_mode](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5) {

[ 59](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd) [MSPI\_IO\_MODE\_SINGLE](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd) = 0,

[ 60](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673) [MSPI\_IO\_MODE\_DUAL](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673) = 1,

[ 61](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da) [MSPI\_IO\_MODE\_DUAL\_1\_1\_2](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da) = 2,

[ 62](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663) [MSPI\_IO\_MODE\_DUAL\_1\_2\_2](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663) = 3,

[ 63](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a) [MSPI\_IO\_MODE\_QUAD](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a) = 4,

[ 64](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a) [MSPI\_IO\_MODE\_QUAD\_1\_1\_4](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a) = 5,

[ 65](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a) [MSPI\_IO\_MODE\_QUAD\_1\_4\_4](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a) = 6,

[ 66](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725) [MSPI\_IO\_MODE\_OCTAL](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725) = 7,

[ 67](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf) [MSPI\_IO\_MODE\_OCTAL\_1\_1\_8](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf) = 8,

[ 68](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573) [MSPI\_IO\_MODE\_OCTAL\_1\_8\_8](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573) = 9,

[ 69](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b) [MSPI\_IO\_MODE\_HEX](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b) = 10,

[ 70](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02) [MSPI\_IO\_MODE\_HEX\_8\_8\_16](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02) = 11,

[ 71](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa) [MSPI\_IO\_MODE\_HEX\_8\_16\_16](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa) = 12,

[ 72](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb) [MSPI\_IO\_MODE\_MAX](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb),

73};

74

[ 84](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68)enum [mspi\_data\_rate](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68) {

[ 85](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0) [MSPI\_DATA\_RATE\_SINGLE](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0) = 0,

[ 86](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39) [MSPI\_DATA\_RATE\_S\_S\_D](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39) = 1,

[ 87](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984) [MSPI\_DATA\_RATE\_S\_D\_D](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984) = 2,

[ 88](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc) [MSPI\_DATA\_RATE\_DUAL](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc) = 3,

[ 89](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9) [MSPI\_DATA\_RATE\_MAX](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9),

90};

91

[ 95](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c)enum [mspi\_cpp\_mode](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c) {

[ 96](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90) [MSPI\_CPP\_MODE\_0](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90) = 0,

[ 97](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870) [MSPI\_CPP\_MODE\_1](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870) = 1,

[ 98](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705) [MSPI\_CPP\_MODE\_2](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705) = 2,

[ 99](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48) [MSPI\_CPP\_MODE\_3](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48) = 3,

100};

101

[ 105](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44)enum [mspi\_endian](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44) {

[ 106](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345) [MSPI\_XFER\_LITTLE\_ENDIAN](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345) = 0,

[ 107](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d) [MSPI\_XFER\_BIG\_ENDIAN](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d) = 1,

108};

109

[ 113](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b)enum [mspi\_ce\_polarity](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b) {

[ 114](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae) [MSPI\_CE\_ACTIVE\_LOW](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae) = 0,

[ 115](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22) [MSPI\_CE\_ACTIVE\_HIGH](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22) = 1,

116};

117

[ 123](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5)enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) {

[ 124](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64) [MSPI\_BUS\_RESET](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64) = 0,

[ 125](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0) [MSPI\_BUS\_ERROR](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0) = 1,

[ 126](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61) [MSPI\_BUS\_XFER\_COMPLETE](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61) = 2,

[ 127](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a) [MSPI\_BUS\_EVENT\_MAX](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a),

128};

129

[ 135](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1)enum [mspi\_bus\_event\_cb\_mask](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1) {

[ 136](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277) [MSPI\_BUS\_NO\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277) = 0,

[ 137](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1) [MSPI\_BUS\_RESET\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 138](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498) [MSPI\_BUS\_ERROR\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 139](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7) [MSPI\_BUS\_XFER\_COMPLETE\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

140};

141

[ 145](group__mspi__interface.md#ga116259bbb1d12a10c2ba9e6051f2f000)enum [mspi\_xfer\_mode](group__mspi__interface.md#ga116259bbb1d12a10c2ba9e6051f2f000) {

[ 146](group__mspi__interface.md#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1) [MSPI\_PIO](group__mspi__interface.md#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1),

[ 147](group__mspi__interface.md#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8) [MSPI\_DMA](group__mspi__interface.md#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8),

148};

149

[ 153](group__mspi__interface.md#ga498f10591acf5dc7ec88e0aa98e537d6)enum [mspi\_xfer\_direction](group__mspi__interface.md#ga498f10591acf5dc7ec88e0aa98e537d6) {

[ 154](group__mspi__interface.md#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541) [MSPI\_RX](group__mspi__interface.md#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541),

[ 155](group__mspi__interface.md#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a) [MSPI\_TX](group__mspi__interface.md#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a),

156};

157

[ 161](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647)enum [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) {

[ 162](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878) [MSPI\_DEVICE\_CONFIG\_NONE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878) = 0,

[ 163](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2) [MSPI\_DEVICE\_CONFIG\_CE\_NUM](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 164](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809) [MSPI\_DEVICE\_CONFIG\_FREQUENCY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 165](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f) [MSPI\_DEVICE\_CONFIG\_IO\_MODE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 166](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9) [MSPI\_DEVICE\_CONFIG\_DATA\_RATE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 167](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65) [MSPI\_DEVICE\_CONFIG\_CPP](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 168](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca) [MSPI\_DEVICE\_CONFIG\_ENDIAN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 169](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b) [MSPI\_DEVICE\_CONFIG\_CE\_POL](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 170](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537) [MSPI\_DEVICE\_CONFIG\_DQS](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 171](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a) [MSPI\_DEVICE\_CONFIG\_RX\_DUMMY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 172](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5) [MSPI\_DEVICE\_CONFIG\_TX\_DUMMY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 173](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872) [MSPI\_DEVICE\_CONFIG\_READ\_CMD](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 174](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b) [MSPI\_DEVICE\_CONFIG\_WRITE\_CMD](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

[ 175](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac) [MSPI\_DEVICE\_CONFIG\_CMD\_LEN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

[ 176](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b) [MSPI\_DEVICE\_CONFIG\_ADDR\_LEN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

[ 177](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946) [MSPI\_DEVICE\_CONFIG\_MEM\_BOUND](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

[ 178](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120) [MSPI\_DEVICE\_CONFIG\_BREAK\_TIME](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

[ 179](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489) [MSPI\_DEVICE\_CONFIG\_ALL](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489) = [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(16),

180};

181

[ 185](group__mspi__interface.md#ga006a1e32778a02299b3500886bb194fa)enum [mspi\_xip\_permit](group__mspi__interface.md#ga006a1e32778a02299b3500886bb194fa) {

[ 186](group__mspi__interface.md#gga006a1e32778a02299b3500886bb194faa431525f8be52537b0a831f522726c7b9) [MSPI\_XIP\_READ\_WRITE](group__mspi__interface.md#gga006a1e32778a02299b3500886bb194faa431525f8be52537b0a831f522726c7b9) = 0,

[ 187](group__mspi__interface.md#gga006a1e32778a02299b3500886bb194faae9b2d08d8ae1722c3014a706fc801731) [MSPI\_XIP\_READ\_ONLY](group__mspi__interface.md#gga006a1e32778a02299b3500886bb194faae9b2d08d8ae1722c3014a706fc801731) = 1,

188};

189

195

[ 199](group__mspi__configure__api.md#gaa25a7f97ab3437d4544832a0e7474f4a)enum [mspi\_timing\_param](group__mspi__configure__api.md#gaa25a7f97ab3437d4544832a0e7474f4a) {

[ 200](group__mspi__configure__api.md#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237) [MSPI\_TIMING\_PARAM\_DUMMY](group__mspi__configure__api.md#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237)

201};

202

[ 206](structmspi__timing__cfg.md)struct [mspi\_timing\_cfg](structmspi__timing__cfg.md) {

207#ifdef \_\_cplusplus

208 /\* For C++ compatibility. \*/

209 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dummy;

210#endif

211};

212

[ 218](structmspi__dev__id.md)struct [mspi\_dev\_id](structmspi__dev__id.md) {

[ 220](structmspi__dev__id.md#ac79d41731c8599f23b666f78cdb58bf0) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [ce](structmspi__dev__id.md#ac79d41731c8599f23b666f78cdb58bf0);

[ 222](structmspi__dev__id.md#aab54e4f449d4cfb87c5c6f0ccd1d7bfb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dev\_idx](structmspi__dev__id.md#aab54e4f449d4cfb87c5c6f0ccd1d7bfb);

223};

224

[ 228](structmspi__cfg.md)struct [mspi\_cfg](structmspi__cfg.md) {

[ 230](structmspi__cfg.md#af54bbbfbe07d88325117131fefe265ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel\_num](structmspi__cfg.md#af54bbbfbe07d88325117131fefe265ef);

[ 232](structmspi__cfg.md#ab33e45d7802cf777a595d87058e8bfb5) enum [mspi\_op\_mode](group__mspi__interface.md#ga3f211cd81e05cb9ee073a2722f6b22d8) [op\_mode](structmspi__cfg.md#ab33e45d7802cf777a595d87058e8bfb5);

[ 234](structmspi__cfg.md#a449894e0e58f96b775b4cc1c1eb83e77) enum [mspi\_duplex](group__mspi__interface.md#ga20e348d7a9f1f9b32078a3bf6c4e82b9) [duplex](structmspi__cfg.md#a449894e0e58f96b775b4cc1c1eb83e77);

[ 236](structmspi__cfg.md#a2cf6e063074f86973cf03324637d656a) bool [dqs\_support](structmspi__cfg.md#a2cf6e063074f86973cf03324637d656a);

[ 238](structmspi__cfg.md#a1192af56f714a42aa667a40e369b185e) bool [sw\_multi\_periph](structmspi__cfg.md#a1192af56f714a42aa667a40e369b185e);

[ 240](structmspi__cfg.md#a4053a398f6390e45ef6da385756f14bf) struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*[ce\_group](structmspi__cfg.md#a4053a398f6390e45ef6da385756f14bf);

[ 242](structmspi__cfg.md#a20f6e453165b6ac22a42906604a3258a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_ce\_gpios](structmspi__cfg.md#a20f6e453165b6ac22a42906604a3258a);

[ 244](structmspi__cfg.md#a6d24969046f175f158a5dae05e9284b1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_periph](structmspi__cfg.md#a6d24969046f175f158a5dae05e9284b1);

[ 246](structmspi__cfg.md#a9a76198688b4acac9101274a71bfbf9c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_freq](structmspi__cfg.md#a9a76198688b4acac9101274a71bfbf9c);

[ 248](structmspi__cfg.md#afef0fe6991e28a4496e51333963fd3d1) bool [re\_init](structmspi__cfg.md#afef0fe6991e28a4496e51333963fd3d1);

249};

250

[ 254](structmspi__dt__spec.md)struct [mspi\_dt\_spec](structmspi__dt__spec.md) {

[ 256](structmspi__dt__spec.md#ab21ff3d5959b78f5b5cdc7fcf70e8756) const struct [device](structdevice.md) \*[bus](structmspi__dt__spec.md#ab21ff3d5959b78f5b5cdc7fcf70e8756);

[ 258](structmspi__dt__spec.md#aaedbcdc55394032e3af50ec7d2e8f439) struct [mspi\_cfg](structmspi__cfg.md) [config](structmspi__dt__spec.md#aaedbcdc55394032e3af50ec7d2e8f439);

259};

260

[ 264](structmspi__dev__cfg.md)struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) {

[ 266](structmspi__dev__cfg.md#abf8d45f88d0c8e1c4ee52ea238ff4466) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ce\_num](structmspi__dev__cfg.md#abf8d45f88d0c8e1c4ee52ea238ff4466);

[ 268](structmspi__dev__cfg.md#a9490d822b67d7fab123f32f38b0ccef8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [freq](structmspi__dev__cfg.md#a9490d822b67d7fab123f32f38b0ccef8);

[ 270](structmspi__dev__cfg.md#ad0f5c1a4cd3002313087a9b1fe6cf7a1) enum [mspi\_io\_mode](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5) [io\_mode](structmspi__dev__cfg.md#ad0f5c1a4cd3002313087a9b1fe6cf7a1);

[ 272](structmspi__dev__cfg.md#a0da8c2ccf80fdf610fcdd7fae7d159f8) enum [mspi\_data\_rate](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68) [data\_rate](structmspi__dev__cfg.md#a0da8c2ccf80fdf610fcdd7fae7d159f8);

[ 274](structmspi__dev__cfg.md#a2bb78caec28fadcecd787fc8a573a336) enum [mspi\_cpp\_mode](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c) [cpp](structmspi__dev__cfg.md#a2bb78caec28fadcecd787fc8a573a336);

[ 276](structmspi__dev__cfg.md#a28cf9d7887e9f840344e2804c4040bc4) enum [mspi\_endian](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44) [endian](structmspi__dev__cfg.md#a28cf9d7887e9f840344e2804c4040bc4);

[ 278](structmspi__dev__cfg.md#ab6ed7eeb6d4b31530e06f69706b98278) enum [mspi\_ce\_polarity](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b) [ce\_polarity](structmspi__dev__cfg.md#ab6ed7eeb6d4b31530e06f69706b98278);

[ 280](structmspi__dev__cfg.md#affdcd07ac3d3d25b8a8e0882277af39a) bool [dqs\_enable](structmspi__dev__cfg.md#affdcd07ac3d3d25b8a8e0882277af39a);

[ 284](structmspi__dev__cfg.md#aae492d2e5bad4b266779be9f5bb12ee9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_dummy](structmspi__dev__cfg.md#aae492d2e5bad4b266779be9f5bb12ee9);

[ 288](structmspi__dev__cfg.md#a9feb1c35f7e1f5c43489771e13f2af8d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_dummy](structmspi__dev__cfg.md#a9feb1c35f7e1f5c43489771e13f2af8d);

[ 290](structmspi__dev__cfg.md#ac9f47b226289005271a800739707456b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [read\_cmd](structmspi__dev__cfg.md#ac9f47b226289005271a800739707456b);

[ 292](structmspi__dev__cfg.md#acac2a0913bfbfe1f3b5e34ff1b71ff42) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [write\_cmd](structmspi__dev__cfg.md#acac2a0913bfbfe1f3b5e34ff1b71ff42);

[ 294](structmspi__dev__cfg.md#a0b0c9f101656e67d71d191b656738d2d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd\_length](structmspi__dev__cfg.md#a0b0c9f101656e67d71d191b656738d2d);

[ 296](structmspi__dev__cfg.md#a6dbe113d5075b1b22896c7d0c281bd3d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr\_length](structmspi__dev__cfg.md#a6dbe113d5075b1b22896c7d0c281bd3d);

[ 298](structmspi__dev__cfg.md#a3ec3e22e25440ac5eecf0f9b2d79b9e0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mem\_boundary](structmspi__dev__cfg.md#a3ec3e22e25440ac5eecf0f9b2d79b9e0);

[ 300](structmspi__dev__cfg.md#a60eeb1503018fa47cc5618d150f09aa8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [time\_to\_break](structmspi__dev__cfg.md#a60eeb1503018fa47cc5618d150f09aa8);

301};

302

[ 306](structmspi__xip__cfg.md)struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) {

[ 308](structmspi__xip__cfg.md#a2ba9873d13a24b5fa42d28e910368486) bool [enable](structmspi__xip__cfg.md#a2ba9873d13a24b5fa42d28e910368486);

[ 312](structmspi__xip__cfg.md#a58c0c05d4fc58704b8b46677b468247c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [address\_offset](structmspi__xip__cfg.md#a58c0c05d4fc58704b8b46677b468247c);

[ 314](structmspi__xip__cfg.md#ac393537eb1a209e1c1e41bf639782e72) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structmspi__xip__cfg.md#ac393537eb1a209e1c1e41bf639782e72);

[ 316](structmspi__xip__cfg.md#a172af688c9f92af04978559697fe230f) enum [mspi\_xip\_permit](group__mspi__interface.md#ga006a1e32778a02299b3500886bb194fa) [permission](structmspi__xip__cfg.md#a172af688c9f92af04978559697fe230f);

317};

318

[ 322](structmspi__scramble__cfg.md)struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) {

[ 324](structmspi__scramble__cfg.md#a362ce29f7748d28e818e2c809bd4cedd) bool [enable](structmspi__scramble__cfg.md#a362ce29f7748d28e818e2c809bd4cedd);

[ 328](structmspi__scramble__cfg.md#adf56743768432f22f0a5090e1b823a67) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [address\_offset](structmspi__scramble__cfg.md#adf56743768432f22f0a5090e1b823a67);

[ 330](structmspi__scramble__cfg.md#a8d6d5b47b3d777674b974a6c79337b43) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structmspi__scramble__cfg.md#a8d6d5b47b3d777674b974a6c79337b43);

331};

332

334

340

[ 348](structmspi__ce__control.md)struct [mspi\_ce\_control](structmspi__ce__control.md) {

[ 355](structmspi__ce__control.md#a1f1b6f5583abc08c8c7fae95e1a29a7a) struct [gpio\_dt\_spec](structgpio__dt__spec.md) [gpio](structmspi__ce__control.md#a1f1b6f5583abc08c8c7fae95e1a29a7a);

[ 361](structmspi__ce__control.md#abc3e35be0b7b3f5c118b0d16033125ba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [delay](structmspi__ce__control.md#abc3e35be0b7b3f5c118b0d16033125ba);

362};

363

[ 367](structmspi__xfer__packet.md)struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) {

[ 369](structmspi__xfer__packet.md#afb408ea48ff8863c9714d39c4f7c8a2c) enum [mspi\_xfer\_direction](group__mspi__interface.md#ga498f10591acf5dc7ec88e0aa98e537d6) [dir](structmspi__xfer__packet.md#afb408ea48ff8863c9714d39c4f7c8a2c);

[ 371](structmspi__xfer__packet.md#aedc8eadfb3a0737c3984b130ec21d96c) enum [mspi\_bus\_event\_cb\_mask](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1) [cb\_mask](structmspi__xfer__packet.md#aedc8eadfb3a0737c3984b130ec21d96c);

[ 373](structmspi__xfer__packet.md#a2717e86b7fbb01be65a4955a8e26ebc0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](structmspi__xfer__packet.md#a2717e86b7fbb01be65a4955a8e26ebc0);

[ 375](structmspi__xfer__packet.md#a08dae9b6fbda60f06430cb2b842280b9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [address](structmspi__xfer__packet.md#a08dae9b6fbda60f06430cb2b842280b9);

[ 377](structmspi__xfer__packet.md#a050a827d0ee0349cd7a006de20b1db0c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_bytes](structmspi__xfer__packet.md#a050a827d0ee0349cd7a006de20b1db0c);

[ 379](structmspi__xfer__packet.md#a0b7b3d68ff46173378e4076b439e35ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_buf](structmspi__xfer__packet.md#a0b7b3d68ff46173378e4076b439e35ac);

380};

381

[ 387](structmspi__xfer.md)struct [mspi\_xfer](structmspi__xfer.md) {

[ 389](structmspi__xfer.md#abf10b3fed96161447ffb7a8a6dce7649) bool [async](structmspi__xfer.md#abf10b3fed96161447ffb7a8a6dce7649);

[ 391](structmspi__xfer.md#afa30e0fac32c6c3e7a3c9d7e29ccc8cb) enum [mspi\_xfer\_mode](group__mspi__interface.md#ga116259bbb1d12a10c2ba9e6051f2f000) [xfer\_mode](structmspi__xfer.md#afa30e0fac32c6c3e7a3c9d7e29ccc8cb);

[ 393](structmspi__xfer.md#adfe7adf63f83f40d1ab92ed511f4e917) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_dummy](structmspi__xfer.md#adfe7adf63f83f40d1ab92ed511f4e917);

[ 395](structmspi__xfer.md#a98f23415592095749a853f3d850d399f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rx\_dummy](structmspi__xfer.md#a98f23415592095749a853f3d850d399f);

[ 397](structmspi__xfer.md#a387dd891ab994d75561b50a094427d22) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd\_length](structmspi__xfer.md#a387dd891ab994d75561b50a094427d22);

[ 399](structmspi__xfer.md#ace851e368d69b76092f8429d83d963fd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr\_length](structmspi__xfer.md#ace851e368d69b76092f8429d83d963fd);

[ 401](structmspi__xfer.md#a335fd5fb02bc75053902c4d1b294af57) bool [hold\_ce](structmspi__xfer.md#a335fd5fb02bc75053902c4d1b294af57);

[ 403](structmspi__xfer.md#ae2e7a475ac4bcec88f12742642087505) struct [mspi\_ce\_control](structmspi__ce__control.md) [ce\_sw\_ctrl](structmspi__xfer.md#ae2e7a475ac4bcec88f12742642087505);

[ 407](structmspi__xfer.md#a8a829f14523acb252507e291b574363d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [priority](structmspi__xfer.md#a8a829f14523acb252507e291b574363d);

[ 409](structmspi__xfer.md#a49e4102b694ffb5f9afe72c81fb7ca94) const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) \*[packets](structmspi__xfer.md#a49e4102b694ffb5f9afe72c81fb7ca94);

[ 411](structmspi__xfer.md#a4061b26045ef860b8c9a6509ff054bc3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_packet](structmspi__xfer.md#a4061b26045ef860b8c9a6509ff054bc3);

[ 413](structmspi__xfer.md#afd83aa864cf300e9848ef46b7331ca5a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structmspi__xfer.md#afd83aa864cf300e9848ef46b7331ca5a);

414};

415

417

423

[ 427](structmspi__event__data.md)struct [mspi\_event\_data](structmspi__event__data.md) {

[ 429](structmspi__event__data.md#af788dc5374778055d1ee9fddbe2a4d8d) const struct [device](structdevice.md) \*[controller](structmspi__event__data.md#af788dc5374778055d1ee9fddbe2a4d8d);

[ 431](structmspi__event__data.md#ab1138c26f9a6b11b75e1e50fb3e5d8e9) const struct [mspi\_dev\_id](structmspi__dev__id.md) \*[dev\_id](structmspi__event__data.md#ab1138c26f9a6b11b75e1e50fb3e5d8e9);

[ 433](structmspi__event__data.md#a1bb8c4591ced464181927b0c00003205) const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) \*[packet](structmspi__event__data.md#a1bb8c4591ced464181927b0c00003205);

[ 435](structmspi__event__data.md#a4b926cf5abb4f23bb7e1f85fecd323ef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [status](structmspi__event__data.md#a4b926cf5abb4f23bb7e1f85fecd323ef);

[ 437](structmspi__event__data.md#a6e71714475e45a0d758aa49db33ff57e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [packet\_idx](structmspi__event__data.md#a6e71714475e45a0d758aa49db33ff57e);

438};

439

[ 443](structmspi__event.md)struct [mspi\_event](structmspi__event.md) {

[ 445](structmspi__event.md#a65079ed0fcdb2ca607dab070f2ed010b) enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) [evt\_type](structmspi__event.md#a65079ed0fcdb2ca607dab070f2ed010b);

[ 447](structmspi__event.md#aeeb42b82bd219169e6f185ecdcc2129d) struct [mspi\_event\_data](structmspi__event__data.md) [evt\_data](structmspi__event.md#aeeb42b82bd219169e6f185ecdcc2129d);

448};

449

[ 453](structmspi__callback__context.md)struct [mspi\_callback\_context](structmspi__callback__context.md) {

[ 455](structmspi__callback__context.md#a5649bddfac23544522969fc9e500eb0c) struct [mspi\_event](structmspi__event.md) [mspi\_evt](structmspi__callback__context.md#a5649bddfac23544522969fc9e500eb0c);

[ 457](structmspi__callback__context.md#ab2225b77f4d9e0403192c0ab11482e2e) void \*[ctx](structmspi__callback__context.md#ab2225b77f4d9e0403192c0ab11482e2e);

458};

459

[ 467](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4)typedef void (\*[mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4))(struct [mspi\_callback\_context](structmspi__callback__context.md) \*mspi\_cb\_ctx, ...);

468

470

[ 474](group__mspi__interface.md#ga2ff9209634fb241e2f7323e749df612e)typedef int (\*[mspi\_api\_config](group__mspi__interface.md#ga2ff9209634fb241e2f7323e749df612e))(const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \*spec);

475

[ 476](group__mspi__interface.md#ga7e3bae501067b045e9ed8d0efbe6e61d)typedef int (\*[mspi\_api\_dev\_config](group__mspi__interface.md#ga7e3bae501067b045e9ed8d0efbe6e61d))(const struct [device](structdevice.md) \*controller,

477 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

478 const enum [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) param\_mask,

479 const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \*cfg);

480

[ 481](group__mspi__interface.md#gadd66b118b76a4ee7ef252afc6b830bfa)typedef int (\*[mspi\_api\_get\_channel\_status](group__mspi__interface.md#gadd66b118b76a4ee7ef252afc6b830bfa))(const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ch);

482

[ 483](group__mspi__interface.md#ga17b551f4d9f980fde8eabcaae3318617)typedef int (\*[mspi\_api\_transceive](group__mspi__interface.md#ga17b551f4d9f980fde8eabcaae3318617))(const struct [device](structdevice.md) \*controller,

484 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

485 const struct [mspi\_xfer](structmspi__xfer.md) \*req);

486

[ 487](group__mspi__interface.md#gad6d65ef0d523f22592ff17c04698f663)typedef int (\*[mspi\_api\_register\_callback](group__mspi__interface.md#gad6d65ef0d523f22592ff17c04698f663))(const struct [device](structdevice.md) \*controller,

488 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

489 const enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type,

490 [mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4) cb,

491 struct [mspi\_callback\_context](structmspi__callback__context.md) \*[ctx](structmspi__callback__context.md#ab2225b77f4d9e0403192c0ab11482e2e));

492

[ 493](group__mspi__interface.md#ga823ad87bec1c73ee110f3ae8107d03e7)typedef int (\*[mspi\_api\_xip\_config](group__mspi__interface.md#ga823ad87bec1c73ee110f3ae8107d03e7))(const struct [device](structdevice.md) \*controller,

494 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

495 const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \*xip\_cfg);

496

[ 497](group__mspi__interface.md#ga092c8bb0879977a8cc8eea5d1662c34b)typedef int (\*[mspi\_api\_scramble\_config](group__mspi__interface.md#ga092c8bb0879977a8cc8eea5d1662c34b))(const struct [device](structdevice.md) \*controller,

498 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

499 const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \*scramble\_cfg);

500

[ 501](group__mspi__interface.md#ga407713e07f23756564814402342c9c97)typedef int (\*[mspi\_api\_timing\_config](group__mspi__interface.md#ga407713e07f23756564814402342c9c97))(const struct [device](structdevice.md) \*controller,

502 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param\_mask,

503 void \*timing\_cfg);

504

[ 505](structmspi__driver__api.md)\_\_subsystem struct [mspi\_driver\_api](structmspi__driver__api.md) {

[ 506](structmspi__driver__api.md#a05c3dad20834850a833663dd896fa6eb) [mspi\_api\_config](group__mspi__interface.md#ga2ff9209634fb241e2f7323e749df612e) [config](structmspi__driver__api.md#a05c3dad20834850a833663dd896fa6eb);

[ 507](structmspi__driver__api.md#a1a4593ada09a204004a11dcb6031c18f) [mspi\_api\_dev\_config](group__mspi__interface.md#ga7e3bae501067b045e9ed8d0efbe6e61d) [dev\_config](structmspi__driver__api.md#a1a4593ada09a204004a11dcb6031c18f);

[ 508](structmspi__driver__api.md#a31bf25f0ce01b9aada76f6b0030b05be) [mspi\_api\_get\_channel\_status](group__mspi__interface.md#gadd66b118b76a4ee7ef252afc6b830bfa) [get\_channel\_status](structmspi__driver__api.md#a31bf25f0ce01b9aada76f6b0030b05be);

[ 509](structmspi__driver__api.md#aae8c346182a9c437891044afc0b16e07) [mspi\_api\_transceive](group__mspi__interface.md#ga17b551f4d9f980fde8eabcaae3318617) [transceive](structmspi__driver__api.md#aae8c346182a9c437891044afc0b16e07);

[ 510](structmspi__driver__api.md#a15a53b61fcd32d0436323ad85c75f62a) [mspi\_api\_register\_callback](group__mspi__interface.md#gad6d65ef0d523f22592ff17c04698f663) [register\_callback](structmspi__driver__api.md#a15a53b61fcd32d0436323ad85c75f62a);

[ 511](structmspi__driver__api.md#ae0762538f5c73eac4dc2078b509819dd) [mspi\_api\_xip\_config](group__mspi__interface.md#ga823ad87bec1c73ee110f3ae8107d03e7) [xip\_config](structmspi__driver__api.md#ae0762538f5c73eac4dc2078b509819dd);

[ 512](structmspi__driver__api.md#aa0a42a85841370693ce054ed859d1fd8) [mspi\_api\_scramble\_config](group__mspi__interface.md#ga092c8bb0879977a8cc8eea5d1662c34b) [scramble\_config](structmspi__driver__api.md#aa0a42a85841370693ce054ed859d1fd8);

[ 513](structmspi__driver__api.md#a77553c6ea19e8803dcabc4deccf35619) [mspi\_api\_timing\_config](group__mspi__interface.md#ga407713e07f23756564814402342c9c97) [timing\_config](structmspi__driver__api.md#a77553c6ea19e8803dcabc4deccf35619);

514};

515

520

[ 542](group__mspi__configure__api.md#ga46c2b98e99ecea045c1ecac4bdf3f087)\_\_syscall int [mspi\_config](group__mspi__configure__api.md#ga46c2b98e99ecea045c1ecac4bdf3f087)(const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \*spec);

543

544static inline int z\_impl\_mspi\_config(const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \*spec)

545{

546 const struct [mspi\_driver\_api](structmspi__driver__api.md) \*api = (const struct [mspi\_driver\_api](structmspi__driver__api.md) \*)spec->[bus](structmspi__dt__spec.md#ab21ff3d5959b78f5b5cdc7fcf70e8756)->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

547

548 return api->config(spec);

549}

550

[ 578](group__mspi__configure__api.md#gaa3c1eae8b3000c9bafcc26f14a8beb8b)\_\_syscall int [mspi\_dev\_config](group__mspi__configure__api.md#gaa3c1eae8b3000c9bafcc26f14a8beb8b)(const struct [device](structdevice.md) \*controller,

579 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

580 const enum [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) param\_mask,

581 const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \*cfg);

582

583static inline int z\_impl\_mspi\_dev\_config(const struct [device](structdevice.md) \*controller,

584 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

585 const enum [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) param\_mask,

586 const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \*cfg)

587{

588 const struct [mspi\_driver\_api](structmspi__driver__api.md) \*api = (const struct [mspi\_driver\_api](structmspi__driver__api.md) \*)controller->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

589

590 return api->dev\_config(controller, dev\_id, param\_mask, cfg);

591}

592

[ 604](group__mspi__configure__api.md#ga957b6ecd96c9f942f75bbe500898930d)\_\_syscall int [mspi\_get\_channel\_status](group__mspi__configure__api.md#ga957b6ecd96c9f942f75bbe500898930d)(const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ch);

605

606static inline int z\_impl\_mspi\_get\_channel\_status(const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ch)

607{

608 const struct [mspi\_driver\_api](structmspi__driver__api.md) \*api = (const struct [mspi\_driver\_api](structmspi__driver__api.md) \*)controller->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

609

610 return api->get\_channel\_status(controller, ch);

611}

612

614

619

[ 644](group__mspi__transfer__api.md#ga8c98c73e322c575b759ce911cc115129)\_\_syscall int [mspi\_transceive](group__mspi__transfer__api.md#ga8c98c73e322c575b759ce911cc115129)(const struct [device](structdevice.md) \*controller,

645 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

646 const struct [mspi\_xfer](structmspi__xfer.md) \*req);

647

648static inline int z\_impl\_mspi\_transceive(const struct [device](structdevice.md) \*controller,

649 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

650 const struct [mspi\_xfer](structmspi__xfer.md) \*req)

651{

652 const struct [mspi\_driver\_api](structmspi__driver__api.md) \*api = (const struct [mspi\_driver\_api](structmspi__driver__api.md) \*)controller->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

653

654 if (!api->transceive) {

655 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

656 }

657

658 return api->transceive(controller, dev\_id, req);

659}

660

662

667

[ 682](group__mspi__configure__api.md#gab9d9104636d3c8167b5876b1bc4348ea)\_\_syscall int [mspi\_xip\_config](group__mspi__configure__api.md#gab9d9104636d3c8167b5876b1bc4348ea)(const struct [device](structdevice.md) \*controller,

683 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

684 const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \*cfg);

685

686static inline int z\_impl\_mspi\_xip\_config(const struct [device](structdevice.md) \*controller,

687 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

688 const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \*cfg)

689{

690 const struct [mspi\_driver\_api](structmspi__driver__api.md) \*api = (const struct [mspi\_driver\_api](structmspi__driver__api.md) \*)controller->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

691

692 if (!api->xip\_config) {

693 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

694 }

695

696 return api->xip\_config(controller, dev\_id, cfg);

697}

698

[ 714](group__mspi__configure__api.md#gacf287e08b6ce4898524884e8de22b806)\_\_syscall int [mspi\_scramble\_config](group__mspi__configure__api.md#gacf287e08b6ce4898524884e8de22b806)(const struct [device](structdevice.md) \*controller,

715 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

716 const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \*cfg);

717

718static inline int z\_impl\_mspi\_scramble\_config(const struct [device](structdevice.md) \*controller,

719 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

720 const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \*cfg)

721{

722 const struct [mspi\_driver\_api](structmspi__driver__api.md) \*api = (const struct [mspi\_driver\_api](structmspi__driver__api.md) \*)controller->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

723

724 if (!api->scramble\_config) {

725 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

726 }

727

728 return api->scramble\_config(controller, dev\_id, cfg);

729}

730

[ 747](group__mspi__configure__api.md#gaff82af1cfc99b9e78cec17ea27f79ab6)\_\_syscall int [mspi\_timing\_config](group__mspi__configure__api.md#gaff82af1cfc99b9e78cec17ea27f79ab6)(const struct [device](structdevice.md) \*controller,

748 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

749 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param\_mask, void \*cfg);

750

751static inline int z\_impl\_mspi\_timing\_config(const struct [device](structdevice.md) \*controller,

752 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

753 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param\_mask, void \*cfg)

754{

755 const struct [mspi\_driver\_api](structmspi__driver__api.md) \*api = (const struct [mspi\_driver\_api](structmspi__driver__api.md) \*)controller->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

756

757 if (!api->timing\_config) {

758 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

759 }

760

761 return api->timing\_config(controller, dev\_id, param\_mask, cfg);

762}

763

765

770

[ 786](group__mspi__callback__api.md#ga967f5fed63f08ac2d5a88625b030cd14)static inline int [mspi\_register\_callback](group__mspi__callback__api.md#ga967f5fed63f08ac2d5a88625b030cd14)(const struct [device](structdevice.md) \*controller,

787 const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id,

788 const enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type,

789 [mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4) cb,

790 struct [mspi\_callback\_context](structmspi__callback__context.md) \*ctx)

791{

792 const struct [mspi\_driver\_api](structmspi__driver__api.md) \*api = (const struct [mspi\_driver\_api](structmspi__driver__api.md) \*)controller->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

793

794 if (!api->[register\_callback](structmspi__driver__api.md#a15a53b61fcd32d0436323ad85c75f62a)) {

795 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

796 }

797

798 return api->[register\_callback](structmspi__driver__api.md#a15a53b61fcd32d0436323ad85c75f62a)(controller, dev\_id, evt\_type, cb, ctx);

799}

800

802

803#ifdef \_\_cplusplus

804}

805#endif

806

807#include <[zephyr/drivers/mspi/devicetree.h](drivers_2mspi_2devicetree_8h.md)>

808

812#include <zephyr/syscalls/mspi.h>

813#endif /\* ZEPHYR\_INCLUDE\_MSPI\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[device.h](device_8h.md)

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[devicetree.h](drivers_2mspi_2devicetree_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4)

void(\* mspi\_callback\_handler\_t)(struct mspi\_callback\_context \*mspi\_cb\_ctx,...)

Define the application callback handler function signature.

**Definition** mspi.h:467

[mspi\_register\_callback](group__mspi__callback__api.md#ga967f5fed63f08ac2d5a88625b030cd14)

static int mspi\_register\_callback(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const enum mspi\_bus\_event evt\_type, mspi\_callback\_handler\_t cb, struct mspi\_callback\_context \*ctx)

Register the mspi callback functions.

**Definition** mspi.h:786

[mspi\_config](group__mspi__configure__api.md#ga46c2b98e99ecea045c1ecac4bdf3f087)

int mspi\_config(const struct mspi\_dt\_spec \*spec)

Configure a MSPI controller.

[mspi\_get\_channel\_status](group__mspi__configure__api.md#ga957b6ecd96c9f942f75bbe500898930d)

int mspi\_get\_channel\_status(const struct device \*controller, uint8\_t ch)

Query to see if it a channel is ready.

[mspi\_timing\_param](group__mspi__configure__api.md#gaa25a7f97ab3437d4544832a0e7474f4a)

mspi\_timing\_param

Stub for timing parameter.

**Definition** mspi.h:199

[mspi\_dev\_config](group__mspi__configure__api.md#gaa3c1eae8b3000c9bafcc26f14a8beb8b)

int mspi\_dev\_config(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const enum mspi\_dev\_cfg\_mask param\_mask, const struct mspi\_dev\_cfg \*cfg)

Configure a MSPI controller with device specific parameters.

[mspi\_xip\_config](group__mspi__configure__api.md#gab9d9104636d3c8167b5876b1bc4348ea)

int mspi\_xip\_config(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_xip\_cfg \*cfg)

Configure a MSPI XIP settings.

[mspi\_scramble\_config](group__mspi__configure__api.md#gacf287e08b6ce4898524884e8de22b806)

int mspi\_scramble\_config(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_scramble\_cfg \*cfg)

Configure a MSPI scrambling settings.

[mspi\_timing\_config](group__mspi__configure__api.md#gaff82af1cfc99b9e78cec17ea27f79ab6)

int mspi\_timing\_config(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const uint32\_t param\_mask, void \*cfg)

Configure a MSPI timing settings.

[MSPI\_TIMING\_PARAM\_DUMMY](group__mspi__configure__api.md#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237)

@ MSPI\_TIMING\_PARAM\_DUMMY

**Definition** mspi.h:200

[mspi\_xip\_permit](group__mspi__interface.md#ga006a1e32778a02299b3500886bb194fa)

mspi\_xip\_permit

MSPI XIP access permissions.

**Definition** mspi.h:185

[mspi\_api\_scramble\_config](group__mspi__interface.md#ga092c8bb0879977a8cc8eea5d1662c34b)

int(\* mspi\_api\_scramble\_config)(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_scramble\_cfg \*scramble\_cfg)

**Definition** mspi.h:497

[mspi\_xfer\_mode](group__mspi__interface.md#ga116259bbb1d12a10c2ba9e6051f2f000)

mspi\_xfer\_mode

MSPI transfer modes.

**Definition** mspi.h:145

[mspi\_api\_transceive](group__mspi__interface.md#ga17b551f4d9f980fde8eabcaae3318617)

int(\* mspi\_api\_transceive)(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_xfer \*req)

**Definition** mspi.h:483

[mspi\_duplex](group__mspi__interface.md#ga20e348d7a9f1f9b32078a3bf6c4e82b9)

mspi\_duplex

MSPI duplex mode.

**Definition** mspi.h:47

[mspi\_ce\_polarity](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b)

mspi\_ce\_polarity

MSPI chip enable polarity.

**Definition** mspi.h:113

[mspi\_api\_config](group__mspi__interface.md#ga2ff9209634fb241e2f7323e749df612e)

int(\* mspi\_api\_config)(const struct mspi\_dt\_spec \*spec)

MSPI driver API definition and system call entry points.

**Definition** mspi.h:474

[mspi\_endian](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44)

mspi\_endian

MSPI Endian.

**Definition** mspi.h:105

[mspi\_op\_mode](group__mspi__interface.md#ga3f211cd81e05cb9ee073a2722f6b22d8)

mspi\_op\_mode

MSPI operational mode.

**Definition** mspi.h:39

[mspi\_api\_timing\_config](group__mspi__interface.md#ga407713e07f23756564814402342c9c97)

int(\* mspi\_api\_timing\_config)(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const uint32\_t param\_mask, void \*timing\_cfg)

**Definition** mspi.h:501

[mspi\_xfer\_direction](group__mspi__interface.md#ga498f10591acf5dc7ec88e0aa98e537d6)

mspi\_xfer\_direction

MSPI transfer directions.

**Definition** mspi.h:153

[mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5)

mspi\_bus\_event

MSPI bus event.

**Definition** mspi.h:123

[mspi\_cpp\_mode](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c)

mspi\_cpp\_mode

MSPI Polarity & Phase Modes.

**Definition** mspi.h:95

[mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647)

mspi\_dev\_cfg\_mask

MSPI controller device specific configuration mask.

**Definition** mspi.h:161

[mspi\_api\_dev\_config](group__mspi__interface.md#ga7e3bae501067b045e9ed8d0efbe6e61d)

int(\* mspi\_api\_dev\_config)(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const enum mspi\_dev\_cfg\_mask param\_mask, const struct mspi\_dev\_cfg \*cfg)

**Definition** mspi.h:476

[mspi\_api\_xip\_config](group__mspi__interface.md#ga823ad87bec1c73ee110f3ae8107d03e7)

int(\* mspi\_api\_xip\_config)(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_xip\_cfg \*xip\_cfg)

**Definition** mspi.h:493

[mspi\_io\_mode](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5)

mspi\_io\_mode

MSPI I/O mode capabilities Postfix like 1\_4\_4 stands for the number of lines used for command,...

**Definition** mspi.h:58

[mspi\_data\_rate](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68)

mspi\_data\_rate

MSPI data rate capabilities SINGLE stands for single data rate for all phases.

**Definition** mspi.h:84

[mspi\_bus\_event\_cb\_mask](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1)

mspi\_bus\_event\_cb\_mask

MSPI bus event callback mask This is a preliminary list same as mspi\_bus\_event.

**Definition** mspi.h:135

[mspi\_api\_register\_callback](group__mspi__interface.md#gad6d65ef0d523f22592ff17c04698f663)

int(\* mspi\_api\_register\_callback)(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const enum mspi\_bus\_event evt\_type, mspi\_callback\_handler\_t cb, struct mspi\_callback\_context \*ctx)

**Definition** mspi.h:487

[mspi\_api\_get\_channel\_status](group__mspi__interface.md#gadd66b118b76a4ee7ef252afc6b830bfa)

int(\* mspi\_api\_get\_channel\_status)(const struct device \*controller, uint8\_t ch)

**Definition** mspi.h:481

[MSPI\_XIP\_READ\_WRITE](group__mspi__interface.md#gga006a1e32778a02299b3500886bb194faa431525f8be52537b0a831f522726c7b9)

@ MSPI\_XIP\_READ\_WRITE

**Definition** mspi.h:186

[MSPI\_XIP\_READ\_ONLY](group__mspi__interface.md#gga006a1e32778a02299b3500886bb194faae9b2d08d8ae1722c3014a706fc801731)

@ MSPI\_XIP\_READ\_ONLY

**Definition** mspi.h:187

[MSPI\_DMA](group__mspi__interface.md#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8)

@ MSPI\_DMA

**Definition** mspi.h:147

[MSPI\_PIO](group__mspi__interface.md#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1)

@ MSPI\_PIO

**Definition** mspi.h:146

[MSPI\_FULL\_DUPLEX](group__mspi__interface.md#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c)

@ MSPI\_FULL\_DUPLEX

**Definition** mspi.h:49

[MSPI\_HALF\_DUPLEX](group__mspi__interface.md#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3)

@ MSPI\_HALF\_DUPLEX

**Definition** mspi.h:48

[MSPI\_CE\_ACTIVE\_HIGH](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22)

@ MSPI\_CE\_ACTIVE\_HIGH

**Definition** mspi.h:115

[MSPI\_CE\_ACTIVE\_LOW](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae)

@ MSPI\_CE\_ACTIVE\_LOW

**Definition** mspi.h:114

[MSPI\_XFER\_BIG\_ENDIAN](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d)

@ MSPI\_XFER\_BIG\_ENDIAN

**Definition** mspi.h:107

[MSPI\_XFER\_LITTLE\_ENDIAN](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345)

@ MSPI\_XFER\_LITTLE\_ENDIAN

**Definition** mspi.h:106

[MSPI\_OP\_MODE\_PERIPHERAL](group__mspi__interface.md#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83)

@ MSPI\_OP\_MODE\_PERIPHERAL

**Definition** mspi.h:41

[MSPI\_OP\_MODE\_CONTROLLER](group__mspi__interface.md#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a)

@ MSPI\_OP\_MODE\_CONTROLLER

**Definition** mspi.h:40

[MSPI\_RX](group__mspi__interface.md#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541)

@ MSPI\_RX

**Definition** mspi.h:154

[MSPI\_TX](group__mspi__interface.md#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a)

@ MSPI\_TX

**Definition** mspi.h:155

[MSPI\_BUS\_EVENT\_MAX](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a)

@ MSPI\_BUS\_EVENT\_MAX

**Definition** mspi.h:127

[MSPI\_BUS\_XFER\_COMPLETE](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61)

@ MSPI\_BUS\_XFER\_COMPLETE

**Definition** mspi.h:126

[MSPI\_BUS\_ERROR](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0)

@ MSPI\_BUS\_ERROR

**Definition** mspi.h:125

[MSPI\_BUS\_RESET](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64)

@ MSPI\_BUS\_RESET

**Definition** mspi.h:124

[MSPI\_CPP\_MODE\_3](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48)

@ MSPI\_CPP\_MODE\_3

**Definition** mspi.h:99

[MSPI\_CPP\_MODE\_1](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870)

@ MSPI\_CPP\_MODE\_1

**Definition** mspi.h:97

[MSPI\_CPP\_MODE\_2](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705)

@ MSPI\_CPP\_MODE\_2

**Definition** mspi.h:98

[MSPI\_CPP\_MODE\_0](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90)

@ MSPI\_CPP\_MODE\_0

**Definition** mspi.h:96

[MSPI\_DEVICE\_CONFIG\_CPP](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65)

@ MSPI\_DEVICE\_CONFIG\_CPP

**Definition** mspi.h:167

[MSPI\_DEVICE\_CONFIG\_DATA\_RATE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9)

@ MSPI\_DEVICE\_CONFIG\_DATA\_RATE

**Definition** mspi.h:166

[MSPI\_DEVICE\_CONFIG\_RX\_DUMMY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a)

@ MSPI\_DEVICE\_CONFIG\_RX\_DUMMY

**Definition** mspi.h:171

[MSPI\_DEVICE\_CONFIG\_FREQUENCY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809)

@ MSPI\_DEVICE\_CONFIG\_FREQUENCY

**Definition** mspi.h:164

[MSPI\_DEVICE\_CONFIG\_CMD\_LEN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac)

@ MSPI\_DEVICE\_CONFIG\_CMD\_LEN

**Definition** mspi.h:175

[MSPI\_DEVICE\_CONFIG\_CE\_NUM](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2)

@ MSPI\_DEVICE\_CONFIG\_CE\_NUM

**Definition** mspi.h:163

[MSPI\_DEVICE\_CONFIG\_IO\_MODE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f)

@ MSPI\_DEVICE\_CONFIG\_IO\_MODE

**Definition** mspi.h:165

[MSPI\_DEVICE\_CONFIG\_CE\_POL](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b)

@ MSPI\_DEVICE\_CONFIG\_CE\_POL

**Definition** mspi.h:169

[MSPI\_DEVICE\_CONFIG\_DQS](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537)

@ MSPI\_DEVICE\_CONFIG\_DQS

**Definition** mspi.h:170

[MSPI\_DEVICE\_CONFIG\_TX\_DUMMY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5)

@ MSPI\_DEVICE\_CONFIG\_TX\_DUMMY

**Definition** mspi.h:172

[MSPI\_DEVICE\_CONFIG\_ALL](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489)

@ MSPI\_DEVICE\_CONFIG\_ALL

**Definition** mspi.h:179

[MSPI\_DEVICE\_CONFIG\_WRITE\_CMD](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b)

@ MSPI\_DEVICE\_CONFIG\_WRITE\_CMD

**Definition** mspi.h:174

[MSPI\_DEVICE\_CONFIG\_ADDR\_LEN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b)

@ MSPI\_DEVICE\_CONFIG\_ADDR\_LEN

**Definition** mspi.h:176

[MSPI\_DEVICE\_CONFIG\_ENDIAN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca)

@ MSPI\_DEVICE\_CONFIG\_ENDIAN

**Definition** mspi.h:168

[MSPI\_DEVICE\_CONFIG\_NONE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878)

@ MSPI\_DEVICE\_CONFIG\_NONE

**Definition** mspi.h:162

[MSPI\_DEVICE\_CONFIG\_BREAK\_TIME](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120)

@ MSPI\_DEVICE\_CONFIG\_BREAK\_TIME

**Definition** mspi.h:178

[MSPI\_DEVICE\_CONFIG\_MEM\_BOUND](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946)

@ MSPI\_DEVICE\_CONFIG\_MEM\_BOUND

**Definition** mspi.h:177

[MSPI\_DEVICE\_CONFIG\_READ\_CMD](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872)

@ MSPI\_DEVICE\_CONFIG\_READ\_CMD

**Definition** mspi.h:173

[MSPI\_IO\_MODE\_HEX](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b)

@ MSPI\_IO\_MODE\_HEX

**Definition** mspi.h:69

[MSPI\_IO\_MODE\_QUAD\_1\_4\_4](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a)

@ MSPI\_IO\_MODE\_QUAD\_1\_4\_4

**Definition** mspi.h:65

[MSPI\_IO\_MODE\_OCTAL\_1\_8\_8](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573)

@ MSPI\_IO\_MODE\_OCTAL\_1\_8\_8

**Definition** mspi.h:68

[MSPI\_IO\_MODE\_HEX\_8\_16\_16](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa)

@ MSPI\_IO\_MODE\_HEX\_8\_16\_16

**Definition** mspi.h:71

[MSPI\_IO\_MODE\_SINGLE](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd)

@ MSPI\_IO\_MODE\_SINGLE

**Definition** mspi.h:59

[MSPI\_IO\_MODE\_DUAL\_1\_1\_2](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da)

@ MSPI\_IO\_MODE\_DUAL\_1\_1\_2

**Definition** mspi.h:61

[MSPI\_IO\_MODE\_DUAL](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673)

@ MSPI\_IO\_MODE\_DUAL

**Definition** mspi.h:60

[MSPI\_IO\_MODE\_MAX](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb)

@ MSPI\_IO\_MODE\_MAX

**Definition** mspi.h:72

[MSPI\_IO\_MODE\_DUAL\_1\_2\_2](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663)

@ MSPI\_IO\_MODE\_DUAL\_1\_2\_2

**Definition** mspi.h:62

[MSPI\_IO\_MODE\_QUAD\_1\_1\_4](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a)

@ MSPI\_IO\_MODE\_QUAD\_1\_1\_4

**Definition** mspi.h:64

[MSPI\_IO\_MODE\_OCTAL\_1\_1\_8](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf)

@ MSPI\_IO\_MODE\_OCTAL\_1\_1\_8

**Definition** mspi.h:67

[MSPI\_IO\_MODE\_OCTAL](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725)

@ MSPI\_IO\_MODE\_OCTAL

**Definition** mspi.h:66

[MSPI\_IO\_MODE\_HEX\_8\_8\_16](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02)

@ MSPI\_IO\_MODE\_HEX\_8\_8\_16

**Definition** mspi.h:70

[MSPI\_IO\_MODE\_QUAD](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a)

@ MSPI\_IO\_MODE\_QUAD

**Definition** mspi.h:63

[MSPI\_DATA\_RATE\_SINGLE](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0)

@ MSPI\_DATA\_RATE\_SINGLE

**Definition** mspi.h:85

[MSPI\_DATA\_RATE\_S\_S\_D](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39)

@ MSPI\_DATA\_RATE\_S\_S\_D

**Definition** mspi.h:86

[MSPI\_DATA\_RATE\_MAX](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9)

@ MSPI\_DATA\_RATE\_MAX

**Definition** mspi.h:89

[MSPI\_DATA\_RATE\_S\_D\_D](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984)

@ MSPI\_DATA\_RATE\_S\_D\_D

**Definition** mspi.h:87

[MSPI\_DATA\_RATE\_DUAL](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc)

@ MSPI\_DATA\_RATE\_DUAL

**Definition** mspi.h:88

[MSPI\_BUS\_ERROR\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498)

@ MSPI\_BUS\_ERROR\_CB

**Definition** mspi.h:138

[MSPI\_BUS\_RESET\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1)

@ MSPI\_BUS\_RESET\_CB

**Definition** mspi.h:137

[MSPI\_BUS\_XFER\_COMPLETE\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7)

@ MSPI\_BUS\_XFER\_COMPLETE\_CB

**Definition** mspi.h:139

[MSPI\_BUS\_NO\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277)

@ MSPI\_BUS\_NO\_CB

**Definition** mspi.h:136

[mspi\_transceive](group__mspi__transfer__api.md#ga8c98c73e322c575b759ce911cc115129)

int mspi\_transceive(const struct device \*controller, const struct mspi\_dev\_id \*dev\_id, const struct mspi\_xfer \*req)

Transfer request over MSPI.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

Bit mask with bits 0 through n-1 (inclusive) set, or 0 if n is 0.

**Definition** util\_macro.h:68

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:288

[mspi\_callback\_context](structmspi__callback__context.md)

MSPI callback context.

**Definition** mspi.h:453

[mspi\_callback\_context::mspi\_evt](structmspi__callback__context.md#a5649bddfac23544522969fc9e500eb0c)

struct mspi\_event mspi\_evt

MSPI event.

**Definition** mspi.h:455

[mspi\_callback\_context::ctx](structmspi__callback__context.md#ab2225b77f4d9e0403192c0ab11482e2e)

void \* ctx

user defined context

**Definition** mspi.h:457

[mspi\_ce\_control](structmspi__ce__control.md)

MSPI Chip Select control structure.

**Definition** mspi.h:348

[mspi\_ce\_control::gpio](structmspi__ce__control.md#a1f1b6f5583abc08c8c7fae95e1a29a7a)

struct gpio\_dt\_spec gpio

GPIO devicetree specification of CE GPIO.

**Definition** mspi.h:355

[mspi\_ce\_control::delay](structmspi__ce__control.md#abc3e35be0b7b3f5c118b0d16033125ba)

uint32\_t delay

Delay to wait.

**Definition** mspi.h:361

[mspi\_cfg](structmspi__cfg.md)

MSPI controller configuration.

**Definition** mspi.h:228

[mspi\_cfg::sw\_multi\_periph](structmspi__cfg.md#a1192af56f714a42aa667a40e369b185e)

bool sw\_multi\_periph

Software managed multi peripheral enable.

**Definition** mspi.h:238

[mspi\_cfg::num\_ce\_gpios](structmspi__cfg.md#a20f6e453165b6ac22a42906604a3258a)

uint32\_t num\_ce\_gpios

GPIO chip-select line numbers (optional).

**Definition** mspi.h:242

[mspi\_cfg::dqs\_support](structmspi__cfg.md#a2cf6e063074f86973cf03324637d656a)

bool dqs\_support

DQS support flag.

**Definition** mspi.h:236

[mspi\_cfg::ce\_group](structmspi__cfg.md#a4053a398f6390e45ef6da385756f14bf)

struct gpio\_dt\_spec \* ce\_group

GPIO chip select lines (optional).

**Definition** mspi.h:240

[mspi\_cfg::duplex](structmspi__cfg.md#a449894e0e58f96b775b4cc1c1eb83e77)

enum mspi\_duplex duplex

Configure duplex mode.

**Definition** mspi.h:234

[mspi\_cfg::num\_periph](structmspi__cfg.md#a6d24969046f175f158a5dae05e9284b1)

uint32\_t num\_periph

Peripheral number from 0 to host controller peripheral limit.

**Definition** mspi.h:244

[mspi\_cfg::max\_freq](structmspi__cfg.md#a9a76198688b4acac9101274a71bfbf9c)

uint32\_t max\_freq

Maximum supported frequency in MHz.

**Definition** mspi.h:246

[mspi\_cfg::op\_mode](structmspi__cfg.md#ab33e45d7802cf777a595d87058e8bfb5)

enum mspi\_op\_mode op\_mode

Configure operation mode.

**Definition** mspi.h:232

[mspi\_cfg::channel\_num](structmspi__cfg.md#af54bbbfbe07d88325117131fefe265ef)

uint8\_t channel\_num

mspi channel number

**Definition** mspi.h:230

[mspi\_cfg::re\_init](structmspi__cfg.md#afef0fe6991e28a4496e51333963fd3d1)

bool re\_init

Whether to re-initialize controller.

**Definition** mspi.h:248

[mspi\_dev\_cfg](structmspi__dev__cfg.md)

MSPI controller device specific configuration.

**Definition** mspi.h:264

[mspi\_dev\_cfg::cmd\_length](structmspi__dev__cfg.md#a0b0c9f101656e67d71d191b656738d2d)

uint8\_t cmd\_length

Configure command length.

**Definition** mspi.h:294

[mspi\_dev\_cfg::data\_rate](structmspi__dev__cfg.md#a0da8c2ccf80fdf610fcdd7fae7d159f8)

enum mspi\_data\_rate data\_rate

Configure data rate.

**Definition** mspi.h:272

[mspi\_dev\_cfg::endian](structmspi__dev__cfg.md#a28cf9d7887e9f840344e2804c4040bc4)

enum mspi\_endian endian

Configure transfer endian.

**Definition** mspi.h:276

[mspi\_dev\_cfg::cpp](structmspi__dev__cfg.md#a2bb78caec28fadcecd787fc8a573a336)

enum mspi\_cpp\_mode cpp

Configure clock polarity and phase.

**Definition** mspi.h:274

[mspi\_dev\_cfg::mem\_boundary](structmspi__dev__cfg.md#a3ec3e22e25440ac5eecf0f9b2d79b9e0)

uint32\_t mem\_boundary

Configure memory boundary.

**Definition** mspi.h:298

[mspi\_dev\_cfg::time\_to\_break](structmspi__dev__cfg.md#a60eeb1503018fa47cc5618d150f09aa8)

uint32\_t time\_to\_break

Configure the time to break up a transfer into 2.

**Definition** mspi.h:300

[mspi\_dev\_cfg::addr\_length](structmspi__dev__cfg.md#a6dbe113d5075b1b22896c7d0c281bd3d)

uint8\_t addr\_length

Configure address length.

**Definition** mspi.h:296

[mspi\_dev\_cfg::freq](structmspi__dev__cfg.md#a9490d822b67d7fab123f32f38b0ccef8)

uint32\_t freq

Configure frequency.

**Definition** mspi.h:268

[mspi\_dev\_cfg::tx\_dummy](structmspi__dev__cfg.md#a9feb1c35f7e1f5c43489771e13f2af8d)

uint16\_t tx\_dummy

Configure number of clock cycles between addr and data in TX direction.

**Definition** mspi.h:288

[mspi\_dev\_cfg::rx\_dummy](structmspi__dev__cfg.md#aae492d2e5bad4b266779be9f5bb12ee9)

uint16\_t rx\_dummy

Configure number of clock cycles between addr and data in RX direction.

**Definition** mspi.h:284

[mspi\_dev\_cfg::ce\_polarity](structmspi__dev__cfg.md#ab6ed7eeb6d4b31530e06f69706b98278)

enum mspi\_ce\_polarity ce\_polarity

Configure chip enable polarity.

**Definition** mspi.h:278

[mspi\_dev\_cfg::ce\_num](structmspi__dev__cfg.md#abf8d45f88d0c8e1c4ee52ea238ff4466)

uint8\_t ce\_num

Configure CE0 or CE1 or more.

**Definition** mspi.h:266

[mspi\_dev\_cfg::read\_cmd](structmspi__dev__cfg.md#ac9f47b226289005271a800739707456b)

uint32\_t read\_cmd

Configure read command.

**Definition** mspi.h:290

[mspi\_dev\_cfg::write\_cmd](structmspi__dev__cfg.md#acac2a0913bfbfe1f3b5e34ff1b71ff42)

uint32\_t write\_cmd

Configure write command.

**Definition** mspi.h:292

[mspi\_dev\_cfg::io\_mode](structmspi__dev__cfg.md#ad0f5c1a4cd3002313087a9b1fe6cf7a1)

enum mspi\_io\_mode io\_mode

Configure I/O mode.

**Definition** mspi.h:270

[mspi\_dev\_cfg::dqs\_enable](structmspi__dev__cfg.md#affdcd07ac3d3d25b8a8e0882277af39a)

bool dqs\_enable

Configure DQS mode.

**Definition** mspi.h:280

[mspi\_dev\_id](structmspi__dev__id.md)

MSPI device ID The controller can identify its devices and determine whether the access is allowed in...

**Definition** mspi.h:218

[mspi\_dev\_id::dev\_idx](structmspi__dev__id.md#aab54e4f449d4cfb87c5c6f0ccd1d7bfb)

uint16\_t dev\_idx

device index on DT

**Definition** mspi.h:222

[mspi\_dev\_id::ce](structmspi__dev__id.md#ac79d41731c8599f23b666f78cdb58bf0)

struct gpio\_dt\_spec ce

device gpio ce

**Definition** mspi.h:220

[mspi\_driver\_api](structmspi__driver__api.md)

**Definition** mspi.h:505

[mspi\_driver\_api::config](structmspi__driver__api.md#a05c3dad20834850a833663dd896fa6eb)

mspi\_api\_config config

**Definition** mspi.h:506

[mspi\_driver\_api::register\_callback](structmspi__driver__api.md#a15a53b61fcd32d0436323ad85c75f62a)

mspi\_api\_register\_callback register\_callback

**Definition** mspi.h:510

[mspi\_driver\_api::dev\_config](structmspi__driver__api.md#a1a4593ada09a204004a11dcb6031c18f)

mspi\_api\_dev\_config dev\_config

**Definition** mspi.h:507

[mspi\_driver\_api::get\_channel\_status](structmspi__driver__api.md#a31bf25f0ce01b9aada76f6b0030b05be)

mspi\_api\_get\_channel\_status get\_channel\_status

**Definition** mspi.h:508

[mspi\_driver\_api::timing\_config](structmspi__driver__api.md#a77553c6ea19e8803dcabc4deccf35619)

mspi\_api\_timing\_config timing\_config

**Definition** mspi.h:513

[mspi\_driver\_api::scramble\_config](structmspi__driver__api.md#aa0a42a85841370693ce054ed859d1fd8)

mspi\_api\_scramble\_config scramble\_config

**Definition** mspi.h:512

[mspi\_driver\_api::transceive](structmspi__driver__api.md#aae8c346182a9c437891044afc0b16e07)

mspi\_api\_transceive transceive

**Definition** mspi.h:509

[mspi\_driver\_api::xip\_config](structmspi__driver__api.md#ae0762538f5c73eac4dc2078b509819dd)

mspi\_api\_xip\_config xip\_config

**Definition** mspi.h:511

[mspi\_dt\_spec](structmspi__dt__spec.md)

MSPI DT information.

**Definition** mspi.h:254

[mspi\_dt\_spec::config](structmspi__dt__spec.md#aaedbcdc55394032e3af50ec7d2e8f439)

struct mspi\_cfg config

MSPI hardware specific configuration.

**Definition** mspi.h:258

[mspi\_dt\_spec::bus](structmspi__dt__spec.md#ab21ff3d5959b78f5b5cdc7fcf70e8756)

const struct device \* bus

MSPI bus.

**Definition** mspi.h:256

[mspi\_event\_data](structmspi__event__data.md)

MSPI event data.

**Definition** mspi.h:427

[mspi\_event\_data::packet](structmspi__event__data.md#a1bb8c4591ced464181927b0c00003205)

const struct mspi\_xfer\_packet \* packet

Pointer to a transfer packet.

**Definition** mspi.h:433

[mspi\_event\_data::status](structmspi__event__data.md#a4b926cf5abb4f23bb7e1f85fecd323ef)

uint32\_t status

MSPI event status.

**Definition** mspi.h:435

[mspi\_event\_data::packet\_idx](structmspi__event__data.md#a6e71714475e45a0d758aa49db33ff57e)

uint32\_t packet\_idx

Packet index.

**Definition** mspi.h:437

[mspi\_event\_data::dev\_id](structmspi__event__data.md#ab1138c26f9a6b11b75e1e50fb3e5d8e9)

const struct mspi\_dev\_id \* dev\_id

Pointer to the peripheral device ID.

**Definition** mspi.h:431

[mspi\_event\_data::controller](structmspi__event__data.md#af788dc5374778055d1ee9fddbe2a4d8d)

const struct device \* controller

Pointer to the bus controller.

**Definition** mspi.h:429

[mspi\_event](structmspi__event.md)

MSPI event.

**Definition** mspi.h:443

[mspi\_event::evt\_type](structmspi__event.md#a65079ed0fcdb2ca607dab070f2ed010b)

enum mspi\_bus\_event evt\_type

Event type.

**Definition** mspi.h:445

[mspi\_event::evt\_data](structmspi__event.md#aeeb42b82bd219169e6f185ecdcc2129d)

struct mspi\_event\_data evt\_data

Data associated to the event.

**Definition** mspi.h:447

[mspi\_scramble\_cfg](structmspi__scramble__cfg.md)

MSPI controller scramble configuration.

**Definition** mspi.h:322

[mspi\_scramble\_cfg::enable](structmspi__scramble__cfg.md#a362ce29f7748d28e818e2c809bd4cedd)

bool enable

scramble enable

**Definition** mspi.h:324

[mspi\_scramble\_cfg::size](structmspi__scramble__cfg.md#a8d6d5b47b3d777674b974a6c79337b43)

uint32\_t size

scramble region size

**Definition** mspi.h:330

[mspi\_scramble\_cfg::address\_offset](structmspi__scramble__cfg.md#adf56743768432f22f0a5090e1b823a67)

uint32\_t address\_offset

scramble region start address = hardware default + address offset

**Definition** mspi.h:328

[mspi\_timing\_cfg](structmspi__timing__cfg.md)

Stub for struct timing\_cfg.

**Definition** mspi.h:206

[mspi\_xfer\_packet](structmspi__xfer__packet.md)

MSPI peripheral xfer packet format.

**Definition** mspi.h:367

[mspi\_xfer\_packet::num\_bytes](structmspi__xfer__packet.md#a050a827d0ee0349cd7a006de20b1db0c)

uint32\_t num\_bytes

Number of bytes to transfer.

**Definition** mspi.h:377

[mspi\_xfer\_packet::address](structmspi__xfer__packet.md#a08dae9b6fbda60f06430cb2b842280b9)

uint32\_t address

Transfer Address.

**Definition** mspi.h:375

[mspi\_xfer\_packet::data\_buf](structmspi__xfer__packet.md#a0b7b3d68ff46173378e4076b439e35ac)

uint8\_t \* data\_buf

Data Buffer.

**Definition** mspi.h:379

[mspi\_xfer\_packet::cmd](structmspi__xfer__packet.md#a2717e86b7fbb01be65a4955a8e26ebc0)

uint32\_t cmd

Transfer command.

**Definition** mspi.h:373

[mspi\_xfer\_packet::cb\_mask](structmspi__xfer__packet.md#aedc8eadfb3a0737c3984b130ec21d96c)

enum mspi\_bus\_event\_cb\_mask cb\_mask

Bus event callback masks.

**Definition** mspi.h:371

[mspi\_xfer\_packet::dir](structmspi__xfer__packet.md#afb408ea48ff8863c9714d39c4f7c8a2c)

enum mspi\_xfer\_direction dir

Direction (Transmit/Receive).

**Definition** mspi.h:369

[mspi\_xfer](structmspi__xfer.md)

MSPI peripheral xfer format This includes transfer related settings that may require configuring the ...

**Definition** mspi.h:387

[mspi\_xfer::hold\_ce](structmspi__xfer.md#a335fd5fb02bc75053902c4d1b294af57)

bool hold\_ce

Hold CE active after xfer.

**Definition** mspi.h:401

[mspi\_xfer::cmd\_length](structmspi__xfer.md#a387dd891ab994d75561b50a094427d22)

uint8\_t cmd\_length

Configure command length.

**Definition** mspi.h:397

[mspi\_xfer::num\_packet](structmspi__xfer.md#a4061b26045ef860b8c9a6509ff054bc3)

uint32\_t num\_packet

Number of transfer packets.

**Definition** mspi.h:411

[mspi\_xfer::packets](structmspi__xfer.md#a49e4102b694ffb5f9afe72c81fb7ca94)

const struct mspi\_xfer\_packet \* packets

Transfer packets.

**Definition** mspi.h:409

[mspi\_xfer::priority](structmspi__xfer.md#a8a829f14523acb252507e291b574363d)

uint8\_t priority

Priority 0 = Low (best effort) 1 = High (service immediately).

**Definition** mspi.h:407

[mspi\_xfer::rx\_dummy](structmspi__xfer.md#a98f23415592095749a853f3d850d399f)

uint16\_t rx\_dummy

Configure RX dummy cycles.

**Definition** mspi.h:395

[mspi\_xfer::async](structmspi__xfer.md#abf10b3fed96161447ffb7a8a6dce7649)

bool async

Async or sync transfer.

**Definition** mspi.h:389

[mspi\_xfer::addr\_length](structmspi__xfer.md#ace851e368d69b76092f8429d83d963fd)

uint8\_t addr\_length

Configure address length.

**Definition** mspi.h:399

[mspi\_xfer::tx\_dummy](structmspi__xfer.md#adfe7adf63f83f40d1ab92ed511f4e917)

uint16\_t tx\_dummy

Configure TX dummy cycles.

**Definition** mspi.h:393

[mspi\_xfer::ce\_sw\_ctrl](structmspi__xfer.md#ae2e7a475ac4bcec88f12742642087505)

struct mspi\_ce\_control ce\_sw\_ctrl

Software CE control.

**Definition** mspi.h:403

[mspi\_xfer::xfer\_mode](structmspi__xfer.md#afa30e0fac32c6c3e7a3c9d7e29ccc8cb)

enum mspi\_xfer\_mode xfer\_mode

Transfer Mode.

**Definition** mspi.h:391

[mspi\_xfer::timeout](structmspi__xfer.md#afd83aa864cf300e9848ef46b7331ca5a)

uint32\_t timeout

Transfer timeout value.

**Definition** mspi.h:413

[mspi\_xip\_cfg](structmspi__xip__cfg.md)

MSPI controller XIP configuration.

**Definition** mspi.h:306

[mspi\_xip\_cfg::permission](structmspi__xip__cfg.md#a172af688c9f92af04978559697fe230f)

enum mspi\_xip\_permit permission

XIP access permission.

**Definition** mspi.h:316

[mspi\_xip\_cfg::enable](structmspi__xip__cfg.md#a2ba9873d13a24b5fa42d28e910368486)

bool enable

XIP enable.

**Definition** mspi.h:308

[mspi\_xip\_cfg::address\_offset](structmspi__xip__cfg.md#a58c0c05d4fc58704b8b46677b468247c)

uint32\_t address\_offset

XIP region start address = hardware default + address offset.

**Definition** mspi.h:312

[mspi\_xip\_cfg::size](structmspi__xip__cfg.md#ac393537eb1a209e1c1e41bf639782e72)

uint32\_t size

XIP region size.

**Definition** mspi.h:314

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mspi.h](mspi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
