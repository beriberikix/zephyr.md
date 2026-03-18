---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mqtt__sn_8h_source.html
original_path: doxygen/html/mqtt__sn_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_sn.h

[Go to the documentation of this file.](mqtt__sn_8h.md)

1/\*

2 \* Copyright (c) 2022 René Beckmann

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

19

20#ifndef ZEPHYR\_INCLUDE\_NET\_MQTT\_SN\_H\_

21#define ZEPHYR\_INCLUDE\_NET\_MQTT\_SN\_H\_

22

23#include <stddef.h>

24

25#include <[zephyr/net/buf.h](net_2buf_8h.md)>

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27

28#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

29

30#ifdef CONFIG\_MQTT\_SN\_TRANSPORT\_UDP

31#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

32#endif

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 42](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786)enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) {

[ 43](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389) [MQTT\_SN\_QOS\_0](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389),

[ 44](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da) [MQTT\_SN\_QOS\_1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da),

[ 45](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4) [MQTT\_SN\_QOS\_2](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4),

[ 46](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9) [MQTT\_SN\_QOS\_M1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9)

47};

48

[ 52](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd)enum [mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd) {

[ 57](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b) [MQTT\_SN\_TOPIC\_TYPE\_NORMAL](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b),

[ 64](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b) [MQTT\_SN\_TOPIC\_TYPE\_PREDEF](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b),

[ 69](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730) [MQTT\_SN\_TOPIC\_TYPE\_SHORT](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730)

70};

71

[ 75](group__mqtt__sn__socket.md#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)enum [mqtt\_sn\_return\_code](group__mqtt__sn__socket.md#gaab8c9d8ddbaa2af542fdcd3e4178ea9e) {

[ 76](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c) [MQTT\_SN\_CODE\_ACCEPTED](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c) = 0x00,

[ 77](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7) [MQTT\_SN\_CODE\_REJECTED\_CONGESTION](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7) = 0x01,

[ 78](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3) [MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3) = 0x02,

[ 79](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5) [MQTT\_SN\_CODE\_REJECTED\_NOTSUP](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5) = 0x03,

80};

81

[ 83](structmqtt__sn__data.md)struct [mqtt\_sn\_data](structmqtt__sn__data.md) {

[ 84](structmqtt__sn__data.md#ae3726684337ee8175224d11dfcf4a7c6) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structmqtt__sn__data.md#ae3726684337ee8175224d11dfcf4a7c6);

[ 85](structmqtt__sn__data.md#a7735f2459fa22fac2b7cf7a08dbee4a5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structmqtt__sn__data.md#a7735f2459fa22fac2b7cf7a08dbee4a5);

86};

87

[ 97](group__mqtt__sn__socket.md#gaf8223bf7e5548323c453b30be031e37e)#define MQTT\_SN\_DATA\_STRING\_LITERAL(literal) ((struct mqtt\_sn\_data){literal, sizeof(literal) - 1})

98

[ 106](group__mqtt__sn__socket.md#gabb58a0e4aa418a864f1208ff188f40bc)#define MQTT\_SN\_DATA\_BYTES(...) \

107 ((struct mqtt\_sn\_data) { (uint8\_t[]){ \_\_VA\_ARGS\_\_ }, sizeof((uint8\_t[]){ \_\_VA\_ARGS\_\_ })})

108

[ 112](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42)enum [mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42) {

[ 113](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6) [MQTT\_SN\_EVT\_CONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6),

[ 114](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf) [MQTT\_SN\_EVT\_DISCONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf),

[ 115](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f) [MQTT\_SN\_EVT\_ASLEEP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f),

[ 116](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd) [MQTT\_SN\_EVT\_AWAKE](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd),

[ 117](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf) [MQTT\_SN\_EVT\_PUBLISH](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf),

[ 118](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135) [MQTT\_SN\_EVT\_PINGRESP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)

119};

120

[ 124](unionmqtt__sn__evt__param.md)union [mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md) {

126 struct {

[ 128](unionmqtt__sn__evt__param.md#a2440375957dae427bb61526331052567) struct [mqtt\_sn\_data](structmqtt__sn__data.md) [data](unionmqtt__sn__evt__param.md#a2440375957dae427bb61526331052567);

[ 130](unionmqtt__sn__evt__param.md#ab7930bb48e91a24a79593e375f17cdf1) enum [mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd) [topic\_type](unionmqtt__sn__evt__param.md#ab7930bb48e91a24a79593e375f17cdf1);

[ 132](unionmqtt__sn__evt__param.md#ae79e9793f8fc70cc781c4527d8f8496d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [topic\_id](unionmqtt__sn__evt__param.md#ae79e9793f8fc70cc781c4527d8f8496d);

[ 133](unionmqtt__sn__evt__param.md#afa0ea7d03a7ffdc95c68848af4c9f3ae) } [publish](unionmqtt__sn__evt__param.md#afa0ea7d03a7ffdc95c68848af4c9f3ae);

134};

135

[ 139](structmqtt__sn__evt.md)struct [mqtt\_sn\_evt](structmqtt__sn__evt.md) {

[ 141](structmqtt__sn__evt.md#aef636c6acdc17831acb44095fbef1885) enum [mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42) [type](structmqtt__sn__evt.md#aef636c6acdc17831acb44095fbef1885);

[ 143](structmqtt__sn__evt.md#a8e75d71d1b38e1b84bf1ad20063ec4e8) union [mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md) [param](structmqtt__sn__evt.md#a8e75d71d1b38e1b84bf1ad20063ec4e8);

144};

145

146struct [mqtt\_sn\_client](structmqtt__sn__client.md);

147

[ 156](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a)typedef void (\*[mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a))(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_evt](structmqtt__sn__evt.md) \*evt);

157

[ 165](structmqtt__sn__transport.md)struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) {

[ 171](structmqtt__sn__transport.md#a3486cb5d56fb42db4c1f62ef9a6bb75b) int (\*[init](structmqtt__sn__transport.md#a3486cb5d56fb42db4c1f62ef9a6bb75b))(struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport);

172

[ 178](structmqtt__sn__transport.md#af51e433970bed12b5217c63416d0ec4c) void (\*[deinit](structmqtt__sn__transport.md#af51e433970bed12b5217c63416d0ec4c))(struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport);

179

[ 183](structmqtt__sn__transport.md#acbb05050af4c87d7fd3473a9d3fe74a1) int (\*[msg\_send](structmqtt__sn__transport.md#acbb05050af4c87d7fd3473a9d3fe74a1))(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, void \*buf, size\_t sz);

184

[ 190](structmqtt__sn__transport.md#a0f34a4ee28096c8db46db594e44efe98) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[recv](structmqtt__sn__transport.md#a0f34a4ee28096c8db46db594e44efe98))(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, void \*buffer, size\_t length);

191

[ 202](structmqtt__sn__transport.md#abe102ec52b34f767d0b231e93bedd0a9) int (\*[poll](structmqtt__sn__transport.md#abe102ec52b34f767d0b231e93bedd0a9))(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client);

203};

204

205#ifdef CONFIG\_MQTT\_SN\_TRANSPORT\_UDP

209struct mqtt\_sn\_transport\_udp {

211 struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) tp;

212

214 int sock;

215

217 struct [sockaddr](structsockaddr.md) gwaddr;

218 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) gwaddrlen;

219};

220

221#define UDP\_TRANSPORT(transport) CONTAINER\_OF(transport, struct mqtt\_sn\_transport\_udp, tp)

222

230int mqtt\_sn\_transport\_udp\_init(struct mqtt\_sn\_transport\_udp \*udp, struct [sockaddr](structsockaddr.md) \*gwaddr,

231 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

232#endif

233

[ 237](structmqtt__sn__client.md)struct [mqtt\_sn\_client](structmqtt__sn__client.md) {

[ 239](structmqtt__sn__client.md#a9cbf86052061b55a93356346cae75e8b) struct [mqtt\_sn\_data](structmqtt__sn__data.md) [client\_id](structmqtt__sn__client.md#a9cbf86052061b55a93356346cae75e8b);

240

[ 244](structmqtt__sn__client.md#af70196b9800123e2f9c36362cfb8b6be) struct [mqtt\_sn\_data](structmqtt__sn__data.md) [will\_topic](structmqtt__sn__client.md#af70196b9800123e2f9c36362cfb8b6be);

245

[ 249](structmqtt__sn__client.md#a9d2397f5ff59a51630f5b82f94c92327) struct [mqtt\_sn\_data](structmqtt__sn__data.md) [will\_msg](structmqtt__sn__client.md#a9d2397f5ff59a51630f5b82f94c92327);

250

[ 252](structmqtt__sn__client.md#a42d76db9cbcc9770246241283bb65486) enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) [will\_qos](structmqtt__sn__client.md#a42d76db9cbcc9770246241283bb65486);

253

[ 255](structmqtt__sn__client.md#ad8f5b3b7815033cfecda7519ca657724) bool [will\_retain](structmqtt__sn__client.md#ad8f5b3b7815033cfecda7519ca657724);

256

[ 258](structmqtt__sn__client.md#aec0d4d3f436d7c7d40e2548d7c6575c1) struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*[transport](structmqtt__sn__client.md#aec0d4d3f436d7c7d40e2548d7c6575c1);

259

[ 261](structmqtt__sn__client.md#a3802bd92a42e421a5d733c64b53473db) struct [net\_buf\_simple](structnet__buf__simple.md) [tx](structmqtt__sn__client.md#a3802bd92a42e421a5d733c64b53473db);

262

[ 264](structmqtt__sn__client.md#aec40ceeac5a4160b058ee6a7676ec68f) struct [net\_buf\_simple](structnet__buf__simple.md) [rx](structmqtt__sn__client.md#aec40ceeac5a4160b058ee6a7676ec68f);

265

[ 267](structmqtt__sn__client.md#ac2b8e9d7d4c246c5d5538922a1e9887b) [mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a) [evt\_cb](structmqtt__sn__client.md#ac2b8e9d7d4c246c5d5538922a1e9887b);

268

[ 270](structmqtt__sn__client.md#a05b83c732ed9199dac0110cfb1e56563) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [next\_msg\_id](structmqtt__sn__client.md#a05b83c732ed9199dac0110cfb1e56563);

271

[ 273](structmqtt__sn__client.md#a32efbccbf7b1820ff5092896130e6b7e) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [publish](structmqtt__sn__client.md#a32efbccbf7b1820ff5092896130e6b7e);

274

[ 276](structmqtt__sn__client.md#aa47e6426ca7e8434734377a85f586b84) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [topic](structmqtt__sn__client.md#aa47e6426ca7e8434734377a85f586b84);

277

[ 279](structmqtt__sn__client.md#a02a38427caa60c51f85661efe58813f6) int [state](structmqtt__sn__client.md#a02a38427caa60c51f85661efe58813f6);

280

[ 282](structmqtt__sn__client.md#af400a2f993c27e0f25a4325daeacee28) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [last\_ping](structmqtt__sn__client.md#af400a2f993c27e0f25a4325daeacee28);

283

[ 285](structmqtt__sn__client.md#a2be2f7d041f325dda14007864e03fb70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ping\_retries](structmqtt__sn__client.md#a2be2f7d041f325dda14007864e03fb70);

286

[ 288](structmqtt__sn__client.md#a65bb52c8a5ecbd81e743fdc7c213b43a) struct [k\_work\_delayable](structk__work__delayable.md) [process\_work](structmqtt__sn__client.md#a65bb52c8a5ecbd81e743fdc7c213b43a);

289};

290

[ 305](group__mqtt__sn__socket.md#gae6a3f7a7762653474df97364ef69fc74)int [mqtt\_sn\_client\_init](group__mqtt__sn__socket.md#gae6a3f7a7762653474df97364ef69fc74)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*client\_id,

306 struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport, [mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a) evt\_cb, void \*tx,

307 size\_t txsz, void \*rx, size\_t rxsz);

308

[ 316](group__mqtt__sn__socket.md#ga67d69e4e3f00b31b5ea3b37fb6d653b1)void [mqtt\_sn\_client\_deinit](group__mqtt__sn__socket.md#ga67d69e4e3f00b31b5ea3b37fb6d653b1)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client);

317

[ 327](group__mqtt__sn__socket.md#ga8c2a525f1c30e5d5ff37180d33a76d4d)int [mqtt\_sn\_connect](group__mqtt__sn__socket.md#ga8c2a525f1c30e5d5ff37180d33a76d4d)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, bool will, bool clean\_session);

328

[ 336](group__mqtt__sn__socket.md#gab9cba16f8ce06f606ee81e0d34deb862)int [mqtt\_sn\_disconnect](group__mqtt__sn__socket.md#gab9cba16f8ce06f606ee81e0d34deb862)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client);

337

[ 346](group__mqtt__sn__socket.md#gaf29a6339419ea02052fe53a18bb8e5ee)int [mqtt\_sn\_sleep](group__mqtt__sn__socket.md#gaf29a6339419ea02052fe53a18bb8e5ee)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration);

347

[ 357](group__mqtt__sn__socket.md#ga9b481db6d39dee05e2c58d4c721fe0a5)int [mqtt\_sn\_subscribe](group__mqtt__sn__socket.md#ga9b481db6d39dee05e2c58d4c721fe0a5)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos,

358 struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name);

359

[ 369](group__mqtt__sn__socket.md#ga1bcd2a0f52610708bebb4b3b6d6cbf35)int [mqtt\_sn\_unsubscribe](group__mqtt__sn__socket.md#ga1bcd2a0f52610708bebb4b3b6d6cbf35)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos,

370 struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name);

371

[ 385](group__mqtt__sn__socket.md#ga434c3626ceaf3a9b60c5ffb75e9b5b56)int [mqtt\_sn\_publish](group__mqtt__sn__socket.md#ga434c3626ceaf3a9b60c5ffb75e9b5b56)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos,

386 struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name, bool retain, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*data);

387

[ 398](group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49)int [mqtt\_sn\_input](group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client);

399

[ 410](group__mqtt__sn__socket.md#gade962a4da5311a403893ba24714dc332)int [mqtt\_sn\_get\_topic\_name](group__mqtt__sn__socket.md#gade962a4da5311a403893ba24714dc332)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

411 struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name);

412

413#ifdef \_\_cplusplus

414}

415#endif

416

417#endif /\* ZEPHYR\_INCLUDE\_NET\_MQTT\_SN\_H\_ \*/

418

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[mqtt\_sn\_unsubscribe](group__mqtt__sn__socket.md#ga1bcd2a0f52610708bebb4b3b6d6cbf35)

int mqtt\_sn\_unsubscribe(struct mqtt\_sn\_client \*client, enum mqtt\_sn\_qos qos, struct mqtt\_sn\_data \*topic\_name)

Unsubscribe from a topic.

[mqtt\_sn\_publish](group__mqtt__sn__socket.md#ga434c3626ceaf3a9b60c5ffb75e9b5b56)

int mqtt\_sn\_publish(struct mqtt\_sn\_client \*client, enum mqtt\_sn\_qos qos, struct mqtt\_sn\_data \*topic\_name, bool retain, struct mqtt\_sn\_data \*data)

Publish a value.

[mqtt\_sn\_client\_deinit](group__mqtt__sn__socket.md#ga67d69e4e3f00b31b5ea3b37fb6d653b1)

void mqtt\_sn\_client\_deinit(struct mqtt\_sn\_client \*client)

Deinitialize the client.

[mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786)

mqtt\_sn\_qos

Quality of Service.

**Definition** mqtt\_sn.h:42

[mqtt\_sn\_connect](group__mqtt__sn__socket.md#ga8c2a525f1c30e5d5ff37180d33a76d4d)

int mqtt\_sn\_connect(struct mqtt\_sn\_client \*client, bool will, bool clean\_session)

Connect the client.

[mqtt\_sn\_subscribe](group__mqtt__sn__socket.md#ga9b481db6d39dee05e2c58d4c721fe0a5)

int mqtt\_sn\_subscribe(struct mqtt\_sn\_client \*client, enum mqtt\_sn\_qos qos, struct mqtt\_sn\_data \*topic\_name)

Subscribe to a given topic.

[mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42)

mqtt\_sn\_evt\_type

Event types that can be emitted by the library.

**Definition** mqtt\_sn.h:112

[mqtt\_sn\_return\_code](group__mqtt__sn__socket.md#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)

mqtt\_sn\_return\_code

MQTT-SN return codes.

**Definition** mqtt\_sn.h:75

[mqtt\_sn\_disconnect](group__mqtt__sn__socket.md#gab9cba16f8ce06f606ee81e0d34deb862)

int mqtt\_sn\_disconnect(struct mqtt\_sn\_client \*client)

Disconnect the client.

[mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd)

mqtt\_sn\_topic\_type

MQTT-SN topic types.

**Definition** mqtt\_sn.h:52

[mqtt\_sn\_get\_topic\_name](group__mqtt__sn__socket.md#gade962a4da5311a403893ba24714dc332)

int mqtt\_sn\_get\_topic\_name(struct mqtt\_sn\_client \*client, uint16\_t id, struct mqtt\_sn\_data \*topic\_name)

Get topic name by topic ID.

[mqtt\_sn\_client\_init](group__mqtt__sn__socket.md#gae6a3f7a7762653474df97364ef69fc74)

int mqtt\_sn\_client\_init(struct mqtt\_sn\_client \*client, const struct mqtt\_sn\_data \*client\_id, struct mqtt\_sn\_transport \*transport, mqtt\_sn\_evt\_cb\_t evt\_cb, void \*tx, size\_t txsz, void \*rx, size\_t rxsz)

Initialize a client.

[mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a)

void(\* mqtt\_sn\_evt\_cb\_t)(struct mqtt\_sn\_client \*client, const struct mqtt\_sn\_evt \*evt)

Asynchronous event notification callback registered by the application.

**Definition** mqtt\_sn.h:156

[mqtt\_sn\_sleep](group__mqtt__sn__socket.md#gaf29a6339419ea02052fe53a18bb8e5ee)

int mqtt\_sn\_sleep(struct mqtt\_sn\_client \*client, uint16\_t duration)

Set the client into sleep state.

[mqtt\_sn\_input](group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49)

int mqtt\_sn\_input(struct mqtt\_sn\_client \*client)

Check the transport for new incoming data.

[MQTT\_SN\_QOS\_M1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9)

@ MQTT\_SN\_QOS\_M1

QOS -1.

**Definition** mqtt\_sn.h:46

[MQTT\_SN\_QOS\_2](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4)

@ MQTT\_SN\_QOS\_2

QOS 2.

**Definition** mqtt\_sn.h:45

[MQTT\_SN\_QOS\_1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da)

@ MQTT\_SN\_QOS\_1

QOS 1.

**Definition** mqtt\_sn.h:44

[MQTT\_SN\_QOS\_0](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389)

@ MQTT\_SN\_QOS\_0

QOS 0.

**Definition** mqtt\_sn.h:43

[MQTT\_SN\_EVT\_PINGRESP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)

@ MQTT\_SN\_EVT\_PINGRESP

Received a PINGRESP.

**Definition** mqtt\_sn.h:118

[MQTT\_SN\_EVT\_CONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6)

@ MQTT\_SN\_EVT\_CONNECTED

Connected to a gateway.

**Definition** mqtt\_sn.h:113

[MQTT\_SN\_EVT\_PUBLISH](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf)

@ MQTT\_SN\_EVT\_PUBLISH

Received a PUBLISH message.

**Definition** mqtt\_sn.h:117

[MQTT\_SN\_EVT\_ASLEEP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f)

@ MQTT\_SN\_EVT\_ASLEEP

Entered ASLEEP state.

**Definition** mqtt\_sn.h:115

[MQTT\_SN\_EVT\_DISCONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf)

@ MQTT\_SN\_EVT\_DISCONNECTED

Disconnected.

**Definition** mqtt\_sn.h:114

[MQTT\_SN\_EVT\_AWAKE](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd)

@ MQTT\_SN\_EVT\_AWAKE

Entered AWAKE state.

**Definition** mqtt\_sn.h:116

[MQTT\_SN\_CODE\_ACCEPTED](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c)

@ MQTT\_SN\_CODE\_ACCEPTED

Accepted.

**Definition** mqtt\_sn.h:76

[MQTT\_SN\_CODE\_REJECTED\_CONGESTION](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7)

@ MQTT\_SN\_CODE\_REJECTED\_CONGESTION

Rejected: congestion.

**Definition** mqtt\_sn.h:77

[MQTT\_SN\_CODE\_REJECTED\_NOTSUP](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5)

@ MQTT\_SN\_CODE\_REJECTED\_NOTSUP

Rejected: Not Supported.

**Definition** mqtt\_sn.h:79

[MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3)

@ MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID

Rejected: Invalid Topic ID.

**Definition** mqtt\_sn.h:78

[MQTT\_SN\_TOPIC\_TYPE\_NORMAL](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b)

@ MQTT\_SN\_TOPIC\_TYPE\_NORMAL

Normal topic.

**Definition** mqtt\_sn.h:57

[MQTT\_SN\_TOPIC\_TYPE\_PREDEF](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b)

@ MQTT\_SN\_TOPIC\_TYPE\_PREDEF

Pre-defined topic.

**Definition** mqtt\_sn.h:64

[MQTT\_SN\_TOPIC\_TYPE\_SHORT](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730)

@ MQTT\_SN\_TOPIC\_TYPE\_SHORT

Short topic.

**Definition** mqtt\_sn.h:69

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[buf.h](net_2buf_8h.md)

Buffer management.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3908

[mqtt\_sn\_client](structmqtt__sn__client.md)

Structure describing an MQTT-SN client.

**Definition** mqtt\_sn.h:237

[mqtt\_sn\_client::state](structmqtt__sn__client.md#a02a38427caa60c51f85661efe58813f6)

int state

Current state of the MQTT-SN client.

**Definition** mqtt\_sn.h:279

[mqtt\_sn\_client::next\_msg\_id](structmqtt__sn__client.md#a05b83c732ed9199dac0110cfb1e56563)

uint16\_t next\_msg\_id

Message ID for the next message to be sent.

**Definition** mqtt\_sn.h:270

[mqtt\_sn\_client::ping\_retries](structmqtt__sn__client.md#a2be2f7d041f325dda14007864e03fb70)

uint8\_t ping\_retries

Number of retries for failed ping attempts.

**Definition** mqtt\_sn.h:285

[mqtt\_sn\_client::publish](structmqtt__sn__client.md#a32efbccbf7b1820ff5092896130e6b7e)

sys\_slist\_t publish

List of pending publish messages.

**Definition** mqtt\_sn.h:273

[mqtt\_sn\_client::tx](structmqtt__sn__client.md#a3802bd92a42e421a5d733c64b53473db)

struct net\_buf\_simple tx

Buffer for outgoing data.

**Definition** mqtt\_sn.h:261

[mqtt\_sn\_client::will\_qos](structmqtt__sn__client.md#a42d76db9cbcc9770246241283bb65486)

enum mqtt\_sn\_qos will\_qos

Quality of Service for the Will message.

**Definition** mqtt\_sn.h:252

[mqtt\_sn\_client::process\_work](structmqtt__sn__client.md#a65bb52c8a5ecbd81e743fdc7c213b43a)

struct k\_work\_delayable process\_work

Delayable work structure for processing MQTT-SN events.

**Definition** mqtt\_sn.h:288

[mqtt\_sn\_client::client\_id](structmqtt__sn__client.md#a9cbf86052061b55a93356346cae75e8b)

struct mqtt\_sn\_data client\_id

1-23 character unique client ID

**Definition** mqtt\_sn.h:239

[mqtt\_sn\_client::will\_msg](structmqtt__sn__client.md#a9d2397f5ff59a51630f5b82f94c92327)

struct mqtt\_sn\_data will\_msg

Will message.

**Definition** mqtt\_sn.h:249

[mqtt\_sn\_client::topic](structmqtt__sn__client.md#aa47e6426ca7e8434734377a85f586b84)

sys\_slist\_t topic

List of registered topics.

**Definition** mqtt\_sn.h:276

[mqtt\_sn\_client::evt\_cb](structmqtt__sn__client.md#ac2b8e9d7d4c246c5d5538922a1e9887b)

mqtt\_sn\_evt\_cb\_t evt\_cb

Event callback.

**Definition** mqtt\_sn.h:267

[mqtt\_sn\_client::will\_retain](structmqtt__sn__client.md#ad8f5b3b7815033cfecda7519ca657724)

bool will\_retain

Flag indicating if the will message should be retained by the broker.

**Definition** mqtt\_sn.h:255

[mqtt\_sn\_client::transport](structmqtt__sn__client.md#aec0d4d3f436d7c7d40e2548d7c6575c1)

struct mqtt\_sn\_transport \* transport

Underlying transport to be used by the client.

**Definition** mqtt\_sn.h:258

[mqtt\_sn\_client::rx](structmqtt__sn__client.md#aec40ceeac5a4160b058ee6a7676ec68f)

struct net\_buf\_simple rx

Buffer for incoming data.

**Definition** mqtt\_sn.h:264

[mqtt\_sn\_client::last\_ping](structmqtt__sn__client.md#af400a2f993c27e0f25a4325daeacee28)

int64\_t last\_ping

Timestamp of the last ping request.

**Definition** mqtt\_sn.h:282

[mqtt\_sn\_client::will\_topic](structmqtt__sn__client.md#af70196b9800123e2f9c36362cfb8b6be)

struct mqtt\_sn\_data will\_topic

Topic for Will message.

**Definition** mqtt\_sn.h:244

[mqtt\_sn\_data](structmqtt__sn__data.md)

Abstracts memory buffers.

**Definition** mqtt\_sn.h:83

[mqtt\_sn\_data::size](structmqtt__sn__data.md#a7735f2459fa22fac2b7cf7a08dbee4a5)

uint16\_t size

Size of data, in bytes.

**Definition** mqtt\_sn.h:85

[mqtt\_sn\_data::data](structmqtt__sn__data.md#ae3726684337ee8175224d11dfcf4a7c6)

const uint8\_t \* data

Pointer to data.

**Definition** mqtt\_sn.h:84

[mqtt\_sn\_evt](structmqtt__sn__evt.md)

MQTT-SN event structure to be handled by the event callback.

**Definition** mqtt\_sn.h:139

[mqtt\_sn\_evt::param](structmqtt__sn__evt.md#a8e75d71d1b38e1b84bf1ad20063ec4e8)

union mqtt\_sn\_evt\_param param

Event parameters.

**Definition** mqtt\_sn.h:143

[mqtt\_sn\_evt::type](structmqtt__sn__evt.md#aef636c6acdc17831acb44095fbef1885)

enum mqtt\_sn\_evt\_type type

Event type.

**Definition** mqtt\_sn.h:141

[mqtt\_sn\_transport](structmqtt__sn__transport.md)

Structure to describe an MQTT-SN transport.

**Definition** mqtt\_sn.h:165

[mqtt\_sn\_transport::recv](structmqtt__sn__transport.md#a0f34a4ee28096c8db46db594e44efe98)

ssize\_t(\* recv)(struct mqtt\_sn\_client \*client, void \*buffer, size\_t length)

Will be called by the library when it wants to receive a message.

**Definition** mqtt\_sn.h:190

[mqtt\_sn\_transport::init](structmqtt__sn__transport.md#a3486cb5d56fb42db4c1f62ef9a6bb75b)

int(\* init)(struct mqtt\_sn\_transport \*transport)

Will be called once on client init to initialize the transport.

**Definition** mqtt\_sn.h:171

[mqtt\_sn\_transport::poll](structmqtt__sn__transport.md#abe102ec52b34f767d0b231e93bedd0a9)

int(\* poll)(struct mqtt\_sn\_client \*client)

Check if incoming data is available.

**Definition** mqtt\_sn.h:202

[mqtt\_sn\_transport::msg\_send](structmqtt__sn__transport.md#acbb05050af4c87d7fd3473a9d3fe74a1)

int(\* msg\_send)(struct mqtt\_sn\_client \*client, void \*buf, size\_t sz)

Will be called by the library when it wants to send a message.

**Definition** mqtt\_sn.h:183

[mqtt\_sn\_transport::deinit](structmqtt__sn__transport.md#af51e433970bed12b5217c63416d0ec4c)

void(\* deinit)(struct mqtt\_sn\_transport \*transport)

Will be called on client deinit.

**Definition** mqtt\_sn.h:178

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

[mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md)

Event metadata.

**Definition** mqtt\_sn.h:124

[mqtt\_sn\_evt\_param::data](unionmqtt__sn__evt__param.md#a2440375957dae427bb61526331052567)

struct mqtt\_sn\_data data

The payload data associated with the event.

**Definition** mqtt\_sn.h:128

[mqtt\_sn\_evt\_param::topic\_type](unionmqtt__sn__evt__param.md#ab7930bb48e91a24a79593e375f17cdf1)

enum mqtt\_sn\_topic\_type topic\_type

The type of topic for the event.

**Definition** mqtt\_sn.h:130

[mqtt\_sn\_evt\_param::topic\_id](unionmqtt__sn__evt__param.md#ae79e9793f8fc70cc781c4527d8f8496d)

uint16\_t topic\_id

The identifier for the topic of the event.

**Definition** mqtt\_sn.h:132

[mqtt\_sn\_evt\_param::publish](unionmqtt__sn__evt__param.md#afa0ea7d03a7ffdc95c68848af4c9f3ae)

struct mqtt\_sn\_evt\_param::@275266202006044005055345147344370221371361315200 publish

Structure holding publish event details.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mqtt\_sn.h](mqtt__sn_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
