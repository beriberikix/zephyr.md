---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structpinctrl__dev__config.html
original_path: doxygen/html/structpinctrl__dev__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_dev\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Pin Controller Interface](group__pinctrl__interface.md)

Pin controller configuration for a given device.
[More...](#details)

`#include <[pinctrl.h](drivers_2pinctrl_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [reg](#a69db43c310985f38f0802a3e9f82fd62) |
|  | Device address (only available if `CONFIG_PINCTRL_STORE_REG` is enabled). |
| const struct [pinctrl\_state](structpinctrl__state.md) \* | [states](#a57dcdf2f712de95f8e8568e2be4b52e6) |
|  | List of state configurations. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [state\_cnt](#a0af0d0115eaa9729c1fe782666ad0e66) |
|  | Number of state configurations. |

## Detailed Description

Pin controller configuration for a given device.

## Field Documentation

## [◆ ](#a69db43c310985f38f0802a3e9f82fd62)reg

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) pinctrl\_dev\_config::reg |
| --- |

Device address (only available if `CONFIG_PINCTRL_STORE_REG` is enabled).

## [◆ ](#a0af0d0115eaa9729c1fe782666ad0e66)state\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pinctrl\_dev\_config::state\_cnt |
| --- |

Number of state configurations.

## [◆ ](#a57dcdf2f712de95f8e8568e2be4b52e6)states

| const struct [pinctrl\_state](structpinctrl__state.md)\* pinctrl\_dev\_config::states |
| --- |

List of state configurations.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[pinctrl.h](drivers_2pinctrl_8h_source.md)

- [pinctrl\_dev\_config](structpinctrl__dev__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
