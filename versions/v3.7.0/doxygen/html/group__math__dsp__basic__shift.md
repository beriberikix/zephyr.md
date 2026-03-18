---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__math__dsp__basic__shift.html
original_path: doxygen/html/group__math__dsp__basic__shift.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector Shift

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_shift\_q7](#ga8eb72ff139c173d3e1794a1d1c1c8fde) (const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits, [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Shifts the elements of a Q7 vector a specified number of bits. |
| void | [zdsp\_shift\_q15](#ga738fc0fe86b9c910a30fceff7dc4a789) (const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits, [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Shifts the elements of a Q15 vector a specified number of bits. |
| void | [zdsp\_shift\_q31](#gaf9af89a3c76ad385eec0225185b522c9) (const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*src, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) shift\_bits, [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Shifts the elements of a Q31 vector a specified number of bits. |

## Detailed Description

Shifts the elements of a fixed-point vector by a specified number of bits. There are separate functions for Q7, Q15, and Q31 data types. The underlying algorithm used is:

```
    dst[n] = src[n] << shift,   0 <= n < block_size.
```

If `shift` is positive then the elements of the vector are shifted to the left. If `shift` is negative then the elements of the vector are shifted to the right.

The functions support in-place computation allowing the source and destination pointers to reference the same memory buffer.

## Function Documentation

## [◆ ](#ga738fc0fe86b9c910a30fceff7dc4a789)zdsp\_shift\_q15()

| void zdsp\_shift\_q15 | ( | const [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *shift\_bits*, |
|  |  | [q15\_t](group__math__dsp.md#gab5a8fb21a5b3b983d5f54f31614052ea) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Shifts the elements of a Q15 vector a specified number of bits.

Precondition
:   Scaling and Overflow Behavior The function uses saturating arithmetic. Results outside of the allowable Q15 range [0x8000 0x7FFF] are saturated.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | shift\_bits | number of bits to shift. A positive value shifts left; a negative value shifts right. |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#gaf9af89a3c76ad385eec0225185b522c9)zdsp\_shift\_q31()

| void zdsp\_shift\_q31 | ( | const [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *shift\_bits*, |
|  |  | [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Shifts the elements of a Q31 vector a specified number of bits.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q31 range [0x80000000 0x7FFFFFFF] are saturated.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | shift\_bits | number of bits to shift. A positive value shifts left; a negative value shifts right. |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

## [◆ ](#ga8eb72ff139c173d3e1794a1d1c1c8fde)zdsp\_shift\_q7()

| void zdsp\_shift\_q7 | ( | const [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *shift\_bits*, |
|  |  | [q7\_t](group__math__dsp.md#gae541b6f232c305361e9b416fc9eed263) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Shifts the elements of a Q7 vector a specified number of bits.

Scaling and Overflow Behavior
:   The function uses saturating arithmetic. Results outside of the allowable Q7 range [0x80 0x7F] are saturated.

Parameters
:   | [in] | src | points to the input vector |
    | --- | --- | --- |
    | [in] | shift\_bits | number of bits to shift. A positive value shifts left; a negative value shifts right. |
    | [out] | dst | points to the output vector |
    | [in] | block\_size | number of samples in the vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
