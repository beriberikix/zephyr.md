---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensing__sensor_8h_source.html
original_path: doxygen/html/sensing__sensor_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor.h

[Go to the documentation of this file.](sensing__sensor_8h.md)

1/\*

2 \* Copyright (c) 2022-2023 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SENSING\_SENSOR\_H\_

8#define ZEPHYR\_INCLUDE\_SENSING\_SENSOR\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11#include <[zephyr/device.h](device_8h.md)>

12#include <[zephyr/drivers/sensor.h](sensor_8h.md)>

13#include <[zephyr/sensing/sensing.h](sensing_8h.md)>

14

21

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 36](structsensing__sensor__register__info.md)struct [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md) {

[ 40](structsensing__sensor__register__info.md#a6300055172c8692b8313adcef5507d41) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structsensing__sensor__register__info.md#a6300055172c8692b8313adcef5507d41);

41

[ 46](structsensing__sensor__register__info.md#a133621dcf1da9c9ffd111eeec007f220) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sample\_size](structsensing__sensor__register__info.md#a133621dcf1da9c9ffd111eeec007f220);

47

[ 51](structsensing__sensor__register__info.md#aab10e29faf4e3a6bcc33d99119bb8bc9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sensitivity\_count](structsensing__sensor__register__info.md#aab10e29faf4e3a6bcc33d99119bb8bc9);

52

[ 57](structsensing__sensor__register__info.md#af87ee2748229a7f43049d058da930ce1) struct [sensing\_sensor\_version](structsensing__sensor__version.md) [version](structsensing__sensor__register__info.md#af87ee2748229a7f43049d058da930ce1);

58};

59

61

67enum {

68 EVENT\_CONFIG\_READY,

69};

70

76enum {

77 SENSOR\_LATER\_CFG\_BIT,

78};

79

83struct sensing\_connection {

84 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) snode;

85 struct sensing\_sensor \*source;

86 struct sensing\_sensor \*sink;

87 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) interval;

89 int sensitivity[CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT];

90 void \*data;

92 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) next\_consume\_time;

93 struct sensing\_callback\_list \*callback\_list;

94};

95

105struct sensing\_sensor {

106 const struct device \*dev;

107 const struct sensing\_sensor\_info \*info;

109 const struct sensing\_sensor\_register\_info \*register\_info;

110 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reporter\_num;

111 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) client\_list;

112 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) interval;

113 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensitivity\_count;

115 int sensitivity[CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT];

116 enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

117 struct rtio\_iodev \*iodev;

118 struct k\_timer timer;

119 struct rtio\_sqe \*stream\_sqe;

120 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) flag;

121 struct sensing\_connection \*conns;

122};

123

132#define SENSING\_SENSOR\_INFO\_NAME(node, idx) \

133 \_CONCAT(\_CONCAT(\_\_sensing\_sensor\_info\_, idx), DEVICE\_DT\_NAME\_GET(node))

134

145#define SENSING\_SENSOR\_INFO\_DEFINE(node, idx) \

146 const static STRUCT\_SECTION\_ITERABLE(sensing\_sensor\_info, \

147 SENSING\_SENSOR\_INFO\_NAME(node, idx)) = { \

148 .type = DT\_PROP\_BY\_IDX(node, sensor\_types, idx), \

149 .name = DT\_NODE\_FULL\_NAME(node), \

150 .friendly\_name = DT\_PROP(node, friendly\_name), \

151 .vendor = DT\_NODE\_VENDOR\_OR(node, NULL), \

152 .model = DT\_NODE\_MODEL\_OR(node, NULL), \

153 .minimal\_interval = DT\_PROP(node, minimal\_interval), \

154 };

155

163#define SENSING\_CONNECTIONS\_NAME(node) \

164 \_CONCAT(\_\_sensing\_connections\_, DEVICE\_DT\_NAME\_GET(node))

165

174#define SENSING\_SENSOR\_SOURCE\_NAME(idx, node) \

175 SENSING\_SENSOR\_NAME(DT\_PHANDLE\_BY\_IDX(node, reporters, idx), \

176 DT\_PROP\_BY\_IDX(node, reporters\_index, idx))

177

186#define SENSING\_SENSOR\_SOURCE\_EXTERN(idx, node) \

187extern struct sensing\_sensor SENSING\_SENSOR\_SOURCE\_NAME(idx, node);

188

197#define SENSING\_CONNECTION\_INITIALIZER(source\_name, cb\_list\_ptr) \

198{ \

199 .callback\_list = cb\_list\_ptr, \

200 .source = &source\_name, \

201}

202

212#define SENSING\_CONNECTION\_DEFINE(idx, node, cb\_list\_ptr) \

213 SENSING\_CONNECTION\_INITIALIZER(SENSING\_SENSOR\_SOURCE\_NAME(idx, node), \

214 cb\_list\_ptr)

215

226#define SENSING\_CONNECTIONS\_DEFINE(node, num, cb\_list\_ptr) \

227 LISTIFY(num, SENSING\_SENSOR\_SOURCE\_EXTERN, \

228 (), node) \

229 static struct sensing\_connection \

230 SENSING\_CONNECTIONS\_NAME(node)[(num)] = { \

231 LISTIFY(num, SENSING\_CONNECTION\_DEFINE, \

232 (,), node, cb\_list\_ptr) \

233 };

234

241struct sensing\_submit\_config {

242 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan;

243 const int info\_index;

244 const bool is\_streaming;

245};

246

252extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \_\_sensing\_iodev\_api;

253

262#define SENSING\_SUBMIT\_CFG\_NAME(node, idx) \

263 \_CONCAT(\_CONCAT(\_\_sensing\_submit\_cfg\_, idx), DEVICE\_DT\_NAME\_GET(node))

264

273#define SENSING\_SENSOR\_IODEV\_NAME(node, idx) \

274 \_CONCAT(\_CONCAT(\_\_sensing\_iodev\_, idx), DEVICE\_DT\_NAME\_GET(node))

275

285#define SENSING\_SENSOR\_IODEV\_DEFINE(node, idx) \

286 static struct sensing\_submit\_config SENSING\_SUBMIT\_CFG\_NAME(node, idx) = { \

287 .is\_streaming = DT\_PROP(node, stream\_mode), \

288 .info\_index = idx, \

289 }; \

290 RTIO\_IODEV\_DEFINE(SENSING\_SENSOR\_IODEV\_NAME(node, idx), \

291 &\_\_sensing\_iodev\_api, \

292 &SENSING\_SUBMIT\_CFG\_NAME(node, idx));

293

302#define SENSING\_SENSOR\_NAME(node, idx) \

303 \_CONCAT(\_CONCAT(\_\_sensing\_sensor\_, idx), DEVICE\_DT\_NAME\_GET(node))

304

318#define SENSING\_SENSOR\_DEFINE(node, prop, idx, reg\_ptr, cb\_list\_ptr) \

319 SENSING\_SENSOR\_INFO\_DEFINE(node, idx) \

320 SENSING\_SENSOR\_IODEV\_DEFINE(node, idx) \

321 STRUCT\_SECTION\_ITERABLE(sensing\_sensor, \

322 SENSING\_SENSOR\_NAME(node, idx)) = { \

323 .dev = DEVICE\_DT\_GET(node), \

324 .info = &SENSING\_SENSOR\_INFO\_NAME(node, idx), \

325 .register\_info = reg\_ptr, \

326 .reporter\_num = DT\_PROP\_LEN\_OR(node, reporters, 0), \

327 .conns = SENSING\_CONNECTIONS\_NAME(node), \

328 .iodev = &SENSING\_SENSOR\_IODEV\_NAME(node, idx), \

329 };

330

341#define SENSING\_SENSORS\_DEFINE(node, reg\_ptr, cb\_list\_ptr) \

342 DT\_FOREACH\_PROP\_ELEM\_VARGS(node, sensor\_types, \

343 SENSING\_SENSOR\_DEFINE, reg\_ptr, cb\_list\_ptr)

344

346

[ 369](group__sensing__sensor.md#gad5a9ccb04d96efc57078e880ca28b654)#define SENSING\_SENSORS\_DT\_DEFINE(node, reg\_ptr, cb\_list\_ptr, \

370 init\_fn, pm\_device, \

371 data\_ptr, cfg\_ptr, level, prio, \

372 api\_ptr, ...) \

373 SENSOR\_DEVICE\_DT\_DEFINE(node, init\_fn, pm\_device, \

374 data\_ptr, cfg\_ptr, level, prio, \

375 api\_ptr, \_\_VA\_ARGS\_\_); \

376 SENSING\_CONNECTIONS\_DEFINE(node, \

377 DT\_PROP\_LEN\_OR(node, reporters, 0), \

378 cb\_list\_ptr); \

379 SENSING\_SENSORS\_DEFINE(node, reg\_ptr, cb\_list\_ptr);

380

[ 389](group__sensing__sensor.md#gae3c7a2acba53cc524a4b1043df49fe85)#define SENSING\_SENSORS\_DT\_INST\_DEFINE(inst, ...) \

390 SENSING\_SENSORS\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

391

[ 404](group__sensing__sensor.md#gab4c41d02b3731e5829a41e1f5f5154a5)int [sensing\_sensor\_get\_reporters](group__sensing__sensor.md#gab4c41d02b3731e5829a41e1f5f5154a5)(

405 const struct [device](structdevice.md) \*dev, int type,

406 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*reporter\_handles, int max\_handles);

407

[ 415](group__sensing__sensor.md#ga2c5cfb298b2dfde967edfdd987115021)int [sensing\_sensor\_get\_reporters\_count](group__sensing__sensor.md#ga2c5cfb298b2dfde967edfdd987115021)(

416 const struct [device](structdevice.md) \*dev, int type);

417

[ 425](group__sensing__sensor.md#gab9446a3085b6b05da448dce59db50387)int [sensing\_sensor\_get\_state](group__sensing__sensor.md#gab9446a3085b6b05da448dce59db50387)(

426 const struct [device](structdevice.md) \*dev,

427 enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

428

432

433#ifdef \_\_cplusplus

434}

435#endif

436

437#endif /\*ZEPHYR\_INCLUDE\_SENSING\_SENSOR\_H\_\*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06)

sensing\_sensor\_state

Sensing subsystem sensor state.

**Definition** sensing.h:89

[sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293)

void \* sensing\_sensor\_handle\_t

Define Sensing subsystem sensor handle.

**Definition** sensing.h:113

[sensing\_sensor\_get\_reporters\_count](group__sensing__sensor.md#ga2c5cfb298b2dfde967edfdd987115021)

int sensing\_sensor\_get\_reporters\_count(const struct device \*dev, int type)

Get reporters count of a given sensor instance by sensor type.

[sensing\_sensor\_get\_reporters](group__sensing__sensor.md#gab4c41d02b3731e5829a41e1f5f5154a5)

int sensing\_sensor\_get\_reporters(const struct device \*dev, int type, sensing\_sensor\_handle\_t \*reporter\_handles, int max\_handles)

Get reporter handles of a given sensor instance by sensor type.

[sensing\_sensor\_get\_state](group__sensing__sensor.md#gab9446a3085b6b05da448dce59db50387)

int sensing\_sensor\_get\_state(const struct device \*dev, enum sensing\_sensor\_state \*state)

Get this sensor's state.

[sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)

sensor\_channel

Sensor channels.

**Definition** sensor.h:61

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[sensing.h](sensing_8h.md)

[sensor.h](sensor_8h.md)

Public APIs for the sensor driver.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:502

[sensing\_sensor\_register\_info](structsensing__sensor__register__info.md)

Sensor registration information.

**Definition** sensing\_sensor.h:36

[sensing\_sensor\_register\_info::sample\_size](structsensing__sensor__register__info.md#a133621dcf1da9c9ffd111eeec007f220)

uint16\_t sample\_size

Sample size in bytes for a single sample of the registered sensor.

**Definition** sensing\_sensor.h:46

[sensing\_sensor\_register\_info::flags](structsensing__sensor__register__info.md#a6300055172c8692b8313adcef5507d41)

uint16\_t flags

Sensor flags.

**Definition** sensing\_sensor.h:40

[sensing\_sensor\_register\_info::sensitivity\_count](structsensing__sensor__register__info.md#aab10e29faf4e3a6bcc33d99119bb8bc9)

uint8\_t sensitivity\_count

The number of sensor sensitivities.

**Definition** sensing\_sensor.h:51

[sensing\_sensor\_register\_info::version](structsensing__sensor__register__info.md#af87ee2748229a7f43049d058da930ce1)

struct sensing\_sensor\_version version

Sensor version.

**Definition** sensing\_sensor.h:57

[sensing\_sensor\_version](structsensing__sensor__version.md)

Sensor Version.

**Definition** sensing.h:39

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sensing](dir_89ae873b54fa3664e4a65bb9dc3973c9.md)
- [sensing\_sensor.h](sensing__sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
