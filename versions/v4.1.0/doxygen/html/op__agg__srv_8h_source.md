---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/op__agg__srv_8h_source.html
original_path: doxygen/html/op__agg__srv_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

op\_agg\_srv.h

[Go to the documentation of this file.](op__agg__srv_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef BT\_MESH\_OP\_AGG\_SRV\_H\_\_

8#define BT\_MESH\_OP\_AGG\_SRV\_H\_\_

9

10#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 32](group__bt__mesh__op__agg__srv.md#ga9729e918d83a5b86e2fb1d443d23558a)#define BT\_MESH\_MODEL\_OP\_AGG\_SRV \

33 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_OP\_AGG\_SRV, \_bt\_mesh\_op\_agg\_srv\_op, \

34 NULL, NULL, &\_bt\_mesh\_op\_agg\_srv\_cb)

35

37extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_op\_agg\_srv\_op[];

38extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_op\_agg\_srv\_cb;

40

44

45#ifdef \_\_cplusplus

46}

47#endif

48

49#endif /\* BT\_MESH\_OP\_AGG\_SRV\_H\_\_ \*/

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [op\_agg\_srv.h](op__agg__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
