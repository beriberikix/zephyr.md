---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/memory-attr-riscv_8h.html
original_path: doxygen/html/memory-attr-riscv_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memory-attr-riscv.h File Reference

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/dt-bindings/memory-attr/memory-attr.h](memory-attr_8h_source.md)>`

[Go to the source code of this file.](memory-attr-riscv_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_MEM\_RISCV\_MASK](#a9a9ef79de1ef1c634e27dcec5a6ca8e3)   [DT\_MEM\_ARCH\_ATTR\_MASK](memory-attr_8h.md#aa180a5da02572a4fe600573e2521abbe) |
| #define | [DT\_MEM\_RISCV\_GET](#afea331be5ba6698753abd1a1a1d958eb)(x) |
| #define | [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)(x) |
| #define | [ATTR\_RISCV\_TYPE\_MAIN](#a326a99ea398a6972b5f6412a619b7729)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ATTR\_RISCV\_TYPE\_IO](#a7edefffaeae15842d748376348354e01)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ATTR\_RISCV\_TYPE\_EMPTY](#a4298e697fdee5155acc0dae339e8c7b0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [ATTR\_RISCV\_AMO\_SWAP](#a5b3078bb1a6db09697ca57f47c31f0d0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [ATTR\_RISCV\_AMO\_LOGICAL](#aed9286d69906a98892dd15602b747629)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [ATTR\_RISCV\_AMO\_ARITHMETIC](#af404c9544d1487688bf0a275c02cf80e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [ATTR\_RISCV\_IO\_IDEMPOTENT\_READ](#a2e51b151a96c55c5a4ab63a265a93161)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [ATTR\_RISCV\_IO\_IDEMPOTENT\_WRITE](#a9969de51c4a6ed2c6b332bf67b55820b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [DT\_MEM\_RISCV\_TYPE\_MAIN](#a4c67437419601ee8c81b9c34f39122c4)   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_TYPE\_MAIN](#a326a99ea398a6972b5f6412a619b7729)) |
| #define | [DT\_MEM\_RISCV\_TYPE\_IO](#a30903aee0dabbf6f15c8526834b11f11)   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_TYPE\_IO](#a7edefffaeae15842d748376348354e01)) |
| #define | [DT\_MEM\_RISCV\_TYPE\_EMPTY](#a938f9f8b108f8e1230726bf3cbadbe99)   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_TYPE\_EMPTY](#a4298e697fdee5155acc0dae339e8c7b0)) |
| #define | [DT\_MEM\_RISCV\_AMO\_SWAP](#afe6b3c00217e837092384b2baf36d613)   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_AMO\_SWAP](#a5b3078bb1a6db09697ca57f47c31f0d0)) |
| #define | [DT\_MEM\_RISCV\_AMO\_LOGICAL](#a1b28fc152f2c96c3236e2e4c37c8fbb2)   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_AMO\_LOGICAL](#aed9286d69906a98892dd15602b747629)) |
| #define | [DT\_MEM\_RISCV\_AMO\_ARITHMETIC](#adafec66eb70663372088154a2703012e)   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_AMO\_ARITHMETIC](#af404c9544d1487688bf0a275c02cf80e)) |
| #define | [DT\_MEM\_RISCV\_IO\_IDEMPOTENT\_READ](#a2be0609b3bc135633711554e840e512a)   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_IO\_IDEMPOTENT\_READ](#a2e51b151a96c55c5a4ab63a265a93161)) |
| #define | [DT\_MEM\_RISCV\_IO\_IDEMPOTENT\_WRITE](#a1b04dd65a2a5bf184b0965a352cba49f)   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_IO\_IDEMPOTENT\_WRITE](#a9969de51c4a6ed2c6b332bf67b55820b)) |
| #define | [DT\_MEM\_RISCV\_UNKNOWN](#ae008d2f860df3c52c9a02e97757f4168)   [DT\_MEM\_ARCH\_ATTR\_UNKNOWN](memory-attr_8h.md#aaefc7bf33d8fa6d5151338cd23b84474) |

## Macro Definition Documentation

## [◆ ](#af404c9544d1487688bf0a275c02cf80e)ATTR\_RISCV\_AMO\_ARITHMETIC

| #define ATTR\_RISCV\_AMO\_ARITHMETIC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#aed9286d69906a98892dd15602b747629)ATTR\_RISCV\_AMO\_LOGICAL

| #define ATTR\_RISCV\_AMO\_LOGICAL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a5b3078bb1a6db09697ca57f47c31f0d0)ATTR\_RISCV\_AMO\_SWAP

| #define ATTR\_RISCV\_AMO\_SWAP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a2e51b151a96c55c5a4ab63a265a93161)ATTR\_RISCV\_IO\_IDEMPOTENT\_READ

| #define ATTR\_RISCV\_IO\_IDEMPOTENT\_READ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a9969de51c4a6ed2c6b332bf67b55820b)ATTR\_RISCV\_IO\_IDEMPOTENT\_WRITE

| #define ATTR\_RISCV\_IO\_IDEMPOTENT\_WRITE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a4298e697fdee5155acc0dae339e8c7b0)ATTR\_RISCV\_TYPE\_EMPTY

| #define ATTR\_RISCV\_TYPE\_EMPTY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a7edefffaeae15842d748376348354e01)ATTR\_RISCV\_TYPE\_IO

| #define ATTR\_RISCV\_TYPE\_IO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a326a99ea398a6972b5f6412a619b7729)ATTR\_RISCV\_TYPE\_MAIN

| #define ATTR\_RISCV\_TYPE\_MAIN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a26562c62513dfb712404e3a636c6b7b2)DT\_MEM\_RISCV

| #define DT\_MEM\_RISCV | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) << [DT\_MEM\_ARCH\_ATTR\_SHIFT](memory-attr_8h.md#a06e4088178d1ec01ec5cafe289c8eebe))

[DT\_MEM\_ARCH\_ATTR\_SHIFT](memory-attr_8h.md#a06e4088178d1ec01ec5cafe289c8eebe)

#define DT\_MEM\_ARCH\_ATTR\_SHIFT

**Definition** memory-attr.h:48

## [◆ ](#adafec66eb70663372088154a2703012e)DT\_MEM\_RISCV\_AMO\_ARITHMETIC

| #define DT\_MEM\_RISCV\_AMO\_ARITHMETIC   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_AMO\_ARITHMETIC](#af404c9544d1487688bf0a275c02cf80e)) |
| --- |

## [◆ ](#a1b28fc152f2c96c3236e2e4c37c8fbb2)DT\_MEM\_RISCV\_AMO\_LOGICAL

| #define DT\_MEM\_RISCV\_AMO\_LOGICAL   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_AMO\_LOGICAL](#aed9286d69906a98892dd15602b747629)) |
| --- |

## [◆ ](#afe6b3c00217e837092384b2baf36d613)DT\_MEM\_RISCV\_AMO\_SWAP

| #define DT\_MEM\_RISCV\_AMO\_SWAP   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_AMO\_SWAP](#a5b3078bb1a6db09697ca57f47c31f0d0)) |
| --- |

## [◆ ](#afea331be5ba6698753abd1a1a1d958eb)DT\_MEM\_RISCV\_GET

| #define DT\_MEM\_RISCV\_GET | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x) & [DT\_MEM\_RISCV\_MASK](#a9a9ef79de1ef1c634e27dcec5a6ca8e3))

[DT\_MEM\_RISCV\_MASK](#a9a9ef79de1ef1c634e27dcec5a6ca8e3)

#define DT\_MEM\_RISCV\_MASK

**Definition** memory-attr-riscv.h:15

## [◆ ](#a2be0609b3bc135633711554e840e512a)DT\_MEM\_RISCV\_IO\_IDEMPOTENT\_READ

| #define DT\_MEM\_RISCV\_IO\_IDEMPOTENT\_READ   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_IO\_IDEMPOTENT\_READ](#a2e51b151a96c55c5a4ab63a265a93161)) |
| --- |

## [◆ ](#a1b04dd65a2a5bf184b0965a352cba49f)DT\_MEM\_RISCV\_IO\_IDEMPOTENT\_WRITE

| #define DT\_MEM\_RISCV\_IO\_IDEMPOTENT\_WRITE   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_IO\_IDEMPOTENT\_WRITE](#a9969de51c4a6ed2c6b332bf67b55820b)) |
| --- |

## [◆ ](#a9a9ef79de1ef1c634e27dcec5a6ca8e3)DT\_MEM\_RISCV\_MASK

| #define DT\_MEM\_RISCV\_MASK   [DT\_MEM\_ARCH\_ATTR\_MASK](memory-attr_8h.md#aa180a5da02572a4fe600573e2521abbe) |
| --- |

## [◆ ](#a938f9f8b108f8e1230726bf3cbadbe99)DT\_MEM\_RISCV\_TYPE\_EMPTY

| #define DT\_MEM\_RISCV\_TYPE\_EMPTY   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_TYPE\_EMPTY](#a4298e697fdee5155acc0dae339e8c7b0)) |
| --- |

## [◆ ](#a30903aee0dabbf6f15c8526834b11f11)DT\_MEM\_RISCV\_TYPE\_IO

| #define DT\_MEM\_RISCV\_TYPE\_IO   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_TYPE\_IO](#a7edefffaeae15842d748376348354e01)) |
| --- |

## [◆ ](#a4c67437419601ee8c81b9c34f39122c4)DT\_MEM\_RISCV\_TYPE\_MAIN

| #define DT\_MEM\_RISCV\_TYPE\_MAIN   [DT\_MEM\_RISCV](#a26562c62513dfb712404e3a636c6b7b2)([ATTR\_RISCV\_TYPE\_MAIN](#a326a99ea398a6972b5f6412a619b7729)) |
| --- |

## [◆ ](#ae008d2f860df3c52c9a02e97757f4168)DT\_MEM\_RISCV\_UNKNOWN

| #define DT\_MEM\_RISCV\_UNKNOWN   [DT\_MEM\_ARCH\_ATTR\_UNKNOWN](memory-attr_8h.md#aaefc7bf33d8fa6d5151338cd23b84474) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-attr](dir_505b2faf98fd683dcb4dcae28f4fc25d.md)
- [memory-attr-riscv.h](memory-attr-riscv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
