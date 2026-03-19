---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__math__dsp__basic__negate.html
original_path: doxygen/html/group__math__dsp__basic__negate.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Negate

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_negate\_f32](#gad8760ce77fcf2198f73813278fa15343) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a floating-point vector. |
| void | [zdsp\_negate\_q7](#ga578a3cee7cff2d818e41ec974066d55a) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a Q7 vector. |
| void | [zdsp\_negate\_q15](#ga41dc3e0d8a0bd3654f74cbbd9038153d) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a Q15 vector. |
| void | [zdsp\_negate\_q31](#ga08591323e804b4d7932c7bade4331705) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a Q31 vector. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_negate\_f16](#ga7aacb425c3dfb2c5d8664a7cf4031c3b) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Negates the elements of a floating-point vector. |

## Detailed Description

Negates the elements of a vector.

```
    dst[n] = -src[n],   0 <= n < block_size.
```

The functions support in-place computation allowing the source and destination pointers to reference the same memory buffer. There are separate functions for floating-point, Q7, Q15, and Q31 data types.

## Function Documentation

## [◆ ](#ga7aacb425c3dfb2c5d8664a7cf4031c3b)zdsp\_negate\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_negate\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Negates the elements of a floating-point vector.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#gad8760ce77fcf2198f73813278fa15343)zdsp\_negate\_f32()

| void zdsp\_negate\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Negates the elements of a floating-point vector.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga41dc3e0d8a0bd3654f74cbbd9038153d)zdsp\_negate\_q15()

| void zdsp\_negate\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Negates the elements of a Q15 vector.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. The Q15 value -1 (0x8000) is saturated to the maximum allowable positive value 0x7FFF.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga08591323e804b4d7932c7bade4331705)zdsp\_negate\_q31()

| void zdsp\_negate\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Negates the elements of a Q31 vector.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. The Q31 value -1 (0x80000000) is saturated to the maximum allowable positive value 0x7FFFFFFF.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga578a3cee7cff2d818e41ec974066d55a)zdsp\_negate\_q7()

| void zdsp\_negate\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Negates the elements of a Q7 vector.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. The Q7 value -1 (0x80) is saturated to the maximum allowable positive value 0x7F.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
