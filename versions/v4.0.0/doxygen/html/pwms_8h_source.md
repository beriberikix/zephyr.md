---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pwms_8h_source.html
original_path: doxygen/html/pwms_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwms.h

[Go to the documentation of this file.](pwms_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020, Linaro Ltd.

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_PWMS\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_PWMS\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 51](group__devicetree-pwms.md#ga2f16d00a53717a66668fb8bc967acce5)#define DT\_PWMS\_CTLR\_BY\_IDX(node\_id, idx) \

52 DT\_PHANDLE\_BY\_IDX(node\_id, pwms, idx)

53

[ 81](group__devicetree-pwms.md#ga6922e69c707219cd766fe317484dac8a)#define DT\_PWMS\_CTLR\_BY\_NAME(node\_id, name) \

82 DT\_PHANDLE\_BY\_NAME(node\_id, pwms, name)

83

[ 91](group__devicetree-pwms.md#gaff7a0b201d97a1d1bb1893b556d5a194)#define DT\_PWMS\_CTLR(node\_id) DT\_PWMS\_CTLR\_BY\_IDX(node\_id, 0)

92

[ 135](group__devicetree-pwms.md#ga0c1ab3329448f92936d57a83b5b3594e)#define DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, cell) \

136 DT\_PHA\_BY\_IDX(node\_id, pwms, idx, cell)

137

[ 182](group__devicetree-pwms.md#ga69233198a489283068bc1ded5072ca26)#define DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, cell) \

183 DT\_PHA\_BY\_NAME(node\_id, pwms, name, cell)

184

[ 192](group__devicetree-pwms.md#ga2062b31a090c05ccd267ae1468b182ef)#define DT\_PWMS\_CELL(node\_id, cell) DT\_PWMS\_CELL\_BY\_IDX(node\_id, 0, cell)

193

[ 207](group__devicetree-pwms.md#ga10a372e44c7e3feb551ca996c6ca5a8f)#define DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, idx) \

208 DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, channel)

209

[ 224](group__devicetree-pwms.md#ga59a4b9884e9620eac04c3808a3a6d164)#define DT\_PWMS\_CHANNEL\_BY\_NAME(node\_id, name) \

225 DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, channel)

226

[ 233](group__devicetree-pwms.md#gaeb0a10ad37fdfd3dcc75bd379908acdc)#define DT\_PWMS\_CHANNEL(node\_id) DT\_PWMS\_CHANNEL\_BY\_IDX(node\_id, 0)

234

[ 248](group__devicetree-pwms.md#ga9456f65777e6fc7c057c6e0709c9245f)#define DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, idx) \

249 DT\_PWMS\_CELL\_BY\_IDX(node\_id, idx, period)

250

[ 265](group__devicetree-pwms.md#ga74af83d31fc38f331808dedfaecf4c74)#define DT\_PWMS\_PERIOD\_BY\_NAME(node\_id, name) \

266 DT\_PWMS\_CELL\_BY\_NAME(node\_id, name, period)

267

[ 274](group__devicetree-pwms.md#gac6006a723932325b96a1b50619be153b)#define DT\_PWMS\_PERIOD(node\_id) DT\_PWMS\_PERIOD\_BY\_IDX(node\_id, 0)

275

[ 290](group__devicetree-pwms.md#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)#define DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, idx) \

291 DT\_PHA\_BY\_IDX\_OR(node\_id, pwms, idx, flags, 0)

292

[ 310](group__devicetree-pwms.md#ga7a1621bfb223da23aa030b64fc0c0bcd)#define DT\_PWMS\_FLAGS\_BY\_NAME(node\_id, name) \

311 DT\_PHA\_BY\_NAME\_OR(node\_id, pwms, name, flags, 0)

312

[ 319](group__devicetree-pwms.md#ga8dcd2d18129504d1a4ab71ae05c48c44)#define DT\_PWMS\_FLAGS(node\_id) DT\_PWMS\_FLAGS\_BY\_IDX(node\_id, 0)

320

[ 331](group__devicetree-pwms.md#ga4f751ba5f3c1aad5d62178b166f36c24)#define DT\_INST\_PWMS\_CTLR\_BY\_IDX(inst, idx) \

332 DT\_PWMS\_CTLR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

333

[ 343](group__devicetree-pwms.md#gae66d3e710496bff9789996ddb72e1ebe)#define DT\_INST\_PWMS\_CTLR\_BY\_NAME(inst, name) \

344 DT\_PWMS\_CTLR\_BY\_NAME(DT\_DRV\_INST(inst), name)

345

[ 353](group__devicetree-pwms.md#ga2f79a0a48e08c89bac58d16d9731e683)#define DT\_INST\_PWMS\_CTLR(inst) DT\_INST\_PWMS\_CTLR\_BY\_IDX(inst, 0)

354

[ 363](group__devicetree-pwms.md#gad106bf22d9dc90384519cd6ccc8fd1c6)#define DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, cell) \

364 DT\_PWMS\_CELL\_BY\_IDX(DT\_DRV\_INST(inst), idx, cell)

365

[ 375](group__devicetree-pwms.md#ga5731d949be09461f5da040e451cc509c)#define DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, cell) \

376 DT\_PWMS\_CELL\_BY\_NAME(DT\_DRV\_INST(inst), name, cell)

377

[ 384](group__devicetree-pwms.md#ga199804a2d06c301f19c5c8de232ede15)#define DT\_INST\_PWMS\_CELL(inst, cell) \

385 DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, 0, cell)

386

[ 394](group__devicetree-pwms.md#ga154ece84d782a7df2ce31b2a34f43870)#define DT\_INST\_PWMS\_CHANNEL\_BY\_IDX(inst, idx) \

395 DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, channel)

396

[ 405](group__devicetree-pwms.md#ga60901952d81e29dbfbbe88ee3ffe3e17)#define DT\_INST\_PWMS\_CHANNEL\_BY\_NAME(inst, name) \

406 DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, channel)

407

[ 414](group__devicetree-pwms.md#gad871b89fd1b2d62aae84dc35a0819032)#define DT\_INST\_PWMS\_CHANNEL(inst) DT\_INST\_PWMS\_CHANNEL\_BY\_IDX(inst, 0)

415

[ 423](group__devicetree-pwms.md#ga7e7408507ecdac75cb7c9ba2b9176ec8)#define DT\_INST\_PWMS\_PERIOD\_BY\_IDX(inst, idx) \

424 DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, period)

425

[ 434](group__devicetree-pwms.md#ga7ac719270232e67f91bc65e3786be1a1)#define DT\_INST\_PWMS\_PERIOD\_BY\_NAME(inst, name) \

435 DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, period)

436

[ 443](group__devicetree-pwms.md#ga2b122199764cff41c04bad243f4456dc)#define DT\_INST\_PWMS\_PERIOD(inst) DT\_INST\_PWMS\_PERIOD\_BY\_IDX(inst, 0)

444

[ 452](group__devicetree-pwms.md#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)#define DT\_INST\_PWMS\_FLAGS\_BY\_IDX(inst, idx) \

453 DT\_INST\_PWMS\_CELL\_BY\_IDX(inst, idx, flags)

454

[ 464](group__devicetree-pwms.md#ga23a8815368cbd82a8673e00abdfeab6b)#define DT\_INST\_PWMS\_FLAGS\_BY\_NAME(inst, name) \

465 DT\_INST\_PWMS\_CELL\_BY\_NAME(inst, name, flags)

466

[ 473](group__devicetree-pwms.md#ga5ca45d33eae6b50012e8c052e3bd5df0)#define DT\_INST\_PWMS\_FLAGS(inst) DT\_INST\_PWMS\_FLAGS\_BY\_IDX(inst, 0)

474

478

479#ifdef \_\_cplusplus

480}

481#endif

482

483#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_PWMS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [pwms.h](pwms_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
