---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__frontend_8h.html
original_path: doxygen/html/log__frontend_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend.h File Reference

`#include <[zephyr/logging/log_core.h](log__core_8h_source.md)>`

[Go to the source code of this file.](log__frontend_8h_source.md)

| Functions | |
| --- | --- |
| void | [log\_frontend\_init](#a10b0e6f2dd38be09465b6356586f6745) (void) |
|  | Initialize frontend. |
| void | [log\_frontend\_msg](#a81d90e2daca1f6c16f948c6a725803ba) (const void \*source, const struct [log\_msg\_desc](structlog__msg__desc.md) desc, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*package, const void \*data) |
|  | Log generic message. |
| void | [log\_frontend\_simple\_0](#a19e07719a21e8d2138d8e5932b1e7c68) (const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level, const char \*fmt) |
|  | Log message with 0 arguments. |
| void | [log\_frontend\_simple\_1](#a6a4875ae710dc7e14c93b9225d2496d2) (const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level, const char \*fmt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg) |
|  | Log message with 1 argument. |
| void | [log\_frontend\_simple\_2](#a13ea68c36a760c2da64d164d8b79c1db) (const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level, const char \*fmt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg0, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg1) |
|  | Log message with 2 arguments. |
| void | [log\_frontend\_panic](#a3ef25b9e13a89b566c507fcf14d7fb91) (void) |
|  | Panic state notification. |

## Function Documentation

## [◆ ](#a10b0e6f2dd38be09465b6356586f6745)log\_frontend\_init()

| void log\_frontend\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize frontend.

## [◆ ](#a81d90e2daca1f6c16f948c6a725803ba)log\_frontend\_msg()

| void log\_frontend\_msg | ( | const void \* | *source*, |
| --- | --- | --- | --- |
|  |  | const struct [log\_msg\_desc](structlog__msg__desc.md) | *desc*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *package*, |
|  |  | const void \* | *data* ) |

Log generic message.

Message details does not contain timestamp. Since function is called in the context of log message call, implementation can use its own timestamping scheme.

Parameters
:   | source | Pointer to a structure associated with given source. It points to static structure or dynamic structure if runtime filtering is enabled. [log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5 "log_const_source_id") or [log\_dynamic\_source\_id](log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008 "log_dynamic_source_id") can be used to determine source id. |
    | --- | --- |
    | desc | Message descriptor. |
    | package | Cbprintf package containing logging formatted string. Length s in `desc`. |
    | data | Hexdump data. Length is in `desc`. |

## [◆ ](#a3ef25b9e13a89b566c507fcf14d7fb91)log\_frontend\_panic()

| void log\_frontend\_panic | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Panic state notification.

## [◆ ](#a19e07719a21e8d2138d8e5932b1e7c68)log\_frontend\_simple\_0()

| void log\_frontend\_simple\_0 | ( | const void \* | *source*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *level*, |
|  |  | const char \* | *fmt* ) |

Log message with 0 arguments.

Optimized version for log message which does not have arguments (only string). This API is optional and is used only if optimizing common log messages is enabled.

Parameters
:   | source | Pointer to a structure associated with given source. It points to static structure or dynamic structure if runtime filtering is enabled. [log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5 "log_const_source_id") or [log\_dynamic\_source\_id](log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008 "log_dynamic_source_id") can be used to determine source id. |
    | --- | --- |
    | level | Severity level. |
    | fmt | String. |

## [◆ ](#a6a4875ae710dc7e14c93b9225d2496d2)log\_frontend\_simple\_1()

| void log\_frontend\_simple\_1 | ( | const void \* | *source*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *level*, |
|  |  | const char \* | *fmt*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *arg* ) |

Log message with 1 argument.

Optimized version for log message which has one argument that fits in a 32 bit word. This API is optional and is used only if optimizing common log messages is enabled.

Parameters
:   | source | Pointer to a structure associated with given source. It points to static structure or dynamic structure if runtime filtering is enabled. [log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5 "log_const_source_id") or [log\_dynamic\_source\_id](log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008 "log_dynamic_source_id") can be used to determine source id. |
    | --- | --- |
    | level | Severity level. |
    | fmt | String. |
    | arg | Argument passed to the string. |

## [◆ ](#a13ea68c36a760c2da64d164d8b79c1db)log\_frontend\_simple\_2()

| void log\_frontend\_simple\_2 | ( | const void \* | *source*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *level*, |
|  |  | const char \* | *fmt*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *arg0*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *arg1* ) |

Log message with 2 arguments.

Optimized version for log message which has two arguments that fit in a 32 bit word. This API is optional and is used only if optimizing common log messages is enabled.

Parameters
:   | source | Pointer to a structure associated with given source. It points to static structure or dynamic structure if runtime filtering is enabled. [log\_const\_source\_id](log__core_8h.md#add353f5f883b7edee6428adb7fb7e4d5 "log_const_source_id") or [log\_dynamic\_source\_id](log__core_8h.md#ab2e628ee35c240d79a5e622fa1209008 "log_dynamic_source_id") can be used to determine source id. |
    | --- | --- |
    | level | Severity level. |
    | fmt | String. |
    | arg0 | First argument passed to the string. |
    | arg1 | Second argument passed to the string. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_frontend.h](log__frontend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
