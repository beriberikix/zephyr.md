---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/include_2zephyr_2dsp_2types_8h_source.html
original_path: doxygen/html/include_2zephyr_2dsp_2types_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

types.h

[Go to the documentation of this file.](include_2zephyr_2dsp_2types_8h.md)

1/\* Copyright (c) 2022 Google LLC

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4

5#ifndef INCLUDE\_ZEPHYR\_DSP\_TYPES\_H\_

6#define INCLUDE\_ZEPHYR\_DSP\_TYPES\_H\_

7

8#include <[stdint.h](stdint_8h.md)>

9

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 23](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263)typedef [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263);

24

[ 29](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea)typedef [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea);

30

[ 35](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0);

36

[ 41](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6);

42

47#if defined(CONFIG\_FP16)

[ 48](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f)typedef \_\_fp16 [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f);

49#endif /\* CONFIG\_FP16 \*/

50

[ 55](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715)typedef float [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715);

56

[ 61](group__math__dsp.md#gac55f3ae81b5bc9053760baacf57e47f4)typedef double [float64\_t](group__math__dsp.md#gac55f3ae81b5bc9053760baacf57e47f4);

62

63#ifdef \_\_cplusplus

64}

65#endif

66

70

71#endif /\* INCLUDE\_ZEPHYR\_DSP\_TYPES\_H\_ \*/

[float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715)

float float32\_t

32-bit floating-point type definition.

**Definition** types.h:55

[q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6)

int64\_t q63\_t

64-bit fractional data type in 1.63 format.

**Definition** types.h:41

[float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f)

\_\_fp16 float16\_t

16-bit floating point type definition.

**Definition** types.h:48

[q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea)

int16\_t q15\_t

16-bit fractional data type in 1.15 format.

**Definition** types.h:29

[float64\_t](group__math__dsp.md#gac55f3ae81b5bc9053760baacf57e47f4)

double float64\_t

64-bit floating-point type definition.

**Definition** types.h:61

[q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)

int32\_t q31\_t

32-bit fractional data type in 1.31 format.

**Definition** types.h:35

[q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263)

int8\_t q7\_t

8-bit fractional data type in 1.7 format.

**Definition** types.h:23

[stdint.h](stdint_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [types.h](include_2zephyr_2dsp_2types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
