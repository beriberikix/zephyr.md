---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/devicetree_2dma_8h_source.html
original_path: doxygen/html/devicetree_2dma_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma.h

[Go to the documentation of this file.](devicetree_2dma_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020, Linaro Ltd.

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_DMAS\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_DMAS\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 51](group__devicetree-dmas.md#gac74e56d90f8abe4bb0b53acddb618a3a)#define DT\_DMAS\_CTLR\_BY\_IDX(node\_id, idx) DT\_PHANDLE\_BY\_IDX(node\_id, dmas, idx)

52

[ 80](group__devicetree-dmas.md#ga8c148fc826dee34f5e4601f4a7aa9f55)#define DT\_DMAS\_CTLR\_BY\_NAME(node\_id, name) \

81 DT\_PHANDLE\_BY\_NAME(node\_id, dmas, name)

82

[ 90](group__devicetree-dmas.md#ga09a22a0e5133dc7514680c16373f6ad3)#define DT\_DMAS\_CTLR(node\_id) DT\_DMAS\_CTLR\_BY\_IDX(node\_id, 0)

91

[ 102](group__devicetree-dmas.md#ga5dbb1f22a0098a3493fd6f4cef9985a9)#define DT\_INST\_DMAS\_CTLR\_BY\_IDX(inst, idx) \

103 DT\_DMAS\_CTLR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

104

[ 114](group__devicetree-dmas.md#gad098f0b51ee1f629c1259ca346f49303)#define DT\_INST\_DMAS\_CTLR\_BY\_NAME(inst, name) \

115 DT\_DMAS\_CTLR\_BY\_NAME(DT\_DRV\_INST(inst), name)

116

[ 124](group__devicetree-dmas.md#ga32025fb8590eec09adaff23db1138e75)#define DT\_INST\_DMAS\_CTLR(inst) DT\_INST\_DMAS\_CTLR\_BY\_IDX(inst, 0)

125

[ 165](group__devicetree-dmas.md#ga8aff7a91d19482964b8b56cb558c1b59)#define DT\_DMAS\_CELL\_BY\_IDX(node\_id, idx, cell) \

166 DT\_PHA\_BY\_IDX(node\_id, dmas, idx, cell)

167

[ 176](group__devicetree-dmas.md#gad4e1a8f22b8943328df2a3f8f2a149b7)#define DT\_INST\_DMAS\_CELL\_BY\_IDX(inst, idx, cell) \

177 DT\_PHA\_BY\_IDX(DT\_DRV\_INST(inst), dmas, idx, cell)

178

[ 220](group__devicetree-dmas.md#ga1b80ae7fee6bcc9aa2ad03435e70dd14)#define DT\_DMAS\_CELL\_BY\_NAME(node\_id, name, cell) \

221 DT\_PHA\_BY\_NAME(node\_id, dmas, name, cell)

222

[ 232](group__devicetree-dmas.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)#define DT\_INST\_DMAS\_CELL\_BY\_NAME(inst, name, cell) \

233 DT\_DMAS\_CELL\_BY\_NAME(DT\_DRV\_INST(inst), name, cell)

234

[ 241](group__devicetree-dmas.md#gab789e18935628f40d80f3b64ca5cbe80)#define DT\_DMAS\_HAS\_IDX(node\_id, idx) \

242 IS\_ENABLED(DT\_CAT4(node\_id, \_P\_dmas\_IDX\_, idx, \_EXISTS))

243

[ 250](group__devicetree-dmas.md#gaff634d5b2a342c73f001a5ee64b70829)#define DT\_INST\_DMAS\_HAS\_IDX(inst, idx) \

251 DT\_DMAS\_HAS\_IDX(DT\_DRV\_INST(inst), idx)

252

[ 260](group__devicetree-dmas.md#ga865adb5b82c63e7f63451b96cd5a6404)#define DT\_DMAS\_HAS\_NAME(node\_id, name) \

261 DT\_PROP\_HAS\_NAME(node\_id, dmas, name)

262

[ 270](group__devicetree-dmas.md#gad60c155da3d850a61365ca7d12dc1813)#define DT\_INST\_DMAS\_HAS\_NAME(inst, name) \

271 DT\_DMAS\_HAS\_NAME(DT\_DRV\_INST(inst), name)

272

276

277#ifdef \_\_cplusplus

278}

279#endif

280

281#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_DMAS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [dma.h](devicetree_2dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
