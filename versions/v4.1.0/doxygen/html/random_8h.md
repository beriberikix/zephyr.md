---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/random_8h.html
original_path: doxygen/html/random_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

random.h File Reference

Random number generator header file.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <zephyr/syscalls/random.h>`

[Go to the source code of this file.](random_8h_source.md)

| Functions | |
| --- | --- |
| void | [sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fill the destination buffer with random data values that should pass general randomness tests. |
| int | [sys\_csrand\_get](group__random__api.md#ga98f123f216b5df6e27eb980d6e5dec86) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fill the destination buffer with cryptographically secure random data values. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_rand8\_get](group__random__api.md#ga810eaca8c5f71c9417d87f05c8fa4ebb) (void) |
|  | Return a 8-bit random value that should pass general randomness tests. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sys\_rand16\_get](group__random__api.md#ga27581a2b65faa6f1f3978ad6794300ba) (void) |
|  | Return a 16-bit random value that should pass general randomness tests. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_rand32\_get](group__random__api.md#ga62cb24a6049b7aa9d03d66786e4a4db6) (void) |
|  | Return a 32-bit random value that should pass general randomness tests. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_rand64\_get](group__random__api.md#ga26da47b7d5a76475b2fc528f5d6eced6) (void) |
|  | Return a 64-bit random value that should pass general randomness tests. |

## Detailed Description

Random number generator header file.

This header file declares prototypes for the kernel's random number generator APIs.

Typically, a platform enables the appropriate source for the random number generation based on the hardware platform's capabilities or (for testing purposes only) enables the TEST\_RANDOM\_GENERATOR configuration option.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [random](dir_0a0921beff714d16ead0b6fce37bcefe.md)
- [random.h](random_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
