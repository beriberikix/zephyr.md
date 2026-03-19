---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ft8xx__common_8h.html
original_path: doxygen/html/ft8xx__common_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_common.h File Reference

FT8XX common functions.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](ft8xx__common_8h_source.md)

| Functions | |
| --- | --- |
| void | [ft8xx\_wr8](group__ft8xx__common.md#ga7623499f328d820b1e84d2a3834a89a2) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write 1 byte (8 bits) to FT8xx memory. |
| void | [ft8xx\_wr16](group__ft8xx__common.md#gadfbff24d8fb246081cefbc51190b32e5) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write 2 bytes (16 bits) to FT8xx memory. |
| void | [ft8xx\_wr32](group__ft8xx__common.md#ga3158d2c2605f66fc22bbf336d780b8bf) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write 4 bytes (32 bits) to FT8xx memory. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ft8xx\_rd8](group__ft8xx__common.md#gac7ed90cf4a51fc9139c49ce352a25385) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 1 byte (8 bits) from FT8xx memory. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ft8xx\_rd16](group__ft8xx__common.md#gad52c57f65516917792cb07f6d2f2bf71) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 2 bytes (16 bits) from FT8xx memory. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ft8xx\_rd32](group__ft8xx__common.md#ga9e78caa02181c65a5c5dac39438ca3e3) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 4 bytes (32 bits) from FT8xx memory. |

## Detailed Description

FT8XX common functions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_common.h](ft8xx__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
