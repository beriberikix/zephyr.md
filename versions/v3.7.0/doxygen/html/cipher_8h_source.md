---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cipher_8h_source.html
original_path: doxygen/html/cipher_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cipher.h

[Go to the documentation of this file.](cipher_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

16

17#ifndef ZEPHYR\_INCLUDE\_CRYPTO\_CIPHER\_H\_

18#define ZEPHYR\_INCLUDE\_CRYPTO\_CIPHER\_H\_

19

20#include <[zephyr/device.h](device_8h.md)>

21#include <[zephyr/sys/util.h](util_8h.md)>

26

27

[ 29](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424)enum [cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424) {

[ 30](group__crypto__cipher.md#ggaa43d9907b508cb28c649aaa524d84424aed0c05202ecbb1496f84ec6c383ddcf0) [CRYPTO\_CIPHER\_ALGO\_AES](group__crypto__cipher.md#ggaa43d9907b508cb28c649aaa524d84424aed0c05202ecbb1496f84ec6c383ddcf0) = 1,

31};

32

[ 34](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21)enum [cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21) {

[ 35](group__crypto__cipher.md#gga1db3a5604bff0669672af4457aaaee21a1e1205f695285034b4889ac19a191617) [CRYPTO\_CIPHER\_OP\_DECRYPT](group__crypto__cipher.md#gga1db3a5604bff0669672af4457aaaee21a1e1205f695285034b4889ac19a191617) = 0,

[ 36](group__crypto__cipher.md#gga1db3a5604bff0669672af4457aaaee21a71bf6ee186bab1729e24e37c119d0019) [CRYPTO\_CIPHER\_OP\_ENCRYPT](group__crypto__cipher.md#gga1db3a5604bff0669672af4457aaaee21a71bf6ee186bab1729e24e37c119d0019) = 1,

37};

38

[ 44](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43)enum [cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43) {

[ 45](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a30ffc1c7c1489f938ed8c567a4fb885e) [CRYPTO\_CIPHER\_MODE\_ECB](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a30ffc1c7c1489f938ed8c567a4fb885e) = 1,

[ 46](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a98034da3b89ae5c47749c59a3b15bbfd) [CRYPTO\_CIPHER\_MODE\_CBC](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a98034da3b89ae5c47749c59a3b15bbfd) = 2,

[ 47](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a58823b401487d57d62a067d71bd2e9d2) [CRYPTO\_CIPHER\_MODE\_CTR](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a58823b401487d57d62a067d71bd2e9d2) = 3,

[ 48](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a5116e1683b8c9c26582863a65128ce3b) [CRYPTO\_CIPHER\_MODE\_CCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a5116e1683b8c9c26582863a65128ce3b) = 4,

[ 49](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a2f0de7c8f0b9c1a8ac7343ca3ca72c12) [CRYPTO\_CIPHER\_MODE\_GCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a2f0de7c8f0b9c1a8ac7343ca3ca72c12) = 5,

50};

51

52/\* Forward declarations \*/

53struct [cipher\_aead\_pkt](structcipher__aead__pkt.md);

54struct [cipher\_ctx](structcipher__ctx.md);

55struct [cipher\_pkt](structcipher__pkt.md);

56

[ 57](group__crypto__cipher.md#ga584073236a507f736442dedab87b1e17)typedef int (\*[block\_op\_t](group__crypto__cipher.md#ga584073236a507f736442dedab87b1e17))(struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt);

58

59/\* Function signatures for encryption/ decryption using standard cipher modes

60 \* like CBC, CTR, CCM.

61 \*/

[ 62](group__crypto__cipher.md#gaa74d09d409b42b29c4c7045dc77552d2)typedef int (\*[cbc\_op\_t](group__crypto__cipher.md#gaa74d09d409b42b29c4c7045dc77552d2))(struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt,

63 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*iv);

64

[ 65](group__crypto__cipher.md#gad1ed48328ca31f8ce2dd7e0a166cacba)typedef int (\*[ctr\_op\_t](group__crypto__cipher.md#gad1ed48328ca31f8ce2dd7e0a166cacba))(struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_pkt](structcipher__pkt.md) \*pkt,

66 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ctr);

67

[ 68](group__crypto__cipher.md#ga55e4d15dde1a5134c695ce0c31dabaf7)typedef int (\*[ccm\_op\_t](group__crypto__cipher.md#ga55e4d15dde1a5134c695ce0c31dabaf7))(struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*[pkt](structcipher__aead__pkt.md#a4953711ca04b1c1d17980fff03561d03),

69 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce);

70

[ 71](group__crypto__cipher.md#gad27577142dd49308b2470253a41bd09d)typedef int (\*[gcm\_op\_t](group__crypto__cipher.md#gad27577142dd49308b2470253a41bd09d))(struct [cipher\_ctx](structcipher__ctx.md) \*ctx, struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) \*[pkt](structcipher__aead__pkt.md#a4953711ca04b1c1d17980fff03561d03),

72 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*nonce);

73

[ 74](structcipher__ops.md)struct [cipher\_ops](structcipher__ops.md) {

75

[ 76](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4) enum [cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4) [cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4);

77

78 union {

[ 79](structcipher__ops.md#a2675dd312be240c24d7d2c0e81bcde2b) [block\_op\_t](group__crypto__cipher.md#ga584073236a507f736442dedab87b1e17) [block\_crypt\_hndlr](structcipher__ops.md#a2675dd312be240c24d7d2c0e81bcde2b);

[ 80](structcipher__ops.md#abc7cf6306467c5aff24ae3faa37902e6) [cbc\_op\_t](group__crypto__cipher.md#gaa74d09d409b42b29c4c7045dc77552d2) [cbc\_crypt\_hndlr](structcipher__ops.md#abc7cf6306467c5aff24ae3faa37902e6);

[ 81](structcipher__ops.md#ac792113d841e3a6b7dc107d7123162db) [ctr\_op\_t](group__crypto__cipher.md#gad1ed48328ca31f8ce2dd7e0a166cacba) [ctr\_crypt\_hndlr](structcipher__ops.md#ac792113d841e3a6b7dc107d7123162db);

[ 82](structcipher__ops.md#af53f5f04fb5e1a7ca148f786d8cfe41f) [ccm\_op\_t](group__crypto__cipher.md#ga55e4d15dde1a5134c695ce0c31dabaf7) [ccm\_crypt\_hndlr](structcipher__ops.md#af53f5f04fb5e1a7ca148f786d8cfe41f);

[ 83](structcipher__ops.md#a570d1ed37d6cce61caa1c6e257f9cdc8) [gcm\_op\_t](group__crypto__cipher.md#gad27577142dd49308b2470253a41bd09d) [gcm\_crypt\_hndlr](structcipher__ops.md#a570d1ed37d6cce61caa1c6e257f9cdc8);

84 };

85};

86

[ 87](structccm__params.md)struct [ccm\_params](structccm__params.md) {

[ 88](structccm__params.md#a6a0d01056dcc05e2f7dccef25d4c5747) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tag\_len](structccm__params.md#a6a0d01056dcc05e2f7dccef25d4c5747);

[ 89](structccm__params.md#adbc306823d339083ec439277a7e35e8a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nonce\_len](structccm__params.md#adbc306823d339083ec439277a7e35e8a);

90};

91

[ 92](structctr__params.md)struct [ctr\_params](structctr__params.md) {

93 /\* CTR mode counter is a split counter composed of iv and counter

94 \* such that ivlen + ctr\_len = keylen

95 \*/

[ 96](structctr__params.md#a8187ad9553ff8b223f39c14919c48b70) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ctr\_len](structctr__params.md#a8187ad9553ff8b223f39c14919c48b70);

97};

98

[ 99](structgcm__params.md)struct [gcm\_params](structgcm__params.md) {

[ 100](structgcm__params.md#a4fd478dee1eedfd75ab77e8e63bcbf40) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tag\_len](structgcm__params.md#a4fd478dee1eedfd75ab77e8e63bcbf40);

[ 101](structgcm__params.md#ae4458a261310577778fca927e7fdc829) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [nonce\_len](structgcm__params.md#ae4458a261310577778fca927e7fdc829);

102};

103

[ 110](structcipher__ctx.md)struct [cipher\_ctx](structcipher__ctx.md) {

111

[ 116](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682) struct [cipher\_ops](structcipher__ops.md) [ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682);

117

119 union {

120 /\* Cryptographic key to be used in this session \*/

[ 121](structcipher__ctx.md#abc8f2818fcb3a83c3c00805a55e5805d) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[bit\_stream](structcipher__ctx.md#abc8f2818fcb3a83c3c00805a55e5805d);

122 /\* For cases where key is protected and is not

123 \* available to caller

124 \*/

[ 125](structcipher__ctx.md#a81dfa0793e62065a247bd3d5b5bdc903) void \*[handle](structcipher__ctx.md#a81dfa0793e62065a247bd3d5b5bdc903);

[ 126](structcipher__ctx.md#a441096f011ad26e2ba6411bdd98eb0a2) } [key](structcipher__ctx.md#a441096f011ad26e2ba6411bdd98eb0a2);

127

[ 131](structcipher__ctx.md#a44842ea8ece2aaea4d757137cdb67b52) const struct [device](structcipher__ctx.md#a44842ea8ece2aaea4d757137cdb67b52) \*[device](structcipher__ctx.md#a44842ea8ece2aaea4d757137cdb67b52);

132

[ 140](structcipher__ctx.md#a624cf985cf35b3aa8681c3892fd67429) void \*[drv\_sessn\_state](structcipher__ctx.md#a624cf985cf35b3aa8681c3892fd67429);

141

[ 146](structcipher__ctx.md#a0439c7f7c300a59296d353e76132c028) void \*[app\_sessn\_state](structcipher__ctx.md#a0439c7f7c300a59296d353e76132c028);

147

152 union {

[ 153](structcipher__ctx.md#a3b6f3cdda6344880f3dcc3e2c8246b15) struct [ccm\_params](structccm__params.md) [ccm\_info](structcipher__ctx.md#a3b6f3cdda6344880f3dcc3e2c8246b15);

[ 154](structcipher__ctx.md#a8a7b59087bd474eaad8d996e1600e757) struct [ctr\_params](structctr__params.md) [ctr\_info](structcipher__ctx.md#a8a7b59087bd474eaad8d996e1600e757);

[ 155](structcipher__ctx.md#a995276020bd2ef77451d941fa3b238d2) struct [gcm\_params](structgcm__params.md) [gcm\_info](structcipher__ctx.md#a995276020bd2ef77451d941fa3b238d2);

[ 156](structcipher__ctx.md#aa0f89473a5d1d6417a128bb452982db7) } [mode\_params](structcipher__ctx.md#aa0f89473a5d1d6417a128bb452982db7);

157

[ 161](structcipher__ctx.md#a10dbfc431a748118c186099c249ed5e4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [keylen](structcipher__ctx.md#a10dbfc431a748118c186099c249ed5e4);

162

[ 169](structcipher__ctx.md#a5745811b9b08e6df51f9b8f8b14ceae7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structcipher__ctx.md#a5745811b9b08e6df51f9b8f8b14ceae7);

170};

171

[ 180](structcipher__pkt.md)struct [cipher\_pkt](structcipher__pkt.md) {

181

[ 183](structcipher__pkt.md#a56d2de56d9efc153032eb7f6503748ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[in\_buf](structcipher__pkt.md#a56d2de56d9efc153032eb7f6503748ba);

184

[ 186](structcipher__pkt.md#ac5c98e7edafb4b61e01f707c785afbea) int [in\_len](structcipher__pkt.md#ac5c98e7edafb4b61e01f707c785afbea);

187

[ 192](structcipher__pkt.md#ab95bae428d3d3c80b1b8ee6ea03a05d0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[out\_buf](structcipher__pkt.md#ab95bae428d3d3c80b1b8ee6ea03a05d0);

193

[ 197](structcipher__pkt.md#a6e51f941334e87cc966f5a37e783d1fc) int [out\_buf\_max](structcipher__pkt.md#a6e51f941334e87cc966f5a37e783d1fc);

198

[ 202](structcipher__pkt.md#abc9588a5f84f9daa13ce4aec965f0a91) int [out\_len](structcipher__pkt.md#abc9588a5f84f9daa13ce4aec965f0a91);

203

[ 208](structcipher__pkt.md#a26fb877d705580648da03ce95264d100) struct [cipher\_ctx](structcipher__ctx.md) \*[ctx](structcipher__pkt.md#a26fb877d705580648da03ce95264d100);

209};

210

[ 217](structcipher__aead__pkt.md)struct [cipher\_aead\_pkt](structcipher__aead__pkt.md) {

218 /\* IO buffers for encryption. This has to be supplied by the app. \*/

[ 219](structcipher__aead__pkt.md#a4953711ca04b1c1d17980fff03561d03) struct [cipher\_pkt](structcipher__pkt.md) \*[pkt](structcipher__aead__pkt.md#a4953711ca04b1c1d17980fff03561d03);

220

[ 224](structcipher__aead__pkt.md#a1b00939c8409041b8202ae90ee01a41c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ad](structcipher__aead__pkt.md#a1b00939c8409041b8202ae90ee01a41c);

225

[ 227](structcipher__aead__pkt.md#a2964d6ffbe02b7088be9a2d5c21a2f9c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ad\_len](structcipher__aead__pkt.md#a2964d6ffbe02b7088be9a2d5c21a2f9c);

228

[ 233](structcipher__aead__pkt.md#a3c7a3e72c7d21ec574dd777ac0bdf3c4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[tag](structcipher__aead__pkt.md#a3c7a3e72c7d21ec574dd777ac0bdf3c4);

234};

235

236/\* Prototype for the application function to be invoked by the crypto driver

237 \* on completion of an async request. The app may get the session context

238 \* via the pkt->ctx field. For CCM ops the encompassing AEAD packet may be

239 \* accessed via container\_of(). The type of a packet can be determined via

240 \* pkt->ctx.ops.mode .

241 \*/

[ 242](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd)typedef void (\*[cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd))(struct [cipher\_pkt](structcipher__pkt.md) \*completed, int status);

243

247#endif /\* ZEPHYR\_INCLUDE\_CRYPTO\_CIPHER\_H\_ \*/

[device.h](device_8h.md)

[cipher\_completion\_cb](group__crypto__cipher.md#ga062b07459bcc2990535465a7b9044ecd)

void(\* cipher\_completion\_cb)(struct cipher\_pkt \*completed, int status)

**Definition** cipher.h:242

[cipher\_op](group__crypto__cipher.md#ga1db3a5604bff0669672af4457aaaee21)

cipher\_op

Cipher Operation.

**Definition** cipher.h:34

[ccm\_op\_t](group__crypto__cipher.md#ga55e4d15dde1a5134c695ce0c31dabaf7)

int(\* ccm\_op\_t)(struct cipher\_ctx \*ctx, struct cipher\_aead\_pkt \*pkt, uint8\_t \*nonce)

**Definition** cipher.h:68

[block\_op\_t](group__crypto__cipher.md#ga584073236a507f736442dedab87b1e17)

int(\* block\_op\_t)(struct cipher\_ctx \*ctx, struct cipher\_pkt \*pkt)

**Definition** cipher.h:57

[cipher\_algo](group__crypto__cipher.md#gaa43d9907b508cb28c649aaa524d84424)

cipher\_algo

Cipher Algorithm.

**Definition** cipher.h:29

[cbc\_op\_t](group__crypto__cipher.md#gaa74d09d409b42b29c4c7045dc77552d2)

int(\* cbc\_op\_t)(struct cipher\_ctx \*ctx, struct cipher\_pkt \*pkt, uint8\_t \*iv)

**Definition** cipher.h:62

[ctr\_op\_t](group__crypto__cipher.md#gad1ed48328ca31f8ce2dd7e0a166cacba)

int(\* ctr\_op\_t)(struct cipher\_ctx \*ctx, struct cipher\_pkt \*pkt, uint8\_t \*ctr)

**Definition** cipher.h:65

[gcm\_op\_t](group__crypto__cipher.md#gad27577142dd49308b2470253a41bd09d)

int(\* gcm\_op\_t)(struct cipher\_ctx \*ctx, struct cipher\_aead\_pkt \*pkt, uint8\_t \*nonce)

**Definition** cipher.h:71

[cipher\_mode](group__crypto__cipher.md#gaeedaf8017f8d6518f7dedef365bbae43)

cipher\_mode

Possible cipher mode options.

**Definition** cipher.h:44

[CRYPTO\_CIPHER\_OP\_DECRYPT](group__crypto__cipher.md#gga1db3a5604bff0669672af4457aaaee21a1e1205f695285034b4889ac19a191617)

@ CRYPTO\_CIPHER\_OP\_DECRYPT

**Definition** cipher.h:35

[CRYPTO\_CIPHER\_OP\_ENCRYPT](group__crypto__cipher.md#gga1db3a5604bff0669672af4457aaaee21a71bf6ee186bab1729e24e37c119d0019)

@ CRYPTO\_CIPHER\_OP\_ENCRYPT

**Definition** cipher.h:36

[CRYPTO\_CIPHER\_ALGO\_AES](group__crypto__cipher.md#ggaa43d9907b508cb28c649aaa524d84424aed0c05202ecbb1496f84ec6c383ddcf0)

@ CRYPTO\_CIPHER\_ALGO\_AES

**Definition** cipher.h:30

[CRYPTO\_CIPHER\_MODE\_GCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a2f0de7c8f0b9c1a8ac7343ca3ca72c12)

@ CRYPTO\_CIPHER\_MODE\_GCM

**Definition** cipher.h:49

[CRYPTO\_CIPHER\_MODE\_ECB](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a30ffc1c7c1489f938ed8c567a4fb885e)

@ CRYPTO\_CIPHER\_MODE\_ECB

**Definition** cipher.h:45

[CRYPTO\_CIPHER\_MODE\_CCM](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a5116e1683b8c9c26582863a65128ce3b)

@ CRYPTO\_CIPHER\_MODE\_CCM

**Definition** cipher.h:48

[CRYPTO\_CIPHER\_MODE\_CTR](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a58823b401487d57d62a067d71bd2e9d2)

@ CRYPTO\_CIPHER\_MODE\_CTR

**Definition** cipher.h:47

[CRYPTO\_CIPHER\_MODE\_CBC](group__crypto__cipher.md#ggaeedaf8017f8d6518f7dedef365bbae43a98034da3b89ae5c47749c59a3b15bbfd)

@ CRYPTO\_CIPHER\_MODE\_CBC

**Definition** cipher.h:46

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ccm\_params](structccm__params.md)

**Definition** cipher.h:87

[ccm\_params::tag\_len](structccm__params.md#a6a0d01056dcc05e2f7dccef25d4c5747)

uint16\_t tag\_len

**Definition** cipher.h:88

[ccm\_params::nonce\_len](structccm__params.md#adbc306823d339083ec439277a7e35e8a)

uint16\_t nonce\_len

**Definition** cipher.h:89

[cipher\_aead\_pkt](structcipher__aead__pkt.md)

Structure encoding IO parameters in AEAD (Authenticated Encryption with Associated Data) scenario lik...

**Definition** cipher.h:217

[cipher\_aead\_pkt::ad](structcipher__aead__pkt.md#a1b00939c8409041b8202ae90ee01a41c)

uint8\_t \* ad

Start address for Associated Data.

**Definition** cipher.h:224

[cipher\_aead\_pkt::ad\_len](structcipher__aead__pkt.md#a2964d6ffbe02b7088be9a2d5c21a2f9c)

uint32\_t ad\_len

Size of Associated Data.

**Definition** cipher.h:227

[cipher\_aead\_pkt::tag](structcipher__aead__pkt.md#a3c7a3e72c7d21ec574dd777ac0bdf3c4)

uint8\_t \* tag

Start address for the auth hash.

**Definition** cipher.h:233

[cipher\_aead\_pkt::pkt](structcipher__aead__pkt.md#a4953711ca04b1c1d17980fff03561d03)

struct cipher\_pkt \* pkt

**Definition** cipher.h:219

[cipher\_ctx](structcipher__ctx.md)

Structure encoding session parameters.

**Definition** cipher.h:110

[cipher\_ctx::app\_sessn\_state](structcipher__ctx.md#a0439c7f7c300a59296d353e76132c028)

void \* app\_sessn\_state

Place for the user app to put info relevant stuff for resuming when completion callback happens for a...

**Definition** cipher.h:146

[cipher\_ctx::keylen](structcipher__ctx.md#a10dbfc431a748118c186099c249ed5e4)

uint16\_t keylen

Cryptographic keylength in bytes.

**Definition** cipher.h:161

[cipher\_ctx::ccm\_info](structcipher__ctx.md#a3b6f3cdda6344880f3dcc3e2c8246b15)

struct ccm\_params ccm\_info

**Definition** cipher.h:153

[cipher\_ctx::key](structcipher__ctx.md#a441096f011ad26e2ba6411bdd98eb0a2)

union cipher\_ctx::@252266264254052346115200201223263334036213076237 key

To be populated by the app before calling begin\_session().

[cipher\_ctx::device](structcipher__ctx.md#a44842ea8ece2aaea4d757137cdb67b52)

const struct device \* device

The device driver instance this crypto context relates to.

**Definition** cipher.h:131

[cipher\_ctx::flags](structcipher__ctx.md#a5745811b9b08e6df51f9b8f8b14ceae7)

uint16\_t flags

How certain fields are to be interpreted for this session.

**Definition** cipher.h:169

[cipher\_ctx::drv\_sessn\_state](structcipher__ctx.md#a624cf985cf35b3aa8681c3892fd67429)

void \* drv\_sessn\_state

If the driver supports multiple simultaneously crypto sessions, this will identify the specific drive...

**Definition** cipher.h:140

[cipher\_ctx::handle](structcipher__ctx.md#a81dfa0793e62065a247bd3d5b5bdc903)

void \* handle

**Definition** cipher.h:125

[cipher\_ctx::ctr\_info](structcipher__ctx.md#a8a7b59087bd474eaad8d996e1600e757)

struct ctr\_params ctr\_info

**Definition** cipher.h:154

[cipher\_ctx::gcm\_info](structcipher__ctx.md#a995276020bd2ef77451d941fa3b238d2)

struct gcm\_params gcm\_info

**Definition** cipher.h:155

[cipher\_ctx::mode\_params](structcipher__ctx.md#aa0f89473a5d1d6417a128bb452982db7)

union cipher\_ctx::@154152356303000122313150276277376275054131233366 mode\_params

Cypher mode parameters, which remain constant for all ops in a session.

[cipher\_ctx::bit\_stream](structcipher__ctx.md#abc8f2818fcb3a83c3c00805a55e5805d)

const uint8\_t \* bit\_stream

**Definition** cipher.h:121

[cipher\_ctx::ops](structcipher__ctx.md#ae3eb86d5be42450b761f89114723b682)

struct cipher\_ops ops

Place for driver to return function pointers to be invoked per cipher operation.

**Definition** cipher.h:116

[cipher\_ops](structcipher__ops.md)

**Definition** cipher.h:74

[cipher\_ops::block\_crypt\_hndlr](structcipher__ops.md#a2675dd312be240c24d7d2c0e81bcde2b)

block\_op\_t block\_crypt\_hndlr

**Definition** cipher.h:79

[cipher\_ops::gcm\_crypt\_hndlr](structcipher__ops.md#a570d1ed37d6cce61caa1c6e257f9cdc8)

gcm\_op\_t gcm\_crypt\_hndlr

**Definition** cipher.h:83

[cipher\_ops::cipher\_mode](structcipher__ops.md#a93c8c2c77d44ea013fbb6e7fd788d4d4)

enum cipher\_mode cipher\_mode

**Definition** cipher.h:76

[cipher\_ops::cbc\_crypt\_hndlr](structcipher__ops.md#abc7cf6306467c5aff24ae3faa37902e6)

cbc\_op\_t cbc\_crypt\_hndlr

**Definition** cipher.h:80

[cipher\_ops::ctr\_crypt\_hndlr](structcipher__ops.md#ac792113d841e3a6b7dc107d7123162db)

ctr\_op\_t ctr\_crypt\_hndlr

**Definition** cipher.h:81

[cipher\_ops::ccm\_crypt\_hndlr](structcipher__ops.md#af53f5f04fb5e1a7ca148f786d8cfe41f)

ccm\_op\_t ccm\_crypt\_hndlr

**Definition** cipher.h:82

[cipher\_pkt](structcipher__pkt.md)

Structure encoding IO parameters of one cryptographic operation like encrypt/decrypt.

**Definition** cipher.h:180

[cipher\_pkt::ctx](structcipher__pkt.md#a26fb877d705580648da03ce95264d100)

struct cipher\_ctx \* ctx

Context this packet relates to.

**Definition** cipher.h:208

[cipher\_pkt::in\_buf](structcipher__pkt.md#a56d2de56d9efc153032eb7f6503748ba)

uint8\_t \* in\_buf

Start address of input buffer.

**Definition** cipher.h:183

[cipher\_pkt::out\_buf\_max](structcipher__pkt.md#a6e51f941334e87cc966f5a37e783d1fc)

int out\_buf\_max

Size of the out\_buf area allocated by the application.

**Definition** cipher.h:197

[cipher\_pkt::out\_buf](structcipher__pkt.md#ab95bae428d3d3c80b1b8ee6ea03a05d0)

uint8\_t \* out\_buf

Start of the output buffer, to be allocated by the application.

**Definition** cipher.h:192

[cipher\_pkt::out\_len](structcipher__pkt.md#abc9588a5f84f9daa13ce4aec965f0a91)

int out\_len

To be populated by driver on return from cipher\_xxx\_op() and holds the size of the actual result.

**Definition** cipher.h:202

[cipher\_pkt::in\_len](structcipher__pkt.md#ac5c98e7edafb4b61e01f707c785afbea)

int in\_len

Bytes to be operated upon.

**Definition** cipher.h:186

[ctr\_params](structctr__params.md)

**Definition** cipher.h:92

[ctr\_params::ctr\_len](structctr__params.md#a8187ad9553ff8b223f39c14919c48b70)

uint32\_t ctr\_len

**Definition** cipher.h:96

[gcm\_params](structgcm__params.md)

**Definition** cipher.h:99

[gcm\_params::tag\_len](structgcm__params.md#a4fd478dee1eedfd75ab77e8e63bcbf40)

uint16\_t tag\_len

**Definition** cipher.h:100

[gcm\_params::nonce\_len](structgcm__params.md#ae4458a261310577778fca927e7fdc829)

uint16\_t nonce\_len

**Definition** cipher.h:101

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [crypto](dir_8e645738bb65aae54152153b1372b1b2.md)
- [cipher.h](cipher_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
