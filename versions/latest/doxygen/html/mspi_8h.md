---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mspi_8h.html
original_path: doxygen/html/mspi_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi.h File Reference

Public APIs for MSPI driver.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`  
`#include <[zephyr/drivers/mspi/devicetree.h](drivers_2mspi_2devicetree_8h_source.md)>`  
`#include <zephyr/syscalls/mspi.h>`

[Go to the source code of this file.](mspi_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mspi\_timing\_cfg](structmspi__timing__cfg.md) |
|  | Stub for struct timing\_cfg. [More...](structmspi__timing__cfg.md#details) |
| struct | [mspi\_dev\_id](structmspi__dev__id.md) |
|  | MSPI device ID The controller can identify its devices and determine whether the access is allowed in a multiple device scheme. [More...](structmspi__dev__id.md#details) |
| struct | [mspi\_cfg](structmspi__cfg.md) |
|  | MSPI controller configuration. [More...](structmspi__cfg.md#details) |
| struct | [mspi\_dt\_spec](structmspi__dt__spec.md) |
|  | MSPI DT information. [More...](structmspi__dt__spec.md#details) |
| struct | [mspi\_dev\_cfg](structmspi__dev__cfg.md) |
|  | MSPI controller device specific configuration. [More...](structmspi__dev__cfg.md#details) |
| struct | [mspi\_xip\_cfg](structmspi__xip__cfg.md) |
|  | MSPI controller XIP configuration. [More...](structmspi__xip__cfg.md#details) |
| struct | [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) |
|  | MSPI controller scramble configuration. [More...](structmspi__scramble__cfg.md#details) |
| struct | [mspi\_ce\_control](structmspi__ce__control.md) |
|  | MSPI Chip Select control structure. [More...](structmspi__ce__control.md#details) |
| struct | [mspi\_xfer\_packet](structmspi__xfer__packet.md) |
|  | MSPI peripheral xfer packet format. [More...](structmspi__xfer__packet.md#details) |
| struct | [mspi\_xfer](structmspi__xfer.md) |
|  | MSPI peripheral xfer format This includes transfer related settings that may require configuring the hardware. [More...](structmspi__xfer.md#details) |
| struct | [mspi\_event\_data](structmspi__event__data.md) |
|  | MSPI event data. [More...](structmspi__event__data.md#details) |
| struct | [mspi\_event](structmspi__event.md) |
|  | MSPI event. [More...](structmspi__event.md#details) |
| struct | [mspi\_callback\_context](structmspi__callback__context.md) |
|  | MSPI callback context. [More...](structmspi__callback__context.md#details) |
| struct | [mspi\_driver\_api](structmspi__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4)) (struct [mspi\_callback\_context](structmspi__callback__context.md) \*mspi\_cb\_ctx,...) |
|  | Define the application callback handler function signature. |
| typedef int(\* | [mspi\_api\_config](group__mspi__interface.md#ga2ff9209634fb241e2f7323e749df612e)) (const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \*spec) |
|  | MSPI driver API definition and system call entry points. |
| typedef int(\* | [mspi\_api\_dev\_config](group__mspi__interface.md#ga7e3bae501067b045e9ed8d0efbe6e61d)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) param\_mask, const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \*cfg) |
| typedef int(\* | [mspi\_api\_get\_channel\_status](group__mspi__interface.md#gadd66b118b76a4ee7ef252afc6b830bfa)) (const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ch) |
| typedef int(\* | [mspi\_api\_transceive](group__mspi__interface.md#ga17b551f4d9f980fde8eabcaae3318617)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xfer](structmspi__xfer.md) \*req) |
| typedef int(\* | [mspi\_api\_register\_callback](group__mspi__interface.md#gad6d65ef0d523f22592ff17c04698f663)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type, [mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4) cb, struct [mspi\_callback\_context](structmspi__callback__context.md) \*ctx) |
| typedef int(\* | [mspi\_api\_xip\_config](group__mspi__interface.md#ga823ad87bec1c73ee110f3ae8107d03e7)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \*xip\_cfg) |
| typedef int(\* | [mspi\_api\_scramble\_config](group__mspi__interface.md#ga092c8bb0879977a8cc8eea5d1662c34b)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \*scramble\_cfg) |
| typedef int(\* | [mspi\_api\_timing\_config](group__mspi__interface.md#ga407713e07f23756564814402342c9c97)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param\_mask, void \*timing\_cfg) |

| Enumerations | |
| --- | --- |
| enum | [mspi\_op\_mode](group__mspi__interface.md#ga3f211cd81e05cb9ee073a2722f6b22d8) { [MSPI\_OP\_MODE\_CONTROLLER](group__mspi__interface.md#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a) = 0 , [MSPI\_OP\_MODE\_PERIPHERAL](group__mspi__interface.md#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83) = 1 } |
|  | MSPI operational mode. [More...](group__mspi__interface.md#ga3f211cd81e05cb9ee073a2722f6b22d8) |
| enum | [mspi\_duplex](group__mspi__interface.md#ga20e348d7a9f1f9b32078a3bf6c4e82b9) { [MSPI\_HALF\_DUPLEX](group__mspi__interface.md#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3) = 0 , [MSPI\_FULL\_DUPLEX](group__mspi__interface.md#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c) = 1 } |
|  | MSPI duplex mode. [More...](group__mspi__interface.md#ga20e348d7a9f1f9b32078a3bf6c4e82b9) |
| enum | [mspi\_io\_mode](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5) {     [MSPI\_IO\_MODE\_SINGLE](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd) = 0 , [MSPI\_IO\_MODE\_DUAL](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673) = 1 , [MSPI\_IO\_MODE\_DUAL\_1\_1\_2](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da) = 2 , [MSPI\_IO\_MODE\_DUAL\_1\_2\_2](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663) = 3 ,     [MSPI\_IO\_MODE\_QUAD](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a) = 4 , [MSPI\_IO\_MODE\_QUAD\_1\_1\_4](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a) = 5 , [MSPI\_IO\_MODE\_QUAD\_1\_4\_4](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a) = 6 , [MSPI\_IO\_MODE\_OCTAL](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725) = 7 ,     [MSPI\_IO\_MODE\_OCTAL\_1\_1\_8](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf) = 8 , [MSPI\_IO\_MODE\_OCTAL\_1\_8\_8](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573) = 9 , [MSPI\_IO\_MODE\_HEX](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b) = 10 , [MSPI\_IO\_MODE\_HEX\_8\_8\_16](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02) = 11 ,     [MSPI\_IO\_MODE\_HEX\_8\_16\_16](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa) = 12 , [MSPI\_IO\_MODE\_MAX](group__mspi__interface.md#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb)   } |
|  | MSPI I/O mode capabilities Postfix like 1\_4\_4 stands for the number of lines used for command, address and data phases. [More...](group__mspi__interface.md#ga904dfc1c800fb9832f7c6200f767f9a5) |
| enum | [mspi\_data\_rate](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68) {     [MSPI\_DATA\_RATE\_SINGLE](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0) = 0 , [MSPI\_DATA\_RATE\_S\_S\_D](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39) = 1 , [MSPI\_DATA\_RATE\_S\_D\_D](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984) = 2 , [MSPI\_DATA\_RATE\_DUAL](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc) = 3 ,     [MSPI\_DATA\_RATE\_MAX](group__mspi__interface.md#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9)   } |
|  | MSPI data rate capabilities SINGLE stands for single data rate for all phases. [More...](group__mspi__interface.md#gaa2131d9846bbfd74488a6ae1c2003e68) |
| enum | [mspi\_cpp\_mode](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c) { [MSPI\_CPP\_MODE\_0](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90) = 0 , [MSPI\_CPP\_MODE\_1](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870) = 1 , [MSPI\_CPP\_MODE\_2](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705) = 2 , [MSPI\_CPP\_MODE\_3](group__mspi__interface.md#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48) = 3 } |
|  | MSPI Polarity & Phase Modes. [More...](group__mspi__interface.md#ga704e4d3759d3261b4468e9d9900e578c) |
| enum | [mspi\_endian](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44) { [MSPI\_XFER\_LITTLE\_ENDIAN](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345) = 0 , [MSPI\_XFER\_BIG\_ENDIAN](group__mspi__interface.md#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d) = 1 } |
|  | MSPI Endian. [More...](group__mspi__interface.md#ga3625cde1379e66cb66a8cb3803ab2e44) |
| enum | [mspi\_ce\_polarity](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b) { [MSPI\_CE\_ACTIVE\_LOW](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae) = 0 , [MSPI\_CE\_ACTIVE\_HIGH](group__mspi__interface.md#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22) = 1 } |
|  | MSPI chip enable polarity. [More...](group__mspi__interface.md#ga283275f86fe186f4b5e30110ae0d506b) |
| enum | [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) { [MSPI\_BUS\_RESET](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64) = 0 , [MSPI\_BUS\_ERROR](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0) = 1 , [MSPI\_BUS\_XFER\_COMPLETE](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61) = 2 , [MSPI\_BUS\_EVENT\_MAX](group__mspi__interface.md#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a) } |
|  | MSPI bus event. [More...](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) |
| enum | [mspi\_bus\_event\_cb\_mask](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1) { [MSPI\_BUS\_NO\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277) = 0 , [MSPI\_BUS\_RESET\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1) = BIT(0) , [MSPI\_BUS\_ERROR\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498) = BIT(1) , [MSPI\_BUS\_XFER\_COMPLETE\_CB](group__mspi__interface.md#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7) = BIT(2) } |
|  | MSPI bus event callback mask This is a preliminary list same as [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5 "MSPI bus event."). [More...](group__mspi__interface.md#gab33e9840b0937c944f4e1a2525534cb1) |
| enum | [mspi\_xfer\_mode](group__mspi__interface.md#ga116259bbb1d12a10c2ba9e6051f2f000) { [MSPI\_PIO](group__mspi__interface.md#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1) , [MSPI\_DMA](group__mspi__interface.md#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8) } |
|  | MSPI transfer modes. [More...](group__mspi__interface.md#ga116259bbb1d12a10c2ba9e6051f2f000) |
| enum | [mspi\_xfer\_direction](group__mspi__interface.md#ga498f10591acf5dc7ec88e0aa98e537d6) { [MSPI\_RX](group__mspi__interface.md#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541) , [MSPI\_TX](group__mspi__interface.md#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a) } |
|  | MSPI transfer directions. [More...](group__mspi__interface.md#ga498f10591acf5dc7ec88e0aa98e537d6) |
| enum | [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) {     [MSPI\_DEVICE\_CONFIG\_NONE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878) = 0 , [MSPI\_DEVICE\_CONFIG\_CE\_NUM](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2) = BIT(0) , [MSPI\_DEVICE\_CONFIG\_FREQUENCY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809) = BIT(1) , [MSPI\_DEVICE\_CONFIG\_IO\_MODE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f) = BIT(2) ,     [MSPI\_DEVICE\_CONFIG\_DATA\_RATE](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9) = BIT(3) , [MSPI\_DEVICE\_CONFIG\_CPP](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65) = BIT(4) , [MSPI\_DEVICE\_CONFIG\_ENDIAN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca) = BIT(5) , [MSPI\_DEVICE\_CONFIG\_CE\_POL](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b) = BIT(6) ,     [MSPI\_DEVICE\_CONFIG\_DQS](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537) = BIT(7) , [MSPI\_DEVICE\_CONFIG\_RX\_DUMMY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a) = BIT(8) , [MSPI\_DEVICE\_CONFIG\_TX\_DUMMY](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5) = BIT(9) , [MSPI\_DEVICE\_CONFIG\_READ\_CMD](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872) = BIT(10) ,     [MSPI\_DEVICE\_CONFIG\_WRITE\_CMD](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b) = BIT(11) , [MSPI\_DEVICE\_CONFIG\_CMD\_LEN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac) = BIT(12) , [MSPI\_DEVICE\_CONFIG\_ADDR\_LEN](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b) = BIT(13) , [MSPI\_DEVICE\_CONFIG\_MEM\_BOUND](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946) = BIT(14) ,     [MSPI\_DEVICE\_CONFIG\_BREAK\_TIME](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120) = BIT(15) , [MSPI\_DEVICE\_CONFIG\_ALL](group__mspi__interface.md#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489) = BIT\_MASK(16)   } |
|  | MSPI controller device specific configuration mask. [More...](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) |
| enum | [mspi\_xip\_permit](group__mspi__interface.md#ga006a1e32778a02299b3500886bb194fa) { [MSPI\_XIP\_READ\_WRITE](group__mspi__interface.md#gga006a1e32778a02299b3500886bb194faa431525f8be52537b0a831f522726c7b9) = 0 , [MSPI\_XIP\_READ\_ONLY](group__mspi__interface.md#gga006a1e32778a02299b3500886bb194faae9b2d08d8ae1722c3014a706fc801731) = 1 } |
|  | MSPI XIP access permissions. [More...](group__mspi__interface.md#ga006a1e32778a02299b3500886bb194fa) |
| enum | [mspi\_timing\_param](group__mspi__configure__api.md#gaa25a7f97ab3437d4544832a0e7474f4a) { [MSPI\_TIMING\_PARAM\_DUMMY](group__mspi__configure__api.md#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237) } |
|  | Stub for timing parameter. [More...](group__mspi__configure__api.md#gaa25a7f97ab3437d4544832a0e7474f4a) |

| Functions | |
| --- | --- |
| int | [mspi\_config](group__mspi__configure__api.md#ga46c2b98e99ecea045c1ecac4bdf3f087) (const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \*spec) |
|  | Configure a MSPI controller. |
| int | [mspi\_dev\_config](group__mspi__configure__api.md#gaa3c1eae8b3000c9bafcc26f14a8beb8b) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_dev\_cfg\_mask](group__mspi__interface.md#ga71c447d059acf7a8055c380243f3a647) param\_mask, const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \*cfg) |
|  | Configure a MSPI controller with device specific parameters. |
| int | [mspi\_get\_channel\_status](group__mspi__configure__api.md#ga957b6ecd96c9f942f75bbe500898930d) (const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ch) |
|  | Query to see if it a channel is ready. |
| int | [mspi\_transceive](group__mspi__transfer__api.md#ga8c98c73e322c575b759ce911cc115129) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xfer](structmspi__xfer.md) \*req) |
|  | Transfer request over MSPI. |
| int | [mspi\_xip\_config](group__mspi__configure__api.md#gab9d9104636d3c8167b5876b1bc4348ea) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \*cfg) |
|  | Configure a MSPI XIP settings. |
| int | [mspi\_scramble\_config](group__mspi__configure__api.md#gacf287e08b6ce4898524884e8de22b806) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \*cfg) |
|  | Configure a MSPI scrambling settings. |
| int | [mspi\_timing\_config](group__mspi__configure__api.md#gaff82af1cfc99b9e78cec17ea27f79ab6) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param\_mask, void \*cfg) |
|  | Configure a MSPI timing settings. |
| static int | [mspi\_register\_callback](group__mspi__callback__api.md#ga967f5fed63f08ac2d5a88625b030cd14) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type, [mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4) cb, struct [mspi\_callback\_context](structmspi__callback__context.md) \*ctx) |
|  | Register the mspi callback functions. |

## Detailed Description

Public APIs for MSPI driver.

Since
:   3.7

Version
:   0.1.0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mspi.h](mspi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
