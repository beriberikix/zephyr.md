---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__math__dsp__basic__sub.html
original_path: doxygen/html/group__math__dsp__basic__sub.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Subtraction

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_sub\_f32](#gafc66edd5888b19174cb24c2ea858d24d) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector subtraction. |
| void | [zdsp\_sub\_q7](#ga4eb67772a48933a9f24a68f73228adbf) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q7 vector subtraction. |
| void | [zdsp\_sub\_q15](#gab9698353b69654eefbd76ff6f723a4f3) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q15 vector subtraction. |
| void | [zdsp\_sub\_q31](#ga693b9677fdf54694e49e03a9b629b35d) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Q31 vector subtraction. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_sub\_f16](#ga500f6403d4382bc797231d7962275230) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Floating-point vector subtraction. |

## Detailed Description

Element-by-element subtraction of two vectors.

```
    dst[n] = src_a[n] - src_b[n],   0 <= n < block_size.
```

There are separate functions for floating-point, Q7, Q15, and Q31 data types.

## Function Documentation

## [◆ ](#ga500f6403d4382bc797231d7962275230)zdsp\_sub\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_sub\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src\_b*, |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Floating-point vector subtraction.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gafc66edd5888b19174cb24c2ea858d24d)zdsp\_sub\_f32()

| void zdsp\_sub\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src\_b*, |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Floating-point vector subtraction.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gab9698353b69654eefbd76ff6f723a4f3)zdsp\_sub\_q15()

| void zdsp\_sub\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src\_b*, |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q15 vector subtraction.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q15 range [0x8000 0x7FFF] are saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga693b9677fdf54694e49e03a9b629b35d)zdsp\_sub\_q31()

| void zdsp\_sub\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src\_b*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q31 vector subtraction.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q31 range [0x80000000 0x7FFFFFFF] are saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga4eb67772a48933a9f24a68f73228adbf)zdsp\_sub\_q7()

| void zdsp\_sub\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src\_b*, |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Q7 vector subtraction.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q7 range [0x80 0x7F] will be saturated.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in each vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
