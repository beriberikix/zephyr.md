---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cs__trace__defmt_8h.html
original_path: doxygen/html/cs__trace__defmt_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cs\_trace\_defmt.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](cs__trace__defmt_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CORESIGHT\_TRACE\_FRAME\_SIZE32](group__cs__trace__defmt.md#gabecbf043f9f0888a0b60d2784aff55e3)   4 |
|  | Size of trace deformatter frame size in 32 bit words. |
| #define | [CORESIGHT\_TRACE\_FRAME\_SIZE](group__cs__trace__defmt.md#ga7a31378ad5570f930cab4227a018d80d)   ([CORESIGHT\_TRACE\_FRAME\_SIZE32](group__cs__trace__defmt.md#gabecbf043f9f0888a0b60d2784aff55e3) \* [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) |
|  | Size of trace deformatter frame size in bytes. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [cs\_trace\_defmt\_cb](group__cs__trace__defmt.md#gaccc05f92bfbc04b787f6f959e954115d)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Callback signature. |

| Functions | |
| --- | --- |
| int | [cs\_trace\_defmt\_init](group__cs__trace__defmt.md#gaaeaaefe2221161691144d82c932196ca) ([cs\_trace\_defmt\_cb](group__cs__trace__defmt.md#gaccc05f92bfbc04b787f6f959e954115d) cb) |
|  | Initialize Coresight Trace Deformatter. |
| int | [cs\_trace\_defmt\_process](group__cs__trace__defmt.md#ga109bab752da74692779aa3eb96b771ba) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Decode data from the stream. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [coresight](dir_9e253c82b70fbbc4699540bacc17d458.md)
- [cs\_trace\_defmt.h](cs__trace__defmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
