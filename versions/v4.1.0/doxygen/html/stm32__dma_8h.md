---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stm32__dma_8h.html
original_path: doxygen/html/stm32__dma_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_dma.h File Reference

[Go to the source code of this file.](stm32__dma_8h_source.md)

| Macros | |
| --- | --- |
| custom DMA flags for channel configuration | |
| #define | [STM32\_DMA\_CH\_CFG\_MODE](#a86e8ab71081233e1f9aa8300b6ea3c85)(val) |
|  | DMA cyclic mode config on bit 5. |
| #define | [STM32\_DMA\_MODE\_NORMAL](#a6d811813db4e97b831b4b1fb95ec594c)   [STM32\_DMA\_CH\_CFG\_MODE](#a86e8ab71081233e1f9aa8300b6ea3c85)(0) |
| #define | [STM32\_DMA\_MODE\_CYCLIC](#a944c3985d60fa92a53b9db6c57a54e6a)   [STM32\_DMA\_CH\_CFG\_MODE](#a86e8ab71081233e1f9aa8300b6ea3c85)(1) |
| #define | [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(val) |
|  | DMA transfer direction config on bits 6-7. |
| #define | [STM32\_DMA\_MEMORY\_TO\_MEMORY](#a3678dc5bb6f7b7a7c7fbb87c43ad3724)   [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(0) |
| #define | [STM32\_DMA\_MEMORY\_TO\_PERIPH](#ae0c8bc868d309a4fc1a57b28b6d88811)   [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(1) |
| #define | [STM32\_DMA\_PERIPH\_TO\_MEMORY](#a399cbac4220647c4604c94fdb7512f8a)   [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(2) |
| #define | [STM32\_DMA\_PERIPH\_TO\_PERIPH](#a35bc7af86b12a421cc0391a43307d808)   [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(3) |
| #define | [STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#a69d16d7d3474f075c8a639370297eeaa)(val) |
|  | DMA Peripheral increment Address config on bit 9. |
| #define | [STM32\_DMA\_PERIPH\_NO\_INC](#aa7cc172e318bf2558a44c87f1b1d3693)   [STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#a69d16d7d3474f075c8a639370297eeaa)(0) |
| #define | [STM32\_DMA\_PERIPH\_INC](#ae0f9a8b757005339a550959930084ecb)   [STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#a69d16d7d3474f075c8a639370297eeaa)(1) |
| #define | [STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC](#abf66072cff1f8d835beb78a8d974fa2a)(val) |
|  | DMA Memory increment Address config on bit 10. |
| #define | [STM32\_DMA\_MEM\_NO\_INC](#ae46002f328f981e5dbe7bc502c46b759)   [STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC](#abf66072cff1f8d835beb78a8d974fa2a)(0) |
| #define | [STM32\_DMA\_MEM\_INC](#a46f20993a4561c34cce25cf70f56879f)   [STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC](#abf66072cff1f8d835beb78a8d974fa2a)(1) |
| #define | [STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)(val) |
|  | DMA Peripheral data size config on bits 11, 12. |
| #define | [STM32\_DMA\_PERIPH\_8BITS](#a8ab5a7090927e92bef333fb33416c32b)   [STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)(0) |
| #define | [STM32\_DMA\_PERIPH\_16BITS](#aad24cf95434530d2d64025512d467d5e)   [STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)(1) |
| #define | [STM32\_DMA\_PERIPH\_32BITS](#af869e4e36689a3b9402425f0a7dcc970)   [STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)(2) |
| #define | [STM32\_DMA\_CH\_CFG\_MEM\_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)(val) |
|  | DMA Memory data size config on bits 13, 14. |
| #define | [STM32\_DMA\_MEM\_8BITS](#a372c638a2cffdcb69f7748e12e1564d9)   [STM32\_DMA\_CH\_CFG\_MEM\_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)(0) |
| #define | [STM32\_DMA\_MEM\_16BITS](#ac9f13ef8eb95fc507d707064a5dae605)   [STM32\_DMA\_CH\_CFG\_MEM\_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)(1) |
| #define | [STM32\_DMA\_MEM\_32BITS](#ab5cc477888dac48daacf0365530dba95)   [STM32\_DMA\_CH\_CFG\_MEM\_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)(2) |
| #define | [STM32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED](#a7f7fa52e8b080c1ea756cd8df666c9cf)(val) |
|  | DMA Peripheral increment offset config on bit 15. |
| #define | [STM32\_DMA\_OFFSET\_LINKED\_BUS](#a23683d3d614c2b82cb5d93b9fe9f572d)   [STM32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED](#a7f7fa52e8b080c1ea756cd8df666c9cf)(0) |
| #define | [STM32\_DMA\_OFFSET\_FIXED\_4](#a5ba0d5a9e52cb2f443504624606e4a10)   [STM32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED](#a7f7fa52e8b080c1ea756cd8df666c9cf)(1) |
| #define | [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(val) |
|  | DMA Priority config on bits 16, 17. |
| #define | [STM32\_DMA\_PRIORITY\_LOW](#a1e3161e8a567113a9b3a6874ad9c7ec9)   [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(0) |
| #define | [STM32\_DMA\_PRIORITY\_MEDIUM](#a7ab285799783a4a45248f97c24cc2572)   [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(1) |
| #define | [STM32\_DMA\_PRIORITY\_HIGH](#a2aeaf7b8cccb8512d0f18c07e66465de)   [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(2) |
| #define | [STM32\_DMA\_PRIORITY\_VERY\_HIGH](#a5ce1311f75b678c623f1276de3463aa5)   [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(3) |
| #define | [STM32\_DMA\_FIFO\_1\_4](#a30103ad3e6fe698187674f09af5bf057)   0U |
|  | DMA FIFO threshold feature. |
| #define | [STM32\_DMA\_FIFO\_HALF](#a6595f13f24d26e28aa82b1571c03075c)   1U |
| #define | [STM32\_DMA\_FIFO\_3\_4](#a8720db61ce6623cf6a96ac862fa89041)   2U |
| #define | [STM32\_DMA\_FIFO\_FULL](#a4a561bb696eeaf8f8878fc327eab5f37)   3U |
| #define | [STM32\_DMA\_PERIPH\_TX](#ab26996ccb981ef26dc0783302f4564f7)   ([STM32\_DMA\_MEMORY\_TO\_PERIPH](#ae0c8bc868d309a4fc1a57b28b6d88811) | [STM32\_DMA\_MEM\_INC](#a46f20993a4561c34cce25cf70f56879f)) |
| #define | [STM32\_DMA\_PERIPH\_RX](#ac680c9808061136e327cf6a14b09ea57)   ([STM32\_DMA\_PERIPH\_TO\_MEMORY](#a399cbac4220647c4604c94fdb7512f8a) | [STM32\_DMA\_MEM\_INC](#a46f20993a4561c34cce25cf70f56879f)) |
| #define | [STM32\_DMA\_16BITS](#a7fd16b4e2d5fd63fc4d012def6f8c186)   ([STM32\_DMA\_PERIPH\_16BITS](#aad24cf95434530d2d64025512d467d5e) | [STM32\_DMA\_MEM\_16BITS](#ac9f13ef8eb95fc507d707064a5dae605)) |

## Macro Definition Documentation

## [◆ ](#a7fd16b4e2d5fd63fc4d012def6f8c186)STM32\_DMA\_16BITS

| #define STM32\_DMA\_16BITS   ([STM32\_DMA\_PERIPH\_16BITS](#aad24cf95434530d2d64025512d467d5e) | [STM32\_DMA\_MEM\_16BITS](#ac9f13ef8eb95fc507d707064a5dae605)) |
| --- |

## [◆ ](#a1184bb6207bf6347ede5b3cfd1b67da9)STM32\_DMA\_CH\_CFG\_DIRECTION

| #define STM32\_DMA\_CH\_CFG\_DIRECTION | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x3) << 6)

DMA transfer direction config on bits 6-7.

## [◆ ](#abf66072cff1f8d835beb78a8d974fa2a)STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC

| #define STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 10)

DMA Memory increment Address config on bit 10.

## [◆ ](#ac0bb2e159dc52537c60851c1b9bac4c3)STM32\_DMA\_CH\_CFG\_MEM\_WIDTH

| #define STM32\_DMA\_CH\_CFG\_MEM\_WIDTH | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x3) << 13)

DMA Memory data size config on bits 13, 14.

## [◆ ](#a86e8ab71081233e1f9aa8300b6ea3c85)STM32\_DMA\_CH\_CFG\_MODE

| #define STM32\_DMA\_CH\_CFG\_MODE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 5)

DMA cyclic mode config on bit 5.

## [◆ ](#a69d16d7d3474f075c8a639370297eeaa)STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC

| #define STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 9)

DMA Peripheral increment Address config on bit 9.

## [◆ ](#a7f7fa52e8b080c1ea756cd8df666c9cf)STM32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED

| #define STM32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 15)

DMA Peripheral increment offset config on bit 15.

## [◆ ](#a0c0c0c5cde99d895079197bf75c25245)STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH

| #define STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x3) << 11)

DMA Peripheral data size config on bits 11, 12.

## [◆ ](#add3e03ced6f685382d43058f0cbceb9b)STM32\_DMA\_CH\_CFG\_PRIORITY

| #define STM32\_DMA\_CH\_CFG\_PRIORITY | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x3) << 16)

DMA Priority config on bits 16, 17.

## [◆ ](#a30103ad3e6fe698187674f09af5bf057)STM32\_DMA\_FIFO\_1\_4

| #define STM32\_DMA\_FIFO\_1\_4   0U |
| --- |

DMA FIFO threshold feature.

## [◆ ](#a8720db61ce6623cf6a96ac862fa89041)STM32\_DMA\_FIFO\_3\_4

| #define STM32\_DMA\_FIFO\_3\_4   2U |
| --- |

## [◆ ](#a4a561bb696eeaf8f8878fc327eab5f37)STM32\_DMA\_FIFO\_FULL

| #define STM32\_DMA\_FIFO\_FULL   3U |
| --- |

## [◆ ](#a6595f13f24d26e28aa82b1571c03075c)STM32\_DMA\_FIFO\_HALF

| #define STM32\_DMA\_FIFO\_HALF   1U |
| --- |

## [◆ ](#ac9f13ef8eb95fc507d707064a5dae605)STM32\_DMA\_MEM\_16BITS

| #define STM32\_DMA\_MEM\_16BITS   [STM32\_DMA\_CH\_CFG\_MEM\_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)(1) |
| --- |

## [◆ ](#ab5cc477888dac48daacf0365530dba95)STM32\_DMA\_MEM\_32BITS

| #define STM32\_DMA\_MEM\_32BITS   [STM32\_DMA\_CH\_CFG\_MEM\_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)(2) |
| --- |

## [◆ ](#a372c638a2cffdcb69f7748e12e1564d9)STM32\_DMA\_MEM\_8BITS

| #define STM32\_DMA\_MEM\_8BITS   [STM32\_DMA\_CH\_CFG\_MEM\_WIDTH](#ac0bb2e159dc52537c60851c1b9bac4c3)(0) |
| --- |

## [◆ ](#a46f20993a4561c34cce25cf70f56879f)STM32\_DMA\_MEM\_INC

| #define STM32\_DMA\_MEM\_INC   [STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC](#abf66072cff1f8d835beb78a8d974fa2a)(1) |
| --- |

## [◆ ](#ae46002f328f981e5dbe7bc502c46b759)STM32\_DMA\_MEM\_NO\_INC

| #define STM32\_DMA\_MEM\_NO\_INC   [STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC](#abf66072cff1f8d835beb78a8d974fa2a)(0) |
| --- |

## [◆ ](#a3678dc5bb6f7b7a7c7fbb87c43ad3724)STM32\_DMA\_MEMORY\_TO\_MEMORY

| #define STM32\_DMA\_MEMORY\_TO\_MEMORY   [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(0) |
| --- |

## [◆ ](#ae0c8bc868d309a4fc1a57b28b6d88811)STM32\_DMA\_MEMORY\_TO\_PERIPH

| #define STM32\_DMA\_MEMORY\_TO\_PERIPH   [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(1) |
| --- |

## [◆ ](#a944c3985d60fa92a53b9db6c57a54e6a)STM32\_DMA\_MODE\_CYCLIC

| #define STM32\_DMA\_MODE\_CYCLIC   [STM32\_DMA\_CH\_CFG\_MODE](#a86e8ab71081233e1f9aa8300b6ea3c85)(1) |
| --- |

## [◆ ](#a6d811813db4e97b831b4b1fb95ec594c)STM32\_DMA\_MODE\_NORMAL

| #define STM32\_DMA\_MODE\_NORMAL   [STM32\_DMA\_CH\_CFG\_MODE](#a86e8ab71081233e1f9aa8300b6ea3c85)(0) |
| --- |

## [◆ ](#a5ba0d5a9e52cb2f443504624606e4a10)STM32\_DMA\_OFFSET\_FIXED\_4

| #define STM32\_DMA\_OFFSET\_FIXED\_4   [STM32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED](#a7f7fa52e8b080c1ea756cd8df666c9cf)(1) |
| --- |

## [◆ ](#a23683d3d614c2b82cb5d93b9fe9f572d)STM32\_DMA\_OFFSET\_LINKED\_BUS

| #define STM32\_DMA\_OFFSET\_LINKED\_BUS   [STM32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED](#a7f7fa52e8b080c1ea756cd8df666c9cf)(0) |
| --- |

## [◆ ](#aad24cf95434530d2d64025512d467d5e)STM32\_DMA\_PERIPH\_16BITS

| #define STM32\_DMA\_PERIPH\_16BITS   [STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)(1) |
| --- |

## [◆ ](#af869e4e36689a3b9402425f0a7dcc970)STM32\_DMA\_PERIPH\_32BITS

| #define STM32\_DMA\_PERIPH\_32BITS   [STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)(2) |
| --- |

## [◆ ](#a8ab5a7090927e92bef333fb33416c32b)STM32\_DMA\_PERIPH\_8BITS

| #define STM32\_DMA\_PERIPH\_8BITS   [STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH](#a0c0c0c5cde99d895079197bf75c25245)(0) |
| --- |

## [◆ ](#ae0f9a8b757005339a550959930084ecb)STM32\_DMA\_PERIPH\_INC

| #define STM32\_DMA\_PERIPH\_INC   [STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#a69d16d7d3474f075c8a639370297eeaa)(1) |
| --- |

## [◆ ](#aa7cc172e318bf2558a44c87f1b1d3693)STM32\_DMA\_PERIPH\_NO\_INC

| #define STM32\_DMA\_PERIPH\_NO\_INC   [STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC](#a69d16d7d3474f075c8a639370297eeaa)(0) |
| --- |

## [◆ ](#ac680c9808061136e327cf6a14b09ea57)STM32\_DMA\_PERIPH\_RX

| #define STM32\_DMA\_PERIPH\_RX   ([STM32\_DMA\_PERIPH\_TO\_MEMORY](#a399cbac4220647c4604c94fdb7512f8a) | [STM32\_DMA\_MEM\_INC](#a46f20993a4561c34cce25cf70f56879f)) |
| --- |

## [◆ ](#a399cbac4220647c4604c94fdb7512f8a)STM32\_DMA\_PERIPH\_TO\_MEMORY

| #define STM32\_DMA\_PERIPH\_TO\_MEMORY   [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(2) |
| --- |

## [◆ ](#a35bc7af86b12a421cc0391a43307d808)STM32\_DMA\_PERIPH\_TO\_PERIPH

| #define STM32\_DMA\_PERIPH\_TO\_PERIPH   [STM32\_DMA\_CH\_CFG\_DIRECTION](#a1184bb6207bf6347ede5b3cfd1b67da9)(3) |
| --- |

## [◆ ](#ab26996ccb981ef26dc0783302f4564f7)STM32\_DMA\_PERIPH\_TX

| #define STM32\_DMA\_PERIPH\_TX   ([STM32\_DMA\_MEMORY\_TO\_PERIPH](#ae0c8bc868d309a4fc1a57b28b6d88811) | [STM32\_DMA\_MEM\_INC](#a46f20993a4561c34cce25cf70f56879f)) |
| --- |

## [◆ ](#a2aeaf7b8cccb8512d0f18c07e66465de)STM32\_DMA\_PRIORITY\_HIGH

| #define STM32\_DMA\_PRIORITY\_HIGH   [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(2) |
| --- |

## [◆ ](#a1e3161e8a567113a9b3a6874ad9c7ec9)STM32\_DMA\_PRIORITY\_LOW

| #define STM32\_DMA\_PRIORITY\_LOW   [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(0) |
| --- |

## [◆ ](#a7ab285799783a4a45248f97c24cc2572)STM32\_DMA\_PRIORITY\_MEDIUM

| #define STM32\_DMA\_PRIORITY\_MEDIUM   [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(1) |
| --- |

## [◆ ](#a5ce1311f75b678c623f1276de3463aa5)STM32\_DMA\_PRIORITY\_VERY\_HIGH

| #define STM32\_DMA\_PRIORITY\_VERY\_HIGH   [STM32\_DMA\_CH\_CFG\_PRIORITY](#add3e03ced6f685382d43058f0cbceb9b)(3) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [stm32\_dma.h](stm32__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
