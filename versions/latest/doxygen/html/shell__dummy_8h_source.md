---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__dummy_8h_source.html
original_path: doxygen/html/shell__dummy_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_dummy.h

[Go to the documentation of this file.](shell__dummy_8h.md)

1/\*

2 \* Shell backend used for testing

3 \*

4 \* Copyright (c) 2018 Nordic Semiconductor ASA

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef SHELL\_DUMMY\_H\_\_

10#define SHELL\_DUMMY\_H\_\_

11

12#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_dummy\_transport\_api](shell__dummy_8h.md#a26384803c3ef08c2c357f2c383f837e6);

19

[ 20](structshell__dummy.md)struct [shell\_dummy](structshell__dummy.md) {

[ 21](structshell__dummy.md#a18b0aa67864bbb1bedb0af574d433cc8) bool [initialized](structshell__dummy.md#a18b0aa67864bbb1bedb0af574d433cc8);

22

[ 24](structshell__dummy.md#a2eb3c3976f7d0d22318ba376ca3617c9) size\_t [len](structshell__dummy.md#a2eb3c3976f7d0d22318ba376ca3617c9);

25

[ 27](structshell__dummy.md#a3d227470504d3c565cdd5ff3408b69d3) char [buf](structshell__dummy.md#a3d227470504d3c565cdd5ff3408b69d3)[CONFIG\_SHELL\_BACKEND\_DUMMY\_BUF\_SIZE];

28};

29

[ 30](shell__dummy_8h.md#ab54399f9fbe08aafb9a7bdf540ff1c70)#define SHELL\_DUMMY\_DEFINE(\_name) \

31 static struct shell\_dummy \_name##\_shell\_dummy; \

32 struct shell\_transport \_name = { \

33 .api = &shell\_dummy\_transport\_api, \

34 .ctx = (struct shell\_dummy \*)&\_name##\_shell\_dummy \

35 }

36

[ 46](shell__dummy_8h.md#a12827fc2f644eb4748408807d763419e)const struct [shell](structshell.md) \*[shell\_backend\_dummy\_get\_ptr](shell__dummy_8h.md#a12827fc2f644eb4748408807d763419e)(void);

47

[ 57](shell__dummy_8h.md#aa93489d27aab568d3ca04640e9d18391)const char \*[shell\_backend\_dummy\_get\_output](shell__dummy_8h.md#aa93489d27aab568d3ca04640e9d18391)(const struct [shell](structshell.md) \*sh,

58 size\_t \*sizep);

59

[ 65](shell__dummy_8h.md#a8eb6e736190c11fe4a6eb6a02a48f44f)void [shell\_backend\_dummy\_clear\_output](shell__dummy_8h.md#a8eb6e736190c11fe4a6eb6a02a48f44f)(const struct [shell](structshell.md) \*sh);

66

67#ifdef \_\_cplusplus

68}

69#endif

70

71#endif /\* SHELL\_DUMMY\_H\_\_ \*/

[shell.h](shell_2shell_8h.md)

[shell\_backend\_dummy\_get\_ptr](shell__dummy_8h.md#a12827fc2f644eb4748408807d763419e)

const struct shell \* shell\_backend\_dummy\_get\_ptr(void)

This function shall not be used directly.

[shell\_dummy\_transport\_api](shell__dummy_8h.md#a26384803c3ef08c2c357f2c383f837e6)

const struct shell\_transport\_api shell\_dummy\_transport\_api

[shell\_backend\_dummy\_clear\_output](shell__dummy_8h.md#a8eb6e736190c11fe4a6eb6a02a48f44f)

void shell\_backend\_dummy\_clear\_output(const struct shell \*sh)

Clears the output buffer in the shell backend.

[shell\_backend\_dummy\_get\_output](shell__dummy_8h.md#aa93489d27aab568d3ca04640e9d18391)

const char \* shell\_backend\_dummy\_get\_output(const struct shell \*sh, size\_t \*sizep)

Returns the buffered output in the shell and resets the pointer.

[shell\_dummy](structshell__dummy.md)

**Definition** shell\_dummy.h:20

[shell\_dummy::initialized](structshell__dummy.md#a18b0aa67864bbb1bedb0af574d433cc8)

bool initialized

**Definition** shell\_dummy.h:21

[shell\_dummy::len](structshell__dummy.md#a2eb3c3976f7d0d22318ba376ca3617c9)

size\_t len

current number of bytes in buffer (0 if no output)

**Definition** shell\_dummy.h:24

[shell\_dummy::buf](structshell__dummy.md#a3d227470504d3c565cdd5ff3408b69d3)

char buf[CONFIG\_SHELL\_BACKEND\_DUMMY\_BUF\_SIZE]

output buffer to collect shell output

**Definition** shell\_dummy.h:27

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:612

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:852

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_dummy.h](shell__dummy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
