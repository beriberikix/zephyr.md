---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/smp__bt_8h_source.html
original_path: doxygen/html/smp__bt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_bt.h

[Go to the documentation of this file.](smp__bt_8h.md)

1/\*

2 \* Copyright Runtime.io 2018. All rights reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_MGMT\_SMP\_BT\_H\_

12#define ZEPHYR\_INCLUDE\_MGMT\_SMP\_BT\_H\_

13

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15struct bt\_conn;

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 27](smp__bt_8h.md#a9ceedfe6c84f194ff103356a4c30331f)int [smp\_bt\_register](smp__bt_8h.md#a9ceedfe6c84f194ff103356a4c30331f)(void);

28

[ 34](smp__bt_8h.md#ad19e1e1ba3ed59f13b5953bfda53ac15)int [smp\_bt\_unregister](smp__bt_8h.md#ad19e1e1ba3ed59f13b5953bfda53ac15)(void);

35

[ 46](smp__bt_8h.md#a8f52f0fda08b308dd7f1272b5ce5ba84)int [smp\_bt\_notify](smp__bt_8h.md#a8f52f0fda08b308dd7f1272b5ce5ba84)(struct bt\_conn \*conn, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

47

48#ifdef \_\_cplusplus

49}

50#endif

51

52#endif

[types.h](include_2zephyr_2types_8h.md)

[smp\_bt\_notify](smp__bt_8h.md#a8f52f0fda08b308dd7f1272b5ce5ba84)

int smp\_bt\_notify(struct bt\_conn \*conn, const void \*data, uint16\_t len)

Transmits an SMP command/response over the specified Bluetooth connection as a notification.

[smp\_bt\_register](smp__bt_8h.md#a9ceedfe6c84f194ff103356a4c30331f)

int smp\_bt\_register(void)

Registers the SMP Bluetooth service.

[smp\_bt\_unregister](smp__bt_8h.md#ad19e1e1ba3ed59f13b5953bfda53ac15)

int smp\_bt\_unregister(void)

Unregisters the SMP Bluetooth service.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_bt.h](smp__bt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
