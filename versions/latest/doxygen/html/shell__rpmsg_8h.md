---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shell__rpmsg_8h.html
original_path: doxygen/html/shell__rpmsg_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_rpmsg.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`  
`#include <openamp/rpmsg.h>`

[Go to the source code of this file.](shell__rpmsg_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_rpmsg\_rx](structshell__rpmsg__rx.md) |
|  | RPMsg received message placeholder. [More...](structshell__rpmsg__rx.md#details) |
| struct | [shell\_rpmsg](structshell__rpmsg.md) |
|  | RPMsg-based shell transport. [More...](structshell__rpmsg.md#details) |

| Macros | |
| --- | --- |
| #define | [SHELL\_RPMSG\_DEFINE](#a95bbdb52f1dab7231087cc94fba5a62c)(\_name) |

| Functions | |
| --- | --- |
| int | [shell\_backend\_rpmsg\_init\_transport](#adf66e74fc7cf312979d8b79d4dffbbf5) (struct rpmsg\_device \*rpmsg\_dev) |
|  | Initialize the Shell backend using the provided `rpmsg_dev` device. |
| const struct [shell](structshell.md) \* | [shell\_backend\_rpmsg\_get\_ptr](#a486b7ee360b0cb75ab6df977464c4878) (void) |
|  | This function provides pointer to shell RPMsg backend instance. |

| Variables | |
| --- | --- |
| const struct [shell\_transport\_api](structshell__transport__api.md) | [shell\_rpmsg\_transport\_api](#a9189ca38b2b0d084a9169828abcf91d7) |

## Macro Definition Documentation

## [◆ ](#a95bbdb52f1dab7231087cc94fba5a62c)SHELL\_RPMSG\_DEFINE

| #define SHELL\_RPMSG\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [shell\_rpmsg](structshell__rpmsg.md) \_name##\_shell\_rpmsg; \

struct [shell\_transport](structshell__transport.md) \_name = { \

.api = &[shell\_rpmsg\_transport\_api](#a9189ca38b2b0d084a9169828abcf91d7), \

.ctx = (struct [shell\_rpmsg](structshell__rpmsg.md) \*)&\_name##\_shell\_rpmsg, \

}

[shell\_rpmsg\_transport\_api](#a9189ca38b2b0d084a9169828abcf91d7)

const struct shell\_transport\_api shell\_rpmsg\_transport\_api

[shell\_rpmsg](structshell__rpmsg.md)

RPMsg-based shell transport.

**Definition** shell\_rpmsg.h:29

[shell\_transport](structshell__transport.md)

**Definition** shell.h:724

## Function Documentation

## [◆ ](#a486b7ee360b0cb75ab6df977464c4878)shell\_backend\_rpmsg\_get\_ptr()

| const struct [shell](structshell.md) \* shell\_backend\_rpmsg\_get\_ptr | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

This function provides pointer to shell RPMsg backend instance.

Function returns pointer to the shell RPMsg instance. This instance can be next used with shell\_execute\_cmd function in order to test commands behavior.

Returns
:   Pointer to the shell instance.

## [◆ ](#adf66e74fc7cf312979d8b79d4dffbbf5)shell\_backend\_rpmsg\_init\_transport()

| int shell\_backend\_rpmsg\_init\_transport | ( | struct rpmsg\_device \* | *rpmsg\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize the Shell backend using the provided `rpmsg_dev` device.

Parameters
:   | rpmsg\_dev | A pointer to an RPMsg device |
    | --- | --- |

Returns
:   0 on success or a negative value on error

## Variable Documentation

## [◆ ](#a9189ca38b2b0d084a9169828abcf91d7)shell\_rpmsg\_transport\_api

| | const struct [shell\_transport\_api](structshell__transport__api.md) shell\_rpmsg\_transport\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_rpmsg.h](shell__rpmsg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
