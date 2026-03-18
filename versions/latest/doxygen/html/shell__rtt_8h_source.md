---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__rtt_8h_source.html
original_path: doxygen/html/shell__rtt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_rtt.h

[Go to the documentation of this file.](shell__rtt_8h.md)

1/\*

2 \* Copyright (c) 2018 Makaio GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef SHELL\_RTT\_H\_\_

8#define SHELL\_RTT\_H\_\_

9

10#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_rtt\_transport\_api](shell__rtt_8h.md#a981a63a78fb537843526cb19cdd667e4);

17

[ 18](structshell__rtt.md)struct [shell\_rtt](structshell__rtt.md) {

[ 19](structshell__rtt.md#a3ef62874e58dec11758b01a9e4c25320) [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) [handler](structshell__rtt.md#a3ef62874e58dec11758b01a9e4c25320);

[ 20](structshell__rtt.md#ad580036208bcf75b888f24d22516543f) struct k\_timer [timer](structshell__rtt.md#ad580036208bcf75b888f24d22516543f);

[ 21](structshell__rtt.md#ad19e5bf95e633ccec80d39d7bfe54a4c) void \*[context](structshell__rtt.md#ad19e5bf95e633ccec80d39d7bfe54a4c);

22};

23

[ 24](shell__rtt_8h.md#a58deb777f206a6afbc77c9d047204c7a)#define SHELL\_RTT\_DEFINE(\_name) \

25 static struct shell\_rtt \_name##\_shell\_rtt; \

26 struct shell\_transport \_name = { \

27 .api = &shell\_rtt\_transport\_api, \

28 .ctx = (struct shell\_rtt \*)&\_name##\_shell\_rtt \

29 }

30

[ 39](shell__rtt_8h.md#a74ccc10cf40cd54f6d4d28f5e62f3091)const struct [shell](structshell.md) \*[shell\_backend\_rtt\_get\_ptr](shell__rtt_8h.md#a74ccc10cf40cd54f6d4d28f5e62f3091)(void);

40#ifdef \_\_cplusplus

41}

42#endif

43

44#endif /\* SHELL\_RTT\_H\_\_ \*/

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:590

[shell.h](shell_2shell_8h.md)

[shell\_backend\_rtt\_get\_ptr](shell__rtt_8h.md#a74ccc10cf40cd54f6d4d28f5e62f3091)

const struct shell \* shell\_backend\_rtt\_get\_ptr(void)

Function provides pointer to shell rtt backend instance.

[shell\_rtt\_transport\_api](shell__rtt_8h.md#a981a63a78fb537843526cb19cdd667e4)

const struct shell\_transport\_api shell\_rtt\_transport\_api

[shell\_rtt](structshell__rtt.md)

**Definition** shell\_rtt.h:18

[shell\_rtt::handler](structshell__rtt.md#a3ef62874e58dec11758b01a9e4c25320)

shell\_transport\_handler\_t handler

**Definition** shell\_rtt.h:19

[shell\_rtt::context](structshell__rtt.md#ad19e5bf95e633ccec80d39d7bfe54a4c)

void \* context

**Definition** shell\_rtt.h:21

[shell\_rtt::timer](structshell__rtt.md#ad580036208bcf75b888f24d22516543f)

struct k\_timer timer

**Definition** shell\_rtt.h:20

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:612

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:852

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_rtt.h](shell__rtt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
