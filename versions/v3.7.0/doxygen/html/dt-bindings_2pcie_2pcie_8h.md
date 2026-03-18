---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dt-bindings_2pcie_2pcie_8h.html
original_path: doxygen/html/dt-bindings_2pcie_2pcie_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie.h File Reference

[Go to the source code of this file.](dt-bindings_2pcie_2pcie_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PCIE\_IRQ\_DETECT](#af0887b3d40d4ea7e2c45b750428c7268)   0xFFFFFFFU |
| #define | [PCIE\_ID\_VEND\_SHIFT](#a1c7936d783359e8fa84236dfa852c701)   0U |
| #define | [PCIE\_ID\_VEND\_MASK](#a4d9c60447a305f7f969f0f49d04afba6)   0xFFFFU |
| #define | [PCIE\_ID\_DEV\_SHIFT](#ab6c544956c1bdc670bd3ce8f541b8807)   16U |
| #define | [PCIE\_ID\_DEV\_MASK](#a6ebb481752bacbea6d7b3febb4a8ad5c)   0xFFFFU |
| #define | [CAST](#a5cc7a8d3810218cc9582df360ad58cb8)(type, v) |
| #define | [PCIE\_ID](#af3107df4821c35c5f217a2b8bc49bce6)(vend, dev) |
| #define | [PCIE\_ID\_TO\_VEND](#aa99534d1e5bfed4e1a57d8534a534045)(id) |
| #define | [PCIE\_ID\_TO\_DEV](#aa2198fcdc69f0d86d120355342781a62)(id) |
| #define | [PCIE\_ID\_NONE](#a23ce79d01609cb14f0cd4b2298e13b14)   [PCIE\_ID](#af3107df4821c35c5f217a2b8bc49bce6)(0xFFFF, 0xFFFF) |
| #define | [PCIE\_BDF\_NONE](#a6268e6c107a85fbc6035eca5e6b3cfd6)   0xFFFFFFFFU |
| #define | [PCIE\_BDF\_BUS\_SHIFT](#ada4a5da3eabff1240e651b18e8b10ca7)   16U |
| #define | [PCIE\_BDF\_BUS\_MASK](#a193dd359d7a96bdd904662717c7fbf6d)   0xFFU |
| #define | [PCIE\_BDF\_DEV\_SHIFT](#a7b6be889b801a52f7a713cbf7f2924f6)   11U |
| #define | [PCIE\_BDF\_DEV\_MASK](#a85cc69963a93046bda0f1594803af9eb)   0x1FU |
| #define | [PCIE\_BDF\_FUNC\_SHIFT](#aa14155ded76c4587c49d0a71e25166cc)   8U |
| #define | [PCIE\_BDF\_FUNC\_MASK](#ab481360fa29cf086cc5369e6f1860a5f)   0x7U |
| #define | [PCIE\_BDF](#a09a440a45623a282c23eaa2cfeef63d2)(bus, dev, func) |
| #define | [PCIE\_BDF\_TO\_BUS](#a1c5051a72c50d6ee6cb72cd8d5c41a16)(bdf) |
| #define | [PCIE\_BDF\_TO\_DEV](#ad97fbff75fe4aa3bacad0f952e7349e9)(bdf) |
| #define | [PCIE\_BDF\_TO\_FUNC](#ab5faa8800faa83015623439447dc0fe7)(bdf) |

## Macro Definition Documentation

## [◆ ](#a5cc7a8d3810218cc9582df360ad58cb8)CAST

| #define CAST | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *v* ) |

**Value:**

((type)(v))

## [◆ ](#a09a440a45623a282c23eaa2cfeef63d2)PCIE\_BDF

| #define PCIE\_BDF | ( |  | *bus*, |
| --- | --- | --- | --- |
|  |  |  | *dev*, |
|  |  |  | *func* ) |

**Value:**

((((bus) & [PCIE\_BDF\_BUS\_MASK](#a193dd359d7a96bdd904662717c7fbf6d)) << [PCIE\_BDF\_BUS\_SHIFT](#ada4a5da3eabff1240e651b18e8b10ca7)) | \

(((dev) & [PCIE\_BDF\_DEV\_MASK](#a85cc69963a93046bda0f1594803af9eb)) << [PCIE\_BDF\_DEV\_SHIFT](#a7b6be889b801a52f7a713cbf7f2924f6)) | \

(((func) & [PCIE\_BDF\_FUNC\_MASK](#ab481360fa29cf086cc5369e6f1860a5f)) << [PCIE\_BDF\_FUNC\_SHIFT](#aa14155ded76c4587c49d0a71e25166cc)))

[PCIE\_BDF\_BUS\_MASK](#a193dd359d7a96bdd904662717c7fbf6d)

#define PCIE\_BDF\_BUS\_MASK

**Definition** pcie.h:59

[PCIE\_BDF\_DEV\_SHIFT](#a7b6be889b801a52f7a713cbf7f2924f6)

#define PCIE\_BDF\_DEV\_SHIFT

**Definition** pcie.h:60

[PCIE\_BDF\_DEV\_MASK](#a85cc69963a93046bda0f1594803af9eb)

#define PCIE\_BDF\_DEV\_MASK

**Definition** pcie.h:61

[PCIE\_BDF\_FUNC\_SHIFT](#aa14155ded76c4587c49d0a71e25166cc)

#define PCIE\_BDF\_FUNC\_SHIFT

**Definition** pcie.h:62

[PCIE\_BDF\_FUNC\_MASK](#ab481360fa29cf086cc5369e6f1860a5f)

#define PCIE\_BDF\_FUNC\_MASK

**Definition** pcie.h:63

[PCIE\_BDF\_BUS\_SHIFT](#ada4a5da3eabff1240e651b18e8b10ca7)

#define PCIE\_BDF\_BUS\_SHIFT

**Definition** pcie.h:58

## [◆ ](#a193dd359d7a96bdd904662717c7fbf6d)PCIE\_BDF\_BUS\_MASK

| #define PCIE\_BDF\_BUS\_MASK   0xFFU |
| --- |

## [◆ ](#ada4a5da3eabff1240e651b18e8b10ca7)PCIE\_BDF\_BUS\_SHIFT

| #define PCIE\_BDF\_BUS\_SHIFT   16U |
| --- |

## [◆ ](#a85cc69963a93046bda0f1594803af9eb)PCIE\_BDF\_DEV\_MASK

| #define PCIE\_BDF\_DEV\_MASK   0x1FU |
| --- |

## [◆ ](#a7b6be889b801a52f7a713cbf7f2924f6)PCIE\_BDF\_DEV\_SHIFT

| #define PCIE\_BDF\_DEV\_SHIFT   11U |
| --- |

## [◆ ](#ab481360fa29cf086cc5369e6f1860a5f)PCIE\_BDF\_FUNC\_MASK

| #define PCIE\_BDF\_FUNC\_MASK   0x7U |
| --- |

## [◆ ](#aa14155ded76c4587c49d0a71e25166cc)PCIE\_BDF\_FUNC\_SHIFT

| #define PCIE\_BDF\_FUNC\_SHIFT   8U |
| --- |

## [◆ ](#a6268e6c107a85fbc6035eca5e6b3cfd6)PCIE\_BDF\_NONE

| #define PCIE\_BDF\_NONE   0xFFFFFFFFU |
| --- |

## [◆ ](#a1c5051a72c50d6ee6cb72cd8d5c41a16)PCIE\_BDF\_TO\_BUS

| #define PCIE\_BDF\_TO\_BUS | ( |  | *bdf* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((bdf) >> [PCIE\_BDF\_BUS\_SHIFT](#ada4a5da3eabff1240e651b18e8b10ca7)) & [PCIE\_BDF\_BUS\_MASK](#a193dd359d7a96bdd904662717c7fbf6d))

## [◆ ](#ad97fbff75fe4aa3bacad0f952e7349e9)PCIE\_BDF\_TO\_DEV

| #define PCIE\_BDF\_TO\_DEV | ( |  | *bdf* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((bdf) >> [PCIE\_BDF\_DEV\_SHIFT](#a7b6be889b801a52f7a713cbf7f2924f6)) & [PCIE\_BDF\_DEV\_MASK](#a85cc69963a93046bda0f1594803af9eb))

## [◆ ](#ab5faa8800faa83015623439447dc0fe7)PCIE\_BDF\_TO\_FUNC

| #define PCIE\_BDF\_TO\_FUNC | ( |  | *bdf* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((bdf) >> [PCIE\_BDF\_FUNC\_SHIFT](#aa14155ded76c4587c49d0a71e25166cc)) & [PCIE\_BDF\_FUNC\_MASK](#ab481360fa29cf086cc5369e6f1860a5f))

## [◆ ](#af3107df4821c35c5f217a2b8bc49bce6)PCIE\_ID

| #define PCIE\_ID | ( |  | *vend*, |
| --- | --- | --- | --- |
|  |  |  | *dev* ) |

**Value:**

((((vend) & [PCIE\_ID\_VEND\_MASK](#a4d9c60447a305f7f969f0f49d04afba6)) << [PCIE\_ID\_VEND\_SHIFT](#a1c7936d783359e8fa84236dfa852c701)) | \

([CAST](#a5cc7a8d3810218cc9582df360ad58cb8)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f), (dev) & [PCIE\_ID\_DEV\_MASK](#a6ebb481752bacbea6d7b3febb4a8ad5c)) << [PCIE\_ID\_DEV\_SHIFT](#ab6c544956c1bdc670bd3ce8f541b8807)))

[PCIE\_ID\_VEND\_SHIFT](#a1c7936d783359e8fa84236dfa852c701)

#define PCIE\_ID\_VEND\_SHIFT

**Definition** pcie.h:24

[PCIE\_ID\_VEND\_MASK](#a4d9c60447a305f7f969f0f49d04afba6)

#define PCIE\_ID\_VEND\_MASK

**Definition** pcie.h:25

[CAST](#a5cc7a8d3810218cc9582df360ad58cb8)

#define CAST(type, v)

**Definition** pcie.h:32

[PCIE\_ID\_DEV\_MASK](#a6ebb481752bacbea6d7b3febb4a8ad5c)

#define PCIE\_ID\_DEV\_MASK

**Definition** pcie.h:27

[PCIE\_ID\_DEV\_SHIFT](#ab6c544956c1bdc670bd3ce8f541b8807)

#define PCIE\_ID\_DEV\_SHIFT

**Definition** pcie.h:26

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## [◆ ](#a6ebb481752bacbea6d7b3febb4a8ad5c)PCIE\_ID\_DEV\_MASK

| #define PCIE\_ID\_DEV\_MASK   0xFFFFU |
| --- |

## [◆ ](#ab6c544956c1bdc670bd3ce8f541b8807)PCIE\_ID\_DEV\_SHIFT

| #define PCIE\_ID\_DEV\_SHIFT   16U |
| --- |

## [◆ ](#a23ce79d01609cb14f0cd4b2298e13b14)PCIE\_ID\_NONE

| #define PCIE\_ID\_NONE   [PCIE\_ID](#af3107df4821c35c5f217a2b8bc49bce6)(0xFFFF, 0xFFFF) |
| --- |

## [◆ ](#aa2198fcdc69f0d86d120355342781a62)PCIE\_ID\_TO\_DEV

| #define PCIE\_ID\_TO\_DEV | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((id) >> [PCIE\_ID\_DEV\_SHIFT](#ab6c544956c1bdc670bd3ce8f541b8807)) & [PCIE\_ID\_DEV\_MASK](#a6ebb481752bacbea6d7b3febb4a8ad5c))

## [◆ ](#aa99534d1e5bfed4e1a57d8534a534045)PCIE\_ID\_TO\_VEND

| #define PCIE\_ID\_TO\_VEND | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((id) >> [PCIE\_ID\_VEND\_SHIFT](#a1c7936d783359e8fa84236dfa852c701)) & [PCIE\_ID\_VEND\_MASK](#a4d9c60447a305f7f969f0f49d04afba6))

## [◆ ](#a4d9c60447a305f7f969f0f49d04afba6)PCIE\_ID\_VEND\_MASK

| #define PCIE\_ID\_VEND\_MASK   0xFFFFU |
| --- |

## [◆ ](#a1c7936d783359e8fa84236dfa852c701)PCIE\_ID\_VEND\_SHIFT

| #define PCIE\_ID\_VEND\_SHIFT   0U |
| --- |

## [◆ ](#af0887b3d40d4ea7e2c45b750428c7268)PCIE\_IRQ\_DETECT

| #define PCIE\_IRQ\_DETECT   0xFFFFFFFU |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pcie](dir_f9fb0c2f559a5655635ae30044ebff42.md)
- [pcie.h](dt-bindings_2pcie_2pcie_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
