---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm__mpu__v8_8h.html
original_path: doxygen/html/arm__mpu__v8_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu\_v8.h File Reference

`#include <cmsis_core.h>`

[Go to the source code of this file.](arm__mpu__v8_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) |
| struct | [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) |

| Macros | |
| --- | --- |
| #define | [P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215)   0x0 |
| #define | [P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7)   (([P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34)   0x1 |
| #define | [P\_RW\_U\_RW\_Msk](#adc9ba826d1bf9a013724b7a24e9535db)   (([P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [FULL\_ACCESS](#a4da15c917ab4e26cd3e5e39dbec83000)   0x1 |
| #define | [FULL\_ACCESS\_Msk](#a1da8e3113a0446b3d2acbe78b4e40b0c)   (([FULL\_ACCESS](#a4da15c917ab4e26cd3e5e39dbec83000) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd)   0x2 |
| #define | [P\_RO\_U\_NA\_Msk](#aeec24407a5fffaf967a841a26ccf46ed)   (([P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211)   0x3 |
| #define | [P\_RO\_U\_RO\_Msk](#a4ec38b9015a95b2aafca5e9aa35f1f46)   (([P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [RO](#a628642b04c07236ae1e986c248a79ae5)   0x3 |
| #define | [RO\_Msk](#a35e3f724856c6947c52885def2e3c0d6)   (([RO](#a628642b04c07236ae1e986c248a79ae5) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| #define | [NOT\_EXEC](#a74c8c1c16d8d613d7b32d5fe9bd5d08d)   [MPU\_RBAR\_XN\_Msk](4_2cortex__r_2arm__mpu_8h.md#ae960690ad7849b21e6cd0c414075de1b) |
| #define | [NON\_SHAREABLE](#ad2047a4b8dae13c488a331b1691000b5)   0x0 |
| #define | [NON\_SHAREABLE\_Msk](#a5c302dfed348f344a036701d4b9c7ec8)   (([NON\_SHAREABLE](#ad2047a4b8dae13c488a331b1691000b5) << [MPU\_RBAR\_SH\_Pos](4_2cortex__r_2arm__mpu_8h.md#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](4_2cortex__r_2arm__mpu_8h.md#aa014b1c92266313a3c1dc06e37e39aef)) |
| #define | [OUTER\_SHAREABLE](#a6d48175f63f47fcbe1fedbbdfcd56a85)   0x2 |
| #define | [OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)   (([OUTER\_SHAREABLE](#a6d48175f63f47fcbe1fedbbdfcd56a85) << [MPU\_RBAR\_SH\_Pos](4_2cortex__r_2arm__mpu_8h.md#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](4_2cortex__r_2arm__mpu_8h.md#aa014b1c92266313a3c1dc06e37e39aef)) |
| #define | [INNER\_SHAREABLE](#a8c245b5c485b439790459255fc645131)   0x3 |
| #define | [INNER\_SHAREABLE\_Msk](#ab0d195350222b02d2d83ecd94a9ca395)   (([INNER\_SHAREABLE](#a8c245b5c485b439790459255fc645131) << [MPU\_RBAR\_SH\_Pos](4_2cortex__r_2arm__mpu_8h.md#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](4_2cortex__r_2arm__mpu_8h.md#aa014b1c92266313a3c1dc06e37e39aef)) |
| #define | [REGION\_LIMIT\_ADDR](#adc21e54d67b5ad7688c15784e8b0459c)(base, size) |
| #define | [DEVICE\_nGnRnE](#a7e8d641f98b092387124bd1ecf2fdb53)   0x0U |
| #define | [DEVICE\_nGnRE](#a1fb228a36a14d8679f6d038c47f5f2e1)   0x4U |
| #define | [DEVICE\_nGRE](#a50d2ee15f01cc5379a74d23efd969051)   0x8U |
| #define | [DEVICE\_GRE](#a3d0243c563668b7358ce29d54f7f1afa)   0xCU |
| #define | [R\_NON\_W\_NON](#a1160c997a66c9fd58dbc3dcfd65982a8)   0x0 /\* Do not allocate Read/Write \*/ |
| #define | [R\_NON\_W\_ALLOC](#a0696dfbe29563622fe76970f9d146ff5)   0x1 /\* Do not allocate Read, Allocate Write \*/ |
| #define | [R\_ALLOC\_W\_NON](#a8476bb45227afc0236bc9f427793d6a9)   0x2 /\* Allocate Read, Do not allocate Write \*/ |
| #define | [R\_ALLOC\_W\_ALLOC](#a1815e3622467845af3b3083fa76f3314)   0x3 /\* Allocate Read/Write \*/ |
| #define | [NORMAL\_O\_WT\_NT](#a4720c776e51ea52fc8cfa2c1dc935d47)   0x80 /\* Normal, Outer Write-through non-transient \*/ |
| #define | [NORMAL\_O\_WB\_NT](#a7d87ec111ffd79cddb9ce9f23e9f20d9)   0xC0 /\* Normal, Outer Write-back non-transient \*/ |
| #define | [NORMAL\_O\_NON\_C](#ae36bc21dc922e88f8d5d4ff0657d80b6)   0x40 /\* Normal, Outer Non-Cacheable \*/ |
| #define | [NORMAL\_I\_WT\_NT](#a2d60ab7f15ac71d451a73758315eff07)   0x08 /\* Normal, Inner Write-through non-transient \*/ |
| #define | [NORMAL\_I\_WB\_NT](#a28f31a1e2a47e2cafa7f41260780fd5f)   0x0C /\* Normal, Inner Write-back non-transient \*/ |
| #define | [NORMAL\_I\_NON\_C](#a8dda4d3d5f372f8ef3070fb492448992)   0x04 /\* Normal, Inner Non-Cacheable \*/ |
| #define | [NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS](#a08d01129e0f1606f274cccd64c8560ef) |
| #define | [NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS](#ad99764b02ad6122b1a952d0f4e79c37f) |
| #define | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE](#a45568f5e60950fbdb89b6e837b87aaac) |
| #define | [MPU\_CACHE\_ATTRIBUTES\_FLASH](#acc7f5f300029c52f64a585be8c18876b)   [NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS](#a08d01129e0f1606f274cccd64c8560ef) |
| #define | [MPU\_CACHE\_ATTRIBUTES\_SRAM](#aaf4cfc11f9981eac67ea432c18edc384)   [NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS](#ad99764b02ad6122b1a952d0f4e79c37f) |
| #define | [MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE](#a9637e9763b6b09741be5589eeceb3873)   [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE](#a45568f5e60950fbdb89b6e837b87aaac) |
| #define | [MPU\_MAIR\_ATTR\_FLASH](#ad384c906ae7e1f4841c8ea98754acc1c)   [MPU\_CACHE\_ATTRIBUTES\_FLASH](#acc7f5f300029c52f64a585be8c18876b) |
| #define | [MPU\_MAIR\_INDEX\_FLASH](#ab1521fd2deea0bd6b88c73aed7159f8a)   0 |
| #define | [MPU\_MAIR\_ATTR\_SRAM](#aca50d2bc85d65c0ad231ecd7deb40c50)   [MPU\_CACHE\_ATTRIBUTES\_SRAM](#aaf4cfc11f9981eac67ea432c18edc384) |
| #define | [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)   1 |
| #define | [MPU\_MAIR\_ATTR\_SRAM\_NOCACHE](#ab6bce12dbd72d216cbb6bc748d801ce0)   [MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE](#a9637e9763b6b09741be5589eeceb3873) |
| #define | [MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)   2 |
| #define | [MPU\_MAIR\_ATTR\_DEVICE](#acfdb4baf0d7ec48fdc77e8e2973a1487)   [DEVICE\_nGnRnE](#a7e8d641f98b092387124bd1ecf2fdb53) |
| #define | [MPU\_MAIR\_INDEX\_DEVICE](#a6ae855ff0c11d85dc72a1c45edaa7f75)   3 |
| #define | [MPU\_MAIR\_ATTRS](#a497d0db2bf062be1a466a1c7cab6a260) |
| #define | [ARM\_MPU\_REGION\_INIT](#a2ec2a5ebe99ddac405570be52bc3a728)(p\_name, p\_base, p\_size, p\_attr) |
| #define | [REGION\_RAM\_ATTR](#a6017a9ca9983921e946771ea57dc4201)(base, size) |
| #define | [REGION\_RAM\_NOCACHE\_ATTR](#a8b4189f8ce0221dc34b199f3961aaf66)(base, size) |
| #define | [REGION\_FLASH\_ATTR](#a0293a2955ef2b9772d2ef4e1aaf9b24c)(base, size) |
| #define | [REGION\_DEVICE\_ATTR](#a3d1bfca872cb0bc3a4e010c3e518ce91)(base, size) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#a9b7cc3c51f518517031d76807470aa10) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#a3c52d13e42a66beb72d088ac56388951) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#a708338371e91b5a3f2d44f9ae48849db) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#a706eaa9c515f1cc859d97ef8455b2f2f) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RWX](#a29db5fb48087c0cae596ff212989ed24) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](#a78f9b21aa8b5c894db28328f5a1e2641) |
| #define | [K\_MEM\_PARTITION\_IS\_WRITABLE](#a7879968909ce2f0e33763ae1e2fc9d84)(attr) |
| #define | [K\_MEM\_PARTITION\_IS\_EXECUTABLE](#ab6fb9b9c6c1c968a11ae80bfd70fec26)(attr) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE](#afb811f7933ed0147b255c170427e0fb6) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE](#a8c982ab9a12ea1da0b7505c915832e89) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE](#a840d782e977d03ed4f9ca5858f61d1a5) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE](#ae47c158f93de002298e0c46a47c6337e) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE](#a5bcd5603dda3c2825a0eca8a7d994d83) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE](#a0b22795be27057cc03e6f49d1e1e455d) |

## Macro Definition Documentation

## [◆ ](#a2ec2a5ebe99ddac405570be52bc3a728)ARM\_MPU\_REGION\_INIT

| #define ARM\_MPU\_REGION\_INIT | ( |  | *p\_name*, |
| --- | --- | --- | --- |
|  |  |  | *p\_base*, |
|  |  |  | *p\_size*, |
|  |  |  | *p\_attr* ) |

**Value:**

{ .name = p\_name, \

.base = p\_base, \

.attr = p\_attr(p\_base, p\_size), \

}

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

## [◆ ](#a4da15c917ab4e26cd3e5e39dbec83000)FULL\_ACCESS

| #define FULL\_ACCESS   0x1 |
| --- |

## [◆ ](#a1da8e3113a0446b3d2acbe78b4e40b0c)FULL\_ACCESS\_Msk

| #define FULL\_ACCESS\_Msk   (([FULL\_ACCESS](#a4da15c917ab4e26cd3e5e39dbec83000) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a8c245b5c485b439790459255fc645131)INNER\_SHAREABLE

| #define INNER\_SHAREABLE   0x3 |
| --- |

## [◆ ](#ab0d195350222b02d2d83ecd94a9ca395)INNER\_SHAREABLE\_Msk

| #define INNER\_SHAREABLE\_Msk   (([INNER\_SHAREABLE](#a8c245b5c485b439790459255fc645131) << [MPU\_RBAR\_SH\_Pos](4_2cortex__r_2arm__mpu_8h.md#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](4_2cortex__r_2arm__mpu_8h.md#aa014b1c92266313a3c1dc06e37e39aef)) |
| --- |

## [◆ ](#ab6fb9b9c6c1c968a11ae80bfd70fec26)K\_MEM\_PARTITION\_IS\_EXECUTABLE

| #define K\_MEM\_PARTITION\_IS\_EXECUTABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(!((attr.rbar) & ([NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d))))

[NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)

#define NOT\_EXEC

**Definition** arm\_mpu\_v7m.h:46

## [◆ ](#a7879968909ce2f0e33763ae1e2fc9d84)K\_MEM\_PARTITION\_IS\_WRITABLE

| #define K\_MEM\_PARTITION\_IS\_WRITABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

int \_\_is\_writable\_\_; \

switch (attr.rbar & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) { \

case [P\_RW\_U\_RW\_Msk](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db): \

case [P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7): \

\_\_is\_writable\_\_ = 1; \

break; \

default: \

\_\_is\_writable\_\_ = 0; \

} \

\_\_is\_writable\_\_; \

})

[MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)

#define MPU\_RBAR\_AP\_Msk

**Definition** arm\_mpu.h:23

[P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7)

#define P\_RW\_U\_NA\_Msk

**Definition** arm\_mpu\_v7m.h:25

[P\_RW\_U\_RW\_Msk](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db)

#define P\_RW\_U\_RW\_Msk

**Definition** arm\_mpu\_v7m.h:31

## [◆ ](#a706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RO\_U\_NA\_Msk](arm__mpu__v7m_8h.md#aeec24407a5fffaf967a841a26ccf46ed) | [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)), [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)})

[P\_RO\_U\_NA\_Msk](arm__mpu__v7m_8h.md#aeec24407a5fffaf967a841a26ccf46ed)

#define P\_RO\_U\_NA\_Msk

**Definition** arm\_mpu\_v7m.h:37

[MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)

#define MPU\_MAIR\_INDEX\_SRAM

**Definition** arm\_mpu\_v8.h:151

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

## [◆ ](#ae47c158f93de002298e0c46a47c6337e)K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RO\_U\_NA\_Msk](arm__mpu__v7m_8h.md#aeec24407a5fffaf967a841a26ccf46ed) | [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)), \

[MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)})

[MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)

#define MPU\_MAIR\_INDEX\_SRAM\_NOCACHE

**Definition** arm\_mpu\_v8.h:153

[OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)

#define OUTER\_SHAREABLE\_Msk

**Definition** arm\_mpu\_v8.h:74

## [◆ ](#a708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46) | [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)), [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)})

[P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46)

#define P\_RO\_U\_RO\_Msk

**Definition** arm\_mpu\_v7m.h:40

## [◆ ](#a840d782e977d03ed4f9ca5858f61d1a5)K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46) | [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)), \

[MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)})

## [◆ ](#a3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7) | [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)), [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)})

## [◆ ](#a8c982ab9a12ea1da0b7505c915832e89)K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7) | [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)), \

[MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)})

## [◆ ](#a9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RW\_U\_RW\_Msk](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db) | [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d)), [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)})

## [◆ ](#afb811f7933ed0147b255c170427e0fb6)K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RW\_U\_RW\_Msk](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db) | [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)), \

[MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)})

## [◆ ](#a29db5fb48087c0cae596ff212989ed24)K\_MEM\_PARTITION\_P\_RWX\_U\_RWX

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RW\_U\_RW\_Msk](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db)), [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)})

## [◆ ](#a5bcd5603dda3c2825a0eca8a7d994d83)K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RW\_U\_RW\_Msk](arm__mpu__v7m_8h.md#adc9ba826d1bf9a013724b7a24e9535db) | [OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)), [MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)})

## [◆ ](#a78f9b21aa8b5c894db28328f5a1e2641)K\_MEM\_PARTITION\_P\_RX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46)), [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03)})

## [◆ ](#a0b22795be27057cc03e6f49d1e1e455d)K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) \

{([P\_RO\_U\_RO\_Msk](arm__mpu__v7m_8h.md#a4ec38b9015a95b2aafca5e9aa35f1f46) | [OUTER\_SHAREABLE\_Msk](#aa4f924c424fc141ffa32a9b5c1180d56)), [MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946)})

## [◆ ](#acc7f5f300029c52f64a585be8c18876b)MPU\_CACHE\_ATTRIBUTES\_FLASH

| #define MPU\_CACHE\_ATTRIBUTES\_FLASH   [NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS](#a08d01129e0f1606f274cccd64c8560ef) |
| --- |

## [◆ ](#aaf4cfc11f9981eac67ea432c18edc384)MPU\_CACHE\_ATTRIBUTES\_SRAM

| #define MPU\_CACHE\_ATTRIBUTES\_SRAM   [NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS](#ad99764b02ad6122b1a952d0f4e79c37f) |
| --- |

## [◆ ](#a9637e9763b6b09741be5589eeceb3873)MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE

| #define MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE   [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE](#a45568f5e60950fbdb89b6e837b87aaac) |
| --- |

## [◆ ](#acfdb4baf0d7ec48fdc77e8e2973a1487)MPU\_MAIR\_ATTR\_DEVICE

| #define MPU\_MAIR\_ATTR\_DEVICE   [DEVICE\_nGnRnE](#a7e8d641f98b092387124bd1ecf2fdb53) |
| --- |

## [◆ ](#ad384c906ae7e1f4841c8ea98754acc1c)MPU\_MAIR\_ATTR\_FLASH

| #define MPU\_MAIR\_ATTR\_FLASH   [MPU\_CACHE\_ATTRIBUTES\_FLASH](#acc7f5f300029c52f64a585be8c18876b) |
| --- |

## [◆ ](#aca50d2bc85d65c0ad231ecd7deb40c50)MPU\_MAIR\_ATTR\_SRAM

| #define MPU\_MAIR\_ATTR\_SRAM   [MPU\_CACHE\_ATTRIBUTES\_SRAM](#aaf4cfc11f9981eac67ea432c18edc384) |
| --- |

## [◆ ](#ab6bce12dbd72d216cbb6bc748d801ce0)MPU\_MAIR\_ATTR\_SRAM\_NOCACHE

| #define MPU\_MAIR\_ATTR\_SRAM\_NOCACHE   [MPU\_CACHE\_ATTRIBUTES\_SRAM\_NOCACHE](#a9637e9763b6b09741be5589eeceb3873) |
| --- |

## [◆ ](#a497d0db2bf062be1a466a1c7cab6a260)MPU\_MAIR\_ATTRS

| #define MPU\_MAIR\_ATTRS |
| --- |

**Value:**

(([MPU\_MAIR\_ATTR\_FLASH](#ad384c906ae7e1f4841c8ea98754acc1c) << ([MPU\_MAIR\_INDEX\_FLASH](#ab1521fd2deea0bd6b88c73aed7159f8a) \* 8)) | \

([MPU\_MAIR\_ATTR\_SRAM](#aca50d2bc85d65c0ad231ecd7deb40c50) << ([MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03) \* 8)) | \

([MPU\_MAIR\_ATTR\_SRAM\_NOCACHE](#ab6bce12dbd72d216cbb6bc748d801ce0) << ([MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946) \* 8)) | \

([MPU\_MAIR\_ATTR\_DEVICE](#acfdb4baf0d7ec48fdc77e8e2973a1487) << ([MPU\_MAIR\_INDEX\_DEVICE](#a6ae855ff0c11d85dc72a1c45edaa7f75) \* 8)))

[MPU\_MAIR\_INDEX\_DEVICE](#a6ae855ff0c11d85dc72a1c45edaa7f75)

#define MPU\_MAIR\_INDEX\_DEVICE

**Definition** arm\_mpu\_v8.h:155

[MPU\_MAIR\_INDEX\_FLASH](#ab1521fd2deea0bd6b88c73aed7159f8a)

#define MPU\_MAIR\_INDEX\_FLASH

**Definition** arm\_mpu\_v8.h:149

[MPU\_MAIR\_ATTR\_SRAM\_NOCACHE](#ab6bce12dbd72d216cbb6bc748d801ce0)

#define MPU\_MAIR\_ATTR\_SRAM\_NOCACHE

**Definition** arm\_mpu\_v8.h:152

[MPU\_MAIR\_ATTR\_SRAM](#aca50d2bc85d65c0ad231ecd7deb40c50)

#define MPU\_MAIR\_ATTR\_SRAM

**Definition** arm\_mpu\_v8.h:150

[MPU\_MAIR\_ATTR\_DEVICE](#acfdb4baf0d7ec48fdc77e8e2973a1487)

#define MPU\_MAIR\_ATTR\_DEVICE

**Definition** arm\_mpu\_v8.h:154

[MPU\_MAIR\_ATTR\_FLASH](#ad384c906ae7e1f4841c8ea98754acc1c)

#define MPU\_MAIR\_ATTR\_FLASH

**Definition** arm\_mpu\_v8.h:148

## [◆ ](#a6ae855ff0c11d85dc72a1c45edaa7f75)MPU\_MAIR\_INDEX\_DEVICE

| #define MPU\_MAIR\_INDEX\_DEVICE   3 |
| --- |

## [◆ ](#ab1521fd2deea0bd6b88c73aed7159f8a)MPU\_MAIR\_INDEX\_FLASH

| #define MPU\_MAIR\_INDEX\_FLASH   0 |
| --- |

## [◆ ](#a386bbcc650a8313774651212bda40d03)MPU\_MAIR\_INDEX\_SRAM

| #define MPU\_MAIR\_INDEX\_SRAM   1 |
| --- |

## [◆ ](#a03e37d7769647008655338fe8359d946)MPU\_MAIR\_INDEX\_SRAM\_NOCACHE

| #define MPU\_MAIR\_INDEX\_SRAM\_NOCACHE   2 |
| --- |

## [◆ ](#ad2047a4b8dae13c488a331b1691000b5)NON\_SHAREABLE

| #define NON\_SHAREABLE   0x0 |
| --- |

## [◆ ](#a5c302dfed348f344a036701d4b9c7ec8)NON\_SHAREABLE\_Msk

| #define NON\_SHAREABLE\_Msk   (([NON\_SHAREABLE](#ad2047a4b8dae13c488a331b1691000b5) << [MPU\_RBAR\_SH\_Pos](4_2cortex__r_2arm__mpu_8h.md#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](4_2cortex__r_2arm__mpu_8h.md#aa014b1c92266313a3c1dc06e37e39aef)) |
| --- |

## [◆ ](#a8dda4d3d5f372f8ef3070fb492448992)NORMAL\_I\_NON\_C

| #define NORMAL\_I\_NON\_C   0x04 /\* Normal, Inner Non-Cacheable \*/ |
| --- |

## [◆ ](#a28f31a1e2a47e2cafa7f41260780fd5f)NORMAL\_I\_WB\_NT

| #define NORMAL\_I\_WB\_NT   0x0C /\* Normal, Inner Write-back non-transient \*/ |
| --- |

## [◆ ](#a2d60ab7f15ac71d451a73758315eff07)NORMAL\_I\_WT\_NT

| #define NORMAL\_I\_WT\_NT   0x08 /\* Normal, Inner Write-through non-transient \*/ |
| --- |

## [◆ ](#ae36bc21dc922e88f8d5d4ff0657d80b6)NORMAL\_O\_NON\_C

| #define NORMAL\_O\_NON\_C   0x40 /\* Normal, Outer Non-Cacheable \*/ |
| --- |

## [◆ ](#a7d87ec111ffd79cddb9ce9f23e9f20d9)NORMAL\_O\_WB\_NT

| #define NORMAL\_O\_WB\_NT   0xC0 /\* Normal, Outer Write-back non-transient \*/ |
| --- |

## [◆ ](#a4720c776e51ea52fc8cfa2c1dc935d47)NORMAL\_O\_WT\_NT

| #define NORMAL\_O\_WT\_NT   0x80 /\* Normal, Outer Write-through non-transient \*/ |
| --- |

## [◆ ](#a45568f5e60950fbdb89b6e837b87aaac)NORMAL\_OUTER\_INNER\_NON\_CACHEABLE

| #define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE |
| --- |

**Value:**

(([NORMAL\_O\_NON\_C](#ae36bc21dc922e88f8d5d4ff0657d80b6) | ([R\_NON\_W\_NON](#a1160c997a66c9fd58dbc3dcfd65982a8) << 4)) \

| \

([NORMAL\_I\_NON\_C](#a8dda4d3d5f372f8ef3070fb492448992) | [R\_NON\_W\_NON](#a1160c997a66c9fd58dbc3dcfd65982a8)))

[R\_NON\_W\_NON](#a1160c997a66c9fd58dbc3dcfd65982a8)

#define R\_NON\_W\_NON

**Definition** arm\_mpu\_v8.h:110

[NORMAL\_I\_NON\_C](#a8dda4d3d5f372f8ef3070fb492448992)

#define NORMAL\_I\_NON\_C

**Definition** arm\_mpu\_v8.h:122

[NORMAL\_O\_NON\_C](#ae36bc21dc922e88f8d5d4ff0657d80b6)

#define NORMAL\_O\_NON\_C

**Definition** arm\_mpu\_v8.h:118

## [◆ ](#ad99764b02ad6122b1a952d0f4e79c37f)NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS

| #define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_TRANS |
| --- |

**Value:**

(([NORMAL\_O\_WB\_NT](#a7d87ec111ffd79cddb9ce9f23e9f20d9) | ([R\_ALLOC\_W\_ALLOC](#a1815e3622467845af3b3083fa76f3314) << 4)) \

| \

([NORMAL\_I\_WB\_NT](#a28f31a1e2a47e2cafa7f41260780fd5f) | [R\_ALLOC\_W\_ALLOC](#a1815e3622467845af3b3083fa76f3314)))

[R\_ALLOC\_W\_ALLOC](#a1815e3622467845af3b3083fa76f3314)

#define R\_ALLOC\_W\_ALLOC

**Definition** arm\_mpu\_v8.h:113

[NORMAL\_I\_WB\_NT](#a28f31a1e2a47e2cafa7f41260780fd5f)

#define NORMAL\_I\_WB\_NT

**Definition** arm\_mpu\_v8.h:121

[NORMAL\_O\_WB\_NT](#a7d87ec111ffd79cddb9ce9f23e9f20d9)

#define NORMAL\_O\_WB\_NT

**Definition** arm\_mpu\_v8.h:117

## [◆ ](#a08d01129e0f1606f274cccd64c8560ef)NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS

| #define NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_READ\_ALLOCATE\_NON\_TRANS |
| --- |

**Value:**

(([NORMAL\_O\_WT\_NT](#a4720c776e51ea52fc8cfa2c1dc935d47) | ([R\_ALLOC\_W\_NON](#a8476bb45227afc0236bc9f427793d6a9) << 4)) \

| \

([NORMAL\_I\_WT\_NT](#a2d60ab7f15ac71d451a73758315eff07) | [R\_ALLOC\_W\_NON](#a8476bb45227afc0236bc9f427793d6a9))) \

[NORMAL\_I\_WT\_NT](#a2d60ab7f15ac71d451a73758315eff07)

#define NORMAL\_I\_WT\_NT

**Definition** arm\_mpu\_v8.h:120

[NORMAL\_O\_WT\_NT](#a4720c776e51ea52fc8cfa2c1dc935d47)

#define NORMAL\_O\_WT\_NT

**Definition** arm\_mpu\_v8.h:116

[R\_ALLOC\_W\_NON](#a8476bb45227afc0236bc9f427793d6a9)

#define R\_ALLOC\_W\_NON

**Definition** arm\_mpu\_v8.h:112

## [◆ ](#a74c8c1c16d8d613d7b32d5fe9bd5d08d)NOT\_EXEC

| #define NOT\_EXEC   [MPU\_RBAR\_XN\_Msk](4_2cortex__r_2arm__mpu_8h.md#ae960690ad7849b21e6cd0c414075de1b) |
| --- |

## [◆ ](#a6d48175f63f47fcbe1fedbbdfcd56a85)OUTER\_SHAREABLE

| #define OUTER\_SHAREABLE   0x2 |
| --- |

## [◆ ](#aa4f924c424fc141ffa32a9b5c1180d56)OUTER\_SHAREABLE\_Msk

| #define OUTER\_SHAREABLE\_Msk   (([OUTER\_SHAREABLE](#a6d48175f63f47fcbe1fedbbdfcd56a85) << [MPU\_RBAR\_SH\_Pos](4_2cortex__r_2arm__mpu_8h.md#a3150317eff21434c7ca4b24516603615)) & [MPU\_RBAR\_SH\_Msk](4_2cortex__r_2arm__mpu_8h.md#aa014b1c92266313a3c1dc06e37e39aef)) |
| --- |

## [◆ ](#ad3012e82dde223bbe84c9e4d7c46e7fd)P\_RO\_U\_NA

| #define P\_RO\_U\_NA   0x2 |
| --- |

## [◆ ](#aeec24407a5fffaf967a841a26ccf46ed)P\_RO\_U\_NA\_Msk

| #define P\_RO\_U\_NA\_Msk   (([P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a75fd88fb93da28e84017d4ba6fcb4211)P\_RO\_U\_RO

| #define P\_RO\_U\_RO   0x3 |
| --- |

## [◆ ](#a4ec38b9015a95b2aafca5e9aa35f1f46)P\_RO\_U\_RO\_Msk

| #define P\_RO\_U\_RO\_Msk   (([P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a6632f2c0eba4d5aee046a86258100215)P\_RW\_U\_NA

| #define P\_RW\_U\_NA   0x0 |
| --- |

## [◆ ](#a8a5805b5b1a6ca5cf5f59b2874ec68d7)P\_RW\_U\_NA\_Msk

| #define P\_RW\_U\_NA\_Msk   (([P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a8faee650ae8cc79e1d3605f251c3df34)P\_RW\_U\_RW

| #define P\_RW\_U\_RW   0x1 |
| --- |

## [◆ ](#adc9ba826d1bf9a013724b7a24e9535db)P\_RW\_U\_RW\_Msk

| #define P\_RW\_U\_RW\_Msk   (([P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

## [◆ ](#a1815e3622467845af3b3083fa76f3314)R\_ALLOC\_W\_ALLOC

| #define R\_ALLOC\_W\_ALLOC   0x3 /\* Allocate Read/Write \*/ |
| --- |

## [◆ ](#a8476bb45227afc0236bc9f427793d6a9)R\_ALLOC\_W\_NON

| #define R\_ALLOC\_W\_NON   0x2 /\* Allocate Read, Do not allocate Write \*/ |
| --- |

## [◆ ](#a0696dfbe29563622fe76970f9d146ff5)R\_NON\_W\_ALLOC

| #define R\_NON\_W\_ALLOC   0x1 /\* Do not allocate Read, Allocate Write \*/ |
| --- |

## [◆ ](#a1160c997a66c9fd58dbc3dcfd65982a8)R\_NON\_W\_NON

| #define R\_NON\_W\_NON   0x0 /\* Do not allocate Read/Write \*/ |
| --- |

## [◆ ](#a3d1bfca872cb0bc3a4e010c3e518ce91)REGION\_DEVICE\_ATTR

| #define REGION\_DEVICE\_ATTR | ( |  | *base*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

**Value:**

{ \

/\* AP, XN, SH \*/ \

.rbar = [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | [P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7) | [NON\_SHAREABLE\_Msk](#a5c302dfed348f344a036701d4b9c7ec8), /\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_DEVICE](#a6ae855ff0c11d85dc72a1c45edaa7f75), \

.r\_limit = [REGION\_LIMIT\_ADDR](#adc21e54d67b5ad7688c15784e8b0459c)(base, size), /\* Region Limit \*/ \

}

[NON\_SHAREABLE\_Msk](#a5c302dfed348f344a036701d4b9c7ec8)

#define NON\_SHAREABLE\_Msk

**Definition** arm\_mpu\_v8.h:71

[REGION\_LIMIT\_ADDR](#adc21e54d67b5ad7688c15784e8b0459c)

#define REGION\_LIMIT\_ADDR(base, size)

**Definition** arm\_mpu\_v8.h:81

## [◆ ](#a0293a2955ef2b9772d2ef4e1aaf9b24c)REGION\_FLASH\_ATTR

| #define REGION\_FLASH\_ATTR | ( |  | *base*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

**Value:**

{\

.rbar = [RO\_Msk](arm__mpu__v7m_8h.md#a35e3f724856c6947c52885def2e3c0d6) | [NON\_SHAREABLE\_Msk](#a5c302dfed348f344a036701d4b9c7ec8), /\* AP, XN, SH \*/ \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_FLASH](#ab1521fd2deea0bd6b88c73aed7159f8a), \

.r\_limit = [REGION\_LIMIT\_ADDR](#adc21e54d67b5ad7688c15784e8b0459c)(base, size), /\* Region Limit \*/ \

}

[RO\_Msk](arm__mpu__v7m_8h.md#a35e3f724856c6947c52885def2e3c0d6)

#define RO\_Msk

**Definition** arm\_mpu\_v7m.h:43

## [◆ ](#adc21e54d67b5ad7688c15784e8b0459c)REGION\_LIMIT\_ADDR

| #define REGION\_LIMIT\_ADDR | ( |  | *base*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

**Value:**

(((base & [MPU\_RBAR\_BASE\_Msk](4_2cortex__r_2arm__mpu_8h.md#a57f2217a12342e8e43c7ad6949a9a65b)) + size - 1) & [MPU\_RLAR\_LIMIT\_Msk](4_2cortex__r_2arm__mpu_8h.md#a9612abff664c827b36844fe42d8ee5cb))

[MPU\_RBAR\_BASE\_Msk](4_2cortex__r_2arm__mpu_8h.md#a57f2217a12342e8e43c7ad6949a9a65b)

#define MPU\_RBAR\_BASE\_Msk

**Definition** arm\_mpu.h:19

[MPU\_RLAR\_LIMIT\_Msk](4_2cortex__r_2arm__mpu_8h.md#a9612abff664c827b36844fe42d8ee5cb)

#define MPU\_RLAR\_LIMIT\_Msk

**Definition** arm\_mpu.h:30

## [◆ ](#a6017a9ca9983921e946771ea57dc4201)REGION\_RAM\_ATTR

| #define REGION\_RAM\_ATTR | ( |  | *base*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

**Value:**

{\

.rbar = [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_XIP, ([NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) |)) \

[P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7) | [NON\_SHAREABLE\_Msk](#a5c302dfed348f344a036701d4b9c7ec8), /\* AP, XN, SH \*/ \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_SRAM](#a386bbcc650a8313774651212bda40d03), \

.r\_limit = [REGION\_LIMIT\_ADDR](#adc21e54d67b5ad7688c15784e8b0459c)(base, size), /\* Region Limit \*/ \

}

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:239

## [◆ ](#a8b4189f8ce0221dc34b199f3961aaf66)REGION\_RAM\_NOCACHE\_ATTR

| #define REGION\_RAM\_NOCACHE\_ATTR | ( |  | *base*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

**Value:**

{\

.rbar = [NOT\_EXEC](arm__mpu__v7m_8h.md#a74c8c1c16d8d613d7b32d5fe9bd5d08d) | \

[P\_RW\_U\_NA\_Msk](arm__mpu__v7m_8h.md#a8a5805b5b1a6ca5cf5f59b2874ec68d7) | [NON\_SHAREABLE\_Msk](#a5c302dfed348f344a036701d4b9c7ec8), /\* AP, XN, SH \*/ \

/\* Cache-ability \*/ \

.mair\_idx = [MPU\_MAIR\_INDEX\_SRAM\_NOCACHE](#a03e37d7769647008655338fe8359d946), \

.r\_limit = [REGION\_LIMIT\_ADDR](#adc21e54d67b5ad7688c15784e8b0459c)(base, size), /\* Region Limit \*/ \

}

## [◆ ](#a628642b04c07236ae1e986c248a79ae5)RO

| #define RO   0x3 |
| --- |

## [◆ ](#a35e3f724856c6947c52885def2e3c0d6)RO\_Msk

| #define RO\_Msk   (([RO](#a628642b04c07236ae1e986c248a79ae5) << [MPU\_RBAR\_AP\_Pos](4_2cortex__r_2arm__mpu_8h.md#a33723f1259fdb840b50a6e34786755aa)) & [MPU\_RBAR\_AP\_Msk](4_2cortex__r_2arm__mpu_8h.md#a76c759e3484530af0b2806ecf0018f75)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [arm\_mpu\_v8.h](arm__mpu__v8_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
