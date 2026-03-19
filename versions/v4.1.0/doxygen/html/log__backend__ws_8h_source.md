---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__backend__ws_8h_source.html
original_path: doxygen/html/log__backend__ws_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_ws.h

[Go to the documentation of this file.](log__backend__ws_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_LOG\_BACKEND\_WS\_H\_

8#define ZEPHYR\_LOG\_BACKEND\_WS\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 23](log__backend__ws_8h.md#abf3157cb42022eeea46cbe43c3824de0)int [log\_backend\_ws\_register](log__backend__ws_8h.md#abf3157cb42022eeea46cbe43c3824de0)(int fd);

24

[ 34](log__backend__ws_8h.md#a6026cf4df6ba455708ca58867dd66b72)int [log\_backend\_ws\_unregister](log__backend__ws_8h.md#a6026cf4df6ba455708ca58867dd66b72)(int fd);

35

[ 43](log__backend__ws_8h.md#ac502c554b139ba774bf1716126e36110)const struct [log\_backend](structlog__backend.md) \*[log\_backend\_ws\_get](log__backend__ws_8h.md#ac502c554b139ba774bf1716126e36110)(void);

44

[ 50](log__backend__ws_8h.md#a5501764d7eefda59e35990671be58387)void [log\_backend\_ws\_start](log__backend__ws_8h.md#a5501764d7eefda59e35990671be58387)(void);

51

52#ifdef \_\_cplusplus

53}

54#endif

55

56#endif /\* ZEPHYR\_LOG\_BACKEND\_WS\_H\_ \*/

[log\_backend\_ws\_start](log__backend__ws_8h.md#a5501764d7eefda59e35990671be58387)

void log\_backend\_ws\_start(void)

Start the websocket logger backend.

[log\_backend\_ws\_unregister](log__backend__ws_8h.md#a6026cf4df6ba455708ca58867dd66b72)

int log\_backend\_ws\_unregister(int fd)

Unregister websocket socket where the logging output was sent.

[log\_backend\_ws\_register](log__backend__ws_8h.md#abf3157cb42022eeea46cbe43c3824de0)

int log\_backend\_ws\_register(int fd)

Register websocket socket where the logging output is sent.

[log\_backend\_ws\_get](log__backend__ws_8h.md#ac502c554b139ba774bf1716126e36110)

const struct log\_backend \* log\_backend\_ws\_get(void)

Get the websocket logger backend.

[stdbool.h](stdbool_8h.md)

[log\_backend](structlog__backend.md)

Logger backend structure.

**Definition** log\_backend.h:95

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_ws.h](log__backend__ws_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
