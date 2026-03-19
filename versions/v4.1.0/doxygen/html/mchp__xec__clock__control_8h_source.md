---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mchp__xec__clock__control_8h_source.html
original_path: doxygen/html/mchp__xec__clock__control_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp\_xec\_clock\_control.h

[Go to the documentation of this file.](mchp__xec__clock__control_8h.md)

1/\*

2 \* Copyright (c) 2021 Microchip Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_MCHP\_XEC\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_MCHP\_XEC\_H\_

8

9#include <[zephyr/drivers/clock\_control.h](clock__control_8h.md)>

10#include <[zephyr/dt-bindings/clock/mchp\_xec\_pcr.h](mchp__xec__pcr_8h.md)>

11

12/\*

13 \* Set/clear Microchip XEC peripheral sleep enable.

14 \* SoC layer contains the chip specific sleep index and positions

15 \*/

16int z\_mchp\_xec\_pcr\_periph\_sleep([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) slp\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) slp\_pos,

17 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) slp\_en);

18

19int z\_mchp\_xec\_pcr\_periph\_reset([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) slp\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) slp\_pos);

20

21#if defined(CONFIG\_PM)

22void mchp\_xec\_clk\_ctrl\_sys\_sleep\_enable(bool is\_deep);

23void mchp\_xec\_clk\_ctrl\_sys\_sleep\_disable(void);

24#endif

25

26#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CLOCK\_CONTROL\_LPC11U6X\_CLOCK\_CONTROL\_H\_ \*/

[clock\_control.h](clock__control_8h.md)

Public Clock Control APIs.

[mchp\_xec\_pcr.h](mchp__xec__pcr_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [mchp\_xec\_clock\_control.h](mchp__xec__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
