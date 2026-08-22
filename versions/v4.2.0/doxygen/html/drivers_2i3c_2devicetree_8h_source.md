---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2i3c_2devicetree_8h_source.html
original_path: doxygen/html/drivers_2i3c_2devicetree_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

60

[ 62](group__i3c__devicetree.md#ga24fbe85a8cb5ffc049288b1b82e1c15b)#define I3C\_SUPPORTS\_SETAASA BIT(0)

[ 64](group__i3c__devicetree.md#ga91bb0d3b4b86524d5f7a6a0429a123da)#define I3C\_V1P0\_SUPPORT BIT(1)

65

67

[ 78](group__i3c__devicetree.md#ga07eca721a06080900d976474138346fc)#define I3C\_DEVICE\_DESC\_DT(node\_id) \

79 { \

80 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

81 .dev = DEVICE\_DT\_GET(node\_id), \

82 .static\_addr = DT\_PROP\_BY\_IDX(node\_id, reg, 0), \

83 .pid = ((uint64\_t)DT\_PROP\_BY\_IDX(node\_id, reg, 1) << 32) | \

84 DT\_PROP\_BY\_IDX(node\_id, reg, 2), \

85 .init\_dynamic\_addr = DT\_PROP\_OR(node\_id, assigned\_address, 0), \

86 .flags = FIELD\_PREP(I3C\_SUPPORTS\_SETAASA, DT\_PROP(node\_id, supports\_setaasa)) | \

87 FIELD\_PREP(I3C\_V1P0\_SUPPORT, DT\_PROP(node\_id, v1p0\_support)), \

88 },

89

[ 101](group__i3c__devicetree.md#gafb9b50f7d6e288d1722db5b4176742e9)#define I3C\_DEVICE\_DESC\_DT\_INST(inst) \

102 I3C\_DEVICE\_DESC\_DT(DT\_DRV\_INST(inst))

103

[ 110](group__i3c__devicetree.md#gae5c3df5af3fe52476a506c4eff34ca1e)#define I3C\_DEVICE\_DESC\_DT\_FILTERED(node\_id) \

111 COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, reg, 1), \

112 (), (I3C\_DEVICE\_DESC\_DT(node\_id)))

113

[ 122](group__i3c__devicetree.md#ga88aac6c42bbcd2f3276b6686c6786363)#define I3C\_DEVICE\_ARRAY\_DT(node\_id) \

123 { \

124 DT\_FOREACH\_CHILD\_STATUS\_OKAY( \

125 node\_id, \

126 I3C\_DEVICE\_DESC\_DT\_FILTERED) \

127 }

128

[ 139](group__i3c__devicetree.md#ga3153fd2d2b68eb760730827f6d6986c5)#define I3C\_DEVICE\_ARRAY\_DT\_INST(inst) \

140 I3C\_DEVICE\_ARRAY\_DT(DT\_DRV\_INST(inst))

141

[ 167](group__i3c__devicetree.md#gaab3219d45b125dd12d583bfd1823a61c)#define I3C\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

168 prio, api, ...) \

169 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

170 prio, api, \_\_VA\_ARGS\_\_)

171

[ 180](group__i3c__devicetree.md#ga77a471977d2c6edc530d3ce0febb8dbe)#define I3C\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

181 I3C\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

182

[ 192](group__i3c__devicetree.md#gaf317b1bcec787d594d3952dda2b9dc51)#define I3C\_I2C\_DEVICE\_DESC\_DT(node\_id) \

193 { \

194 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

195 .addr = DT\_PROP\_BY\_IDX(node\_id, reg, 0), \

196 .lvr = DT\_PROP\_BY\_IDX(node\_id, reg, 2), \

197 },

198

[ 209](group__i3c__devicetree.md#ga4c004a38164a56a1d1d027f2d29974e4)#define I3C\_I2C\_DEVICE\_DESC\_DT\_INST(inst) \

210 I3C\_I2C\_DEVICE\_DESC\_DT(DT\_DRV\_INST(inst))

211

212

[ 219](group__i3c__devicetree.md#ga703052c71216a4f152028540592ad581)#define I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED(node\_id) \

220 COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, reg, 1), \

221 (I3C\_I2C\_DEVICE\_DESC\_DT(node\_id)), ())

222

[ 231](group__i3c__devicetree.md#ga78f4d3fa3977989a731e33089d535701)#define I3C\_I2C\_DEVICE\_ARRAY\_DT(node\_id) \

232 { \

233 DT\_FOREACH\_CHILD\_STATUS\_OKAY( \

234 node\_id, \

235 I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED) \

236 }

237

[ 248](group__i3c__devicetree.md#gab441564c36a5d7e0856bba5eed51906f)#define I3C\_I2C\_DEVICE\_ARRAY\_DT\_INST(inst) \

249 I3C\_I2C\_DEVICE\_ARRAY\_DT(DT\_DRV\_INST(inst))

250

251#ifdef \_\_cplusplus

252}

253#endif

254

258

259#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_DEVICETREE\_H\_ \*/

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
