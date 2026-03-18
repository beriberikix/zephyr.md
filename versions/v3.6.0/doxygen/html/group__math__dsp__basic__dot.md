---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__math__dsp__basic__dot.html
original_path: doxygen/html/group__math__dsp__basic__dot.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Dot Product

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_dot\_prod\_f32](#ga66932c50dc7e2b7207ad5c8218c110a6) (const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_a, const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \*result) |
|  | Dot product of floating-point vectors. |
| void | [zdsp\_dot\_prod\_q7](#gaa6bdeed693734e5d1c7b93b58eaf9eeb) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_a, const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*result) |
|  | Dot product of Q7 vectors. |
| void | [zdsp\_dot\_prod\_q15](#ga5a76ac790b7d981b97143f7473587ccf) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_a, const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6) \*result) |
|  | Dot product of Q15 vectors. |
| void | [zdsp\_dot\_prod\_q31](#gaae752f1d9645d8c80fcdabc0f0b249f8) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_a, const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6) \*result) |
|  | Dot product of Q31 vectors. |
| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void | [zdsp\_dot\_prod\_f16](#ga11af65d379fa201a04408544ddca8354) (const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_a, const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size, [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \*result) |
|  | Dot product of floating-point vectors. |

## Detailed Description

Computes the dot product of two vectors. The vectors are multiplied element-by-element and then summed.

```
    sum = src_a[0]*src_b[0] + src_a[1]*src_b[1] + ... + src_a[block_size-1]*src_b[block_size-1]
```

There are separate functions for floating-point, Q7, Q15, and Q31 data types.

## Function Documentation

## [◆ ](#ga11af65d379fa201a04408544ddca8354)zdsp\_dot\_prod\_f16()

| [DSP\_FUNC\_SCOPE](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7) void zdsp\_dot\_prod\_f16 | ( | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *src\_b*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size*, |
|  |  | [float16\_t](group__math__dsp.md#gaa94dc44bddb5718a22bb612890a7fe9f) \* | *result* ) |

`#include <[basicmath_f16.h](basicmath__f16_8h.md)>`

Dot product of floating-point vectors.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [in] | block\_size | number of samples in each vector |
    | [out] | result | output result returned here |

## [◆ ](#ga66932c50dc7e2b7207ad5c8218c110a6)zdsp\_dot\_prod\_f32()

| void zdsp\_dot\_prod\_f32 | ( | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *src\_b*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size*, |
|  |  | [float32\_t](group__math__dsp.md#ga4611b605e45ab401f02cab15c5e38715) \* | *result* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Dot product of floating-point vectors.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [in] | block\_size | number of samples in each vector |
    | [out] | result | output result returned here |

## [◆ ](#ga5a76ac790b7d981b97143f7473587ccf)zdsp\_dot\_prod\_q15()

| void zdsp\_dot\_prod\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src\_b*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size*, |
|  |  | [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6) \* | *result* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Dot product of Q15 vectors.

Scaling and Overflow Behavior
:   The intermediate multiplications are in 1.15 x 1.15 = 2.30 format and these results are added to a 64-bit accumulator in 34.30 format. Nonsaturating additions are used and given that there are 33 guard bits in the accumulator there is no risk of overflow. The return result is in 34.30 format.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [in] | block\_size | number of samples in each vector |
    | [out] | result | output result returned here |

## [◆ ](#gaae752f1d9645d8c80fcdabc0f0b249f8)zdsp\_dot\_prod\_q31()

| void zdsp\_dot\_prod\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src\_b*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size*, |
|  |  | [q63\_t](group__math__dsp.md#ga5aea1cb12fc02d9d44c8abf217eaa5c6) \* | *result* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Dot product of Q31 vectors.

Scaling and Overflow Behavior
:   The intermediate multiplications are in 1.31 x 1.31 = 2.62 format and these are truncated to 2.48 format by discarding the lower 14 bits. The 2.48 result is then added without saturation to a 64-bit accumulator in 16.48 format. There are 15 guard bits in the accumulator and there is no risk of overflow as long as the length of the vectors is less than 2^16 elements. The return result is in 16.48 format.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [in] | block\_size | number of samples in each vector |
    | [out] | result | output result returned here |

## [◆ ](#gaa6bdeed693734e5d1c7b93b58eaf9eeb)zdsp\_dot\_prod\_q7()

| void zdsp\_dot\_prod\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src\_b*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *result* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Dot product of Q7 vectors.

Scaling and Overflow Behavior
:   The intermediate multiplications are in 1.7 x 1.7 = 2.14 format and these results are added to an accumulator in 18.14 format. Nonsaturating additions are used and there is no danger of wrap around as long as the vectors are less than 2^18 elements long. The return result is in 18.14 format.

Parameters
:   | [in] | src\_a | points to the first input vector |
    | --- | --- | --- |
    | [in] | src\_b | points to the second input vector |
    | [in] | block\_size | number of samples in each vector |
    | [out] | result | output result returned here |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
