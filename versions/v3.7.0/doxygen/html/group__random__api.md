---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__random__api.html
original_path: doxygen/html/group__random__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Random Function APIs

[Operating System Services](group__os__services.md) » [Crypto](group__crypto.md)

Random Function APIs.
[More...](#details)

| Functions | |
| --- | --- |
| void | [sys\_rand\_get](#gaf4f6792ac29c876d59ace1deae53bbd7) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fill the destination buffer with random data values that should pass general randomness tests. |
| int | [sys\_csrand\_get](#ga98f123f216b5df6e27eb980d6e5dec86) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fill the destination buffer with cryptographically secure random data values. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_rand8\_get](#ga810eaca8c5f71c9417d87f05c8fa4ebb) (void) |
|  | Return a 8-bit random value that should pass general randomness tests. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sys\_rand16\_get](#ga27581a2b65faa6f1f3978ad6794300ba) (void) |
|  | Return a 16-bit random value that should pass general randomness tests. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_rand32\_get](#ga62cb24a6049b7aa9d03d66786e4a4db6) (void) |
|  | Return a 32-bit random value that should pass general randomness tests. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_rand64\_get](#ga26da47b7d5a76475b2fc528f5d6eced6) (void) |
|  | Return a 64-bit random value that should pass general randomness tests. |

## Detailed Description

Random Function APIs.

Since
:   1.0

Version
:   1.0.0

## Function Documentation

## [◆ ](#ga98f123f216b5df6e27eb980d6e5dec86)sys\_csrand\_get()

| int sys\_csrand\_get | ( | void \* | *dst*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[random.h](random_8h.md)>`

Fill the destination buffer with cryptographically secure random data values.

Note
:   If the random values requested do not need to be cryptographically secure then use [sys\_rand\_get()](#gaf4f6792ac29c876d59ace1deae53bbd7) instead.

Parameters
:   | [out] | dst | destination buffer to fill. |
    | --- | --- | --- |
    |  | len | size of the destination buffer. |

Returns
:   0 if success, -EIO if entropy reseed error

## [◆ ](#ga27581a2b65faa6f1f3978ad6794300ba)sys\_rand16\_get()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sys\_rand16\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[random.h](random_8h.md)>`

Return a 16-bit random value that should pass general randomness tests.

Note
:   The random value returned is not a cryptographically secure random number value.

Returns
:   16-bit random value.

## [◆ ](#ga62cb24a6049b7aa9d03d66786e4a4db6)sys\_rand32\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_rand32\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[random.h](random_8h.md)>`

Return a 32-bit random value that should pass general randomness tests.

Note
:   The random value returned is not a cryptographically secure random number value.

Returns
:   32-bit random value.

## [◆ ](#ga26da47b7d5a76475b2fc528f5d6eced6)sys\_rand64\_get()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_rand64\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[random.h](random_8h.md)>`

Return a 64-bit random value that should pass general randomness tests.

Note
:   The random value returned is not a cryptographically secure random number value.

Returns
:   64-bit random value.

## [◆ ](#ga810eaca8c5f71c9417d87f05c8fa4ebb)sys\_rand8\_get()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_rand8\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[random.h](random_8h.md)>`

Return a 8-bit random value that should pass general randomness tests.

Note
:   The random value returned is not a cryptographically secure random number value.

Returns
:   8-bit random value.

## [◆ ](#gaf4f6792ac29c876d59ace1deae53bbd7)sys\_rand\_get()

| void sys\_rand\_get | ( | void \* | *dst*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[random.h](random_8h.md)>`

Fill the destination buffer with random data values that should pass general randomness tests.

Note
:   The random values returned are not considered cryptographically secure random number values.

Parameters
:   | [out] | dst | destination buffer to fill with random data. |
    | --- | --- | --- |
    |  | len | size of the destination buffer. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
