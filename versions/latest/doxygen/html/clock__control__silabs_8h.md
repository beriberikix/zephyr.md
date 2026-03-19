---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/clock__control__silabs_8h.html
original_path: doxygen/html/clock__control__silabs_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control\_silabs.h File Reference

`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`

[Go to the source code of this file.](clock__control__silabs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [silabs\_clock\_control\_cmu\_config](structsilabs__clock__control__cmu__config.md) |

| Macros | |
| --- | --- |
| #define | [SILABS\_DT\_CLOCK\_CFG](#a2238842842469b06a3cb0d0cf187583c)(node\_id) |
| #define | [SILABS\_DT\_INST\_CLOCK\_CFG](#a109d85a9e8fe8ec3730927a91d885721)(inst) |

## Macro Definition Documentation

## [◆ ](#a2238842842469b06a3cb0d0cf187583c)SILABS\_DT\_CLOCK\_CFG

| #define SILABS\_DT\_CLOCK\_CFG | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

.bus\_clock = [DT\_CLOCKS\_CELL](group__devicetree-clocks.md#ga211bc385cbbb1d8b8fa52e2e0a52d23d)(node\_id, enable), \

.branch = [DT\_CLOCKS\_CELL](group__devicetree-clocks.md#ga211bc385cbbb1d8b8fa52e2e0a52d23d)(node\_id, branch), \

}

[DT\_CLOCKS\_CELL](group__devicetree-clocks.md#ga211bc385cbbb1d8b8fa52e2e0a52d23d)

#define DT\_CLOCKS\_CELL(node\_id, cell)

Equivalent to DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, 0, cell).

**Definition** clocks.h:253

## [◆ ](#a109d85a9e8fe8ec3730927a91d885721)SILABS\_DT\_INST\_CLOCK\_CFG

| #define SILABS\_DT\_INST\_CLOCK\_CFG | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

.bus\_clock = [DT\_INST\_CLOCKS\_CELL](group__devicetree-clocks.md#gad6a9584690066548b8d61489ad615a45)(inst, enable), \

.branch = [DT\_INST\_CLOCKS\_CELL](group__devicetree-clocks.md#gad6a9584690066548b8d61489ad615a45)(inst, branch), \

}

[DT\_INST\_CLOCKS\_CELL](group__devicetree-clocks.md#gad6a9584690066548b8d61489ad615a45)

#define DT\_INST\_CLOCKS\_CELL(inst, cell)

Equivalent to DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, 0, cell).

**Definition** clocks.h:347

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_control\_silabs.h](clock__control__silabs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
