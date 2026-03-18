---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__devicetree-generic-vendor.html
original_path: doxygen/html/group__devicetree-generic-vendor.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vendor and model name helpers

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_NODE\_VENDOR\_BY\_IDX](#gafcd6cc682b573d61c7e28c8e3bafc747)(node\_id, idx) |
|  | Get the vendor at index `idx` as a string literal. |
| #define | [DT\_NODE\_VENDOR\_HAS\_IDX](#gabfa4130fa24457c457961caa7e2c6276)(node\_id, idx) |
|  | Does a node's compatible property have a vendor at an index? |
| #define | [DT\_NODE\_VENDOR\_BY\_IDX\_OR](#gaa71b1152516847d51582b9b23c472f3d)(node\_id, idx, default\_value) |
|  | Like [DT\_NODE\_VENDOR\_BY\_IDX()](#gafcd6cc682b573d61c7e28c8e3bafc747), but with a fallback to default\_value. |
| #define | [DT\_NODE\_VENDOR\_OR](#gad91ad9294d36eb151c96e719f1a5b0ef)(node\_id, default\_value) |
|  | Get the node's (only) vendor as a string literal. |
| #define | [DT\_NODE\_MODEL\_BY\_IDX](#gae4bbd66726d930d878588f9bb9f4d500)(node\_id, idx) |
|  | Get the model at index "idx" as a string literal. |
| #define | [DT\_NODE\_MODEL\_HAS\_IDX](#ga2ff3c91b22fae081d00d96964f465aa2)(node\_id, idx) |
|  | Does a node's compatible property have a model at an index? |
| #define | [DT\_NODE\_MODEL\_BY\_IDX\_OR](#ga98a2ff981359088e2e995017791176b1)(node\_id, idx, default\_value) |
|  | Like [DT\_NODE\_MODEL\_BY\_IDX()](#gae4bbd66726d930d878588f9bb9f4d500), but with a fallback to default\_value. |
| #define | [DT\_NODE\_MODEL\_OR](#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)(node\_id, default\_value) |
|  | Get the node's (only) model as a string literal. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gae4bbd66726d930d878588f9bb9f4d500)DT\_NODE\_MODEL\_BY\_IDX

| #define DT\_NODE\_MODEL\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT3(node\_id, \_COMPAT\_MODEL\_IDX\_, idx)

Get the model at index "idx" as a string literal.

The model is a string extracted from the compatible after the vendor prefix.

Example vendor-prefixes.txt:

```
 vnd        A stand-in for a real vendor
 zephyr     Zephyr-specific binding
```

Example devicetree fragment:

```
 n1: node-1 {
    compatible = "vnd,model1", "gpio", "zephyr,model2";
 };
```

Example usage:

```
 DT_NODE_MODEL_BY_IDX(DT_NODELABEL(n1), 0) // "model1"
 DT_NODE_MODEL_BY_IDX(DT_NODELABEL(n1), 2) // "model2"
```

Notice that the compatible at index 1 doesn't match any entries in the vendor prefix file and therefore index 1 is not a valid model index. Use [DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx)](#ga2ff3c91b22fae081d00d96964f465aa2) to determine if an index is valid.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the model to return |

Returns
:   string literal of the idx-th model

## [◆ ](#ga98a2ff981359088e2e995017791176b1)DT\_NODE\_MODEL\_BY\_IDX\_OR

| #define DT\_NODE\_MODEL\_BY\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_MODEL\_HAS\_IDX](#ga2ff3c91b22fae081d00d96964f465aa2)(node\_id, idx), \

([DT\_NODE\_MODEL\_BY\_IDX](#gae4bbd66726d930d878588f9bb9f4d500)(node\_id, idx)), (default\_value))

[DT\_NODE\_MODEL\_HAS\_IDX](#ga2ff3c91b22fae081d00d96964f465aa2)

#define DT\_NODE\_MODEL\_HAS\_IDX(node\_id, idx)

Does a node's compatible property have a model at an index?

**Definition** devicetree.h:2119

[DT\_NODE\_MODEL\_BY\_IDX](#gae4bbd66726d930d878588f9bb9f4d500)

#define DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx)

Get the model at index "idx" as a string literal.

**Definition** devicetree.h:2104

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

Like [DT\_NODE\_MODEL\_BY\_IDX()](#gae4bbd66726d930d878588f9bb9f4d500), but with a fallback to default\_value.

If the value exists, this expands to [DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx)](#gae4bbd66726d930d878588f9bb9f4d500). The default\_value parameter is not expanded in this case.

Otherwise, this expands to default\_value.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the model to return |

Returns
:   string literal of the idx-th model

Parameters
:   | default\_value | a fallback value to expand to |
    | --- | --- |

Returns
:   string literal of the idx-th model or "default\_value"

## [◆ ](#ga2ff3c91b22fae081d00d96964f465aa2)DT\_NODE\_MODEL\_HAS\_IDX

| #define DT\_NODE\_MODEL\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_COMPAT\_MODEL\_IDX\_, idx, \_EXISTS))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Does a node's compatible property have a model at an index?

If this returns 1, then [DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx)](#gae4bbd66726d930d878588f9bb9f4d500) is valid. If it returns 0, it is an error to use [DT\_NODE\_MODEL\_BY\_IDX(node\_id, idx)](#gae4bbd66726d930d878588f9bb9f4d500) with index "idx".

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the model to check |

Returns
:   1 if "idx" is a valid model index, 0 otherwise.

## [◆ ](#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)DT\_NODE\_MODEL\_OR

| #define DT\_NODE\_MODEL\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_NODE\_MODEL\_BY\_IDX\_OR](#ga98a2ff981359088e2e995017791176b1)(node\_id, 0, default\_value)

[DT\_NODE\_MODEL\_BY\_IDX\_OR](#ga98a2ff981359088e2e995017791176b1)

#define DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, idx, default\_value)

Like DT\_NODE\_MODEL\_BY\_IDX(), but with a fallback to default\_value.

**Definition** devicetree.h:2136

Get the node's (only) model as a string literal.

Equivalent to [DT\_NODE\_MODEL\_BY\_IDX\_OR(node\_id, 0, default\_value)](#ga98a2ff981359088e2e995017791176b1).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | default\_value | a fallback value to expand to |

## [◆ ](#gafcd6cc682b573d61c7e28c8e3bafc747)DT\_NODE\_VENDOR\_BY\_IDX

| #define DT\_NODE\_VENDOR\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

DT\_CAT3(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx)

Get the vendor at index `idx` as a string literal.

The vendor is a string extracted from vendor prefixes if an entry exists that matches the node's compatible prefix. There may be as many as one vendor prefixes file per directory in DTS\_ROOT.

Example vendor-prefixes.txt:

```
 vnd        A stand-in for a real vendor
 zephyr     Zephyr-specific binding
```

Example devicetree fragment:

n1: node-1 {

compatible = "vnd,model1", "gpio", "zephyr,model2";

};

Example usage:

[DT\_NODE\_VENDOR\_BY\_IDX](#gafcd6cc682b573d61c7e28c8e3bafc747)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n1), 0) // "A stand-in for a real vendor"

[DT\_NODE\_VENDOR\_BY\_IDX](#gafcd6cc682b573d61c7e28c8e3bafc747)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(n1), 2) // "Zephyr-specific binding"

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:198

[DT\_NODE\_VENDOR\_BY\_IDX](#gafcd6cc682b573d61c7e28c8e3bafc747)

#define DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx)

Get the vendor at index idx as a string literal.

**Definition** devicetree.h:2028

Notice that the compatible at index 1 doesn't match any entries in the vendor prefix file and therefore index 1 is not a valid vendor index. Use [DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx)](#gabfa4130fa24457c457961caa7e2c6276) to determine if an index is valid.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the vendor to return |

Returns
:   string literal of the idx-th vendor

## [◆ ](#gaa71b1152516847d51582b9b23c472f3d)DT\_NODE\_VENDOR\_BY\_IDX\_OR

| #define DT\_NODE\_VENDOR\_BY\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_VENDOR\_HAS\_IDX](#gabfa4130fa24457c457961caa7e2c6276)(node\_id, idx), \

([DT\_NODE\_VENDOR\_BY\_IDX](#gafcd6cc682b573d61c7e28c8e3bafc747)(node\_id, idx)), (default\_value))

[DT\_NODE\_VENDOR\_HAS\_IDX](#gabfa4130fa24457c457961caa7e2c6276)

#define DT\_NODE\_VENDOR\_HAS\_IDX(node\_id, idx)

Does a node's compatible property have a vendor at an index?

**Definition** devicetree.h:2043

Like [DT\_NODE\_VENDOR\_BY\_IDX()](#gafcd6cc682b573d61c7e28c8e3bafc747), but with a fallback to default\_value.

If the value exists, this expands to [DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx)](#gafcd6cc682b573d61c7e28c8e3bafc747). The default\_value parameter is not expanded in this case.

Otherwise, this expands to default\_value.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the vendor to return |

Returns
:   string literal of the idx-th vendor

Parameters
:   | default\_value | a fallback value to expand to |
    | --- | --- |

Returns
:   string literal of the idx-th vendor or "default\_value"

## [◆ ](#gabfa4130fa24457c457961caa7e2c6276)DT\_NODE\_VENDOR\_HAS\_IDX

| #define DT\_NODE\_VENDOR\_HAS\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_COMPAT\_VENDOR\_IDX\_, idx, \_EXISTS))

Does a node's compatible property have a vendor at an index?

If this returns 1, then [DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx)](#gafcd6cc682b573d61c7e28c8e3bafc747) is valid. If it returns 0, it is an error to use [DT\_NODE\_VENDOR\_BY\_IDX(node\_id, idx)](#gafcd6cc682b573d61c7e28c8e3bafc747) with index `idx`.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | index of the vendor to check |

Returns
:   1 if `idx` is a valid vendor index, 0 otherwise.

## [◆ ](#gad91ad9294d36eb151c96e719f1a5b0ef)DT\_NODE\_VENDOR\_OR

| #define DT\_NODE\_VENDOR\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_NODE\_VENDOR\_BY\_IDX\_OR](#gaa71b1152516847d51582b9b23c472f3d)(node\_id, 0, default\_value)

[DT\_NODE\_VENDOR\_BY\_IDX\_OR](#gaa71b1152516847d51582b9b23c472f3d)

#define DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, idx, default\_value)

Like DT\_NODE\_VENDOR\_BY\_IDX(), but with a fallback to default\_value.

**Definition** devicetree.h:2060

Get the node's (only) vendor as a string literal.

Equivalent to [DT\_NODE\_VENDOR\_BY\_IDX\_OR(node\_id, 0, default\_value)](#gaa71b1152516847d51582b9b23c472f3d).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | default\_value | a fallback value to expand to |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
