---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__random__api.html
original_path: doxygen/html/group__random__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_rand32\_get](#ga9adb8fe5d17088418788877e568cdbd2) (void) |
|  | Return a 32-bit random value that should pass general randomness tests. |
| void | [sys\_rand\_get](#gaf4f6792ac29c876d59ace1deae53bbd7) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fill the destination buffer with random data values that should pass general randomness tests. |
| int | [sys\_csrand\_get](#ga98f123f216b5df6e27eb980d6e5dec86) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fill the destination buffer with cryptographically secure random data values. |

## Detailed Description

Random Function APIs.

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

## [◆ ](#ga9adb8fe5d17088418788877e568cdbd2)sys\_rand32\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_rand32\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[random.h](random_8h.md)>`

Return a 32-bit random value that should pass general randomness tests.

Note
:   The random value returned is not a cryptographically secure random number value.

Returns
:   32-bit random value.

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
