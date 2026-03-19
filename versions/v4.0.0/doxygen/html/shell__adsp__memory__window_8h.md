---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/shell__adsp__memory__window_8h.html
original_path: doxygen/html/shell__adsp__memory__window_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_adsp\_memory\_window.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`

[Go to the source code of this file.](shell__adsp__memory__window_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_adsp\_memory\_window](structshell__adsp__memory__window.md) |
|  | Memwindow based shell transport. [More...](structshell__adsp__memory__window.md#details) |

| Macros | |
| --- | --- |
| #define | [SHELL\_ADSP\_MEMORY\_WINDOW\_DEFINE](#a2d5483ee279894ca82bc14b41c3d3745)(\_name) |

| Functions | |
| --- | --- |
| const struct [shell](structshell.md) \* | [shell\_backend\_adsp\_memory\_window\_get\_ptr](#a03636e7b928b9c6a21d54270ba95480b) (void) |
|  | This function provides pointer to shell ADSP memory window backend instance. |

| Variables | |
| --- | --- |
| const struct [shell\_transport\_api](structshell__transport__api.md) | [shell\_adsp\_memory\_window\_transport\_api](#a47c6df5cd7aaf460925783c10db2d5de) |

## Macro Definition Documentation

## [◆ ](#a2d5483ee279894ca82bc14b41c3d3745)SHELL\_ADSP\_MEMORY\_WINDOW\_DEFINE

| #define SHELL\_ADSP\_MEMORY\_WINDOW\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [shell\_adsp\_memory\_window](structshell__adsp__memory__window.md) \_name##\_shell\_adsp\_memory\_window;\

struct [shell\_transport](structshell__transport.md) \_name = { \

.api = &[shell\_adsp\_memory\_window\_transport\_api](#a47c6df5cd7aaf460925783c10db2d5de), \

.ctx = &\_name##\_shell\_adsp\_memory\_window, \

}

[shell\_adsp\_memory\_window\_transport\_api](#a47c6df5cd7aaf460925783c10db2d5de)

const struct shell\_transport\_api shell\_adsp\_memory\_window\_transport\_api

[shell\_adsp\_memory\_window](structshell__adsp__memory__window.md)

Memwindow based shell transport.

**Definition** shell\_adsp\_memory\_window.h:22

[shell\_transport](structshell__transport.md)

**Definition** shell.h:724

## Function Documentation

## [◆ ](#a03636e7b928b9c6a21d54270ba95480b)shell\_backend\_adsp\_memory\_window\_get\_ptr()

| const struct [shell](structshell.md) \* shell\_backend\_adsp\_memory\_window\_get\_ptr | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

This function provides pointer to shell ADSP memory window backend instance.

Function returns pointer to the shell ADSP memory window instance. This instance can be next used with shell\_execute\_cmd function in order to test commands behavior.

Returns
:   Pointer to the shell instance.

## Variable Documentation

## [◆ ](#a47c6df5cd7aaf460925783c10db2d5de)shell\_adsp\_memory\_window\_transport\_api

| | const struct [shell\_transport\_api](structshell__transport__api.md) shell\_adsp\_memory\_window\_transport\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_adsp\_memory\_window.h](shell__adsp__memory__window_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
