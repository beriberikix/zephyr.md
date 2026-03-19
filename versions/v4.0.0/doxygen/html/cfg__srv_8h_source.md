---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cfg__srv_8h_source.html
original_path: doxygen/html/cfg__srv_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cfg\_srv.h

[Go to the documentation of this file.](cfg__srv_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CFG\_SRV\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CFG\_SRV\_H\_

12

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 27](group__bt__mesh__cfg__srv.md#gafc6b9dea9f72d5754c1a4b42bfafd656)#define BT\_MESH\_MODEL\_CFG\_SRV \

28 BT\_MESH\_MODEL\_CNT\_CB(BT\_MESH\_MODEL\_ID\_CFG\_SRV, \

29 bt\_mesh\_cfg\_srv\_op, NULL, \

30 NULL, 1, 0, &bt\_mesh\_cfg\_srv\_cb)

31

33extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) bt\_mesh\_cfg\_srv\_op[];

34extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) bt\_mesh\_cfg\_srv\_cb;

36

37#ifdef \_\_cplusplus

38}

39#endif

40

44

45#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CFG\_SRV\_H\_ \*/

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [cfg\_srv.h](cfg__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
