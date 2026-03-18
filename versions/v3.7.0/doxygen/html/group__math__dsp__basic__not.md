---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__math__dsp__basic__not.html
original_path: doxygen/html/group__math__dsp__basic__not.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector bitwise NOT

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_not\_u8](#gaafd38edd648a03d328d51b5ca9097b5d) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise NOT of a fixed-point vector. |
| void | [zdsp\_not\_u16](#ga3bca20f3c626e1a64dd79d0e22a43bed) (const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise NOT of a fixed-point vector. |
| void | [zdsp\_not\_u32](#gafd6993acd6abeaa529dea84f3fd4d3a9) (const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise NOT of a fixed-point vector. |

## Detailed Description

Compute the logical bitwise NOT.

There are separate functions for [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e), and uint7\_t data types.

## Function Documentation

## [◆ ](#ga3bca20f3c626e1a64dd79d0e22a43bed)zdsp\_not\_u16()

| void zdsp\_not\_u16 | ( | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise NOT of a fixed-point vector.

Parameters
:   | [in] | src | points to input vector |
    | --- | --- | --- |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gafd6993acd6abeaa529dea84f3fd4d3a9)zdsp\_not\_u32()

| void zdsp\_not\_u32 | ( | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise NOT of a fixed-point vector.

Parameters
:   | [in] | src | points to input vector |
    | --- | --- | --- |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gaafd38edd648a03d328d51b5ca9097b5d)zdsp\_not\_u8()

| void zdsp\_not\_u8 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise NOT of a fixed-point vector.

Parameters
:   | [in] | src | points to input vector |
    | --- | --- | --- |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
