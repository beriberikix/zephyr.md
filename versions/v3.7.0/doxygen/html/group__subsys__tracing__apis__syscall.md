---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__syscall.html
original_path: doxygen/html/group__subsys__tracing__apis__syscall.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Syscall Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Syscall Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_syscall\_enter](#ga5526336abc0394bd8d8c7541473ad4ef)(id, name, ...) |
|  | Trace syscall entry. |
| #define | [sys\_port\_trace\_syscall\_exit](#gaed9dc749bc6da68e4df2ba9cd098f863)(id, name, ...) |
|  | Trace syscall exit. |

## Detailed Description

Syscall Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga5526336abc0394bd8d8c7541473ad4ef)sys\_port\_trace\_syscall\_enter

| #define sys\_port\_trace\_syscall\_enter | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | ... ) |

`#include <[tracing_syscall.h](tracing__syscall_8h.md)>`

Trace syscall entry.

Parameters
:   | id | Syscall ID (as defined in the generated syscall\_list.h) |
    | --- | --- |
    | name | Syscall name as a token (ex: k\_thread\_create) |
    | ... | Other parameters passed to the syscall |

## [◆ ](#gaed9dc749bc6da68e4df2ba9cd098f863)sys\_port\_trace\_syscall\_exit

| #define sys\_port\_trace\_syscall\_exit | ( |  | *id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | ... ) |

`#include <[tracing_syscall.h](tracing__syscall_8h.md)>`

Trace syscall exit.

Parameters
:   | id | Syscall ID (as defined in the generated syscall\_list.h) |
    | --- | --- |
    | name | Syscall name as a token (ex: k\_thread\_create) |
    | ... | Other parameters passed to the syscall, if the syscall has a return, the return value is the last parameter in the list |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
