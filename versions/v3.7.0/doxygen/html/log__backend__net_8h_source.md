---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/log__backend__net_8h_source.html
original_path: doxygen/html/log__backend__net_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

11#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 29](log__backend__net_8h.md#a127f2042973746f183bd3562821844cf)bool [log\_backend\_net\_set\_addr](log__backend__net_8h.md#a127f2042973746f183bd3562821844cf)(const char \*addr);

30

[ 43](log__backend__net_8h.md#aae909fb9ee8e4dbd773f44a2666dfa3a)bool [log\_backend\_net\_set\_ip](log__backend__net_8h.md#aae909fb9ee8e4dbd773f44a2666dfa3a)(const struct [sockaddr](structsockaddr.md) \*addr);

44

54#if defined(CONFIG\_NET\_HOSTNAME\_ENABLE)

55void [log\_backend\_net\_hostname\_set](log__backend__net_8h.md#a539dafe8aba869f11d244db4820baf8d)(char \*hostname, size\_t len);

56#else

[ 57](log__backend__net_8h.md#a539dafe8aba869f11d244db4820baf8d)static inline void [log\_backend\_net\_hostname\_set](log__backend__net_8h.md#a539dafe8aba869f11d244db4820baf8d)(const char \*hostname, size\_t len)

58{

59 ARG\_UNUSED(hostname);

60 ARG\_UNUSED(len);

61}

62#endif

63

[ 71](log__backend__net_8h.md#a6513cd9aabc8f594347d14901112f32e)const struct [log\_backend](structlog__backend.md) \*[log\_backend\_net\_get](log__backend__net_8h.md#a6513cd9aabc8f594347d14901112f32e)(void);

72

[ 78](log__backend__net_8h.md#aab57f963e8a9e88b1e9483872e737466)void [log\_backend\_net\_start](log__backend__net_8h.md#aab57f963e8a9e88b1e9483872e737466)(void);

79

80#ifdef \_\_cplusplus

81}

82#endif

83

84#endif /\* ZEPHYR\_LOG\_BACKEND\_NET\_H\_ \*/

[log\_backend\_net\_set\_addr](log__backend__net_8h.md#a127f2042973746f183bd3562821844cf)

bool log\_backend\_net\_set\_addr(const char \*addr)

Allows user to set a server IP address, provided as string, at runtime.

[log\_backend\_net\_hostname\_set](log__backend__net_8h.md#a539dafe8aba869f11d244db4820baf8d)

static void log\_backend\_net\_hostname\_set(const char \*hostname, size\_t len)

update the hostname

**Definition** log\_backend\_net.h:57

[log\_backend\_net\_get](log__backend__net_8h.md#a6513cd9aabc8f594347d14901112f32e)

const struct log\_backend \* log\_backend\_net\_get(void)

Get the net logger backend.

[log\_backend\_net\_start](log__backend__net_8h.md#aab57f963e8a9e88b1e9483872e737466)

void log\_backend\_net\_start(void)

Start the net logger backend.

[log\_backend\_net\_set\_ip](log__backend__net_8h.md#aae909fb9ee8e4dbd773f44a2666dfa3a)

bool log\_backend\_net\_set\_ip(const struct sockaddr \*addr)

Allows user to set a server IP address, provided as sockaddr structure, at runtime.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[stdbool.h](stdbool_8h.md)

[log\_backend](structlog__backend.md)

Logger backend structure.

**Definition** log\_backend.h:94

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_net.h](log__backend__net_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
