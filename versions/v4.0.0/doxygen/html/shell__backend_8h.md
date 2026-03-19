---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/shell__backend_8h.html
original_path: doxygen/html/shell__backend_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_backend.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](shell__backend_8h_source.md)

| Functions | |
| --- | --- |
| static const struct [shell](structshell.md) \* | [shell\_backend\_get](#ad299b24f7d116d733c3f9ccc839fdb2b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx) |
|  | Get backend. |
| static int | [shell\_backend\_count\_get](#afcf533acf3e0540c6798e58d4c1f7528) (void) |
|  | Get number of backends. |
| const struct [shell](structshell.md) \* | [shell\_backend\_get\_by\_name](#a34edbd459f8acce386a2f953bc6c795f) (const char \*backend\_name) |
|  | Get backend by name. |

## Function Documentation

## [◆ ](#afcf533acf3e0540c6798e58d4c1f7528)shell\_backend\_count\_get()

| | int shell\_backend\_count\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get number of backends.

Returns
:   Number of backends.

## [◆ ](#ad299b24f7d116d733c3f9ccc839fdb2b)shell\_backend\_get()

| | const struct [shell](structshell.md) \* shell\_backend\_get | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *idx* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get backend.

Parameters
:   | [in] | idx | Pointer to the backend instance. |
    | --- | --- | --- |

Returns
:   Pointer to the backend instance.

## [◆ ](#a34edbd459f8acce386a2f953bc6c795f)shell\_backend\_get\_by\_name()

| const struct [shell](structshell.md) \* shell\_backend\_get\_by\_name | ( | const char \* | *backend\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get backend by name.

Parameters
:   | [in] | backend\_name | Name of the backend as defined by the SHELL\_DEFINE. |
    | --- | --- | --- |

Return values
:   | Pointer | to the backend instance if found, NULL if backend is not found. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_backend.h](shell__backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
