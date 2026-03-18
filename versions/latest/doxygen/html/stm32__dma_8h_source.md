---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32__dma_8h_source.html
original_path: doxygen/html/stm32__dma_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32\_dma.h

[Go to the documentation of this file.](stm32__dma_8h.md)

1/\*

2 \* Copyright (c) 2023 STMicroelectronics

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32\_DMA\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32\_DMA\_H\_

8

[ 14](stm32__dma_8h.md#a86e8ab71081233e1f9aa8300b6ea3c85)#define STM32\_DMA\_CH\_CFG\_MODE(val) ((val & 0x1) << 5)

[ 15](stm32__dma_8h.md#a6d811813db4e97b831b4b1fb95ec594c)#define STM32\_DMA\_MODE\_NORMAL STM32\_DMA\_CH\_CFG\_MODE(0)

[ 16](stm32__dma_8h.md#a944c3985d60fa92a53b9db6c57a54e6a)#define STM32\_DMA\_MODE\_CYCLIC STM32\_DMA\_CH\_CFG\_MODE(1)

17

[ 19](stm32__dma_8h.md#a1184bb6207bf6347ede5b3cfd1b67da9)#define STM32\_DMA\_CH\_CFG\_DIRECTION(val) ((val & 0x3) << 6)

[ 20](stm32__dma_8h.md#a3678dc5bb6f7b7a7c7fbb87c43ad3724)#define STM32\_DMA\_MEMORY\_TO\_MEMORY STM32\_DMA\_CH\_CFG\_DIRECTION(0)

[ 21](stm32__dma_8h.md#ae0c8bc868d309a4fc1a57b28b6d88811)#define STM32\_DMA\_MEMORY\_TO\_PERIPH STM32\_DMA\_CH\_CFG\_DIRECTION(1)

[ 22](stm32__dma_8h.md#a399cbac4220647c4604c94fdb7512f8a)#define STM32\_DMA\_PERIPH\_TO\_MEMORY STM32\_DMA\_CH\_CFG\_DIRECTION(2)

[ 23](stm32__dma_8h.md#a35bc7af86b12a421cc0391a43307d808)#define STM32\_DMA\_PERIPH\_TO\_PERIPH STM32\_DMA\_CH\_CFG\_DIRECTION(3)

24

[ 26](stm32__dma_8h.md#a69d16d7d3474f075c8a639370297eeaa)#define STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC(val) ((val & 0x1) << 9)

[ 27](stm32__dma_8h.md#aa7cc172e318bf2558a44c87f1b1d3693)#define STM32\_DMA\_PERIPH\_NO\_INC STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC(0)

[ 28](stm32__dma_8h.md#ae0f9a8b757005339a550959930084ecb)#define STM32\_DMA\_PERIPH\_INC STM32\_DMA\_CH\_CFG\_PERIPH\_ADDR\_INC(1)

29

[ 31](stm32__dma_8h.md#abf66072cff1f8d835beb78a8d974fa2a)#define STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC(val) ((val & 0x1) << 10)

[ 32](stm32__dma_8h.md#ae46002f328f981e5dbe7bc502c46b759)#define STM32\_DMA\_MEM\_NO\_INC STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC(0)

[ 33](stm32__dma_8h.md#a46f20993a4561c34cce25cf70f56879f)#define STM32\_DMA\_MEM\_INC STM32\_DMA\_CH\_CFG\_MEM\_ADDR\_INC(1)

34

[ 36](stm32__dma_8h.md#a0c0c0c5cde99d895079197bf75c25245)#define STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(val) ((val & 0x3) << 11)

[ 37](stm32__dma_8h.md#a8ab5a7090927e92bef333fb33416c32b)#define STM32\_DMA\_PERIPH\_8BITS STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(0)

[ 38](stm32__dma_8h.md#aad24cf95434530d2d64025512d467d5e)#define STM32\_DMA\_PERIPH\_16BITS STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(1)

[ 39](stm32__dma_8h.md#af869e4e36689a3b9402425f0a7dcc970)#define STM32\_DMA\_PERIPH\_32BITS STM32\_DMA\_CH\_CFG\_PERIPH\_WIDTH(2)

40

[ 42](stm32__dma_8h.md#ac0bb2e159dc52537c60851c1b9bac4c3)#define STM32\_DMA\_CH\_CFG\_MEM\_WIDTH(val) ((val & 0x3) << 13)

[ 43](stm32__dma_8h.md#a372c638a2cffdcb69f7748e12e1564d9)#define STM32\_DMA\_MEM\_8BITS STM32\_DMA\_CH\_CFG\_MEM\_WIDTH(0)

[ 44](stm32__dma_8h.md#ac9f13ef8eb95fc507d707064a5dae605)#define STM32\_DMA\_MEM\_16BITS STM32\_DMA\_CH\_CFG\_MEM\_WIDTH(1)

[ 45](stm32__dma_8h.md#ab5cc477888dac48daacf0365530dba95)#define STM32\_DMA\_MEM\_32BITS STM32\_DMA\_CH\_CFG\_MEM\_WIDTH(2)

46

[ 48](stm32__dma_8h.md#a7f7fa52e8b080c1ea756cd8df666c9cf)#define STM32\_DMA\_CH\_CFG\_PERIPH\_INC\_FIXED(val) ((val & 0x1) << 15)

49

[ 51](stm32__dma_8h.md#add3e03ced6f685382d43058f0cbceb9b)#define STM32\_DMA\_CH\_CFG\_PRIORITY(val) ((val & 0x3) << 16)

[ 52](stm32__dma_8h.md#a1e3161e8a567113a9b3a6874ad9c7ec9)#define STM32\_DMA\_PRIORITY\_LOW STM32\_DMA\_CH\_CFG\_PRIORITY(0)

[ 53](stm32__dma_8h.md#a7ab285799783a4a45248f97c24cc2572)#define STM32\_DMA\_PRIORITY\_MEDIUM STM32\_DMA\_CH\_CFG\_PRIORITY(1)

[ 54](stm32__dma_8h.md#a2aeaf7b8cccb8512d0f18c07e66465de)#define STM32\_DMA\_PRIORITY\_HIGH STM32\_DMA\_CH\_CFG\_PRIORITY(2)

[ 55](stm32__dma_8h.md#a5ce1311f75b678c623f1276de3463aa5)#define STM32\_DMA\_PRIORITY\_VERY\_HIGH STM32\_DMA\_CH\_CFG\_PRIORITY(3)

56

[ 58](stm32__dma_8h.md#a30103ad3e6fe698187674f09af5bf057)#define STM32\_DMA\_FIFO\_1\_4 0U

[ 59](stm32__dma_8h.md#a6595f13f24d26e28aa82b1571c03075c)#define STM32\_DMA\_FIFO\_HALF 1U

[ 60](stm32__dma_8h.md#a8720db61ce6623cf6a96ac862fa89041)#define STM32\_DMA\_FIFO\_3\_4 2U

[ 61](stm32__dma_8h.md#a4a561bb696eeaf8f8878fc327eab5f37)#define STM32\_DMA\_FIFO\_FULL 3U

62

63/\* DMA usual combination for peripheral transfer \*/

[ 64](stm32__dma_8h.md#ab26996ccb981ef26dc0783302f4564f7)#define STM32\_DMA\_PERIPH\_TX (STM32\_DMA\_MEMORY\_TO\_PERIPH | STM32\_DMA\_MEM\_INC)

[ 65](stm32__dma_8h.md#ac680c9808061136e327cf6a14b09ea57)#define STM32\_DMA\_PERIPH\_RX (STM32\_DMA\_PERIPH\_TO\_MEMORY | STM32\_DMA\_MEM\_INC)

66

68

69#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_STM32\_DMA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [stm32\_dma.h](stm32__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
