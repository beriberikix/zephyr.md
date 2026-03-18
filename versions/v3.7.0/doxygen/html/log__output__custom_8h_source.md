---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/log__output__custom_8h_source.html
original_path: doxygen/html/log__output__custom_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_output\_custom.h

[Go to the documentation of this file.](log__output__custom_8h.md)

1/\*

2 \* Copyright (c) 2021 Converge

3 \* Copyright (c) 2023 Nobleo Technology

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_CUSTOM\_H\_

8#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_CUSTOM\_H\_

9

10#include <[zephyr/logging/log\_output.h](log__output_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

20

[ 31](group__log__output.md#gadcbd0a6378ddefce1a70f7ee9ae8c47a)void [log\_custom\_output\_msg\_process](group__log__output.md#gadcbd0a6378ddefce1a70f7ee9ae8c47a)(const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md),

32 struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

33

[ 38](log__output__custom_8h.md#a2b9b68702c90af6caa8da74d3674607c)void [log\_custom\_output\_msg\_set](log__output__custom_8h.md#a2b9b68702c90af6caa8da74d3674607c)([log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737) format);

39

40

[ 55](log__output__custom_8h.md#a40a92ad6ae0991cbb0f0af45681ae35e)typedef int (\*[log\_timestamp\_printer\_t](log__output__custom_8h.md#a40a92ad6ae0991cbb0f0af45681ae35e))(const struct [log\_output](structlog__output.md) \*output, const char \*fmt, ...);

56

[ 74](log__output__custom_8h.md#a92eda6f74e14725a875eaece6169987a)typedef int (\*[log\_timestamp\_format\_func\_t](log__output__custom_8h.md#a92eda6f74e14725a875eaece6169987a))(const struct [log\_output](structlog__output.md) \*output,

75 const [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp,

76 const [log\_timestamp\_printer\_t](log__output__custom_8h.md#a40a92ad6ae0991cbb0f0af45681ae35e) printer);

77

[ 87](log__output__custom_8h.md#a2b09917a2f801d90109b46afaa445d22)int [log\_custom\_timestamp\_print](log__output__custom_8h.md#a2b09917a2f801d90109b46afaa445d22)(const struct [log\_output](structlog__output.md) \*output, const [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp,

88 const [log\_timestamp\_printer\_t](log__output__custom_8h.md#a40a92ad6ae0991cbb0f0af45681ae35e) printer);

89

[ 95](log__output__custom_8h.md#acc5df49202b3fa5dc1070cf81ae75539)void [log\_custom\_timestamp\_set](log__output__custom_8h.md#acc5df49202b3fa5dc1070cf81ae75539)([log\_timestamp\_format\_func\_t](log__output__custom_8h.md#a92eda6f74e14725a875eaece6169987a) format);

96

100

101#ifdef \_\_cplusplus

102}

103#endif

104

105#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_CUSTOM\_H\_ \*/

[log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737)

void(\* log\_format\_func\_t)(const struct log\_output \*output, struct log\_msg \*msg, uint32\_t flags)

Typedef of the function pointer table "format\_table".

**Definition** log\_output.h:112

[log\_custom\_output\_msg\_process](group__log__output.md#gadcbd0a6378ddefce1a70f7ee9ae8c47a)

void log\_custom\_output\_msg\_process(const struct log\_output \*log\_output, struct log\_msg \*msg, uint32\_t flags)

Custom logging output formatting.

[log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)

uint32\_t log\_timestamp\_t

**Definition** log\_msg.h:36

[log\_output.h](log__output_8h.md)

[log\_custom\_timestamp\_print](log__output__custom_8h.md#a2b09917a2f801d90109b46afaa445d22)

int log\_custom\_timestamp\_print(const struct log\_output \*output, const log\_timestamp\_t timestamp, const log\_timestamp\_printer\_t printer)

Format the timestamp with a external function.

[log\_custom\_output\_msg\_set](log__output__custom_8h.md#a2b9b68702c90af6caa8da74d3674607c)

void log\_custom\_output\_msg\_set(log\_format\_func\_t format)

Set the formatting log function that will be applied with LOG\_OUTPUT\_CUSTOM.

[log\_timestamp\_printer\_t](log__output__custom_8h.md#a40a92ad6ae0991cbb0f0af45681ae35e)

int(\* log\_timestamp\_printer\_t)(const struct log\_output \*output, const char \*fmt,...)

Prototype of a printer function that can print the given timestamp into a specific logger instance.

**Definition** log\_output\_custom.h:55

[log\_timestamp\_format\_func\_t](log__output__custom_8h.md#a92eda6f74e14725a875eaece6169987a)

int(\* log\_timestamp\_format\_func\_t)(const struct log\_output \*output, const log\_timestamp\_t timestamp, const log\_timestamp\_printer\_t printer)

Prototype of the function that will apply custom formatting to a timestamp when LOG\_OUTPUT\_FORMAT\_CUS...

**Definition** log\_output\_custom.h:74

[log\_custom\_timestamp\_set](log__output__custom_8h.md#acc5df49202b3fa5dc1070cf81ae75539)

void log\_custom\_timestamp\_set(log\_timestamp\_format\_func\_t format)

Set the timestamp formatting function that will be applied when LOG\_OUTPUT\_FORMAT\_CUSTOM\_TIMESTAMP.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[log\_msg](structlog__msg.md)

**Definition** log\_msg.h:94

[log\_output](structlog__output.md)

Log\_output instance structure.

**Definition** log\_output.h:96

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_output\_custom.h](log__output__custom_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
