---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sensing__sensor_8h_source.html
original_path: doxygen/html/sensing__sensor_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

60enum {

[ 61](group__sensing__sensor.md#ggaafa611add600aa3b2fba2c3e08562a02a78480d5dce2873492e587176880531d8) [EVENT\_CONFIG\_READY](group__sensing__sensor.md#ggaafa611add600aa3b2fba2c3e08562a02a78480d5dce2873492e587176880531d8),

62};

63

64enum {

[ 65](group__sensing__sensor.md#ggaf3548dcc45caf8e64b2ecec463bea7e6a079aade4a76672cd9a96d777534fb584) [SENSOR\_LATER\_CFG\_BIT](group__sensing__sensor.md#ggaf3548dcc45caf8e64b2ecec463bea7e6a079aade4a76672cd9a96d777534fb584),

66};

67

[ 71](structsensing__connection.md)struct [sensing\_connection](structsensing__connection.md) {

[ 72](structsensing__connection.md#a0ed58bb9a5227c6113c9eb4e5568729b) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [snode](structsensing__connection.md#a0ed58bb9a5227c6113c9eb4e5568729b);

[ 73](structsensing__connection.md#ab5cb1fd5ed2de2bf7a41143fc4cdc51b) struct [sensing\_sensor](structsensing__sensor.md) \*[source](structsensing__connection.md#ab5cb1fd5ed2de2bf7a41143fc4cdc51b);

[ 74](structsensing__connection.md#a79223ce36e160a3f2b8adffccaf7fb09) struct [sensing\_sensor](structsensing__sensor.md) \*[sink](structsensing__connection.md#a79223ce36e160a3f2b8adffccaf7fb09);

75 /\* interval and sensitivity set from client(sink) to reporter(source) \*/

[ 76](structsensing__connection.md#a9c6a1b8bc3c5b80d2368fb01b316391c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval](structsensing__connection.md#a9c6a1b8bc3c5b80d2368fb01b316391c);

[ 77](structsensing__connection.md#a1c831b73840d686b742b90eebaf42083) int [sensitivity](structsensing__connection.md#a1c831b73840d686b742b90eebaf42083)[CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT];

78 /\* copy sensor data to connection data buf from reporter \*/

[ 79](structsensing__connection.md#a3d3d6463ff7c6a142657c6a8b016ea53) void \*[data](structsensing__connection.md#a3d3d6463ff7c6a142657c6a8b016ea53);

80 /\* client(sink) next consume time \*/

[ 81](structsensing__connection.md#ae3d82838cca620f234d3a4638c91d61a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [next\_consume\_time](structsensing__connection.md#ae3d82838cca620f234d3a4638c91d61a);

82 /\* post data to application \*/

[ 83](structsensing__connection.md#a3ab7dc6ce305b594661e5ab9dbfa0512) struct [sensing\_callback\_list](structsensing__callback__list.md) \*[callback\_list](structsensing__connection.md#a3ab7dc6ce305b594661e5ab9dbfa0512);

84};

85

[ 95](structsensing__sensor.md)struct [sensing\_sensor](structsensing__sensor.md) {

[ 96](structsensing__sensor.md#a08f7ce5927273e550e095b86d21c9abd) const struct [device](structdevice.md) \*[dev](structsensing__sensor.md#a08f7ce5927273e550e095b86d21c9abd);

[ 97](structsensing__sensor.md#aee23cc4afccaf3cbbbe00afa54575098) const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*[info](structsensing__sensor.md#aee23cc4afccaf3cbbbe00afa54575098);

[ 98](structsensing__sensor.md#ad87ede91d87dac49cc53a91cf08c6565) const struct [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md) \*[register\_info](structsensing__sensor.md#ad87ede91d87dac49cc53a91cf08c6565);

[ 99](structsensing__sensor.md#a229ec163e8e8f3842495ab039e869ca9) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reporter\_num](structsensing__sensor.md#a229ec163e8e8f3842495ab039e869ca9);

[ 100](structsensing__sensor.md#a0874639b380cce49fb8a9bd9ae2dd68d) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [client\_list](structsensing__sensor.md#a0874639b380cce49fb8a9bd9ae2dd68d);

[ 101](structsensing__sensor.md#a1f975314ddbaec330a284d0865946f85) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval](structsensing__sensor.md#a1f975314ddbaec330a284d0865946f85);

[ 102](structsensing__sensor.md#aa21babb895f8aca56d415e862d4b79f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sensitivity\_count](structsensing__sensor.md#aa21babb895f8aca56d415e862d4b79f7);

[ 103](structsensing__sensor.md#a2bba0047276fbb6b3586f301ec9d5e8c) int [sensitivity](structsensing__sensor.md#a2bba0047276fbb6b3586f301ec9d5e8c)[CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT];

[ 104](structsensing__sensor.md#aa7d285c1c281f0c3ab8fc1d8ad8fea5b) enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) [state](structsensing__sensor.md#aa7d285c1c281f0c3ab8fc1d8ad8fea5b);

105 /\* runtime info \*/

[ 106](structsensing__sensor.md#aa62ec63a776d0debd76acee9b7459712) struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structsensing__sensor.md#aa62ec63a776d0debd76acee9b7459712);

[ 107](structsensing__sensor.md#a7e28a435642cafa2641b84186d28e21f) struct k\_timer [timer](structsensing__sensor.md#a7e28a435642cafa2641b84186d28e21f);

[ 108](structsensing__sensor.md#ab8d7a1a062241fd56e94defd13357302) struct [rtio\_sqe](structrtio__sqe.md) \*[stream\_sqe](structsensing__sensor.md#ab8d7a1a062241fd56e94defd13357302);

[ 109](structsensing__sensor.md#af8ae1aaef2e5d96cf00145901124f6aa) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flag](structsensing__sensor.md#af8ae1aaef2e5d96cf00145901124f6aa);

[ 110](structsensing__sensor.md#a7a10e55364207ff3e6464784933c874f) struct [sensing\_connection](structsensing__connection.md) \*[conns](structsensing__sensor.md#a7a10e55364207ff3e6464784933c874f);

111};

112

[ 113](group__sensing__sensor.md#ga4a11557e9d28c75e67f2d21af8dd24d7)#define SENSING\_SENSOR\_INFO\_NAME(node, idx) \

114 \_CONCAT(\_CONCAT(\_\_sensing\_sensor\_info\_, idx), DEVICE\_DT\_NAME\_GET(node))

115

[ 116](group__sensing__sensor.md#ga46b8830de0d42506c8804307c515c00b)#define SENSING\_SENSOR\_INFO\_DEFINE(node, idx) \

117 const static STRUCT\_SECTION\_ITERABLE(sensing\_sensor\_info, \

118 SENSING\_SENSOR\_INFO\_NAME(node, idx)) = { \

119 .type = DT\_PROP\_BY\_IDX(node, sensor\_types, idx), \

120 .name = DT\_NODE\_FULL\_NAME(node), \

121 .friendly\_name = DT\_PROP(node, friendly\_name), \

122 .vendor = DT\_NODE\_VENDOR\_OR(node, NULL), \

123 .model = DT\_NODE\_MODEL\_OR(node, NULL), \

124 .minimal\_interval = DT\_PROP(node, minimal\_interval),\

125 };

126

[ 127](group__sensing__sensor.md#ga11f2d720e050f2212b67f2e11fa9677b)#define SENSING\_CONNECTIONS\_NAME(node) \

128 \_CONCAT(\_\_sensing\_connections\_, DEVICE\_DT\_NAME\_GET(node))

129

[ 130](group__sensing__sensor.md#ga256546e178d1b2e507cb862876fec2d0)#define SENSING\_SENSOR\_SOURCE\_NAME(idx, node) \

131 SENSING\_SENSOR\_NAME(DT\_PHANDLE\_BY\_IDX(node, reporters, idx), \

132 DT\_PROP\_BY\_IDX(node, reporters\_index, idx))

133

[ 134](group__sensing__sensor.md#ga3df3d46d0102ec114d9125dcb1474745)#define SENSING\_SENSOR\_SOURCE\_EXTERN(idx, node) \

135extern struct sensing\_sensor SENSING\_SENSOR\_SOURCE\_NAME(idx, node); \

136

[ 137](group__sensing__sensor.md#ga11ddd317f3aef5edc0f80bad11738612)#define SENSING\_CONNECTION\_INITIALIZER(source\_name, cb\_list\_ptr) \

138{ \

139 .callback\_list = cb\_list\_ptr, \

140 .source = &source\_name, \

141}

142

[ 143](group__sensing__sensor.md#ga791ffbf312fa2eae23350cd9add0afc3)#define SENSING\_CONNECTION\_DEFINE(idx, node, cb\_list\_ptr) \

144 SENSING\_CONNECTION\_INITIALIZER(SENSING\_SENSOR\_SOURCE\_NAME(idx, node), \

145 cb\_list\_ptr)

146

[ 147](group__sensing__sensor.md#ga5c932e7be9361293a7b5ff3124e9799d)#define SENSING\_CONNECTIONS\_DEFINE(node, num, cb\_list\_ptr) \

148 LISTIFY(num, SENSING\_SENSOR\_SOURCE\_EXTERN, \

149 (), node) \

150 static struct sensing\_connection \

151 SENSING\_CONNECTIONS\_NAME(node)[(num)] = { \

152 LISTIFY(num, SENSING\_CONNECTION\_DEFINE, \

153 (,), node, cb\_list\_ptr) \

154 };

155

[ 156](structsensing__submit__config.md)struct [sensing\_submit\_config](structsensing__submit__config.md) {

[ 157](structsensing__submit__config.md#a0004665cd7148289867fff549fbdc1b0) enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) [chan](structsensing__submit__config.md#a0004665cd7148289867fff549fbdc1b0);

[ 158](structsensing__submit__config.md#a7a27243955ba545d98d5d18954c80520) const int [info\_index](structsensing__submit__config.md#a7a27243955ba545d98d5d18954c80520);

[ 159](structsensing__submit__config.md#a4672af546d2c8f25baf1a0691a26e94c) const bool [is\_streaming](structsensing__submit__config.md#a4672af546d2c8f25baf1a0691a26e94c);

160};

161

162extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \_\_sensing\_iodev\_api;

163

[ 164](group__sensing__sensor.md#gaa0c5eb169a6e3922c091a4bf6ff82478)#define SENSING\_SUBMIT\_CFG\_NAME(node, idx) \

165 \_CONCAT(\_CONCAT(\_\_sensing\_submit\_cfg\_, idx), DEVICE\_DT\_NAME\_GET(node))

166

[ 167](group__sensing__sensor.md#ga8c15780ceb1988ab7192c3c3ca70ac82)#define SENSING\_SENSOR\_IODEV\_NAME(node, idx) \

168 \_CONCAT(\_CONCAT(\_\_sensing\_iodev\_, idx), DEVICE\_DT\_NAME\_GET(node))

169

[ 170](group__sensing__sensor.md#gafd8cbf368e9fa541ce67013d0e8624f2)#define SENSING\_SENSOR\_IODEV\_DEFINE(node, idx) \

171 static struct sensing\_submit\_config SENSING\_SUBMIT\_CFG\_NAME(node, idx) = { \

172 .is\_streaming = DT\_PROP(node, stream\_mode), \

173 .info\_index = idx, \

174 }; \

175 RTIO\_IODEV\_DEFINE(SENSING\_SENSOR\_IODEV\_NAME(node, idx), \

176 &\_\_sensing\_iodev\_api, \

177 &SENSING\_SUBMIT\_CFG\_NAME(node, idx));

178

[ 179](group__sensing__sensor.md#ga4f8a39411260fbfd55258241de9bbb37)#define SENSING\_SENSOR\_NAME(node, idx) \

180 \_CONCAT(\_CONCAT(\_\_sensing\_sensor\_, idx), DEVICE\_DT\_NAME\_GET(node))

181

[ 182](group__sensing__sensor.md#gae3588d8dce25ad800bf0633f1b3c6bf7)#define SENSING\_SENSOR\_DEFINE(node, prop, idx, reg\_ptr, cb\_list\_ptr) \

183 SENSING\_SENSOR\_INFO\_DEFINE(node, idx) \

184 SENSING\_SENSOR\_IODEV\_DEFINE(node, idx) \

185 STRUCT\_SECTION\_ITERABLE(sensing\_sensor, \

186 SENSING\_SENSOR\_NAME(node, idx)) = { \

187 .dev = DEVICE\_DT\_GET(node), \

188 .info = &SENSING\_SENSOR\_INFO\_NAME(node, idx), \

189 .register\_info = reg\_ptr, \

190 .reporter\_num = DT\_PROP\_LEN\_OR(node, reporters, 0), \

191 .conns = SENSING\_CONNECTIONS\_NAME(node), \

192 .iodev = &SENSING\_SENSOR\_IODEV\_NAME(node, idx), \

193 };

194

[ 195](group__sensing__sensor.md#ga6fd18be5f503ad4a744df6583495c3fe)#define SENSING\_SENSORS\_DEFINE(node, reg\_ptr, cb\_list\_ptr) \

196 DT\_FOREACH\_PROP\_ELEM\_VARGS(node, sensor\_types, \

197 SENSING\_SENSOR\_DEFINE, reg\_ptr, cb\_list\_ptr)

198

[ 229](group__sensing__sensor.md#gad5a9ccb04d96efc57078e880ca28b654)#define SENSING\_SENSORS\_DT\_DEFINE(node, reg\_ptr, cb\_list\_ptr, \

230 init\_fn, pm\_device, \

231 data\_ptr, cfg\_ptr, level, prio, \

232 api\_ptr, ...) \

233 SENSOR\_DEVICE\_DT\_DEFINE(node, init\_fn, pm\_device, \

234 data\_ptr, cfg\_ptr, level, prio, \

235 api\_ptr, \_\_VA\_ARGS\_\_); \

236 SENSING\_CONNECTIONS\_DEFINE(node, \

237 DT\_PROP\_LEN\_OR(node, reporters, 0), \

238 cb\_list\_ptr); \

239 SENSING\_SENSORS\_DEFINE(node, reg\_ptr, cb\_list\_ptr);

240

[ 250](group__sensing__sensor.md#gae3c7a2acba53cc524a4b1043df49fe85)#define SENSING\_SENSORS\_DT\_INST\_DEFINE(inst, ...) \

251 SENSING\_SENSORS\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

252

[ 269](group__sensing__sensor.md#gab4c41d02b3731e5829a41e1f5f5154a5)int [sensing\_sensor\_get\_reporters](group__sensing__sensor.md#gab4c41d02b3731e5829a41e1f5f5154a5)(

270 const struct [device](structdevice.md) \*dev, int type,

271 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*reporter\_handles, int max\_handles);

272

[ 282](group__sensing__sensor.md#ga2c5cfb298b2dfde967edfdd987115021)int [sensing\_sensor\_get\_reporters\_count](group__sensing__sensor.md#ga2c5cfb298b2dfde967edfdd987115021)(

283 const struct [device](structdevice.md) \*dev, int type);

284

[ 294](group__sensing__sensor.md#gab9446a3085b6b05da448dce59db50387)int [sensing\_sensor\_get\_state](group__sensing__sensor.md#gab9446a3085b6b05da448dce59db50387)(

295 const struct [device](structdevice.md) \*dev,

296 enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

297

301

302#ifdef \_\_cplusplus

303}

304#endif

305

306#endif /\*ZEPHYR\_INCLUDE\_SENSING\_SENSOR\_H\_\*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06)

sensing\_sensor\_state

Sensing subsystem sensor state.

**Definition** sensing.h:85

[sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293)

void \* sensing\_sensor\_handle\_t

Define Sensing subsystem sensor handle.

**Definition** sensing.h:106

[sensing\_sensor\_get\_reporters\_count](group__sensing__sensor.md#ga2c5cfb298b2dfde967edfdd987115021)

int sensing\_sensor\_get\_reporters\_count(const struct device \*dev, int type)

Get reporters count of a given sensor instance by sensor type.

[sensing\_sensor\_get\_reporters](group__sensing__sensor.md#gab4c41d02b3731e5829a41e1f5f5154a5)

int sensing\_sensor\_get\_reporters(const struct device \*dev, int type, sensing\_sensor\_handle\_t \*reporter\_handles, int max\_handles)

Get reporter handles of a given sensor instance by sensor type.

[sensing\_sensor\_get\_state](group__sensing__sensor.md#gab9446a3085b6b05da448dce59db50387)

int sensing\_sensor\_get\_state(const struct device \*dev, enum sensing\_sensor\_state \*state)

Get this sensor's state.

[EVENT\_CONFIG\_READY](group__sensing__sensor.md#ggaafa611add600aa3b2fba2c3e08562a02a78480d5dce2873492e587176880531d8)

@ EVENT\_CONFIG\_READY

**Definition** sensing\_sensor.h:61

[SENSOR\_LATER\_CFG\_BIT](group__sensing__sensor.md#ggaf3548dcc45caf8e64b2ecec463bea7e6a079aade4a76672cd9a96d777534fb584)

@ SENSOR\_LATER\_CFG\_BIT

**Definition** sensing\_sensor.h:65

[sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)

sensor\_channel

Sensor channels.

**Definition** sensor.h:59

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

**Definition** device.h:387

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:429

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:444

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:230

[sensing\_callback\_list](structsensing__callback__list.md)

Sensing subsystem event callback list.

**Definition** sensing.h:151

[sensing\_connection](structsensing__connection.md)

Connection between a source and sink of sensor data.

**Definition** sensing\_sensor.h:71

[sensing\_connection::snode](structsensing__connection.md#a0ed58bb9a5227c6113c9eb4e5568729b)

sys\_snode\_t snode

**Definition** sensing\_sensor.h:72

[sensing\_connection::sensitivity](structsensing__connection.md#a1c831b73840d686b742b90eebaf42083)

int sensitivity[CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT]

**Definition** sensing\_sensor.h:77

[sensing\_connection::callback\_list](structsensing__connection.md#a3ab7dc6ce305b594661e5ab9dbfa0512)

struct sensing\_callback\_list \* callback\_list

**Definition** sensing\_sensor.h:83

[sensing\_connection::data](structsensing__connection.md#a3d3d6463ff7c6a142657c6a8b016ea53)

void \* data

**Definition** sensing\_sensor.h:79

[sensing\_connection::sink](structsensing__connection.md#a79223ce36e160a3f2b8adffccaf7fb09)

struct sensing\_sensor \* sink

**Definition** sensing\_sensor.h:74

[sensing\_connection::interval](structsensing__connection.md#a9c6a1b8bc3c5b80d2368fb01b316391c)

uint32\_t interval

**Definition** sensing\_sensor.h:76

[sensing\_connection::source](structsensing__connection.md#ab5cb1fd5ed2de2bf7a41143fc4cdc51b)

struct sensing\_sensor \* source

**Definition** sensing\_sensor.h:73

[sensing\_connection::next\_consume\_time](structsensing__connection.md#ae3d82838cca620f234d3a4638c91d61a)

uint64\_t next\_consume\_time

**Definition** sensing\_sensor.h:81

[sensing\_sensor\_info](structsensing__sensor__info.md)

Sensor basic constant information.

**Definition** sensing.h:126

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

[sensing\_sensor](structsensing__sensor.md)

Internal sensor instance data structure.

**Definition** sensing\_sensor.h:95

[sensing\_sensor::client\_list](structsensing__sensor.md#a0874639b380cce49fb8a9bd9ae2dd68d)

sys\_slist\_t client\_list

**Definition** sensing\_sensor.h:100

[sensing\_sensor::dev](structsensing__sensor.md#a08f7ce5927273e550e095b86d21c9abd)

const struct device \* dev

**Definition** sensing\_sensor.h:96

[sensing\_sensor::interval](structsensing__sensor.md#a1f975314ddbaec330a284d0865946f85)

uint32\_t interval

**Definition** sensing\_sensor.h:101

[sensing\_sensor::reporter\_num](structsensing__sensor.md#a229ec163e8e8f3842495ab039e869ca9)

const uint16\_t reporter\_num

**Definition** sensing\_sensor.h:99

[sensing\_sensor::sensitivity](structsensing__sensor.md#a2bba0047276fbb6b3586f301ec9d5e8c)

int sensitivity[CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT]

**Definition** sensing\_sensor.h:103

[sensing\_sensor::conns](structsensing__sensor.md#a7a10e55364207ff3e6464784933c874f)

struct sensing\_connection \* conns

**Definition** sensing\_sensor.h:110

[sensing\_sensor::timer](structsensing__sensor.md#a7e28a435642cafa2641b84186d28e21f)

struct k\_timer timer

**Definition** sensing\_sensor.h:107

[sensing\_sensor::sensitivity\_count](structsensing__sensor.md#aa21babb895f8aca56d415e862d4b79f7)

uint8\_t sensitivity\_count

**Definition** sensing\_sensor.h:102

[sensing\_sensor::iodev](structsensing__sensor.md#aa62ec63a776d0debd76acee9b7459712)

struct rtio\_iodev \* iodev

**Definition** sensing\_sensor.h:106

[sensing\_sensor::state](structsensing__sensor.md#aa7d285c1c281f0c3ab8fc1d8ad8fea5b)

enum sensing\_sensor\_state state

**Definition** sensing\_sensor.h:104

[sensing\_sensor::stream\_sqe](structsensing__sensor.md#ab8d7a1a062241fd56e94defd13357302)

struct rtio\_sqe \* stream\_sqe

**Definition** sensing\_sensor.h:108

[sensing\_sensor::register\_info](structsensing__sensor.md#ad87ede91d87dac49cc53a91cf08c6565)

const struct sensing\_sensor\_register\_info \* register\_info

**Definition** sensing\_sensor.h:98

[sensing\_sensor::info](structsensing__sensor.md#aee23cc4afccaf3cbbbe00afa54575098)

const struct sensing\_sensor\_info \* info

**Definition** sensing\_sensor.h:97

[sensing\_sensor::flag](structsensing__sensor.md#af8ae1aaef2e5d96cf00145901124f6aa)

atomic\_t flag

**Definition** sensing\_sensor.h:109

[sensing\_submit\_config](structsensing__submit__config.md)

**Definition** sensing\_sensor.h:156

[sensing\_submit\_config::chan](structsensing__submit__config.md#a0004665cd7148289867fff549fbdc1b0)

enum sensor\_channel chan

**Definition** sensing\_sensor.h:157

[sensing\_submit\_config::is\_streaming](structsensing__submit__config.md#a4672af546d2c8f25baf1a0691a26e94c)

const bool is\_streaming

**Definition** sensing\_sensor.h:159

[sensing\_submit\_config::info\_index](structsensing__submit__config.md#a7a27243955ba545d98d5d18954c80520)

const int info\_index

**Definition** sensing\_sensor.h:158

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sensing](dir_89ae873b54fa3664e4a65bb9dc3973c9.md)
- [sensing\_sensor.h](sensing__sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
