---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sys_2barrier_8h.html
original_path: doxygen/html/sys_2barrier_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

barrier.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](sys_2barrier_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [barrier\_dmem\_fence\_full](group__barrier__apis.md#gab0dd6769236babde7cf48c32007edf31) (void) |
|  | Full/sequentially-consistent data memory barrier. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [barrier\_dsync\_fence\_full](group__barrier__apis.md#gaaa6909c1410bc371f59ad3eec21ee5ef) (void) |
|  | Full/sequentially-consistent data synchronization barrier. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [barrier\_isync\_fence\_full](group__barrier__apis.md#gaa916454a2ff58e50b2f51845447177ec) (void) |
|  | Full/sequentially-consistent instruction synchronization barrier. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [barrier.h](sys_2barrier_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
