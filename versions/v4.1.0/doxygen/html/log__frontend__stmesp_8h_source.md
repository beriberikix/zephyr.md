---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__frontend__stmesp_8h_source.html
original_path: doxygen/html/log__frontend__stmesp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp.h

[Go to the documentation of this file.](log__frontend__stmesp_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_FRONTEND\_STMESP\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_FRONTEND\_STMESP\_H\_

8

9#include <[errno.h](errno_8h.md)>

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11#ifdef CONFIG\_LOG\_FRONTEND\_STMESP

12#include <[zephyr/drivers/misc/coresight/stmesp.h](stmesp_8h.md)>

13#endif

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 29](log__frontend__stmesp_8h.md#afdfa76ad219bd073b54825ae50cf13d3)int [log\_frontend\_stmesp\_etr\_ready](log__frontend__stmesp_8h.md#afdfa76ad219bd073b54825ae50cf13d3)(void);

30

[ 36](log__frontend__stmesp_8h.md#ae222ceeee8aa370e3aaeb6eb8f1e1a8f)void [log\_frontend\_stmesp\_pre\_sleep](log__frontend__stmesp_8h.md#ae222ceeee8aa370e3aaeb6eb8f1e1a8f)(void);

37

[ 42](log__frontend__stmesp_8h.md#acb1274db685fbd6282868b03d3c627da)void [log\_frontend\_stmesp\_dummy\_write](log__frontend__stmesp_8h.md#acb1274db685fbd6282868b03d3c627da)(void);

43

[ 51](log__frontend__stmesp_8h.md#ab2b829f38108c54490090dcd97719cec)static inline void [log\_frontend\_stmesp\_tp](log__frontend__stmesp_8h.md#ab2b829f38108c54490090dcd97719cec)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x)

52{

53#ifdef CONFIG\_LOG\_FRONTEND\_STMESP

54 STMESP\_Type \*port;

55 int err = [stmesp\_get\_port](group__stmsp__interface.md#ga4350f5d201e3591221a932aa9fc3e94d)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))x + CONFIG\_LOG\_FRONTEND\_STMESP\_TP\_CHAN\_BASE, &port);

56

57 \_\_ASSERT\_NO\_MSG(err == 0);

58 if (err == 0) {

59 [stmesp\_flag](group__stmsp__interface.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)(port, 1, true,

60 [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_FRONTEND\_STMESP\_GUARANTEED\_ACCESS));

61 }

62#endif

63}

64

[ 73](log__frontend__stmesp_8h.md#a68b8bdb65457ffa2c0ab7c97b8414600)static inline void [log\_frontend\_stmesp\_tp\_d32](log__frontend__stmesp_8h.md#a68b8bdb65457ffa2c0ab7c97b8414600)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417))

74{

75#ifdef CONFIG\_LOG\_FRONTEND\_STMESP

76 STMESP\_Type \*port;

77 int err = [stmesp\_get\_port](group__stmsp__interface.md#ga4350f5d201e3591221a932aa9fc3e94d)(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))x + CONFIG\_LOG\_FRONTEND\_STMESP\_TP\_CHAN\_BASE, &port);

78

79 \_\_ASSERT\_NO\_MSG(err == 0);

80 if (err == 0) {

81 [stmesp\_data32](group__stmsp__interface.md#gaa7885c5a7620e46a532dbf405bfc6034)(port, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), true, true,

82 [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_FRONTEND\_STMESP\_GUARANTEED\_ACCESS));

83 }

84#endif

85}

86

[ 92](log__frontend__stmesp_8h.md#af3052fc610038ca8b3c2b9488a98d54a)void [log\_frontend\_stmesp\_log0](log__frontend__stmesp_8h.md#af3052fc610038ca8b3c2b9488a98d54a)(const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x);

93

[ 100](log__frontend__stmesp_8h.md#a7b9ad98fd11cbc6c28cc6b38307d52c6)void [log\_frontend\_stmesp\_log1](log__frontend__stmesp_8h.md#a7b9ad98fd11cbc6c28cc6b38307d52c6)(const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg);

101

[ 102](log__frontend__stmesp_8h.md#a135d13f257ea7bc2a2993d735cede654)[TYPE\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)(const char \*, log\_stmesp\_ptr);

103

[ 109](log__frontend__stmesp_8h.md#ae583dd282c17ad3330955b98206b401a)#define LOG\_FRONTEND\_STMESP\_LOG0(\_source, ...) \

110 do { \

111 static const char \_str[] \_\_in\_section(\_log\_stmesp\_str, static, \_) \

112 \_\_used \_\_noasan \_\_aligned(sizeof(uint32\_t)) = GET\_ARG\_N(1, \_\_VA\_ARGS\_\_); \

113 static const char \*\_str\_ptr \_\_in\_section(\_log\_stmesp\_ptr, static, \_) \

114 \_\_used \_\_noasan = \_str; \

115 uint32\_t idx = \

116 ((uintptr\_t)&\_str\_ptr - (uintptr\_t)TYPE\_SECTION\_START(log\_stmesp\_ptr)) / \

117 sizeof(void \*); \

118 log\_frontend\_stmesp\_log0(\_source, idx); \

119 } while (0)

120

[ 126](log__frontend__stmesp_8h.md#ae82104c26a3426e5c1ab45ba1149204a)#define LOG\_FRONTEND\_STMESP\_LOG1(\_source, ...) \

127 do { \

128 static const char \_str[] \_\_in\_section(\_log\_stmesp\_str, static, \_) \

129 \_\_used \_\_noasan \_\_aligned(sizeof(uint32\_t)) = GET\_ARG\_N(1, \_\_VA\_ARGS\_\_); \

130 static const char \*\_str\_ptr \_\_in\_section(\_log\_stmesp\_ptr, static, \_) \

131 \_\_used \_\_noasan = \_str; \

132 uint32\_t idx = \

133 ((uintptr\_t)&\_str\_ptr - (uintptr\_t)TYPE\_SECTION\_START(log\_stmesp\_ptr)) / \

134 sizeof(void \*); \

135 log\_frontend\_stmesp\_log1(\_source, idx, (uintptr\_t)(GET\_ARG\_N(2, \_\_VA\_ARGS\_\_))); \

136 } while (0)

137

138#ifdef \_\_cplusplus

139}

140#endif

141

142#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_FRONTEND\_STMESP\_H\_ \*/

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[errno.h](errno_8h.md)

System error numbers.

[TYPE\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)

#define TYPE\_SECTION\_START\_EXTERN(type, secname)

iterable section extern for start symbol for a generic type

**Definition** iterable\_sections.h:78

[stmesp\_flag](group__stmsp__interface.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)

static void stmesp\_flag(STMESP\_Type \*reg, uint32\_t data, bool ts, bool guaranteed)

Write flag to STMESP.

**Definition** stmesp.h:99

[stmesp\_get\_port](group__stmsp__interface.md#ga4350f5d201e3591221a932aa9fc3e94d)

static int stmesp\_get\_port(uint32\_t idx, STMESP\_Type \*\*port)

Return address of a STM extended stimulus port.

**Definition** stmesp.h:169

[stmesp\_data32](group__stmsp__interface.md#gaa7885c5a7620e46a532dbf405bfc6034)

static void stmesp\_data32(STMESP\_Type \*reg, uint32\_t data, bool ts, bool marked, bool guaranteed)

Write 32 bit data to STMESP.

**Definition** stmesp.h:152

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

[types.h](include_2zephyr_2types_8h.md)

[log\_frontend\_stmesp\_tp\_d32](log__frontend__stmesp_8h.md#a68b8bdb65457ffa2c0ab7c97b8414600)

static void log\_frontend\_stmesp\_tp\_d32(uint16\_t x, uint32\_t d)

Trace point with 32 bit data.

**Definition** log\_frontend\_stmesp.h:73

[log\_frontend\_stmesp\_log1](log__frontend__stmesp_8h.md#a7b9ad98fd11cbc6c28cc6b38307d52c6)

void log\_frontend\_stmesp\_log1(const void \*source, uint32\_t x, uint32\_t arg)

Function called for log message with one argument when turbo logging is enabled.

[log\_frontend\_stmesp\_tp](log__frontend__stmesp_8h.md#ab2b829f38108c54490090dcd97719cec)

static void log\_frontend\_stmesp\_tp(uint16\_t x)

Trace point.

**Definition** log\_frontend\_stmesp.h:51

[log\_frontend\_stmesp\_dummy\_write](log__frontend__stmesp_8h.md#acb1274db685fbd6282868b03d3c627da)

void log\_frontend\_stmesp\_dummy\_write(void)

Perform a dummy write to STMESP.

[log\_frontend\_stmesp\_pre\_sleep](log__frontend__stmesp_8h.md#ae222ceeee8aa370e3aaeb6eb8f1e1a8f)

void log\_frontend\_stmesp\_pre\_sleep(void)

Hook to be called before going to sleep.

[log\_frontend\_stmesp\_log0](log__frontend__stmesp_8h.md#af3052fc610038ca8b3c2b9488a98d54a)

void log\_frontend\_stmesp\_log0(const void \*source, uint32\_t x)

Function called for log message with no arguments when turbo logging is enabled.

[log\_frontend\_stmesp\_etr\_ready](log__frontend__stmesp_8h.md#afdfa76ad219bd073b54825ae50cf13d3)

int log\_frontend\_stmesp\_etr\_ready(void)

Notify frontend that ETR/STM is ready.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[stmesp.h](stmesp_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_frontend\_stmesp.h](log__frontend__stmesp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
