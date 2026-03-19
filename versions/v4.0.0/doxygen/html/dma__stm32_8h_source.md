---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dma__stm32_8h_source.html
original_path: doxygen/html/dma__stm32_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_stm32.h

[Go to the documentation of this file.](dma__stm32_8h.md)

1/\*

2 \* Copyright (c) 2021 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_STM32\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_STM32\_H\_

9

10/\* @brief linked\_channel value to inform zephyr dma driver that

11 \* DMA channel will be handled by HAL

12 \*/

[ 13](dma__stm32_8h.md#a00fdf498cabe4214e28add6ef55681bc)#define STM32\_DMA\_HAL\_OVERRIDE 0x7F

14

15/\* @brief gives the first DMA channel : 0 or 1 in the register map

16 \* when counting channels from 1 to N or from 0 to N-1

17 \*/

18#if defined(CONFIG\_DMA\_STM32U5)

19/\* from DTS the dma stream id is in range 0..N-1 \*/

20#define STM32\_DMA\_STREAM\_OFFSET 0

21#elif !defined(CONFIG\_DMA\_STM32\_V1)

22/\* from DTS the dma stream id is in range 1..N \*/

23/\* so decrease to set range from 0 from now on \*/

[ 24](dma__stm32_8h.md#aca656daf77c45e1d6b18e911bcb6b76b)#define STM32\_DMA\_STREAM\_OFFSET 1

25#elif defined(CONFIG\_DMA\_STM32\_V1) && defined(CONFIG\_DMAMUX\_STM32)

26/\* typically on the stm32H7 series, DMA V1 with mux \*/

27#define STM32\_DMA\_STREAM\_OFFSET 1

28#else

29/\* from DTS the dma stream id is in range 0..N-1 \*/

30#define STM32\_DMA\_STREAM\_OFFSET 0

31#endif /\* ! CONFIG\_DMA\_STM32\_V1 \*/

32

33/\* macro for dma slot (only for dma-v1 or dma-v2 types) \*/

34#if DT\_HAS\_COMPAT\_STATUS\_OKAY(st\_stm32\_dma\_v2bis)

35#define STM32\_DMA\_SLOT(id, dir, slot) 0

36#define STM32\_DMA\_SLOT\_BY\_IDX(id, idx, slot) 0

37#else

[ 38](dma__stm32_8h.md#ad2f2b0a1e77f5f829bb2833a31486ff8)#define STM32\_DMA\_SLOT(id, dir, slot) DT\_INST\_DMAS\_CELL\_BY\_NAME(id, dir, slot)

[ 39](dma__stm32_8h.md#a1802cfe36a268822a2e008b0a748b8c5)#define STM32\_DMA\_SLOT\_BY\_IDX(id, idx, slot) DT\_INST\_DMAS\_CELL\_BY\_IDX(id, idx, slot)

40#endif

41

42#if DT\_HAS\_COMPAT\_STATUS\_OKAY(st\_stm32\_dma\_v2) || \

43 DT\_HAS\_COMPAT\_STATUS\_OKAY(st\_stm32\_dma\_v2bis) || \

44 DT\_HAS\_COMPAT\_STATUS\_OKAY(st\_stm32\_dmamux)

45#define STM32\_DMA\_FEATURES(id, dir) 0

46#else

[ 47](dma__stm32_8h.md#aa1aa5181a6387f56cc914c755d4dcb69)#define STM32\_DMA\_FEATURES(id, dir) \

48 DT\_INST\_DMAS\_CELL\_BY\_NAME(id, dir, features)

49#endif

50

[ 51](dma__stm32_8h.md#a65697918b25bd6e316a2141289a3bba4)#define STM32\_DMA\_CTLR(id, dir) \

52 DT\_INST\_DMAS\_CTLR\_BY\_NAME(id, dir)

[ 53](dma__stm32_8h.md#ac9830f1d3c46089010a8354fc344b68e)#define STM32\_DMA\_CHANNEL\_CONFIG(id, dir) \

54 DT\_INST\_DMAS\_CELL\_BY\_NAME(id, dir, channel\_config)

[ 55](dma__stm32_8h.md#a8739b1eb41560e1fc46afc464f5ac0c3)#define STM32\_DMA\_CHANNEL\_CONFIG\_BY\_IDX(id, idx) \

56 DT\_INST\_DMAS\_CELL\_BY\_IDX(id, idx, channel\_config)

57

58/\* macros for channel-config \*/

59/\* direction defined on bits 6-7 \*/

60/\* 0 -> MEM\_TO\_MEM, 1 -> MEM\_TO\_PERIPH, 2 -> PERIPH\_TO\_MEM \*/

[ 61](dma__stm32_8h.md#aed17fb68ee78831fbce6628cc97ef4d0)#define STM32\_DMA\_CONFIG\_DIRECTION(config) ((config >> 6) & 0x3)

62/\* periph increment defined on bit 9 as true/false \*/

[ 63](dma__stm32_8h.md#a1b97fe65f90e0b73f1450e5a763cc5cb)#define STM32\_DMA\_CONFIG\_PERIPHERAL\_ADDR\_INC(config) ((config >> 9) & 0x1)

64/\* mem increment defined on bit 10 as true/false \*/

[ 65](dma__stm32_8h.md#ad4bb23a652c15f856431d13048ac639f)#define STM32\_DMA\_CONFIG\_MEMORY\_ADDR\_INC(config) ((config >> 10) & 0x1)

66/\* periph data size defined on bits 11-12 \*/

67/\* 0 -> 1 byte, 1 -> 2 bytes, 2 -> 4 bytes \*/

[ 68](dma__stm32_8h.md#a208ec04cc0c0e8e41012c6c07bd10e3e)#define STM32\_DMA\_CONFIG\_PERIPHERAL\_DATA\_SIZE(config) \

69 (1 << ((config >> 11) & 0x3))

70/\* memory data size defined on bits 13, 14 \*/

71/\* 0 -> 1 byte, 1 -> 2 bytes, 2 -> 4 bytes \*/

[ 72](dma__stm32_8h.md#ae2664884f88d4df0be45c189ecdabf1d)#define STM32\_DMA\_CONFIG\_MEMORY\_DATA\_SIZE(config) \

73 (1 << ((config >> 13) & 0x3))

74/\* priority increment offset defined on bit 15 \*/

[ 75](dma__stm32_8h.md#ac1e469f441e34af9a62fc4ab697a0275)#define STM32\_DMA\_CONFIG\_PERIPHERAL\_INC\_FIXED(config) ((config >> 15) & 0x1)

76/\* priority defined on bits 16-17 as 0, 1, 2, 3 \*/

[ 77](dma__stm32_8h.md#af20462bb4d9f9a38dec07add57de4795)#define STM32\_DMA\_CONFIG\_PRIORITY(config) ((config >> 16) & 0x3)

78

79/\* macro for features (only for dma-v1) \*/

80#if DT\_HAS\_COMPAT\_STATUS\_OKAY(st\_stm32\_dma\_v1)

81#define STM32\_DMA\_FEATURES\_FIFO\_THRESHOLD(features) (features & 0x3)

82#else

[ 83](dma__stm32_8h.md#abf490559310376a854ae1e8ee18209ce)#define STM32\_DMA\_FEATURES\_FIFO\_THRESHOLD(features) 0

84#endif

85

86#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_STM32\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_stm32.h](dma__stm32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
