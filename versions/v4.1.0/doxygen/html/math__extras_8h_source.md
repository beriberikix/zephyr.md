---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/math__extras_8h_source.html
original_path: doxygen/html/math__extras_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

math\_extras.h

[Go to the documentation of this file.](math__extras_8h.md)

1/\*

2 \* Copyright (c) 2019 Facebook.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_SYS\_MATH\_EXTRAS\_H\_

20#define ZEPHYR\_INCLUDE\_SYS\_MATH\_EXTRAS\_H\_

21

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23#include <[stdbool.h](stdbool_8h.md)>

24#include <stddef.h>

25

33

[ 41](group__math__extras.md#ga62d018abdf97551665cab7486b5a519a)static bool [u16\_add\_overflow](group__math__extras.md#ga62d018abdf97551665cab7486b5a519a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result);

42

50

[ 51](group__math__extras.md#ga3f36aa272f5595d78c6e8219b2c4dbfb)static bool [u32\_add\_overflow](group__math__extras.md#ga3f36aa272f5595d78c6e8219b2c4dbfb)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result);

52

[ 60](group__math__extras.md#gaf98ec1d8b1c00e30382eed01853e3307)static bool [u64\_add\_overflow](group__math__extras.md#gaf98ec1d8b1c00e30382eed01853e3307)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result);

61

[ 69](group__math__extras.md#ga7aaec179564038b540aaf4ab3c9a666d)static bool [size\_add\_overflow](group__math__extras.md#ga7aaec179564038b540aaf4ab3c9a666d)(size\_t a, size\_t b, size\_t \*result);

70

72

80

[ 88](group__math__extras.md#ga292df7083a9da5525cda13e2546e81ba)static bool [u16\_mul\_overflow](group__math__extras.md#ga292df7083a9da5525cda13e2546e81ba)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result);

89

97

[ 98](group__math__extras.md#ga427e8cd4fcafab244576994acc9b960f)static bool [u32\_mul\_overflow](group__math__extras.md#ga427e8cd4fcafab244576994acc9b960f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result);

[ 106](group__math__extras.md#ga366f6606874071677bf9079647d9abce)static bool [u64\_mul\_overflow](group__math__extras.md#ga366f6606874071677bf9079647d9abce)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result);

107

[ 115](group__math__extras.md#ga790b24a5d239afcc08d9e4f66c25ea56)static bool [size\_mul\_overflow](group__math__extras.md#ga790b24a5d239afcc08d9e4f66c25ea56)(size\_t a, size\_t b, size\_t \*result);

116

118

126

[ 132](group__math__extras.md#ga97e8d8a40a45899ab7e5ce718342536b)static int [u32\_count\_leading\_zeros](group__math__extras.md#ga97e8d8a40a45899ab7e5ce718342536b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x);

133

[ 139](group__math__extras.md#gaf5f31e98f2f675a0b4cc54b7fba6f56c)static int [u64\_count\_leading\_zeros](group__math__extras.md#gaf5f31e98f2f675a0b4cc54b7fba6f56c)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x);

140

142

150

[ 156](group__math__extras.md#ga4cb313f98c3fd3b00d6f4db74a9a0076)static int [u32\_count\_trailing\_zeros](group__math__extras.md#ga4cb313f98c3fd3b00d6f4db74a9a0076)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x);

157

[ 163](group__math__extras.md#ga300356629c0388d37958ef026180ea4d)static int [u64\_count\_trailing\_zeros](group__math__extras.md#ga300356629c0388d37958ef026180ea4d)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x);

164

166

168

169#include <[zephyr/sys/math\_extras\_impl.h](math__extras__impl_8h.md)>

170

171#endif /\* ZEPHYR\_INCLUDE\_SYS\_MATH\_EXTRAS\_H\_ \*/

[u16\_mul\_overflow](group__math__extras.md#ga292df7083a9da5525cda13e2546e81ba)

static bool u16\_mul\_overflow(uint16\_t a, uint16\_t b, uint16\_t \*result)

Multiply two unsigned 16-bit integers.

[u64\_count\_trailing\_zeros](group__math__extras.md#ga300356629c0388d37958ef026180ea4d)

static int u64\_count\_trailing\_zeros(uint64\_t x)

Count the number of trailing zero bits in a 64-bit integer.

[u64\_mul\_overflow](group__math__extras.md#ga366f6606874071677bf9079647d9abce)

static bool u64\_mul\_overflow(uint64\_t a, uint64\_t b, uint64\_t \*result)

Multiply two unsigned 64-bit integers.

[u32\_add\_overflow](group__math__extras.md#ga3f36aa272f5595d78c6e8219b2c4dbfb)

static bool u32\_add\_overflow(uint32\_t a, uint32\_t b, uint32\_t \*result)

Add two unsigned 32-bit integers.

[u32\_mul\_overflow](group__math__extras.md#ga427e8cd4fcafab244576994acc9b960f)

static bool u32\_mul\_overflow(uint32\_t a, uint32\_t b, uint32\_t \*result)

Multiply two unsigned 32-bit integers.

[u32\_count\_trailing\_zeros](group__math__extras.md#ga4cb313f98c3fd3b00d6f4db74a9a0076)

static int u32\_count\_trailing\_zeros(uint32\_t x)

Count the number of trailing zero bits in a 32-bit integer.

[u16\_add\_overflow](group__math__extras.md#ga62d018abdf97551665cab7486b5a519a)

static bool u16\_add\_overflow(uint16\_t a, uint16\_t b, uint16\_t \*result)

Add two unsigned 16-bit integers.

[size\_mul\_overflow](group__math__extras.md#ga790b24a5d239afcc08d9e4f66c25ea56)

static bool size\_mul\_overflow(size\_t a, size\_t b, size\_t \*result)

Multiply two size\_t integers.

[size\_add\_overflow](group__math__extras.md#ga7aaec179564038b540aaf4ab3c9a666d)

static bool size\_add\_overflow(size\_t a, size\_t b, size\_t \*result)

Add two size\_t integers.

[u32\_count\_leading\_zeros](group__math__extras.md#ga97e8d8a40a45899ab7e5ce718342536b)

static int u32\_count\_leading\_zeros(uint32\_t x)

Count the number of leading zero bits in a 32-bit integer.

[u64\_count\_leading\_zeros](group__math__extras.md#gaf5f31e98f2f675a0b4cc54b7fba6f56c)

static int u64\_count\_leading\_zeros(uint64\_t x)

Count the number of leading zero bits in a 64-bit integer.

[u64\_add\_overflow](group__math__extras.md#gaf98ec1d8b1c00e30382eed01853e3307)

static bool u64\_add\_overflow(uint64\_t a, uint64\_t b, uint64\_t \*result)

Add two unsigned 64-bit integers.

[types.h](include_2zephyr_2types_8h.md)

[math\_extras\_impl.h](math__extras__impl_8h.md)

Inline implementation of functions declared in math\_extras.h.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [math\_extras.h](math__extras_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
