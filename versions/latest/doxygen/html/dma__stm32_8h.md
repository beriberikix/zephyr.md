---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dma__stm32_8h.html
original_path: doxygen/html/dma__stm32_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_stm32.h File Reference

[Go to the source code of this file.](dma__stm32_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_DMA\_HAL\_OVERRIDE](#a00fdf498cabe4214e28add6ef55681bc)   0x7F |
| #define | [STM32\_DMA\_STREAM\_OFFSET](#aca656daf77c45e1d6b18e911bcb6b76b)   1 |
| #define | [STM32\_DMA\_SLOT](#ad2f2b0a1e77f5f829bb2833a31486ff8)(id, dir, slot) |
| #define | [STM32\_DMA\_SLOT\_BY\_IDX](#a1802cfe36a268822a2e008b0a748b8c5)(id, idx, slot) |
| #define | [STM32\_DMA\_FEATURES](#aa1aa5181a6387f56cc914c755d4dcb69)(id, dir) |
| #define | [STM32\_DMA\_CTLR](#a65697918b25bd6e316a2141289a3bba4)(id, dir) |
| #define | [STM32\_DMA\_CHANNEL\_CONFIG](#ac9830f1d3c46089010a8354fc344b68e)(id, dir) |
| #define | [STM32\_DMA\_CHANNEL\_CONFIG\_BY\_IDX](#a8739b1eb41560e1fc46afc464f5ac0c3)(id, idx) |
| #define | [STM32\_DMA\_CONFIG\_DIRECTION](#aed17fb68ee78831fbce6628cc97ef4d0)(config) |
| #define | [STM32\_DMA\_CONFIG\_PERIPHERAL\_ADDR\_INC](#a1b97fe65f90e0b73f1450e5a763cc5cb)(config) |
| #define | [STM32\_DMA\_CONFIG\_MEMORY\_ADDR\_INC](#ad4bb23a652c15f856431d13048ac639f)(config) |
| #define | [STM32\_DMA\_CONFIG\_PERIPHERAL\_DATA\_SIZE](#a208ec04cc0c0e8e41012c6c07bd10e3e)(config) |
| #define | [STM32\_DMA\_CONFIG\_MEMORY\_DATA\_SIZE](#ae2664884f88d4df0be45c189ecdabf1d)(config) |
| #define | [STM32\_DMA\_CONFIG\_PERIPHERAL\_INC\_FIXED](#ac1e469f441e34af9a62fc4ab697a0275)(config) |
| #define | [STM32\_DMA\_CONFIG\_PRIORITY](#af20462bb4d9f9a38dec07add57de4795)(config) |
| #define | [STM32\_DMA\_FEATURES\_FIFO\_THRESHOLD](#abf490559310376a854ae1e8ee18209ce)(features) |

## Macro Definition Documentation

## [◆ ](#ac9830f1d3c46089010a8354fc344b68e)STM32\_DMA\_CHANNEL\_CONFIG

| #define STM32\_DMA\_CHANNEL\_CONFIG | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *dir* ) |

**Value:**

[DT\_INST\_DMAS\_CELL\_BY\_NAME](group__devicetree-dmas.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)(id, dir, channel\_config)

[DT\_INST\_DMAS\_CELL\_BY\_NAME](group__devicetree-dmas.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)

#define DT\_INST\_DMAS\_CELL\_BY\_NAME(inst, name, cell)

Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value by name.

**Definition** dma.h:232

## [◆ ](#a8739b1eb41560e1fc46afc464f5ac0c3)STM32\_DMA\_CHANNEL\_CONFIG\_BY\_IDX

| #define STM32\_DMA\_CHANNEL\_CONFIG\_BY\_IDX | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

**Value:**

[DT\_INST\_DMAS\_CELL\_BY\_IDX](group__devicetree-dmas.md#gad4e1a8f22b8943328df2a3f8f2a149b7)(id, idx, channel\_config)

[DT\_INST\_DMAS\_CELL\_BY\_IDX](group__devicetree-dmas.md#gad4e1a8f22b8943328df2a3f8f2a149b7)

#define DT\_INST\_DMAS\_CELL\_BY\_IDX(inst, idx, cell)

Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value at an index.

**Definition** dma.h:176

## [◆ ](#aed17fb68ee78831fbce6628cc97ef4d0)STM32\_DMA\_CONFIG\_DIRECTION

| #define STM32\_DMA\_CONFIG\_DIRECTION | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 6) & 0x3)

## [◆ ](#ad4bb23a652c15f856431d13048ac639f)STM32\_DMA\_CONFIG\_MEMORY\_ADDR\_INC

| #define STM32\_DMA\_CONFIG\_MEMORY\_ADDR\_INC | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 10) & 0x1)

## [◆ ](#ae2664884f88d4df0be45c189ecdabf1d)STM32\_DMA\_CONFIG\_MEMORY\_DATA\_SIZE

| #define STM32\_DMA\_CONFIG\_MEMORY\_DATA\_SIZE | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(1 << ((config >> 13) & 0x3))

## [◆ ](#a1b97fe65f90e0b73f1450e5a763cc5cb)STM32\_DMA\_CONFIG\_PERIPHERAL\_ADDR\_INC

| #define STM32\_DMA\_CONFIG\_PERIPHERAL\_ADDR\_INC | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 9) & 0x1)

## [◆ ](#a208ec04cc0c0e8e41012c6c07bd10e3e)STM32\_DMA\_CONFIG\_PERIPHERAL\_DATA\_SIZE

| #define STM32\_DMA\_CONFIG\_PERIPHERAL\_DATA\_SIZE | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(1 << ((config >> 11) & 0x3))

## [◆ ](#ac1e469f441e34af9a62fc4ab697a0275)STM32\_DMA\_CONFIG\_PERIPHERAL\_INC\_FIXED

| #define STM32\_DMA\_CONFIG\_PERIPHERAL\_INC\_FIXED | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 15) & 0x1)

## [◆ ](#af20462bb4d9f9a38dec07add57de4795)STM32\_DMA\_CONFIG\_PRIORITY

| #define STM32\_DMA\_CONFIG\_PRIORITY | ( |  | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((config >> 16) & 0x3)

## [◆ ](#a65697918b25bd6e316a2141289a3bba4)STM32\_DMA\_CTLR

| #define STM32\_DMA\_CTLR | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *dir* ) |

**Value:**

[DT\_INST\_DMAS\_CTLR\_BY\_NAME](group__devicetree-dmas.md#gad098f0b51ee1f629c1259ca346f49303)(id, dir)

[DT\_INST\_DMAS\_CTLR\_BY\_NAME](group__devicetree-dmas.md#gad098f0b51ee1f629c1259ca346f49303)

#define DT\_INST\_DMAS\_CTLR\_BY\_NAME(inst, name)

Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property by name.

**Definition** dma.h:114

## [◆ ](#aa1aa5181a6387f56cc914c755d4dcb69)STM32\_DMA\_FEATURES

| #define STM32\_DMA\_FEATURES | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *dir* ) |

**Value:**

[DT\_INST\_DMAS\_CELL\_BY\_NAME](group__devicetree-dmas.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)(id, dir, features)

## [◆ ](#abf490559310376a854ae1e8ee18209ce)STM32\_DMA\_FEATURES\_FIFO\_THRESHOLD

| #define STM32\_DMA\_FEATURES\_FIFO\_THRESHOLD | ( |  | *features* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

0

## [◆ ](#a00fdf498cabe4214e28add6ef55681bc)STM32\_DMA\_HAL\_OVERRIDE

| #define STM32\_DMA\_HAL\_OVERRIDE   0x7F |
| --- |

## [◆ ](#ad2f2b0a1e77f5f829bb2833a31486ff8)STM32\_DMA\_SLOT

| #define STM32\_DMA\_SLOT | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *dir*, |
|  |  |  | *slot* ) |

**Value:**

[DT\_INST\_DMAS\_CELL\_BY\_NAME](group__devicetree-dmas.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)(id, dir, slot)

## [◆ ](#a1802cfe36a268822a2e008b0a748b8c5)STM32\_DMA\_SLOT\_BY\_IDX

| #define STM32\_DMA\_SLOT\_BY\_IDX | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *slot* ) |

**Value:**

[DT\_INST\_DMAS\_CELL\_BY\_IDX](group__devicetree-dmas.md#gad4e1a8f22b8943328df2a3f8f2a149b7)(id, idx, slot)

## [◆ ](#aca656daf77c45e1d6b18e911bcb6b76b)STM32\_DMA\_STREAM\_OFFSET

| #define STM32\_DMA\_STREAM\_OFFSET   1 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_stm32.h](dma__stm32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
