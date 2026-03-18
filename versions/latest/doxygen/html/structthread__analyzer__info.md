---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structthread__analyzer__info.html
original_path: doxygen/html/structthread__analyzer__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_analyzer\_info Struct Reference

[Operating System Services](group__os__services.md) » [Thread analyzer](group__thread__analyzer.md)

`#include <[thread_analyzer.h](thread__analyzer_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#a972c2f720864788fa657be15c04c9424) |
|  | The name of the thread or stringified address of the thread handle if name is not set. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [stack\_size](#ad4b6eb4a085f1c250314a452f4005e2e) |
|  | The total size of the stack. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [stack\_used](#ac24b93b5fe53d0d1928eb904af6f2a36) |
|  | Stack size in used. |

## Field Documentation

## [◆ ](#a972c2f720864788fa657be15c04c9424)name

| const char\* thread\_analyzer\_info::name |
| --- |

The name of the thread or stringified address of the thread handle if name is not set.

## [◆ ](#ad4b6eb4a085f1c250314a452f4005e2e)stack\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) thread\_analyzer\_info::stack\_size |
| --- |

The total size of the stack.

## [◆ ](#ac24b93b5fe53d0d1928eb904af6f2a36)stack\_used

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) thread\_analyzer\_info::stack\_used |
| --- |

Stack size in used.

---

The documentation for this struct was generated from the following file:

- zephyr/debug/[thread\_analyzer.h](thread__analyzer_8h_source.md)

- [thread\_analyzer\_info](structthread__analyzer__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
