---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__output__dict_8h_source.html
original_path: doxygen/html/log__output__dict_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_output\_dict.h

[Go to the documentation of this file.](log__output__dict_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \* Copyright (c) 2021 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_DICT\_H\_

8#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_DICT\_H\_

9

10#include <[zephyr/logging/log\_output.h](log__output_8h.md)>

11#include <[zephyr/logging/log\_msg.h](log__msg_8h.md)>

12#include <stdarg.h>

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14#include <[zephyr/sys/util.h](sys_2util_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 23](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031)enum [log\_dict\_output\_msg\_type](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031) {

[ 24](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031a812d08168eae9c7ebbe7dfda459b1304) [MSG\_NORMAL](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031a812d08168eae9c7ebbe7dfda459b1304) = 0,

[ 25](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031ab620d227e5d1704bf479bee5e650e1cd) [MSG\_DROPPED\_MSG](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031ab620d227e5d1704bf479bee5e650e1cd) = 1,

26};

27

[ 31](structlog__dict__output__normal__msg__hdr__t.md)struct [log\_dict\_output\_normal\_msg\_hdr\_t](structlog__dict__output__normal__msg__hdr__t.md) {

[ 32](structlog__dict__output__normal__msg__hdr__t.md#a5c2916995965e12d5504d5f9ae3ea04f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structlog__dict__output__normal__msg__hdr__t.md#a5c2916995965e12d5504d5f9ae3ea04f);

[ 33](structlog__dict__output__normal__msg__hdr__t.md#ac70bc70b6c59d6905b86ddb94f0f8f11) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [domain](structlog__dict__output__normal__msg__hdr__t.md#ac70bc70b6c59d6905b86ddb94f0f8f11):4;

[ 34](structlog__dict__output__normal__msg__hdr__t.md#a41b40465b8d86d25cfdf61fd8067c60f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [level](structlog__dict__output__normal__msg__hdr__t.md#a41b40465b8d86d25cfdf61fd8067c60f):4;

[ 35](structlog__dict__output__normal__msg__hdr__t.md#a207adee5780cc0c33adc4a3e9b28d2ed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [package\_len](structlog__dict__output__normal__msg__hdr__t.md#a207adee5780cc0c33adc4a3e9b28d2ed):16;

[ 36](structlog__dict__output__normal__msg__hdr__t.md#a7fb4f8934358565646f35c20238a1289) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data\_len](structlog__dict__output__normal__msg__hdr__t.md#a7fb4f8934358565646f35c20238a1289):16;

[ 37](structlog__dict__output__normal__msg__hdr__t.md#a6570a840284fee5b84dacc746ce838fc) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [source](structlog__dict__output__normal__msg__hdr__t.md#a6570a840284fee5b84dacc746ce838fc);

[ 38](structlog__dict__output__normal__msg__hdr__t.md#adb10537b51af8632dd9d9e18e18f15e4) [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) [timestamp](structlog__dict__output__normal__msg__hdr__t.md#adb10537b51af8632dd9d9e18e18f15e4);

39} \_\_packed;

40

[ 45](structlog__dict__output__dropped__msg__t.md)struct [log\_dict\_output\_dropped\_msg\_t](structlog__dict__output__dropped__msg__t.md) {

[ 46](structlog__dict__output__dropped__msg__t.md#a253ff870422b308bb1454ea55251d1f1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structlog__dict__output__dropped__msg__t.md#a253ff870422b308bb1454ea55251d1f1);

[ 47](structlog__dict__output__dropped__msg__t.md#a893e9d78bde12f6130a55962bb78c0b1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [num\_dropped\_messages](structlog__dict__output__dropped__msg__t.md#a893e9d78bde12f6130a55962bb78c0b1);

48} \_\_packed;

49

[ 59](log__output__dict_8h.md#a725370821b41f40022856e8d1bb29693)void [log\_dict\_output\_msg\_process](log__output__dict_8h.md#a725370821b41f40022856e8d1bb29693)(const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md),

60 struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

61

[ 69](log__output__dict_8h.md#a52364c7c9f15b9b69c5c83010758faa2)void [log\_dict\_output\_dropped\_process](log__output__dict_8h.md#a52364c7c9f15b9b69c5c83010758faa2)(const struct [log\_output](structlog__output.md) \*output, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt);

70

71#ifdef \_\_cplusplus

72}

73#endif

74

75#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_DICT\_H\_ \*/

[log\_msg.h](log__msg_8h.md)

[log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)

uint32\_t log\_timestamp\_t

**Definition** log\_msg.h:36

[log\_output.h](log__output_8h.md)

[log\_dict\_output\_dropped\_process](log__output__dict_8h.md#a52364c7c9f15b9b69c5c83010758faa2)

void log\_dict\_output\_dropped\_process(const struct log\_output \*output, uint32\_t cnt)

Process dropped messages indication for dictionary-based logging.

[log\_dict\_output\_msg\_process](log__output__dict_8h.md#a725370821b41f40022856e8d1bb29693)

void log\_dict\_output\_msg\_process(const struct log\_output \*log\_output, struct log\_msg \*msg, uint32\_t flags)

Process log messages v2 for dictionary-based logging.

[log\_dict\_output\_msg\_type](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031)

log\_dict\_output\_msg\_type

Log message type.

**Definition** log\_output\_dict.h:23

[MSG\_NORMAL](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031a812d08168eae9c7ebbe7dfda459b1304)

@ MSG\_NORMAL

**Definition** log\_output\_dict.h:24

[MSG\_DROPPED\_MSG](log__output__dict_8h.md#a754616ab4233be81726614f64d5d4031ab620d227e5d1704bf479bee5e650e1cd)

@ MSG\_DROPPED\_MSG

**Definition** log\_output\_dict.h:25

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[log\_dict\_output\_dropped\_msg\_t](structlog__dict__output__dropped__msg__t.md)

Output for one dictionary based log message about dropped messages.

**Definition** log\_output\_dict.h:45

[log\_dict\_output\_dropped\_msg\_t::type](structlog__dict__output__dropped__msg__t.md#a253ff870422b308bb1454ea55251d1f1)

uint8\_t type

**Definition** log\_output\_dict.h:46

[log\_dict\_output\_dropped\_msg\_t::num\_dropped\_messages](structlog__dict__output__dropped__msg__t.md#a893e9d78bde12f6130a55962bb78c0b1)

uint16\_t num\_dropped\_messages

**Definition** log\_output\_dict.h:47

[log\_dict\_output\_normal\_msg\_hdr\_t](structlog__dict__output__normal__msg__hdr__t.md)

Output header for one dictionary based log message.

**Definition** log\_output\_dict.h:31

[log\_dict\_output\_normal\_msg\_hdr\_t::package\_len](structlog__dict__output__normal__msg__hdr__t.md#a207adee5780cc0c33adc4a3e9b28d2ed)

uint32\_t package\_len

**Definition** log\_output\_dict.h:35

[log\_dict\_output\_normal\_msg\_hdr\_t::level](structlog__dict__output__normal__msg__hdr__t.md#a41b40465b8d86d25cfdf61fd8067c60f)

uint32\_t level

**Definition** log\_output\_dict.h:34

[log\_dict\_output\_normal\_msg\_hdr\_t::type](structlog__dict__output__normal__msg__hdr__t.md#a5c2916995965e12d5504d5f9ae3ea04f)

uint8\_t type

**Definition** log\_output\_dict.h:32

[log\_dict\_output\_normal\_msg\_hdr\_t::source](structlog__dict__output__normal__msg__hdr__t.md#a6570a840284fee5b84dacc746ce838fc)

uintptr\_t source

**Definition** log\_output\_dict.h:37

[log\_dict\_output\_normal\_msg\_hdr\_t::data\_len](structlog__dict__output__normal__msg__hdr__t.md#a7fb4f8934358565646f35c20238a1289)

uint32\_t data\_len

**Definition** log\_output\_dict.h:36

[log\_dict\_output\_normal\_msg\_hdr\_t::domain](structlog__dict__output__normal__msg__hdr__t.md#ac70bc70b6c59d6905b86ddb94f0f8f11)

uint32\_t domain

**Definition** log\_output\_dict.h:33

[log\_dict\_output\_normal\_msg\_hdr\_t::timestamp](structlog__dict__output__normal__msg__hdr__t.md#adb10537b51af8632dd9d9e18e18f15e4)

log\_timestamp\_t timestamp

**Definition** log\_output\_dict.h:38

[log\_msg](structlog__msg.md)

**Definition** log\_msg.h:94

[log\_output](structlog__output.md)

Log\_output instance structure.

**Definition** log\_output.h:96

[util.h](sys_2util_8h.md)

Misc utilities.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_output\_dict.h](log__output__dict_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
