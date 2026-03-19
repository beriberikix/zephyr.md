---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ec__host__cmd_8h_source.html
original_path: doxygen/html/ec__host__cmd_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd.h

[Go to the documentation of this file.](ec__host__cmd_8h.md)

1/\*

2 \* Copyright (c) 2020 Google LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_EC\_HOST\_CMD\_H\_

8#define ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_EC\_HOST\_CMD\_H\_

9

18

19#include <[stdint.h](stdint_8h.md)>

20#include <[zephyr/kernel.h](kernel_8h.md)>

21#include <[zephyr/mgmt/ec\_host\_cmd/backend.h](backend_8h.md)>

22#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

23#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

24

[ 28](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f)enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) {

[ 30](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e) [EC\_HOST\_CMD\_SUCCESS](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e) = 0,

[ 32](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432) [EC\_HOST\_CMD\_INVALID\_COMMAND](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432) = 1,

[ 34](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201) [EC\_HOST\_CMD\_ERROR](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201) = 2,

[ 36](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d) [EC\_HOST\_CMD\_INVALID\_PARAM](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d) = 3,

[ 38](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c) [EC\_HOST\_CMD\_ACCESS\_DENIED](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c) = 4,

[ 40](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9) [EC\_HOST\_CMD\_INVALID\_RESPONSE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9) = 5,

[ 42](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39) [EC\_HOST\_CMD\_INVALID\_VERSION](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39) = 6,

[ 44](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301) [EC\_HOST\_CMD\_INVALID\_CHECKSUM](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301) = 7,

[ 46](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e) [EC\_HOST\_CMD\_IN\_PROGRESS](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e) = 8,

[ 48](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996) [EC\_HOST\_CMD\_UNAVAILABLE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996) = 9,

[ 50](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26) [EC\_HOST\_CMD\_TIMEOUT](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26) = 10,

[ 52](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443) [EC\_HOST\_CMD\_OVERFLOW](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443) = 11,

[ 54](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b) [EC\_HOST\_CMD\_INVALID\_HEADER](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b) = 12,

[ 56](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00) [EC\_HOST\_CMD\_REQUEST\_TRUNCATED](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00) = 13,

[ 58](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5) [EC\_HOST\_CMD\_RESPONSE\_TOO\_BIG](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5) = 14,

[ 60](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2) [EC\_HOST\_CMD\_BUS\_ERROR](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2) = 15,

[ 62](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1) [EC\_HOST\_CMD\_BUSY](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1) = 16,

[ 64](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5) [EC\_HOST\_CMD\_INVALID\_HEADER\_VERSION](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5) = 17,

[ 66](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e) [EC\_HOST\_CMD\_INVALID\_HEADER\_CRC](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e) = 18,

[ 68](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985) [EC\_HOST\_CMD\_INVALID\_DATA\_CRC](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985) = 19,

[ 70](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80) [EC\_HOST\_CMD\_DUP\_UNAVAILABLE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80) = 20,

71

[ 72](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad202e5ae4fac72a7fb3d1f4a7dff3ba9) [EC\_HOST\_CMD\_MAX](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad202e5ae4fac72a7fb3d1f4a7dff3ba9) = [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602) /\* Force enum to be 16 bits. \*/

73} \_\_packed;

74

[ 75](group__ec__host__cmd__interface.md#ga70cbd55129ef589688c6d2f5999337c9)enum [ec\_host\_cmd\_log\_level](group__ec__host__cmd__interface.md#ga70cbd55129ef589688c6d2f5999337c9) {

[ 76](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38) [EC\_HOST\_CMD\_DEBUG\_OFF](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38), /\* No Host Command debug output \*/

[ 77](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81) [EC\_HOST\_CMD\_DEBUG\_NORMAL](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81), /\* Normal output mode; skips repeated commands \*/

[ 78](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6) [EC\_HOST\_CMD\_DEBUG\_EVERY](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6), /\* Print every command \*/

[ 79](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1) [EC\_HOST\_CMD\_DEBUG\_PARAMS](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1), /\* ... and print params for request/response \*/

[ 80](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b) [EC\_HOST\_CMD\_DEBUG\_MODES](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b) /\* Number of host command debug modes \*/

81};

82

[ 83](group__ec__host__cmd__interface.md#gabf0f1243bf55cb70078f2a9fd0a755ec)enum [ec\_host\_cmd\_state](group__ec__host__cmd__interface.md#gabf0f1243bf55cb70078f2a9fd0a755ec) {

[ 84](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af) [EC\_HOST\_CMD\_STATE\_DISABLED](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af) = 0,

[ 85](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20) [EC\_HOST\_CMD\_STATE\_RECEIVING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20),

[ 86](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8) [EC\_HOST\_CMD\_STATE\_PROCESSING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8),

[ 87](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46) [EC\_HOST\_CMD\_STATE\_SENDING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46),

88};

89

[ 90](group__ec__host__cmd__interface.md#ga027ae23ea11a0ec7711725d1b28125d7)typedef void (\*[ec\_host\_cmd\_user\_cb\_t](group__ec__host__cmd__interface.md#gaa6ea251ee113cc15fd085ef12b76a573))(const struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) \*rx\_ctx, void \*user\_data);

91typedef enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) (\*[ec\_host\_cmd\_in\_progress\_cb\_t](group__ec__host__cmd__interface.md#gacf91301985634f9a12cd80db5e818821))(void \*user\_data);

92

[ 93](structec__host__cmd.md)struct [ec\_host\_cmd](structec__host__cmd.md) {

[ 94](structec__host__cmd.md#a1f5153ec8442ae8c70d4918ff21b908e) struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) [rx\_ctx](structec__host__cmd.md#a1f5153ec8442ae8c70d4918ff21b908e);

[ 95](structec__host__cmd.md#af1a3f483c1a7ddb88db187e406caa08d) struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) [tx](structec__host__cmd.md#af1a3f483c1a7ddb88db187e406caa08d);

[ 96](structec__host__cmd.md#ad269f3223fc0885ba5c847b4443c993c) struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*[backend](structec__host__cmd.md#ad269f3223fc0885ba5c847b4443c993c);

[ 101](structec__host__cmd.md#a465d588b50f0a881e7f1d8b761c4288f) struct k\_sem [rx\_ready](structec__host__cmd.md#a465d588b50f0a881e7f1d8b761c4288f);

[ 103](structec__host__cmd.md#a0e50770725cd93b0923769b3b650b04d) enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) [rx\_status](structec__host__cmd.md#a0e50770725cd93b0923769b3b650b04d);

[ 108](structec__host__cmd.md#ad2f10eda2e6c2743d9c3068bda4deb7c) [ec\_host\_cmd\_user\_cb\_t](group__ec__host__cmd__interface.md#gaa6ea251ee113cc15fd085ef12b76a573) [user\_cb](structec__host__cmd.md#ad2f10eda2e6c2743d9c3068bda4deb7c);

[ 109](structec__host__cmd.md#a7982f079e67180de58ebd0a6f0f5d7e0) void \*[user\_data](structec__host__cmd.md#a7982f079e67180de58ebd0a6f0f5d7e0);

[ 110](structec__host__cmd.md#a444f295157c5ada6162aea803ff219e1) enum [ec\_host\_cmd\_state](group__ec__host__cmd__interface.md#gabf0f1243bf55cb70078f2a9fd0a755ec) [state](structec__host__cmd.md#a444f295157c5ada6162aea803ff219e1);

111#ifdef CONFIG\_EC\_HOST\_CMD\_DEDICATED\_THREAD

112 struct [k\_thread](structk__thread.md) thread;

113#endif /\* CONFIG\_EC\_HOST\_CMD\_DEDICATED\_THREAD \*/

114};

115

[ 119](structec__host__cmd__handler__args.md)struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) {

[ 121](structec__host__cmd__handler__args.md#a8c7fcd1d310b0622f45458388462c9ef) void \*[reserved](structec__host__cmd__handler__args.md#a8c7fcd1d310b0622f45458388462c9ef);

[ 123](structec__host__cmd__handler__args.md#a059b20824ece1ada2d53c7e73f49972d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [command](structec__host__cmd__handler__args.md#a059b20824ece1ada2d53c7e73f49972d);

[ 128](structec__host__cmd__handler__args.md#ad346a4c196ee5e48c67640232a828745) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [version](structec__host__cmd__handler__args.md#ad346a4c196ee5e48c67640232a828745);

[ 130](structec__host__cmd__handler__args.md#a364bda288790f65205f26310148d2888) const void \*[input\_buf](structec__host__cmd__handler__args.md#a364bda288790f65205f26310148d2888);

[ 132](structec__host__cmd__handler__args.md#a7d6d622f7dd9e3b8faf928befa72f36a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [input\_buf\_size](structec__host__cmd__handler__args.md#a7d6d622f7dd9e3b8faf928befa72f36a);

[ 134](structec__host__cmd__handler__args.md#a1ac9d891b168b4db55a1829d72362ca5) void \*[output\_buf](structec__host__cmd__handler__args.md#a1ac9d891b168b4db55a1829d72362ca5);

[ 136](structec__host__cmd__handler__args.md#ab3eaef25fd80d0ac38b8d2eb9e40ebd4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [output\_buf\_max](structec__host__cmd__handler__args.md#ab3eaef25fd80d0ac38b8d2eb9e40ebd4);

[ 138](structec__host__cmd__handler__args.md#a1a6f9a7ba7faf810f7095b4c053dd3b2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [output\_buf\_size](structec__host__cmd__handler__args.md#a1a6f9a7ba7faf810f7095b4c053dd3b2);

139};

140

141typedef enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) (\*[ec\_host\_cmd\_handler\_cb](group__ec__host__cmd__interface.md#ga027ae23ea11a0ec7711725d1b28125d7))(struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) \*args);

[ 145](structec__host__cmd__handler.md)struct [ec\_host\_cmd\_handler](structec__host__cmd__handler.md) {

[ 147](structec__host__cmd__handler.md#aa87d559e625871f78023fcc015a02c82) [ec\_host\_cmd\_handler\_cb](group__ec__host__cmd__interface.md#ga027ae23ea11a0ec7711725d1b28125d7) [handler](structec__host__cmd__handler.md#aa87d559e625871f78023fcc015a02c82);

[ 149](structec__host__cmd__handler.md#ad0aea63728aa9254e2a14d8cf0352b87) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structec__host__cmd__handler.md#ad0aea63728aa9254e2a14d8cf0352b87);

[ 155](structec__host__cmd__handler.md#a2e4643dc7ca0ee4b8f7169b9156dadc6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [version\_mask](structec__host__cmd__handler.md#a2e4643dc7ca0ee4b8f7169b9156dadc6);

[ 160](structec__host__cmd__handler.md#aef233f030a30032e9dcde620c1953394) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_rqt\_size](structec__host__cmd__handler.md#aef233f030a30032e9dcde620c1953394);

[ 165](structec__host__cmd__handler.md#a4777b0c23ddf568c36ca995886cf3248) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min\_rsp\_size](structec__host__cmd__handler.md#a4777b0c23ddf568c36ca995886cf3248);

166};

167

[ 182](group__ec__host__cmd__interface.md#gaed5a8c4ba3648ae9e6284502f6a48dc7)#define EC\_HOST\_CMD\_HANDLER(\_id, \_function, \_version\_mask, \_request\_type, \_response\_type) \

183 const STRUCT\_SECTION\_ITERABLE(ec\_host\_cmd\_handler, \_\_cmd##\_id) = { \

184 .handler = \_function, \

185 .id = \_id, \

186 .version\_mask = \_version\_mask, \

187 .min\_rqt\_size = sizeof(\_request\_type), \

188 .min\_rsp\_size = sizeof(\_response\_type), \

189 }

190

[ 202](group__ec__host__cmd__interface.md#ga2dae15d1db72c7c9b5f879284a990e13)#define EC\_HOST\_CMD\_HANDLER\_UNBOUND(\_id, \_function, \_version\_mask) \

203 const STRUCT\_SECTION\_ITERABLE(ec\_host\_cmd\_handler, \_\_cmd##\_id) = { \

204 .handler = \_function, \

205 .id = \_id, \

206 .version\_mask = \_version\_mask, \

207 .min\_rqt\_size = 0, \

208 .min\_rsp\_size = 0, \

209 }

210

[ 218](structec__host__cmd__request__header.md)struct [ec\_host\_cmd\_request\_header](structec__host__cmd__request__header.md) {

[ 223](structec__host__cmd__request__header.md#a2f723addb6f8aec8b2d1b02a555d7b59) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prtcl\_ver](structec__host__cmd__request__header.md#a2f723addb6f8aec8b2d1b02a555d7b59);

[ 228](structec__host__cmd__request__header.md#a91358051660c5fa5bab1cd61991ff6b5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [checksum](structec__host__cmd__request__header.md#a91358051660c5fa5bab1cd61991ff6b5);

[ 230](structec__host__cmd__request__header.md#a1b4bd2b53046e29554f27dd49eb3e807) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cmd\_id](structec__host__cmd__request__header.md#a1b4bd2b53046e29554f27dd49eb3e807);

[ 235](structec__host__cmd__request__header.md#a2eb262f5fd1c7106d75feb8a5a6333a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd\_ver](structec__host__cmd__request__header.md#a2eb262f5fd1c7106d75feb8a5a6333a3);

[ 237](structec__host__cmd__request__header.md#ad5a54882becb66008a378be28a20dd2f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structec__host__cmd__request__header.md#ad5a54882becb66008a378be28a20dd2f);

[ 239](structec__host__cmd__request__header.md#afedc78b6d294f73313f9eae9ecc6a03d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data\_len](structec__host__cmd__request__header.md#afedc78b6d294f73313f9eae9ecc6a03d);

240} \_\_packed;

241

[ 249](structec__host__cmd__response__header.md)struct [ec\_host\_cmd\_response\_header](structec__host__cmd__response__header.md) {

[ 251](structec__host__cmd__response__header.md#a50baff1f46f56c992194c3c244897aa8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prtcl\_ver](structec__host__cmd__response__header.md#a50baff1f46f56c992194c3c244897aa8);

[ 256](structec__host__cmd__response__header.md#ac77bfd822866c9f48cec249a60eaa82b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [checksum](structec__host__cmd__response__header.md#ac77bfd822866c9f48cec249a60eaa82b);

[ 258](structec__host__cmd__response__header.md#ab64789cfe9fc9008aa5d88182fee9885) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [result](structec__host__cmd__response__header.md#ab64789cfe9fc9008aa5d88182fee9885);

[ 260](structec__host__cmd__response__header.md#af0abf8f0d16b2089bb4f7abaac5191af) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [data\_len](structec__host__cmd__response__header.md#af0abf8f0d16b2089bb4f7abaac5191af);

[ 262](structec__host__cmd__response__header.md#ab45cadbdafc4ab1eb5d8b1b1db2303de) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [reserved](structec__host__cmd__response__header.md#ab45cadbdafc4ab1eb5d8b1b1db2303de);

263} \_\_packed;

264

[ 281](group__ec__host__cmd__interface.md#gaab1fdcb0fd13a19447d262d496b8aed9)int [ec\_host\_cmd\_init](group__ec__host__cmd__interface.md#gaab1fdcb0fd13a19447d262d496b8aed9)(struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend);

282

[ 294](group__ec__host__cmd__interface.md#ga95f36f8cf2d21ea73bd8a36f3f7303e8)int [ec\_host\_cmd\_send\_response](group__ec__host__cmd__interface.md#ga95f36f8cf2d21ea73bd8a36f3f7303e8)(enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) status,

295 const struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) \*args);

296

[ 303](group__ec__host__cmd__interface.md#gadbee4a2588abeb6db63f70a90b67a8fb)void [ec\_host\_cmd\_rx\_notify](group__ec__host__cmd__interface.md#gadbee4a2588abeb6db63f70a90b67a8fb)(void);

304

[ 313](group__ec__host__cmd__interface.md#gaaf267a44816e5f856db2092fca681d3e)void [ec\_host\_cmd\_set\_user\_cb](group__ec__host__cmd__interface.md#gaaf267a44816e5f856db2092fca681d3e)([ec\_host\_cmd\_user\_cb\_t](group__ec__host__cmd__interface.md#gaa6ea251ee113cc15fd085ef12b76a573) cb, void \*user\_data);

314

[ 324](group__ec__host__cmd__interface.md#gaf3b87533037c4d865641643736904d02)const struct [ec\_host\_cmd](structec__host__cmd.md) \*[ec\_host\_cmd\_get\_hc](group__ec__host__cmd__interface.md#gaf3b87533037c4d865641643736904d02)(void);

325

326#ifndef CONFIG\_EC\_HOST\_CMD\_DEDICATED\_THREAD

[ 334](group__ec__host__cmd__interface.md#gaaa3dc6c413b9637a3817cf82e138b27a)FUNC\_NORETURN void [ec\_host\_cmd\_task](group__ec__host__cmd__interface.md#gaaa3dc6c413b9637a3817cf82e138b27a)(void);

335#endif

336

337#ifdef CONFIG\_EC\_HOST\_CMD\_IN\_PROGRESS\_STATUS

346bool ec\_host\_cmd\_send\_in\_progress\_ended(void);

347

359enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) ec\_host\_cmd\_send\_in\_progress\_status(void);

360

375enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) ec\_host\_cmd\_send\_in\_progress\_continue([ec\_host\_cmd\_in\_progress\_cb\_t](group__ec__host__cmd__interface.md#gacf91301985634f9a12cd80db5e818821) cb,

376 void \*[user\_data](structec__host__cmd.md#a7982f079e67180de58ebd0a6f0f5d7e0));

377#endif /\* CONFIG\_EC\_HOST\_CMD\_IN\_PROGRESS\_STATUS \*/

378

[ 388](group__ec__host__cmd__interface.md#ga9f734642958684ca654a3c786b2ceb74)int [ec\_host\_cmd\_add\_suppressed](group__ec__host__cmd__interface.md#ga9f734642958684ca654a3c786b2ceb74)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cmd\_id);

389

393

394#endif /\* ZEPHYR\_INCLUDE\_MGMT\_EC\_HOST\_CMD\_EC\_HOST\_CMD\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[backend.h](backend_8h.md)

Public APIs for Host Command backends that respond to host commands.

[ec\_host\_cmd\_handler\_cb](group__ec__host__cmd__interface.md#ga027ae23ea11a0ec7711725d1b28125d7)

enum ec\_host\_cmd\_status(\* ec\_host\_cmd\_handler\_cb)(struct ec\_host\_cmd\_handler\_args \*args)

**Definition** ec\_host\_cmd.h:141

[ec\_host\_cmd\_log\_level](group__ec__host__cmd__interface.md#ga70cbd55129ef589688c6d2f5999337c9)

ec\_host\_cmd\_log\_level

**Definition** ec\_host\_cmd.h:75

[ec\_host\_cmd\_send\_response](group__ec__host__cmd__interface.md#ga95f36f8cf2d21ea73bd8a36f3f7303e8)

int ec\_host\_cmd\_send\_response(enum ec\_host\_cmd\_status status, const struct ec\_host\_cmd\_handler\_args \*args)

Send the host command response.

[ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f)

ec\_host\_cmd\_status

Host command response codes (16-bit).

**Definition** ec\_host\_cmd.h:28

[ec\_host\_cmd\_add\_suppressed](group__ec__host__cmd__interface.md#ga9f734642958684ca654a3c786b2ceb74)

int ec\_host\_cmd\_add\_suppressed(uint16\_t cmd\_id)

Add a suppressed command.

[ec\_host\_cmd\_user\_cb\_t](group__ec__host__cmd__interface.md#gaa6ea251ee113cc15fd085ef12b76a573)

void(\* ec\_host\_cmd\_user\_cb\_t)(const struct ec\_host\_cmd\_rx\_ctx \*rx\_ctx, void \*user\_data)

**Definition** ec\_host\_cmd.h:90

[ec\_host\_cmd\_task](group__ec__host__cmd__interface.md#gaaa3dc6c413b9637a3817cf82e138b27a)

FUNC\_NORETURN void ec\_host\_cmd\_task(void)

The thread function for Host Command subsystem.

[ec\_host\_cmd\_init](group__ec__host__cmd__interface.md#gaab1fdcb0fd13a19447d262d496b8aed9)

int ec\_host\_cmd\_init(struct ec\_host\_cmd\_backend \*backend)

Initialize the host command subsystem.

[ec\_host\_cmd\_set\_user\_cb](group__ec__host__cmd__interface.md#gaaf267a44816e5f856db2092fca681d3e)

void ec\_host\_cmd\_set\_user\_cb(ec\_host\_cmd\_user\_cb\_t cb, void \*user\_data)

Install a user callback for receiving a host command.

[ec\_host\_cmd\_state](group__ec__host__cmd__interface.md#gabf0f1243bf55cb70078f2a9fd0a755ec)

ec\_host\_cmd\_state

**Definition** ec\_host\_cmd.h:83

[ec\_host\_cmd\_in\_progress\_cb\_t](group__ec__host__cmd__interface.md#gacf91301985634f9a12cd80db5e818821)

enum ec\_host\_cmd\_status(\* ec\_host\_cmd\_in\_progress\_cb\_t)(void \*user\_data)

**Definition** ec\_host\_cmd.h:91

[ec\_host\_cmd\_rx\_notify](group__ec__host__cmd__interface.md#gadbee4a2588abeb6db63f70a90b67a8fb)

void ec\_host\_cmd\_rx\_notify(void)

Signal a new host command.

[ec\_host\_cmd\_get\_hc](group__ec__host__cmd__interface.md#gaf3b87533037c4d865641643736904d02)

const struct ec\_host\_cmd \* ec\_host\_cmd\_get\_hc(void)

Get the main ec host command structure.

[EC\_HOST\_CMD\_DEBUG\_EVERY](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6)

@ EC\_HOST\_CMD\_DEBUG\_EVERY

**Definition** ec\_host\_cmd.h:78

[EC\_HOST\_CMD\_DEBUG\_PARAMS](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1)

@ EC\_HOST\_CMD\_DEBUG\_PARAMS

**Definition** ec\_host\_cmd.h:79

[EC\_HOST\_CMD\_DEBUG\_OFF](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38)

@ EC\_HOST\_CMD\_DEBUG\_OFF

**Definition** ec\_host\_cmd.h:76

[EC\_HOST\_CMD\_DEBUG\_MODES](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b)

@ EC\_HOST\_CMD\_DEBUG\_MODES

**Definition** ec\_host\_cmd.h:80

[EC\_HOST\_CMD\_DEBUG\_NORMAL](group__ec__host__cmd__interface.md#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81)

@ EC\_HOST\_CMD\_DEBUG\_NORMAL

**Definition** ec\_host\_cmd.h:77

[EC\_HOST\_CMD\_BUSY](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1)

@ EC\_HOST\_CMD\_BUSY

System busy.

**Definition** ec\_host\_cmd.h:62

[EC\_HOST\_CMD\_REQUEST\_TRUNCATED](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00)

@ EC\_HOST\_CMD\_REQUEST\_TRUNCATED

Did not receive all expected request data.

**Definition** ec\_host\_cmd.h:56

[EC\_HOST\_CMD\_INVALID\_DATA\_CRC](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985)

@ EC\_HOST\_CMD\_INVALID\_DATA\_CRC

Data CRC invalid.

**Definition** ec\_host\_cmd.h:68

[EC\_HOST\_CMD\_DUP\_UNAVAILABLE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80)

@ EC\_HOST\_CMD\_DUP\_UNAVAILABLE

Can't resend response.

**Definition** ec\_host\_cmd.h:70

[EC\_HOST\_CMD\_ERROR](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201)

@ EC\_HOST\_CMD\_ERROR

Generic Error.

**Definition** ec\_host\_cmd.h:34

[EC\_HOST\_CMD\_INVALID\_HEADER](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b)

@ EC\_HOST\_CMD\_INVALID\_HEADER

Header is invalid or unsupported (e.g.

**Definition** ec\_host\_cmd.h:54

[EC\_HOST\_CMD\_INVALID\_HEADER\_VERSION](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5)

@ EC\_HOST\_CMD\_INVALID\_HEADER\_VERSION

Header version invalid.

**Definition** ec\_host\_cmd.h:64

[EC\_HOST\_CMD\_IN\_PROGRESS](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e)

@ EC\_HOST\_CMD\_IN\_PROGRESS

A host command is currently being processed.

**Definition** ec\_host\_cmd.h:46

[EC\_HOST\_CMD\_SUCCESS](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e)

@ EC\_HOST\_CMD\_SUCCESS

Host command was successful.

**Definition** ec\_host\_cmd.h:30

[EC\_HOST\_CMD\_INVALID\_VERSION](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39)

@ EC\_HOST\_CMD\_INVALID\_VERSION

Host command id version unsupported.

**Definition** ec\_host\_cmd.h:42

[EC\_HOST\_CMD\_INVALID\_CHECKSUM](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301)

@ EC\_HOST\_CMD\_INVALID\_CHECKSUM

Checksum did not match.

**Definition** ec\_host\_cmd.h:44

[EC\_HOST\_CMD\_UNAVAILABLE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996)

@ EC\_HOST\_CMD\_UNAVAILABLE

Requested information is currently unavailable.

**Definition** ec\_host\_cmd.h:48

[EC\_HOST\_CMD\_INVALID\_HEADER\_CRC](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e)

@ EC\_HOST\_CMD\_INVALID\_HEADER\_CRC

Header CRC invalid.

**Definition** ec\_host\_cmd.h:66

[EC\_HOST\_CMD\_MAX](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad202e5ae4fac72a7fb3d1f4a7dff3ba9)

@ EC\_HOST\_CMD\_MAX

**Definition** ec\_host\_cmd.h:72

[EC\_HOST\_CMD\_INVALID\_COMMAND](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432)

@ EC\_HOST\_CMD\_INVALID\_COMMAND

The specified command id is not recognized or supported.

**Definition** ec\_host\_cmd.h:32

[EC\_HOST\_CMD\_ACCESS\_DENIED](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c)

@ EC\_HOST\_CMD\_ACCESS\_DENIED

Host command is not permitted.

**Definition** ec\_host\_cmd.h:38

[EC\_HOST\_CMD\_TIMEOUT](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26)

@ EC\_HOST\_CMD\_TIMEOUT

Timeout during processing.

**Definition** ec\_host\_cmd.h:50

[EC\_HOST\_CMD\_BUS\_ERROR](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2)

@ EC\_HOST\_CMD\_BUS\_ERROR

Error on underlying communication bus.

**Definition** ec\_host\_cmd.h:60

[EC\_HOST\_CMD\_INVALID\_PARAM](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d)

@ EC\_HOST\_CMD\_INVALID\_PARAM

One of more of the input request parameters is invalid.

**Definition** ec\_host\_cmd.h:36

[EC\_HOST\_CMD\_OVERFLOW](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443)

@ EC\_HOST\_CMD\_OVERFLOW

Data or table overflow.

**Definition** ec\_host\_cmd.h:52

[EC\_HOST\_CMD\_RESPONSE\_TOO\_BIG](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5)

@ EC\_HOST\_CMD\_RESPONSE\_TOO\_BIG

Response was too big to send within one response packet.

**Definition** ec\_host\_cmd.h:58

[EC\_HOST\_CMD\_INVALID\_RESPONSE](group__ec__host__cmd__interface.md#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9)

@ EC\_HOST\_CMD\_INVALID\_RESPONSE

Response was invalid (e.g.

**Definition** ec\_host\_cmd.h:40

[EC\_HOST\_CMD\_STATE\_RECEIVING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20)

@ EC\_HOST\_CMD\_STATE\_RECEIVING

**Definition** ec\_host\_cmd.h:85

[EC\_HOST\_CMD\_STATE\_PROCESSING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8)

@ EC\_HOST\_CMD\_STATE\_PROCESSING

**Definition** ec\_host\_cmd.h:86

[EC\_HOST\_CMD\_STATE\_DISABLED](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af)

@ EC\_HOST\_CMD\_STATE\_DISABLED

**Definition** ec\_host\_cmd.h:84

[EC\_HOST\_CMD\_STATE\_SENDING](group__ec__host__cmd__interface.md#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46)

@ EC\_HOST\_CMD\_STATE\_SENDING

**Definition** ec\_host\_cmd.h:87

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602)

#define UINT16\_MAX

**Definition** stdint.h:28

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ec\_host\_cmd\_backend](structec__host__cmd__backend.md)

**Definition** backend.h:25

[ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md)

Arguments passed into every installed host command handler.

**Definition** ec\_host\_cmd.h:119

[ec\_host\_cmd\_handler\_args::command](structec__host__cmd__handler__args.md#a059b20824ece1ada2d53c7e73f49972d)

uint16\_t command

Command identifier.

**Definition** ec\_host\_cmd.h:123

[ec\_host\_cmd\_handler\_args::output\_buf\_size](structec__host__cmd__handler__args.md#a1a6f9a7ba7faf810f7095b4c053dd3b2)

uint16\_t output\_buf\_size

Number of bytes of output\_buf to send to the host.

**Definition** ec\_host\_cmd.h:138

[ec\_host\_cmd\_handler\_args::output\_buf](structec__host__cmd__handler__args.md#a1ac9d891b168b4db55a1829d72362ca5)

void \* output\_buf

The data written to this buffer will be send to the host.

**Definition** ec\_host\_cmd.h:134

[ec\_host\_cmd\_handler\_args::input\_buf](structec__host__cmd__handler__args.md#a364bda288790f65205f26310148d2888)

const void \* input\_buf

The incoming data that can be cast to the handlers request type.

**Definition** ec\_host\_cmd.h:130

[ec\_host\_cmd\_handler\_args::input\_buf\_size](structec__host__cmd__handler__args.md#a7d6d622f7dd9e3b8faf928befa72f36a)

uint16\_t input\_buf\_size

The number of valid bytes that can be read from input\_buf.

**Definition** ec\_host\_cmd.h:132

[ec\_host\_cmd\_handler\_args::reserved](structec__host__cmd__handler__args.md#a8c7fcd1d310b0622f45458388462c9ef)

void \* reserved

Reserved for compatibility.

**Definition** ec\_host\_cmd.h:121

[ec\_host\_cmd\_handler\_args::output\_buf\_max](structec__host__cmd__handler__args.md#ab3eaef25fd80d0ac38b8d2eb9e40ebd4)

uint16\_t output\_buf\_max

Maximum number of bytes that can be written to the output\_buf.

**Definition** ec\_host\_cmd.h:136

[ec\_host\_cmd\_handler\_args::version](structec__host__cmd__handler__args.md#ad346a4c196ee5e48c67640232a828745)

uint8\_t version

The version of the host command that is being requested.

**Definition** ec\_host\_cmd.h:128

[ec\_host\_cmd\_handler](structec__host__cmd__handler.md)

Structure use for statically registering host command handlers.

**Definition** ec\_host\_cmd.h:145

[ec\_host\_cmd\_handler::version\_mask](structec__host__cmd__handler.md#a2e4643dc7ca0ee4b8f7169b9156dadc6)

uint16\_t version\_mask

The bitfield of all versions that the handler supports, where each bit value represents that the hand...

**Definition** ec\_host\_cmd.h:155

[ec\_host\_cmd\_handler::min\_rsp\_size](structec__host__cmd__handler.md#a4777b0c23ddf568c36ca995886cf3248)

uint16\_t min\_rsp\_size

The minimum output\_buf\_size enforced by the framework before passing to the handler.

**Definition** ec\_host\_cmd.h:165

[ec\_host\_cmd\_handler::handler](structec__host__cmd__handler.md#aa87d559e625871f78023fcc015a02c82)

ec\_host\_cmd\_handler\_cb handler

Callback routine to process commands that match id.

**Definition** ec\_host\_cmd.h:147

[ec\_host\_cmd\_handler::id](structec__host__cmd__handler.md#ad0aea63728aa9254e2a14d8cf0352b87)

uint16\_t id

The numerical command id used as the lookup for commands.

**Definition** ec\_host\_cmd.h:149

[ec\_host\_cmd\_handler::min\_rqt\_size](structec__host__cmd__handler.md#aef233f030a30032e9dcde620c1953394)

uint16\_t min\_rqt\_size

The minimum input\_buf\_size enforced by the framework before passing to the handler.

**Definition** ec\_host\_cmd.h:160

[ec\_host\_cmd\_request\_header](structec__host__cmd__request__header.md)

Header for requests from host to embedded controller.

**Definition** ec\_host\_cmd.h:218

[ec\_host\_cmd\_request\_header::cmd\_id](structec__host__cmd__request__header.md#a1b4bd2b53046e29554f27dd49eb3e807)

uint16\_t cmd\_id

Id of command that is being sent.

**Definition** ec\_host\_cmd.h:230

[ec\_host\_cmd\_request\_header::cmd\_ver](structec__host__cmd__request__header.md#a2eb262f5fd1c7106d75feb8a5a6333a3)

uint8\_t cmd\_ver

Version of the specific cmd\_id being requested.

**Definition** ec\_host\_cmd.h:235

[ec\_host\_cmd\_request\_header::prtcl\_ver](structec__host__cmd__request__header.md#a2f723addb6f8aec8b2d1b02a555d7b59)

uint8\_t prtcl\_ver

Should be 3.

**Definition** ec\_host\_cmd.h:223

[ec\_host\_cmd\_request\_header::checksum](structec__host__cmd__request__header.md#a91358051660c5fa5bab1cd61991ff6b5)

uint8\_t checksum

Checksum of response and data; sum of all bytes including checksum.

**Definition** ec\_host\_cmd.h:228

[ec\_host\_cmd\_request\_header::reserved](structec__host__cmd__request__header.md#ad5a54882becb66008a378be28a20dd2f)

uint8\_t reserved

Unused byte in current protocol version; set to 0.

**Definition** ec\_host\_cmd.h:237

[ec\_host\_cmd\_request\_header::data\_len](structec__host__cmd__request__header.md#afedc78b6d294f73313f9eae9ecc6a03d)

uint16\_t data\_len

Length of data which follows this header.

**Definition** ec\_host\_cmd.h:239

[ec\_host\_cmd\_response\_header](structec__host__cmd__response__header.md)

Header for responses from embedded controller to host.

**Definition** ec\_host\_cmd.h:249

[ec\_host\_cmd\_response\_header::prtcl\_ver](structec__host__cmd__response__header.md#a50baff1f46f56c992194c3c244897aa8)

uint8\_t prtcl\_ver

Should be 3.

**Definition** ec\_host\_cmd.h:251

[ec\_host\_cmd\_response\_header::reserved](structec__host__cmd__response__header.md#ab45cadbdafc4ab1eb5d8b1b1db2303de)

uint16\_t reserved

Unused bytes in current protocol version; set to 0.

**Definition** ec\_host\_cmd.h:262

[ec\_host\_cmd\_response\_header::result](structec__host__cmd__response__header.md#ab64789cfe9fc9008aa5d88182fee9885)

uint16\_t result

A ec\_host\_cmd\_status response code for specific command.

**Definition** ec\_host\_cmd.h:258

[ec\_host\_cmd\_response\_header::checksum](structec__host__cmd__response__header.md#ac77bfd822866c9f48cec249a60eaa82b)

uint8\_t checksum

Checksum of response and data; sum of all bytes including checksum.

**Definition** ec\_host\_cmd.h:256

[ec\_host\_cmd\_response\_header::data\_len](structec__host__cmd__response__header.md#af0abf8f0d16b2089bb4f7abaac5191af)

uint16\_t data\_len

Length of data which follows this header.

**Definition** ec\_host\_cmd.h:260

[ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md)

Context for host command backend and handler to pass rx data.

**Definition** backend.h:42

[ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md)

Context for host command backend and handler to pass tx data.

**Definition** backend.h:59

[ec\_host\_cmd](structec__host__cmd.md)

**Definition** ec\_host\_cmd.h:93

[ec\_host\_cmd::rx\_status](structec__host__cmd.md#a0e50770725cd93b0923769b3b650b04d)

enum ec\_host\_cmd\_status rx\_status

Status of the rx data checked in the ec\_host\_cmd\_send\_received function.

**Definition** ec\_host\_cmd.h:103

[ec\_host\_cmd::rx\_ctx](structec__host__cmd.md#a1f5153ec8442ae8c70d4918ff21b908e)

struct ec\_host\_cmd\_rx\_ctx rx\_ctx

**Definition** ec\_host\_cmd.h:94

[ec\_host\_cmd::state](structec__host__cmd.md#a444f295157c5ada6162aea803ff219e1)

enum ec\_host\_cmd\_state state

**Definition** ec\_host\_cmd.h:110

[ec\_host\_cmd::rx\_ready](structec__host__cmd.md#a465d588b50f0a881e7f1d8b761c4288f)

struct k\_sem rx\_ready

The backend gives rx\_ready (by calling the ec\_host\_cmd\_send\_receive function), when data in rx\_ctx ar...

**Definition** ec\_host\_cmd.h:101

[ec\_host\_cmd::user\_data](structec__host__cmd.md#a7982f079e67180de58ebd0a6f0f5d7e0)

void \* user\_data

**Definition** ec\_host\_cmd.h:109

[ec\_host\_cmd::backend](structec__host__cmd.md#ad269f3223fc0885ba5c847b4443c993c)

struct ec\_host\_cmd\_backend \* backend

**Definition** ec\_host\_cmd.h:96

[ec\_host\_cmd::user\_cb](structec__host__cmd.md#ad2f10eda2e6c2743d9c3068bda4deb7c)

ec\_host\_cmd\_user\_cb\_t user\_cb

User callback after receiving a command.

**Definition** ec\_host\_cmd.h:108

[ec\_host\_cmd::tx](structec__host__cmd.md#af1a3f483c1a7ddb88db187e406caa08d)

struct ec\_host\_cmd\_tx\_buf tx

**Definition** ec\_host\_cmd.h:95

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [ec\_host\_cmd](dir_d53ada025add0f463456d44507c0d96c.md)
- [ec\_host\_cmd.h](ec__host__cmd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
