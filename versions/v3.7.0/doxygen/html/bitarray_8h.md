---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bitarray_8h.html
original_path: doxygen/html/bitarray_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bitarray.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](bitarray_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_BITARRAY\_DEFINE](group__bitarray__apis.md#gabbe958c6b995023665651e4aa050aa62)(name, total\_bits) |
|  | Create a bitarray object. |
| #define | [SYS\_BITARRAY\_DEFINE\_STATIC](group__bitarray__apis.md#ga2c55680355b67fc25125299a35f604d1)(name, total\_bits) |
|  | Create a static bitarray object. |

| Typedefs | |
| --- | --- |
| typedef struct sys\_bitarray | [sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) |
|  | Bitarray structure. |

| Functions | |
| --- | --- |
| int | [sys\_bitarray\_set\_bit](group__bitarray__apis.md#ga5fe657e79fee3e111284e4184eb6b681) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit) |
|  | Set a bit in a bit array. |
| int | [sys\_bitarray\_clear\_bit](group__bitarray__apis.md#ga795e8bf81f5717addf523cec124cde4e) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit) |
|  | Clear a bit in a bit array. |
| int | [sys\_bitarray\_test\_bit](group__bitarray__apis.md#gae024ace00949fe8c565081e62818449d) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit, int \*val) |
|  | Test whether a bit is set or not. |
| int | [sys\_bitarray\_test\_and\_set\_bit](group__bitarray__apis.md#gad1761b9eae8a1d9302893ce5f8591923) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit, int \*prev\_val) |
|  | Test the bit and set it. |
| int | [sys\_bitarray\_test\_and\_clear\_bit](group__bitarray__apis.md#ga40fa4d37f1fb2da8789f70de50c599d5) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit, int \*prev\_val) |
|  | Test the bit and clear it. |
| int | [sys\_bitarray\_alloc](group__bitarray__apis.md#gac96766d9441a3b143aa386e2ac79ffd9) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*offset) |
|  | Allocate bits in a bit array. |
| int | [sys\_bitarray\_xor](group__bitarray__apis.md#ga195f100be66d9392c8a5e917ad9f8cea) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*dst, [sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*other, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Calculates the bit-wise XOR of two bitarrays in a region. |
| int | [sys\_bitarray\_find\_nth\_set](group__bitarray__apis.md#ga134b8b9cb37c69fc174ef0acc61075ec) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) n, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*found\_at) |
|  | Find nth bit set in region. |
| int | [sys\_bitarray\_popcount\_region](group__bitarray__apis.md#ga8dd6d35a082922b17c0efb7808f5e4be) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*count) |
|  | Count bits set in a bit array region. |
| int | [sys\_bitarray\_free](group__bitarray__apis.md#gaf9a2c34896d3b1866a5a60f78d4166b0) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Free bits in a bit array. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_bitarray\_is\_region\_set](group__bitarray__apis.md#ga2aa91a9be38b11e74dacbeb2fe5e6d6d) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Test if bits in a region is all set. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_bitarray\_is\_region\_cleared](group__bitarray__apis.md#ga21cd833e7118f188ca3e06f8cfd13a49) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Test if bits in a region is all cleared. |
| int | [sys\_bitarray\_set\_region](group__bitarray__apis.md#ga94d1a547b9fe0a01d73acf4a5c4f308b) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Set all bits in a region. |
| int | [sys\_bitarray\_test\_and\_set\_region](group__bitarray__apis.md#gad18590d2ab0bf251a59996620ed6e6bf) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) to\_set) |
|  | Test if all bits in a region are cleared/set and set/clear them in a single atomic operation. |
| int | [sys\_bitarray\_clear\_region](group__bitarray__apis.md#gad13bb2c37d0889807e026dbac6a2872d) ([sys\_bitarray\_t](group__bitarray__apis.md#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Clear all bits in a region. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [bitarray.h](bitarray_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
