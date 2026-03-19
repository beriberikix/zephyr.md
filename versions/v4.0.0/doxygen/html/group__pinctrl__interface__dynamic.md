---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__pinctrl__interface__dynamic.html
original_path: doxygen/html/group__pinctrl__interface__dynamic.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Dynamic Pin Control

[Device Driver APIs](group__io__interfaces.md) » [Pin Controller Interface](group__pinctrl__interface.md)

| Macros | |
| --- | --- |
| #define | [PINCTRL\_DT\_STATE\_PINS\_DEFINE](#ga202dbcf2bcde364733996673dbdf2922)(node\_id, prop) |
|  | Helper macro to define the pins of a pin control state from Devicetree. |
| #define | [PINCTRL\_DT\_STATE\_INIT](#ga6331121c706ba721e5bd43491dcc14d2)(prop, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Utility macro to initialize a pin control state. |

| Functions | |
| --- | --- |
| int | [pinctrl\_update\_states](#ga647115208cbed7534a98c56d93a517b8) (struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, const struct [pinctrl\_state](structpinctrl__state.md) \*states, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) state\_cnt) |
|  | Update states with a new set. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga6331121c706ba721e5bd43491dcc14d2)PINCTRL\_DT\_STATE\_INIT

| #define PINCTRL\_DT\_STATE\_INIT | ( |  | *prop*, |
| --- | --- | --- | --- |
|  |  |  | *[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)* ) |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

**Value:**

{ \

.pins = prop ## \_pins, \

.pin\_cnt = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(prop ## \_pins), \

.id = [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

Utility macro to initialize a pin control state.

This macro should be used in conjunction with [PINCTRL\_DT\_STATE\_PINS\_DEFINE](#ga202dbcf2bcde364733996673dbdf2922) when using dynamic pin control to define an alternative state configuration stored in Devicetree.

Example:

// board.dts

/{

zephyr,user {

// uart0\_alt\_default node contains alternative pin config

uart0\_alt\_default = <&uart0\_alt\_default>;

};

};

// application

[PINCTRL\_DT\_STATE\_PINS\_DEFINE](#ga202dbcf2bcde364733996673dbdf2922)([DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)(zephyr\_user), uart0\_alt\_default);

static const struct [pinctrl\_state](structpinctrl__state.md) uart0\_alt[] = {

[PINCTRL\_DT\_STATE\_INIT](#ga6331121c706ba721e5bd43491dcc14d2)(uart0\_alt\_default, [PINCTRL\_STATE\_DEFAULT](group__pinctrl__interface.md#ga9bc564353cb9b1a7238c9fe8796023e6))

};

[DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)

#define DT\_PATH(...)

Get a node identifier for a devicetree path.

**Definition** devicetree.h:140

[PINCTRL\_DT\_STATE\_PINS\_DEFINE](#ga202dbcf2bcde364733996673dbdf2922)

#define PINCTRL\_DT\_STATE\_PINS\_DEFINE(node\_id, prop)

Helper macro to define the pins of a pin control state from Devicetree.

**Definition** pinctrl.h:376

[PINCTRL\_DT\_STATE\_INIT](#ga6331121c706ba721e5bd43491dcc14d2)

#define PINCTRL\_DT\_STATE\_INIT(prop, state)

Utility macro to initialize a pin control state.

**Definition** pinctrl.h:415

[PINCTRL\_STATE\_DEFAULT](group__pinctrl__interface.md#ga9bc564353cb9b1a7238c9fe8796023e6)

#define PINCTRL\_STATE\_DEFAULT

Default state (state used when the device is in operational state).

**Definition** pinctrl.h:42

[pinctrl\_state](structpinctrl__state.md)

Pin control state configuration.

**Definition** pinctrl.h:52

Parameters
:   | prop | Property name in Devicetree containing state configuration. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | State represented by `prop` (see [PINCTRL\_STATES](group__pinctrl__interface.md#PINCTRL_STATES "PINCTRL_STATES")). |

See also
:   [PINCTRL\_DT\_STATE\_PINS\_DEFINE](#ga202dbcf2bcde364733996673dbdf2922)

## [◆ ](#ga202dbcf2bcde364733996673dbdf2922)PINCTRL\_DT\_STATE\_PINS\_DEFINE

| #define PINCTRL\_DT\_STATE\_PINS\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

**Value:**

static const [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d) prop ## \_pins[] = \

Z\_PINCTRL\_STATE\_PINS\_INIT(node\_id, prop); \

[pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d)

struct pinctrl\_soc\_pin pinctrl\_soc\_pin\_t

Type for R-Car pin.

Helper macro to define the pins of a pin control state from Devicetree.

The name of the defined state pins variable is the same used by `prop`. This macro is expected to be used in conjunction with [PINCTRL\_DT\_STATE\_INIT](#ga6331121c706ba721e5bd43491dcc14d2).

Parameters
:   | node\_id | Node identifier containing `prop`. |
    | --- | --- |
    | prop | Property within `node_id` containing state configuration. |

See also
:   [PINCTRL\_DT\_STATE\_INIT](#ga6331121c706ba721e5bd43491dcc14d2)

## Function Documentation

## [◆ ](#ga647115208cbed7534a98c56d93a517b8)pinctrl\_update\_states()

| int pinctrl\_update\_states | ( | struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \* | *config*, |
| --- | --- | --- | --- |
|  |  | const struct [pinctrl\_state](structpinctrl__state.md) \* | *states*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *state\_cnt* ) |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

Update states with a new set.

Note
:   In order to guarantee device drivers correct operation the same states have to be provided. For example, if `default` and `sleep` are in the current list of states, it is expected that the new array of states also contains both.

Parameters
:   | config | Pin control configuration. |
    | --- | --- |
    | states | New states to be set. |
    | state\_cnt | Number of new states to be set. |

Return values
:   | -EINVAL | If the new configuration does not contain the same states as the current active configuration. |
    | --- | --- |
    | -ENOSYS | If the functionality is not available. |
    | 0 | On success. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
