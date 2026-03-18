---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/clocks_8h_source.html
original_path: doxygen/html/clocks_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clocks.h

[Go to the documentation of this file.](clocks_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020, Linaro Ltd.

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_CLOCKS\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_CLOCKS\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 52](group__devicetree-clocks.md#gabfdf51e2b14c05e84366cff1bb056da0)#define DT\_CLOCKS\_HAS\_IDX(node\_id, idx) \

53 DT\_PROP\_HAS\_IDX(node\_id, clocks, idx)

54

[ 83](group__devicetree-clocks.md#ga9d32df36dd18c4839e6e9efe509b17a4)#define DT\_CLOCKS\_HAS\_NAME(node\_id, name) \

84 DT\_PROP\_HAS\_NAME(node\_id, clocks, name)

85

[ 107](group__devicetree-clocks.md#ga22d4e8621b5bf56ed0ac8295dd11d7e3)#define DT\_NUM\_CLOCKS(node\_id) \

108 DT\_PROP\_LEN(node\_id, clocks)

109

110

[ 136](group__devicetree-clocks.md#gab36c92fc26c3517031bce342148308c3)#define DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, idx) \

137 DT\_PHANDLE\_BY\_IDX(node\_id, clocks, idx)

138

[ 146](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)#define DT\_CLOCKS\_CTLR(node\_id) DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, 0)

147

[ 173](group__devicetree-clocks.md#gaf4c92378a2599ee7024f914ea3584404)#define DT\_CLOCKS\_CTLR\_BY\_NAME(node\_id, name) \

174 DT\_PHANDLE\_BY\_NAME(node\_id, clocks, name)

175

[ 207](group__devicetree-clocks.md#ga7db765e869b8455a6c56a8f22a7cc5c8)#define DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, idx, cell) \

208 DT\_PHA\_BY\_IDX(node\_id, clocks, idx, cell)

209

[ 243](group__devicetree-clocks.md#gaca32bfb478ac92e6a760ad0761328d5a)#define DT\_CLOCKS\_CELL\_BY\_NAME(node\_id, name, cell) \

244 DT\_PHA\_BY\_NAME(node\_id, clocks, name, cell)

245

[ 253](group__devicetree-clocks.md#ga211bc385cbbb1d8b8fa52e2e0a52d23d)#define DT\_CLOCKS\_CELL(node\_id, cell) DT\_CLOCKS\_CELL\_BY\_IDX(node\_id, 0, cell)

254

[ 261](group__devicetree-clocks.md#gaf8ebb6ccd4915cc4069e92f804fb63ac)#define DT\_INST\_CLOCKS\_HAS\_IDX(inst, idx) \

262 DT\_CLOCKS\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

263

[ 270](group__devicetree-clocks.md#ga6b2997f105a29ff5c136f3dbb6120287)#define DT\_INST\_CLOCKS\_HAS\_NAME(inst, name) \

271 DT\_CLOCKS\_HAS\_NAME(DT\_DRV\_INST(inst), name)

272

[ 278](group__devicetree-clocks.md#gadab88fe4063540efc136e5ae270c7cfa)#define DT\_INST\_NUM\_CLOCKS(inst) \

279 DT\_NUM\_CLOCKS(DT\_DRV\_INST(inst))

280

[ 291](group__devicetree-clocks.md#gac4a7a89937eae57960a2091d7edc5fd3)#define DT\_INST\_CLOCKS\_CTLR\_BY\_IDX(inst, idx) \

292 DT\_CLOCKS\_CTLR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

293

[ 301](group__devicetree-clocks.md#gaeebaf3a45822d86dfeb38a3fda66dc54)#define DT\_INST\_CLOCKS\_CTLR(inst) DT\_INST\_CLOCKS\_CTLR\_BY\_IDX(inst, 0)

302

[ 314](group__devicetree-clocks.md#ga209f77daee5016ed0d0d678ec6ec57b7)#define DT\_INST\_CLOCKS\_CTLR\_BY\_NAME(inst, name) \

315 DT\_CLOCKS\_CTLR\_BY\_NAME(DT\_DRV\_INST(inst), name)

316

[ 326](group__devicetree-clocks.md#ga5bee2e489f0818f0f2d1ec6d195bd3a8)#define DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, idx, cell) \

327 DT\_CLOCKS\_CELL\_BY\_IDX(DT\_DRV\_INST(inst), idx, cell)

328

[ 338](group__devicetree-clocks.md#ga976ab2adb237e5f1e0ba3496e9322d14)#define DT\_INST\_CLOCKS\_CELL\_BY\_NAME(inst, name, cell) \

339 DT\_CLOCKS\_CELL\_BY\_NAME(DT\_DRV\_INST(inst), name, cell)

340

[ 347](group__devicetree-clocks.md#gad6a9584690066548b8d61489ad615a45)#define DT\_INST\_CLOCKS\_CELL(inst, cell) \

348 DT\_INST\_CLOCKS\_CELL\_BY\_IDX(inst, 0, cell)

349

353

354#ifdef \_\_cplusplus

355}

356#endif

357

358#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_CLOCKS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [clocks.h](clocks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
