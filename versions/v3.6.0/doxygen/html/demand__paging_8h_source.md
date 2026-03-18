---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/demand__paging_8h_source.html
original_path: doxygen/html/demand__paging_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

demand\_paging.h

[Go to the documentation of this file.](demand__paging_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_KERNEL\_MM\_DEMAND\_PAGING\_H

8#define ZEPHYR\_INCLUDE\_KERNEL\_MM\_DEMAND\_PAGING\_H

9

10#include <[zephyr/kernel/mm.h](kernel_2mm_8h.md)>

11

12#include <[zephyr/sys/util.h](util_8h.md)>

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14

19

25

26#ifndef \_ASMLANGUAGE

27#include <[stdint.h](stdint_8h.md)>

28#include <stddef.h>

29#include <[inttypes.h](inttypes_8h.md)>

30#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

31

[ 35](structk__mem__paging__stats__t.md)struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) {

36#if defined(CONFIG\_DEMAND\_PAGING\_STATS) || defined(\_\_DOXYGEN\_\_)

37 struct {

[ 39](structk__mem__paging__stats__t.md#a3daad63e37d200f44d88c3d4e49f361a) unsigned long [cnt](structk__mem__paging__stats__t.md#a3daad63e37d200f44d88c3d4e49f361a);

40

[ 42](structk__mem__paging__stats__t.md#aa762731df50fc81d08beb3628f9dbd71) unsigned long [irq\_locked](structk__mem__paging__stats__t.md#aa762731df50fc81d08beb3628f9dbd71);

43

[ 45](structk__mem__paging__stats__t.md#a2c2183c1679ae158bdd232fa1fdeb250) unsigned long [irq\_unlocked](structk__mem__paging__stats__t.md#a2c2183c1679ae158bdd232fa1fdeb250);

46

47#if !defined(CONFIG\_DEMAND\_PAGING\_ALLOW\_IRQ) || defined(\_\_DOXYGEN\_\_)

[ 49](structk__mem__paging__stats__t.md#a210c83357c14a06fbd69b0cf2263fbb6) unsigned long [in\_isr](structk__mem__paging__stats__t.md#a210c83357c14a06fbd69b0cf2263fbb6);

50#endif

[ 51](structk__mem__paging__stats__t.md#af6331dae30074d48396151b33ac7a0a7) } [pagefaults](structk__mem__paging__stats__t.md#af6331dae30074d48396151b33ac7a0a7);

52

53 struct {

[ 55](structk__mem__paging__stats__t.md#a7b421897b3125d1a44284ca964ef1f66) unsigned long [clean](structk__mem__paging__stats__t.md#a7b421897b3125d1a44284ca964ef1f66);

56

[ 58](structk__mem__paging__stats__t.md#a4f8523c0e78c8de1e2443a194e875609) unsigned long [dirty](structk__mem__paging__stats__t.md#a4f8523c0e78c8de1e2443a194e875609);

[ 59](structk__mem__paging__stats__t.md#aa8175953fd7fa0a5057069b73b930f3b) } [eviction](structk__mem__paging__stats__t.md#aa8175953fd7fa0a5057069b73b930f3b);

60#endif /\* CONFIG\_DEMAND\_PAGING\_STATS \*/

61};

62

[ 66](structk__mem__paging__histogram__t.md)struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) {

67#if defined(CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM) || defined(\_\_DOXYGEN\_\_)

68 /\* Counts for each bin in timing histogram \*/

[ 69](structk__mem__paging__histogram__t.md#a4421676cbc9f6c63808ee914e2ff8c90) unsigned long [counts](structk__mem__paging__histogram__t.md#a4421676cbc9f6c63808ee914e2ff8c90)[CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM\_NUM\_BINS];

70

71 /\* Bounds for the bins in timing histogram,

72 \* excluding the first and last (hence, NUM\_SLOTS - 1).

73 \*/

[ 74](structk__mem__paging__histogram__t.md#a893236502aeb56975263b27cf4f2755a) unsigned long [bounds](structk__mem__paging__histogram__t.md#a893236502aeb56975263b27cf4f2755a)[CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM\_NUM\_BINS];

75#endif /\* CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM \*/

76};

77

78#ifdef \_\_cplusplus

79extern "C" {

80#endif

81

[ 105](group__mem-demand-paging.md#ga0b18037209b4d8b5964bd9a1d760f703)int [k\_mem\_page\_out](group__mem-demand-paging.md#ga0b18037209b4d8b5964bd9a1d760f703)(void \*addr, size\_t size);

106

[ 120](group__mem-demand-paging.md#gab36c36a4e230677d2090514f7a34b408)void [k\_mem\_page\_in](group__mem-demand-paging.md#gab36c36a4e230677d2090514f7a34b408)(void \*addr, size\_t size);

121

[ 135](group__mem-demand-paging.md#ga5f2d422edde7d366e81a870ce057589f)void [k\_mem\_pin](group__mem-demand-paging.md#ga5f2d422edde7d366e81a870ce057589f)(void \*addr, size\_t size);

136

[ 147](group__mem-demand-paging.md#ga3278aae5e24733c722b7d83c4b17dab3)void [k\_mem\_unpin](group__mem-demand-paging.md#ga3278aae5e24733c722b7d83c4b17dab3)(void \*addr, size\_t size);

148

[ 157](group__mem-demand-paging.md#ga52ad88e0c0eed2aa27331bfd4707b7ec)\_\_syscall void [k\_mem\_paging\_stats\_get](group__mem-demand-paging.md#ga52ad88e0c0eed2aa27331bfd4707b7ec)(struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) \*stats);

158

159struct [k\_thread](structk__thread.md);

169\_\_syscall

[ 170](group__mem-demand-paging.md#gafad6b39cb2faf3bb416cd4d3faaa8d8c)void [k\_mem\_paging\_thread\_stats\_get](group__mem-demand-paging.md#gafad6b39cb2faf3bb416cd4d3faaa8d8c)(struct [k\_thread](structk__thread.md) \*thread,

171 struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) \*stats);

172

[ 181](group__mem-demand-paging.md#gaec64d019d819b00c7bc3804aac269199)\_\_syscall void [k\_mem\_paging\_histogram\_eviction\_get](group__mem-demand-paging.md#gaec64d019d819b00c7bc3804aac269199)(

182 struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist);

183

[ 192](group__mem-demand-paging.md#ga1da0a643e8f85f98e29288e441a37dfa)\_\_syscall void [k\_mem\_paging\_histogram\_backing\_store\_page\_in\_get](group__mem-demand-paging.md#ga1da0a643e8f85f98e29288e441a37dfa)(

193 struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist);

194

[ 203](group__mem-demand-paging.md#gae4f80d14f88a46ddb9aeb7afba861864)\_\_syscall void [k\_mem\_paging\_histogram\_backing\_store\_page\_out\_get](group__mem-demand-paging.md#gae4f80d14f88a46ddb9aeb7afba861864)(

204 struct [k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md) \*hist);

205

206#include <syscalls/demand\_paging.h>

207

209

217

[ 232](group__mem-demand-paging-eviction.md#ga12641d53942529c7d7364c08473a6eca)struct z\_page\_frame \*[k\_mem\_paging\_eviction\_select](group__mem-demand-paging-eviction.md#ga12641d53942529c7d7364c08473a6eca)(bool \*dirty);

233

[ 241](group__mem-demand-paging-eviction.md#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)void [k\_mem\_paging\_eviction\_init](group__mem-demand-paging-eviction.md#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)(void);

242

244

252

[ 288](group__mem-demand-paging-backing-store.md#gaadedcda81ca04a2044332a8f6787967a)int [k\_mem\_paging\_backing\_store\_location\_get](group__mem-demand-paging-backing-store.md#gaadedcda81ca04a2044332a8f6787967a)(struct z\_page\_frame \*pf,

289 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*location,

290 bool page\_fault);

291

[ 302](group__mem-demand-paging-backing-store.md#ga6ad421ad5671d9df3d96e03361f672e8)void [k\_mem\_paging\_backing\_store\_location\_free](group__mem-demand-paging-backing-store.md#ga6ad421ad5671d9df3d96e03361f672e8)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location);

303

[ 315](group__mem-demand-paging-backing-store.md#ga51f663e0a8c31367082e78097359af6d)void [k\_mem\_paging\_backing\_store\_page\_out](group__mem-demand-paging-backing-store.md#ga51f663e0a8c31367082e78097359af6d)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location);

316

[ 328](group__mem-demand-paging-backing-store.md#ga9becb4908cc7840ece93a2360692962d)void [k\_mem\_paging\_backing\_store\_page\_in](group__mem-demand-paging-backing-store.md#ga9becb4908cc7840ece93a2360692962d)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location);

329

[ 350](group__mem-demand-paging-backing-store.md#ga0902bc03fecfe8c7b51eb1f3efe587b7)void [k\_mem\_paging\_backing\_store\_page\_finalize](group__mem-demand-paging-backing-store.md#ga0902bc03fecfe8c7b51eb1f3efe587b7)(struct z\_page\_frame \*pf,

351 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) location);

352

[ 366](group__mem-demand-paging-backing-store.md#ga7ff441f23619b2678bfb72559d5bd592)void [k\_mem\_paging\_backing\_store\_init](group__mem-demand-paging-backing-store.md#ga7ff441f23619b2678bfb72559d5bd592)(void);

367

369

370#ifdef \_\_cplusplus

371}

372#endif

373

374#endif /\* !\_ASMLANGUAGE \*/

375#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_MM\_DEMAND\_PAGING\_H \*/

[\_\_assert.h](____assert_8h.md)

[k\_mem\_paging\_backing\_store\_page\_finalize](group__mem-demand-paging-backing-store.md#ga0902bc03fecfe8c7b51eb1f3efe587b7)

void k\_mem\_paging\_backing\_store\_page\_finalize(struct z\_page\_frame \*pf, uintptr\_t location)

Update internal accounting after a page-in.

[k\_mem\_paging\_backing\_store\_page\_out](group__mem-demand-paging-backing-store.md#ga51f663e0a8c31367082e78097359af6d)

void k\_mem\_paging\_backing\_store\_page\_out(uintptr\_t location)

Copy a data page from Z\_SCRATCH\_PAGE to the specified location.

[k\_mem\_paging\_backing\_store\_location\_free](group__mem-demand-paging-backing-store.md#ga6ad421ad5671d9df3d96e03361f672e8)

void k\_mem\_paging\_backing\_store\_location\_free(uintptr\_t location)

Free a backing store location.

[k\_mem\_paging\_backing\_store\_init](group__mem-demand-paging-backing-store.md#ga7ff441f23619b2678bfb72559d5bd592)

void k\_mem\_paging\_backing\_store\_init(void)

Backing store initialization function.

[k\_mem\_paging\_backing\_store\_page\_in](group__mem-demand-paging-backing-store.md#ga9becb4908cc7840ece93a2360692962d)

void k\_mem\_paging\_backing\_store\_page\_in(uintptr\_t location)

Copy a data page from the provided location to Z\_SCRATCH\_PAGE.

[k\_mem\_paging\_backing\_store\_location\_get](group__mem-demand-paging-backing-store.md#gaadedcda81ca04a2044332a8f6787967a)

int k\_mem\_paging\_backing\_store\_location\_get(struct z\_page\_frame \*pf, uintptr\_t \*location, bool page\_fault)

Reserve or fetch a storage location for a data page loaded into a page frame.

[k\_mem\_paging\_eviction\_select](group__mem-demand-paging-eviction.md#ga12641d53942529c7d7364c08473a6eca)

struct z\_page\_frame \* k\_mem\_paging\_eviction\_select(bool \*dirty)

Select a page frame for eviction.

[k\_mem\_paging\_eviction\_init](group__mem-demand-paging-eviction.md#ga68dcfc0e5374de2c8ad7b9fe4e65c4f4)

void k\_mem\_paging\_eviction\_init(void)

Initialization function.

[k\_mem\_page\_out](group__mem-demand-paging.md#ga0b18037209b4d8b5964bd9a1d760f703)

int k\_mem\_page\_out(void \*addr, size\_t size)

Evict a page-aligned virtual memory region to the backing store.

[k\_mem\_paging\_histogram\_backing\_store\_page\_in\_get](group__mem-demand-paging.md#ga1da0a643e8f85f98e29288e441a37dfa)

void k\_mem\_paging\_histogram\_backing\_store\_page\_in\_get(struct k\_mem\_paging\_histogram\_t \*hist)

Get the backing store page-in timing histogram.

[k\_mem\_unpin](group__mem-demand-paging.md#ga3278aae5e24733c722b7d83c4b17dab3)

void k\_mem\_unpin(void \*addr, size\_t size)

Un-pin an aligned virtual data region.

[k\_mem\_paging\_stats\_get](group__mem-demand-paging.md#ga52ad88e0c0eed2aa27331bfd4707b7ec)

void k\_mem\_paging\_stats\_get(struct k\_mem\_paging\_stats\_t \*stats)

Get the paging statistics since system startup.

[k\_mem\_pin](group__mem-demand-paging.md#ga5f2d422edde7d366e81a870ce057589f)

void k\_mem\_pin(void \*addr, size\_t size)

Pin an aligned virtual data region, paging in as necessary.

[k\_mem\_page\_in](group__mem-demand-paging.md#gab36c36a4e230677d2090514f7a34b408)

void k\_mem\_page\_in(void \*addr, size\_t size)

Load a virtual data region into memory.

[k\_mem\_paging\_histogram\_backing\_store\_page\_out\_get](group__mem-demand-paging.md#gae4f80d14f88a46ddb9aeb7afba861864)

void k\_mem\_paging\_histogram\_backing\_store\_page\_out\_get(struct k\_mem\_paging\_histogram\_t \*hist)

Get the backing store page-out timing histogram.

[k\_mem\_paging\_histogram\_eviction\_get](group__mem-demand-paging.md#gaec64d019d819b00c7bc3804aac269199)

void k\_mem\_paging\_histogram\_eviction\_get(struct k\_mem\_paging\_histogram\_t \*hist)

Get the eviction timing histogram.

[k\_mem\_paging\_thread\_stats\_get](group__mem-demand-paging.md#gafad6b39cb2faf3bb416cd4d3faaa8d8c)

void k\_mem\_paging\_thread\_stats\_get(struct k\_thread \*thread, struct k\_mem\_paging\_stats\_t \*stats)

Get the paging statistics since system startup for a thread.

[inttypes.h](inttypes_8h.md)

[mm.h](kernel_2mm_8h.md)

[stdint.h](stdint_8h.md)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[k\_mem\_paging\_histogram\_t](structk__mem__paging__histogram__t.md)

Paging Statistics Histograms.

**Definition** demand\_paging.h:66

[k\_mem\_paging\_histogram\_t::counts](structk__mem__paging__histogram__t.md#a4421676cbc9f6c63808ee914e2ff8c90)

unsigned long counts[CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM\_NUM\_BINS]

**Definition** demand\_paging.h:69

[k\_mem\_paging\_histogram\_t::bounds](structk__mem__paging__histogram__t.md#a893236502aeb56975263b27cf4f2755a)

unsigned long bounds[CONFIG\_DEMAND\_PAGING\_TIMING\_HISTOGRAM\_NUM\_BINS]

**Definition** demand\_paging.h:74

[k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md)

Paging Statistics.

**Definition** demand\_paging.h:35

[k\_mem\_paging\_stats\_t::in\_isr](structk__mem__paging__stats__t.md#a210c83357c14a06fbd69b0cf2263fbb6)

unsigned long in\_isr

Number of page faults while in ISR.

**Definition** demand\_paging.h:49

[k\_mem\_paging\_stats\_t::irq\_unlocked](structk__mem__paging__stats__t.md#a2c2183c1679ae158bdd232fa1fdeb250)

unsigned long irq\_unlocked

Number of page faults with IRQ unlocked.

**Definition** demand\_paging.h:45

[k\_mem\_paging\_stats\_t::cnt](structk__mem__paging__stats__t.md#a3daad63e37d200f44d88c3d4e49f361a)

unsigned long cnt

Number of page faults.

**Definition** demand\_paging.h:39

[k\_mem\_paging\_stats\_t::dirty](structk__mem__paging__stats__t.md#a4f8523c0e78c8de1e2443a194e875609)

unsigned long dirty

Number of dirty pages selected for eviction.

**Definition** demand\_paging.h:58

[k\_mem\_paging\_stats\_t::clean](structk__mem__paging__stats__t.md#a7b421897b3125d1a44284ca964ef1f66)

unsigned long clean

Number of clean pages selected for eviction.

**Definition** demand\_paging.h:55

[k\_mem\_paging\_stats\_t::irq\_locked](structk__mem__paging__stats__t.md#aa762731df50fc81d08beb3628f9dbd71)

unsigned long irq\_locked

Number of page faults with IRQ locked.

**Definition** demand\_paging.h:42

[k\_mem\_paging\_stats\_t::eviction](structk__mem__paging__stats__t.md#aa8175953fd7fa0a5057069b73b930f3b)

struct k\_mem\_paging\_stats\_t::@371075322273065342024065267377370237043373206123 eviction

[k\_mem\_paging\_stats\_t::pagefaults](structk__mem__paging__stats__t.md#af6331dae30074d48396151b33ac7a0a7)

struct k\_mem\_paging\_stats\_t::@321226162154203320160315155356321330167027120302 pagefaults

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [mm](dir_29d573030f160bf8332fbdce7db88bc8.md)
- [demand\_paging.h](demand__paging_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
