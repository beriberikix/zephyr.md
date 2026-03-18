---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cache_8h.html
original_path: doxygen/html/cache_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cache.h File Reference

cache API interface
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/arch/cpu.h](cpu_8h_source.md)>`  
`#include <[zephyr/debug/sparse.h](sparse_8h_source.md)>`  
`#include <zephyr/syscalls/cache.h>`

[Go to the source code of this file.](cache_8h_source.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_cache\_data\_enable](group__cache__interface.md#ga8e065404f0d13a33f7b04096165b8776) (void) |
|  | Enable the d-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_cache\_data\_disable](group__cache__interface.md#ga7952019e9231e250a37a3226908102ee) (void) |
|  | Disable the d-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_cache\_instr\_enable](group__cache__interface.md#ga98bd00d87195cbf5f99cea4b68765a7f) (void) |
|  | Enable the i-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_cache\_instr\_disable](group__cache__interface.md#ga502377e711c5399926992e530456af60) (void) |
|  | Disable the i-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_data\_flush\_all](group__cache__interface.md#ga3992ceae117dbd8bd11a5392e8ab2aa3) (void) |
|  | Flush the d-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_flush\_all](group__cache__interface.md#ga6846744d9cdfe5d164679f12abe31e48) (void) |
|  | Flush the i-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_data\_invd\_all](group__cache__interface.md#ga9c7f8f6783196fc226e58d2da1b7781d) (void) |
|  | Invalidate the d-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_invd\_all](group__cache__interface.md#gadc460f782f2642203e1bd4797dd46308) (void) |
|  | Invalidate the i-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_data\_flush\_and\_invd\_all](group__cache__interface.md#gaa38ce02275c001f4c542c6d967be25ac) (void) |
|  | Flush and Invalidate the d-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_flush\_and\_invd\_all](group__cache__interface.md#ga3ac77afb61ae32cc0af7bd61e07cf765) (void) |
|  | Flush and Invalidate the i-cache. |
| int | [sys\_cache\_data\_flush\_range](group__cache__interface.md#ga6b61424f0aa81e2893c915b096de0cdb) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush an address range in the d-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_flush\_range](group__cache__interface.md#ga628ee038060351a9958067dfc2e3192c) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush an address range in the i-cache. |
| int | [sys\_cache\_data\_invd\_range](group__cache__interface.md#ga578f2f926cbf5ad196765881c8c1265e) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Invalidate an address range in the d-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_invd\_range](group__cache__interface.md#ga7cc3e53a18492b871b69af8b2d1d0db9) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Invalidate an address range in the i-cache. |
| int | [sys\_cache\_data\_flush\_and\_invd\_range](group__cache__interface.md#ga51d2bfa0ed0d139d1d299d14e8269eac) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush and Invalidate an address range in the d-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_cache\_instr\_flush\_and\_invd\_range](group__cache__interface.md#ga768ada6618e2b9ddc5ba3bb54ba48773) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flush and Invalidate an address range in the i-cache. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_cache\_data\_line\_size\_get](group__cache__interface.md#ga6b25a6076791c4a559aa20633b49b07e) (void) |
|  | Get the d-cache line size. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [sys\_cache\_instr\_line\_size\_get](group__cache__interface.md#ga4d130b1ef9a3ecfcd08c0eb2f474e5f1) (void) |
|  | Get the i-cache line size. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_cache\_is\_ptr\_cached](group__cache__interface.md#ga0d21da511beb423a64d9bb23e6b5dacf) (void \*ptr) |
|  | Test if a pointer is in cached region. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_cache\_is\_ptr\_uncached](group__cache__interface.md#gaa02f0bac4addff95dda539dca2b1d4d1) (void \*ptr) |
|  | Test if a pointer is in un-cached region. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* | [sys\_cache\_cached\_ptr\_get](group__cache__interface.md#ga773d9fef6f1a2d76927957e73e245ef5) (void \*ptr) |
|  | Return cached pointer to a RAM address. |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void \* | [sys\_cache\_uncached\_ptr\_get](group__cache__interface.md#ga1410d43a8c6d16e1b54a32868eaecfe3) (void \*ptr) |
|  | Return uncached pointer to a RAM address. |

## Detailed Description

cache API interface

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [cache.h](cache_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
