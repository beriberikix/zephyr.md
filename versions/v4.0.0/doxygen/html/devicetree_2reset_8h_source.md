---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree_2reset_8h_source.html
original_path: doxygen/html/devicetree_2reset_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

reset.h

[Go to the documentation of this file.](devicetree_2reset_8h.md)

1

5

6/\*

7 \* Copyright (c) 2022, Andrei-Edward Popa

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_RESET\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_RESET\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 50](group__devicetree-reset-controller.md#gaa730fe6a58ee0a2d9daf7e125048f9e6)#define DT\_RESET\_CTLR\_BY\_IDX(node\_id, idx) \

51 DT\_PHANDLE\_BY\_IDX(node\_id, resets, idx)

52

[ 60](group__devicetree-reset-controller.md#ga55afbfa565375eb4b233051f7065e504)#define DT\_RESET\_CTLR(node\_id) \

61 DT\_RESET\_CTLR\_BY\_IDX(node\_id, 0)

62

[ 89](group__devicetree-reset-controller.md#ga5bc0702036df3a38ceb2d2741ee0717d)#define DT\_RESET\_CTLR\_BY\_NAME(node\_id, name) \

90 DT\_PHANDLE\_BY\_NAME(node\_id, resets, name)

91

[ 121](group__devicetree-reset-controller.md#ga17918c75ef82acea60d7e65b6f1cee0a)#define DT\_RESET\_CELL\_BY\_IDX(node\_id, idx, cell) \

122 DT\_PHA\_BY\_IDX(node\_id, resets, idx, cell)

123

[ 155](group__devicetree-reset-controller.md#ga102229a7a1a30a29c5a5bf2bb0d42ada)#define DT\_RESET\_CELL\_BY\_NAME(node\_id, name, cell) \

156 DT\_PHA\_BY\_NAME(node\_id, resets, name, cell)

157

[ 165](group__devicetree-reset-controller.md#ga626173f9cd280016f9f743d12bc4c047)#define DT\_RESET\_CELL(node\_id, cell) \

166 DT\_RESET\_CELL\_BY\_IDX(node\_id, 0, cell)

167

[ 178](group__devicetree-reset-controller.md#ga44cc59dc014eb69aacd4b6fedb5b2a54)#define DT\_INST\_RESET\_CTLR\_BY\_IDX(inst, idx) \

179 DT\_RESET\_CTLR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

180

[ 188](group__devicetree-reset-controller.md#gadc32a356d6a18689ca4a20cc657ce600)#define DT\_INST\_RESET\_CTLR(inst) \

189 DT\_INST\_RESET\_CTLR\_BY\_IDX(inst, 0)

190

[ 202](group__devicetree-reset-controller.md#ga66352f34890886dc20fdaa3a3f9beea9)#define DT\_INST\_RESET\_CTLR\_BY\_NAME(inst, name) \

203 DT\_RESET\_CTLR\_BY\_NAME(DT\_DRV\_INST(inst), name)

204

[ 214](group__devicetree-reset-controller.md#ga9727e93185d96b84ec2d53ef07597a02)#define DT\_INST\_RESET\_CELL\_BY\_IDX(inst, idx, cell) \

215 DT\_RESET\_CELL\_BY\_IDX(DT\_DRV\_INST(inst), idx, cell)

216

[ 226](group__devicetree-reset-controller.md#ga3d914f91e6f1514d2b0d6ec61cf92a5e)#define DT\_INST\_RESET\_CELL\_BY\_NAME(inst, name, cell) \

227 DT\_RESET\_CELL\_BY\_NAME(DT\_DRV\_INST(inst), name, cell)

228

[ 235](group__devicetree-reset-controller.md#gad078f74edd7e672f6c3fda91dec01f12)#define DT\_INST\_RESET\_CELL(inst, cell) \

236 DT\_INST\_RESET\_CELL\_BY\_IDX(inst, 0, cell)

237

[ 269](group__devicetree-reset-controller.md#ga4259b4aa8bfe6f4ccb268c180541237d)#define DT\_RESET\_ID\_BY\_IDX(node\_id, idx) \

270 DT\_PHA\_BY\_IDX(node\_id, resets, idx, id)

271

[ 278](group__devicetree-reset-controller.md#gae8a5453df7ac3710858937485a9ee49b)#define DT\_RESET\_ID(node\_id) \

279 DT\_RESET\_ID\_BY\_IDX(node\_id, 0)

280

[ 289](group__devicetree-reset-controller.md#gac42ce32f6e5fd1ae2b449bcf60d70afc)#define DT\_INST\_RESET\_ID\_BY\_IDX(inst, idx) \

290 DT\_RESET\_ID\_BY\_IDX(DT\_DRV\_INST(inst), idx)

291

[ 298](group__devicetree-reset-controller.md#ga64080e5a9a0a568975323e637127e20f)#define DT\_INST\_RESET\_ID(inst) \

299 DT\_INST\_RESET\_ID\_BY\_IDX(inst, 0)

300

304

305#ifdef \_\_cplusplus

306}

307#endif

308

309#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_RESET\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [reset.h](devicetree_2reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
