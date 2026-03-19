---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/base64_8h.html
original_path: doxygen/html/base64_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

base64.h File Reference

`#include <stddef.h>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](base64_8h_source.md)

| Functions | |
| --- | --- |
| int | [base64\_encode](group__base64.md#gaaff09edf41470c26d5a54d18c4f91ba0) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dlen, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*olen, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) slen) |
|  | Encode a buffer into base64 format. |
| int | [base64\_decode](group__base64.md#ga9e84f3adc54120fb1f1ccffb1bac8c5c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dlen, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*olen, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) slen) |
|  | Decode a base64-formatted buffer. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [base64.h](base64_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
