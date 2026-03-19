---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree__regions_8h.html
original_path: doxygen/html/devicetree__regions_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devicetree\_regions.h File Reference

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](devicetree__regions_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN](#a9df6c66f56e571a0dada9ab46b40ba26)(node\_id) |
|  | Get the linker memory-region name in a token form. |
| #define | [LINKER\_DT\_NODE\_REGION\_NAME](#a3244e16032cc575ab5c7275caca14801)(node\_id) |
|  | Get the linker memory-region name. |
| #define | [LINKER\_DT\_REGIONS](#a1b743e1c6c735c87d4fbd2094819c573)() |
|  | Generate linker memory regions from the device tree nodes with compatible 'zephyr,memory-region'. |
| #define | [LINKER\_DT\_SECTIONS](#a171f1425c840f60dd94722ff046e0e81)() |
|  | Generate linker memory sections from the device tree nodes with compatible 'zephyr,memory-region'. |

## Macro Definition Documentation

## [◆ ](#a3244e16032cc575ab5c7275caca14801)LINKER\_DT\_NODE\_REGION\_NAME

| #define LINKER\_DT\_NODE\_REGION\_NAME | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)([LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN](#a9df6c66f56e571a0dada9ab46b40ba26)(node\_id))

[LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN](#a9df6c66f56e571a0dada9ab46b40ba26)

#define LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN(node\_id)

Get the linker memory-region name in a token form.

**Definition** devicetree\_regions.h:48

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

Get the linker memory-region name.

This attempts to use the zephyr,memory-region property (with non-alphanumeric characters replaced with underscores).

Example devicetree fragment:

/ {

soc {

sram1: memory@2000000 {

zephyr,memory-region = "MY\_NAME";

};

sram2: memory@2001000 {

zephyr,memory-region = "MY@OTHER@NAME";

};

};

};

Example usage:

[LINKER\_DT\_NODE\_REGION\_NAME](#a3244e16032cc575ab5c7275caca14801)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(sram1)) // "MY\_NAME"

[LINKER\_DT\_NODE\_REGION\_NAME](#a3244e16032cc575ab5c7275caca14801)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(sram2)) // "MY\_OTHER\_NAME"

[LINKER\_DT\_NODE\_REGION\_NAME](#a3244e16032cc575ab5c7275caca14801)

#define LINKER\_DT\_NODE\_REGION\_NAME(node\_id)

Get the linker memory-region name.

**Definition** devicetree\_regions.h:82

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the name of the memory memory region the node will generate

## [◆ ](#a9df6c66f56e571a0dada9ab46b40ba26)LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN

| #define LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)(node\_id, zephyr\_memory\_region)

[DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)

#define DT\_STRING\_TOKEN(node\_id, prop)

Get a string property's value as a token.

**Definition** devicetree.h:1088

Get the linker memory-region name in a token form.

This attempts to use the zephyr,memory-region property (with non-alphanumeric characters replaced with underscores) returning a token.

Example devicetree fragment:

/ {

soc {

sram1: memory@2000000 {

zephyr,memory-region = "MY\_NAME";

};

sram2: memory@2001000 {

zephyr,memory-region = "MY@OTHER@NAME";

};

};

};

Example usage:

[LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN](#a9df6c66f56e571a0dada9ab46b40ba26)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(sram1)) // MY\_NAME

[LINKER\_DT\_NODE\_REGION\_NAME\_TOKEN](#a9df6c66f56e571a0dada9ab46b40ba26)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(sram2)) // MY\_OTHER\_NAME

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the name of the memory memory region the node will generate

## [◆ ](#a1b743e1c6c735c87d4fbd2094819c573)LINKER\_DT\_REGIONS

| #define LINKER\_DT\_REGIONS | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[DT\_FOREACH\_STATUS\_OKAY](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)(\_DT\_COMPATIBLE, \_REGION\_DECLARE)

[DT\_FOREACH\_STATUS\_OKAY](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)

#define DT\_FOREACH\_STATUS\_OKAY(compat, fn)

Invokes fn for each status okay node of a compatible.

**Definition** devicetree.h:3359

Generate linker memory regions from the device tree nodes with compatible 'zephyr,memory-region'.

Note: for now we do not deal with MEMORY attributes since those are optional, not actually used by Zephyr and they will likely conflict with the MPU configuration.

## [◆ ](#a171f1425c840f60dd94722ff046e0e81)LINKER\_DT\_SECTIONS

| #define LINKER\_DT\_SECTIONS | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[DT\_FOREACH\_STATUS\_OKAY](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)(\_DT\_COMPATIBLE, \_SECTION\_DECLARE)

Generate linker memory sections from the device tree nodes with compatible 'zephyr,memory-region'.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [linker](dir_5526e36ffa03ff8f2351c0fa0b79158f.md)
- [devicetree\_regions.h](devicetree__regions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
