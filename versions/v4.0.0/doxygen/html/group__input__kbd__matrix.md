---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__input__kbd__matrix.html
original_path: doxygen/html/group__input__kbd__matrix.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Keyboard Matrix API

[Device Driver APIs](group__io__interfaces.md)

Keyboard Matrix API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md) |
|  | Keyboard matrix internal APIs. [More...](structinput__kbd__matrix__api.md#details) |
| struct | [input\_kbd\_matrix\_common\_config](structinput__kbd__matrix__common__config.md) |
|  | Common keyboard matrix config. [More...](structinput__kbd__matrix__common__config.md#details) |
| struct | [input\_kbd\_matrix\_common\_data](structinput__kbd__matrix__common__data.md) |
|  | Common keyboard matrix data. [More...](structinput__kbd__matrix__common__data.md#details) |

| Macros | |
| --- | --- |
| #define | [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE](#ga2f35f23d426f93f71057a31f612a88de)   -1 |
|  | Special drive\_column argument for not driving any column. |
| #define | [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL](#ga6d27ba5612c09d80087e854b21fb9e65)   -2 |
|  | Special drive\_column argument for driving all the columns. |
| #define | [INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES](#ga80a384d2041dcee27d7940a1e408d82a)   30U |
|  | Number of tracked scan cycles. |
| #define | [PRIkbdrow](#ga1343b97a8b072f8ed362e8a4f242bdd1)   "02" [PRIx8](inttypes_8h.md#adac1acc1d24060aeee7791a99d1a3a8c) |
| #define | [INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST](#gaec0209680e18da8584bdf41e5229aaae) |
| #define | [INPUT\_KBD\_MATRIX\_ROW\_BITS](#gae395cd03c295673dc9563c252ba7e022)   [NUM\_BITS](sys_2util_8h.md#afa27c06d0ad6b949289431ad75f104ab)([kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86)) |
|  | Maximum number of rows. |
| #define | [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, name) |
| #define | [INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL](#gac1a4389b1afeab9c48a15c024bfb0cac)(node\_id, \_row\_size, \_col\_size) |
|  | Defines the common keyboard matrix support data from devicetree, specify row and col count. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_DEFINE](#ga512bea2ca97569f465074ca8f231a0a3)(node\_id) |
|  | Defines the common keyboard matrix support data from devicetree. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE\_ROW\_COL](#ga1d3fe52f10c75dc4c32c8583c05fb2a2)(inst, row\_size, col\_size) |
|  | Defines the common keyboard matrix support data from devicetree instance, specify row and col count. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE](#gab3ea5b7d597574b32ced16604648a6d2)(inst) |
|  | Defines the common keyboard matrix support data from devicetree instance. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL](#ga5ad9141616b4a63068bfbe8004bba67d)(node\_id, \_api, \_row\_size, \_col\_size) |
|  | Initialize common keyboard matrix config from devicetree, specify row and col count. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT](#ga3281b4e5909a1c07d8190092bc31cb12)(node\_id, api) |
|  | Initialize common keyboard matrix config from devicetree. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT\_ROW\_COL](#gac6baf9b284f0796cdd5dbcef338f9588)(inst, api, row\_size, col\_size) |
|  | Initialize common keyboard matrix config from devicetree instance, specify row and col count. |
| #define | [INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT](#gab19b4a8c66c5540b4e690459655f92fd)(inst, api) |
|  | Initialize common keyboard matrix config from devicetree instance. |
| #define | [INPUT\_KBD\_STRUCT\_CHECK](#ga352d484344c93c30f5cad75551793377)(config, data) |
|  | Validate the offset of the common data structures. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86) |
|  | Row entry data type. |

| Functions | |
| --- | --- |
| int | [input\_kbd\_matrix\_actual\_key\_mask\_set](#gab35f4bf523760933294242ccc8226490) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) row, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) col, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Enables or disables a specific row, column combination in the actual key mask. |
| void | [input\_kbd\_matrix\_poll\_start](#gaf97b6ff410631f111d7c3a7aa7f64171) (const struct [device](structdevice.md) \*dev) |
|  | Start scanning the keyboard matrix. |
| void | [input\_kbd\_matrix\_drive\_column\_hook](#ga6d843c7213bf5c0af9003c165a5f3e03) (const struct [device](structdevice.md) \*dev, int col) |
|  | Drive column hook. |
| int | [input\_kbd\_matrix\_common\_init](#ga938dc38da7e81e5a68b8b9dc585c4bab) (const struct [device](structdevice.md) \*dev) |
|  | Common function to initialize a keyboard matrix device at init time. |

## Detailed Description

Keyboard Matrix API.

## Macro Definition Documentation

## [◆ ](#gaec0209680e18da8584bdf41e5229aaae)INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST

| #define INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST |
| --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

## [◆ ](#ga6d27ba5612c09d80087e854b21fb9e65)INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL

| #define INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL   -2 |
| --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Special drive\_column argument for driving all the columns.

## [◆ ](#ga2f35f23d426f93f71057a31f612a88de)INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE

| #define INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE   -1 |
| --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Special drive\_column argument for not driving any column.

## [◆ ](#gac7cc0314fa201b1efbcac37cf5f90576)INPUT\_KBD\_MATRIX\_DATA\_NAME

| #define INPUT\_KBD\_MATRIX\_DATA\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

\_CONCAT(\_\_input\_kbd\_matrix\_, \

\_CONCAT(name, [DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)(node\_id)))

[DEVICE\_DT\_NAME\_GET](group__device__model.md#ga8ebbf17ef805817aa638f36f177a1a0e)

#define DEVICE\_DT\_NAME\_GET(node\_id)

The name of the global device object for node\_id.

**Definition** device.h:238

## [◆ ](#ga3281b4e5909a1c07d8190092bc31cb12)INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT

| #define INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *api* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

[INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL](#ga5ad9141616b4a63068bfbe8004bba67d)( \

node\_id, api, [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, row\_size), [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, col\_size))

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:745

[INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL](#ga5ad9141616b4a63068bfbe8004bba67d)

#define INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL(node\_id, \_api, \_row\_size, \_col\_size)

Initialize common keyboard matrix config from devicetree, specify row and col count.

**Definition** input\_kbd\_matrix.h:189

Initialize common keyboard matrix config from devicetree.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | api | Pointer to a [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md "input_kbd_matrix_api") structure. |

## [◆ ](#ga5ad9141616b4a63068bfbe8004bba67d)INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL

| #define INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_api*, |
|  |  |  | *\_row\_size*, |
|  |  |  | *\_col\_size* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

{ \

.api = \_api, \

.row\_size = \_row\_size, \

.col\_size = \_col\_size, \

.poll\_period\_us = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, poll\_period\_ms) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27), \

.poll\_timeout\_ms = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, poll\_timeout\_ms), \

.debounce\_down\_us = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, debounce\_down\_ms) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27), \

.debounce\_up\_us = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, debounce\_up\_ms) \* [USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27), \

.settle\_time\_us = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, settle\_time\_us), \

.ghostkey\_check = ![DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, no\_ghostkey\_check), \

IF\_ENABLED([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, actual\_key\_mask), ( \

.actual\_key\_mask = [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, actual\_key\_mask), \

)) \

\

.matrix\_stable\_state = [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, stable\_state), \

.matrix\_unstable\_state = [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, unstable\_state), \

.matrix\_previous\_state = [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, previous\_state), \

.matrix\_new\_state = [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, new\_state), \

.scan\_cycle\_idx = [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, scan\_cycle\_idx), \

}

[USEC\_PER\_MSEC](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)

#define USEC\_PER\_MSEC

number of microseconds per millisecond

**Definition** sys\_clock.h:89

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3677

[INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)

#define INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, name)

**Definition** input\_kbd\_matrix.h:131

Initialize common keyboard matrix config from devicetree, specify row and col count.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | \_api | Pointer to a [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md "input_kbd_matrix_api") structure. |
    | \_row\_size | The matrix row count. |
    | \_col\_size | The matrix column count. |

## [◆ ](#ga512bea2ca97569f465074ca8f231a0a3)INPUT\_KBD\_MATRIX\_DT\_DEFINE

| #define INPUT\_KBD\_MATRIX\_DT\_DEFINE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

[INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL](#gac1a4389b1afeab9c48a15c024bfb0cac)( \

node\_id, [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, row\_size), [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, col\_size))

[INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL](#gac1a4389b1afeab9c48a15c024bfb0cac)

#define INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL(node\_id, \_row\_size, \_col\_size)

Defines the common keyboard matrix support data from devicetree, specify row and col count.

**Definition** input\_kbd\_matrix.h:139

Defines the common keyboard matrix support data from devicetree.

## [◆ ](#gac1a4389b1afeab9c48a15c024bfb0cac)INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL

| #define INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_row\_size*, |
|  |  |  | *\_col\_size* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)(\_row\_size, 1, [INPUT\_KBD\_MATRIX\_ROW\_BITS](#gae395cd03c295673dc9563c252ba7e022)), "invalid row-size"); \

BUILD\_ASSERT([IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)(\_col\_size, 1, [UINT8\_MAX](stdint_8h.md#aeb4e270a084ee26fe73e799861bd0252)), "invalid col-size"); \

IF\_ENABLED([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, actual\_key\_mask), ( \

BUILD\_ASSERT([DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)(node\_id, actual\_key\_mask) == \_col\_size, \

"actual-key-mask size does not match the number of columns"); \

static [INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST](#gaec0209680e18da8584bdf41e5229aaae) kbd\_row\_t \

INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, actual\_key\_mask)[\_col\_size] = \

DT\_PROP(node\_id, actual\_key\_mask); \

)) \

static [kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86) [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, stable\_state)[\_col\_size]; \

static [kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86) [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, unstable\_state)[\_col\_size]; \

static [kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86) [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, previous\_state)[\_col\_size]; \

static [kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86) [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, new\_state)[\_col\_size]; \

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [INPUT\_KBD\_MATRIX\_DATA\_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)(node\_id, scan\_cycle\_idx)[\_row\_size \* \_col\_size];

[DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)

#define DT\_PROP\_LEN(node\_id, prop)

Get a property's logical length.

**Definition** devicetree.h:779

[kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86)

uint8\_t kbd\_row\_t

Row entry data type.

**Definition** input\_kbd\_matrix.h:39

[INPUT\_KBD\_MATRIX\_ROW\_BITS](#gae395cd03c295673dc9563c252ba7e022)

#define INPUT\_KBD\_MATRIX\_ROW\_BITS

Maximum number of rows.

**Definition** input\_kbd\_matrix.h:70

[INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST](#gaec0209680e18da8584bdf41e5229aaae)

#define INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST

**Definition** input\_kbd\_matrix.h:44

[IN\_RANGE](group__sys-util.md#gaea00fb0c11b73f77da8884374e2121b4)

#define IN\_RANGE(val, min, max)

Checks if a value is within range.

**Definition** util.h:431

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[UINT8\_MAX](stdint_8h.md#aeb4e270a084ee26fe73e799861bd0252)

#define UINT8\_MAX

**Definition** stdint.h:27

Defines the common keyboard matrix support data from devicetree, specify row and col count.

## [◆ ](#gab19b4a8c66c5540b4e690459655f92fd)INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT

| #define INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *api* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

[INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT](#ga3281b4e5909a1c07d8190092bc31cb12)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), api)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

[INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT](#ga3281b4e5909a1c07d8190092bc31cb12)

#define INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT(node\_id, api)

Initialize common keyboard matrix config from devicetree.

**Definition** input\_kbd\_matrix.h:217

Initialize common keyboard matrix config from devicetree instance.

Parameters
:   | inst | Instance. |
    | --- | --- |
    | api | Pointer to a [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md "input_kbd_matrix_api") structure. |

## [◆ ](#gac6baf9b284f0796cdd5dbcef338f9588)INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT\_ROW\_COL

| #define INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT\_ROW\_COL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *api*, |
|  |  |  | *row\_size*, |
|  |  |  | *col\_size* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

[INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL](#ga5ad9141616b4a63068bfbe8004bba67d)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), api, row\_size, col\_size)

Initialize common keyboard matrix config from devicetree instance, specify row and col count.

Parameters
:   | inst | Instance. |
    | --- | --- |
    | api | Pointer to a [input\_kbd\_matrix\_api](structinput__kbd__matrix__api.md "input_kbd_matrix_api") structure. |
    | row\_size | The matrix row count. |
    | col\_size | The matrix column count. |

## [◆ ](#gab3ea5b7d597574b32ced16604648a6d2)INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE

| #define INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

[INPUT\_KBD\_MATRIX\_DT\_DEFINE](#ga512bea2ca97569f465074ca8f231a0a3)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[INPUT\_KBD\_MATRIX\_DT\_DEFINE](#ga512bea2ca97569f465074ca8f231a0a3)

#define INPUT\_KBD\_MATRIX\_DT\_DEFINE(node\_id)

Defines the common keyboard matrix support data from devicetree.

**Definition** input\_kbd\_matrix.h:158

Defines the common keyboard matrix support data from devicetree instance.

Parameters
:   | inst | Instance. |
    | --- | --- |

## [◆ ](#ga1d3fe52f10c75dc4c32c8583c05fb2a2)INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE\_ROW\_COL

| #define INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE\_ROW\_COL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *row\_size*, |
|  |  |  | *col\_size* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

[INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL](#gac1a4389b1afeab9c48a15c024bfb0cac)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), row\_size, col\_size)

Defines the common keyboard matrix support data from devicetree instance, specify row and col count.

Parameters
:   | inst | Instance. |
    | --- | --- |
    | row\_size | The matrix row count. |
    | col\_size | The matrix column count. |

## [◆ ](#gae395cd03c295673dc9563c252ba7e022)INPUT\_KBD\_MATRIX\_ROW\_BITS

| #define INPUT\_KBD\_MATRIX\_ROW\_BITS   [NUM\_BITS](sys_2util_8h.md#afa27c06d0ad6b949289431ad75f104ab)([kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86)) |
| --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Maximum number of rows.

## [◆ ](#ga80a384d2041dcee27d7940a1e408d82a)INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES

| #define INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES   30U |
| --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Number of tracked scan cycles.

## [◆ ](#ga352d484344c93c30f5cad75551793377)INPUT\_KBD\_STRUCT\_CHECK

| #define INPUT\_KBD\_STRUCT\_CHECK | ( |  | *config*, |
| --- | --- | --- | --- |
|  |  |  | *data* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

**Value:**

BUILD\_ASSERT(offsetof(config, common) == 0, \

"struct input\_kbd\_matrix\_common\_config must be placed first"); \

BUILD\_ASSERT(offsetof(data, common) == 0, \

"struct input\_kbd\_matrix\_common\_data must be placed first")

Validate the offset of the common data structures.

Parameters
:   | config | Name of the config structure. |
    | --- | --- |
    | data | Name of the data structure. |

## [◆ ](#ga1343b97a8b072f8ed362e8a4f242bdd1)PRIkbdrow

| #define PRIkbdrow   "02" [PRIx8](inttypes_8h.md#adac1acc1d24060aeee7791a99d1a3a8c) |
| --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

## Typedef Documentation

## [◆ ](#gac7d5c811da0c9ab2660be3c3f2fcfe86)kbd\_row\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [kbd\_row\_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86) |
| --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Row entry data type.

## Function Documentation

## [◆ ](#gab35f4bf523760933294242ccc8226490)input\_kbd\_matrix\_actual\_key\_mask\_set()

| int input\_kbd\_matrix\_actual\_key\_mask\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *row*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *col*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enabled* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Enables or disables a specific row, column combination in the actual key mask.

This allows enabling or disabling specific row, column combination in the actual key mask in runtime. It can be useful if some of the keys are not present in some configuration, and the specific configuration is determined in runtime. Requires

```
CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC
```

to be enabled.

Parameters
:   | dev | Pointer to the keyboard matrix device. |
    | --- | --- |
    | row | The matrix row to enable or disable. |
    | col | The matrix column to enable or disable. |
    | enabled | Whether the specified row, col has to be enabled or disabled. |

Return values
:   | 0 | If the change is successful. |
    | --- | --- |
    | -errno | Negative errno if row or col are out of range for the device. |

## [◆ ](#ga938dc38da7e81e5a68b8b9dc585c4bab)input\_kbd\_matrix\_common\_init()

| int input\_kbd\_matrix\_common\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Common function to initialize a keyboard matrix device at init time.

This function must be called at the end of the device init function.

Parameters
:   | dev | Keyboard matrix device instance. |
    | --- | --- |

Return values
:   | 0 | If initialized successfully. |
    | --- | --- |
    | -errno | Negative errno in case of failure. |

## [◆ ](#ga6d843c7213bf5c0af9003c165a5f3e03)input\_kbd\_matrix\_drive\_column\_hook()

| void input\_kbd\_matrix\_drive\_column\_hook | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *col* ) |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Drive column hook.

This can be implemented by the application to handle column selection quirks. Called after the driver specific drive\_column function. Requires

```
CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK
```

to be enabled.

Parameters
:   | dev | Keyboard matrix device instance. |
    | --- | --- |
    | col | The column to drive, or [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE](#ga2f35f23d426f93f71057a31f612a88de) or [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL](#ga6d27ba5612c09d80087e854b21fb9e65). |

## [◆ ](#gaf97b6ff410631f111d7c3a7aa7f64171)input\_kbd\_matrix\_poll\_start()

| void input\_kbd\_matrix\_poll\_start | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[input_kbd_matrix.h](input__kbd__matrix_8h.md)>`

Start scanning the keyboard matrix.

Starts the keyboard matrix scanning cycle, this should be called in reaction of a press event, after the device has been put in detect mode.

Parameters
:   | dev | Keyboard matrix device instance. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
