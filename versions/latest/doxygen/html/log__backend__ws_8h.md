---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__backend__ws_8h.html
original_path: doxygen/html/log__backend__ws_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_ws.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](log__backend__ws_8h_source.md)

| Functions | |
| --- | --- |
| int | [log\_backend\_ws\_register](#abf3157cb42022eeea46cbe43c3824de0) (int fd) |
|  | Register websocket socket where the logging output is sent. |
| int | [log\_backend\_ws\_unregister](#a6026cf4df6ba455708ca58867dd66b72) (int fd) |
|  | Unregister websocket socket where the logging output was sent. |
| const struct [log\_backend](structlog__backend.md) \* | [log\_backend\_ws\_get](#ac502c554b139ba774bf1716126e36110) (void) |
|  | Get the websocket logger backend. |
| void | [log\_backend\_ws\_start](#a5501764d7eefda59e35990671be58387) (void) |
|  | Start the websocket logger backend. |

## Function Documentation

## [◆ ](#ac502c554b139ba774bf1716126e36110)log\_backend\_ws\_get()

| const struct [log\_backend](structlog__backend.md) \* log\_backend\_ws\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the websocket logger backend.

This function returns the websocket logger backend.

Returns
:   Pointer to the websocket logger backend.

## [◆ ](#abf3157cb42022eeea46cbe43c3824de0)log\_backend\_ws\_register()

| int log\_backend\_ws\_register | ( | int | *fd* | ) |  |
| --- | --- | --- | --- | --- | --- |

Register websocket socket where the logging output is sent.

Parameters
:   | fd | Websocket socket value. |
    | --- | --- |

Returns
:   0 if ok, <0 if error

## [◆ ](#a5501764d7eefda59e35990671be58387)log\_backend\_ws\_start()

| void log\_backend\_ws\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Start the websocket logger backend.

This function starts the websocket logger backend.

## [◆ ](#a6026cf4df6ba455708ca58867dd66b72)log\_backend\_ws\_unregister()

| int log\_backend\_ws\_unregister | ( | int | *fd* | ) |  |
| --- | --- | --- | --- | --- | --- |

Unregister websocket socket where the logging output was sent.

After this the websocket output is disabled.

Parameters
:   | fd | Websocket socket value. |
    | --- | --- |

Returns
:   0 if ok, <0 if error

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_ws.h](log__backend__ws_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
