---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__math__dsp__basic__xor.html
original_path: doxygen/html/group__math__dsp__basic__xor.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector bitwise XOR

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_xor\_u8](#ga4f5a442ce2ce79a6d09fde4648ceb100) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_a, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_b, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise XOR of two fixed-point vectors. |
| void | [zdsp\_xor\_u16](#gaa4d486a9a9022120e86e6e5d62940444) (const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_a, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise XOR of two fixed-point vectors. |
| void | [zdsp\_xor\_u32](#gac4dd8fed6e7485a0e989fb37b3fe0c77) (const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_a, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise XOR of two fixed-point vectors. |

## Detailed Description

Compute the logical bitwise XOR.

There are separate functions for [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e), and uint7\_t data types.

## Function Documentation

## [◆ ](#gaa4d486a9a9022120e86e6e5d62940444)zdsp\_xor\_u16()

| void zdsp\_xor\_u16 | ( | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *src\_b*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise XOR of two fixed-point vectors.

Parameters
:   | [in] | src\_a | points to input vector A |
    | --- | --- | --- |
    | [in] | src\_b | points to input vector B |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gac4dd8fed6e7485a0e989fb37b3fe0c77)zdsp\_xor\_u32()

| void zdsp\_xor\_u32 | ( | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *src\_b*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise XOR of two fixed-point vectors.

Parameters
:   | [in] | src\_a | points to input vector A |
    | --- | --- | --- |
    | [in] | src\_b | points to input vector B |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#ga4f5a442ce2ce79a6d09fde4648ceb100)zdsp\_xor\_u8()

| void zdsp\_xor\_u8 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src\_b*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise XOR of two fixed-point vectors.

Parameters
:   | [in] | src\_a | points to input vector A |
    | --- | --- | --- |
    | [in] | src\_b | points to input vector B |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
