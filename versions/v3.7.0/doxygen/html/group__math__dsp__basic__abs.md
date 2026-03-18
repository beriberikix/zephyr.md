---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__math__dsp__basic__abs.html
original_path: doxygen/html/group__math__dsp__basic__abs.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Absolute Value

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_abs\_f32](#ga5a5358fb90f726256f064757fbab1bcd) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector absolute value. |
| void | [zdsp\_abs\_q7](#ga69c38809979de090a3458ec9b31f4cb4) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q7 vector absolute value. |
| void | [zdsp\_abs\_q15](#ga53ee6bbc05423703f6299fd60c8e1d44) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q15 vector absolute value. |
| void | [zdsp\_abs\_q31](#ga74ccbbaf60257ca482fc96e1d40edeca) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q31 vector absolute value. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_abs\_f16](#gaf178acd8862a2928a65e98f4fef1380b) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector absolute value. |

## Detailed Description

Computes the absolute value of a vector on an element-by-element basis.

```
    dst[n] = abs(src[n]),   0 <= n < block_size.
```

The functions support in-place computation allowing the source and destination pointers to reference the same memory buffer. There are separate functions for floating-point, Q7, Q15, and Q31 data types.

## Function Documentation

## [◆ ](#gaf178acd8862a2928a65e98f4fef1380b)zdsp\_abs\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_abs\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Floating-point vector absolute value.

Parameters
:   | [in] | src | points to the input buffer |
    | --- | --- | --- |
    | [out] | dst | points to the output buffer |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga5a5358fb90f726256f064757fbab1bcd)zdsp\_abs\_f32()

| void zdsp\_abs\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Floating-point vector absolute value.

Parameters
:   | [in] | src | points to the input buffer |
    | --- | --- | --- |
    | [out] | dst | points to the output buffer |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga53ee6bbc05423703f6299fd60c8e1d44)zdsp\_abs\_q15()

| void zdsp\_abs\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q15 vector absolute value.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. The Q15 value -1 (0x8000) will be saturated to the maximum allowable positive value 0x7FFF.

Parameters
:   | [in] | src | points to the input buffer |
    | --- | --- | --- |
    | [out] | dst | points to the output buffer |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga74ccbbaf60257ca482fc96e1d40edeca)zdsp\_abs\_q31()

| void zdsp\_abs\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q31 vector absolute value.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. The Q31 value -1 (0x80000000) will be saturated to the maximum allowable positive value 0x7FFFFFFF.

Parameters
:   | [in] | src | points to the input buffer |
    | --- | --- | --- |
    | [out] | dst | points to the output buffer |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga69c38809979de090a3458ec9b31f4cb4)zdsp\_abs\_q7()

| void zdsp\_abs\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q7 vector absolute value.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. The Q7 value -1 (0x80) will be saturated to the maximum allowable positive value 0x7F.

Parameters
:   | [in] | src | points to the input buffer |
    | --- | --- | --- |
    | [out] | dst | points to the output buffer |
    | [in] | block\_size | number of samples in each vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
