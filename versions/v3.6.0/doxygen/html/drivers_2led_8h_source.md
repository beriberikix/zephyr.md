---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2led_8h_source.html
original_path: doxygen/html/drivers_2led_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led.h

[Go to the documentation of this file.](drivers_2led_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LED\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_LED\_H\_

14

21

22#include <[errno.h](errno_8h.md)>

23

24#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 36](structled__info.md)struct [led\_info](structled__info.md) {

[ 38](structled__info.md#a5d01795e49663654e9fe4a821797956a) const char \*[label](structled__info.md#a5d01795e49663654e9fe4a821797956a);

[ 40](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55);

[ 42](structled__info.md#ab6db05157b960669e3b01154a9621530) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_colors](structled__info.md#ab6db05157b960669e3b01154a9621530);

[ 44](structled__info.md#a8daacbe0a68d7ff710938722003fceaf) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[color\_mapping](structled__info.md#a8daacbe0a68d7ff710938722003fceaf);

45};

46

[ 53](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd)typedef int (\*[led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

54 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off);

55

[ 62](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77)typedef int (\*[led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

63 const struct [led\_info](structled__info.md) \*\*info);

64

[ 71](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f)typedef int (\*[led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

72 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

[ 79](group__led__interface.md#ga977317f3208d5336463edf9979def4ae)typedef int (\*[led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

80 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color);

81

[ 88](group__led__interface.md#gad13f55702668133575658d2ccc295339)typedef int (\*[led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

89

[ 96](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)typedef int (\*[led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

97

[ 104](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae)typedef int (\*[led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae))(const struct [device](structdevice.md) \*dev,

105 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

106 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels,

107 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

108

[ 112](structled__driver__api.md)\_\_subsystem struct [led\_driver\_api](structled__driver__api.md) {

113 /\* Mandatory callbacks. \*/

[ 114](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4) [led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339) [on](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4);

[ 115](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7) [led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd) [off](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7);

116 /\* Optional callbacks. \*/

[ 117](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b) [led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd) [blink](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b);

[ 118](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e) [led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77) [get\_info](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e);

[ 119](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058) [led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f) [set\_brightness](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058);

[ 120](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a) [led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae) [set\_color](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a);

[ 121](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337) [led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae) [write\_channels](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337);

122};

123

[ 136](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)\_\_syscall int [led\_blink](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

137 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off);

138

139static inline int z\_impl\_led\_blink(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

140 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off)

141{

142 const struct [led\_driver\_api](structled__driver__api.md) \*api =

143 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

144

145 if (api->blink == NULL) {

146 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

147 }

148 return api->blink(dev, led, delay\_on, delay\_off);

149}

150

[ 161](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)\_\_syscall int [led\_get\_info](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

162 const struct [led\_info](structled__info.md) \*\*info);

163

164static inline int z\_impl\_led\_get\_info(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

165 const struct [led\_info](structled__info.md) \*\*info)

166{

167 const struct [led\_driver\_api](structled__driver__api.md) \*api =

168 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

169

170 if (api->get\_info == NULL) {

171 \*info = NULL;

172 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

173 }

174 return api->get\_info(dev, led, info);

175}

176

[ 192](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)\_\_syscall int [led\_set\_brightness](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

193 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

194

195static inline int z\_impl\_led\_set\_brightness(const struct [device](structdevice.md) \*dev,

196 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

197 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

198{

199 const struct [led\_driver\_api](structled__driver__api.md) \*api =

200 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

201

202 if (api->set\_brightness == NULL) {

203 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

204 }

205 return api->set\_brightness(dev, led, value);

206}

207

[ 224](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a)\_\_syscall int [led\_write\_channels](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a)(const struct [device](structdevice.md) \*dev,

225 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

226 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

227

228static inline int

229z\_impl\_led\_write\_channels(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

230 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf)

231{

232 const struct [led\_driver\_api](structled__driver__api.md) \*api =

233 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

234

235 if (api->write\_channels == NULL) {

236 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

237 }

238 return api->write\_channels(dev, start\_channel, num\_channels, buf);

239}

240

[ 253](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)\_\_syscall int [led\_set\_channel](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)(const struct [device](structdevice.md) \*dev,

254 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

255

256static inline int z\_impl\_led\_set\_channel(const struct [device](structdevice.md) \*dev,

257 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

258{

259 return z\_impl\_led\_write\_channels(dev, channel, 1, &value);

260}

261

[ 278](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)\_\_syscall int [led\_set\_color](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

279 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color);

280

281static inline int z\_impl\_led\_set\_color(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

282 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color)

283{

284 const struct [led\_driver\_api](structled__driver__api.md) \*api =

285 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

286

287 if (api->set\_color == NULL) {

288 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

289 }

290 return api->set\_color(dev, led, num\_colors, color);

291}

292

[ 302](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)\_\_syscall int [led\_on](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

303

304static inline int z\_impl\_led\_on(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led)

305{

306 const struct [led\_driver\_api](structled__driver__api.md) \*api =

307 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

308

309 return api->on(dev, led);

310}

311

[ 321](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)\_\_syscall int [led\_off](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

322

323static inline int z\_impl\_led\_off(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led)

324{

325 const struct [led\_driver\_api](structled__driver__api.md) \*api =

326 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

327

328 return api->off(dev, led);

329}

330

334

335#ifdef \_\_cplusplus

336}

337#endif

338

339#include <syscalls/led.h>

340

341#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[led\_off](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)

int led\_off(const struct device \*dev, uint32\_t led)

Turn off an LED.

[led\_write\_channels](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a)

int led\_write\_channels(const struct device \*dev, uint32\_t start\_channel, uint32\_t num\_channels, const uint8\_t \*buf)

Write/update a strip of LED channels.

[led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77)

int(\* led\_api\_get\_info)(const struct device \*dev, uint32\_t led, const struct led\_info \*\*info)

Optional API callback to get LED information.

**Definition** led.h:62

[led\_blink](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)

int led\_blink(const struct device \*dev, uint32\_t led, uint32\_t delay\_on, uint32\_t delay\_off)

Blink an LED.

[led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)

int(\* led\_api\_off)(const struct device \*dev, uint32\_t led)

Callback API for turning off an LED.

**Definition** led.h:96

[led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae)

int(\* led\_api\_write\_channels)(const struct device \*dev, uint32\_t start\_channel, uint32\_t num\_channels, const uint8\_t \*buf)

Callback API for writing a strip of LED channels.

**Definition** led.h:104

[led\_set\_channel](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)

int led\_set\_channel(const struct device \*dev, uint32\_t channel, uint8\_t value)

Set a single LED channel.

[led\_set\_color](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)

int led\_set\_color(const struct device \*dev, uint32\_t led, uint8\_t num\_colors, const uint8\_t \*color)

Set LED color.

[led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae)

int(\* led\_api\_set\_color)(const struct device \*dev, uint32\_t led, uint8\_t num\_colors, const uint8\_t \*color)

Optional API callback to set the colors of a LED.

**Definition** led.h:79

[led\_get\_info](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)

int led\_get\_info(const struct device \*dev, uint32\_t led, const struct led\_info \*\*info)

Get LED information.

[led\_set\_brightness](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)

int led\_set\_brightness(const struct device \*dev, uint32\_t led, uint8\_t value)

Set LED brightness.

[led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339)

int(\* led\_api\_on)(const struct device \*dev, uint32\_t led)

Callback API for turning on an LED.

**Definition** led.h:88

[led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd)

int(\* led\_api\_blink)(const struct device \*dev, uint32\_t led, uint32\_t delay\_on, uint32\_t delay\_off)

Callback API for blinking an LED.

**Definition** led.h:53

[led\_on](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)

int led\_on(const struct device \*dev, uint32\_t led)

Turn on an LED.

[led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f)

int(\* led\_api\_set\_brightness)(const struct device \*dev, uint32\_t led, uint8\_t value)

Callback API for setting brightness of an LED.

**Definition** led.h:71

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[led\_driver\_api](structled__driver__api.md)

LED driver API.

**Definition** led.h:112

[led\_driver\_api::off](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7)

led\_api\_off off

**Definition** led.h:115

[led\_driver\_api::set\_color](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a)

led\_api\_set\_color set\_color

**Definition** led.h:120

[led\_driver\_api::get\_info](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e)

led\_api\_get\_info get\_info

**Definition** led.h:118

[led\_driver\_api::set\_brightness](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058)

led\_api\_set\_brightness set\_brightness

**Definition** led.h:119

[led\_driver\_api::on](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4)

led\_api\_on on

**Definition** led.h:114

[led\_driver\_api::write\_channels](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337)

led\_api\_write\_channels write\_channels

**Definition** led.h:121

[led\_driver\_api::blink](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b)

led\_api\_blink blink

**Definition** led.h:117

[led\_info](structled__info.md)

LED information structure.

**Definition** led.h:36

[led\_info::label](structled__info.md#a5d01795e49663654e9fe4a821797956a)

const char \* label

LED label.

**Definition** led.h:38

[led\_info::index](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55)

uint32\_t index

Number of colors per LED.

**Definition** led.h:40

[led\_info::color\_mapping](structled__info.md#a8daacbe0a68d7ff710938722003fceaf)

const uint8\_t \* color\_mapping

Mapping of the LED colors.

**Definition** led.h:44

[led\_info::num\_colors](structled__info.md#ab6db05157b960669e3b01154a9621530)

uint8\_t num\_colors

Index of the LED on the controller.

**Definition** led.h:42

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led.h](drivers_2led_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
