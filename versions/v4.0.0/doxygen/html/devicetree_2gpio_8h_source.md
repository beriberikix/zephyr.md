---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree_2gpio_8h_source.html
original_path: doxygen/html/devicetree_2gpio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio.h

[Go to the documentation of this file.](devicetree_2gpio_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020, Linaro Ltd.

8 \* Copyright (c) 2020 Nordic Semiconductor

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_GPIO\_H\_

14#define ZEPHYR\_INCLUDE\_DEVICETREE\_GPIO\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

25

[ 53](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)#define DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, idx) \

54 DT\_PHANDLE\_BY\_IDX(node\_id, gpio\_pha, idx)

55

[ 65](group__devicetree-gpio.md#gafbad7d0d7f7fb9338997482c8da0e566)#define DT\_GPIO\_CTLR(node\_id, gpio\_pha) \

66 DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, 0)

67

[ 109](group__devicetree-gpio.md#ga8f7d82567056266bab1603865f8b27af)#define DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, idx) \

110 DT\_PHA\_BY\_IDX(node\_id, gpio\_pha, idx, pin)

111

[ 120](group__devicetree-gpio.md#ga4e41ec30ece058555333811a9fcee333)#define DT\_GPIO\_PIN(node\_id, gpio\_pha) \

121 DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, 0)

122

[ 165](group__devicetree-gpio.md#ga672b2597b99194b8cbd42b3f3401d2b5)#define DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, idx) \

166 DT\_PHA\_BY\_IDX\_OR(node\_id, gpio\_pha, idx, flags, 0)

167

[ 176](group__devicetree-gpio.md#ga32b3383d7ed543602a7b4a031018316f)#define DT\_GPIO\_FLAGS(node\_id, gpio\_pha) \

177 DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, 0)

178

[ 217](group__devicetree-gpio.md#ga0a4575c3750db76692fd0f817a169b50)#define DT\_NUM\_GPIO\_HOGS(node\_id) \

218 COND\_CODE\_1(IS\_ENABLED(DT\_CAT(node\_id, \_GPIO\_HOGS\_EXISTS)), \

219 (DT\_CAT(node\_id, \_GPIO\_HOGS\_NUM)), (0))

220

[ 262](group__devicetree-gpio.md#gaf4ecdebbd433473f654f4b6859542af9)#define DT\_GPIO\_HOG\_PIN\_BY\_IDX(node\_id, idx) \

263 DT\_CAT4(node\_id, \_GPIO\_HOGS\_IDX\_, idx, \_VAL\_pin)

264

[ 307](group__devicetree-gpio.md#gaed024e6acac49f591fe50cd43e8af14f)#define DT\_GPIO\_HOG\_FLAGS\_BY\_IDX(node\_id, idx) \

308 COND\_CODE\_1(IS\_ENABLED(DT\_CAT4(node\_id, \_GPIO\_HOGS\_IDX\_, idx, \_VAL\_flags\_EXISTS)), \

309 (DT\_CAT4(node\_id, \_GPIO\_HOGS\_IDX\_, idx, \_VAL\_flags)), (0))

310

[ 321](group__devicetree-gpio.md#ga162bca126f7015816286358f09bde6ff)#define DT\_INST\_GPIO\_PIN\_BY\_IDX(inst, gpio\_pha, idx) \

322 DT\_GPIO\_PIN\_BY\_IDX(DT\_DRV\_INST(inst), gpio\_pha, idx)

323

[ 332](group__devicetree-gpio.md#ga5ee13b3de1d4cecc877963dfa8820cfd)#define DT\_INST\_GPIO\_PIN(inst, gpio\_pha) \

333 DT\_INST\_GPIO\_PIN\_BY\_IDX(inst, gpio\_pha, 0)

334

[ 345](group__devicetree-gpio.md#gafd40d1eec5c1672b7675ae47388c1cef)#define DT\_INST\_GPIO\_FLAGS\_BY\_IDX(inst, gpio\_pha, idx) \

346 DT\_GPIO\_FLAGS\_BY\_IDX(DT\_DRV\_INST(inst), gpio\_pha, idx)

347

[ 356](group__devicetree-gpio.md#ga8d3edd53d6d8e89afc68f0c10176f57f)#define DT\_INST\_GPIO\_FLAGS(inst, gpio\_pha) \

357 DT\_INST\_GPIO\_FLAGS\_BY\_IDX(inst, gpio\_pha, 0)

358

362

363#ifdef \_\_cplusplus

364}

365#endif

366

367#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_GPIO\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [gpio.h](devicetree_2gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
