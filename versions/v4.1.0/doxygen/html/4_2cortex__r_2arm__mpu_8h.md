---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/4_2cortex__r_2arm__mpu_8h.html
original_path: doxygen/html/4_2cortex__r_2arm__mpu_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu.h File Reference

[Go to the source code of this file.](4_2cortex__r_2arm__mpu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) |
| struct | [arm\_mpu\_region](structarm__mpu__region.md) |
| struct | [arm\_mpu\_config](structarm__mpu__config.md) |
| struct | [dynamic\_region\_info](structdynamic__region__info.md) |

| Macros | |
| --- | --- |
| #define | [MPU\_IR\_REGION\_Msk](#a734d7c223353e973a104581b6e87d227)   (0xFFU) |
| #define | [MPU\_RBAR\_BASE\_Pos](#a73dbc6dcdf74ba9a411bc2670c17b7d0)   6U |
| #define | [MPU\_RBAR\_BASE\_Msk](#a57f2217a12342e8e43c7ad6949a9a65b)   (0x3FFFFFFFFFFFFFFUL << [MPU\_RBAR\_BASE\_Pos](#a73dbc6dcdf74ba9a411bc2670c17b7d0)) |
| #define | [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)   4U |
| #define | [MPU\_RBAR\_SH\_Msk](#aa014b1c92266313a3c1dc06e37e39aef)   (0x3UL << [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)) |
| #define | [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)   2U |
| #define | [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)   (0x3UL << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) |
| #define | [MPU\_RBAR\_XN\_Pos](#a6db81ec93c662cb563f18ef61e4df669)   1U |
| #define | [MPU\_RBAR\_XN\_Msk](#ae960690ad7849b21e6cd0c414075de1b)   (0x1UL << [MPU\_RBAR\_XN\_Pos](#a6db81ec93c662cb563f18ef61e4df669)) |
| #define | [MPU\_RLAR\_LIMIT\_Pos](#a6e827ab46bc85f283867819889865a23)   6U |
| #define | [MPU\_RLAR\_LIMIT\_Msk](#a9612abff664c827b36844fe42d8ee5cb)   (0x3FFFFFFFFFFFFFFUL << [MPU\_RLAR\_LIMIT\_Pos](#a6e827ab46bc85f283867819889865a23)) |
| #define | [MPU\_RLAR\_AttrIndx\_Pos](#a467ebe320762d7d1067ffec939119bcd)   1U |
| #define | [MPU\_RLAR\_AttrIndx\_Msk](#ab5ac20d186a58cc39a8d02a554d0868d)   (0x7UL << [MPU\_RLAR\_AttrIndx\_Pos](#a467ebe320762d7d1067ffec939119bcd)) |
| #define | [MPU\_RLAR\_EN\_Msk](#af1da1b8c76ac4a21ee44dbe8268073dd)   (0x1UL) |
| #define | [NOT\_EXEC](#a74c8c1c16d8d613d7b32d5fe9bd5d08d)   [MPU\_RBAR\_XN\_Msk](#ae960690ad7849b21e6cd0c414075de1b) /\* PRBAR\_EL1 \*/ |
| #define | [P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215)   0x0U |
| #define | [P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7)   (([P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215) << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34)   0x1U |
| #define | [P\_RW\_U\_RW\_Msk](#adc9ba826d1bf9a013724b7a24e9535db)   (([P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34) << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd)   0x2U |
| #define | [P\_RO\_U\_NA\_Msk](#aeec24407a5fffaf967a841a26ccf46ed)   (([P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd) << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211)   0x3U |
| #define | [P\_RO\_U\_RO\_Msk](#a4ec38b9015a95b2aafca5e9aa35f1f46)   (([P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211) << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [NON\_SHAREABLE](#ad2047a4b8dae13c488a331b1691000b5)   0x0U |
| #define | [NON\_SHAREABLE\_Msk](#a5c302dfed348f344a036701d4b9c7ec8)   (([NON\_SHAREABLE](#ad2047a4b8dae13c488a331b1691000b5) << [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](#aa014b1c92266313a3c1dc06e37e39aef)) |
| #define | [OUTER\_SHAREABLE](#a6d48175f63f47fcbe1fedbbdfcd56a85)   0x2U |
| #define | [OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)   (([OUTER\_SHAREABLE](#a6d48175f63f47fcbe1fedbbdfcd56a85) << [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](#aa014b1c92266313a3c1dc06e37e39aef)) |
| #define | [INNER\_SHAREABLE](#a8c245b5c485b439790459255fc645131)   0x3U |
| #define | [INNER\_SHAREABLE\_Msk](#ab0d195350222b02d2d83ecd94a9ca395)   (([INNER\_SHAREABLE](#a8c245b5c485b439790459255fc645131) << [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](#aa014b1c92266313a3c1dc06e37e39aef)) |
| #define | [DEVICE\_nGnRnE](#a7e8d641f98b092387124bd1ecf2fdb53)   0x0U |
| #define | [DEVICE\_nGnRE](#a1fb228a36a14d8679f6d038c47f5f2e1)   0x4U |
| #define | [DEVICE\_nGRE](#a50d2ee15f01cc5379a74d23efd969051)   0x8U |
| #define | [DEVICE\_GRE](#a3d0243c563668b7358ce29d54f7f1afa)   0xCU |
| #define | [R\_NON\_W\_NON](#a1160c997a66c9fd58dbc3dcfd65982a8)   0x0U /\* Do not allocate Read/Write \*/ |
| #define | [R\_NON\_W\_ALLOC](#a0696dfbe29563622fe76970f9d146ff5)   0x1U /\* Do not allocate Read, Allocate Write \*/ |
| #define | [R\_ALLOC\_W\_NON](#a8476bb45227afc0236bc9f427793d6a9)   0x2U /\* Allocate Read, Do not allocate Write \*/ |
| #define | [R\_ALLOC\_W\_ALLOC](#a1815e3622467845af3b3083fa76f3314)   0x3U /\* Allocate Read/Write \*/ |
| #define | [NORMAL\_O\_WT\_NT](#a4720c776e51ea52fc8cfa2c1dc935d47)   0x80U /\* Normal, Outer Write-through non-transient \*/ |
| #define | [NORMAL\_O\_WB\_NT](#a7d87ec111ffd79cddb9ce9f23e9f20d9)   0xC0U /\* Normal, Outer Write-back non-transient \*/ |
| #define | [NORMAL\_O\_NON\_C](#ae36bc21dc922e88f8d5d4ff0657d80b6)   0x40U /\* Normal, Outer Non-Cacheable \*/ |
| #define | [NORMAL\_I\_WT\_NT](#a2d60ab7f15ac71d451a73758315eff07)   0x08U /\* Normal, Inner Write-through non-transient \*/ |
| #define | [NORMAL\_I\_WB\_NT](#a28f31a1e2a47e2cafa7f41260780fd5f)   0x0CU /\* Normal, Inner Write-back non-transient \*/ |
| #define | [NORMAL\_I\_NON\_C](#a8dda4d3d5f372f8ef3070fb492448992)   0x04U /\* Normal, Inner Non-Cacheable \*/ |
| #define | [MPU\_MAIR\_INDEX\_DEVICE](#a6ae855ff0c11d85dc72a1c45edaa7f75)   0U |
| #define | [MPU\_MAIR\_ATTR\_DEVICE](#acfdb4baf0d7ec48fdc77e8e2973a1487)   ([DEVICE\_nGnRnE](#a7e8d641f98b092387124bd1ecf2fdb53)) |
| #define | [MPU\_MAIR\_INDEX\_FLASH](#ab1521fd2deea0bd6b88c73aed7159f8a)   1U |
| #define | [MPU\_MAIR\_ATTR\_FLASH](#ad384c906ae7e1f4841c8ea98754acc1c) |
| #define | [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)   2U |
| #define | [MPU\_MAIR\_ATTR\_SRAM](#aca50d2bc85d65c0ad231ecd7deb40c50) |
| #define | [MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)   3U |
| #define | [MPU\_MAIR\_ATTR\_SRAM\_NOCACHE](#ab6bce12dbd72d216cbb6bc748d801ce0) |
| #define | [MPU\_MAIR\_ATTRS](#a497d0db2bf062be1a466a1c7cab6a260) |
| #define | [REGION\_IO\_ATTR](#a4ce0d123898b8cb22cb161c8d69c411f) |
| #define | [REGION\_RAM\_ATTR](#a859d811feecb32c788b16a413e1b4781) |
| #define | [REGION\_RAM\_NOCACHE\_ATTR](#a89573cb3bde7b26846a3607276c843d9) |
| #define | [REGION\_RAM\_TEXT\_ATTR](#a00fb6882c3ff5d043e319be2ac04ea01) |
| #define | [REGION\_RAM\_RO\_ATTR](#a677d1642d4a105f9d5f81404e58b2cf4) |
| #define | [REGION\_FLASH\_ATTR](#aef333777108782979d84344af4bc51d6) |
| #define | [MPU\_REGION\_ENTRY](#a05f77a35978ad9b60c8ba099d9a915f0)(\_name, \_base, \_limit, \_attr) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#a9b7cc3c51f518517031d76807470aa10) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#a3c52d13e42a66beb72d088ac56388951) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#a708338371e91b5a3f2d44f9ae48849db) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#a706eaa9c515f1cc859d97ef8455b2f2f) |
| #define | [ARM64\_MPU\_MAX\_DYNAMIC\_REGIONS](#a6e954e6d9c6117210d857b360bf5fa51) |

| Typedefs | |
| --- | --- |
| typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) | [k\_mem\_partition\_attr\_t](#a6b3c416482c4d01cc12db5269886bb05) |

| Variables | |
| --- | --- |
| const struct [arm\_mpu\_config](structarm__mpu__config.md) | [mpu\_config](#ab4f9746862097dfdc048d75c9c08b795) |

## Macro Definition Documentation

## [◆ ](#a6e954e6d9c6117210d857b360bf5fa51)ARM64\_MPU\_MAX\_DYNAMIC\_REGIONS

| #define ARM64\_MPU\_MAX\_DYNAMIC\_REGIONS |
| --- |

**Value:**

1 + /\* data section \*/ \

(CONFIG\_MAX\_DOMAIN\_PARTITIONS + 2) + \

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_ARM64\_STACK\_PROTECTION) ? 2 : 0) + \

([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE) ? 2 : 0)

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

## [◆ ](#a3d0243c563668b7358ce29d54f7f1afa)DEVICE\_GRE

| #define DEVICE\_GRE   0xCU |
| --- |

## [◆ ](#a1fb228a36a14d8679f6d038c47f5f2e1)DEVICE\_nGnRE

| #define DEVICE\_nGnRE   0x4U |
| --- |

## [◆ ](#a7e8d641f98b092387124bd1ecf2fdb53)DEVICE\_nGnRnE

| #define DEVICE\_nGnRnE   0x0U |
| --- |

## [◆ ](#a50d2ee15f01cc5379a74d23efd969051)DEVICE\_nGRE

| #define DEVICE\_nGRE   0x8U |
| --- |

## [◆ ](#a8c245b5c485b439790459255fc645131)INNER\_SHAREABLE

| #define INNER\_SHAREABLE   0x3U |
| --- |

## [◆ ](#ab0d195350222b02d2d83ecd94a9ca395)INNER\_SHAREABLE\_Msk

| #define INNER\_SHAREABLE\_Msk   (([INNER\_SHAREABLE](#a8c245b5c485b439790459255fc645131) << [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](#aa014b1c92266313a3c1dc06e37e39aef)) |
| --- |

## [◆ ](#a706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RO\_U\_NA\_Msk](arm__mpu__v7m_8h.md#aeec24407a5fffaf967a841a26ccf46ed)), [MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03)})

[P\_RO\_U\_NA\_Msk](arm__mpu__v7m_8h.md#aeec24407a5fffaf967a841a26ccf46ed)

#define P\_RO\_U\_NA\_Msk

**Definition** arm\_mpu\_v7m.h:37

[MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03)

#define MPU\_MAIR\_INDEX\_SRAM

**Definition** arm\_mpu\_v8.h:141

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:143

## [◆ ](#a708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46)), [MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03)})

[P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46)

#define P\_RO\_U\_RO\_Msk

**Definition** arm\_mpu\_v7m.h:40

## [◆ ](#a3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7)), [MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03)})

[P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7)

#define P\_RW\_U\_NA\_Msk

**Definition** arm\_mpu\_v7m.h:25

## [◆ ](#a9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RW\_U\_RW\_Msk](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db)), [MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03)})

[P\_RW\_U\_RW\_Msk](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db)

#define P\_RW\_U\_RW\_Msk

**Definition** arm\_mpu\_v7m.h:31

## [◆ ](#a734d7c223353e973a104581b6e87d227)MPU\_IR\_REGION\_Msk

| #define MPU\_IR\_REGION\_Msk   (0xFFU) |
| --- |

## [◆ ](#acfdb4baf0d7ec48fdc77e8e2973a1487)MPU\_MAIR\_ATTR\_DEVICE

| #define MPU\_MAIR\_ATTR\_DEVICE   ([DEVICE\_nGnRnE](#a7e8d641f98b092387124bd1ecf2fdb53)) |
| --- |

## [◆ ](#ad384c906ae7e1f4841c8ea98754acc1c)MPU\_MAIR\_ATTR\_FLASH

| #define MPU\_MAIR\_ATTR\_FLASH |
| --- |

**Value:**

(([NORMAL\_O\_WT\_NT](arm__mpu__v8_8h.md#a4720c776e51ea52fc8cfa2c1dc935d47) | ([R\_ALLOC\_W\_NON](arm__mpu__v8_8h.md#a8476bb45227afc0236bc9f427793d6a9) << 4)) | \

([NORMAL\_I\_WT\_NT](arm__mpu__v8_8h.md#a2d60ab7f15ac71d451a73758315eff07) | [R\_ALLOC\_W\_NON](arm__mpu__v8_8h.md#a8476bb45227afc0236bc9f427793d6a9)))

[NORMAL\_I\_WT\_NT](arm__mpu__v8_8h.md#a2d60ab7f15ac71d451a73758315eff07)

#define NORMAL\_I\_WT\_NT

**Definition** arm\_mpu\_v8.h:116

[NORMAL\_O\_WT\_NT](arm__mpu__v8_8h.md#a4720c776e51ea52fc8cfa2c1dc935d47)

#define NORMAL\_O\_WT\_NT

**Definition** arm\_mpu\_v8.h:112

[R\_ALLOC\_W\_NON](arm__mpu__v8_8h.md#a8476bb45227afc0236bc9f427793d6a9)

#define R\_ALLOC\_W\_NON

**Definition** arm\_mpu\_v8.h:108

## [◆ ](#aca50d2bc85d65c0ad231ecd7deb40c50)MPU\_MAIR\_ATTR\_SRAM

| #define MPU\_MAIR\_ATTR\_SRAM |
| --- |

**Value:**

(([NORMAL\_O\_WB\_NT](arm__mpu__v8_8h.md#a7d87ec111ffd79cddb9ce9f23e9f20d9) | ([R\_ALLOC\_W\_ALLOC](arm__mpu__v8_8h.md#a1815e3622467845af3b3083fa76f3314) << 4)) | \

([NORMAL\_I\_WB\_NT](arm__mpu__v8_8h.md#a28f31a1e2a47e2cafa7f41260780fd5f) | [R\_ALLOC\_W\_ALLOC](arm__mpu__v8_8h.md#a1815e3622467845af3b3083fa76f3314)))

[R\_ALLOC\_W\_ALLOC](arm__mpu__v8_8h.md#a1815e3622467845af3b3083fa76f3314)

#define R\_ALLOC\_W\_ALLOC

**Definition** arm\_mpu\_v8.h:109

[NORMAL\_I\_WB\_NT](arm__mpu__v8_8h.md#a28f31a1e2a47e2cafa7f41260780fd5f)

#define NORMAL\_I\_WB\_NT

**Definition** arm\_mpu\_v8.h:117

[NORMAL\_O\_WB\_NT](arm__mpu__v8_8h.md#a7d87ec111ffd79cddb9ce9f23e9f20d9)

#define NORMAL\_O\_WB\_NT

**Definition** arm\_mpu\_v8.h:113

## [◆ ](#ab6bce12dbd72d216cbb6bc748d801ce0)MPU\_MAIR\_ATTR\_SRAM\_NOCACHE

| #define MPU\_MAIR\_ATTR\_SRAM\_NOCACHE |
| --- |

**Value:**

(([NORMAL\_O\_NON\_C](arm__mpu__v8_8h.md#ae36bc21dc922e88f8d5d4ff0657d80b6) | ([R\_NON\_W\_NON](arm__mpu__v8_8h.md#a1160c997a66c9fd58dbc3dcfd65982a8) << 4)) | \

([NORMAL\_I\_NON\_C](arm__mpu__v8_8h.md#a8dda4d3d5f372f8ef3070fb492448992) | [R\_NON\_W\_NON](arm__mpu__v8_8h.md#a1160c997a66c9fd58dbc3dcfd65982a8)))

[R\_NON\_W\_NON](arm__mpu__v8_8h.md#a1160c997a66c9fd58dbc3dcfd65982a8)

#define R\_NON\_W\_NON

**Definition** arm\_mpu\_v8.h:106

[NORMAL\_I\_NON\_C](arm__mpu__v8_8h.md#a8dda4d3d5f372f8ef3070fb492448992)

#define NORMAL\_I\_NON\_C

**Definition** arm\_mpu\_v8.h:118

[NORMAL\_O\_NON\_C](arm__mpu__v8_8h.md#ae36bc21dc922e88f8d5d4ff0657d80b6)

#define NORMAL\_O\_NON\_C

**Definition** arm\_mpu\_v8.h:114

## [◆ ](#a497d0db2bf062be1a466a1c7cab6a260)MPU\_MAIR\_ATTRS

| #define MPU\_MAIR\_ATTRS |
| --- |

**Value:**

(([MPU\_MAIR\_ATTR\_DEVICE](arm__mpu__v8_8h.md#acfdb4baf0d7ec48fdc77e8e2973a1487) << ([MPU\_MAIR\_INDEX\_DEVICE](arm__mpu__v8_8h.md#a6ae855ff0c11d85dc72a1c45edaa7f75) \* 8)) | \

([MPU\_MAIR\_ATTR\_FLASH](arm__mpu__v8_8h.md#ad384c906ae7e1f4841c8ea98754acc1c) << ([MPU\_MAIR\_INDEX\_FLASH](arm__mpu__v8_8h.md#ab1521fd2deea0bd6b88c73aed7159f8a) \* 8)) | \

([MPU\_MAIR\_ATTR\_SRAM](arm__mpu__v8_8h.md#aca50d2bc85d65c0ad231ecd7deb40c50) << ([MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03) \* 8)) | \

([MPU\_MAIR\_ATTR\_SRAM\_NOCACHE](arm__mpu__v8_8h.md#ab6bce12dbd72d216cbb6bc748d801ce0) << ([MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](arm__mpu__v8_8h.md#a03e37d7769647008655338fe8359d946) \* 8)))

[MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](arm__mpu__v8_8h.md#a03e37d7769647008655338fe8359d946)

#define MPU\_MAIR\_INDEX\_SRAM\_NOCACHE

**Definition** arm\_mpu\_v8.h:143

[MPU\_MAIR\_INDEX\_DEVICE](arm__mpu__v8_8h.md#a6ae855ff0c11d85dc72a1c45edaa7f75)

#define MPU\_MAIR\_INDEX\_DEVICE

**Definition** arm\_mpu\_v8.h:145

[MPU\_MAIR\_INDEX\_FLASH](arm__mpu__v8_8h.md#ab1521fd2deea0bd6b88c73aed7159f8a)

#define MPU\_MAIR\_INDEX\_FLASH

**Definition** arm\_mpu\_v8.h:139

[MPU\_MAIR\_ATTR\_SRAM\_NOCACHE](arm__mpu__v8_8h.md#ab6bce12dbd72d216cbb6bc748d801ce0)

#define MPU\_MAIR\_ATTR\_SRAM\_NOCACHE

**Definition** arm\_mpu\_v8.h:142

[MPU\_MAIR\_ATTR\_SRAM](arm__mpu__v8_8h.md#aca50d2bc85d65c0ad231ecd7deb40c50)

#define MPU\_MAIR\_ATTR\_SRAM

**Definition** arm\_mpu\_v8.h:140

[MPU\_MAIR\_ATTR\_DEVICE](arm__mpu__v8_8h.md#acfdb4baf0d7ec48fdc77e8e2973a1487)

#define MPU\_MAIR\_ATTR\_DEVICE

**Definition** arm\_mpu\_v8.h:144

[MPU\_MAIR\_ATTR\_FLASH](arm__mpu__v8_8h.md#ad384c906ae7e1f4841c8ea98754acc1c)

#define MPU\_MAIR\_ATTR\_FLASH

**Definition** arm\_mpu\_v8.h:138

## [◆ ](#a6ae855ff0c11d85dc72a1c45edaa7f75)MPU\_MAIR\_INDEX\_DEVICE

| #define MPU\_MAIR\_INDEX\_DEVICE   0U |
| --- |

## [◆ ](#ab1521fd2deea0bd6b88c73aed7159f8a)MPU\_MAIR\_INDEX\_FLASH

| #define MPU\_MAIR\_INDEX\_FLASH   1U |
| --- |

## [◆ ](#a386bbcc650a8313774651212bda40d03)MPU\_MAIR\_INDEX\_SRAM

| #define MPU\_MAIR\_INDEX\_SRAM   2U |
| --- |

## [◆ ](#a03e37d7769647008655338fe8359d946)MPU\_MAIR\_INDEX\_SRAM\_NOCACHE

| #define MPU\_MAIR\_INDEX\_SRAM\_NOCACHE   3U |
| --- |

## [◆ ](#a76c759e3484530af0b2806ecf0018f75)MPU\_RBAR\_AP\_Msk

| #define MPU\_RBAR\_AP\_Msk   (0x3UL << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) |
| --- |

## [◆ ](#a33723f1259fdb840b50a6e34786755aa)MPU\_RBAR\_AP\_Pos

| #define MPU\_RBAR\_AP\_Pos   2U |
| --- |

## [◆ ](#a57f2217a12342e8e43c7ad6949a9a65b)MPU\_RBAR\_BASE\_Msk

| #define MPU\_RBAR\_BASE\_Msk   (0x3FFFFFFFFFFFFFFUL << [MPU\_RBAR\_BASE\_Pos](#a73dbc6dcdf74ba9a411bc2670c17b7d0)) |
| --- |

## [◆ ](#a73dbc6dcdf74ba9a411bc2670c17b7d0)MPU\_RBAR\_BASE\_Pos

| #define MPU\_RBAR\_BASE\_Pos   6U |
| --- |

## [◆ ](#aa014b1c92266313a3c1dc06e37e39aef)MPU\_RBAR\_SH\_Msk

| #define MPU\_RBAR\_SH\_Msk   (0x3UL << [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)) |
| --- |

## [◆ ](#a3150317eff21434c7ca4b24516603615)MPU\_RBAR\_SH\_Pos

| #define MPU\_RBAR\_SH\_Pos   4U |
| --- |

## [◆ ](#ae960690ad7849b21e6cd0c414075de1b)MPU\_RBAR\_XN\_Msk

| #define MPU\_RBAR\_XN\_Msk   (0x1UL << [MPU\_RBAR\_XN\_Pos](#a6db81ec93c662cb563f18ef61e4df669)) |
| --- |

## [◆ ](#a6db81ec93c662cb563f18ef61e4df669)MPU\_RBAR\_XN\_Pos

| #define MPU\_RBAR\_XN\_Pos   1U |
| --- |

## [◆ ](#a05f77a35978ad9b60c8ba099d9a915f0)MPU\_REGION\_ENTRY

| #define MPU\_REGION\_ENTRY | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_base*, |
|  |  |  | *\_limit*, |
|  |  |  | *\_attr* ) |

**Value:**

{ \

.name = \_name, \

.base = \_base, \

.limit = \_limit, \

.attr = \_attr, \

}

## [◆ ](#ab5ac20d186a58cc39a8d02a554d0868d)MPU\_RLAR\_AttrIndx\_Msk

| #define MPU\_RLAR\_AttrIndx\_Msk   (0x7UL << [MPU\_RLAR\_AttrIndx\_Pos](#a467ebe320762d7d1067ffec939119bcd)) |
| --- |

## [◆ ](#a467ebe320762d7d1067ffec939119bcd)MPU\_RLAR\_AttrIndx\_Pos

| #define MPU\_RLAR\_AttrIndx\_Pos   1U |
| --- |

## [◆ ](#af1da1b8c76ac4a21ee44dbe8268073dd)MPU\_RLAR\_EN\_Msk

| #define MPU\_RLAR\_EN\_Msk   (0x1UL) |
| --- |

## [◆ ](#a9612abff664c827b36844fe42d8ee5cb)MPU\_RLAR\_LIMIT\_Msk

| #define MPU\_RLAR\_LIMIT\_Msk   (0x3FFFFFFFFFFFFFFUL << [MPU\_RLAR\_LIMIT\_Pos](#a6e827ab46bc85f283867819889865a23)) |
| --- |

## [◆ ](#a6e827ab46bc85f283867819889865a23)MPU\_RLAR\_LIMIT\_Pos

| #define MPU\_RLAR\_LIMIT\_Pos   6U |
| --- |

## [◆ ](#ad2047a4b8dae13c488a331b1691000b5)NON\_SHAREABLE

| #define NON\_SHAREABLE   0x0U |
| --- |

## [◆ ](#a5c302dfed348f344a036701d4b9c7ec8)NON\_SHAREABLE\_Msk

| #define NON\_SHAREABLE\_Msk   (([NON\_SHAREABLE](#ad2047a4b8dae13c488a331b1691000b5) << [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](#aa014b1c92266313a3c1dc06e37e39aef)) |
| --- |

## [◆ ](#a8dda4d3d5f372f8ef3070fb492448992)NORMAL\_I\_NON\_C

| #define NORMAL\_I\_NON\_C   0x04U /\* Normal, Inner Non-Cacheable \*/ |
| --- |

## [◆ ](#a28f31a1e2a47e2cafa7f41260780fd5f)NORMAL\_I\_WB\_NT

| #define NORMAL\_I\_WB\_NT   0x0CU /\* Normal, Inner Write-back non-transient \*/ |
| --- |

## [◆ ](#a2d60ab7f15ac71d451a73758315eff07)NORMAL\_I\_WT\_NT

| #define NORMAL\_I\_WT\_NT   0x08U /\* Normal, Inner Write-through non-transient \*/ |
| --- |

## [◆ ](#ae36bc21dc922e88f8d5d4ff0657d80b6)NORMAL\_O\_NON\_C

| #define NORMAL\_O\_NON\_C   0x40U /\* Normal, Outer Non-Cacheable \*/ |
| --- |

## [◆ ](#a7d87ec111ffd79cddb9ce9f23e9f20d9)NORMAL\_O\_WB\_NT

| #define NORMAL\_O\_WB\_NT   0xC0U /\* Normal, Outer Write-back non-transient \*/ |
| --- |

## [◆ ](#a4720c776e51ea52fc8cfa2c1dc935d47)NORMAL\_O\_WT\_NT

| #define NORMAL\_O\_WT\_NT   0x80U /\* Normal, Outer Write-through non-transient \*/ |
| --- |

## [◆ ](#a74c8c1c16d8d613d7b32d5fe9bd5d08d)NOT\_EXEC

| #define NOT\_EXEC   [MPU\_RBAR\_XN\_Msk](#ae960690ad7849b21e6cd0c414075de1b) /\* PRBAR\_EL1 \*/ |
| --- |

## [◆ ](#a6d48175f63f47fcbe1fedbbdfcd56a85)OUTER\_SHAREABLE

| #define OUTER\_SHAREABLE   0x2U |
| --- |

## [◆ ](#aa4f924c424fc141ffa32a9b5c1180d56)OUTER\_SHAREABLE\_Msk

| #define OUTER\_SHAREABLE\_Msk   (([OUTER\_SHAREABLE](#a6d48175f63f47fcbe1fedbbdfcd56a85) << [MPU\_RBAR\_SH\_Pos](#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](#aa014b1c92266313a3c1dc06e37e39aef)) |
| --- |

## [◆ ](#ad3012e82dde223bbe84c9e4d7c46e7fd)P\_RO\_U\_NA

| #define P\_RO\_U\_NA   0x2U |
| --- |

## [◆ ](#aeec24407a5fffaf967a841a26ccf46ed)P\_RO\_U\_NA\_Msk

| #define P\_RO\_U\_NA\_Msk   (([P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd) << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a75fd88fb93da28e84017d4ba6fcb4211)P\_RO\_U\_RO

| #define P\_RO\_U\_RO   0x3U |
| --- |

## [◆ ](#a4ec38b9015a95b2aafca5e9aa35f1f46)P\_RO\_U\_RO\_Msk

| #define P\_RO\_U\_RO\_Msk   (([P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211) << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a6632f2c0eba4d5aee046a86258100215)P\_RW\_U\_NA

| #define P\_RW\_U\_NA   0x0U |
| --- |

## [◆ ](#a8a5805b5b1a6ca5cf5f59b2874ec68d7)P\_RW\_U\_NA\_Msk

| #define P\_RW\_U\_NA\_Msk   (([P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215) << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a8faee650ae8cc79e1d3605f251c3df34)P\_RW\_U\_RW

| #define P\_RW\_U\_RW   0x1U |
| --- |

## [◆ ](#adc9ba826d1bf9a013724b7a24e9535db)P\_RW\_U\_RW\_Msk

| #define P\_RW\_U\_RW\_Msk   (([P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34) << [MPU\_RBAR\_AP\_Pos](#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a1815e3622467845af3b3083fa76f3314)R\_ALLOC\_W\_ALLOC

| #define R\_ALLOC\_W\_ALLOC   0x3U /\* Allocate Read/Write \*/ |
| --- |

## [◆ ](#a8476bb45227afc0236bc9f427793d6a9)R\_ALLOC\_W\_NON

| #define R\_ALLOC\_W\_NON   0x2U /\* Allocate Read, Do not allocate Write \*/ |
| --- |

## [◆ ](#a0696dfbe29563622fe76970f9d146ff5)R\_NON\_W\_ALLOC

| #define R\_NON\_W\_ALLOC   0x1U /\* Do not allocate Read, Allocate Write \*/ |
| --- |

## [◆ ](#a1160c997a66c9fd58dbc3dcfd65982a8)R\_NON\_W\_NON

| #define R\_NON\_W\_NON   0x0U /\* Do not allocate Read/Write \*/ |
| --- |

## [◆ ](#aef333777108782979d84344af4bc51d6)REGION\_FLASH\_ATTR

| #define REGION\_FLASH\_ATTR |
| --- |

**Value:**

{ \

.rbar = [P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46) | [NON\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#a5c302dfed348f344a036701d4b9c7ec8), /\* AP, XN, SH \*/ \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_FLASH](arm__mpu__v8_8h.md#ab1521fd2deea0bd6b88c73aed7159f8a), \

}

[NON\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#a5c302dfed348f344a036701d4b9c7ec8)

#define NON\_SHAREABLE\_Msk

**Definition** arm\_mpu\_v8.h:71

## [◆ ](#a4ce0d123898b8cb22cb161c8d69c411f)REGION\_IO\_ATTR

| #define REGION\_IO\_ATTR |
| --- |

**Value:**

{ \

/\* AP, XN, SH \*/ \

.rbar = [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7) | [NON\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#a5c302dfed348f344a036701d4b9c7ec8), \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_DEVICE](arm__mpu__v8_8h.md#a6ae855ff0c11d85dc72a1c45edaa7f75), \

}

[NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)

#define NOT\_EXEC

**Definition** arm\_mpu\_v7m.h:46

## [◆ ](#a859d811feecb32c788b16a413e1b4781)REGION\_RAM\_ATTR

| #define REGION\_RAM\_ATTR |
| --- |

**Value:**

{ \

/\* AP, XN, SH \*/ \

.rbar = [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7) | [OUTER\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#aa4f924c424fc141ffa32a9b5c1180d56), \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03), \

}

[OUTER\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#aa4f924c424fc141ffa32a9b5c1180d56)

#define OUTER\_SHAREABLE\_Msk

**Definition** arm\_mpu\_v8.h:73

## [◆ ](#a89573cb3bde7b26846a3607276c843d9)REGION\_RAM\_NOCACHE\_ATTR

| #define REGION\_RAM\_NOCACHE\_ATTR |
| --- |

**Value:**

{ \

/\* AP, XN, SH \*/ \

.rbar = [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7) | [NON\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#a5c302dfed348f344a036701d4b9c7ec8), \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](arm__mpu__v8_8h.md#a03e37d7769647008655338fe8359d946), \

}

## [◆ ](#a677d1642d4a105f9d5f81404e58b2cf4)REGION\_RAM\_RO\_ATTR

| #define REGION\_RAM\_RO\_ATTR |
| --- |

**Value:**

{ \

/\* AP, XN, SH \*/ \

.rbar = [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46) | [INNER\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#ab0d195350222b02d2d83ecd94a9ca395), \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03), \

}

[INNER\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#ab0d195350222b02d2d83ecd94a9ca395)

#define INNER\_SHAREABLE\_Msk

**Definition** arm\_mpu\_v8.h:75

## [◆ ](#a00fb6882c3ff5d043e319be2ac04ea01)REGION\_RAM\_TEXT\_ATTR

| #define REGION\_RAM\_TEXT\_ATTR |
| --- |

**Value:**

{ \

/\* AP, XN, SH \*/ \

.rbar = [P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46) | [INNER\_SHAREABLE\_Msk](arm__mpu__v8_8h.md#ab0d195350222b02d2d83ecd94a9ca395), \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_SRAM](arm__mpu__v8_8h.md#a386bbcc650a8313774651212bda40d03), \

}

## Typedef Documentation

## [◆ ](#a6b3c416482c4d01cc12db5269886bb05)k\_mem\_partition\_attr\_t

| typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) k\_mem\_partition\_attr\_t |
| --- |

## Variable Documentation

## [◆ ](#ab4f9746862097dfdc048d75c9c08b795)mpu\_config

| | const struct [arm\_mpu\_config](structarm__mpu__config.md) mpu\_config | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [cortex\_r](dir_c43630f15275c571a36c3286c2e4d54b.md)
- [arm\_mpu.h](4_2cortex__r_2arm__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
