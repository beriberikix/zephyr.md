---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__devicetree-pwms.html
original_path: doxygen/html/group__devicetree-pwms.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree PWMs API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_PWMS\_CTLR\_BY\_IDX](#ga2f16d00a53717a66668fb8bc967acce5)(node\_id, idx) |
|  | Get the node identifier for the PWM controller from a pwms property at an index. |
| #define | [DT\_PWMS\_CTLR\_BY\_NAME](#ga6922e69c707219cd766fe317484dac8a)(node\_id, name) |
|  | Get the node identifier for the PWM controller from a pwms property by name. |
| #define | [DT\_PWMS\_CTLR](#gaff7a0b201d97a1d1bb1893b556d5a194)(node\_id) |
|  | Equivalent to [DT\_PWMS\_CTLR\_BY\_IDX(node\_id, 0)](#ga2f16d00a53717a66668fb8bc967acce5). |
| #define | [DT\_PWMS\_CELL\_BY\_IDX](#ga0c1ab3329448f92936d57a83b5b3594e)(node\_id, idx, cell) |
|  | Get PWM specifier's cell value at an index. |
| #define | [DT\_PWMS\_CELL\_BY\_NAME](#ga69233198a489283068bc1ded5072ca26)(node\_id, name, cell) |
|  | Get a PWM specifier's cell value by name. |
| #define | [DT\_PWMS\_CELL](#ga2062b31a090c05ccd267ae1468b182ef)(node\_id, cell) |
|  | Equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, 0, cell)](#ga0c1ab3329448f92936d57a83b5b3594e). |
| #define | [DT\_PWMS\_CHANNEL\_BY\_IDX](#ga10a372e44c7e3feb551ca996c6ca5a8f)(node\_id, idx) |
|  | Get a PWM specifier's channel cell value at an index. |
| #define | [DT\_PWMS\_CHANNEL\_BY\_NAME](#ga59a4b9884e9620eac04c3808a3a6d164)(node\_id, name) |
|  | Get a PWM specifier's channel cell value by name. |
| #define | [DT\_PWMS\_CHANNEL](#gaeb0a10ad37fdfd3dcc75bd379908acdc)(node\_id) |
|  | Equivalent to [DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, 0)](#ga10a372e44c7e3feb551ca996c6ca5a8f). |
| #define | [DT\_PWMS\_PERIOD\_BY\_IDX](#ga9456f65777e6fc7c057c6e0709c9245f)(node\_id, idx) |
|  | Get PWM specifier's period cell value at an index. |
| #define | [DT\_PWMS\_PERIOD\_BY\_NAME](#ga74af83d31fc38f331808dedfaecf4c74)(node\_id, name) |
|  | Get a PWM specifier's period cell value by name. |
| #define | [DT\_PWMS\_PERIOD](#gac6006a723932325b96a1b50619be153b)(node\_id) |
|  | Equivalent to [DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, 0)](#ga9456f65777e6fc7c057c6e0709c9245f). |
| #define | [DT\_PWMS\_FLAGS\_BY\_IDX](#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)(node\_id, idx) |
|  | Get a PWM specifier's flags cell value at an index. |
| #define | [DT\_PWMS\_FLAGS\_BY\_NAME](#ga7a1621bfb223da23aa030b64fc0c0bcd)(node\_id, name) |
|  | Get a PWM specifier's flags cell value by name. |
| #define | [DT\_PWMS\_FLAGS](#ga8dcd2d18129504d1a4ab71ae05c48c44)(node\_id) |
|  | Equivalent to [DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, 0)](#gaf9c1ac7f3a39f4022f3ec31ef8de98e6). |
| #define | [DT\_INST\_PWMS\_CTLR\_BY\_IDX](#ga4f751ba5f3c1aad5d62178b166f36c24)(inst, idx) |
|  | Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance's pwms property at an index. |
| #define | [DT\_INST\_PWMS\_CTLR\_BY\_NAME](#gae66d3e710496bff9789996ddb72e1ebe)(inst, name) |
|  | Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance's pwms property by name. |
| #define | [DT\_INST\_PWMS\_CTLR](#ga2f79a0a48e08c89bac58d16d9731e683)(inst) |
|  | Equivalent to [DT\_INST\_PWMS\_CTLR\_BY\_IDX(inst, 0)](#ga4f751ba5f3c1aad5d62178b166f36c24). |
| #define | [DT\_INST\_PWMS\_CELL\_BY\_IDX](#gad106bf22d9dc90384519cd6ccc8fd1c6)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's PWM specifier's cell value at an index. |
| #define | [DT\_INST\_PWMS\_CELL\_BY\_NAME](#ga5731d949be09461f5da040e451cc509c)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's PWM specifier's cell value by name. |
| #define | [DT\_INST\_PWMS\_CELL](#ga199804a2d06c301f19c5c8de232ede15)(inst, cell) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, 0, cell)](#gad106bf22d9dc90384519cd6ccc8fd1c6). |
| #define | [DT\_INST\_PWMS\_CHANNEL\_BY\_IDX](#ga154ece84d782a7df2ce31b2a34f43870)(inst, idx) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, channel)](#gad106bf22d9dc90384519cd6ccc8fd1c6). |
| #define | [DT\_INST\_PWMS\_CHANNEL\_BY\_NAME](#ga60901952d81e29dbfbbe88ee3ffe3e17)(inst, name) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, channel)](#ga5731d949be09461f5da040e451cc509c). |
| #define | [DT\_INST\_PWMS\_CHANNEL](#gad871b89fd1b2d62aae84dc35a0819032)(inst) |
|  | Equivalent to [DT\_INST\_PWMS\_CHANNEL\_BY\_IDX(inst, 0)](#ga154ece84d782a7df2ce31b2a34f43870). |
| #define | [DT\_INST\_PWMS\_PERIOD\_BY\_IDX](#ga7e7408507ecdac75cb7c9ba2b9176ec8)(inst, idx) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, period)](#gad106bf22d9dc90384519cd6ccc8fd1c6). |
| #define | [DT\_INST\_PWMS\_PERIOD\_BY\_NAME](#ga7ac719270232e67f91bc65e3786be1a1)(inst, name) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, period)](#ga5731d949be09461f5da040e451cc509c). |
| #define | [DT\_INST\_PWMS\_PERIOD](#ga2b122199764cff41c04bad243f4456dc)(inst) |
|  | Equivalent to [DT\_INST\_PWMS\_PERIOD\_BY\_IDX(inst, 0)](#ga7e7408507ecdac75cb7c9ba2b9176ec8). |
| #define | [DT\_INST\_PWMS\_FLAGS\_BY\_IDX](#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)(inst, idx) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, flags)](#gad106bf22d9dc90384519cd6ccc8fd1c6). |
| #define | [DT\_INST\_PWMS\_FLAGS\_BY\_NAME](#ga23a8815368cbd82a8673e00abdfeab6b)(inst, name) |
|  | Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, flags)](#ga5731d949be09461f5da040e451cc509c). |
| #define | [DT\_INST\_PWMS\_FLAGS](#ga5ca45d33eae6b50012e8c052e3bd5df0)(inst) |
|  | Equivalent to [DT\_INST\_PWMS\_FLAGS\_BY\_IDX(inst, 0)](#ga9cfbc4e3c0ab9d419cfb7700a5b42ced). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga199804a2d06c301f19c5c8de232ede15)DT\_INST\_PWMS\_CELL

| #define DT\_INST\_PWMS\_CELL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CELL\_BY\_IDX](#gad106bf22d9dc90384519cd6ccc8fd1c6)(inst, 0, cell)

[DT\_INST\_PWMS\_CELL\_BY\_IDX](#gad106bf22d9dc90384519cd6ccc8fd1c6)

#define DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, cell)

Get a DT\_DRV\_COMPAT instance's PWM specifier's cell value at an index.

**Definition** pwms.h:363

Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, 0, cell)](#gad106bf22d9dc90384519cd6ccc8fd1c6).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index 0

## [◆ ](#gad106bf22d9dc90384519cd6ccc8fd1c6)DT\_INST\_PWMS\_CELL\_BY\_IDX

| #define DT\_INST\_PWMS\_CELL\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CELL\_BY\_IDX](#ga0c1ab3329448f92936d57a83b5b3594e)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx, cell)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

[DT\_PWMS\_CELL\_BY\_IDX](#ga0c1ab3329448f92936d57a83b5b3594e)

#define DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, cell)

Get PWM specifier's cell value at an index.

**Definition** pwms.h:135

Get a DT\_DRV\_COMPAT instance's PWM specifier's cell value at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into pwms property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index "idx"

## [◆ ](#ga5731d949be09461f5da040e451cc509c)DT\_INST\_PWMS\_CELL\_BY\_NAME

| #define DT\_INST\_PWMS\_CELL\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CELL\_BY\_NAME](#ga69233198a489283068bc1ded5072ca26)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, cell)

[DT\_PWMS\_CELL\_BY\_NAME](#ga69233198a489283068bc1ded5072ca26)

#define DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, cell)

Get a PWM specifier's cell value by name.

**Definition** pwms.h:182

Get a DT\_DRV\_COMPAT instance's PWM specifier's cell value by name.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value in the specifier at the named element

See also
:   [DT\_PWMS\_CELL\_BY\_NAME()](#ga69233198a489283068bc1ded5072ca26)

## [◆ ](#gad871b89fd1b2d62aae84dc35a0819032)DT\_INST\_PWMS\_CHANNEL

| #define DT\_INST\_PWMS\_CHANNEL | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CHANNEL\_BY\_IDX](#ga154ece84d782a7df2ce31b2a34f43870)(inst, 0)

[DT\_INST\_PWMS\_CHANNEL\_BY\_IDX](#ga154ece84d782a7df2ce31b2a34f43870)

#define DT\_INST\_PWMS\_CHANNEL\_BY\_IDX(inst, idx)

Equivalent to DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, channel).

**Definition** pwms.h:394

Equivalent to [DT\_INST\_PWMS\_CHANNEL\_BY\_IDX(inst, 0)](#ga154ece84d782a7df2ce31b2a34f43870).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the channel cell value at index 0

See also
:   [DT\_INST\_PWMS\_CHANNEL\_BY\_IDX()](#ga154ece84d782a7df2ce31b2a34f43870)

## [◆ ](#ga154ece84d782a7df2ce31b2a34f43870)DT\_INST\_PWMS\_CHANNEL\_BY\_IDX

| #define DT\_INST\_PWMS\_CHANNEL\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CELL\_BY\_IDX](#gad106bf22d9dc90384519cd6ccc8fd1c6)(inst, idx, channel)

Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, channel)](#gad106bf22d9dc90384519cd6ccc8fd1c6).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into pwms property |

Returns
:   the channel cell value at index "idx"

See also
:   [DT\_INST\_PWMS\_CELL\_BY\_IDX()](#gad106bf22d9dc90384519cd6ccc8fd1c6)

## [◆ ](#ga60901952d81e29dbfbbe88ee3ffe3e17)DT\_INST\_PWMS\_CHANNEL\_BY\_NAME

| #define DT\_INST\_PWMS\_CHANNEL\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CELL\_BY\_NAME](#ga5731d949be09461f5da040e451cc509c)(inst, name, channel)

[DT\_INST\_PWMS\_CELL\_BY\_NAME](#ga5731d949be09461f5da040e451cc509c)

#define DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, cell)

Get a DT\_DRV\_COMPAT instance's PWM specifier's cell value by name.

**Definition** pwms.h:375

Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, channel)](#ga5731d949be09461f5da040e451cc509c).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |

Returns
:   the channel cell value in the specifier at the named element

See also
:   [DT\_INST\_PWMS\_CELL\_BY\_NAME()](#ga5731d949be09461f5da040e451cc509c)

## [◆ ](#ga2f79a0a48e08c89bac58d16d9731e683)DT\_INST\_PWMS\_CTLR

| #define DT\_INST\_PWMS\_CTLR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CTLR\_BY\_IDX](#ga4f751ba5f3c1aad5d62178b166f36c24)(inst, 0)

[DT\_INST\_PWMS\_CTLR\_BY\_IDX](#ga4f751ba5f3c1aad5d62178b166f36c24)

#define DT\_INST\_PWMS\_CTLR\_BY\_IDX(inst, idx)

Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance's pwms property at an in...

**Definition** pwms.h:331

Equivalent to [DT\_INST\_PWMS\_CTLR\_BY\_IDX(inst, 0)](#ga4f751ba5f3c1aad5d62178b166f36c24).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the node identifier for the PWM controller at index 0 in the instance's "pwms" property

See also
:   [DT\_PWMS\_CTLR\_BY\_IDX()](#ga2f16d00a53717a66668fb8bc967acce5)

## [◆ ](#ga4f751ba5f3c1aad5d62178b166f36c24)DT\_INST\_PWMS\_CTLR\_BY\_IDX

| #define DT\_INST\_PWMS\_CTLR\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CTLR\_BY\_IDX](#ga2f16d00a53717a66668fb8bc967acce5)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_PWMS\_CTLR\_BY\_IDX](#ga2f16d00a53717a66668fb8bc967acce5)

#define DT\_PWMS\_CTLR\_BY\_IDX(node\_id, idx)

Get the node identifier for the PWM controller from a pwms property at an index.

**Definition** pwms.h:51

Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance's pwms property at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into pwms property |

Returns
:   the node identifier for the PWM controller referenced at index "idx"

See also
:   [DT\_PWMS\_CTLR\_BY\_IDX()](#ga2f16d00a53717a66668fb8bc967acce5)

## [◆ ](#gae66d3e710496bff9789996ddb72e1ebe)DT\_INST\_PWMS\_CTLR\_BY\_NAME

| #define DT\_INST\_PWMS\_CTLR\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CTLR\_BY\_NAME](#ga6922e69c707219cd766fe317484dac8a)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_PWMS\_CTLR\_BY\_NAME](#ga6922e69c707219cd766fe317484dac8a)

#define DT\_PWMS\_CTLR\_BY\_NAME(node\_id, name)

Get the node identifier for the PWM controller from a pwms property by name.

**Definition** pwms.h:81

Get the node identifier for the PWM controller from a DT\_DRV\_COMPAT instance's pwms property by name.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |

Returns
:   the node identifier for the PWM controller in the named element

See also
:   [DT\_PWMS\_CTLR\_BY\_NAME()](#ga6922e69c707219cd766fe317484dac8a)

## [◆ ](#ga5ca45d33eae6b50012e8c052e3bd5df0)DT\_INST\_PWMS\_FLAGS

| #define DT\_INST\_PWMS\_FLAGS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_FLAGS\_BY\_IDX](#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)(inst, 0)

[DT\_INST\_PWMS\_FLAGS\_BY\_IDX](#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)

#define DT\_INST\_PWMS\_FLAGS\_BY\_IDX(inst, idx)

Equivalent to DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, flags).

**Definition** pwms.h:452

Equivalent to [DT\_INST\_PWMS\_FLAGS\_BY\_IDX(inst, 0)](#ga9cfbc4e3c0ab9d419cfb7700a5b42ced).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the flags cell value at index 0, or zero if there is none

See also
:   [DT\_INST\_PWMS\_FLAGS\_BY\_IDX()](#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)

## [◆ ](#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)DT\_INST\_PWMS\_FLAGS\_BY\_IDX

| #define DT\_INST\_PWMS\_FLAGS\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CELL\_BY\_IDX](#gad106bf22d9dc90384519cd6ccc8fd1c6)(inst, idx, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, flags)](#gad106bf22d9dc90384519cd6ccc8fd1c6).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into pwms property |

Returns
:   the flags cell value at index "idx", or zero if there is none

See also
:   [DT\_INST\_PWMS\_CELL\_BY\_IDX()](#gad106bf22d9dc90384519cd6ccc8fd1c6)

## [◆ ](#ga23a8815368cbd82a8673e00abdfeab6b)DT\_INST\_PWMS\_FLAGS\_BY\_NAME

| #define DT\_INST\_PWMS\_FLAGS\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CELL\_BY\_NAME](#ga5731d949be09461f5da040e451cc509c)(inst, name, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, flags)](#ga5731d949be09461f5da040e451cc509c).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |

Returns
:   the flags cell value in the specifier at the named element, or zero if there is none

See also
:   [DT\_INST\_PWMS\_CELL\_BY\_NAME()](#ga5731d949be09461f5da040e451cc509c)

## [◆ ](#ga2b122199764cff41c04bad243f4456dc)DT\_INST\_PWMS\_PERIOD

| #define DT\_INST\_PWMS\_PERIOD | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_PERIOD\_BY\_IDX](#ga7e7408507ecdac75cb7c9ba2b9176ec8)(inst, 0)

[DT\_INST\_PWMS\_PERIOD\_BY\_IDX](#ga7e7408507ecdac75cb7c9ba2b9176ec8)

#define DT\_INST\_PWMS\_PERIOD\_BY\_IDX(inst, idx)

Equivalent to DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, period).

**Definition** pwms.h:423

Equivalent to [DT\_INST\_PWMS\_PERIOD\_BY\_IDX(inst, 0)](#ga7e7408507ecdac75cb7c9ba2b9176ec8).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the period cell value at index 0

See also
:   [DT\_INST\_PWMS\_PERIOD\_BY\_IDX()](#ga7e7408507ecdac75cb7c9ba2b9176ec8)

## [◆ ](#ga7e7408507ecdac75cb7c9ba2b9176ec8)DT\_INST\_PWMS\_PERIOD\_BY\_IDX

| #define DT\_INST\_PWMS\_PERIOD\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CELL\_BY\_IDX](#gad106bf22d9dc90384519cd6ccc8fd1c6)(inst, idx, period)

Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, period)](#gad106bf22d9dc90384519cd6ccc8fd1c6).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | idx | logical index into pwms property |

Returns
:   the period cell value at index "idx"

See also
:   [DT\_INST\_PWMS\_CELL\_BY\_IDX()](#gad106bf22d9dc90384519cd6ccc8fd1c6)

## [◆ ](#ga7ac719270232e67f91bc65e3786be1a1)DT\_INST\_PWMS\_PERIOD\_BY\_NAME

| #define DT\_INST\_PWMS\_PERIOD\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_INST\_PWMS\_CELL\_BY\_NAME](#ga5731d949be09461f5da040e451cc509c)(inst, name, period)

Equivalent to [DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, period)](#ga5731d949be09461f5da040e451cc509c).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |

Returns
:   the period cell value in the specifier at the named element

See also
:   [DT\_INST\_PWMS\_CELL\_BY\_NAME()](#ga5731d949be09461f5da040e451cc509c)

## [◆ ](#ga2062b31a090c05ccd267ae1468b182ef)DT\_PWMS\_CELL

| #define DT\_PWMS\_CELL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CELL\_BY\_IDX](#ga0c1ab3329448f92936d57a83b5b3594e)(node\_id, 0, cell)

Equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, 0, cell)](#ga0c1ab3329448f92936d57a83b5b3594e).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index 0

See also
:   [DT\_PWMS\_CELL\_BY\_IDX()](#ga0c1ab3329448f92936d57a83b5b3594e)

## [◆ ](#ga0c1ab3329448f92936d57a83b5b3594e)DT\_PWMS\_CELL\_BY\_IDX

| #define DT\_PWMS\_CELL\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, pwms, idx, cell)

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1536

Get PWM specifier's cell value at an index.

Example devicetree fragment:

```
pwm1: pwm-controller@... {
        compatible = "vnd,pwm";
        #pwm-cells = <2>;
};

pwm2: pwm-controller@... {
        compatible = "vnd,pwm";
        #pwm-cells = <2>;
};

n: node {
        pwms = <&pwm1 1 200000 PWM_POLARITY_NORMAL>,
               <&pwm2 3 100000 PWM_POLARITY_INVERTED>;
};
```

Bindings fragment for the "vnd,pwm" compatible:

```
pwm-cells:
  - channel
  - period
  - flags
```

Example usage:

```
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, channel) // 1
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, channel) // 3
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, period)  // 200000
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, period)  // 100000
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, flags)   // PWM_POLARITY_NORMAL
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, flags)   // PWM_POLARITY_INVERTED
```

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | idx | logical index into pwms property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value at index "idx"

See also
:   [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.")

## [◆ ](#ga69233198a489283068bc1ded5072ca26)DT\_PWMS\_CELL\_BY\_NAME

| #define DT\_PWMS\_CELL\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)(node\_id, pwms, name, cell)

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)

#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)

Get a value within a phandle-array specifier by name.

**Definition** devicetree.h:1631

Get a PWM specifier's cell value by name.

Example devicetree fragment:

```
pwm1: pwm-controller@... {
        compatible = "vnd,pwm";
        #pwm-cells = <2>;
};

pwm2: pwm-controller@... {
        compatible = "vnd,pwm";
        #pwm-cells = <2>;
};

n: node {
        pwms = <&pwm1 1 200000 PWM_POLARITY_NORMAL>,
               <&pwm2 3 100000 PWM_POLARITY_INVERTED>;
        pwm-names = "alpha", "beta";
};
```

Bindings fragment for the "vnd,pwm" compatible:

```
pwm-cells:
  - channel
  - period
  - flags
```

Example usage:

```
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, channel) // 1
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, channel)  // 3
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, period)  // 200000
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, period)   // 100000
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, flags)   // PWM_POLARITY_NORMAL
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, flags)    // PWM_POLARITY_INVERTED
```

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell value in the specifier at the named element

See also
:   [DT\_PHA\_BY\_NAME()](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26 "Get a value within a phandle-array specifier by name.")

## [◆ ](#gaeb0a10ad37fdfd3dcc75bd379908acdc)DT\_PWMS\_CHANNEL

| #define DT\_PWMS\_CHANNEL | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CHANNEL\_BY\_IDX](#ga10a372e44c7e3feb551ca996c6ca5a8f)(node\_id, 0)

[DT\_PWMS\_CHANNEL\_BY\_IDX](#ga10a372e44c7e3feb551ca996c6ca5a8f)

#define DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, idx)

Get a PWM specifier's channel cell value at an index.

**Definition** pwms.h:207

Equivalent to [DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, 0)](#ga10a372e44c7e3feb551ca996c6ca5a8f).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |

Returns
:   the channel cell value at index 0

See also
:   [DT\_PWMS\_CHANNEL\_BY\_IDX()](#ga10a372e44c7e3feb551ca996c6ca5a8f)

## [◆ ](#ga10a372e44c7e3feb551ca996c6ca5a8f)DT\_PWMS\_CHANNEL\_BY\_IDX

| #define DT\_PWMS\_CHANNEL\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CELL\_BY\_IDX](#ga0c1ab3329448f92936d57a83b5b3594e)(node\_id, idx, channel)

Get a PWM specifier's channel cell value at an index.

This macro only works for PWM specifiers with cells named "channel". Refer to the node's binding to check if necessary.

This is equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, channel)](#ga0c1ab3329448f92936d57a83b5b3594e).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | idx | logical index into pwms property |

Returns
:   the channel cell value at index "idx"

See also
:   [DT\_PWMS\_CELL\_BY\_IDX()](#ga0c1ab3329448f92936d57a83b5b3594e)

## [◆ ](#ga59a4b9884e9620eac04c3808a3a6d164)DT\_PWMS\_CHANNEL\_BY\_NAME

| #define DT\_PWMS\_CHANNEL\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CELL\_BY\_NAME](#ga69233198a489283068bc1ded5072ca26)(node\_id, name, channel)

Get a PWM specifier's channel cell value by name.

This macro only works for PWM specifiers with cells named "channel". Refer to the node's binding to check if necessary.

This is equivalent to [DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, channel)](#ga69233198a489283068bc1ded5072ca26).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |

Returns
:   the channel cell value in the specifier at the named element

See also
:   [DT\_PWMS\_CELL\_BY\_NAME()](#ga69233198a489283068bc1ded5072ca26)

## [◆ ](#gaff7a0b201d97a1d1bb1893b556d5a194)DT\_PWMS\_CTLR

| #define DT\_PWMS\_CTLR | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CTLR\_BY\_IDX](#ga2f16d00a53717a66668fb8bc967acce5)(node\_id, 0)

Equivalent to [DT\_PWMS\_CTLR\_BY\_IDX(node\_id, 0)](#ga2f16d00a53717a66668fb8bc967acce5).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |

Returns
:   the node identifier for the PWM controller at index 0 in the node's "pwms" property

See also
:   [DT\_PWMS\_CTLR\_BY\_IDX()](#ga2f16d00a53717a66668fb8bc967acce5)

## [◆ ](#ga2f16d00a53717a66668fb8bc967acce5)DT\_PWMS\_CTLR\_BY\_IDX

| #define DT\_PWMS\_CTLR\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, pwms, idx)

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1757

Get the node identifier for the PWM controller from a pwms property at an index.

Example devicetree fragment:

```
pwm1: pwm-controller@... { ... };

pwm2: pwm-controller@... { ... };

n: node {
        pwms = <&pwm1 1 PWM_POLARITY_NORMAL>,
               <&pwm2 3 PWM_POLARITY_INVERTED>;
};
```

Example usage:

```
DT_PWMS_CTLR_BY_IDX(DT_NODELABEL(n), 0) // DT_NODELABEL(pwm1)
DT_PWMS_CTLR_BY_IDX(DT_NODELABEL(n), 1) // DT_NODELABEL(pwm2)
```

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | idx | logical index into pwms property |

Returns
:   the node identifier for the PWM controller referenced at index "idx"

See also
:   [DT\_PROP\_BY\_PHANDLE\_IDX()](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d "Get a property value from a phandle in a property.")

## [◆ ](#ga6922e69c707219cd766fe317484dac8a)DT\_PWMS\_CTLR\_BY\_NAME

| #define DT\_PWMS\_CTLR\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, pwms, name)

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1705

Get the node identifier for the PWM controller from a pwms property by name.

Example devicetree fragment:

```
pwm1: pwm-controller@... { ... };
```

pwm2: pwm-controller... { ... };

n: node { pwms = <&pwm1 1 PWM\_POLARITY\_NORMAL>, <&pwm2 3 PWM\_POLARITY\_INVERTED>; pwm-names = "alpha", "beta"; };

Example usage:

```
DT_PWMS_CTLR_BY_NAME(DT_NODELABEL(n), alpha) // DT_NODELABEL(pwm1)
DT_PWMS_CTLR_BY_NAME(DT_NODELABEL(n), beta)  // DT_NODELABEL(pwm2)
```

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |

Returns
:   the node identifier for the PWM controller in the named element

See also
:   [DT\_PHANDLE\_BY\_NAME()](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd "Get a phandle's node identifier from a phandle array by name.")

## [◆ ](#ga8dcd2d18129504d1a4ab71ae05c48c44)DT\_PWMS\_FLAGS

| #define DT\_PWMS\_FLAGS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_FLAGS\_BY\_IDX](#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)(node\_id, 0)

[DT\_PWMS\_FLAGS\_BY\_IDX](#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)

#define DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, idx)

Get a PWM specifier's flags cell value at an index.

**Definition** pwms.h:290

Equivalent to [DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, 0)](#gaf9c1ac7f3a39f4022f3ec31ef8de98e6).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |

Returns
:   the flags cell value at index 0, or zero if there is none

See also
:   [DT\_PWMS\_FLAGS\_BY\_IDX()](#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)

## [◆ ](#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)DT\_PWMS\_FLAGS\_BY\_IDX

| #define DT\_PWMS\_FLAGS\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)(node\_id, pwms, idx, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), 0)

[DT\_PHA\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)

#define DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value)

Like DT\_PHA\_BY\_IDX(), but with a fallback to default\_value.

**Definition** devicetree.h:1562

Get a PWM specifier's flags cell value at an index.

This macro expects PWM specifiers with cells named "flags". If there is no "flags" cell in the PWM specifier, zero is returned. Refer to the node's binding to check specifier cell names if necessary.

This is equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, flags)](#ga0c1ab3329448f92936d57a83b5b3594e).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | idx | logical index into pwms property |

Returns
:   the flags cell value at index "idx", or zero if there is none

See also
:   [DT\_PWMS\_CELL\_BY\_IDX()](#ga0c1ab3329448f92936d57a83b5b3594e)

## [◆ ](#ga7a1621bfb223da23aa030b64fc0c0bcd)DT\_PWMS\_FLAGS\_BY\_NAME

| #define DT\_PWMS\_FLAGS\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME\_OR](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)(node\_id, pwms, name, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), 0)

[DT\_PHA\_BY\_NAME\_OR](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)

#define DT\_PHA\_BY\_NAME\_OR(node\_id, pha, name, cell, default\_value)

Like DT\_PHA\_BY\_NAME(), but with a fallback to default\_value.

**Definition** devicetree.h:1655

Get a PWM specifier's flags cell value by name.

This macro expects PWM specifiers with cells named "flags". If there is no "flags" cell in the PWM specifier, zero is returned. Refer to the node's binding to check specifier cell names if necessary.

This is equivalent to [DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, flags)](#ga69233198a489283068bc1ded5072ca26) if there is a flags cell, but expands to zero if there is none.

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |

Returns
:   the flags cell value in the specifier at the named element, or zero if there is none

See also
:   [DT\_PWMS\_CELL\_BY\_NAME()](#ga69233198a489283068bc1ded5072ca26)

## [◆ ](#gac6006a723932325b96a1b50619be153b)DT\_PWMS\_PERIOD

| #define DT\_PWMS\_PERIOD | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_PERIOD\_BY\_IDX](#ga9456f65777e6fc7c057c6e0709c9245f)(node\_id, 0)

[DT\_PWMS\_PERIOD\_BY\_IDX](#ga9456f65777e6fc7c057c6e0709c9245f)

#define DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, idx)

Get PWM specifier's period cell value at an index.

**Definition** pwms.h:248

Equivalent to [DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, 0)](#ga9456f65777e6fc7c057c6e0709c9245f).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |

Returns
:   the period cell value at index 0

See also
:   [DT\_PWMS\_PERIOD\_BY\_IDX()](#ga9456f65777e6fc7c057c6e0709c9245f)

## [◆ ](#ga9456f65777e6fc7c057c6e0709c9245f)DT\_PWMS\_PERIOD\_BY\_IDX

| #define DT\_PWMS\_PERIOD\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CELL\_BY\_IDX](#ga0c1ab3329448f92936d57a83b5b3594e)(node\_id, idx, period)

Get PWM specifier's period cell value at an index.

This macro only works for PWM specifiers with cells named "period". Refer to the node's binding to check if necessary.

This is equivalent to [DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, period)](#ga0c1ab3329448f92936d57a83b5b3594e).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | idx | logical index into pwms property |

Returns
:   the period cell value at index "idx"

See also
:   [DT\_PWMS\_CELL\_BY\_IDX()](#ga0c1ab3329448f92936d57a83b5b3594e)

## [◆ ](#ga74af83d31fc38f331808dedfaecf4c74)DT\_PWMS\_PERIOD\_BY\_NAME

| #define DT\_PWMS\_PERIOD\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pwms.h](pwms_8h.md)>`

**Value:**

[DT\_PWMS\_CELL\_BY\_NAME](#ga69233198a489283068bc1ded5072ca26)(node\_id, name, period)

Get a PWM specifier's period cell value by name.

This macro only works for PWM specifiers with cells named "period". Refer to the node's binding to check if necessary.

This is equivalent to [DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, period)](#ga69233198a489283068bc1ded5072ca26).

Parameters
:   | node\_id | node identifier for a node with a pwms property |
    | --- | --- |
    | name | lowercase-and-underscores name of a pwms element as defined by the node's pwm-names property |

Returns
:   the period cell value in the specifier at the named element

See also
:   [DT\_PWMS\_CELL\_BY\_NAME()](#ga69233198a489283068bc1ded5072ca26)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
