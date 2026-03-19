---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mqtt__sn_8h_source.html
original_path: doxygen/html/mqtt__sn_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

21

22#ifndef ZEPHYR\_INCLUDE\_NET\_MQTT\_SN\_H\_

23#define ZEPHYR\_INCLUDE\_NET\_MQTT\_SN\_H\_

24

25#include <stddef.h>

26

27#include <[zephyr/net\_buf.h](net__buf_8h.md)>

28#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

29

30#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

31

32#ifdef CONFIG\_MQTT\_SN\_TRANSPORT\_UDP

33#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

34#endif

35

36#ifdef \_\_cplusplus

37extern "C" {

38#endif

39

[ 44](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786)enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) {

[ 45](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389) [MQTT\_SN\_QOS\_0](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389),

[ 46](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da) [MQTT\_SN\_QOS\_1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da),

[ 47](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4) [MQTT\_SN\_QOS\_2](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4),

[ 48](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9) [MQTT\_SN\_QOS\_M1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9)

49};

50

[ 54](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd)enum [mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd) {

[ 59](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b) [MQTT\_SN\_TOPIC\_TYPE\_NORMAL](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b),

[ 66](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b) [MQTT\_SN\_TOPIC\_TYPE\_PREDEF](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b),

[ 71](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730) [MQTT\_SN\_TOPIC\_TYPE\_SHORT](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730)

72};

73

[ 77](group__mqtt__sn__socket.md#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)enum [mqtt\_sn\_return\_code](group__mqtt__sn__socket.md#gaab8c9d8ddbaa2af542fdcd3e4178ea9e) {

[ 78](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c) [MQTT\_SN\_CODE\_ACCEPTED](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c) = 0x00,

[ 79](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7) [MQTT\_SN\_CODE\_REJECTED\_CONGESTION](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7) = 0x01,

[ 80](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3) [MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3) = 0x02,

[ 81](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5) [MQTT\_SN\_CODE\_REJECTED\_NOTSUP](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5) = 0x03,

82};

83

[ 85](structmqtt__sn__data.md)struct [mqtt\_sn\_data](structmqtt__sn__data.md) {

[ 86](structmqtt__sn__data.md#ae3726684337ee8175224d11dfcf4a7c6) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structmqtt__sn__data.md#ae3726684337ee8175224d11dfcf4a7c6);

[ 87](structmqtt__sn__data.md#a7735f2459fa22fac2b7cf7a08dbee4a5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structmqtt__sn__data.md#a7735f2459fa22fac2b7cf7a08dbee4a5);

88};

89

[ 99](group__mqtt__sn__socket.md#gaf8223bf7e5548323c453b30be031e37e)#define MQTT\_SN\_DATA\_STRING\_LITERAL(literal) ((struct mqtt\_sn\_data){literal, sizeof(literal) - 1})

100

[ 108](group__mqtt__sn__socket.md#gabb58a0e4aa418a864f1208ff188f40bc)#define MQTT\_SN\_DATA\_BYTES(...) \

109 ((struct mqtt\_sn\_data) { (uint8\_t[]){ \_\_VA\_ARGS\_\_ }, sizeof((uint8\_t[]){ \_\_VA\_ARGS\_\_ })})

110

[ 114](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42)enum [mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42) {

[ 115](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6) [MQTT\_SN\_EVT\_CONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6),

[ 116](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf) [MQTT\_SN\_EVT\_DISCONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf),

[ 117](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f) [MQTT\_SN\_EVT\_ASLEEP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f),

[ 118](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd) [MQTT\_SN\_EVT\_AWAKE](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd),

[ 119](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf) [MQTT\_SN\_EVT\_PUBLISH](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf),

[ 120](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135) [MQTT\_SN\_EVT\_PINGRESP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)

121};

122

[ 126](unionmqtt__sn__evt__param.md)union [mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md) {

128 struct {

[ 130](unionmqtt__sn__evt__param.md#a2440375957dae427bb61526331052567) struct [mqtt\_sn\_data](structmqtt__sn__data.md) [data](unionmqtt__sn__evt__param.md#a2440375957dae427bb61526331052567);

[ 132](unionmqtt__sn__evt__param.md#ab7930bb48e91a24a79593e375f17cdf1) enum [mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd) [topic\_type](unionmqtt__sn__evt__param.md#ab7930bb48e91a24a79593e375f17cdf1);

[ 134](unionmqtt__sn__evt__param.md#ae79e9793f8fc70cc781c4527d8f8496d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [topic\_id](unionmqtt__sn__evt__param.md#ae79e9793f8fc70cc781c4527d8f8496d);

[ 135](unionmqtt__sn__evt__param.md#afa0ea7d03a7ffdc95c68848af4c9f3ae) } [publish](unionmqtt__sn__evt__param.md#afa0ea7d03a7ffdc95c68848af4c9f3ae);

136};

137

[ 141](structmqtt__sn__evt.md)struct [mqtt\_sn\_evt](structmqtt__sn__evt.md) {

[ 143](structmqtt__sn__evt.md#aef636c6acdc17831acb44095fbef1885) enum [mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42) [type](structmqtt__sn__evt.md#aef636c6acdc17831acb44095fbef1885);

[ 145](structmqtt__sn__evt.md#a8e75d71d1b38e1b84bf1ad20063ec4e8) union [mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md) [param](structmqtt__sn__evt.md#a8e75d71d1b38e1b84bf1ad20063ec4e8);

146};

147

148struct [mqtt\_sn\_client](structmqtt__sn__client.md);

149

[ 158](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a)typedef void (\*[mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a))(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_evt](structmqtt__sn__evt.md) \*evt);

159

[ 167](structmqtt__sn__transport.md)struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) {

[ 173](structmqtt__sn__transport.md#a3486cb5d56fb42db4c1f62ef9a6bb75b) int (\*[init](structmqtt__sn__transport.md#a3486cb5d56fb42db4c1f62ef9a6bb75b))(struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport);

174

[ 180](structmqtt__sn__transport.md#af51e433970bed12b5217c63416d0ec4c) void (\*[deinit](structmqtt__sn__transport.md#af51e433970bed12b5217c63416d0ec4c))(struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport);

181

[ 185](structmqtt__sn__transport.md#acbb05050af4c87d7fd3473a9d3fe74a1) int (\*[msg\_send](structmqtt__sn__transport.md#acbb05050af4c87d7fd3473a9d3fe74a1))(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, void \*buf, size\_t sz);

186

[ 192](structmqtt__sn__transport.md#a0f34a4ee28096c8db46db594e44efe98) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[recv](structmqtt__sn__transport.md#a0f34a4ee28096c8db46db594e44efe98))(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, void \*buffer, size\_t length);

193

[ 204](structmqtt__sn__transport.md#abe102ec52b34f767d0b231e93bedd0a9) int (\*[poll](structmqtt__sn__transport.md#abe102ec52b34f767d0b231e93bedd0a9))(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client);

205};

206

207#ifdef CONFIG\_MQTT\_SN\_TRANSPORT\_UDP

211struct mqtt\_sn\_transport\_udp {

213 struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) tp;

214

216 int sock;

217

219 struct [sockaddr](structsockaddr.md) gwaddr;

220 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) gwaddrlen;

221};

222

223#define UDP\_TRANSPORT(transport) CONTAINER\_OF(transport, struct mqtt\_sn\_transport\_udp, tp)

224

232int mqtt\_sn\_transport\_udp\_init(struct mqtt\_sn\_transport\_udp \*udp, struct [sockaddr](structsockaddr.md) \*gwaddr,

233 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

234#endif

235

[ 239](structmqtt__sn__client.md)struct [mqtt\_sn\_client](structmqtt__sn__client.md) {

[ 241](structmqtt__sn__client.md#a9cbf86052061b55a93356346cae75e8b) struct [mqtt\_sn\_data](structmqtt__sn__data.md) [client\_id](structmqtt__sn__client.md#a9cbf86052061b55a93356346cae75e8b);

242

[ 246](structmqtt__sn__client.md#af70196b9800123e2f9c36362cfb8b6be) struct [mqtt\_sn\_data](structmqtt__sn__data.md) [will\_topic](structmqtt__sn__client.md#af70196b9800123e2f9c36362cfb8b6be);

247

[ 251](structmqtt__sn__client.md#a9d2397f5ff59a51630f5b82f94c92327) struct [mqtt\_sn\_data](structmqtt__sn__data.md) [will\_msg](structmqtt__sn__client.md#a9d2397f5ff59a51630f5b82f94c92327);

252

[ 254](structmqtt__sn__client.md#a42d76db9cbcc9770246241283bb65486) enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) [will\_qos](structmqtt__sn__client.md#a42d76db9cbcc9770246241283bb65486);

255

[ 257](structmqtt__sn__client.md#ad8f5b3b7815033cfecda7519ca657724) bool [will\_retain](structmqtt__sn__client.md#ad8f5b3b7815033cfecda7519ca657724);

258

[ 260](structmqtt__sn__client.md#aec0d4d3f436d7c7d40e2548d7c6575c1) struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*[transport](structmqtt__sn__client.md#aec0d4d3f436d7c7d40e2548d7c6575c1);

261

[ 263](structmqtt__sn__client.md#a3802bd92a42e421a5d733c64b53473db) struct [net\_buf\_simple](structnet__buf__simple.md) [tx](structmqtt__sn__client.md#a3802bd92a42e421a5d733c64b53473db);

264

[ 266](structmqtt__sn__client.md#aec40ceeac5a4160b058ee6a7676ec68f) struct [net\_buf\_simple](structnet__buf__simple.md) [rx](structmqtt__sn__client.md#aec40ceeac5a4160b058ee6a7676ec68f);

267

[ 269](structmqtt__sn__client.md#ac2b8e9d7d4c246c5d5538922a1e9887b) [mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a) [evt\_cb](structmqtt__sn__client.md#ac2b8e9d7d4c246c5d5538922a1e9887b);

270

[ 272](structmqtt__sn__client.md#a05b83c732ed9199dac0110cfb1e56563) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [next\_msg\_id](structmqtt__sn__client.md#a05b83c732ed9199dac0110cfb1e56563);

273

[ 275](structmqtt__sn__client.md#a32efbccbf7b1820ff5092896130e6b7e) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [publish](structmqtt__sn__client.md#a32efbccbf7b1820ff5092896130e6b7e);

276

[ 278](structmqtt__sn__client.md#aa47e6426ca7e8434734377a85f586b84) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [topic](structmqtt__sn__client.md#aa47e6426ca7e8434734377a85f586b84);

279

[ 281](structmqtt__sn__client.md#a02a38427caa60c51f85661efe58813f6) int [state](structmqtt__sn__client.md#a02a38427caa60c51f85661efe58813f6);

282

[ 284](structmqtt__sn__client.md#af400a2f993c27e0f25a4325daeacee28) [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [last\_ping](structmqtt__sn__client.md#af400a2f993c27e0f25a4325daeacee28);

285

[ 287](structmqtt__sn__client.md#a2be2f7d041f325dda14007864e03fb70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ping\_retries](structmqtt__sn__client.md#a2be2f7d041f325dda14007864e03fb70);

288

[ 290](structmqtt__sn__client.md#a65bb52c8a5ecbd81e743fdc7c213b43a) struct [k\_work\_delayable](structk__work__delayable.md) [process\_work](structmqtt__sn__client.md#a65bb52c8a5ecbd81e743fdc7c213b43a);

291};

292

[ 307](group__mqtt__sn__socket.md#gae6a3f7a7762653474df97364ef69fc74)int [mqtt\_sn\_client\_init](group__mqtt__sn__socket.md#gae6a3f7a7762653474df97364ef69fc74)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*client\_id,

308 struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport, [mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a) evt\_cb, void \*tx,

309 size\_t txsz, void \*rx, size\_t rxsz);

310

[ 318](group__mqtt__sn__socket.md#ga67d69e4e3f00b31b5ea3b37fb6d653b1)void [mqtt\_sn\_client\_deinit](group__mqtt__sn__socket.md#ga67d69e4e3f00b31b5ea3b37fb6d653b1)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client);

319

[ 329](group__mqtt__sn__socket.md#ga8c2a525f1c30e5d5ff37180d33a76d4d)int [mqtt\_sn\_connect](group__mqtt__sn__socket.md#ga8c2a525f1c30e5d5ff37180d33a76d4d)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, bool will, bool clean\_session);

330

[ 338](group__mqtt__sn__socket.md#gab9cba16f8ce06f606ee81e0d34deb862)int [mqtt\_sn\_disconnect](group__mqtt__sn__socket.md#gab9cba16f8ce06f606ee81e0d34deb862)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client);

339

[ 348](group__mqtt__sn__socket.md#gaf29a6339419ea02052fe53a18bb8e5ee)int [mqtt\_sn\_sleep](group__mqtt__sn__socket.md#gaf29a6339419ea02052fe53a18bb8e5ee)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration);

349

[ 359](group__mqtt__sn__socket.md#ga9b481db6d39dee05e2c58d4c721fe0a5)int [mqtt\_sn\_subscribe](group__mqtt__sn__socket.md#ga9b481db6d39dee05e2c58d4c721fe0a5)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos,

360 struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name);

361

[ 371](group__mqtt__sn__socket.md#ga1bcd2a0f52610708bebb4b3b6d6cbf35)int [mqtt\_sn\_unsubscribe](group__mqtt__sn__socket.md#ga1bcd2a0f52610708bebb4b3b6d6cbf35)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos,

372 struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name);

373

[ 387](group__mqtt__sn__socket.md#ga434c3626ceaf3a9b60c5ffb75e9b5b56)int [mqtt\_sn\_publish](group__mqtt__sn__socket.md#ga434c3626ceaf3a9b60c5ffb75e9b5b56)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos,

388 struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name, bool retain, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*data);

389

[ 400](group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49)int [mqtt\_sn\_input](group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client);

401

[ 412](group__mqtt__sn__socket.md#gade962a4da5311a403893ba24714dc332)int [mqtt\_sn\_get\_topic\_name](group__mqtt__sn__socket.md#gade962a4da5311a403893ba24714dc332)(struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id,

413 struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name);

414

415#ifdef \_\_cplusplus

416}

417#endif

418

419#endif /\* ZEPHYR\_INCLUDE\_NET\_MQTT\_SN\_H\_ \*/

420

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:171

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

**Definition** mqtt\_sn.h:44

[mqtt\_sn\_connect](group__mqtt__sn__socket.md#ga8c2a525f1c30e5d5ff37180d33a76d4d)

int mqtt\_sn\_connect(struct mqtt\_sn\_client \*client, bool will, bool clean\_session)

Connect the client.

[mqtt\_sn\_subscribe](group__mqtt__sn__socket.md#ga9b481db6d39dee05e2c58d4c721fe0a5)

int mqtt\_sn\_subscribe(struct mqtt\_sn\_client \*client, enum mqtt\_sn\_qos qos, struct mqtt\_sn\_data \*topic\_name)

Subscribe to a given topic.

[mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42)

mqtt\_sn\_evt\_type

Event types that can be emitted by the library.

**Definition** mqtt\_sn.h:114

[mqtt\_sn\_return\_code](group__mqtt__sn__socket.md#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)

mqtt\_sn\_return\_code

MQTT-SN return codes.

**Definition** mqtt\_sn.h:77

[mqtt\_sn\_disconnect](group__mqtt__sn__socket.md#gab9cba16f8ce06f606ee81e0d34deb862)

int mqtt\_sn\_disconnect(struct mqtt\_sn\_client \*client)

Disconnect the client.

[mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd)

mqtt\_sn\_topic\_type

MQTT-SN topic types.

**Definition** mqtt\_sn.h:54

[mqtt\_sn\_get\_topic\_name](group__mqtt__sn__socket.md#gade962a4da5311a403893ba24714dc332)

int mqtt\_sn\_get\_topic\_name(struct mqtt\_sn\_client \*client, uint16\_t id, struct mqtt\_sn\_data \*topic\_name)

Get topic name by topic ID.

[mqtt\_sn\_client\_init](group__mqtt__sn__socket.md#gae6a3f7a7762653474df97364ef69fc74)

int mqtt\_sn\_client\_init(struct mqtt\_sn\_client \*client, const struct mqtt\_sn\_data \*client\_id, struct mqtt\_sn\_transport \*transport, mqtt\_sn\_evt\_cb\_t evt\_cb, void \*tx, size\_t txsz, void \*rx, size\_t rxsz)

Initialize a client.

[mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a)

void(\* mqtt\_sn\_evt\_cb\_t)(struct mqtt\_sn\_client \*client, const struct mqtt\_sn\_evt \*evt)

Asynchronous event notification callback registered by the application.

**Definition** mqtt\_sn.h:158

[mqtt\_sn\_sleep](group__mqtt__sn__socket.md#gaf29a6339419ea02052fe53a18bb8e5ee)

int mqtt\_sn\_sleep(struct mqtt\_sn\_client \*client, uint16\_t duration)

Set the client into sleep state.

[mqtt\_sn\_input](group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49)

int mqtt\_sn\_input(struct mqtt\_sn\_client \*client)

Check the transport for new incoming data.

[MQTT\_SN\_QOS\_M1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9)

@ MQTT\_SN\_QOS\_M1

QOS -1.

**Definition** mqtt\_sn.h:48

[MQTT\_SN\_QOS\_2](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4)

@ MQTT\_SN\_QOS\_2

QOS 2.

**Definition** mqtt\_sn.h:47

[MQTT\_SN\_QOS\_1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da)

@ MQTT\_SN\_QOS\_1

QOS 1.

**Definition** mqtt\_sn.h:46

[MQTT\_SN\_QOS\_0](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389)

@ MQTT\_SN\_QOS\_0

QOS 0.

**Definition** mqtt\_sn.h:45

[MQTT\_SN\_EVT\_PINGRESP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)

@ MQTT\_SN\_EVT\_PINGRESP

Received a PINGRESP.

**Definition** mqtt\_sn.h:120

[MQTT\_SN\_EVT\_CONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6)

@ MQTT\_SN\_EVT\_CONNECTED

Connected to a gateway.

**Definition** mqtt\_sn.h:115

[MQTT\_SN\_EVT\_PUBLISH](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf)

@ MQTT\_SN\_EVT\_PUBLISH

Received a PUBLISH message.

**Definition** mqtt\_sn.h:119

[MQTT\_SN\_EVT\_ASLEEP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f)

@ MQTT\_SN\_EVT\_ASLEEP

Entered ASLEEP state.

**Definition** mqtt\_sn.h:117

[MQTT\_SN\_EVT\_DISCONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf)

@ MQTT\_SN\_EVT\_DISCONNECTED

Disconnected.

**Definition** mqtt\_sn.h:116

[MQTT\_SN\_EVT\_AWAKE](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd)

@ MQTT\_SN\_EVT\_AWAKE

Entered AWAKE state.

**Definition** mqtt\_sn.h:118

[MQTT\_SN\_CODE\_ACCEPTED](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c)

@ MQTT\_SN\_CODE\_ACCEPTED

Accepted.

**Definition** mqtt\_sn.h:78

[MQTT\_SN\_CODE\_REJECTED\_CONGESTION](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7)

@ MQTT\_SN\_CODE\_REJECTED\_CONGESTION

Rejected: congestion.

**Definition** mqtt\_sn.h:79

[MQTT\_SN\_CODE\_REJECTED\_NOTSUP](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5)

@ MQTT\_SN\_CODE\_REJECTED\_NOTSUP

Rejected: Not Supported.

**Definition** mqtt\_sn.h:81

[MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3)

@ MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID

Rejected: Invalid Topic ID.

**Definition** mqtt\_sn.h:80

[MQTT\_SN\_TOPIC\_TYPE\_NORMAL](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b)

@ MQTT\_SN\_TOPIC\_TYPE\_NORMAL

Normal topic.

**Definition** mqtt\_sn.h:59

[MQTT\_SN\_TOPIC\_TYPE\_PREDEF](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b)

@ MQTT\_SN\_TOPIC\_TYPE\_PREDEF

Pre-defined topic.

**Definition** mqtt\_sn.h:66

[MQTT\_SN\_TOPIC\_TYPE\_SHORT](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730)

@ MQTT\_SN\_TOPIC\_TYPE\_SHORT

Short topic.

**Definition** mqtt\_sn.h:71

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[net\_buf.h](net__buf_8h.md)

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

**Definition** kernel.h:3985

[mqtt\_sn\_client](structmqtt__sn__client.md)

Structure describing an MQTT-SN client.

**Definition** mqtt\_sn.h:239

[mqtt\_sn\_client::state](structmqtt__sn__client.md#a02a38427caa60c51f85661efe58813f6)

int state

Current state of the MQTT-SN client.

**Definition** mqtt\_sn.h:281

[mqtt\_sn\_client::next\_msg\_id](structmqtt__sn__client.md#a05b83c732ed9199dac0110cfb1e56563)

uint16\_t next\_msg\_id

Message ID for the next message to be sent.

**Definition** mqtt\_sn.h:272

[mqtt\_sn\_client::ping\_retries](structmqtt__sn__client.md#a2be2f7d041f325dda14007864e03fb70)

uint8\_t ping\_retries

Number of retries for failed ping attempts.

**Definition** mqtt\_sn.h:287

[mqtt\_sn\_client::publish](structmqtt__sn__client.md#a32efbccbf7b1820ff5092896130e6b7e)

sys\_slist\_t publish

List of pending publish messages.

**Definition** mqtt\_sn.h:275

[mqtt\_sn\_client::tx](structmqtt__sn__client.md#a3802bd92a42e421a5d733c64b53473db)

struct net\_buf\_simple tx

Buffer for outgoing data.

**Definition** mqtt\_sn.h:263

[mqtt\_sn\_client::will\_qos](structmqtt__sn__client.md#a42d76db9cbcc9770246241283bb65486)

enum mqtt\_sn\_qos will\_qos

Quality of Service for the Will message.

**Definition** mqtt\_sn.h:254

[mqtt\_sn\_client::process\_work](structmqtt__sn__client.md#a65bb52c8a5ecbd81e743fdc7c213b43a)

struct k\_work\_delayable process\_work

Delayable work structure for processing MQTT-SN events.

**Definition** mqtt\_sn.h:290

[mqtt\_sn\_client::client\_id](structmqtt__sn__client.md#a9cbf86052061b55a93356346cae75e8b)

struct mqtt\_sn\_data client\_id

1-23 character unique client ID

**Definition** mqtt\_sn.h:241

[mqtt\_sn\_client::will\_msg](structmqtt__sn__client.md#a9d2397f5ff59a51630f5b82f94c92327)

struct mqtt\_sn\_data will\_msg

Will message.

**Definition** mqtt\_sn.h:251

[mqtt\_sn\_client::topic](structmqtt__sn__client.md#aa47e6426ca7e8434734377a85f586b84)

sys\_slist\_t topic

List of registered topics.

**Definition** mqtt\_sn.h:278

[mqtt\_sn\_client::evt\_cb](structmqtt__sn__client.md#ac2b8e9d7d4c246c5d5538922a1e9887b)

mqtt\_sn\_evt\_cb\_t evt\_cb

Event callback.

**Definition** mqtt\_sn.h:269

[mqtt\_sn\_client::will\_retain](structmqtt__sn__client.md#ad8f5b3b7815033cfecda7519ca657724)

bool will\_retain

Flag indicating if the will message should be retained by the broker.

**Definition** mqtt\_sn.h:257

[mqtt\_sn\_client::transport](structmqtt__sn__client.md#aec0d4d3f436d7c7d40e2548d7c6575c1)

struct mqtt\_sn\_transport \* transport

Underlying transport to be used by the client.

**Definition** mqtt\_sn.h:260

[mqtt\_sn\_client::rx](structmqtt__sn__client.md#aec40ceeac5a4160b058ee6a7676ec68f)

struct net\_buf\_simple rx

Buffer for incoming data.

**Definition** mqtt\_sn.h:266

[mqtt\_sn\_client::last\_ping](structmqtt__sn__client.md#af400a2f993c27e0f25a4325daeacee28)

int64\_t last\_ping

Timestamp of the last ping request.

**Definition** mqtt\_sn.h:284

[mqtt\_sn\_client::will\_topic](structmqtt__sn__client.md#af70196b9800123e2f9c36362cfb8b6be)

struct mqtt\_sn\_data will\_topic

Topic for Will message.

**Definition** mqtt\_sn.h:246

[mqtt\_sn\_data](structmqtt__sn__data.md)

Abstracts memory buffers.

**Definition** mqtt\_sn.h:85

[mqtt\_sn\_data::size](structmqtt__sn__data.md#a7735f2459fa22fac2b7cf7a08dbee4a5)

uint16\_t size

Size of data, in bytes.

**Definition** mqtt\_sn.h:87

[mqtt\_sn\_data::data](structmqtt__sn__data.md#ae3726684337ee8175224d11dfcf4a7c6)

const uint8\_t \* data

Pointer to data.

**Definition** mqtt\_sn.h:86

[mqtt\_sn\_evt](structmqtt__sn__evt.md)

MQTT-SN event structure to be handled by the event callback.

**Definition** mqtt\_sn.h:141

[mqtt\_sn\_evt::param](structmqtt__sn__evt.md#a8e75d71d1b38e1b84bf1ad20063ec4e8)

union mqtt\_sn\_evt\_param param

Event parameters.

**Definition** mqtt\_sn.h:145

[mqtt\_sn\_evt::type](structmqtt__sn__evt.md#aef636c6acdc17831acb44095fbef1885)

enum mqtt\_sn\_evt\_type type

Event type.

**Definition** mqtt\_sn.h:143

[mqtt\_sn\_transport](structmqtt__sn__transport.md)

Structure to describe an MQTT-SN transport.

**Definition** mqtt\_sn.h:167

[mqtt\_sn\_transport::recv](structmqtt__sn__transport.md#a0f34a4ee28096c8db46db594e44efe98)

ssize\_t(\* recv)(struct mqtt\_sn\_client \*client, void \*buffer, size\_t length)

Will be called by the library when it wants to receive a message.

**Definition** mqtt\_sn.h:192

[mqtt\_sn\_transport::init](structmqtt__sn__transport.md#a3486cb5d56fb42db4c1f62ef9a6bb75b)

int(\* init)(struct mqtt\_sn\_transport \*transport)

Will be called once on client init to initialize the transport.

**Definition** mqtt\_sn.h:173

[mqtt\_sn\_transport::poll](structmqtt__sn__transport.md#abe102ec52b34f767d0b231e93bedd0a9)

int(\* poll)(struct mqtt\_sn\_client \*client)

Check if incoming data is available.

**Definition** mqtt\_sn.h:204

[mqtt\_sn\_transport::msg\_send](structmqtt__sn__transport.md#acbb05050af4c87d7fd3473a9d3fe74a1)

int(\* msg\_send)(struct mqtt\_sn\_client \*client, void \*buf, size\_t sz)

Will be called by the library when it wants to send a message.

**Definition** mqtt\_sn.h:185

[mqtt\_sn\_transport::deinit](structmqtt__sn__transport.md#af51e433970bed12b5217c63416d0ec4c)

void(\* deinit)(struct mqtt\_sn\_transport \*transport)

Will be called on client deinit.

**Definition** mqtt\_sn.h:180

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:388

[mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md)

Event metadata.

**Definition** mqtt\_sn.h:126

[mqtt\_sn\_evt\_param::data](unionmqtt__sn__evt__param.md#a2440375957dae427bb61526331052567)

struct mqtt\_sn\_data data

The payload data associated with the event.

**Definition** mqtt\_sn.h:130

[mqtt\_sn\_evt\_param::topic\_type](unionmqtt__sn__evt__param.md#ab7930bb48e91a24a79593e375f17cdf1)

enum mqtt\_sn\_topic\_type topic\_type

The type of topic for the event.

**Definition** mqtt\_sn.h:132

[mqtt\_sn\_evt\_param::topic\_id](unionmqtt__sn__evt__param.md#ae79e9793f8fc70cc781c4527d8f8496d)

uint16\_t topic\_id

The identifier for the topic of the event.

**Definition** mqtt\_sn.h:134

[mqtt\_sn\_evt\_param::publish](unionmqtt__sn__evt__param.md#afa0ea7d03a7ffdc95c68848af4c9f3ae)

struct mqtt\_sn\_evt\_param::@275266202006044005055345147344370221371361315200 publish

Structure holding publish event details.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mqtt\_sn.h](mqtt__sn_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
