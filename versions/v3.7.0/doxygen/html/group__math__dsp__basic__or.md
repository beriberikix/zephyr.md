---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__math__dsp__basic__or.html
original_path: doxygen/html/group__math__dsp__basic__or.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Vector bitwise OR

[DSP Interface](group__math__dsp.md) » [Basic Math Functions](group__math__dsp__basic.md)

| Functions | |
| --- | --- |
| void | [zdsp\_or\_u8](#gabf9687bce70f19c4192b2ddba7b0d2da) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_a, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src\_b, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise OR of two fixed-point vectors. |
| void | [zdsp\_or\_u16](#ga979e50ef34a5e5c8dc28f1cfc5ef708a) (const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_a, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*src\_b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise OR of two fixed-point vectors. |
| void | [zdsp\_or\_u32](#gaa218930efe8ab83663eb00b4f6f170bc) (const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_a, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*src\_b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block\_size) |
|  | Compute the logical bitwise OR of two fixed-point vectors. |

## Detailed Description

Compute the logical bitwise OR.

There are separate functions for [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e), and uint7\_t data types.

## Function Documentation

## [◆ ](#ga979e50ef34a5e5c8dc28f1cfc5ef708a)zdsp\_or\_u16()

| void zdsp\_or\_u16 | ( | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *src\_b*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise OR of two fixed-point vectors.

Parameters
:   | [in] | src\_a | points to input vector A |
    | --- | --- | --- |
    | [in] | src\_b | points to input vector B |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gaa218930efe8ab83663eb00b4f6f170bc)zdsp\_or\_u32()

| void zdsp\_or\_u32 | ( | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *src\_b*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise OR of two fixed-point vectors.

Parameters
:   | [in] | src\_a | points to input vector A |
    | --- | --- | --- |
    | [in] | src\_b | points to input vector B |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

## [◆ ](#gabf9687bce70f19c4192b2ddba7b0d2da)zdsp\_or\_u8()

| void zdsp\_or\_u8 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src\_a*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src\_b*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *block\_size* ) |

`#include <[basicmath.h](basicmath_8h.md)>`

Compute the logical bitwise OR of two fixed-point vectors.

Parameters
:   | [in] | src\_a | points to input vector A |
    | --- | --- | --- |
    | [in] | src\_b | points to input vector B |
    | [out] | dst | points to output vector |
    | [in] | block\_size | number of samples in each vector |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
