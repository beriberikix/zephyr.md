---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/devicetree_2pinctrl_8h_source.html
original_path: doxygen/html/devicetree_2pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl.h

[Go to the documentation of this file.](devicetree_2pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_PINCTRL\_H\_

7#define ZEPHYR\_INCLUDE\_DEVICETREE\_PINCTRL\_H\_

8

13

19

[ 40](group__devicetree-pinctrl.md#ga24089220a93bc955700fba2c6170090e)#define DT\_PINCTRL\_BY\_IDX(node\_id, pc\_idx, idx) \

41 DT\_CAT6(node\_id, \_P\_pinctrl\_, pc\_idx, \_IDX\_, idx, \_PH)

42

[ 57](group__devicetree-pinctrl.md#gaf4e6f811ea4b1698c048d5dd8bfa604a)#define DT\_PINCTRL\_0(node\_id, idx) DT\_PINCTRL\_BY\_IDX(node\_id, 0, idx)

58

[ 81](group__devicetree-pinctrl.md#ga1cd336f902738fd684f3d81b3fb6caae)#define DT\_PINCTRL\_BY\_NAME(node\_id, name, idx) \

82 DT\_CAT6(node\_id, \_PINCTRL\_NAME\_, name, \_IDX\_, idx, \_PH)

83

[ 104](group__devicetree-pinctrl.md#ga36eb691efc2a4854ccb62555aeade785)#define DT\_PINCTRL\_NAME\_TO\_IDX(node\_id, name) \

105 DT\_CAT4(node\_id, \_PINCTRL\_NAME\_, name, \_IDX)

106

[ 138](group__devicetree-pinctrl.md#ga47b0e5a18919f9f4829209cccbdeb430)#define DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(node\_id, pc\_idx) \

139 DT\_CAT4(node\_id, \_PINCTRL\_IDX\_, pc\_idx, \_TOKEN)

140

[ 164](group__devicetree-pinctrl.md#gaa6eec236ccde612e88017b027f4ba711)#define DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(node\_id, pc\_idx) \

165 DT\_CAT4(node\_id, \_PINCTRL\_IDX\_, pc\_idx, \_UPPER\_TOKEN)

166

[ 189](group__devicetree-pinctrl.md#ga6ae1bab2a71cb628405ec43d38705606)#define DT\_NUM\_PINCTRLS\_BY\_IDX(node\_id, pc\_idx) \

190 DT\_CAT4(node\_id, \_P\_pinctrl\_, pc\_idx, \_LEN)

191

[ 212](group__devicetree-pinctrl.md#gaf96f1c82cc08008882f52e719ecd348c)#define DT\_NUM\_PINCTRLS\_BY\_NAME(node\_id, name) \

213 DT\_NUM\_PINCTRLS\_BY\_IDX(node\_id, DT\_PINCTRL\_NAME\_TO\_IDX(node\_id, name))

214

[ 239](group__devicetree-pinctrl.md#gaa2a012ce1d9ba026ee90001ae7f80381)#define DT\_NUM\_PINCTRL\_STATES(node\_id) DT\_CAT(node\_id, \_PINCTRL\_NUM)

240

[ 268](group__devicetree-pinctrl.md#ga5f1493cbfb7578b8fe3e37953aa9feaa)#define DT\_PINCTRL\_HAS\_IDX(node\_id, pc\_idx) \

269 IS\_ENABLED(DT\_CAT4(node\_id, \_PINCTRL\_IDX\_, pc\_idx, \_EXISTS))

270

[ 297](group__devicetree-pinctrl.md#gac9cd8112ad745f34eb6f6e4a13d7fd7e)#define DT\_PINCTRL\_HAS\_NAME(node\_id, name) \

298 IS\_ENABLED(DT\_CAT4(node\_id, \_PINCTRL\_NAME\_, name, \_EXISTS))

299

[ 311](group__devicetree-pinctrl.md#ga3388742fe3fb1f32a03566730890eaf0)#define DT\_INST\_PINCTRL\_BY\_IDX(inst, pc\_idx, idx) \

312 DT\_PINCTRL\_BY\_IDX(DT\_DRV\_INST(inst), pc\_idx, idx)

313

[ 329](group__devicetree-pinctrl.md#ga3cd59afe76bc5d82b63ef21cae451f11)#define DT\_INST\_PINCTRL\_0(inst, idx) \

330 DT\_PINCTRL\_BY\_IDX(DT\_DRV\_INST(inst), 0, idx)

331

[ 344](group__devicetree-pinctrl.md#ga4c171c27a91bd85e49b725bda6c05619)#define DT\_INST\_PINCTRL\_BY\_NAME(inst, name, idx) \

345 DT\_PINCTRL\_BY\_NAME(DT\_DRV\_INST(inst), name, idx)

346

[ 358](group__devicetree-pinctrl.md#ga12c18d8d9724d98d121d8118b43686c3)#define DT\_INST\_PINCTRL\_NAME\_TO\_IDX(inst, name) \

359 DT\_PINCTRL\_NAME\_TO\_IDX(DT\_DRV\_INST(inst), name)

360

[ 371](group__devicetree-pinctrl.md#ga80c3fb3defb7315877dc48db2932ef70)#define DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(inst, pc\_idx) \

372 DT\_PINCTRL\_IDX\_TO\_NAME\_TOKEN(DT\_DRV\_INST(inst), pc\_idx)

373

[ 384](group__devicetree-pinctrl.md#ga6d01324cecb6db502c46c42817c56bc9)#define DT\_INST\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(inst, pc\_idx) \

385 DT\_PINCTRL\_IDX\_TO\_NAME\_UPPER\_TOKEN(DT\_DRV\_INST(inst), pc\_idx)

386

[ 398](group__devicetree-pinctrl.md#ga1de8198573428ec717733204d91f0391)#define DT\_INST\_NUM\_PINCTRLS\_BY\_IDX(inst, pc\_idx) \

399 DT\_NUM\_PINCTRLS\_BY\_IDX(DT\_DRV\_INST(inst), pc\_idx)

400

[ 411](group__devicetree-pinctrl.md#gae253489146c61cb075f06192948275ff)#define DT\_INST\_NUM\_PINCTRLS\_BY\_NAME(inst, name) \

412 DT\_NUM\_PINCTRLS\_BY\_NAME(DT\_DRV\_INST(inst), name)

413

[ 422](group__devicetree-pinctrl.md#ga4e91cf82c2a7aaecdb43761b217231d4)#define DT\_INST\_NUM\_PINCTRL\_STATES(inst) \

423 DT\_NUM\_PINCTRL\_STATES(DT\_DRV\_INST(inst))

424

[ 435](group__devicetree-pinctrl.md#ga53f17d0a6061cad7270544068f1cb003)#define DT\_INST\_PINCTRL\_HAS\_IDX(inst, pc\_idx) \

436 DT\_PINCTRL\_HAS\_IDX(DT\_DRV\_INST(inst), pc\_idx)

437

[ 447](group__devicetree-pinctrl.md#ga0e2af9dde68b57f6b1ffc86143fc2e40)#define DT\_INST\_PINCTRL\_HAS\_NAME(inst, name) \

448 DT\_PINCTRL\_HAS\_NAME(DT\_DRV\_INST(inst), name)

449

450

454

455#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [pinctrl.h](devicetree_2pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
