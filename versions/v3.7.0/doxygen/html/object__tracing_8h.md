---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/object__tracing_8h.html
original_path: doxygen/html/object__tracing_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

object\_tracing.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/kernel_structs.h](kernel__structs_8h_source.md)>`

[Go to the source code of this file.](object__tracing_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_THREAD\_MONITOR\_HEAD](#aba3e9abb310c42fef67ce63cb2845046)   ((struct [k\_thread](structk__thread.md) \*)(\_kernel.threads)) |
|  | Head element of the thread monitor list. |
| #define | [SYS\_THREAD\_MONITOR\_NEXT](#aefa138ca1b427f994b994ebe1224764e)(obj) |
|  | Gets a thread node's next element. |

## Macro Definition Documentation

## [◆ ](#aba3e9abb310c42fef67ce63cb2845046)SYS\_THREAD\_MONITOR\_HEAD

| #define SYS\_THREAD\_MONITOR\_HEAD   ((struct [k\_thread](structk__thread.md) \*)(\_kernel.threads)) |
| --- |

Head element of the thread monitor list.

Access the head element of the thread monitor list.

## [◆ ](#aefa138ca1b427f994b994ebe1224764e)SYS\_THREAD\_MONITOR\_NEXT

| #define SYS\_THREAD\_MONITOR\_NEXT | ( |  | *obj* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((struct [k\_thread](structk__thread.md) \*)obj)->next\_thread)

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

Gets a thread node's next element.

Given a node in a thread monitor list, gets the next element in the list.

Parameters
:   | obj | Object to get the next element from. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [object\_tracing.h](object__tracing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
