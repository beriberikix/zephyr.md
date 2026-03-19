---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hash_8h.html
original_path: doxygen/html/hash_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash.h File Reference

Crypto Hash APIs.
[More...](#details)

[Go to the source code of this file.](hash_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [hash\_ctx](structhash__ctx.md) |
|  | Structure encoding session parameters. [More...](structhash__ctx.md#details) |
| struct | [hash\_pkt](structhash__pkt.md) |
|  | Structure encoding IO parameters of a hash operation. [More...](structhash__pkt.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [hash\_op\_t](group__crypto__hash.md#ga955369c6da6aa70ded229d8861292070)) (struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) finish) |
| typedef void(\* | [hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd)) (struct [hash\_pkt](structhash__pkt.md) \*completed, int status) |

| Enumerations | |
| --- | --- |
| enum | [hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a) { [CRYPTO\_HASH\_ALGO\_SHA224](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aaa49fd348b98d55eca407ae88e3626265) = 1 , [CRYPTO\_HASH\_ALGO\_SHA256](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aa1b0b60a3270618fd492491668dc2ad43) = 2 , [CRYPTO\_HASH\_ALGO\_SHA384](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aabba9e518a333ce75825957fde1993dd5) = 3 , [CRYPTO\_HASH\_ALGO\_SHA512](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aa72a129765ae9e15f456c295c3917bf3f) = 4 } |
|  | Hash algorithm. [More...](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a) |

## Detailed Description

Crypto Hash APIs.

This file contains the Crypto Abstraction layer APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [crypto](dir_8e645738bb65aae54152153b1372b1b2.md)
- [hash.h](hash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
