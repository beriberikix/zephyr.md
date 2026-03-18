---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__math__dsp__basic__offset.html
original_path: doxygen/html/group__math__dsp__basic__offset.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Offset

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_offset\_f32](#ga1f14e702ad5dc6482fcdb4758ad862c3) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) offset, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a floating-point vector. |
| void | [zdsp\_offset\_q7](#ga701b8bbd1437e0f19807c38fd4d0e7e9) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) offset, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a Q7 vector. |
| void | [zdsp\_offset\_q15](#ga1740996532090e41ce20913bb201023c) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) offset, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a Q15 vector. |
| void | [zdsp\_offset\_q31](#ga2b5958ec0fc8bb26662c41136ec46b3e) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) offset, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a Q31 vector. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_offset\_f16](#ga60d4ef0543308773e651a0f40b3b0fe1) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) offset, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Adds a constant offset to a floating-point vector. |

## Detailed Description

Adds a constant offset to each element of a vector.

```
    dst[n] = src[n] + offset,   0 <= n < block_size.
```

The functions support in-place computation allowing the source and destination pointers to reference the same memory buffer. There are separate functions for floating-point, Q7, Q15, and Q31 data types.

## Function Documentation

## [◆ ](#ga60d4ef0543308773e651a0f40b3b0fe1)zdsp\_offset\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_offset\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) | *offset*, |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Adds a constant offset to a floating-point vector.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | offset | is the offset to be added |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga1f14e702ad5dc6482fcdb4758ad862c3)zdsp\_offset\_f32()

| void zdsp\_offset\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) | *offset*, |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Adds a constant offset to a floating-point vector.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | offset | is the offset to be added |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga1740996532090e41ce20913bb201023c)zdsp\_offset\_q15()

| void zdsp\_offset\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) | *offset*, |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Adds a constant offset to a Q15 vector.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q15 range [0x8000 0x7FFF] are saturated.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | offset | is the offset to be added |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga2b5958ec0fc8bb26662c41136ec46b3e)zdsp\_offset\_q31()

| void zdsp\_offset\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) | *offset*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Adds a constant offset to a Q31 vector.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q31 range [0x80000000 0x7FFFFFFF] are saturated.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | offset | is the offset to be added |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga701b8bbd1437e0f19807c38fd4d0e7e9)zdsp\_offset\_q7()

| void zdsp\_offset\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) | *offset*, |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Adds a constant offset to a Q7 vector.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q7 range [0x80 0x7F] are saturated.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | offset | is the offset to be added |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
