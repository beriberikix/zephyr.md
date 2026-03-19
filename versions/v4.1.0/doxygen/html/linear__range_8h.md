---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/linear__range_8h.html
original_path: doxygen/html/linear__range_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

linear\_range.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdlib.h](stdlib_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](linear__range_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [linear\_range](structlinear__range.md) |
|  | Linear range. [More...](structlinear__range.md#details) |

| Macros | |
| --- | --- |
| #define | [LINEAR\_RANGE\_INIT](group__linear__range.md#ga3f936124e81ea46aa5f8dd4d9bde9ece)(\_min, \_step, \_min\_idx, \_max\_idx) |
|  | Initializer for [Linear Range](group__linear__range.md "Linear Range"). |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [linear\_range\_values\_count](group__linear__range.md#gae02547c7922e5a36c815dc89bc1df128) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Obtain the number of values representable in a linear range. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [linear\_range\_group\_values\_count](group__linear__range.md#ga67b24d9d6e7088daf39020c8c02f8d96) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) r\_cnt) |
|  | Obtain the number of values representable by a group of linear ranges. |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [linear\_range\_get\_max\_value](group__linear__range.md#gae6315858afa73945bc44d8c5c997645c) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)) |
|  | Obtain the maximum value representable by a linear range. |
| static int | [linear\_range\_get\_value](group__linear__range.md#ga72b800d1c6af44cb247130139176a59e) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*val) |
|  | Obtain value given a linear range index. |
| static int | [linear\_range\_group\_get\_value](group__linear__range.md#gac054f5cc2aad11de223fa968ebeaa55c) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) r\_cnt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) idx, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*val) |
|  | Obtain value in a group given a linear range index. |
| static int | [linear\_range\_get\_index](group__linear__range.md#ga90610e42e63eb4290e5ae6187a53143f) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx) |
|  | Obtain index given a value. |
| static int | [linear\_range\_group\_get\_index](group__linear__range.md#gab8b661f6ed1caba2ab4796a02c1b24a8) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) r\_cnt, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx) |
|  | Obtain index in a group given a value. |
| static int | [linear\_range\_get\_win\_index](group__linear__range.md#ga6c06a26d629f4d7a195188e7c5df5db1) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_min, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_max, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx) |
|  | Obtain index given a window of values. |
| static int | [linear\_range\_group\_get\_win\_index](group__linear__range.md#ga11dc5408be53887e9ddf992b574aa16c) (const struct [linear\_range](structlinear__range.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) r\_cnt, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_min, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) val\_max, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*idx) |
|  | Obtain index in a group given a value that must be within a window of values. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [linear\_range.h](linear__range_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
