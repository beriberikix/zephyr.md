---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__backend__ble_8h_source.html
original_path: doxygen/html/log__backend__ble_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_ble.h

[Go to the documentation of this file.](log__backend__ble_8h.md)

1/\*

2 \* Copyright (c) 2023 Victor Chavez

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LOG\_BACKEND\_BLE\_H\_

8#define ZEPHYR\_LOG\_BACKEND\_BLE\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

16

[ 17](log__backend__ble_8h.md#a35e6ef530516c345125da273d06e359d)#define LOGGER\_BACKEND\_BLE\_ADV\_UUID\_DATA \

18 0x9E, 0xCA, 0xDC, 0x24, 0x0E, 0xE5, 0xA9, 0xE0, 0x93, 0xF3, 0xA3, 0xB5, 0x01, 0x00, 0x40, \

19 0x6E

20

[ 28](log__backend__ble_8h.md#a54f16cb2a3e183f47110b49af97c6062)typedef void (\*[logger\_backend\_ble\_hook](log__backend__ble_8h.md#a54f16cb2a3e183f47110b49af97c6062))(bool backend\_status, void \*ctx);

29

[ 40](log__backend__ble_8h.md#a324e2709a95362f3c83aaa89facca2cc)void [logger\_backend\_ble\_set\_hook](log__backend__ble_8h.md#a324e2709a95362f3c83aaa89facca2cc)([logger\_backend\_ble\_hook](log__backend__ble_8h.md#a54f16cb2a3e183f47110b49af97c6062) hook, void \*ctx);

41

42#endif /\* ZEPHYR\_LOG\_BACKEND\_BLE\_H\_ \*/

[logger\_backend\_ble\_set\_hook](log__backend__ble_8h.md#a324e2709a95362f3c83aaa89facca2cc)

void logger\_backend\_ble\_set\_hook(logger\_backend\_ble\_hook hook, void \*ctx)

Allows application to add a hook for the status of the Bluetooth logger backend.

[logger\_backend\_ble\_hook](log__backend__ble_8h.md#a54f16cb2a3e183f47110b49af97c6062)

void(\* logger\_backend\_ble\_hook)(bool backend\_status, void \*ctx)

Hook for application to know when the Bluetooth backend is enabled or disabled.

**Definition** log\_backend\_ble.h:28

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_ble.h](log__backend__ble_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
