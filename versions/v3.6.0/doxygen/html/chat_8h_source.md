---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/chat_8h_source.html
original_path: doxygen/html/chat_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

7#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

8#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

9#include <[zephyr/device.h](device_8h.md)>

10#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

11

12#include <[zephyr/modem/pipe.h](pipe_8h.md)>

13

14#ifndef ZEPHYR\_MODEM\_CHAT\_

15#define ZEPHYR\_MODEM\_CHAT\_

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

21struct [modem\_chat](structmodem__chat.md);

22

[ 31](chat_8h.md#ae689e92c91d414f968267e290e5246bd)typedef void (\*[modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd))(struct [modem\_chat](structmodem__chat.md) \*chat, char \*\*[argv](structmodem__chat.md#ae7a2d23e34f95d3c3c5d5df15af1571a), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [argc](structmodem__chat.md#ad08436ccb8308912a6d45b3b11cc0c59),

32 void \*[user\_data](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da));

33

[ 37](structmodem__chat__match.md)struct [modem\_chat\_match](structmodem__chat__match.md) {

[ 39](structmodem__chat__match.md#ad1bed20d70285a465663d9babc3fb3e2) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[match](structmodem__chat__match.md#ad1bed20d70285a465663d9babc3fb3e2);

[ 41](structmodem__chat__match.md#afe00a3c87a68d9f7f889f7a0d3cc4150) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [match\_size](structmodem__chat__match.md#afe00a3c87a68d9f7f889f7a0d3cc4150);

[ 43](structmodem__chat__match.md#a7fd423890bea11c65f326ace831233fc) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[separators](structmodem__chat__match.md#a7fd423890bea11c65f326ace831233fc);

[ 45](structmodem__chat__match.md#a7c80555e1bf33504cef7be6c0f9db383) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [separators\_size](structmodem__chat__match.md#a7c80555e1bf33504cef7be6c0f9db383);

[ 47](structmodem__chat__match.md#a0e08870ad8dd3b781b8f20ed5fb230ca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [wildcards](structmodem__chat__match.md#a0e08870ad8dd3b781b8f20ed5fb230ca) : 1;

[ 49](structmodem__chat__match.md#aeb52b41db39ac21f5991524add42f8e3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [partial](structmodem__chat__match.md#aeb52b41db39ac21f5991524add42f8e3) : 1;

[ 51](structmodem__chat__match.md#a11f6e35cd2fd2166ac95adace6ec5c54) [modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd) [callback](structmodem__chat__match.md#a11f6e35cd2fd2166ac95adace6ec5c54);

52};

53

[ 54](chat_8h.md#a078fd13acc9abcc0e0aa0304e6a8537a)#define MODEM\_CHAT\_MATCH(\_match, \_separators, \_callback) \

55 { \

56 .match = (uint8\_t \*)(\_match), .match\_size = (uint8\_t)(sizeof(\_match) - 1), \

57 .separators = (uint8\_t \*)(\_separators), \

58 .separators\_size = (uint8\_t)(sizeof(\_separators) - 1), .wildcards = false, \

59 .callback = \_callback, \

60 }

61

[ 62](chat_8h.md#a02b06e0d97df03b32eb6c40e91f91fd8)#define MODEM\_CHAT\_MATCH\_WILDCARD(\_match, \_separators, \_callback) \

63 { \

64 .match = (uint8\_t \*)(\_match), .match\_size = (uint8\_t)(sizeof(\_match) - 1), \

65 .separators = (uint8\_t \*)(\_separators), \

66 .separators\_size = (uint8\_t)(sizeof(\_separators) - 1), .wildcards = true, \

67 .callback = \_callback, \

68 }

69

[ 70](chat_8h.md#aa62ca91615d0b93b0d2adbcf6c78e251)#define MODEM\_CHAT\_MATCH\_INITIALIZER(\_match, \_separators, \_callback, \_wildcards, \_partial) \

71 { \

72 .match = (uint8\_t \*)(\_match), \

73 .match\_size = (uint8\_t)(sizeof(\_match) - 1), \

74 .separators = (uint8\_t \*)(\_separators), \

75 .separators\_size = (uint8\_t)(sizeof(\_separators) - 1), \

76 .wildcards = \_wildcards, \

77 .partial = \_partial, \

78 .callback = \_callback, \

79 }

80

[ 81](chat_8h.md#a926b0d2993eb8158137e2caa7687abb8)#define MODEM\_CHAT\_MATCH\_DEFINE(\_sym, \_match, \_separators, \_callback) \

82 const static struct modem\_chat\_match \_sym = MODEM\_CHAT\_MATCH(\_match, \_separators, \_callback)

83

[ 84](chat_8h.md#a216094ddd94351fadf0e84bacbadc84e)#define MODEM\_CHAT\_MATCHES\_DEFINE(\_sym, ...) \

85 const static struct modem\_chat\_match \_sym[] = {\_\_VA\_ARGS\_\_}

86

[ 90](structmodem__chat__script__chat.md)struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) {

[ 92](structmodem__chat__script__chat.md#a92c038d56623b4f4b26c64b537e7ce8a) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[request](structmodem__chat__script__chat.md#a92c038d56623b4f4b26c64b537e7ce8a);

[ 94](structmodem__chat__script__chat.md#ad87948ff4e6441c118ee269bf6458aa0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [request\_size](structmodem__chat__script__chat.md#ad87948ff4e6441c118ee269bf6458aa0);

[ 96](structmodem__chat__script__chat.md#a5cab9c3a31624c8ffb490b70285f86ee) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[response\_matches](structmodem__chat__script__chat.md#a5cab9c3a31624c8ffb490b70285f86ee);

[ 98](structmodem__chat__script__chat.md#afaaa9a7bc1842dfb65156fff2d91cfa0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [response\_matches\_size](structmodem__chat__script__chat.md#afaaa9a7bc1842dfb65156fff2d91cfa0);

[ 100](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268);

101};

102

[ 103](chat_8h.md#a01c94aa4a5881f2f4bdc004d08abaf0d)#define MODEM\_CHAT\_SCRIPT\_CMD\_RESP(\_request, \_response\_match) \

104 { \

105 .request = (uint8\_t \*)(\_request), \

106 .request\_size = (uint16\_t)(sizeof(\_request) - 1), \

107 .response\_matches = &\_response\_match, \

108 .response\_matches\_size = 1, \

109 .timeout = 0, \

110 }

111

[ 112](chat_8h.md#add48fe039151f5596e5208cccd170746)#define MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_MULT(\_request, \_response\_matches) \

113 { \

114 .request = (uint8\_t \*)(\_request), \

115 .request\_size = (uint16\_t)(sizeof(\_request) - 1), \

116 .response\_matches = \_response\_matches, \

117 .response\_matches\_size = ARRAY\_SIZE(\_response\_matches), \

118 .timeout = 0, \

119 }

120

[ 121](chat_8h.md#a13613a9df035c4ac55a730ca9d64fa36)#define MODEM\_CHAT\_SCRIPT\_CMD\_RESP\_NONE(\_request, \_timeout) \

122 { \

123 .request = (uint8\_t \*)(\_request), \

124 .request\_size = (uint16\_t)(sizeof(\_request) - 1), \

125 .response\_matches = NULL, \

126 .response\_matches\_size = 0, \

127 .timeout = \_timeout, \

128 }

129

[ 130](chat_8h.md#ab807fffae2007bc03a8e87ba73921888)#define MODEM\_CHAT\_SCRIPT\_CMDS\_DEFINE(\_sym, ...) \

131 const struct modem\_chat\_script\_chat \_sym[] = {\_\_VA\_ARGS\_\_}

132

[ 133](chat_8h.md#a4035be227ddec8424311575305647d3e)enum [modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e) {

[ 134](chat_8h.md#a4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee) [MODEM\_CHAT\_SCRIPT\_RESULT\_SUCCESS](chat_8h.md#a4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee),

[ 135](chat_8h.md#a4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b) [MODEM\_CHAT\_SCRIPT\_RESULT\_ABORT](chat_8h.md#a4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b),

[ 136](chat_8h.md#a4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e) [MODEM\_CHAT\_SCRIPT\_RESULT\_TIMEOUT](chat_8h.md#a4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e)

137};

138

[ 146](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e)typedef void (\*[modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e))(struct [modem\_chat](structmodem__chat.md) \*chat,

147 enum [modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e) result, void \*[user\_data](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da));

148

[ 152](structmodem__chat__script.md)struct [modem\_chat\_script](structmodem__chat__script.md) {

[ 154](structmodem__chat__script.md#aca3b75a494273d8c06cf943153dd7dc8) const char \*[name](structmodem__chat__script.md#aca3b75a494273d8c06cf943153dd7dc8);

[ 156](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114) const struct [modem\_chat\_script\_chat](structmodem__chat__script__chat.md) \*[script\_chats](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114);

[ 158](structmodem__chat__script.md#a3ac30e3ba1842cf53747721592f16cd4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [script\_chats\_size](structmodem__chat__script.md#a3ac30e3ba1842cf53747721592f16cd4);

[ 160](structmodem__chat__script.md#a2b586e1ff80c22d8ff45829f3e2e7b17) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[abort\_matches](structmodem__chat__script.md#a2b586e1ff80c22d8ff45829f3e2e7b17);

[ 162](structmodem__chat__script.md#aa56bdf520b0f385bc6410b2c6aa2e8d4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [abort\_matches\_size](structmodem__chat__script.md#aa56bdf520b0f385bc6410b2c6aa2e8d4);

[ 164](structmodem__chat__script.md#a73f4c3892052f827c10ea466c9a75954) [modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e) [callback](structmodem__chat__script.md#a73f4c3892052f827c10ea466c9a75954);

[ 166](structmodem__chat__script.md#a0b9a9d3d44a8624728e16922cbdfd662) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [timeout](structmodem__chat__script.md#a0b9a9d3d44a8624728e16922cbdfd662);

167};

168

[ 169](chat_8h.md#a20bd8d3dd49c813101c6f456351bc771)#define MODEM\_CHAT\_SCRIPT\_DEFINE(\_sym, \_script\_chats, \_abort\_matches, \_callback, \_timeout) \

170 const static struct modem\_chat\_script \_sym = { \

171 .name = #\_sym, \

172 .script\_chats = \_script\_chats, \

173 .script\_chats\_size = ARRAY\_SIZE(\_script\_chats), \

174 .abort\_matches = \_abort\_matches, \

175 .abort\_matches\_size = ARRAY\_SIZE(\_abort\_matches), \

176 .callback = \_callback, \

177 .timeout = \_timeout, \

178 }

179

[ 180](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae)enum [modem\_chat\_script\_send\_state](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae) {

181 /\* No data to send \*/

[ 182](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974) [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_IDLE](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974),

183 /\* Sending request \*/

[ 184](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd) [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_REQUEST](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd),

185 /\* Sending delimiter \*/

[ 186](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aeaaf1d0f61d85bc5fbb77a979efe9b1aaf) [MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_DELIMITER](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aeaaf1d0f61d85bc5fbb77a979efe9b1aaf),

187};

188

[ 193](structmodem__chat.md)struct [modem\_chat](structmodem__chat.md) {

194 /\* Pipe used to send and receive data \*/

[ 195](structmodem__chat.md#a9bec3daf58728d27a554d228452a8fa9) struct modem\_pipe \*[pipe](structmodem__chat.md#a9bec3daf58728d27a554d228452a8fa9);

196

197 /\* User data passed with match callbacks \*/

[ 198](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da) void \*[user\_data](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da);

199

200 /\* Receive buffer \*/

[ 201](structmodem__chat.md#af2ac2cf3efac415af72b702a1ec62ae7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__chat.md#af2ac2cf3efac415af72b702a1ec62ae7);

[ 202](structmodem__chat.md#a962b245335979eeb782410ba6429b4e6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__chat.md#a962b245335979eeb782410ba6429b4e6);

[ 203](structmodem__chat.md#ae15c5238e6e04a4f94a27e779d3f2a30) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_len](structmodem__chat.md#ae15c5238e6e04a4f94a27e779d3f2a30);

204

205 /\* Work buffer \*/

[ 206](structmodem__chat.md#a5b3667c1e409fdc5382af75ad1329df9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [work\_buf](structmodem__chat.md#a5b3667c1e409fdc5382af75ad1329df9)[32];

[ 207](structmodem__chat.md#a9acd26d97eec7c48482063a3c558c717) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [work\_buf\_len](structmodem__chat.md#a9acd26d97eec7c48482063a3c558c717);

208

209 /\* Chat delimiter \*/

[ 210](structmodem__chat.md#aa8d3d31dc6eaf676c03fad034597ad91) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[delimiter](structmodem__chat.md#aa8d3d31dc6eaf676c03fad034597ad91);

[ 211](structmodem__chat.md#a14104456f6e4b8c36b38eb232fb36996) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [delimiter\_size](structmodem__chat.md#a14104456f6e4b8c36b38eb232fb36996);

[ 212](structmodem__chat.md#ae5fe73d09b6fad3302e84ca841ad65ca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [delimiter\_match\_len](structmodem__chat.md#ae5fe73d09b6fad3302e84ca841ad65ca);

213

214 /\* Array of bytes which are discarded out by parser \*/

[ 215](structmodem__chat.md#adcb6a8d9fdb9b7c0e950d64ec4b0853c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[filter](structmodem__chat.md#adcb6a8d9fdb9b7c0e950d64ec4b0853c);

[ 216](structmodem__chat.md#a199b2c9e9c6fd41e81ef6bca138b6328) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [filter\_size](structmodem__chat.md#a199b2c9e9c6fd41e81ef6bca138b6328);

217

218 /\* Parsed arguments \*/

[ 219](structmodem__chat.md#ae7a2d23e34f95d3c3c5d5df15af1571a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*[argv](structmodem__chat.md#ae7a2d23e34f95d3c3c5d5df15af1571a);

[ 220](structmodem__chat.md#ac1c71497eb22137bc4a03877b6f30b37) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [argv\_size](structmodem__chat.md#ac1c71497eb22137bc4a03877b6f30b37);

[ 221](structmodem__chat.md#ad08436ccb8308912a6d45b3b11cc0c59) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [argc](structmodem__chat.md#ad08436ccb8308912a6d45b3b11cc0c59);

222

223 /\* Matches

224 \* Index 0 -> Response matches

225 \* Index 1 -> Abort matches

226 \* Index 2 -> Unsolicited matches

227 \*/

[ 228](structmodem__chat.md#ac16520e4e7031bbc2162d29728eb86d2) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[matches](structmodem__chat.md#ac16520e4e7031bbc2162d29728eb86d2)[3];

[ 229](structmodem__chat.md#a249bc37382bddf11bfcabef834a19f2a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [matches\_size](structmodem__chat.md#a249bc37382bddf11bfcabef834a19f2a)[3];

230

231 /\* Script execution \*/

[ 232](structmodem__chat.md#a7c181f6c68809379d756080729e1e3a1) const struct [modem\_chat\_script](structmodem__chat__script.md) \*[script](structmodem__chat.md#a7c181f6c68809379d756080729e1e3a1);

[ 233](structmodem__chat.md#abff96c9a7bd215f20fece3d6f96899b5) const struct [modem\_chat\_script](structmodem__chat__script.md) \*[pending\_script](structmodem__chat.md#abff96c9a7bd215f20fece3d6f96899b5);

[ 234](structmodem__chat.md#a44f303f7ec2aa304de5ba0e1249bff35) struct [k\_work](structk__work.md) [script\_run\_work](structmodem__chat.md#a44f303f7ec2aa304de5ba0e1249bff35);

[ 235](structmodem__chat.md#ada952e3176a7f2645ff7b64ca32cb29e) struct [k\_work\_delayable](structk__work__delayable.md) [script\_timeout\_work](structmodem__chat.md#ada952e3176a7f2645ff7b64ca32cb29e);

[ 236](structmodem__chat.md#ae8df85a6e2c27f720e8f7f993e7d6a75) struct [k\_work](structk__work.md) [script\_abort\_work](structmodem__chat.md#ae8df85a6e2c27f720e8f7f993e7d6a75);

[ 237](structmodem__chat.md#aa09d879afc7f69901799d564c3951c7b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [script\_chat\_it](structmodem__chat.md#aa09d879afc7f69901799d564c3951c7b);

[ 238](structmodem__chat.md#af55e1bf861e72b497230c92b4a673f4c) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [script\_state](structmodem__chat.md#af55e1bf861e72b497230c92b4a673f4c);

[ 239](structmodem__chat.md#a8560fa2c2d26366ed27d8ca4620f30ff) enum [modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e) [script\_result](structmodem__chat.md#a8560fa2c2d26366ed27d8ca4620f30ff);

[ 240](structmodem__chat.md#aa365a6e40ec8de9e2a74c035dff0c203) struct k\_sem [script\_stopped\_sem](structmodem__chat.md#aa365a6e40ec8de9e2a74c035dff0c203);

241

242 /\* Script sending \*/

[ 243](structmodem__chat.md#a9fc3fc3f5d2285d12ecad12e21e5be13) enum [modem\_chat\_script\_send\_state](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae) [script\_send\_state](structmodem__chat.md#a9fc3fc3f5d2285d12ecad12e21e5be13);

[ 244](structmodem__chat.md#a36fb50970ebd8eb041506c913648be6c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [script\_send\_pos](structmodem__chat.md#a36fb50970ebd8eb041506c913648be6c);

[ 245](structmodem__chat.md#a5260f843646e401159fd5f13015e9db6) struct [k\_work](structk__work.md) [script\_send\_work](structmodem__chat.md#a5260f843646e401159fd5f13015e9db6);

[ 246](structmodem__chat.md#a37ae5aeeaaeba6e50d7d9f0df6ff2870) struct [k\_work\_delayable](structk__work__delayable.md) [script\_send\_timeout\_work](structmodem__chat.md#a37ae5aeeaaeba6e50d7d9f0df6ff2870);

247

248 /\* Match parsing \*/

[ 249](structmodem__chat.md#a42d6fe9641db254459498d26b05ce152) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[parse\_match](structmodem__chat.md#a42d6fe9641db254459498d26b05ce152);

[ 250](structmodem__chat.md#ae14032ba980271ea758278d4bd8cca30) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [parse\_match\_len](structmodem__chat.md#ae14032ba980271ea758278d4bd8cca30);

[ 251](structmodem__chat.md#a2e2555e463d6dffb5ed6531ad8a822ca) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [parse\_arg\_len](structmodem__chat.md#a2e2555e463d6dffb5ed6531ad8a822ca);

[ 252](structmodem__chat.md#ae4063127d0a802801660f08a1f403121) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [parse\_match\_type](structmodem__chat.md#ae4063127d0a802801660f08a1f403121);

253

254 /\* Process received data \*/

[ 255](structmodem__chat.md#a4558d8dc063f0330bdb4d203e2af6907) struct [k\_work](structk__work.md) [receive\_work](structmodem__chat.md#a4558d8dc063f0330bdb4d203e2af6907);

256};

257

[ 261](structmodem__chat__config.md)struct [modem\_chat\_config](structmodem__chat__config.md) {

[ 263](structmodem__chat__config.md#ac002d9f43309db8c3c35826127d94194) void \*[user\_data](structmodem__chat__config.md#ac002d9f43309db8c3c35826127d94194);

[ 265](structmodem__chat__config.md#a295de98c2e8866059e7194c57d0502b7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__chat__config.md#a295de98c2e8866059e7194c57d0502b7);

[ 267](structmodem__chat__config.md#a76f85951f5750f0d07b1253af118ec6f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__chat__config.md#a76f85951f5750f0d07b1253af118ec6f);

[ 269](structmodem__chat__config.md#ab3adfaddd56884553a57467c762bdf98) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[delimiter](structmodem__chat__config.md#ab3adfaddd56884553a57467c762bdf98);

[ 271](structmodem__chat__config.md#aa30ccfd372c47c64e2a7b7c840405499) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [delimiter\_size](structmodem__chat__config.md#aa30ccfd372c47c64e2a7b7c840405499);

[ 273](structmodem__chat__config.md#af6646dee93b3279429eb95c87426168b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[filter](structmodem__chat__config.md#af6646dee93b3279429eb95c87426168b);

[ 275](structmodem__chat__config.md#af762b783d33e192ef45647e0b2e2d70b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [filter\_size](structmodem__chat__config.md#af762b783d33e192ef45647e0b2e2d70b);

[ 277](structmodem__chat__config.md#ae2afa6465bfad9c83dd57498165888b4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*[argv](structmodem__chat__config.md#ae2afa6465bfad9c83dd57498165888b4);

[ 279](structmodem__chat__config.md#a2cf551a0946459b2825595026ebc7490) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [argv\_size](structmodem__chat__config.md#a2cf551a0946459b2825595026ebc7490);

[ 281](structmodem__chat__config.md#a661d96b8a7031b17e6f660c6e0e4be11) const struct [modem\_chat\_match](structmodem__chat__match.md) \*[unsol\_matches](structmodem__chat__config.md#a661d96b8a7031b17e6f660c6e0e4be11);

[ 283](structmodem__chat__config.md#addfa7cacc676190d9e29c451d47ea3bd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [unsol\_matches\_size](structmodem__chat__config.md#addfa7cacc676190d9e29c451d47ea3bd);

284};

285

[ 292](chat_8h.md#af79f3b0e67b5777876137b9e3e16d985)int [modem\_chat\_init](chat_8h.md#af79f3b0e67b5777876137b9e3e16d985)(struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_config](structmodem__chat__config.md) \*config);

293

[ 302](chat_8h.md#af91ae4e64113188e7049a7568a086556)int [modem\_chat\_attach](chat_8h.md#af91ae4e64113188e7049a7568a086556)(struct [modem\_chat](structmodem__chat.md) \*chat, struct modem\_pipe \*pipe);

303

[ 314](chat_8h.md#a397d399703449498171ac898776fe791)int [modem\_chat\_run\_script\_async](chat_8h.md#a397d399703449498171ac898776fe791)(struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_script](structmodem__chat__script.md) \*script);

315

[ 326](chat_8h.md#ae64d151a5f65bde1dd1973393acf3ff1)int [modem\_chat\_run\_script](chat_8h.md#ae64d151a5f65bde1dd1973393acf3ff1)(struct [modem\_chat](structmodem__chat.md) \*chat, const struct [modem\_chat\_script](structmodem__chat__script.md) \*script);

327

[ 338](chat_8h.md#aa92ffb91bab15c882cff7b13fca7eeb5)static inline int [modem\_chat\_script\_run](chat_8h.md#aa92ffb91bab15c882cff7b13fca7eeb5)(struct [modem\_chat](structmodem__chat.md) \*chat,

339 const struct [modem\_chat\_script](structmodem__chat__script.md) \*script)

340{

341 return [modem\_chat\_run\_script\_async](chat_8h.md#a397d399703449498171ac898776fe791)(chat, script);

342}

343

[ 348](chat_8h.md#a5ec3918a4beb6b30deecedbd6f6382ee)void [modem\_chat\_script\_abort](chat_8h.md#a5ec3918a4beb6b30deecedbd6f6382ee)(struct [modem\_chat](structmodem__chat.md) \*chat);

349

[ 354](chat_8h.md#a62fa275cb9ce387b0bf5b384c9448c41)void [modem\_chat\_release](chat_8h.md#a62fa275cb9ce387b0bf5b384c9448c41)(struct [modem\_chat](structmodem__chat.md) \*chat);

355

356#ifdef \_\_cplusplus

357}

358#endif

359

360#endif /\* ZEPHYR\_MODEM\_CHAT\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[modem\_chat\_run\_script\_async](chat_8h.md#a397d399703449498171ac898776fe791)

int modem\_chat\_run\_script\_async(struct modem\_chat \*chat, const struct modem\_chat\_script \*script)

Run script asynchronously.

[modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e)

modem\_chat\_script\_result

**Definition** chat.h:133

[MODEM\_CHAT\_SCRIPT\_RESULT\_TIMEOUT](chat_8h.md#a4035be227ddec8424311575305647d3ea4991b2748978d1219923d275a42c575e)

@ MODEM\_CHAT\_SCRIPT\_RESULT\_TIMEOUT

**Definition** chat.h:136

[MODEM\_CHAT\_SCRIPT\_RESULT\_SUCCESS](chat_8h.md#a4035be227ddec8424311575305647d3ea977c97fa42b7fb38d337062984b0deee)

@ MODEM\_CHAT\_SCRIPT\_RESULT\_SUCCESS

**Definition** chat.h:134

[MODEM\_CHAT\_SCRIPT\_RESULT\_ABORT](chat_8h.md#a4035be227ddec8424311575305647d3eacddc6a743055b7c49fac484442dda31b)

@ MODEM\_CHAT\_SCRIPT\_RESULT\_ABORT

**Definition** chat.h:135

[modem\_chat\_script\_abort](chat_8h.md#a5ec3918a4beb6b30deecedbd6f6382ee)

void modem\_chat\_script\_abort(struct modem\_chat \*chat)

Abort script.

[modem\_chat\_release](chat_8h.md#a62fa275cb9ce387b0bf5b384c9448c41)

void modem\_chat\_release(struct modem\_chat \*chat)

Release pipe from chat instance.

[modem\_chat\_script\_callback](chat_8h.md#a72ee94db5e79658fb71a65a3118d301e)

void(\* modem\_chat\_script\_callback)(struct modem\_chat \*chat, enum modem\_chat\_script\_result result, void \*user\_data)

Callback called when script chat is received.

**Definition** chat.h:146

[modem\_chat\_script\_send\_state](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae)

modem\_chat\_script\_send\_state

**Definition** chat.h:180

[MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_REQUEST](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea14824a0ffb464bf00a8aadcf4c8bdbbd)

@ MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_REQUEST

**Definition** chat.h:184

[MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_IDLE](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aea8971f4f05275f31d255f4a5c7dd47974)

@ MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_IDLE

**Definition** chat.h:182

[MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_DELIMITER](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608aeaaf1d0f61d85bc5fbb77a979efe9b1aaf)

@ MODEM\_CHAT\_SCRIPT\_SEND\_STATE\_DELIMITER

**Definition** chat.h:186

[modem\_chat\_script\_run](chat_8h.md#aa92ffb91bab15c882cff7b13fca7eeb5)

static int modem\_chat\_script\_run(struct modem\_chat \*chat, const struct modem\_chat\_script \*script)

Run script asynchronously.

**Definition** chat.h:338

[modem\_chat\_run\_script](chat_8h.md#ae64d151a5f65bde1dd1973393acf3ff1)

int modem\_chat\_run\_script(struct modem\_chat \*chat, const struct modem\_chat\_script \*script)

Run script.

[modem\_chat\_match\_callback](chat_8h.md#ae689e92c91d414f968267e290e5246bd)

void(\* modem\_chat\_match\_callback)(struct modem\_chat \*chat, char \*\*argv, uint16\_t argc, void \*user\_data)

Callback called when matching chat is received.

**Definition** chat.h:31

[modem\_chat\_init](chat_8h.md#af79f3b0e67b5777876137b9e3e16d985)

int modem\_chat\_init(struct modem\_chat \*chat, const struct modem\_chat\_config \*config)

Initialize modem pipe chat instance.

[modem\_chat\_attach](chat_8h.md#af91ae4e64113188e7049a7568a086556)

int modem\_chat\_attach(struct modem\_chat \*chat, struct modem\_pipe \*pipe)

Attach modem chat instance to pipe.

[device.h](device_8h.md)

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

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

**Definition** kernel.h:3889

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3861

[modem\_chat\_config](structmodem__chat__config.md)

Chat configuration.

**Definition** chat.h:261

[modem\_chat\_config::receive\_buf](structmodem__chat__config.md#a295de98c2e8866059e7194c57d0502b7)

uint8\_t \* receive\_buf

Receive buffer used to store parsed arguments.

**Definition** chat.h:265

[modem\_chat\_config::argv\_size](structmodem__chat__config.md#a2cf551a0946459b2825595026ebc7490)

uint16\_t argv\_size

Elements in array of pointers.

**Definition** chat.h:279

[modem\_chat\_config::unsol\_matches](structmodem__chat__config.md#a661d96b8a7031b17e6f660c6e0e4be11)

const struct modem\_chat\_match \* unsol\_matches

Array of unsolicited matches.

**Definition** chat.h:281

[modem\_chat\_config::receive\_buf\_size](structmodem__chat__config.md#a76f85951f5750f0d07b1253af118ec6f)

uint16\_t receive\_buf\_size

Size of receive buffer should be longest line + longest match.

**Definition** chat.h:267

[modem\_chat\_config::delimiter\_size](structmodem__chat__config.md#aa30ccfd372c47c64e2a7b7c840405499)

uint8\_t delimiter\_size

Size of delimiter.

**Definition** chat.h:271

[modem\_chat\_config::delimiter](structmodem__chat__config.md#ab3adfaddd56884553a57467c762bdf98)

uint8\_t \* delimiter

Delimiter.

**Definition** chat.h:269

[modem\_chat\_config::user\_data](structmodem__chat__config.md#ac002d9f43309db8c3c35826127d94194)

void \* user\_data

Free to use user data passed with modem match callbacks.

**Definition** chat.h:263

[modem\_chat\_config::unsol\_matches\_size](structmodem__chat__config.md#addfa7cacc676190d9e29c451d47ea3bd)

uint16\_t unsol\_matches\_size

Elements in array of unsolicited matches.

**Definition** chat.h:283

[modem\_chat\_config::argv](structmodem__chat__config.md#ae2afa6465bfad9c83dd57498165888b4)

uint8\_t \*\* argv

Array of pointers used to point to parsed arguments.

**Definition** chat.h:277

[modem\_chat\_config::filter](structmodem__chat__config.md#af6646dee93b3279429eb95c87426168b)

uint8\_t \* filter

Bytes which are discarded by parser.

**Definition** chat.h:273

[modem\_chat\_config::filter\_size](structmodem__chat__config.md#af762b783d33e192ef45647e0b2e2d70b)

uint8\_t filter\_size

Size of filter.

**Definition** chat.h:275

[modem\_chat\_match](structmodem__chat__match.md)

Modem chat match.

**Definition** chat.h:37

[modem\_chat\_match::wildcards](structmodem__chat__match.md#a0e08870ad8dd3b781b8f20ed5fb230ca)

uint8\_t wildcards

Set if modem chat instance shall use wildcards when matching.

**Definition** chat.h:47

[modem\_chat\_match::callback](structmodem__chat__match.md#a11f6e35cd2fd2166ac95adace6ec5c54)

modem\_chat\_match\_callback callback

Type of modem chat instance.

**Definition** chat.h:51

[modem\_chat\_match::separators\_size](structmodem__chat__match.md#a7c80555e1bf33504cef7be6c0f9db383)

uint8\_t separators\_size

Size of separators array.

**Definition** chat.h:45

[modem\_chat\_match::separators](structmodem__chat__match.md#a7fd423890bea11c65f326ace831233fc)

const uint8\_t \* separators

Separators array.

**Definition** chat.h:43

[modem\_chat\_match::match](structmodem__chat__match.md#ad1bed20d70285a465663d9babc3fb3e2)

const uint8\_t \* match

Match array.

**Definition** chat.h:39

[modem\_chat\_match::partial](structmodem__chat__match.md#aeb52b41db39ac21f5991524add42f8e3)

uint8\_t partial

Set if script shall not continue to next step in case of match.

**Definition** chat.h:49

[modem\_chat\_match::match\_size](structmodem__chat__match.md#afe00a3c87a68d9f7f889f7a0d3cc4150)

uint8\_t match\_size

Size of match.

**Definition** chat.h:41

[modem\_chat\_script\_chat](structmodem__chat__script__chat.md)

Modem chat script chat.

**Definition** chat.h:90

[modem\_chat\_script\_chat::timeout](structmodem__chat__script__chat.md#a21647c746e9b2da52b7093afccf08268)

uint16\_t timeout

Timeout before chat script may continue to next step in milliseconds.

**Definition** chat.h:100

[modem\_chat\_script\_chat::response\_matches](structmodem__chat__script__chat.md#a5cab9c3a31624c8ffb490b70285f86ee)

const struct modem\_chat\_match \* response\_matches

Expected responses to request.

**Definition** chat.h:96

[modem\_chat\_script\_chat::request](structmodem__chat__script__chat.md#a92c038d56623b4f4b26c64b537e7ce8a)

const uint8\_t \* request

Request to send to modem.

**Definition** chat.h:92

[modem\_chat\_script\_chat::request\_size](structmodem__chat__script__chat.md#ad87948ff4e6441c118ee269bf6458aa0)

uint16\_t request\_size

Size of request.

**Definition** chat.h:94

[modem\_chat\_script\_chat::response\_matches\_size](structmodem__chat__script__chat.md#afaaa9a7bc1842dfb65156fff2d91cfa0)

uint16\_t response\_matches\_size

Number of elements in expected responses.

**Definition** chat.h:98

[modem\_chat\_script](structmodem__chat__script.md)

Modem chat script.

**Definition** chat.h:152

[modem\_chat\_script::timeout](structmodem__chat__script.md#a0b9a9d3d44a8624728e16922cbdfd662)

uint32\_t timeout

Timeout in seconds within which the script execution must terminate.

**Definition** chat.h:166

[modem\_chat\_script::abort\_matches](structmodem__chat__script.md#a2b586e1ff80c22d8ff45829f3e2e7b17)

const struct modem\_chat\_match \* abort\_matches

Array of abort matches.

**Definition** chat.h:160

[modem\_chat\_script::script\_chats\_size](structmodem__chat__script.md#a3ac30e3ba1842cf53747721592f16cd4)

uint16\_t script\_chats\_size

Elements in array of script chats.

**Definition** chat.h:158

[modem\_chat\_script::script\_chats](structmodem__chat__script.md#a5f329ecadd721d88e423074f00005114)

const struct modem\_chat\_script\_chat \* script\_chats

Array of script chats.

**Definition** chat.h:156

[modem\_chat\_script::callback](structmodem__chat__script.md#a73f4c3892052f827c10ea466c9a75954)

modem\_chat\_script\_callback callback

Callback called when script execution terminates.

**Definition** chat.h:164

[modem\_chat\_script::abort\_matches\_size](structmodem__chat__script.md#aa56bdf520b0f385bc6410b2c6aa2e8d4)

uint16\_t abort\_matches\_size

Number of elements in array of abort matches.

**Definition** chat.h:162

[modem\_chat\_script::name](structmodem__chat__script.md#aca3b75a494273d8c06cf943153dd7dc8)

const char \* name

Name of script.

**Definition** chat.h:154

[modem\_chat](structmodem__chat.md)

Chat instance internal context.

**Definition** chat.h:193

[modem\_chat::delimiter\_size](structmodem__chat.md#a14104456f6e4b8c36b38eb232fb36996)

uint16\_t delimiter\_size

**Definition** chat.h:211

[modem\_chat::filter\_size](structmodem__chat.md#a199b2c9e9c6fd41e81ef6bca138b6328)

uint16\_t filter\_size

**Definition** chat.h:216

[modem\_chat::matches\_size](structmodem__chat.md#a249bc37382bddf11bfcabef834a19f2a)

uint16\_t matches\_size[3]

**Definition** chat.h:229

[modem\_chat::user\_data](structmodem__chat.md#a26d717e335b4b1ade0972458c11f42da)

void \* user\_data

**Definition** chat.h:198

[modem\_chat::parse\_arg\_len](structmodem__chat.md#a2e2555e463d6dffb5ed6531ad8a822ca)

uint16\_t parse\_arg\_len

**Definition** chat.h:251

[modem\_chat::script\_send\_pos](structmodem__chat.md#a36fb50970ebd8eb041506c913648be6c)

uint16\_t script\_send\_pos

**Definition** chat.h:244

[modem\_chat::script\_send\_timeout\_work](structmodem__chat.md#a37ae5aeeaaeba6e50d7d9f0df6ff2870)

struct k\_work\_delayable script\_send\_timeout\_work

**Definition** chat.h:246

[modem\_chat::parse\_match](structmodem__chat.md#a42d6fe9641db254459498d26b05ce152)

const struct modem\_chat\_match \* parse\_match

**Definition** chat.h:249

[modem\_chat::script\_run\_work](structmodem__chat.md#a44f303f7ec2aa304de5ba0e1249bff35)

struct k\_work script\_run\_work

**Definition** chat.h:234

[modem\_chat::receive\_work](structmodem__chat.md#a4558d8dc063f0330bdb4d203e2af6907)

struct k\_work receive\_work

**Definition** chat.h:255

[modem\_chat::script\_send\_work](structmodem__chat.md#a5260f843646e401159fd5f13015e9db6)

struct k\_work script\_send\_work

**Definition** chat.h:245

[modem\_chat::work\_buf](structmodem__chat.md#a5b3667c1e409fdc5382af75ad1329df9)

uint8\_t work\_buf[32]

**Definition** chat.h:206

[modem\_chat::script](structmodem__chat.md#a7c181f6c68809379d756080729e1e3a1)

const struct modem\_chat\_script \* script

**Definition** chat.h:232

[modem\_chat::script\_result](structmodem__chat.md#a8560fa2c2d26366ed27d8ca4620f30ff)

enum modem\_chat\_script\_result script\_result

**Definition** chat.h:239

[modem\_chat::receive\_buf\_size](structmodem__chat.md#a962b245335979eeb782410ba6429b4e6)

uint16\_t receive\_buf\_size

**Definition** chat.h:202

[modem\_chat::work\_buf\_len](structmodem__chat.md#a9acd26d97eec7c48482063a3c558c717)

uint16\_t work\_buf\_len

**Definition** chat.h:207

[modem\_chat::pipe](structmodem__chat.md#a9bec3daf58728d27a554d228452a8fa9)

struct modem\_pipe \* pipe

**Definition** chat.h:195

[modem\_chat::script\_send\_state](structmodem__chat.md#a9fc3fc3f5d2285d12ecad12e21e5be13)

enum modem\_chat\_script\_send\_state script\_send\_state

**Definition** chat.h:243

[modem\_chat::script\_chat\_it](structmodem__chat.md#aa09d879afc7f69901799d564c3951c7b)

uint16\_t script\_chat\_it

**Definition** chat.h:237

[modem\_chat::script\_stopped\_sem](structmodem__chat.md#aa365a6e40ec8de9e2a74c035dff0c203)

struct k\_sem script\_stopped\_sem

**Definition** chat.h:240

[modem\_chat::delimiter](structmodem__chat.md#aa8d3d31dc6eaf676c03fad034597ad91)

uint8\_t \* delimiter

**Definition** chat.h:210

[modem\_chat::pending\_script](structmodem__chat.md#abff96c9a7bd215f20fece3d6f96899b5)

const struct modem\_chat\_script \* pending\_script

**Definition** chat.h:233

[modem\_chat::matches](structmodem__chat.md#ac16520e4e7031bbc2162d29728eb86d2)

const struct modem\_chat\_match \* matches[3]

**Definition** chat.h:228

[modem\_chat::argv\_size](structmodem__chat.md#ac1c71497eb22137bc4a03877b6f30b37)

uint16\_t argv\_size

**Definition** chat.h:220

[modem\_chat::argc](structmodem__chat.md#ad08436ccb8308912a6d45b3b11cc0c59)

uint16\_t argc

**Definition** chat.h:221

[modem\_chat::script\_timeout\_work](structmodem__chat.md#ada952e3176a7f2645ff7b64ca32cb29e)

struct k\_work\_delayable script\_timeout\_work

**Definition** chat.h:235

[modem\_chat::filter](structmodem__chat.md#adcb6a8d9fdb9b7c0e950d64ec4b0853c)

uint8\_t \* filter

**Definition** chat.h:215

[modem\_chat::parse\_match\_len](structmodem__chat.md#ae14032ba980271ea758278d4bd8cca30)

uint16\_t parse\_match\_len

**Definition** chat.h:250

[modem\_chat::receive\_buf\_len](structmodem__chat.md#ae15c5238e6e04a4f94a27e779d3f2a30)

uint16\_t receive\_buf\_len

**Definition** chat.h:203

[modem\_chat::parse\_match\_type](structmodem__chat.md#ae4063127d0a802801660f08a1f403121)

uint16\_t parse\_match\_type

**Definition** chat.h:252

[modem\_chat::delimiter\_match\_len](structmodem__chat.md#ae5fe73d09b6fad3302e84ca841ad65ca)

uint16\_t delimiter\_match\_len

**Definition** chat.h:212

[modem\_chat::argv](structmodem__chat.md#ae7a2d23e34f95d3c3c5d5df15af1571a)

uint8\_t \*\* argv

**Definition** chat.h:219

[modem\_chat::script\_abort\_work](structmodem__chat.md#ae8df85a6e2c27f720e8f7f993e7d6a75)

struct k\_work script\_abort\_work

**Definition** chat.h:236

[modem\_chat::receive\_buf](structmodem__chat.md#af2ac2cf3efac415af72b702a1ec62ae7)

uint8\_t \* receive\_buf

**Definition** chat.h:201

[modem\_chat::script\_state](structmodem__chat.md#af55e1bf861e72b497230c92b4a673f4c)

atomic\_t script\_state

**Definition** chat.h:238

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [chat.h](chat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
