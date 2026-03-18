---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/buf__loader_8h_source.html
original_path: doxygen/html/buf__loader_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

buf\_loader.h

[Go to the documentation of this file.](buf__loader_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LLEXT\_BUF\_LOADER\_H

8#define ZEPHYR\_LLEXT\_BUF\_LOADER\_H

9

10#include <[zephyr/llext/loader.h](loader_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

22

[ 26](structllext__buf__loader.md)struct [llext\_buf\_loader](structllext__buf__loader.md) {

[ 28](structllext__buf__loader.md#a8ffcae668c62c0e2488e4bf460a8a196) struct [llext\_loader](structllext__loader.md) [loader](structllext__buf__loader.md#a8ffcae668c62c0e2488e4bf460a8a196);

29

31 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf;

32 size\_t len;

33 size\_t pos;

35};

36

38int llext\_buf\_read(struct [llext\_loader](structllext__loader.md) \*ldr, void \*buf, size\_t len);

39int llext\_buf\_seek(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

40void \*llext\_buf\_peek(struct [llext\_loader](structllext__loader.md) \*ldr, size\_t pos);

42

[ 49](group__llext__buf__loader.md#ga9ca06c7c3e57f5284ce44c62f5cc2c02)#define LLEXT\_BUF\_LOADER(\_buf, \_buf\_len) \

50 { \

51 .loader = { \

52 .read = llext\_buf\_read, \

53 .seek = llext\_buf\_seek, \

54 .peek = llext\_buf\_peek, \

55 }, \

56 .buf = (\_buf), \

57 .len = (\_buf\_len), \

58 .pos = 0 \

59 }

60

64

65#ifdef \_\_cplusplus

66}

67#endif

68

69#endif /\* ZEPHYR\_LLEXT\_BUF\_LOADER\_H \*/

[loader.h](loader_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[llext\_buf\_loader](structllext__buf__loader.md)

An extension loader from a provided buffer containing an ELF.

**Definition** buf\_loader.h:26

[llext\_buf\_loader::loader](structllext__buf__loader.md#a8ffcae668c62c0e2488e4bf460a8a196)

struct llext\_loader loader

Extension loader.

**Definition** buf\_loader.h:28

[llext\_loader](structllext__loader.md)

Linkable loadable extension loader context.

**Definition** loader.h:29

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [buf\_loader.h](buf__loader_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
