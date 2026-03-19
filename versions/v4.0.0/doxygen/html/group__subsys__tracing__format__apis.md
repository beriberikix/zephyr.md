---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__subsys__tracing__format__apis.html
original_path: doxygen/html/group__subsys__tracing__format__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Tracing format APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md)

Tracing format APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [tracing\_data](structtracing__data.md) |
|  | A structure to represent tracing data format. [More...](structtracing__data.md#details) |

| Macros | |
| --- | --- |
| #define | [TRACING\_STRING](#gac6aa3236d7aeb8c4a3f0c421899f74e6)(fmt, ...) |
|  | Macro to trace a message in string format. |
| #define | [TRACING\_FORMAT\_DATA](#ga5cf7507b0040325a4c04600fcdeb3b21)(x) |
|  | Macro to format data to tracing data format. |
| #define | [TRACING\_DATA](#ga1b9265a15c577024edd687edc368ca82)(...) |
|  | Macro to trace a message in tracing data format. |

| Typedefs | |
| --- | --- |
| typedef struct [tracing\_data](structtracing__data.md) | [tracing\_data\_t](#ga1a947f2e998d283b58a5e056f7edbb24) |
|  | A structure to represent tracing data format. |

| Functions | |
| --- | --- |
| void | [tracing\_format\_string](#gaf372e7223a7be6f938cd6a0263815d44) (const char \*str,...) |
|  | Tracing a message in string format. |
| void | [tracing\_format\_raw\_data](#gadb864c39916bc50bad341964fead14f5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) length) |
|  | Tracing a message in raw data format. |
| void | [tracing\_format\_data](#ga4072def87e770f60de40062617e96256) ([tracing\_data\_t](#ga1a947f2e998d283b58a5e056f7edbb24) \*tracing\_data\_array, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Tracing a message in tracing data format. |

## Detailed Description

Tracing format APIs.

## Macro Definition Documentation

## [◆ ](#ga1b9265a15c577024edd687edc368ca82)TRACING\_DATA

| #define TRACING\_DATA | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing_format.h](tracing__format_8h.md)>`

**Value:**

do { \

struct [tracing\_data](structtracing__data.md) arg[] = {\_\_VA\_ARGS\_\_}; \

\

tracing\_format\_data(arg, sizeof(arg) / \

sizeof(struct [tracing\_data](structtracing__data.md))); \

} while (false)

[tracing\_data](structtracing__data.md)

A structure to represent tracing data format.

**Definition** tracing\_format.h:24

Macro to trace a message in tracing data format.

All the parameters should be struct [tracing\_data](structtracing__data.md "A structure to represent tracing data format.").

## [◆ ](#ga5cf7507b0040325a4c04600fcdeb3b21)TRACING\_FORMAT\_DATA

| #define TRACING\_FORMAT\_DATA | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing_format.h](tracing__format_8h.md)>`

**Value:**

((struct [tracing\_data](structtracing__data.md)){.data = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)&(x), .length = sizeof((x))})

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Macro to format data to tracing data format.

Parameters
:   | x | Data field. |
    | --- | --- |

## [◆ ](#gac6aa3236d7aeb8c4a3f0c421899f74e6)TRACING\_STRING

| #define TRACING\_STRING | ( |  | *fmt*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[tracing_format.h](tracing__format_8h.md)>`

**Value:**

do { \

tracing\_format\_string(fmt, ##\_\_VA\_ARGS\_\_); \

} while (false)

Macro to trace a message in string format.

Parameters
:   | fmt | The format string. |
    | --- | --- |
    | ... | The format arguments. |

## Typedef Documentation

## [◆ ](#ga1a947f2e998d283b58a5e056f7edbb24)tracing\_data\_t

| typedef struct [tracing\_data](structtracing__data.md) [tracing\_data\_t](#ga1a947f2e998d283b58a5e056f7edbb24) |
| --- |

`#include <[tracing_format.h](tracing__format_8h.md)>`

A structure to represent tracing data format.

## Function Documentation

## [◆ ](#ga4072def87e770f60de40062617e96256)tracing\_format\_data()

| void tracing\_format\_data | ( | [tracing\_data\_t](#ga1a947f2e998d283b58a5e056f7edbb24) \* | *tracing\_data\_array*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *count* ) |

`#include <[tracing_format.h](tracing__format_8h.md)>`

Tracing a message in tracing data format.

Parameters
:   | tracing\_data\_array | Tracing\_data format data array to be traced. |
    | --- | --- |
    | count | Tracing\_data array data count. |

## [◆ ](#gadb864c39916bc50bad341964fead14f5)tracing\_format\_raw\_data()

| void tracing\_format\_raw\_data | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *length* ) |

`#include <[tracing_format.h](tracing__format_8h.md)>`

Tracing a message in raw data format.

Parameters
:   | data | Raw data to be traced. |
    | --- | --- |
    | length | Raw data length. |

## [◆ ](#gaf372e7223a7be6f938cd6a0263815d44)tracing\_format\_string()

| void tracing\_format\_string | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  |  | *...* ) |

`#include <[tracing_format.h](tracing__format_8h.md)>`

Tracing a message in string format.

Parameters
:   | str | String to format. |
    | --- | --- |
    | ... | Variable length arguments. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
