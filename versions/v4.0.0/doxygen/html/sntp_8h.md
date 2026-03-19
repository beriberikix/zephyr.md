---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sntp_8h.html
original_path: doxygen/html/sntp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sntp.h File Reference

SNTP (Simple Network Time Protocol).
[More...](#details)

`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](sntp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sntp\_time](structsntp__time.md) |
|  | Time as returned by SNTP API, fractional seconds since 1 Jan 1970. [More...](structsntp__time.md#details) |
| struct | [sntp\_ctx](structsntp__ctx.md) |
|  | SNTP context. [More...](structsntp__ctx.md#details) |

| Functions | |
| --- | --- |
| int | [sntp\_init](group__sntp.md#ga945936e5164bbd959cfa666ceacdac13) (struct [sntp\_ctx](structsntp__ctx.md) \*ctx, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len) |
|  | Initialize SNTP context. |
| int | [sntp\_query](group__sntp.md#ga25ef46cc74be71bbe2f76de7c30cbe45) (struct [sntp\_ctx](structsntp__ctx.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts) |
|  | Perform SNTP query. |
| int | [sntp\_recv\_response](group__sntp.md#ga8771cdc6e64ab1489b333cc0c1731e9f) (struct [sntp\_ctx](structsntp__ctx.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts) |
|  | Attempt to receive an SNTP response after issuing a query. |
| void | [sntp\_close](group__sntp.md#ga0cff25edb11ae944dd24a234450a2f3d) (struct [sntp\_ctx](structsntp__ctx.md) \*ctx) |
|  | Release SNTP context. |
| int | [sntp\_simple](group__sntp.md#ga25c894db6d24a5e729b4edcb8917ce9c) (const char \*server, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts) |
|  | Convenience function to query SNTP in one-shot fashion. |
| int | [sntp\_simple\_addr](group__sntp.md#ga75aaee9a8f8490c0cc826a0e9298cd88) (struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addr\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout, struct [sntp\_time](structsntp__time.md) \*ts) |
|  | Convenience function to query SNTP in one-shot fashion using a pre-initialized address struct. |

## Detailed Description

SNTP (Simple Network Time Protocol).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [sntp.h](sntp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
