---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sip__svc__proto_8h_source.html
original_path: doxygen/html/sip__svc__proto_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_proto.h

[Go to the documentation of this file.](sip__svc__proto_8h.md)

1/\*

2 \* Copyright (c) 2023, Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SIP\_SVC\_PROTO\_H\_

8#define ZEPHYR\_INCLUDE\_SIP\_SVC\_PROTO\_H\_

9

21

[ 25](sip__svc__proto_8h.md#ad1cb9509a40e51809b13f1fccf0f35ba)#define SIP\_SVC\_ID\_INVALID 0xFFFFFFFF

26

29

[ 30](sip__svc__proto_8h.md#a5544d9131eef67538c3a36bdfec5482e)#define SIP\_SVC\_PROTO\_VER 0x0

31

[ 32](sip__svc__proto_8h.md#a218d17af00117be8baf393e6b95cd9b2)#define SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET 0

[ 33](sip__svc__proto_8h.md#aa8dbe689b3b375f72d049a89389ff591)#define SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK 0xFFFF

34

[ 35](sip__svc__proto_8h.md#a4f147d26b354026e01225395e3f074ce)#define SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET 16

[ 36](sip__svc__proto_8h.md#a2da7d9fd032cf43814b535f7b9ff9028)#define SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK 0xFF

37

[ 38](sip__svc__proto_8h.md#a10ce84feaee4a6454c36dc3daf4f7722)#define SIP\_SVC\_PROTO\_HEADER\_VER\_OFFSET 30

[ 39](sip__svc__proto_8h.md#a8ffae8b2e3adb78378308944fb38601e)#define SIP\_SVC\_PROTO\_HEADER\_VER\_MASK 0x3

40

[ 41](sip__svc__proto_8h.md#a8ad11e26b133a65a94877930e74afa90)#define SIP\_SVC\_PROTO\_HEADER(code, trans\_id) \

42 ((((code)&SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK) << SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET) | \

43 (((trans\_id)&SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK) \

44 << SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET) | \

45 ((SIP\_SVC\_PROTO\_VER & SIP\_SVC\_PROTO\_HEADER\_VER\_MASK) << SIP\_SVC\_PROTO\_HEADER\_VER\_OFFSET))

46

[ 47](sip__svc__proto_8h.md#a365877f6f62717cb3f271666fa392d8e)#define SIP\_SVC\_PROTO\_HEADER\_GET\_CODE(header) \

48 (((header) >> SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET) & SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK)

49

[ 50](sip__svc__proto_8h.md#a4badc2fa72b4d5ae55c9b6503e3d2f41)#define SIP\_SVC\_PROTO\_HEADER\_GET\_TRANS\_ID(header) \

51 (((header) >> SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET) & SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK)

52

[ 53](sip__svc__proto_8h.md#a57124f787454b1253737bdde7ad04c6f)#define SIP\_SVC\_PROTO\_HEADER\_SET\_TRANS\_ID(header, trans\_id) \

54 (header) &= ~(SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK << SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET); \

55 (header) |= (((trans\_id)&SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK) \

56 << SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET);

57

69

[ 70](sip__svc__proto_8h.md#a6ea30874bbe6393807ccc8c02038cc30)#define SIP\_SVC\_PROTO\_CMD\_SYNC 0x0

[ 71](sip__svc__proto_8h.md#a8bc75a10006e42097f74edf990fa1f16)#define SIP\_SVC\_PROTO\_CMD\_ASYNC 0x1

[ 72](sip__svc__proto_8h.md#a8d7c4970ff149584080532c7bfa0cd51)#define SIP\_SVC\_PROTO\_CMD\_MAX SIP\_SVC\_PROTO\_CMD\_ASYNC

73

97

[ 98](sip__svc__proto_8h.md#af4153e73a6024d7d4355e9373f10388b)#define SIP\_SVC\_PROTO\_STATUS\_OK 0x0

[ 99](sip__svc__proto_8h.md#a1c7567c532ab25d3d21ed76c655b9680)#define SIP\_SVC\_PROTO\_STATUS\_UNKNOWN 0xFFFF

[ 100](sip__svc__proto_8h.md#aeae6b273da4e3e91f0a6ee2558a7585f)#define SIP\_SVC\_PROTO\_STATUS\_BUSY 0x1

[ 101](sip__svc__proto_8h.md#aa777087a721423e0e65cac4949813aaf)#define SIP\_SVC\_PROTO\_STATUS\_REJECT 0x2

[ 102](sip__svc__proto_8h.md#afba704d63c783fdd3d143045ca260706)#define SIP\_SVC\_PROTO\_STATUS\_NO\_RESPONSE 0x3

[ 103](sip__svc__proto_8h.md#a0d92a17202ff227476277500f539fd51)#define SIP\_SVC\_PROTO\_STATUS\_ERROR 0x4

104

132

[ 133](structsip__svc__request.md)struct [sip\_svc\_request](structsip__svc__request.md) {

[ 134](structsip__svc__request.md#aa8c71f7af00dd3195d49c04df5cb3509) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [header](structsip__svc__request.md#aa8c71f7af00dd3195d49c04df5cb3509);

[ 135](structsip__svc__request.md#a95e4d0bb03bfca90ea78fc19c581ef7f) unsigned long [a0](structsip__svc__request.md#a95e4d0bb03bfca90ea78fc19c581ef7f);

[ 136](structsip__svc__request.md#a3b41176de28f042510d5ca5fc9c4678e) unsigned long [a1](structsip__svc__request.md#a3b41176de28f042510d5ca5fc9c4678e);

[ 137](structsip__svc__request.md#aa20d78ab299064e8d4b304f4165bfdf2) unsigned long [a2](structsip__svc__request.md#aa20d78ab299064e8d4b304f4165bfdf2);

[ 138](structsip__svc__request.md#a6cd5c3cf895daad0c600544a903f2eb8) unsigned long [a3](structsip__svc__request.md#a6cd5c3cf895daad0c600544a903f2eb8);

[ 139](structsip__svc__request.md#a8d827ae174a2b8f11b50c7e6f31c3708) unsigned long [a4](structsip__svc__request.md#a8d827ae174a2b8f11b50c7e6f31c3708);

[ 140](structsip__svc__request.md#a67c7626f24035b9cdfef24193e2442c6) unsigned long [a5](structsip__svc__request.md#a67c7626f24035b9cdfef24193e2442c6);

[ 141](structsip__svc__request.md#a35198a51b070fb2acf76458568204ec1) unsigned long [a6](structsip__svc__request.md#a35198a51b070fb2acf76458568204ec1);

[ 142](structsip__svc__request.md#af20b0881ec14973d7a6b79f3b146dc7a) unsigned long [a7](structsip__svc__request.md#af20b0881ec14973d7a6b79f3b146dc7a);

[ 143](structsip__svc__request.md#a9b4cc837fbb958e93a900b58b2ea3a75) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [resp\_data\_addr](structsip__svc__request.md#a9b4cc837fbb958e93a900b58b2ea3a75);

[ 144](structsip__svc__request.md#aff7c782bc6690ef134db4e4d999189a7) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [resp\_data\_size](structsip__svc__request.md#aff7c782bc6690ef134db4e4d999189a7);

[ 145](structsip__svc__request.md#a0b70942fc037346bb5ee051484c21745) void \*[priv\_data](structsip__svc__request.md#a0b70942fc037346bb5ee051484c21745);

146};

147

176

[ 177](structsip__svc__response.md)struct [sip\_svc\_response](structsip__svc__response.md) {

[ 178](structsip__svc__response.md#ab2a3ed6ec283ef83a2ad8ea8eea421be) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [header](structsip__svc__response.md#ab2a3ed6ec283ef83a2ad8ea8eea421be);

[ 179](structsip__svc__response.md#a4f413e152dc2ef463140499164c3e410) unsigned long [a0](structsip__svc__response.md#a4f413e152dc2ef463140499164c3e410);

[ 180](structsip__svc__response.md#abfb0f411524209388f79f35a82031e79) unsigned long [a1](structsip__svc__response.md#abfb0f411524209388f79f35a82031e79);

[ 181](structsip__svc__response.md#af973d08da13a7dcecf344f3f9d6f118e) unsigned long [a2](structsip__svc__response.md#af973d08da13a7dcecf344f3f9d6f118e);

[ 182](structsip__svc__response.md#aac8bb11e4661e59cbce0d6b5d50a0820) unsigned long [a3](structsip__svc__response.md#aac8bb11e4661e59cbce0d6b5d50a0820);

[ 183](structsip__svc__response.md#a5b8a49d292e45ecdd81920c30b650c10) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [resp\_data\_addr](structsip__svc__response.md#a5b8a49d292e45ecdd81920c30b650c10);

[ 184](structsip__svc__response.md#a2e8373be61b16ac4f4d013103539cceb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [resp\_data\_size](structsip__svc__response.md#a2e8373be61b16ac4f4d013103539cceb);

[ 185](structsip__svc__response.md#a992b3f936866852633569f9c8d37d6a0) void \*[priv\_data](structsip__svc__response.md#a992b3f936866852633569f9c8d37d6a0);

186};

187

188#endif /\* ZEPHYR\_INCLUDE\_SIP\_SVC\_PROTO\_H\_ \*/

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[sip\_svc\_request](structsip__svc__request.md)

SiP Service communication protocol request format.

**Definition** sip\_svc\_proto.h:133

[sip\_svc\_request::priv\_data](structsip__svc__request.md#a0b70942fc037346bb5ee051484c21745)

void \* priv\_data

**Definition** sip\_svc\_proto.h:145

[sip\_svc\_request::a6](structsip__svc__request.md#a35198a51b070fb2acf76458568204ec1)

unsigned long a6

**Definition** sip\_svc\_proto.h:141

[sip\_svc\_request::a1](structsip__svc__request.md#a3b41176de28f042510d5ca5fc9c4678e)

unsigned long a1

**Definition** sip\_svc\_proto.h:136

[sip\_svc\_request::a5](structsip__svc__request.md#a67c7626f24035b9cdfef24193e2442c6)

unsigned long a5

**Definition** sip\_svc\_proto.h:140

[sip\_svc\_request::a3](structsip__svc__request.md#a6cd5c3cf895daad0c600544a903f2eb8)

unsigned long a3

**Definition** sip\_svc\_proto.h:138

[sip\_svc\_request::a4](structsip__svc__request.md#a8d827ae174a2b8f11b50c7e6f31c3708)

unsigned long a4

**Definition** sip\_svc\_proto.h:139

[sip\_svc\_request::a0](structsip__svc__request.md#a95e4d0bb03bfca90ea78fc19c581ef7f)

unsigned long a0

**Definition** sip\_svc\_proto.h:135

[sip\_svc\_request::resp\_data\_addr](structsip__svc__request.md#a9b4cc837fbb958e93a900b58b2ea3a75)

uint64\_t resp\_data\_addr

**Definition** sip\_svc\_proto.h:143

[sip\_svc\_request::a2](structsip__svc__request.md#aa20d78ab299064e8d4b304f4165bfdf2)

unsigned long a2

**Definition** sip\_svc\_proto.h:137

[sip\_svc\_request::header](structsip__svc__request.md#aa8c71f7af00dd3195d49c04df5cb3509)

uint32\_t header

**Definition** sip\_svc\_proto.h:134

[sip\_svc\_request::a7](structsip__svc__request.md#af20b0881ec14973d7a6b79f3b146dc7a)

unsigned long a7

**Definition** sip\_svc\_proto.h:142

[sip\_svc\_request::resp\_data\_size](structsip__svc__request.md#aff7c782bc6690ef134db4e4d999189a7)

uint32\_t resp\_data\_size

**Definition** sip\_svc\_proto.h:144

[sip\_svc\_response](structsip__svc__response.md)

SiP Services service communication protocol response format.

**Definition** sip\_svc\_proto.h:177

[sip\_svc\_response::resp\_data\_size](structsip__svc__response.md#a2e8373be61b16ac4f4d013103539cceb)

uint32\_t resp\_data\_size

**Definition** sip\_svc\_proto.h:184

[sip\_svc\_response::a0](structsip__svc__response.md#a4f413e152dc2ef463140499164c3e410)

unsigned long a0

**Definition** sip\_svc\_proto.h:179

[sip\_svc\_response::resp\_data\_addr](structsip__svc__response.md#a5b8a49d292e45ecdd81920c30b650c10)

uint64\_t resp\_data\_addr

**Definition** sip\_svc\_proto.h:183

[sip\_svc\_response::priv\_data](structsip__svc__response.md#a992b3f936866852633569f9c8d37d6a0)

void \* priv\_data

**Definition** sip\_svc\_proto.h:185

[sip\_svc\_response::a3](structsip__svc__response.md#aac8bb11e4661e59cbce0d6b5d50a0820)

unsigned long a3

**Definition** sip\_svc\_proto.h:182

[sip\_svc\_response::header](structsip__svc__response.md#ab2a3ed6ec283ef83a2ad8ea8eea421be)

uint32\_t header

**Definition** sip\_svc\_proto.h:178

[sip\_svc\_response::a1](structsip__svc__response.md#abfb0f411524209388f79f35a82031e79)

unsigned long a1

**Definition** sip\_svc\_proto.h:180

[sip\_svc\_response::a2](structsip__svc__response.md#af973d08da13a7dcecf344f3f9d6f118e)

unsigned long a2

**Definition** sip\_svc\_proto.h:181

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sip\_svc](dir_be59f4c2e7724c8d2ef47362c82e9052.md)
- [sip\_svc\_proto.h](sip__svc__proto_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
