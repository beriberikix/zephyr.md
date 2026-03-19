---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shell__backend_8h_source.html
original_path: doxygen/html/shell__backend_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_backend.h

[Go to the documentation of this file.](shell__backend_8h.md)

1/\*

2 \* Copyright (c) 2023 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SHELL\_BACKEND\_H\_

8#define ZEPHYR\_INCLUDE\_SHELL\_BACKEND\_H\_

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

12#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 25](shell__backend_8h.md#ad299b24f7d116d733c3f9ccc839fdb2b)static inline const struct [shell](structshell.md) \*[shell\_backend\_get](shell__backend_8h.md#ad299b24f7d116d733c3f9ccc839fdb2b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx)

26{

27 const struct [shell](structshell.md) \*backend;

28

29 [STRUCT\_SECTION\_GET](group__iterable__section__apis.md#ga583e57b527884034116bf0b27a942b50)([shell](structshell.md), idx, &backend);

30

31 return backend;

32}

33

[ 39](shell__backend_8h.md#afcf533acf3e0540c6798e58d4c1f7528)static inline int [shell\_backend\_count\_get](shell__backend_8h.md#afcf533acf3e0540c6798e58d4c1f7528)(void)

40{

41 int cnt;

42

43 [STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)([shell](structshell.md), &cnt);

44

45 return cnt;

46}

47

[ 55](shell__backend_8h.md#a34edbd459f8acce386a2f953bc6c795f)const struct [shell](structshell.md) \*[shell\_backend\_get\_by\_name](shell__backend_8h.md#a34edbd459f8acce386a2f953bc6c795f)(const char \*backend\_name);

56

57#ifdef \_\_cplusplus

58}

59#endif

60

61#endif /\* ZEPHYR\_INCLUDE\_SHELL\_BACKEND\_H\_ \*/

[STRUCT\_SECTION\_GET](group__iterable__section__apis.md#ga583e57b527884034116bf0b27a942b50)

#define STRUCT\_SECTION\_GET(struct\_type, i, dst)

Get element from section.

**Definition** iterable\_sections.h:282

[STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)

#define STRUCT\_SECTION\_COUNT(struct\_type, dst)

Count elements in a section.

**Definition** iterable\_sections.h:291

[types.h](include_2zephyr_2types_8h.md)

[shell.h](shell_2shell_8h.md)

[shell\_backend\_get\_by\_name](shell__backend_8h.md#a34edbd459f8acce386a2f953bc6c795f)

const struct shell \* shell\_backend\_get\_by\_name(const char \*backend\_name)

Get backend by name.

[shell\_backend\_get](shell__backend_8h.md#ad299b24f7d116d733c3f9ccc839fdb2b)

static const struct shell \* shell\_backend\_get(uint32\_t idx)

Get backend.

**Definition** shell\_backend.h:25

[shell\_backend\_count\_get](shell__backend_8h.md#afcf533acf3e0540c6798e58d4c1f7528)

static int shell\_backend\_count\_get(void)

Get number of backends.

**Definition** shell\_backend.h:39

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:912

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_backend.h](shell__backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
