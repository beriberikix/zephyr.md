---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lora_8h_source.html
original_path: doxygen/html/lora_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

21

22#include <[stdint.h](stdint_8h.md)>

23#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

24#include <[zephyr/device.h](device_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 33](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136)enum [lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136) {

[ 34](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1) [BW\_125\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1) = 0,

[ 35](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411) [BW\_250\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411),

[ 36](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9) [BW\_500\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9),

37};

38

[ 42](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb)enum [lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb) {

[ 43](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d) [SF\_6](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d) = 6,

[ 44](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608) [SF\_7](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608),

[ 45](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e) [SF\_8](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e),

[ 46](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc) [SF\_9](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc),

[ 47](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6) [SF\_10](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6),

[ 48](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407) [SF\_11](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407),

[ 49](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958) [SF\_12](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958),

50};

51

[ 55](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8)enum [lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8) {

[ 56](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18) [CR\_4\_5](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18) = 1,

[ 57](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e) [CR\_4\_6](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e) = 2,

[ 58](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943) [CR\_4\_7](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943) = 3,

[ 59](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42) [CR\_4\_8](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42) = 4,

60};

61

[ 66](structlora__modem__config.md)struct [lora\_modem\_config](structlora__modem__config.md) {

[ 68](structlora__modem__config.md#a08209a2dabc5111025810fc8e141c2df) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frequency](structlora__modem__config.md#a08209a2dabc5111025810fc8e141c2df);

69

[ 71](structlora__modem__config.md#a0c6a90e31b4a97d962af3dbd0ee8e885) enum [lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136) [bandwidth](structlora__modem__config.md#a0c6a90e31b4a97d962af3dbd0ee8e885);

72

[ 74](structlora__modem__config.md#ae438c1c223f12fc6c3747d4297ec61ba) enum [lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb) [datarate](structlora__modem__config.md#ae438c1c223f12fc6c3747d4297ec61ba);

75

[ 77](structlora__modem__config.md#a8e47a8506265562c7b118fab72cceb10) enum [lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8) [coding\_rate](structlora__modem__config.md#a8e47a8506265562c7b118fab72cceb10);

78

[ 80](structlora__modem__config.md#a9d0795c5be6ae0042babaa05615cf7f2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [preamble\_len](structlora__modem__config.md#a9d0795c5be6ae0042babaa05615cf7f2);

81

[ 83](structlora__modem__config.md#a41a194d62e1e3e1b142e194a75efb8a1) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tx\_power](structlora__modem__config.md#a41a194d62e1e3e1b142e194a75efb8a1);

84

[ 86](structlora__modem__config.md#a10b12a2092712050bdd64c6250c8731f) bool [tx](structlora__modem__config.md#a10b12a2092712050bdd64c6250c8731f);

87

[ 95](structlora__modem__config.md#a5737749b3bd29515887bb0b8c48c8bd1) bool [iq\_inverted](structlora__modem__config.md#a5737749b3bd29515887bb0b8c48c8bd1);

96

[ 106](structlora__modem__config.md#af97fde1f5f40a4d702c0140872728e86) bool [public\_network](structlora__modem__config.md#af97fde1f5f40a4d702c0140872728e86);

107};

108

114

121typedef void (\*lora\_recv\_cb)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size,

122 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) snr);

123

130typedef int (\*lora\_api\_config)(const struct [device](structdevice.md) \*dev,

131 struct [lora\_modem\_config](structlora__modem__config.md) \*config);

132

139typedef int (\*lora\_api\_send)(const struct [device](structdevice.md) \*dev,

140 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len);

141

148typedef int (\*lora\_api\_send\_async)(const struct [device](structdevice.md) \*dev,

149 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len,

150 struct [k\_poll\_signal](structk__poll__signal.md) \*async);

151

158typedef int (\*lora\_api\_recv)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

159 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size,

160 [k\_timeout\_t](structk__timeout__t.md) timeout, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*snr);

161

169typedef int (\*lora\_api\_recv\_async)(const struct [device](structdevice.md) \*dev, lora\_recv\_cb cb);

170

177typedef int (\*lora\_api\_test\_cw)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency,

178 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) tx\_power, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration);

179

180struct lora\_driver\_api {

181 lora\_api\_config config;

182 lora\_api\_send [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d);

183 lora\_api\_send\_async send\_async;

184 lora\_api\_recv [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40);

185 lora\_api\_recv\_async recv\_async;

186 lora\_api\_test\_cw test\_cw;

187};

188

190

[ 199](group__lora__api.md#gad7c6c516d2d0e023da952666d3f8decb)static inline int [lora\_config](group__lora__api.md#gad7c6c516d2d0e023da952666d3f8decb)(const struct [device](structdevice.md) \*dev,

200 struct [lora\_modem\_config](structlora__modem__config.md) \*config)

201{

202 const struct lora\_driver\_api \*api =

203 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

204

205 return api->config(dev, config);

206}

207

[ 218](group__lora__api.md#gad893b49a74e350bb05f42f863af31446)static inline int [lora\_send](group__lora__api.md#gad893b49a74e350bb05f42f863af31446)(const struct [device](structdevice.md) \*dev,

219 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len)

220{

221 const struct lora\_driver\_api \*api =

222 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

223

224 return api->send(dev, data, data\_len);

225}

226

[ 241](group__lora__api.md#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)static inline int [lora\_send\_async](group__lora__api.md#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)(const struct [device](structdevice.md) \*dev,

242 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len,

243 struct [k\_poll\_signal](structk__poll__signal.md) \*async)

244{

245 const struct lora\_driver\_api \*api =

246 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

247

248 return api->send\_async(dev, data, data\_len, async);

249}

250

[ 265](group__lora__api.md#ga28005c24ab1c13eb311bc05c3454a8f6)static inline int [lora\_recv](group__lora__api.md#ga28005c24ab1c13eb311bc05c3454a8f6)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

266 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size,

267 [k\_timeout\_t](structk__timeout__t.md) timeout, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*snr)

268{

269 const struct lora\_driver\_api \*api =

270 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

271

272 return api->recv(dev, data, size, timeout, rssi, snr);

273}

274

[ 289](group__lora__api.md#ga4f7ec5eaff55f295ff82f3e22d77f34c)static inline int [lora\_recv\_async](group__lora__api.md#ga4f7ec5eaff55f295ff82f3e22d77f34c)(const struct [device](structdevice.md) \*dev, lora\_recv\_cb cb)

290{

291 const struct lora\_driver\_api \*api =

292 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

293

294 return api->recv\_async(dev, cb);

295}

296

[ 309](group__lora__api.md#ga27d78168c737d56f9f7f3bbdacb808fb)static inline int [lora\_test\_cw](group__lora__api.md#ga27d78168c737d56f9f7f3bbdacb808fb)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frequency,

310 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) tx\_power, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration)

311{

312 const struct lora\_driver\_api \*api =

313 (const struct lora\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

314

315 if (api->test\_cw == NULL) {

316 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

317 }

318

319 return api->test\_cw(dev, frequency, tx\_power, duration);

320}

321

322#ifdef \_\_cplusplus

323}

324#endif

325

329

330#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LORA\_H\_ \*/

[device.h](device_8h.md)

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:882

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:888

[lora\_test\_cw](group__lora__api.md#ga27d78168c737d56f9f7f3bbdacb808fb)

static int lora\_test\_cw(const struct device \*dev, uint32\_t frequency, int8\_t tx\_power, uint16\_t duration)

Transmit an unmodulated continuous wave at a given frequency.

**Definition** lora.h:309

[lora\_recv](group__lora__api.md#ga28005c24ab1c13eb311bc05c3454a8f6)

static int lora\_recv(const struct device \*dev, uint8\_t \*data, uint8\_t size, k\_timeout\_t timeout, int16\_t \*rssi, int8\_t \*snr)

Receive data over LoRa.

**Definition** lora.h:265

[lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb)

lora\_datarate

LoRa data-rate.

**Definition** lora.h:42

[lora\_send\_async](group__lora__api.md#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)

static int lora\_send\_async(const struct device \*dev, uint8\_t \*data, uint32\_t data\_len, struct k\_poll\_signal \*async)

Asynchronously send data over LoRa.

**Definition** lora.h:241

[lora\_recv\_async](group__lora__api.md#ga4f7ec5eaff55f295ff82f3e22d77f34c)

static int lora\_recv\_async(const struct device \*dev, lora\_recv\_cb cb)

Receive data asynchronously over LoRa.

**Definition** lora.h:289

[lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8)

lora\_coding\_rate

LoRa coding rate.

**Definition** lora.h:55

[lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136)

lora\_signal\_bandwidth

LoRa signal bandwidth.

**Definition** lora.h:33

[lora\_config](group__lora__api.md#gad7c6c516d2d0e023da952666d3f8decb)

static int lora\_config(const struct device \*dev, struct lora\_modem\_config \*config)

Configure the LoRa modem.

**Definition** lora.h:199

[lora\_send](group__lora__api.md#gad893b49a74e350bb05f42f863af31446)

static int lora\_send(const struct device \*dev, uint8\_t \*data, uint32\_t data\_len)

Send data over LoRa.

**Definition** lora.h:218

[SF\_12](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958)

@ SF\_12

**Definition** lora.h:49

[SF\_8](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e)

@ SF\_8

**Definition** lora.h:45

[SF\_11](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407)

@ SF\_11

**Definition** lora.h:48

[SF\_10](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6)

@ SF\_10

**Definition** lora.h:47

[SF\_9](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc)

@ SF\_9

**Definition** lora.h:46

[SF\_6](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d)

@ SF\_6

**Definition** lora.h:43

[SF\_7](group__lora__api.md#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608)

@ SF\_7

**Definition** lora.h:44

[CR\_4\_5](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18)

@ CR\_4\_5

**Definition** lora.h:56

[CR\_4\_6](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e)

@ CR\_4\_6

**Definition** lora.h:57

[CR\_4\_8](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42)

@ CR\_4\_8

**Definition** lora.h:59

[CR\_4\_7](group__lora__api.md#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943)

@ CR\_4\_7

**Definition** lora.h:58

[BW\_250\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411)

@ BW\_250\_KHZ

**Definition** lora.h:35

[BW\_125\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1)

@ BW\_125\_KHZ

**Definition** lora.h:34

[BW\_500\_KHZ](group__lora__api.md#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9)

@ BW\_500\_KHZ

**Definition** lora.h:36

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

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

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5622

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[lora\_modem\_config](structlora__modem__config.md)

Structure containing the configuration of a LoRa modem.

**Definition** lora.h:66

[lora\_modem\_config::frequency](structlora__modem__config.md#a08209a2dabc5111025810fc8e141c2df)

uint32\_t frequency

Frequency in Hz to use for transceiving.

**Definition** lora.h:68

[lora\_modem\_config::bandwidth](structlora__modem__config.md#a0c6a90e31b4a97d962af3dbd0ee8e885)

enum lora\_signal\_bandwidth bandwidth

The bandwidth to use for transceiving.

**Definition** lora.h:71

[lora\_modem\_config::tx](structlora__modem__config.md#a10b12a2092712050bdd64c6250c8731f)

bool tx

Set to true for transmission, false for receiving.

**Definition** lora.h:86

[lora\_modem\_config::tx\_power](structlora__modem__config.md#a41a194d62e1e3e1b142e194a75efb8a1)

int8\_t tx\_power

TX-power in dBm to use for transmission.

**Definition** lora.h:83

[lora\_modem\_config::iq\_inverted](structlora__modem__config.md#a5737749b3bd29515887bb0b8c48c8bd1)

bool iq\_inverted

Invert the In-Phase and Quadrature (IQ) signals.

**Definition** lora.h:95

[lora\_modem\_config::coding\_rate](structlora__modem__config.md#a8e47a8506265562c7b118fab72cceb10)

enum lora\_coding\_rate coding\_rate

The coding rate to use for transceiving.

**Definition** lora.h:77

[lora\_modem\_config::preamble\_len](structlora__modem__config.md#a9d0795c5be6ae0042babaa05615cf7f2)

uint16\_t preamble\_len

Length of the preamble.

**Definition** lora.h:80

[lora\_modem\_config::datarate](structlora__modem__config.md#ae438c1c223f12fc6c3747d4297ec61ba)

enum lora\_datarate datarate

The data-rate to use for transceiving.

**Definition** lora.h:74

[lora\_modem\_config::public\_network](structlora__modem__config.md#af97fde1f5f40a4d702c0140872728e86)

bool public\_network

Sets the sync-byte to use:

**Definition** lora.h:106

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [lora.h](lora_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
