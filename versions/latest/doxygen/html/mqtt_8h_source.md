---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mqtt_8h_source.html
original_path: doxygen/html/mqtt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt.h

[Go to the documentation of this file.](mqtt_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

18

19#ifndef ZEPHYR\_INCLUDE\_NET\_MQTT\_H\_

20#define ZEPHYR\_INCLUDE\_NET\_MQTT\_H\_

21

22#include <stddef.h>

23

24#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/net/tls\_credentials.h](tls__credentials_8h.md)>

27#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

28#include <[zephyr/sys/mutex.h](mutex_8h.md)>

29#include <[zephyr/net/websocket.h](websocket_8h.md)>

30

31#ifdef \_\_cplusplus

32extern "C" {

33#endif

34

[ 39](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91)enum [mqtt\_evt\_type](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91) {

[ 43](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3) [MQTT\_EVT\_CONNACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3),

44

[ 48](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032) [MQTT\_EVT\_DISCONNECT](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032),

49

[ 57](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9) [MQTT\_EVT\_PUBLISH](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9),

58

[ 60](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de) [MQTT\_EVT\_PUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de),

61

[ 63](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87) [MQTT\_EVT\_PUBREC](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87),

64

[ 66](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2) [MQTT\_EVT\_PUBREL](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2),

67

[ 69](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8) [MQTT\_EVT\_PUBCOMP](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8),

70

[ 72](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb) [MQTT\_EVT\_SUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb),

73

[ 75](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2) [MQTT\_EVT\_UNSUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2),

76

[ 78](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5) [MQTT\_EVT\_PINGRESP](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5),

79};

80

[ 82](group__mqtt__socket.md#ga90d152a4b0986e9a07a12c7c56f5e2a0)enum [mqtt\_version](group__mqtt__socket.md#ga90d152a4b0986e9a07a12c7c56f5e2a0) {

[ 83](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7) [MQTT\_VERSION\_3\_1\_0](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7) = 3,

[ 84](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e) [MQTT\_VERSION\_3\_1\_1](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e) = 4

85};

86

[ 88](group__mqtt__socket.md#ga396015e492b0fee8da37c7168d9cdb33)enum [mqtt\_qos](group__mqtt__socket.md#ga396015e492b0fee8da37c7168d9cdb33) {

[ 92](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e) [MQTT\_QOS\_0\_AT\_MOST\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e) = 0x00,

93

[ 97](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d) [MQTT\_QOS\_1\_AT\_LEAST\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d) = 0x01,

98

[ 103](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117) [MQTT\_QOS\_2\_EXACTLY\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117) = 0x02

104};

105

[ 107](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618)enum [mqtt\_conn\_return\_code](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618) {

[ 109](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050) [MQTT\_CONNECTION\_ACCEPTED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050) = 0x00,

110

[ 114](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744) [MQTT\_UNACCEPTABLE\_PROTOCOL\_VERSION](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744) = 0x01,

115

[ 119](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141) [MQTT\_IDENTIFIER\_REJECTED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141) = 0x02,

120

[ 124](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3) [MQTT\_SERVER\_UNAVAILABLE](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3) = 0x03,

125

[ 127](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134) [MQTT\_BAD\_USER\_NAME\_OR\_PASSWORD](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134) = 0x04,

128

[ 130](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb) [MQTT\_NOT\_AUTHORIZED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb) = 0x05

131};

132

[ 134](group__mqtt__socket.md#gaca1e61c8b14b75544e253cea355274a8)enum [mqtt\_suback\_return\_code](group__mqtt__socket.md#gaca1e61c8b14b75544e253cea355274a8) {

[ 136](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01) [MQTT\_SUBACK\_SUCCESS\_QoS\_0](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01) = 0x00,

137

[ 139](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c) [MQTT\_SUBACK\_SUCCESS\_QoS\_1](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c) = 0x01,

140

[ 142](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b) [MQTT\_SUBACK\_SUCCESS\_QoS\_2](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b) = 0x02,

143

[ 145](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7) [MQTT\_SUBACK\_FAILURE](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7) = 0x80

146};

147

[ 149](structmqtt__utf8.md)struct [mqtt\_utf8](structmqtt__utf8.md) {

[ 150](structmqtt__utf8.md#a69a949e3c9cb1794f8d28091601eba16) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[utf8](structmqtt__utf8.md#a69a949e3c9cb1794f8d28091601eba16);

[ 151](structmqtt__utf8.md#a2376f943335326dae74c798141326b70) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [size](structmqtt__utf8.md#a2376f943335326dae74c798141326b70);

152};

153

[ 163](group__mqtt__socket.md#gaeaa4fcf581c7d6be755f9a053a3b488c)#define MQTT\_UTF8\_LITERAL(literal) \

164 ((struct mqtt\_utf8) {literal, sizeof(literal) - 1})

165

[ 167](structmqtt__binstr.md)struct [mqtt\_binstr](structmqtt__binstr.md) {

[ 168](structmqtt__binstr.md#a1f61872edd09941155f60a242e582ff7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structmqtt__binstr.md#a1f61872edd09941155f60a242e582ff7);

[ 169](structmqtt__binstr.md#abcc36b6c59c3da740a6b352fe846fd5f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structmqtt__binstr.md#abcc36b6c59c3da740a6b352fe846fd5f);

170};

171

[ 175](structmqtt__topic.md)struct [mqtt\_topic](structmqtt__topic.md) {

[ 177](structmqtt__topic.md#ab859d08baf88e6a1ac5135e1e55158d5) struct [mqtt\_utf8](structmqtt__utf8.md) [topic](structmqtt__topic.md#ab859d08baf88e6a1ac5135e1e55158d5);

178

[ 182](structmqtt__topic.md#a780e90d62c094557bd3918de3b3921e6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [qos](structmqtt__topic.md#a780e90d62c094557bd3918de3b3921e6);

183};

184

[ 186](structmqtt__publish__message.md)struct [mqtt\_publish\_message](structmqtt__publish__message.md) {

[ 187](structmqtt__publish__message.md#acf5dba605db61efe68ec29337eea95e9) struct [mqtt\_topic](structmqtt__topic.md) [topic](structmqtt__publish__message.md#acf5dba605db61efe68ec29337eea95e9);

[ 188](structmqtt__publish__message.md#a6cfed92c8f8fb319d3cbf40b956cb94d) struct [mqtt\_binstr](structmqtt__binstr.md) [payload](structmqtt__publish__message.md#a6cfed92c8f8fb319d3cbf40b956cb94d);

189};

190

[ 192](structmqtt__connack__param.md)struct [mqtt\_connack\_param](structmqtt__connack__param.md) {

[ 197](structmqtt__connack__param.md#ab123a8236804082667ad93ddd7e40e7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [session\_present\_flag](structmqtt__connack__param.md#ab123a8236804082667ad93ddd7e40e7a);

198

[ 202](structmqtt__connack__param.md#a07e8ca2df92b2f83fc9e732a9c9964f4) enum [mqtt\_conn\_return\_code](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618) [return\_code](structmqtt__connack__param.md#a07e8ca2df92b2f83fc9e732a9c9964f4);

203};

204

[ 206](structmqtt__puback__param.md)struct [mqtt\_puback\_param](structmqtt__puback__param.md) {

[ 208](structmqtt__puback__param.md#a727b919b853e77e480fb841e74a2dedf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](structmqtt__puback__param.md#a727b919b853e77e480fb841e74a2dedf);

209};

210

[ 212](structmqtt__pubrec__param.md)struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) {

[ 214](structmqtt__pubrec__param.md#ab0f92884dbd6e63894210ff7f57fe62c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](structmqtt__pubrec__param.md#ab0f92884dbd6e63894210ff7f57fe62c);

215};

216

[ 218](structmqtt__pubrel__param.md)struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) {

[ 220](structmqtt__pubrel__param.md#a4333fba7ac37d5a68fe921453b56b572) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](structmqtt__pubrel__param.md#a4333fba7ac37d5a68fe921453b56b572);

221};

222

[ 224](structmqtt__pubcomp__param.md)struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) {

[ 226](structmqtt__pubcomp__param.md#ae8484ad4d62f953ecace6c990002e316) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](structmqtt__pubcomp__param.md#ae8484ad4d62f953ecace6c990002e316);

227};

228

[ 230](structmqtt__suback__param.md)struct [mqtt\_suback\_param](structmqtt__suback__param.md) {

[ 232](structmqtt__suback__param.md#a985b53444e7b2c10ab68844fcee34ee4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](structmqtt__suback__param.md#a985b53444e7b2c10ab68844fcee34ee4);

[ 236](structmqtt__suback__param.md#a94ef5183aa3438db0521f445650c5868) struct [mqtt\_binstr](structmqtt__binstr.md) [return\_codes](structmqtt__suback__param.md#a94ef5183aa3438db0521f445650c5868);

237};

238

[ 240](structmqtt__unsuback__param.md)struct [mqtt\_unsuback\_param](structmqtt__unsuback__param.md) {

[ 242](structmqtt__unsuback__param.md#aa453177181e07cd0532b8cf591be0f32) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](structmqtt__unsuback__param.md#aa453177181e07cd0532b8cf591be0f32);

243};

244

[ 246](structmqtt__publish__param.md)struct [mqtt\_publish\_param](structmqtt__publish__param.md) {

[ 250](structmqtt__publish__param.md#a9841a4fbb30b597a9710863ce6034688) struct [mqtt\_publish\_message](structmqtt__publish__message.md) [message](structmqtt__publish__param.md#a9841a4fbb30b597a9710863ce6034688);

251

[ 253](structmqtt__publish__param.md#aac4c6ba605506c183d2d5bdd7e550b3e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](structmqtt__publish__param.md#aac4c6ba605506c183d2d5bdd7e550b3e);

254

[ 258](structmqtt__publish__param.md#a2c2062c2b3ad027d5dfea56cb81c48e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dup\_flag](structmqtt__publish__param.md#a2c2062c2b3ad027d5dfea56cb81c48e7) : 1;

259

[ 263](structmqtt__publish__param.md#a9b2c6fad5bf830276d8d3f6b5ab04210) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [retain\_flag](structmqtt__publish__param.md#a9b2c6fad5bf830276d8d3f6b5ab04210) : 1;

264};

265

[ 267](structmqtt__subscription__list.md)struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) {

[ 269](structmqtt__subscription__list.md#ae9db5f602e3c649b1ccc180aef6c4b4e) struct [mqtt\_topic](structmqtt__topic.md) \*[list](structmqtt__subscription__list.md#ae9db5f602e3c649b1ccc180aef6c4b4e);

270

[ 272](structmqtt__subscription__list.md#aa44e0af3526ee0424627bb24a90ea6b1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [list\_count](structmqtt__subscription__list.md#aa44e0af3526ee0424627bb24a90ea6b1);

273

[ 275](structmqtt__subscription__list.md#a0667dcd4bd5eb5fe1b13b4df1bf2c26f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [message\_id](structmqtt__subscription__list.md#a0667dcd4bd5eb5fe1b13b4df1bf2c26f);

276};

277

[ 282](unionmqtt__evt__param.md)union [mqtt\_evt\_param](unionmqtt__evt__param.md) {

[ 284](unionmqtt__evt__param.md#aa99a77bbade75b3f450088b32131f87a) struct [mqtt\_connack\_param](structmqtt__connack__param.md) [connack](unionmqtt__evt__param.md#aa99a77bbade75b3f450088b32131f87a);

285

[ 292](unionmqtt__evt__param.md#a41be40873e1ebb9bf6fbf6dc9566d6ff) struct [mqtt\_publish\_param](structmqtt__publish__param.md) [publish](unionmqtt__evt__param.md#a41be40873e1ebb9bf6fbf6dc9566d6ff);

293

[ 295](unionmqtt__evt__param.md#a24bf756db9fa8cc67c0b02c4e2cb602c) struct [mqtt\_puback\_param](structmqtt__puback__param.md) [puback](unionmqtt__evt__param.md#a24bf756db9fa8cc67c0b02c4e2cb602c);

296

[ 298](unionmqtt__evt__param.md#a3b31e1d94c480b8d0244cc12d1c25524) struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) [pubrec](unionmqtt__evt__param.md#a3b31e1d94c480b8d0244cc12d1c25524);

299

[ 301](unionmqtt__evt__param.md#a2269e07f580fb65df5f3d0832aa6b3af) struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) [pubrel](unionmqtt__evt__param.md#a2269e07f580fb65df5f3d0832aa6b3af);

302

[ 304](unionmqtt__evt__param.md#ac3d564095019ccf57c10678a433bc31a) struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) [pubcomp](unionmqtt__evt__param.md#ac3d564095019ccf57c10678a433bc31a);

305

[ 307](unionmqtt__evt__param.md#af6ce2426884d2faa443b3dfdaa45594c) struct [mqtt\_suback\_param](structmqtt__suback__param.md) [suback](unionmqtt__evt__param.md#af6ce2426884d2faa443b3dfdaa45594c);

308

[ 310](unionmqtt__evt__param.md#ad040b028ed0aaabcaddedc204fb709d8) struct [mqtt\_unsuback\_param](structmqtt__unsuback__param.md) [unsuback](unionmqtt__evt__param.md#ad040b028ed0aaabcaddedc204fb709d8);

311};

312

[ 314](structmqtt__evt.md)struct [mqtt\_evt](structmqtt__evt.md) {

[ 316](structmqtt__evt.md#a79d7a198d8ed9959bb7aae835b6301c2) enum [mqtt\_evt\_type](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91) [type](structmqtt__evt.md#a79d7a198d8ed9959bb7aae835b6301c2);

317

[ 319](structmqtt__evt.md#aca1085171667c46b2438f66d9227e07c) union [mqtt\_evt\_param](unionmqtt__evt__param.md) [param](structmqtt__evt.md#aca1085171667c46b2438f66d9227e07c);

320

[ 324](structmqtt__evt.md#aa1a4304d4aa70440ba630f3fe5e76d2f) int [result](structmqtt__evt.md#aa1a4304d4aa70440ba630f3fe5e76d2f);

325};

326

327struct [mqtt\_client](structmqtt__client.md);

328

[ 337](group__mqtt__socket.md#gabdf01ededb62ceb4c1608a64cb718a8c)typedef void (\*[mqtt\_evt\_cb\_t](group__mqtt__socket.md#gabdf01ededb62ceb4c1608a64cb718a8c))(struct [mqtt\_client](structmqtt__client.md) \*client,

338 const struct [mqtt\_evt](structmqtt__evt.md) \*evt);

339

[ 341](structmqtt__sec__config.md)struct [mqtt\_sec\_config](structmqtt__sec__config.md) {

[ 343](structmqtt__sec__config.md#a0e04768b6589823464c2d13c31230cad) int [peer\_verify](structmqtt__sec__config.md#a0e04768b6589823464c2d13c31230cad);

344

[ 346](structmqtt__sec__config.md#a25415e32e00808fb6a24187f4234059f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cipher\_count](structmqtt__sec__config.md#a25415e32e00808fb6a24187f4234059f);

347

[ 351](structmqtt__sec__config.md#a179a97d56a7a12d5afb60257a67ce46c) const int \*[cipher\_list](structmqtt__sec__config.md#a179a97d56a7a12d5afb60257a67ce46c);

352

[ 354](structmqtt__sec__config.md#a6d59afc061a749ea31f5bd415918a3e0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sec\_tag\_count](structmqtt__sec__config.md#a6d59afc061a749ea31f5bd415918a3e0);

355

[ 357](structmqtt__sec__config.md#adeb8630a9e73c4b3226afa1c9a5060fe) const [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) \*[sec\_tag\_list](structmqtt__sec__config.md#adeb8630a9e73c4b3226afa1c9a5060fe);

358

[ 362](structmqtt__sec__config.md#af7a0ee827bf98fde264000f4c9020c15) const char \*[hostname](structmqtt__sec__config.md#af7a0ee827bf98fde264000f4c9020c15);

363

[ 365](structmqtt__sec__config.md#a5beac5704fec3e399e5c0099a57ce115) int [cert\_nocopy](structmqtt__sec__config.md#a5beac5704fec3e399e5c0099a57ce115);

366};

367

[ 369](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4)enum [mqtt\_transport\_type](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4) {

[ 371](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a) [MQTT\_TRANSPORT\_NON\_SECURE](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a),

372

373#if defined(CONFIG\_MQTT\_LIB\_TLS)

375 MQTT\_TRANSPORT\_SECURE,

376#endif /\* CONFIG\_MQTT\_LIB\_TLS \*/

377

378#if defined(CONFIG\_MQTT\_LIB\_WEBSOCKET)

380 MQTT\_TRANSPORT\_NON\_SECURE\_WEBSOCKET,

381#if defined(CONFIG\_MQTT\_LIB\_TLS)

383 MQTT\_TRANSPORT\_SECURE\_WEBSOCKET,

384#endif

385#endif /\* CONFIG\_MQTT\_LIB\_WEBSOCKET \*/

386#if defined(CONFIG\_MQTT\_LIB\_CUSTOM\_TRANSPORT)

388 MQTT\_TRANSPORT\_CUSTOM,

389#endif /\* CONFIG\_MQTT\_LIB\_CUSTOM\_TRANSPORT \*/

390

[ 394](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df) [MQTT\_TRANSPORT\_NUM](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df)

395};

396

[ 398](structmqtt__transport.md)struct [mqtt\_transport](structmqtt__transport.md) {

[ 403](structmqtt__transport.md#a47b49927c79e67b202112c68b53d83f4) enum [mqtt\_transport\_type](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4) [type](structmqtt__transport.md#a47b49927c79e67b202112c68b53d83f4);

404

405 union {

406 /\* TCP socket transport for MQTT \*/

407 struct {

[ 409](structmqtt__transport.md#a3b4589dd05394589e7af460761b800bf) int [sock](structmqtt__transport.md#a3b4589dd05394589e7af460761b800bf);

[ 410](structmqtt__transport.md#aa24b42579c13104c8660efc764f0b8f2) } [tcp](structmqtt__transport.md#aa24b42579c13104c8660efc764f0b8f2);

411

412#if defined(CONFIG\_MQTT\_LIB\_TLS)

413 /\* TLS socket transport for MQTT \*/

414 struct {

416 int [sock](structmqtt__transport.md#a3b4589dd05394589e7af460761b800bf);

417

421 struct [mqtt\_sec\_config](structmqtt__sec__config.md) config;

422 } tls;

423#endif /\* CONFIG\_MQTT\_LIB\_TLS \*/

424 };

425

426#if defined(CONFIG\_MQTT\_LIB\_WEBSOCKET)

428 struct {

430 struct websocket\_request config;

431

433 int sock;

434

436 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout;

437 } websocket;

438#endif

439

440#if defined(CONFIG\_MQTT\_LIB\_CUSTOM\_TRANSPORT)

442 void \*custom\_transport\_data;

443#endif /\* CONFIG\_MQTT\_LIB\_CUSTOM\_TRANSPORT \*/

444

445#if defined(CONFIG\_SOCKS)

446 struct {

447 struct sockaddr addr;

448 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen;

449 } proxy;

450#endif

451};

452

[ 454](structmqtt__internal.md)struct [mqtt\_internal](structmqtt__internal.md) {

[ 456](structmqtt__internal.md#af866a252b9e18496c8e1627704d8a8b2) struct [sys\_mutex](structsys__mutex.md) [mutex](structmqtt__internal.md#af866a252b9e18496c8e1627704d8a8b2);

457

[ 461](structmqtt__internal.md#a8f30cb1440efecf8ae8fc448e4f462f8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [last\_activity](structmqtt__internal.md#a8f30cb1440efecf8ae8fc448e4f462f8);

462

[ 464](structmqtt__internal.md#acf93a973de5a5430e767e2996f1cd048) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](structmqtt__internal.md#acf93a973de5a5430e767e2996f1cd048);

465

[ 467](structmqtt__internal.md#a45aeafd71dadaf1d0fd0bc3969c921de) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_buf\_datalen](structmqtt__internal.md#a45aeafd71dadaf1d0fd0bc3969c921de);

468

[ 470](structmqtt__internal.md#a921477a9839447f4fe1c823911680c92) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [remaining\_payload](structmqtt__internal.md#a921477a9839447f4fe1c823911680c92);

471};

472

[ 477](structmqtt__client.md)struct [mqtt\_client](structmqtt__client.md) {

[ 479](structmqtt__client.md#a41cc1d3c5e5180af1d6376f88598678a) struct [mqtt\_internal](structmqtt__internal.md) [internal](structmqtt__client.md#a41cc1d3c5e5180af1d6376f88598678a);

480

[ 482](structmqtt__client.md#ac31a2ea9d67886f83fd3af88f33f36d9) struct [mqtt\_transport](structmqtt__transport.md) [transport](structmqtt__client.md#ac31a2ea9d67886f83fd3af88f33f36d9);

483

[ 485](structmqtt__client.md#aabd419115c8637e4e4c0e6d23a5a984d) struct [mqtt\_utf8](structmqtt__utf8.md) [client\_id](structmqtt__client.md#aabd419115c8637e4e4c0e6d23a5a984d);

486

[ 490](structmqtt__client.md#a72d61d9c0e717010ff90c2ed7fcddf5c) const void \*[broker](structmqtt__client.md#a72d61d9c0e717010ff90c2ed7fcddf5c);

491

[ 495](structmqtt__client.md#ab271f2061fe3c9e3c1a76158a1c00449) struct [mqtt\_utf8](structmqtt__utf8.md) \*[user\_name](structmqtt__client.md#ab271f2061fe3c9e3c1a76158a1c00449);

496

[ 501](structmqtt__client.md#aef6da1db6f600a2bfd1c7dd0d78d1b6d) struct [mqtt\_utf8](structmqtt__utf8.md) \*[password](structmqtt__client.md#aef6da1db6f600a2bfd1c7dd0d78d1b6d);

502

[ 504](structmqtt__client.md#a4b23a72831697b78dc4019a4b6ac97e4) struct [mqtt\_topic](structmqtt__topic.md) \*[will\_topic](structmqtt__client.md#a4b23a72831697b78dc4019a4b6ac97e4);

505

[ 509](structmqtt__client.md#a7f4e9547b1d91edf21589334db711499) struct [mqtt\_utf8](structmqtt__utf8.md) \*[will\_message](structmqtt__client.md#a7f4e9547b1d91edf21589334db711499);

510

[ 513](structmqtt__client.md#a44c515b8b25d59554990f6193217d83f) [mqtt\_evt\_cb\_t](group__mqtt__socket.md#gabdf01ededb62ceb4c1608a64cb718a8c) [evt\_cb](structmqtt__client.md#a44c515b8b25d59554990f6193217d83f);

514

[ 516](structmqtt__client.md#a9f63fb54f8557135c1aa38a60bb7053c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[rx\_buf](structmqtt__client.md#a9f63fb54f8557135c1aa38a60bb7053c);

517

[ 519](structmqtt__client.md#a66335741e991a2985ab5d4d7765651d2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rx\_buf\_size](structmqtt__client.md#a66335741e991a2985ab5d4d7765651d2);

520

[ 522](structmqtt__client.md#ae582274bf396caa0a3427f1aeace639c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tx\_buf](structmqtt__client.md#ae582274bf396caa0a3427f1aeace639c);

523

[ 525](structmqtt__client.md#a4c456f4065e3bc20752d908f2d805667) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tx\_buf\_size](structmqtt__client.md#a4c456f4065e3bc20752d908f2d805667);

526

[ 530](structmqtt__client.md#aa65a4af5952634e4ff5c4bf700ccccd7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [keepalive](structmqtt__client.md#aa65a4af5952634e4ff5c4bf700ccccd7);

531

[ 533](structmqtt__client.md#a63e3c1b470a7de9d179b1c0686504a68) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [protocol\_version](structmqtt__client.md#a63e3c1b470a7de9d179b1c0686504a68);

534

[ 536](structmqtt__client.md#a67f76cd0feadf8ae11ed232dcc9ac1d1) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [unacked\_ping](structmqtt__client.md#a67f76cd0feadf8ae11ed232dcc9ac1d1);

537

[ 540](structmqtt__client.md#ac96879e15ccd829fbcf9b88913161c0d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [will\_retain](structmqtt__client.md#ac96879e15ccd829fbcf9b88913161c0d) : 1;

541

[ 545](structmqtt__client.md#aae9ecb0faf8dc4337579e0713d065184) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clean\_session](structmqtt__client.md#aae9ecb0faf8dc4337579e0713d065184) : 1;

546};

547

[ 557](group__mqtt__socket.md#gad1376509ae7c946c840d103d8b59e9a1)void [mqtt\_client\_init](group__mqtt__socket.md#gad1376509ae7c946c840d103d8b59e9a1)(struct [mqtt\_client](structmqtt__client.md) \*client);

558

559#if defined(CONFIG\_SOCKS)

560/\*

561 \* @brief Set proxy server details

562 \*

563 \* @param[in] client Client instance for which the procedure is requested,

564 \* Shall not be NULL.

565 \* @param[in] proxy\_addr Proxy server address.

566 \* @param[in] addrlen Proxy server address length.

567 \*

568 \* @return 0 or a negative error code (errno.h) indicating reason of failure.

569 \*

570 \* @note Must be called before calling mqtt\_connect().

571 \*/

572int mqtt\_client\_set\_proxy(struct [mqtt\_client](structmqtt__client.md) \*client,

573 struct [sockaddr](structsockaddr.md) \*proxy\_addr,

574 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

575#endif

576

[ 595](group__mqtt__socket.md#gad936f28553cb2e771a843512b0a315fa)int [mqtt\_connect](group__mqtt__socket.md#gad936f28553cb2e771a843512b0a315fa)(struct [mqtt\_client](structmqtt__client.md) \*client);

596

[ 607](group__mqtt__socket.md#ga57745efa1bf6fbdf7eb1b3f01623e4c7)int [mqtt\_publish](group__mqtt__socket.md#ga57745efa1bf6fbdf7eb1b3f01623e4c7)(struct [mqtt\_client](structmqtt__client.md) \*client,

608 const struct [mqtt\_publish\_param](structmqtt__publish__param.md) \*param);

609

[ 621](group__mqtt__socket.md#gae9069fceec2c018e64cc6beb16aa055c)int [mqtt\_publish\_qos1\_ack](group__mqtt__socket.md#gae9069fceec2c018e64cc6beb16aa055c)(struct [mqtt\_client](structmqtt__client.md) \*client,

622 const struct [mqtt\_puback\_param](structmqtt__puback__param.md) \*param);

623

[ 635](group__mqtt__socket.md#gacbe41b83d9c0676d0d4cf01dd91765eb)int [mqtt\_publish\_qos2\_receive](group__mqtt__socket.md#gacbe41b83d9c0676d0d4cf01dd91765eb)(struct [mqtt\_client](structmqtt__client.md) \*client,

636 const struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) \*param);

637

[ 648](group__mqtt__socket.md#ga6c952ed014f78774096bfb6099794803)int [mqtt\_publish\_qos2\_release](group__mqtt__socket.md#ga6c952ed014f78774096bfb6099794803)(struct [mqtt\_client](structmqtt__client.md) \*client,

649 const struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) \*param);

650

[ 662](group__mqtt__socket.md#ga2b17999e845d613f5b0b20015b8204f3)int [mqtt\_publish\_qos2\_complete](group__mqtt__socket.md#ga2b17999e845d613f5b0b20015b8204f3)(struct [mqtt\_client](structmqtt__client.md) \*client,

663 const struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) \*param);

664

[ 674](group__mqtt__socket.md#ga40d226b891b8f62f2c486bbb11ce9678)int [mqtt\_subscribe](group__mqtt__socket.md#ga40d226b891b8f62f2c486bbb11ce9678)(struct [mqtt\_client](structmqtt__client.md) \*client,

675 const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \*param);

676

[ 689](group__mqtt__socket.md#ga4ff43a198e93e332b5553a4d0b59261d)int [mqtt\_unsubscribe](group__mqtt__socket.md#ga4ff43a198e93e332b5553a4d0b59261d)(struct [mqtt\_client](structmqtt__client.md) \*client,

690 const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \*param);

691

[ 701](group__mqtt__socket.md#gad1d549d37b69a61e1bf8d9d213e02ca8)int [mqtt\_ping](group__mqtt__socket.md#gad1d549d37b69a61e1bf8d9d213e02ca8)(struct [mqtt\_client](structmqtt__client.md) \*client);

702

[ 711](group__mqtt__socket.md#gad5e01a1b60c393adb0f7f34c1a90e6ff)int [mqtt\_disconnect](group__mqtt__socket.md#gad5e01a1b60c393adb0f7f34c1a90e6ff)(struct [mqtt\_client](structmqtt__client.md) \*client);

712

[ 723](group__mqtt__socket.md#gafb2df41fad7c318f9fe75919919139bd)int [mqtt\_abort](group__mqtt__socket.md#gafb2df41fad7c318f9fe75919919139bd)(struct [mqtt\_client](structmqtt__client.md) \*client);

724

[ 739](group__mqtt__socket.md#ga8b87710d01076c8e51b1a75634168269)int [mqtt\_live](group__mqtt__socket.md#ga8b87710d01076c8e51b1a75634168269)(struct [mqtt\_client](structmqtt__client.md) \*client);

740

[ 751](group__mqtt__socket.md#gaa16bf7b0597ad00c4a3943235579e86b)int [mqtt\_keepalive\_time\_left](group__mqtt__socket.md#gaa16bf7b0597ad00c4a3943235579e86b)(const struct [mqtt\_client](structmqtt__client.md) \*client);

752

[ 768](group__mqtt__socket.md#ga2dbc3c158d63a6f57b362be94c22660a)int [mqtt\_input](group__mqtt__socket.md#ga2dbc3c158d63a6f57b362be94c22660a)(struct [mqtt\_client](structmqtt__client.md) \*client);

769

[ 785](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172)int [mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172)(struct [mqtt\_client](structmqtt__client.md) \*client, void \*buffer,

786 size\_t length);

787

[ 799](group__mqtt__socket.md#ga05213aceaa9e9cbbfaa9bab7a78b3d25)int [mqtt\_read\_publish\_payload\_blocking](group__mqtt__socket.md#ga05213aceaa9e9cbbfaa9bab7a78b3d25)(struct [mqtt\_client](structmqtt__client.md) \*client, void \*buffer,

800 size\_t length);

801

[ 814](group__mqtt__socket.md#ga31823965ec34a253793b40b50e800417)int [mqtt\_readall\_publish\_payload](group__mqtt__socket.md#ga31823965ec34a253793b40b50e800417)(struct [mqtt\_client](structmqtt__client.md) \*client, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer,

815 size\_t length);

816

817#ifdef \_\_cplusplus

818}

819#endif

820

821#endif /\* ZEPHYR\_INCLUDE\_NET\_MQTT\_H\_ \*/

822

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[mqtt\_evt\_type](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91)

mqtt\_evt\_type

MQTT Asynchronous Events notified to the application from the module through the callback registered ...

**Definition** mqtt.h:39

[mqtt\_read\_publish\_payload\_blocking](group__mqtt__socket.md#ga05213aceaa9e9cbbfaa9bab7a78b3d25)

int mqtt\_read\_publish\_payload\_blocking(struct mqtt\_client \*client, void \*buffer, size\_t length)

Blocking version of mqtt\_read\_publish\_payload function.

[mqtt\_publish\_qos2\_complete](group__mqtt__socket.md#ga2b17999e845d613f5b0b20015b8204f3)

int mqtt\_publish\_qos2\_complete(struct mqtt\_client \*client, const struct mqtt\_pubcomp\_param \*param)

API used by client to send acknowledgment on receiving QoS2 publish release message.

[mqtt\_input](group__mqtt__socket.md#ga2dbc3c158d63a6f57b362be94c22660a)

int mqtt\_input(struct mqtt\_client \*client)

Receive an incoming MQTT packet.

[mqtt\_readall\_publish\_payload](group__mqtt__socket.md#ga31823965ec34a253793b40b50e800417)

int mqtt\_readall\_publish\_payload(struct mqtt\_client \*client, uint8\_t \*buffer, size\_t length)

Blocking version of mqtt\_read\_publish\_payload function which runs until the required number of bytes ...

[mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172)

int mqtt\_read\_publish\_payload(struct mqtt\_client \*client, void \*buffer, size\_t length)

Read the payload of the received PUBLISH message.

[mqtt\_qos](group__mqtt__socket.md#ga396015e492b0fee8da37c7168d9cdb33)

mqtt\_qos

MQTT Quality of Service types.

**Definition** mqtt.h:88

[mqtt\_subscribe](group__mqtt__socket.md#ga40d226b891b8f62f2c486bbb11ce9678)

int mqtt\_subscribe(struct mqtt\_client \*client, const struct mqtt\_subscription\_list \*param)

API to request subscription of one or more topics on the connection.

[mqtt\_unsubscribe](group__mqtt__socket.md#ga4ff43a198e93e332b5553a4d0b59261d)

int mqtt\_unsubscribe(struct mqtt\_client \*client, const struct mqtt\_subscription\_list \*param)

API to request unsubscription of one or more topics on the connection.

[mqtt\_publish](group__mqtt__socket.md#ga57745efa1bf6fbdf7eb1b3f01623e4c7)

int mqtt\_publish(struct mqtt\_client \*client, const struct mqtt\_publish\_param \*param)

API to publish messages on topics.

[mqtt\_publish\_qos2\_release](group__mqtt__socket.md#ga6c952ed014f78774096bfb6099794803)

int mqtt\_publish\_qos2\_release(struct mqtt\_client \*client, const struct mqtt\_pubrel\_param \*param)

API used by client to request release of QoS2 publish message.

[mqtt\_live](group__mqtt__socket.md#ga8b87710d01076c8e51b1a75634168269)

int mqtt\_live(struct mqtt\_client \*client)

This API should be called periodically for the client to be able to keep the connection alive by send...

[mqtt\_version](group__mqtt__socket.md#ga90d152a4b0986e9a07a12c7c56f5e2a0)

mqtt\_version

MQTT version protocol level.

**Definition** mqtt.h:82

[mqtt\_keepalive\_time\_left](group__mqtt__socket.md#gaa16bf7b0597ad00c4a3943235579e86b)

int mqtt\_keepalive\_time\_left(const struct mqtt\_client \*client)

Helper function to determine when next keep alive message should be sent.

[mqtt\_conn\_return\_code](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618)

mqtt\_conn\_return\_code

MQTT CONNACK return codes.

**Definition** mqtt.h:107

[mqtt\_evt\_cb\_t](group__mqtt__socket.md#gabdf01ededb62ceb4c1608a64cb718a8c)

void(\* mqtt\_evt\_cb\_t)(struct mqtt\_client \*client, const struct mqtt\_evt \*evt)

Asynchronous event notification callback registered by the application.

**Definition** mqtt.h:337

[mqtt\_suback\_return\_code](group__mqtt__socket.md#gaca1e61c8b14b75544e253cea355274a8)

mqtt\_suback\_return\_code

MQTT SUBACK return codes.

**Definition** mqtt.h:134

[mqtt\_publish\_qos2\_receive](group__mqtt__socket.md#gacbe41b83d9c0676d0d4cf01dd91765eb)

int mqtt\_publish\_qos2\_receive(struct mqtt\_client \*client, const struct mqtt\_pubrec\_param \*param)

API used by client to send acknowledgment on receiving QoS2 publish message.

[mqtt\_client\_init](group__mqtt__socket.md#gad1376509ae7c946c840d103d8b59e9a1)

void mqtt\_client\_init(struct mqtt\_client \*client)

Initializes the client instance.

[mqtt\_ping](group__mqtt__socket.md#gad1d549d37b69a61e1bf8d9d213e02ca8)

int mqtt\_ping(struct mqtt\_client \*client)

API to send MQTT ping.

[mqtt\_disconnect](group__mqtt__socket.md#gad5e01a1b60c393adb0f7f34c1a90e6ff)

int mqtt\_disconnect(struct mqtt\_client \*client)

API to disconnect MQTT connection.

[mqtt\_connect](group__mqtt__socket.md#gad936f28553cb2e771a843512b0a315fa)

int mqtt\_connect(struct mqtt\_client \*client)

API to request new MQTT client connection.

[mqtt\_publish\_qos1\_ack](group__mqtt__socket.md#gae9069fceec2c018e64cc6beb16aa055c)

int mqtt\_publish\_qos1\_ack(struct mqtt\_client \*client, const struct mqtt\_puback\_param \*param)

API used by client to send acknowledgment on receiving QoS1 publish message.

[mqtt\_abort](group__mqtt__socket.md#gafb2df41fad7c318f9fe75919919139bd)

int mqtt\_abort(struct mqtt\_client \*client)

API to abort MQTT connection.

[mqtt\_transport\_type](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4)

mqtt\_transport\_type

MQTT transport type.

**Definition** mqtt.h:369

[MQTT\_EVT\_PUBREC](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87)

@ MQTT\_EVT\_PUBREC

Reception confirmation for published message with QoS 2.

**Definition** mqtt.h:63

[MQTT\_EVT\_PUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de)

@ MQTT\_EVT\_PUBACK

Acknowledgment for published message with QoS 1.

**Definition** mqtt.h:60

[MQTT\_EVT\_PINGRESP](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5)

@ MQTT\_EVT\_PINGRESP

Ping Response from server.

**Definition** mqtt.h:78

[MQTT\_EVT\_SUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb)

@ MQTT\_EVT\_SUBACK

Acknowledgment to a subscribe request.

**Definition** mqtt.h:72

[MQTT\_EVT\_DISCONNECT](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032)

@ MQTT\_EVT\_DISCONNECT

Disconnection Event.

**Definition** mqtt.h:48

[MQTT\_EVT\_UNSUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2)

@ MQTT\_EVT\_UNSUBACK

Acknowledgment to a unsubscribe request.

**Definition** mqtt.h:75

[MQTT\_EVT\_PUBLISH](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9)

@ MQTT\_EVT\_PUBLISH

Publish event received when message is published on a topic client is subscribed to.

**Definition** mqtt.h:57

[MQTT\_EVT\_PUBREL](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2)

@ MQTT\_EVT\_PUBREL

Release of published message with QoS 2.

**Definition** mqtt.h:66

[MQTT\_EVT\_CONNACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3)

@ MQTT\_EVT\_CONNACK

Acknowledgment of connection request.

**Definition** mqtt.h:43

[MQTT\_EVT\_PUBCOMP](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8)

@ MQTT\_EVT\_PUBCOMP

Confirmation to a publish release message with QoS 2.

**Definition** mqtt.h:69

[MQTT\_QOS\_0\_AT\_MOST\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e)

@ MQTT\_QOS\_0\_AT\_MOST\_ONCE

Lowest Quality of Service, no acknowledgment needed for published message.

**Definition** mqtt.h:92

[MQTT\_QOS\_1\_AT\_LEAST\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d)

@ MQTT\_QOS\_1\_AT\_LEAST\_ONCE

Medium Quality of Service, if acknowledgment expected for published message, duplicate messages permi...

**Definition** mqtt.h:97

[MQTT\_QOS\_2\_EXACTLY\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117)

@ MQTT\_QOS\_2\_EXACTLY\_ONCE

Highest Quality of Service, acknowledgment expected and message shall be published only once.

**Definition** mqtt.h:103

[MQTT\_VERSION\_3\_1\_0](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7)

@ MQTT\_VERSION\_3\_1\_0

Protocol level for 3.1.0.

**Definition** mqtt.h:83

[MQTT\_VERSION\_3\_1\_1](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e)

@ MQTT\_VERSION\_3\_1\_1

Protocol level for 3.1.1.

**Definition** mqtt.h:84

[MQTT\_CONNECTION\_ACCEPTED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050)

@ MQTT\_CONNECTION\_ACCEPTED

Connection accepted.

**Definition** mqtt.h:109

[MQTT\_NOT\_AUTHORIZED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb)

@ MQTT\_NOT\_AUTHORIZED

The Client is not authorized to connect.

**Definition** mqtt.h:130

[MQTT\_UNACCEPTABLE\_PROTOCOL\_VERSION](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744)

@ MQTT\_UNACCEPTABLE\_PROTOCOL\_VERSION

The Server does not support the level of the MQTT protocol requested by the Client.

**Definition** mqtt.h:114

[MQTT\_BAD\_USER\_NAME\_OR\_PASSWORD](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134)

@ MQTT\_BAD\_USER\_NAME\_OR\_PASSWORD

The data in the user name or password is malformed.

**Definition** mqtt.h:127

[MQTT\_IDENTIFIER\_REJECTED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141)

@ MQTT\_IDENTIFIER\_REJECTED

The Client identifier is correct UTF-8 but not allowed by the Server.

**Definition** mqtt.h:119

[MQTT\_SERVER\_UNAVAILABLE](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3)

@ MQTT\_SERVER\_UNAVAILABLE

The Network Connection has been made but the MQTT service is unavailable.

**Definition** mqtt.h:124

[MQTT\_SUBACK\_FAILURE](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7)

@ MQTT\_SUBACK\_FAILURE

Subscription for a topic failed.

**Definition** mqtt.h:145

[MQTT\_SUBACK\_SUCCESS\_QoS\_0](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01)

@ MQTT\_SUBACK\_SUCCESS\_QoS\_0

Subscription with QoS 0 succeeded.

**Definition** mqtt.h:136

[MQTT\_SUBACK\_SUCCESS\_QoS\_2](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b)

@ MQTT\_SUBACK\_SUCCESS\_QoS\_2

Subscription with QoS 2 succeeded.

**Definition** mqtt.h:142

[MQTT\_SUBACK\_SUCCESS\_QoS\_1](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c)

@ MQTT\_SUBACK\_SUCCESS\_QoS\_1

Subscription with QoS 1 succeeded.

**Definition** mqtt.h:139

[MQTT\_TRANSPORT\_NUM](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df)

@ MQTT\_TRANSPORT\_NUM

Shall not be used as a transport type.

**Definition** mqtt.h:394

[MQTT\_TRANSPORT\_NON\_SECURE](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a)

@ MQTT\_TRANSPORT\_NON\_SECURE

Use non secure TCP transport for MQTT connection.

**Definition** mqtt.h:371

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:72

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[mutex.h](mutex_8h.md)

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[mqtt\_binstr](structmqtt__binstr.md)

Abstracts binary strings.

**Definition** mqtt.h:167

[mqtt\_binstr::data](structmqtt__binstr.md#a1f61872edd09941155f60a242e582ff7)

uint8\_t \* data

Pointer to binary stream.

**Definition** mqtt.h:168

[mqtt\_binstr::len](structmqtt__binstr.md#abcc36b6c59c3da740a6b352fe846fd5f)

uint32\_t len

Length of binary stream.

**Definition** mqtt.h:169

[mqtt\_client](structmqtt__client.md)

MQTT Client definition to maintain information relevant to the client.

**Definition** mqtt.h:477

[mqtt\_client::internal](structmqtt__client.md#a41cc1d3c5e5180af1d6376f88598678a)

struct mqtt\_internal internal

MQTT client internal state.

**Definition** mqtt.h:479

[mqtt\_client::evt\_cb](structmqtt__client.md#a44c515b8b25d59554990f6193217d83f)

mqtt\_evt\_cb\_t evt\_cb

Application callback registered with the module to get MQTT events.

**Definition** mqtt.h:513

[mqtt\_client::will\_topic](structmqtt__client.md#a4b23a72831697b78dc4019a4b6ac97e4)

struct mqtt\_topic \* will\_topic

Will topic and QoS.

**Definition** mqtt.h:504

[mqtt\_client::tx\_buf\_size](structmqtt__client.md#a4c456f4065e3bc20752d908f2d805667)

uint32\_t tx\_buf\_size

Size of transmit buffer.

**Definition** mqtt.h:525

[mqtt\_client::protocol\_version](structmqtt__client.md#a63e3c1b470a7de9d179b1c0686504a68)

uint8\_t protocol\_version

MQTT protocol version.

**Definition** mqtt.h:533

[mqtt\_client::rx\_buf\_size](structmqtt__client.md#a66335741e991a2985ab5d4d7765651d2)

uint32\_t rx\_buf\_size

Size of receive buffer.

**Definition** mqtt.h:519

[mqtt\_client::unacked\_ping](structmqtt__client.md#a67f76cd0feadf8ae11ed232dcc9ac1d1)

int8\_t unacked\_ping

Unanswered PINGREQ count on this connection.

**Definition** mqtt.h:536

[mqtt\_client::broker](structmqtt__client.md#a72d61d9c0e717010ff90c2ed7fcddf5c)

const void \* broker

Broker details, for example, address, port.

**Definition** mqtt.h:490

[mqtt\_client::will\_message](structmqtt__client.md#a7f4e9547b1d91edf21589334db711499)

struct mqtt\_utf8 \* will\_message

Will message.

**Definition** mqtt.h:509

[mqtt\_client::rx\_buf](structmqtt__client.md#a9f63fb54f8557135c1aa38a60bb7053c)

uint8\_t \* rx\_buf

Receive buffer used for MQTT packet reception in RX path.

**Definition** mqtt.h:516

[mqtt\_client::keepalive](structmqtt__client.md#aa65a4af5952634e4ff5c4bf700ccccd7)

uint16\_t keepalive

Keepalive interval for this client in seconds.

**Definition** mqtt.h:530

[mqtt\_client::client\_id](structmqtt__client.md#aabd419115c8637e4e4c0e6d23a5a984d)

struct mqtt\_utf8 client\_id

Unique client identification to be used for the connection.

**Definition** mqtt.h:485

[mqtt\_client::clean\_session](structmqtt__client.md#aae9ecb0faf8dc4337579e0713d065184)

uint8\_t clean\_session

Clean session flag indicating a fresh (1) or a retained session (0).

**Definition** mqtt.h:545

[mqtt\_client::user\_name](structmqtt__client.md#ab271f2061fe3c9e3c1a76158a1c00449)

struct mqtt\_utf8 \* user\_name

User name (if any) to be used for the connection.

**Definition** mqtt.h:495

[mqtt\_client::transport](structmqtt__client.md#ac31a2ea9d67886f83fd3af88f33f36d9)

struct mqtt\_transport transport

MQTT transport configuration and data.

**Definition** mqtt.h:482

[mqtt\_client::will\_retain](structmqtt__client.md#ac96879e15ccd829fbcf9b88913161c0d)

uint8\_t will\_retain

Will retain flag, 1 if will message shall be retained persistently.

**Definition** mqtt.h:540

[mqtt\_client::tx\_buf](structmqtt__client.md#ae582274bf396caa0a3427f1aeace639c)

uint8\_t \* tx\_buf

Transmit buffer used for creating MQTT packet in TX path.

**Definition** mqtt.h:522

[mqtt\_client::password](structmqtt__client.md#aef6da1db6f600a2bfd1c7dd0d78d1b6d)

struct mqtt\_utf8 \* password

Password (if any) to be used for the connection.

**Definition** mqtt.h:501

[mqtt\_connack\_param](structmqtt__connack__param.md)

Parameters for a connection acknowledgment (CONNACK).

**Definition** mqtt.h:192

[mqtt\_connack\_param::return\_code](structmqtt__connack__param.md#a07e8ca2df92b2f83fc9e732a9c9964f4)

enum mqtt\_conn\_return\_code return\_code

The appropriate non-zero Connect return code indicates if the Server is unable to process a connectio...

**Definition** mqtt.h:202

[mqtt\_connack\_param::session\_present\_flag](structmqtt__connack__param.md#ab123a8236804082667ad93ddd7e40e7a)

uint8\_t session\_present\_flag

The Session Present flag enables a Client to establish whether the Client and Server have a consisten...

**Definition** mqtt.h:197

[mqtt\_evt](structmqtt__evt.md)

Defines MQTT asynchronous event notified to the application.

**Definition** mqtt.h:314

[mqtt\_evt::type](structmqtt__evt.md#a79d7a198d8ed9959bb7aae835b6301c2)

enum mqtt\_evt\_type type

Identifies the event.

**Definition** mqtt.h:316

[mqtt\_evt::result](structmqtt__evt.md#aa1a4304d4aa70440ba630f3fe5e76d2f)

int result

Event result.

**Definition** mqtt.h:324

[mqtt\_evt::param](structmqtt__evt.md#aca1085171667c46b2438f66d9227e07c)

union mqtt\_evt\_param param

Contains parameters (if any) accompanying the event.

**Definition** mqtt.h:319

[mqtt\_internal](structmqtt__internal.md)

MQTT internal state.

**Definition** mqtt.h:454

[mqtt\_internal::rx\_buf\_datalen](structmqtt__internal.md#a45aeafd71dadaf1d0fd0bc3969c921de)

uint32\_t rx\_buf\_datalen

Internal.

**Definition** mqtt.h:467

[mqtt\_internal::last\_activity](structmqtt__internal.md#a8f30cb1440efecf8ae8fc448e4f462f8)

uint32\_t last\_activity

Internal.

**Definition** mqtt.h:461

[mqtt\_internal::remaining\_payload](structmqtt__internal.md#a921477a9839447f4fe1c823911680c92)

uint32\_t remaining\_payload

Internal.

**Definition** mqtt.h:470

[mqtt\_internal::state](structmqtt__internal.md#acf93a973de5a5430e767e2996f1cd048)

uint32\_t state

Internal.

**Definition** mqtt.h:464

[mqtt\_internal::mutex](structmqtt__internal.md#af866a252b9e18496c8e1627704d8a8b2)

struct sys\_mutex mutex

Internal.

**Definition** mqtt.h:456

[mqtt\_puback\_param](structmqtt__puback__param.md)

Parameters for MQTT publish acknowledgment (PUBACK).

**Definition** mqtt.h:206

[mqtt\_puback\_param::message\_id](structmqtt__puback__param.md#a727b919b853e77e480fb841e74a2dedf)

uint16\_t message\_id

Message id of the PUBLISH message being acknowledged.

**Definition** mqtt.h:208

[mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md)

Parameters for MQTT publish complete (PUBCOMP).

**Definition** mqtt.h:224

[mqtt\_pubcomp\_param::message\_id](structmqtt__pubcomp__param.md#ae8484ad4d62f953ecace6c990002e316)

uint16\_t message\_id

Message id of the PUBREL message being acknowledged.

**Definition** mqtt.h:226

[mqtt\_publish\_message](structmqtt__publish__message.md)

Parameters for a publish message.

**Definition** mqtt.h:186

[mqtt\_publish\_message::payload](structmqtt__publish__message.md#a6cfed92c8f8fb319d3cbf40b956cb94d)

struct mqtt\_binstr payload

Payload on the topic published.

**Definition** mqtt.h:188

[mqtt\_publish\_message::topic](structmqtt__publish__message.md#acf5dba605db61efe68ec29337eea95e9)

struct mqtt\_topic topic

Topic on which data was published.

**Definition** mqtt.h:187

[mqtt\_publish\_param](structmqtt__publish__param.md)

Parameters for a publish message (PUBLISH).

**Definition** mqtt.h:246

[mqtt\_publish\_param::dup\_flag](structmqtt__publish__param.md#a2c2062c2b3ad027d5dfea56cb81c48e7)

uint8\_t dup\_flag

Duplicate flag.

**Definition** mqtt.h:258

[mqtt\_publish\_param::message](structmqtt__publish__param.md#a9841a4fbb30b597a9710863ce6034688)

struct mqtt\_publish\_message message

Messages including topic, QoS and its payload (if any) to be published.

**Definition** mqtt.h:250

[mqtt\_publish\_param::retain\_flag](structmqtt__publish__param.md#a9b2c6fad5bf830276d8d3f6b5ab04210)

uint8\_t retain\_flag

Retain flag.

**Definition** mqtt.h:263

[mqtt\_publish\_param::message\_id](structmqtt__publish__param.md#aac4c6ba605506c183d2d5bdd7e550b3e)

uint16\_t message\_id

Message id used for the publish message.

**Definition** mqtt.h:253

[mqtt\_pubrec\_param](structmqtt__pubrec__param.md)

Parameters for MQTT publish receive (PUBREC).

**Definition** mqtt.h:212

[mqtt\_pubrec\_param::message\_id](structmqtt__pubrec__param.md#ab0f92884dbd6e63894210ff7f57fe62c)

uint16\_t message\_id

Message id of the PUBLISH message being acknowledged.

**Definition** mqtt.h:214

[mqtt\_pubrel\_param](structmqtt__pubrel__param.md)

Parameters for MQTT publish release (PUBREL).

**Definition** mqtt.h:218

[mqtt\_pubrel\_param::message\_id](structmqtt__pubrel__param.md#a4333fba7ac37d5a68fe921453b56b572)

uint16\_t message\_id

Message id of the PUBREC message being acknowledged.

**Definition** mqtt.h:220

[mqtt\_sec\_config](structmqtt__sec__config.md)

TLS configuration for secure MQTT transports.

**Definition** mqtt.h:341

[mqtt\_sec\_config::peer\_verify](structmqtt__sec__config.md#a0e04768b6589823464c2d13c31230cad)

int peer\_verify

Indicates the preference for peer verification.

**Definition** mqtt.h:343

[mqtt\_sec\_config::cipher\_list](structmqtt__sec__config.md#a179a97d56a7a12d5afb60257a67ce46c)

const int \* cipher\_list

Indicates the list of ciphers to be used for the session.

**Definition** mqtt.h:351

[mqtt\_sec\_config::cipher\_count](structmqtt__sec__config.md#a25415e32e00808fb6a24187f4234059f)

uint32\_t cipher\_count

Indicates the number of entries in the cipher list.

**Definition** mqtt.h:346

[mqtt\_sec\_config::cert\_nocopy](structmqtt__sec__config.md#a5beac5704fec3e399e5c0099a57ce115)

int cert\_nocopy

Indicates the preference for copying certificates to the heap.

**Definition** mqtt.h:365

[mqtt\_sec\_config::sec\_tag\_count](structmqtt__sec__config.md#a6d59afc061a749ea31f5bd415918a3e0)

uint32\_t sec\_tag\_count

Indicates the number of entries in the sec tag list.

**Definition** mqtt.h:354

[mqtt\_sec\_config::sec\_tag\_list](structmqtt__sec__config.md#adeb8630a9e73c4b3226afa1c9a5060fe)

const sec\_tag\_t \* sec\_tag\_list

Indicates the list of security tags to be used for the session.

**Definition** mqtt.h:357

[mqtt\_sec\_config::hostname](structmqtt__sec__config.md#af7a0ee827bf98fde264000f4c9020c15)

const char \* hostname

Peer hostname for ceritificate verification.

**Definition** mqtt.h:362

[mqtt\_suback\_param](structmqtt__suback__param.md)

Parameters for MQTT subscription acknowledgment (SUBACK).

**Definition** mqtt.h:230

[mqtt\_suback\_param::return\_codes](structmqtt__suback__param.md#a94ef5183aa3438db0521f445650c5868)

struct mqtt\_binstr return\_codes

Return codes indicating maximum QoS level granted for each topic in the subscription list.

**Definition** mqtt.h:236

[mqtt\_suback\_param::message\_id](structmqtt__suback__param.md#a985b53444e7b2c10ab68844fcee34ee4)

uint16\_t message\_id

Message id of the SUBSCRIBE message being acknowledged.

**Definition** mqtt.h:232

[mqtt\_subscription\_list](structmqtt__subscription__list.md)

List of topics in a subscription request.

**Definition** mqtt.h:267

[mqtt\_subscription\_list::message\_id](structmqtt__subscription__list.md#a0667dcd4bd5eb5fe1b13b4df1bf2c26f)

uint16\_t message\_id

Message id used to identify subscription request.

**Definition** mqtt.h:275

[mqtt\_subscription\_list::list\_count](structmqtt__subscription__list.md#aa44e0af3526ee0424627bb24a90ea6b1)

uint16\_t list\_count

Number of topics in the subscription list.

**Definition** mqtt.h:272

[mqtt\_subscription\_list::list](structmqtt__subscription__list.md#ae9db5f602e3c649b1ccc180aef6c4b4e)

struct mqtt\_topic \* list

Array containing topics along with QoS for each.

**Definition** mqtt.h:269

[mqtt\_topic](structmqtt__topic.md)

Abstracts MQTT UTF-8 encoded topic that can be subscribed to or published.

**Definition** mqtt.h:175

[mqtt\_topic::qos](structmqtt__topic.md#a780e90d62c094557bd3918de3b3921e6)

uint8\_t qos

Quality of service requested for the subscription.

**Definition** mqtt.h:182

[mqtt\_topic::topic](structmqtt__topic.md#ab859d08baf88e6a1ac5135e1e55158d5)

struct mqtt\_utf8 topic

Topic on to be published or subscribed to.

**Definition** mqtt.h:177

[mqtt\_transport](structmqtt__transport.md)

MQTT transport specific data.

**Definition** mqtt.h:398

[mqtt\_transport::sock](structmqtt__transport.md#a3b4589dd05394589e7af460761b800bf)

int sock

Socket descriptor.

**Definition** mqtt.h:409

[mqtt\_transport::type](structmqtt__transport.md#a47b49927c79e67b202112c68b53d83f4)

enum mqtt\_transport\_type type

Transport type selection for client instance.

**Definition** mqtt.h:403

[mqtt\_transport::tcp](structmqtt__transport.md#aa24b42579c13104c8660efc764f0b8f2)

struct mqtt\_transport::@142223201017206201250124032135157075026165211271::@247227174316354166044343243236340014224120252320 tcp

[mqtt\_unsuback\_param](structmqtt__unsuback__param.md)

Parameters for MQTT unsubscribe acknowledgment (UNSUBACK).

**Definition** mqtt.h:240

[mqtt\_unsuback\_param::message\_id](structmqtt__unsuback__param.md#aa453177181e07cd0532b8cf591be0f32)

uint16\_t message\_id

Message id of the UNSUBSCRIBE message being acknowledged.

**Definition** mqtt.h:242

[mqtt\_utf8](structmqtt__utf8.md)

Abstracts UTF-8 encoded strings.

**Definition** mqtt.h:149

[mqtt\_utf8::size](structmqtt__utf8.md#a2376f943335326dae74c798141326b70)

uint32\_t size

Size of UTF string, in bytes.

**Definition** mqtt.h:151

[mqtt\_utf8::utf8](structmqtt__utf8.md#a69a949e3c9cb1794f8d28091601eba16)

const uint8\_t \* utf8

Pointer to UTF-8 string.

**Definition** mqtt.h:150

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

[sys\_mutex](structsys__mutex.md)

**Definition** mutex.h:28

[tls\_credentials.h](tls__credentials_8h.md)

TLS credentials management.

[mqtt\_evt\_param](unionmqtt__evt__param.md)

Defines event parameters notified along with asynchronous events to the application.

**Definition** mqtt.h:282

[mqtt\_evt\_param::pubrel](unionmqtt__evt__param.md#a2269e07f580fb65df5f3d0832aa6b3af)

struct mqtt\_pubrel\_param pubrel

Parameters accompanying MQTT\_EVT\_PUBREL event.

**Definition** mqtt.h:301

[mqtt\_evt\_param::puback](unionmqtt__evt__param.md#a24bf756db9fa8cc67c0b02c4e2cb602c)

struct mqtt\_puback\_param puback

Parameters accompanying MQTT\_EVT\_PUBACK event.

**Definition** mqtt.h:295

[mqtt\_evt\_param::pubrec](unionmqtt__evt__param.md#a3b31e1d94c480b8d0244cc12d1c25524)

struct mqtt\_pubrec\_param pubrec

Parameters accompanying MQTT\_EVT\_PUBREC event.

**Definition** mqtt.h:298

[mqtt\_evt\_param::publish](unionmqtt__evt__param.md#a41be40873e1ebb9bf6fbf6dc9566d6ff)

struct mqtt\_publish\_param publish

Parameters accompanying MQTT\_EVT\_PUBLISH event.

**Definition** mqtt.h:292

[mqtt\_evt\_param::connack](unionmqtt__evt__param.md#aa99a77bbade75b3f450088b32131f87a)

struct mqtt\_connack\_param connack

Parameters accompanying MQTT\_EVT\_CONNACK event.

**Definition** mqtt.h:284

[mqtt\_evt\_param::pubcomp](unionmqtt__evt__param.md#ac3d564095019ccf57c10678a433bc31a)

struct mqtt\_pubcomp\_param pubcomp

Parameters accompanying MQTT\_EVT\_PUBCOMP event.

**Definition** mqtt.h:304

[mqtt\_evt\_param::unsuback](unionmqtt__evt__param.md#ad040b028ed0aaabcaddedc204fb709d8)

struct mqtt\_unsuback\_param unsuback

Parameters accompanying MQTT\_EVT\_UNSUBACK event.

**Definition** mqtt.h:310

[mqtt\_evt\_param::suback](unionmqtt__evt__param.md#af6ce2426884d2faa443b3dfdaa45594c)

struct mqtt\_suback\_param suback

Parameters accompanying MQTT\_EVT\_SUBACK event.

**Definition** mqtt.h:307

[websocket.h](websocket_8h.md)

Websocket API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mqtt.h](mqtt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
