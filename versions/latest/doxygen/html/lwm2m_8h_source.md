---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lwm2m_8h_source.html
original_path: doxygen/html/lwm2m_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lwm2m.h

[Go to the documentation of this file.](lwm2m_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited

3 \* Copyright (c) 2017-2019 Foundries.io

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

23

24#ifndef ZEPHYR\_INCLUDE\_NET\_LWM2M\_H\_

25#define ZEPHYR\_INCLUDE\_NET\_LWM2M\_H\_

26

27#include <time.h>

28#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

29#include <[zephyr/sys/mutex.h](mutex_8h.md)>

30#include <[zephyr/net/coap.h](coap_8h.md)>

31#include <[zephyr/net/lwm2m\_path.h](lwm2m__path_8h.md)>

32

38

39/\* clang-format off \*/

[ 40](group__lwm2m__api.md#ga785e4a647a2cf93194a249537223ab0f)#define LWM2M\_OBJECT\_SECURITY\_ID 0

[ 41](group__lwm2m__api.md#gace7b2f0a1f97b6e99c0958a8382ca0d2)#define LWM2M\_OBJECT\_SERVER\_ID 1

[ 42](group__lwm2m__api.md#gaa8387c8838f952c7c60602e2952c7f55)#define LWM2M\_OBJECT\_ACCESS\_CONTROL\_ID 2

[ 43](group__lwm2m__api.md#ga699f585b320ab5b259d4fb2bda10eb78)#define LWM2M\_OBJECT\_DEVICE\_ID 3

[ 44](group__lwm2m__api.md#ga73db8616cc7dbbd04267d97a743b8ec0)#define LWM2M\_OBJECT\_CONNECTIVITY\_MONITORING\_ID 4

[ 45](group__lwm2m__api.md#ga442cc51c7d0807a752ce4affe9221c5b)#define LWM2M\_OBJECT\_FIRMWARE\_ID 5

[ 46](group__lwm2m__api.md#ga1046ec68deab3d812d7e5921fb718028)#define LWM2M\_OBJECT\_LOCATION\_ID 6

[ 47](group__lwm2m__api.md#gaa6c374c401dd36b6e121ac48c91ca9cf)#define LWM2M\_OBJECT\_CONNECTIVITY\_STATISTICS\_ID 7

[ 48](group__lwm2m__api.md#gac2d140b4a36d6010fe93bca443a658c0)#define LWM2M\_OBJECT\_SOFTWARE\_MANAGEMENT\_ID 9

[ 49](group__lwm2m__api.md#ga4b4ce912a4554923974461ea3c76007e)#define LWM2M\_OBJECT\_PORTFOLIO\_ID 16

[ 50](group__lwm2m__api.md#ga85eabde1900ef052064d34cf5e3a4afe)#define LWM2M\_OBJECT\_BINARYAPPDATACONTAINER\_ID 19

[ 51](group__lwm2m__api.md#ga4f0455fb0271c2fcbb7dadb944431ff0)#define LWM2M\_OBJECT\_EVENT\_LOG\_ID 20

[ 52](group__lwm2m__api.md#gab13a1600a662ed1dbd8845c6d7d4549a)#define LWM2M\_OBJECT\_OSCORE\_ID 21

[ 53](group__lwm2m__api.md#ga3505e9ddcd54afe86e8bd5fbc03fb565)#define LWM2M\_OBJECT\_GATEWAY\_ID 25

54/\* clang-format on \*/

55

57

65

66/\* clang-format off \*/

[ 67](group__lwm2m__api.md#gaeef485c23d306c93fc0f45dd58766ad9)#define IPSO\_OBJECT\_GENERIC\_SENSOR\_ID 3300

[ 68](group__lwm2m__api.md#ga3b0c046d93c7bcee9d4da121dd574ff0)#define IPSO\_OBJECT\_TEMP\_SENSOR\_ID 3303

[ 69](group__lwm2m__api.md#ga8075d8b7eb3b4c98f621efef673bb11f)#define IPSO\_OBJECT\_HUMIDITY\_SENSOR\_ID 3304

[ 70](group__lwm2m__api.md#ga56ebac5260ee467b3763abe49ff3b8ff)#define IPSO\_OBJECT\_LIGHT\_CONTROL\_ID 3311

[ 71](group__lwm2m__api.md#ga0b3b9db806e5fe47cc08de34b5fb35fe)#define IPSO\_OBJECT\_ACCELEROMETER\_ID 3313

[ 72](group__lwm2m__api.md#ga270a1b5a576d72099287633b32ce909f)#define IPSO\_OBJECT\_VOLTAGE\_SENSOR\_ID 3316

[ 73](group__lwm2m__api.md#gae511fd54112829e63c691776750893c2)#define IPSO\_OBJECT\_CURRENT\_SENSOR\_ID 3317

[ 74](group__lwm2m__api.md#ga752f81e91d0965a50ecfb0679bdea6ba)#define IPSO\_OBJECT\_PRESSURE\_ID 3323

[ 75](group__lwm2m__api.md#ga15d664ddbfbf4d5b25dde34a5c650e6b)#define IPSO\_OBJECT\_BUZZER\_ID 3338

[ 76](group__lwm2m__api.md#ga6c7bd5880fa22050748c2cb01981cbcb)#define IPSO\_OBJECT\_TIMER\_ID 3340

[ 77](group__lwm2m__api.md#ga776a6a5e1eab3a8de0a39382f94b663a)#define IPSO\_OBJECT\_ONOFF\_SWITCH\_ID 3342

[ 78](group__lwm2m__api.md#ga6e3119bc8f0b9143ab384e82a5bccf7c)#define IPSO\_OBJECT\_PUSH\_BUTTON\_ID 3347

[ 79](group__lwm2m__api.md#gacdd09a26ce52f36c644a89a8b89f7d32)#define UCIFI\_OBJECT\_BATTERY\_ID 3411

[ 80](group__lwm2m__api.md#ga21f6bc6255f5f5ed28881fa797d026ca)#define IPSO\_OBJECT\_FILLING\_LEVEL\_SENSOR\_ID 3435

81/\* clang-format on \*/

82

84

[ 90](group__lwm2m__api.md#gae7bf50f9abf1b82b76ac3e9175e685ac)typedef void (\*[lwm2m\_socket\_fault\_cb\_t](group__lwm2m__api.md#gae7bf50f9abf1b82b76ac3e9175e685ac))(int error);

91

[ 93](structlwm2m__obj__path.md)struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) {

[ 94](structlwm2m__obj__path.md#ad1cf2b4f67b059e92853a05e2d070bb7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_id](structlwm2m__obj__path.md#ad1cf2b4f67b059e92853a05e2d070bb7);

[ 95](structlwm2m__obj__path.md#a7ae1a626b6f4b4c9cdc3e1a99d644ff2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_inst\_id](structlwm2m__obj__path.md#a7ae1a626b6f4b4c9cdc3e1a99d644ff2);

[ 96](structlwm2m__obj__path.md#ac52cc68142a270b4bab8edfc7cb8b106) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [res\_id](structlwm2m__obj__path.md#ac52cc68142a270b4bab8edfc7cb8b106);

[ 97](structlwm2m__obj__path.md#a924d75187c05b64989b6eed69b563c29) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [res\_inst\_id](structlwm2m__obj__path.md#a924d75187c05b64989b6eed69b563c29);

[ 98](structlwm2m__obj__path.md#aaeb8482037aa5d9b389236eb9f3e2984) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](structlwm2m__obj__path.md#aaeb8482037aa5d9b389236eb9f3e2984);

99};

100

[ 104](group__lwm2m__api.md#gac8d63952ec94ca6cfb1dbe12a6c53bfb)enum [lwm2m\_observe\_event](group__lwm2m__api.md#gac8d63952ec94ca6cfb1dbe12a6c53bfb) {

[ 105](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3) [LWM2M\_OBSERVE\_EVENT\_OBSERVER\_ADDED](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3),

[ 106](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c) [LWM2M\_OBSERVE\_EVENT\_OBSERVER\_REMOVED](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c),

[ 107](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885) [LWM2M\_OBSERVE\_EVENT\_NOTIFY\_ACK](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885),

[ 108](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e) [LWM2M\_OBSERVE\_EVENT\_NOTIFY\_TIMEOUT](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e),

109};

110

[ 121](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe)typedef void (\*[lwm2m\_observe\_cb\_t](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe))(enum [lwm2m\_observe\_event](group__lwm2m__api.md#gac8d63952ec94ca6cfb1dbe12a6c53bfb) event, struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path,

122 void \*user\_data);

123

124

125struct [lwm2m\_ctx](structlwm2m__ctx.md);

126enum [lwm2m\_rd\_client\_event](group__lwm2m__api.md#gaca90ab8960a4ff01d44735dbc0405862);

[ 133](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9)typedef void (\*[lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9))(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx,

134 enum [lwm2m\_rd\_client\_event](group__lwm2m__api.md#gaca90ab8960a4ff01d44735dbc0405862) event);

135

136

[ 146](group__lwm2m__api.md#ga7611c1aebb0309ee8340e06dd8ee234d)enum [lwm2m\_socket\_states](group__lwm2m__api.md#ga7611c1aebb0309ee8340e06dd8ee234d) {

[ 147](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab) [LWM2M\_SOCKET\_STATE\_ONGOING](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab),

[ 148](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711) [LWM2M\_SOCKET\_STATE\_ONE\_RESPONSE](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711),

[ 149](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100) [LWM2M\_SOCKET\_STATE\_LAST](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100),

[ 150](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915) [LWM2M\_SOCKET\_STATE\_NO\_DATA](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915),

151};

152

[ 157](structlwm2m__ctx.md)struct [lwm2m\_ctx](structlwm2m__ctx.md) {

[ 159](structlwm2m__ctx.md#a4ed594ecc5d442ffc2a604a879f5bfb7) struct [sockaddr](structsockaddr.md) [remote\_addr](structlwm2m__ctx.md#a4ed594ecc5d442ffc2a604a879f5bfb7);

160

164 struct [coap\_pending](structcoap__pending.md) pendings[CONFIG\_LWM2M\_ENGINE\_MAX\_PENDING + 1];

165 struct [coap\_reply](structcoap__reply.md) replies[CONFIG\_LWM2M\_ENGINE\_MAX\_REPLIES + 1];

166 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) pending\_sends;

167#if defined(CONFIG\_LWM2M\_QUEUE\_MODE\_ENABLED)

168 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) queued\_messages;

169#endif

170 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) observer;

172

[ 178](structlwm2m__ctx.md#a9b56ad9b3f2202d25b8c48f34a898dd3) void \*[processed\_req](structlwm2m__ctx.md#a9b56ad9b3f2202d25b8c48f34a898dd3);

179

180#if defined(CONFIG\_LWM2M\_DTLS\_SUPPORT) || defined(\_\_DOXYGEN\_\_)

[ 190](structlwm2m__ctx.md#a6c4c9025a17a3dc3451651cb1f83d575) int [tls\_tag](structlwm2m__ctx.md#a6c4c9025a17a3dc3451651cb1f83d575);

191

[ 196](structlwm2m__ctx.md#a342cb5a0aaf9e5bc53228d3b0cc0fd43) char \*[desthostname](structlwm2m__ctx.md#a342cb5a0aaf9e5bc53228d3b0cc0fd43);

[ 198](structlwm2m__ctx.md#aff084b28e547a81bd71215125c28f705) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [desthostnamelen](structlwm2m__ctx.md#aff084b28e547a81bd71215125c28f705);

[ 200](structlwm2m__ctx.md#a380db99dd1930f29044a09876122c083) bool [hostname\_verify](structlwm2m__ctx.md#a380db99dd1930f29044a09876122c083);

201

[ 206](structlwm2m__ctx.md#a5f17296cd4600b25515e0952dc61ea97) int (\*[load\_credentials](structlwm2m__ctx.md#a5f17296cd4600b25515e0952dc61ea97))(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx);

208#endif

[ 214](structlwm2m__ctx.md#a746c578cf1d2c5eb606d0b592f419317) int (\*[set\_socketoptions](structlwm2m__ctx.md#a746c578cf1d2c5eb606d0b592f419317))(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx);

215

[ 221](structlwm2m__ctx.md#aeb1e3ffc83853f74f2201f582917c2ce) bool [use\_dtls](structlwm2m__ctx.md#aeb1e3ffc83853f74f2201f582917c2ce);

222

[ 227](structlwm2m__ctx.md#aff523bc7473073c917ff1c888da7bece) bool [connection\_suspended](structlwm2m__ctx.md#aff523bc7473073c917ff1c888da7bece);

228

229#if defined(CONFIG\_LWM2M\_QUEUE\_MODE\_ENABLED) || defined(\_\_DOXYGEN\_\_)

[ 234](structlwm2m__ctx.md#ac6709d32a87ece72c7cdf283c4ff60c0) bool [buffer\_client\_messages](structlwm2m__ctx.md#ac6709d32a87ece72c7cdf283c4ff60c0);

235#endif

[ 237](structlwm2m__ctx.md#ab5fe85963a265f9c059a25138a637e02) int [sec\_obj\_inst](structlwm2m__ctx.md#ab5fe85963a265f9c059a25138a637e02);

238

[ 240](structlwm2m__ctx.md#a76d92a14bf1729d7b0fee174c51ed4bf) int [srv\_obj\_inst](structlwm2m__ctx.md#a76d92a14bf1729d7b0fee174c51ed4bf);

241

[ 245](structlwm2m__ctx.md#aafa787c2b7ea7599c51d9247ea9f1090) bool [bootstrap\_mode](structlwm2m__ctx.md#aafa787c2b7ea7599c51d9247ea9f1090);

246

[ 248](structlwm2m__ctx.md#afed1a599a72f131e4f196848c3e6fe85) int [sock\_fd](structlwm2m__ctx.md#afed1a599a72f131e4f196848c3e6fe85);

249

[ 253](structlwm2m__ctx.md#a1b90780926f3cda2d48dfa8f94b1efd8) [lwm2m\_socket\_fault\_cb\_t](group__lwm2m__api.md#gae7bf50f9abf1b82b76ac3e9175e685ac) [fault\_cb](structlwm2m__ctx.md#a1b90780926f3cda2d48dfa8f94b1efd8);

254

[ 258](structlwm2m__ctx.md#a412bd706adcd17ec8c00f1779012a845) [lwm2m\_observe\_cb\_t](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe) [observe\_cb](structlwm2m__ctx.md#a412bd706adcd17ec8c00f1779012a845);

259

[ 261](structlwm2m__ctx.md#ab01ec6be0effa24dde31363a476eccbb) [lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9) [event\_cb](structlwm2m__ctx.md#ab01ec6be0effa24dde31363a476eccbb);

262

[ 267](structlwm2m__ctx.md#a574b50b9ec4cdfb5fac53a9b6d8c31d5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [validate\_buf](structlwm2m__ctx.md#a574b50b9ec4cdfb5fac53a9b6d8c31d5)[CONFIG\_LWM2M\_ENGINE\_VALIDATION\_BUFFER\_SIZE];

268

[ 275](structlwm2m__ctx.md#ad3d66164415325e7009d1a4c1111f4b3) void (\*[set\_socket\_state](structlwm2m__ctx.md#ad3d66164415325e7009d1a4c1111f4b3))(int fd, enum [lwm2m\_socket\_states](group__lwm2m__api.md#ga7611c1aebb0309ee8340e06dd8ee234d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

276};

277

[ 281](structlwm2m__time__series__elem.md)struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) {

[ 283](structlwm2m__time__series__elem.md#acd00227c551b6ee1960b3881819ef90b) [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [t](structlwm2m__time__series__elem.md#acd00227c551b6ee1960b3881819ef90b);

284 union {

[ 285](structlwm2m__time__series__elem.md#abb0726f2ba23ab5f3229342d62f63e6b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [u8](structlwm2m__time__series__elem.md#abb0726f2ba23ab5f3229342d62f63e6b);

[ 286](structlwm2m__time__series__elem.md#ad0cd9f29ce0d7e99c1ae411bd89a29fa) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [u16](structlwm2m__time__series__elem.md#ad0cd9f29ce0d7e99c1ae411bd89a29fa);

[ 287](structlwm2m__time__series__elem.md#a58b1e7f9eb00d58421aec63bfbc732ed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [u32](structlwm2m__time__series__elem.md#a58b1e7f9eb00d58421aec63bfbc732ed);

[ 288](structlwm2m__time__series__elem.md#ae432e592ddceb17113f25bef77308f1b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [u64](structlwm2m__time__series__elem.md#ae432e592ddceb17113f25bef77308f1b);

[ 289](structlwm2m__time__series__elem.md#ab895cd3addf57b8e59c8a1282588ee2d) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [i8](structlwm2m__time__series__elem.md#ab895cd3addf57b8e59c8a1282588ee2d);

[ 290](structlwm2m__time__series__elem.md#a37489f6edbcb125691bd02f28346c788) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [i16](structlwm2m__time__series__elem.md#a37489f6edbcb125691bd02f28346c788);

[ 291](structlwm2m__time__series__elem.md#a61f4d65dd7e6e2e6b215fdc800bba6e4) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [i32](structlwm2m__time__series__elem.md#a61f4d65dd7e6e2e6b215fdc800bba6e4);

[ 292](structlwm2m__time__series__elem.md#a2cccc464d029dc0f3f748b2a48f5cb50) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [i64](structlwm2m__time__series__elem.md#a2cccc464d029dc0f3f748b2a48f5cb50);

[ 293](structlwm2m__time__series__elem.md#af25edfa95c28e43bb5abc60f3027ed9a) [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [time](structlwm2m__time__series__elem.md#af25edfa95c28e43bb5abc60f3027ed9a);

[ 294](structlwm2m__time__series__elem.md#a3f25d66fa0e7918326a522e76451d6ae) double [f](structlwm2m__time__series__elem.md#a3f25d66fa0e7918326a522e76451d6ae);

[ 295](structlwm2m__time__series__elem.md#ae6b37f532055bdd6b5b39c909a6873e7) bool [b](structlwm2m__time__series__elem.md#ae6b37f532055bdd6b5b39c909a6873e7);

296 };

297};

298

[ 318](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384)typedef void \*(\*lwm2m\_engine\_get\_data\_cb\_t)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id,

319 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_id,

320 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_inst\_id,

321 size\_t \*data\_len);

322

[ 349](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9)typedef int (\*[lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id,

350 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) res\_inst\_id,

351 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len,

352 bool last\_block, size\_t total\_size);

353

[ 370](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf)typedef int (\*[lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id);

371

[ 388](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe)typedef int (\*[lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe))([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id,

389 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*args, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) args\_len);

390

[ 396](group__lwm2m__api.md#gae154ca2e54ec7759dd43f2a7a275077e)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_DC\_POWER 0

[ 397](group__lwm2m__api.md#ga04ca8ac536eed7d411c1b1ea2b2a59ac)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_INT 1

[ 398](group__lwm2m__api.md#gaf12052f903a688712928d036b782f621)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_EXT 2

[ 399](group__lwm2m__api.md#ga10c4633c97881ca7d87c748aaeec68c9)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_FUEL\_CELL 3

[ 400](group__lwm2m__api.md#ga72352523996e61ea93caff0bb80c42ba)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_PWR\_OVER\_ETH 4

[ 401](group__lwm2m__api.md#ga4877877be75d3dd3c8f600b438b7ea8e)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_USB 5

[ 402](group__lwm2m__api.md#ga97b9d38ec402478f10642f1f83a4f88a)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_AC\_POWER 6

[ 403](group__lwm2m__api.md#gaa41ec1d2ca43e1385cfb11204aff729d)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_SOLAR 7

[ 404](group__lwm2m__api.md#gae7a580aac1804abbcf3feb57a5a30a02)#define LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_MAX 8

406

[ 414](group__lwm2m__api.md#gad54ec75eb2843d5eed199ddedca6ef4f)#define LWM2M\_DEVICE\_ERROR\_NONE 0

[ 415](group__lwm2m__api.md#ga53a9ee1ae09dd32a8dc2df6018798f9f)#define LWM2M\_DEVICE\_ERROR\_LOW\_POWER 1

[ 416](group__lwm2m__api.md#ga33152ea4ef497b02a12d1218d470a5a6)#define LWM2M\_DEVICE\_ERROR\_EXT\_POWER\_SUPPLY\_OFF 2

[ 417](group__lwm2m__api.md#ga3c1b7693167ff517c5cbd7bbdbfd1ea0)#define LWM2M\_DEVICE\_ERROR\_GPS\_FAILURE 3

[ 418](group__lwm2m__api.md#ga78048382d8bc85bbabbff58f0a9860f2)#define LWM2M\_DEVICE\_ERROR\_LOW\_SIGNAL\_STRENGTH 4

[ 419](group__lwm2m__api.md#ga94ce0177c066dd43ef660b85afc83485)#define LWM2M\_DEVICE\_ERROR\_OUT\_OF\_MEMORY 5

[ 420](group__lwm2m__api.md#gabcb39cd3757ea60859984f6ad0df9e31)#define LWM2M\_DEVICE\_ERROR\_SMS\_FAILURE 6

[ 421](group__lwm2m__api.md#ga2110d71a0c58087ff877e66b7500ba66)#define LWM2M\_DEVICE\_ERROR\_NETWORK\_FAILURE 7

[ 422](group__lwm2m__api.md#ga77e6352eace8116576c880bf7e416ba3)#define LWM2M\_DEVICE\_ERROR\_PERIPHERAL\_FAILURE 8

423

425

[ 433](group__lwm2m__api.md#ga4329c971f95f1c345381d1c864a9f334)#define LWM2M\_DEVICE\_BATTERY\_STATUS\_NORMAL 0

[ 436](group__lwm2m__api.md#gaf19da3a566782aeebebfb6ff110a9152)#define LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGING 1

[ 437](group__lwm2m__api.md#ga5f7e88b52d8e6029467a2ed10585e6d4)#define LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGE\_COMP 2

[ 440](group__lwm2m__api.md#gaa3f81df5e4d45838922eb20a15ee3153)#define LWM2M\_DEVICE\_BATTERY\_STATUS\_DAMAGED 3

[ 441](group__lwm2m__api.md#ga578f6446ec1b70d2a32917abf1f5aad7)#define LWM2M\_DEVICE\_BATTERY\_STATUS\_LOW 4

[ 442](group__lwm2m__api.md#gacc3dfc99fc2cd9ef7048b1a0a0fd55c8)#define LWM2M\_DEVICE\_BATTERY\_STATUS\_NOT\_INST 5

[ 443](group__lwm2m__api.md#ga174e118b07982b87c6c083236b79c3b7)#define LWM2M\_DEVICE\_BATTERY\_STATUS\_UNKNOWN 6

444

446

[ 454](group__lwm2m__api.md#gabf8726f0438477863423947a7bb77ce2)int [lwm2m\_device\_add\_err](group__lwm2m__api.md#gabf8726f0438477863423947a7bb77ce2)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) error\_code);

455

456

464

[ 468](group__lwm2m__api.md#gaafff27c7165f059a969fe60fee51f683)#define STATE\_IDLE 0

[ 472](group__lwm2m__api.md#gaeb34e88a0da4ac1274ae6b2cef010086)#define STATE\_DOWNLOADING 1

[ 476](group__lwm2m__api.md#ga009085120be71a28c1f6ebdaf7503365)#define STATE\_DOWNLOADED 2

[ 480](group__lwm2m__api.md#gaac1dab8d1ac28bf13faeee39d1df47c5)#define STATE\_UPDATING 3

481

483

491

[ 492](group__lwm2m__api.md#ga391b47507468bbc1005903a56f80b1ea)#define RESULT\_DEFAULT 0

[ 493](group__lwm2m__api.md#ga7cc1753a05a0821f6c70dd2bccfbab5c)#define RESULT\_SUCCESS 1

[ 494](group__lwm2m__api.md#ga829f7bc83b67dcf16ea4775addd87343)#define RESULT\_NO\_STORAGE 2

[ 495](group__lwm2m__api.md#gab5446111a8969aa2c66dae49f04c93cf)#define RESULT\_OUT\_OF\_MEM 3

[ 496](group__lwm2m__api.md#ga0655ba8c402d8b6c8bbd84fb36447bd4)#define RESULT\_CONNECTION\_LOST 4

[ 497](group__lwm2m__api.md#gadfd0ac7b6a3fededa2b4471dfe52d3d2)#define RESULT\_INTEGRITY\_FAILED 5

[ 498](group__lwm2m__api.md#gab06dbfdac0c95f8100908a1177f3a62a)#define RESULT\_UNSUP\_FW 6

[ 499](group__lwm2m__api.md#ga268204053d7e23737283523224699979)#define RESULT\_INVALID\_URI 7

[ 500](group__lwm2m__api.md#ga2dfdd95c2c03ccca25d855b6d6f96ed3)#define RESULT\_UPDATE\_FAILED 8

[ 501](group__lwm2m__api.md#gade3da37a44ee40292ec6344403db8d8d)#define RESULT\_UNSUP\_PROTO 9

502

504

505#if defined(CONFIG\_LWM2M\_FIRMWARE\_UPDATE\_OBJ\_SUPPORT) || defined(\_\_DOXYGEN\_\_)

[ 514](group__lwm2m__api.md#ga6878ea0ebb512b19a4fb0859756f51d0)void [lwm2m\_firmware\_set\_write\_cb](group__lwm2m__api.md#ga6878ea0ebb512b19a4fb0859756f51d0)([lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb);

515

[ 521](group__lwm2m__api.md#ga4bf0bbedf5573ac18a11ac4fced11284)[lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) [lwm2m\_firmware\_get\_write\_cb](group__lwm2m__api.md#ga4bf0bbedf5573ac18a11ac4fced11284)(void);

522

[ 532](group__lwm2m__api.md#gac4e4a819e54344657d70ec479eb6ec8d)void [lwm2m\_firmware\_set\_write\_cb\_inst](group__lwm2m__api.md#gac4e4a819e54344657d70ec479eb6ec8d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb);

533

[ 540](group__lwm2m__api.md#gad7334f06c3bdb14485597794a417152d)[lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) [lwm2m\_firmware\_get\_write\_cb\_inst](group__lwm2m__api.md#gad7334f06c3bdb14485597794a417152d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id);

541

[ 550](group__lwm2m__api.md#ga3955dca5cd6d67807ed75e61a4d84d84)void [lwm2m\_firmware\_set\_cancel\_cb](group__lwm2m__api.md#ga3955dca5cd6d67807ed75e61a4d84d84)([lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb);

551

[ 557](group__lwm2m__api.md#ga9561c1b8407d888f6fbe1e0ceab1c235)[lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) [lwm2m\_firmware\_get\_cancel\_cb](group__lwm2m__api.md#ga9561c1b8407d888f6fbe1e0ceab1c235)(void);

558

[ 568](group__lwm2m__api.md#gaa200b524e505f64247f1e7472c5f36d4)void [lwm2m\_firmware\_set\_cancel\_cb\_inst](group__lwm2m__api.md#gaa200b524e505f64247f1e7472c5f36d4)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb);

569

[ 576](group__lwm2m__api.md#ga6f4b3e08c7e03cff4bf31e2f2999971e)[lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) [lwm2m\_firmware\_get\_cancel\_cb\_inst](group__lwm2m__api.md#ga6f4b3e08c7e03cff4bf31e2f2999971e)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id);

577

[ 586](group__lwm2m__api.md#ga61eb38e42d9e1b3f467c43a324f2fc65)void [lwm2m\_firmware\_set\_update\_cb](group__lwm2m__api.md#ga61eb38e42d9e1b3f467c43a324f2fc65)([lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb);

587

[ 593](group__lwm2m__api.md#ga1e4b8ba1b19ac9025dca3c4799bba84a)[lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) [lwm2m\_firmware\_get\_update\_cb](group__lwm2m__api.md#ga1e4b8ba1b19ac9025dca3c4799bba84a)(void);

594

[ 604](group__lwm2m__api.md#ga31d0f3e40b5e3d608d16a4268b2f1b29)void [lwm2m\_firmware\_set\_update\_cb\_inst](group__lwm2m__api.md#ga31d0f3e40b5e3d608d16a4268b2f1b29)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb);

605

[ 612](group__lwm2m__api.md#ga34995e902b63c4d7d37ebd709d88a72a)[lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) [lwm2m\_firmware\_get\_update\_cb\_inst](group__lwm2m__api.md#ga34995e902b63c4d7d37ebd709d88a72a)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id);

613#endif

614

615#if defined(CONFIG\_LWM2M\_SWMGMT\_OBJ\_SUPPORT) || defined(\_\_DOXYGEN\_\_)

616

[ 628](group__lwm2m__api.md#gac374d0559056ddb9cf43deae932fd128)int [lwm2m\_swmgmt\_set\_activate\_cb](group__lwm2m__api.md#gac374d0559056ddb9cf43deae932fd128)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb);

629

[ 641](group__lwm2m__api.md#ga7a2b93b918257bece819dc44804f27f5)int [lwm2m\_swmgmt\_set\_deactivate\_cb](group__lwm2m__api.md#ga7a2b93b918257bece819dc44804f27f5)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb);

642

[ 654](group__lwm2m__api.md#gadfc00060c0b538ed576b5e3edd7dac80)int [lwm2m\_swmgmt\_set\_install\_package\_cb](group__lwm2m__api.md#gadfc00060c0b538ed576b5e3edd7dac80)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb);

655

[ 667](group__lwm2m__api.md#gacf209563efdc5f3201152088c52d05c3)int [lwm2m\_swmgmt\_set\_delete\_package\_cb](group__lwm2m__api.md#gacf209563efdc5f3201152088c52d05c3)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb);

668

[ 680](group__lwm2m__api.md#gab59370ce4fdc94adb4903f22ab1f95b2)int [lwm2m\_swmgmt\_set\_read\_package\_version\_cb](group__lwm2m__api.md#gab59370ce4fdc94adb4903f22ab1f95b2)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb);

681

[ 693](group__lwm2m__api.md#ga293904118f972ae387c8aa85a1028b54)int [lwm2m\_swmgmt\_set\_write\_package\_cb](group__lwm2m__api.md#ga293904118f972ae387c8aa85a1028b54)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb);

694

[ 705](group__lwm2m__api.md#ga573e128348fb2f43a33bd09332dd677f)int [lwm2m\_swmgmt\_install\_completed](group__lwm2m__api.md#ga573e128348fb2f43a33bd09332dd677f)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_inst\_id, int error\_code);

706

707#endif

708

709#if defined(CONFIG\_LWM2M\_EVENT\_LOG\_OBJ\_SUPPORT) || defined(\_\_DOXYGEN\_\_)

710

[ 719](group__lwm2m__api.md#ga950557bce8c510bcc8b0704e7bc4a9dc)void [lwm2m\_event\_log\_set\_read\_log\_data\_cb](group__lwm2m__api.md#ga950557bce8c510bcc8b0704e7bc4a9dc)([lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb);

720

721#endif

722

[ 726](group__lwm2m__api.md#ga34febb0c6fb1c68b0963a6e4dd721763)#define LWM2M\_OBJLNK\_MAX\_ID USHRT\_MAX

727

[ 731](structlwm2m__objlnk.md)struct [lwm2m\_objlnk](structlwm2m__objlnk.md) {

[ 732](structlwm2m__objlnk.md#a67193c8612b3a3d2a6a9685f7d1a0053) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_id](structlwm2m__objlnk.md#a67193c8612b3a3d2a6a9685f7d1a0053);

[ 733](structlwm2m__objlnk.md#aa51649798b00bc0bb9887c9739b83d27) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [obj\_inst](structlwm2m__objlnk.md#aa51649798b00bc0bb9887c9739b83d27);

734};

735

752\_\_deprecated

[ 753](group__lwm2m__api.md#ga489c8ea2eb89c7c6dc008002ab2ea836)int [lwm2m\_engine\_update\_observer\_min\_period](group__lwm2m__api.md#ga489c8ea2eb89c7c6dc008002ab2ea836)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const char \*pathstr,

754 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s);

755

[ 770](group__lwm2m__api.md#gadd163806d70713d8349a9db484ba88bf)int [lwm2m\_update\_observer\_min\_period](group__lwm2m__api.md#gadd163806d70713d8349a9db484ba88bf)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx,

771 const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s);

772

789\_\_deprecated

[ 790](group__lwm2m__api.md#gacb717ef5a36524e6f0f78b90cc803577)int [lwm2m\_engine\_update\_observer\_max\_period](group__lwm2m__api.md#gacb717ef5a36524e6f0f78b90cc803577)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const char \*pathstr,

791 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s);

792

[ 807](group__lwm2m__api.md#ga6acccbcd879901574aceab53a21800fc)int [lwm2m\_update\_observer\_max\_period](group__lwm2m__api.md#ga6acccbcd879901574aceab53a21800fc)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx,

808 const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_s);

809

823\_\_deprecated

[ 824](group__lwm2m__api.md#ga32f393a9e302f1f60839fd2147ebd7e9)int [lwm2m\_engine\_create\_obj\_inst](group__lwm2m__api.md#ga32f393a9e302f1f60839fd2147ebd7e9)(const char \*pathstr);

825

[ 837](group__lwm2m__api.md#ga53f5b4c5967e93c7dd224fce8f416265)int [lwm2m\_create\_object\_inst](group__lwm2m__api.md#ga53f5b4c5967e93c7dd224fce8f416265)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path);

838

850\_\_deprecated

[ 851](group__lwm2m__api.md#ga3849e960b54bcb089ac00476da8fb430)int [lwm2m\_engine\_delete\_obj\_inst](group__lwm2m__api.md#ga3849e960b54bcb089ac00476da8fb430)(const char \*pathstr);

852

[ 862](group__lwm2m__api.md#gaf921d4bc96090ef8735d90d173feab94)int [lwm2m\_delete\_object\_inst](group__lwm2m__api.md#gaf921d4bc96090ef8735d90d173feab94)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path);

863

[ 871](group__lwm2m__api.md#ga9a0cdcc9fc6d37462eddeb54e5d1f87a)void [lwm2m\_registry\_lock](group__lwm2m__api.md#ga9a0cdcc9fc6d37462eddeb54e5d1f87a)(void);

872

[ 877](group__lwm2m__api.md#gab09b62982c34887cdd16c30659d3349a)void [lwm2m\_registry\_unlock](group__lwm2m__api.md#gab09b62982c34887cdd16c30659d3349a)(void);

878

890\_\_deprecated

[ 891](group__lwm2m__api.md#ga2a891e26440f732b77ab90b979c8cb49)int [lwm2m\_engine\_set\_opaque](group__lwm2m__api.md#ga2a891e26440f732b77ab90b979c8cb49)(const char \*pathstr, const char \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len);

892

[ 902](group__lwm2m__api.md#gaaef33bdf3f48fd91abdb50db4d5460f9)int [lwm2m\_set\_opaque](group__lwm2m__api.md#gaaef33bdf3f48fd91abdb50db4d5460f9)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const char \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len);

903

914\_\_deprecated

[ 915](group__lwm2m__api.md#ga28911733660e7ce2f2f73c8eeb87de59)int [lwm2m\_engine\_set\_string](group__lwm2m__api.md#ga28911733660e7ce2f2f73c8eeb87de59)(const char \*pathstr, const char \*data\_ptr);

916

[ 925](group__lwm2m__api.md#ga7217f33bf705011d91ba66c86a4d5747)int [lwm2m\_set\_string](group__lwm2m__api.md#ga7217f33bf705011d91ba66c86a4d5747)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const char \*data\_ptr);

926

937\_\_deprecated

[ 938](group__lwm2m__api.md#ga00a61b227bae53a70b0092bb94801ea8)int [lwm2m\_engine\_set\_u8](group__lwm2m__api.md#ga00a61b227bae53a70b0092bb94801ea8)(const char \*pathstr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

939

[ 948](group__lwm2m__api.md#ga1aa3ff424b7190d0fbd9366626b2685c)int [lwm2m\_set\_u8](group__lwm2m__api.md#ga1aa3ff424b7190d0fbd9366626b2685c)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value);

949

960\_\_deprecated

[ 961](group__lwm2m__api.md#ga4fcea78d9506822ee76df465cf71ffdf)int [lwm2m\_engine\_set\_u16](group__lwm2m__api.md#ga4fcea78d9506822ee76df465cf71ffdf)(const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

962

[ 971](group__lwm2m__api.md#ga1f06bb65571efee18db5d061f95399c3)int [lwm2m\_set\_u16](group__lwm2m__api.md#ga1f06bb65571efee18db5d061f95399c3)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

972

983\_\_deprecated

[ 984](group__lwm2m__api.md#ga326c722de4ecdcbc09adb52c83cf6400)int [lwm2m\_engine\_set\_u32](group__lwm2m__api.md#ga326c722de4ecdcbc09adb52c83cf6400)(const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

985

[ 994](group__lwm2m__api.md#ga9481e570b121404dc1be1ce23d904894)int [lwm2m\_set\_u32](group__lwm2m__api.md#ga9481e570b121404dc1be1ce23d904894)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

995

1006\_\_deprecated

[ 1007](group__lwm2m__api.md#ga7d04c579284369233156a0597f09ab83)int [lwm2m\_engine\_set\_u64](group__lwm2m__api.md#ga7d04c579284369233156a0597f09ab83)(const char \*pathstr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

1008

1021\_\_deprecated

[ 1022](group__lwm2m__api.md#ga8a751dc8384cc47f9c14d916e20ae19d)int [lwm2m\_set\_u64](group__lwm2m__api.md#ga8a751dc8384cc47f9c14d916e20ae19d)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

1023

1034\_\_deprecated

[ 1035](group__lwm2m__api.md#gae665c8bb81c0aef3b960b087ff0f97f8)int [lwm2m\_engine\_set\_s8](group__lwm2m__api.md#gae665c8bb81c0aef3b960b087ff0f97f8)(const char \*pathstr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) value);

1036

[ 1045](group__lwm2m__api.md#ga37261a4b9e54eab3d1d855a084d082aa)int [lwm2m\_set\_s8](group__lwm2m__api.md#ga37261a4b9e54eab3d1d855a084d082aa)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) value);

1046

1057\_\_deprecated

[ 1058](group__lwm2m__api.md#ga1dd4952af0029c94a71f74734ae3a16c)int [lwm2m\_engine\_set\_s16](group__lwm2m__api.md#ga1dd4952af0029c94a71f74734ae3a16c)(const char \*pathstr, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) value);

1059

[ 1068](group__lwm2m__api.md#gad548ffedcb8328b23eb32476a97be6ee)int [lwm2m\_set\_s16](group__lwm2m__api.md#gad548ffedcb8328b23eb32476a97be6ee)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) value);

1069

1080\_\_deprecated

[ 1081](group__lwm2m__api.md#ga4f45dc38b5e6a55633474ff5d5447ecb)int [lwm2m\_engine\_set\_s32](group__lwm2m__api.md#ga4f45dc38b5e6a55633474ff5d5447ecb)(const char \*pathstr, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

1082

[ 1091](group__lwm2m__api.md#ga327e086959fc5649a5ef14f1f2943e88)int [lwm2m\_set\_s32](group__lwm2m__api.md#ga327e086959fc5649a5ef14f1f2943e88)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value);

1092

1103\_\_deprecated

[ 1104](group__lwm2m__api.md#ga11619cc0907010018217b8d67e9e9f7e)int [lwm2m\_engine\_set\_s64](group__lwm2m__api.md#ga11619cc0907010018217b8d67e9e9f7e)(const char \*pathstr, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value);

1105

[ 1114](group__lwm2m__api.md#ga18fcee379640c0dda32d6e3d14827260)int [lwm2m\_set\_s64](group__lwm2m__api.md#ga18fcee379640c0dda32d6e3d14827260)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) value);

1115

1126\_\_deprecated

[ 1127](group__lwm2m__api.md#ga8c82346313a9bf1234f72d71a5db34f5)int [lwm2m\_engine\_set\_bool](group__lwm2m__api.md#ga8c82346313a9bf1234f72d71a5db34f5)(const char \*pathstr, bool value);

1128

[ 1137](group__lwm2m__api.md#ga9ef21d06bef8a97b7666c0aa7fa753b4)int [lwm2m\_set\_bool](group__lwm2m__api.md#ga9ef21d06bef8a97b7666c0aa7fa753b4)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, bool value);

1138

1149\_\_deprecated

[ 1150](group__lwm2m__api.md#gae85eb5da495b7d42b10cf01c0d826632)int [lwm2m\_engine\_set\_float](group__lwm2m__api.md#gae85eb5da495b7d42b10cf01c0d826632)(const char \*pathstr, const double \*value);

1151

[ 1160](group__lwm2m__api.md#ga3386d3f2ad8d9713fc2283ed6921c2fc)int [lwm2m\_set\_f64](group__lwm2m__api.md#ga3386d3f2ad8d9713fc2283ed6921c2fc)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const double value);

1161

1172\_\_deprecated

[ 1173](group__lwm2m__api.md#gada5007c34ce2ee72017065b32f1cee58)int [lwm2m\_engine\_set\_objlnk](group__lwm2m__api.md#gada5007c34ce2ee72017065b32f1cee58)(const char \*pathstr, const struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*value);

1174

[ 1183](group__lwm2m__api.md#ga04a18bd8a4eeea41a47803c16567d67b)int [lwm2m\_set\_objlnk](group__lwm2m__api.md#ga04a18bd8a4eeea41a47803c16567d67b)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, const struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*value);

1184

1195\_\_deprecated

[ 1196](group__lwm2m__api.md#gad3621c4a9ddfdc2a9e8fe2df058aefd7)int [lwm2m\_engine\_set\_time](group__lwm2m__api.md#gad3621c4a9ddfdc2a9e8fe2df058aefd7)(const char \*pathstr, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) value);

1197

[ 1206](group__lwm2m__api.md#ga7194ad24842e35130d8af7f5104c0844)int [lwm2m\_set\_time](group__lwm2m__api.md#ga7194ad24842e35130d8af7f5104c0844)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) value);

1207

1219\_\_deprecated

[ 1220](group__lwm2m__api.md#ga3439a579648c15bfe8883337c4618095)int [lwm2m\_engine\_get\_opaque](group__lwm2m__api.md#ga3439a579648c15bfe8883337c4618095)(const char \*pathstr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen);

1221

[ 1231](group__lwm2m__api.md#gae245a9a1d9456af7e6283b1074944606)int [lwm2m\_get\_opaque](group__lwm2m__api.md#gae245a9a1d9456af7e6283b1074944606)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen);

1232

1244\_\_deprecated

[ 1245](group__lwm2m__api.md#ga72e27dfaf0881561245d01d6f800f0dc)int [lwm2m\_engine\_get\_string](group__lwm2m__api.md#ga72e27dfaf0881561245d01d6f800f0dc)(const char \*pathstr, void \*str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen);

1246

[ 1256](group__lwm2m__api.md#ga20fc58b25468bf309175db59d67b820b)int [lwm2m\_get\_string](group__lwm2m__api.md#ga20fc58b25468bf309175db59d67b820b)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buflen);

1257

1268\_\_deprecated

[ 1269](group__lwm2m__api.md#ga50ee578c777c7b8a1b0fbe028c8342ec)int [lwm2m\_engine\_get\_u8](group__lwm2m__api.md#ga50ee578c777c7b8a1b0fbe028c8342ec)(const char \*pathstr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

1270

[ 1279](group__lwm2m__api.md#gac56e804962e529799c771d81ac1fd027)int [lwm2m\_get\_u8](group__lwm2m__api.md#gac56e804962e529799c771d81ac1fd027)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value);

1280

1291\_\_deprecated

[ 1292](group__lwm2m__api.md#ga68986109d78b60f83f9cd85742ed80fb)int [lwm2m\_engine\_get\_u16](group__lwm2m__api.md#ga68986109d78b60f83f9cd85742ed80fb)(const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value);

1293

[ 1302](group__lwm2m__api.md#ga1b96848f96bdab9939bb2619d3e1059b)int [lwm2m\_get\_u16](group__lwm2m__api.md#ga1b96848f96bdab9939bb2619d3e1059b)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value);

1303

1314\_\_deprecated

[ 1315](group__lwm2m__api.md#gafddb717b3f43619e03a240660f65eb03)int [lwm2m\_engine\_get\_u32](group__lwm2m__api.md#gafddb717b3f43619e03a240660f65eb03)(const char \*pathstr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value);

1316

[ 1325](group__lwm2m__api.md#ga0bc84cb39a7a537925ec7d62e54b8b48)int [lwm2m\_get\_u32](group__lwm2m__api.md#ga0bc84cb39a7a537925ec7d62e54b8b48)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*value);

1326

1337\_\_deprecated

[ 1338](group__lwm2m__api.md#ga8d9068217afe09b0930996e5796b8aac)int [lwm2m\_engine\_get\_u64](group__lwm2m__api.md#ga8d9068217afe09b0930996e5796b8aac)(const char \*pathstr, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

1339

1352\_\_deprecated

[ 1353](group__lwm2m__api.md#ga831d229d9a4b983223dff626bbde7a66)int [lwm2m\_get\_u64](group__lwm2m__api.md#ga831d229d9a4b983223dff626bbde7a66)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

1354

1365\_\_deprecated

[ 1366](group__lwm2m__api.md#ga701d36c7b7a63c8214bfa30c0c19c946)int [lwm2m\_engine\_get\_s8](group__lwm2m__api.md#ga701d36c7b7a63c8214bfa30c0c19c946)(const char \*pathstr, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*value);

1367

[ 1376](group__lwm2m__api.md#ga12817bfbf0a0cbb742568ee974a1c337)int [lwm2m\_get\_s8](group__lwm2m__api.md#ga12817bfbf0a0cbb742568ee974a1c337)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \*value);

1377

1388\_\_deprecated

[ 1389](group__lwm2m__api.md#ga96f29e6d897b96fedc7f3e19bd906f7c)int [lwm2m\_engine\_get\_s16](group__lwm2m__api.md#ga96f29e6d897b96fedc7f3e19bd906f7c)(const char \*pathstr, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value);

1390

[ 1399](group__lwm2m__api.md#ga2426db6720b3f3e15e63022cabae5ece)int [lwm2m\_get\_s16](group__lwm2m__api.md#ga2426db6720b3f3e15e63022cabae5ece)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value);

1400

1411\_\_deprecated

[ 1412](group__lwm2m__api.md#ga40895289c1c8b778b6bf30d444dda63a)int [lwm2m\_engine\_get\_s32](group__lwm2m__api.md#ga40895289c1c8b778b6bf30d444dda63a)(const char \*pathstr, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

1413

[ 1422](group__lwm2m__api.md#ga99d7189efa25881dbcddd99e2a795f1b)int [lwm2m\_get\_s32](group__lwm2m__api.md#ga99d7189efa25881dbcddd99e2a795f1b)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*value);

1423

1434\_\_deprecated

[ 1435](group__lwm2m__api.md#ga7ad1a482074d033ad1def72882efd245)int [lwm2m\_engine\_get\_s64](group__lwm2m__api.md#ga7ad1a482074d033ad1def72882efd245)(const char \*pathstr, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*value);

1436

[ 1445](group__lwm2m__api.md#gaaffe06ca9ee5302fb6e26164f250653e)int [lwm2m\_get\_s64](group__lwm2m__api.md#gaaffe06ca9ee5302fb6e26164f250653e)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*value);

1446

1457\_\_deprecated

[ 1458](group__lwm2m__api.md#ga606e281a1146f930d7c0675d5881c7d6)int [lwm2m\_engine\_get\_bool](group__lwm2m__api.md#ga606e281a1146f930d7c0675d5881c7d6)(const char \*pathstr, bool \*value);

1459

[ 1468](group__lwm2m__api.md#gafdc72844ce0ca417e297d76288155aa4)int [lwm2m\_get\_bool](group__lwm2m__api.md#gafdc72844ce0ca417e297d76288155aa4)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, bool \*value);

1469

1480\_\_deprecated

[ 1481](group__lwm2m__api.md#ga0a272643082347fe6044bddbd7e5cebf)int [lwm2m\_engine\_get\_float](group__lwm2m__api.md#ga0a272643082347fe6044bddbd7e5cebf)(const char \*pathstr, double \*buf);

1482

[ 1491](group__lwm2m__api.md#ga03b72e96a67fcbf85feb5bf0b9df81ce)int [lwm2m\_get\_f64](group__lwm2m__api.md#ga03b72e96a67fcbf85feb5bf0b9df81ce)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, double \*value);

1492

1503\_\_deprecated

[ 1504](group__lwm2m__api.md#gaf4b23e412fcff5f2838f3e232a3cd224)int [lwm2m\_engine\_get\_objlnk](group__lwm2m__api.md#gaf4b23e412fcff5f2838f3e232a3cd224)(const char \*pathstr, struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*buf);

1505

[ 1514](group__lwm2m__api.md#ga4de941c36cf678e12da6e05c378a92e5)int [lwm2m\_get\_objlnk](group__lwm2m__api.md#ga4de941c36cf678e12da6e05c378a92e5)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, struct [lwm2m\_objlnk](structlwm2m__objlnk.md) \*buf);

1515

1526\_\_deprecated

[ 1527](group__lwm2m__api.md#ga273fa47b65309b46aa1b73b224d0dfce)int [lwm2m\_engine\_get\_time](group__lwm2m__api.md#ga273fa47b65309b46aa1b73b224d0dfce)(const char \*pathstr, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*buf);

1528

[ 1537](group__lwm2m__api.md#ga2e1d41866b5ea35c5aa29bca9bb43812)int [lwm2m\_get\_time](group__lwm2m__api.md#ga2e1d41866b5ea35c5aa29bca9bb43812)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) \*buf);

1538

1559\_\_deprecated

[ 1560](group__lwm2m__api.md#ga21d15060cce1c039a11106d71d681f4c)int [lwm2m\_engine\_register\_read\_callback](group__lwm2m__api.md#ga21d15060cce1c039a11106d71d681f4c)(const char \*pathstr,

1561 [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb);

1562

[ 1581](group__lwm2m__api.md#gaf33bd6a527b6d399f3d92b666ac77dfb)int [lwm2m\_register\_read\_callback](group__lwm2m__api.md#gaf33bd6a527b6d399f3d92b666ac77dfb)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb);

1582

1597\_\_deprecated

[ 1598](group__lwm2m__api.md#ga1354bc59163db5b3435e8e86c8feafd8)int [lwm2m\_engine\_register\_pre\_write\_callback](group__lwm2m__api.md#ga1354bc59163db5b3435e8e86c8feafd8)(const char \*pathstr,

1599 [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb);

1600

[ 1613](group__lwm2m__api.md#ga6f775837e07ba9b0032be8917a593e16)int [lwm2m\_register\_pre\_write\_callback](group__lwm2m__api.md#ga6f775837e07ba9b0032be8917a593e16)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path,

1614 [lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384) cb);

1615

1638\_\_deprecated

[ 1639](group__lwm2m__api.md#gac1c92e1ee3a804b325aacfe116bad096)int [lwm2m\_engine\_register\_validate\_callback](group__lwm2m__api.md#gac1c92e1ee3a804b325aacfe116bad096)(const char \*pathstr,

1640 [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb);

1641

[ 1662](group__lwm2m__api.md#gad6e5fd4815f409ad59ad631b03199333)int [lwm2m\_register\_validate\_callback](group__lwm2m__api.md#gad6e5fd4815f409ad59ad631b03199333)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path,

1663 [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb);

1664

1681\_\_deprecated

[ 1682](group__lwm2m__api.md#ga5c43bcdb0575f8c56354d6b4e30641a3)int [lwm2m\_engine\_register\_post\_write\_callback](group__lwm2m__api.md#ga5c43bcdb0575f8c56354d6b4e30641a3)(const char \*pathstr,

1683 [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb);

1684

[ 1699](group__lwm2m__api.md#ga3dd8b38e797173dae902404fb5b7a3f4)int [lwm2m\_register\_post\_write\_callback](group__lwm2m__api.md#ga3dd8b38e797173dae902404fb5b7a3f4)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path,

1700 [lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9) cb);

1701

1714\_\_deprecated

[ 1715](group__lwm2m__api.md#gad213063b7e68bd7b4f3ce3de3736a237)int [lwm2m\_engine\_register\_exec\_callback](group__lwm2m__api.md#gad213063b7e68bd7b4f3ce3de3736a237)(const char \*pathstr,

1716 [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb);

1717

[ 1728](group__lwm2m__api.md#ga29cc5cdd697e94d7379b1fb178487916)int [lwm2m\_register\_exec\_callback](group__lwm2m__api.md#ga29cc5cdd697e94d7379b1fb178487916)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe) cb);

1729

1742\_\_deprecated

[ 1743](group__lwm2m__api.md#gaa198bfb55f98183cbd33169468ae0bcc)int [lwm2m\_engine\_register\_create\_callback](group__lwm2m__api.md#gaa198bfb55f98183cbd33169468ae0bcc)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id,

1744 [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb);

1745

[ 1756](group__lwm2m__api.md#ga346d547e02bd53ee83f83b2248449e98)int [lwm2m\_register\_create\_callback](group__lwm2m__api.md#ga346d547e02bd53ee83f83b2248449e98)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id,

1757 [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb);

1758

1771\_\_deprecated

[ 1772](group__lwm2m__api.md#ga6a5dfdd29055bed245bf16ecc5829f95)int [lwm2m\_engine\_register\_delete\_callback](group__lwm2m__api.md#ga6a5dfdd29055bed245bf16ecc5829f95)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id,

1773 [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb);

1774

[ 1785](group__lwm2m__api.md#ga92d7e6d81ef674a6c311e1717c6bf373)int [lwm2m\_register\_delete\_callback](group__lwm2m__api.md#ga92d7e6d81ef674a6c311e1717c6bf373)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) obj\_id,

1786 [lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf) cb);

1787

[ 1791](group__lwm2m__api.md#ga12c2e0af3d3fc6dd5785e08c0d831a67)#define LWM2M\_RES\_DATA\_READ\_ONLY 0

1792

[ 1796](group__lwm2m__api.md#ga1bfa5b7d83e3560828a1fb61a4d07355)#define LWM2M\_RES\_DATA\_FLAG\_RO BIT(LWM2M\_RES\_DATA\_READ\_ONLY)

1797

[ 1801](group__lwm2m__api.md#ga49f4117dfec8cd1abe9f827e235f55b0)#define LWM2M\_HAS\_RES\_FLAG(res, f) ((res->data\_flags & f) == f)

1802

1819\_\_deprecated

[ 1820](group__lwm2m__api.md#ga66bdc3f3a4d0e88b036c9704abfbcafc)int [lwm2m\_engine\_set\_res\_buf](group__lwm2m__api.md#ga66bdc3f3a4d0e88b036c9704abfbcafc)(const char \*pathstr, void \*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buffer\_len,

1821 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags);

1822

[ 1837](group__lwm2m__api.md#ga56a2aecd38baedb5dc17258610c4780d)int [lwm2m\_set\_res\_buf](group__lwm2m__api.md#ga56a2aecd38baedb5dc17258610c4780d)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buffer\_len,

1838 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags);

1839

1856\_\_deprecated

[ 1857](group__lwm2m__api.md#gabf56a29aec75675099df2d45ca802718)int [lwm2m\_engine\_set\_res\_data](group__lwm2m__api.md#gabf56a29aec75675099df2d45ca802718)(const char \*pathstr, void \*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len,

1858 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data\_flags);

1859

1872\_\_deprecated

[ 1873](group__lwm2m__api.md#ga87833da93894dc5df45b91dfaebf3f91)int [lwm2m\_engine\_set\_res\_data\_len](group__lwm2m__api.md#ga87833da93894dc5df45b91dfaebf3f91)(const char \*pathstr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len);

1874

[ 1885](group__lwm2m__api.md#ga0f2b115d231bea6622135d72b51f55ca)int [lwm2m\_set\_res\_data\_len](group__lwm2m__api.md#ga0f2b115d231bea6622135d72b51f55ca)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len);

1886

1908\_\_deprecated

[ 1909](group__lwm2m__api.md#gaff5e10bc0fa34c1fe72a0b4e1ed2bc39)int [lwm2m\_engine\_get\_res\_buf](group__lwm2m__api.md#gaff5e10bc0fa34c1fe72a0b4e1ed2bc39)(const char \*pathstr, void \*\*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buffer\_len,

1910 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags);

1911

[ 1931](group__lwm2m__api.md#gac0b6669d8a19b03eb8b08cbbcdb0c192)int [lwm2m\_get\_res\_buf](group__lwm2m__api.md#gac0b6669d8a19b03eb8b08cbbcdb0c192)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, void \*\*buffer\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buffer\_len,

1932 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags);

1933

1949\_\_deprecated

[ 1950](group__lwm2m__api.md#ga630079a8d2f2acae1c313297cfdbada9)int [lwm2m\_engine\_get\_res\_data](group__lwm2m__api.md#ga630079a8d2f2acae1c313297cfdbada9)(const char \*pathstr, void \*\*data\_ptr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data\_len,

1951 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_flags);

1952

1966\_\_deprecated

[ 1967](group__lwm2m__api.md#ga64b0427f36b6d2d2f8af8cc2e35cdb89)int [lwm2m\_engine\_create\_res\_inst](group__lwm2m__api.md#ga64b0427f36b6d2d2f8af8cc2e35cdb89)(const char \*pathstr);

1968

[ 1980](group__lwm2m__api.md#gac69c40474180fe14c3761185b2db1c0c)int [lwm2m\_create\_res\_inst](group__lwm2m__api.md#gac69c40474180fe14c3761185b2db1c0c)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path);

1981

1993\_\_deprecated

[ 1994](group__lwm2m__api.md#gac188cd5fdd226dd105d73a4e391c601b)int [lwm2m\_engine\_delete\_res\_inst](group__lwm2m__api.md#gac188cd5fdd226dd105d73a4e391c601b)(const char \*pathstr);

1995

[ 2005](group__lwm2m__api.md#gacfeb63db0423e6730ffaa826a87eb262)int [lwm2m\_delete\_res\_inst](group__lwm2m__api.md#gacfeb63db0423e6730ffaa826a87eb262)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path);

2006

[ 2017](group__lwm2m__api.md#gab45cebf6f0b6b70974367ca453d16aeb)int [lwm2m\_update\_device\_service\_period](group__lwm2m__api.md#gab45cebf6f0b6b70974367ca453d16aeb)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) period\_ms);

2018

2032\_\_deprecated

[ 2033](group__lwm2m__api.md#ga07149d4b624a7294f4508df8c1681b1b)bool [lwm2m\_engine\_path\_is\_observed](group__lwm2m__api.md#ga07149d4b624a7294f4508df8c1681b1b)(const char \*pathstr);

2034

[ 2046](group__lwm2m__api.md#ga1065c729d5caa8ca13de7766fce77953)bool [lwm2m\_path\_is\_observed](group__lwm2m__api.md#ga1065c729d5caa8ca13de7766fce77953)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path);

2047

[ 2059](group__lwm2m__api.md#ga077e1abd612d31dd33fab52b7d205c39)int [lwm2m\_engine\_stop](group__lwm2m__api.md#ga077e1abd612d31dd33fab52b7d205c39)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx);

2060

[ 2072](group__lwm2m__api.md#ga9f72fbd0163b15c48ea09cf7d511e444)int [lwm2m\_engine\_start](group__lwm2m__api.md#ga9f72fbd0163b15c48ea09cf7d511e444)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx);

2073

[ 2085](group__lwm2m__api.md#ga919c7d6f418cda99c77fdaf54ae1a7b0)void [lwm2m\_acknowledge](group__lwm2m__api.md#ga919c7d6f418cda99c77fdaf54ae1a7b0)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx);

2086

[ 2093](group__lwm2m__api.md#gaca90ab8960a4ff01d44735dbc0405862)enum [lwm2m\_rd\_client\_event](group__lwm2m__api.md#gaca90ab8960a4ff01d44735dbc0405862) {

[ 2094](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc) [LWM2M\_RD\_CLIENT\_EVENT\_NONE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc),

[ 2095](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4) [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4),

[ 2096](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524) [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524),

[ 2097](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc) [LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_TRANSFER\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc),

[ 2098](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6) [LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6),

[ 2099](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541) [LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541),

[ 2100](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404) [LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404),

[ 2101](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683) [LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683),

[ 2102](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f) [LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f),

[ 2103](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b) [LWM2M\_RD\_CLIENT\_EVENT\_DISCONNECT](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b),

[ 2104](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe) [LWM2M\_RD\_CLIENT\_EVENT\_QUEUE\_MODE\_RX\_OFF](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe),

[ 2105](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525) [LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525),

[ 2106](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4) [LWM2M\_RD\_CLIENT\_EVENT\_NETWORK\_ERROR](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4),

[ 2107](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd) [LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd),

[ 2108](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13) [LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13),

[ 2109](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763) [LWM2M\_RD\_CLIENT\_EVENT\_SERVER\_DISABLED](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763),

2110};

2111

[ 2115](group__lwm2m__api.md#ga19c025d7df4dec8069ed59ffc788b00c)#define LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_FAILURE \

2116 LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT \_\_DEPRECATED\_MACRO

2117

2118/\*

2119 \* LwM2M RD client flags, used to configure LwM2M session.

2120 \*/

2121

[ 2125](group__lwm2m__api.md#ga3a3669237762fa8c23686e5e00b7809f)#define LWM2M\_RD\_CLIENT\_FLAG\_BOOTSTRAP BIT(0)

2126

[ 2148](group__lwm2m__api.md#ga9dfd46b8a535b1f28e644dc18f57fd79)int [lwm2m\_rd\_client\_start](group__lwm2m__api.md#ga9dfd46b8a535b1f28e644dc18f57fd79)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx, const char \*ep\_name,

2149 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9) event\_cb,

2150 [lwm2m\_observe\_cb\_t](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe) observe\_cb);

2151

[ 2167](group__lwm2m__api.md#gafd87e5d975c4d88973ac3e95e4d156ac)int [lwm2m\_rd\_client\_stop](group__lwm2m__api.md#gafd87e5d975c4d88973ac3e95e4d156ac)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx,

2168 [lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9) event\_cb, bool deregister);

2169

[ 2179](group__lwm2m__api.md#ga1a4dadb822a8241c5bdf339c21cc57a4)int [lwm2m\_engine\_pause](group__lwm2m__api.md#ga1a4dadb822a8241c5bdf339c21cc57a4)(void);

2180

[ 2191](group__lwm2m__api.md#ga178fea0407a5e98c4f5d5ad69688853a)int [lwm2m\_engine\_resume](group__lwm2m__api.md#ga178fea0407a5e98c4f5d5ad69688853a)(void);

2192

[ 2196](group__lwm2m__api.md#gab4ec7a22d01259b6ba9d3a7b6681e6f0)void [lwm2m\_rd\_client\_update](group__lwm2m__api.md#gab4ec7a22d01259b6ba9d3a7b6681e6f0)(void);

2197

[ 2201](group__lwm2m__api.md#gab97329844cd411195add5d72ad6aa4b7)#define LWM2M\_MAX\_PATH\_STR\_SIZE sizeof("/65535/65535/65535/65535")

2202

[ 2211](group__lwm2m__api.md#ga971c0636c19fe7f0a6e918622560a750)char \*[lwm2m\_path\_log\_buf](group__lwm2m__api.md#ga971c0636c19fe7f0a6e918622560a750)(char \*buf, struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path);

2212

[ 2219](group__lwm2m__api.md#ga20848e0942882e8c2cc40ee8a48b7bfd)enum [lwm2m\_send\_status](group__lwm2m__api.md#ga20848e0942882e8c2cc40ee8a48b7bfd) {

[ 2220](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4) [LWM2M\_SEND\_STATUS\_SUCCESS](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4),

[ 2221](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd) [LWM2M\_SEND\_STATUS\_FAILURE](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd),

[ 2222](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a) [LWM2M\_SEND\_STATUS\_TIMEOUT](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a),

2223};

2224

[ 2229](group__lwm2m__api.md#gaf5394884da53edb28fe4afc92bf40e6a)typedef void (\*[lwm2m\_send\_cb\_t](group__lwm2m__api.md#gaf5394884da53edb28fe4afc92bf40e6a))(enum [lwm2m\_send\_status](group__lwm2m__api.md#ga20848e0942882e8c2cc40ee8a48b7bfd) status);

2230

2244\_\_deprecated

[ 2245](group__lwm2m__api.md#ga5a0eed7bf3593f698194e5e047b07fa8)int [lwm2m\_engine\_send](group__lwm2m__api.md#ga5a0eed7bf3593f698194e5e047b07fa8)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, char const \*path\_list[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size,

2246 bool confirmation\_request);

2247

2261\_\_deprecated

[ 2262](group__lwm2m__api.md#gae6358ef4b4e3a1e342828ad9c429ff72)int [lwm2m\_send](group__lwm2m__api.md#gae6358ef4b4e3a1e342828ad9c429ff72)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) path\_list[],

2263 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size, bool confirmation\_request);

2264

[ 2276](group__lwm2m__api.md#ga026cc9288d2de17ec557e08b9b987ebc)int [lwm2m\_send\_cb](group__lwm2m__api.md#ga026cc9288d2de17ec557e08b9b987ebc)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx, const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) path\_list[],

2277 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) path\_list\_size, [lwm2m\_send\_cb\_t](group__lwm2m__api.md#gaf5394884da53edb28fe4afc92bf40e6a) reply\_cb);

2278

[ 2285](group__lwm2m__api.md#ga896caab5473eadff860872023d13b6c0)struct [lwm2m\_ctx](structlwm2m__ctx.md) \*[lwm2m\_rd\_client\_ctx](group__lwm2m__api.md#ga896caab5473eadff860872023d13b6c0)(void);

2286

2302\_\_deprecated

[ 2303](group__lwm2m__api.md#gaea2d9f740dd6d6152143be0360f19308)int [lwm2m\_engine\_enable\_cache](group__lwm2m__api.md#gaea2d9f740dd6d6152143be0360f19308)(char const \*resource\_path, struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) \*data\_cache,

2304 size\_t cache\_len);

2305

[ 2319](group__lwm2m__api.md#ga6975c5c4825afaccc52741eb54aca4cb)int [lwm2m\_enable\_cache](group__lwm2m__api.md#ga6975c5c4825afaccc52741eb54aca4cb)(const struct [lwm2m\_obj\_path](structlwm2m__obj__path.md) \*path, struct [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) \*data\_cache,

2320 size\_t cache\_len);

2321

[ 2325](group__lwm2m__api.md#ga11de8078091631cb88b26a9a460097ab)enum [lwm2m\_security\_mode\_e](group__lwm2m__api.md#ga11de8078091631cb88b26a9a460097ab) {

[ 2326](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25) [LWM2M\_SECURITY\_PSK](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25) = 0,

[ 2327](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716) [LWM2M\_SECURITY\_RAW\_PK](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716) = 1,

[ 2328](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba) [LWM2M\_SECURITY\_CERT](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba) = 2,

[ 2329](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7) [LWM2M\_SECURITY\_NOSEC](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7) = 3,

[ 2330](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824) [LWM2M\_SECURITY\_CERT\_EST](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824) = 4,

2331};

2332

[ 2341](group__lwm2m__api.md#ga6c05640737cfc4da71841a77de128be0)int [lwm2m\_security\_mode](group__lwm2m__api.md#ga6c05640737cfc4da71841a77de128be0)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx);

2342

[ 2353](group__lwm2m__api.md#ga956c4fc742a588b7b8b95ce8481f09bf)int [lwm2m\_set\_default\_sockopt](group__lwm2m__api.md#ga956c4fc742a588b7b8b95ce8481f09bf)(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*ctx);

2354

2355#endif /\* ZEPHYR\_INCLUDE\_NET\_LWM2M\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[coap.h](coap_8h.md)

CoAP implementation for Zephyr.

[lwm2m\_engine\_set\_u8](group__lwm2m__api.md#ga00a61b227bae53a70b0092bb94801ea8)

int lwm2m\_engine\_set\_u8(const char \*pathstr, uint8\_t value)

Set resource (instance) value (u8).

[lwm2m\_send\_cb](group__lwm2m__api.md#ga026cc9288d2de17ec557e08b9b987ebc)

int lwm2m\_send\_cb(struct lwm2m\_ctx \*ctx, const struct lwm2m\_obj\_path path\_list[], uint8\_t path\_list\_size, lwm2m\_send\_cb\_t reply\_cb)

[lwm2m\_engine\_set\_data\_cb\_t](group__lwm2m__api.md#ga02d8748f5b75e1f4344dd05def597ba9)

int(\* lwm2m\_engine\_set\_data\_cb\_t)(uint16\_t obj\_inst\_id, uint16\_t res\_id, uint16\_t res\_inst\_id, uint8\_t \*data, uint16\_t data\_len, bool last\_block, size\_t total\_size)

Asynchronous callback when data has been set to a resource buffer.

**Definition** lwm2m.h:349

[lwm2m\_get\_f64](group__lwm2m__api.md#ga03b72e96a67fcbf85feb5bf0b9df81ce)

int lwm2m\_get\_f64(const struct lwm2m\_obj\_path \*path, double \*value)

Get resource (instance) value (double).

[lwm2m\_set\_objlnk](group__lwm2m__api.md#ga04a18bd8a4eeea41a47803c16567d67b)

int lwm2m\_set\_objlnk(const struct lwm2m\_obj\_path \*path, const struct lwm2m\_objlnk \*value)

Set resource (instance) value (Objlnk).

[lwm2m\_engine\_path\_is\_observed](group__lwm2m__api.md#ga07149d4b624a7294f4508df8c1681b1b)

bool lwm2m\_engine\_path\_is\_observed(const char \*pathstr)

Check whether a path is observed.

[lwm2m\_engine\_stop](group__lwm2m__api.md#ga077e1abd612d31dd33fab52b7d205c39)

int lwm2m\_engine\_stop(struct lwm2m\_ctx \*client\_ctx)

Stop the LwM2M engine.

[lwm2m\_engine\_get\_float](group__lwm2m__api.md#ga0a272643082347fe6044bddbd7e5cebf)

int lwm2m\_engine\_get\_float(const char \*pathstr, double \*buf)

Get resource (instance) value (double).

[lwm2m\_get\_u32](group__lwm2m__api.md#ga0bc84cb39a7a537925ec7d62e54b8b48)

int lwm2m\_get\_u32(const struct lwm2m\_obj\_path \*path, uint32\_t \*value)

Get resource (instance) value (u32).

[lwm2m\_set\_res\_data\_len](group__lwm2m__api.md#ga0f2b115d231bea6622135d72b51f55ca)

int lwm2m\_set\_res\_data\_len(const struct lwm2m\_obj\_path \*path, uint16\_t data\_len)

Update data size for a resource.

[lwm2m\_path\_is\_observed](group__lwm2m__api.md#ga1065c729d5caa8ca13de7766fce77953)

bool lwm2m\_path\_is\_observed(const struct lwm2m\_obj\_path \*path)

Check whether a path is observed.

[lwm2m\_engine\_set\_s64](group__lwm2m__api.md#ga11619cc0907010018217b8d67e9e9f7e)

int lwm2m\_engine\_set\_s64(const char \*pathstr, int64\_t value)

Set resource (instance) value (s64).

[lwm2m\_security\_mode\_e](group__lwm2m__api.md#ga11de8078091631cb88b26a9a460097ab)

lwm2m\_security\_mode\_e

Security modes as defined in LwM2M Security object.

**Definition** lwm2m.h:2325

[lwm2m\_get\_s8](group__lwm2m__api.md#ga12817bfbf0a0cbb742568ee974a1c337)

int lwm2m\_get\_s8(const struct lwm2m\_obj\_path \*path, int8\_t \*value)

Get resource (instance) value (s8).

[lwm2m\_engine\_register\_pre\_write\_callback](group__lwm2m__api.md#ga1354bc59163db5b3435e8e86c8feafd8)

int lwm2m\_engine\_register\_pre\_write\_callback(const char \*pathstr, lwm2m\_engine\_get\_data\_cb\_t cb)

Set resource (instance) pre-write callback.

[lwm2m\_engine\_resume](group__lwm2m__api.md#ga178fea0407a5e98c4f5d5ad69688853a)

int lwm2m\_engine\_resume(void)

Resume the LwM2M engine thread.

[lwm2m\_set\_s64](group__lwm2m__api.md#ga18fcee379640c0dda32d6e3d14827260)

int lwm2m\_set\_s64(const struct lwm2m\_obj\_path \*path, int64\_t value)

Set resource (instance) value (s64).

[lwm2m\_engine\_pause](group__lwm2m__api.md#ga1a4dadb822a8241c5bdf339c21cc57a4)

int lwm2m\_engine\_pause(void)

Suspend the LwM2M engine Thread.

[lwm2m\_set\_u8](group__lwm2m__api.md#ga1aa3ff424b7190d0fbd9366626b2685c)

int lwm2m\_set\_u8(const struct lwm2m\_obj\_path \*path, uint8\_t value)

Set resource (instance) value (u8).

[lwm2m\_get\_u16](group__lwm2m__api.md#ga1b96848f96bdab9939bb2619d3e1059b)

int lwm2m\_get\_u16(const struct lwm2m\_obj\_path \*path, uint16\_t \*value)

Get resource (instance) value (u16).

[lwm2m\_engine\_set\_s16](group__lwm2m__api.md#ga1dd4952af0029c94a71f74734ae3a16c)

int lwm2m\_engine\_set\_s16(const char \*pathstr, int16\_t value)

Set resource (instance) value (s16).

[lwm2m\_firmware\_get\_update\_cb](group__lwm2m__api.md#ga1e4b8ba1b19ac9025dca3c4799bba84a)

lwm2m\_engine\_execute\_cb\_t lwm2m\_firmware\_get\_update\_cb(void)

Get the event callback for firmware update execute events.

[lwm2m\_set\_u16](group__lwm2m__api.md#ga1f06bb65571efee18db5d061f95399c3)

int lwm2m\_set\_u16(const struct lwm2m\_obj\_path \*path, uint16\_t value)

Set resource (instance) value (u16).

[lwm2m\_send\_status](group__lwm2m__api.md#ga20848e0942882e8c2cc40ee8a48b7bfd)

lwm2m\_send\_status

LwM2M send status.

**Definition** lwm2m.h:2219

[lwm2m\_get\_string](group__lwm2m__api.md#ga20fc58b25468bf309175db59d67b820b)

int lwm2m\_get\_string(const struct lwm2m\_obj\_path \*path, void \*str, uint16\_t buflen)

Get resource (instance) value (string).

[lwm2m\_engine\_register\_read\_callback](group__lwm2m__api.md#ga21d15060cce1c039a11106d71d681f4c)

int lwm2m\_engine\_register\_read\_callback(const char \*pathstr, lwm2m\_engine\_get\_data\_cb\_t cb)

Set resource (instance) read callback.

[lwm2m\_get\_s16](group__lwm2m__api.md#ga2426db6720b3f3e15e63022cabae5ece)

int lwm2m\_get\_s16(const struct lwm2m\_obj\_path \*path, int16\_t \*value)

Get resource (instance) value (s16).

[lwm2m\_engine\_get\_time](group__lwm2m__api.md#ga273fa47b65309b46aa1b73b224d0dfce)

int lwm2m\_engine\_get\_time(const char \*pathstr, time\_t \*buf)

Get resource (instance) value (Time).

[lwm2m\_engine\_set\_string](group__lwm2m__api.md#ga28911733660e7ce2f2f73c8eeb87de59)

int lwm2m\_engine\_set\_string(const char \*pathstr, const char \*data\_ptr)

Set resource (instance) value (string).

[lwm2m\_swmgmt\_set\_write\_package\_cb](group__lwm2m__api.md#ga293904118f972ae387c8aa85a1028b54)

int lwm2m\_swmgmt\_set\_write\_package\_cb(uint16\_t obj\_inst\_id, lwm2m\_engine\_set\_data\_cb\_t cb)

Set data callback for software management block transfer.

[lwm2m\_register\_exec\_callback](group__lwm2m__api.md#ga29cc5cdd697e94d7379b1fb178487916)

int lwm2m\_register\_exec\_callback(const struct lwm2m\_obj\_path \*path, lwm2m\_engine\_execute\_cb\_t cb)

Set resource execute event callback.

[lwm2m\_engine\_set\_opaque](group__lwm2m__api.md#ga2a891e26440f732b77ab90b979c8cb49)

int lwm2m\_engine\_set\_opaque(const char \*pathstr, const char \*data\_ptr, uint16\_t data\_len)

Set resource (instance) value (opaque buffer).

[lwm2m\_get\_time](group__lwm2m__api.md#ga2e1d41866b5ea35c5aa29bca9bb43812)

int lwm2m\_get\_time(const struct lwm2m\_obj\_path \*path, time\_t \*buf)

Get resource (instance) value (Time).

[lwm2m\_firmware\_set\_update\_cb\_inst](group__lwm2m__api.md#ga31d0f3e40b5e3d608d16a4268b2f1b29)

void lwm2m\_firmware\_set\_update\_cb\_inst(uint16\_t obj\_inst\_id, lwm2m\_engine\_execute\_cb\_t cb)

Set data callback to handle firmware update execute events.

[lwm2m\_engine\_set\_u32](group__lwm2m__api.md#ga326c722de4ecdcbc09adb52c83cf6400)

int lwm2m\_engine\_set\_u32(const char \*pathstr, uint32\_t value)

Set resource (instance) value (u32).

[lwm2m\_set\_s32](group__lwm2m__api.md#ga327e086959fc5649a5ef14f1f2943e88)

int lwm2m\_set\_s32(const struct lwm2m\_obj\_path \*path, int32\_t value)

Set resource (instance) value (s32).

[lwm2m\_engine\_create\_obj\_inst](group__lwm2m__api.md#ga32f393a9e302f1f60839fd2147ebd7e9)

int lwm2m\_engine\_create\_obj\_inst(const char \*pathstr)

Create an LwM2M object instance.

[lwm2m\_set\_f64](group__lwm2m__api.md#ga3386d3f2ad8d9713fc2283ed6921c2fc)

int lwm2m\_set\_f64(const struct lwm2m\_obj\_path \*path, const double value)

Set resource (instance) value (double).

[lwm2m\_engine\_get\_opaque](group__lwm2m__api.md#ga3439a579648c15bfe8883337c4618095)

int lwm2m\_engine\_get\_opaque(const char \*pathstr, void \*buf, uint16\_t buflen)

Get resource (instance) value (opaque buffer).

[lwm2m\_register\_create\_callback](group__lwm2m__api.md#ga346d547e02bd53ee83f83b2248449e98)

int lwm2m\_register\_create\_callback(uint16\_t obj\_id, lwm2m\_engine\_user\_cb\_t cb)

Set object instance create event callback.

[lwm2m\_firmware\_get\_update\_cb\_inst](group__lwm2m__api.md#ga34995e902b63c4d7d37ebd709d88a72a)

lwm2m\_engine\_execute\_cb\_t lwm2m\_firmware\_get\_update\_cb\_inst(uint16\_t obj\_inst\_id)

Get the event callback for firmware update execute events.

[lwm2m\_set\_s8](group__lwm2m__api.md#ga37261a4b9e54eab3d1d855a084d082aa)

int lwm2m\_set\_s8(const struct lwm2m\_obj\_path \*path, int8\_t value)

Set resource (instance) value (s8).

[lwm2m\_engine\_delete\_obj\_inst](group__lwm2m__api.md#ga3849e960b54bcb089ac00476da8fb430)

int lwm2m\_engine\_delete\_obj\_inst(const char \*pathstr)

Delete an LwM2M object instance.

[lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9)

void(\* lwm2m\_ctx\_event\_cb\_t)(struct lwm2m\_ctx \*ctx, enum lwm2m\_rd\_client\_event event)

Asynchronous RD client event callback.

**Definition** lwm2m.h:133

[lwm2m\_firmware\_set\_cancel\_cb](group__lwm2m__api.md#ga3955dca5cd6d67807ed75e61a4d84d84)

void lwm2m\_firmware\_set\_cancel\_cb(lwm2m\_engine\_user\_cb\_t cb)

Set callback for firmware update cancel.

[lwm2m\_register\_post\_write\_callback](group__lwm2m__api.md#ga3dd8b38e797173dae902404fb5b7a3f4)

int lwm2m\_register\_post\_write\_callback(const struct lwm2m\_obj\_path \*path, lwm2m\_engine\_set\_data\_cb\_t cb)

Set resource (instance) post-write callback.

[lwm2m\_engine\_get\_s32](group__lwm2m__api.md#ga40895289c1c8b778b6bf30d444dda63a)

int lwm2m\_engine\_get\_s32(const char \*pathstr, int32\_t \*value)

Get resource (instance) value (s32).

[lwm2m\_engine\_update\_observer\_min\_period](group__lwm2m__api.md#ga489c8ea2eb89c7c6dc008002ab2ea836)

int lwm2m\_engine\_update\_observer\_min\_period(struct lwm2m\_ctx \*client\_ctx, const char \*pathstr, uint32\_t period\_s)

Change an observer's pmin value.

[lwm2m\_firmware\_get\_write\_cb](group__lwm2m__api.md#ga4bf0bbedf5573ac18a11ac4fced11284)

lwm2m\_engine\_set\_data\_cb\_t lwm2m\_firmware\_get\_write\_cb(void)

Get the data callback for firmware block transfer writes.

[lwm2m\_get\_objlnk](group__lwm2m__api.md#ga4de941c36cf678e12da6e05c378a92e5)

int lwm2m\_get\_objlnk(const struct lwm2m\_obj\_path \*path, struct lwm2m\_objlnk \*buf)

Get resource (instance) value (Objlnk).

[lwm2m\_engine\_set\_s32](group__lwm2m__api.md#ga4f45dc38b5e6a55633474ff5d5447ecb)

int lwm2m\_engine\_set\_s32(const char \*pathstr, int32\_t value)

Set resource (instance) value (s32).

[lwm2m\_engine\_set\_u16](group__lwm2m__api.md#ga4fcea78d9506822ee76df465cf71ffdf)

int lwm2m\_engine\_set\_u16(const char \*pathstr, uint16\_t value)

Set resource (instance) value (u16).

[lwm2m\_engine\_get\_u8](group__lwm2m__api.md#ga50ee578c777c7b8a1b0fbe028c8342ec)

int lwm2m\_engine\_get\_u8(const char \*pathstr, uint8\_t \*value)

Get resource (instance) value (u8).

[lwm2m\_create\_object\_inst](group__lwm2m__api.md#ga53f5b4c5967e93c7dd224fce8f416265)

int lwm2m\_create\_object\_inst(const struct lwm2m\_obj\_path \*path)

Create an LwM2M object instance.

[lwm2m\_set\_res\_buf](group__lwm2m__api.md#ga56a2aecd38baedb5dc17258610c4780d)

int lwm2m\_set\_res\_buf(const struct lwm2m\_obj\_path \*path, void \*buffer\_ptr, uint16\_t buffer\_len, uint16\_t data\_len, uint8\_t data\_flags)

Set data buffer for a resource.

[lwm2m\_swmgmt\_install\_completed](group__lwm2m__api.md#ga573e128348fb2f43a33bd09332dd677f)

int lwm2m\_swmgmt\_install\_completed(uint16\_t obj\_inst\_id, int error\_code)

Function to be called when a Software Management object instance completed the Install operation.

[lwm2m\_engine\_send](group__lwm2m__api.md#ga5a0eed7bf3593f698194e5e047b07fa8)

int lwm2m\_engine\_send(struct lwm2m\_ctx \*ctx, char const \*path\_list[], uint8\_t path\_list\_size, bool confirmation\_request)

[lwm2m\_engine\_register\_post\_write\_callback](group__lwm2m__api.md#ga5c43bcdb0575f8c56354d6b4e30641a3)

int lwm2m\_engine\_register\_post\_write\_callback(const char \*pathstr, lwm2m\_engine\_set\_data\_cb\_t cb)

Set resource (instance) post-write callback.

[lwm2m\_engine\_get\_data\_cb\_t](group__lwm2m__api.md#ga5e531aade0537eb5e3f5756e9287e384)

void \*(\* lwm2m\_engine\_get\_data\_cb\_t)(uint16\_t obj\_inst\_id, uint16\_t res\_id, uint16\_t res\_inst\_id, size\_t \*data\_len)

Asynchronous callback to get a resource buffer and length.

**Definition** lwm2m.h:318

[lwm2m\_engine\_get\_bool](group__lwm2m__api.md#ga606e281a1146f930d7c0675d5881c7d6)

int lwm2m\_engine\_get\_bool(const char \*pathstr, bool \*value)

Get resource (instance) value (bool).

[lwm2m\_firmware\_set\_update\_cb](group__lwm2m__api.md#ga61eb38e42d9e1b3f467c43a324f2fc65)

void lwm2m\_firmware\_set\_update\_cb(lwm2m\_engine\_execute\_cb\_t cb)

Set data callback to handle firmware update execute events.

[lwm2m\_engine\_get\_res\_data](group__lwm2m__api.md#ga630079a8d2f2acae1c313297cfdbada9)

int lwm2m\_engine\_get\_res\_data(const char \*pathstr, void \*\*data\_ptr, uint16\_t \*data\_len, uint8\_t \*data\_flags)

Get data buffer for a resource.

[lwm2m\_engine\_create\_res\_inst](group__lwm2m__api.md#ga64b0427f36b6d2d2f8af8cc2e35cdb89)

int lwm2m\_engine\_create\_res\_inst(const char \*pathstr)

Create a resource instance.

[lwm2m\_engine\_set\_res\_buf](group__lwm2m__api.md#ga66bdc3f3a4d0e88b036c9704abfbcafc)

int lwm2m\_engine\_set\_res\_buf(const char \*pathstr, void \*buffer\_ptr, uint16\_t buffer\_len, uint16\_t data\_len, uint8\_t data\_flags)

Set data buffer for a resource.

[lwm2m\_firmware\_set\_write\_cb](group__lwm2m__api.md#ga6878ea0ebb512b19a4fb0859756f51d0)

void lwm2m\_firmware\_set\_write\_cb(lwm2m\_engine\_set\_data\_cb\_t cb)

Set data callback for firmware block transfer.

[lwm2m\_engine\_get\_u16](group__lwm2m__api.md#ga68986109d78b60f83f9cd85742ed80fb)

int lwm2m\_engine\_get\_u16(const char \*pathstr, uint16\_t \*value)

Get resource (instance) value (u16).

[lwm2m\_enable\_cache](group__lwm2m__api.md#ga6975c5c4825afaccc52741eb54aca4cb)

int lwm2m\_enable\_cache(const struct lwm2m\_obj\_path \*path, struct lwm2m\_time\_series\_elem \*data\_cache, size\_t cache\_len)

[lwm2m\_engine\_register\_delete\_callback](group__lwm2m__api.md#ga6a5dfdd29055bed245bf16ecc5829f95)

int lwm2m\_engine\_register\_delete\_callback(uint16\_t obj\_id, lwm2m\_engine\_user\_cb\_t cb)

Set object instance delete event callback.

[lwm2m\_update\_observer\_max\_period](group__lwm2m__api.md#ga6acccbcd879901574aceab53a21800fc)

int lwm2m\_update\_observer\_max\_period(struct lwm2m\_ctx \*client\_ctx, const struct lwm2m\_obj\_path \*path, uint32\_t period\_s)

Change an observer's pmax value.

[lwm2m\_security\_mode](group__lwm2m__api.md#ga6c05640737cfc4da71841a77de128be0)

int lwm2m\_security\_mode(struct lwm2m\_ctx \*ctx)

Read security mode from selected security object instance.

[lwm2m\_firmware\_get\_cancel\_cb\_inst](group__lwm2m__api.md#ga6f4b3e08c7e03cff4bf31e2f2999971e)

lwm2m\_engine\_user\_cb\_t lwm2m\_firmware\_get\_cancel\_cb\_inst(uint16\_t obj\_inst\_id)

Get the callback for firmware update cancel.

[lwm2m\_register\_pre\_write\_callback](group__lwm2m__api.md#ga6f775837e07ba9b0032be8917a593e16)

int lwm2m\_register\_pre\_write\_callback(const struct lwm2m\_obj\_path \*path, lwm2m\_engine\_get\_data\_cb\_t cb)

Set resource (instance) pre-write callback.

[lwm2m\_engine\_get\_s8](group__lwm2m__api.md#ga701d36c7b7a63c8214bfa30c0c19c946)

int lwm2m\_engine\_get\_s8(const char \*pathstr, int8\_t \*value)

Get resource (instance) value (s8).

[lwm2m\_set\_time](group__lwm2m__api.md#ga7194ad24842e35130d8af7f5104c0844)

int lwm2m\_set\_time(const struct lwm2m\_obj\_path \*path, time\_t value)

Set resource (instance) value (Time).

[lwm2m\_set\_string](group__lwm2m__api.md#ga7217f33bf705011d91ba66c86a4d5747)

int lwm2m\_set\_string(const struct lwm2m\_obj\_path \*path, const char \*data\_ptr)

Set resource (instance) value (string).

[lwm2m\_engine\_get\_string](group__lwm2m__api.md#ga72e27dfaf0881561245d01d6f800f0dc)

int lwm2m\_engine\_get\_string(const char \*pathstr, void \*str, uint16\_t buflen)

Get resource (instance) value (string).

[lwm2m\_socket\_states](group__lwm2m__api.md#ga7611c1aebb0309ee8340e06dd8ee234d)

lwm2m\_socket\_states

Different traffic states of the LwM2M socket.

**Definition** lwm2m.h:146

[lwm2m\_swmgmt\_set\_deactivate\_cb](group__lwm2m__api.md#ga7a2b93b918257bece819dc44804f27f5)

int lwm2m\_swmgmt\_set\_deactivate\_cb(uint16\_t obj\_inst\_id, lwm2m\_engine\_execute\_cb\_t cb)

Set callback to handle software deactivation requests.

[lwm2m\_engine\_get\_s64](group__lwm2m__api.md#ga7ad1a482074d033ad1def72882efd245)

int lwm2m\_engine\_get\_s64(const char \*pathstr, int64\_t \*value)

Get resource (instance) value (s64).

[lwm2m\_engine\_set\_u64](group__lwm2m__api.md#ga7d04c579284369233156a0597f09ab83)

int lwm2m\_engine\_set\_u64(const char \*pathstr, uint64\_t value)

Set resource (instance) value (u64).

[lwm2m\_get\_u64](group__lwm2m__api.md#ga831d229d9a4b983223dff626bbde7a66)

int lwm2m\_get\_u64(const struct lwm2m\_obj\_path \*path, uint64\_t \*value)

Get resource (instance) value (u64).

[lwm2m\_engine\_set\_res\_data\_len](group__lwm2m__api.md#ga87833da93894dc5df45b91dfaebf3f91)

int lwm2m\_engine\_set\_res\_data\_len(const char \*pathstr, uint16\_t data\_len)

Update data size for a resource.

[lwm2m\_rd\_client\_ctx](group__lwm2m__api.md#ga896caab5473eadff860872023d13b6c0)

struct lwm2m\_ctx \* lwm2m\_rd\_client\_ctx(void)

&#160;

[lwm2m\_set\_u64](group__lwm2m__api.md#ga8a751dc8384cc47f9c14d916e20ae19d)

int lwm2m\_set\_u64(const struct lwm2m\_obj\_path \*path, uint64\_t value)

Set resource (instance) value (u64).

[lwm2m\_engine\_set\_bool](group__lwm2m__api.md#ga8c82346313a9bf1234f72d71a5db34f5)

int lwm2m\_engine\_set\_bool(const char \*pathstr, bool value)

Set resource (instance) value (bool).

[lwm2m\_engine\_get\_u64](group__lwm2m__api.md#ga8d9068217afe09b0930996e5796b8aac)

int lwm2m\_engine\_get\_u64(const char \*pathstr, uint64\_t \*value)

Get resource (instance) value (u64).

[lwm2m\_acknowledge](group__lwm2m__api.md#ga919c7d6f418cda99c77fdaf54ae1a7b0)

void lwm2m\_acknowledge(struct lwm2m\_ctx \*client\_ctx)

Acknowledge the currently processed request with an empty ACK.

[lwm2m\_register\_delete\_callback](group__lwm2m__api.md#ga92d7e6d81ef674a6c311e1717c6bf373)

int lwm2m\_register\_delete\_callback(uint16\_t obj\_id, lwm2m\_engine\_user\_cb\_t cb)

Set object instance delete event callback.

[lwm2m\_set\_u32](group__lwm2m__api.md#ga9481e570b121404dc1be1ce23d904894)

int lwm2m\_set\_u32(const struct lwm2m\_obj\_path \*path, uint32\_t value)

Set resource (instance) value (u32).

[lwm2m\_event\_log\_set\_read\_log\_data\_cb](group__lwm2m__api.md#ga950557bce8c510bcc8b0704e7bc4a9dc)

void lwm2m\_event\_log\_set\_read\_log\_data\_cb(lwm2m\_engine\_get\_data\_cb\_t cb)

Set callback to read log data.

[lwm2m\_firmware\_get\_cancel\_cb](group__lwm2m__api.md#ga9561c1b8407d888f6fbe1e0ceab1c235)

lwm2m\_engine\_user\_cb\_t lwm2m\_firmware\_get\_cancel\_cb(void)

Get a callback for firmware update cancel.

[lwm2m\_set\_default\_sockopt](group__lwm2m__api.md#ga956c4fc742a588b7b8b95ce8481f09bf)

int lwm2m\_set\_default\_sockopt(struct lwm2m\_ctx \*ctx)

Set default socket options for DTLS connections.

[lwm2m\_engine\_get\_s16](group__lwm2m__api.md#ga96f29e6d897b96fedc7f3e19bd906f7c)

int lwm2m\_engine\_get\_s16(const char \*pathstr, int16\_t \*value)

Get resource (instance) value (s16).

[lwm2m\_path\_log\_buf](group__lwm2m__api.md#ga971c0636c19fe7f0a6e918622560a750)

char \* lwm2m\_path\_log\_buf(char \*buf, struct lwm2m\_obj\_path \*path)

Helper function to print path objects' contents to log.

[lwm2m\_get\_s32](group__lwm2m__api.md#ga99d7189efa25881dbcddd99e2a795f1b)

int lwm2m\_get\_s32(const struct lwm2m\_obj\_path \*path, int32\_t \*value)

Get resource (instance) value (s32).

[lwm2m\_registry\_lock](group__lwm2m__api.md#ga9a0cdcc9fc6d37462eddeb54e5d1f87a)

void lwm2m\_registry\_lock(void)

Locks the registry for this thread.

[lwm2m\_rd\_client\_start](group__lwm2m__api.md#ga9dfd46b8a535b1f28e644dc18f57fd79)

int lwm2m\_rd\_client\_start(struct lwm2m\_ctx \*client\_ctx, const char \*ep\_name, uint32\_t flags, lwm2m\_ctx\_event\_cb\_t event\_cb, lwm2m\_observe\_cb\_t observe\_cb)

Start the LwM2M RD (Registration / Discovery) Client.

[lwm2m\_set\_bool](group__lwm2m__api.md#ga9ef21d06bef8a97b7666c0aa7fa753b4)

int lwm2m\_set\_bool(const struct lwm2m\_obj\_path \*path, bool value)

Set resource (instance) value (bool).

[lwm2m\_engine\_start](group__lwm2m__api.md#ga9f72fbd0163b15c48ea09cf7d511e444)

int lwm2m\_engine\_start(struct lwm2m\_ctx \*client\_ctx)

Start the LwM2M engine.

[lwm2m\_engine\_register\_create\_callback](group__lwm2m__api.md#gaa198bfb55f98183cbd33169468ae0bcc)

int lwm2m\_engine\_register\_create\_callback(uint16\_t obj\_id, lwm2m\_engine\_user\_cb\_t cb)

Set object instance create event callback.

[lwm2m\_firmware\_set\_cancel\_cb\_inst](group__lwm2m__api.md#gaa200b524e505f64247f1e7472c5f36d4)

void lwm2m\_firmware\_set\_cancel\_cb\_inst(uint16\_t obj\_inst\_id, lwm2m\_engine\_user\_cb\_t cb)

Set data callback for firmware update cancel.

[lwm2m\_set\_opaque](group__lwm2m__api.md#gaaef33bdf3f48fd91abdb50db4d5460f9)

int lwm2m\_set\_opaque(const struct lwm2m\_obj\_path \*path, const char \*data\_ptr, uint16\_t data\_len)

Set resource (instance) value (opaque buffer).

[lwm2m\_get\_s64](group__lwm2m__api.md#gaaffe06ca9ee5302fb6e26164f250653e)

int lwm2m\_get\_s64(const struct lwm2m\_obj\_path \*path, int64\_t \*value)

Get resource (instance) value (s64).

[lwm2m\_registry\_unlock](group__lwm2m__api.md#gab09b62982c34887cdd16c30659d3349a)

void lwm2m\_registry\_unlock(void)

Unlocks the registry previously locked by lwm2m\_registry\_lock().

[lwm2m\_update\_device\_service\_period](group__lwm2m__api.md#gab45cebf6f0b6b70974367ca453d16aeb)

int lwm2m\_update\_device\_service\_period(uint32\_t period\_ms)

Update the period of the device service.

[lwm2m\_rd\_client\_update](group__lwm2m__api.md#gab4ec7a22d01259b6ba9d3a7b6681e6f0)

void lwm2m\_rd\_client\_update(void)

Trigger a Registration Update of the LwM2M RD Client.

[lwm2m\_swmgmt\_set\_read\_package\_version\_cb](group__lwm2m__api.md#gab59370ce4fdc94adb4903f22ab1f95b2)

int lwm2m\_swmgmt\_set\_read\_package\_version\_cb(uint16\_t obj\_inst\_id, lwm2m\_engine\_get\_data\_cb\_t cb)

Set callback to read software package.

[lwm2m\_engine\_user\_cb\_t](group__lwm2m__api.md#gabcbca483b310e0c4cd68aef2d9cda0bf)

int(\* lwm2m\_engine\_user\_cb\_t)(uint16\_t obj\_inst\_id)

Asynchronous event notification callback.

**Definition** lwm2m.h:370

[lwm2m\_engine\_set\_res\_data](group__lwm2m__api.md#gabf56a29aec75675099df2d45ca802718)

int lwm2m\_engine\_set\_res\_data(const char \*pathstr, void \*data\_ptr, uint16\_t data\_len, uint8\_t data\_flags)

Set data buffer for a resource.

[lwm2m\_device\_add\_err](group__lwm2m__api.md#gabf8726f0438477863423947a7bb77ce2)

int lwm2m\_device\_add\_err(uint8\_t error\_code)

Register a new error code with LwM2M Device object.

[lwm2m\_get\_res\_buf](group__lwm2m__api.md#gac0b6669d8a19b03eb8b08cbbcdb0c192)

int lwm2m\_get\_res\_buf(const struct lwm2m\_obj\_path \*path, void \*\*buffer\_ptr, uint16\_t \*buffer\_len, uint16\_t \*data\_len, uint8\_t \*data\_flags)

Get data buffer for a resource.

[lwm2m\_engine\_delete\_res\_inst](group__lwm2m__api.md#gac188cd5fdd226dd105d73a4e391c601b)

int lwm2m\_engine\_delete\_res\_inst(const char \*pathstr)

Delete a resource instance.

[lwm2m\_engine\_register\_validate\_callback](group__lwm2m__api.md#gac1c92e1ee3a804b325aacfe116bad096)

int lwm2m\_engine\_register\_validate\_callback(const char \*pathstr, lwm2m\_engine\_set\_data\_cb\_t cb)

Set resource (instance) validation callback.

[lwm2m\_swmgmt\_set\_activate\_cb](group__lwm2m__api.md#gac374d0559056ddb9cf43deae932fd128)

int lwm2m\_swmgmt\_set\_activate\_cb(uint16\_t obj\_inst\_id, lwm2m\_engine\_execute\_cb\_t cb)

Set callback to handle software activation requests.

[lwm2m\_firmware\_set\_write\_cb\_inst](group__lwm2m__api.md#gac4e4a819e54344657d70ec479eb6ec8d)

void lwm2m\_firmware\_set\_write\_cb\_inst(uint16\_t obj\_inst\_id, lwm2m\_engine\_set\_data\_cb\_t cb)

Set data callback for firmware block transfer.

[lwm2m\_get\_u8](group__lwm2m__api.md#gac56e804962e529799c771d81ac1fd027)

int lwm2m\_get\_u8(const struct lwm2m\_obj\_path \*path, uint8\_t \*value)

Get resource (instance) value (u8).

[lwm2m\_create\_res\_inst](group__lwm2m__api.md#gac69c40474180fe14c3761185b2db1c0c)

int lwm2m\_create\_res\_inst(const struct lwm2m\_obj\_path \*path)

Create a resource instance.

[lwm2m\_observe\_event](group__lwm2m__api.md#gac8d63952ec94ca6cfb1dbe12a6c53bfb)

lwm2m\_observe\_event

Observe callback events.

**Definition** lwm2m.h:104

[lwm2m\_rd\_client\_event](group__lwm2m__api.md#gaca90ab8960a4ff01d44735dbc0405862)

lwm2m\_rd\_client\_event

LwM2M RD client events.

**Definition** lwm2m.h:2093

[lwm2m\_engine\_update\_observer\_max\_period](group__lwm2m__api.md#gacb717ef5a36524e6f0f78b90cc803577)

int lwm2m\_engine\_update\_observer\_max\_period(struct lwm2m\_ctx \*client\_ctx, const char \*pathstr, uint32\_t period\_s)

Change an observer's pmax value.

[lwm2m\_swmgmt\_set\_delete\_package\_cb](group__lwm2m__api.md#gacf209563efdc5f3201152088c52d05c3)

int lwm2m\_swmgmt\_set\_delete\_package\_cb(uint16\_t obj\_inst\_id, lwm2m\_engine\_execute\_cb\_t cb)

Set callback to handle software uninstall requests.

[lwm2m\_delete\_res\_inst](group__lwm2m__api.md#gacfeb63db0423e6730ffaa826a87eb262)

int lwm2m\_delete\_res\_inst(const struct lwm2m\_obj\_path \*path)

Delete a resource instance.

[lwm2m\_engine\_register\_exec\_callback](group__lwm2m__api.md#gad213063b7e68bd7b4f3ce3de3736a237)

int lwm2m\_engine\_register\_exec\_callback(const char \*pathstr, lwm2m\_engine\_execute\_cb\_t cb)

Set resource execute event callback.

[lwm2m\_engine\_set\_time](group__lwm2m__api.md#gad3621c4a9ddfdc2a9e8fe2df058aefd7)

int lwm2m\_engine\_set\_time(const char \*pathstr, time\_t value)

Set resource (instance) value (Time).

[lwm2m\_set\_s16](group__lwm2m__api.md#gad548ffedcb8328b23eb32476a97be6ee)

int lwm2m\_set\_s16(const struct lwm2m\_obj\_path \*path, int16\_t value)

Set resource (instance) value (s16).

[lwm2m\_register\_validate\_callback](group__lwm2m__api.md#gad6e5fd4815f409ad59ad631b03199333)

int lwm2m\_register\_validate\_callback(const struct lwm2m\_obj\_path \*path, lwm2m\_engine\_set\_data\_cb\_t cb)

Set resource (instance) validation callback.

[lwm2m\_firmware\_get\_write\_cb\_inst](group__lwm2m__api.md#gad7334f06c3bdb14485597794a417152d)

lwm2m\_engine\_set\_data\_cb\_t lwm2m\_firmware\_get\_write\_cb\_inst(uint16\_t obj\_inst\_id)

Get the data callback for firmware block transfer writes.

[lwm2m\_observe\_cb\_t](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe)

void(\* lwm2m\_observe\_cb\_t)(enum lwm2m\_observe\_event event, struct lwm2m\_obj\_path \*path, void \*user\_data)

Observe callback indicating observer adds and deletes, and notification ACKs and timeouts.

**Definition** lwm2m.h:121

[lwm2m\_engine\_set\_objlnk](group__lwm2m__api.md#gada5007c34ce2ee72017065b32f1cee58)

int lwm2m\_engine\_set\_objlnk(const char \*pathstr, const struct lwm2m\_objlnk \*value)

Set resource (instance) value (Objlnk).

[lwm2m\_update\_observer\_min\_period](group__lwm2m__api.md#gadd163806d70713d8349a9db484ba88bf)

int lwm2m\_update\_observer\_min\_period(struct lwm2m\_ctx \*client\_ctx, const struct lwm2m\_obj\_path \*path, uint32\_t period\_s)

Change an observer's pmin value.

[lwm2m\_swmgmt\_set\_install\_package\_cb](group__lwm2m__api.md#gadfc00060c0b538ed576b5e3edd7dac80)

int lwm2m\_swmgmt\_set\_install\_package\_cb(uint16\_t obj\_inst\_id, lwm2m\_engine\_execute\_cb\_t cb)

Set callback to handle software install requests.

[lwm2m\_get\_opaque](group__lwm2m__api.md#gae245a9a1d9456af7e6283b1074944606)

int lwm2m\_get\_opaque(const struct lwm2m\_obj\_path \*path, void \*buf, uint16\_t buflen)

Get resource (instance) value (opaque buffer).

[lwm2m\_send](group__lwm2m__api.md#gae6358ef4b4e3a1e342828ad9c429ff72)

int lwm2m\_send(struct lwm2m\_ctx \*ctx, const struct lwm2m\_obj\_path path\_list[], uint8\_t path\_list\_size, bool confirmation\_request)

[lwm2m\_engine\_set\_s8](group__lwm2m__api.md#gae665c8bb81c0aef3b960b087ff0f97f8)

int lwm2m\_engine\_set\_s8(const char \*pathstr, int8\_t value)

Set resource (instance) value (s8).

[lwm2m\_socket\_fault\_cb\_t](group__lwm2m__api.md#gae7bf50f9abf1b82b76ac3e9175e685ac)

void(\* lwm2m\_socket\_fault\_cb\_t)(int error)

Callback function called when a socket error is encountered.

**Definition** lwm2m.h:90

[lwm2m\_engine\_set\_float](group__lwm2m__api.md#gae85eb5da495b7d42b10cf01c0d826632)

int lwm2m\_engine\_set\_float(const char \*pathstr, const double \*value)

Set resource (instance) value (double).

[lwm2m\_engine\_enable\_cache](group__lwm2m__api.md#gaea2d9f740dd6d6152143be0360f19308)

int lwm2m\_engine\_enable\_cache(char const \*resource\_path, struct lwm2m\_time\_series\_elem \*data\_cache, size\_t cache\_len)

[lwm2m\_engine\_execute\_cb\_t](group__lwm2m__api.md#gaeb32bcd4981b4c7bd891f99668ebc0fe)

int(\* lwm2m\_engine\_execute\_cb\_t)(uint16\_t obj\_inst\_id, uint8\_t \*args, uint16\_t args\_len)

Asynchronous execute notification callback.

**Definition** lwm2m.h:388

[lwm2m\_register\_read\_callback](group__lwm2m__api.md#gaf33bd6a527b6d399f3d92b666ac77dfb)

int lwm2m\_register\_read\_callback(const struct lwm2m\_obj\_path \*path, lwm2m\_engine\_get\_data\_cb\_t cb)

Set resource (instance) read callback.

[lwm2m\_engine\_get\_objlnk](group__lwm2m__api.md#gaf4b23e412fcff5f2838f3e232a3cd224)

int lwm2m\_engine\_get\_objlnk(const char \*pathstr, struct lwm2m\_objlnk \*buf)

Get resource (instance) value (Objlnk).

[lwm2m\_send\_cb\_t](group__lwm2m__api.md#gaf5394884da53edb28fe4afc92bf40e6a)

void(\* lwm2m\_send\_cb\_t)(enum lwm2m\_send\_status status)

Callback returning send status.

**Definition** lwm2m.h:2229

[lwm2m\_delete\_object\_inst](group__lwm2m__api.md#gaf921d4bc96090ef8735d90d173feab94)

int lwm2m\_delete\_object\_inst(const struct lwm2m\_obj\_path \*path)

Delete an LwM2M object instance.

[lwm2m\_rd\_client\_stop](group__lwm2m__api.md#gafd87e5d975c4d88973ac3e95e4d156ac)

int lwm2m\_rd\_client\_stop(struct lwm2m\_ctx \*client\_ctx, lwm2m\_ctx\_event\_cb\_t event\_cb, bool deregister)

Stop the LwM2M RD (De-register) Client.

[lwm2m\_get\_bool](group__lwm2m__api.md#gafdc72844ce0ca417e297d76288155aa4)

int lwm2m\_get\_bool(const struct lwm2m\_obj\_path \*path, bool \*value)

Get resource (instance) value (bool).

[lwm2m\_engine\_get\_u32](group__lwm2m__api.md#gafddb717b3f43619e03a240660f65eb03)

int lwm2m\_engine\_get\_u32(const char \*pathstr, uint32\_t \*value)

Get resource (instance) value (u32).

[lwm2m\_engine\_get\_res\_buf](group__lwm2m__api.md#gaff5e10bc0fa34c1fe72a0b4e1ed2bc39)

int lwm2m\_engine\_get\_res\_buf(const char \*pathstr, void \*\*buffer\_ptr, uint16\_t \*buffer\_len, uint16\_t \*data\_len, uint8\_t \*data\_flags)

Get data buffer for a resource.

[LWM2M\_SECURITY\_PSK](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25)

@ LWM2M\_SECURITY\_PSK

Pre-Shared Key mode.

**Definition** lwm2m.h:2326

[LWM2M\_SECURITY\_RAW\_PK](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716)

@ LWM2M\_SECURITY\_RAW\_PK

Raw Public Key mode.

**Definition** lwm2m.h:2327

[LWM2M\_SECURITY\_CERT](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba)

@ LWM2M\_SECURITY\_CERT

Certificate mode.

**Definition** lwm2m.h:2328

[LWM2M\_SECURITY\_CERT\_EST](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824)

@ LWM2M\_SECURITY\_CERT\_EST

Certificate mode with EST.

**Definition** lwm2m.h:2330

[LWM2M\_SECURITY\_NOSEC](group__lwm2m__api.md#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7)

@ LWM2M\_SECURITY\_NOSEC

NoSec mode.

**Definition** lwm2m.h:2329

[LWM2M\_SEND\_STATUS\_SUCCESS](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4)

@ LWM2M\_SEND\_STATUS\_SUCCESS

**Definition** lwm2m.h:2220

[LWM2M\_SEND\_STATUS\_FAILURE](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd)

@ LWM2M\_SEND\_STATUS\_FAILURE

**Definition** lwm2m.h:2221

[LWM2M\_SEND\_STATUS\_TIMEOUT](group__lwm2m__api.md#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a)

@ LWM2M\_SEND\_STATUS\_TIMEOUT

**Definition** lwm2m.h:2222

[LWM2M\_SOCKET\_STATE\_NO\_DATA](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915)

@ LWM2M\_SOCKET\_STATE\_NO\_DATA

No more data is expected.

**Definition** lwm2m.h:150

[LWM2M\_SOCKET\_STATE\_ONE\_RESPONSE](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711)

@ LWM2M\_SOCKET\_STATE\_ONE\_RESPONSE

One response is expected for the next message.

**Definition** lwm2m.h:148

[LWM2M\_SOCKET\_STATE\_ONGOING](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab)

@ LWM2M\_SOCKET\_STATE\_ONGOING

Ongoing traffic is expected.

**Definition** lwm2m.h:147

[LWM2M\_SOCKET\_STATE\_LAST](group__lwm2m__api.md#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100)

@ LWM2M\_SOCKET\_STATE\_LAST

Next message is the last one.

**Definition** lwm2m.h:149

[LWM2M\_OBSERVE\_EVENT\_OBSERVER\_ADDED](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3)

@ LWM2M\_OBSERVE\_EVENT\_OBSERVER\_ADDED

Observer added.

**Definition** lwm2m.h:105

[LWM2M\_OBSERVE\_EVENT\_NOTIFY\_TIMEOUT](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e)

@ LWM2M\_OBSERVE\_EVENT\_NOTIFY\_TIMEOUT

Notification timed out.

**Definition** lwm2m.h:108

[LWM2M\_OBSERVE\_EVENT\_NOTIFY\_ACK](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885)

@ LWM2M\_OBSERVE\_EVENT\_NOTIFY\_ACK

Notification ACKed.

**Definition** lwm2m.h:107

[LWM2M\_OBSERVE\_EVENT\_OBSERVER\_REMOVED](group__lwm2m__api.md#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c)

@ LWM2M\_OBSERVE\_EVENT\_OBSERVER\_REMOVED

Observer removed.

**Definition** lwm2m.h:106

[LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f)

@ LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER\_FAILURE

**Definition** lwm2m.h:2102

[LWM2M\_RD\_CLIENT\_EVENT\_QUEUE\_MODE\_RX\_OFF](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe)

@ LWM2M\_RD\_CLIENT\_EVENT\_QUEUE\_MODE\_RX\_OFF

**Definition** lwm2m.h:2104

[LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_TRANSFER\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc)

@ LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_TRANSFER\_COMPLETE

**Definition** lwm2m.h:2097

[LWM2M\_RD\_CLIENT\_EVENT\_SERVER\_DISABLED](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763)

@ LWM2M\_RD\_CLIENT\_EVENT\_SERVER\_DISABLED

**Definition** lwm2m.h:2109

[LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541)

@ LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE

**Definition** lwm2m.h:2099

[LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404)

@ LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT

**Definition** lwm2m.h:2100

[LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683)

@ LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE

**Definition** lwm2m.h:2101

[LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13)

@ LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER

**Definition** lwm2m.h:2108

[LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd)

@ LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE

**Definition** lwm2m.h:2107

[LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4)

@ LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_FAILURE

**Definition** lwm2m.h:2095

[LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_COMPLETE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524)

@ LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_COMPLETE

**Definition** lwm2m.h:2096

[LWM2M\_RD\_CLIENT\_EVENT\_DISCONNECT](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b)

@ LWM2M\_RD\_CLIENT\_EVENT\_DISCONNECT

**Definition** lwm2m.h:2103

[LWM2M\_RD\_CLIENT\_EVENT\_NONE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc)

@ LWM2M\_RD\_CLIENT\_EVENT\_NONE

**Definition** lwm2m.h:2094

[LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_FAILURE](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6)

@ LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_FAILURE

**Definition** lwm2m.h:2098

[LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525)

@ LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED

**Definition** lwm2m.h:2105

[LWM2M\_RD\_CLIENT\_EVENT\_NETWORK\_ERROR](group__lwm2m__api.md#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4)

@ LWM2M\_RD\_CLIENT\_EVENT\_NETWORK\_ERROR

**Definition** lwm2m.h:2106

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[lwm2m\_path.h](lwm2m__path_8h.md)

[mutex.h](mutex_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

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

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[coap\_pending](structcoap__pending.md)

Represents a request awaiting for an acknowledgment (ACK).

**Definition** coap.h:327

[coap\_reply](structcoap__reply.md)

Represents the handler for the reply of a request, it is also used when observing resources.

**Definition** coap.h:342

[lwm2m\_ctx](structlwm2m__ctx.md)

LwM2M context structure to maintain information for a single LwM2M connection.

**Definition** lwm2m.h:157

[lwm2m\_ctx::fault\_cb](structlwm2m__ctx.md#a1b90780926f3cda2d48dfa8f94b1efd8)

lwm2m\_socket\_fault\_cb\_t fault\_cb

Socket fault callback.

**Definition** lwm2m.h:253

[lwm2m\_ctx::desthostname](structlwm2m__ctx.md#a342cb5a0aaf9e5bc53228d3b0cc0fd43)

char \* desthostname

Destination hostname.

**Definition** lwm2m.h:196

[lwm2m\_ctx::hostname\_verify](structlwm2m__ctx.md#a380db99dd1930f29044a09876122c083)

bool hostname\_verify

Flag to indicate if hostname verification is enabled.

**Definition** lwm2m.h:200

[lwm2m\_ctx::observe\_cb](structlwm2m__ctx.md#a412bd706adcd17ec8c00f1779012a845)

lwm2m\_observe\_cb\_t observe\_cb

Callback for new or cancelled observations, and acknowledged or timed out notifications.

**Definition** lwm2m.h:258

[lwm2m\_ctx::remote\_addr](structlwm2m__ctx.md#a4ed594ecc5d442ffc2a604a879f5bfb7)

struct sockaddr remote\_addr

Destination address storage.

**Definition** lwm2m.h:159

[lwm2m\_ctx::validate\_buf](structlwm2m__ctx.md#a574b50b9ec4cdfb5fac53a9b6d8c31d5)

uint8\_t validate\_buf[CONFIG\_LWM2M\_ENGINE\_VALIDATION\_BUFFER\_SIZE]

Validation buffer.

**Definition** lwm2m.h:267

[lwm2m\_ctx::load\_credentials](structlwm2m__ctx.md#a5f17296cd4600b25515e0952dc61ea97)

int(\* load\_credentials)(struct lwm2m\_ctx \*client\_ctx)

Custom load\_credentials function.

**Definition** lwm2m.h:206

[lwm2m\_ctx::tls\_tag](structlwm2m__ctx.md#a6c4c9025a17a3dc3451651cb1f83d575)

int tls\_tag

TLS tag is set by client as a reference used when the LwM2M engine calls tls\_credential\_(add|delete).

**Definition** lwm2m.h:190

[lwm2m\_ctx::set\_socketoptions](structlwm2m__ctx.md#a746c578cf1d2c5eb606d0b592f419317)

int(\* set\_socketoptions)(struct lwm2m\_ctx \*client\_ctx)

Custom socket options.

**Definition** lwm2m.h:214

[lwm2m\_ctx::srv\_obj\_inst](structlwm2m__ctx.md#a76d92a14bf1729d7b0fee174c51ed4bf)

int srv\_obj\_inst

Current index of Server Object used in this context.

**Definition** lwm2m.h:240

[lwm2m\_ctx::processed\_req](structlwm2m__ctx.md#a9b56ad9b3f2202d25b8c48f34a898dd3)

void \* processed\_req

A pointer to currently processed request, for internal LwM2M engine use.

**Definition** lwm2m.h:178

[lwm2m\_ctx::bootstrap\_mode](structlwm2m__ctx.md#aafa787c2b7ea7599c51d9247ea9f1090)

bool bootstrap\_mode

Flag to enable BOOTSTRAP interface.

**Definition** lwm2m.h:245

[lwm2m\_ctx::event\_cb](structlwm2m__ctx.md#ab01ec6be0effa24dde31363a476eccbb)

lwm2m\_ctx\_event\_cb\_t event\_cb

Callback for client events.

**Definition** lwm2m.h:261

[lwm2m\_ctx::sec\_obj\_inst](structlwm2m__ctx.md#ab5fe85963a265f9c059a25138a637e02)

int sec\_obj\_inst

Current index of Security Object used for server credentials.

**Definition** lwm2m.h:237

[lwm2m\_ctx::buffer\_client\_messages](structlwm2m__ctx.md#ac6709d32a87ece72c7cdf283c4ff60c0)

bool buffer\_client\_messages

Flag to indicate that the client is buffering Notifications and Send messages.

**Definition** lwm2m.h:234

[lwm2m\_ctx::set\_socket\_state](structlwm2m__ctx.md#ad3d66164415325e7009d1a4c1111f4b3)

void(\* set\_socket\_state)(int fd, enum lwm2m\_socket\_states state)

Callback to indicate transmission states.

**Definition** lwm2m.h:275

[lwm2m\_ctx::use\_dtls](structlwm2m__ctx.md#aeb1e3ffc83853f74f2201f582917c2ce)

bool use\_dtls

Flag to indicate if context should use DTLS.

**Definition** lwm2m.h:221

[lwm2m\_ctx::sock\_fd](structlwm2m__ctx.md#afed1a599a72f131e4f196848c3e6fe85)

int sock\_fd

Socket File Descriptor.

**Definition** lwm2m.h:248

[lwm2m\_ctx::desthostnamelen](structlwm2m__ctx.md#aff084b28e547a81bd71215125c28f705)

uint16\_t desthostnamelen

Destination hostname length.

**Definition** lwm2m.h:198

[lwm2m\_ctx::connection\_suspended](structlwm2m__ctx.md#aff523bc7473073c917ff1c888da7bece)

bool connection\_suspended

Flag to indicate that the socket connection is suspended.

**Definition** lwm2m.h:227

[lwm2m\_obj\_path](structlwm2m__obj__path.md)

LwM2M object path structure.

**Definition** lwm2m.h:93

[lwm2m\_obj\_path::obj\_inst\_id](structlwm2m__obj__path.md#a7ae1a626b6f4b4c9cdc3e1a99d644ff2)

uint16\_t obj\_inst\_id

Object instance ID.

**Definition** lwm2m.h:95

[lwm2m\_obj\_path::res\_inst\_id](structlwm2m__obj__path.md#a924d75187c05b64989b6eed69b563c29)

uint16\_t res\_inst\_id

Resource instance ID.

**Definition** lwm2m.h:97

[lwm2m\_obj\_path::level](structlwm2m__obj__path.md#aaeb8482037aa5d9b389236eb9f3e2984)

uint8\_t level

Path level (0-4).

**Definition** lwm2m.h:98

[lwm2m\_obj\_path::res\_id](structlwm2m__obj__path.md#ac52cc68142a270b4bab8edfc7cb8b106)

uint16\_t res\_id

Resource ID.

**Definition** lwm2m.h:96

[lwm2m\_obj\_path::obj\_id](structlwm2m__obj__path.md#ad1cf2b4f67b059e92853a05e2d070bb7)

uint16\_t obj\_id

Object ID.

**Definition** lwm2m.h:94

[lwm2m\_objlnk](structlwm2m__objlnk.md)

LWM2M Objlnk resource type structure.

**Definition** lwm2m.h:731

[lwm2m\_objlnk::obj\_id](structlwm2m__objlnk.md#a67193c8612b3a3d2a6a9685f7d1a0053)

uint16\_t obj\_id

Object ID.

**Definition** lwm2m.h:732

[lwm2m\_objlnk::obj\_inst](structlwm2m__objlnk.md#aa51649798b00bc0bb9887c9739b83d27)

uint16\_t obj\_inst

Object instance ID.

**Definition** lwm2m.h:733

[lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md)

LwM2M Time series data structure.

**Definition** lwm2m.h:281

[lwm2m\_time\_series\_elem::i64](structlwm2m__time__series__elem.md#a2cccc464d029dc0f3f748b2a48f5cb50)

int64\_t i64

**Definition** lwm2m.h:292

[lwm2m\_time\_series\_elem::i16](structlwm2m__time__series__elem.md#a37489f6edbcb125691bd02f28346c788)

int16\_t i16

**Definition** lwm2m.h:290

[lwm2m\_time\_series\_elem::f](structlwm2m__time__series__elem.md#a3f25d66fa0e7918326a522e76451d6ae)

double f

**Definition** lwm2m.h:294

[lwm2m\_time\_series\_elem::u32](structlwm2m__time__series__elem.md#a58b1e7f9eb00d58421aec63bfbc732ed)

uint32\_t u32

**Definition** lwm2m.h:287

[lwm2m\_time\_series\_elem::i32](structlwm2m__time__series__elem.md#a61f4d65dd7e6e2e6b215fdc800bba6e4)

int32\_t i32

**Definition** lwm2m.h:291

[lwm2m\_time\_series\_elem::i8](structlwm2m__time__series__elem.md#ab895cd3addf57b8e59c8a1282588ee2d)

int8\_t i8

**Definition** lwm2m.h:289

[lwm2m\_time\_series\_elem::u8](structlwm2m__time__series__elem.md#abb0726f2ba23ab5f3229342d62f63e6b)

uint8\_t u8

**Definition** lwm2m.h:285

[lwm2m\_time\_series\_elem::t](structlwm2m__time__series__elem.md#acd00227c551b6ee1960b3881819ef90b)

time\_t t

Cached data Unix timestamp.

**Definition** lwm2m.h:283

[lwm2m\_time\_series\_elem::u16](structlwm2m__time__series__elem.md#ad0cd9f29ce0d7e99c1ae411bd89a29fa)

uint16\_t u16

**Definition** lwm2m.h:286

[lwm2m\_time\_series\_elem::u64](structlwm2m__time__series__elem.md#ae432e592ddceb17113f25bef77308f1b)

uint64\_t u64

**Definition** lwm2m.h:288

[lwm2m\_time\_series\_elem::b](structlwm2m__time__series__elem.md#ae6b37f532055bdd6b5b39c909a6873e7)

bool b

**Definition** lwm2m.h:295

[lwm2m\_time\_series\_elem::time](structlwm2m__time__series__elem.md#af25edfa95c28e43bb5abc60f3027ed9a)

time\_t time

**Definition** lwm2m.h:293

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [lwm2m.h](lwm2m_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
