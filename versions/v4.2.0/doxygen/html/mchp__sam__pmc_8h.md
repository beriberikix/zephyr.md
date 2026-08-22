---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mchp__sam__pmc_8h.html
original_path: doxygen/html/mchp__sam__pmc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp\_sam\_pmc.h File Reference

`#include <soc.h>`  
`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`  
`#include <[zephyr/dt-bindings/clock/microchip_sam_pmc.h](microchip__sam__pmc_8h_source.md)>`

[Go to the source code of this file.](mchp__sam__pmc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sam\_sckc\_config](structsam__sckc__config.md) |
| struct | [sam\_clk\_cfg](structsam__clk__cfg.md) |
| struct | [sam\_pmc\_cfg](structsam__pmc__cfg.md) |
| struct | [sam\_pmc\_data](structsam__pmc__data.md) |

| Macros | |
| --- | --- |
| #define | [SAM\_DT\_CLOCK\_PMC\_CFG](#ae6ab16601edc5287a1657ff7bb1c8dbd)(clock, node\_id) |
| #define | [SAM\_DT\_INST\_CLOCK\_PMC\_CFG](#a0f6e3f89dcfde77d27b2685220055109)(inst) |
| #define | [SAM\_DT\_CLOCKS\_PMC\_CFG](#adc7b9d880d6ebcf81b47eafc223e8512)(node\_id) |
| #define | [SAM\_DT\_INST\_CLOCKS\_PMC\_CFG](#af27b70e3c0fa178c3096748bb636b704)(inst) |

## Macro Definition Documentation

## [◆ ](#ae6ab16601edc5287a1657ff7bb1c8dbd)SAM\_DT\_CLOCK\_PMC\_CFG

| #define SAM\_DT\_CLOCK\_PMC\_CFG | ( |  | *clock*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

**Value:**

{ \

.clock\_type = [DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, \

clock, \

clock\_type), \

.clock\_id = [DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, \

clock, \

peripheral\_id) \

}

[DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)

#define DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, idx, cell)

Get a clock specifier's cell value at an index.

**Definition** clocks.h:207

## [◆ ](#adc7b9d880d6ebcf81b47eafc223e8512)SAM\_DT\_CLOCKS\_PMC\_CFG

| #define SAM\_DT\_CLOCKS\_PMC\_CFG | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

LISTIFY([DT\_NUM\_CLOCKS](group__devicetree-clocks.md#ga22d4e8621b5bf56ed0ac8295dd11d7e3)(node\_id), \

[SAM\_DT\_CLOCK\_PMC\_CFG](drivers_2clock__control_2atmel__sam__pmc_8h.md#afe5b223995886a213b8e9108fdce94d5), (,), node\_id) \

}

[SAM\_DT\_CLOCK\_PMC\_CFG](drivers_2clock__control_2atmel__sam__pmc_8h.md#afe5b223995886a213b8e9108fdce94d5)

#define SAM\_DT\_CLOCK\_PMC\_CFG(clock\_id, node\_id)

**Definition** atmel\_sam\_pmc.h:20

[DT\_NUM\_CLOCKS](group__devicetree-clocks.md#ga22d4e8621b5bf56ed0ac8295dd11d7e3)

#define DT\_NUM\_CLOCKS(node\_id)

Get the number of elements in a clocks property.

**Definition** clocks.h:107

## [◆ ](#a0f6e3f89dcfde77d27b2685220055109)SAM\_DT\_INST\_CLOCK\_PMC\_CFG

| #define SAM\_DT\_INST\_CLOCK\_PMC\_CFG | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SAM\_DT\_CLOCK\_PMC\_CFG](drivers_2clock__control_2atmel__sam__pmc_8h.md#afe5b223995886a213b8e9108fdce94d5)(0, [DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

## [◆ ](#af27b70e3c0fa178c3096748bb636b704)SAM\_DT\_INST\_CLOCKS\_PMC\_CFG

| #define SAM\_DT\_INST\_CLOCKS\_PMC\_CFG | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SAM\_DT\_CLOCKS\_PMC\_CFG](drivers_2clock__control_2atmel__sam__pmc_8h.md#adc7b9d880d6ebcf81b47eafc223e8512)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[SAM\_DT\_CLOCKS\_PMC\_CFG](drivers_2clock__control_2atmel__sam__pmc_8h.md#adc7b9d880d6ebcf81b47eafc223e8512)

#define SAM\_DT\_CLOCKS\_PMC\_CFG(node\_id)

**Definition** atmel\_sam\_pmc.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [mchp\_sam\_pmc.h](mchp__sam__pmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
