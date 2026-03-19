---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hash__function_8h_source.html
original_path: doxygen/html/hash__function_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_function.h

[Go to the documentation of this file.](hash__function_8h.md)

1/\*

2 \* Copyright (c) 2022 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_HASH\_FUNCTION\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_HASH\_FUNCTION\_H\_

9

10#include <stddef.h>

11#include <[stdint.h](stdint_8h.md)>

12

13#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

14#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

25

[ 41](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad))(const void \*str, size\_t n);

42

[ 58](group__hash__functions.md#ga3bc327796b6836648e5dcf7c46cf38fa)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_hash32\_identity](group__hash__functions.md#ga3bc327796b6836648e5dcf7c46cf38fa)(const void \*str, size\_t n)

59{

60 switch (n) {

61 case sizeof([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)):

62 return \*([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)str;

63 case sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)):

64 return \*([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*)str;

65 case sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)):

66 return \*([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)str;

67 case sizeof([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)):

68 return ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))(\*([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*)str);

69 default:

70 break;

71 }

72

73 \_\_ASSERT(false, "invalid str length %zu", n);

74

75 return 0;

76}

77

[ 95](group__hash__functions.md#gaaf45db9467193fe9e9d597537dd41c5e)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_hash32\_djb2](group__hash__functions.md#gaaf45db9467193fe9e9d597537dd41c5e)(const void \*str, size\_t n);

96

[ 109](group__hash__functions.md#gad35726d71600a63f4c3ac0382d0a3981)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_hash32\_murmur3](group__hash__functions.md#gad35726d71600a63f4c3ac0382d0a3981)(const void \*str, size\_t n);

110

[ 119](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d)(const void \*str, size\_t n)

120{

121 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_SYS\_HASH\_FUNC32\_CHOICE\_IDENTITY)) {

122 return [sys\_hash32\_identity](group__hash__functions.md#ga3bc327796b6836648e5dcf7c46cf38fa)(str, n);

123 }

124

125 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_SYS\_HASH\_FUNC32\_CHOICE\_DJB2)) {

126 return [sys\_hash32\_djb2](group__hash__functions.md#gaaf45db9467193fe9e9d597537dd41c5e)(str, n);

127 }

128

129 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_SYS\_HASH\_FUNC32\_CHOICE\_MURMUR3)) {

130 return [sys\_hash32\_murmur3](group__hash__functions.md#gad35726d71600a63f4c3ac0382d0a3981)(str, n);

131 }

132

133 \_\_ASSERT(0, "No default 32-bit hash. See CONFIG\_SYS\_HASH\_FUNC32\_CHOICE");

134

135 return 0;

136}

137

141

142#ifdef \_\_cplusplus

143}

144#endif

145

146#endif /\* ZEPHYR\_INCLUDE\_SYS\_HASH\_FUNCTION\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad)

uint32\_t(\* sys\_hash\_func32\_t)(const void \*str, size\_t n)

32-bit Hash function interface

**Definition** hash\_function.h:41

[sys\_hash32\_identity](group__hash__functions.md#ga3bc327796b6836648e5dcf7c46cf38fa)

static uint32\_t sys\_hash32\_identity(const void \*str, size\_t n)

The naive identity hash function.

**Definition** hash\_function.h:58

[sys\_hash32\_djb2](group__hash__functions.md#gaaf45db9467193fe9e9d597537dd41c5e)

uint32\_t sys\_hash32\_djb2(const void \*str, size\_t n)

Daniel J. Bernstein's hash function.

[sys\_hash32\_murmur3](group__hash__functions.md#gad35726d71600a63f4c3ac0382d0a3981)

uint32\_t sys\_hash32\_murmur3(const void \*str, size\_t n)

Murmur3 hash function.

[sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d)

static uint32\_t sys\_hash32(const void \*str, size\_t n)

System default 32-bit hash function.

**Definition** hash\_function.h:119

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_function.h](hash__function_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
