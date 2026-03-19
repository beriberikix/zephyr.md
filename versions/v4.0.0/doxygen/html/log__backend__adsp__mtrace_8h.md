---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__backend__adsp__mtrace_8h.html
original_path: doxygen/html/log__backend__adsp__mtrace_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_adsp\_mtrace.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`

[Go to the source code of this file.](log__backend__adsp__mtrace_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [adsp\_mtrace\_log\_hook\_t](#ab6362dba4defcd461d24a155763b465d)) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) written, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) space\_left) |
|  | mtracelogger requires a hook for IPC messages |

| Functions | |
| --- | --- |
| void | [adsp\_mtrace\_log\_init](#a9bb9152344270b8257182471443caa78) ([adsp\_mtrace\_log\_hook\_t](#ab6362dba4defcd461d24a155763b465d) hook) |
|  | Initialize the Intel ADSP mtrace logger. |
| const struct [log\_backend](structlog__backend.md) \* | [log\_backend\_adsp\_mtrace\_get](#aecd49115065234a120c75f450b799269) (void) |

## Typedef Documentation

## [◆ ](#ab6362dba4defcd461d24a155763b465d)adsp\_mtrace\_log\_hook\_t

| typedef void(\* adsp\_mtrace\_log\_hook\_t) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) written, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) space\_left) |
| --- |

mtracelogger requires a hook for IPC messages

When new log data is added to the SRAM buffer, a IPC message should be sent to the host. This hook function pointer allows for that.

## Function Documentation

## [◆ ](#a9bb9152344270b8257182471443caa78)adsp\_mtrace\_log\_init()

| void adsp\_mtrace\_log\_init | ( | [adsp\_mtrace\_log\_hook\_t](#ab6362dba4defcd461d24a155763b465d) | *hook* | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize the Intel ADSP mtrace logger.

Parameters
:   | hook | Function is called after each write to the SRAM buffer It is up to the author of the hook to serialize if needed. |
    | --- | --- |

## [◆ ](#aecd49115065234a120c75f450b799269)log\_backend\_adsp\_mtrace\_get()

| const struct [log\_backend](structlog__backend.md) \* log\_backend\_adsp\_mtrace\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_adsp\_mtrace.h](log__backend__adsp__mtrace_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
