---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shell__rtt_8h.html
original_path: doxygen/html/shell__rtt_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_rtt.h File Reference

`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`

[Go to the source code of this file.](shell__rtt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_rtt](structshell__rtt.md) |

| Macros | |
| --- | --- |
| #define | [SHELL\_RTT\_DEFINE](#a58deb777f206a6afbc77c9d047204c7a)(\_name) |

| Functions | |
| --- | --- |
| const struct [shell](structshell.md) \* | [shell\_backend\_rtt\_get\_ptr](#a74ccc10cf40cd54f6d4d28f5e62f3091) (void) |
|  | Function provides pointer to shell rtt backend instance. |

| Variables | |
| --- | --- |
| const struct [shell\_transport\_api](structshell__transport__api.md) | [shell\_rtt\_transport\_api](#a981a63a78fb537843526cb19cdd667e4) |

## Macro Definition Documentation

## [◆ ](#a58deb777f206a6afbc77c9d047204c7a)SHELL\_RTT\_DEFINE

| #define SHELL\_RTT\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [shell\_rtt](structshell__rtt.md) \_name##\_shell\_rtt; \

struct [shell\_transport](structshell__transport.md) \_name = { \

.api = &[shell\_rtt\_transport\_api](#a981a63a78fb537843526cb19cdd667e4), \

.ctx = (struct [shell\_rtt](structshell__rtt.md) \*)&\_name##\_shell\_rtt \

}

[shell\_rtt\_transport\_api](#a981a63a78fb537843526cb19cdd667e4)

const struct shell\_transport\_api shell\_rtt\_transport\_api

[shell\_rtt](structshell__rtt.md)

**Definition** shell\_rtt.h:18

[shell\_transport](structshell__transport.md)

**Definition** shell.h:724

## Function Documentation

## [◆ ](#a74ccc10cf40cd54f6d4d28f5e62f3091)shell\_backend\_rtt\_get\_ptr()

| const struct [shell](structshell.md) \* shell\_backend\_rtt\_get\_ptr | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Function provides pointer to shell rtt backend instance.

Function returns pointer to the shell rtt instance. This instance can be next used with shell\_execute\_cmd function in order to test commands behavior.

Returns
:   Pointer to the shell instance.

## Variable Documentation

## [◆ ](#a981a63a78fb537843526cb19cdd667e4)shell\_rtt\_transport\_api

| | const struct [shell\_transport\_api](structshell__transport__api.md) shell\_rtt\_transport\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_rtt.h](shell__rtt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
