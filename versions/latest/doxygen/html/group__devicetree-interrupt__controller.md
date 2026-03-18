---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__devicetree-interrupt__controller.html
original_path: doxygen/html/group__devicetree-interrupt__controller.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree Interrupt Controller API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_INTC\_GET\_AGGREGATOR\_LEVEL](#ga4eebef2c5e75d6a6c87d0cea03ac1bee)(node\_id) |
|  | Get the aggregator level of an interrupt controller. |
| #define | [DT\_INST\_INTC\_GET\_AGGREGATOR\_LEVEL](#ga914952a10c55fecc1f6e7c0cc3685b1b)(inst) |
|  | Get the aggregator level of a DT\_DRV\_COMPAT interrupt controller. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga914952a10c55fecc1f6e7c0cc3685b1b)DT\_INST\_INTC\_GET\_AGGREGATOR\_LEVEL

| #define DT\_INST\_INTC\_GET\_AGGREGATOR\_LEVEL | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[interrupt_controller.h](interrupt__controller_8h.md)>`

**Value:**

[DT\_INTC\_GET\_AGGREGATOR\_LEVEL](#ga4eebef2c5e75d6a6c87d0cea03ac1bee)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

[DT\_INTC\_GET\_AGGREGATOR\_LEVEL](#ga4eebef2c5e75d6a6c87d0cea03ac1bee)

#define DT\_INTC\_GET\_AGGREGATOR\_LEVEL(node\_id)

Get the aggregator level of an interrupt controller.

**Definition** interrupt\_controller.h:38

Get the aggregator level of a DT\_DRV\_COMPAT interrupt controller.

Note
:   Aggregator level is equivalent to IRQ\_LEVEL + 1 (a 2nd level aggregator has Zephyr level 1 IRQ encoding)

Parameters
:   | inst | instance of an interrupt controller |
    | --- | --- |

Returns
:   Level of the interrupt controller

## [◆ ](#ga4eebef2c5e75d6a6c87d0cea03ac1bee)DT\_INTC\_GET\_AGGREGATOR\_LEVEL

| #define DT\_INTC\_GET\_AGGREGATOR\_LEVEL | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[interrupt_controller.h](interrupt__controller_8h.md)>`

**Value:**

[UTIL\_INC](group__sys-util.md#ga90a54212306c3e210ac87fd0bd7b32da)([DT\_IRQ\_LEVEL](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)(node\_id))

[DT\_IRQ\_LEVEL](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)

#define DT\_IRQ\_LEVEL(node\_id)

Get the interrupt level for the node.

**Definition** devicetree.h:2409

[UTIL\_INC](group__sys-util.md#ga90a54212306c3e210ac87fd0bd7b32da)

#define UTIL\_INC(x)

UTIL\_INC(x) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x+1.

**Definition** util\_macro.h:399

Get the aggregator level of an interrupt controller.

Note
:   Aggregator level is equivalent to IRQ\_LEVEL + 1 (a 2nd level aggregator has Zephyr level 1 IRQ encoding)

Parameters
:   | node\_id | node identifier of an interrupt controller |
    | --- | --- |

Returns
:   Level of the interrupt controller

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
