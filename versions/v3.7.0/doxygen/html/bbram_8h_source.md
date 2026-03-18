---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bbram_8h_source.html
original_path: doxygen/html/bbram_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bbram.h

[Go to the documentation of this file.](bbram_8h.md)

1/\*

2 \* Copyright (c) 2021 Google Inc

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_BBRAM\_H

8#define ZEPHYR\_INCLUDE\_DRIVERS\_BBRAM\_H

9

10#include <[errno.h](errno_8h.md)>

11

12#include <[zephyr/device.h](device_8h.md)>

13

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

[ 31](group__bbram__interface.md#gac23658302662587043f3587080f798fe)typedef int (\*[bbram\_api\_check\_invalid\_t](group__bbram__interface.md#gac23658302662587043f3587080f798fe))(const struct [device](structdevice.md) \*dev);

32

[ 39](group__bbram__interface.md#ga99adefcb89ab80d8b5e24b8ffad8f43e)typedef int (\*[bbram\_api\_check\_standby\_power\_t](group__bbram__interface.md#ga99adefcb89ab80d8b5e24b8ffad8f43e))(const struct [device](structdevice.md) \*dev);

40

[ 47](group__bbram__interface.md#gaa6edc8a61529edad90de2e6fff619fdf)typedef int (\*[bbram\_api\_check\_power\_t](group__bbram__interface.md#gaa6edc8a61529edad90de2e6fff619fdf))(const struct [device](structdevice.md) \*dev);

48

[ 55](group__bbram__interface.md#gacfa586f705c520a6a05638a2e289fe50)typedef int (\*[bbram\_api\_get\_size\_t](group__bbram__interface.md#gacfa586f705c520a6a05638a2e289fe50))(const struct [device](structdevice.md) \*dev, size\_t \*size);

56

[ 63](group__bbram__interface.md#ga8b06a1b3bb9b524597804dd268904881)typedef int (\*[bbram\_api\_read\_t](group__bbram__interface.md#ga8b06a1b3bb9b524597804dd268904881))(const struct [device](structdevice.md) \*dev, size\_t offset, size\_t size,

64 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

65

[ 72](group__bbram__interface.md#ga1b111ae421791b9544777c1bab5e2a02)typedef int (\*[bbram\_api\_write\_t](group__bbram__interface.md#ga1b111ae421791b9544777c1bab5e2a02))(const struct [device](structdevice.md) \*dev, size\_t offset, size\_t size,

73 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

74

[ 75](structbbram__driver__api.md)\_\_subsystem struct [bbram\_driver\_api](structbbram__driver__api.md) {

[ 76](structbbram__driver__api.md#a04c9f9487d35a0c2d264d033ef266fc7) [bbram\_api\_check\_invalid\_t](group__bbram__interface.md#gac23658302662587043f3587080f798fe) [check\_invalid](structbbram__driver__api.md#a04c9f9487d35a0c2d264d033ef266fc7);

[ 77](structbbram__driver__api.md#a4c3813853e2364109ea1b481277f2816) [bbram\_api\_check\_standby\_power\_t](group__bbram__interface.md#ga99adefcb89ab80d8b5e24b8ffad8f43e) [check\_standby\_power](structbbram__driver__api.md#a4c3813853e2364109ea1b481277f2816);

[ 78](structbbram__driver__api.md#a6df89dfb1ce05bc557286bc894751702) [bbram\_api\_check\_power\_t](group__bbram__interface.md#gaa6edc8a61529edad90de2e6fff619fdf) [check\_power](structbbram__driver__api.md#a6df89dfb1ce05bc557286bc894751702);

[ 79](structbbram__driver__api.md#a15809ed9c49ade6de1ddbc7e48072b12) [bbram\_api\_get\_size\_t](group__bbram__interface.md#gacfa586f705c520a6a05638a2e289fe50) [get\_size](structbbram__driver__api.md#a15809ed9c49ade6de1ddbc7e48072b12);

[ 80](structbbram__driver__api.md#a50a91db769c65d4e9dceb027c5bc956d) [bbram\_api\_read\_t](group__bbram__interface.md#ga8b06a1b3bb9b524597804dd268904881) [read](structbbram__driver__api.md#a50a91db769c65d4e9dceb027c5bc956d);

[ 81](structbbram__driver__api.md#a937578d674e8ed1e26026aea7428e616) [bbram\_api\_write\_t](group__bbram__interface.md#ga1b111ae421791b9544777c1bab5e2a02) [write](structbbram__driver__api.md#a937578d674e8ed1e26026aea7428e616);

82};

83

[ 93](group__bbram__interface.md#ga7164969f308616696a9ab71a4d19b70b)\_\_syscall int [bbram\_check\_invalid](group__bbram__interface.md#ga7164969f308616696a9ab71a4d19b70b)(const struct [device](structdevice.md) \*dev);

94

95static inline int z\_impl\_bbram\_check\_invalid(const struct [device](structdevice.md) \*dev)

96{

97 const struct [bbram\_driver\_api](structbbram__driver__api.md) \*api =

98 (const struct [bbram\_driver\_api](structbbram__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

99

100 if (!api->check\_invalid) {

101 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

102 }

103

104 return api->check\_invalid(dev);

105}

106

[ 115](group__bbram__interface.md#ga948ed0a7d3824f950ad46b99ba3d86f4)\_\_syscall int [bbram\_check\_standby\_power](group__bbram__interface.md#ga948ed0a7d3824f950ad46b99ba3d86f4)(const struct [device](structdevice.md) \*dev);

116

117static inline int z\_impl\_bbram\_check\_standby\_power(const struct [device](structdevice.md) \*dev)

118{

119 const struct [bbram\_driver\_api](structbbram__driver__api.md) \*api =

120 (const struct [bbram\_driver\_api](structbbram__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

121

122 if (!api->check\_standby\_power) {

123 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

124 }

125

126 return api->check\_standby\_power(dev);

127}

128

[ 138](group__bbram__interface.md#ga8fc2a647bda90e96f866514300180a96)\_\_syscall int [bbram\_check\_power](group__bbram__interface.md#ga8fc2a647bda90e96f866514300180a96)(const struct [device](structdevice.md) \*dev);

139

140static inline int z\_impl\_bbram\_check\_power(const struct [device](structdevice.md) \*dev)

141{

142 const struct [bbram\_driver\_api](structbbram__driver__api.md) \*api =

143 (const struct [bbram\_driver\_api](structbbram__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

144

145 if (!api->check\_power) {

146 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

147 }

148

149 return api->check\_power(dev);

150}

151

[ 159](group__bbram__interface.md#gab6bdb4a1cba88ca645c256366a696bdd)\_\_syscall int [bbram\_get\_size](group__bbram__interface.md#gab6bdb4a1cba88ca645c256366a696bdd)(const struct [device](structdevice.md) \*dev, size\_t \*size);

160

161static inline int z\_impl\_bbram\_get\_size(const struct [device](structdevice.md) \*dev, size\_t \*size)

162{

163 const struct [bbram\_driver\_api](structbbram__driver__api.md) \*api =

164 (const struct [bbram\_driver\_api](structbbram__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

165

166 if (!api->get\_size) {

167 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

168 }

169

170 return api->get\_size(dev, size);

171}

172

[ 182](group__bbram__interface.md#ga9ef786b0fbac3f8523be2bb87b7cff7b)\_\_syscall int [bbram\_read](group__bbram__interface.md#ga9ef786b0fbac3f8523be2bb87b7cff7b)(const struct [device](structdevice.md) \*dev, size\_t offset, size\_t size,

183 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

184

185static inline int z\_impl\_bbram\_read(const struct [device](structdevice.md) \*dev, size\_t offset,

186 size\_t size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

187{

188 const struct [bbram\_driver\_api](structbbram__driver__api.md) \*api =

189 (const struct [bbram\_driver\_api](structbbram__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

190

191 if (!api->read) {

192 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

193 }

194

195 return api->read(dev, offset, size, data);

196}

197

[ 207](group__bbram__interface.md#ga51007eed4820aed341d20e4562607564)\_\_syscall int [bbram\_write](group__bbram__interface.md#ga51007eed4820aed341d20e4562607564)(const struct [device](structdevice.md) \*dev, size\_t offset, size\_t size,

208 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

209

210static inline int z\_impl\_bbram\_write(const struct [device](structdevice.md) \*dev, size\_t offset,

211 size\_t size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

212{

213 const struct [bbram\_driver\_api](structbbram__driver__api.md) \*api =

214 (const struct [bbram\_driver\_api](structbbram__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

215

216 if (!api->write) {

217 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

218 }

219

220 return api->write(dev, offset, size, data);

221}

222

[ 232](group__bbram__interface.md#gae2b89f8a44e38fe7df2219397bad139b)int [bbram\_emul\_set\_invalid](group__bbram__interface.md#gae2b89f8a44e38fe7df2219397bad139b)(const struct [device](structdevice.md) \*dev, bool is\_invalid);

233

[ 243](group__bbram__interface.md#ga08a2c565ba0ec6ac5894a718a652eec2)int [bbram\_emul\_set\_standby\_power\_state](group__bbram__interface.md#ga08a2c565ba0ec6ac5894a718a652eec2)(const struct [device](structdevice.md) \*dev, bool failure);

244

[ 254](group__bbram__interface.md#gadc0243187b853832b08af36c9baf9cb0)int [bbram\_emul\_set\_power\_state](group__bbram__interface.md#gadc0243187b853832b08af36c9baf9cb0)(const struct [device](structdevice.md) \*dev, bool failure);

255

256#ifdef \_\_cplusplus

257}

258#endif

259

263

264#include <zephyr/syscalls/bbram.h>

265

266#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_BBRAM\_H \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[bbram\_emul\_set\_standby\_power\_state](group__bbram__interface.md#ga08a2c565ba0ec6ac5894a718a652eec2)

int bbram\_emul\_set\_standby\_power\_state(const struct device \*dev, bool failure)

Set the emulated BBRAM driver's standby power state.

[bbram\_api\_write\_t](group__bbram__interface.md#ga1b111ae421791b9544777c1bab5e2a02)

int(\* bbram\_api\_write\_t)(const struct device \*dev, size\_t offset, size\_t size, const uint8\_t \*data)

API template to write to BBRAM.

**Definition** bbram.h:72

[bbram\_write](group__bbram__interface.md#ga51007eed4820aed341d20e4562607564)

int bbram\_write(const struct device \*dev, size\_t offset, size\_t size, const uint8\_t \*data)

Write bytes to BBRAM.

[bbram\_check\_invalid](group__bbram__interface.md#ga7164969f308616696a9ab71a4d19b70b)

int bbram\_check\_invalid(const struct device \*dev)

Check if BBRAM is invalid.

[bbram\_api\_read\_t](group__bbram__interface.md#ga8b06a1b3bb9b524597804dd268904881)

int(\* bbram\_api\_read\_t)(const struct device \*dev, size\_t offset, size\_t size, uint8\_t \*data)

API template to read from BBRAM.

**Definition** bbram.h:63

[bbram\_check\_power](group__bbram__interface.md#ga8fc2a647bda90e96f866514300180a96)

int bbram\_check\_power(const struct device \*dev)

Check for V CC1 power failure.

[bbram\_check\_standby\_power](group__bbram__interface.md#ga948ed0a7d3824f950ad46b99ba3d86f4)

int bbram\_check\_standby\_power(const struct device \*dev)

Check for standby (Volt SBY) power failure.

[bbram\_api\_check\_standby\_power\_t](group__bbram__interface.md#ga99adefcb89ab80d8b5e24b8ffad8f43e)

int(\* bbram\_api\_check\_standby\_power\_t)(const struct device \*dev)

API template to check for standby power failure.

**Definition** bbram.h:39

[bbram\_read](group__bbram__interface.md#ga9ef786b0fbac3f8523be2bb87b7cff7b)

int bbram\_read(const struct device \*dev, size\_t offset, size\_t size, uint8\_t \*data)

Read bytes from BBRAM.

[bbram\_api\_check\_power\_t](group__bbram__interface.md#gaa6edc8a61529edad90de2e6fff619fdf)

int(\* bbram\_api\_check\_power\_t)(const struct device \*dev)

API template to check for V CC1 power failure.

**Definition** bbram.h:47

[bbram\_get\_size](group__bbram__interface.md#gab6bdb4a1cba88ca645c256366a696bdd)

int bbram\_get\_size(const struct device \*dev, size\_t \*size)

Get the size of the BBRAM (in bytes).

[bbram\_api\_check\_invalid\_t](group__bbram__interface.md#gac23658302662587043f3587080f798fe)

int(\* bbram\_api\_check\_invalid\_t)(const struct device \*dev)

API template to check if the BBRAM is invalid.

**Definition** bbram.h:31

[bbram\_api\_get\_size\_t](group__bbram__interface.md#gacfa586f705c520a6a05638a2e289fe50)

int(\* bbram\_api\_get\_size\_t)(const struct device \*dev, size\_t \*size)

API template to check the size of the BBRAM.

**Definition** bbram.h:55

[bbram\_emul\_set\_power\_state](group__bbram__interface.md#gadc0243187b853832b08af36c9baf9cb0)

int bbram\_emul\_set\_power\_state(const struct device \*dev, bool failure)

Set the emulated BBRAM driver's power state.

[bbram\_emul\_set\_invalid](group__bbram__interface.md#gae2b89f8a44e38fe7df2219397bad139b)

int bbram\_emul\_set\_invalid(const struct device \*dev, bool is\_invalid)

Set the emulated BBRAM driver's invalid state.

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bbram\_driver\_api](structbbram__driver__api.md)

**Definition** bbram.h:75

[bbram\_driver\_api::check\_invalid](structbbram__driver__api.md#a04c9f9487d35a0c2d264d033ef266fc7)

bbram\_api\_check\_invalid\_t check\_invalid

**Definition** bbram.h:76

[bbram\_driver\_api::get\_size](structbbram__driver__api.md#a15809ed9c49ade6de1ddbc7e48072b12)

bbram\_api\_get\_size\_t get\_size

**Definition** bbram.h:79

[bbram\_driver\_api::check\_standby\_power](structbbram__driver__api.md#a4c3813853e2364109ea1b481277f2816)

bbram\_api\_check\_standby\_power\_t check\_standby\_power

**Definition** bbram.h:77

[bbram\_driver\_api::read](structbbram__driver__api.md#a50a91db769c65d4e9dceb027c5bc956d)

bbram\_api\_read\_t read

**Definition** bbram.h:80

[bbram\_driver\_api::check\_power](structbbram__driver__api.md#a6df89dfb1ce05bc557286bc894751702)

bbram\_api\_check\_power\_t check\_power

**Definition** bbram.h:78

[bbram\_driver\_api::write](structbbram__driver__api.md#a937578d674e8ed1e26026aea7428e616)

bbram\_api\_write\_t write

**Definition** bbram.h:81

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bbram.h](bbram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
