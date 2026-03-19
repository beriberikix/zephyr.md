---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/smp__bt_8h_source.html
original_path: doxygen/html/smp__bt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

14#include <[zephyr/bluetooth/uuid.h](uuid_8h.md)>

15#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

16struct bt\_conn;

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

[ 23](smp__bt_8h.md#a35a151d8a3e9fb6f5e2e355c0c23f17c)#define SMP\_BT\_SVC\_UUID\_VAL \

24 BT\_UUID\_128\_ENCODE(0x8d53dc1d, 0x1db7, 0x4cd3, 0x868b, 0x8a527460aa84)

25

[ 27](smp__bt_8h.md#afa04c341a4ed3b5a10c07d268266acc3)#define SMP\_BT\_SVC\_UUID \

28 BT\_UUID\_DECLARE\_128(SMP\_BT\_SVC\_UUID\_VAL)

29

[ 31](smp__bt_8h.md#a3f75f06a2f437008ecbe87474971a4ec)#define SMP\_BT\_CHR\_UUID\_VAL \

32 BT\_UUID\_128\_ENCODE(0xda2e7828, 0xfbce, 0x4e01, 0xae9e, 0x261174997c48)

33

[ 37](smp__bt_8h.md#aa42455942e31ddafc6174c5eca6f85ac)#define SMP\_BT\_CHR\_UUID \

38 BT\_UUID\_DECLARE\_128(SMP\_BT\_CHR\_UUID\_VAL)

39

[ 46](smp__bt_8h.md#a9ceedfe6c84f194ff103356a4c30331f)int [smp\_bt\_register](smp__bt_8h.md#a9ceedfe6c84f194ff103356a4c30331f)(void);

47

[ 53](smp__bt_8h.md#ad19e1e1ba3ed59f13b5953bfda53ac15)int [smp\_bt\_unregister](smp__bt_8h.md#ad19e1e1ba3ed59f13b5953bfda53ac15)(void);

54

[ 65](smp__bt_8h.md#a8f52f0fda08b308dd7f1272b5ce5ba84)int [smp\_bt\_notify](smp__bt_8h.md#a8f52f0fda08b308dd7f1272b5ce5ba84)(struct bt\_conn \*conn, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

66

67#ifdef \_\_cplusplus

68}

69#endif

70

71#endif

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

[uuid.h](uuid_8h.md)

Bluetooth UUID handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_bt.h](smp__bt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
