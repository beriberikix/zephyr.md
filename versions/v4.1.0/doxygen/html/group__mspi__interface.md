---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mspi__interface.html
original_path: doxygen/html/group__mspi__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MSPI Driver APIs

[Device Driver APIs](group__io__interfaces.md)

MSPI Driver APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [MSPI Configure API](group__mspi__configure__api.md) |
|  | MSPI Configure API. |
|  | [MSPI Transfer API](group__mspi__transfer__api.md) |
|  | MSPI Transfer API. |
|  | [MSPI callback API](group__mspi__callback__api.md) |
|  | MSPI callback API. |

| Data Structures | |
| --- | --- |
| struct | [mspi\_driver\_api](structmspi__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [mspi\_api\_config](#ga2ff9209634fb241e2f7323e749df612e)) (const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \*spec) |
|  | MSPI driver API definition and system call entry points. |
| typedef int(\* | [mspi\_api\_dev\_config](#ga7e3bae501067b045e9ed8d0efbe6e61d)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_dev\_cfg\_mask](#ga71c447d059acf7a8055c380243f3a647) param\_mask, const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \*cfg) |
| typedef int(\* | [mspi\_api\_get\_channel\_status](#gadd66b118b76a4ee7ef252afc6b830bfa)) (const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ch) |
| typedef int(\* | [mspi\_api\_transceive](#ga17b551f4d9f980fde8eabcaae3318617)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xfer](structmspi__xfer.md) \*req) |
| typedef int(\* | [mspi\_api\_register\_callback](#gad6d65ef0d523f22592ff17c04698f663)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_bus\_event](#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type, [mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4) cb, struct [mspi\_callback\_context](structmspi__callback__context.md) \*ctx) |
| typedef int(\* | [mspi\_api\_xip\_config](#ga823ad87bec1c73ee110f3ae8107d03e7)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \*xip\_cfg) |
| typedef int(\* | [mspi\_api\_scramble\_config](#ga092c8bb0879977a8cc8eea5d1662c34b)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \*scramble\_cfg) |
| typedef int(\* | [mspi\_api\_timing\_config](#ga407713e07f23756564814402342c9c97)) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param\_mask, void \*timing\_cfg) |

| Enumerations | |
| --- | --- |
| enum | [mspi\_op\_mode](#ga3f211cd81e05cb9ee073a2722f6b22d8) { [MSPI\_OP\_MODE\_CONTROLLER](#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a) = 0 , [MSPI\_OP\_MODE\_PERIPHERAL](#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83) = 1 } |
|  | MSPI operational mode. [More...](#ga3f211cd81e05cb9ee073a2722f6b22d8) |
| enum | [mspi\_duplex](#ga20e348d7a9f1f9b32078a3bf6c4e82b9) { [MSPI\_HALF\_DUPLEX](#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3) = 0 , [MSPI\_FULL\_DUPLEX](#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c) = 1 } |
|  | MSPI duplex mode. [More...](#ga20e348d7a9f1f9b32078a3bf6c4e82b9) |
| enum | [mspi\_io\_mode](#ga904dfc1c800fb9832f7c6200f767f9a5) {     [MSPI\_IO\_MODE\_SINGLE](#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd) = 0 , [MSPI\_IO\_MODE\_DUAL](#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673) = 1 , [MSPI\_IO\_MODE\_DUAL\_1\_1\_2](#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da) = 2 , [MSPI\_IO\_MODE\_DUAL\_1\_2\_2](#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663) = 3 ,     [MSPI\_IO\_MODE\_QUAD](#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a) = 4 , [MSPI\_IO\_MODE\_QUAD\_1\_1\_4](#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a) = 5 , [MSPI\_IO\_MODE\_QUAD\_1\_4\_4](#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a) = 6 , [MSPI\_IO\_MODE\_OCTAL](#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725) = 7 ,     [MSPI\_IO\_MODE\_OCTAL\_1\_1\_8](#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf) = 8 , [MSPI\_IO\_MODE\_OCTAL\_1\_8\_8](#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573) = 9 , [MSPI\_IO\_MODE\_HEX](#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b) = 10 , [MSPI\_IO\_MODE\_HEX\_8\_8\_16](#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02) = 11 ,     [MSPI\_IO\_MODE\_HEX\_8\_16\_16](#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa) = 12 , [MSPI\_IO\_MODE\_MAX](#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb)   } |
|  | MSPI I/O mode capabilities Postfix like 1\_4\_4 stands for the number of lines used for command, address and data phases. [More...](#ga904dfc1c800fb9832f7c6200f767f9a5) |
| enum | [mspi\_data\_rate](#gaa2131d9846bbfd74488a6ae1c2003e68) {     [MSPI\_DATA\_RATE\_SINGLE](#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0) = 0 , [MSPI\_DATA\_RATE\_S\_S\_D](#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39) = 1 , [MSPI\_DATA\_RATE\_S\_D\_D](#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984) = 2 , [MSPI\_DATA\_RATE\_DUAL](#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc) = 3 ,     [MSPI\_DATA\_RATE\_MAX](#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9)   } |
|  | MSPI data rate capabilities SINGLE stands for single data rate for all phases. [More...](#gaa2131d9846bbfd74488a6ae1c2003e68) |
| enum | [mspi\_cpp\_mode](#ga704e4d3759d3261b4468e9d9900e578c) { [MSPI\_CPP\_MODE\_0](#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90) = 0 , [MSPI\_CPP\_MODE\_1](#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870) = 1 , [MSPI\_CPP\_MODE\_2](#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705) = 2 , [MSPI\_CPP\_MODE\_3](#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48) = 3 } |
|  | MSPI Polarity & Phase Modes. [More...](#ga704e4d3759d3261b4468e9d9900e578c) |
| enum | [mspi\_endian](#ga3625cde1379e66cb66a8cb3803ab2e44) { [MSPI\_XFER\_LITTLE\_ENDIAN](#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345) = 0 , [MSPI\_XFER\_BIG\_ENDIAN](#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d) = 1 } |
|  | MSPI Endian. [More...](#ga3625cde1379e66cb66a8cb3803ab2e44) |
| enum | [mspi\_ce\_polarity](#ga283275f86fe186f4b5e30110ae0d506b) { [MSPI\_CE\_ACTIVE\_LOW](#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae) = 0 , [MSPI\_CE\_ACTIVE\_HIGH](#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22) = 1 } |
|  | MSPI chip enable polarity. [More...](#ga283275f86fe186f4b5e30110ae0d506b) |
| enum | [mspi\_bus\_event](#ga4cd05950729893e08ef0d4a12e2242d5) { [MSPI\_BUS\_RESET](#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64) = 0 , [MSPI\_BUS\_ERROR](#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0) = 1 , [MSPI\_BUS\_XFER\_COMPLETE](#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61) = 2 , [MSPI\_BUS\_EVENT\_MAX](#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a) } |
|  | MSPI bus event. [More...](#ga4cd05950729893e08ef0d4a12e2242d5) |
| enum | [mspi\_bus\_event\_cb\_mask](#gab33e9840b0937c944f4e1a2525534cb1) { [MSPI\_BUS\_NO\_CB](#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277) = 0 , [MSPI\_BUS\_RESET\_CB](#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1) = BIT(0) , [MSPI\_BUS\_ERROR\_CB](#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498) = BIT(1) , [MSPI\_BUS\_XFER\_COMPLETE\_CB](#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7) = BIT(2) } |
|  | MSPI bus event callback mask This is a preliminary list same as [mspi\_bus\_event](#ga4cd05950729893e08ef0d4a12e2242d5). [More...](#gab33e9840b0937c944f4e1a2525534cb1) |
| enum | [mspi\_xfer\_mode](#ga116259bbb1d12a10c2ba9e6051f2f000) { [MSPI\_PIO](#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1) , [MSPI\_DMA](#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8) } |
|  | MSPI transfer modes. [More...](#ga116259bbb1d12a10c2ba9e6051f2f000) |
| enum | [mspi\_xfer\_direction](#ga498f10591acf5dc7ec88e0aa98e537d6) { [MSPI\_RX](#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541) , [MSPI\_TX](#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a) } |
|  | MSPI transfer directions. [More...](#ga498f10591acf5dc7ec88e0aa98e537d6) |
| enum | [mspi\_dev\_cfg\_mask](#ga71c447d059acf7a8055c380243f3a647) {     [MSPI\_DEVICE\_CONFIG\_NONE](#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878) = 0 , [MSPI\_DEVICE\_CONFIG\_CE\_NUM](#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2) = BIT(0) , [MSPI\_DEVICE\_CONFIG\_FREQUENCY](#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809) = BIT(1) , [MSPI\_DEVICE\_CONFIG\_IO\_MODE](#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f) = BIT(2) ,     [MSPI\_DEVICE\_CONFIG\_DATA\_RATE](#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9) = BIT(3) , [MSPI\_DEVICE\_CONFIG\_CPP](#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65) = BIT(4) , [MSPI\_DEVICE\_CONFIG\_ENDIAN](#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca) = BIT(5) , [MSPI\_DEVICE\_CONFIG\_CE\_POL](#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b) = BIT(6) ,     [MSPI\_DEVICE\_CONFIG\_DQS](#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537) = BIT(7) , [MSPI\_DEVICE\_CONFIG\_RX\_DUMMY](#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a) = BIT(8) , [MSPI\_DEVICE\_CONFIG\_TX\_DUMMY](#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5) = BIT(9) , [MSPI\_DEVICE\_CONFIG\_READ\_CMD](#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872) = BIT(10) ,     [MSPI\_DEVICE\_CONFIG\_WRITE\_CMD](#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b) = BIT(11) , [MSPI\_DEVICE\_CONFIG\_CMD\_LEN](#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac) = BIT(12) , [MSPI\_DEVICE\_CONFIG\_ADDR\_LEN](#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b) = BIT(13) , [MSPI\_DEVICE\_CONFIG\_MEM\_BOUND](#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946) = BIT(14) ,     [MSPI\_DEVICE\_CONFIG\_BREAK\_TIME](#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120) = BIT(15) , [MSPI\_DEVICE\_CONFIG\_ALL](#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489) = BIT\_MASK(16)   } |
|  | MSPI controller device specific configuration mask. [More...](#ga71c447d059acf7a8055c380243f3a647) |
| enum | [mspi\_xip\_permit](#ga006a1e32778a02299b3500886bb194fa) { [MSPI\_XIP\_READ\_WRITE](#gga006a1e32778a02299b3500886bb194faa431525f8be52537b0a831f522726c7b9) = 0 , [MSPI\_XIP\_READ\_ONLY](#gga006a1e32778a02299b3500886bb194faae9b2d08d8ae1722c3014a706fc801731) = 1 } |
|  | MSPI XIP access permissions. [More...](#ga006a1e32778a02299b3500886bb194fa) |

## Detailed Description

MSPI Driver APIs.

## Typedef Documentation

## [◆ ](#ga2ff9209634fb241e2f7323e749df612e)mspi\_api\_config

| typedef int(\* mspi\_api\_config) (const struct [mspi\_dt\_spec](structmspi__dt__spec.md) \*spec) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI driver API definition and system call entry points.

## [◆ ](#ga7e3bae501067b045e9ed8d0efbe6e61d)mspi\_api\_dev\_config

| typedef int(\* mspi\_api\_dev\_config) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_dev\_cfg\_mask](#ga71c447d059acf7a8055c380243f3a647) param\_mask, const struct [mspi\_dev\_cfg](structmspi__dev__cfg.md) \*cfg) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

## [◆ ](#gadd66b118b76a4ee7ef252afc6b830bfa)mspi\_api\_get\_channel\_status

| typedef int(\* mspi\_api\_get\_channel\_status) (const struct [device](structdevice.md) \*controller, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ch) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

## [◆ ](#gad6d65ef0d523f22592ff17c04698f663)mspi\_api\_register\_callback

| typedef int(\* mspi\_api\_register\_callback) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const enum [mspi\_bus\_event](#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type, [mspi\_callback\_handler\_t](group__mspi__callback__api.md#ga29421f748fdb89c823e1a48ff69cf0f4) cb, struct [mspi\_callback\_context](structmspi__callback__context.md) \*ctx) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

## [◆ ](#ga092c8bb0879977a8cc8eea5d1662c34b)mspi\_api\_scramble\_config

| typedef int(\* mspi\_api\_scramble\_config) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_scramble\_cfg](structmspi__scramble__cfg.md) \*scramble\_cfg) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

## [◆ ](#ga407713e07f23756564814402342c9c97)mspi\_api\_timing\_config

| typedef int(\* mspi\_api\_timing\_config) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) param\_mask, void \*timing\_cfg) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

## [◆ ](#ga17b551f4d9f980fde8eabcaae3318617)mspi\_api\_transceive

| typedef int(\* mspi\_api\_transceive) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xfer](structmspi__xfer.md) \*req) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

## [◆ ](#ga823ad87bec1c73ee110f3ae8107d03e7)mspi\_api\_xip\_config

| typedef int(\* mspi\_api\_xip\_config) (const struct [device](structdevice.md) \*controller, const struct [mspi\_dev\_id](structmspi__dev__id.md) \*dev\_id, const struct [mspi\_xip\_cfg](structmspi__xip__cfg.md) \*xip\_cfg) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga4cd05950729893e08ef0d4a12e2242d5)mspi\_bus\_event

| enum [mspi\_bus\_event](#ga4cd05950729893e08ef0d4a12e2242d5) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI bus event.

This is a preliminary list of events. I encourage the community to fill it up.

| Enumerator | |
| --- | --- |
| MSPI\_BUS\_RESET |  |
| MSPI\_BUS\_ERROR |  |
| MSPI\_BUS\_XFER\_COMPLETE |  |
| MSPI\_BUS\_EVENT\_MAX |  |

## [◆ ](#gab33e9840b0937c944f4e1a2525534cb1)mspi\_bus\_event\_cb\_mask

| enum [mspi\_bus\_event\_cb\_mask](#gab33e9840b0937c944f4e1a2525534cb1) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI bus event callback mask This is a preliminary list same as [mspi\_bus\_event](#ga4cd05950729893e08ef0d4a12e2242d5).

I encourage the community to fill it up.

| Enumerator | |
| --- | --- |
| MSPI\_BUS\_NO\_CB |  |
| MSPI\_BUS\_RESET\_CB |  |
| MSPI\_BUS\_ERROR\_CB |  |
| MSPI\_BUS\_XFER\_COMPLETE\_CB |  |

## [◆ ](#ga283275f86fe186f4b5e30110ae0d506b)mspi\_ce\_polarity

| enum [mspi\_ce\_polarity](#ga283275f86fe186f4b5e30110ae0d506b) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI chip enable polarity.

| Enumerator | |
| --- | --- |
| MSPI\_CE\_ACTIVE\_LOW |  |
| MSPI\_CE\_ACTIVE\_HIGH |  |

## [◆ ](#ga704e4d3759d3261b4468e9d9900e578c)mspi\_cpp\_mode

| enum [mspi\_cpp\_mode](#ga704e4d3759d3261b4468e9d9900e578c) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI Polarity & Phase Modes.

| Enumerator | |
| --- | --- |
| MSPI\_CPP\_MODE\_0 |  |
| MSPI\_CPP\_MODE\_1 |  |
| MSPI\_CPP\_MODE\_2 |  |
| MSPI\_CPP\_MODE\_3 |  |

## [◆ ](#gaa2131d9846bbfd74488a6ae1c2003e68)mspi\_data\_rate

| enum [mspi\_data\_rate](#gaa2131d9846bbfd74488a6ae1c2003e68) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI data rate capabilities SINGLE stands for single data rate for all phases.

DUAL stands for dual data rate for all phases. S\_S\_D stands for single data rate for command and address phases but dual data rate for data phase. S\_D\_D stands for single data rate for command phase but dual data rate for address and data phases.

| Enumerator | |
| --- | --- |
| MSPI\_DATA\_RATE\_SINGLE |  |
| MSPI\_DATA\_RATE\_S\_S\_D |  |
| MSPI\_DATA\_RATE\_S\_D\_D |  |
| MSPI\_DATA\_RATE\_DUAL |  |
| MSPI\_DATA\_RATE\_MAX |  |

## [◆ ](#ga71c447d059acf7a8055c380243f3a647)mspi\_dev\_cfg\_mask

| enum [mspi\_dev\_cfg\_mask](#ga71c447d059acf7a8055c380243f3a647) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI controller device specific configuration mask.

| Enumerator | |
| --- | --- |
| MSPI\_DEVICE\_CONFIG\_NONE |  |
| MSPI\_DEVICE\_CONFIG\_CE\_NUM |  |
| MSPI\_DEVICE\_CONFIG\_FREQUENCY |  |
| MSPI\_DEVICE\_CONFIG\_IO\_MODE |  |
| MSPI\_DEVICE\_CONFIG\_DATA\_RATE |  |
| MSPI\_DEVICE\_CONFIG\_CPP |  |
| MSPI\_DEVICE\_CONFIG\_ENDIAN |  |
| MSPI\_DEVICE\_CONFIG\_CE\_POL |  |
| MSPI\_DEVICE\_CONFIG\_DQS |  |
| MSPI\_DEVICE\_CONFIG\_RX\_DUMMY |  |
| MSPI\_DEVICE\_CONFIG\_TX\_DUMMY |  |
| MSPI\_DEVICE\_CONFIG\_READ\_CMD |  |
| MSPI\_DEVICE\_CONFIG\_WRITE\_CMD |  |
| MSPI\_DEVICE\_CONFIG\_CMD\_LEN |  |
| MSPI\_DEVICE\_CONFIG\_ADDR\_LEN |  |
| MSPI\_DEVICE\_CONFIG\_MEM\_BOUND |  |
| MSPI\_DEVICE\_CONFIG\_BREAK\_TIME |  |
| MSPI\_DEVICE\_CONFIG\_ALL |  |

## [◆ ](#ga20e348d7a9f1f9b32078a3bf6c4e82b9)mspi\_duplex

| enum [mspi\_duplex](#ga20e348d7a9f1f9b32078a3bf6c4e82b9) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI duplex mode.

| Enumerator | |
| --- | --- |
| MSPI\_HALF\_DUPLEX |  |
| MSPI\_FULL\_DUPLEX |  |

## [◆ ](#ga3625cde1379e66cb66a8cb3803ab2e44)mspi\_endian

| enum [mspi\_endian](#ga3625cde1379e66cb66a8cb3803ab2e44) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI Endian.

| Enumerator | |
| --- | --- |
| MSPI\_XFER\_LITTLE\_ENDIAN |  |
| MSPI\_XFER\_BIG\_ENDIAN |  |

## [◆ ](#ga904dfc1c800fb9832f7c6200f767f9a5)mspi\_io\_mode

| enum [mspi\_io\_mode](#ga904dfc1c800fb9832f7c6200f767f9a5) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI I/O mode capabilities Postfix like 1\_4\_4 stands for the number of lines used for command, address and data phases.

Mode with no postfix has the same number of lines for all phases.

| Enumerator | |
| --- | --- |
| MSPI\_IO\_MODE\_SINGLE |  |
| MSPI\_IO\_MODE\_DUAL |  |
| MSPI\_IO\_MODE\_DUAL\_1\_1\_2 |  |
| MSPI\_IO\_MODE\_DUAL\_1\_2\_2 |  |
| MSPI\_IO\_MODE\_QUAD |  |
| MSPI\_IO\_MODE\_QUAD\_1\_1\_4 |  |
| MSPI\_IO\_MODE\_QUAD\_1\_4\_4 |  |
| MSPI\_IO\_MODE\_OCTAL |  |
| MSPI\_IO\_MODE\_OCTAL\_1\_1\_8 |  |
| MSPI\_IO\_MODE\_OCTAL\_1\_8\_8 |  |
| MSPI\_IO\_MODE\_HEX |  |
| MSPI\_IO\_MODE\_HEX\_8\_8\_16 |  |
| MSPI\_IO\_MODE\_HEX\_8\_16\_16 |  |
| MSPI\_IO\_MODE\_MAX |  |

## [◆ ](#ga3f211cd81e05cb9ee073a2722f6b22d8)mspi\_op\_mode

| enum [mspi\_op\_mode](#ga3f211cd81e05cb9ee073a2722f6b22d8) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI operational mode.

| Enumerator | |
| --- | --- |
| MSPI\_OP\_MODE\_CONTROLLER |  |
| MSPI\_OP\_MODE\_PERIPHERAL |  |

## [◆ ](#ga498f10591acf5dc7ec88e0aa98e537d6)mspi\_xfer\_direction

| enum [mspi\_xfer\_direction](#ga498f10591acf5dc7ec88e0aa98e537d6) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI transfer directions.

| Enumerator | |
| --- | --- |
| MSPI\_RX |  |
| MSPI\_TX |  |

## [◆ ](#ga116259bbb1d12a10c2ba9e6051f2f000)mspi\_xfer\_mode

| enum [mspi\_xfer\_mode](#ga116259bbb1d12a10c2ba9e6051f2f000) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI transfer modes.

| Enumerator | |
| --- | --- |
| MSPI\_PIO |  |
| MSPI\_DMA |  |

## [◆ ](#ga006a1e32778a02299b3500886bb194fa)mspi\_xip\_permit

| enum [mspi\_xip\_permit](#ga006a1e32778a02299b3500886bb194fa) |
| --- |

`#include <[mspi.h](mspi_8h.md)>`

MSPI XIP access permissions.

| Enumerator | |
| --- | --- |
| MSPI\_XIP\_READ\_WRITE |  |
| MSPI\_XIP\_READ\_ONLY |  |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
