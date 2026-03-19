---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cluster_8h_source.html
original_path: doxygen/html/cluster_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cluster.h

[Go to the documentation of this file.](cluster_8h.md)

1/\*

2 \* Copyright (c) 2023 Synopsys.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_CLUSTER\_H\_

13#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_CLUSTER\_H\_

14

15#include <[zephyr/arch/arc/v2/aux\_regs.h](aux__regs_8h.md)>

16#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

17

18/\* Cluster AUX \*/

19#define \_ARC\_REG\_CLN\_BCR 0xcf

20

21#define \_ARC\_CLNR\_ADDR 0x640 /\* CLN address for CLNR\_DATA \*/

22#define \_ARC\_CLNR\_DATA 0x641 /\* CLN data indicated by CLNR\_ADDR \*/

23#define \_ARC\_CLNR\_DATA\_NXT 0x642 /\* CLNR\_DATA and then CLNR\_ADDR++ \*/

24#define \_ARC\_CLNR\_BCR\_0 0xF61

25#define \_ARC\_CLNR\_BCR\_1 0xF62

26#define \_ARC\_CLNR\_BCR\_2 0xF63

27#define \_ARC\_CLNR\_SCM\_BCR\_0 0xF64

28#define \_ARC\_CLNR\_SCM\_BCR\_1 0xF65

29

30#define \_ARC\_REG\_CLN\_BCR\_VER\_MAJOR\_ARCV3\_MIN 32 /\* Minimal version of cluster in ARCv3 \*/

31#define \_ARC\_CLN\_BCR\_VER\_MAJOR\_MASK 0xff

32#define \_ARC\_CLNR\_BCR\_0\_HAS\_SCM BIT(29)

33

34/\* Cluster registers (not in the AUX address space - indirect access via CLNR\_ADDR + CLNR\_DATA) \*/

[ 35](cluster_8h.md#ae8548b32fefa14c8ee8b2df215bcde8a)#define ARC\_CLN\_MST\_NOC\_0\_BCR 0

[ 36](cluster_8h.md#a7b9948865accce27b428ab101d4f7488)#define ARC\_CLN\_MST\_NOC\_1\_BCR 1

[ 37](cluster_8h.md#af8bb48bfd94941b91441f8fab7e26b39)#define ARC\_CLN\_MST\_NOC\_2\_BCR 2

[ 38](cluster_8h.md#a5ec102830a019fd6b9eff79c1fc64a9c)#define ARC\_CLN\_MST\_NOC\_3\_BCR 3

[ 39](cluster_8h.md#a4a990ce76f504e654ef3ac5fd8f7213a)#define ARC\_CLN\_MST\_PER\_0\_BCR 16

[ 40](cluster_8h.md#a669fcee44d5ac869dc49776bb6984724)#define ARC\_CLN\_MST\_PER\_1\_BCR 17

[ 41](cluster_8h.md#a2e148f6cb243a4e98bbac15e91a08bca)#define ARC\_CLN\_PER\_0\_BASE 2688

[ 42](cluster_8h.md#a80b5165ddda4c428344f008886389779)#define ARC\_CLN\_PER\_0\_SIZE 2689

[ 43](cluster_8h.md#a45ed0679d4903c9ad3cae818ea69ded7)#define ARC\_CLN\_PER\_1\_BASE 2690

[ 44](cluster_8h.md#ac5a80d92726f545edd24586c7e9e537e)#define ARC\_CLN\_PER\_1\_SIZE 2691

45

[ 46](cluster_8h.md#acd23250017388ccdc6c4d29937fd6a32)#define ARC\_CLN\_SCM\_BCR\_0 100

[ 47](cluster_8h.md#aa81707d4070e08efea3a7d602611fb18)#define ARC\_CLN\_SCM\_BCR\_1 101

48

[ 49](cluster_8h.md#af50cee9c1dd5c1b68f98704f5cfb528a)#define ARC\_CLN\_MST\_NOC\_0\_0\_ADDR 292

[ 50](cluster_8h.md#ae41dbdd46df7733240048b55815ba654)#define ARC\_CLN\_MST\_NOC\_0\_0\_SIZE 293

[ 51](cluster_8h.md#a7000f685fa8063fd0057c49691290645)#define ARC\_CLN\_MST\_NOC\_0\_1\_ADDR 2560

[ 52](cluster_8h.md#a426c96f351acc28a58bd5cef0f36f3ff)#define ARC\_CLN\_MST\_NOC\_0\_1\_SIZE 2561

[ 53](cluster_8h.md#ab3846a793efd5eb9570de9f6178a9a48)#define ARC\_CLN\_MST\_NOC\_0\_2\_ADDR 2562

[ 54](cluster_8h.md#a876421485286903d1af0f5a4a56ed426)#define ARC\_CLN\_MST\_NOC\_0\_2\_SIZE 2563

[ 55](cluster_8h.md#a7e5a8e8618d82e734af8104a14ceaa42)#define ARC\_CLN\_MST\_NOC\_0\_3\_ADDR 2564

[ 56](cluster_8h.md#af55d5a6b812ca91bf826f6b6ff6db5f3)#define ARC\_CLN\_MST\_NOC\_0\_3\_SIZE 2565

[ 57](cluster_8h.md#a637eb678ac4f9737e822820f3f4cc4d3)#define ARC\_CLN\_MST\_NOC\_0\_4\_ADDR 2566

[ 58](cluster_8h.md#ac384c2a493b8036c3ff4d2b588abb2b0)#define ARC\_CLN\_MST\_NOC\_0\_4\_SIZE 2567

59

[ 60](cluster_8h.md#adfd899ecec6fb897c839ea59066723bd)#define ARC\_CLN\_PER0\_BASE 2688

[ 61](cluster_8h.md#ad88ec2aeacf13576b40f734c6d0aeebc)#define ARC\_CLN\_PER0\_SIZE 2689

62

[ 63](cluster_8h.md#a36813211233630a20c6b5c8e6c5e9871)#define ARC\_CLN\_SHMEM\_ADDR 200

[ 64](cluster_8h.md#a93000d405af39e772bf1f4b0abad6988)#define ARC\_CLN\_SHMEM\_SIZE 201

[ 65](cluster_8h.md#a837a7b2c1dce58bfe20738b5335d3847)#define ARC\_CLN\_CACHE\_ADDR\_LO0 204

[ 66](cluster_8h.md#abf4e31eb215a4f8a1be02a0ac9d02b2d)#define ARC\_CLN\_CACHE\_ADDR\_LO1 205

[ 67](cluster_8h.md#a2ef20e3976381cacf0c93e3c8b89eb25)#define ARC\_CLN\_CACHE\_ADDR\_HI0 206

[ 68](cluster_8h.md#aad5886b10a82cf6fd46bf3a4b6fb7140)#define ARC\_CLN\_CACHE\_ADDR\_HI1 207

[ 69](cluster_8h.md#a23e947cb61e4110104f06187accf7eab)#define ARC\_CLN\_CACHE\_CMD 207

[ 70](cluster_8h.md#a3e89f76e02a55187fe1acabdb6231663)#define ARC\_CLN\_CACHE\_CMD\_OP\_NOP 0b0000

[ 71](cluster_8h.md#a8134b5e1fe035d87d9b72460ff03b4a0)#define ARC\_CLN\_CACHE\_CMD\_OP\_LOOKUP 0b0001

[ 72](cluster_8h.md#ab5881a521b91e7061b317889e22c68a6)#define ARC\_CLN\_CACHE\_CMD\_OP\_PROBE 0b0010

[ 73](cluster_8h.md#a07e8d0b1bbf0f700ba8b1ffb435fc5cc)#define ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_INV 0b0101

[ 74](cluster_8h.md#a598ceb22f93111d7e3d1e86530a541c9)#define ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_CLN 0b0110

[ 75](cluster_8h.md#a9277c238385224cfe5365c6cb2256e6c)#define ARC\_CLN\_CACHE\_CMD\_OP\_IDX\_CLN\_INV 0b0111

[ 76](cluster_8h.md#ab925b9c327fd17d609b482895891c52d)#define ARC\_CLN\_CACHE\_CMD\_OP\_REG\_INV 0b1001

[ 77](cluster_8h.md#a1beaa91ef4611c2c13c202f2f5de3cb7)#define ARC\_CLN\_CACHE\_CMD\_OP\_REG\_CLN 0b1010

[ 78](cluster_8h.md#a5051697d74e83e04e45f0f235a8810b5)#define ARC\_CLN\_CACHE\_CMD\_OP\_REG\_CLN\_INV 0b1011

[ 79](cluster_8h.md#a7c5f71d32bb9a5b09a6dd0eab402b127)#define ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_INV 0b1101

[ 80](cluster_8h.md#a31a497b5cfaa26f8bd8982873c9d930d)#define ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_CLN 0b1110

[ 81](cluster_8h.md#a4b7313b87b272d1f3b4a18faab1d74c7)#define ARC\_CLN\_CACHE\_CMD\_OP\_ADDR\_CLN\_INV 0b1111

[ 82](cluster_8h.md#a8769aaa12bdd2bb25b51125f37f4c213)#define ARC\_CLN\_CACHE\_CMD\_INCR BIT(4)

83

[ 84](cluster_8h.md#a04b102793c6c338475d0c417fdc37dc7)#define ARC\_CLN\_CACHE\_STATUS 209

[ 85](cluster_8h.md#a5588c243334ec9f77094e3790de1edfc)#define ARC\_CLN\_CACHE\_STATUS\_BUSY BIT(23)

[ 86](cluster_8h.md#ad47fc2d06da9cad04f418c3be0b64d47)#define ARC\_CLN\_CACHE\_STATUS\_DONE BIT(24)

[ 87](cluster_8h.md#a9db97202cbf743f26d0ecfc5c67bda72)#define ARC\_CLN\_CACHE\_STATUS\_MASK BIT(26)

[ 88](cluster_8h.md#a7a26bf132d33d0b822f6e545e1a7a1ef)#define ARC\_CLN\_CACHE\_STATUS\_EN BIT(27)

[ 89](cluster_8h.md#ae73c0ea02ac014b76276565641fbad1a)#define ARC\_CLN\_CACHE\_ERR 210

[ 90](cluster_8h.md#a87e8c3294e03bdec644004708df609a9)#define ARC\_CLN\_CACHE\_ERR\_ADDR0 211

[ 91](cluster_8h.md#aba01780d29faae95511855fbe173899d)#define ARC\_CLN\_CACHE\_ERR\_ADDR1 212

92

93

[ 94](cluster_8h.md#a3b20fd71aae07450ee1fe430bd180bcf)static inline unsigned int [arc\_cln\_read\_reg\_nolock](cluster_8h.md#a3b20fd71aae07450ee1fe430bd180bcf)(unsigned int reg)

95{

96 z\_arc\_v2\_aux\_reg\_write(\_ARC\_CLNR\_ADDR, reg);

97 return z\_arc\_v2\_aux\_reg\_read(\_ARC\_CLNR\_DATA);

98}

99

[ 100](cluster_8h.md#aca1c314c890ac39194725215a1a39ca7)static inline void [arc\_cln\_write\_reg\_nolock](cluster_8h.md#aca1c314c890ac39194725215a1a39ca7)(unsigned int reg, unsigned int data)

101{

102 z\_arc\_v2\_aux\_reg\_write(\_ARC\_CLNR\_ADDR, reg);

103 z\_arc\_v2\_aux\_reg\_write(\_ARC\_CLNR\_DATA, data);

104}

105

106#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_CLUSTER\_H\_ \*/

[aux\_regs.h](aux__regs_8h.md)

ARCv2 auxiliary registers definitions.

[arc\_cln\_read\_reg\_nolock](cluster_8h.md#a3b20fd71aae07450ee1fe430bd180bcf)

static unsigned int arc\_cln\_read\_reg\_nolock(unsigned int reg)

**Definition** cluster.h:94

[arc\_cln\_write\_reg\_nolock](cluster_8h.md#aca1c314c890ac39194725215a1a39ca7)

static void arc\_cln\_write\_reg\_nolock(unsigned int reg, unsigned int data)

**Definition** cluster.h:100

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [cluster.h](cluster_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
