---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__math__dsp__basic__scale.html
original_path: doxygen/html/group__math__dsp__basic__scale.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Scale

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_scale\_f32](#ga3a07935285b763bb9e9106db42292466) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) scale, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a floating-point vector by a scalar. |
| void | [zdsp\_scale\_q7](#ga2158a3f20bd5af0516f5b3af824c32e1) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a Q7 vector by a scalar. |
| void | [zdsp\_scale\_q15](#ga95e03e993542ff1710c771a9dc0eb01b) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a Q15 vector by a scalar. |
| void | [zdsp\_scale\_q31](#ga63eaab2b1ef431e4bceb90b0a701c879) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) scale\_fract, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a Q31 vector by a scalar. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_scale\_f16](#ga26c461531e82511c18902ba908f36230) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) scale, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Multiplies a floating-point vector by a scalar. |

## Detailed Description

Multiply a vector by a scalar value. For floating-point data, the algorithm used is:

```
    dst[n] = src[n] * scale,   0 <= n < block_size.
```

In the fixed-point Q7, Q15, and Q31 functions, scale is represented by a fractional multiplication `scale_fract` and an arithmetic shift `shift`. The shift allows the gain of the scaling operation to exceed 1.0. The algorithm used with fixed-point data is:

```
    dst[n] = (src[n] * scale_fract) << shift,   0 <= n < block_size.
```

The overall scale factor applied to the fixed-point data is

```
    scale = scale_fract * 2^shift.
```

The functions support in-place computation allowing the source and destination pointers to reference the same memory buffer.

## Function Documentation

## [◆ ](#ga26c461531e82511c18902ba908f36230)zdsp\_scale\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_scale\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) | *scale*, |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Multiplies a floating-point vector by a scalar.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | scale | scale factor to be applied |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga3a07935285b763bb9e9106db42292466)zdsp\_scale\_f32()

| void zdsp\_scale\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) | *scale*, |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Multiplies a floating-point vector by a scalar.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | scale | scale factor to be applied |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga95e03e993542ff1710c771a9dc0eb01b)zdsp\_scale\_q15()

| void zdsp\_scale\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) | *scale\_fract*, |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *shift*, |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Multiplies a Q15 vector by a scalar.

Scaling and Overflow Behavior
:   The input data `*src` and `scale_fract` are in 1.15 format. These are multiplied to yield a 2.30 intermediate result and this is shifted with saturation to 1.15 format.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | scale\_fract | fractional portion of the scale value |
    | [in] | shift | number of bits to shift the result by |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga63eaab2b1ef431e4bceb90b0a701c879)zdsp\_scale\_q31()

| void zdsp\_scale\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) | *scale\_fract*, |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *shift*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Multiplies a Q31 vector by a scalar.

Scaling and Overflow Behavior
:   The input data `*src` and `scale_fract` are in 1.31 format. These are multiplied to yield a 2.62 intermediate result and this is shifted with saturation to 1.31 format.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | scale\_fract | fractional portion of the scale value |
    | [in] | shift | number of bits to shift the result by |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga2158a3f20bd5af0516f5b3af824c32e1)zdsp\_scale\_q7()

| void zdsp\_scale\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) | *scale\_fract*, |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *shift*, |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Multiplies a Q7 vector by a scalar.

Scaling and Overflow Behavior
:   The input data `*src` and `scale_fract` are in 1.7 format. These are multiplied to yield a 2.14 intermediate result and this is shifted with saturation to 1.7 format.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | scale\_fract | fractional portion of the scale value |
    | [in] | shift | number of bits to shift the result by |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
