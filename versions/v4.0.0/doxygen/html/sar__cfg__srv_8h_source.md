---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sar__cfg__srv_8h_source.html
original_path: doxygen/html/sar__cfg__srv_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sar\_cfg\_srv.h

[Go to the documentation of this file.](sar__cfg__srv_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10#ifndef BT\_MESH\_SAR\_CFG\_SRV\_H\_\_

11#define BT\_MESH\_SAR\_CFG\_SRV\_H\_\_

12

13#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

14#include <[zephyr/bluetooth/mesh/sar\_cfg.h](sar__cfg_8h.md)>

15

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 31](group__bt__mesh__sar__cfg__srv.md#gaddb9214dd96ad476aac4f9a8947dfd45)#define BT\_MESH\_MODEL\_SAR\_CFG\_SRV \

32 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_SAR\_CFG\_SRV, bt\_mesh\_sar\_cfg\_srv\_op, \

33 NULL, NULL, &bt\_mesh\_sar\_cfg\_srv\_cb)

34

36extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) bt\_mesh\_sar\_cfg\_srv\_op[];

37extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) bt\_mesh\_sar\_cfg\_srv\_cb;

39

40#ifdef \_\_cplusplus

41}

42#endif

43

44#endif /\* BT\_MESH\_SAR\_CFG\_SRV\_H\_\_ \*/

45

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[sar\_cfg.h](sar__cfg_8h.md)

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [sar\_cfg\_srv.h](sar__cfg__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
