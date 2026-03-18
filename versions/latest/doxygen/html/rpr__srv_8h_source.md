---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rpr__srv_8h_source.html
original_path: doxygen/html/rpr__srv_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpr\_srv.h

[Go to the documentation of this file.](rpr__srv_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_SRV\_H\_\_

8#define ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_SRV\_H\_\_

9

10#include <[zephyr/bluetooth/bluetooth.h](bluetooth_8h.md)>

11#include <[zephyr/bluetooth/mesh/access.h](access_8h.md)>

12#include <[zephyr/bluetooth/mesh/rpr.h](rpr_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

23

[ 28](group__bt__mesh__rpr__srv.md#ga49c08c3e98b0c3863dd79b37aea25b34)#define BT\_MESH\_MODEL\_RPR\_SRV \

29 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_REMOTE\_PROV\_SRV, \

30 \_bt\_mesh\_rpr\_srv\_op, NULL, NULL, \

31 &\_bt\_mesh\_rpr\_srv\_cb)

32

34extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_rpr\_srv\_op[];

35extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_rpr\_srv\_cb;

37

39

40#ifdef \_\_cplusplus

41}

42#endif

43

44#endif /\* ZEPHYR\_INCLUDE\_BT\_MESH\_RPR\_SRV\_H\_\_ \*/

[access.h](access_8h.md)

Access layer APIs.

[bluetooth.h](bluetooth_8h.md)

Bluetooth subsystem core APIs.

[rpr.h](rpr_8h.md)

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:803

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [rpr\_srv.h](rpr__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
