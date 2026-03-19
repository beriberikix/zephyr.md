---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__devicetree-generic-foreach.html
original_path: doxygen/html/group__devicetree-generic-foreach.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

"For-each" macros

[Devicetree](group__devicetree.md)

IMPORTANT: you can't use the DT for-each macros in their own expansions.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [DT\_FOREACH\_NODE](#gad27b29ae71a3d3294984fd3bc721121d)(fn) |
|  | Invokes `fn` for every node in the tree. |
| #define | [DT\_FOREACH\_NODE\_VARGS](#ga4e708120bf839568b1215a6c21c54eed)(fn, ...) |
|  | Invokes `fn` for every node in the tree with multiple arguments. |
| #define | [DT\_FOREACH\_STATUS\_OKAY\_NODE](#ga926f68202042c9db05390e628787f916)(fn) |
|  | Invokes `fn` for every status okay node in the tree. |
| #define | [DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS](#ga9aa3ee2b90a4ec30621597f4d1448c51)(fn, ...) |
|  | Invokes `fn` for every status okay node in the tree with multiple arguments. |
| #define | [DT\_FOREACH\_ANCESTOR](#gac4f9fee38bffbd5d315d386fe3c7bc91)(node\_id, fn) |
|  | Invokes `fn` for each ancestor of `node_id`. |
| #define | [DT\_FOREACH\_CHILD](#ga2f4eead8e8190110f5c0eb353e6a408f)(node\_id, fn) |
|  | Invokes `fn` for each child of `node_id`. |
| #define | [DT\_FOREACH\_CHILD\_SEP](#ga1fbeb335d66745803dbf7a185bf10afc)(node\_id, fn, sep) |
|  | Invokes `fn` for each child of `node_id` with a separator. |
| #define | [DT\_FOREACH\_CHILD\_VARGS](#gae7461e9fa4687bf88cdd7c76f30986de)(node\_id, fn, ...) |
|  | Invokes `fn` for each child of `node_id` with multiple arguments. |
| #define | [DT\_FOREACH\_CHILD\_SEP\_VARGS](#ga0042485aef7caaa48fa252b76a6629aa)(node\_id, fn, sep, ...) |
|  | Invokes `fn` for each child of `node_id` with separator and multiple arguments. |
| #define | [DT\_FOREACH\_CHILD\_STATUS\_OKAY](#gae907df926b94f1da52b1ab701392f3bd)(node\_id, fn) |
|  | Call `fn` on the child nodes with status okay. |
| #define | [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP](#ga97414c01ebbb6df5ee2862c0ee9d44ce)(node\_id, fn, sep) |
|  | Call `fn` on the child nodes with status okay with separator. |
| #define | [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS](#ga8bbf6992e5f90d8a28035ea6211dd2a3)(node\_id, fn, ...) |
|  | Call `fn` on the child nodes with status okay with multiple arguments. |
| #define | [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS](#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)(node\_id, fn, sep, ...) |
|  | Call `fn` on the child nodes with status okay with separator and multiple arguments. |
| #define | [DT\_FOREACH\_PROP\_ELEM](#ga118a0477ab297a1bda9e16acf556babc)(node\_id, prop, fn) |
|  | Invokes `fn` for each element in the value of property `prop`. |
| #define | [DT\_FOREACH\_PROP\_ELEM\_SEP](#ga72d0b6859b4fc61cde518aee118d9ed8)(node\_id, prop, fn, sep) |
|  | Invokes `fn` for each element in the value of property `prop` with separator. |
| #define | [DT\_FOREACH\_PROP\_ELEM\_VARGS](#gaae36970d49c860414374c76e136a9607)(node\_id, prop, fn, ...) |
|  | Invokes `fn` for each element in the value of property `prop` with multiple arguments. |
| #define | [DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS](#ga29120ee8718b889273dc2649ab25438f)(node\_id, prop, fn, sep, ...) |
|  | Invokes `fn` for each element in the value of property `prop` with multiple arguments and a separator. |
| #define | [DT\_FOREACH\_STATUS\_OKAY](#ga52b34316d269cc8d8ef2244d3ca460b8)(compat, fn) |
|  | Invokes `fn` for each status okay node of a compatible. |
| #define | [DT\_FOREACH\_STATUS\_OKAY\_VARGS](#ga99cf30d6cf4847ed99ba7d81ad2b49d0)(compat, fn, ...) |
|  | Invokes `fn` for each status okay node of a compatible with multiple arguments. |
| #define | [DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS](#ga368d08572b01efacdad370e6ceb515f9)(compat, fn, ...) |
|  | Call `fn` on all nodes with compatible compat and status okay with multiple arguments. |
| #define | [DT\_FOREACH\_NODELABEL](#gad5585436896efc4c5154a93b5980d3b0)(node\_id, fn) |
|  | Invokes `fn` for each node label of a given node. |
| #define | [DT\_FOREACH\_NODELABEL\_VARGS](#ga2a88abdb46158bcf36a8c976a1e2186d)(node\_id, fn, ...) |
|  | Invokes `fn` for each node label of a given node with multiple arguments. |

## Detailed Description

IMPORTANT: you can't use the DT for-each macros in their own expansions.

For example, something like this won't work the way you might expect:

#define FOO(node\_id) [...] DT\_FOREACH\_NODE(...) [...]

[DT\_FOREACH\_NODE](#gad27b29ae71a3d3294984fd3bc721121d)(FOO)

[DT\_FOREACH\_NODE](#gad27b29ae71a3d3294984fd3bc721121d)

#define DT\_FOREACH\_NODE(fn)

Invokes fn for every node in the tree.

**Definition** devicetree.h:2973

In this example, the C preprocessor won't expand the [DT\_FOREACH\_NODE()](#gad27b29ae71a3d3294984fd3bc721121d) macro inside of FOO() while it's already expanding [DT\_FOREACH\_NODE()](#gad27b29ae71a3d3294984fd3bc721121d) at the top level of the file.

This is true of any macro, not just [DT\_FOREACH\_NODE()](#gad27b29ae71a3d3294984fd3bc721121d). The C language works this way to avoid infinite recursions inside of macro expansions.

If you need to "nest" calls to one of these macros, you can work around this preprocessor limitation by using a different, related macro instead, like this:

#define BAR(node\_id) [...] DT\_FOREACH\_NODE\_VARGS(...) [...]

[DT\_FOREACH\_NODE](#gad27b29ae71a3d3294984fd3bc721121d)(BAR)

Here, we use [DT\_FOREACH\_NODE\_VARGS()](#ga4e708120bf839568b1215a6c21c54eed) "inside" BAR() "inside" [DT\_FOREACH\_NODE()](#gad27b29ae71a3d3294984fd3bc721121d). Because of this, the preprocessor will expand both [DT\_FOREACH\_NODE\_VARGS()](#ga4e708120bf839568b1215a6c21c54eed) and [DT\_FOREACH\_NODE()](#gad27b29ae71a3d3294984fd3bc721121d) as expected.

## Macro Definition Documentation

## [◆ ](#ga368d08572b01efacdad370e6ceb515f9)DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS

| #define DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS | ( |  | *compat*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(compat), \

([UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(DT\_FOREACH\_OKAY\_INST\_VARGS\_, \

compat)(fn, compat, \_\_VA\_ARGS\_\_)), \

())

[DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)

#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat)

Does the devicetree have a status okay node with a compatible?

**Definition** devicetree.h:3711

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Call `fn` on all nodes with compatible compat and status okay with multiple arguments.

Parameters
:   | compat | lowercase-and-underscores devicetree compatible |
    | --- | --- |
    | fn | Macro to call for each enabled node. Must accept a devicetree compatible and instance number. |
    | ... | Additional arguments to pass to `fn` |

See also
:   [DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-inst.md#ga1b9fd4b9c37a23e52e69ea23f7aedb38 "Call fn on all nodes with compatible DT_DRV_COMPAT and status okay with multiple arguments.")

## [◆ ](#gac4f9fee38bffbd5d315d386fe3c7bc91)DT\_FOREACH\_ANCESTOR

| #define DT\_FOREACH\_ANCESTOR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_ANCESTOR)(fn)

Invokes `fn` for each ancestor of `node_id`.

The macro `fn` must take one parameter, which will be the identifier of a child node of `node_id` to enable traversal of all ancestor nodes.

The ancestor will be iterated over in the same order as they appear in the final devicetree.

Example devicetree fragment:

n: node1 {

foobar = "foo1";

n\_2: node2 {

foobar = "foo2";

n\_3: node3 {

foobar = "foo3";

};

};

};

Example usage:

#define GET\_PROP(n) DT\_PROP(n, foobar),

const char \*ancestor\_names[] = {

[DT\_FOREACH\_ANCESTOR](#gac4f9fee38bffbd5d315d386fe3c7bc91)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n\_3), GET\_PROP)

};

[DT\_FOREACH\_ANCESTOR](#gac4f9fee38bffbd5d315d386fe3c7bc91)

#define DT\_FOREACH\_ANCESTOR(node\_id, fn)

Invokes fn for each ancestor of node\_id.

**Definition** devicetree.h:3064

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

This expands to:

const char \*ancestor\_names[] = {

"foo2", "foo1",

};

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |

## [◆ ](#ga2f4eead8e8190110f5c0eb353e6a408f)DT\_FOREACH\_CHILD

| #define DT\_FOREACH\_CHILD | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_CHILD)(fn)

Invokes `fn` for each child of `node_id`.

The macro `fn` must take one parameter, which will be the node identifier of a child node of `node_id`.

The children will be iterated over in the same order as they appear in the final devicetree.

Example devicetree fragment:

n: node {

child-1 {

foobar = "foo";

};

child-2 {

foobar = "bar";

};

};

Example usage:

#define FOOBAR\_AND\_COMMA(node\_id) DT\_PROP(node\_id, foobar),

const char \*child\_foobars[] = {

[DT\_FOREACH\_CHILD](#ga2f4eead8e8190110f5c0eb353e6a408f)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), FOOBAR\_AND\_COMMA)

};

[DT\_FOREACH\_CHILD](#ga2f4eead8e8190110f5c0eb353e6a408f)

#define DT\_FOREACH\_CHILD(node\_id, fn)

Invokes fn for each child of node\_id.

**Definition** devicetree.h:3110

This expands to:

const char \*child\_foobars[] = {

"foo", "bar",

};

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |

## [◆ ](#ga1fbeb335d66745803dbf7a185bf10afc)DT\_FOREACH\_CHILD\_SEP

| #define DT\_FOREACH\_CHILD\_SEP | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | *sep* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP)(fn, sep)

Invokes `fn` for each child of `node_id` with a separator.

The macro `fn` must take one parameter, which will be the node identifier of a child node of `node_id`.

Example devicetree fragment:

n: node {

child-1 {

...

};

child-2 {

...

};

};

Example usage:

const char \*child\_names[] = {

[DT\_FOREACH\_CHILD\_SEP](#ga1fbeb335d66745803dbf7a185bf10afc)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), [DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667), (,))

};

[DT\_FOREACH\_CHILD\_SEP](#ga1fbeb335d66745803dbf7a185bf10afc)

#define DT\_FOREACH\_CHILD\_SEP(node\_id, fn, sep)

Invokes fn for each child of node\_id with a separator.

**Definition** devicetree.h:3153

[DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)

#define DT\_NODE\_FULL\_NAME(node\_id)

Get a devicetree node's name with unit-address as a string literal.

**Definition** devicetree.h:537

This expands to:

const char \*child\_names[] = {

"child-1", "child-2"

};

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |

## [◆ ](#ga0042485aef7caaa48fa252b76a6629aa)DT\_FOREACH\_CHILD\_SEP\_VARGS

| #define DT\_FOREACH\_CHILD\_SEP\_VARGS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_CHILD\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

Invokes `fn` for each child of `node_id` with separator and multiple arguments.

The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_FOREACH\_CHILD\_VARGS](#gae7461e9fa4687bf88cdd7c76f30986de)

## [◆ ](#gae907df926b94f1da52b1ab701392f3bd)DT\_FOREACH\_CHILD\_STATUS\_OKAY

| #define DT\_FOREACH\_CHILD\_STATUS\_OKAY | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY)(fn)

Call `fn` on the child nodes with status okay.

The macro `fn` should take one argument, which is the node identifier for the child node.

As usual, both a missing status and an ok status are treated as okay.

The children will be iterated over in the same order as they appear in the final devicetree.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |

## [◆ ](#ga97414c01ebbb6df5ee2862c0ee9d44ce)DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP

| #define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | *sep* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP)(fn, sep)

Call `fn` on the child nodes with status okay with separator.

The macro `fn` should take one argument, which is the node identifier for the child node.

As usual, both a missing status and an ok status are treated as okay.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |

See also
:   [DT\_FOREACH\_CHILD\_STATUS\_OKAY](#gae907df926b94f1da52b1ab701392f3bd)

## [◆ ](#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS

| #define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS)(fn, sep, \_\_VA\_ARGS\_\_)

Call `fn` on the child nodes with status okay with separator and multiple arguments.

The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

As usual, both a missing status and an ok status are treated as okay.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | variable number of arguments to pass to `fn` |

See also
:   DT\_FOREACH\_CHILD\_SEP\_STATUS\_OKAY

## [◆ ](#ga8bbf6992e5f90d8a28035ea6211dd2a3)DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS

| #define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS)(fn, \_\_VA\_ARGS\_\_)

Call `fn` on the child nodes with status okay with multiple arguments.

The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

As usual, both a missing status and an ok status are treated as okay.

The children will be iterated over in the same order as they appear in the final devicetree.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_FOREACH\_CHILD\_STATUS\_OKAY](#gae907df926b94f1da52b1ab701392f3bd)

## [◆ ](#gae7461e9fa4687bf88cdd7c76f30986de)DT\_FOREACH\_CHILD\_VARGS

| #define DT\_FOREACH\_CHILD\_VARGS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_CHILD\_VARGS)(fn, \_\_VA\_ARGS\_\_)

Invokes `fn` for each child of `node_id` with multiple arguments.

The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

The children will be iterated over in the same order as they appear in the final devicetree.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | fn | macro to invoke |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_FOREACH\_CHILD](#ga2f4eead8e8190110f5c0eb353e6a408f)

## [◆ ](#gad27b29ae71a3d3294984fd3bc721121d)DT\_FOREACH\_NODE

| #define DT\_FOREACH\_NODE | ( |  | *fn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_FOREACH\_HELPER(fn)

Invokes `fn` for every node in the tree.

The macro `fn` must take one parameter, which will be a node identifier. The macro is expanded once for each node in the tree. The order that nodes are visited in is not specified.

Parameters
:   | fn | macro to invoke |
    | --- | --- |

## [◆ ](#ga4e708120bf839568b1215a6c21c54eed)DT\_FOREACH\_NODE\_VARGS

| #define DT\_FOREACH\_NODE\_VARGS | ( |  | *fn*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_FOREACH\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

Invokes `fn` for every node in the tree with multiple arguments.

The macro `fn` takes multiple arguments. The first should be the node identifier for the node. The remaining are passed-in by the caller.

The macro is expanded once for each node in the tree. The order that nodes are visited in is not specified.

Parameters
:   | fn | macro to invoke |
    | --- | --- |
    | ... | variable number of arguments to pass to `fn` |

## [◆ ](#gad5585436896efc4c5154a93b5980d3b0)DT\_FOREACH\_NODELABEL

| #define DT\_FOREACH\_NODELABEL | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_NODELABEL)(fn)

Invokes `fn` for each node label of a given node.

The order of the node labels in this macro's expansion matches the order in the final devicetree, with duplicates removed.

Node labels are passed to `fn` as tokens. Note that devicetree node labels are always valid C tokens (see "6.2 Labels" in Devicetree Specification v0.4 for details). The node labels are passed as tokens to `fn` as-is, without any lowercasing or conversion of special characters to underscores.

Example devicetree fragment:

foo: bar: FOO: node@deadbeef {};

Example usage:

int foo = 1;

int bar = 2;

int FOO = 3;

#define FN(nodelabel) + nodelabel

int sum = 0 [DT\_FOREACH\_NODELABEL](#gad5585436896efc4c5154a93b5980d3b0)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(foo), FN)

[DT\_FOREACH\_NODELABEL](#gad5585436896efc4c5154a93b5980d3b0)

#define DT\_FOREACH\_NODELABEL(node\_id, fn)

Invokes fn for each node label of a given node.

**Definition** devicetree.h:3578

This expands to:

int sum = 0 + 1 + 2 + 3;

Parameters
:   | node\_id | node identifier whose node labels to use |
    | --- | --- |
    | fn | macro which will be passed each node label in order |

## [◆ ](#ga2a88abdb46158bcf36a8c976a1e2186d)DT\_FOREACH\_NODELABEL\_VARGS

| #define DT\_FOREACH\_NODELABEL\_VARGS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT(node\_id, \_FOREACH\_NODELABEL\_VARGS)(fn, \_\_VA\_ARGS\_\_)

Invokes `fn` for each node label of a given node with multiple arguments.

This is like [DT\_FOREACH\_NODELABEL()](#gad5585436896efc4c5154a93b5980d3b0) except you can also pass additional arguments to `fn`.

Example devicetree fragment:

foo: bar: node@deadbeef {};

Example usage:

int foo = 0;

int bar = 1;

#define VAR\_PLUS(nodelabel, to\_add) int nodelabel ## \_added = nodelabel + to\_add;

[DT\_FOREACH\_NODELABEL\_VARGS](#ga2a88abdb46158bcf36a8c976a1e2186d)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(foo), VAR\_PLUS, 1)

[DT\_FOREACH\_NODELABEL\_VARGS](#ga2a88abdb46158bcf36a8c976a1e2186d)

#define DT\_FOREACH\_NODELABEL\_VARGS(node\_id, fn,...)

Invokes fn for each node label of a given node with multiple arguments.

**Definition** devicetree.h:3617

This expands to:

int foo = 0;

int bar = 1;

int foo\_added = foo + 1;

int bar\_added = bar + 1;

Parameters
:   | node\_id | node identifier whose node labels to use |
    | --- | --- |
    | fn | macro which will be passed each node label in order |
    | ... | additional arguments to pass to `fn` |

## [◆ ](#ga118a0477ab297a1bda9e16acf556babc)DT\_FOREACH\_PROP\_ELEM

| #define DT\_FOREACH\_PROP\_ELEM | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM)(fn)

Invokes `fn` for each element in the value of property `prop`.

The macro `fn` must take three parameters: fn(node\_id, prop, idx). `node_id` and `prop` are the same as what is passed to [DT\_FOREACH\_PROP\_ELEM()](#ga118a0477ab297a1bda9e16acf556babc), and `idx` is the current index into the array. The `idx` values are integer literals starting from 0.

The `prop` argument must refer to a property that can be passed to [DT\_PROP\_LEN()](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6 "Get a property's logical length.").

Example devicetree fragment:

n: node {

my-ints = <1 2 3>;

};

Example usage:

#define TIMES\_TWO(node\_id, prop, idx) \

(2 \* DT\_PROP\_BY\_IDX(node\_id, prop, idx)),

int array[] = {

[DT\_FOREACH\_PROP\_ELEM](#ga118a0477ab297a1bda9e16acf556babc)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), my\_ints, TIMES\_TWO)

};

[DT\_FOREACH\_PROP\_ELEM](#ga118a0477ab297a1bda9e16acf556babc)

#define DT\_FOREACH\_PROP\_ELEM(node\_id, prop, fn)

Invokes fn for each element in the value of property prop.

**Definition** devicetree.h:3322

This expands to:

int array[] = {

(2 \* 1), (2 \* 2), (2 \* 3),

};

In general, this macro expands to:

```
fn(node_id, prop, 0) fn(node_id, prop, 1) [...] fn(node_id, prop, n-1)
```

where n is the number of elements in `prop`, as it would be returned by [DT\_PROP\_LEN(node\_id, prop)](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6 "Get a property's logical length.").

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | fn | macro to invoke |

See also
:   [DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6 "Get a property's logical length.")

## [◆ ](#ga72d0b6859b4fc61cde518aee118d9ed8)DT\_FOREACH\_PROP\_ELEM\_SEP

| #define DT\_FOREACH\_PROP\_ELEM\_SEP | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *fn*, |
|  |  |  | *sep* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP)(fn, sep)

Invokes `fn` for each element in the value of property `prop` with separator.

Example devicetree fragment:

n: node {

my-gpios = <&gpioa 0 GPIO\_ACTICE\_HIGH>,

<&gpiob 1 GPIO\_ACTIVE\_HIGH>;

};

Example usage:

struct [gpio\_dt\_spec](structgpio__dt__spec.md) specs[] = {

[DT\_FOREACH\_PROP\_ELEM\_SEP](#ga72d0b6859b4fc61cde518aee118d9ed8)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), my\_gpios,

[GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf), (,))

};

[DT\_FOREACH\_PROP\_ELEM\_SEP](#ga72d0b6859b4fc61cde518aee118d9ed8)

#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep)

Invokes fn for each element in the value of property prop with separator.

**Definition** devicetree.h:3367

[GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx)

Static initializer for a gpio\_dt\_spec.

**Definition** gpio.h:332

[gpio\_dt\_spec](structgpio__dt__spec.md)

Container for GPIO pin information specified in devicetree.

**Definition** gpio.h:289

This expands as a first step to:

struct [gpio\_dt\_spec](structgpio__dt__spec.md) specs[] = {

[GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), my\_gpios, 0),

[GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n), my\_gpios, 1)

};

The `prop` parameter has the same restrictions as the same parameter given to [DT\_FOREACH\_PROP\_ELEM()](#ga118a0477ab297a1bda9e16acf556babc).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | fn | macro to invoke |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |

See also
:   [DT\_FOREACH\_PROP\_ELEM](#ga118a0477ab297a1bda9e16acf556babc)

## [◆ ](#ga29120ee8718b889273dc2649ab25438f)DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS

| #define DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *fn*, |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_SEP\_VARGS)( \

fn, sep, \_\_VA\_ARGS\_\_)

Invokes `fn` for each element in the value of property `prop` with multiple arguments and a separator.

The `prop` parameter has the same restrictions as the same parameter given to [DT\_FOREACH\_PROP\_ELEM()](#ga118a0477ab297a1bda9e16acf556babc).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | fn | macro to invoke |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | variable number of arguments to pass to fn |

See also
:   [DT\_FOREACH\_PROP\_ELEM\_VARGS](#gaae36970d49c860414374c76e136a9607)

## [◆ ](#gaae36970d49c860414374c76e136a9607)DT\_FOREACH\_PROP\_ELEM\_VARGS

| #define DT\_FOREACH\_PROP\_ELEM\_VARGS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_P\_, prop, \_FOREACH\_PROP\_ELEM\_VARGS)(fn, \_\_VA\_ARGS\_\_)

Invokes `fn` for each element in the value of property `prop` with multiple arguments.

The macro `fn` must take multiple parameters: fn(node\_id, prop, idx, ...). `node_id` and `prop` are the same as what is passed to [DT\_FOREACH\_PROP\_ELEM()](#ga118a0477ab297a1bda9e16acf556babc), and `idx` is the current index into the array. The `idx` values are integer literals starting from 0. The remaining arguments are passed-in by the caller.

The `prop` parameter has the same restrictions as the same parameter given to [DT\_FOREACH\_PROP\_ELEM()](#ga118a0477ab297a1bda9e16acf556babc).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | fn | macro to invoke |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_FOREACH\_PROP\_ELEM](#ga118a0477ab297a1bda9e16acf556babc)

## [◆ ](#ga52b34316d269cc8d8ef2244d3ca460b8)DT\_FOREACH\_STATUS\_OKAY

| #define DT\_FOREACH\_STATUS\_OKAY | ( |  | *compat*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(compat), \

([UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(DT\_FOREACH\_OKAY\_, compat)(fn)), \

())

Invokes `fn` for each status okay node of a compatible.

This macro expands to:

```
fn(node_id_1) fn(node_id_2) ... fn(node_id_n)
```

where each node\_id\_<i> is a node identifier for some node with compatible `compat` and status okay. Whitespace is added between expansions as shown above.

Example devicetree fragment:

/ {

a {

compatible = "foo";

status = "okay";

};

b {

compatible = "foo";

status = "disabled";

};

c {

compatible = "foo";

};

};

Example usage:

[DT\_FOREACH\_STATUS\_OKAY](#ga52b34316d269cc8d8ef2244d3ca460b8)(foo, [DT\_NODE\_PATH](group__devicetree-generic-id.md#gacd79818b99724d834e3bb7ae74ee02cf))

[DT\_FOREACH\_STATUS\_OKAY](#ga52b34316d269cc8d8ef2244d3ca460b8)

#define DT\_FOREACH\_STATUS\_OKAY(compat, fn)

Invokes fn for each status okay node of a compatible.

**Definition** devicetree.h:3466

[DT\_NODE\_PATH](group__devicetree-generic-id.md#gacd79818b99724d834e3bb7ae74ee02cf)

#define DT\_NODE\_PATH(node\_id)

Get a devicetree node's full path as a string literal.

**Definition** devicetree.h:511

This expands to one of the following:

```
"/a" "/c"
"/c" "/a"
```

"One of the following" is because no guarantees are made about the order that node identifiers are passed to `fn` in the expansion.

(The /c string literal is present because a missing status property is always treated as if the status were set to okay.)

Note also that `fn` is responsible for adding commas, semicolons, or other terminators as needed.

Parameters
:   | compat | lowercase-and-underscores devicetree compatible |
    | --- | --- |
    | fn | Macro to call for each enabled node. Must accept a node\_id as its only parameter. |

## [◆ ](#ga926f68202042c9db05390e628787f916)DT\_FOREACH\_STATUS\_OKAY\_NODE

| #define DT\_FOREACH\_STATUS\_OKAY\_NODE | ( |  | *fn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_FOREACH\_OKAY\_HELPER(fn)

Invokes `fn` for every status okay node in the tree.

The macro `fn` must take one parameter, which will be a node identifier. The macro is expanded once for each node in the tree with status okay (as usual, a missing status property is treated as status okay). The order that nodes are visited in is not specified.

Parameters
:   | fn | macro to invoke |
    | --- | --- |

## [◆ ](#ga9aa3ee2b90a4ec30621597f4d1448c51)DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS

| #define DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS | ( |  | *fn*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_FOREACH\_OKAY\_VARGS\_HELPER(fn, \_\_VA\_ARGS\_\_)

Invokes `fn` for every status okay node in the tree with multiple arguments.

The macro `fn` takes multiple arguments. The first should be the node identifier for the node. The remaining are passed-in by the caller.

The macro is expanded once for each node in the tree with status okay (as usual, a missing status property is treated as status okay). The order that nodes are visited in is not specified.

Parameters
:   | fn | macro to invoke |
    | --- | --- |
    | ... | variable number of arguments to pass to `fn` |

## [◆ ](#ga99cf30d6cf4847ed99ba7d81ad2b49d0)DT\_FOREACH\_STATUS\_OKAY\_VARGS

| #define DT\_FOREACH\_STATUS\_OKAY\_VARGS | ( |  | *compat*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(compat), \

(DT\_CAT(DT\_FOREACH\_OKAY\_VARGS\_, \

compat)(fn, \_\_VA\_ARGS\_\_)), \

())

Invokes `fn` for each status okay node of a compatible with multiple arguments.

This is like [DT\_FOREACH\_STATUS\_OKAY()](#ga52b34316d269cc8d8ef2244d3ca460b8) except you can also pass additional arguments to `fn`.

Example devicetree fragment:

/ {

a {

compatible = "foo";

val = <3>;

};

b {

compatible = "foo";

val = <4>;

};

};

Example usage:

#define MY\_FN(node\_id, operator) DT\_PROP(node\_id, val) operator

x = [DT\_FOREACH\_STATUS\_OKAY\_VARGS](#ga99cf30d6cf4847ed99ba7d81ad2b49d0)(foo, MY\_FN, +) 0;

[DT\_FOREACH\_STATUS\_OKAY\_VARGS](#ga99cf30d6cf4847ed99ba7d81ad2b49d0)

#define DT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn,...)

Invokes fn for each status okay node of a compatible with multiple arguments.

**Definition** devicetree.h:3515

This expands to one of the following:

x = 3 + 4 + 0;

x = 4 + 3 + 0;

i.e. it sets x to 7. As with [DT\_FOREACH\_STATUS\_OKAY()](#ga52b34316d269cc8d8ef2244d3ca460b8), there are no guarantees about the order nodes appear in the expansion.

Parameters
:   | compat | lowercase-and-underscores devicetree compatible |
    | --- | --- |
    | fn | Macro to call for each enabled node. Must accept a node\_id as its only parameter. |
    | ... | Additional arguments to pass to `fn` |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
