---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__devicetree-ranges-prop.html
original_path: doxygen/html/group__devicetree-ranges-prop.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ranges property

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_NUM\_RANGES](#ga784cff5ee4c0439c429cc3c26c4410fc)(node\_id) |
|  | Get the number of range blocks in the ranges property. |
| #define | [DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)(node\_id, idx) |
|  | Is `idx` a valid range block index? |
| #define | [DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)(node\_id, idx) |
|  | Does a ranges property have child bus flags at index? |
| #define | [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX](#ga32a9c873d3ec1f5d7922c38eaafd1af8)(node\_id, idx) |
|  | Get the ranges property child bus flags at index. |
| #define | [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](#ga449940559213086b15151ec00e46607d)(node\_id, idx) |
|  | Get the ranges property child bus address at index. |
| #define | [DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](#ga48d493ad616438ace2396c0312a242ba)(node\_id, idx) |
|  | Get the ranges property parent bus address at index. |
| #define | [DT\_RANGES\_LENGTH\_BY\_IDX](#ga52677a5bc86f9132a09b6bc37153afb2)(node\_id, idx) |
|  | Get the ranges property length at index. |
| #define | [DT\_FOREACH\_RANGE](#ga4c71a8adcfe6c53b480775510c92a632)(node\_id, fn) |
|  | Invokes `fn` for each entry of `node_id` ranges property. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga4c71a8adcfe6c53b480775510c92a632)DT\_FOREACH\_RANGE

| #define DT\_FOREACH\_RANGE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_RANGE)(fn)

Invokes `fn` for each entry of `node_id` ranges property.

The macro `fn` must take two parameters, `node_id` which will be the node identifier of the node with the ranges property and `idx` the index of the ranges block.

Example devicetree fragment:

n: node@0 {

reg = <0 0 1>;

ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,

<0x0 0x10000000 0x0 0x10000000 0x2eff0000>;

};

Example usage:

#define RANGE\_LENGTH(node\_id, idx) DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx),

const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ranges\_length[] = {

[DT\_FOREACH\_RANGE](#ga4c71a8adcfe6c53b480775510c92a632)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), RANGE\_LENGTH)

};

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:200

[DT\_FOREACH\_RANGE](#ga4c71a8adcfe6c53b480775510c92a632)

#define DT\_FOREACH\_RANGE(node\_id, fn)

Invokes fn for each entry of node\_id ranges property.

**Definition** devicetree.h:2028

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

This expands to:

const char \*ranges\_length[] = {

0x10000, 0x2eff0000,

};

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |

## [◆ ](#ga784cff5ee4c0439c429cc3c26c4410fc)DT\_NUM\_RANGES

| #define DT\_NUM\_RANGES | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_RANGES\_NUM)

Get the number of range blocks in the ranges property.

Use this instead of [DT\_PROP\_LEN(node\_id, ranges)](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6 "Get a property's logical length.").

Example devicetree fragment:

pcie0: pcie@0 {

compatible = "pcie-controller";

reg = <0 1>;

#address-cells = <3>;

#size-cells = <2>;

ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,

<0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,

<0x3000000 0x80 0 0x80 0 0x80 0>;

};

other: other@1 {

reg = <1 1>;

ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,

<0x0 0x10000000 0x0 0x10000000 0x2eff0000>;

};

Example usage:

[DT\_NUM\_RANGES](#ga784cff5ee4c0439c429cc3c26c4410fc)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0)) // 3

[DT\_NUM\_RANGES](#ga784cff5ee4c0439c429cc3c26c4410fc)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other)) // 2

[DT\_NUM\_RANGES](#ga784cff5ee4c0439c429cc3c26c4410fc)

#define DT\_NUM\_RANGES(node\_id)

Get the number of range blocks in the ranges property.

**Definition** devicetree.h:1690

Parameters
:   | node\_id | node identifier |
    | --- | --- |

## [◆ ](#ga449940559213086b15151ec00e46607d)DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX

| #define DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_ADDRESS)

Get the ranges property child bus address at index.

When the node is a PCIe bus, the Child Bus Address has an extra cell used to store some flags, thus this cell is removed from the Child Bus Address.

Example devicetree fragments:

parent {

#address-cells = <2>;

pcie0: pcie@0 {

compatible = "pcie-controller";

reg = <0 0 1>;

#address-cells = <3>;

#size-cells = <2>;

ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,

<0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,

<0x3000000 0x80 0 0x80 0 0x80 0>;

};

other: other@1 {

reg = <0 1 1>;

ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,

<0x0 0x10000000 0x0 0x10000000 0x2eff0000>;

};

};

Example usage:

[DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](#ga449940559213086b15151ec00e46607d)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 0) // 0

[DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](#ga449940559213086b15151ec00e46607d)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 1) // 0x10000000

[DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](#ga449940559213086b15151ec00e46607d)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 2) // 0x8000000000

[DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](#ga449940559213086b15151ec00e46607d)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 0) // 0

[DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](#ga449940559213086b15151ec00e46607d)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 1) // 0x10000000

[DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](#ga449940559213086b15151ec00e46607d)

#define DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)

Get the ranges property child bus address at index.

**Definition** devicetree.h:1888

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into the ranges array |

Returns
:   range child bus address field at idx

## [◆ ](#ga32a9c873d3ec1f5d7922c38eaafd1af8)DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX

| #define DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS)

Get the ranges property child bus flags at index.

When the node is a PCIe bus, the Child Bus Address has an extra cell used to store some flags, thus this cell is extracted from the Child Bus Address as Child Bus Flags field.

Example devicetree fragments:

parent {

#address-cells = <2>;

pcie0: pcie@0 {

compatible = "pcie-controller";

reg = <0 0 1>;

#address-cells = <3>;

#size-cells = <2>;

ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,

<0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,

<0x3000000 0x80 0 0x80 0 0x80 0>;

};

};

Example usage:

[DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX](#ga32a9c873d3ec1f5d7922c38eaafd1af8)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 0) // 0x1000000

[DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX](#ga32a9c873d3ec1f5d7922c38eaafd1af8)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 1) // 0x2000000

[DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX](#ga32a9c873d3ec1f5d7922c38eaafd1af8)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 2) // 0x3000000

[DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX](#ga32a9c873d3ec1f5d7922c38eaafd1af8)

#define DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)

Get the ranges property child bus flags at index.

**Definition** devicetree.h:1839

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into the ranges array |

Returns
:   range child bus flags field at idx

## [◆ ](#ga3730c9176911bd8cc762f447eb020ecd)DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX

| #define DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_CHILD\_BUS\_FLAGS\_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Does a ranges property have child bus flags at index?

If this returns 1, then [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)](#ga32a9c873d3ec1f5d7922c38eaafd1af8) is valid. If it returns 0, it is an error to use this macro with index `idx`. This macro only returns 1 for PCIe buses (i.e. nodes whose bindings specify they are "pcie" bus nodes.)

Example devicetree fragment:

parent {

#address-cells = <2>;

pcie0: pcie@0 {

compatible = "pcie-controller";

reg = <0 0 1>;

#address-cells = <3>;

#size-cells = <2>;

ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,

<0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,

<0x3000000 0x80 0 0x80 0 0x80 0>;

};

other: other@1 {

reg = <0 1 1>;

ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,

<0x0 0x10000000 0x0 0x10000000 0x2eff0000>;

};

};

Example usage:

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 0) // 1

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 1) // 1

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 2) // 1

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 3) // 0

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 0) // 0

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 1) // 0

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 2) // 0

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 3) // 0

[DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](#ga3730c9176911bd8cc762f447eb020ecd)

#define DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX(node\_id, idx)

Does a ranges property have child bus flags at index?

**Definition** devicetree.h:1799

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into the ranges array |

Returns
:   1 if `idx` is a valid child bus flags index, 0 otherwise.

## [◆ ](#gac6f54058c58b06935bd2deae9f1ec2db)DT\_RANGES\_HAS\_IDX

| #define DT\_RANGES\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_EXISTS))

Is `idx` a valid range block index?

If this returns 1, then [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)](#ga449940559213086b15151ec00e46607d), [DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)](#ga48d493ad616438ace2396c0312a242ba) or [DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx)](#ga52677a5bc86f9132a09b6bc37153afb2) are valid. For [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)](#ga32a9c873d3ec1f5d7922c38eaafd1af8) the return value of [DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX(node\_id, idx)](#ga3730c9176911bd8cc762f447eb020ecd) will indicate validity. If it returns 0, it is an error to use those macros with index `idx`, including [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX(node\_id, idx)](#ga32a9c873d3ec1f5d7922c38eaafd1af8).

Example devicetree fragment:

pcie0: pcie@0 {

compatible = "pcie-controller";

reg = <0 1>;

#address-cells = <3>;

#size-cells = <2>;

ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,

<0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,

<0x3000000 0x80 0 0x80 0 0x80 0>;

};

other: other@1 {

reg = <1 1>;

ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,

<0x0 0x10000000 0x0 0x10000000 0x2eff0000>;

};

Example usage:

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 0) // 1

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 1) // 1

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 2) // 1

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 3) // 0

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 0) // 1

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 1) // 1

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 2) // 0

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 3) // 0

[DT\_RANGES\_HAS\_IDX](#gac6f54058c58b06935bd2deae9f1ec2db)

#define DT\_RANGES\_HAS\_IDX(node\_id, idx)

Is idx a valid range block index?

**Definition** devicetree.h:1744

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index to check |

Returns
:   1 if `idx` is a valid register block index, 0 otherwise.

## [◆ ](#ga52677a5bc86f9132a09b6bc37153afb2)DT\_RANGES\_LENGTH\_BY\_IDX

| #define DT\_RANGES\_LENGTH\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_LENGTH)

Get the ranges property length at index.

Similarly to [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX()](#ga449940559213086b15151ec00e46607d), this properly accounts for child bus flags cells when the node is a PCIe bus.

Example devicetree fragment:

parent {

#address-cells = <2>;

pcie0: pcie@0 {

compatible = "pcie-controller";

reg = <0 0 1>;

#address-cells = <3>;

#size-cells = <2>;

ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,

<0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,

<0x3000000 0x80 0 0x80 0 0x80 0>;

};

other: other@1 {

reg = <0 1 1>;

ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,

<0x0 0x10000000 0x0 0x10000000 0x2eff0000>;

};

};

Example usage:

[DT\_RANGES\_LENGTH\_BY\_IDX](#ga52677a5bc86f9132a09b6bc37153afb2)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 0) // 0x10000

[DT\_RANGES\_LENGTH\_BY\_IDX](#ga52677a5bc86f9132a09b6bc37153afb2)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 1) // 0x2eff0000

[DT\_RANGES\_LENGTH\_BY\_IDX](#ga52677a5bc86f9132a09b6bc37153afb2)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 2) // 0x8000000000

[DT\_RANGES\_LENGTH\_BY\_IDX](#ga52677a5bc86f9132a09b6bc37153afb2)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 0) // 0x10000

[DT\_RANGES\_LENGTH\_BY\_IDX](#ga52677a5bc86f9132a09b6bc37153afb2)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 1) // 0x2eff0000

[DT\_RANGES\_LENGTH\_BY\_IDX](#ga52677a5bc86f9132a09b6bc37153afb2)

#define DT\_RANGES\_LENGTH\_BY\_IDX(node\_id, idx)

Get the ranges property length at index.

**Definition** devicetree.h:1986

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into the ranges array |

Returns
:   range length field at idx

## [◆ ](#ga48d493ad616438ace2396c0312a242ba)DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX

| #define DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_RANGES\_IDX\_, idx, \_VAL\_PARENT\_BUS\_ADDRESS)

Get the ranges property parent bus address at index.

Similarly to [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX()](#ga449940559213086b15151ec00e46607d), this properly accounts for child bus flags cells when the node is a PCIe bus.

Example devicetree fragment:

parent {

#address-cells = <2>;

pcie0: pcie@0 {

compatible = "pcie-controller";

reg = <0 0 1>;

#address-cells = <3>;

#size-cells = <2>;

ranges = <0x1000000 0 0 0 0x3eff0000 0 0x10000>,

<0x2000000 0 0x10000000 0 0x10000000 0 0x2eff0000>,

<0x3000000 0x80 0 0x80 0 0x80 0>;

};

other: other@1 {

reg = <0 1 1>;

ranges = <0x0 0x0 0x0 0x3eff0000 0x10000>,

<0x0 0x10000000 0x0 0x10000000 0x2eff0000>;

};

};

Example usage:

[DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](#ga48d493ad616438ace2396c0312a242ba)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 0) // 0x3eff0000

[DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](#ga48d493ad616438ace2396c0312a242ba)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 1) // 0x10000000

[DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](#ga48d493ad616438ace2396c0312a242ba)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(pcie0), 2) // 0x8000000000

[DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](#ga48d493ad616438ace2396c0312a242ba)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 0) // 0x3eff0000

[DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](#ga48d493ad616438ace2396c0312a242ba)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(other), 1) // 0x10000000

[DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](#ga48d493ad616438ace2396c0312a242ba)

#define DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX(node\_id, idx)

Get the ranges property parent bus address at index.

**Definition** devicetree.h:1937

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into the ranges array |

Returns
:   range parent bus address field at idx

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
