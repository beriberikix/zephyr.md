---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__devicetree-reg-prop.html
original_path: doxygen/html/group__devicetree-reg-prop.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reg property

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_NUM\_REGS](#ga6cdd22b6a2881b09ed63d9d262566a0a)(node\_id) |
|  | Get the number of register blocks in the reg property. |
| #define | [DT\_REG\_HAS\_IDX](#ga59aa43231678d08eeac6e5b344048f02)(node\_id, idx) |
|  | Is `idx` a valid register block index? |
| #define | [DT\_REG\_ADDR\_BY\_IDX](#gac540b00bb12d0662f6aefe6ac0cff243)(node\_id, idx) |
|  | Get the base address of the register block at index `idx`. |
| #define | [DT\_REG\_SIZE\_BY\_IDX](#ga9a703d688e4b983689b8579e0e7d9f48)(node\_id, idx) |
|  | Get the size of the register block at index `idx`. |
| #define | [DT\_REG\_ADDR](#gac6d8279c32351ced4c0ac7f32270974e)(node\_id) |
|  | Get a node's (only) register block address. |
| #define | [DT\_REG\_ADDR\_U64](#gaf77354db552821a865b93f709b25e410)(node\_id) |
|  | 64-bit version of [DT\_REG\_ADDR()](#gac6d8279c32351ced4c0ac7f32270974e) |
| #define | [DT\_REG\_SIZE](#gad223efc6c77d008e55c3588953e85bfb)(node\_id) |
|  | Get a node's (only) register block size. |
| #define | [DT\_REG\_ADDR\_BY\_NAME](#gaeb5863e878bbd3a362e17616403da692)(node\_id, name) |
|  | Get a register block's base address by name. |
| #define | [DT\_REG\_ADDR\_BY\_NAME\_U64](#gaf03f1b5518ff146d6de986f867fcc2c8)(node\_id, name) |
|  | 64-bit version of [DT\_REG\_ADDR\_BY\_NAME()](#gaeb5863e878bbd3a362e17616403da692) |
| #define | [DT\_REG\_SIZE\_BY\_NAME](#ga042988feb27e58989baa7abb4930409e)(node\_id, name) |
|  | Get a register block's size by name. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga6cdd22b6a2881b09ed63d9d262566a0a)DT\_NUM\_REGS

| #define DT\_NUM\_REGS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_REG\_NUM)

Get the number of register blocks in the reg property.

Use this instead of [DT\_PROP\_LEN(node\_id, reg)](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6 "Get a property's logical length.").

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   Number of register blocks in the node's "reg" property.

## [◆ ](#gac6d8279c32351ced4c0ac7f32270974e)DT\_REG\_ADDR

| #define DT\_REG\_ADDR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_ADDR\_BY\_IDX](#gac540b00bb12d0662f6aefe6ac0cff243)(node\_id, 0)

[DT\_REG\_ADDR\_BY\_IDX](#gac540b00bb12d0662f6aefe6ac0cff243)

#define DT\_REG\_ADDR\_BY\_IDX(node\_id, idx)

Get the base address of the register block at index idx.

**Definition** devicetree.h:2190

Get a node's (only) register block address.

Equivalent to [DT\_REG\_ADDR\_BY\_IDX(node\_id, 0)](#gac540b00bb12d0662f6aefe6ac0cff243).

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   node's register block address

## [◆ ](#gac540b00bb12d0662f6aefe6ac0cff243)DT\_REG\_ADDR\_BY\_IDX

| #define DT\_REG\_ADDR\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_ADDRESS)

Get the base address of the register block at index `idx`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the register whose address to return |

Returns
:   address of the idx-th register block

## [◆ ](#gaeb5863e878bbd3a362e17616403da692)DT\_REG\_ADDR\_BY\_NAME

| #define DT\_REG\_ADDR\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS)

Get a register block's base address by name.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   address of the register block specified by name

## [◆ ](#gaf03f1b5518ff146d6de986f867fcc2c8)DT\_REG\_ADDR\_BY\_NAME\_U64

| #define DT\_REG\_ADDR\_BY\_NAME\_U64 | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_U64\_C([DT\_REG\_ADDR\_BY\_NAME](#gaeb5863e878bbd3a362e17616403da692)(node\_id, name))

[DT\_REG\_ADDR\_BY\_NAME](#gaeb5863e878bbd3a362e17616403da692)

#define DT\_REG\_ADDR\_BY\_NAME(node\_id, name)

Get a register block's base address by name.

**Definition** devicetree.h:2243

64-bit version of [DT\_REG\_ADDR\_BY\_NAME()](#gaeb5863e878bbd3a362e17616403da692)

This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_REG\_ADDR\_BY\_NAME()](#gaeb5863e878bbd3a362e17616403da692) in linker/ASM context.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   address of the register block specified by name

## [◆ ](#gaf77354db552821a865b93f709b25e410)DT\_REG\_ADDR\_U64

| #define DT\_REG\_ADDR\_U64 | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_U64\_C([DT\_REG\_ADDR](#gac6d8279c32351ced4c0ac7f32270974e)(node\_id))

[DT\_REG\_ADDR](#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2214

64-bit version of [DT\_REG\_ADDR()](#gac6d8279c32351ced4c0ac7f32270974e)

This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_REG\_ADDR()](#gac6d8279c32351ced4c0ac7f32270974e) in linker/ASM context.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   node's register block address

## [◆ ](#ga59aa43231678d08eeac6e5b344048f02)DT\_REG\_HAS\_IDX

| #define DT\_REG\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Is `idx` a valid register block index?

If this returns 1, then [DT\_REG\_ADDR\_BY\_IDX(node\_id, idx)](#gac540b00bb12d0662f6aefe6ac0cff243) or [DT\_REG\_SIZE\_BY\_IDX(node\_id, idx)](#ga9a703d688e4b983689b8579e0e7d9f48) are valid. If it returns 0, it is an error to use those macros with index `idx`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index to check |

Returns
:   1 if `idx` is a valid register block index, 0 otherwise.

## [◆ ](#gad223efc6c77d008e55c3588953e85bfb)DT\_REG\_SIZE

| #define DT\_REG\_SIZE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_SIZE\_BY\_IDX](#ga9a703d688e4b983689b8579e0e7d9f48)(node\_id, 0)

[DT\_REG\_SIZE\_BY\_IDX](#ga9a703d688e4b983689b8579e0e7d9f48)

#define DT\_REG\_SIZE\_BY\_IDX(node\_id, idx)

Get the size of the register block at index idx.

**Definition** devicetree.h:2204

Get a node's (only) register block size.

Equivalent to [DT\_REG\_SIZE\_BY\_IDX(node\_id, 0)](#ga9a703d688e4b983689b8579e0e7d9f48).

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   node's only register block's size

## [◆ ](#ga9a703d688e4b983689b8579e0e7d9f48)DT\_REG\_SIZE\_BY\_IDX

| #define DT\_REG\_SIZE\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_SIZE)

Get the size of the register block at index `idx`.

This is the size of an individual register block, not the total number of register blocks in the property; use [DT\_NUM\_REGS()](#ga6cdd22b6a2881b09ed63d9d262566a0a) for that.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the register whose size to return |

Returns
:   size of the idx-th register block

## [◆ ](#ga042988feb27e58989baa7abb4930409e)DT\_REG\_SIZE\_BY\_NAME

| #define DT\_REG\_SIZE\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_SIZE)

Get a register block's size by name.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   size of the register block specified by name

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
