---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__history_8h_source.html
original_path: doxygen/html/shell__history_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_history.h

[Go to the documentation of this file.](shell__history_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef SHELL\_HISTORY\_H\_\_

8#define SHELL\_HISTORY\_H\_\_

9

10#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

11#include <[zephyr/sys/util.h](util_8h.md)>

12#include <[zephyr/sys/dlist.h](dlist_8h.md)>

13#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

14#include <[stdbool.h](stdbool_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

20

[ 21](structshell__history.md)struct [shell\_history](structshell__history.md) {

[ 22](structshell__history.md#a8e9fbd6e179a1a8063eb80df04b86395) struct [ring\_buf](structshell__history.md#a8e9fbd6e179a1a8063eb80df04b86395) \*[ring\_buf](structshell__history.md#a8e9fbd6e179a1a8063eb80df04b86395);

[ 23](structshell__history.md#af3b256c6fdb29eddedadcc2720e0b2c3) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [list](structshell__history.md#af3b256c6fdb29eddedadcc2720e0b2c3);

[ 24](structshell__history.md#a3f7d85e4e3123048e5a7d758d54a8602) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) \*[current](structshell__history.md#a3f7d85e4e3123048e5a7d758d54a8602);

25};

26

33#define Z\_SHELL\_HISTORY\_DEFINE(\_name, \_size) \

34 static uint8\_t \_\_noinit \_\_aligned(sizeof(void \*)) \

35 \_name##\_ring\_buf\_data[\_size]; \

36 static struct ring\_buf \_name##\_ring\_buf = \

37 { \

38 .size = \_size, \

39 .buffer = \_name##\_ring\_buf\_data \

40 }; \

41 static struct shell\_history \_name = { \

42 .ring\_buf = &\_name##\_ring\_buf \

43 }

44

45

51void z\_shell\_history\_init(struct [shell\_history](structshell__history.md) \*history);

52

61void z\_shell\_history\_purge(struct [shell\_history](structshell__history.md) \*history);

62

68void z\_shell\_history\_mode\_exit(struct [shell\_history](structshell__history.md) \*history);

69

82bool z\_shell\_history\_get(struct [shell\_history](structshell__history.md) \*history, bool up,

83 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*len);

84

95void z\_shell\_history\_put(struct [shell\_history](structshell__history.md) \*history, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*line,

96 size\_t len);

97

105static inline bool z\_shell\_history\_active(struct [shell\_history](structshell__history.md) \*history)

106{

107 return (history->[current](structshell__history.md#a3f7d85e4e3123048e5a7d758d54a8602)) ? [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) : false;

108}

109

110#ifdef \_\_cplusplus

111}

112#endif

113

114#endif /\* SHELL\_HISTORY\_H\_\_ \*/

[dlist.h](dlist_8h.md)

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:55

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:51

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[ring\_buffer.h](ring__buffer_8h.md)

[stdbool.h](stdbool_8h.md)

[true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

#define true

**Definition** stdbool.h:14

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[shell\_history](structshell__history.md)

**Definition** shell\_history.h:21

[shell\_history::current](structshell__history.md#a3f7d85e4e3123048e5a7d758d54a8602)

sys\_dnode\_t \* current

**Definition** shell\_history.h:24

[shell\_history::ring\_buf](structshell__history.md#a8e9fbd6e179a1a8063eb80df04b86395)

struct ring\_buf \* ring\_buf

**Definition** shell\_history.h:22

[shell\_history::list](structshell__history.md#af3b256c6fdb29eddedadcc2720e0b2c3)

sys\_dlist\_t list

**Definition** shell\_history.h:23

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_history.h](shell__history_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
