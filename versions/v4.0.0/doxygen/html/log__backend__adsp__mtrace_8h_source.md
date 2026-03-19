---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__backend__adsp__mtrace_8h_source.html
original_path: doxygen/html/log__backend__adsp__mtrace_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_adsp\_mtrace.h

[Go to the documentation of this file.](log__backend__adsp__mtrace_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LOG\_BACKEND\_ADSP\_MTRACE\_H\_

8#define ZEPHYR\_LOG\_BACKEND\_ADSP\_MTRACE\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <stddef.h>

12

[ 20](log__backend__adsp__mtrace_8h.md#ab6362dba4defcd461d24a155763b465d)typedef void(\*[adsp\_mtrace\_log\_hook\_t](log__backend__adsp__mtrace_8h.md#ab6362dba4defcd461d24a155763b465d))(size\_t written, size\_t space\_left);

21

[ 28](log__backend__adsp__mtrace_8h.md#a9bb9152344270b8257182471443caa78)void [adsp\_mtrace\_log\_init](log__backend__adsp__mtrace_8h.md#a9bb9152344270b8257182471443caa78)([adsp\_mtrace\_log\_hook\_t](log__backend__adsp__mtrace_8h.md#ab6362dba4defcd461d24a155763b465d) hook);

29

[ 30](log__backend__adsp__mtrace_8h.md#aecd49115065234a120c75f450b799269)const struct [log\_backend](structlog__backend.md) \*[log\_backend\_adsp\_mtrace\_get](log__backend__adsp__mtrace_8h.md#aecd49115065234a120c75f450b799269)(void);

31

32#endif /\* ZEPHYR\_LOG\_BACKEND\_ADSP\_MTRACE\_H\_ \*/

[adsp\_mtrace\_log\_init](log__backend__adsp__mtrace_8h.md#a9bb9152344270b8257182471443caa78)

void adsp\_mtrace\_log\_init(adsp\_mtrace\_log\_hook\_t hook)

Initialize the Intel ADSP mtrace logger.

[adsp\_mtrace\_log\_hook\_t](log__backend__adsp__mtrace_8h.md#ab6362dba4defcd461d24a155763b465d)

void(\* adsp\_mtrace\_log\_hook\_t)(size\_t written, size\_t space\_left)

mtracelogger requires a hook for IPC messages

**Definition** log\_backend\_adsp\_mtrace.h:20

[log\_backend\_adsp\_mtrace\_get](log__backend__adsp__mtrace_8h.md#aecd49115065234a120c75f450b799269)

const struct log\_backend \* log\_backend\_adsp\_mtrace\_get(void)

[stdint.h](stdint_8h.md)

[log\_backend](structlog__backend.md)

Logger backend structure.

**Definition** log\_backend.h:94

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_adsp\_mtrace.h](log__backend__adsp__mtrace_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
