---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/od__priv__proxy__srv_8h_source.html
original_path: doxygen/html/od__priv__proxy__srv_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

od\_priv\_proxy\_srv.h

[Go to the documentation of this file.](od__priv__proxy__srv_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef BT\_MESH\_OD\_PRIV\_PROXY\_SRV\_H\_\_

8#define BT\_MESH\_OD\_PRIV\_PROXY\_SRV\_H\_\_

9

10#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 25](group__bt__mesh__od__priv__proxy__srv.md#gaa3c6451144f696ef9e67494165283c41)#define BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_SRV \

26 BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_SRV, \

27 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_SRV, \

28 \_bt\_mesh\_od\_priv\_proxy\_srv\_op, NULL, NULL, \

29 &\_bt\_mesh\_od\_priv\_proxy\_srv\_cb)

30

32extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_od\_priv\_proxy\_srv\_op[];

33extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_od\_priv\_proxy\_srv\_cb;

35

37

38#ifdef \_\_cplusplus

39}

40#endif

41

42#endif /\* BT\_MESH\_OD\_PRIV\_PROXY\_SRV\_H\_\_ \*/

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
- [od\_priv\_proxy\_srv.h](od__priv__proxy__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
