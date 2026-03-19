---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__backend__std_8h_source.html
original_path: doxygen/html/log__backend__std_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_std.h

[Go to the documentation of this file.](log__backend__std_8h.md)

1/\*

2 \* Copyright (c) 2019 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_LOG\_BACKEND\_STD\_H\_

7#define ZEPHYR\_LOG\_BACKEND\_STD\_H\_

8

9#include <[zephyr/logging/log\_msg.h](log__msg_8h.md)>

10#include <[zephyr/logging/log\_output.h](log__output_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 24](group__log__backend__std.md#ga187212f5bcf701e57f3859338afa04ac)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_backend\_std\_get\_flags](group__log__backend__std.md#ga187212f5bcf701e57f3859338afa04ac)(void)

25{

26 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = ([LOG\_OUTPUT\_FLAG\_LEVEL](group__LOG__OUTPUT__FLAGS.md#ga4a9e9275950ea4f87b12fab1b311d598) | [LOG\_OUTPUT\_FLAG\_TIMESTAMP](group__LOG__OUTPUT__FLAGS.md#gad720632f631fcfbd3f1a57aaa6f627f4));

27

28 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_BACKEND\_SHOW\_COLOR)) {

29 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) |= [LOG\_OUTPUT\_FLAG\_COLORS](group__LOG__OUTPUT__FLAGS.md#gaff76f2c3b2f84eb212def15d3ec6d8d4);

30 }

31

32 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_BACKEND\_FORMAT\_TIMESTAMP)) {

33 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) |= [LOG\_OUTPUT\_FLAG\_FORMAT\_TIMESTAMP](group__LOG__OUTPUT__FLAGS.md#gad6da2da1aa7b511a8a1188afe5ca4ec7);

34 }

35

36 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_THREAD\_ID\_PREFIX)) {

37 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) |= [LOG\_OUTPUT\_FLAG\_THREAD](group__LOG__OUTPUT__FLAGS.md#ga37a3e1f964a2ee590368cee446b3ddc2);

38 }

39

40 return [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

41}

42

47static inline void

[ 48](group__log__backend__std.md#gae64f537029b579ae947a8ba4c5b2634d)[log\_backend\_std\_panic](group__log__backend__std.md#gae64f537029b579ae947a8ba4c5b2634d)(const struct [log\_output](structlog__output.md) \*const output)

49{

50 [log\_output\_flush](group__log__output.md#gae9309a649e6fe5448a941ef648d364a8)(output);

51}

52

58static inline void

[ 59](group__log__backend__std.md#gac79c5ea2d5f7a952f55ba21621120805)[log\_backend\_std\_dropped](group__log__backend__std.md#gac79c5ea2d5f7a952f55ba21621120805)(const struct [log\_output](structlog__output.md) \*const output, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt)

60{

61 [log\_output\_dropped\_process](group__log__output.md#ga10bbd405659afefdc7ffc686cb5a4f99)(output, cnt);

62}

63

67

68#ifdef \_\_cplusplus

69}

70#endif

71

72#endif /\* ZEPHYR\_LOG\_BACKEND\_STD\_H\_ \*/

[LOG\_OUTPUT\_FLAG\_THREAD](group__LOG__OUTPUT__FLAGS.md#ga37a3e1f964a2ee590368cee446b3ddc2)

#define LOG\_OUTPUT\_FLAG\_THREAD

Flag thread id or name prefix.

**Definition** log\_output.h:55

[LOG\_OUTPUT\_FLAG\_LEVEL](group__LOG__OUTPUT__FLAGS.md#ga4a9e9275950ea4f87b12fab1b311d598)

#define LOG\_OUTPUT\_FLAG\_LEVEL

Flag forcing severity level prefix.

**Definition** log\_output.h:42

[LOG\_OUTPUT\_FLAG\_FORMAT\_TIMESTAMP](group__LOG__OUTPUT__FLAGS.md#gad6da2da1aa7b511a8a1188afe5ca4ec7)

#define LOG\_OUTPUT\_FLAG\_FORMAT\_TIMESTAMP

Flag forcing timestamp formatting.

**Definition** log\_output.h:39

[LOG\_OUTPUT\_FLAG\_TIMESTAMP](group__LOG__OUTPUT__FLAGS.md#gad720632f631fcfbd3f1a57aaa6f627f4)

#define LOG\_OUTPUT\_FLAG\_TIMESTAMP

Flag forcing timestamp.

**Definition** log\_output.h:36

[LOG\_OUTPUT\_FLAG\_COLORS](group__LOG__OUTPUT__FLAGS.md#gaff76f2c3b2f84eb212def15d3ec6d8d4)

#define LOG\_OUTPUT\_FLAG\_COLORS

Flag forcing ANSI escape code colors, red (errors), yellow (warnings).

**Definition** log\_output.h:33

[log\_backend\_std\_get\_flags](group__log__backend__std.md#ga187212f5bcf701e57f3859338afa04ac)

static uint32\_t log\_backend\_std\_get\_flags(void)

**Definition** log\_backend\_std.h:24

[log\_backend\_std\_dropped](group__log__backend__std.md#gac79c5ea2d5f7a952f55ba21621120805)

static void log\_backend\_std\_dropped(const struct log\_output \*const output, uint32\_t cnt)

Report dropped messages to a standard logger backend.

**Definition** log\_backend\_std.h:59

[log\_backend\_std\_panic](group__log__backend__std.md#gae64f537029b579ae947a8ba4c5b2634d)

static void log\_backend\_std\_panic(const struct log\_output \*const output)

Put a standard logger backend into panic mode.

**Definition** log\_backend\_std.h:48

[log\_output\_dropped\_process](group__log__output.md#ga10bbd405659afefdc7ffc686cb5a4f99)

void log\_output\_dropped\_process(const struct log\_output \*output, uint32\_t cnt)

Process dropped messages indication.

[log\_output\_flush](group__log__output.md#gae9309a649e6fe5448a941ef648d364a8)

static void log\_output\_flush(const struct log\_output \*output)

Flush output buffer.

**Definition** log\_output.h:215

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

[kernel.h](kernel_8h.md)

Public kernel APIs.

[log\_msg.h](log__msg_8h.md)

[log\_output.h](log__output_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[log\_output](structlog__output.md)

Log\_output instance structure.

**Definition** log\_output.h:96

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_std.h](log__backend__std_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
