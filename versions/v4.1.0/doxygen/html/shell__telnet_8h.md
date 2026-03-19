---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shell__telnet_8h.html
original_path: doxygen/html/shell__telnet_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_telnet.h File Reference

`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`  
`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`

[Go to the source code of this file.](shell__telnet_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md) |
|  | Line buffer structure. [More...](structshell__telnet__line__buf.md#details) |
| struct | [shell\_telnet](structshell__telnet.md) |
|  | TELNET-based shell transport. [More...](structshell__telnet.md#details) |

| Macros | |
| --- | --- |
| #define | [SHELL\_TELNET\_POLLFD\_COUNT](#a6307a5cc6b33233351090fa871695609)   3 |
| #define | [SHELL\_TELNET\_MAX\_CMD\_SIZE](#ab3b85da7a39a8270dfa23bc099113528)   3 |
| #define | [SHELL\_TELNET\_DEFINE](#a82cf4289a4a5d724edd2d4d333eafe4e)(\_name) |

| Functions | |
| --- | --- |
| const struct [shell](structshell.md) \* | [shell\_backend\_telnet\_get\_ptr](#a628b99d20ef08a0b1165af07aee4888c) (void) |
|  | This function provides pointer to shell telnet backend instance. |

| Variables | |
| --- | --- |
| const struct [shell\_transport\_api](structshell__transport__api.md) | [shell\_telnet\_transport\_api](#a39f18c861db9a87f151285600d44014e) |

## Macro Definition Documentation

## [◆ ](#a82cf4289a4a5d724edd2d4d333eafe4e)SHELL\_TELNET\_DEFINE

| #define SHELL\_TELNET\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [shell\_telnet](structshell__telnet.md) \_name##\_shell\_telnet; \

struct [shell\_transport](structshell__transport.md) \_name = { \

.api = &[shell\_telnet\_transport\_api](#a39f18c861db9a87f151285600d44014e), \

.ctx = (struct [shell\_telnet](structshell__telnet.md) \*)&\_name##\_shell\_telnet \

}

[shell\_telnet\_transport\_api](#a39f18c861db9a87f151285600d44014e)

const struct shell\_transport\_api shell\_telnet\_transport\_api

[shell\_telnet](structshell__telnet.md)

TELNET-based shell transport.

**Definition** shell\_telnet.h:32

[shell\_transport](structshell__transport.md)

**Definition** shell.h:746

## [◆ ](#ab3b85da7a39a8270dfa23bc099113528)SHELL\_TELNET\_MAX\_CMD\_SIZE

| #define SHELL\_TELNET\_MAX\_CMD\_SIZE   3 |
| --- |

## [◆ ](#a6307a5cc6b33233351090fa871695609)SHELL\_TELNET\_POLLFD\_COUNT

| #define SHELL\_TELNET\_POLLFD\_COUNT   3 |
| --- |

## Function Documentation

## [◆ ](#a628b99d20ef08a0b1165af07aee4888c)shell\_backend\_telnet\_get\_ptr()

| const struct [shell](structshell.md) \* shell\_backend\_telnet\_get\_ptr | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

This function provides pointer to shell telnet backend instance.

Function returns pointer to the shell telnet instance. This instance can be next used with shell\_execute\_cmd function in order to test commands behavior.

Returns
:   Pointer to the shell instance.

## Variable Documentation

## [◆ ](#a39f18c861db9a87f151285600d44014e)shell\_telnet\_transport\_api

| | const struct [shell\_transport\_api](structshell__transport__api.md) shell\_telnet\_transport\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_telnet.h](shell__telnet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
