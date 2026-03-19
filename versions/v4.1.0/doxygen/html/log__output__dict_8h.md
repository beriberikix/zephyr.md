---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__output__dict_8h.html
original_path: doxygen/html/log__output__dict_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_output\_dict.h File Reference

`#include <[zephyr/logging/log_output.h](log__output_8h_source.md)>`  
`#include <[zephyr/logging/log_msg.h](log__msg_8h_source.md)>`  
`#include <stdarg.h>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](log__output__dict_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [log\_dict\_output\_normal\_msg\_hdr\_t](structlog__dict__output__normal__msg__hdr__t.md) |
|  | Output header for one dictionary based log message. [More...](structlog__dict__output__normal__msg__hdr__t.md#details) |
| struct | [log\_dict\_output\_dropped\_msg\_t](structlog__dict__output__dropped__msg__t.md) |
|  | Output for one dictionary based log message about dropped messages. [More...](structlog__dict__output__dropped__msg__t.md#details) |

| Enumerations | |
| --- | --- |
| enum | [log\_dict\_output\_msg\_type](#a754616ab4233be81726614f64d5d4031) { [MSG\_NORMAL](#a754616ab4233be81726614f64d5d4031a812d08168eae9c7ebbe7dfda459b1304) = 0 , [MSG\_DROPPED\_MSG](#a754616ab4233be81726614f64d5d4031ab620d227e5d1704bf479bee5e650e1cd) = 1 } |
|  | Log message type. [More...](#a754616ab4233be81726614f64d5d4031) |

| Functions | |
| --- | --- |
| void | [log\_dict\_output\_msg\_process](#a725370821b41f40022856e8d1bb29693) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Process log messages v2 for dictionary-based logging. |
| void | [log\_dict\_output\_dropped\_process](#a52364c7c9f15b9b69c5c83010758faa2) (const struct [log\_output](structlog__output.md) \*output, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Process dropped messages indication for dictionary-based logging. |

## Enumeration Type Documentation

## [◆ ](#a754616ab4233be81726614f64d5d4031)log\_dict\_output\_msg\_type

| enum [log\_dict\_output\_msg\_type](#a754616ab4233be81726614f64d5d4031) |
| --- |

Log message type.

| Enumerator | |
| --- | --- |
| MSG\_NORMAL |  |
| MSG\_DROPPED\_MSG |  |

## Function Documentation

## [◆ ](#a52364c7c9f15b9b69c5c83010758faa2)log\_dict\_output\_dropped\_process()

| void log\_dict\_output\_dropped\_process | ( | const struct [log\_output](structlog__output.md) \* | *output*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cnt* ) |

Process dropped messages indication for dictionary-based logging.

Function prints error message indicating lost log messages.

Parameters
:   | output | Pointer to the log output instance. |
    | --- | --- |
    | cnt | Number of dropped messages. |

## [◆ ](#a725370821b41f40022856e8d1bb29693)log\_dict\_output\_msg\_process()

| void log\_dict\_output\_msg\_process | ( | const struct [log\_output](structlog__output.md) \* | *log\_output*, |
| --- | --- | --- | --- |
|  |  | struct [log\_msg](structlog__msg.md) \* | *msg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

Process log messages v2 for dictionary-based logging.

Function is using provided context with the buffer and output function to process formatted string and output the data.

Parameters
:   | [log\_output](structlog__output.md "Log_output instance structure.") | Pointer to the log output instance. |
    | --- | --- |
    | msg | Log message. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Optional flags. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_output\_dict.h](log__output__dict_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
