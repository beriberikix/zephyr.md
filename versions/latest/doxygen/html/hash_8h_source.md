---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hash_8h_source.html
original_path: doxygen/html/hash_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash.h

[Go to the documentation of this file.](hash_8h.md)

1/\*

2 \* Copyright (c) 2022 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13#ifndef ZEPHYR\_INCLUDE\_CRYPTO\_HASH\_H\_

14#define ZEPHYR\_INCLUDE\_CRYPTO\_HASH\_H\_

15

16

21

22

[ 26](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a)enum [hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a) {

[ 27](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aaa49fd348b98d55eca407ae88e3626265) [CRYPTO\_HASH\_ALGO\_SHA224](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aaa49fd348b98d55eca407ae88e3626265) = 1,

[ 28](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aa1b0b60a3270618fd492491668dc2ad43) [CRYPTO\_HASH\_ALGO\_SHA256](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aa1b0b60a3270618fd492491668dc2ad43) = 2,

[ 29](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aabba9e518a333ce75825957fde1993dd5) [CRYPTO\_HASH\_ALGO\_SHA384](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aabba9e518a333ce75825957fde1993dd5) = 3,

[ 30](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aa72a129765ae9e15f456c295c3917bf3f) [CRYPTO\_HASH\_ALGO\_SHA512](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aa72a129765ae9e15f456c295c3917bf3f) = 4,

31};

32

33/\* Forward declarations \*/

34struct [hash\_ctx](structhash__ctx.md);

35struct [hash\_pkt](structhash__pkt.md);

36

37

[ 38](group__crypto__hash.md#ga955369c6da6aa70ded229d8861292070)typedef int (\*[hash\_op\_t](group__crypto__hash.md#ga955369c6da6aa70ded229d8861292070))(struct [hash\_ctx](structhash__ctx.md) \*ctx, struct [hash\_pkt](structhash__pkt.md) \*pkt,

39 bool finish);

40

[ 47](structhash__ctx.md)struct [hash\_ctx](structhash__ctx.md) {

[ 51](structhash__ctx.md#abe1e70bd23305296e54564b5966ff310) const struct [device](structhash__ctx.md#abe1e70bd23305296e54564b5966ff310) \*[device](structhash__ctx.md#abe1e70bd23305296e54564b5966ff310);

52

[ 60](structhash__ctx.md#ad9c9bb4472975ba6999986bb6c01b501) void \*[drv\_sessn\_state](structhash__ctx.md#ad9c9bb4472975ba6999986bb6c01b501);

61

[ 65](structhash__ctx.md#a72a2e7af667bed1ee1dabb8411b01e40) [hash\_op\_t](group__crypto__hash.md#ga955369c6da6aa70ded229d8861292070) [hash\_hndlr](structhash__ctx.md#a72a2e7af667bed1ee1dabb8411b01e40);

66

[ 70](structhash__ctx.md#a33dbeb54cd8663f1f5391988d8ee642e) bool [started](structhash__ctx.md#a33dbeb54cd8663f1f5391988d8ee642e);

71

[ 78](structhash__ctx.md#ab550711912423a0eb03c410aef491854) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structhash__ctx.md#ab550711912423a0eb03c410aef491854);

79};

80

[ 88](structhash__pkt.md)struct [hash\_pkt](structhash__pkt.md) {

89

[ 91](structhash__pkt.md#a80d73d3c64718a62213a7fb857e3c5ce) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[in\_buf](structhash__pkt.md#a80d73d3c64718a62213a7fb857e3c5ce);

92

[ 94](structhash__pkt.md#a06c516ec59f233a2090fb37eb0476652) size\_t [in\_len](structhash__pkt.md#a06c516ec59f233a2090fb37eb0476652);

95

[ 101](structhash__pkt.md#ac86c2221c6ebe7c3e568c6d72b91ff43) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[out\_buf](structhash__pkt.md#ac86c2221c6ebe7c3e568c6d72b91ff43);

102

[ 107](structhash__pkt.md#ab5b3ffd87a11ce3838178b2e652d49b9) struct [hash\_ctx](structhash__ctx.md) \*[ctx](structhash__pkt.md#ab5b3ffd87a11ce3838178b2e652d49b9);

108};

109

110/\* Prototype for the application function to be invoked by the crypto driver

111 \* on completion of an async request. The app may get the session context

112 \* via the pkt->ctx field.

113 \*/

[ 114](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd)typedef void (\*[hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd))(struct [hash\_pkt](structhash__pkt.md) \*completed, int status);

115

116

120#endif /\* ZEPHYR\_INCLUDE\_CRYPTO\_HASH\_H\_ \*/

[hash\_completion\_cb](group__crypto__hash.md#ga1f49008c35d9f04b66e587d1b43404bd)

void(\* hash\_completion\_cb)(struct hash\_pkt \*completed, int status)

**Definition** hash.h:114

[hash\_op\_t](group__crypto__hash.md#ga955369c6da6aa70ded229d8861292070)

int(\* hash\_op\_t)(struct hash\_ctx \*ctx, struct hash\_pkt \*pkt, bool finish)

**Definition** hash.h:38

[hash\_algo](group__crypto__hash.md#gaaea88501aa8243eacc8c57ac0914ac7a)

hash\_algo

Hash algorithm.

**Definition** hash.h:26

[CRYPTO\_HASH\_ALGO\_SHA256](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aa1b0b60a3270618fd492491668dc2ad43)

@ CRYPTO\_HASH\_ALGO\_SHA256

**Definition** hash.h:28

[CRYPTO\_HASH\_ALGO\_SHA512](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aa72a129765ae9e15f456c295c3917bf3f)

@ CRYPTO\_HASH\_ALGO\_SHA512

**Definition** hash.h:30

[CRYPTO\_HASH\_ALGO\_SHA224](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aaa49fd348b98d55eca407ae88e3626265)

@ CRYPTO\_HASH\_ALGO\_SHA224

**Definition** hash.h:27

[CRYPTO\_HASH\_ALGO\_SHA384](group__crypto__hash.md#ggaaea88501aa8243eacc8c57ac0914ac7aabba9e518a333ce75825957fde1993dd5)

@ CRYPTO\_HASH\_ALGO\_SHA384

**Definition** hash.h:29

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[hash\_ctx](structhash__ctx.md)

Structure encoding session parameters.

**Definition** hash.h:47

[hash\_ctx::started](structhash__ctx.md#a33dbeb54cd8663f1f5391988d8ee642e)

bool started

If it has started a multipart hash operation.

**Definition** hash.h:70

[hash\_ctx::hash\_hndlr](structhash__ctx.md#a72a2e7af667bed1ee1dabb8411b01e40)

hash\_op\_t hash\_hndlr

Hash handler set up when the session begins.

**Definition** hash.h:65

[hash\_ctx::flags](structhash__ctx.md#ab550711912423a0eb03c410aef491854)

uint16\_t flags

How certain fields are to be interpreted for this session.

**Definition** hash.h:78

[hash\_ctx::device](structhash__ctx.md#abe1e70bd23305296e54564b5966ff310)

const struct device \* device

The device driver instance this crypto context relates to.

**Definition** hash.h:51

[hash\_ctx::drv\_sessn\_state](structhash__ctx.md#ad9c9bb4472975ba6999986bb6c01b501)

void \* drv\_sessn\_state

If the driver supports multiple simultaneously crypto sessions, this will identify the specific drive...

**Definition** hash.h:60

[hash\_pkt](structhash__pkt.md)

Structure encoding IO parameters of a hash operation.

**Definition** hash.h:88

[hash\_pkt::in\_len](structhash__pkt.md#a06c516ec59f233a2090fb37eb0476652)

size\_t in\_len

Bytes to be operated upon.

**Definition** hash.h:94

[hash\_pkt::in\_buf](structhash__pkt.md#a80d73d3c64718a62213a7fb857e3c5ce)

uint8\_t \* in\_buf

Start address of input buffer.

**Definition** hash.h:91

[hash\_pkt::ctx](structhash__pkt.md#ab5b3ffd87a11ce3838178b2e652d49b9)

struct hash\_ctx \* ctx

Context this packet relates to.

**Definition** hash.h:107

[hash\_pkt::out\_buf](structhash__pkt.md#ac86c2221c6ebe7c3e568c6d72b91ff43)

uint8\_t \* out\_buf

Start of the output buffer, to be allocated by the application.

**Definition** hash.h:101

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [crypto](dir_8e645738bb65aae54152153b1372b1b2.md)
- [hash.h](hash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
