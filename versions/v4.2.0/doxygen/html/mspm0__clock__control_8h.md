---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mspm0__clock__control_8h.html
original_path: doxygen/html/mspm0__clock__control_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspm0\_clock\_control.h File Reference

`#include <[zephyr/dt-bindings/clock/mspm0_clock.h](mspm0__clock_8h_source.md)>`

[Go to the source code of this file.](mspm0__clock__control_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mspm0\_sys\_clock](structmspm0__sys__clock.md) |

| Macros | |
| --- | --- |
| #define | [MSPM0\_CLOCK\_SUBSYS\_FN](#a438e7623f4a0dde8f48ce81cc9ecb4d5)(index) |

## Macro Definition Documentation

## [◆ ](#a438e7623f4a0dde8f48ce81cc9ecb4d5)MSPM0\_CLOCK\_SUBSYS\_FN

| #define MSPM0\_CLOCK\_SUBSYS\_FN | ( |  | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{.clk = [DT\_INST\_CLOCKS\_CELL](group__devicetree-clocks.md#gad6a9584690066548b8d61489ad615a45)(index, clk)}

[DT\_INST\_CLOCKS\_CELL](group__devicetree-clocks.md#gad6a9584690066548b8d61489ad615a45)

#define DT\_INST\_CLOCKS\_CELL(inst, cell)

Equivalent to DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, 0, cell).

**Definition** clocks.h:347

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [mspm0\_clock\_control.h](mspm0__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
