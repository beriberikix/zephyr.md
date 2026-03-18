---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__dummy_8h.html
original_path: doxygen/html/shell__dummy_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_dummy.h File Reference

`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`

[Go to the source code of this file.](shell__dummy_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_dummy](structshell__dummy.md) |

| Macros | |
| --- | --- |
| #define | [SHELL\_DUMMY\_DEFINE](#ab54399f9fbe08aafb9a7bdf540ff1c70)(\_name) |

| Functions | |
| --- | --- |
| const struct [shell](structshell.md) \* | [shell\_backend\_dummy\_get\_ptr](#a12827fc2f644eb4748408807d763419e) (void) |
|  | This function shall not be used directly. |
| const char \* | [shell\_backend\_dummy\_get\_output](#aa93489d27aab568d3ca04640e9d18391) (const struct [shell](structshell.md) \*sh, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*sizep) |
|  | Returns the buffered output in the shell and resets the pointer. |
| void | [shell\_backend\_dummy\_clear\_output](#a8eb6e736190c11fe4a6eb6a02a48f44f) (const struct [shell](structshell.md) \*sh) |
|  | Clears the output buffer in the shell backend. |

| Variables | |
| --- | --- |
| const struct [shell\_transport\_api](structshell__transport__api.md) | [shell\_dummy\_transport\_api](#a26384803c3ef08c2c357f2c383f837e6) |

## Macro Definition Documentation

## [◆ ](#ab54399f9fbe08aafb9a7bdf540ff1c70)SHELL\_DUMMY\_DEFINE

| #define SHELL\_DUMMY\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [shell\_dummy](structshell__dummy.md) \_name##\_shell\_dummy; \

struct [shell\_transport](structshell__transport.md) \_name = { \

.api = &[shell\_dummy\_transport\_api](#a26384803c3ef08c2c357f2c383f837e6), \

.ctx = (struct [shell\_dummy](structshell__dummy.md) \*)&\_name##\_shell\_dummy \

}

[shell\_dummy\_transport\_api](#a26384803c3ef08c2c357f2c383f837e6)

const struct shell\_transport\_api shell\_dummy\_transport\_api

[shell\_dummy](structshell__dummy.md)

**Definition** shell\_dummy.h:20

[shell\_transport](structshell__transport.md)

**Definition** shell.h:690

## Function Documentation

## [◆ ](#a8eb6e736190c11fe4a6eb6a02a48f44f)shell\_backend\_dummy\_clear\_output()

| void shell\_backend\_dummy\_clear\_output | ( | const struct [shell](structshell.md) \* | *sh* | ) |  |
| --- | --- | --- | --- | --- | --- |

Clears the output buffer in the shell backend.

Parameters
:   | sh | Shell pointer |
    | --- | --- |

## [◆ ](#aa93489d27aab568d3ca04640e9d18391)shell\_backend\_dummy\_get\_output()

| const char \* shell\_backend\_dummy\_get\_output | ( | const struct [shell](structshell.md) \* | *sh*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *sizep* ) |

Returns the buffered output in the shell and resets the pointer.

The returned data is always followed by a nul character at position \*sizep

Parameters
:   | sh | Shell pointer |
    | --- | --- |
    | sizep | Returns size of data in shell buffer |

Returns
:   pointer to buffer containing shell output

## [◆ ](#a12827fc2f644eb4748408807d763419e)shell\_backend\_dummy\_get\_ptr()

| const struct [shell](structshell.md) \* shell\_backend\_dummy\_get\_ptr | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

This function shall not be used directly.

It provides pointer to shell dummy backend instance.

Function returns pointer to the shell dummy instance. This instance can be next used with shell\_execute\_cmd function in order to test commands behavior.

Returns
:   Pointer to the shell instance.

## Variable Documentation

## [◆ ](#a26384803c3ef08c2c357f2c383f837e6)shell\_dummy\_transport\_api

| | const struct [shell\_transport\_api](structshell__transport__api.md) shell\_dummy\_transport\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_dummy.h](shell__dummy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
