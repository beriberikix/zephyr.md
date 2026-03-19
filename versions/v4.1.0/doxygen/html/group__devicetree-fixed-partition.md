---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__devicetree-fixed-partition.html
original_path: doxygen/html/group__devicetree-fixed-partition.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree Fixed Partition API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL](#gafcd93790974c48b10dd1170d14c49bf9)(label) |
|  | Get a node identifier for a fixed partition with a given label property. |
| #define | [DT\_HAS\_FIXED\_PARTITION\_LABEL](#gac402d149d6b527cccf5f955f1ad57fc3)(label) |
|  | Test if a fixed partition with a given label property exists. |
| #define | [DT\_FIXED\_PARTITION\_EXISTS](#ga444fa975d314c342268a6d211627c3d1)(node\_id) |
|  | Test if fixed-partition compatible node exists. |
| #define | [DT\_FIXED\_PARTITION\_ID](#gaf3b448e91dff79ece4d67ef833088ac9)(node\_id) |
|  | Get a numeric identifier for a fixed partition. |
| #define | [DT\_MEM\_FROM\_FIXED\_PARTITION](#gae89b5f21fecae407f3b1baf231e4dba5)(node\_id) |
|  | Get the node identifier of the flash memory for a partition. |
| #define | [DT\_MTD\_FROM\_FIXED\_PARTITION](#ga3484bb9a0cd8c2a4d971989dc58c194e)(node\_id) |
|  | Get the node identifier of the flash controller for a partition. |
| #define | [DT\_FIXED\_PARTITION\_ADDR](#gac8be7ec2cddde3f76f0f096bd3c63546)(node\_id) |
|  | Get the absolute address of a fixed partition. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gac8be7ec2cddde3f76f0f096bd3c63546)DT\_FIXED\_PARTITION\_ADDR

| #define DT\_FIXED\_PARTITION\_ADDR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fixed-partitions.h](fixed-partitions_8h.md)>`

**Value:**

([DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)([DT\_MEM\_FROM\_FIXED\_PARTITION](#gae89b5f21fecae407f3b1baf231e4dba5)(node\_id)) + [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id))

[DT\_MEM\_FROM\_FIXED\_PARTITION](#gae89b5f21fecae407f3b1baf231e4dba5)

#define DT\_MEM\_FROM\_FIXED\_PARTITION(node\_id)

Get the node identifier of the flash memory for a partition.

**Definition** fixed-partitions.h:86

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2461

Get the absolute address of a fixed partition.

Example devicetree fragment:

```
&flash_controller {
        flash@1000000 {
                compatible = "soc-nv-flash";
                partitions {
                        compatible = "fixed-partitions";
                        storage_partition: partition@3a000 {
                                label = "storage";
                        };
                };
        };
};
```

Here, the "storage" partition is seen to belong to flash memory starting at address 0x1000000. The partition's unit address of 0x3a000 represents an offset inside that flash memory.

Example usage:

```
DT_FIXED_PARTITION_ADDR(DT_NODELABEL(storage_partition)) // 0x103a000
```

This macro can only be used with partitions of internal memory addressable by the CPU. Otherwise, it may produce a compile-time error, such as: '\_\_REG\_IDX\_0\_VAL\_ADDRESS' undeclared.

Parameters
:   | node\_id | node identifier for a fixed-partitions child node |
    | --- | --- |

Returns
:   the partition's offset plus the base address of the flash node containing it.

## [◆ ](#ga444fa975d314c342268a6d211627c3d1)DT\_FIXED\_PARTITION\_EXISTS

| #define DT\_FIXED\_PARTITION\_EXISTS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fixed-partitions.h](fixed-partitions_8h.md)>`

**Value:**

[DT\_NODE\_HAS\_COMPAT](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)([DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)(node\_id), fixed\_partitions)

[DT\_NODE\_HAS\_COMPAT](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)

#define DT\_NODE\_HAS\_COMPAT(node\_id, compat)

Does a devicetree node match a compatible?

**Definition** devicetree.h:3751

[DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)

#define DT\_PARENT(node\_id)

Get a node identifier for a parent node.

**Definition** devicetree.h:374

Test if fixed-partition compatible node exists.

Parameters
:   | node\_id | DTS node to test |
    | --- | --- |

Returns
:   1 if node exists and is fixed-partition compatible, 0 otherwise.

## [◆ ](#gaf3b448e91dff79ece4d67ef833088ac9)DT\_FIXED\_PARTITION\_ID

| #define DT\_FIXED\_PARTITION\_ID | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fixed-partitions.h](fixed-partitions_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_PARTITION\_ID)

Get a numeric identifier for a fixed partition.

Parameters
:   | node\_id | node identifier for a fixed-partitions child node |
    | --- | --- |

Returns
:   the partition's ID, a unique zero-based index number

## [◆ ](#gac402d149d6b527cccf5f955f1ad57fc3)DT\_HAS\_FIXED\_PARTITION\_LABEL

| #define DT\_HAS\_FIXED\_PARTITION\_LABEL | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fixed-partitions.h](fixed-partitions_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT3(DT\_COMPAT\_fixed\_partitions\_LABEL\_, label, \_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

Test if a fixed partition with a given label property exists.

Parameters
:   | label | lowercase-and-underscores label property value |
    | --- | --- |

Returns
:   1 if any "fixed-partitions" child node has the given label, 0 otherwise.

## [◆ ](#gae89b5f21fecae407f3b1baf231e4dba5)DT\_MEM\_FROM\_FIXED\_PARTITION

| #define DT\_MEM\_FROM\_FIXED\_PARTITION | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fixed-partitions.h](fixed-partitions_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_COMPAT](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)([DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)(node\_id), soc\_nv\_flash), ([DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)(node\_id)), \

([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)))

[DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)

#define DT\_INVALID\_NODE

Name for an invalid node identifier.

**Definition** devicetree.h:83

[DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)

#define DT\_GPARENT(node\_id)

Get a node identifier for a grandparent node.

**Definition** devicetree.h:399

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

Get the node identifier of the flash memory for a partition.

Parameters
:   | node\_id | node identifier for a fixed-partitions child node |
    | --- | --- |

Returns
:   the node identifier of the internal memory that contains the fixed-partitions node, or [DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855 "DT_INVALID_NODE") if it doesn't exist.

## [◆ ](#ga3484bb9a0cd8c2a4d971989dc58c194e)DT\_MTD\_FROM\_FIXED\_PARTITION

| #define DT\_MTD\_FROM\_FIXED\_PARTITION | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fixed-partitions.h](fixed-partitions_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)([DT\_MEM\_FROM\_FIXED\_PARTITION](#gae89b5f21fecae407f3b1baf231e4dba5)(node\_id)), \

([DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)([DT\_MEM\_FROM\_FIXED\_PARTITION](#gae89b5f21fecae407f3b1baf231e4dba5)(node\_id))), ([DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)(node\_id)))

[DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)

#define DT\_NODE\_EXISTS(node\_id)

Does a node identifier refer to a node?

**Definition** devicetree.h:3644

Get the node identifier of the flash controller for a partition.

Parameters
:   | node\_id | node identifier for a fixed-partitions child node |
    | --- | --- |

Returns
:   the node identifier of the memory technology device that contains the fixed-partitions node.

## [◆ ](#gafcd93790974c48b10dd1170d14c49bf9)DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL

| #define DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fixed-partitions.h](fixed-partitions_8h.md)>`

**Value:**

DT\_CAT(DT\_COMPAT\_fixed\_partitions\_LABEL\_, label)

Get a node identifier for a fixed partition with a given label property.

Example devicetree fragment:

```
flash@... {
         partitions {
                 compatible = "fixed-partitions";
                 boot_partition: partition@0 {
                         label = "mcuboot";
                 };
                 slot0_partition: partition@c000 {
                         label = "image-0";
                 };
                 ...
         };
};
```

Example usage:

```
DT_NODE_BY_FIXED_PARTITION_LABEL(mcuboot) // node identifier for boot_partition
DT_NODE_BY_FIXED_PARTITION_LABEL(image_0) // node identifier for slot0_partition
```

Parameters
:   | label | lowercase-and-underscores label property value |
    | --- | --- |

Returns
:   a node identifier for the partition with that label property

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
