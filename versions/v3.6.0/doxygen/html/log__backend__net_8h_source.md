---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/log__backend__net_8h_source.html
original_path: doxygen/html/log__backend__net_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_net.h

[Go to the documentation of this file.](log__backend__net_8h.md)

1/\*

2 \* Copyright (c) 2023 David Corbeil

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LOG\_BACKEND\_NET\_H\_

8#define ZEPHYR\_LOG\_BACKEND\_NET\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 28](log__backend__net_8h.md#a127f2042973746f183bd3562821844cf)bool [log\_backend\_net\_set\_addr](log__backend__net_8h.md#a127f2042973746f183bd3562821844cf)(const char \*addr);

29

39#if defined(CONFIG\_NET\_HOSTNAME\_ENABLE)

40void [log\_backend\_net\_hostname\_set](log__backend__net_8h.md#a539dafe8aba869f11d244db4820baf8d)(char \*hostname, size\_t len);

41#else

[ 42](log__backend__net_8h.md#a539dafe8aba869f11d244db4820baf8d)static inline void [log\_backend\_net\_hostname\_set](log__backend__net_8h.md#a539dafe8aba869f11d244db4820baf8d)(const char \*hostname, size\_t len)

43{

44 ARG\_UNUSED(hostname);

45 ARG\_UNUSED(len);

46}

47#endif

48

49#ifdef \_\_cplusplus

50}

51#endif

52

53#endif /\* ZEPHYR\_LOG\_BACKEND\_NET\_H\_ \*/

[log\_backend\_net\_set\_addr](log__backend__net_8h.md#a127f2042973746f183bd3562821844cf)

bool log\_backend\_net\_set\_addr(const char \*addr)

Allows user to set a server IP address at runtime.

[log\_backend\_net\_hostname\_set](log__backend__net_8h.md#a539dafe8aba869f11d244db4820baf8d)

static void log\_backend\_net\_hostname\_set(const char \*hostname, size\_t len)

update the hostname

**Definition** log\_backend\_net.h:42

[stdbool.h](stdbool_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_net.h](log__backend__net_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
