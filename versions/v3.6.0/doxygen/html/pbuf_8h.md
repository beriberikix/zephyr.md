---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pbuf_8h.html
original_path: doxygen/html/pbuf_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pbuf.h File Reference

`#include <[zephyr/cache.h](cache_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](pbuf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pbuf\_cfg](structpbuf__cfg.md) |
|  | Control block of packet buffer. [More...](structpbuf__cfg.md#details) |
| struct | [pbuf\_data](structpbuf__data.md) |
|  | Data block of the packed buffer. [More...](structpbuf__data.md#details) |
| struct | [pbuf](structpbuf.md) |
|  | Scure packed buffer. [More...](structpbuf.md#details) |

| Macros | |
| --- | --- |
| #define | [PBUF\_PACKET\_LEN\_SZ](group__pbuf.md#gaa57dc50fdf97af6690ac784f0a4450be)   [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) |
|  | Size of packet length field. |
| #define | [PBUF\_CFG\_INIT](group__pbuf.md#gafc65e8f044930fbd51dd6178302d75e1)(mem\_addr, size, dcache\_align) |
|  | Macro for configuration initialization. |
| #define | [PBUF\_HEADER\_OVERHEAD](group__pbuf.md#ga00f201bb5e2e139272b2c32f9c3f6efc)(dcache\_align) |
|  | Macro calculates memory overhead taken by the header in shared memory. |
| #define | [PBUF\_DEFINE](group__pbuf.md#gafc988125a3c06d0ecdc948cab3a3d23a)(name, mem\_addr, size, dcache\_align) |
|  | Statically define and initialize pbuf. |

| Functions | |
| --- | --- |
| int | [pbuf\_init](group__pbuf.md#ga651cf4ad3dc69e5dc1a0cea9f06a084e) (struct [pbuf](structpbuf.md) \*pb) |
|  | Initialize the packet buffer. |
| int | [pbuf\_write](group__pbuf.md#ga9df9413dcd6268690a410c33126c081e) (struct [pbuf](structpbuf.md) \*pb, const char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Write specified amount of data to the packet buffer. |
| int | [pbuf\_read](group__pbuf.md#ga44cc22d33d4ec7b7c95459e96ef7d7d0) (struct [pbuf](structpbuf.md) \*pb, char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Read specified amount of data from the packet buffer. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [pbuf.h](pbuf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
