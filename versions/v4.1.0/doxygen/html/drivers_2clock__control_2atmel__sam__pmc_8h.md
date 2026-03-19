---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h.html
original_path: doxygen/html/drivers_2clock__control_2atmel__sam__pmc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atmel\_sam\_pmc.h File Reference

`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`  
`#include <[zephyr/dt-bindings/clock/atmel_sam_pmc.h](dt-bindings_2clock_2atmel__sam__pmc_8h_source.md)>`

[Go to the source code of this file.](drivers_2clock__control_2atmel__sam__pmc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [atmel\_sam\_pmc\_config](structatmel__sam__pmc__config.md) |

| Macros | |
| --- | --- |
| #define | [SAM\_DT\_PMC\_CONTROLLER](#a90fa2e9a2226f7a2cb8926e9091b5eb3)   [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pmc)) |
| #define | [SAM\_DT\_CLOCK\_PMC\_CFG](#afe5b223995886a213b8e9108fdce94d5)(clock\_id, node\_id) |
| #define | [SAM\_DT\_INST\_CLOCK\_PMC\_CFG](#a0f6e3f89dcfde77d27b2685220055109)(inst) |
| #define | [SAM\_DT\_CLOCKS\_PMC\_CFG](#adc7b9d880d6ebcf81b47eafc223e8512)(node\_id) |
| #define | [SAM\_DT\_INST\_CLOCKS\_PMC\_CFG](#af27b70e3c0fa178c3096748bb636b704)(inst) |

## Macro Definition Documentation

## [◆ ](#afe5b223995886a213b8e9108fdce94d5)SAM\_DT\_CLOCK\_PMC\_CFG

| #define SAM\_DT\_CLOCK\_PMC\_CFG | ( |  | *clock\_id*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id* ) |

**Value:**

{ \

.clock\_type = [DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, clock\_id, clock\_type), \

.peripheral\_id = [DT\_CLOCKS\_CELL\_BY\_IDX](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)(node\_id, clock\_id, peripheral\_id)\

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

[SAM\_DT\_CLOCK\_PMC\_CFG](#afe5b223995886a213b8e9108fdce94d5), (,), node\_id) \

}

[SAM\_DT\_CLOCK\_PMC\_CFG](#afe5b223995886a213b8e9108fdce94d5)

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

[SAM\_DT\_CLOCK\_PMC\_CFG](#afe5b223995886a213b8e9108fdce94d5)(0, [DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

## [◆ ](#af27b70e3c0fa178c3096748bb636b704)SAM\_DT\_INST\_CLOCKS\_PMC\_CFG

| #define SAM\_DT\_INST\_CLOCKS\_PMC\_CFG | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[SAM\_DT\_CLOCKS\_PMC\_CFG](#adc7b9d880d6ebcf81b47eafc223e8512)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[SAM\_DT\_CLOCKS\_PMC\_CFG](#adc7b9d880d6ebcf81b47eafc223e8512)

#define SAM\_DT\_CLOCKS\_PMC\_CFG(node\_id)

**Definition** atmel\_sam\_pmc.h:28

## [◆ ](#a90fa2e9a2226f7a2cb8926e9091b5eb3)SAM\_DT\_PMC\_CONTROLLER

| #define SAM\_DT\_PMC\_CONTROLLER   [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pmc)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [atmel\_sam\_pmc.h](drivers_2clock__control_2atmel__sam__pmc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
