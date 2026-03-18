---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/demand__paging_8h.html
original_path: doxygen/html/demand__paging_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

demand\_paging.h File Reference

`#include <[zephyr/kernel/mm.h](kernel_2mm_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <zephyr/syscalls/demand_paging.h>`

[Go to the source code of this file.](demand__paging_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) |
|  | Paging Statistics. [More...](structk__mem__paging__stats__t.md#details) |
| struct | [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) |
|  | Paging Statistics Histograms. [More...](structk__mem__paging__histogram__t.md#details) |

| Functions | |
| --- | --- |
| int | [k\_mem\_page\_out](group__mem-demand-paging.md#ga0b18037209b4d8b5964bd9a1d760f703) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Evict a page-aligned virtual memory region to the backing store. |
| void | [k\_mem\_page\_in](group__mem-demand-paging.md#gab36c36a4e230677d2090514f7a34b408) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Load a virtual data region into memory. |
| void | [k\_mem\_pin](group__mem-demand-paging.md#ga5f2d422edde7d366e81a870ce057589f) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Pin an aligned virtual data region, paging in as necessary. |
| void | [k\_mem\_unpin](group__mem-demand-paging.md#ga3278aae5e24733c722b7d83c4b17dab3) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Un-pin an aligned virtual data region. |
| void | [k\_mem\_paging\_stats\_get](group__mem-demand-paging.md#ga52ad88e0c0eed2aa27331bfd4707b7ec) (struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) \*stats) |
|  | Get the paging statistics since system startup. |
| void | [k\_mem\_paging\_thread\_stats\_get](group__mem-demand-paging.md#gafad6b39cb2faf3bb416cd4d3faaa8d8c) (struct [k\_thread](structk__thread.md) \*thread, struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) \*stats) |
|  | Get the paging statistics since system startup for a thread. |
| void | [k\_mem\_paging\_histogram\_eviction\_get](group__mem-demand-paging.md#gaec64d019d819b00c7bc3804aac269199) (struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist) |
|  | Get the eviction timing histogram. |
| void | [k\_mem\_paging\_histogram\_backing\_store\_page\_in\_get](group__mem-demand-paging.md#ga1da0a643e8f85f98e29288e441a37dfa) (struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist) |
|  | Get the backing store page-in timing histogram. |
| void | [k\_mem\_paging\_histogram\_backing\_store\_page\_out\_get](group__mem-demand-paging.md#gae4f80d14f88a46ddb9aeb7afba861864) (struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist) |
|  | Get the backing store page-out timing histogram. |
| void | [k\_mem\_paging\_eviction\_add](group__mem-demand-paging-eviction.md#ga6bb19be3098cc839ae3f6e9528598867) (struct k\_mem\_page\_frame \*pf) |
|  | Submit a page frame for eviction candidate tracking. |
| void | [k\_mem\_paging\_eviction\_remove](group__mem-demand-paging-eviction.md#ga16a4df904cc7a9641d06741ed589949d) (struct k\_mem\_page\_frame \*pf) |
|  | Remove a page frame from potential eviction candidates. |
| void | [k\_mem\_paging\_eviction\_accessed](group__mem-demand-paging-eviction.md#ga228747c10bfd8816aec59fddf0e3a224) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys) |
|  | Process a page frame as being newly accessed. |
| struct k\_mem\_page\_frame \* | [k\_mem\_paging\_eviction\_select](group__mem-demand-paging-eviction.md#gaadbb4eb56c239f800daf995e6673ae1d) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*dirty) |
|  | Select a page frame for eviction. |
| void | [k\_mem\_paging\_eviction\_init](group__mem-demand-paging-eviction.md#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4) (void) |
|  | Initialization function. |
| int | [k\_mem\_paging\_backing\_store\_location\_get](group__mem-demand-paging-backing-store.md#ga1192487fdc8d63c025de42162fb204cd) (struct k\_mem\_page\_frame \*pf, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) page\_fault) |
|  | Reserve or fetch a storage location for a data page loaded into a page frame. |
| void | [k\_mem\_paging\_backing\_store\_location\_free](group__mem-demand-paging-backing-store.md#ga6ad421ad5671d9df3d96e03361f672e8) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Free a backing store location. |
| void | [k\_mem\_paging\_backing\_store\_page\_out](group__mem-demand-paging-backing-store.md#ga51f663e0a8c31367082e78097359af6d) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Copy a data page from K\_MEM\_SCRATCH\_PAGE to the specified location. |
| void | [k\_mem\_paging\_backing\_store\_page\_in](group__mem-demand-paging-backing-store.md#ga9becb4908cc7840ece93a2360692962d) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Copy a data page from the provided location to K\_MEM\_SCRATCH\_PAGE. |
| void | [k\_mem\_paging\_backing\_store\_page\_finalize](group__mem-demand-paging-backing-store.md#ga8d4bd3ea311fd873413d0477e8deb464) (struct k\_mem\_page\_frame \*pf, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location) |
|  | Update internal accounting after a page-in. |
| void | [k\_mem\_paging\_backing\_store\_init](group__mem-demand-paging-backing-store.md#ga7ff441f23619b2678bfb72559d5bd592) (void) |
|  | Backing store initialization function. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [mm](dir_29d573030f160bf8332fbdce7db88bc8.md)
- [demand\_paging.h](demand__paging_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
