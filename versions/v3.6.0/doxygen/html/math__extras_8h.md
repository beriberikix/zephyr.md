---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/math__extras_8h.html
original_path: doxygen/html/math__extras_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

math\_extras.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/math_extras_impl.h](math__extras__impl_8h_source.md)>`

[Go to the source code of this file.](math__extras_8h_source.md)

| Functions | |
| --- | --- |
| Unsigned integer addition with overflow detection. | |
| These functions compute a + b and store the result in \*result, returning true if the operation overflowed. | |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u16\_add\_overflow](group__math__extras.md#ga62d018abdf97551665cab7486b5a519a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result) |
|  | Add two unsigned 16-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u32\_add\_overflow](group__math__extras.md#ga3f36aa272f5595d78c6e8219b2c4dbfb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Add two unsigned 32-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u64\_add\_overflow](group__math__extras.md#gaf98ec1d8b1c00e30382eed01853e3307) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result) |
|  | Add two unsigned 64-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [size\_add\_overflow](group__math__extras.md#ga7aaec179564038b540aaf4ab3c9a666d) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) a, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) b, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result) |
|  | Add two size\_t integers. |
| Unsigned integer multiplication with overflow detection. | |
| These functions compute a \* b and store the result in \*result, returning true if the operation overflowed. | |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u16\_mul\_overflow](group__math__extras.md#ga292df7083a9da5525cda13e2546e81ba) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) a, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) b, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result) |
|  | Multiply two unsigned 16-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u32\_mul\_overflow](group__math__extras.md#ga427e8cd4fcafab244576994acc9b960f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) a, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) b, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Multiply two unsigned 32-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [u64\_mul\_overflow](group__math__extras.md#ga366f6606874071677bf9079647d9abce) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) a, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) b, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*result) |
|  | Multiply two unsigned 64-bit integers. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [size\_mul\_overflow](group__math__extras.md#ga790b24a5d239afcc08d9e4f66c25ea56) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) a, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) b, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*result) |
|  | Multiply two size\_t integers. |
| Count leading zeros. | |
| Count the number of leading zero bits in the bitwise representation of x.  When x = 0, this is the size of x in bits. | |
| static int | [u32\_count\_leading\_zeros](group__math__extras.md#ga97e8d8a40a45899ab7e5ce718342536b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x) |
|  | Count the number of leading zero bits in a 32-bit integer. |
| static int | [u64\_count\_leading\_zeros](group__math__extras.md#gaf5f31e98f2f675a0b4cc54b7fba6f56c) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x) |
|  | Count the number of leading zero bits in a 64-bit integer. |
| Count trailing zeros. | |
| Count the number of trailing zero bits in the bitwise representation of x.  When x = 0, this is the size of x in bits. | |
| static int | [u32\_count\_trailing\_zeros](group__math__extras.md#ga4cb313f98c3fd3b00d6f4db74a9a0076) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x) |
|  | Count the number of trailing zero bits in a 32-bit integer. |
| static int | [u64\_count\_trailing\_zeros](group__math__extras.md#ga300356629c0388d37958ef026180ea4d) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) x) |
|  | Count the number of trailing zero bits in a 64-bit integer. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [math\_extras.h](math__extras_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
