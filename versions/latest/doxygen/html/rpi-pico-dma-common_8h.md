---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-dma-common_8h.html
original_path: doxygen/html/rpi-pico-dma-common_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-dma-common.h File Reference

[Go to the source code of this file.](rpi-pico-dma-common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RPI\_PICO\_DMA\_SLOT\_TO\_DREQ](#af17a4ab6d1b744cb7ba78185681f464b)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)   [RPI\_PICO\_DMA\_SLOT\_TO\_DREQ](#af17a4ab6d1b744cb7ba78185681f464b) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_TX0](#ab4efb501d7d6acf7c4e320a992a736c9)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x00) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_TX1](#ac83bcbc6b3716d947051d785f60447c1)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x01) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_TX2](#ad2452d29f952c828fc38036d3fc8f7c7)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x02) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_TX3](#a3be36155cb5c9faff83951e46e1ce6eb)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x03) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_RX0](#a4931c164398407d3365d600d17110f95)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x04) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_RX1](#a84583ff2852ec17e709f44cfe85a21d1)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x05) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_RX2](#a7a30cab865790b3ff4c873cec1ae39a4)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x06) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_RX3](#a131cdd1941010a43bebcda6fffd98016)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x07) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_TX0](#a17f1642461493cde7e832a1ab78d9f69)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x08) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_TX1](#a7a19561e334931146de9a56ce3214680)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x09) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_TX2](#ae6f04b3ecc7adfa5bb4e070f6cc29780)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0A) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_TX3](#ab39ac333962fe0debca583061ba1b6cb)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0B) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_RX0](#a7eaaa6b0e6f80021364a66fd75450c0d)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0C) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_RX1](#a9963f9b698a5ffde3e3bcf9b4b43ed22)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0D) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_RX2](#ad1a63c332b00cf4442907a3a11d155d1)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0E) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_RX3](#a07eab28aade43838cf5580e0c0ea3bde)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0F) |
| #define | [RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER0](#aac94fe3f6411cd4bad422974be560d92)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3B) |
| #define | [RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER1](#a864c5126bab363926d43b8d2a951a935)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3C) |
| #define | [RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER2](#a0b8c6347ccfe168d06851fdac5bfe470)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3D) |
| #define | [RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER3](#aa4cf3c65b88cf11aaadd685363695262)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3E) |
| #define | [RPI\_PICO\_DMA\_SLOT\_FORCE](#a6571b7502d26dcb0011fa9c38f64f793)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3F) |

## Macro Definition Documentation

## [◆ ](#a108c9650b4eb398c9994d7c1683beaa8)RPI\_PICO\_DMA\_DREQ\_TO\_SLOT

| #define RPI\_PICO\_DMA\_DREQ\_TO\_SLOT   [RPI\_PICO\_DMA\_SLOT\_TO\_DREQ](#af17a4ab6d1b744cb7ba78185681f464b) |
| --- |

## [◆ ](#aac94fe3f6411cd4bad422974be560d92)RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER0

| #define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3B) |
| --- |

## [◆ ](#a864c5126bab363926d43b8d2a951a935)RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER1

| #define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3C) |
| --- |

## [◆ ](#a0b8c6347ccfe168d06851fdac5bfe470)RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER2

| #define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3D) |
| --- |

## [◆ ](#aa4cf3c65b88cf11aaadd685363695262)RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER3

| #define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3E) |
| --- |

## [◆ ](#a6571b7502d26dcb0011fa9c38f64f793)RPI\_PICO\_DMA\_SLOT\_FORCE

| #define RPI\_PICO\_DMA\_SLOT\_FORCE   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3F) |
| --- |

## [◆ ](#a4931c164398407d3365d600d17110f95)RPI\_PICO\_DMA\_SLOT\_PIO0\_RX0

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x04) |
| --- |

## [◆ ](#a84583ff2852ec17e709f44cfe85a21d1)RPI\_PICO\_DMA\_SLOT\_PIO0\_RX1

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x05) |
| --- |

## [◆ ](#a7a30cab865790b3ff4c873cec1ae39a4)RPI\_PICO\_DMA\_SLOT\_PIO0\_RX2

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x06) |
| --- |

## [◆ ](#a131cdd1941010a43bebcda6fffd98016)RPI\_PICO\_DMA\_SLOT\_PIO0\_RX3

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x07) |
| --- |

## [◆ ](#ab4efb501d7d6acf7c4e320a992a736c9)RPI\_PICO\_DMA\_SLOT\_PIO0\_TX0

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x00) |
| --- |

## [◆ ](#ac83bcbc6b3716d947051d785f60447c1)RPI\_PICO\_DMA\_SLOT\_PIO0\_TX1

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x01) |
| --- |

## [◆ ](#ad2452d29f952c828fc38036d3fc8f7c7)RPI\_PICO\_DMA\_SLOT\_PIO0\_TX2

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x02) |
| --- |

## [◆ ](#a3be36155cb5c9faff83951e46e1ce6eb)RPI\_PICO\_DMA\_SLOT\_PIO0\_TX3

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x03) |
| --- |

## [◆ ](#a7eaaa6b0e6f80021364a66fd75450c0d)RPI\_PICO\_DMA\_SLOT\_PIO1\_RX0

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0C) |
| --- |

## [◆ ](#a9963f9b698a5ffde3e3bcf9b4b43ed22)RPI\_PICO\_DMA\_SLOT\_PIO1\_RX1

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0D) |
| --- |

## [◆ ](#ad1a63c332b00cf4442907a3a11d155d1)RPI\_PICO\_DMA\_SLOT\_PIO1\_RX2

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0E) |
| --- |

## [◆ ](#a07eab28aade43838cf5580e0c0ea3bde)RPI\_PICO\_DMA\_SLOT\_PIO1\_RX3

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0F) |
| --- |

## [◆ ](#a17f1642461493cde7e832a1ab78d9f69)RPI\_PICO\_DMA\_SLOT\_PIO1\_TX0

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x08) |
| --- |

## [◆ ](#a7a19561e334931146de9a56ce3214680)RPI\_PICO\_DMA\_SLOT\_PIO1\_TX1

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x09) |
| --- |

## [◆ ](#ae6f04b3ecc7adfa5bb4e070f6cc29780)RPI\_PICO\_DMA\_SLOT\_PIO1\_TX2

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0A) |
| --- |

## [◆ ](#ab39ac333962fe0debca583061ba1b6cb)RPI\_PICO\_DMA\_SLOT\_PIO1\_TX3

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0B) |
| --- |

## [◆ ](#af17a4ab6d1b744cb7ba78185681f464b)RPI\_PICO\_DMA\_SLOT\_TO\_DREQ

| #define RPI\_PICO\_DMA\_SLOT\_TO\_DREQ | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(~([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))&0x3F)

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [rpi-pico-dma-common.h](rpi-pico-dma-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
