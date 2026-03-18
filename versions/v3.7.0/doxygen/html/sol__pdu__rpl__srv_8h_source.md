---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sol__pdu__rpl__srv_8h_source.html
original_path: doxygen/html/sol__pdu__rpl__srv_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sol\_pdu\_rpl\_srv.h

[Go to the documentation of this file.](sol__pdu__rpl__srv_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef BT\_MESH\_SOL\_PDU\_RPL\_SRV\_H\_\_

8#define BT\_MESH\_SOL\_PDU\_RPL\_SRV\_H\_\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

19

[ 23](group__bt__mesh__sol__pdu__rpl__srv.md#gab32d54a2d8e7020107063b292a70f7b6)#define BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_SRV \

24 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_SRV, \

25 \_bt\_mesh\_sol\_pdu\_rpl\_srv\_op, NULL, NULL, \

26 &\_bt\_mesh\_sol\_pdu\_rpl\_srv\_cb)

27

29extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_sol\_pdu\_rpl\_srv\_op[];

30extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_sol\_pdu\_rpl\_srv\_cb;

32

34

35#ifdef \_\_cplusplus

36}

37#endif

38#endif /\* BT\_MESH\_SOL\_PDU\_RPL\_SRV\_H\_\_ \*/

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:809

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [sol\_pdu\_rpl\_srv.h](sol__pdu__rpl__srv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
