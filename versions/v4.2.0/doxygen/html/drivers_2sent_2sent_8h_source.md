---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2sent_2sent_8h_source.html
original_path: doxygen/html/drivers_2sent_2sent_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sent.h

[Go to the documentation of this file.](drivers_2sent_2sent_8h.md)

1/\*

2 \* Copyright 2025 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENT\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SENT\_H\_

14

15#include <[zephyr/kernel.h](kernel_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

30

[ 34](group__sent__interface.md#ga069232b79943be845df411539ef04993)enum [sent\_frame\_type](group__sent__interface.md#ga069232b79943be845df411539ef04993) {

[ 36](group__sent__interface.md#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5) [SENT\_SHORT\_SERIAL\_FRAME](group__sent__interface.md#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5),

[ 38](group__sent__interface.md#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73) [SENT\_ENHANCED\_SERIAL\_FRAME\_4\_BIT\_ID](group__sent__interface.md#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73),

[ 40](group__sent__interface.md#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137) [SENT\_ENHANCED\_SERIAL\_FRAME\_8\_BIT\_ID](group__sent__interface.md#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137),

[ 42](group__sent__interface.md#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1) [SENT\_FAST\_FRAME](group__sent__interface.md#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1)

43};

44

[ 48](group__sent__interface.md#ga19bb6e9149dfb7af97ca90289e33bdac)#define SENT\_MAX\_DATA\_NIBBLES 8

49

[ 53](structsent__frame.md)struct [sent\_frame](structsent__frame.md) {

[ 55](structsent__frame.md#aafd880b826c351481b384b5fef106068) enum [sent\_frame\_type](group__sent__interface.md#ga069232b79943be845df411539ef04993) [type](structsent__frame.md#aafd880b826c351481b384b5fef106068);

56

57 union {

61 struct {

[ 63](structsent__frame.md#a689cb24f6c8049e6282ca30939430c8f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structsent__frame.md#a689cb24f6c8049e6282ca30939430c8f);

64

[ 66](structsent__frame.md#a43d52380608b7683534dc31873a396af) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data](structsent__frame.md#a43d52380608b7683534dc31873a396af);

[ 67](structsent__frame.md#ab39f8ecf19e198ca4818fb13d522c6f4) } [serial](structsent__frame.md#ab39f8ecf19e198ca4818fb13d522c6f4);

68

72 struct {

[ 74](structsent__frame.md#a4bef9a0871e8ecd86b6753e5bb46c6a0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_nibbles](structsent__frame.md#a4bef9a0871e8ecd86b6753e5bb46c6a0)[[SENT\_MAX\_DATA\_NIBBLES](group__sent__interface.md#ga19bb6e9149dfb7af97ca90289e33bdac)];

[ 75](structsent__frame.md#a1c02dabd2b0605b77683daf17fc7980b) } [fast](structsent__frame.md#a1c02dabd2b0605b77683daf17fc7980b);

76 };

77

[ 79](structsent__frame.md#aae185d5b024a3d9afc135ecc19c9410f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timestamp](structsent__frame.md#aae185d5b024a3d9afc135ecc19c9410f);

80

[ 82](structsent__frame.md#a648203dab36ae27e874a171c71d92fe8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [crc](structsent__frame.md#a648203dab36ae27e874a171c71d92fe8);

83};

84

[ 93](group__sent__interface.md#ga47d05656177dae0a388e1155be82494f)typedef void (\*[sent\_rx\_frame\_callback\_t](group__sent__interface.md#ga47d05656177dae0a388e1155be82494f))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

94 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_frame, void \*user\_data);

95

97

102typedef int (\*sent\_start\_listening\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

103

108typedef int (\*sent\_stop\_listening\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

109

113struct sent\_rx\_callback\_config {

115 [sent\_rx\_frame\_callback\_t](group__sent__interface.md#ga47d05656177dae0a388e1155be82494f) callback;

117 struct [sent\_frame](structsent__frame.md) \*frame;

119 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_num\_frame;

121 void \*user\_data;

122};

123

127struct sent\_rx\_callback\_configs {

129 struct sent\_rx\_callback\_config \*serial;

131 struct sent\_rx\_callback\_config \*fast;

132};

133

138typedef int (\*sent\_register\_callback\_t)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

139 struct sent\_rx\_callback\_configs callback\_configs);

140

141\_\_subsystem struct sent\_driver\_api {

142 sent\_start\_listening\_t start\_listening;

143 sent\_stop\_listening\_t stop\_listening;

144 sent\_register\_callback\_t register\_callback;

145};

146

148

[ 159](group__sent__interface.md#ga227aafdbe8f93dbdb97f3969517e6c63)\_\_syscall int [sent\_start\_listening](group__sent__interface.md#ga227aafdbe8f93dbdb97f3969517e6c63)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

160

161static inline int z\_impl\_sent\_start\_listening(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel)

162{

163 const struct sent\_driver\_api \*api = (const struct sent\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

164

165 if (api->start\_listening) {

166 return api->start\_listening(dev, channel);

167 }

168

169 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

170}

171

[ 182](group__sent__interface.md#gae1eacde97297c97e27b67a7ae7e121cb)\_\_syscall int [sent\_stop\_listening](group__sent__interface.md#gae1eacde97297c97e27b67a7ae7e121cb)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

183

184static inline int z\_impl\_sent\_stop\_listening(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel)

185{

186 const struct sent\_driver\_api \*api = (const struct sent\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

187

188 if (api->stop\_listening) {

189 return api->stop\_listening(dev, channel);

190 }

191

192 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

193}

194

[ 204](group__sent__interface.md#ga9deb810297f7d42159187bbb8dddb8d2)\_\_syscall int [sent\_register\_callback](group__sent__interface.md#ga9deb810297f7d42159187bbb8dddb8d2)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

205 struct sent\_rx\_callback\_configs callback\_configs);

206

207static inline int z\_impl\_sent\_register\_callback(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

208 struct sent\_rx\_callback\_configs callback\_configs)

209{

210 const struct sent\_driver\_api \*api = (const struct sent\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

211

212 if (api->register\_callback) {

213 return api->register\_callback(dev, channel, callback\_configs);

214 }

215

216 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

217}

218

219#ifdef \_\_cplusplus

220}

221#endif

222

226

227#include <zephyr/syscalls/sent.h>

228

229#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENT\_H\_ \*/

[device.h](device_8h.md)

[sent\_frame\_type](group__sent__interface.md#ga069232b79943be845df411539ef04993)

sent\_frame\_type

SENT frame type.

**Definition** sent.h:34

[SENT\_MAX\_DATA\_NIBBLES](group__sent__interface.md#ga19bb6e9149dfb7af97ca90289e33bdac)

#define SENT\_MAX\_DATA\_NIBBLES

Maximum number of data nibbles.

**Definition** sent.h:48

[sent\_start\_listening](group__sent__interface.md#ga227aafdbe8f93dbdb97f3969517e6c63)

int sent\_start\_listening(const struct device \*dev, uint8\_t channel)

Enable a specific channel to start receiving from the bus.

[sent\_rx\_frame\_callback\_t](group__sent__interface.md#ga47d05656177dae0a388e1155be82494f)

void(\* sent\_rx\_frame\_callback\_t)(const struct device \*dev, uint8\_t channel, uint32\_t num\_frame, void \*user\_data)

Defines the application callback handler function signature for receiving frame.

**Definition** sent.h:93

[sent\_register\_callback](group__sent__interface.md#ga9deb810297f7d42159187bbb8dddb8d2)

int sent\_register\_callback(const struct device \*dev, uint8\_t channel, struct sent\_rx\_callback\_configs callback\_configs)

Add a callback function to handle messages received for a specific channel.

[sent\_stop\_listening](group__sent__interface.md#gae1eacde97297c97e27b67a7ae7e121cb)

int sent\_stop\_listening(const struct device \*dev, uint8\_t channel)

Disable a specific channel to stop receiving from the bus.

[SENT\_ENHANCED\_SERIAL\_FRAME\_4\_BIT\_ID](group__sent__interface.md#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73)

@ SENT\_ENHANCED\_SERIAL\_FRAME\_4\_BIT\_ID

Enhanced serial message frame with 4-bit message ID.

**Definition** sent.h:38

[SENT\_SHORT\_SERIAL\_FRAME](group__sent__interface.md#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5)

@ SENT\_SHORT\_SERIAL\_FRAME

Short serial message frame.

**Definition** sent.h:36

[SENT\_ENHANCED\_SERIAL\_FRAME\_8\_BIT\_ID](group__sent__interface.md#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137)

@ SENT\_ENHANCED\_SERIAL\_FRAME\_8\_BIT\_ID

Enhanced serial message frame with 8-bit message ID.

**Definition** sent.h:40

[SENT\_FAST\_FRAME](group__sent__interface.md#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1)

@ SENT\_FAST\_FRAME

Fast message frame.

**Definition** sent.h:42

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:516

[sent\_frame](structsent__frame.md)

SENT frame structure.

**Definition** sent.h:53

[sent\_frame::fast](structsent__frame.md#a1c02dabd2b0605b77683daf17fc7980b)

struct sent\_frame::@073352004002173133105234200026220315236122230346::@052310202357350204237047306111207070070357322354 fast

Fast message.

[sent\_frame::data](structsent__frame.md#a43d52380608b7683534dc31873a396af)

uint16\_t data

Serial message data.

**Definition** sent.h:66

[sent\_frame::data\_nibbles](structsent__frame.md#a4bef9a0871e8ecd86b6753e5bb46c6a0)

uint8\_t data\_nibbles[8]

Array of fast message data nibbles.

**Definition** sent.h:74

[sent\_frame::crc](structsent__frame.md#a648203dab36ae27e874a171c71d92fe8)

uint8\_t crc

CRC checksum for message integrity validation.

**Definition** sent.h:82

[sent\_frame::id](structsent__frame.md#a689cb24f6c8049e6282ca30939430c8f)

uint8\_t id

Serial message ID.

**Definition** sent.h:63

[sent\_frame::timestamp](structsent__frame.md#aae185d5b024a3d9afc135ecc19c9410f)

uint32\_t timestamp

Timestamp of when the frame was captured.

**Definition** sent.h:79

[sent\_frame::type](structsent__frame.md#aafd880b826c351481b384b5fef106068)

enum sent\_frame\_type type

Type of SENT frame.

**Definition** sent.h:55

[sent\_frame::serial](structsent__frame.md#ab39f8ecf19e198ca4818fb13d522c6f4)

struct sent\_frame::@073352004002173133105234200026220315236122230346::@200101137234253347137231003000335224000042211161 serial

Serial message.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sent](dir_c7c606dbfefe42cf24a6f31b226e5895.md)
- [sent.h](drivers_2sent_2sent_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
