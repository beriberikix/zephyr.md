---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fcb_8h.html
original_path: doxygen/html/fcb_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcb.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[limits.h](limits_8h_source.md)>`  
`#include <[zephyr/storage/flash_map.h](flash__map_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

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
| #define | [FCB\_MAX\_LEN](group__fcb__data__structures.md#gaccabb1cb7f83c0d8919571cf3de7ee47)   (0x3fffu) |
|  | Max length of element (16,383). |
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
| int | [fcb\_init](group__fcb__api.md#gab304f3e9e28f6229d7ddbe638eda2f70) (int f\_area\_id, struct [fcb](structfcb.md) \*fcbp) |
|  | Initialize FCB instance. |
| int | [fcb\_append](group__fcb__api.md#gad567d124d8b0fe181ed54cfbe33b315c) (struct [fcb](structfcb.md) \*fcbp, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, struct [fcb\_entry](structfcb__entry.md) \*loc) |
|  | Appends an entry to circular buffer. |
| int | [fcb\_append\_finish](group__fcb__api.md#gaae445e8376db192ce45fff9dcf95c954) (struct [fcb](structfcb.md) \*fcbp, struct [fcb\_entry](structfcb__entry.md) \*append\_loc) |
|  | Finishes entry append operation. |
| int | [fcb\_walk](group__fcb__api.md#gad50e579ec9430a23ef5525e74ceb21b2) (struct [fcb](structfcb.md) \*fcbp, struct [flash\_sector](structflash__sector.md) \*sector, [fcb\_walk\_cb](group__fcb__api.md#gaeed5144438ee00d83c9b3d3b4b7490ea) cb, void \*cb\_arg) |
|  | Walk over all entries in the FCB sector. |
| int | [fcb\_getnext](group__fcb__api.md#ga7908a252a09ebbb98b60a505220072bc) (struct [fcb](structfcb.md) \*fcbp, struct [fcb\_entry](structfcb__entry.md) \*loc) |
|  | Get next fcb entry location. |
| int | [fcb\_rotate](group__fcb__api.md#gad2fb288645e678dd6ea05b0871d5e774) (struct [fcb](structfcb.md) \*fcbp) |
|  | Rotate fcb sectors. |
| int | [fcb\_append\_to\_scratch](group__fcb__api.md#ga22b2bab8af3004c93e5d40659ccfec29) (struct [fcb](structfcb.md) \*fcbp) |
|  | Start using the scratch block. |
| int | [fcb\_free\_sector\_cnt](group__fcb__api.md#gaa9beaa3f5a6cc52b7e460d5670fdaabf) (struct [fcb](structfcb.md) \*fcbp) |
|  | Get free sector count. |
| int | [fcb\_is\_empty](group__fcb__api.md#gade8af12645d769ce3b27848976ada32a) (struct [fcb](structfcb.md) \*fcbp) |
|  | Check whether FCB has any data. |
| int | [fcb\_offset\_last\_n](group__fcb__api.md#gac15df95c0d9bed45c9da39802411598d) (struct [fcb](structfcb.md) \*fcbp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) entries, struct [fcb\_entry](structfcb__entry.md) \*last\_n\_entry) |
|  | Finds the fcb entry that gives back up to n entries at the end. |
| int | [fcb\_clear](group__fcb__api.md#gaab78da410b7e709854e29219eb02a0c9) (struct [fcb](structfcb.md) \*fcbp) |
|  | Clear fcb instance storage. |
| int | [fcb\_flash\_read](group__fcb__internal.md#ga0b921b509dab767661058d164e80f55e) (const struct [fcb](structfcb.md) \*fcbp, const struct [flash\_sector](structflash__sector.md) \*sector, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read raw data from the fcb flash sector. |
| int | [fcb\_flash\_write](group__fcb__internal.md#gafcfb9b6d4b5c0e593c0a9e512a0ec309) (const struct [fcb](structfcb.md) \*fcbp, const struct [flash\_sector](structflash__sector.md) \*sector, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write raw data to the fcb flash sector. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [fcb.h](fcb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
