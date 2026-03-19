---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cbprintf__enums_8h_source.html
original_path: doxygen/html/cbprintf__enums_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cbprintf\_enums.h

[Go to the documentation of this file.](cbprintf__enums_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_ENUMS\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_ENUMS\_H\_

9

[ 15](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976b)enum [cbprintf\_package\_arg\_type](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976b) {

[ 17](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba34275ebbde48f20f919cecf161785338) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_END](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba34275ebbde48f20f919cecf161785338) = 0,

18

[ 19](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba79025ff0bd14a42a6112d3f57d19157e) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_CHAR](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba79025ff0bd14a42a6112d3f57d19157e),

[ 20](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976bafd2b463b0646b4da744557634a0f4b90) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_CHAR](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976bafd2b463b0646b4da744557634a0f4b90),

21

[ 22](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba14a44a3d8e799cb7547ce070328b76d8) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_SHORT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba14a44a3d8e799cb7547ce070328b76d8),

[ 23](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba4dff71a5cf651c0f945de53f9ba7be55) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_SHORT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba4dff71a5cf651c0f945de53f9ba7be55),

24

[ 25](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baf97e06e7f012dfc5571c0f99f21cf581) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_INT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baf97e06e7f012dfc5571c0f99f21cf581),

[ 26](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba329e514df49a5b39f19e3ec78e96dda7) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_INT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba329e514df49a5b39f19e3ec78e96dda7),

27

[ 28](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba74d7c7d173a7dbf75480a2fbb125a89e) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba74d7c7d173a7dbf75480a2fbb125a89e),

[ 29](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976badaa8d77af2accfcf268c44488cc43ecf) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976badaa8d77af2accfcf268c44488cc43ecf),

30

[ 31](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba79adbef17165e0a196c389684a4ae78c) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_LONG](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba79adbef17165e0a196c389684a4ae78c),

[ 32](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976babbd5e36a8966537880cbac87142b3f8f) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG\_LONG](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976babbd5e36a8966537880cbac87142b3f8f),

33

[ 34](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba8fdb082bc438a3fe1d44de8f79ef0fdb) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_FLOAT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba8fdb082bc438a3fe1d44de8f79ef0fdb),

[ 35](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba7e63e24f76257799793f15815ab5b47a) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_DOUBLE](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba7e63e24f76257799793f15815ab5b47a),

[ 36](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baafa01b0585c800675ddb43e3e1a72fd4) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_DOUBLE](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baafa01b0585c800675ddb43e3e1a72fd4),

37

[ 38](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baa77a46e2ec92bfb6f14ef0b1a88baafa) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baa77a46e2ec92bfb6f14ef0b1a88baafa),

39

[ 40](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba90dec8ae7faa7fdf8f0e9f12aafa9fae) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba90dec8ae7faa7fdf8f0e9f12aafa9fae),

41

[ 42](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976bab169302a191fb7535dcd8e1fce2d617e) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_MAX](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976bab169302a191fb7535dcd8e1fce2d617e),

43

[ 44](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba600828d5404b54bc435850441ebaaba0) [CBPRINTF\_PACKAGE\_ARG\_TYPE\_COUNT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba600828d5404b54bc435850441ebaaba0) = [CBPRINTF\_PACKAGE\_ARG\_TYPE\_MAX](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976bab169302a191fb7535dcd8e1fce2d617e)

45};

46

47#endif /\* ZEPHYR\_INCLUDE\_SYS\_CBPRINTF\_ENUMS\_H\_ \*/

[cbprintf\_package\_arg\_type](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976b)

cbprintf\_package\_arg\_type

cbprintf package argument type

**Definition** cbprintf\_enums.h:15

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_SHORT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba14a44a3d8e799cb7547ce070328b76d8)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_SHORT

**Definition** cbprintf\_enums.h:22

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_INT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba329e514df49a5b39f19e3ec78e96dda7)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_INT

**Definition** cbprintf\_enums.h:26

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_END](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba34275ebbde48f20f919cecf161785338)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_END

End of argument list.

**Definition** cbprintf\_enums.h:17

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_SHORT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba4dff71a5cf651c0f945de53f9ba7be55)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_SHORT

**Definition** cbprintf\_enums.h:23

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_COUNT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba600828d5404b54bc435850441ebaaba0)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_COUNT

**Definition** cbprintf\_enums.h:44

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba74d7c7d173a7dbf75480a2fbb125a89e)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG

**Definition** cbprintf\_enums.h:28

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_CHAR](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba79025ff0bd14a42a6112d3f57d19157e)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_CHAR

**Definition** cbprintf\_enums.h:19

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_LONG](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba79adbef17165e0a196c389684a4ae78c)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_LONG

**Definition** cbprintf\_enums.h:31

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_DOUBLE](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba7e63e24f76257799793f15815ab5b47a)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_DOUBLE

**Definition** cbprintf\_enums.h:35

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_FLOAT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba8fdb082bc438a3fe1d44de8f79ef0fdb)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_FLOAT

**Definition** cbprintf\_enums.h:34

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976ba90dec8ae7faa7fdf8f0e9f12aafa9fae)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_VOID

**Definition** cbprintf\_enums.h:40

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baa77a46e2ec92bfb6f14ef0b1a88baafa)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_PTR\_CHAR

**Definition** cbprintf\_enums.h:38

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_DOUBLE](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baafa01b0585c800675ddb43e3e1a72fd4)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_LONG\_DOUBLE

**Definition** cbprintf\_enums.h:36

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_MAX](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976bab169302a191fb7535dcd8e1fce2d617e)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_MAX

**Definition** cbprintf\_enums.h:42

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG\_LONG](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976babbd5e36a8966537880cbac87142b3f8f)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG\_LONG

**Definition** cbprintf\_enums.h:32

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976badaa8d77af2accfcf268c44488cc43ecf)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_LONG

**Definition** cbprintf\_enums.h:29

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_INT](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976baf97e06e7f012dfc5571c0f99f21cf581)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_INT

**Definition** cbprintf\_enums.h:25

[CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_CHAR](cbprintf__enums_8h.md#a7330fe0c9f113a6060326bf20c0d976bafd2b463b0646b4da744557634a0f4b90)

@ CBPRINTF\_PACKAGE\_ARG\_TYPE\_UNSIGNED\_CHAR

**Definition** cbprintf\_enums.h:20

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [cbprintf\_enums.h](cbprintf__enums_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
