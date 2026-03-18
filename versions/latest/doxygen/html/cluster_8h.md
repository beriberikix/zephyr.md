---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cluster_8h.html
original_path: doxygen/html/cluster_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cluster.h File Reference

ARC Cluster registers and accessors.
[More...](#details)

`#include <[zephyr/arch/arc/v2/aux_regs.h](aux__regs_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](cluster_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARC\_CLN\_MST\_NOC\_0\_BCR](#ae8548b32fefa14c8ee8b2df215bcde8a)   0 |
| #define | [ARC\_CLN\_MST\_NOC\_1\_BCR](#a7b9948865accce27b428ab101d4f7488)   1 |
| #define | [ARC\_CLN\_MST\_NOC\_2\_BCR](#af8bb48bfd94941b91441f8fab7e26b39)   2 |
| #define | [ARC\_CLN\_MST\_NOC\_3\_BCR](#a5ec102830a019fd6b9eff79c1fc64a9c)   3 |
| #define | [ARC\_CLN\_MST\_PER\_0\_BCR](#a4a990ce76f504e654ef3ac5fd8f7213a)   16 |
| #define | [ARC\_CLN\_MST\_PER\_1\_BCR](#a669fcee44d5ac869dc49776bb6984724)   17 |
| #define | [ARC\_CLN\_PER\_0\_BASE](#a2e148f6cb243a4e98bbac15e91a08bca)   2688 |
| #define | [ARC\_CLN\_PER\_0\_SIZE](#a80b5165ddda4c428344f008886389779)   2689 |
| #define | [ARC\_CLN\_PER\_1\_BASE](#a45ed0679d4903c9ad3cae818ea69ded7)   2690 |
| #define | [ARC\_CLN\_PER\_1\_SIZE](#ac5a80d92726f545edd24586c7e9e537e)   2691 |
| #define | [ARC\_CLN\_SCM\_BCR\_0](#acd23250017388ccdc6c4d29937fd6a32)   100 |
| #define | [ARC\_CLN\_SCM\_BCR\_1](#aa81707d4070e08efea3a7d602611fb18)   101 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_0\_ADDR](#af50cee9c1dd5c1b68f98704f5cfb528a)   292 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_0\_SIZE](#ae41dbdd46df7733240048b55815ba654)   293 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_1\_ADDR](#a7000f685fa8063fd0057c49691290645)   2560 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_1\_SIZE](#a426c96f351acc28a58bd5cef0f36f3ff)   2561 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_2\_ADDR](#ab3846a793efd5eb9570de9f6178a9a48)   2562 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_2\_SIZE](#a876421485286903d1af0f5a4a56ed426)   2563 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_3\_ADDR](#a7e5a8e8618d82e734af8104a14ceaa42)   2564 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_3\_SIZE](#af55d5a6b812ca91bf826f6b6ff6db5f3)   2565 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_4\_ADDR](#a637eb678ac4f9737e822820f3f4cc4d3)   2566 |
| #define | [ARC\_CLN\_MST\_NOC\_0\_4\_SIZE](#ac384c2a493b8036c3ff4d2b588abb2b0)   2567 |
| #define | [ARC\_CLN\_PER0\_BASE](#adfd899ecec6fb897c839ea59066723bd)   2688 |
| #define | [ARC\_CLN\_PER0\_SIZE](#ad88ec2aeacf13576b40f734c6d0aeebc)   2689 |
| #define | [ARC\_CLN\_SHMEM\_ADDR](#a36813211233630a20c6b5c8e6c5e9871)   200 |
| #define | [ARC\_CLN\_SHMEM\_SIZE](#a93000d405af39e772bf1f4b0abad6988)   201 |
| #define | [ARC\_CLN\_CACHE\_ADDR\_LO0](#a837a7b2c1dce58bfe20738b5335d3847)   204 |
| #define | [ARC\_CLN\_CACHE\_ADDR\_LO1](#abf4e31eb215a4f8a1be02a0ac9d02b2d)   205 |
| #define | [ARC\_CLN\_CACHE\_ADDR\_HI0](#a2ef20e3976381cacf0c93e3c8b89eb25)   206 |
| #define | [ARC\_CLN\_CACHE\_ADDR\_HI1](#aad5886b10a82cf6fd46bf3a4b6fb7140)   207 |
| #define | [ARC\_CLN\_CACHE\_CMD](#a23e947cb61e4110104f06187accf7eab)   207 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_NOP](#a3e89f76e02a55187fe1acabdb6231663)   0b0000 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_LOOKUP](#a8134b5e1fe035d87d9b72460ff03b4a0)   0b0001 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_PROBE](#ab5881a521b91e7061b317889e22c68a6)   0b0010 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_INV](#a07e8d0b1bbf0f700ba8b1ffb435fc5cc)   0b0101 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_CLN](#a598ceb22f93111d7e3d1e86530a541c9)   0b0110 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_CLN\_INV](#a9277c238385224cfe5365c6cb2256e6c)   0b0111 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_REG\_INV](#ab925b9c327fd17d609b482895891c52d)   0b1001 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_REG\_CLN](#a1beaa91ef4611c2c13c202f2f5de3cb7)   0b1010 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_REG\_CLN\_INV](#a5051697d74e83e04e45f0f235a8810b5)   0b1011 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_INV](#a7c5f71d32bb9a5b09a6dd0eab402b127)   0b1101 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_CLN](#a31a497b5cfaa26f8bd8982873c9d930d)   0b1110 |
| #define | [ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_CLN\_INV](#a4b7313b87b272d1f3b4a18faab1d74c7)   0b1111 |
| #define | [ARC\_CLN\_CACHE\_CMD\_INCR](#a8769aaa12bdd2bb25b51125f37f4c213)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [ARC\_CLN\_CACHE\_STATUS](#a04b102793c6c338475d0c417fdc37dc7)   209 |
| #define | [ARC\_CLN\_CACHE\_STATUS\_BUSY](#a5588c243334ec9f77094e3790de1edfc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| #define | [ARC\_CLN\_CACHE\_STATUS\_DONE](#ad47fc2d06da9cad04f418c3be0b64d47)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| #define | [ARC\_CLN\_CACHE\_STATUS\_MASK](#a9db97202cbf743f26d0ecfc5c67bda72)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| #define | [ARC\_CLN\_CACHE\_STATUS\_EN](#a7a26bf132d33d0b822f6e545e1a7a1ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| #define | [ARC\_CLN\_CACHE\_ERR](#ae73c0ea02ac014b76276565641fbad1a)   210 |
| #define | [ARC\_CLN\_CACHE\_ERR\_ADDR0](#a87e8c3294e03bdec644004708df609a9)   211 |
| #define | [ARC\_CLN\_CACHE\_ERR\_ADDR1](#aba01780d29faae95511855fbe173899d)   212 |

| Functions | |
| --- | --- |
| static [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arc\_cln\_read\_reg\_nolock](#a3b20fd71aae07450ee1fe430bd180bcf) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
| static void | [arc\_cln\_write\_reg\_nolock](#aca1c314c890ac39194725215a1a39ca7) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int data) |

## Detailed Description

ARC Cluster registers and accessors.

## Macro Definition Documentation

## [◆ ](#a2ef20e3976381cacf0c93e3c8b89eb25)ARC\_CLN\_CACHE\_ADDR\_HI0

| #define ARC\_CLN\_CACHE\_ADDR\_HI0   206 |
| --- |

## [◆ ](#aad5886b10a82cf6fd46bf3a4b6fb7140)ARC\_CLN\_CACHE\_ADDR\_HI1

| #define ARC\_CLN\_CACHE\_ADDR\_HI1   207 |
| --- |

## [◆ ](#a837a7b2c1dce58bfe20738b5335d3847)ARC\_CLN\_CACHE\_ADDR\_LO0

| #define ARC\_CLN\_CACHE\_ADDR\_LO0   204 |
| --- |

## [◆ ](#abf4e31eb215a4f8a1be02a0ac9d02b2d)ARC\_CLN\_CACHE\_ADDR\_LO1

| #define ARC\_CLN\_CACHE\_ADDR\_LO1   205 |
| --- |

## [◆ ](#a23e947cb61e4110104f06187accf7eab)ARC\_CLN\_CACHE\_CMD

| #define ARC\_CLN\_CACHE\_CMD   207 |
| --- |

## [◆ ](#a8769aaa12bdd2bb25b51125f37f4c213)ARC\_CLN\_CACHE\_CMD\_INCR

| #define ARC\_CLN\_CACHE\_CMD\_INCR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a31a497b5cfaa26f8bd8982873c9d930d)ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_CLN

| #define ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_CLN   0b1110 |
| --- |

## [◆ ](#a4b7313b87b272d1f3b4a18faab1d74c7)ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_CLN\_INV

| #define ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_CLN\_INV   0b1111 |
| --- |

## [◆ ](#a7c5f71d32bb9a5b09a6dd0eab402b127)ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_INV

| #define ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_INV   0b1101 |
| --- |

## [◆ ](#a598ceb22f93111d7e3d1e86530a541c9)ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_CLN

| #define ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_CLN   0b0110 |
| --- |

## [◆ ](#a9277c238385224cfe5365c6cb2256e6c)ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_CLN\_INV

| #define ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_CLN\_INV   0b0111 |
| --- |

## [◆ ](#a07e8d0b1bbf0f700ba8b1ffb435fc5cc)ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_INV

| #define ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_INV   0b0101 |
| --- |

## [◆ ](#a8134b5e1fe035d87d9b72460ff03b4a0)ARC\_CLN\_CACHE\_CMD\_OP\_LOOKUP

| #define ARC\_CLN\_CACHE\_CMD\_OP\_LOOKUP   0b0001 |
| --- |

## [◆ ](#a3e89f76e02a55187fe1acabdb6231663)ARC\_CLN\_CACHE\_CMD\_OP\_NOP

| #define ARC\_CLN\_CACHE\_CMD\_OP\_NOP   0b0000 |
| --- |

## [◆ ](#ab5881a521b91e7061b317889e22c68a6)ARC\_CLN\_CACHE\_CMD\_OP\_PROBE

| #define ARC\_CLN\_CACHE\_CMD\_OP\_PROBE   0b0010 |
| --- |

## [◆ ](#a1beaa91ef4611c2c13c202f2f5de3cb7)ARC\_CLN\_CACHE\_CMD\_OP\_REG\_CLN

| #define ARC\_CLN\_CACHE\_CMD\_OP\_REG\_CLN   0b1010 |
| --- |

## [◆ ](#a5051697d74e83e04e45f0f235a8810b5)ARC\_CLN\_CACHE\_CMD\_OP\_REG\_CLN\_INV

| #define ARC\_CLN\_CACHE\_CMD\_OP\_REG\_CLN\_INV   0b1011 |
| --- |

## [◆ ](#ab925b9c327fd17d609b482895891c52d)ARC\_CLN\_CACHE\_CMD\_OP\_REG\_INV

| #define ARC\_CLN\_CACHE\_CMD\_OP\_REG\_INV   0b1001 |
| --- |

## [◆ ](#ae73c0ea02ac014b76276565641fbad1a)ARC\_CLN\_CACHE\_ERR

| #define ARC\_CLN\_CACHE\_ERR   210 |
| --- |

## [◆ ](#a87e8c3294e03bdec644004708df609a9)ARC\_CLN\_CACHE\_ERR\_ADDR0

| #define ARC\_CLN\_CACHE\_ERR\_ADDR0   211 |
| --- |

## [◆ ](#aba01780d29faae95511855fbe173899d)ARC\_CLN\_CACHE\_ERR\_ADDR1

| #define ARC\_CLN\_CACHE\_ERR\_ADDR1   212 |
| --- |

## [◆ ](#a04b102793c6c338475d0c417fdc37dc7)ARC\_CLN\_CACHE\_STATUS

| #define ARC\_CLN\_CACHE\_STATUS   209 |
| --- |

## [◆ ](#a5588c243334ec9f77094e3790de1edfc)ARC\_CLN\_CACHE\_STATUS\_BUSY

| #define ARC\_CLN\_CACHE\_STATUS\_BUSY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) |
| --- |

## [◆ ](#ad47fc2d06da9cad04f418c3be0b64d47)ARC\_CLN\_CACHE\_STATUS\_DONE

| #define ARC\_CLN\_CACHE\_STATUS\_DONE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24) |
| --- |

## [◆ ](#a7a26bf132d33d0b822f6e545e1a7a1ef)ARC\_CLN\_CACHE\_STATUS\_EN

| #define ARC\_CLN\_CACHE\_STATUS\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| --- |

## [◆ ](#a9db97202cbf743f26d0ecfc5c67bda72)ARC\_CLN\_CACHE\_STATUS\_MASK

| #define ARC\_CLN\_CACHE\_STATUS\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26) |
| --- |

## [◆ ](#af50cee9c1dd5c1b68f98704f5cfb528a)ARC\_CLN\_MST\_NOC\_0\_0\_ADDR

| #define ARC\_CLN\_MST\_NOC\_0\_0\_ADDR   292 |
| --- |

## [◆ ](#ae41dbdd46df7733240048b55815ba654)ARC\_CLN\_MST\_NOC\_0\_0\_SIZE

| #define ARC\_CLN\_MST\_NOC\_0\_0\_SIZE   293 |
| --- |

## [◆ ](#a7000f685fa8063fd0057c49691290645)ARC\_CLN\_MST\_NOC\_0\_1\_ADDR

| #define ARC\_CLN\_MST\_NOC\_0\_1\_ADDR   2560 |
| --- |

## [◆ ](#a426c96f351acc28a58bd5cef0f36f3ff)ARC\_CLN\_MST\_NOC\_0\_1\_SIZE

| #define ARC\_CLN\_MST\_NOC\_0\_1\_SIZE   2561 |
| --- |

## [◆ ](#ab3846a793efd5eb9570de9f6178a9a48)ARC\_CLN\_MST\_NOC\_0\_2\_ADDR

| #define ARC\_CLN\_MST\_NOC\_0\_2\_ADDR   2562 |
| --- |

## [◆ ](#a876421485286903d1af0f5a4a56ed426)ARC\_CLN\_MST\_NOC\_0\_2\_SIZE

| #define ARC\_CLN\_MST\_NOC\_0\_2\_SIZE   2563 |
| --- |

## [◆ ](#a7e5a8e8618d82e734af8104a14ceaa42)ARC\_CLN\_MST\_NOC\_0\_3\_ADDR

| #define ARC\_CLN\_MST\_NOC\_0\_3\_ADDR   2564 |
| --- |

## [◆ ](#af55d5a6b812ca91bf826f6b6ff6db5f3)ARC\_CLN\_MST\_NOC\_0\_3\_SIZE

| #define ARC\_CLN\_MST\_NOC\_0\_3\_SIZE   2565 |
| --- |

## [◆ ](#a637eb678ac4f9737e822820f3f4cc4d3)ARC\_CLN\_MST\_NOC\_0\_4\_ADDR

| #define ARC\_CLN\_MST\_NOC\_0\_4\_ADDR   2566 |
| --- |

## [◆ ](#ac384c2a493b8036c3ff4d2b588abb2b0)ARC\_CLN\_MST\_NOC\_0\_4\_SIZE

| #define ARC\_CLN\_MST\_NOC\_0\_4\_SIZE   2567 |
| --- |

## [◆ ](#ae8548b32fefa14c8ee8b2df215bcde8a)ARC\_CLN\_MST\_NOC\_0\_BCR

| #define ARC\_CLN\_MST\_NOC\_0\_BCR   0 |
| --- |

## [◆ ](#a7b9948865accce27b428ab101d4f7488)ARC\_CLN\_MST\_NOC\_1\_BCR

| #define ARC\_CLN\_MST\_NOC\_1\_BCR   1 |
| --- |

## [◆ ](#af8bb48bfd94941b91441f8fab7e26b39)ARC\_CLN\_MST\_NOC\_2\_BCR

| #define ARC\_CLN\_MST\_NOC\_2\_BCR   2 |
| --- |

## [◆ ](#a5ec102830a019fd6b9eff79c1fc64a9c)ARC\_CLN\_MST\_NOC\_3\_BCR

| #define ARC\_CLN\_MST\_NOC\_3\_BCR   3 |
| --- |

## [◆ ](#a4a990ce76f504e654ef3ac5fd8f7213a)ARC\_CLN\_MST\_PER\_0\_BCR

| #define ARC\_CLN\_MST\_PER\_0\_BCR   16 |
| --- |

## [◆ ](#a669fcee44d5ac869dc49776bb6984724)ARC\_CLN\_MST\_PER\_1\_BCR

| #define ARC\_CLN\_MST\_PER\_1\_BCR   17 |
| --- |

## [◆ ](#adfd899ecec6fb897c839ea59066723bd)ARC\_CLN\_PER0\_BASE

| #define ARC\_CLN\_PER0\_BASE   2688 |
| --- |

## [◆ ](#ad88ec2aeacf13576b40f734c6d0aeebc)ARC\_CLN\_PER0\_SIZE

| #define ARC\_CLN\_PER0\_SIZE   2689 |
| --- |

## [◆ ](#a2e148f6cb243a4e98bbac15e91a08bca)ARC\_CLN\_PER\_0\_BASE

| #define ARC\_CLN\_PER\_0\_BASE   2688 |
| --- |

## [◆ ](#a80b5165ddda4c428344f008886389779)ARC\_CLN\_PER\_0\_SIZE

| #define ARC\_CLN\_PER\_0\_SIZE   2689 |
| --- |

## [◆ ](#a45ed0679d4903c9ad3cae818ea69ded7)ARC\_CLN\_PER\_1\_BASE

| #define ARC\_CLN\_PER\_1\_BASE   2690 |
| --- |

## [◆ ](#ac5a80d92726f545edd24586c7e9e537e)ARC\_CLN\_PER\_1\_SIZE

| #define ARC\_CLN\_PER\_1\_SIZE   2691 |
| --- |

## [◆ ](#acd23250017388ccdc6c4d29937fd6a32)ARC\_CLN\_SCM\_BCR\_0

| #define ARC\_CLN\_SCM\_BCR\_0   100 |
| --- |

## [◆ ](#aa81707d4070e08efea3a7d602611fb18)ARC\_CLN\_SCM\_BCR\_1

| #define ARC\_CLN\_SCM\_BCR\_1   101 |
| --- |

## [◆ ](#a36813211233630a20c6b5c8e6c5e9871)ARC\_CLN\_SHMEM\_ADDR

| #define ARC\_CLN\_SHMEM\_ADDR   200 |
| --- |

## [◆ ](#a93000d405af39e772bf1f4b0abad6988)ARC\_CLN\_SHMEM\_SIZE

| #define ARC\_CLN\_SHMEM\_SIZE   201 |
| --- |

## Function Documentation

## [◆ ](#a3b20fd71aae07450ee1fe430bd180bcf)arc\_cln\_read\_reg\_nolock()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int arc\_cln\_read\_reg\_nolock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aca1c314c890ac39194725215a1a39ca7)arc\_cln\_write\_reg\_nolock()

| | void arc\_cln\_write\_reg\_nolock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [cluster.h](cluster_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
