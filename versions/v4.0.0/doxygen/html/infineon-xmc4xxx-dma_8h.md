---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/infineon-xmc4xxx-dma_8h.html
original_path: doxygen/html/infineon-xmc4xxx-dma_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

infineon-xmc4xxx-dma.h File Reference

[Go to the source code of this file.](infineon-xmc4xxx-dma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS](#a3c4acabda14da40580e0a2b27ee65460)   0 |
| #define | [XMC4XXX\_DMA\_REQUEST\_SOURCE\_MASK](#a4df66f182189c3ae0983cdbbf9ae441c)   0xf |
| #define | [XMC4XXX\_DMA\_LINE\_POS](#a770a813125a4338de8e409d4c9056c16)   4 |
| #define | [XMC4XXX\_DMA\_LINE\_MASK](#a6675bcb092ce91d47fa5b47142ca45f4)   0xf |
| #define | [XMC4XXX\_DMA\_GET\_REQUEST\_SOURCE](#a7545b103c79e582bec92c59571c2aee5)(mx) |
| #define | [XMC4XXX\_DMA\_GET\_LINE](#a27d5d96c050301bfc22b52fe7f5483db)(mx) |
| #define | [XMC4XXX\_SET\_CONFIG](#afa54bae091f586404ae79cfa97db6d36)(line, rs) |

## Macro Definition Documentation

## [◆ ](#a27d5d96c050301bfc22b52fe7f5483db)XMC4XXX\_DMA\_GET\_LINE

| #define XMC4XXX\_DMA\_GET\_LINE | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_DMA\_LINE\_POS](#a770a813125a4338de8e409d4c9056c16)) & [XMC4XXX\_DMA\_LINE\_MASK](#a6675bcb092ce91d47fa5b47142ca45f4))

[XMC4XXX\_DMA\_LINE\_MASK](#a6675bcb092ce91d47fa5b47142ca45f4)

#define XMC4XXX\_DMA\_LINE\_MASK

**Definition** infineon-xmc4xxx-dma.h:14

[XMC4XXX\_DMA\_LINE\_POS](#a770a813125a4338de8e409d4c9056c16)

#define XMC4XXX\_DMA\_LINE\_POS

**Definition** infineon-xmc4xxx-dma.h:13

## [◆ ](#a7545b103c79e582bec92c59571c2aee5)XMC4XXX\_DMA\_GET\_REQUEST\_SOURCE

| #define XMC4XXX\_DMA\_GET\_REQUEST\_SOURCE | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS](#a3c4acabda14da40580e0a2b27ee65460)) & [XMC4XXX\_DMA\_REQUEST\_SOURCE\_MASK](#a4df66f182189c3ae0983cdbbf9ae441c))

[XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS](#a3c4acabda14da40580e0a2b27ee65460)

#define XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS

**Definition** infineon-xmc4xxx-dma.h:10

[XMC4XXX\_DMA\_REQUEST\_SOURCE\_MASK](#a4df66f182189c3ae0983cdbbf9ae441c)

#define XMC4XXX\_DMA\_REQUEST\_SOURCE\_MASK

**Definition** infineon-xmc4xxx-dma.h:11

## [◆ ](#a6675bcb092ce91d47fa5b47142ca45f4)XMC4XXX\_DMA\_LINE\_MASK

| #define XMC4XXX\_DMA\_LINE\_MASK   0xf |
| --- |

## [◆ ](#a770a813125a4338de8e409d4c9056c16)XMC4XXX\_DMA\_LINE\_POS

| #define XMC4XXX\_DMA\_LINE\_POS   4 |
| --- |

## [◆ ](#a4df66f182189c3ae0983cdbbf9ae441c)XMC4XXX\_DMA\_REQUEST\_SOURCE\_MASK

| #define XMC4XXX\_DMA\_REQUEST\_SOURCE\_MASK   0xf |
| --- |

## [◆ ](#a3c4acabda14da40580e0a2b27ee65460)XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS

| #define XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS   0 |
| --- |

## [◆ ](#afa54bae091f586404ae79cfa97db6d36)XMC4XXX\_SET\_CONFIG

| #define XMC4XXX\_SET\_CONFIG | ( |  | *line*, |
| --- | --- | --- | --- |
|  |  |  | *rs* ) |

**Value:**

((line) << [XMC4XXX\_DMA\_LINE\_POS](#a770a813125a4338de8e409d4c9056c16) | (rs) << [XMC4XXX\_DMA\_REQUEST\_SOURCE\_POS](#a3c4acabda14da40580e0a2b27ee65460))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [infineon-xmc4xxx-dma.h](infineon-xmc4xxx-dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
