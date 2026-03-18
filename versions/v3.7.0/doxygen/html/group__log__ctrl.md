---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__log__ctrl.html
original_path: doxygen/html/group__log__ctrl.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Logger control API

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md)

Logger control API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [LOG\_CORE\_INIT](#gabb1d00fe08bc48ed4d352ce61b0e0582)() |
| #define | [LOG\_INIT](#ga062ce2496c8e47adec91c0d11744a7a7)() |
| #define | [LOG\_PANIC](#ga9ee5a99e0487e3f1e6d289b12c19ad5a)() |
| #define | [LOG\_PROCESS](#gacd14d69929496cea19c699509eb5ea1b)() |

| Typedefs | |
| --- | --- |
| typedef [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)(\* | [log\_timestamp\_get\_t](#gae7aaa810aabda4aed6226a85f28d6fbb)) (void) |

| Functions | |
| --- | --- |
| void | [log\_core\_init](#ga338338de3c3e3ce6d3ea7ca6a6fa83e0) (void) |
|  | Function system initialization of the logger. |
| void | [log\_init](#ga2508fad025e49f9746b6c178dce6917e) (void) |
|  | Function for user initialization of the logger. |
| void | [log\_thread\_trigger](#ga173eff0a07bbd1fc2978a1a705cae1fb) (void) |
|  | Trigger the log processing thread to process logs immediately. |
| void | [log\_thread\_set](#ga5f58516c3c155dde0f44ea9cc7cd8b37) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) process\_tid) |
|  | Function for providing thread which is processing logs. |
| int | [log\_set\_timestamp\_func](#gaea92150610f900ab1258cbce65662ae6) ([log\_timestamp\_get\_t](#gae7aaa810aabda4aed6226a85f28d6fbb) timestamp\_getter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq) |
|  | Function for providing timestamp function. |
| void | [log\_panic](#ga6a4d408fc9d7c55366cd7a02850b03f5) (void) |
|  | Switch the logger subsystem to the panic mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_process](#ga7276787473a372eac8b77c012ae7226a) (void) |
|  | Process one pending log message. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_buffered\_cnt](#gab6785b1f77080bbaf9f5ac3bfe0fd23c) (void) |
|  | Return number of buffered log messages. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_src\_cnt\_get](#ga10b12f5c462f3d0f1cb8d60ead802c9a) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id) |
|  | Get number of independent logger sources (modules and instances). |
| const char \* | [log\_source\_name\_get](#ga7047a91d157b329362cff22784472c83) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) source\_id) |
|  | Get name of the source (module or instance). |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_domains\_count](#ga3fdf07aecb4f559f5119f16c137daf3d) (void) |
|  | Return number of domains present in the system. |
| const char \* | [log\_domain\_name\_get](#gac20a57745d0a10e6cf100eb47eb9561d) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id) |
|  | Get name of the domain. |
| int | [log\_source\_id\_get](#ga0ae80c298349cc784b890809919ad629) (const char \*name) |
|  | Function for finding source ID based on source name. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_filter\_get](#ga83b8fe6d2592f02fe8a73faed819c3ce) (struct [log\_backend](structlog__backend.md) const \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) runtime) |
|  | Get source filter for the provided backend. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_filter\_set](#ga32956e4ba4ed92e5e5aeb5503be0047e) (struct [log\_backend](structlog__backend.md) const \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level) |
|  | Set filter on given source for the provided backend. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_frontend\_filter\_get](#ga826f2176d0ece92617725960db697849) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) runtime) |
|  | Get source filter for the frontend. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_frontend\_filter\_set](#ga305700387e40548dee873ef197228f9b) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level) |
|  | Set filter on given source for the frontend. |
| void | [log\_backend\_enable](#gadbd0b5dd8c459c6ef85f9fef4f2bdebf) (struct [log\_backend](structlog__backend.md) const \*const backend, void \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level) |
|  | Enable backend with initial maximum filtering level. |
| void | [log\_backend\_disable](#gaf5d428f18b00138fd2ccca190981191d) (struct [log\_backend](structlog__backend.md) const \*const backend) |
|  | Disable backend. |
| const struct [log\_backend](structlog__backend.md) \* | [log\_backend\_get\_by\_name](#ga8c374e83492b221eeaf2c2b0f38e3b42) (const char \*backend\_name) |
|  | Get backend by name. |
| const struct [log\_backend](structlog__backend.md) \* | [log\_format\_set\_all\_active\_backends](#gaeaaaa2e68877837a4af20fa172fc2f06) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) log\_type) |
|  | Sets logging format for all active backends. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_data\_pending](#ga6d6c48ddd4b6739e34fde2098ad61731) (void) |
|  | Check if there is pending data to be processed by the logging subsystem. |
| int | [log\_set\_tag](#ga58499087f61cc377615311498eedf1ae) (const char \*tag) |
|  | Configure tag used to prefix each message. |
| int | [log\_mem\_get\_usage](#ga5f3487ab08e421ae7ce8a8b80310a338) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*usage) |
|  | Get current memory usage. |
| int | [log\_mem\_get\_max\_usage](#ga2d3f29bf2783e70242c8608a20a934ee) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max) |
|  | Get maximum memory usage. |

## Detailed Description

Logger control API.

Since
:   1.13

## Macro Definition Documentation

## [◆ ](#gabb1d00fe08bc48ed4d352ce61b0e0582)LOG\_CORE\_INIT

| #define LOG\_CORE\_INIT | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

**Value:**

do { } while (false)

## [◆ ](#ga062ce2496c8e47adec91c0d11744a7a7)LOG\_INIT

| #define LOG\_INIT | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

**Value:**

0

## [◆ ](#ga9ee5a99e0487e3f1e6d289b12c19ad5a)LOG\_PANIC

| #define LOG\_PANIC | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

**Value:**

/\* Empty \*/

## [◆ ](#gacd14d69929496cea19c699509eb5ea1b)LOG\_PROCESS

| #define LOG\_PROCESS | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

**Value:**

false

## Typedef Documentation

## [◆ ](#gae7aaa810aabda4aed6226a85f28d6fbb)log\_timestamp\_get\_t

| typedef [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)(\* log\_timestamp\_get\_t) (void) |
| --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

## Function Documentation

## [◆ ](#gaf5d428f18b00138fd2ccca190981191d)log\_backend\_disable()

| void log\_backend\_disable | ( | struct [log\_backend](structlog__backend.md) const \*const | *backend* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Disable backend.

Parameters
:   | backend | Backend instance. |
    | --- | --- |

## [◆ ](#gadbd0b5dd8c459c6ef85f9fef4f2bdebf)log\_backend\_enable()

| void log\_backend\_enable | ( | struct [log\_backend](structlog__backend.md) const \*const | *backend*, |
| --- | --- | --- | --- |
|  |  | void \* | *ctx*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *level* ) |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Enable backend with initial maximum filtering level.

Parameters
:   | backend | Backend instance. |
    | --- | --- |
    | ctx | User context. |
    | level | Severity level. |

## [◆ ](#ga8c374e83492b221eeaf2c2b0f38e3b42)log\_backend\_get\_by\_name()

| const struct [log\_backend](structlog__backend.md) \* log\_backend\_get\_by\_name | ( | const char \* | *backend\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Get backend by name.

Parameters
:   | [in] | backend\_name | Name of the backend as defined by the LOG\_BACKEND\_DEFINE. |
    | --- | --- | --- |

Return values
:   | Pointer | to the backend instance if found, NULL if backend is not found. |
    | --- | --- |

## [◆ ](#gab6785b1f77080bbaf9f5ac3bfe0fd23c)log\_buffered\_cnt()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_buffered\_cnt | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Return number of buffered log messages.

Returns
:   Number of currently buffered log messages.

## [◆ ](#ga338338de3c3e3ce6d3ea7ca6a6fa83e0)log\_core\_init()

| void log\_core\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Function system initialization of the logger.

Function is called during start up to allow logging before user can explicitly initialize the logger.

## [◆ ](#ga6d6c48ddd4b6739e34fde2098ad61731)log\_data\_pending()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_data\_pending | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Check if there is pending data to be processed by the logging subsystem.

Function can be used to determine if all logs have been flushed. Function returns false when deferred mode is not enabled.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | There is pending data. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | No pending data to process. |

## [◆ ](#gac20a57745d0a10e6cf100eb47eb9561d)log\_domain\_name\_get()

| const char \* log\_domain\_name\_get | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Get name of the domain.

Parameters
:   | domain\_id | Domain ID. |
    | --- | --- |

Returns
:   Domain name.

## [◆ ](#ga3fdf07aecb4f559f5119f16c137daf3d)log\_domains\_count()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_domains\_count | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Return number of domains present in the system.

There will be at least one local domain.

Returns
:   Number of domains.

## [◆ ](#ga83b8fe6d2592f02fe8a73faed819c3ce)log\_filter\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_filter\_get | ( | struct [log\_backend](structlog__backend.md) const \*const | *backend*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *source\_id*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *runtime* ) |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Get source filter for the provided backend.

Parameters
:   | backend | Backend instance. |
    | --- | --- |
    | domain\_id | ID of the domain. |
    | source\_id | Source (module or instance) ID. |
    | runtime | True for runtime filter or false for compiled in. |

Returns
:   Severity level.

## [◆ ](#ga32956e4ba4ed92e5e5aeb5503be0047e)log\_filter\_set()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_filter\_set | ( | struct [log\_backend](structlog__backend.md) const \*const | *backend*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id*, |
|  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *source\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *level* ) |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Set filter on given source for the provided backend.

Parameters
:   | backend | Backend instance. NULL for all backends (and frontend). |
    | --- | --- |
    | domain\_id | ID of the domain. |
    | source\_id | Source (module or instance) ID. |
    | level | Severity level. |

Returns
:   Actual level set which may be limited by compiled level. If filter was set for all backends then maximal level that was set is returned.

## [◆ ](#gaeaaaa2e68877837a4af20fa172fc2f06)log\_format\_set\_all\_active\_backends()

| const struct [log\_backend](structlog__backend.md) \* log\_format\_set\_all\_active\_backends | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *log\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Sets logging format for all active backends.

Parameters
:   | log\_type | Log format. |
    | --- | --- |

Return values
:   | Pointer | to the last backend that failed, NULL for success. |
    | --- | --- |

## [◆ ](#ga826f2176d0ece92617725960db697849)log\_frontend\_filter\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_filter\_get | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *source\_id*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *runtime* ) |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Get source filter for the frontend.

Parameters
:   | source\_id | Source (module or instance) ID. |
    | --- | --- |
    | runtime | True for runtime filter or false for compiled in. |

Returns
:   Severity level.

## [◆ ](#ga305700387e40548dee873ef197228f9b)log\_frontend\_filter\_set()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_filter\_set | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *source\_id*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *level* ) |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Set filter on given source for the frontend.

Parameters
:   | source\_id | Source (module or instance) ID. |
    | --- | --- |
    | level | Severity level. |

Returns
:   Actual level set which may be limited by compiled level.

## [◆ ](#ga2508fad025e49f9746b6c178dce6917e)log\_init()

| void log\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Function for user initialization of the logger.

## [◆ ](#ga2d3f29bf2783e70242c8608a20a934ee)log\_mem\_get\_max\_usage()

| int log\_mem\_get\_max\_usage | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *max* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Get maximum memory usage.

Requires CONFIG\_LOG\_MEM\_UTILIZATION option.

Parameters
:   | [out] | max | Maximum number of bytes used for pending log messages. |
    | --- | --- | --- |

Return values
:   | -EINVAL | if logging mode does not use the buffer. |
    | --- | --- |
    | -ENOTSUP | if instrumentation is not enabled. not been enabled. |
    | 0 | successfully collected usage data. |

## [◆ ](#ga5f3487ab08e421ae7ce8a8b80310a338)log\_mem\_get\_usage()

| int log\_mem\_get\_usage | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *buf\_size*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *usage* ) |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Get current memory usage.

Parameters
:   | [out] | buf\_size | Capacity of the buffer used for storing log messages. |
    | --- | --- | --- |
    | [out] | usage | Number of bytes currently containing pending log messages. |

Return values
:   | -EINVAL | if logging mode does not use the buffer. |
    | --- | --- |
    | 0 | successfully collected usage data. |

## [◆ ](#ga6a4d408fc9d7c55366cd7a02850b03f5)log\_panic()

| void log\_panic | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Switch the logger subsystem to the panic mode.

Returns immediately if the logger is already in the panic mode.

On panic the logger subsystem informs all backends about panic mode. Backends must switch to blocking mode or halt. All pending logs are flushed after switching to panic mode. In panic mode, all log messages must be processed in the context of the call.

## [◆ ](#ga7276787473a372eac8b77c012ae7226a)log\_process()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_process | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Process one pending log message.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | There are more messages pending to be processed. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | No messages pending. |

## [◆ ](#ga58499087f61cc377615311498eedf1ae)log\_set\_tag()

| int log\_set\_tag | ( | const char \* | *tag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Configure tag used to prefix each message.

Parameters
:   | tag | Tag. |
    | --- | --- |

Return values
:   | 0 | on successful operation. |
    | --- | --- |
    | -ENOTSUP | if feature is disabled. |
    | -ENOMEM | if string is longer than the buffer capacity. Tag will be trimmed. |

## [◆ ](#gaea92150610f900ab1258cbce65662ae6)log\_set\_timestamp\_func()

| int log\_set\_timestamp\_func | ( | [log\_timestamp\_get\_t](#gae7aaa810aabda4aed6226a85f28d6fbb) | *timestamp\_getter*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *freq* ) |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Function for providing timestamp function.

Parameters
:   | timestamp\_getter | Timestamp function. |
    | --- | --- |
    | freq | Timestamping frequency. |

Returns
:   0 on success or error.

## [◆ ](#ga0ae80c298349cc784b890809919ad629)log\_source\_id\_get()

| int log\_source\_id\_get | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Function for finding source ID based on source name.

Parameters
:   | name | Source name |
    | --- | --- |

Returns
:   Source ID or negative number when source ID is not found.

## [◆ ](#ga7047a91d157b329362cff22784472c83)log\_source\_name\_get()

| const char \* log\_source\_name\_get | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *source\_id* ) |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Get name of the source (module or instance).

Parameters
:   | domain\_id | Domain ID. |
    | --- | --- |
    | source\_id | Source ID. |

Returns
:   Source name or NULL if invalid arguments.

## [◆ ](#ga10b12f5c462f3d0f1cb8d60ead802c9a)log\_src\_cnt\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_src\_cnt\_get | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Get number of independent logger sources (modules and instances).

Parameters
:   | domain\_id | Domain ID. |
    | --- | --- |

Returns
:   Number of sources.

## [◆ ](#ga5f58516c3c155dde0f44ea9cc7cd8b37)log\_thread\_set()

| void log\_thread\_set | ( | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *process\_tid* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Function for providing thread which is processing logs.

See CONFIG\_LOG\_PROCESS\_TRIGGER\_THRESHOLD.

Note
:   Function has asserts and has no effect when CONFIG\_LOG\_PROCESS\_THREAD is set.

Parameters
:   | process\_tid | Process thread id. Used to wake up the thread. |
    | --- | --- |

## [◆ ](#ga173eff0a07bbd1fc2978a1a705cae1fb)log\_thread\_trigger()

| void log\_thread\_trigger | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_ctrl.h](log__ctrl_8h.md)>`

Trigger the log processing thread to process logs immediately.

Note
:   Function has no effect when CONFIG\_LOG\_MODE\_IMMEDIATE is set.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
