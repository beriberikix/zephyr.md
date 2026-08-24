---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/rts5912__flash__api__ex_8h_source.html
original_path: doxygen/html/rts5912__flash__api__ex_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rts5912\_flash\_api\_ex.h

[Go to the documentation of this file.](rts5912__flash__api__ex_8h.md)

1/\*

2 \* Copyright (c) 2025 Realtek, SIBG-SD7

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_\_ZEPHYR\_INCLUDE\_DRIVERS\_RTS5912\_FLASH\_API\_EX\_H\_\_

7#define \_\_ZEPHYR\_INCLUDE\_DRIVERS\_RTS5912\_FLASH\_API\_EX\_H\_\_

8

[ 9](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839)enum [flash\_rts5912\_ex\_ops](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839) {

[ 10](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8) [FLASH\_RTS5912\_EX\_OP\_WR\_ENABLE](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8) = [FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3),

[ 11](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c) [FLASH\_RTS5912\_EX\_OP\_WR\_DISABLE](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c),

[ 12](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695) [FLASH\_RTS5912\_EX\_OP\_WR\_SR](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695),

[ 13](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584) [FLASH\_RTS5912\_EX\_OP\_WR\_SR2](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584),

[ 14](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e) [FLASH\_RTS5912\_EX\_OP\_RD\_SR](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e),

[ 15](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f) [FLASH\_RTS5912\_EX\_OP\_RD\_SR2](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f),

[ 16](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614) [FLASH\_RTS5912\_EX\_OP\_SET\_WP](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614),

[ 17](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e) [FLASH\_RTS5912\_EX\_OP\_GET\_WP](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e),

18};

19

20#endif /\* \_\_ZEPHYR\_INCLUDE\_DRIVERS\_RTS5912\_FLASH\_API\_EX\_H\_\_ \*/

[FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)

#define FLASH\_EX\_OP\_VENDOR\_BASE

**Definition** flash.h:682

[flash\_rts5912\_ex\_ops](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839)

flash\_rts5912\_ex\_ops

**Definition** rts5912\_flash\_api\_ex.h:9

[FLASH\_RTS5912\_EX\_OP\_RD\_SR](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e)

@ FLASH\_RTS5912\_EX\_OP\_RD\_SR

**Definition** rts5912\_flash\_api\_ex.h:14

[FLASH\_RTS5912\_EX\_OP\_SET\_WP](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614)

@ FLASH\_RTS5912\_EX\_OP\_SET\_WP

**Definition** rts5912\_flash\_api\_ex.h:16

[FLASH\_RTS5912\_EX\_OP\_GET\_WP](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e)

@ FLASH\_RTS5912\_EX\_OP\_GET\_WP

**Definition** rts5912\_flash\_api\_ex.h:17

[FLASH\_RTS5912\_EX\_OP\_WR\_SR](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695)

@ FLASH\_RTS5912\_EX\_OP\_WR\_SR

**Definition** rts5912\_flash\_api\_ex.h:12

[FLASH\_RTS5912\_EX\_OP\_WR\_DISABLE](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c)

@ FLASH\_RTS5912\_EX\_OP\_WR\_DISABLE

**Definition** rts5912\_flash\_api\_ex.h:11

[FLASH\_RTS5912\_EX\_OP\_WR\_ENABLE](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8)

@ FLASH\_RTS5912\_EX\_OP\_WR\_ENABLE

**Definition** rts5912\_flash\_api\_ex.h:10

[FLASH\_RTS5912\_EX\_OP\_RD\_SR2](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f)

@ FLASH\_RTS5912\_EX\_OP\_RD\_SR2

**Definition** rts5912\_flash\_api\_ex.h:15

[FLASH\_RTS5912\_EX\_OP\_WR\_SR2](rts5912__flash__api__ex_8h.md#a76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584)

@ FLASH\_RTS5912\_EX\_OP\_WR\_SR2

**Definition** rts5912\_flash\_api\_ex.h:13

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash](dir_b5b0d43e6264d65db716db62f9858e50.md)
- [rts5912\_flash\_api\_ex.h](rts5912__flash__api__ex_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
