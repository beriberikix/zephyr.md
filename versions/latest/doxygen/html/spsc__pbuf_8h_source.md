---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/spsc__pbuf_8h_source.html
original_path: doxygen/html/spsc__pbuf_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spsc\_pbuf.h

[Go to the documentation of this file.](spsc__pbuf_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_SPSC\_PBUF\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_SPSC\_PBUF\_H\_

9

10#include <[zephyr/cache.h](cache_8h.md)>

11#include <[zephyr/devicetree.h](devicetree_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

27

[ 29](group__SPSC__PBUF__FLAGS.md#ga97255180be37860a513d0a87b3dac573)#define SPSC\_PBUF\_CACHE BIT(0)

30

[ 32](group__SPSC__PBUF__FLAGS.md#gaaaccc1ca6c802c2740b4af07ba1650b9)#define SPSC\_PBUF\_UTILIZATION\_BITS 24

33

[ 35](group__SPSC__PBUF__FLAGS.md#ga5c1783e202a62161b6f5b0f11fb62f8a)#define SPSC\_PBUF\_UTILIZATION\_OFFSET 8

36

38

39#if CONFIG\_DCACHE\_LINE\_SIZE != 0

40#define Z\_SPSC\_PBUF\_LOCAL\_DCACHE\_LINE CONFIG\_DCACHE\_LINE\_SIZE

41#else

42#define Z\_SPSC\_PBUF\_LOCAL\_DCACHE\_LINE DT\_PROP\_OR(CPU, d\_cache\_line\_size, 0)

43#endif

44

45#ifndef CONFIG\_SPSC\_PBUF\_REMOTE\_DCACHE\_LINE

[ 46](group__spsc__buf.md#ga01f1a8120df7afe197f5ed9d1c667370)#define CONFIG\_SPSC\_PBUF\_REMOTE\_DCACHE\_LINE 0

47#endif

48

49#define Z\_SPSC\_PBUF\_DCACHE\_LINE \

50 MAX(CONFIG\_SPSC\_PBUF\_REMOTE\_DCACHE\_LINE, Z\_SPSC\_PBUF\_LOCAL\_DCACHE\_LINE)

51

[ 53](group__spsc__buf.md#gaec777dd30be52c1773dcf9e9ec1f6f9d)#define SPSC\_PBUF\_MAX\_LEN 0xFF00

54

[ 62](structspsc__pbuf__common.md)struct [spsc\_pbuf\_common](structspsc__pbuf__common.md) {

[ 63](structspsc__pbuf__common.md#a7e6a0859238d5abc92ce48cb8dafb89c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structspsc__pbuf__common.md#a7e6a0859238d5abc92ce48cb8dafb89c); /\* Length of data[] in bytes. \*/

[ 64](structspsc__pbuf__common.md#aeeaddf75caa7d899120d9ff4bf39432c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structspsc__pbuf__common.md#aeeaddf75caa7d899120d9ff4bf39432c); /\* Flags. See @ref SPSC\_PBUF\_FLAGS \*/

[ 65](structspsc__pbuf__common.md#af396b2cb886441c56ddd3c866bb6637a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rd\_idx](structspsc__pbuf__common.md#af396b2cb886441c56ddd3c866bb6637a); /\* Index of the first valid byte in data[] \*/

66};

67

68/\* Padding to fill cache line. \*/

69#define Z\_SPSC\_PBUF\_PADDING \

70 MAX(0, Z\_SPSC\_PBUF\_DCACHE\_LINE - (int)sizeof(struct spsc\_pbuf\_common))

71

[ 77](structspsc__pbuf__ext__cache.md)struct [spsc\_pbuf\_ext\_cache](structspsc__pbuf__ext__cache.md) {

[ 78](structspsc__pbuf__ext__cache.md#af8da453c98a365ad7de52991487d681f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [reserved](structspsc__pbuf__ext__cache.md#af8da453c98a365ad7de52991487d681f)[Z\_SPSC\_PBUF\_PADDING];

[ 79](structspsc__pbuf__ext__cache.md#a513b3ec0f7e3c670c8ddd9a787ed500a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wr\_idx](structspsc__pbuf__ext__cache.md#a513b3ec0f7e3c670c8ddd9a787ed500a); /\* Index of the first free byte in data[] \*/

[ 80](structspsc__pbuf__ext__cache.md#acd6006164d2724afcc2b609d149f3aa1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structspsc__pbuf__ext__cache.md#acd6006164d2724afcc2b609d149f3aa1)[]; /\* Buffer data. \*/

81};

82

[ 84](structspsc__pbuf__ext__nocache.md)struct [spsc\_pbuf\_ext\_nocache](structspsc__pbuf__ext__nocache.md) {

[ 85](structspsc__pbuf__ext__nocache.md#af287a5f0150ed97536427b73ea8a46b8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wr\_idx](structspsc__pbuf__ext__nocache.md#af287a5f0150ed97536427b73ea8a46b8); /\* Index of the first free byte in data[] \*/

[ 86](structspsc__pbuf__ext__nocache.md#a3e0722d5d153bc3fc9af25ac64a539c5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structspsc__pbuf__ext__nocache.md#a3e0722d5d153bc3fc9af25ac64a539c5)[]; /\* Buffer data. \*/

87};

88

[ 101](structspsc__pbuf.md)struct [spsc\_pbuf](structspsc__pbuf.md) {

[ 102](structspsc__pbuf.md#a0f2e4726ed93b9132b6429adf45a98cb) struct [spsc\_pbuf\_common](structspsc__pbuf__common.md) [common](structspsc__pbuf.md#a0f2e4726ed93b9132b6429adf45a98cb);

103 union {

[ 104](structspsc__pbuf.md#adc8af418a006b9761ff28ceb76a3f1af) struct [spsc\_pbuf\_ext\_cache](structspsc__pbuf__ext__cache.md) [cache](structspsc__pbuf.md#adc8af418a006b9761ff28ceb76a3f1af);

[ 105](structspsc__pbuf.md#a8e851fc5b99dbbba53522b1d3aa23c25) struct [spsc\_pbuf\_ext\_nocache](structspsc__pbuf__ext__nocache.md) [nocache](structspsc__pbuf.md#a8e851fc5b99dbbba53522b1d3aa23c25);

[ 106](structspsc__pbuf.md#a1319cdcb211031b9bb79f8b9cb0a3765) } [ext](structspsc__pbuf.md#a1319cdcb211031b9bb79f8b9cb0a3765);

107};

108

[ 119](group__spsc__buf.md#ga02955c21404d71ac3ceeb9aa82cb18af)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [spsc\_pbuf\_capacity](group__spsc__buf.md#ga02955c21404d71ac3ceeb9aa82cb18af)(struct [spsc\_pbuf](structspsc__pbuf.md) \*pb)

120{

121 return pb->[common](structspsc__pbuf.md#a0f2e4726ed93b9132b6429adf45a98cb).[len](structspsc__pbuf__common.md#a7e6a0859238d5abc92ce48cb8dafb89c) - sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f));

122}

123

[ 143](group__spsc__buf.md#ga6db38d6a0200a2468db02815cfe3bb6e)struct [spsc\_pbuf](structspsc__pbuf.md) \*[spsc\_pbuf\_init](group__spsc__buf.md#ga6db38d6a0200a2468db02815cfe3bb6e)(void \*buf, size\_t blen, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

144

[ 158](group__spsc__buf.md#ga492c895f1723567445ce23c73ed3d0ef)int [spsc\_pbuf\_write](group__spsc__buf.md#ga492c895f1723567445ce23c73ed3d0ef)(struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, const char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

159

[ 188](group__spsc__buf.md#ga44485fd6756810f56c6bf7d41b3b447c)int [spsc\_pbuf\_alloc](group__spsc__buf.md#ga44485fd6756810f56c6bf7d41b3b447c)(struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, char \*\*buf);

189

[ 199](group__spsc__buf.md#ga664da6f26fd99e7f1ce76828273408a0)void [spsc\_pbuf\_commit](group__spsc__buf.md#ga664da6f26fd99e7f1ce76828273408a0)(struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

200

[ 218](group__spsc__buf.md#ga24d4cc2a41fd2c42c6085e106bf71c0c)int [spsc\_pbuf\_read](group__spsc__buf.md#ga24d4cc2a41fd2c42c6085e106bf71c0c)(struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

219

[ 237](group__spsc__buf.md#ga6727d38e40a780f9116d5d7b1c0ae8c4)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [spsc\_pbuf\_claim](group__spsc__buf.md#ga6727d38e40a780f9116d5d7b1c0ae8c4)(struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, char \*\*buf);

238

[ 247](group__spsc__buf.md#ga28ea4f10fcab4d04f9e831f2057822ca)void [spsc\_pbuf\_free](group__spsc__buf.md#ga28ea4f10fcab4d04f9e831f2057822ca)(struct [spsc\_pbuf](structspsc__pbuf.md) \*pb, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

248

[ 260](group__spsc__buf.md#gae3f455db53147709d40a7a86406a9311)int [spsc\_pbuf\_get\_utilization](group__spsc__buf.md#gae3f455db53147709d40a7a86406a9311)(struct [spsc\_pbuf](structspsc__pbuf.md) \*pb);

264

265#ifdef \_\_cplusplus

266}

267#endif

268

269#endif /\* ZEPHYR\_INCLUDE\_SYS\_SPSC\_PBUF\_H\_ \*/

[cache.h](cache_8h.md)

cache API interface

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[spsc\_pbuf\_capacity](group__spsc__buf.md#ga02955c21404d71ac3ceeb9aa82cb18af)

static uint32\_t spsc\_pbuf\_capacity(struct spsc\_pbuf \*pb)

Get buffer capacity.

**Definition** spsc\_pbuf.h:119

[spsc\_pbuf\_read](group__spsc__buf.md#ga24d4cc2a41fd2c42c6085e106bf71c0c)

int spsc\_pbuf\_read(struct spsc\_pbuf \*pb, char \*buf, uint16\_t len)

Read specified amount of data from the packet buffer.

[spsc\_pbuf\_free](group__spsc__buf.md#ga28ea4f10fcab4d04f9e831f2057822ca)

void spsc\_pbuf\_free(struct spsc\_pbuf \*pb, uint16\_t len)

Free the packet to the buffer.

[spsc\_pbuf\_alloc](group__spsc__buf.md#ga44485fd6756810f56c6bf7d41b3b447c)

int spsc\_pbuf\_alloc(struct spsc\_pbuf \*pb, uint16\_t len, char \*\*buf)

Allocate space in the packet buffer.

[spsc\_pbuf\_write](group__spsc__buf.md#ga492c895f1723567445ce23c73ed3d0ef)

int spsc\_pbuf\_write(struct spsc\_pbuf \*pb, const char \*buf, uint16\_t len)

Write specified amount of data to the packet buffer.

[spsc\_pbuf\_commit](group__spsc__buf.md#ga664da6f26fd99e7f1ce76828273408a0)

void spsc\_pbuf\_commit(struct spsc\_pbuf \*pb, uint16\_t len)

Commit packet to the buffer.

[spsc\_pbuf\_claim](group__spsc__buf.md#ga6727d38e40a780f9116d5d7b1c0ae8c4)

uint16\_t spsc\_pbuf\_claim(struct spsc\_pbuf \*pb, char \*\*buf)

Claim packet from the buffer.

[spsc\_pbuf\_init](group__spsc__buf.md#ga6db38d6a0200a2468db02815cfe3bb6e)

struct spsc\_pbuf \* spsc\_pbuf\_init(void \*buf, size\_t blen, uint32\_t flags)

Initialize the packet buffer.

[spsc\_pbuf\_get\_utilization](group__spsc__buf.md#gae3f455db53147709d40a7a86406a9311)

int spsc\_pbuf\_get\_utilization(struct spsc\_pbuf \*pb)

Get maximum utilization of the packet buffer.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[spsc\_pbuf\_common](structspsc__pbuf__common.md)

First part of packet buffer control block.

**Definition** spsc\_pbuf.h:62

[spsc\_pbuf\_common::len](structspsc__pbuf__common.md#a7e6a0859238d5abc92ce48cb8dafb89c)

uint32\_t len

**Definition** spsc\_pbuf.h:63

[spsc\_pbuf\_common::flags](structspsc__pbuf__common.md#aeeaddf75caa7d899120d9ff4bf39432c)

uint32\_t flags

**Definition** spsc\_pbuf.h:64

[spsc\_pbuf\_common::rd\_idx](structspsc__pbuf__common.md#af396b2cb886441c56ddd3c866bb6637a)

uint32\_t rd\_idx

**Definition** spsc\_pbuf.h:65

[spsc\_pbuf\_ext\_cache](structspsc__pbuf__ext__cache.md)

Remaining part of a packet buffer when cache is used.

**Definition** spsc\_pbuf.h:77

[spsc\_pbuf\_ext\_cache::wr\_idx](structspsc__pbuf__ext__cache.md#a513b3ec0f7e3c670c8ddd9a787ed500a)

uint32\_t wr\_idx

**Definition** spsc\_pbuf.h:79

[spsc\_pbuf\_ext\_cache::data](structspsc__pbuf__ext__cache.md#acd6006164d2724afcc2b609d149f3aa1)

uint8\_t data[]

**Definition** spsc\_pbuf.h:80

[spsc\_pbuf\_ext\_cache::reserved](structspsc__pbuf__ext__cache.md#af8da453c98a365ad7de52991487d681f)

uint8\_t reserved[MAX(0, MAX(0, DT\_PROP\_OR(CPU, d\_cache\_line\_size, 0)) -(int) sizeof(struct spsc\_pbuf\_common))]

**Definition** spsc\_pbuf.h:78

[spsc\_pbuf\_ext\_nocache](structspsc__pbuf__ext__nocache.md)

Remaining part of a packet buffer when cache is not used.

**Definition** spsc\_pbuf.h:84

[spsc\_pbuf\_ext\_nocache::data](structspsc__pbuf__ext__nocache.md#a3e0722d5d153bc3fc9af25ac64a539c5)

uint8\_t data[]

**Definition** spsc\_pbuf.h:86

[spsc\_pbuf\_ext\_nocache::wr\_idx](structspsc__pbuf__ext__nocache.md#af287a5f0150ed97536427b73ea8a46b8)

uint32\_t wr\_idx

**Definition** spsc\_pbuf.h:85

[spsc\_pbuf](structspsc__pbuf.md)

Single producer, single consumer packet buffer.

**Definition** spsc\_pbuf.h:101

[spsc\_pbuf::common](structspsc__pbuf.md#a0f2e4726ed93b9132b6429adf45a98cb)

struct spsc\_pbuf\_common common

**Definition** spsc\_pbuf.h:102

[spsc\_pbuf::ext](structspsc__pbuf.md#a1319cdcb211031b9bb79f8b9cb0a3765)

union spsc\_pbuf::@231221263231315276224270165325337046003173211363 ext

[spsc\_pbuf::nocache](structspsc__pbuf.md#a8e851fc5b99dbbba53522b1d3aa23c25)

struct spsc\_pbuf\_ext\_nocache nocache

**Definition** spsc\_pbuf.h:105

[spsc\_pbuf::cache](structspsc__pbuf.md#adc8af418a006b9761ff28ceb76a3f1af)

struct spsc\_pbuf\_ext\_cache cache

**Definition** spsc\_pbuf.h:104

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [spsc\_pbuf.h](spsc__pbuf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
