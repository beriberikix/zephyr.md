---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__devicetree-gpio.html
original_path: doxygen/html/group__devicetree-gpio.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devicetree GPIO API

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_GPIO\_CTLR\_BY\_IDX](#ga97bd46d2ab88d392a3f336f4d23184eb)(node\_id, gpio\_pha, idx) |
|  | Get the node identifier for the controller phandle from a gpio phandle-array property at an index. |
| #define | [DT\_GPIO\_CTLR](#gafbad7d0d7f7fb9338997482c8da0e566)(node\_id, gpio\_pha) |
|  | Equivalent to [DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, 0)](#ga97bd46d2ab88d392a3f336f4d23184eb). |
| #define | [DT\_GPIO\_PIN\_BY\_IDX](#ga8f7d82567056266bab1603865f8b27af)(node\_id, gpio\_pha, idx) |
|  | Get a GPIO specifier's pin cell at an index. |
| #define | [DT\_GPIO\_PIN](#ga4e41ec30ece058555333811a9fcee333)(node\_id, gpio\_pha) |
|  | Equivalent to [DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, 0)](#ga8f7d82567056266bab1603865f8b27af). |
| #define | [DT\_GPIO\_FLAGS\_BY\_IDX](#ga672b2597b99194b8cbd42b3f3401d2b5)(node\_id, gpio\_pha, idx) |
|  | Get a GPIO specifier's flags cell at an index. |
| #define | [DT\_GPIO\_FLAGS](#ga32b3383d7ed543602a7b4a031018316f)(node\_id, gpio\_pha) |
|  | Equivalent to [DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, 0)](#ga672b2597b99194b8cbd42b3f3401d2b5). |
| #define | [DT\_NUM\_GPIO\_HOGS](#ga0a4575c3750db76692fd0f817a169b50)(node\_id) |
|  | Get the number of GPIO hogs in a node. |
| #define | [DT\_GPIO\_HOG\_PIN\_BY\_IDX](#gaf4ecdebbd433473f654f4b6859542af9)(node\_id, idx) |
|  | Get a GPIO hog specifier's pin cell at an index. |
| #define | [DT\_GPIO\_HOG\_FLAGS\_BY\_IDX](#gaed024e6acac49f591fe50cd43e8af14f)(node\_id, idx) |
|  | Get a GPIO hog specifier's flags cell at an index. |
| #define | [DT\_INST\_GPIO\_PIN\_BY\_IDX](#ga162bca126f7015816286358f09bde6ff)(inst, gpio\_pha, idx) |
|  | Get a DT\_DRV\_COMPAT instance's GPIO specifier's pin cell value at an index. |
| #define | [DT\_INST\_GPIO\_PIN](#ga5ee13b3de1d4cecc877963dfa8820cfd)(inst, gpio\_pha) |
|  | Equivalent to [DT\_INST\_GPIO\_PIN\_BY\_IDX(inst, gpio\_pha, 0)](#ga162bca126f7015816286358f09bde6ff). |
| #define | [DT\_INST\_GPIO\_FLAGS\_BY\_IDX](#gafd40d1eec5c1672b7675ae47388c1cef)(inst, gpio\_pha, idx) |
|  | Get a DT\_DRV\_COMPAT instance's GPIO specifier's flags cell at an index. |
| #define | [DT\_INST\_GPIO\_FLAGS](#ga8d3edd53d6d8e89afc68f0c10176f57f)(inst, gpio\_pha) |
|  | Equivalent to [DT\_INST\_GPIO\_FLAGS\_BY\_IDX(inst, gpio\_pha, 0)](#gafd40d1eec5c1672b7675ae47388c1cef). |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gafbad7d0d7f7fb9338997482c8da0e566)DT\_GPIO\_CTLR

| #define DT\_GPIO\_CTLR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_GPIO\_CTLR\_BY\_IDX](#ga97bd46d2ab88d392a3f336f4d23184eb)(node\_id, gpio\_pha, 0)

[DT\_GPIO\_CTLR\_BY\_IDX](#ga97bd46d2ab88d392a3f336f4d23184eb)

#define DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, idx)

Get the node identifier for the controller phandle from a gpio phandle-array property at an index.

**Definition** gpio.h:53

Equivalent to [DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, 0)](#ga97bd46d2ab88d392a3f336f4d23184eb).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |

Returns
:   a node identifier for the gpio controller at index 0 in "gpio\_pha"

See also
:   [DT\_GPIO\_CTLR\_BY\_IDX()](#ga97bd46d2ab88d392a3f336f4d23184eb)

## [◆ ](#ga97bd46d2ab88d392a3f336f4d23184eb)DT\_GPIO\_CTLR\_BY\_IDX

| #define DT\_GPIO\_CTLR\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha*, |
|  |  |  | *idx* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, gpio\_pha, idx)

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1628

Get the node identifier for the controller phandle from a gpio phandle-array property at an index.

Example devicetree fragment:

```
gpio1: gpio@... { };

gpio2: gpio@... { };

n: node {
        gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                <&gpio2 30 GPIO_ACTIVE_HIGH>;
};
```

Example usage:

```
DT_GPIO_CTLR_BY_IDX(DT_NODELABEL(n), gpios, 1) // DT_NODELABEL(gpio2)
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |
    | idx | logical index into "gpio\_pha" |

Returns
:   the node identifier for the gpio controller referenced at index "idx"

See also
:   [DT\_PHANDLE\_BY\_IDX()](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de "Get a node identifier for a phandle in a property.")

## [◆ ](#ga32b3383d7ed543602a7b4a031018316f)DT\_GPIO\_FLAGS

| #define DT\_GPIO\_FLAGS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_GPIO\_FLAGS\_BY\_IDX](#ga672b2597b99194b8cbd42b3f3401d2b5)(node\_id, gpio\_pha, 0)

[DT\_GPIO\_FLAGS\_BY\_IDX](#ga672b2597b99194b8cbd42b3f3401d2b5)

#define DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, idx)

Get a GPIO specifier's flags cell at an index.

**Definition** gpio.h:165

Equivalent to [DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, 0)](#ga672b2597b99194b8cbd42b3f3401d2b5).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |

Returns
:   the flags cell value at index 0, or zero if there is none

See also
:   [DT\_GPIO\_FLAGS\_BY\_IDX()](#ga672b2597b99194b8cbd42b3f3401d2b5)

## [◆ ](#ga672b2597b99194b8cbd42b3f3401d2b5)DT\_GPIO\_FLAGS\_BY\_IDX

| #define DT\_GPIO\_FLAGS\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha*, |
|  |  |  | *idx* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)(node\_id, gpio\_pha, idx, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), 0)

[DT\_PHA\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)

#define DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value)

Like DT\_PHA\_BY\_IDX(), but with a fallback to default\_value.

**Definition** devicetree.h:1433

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

Get a GPIO specifier's flags cell at an index.

This macro expects GPIO specifiers with cells named "flags". If there is no "flags" cell in the GPIO specifier, zero is returned. Refer to the node's binding to check specifier cell names if necessary.

Example devicetree fragment:

```
gpio1: gpio@... {
        compatible = "vnd,gpio";
        #gpio-cells = <2>;
};

gpio2: gpio@... {
        compatible = "vnd,gpio";
        #gpio-cells = <2>;
};

n: node {
        gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                <&gpio2 30 GPIO_ACTIVE_HIGH>;
};
```

Bindings fragment for the vnd,gpio compatible:

```
gpio-cells:
  - pin
  - flags
```

Example usage:

```
DT_GPIO_FLAGS_BY_IDX(DT_NODELABEL(n), gpios, 0) // GPIO_ACTIVE_LOW
DT_GPIO_FLAGS_BY_IDX(DT_NODELABEL(n), gpios, 1) // GPIO_ACTIVE_HIGH
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |
    | idx | logical index into "gpio\_pha" |

Returns
:   the flags cell value at index "idx", or zero if there is none

See also
:   [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.")

## [◆ ](#gaed024e6acac49f591fe50cd43e8af14f)DT\_GPIO\_HOG\_FLAGS\_BY\_IDX

| #define DT\_GPIO\_HOG\_FLAGS\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(node\_id, \_GPIO\_HOGS\_IDX\_, idx, \_VAL\_flags\_EXISTS)), \

(DT\_CAT4(node\_id, \_GPIO\_HOGS\_IDX\_, idx, \_VAL\_flags)), (0))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

Get a GPIO hog specifier's flags cell at an index.

This macro expects GPIO specifiers with cells named "flags". If there is no "flags" cell in the GPIO specifier, zero is returned. Refer to the node's binding to check specifier cell names if necessary.

Example devicetree fragment:

```
gpio1: gpio@... {
  compatible = "vnd,gpio";
  #gpio-cells = <2>;

  n1: node-1 {
          gpio-hog;
          gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
          output-high;
  };

  n2: node-2 {
          gpio-hog;
          gpios = <3 GPIO_ACTIVE_HIGH>;
          output-low;
  };
};
```

Bindings fragment for the vnd,gpio compatible:

```
gpio-cells:
  - pin
  - flags
```

Example usage:

```
DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n1), 0) // GPIO_ACTIVE_HIGH
DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n1), 1) // GPIO_ACTIVE_LOW
DT_GPIO_HOG_FLAGS_BY_IDX(DT_NODELABEL(n2), 0) // GPIO_ACTIVE_HIGH
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into "gpios" |

Returns
:   the flags cell value at index "idx", or zero if there is none

## [◆ ](#gaf4ecdebbd433473f654f4b6859542af9)DT\_GPIO\_HOG\_PIN\_BY\_IDX

| #define DT\_GPIO\_HOG\_PIN\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

DT\_CAT4(node\_id, \_GPIO\_HOGS\_IDX\_, idx, \_VAL\_pin)

Get a GPIO hog specifier's pin cell at an index.

This macro only works for GPIO specifiers with cells named "pin". Refer to the node's binding to check if necessary.

Example devicetree fragment:

```
gpio1: gpio@... {
  compatible = "vnd,gpio";
  #gpio-cells = <2>;

  n1: node-1 {
          gpio-hog;
          gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
          output-high;
  };

  n2: node-2 {
          gpio-hog;
          gpios = <3 GPIO_ACTIVE_HIGH>;
          output-low;
  };
};
```

Bindings fragment for the vnd,gpio compatible:

```
gpio-cells:
  - pin
  - flags
```

Example usage:

```
DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n1), 0) // 0
DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n1), 1) // 1
DT_GPIO_HOG_PIN_BY_IDX(DT_NODELABEL(n2), 0) // 3
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | idx | logical index into "gpios" |

Returns
:   the pin cell value at index "idx"

## [◆ ](#ga4e41ec30ece058555333811a9fcee333)DT\_GPIO\_PIN

| #define DT\_GPIO\_PIN | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_GPIO\_PIN\_BY\_IDX](#ga8f7d82567056266bab1603865f8b27af)(node\_id, gpio\_pha, 0)

[DT\_GPIO\_PIN\_BY\_IDX](#ga8f7d82567056266bab1603865f8b27af)

#define DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, idx)

Get a GPIO specifier's pin cell at an index.

**Definition** gpio.h:109

Equivalent to [DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, 0)](#ga8f7d82567056266bab1603865f8b27af).

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |

Returns
:   the pin cell value at index 0

See also
:   [DT\_GPIO\_PIN\_BY\_IDX()](#ga8f7d82567056266bab1603865f8b27af)

## [◆ ](#ga8f7d82567056266bab1603865f8b27af)DT\_GPIO\_PIN\_BY\_IDX

| #define DT\_GPIO\_PIN\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha*, |
|  |  |  | *idx* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, gpio\_pha, idx, pin)

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1407

Get a GPIO specifier's pin cell at an index.

This macro only works for GPIO specifiers with cells named "pin". Refer to the node's binding to check if necessary.

Example devicetree fragment:

```
gpio1: gpio@... {
        compatible = "vnd,gpio";
        #gpio-cells = <2>;
};

gpio2: gpio@... {
        compatible = "vnd,gpio";
        #gpio-cells = <2>;
};

n: node {
        gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                <&gpio2 30 GPIO_ACTIVE_HIGH>;
};
```

Bindings fragment for the vnd,gpio compatible:

```
gpio-cells:
  - pin
  - flags
```

Example usage:

```
DT_GPIO_PIN_BY_IDX(DT_NODELABEL(n), gpios, 0) // 10
DT_GPIO_PIN_BY_IDX(DT_NODELABEL(n), gpios, 1) // 30
```

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |
    | idx | logical index into "gpio\_pha" |

Returns
:   the pin cell value at index "idx"

See also
:   [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index.")

## [◆ ](#ga8d3edd53d6d8e89afc68f0c10176f57f)DT\_INST\_GPIO\_FLAGS

| #define DT\_INST\_GPIO\_FLAGS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_INST\_GPIO\_FLAGS\_BY\_IDX](#gafd40d1eec5c1672b7675ae47388c1cef)(inst, gpio\_pha, 0)

[DT\_INST\_GPIO\_FLAGS\_BY\_IDX](#gafd40d1eec5c1672b7675ae47388c1cef)

#define DT\_INST\_GPIO\_FLAGS\_BY\_IDX(inst, gpio\_pha, idx)

Get a DT\_DRV\_COMPAT instance's GPIO specifier's flags cell at an index.

**Definition** gpio.h:345

Equivalent to [DT\_INST\_GPIO\_FLAGS\_BY\_IDX(inst, gpio\_pha, 0)](#gafd40d1eec5c1672b7675ae47388c1cef).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |

Returns
:   the flags cell value at index 0, or zero if there is none

See also
:   [DT\_INST\_GPIO\_FLAGS\_BY\_IDX()](#gafd40d1eec5c1672b7675ae47388c1cef)

## [◆ ](#gafd40d1eec5c1672b7675ae47388c1cef)DT\_INST\_GPIO\_FLAGS\_BY\_IDX

| #define DT\_INST\_GPIO\_FLAGS\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha*, |
|  |  |  | *idx* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_GPIO\_FLAGS\_BY\_IDX](#ga672b2597b99194b8cbd42b3f3401d2b5)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), gpio\_pha, idx)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3604

Get a DT\_DRV\_COMPAT instance's GPIO specifier's flags cell at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |
    | idx | logical index into "gpio\_pha" |

Returns
:   the flags cell value at index "idx", or zero if there is none

See also
:   [DT\_GPIO\_FLAGS\_BY\_IDX()](#ga672b2597b99194b8cbd42b3f3401d2b5)

## [◆ ](#ga5ee13b3de1d4cecc877963dfa8820cfd)DT\_INST\_GPIO\_PIN

| #define DT\_INST\_GPIO\_PIN | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_INST\_GPIO\_PIN\_BY\_IDX](#ga162bca126f7015816286358f09bde6ff)(inst, gpio\_pha, 0)

[DT\_INST\_GPIO\_PIN\_BY\_IDX](#ga162bca126f7015816286358f09bde6ff)

#define DT\_INST\_GPIO\_PIN\_BY\_IDX(inst, gpio\_pha, idx)

Get a DT\_DRV\_COMPAT instance's GPIO specifier's pin cell value at an index.

**Definition** gpio.h:321

Equivalent to [DT\_INST\_GPIO\_PIN\_BY\_IDX(inst, gpio\_pha, 0)](#ga162bca126f7015816286358f09bde6ff).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |

Returns
:   the pin cell value at index 0

See also
:   [DT\_INST\_GPIO\_PIN\_BY\_IDX()](#ga162bca126f7015816286358f09bde6ff)

## [◆ ](#ga162bca126f7015816286358f09bde6ff)DT\_INST\_GPIO\_PIN\_BY\_IDX

| #define DT\_INST\_GPIO\_PIN\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *gpio\_pha*, |
|  |  |  | *idx* ) |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[DT\_GPIO\_PIN\_BY\_IDX](#ga8f7d82567056266bab1603865f8b27af)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), gpio\_pha, idx)

Get a DT\_DRV\_COMPAT instance's GPIO specifier's pin cell value at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | gpio\_pha | lowercase-and-underscores GPIO property with type "phandle-array" |
    | idx | logical index into "gpio\_pha" |

Returns
:   the pin cell value at index "idx"

See also
:   [DT\_GPIO\_PIN\_BY\_IDX()](#ga8f7d82567056266bab1603865f8b27af)

## [◆ ](#ga0a4575c3750db76692fd0f817a169b50)DT\_NUM\_GPIO\_HOGS

| #define DT\_NUM\_GPIO\_HOGS | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](devicetree_2gpio_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT(node\_id, \_GPIO\_HOGS\_EXISTS)), \

(DT\_CAT(node\_id, \_GPIO\_HOGS\_NUM)), (0))

Get the number of GPIO hogs in a node.

This expands to the number of hogged GPIOs, or zero if there are none.

Example devicetree fragment:

```
gpio1: gpio@... {
  compatible = "vnd,gpio";
  #gpio-cells = <2>;

  n1: node-1 {
          gpio-hog;
          gpios = <0 GPIO_ACTIVE_HIGH>, <1 GPIO_ACTIVE_LOW>;
          output-high;
  };

  n2: node-2 {
          gpio-hog;
          gpios = <3 GPIO_ACTIVE_HIGH>;
          output-low;
  };
};
```

Bindings fragment for the vnd,gpio compatible:

```
gpio-cells:
  - pin
  - flags
```

Example usage:

```
DT_NUM_GPIO_HOGS(DT_NODELABEL(n1)) // 2
DT_NUM_GPIO_HOGS(DT_NODELABEL(n2)) // 1
```

Parameters
:   | node\_id | node identifier; may or may not be a GPIO hog node. |
    | --- | --- |

Returns
:   number of hogged GPIOs in the node

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
