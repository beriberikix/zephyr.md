---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/winstream_8h_source.html
original_path: doxygen/html/winstream_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

winstream.h

[Go to the documentation of this file.](winstream_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5#ifndef ZEPHYR\_INCLUDE\_SYS\_WINSTREAM\_H\_

6#define ZEPHYR\_INCLUDE\_SYS\_WINSTREAM\_H\_

7

8#include <[stdint.h](stdint_8h.md)>

9

[ 25](structsys__winstream.md)struct [sys\_winstream](structsys__winstream.md) {

[ 26](structsys__winstream.md#a30b03df76a51ecbf0cbe33975d5aaa66) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structsys__winstream.md#a30b03df76a51ecbf0cbe33975d5aaa66); /\* Length of data[] in bytes \*/

[ 27](structsys__winstream.md#a1cc84dfd9f812b3491135d13365c7a98) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [start](structsys__winstream.md#a1cc84dfd9f812b3491135d13365c7a98); /\* Index of first valid byte in data[] \*/

[ 28](structsys__winstream.md#a6b80cf715e4a3ca7b7b74b9efd150a23) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [end](structsys__winstream.md#a6b80cf715e4a3ca7b7b74b9efd150a23); /\* Index of next byte in data[] to write \*/

[ 29](structsys__winstream.md#a7d946d6a54652a8ac035dd8cd0ba861a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [seq](structsys__winstream.md#a7d946d6a54652a8ac035dd8cd0ba861a); /\* Mod-2^32 index of 'end' since stream init \*/

[ 30](structsys__winstream.md#a341203116bfee52d4b801466097fc3eb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structsys__winstream.md#a341203116bfee52d4b801466097fc3eb)[];

31};

32

[ 48](winstream_8h.md#acc72f0f65bd88e8f2b630a3832006f9c)static inline struct [sys\_winstream](structsys__winstream.md) \*[sys\_winstream\_init](winstream_8h.md#acc72f0f65bd88e8f2b630a3832006f9c)(void \*buf, int buflen)

49{

50 struct [sys\_winstream](structsys__winstream.md) \*ws = buf, tmp = { .len = buflen - sizeof(\*ws) };

51

52 \*ws = tmp;

53 return ws;

54}

55

[ 69](winstream_8h.md#ae8686be598c081858322378c8e4368cb)void [sys\_winstream\_write](winstream_8h.md#ae8686be598c081858322378c8e4368cb)(struct [sys\_winstream](structsys__winstream.md) \*ws,

70 const char \*[data](structsys__winstream.md#a341203116bfee52d4b801466097fc3eb), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structsys__winstream.md#a30b03df76a51ecbf0cbe33975d5aaa66));

71

[ 92](winstream_8h.md#a55dc3b77ec21e6d799aa951e327dc392)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_winstream\_read](winstream_8h.md#a55dc3b77ec21e6d799aa951e327dc392)(struct [sys\_winstream](structsys__winstream.md) \*ws,

93 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[seq](structsys__winstream.md#a7d946d6a54652a8ac035dd8cd0ba861a), char \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buflen);

94

95#endif /\* ZEPHYR\_INCLUDE\_SYS\_WINSTREAM\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sys\_winstream](structsys__winstream.md)

Lockless shared memory byte stream IPC.

**Definition** winstream.h:25

[sys\_winstream::start](structsys__winstream.md#a1cc84dfd9f812b3491135d13365c7a98)

uint32\_t start

**Definition** winstream.h:27

[sys\_winstream::len](structsys__winstream.md#a30b03df76a51ecbf0cbe33975d5aaa66)

uint32\_t len

**Definition** winstream.h:26

[sys\_winstream::data](structsys__winstream.md#a341203116bfee52d4b801466097fc3eb)

uint8\_t data[]

**Definition** winstream.h:30

[sys\_winstream::end](structsys__winstream.md#a6b80cf715e4a3ca7b7b74b9efd150a23)

uint32\_t end

**Definition** winstream.h:28

[sys\_winstream::seq](structsys__winstream.md#a7d946d6a54652a8ac035dd8cd0ba861a)

uint32\_t seq

**Definition** winstream.h:29

[sys\_winstream\_read](winstream_8h.md#a55dc3b77ec21e6d799aa951e327dc392)

uint32\_t sys\_winstream\_read(struct sys\_winstream \*ws, uint32\_t \*seq, char \*buf, uint32\_t buflen)

Read bytes from a sys\_winstream.

[sys\_winstream\_init](winstream_8h.md#acc72f0f65bd88e8f2b630a3832006f9c)

static struct sys\_winstream \* sys\_winstream\_init(void \*buf, int buflen)

Construct a sys\_winstream from a region of memory.

**Definition** winstream.h:48

[sys\_winstream\_write](winstream_8h.md#ae8686be598c081858322378c8e4368cb)

void sys\_winstream\_write(struct sys\_winstream \*ws, const char \*data, uint32\_t len)

Write bytes to a sys\_winstream.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [winstream.h](winstream_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
