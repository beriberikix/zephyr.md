---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sensing_8h_source.html
original_path: doxygen/html/sensing_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing.h

[Go to the documentation of this file.](sensing_8h.md)

1/\*

2 \* Copyright (c) 2022-2023 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SENSING\_H\_

8#define ZEPHYR\_INCLUDE\_SENSING\_H\_

9

19

20#include <[zephyr/sensing/sensing\_datatypes.h](sensing__datatypes_8h.md)>

21#include <[zephyr/sensing/sensing\_sensor\_types.h](sensing__sensor__types_8h.md)>

22#include <[zephyr/device.h](device_8h.md)>

23

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

34

[ 39](structsensing__sensor__version.md)struct [sensing\_sensor\_version](structsensing__sensor__version.md) {

40 union {

[ 41](structsensing__sensor__version.md#a0023cbb5114f4a3d3a1cf388e5034cfc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [value](structsensing__sensor__version.md#a0023cbb5114f4a3d3a1cf388e5034cfc);

42 struct {

[ 43](structsensing__sensor__version.md#ad7275123dd08f06ee0307325c8f5fb37) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [major](structsensing__sensor__version.md#ad7275123dd08f06ee0307325c8f5fb37);

[ 44](structsensing__sensor__version.md#a8d41ea3c181c7062aa8f76b17c652b41) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minor](structsensing__sensor__version.md#a8d41ea3c181c7062aa8f76b17c652b41);

[ 45](structsensing__sensor__version.md#a10fe885cd0cd9a6a5209308e188def3d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hotfix](structsensing__sensor__version.md#a10fe885cd0cd9a6a5209308e188def3d);

[ 46](structsensing__sensor__version.md#a668f5d23171c38e1cc13a4221e639815) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [build](structsensing__sensor__version.md#a668f5d23171c38e1cc13a4221e639815);

47 };

48 };

49};

50

[ 51](group__sensing__api.md#ga180bc8c822f125204964f3c667464273)#define SENSING\_SENSOR\_VERSION(\_major, \_minor, \_hotfix, \_build) \

52 (FIELD\_PREP(GENMASK(31, 24), \_major) | \

53 FIELD\_PREP(GENMASK(23, 16), \_minor) | \

54 FIELD\_PREP(GENMASK(15, 8), \_hotfix) | \

55 FIELD\_PREP(GENMASK(7, 0), \_build))

56

57

[ 64](group__sensing__api.md#ga498dcf4dbd0eb42d8ca399df4acc2e5e)#define SENSING\_SENSOR\_FLAG\_REPORT\_ON\_EVENT BIT(0)

65

[ 73](group__sensing__api.md#ga8b9766509e66fd8b8fa8e718a1544137)#define SENSING\_SENSOR\_FLAG\_REPORT\_ON\_CHANGE BIT(1)

74

[ 79](group__sensing__api.md#ga16ac7bd397836280f7e8b4aa82f8eb4c)#define SENSING\_SENSITIVITY\_INDEX\_ALL -1

80

[ 85](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06)enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) {

[ 86](group__sensing__api.md#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93) [SENSING\_SENSOR\_STATE\_READY](group__sensing__api.md#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93) = 0,

[ 87](group__sensing__api.md#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e) [SENSING\_SENSOR\_STATE\_OFFLINE](group__sensing__api.md#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e) = 1,

88};

89

[ 94](group__sensing__api.md#ga69d2ae9f45215742654bfc7e4676e6f2)enum [sensing\_sensor\_attribute](group__sensing__api.md#ga69d2ae9f45215742654bfc7e4676e6f2) {

[ 95](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3) [SENSING\_SENSOR\_ATTRIBUTE\_INTERVAL](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3) = 0,

[ 96](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b) [SENSING\_SENSOR\_ATTRIBUTE\_SENSITIVITY](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b) = 1,

[ 97](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476) [SENSING\_SENSOR\_ATTRIBUTE\_LATENCY](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476) = 2,

[ 98](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980) [SENSING\_SENSOR\_ATTRIBUTE\_MAX](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980),

99};

100

101

[ 106](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293)typedef void \*[sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293);

107

108

[ 116](group__sensing__api.md#ga5440a8914b664209d62388183b3c89ea)typedef void (\*[sensing\_data\_event\_t](group__sensing__api.md#ga5440a8914b664209d62388183b3c89ea))(

117 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) handle,

118 const void \*buf,

119 void \*context);

120

[ 126](structsensing__sensor__info.md)struct [sensing\_sensor\_info](structsensing__sensor__info.md) {

[ 128](structsensing__sensor__info.md#ac7b4f33115f7a7a24095ca90b1e7acfe) const char \*[name](structsensing__sensor__info.md#ac7b4f33115f7a7a24095ca90b1e7acfe);

129

[ 131](structsensing__sensor__info.md#aa3e056ad9c52c3388e049b08d0844b49) const char \*[friendly\_name](structsensing__sensor__info.md#aa3e056ad9c52c3388e049b08d0844b49);

132

[ 134](structsensing__sensor__info.md#a085e8c00586c61245b822c7ea9db9c98) const char \*[vendor](structsensing__sensor__info.md#a085e8c00586c61245b822c7ea9db9c98);

135

[ 137](structsensing__sensor__info.md#ace77ba2ab5d5eee7c4e385fc2ea74ee8) const char \*[model](structsensing__sensor__info.md#ace77ba2ab5d5eee7c4e385fc2ea74ee8);

138

[ 140](structsensing__sensor__info.md#a6b20ad8747a95cf1dc7346374de6b855) const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [type](structsensing__sensor__info.md#a6b20ad8747a95cf1dc7346374de6b855);

141

[ 143](structsensing__sensor__info.md#a5b2ddf0829031098301e244f60741f2b) const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [minimal\_interval](structsensing__sensor__info.md#a5b2ddf0829031098301e244f60741f2b);

144};

145

[ 151](structsensing__callback__list.md)struct [sensing\_callback\_list](structsensing__callback__list.md) {

[ 152](structsensing__callback__list.md#a7d0d7c878e338f19fd48c66cda9d04fc) [sensing\_data\_event\_t](group__sensing__api.md#ga5440a8914b664209d62388183b3c89ea) [on\_data\_event](structsensing__callback__list.md#a7d0d7c878e338f19fd48c66cda9d04fc);

[ 153](structsensing__callback__list.md#a43504dbe7d484f0d0e7d33b8bb6318d4) void \*[context](structsensing__callback__list.md#a43504dbe7d484f0d0e7d33b8bb6318d4);

154};

155

[ 160](structsensing__sensor__config.md)struct [sensing\_sensor\_config](structsensing__sensor__config.md) {

[ 161](structsensing__sensor__config.md#a9bdf50a1018d6d9426efd991d05bf72b) enum [sensing\_sensor\_attribute](group__sensing__api.md#ga69d2ae9f45215742654bfc7e4676e6f2) [attri](structsensing__sensor__config.md#a9bdf50a1018d6d9426efd991d05bf72b);

162

[ 164](structsensing__sensor__config.md#ac4389c439db16cb25a2e622baf0aeb9b) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [data\_field](structsensing__sensor__config.md#ac4389c439db16cb25a2e622baf0aeb9b);

165

166 union {

[ 167](structsensing__sensor__config.md#a7512f7254f6960ed398150db23868965) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval](structsensing__sensor__config.md#a7512f7254f6960ed398150db23868965);

[ 168](structsensing__sensor__config.md#acc1270dbe02ff6324e0f66acbde8ce33) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sensitivity](structsensing__sensor__config.md#acc1270dbe02ff6324e0f66acbde8ce33);

[ 169](structsensing__sensor__config.md#af9d2ee27b3a04fd65baa1d1d0cb2badc) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [latency](structsensing__sensor__config.md#af9d2ee27b3a04fd65baa1d1d0cb2badc);

170 };

171};

172

173

[ 187](group__sensing__api.md#gaf3b6c66c2db12115f3ebec0cdba32e86)int [sensing\_get\_sensors](group__sensing__api.md#gaf3b6c66c2db12115f3ebec0cdba32e86)(int \*num\_sensors, const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*\*info);

188

[ 206](group__sensing__api.md#ga8e427d28efc492f15d762af3308d78cd)int [sensing\_open\_sensor](group__sensing__api.md#ga8e427d28efc492f15d762af3308d78cd)(

207 const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*info,

208 struct [sensing\_callback\_list](structsensing__callback__list.md) \*cb\_list,

209 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*handle);

210

[ 228](group__sensing__api.md#ga4218453664fee0aa61697018e3193e7a)int [sensing\_open\_sensor\_by\_dt](group__sensing__api.md#ga4218453664fee0aa61697018e3193e7a)(

229 const struct [device](structdevice.md) \*dev, struct [sensing\_callback\_list](structsensing__callback__list.md) \*cb\_list,

230 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*handle);

231

[ 239](group__sensing__api.md#ga98e49ea0e84e93867df20033d01ee66c)int [sensing\_close\_sensor](group__sensing__api.md#ga98e49ea0e84e93867df20033d01ee66c)(

240 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*handle);

241

[ 253](group__sensing__api.md#ga46591a2d29f5b5e160a72bbe289884ab)int [sensing\_set\_config](group__sensing__api.md#ga46591a2d29f5b5e160a72bbe289884ab)(

254 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) handle,

255 struct [sensing\_sensor\_config](structsensing__sensor__config.md) \*configs, int count);

256

[ 268](group__sensing__api.md#gaf4037066c9a7a9f3eb1c79a4d8ae0920)int [sensing\_get\_config](group__sensing__api.md#gaf4037066c9a7a9f3eb1c79a4d8ae0920)(

269 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) handle,

270 struct [sensing\_sensor\_config](structsensing__sensor__config.md) \*configs, int count);

271

[ 279](group__sensing__api.md#ga4399f2e03d4d9444045b705b13cb6dfd)const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*[sensing\_get\_sensor\_info](group__sensing__api.md#ga4399f2e03d4d9444045b705b13cb6dfd)(

280 [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) handle);

281

282#ifdef \_\_cplusplus

283}

284#endif

285

289

290

291#endif /\*ZEPHYR\_INCLUDE\_SENSING\_H\_\*/

[device.h](device_8h.md)

[sensing\_open\_sensor\_by\_dt](group__sensing__api.md#ga4218453664fee0aa61697018e3193e7a)

int sensing\_open\_sensor\_by\_dt(const struct device \*dev, struct sensing\_callback\_list \*cb\_list, sensing\_sensor\_handle\_t \*handle)

Open sensor instance by device.

[sensing\_get\_sensor\_info](group__sensing__api.md#ga4399f2e03d4d9444045b705b13cb6dfd)

const struct sensing\_sensor\_info \* sensing\_get\_sensor\_info(sensing\_sensor\_handle\_t handle)

Get sensor information from sensor instance handle.

[sensing\_set\_config](group__sensing__api.md#ga46591a2d29f5b5e160a72bbe289884ab)

int sensing\_set\_config(sensing\_sensor\_handle\_t handle, struct sensing\_sensor\_config \*configs, int count)

Set current config items to Sensing subsystem.

[sensing\_data\_event\_t](group__sensing__api.md#ga5440a8914b664209d62388183b3c89ea)

void(\* sensing\_data\_event\_t)(sensing\_sensor\_handle\_t handle, const void \*buf, void \*context)

Sensor data event receive callback.

**Definition** sensing.h:116

[sensing\_sensor\_attribute](group__sensing__api.md#ga69d2ae9f45215742654bfc7e4676e6f2)

sensing\_sensor\_attribute

Sensing subsystem sensor config attribute.

**Definition** sensing.h:94

[sensing\_open\_sensor](group__sensing__api.md#ga8e427d28efc492f15d762af3308d78cd)

int sensing\_open\_sensor(const struct sensing\_sensor\_info \*info, struct sensing\_callback\_list \*cb\_list, sensing\_sensor\_handle\_t \*handle)

Open sensor instance by sensing sensor info.

[sensing\_close\_sensor](group__sensing__api.md#ga98e49ea0e84e93867df20033d01ee66c)

int sensing\_close\_sensor(sensing\_sensor\_handle\_t \*handle)

Close sensor instance.

[sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06)

sensing\_sensor\_state

Sensing subsystem sensor state.

**Definition** sensing.h:85

[sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293)

void \* sensing\_sensor\_handle\_t

Define Sensing subsystem sensor handle.

**Definition** sensing.h:106

[sensing\_get\_sensors](group__sensing__api.md#gaf3b6c66c2db12115f3ebec0cdba32e86)

int sensing\_get\_sensors(int \*num\_sensors, const struct sensing\_sensor\_info \*\*info)

Get all supported sensor instances' information.

[sensing\_get\_config](group__sensing__api.md#gaf4037066c9a7a9f3eb1c79a4d8ae0920)

int sensing\_get\_config(sensing\_sensor\_handle\_t handle, struct sensing\_sensor\_config \*configs, int count)

Get current config items from Sensing subsystem.

[SENSING\_SENSOR\_ATTRIBUTE\_MAX](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980)

@ SENSING\_SENSOR\_ATTRIBUTE\_MAX

**Definition** sensing.h:98

[SENSING\_SENSOR\_ATTRIBUTE\_LATENCY](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476)

@ SENSING\_SENSOR\_ATTRIBUTE\_LATENCY

**Definition** sensing.h:97

[SENSING\_SENSOR\_ATTRIBUTE\_INTERVAL](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3)

@ SENSING\_SENSOR\_ATTRIBUTE\_INTERVAL

**Definition** sensing.h:95

[SENSING\_SENSOR\_ATTRIBUTE\_SENSITIVITY](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b)

@ SENSING\_SENSOR\_ATTRIBUTE\_SENSITIVITY

**Definition** sensing.h:96

[SENSING\_SENSOR\_STATE\_READY](group__sensing__api.md#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93)

@ SENSING\_SENSOR\_STATE\_READY

**Definition** sensing.h:86

[SENSING\_SENSOR\_STATE\_OFFLINE](group__sensing__api.md#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e)

@ SENSING\_SENSOR\_STATE\_OFFLINE

**Definition** sensing.h:87

[sensing\_datatypes.h](sensing__datatypes_8h.md)

[sensing\_sensor\_types.h](sensing__sensor__types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[sensing\_callback\_list](structsensing__callback__list.md)

Sensing subsystem event callback list.

**Definition** sensing.h:151

[sensing\_callback\_list::context](structsensing__callback__list.md#a43504dbe7d484f0d0e7d33b8bb6318d4)

void \* context

**Definition** sensing.h:153

[sensing\_callback\_list::on\_data\_event](structsensing__callback__list.md#a7d0d7c878e338f19fd48c66cda9d04fc)

sensing\_data\_event\_t on\_data\_event

**Definition** sensing.h:152

[sensing\_sensor\_config](structsensing__sensor__config.md)

Sensing subsystem sensor configure, including interval, sensitivity, latency.

**Definition** sensing.h:160

[sensing\_sensor\_config::interval](structsensing__sensor__config.md#a7512f7254f6960ed398150db23868965)

uint32\_t interval

**Definition** sensing.h:167

[sensing\_sensor\_config::attri](structsensing__sensor__config.md#a9bdf50a1018d6d9426efd991d05bf72b)

enum sensing\_sensor\_attribute attri

**Definition** sensing.h:161

[sensing\_sensor\_config::data\_field](structsensing__sensor__config.md#ac4389c439db16cb25a2e622baf0aeb9b)

int8\_t data\_field

SENSING\_SENSITIVITY\_INDEX\_ALL

**Definition** sensing.h:164

[sensing\_sensor\_config::sensitivity](structsensing__sensor__config.md#acc1270dbe02ff6324e0f66acbde8ce33)

uint32\_t sensitivity

**Definition** sensing.h:168

[sensing\_sensor\_config::latency](structsensing__sensor__config.md#af9d2ee27b3a04fd65baa1d1d0cb2badc)

uint64\_t latency

**Definition** sensing.h:169

[sensing\_sensor\_info](structsensing__sensor__info.md)

Sensor basic constant information.

**Definition** sensing.h:126

[sensing\_sensor\_info::vendor](structsensing__sensor__info.md#a085e8c00586c61245b822c7ea9db9c98)

const char \* vendor

Vendor name of the sensor instance.

**Definition** sensing.h:134

[sensing\_sensor\_info::minimal\_interval](structsensing__sensor__info.md#a5b2ddf0829031098301e244f60741f2b)

const uint32\_t minimal\_interval

Minimal report interval in micro seconds.

**Definition** sensing.h:143

[sensing\_sensor\_info::type](structsensing__sensor__info.md#a6b20ad8747a95cf1dc7346374de6b855)

const int32\_t type

Sensor type.

**Definition** sensing.h:140

[sensing\_sensor\_info::friendly\_name](structsensing__sensor__info.md#aa3e056ad9c52c3388e049b08d0844b49)

const char \* friendly\_name

Friendly name of the sensor instance.

**Definition** sensing.h:131

[sensing\_sensor\_info::name](structsensing__sensor__info.md#ac7b4f33115f7a7a24095ca90b1e7acfe)

const char \* name

Name of the sensor instance.

**Definition** sensing.h:128

[sensing\_sensor\_info::model](structsensing__sensor__info.md#ace77ba2ab5d5eee7c4e385fc2ea74ee8)

const char \* model

Model name of the sensor instance.

**Definition** sensing.h:137

[sensing\_sensor\_version](structsensing__sensor__version.md)

Sensor Version.

**Definition** sensing.h:39

[sensing\_sensor\_version::value](structsensing__sensor__version.md#a0023cbb5114f4a3d3a1cf388e5034cfc)

uint32\_t value

**Definition** sensing.h:41

[sensing\_sensor\_version::hotfix](structsensing__sensor__version.md#a10fe885cd0cd9a6a5209308e188def3d)

uint8\_t hotfix

**Definition** sensing.h:45

[sensing\_sensor\_version::build](structsensing__sensor__version.md#a668f5d23171c38e1cc13a4221e639815)

uint8\_t build

**Definition** sensing.h:46

[sensing\_sensor\_version::minor](structsensing__sensor__version.md#a8d41ea3c181c7062aa8f76b17c652b41)

uint8\_t minor

**Definition** sensing.h:44

[sensing\_sensor\_version::major](structsensing__sensor__version.md#ad7275123dd08f06ee0307325c8f5fb37)

uint8\_t major

**Definition** sensing.h:43

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sensing](dir_89ae873b54fa3664e4a65bb9dc3973c9.md)
- [sensing.h](sensing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
