---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/chat_8h_source.html
original_path: doxygen/html/chat_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

chat.h

[Go to the documentation of this file.](chat_8h.md)

1/\*

2 \* Copyright (c) 2022 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/kernel.h](kernel_8h.md)>

8#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

9#include <[zephyr/device.h](device_8h.md)>

10#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

11

12#include <[zephyr/modem/pipe.h](pipe_8h.md)>

13#include <[zephyr/modem/stats.h](modem_2stats_8h.md)>

14

15#ifndef ZEPHYR\_MODEM\_CHAT\_

16#define ZEPHYR\_MODEM\_CHAT\_

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

22struct [modem\_chat](structmodem__chat.md);

23

[ 32](chat_8h.md#ae689e92c91d414f968267e290e5246bd)typedef void (\*[modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd))(struct [modem\_chat](structmodem__chat.md) \*chat, char \*\*[argv](structmodem__chat.md#ae7a2d23e34f95d3c3c5d5df15af1571a), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [argc](structmodem__chat.md#ad08436ccb8308912a6d45b3b11cc0c59),

33 void \*[user\_data](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da));

34

[ 38](structmodem__chat__match.md)struct [modem\_chat\_match](structmodem__chat__match.md) {

[ 40](structmodem__chat__match.md#ad1bed20d70285a465663d9babc3fb3e2) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[match](structmodem__chat__match.md#ad1bed20d70285a465663d9babc3fb3e2);

[ 42](structmodem__chat__match.md#afe00a3c87a68d9f7f889f7a0d3cc4150) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [match\_size](structmodem__chat__match.md#afe00a3c87a68d9f7f889f7a0d3cc4150);

[ 44](structmodem__chat__match.md#a7fd423890bea11c65f326ace831233fc) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[separators](structmodem__chat__match.md#a7fd423890bea11c65f326ace831233fc);

[ 46](structmodem__chat__match.md#a7c80555e1bf33504cef7be6c0f9db383) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [separators\_size](structmodem__chat__match.md#a7c80555e1bf33504cef7be6c0f9db383);

[ 48](structmodem__chat__match.md#adb8c0ee17d317192432198949d116259) bool [wildcards](structmodem__chat__match.md#adb8c0ee17d317192432198949d116259);

[ 50](structmodem__chat__match.md#aa7f414d867fdcb2f34a9e4bd3c9b0eeb) bool [partial](structmodem__chat__match.md#aa7f414d867fdcb2f34a9e4bd3c9b0eeb);

[ 52](structmodem__chat__match.md#a11f6e35cd2fd2166ac95adace6ec5c54) [modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd) [callback](structmodem__chat__match.md#a11f6e35cd2fd2166ac95adace6ec5c54);

53};

54

[ 55](chat_8h.md#a078fd13acc9abcc0e0aa0304e6a8537a)#define MODEM\_CHAT\_MATCH(\_match, \_separators, \_callback) \

56 { \

57 .match = (uint8\_t \*)(\_match), .match\_size = (uint8\_t)(sizeof(\_match) - 1), \

58 .separators = (uint8\_t \*)(\_separators), \

59 .separators\_size = (uint8\_t)(sizeof(\_separators) - 1), .wildcards = false, \

60 .callback = \_callback, \

61 }

62

[ 63](chat_8h.md#a02b06e0d97df03b32eb6c40e91f91fd8)#define MODEM\_CHAT\_MATCH\_WILDCARD(\_match, \_separators, \_callback) \

64 { \

65 .match = (uint8\_t \*)(\_match), .match\_size = (uint8\_t)(sizeof(\_match) - 1), \

66 .separators = (uint8\_t \*)(\_separators), \

67 .separators\_size = (uint8\_t)(sizeof(\_separators) - 1), .wildcards = true, \

68 .callback = \_callback, \

69 }

70

[ 71](chat_8h.md#aa62ca91615d0b93b0d2adbcf6c78e251)#define MODEM\_CHAT\_MATCH\_INITIALIZER(\_match, \_separators, \_callback, \_wildcards, \_partial) \

72 { \

73 .match = (uint8\_t \*)(\_match), \

74 .match\_size = (uint8\_t)(sizeof(\_match) - 1), \

75 .separators = (uint8\_t \*)(\_separators), \

76 .separators\_size = (uint8\_t)(sizeof(\_separators) - 1), \

77 .wildcards = \_wildcards, \

78 .partial = \_partial, \

79 .callback = \_callback, \

80 }

81

[ 82](chat_8h.md#a926b0d2993eb8158137e2caa7687abb8)#define MODEM\_CHAT\_MATCH\_DEFINE(\_sym, \_match, \_separators, \_callback) \

83 const static struct modem\_chat\_match \_sym = MODEM\_CHAT\_MATCH(\_match, \_separators, \_callback)

84

85/\* Helper struct to match any response without callback. \*/

86extern const struct [modem\_chat\_match](structmodem__chat__match.md) [modem\_chat\_any\_match](chat_8h.md#ada2cd7e12d9a37af6f13ecfb6c182176);

87

[ 88](chat_8h.md#a216094ddd94351fadf0e84bacbadc84e)#define MODEM\_CHAT\_MATCHES\_DEFINE(\_sym, ...) \

89 const static struct modem\_chat\_match \_sym[] = {\_\_VA\_ARGS\_\_}

90

91/\* Helper struct to match nothing. \*/

92extern const struct [modem\_chat\_match](structmodem__chat__match.md) [modem\_chat\_empty\_matches](chat_8h.md#ac94a45b118b155ca7de1a45d12297ae4)[0];

93

[ 97](structmodem__chat__script__chat.md)struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) {

[ 99](structmodem__chat__script__chat.md#a92c038d56623b4f4b26c64b537e7ce8a) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[request](structmodem__chat__script__chat.md#a92c038d56623b4f4b26c64b537e7ce8a);

[ 101](structmodem__chat__script__chat.md#ad87948ff4e6441c118ee269bf6458aa0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [request\_size](structmodem__chat__script__chat.md#ad87948ff4e6441c118ee269bf6458aa0);

[ 103](structmodem__chat__script__chat.md#a5cab9c3a31624c8ffb490b70285f86ee) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[response\_matches](structmodem__chat__script__chat.md#a5cab9c3a31624c8ffb490b70285f86ee);

[ 105](structmodem__chat__script__chat.md#afaaa9a7bc1842dfb65156fff2d91cfa0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [response\_matches\_size](structmodem__chat__script__chat.md#afaaa9a7bc1842dfb65156fff2d91cfa0);

[ 107](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268);

108};

109

[ 110](chat_8h.md#a01c94aa4a5881f2f4bdc004d08abaf0d)#define MODEM\_CHAT\_SCRIPT\_CMD\_RESP(\_request, \_response\_match) \

111 { \

112 .request = (uint8\_t \*)(\_request), \

113 .request\_size = (uint16\_t)(sizeof(\_request) - 1), \

114 .response\_matches = &\_response\_match, \

115 .response\_matches\_size = 1, \

116 .timeout = 0, \

117 }

118

[ 119](chat_8h.md#add48fe039151f5596e5208cccd170746)#define MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_MULT(\_request, \_response\_matches) \

120 { \

121 .request = (uint8\_t \*)(\_request), \

122 .request\_size = (uint16\_t)(sizeof(\_request) - 1), \

123 .response\_matches = \_response\_matches, \

124 .response\_matches\_size = ARRAY\_SIZE(\_response\_matches), \

125 .timeout = 0, \

126 }

127

[ 128](chat_8h.md#a0a62af922c1ca5aed812ac634e490453)#define MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_NONE(\_request, \_timeout\_ms) \

129 { \

130 .request = (uint8\_t \*)(\_request), \

131 .request\_size = (uint16\_t)(sizeof(\_request) - 1), \

132 .response\_matches = NULL, \

133 .response\_matches\_size = 0, \

134 .timeout = \_timeout\_ms, \

135 }

136

[ 137](chat_8h.md#ab807fffae2007bc03a8e87ba73921888)#define MODEM\_CHAT\_SCRIPT\_CMDS\_DEFINE(\_sym, ...) \

138 const struct modem\_chat\_script\_chat \_sym[] = {\_\_VA\_ARGS\_\_}

139

140/\* Helper struct to have no chat script command. \*/

141extern const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) [modem\_chat\_empty\_script\_chats](chat_8h.md#a19cd30454fb4eb9293e87b24a8cf0655)[0];

142

[ 143](chat_8h.md#a4035be227ddec8424311575305647d3e)enum [modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e) {

[ 144](chat_8h.md#a4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee) [MODEM\_CHAT\_SCRIPT\_RESULT\_SUCCESS](chat_8h.md#a4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee),

[ 145](chat_8h.md#a4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b) [MODEM\_CHAT\_SCRIPT\_RESULT\_ABORT](chat_8h.md#a4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b),

[ 146](chat_8h.md#a4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e) [MODEM\_CHAT\_SCRIPT\_RESULT\_TIMEOUT](chat_8h.md#a4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e)

147};

148

[ 156](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e)typedef void (\*[modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e))(struct [modem\_chat](structmodem__chat.md) \*chat,

157 enum [modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e) result, void \*[user\_data](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da));

158

[ 162](structmodem__chat__script.md)struct [modem\_chat\_script](structmodem__chat__script.md) {

[ 164](structmodem__chat__script.md#aca3b75a494273d8c06cf943153dd7dc8) const char \*[name](structmodem__chat__script.md#aca3b75a494273d8c06cf943153dd7dc8);

[ 166](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114) const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*[script\_chats](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114);

[ 168](structmodem__chat__script.md#a3ac30e3ba1842cf53747721592f16cd4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [script\_chats\_size](structmodem__chat__script.md#a3ac30e3ba1842cf53747721592f16cd4);

[ 170](structmodem__chat__script.md#a2b586e1ff80c22d8ff45829f3e2e7b17) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[abort\_matches](structmodem__chat__script.md#a2b586e1ff80c22d8ff45829f3e2e7b17);

[ 172](structmodem__chat__script.md#aa56bdf520b0f385bc6410b2c6aa2e8d4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [abort\_matches\_size](structmodem__chat__script.md#aa56bdf520b0f385bc6410b2c6aa2e8d4);

[ 174](structmodem__chat__script.md#a73f4c3892052f827c10ea466c9a75954) [modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e) [callback](structmodem__chat__script.md#a73f4c3892052f827c10ea466c9a75954);

[ 176](structmodem__chat__script.md#a0b9a9d3d44a8624728e16922cbdfd662) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structmodem__chat__script.md#a0b9a9d3d44a8624728e16922cbdfd662);

177};

178

[ 179](chat_8h.md#ad15f82648a073883c5956d6b14f4e41a)#define MODEM\_CHAT\_SCRIPT\_DEFINE(\_sym, \_script\_chats, \_abort\_matches, \_callback, \_timeout\_s) \

180 const static struct modem\_chat\_script \_sym = { \

181 .name = #\_sym, \

182 .script\_chats = \_script\_chats, \

183 .script\_chats\_size = ARRAY\_SIZE(\_script\_chats), \

184 .abort\_matches = \_abort\_matches, \

185 .abort\_matches\_size = ARRAY\_SIZE(\_abort\_matches), \

186 .callback = \_callback, \

187 .timeout = \_timeout\_s, \

188 }

189

[ 190](chat_8h.md#a7be78a33341512359a1857baaa4ac915)#define MODEM\_CHAT\_SCRIPT\_NO\_ABORT\_DEFINE(\_sym, \_script\_chats, \_callback, \_timeout\_s) \

191 MODEM\_CHAT\_SCRIPT\_DEFINE(\_sym, \_script\_chats, modem\_chat\_empty\_matches, \

192 \_callback, \_timeout\_s)

193

[ 194](chat_8h.md#a16441c0c385874a41b9ac071a67cea1c)#define MODEM\_CHAT\_SCRIPT\_EMPTY\_DEFINE(\_sym) \

195 MODEM\_CHAT\_SCRIPT\_NO\_ABORT\_DEFINE(\_sym, modem\_chat\_empty\_script\_chats, NULL, 0)

196

[ 197](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae)enum [modem\_chat\_script\_send\_state](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae) {

198 /\* No data to send \*/

[ 199](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974) [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_IDLE](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974),

200 /\* Sending request \*/

[ 201](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd) [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_REQUEST](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd),

202 /\* Sending delimiter \*/

[ 203](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aeaaf1d0f61d85bc5fbb77a979efe9b1aaf) [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_DELIMITER](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aeaaf1d0f61d85bc5fbb77a979efe9b1aaf),

204};

205

[ 210](structmodem__chat.md)struct [modem\_chat](structmodem__chat.md) {

211 /\* Pipe used to send and receive data \*/

[ 212](structmodem__chat.md#a9bec3daf58728d27a554d228452a8fa9) struct modem\_pipe \*[pipe](structmodem__chat.md#a9bec3daf58728d27a554d228452a8fa9);

213

214 /\* User data passed with match callbacks \*/

[ 215](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da) void \*[user\_data](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da);

216

217 /\* Receive buffer \*/

[ 218](structmodem__chat.md#af2ac2cf3efac415af72b702a1ec62ae7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__chat.md#af2ac2cf3efac415af72b702a1ec62ae7);

[ 219](structmodem__chat.md#a962b245335979eeb782410ba6429b4e6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__chat.md#a962b245335979eeb782410ba6429b4e6);

[ 220](structmodem__chat.md#ae15c5238e6e04a4f94a27e779d3f2a30) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_len](structmodem__chat.md#ae15c5238e6e04a4f94a27e779d3f2a30);

221

222 /\* Work buffer \*/

[ 223](structmodem__chat.md#a5b3667c1e409fdc5382af75ad1329df9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [work\_buf](structmodem__chat.md#a5b3667c1e409fdc5382af75ad1329df9)[32];

[ 224](structmodem__chat.md#a9acd26d97eec7c48482063a3c558c717) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [work\_buf\_len](structmodem__chat.md#a9acd26d97eec7c48482063a3c558c717);

225

226 /\* Chat delimiter \*/

[ 227](structmodem__chat.md#aa8d3d31dc6eaf676c03fad034597ad91) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[delimiter](structmodem__chat.md#aa8d3d31dc6eaf676c03fad034597ad91);

[ 228](structmodem__chat.md#a14104456f6e4b8c36b38eb232fb36996) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [delimiter\_size](structmodem__chat.md#a14104456f6e4b8c36b38eb232fb36996);

[ 229](structmodem__chat.md#ae5fe73d09b6fad3302e84ca841ad65ca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [delimiter\_match\_len](structmodem__chat.md#ae5fe73d09b6fad3302e84ca841ad65ca);

230

231 /\* Array of bytes which are discarded out by parser \*/

[ 232](structmodem__chat.md#adcb6a8d9fdb9b7c0e950d64ec4b0853c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[filter](structmodem__chat.md#adcb6a8d9fdb9b7c0e950d64ec4b0853c);

[ 233](structmodem__chat.md#a199b2c9e9c6fd41e81ef6bca138b6328) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [filter\_size](structmodem__chat.md#a199b2c9e9c6fd41e81ef6bca138b6328);

234

235 /\* Parsed arguments \*/

[ 236](structmodem__chat.md#ae7a2d23e34f95d3c3c5d5df15af1571a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*[argv](structmodem__chat.md#ae7a2d23e34f95d3c3c5d5df15af1571a);

[ 237](structmodem__chat.md#ac1c71497eb22137bc4a03877b6f30b37) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [argv\_size](structmodem__chat.md#ac1c71497eb22137bc4a03877b6f30b37);

[ 238](structmodem__chat.md#ad08436ccb8308912a6d45b3b11cc0c59) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [argc](structmodem__chat.md#ad08436ccb8308912a6d45b3b11cc0c59);

239

240 /\* Matches

241 \* Index 0 -> Response matches

242 \* Index 1 -> Abort matches

243 \* Index 2 -> Unsolicited matches

244 \*/

[ 245](structmodem__chat.md#ac16520e4e7031bbc2162d29728eb86d2) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[matches](structmodem__chat.md#ac16520e4e7031bbc2162d29728eb86d2)[3];

[ 246](structmodem__chat.md#a249bc37382bddf11bfcabef834a19f2a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [matches\_size](structmodem__chat.md#a249bc37382bddf11bfcabef834a19f2a)[3];

247

248 /\* Script execution \*/

[ 249](structmodem__chat.md#a7c181f6c68809379d756080729e1e3a1) const struct [modem\_chat\_script](structmodem__chat__script.md) \*[script](structmodem__chat.md#a7c181f6c68809379d756080729e1e3a1);

[ 250](structmodem__chat.md#abff96c9a7bd215f20fece3d6f96899b5) const struct [modem\_chat\_script](structmodem__chat__script.md) \*[pending\_script](structmodem__chat.md#abff96c9a7bd215f20fece3d6f96899b5);

[ 251](structmodem__chat.md#a44f303f7ec2aa304de5ba0e1249bff35) struct [k\_work](structk__work.md) [script\_run\_work](structmodem__chat.md#a44f303f7ec2aa304de5ba0e1249bff35);

[ 252](structmodem__chat.md#ada952e3176a7f2645ff7b64ca32cb29e) struct [k\_work\_delayable](structk__work__delayable.md) [script\_timeout\_work](structmodem__chat.md#ada952e3176a7f2645ff7b64ca32cb29e);

[ 253](structmodem__chat.md#ae8df85a6e2c27f720e8f7f993e7d6a75) struct [k\_work](structk__work.md) [script\_abort\_work](structmodem__chat.md#ae8df85a6e2c27f720e8f7f993e7d6a75);

[ 254](structmodem__chat.md#aa09d879afc7f69901799d564c3951c7b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [script\_chat\_it](structmodem__chat.md#aa09d879afc7f69901799d564c3951c7b);

[ 255](structmodem__chat.md#af55e1bf861e72b497230c92b4a673f4c) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [script\_state](structmodem__chat.md#af55e1bf861e72b497230c92b4a673f4c);

[ 256](structmodem__chat.md#a8560fa2c2d26366ed27d8ca4620f30ff) enum [modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e) [script\_result](structmodem__chat.md#a8560fa2c2d26366ed27d8ca4620f30ff);

[ 257](structmodem__chat.md#aa365a6e40ec8de9e2a74c035dff0c203) struct k\_sem [script\_stopped\_sem](structmodem__chat.md#aa365a6e40ec8de9e2a74c035dff0c203);

258

259 /\* Script sending \*/

[ 260](structmodem__chat.md#a9fc3fc3f5d2285d12ecad12e21e5be13) enum [modem\_chat\_script\_send\_state](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae) [script\_send\_state](structmodem__chat.md#a9fc3fc3f5d2285d12ecad12e21e5be13);

[ 261](structmodem__chat.md#a36fb50970ebd8eb041506c913648be6c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [script\_send\_pos](structmodem__chat.md#a36fb50970ebd8eb041506c913648be6c);

[ 262](structmodem__chat.md#a5260f843646e401159fd5f13015e9db6) struct [k\_work](structk__work.md) [script\_send\_work](structmodem__chat.md#a5260f843646e401159fd5f13015e9db6);

[ 263](structmodem__chat.md#a37ae5aeeaaeba6e50d7d9f0df6ff2870) struct [k\_work\_delayable](structk__work__delayable.md) [script\_send\_timeout\_work](structmodem__chat.md#a37ae5aeeaaeba6e50d7d9f0df6ff2870);

264

265 /\* Match parsing \*/

[ 266](structmodem__chat.md#a42d6fe9641db254459498d26b05ce152) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[parse\_match](structmodem__chat.md#a42d6fe9641db254459498d26b05ce152);

[ 267](structmodem__chat.md#ae14032ba980271ea758278d4bd8cca30) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [parse\_match\_len](structmodem__chat.md#ae14032ba980271ea758278d4bd8cca30);

[ 268](structmodem__chat.md#a2e2555e463d6dffb5ed6531ad8a822ca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [parse\_arg\_len](structmodem__chat.md#a2e2555e463d6dffb5ed6531ad8a822ca);

[ 269](structmodem__chat.md#ae4063127d0a802801660f08a1f403121) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [parse\_match\_type](structmodem__chat.md#ae4063127d0a802801660f08a1f403121);

270

271 /\* Process received data \*/

[ 272](structmodem__chat.md#a4558d8dc063f0330bdb4d203e2af6907) struct [k\_work](structk__work.md) [receive\_work](structmodem__chat.md#a4558d8dc063f0330bdb4d203e2af6907);

273

274 /\* Statistics \*/

275#if CONFIG\_MODEM\_STATS

276 struct modem\_stats\_buffer receive\_buf\_stats;

277 struct modem\_stats\_buffer work\_buf\_stats;

278#endif

279};

280

[ 284](structmodem__chat__config.md)struct [modem\_chat\_config](structmodem__chat__config.md) {

[ 286](structmodem__chat__config.md#ac002d9f43309db8c3c35826127d94194) void \*[user\_data](structmodem__chat__config.md#ac002d9f43309db8c3c35826127d94194);

[ 288](structmodem__chat__config.md#a295de98c2e8866059e7194c57d0502b7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__chat__config.md#a295de98c2e8866059e7194c57d0502b7);

[ 290](structmodem__chat__config.md#a76f85951f5750f0d07b1253af118ec6f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__chat__config.md#a76f85951f5750f0d07b1253af118ec6f);

[ 292](structmodem__chat__config.md#ab3adfaddd56884553a57467c762bdf98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[delimiter](structmodem__chat__config.md#ab3adfaddd56884553a57467c762bdf98);

[ 294](structmodem__chat__config.md#aa30ccfd372c47c64e2a7b7c840405499) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [delimiter\_size](structmodem__chat__config.md#aa30ccfd372c47c64e2a7b7c840405499);

[ 296](structmodem__chat__config.md#af6646dee93b3279429eb95c87426168b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[filter](structmodem__chat__config.md#af6646dee93b3279429eb95c87426168b);

[ 298](structmodem__chat__config.md#af762b783d33e192ef45647e0b2e2d70b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_size](structmodem__chat__config.md#af762b783d33e192ef45647e0b2e2d70b);

[ 300](structmodem__chat__config.md#ae2afa6465bfad9c83dd57498165888b4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*[argv](structmodem__chat__config.md#ae2afa6465bfad9c83dd57498165888b4);

[ 302](structmodem__chat__config.md#a2cf551a0946459b2825595026ebc7490) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [argv\_size](structmodem__chat__config.md#a2cf551a0946459b2825595026ebc7490);

[ 304](structmodem__chat__config.md#a661d96b8a7031b17e6f660c6e0e4be11) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[unsol\_matches](structmodem__chat__config.md#a661d96b8a7031b17e6f660c6e0e4be11);

[ 306](structmodem__chat__config.md#addfa7cacc676190d9e29c451d47ea3bd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unsol\_matches\_size](structmodem__chat__config.md#addfa7cacc676190d9e29c451d47ea3bd);

307};

308

[ 315](chat_8h.md#af79f3b0e67b5777876137b9e3e16d985)int [modem\_chat\_init](chat_8h.md#af79f3b0e67b5777876137b9e3e16d985)(struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_config](structmodem__chat__config.md) \*config);

316

[ 325](chat_8h.md#af91ae4e64113188e7049a7568a086556)int [modem\_chat\_attach](chat_8h.md#af91ae4e64113188e7049a7568a086556)(struct [modem\_chat](structmodem__chat.md) \*chat, struct modem\_pipe \*pipe);

326

[ 337](chat_8h.md#a397d399703449498171ac898776fe791)int [modem\_chat\_run\_script\_async](chat_8h.md#a397d399703449498171ac898776fe791)(struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_script](structmodem__chat__script.md) \*script);

338

[ 349](chat_8h.md#ae64d151a5f65bde1dd1973393acf3ff1)int [modem\_chat\_run\_script](chat_8h.md#ae64d151a5f65bde1dd1973393acf3ff1)(struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_script](structmodem__chat__script.md) \*script);

350

[ 361](chat_8h.md#aa92ffb91bab15c882cff7b13fca7eeb5)static inline int [modem\_chat\_script\_run](chat_8h.md#aa92ffb91bab15c882cff7b13fca7eeb5)(struct [modem\_chat](structmodem__chat.md) \*chat,

362 const struct [modem\_chat\_script](structmodem__chat__script.md) \*script)

363{

364 return [modem\_chat\_run\_script\_async](chat_8h.md#a397d399703449498171ac898776fe791)(chat, script);

365}

366

[ 371](chat_8h.md#a5ec3918a4beb6b30deecedbd6f6382ee)void [modem\_chat\_script\_abort](chat_8h.md#a5ec3918a4beb6b30deecedbd6f6382ee)(struct [modem\_chat](structmodem__chat.md) \*chat);

372

[ 377](chat_8h.md#a62fa275cb9ce387b0bf5b384c9448c41)void [modem\_chat\_release](chat_8h.md#a62fa275cb9ce387b0bf5b384c9448c41)(struct [modem\_chat](structmodem__chat.md) \*chat);

378

[ 383](chat_8h.md#a1f41fc90f5026dc688a90567278ac175)void [modem\_chat\_match\_init](chat_8h.md#a1f41fc90f5026dc688a90567278ac175)(struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match);

384

[ 394](chat_8h.md#ac9ed985688aeaee96adcb2b6c4285099)int [modem\_chat\_match\_set\_match](chat_8h.md#ac9ed985688aeaee96adcb2b6c4285099)(struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, const char \*[match](structmodem__chat__match.md#ad1bed20d70285a465663d9babc3fb3e2));

395

[ 405](chat_8h.md#a35c1a4f9ed2677fb747025f859eeae56)int [modem\_chat\_match\_set\_separators](chat_8h.md#a35c1a4f9ed2677fb747025f859eeae56)(struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, const char \*[separators](structmodem__chat__match.md#a7fd423890bea11c65f326ace831233fc));

406

[ 412](chat_8h.md#afea28e13817e1daa6bb5c42514542e4e)void [modem\_chat\_match\_set\_callback](chat_8h.md#afea28e13817e1daa6bb5c42514542e4e)(struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match,

413 [modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd) [callback](structmodem__chat__match.md#a11f6e35cd2fd2166ac95adace6ec5c54));

414

[ 420](chat_8h.md#a53cb148e665095d036edc266e778a8ce)void [modem\_chat\_match\_set\_partial](chat_8h.md#a53cb148e665095d036edc266e778a8ce)(struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, bool [partial](structmodem__chat__match.md#aa7f414d867fdcb2f34a9e4bd3c9b0eeb));

421

[ 427](chat_8h.md#a3274b7ffcce059c4d0a5d2ccb3e0bcc6)void [modem\_chat\_match\_enable\_wildcards](chat_8h.md#a3274b7ffcce059c4d0a5d2ccb3e0bcc6)(struct [modem\_chat\_match](structmodem__chat__match.md) \*chat\_match, bool enable);

428

[ 433](chat_8h.md#af12d45cf404e85c94fc13252294c76ca)void [modem\_chat\_script\_chat\_init](chat_8h.md#af12d45cf404e85c94fc13252294c76ca)(struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chat);

434

[ 444](chat_8h.md#adaed8cb3a0933fd15a46344ca0df9930)int [modem\_chat\_script\_chat\_set\_request](chat_8h.md#adaed8cb3a0933fd15a46344ca0df9930)(struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chat,

445 const char \*request);

446

[ 456](chat_8h.md#a2aec485e298ebde8af0372deb9c4784f)int [modem\_chat\_script\_chat\_set\_response\_matches](chat_8h.md#a2aec485e298ebde8af0372deb9c4784f)(struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chat,

457 const struct [modem\_chat\_match](structmodem__chat__match.md) \*response\_matches,

458 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) response\_matches\_size);

459

[ 465](chat_8h.md#ae52a949df85cbcb7729c88917f46ef8d)void [modem\_chat\_script\_chat\_set\_timeout](chat_8h.md#ae52a949df85cbcb7729c88917f46ef8d)(struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chat,

466 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) timeout\_ms);

467

[ 472](chat_8h.md#afdca5529d3ae3c982f3577560216e309)void [modem\_chat\_script\_init](chat_8h.md#afdca5529d3ae3c982f3577560216e309)(struct [modem\_chat\_script](structmodem__chat__script.md) \*script);

473

[ 480](chat_8h.md#a9ab3fa018ee0b2ebaacb3d74ee7ce29a)void [modem\_chat\_script\_set\_name](chat_8h.md#a9ab3fa018ee0b2ebaacb3d74ee7ce29a)(struct [modem\_chat\_script](structmodem__chat__script.md) \*script, const char \*name);

481

[ 491](chat_8h.md#ad6b669708d24a3d3d91d1c40c2c504c8)int [modem\_chat\_script\_set\_script\_chats](chat_8h.md#ad6b669708d24a3d3d91d1c40c2c504c8)(struct [modem\_chat\_script](structmodem__chat__script.md) \*script,

492 const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*script\_chats,

493 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) script\_chats\_size);

494

[ 504](chat_8h.md#a9bff858315a05324ff9690bdbce7398f)int [modem\_chat\_script\_set\_abort\_matches](chat_8h.md#a9bff858315a05324ff9690bdbce7398f)(struct [modem\_chat\_script](structmodem__chat__script.md) \*script,

505 const struct [modem\_chat\_match](structmodem__chat__match.md) \*abort\_matches,

506 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) abort\_matches\_size);

507

[ 513](chat_8h.md#a4389d813db136c199c872f20a125eba2)void [modem\_chat\_script\_set\_callback](chat_8h.md#a4389d813db136c199c872f20a125eba2)(struct [modem\_chat\_script](structmodem__chat__script.md) \*script,

514 [modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e) [callback](structmodem__chat__match.md#a11f6e35cd2fd2166ac95adace6ec5c54));

515

[ 521](chat_8h.md#a9180fa670c3b6e88fa6011fdce5fd909)void [modem\_chat\_script\_set\_timeout](chat_8h.md#a9180fa670c3b6e88fa6011fdce5fd909)(struct [modem\_chat\_script](structmodem__chat__script.md) \*script, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout\_s);

522

523#ifdef \_\_cplusplus

524}

525#endif

526

527#endif /\* ZEPHYR\_MODEM\_CHAT\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[modem\_chat\_empty\_script\_chats](chat_8h.md#a19cd30454fb4eb9293e87b24a8cf0655)

const struct modem\_chat\_script\_chat modem\_chat\_empty\_script\_chats[0]

[modem\_chat\_match\_init](chat_8h.md#a1f41fc90f5026dc688a90567278ac175)

void modem\_chat\_match\_init(struct modem\_chat\_match \*chat\_match)

Initialize modem chat match.

[modem\_chat\_script\_chat\_set\_response\_matches](chat_8h.md#a2aec485e298ebde8af0372deb9c4784f)

int modem\_chat\_script\_chat\_set\_response\_matches(struct modem\_chat\_script\_chat \*script\_chat, const struct modem\_chat\_match \*response\_matches, uint16\_t response\_matches\_size)

Set modem chat script chat matches.

[modem\_chat\_match\_enable\_wildcards](chat_8h.md#a3274b7ffcce059c4d0a5d2ccb3e0bcc6)

void modem\_chat\_match\_enable\_wildcards(struct modem\_chat\_match \*chat\_match, bool enable)

Set modem chat match wildcards flag.

[modem\_chat\_match\_set\_separators](chat_8h.md#a35c1a4f9ed2677fb747025f859eeae56)

int modem\_chat\_match\_set\_separators(struct modem\_chat\_match \*chat\_match, const char \*separators)

Set separators of modem chat match instance.

[modem\_chat\_run\_script\_async](chat_8h.md#a397d399703449498171ac898776fe791)

int modem\_chat\_run\_script\_async(struct modem\_chat \*chat, const struct modem\_chat\_script \*script)

Run script asynchronously.

[modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e)

modem\_chat\_script\_result

**Definition** chat.h:143

[MODEM\_CHAT\_SCRIPT\_RESULT\_TIMEOUT](chat_8h.md#a4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e)

@ MODEM\_CHAT\_SCRIPT\_RESULT\_TIMEOUT

**Definition** chat.h:146

[MODEM\_CHAT\_SCRIPT\_RESULT\_SUCCESS](chat_8h.md#a4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee)

@ MODEM\_CHAT\_SCRIPT\_RESULT\_SUCCESS

**Definition** chat.h:144

[MODEM\_CHAT\_SCRIPT\_RESULT\_ABORT](chat_8h.md#a4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b)

@ MODEM\_CHAT\_SCRIPT\_RESULT\_ABORT

**Definition** chat.h:145

[modem\_chat\_script\_set\_callback](chat_8h.md#a4389d813db136c199c872f20a125eba2)

void modem\_chat\_script\_set\_callback(struct modem\_chat\_script \*script, modem\_chat\_script\_callback callback)

Set modem chat script callback.

[modem\_chat\_match\_set\_partial](chat_8h.md#a53cb148e665095d036edc266e778a8ce)

void modem\_chat\_match\_set\_partial(struct modem\_chat\_match \*chat\_match, bool partial)

Set modem chat match partial flag.

[modem\_chat\_script\_abort](chat_8h.md#a5ec3918a4beb6b30deecedbd6f6382ee)

void modem\_chat\_script\_abort(struct modem\_chat \*chat)

Abort script.

[modem\_chat\_release](chat_8h.md#a62fa275cb9ce387b0bf5b384c9448c41)

void modem\_chat\_release(struct modem\_chat \*chat)

Release pipe from chat instance.

[modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e)

void(\* modem\_chat\_script\_callback)(struct modem\_chat \*chat, enum modem\_chat\_script\_result result, void \*user\_data)

Callback called when script chat is received.

**Definition** chat.h:156

[modem\_chat\_script\_send\_state](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae)

modem\_chat\_script\_send\_state

**Definition** chat.h:197

[MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_REQUEST](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd)

@ MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_REQUEST

**Definition** chat.h:201

[MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_IDLE](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974)

@ MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_IDLE

**Definition** chat.h:199

[MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_DELIMITER](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aeaaf1d0f61d85bc5fbb77a979efe9b1aaf)

@ MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_DELIMITER

**Definition** chat.h:203

[modem\_chat\_script\_set\_timeout](chat_8h.md#a9180fa670c3b6e88fa6011fdce5fd909)

void modem\_chat\_script\_set\_timeout(struct modem\_chat\_script \*script, uint32\_t timeout\_s)

Set modem chat script timeout.

[modem\_chat\_script\_set\_name](chat_8h.md#a9ab3fa018ee0b2ebaacb3d74ee7ce29a)

void modem\_chat\_script\_set\_name(struct modem\_chat\_script \*script, const char \*name)

Set modem chat script name.

[modem\_chat\_script\_set\_abort\_matches](chat_8h.md#a9bff858315a05324ff9690bdbce7398f)

int modem\_chat\_script\_set\_abort\_matches(struct modem\_chat\_script \*script, const struct modem\_chat\_match \*abort\_matches, uint16\_t abort\_matches\_size)

Set modem chat script abort matches.

[modem\_chat\_script\_run](chat_8h.md#aa92ffb91bab15c882cff7b13fca7eeb5)

static int modem\_chat\_script\_run(struct modem\_chat \*chat, const struct modem\_chat\_script \*script)

Run script asynchronously.

**Definition** chat.h:361

[modem\_chat\_empty\_matches](chat_8h.md#ac94a45b118b155ca7de1a45d12297ae4)

const struct modem\_chat\_match modem\_chat\_empty\_matches[0]

[modem\_chat\_match\_set\_match](chat_8h.md#ac9ed985688aeaee96adcb2b6c4285099)

int modem\_chat\_match\_set\_match(struct modem\_chat\_match \*chat\_match, const char \*match)

Set match of modem chat match instance.

[modem\_chat\_script\_set\_script\_chats](chat_8h.md#ad6b669708d24a3d3d91d1c40c2c504c8)

int modem\_chat\_script\_set\_script\_chats(struct modem\_chat\_script \*script, const struct modem\_chat\_script\_chat \*script\_chats, uint16\_t script\_chats\_size)

Set modem chat script chats.

[modem\_chat\_any\_match](chat_8h.md#ada2cd7e12d9a37af6f13ecfb6c182176)

const struct modem\_chat\_match modem\_chat\_any\_match

[modem\_chat\_script\_chat\_set\_request](chat_8h.md#adaed8cb3a0933fd15a46344ca0df9930)

int modem\_chat\_script\_chat\_set\_request(struct modem\_chat\_script\_chat \*script\_chat, const char \*request)

Set request of modem chat script chat instance.

[modem\_chat\_script\_chat\_set\_timeout](chat_8h.md#ae52a949df85cbcb7729c88917f46ef8d)

void modem\_chat\_script\_chat\_set\_timeout(struct modem\_chat\_script\_chat \*script\_chat, uint16\_t timeout\_ms)

Set modem chat script chat timeout.

[modem\_chat\_run\_script](chat_8h.md#ae64d151a5f65bde1dd1973393acf3ff1)

int modem\_chat\_run\_script(struct modem\_chat \*chat, const struct modem\_chat\_script \*script)

Run script.

[modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd)

void(\* modem\_chat\_match\_callback)(struct modem\_chat \*chat, char \*\*argv, uint16\_t argc, void \*user\_data)

Callback called when matching chat is received.

**Definition** chat.h:32

[modem\_chat\_script\_chat\_init](chat_8h.md#af12d45cf404e85c94fc13252294c76ca)

void modem\_chat\_script\_chat\_init(struct modem\_chat\_script\_chat \*script\_chat)

Initialize modem chat script chat.

[modem\_chat\_init](chat_8h.md#af79f3b0e67b5777876137b9e3e16d985)

int modem\_chat\_init(struct modem\_chat \*chat, const struct modem\_chat\_config \*config)

Initialize modem pipe chat instance.

[modem\_chat\_attach](chat_8h.md#af91ae4e64113188e7049a7568a086556)

int modem\_chat\_attach(struct modem\_chat \*chat, struct modem\_pipe \*pipe)

Attach modem chat instance to pipe.

[modem\_chat\_script\_init](chat_8h.md#afdca5529d3ae3c982f3577560216e309)

void modem\_chat\_script\_init(struct modem\_chat\_script \*script)

Initialize modem chat script.

[modem\_chat\_match\_set\_callback](chat_8h.md#afea28e13817e1daa6bb5c42514542e4e)

void modem\_chat\_match\_set\_callback(struct modem\_chat\_match \*chat\_match, modem\_chat\_match\_callback callback)

Set modem chat match callback.

[device.h](device_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stats.h](modem_2stats_8h.md)

[pipe.h](pipe_8h.md)

[ring\_buffer.h](ring__buffer_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3985

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3957

[modem\_chat\_config](structmodem__chat__config.md)

Chat configuration.

**Definition** chat.h:284

[modem\_chat\_config::receive\_buf](structmodem__chat__config.md#a295de98c2e8866059e7194c57d0502b7)

uint8\_t \* receive\_buf

Receive buffer used to store parsed arguments.

**Definition** chat.h:288

[modem\_chat\_config::argv\_size](structmodem__chat__config.md#a2cf551a0946459b2825595026ebc7490)

uint16\_t argv\_size

Elements in array of pointers.

**Definition** chat.h:302

[modem\_chat\_config::unsol\_matches](structmodem__chat__config.md#a661d96b8a7031b17e6f660c6e0e4be11)

const struct modem\_chat\_match \* unsol\_matches

Array of unsolicited matches.

**Definition** chat.h:304

[modem\_chat\_config::receive\_buf\_size](structmodem__chat__config.md#a76f85951f5750f0d07b1253af118ec6f)

uint16\_t receive\_buf\_size

Size of receive buffer should be longest line + longest match.

**Definition** chat.h:290

[modem\_chat\_config::delimiter\_size](structmodem__chat__config.md#aa30ccfd372c47c64e2a7b7c840405499)

uint8\_t delimiter\_size

Size of delimiter.

**Definition** chat.h:294

[modem\_chat\_config::delimiter](structmodem__chat__config.md#ab3adfaddd56884553a57467c762bdf98)

uint8\_t \* delimiter

Delimiter.

**Definition** chat.h:292

[modem\_chat\_config::user\_data](structmodem__chat__config.md#ac002d9f43309db8c3c35826127d94194)

void \* user\_data

Free to use user data passed with modem match callbacks.

**Definition** chat.h:286

[modem\_chat\_config::unsol\_matches\_size](structmodem__chat__config.md#addfa7cacc676190d9e29c451d47ea3bd)

uint16\_t unsol\_matches\_size

Elements in array of unsolicited matches.

**Definition** chat.h:306

[modem\_chat\_config::argv](structmodem__chat__config.md#ae2afa6465bfad9c83dd57498165888b4)

uint8\_t \*\* argv

Array of pointers used to point to parsed arguments.

**Definition** chat.h:300

[modem\_chat\_config::filter](structmodem__chat__config.md#af6646dee93b3279429eb95c87426168b)

uint8\_t \* filter

Bytes which are discarded by parser.

**Definition** chat.h:296

[modem\_chat\_config::filter\_size](structmodem__chat__config.md#af762b783d33e192ef45647e0b2e2d70b)

uint8\_t filter\_size

Size of filter.

**Definition** chat.h:298

[modem\_chat\_match](structmodem__chat__match.md)

Modem chat match.

**Definition** chat.h:38

[modem\_chat\_match::callback](structmodem__chat__match.md#a11f6e35cd2fd2166ac95adace6ec5c54)

modem\_chat\_match\_callback callback

Type of modem chat instance.

**Definition** chat.h:52

[modem\_chat\_match::separators\_size](structmodem__chat__match.md#a7c80555e1bf33504cef7be6c0f9db383)

uint8\_t separators\_size

Size of separators array.

**Definition** chat.h:46

[modem\_chat\_match::separators](structmodem__chat__match.md#a7fd423890bea11c65f326ace831233fc)

const uint8\_t \* separators

Separators array.

**Definition** chat.h:44

[modem\_chat\_match::partial](structmodem__chat__match.md#aa7f414d867fdcb2f34a9e4bd3c9b0eeb)

bool partial

Set if script shall not continue to next step in case of match.

**Definition** chat.h:50

[modem\_chat\_match::match](structmodem__chat__match.md#ad1bed20d70285a465663d9babc3fb3e2)

const uint8\_t \* match

Match array.

**Definition** chat.h:40

[modem\_chat\_match::wildcards](structmodem__chat__match.md#adb8c0ee17d317192432198949d116259)

bool wildcards

Set if modem chat instance shall use wildcards when matching.

**Definition** chat.h:48

[modem\_chat\_match::match\_size](structmodem__chat__match.md#afe00a3c87a68d9f7f889f7a0d3cc4150)

uint8\_t match\_size

Size of match.

**Definition** chat.h:42

[modem\_chat\_script\_chat](structmodem__chat__script__chat.md)

Modem chat script chat.

**Definition** chat.h:97

[modem\_chat\_script\_chat::timeout](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268)

uint16\_t timeout

Timeout before chat script may continue to next step in milliseconds.

**Definition** chat.h:107

[modem\_chat\_script\_chat::response\_matches](structmodem__chat__script__chat.md#a5cab9c3a31624c8ffb490b70285f86ee)

const struct modem\_chat\_match \* response\_matches

Expected responses to request.

**Definition** chat.h:103

[modem\_chat\_script\_chat::request](structmodem__chat__script__chat.md#a92c038d56623b4f4b26c64b537e7ce8a)

const uint8\_t \* request

Request to send to modem.

**Definition** chat.h:99

[modem\_chat\_script\_chat::request\_size](structmodem__chat__script__chat.md#ad87948ff4e6441c118ee269bf6458aa0)

uint16\_t request\_size

Size of request.

**Definition** chat.h:101

[modem\_chat\_script\_chat::response\_matches\_size](structmodem__chat__script__chat.md#afaaa9a7bc1842dfb65156fff2d91cfa0)

uint16\_t response\_matches\_size

Number of elements in expected responses.

**Definition** chat.h:105

[modem\_chat\_script](structmodem__chat__script.md)

Modem chat script.

**Definition** chat.h:162

[modem\_chat\_script::timeout](structmodem__chat__script.md#a0b9a9d3d44a8624728e16922cbdfd662)

uint32\_t timeout

Timeout in seconds within which the script execution must terminate.

**Definition** chat.h:176

[modem\_chat\_script::abort\_matches](structmodem__chat__script.md#a2b586e1ff80c22d8ff45829f3e2e7b17)

const struct modem\_chat\_match \* abort\_matches

Array of abort matches.

**Definition** chat.h:170

[modem\_chat\_script::script\_chats\_size](structmodem__chat__script.md#a3ac30e3ba1842cf53747721592f16cd4)

uint16\_t script\_chats\_size

Elements in array of script chats.

**Definition** chat.h:168

[modem\_chat\_script::script\_chats](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114)

const struct modem\_chat\_script\_chat \* script\_chats

Array of script chats.

**Definition** chat.h:166

[modem\_chat\_script::callback](structmodem__chat__script.md#a73f4c3892052f827c10ea466c9a75954)

modem\_chat\_script\_callback callback

Callback called when script execution terminates.

**Definition** chat.h:174

[modem\_chat\_script::abort\_matches\_size](structmodem__chat__script.md#aa56bdf520b0f385bc6410b2c6aa2e8d4)

uint16\_t abort\_matches\_size

Number of elements in array of abort matches.

**Definition** chat.h:172

[modem\_chat\_script::name](structmodem__chat__script.md#aca3b75a494273d8c06cf943153dd7dc8)

const char \* name

Name of script.

**Definition** chat.h:164

[modem\_chat](structmodem__chat.md)

Chat instance internal context.

**Definition** chat.h:210

[modem\_chat::delimiter\_size](structmodem__chat.md#a14104456f6e4b8c36b38eb232fb36996)

uint16\_t delimiter\_size

**Definition** chat.h:228

[modem\_chat::filter\_size](structmodem__chat.md#a199b2c9e9c6fd41e81ef6bca138b6328)

uint16\_t filter\_size

**Definition** chat.h:233

[modem\_chat::matches\_size](structmodem__chat.md#a249bc37382bddf11bfcabef834a19f2a)

uint16\_t matches\_size[3]

**Definition** chat.h:246

[modem\_chat::user\_data](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da)

void \* user\_data

**Definition** chat.h:215

[modem\_chat::parse\_arg\_len](structmodem__chat.md#a2e2555e463d6dffb5ed6531ad8a822ca)

uint16\_t parse\_arg\_len

**Definition** chat.h:268

[modem\_chat::script\_send\_pos](structmodem__chat.md#a36fb50970ebd8eb041506c913648be6c)

uint16\_t script\_send\_pos

**Definition** chat.h:261

[modem\_chat::script\_send\_timeout\_work](structmodem__chat.md#a37ae5aeeaaeba6e50d7d9f0df6ff2870)

struct k\_work\_delayable script\_send\_timeout\_work

**Definition** chat.h:263

[modem\_chat::parse\_match](structmodem__chat.md#a42d6fe9641db254459498d26b05ce152)

const struct modem\_chat\_match \* parse\_match

**Definition** chat.h:266

[modem\_chat::script\_run\_work](structmodem__chat.md#a44f303f7ec2aa304de5ba0e1249bff35)

struct k\_work script\_run\_work

**Definition** chat.h:251

[modem\_chat::receive\_work](structmodem__chat.md#a4558d8dc063f0330bdb4d203e2af6907)

struct k\_work receive\_work

**Definition** chat.h:272

[modem\_chat::script\_send\_work](structmodem__chat.md#a5260f843646e401159fd5f13015e9db6)

struct k\_work script\_send\_work

**Definition** chat.h:262

[modem\_chat::work\_buf](structmodem__chat.md#a5b3667c1e409fdc5382af75ad1329df9)

uint8\_t work\_buf[32]

**Definition** chat.h:223

[modem\_chat::script](structmodem__chat.md#a7c181f6c68809379d756080729e1e3a1)

const struct modem\_chat\_script \* script

**Definition** chat.h:249

[modem\_chat::script\_result](structmodem__chat.md#a8560fa2c2d26366ed27d8ca4620f30ff)

enum modem\_chat\_script\_result script\_result

**Definition** chat.h:256

[modem\_chat::receive\_buf\_size](structmodem__chat.md#a962b245335979eeb782410ba6429b4e6)

uint16\_t receive\_buf\_size

**Definition** chat.h:219

[modem\_chat::work\_buf\_len](structmodem__chat.md#a9acd26d97eec7c48482063a3c558c717)

uint16\_t work\_buf\_len

**Definition** chat.h:224

[modem\_chat::pipe](structmodem__chat.md#a9bec3daf58728d27a554d228452a8fa9)

struct modem\_pipe \* pipe

**Definition** chat.h:212

[modem\_chat::script\_send\_state](structmodem__chat.md#a9fc3fc3f5d2285d12ecad12e21e5be13)

enum modem\_chat\_script\_send\_state script\_send\_state

**Definition** chat.h:260

[modem\_chat::script\_chat\_it](structmodem__chat.md#aa09d879afc7f69901799d564c3951c7b)

uint16\_t script\_chat\_it

**Definition** chat.h:254

[modem\_chat::script\_stopped\_sem](structmodem__chat.md#aa365a6e40ec8de9e2a74c035dff0c203)

struct k\_sem script\_stopped\_sem

**Definition** chat.h:257

[modem\_chat::delimiter](structmodem__chat.md#aa8d3d31dc6eaf676c03fad034597ad91)

uint8\_t \* delimiter

**Definition** chat.h:227

[modem\_chat::pending\_script](structmodem__chat.md#abff96c9a7bd215f20fece3d6f96899b5)

const struct modem\_chat\_script \* pending\_script

**Definition** chat.h:250

[modem\_chat::matches](structmodem__chat.md#ac16520e4e7031bbc2162d29728eb86d2)

const struct modem\_chat\_match \* matches[3]

**Definition** chat.h:245

[modem\_chat::argv\_size](structmodem__chat.md#ac1c71497eb22137bc4a03877b6f30b37)

uint16\_t argv\_size

**Definition** chat.h:237

[modem\_chat::argc](structmodem__chat.md#ad08436ccb8308912a6d45b3b11cc0c59)

uint16\_t argc

**Definition** chat.h:238

[modem\_chat::script\_timeout\_work](structmodem__chat.md#ada952e3176a7f2645ff7b64ca32cb29e)

struct k\_work\_delayable script\_timeout\_work

**Definition** chat.h:252

[modem\_chat::filter](structmodem__chat.md#adcb6a8d9fdb9b7c0e950d64ec4b0853c)

uint8\_t \* filter

**Definition** chat.h:232

[modem\_chat::parse\_match\_len](structmodem__chat.md#ae14032ba980271ea758278d4bd8cca30)

uint16\_t parse\_match\_len

**Definition** chat.h:267

[modem\_chat::receive\_buf\_len](structmodem__chat.md#ae15c5238e6e04a4f94a27e779d3f2a30)

uint16\_t receive\_buf\_len

**Definition** chat.h:220

[modem\_chat::parse\_match\_type](structmodem__chat.md#ae4063127d0a802801660f08a1f403121)

uint16\_t parse\_match\_type

**Definition** chat.h:269

[modem\_chat::delimiter\_match\_len](structmodem__chat.md#ae5fe73d09b6fad3302e84ca841ad65ca)

uint16\_t delimiter\_match\_len

**Definition** chat.h:229

[modem\_chat::argv](structmodem__chat.md#ae7a2d23e34f95d3c3c5d5df15af1571a)

uint8\_t \*\* argv

**Definition** chat.h:236

[modem\_chat::script\_abort\_work](structmodem__chat.md#ae8df85a6e2c27f720e8f7f993e7d6a75)

struct k\_work script\_abort\_work

**Definition** chat.h:253

[modem\_chat::receive\_buf](structmodem__chat.md#af2ac2cf3efac415af72b702a1ec62ae7)

uint8\_t \* receive\_buf

**Definition** chat.h:218

[modem\_chat::script\_state](structmodem__chat.md#af55e1bf861e72b497230c92b4a673f4c)

atomic\_t script\_state

**Definition** chat.h:255

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [chat.h](chat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
