---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__backend__ble_8h.html
original_path: doxygen/html/log__backend__ble_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_ble.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](log__backend__ble_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LOGGER\_BACKEND\_BLE\_ADV\_UUID\_DATA](#a35e6ef530516c345125da273d06e359d) |
|  | Raw adv UUID data to add the Bluetooth backend for the use with apps such as the NRF Toolbox. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [logger\_backend\_ble\_hook](#a54f16cb2a3e183f47110b49af97c6062)) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) backend\_status, void \*ctx) |
|  | Hook for application to know when the Bluetooth backend is enabled or disabled. |

| Functions | |
| --- | --- |
| void | [logger\_backend\_ble\_set\_hook](#a324e2709a95362f3c83aaa89facca2cc) ([logger\_backend\_ble\_hook](#a54f16cb2a3e183f47110b49af97c6062) hook, void \*ctx) |
|  | Allows application to add a hook for the status of the Bluetooth logger backend. |

## Macro Definition Documentation

## [◆ ](#a35e6ef530516c345125da273d06e359d)LOGGER\_BACKEND\_BLE\_ADV\_UUID\_DATA

| #define LOGGER\_BACKEND\_BLE\_ADV\_UUID\_DATA |
| --- |

**Value:**

0x9E, 0xCA, 0xDC, 0x24, 0x0E, 0xE5, 0xA9, 0xE0, 0x93, 0xF3, 0xA3, 0xB5, 0x01, 0x00, 0x40, \

0x6E

Raw adv UUID data to add the Bluetooth backend for the use with apps such as the NRF Toolbox.

## Typedef Documentation

## [◆ ](#a54f16cb2a3e183f47110b49af97c6062)logger\_backend\_ble\_hook

| typedef void(\* logger\_backend\_ble\_hook) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) backend\_status, void \*ctx) |
| --- |

Hook for application to know when the Bluetooth backend is enabled or disabled.

Parameters
:   | backend\_status | True if the backend is enabled or false if disabled |
    | --- | --- |
    | ctx | User context |

## Function Documentation

## [◆ ](#a324e2709a95362f3c83aaa89facca2cc)logger\_backend\_ble\_set\_hook()

| void logger\_backend\_ble\_set\_hook | ( | [logger\_backend\_ble\_hook](#a54f16cb2a3e183f47110b49af97c6062) | *hook*, |
| --- | --- | --- | --- |
|  |  | void \* | *ctx* ) |

Allows application to add a hook for the status of the Bluetooth logger backend.

The Bluetooth logger backend is enabled or disabled auomatically by the subscription of the notification characteristic of this Bluetooth Logger backend service.

Parameters
:   | hook | The hook that will be called when the status of the backend changes |
    | --- | --- |
    | ctx | User context for whenever the hook is called |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_ble.h](log__backend__ble_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
