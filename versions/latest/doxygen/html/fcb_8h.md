---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fcb_8h.html
original_path: doxygen/html/fcb_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcb.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[limits.h](limits_8h_source.md)>`  
`#include <[zephyr/storage/flash_map.h](flash__map_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`

[Go to the source code of this file.](fcb_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fcb\_entry](structfcb__entry.md) |
|  | FCB entry info structure. [More...](structfcb__entry.md#details) |
| struct | [fcb\_entry\_ctx](structfcb__entry__ctx.md) |
|  | Structure for transferring complete information about FCB entry location within flash memory. [More...](structfcb__entry__ctx.md#details) |
| struct | [fcb](structfcb.md) |
|  | FCB instance structure. [More...](structfcb.md#details) |

| Macros | |
| --- | --- |
| #define | [FCB\_MAX\_LEN](group__fcb__data__structures.md#gaccabb1cb7f83c0d8919571cf3de7ee47)   ([CHAR\_MAX](limits_8h.md#a778eefd6535a9d4b752fca5dd0af58db) | [CHAR\_MAX](limits_8h.md#a778eefd6535a9d4b752fca5dd0af58db) << 7) |
|  | Max length of element. |
| #define | [FCB\_ENTRY\_FA\_DATA\_OFF](group__fcb__data__structures.md#ga9b47a1aa59039995107c8e23dfacf43f)(entry) |
|  | Helper macro for calculating the data offset related to the fcb [flash\_area](structflash__area.md "Flash partition.") start offset. |
| #define | [FCB\_FLAGS\_CRC\_DISABLED](group__fcb__data__structures.md#ga2fc8801bea1d91a422aa622bcf4cb6e0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag to disable CRC for the fcb\_entries in flash. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea)) (struct [fcb\_entry\_ctx](structfcb__entry__ctx.md) \*loc\_ctx, void \*arg) |
|  | FCB Walk callback function type. |

| Functions | |
| --- | --- |
| int | [fcb\_init](group__fcb__api.md#ga318d35b6f023bb4079aaf76c01a59b96) (int f\_area\_id, struct [fcb](structfcb.md) \*[fcb](structfcb.md)) |
|  | Initialize FCB instance. |
| int | [fcb\_append](group__fcb__api.md#ga46a06d5c3bf945ba807b6960a354d744) (struct [fcb](structfcb.md) \*[fcb](structfcb.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, struct [fcb\_entry](structfcb__entry.md) \*loc) |
|  | Appends an entry to circular buffer. |
| int | [fcb\_append\_finish](group__fcb__api.md#ga2d8581e0784546fd73e4cd2f8baeebd9) (struct [fcb](structfcb.md) \*[fcb](structfcb.md), struct [fcb\_entry](structfcb__entry.md) \*append\_loc) |
|  | Finishes entry append operation. |
| int | [fcb\_walk](group__fcb__api.md#ga2e22f120b3f1d729f8e861f0c0e448fb) (struct [fcb](structfcb.md) \*[fcb](structfcb.md), struct [flash\_sector](structflash__sector.md) \*sector, [fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea) cb, void \*cb\_arg) |
|  | Walk over all entries in the FCB sector. |
| int | [fcb\_getnext](group__fcb__api.md#gaeeeb1d66ebc6dcefde1e07c3d8bdf4bc) (struct [fcb](structfcb.md) \*[fcb](structfcb.md), struct [fcb\_entry](structfcb__entry.md) \*loc) |
|  | Get next fcb entry location. |
| int | [fcb\_rotate](group__fcb__api.md#gab749a92fa5890a35996c27f9f2b8f98f) (struct [fcb](structfcb.md) \*[fcb](structfcb.md)) |
|  | Rotate fcb sectors. |
| int | [fcb\_append\_to\_scratch](group__fcb__api.md#gaf26d681ddea9b22d06122184b5a09566) (struct [fcb](structfcb.md) \*[fcb](structfcb.md)) |
|  | Start using the scratch block. |
| int | [fcb\_free\_sector\_cnt](group__fcb__api.md#ga2dec5f90b687466997eb25be43448daa) (struct [fcb](structfcb.md) \*[fcb](structfcb.md)) |
|  | Get free sector count. |
| int | [fcb\_is\_empty](group__fcb__api.md#ga76d29d337d5e457f065ed897297ba6cb) (struct [fcb](structfcb.md) \*[fcb](structfcb.md)) |
|  | Check whether FCB has any data. |
| int | [fcb\_offset\_last\_n](group__fcb__api.md#gacf4b86d660b7f3a3b73477defd86590c) (struct [fcb](structfcb.md) \*[fcb](structfcb.md), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) entries, struct [fcb\_entry](structfcb__entry.md) \*last\_n\_entry) |
|  | Finds the fcb entry that gives back up to n entries at the end. |
| int | [fcb\_clear](group__fcb__api.md#gab3d5c09980af72f0de1692682c8dfef1) (struct [fcb](structfcb.md) \*[fcb](structfcb.md)) |
|  | Clear fcb instance storage. |
| int | [fcb\_flash\_read](group__fcb__internal.md#ga85e3a7fcd92a029b16f7aebdfd7fd546) (const struct [fcb](structfcb.md) \*[fcb](structfcb.md), const struct [flash\_sector](structflash__sector.md) \*sector, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read raw data from the fcb flash sector. |
| int | [fcb\_flash\_write](group__fcb__internal.md#ga181d43e24799940105185fef9436ce8d) (const struct [fcb](structfcb.md) \*[fcb](structfcb.md), const struct [flash\_sector](structflash__sector.md) \*sector, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write raw data to the fcb flash sector. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [fcb.h](fcb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
