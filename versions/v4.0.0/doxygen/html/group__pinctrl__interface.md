---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__pinctrl__interface.html
original_path: doxygen/html/group__pinctrl__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Pin Controller Interface

[Device Driver APIs](group__io__interfaces.md)

Pin Controller Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Dynamic Pin Control](group__pinctrl__interface__dynamic.md) |

| Data Structures | |
| --- | --- |
| struct | [pinctrl\_state](structpinctrl__state.md) |
|  | Pin control state configuration. [More...](structpinctrl__state.md#details) |
| struct | [pinctrl\_dev\_config](structpinctrl__dev__config.md) |
|  | Pin controller configuration for a given device. [More...](structpinctrl__dev__config.md#details) |

| Macros | |
| --- | --- |
| #define | [PINCTRL\_REG\_NONE](#ga6e283a1a1b040323b96227b2ea8f731e)   0U |
|  | Utility macro to indicate no register is used. |
| #define | [PINCTRL\_DT\_DEV\_CONFIG\_DECLARE](#ga636656676e81c65e1133607c972d65f4)(node\_id) |
|  | Declare pin control configuration for a given node identifier. |
| #define | [PINCTRL\_DT\_DEFINE](#gace422fcd4b28e6e6e6fdbbc64b99468f)(node\_id) |
|  | Define all pin control information for the given node identifier. |
| #define | [PINCTRL\_DT\_INST\_DEFINE](#ga8e984a57fd3c7a04cc921131ce79ac28)(inst) |
|  | Define all pin control information for the given compatible index. |
| #define | [PINCTRL\_DT\_DEV\_CONFIG\_GET](#ga502c3b6faec140188dd5d614f4777918)(node\_id) |
|  | Obtain a reference to the pin control configuration given a node identifier. |
| #define | [PINCTRL\_DT\_INST\_DEV\_CONFIG\_GET](#ga32748ffc5be4710707c7f1d9380cf93c)(inst) |
|  | Obtain a reference to the pin control configuration given current compatible instance number. |

| Functions | |
| --- | --- |
| int | [pinctrl\_lookup\_state](#ga46d7997af7e9231b431c79af34288d50) (const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const struct [pinctrl\_state](structpinctrl__state.md) \*\*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Find the state configuration for the given state id. |
| int | [pinctrl\_configure\_pins](#ga3397507e30eb10e814b793615f80455b) (const [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d) \*pins, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin\_cnt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) reg) |
|  | Configure a set of pins. |
| static int | [pinctrl\_apply\_state\_direct](#ga3549075e60ccdb743b269d590600d41b) (const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, const struct [pinctrl\_state](structpinctrl__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Apply a state directly from the provided state configuration. |
| static int | [pinctrl\_apply\_state](#ga16a9391222345d00dbc5c39c45f429f9) (const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | Apply a state from the given device configuration. |

| Pin control states | |
| --- | --- |
|  | |
| #define | [PINCTRL\_STATE\_DEFAULT](#ga9bc564353cb9b1a7238c9fe8796023e6)   0U |
|  | Default state (state used when the device is in operational state). |
| #define | [PINCTRL\_STATE\_SLEEP](#ga2ea5ac271930e0e2e9f77952b2dbea1b)   1U |
|  | Sleep state (state used when the device is in low power mode). |
| #define | [PINCTRL\_STATE\_PRIV\_START](#ga25989d7b48b2d7aa4f8ca6a30d9c9077)   2U |
|  | This and higher values refer to custom private states. |

## Detailed Description

Pin Controller Interface.

Since
:   3.0

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#gace422fcd4b28e6e6e6fdbbc64b99468f)PINCTRL\_DT\_DEFINE

| #define PINCTRL\_DT\_DEFINE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

**Value:**

[LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)([DT\_NUM\_PINCTRL\_STATES](group__devicetree-pinctrl.md#gaa2a012ce1d9ba026ee90001ae7f80381)(node\_id), \

Z\_PINCTRL\_STATE\_PINS\_DEFINE, (;), node\_id); \

Z\_PINCTRL\_STATES\_DEFINE(node\_id) \

Z\_PINCTRL\_DEV\_CONFIG\_STATIC Z\_PINCTRL\_DEV\_CONFIG\_CONST \

struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id) = \

Z\_PINCTRL\_DEV\_CONFIG\_INIT(node\_id)

[DT\_NUM\_PINCTRL\_STATES](group__devicetree-pinctrl.md#gaa2a012ce1d9ba026ee90001ae7f80381)

#define DT\_NUM\_PINCTRL\_STATES(node\_id)

Get the number of pinctrl properties in a node.

**Definition** pinctrl.h:239

[LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)

#define LISTIFY(LEN, F, sep,...)

Generates a sequence of code with configurable separator.

**Definition** util\_macro.h:458

[pinctrl\_dev\_config](structpinctrl__dev__config.md)

Pin controller configuration for a given device.

**Definition** pinctrl.h:62

Define all pin control information for the given node identifier.

This helper macro should be called together with device definition. It defines and initializes the pin control configuration for the device represented by node\_id. Each pin control state (pinctrl-0, ..., pinctrl-N) is also defined and initialized. Note that states marked to be skipped will not be defined (refer to Z\_PINCTRL\_SKIP\_STATE for more details).

Parameters
:   | node\_id | Node identifier. |
    | --- | --- |

## [◆ ](#ga636656676e81c65e1133607c972d65f4)PINCTRL\_DT\_DEV\_CONFIG\_DECLARE

| #define PINCTRL\_DT\_DEV\_CONFIG\_DECLARE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

**Value:**

extern Z\_PINCTRL\_DEV\_CONFIG\_CONST struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \

Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id)

Declare pin control configuration for a given node identifier.

This macro should be used by tests or applications using runtime pin control to declare the pin control configuration for a device. [PINCTRL\_DT\_DEV\_CONFIG\_GET](#ga502c3b6faec140188dd5d614f4777918) can later be used to obtain a reference to such configuration.

Only available if

```
CONFIG_PINCTRL_NON_STATIC
```

is selected.

Parameters
:   | node\_id | Node identifier. |
    | --- | --- |

## [◆ ](#ga502c3b6faec140188dd5d614f4777918)PINCTRL\_DT\_DEV\_CONFIG\_GET

| #define PINCTRL\_DT\_DEV\_CONFIG\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

**Value:**

&Z\_PINCTRL\_DEV\_CONFIG\_NAME(node\_id)

Obtain a reference to the pin control configuration given a node identifier.

Parameters
:   | node\_id | Node identifier. |
    | --- | --- |

## [◆ ](#ga8e984a57fd3c7a04cc921131ce79ac28)PINCTRL\_DT\_INST\_DEFINE

| #define PINCTRL\_DT\_INST\_DEFINE | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

**Value:**

[PINCTRL\_DT\_DEFINE](#gace422fcd4b28e6e6e6fdbbc64b99468f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3802

[PINCTRL\_DT\_DEFINE](#gace422fcd4b28e6e6e6fdbbc64b99468f)

#define PINCTRL\_DT\_DEFINE(node\_id)

Define all pin control information for the given node identifier.

**Definition** pinctrl.h:241

Define all pin control information for the given compatible index.

Parameters
:   | inst | Instance number. |
    | --- | --- |

See also
:   [PINCTRL\_DT\_DEFINE](#gace422fcd4b28e6e6e6fdbbc64b99468f)

## [◆ ](#ga32748ffc5be4710707c7f1d9380cf93c)PINCTRL\_DT\_INST\_DEV\_CONFIG\_GET

| #define PINCTRL\_DT\_INST\_DEV\_CONFIG\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

**Value:**

[PINCTRL\_DT\_DEV\_CONFIG\_GET](#ga502c3b6faec140188dd5d614f4777918)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[PINCTRL\_DT\_DEV\_CONFIG\_GET](#ga502c3b6faec140188dd5d614f4777918)

#define PINCTRL\_DT\_DEV\_CONFIG\_GET(node\_id)

Obtain a reference to the pin control configuration given a node identifier.

**Definition** pinctrl.h:264

Obtain a reference to the pin control configuration given current compatible instance number.

Parameters
:   | inst | Instance number. |
    | --- | --- |

See also
:   [PINCTRL\_DT\_DEV\_CONFIG\_GET](#ga502c3b6faec140188dd5d614f4777918)

## [◆ ](#ga6e283a1a1b040323b96227b2ea8f731e)PINCTRL\_REG\_NONE

| #define PINCTRL\_REG\_NONE   0U |
| --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

Utility macro to indicate no register is used.

## [◆ ](#ga9bc564353cb9b1a7238c9fe8796023e6)PINCTRL\_STATE\_DEFAULT

| #define PINCTRL\_STATE\_DEFAULT   0U |
| --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

Default state (state used when the device is in operational state).

## [◆ ](#ga25989d7b48b2d7aa4f8ca6a30d9c9077)PINCTRL\_STATE\_PRIV\_START

| #define PINCTRL\_STATE\_PRIV\_START   2U |
| --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

This and higher values refer to custom private states.

## [◆ ](#ga2ea5ac271930e0e2e9f77952b2dbea1b)PINCTRL\_STATE\_SLEEP

| #define PINCTRL\_STATE\_SLEEP   1U |
| --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

Sleep state (state used when the device is in low power mode).

## Function Documentation

## [◆ ](#ga16a9391222345d00dbc5c39c45f429f9)pinctrl\_apply\_state()

| | int pinctrl\_apply\_state | ( | const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \* | *config*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

Apply a state from the given device configuration.

Parameters
:   | config | Pin control configuration. |
    | --- | --- |
    | id | Id of the state to be applied (see [PINCTRL\_STATES](#PINCTRL_STATES)). |

Return values
:   | 0 | If succeeded. |
    | --- | --- |
    | -ENOENT | If given state id does not exist. |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga3549075e60ccdb743b269d590600d41b)pinctrl\_apply\_state\_direct()

| | int pinctrl\_apply\_state\_direct | ( | const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \* | *config*, | | --- | --- | --- | --- | |  |  | const struct [pinctrl\_state](structpinctrl__state.md) \* | *state* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

Apply a state directly from the provided state configuration.

Parameters
:   | config | Pin control configuration. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | State. |

Return values
:   | 0 | If succeeded |
    | --- | --- |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga3397507e30eb10e814b793615f80455b)pinctrl\_configure\_pins()

| int pinctrl\_configure\_pins | ( | const [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d) \* | *pins*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin\_cnt*, |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *reg* ) |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

Configure a set of pins.

This function will configure the necessary hardware blocks to make the configuration immediately effective.

Warning
:   This function must never be used to configure pins used by an instantiated device driver.

Parameters
:   | pins | List of pins to be configured. |
    | --- | --- |
    | pin\_cnt | Number of pins. |
    | reg | Device register (optional, use [PINCTRL\_REG\_NONE](#ga6e283a1a1b040323b96227b2ea8f731e) if not used). |

Return values
:   | 0 | If succeeded |
    | --- | --- |
    | -errno | Negative errno for other failures. |

## [◆ ](#ga46d7997af7e9231b431c79af34288d50)pinctrl\_lookup\_state()

| int pinctrl\_lookup\_state | ( | const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \* | *config*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
|  |  | const struct [pinctrl\_state](structpinctrl__state.md) \*\* | *state* ) |

`#include <[pinctrl.h](drivers_2pinctrl_8h.md)>`

Find the state configuration for the given state id.

Parameters
:   | config | Pin controller configuration. |
    | --- | --- |
    | id | Pin controller state id (see [PINCTRL\_STATES](#PINCTRL_STATES)). |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Found state. |

Return values
:   | 0 | If state has been found. |
    | --- | --- |
    | -ENOENT | If the state has not been found. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
