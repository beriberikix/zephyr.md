---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__math__dsp__basic__clip.html
original_path: doxygen/html/group__math__dsp__basic__clip.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Clipping

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_clip\_f32](#gaa81f891d1946313161d1a2989aafe0e1) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*dst, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) low, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise floating-point clipping. |
| void | [zdsp\_clip\_q31](#ga2a7483cb8150e3caee8fade382dc3ceb) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) low, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise fixed-point clipping. |
| void | [zdsp\_clip\_q15](#ga7c83f52241784bfdf81baf14581435b9) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) low, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise fixed-point clipping. |
| void | [zdsp\_clip\_q7](#ga4e368fccf4ec5f46e82127816ecfc22e) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) low, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise fixed-point clipping. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_clip\_f16](#ga4edd7ba5b9c3791d7857a2c7d1541cab) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*dst, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) low, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) high, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_samples) |
|  | Elementwise floating-point clipping. |

## Detailed Description

Element-by-element clipping of a value.

The value is constrained between 2 bounds.

There are separate functions for floating-point, Q7, Q15, and Q31 data types.

## Function Documentation

## [◆ ](#ga4edd7ba5b9c3791d7857a2c7d1541cab)zdsp\_clip\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_clip\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *dst*, |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) | *low*, |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) | *high*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_samples* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Elementwise floating-point clipping.

Parameters
:   | [in] | src | points to input values |
    | --- | --- | --- |
    | [out] | dst | points to output clipped values |
    | [in] | low | lower bound |
    | [in] | high | higher bound |
    | [in] | num\_samples | number of samples to clip |

## [◆ ](#gaa81f891d1946313161d1a2989aafe0e1)zdsp\_clip\_f32()

| void zdsp\_clip\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *dst*, |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) | *low*, |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) | *high*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_samples* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Elementwise floating-point clipping.

Parameters
:   | [in] | src | points to input values |
    | --- | --- | --- |
    | [out] | dst | points to output clipped values |
    | [in] | low | lower bound |
    | [in] | high | higher bound |
    | [in] | num\_samples | number of samples to clip |

## [◆ ](#ga7c83f52241784bfdf81baf14581435b9)zdsp\_clip\_q15()

| void zdsp\_clip\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) | *low*, |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) | *high*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_samples* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Elementwise fixed-point clipping.

Parameters
:   | [in] | src | points to input values |
    | --- | --- | --- |
    | [out] | dst | points to output clipped values |
    | [in] | low | lower bound |
    | [in] | high | higher bound |
    | [in] | num\_samples | number of samples to clip |

## [◆ ](#ga2a7483cb8150e3caee8fade382dc3ceb)zdsp\_clip\_q31()

| void zdsp\_clip\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) | *low*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) | *high*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_samples* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Elementwise fixed-point clipping.

Parameters
:   | [in] | src | points to input values |
    | --- | --- | --- |
    | [out] | dst | points to output clipped values |
    | [in] | low | lower bound |
    | [in] | high | higher bound |
    | [in] | num\_samples | number of samples to clip |

## [◆ ](#ga4e368fccf4ec5f46e82127816ecfc22e)zdsp\_clip\_q7()

| void zdsp\_clip\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) | *low*, |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) | *high*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_samples* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Elementwise fixed-point clipping.

Parameters
:   | [in] | src | points to input values |
    | --- | --- | --- |
    | [out] | dst | points to output clipped values |
    | [in] | low | lower bound |
    | [in] | high | higher bound |
    | [in] | num\_samples | number of samples to clip |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
