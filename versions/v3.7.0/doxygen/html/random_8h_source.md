---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/random_8h_source.html
original_path: doxygen/html/random_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

random.h

[Go to the documentation of this file.](random_8h.md)

1/\*

2 \* Copyright (c) 2013-2014 Wind River Systems, Inc.

3 \* Copyright (c) 2023 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

20

21#ifndef ZEPHYR\_INCLUDE\_RANDOM\_RANDOM\_H\_

22#define ZEPHYR\_INCLUDE\_RANDOM\_RANDOM\_H\_

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <stddef.h>

26#include <[zephyr/kernel.h](kernel_8h.md)>

27

36

37#ifdef \_\_cplusplus

38extern "C" {

39#endif

40

41

[ 53](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)\_\_syscall void [sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)(void \*dst, size\_t len);

54

[ 68](group__random__api.md#ga98f123f216b5df6e27eb980d6e5dec86)\_\_syscall int [sys\_csrand\_get](group__random__api.md#ga98f123f216b5df6e27eb980d6e5dec86)(void \*dst, size\_t len);

69

[ 79](group__random__api.md#ga810eaca8c5f71c9417d87f05c8fa4ebb)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sys\_rand8\_get](group__random__api.md#ga810eaca8c5f71c9417d87f05c8fa4ebb)(void)

80{

81 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ret;

82

83 [sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)(&ret, sizeof(ret));

84

85 return ret;

86}

87

[ 97](group__random__api.md#ga27581a2b65faa6f1f3978ad6794300ba)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sys\_rand16\_get](group__random__api.md#ga27581a2b65faa6f1f3978ad6794300ba)(void)

98{

99 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret;

100

101 [sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)(&ret, sizeof(ret));

102

103 return ret;

104}

105

[ 115](group__random__api.md#ga62cb24a6049b7aa9d03d66786e4a4db6)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_rand32\_get](group__random__api.md#ga62cb24a6049b7aa9d03d66786e4a4db6)(void)

116{

117 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ret;

118

119 [sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)(&ret, sizeof(ret));

120

121 return ret;

122}

123

[ 133](group__random__api.md#ga26da47b7d5a76475b2fc528f5d6eced6)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_rand64\_get](group__random__api.md#ga26da47b7d5a76475b2fc528f5d6eced6)(void)

134{

135 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ret;

136

137 [sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)(&ret, sizeof(ret));

138

139 return ret;

140}

141

142#ifdef \_\_cplusplus

143}

144#endif

145

149

150#include <zephyr/syscalls/random.h>

151#endif /\* ZEPHYR\_INCLUDE\_RANDOM\_RANDOM\_H\_ \*/

[sys\_rand64\_get](group__random__api.md#ga26da47b7d5a76475b2fc528f5d6eced6)

static uint64\_t sys\_rand64\_get(void)

Return a 64-bit random value that should pass general randomness tests.

**Definition** random.h:133

[sys\_rand16\_get](group__random__api.md#ga27581a2b65faa6f1f3978ad6794300ba)

static uint16\_t sys\_rand16\_get(void)

Return a 16-bit random value that should pass general randomness tests.

**Definition** random.h:97

[sys\_rand32\_get](group__random__api.md#ga62cb24a6049b7aa9d03d66786e4a4db6)

static uint32\_t sys\_rand32\_get(void)

Return a 32-bit random value that should pass general randomness tests.

**Definition** random.h:115

[sys\_rand8\_get](group__random__api.md#ga810eaca8c5f71c9417d87f05c8fa4ebb)

static uint8\_t sys\_rand8\_get(void)

Return a 8-bit random value that should pass general randomness tests.

**Definition** random.h:79

[sys\_csrand\_get](group__random__api.md#ga98f123f216b5df6e27eb980d6e5dec86)

int sys\_csrand\_get(void \*dst, size\_t len)

Fill the destination buffer with cryptographically secure random data values.

[sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7)

void sys\_rand\_get(void \*dst, size\_t len)

Fill the destination buffer with random data values that should pass general randomness tests.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

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

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [random](dir_0a0921beff714d16ead0b6fce37bcefe.md)
- [random.h](random_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
