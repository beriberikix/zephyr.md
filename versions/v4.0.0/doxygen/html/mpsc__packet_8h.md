---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mpsc__packet_8h.html
original_path: doxygen/html/mpsc__packet_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_packet.h File Reference

`#include <[string.h](string_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](mpsc__packet_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mpsc\_pbuf\_hdr](structmpsc__pbuf__hdr.md) |
|  | Generic packet header. [More...](structmpsc__pbuf__hdr.md#details) |
| struct | [mpsc\_pbuf\_skip](structmpsc__pbuf__skip.md) |
|  | Skip packet used internally by the packet buffer. [More...](structmpsc__pbuf__skip.md#details) |
| union | [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) |
|  | Generic packet header. [More...](unionmpsc__pbuf__generic.md#details) |

| Macros | |
| --- | --- |
| #define | [MPSC\_PBUF\_HDR\_BITS](group__mpsc__packet.md#gadb02a97032e41897ae6644a23d163849)   2 |
|  | Number of bits in the first word which are used by the buffer. |
| #define | [MPSC\_PBUF\_HDR](group__mpsc__packet.md#ga643932633f40ecdcfb9120662221d828) |
|  | Header that must be added to the first word in each packet. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mpsc\_packet.h](mpsc__packet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
