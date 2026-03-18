---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__devicetree-generic-id.html
original_path: doxygen/html/group__devicetree-generic-id.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Node identifiers and helpers

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_INVALID\_NODE](#ga710cc4455dd7e738f43f750153163855)   \_ |
|  | Name for an invalid node identifier. |
| #define | [DT\_ROOT](#gad65aa36621281687b22fa5d72db33e86)   DT\_N |
|  | Node identifier for the root node in the devicetree. |
| #define | [DT\_PATH](#ga015b4819473797982e83cae497697086)(...) |
|  | Get a node identifier for a devicetree path. |
| #define | [DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(label) |
|  | Get a node identifier for a node label. |
| #define | [DT\_ALIAS](#gaa49e19bbc39dc0d6f16b78a5d02482c9)(alias) |
|  | Get a node identifier from /aliases. |
| #define | [DT\_INST](#gae199b930cb21ff38dab284a696093ead)(inst, compat) |
|  | Get a node identifier for an instance of a compatible. |
| #define | [DT\_PARENT](#ga3ac56d491510275ee1321446796ab63b)(node\_id) |
|  | Get a node identifier for a parent node. |
| #define | [DT\_GPARENT](#gaa4eccf276a426cbbc6e440d72b692753)(node\_id) |
|  | Get a node identifier for a grandparent node. |
| #define | [DT\_CHILD](#ga88259608f4e9083ccc2e9ca5ec2c212e)(node\_id, child) |
|  | Get a node identifier for a child node. |
| #define | [DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](#ga4858c378b098dcb7c35de1db25442acc)(compat) |
|  | Get a node identifier for a status okay node with a compatible. |
| #define | [DT\_NODE\_PATH](#gacd79818b99724d834e3bb7ae74ee02cf)(node\_id) |
|  | Get a devicetree node's full path as a string literal. |
| #define | [DT\_NODE\_FULL\_NAME](#ga8a8ab5d12fe59787433d1add94fb1667)(node\_id) |
|  | Get a devicetree node's name with unit-address as a string literal. |
| #define | [DT\_NODE\_CHILD\_IDX](#ga34452788d4fed1fce3e6650d61246866)(node\_id) |
|  | Get a devicetree node's index into its parent's list of children. |
| #define | [DT\_CHILD\_NUM](#ga37cf660c2a7a844f70191d21b6543dc1)(node\_id) |
|  | Get the number of child nodes of a given node. |
| #define | [DT\_CHILD\_NUM\_STATUS\_OKAY](#ga98544b8fd880fdd632f18e2410d39739)(node\_id) |
|  | Get the number of child nodes of a given node which child nodes' status are okay. |
| #define | [DT\_SAME\_NODE](#ga977d0ad58626e3ab906064fdcdace5e6)(node\_id1, node\_id2) |
|  | Do `node_id1` and `node_id2` refer to the same node? |
| #define | [DT\_NODELABEL\_STRING\_ARRAY](#ga0114cbfa3a2075558769d4632b7bb1e9)(node\_id) |
|  | Get a devicetree node's node labels as an array of strings. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaa49e19bbc39dc0d6f16b78a5d02482c9)DT\_ALIAS

| #define DT\_ALIAS | ( |  | *alias* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(DT\_N\_ALIAS\_, alias)

Get a node identifier from /aliases.

This macro's argument is a property of the /aliases node. It returns a node identifier for the node which is aliased. Convert non-alphanumeric characters in the alias property to underscores to form valid C tokens, and lowercase all letters.

Example devicetree fragment:

/ {

aliases {

my-serial = &serial1;

};

soc {

serial1: serial@40001000 {

status = "okay";

current-speed = <115200>;

...

};

};

};

You can use [DT\_ALIAS(my\_serial)](#gaa49e19bbc39dc0d6f16b78a5d02482c9) to get a node identifier for the serial@40001000 node. Notice how my-serial in the devicetree becomes my\_serial in the [DT\_ALIAS()](#gaa49e19bbc39dc0d6f16b78a5d02482c9) argument. Example usage with [DT\_PROP()](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value.") to get the current-speed property:

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_ALIAS](#gaa49e19bbc39dc0d6f16b78a5d02482c9)(my\_serial), current\_speed) // 115200

[DT\_ALIAS](#gaa49e19bbc39dc0d6f16b78a5d02482c9)

#define DT\_ALIAS(alias)

Get a node identifier from /aliases.

**Definition** devicetree.h:240

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:663

Parameters
:   | alias | lowercase-and-underscores alias name. |
    | --- | --- |

Returns
:   node identifier for the node with that alias

## [◆ ](#ga88259608f4e9083ccc2e9ca5ec2c212e)DT\_CHILD

| #define DT\_CHILD | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *child* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(node\_id, DT\_S\_PREFIX(child))

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Get a node identifier for a child node.

Example devicetree fragment:

/ {

soc-label: soc {

serial1: serial@40001000 {

status = "okay";

current-speed = <115200>;

...

};

};

};

Example usage with [DT\_PROP()](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value.") to get the status of the serial@40001000 node:

#define SOC\_NODE DT\_NODELABEL(soc\_label)

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_CHILD](#ga88259608f4e9083ccc2e9ca5ec2c212e)(SOC\_NODE, serial\_40001000), status) // "okay"

[DT\_CHILD](#ga88259608f4e9083ccc2e9ca5ec2c212e)

#define DT\_CHILD(node\_id, child)

Get a node identifier for a child node.

**Definition** devicetree.h:423

Node labels like serial1 cannot be used as the `child` argument to this macro. Use [DT\_NODELABEL()](#gab7d23294a6bf7fd44a98b48ec47d8a79) for that instead.

You can also use [DT\_FOREACH\_CHILD()](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f "Invokes fn for each child of node_id.") to iterate over node identifiers for all of a node's children.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | child | lowercase-and-underscores child node name |

Returns
:   node identifier for the node with the name referred to by 'child'

## [◆ ](#ga37cf660c2a7a844f70191d21b6543dc1)DT\_CHILD\_NUM

| #define DT\_CHILD\_NUM | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_CHILD\_NUM)

Get the number of child nodes of a given node.

Parameters
:   | node\_id | a node identifier |
    | --- | --- |

Returns
:   Number of child nodes

## [◆ ](#ga98544b8fd880fdd632f18e2410d39739)DT\_CHILD\_NUM\_STATUS\_OKAY

| #define DT\_CHILD\_NUM\_STATUS\_OKAY | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_CHILD\_NUM\_STATUS\_OKAY)

Get the number of child nodes of a given node which child nodes' status are okay.

Parameters
:   | node\_id | a node identifier |
    | --- | --- |

Returns
:   Number of child nodes which status are okay

## [◆ ](#ga4858c378b098dcb7c35de1db25442acc)DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY

| #define DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY | ( |  | *compat* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(compat), \

([DT\_INST](#gae199b930cb21ff38dab284a696093ead)(0, compat)), \

([DT\_INVALID\_NODE](#ga710cc4455dd7e738f43f750153163855)))

[DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)

#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat)

Does the devicetree have a status okay node with a compatible?

**Definition** devicetree.h:3406

[DT\_INVALID\_NODE](#ga710cc4455dd7e738f43f750153163855)

#define DT\_INVALID\_NODE

Name for an invalid node identifier.

**Definition** devicetree.h:87

[DT\_INST](#gae199b930cb21ff38dab284a696093ead)

#define DT\_INST(inst, compat)

Get a node identifier for an instance of a compatible.

**Definition** devicetree.h:336

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

Get a node identifier for a status okay node with a compatible.

Use this if you want to get an arbitrary enabled node with a given compatible, and you do not care which one you get. If any enabled nodes with the given compatible exist, a node identifier for one of them is returned. Otherwise, [DT\_INVALID\_NODE](#ga710cc4455dd7e738f43f750153163855) is returned.

Example devicetree fragment:

node-a {

compatible = "vnd,device";

status = "okay";

};

node-b {

compatible = "vnd,device";

status = "okay";

};

node-c {

compatible = "vnd,device";

status = "disabled";

};

Example usage:

[DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](#ga4858c378b098dcb7c35de1db25442acc)(vnd\_device)

[DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](#ga4858c378b098dcb7c35de1db25442acc)

#define DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY(compat)

Get a node identifier for a status okay node with a compatible.

**Definition** devicetree.h:466

This expands to a node identifier for either node-a or node-b. It will not expand to a node identifier for node-c, because that node does not have status okay.

Parameters
:   | compat | lowercase-and-underscores compatible, without quotes |
    | --- | --- |

Returns
:   node identifier for a node with that compatible, or [DT\_INVALID\_NODE](#ga710cc4455dd7e738f43f750153163855)

## [◆ ](#gaa4eccf276a426cbbc6e440d72b692753)DT\_GPARENT

| #define DT\_GPARENT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PARENT](#ga3ac56d491510275ee1321446796ab63b)([DT\_PARENT](#ga3ac56d491510275ee1321446796ab63b)(node\_id))

[DT\_PARENT](#ga3ac56d491510275ee1321446796ab63b)

#define DT\_PARENT(node\_id)

Get a node identifier for a parent node.

**Definition** devicetree.h:361

Get a node identifier for a grandparent node.

Example devicetree fragment:

gparent: grandparent-node {

parent: parent-node {

child: child-node { ... }

};

};

The following are equivalent ways to get the same node identifier:

[DT\_GPARENT](#gaa4eccf276a426cbbc6e440d72b692753)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(child))

[DT\_PARENT](#ga3ac56d491510275ee1321446796ab63b)([DT\_PARENT](#ga3ac56d491510275ee1321446796ab63b)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(child))

[DT\_GPARENT](#gaa4eccf276a426cbbc6e440d72b692753)

#define DT\_GPARENT(node\_id)

Get a node identifier for a grandparent node.

**Definition** devicetree.h:386

[DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:200

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   a node identifier for the node's parent's parent

## [◆ ](#gae199b930cb21ff38dab284a696093ead)DT\_INST

| #define DT\_INST | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *compat* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(DT\_N\_INST, DT\_DASH(inst, compat))

Get a node identifier for an instance of a compatible.

All nodes with a particular compatible property value are assigned instance numbers, which are zero-based indexes specific to that compatible. You can get a node identifier for these nodes by passing [DT\_INST()](#gae199b930cb21ff38dab284a696093ead) an instance number, `inst`, along with the lowercase-and-underscores version of the compatible, `compat`.

Instance numbers have the following properties:

- for each compatible, instance numbers start at 0 and are contiguous
- exactly one instance number is assigned for each node with a compatible, **including disabled nodes**
- enabled nodes (status property is okay or missing) are assigned the instance numbers starting from 0, and disabled nodes have instance numbers which are greater than those of any enabled node

No other guarantees are made. In particular:

- instance numbers **in no way reflect** any numbering scheme that might exist in SoC documentation, node labels or unit addresses, or properties of the /aliases node (use [DT\_NODELABEL()](#gab7d23294a6bf7fd44a98b48ec47d8a79) or [DT\_ALIAS()](#gaa49e19bbc39dc0d6f16b78a5d02482c9) for those)
- there **is no general guarantee** that the same node will have the same instance number between builds, even if you are building the same application again in the same build directory

Example devicetree fragment:

serial1: serial@40001000 {

compatible = "vnd,soc-serial";

status = "disabled";

current-speed = <9600>;

...

};

serial2: serial@40002000 {

compatible = "vnd,soc-serial";

status = "okay";

current-speed = <57600>;

...

};

serial3: serial@40003000 {

compatible = "vnd,soc-serial";

current-speed = <115200>;

...

};

Assuming no other nodes in the devicetree have compatible "vnd,soc-serial", that compatible has nodes with instance numbers 0, 1, and 2.

The nodes serial@40002000 and serial@40003000 are both enabled, so their instance numbers are 0 and 1, but no guarantees are made regarding which node has which instance number.

Since serial@40001000 is the only disabled node, it has instance number 2, since disabled nodes are assigned the largest instance numbers. Therefore:

// Could be 57600 or 115200. There is no way to be sure:

// either serial@40002000 or serial@40003000 could

// have instance number 0, so this could be the current-speed

// property of either of those nodes.

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_INST](#gae199b930cb21ff38dab284a696093ead)(0, vnd\_soc\_serial), current\_speed)

// Could be 57600 or 115200, for the same reason.

// If the above expression expands to 57600, then

// this expands to 115200, and vice-versa.

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_INST](#gae199b930cb21ff38dab284a696093ead)(1, vnd\_soc\_serial), current\_speed)

// 9600, because there is only one disabled node, and

// disabled nodes are "at the end" of the instance

// number "list".

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_INST](#gae199b930cb21ff38dab284a696093ead)(2, vnd\_soc\_serial), current\_speed)

Notice how "vnd,soc-serial" in the devicetree becomes vnd\_soc\_serial (without quotes) in the [DT\_INST()](#gae199b930cb21ff38dab284a696093ead) arguments. (As usual, current-speed in the devicetree becomes current\_speed as well.)

Nodes whose compatible property has multiple values are assigned independent instance numbers for each compatible.

Parameters
:   | inst | instance number for compatible `compat` |
    | --- | --- |
    | compat | lowercase-and-underscores compatible, without quotes |

Returns
:   node identifier for the node with that instance number and compatible

## [◆ ](#ga710cc4455dd7e738f43f750153163855)DT\_INVALID\_NODE

| #define DT\_INVALID\_NODE   \_ |
| --- |

`#include <[devicetree.h](devicetree_8h.md)>`

Name for an invalid node identifier.

This supports cases where factored macros can be invoked from paths where devicetree data may or may not be available. It is a preprocessor identifier that does not match any valid devicetree node identifier.

## [◆ ](#ga34452788d4fed1fce3e6650d61246866)DT\_NODE\_CHILD\_IDX

| #define DT\_NODE\_CHILD\_IDX | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_CHILD\_IDX)

Get a devicetree node's index into its parent's list of children.

Indexes are zero-based.

It is an error to use this macro with the root node.

Example devicetree fragment:

parent {

c1: child-1 {};

c2: child-2 {};

};

Example usage:

[DT\_NODE\_CHILD\_IDX](#ga34452788d4fed1fce3e6650d61246866)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(c1)) // 0

[DT\_NODE\_CHILD\_IDX](#ga34452788d4fed1fce3e6650d61246866)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(c2)) // 1

[DT\_NODE\_CHILD\_IDX](#ga34452788d4fed1fce3e6650d61246866)

#define DT\_NODE\_CHILD\_IDX(node\_id)

Get a devicetree node's index into its parent's list of children.

**Definition** devicetree.h:552

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the node's index in its parent node's list of children

## [◆ ](#ga8a8ab5d12fe59787433d1add94fb1667)DT\_NODE\_FULL\_NAME

| #define DT\_NODE\_FULL\_NAME | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FULL\_NAME)

Get a devicetree node's name with unit-address as a string literal.

This returns the node name and unit-address from a node identifier.

Example devicetree fragment:

/ {

soc {

node: my-node@12345678 { ... };

};

};

Example usage:

[DT\_NODE\_FULL\_NAME](#ga8a8ab5d12fe59787433d1add94fb1667)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(node)) // "my-node@12345678"

[DT\_NODE\_FULL\_NAME](#ga8a8ab5d12fe59787433d1add94fb1667)

#define DT\_NODE\_FULL\_NAME(node\_id)

Get a devicetree node's name with unit-address as a string literal.

**Definition** devicetree.h:524

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the node's name with unit-address as a string in the devicetree

## [◆ ](#gacd79818b99724d834e3bb7ae74ee02cf)DT\_NODE\_PATH

| #define DT\_NODE\_PATH | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_PATH)

Get a devicetree node's full path as a string literal.

This returns the path to a node from a node identifier. To get a node identifier from path components instead, use [DT\_PATH()](#ga015b4819473797982e83cae497697086).

Example devicetree fragment:

/ {

soc {

node: my-node@12345678 { ... };

};

};

Example usage:

[DT\_NODE\_PATH](#gacd79818b99724d834e3bb7ae74ee02cf)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(node)) // "/soc/my-node@12345678"

[DT\_NODE\_PATH](#gacd79818b99724d834e3bb7ae74ee02cf)([DT\_PATH](#ga015b4819473797982e83cae497697086)(soc)) // "/soc"

[DT\_NODE\_PATH](#gacd79818b99724d834e3bb7ae74ee02cf)([DT\_ROOT](#gad65aa36621281687b22fa5d72db33e86)) // "/"

[DT\_PATH](#ga015b4819473797982e83cae497697086)

#define DT\_PATH(...)

Get a node identifier for a devicetree path.

**Definition** devicetree.h:144

[DT\_NODE\_PATH](#gacd79818b99724d834e3bb7ae74ee02cf)

#define DT\_NODE\_PATH(node\_id)

Get a devicetree node's full path as a string literal.

**Definition** devicetree.h:498

[DT\_ROOT](#gad65aa36621281687b22fa5d72db33e86)

#define DT\_ROOT

Node identifier for the root node in the devicetree.

**Definition** devicetree.h:92

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   the node's full path in the devicetree

## [◆ ](#gab7d23294a6bf7fd44a98b48ec47d8a79)DT\_NODELABEL

| #define DT\_NODELABEL | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(DT\_N\_NODELABEL\_, label)

Get a node identifier for a node label.

Convert non-alphanumeric characters in the node label to underscores to form valid C tokens, and lowercase all letters. Note that node labels are not the same thing as label properties.

Example devicetree fragment:

serial1: serial@40001000 {

label = "UART\_0";

status = "okay";

current-speed = <115200>;

...

};

The only node label in this example is serial1.

The string UART\_0 is *not* a node label; it's the value of a property named label.

You can use [DT\_NODELABEL(serial1)](#gab7d23294a6bf7fd44a98b48ec47d8a79) to get a node identifier for the serial@40001000 node. Example usage with [DT\_PROP()](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value.") to get the current-speed property:

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(serial1), current\_speed) // 115200

Another example devicetree fragment:

cpu@0 {

L2\_0: l2-cache {

cache-level = <2>;

...

};

};

Example usage to get the cache-level property:

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(l2\_0), cache\_level) // 2

Notice how L2\_0 in the devicetree is lowercased to l2\_0 in the [DT\_NODELABEL()](#gab7d23294a6bf7fd44a98b48ec47d8a79) argument.

Parameters
:   | label | lowercase-and-underscores node label name |
    | --- | --- |

Returns
:   node identifier for the node with that label

## [◆ ](#ga0114cbfa3a2075558769d4632b7bb1e9)DT\_NODELABEL\_STRING\_ARRAY

| #define DT\_NODELABEL\_STRING\_ARRAY | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

{ [DT\_FOREACH\_NODELABEL](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0)(node\_id, DT\_NODELABEL\_STRING\_ARRAY\_ENTRY\_INTERNAL) }

[DT\_FOREACH\_NODELABEL](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0)

#define DT\_FOREACH\_NODELABEL(node\_id, fn)

Invokes fn for each node label of a given node.

**Definition** devicetree.h:3295

Get a devicetree node's node labels as an array of strings.

Example devicetree fragment:

foo: bar: node@deadbeef {};

Example usage:

[DT\_NODELABEL\_STRING\_ARRAY](#ga0114cbfa3a2075558769d4632b7bb1e9)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(foo))

[DT\_NODELABEL\_STRING\_ARRAY](#ga0114cbfa3a2075558769d4632b7bb1e9)

#define DT\_NODELABEL\_STRING\_ARRAY(node\_id)

Get a devicetree node's node labels as an array of strings.

**Definition** devicetree.h:620

This expands to:

{ "foo", "bar", }

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   an array initializer for an array of the node's node labels as strings

## [◆ ](#ga3ac56d491510275ee1321446796ab63b)DT\_PARENT

| #define DT\_PARENT | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_PARENT)

Get a node identifier for a parent node.

Example devicetree fragment:

parent: parent-node {

child: child-node {

...

};

};

The following are equivalent ways to get the same node identifier:

[DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(parent)

[DT\_PARENT](#ga3ac56d491510275ee1321446796ab63b)([DT\_NODELABEL](#gab7d23294a6bf7fd44a98b48ec47d8a79)(child))

Parameters
:   | node\_id | node identifier |
    | --- | --- |

Returns
:   a node identifier for the node's parent

## [◆ ](#ga015b4819473797982e83cae497697086)DT\_PATH

| #define DT\_PATH | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_PATH\_INTERNAL(\_\_VA\_ARGS\_\_)

Get a node identifier for a devicetree path.

Note
:   This macro returns a node identifier from path components. To get a path string from a node identifier, use [DT\_NODE\_PATH()](#gacd79818b99724d834e3bb7ae74ee02cf) instead.

The arguments to this macro are the names of non-root nodes in the tree required to reach the desired node, starting from the root. Non-alphanumeric characters in each name must be converted to underscores to form valid C tokens, and letters must be lowercased.

Example devicetree fragment:

/ {

soc {

serial1: serial@40001000 {

status = "okay";

current-speed = <115200>;

...

};

};

};

You can use [DT\_PATH(soc, serial\_40001000)](#ga015b4819473797982e83cae497697086) to get a node identifier for the serial@40001000 node. Node labels like serial1 cannot be used as [DT\_PATH()](#ga015b4819473797982e83cae497697086) arguments; use [DT\_NODELABEL()](#gab7d23294a6bf7fd44a98b48ec47d8a79) for those instead.

Example usage with [DT\_PROP()](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value.") to get the current-speed property:

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_PATH](#ga015b4819473797982e83cae497697086)(soc, serial\_40001000), current\_speed) // 115200

(The current-speed property is also in lowercase-and-underscores form when used with this API.)

When determining arguments to [DT\_PATH()](#ga015b4819473797982e83cae497697086):

- the first argument corresponds to a child node of the root (soc above)
- a second argument corresponds to a child of the first argument (serial\_40001000 above, from the node name serial@40001000 after lowercasing and changing @ to \_)
- and so on for deeper nodes in the desired node's path

Parameters
:   | ... | lowercase-and-underscores node names along the node's path, with each name given as a separate argument |
    | --- | --- |

Returns
:   node identifier for the node with that path

## [◆ ](#gad65aa36621281687b22fa5d72db33e86)DT\_ROOT

| #define DT\_ROOT   DT\_N |
| --- |

`#include <[devicetree.h](devicetree_8h.md)>`

Node identifier for the root node in the devicetree.

## [◆ ](#ga977d0ad58626e3ab906064fdcdace5e6)DT\_SAME\_NODE

| #define DT\_SAME\_NODE | ( |  | *node\_id1*, |
| --- | --- | --- | --- |
|  |  |  | *node\_id2* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

([DT\_DEP\_ORD](group__devicetree-dep-ord.md#ga5b96dccfd349dd0ddba1812aa942c1bd)(node\_id1) == ([DT\_DEP\_ORD](group__devicetree-dep-ord.md#ga5b96dccfd349dd0ddba1812aa942c1bd)(node\_id2)))

[DT\_DEP\_ORD](group__devicetree-dep-ord.md#ga5b96dccfd349dd0ddba1812aa942c1bd)

#define DT\_DEP\_ORD(node\_id)

Get a node's dependency ordinal.

**Definition** ordinals.h:25

Do `node_id1` and `node_id2` refer to the same node?

Both `node_id1` and `node_id2` must be node identifiers for nodes that exist in the devicetree (if unsure, you can check with [DT\_NODE\_EXISTS()](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a "Does a node identifier refer to a node?")).

The expansion evaluates to 0 or 1, but may not be a literal integer 0 or 1.

Parameters
:   | node\_id1 | first node identifier |
    | --- | --- |
    | node\_id2 | second node identifier |

Returns
:   an expression that evaluates to 1 if the node identifiers refer to the same node, and evaluates to 0 otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
