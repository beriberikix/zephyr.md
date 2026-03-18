---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__math__dsp__basic__add.html
original_path: doxygen/html/group__math__dsp__basic__add.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Addition

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_add\_f32](#gae890add140205717dcb4b1c39650b797) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector addition. |
| void | [zdsp\_add\_q7](#gae5d919e8595e80216302953797fcf987) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q7 vector addition. |
| void | [zdsp\_add\_q15](#ga978af9251a9c8b8d62b47a921dcf9d38) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q15 vector addition. |
| void | [zdsp\_add\_q31](#gad2bbabc990f868b3ecfe270458e22657) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q31 vector addition. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_add\_f16](#ga3ad2849433440c2d1175cd6f18e6eade) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector addition. |

## Detailed Description

Element-by-element addition of two vectors.

```
    dst[n] = src_a[n] + src_b[n],   0 <= n < block_size.
```

There are separate functions for floating-point, Q7, Q15, and Q31 data types.

## Function Documentation

## [◆ ](#ga3ad2849433440c2d1175cd6f18e6eade)zdsp\_add\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_add\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src\_b*, |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Floating-point vector addition.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gae890add140205717dcb4b1c39650b797)zdsp\_add\_f32()

| void zdsp\_add\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src\_b*, |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Floating-point vector addition.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga978af9251a9c8b8d62b47a921dcf9d38)zdsp\_add\_q15()

| void zdsp\_add\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src\_b*, |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q15 vector addition.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q15 range [0x8000 0x7FFF] are saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gad2bbabc990f868b3ecfe270458e22657)zdsp\_add\_q31()

| void zdsp\_add\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src\_b*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q31 vector addition.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q31 range [0x80000000 0x7FFFFFFF] are saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gae5d919e8595e80216302953797fcf987)zdsp\_add\_q7()

| void zdsp\_add\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src\_b*, |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q7 vector addition.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q7 range [0x80 0x7F] are saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
