---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sw__isr__table_8h.html
original_path: doxygen/html/sw__isr__table_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sw\_isr\_table.h File Reference

Software-managed ISR table.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](sw__isr__table_8h_source.md)

| Macros | |
| --- | --- |
| #define | [INTC\_BASE\_ISR\_TBL\_OFFSET](#a9b130c84dbe718bcb89f7a83eb3a1d04)(node\_id) |
|  | Get an interrupt controller node's level base ISR table offset. |
| #define | [INTC\_INST\_ISR\_TBL\_OFFSET](#a810f9314f0a6d8a902593d0521660176)(inst) |
|  | Get the SW ISR table offset for an instance of interrupt controller. |
| #define | [INTC\_CHILD\_ISR\_TBL\_OFFSET](#a433c2b13315bd1fa93057a48b3b30122)(node\_id) |
|  | Get the SW ISR table offset for a child interrupt controller. |
| #define | [IRQ\_PARENT\_ENTRY\_DEFINE](#aaa922e8bad35d8f5a25d889cd14fd915)(\_name, \_dev, \_irq, \_offset, \_level) |
|  | Register an interrupt controller with the software ISR table. |
| #define | [ISR\_FLAG\_DIRECT](#a1376eec61303fcd20e7656175ddbaf19)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | This interrupt gets put directly in the vector table. |
| #define | [IRQ\_TABLE\_SIZE](#af36594d0586be77420bfe6eaf9f96a2c)   ([CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837) - [CONFIG\_GEN\_IRQ\_START\_VECTOR](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)) |

## Detailed Description

Software-managed ISR table.

Data types for a software-managed ISR table, with a parameter per-ISR.

## Macro Definition Documentation

## [◆ ](#a9b130c84dbe718bcb89f7a83eb3a1d04)INTC\_BASE\_ISR\_TBL\_OFFSET

| #define INTC\_BASE\_ISR\_TBL\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

Z\_SW\_ISR\_TBL\_KCONFIG\_BY\_ALVL([DT\_INTC\_GET\_AGGREGATOR\_LEVEL](group__devicetree-interrupt__controller.md#ga4eebef2c5e75d6a6c87d0cea03ac1bee)(node\_id))

[DT\_INTC\_GET\_AGGREGATOR\_LEVEL](group__devicetree-interrupt__controller.md#ga4eebef2c5e75d6a6c87d0cea03ac1bee)

#define DT\_INTC\_GET\_AGGREGATOR\_LEVEL(node\_id)

Get the aggregator level of an interrupt controller.

**Definition** interrupt\_controller.h:38

Get an interrupt controller node's level base ISR table offset.

Parameters
:   | node\_id | node identifier of the interrupt controller |
    | --- | --- |

Returns
:   CONFIG\_2ND\_LVL\_ISR\_TBL\_OFFSET if node\_id is a second level aggregator, CONFIG\_3RD\_LVL\_ISR\_TBL\_OFFSET if it is a third level aggregator

## [◆ ](#a433c2b13315bd1fa93057a48b3b30122)INTC\_CHILD\_ISR\_TBL\_OFFSET

| #define INTC\_CHILD\_ISR\_TBL\_OFFSET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([INTC\_BASE\_ISR\_TBL\_OFFSET](#a9b130c84dbe718bcb89f7a83eb3a1d04)(node\_id) + \

([DT\_NODE\_CHILD\_IDX](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)(node\_id) \* CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR))

[DT\_NODE\_CHILD\_IDX](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)

#define DT\_NODE\_CHILD\_IDX(node\_id)

Get a devicetree node's index into its parent's list of children.

**Definition** devicetree.h:552

[INTC\_BASE\_ISR\_TBL\_OFFSET](#a9b130c84dbe718bcb89f7a83eb3a1d04)

#define INTC\_BASE\_ISR\_TBL\_OFFSET(node\_id)

Get an interrupt controller node's level base ISR table offset.

**Definition** sw\_isr\_table.h:85

Get the SW ISR table offset for a child interrupt controller.

This macro is a alternative form of the [INTC\_INST\_ISR\_TBL\_OFFSET](#a810f9314f0a6d8a902593d0521660176). This is used by pseudo interrupt controller devices that are child of a main interrupt controller device.

Parameters
:   | node\_id | node identifier of the child interrupt controller |
    | --- | --- |

Returns
:   Software ISR table offset of the child

## [◆ ](#a810f9314f0a6d8a902593d0521660176)INTC\_INST\_ISR\_TBL\_OFFSET

| #define INTC\_INST\_ISR\_TBL\_OFFSET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([INTC\_BASE\_ISR\_TBL\_OFFSET](#a9b130c84dbe718bcb89f7a83eb3a1d04)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst)) + (inst \* CONFIG\_MAX\_IRQ\_PER\_AGGREGATOR))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

Get the SW ISR table offset for an instance of interrupt controller.

Parameters
:   | inst | DT\_DRV\_COMPAT interrupt controller driver instance number |
    | --- | --- |

Returns
:   Software ISR table offset of the interrupt controller

## [◆ ](#aaa922e8bad35d8f5a25d889cd14fd915)IRQ\_PARENT\_ENTRY\_DEFINE

| #define IRQ\_PARENT\_ENTRY\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_dev*, |
|  |  |  | *\_irq*, |
|  |  |  | *\_offset*, |
|  |  |  | *\_level* ) |

**Value:**

static const [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)(intc\_table, \_irq\_parent\_entry, \_name) = { \

.dev = \_dev, \

.level = \_level, \

.irq = \_irq, \

.offset = \_offset, \

}

[STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)

#define STRUCT\_SECTION\_ITERABLE\_ALTERNATE(secname, struct\_type, varname)

Defines a new element of alternate data type for an iterable section.

**Definition** iterable\_sections.h:188

Register an interrupt controller with the software ISR table.

Parameters
:   | \_name | Name of the interrupt controller (must be unique) |
    | --- | --- |
    | \_dev | Pointer to the interrupt controller device instance |
    | \_irq | Interrupt controller IRQ number |
    | \_offset | Software ISR table offset of the interrupt controller |
    | \_level | Interrupt controller aggregator level |

## [◆ ](#af36594d0586be77420bfe6eaf9f96a2c)IRQ\_TABLE\_SIZE

| #define IRQ\_TABLE\_SIZE   ([CONFIG\_NUM\_IRQS](arch_2xtensa_2irq_8h.md#a8f2a902348157b3b8718b05df1b1e837) - [CONFIG\_GEN\_IRQ\_START\_VECTOR](arch_2xtensa_2irq_8h.md#a8216dd1abd78c9fd201320bed1496c1c)) |
| --- |

## [◆ ](#a1376eec61303fcd20e7656175ddbaf19)ISR\_FLAG\_DIRECT

| #define ISR\_FLAG\_DIRECT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

This interrupt gets put directly in the vector table.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sw\_isr\_table.h](sw__isr__table_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
