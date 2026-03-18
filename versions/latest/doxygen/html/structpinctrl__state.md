---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structpinctrl__state.html
original_path: doxygen/html/structpinctrl__state.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_state Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Pin Controller Interface](group__pinctrl__interface.md)

Pin control state configuration.
[More...](#details)

`#include <[pinctrl.h](drivers_2pinctrl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const pinctrl\_soc\_pin\_t \* | [pins](#a99ceb5bff2b8e50109e5915140eebe76) |
|  | Pin configurations. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pin\_cnt](#aa015854e6eae7b86fffb282b07652573) |
|  | Number of pin configurations. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#acae4c7cfc06471533f6d977e1f2ba623) |
|  | State identifier (see [PINCTRL\_STATES](group__pinctrl__interface.md#PINCTRL_STATES "PINCTRL_STATES")). |

## Detailed Description

Pin control state configuration.

## Field Documentation

## [◆ ](#acae4c7cfc06471533f6d977e1f2ba623)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pinctrl\_state::id |
| --- |

State identifier (see [PINCTRL\_STATES](group__pinctrl__interface.md#PINCTRL_STATES "PINCTRL_STATES")).

## [◆ ](#aa015854e6eae7b86fffb282b07652573)pin\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pinctrl\_state::pin\_cnt |
| --- |

Number of pin configurations.

## [◆ ](#a99ceb5bff2b8e50109e5915140eebe76)pins

| const pinctrl\_soc\_pin\_t\* pinctrl\_state::pins |
| --- |

Pin configurations.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[pinctrl.h](drivers_2pinctrl_8h_source.md)

- [pinctrl\_state](structpinctrl__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
