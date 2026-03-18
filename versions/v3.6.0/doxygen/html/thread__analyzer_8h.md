---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/thread__analyzer_8h.html
original_path: doxygen/html/thread__analyzer_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread\_analyzer.h File Reference

`#include <stddef.h>`  
`#include <[zephyr/kernel/thread.h](kernel_2thread_8h_source.md)>`

[Go to the source code of this file.](thread__analyzer_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [thread\_analyzer\_info](structthread__analyzer__info.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [thread\_analyzer\_cb](group__thread__analyzer.md#ga7ac3e88ca6d905ba0efe4afe5822485c)) (struct [thread\_analyzer\_info](structthread__analyzer__info.md) \*info) |
|  | Thread analyzer stack size callback function. |

| Functions | |
| --- | --- |
| void | [thread\_analyzer\_run](group__thread__analyzer.md#ga21ae4723422fb96bf4f20ddb3cc1bb8d) ([thread\_analyzer\_cb](group__thread__analyzer.md#ga7ac3e88ca6d905ba0efe4afe5822485c) cb) |
|  | Run the thread analyzer and provide information to the callback. |
| void | [thread\_analyzer\_print](group__thread__analyzer.md#ga9ff07e2eff100f4b8c79440483c89836) (void) |
|  | Run the thread analyzer and print stack size statistics. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [thread\_analyzer.h](thread__analyzer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
