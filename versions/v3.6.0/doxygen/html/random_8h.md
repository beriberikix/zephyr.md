---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/random_8h.html
original_path: doxygen/html/random_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

random.h File Reference

Random number generator header file.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <syscalls/random.h>`

[Go to the source code of this file.](random_8h_source.md)

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_rand32\_get](group__random__api.md#ga9adb8fe5d17088418788877e568cdbd2) (void) |
|  | Return a 32-bit random value that should pass general randomness tests. |
| void | [sys\_rand\_get](group__random__api.md#gaf4f6792ac29c876d59ace1deae53bbd7) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fill the destination buffer with random data values that should pass general randomness tests. |
| int | [sys\_csrand\_get](group__random__api.md#ga98f123f216b5df6e27eb980d6e5dec86) (void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Fill the destination buffer with cryptographically secure random data values. |

## Detailed Description

Random number generator header file.

This header file declares prototypes for the kernel's random number generator APIs.

Typically, a platform enables the appropriate source for the random number generation based on the hardware platform's capabilities or (for testing purposes only) enables the TEST\_RANDOM\_GENERATOR configuration option.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [random](dir_0a0921beff714d16ead0b6fce37bcefe.md)
- [random.h](random_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
