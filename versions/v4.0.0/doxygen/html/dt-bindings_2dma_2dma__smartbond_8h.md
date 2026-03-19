---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html
original_path: doxygen/html/dt-bindings_2dma_2dma__smartbond_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_smartbond.h File Reference

[Go to the source code of this file.](dt-bindings_2dma_2dma__smartbond_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_SPI](#af46b07be1f5058057addc6b574caf5d8)   0x0 |
|  | Vendror-specific DMA peripheral triggering sources. |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_SPI2](#a1965f7b0abbebba2b44416f9c93ce793)   0x1 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_UART](#a732d794d46d67f039d3b88e172f447e7)   0x2 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_UART2](#ad5762fefff49d30ec23932af767ced7f)   0x3 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_I2C](#a59c1d5957912ee64584e4894b4c40c11)   0x4 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_I2C2](#a0cf51e3db0f0472b36341156544bb218)   0x5 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_USB](#ae4b382b67096e708e0b57ee6ec52a9f0)   0x6 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_UART3](#abcd3ac0c66ee89f6cdec303f8e1bfe39)   0x7 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_PCM](#ab2553e825d7559636ba33894a4744bf6)   0x8 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_SRC](#a6ea3dfcb21bff83188ddb328a6e8bdb0)   0x9 |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_GPADC](#a4aa0cf2a75acd5ca0359cdbddc94c2f0)   0xC |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_SDADC](#a792383e4160b8256a28b4c98508e082a)   0xD |
| #define | [DMA\_SMARTBOND\_TRIG\_MUX\_NONE](#abb1a1462a91080511fc9d94bba685a2b)   0xF |

## Macro Definition Documentation

## [◆ ](#a4aa0cf2a75acd5ca0359cdbddc94c2f0)DMA\_SMARTBOND\_TRIG\_MUX\_GPADC

| #define DMA\_SMARTBOND\_TRIG\_MUX\_GPADC   0xC |
| --- |

## [◆ ](#a59c1d5957912ee64584e4894b4c40c11)DMA\_SMARTBOND\_TRIG\_MUX\_I2C

| #define DMA\_SMARTBOND\_TRIG\_MUX\_I2C   0x4 |
| --- |

## [◆ ](#a0cf51e3db0f0472b36341156544bb218)DMA\_SMARTBOND\_TRIG\_MUX\_I2C2

| #define DMA\_SMARTBOND\_TRIG\_MUX\_I2C2   0x5 |
| --- |

## [◆ ](#abb1a1462a91080511fc9d94bba685a2b)DMA\_SMARTBOND\_TRIG\_MUX\_NONE

| #define DMA\_SMARTBOND\_TRIG\_MUX\_NONE   0xF |
| --- |

## [◆ ](#ab2553e825d7559636ba33894a4744bf6)DMA\_SMARTBOND\_TRIG\_MUX\_PCM

| #define DMA\_SMARTBOND\_TRIG\_MUX\_PCM   0x8 |
| --- |

## [◆ ](#a792383e4160b8256a28b4c98508e082a)DMA\_SMARTBOND\_TRIG\_MUX\_SDADC

| #define DMA\_SMARTBOND\_TRIG\_MUX\_SDADC   0xD |
| --- |

## [◆ ](#af46b07be1f5058057addc6b574caf5d8)DMA\_SMARTBOND\_TRIG\_MUX\_SPI

| #define DMA\_SMARTBOND\_TRIG\_MUX\_SPI   0x0 |
| --- |

Vendror-specific DMA peripheral triggering sources.

A valid triggering source should be provided when DMA is configured for peripheral to peripheral or memory to peripheral transactions.

## [◆ ](#a1965f7b0abbebba2b44416f9c93ce793)DMA\_SMARTBOND\_TRIG\_MUX\_SPI2

| #define DMA\_SMARTBOND\_TRIG\_MUX\_SPI2   0x1 |
| --- |

## [◆ ](#a6ea3dfcb21bff83188ddb328a6e8bdb0)DMA\_SMARTBOND\_TRIG\_MUX\_SRC

| #define DMA\_SMARTBOND\_TRIG\_MUX\_SRC   0x9 |
| --- |

## [◆ ](#a732d794d46d67f039d3b88e172f447e7)DMA\_SMARTBOND\_TRIG\_MUX\_UART

| #define DMA\_SMARTBOND\_TRIG\_MUX\_UART   0x2 |
| --- |

## [◆ ](#ad5762fefff49d30ec23932af767ced7f)DMA\_SMARTBOND\_TRIG\_MUX\_UART2

| #define DMA\_SMARTBOND\_TRIG\_MUX\_UART2   0x3 |
| --- |

## [◆ ](#abcd3ac0c66ee89f6cdec303f8e1bfe39)DMA\_SMARTBOND\_TRIG\_MUX\_UART3

| #define DMA\_SMARTBOND\_TRIG\_MUX\_UART3   0x7 |
| --- |

## [◆ ](#ae4b382b67096e708e0b57ee6ec52a9f0)DMA\_SMARTBOND\_TRIG\_MUX\_USB

| #define DMA\_SMARTBOND\_TRIG\_MUX\_USB   0x6 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [dma\_smartbond.h](dt-bindings_2dma_2dma__smartbond_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
