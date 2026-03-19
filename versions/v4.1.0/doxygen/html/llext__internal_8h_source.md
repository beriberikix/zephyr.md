---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/llext__internal_8h_source.html
original_path: doxygen/html/llext__internal_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

llext\_internal.h

[Go to the documentation of this file.](llext__internal_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_INTERNAL\_H

8#define ZEPHYR\_LLEXT\_INTERNAL\_H

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

18

20

21struct [llext\_loader](structllext__loader.md);

22struct [llext](structllext.md);

23

24struct llext\_elf\_sect\_map {

25 enum [llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953) mem\_idx;

26 size\_t offset;

27};

28

29const void \*llext\_loaded\_sect\_ptr(struct [llext\_loader](structllext__loader.md) \*ldr, struct [llext](structllext.md) \*ext, unsigned int sh\_ndx);

30

32

33#ifdef \_\_cplusplus

34}

35#endif

36

37#endif /\* ZEPHYR\_LLEXT\_INTERNAL\_H \*/

[llext\_mem](group__llext__apis.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)

llext\_mem

List of memory regions stored or referenced in the LLEXT subsystem.

**Definition** llext.h:44

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:42

[llext](structllext.md)

Structure describing a linkable loadable extension.

**Definition** llext.h:77

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [llext\_internal.h](llext__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
