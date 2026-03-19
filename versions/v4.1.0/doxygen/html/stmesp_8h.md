---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stmesp_8h.html
original_path: doxygen/html/stmesp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stmesp.h File Reference

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](stmesp_8h_source.md)

| Functions | |
| --- | --- |
| static void | [stmesp\_flag](group__stmsp__interface.md#ga2ffcc08b7d5c32c90b5d24982c0f6349) (STMESP\_Type \*reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) guaranteed) |
|  | Write flag to STMESP. |
| static void | [stmesp\_data8](group__stmsp__interface.md#ga4af9486d77c93a55f221c7647d69a9f2) (STMESP\_Type \*reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) guaranteed) |
|  | Write 8 bit data to STMESP. |
| static void | [stmesp\_data16](group__stmsp__interface.md#gaef1918a9d15d8da34fb5f2d7a11ff5fd) (STMESP\_Type \*reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) guaranteed) |
|  | Write 16 bit data to STMESP. |
| static void | [stmesp\_data32](group__stmsp__interface.md#gaa7885c5a7620e46a532dbf405bfc6034) (STMESP\_Type \*reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) guaranteed) |
|  | Write 32 bit data to STMESP. |
| static int | [stmesp\_get\_port](group__stmsp__interface.md#ga4350f5d201e3591221a932aa9fc3e94d) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx, STMESP\_Type \*\*port) |
|  | Return address of a STM extended stimulus port. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [coresight](dir_027ea40c83108e8cf62d53228a00b8a9.md)
- [stmesp.h](stmesp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
