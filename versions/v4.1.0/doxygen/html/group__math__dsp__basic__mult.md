---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__math__dsp__basic__mult.html
original_path: doxygen/html/group__math__dsp__basic__mult.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Multiplication

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_mult\_q7](#gae0792b036a40a19af1c25b3a6a23e988) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q7 vector multiplication. |
| void | [zdsp\_mult\_q15](#gaf8aa8d6e976c9ee5f4ac836506da3bc7) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q15 vector multiplication. |
| void | [zdsp\_mult\_q31](#ga0e4e4ff5e33e792feecf811cb8e96d18) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q31 vector multiplication. |
| void | [zdsp\_mult\_f32](#gac9513150fc602b6bab481faf36f81ca4) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector multiplication. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_mult\_f16](#ga795bc69852005a0e547c3f2794c5397a) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector multiplication. |

## Detailed Description

Element-by-element multiplication of two vectors.

```
    dst[n] = src_a[n] * src_b[n],   0 <= n < block_size.
```

There are separate functions for floating-point, Q7, Q15, and Q31 data types.

## Function Documentation

## [◆ ](#ga795bc69852005a0e547c3f2794c5397a)zdsp\_mult\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_mult\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src\_b*, |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Floating-point vector multiplication.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gac9513150fc602b6bab481faf36f81ca4)zdsp\_mult\_f32()

| void zdsp\_mult\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src\_b*, |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Floating-point vector multiplication.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gaf8aa8d6e976c9ee5f4ac836506da3bc7)zdsp\_mult\_q15()

| void zdsp\_mult\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src\_b*, |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q15 vector multiplication.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q15 range [0x8000 0x7FFF] are saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga0e4e4ff5e33e792feecf811cb8e96d18)zdsp\_mult\_q31()

| void zdsp\_mult\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src\_b*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q31 vector multiplication.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q31 range[0x80000000 0x7FFFFFFF] are saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gae0792b036a40a19af1c25b3a6a23e988)zdsp\_mult\_q7()

| void zdsp\_mult\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src\_b*, |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q7 vector multiplication.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q7 range [0x80 0x7F] are saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
