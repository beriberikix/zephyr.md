---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hash__function_8h.html
original_path: doxygen/html/hash__function_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_function.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](hash__function_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [sys\_hash\_func32\_t](group__hash__functions.md#ga2566ca73d30b47ae66659e26fc985fad)) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | 32-bit Hash function interface |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_hash32\_identity](group__hash__functions.md#ga3bc327796b6836648e5dcf7c46cf38fa) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | The naive identity hash function. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_hash32\_djb2](group__hash__functions.md#gaaf45db9467193fe9e9d597537dd41c5e) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | Daniel J. Bernstein's hash function. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_hash32\_murmur3](group__hash__functions.md#gad35726d71600a63f4c3ac0382d0a3981) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | Murmur3 hash function. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_hash32](group__hash__functions.md#gadd3f6fd78ce2c0bf10e1c82a9c50f39d) (const void \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n) |
|  | System default 32-bit hash function. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_function.h](hash__function_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
