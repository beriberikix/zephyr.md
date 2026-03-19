---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__devicetree-reg-prop.html
original_path: doxygen/html/group__devicetree-reg-prop.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| #define | [DT\_REG\_HAS\_NAME](#ga2c68672c60d95725b69371c3ab306d24)(node\_id, name) |
|  | Is `name` a valid register block name? |
| #define | [DT\_REG\_ADDR\_BY\_IDX\_RAW](#ga226e23a6bb94beee690ff6e1cdfbab91)(node\_id, idx) |
|  | Get the base raw address of the register block at index `idx`. |
| #define | [DT\_REG\_ADDR\_RAW](#ga14ebfb75548e45279f3954a75a5f9ac1)(node\_id) |
|  | Get a node's (only) register block raw address. |
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
| #define | [DT\_REG\_ADDR\_BY\_NAME\_OR](#ga3f0a35f6b07da983be6fa63bdfb82732)(node\_id, name, default\_value) |
|  | Like [DT\_REG\_ADDR\_BY\_NAME()](#gaeb5863e878bbd3a362e17616403da692), but with a fallback to `default_value`. |
| #define | [DT\_REG\_ADDR\_BY\_NAME\_U64](#gaf03f1b5518ff146d6de986f867fcc2c8)(node\_id, name) |
|  | 64-bit version of [DT\_REG\_ADDR\_BY\_NAME()](#gaeb5863e878bbd3a362e17616403da692) |
| #define | [DT\_REG\_SIZE\_BY\_NAME](#ga042988feb27e58989baa7abb4930409e)(node\_id, name) |
|  | Get a register block's size by name. |
| #define | [DT\_REG\_SIZE\_BY\_NAME\_OR](#ga823daf216d17b80f4d049c75358078ed)(node\_id, name, default\_value) |
|  | Like [DT\_REG\_SIZE\_BY\_NAME()](#ga042988feb27e58989baa7abb4930409e), but with a fallback to `default_value`. |

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

**Definition** devicetree.h:2409

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

DT\_U32\_C([DT\_REG\_ADDR\_BY\_IDX\_RAW](#ga226e23a6bb94beee690ff6e1cdfbab91)(node\_id, idx))

[DT\_REG\_ADDR\_BY\_IDX\_RAW](#ga226e23a6bb94beee690ff6e1cdfbab91)

#define DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, idx)

Get the base raw address of the register block at index idx.

**Definition** devicetree.h:2386

Get the base address of the register block at index `idx`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the register whose address to return |

Returns
:   address of the idx-th register block

## [◆ ](#ga226e23a6bb94beee690ff6e1cdfbab91)DT\_REG\_ADDR\_BY\_IDX\_RAW

| #define DT\_REG\_ADDR\_BY\_IDX\_RAW | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_ADDRESS)

Get the base raw address of the register block at index `idx`.

Get the base address of the register block at index `idx` without any type suffix. This can be used to index other devicetree properties, use the non \_RAW macros for assigning values in actual code.

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

DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS))

Get a register block's base address by name.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   address of the register block specified by name

## [◆ ](#ga3f0a35f6b07da983be6fa63bdfb82732)DT\_REG\_ADDR\_BY\_NAME\_OR

| #define DT\_REG\_ADDR\_BY\_NAME\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_REG\_HAS\_NAME](#ga2c68672c60d95725b69371c3ab306d24)(node\_id, name), \

([DT\_REG\_ADDR\_BY\_NAME](#gaeb5863e878bbd3a362e17616403da692)(node\_id, name)), (default\_value))

[DT\_REG\_HAS\_NAME](#ga2c68672c60d95725b69371c3ab306d24)

#define DT\_REG\_HAS\_NAME(node\_id, name)

Is name a valid register block name?

**Definition** devicetree.h:2372

[DT\_REG\_ADDR\_BY\_NAME](#gaeb5863e878bbd3a362e17616403da692)

#define DT\_REG\_ADDR\_BY\_NAME(node\_id, name)

Get a register block's base address by name.

**Definition** devicetree.h:2462

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

Like [DT\_REG\_ADDR\_BY\_NAME()](#gaeb5863e878bbd3a362e17616403da692), but with a fallback to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |
    | default\_value | a fallback value to expand to |

Returns
:   address of the register block specified by name if present, `default_value` otherwise

## [◆ ](#gaf03f1b5518ff146d6de986f867fcc2c8)DT\_REG\_ADDR\_BY\_NAME\_U64

| #define DT\_REG\_ADDR\_BY\_NAME\_U64 | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_U64\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_ADDRESS))

64-bit version of [DT\_REG\_ADDR\_BY\_NAME()](#gaeb5863e878bbd3a362e17616403da692)

This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_REG\_ADDR\_BY\_NAME()](#gaeb5863e878bbd3a362e17616403da692) in linker/ASM context.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   address of the register block specified by name

## [◆ ](#ga14ebfb75548e45279f3954a75a5f9ac1)DT\_REG\_ADDR\_RAW

| #define DT\_REG\_ADDR\_RAW | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_ADDR\_BY\_IDX\_RAW](#ga226e23a6bb94beee690ff6e1cdfbab91)(node\_id, 0)

Get a node's (only) register block raw address.

Get a node's only register block address without any type suffix. This can be used to index other devicetree properties, use the non \_RAW macros for assigning values in actual code.

Equivalent to [DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, 0)](#ga226e23a6bb94beee690ff6e1cdfbab91).

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   node's register block address

## [◆ ](#gaf77354db552821a865b93f709b25e410)DT\_REG\_ADDR\_U64

| #define DT\_REG\_ADDR\_U64 | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_U64\_C([DT\_REG\_ADDR\_BY\_IDX\_RAW](#ga226e23a6bb94beee690ff6e1cdfbab91)(node\_id, 0))

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

**Definition** util\_macro.h:140

Is `idx` a valid register block index?

If this returns 1, then [DT\_REG\_ADDR\_BY\_IDX(node\_id, idx)](#gac540b00bb12d0662f6aefe6ac0cff243) or [DT\_REG\_SIZE\_BY\_IDX(node\_id, idx)](#ga9a703d688e4b983689b8579e0e7d9f48) are valid. If it returns 0, it is an error to use those macros with index `idx`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index to check |

Returns
:   1 if `idx` is a valid register block index, 0 otherwise.

## [◆ ](#ga2c68672c60d95725b69371c3ab306d24)DT\_REG\_HAS\_NAME

| #define DT\_REG\_HAS\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_EXISTS))

Is `name` a valid register block name?

If this returns 1, then [DT\_REG\_ADDR\_BY\_NAME(node\_id, name)](#gaeb5863e878bbd3a362e17616403da692) or [DT\_REG\_SIZE\_BY\_NAME(node\_id, name)](#ga042988feb27e58989baa7abb4930409e) are valid. If it returns 0, it is an error to use those macros with name `name`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | name to check |

Returns
:   1 if `name` is a valid register block name, 0 otherwise.

## [◆ ](#gad223efc6c77d008e55c3588953e85bfb)DT\_REG\_SIZE

| #define DT\_REG\_SIZE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_SIZE\_BY\_IDX](#ga9a703d688e4b983689b8579e0e7d9f48)(node\_id, 0)

[DT\_REG\_SIZE\_BY\_IDX](#ga9a703d688e4b983689b8579e0e7d9f48)

#define DT\_REG\_SIZE\_BY\_IDX(node\_id, idx)

Get the size of the register block at index idx.

**Definition** devicetree.h:2423

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

DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_IDX\_, idx, \_VAL\_SIZE))

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

DT\_U32\_C(DT\_CAT4(node\_id, \_REG\_NAME\_, name, \_VAL\_SIZE))

Get a register block's size by name.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   size of the register block specified by name

## [◆ ](#ga823daf216d17b80f4d049c75358078ed)DT\_REG\_SIZE\_BY\_NAME\_OR

| #define DT\_REG\_SIZE\_BY\_NAME\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_REG\_HAS\_NAME](#ga2c68672c60d95725b69371c3ab306d24)(node\_id, name), \

([DT\_REG\_SIZE\_BY\_NAME](#ga042988feb27e58989baa7abb4930409e)(node\_id, name)), (default\_value))

[DT\_REG\_SIZE\_BY\_NAME](#ga042988feb27e58989baa7abb4930409e)

#define DT\_REG\_SIZE\_BY\_NAME(node\_id, name)

Get a register block's size by name.

**Definition** devicetree.h:2498

Like [DT\_REG\_SIZE\_BY\_NAME()](#ga042988feb27e58989baa7abb4930409e), but with a fallback to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |
    | default\_value | a fallback value to expand to |

Returns
:   size of the register block specified by name if present, `default_value` otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
