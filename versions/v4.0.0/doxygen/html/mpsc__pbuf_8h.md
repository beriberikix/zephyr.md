---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mpsc__pbuf_8h.html
original_path: doxygen/html/mpsc__pbuf_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_pbuf.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/mpsc_packet.h](mpsc__packet_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](mpsc__pbuf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) |
|  | MPSC packet buffer structure. [More...](structmpsc__pbuf__buffer.md#details) |
| struct | [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) |
|  | MPSC packet buffer configuration. [More...](structmpsc__pbuf__buffer__config.md#details) |

| Macros | |
| --- | --- |
| #define | [MPSC\_PBUF\_SIZE\_POW2](group__MPSC__PBUF__FLAGS.md#ga6bed4eecb4eca06fb86a70c09505ccb8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag indicating that buffer size is power of 2. |
| #define | [MPSC\_PBUF\_MODE\_OVERWRITE](group__MPSC__PBUF__FLAGS.md#ga983332f7aff31ed7b7e62cacf7960497)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Flag indicating buffer full policy. |
| #define | [MPSC\_PBUF\_MAX\_UTILIZATION](group__MPSC__PBUF__FLAGS.md#gad0f57dbcecbb51a6b5b916c31a8eaab2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Flag indicating that maximum buffer usage is tracked. |
| #define | [MPSC\_PBUF\_FULL](group__MPSC__PBUF__FLAGS.md#ga71a287b22771128b80c23d9263677498)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Flag indicated that buffer is currently full. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [mpsc\_pbuf\_get\_wlen](group__mpsc__buf.md#ga00b0a1839bc466c623928a29921d76b8)) (const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
|  | Callback prototype for getting length of a packet. |
| typedef void(\* | [mpsc\_pbuf\_notify\_drop](group__mpsc__buf.md#ga87f3795770880fb552316a8cac7b85ae)) (const struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
|  | Callback called when packet is dropped. |

| Functions | |
| --- | --- |
| void | [mpsc\_pbuf\_init](group__mpsc__buf.md#ga5152b9ae9c0da98fde3f8b73afac52b8) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \*config) |
|  | Initialize a packet buffer. |
| union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | [mpsc\_pbuf\_alloc](group__mpsc__buf.md#ga398dd24464a5da03e80a3fc7d728dddd) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wlen, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate a packet. |
| void | [mpsc\_pbuf\_commit](group__mpsc__buf.md#gaa537b9e73ca4fda26a92dc56b960270e) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
|  | Commit a packet. |
| void | [mpsc\_pbuf\_put\_word](group__mpsc__buf.md#gabc366638ec262c7ec41b320f0dcc6a87) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) word) |
|  | Put single word packet into a buffer. |
| void | [mpsc\_pbuf\_put\_word\_ext](group__mpsc__buf.md#ga7f4df1864fad89ec9557b6f0e18c9589) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) word, const void \*data) |
|  | Put a packet consisting of a word and a pointer. |
| void | [mpsc\_pbuf\_put\_data](group__mpsc__buf.md#ga7b52261bac98a7a0c6bae2a838f23316) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) wlen) |
|  | Put a packet into a buffer. |
| const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | [mpsc\_pbuf\_claim](group__mpsc__buf.md#ga9642d07deca00bc25cea2ae253ec7d76) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer) |
|  | Claim the first pending packet. |
| void | [mpsc\_pbuf\_free](group__mpsc__buf.md#ga54f8705fa262a6cda75f1feecde5e57e) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*packet) |
|  | Free a packet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mpsc\_pbuf\_is\_pending](group__mpsc__buf.md#ga2c8ac7f489fba611a2bca25bb2bbb5fb) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer) |
|  | Check if there are any message pending. |
| void | [mpsc\_pbuf\_get\_utilization](group__mpsc__buf.md#ga73be0efc020500865cfa07c45494f4a5) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*now) |
|  | Get current memory utilization. |
| int | [mpsc\_pbuf\_get\_max\_utilization](group__mpsc__buf.md#ga8ee7fd071effaca18797862d423279d7) (struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max) |
|  | Get maximum memory utilization. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mpsc\_pbuf.h](mpsc__pbuf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
