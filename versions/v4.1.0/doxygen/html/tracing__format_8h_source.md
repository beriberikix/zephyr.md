---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tracing__format_8h_source.html
original_path: doxygen/html/tracing__format_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracing\_format.h

[Go to the documentation of this file.](tracing__format_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_TRACING\_TRACING\_FORMAT\_H

8#define ZEPHYR\_INCLUDE\_TRACING\_TRACING\_FORMAT\_H

9

10#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

22

[ 24](structtracing__data.md)typedef struct [tracing\_data](structtracing__data.md) {

[ 25](structtracing__data.md#a4aaf5d4b8f7891710878389b6c781a90) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structtracing__data.md#a4aaf5d4b8f7891710878389b6c781a90);

[ 26](structtracing__data.md#aee24ee325da9fc10892a38f61dca4dba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [length](structtracing__data.md#aee24ee325da9fc10892a38f61dca4dba);

[ 27](group__subsys__tracing__format__apis.md#ga1a947f2e998d283b58a5e056f7edbb24)} \_\_packed [tracing\_data\_t](group__subsys__tracing__format__apis.md#ga1a947f2e998d283b58a5e056f7edbb24);

28

[ 35](group__subsys__tracing__format__apis.md#gac6aa3236d7aeb8c4a3f0c421899f74e6)#define TRACING\_STRING(fmt, ...) \

36 do { \

37 tracing\_format\_string(fmt, ##\_\_VA\_ARGS\_\_); \

38 } while (false)

39

[ 45](group__subsys__tracing__format__apis.md#ga5cf7507b0040325a4c04600fcdeb3b21)#define TRACING\_FORMAT\_DATA(x) \

46 ((struct tracing\_data){.data = (uint8\_t \*)&(x), .length = sizeof((x))})

47

[ 53](group__subsys__tracing__format__apis.md#ga1b9265a15c577024edd687edc368ca82)#define TRACING\_DATA(...) \

54 do { \

55 struct tracing\_data arg[] = {\_\_VA\_ARGS\_\_}; \

56 \

57 tracing\_format\_data(arg, sizeof(arg) / \

58 sizeof(struct tracing\_data)); \

59 } while (false)

60

[ 67](group__subsys__tracing__format__apis.md#gaf372e7223a7be6f938cd6a0263815d44)void [tracing\_format\_string](group__subsys__tracing__format__apis.md#gaf372e7223a7be6f938cd6a0263815d44)(const char \*str, ...);

68

[ 75](group__subsys__tracing__format__apis.md#gadb864c39916bc50bad341964fead14f5)void [tracing\_format\_raw\_data](group__subsys__tracing__format__apis.md#gadb864c39916bc50bad341964fead14f5)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) length);

76

[ 83](group__subsys__tracing__format__apis.md#ga4072def87e770f60de40062617e96256)void [tracing\_format\_data](group__subsys__tracing__format__apis.md#ga4072def87e770f60de40062617e96256)([tracing\_data\_t](group__subsys__tracing__format__apis.md#ga1a947f2e998d283b58a5e056f7edbb24) \*tracing\_data\_array, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count);

84 /\* end of subsys\_tracing\_format\_apis \*/

86

87#ifdef \_\_cplusplus

88}

89#endif

90

91#endif /\* ZEPHYR\_INCLUDE\_TRACING\_TRACING\_FORMAT\_H \*/

[tracing\_data\_t](group__subsys__tracing__format__apis.md#ga1a947f2e998d283b58a5e056f7edbb24)

struct tracing\_data tracing\_data\_t

A structure to represent tracing data format.

[tracing\_format\_data](group__subsys__tracing__format__apis.md#ga4072def87e770f60de40062617e96256)

void tracing\_format\_data(tracing\_data\_t \*tracing\_data\_array, uint32\_t count)

Tracing a message in tracing data format.

[tracing\_format\_raw\_data](group__subsys__tracing__format__apis.md#gadb864c39916bc50bad341964fead14f5)

void tracing\_format\_raw\_data(uint8\_t \*data, uint32\_t length)

Tracing a message in raw data format.

[tracing\_format\_string](group__subsys__tracing__format__apis.md#gaf372e7223a7be6f938cd6a0263815d44)

void tracing\_format\_string(const char \*str,...)

Tracing a message in string format.

[common.h](include_2zephyr_2toolchain_2common_8h.md)

Common toolchain abstraction.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[tracing\_data](structtracing__data.md)

A structure to represent tracing data format.

**Definition** tracing\_format.h:24

[tracing\_data::data](structtracing__data.md#a4aaf5d4b8f7891710878389b6c781a90)

uint8\_t \* data

**Definition** tracing\_format.h:25

[tracing\_data::length](structtracing__data.md#aee24ee325da9fc10892a38f61dca4dba)

uint32\_t length

**Definition** tracing\_format.h:26

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracing\_format.h](tracing__format_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
