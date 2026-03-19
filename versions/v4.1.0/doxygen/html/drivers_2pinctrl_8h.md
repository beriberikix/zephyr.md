---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2pinctrl_8h.html
original_path: doxygen/html/drivers_2pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl.h File Reference

Public APIs for pin control drivers.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/devicetree/pinctrl.h](devicetree_2pinctrl_8h_source.md)>`  
`#include <pinctrl_soc.h>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](drivers_2pinctrl_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pinctrl\_state](structpinctrl__state.md) |
|  | Pin control state configuration. [More...](structpinctrl__state.md#details) |
| struct | [pinctrl\_dev\_config](structpinctrl__dev__config.md) |
|  | Pin controller configuration for a given device. [More...](structpinctrl__dev__config.md#details) |

| Macros | |
| --- | --- |
| #define | [PINCTRL\_REG\_NONE](group__pinctrl__interface.md#ga6e283a1a1b040323b96227b2ea8f731e)   0U |
|  | Utility macro to indicate no register is used. |
| #define | [PINCTRL\_DT\_DEV\_CONFIG\_DECLARE](group__pinctrl__interface.md#ga636656676e81c65e1133607c972d65f4)(node\_id) |
|  | Declare pin control configuration for a given node identifier. |
| #define | [PINCTRL\_DT\_DEFINE](group__pinctrl__interface.md#gace422fcd4b28e6e6e6fdbbc64b99468f)(node\_id) |
|  | Define all pin control information for the given node identifier. |
| #define | [PINCTRL\_DT\_INST\_DEFINE](group__pinctrl__interface.md#ga8e984a57fd3c7a04cc921131ce79ac28)(inst) |
|  | Define all pin control information for the given compatible index. |
| #define | [PINCTRL\_DT\_DEV\_CONFIG\_GET](group__pinctrl__interface.md#ga502c3b6faec140188dd5d614f4777918)(node\_id) |
|  | Obtain a reference to the pin control configuration given a node identifier. |
| #define | [PINCTRL\_DT\_INST\_DEV\_CONFIG\_GET](group__pinctrl__interface.md#ga32748ffc5be4710707c7f1d9380cf93c)(inst) |
|  | Obtain a reference to the pin control configuration given current compatible instance number. |
| #define | [PINCTRL\_DT\_STATE\_PINS\_DEFINE](group__pinctrl__interface__dynamic.md#ga202dbcf2bcde364733996673dbdf2922)(node\_id, prop) |
|  | Helper macro to define the pins of a pin control state from Devicetree. |
| #define | [PINCTRL\_DT\_STATE\_INIT](group__pinctrl__interface__dynamic.md#ga6331121c706ba721e5bd43491dcc14d2)(prop, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Utility macro to initialize a pin control state. |
| Pin control states | |
|  | |
| #define | [PINCTRL\_STATE\_DEFAULT](group__pinctrl__interface.md#ga9bc564353cb9b1a7238c9fe8796023e6)   0U |
|  | Default state (state used when the device is in operational state). |
| #define | [PINCTRL\_STATE\_SLEEP](group__pinctrl__interface.md#ga2ea5ac271930e0e2e9f77952b2dbea1b)   1U |
|  | Sleep state (state used when the device is in low power mode). |
| #define | [PINCTRL\_STATE\_PRIV\_START](group__pinctrl__interface.md#ga25989d7b48b2d7aa4f8ca6a30d9c9077)   2U |
|  | This and higher values refer to custom private states. |

| Functions | |
| --- | --- |
| int | [pinctrl\_lookup\_state](group__pinctrl__interface.md#ga46d7997af7e9231b431c79af34288d50) (const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const struct [pinctrl\_state](structpinctrl__state.md) \*\*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Find the state configuration for the given state id. |
| int | [pinctrl\_configure\_pins](group__pinctrl__interface.md#ga3397507e30eb10e814b793615f80455b) (const [pinctrl\_soc\_pin\_t](pinctrl__rcar__common_8h.md#a022eeb1c811e7ef94d3a7a99cbda0e2d) \*pins, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin\_cnt, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) reg) |
|  | Configure a set of pins. |
| static int | [pinctrl\_apply\_state\_direct](group__pinctrl__interface.md#ga3549075e60ccdb743b269d590600d41b) (const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, const struct [pinctrl\_state](structpinctrl__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Apply a state directly from the provided state configuration. |
| static int | [pinctrl\_apply\_state](group__pinctrl__interface.md#ga16a9391222345d00dbc5c39c45f429f9) (const struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | Apply a state from the given device configuration. |
| int | [pinctrl\_update\_states](group__pinctrl__interface__dynamic.md#ga647115208cbed7534a98c56d93a517b8) (struct [pinctrl\_dev\_config](structpinctrl__dev__config.md) \*config, const struct [pinctrl\_state](structpinctrl__state.md) \*states, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) state\_cnt) |
|  | Update states with a new set. |

## Detailed Description

Public APIs for pin control drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl.h](drivers_2pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
