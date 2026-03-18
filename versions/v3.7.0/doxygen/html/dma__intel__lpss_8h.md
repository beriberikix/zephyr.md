---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dma__intel__lpss_8h.html
original_path: doxygen/html/dma__intel__lpss_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_intel\_lpss.h File Reference

[Go to the source code of this file.](dma__intel__lpss_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DMA\_INTEL\_LPSS\_OFFSET](#a30a9efb6d3b728e258083d8c9abb617f)   0x800 |
| #define | [DMA\_INTEL\_LPSS\_REMAP\_LOW](#abc9f1a6bfba312cf78ab7800d3b8c589)   0x240 |
| #define | [DMA\_INTEL\_LPSS\_REMAP\_HI](#a2fa4dfb43c0fc5223d0e17932d6c97ee)   0x244 |
| #define | [DMA\_INTEL\_LPSS\_TX\_CHAN](#a1dd74ce0e651a2fad8abf337ac0bf1aa)   0 |
| #define | [DMA\_INTEL\_LPSS\_RX\_CHAN](#a3797b7de5ebf86a3c722e7667239cb3f)   1 |
| #define | [DMA\_INTEL\_LPSS\_ADDR\_RIGHT\_SHIFT](#a93cbdc5d852735e260d4b767cc591977)   32 |

| Functions | |
| --- | --- |
| void | [dma\_intel\_lpss\_isr](#a769db0413f8ca5fe4c03d1701581edfa) (const struct [device](structdevice.md) \*dev) |
| int | [dma\_intel\_lpss\_setup](#a4a5438ab5a164e80c0564fc73e8b9764) (const struct [device](structdevice.md) \*dev) |
| void | [dma\_intel\_lpss\_set\_base](#aaf5eefbe0476083a87e5c2724a99a73d) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) base) |

## Macro Definition Documentation

## [◆ ](#a93cbdc5d852735e260d4b767cc591977)DMA\_INTEL\_LPSS\_ADDR\_RIGHT\_SHIFT

| #define DMA\_INTEL\_LPSS\_ADDR\_RIGHT\_SHIFT   32 |
| --- |

## [◆ ](#a30a9efb6d3b728e258083d8c9abb617f)DMA\_INTEL\_LPSS\_OFFSET

| #define DMA\_INTEL\_LPSS\_OFFSET   0x800 |
| --- |

## [◆ ](#a2fa4dfb43c0fc5223d0e17932d6c97ee)DMA\_INTEL\_LPSS\_REMAP\_HI

| #define DMA\_INTEL\_LPSS\_REMAP\_HI   0x244 |
| --- |

## [◆ ](#abc9f1a6bfba312cf78ab7800d3b8c589)DMA\_INTEL\_LPSS\_REMAP\_LOW

| #define DMA\_INTEL\_LPSS\_REMAP\_LOW   0x240 |
| --- |

## [◆ ](#a3797b7de5ebf86a3c722e7667239cb3f)DMA\_INTEL\_LPSS\_RX\_CHAN

| #define DMA\_INTEL\_LPSS\_RX\_CHAN   1 |
| --- |

## [◆ ](#a1dd74ce0e651a2fad8abf337ac0bf1aa)DMA\_INTEL\_LPSS\_TX\_CHAN

| #define DMA\_INTEL\_LPSS\_TX\_CHAN   0 |
| --- |

## Function Documentation

## [◆ ](#a769db0413f8ca5fe4c03d1701581edfa)dma\_intel\_lpss\_isr()

| void dma\_intel\_lpss\_isr | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aaf5eefbe0476083a87e5c2724a99a73d)dma\_intel\_lpss\_set\_base()

| void dma\_intel\_lpss\_set\_base | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *base* ) |

## [◆ ](#a4a5438ab5a164e80c0564fc73e8b9764)dma\_intel\_lpss\_setup()

| int dma\_intel\_lpss\_setup | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_intel\_lpss.h](dma__intel__lpss_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
