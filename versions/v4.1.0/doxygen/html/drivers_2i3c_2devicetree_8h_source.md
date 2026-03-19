---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2i3c_2devicetree_8h_source.html
original_path: doxygen/html/drivers_2i3c_2devicetree_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devicetree.h

[Go to the documentation of this file.](drivers_2i3c_2devicetree_8h.md)

1/\*

2 \* Copyright 2022 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_DEVICETREE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_DEVICETREE\_H\_

9

16

17#include <[stdint.h](stdint_8h.md)>

18

19#include <[zephyr/device.h](device_8h.md)>

20#include <[zephyr/devicetree.h](devicetree_8h.md)>

21#include <[zephyr/sys/util.h](sys_2util_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 36](group__i3c__devicetree.md#ga917b45ec38e08d0c464cebe3372b682e)#define I3C\_DEVICE\_ID\_DT(node\_id) \

37 { \

38 .pid = ((uint64\_t)DT\_PROP\_BY\_IDX(node\_id, reg, 1) << 32)\

39 | DT\_PROP\_BY\_IDX(node\_id, reg, 2), \

40 }

41

[ 52](group__i3c__devicetree.md#gadc45c0fdd41c081a0c3767159aae0c57)#define I3C\_DEVICE\_ID\_DT\_INST(inst) \

53 I3C\_DEVICE\_ID\_DT(DT\_DRV\_INST(inst))

54

[ 65](group__i3c__devicetree.md#ga07eca721a06080900d976474138346fc)#define I3C\_DEVICE\_DESC\_DT(node\_id) \

66 { \

67 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

68 .dev = DEVICE\_DT\_GET(node\_id), \

69 .static\_addr = DT\_PROP\_BY\_IDX(node\_id, reg, 0), \

70 .pid = ((uint64\_t)DT\_PROP\_BY\_IDX(node\_id, reg, 1) << 32)\

71 | DT\_PROP\_BY\_IDX(node\_id, reg, 2), \

72 .init\_dynamic\_addr = \

73 DT\_PROP\_OR(node\_id, assigned\_address, 0), \

74 .supports\_setaasa = DT\_PROP(node\_id, supports\_setaasa), \

75 },

76

[ 88](group__i3c__devicetree.md#gafb9b50f7d6e288d1722db5b4176742e9)#define I3C\_DEVICE\_DESC\_DT\_INST(inst) \

89 I3C\_DEVICE\_DESC\_DT(DT\_DRV\_INST(inst))

90

[ 97](group__i3c__devicetree.md#gae5c3df5af3fe52476a506c4eff34ca1e)#define I3C\_DEVICE\_DESC\_DT\_FILTERED(node\_id) \

98 COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, reg, 1), \

99 (), (I3C\_DEVICE\_DESC\_DT(node\_id)))

100

[ 109](group__i3c__devicetree.md#ga88aac6c42bbcd2f3276b6686c6786363)#define I3C\_DEVICE\_ARRAY\_DT(node\_id) \

110 { \

111 DT\_FOREACH\_CHILD\_STATUS\_OKAY( \

112 node\_id, \

113 I3C\_DEVICE\_DESC\_DT\_FILTERED) \

114 }

115

[ 126](group__i3c__devicetree.md#ga3153fd2d2b68eb760730827f6d6986c5)#define I3C\_DEVICE\_ARRAY\_DT\_INST(inst) \

127 I3C\_DEVICE\_ARRAY\_DT(DT\_DRV\_INST(inst))

128

[ 154](group__i3c__devicetree.md#gaab3219d45b125dd12d583bfd1823a61c)#define I3C\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

155 prio, api, ...) \

156 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

157 prio, api, \_\_VA\_ARGS\_\_)

158

[ 167](group__i3c__devicetree.md#ga77a471977d2c6edc530d3ce0febb8dbe)#define I3C\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

168 I3C\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

169

[ 179](group__i3c__devicetree.md#gaf317b1bcec787d594d3952dda2b9dc51)#define I3C\_I2C\_DEVICE\_DESC\_DT(node\_id) \

180 { \

181 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

182 .addr = DT\_PROP\_BY\_IDX(node\_id, reg, 0), \

183 .lvr = DT\_PROP\_BY\_IDX(node\_id, reg, 2), \

184 },

185

[ 196](group__i3c__devicetree.md#ga4c004a38164a56a1d1d027f2d29974e4)#define I3C\_I2C\_DEVICE\_DESC\_DT\_INST(inst) \

197 I3C\_I2C\_DEVICE\_DESC\_DT(DT\_DRV\_INST(inst))

198

199

[ 206](group__i3c__devicetree.md#ga703052c71216a4f152028540592ad581)#define I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED(node\_id) \

207 COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, reg, 1), \

208 (I3C\_I2C\_DEVICE\_DESC\_DT(node\_id)), ())

209

[ 218](group__i3c__devicetree.md#ga78f4d3fa3977989a731e33089d535701)#define I3C\_I2C\_DEVICE\_ARRAY\_DT(node\_id) \

219 { \

220 DT\_FOREACH\_CHILD\_STATUS\_OKAY( \

221 node\_id, \

222 I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED) \

223 }

224

[ 235](group__i3c__devicetree.md#gab441564c36a5d7e0856bba5eed51906f)#define I3C\_I2C\_DEVICE\_ARRAY\_DT\_INST(inst) \

236 I3C\_I2C\_DEVICE\_ARRAY\_DT(DT\_DRV\_INST(inst))

237

238#ifdef \_\_cplusplus

239}

240#endif

241

245

246#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_DEVICETREE\_H\_ \*/

[device.h](device_8h.md)

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[stdint.h](stdint_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [devicetree.h](drivers_2i3c_2devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
