---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/psi5_8h_source.html
original_path: doxygen/html/psi5_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

psi5.h

[Go to the documentation of this file.](psi5_8h.md)

1/\*

2 \* Copyright 2025 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PSI5\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_PSI5\_H\_

14

15#include <[zephyr/kernel.h](kernel_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

30

[ 34](group__psi5__interface.md#ga5cb0ef3be35e9ff2d05c39cc17f2659f)enum [psi5\_frame\_type](group__psi5__interface.md#ga5cb0ef3be35e9ff2d05c39cc17f2659f) {

[ 36](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff) [PSI5\_SERIAL\_FRAME\_4\_BIT\_ID](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff),

[ 38](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a) [PSI5\_SERIAL\_FRAME\_8\_BIT\_ID](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a),

[ 40](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f) [PSI5\_DATA\_FRAME](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f)

41};

42

[ 46](structpsi5__frame.md)struct [psi5\_frame](structpsi5__frame.md) {

[ 48](structpsi5__frame.md#a975b56a545604103687679c2cb0561eb) enum [psi5\_frame\_type](group__psi5__interface.md#ga5cb0ef3be35e9ff2d05c39cc17f2659f) [type](structpsi5__frame.md#a975b56a545604103687679c2cb0561eb);

49

50 union {

[ 52](structpsi5__frame.md#a159d66a7eeee3ffc6714f5058ddeefe9) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structpsi5__frame.md#a159d66a7eeee3ffc6714f5058ddeefe9);

53

57 struct {

[ 59](structpsi5__frame.md#ad32ba54088b03cbd4b91e77d9adadec8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structpsi5__frame.md#ad32ba54088b03cbd4b91e77d9adadec8);

[ 61](structpsi5__frame.md#abdca8ada802a3352e2da439736f7f2aa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structpsi5__frame.md#a159d66a7eeee3ffc6714f5058ddeefe9);

[ 62](structpsi5__frame.md#a04a7d9d8d1238c823d787543ba2188c3) } [serial](structpsi5__frame.md#a04a7d9d8d1238c823d787543ba2188c3);

63 };

64

[ 66](structpsi5__frame.md#a3b7f3b38ab831e2789c326a327a05e53) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structpsi5__frame.md#a3b7f3b38ab831e2789c326a327a05e53);

[ 68](structpsi5__frame.md#abd146305031fa97378b96d46e3e6e97d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc](structpsi5__frame.md#abd146305031fa97378b96d46e3e6e97d);

[ 70](structpsi5__frame.md#aec97ec5f2ebef6903fd0b98d8fd2bec4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [slot\_number](structpsi5__frame.md#aec97ec5f2ebef6903fd0b98d8fd2bec4);

71};

72

[ 82](group__psi5__interface.md#gaac8c99036369b14d639cfb82f3b9cd32)typedef void (\*[psi5\_tx\_callback\_t](group__psi5__interface.md#gaac8c99036369b14d639cfb82f3b9cd32))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, int status,

83 void \*user\_data);

84

[ 93](group__psi5__interface.md#ga5f43079d704d882ae014c7a15bde6406)typedef void (\*[psi5\_rx\_frame\_callback\_t](group__psi5__interface.md#ga5f43079d704d882ae014c7a15bde6406))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

94 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_frame, void \*user\_data);

95

97

102typedef int (\*psi5\_start\_sync\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

103

108typedef int (\*psi5\_stop\_sync\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

109

114typedef int (\*psi5\_send\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

115 [k\_timeout\_t](structk__timeout__t.md) timeout, [psi5\_tx\_callback\_t](group__psi5__interface.md#gaac8c99036369b14d639cfb82f3b9cd32) callback, void \*user\_data);

116

120struct psi5\_rx\_callback\_config {

122 [psi5\_rx\_frame\_callback\_t](group__psi5__interface.md#ga5f43079d704d882ae014c7a15bde6406) callback;

124 struct [psi5\_frame](structpsi5__frame.md) \*frame;

126 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_num\_frame;

128 void \*user\_data;

129};

130

134struct psi5\_rx\_callback\_configs {

136 struct psi5\_rx\_callback\_config \*serial\_frame;

138 struct psi5\_rx\_callback\_config \*data\_frame;

139};

140

145typedef int (\*psi5\_register\_callback\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

146 struct psi5\_rx\_callback\_configs callback\_configs);

147

148\_\_subsystem struct psi5\_driver\_api {

149 psi5\_start\_sync\_t start\_sync;

150 psi5\_stop\_sync\_t stop\_sync;

151 psi5\_send\_t [send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f);

152 psi5\_register\_callback\_t register\_callback;

153};

154

156

[ 167](group__psi5__interface.md#gabbc2a744edf1ab01e7bd9321054cf32b)\_\_syscall int [psi5\_start\_sync](group__psi5__interface.md#gabbc2a744edf1ab01e7bd9321054cf32b)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

168

169static inline int z\_impl\_psi5\_start\_sync(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel)

170{

171 const struct psi5\_driver\_api \*api = (const struct psi5\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

172

173 if (api->start\_sync) {

174 return api->start\_sync(dev, channel);

175 }

176

177 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

178}

179

[ 190](group__psi5__interface.md#gacebce085be1e554e3faa7b69fd8da61f)\_\_syscall int [psi5\_stop\_sync](group__psi5__interface.md#gacebce085be1e554e3faa7b69fd8da61f)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

191

192static inline int z\_impl\_psi5\_stop\_sync(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel)

193{

194 const struct psi5\_driver\_api \*api = (const struct psi5\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

195

196 if (api->stop\_sync) {

197 return api->stop\_sync(dev, channel);

198 }

199

200 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

201}

202

[ 225](group__psi5__interface.md#ga3a27606e2828206608a79ada7238466d)\_\_syscall int [psi5\_send](group__psi5__interface.md#ga3a27606e2828206608a79ada7238466d)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data,

226 [k\_timeout\_t](structk__timeout__t.md) timeout, [psi5\_tx\_callback\_t](group__psi5__interface.md#gaac8c99036369b14d639cfb82f3b9cd32) callback, void \*user\_data);

227

228static inline int z\_impl\_psi5\_send(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data,

229 [k\_timeout\_t](structk__timeout__t.md) timeout, [psi5\_tx\_callback\_t](group__psi5__interface.md#gaac8c99036369b14d639cfb82f3b9cd32) callback,

230 void \*user\_data)

231{

232 const struct psi5\_driver\_api \*api = (const struct psi5\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

233

234 if (api->send) {

235 return api->send(dev, channel, data, timeout, callback, user\_data);

236 }

237

238 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

239}

240

[ 253](group__psi5__interface.md#ga37b0fcdecd4629c5f2657b1cc2e227b4)\_\_syscall int [psi5\_register\_callback](group__psi5__interface.md#ga37b0fcdecd4629c5f2657b1cc2e227b4)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

254 struct psi5\_rx\_callback\_configs callback\_configs);

255

256static inline int z\_impl\_psi5\_register\_callback(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

257 struct psi5\_rx\_callback\_configs callback\_configs)

258{

259 const struct psi5\_driver\_api \*api = (const struct psi5\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

260

261 if (api->register\_callback) {

262 return api->register\_callback(dev, channel, callback\_configs);

263 }

264

265 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

266}

267

268#ifdef \_\_cplusplus

269}

270#endif

271

275

276#include <zephyr/syscalls/psi5.h>

277

278#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PSI5\_H\_ \*/

[device.h](device_8h.md)

[psi5\_register\_callback](group__psi5__interface.md#ga37b0fcdecd4629c5f2657b1cc2e227b4)

int psi5\_register\_callback(const struct device \*dev, uint8\_t channel, struct psi5\_rx\_callback\_configs callback\_configs)

Add a callback function to handle messages received for a specific channel.

[psi5\_send](group__psi5__interface.md#ga3a27606e2828206608a79ada7238466d)

int psi5\_send(const struct device \*dev, uint8\_t channel, const uint64\_t data, k\_timeout\_t timeout, psi5\_tx\_callback\_t callback, void \*user\_data)

Transmitting PSI5 data on a specific channel.

[psi5\_frame\_type](group__psi5__interface.md#ga5cb0ef3be35e9ff2d05c39cc17f2659f)

psi5\_frame\_type

PSI5 frame type.

**Definition** psi5.h:34

[psi5\_rx\_frame\_callback\_t](group__psi5__interface.md#ga5f43079d704d882ae014c7a15bde6406)

void(\* psi5\_rx\_frame\_callback\_t)(const struct device \*dev, uint8\_t channel, uint32\_t num\_frame, void \*user\_data)

Defines the application callback handler function signature for receiving frame.

**Definition** psi5.h:93

[psi5\_tx\_callback\_t](group__psi5__interface.md#gaac8c99036369b14d639cfb82f3b9cd32)

void(\* psi5\_tx\_callback\_t)(const struct device \*dev, uint8\_t channel, int status, void \*user\_data)

Defines the application callback handler function signature for sending.

**Definition** psi5.h:82

[psi5\_start\_sync](group__psi5__interface.md#gabbc2a744edf1ab01e7bd9321054cf32b)

int psi5\_start\_sync(const struct device \*dev, uint8\_t channel)

Start the sync pulse generator on a specific channel.

[psi5\_stop\_sync](group__psi5__interface.md#gacebce085be1e554e3faa7b69fd8da61f)

int psi5\_stop\_sync(const struct device \*dev, uint8\_t channel)

Stop the sync pulse generator on a specific channel.

[PSI5\_SERIAL\_FRAME\_4\_BIT\_ID](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff)

@ PSI5\_SERIAL\_FRAME\_4\_BIT\_ID

Serial message frame with 4-bit message ID.

**Definition** psi5.h:36

[PSI5\_DATA\_FRAME](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f)

@ PSI5\_DATA\_FRAME

Data frame.

**Definition** psi5.h:40

[PSI5\_SERIAL\_FRAME\_8\_BIT\_ID](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a)

@ PSI5\_SERIAL\_FRAME\_8\_BIT\_ID

Serial message frame with 8-bit message ID.

**Definition** psi5.h:38

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[kernel.h](kernel_8h.md)

Public kernel APIs.

[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)

ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

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

**Definition** device.h:510

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:520

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[psi5\_frame](structpsi5__frame.md)

PSI5 frame structure.

**Definition** psi5.h:46

[psi5\_frame::serial](structpsi5__frame.md#a04a7d9d8d1238c823d787543ba2188c3)

struct psi5\_frame::@147241062307066365063355040330314077045061376046::@244231317137073265156064012154356353030045277135 serial

Serial message.

[psi5\_frame::data](structpsi5__frame.md#a159d66a7eeee3ffc6714f5058ddeefe9)

uint32\_t data

Message data.

**Definition** psi5.h:52

[psi5\_frame::timestamp](structpsi5__frame.md#a3b7f3b38ab831e2789c326a327a05e53)

uint32\_t timestamp

Timestamp of when the frame was captured.

**Definition** psi5.h:66

[psi5\_frame::type](structpsi5__frame.md#a975b56a545604103687679c2cb0561eb)

enum psi5\_frame\_type type

Type of PSI5 frame.

**Definition** psi5.h:48

[psi5\_frame::crc](structpsi5__frame.md#abd146305031fa97378b96d46e3e6e97d)

uint8\_t crc

CRC checksum for message integrity validation.

**Definition** psi5.h:68

[psi5\_frame::id](structpsi5__frame.md#ad32ba54088b03cbd4b91e77d9adadec8)

uint8\_t id

Serial message ID.

**Definition** psi5.h:59

[psi5\_frame::slot\_number](structpsi5__frame.md#aec97ec5f2ebef6903fd0b98d8fd2bec4)

uint8\_t slot\_number

Slot Number.

**Definition** psi5.h:70

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [psi5](dir_30659d2cb58c9650599fdf2ac54f2854.md)
- [psi5.h](psi5_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
