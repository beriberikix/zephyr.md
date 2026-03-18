---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dma__mcux__pxp_8h.html
original_path: doxygen/html/dma__mcux__pxp_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_mcux\_pxp.h File Reference

[Go to the source code of this file.](dma__mcux__pxp_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DMA\_MCUX\_PXP\_CMD\_MASK](#a1a447b1990a0a58a58b8f2c1b91f4596)   0xE0 |
| #define | [DMA\_MCUX\_PXP\_CMD\_SHIFT](#a98023d4702873f806316fa8076217f2b)   0x5 |
| #define | [DMA\_MCUX\_PXP\_FMT\_MASK](#a99a43acbabab4f6d3d16601776e64ef5)   0x1F |
| #define | [DMA\_MCUX\_PXP\_FMT\_SHIFT](#a5ecb10ea31b3b4841d1d1e50ef182b39)   0x0 |
| #define | [DMA\_MCUX\_PXP\_FMT](#ae33fe6641b02a3af1910ba0ab30306a2)(x) |
| #define | [DMA\_MCUX\_PXP\_CMD](#a3b6888b7002f91c46c891497420a59a4)(x) |
| #define | [DMA\_MCUX\_PXP\_CMD\_ROTATE\_0](#ad0e771ececbc5a7f6257d76b7d3667d7)   0 |
| #define | [DMA\_MCUX\_PXP\_CMD\_ROTATE\_90](#a26e4776708c27df4c2a17437ea944092)   1 |
| #define | [DMA\_MCUX\_PXP\_CMD\_ROTATE\_180](#ab37674ee7555385cefe3cbc328201e31)   2 |
| #define | [DMA\_MCUX\_PXP\_CMD\_ROTATE\_270](#af53cad3d27fbd9d2ae8ca108201f882f)   3 |
| #define | [DMA\_MCUX\_PXP\_FMT\_RGB565](#a39a2b6f27b7dae092f9cfe491bbd078f)   0 |
| #define | [DMA\_MCUX\_PXP\_FMT\_RGB888](#a3667a7b1faf41211b55c22d5f22edd3b)   1 |

## Macro Definition Documentation

## [◆ ](#a3b6888b7002f91c46c891497420a59a4)DMA\_MCUX\_PXP\_CMD

| #define DMA\_MCUX\_PXP\_CMD | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x << [DMA\_MCUX\_PXP\_CMD\_SHIFT](#a98023d4702873f806316fa8076217f2b)) & [DMA\_MCUX\_PXP\_CMD\_MASK](#a1a447b1990a0a58a58b8f2c1b91f4596))

[DMA\_MCUX\_PXP\_CMD\_MASK](#a1a447b1990a0a58a58b8f2c1b91f4596)

#define DMA\_MCUX\_PXP\_CMD\_MASK

**Definition** dma\_mcux\_pxp.h:10

[DMA\_MCUX\_PXP\_CMD\_SHIFT](#a98023d4702873f806316fa8076217f2b)

#define DMA\_MCUX\_PXP\_CMD\_SHIFT

**Definition** dma\_mcux\_pxp.h:11

## [◆ ](#a1a447b1990a0a58a58b8f2c1b91f4596)DMA\_MCUX\_PXP\_CMD\_MASK

| #define DMA\_MCUX\_PXP\_CMD\_MASK   0xE0 |
| --- |

## [◆ ](#ad0e771ececbc5a7f6257d76b7d3667d7)DMA\_MCUX\_PXP\_CMD\_ROTATE\_0

| #define DMA\_MCUX\_PXP\_CMD\_ROTATE\_0   0 |
| --- |

## [◆ ](#ab37674ee7555385cefe3cbc328201e31)DMA\_MCUX\_PXP\_CMD\_ROTATE\_180

| #define DMA\_MCUX\_PXP\_CMD\_ROTATE\_180   2 |
| --- |

## [◆ ](#af53cad3d27fbd9d2ae8ca108201f882f)DMA\_MCUX\_PXP\_CMD\_ROTATE\_270

| #define DMA\_MCUX\_PXP\_CMD\_ROTATE\_270   3 |
| --- |

## [◆ ](#a26e4776708c27df4c2a17437ea944092)DMA\_MCUX\_PXP\_CMD\_ROTATE\_90

| #define DMA\_MCUX\_PXP\_CMD\_ROTATE\_90   1 |
| --- |

## [◆ ](#a98023d4702873f806316fa8076217f2b)DMA\_MCUX\_PXP\_CMD\_SHIFT

| #define DMA\_MCUX\_PXP\_CMD\_SHIFT   0x5 |
| --- |

## [◆ ](#ae33fe6641b02a3af1910ba0ab30306a2)DMA\_MCUX\_PXP\_FMT

| #define DMA\_MCUX\_PXP\_FMT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x << [DMA\_MCUX\_PXP\_FMT\_SHIFT](#a5ecb10ea31b3b4841d1d1e50ef182b39)) & [DMA\_MCUX\_PXP\_FMT\_MASK](#a99a43acbabab4f6d3d16601776e64ef5))

[DMA\_MCUX\_PXP\_FMT\_SHIFT](#a5ecb10ea31b3b4841d1d1e50ef182b39)

#define DMA\_MCUX\_PXP\_FMT\_SHIFT

**Definition** dma\_mcux\_pxp.h:14

[DMA\_MCUX\_PXP\_FMT\_MASK](#a99a43acbabab4f6d3d16601776e64ef5)

#define DMA\_MCUX\_PXP\_FMT\_MASK

**Definition** dma\_mcux\_pxp.h:13

## [◆ ](#a99a43acbabab4f6d3d16601776e64ef5)DMA\_MCUX\_PXP\_FMT\_MASK

| #define DMA\_MCUX\_PXP\_FMT\_MASK   0x1F |
| --- |

## [◆ ](#a39a2b6f27b7dae092f9cfe491bbd078f)DMA\_MCUX\_PXP\_FMT\_RGB565

| #define DMA\_MCUX\_PXP\_FMT\_RGB565   0 |
| --- |

## [◆ ](#a3667a7b1faf41211b55c22d5f22edd3b)DMA\_MCUX\_PXP\_FMT\_RGB888

| #define DMA\_MCUX\_PXP\_FMT\_RGB888   1 |
| --- |

## [◆ ](#a5ecb10ea31b3b4841d1d1e50ef182b39)DMA\_MCUX\_PXP\_FMT\_SHIFT

| #define DMA\_MCUX\_PXP\_FMT\_SHIFT   0x0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_mcux\_pxp.h](dma__mcux__pxp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
