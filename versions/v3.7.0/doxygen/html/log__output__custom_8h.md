---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/log__output__custom_8h.html
original_path: doxygen/html/log__output__custom_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_output\_custom.h File Reference

`#include <[zephyr/logging/log_output.h](log__output_8h_source.md)>`

[Go to the source code of this file.](log__output__custom_8h_source.md)

| typedef int(\* | [log\_timestamp\_printer\_t](#a40a92ad6ae0991cbb0f0af45681ae35e)) (const struct [log\_output](structlog__output.md) \*output, const char \*fmt,...) |
| --- | --- |
|  | Prototype of a printer function that can print the given timestamp into a specific logger instance. |
| typedef int(\* | [log\_timestamp\_format\_func\_t](#a92eda6f74e14725a875eaece6169987a)) (const struct [log\_output](structlog__output.md) \*output, const [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp, const [log\_timestamp\_printer\_t](#a40a92ad6ae0991cbb0f0af45681ae35e) printer) |
|  | Prototype of the function that will apply custom formatting to a timestamp when LOG\_OUTPUT\_FORMAT\_CUSTOM\_TIMESTAMP. |
| void | [log\_custom\_output\_msg\_process](group__log__output.md#gadcbd0a6378ddefce1a70f7ee9ae8c47a) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Custom logging output formatting. |
| void | [log\_custom\_output\_msg\_set](#a2b9b68702c90af6caa8da74d3674607c) ([log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737) format) |
|  | Set the formatting log function that will be applied with LOG\_OUTPUT\_CUSTOM. |
| int | [log\_custom\_timestamp\_print](#a2b09917a2f801d90109b46afaa445d22) (const struct [log\_output](structlog__output.md) \*output, const [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp, const [log\_timestamp\_printer\_t](#a40a92ad6ae0991cbb0f0af45681ae35e) printer) |
|  | Format the timestamp with a external function. |
| void | [log\_custom\_timestamp\_set](#acc5df49202b3fa5dc1070cf81ae75539) ([log\_timestamp\_format\_func\_t](#a92eda6f74e14725a875eaece6169987a) format) |
|  | Set the timestamp formatting function that will be applied when LOG\_OUTPUT\_FORMAT\_CUSTOM\_TIMESTAMP. |

## Typedef Documentation

## [◆ ](#a92eda6f74e14725a875eaece6169987a)log\_timestamp\_format\_func\_t

| typedef int(\* log\_timestamp\_format\_func\_t) (const struct [log\_output](structlog__output.md) \*output, const [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp, const [log\_timestamp\_printer\_t](#a40a92ad6ae0991cbb0f0af45681ae35e) printer) |
| --- |

Prototype of the function that will apply custom formatting to a timestamp when LOG\_OUTPUT\_FORMAT\_CUSTOM\_TIMESTAMP.

Example function:

int custom\_timestamp\_formatter(const struct [log\_output](structlog__output.md)\* output,

const [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp,

const [log\_timestamp\_printer\_t](#a40a92ad6ae0991cbb0f0af45681ae35e) printer) {

return printer(output, "%d ", timestamp);

}

[log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)

uint32\_t log\_timestamp\_t

**Definition** log\_msg.h:36

[log\_timestamp\_printer\_t](#a40a92ad6ae0991cbb0f0af45681ae35e)

int(\* log\_timestamp\_printer\_t)(const struct log\_output \*output, const char \*fmt,...)

Prototype of a printer function that can print the given timestamp into a specific logger instance.

**Definition** log\_output\_custom.h:55

[log\_output](structlog__output.md)

Log\_output instance structure.

**Definition** log\_output.h:96

Parameters
:   | output | The logger instance to write to |
    | --- | --- |
    | timestamp |  |
    | printer | The printing function to use when formatting the timestamp. |

## [◆ ](#a40a92ad6ae0991cbb0f0af45681ae35e)log\_timestamp\_printer\_t

| typedef int(\* log\_timestamp\_printer\_t) (const struct [log\_output](structlog__output.md) \*output, const char \*fmt,...) |
| --- |

Prototype of a printer function that can print the given timestamp into a specific logger instance.

Example usage:

[log\_timestamp\_printer\_t](#a40a92ad6ae0991cbb0f0af45681ae35e) \*printer = ...;

printer(log\_instance, "%02u:%02u", hours, minutes);

Parameters
:   | output | The logger instance to write to |
    | --- | --- |
    | fmt | The format string |
    | ... | optional arguments for the format string |

## Function Documentation

## [◆ ](#a2b9b68702c90af6caa8da74d3674607c)log\_custom\_output\_msg\_set()

| void log\_custom\_output\_msg\_set | ( | [log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737) | *format* | ) |  |
| --- | --- | --- | --- | --- | --- |

Set the formatting log function that will be applied with LOG\_OUTPUT\_CUSTOM.

Parameters
:   | format | Pointer to the external formatter function |
    | --- | --- |

## [◆ ](#a2b09917a2f801d90109b46afaa445d22)log\_custom\_timestamp\_print()

| int log\_custom\_timestamp\_print | ( | const struct [log\_output](structlog__output.md) \* | *output*, |
| --- | --- | --- | --- |
|  |  | const [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) | *timestamp*, |
|  |  | const [log\_timestamp\_printer\_t](#a40a92ad6ae0991cbb0f0af45681ae35e) | *printer* ) |

Format the timestamp with a external function.

Function is using provided context with the buffer and output function to process formatted string and output the data.

Parameters
:   | output | Pointer to the log output instance. |
    | --- | --- |
    | timestamp |  |
    | printer | The printing function to use when formatting the timestamp. |

## [◆ ](#acc5df49202b3fa5dc1070cf81ae75539)log\_custom\_timestamp\_set()

| void log\_custom\_timestamp\_set | ( | [log\_timestamp\_format\_func\_t](#a92eda6f74e14725a875eaece6169987a) | *format* | ) |  |
| --- | --- | --- | --- | --- | --- |

Set the timestamp formatting function that will be applied when LOG\_OUTPUT\_FORMAT\_CUSTOM\_TIMESTAMP.

Parameters
:   | format | Pointer to the external formatter function |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_output\_custom.h](log__output__custom_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
