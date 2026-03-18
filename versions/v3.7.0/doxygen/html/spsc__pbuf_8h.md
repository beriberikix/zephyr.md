---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/spsc__pbuf_8h.html
original_path: doxygen/html/spsc__pbuf_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spsc\_pbuf.h File Reference

`#include <[zephyr/cache.h](cache_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](spsc__pbuf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [spsc\_pbuf\_common](structspsc__pbuf__common.md) |
|  | First part of packet buffer control block. [More...](structspsc__pbuf__common.md#details) |
| struct | [spsc\_pbuf\_ext\_cache](structspsc__pbuf__ext__cache.md) |
|  | Remaining part of a packet buffer when cache is used. [More...](structspsc__pbuf__ext__cache.md#details) |
| struct | [spsc\_pbuf\_ext\_nocache](structspsc__pbuf__ext__nocache.md) |
|  | Remaining part of a packet buffer when cache is not used. [More...](structspsc__pbuf__ext__nocache.md#details) |
| struct | [spsc\_pbuf](structspsc__pbuf.md) |
|  | Single producer, single consumer packet buffer. [More...](structspsc__pbuf.md#details) |

| Macros | |
| --- | --- |
| #define | [SPSC\_PBUF\_CACHE](group__SPSC__PBUF__FLAGS.md#ga97255180be37860a513d0a87b3dac573)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag indicating that cache shall be handled. |
| #define | [SPSC\_PBUF\_UTILIZATION\_BITS](group__SPSC__PBUF__FLAGS.md#gaaaccc1ca6c802c2740b4af07ba1650b9)   24 |
|  | Size of the field which stores maximum utilization. |
| #define | [SPSC\_PBUF\_UTILIZATION\_OFFSET](group__SPSC__PBUF__FLAGS.md#ga5c1783e202a62161b6f5b0f11fb62f8a)   8 |
|  | Offset of the field which stores maximum utilization. |
| #define | [CONFIG\_SPSC\_PBUF\_REMOTE\_DCACHE\_LINE](group__spsc__buf.md#ga01f1a8120df7afe197f5ed9d1c667370)   0 |
| #define | [SPSC\_PBUF\_MAX\_LEN](group__spsc__buf.md#gaec777dd30be52c1773dcf9e9ec1f6f9d)   0xFF00 |
|  | Maximum packet length. |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [spsc\_pbuf\_capacity](group__spsc__buf.md#ga02955c21404d71ac3ceeb9aa82cb18af) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb) |
|  | Get buffer capacity. |
| struct [spsc\_pbuf](structspsc__pbuf.md) \* | [spsc\_pbuf\_init](group__spsc__buf.md#ga6db38d6a0200a2468db02815cfe3bb6e) (void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) blen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Initialize the packet buffer. |
| int | [spsc\_pbuf\_write](group__spsc__buf.md#ga492c895f1723567445ce23c73ed3d0ef) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, const char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Write specified amount of data to the packet buffer. |
| int | [spsc\_pbuf\_alloc](group__spsc__buf.md#ga44485fd6756810f56c6bf7d41b3b447c) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, char \*\*buf) |
|  | Allocate space in the packet buffer. |
| void | [spsc\_pbuf\_commit](group__spsc__buf.md#ga664da6f26fd99e7f1ce76828273408a0) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Commit packet to the buffer. |
| int | [spsc\_pbuf\_read](group__spsc__buf.md#ga24d4cc2a41fd2c42c6085e106bf71c0c) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Read specified amount of data from the packet buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [spsc\_pbuf\_claim](group__spsc__buf.md#ga6727d38e40a780f9116d5d7b1c0ae8c4) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, char \*\*buf) |
|  | Claim packet from the buffer. |
| void | [spsc\_pbuf\_free](group__spsc__buf.md#ga28ea4f10fcab4d04f9e831f2057822ca) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Free the packet to the buffer. |
| int | [spsc\_pbuf\_get\_utilization](group__spsc__buf.md#gae3f455db53147709d40a7a86406a9311) (struct [spsc\_pbuf](structspsc__pbuf.md) \*pb) |
|  | Get maximum utilization of the packet buffer. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [spsc\_pbuf.h](spsc__pbuf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
