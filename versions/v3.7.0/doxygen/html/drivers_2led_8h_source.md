---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2led_8h_source.html
original_path: doxygen/html/drivers_2led_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

23

24#include <[errno.h](errno_8h.md)>

25

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[zephyr/device.h](device_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 38](structled__info.md)struct [led\_info](structled__info.md) {

[ 40](structled__info.md#a5d01795e49663654e9fe4a821797956a) const char \*[label](structled__info.md#a5d01795e49663654e9fe4a821797956a);

[ 42](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [index](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55);

[ 44](structled__info.md#ab6db05157b960669e3b01154a9621530) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_colors](structled__info.md#ab6db05157b960669e3b01154a9621530);

[ 46](structled__info.md#a8daacbe0a68d7ff710938722003fceaf) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[color\_mapping](structled__info.md#a8daacbe0a68d7ff710938722003fceaf);

47};

48

[ 55](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd)typedef int (\*[led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

56 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off);

57

[ 64](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77)typedef int (\*[led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

65 const struct [led\_info](structled__info.md) \*\*info);

66

[ 73](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f)typedef int (\*[led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

74 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

[ 81](group__led__interface.md#ga977317f3208d5336463edf9979def4ae)typedef int (\*[led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

82 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color);

83

[ 90](group__led__interface.md#gad13f55702668133575658d2ccc295339)typedef int (\*[led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

91

[ 98](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)typedef int (\*[led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

99

[ 106](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae)typedef int (\*[led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae))(const struct [device](structdevice.md) \*dev,

107 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

108 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels,

109 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

110

[ 114](structled__driver__api.md)\_\_subsystem struct [led\_driver\_api](structled__driver__api.md) {

115 /\* Mandatory callbacks. \*/

[ 116](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4) [led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339) [on](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4);

[ 117](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7) [led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd) [off](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7);

118 /\* Optional callbacks. \*/

[ 119](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b) [led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd) [blink](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b);

[ 120](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e) [led\_api\_get\_info](group__led__interface.md#ga3828b1e544a2f64378d5c3bfbbaa0c77) [get\_info](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e);

[ 121](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058) [led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f) [set\_brightness](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058);

[ 122](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a) [led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae) [set\_color](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a);

[ 123](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337) [led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae) [write\_channels](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337);

124};

125

[ 138](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)\_\_syscall int [led\_blink](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

139 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off);

140

141static inline int z\_impl\_led\_blink(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

142 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_on, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_off)

143{

144 const struct [led\_driver\_api](structled__driver__api.md) \*api =

145 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

146

147 if (api->blink == NULL) {

148 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

149 }

150 return api->blink(dev, led, delay\_on, delay\_off);

151}

152

[ 163](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)\_\_syscall int [led\_get\_info](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

164 const struct [led\_info](structled__info.md) \*\*info);

165

166static inline int z\_impl\_led\_get\_info(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

167 const struct [led\_info](structled__info.md) \*\*info)

168{

169 const struct [led\_driver\_api](structled__driver__api.md) \*api =

170 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

171

172 if (api->get\_info == NULL) {

173 \*info = NULL;

174 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

175 }

176 return api->get\_info(dev, led, info);

177}

178

[ 194](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)\_\_syscall int [led\_set\_brightness](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

195 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

196

197static inline int z\_impl\_led\_set\_brightness(const struct [device](structdevice.md) \*dev,

198 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

199 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

200{

201 const struct [led\_driver\_api](structled__driver__api.md) \*api =

202 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

203

204 if (api->set\_brightness == NULL) {

205 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

206 }

207 return api->set\_brightness(dev, led, value);

208}

209

[ 226](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a)\_\_syscall int [led\_write\_channels](group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a)(const struct [device](structdevice.md) \*dev,

227 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

228 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

229

230static inline int

231z\_impl\_led\_write\_channels(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_channel,

232 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_channels, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf)

233{

234 const struct [led\_driver\_api](structled__driver__api.md) \*api =

235 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

236

237 if (api->write\_channels == NULL) {

238 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

239 }

240 return api->write\_channels(dev, start\_channel, num\_channels, buf);

241}

242

[ 255](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)\_\_syscall int [led\_set\_channel](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)(const struct [device](structdevice.md) \*dev,

256 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

257

258static inline int z\_impl\_led\_set\_channel(const struct [device](structdevice.md) \*dev,

259 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value)

260{

261 return z\_impl\_led\_write\_channels(dev, channel, 1, &value);

262}

263

[ 280](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)\_\_syscall int [led\_set\_color](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

281 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color);

282

283static inline int z\_impl\_led\_set\_color(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led,

284 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_colors, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*color)

285{

286 const struct [led\_driver\_api](structled__driver__api.md) \*api =

287 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

288

289 if (api->set\_color == NULL) {

290 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

291 }

292 return api->set\_color(dev, led, num\_colors, color);

293}

294

[ 304](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)\_\_syscall int [led\_on](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

305

306static inline int z\_impl\_led\_on(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led)

307{

308 const struct [led\_driver\_api](structled__driver__api.md) \*api =

309 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

310

311 return api->on(dev, led);

312}

313

[ 323](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)\_\_syscall int [led\_off](group__led__interface.md#ga22c9dbe76f06fec327aebe06448d1542)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led);

324

325static inline int z\_impl\_led\_off(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led)

326{

327 const struct [led\_driver\_api](structled__driver__api.md) \*api =

328 (const struct [led\_driver\_api](structled__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

329

330 return api->off(dev, led);

331}

332

336

337#ifdef \_\_cplusplus

338}

339#endif

340

341#include <zephyr/syscalls/led.h>

342

343#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_H\_ \*/

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

**Definition** led.h:64

[led\_blink](group__led__interface.md#ga4f31fecd215e5597999be4d16b0d2dd5)

int led\_blink(const struct device \*dev, uint32\_t led, uint32\_t delay\_on, uint32\_t delay\_off)

Blink an LED.

[led\_api\_off](group__led__interface.md#ga5ae67fe64f97b0e716f9eb2f3a34f1fd)

int(\* led\_api\_off)(const struct device \*dev, uint32\_t led)

Callback API for turning off an LED.

**Definition** led.h:98

[led\_api\_write\_channels](group__led__interface.md#ga66dac12510c3a2281378d532ba6db2ae)

int(\* led\_api\_write\_channels)(const struct device \*dev, uint32\_t start\_channel, uint32\_t num\_channels, const uint8\_t \*buf)

Callback API for writing a strip of LED channels.

**Definition** led.h:106

[led\_set\_channel](group__led__interface.md#ga717bdbe76331b6286c58feb6e3e214dd)

int led\_set\_channel(const struct device \*dev, uint32\_t channel, uint8\_t value)

Set a single LED channel.

[led\_set\_color](group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea)

int led\_set\_color(const struct device \*dev, uint32\_t led, uint8\_t num\_colors, const uint8\_t \*color)

Set LED color.

[led\_api\_set\_color](group__led__interface.md#ga977317f3208d5336463edf9979def4ae)

int(\* led\_api\_set\_color)(const struct device \*dev, uint32\_t led, uint8\_t num\_colors, const uint8\_t \*color)

Optional API callback to set the colors of a LED.

**Definition** led.h:81

[led\_get\_info](group__led__interface.md#ga9925483b97073354f7be6b40aa2dad1a)

int led\_get\_info(const struct device \*dev, uint32\_t led, const struct led\_info \*\*info)

Get LED information.

[led\_set\_brightness](group__led__interface.md#gaca479fd77518331f4fc84f788e345882)

int led\_set\_brightness(const struct device \*dev, uint32\_t led, uint8\_t value)

Set LED brightness.

[led\_api\_on](group__led__interface.md#gad13f55702668133575658d2ccc295339)

int(\* led\_api\_on)(const struct device \*dev, uint32\_t led)

Callback API for turning on an LED.

**Definition** led.h:90

[led\_api\_blink](group__led__interface.md#gad3c655794f58045459cbd910592d2cdd)

int(\* led\_api\_blink)(const struct device \*dev, uint32\_t led, uint32\_t delay\_on, uint32\_t delay\_off)

Callback API for blinking an LED.

**Definition** led.h:55

[led\_on](group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73)

int led\_on(const struct device \*dev, uint32\_t led)

Turn on an LED.

[led\_api\_set\_brightness](group__led__interface.md#gae24caa14f6aa41c2a509d2eaf468463f)

int(\* led\_api\_set\_brightness)(const struct device \*dev, uint32\_t led, uint8\_t value)

Callback API for setting brightness of an LED.

**Definition** led.h:73

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[led\_driver\_api](structled__driver__api.md)

LED driver API.

**Definition** led.h:114

[led\_driver\_api::off](structled__driver__api.md#a19ad736a130da2aff6bd5b299d8c33a7)

led\_api\_off off

**Definition** led.h:117

[led\_driver\_api::set\_color](structled__driver__api.md#a336f30f2c1bd3d99213cae66911c142a)

led\_api\_set\_color set\_color

**Definition** led.h:122

[led\_driver\_api::get\_info](structled__driver__api.md#a7c68219e44bcf6e766e64fd3967ecf7e)

led\_api\_get\_info get\_info

**Definition** led.h:120

[led\_driver\_api::set\_brightness](structled__driver__api.md#a9c3e3c4d40c4b8219755df6df96b0058)

led\_api\_set\_brightness set\_brightness

**Definition** led.h:121

[led\_driver\_api::on](structled__driver__api.md#a9ce7322282f8c525256d3c16a514ecc4)

led\_api\_on on

**Definition** led.h:116

[led\_driver\_api::write\_channels](structled__driver__api.md#ada1dfb1830b48afb020c7e60dbd92337)

led\_api\_write\_channels write\_channels

**Definition** led.h:123

[led\_driver\_api::blink](structled__driver__api.md#af1974c5cc20c818e0e387b34cd14ac3b)

led\_api\_blink blink

**Definition** led.h:119

[led\_info](structled__info.md)

LED information structure.

**Definition** led.h:38

[led\_info::label](structled__info.md#a5d01795e49663654e9fe4a821797956a)

const char \* label

LED label.

**Definition** led.h:40

[led\_info::index](structled__info.md#a7f87ebb0718e1dc189e6d48d5bb97c55)

uint32\_t index

Index of the LED on the controller.

**Definition** led.h:42

[led\_info::color\_mapping](structled__info.md#a8daacbe0a68d7ff710938722003fceaf)

const uint8\_t \* color\_mapping

Mapping of the LED colors.

**Definition** led.h:46

[led\_info::num\_colors](structled__info.md#ab6db05157b960669e3b01154a9621530)

uint8\_t num\_colors

Number of colors per LED.

**Definition** led.h:44

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led.h](drivers_2led_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
