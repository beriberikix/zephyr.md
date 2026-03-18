---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/isotp_8h_source.html
original_path: doxygen/html/isotp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

isotp.h

[Go to the documentation of this file.](isotp_8h.md)

1/\*

2 \* Copyright (c) 2019 Alexander Wachter

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_CANBUS\_ISOTP\_H\_

15#define ZEPHYR\_INCLUDE\_CANBUS\_ISOTP\_H\_

16

23

24#include <[zephyr/drivers/can.h](drivers_2can_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/net/buf.h](net_2buf_8h.md)>

27

28/\*

29 \* Abbreviations

30 \* BS Block Size

31 \* CAN\_DL CAN LL data size

32 \* CF Consecutive Frame

33 \* CTS Continue to send

34 \* DLC Data length code

35 \* FC Flow Control

36 \* FF First Frame

37 \* SF Single Frame

38 \* FS Flow Status

39 \* AE Address Extension

40 \* SN Sequence Number

41 \* ST Separation time

42 \* SA Source Address

43 \* TA Target Address

44 \* RX\_DL CAN RX LL data size

45 \* TX\_DL CAN TX LL data size

46 \* PCI Process Control Information

47 \*/

48

49/\*

50 \* N\_Result according to ISO 15765-2:2016

51 \* ISOTP\_ prefix is used to be zephyr conform

52 \*/

53

[ 55](group__can__isotp.md#gab7daaebbc303665beb2946ce077d5312)#define ISOTP\_N\_OK 0

56

[ 58](group__can__isotp.md#ga8298423e96932f94308f3064755d18fb)#define ISOTP\_N\_TIMEOUT\_A -1

59

[ 61](group__can__isotp.md#ga9e525bb24928a2656e7cd2842b306553)#define ISOTP\_N\_TIMEOUT\_BS -2

62

[ 64](group__can__isotp.md#ga77b802df46c66ed6002f143b57f73b7a)#define ISOTP\_N\_TIMEOUT\_CR -3

65

[ 67](group__can__isotp.md#ga9caa5677a171e1bd0be06ebb6b006046)#define ISOTP\_N\_WRONG\_SN -4

68

[ 70](group__can__isotp.md#ga99312831df8e1822f02b41e3fccc0661)#define ISOTP\_N\_INVALID\_FS -5

71

[ 73](group__can__isotp.md#ga45e3bfdd3948be6ccb3daec5db412b78)#define ISOTP\_N\_UNEXP\_PDU -6

74

[ 76](group__can__isotp.md#gad6bcb7b6fb8ab30da1a4ddeabe3e3178)#define ISOTP\_N\_WFT\_OVRN -7

77

[ 79](group__can__isotp.md#ga1b8e6b35a637b5f98e7a2ab4270efd41)#define ISOTP\_N\_BUFFER\_OVERFLW -8

80

[ 82](group__can__isotp.md#ga0805646e65d39a9e2f15e110720887ca)#define ISOTP\_N\_ERROR -9

83

85

[ 87](group__can__isotp.md#gaf0624cd5e7d12e94f4a739bc47ee0361)#define ISOTP\_NO\_FREE\_FILTER -10

88

[ 90](group__can__isotp.md#ga901f61175e228a70c2f882bc999caea6)#define ISOTP\_NO\_NET\_BUF\_LEFT -11

91

[ 93](group__can__isotp.md#gaed5270f0ee489128adb8c2ea481c6c77)#define ISOTP\_NO\_BUF\_DATA\_LEFT -12

94

[ 96](group__can__isotp.md#gac5cb1fafeb8aa5cf9fe1695612671c7d)#define ISOTP\_NO\_CTX\_LEFT -13

97

[ 99](group__can__isotp.md#gaa3e873d4a80ee128f1858520874f93b6)#define ISOTP\_RECV\_TIMEOUT -14

100

101/\*

102 \* CAN ID filtering for ISO-TP fixed addressing according to SAE J1939

103 \*

104 \* Format of 29-bit CAN identifier:

105 \* ------------------------------------------------------

106 \* | 28 .. 26 | 25 | 24 | 23 .. 16 | 15 .. 8 | 7 .. 0 |

107 \* ------------------------------------------------------

108 \* | Priority | EDP | DP | N\_TAtype | N\_TA | N\_SA |

109 \* ------------------------------------------------------

110 \*/

111

[ 113](group__can__isotp.md#gaedb0e7330d19b1cdc380c0b36cabf2f5)#define ISOTP\_FIXED\_ADDR\_SA\_POS (CONFIG\_ISOTP\_FIXED\_ADDR\_SA\_POS)

114

[ 116](group__can__isotp.md#ga2a9cbfd95bae05a9f7433f3b1c58689e)#define ISOTP\_FIXED\_ADDR\_SA\_MASK (CONFIG\_ISOTP\_FIXED\_ADDR\_SA\_MASK)

117

[ 119](group__can__isotp.md#ga2b64d4dffde99159ae5120586364e1c6)#define ISOTP\_FIXED\_ADDR\_TA\_POS (CONFIG\_ISOTP\_FIXED\_ADDR\_TA\_POS)

120

[ 122](group__can__isotp.md#ga5d5415982e04e506c9b045bfbe2be337)#define ISOTP\_FIXED\_ADDR\_TA\_MASK (CONFIG\_ISOTP\_FIXED\_ADDR\_TA\_MASK)

123

[ 125](group__can__isotp.md#ga29f8806889f4e41c1529c35a56ee98a9)#define ISOTP\_FIXED\_ADDR\_PRIO\_POS (CONFIG\_ISOTP\_FIXED\_ADDR\_PRIO\_POS)

126

[ 128](group__can__isotp.md#gab5dc33148923e7cd58b438a8906d1ace)#define ISOTP\_FIXED\_ADDR\_PRIO\_MASK (CONFIG\_ISOTP\_FIXED\_ADDR\_PRIO\_MASK)

129

[ 131](group__can__isotp.md#gac27b3210cb754b4621c54923696bfe2d)#define ISOTP\_FIXED\_ADDR\_RX\_MASK (CONFIG\_ISOTP\_FIXED\_ADDR\_RX\_MASK)

132

133#ifdef \_\_cplusplus

134extern "C" {

135#endif

136

143

[ 145](group__can__isotp.md#ga903d326b3bfb05151b9d5d0a0ace59b9)#define ISOTP\_MSG\_EXT\_ADDR BIT(0)

146

[ 151](group__can__isotp.md#ga998ae9b1645485f567e692bfbaa50cbe)#define ISOTP\_MSG\_FIXED\_ADDR BIT(1)

152

[ 154](group__can__isotp.md#ga16935466c1a543c03d11b71b8944d0b8)#define ISOTP\_MSG\_IDE BIT(2)

155

[ 157](group__can__isotp.md#ga70b485a2e576b1b0fec2cc8037215bd9)#define ISOTP\_MSG\_FDF BIT(3)

158

[ 160](group__can__isotp.md#ga9275708b5afba61c8b5c98c718ec4635)#define ISOTP\_MSG\_BRS BIT(4)

161

163

[ 169](structisotp__msg__id.md)struct [isotp\_msg\_id](structisotp__msg__id.md) {

176 union {

[ 177](structisotp__msg__id.md#ac9ded92f8e0afa88609003c5cf819704) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [std\_id](structisotp__msg__id.md#ac9ded92f8e0afa88609003c5cf819704) : 11;

[ 178](structisotp__msg__id.md#a3f9d4a6efd9b1c147f889a6396d7ef1c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ext\_id](structisotp__msg__id.md#a3f9d4a6efd9b1c147f889a6396d7ef1c) : 29;

179 };

[ 181](structisotp__msg__id.md#a7b818e7c6dab02347b32bcc74dfc44a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ext\_addr](structisotp__msg__id.md#a7b818e7c6dab02347b32bcc74dfc44a3);

[ 192](structisotp__msg__id.md#adc7ff4eac4573221b89a5bb5a5e53d49) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dl](structisotp__msg__id.md#adc7ff4eac4573221b89a5bb5a5e53d49);

[ 194](structisotp__msg__id.md#a3185e5b5fddb5d7fc94b86c8d30e61a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structisotp__msg__id.md#a3185e5b5fddb5d7fc94b86c8d30e61a9);

195};

196

197/\*

198 \* STmin is split in two valid ranges:

199 \* 0-127: 0ms-127ms

200 \* 128-240: Reserved

201 \* 241-249: 100us-900us (multiples of 100us)

202 \* 250- : Reserved

203 \*/

204

[ 210](structisotp__fc__opts.md)struct [isotp\_fc\_opts](structisotp__fc__opts.md) {

[ 211](structisotp__fc__opts.md#a8f31bf5c95069352043da33541911b3c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bs](structisotp__fc__opts.md#a8f31bf5c95069352043da33541911b3c);

[ 212](structisotp__fc__opts.md#a5db0ceeed259c26d1d8fe0a901edcbca) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [stmin](structisotp__fc__opts.md#a5db0ceeed259c26d1d8fe0a901edcbca);

213};

214

[ 223](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb)typedef void (\*[isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb))(int error\_nr, void \*arg);

224

225struct isotp\_send\_ctx;

226struct isotp\_recv\_ctx;

227

[ 247](group__can__isotp.md#ga725696a26c3bdc0c99e3c4e611a897f9)int [isotp\_bind](group__can__isotp.md#ga725696a26c3bdc0c99e3c4e611a897f9)(struct isotp\_recv\_ctx \*rctx, const struct [device](structdevice.md) \*can\_dev,

248 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr,

249 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr,

250 const struct [isotp\_fc\_opts](structisotp__fc__opts.md) \*opts,

251 [k\_timeout\_t](structk__timeout__t.md) timeout);

252

[ 263](group__can__isotp.md#ga622293da5564203bf6dcb993410d21ba)void [isotp\_unbind](group__can__isotp.md#ga622293da5564203bf6dcb993410d21ba)(struct isotp\_recv\_ctx \*rctx);

264

[ 282](group__can__isotp.md#ga79c9cad7f39802c5c80af743717e22c6)int [isotp\_recv](group__can__isotp.md#ga79c9cad7f39802c5c80af743717e22c6)(struct isotp\_recv\_ctx \*rctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len, [k\_timeout\_t](structk__timeout__t.md) timeout);

283

[ 302](group__can__isotp.md#ga4fb0ef794b7c4104d6e6b17bc68e09d8)int [isotp\_recv\_net](group__can__isotp.md#ga4fb0ef794b7c4104d6e6b17bc68e09d8)(struct isotp\_recv\_ctx \*rctx, struct [net\_buf](structnet__buf.md) \*\*buffer, [k\_timeout\_t](structk__timeout__t.md) timeout);

303

[ 325](group__can__isotp.md#ga3723fae583a1d7deabc2deee475ba756)int [isotp\_send](group__can__isotp.md#ga3723fae583a1d7deabc2deee475ba756)(struct isotp\_send\_ctx \*sctx, const struct [device](structdevice.md) \*can\_dev,

326 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

327 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr,

328 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr,

329 [isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb) complete\_cb, void \*cb\_arg);

330

331#ifdef CONFIG\_ISOTP\_ENABLE\_CONTEXT\_BUFFERS

350int isotp\_send\_ctx\_buf(const struct [device](structdevice.md) \*can\_dev,

351 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

352 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr,

353 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr,

354 [isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb) complete\_cb, void \*cb\_arg,

355 [k\_timeout\_t](structk__timeout__t.md) timeout);

356

375int isotp\_send\_net\_ctx\_buf(const struct [device](structdevice.md) \*can\_dev,

376 struct [net\_buf](structnet__buf.md) \*data,

377 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr,

378 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr,

379 [isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb) complete\_cb, void \*cb\_arg,

380 [k\_timeout\_t](structk__timeout__t.md) timeout);

381

382#endif /\*CONFIG\_ISOTP\_ENABLE\_CONTEXT\_BUFFERS\*/

383

384#if defined(CONFIG\_ISOTP\_USE\_TX\_BUF) && \

385 defined(CONFIG\_ISOTP\_ENABLE\_CONTEXT\_BUFFERS)

405int isotp\_send\_buf(const struct [device](structdevice.md) \*can\_dev,

406 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

407 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*tx\_addr,

408 const struct [isotp\_msg\_id](structisotp__msg__id.md) \*rx\_addr,

409 [isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb) complete\_cb, void \*cb\_arg,

410 [k\_timeout\_t](structk__timeout__t.md) timeout);

411#endif

412

414

415struct isotp\_callback {

416 [isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb) cb;

417 void \*arg;

418};

419

420struct isotp\_send\_ctx {

421 int filter\_id;

422 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) error\_nr;

423 const struct device \*can\_dev;

424 union {

425 struct net\_buf \*buf;

426 struct {

427 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data;

428 size\_t len;

429 };

430 };

431 struct k\_work work;

432 struct k\_timer timer;

433 union {

434 struct isotp\_callback fin\_cb;

435 struct k\_sem fin\_sem;

436 };

437 struct isotp\_fc\_opts opts;

438 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

439 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_backlog;

440 struct k\_sem tx\_sem;

441 struct isotp\_msg\_id rx\_addr;

442 struct isotp\_msg\_id tx\_addr;

443 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wft;

444 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bs;

445 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sn : 4;

446 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) is\_net\_buf : 1;

447 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) is\_ctx\_slab : 1;

448 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) has\_callback: 1;

449};

450

451struct isotp\_recv\_ctx {

452 int filter\_id;

453 const struct device \*can\_dev;

454 struct net\_buf \*buf;

455 struct net\_buf \*act\_frag;

456 /\* buffer currently processed in isotp\_recv \*/

457 struct net\_buf \*recv\_buf;

458 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) alloc\_node;

459 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) length;

460 int error\_nr;

461 struct k\_work work;

462 struct k\_timer timer;

463 struct k\_fifo fifo;

464 struct isotp\_msg\_id rx\_addr;

465 struct isotp\_msg\_id tx\_addr;

466 struct isotp\_fc\_opts opts;

467 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

468 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bs;

469 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wft;

470 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sn\_expected : 4;

471};

472

474

478

479#ifdef \_\_cplusplus

480}

481#endif

482

483#endif /\* ZEPHYR\_INCLUDE\_CANBUS\_ISOTP\_H\_ \*/

[can.h](drivers_2can_8h.md)

Controller Area Network (CAN) driver API.

[isotp\_send](group__can__isotp.md#ga3723fae583a1d7deabc2deee475ba756)

int isotp\_send(struct isotp\_send\_ctx \*sctx, const struct device \*can\_dev, const uint8\_t \*data, size\_t len, const struct isotp\_msg\_id \*tx\_addr, const struct isotp\_msg\_id \*rx\_addr, isotp\_tx\_callback\_t complete\_cb, void \*cb\_arg)

Send data.

[isotp\_recv\_net](group__can__isotp.md#ga4fb0ef794b7c4104d6e6b17bc68e09d8)

int isotp\_recv\_net(struct isotp\_recv\_ctx \*rctx, struct net\_buf \*\*buffer, k\_timeout\_t timeout)

Get the net buffer on data reception.

[isotp\_unbind](group__can__isotp.md#ga622293da5564203bf6dcb993410d21ba)

void isotp\_unbind(struct isotp\_recv\_ctx \*rctx)

Unbind a context from the interface.

[isotp\_bind](group__can__isotp.md#ga725696a26c3bdc0c99e3c4e611a897f9)

int isotp\_bind(struct isotp\_recv\_ctx \*rctx, const struct device \*can\_dev, const struct isotp\_msg\_id \*rx\_addr, const struct isotp\_msg\_id \*tx\_addr, const struct isotp\_fc\_opts \*opts, k\_timeout\_t timeout)

Bind an address to a receiving context.

[isotp\_recv](group__can__isotp.md#ga79c9cad7f39802c5c80af743717e22c6)

int isotp\_recv(struct isotp\_recv\_ctx \*rctx, uint8\_t \*data, size\_t len, k\_timeout\_t timeout)

Read out received data from fifo.

[isotp\_tx\_callback\_t](group__can__isotp.md#gad4f9c0d3f847d453ea662128db2603bb)

void(\* isotp\_tx\_callback\_t)(int error\_nr, void \*arg)

Transmission callback.

**Definition** isotp.h:223

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[buf.h](net_2buf_8h.md)

Buffer management.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[isotp\_fc\_opts](structisotp__fc__opts.md)

ISO-TP frame control options struct.

**Definition** isotp.h:210

[isotp\_fc\_opts::stmin](structisotp__fc__opts.md#a5db0ceeed259c26d1d8fe0a901edcbca)

uint8\_t stmin

Minimum separation time.

**Definition** isotp.h:212

[isotp\_fc\_opts::bs](structisotp__fc__opts.md#a8f31bf5c95069352043da33541911b3c)

uint8\_t bs

Block size.

**Definition** isotp.h:211

[isotp\_msg\_id](structisotp__msg__id.md)

ISO-TP message id struct.

**Definition** isotp.h:169

[isotp\_msg\_id::flags](structisotp__msg__id.md#a3185e5b5fddb5d7fc94b86c8d30e61a9)

uint8\_t flags

Flags.

**Definition** isotp.h:194

[isotp\_msg\_id::ext\_id](structisotp__msg__id.md#a3f9d4a6efd9b1c147f889a6396d7ef1c)

uint32\_t ext\_id

**Definition** isotp.h:178

[isotp\_msg\_id::ext\_addr](structisotp__msg__id.md#a7b818e7c6dab02347b32bcc74dfc44a3)

uint8\_t ext\_addr

ISO-TP extended address (if used).

**Definition** isotp.h:181

[isotp\_msg\_id::std\_id](structisotp__msg__id.md#ac9ded92f8e0afa88609003c5cf819704)

uint32\_t std\_id

**Definition** isotp.h:177

[isotp\_msg\_id::dl](structisotp__msg__id.md#adc7ff4eac4573221b89a5bb5a5e53d49)

uint8\_t dl

ISO-TP frame data length (TX\_DL for TX address or RX\_DL for RX address).

**Definition** isotp.h:192

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:1004

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [canbus](dir_7890c2fc429c7c0e4d7e0cd7b89129f9.md)
- [isotp.h](isotp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
