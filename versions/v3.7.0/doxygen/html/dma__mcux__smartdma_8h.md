---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dma__mcux__smartdma_8h.html
original_path: doxygen/html/dma__mcux__smartdma_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_mcux\_smartdma.h File Reference

[Go to the source code of this file.](dma__mcux__smartdma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DMA\_SMARTDMA\_MIPI\_RGB565\_DMA](#a2b2585f7729443c19987c81a6a89a353)   0 |
| #define | [DMA\_SMARTDMA\_MIPI\_RGB888\_DMA](#a62fd85940a8765ed652e490f65ef609e)   1 |
| #define | [DMA\_SMARTDMA\_MIPI\_RGB565\_180](#a86dcedc54234c6091b7cab8aa7ab598b)   2 |
| #define | [DMA\_SMARTDMA\_MIPI\_RGB888\_180](#a1f534964f658e9b944637c3fb49c9783)   3 |
| #define | [DMA\_SMARTDMA\_MIPI\_RGB565\_DMA\_SWAP](#a948bb5d59ec4b5347304006c7335e4bf)   4 |
| #define | [DMA\_SMARTDMA\_MIPI\_RGB888\_DMA\_SWAP](#a5cd0156a4a3870c576917f152793580b)   5 |
| #define | [DMA\_SMARTDMA\_MIPI\_RGB565\_180\_SWAP](#a1881916a14a35d65bc5684e74aed8b4c)   6 |
| #define | [DMA\_SMARTDMA\_MIPI\_RGB888\_180\_SWAP](#a31da9953266f56e8aa2ab271cedcef11)   7 |
| #define | [GD32\_DMA\_FEATURES\_FIFO\_THRESHOLD](#af41c61ae669ce510d514ccb9ff6204f9)(threshold) |

| Functions | |
| --- | --- |
| void | [dma\_smartdma\_install\_fw](#a72c469e163fc727135224893adbf757e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*firmware, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len) |
|  | install SMARTDMA firmware |

## Macro Definition Documentation

## [◆ ](#a86dcedc54234c6091b7cab8aa7ab598b)DMA\_SMARTDMA\_MIPI\_RGB565\_180

| #define DMA\_SMARTDMA\_MIPI\_RGB565\_180   2 |
| --- |

## [◆ ](#a1881916a14a35d65bc5684e74aed8b4c)DMA\_SMARTDMA\_MIPI\_RGB565\_180\_SWAP

| #define DMA\_SMARTDMA\_MIPI\_RGB565\_180\_SWAP   6 |
| --- |

## [◆ ](#a2b2585f7729443c19987c81a6a89a353)DMA\_SMARTDMA\_MIPI\_RGB565\_DMA

| #define DMA\_SMARTDMA\_MIPI\_RGB565\_DMA   0 |
| --- |

## [◆ ](#a948bb5d59ec4b5347304006c7335e4bf)DMA\_SMARTDMA\_MIPI\_RGB565\_DMA\_SWAP

| #define DMA\_SMARTDMA\_MIPI\_RGB565\_DMA\_SWAP   4 |
| --- |

## [◆ ](#a1f534964f658e9b944637c3fb49c9783)DMA\_SMARTDMA\_MIPI\_RGB888\_180

| #define DMA\_SMARTDMA\_MIPI\_RGB888\_180   3 |
| --- |

## [◆ ](#a31da9953266f56e8aa2ab271cedcef11)DMA\_SMARTDMA\_MIPI\_RGB888\_180\_SWAP

| #define DMA\_SMARTDMA\_MIPI\_RGB888\_180\_SWAP   7 |
| --- |

## [◆ ](#a62fd85940a8765ed652e490f65ef609e)DMA\_SMARTDMA\_MIPI\_RGB888\_DMA

| #define DMA\_SMARTDMA\_MIPI\_RGB888\_DMA   1 |
| --- |

## [◆ ](#a5cd0156a4a3870c576917f152793580b)DMA\_SMARTDMA\_MIPI\_RGB888\_DMA\_SWAP

| #define DMA\_SMARTDMA\_MIPI\_RGB888\_DMA\_SWAP   5 |
| --- |

## [◆ ](#af41c61ae669ce510d514ccb9ff6204f9)GD32\_DMA\_FEATURES\_FIFO\_THRESHOLD

| #define GD32\_DMA\_FEATURES\_FIFO\_THRESHOLD | ( |  | *threshold* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(threshold & 0x3)

## Function Documentation

## [◆ ](#a72c469e163fc727135224893adbf757e)dma\_smartdma\_install\_fw()

| void dma\_smartdma\_install\_fw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *firmware*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len* ) |

install SMARTDMA firmware

Install a custom firmware for the smartDMA. This function allows the user to install a custom firmware into the smartDMA, which implements different API functions than the standard MCUX SDK firmware.

Parameters
:   | dev | smartDMA device |
    | --- | --- |
    | firmware | address of buffer containing smartDMA firmware |
    | len | length of firmware buffer |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_mcux\_smartdma.h](dma__mcux__smartdma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
