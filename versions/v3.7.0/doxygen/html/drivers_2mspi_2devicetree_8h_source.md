---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2mspi_2devicetree_8h_source.html
original_path: doxygen/html/drivers_2mspi_2devicetree_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devicetree.h

[Go to the documentation of this file.](drivers_2mspi_2devicetree_8h.md)

1/\*

2 \* Copyright (c) 2024, Ambiq Micro Inc. <www.ambiq.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MSPI\_DEVICETREE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_MSPI\_DEVICETREE\_H\_

9

16

17#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 32](group__mspi__devicetree.md#gaa8e730d85dede3d1e5dc9f69f30098b2)#define MSPI\_DEVICE\_CONFIG\_DT(mspi\_dev) \

33 { \

34 .ce\_num = DT\_PROP\_OR(mspi\_dev, mspi\_hardware\_ce\_num, 0), \

35 .freq = DT\_PROP(mspi\_dev, mspi\_max\_frequency), \

36 .io\_mode = DT\_ENUM\_IDX\_OR(mspi\_dev, mspi\_io\_mode, \

37 MSPI\_IO\_MODE\_SINGLE), \

38 .data\_rate = DT\_ENUM\_IDX\_OR(mspi\_dev, mspi\_data\_rate, \

39 MSPI\_DATA\_RATE\_SINGLE), \

40 .cpp = DT\_ENUM\_IDX\_OR(mspi\_dev, mspi\_cpp\_mode, MSPI\_CPP\_MODE\_0), \

41 .endian = DT\_ENUM\_IDX\_OR(mspi\_dev, mspi\_endian, \

42 MSPI\_XFER\_LITTLE\_ENDIAN), \

43 .ce\_polarity = DT\_ENUM\_IDX\_OR(mspi\_dev, mspi\_ce\_polarity, \

44 MSPI\_CE\_ACTIVE\_LOW), \

45 .dqs\_enable = DT\_PROP(mspi\_dev, mspi\_dqs\_enable), \

46 .rx\_dummy = DT\_PROP\_OR(mspi\_dev, rx\_dummy, 0), \

47 .tx\_dummy = DT\_PROP\_OR(mspi\_dev, tx\_dummy, 0), \

48 .read\_cmd = DT\_PROP\_OR(mspi\_dev, read\_command, 0), \

49 .write\_cmd = DT\_PROP\_OR(mspi\_dev, write\_command, 0), \

50 .cmd\_length = DT\_ENUM\_IDX\_OR(mspi\_dev, command\_length, 0), \

51 .addr\_length = DT\_ENUM\_IDX\_OR(mspi\_dev, address\_length, 0), \

52 .mem\_boundary = COND\_CODE\_1(DT\_NODE\_HAS\_PROP(mspi\_dev, ce\_break\_config), \

53 (DT\_PROP\_BY\_IDX(mspi\_dev, ce\_break\_config, 0)), \

54 (0)), \

55 .time\_to\_break = COND\_CODE\_1(DT\_NODE\_HAS\_PROP(mspi\_dev, ce\_break\_config), \

56 (DT\_PROP\_BY\_IDX(mspi\_dev, ce\_break\_config, 1)), \

57 (0)), \

58 }

59

[ 68](group__mspi__devicetree.md#ga52ebf325f9a1eb7d9fda6736ac8188f1)#define MSPI\_DEVICE\_CONFIG\_DT\_INST(inst) MSPI\_DEVICE\_CONFIG\_DT(DT\_DRV\_INST(inst))

69

[ 79](group__mspi__devicetree.md#ga01a618fadb0147bf5abf42972a17f594)#define MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK(mspi\_dev) \

80 { \

81 .enable = DT\_PROP\_BY\_IDX(mspi\_dev, xip\_config, 0), \

82 .address\_offset = DT\_PROP\_BY\_IDX(mspi\_dev, xip\_config, 1), \

83 .size = DT\_PROP\_BY\_IDX(mspi\_dev, xip\_config, 2), \

84 .permission = DT\_PROP\_BY\_IDX(mspi\_dev, xip\_config, 3), \

85 }

86

[ 96](group__mspi__devicetree.md#ga24a88651c634c5ab5630e7844ff98e4b)#define MSPI\_XIP\_CONFIG\_DT(mspi\_dev) \

97 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(mspi\_dev, xip\_config), \

98 (MSPI\_XIP\_CONFIG\_DT\_NO\_CHECK(mspi\_dev)), \

99 ({}))

100

[ 109](group__mspi__devicetree.md#gafe739210f9f5cab4ab71bd61ec5af03f)#define MSPI\_XIP\_CONFIG\_DT\_INST(inst) MSPI\_XIP\_CONFIG\_DT(DT\_DRV\_INST(inst))

110

[ 120](group__mspi__devicetree.md#gad1f36df770167384cc4e3f2c9be07d34)#define MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK(mspi\_dev) \

121 { \

122 .enable = DT\_PROP\_BY\_IDX(mspi\_dev, scramble\_config, 0), \

123 .address\_offset = DT\_PROP\_BY\_IDX(mspi\_dev, scramble\_config, 1), \

124 .size = DT\_PROP\_BY\_IDX(mspi\_dev, scramble\_config, 2), \

125 }

126

[ 136](group__mspi__devicetree.md#ga10ee161794b5c7986a4411b8fc90ea7d)#define MSPI\_SCRAMBLE\_CONFIG\_DT(mspi\_dev) \

137 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(mspi\_dev, scramble\_config), \

138 (MSPI\_SCRAMBLE\_CONFIG\_DT\_NO\_CHECK(mspi\_dev)), \

139 ({}))

140

[ 149](group__mspi__devicetree.md#gaa9b32a8f6984468b5198524bea42ed8c)#define MSPI\_SCRAMBLE\_CONFIG\_DT\_INST(inst) MSPI\_SCRAMBLE\_CONFIG\_DT(DT\_DRV\_INST(inst))

150

[ 160](group__mspi__devicetree.md#gafa7c0d76c85a31004d72392016da1246)#define MSPI\_DEVICE\_ID\_DT(mspi\_dev) \

161 { \

162 .ce = MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET(mspi\_dev), \

163 .dev\_idx = DT\_REG\_ADDR(mspi\_dev), \

164 }

165

[ 174](group__mspi__devicetree.md#gabfd0d3beb91762e939636c87a91a6673)#define MSPI\_DEVICE\_ID\_DT\_INST(inst) MSPI\_DEVICE\_ID\_DT(DT\_DRV\_INST(inst))

175

176

[ 214](group__mspi__devicetree.md#ga0a91ef9392be4493ede6cea607ee8728)#define MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET(mspi\_dev) \

215 GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(DT\_BUS(mspi\_dev), ce\_gpios, DT\_REG\_ADDR(mspi\_dev), {})

216

[ 226](group__mspi__devicetree.md#ga0b98f7a625324abce90933cb2395fb17)#define MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_INST\_GET(inst) \

227 MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

228

229

[ 240](group__mspi__devicetree.md#ga1ca28d7ead69cd3a5e26198bc6815b54)#define MSPI\_CE\_GPIOS\_DT\_SPEC\_GET(node\_id) \

241{ \

242 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, ce\_gpios), \

243 (DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, ce\_gpios, GPIO\_DT\_SPEC\_GET\_BY\_IDX, (,))), \

244 ()) \

245}

246

[ 256](group__mspi__devicetree.md#ga5ae4bd8071da4babd0bdf9767e9542e4)#define MSPI\_CE\_GPIOS\_DT\_SPEC\_INST\_GET(inst) \

257 MSPI\_CE\_GPIOS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))

258

[ 297](group__mspi__devicetree.md#ga501b2e19e358083f2b47838cde58a676)#define MSPI\_CE\_CONTROL\_INIT(node\_id, delay\_) \

298 { \

299 .gpio = MSPI\_DEV\_CE\_GPIOS\_DT\_SPEC\_GET(node\_id), .delay = (delay\_), \

300 }

301

[ 315](group__mspi__devicetree.md#gacec91c9080052adf96aa5d36c6301d8c)#define MSPI\_CE\_CONTROL\_INIT\_INST(inst, delay\_) MSPI\_CE\_CONTROL\_INIT(DT\_DRV\_INST(inst), delay\_)

316

317#ifdef \_\_cplusplus

318}

319#endif

320

324

325#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MSPI\_DEVICETREE\_H\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mspi](dir_288d6185a21193ccd9a81f08240fb63b.md)
- [devicetree.h](drivers_2mspi_2devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
