---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2i3c_2devicetree_8h_source.html
original_path: doxygen/html/drivers_2i3c_2devicetree_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

17#include <[zephyr/device.h](device_8h.md)>

18#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <[zephyr/sys/util.h](util_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 35](group__i3c__devicetree.md#ga917b45ec38e08d0c464cebe3372b682e)#define I3C\_DEVICE\_ID\_DT(node\_id) \

36 { \

37 .pid = ((uint64\_t)DT\_PROP\_BY\_IDX(node\_id, reg, 1) << 32)\

38 | DT\_PROP\_BY\_IDX(node\_id, reg, 2), \

39 }

40

[ 49](group__i3c__devicetree.md#gadc45c0fdd41c081a0c3767159aae0c57)#define I3C\_DEVICE\_ID\_DT\_INST(inst) \

50 I3C\_DEVICE\_ID\_DT(DT\_DRV\_INST(inst))

51

[ 62](group__i3c__devicetree.md#ga07eca721a06080900d976474138346fc)#define I3C\_DEVICE\_DESC\_DT(node\_id) \

63 { \

64 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

65 .dev = DEVICE\_DT\_GET(node\_id), \

66 .static\_addr = DT\_PROP\_BY\_IDX(node\_id, reg, 0), \

67 .pid = ((uint64\_t)DT\_PROP\_BY\_IDX(node\_id, reg, 1) << 32)\

68 | DT\_PROP\_BY\_IDX(node\_id, reg, 2), \

69 .init\_dynamic\_addr = \

70 DT\_PROP\_OR(node\_id, assigned\_address, 0), \

71 },

72

[ 81](group__i3c__devicetree.md#gafb9b50f7d6e288d1722db5b4176742e9)#define I3C\_DEVICE\_DESC\_DT\_INST(inst) \

82 I3C\_DEVICE\_DESC\_DT(DT\_DRV\_INST(inst))

83

[ 90](group__i3c__devicetree.md#gae5c3df5af3fe52476a506c4eff34ca1e)#define I3C\_DEVICE\_DESC\_DT\_FILTERED(node\_id) \

91 COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, reg, 1), \

92 (), (I3C\_DEVICE\_DESC\_DT(node\_id)))

93

[ 102](group__i3c__devicetree.md#ga88aac6c42bbcd2f3276b6686c6786363)#define I3C\_DEVICE\_ARRAY\_DT(node\_id) \

103 { \

104 DT\_FOREACH\_CHILD\_STATUS\_OKAY( \

105 node\_id, \

106 I3C\_DEVICE\_DESC\_DT\_FILTERED) \

107 }

108

[ 117](group__i3c__devicetree.md#ga3153fd2d2b68eb760730827f6d6986c5)#define I3C\_DEVICE\_ARRAY\_DT\_INST(inst) \

118 I3C\_DEVICE\_ARRAY\_DT(DT\_DRV\_INST(inst))

119

[ 145](group__i3c__devicetree.md#gaab3219d45b125dd12d583bfd1823a61c)#define I3C\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

146 prio, api, ...) \

147 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, \

148 prio, api, \_\_VA\_ARGS\_\_)

149

[ 158](group__i3c__devicetree.md#ga77a471977d2c6edc530d3ce0febb8dbe)#define I3C\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

159 I3C\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

160

[ 171](group__i3c__devicetree.md#gaf317b1bcec787d594d3952dda2b9dc51)#define I3C\_I2C\_DEVICE\_DESC\_DT(node\_id) \

172 { \

173 .bus = DEVICE\_DT\_GET(DT\_BUS(node\_id)), \

174 .addr = DT\_PROP\_BY\_IDX(node\_id, reg, 0), \

175 .lvr = DT\_PROP\_BY\_IDX(node\_id, reg, 2), \

176 },

177

[ 186](group__i3c__devicetree.md#ga4c004a38164a56a1d1d027f2d29974e4)#define I3C\_I2C\_DEVICE\_DESC\_DT\_INST(inst) \

187 I3C\_I2C\_DEVICE\_DESC\_DT(DT\_DRV\_INST(inst))

188

189

[ 196](group__i3c__devicetree.md#ga703052c71216a4f152028540592ad581)#define I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED(node\_id) \

197 COND\_CODE\_0(DT\_PROP\_BY\_IDX(node\_id, reg, 1), \

198 (I3C\_I2C\_DEVICE\_DESC\_DT(node\_id)), ())

199

[ 208](group__i3c__devicetree.md#ga78f4d3fa3977989a731e33089d535701)#define I3C\_I2C\_DEVICE\_ARRAY\_DT(node\_id) \

209 { \

210 DT\_FOREACH\_CHILD\_STATUS\_OKAY( \

211 node\_id, \

212 I3C\_I2C\_DEVICE\_DESC\_DT\_FILTERED) \

213 }

214

[ 223](group__i3c__devicetree.md#gab441564c36a5d7e0856bba5eed51906f)#define I3C\_I2C\_DEVICE\_ARRAY\_DT\_INST(inst) \

224 I3C\_I2C\_DEVICE\_ARRAY\_DT(DT\_DRV\_INST(inst))

225

226#ifdef \_\_cplusplus

227}

228#endif

229

233

234#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_DEVICETREE\_H\_ \*/

[device.h](device_8h.md)

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [devicetree.h](drivers_2i3c_2devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
