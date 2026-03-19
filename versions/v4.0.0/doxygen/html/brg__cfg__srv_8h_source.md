---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/brg__cfg__srv_8h_source.html
original_path: doxygen/html/brg__cfg__srv_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

brg\_cfg\_srv.h

[Go to the documentation of this file.](brg__cfg__srv_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_SRV\_H\_\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_SRV\_H\_\_

12

13#include <[zephyr/bluetooth/mesh/brg\_cfg.h](brg__cfg_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

25

[ 30](group__bt__mesh__brg__cfg__srv.md#ga54e0629a3ae842e7c57a69f2cdab98e3)#define BT\_MESH\_MODEL\_BRG\_CFG\_SRV \

31 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_BRG\_CFG\_SRV, \_bt\_mesh\_brg\_cfg\_srv\_op, NULL, NULL, \

32 &\_bt\_mesh\_brg\_cfg\_srv\_cb)

33

35extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_brg\_cfg\_srv\_op[];

36extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_brg\_cfg\_srv\_cb;

38

42

43#ifdef \_\_cplusplus

44}

45#endif

46

47#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_SRV\_H\_\_ \*/

[brg\_cfg.h](brg__cfg_8h.md)

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [brg\_cfg\_srv.h](brg__cfg__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
