---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lora_8h_source.html
original_path: doxygen/html/lora_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lora.h

[Go to the documentation of this file.](lora_8h.md)

1/\*

2 \* Copyright (c) 2019 Manivannan Sadhasivam

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LORA\_H\_

12#define ZEPHYR\_INCLUDE\_DRIVERS\_LORA\_H\_

13

23

24#include <[stdint.h](stdint_8h.md)>

25#include <[zephyr/kernel.h](kernel_8h.md)>

26#include <[zephyr/device.h](device_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 35](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136)enum [lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136) {

[ 36](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1) [BW\_125\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1) = 0,

[ 37](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411) [BW\_250\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411),

[ 38](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9) [BW\_500\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9),

39};

40

[ 44](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb)enum [lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb) {

[ 45](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d) [SF\_6](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d) = 6,

[ 46](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608) [SF\_7](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608),

[ 47](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e) [SF\_8](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e),

[ 48](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc) [SF\_9](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc),

[ 49](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6) [SF\_10](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6),

[ 50](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407) [SF\_11](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407),

[ 51](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958) [SF\_12](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958),

52};

53

[ 57](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8)enum [lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8) {

[ 58](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18) [CR\_4\_5](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18) = 1,

[ 59](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e) [CR\_4\_6](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e) = 2,

[ 60](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943) [CR\_4\_7](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943) = 3,

[ 61](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42) [CR\_4\_8](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42) = 4,

62};

63

[ 68](structlora__modem__config.md)struct [lora\_modem\_config](structlora__modem__config.md) {

[ 70](structlora__modem__config.md#a08209a2dabc5111025810fc8e141c2df) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frequency](structlora__modem__config.md#a08209a2dabc5111025810fc8e141c2df);

71

[ 73](structlora__modem__config.md#a0c6a90e31b4a97d962af3dbd0ee8e885) enum [lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136) [bandwidth](structlora__modem__config.md#a0c6a90e31b4a97d962af3dbd0ee8e885);

74

[ 76](structlora__modem__config.md#ae438c1c223f12fc6c3747d4297ec61ba) enum [lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb) [datarate](structlora__modem__config.md#ae438c1c223f12fc6c3747d4297ec61ba);

77

[ 79](structlora__modem__config.md#a8e47a8506265562c7b118fab72cceb10) enum [lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8) [coding\_rate](structlora__modem__config.md#a8e47a8506265562c7b118fab72cceb10);

80

[ 82](structlora__modem__config.md#a9d0795c5be6ae0042babaa05615cf7f2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [preamble\_len](structlora__modem__config.md#a9d0795c5be6ae0042babaa05615cf7f2);

83

[ 85](structlora__modem__config.md#a41a194d62e1e3e1b142e194a75efb8a1) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structlora__modem__config.md#a41a194d62e1e3e1b142e194a75efb8a1);

86

[ 88](structlora__modem__config.md#a10b12a2092712050bdd64c6250c8731f) bool [tx](structlora__modem__config.md#a10b12a2092712050bdd64c6250c8731f);

89

[ 97](structlora__modem__config.md#a5737749b3bd29515887bb0b8c48c8bd1) bool [iq\_inverted](structlora__modem__config.md#a5737749b3bd29515887bb0b8c48c8bd1);

98

[ 108](structlora__modem__config.md#af97fde1f5f40a4d702c0140872728e86) bool [public\_network](structlora__modem__config.md#af97fde1f5f40a4d702c0140872728e86);

109};

110

116

123typedef void (\*lora\_recv\_cb)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size,

124 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) snr, void \*user\_data);

125

132typedef int (\*lora\_api\_config)(const struct [device](structdevice.md) \*dev,

133 struct [lora\_modem\_config](structlora__modem__config.md) \*config);

134

141typedef int (\*lora\_api\_send)(const struct [device](structdevice.md) \*dev,

142 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len);

143

150typedef int (\*lora\_api\_send\_async)(const struct [device](structdevice.md) \*dev,

151 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len,

152 struct [k\_poll\_signal](structk__poll__signal.md) \*async);

153

160typedef int (\*lora\_api\_recv)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

161 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size,

162 [k\_timeout\_t](structk__timeout__t.md) timeout, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*snr);

163

171typedef int (\*lora\_api\_recv\_async)(const struct [device](structdevice.md) \*dev, lora\_recv\_cb cb,

172 void \*user\_data);

173

180typedef int (\*lora\_api\_test\_cw)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency,

181 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) tx\_power, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration);

182

183\_\_subsystem struct lora\_driver\_api {

184 lora\_api\_config config;

185 lora\_api\_send [send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f);

186 lora\_api\_send\_async send\_async;

187 lora\_api\_recv [recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276);

188 lora\_api\_recv\_async recv\_async;

189 lora\_api\_test\_cw test\_cw;

190};

191

193

[ 202](group__lora__api.md#gad7c6c516d2d0e023da952666d3f8decb)static inline int [lora\_config](group__lora__api.md#gad7c6c516d2d0e023da952666d3f8decb)(const struct [device](structdevice.md) \*dev,

203 struct [lora\_modem\_config](structlora__modem__config.md) \*config)

204{

205 const struct lora\_driver\_api \*api =

206 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

207

208 return api->config(dev, config);

209}

210

[ 221](group__lora__api.md#gad893b49a74e350bb05f42f863af31446)static inline int [lora\_send](group__lora__api.md#gad893b49a74e350bb05f42f863af31446)(const struct [device](structdevice.md) \*dev,

222 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len)

223{

224 const struct lora\_driver\_api \*api =

225 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

226

227 return api->send(dev, data, data\_len);

228}

229

[ 244](group__lora__api.md#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)static inline int [lora\_send\_async](group__lora__api.md#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)(const struct [device](structdevice.md) \*dev,

245 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len,

246 struct [k\_poll\_signal](structk__poll__signal.md) \*async)

247{

248 const struct lora\_driver\_api \*api =

249 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

250

251 return api->send\_async(dev, data, data\_len, async);

252}

253

[ 268](group__lora__api.md#ga28005c24ab1c13eb311bc05c3454a8f6)static inline int [lora\_recv](group__lora__api.md#ga28005c24ab1c13eb311bc05c3454a8f6)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

269 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size,

270 [k\_timeout\_t](structk__timeout__t.md) timeout, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*snr)

271{

272 const struct lora\_driver\_api \*api =

273 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

274

275 return api->recv(dev, data, size, timeout, rssi, snr);

276}

277

[ 293](group__lora__api.md#gafeae6fa9d81508023665705bf16b6435)static inline int [lora\_recv\_async](group__lora__api.md#gafeae6fa9d81508023665705bf16b6435)(const struct [device](structdevice.md) \*dev, lora\_recv\_cb cb,

294 void \*user\_data)

295{

296 const struct lora\_driver\_api \*api =

297 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

298

299 return api->recv\_async(dev, cb, user\_data);

300}

301

[ 314](group__lora__api.md#ga27d78168c737d56f9f7f3bbdacb808fb)static inline int [lora\_test\_cw](group__lora__api.md#ga27d78168c737d56f9f7f3bbdacb808fb)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency,

315 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) tx\_power, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration)

316{

317 const struct lora\_driver\_api \*api =

318 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

319

320 if (api->test\_cw == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

321 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

322 }

323

324 return api->test\_cw(dev, frequency, tx\_power, duration);

325}

326

327#ifdef \_\_cplusplus

328}

329#endif

330

334

335#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LORA\_H\_ \*/

[device.h](device_8h.md)

[lora\_test\_cw](group__lora__api.md#ga27d78168c737d56f9f7f3bbdacb808fb)

static int lora\_test\_cw(const struct device \*dev, uint32\_t frequency, int8\_t tx\_power, uint16\_t duration)

Transmit an unmodulated continuous wave at a given frequency.

**Definition** lora.h:314

[lora\_recv](group__lora__api.md#ga28005c24ab1c13eb311bc05c3454a8f6)

static int lora\_recv(const struct device \*dev, uint8\_t \*data, uint8\_t size, k\_timeout\_t timeout, int16\_t \*rssi, int8\_t \*snr)

Receive data over LoRa.

**Definition** lora.h:268

[lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb)

lora\_datarate

LoRa data-rate.

**Definition** lora.h:44

[lora\_send\_async](group__lora__api.md#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)

static int lora\_send\_async(const struct device \*dev, uint8\_t \*data, uint32\_t data\_len, struct k\_poll\_signal \*async)

Asynchronously send data over LoRa.

**Definition** lora.h:244

[lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8)

lora\_coding\_rate

LoRa coding rate.

**Definition** lora.h:57

[lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136)

lora\_signal\_bandwidth

LoRa signal bandwidth.

**Definition** lora.h:35

[lora\_config](group__lora__api.md#gad7c6c516d2d0e023da952666d3f8decb)

static int lora\_config(const struct device \*dev, struct lora\_modem\_config \*config)

Configure the LoRa modem.

**Definition** lora.h:202

[lora\_send](group__lora__api.md#gad893b49a74e350bb05f42f863af31446)

static int lora\_send(const struct device \*dev, uint8\_t \*data, uint32\_t data\_len)

Send data over LoRa.

**Definition** lora.h:221

[lora\_recv\_async](group__lora__api.md#gafeae6fa9d81508023665705bf16b6435)

static int lora\_recv\_async(const struct device \*dev, lora\_recv\_cb cb, void \*user\_data)

Receive data asynchronously over LoRa.

**Definition** lora.h:293

[SF\_12](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958)

@ SF\_12

**Definition** lora.h:51

[SF\_8](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e)

@ SF\_8

**Definition** lora.h:47

[SF\_11](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407)

@ SF\_11

**Definition** lora.h:50

[SF\_10](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6)

@ SF\_10

**Definition** lora.h:49

[SF\_9](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc)

@ SF\_9

**Definition** lora.h:48

[SF\_6](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d)

@ SF\_6

**Definition** lora.h:45

[SF\_7](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608)

@ SF\_7

**Definition** lora.h:46

[CR\_4\_5](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18)

@ CR\_4\_5

**Definition** lora.h:58

[CR\_4\_6](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e)

@ CR\_4\_6

**Definition** lora.h:59

[CR\_4\_8](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42)

@ CR\_4\_8

**Definition** lora.h:61

[CR\_4\_7](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943)

@ CR\_4\_7

**Definition** lora.h:60

[BW\_250\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411)

@ BW\_250\_KHZ

**Definition** lora.h:37

[BW\_125\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1)

@ BW\_125\_KHZ

**Definition** lora.h:36

[BW\_500\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9)

@ BW\_500\_KHZ

**Definition** lora.h:38

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[kernel.h](kernel_8h.md)

Public kernel APIs.

[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)

ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

[recv](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276)

ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5964

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[lora\_modem\_config](structlora__modem__config.md)

Structure containing the configuration of a LoRa modem.

**Definition** lora.h:68

[lora\_modem\_config::frequency](structlora__modem__config.md#a08209a2dabc5111025810fc8e141c2df)

uint32\_t frequency

Frequency in Hz to use for transceiving.

**Definition** lora.h:70

[lora\_modem\_config::bandwidth](structlora__modem__config.md#a0c6a90e31b4a97d962af3dbd0ee8e885)

enum lora\_signal\_bandwidth bandwidth

The bandwidth to use for transceiving.

**Definition** lora.h:73

[lora\_modem\_config::tx](structlora__modem__config.md#a10b12a2092712050bdd64c6250c8731f)

bool tx

Set to true for transmission, false for receiving.

**Definition** lora.h:88

[lora\_modem\_config::tx\_power](structlora__modem__config.md#a41a194d62e1e3e1b142e194a75efb8a1)

int8\_t tx\_power

TX-power in dBm to use for transmission.

**Definition** lora.h:85

[lora\_modem\_config::iq\_inverted](structlora__modem__config.md#a5737749b3bd29515887bb0b8c48c8bd1)

bool iq\_inverted

Invert the In-Phase and Quadrature (IQ) signals.

**Definition** lora.h:97

[lora\_modem\_config::coding\_rate](structlora__modem__config.md#a8e47a8506265562c7b118fab72cceb10)

enum lora\_coding\_rate coding\_rate

The coding rate to use for transceiving.

**Definition** lora.h:79

[lora\_modem\_config::preamble\_len](structlora__modem__config.md#a9d0795c5be6ae0042babaa05615cf7f2)

uint16\_t preamble\_len

Length of the preamble.

**Definition** lora.h:82

[lora\_modem\_config::datarate](structlora__modem__config.md#ae438c1c223f12fc6c3747d4297ec61ba)

enum lora\_datarate datarate

The data-rate to use for transceiving.

**Definition** lora.h:76

[lora\_modem\_config::public\_network](structlora__modem__config.md#af97fde1f5f40a4d702c0140872728e86)

bool public\_network

Sets the sync-byte to use:

**Definition** lora.h:108

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [lora.h](lora_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
