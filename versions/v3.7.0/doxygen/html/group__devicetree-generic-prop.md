---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__devicetree-generic-prop.html
original_path: doxygen/html/group__devicetree-generic-prop.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Property accessors

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_PROP](#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, prop) |
|  | Get a devicetree property value. |
| #define | [DT\_PROP\_LEN](#gaa7f5afcedd1f54be79a5337e8e28a5b6)(node\_id, prop) |
|  | Get a property's logical length. |
| #define | [DT\_PROP\_LEN\_OR](#gabd2d8a9242818c7a9bf981114c912d75)(node\_id, prop, default\_value) |
|  | Like [DT\_PROP\_LEN()](#gaa7f5afcedd1f54be79a5337e8e28a5b6), but with a fallback to `default_value`. |
| #define | [DT\_PROP\_HAS\_IDX](#ga479dfc704087eea7e7c5af42ae98576c)(node\_id, prop, idx) |
|  | Is index `idx` valid for an array type property? |
| #define | [DT\_PROP\_HAS\_NAME](#gae46c100aecd299eaea51e033890d9a58)(node\_id, prop, name) |
|  | Is name `name` available in a foo-names property? |
| #define | [DT\_PROP\_BY\_IDX](#ga52ad691ea4cae633ca702020e939d461)(node\_id, prop, idx) |
|  | Get the value at index `idx` in an array type property. |
| #define | [DT\_PROP\_OR](#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, prop, default\_value) |
|  | Like [DT\_PROP()](#ga8e1fd9ebacd85d2013df027d041d506b), but with a fallback to `default_value`. |
| #define | [DT\_ENUM\_IDX](#ga6c1a3b93e30429c1c69a7e2d8fe2d840)(node\_id, prop) |
|  | Get a property value's index into its enumeration values. |
| #define | [DT\_ENUM\_IDX\_OR](#gac3616e3aa1a025235032786de8d31576)(node\_id, prop, default\_idx\_value) |
|  | Like [DT\_ENUM\_IDX()](#ga6c1a3b93e30429c1c69a7e2d8fe2d840), but with a fallback to a default enum index. |
| #define | [DT\_ENUM\_HAS\_VALUE](#ga72e66a2b7a159d8b6210ef9be015c955)(node\_id, prop, value) |
|  | Does a node enumeration property have a given value? |
| #define | [DT\_STRING\_TOKEN](#ga5995350cc7fd2d12ef7daa2487d1db54)(node\_id, prop) |
|  | Get a string property's value as a token. |
| #define | [DT\_STRING\_TOKEN\_OR](#ga5c7c7f82abd34403d4e9a6e0c5703e4c)(node\_id, prop, default\_value) |
|  | Like [DT\_STRING\_TOKEN()](#ga5995350cc7fd2d12ef7daa2487d1db54), but with a fallback to `default_value`. |
| #define | [DT\_STRING\_UPPER\_TOKEN](#gae0b5e2b6633a98ead17ec20d3494658f)(node\_id, prop) |
|  | Like [DT\_STRING\_TOKEN()](#ga5995350cc7fd2d12ef7daa2487d1db54), but uppercased. |
| #define | [DT\_STRING\_UPPER\_TOKEN\_OR](#gab79f5274c82d025d805ec94d2935c9b9)(node\_id, prop, default\_value) |
|  | Like [DT\_STRING\_UPPER\_TOKEN()](#gae0b5e2b6633a98ead17ec20d3494658f), but with a fallback to `default_value`. |
| #define | [DT\_STRING\_UNQUOTED](#gad71ae303ce20e116a75c23ca552c2225)(node\_id, prop) |
|  | Get a string property's value as an unquoted sequence of tokens. |
| #define | [DT\_STRING\_UNQUOTED\_OR](#gad9fefdcc15e991ba526300cd20f7c2fa)(node\_id, prop, default\_value) |
|  | Like [DT\_STRING\_UNQUOTED()](#gad71ae303ce20e116a75c23ca552c2225), but with a fallback to `default_value`. |
| #define | [DT\_STRING\_TOKEN\_BY\_IDX](#ga583e5e2e3c897f1095073e6192061d3a)(node\_id, prop, idx) |
|  | Get an element out of a string-array property as a token. |
| #define | [DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](#ga73105b3402fbd6f82274a8b4a2ca6b35)(node\_id, prop, idx) |
|  | Like [DT\_STRING\_TOKEN\_BY\_IDX()](#ga583e5e2e3c897f1095073e6192061d3a), but uppercased. |
| #define | [DT\_STRING\_UNQUOTED\_BY\_IDX](#ga3736709d70fdcb00bf305fd500f9ab64)(node\_id, prop, idx) |
|  | Get a string array item value as an unquoted sequence of tokens. |
| #define | [DT\_PROP\_BY\_PHANDLE\_IDX](#gaeba973992914d493cff5506ecf86a00d)(node\_id, phs, idx, prop) |
|  | Get a property value from a phandle in a property. |
| #define | [DT\_PROP\_BY\_PHANDLE\_IDX\_OR](#gad1c6a6544eac7bc77c1ed4aebd15df2b)(node\_id, phs, idx, prop, default\_value) |
|  | Like [DT\_PROP\_BY\_PHANDLE\_IDX()](#gaeba973992914d493cff5506ecf86a00d), but with a fallback to `default_value`. |
| #define | [DT\_PROP\_BY\_PHANDLE](#gabc1b099dda97fb03a9259a8b21fc04d2)(node\_id, ph, prop) |
|  | Get a property value from a phandle's node. |
| #define | [DT\_PHA\_BY\_IDX](#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, pha, idx, cell) |
|  | Get a phandle-array specifier cell value at an index. |
| #define | [DT\_PHA\_BY\_IDX\_OR](#gad830ed96dbc4f7dac3455153e0a944d6)(node\_id, pha, idx, cell, default\_value) |
|  | Like [DT\_PHA\_BY\_IDX()](#ga118b63fd22c20ef940ac2fa073c126ed), but with a fallback to `default_value`. |
| #define | [DT\_PHA](#gacef5921973a55433161fe0be3f8f628d)(node\_id, pha, cell) |
|  | Equivalent to [DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell)](#ga118b63fd22c20ef940ac2fa073c126ed). |
| #define | [DT\_PHA\_OR](#ga886559b058b24164b62ab95215d860bd)(node\_id, pha, cell, default\_value) |
|  | Like [DT\_PHA()](#gacef5921973a55433161fe0be3f8f628d), but with a fallback to `default_value`. |
| #define | [DT\_PHA\_BY\_NAME](#gae469615356a867c49416da15bdc44a26)(node\_id, pha, name, cell) |
|  | Get a value within a phandle-array specifier by name. |
| #define | [DT\_PHA\_BY\_NAME\_OR](#ga79cda6ca70cc1e27b034ad096d4f4401)(node\_id, pha, name, cell, default\_value) |
|  | Like [DT\_PHA\_BY\_NAME()](#gae469615356a867c49416da15bdc44a26), but with a fallback to `default_value`. |
| #define | [DT\_PHANDLE\_BY\_NAME](#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, pha, name) |
|  | Get a phandle's node identifier from a phandle array by `name`. |
| #define | [DT\_PHANDLE\_BY\_IDX](#ga8ff163c240878a988d29d727671671de)(node\_id, prop, idx) |
|  | Get a node identifier for a phandle in a property. |
| #define | [DT\_PHANDLE](#ga7bd77c49472ba4547d87f00f40fd7171)(node\_id, prop) |
|  | Get a node identifier for a phandle property's value. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga72e66a2b7a159d8b6210ef9be015c955)DT\_ENUM\_HAS\_VALUE

| #define DT\_ENUM\_HAS\_VALUE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT6(node\_id, \_P\_, prop, \_ENUM\_VAL\_, value, \_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Does a node enumeration property have a given value?

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | value | lowercase-and-underscores enumeration value |

Returns
:   1 if the node property has the value *value*, 0 otherwise.

## [◆ ](#ga6c1a3b93e30429c1c69a7e2d8fe2d840)DT\_ENUM\_IDX

| #define DT\_ENUM\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_ENUM\_IDX)

Get a property value's index into its enumeration values.

The return values start at zero.

Example devicetree fragment:

usb1: usb@12340000 {

maximum-speed = "full-speed";

};

usb2: usb@12341000 {

maximum-speed = "super-speed";

};

Example bindings fragment:

properties:

maximum-speed:

type: string

enum:

- "low-speed"

- "full-speed"

- "high-speed"

- "super-speed"

Example usage:

[DT\_ENUM\_IDX](#ga6c1a3b93e30429c1c69a7e2d8fe2d840)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(usb1), maximum\_speed) // 1

[DT\_ENUM\_IDX](#ga6c1a3b93e30429c1c69a7e2d8fe2d840)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(usb2), maximum\_speed) // 3

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:200

[DT\_ENUM\_IDX](#ga6c1a3b93e30429c1c69a7e2d8fe2d840)

#define DT\_ENUM\_IDX(node\_id, prop)

Get a property value's index into its enumeration values.

**Definition** devicetree.h:869

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   zero-based index of the property's value in its enum: list

## [◆ ](#gac3616e3aa1a025235032786de8d31576)DT\_ENUM\_IDX\_OR

| #define DT\_ENUM\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_idx\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, prop), \

([DT\_ENUM\_IDX](#ga6c1a3b93e30429c1c69a7e2d8fe2d840)(node\_id, prop)), (default\_idx\_value))

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3479

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

Like [DT\_ENUM\_IDX()](#ga6c1a3b93e30429c1c69a7e2d8fe2d840), but with a fallback to a default enum index.

If the value exists, this expands to its zero based index value thanks to [DT\_ENUM\_IDX(node\_id, prop)](#ga6c1a3b93e30429c1c69a7e2d8fe2d840).

Otherwise, this expands to provided default index enum value.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_idx\_value | a fallback index value to expand to |

Returns
:   zero-based index of the property's value in its enum if present, default\_idx\_value otherwise

## [◆ ](#gacef5921973a55433161fe0be3f8f628d)DT\_PHA

| #define DT\_PHA | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, pha, 0, cell)

[DT\_PHA\_BY\_IDX](#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1407

Equivalent to [DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell)](#ga118b63fd22c20ef940ac2fa073c126ed).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | cell | lowercase-and-underscores cell name |

Returns
:   the cell's value

## [◆ ](#ga118b63fd22c20ef940ac2fa073c126ed)DT\_PHA\_BY\_IDX

| #define DT\_PHA\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT7(node\_id, \_P\_, pha, \_IDX\_, idx, \_VAL\_, cell)

Get a phandle-array specifier cell value at an index.

It might help to read the argument order as being similar to node->phandle\_array[index].cell. That is, the cell value is in the `pha` property of `node_id`, inside the specifier at index `idx`.

Example devicetree fragment:

gpio0: gpio@abcd1234 {

#gpio-cells = <2>;

};

gpio1: gpio@1234abcd {

#gpio-cells = <2>;

};

led: led\_0 {

gpios = <&gpio0 17 0x1>, <&gpio1 5 0x3>;

};

Bindings fragment for the gpio0 and gpio1 nodes:

gpio-cells:

- pin

- flags

Above, gpios has two elements:

- index 0 has specifier <17 0x1>, so its pin cell is 17, and its [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) cell is 0x1
- index 1 has specifier <5 0x3>, so pin is 5 and [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) is 0x3

Example usage:

#define LED DT\_NODELABEL(led)

[DT\_PHA\_BY\_IDX](#ga118b63fd22c20ef940ac2fa073c126ed)(LED, gpios, 0, pin) // 17

[DT\_PHA\_BY\_IDX](#ga118b63fd22c20ef940ac2fa073c126ed)(LED, gpios, 1, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) // 0x3

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | idx | logical index into `pha` |
    | cell | lowercase-and-underscores cell name within the specifier at `pha` index `idx` |

Returns
:   the cell's value

## [◆ ](#gad830ed96dbc4f7dac3455153e0a944d6)DT\_PHA\_BY\_IDX\_OR

| #define DT\_PHA\_BY\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *idx*, |
|  |  |  | *cell*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_OR](#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, DT\_CAT5(pha, \_IDX\_, idx, \_VAL\_, cell), default\_value)

[DT\_PROP\_OR](#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:825

Like [DT\_PHA\_BY\_IDX()](#ga118b63fd22c20ef940ac2fa073c126ed), but with a fallback to `default_value`.

If the value exists, this expands to [DT\_PHA\_BY\_IDX(node\_id, pha,
idx, cell)](#ga118b63fd22c20ef940ac2fa073c126ed). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | idx | logical index into `pha` |
    | cell | lowercase-and-underscores cell name within the specifier at `pha` index `idx` |
    | default\_value | a fallback value to expand to |

Returns
:   the cell's value or `default_value`

## [◆ ](#gae469615356a867c49416da15bdc44a26)DT\_PHA\_BY\_NAME

| #define DT\_PHA\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT7(node\_id, \_P\_, pha, \_NAME\_, name, \_VAL\_, cell)

Get a value within a phandle-array specifier by name.

This is like [DT\_PHA\_BY\_IDX()](#ga118b63fd22c20ef940ac2fa073c126ed), except it treats `pha` as a structure where each array element has a name.

It might help to read the argument order as being similar to node->phandle\_struct.name.cell. That is, the cell value is in the `pha` property of `node_id`, treated as a data structure where each array element has a name.

Example devicetree fragment:

n: node {

io-channels = <&adc1 10>, <&adc2 20>;

io-channel-names = "SENSOR", "BANDGAP";

};

Bindings fragment for the "adc1" and "adc2" nodes:

io-channel-cells:

- input

Example usage:

[DT\_PHA\_BY\_NAME](#gae469615356a867c49416da15bdc44a26)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), io\_channels, sensor, input) // 10

[DT\_PHA\_BY\_NAME](#gae469615356a867c49416da15bdc44a26)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), io\_channels, bandgap, input) // 20

[DT\_PHA\_BY\_NAME](#gae469615356a867c49416da15bdc44a26)

#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)

Get a value within a phandle-array specifier by name.

**Definition** devicetree.h:1502

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | name | lowercase-and-underscores name of a specifier in `pha` |
    | cell | lowercase-and-underscores cell name in the named specifier |

Returns
:   the cell's value

## [◆ ](#ga79cda6ca70cc1e27b034ad096d4f4401)DT\_PHA\_BY\_NAME\_OR

| #define DT\_PHA\_BY\_NAME\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *name*, |
|  |  |  | *cell*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_OR](#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, DT\_CAT5(pha, \_NAME\_, name, \_VAL\_, cell), default\_value)

Like [DT\_PHA\_BY\_NAME()](#gae469615356a867c49416da15bdc44a26), but with a fallback to `default_value`.

If the value exists, this expands to [DT\_PHA\_BY\_NAME(node\_id, pha,
name, cell)](#gae469615356a867c49416da15bdc44a26). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | name | lowercase-and-underscores name of a specifier in `pha` |
    | cell | lowercase-and-underscores cell name in the named specifier |
    | default\_value | a fallback value to expand to |

Returns
:   the cell's value or `default_value`

## [◆ ](#ga886559b058b24164b62ab95215d860bd)DT\_PHA\_OR

| #define DT\_PHA\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *cell*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX\_OR](#gad830ed96dbc4f7dac3455153e0a944d6)(node\_id, pha, 0, cell, default\_value)

[DT\_PHA\_BY\_IDX\_OR](#gad830ed96dbc4f7dac3455153e0a944d6)

#define DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value)

Like DT\_PHA\_BY\_IDX(), but with a fallback to default\_value.

**Definition** devicetree.h:1433

Like [DT\_PHA()](#gacef5921973a55433161fe0be3f8f628d), but with a fallback to `default_value`.

If the value exists, this expands to [DT\_PHA(node\_id, pha, cell)](#gacef5921973a55433161fe0be3f8f628d). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | cell | lowercase-and-underscores cell name |
    | default\_value | a fallback value to expand to |

Returns
:   the cell's value or `default_value`

## [◆ ](#ga7bd77c49472ba4547d87f00f40fd7171)DT\_PHANDLE

| #define DT\_PHANDLE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](#ga8ff163c240878a988d29d727671671de)(node\_id, prop, 0)

[DT\_PHANDLE\_BY\_IDX](#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1628

Get a node identifier for a phandle property's value.

This is equivalent to [DT\_PHANDLE\_BY\_IDX(node\_id, prop, 0)](#ga8ff163c240878a988d29d727671671de). Its primary benefit is readability when `prop` has type phandle.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property of `node_id` with type phandle |

Returns
:   a node identifier for the node pointed to by "ph"

## [◆ ](#ga8ff163c240878a988d29d727671671de)DT\_PHANDLE\_BY\_IDX

| #define DT\_PHANDLE\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_PH)

Get a node identifier for a phandle in a property.

When a node's value at a logical index contains a phandle, this macro returns a node identifier for the node with that phandle.

Therefore, if `prop` has type phandle, `idx` must be zero. (A phandle type is treated as a phandles with a fixed length of 1).

Example devicetree fragment:

n1: node-1 {

foo = <&n2 &n3>;

};

n2: node-2 { ... };

n3: node-3 { ... };

Above, foo has type phandles and has two elements:

- index 0 has phandle &n2, which is node-2's phandle
- index 1 has phandle &n3, which is node-3's phandle

Example usage:

#define N1 DT\_NODELABEL(n1)

[DT\_PHANDLE\_BY\_IDX](#ga8ff163c240878a988d29d727671671de)(N1, foo, 0) // node identifier for node-2

[DT\_PHANDLE\_BY\_IDX](#ga8ff163c240878a988d29d727671671de)(N1, foo, 1) // node identifier for node-3

Behavior is analogous for phandle-arrays.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name in `node_id` with type phandle, phandles or phandle-array |
    | idx | index into `prop` |

Returns
:   node identifier for the node with the phandle at that index

## [◆ ](#ga65c90d2d96255b8569c5b869b637c2fd)DT\_PHANDLE\_BY\_NAME

| #define DT\_PHANDLE\_BY\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT6(node\_id, \_P\_, pha, \_NAME\_, name, \_PH)

Get a phandle's node identifier from a phandle array by `name`.

It might help to read the argument order as being similar to node->phandle\_struct.name.phandle. That is, the phandle array is treated as a structure with named elements. The return value is the node identifier for a phandle inside the structure.

Example devicetree fragment:

adc1: adc@abcd1234 {

foobar = "ADC\_1";

};

adc2: adc@1234abcd {

foobar = "ADC\_2";

};

n: node {

io-channels = <&adc1 10>, <&adc2 20>;

io-channel-names = "SENSOR", "BANDGAP";

};

Above, "io-channels" has two elements:

- the element named "SENSOR" has phandle &adc1
- the element named "BANDGAP" has phandle &adc2

Example usage:

#define NODE DT\_NODELABEL(n)

[DT\_PROP](#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_PHANDLE\_BY\_NAME](#ga65c90d2d96255b8569c5b869b637c2fd)(NODE, io\_channels, sensor), foobar) // "ADC\_1"

[DT\_PROP](#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_PHANDLE\_BY\_NAME](#ga65c90d2d96255b8569c5b869b637c2fd)(NODE, io\_channels, bandgap), foobar) // "ADC\_2"

[DT\_PHANDLE\_BY\_NAME](#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1576

[DT\_PROP](#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:663

Notice how devicetree properties and names are lowercased, and non-alphanumeric characters are converted to underscores.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | name | lowercase-and-underscores name of an element in `pha` |

Returns
:   a node identifier for the node with that phandle

## [◆ ](#ga8e1fd9ebacd85d2013df027d041d506b)DT\_PROP

| #define DT\_PROP | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT3(node\_id, \_P\_, prop)

Get a devicetree property value.

For properties whose bindings have the following types, this macro expands to:

- string: a string literal
- boolean: 0 if the property is false, or 1 if it is true
- int: the property's value as an integer literal
- array, uint8-array, string-array: an initializer expression in braces, whose elements are integer or string literals (like {0, 1, 2}, {"hello", "world"}, etc.)
- phandle: a node identifier for the node with that phandle

A property's type is usually defined by its binding. In some special cases, it has an assumed type defined by the devicetree specification even when no binding is available: compatible has type string-array, status has type string, and interrupt-controller has type boolean.

For other properties or properties with unknown type due to a missing binding, behavior is undefined.

For usage examples, see [DT\_PATH()](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086 "Get a node identifier for a devicetree path."), [DT\_ALIAS()](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9 "Get a node identifier from /aliases."), [DT\_NODELABEL()](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79 "Get a node identifier for a node label."), and [DT\_INST()](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead "Get a node identifier for an instance of a compatible.") above.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   a representation of the property's value

## [◆ ](#ga52ad691ea4cae633ca702020e939d461)DT\_PROP\_BY\_IDX

| #define DT\_PROP\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT5(node\_id, \_P\_, prop, \_IDX\_, idx)

Get the value at index `idx` in an array type property.

It might help to read the argument order as being similar to node->property[index].

The return value depends on the property's type:

- for types array, string-array, uint8-array, and phandles, this expands to the idx-th array element as an integer, string literal, integer, and node identifier respectively
- for type phandle, idx must be 0 and the expansion is a node identifier (this treats phandle like a phandles of length 1)
- for type string, idx must be 0 and the expansion is the entire string (this treats string like string-array of length 1)

These properties are handled as special cases:

- reg: use [DT\_REG\_ADDR\_BY\_IDX()](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243 "Get the base address of the register block at index idx.") or [DT\_REG\_SIZE\_BY\_IDX()](group__devicetree-reg-prop.md#ga9a703d688e4b983689b8579e0e7d9f48 "Get the size of the register block at index idx.") instead
- interrupts: use [DT\_IRQ\_BY\_IDX()](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f "Get a value within an interrupt specifier at an index.")
- ranges: use [DT\_NUM\_RANGES()](group__devicetree-ranges-prop.md#ga784cff5ee4c0439c429cc3c26c4410fc "Get the number of range blocks in the ranges property.")
- dma-ranges: it is an error to use this property with [DT\_PROP\_BY\_IDX()](#ga52ad691ea4cae633ca702020e939d461)

For properties of other types, behavior is undefined.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   a representation of the idx-th element of the property

## [◆ ](#gabc1b099dda97fb03a9259a8b21fc04d2)DT\_PROP\_BY\_PHANDLE

| #define DT\_PROP\_BY\_PHANDLE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *ph*, |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_BY\_PHANDLE\_IDX](#gaeba973992914d493cff5506ecf86a00d)(node\_id, ph, 0, prop)

[DT\_PROP\_BY\_PHANDLE\_IDX](#gaeba973992914d493cff5506ecf86a00d)

#define DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs, idx, prop)

Get a property value from a phandle in a property.

**Definition** devicetree.h:1314

Get a property value from a phandle's node.

This is equivalent to [DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, ph, 0, prop)](#gaeba973992914d493cff5506ecf86a00d).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | ph | lowercase-and-underscores property of `node_id` with type phandle |
    | prop | lowercase-and-underscores property of the phandle's node |

Returns
:   the property's value

## [◆ ](#gaeba973992914d493cff5506ecf86a00d)DT\_PROP\_BY\_PHANDLE\_IDX

| #define DT\_PROP\_BY\_PHANDLE\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *phs*, |
|  |  |  | *idx*, |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP](#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_PHANDLE\_BY\_IDX](#ga8ff163c240878a988d29d727671671de)(node\_id, phs, idx), prop)

Get a property value from a phandle in a property.

This is a shorthand for:

[DT\_PROP](#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_PHANDLE\_BY\_IDX](#ga8ff163c240878a988d29d727671671de)(node\_id, phs, idx), prop)

That is, `prop` is a property of the phandle's node, not a property of `node_id`.

Example devicetree fragment:

n1: node-1 {

foo = <&n2 &n3>;

};

n2: node-2 {

bar = <42>;

};

n3: node-3 {

baz = <43>;

};

Example usage:

#define N1 DT\_NODELABEL(n1)

[DT\_PROP\_BY\_PHANDLE\_IDX](#gaeba973992914d493cff5506ecf86a00d)(N1, foo, 0, bar) // 42

[DT\_PROP\_BY\_PHANDLE\_IDX](#gaeba973992914d493cff5506ecf86a00d)(N1, foo, 1, baz) // 43

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | phs | lowercase-and-underscores property with type phandle, phandles, or phandle-array |
    | idx | logical index into `phs`, which must be zero if `phs` has type phandle |
    | prop | lowercase-and-underscores property of the phandle's node |

Returns
:   the property's value

## [◆ ](#gad1c6a6544eac7bc77c1ed4aebd15df2b)DT\_PROP\_BY\_PHANDLE\_IDX\_OR

| #define DT\_PROP\_BY\_PHANDLE\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *phs*, |
|  |  |  | *idx*, |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_OR](#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_PHANDLE\_BY\_IDX](#ga8ff163c240878a988d29d727671671de)(node\_id, phs, idx), prop, default\_value)

Like [DT\_PROP\_BY\_PHANDLE\_IDX()](#gaeba973992914d493cff5506ecf86a00d), but with a fallback to `default_value`.

If the value exists, this expands to [DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs,
idx, prop)](#gaeba973992914d493cff5506ecf86a00d). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | phs | lowercase-and-underscores property with type phandle, phandles, or phandle-array |
    | idx | logical index into `phs`, which must be zero if `phs` has type phandle |
    | prop | lowercase-and-underscores property of the phandle's node |
    | default\_value | a fallback value to expand to |

Returns
:   the property's value

## [◆ ](#ga479dfc704087eea7e7c5af42ae98576c)DT\_PROP\_HAS\_IDX

| #define DT\_PROP\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_EXISTS))

Is index `idx` valid for an array type property?

If this returns 1, then [DT\_PROP\_BY\_IDX(node\_id, prop, idx)](#ga52ad691ea4cae633ca702020e939d461) or [DT\_PHA\_BY\_IDX(node\_id, prop, idx, ...)](#ga118b63fd22c20ef940ac2fa073c126ed) are valid at index `idx`. If it returns 0, it is an error to use those macros with that index.

These properties are handled as special cases:

- reg property: use [DT\_REG\_HAS\_IDX(node\_id, idx)](group__devicetree-reg-prop.md#ga59aa43231678d08eeac6e5b344048f02 "Is idx a valid register block index?") instead
- interrupts property: use [DT\_IRQ\_HAS\_IDX(node\_id, idx)](group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c "Is idx a valid interrupt index?") instead

It is an error to use this macro with the reg or interrupts properties.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | a lowercase-and-underscores property with a logical length |
    | idx | index to check |

Returns
:   An expression which evaluates to 1 if `idx` is a valid index into the given property, and 0 otherwise.

## [◆ ](#gae46c100aecd299eaea51e033890d9a58)DT\_PROP\_HAS\_NAME

| #define DT\_PROP\_HAS\_NAME | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT6(node\_id, \_P\_, prop, \_NAME\_, name, \_EXISTS))

Is name `name` available in a foo-names property?

This property is handled as special case:

- interrupts property: use [DT\_IRQ\_HAS\_NAME(node\_id, idx)](group__devicetree-interrupts-prop.md#ga1c757ff5e4d15f1b3020b30f72c0dd5d "Does an interrupts property have a named specifier value at an index?") instead

It is an error to use this macro with the interrupts property.

Example devicetree fragment:

nx: node-x {

foos = <&bar xx yy>, <&baz xx zz>;

foo-names = "event", "error";

status = "okay";

};

Example usage:

[DT\_PROP\_HAS\_NAME](#gae46c100aecd299eaea51e033890d9a58)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(nx), foos, event) // 1

[DT\_PROP\_HAS\_NAME](#gae46c100aecd299eaea51e033890d9a58)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(nx), foos, failure) // 0

[DT\_PROP\_HAS\_NAME](#gae46c100aecd299eaea51e033890d9a58)

#define DT\_PROP\_HAS\_NAME(node\_id, prop, name)

Is name name available in a foo-names property?

**Definition** devicetree.h:772

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | a lowercase-and-underscores prop-names type property |
    | name | a lowercase-and-underscores name to check |

Returns
:   An expression which evaluates to 1 if "name" is an available name into the given property, and 0 otherwise.

## [◆ ](#gaa7f5afcedd1f54be79a5337e8e28a5b6)DT\_PROP\_LEN

| #define DT\_PROP\_LEN | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_LEN)

Get a property's logical length.

Here, "length" is a number of elements, which may differ from the property's size in bytes.

The return value depends on the property's type:

- for types array, string-array, and uint8-array, this expands to the number of elements in the array
- for type phandles, this expands to the number of phandles
- for type phandle-array, this expands to the number of phandle and specifier blocks in the property
- for type phandle, this expands to 1 (so that a phandle can be treated as a degenerate case of phandles with length 1)
- for type string, this expands to 1 (so that a string can be treated as a degenerate case of string-array with length 1)

These properties are handled as special cases:

- reg property: use [DT\_NUM\_REGS(node\_id)](group__devicetree-reg-prop.md#ga6cdd22b6a2881b09ed63d9d262566a0a "Get the number of register blocks in the reg property.") instead
- interrupts property: use [DT\_NUM\_IRQS(node\_id)](group__devicetree-interrupts-prop.md#ga2985e5d55d2d9dbbbe93ba855d5db320 "Get the number of interrupt sources for the node.") instead

It is an error to use this macro with the ranges, dma-ranges, reg or interrupts properties.

For other properties, behavior is undefined.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | a lowercase-and-underscores property with a logical length |

Returns
:   the property's length

## [◆ ](#gabd2d8a9242818c7a9bf981114c912d75)DT\_PROP\_LEN\_OR

| #define DT\_PROP\_LEN\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, prop), \

([DT\_PROP\_LEN](#gaa7f5afcedd1f54be79a5337e8e28a5b6)(node\_id, prop)), (default\_value))

[DT\_PROP\_LEN](#gaa7f5afcedd1f54be79a5337e8e28a5b6)

#define DT\_PROP\_LEN(node\_id, prop)

Get a property's logical length.

**Definition** devicetree.h:697

Like [DT\_PROP\_LEN()](#gaa7f5afcedd1f54be79a5337e8e28a5b6), but with a fallback to `default_value`.

If the property is defined (as determined by [DT\_NODE\_HAS\_PROP()](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692 "Does a devicetree node have a property?")), this expands to [DT\_PROP\_LEN(node\_id, prop)](#gaa7f5afcedd1f54be79a5337e8e28a5b6). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | a lowercase-and-underscores property with a logical length |
    | default\_value | a fallback value to expand to |

Returns
:   the property's length or the given default value

## [◆ ](#ga5e5bfc9b1a6627b3f73014329e96340f)DT\_PROP\_OR

| #define DT\_PROP\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, prop), \

([DT\_PROP](#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, prop)), (default\_value))

Like [DT\_PROP()](#ga8e1fd9ebacd85d2013df027d041d506b), but with a fallback to `default_value`.

If the value exists, this expands to [DT\_PROP(node\_id, prop)](#ga8e1fd9ebacd85d2013df027d041d506b). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   the property's value or `default_value`

## [◆ ](#ga5995350cc7fd2d12ef7daa2487d1db54)DT\_STRING\_TOKEN

| #define DT\_STRING\_TOKEN | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_TOKEN)

Get a string property's value as a token.

This removes "the quotes" from a string property's value, converting any non-alphanumeric characters to underscores. This can be useful, for example, when programmatically using the value to form a C variable or code.

[DT\_STRING\_TOKEN()](#ga5995350cc7fd2d12ef7daa2487d1db54) can only be used for properties with string type.

It is an error to use [DT\_STRING\_TOKEN()](#ga5995350cc7fd2d12ef7daa2487d1db54) in other circumstances.

Example devicetree fragment:

n1: node-1 {

prop = "foo";

};

n2: node-2 {

prop = "FOO";

}

n3: node-3 {

prop = "123 foo";

};

Example bindings fragment:

properties:

prop:

type: string

Example usage:

[DT\_STRING\_TOKEN](#ga5995350cc7fd2d12ef7daa2487d1db54)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n1), prop) // foo

[DT\_STRING\_TOKEN](#ga5995350cc7fd2d12ef7daa2487d1db54)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n2), prop) // FOO

[DT\_STRING\_TOKEN](#ga5995350cc7fd2d12ef7daa2487d1db54)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n3), prop) // 123\_foo

[DT\_STRING\_TOKEN](#ga5995350cc7fd2d12ef7daa2487d1db54)

#define DT\_STRING\_TOKEN(node\_id, prop)

Get a string property's value as a token.

**Definition** devicetree.h:959

Notice how:

- Unlike C identifiers, the property values may begin with a number. It's the user's responsibility not to use such values as the name of a C identifier.
- The uppercased "FOO" in the DTS remains FOO as a token. It is *not* converted to foo.
- The whitespace in the DTS "123 foo" string is converted to 123\_foo as a token.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   the value of `prop` as a token, i.e. without any quotes and with special characters converted to underscores

## [◆ ](#ga583e5e2e3c897f1095073e6192061d3a)DT\_STRING\_TOKEN\_BY\_IDX

| #define DT\_STRING\_TOKEN\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_TOKEN)

Get an element out of a string-array property as a token.

This removes "the quotes" from an element in the array, and converts non-alphanumeric characters to underscores. That can be useful, for example, when programmatically using the value to form a C variable or code.

[DT\_STRING\_TOKEN\_BY\_IDX()](#ga583e5e2e3c897f1095073e6192061d3a) can only be used for properties with string-array type.

It is an error to use [DT\_STRING\_TOKEN\_BY\_IDX()](#ga583e5e2e3c897f1095073e6192061d3a) in other circumstances.

Example devicetree fragment:

n1: node-1 {

prop = "f1", "F2";

};

n2: node-2 {

prop = "123 foo", "456 FOO";

};

Example bindings fragment:

properties:

prop:

type: string-array

Example usage:

[DT\_STRING\_TOKEN\_BY\_IDX](#ga583e5e2e3c897f1095073e6192061d3a)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n1), prop, 0) // f1

[DT\_STRING\_TOKEN\_BY\_IDX](#ga583e5e2e3c897f1095073e6192061d3a)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n1), prop, 1) // F2

[DT\_STRING\_TOKEN\_BY\_IDX](#ga583e5e2e3c897f1095073e6192061d3a)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n2), prop, 0) // 123\_foo

[DT\_STRING\_TOKEN\_BY\_IDX](#ga583e5e2e3c897f1095073e6192061d3a)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n2), prop, 1) // 456\_FOO

[DT\_STRING\_TOKEN\_BY\_IDX](#ga583e5e2e3c897f1095073e6192061d3a)

#define DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx)

Get an element out of a string-array property as a token.

**Definition** devicetree.h:1165

For more information, see [DT\_STRING\_TOKEN](#ga5995350cc7fd2d12ef7daa2487d1db54).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   the element in `prop` at index `idx` as a token

## [◆ ](#ga5c7c7f82abd34403d4e9a6e0c5703e4c)DT\_STRING\_TOKEN\_OR

| #define DT\_STRING\_TOKEN\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, prop), \

([DT\_STRING\_TOKEN](#ga5995350cc7fd2d12ef7daa2487d1db54)(node\_id, prop)), (default\_value))

Like [DT\_STRING\_TOKEN()](#ga5995350cc7fd2d12ef7daa2487d1db54), but with a fallback to `default_value`.

If the value exists, this expands to [DT\_STRING\_TOKEN(node\_id, prop)](#ga5995350cc7fd2d12ef7daa2487d1db54). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   the property's value as a token, or `default_value`

## [◆ ](#gad71ae303ce20e116a75c23ca552c2225)DT\_STRING\_UNQUOTED

| #define DT\_STRING\_UNQUOTED | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UNQUOTED)

Get a string property's value as an unquoted sequence of tokens.

This removes "the quotes" from string-valued properties. That can be useful, for example, when defining floating point values as a string in devicetree that you would like to use to initialize a float or double variable in C.

[DT\_STRING\_UNQUOTED()](#gad71ae303ce20e116a75c23ca552c2225) can only be used for properties with string type.

It is an error to use [DT\_STRING\_UNQUOTED()](#gad71ae303ce20e116a75c23ca552c2225) in other circumstances.

Example devicetree fragment:

```
n1: node-1 {
        prop = "12.7";
};
n2: node-2 {
        prop = "0.5";
}
n3: node-3 {
        prop = "A B C";
};
```

Example bindings fragment:

```
properties:
  prop:
    type: string
```

Example usage:

```
DT_STRING_UNQUOTED(DT_NODELABEL(n1), prop) // 12.7
DT_STRING_UNQUOTED(DT_NODELABEL(n2), prop) // 0.5
DT_STRING_UNQUOTED(DT_NODELABEL(n3), prop) // A B C
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   the property's value as a sequence of tokens, with no quotes

## [◆ ](#ga3736709d70fdcb00bf305fd500f9ab64)DT\_STRING\_UNQUOTED\_BY\_IDX

| #define DT\_STRING\_UNQUOTED\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UNQUOTED)

Get a string array item value as an unquoted sequence of tokens.

This removes "the quotes" from string-valued item. That can be useful, for example, when defining floating point values as a string in devicetree that you would like to use to initialize a float or double variable in C.

[DT\_STRING\_UNQUOTED\_BY\_IDX()](#ga3736709d70fdcb00bf305fd500f9ab64) can only be used for properties with string-array type.

It is an error to use [DT\_STRING\_UNQUOTED\_BY\_IDX()](#ga3736709d70fdcb00bf305fd500f9ab64) in other circumstances.

Example devicetree fragment:

```
n1: node-1 {
        prop = "12.7", "34.1";
};
n2: node-2 {
        prop = "A B", "C D";
}
```

Example bindings fragment:

```
properties:
  prop:
    type: string-array
```

Example usage:

```
DT_STRING_UNQUOTED_BY_IDX(DT_NODELABEL(n1), prop, 0) // 12.7
DT_STRING_UNQUOTED_BY_IDX(DT_NODELABEL(n1), prop, 1) // 34.1
DT_STRING_UNQUOTED_BY_IDX(DT_NODELABEL(n2), prop, 0) // A B
DT_STRING_UNQUOTED_BY_IDX(DT_NODELABEL(n2), prop, 1) // C D
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   the property's value as a sequence of tokens, with no quotes

## [◆ ](#gad9fefdcc15e991ba526300cd20f7c2fa)DT\_STRING\_UNQUOTED\_OR

| #define DT\_STRING\_UNQUOTED\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, prop), \

([DT\_STRING\_UNQUOTED](#gad71ae303ce20e116a75c23ca552c2225)(node\_id, prop)), (default\_value))

[DT\_STRING\_UNQUOTED](#gad71ae303ce20e116a75c23ca552c2225)

#define DT\_STRING\_UNQUOTED(node\_id, prop)

Get a string property's value as an unquoted sequence of tokens.

**Definition** devicetree.h:1097

Like [DT\_STRING\_UNQUOTED()](#gad71ae303ce20e116a75c23ca552c2225), but with a fallback to `default_value`.

If the value exists, this expands to [DT\_STRING\_UNQUOTED(node\_id, prop)](#gad71ae303ce20e116a75c23ca552c2225). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   the property's value as a sequence of tokens, with no quotes, or `default_value`

## [◆ ](#gae0b5e2b6633a98ead17ec20d3494658f)DT\_STRING\_UPPER\_TOKEN

| #define DT\_STRING\_UPPER\_TOKEN | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_STRING\_UPPER\_TOKEN)

Like [DT\_STRING\_TOKEN()](#ga5995350cc7fd2d12ef7daa2487d1db54), but uppercased.

This removes "the quotes" from a string property's value, converting any non-alphanumeric characters to underscores, and capitalizing the result. This can be useful, for example, when programmatically using the value to form a C variable or code.

[DT\_STRING\_UPPER\_TOKEN()](#gae0b5e2b6633a98ead17ec20d3494658f) can only be used for properties with string type.

It is an error to use [DT\_STRING\_UPPER\_TOKEN()](#gae0b5e2b6633a98ead17ec20d3494658f) in other circumstances.

Example devicetree fragment:

n1: node-1 {

prop = "foo";

};

n2: node-2 {

prop = "123 foo";

};

Example bindings fragment:

properties:

prop:

type: string

Example usage:

[DT\_STRING\_UPPER\_TOKEN](#gae0b5e2b6633a98ead17ec20d3494658f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n1), prop) // FOO

[DT\_STRING\_UPPER\_TOKEN](#gae0b5e2b6633a98ead17ec20d3494658f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n2), prop) // 123\_FOO

[DT\_STRING\_UPPER\_TOKEN](#gae0b5e2b6633a98ead17ec20d3494658f)

#define DT\_STRING\_UPPER\_TOKEN(node\_id, prop)

Like DT\_STRING\_TOKEN(), but uppercased.

**Definition** devicetree.h:1036

Notice how:

- Unlike C identifiers, the property values may begin with a number. It's the user's responsibility not to use such values as the name of a C identifier.
- The lowercased "foo" in the DTS becomes FOO as a token, i.e. it is uppercased.
- The whitespace in the DTS "123 foo" string is converted to 123\_FOO as a token, i.e. it is uppercased and whitespace becomes an underscore.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   the value of `prop` as an uppercased token, i.e. without any quotes and with special characters converted to underscores

## [◆ ](#ga73105b3402fbd6f82274a8b4a2ca6b35)DT\_STRING\_UPPER\_TOKEN\_BY\_IDX

| #define DT\_STRING\_UPPER\_TOKEN\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT6(node\_id, \_P\_, prop, \_IDX\_, idx, \_STRING\_UPPER\_TOKEN)

Like [DT\_STRING\_TOKEN\_BY\_IDX()](#ga583e5e2e3c897f1095073e6192061d3a), but uppercased.

This removes "the quotes" and capitalizes an element in the array, and converts non-alphanumeric characters to underscores. That can be useful, for example, when programmatically using the value to form a C variable or code.

[DT\_STRING\_UPPER\_TOKEN\_BY\_IDX()](#ga73105b3402fbd6f82274a8b4a2ca6b35) can only be used for properties with string-array type.

It is an error to use [DT\_STRING\_UPPER\_TOKEN\_BY\_IDX()](#ga73105b3402fbd6f82274a8b4a2ca6b35) in other circumstances.

Example devicetree fragment:

n1: node-1 {

prop = "f1", "F2";

};

n2: node-2 {

prop = "123 foo", "456 FOO";

};

Example bindings fragment:

properties:

prop:

type: string-array

Example usage:

[DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](#ga73105b3402fbd6f82274a8b4a2ca6b35)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n1), prop, 0) // F1

[DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](#ga73105b3402fbd6f82274a8b4a2ca6b35)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n1), prop, 1) // F2

[DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](#ga73105b3402fbd6f82274a8b4a2ca6b35)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n2), prop, 0) // 123\_FOO

[DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](#ga73105b3402fbd6f82274a8b4a2ca6b35)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n2), prop, 1) // 456\_FOO

[DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](#ga73105b3402fbd6f82274a8b4a2ca6b35)

#define DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(node\_id, prop, idx)

Like DT\_STRING\_TOKEN\_BY\_IDX(), but uppercased.

**Definition** devicetree.h:1215

For more information, see [DT\_STRING\_UPPER\_TOKEN](#gae0b5e2b6633a98ead17ec20d3494658f).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   the element in `prop` at index `idx` as an uppercased token

## [◆ ](#gab79f5274c82d025d805ec94d2935c9b9)DT\_STRING\_UPPER\_TOKEN\_OR

| #define DT\_STRING\_UPPER\_TOKEN\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, prop), \

([DT\_STRING\_UPPER\_TOKEN](#gae0b5e2b6633a98ead17ec20d3494658f)(node\_id, prop)), (default\_value))

Like [DT\_STRING\_UPPER\_TOKEN()](#gae0b5e2b6633a98ead17ec20d3494658f), but with a fallback to `default_value`.

If the value exists, this expands to [DT\_STRING\_UPPER\_TOKEN(node\_id, prop)](#gae0b5e2b6633a98ead17ec20d3494658f). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   the property's value as an uppercased token, or `default_value`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
