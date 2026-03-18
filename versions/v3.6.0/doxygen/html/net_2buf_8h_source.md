---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net_2buf_8h_source.html
original_path: doxygen/html/net_2buf_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

buf.h

[Go to the documentation of this file.](net_2buf_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_NET\_BUF\_H\_

11#define ZEPHYR\_INCLUDE\_NET\_BUF\_H\_

12

13#include <stddef.h>

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15#include <[zephyr/sys/util.h](util_8h.md)>

16#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

17#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

30/\* Alignment needed for various parts of the buffer definition \*/

31#if CONFIG\_NET\_BUF\_ALIGNMENT == 0

32#define \_\_net\_buf\_align \_\_aligned(sizeof(void \*))

33#else

34#define \_\_net\_buf\_align \_\_aligned(CONFIG\_NET\_BUF\_ALIGNMENT)

35#endif

36

[ 46](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501)#define NET\_BUF\_SIMPLE\_DEFINE(\_name, \_size) \

47 uint8\_t net\_buf\_data\_##\_name[\_size]; \

48 struct net\_buf\_simple \_name = { \

49 .data = net\_buf\_data\_##\_name, \

50 .len = 0, \

51 .size = \_size, \

52 .\_\_buf = net\_buf\_data\_##\_name, \

53 }

54

[ 65](group__net__buf.md#ga21ced8b3082d57bf071008de5fffc0f4)#define NET\_BUF\_SIMPLE\_DEFINE\_STATIC(\_name, \_size) \

66 static \_\_noinit uint8\_t net\_buf\_data\_##\_name[\_size]; \

67 static struct net\_buf\_simple \_name = { \

68 .data = net\_buf\_data\_##\_name, \

69 .len = 0, \

70 .size = \_size, \

71 .\_\_buf = net\_buf\_data\_##\_name, \

72 }

73

[ 87](structnet__buf__simple.md)struct [net\_buf\_simple](structnet__buf__simple.md) {

[ 89](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1);

90

[ 96](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3);

97

[ 99](structnet__buf__simple.md#ae6dc4aa029a67d3911293618eb30caa6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structnet__buf__simple.md#ae6dc4aa029a67d3911293618eb30caa6);

100

104 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\_\_buf;

105};

106

[ 123](group__net__buf.md#ga0b01dc80027d13b1895379d4d1397207)#define NET\_BUF\_SIMPLE(\_size) \

124 ((struct net\_buf\_simple \*)(&(struct { \

125 struct net\_buf\_simple buf; \

126 uint8\_t data[\_size]; \

127 }) { \

128 .buf.size = \_size, \

129 }))

130

[ 140](group__net__buf.md#ga040279b601191367dee013bab9916d8d)static inline void [net\_buf\_simple\_init](group__net__buf.md#ga040279b601191367dee013bab9916d8d)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

141 size\_t reserve\_head)

142{

143 if (!buf->\_\_buf) {

144 buf->\_\_buf = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf + sizeof(\*buf);

145 }

146

147 buf->[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) = buf->\_\_buf + reserve\_head;

148 buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) = 0U;

149}

150

[ 160](group__net__buf.md#ga7fac47a2a25eaca39c5d14f1f55b485d)void [net\_buf\_simple\_init\_with\_data](group__net__buf.md#ga7fac47a2a25eaca39c5d14f1f55b485d)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

161 void \*data, size\_t size);

162

[ 170](group__net__buf.md#ga4b537e913e132448cbf56976504ddddd)static inline void [net\_buf\_simple\_reset](group__net__buf.md#ga4b537e913e132448cbf56976504ddddd)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf)

171{

172 buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) = 0U;

173 buf->[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) = buf->\_\_buf;

174}

175

[ 186](group__net__buf.md#ga0186c153b72a379affdd3e2e3994b5a7)void [net\_buf\_simple\_clone](group__net__buf.md#ga0186c153b72a379affdd3e2e3994b5a7)(const struct [net\_buf\_simple](structnet__buf__simple.md) \*original,

187 struct [net\_buf\_simple](structnet__buf__simple.md) \*clone);

188

[ 200](group__net__buf.md#ga1906e637c848948f5780428a99b3341e)void \*[net\_buf\_simple\_add](group__net__buf.md#ga1906e637c848948f5780428a99b3341e)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

201

[ 214](group__net__buf.md#gac37209c1e5097e5610860943fb7d0115)void \*[net\_buf\_simple\_add\_mem](group__net__buf.md#gac37209c1e5097e5610860943fb7d0115)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, const void \*mem,

215 size\_t len);

216

[ 228](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[net\_buf\_simple\_add\_u8](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val);

229

[ 240](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5)void [net\_buf\_simple\_add\_le16](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

241

[ 252](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa)void [net\_buf\_simple\_add\_be16](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

253

[ 264](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6)void [net\_buf\_simple\_add\_le24](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

265

[ 276](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8)void [net\_buf\_simple\_add\_be24](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

277

[ 288](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56)void [net\_buf\_simple\_add\_le32](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

289

[ 300](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c)void [net\_buf\_simple\_add\_be32](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

301

[ 312](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25)void [net\_buf\_simple\_add\_le48](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

313

[ 324](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171)void [net\_buf\_simple\_add\_be48](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

325

[ 336](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011)void [net\_buf\_simple\_add\_le64](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

337

[ 348](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0)void [net\_buf\_simple\_add\_be64](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

349

[ 360](group__net__buf.md#ga8473bdffadc05b22335a321df89f4b83)void \*[net\_buf\_simple\_remove\_mem](group__net__buf.md#ga8473bdffadc05b22335a321df89f4b83)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

361

[ 372](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_buf\_simple\_remove\_u8](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

373

[ 384](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_remove\_le16](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

385

[ 396](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_remove\_be16](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

397

[ 408](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_remove\_le24](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

409

[ 420](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_remove\_be24](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

421

[ 432](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_remove\_le32](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

433

[ 444](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_remove\_be32](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

445

[ 456](group__net__buf.md#gac0628bbbe5d9c2b82766d5a17e767696)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_le48](group__net__buf.md#gac0628bbbe5d9c2b82766d5a17e767696)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

457

[ 468](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_be48](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

469

[ 480](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_le64](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

481

[ 492](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_be64](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

493

[ 505](group__net__buf.md#ga64df9754665440370340c6dddde625d1)void \*[net\_buf\_simple\_push](group__net__buf.md#ga64df9754665440370340c6dddde625d1)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

506

[ 519](group__net__buf.md#gaaa838083c610f7426c509efaae69a511)void \*[net\_buf\_simple\_push\_mem](group__net__buf.md#gaaa838083c610f7426c509efaae69a511)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, const void \*mem,

520 size\_t len);

521

[ 531](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6)void [net\_buf\_simple\_push\_le16](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

532

[ 542](group__net__buf.md#ga827bd85eba0dbd098790d84d22e8e32d)void [net\_buf\_simple\_push\_be16](group__net__buf.md#ga827bd85eba0dbd098790d84d22e8e32d)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

543

[ 552](group__net__buf.md#ga0f19da70bfc8f597680ee02c21226a77)void [net\_buf\_simple\_push\_u8](group__net__buf.md#ga0f19da70bfc8f597680ee02c21226a77)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val);

553

[ 563](group__net__buf.md#gabe52d6735d835edc361666bb3413b907)void [net\_buf\_simple\_push\_le24](group__net__buf.md#gabe52d6735d835edc361666bb3413b907)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

564

[ 574](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72)void [net\_buf\_simple\_push\_be24](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

575

[ 585](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1)void [net\_buf\_simple\_push\_le32](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

586

[ 596](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426)void [net\_buf\_simple\_push\_be32](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

597

[ 607](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e)void [net\_buf\_simple\_push\_le48](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

608

[ 618](group__net__buf.md#ga1ea39c7d7e9ba4e10d31d818e45e192a)void [net\_buf\_simple\_push\_be48](group__net__buf.md#ga1ea39c7d7e9ba4e10d31d818e45e192a)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

619

[ 629](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85)void [net\_buf\_simple\_push\_le64](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

630

[ 640](group__net__buf.md#gafea2201655955ab004b5f77106998ae9)void [net\_buf\_simple\_push\_be64](group__net__buf.md#gafea2201655955ab004b5f77106998ae9)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

641

[ 653](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8)void \*[net\_buf\_simple\_pull](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

654

[ 666](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c)void \*[net\_buf\_simple\_pull\_mem](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

667

[ 678](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_buf\_simple\_pull\_u8](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

679

[ 690](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_pull\_le16](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

691

[ 702](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_pull\_be16](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

703

[ 714](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_pull\_le24](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

715

[ 726](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_pull\_be24](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

727

[ 738](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_pull\_le32](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

739

[ 750](group__net__buf.md#ga1a53892ed75f994bbbb3a2bcf1743d3c)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_pull\_be32](group__net__buf.md#ga1a53892ed75f994bbbb3a2bcf1743d3c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

751

[ 762](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_le48](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

763

[ 774](group__net__buf.md#ga19bdefe740fe94a42fba76d71b4ef6e2)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_be48](group__net__buf.md#ga19bdefe740fe94a42fba76d71b4ef6e2)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

775

[ 786](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_le64](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

787

[ 798](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_be64](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

799

[ 809](group__net__buf.md#ga8d623415477ed880ceb1fb8861832309)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[net\_buf\_simple\_tail](group__net__buf.md#ga8d623415477ed880ceb1fb8861832309)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf)

810{

811 return buf->[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) + buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3);

812}

813

[ 823](group__net__buf.md#gacfdef39367c6de8a1b4479c3647cca76)size\_t [net\_buf\_simple\_headroom](group__net__buf.md#gacfdef39367c6de8a1b4479c3647cca76)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

824

[ 834](group__net__buf.md#ga59b2e4d1c5c5743ba20eba3bf35ac39e)size\_t [net\_buf\_simple\_tailroom](group__net__buf.md#ga59b2e4d1c5c5743ba20eba3bf35ac39e)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

835

[ 845](group__net__buf.md#ga7deeb4a89b90a3784e582abcb81d5126)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_max\_len](group__net__buf.md#ga7deeb4a89b90a3784e582abcb81d5126)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

846

[ 854](structnet__buf__simple__state.md)struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) {

[ 856](structnet__buf__simple__state.md#a4061f8e50e14289b1ec999ef490c8fbf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset](structnet__buf__simple__state.md#a4061f8e50e14289b1ec999ef490c8fbf);

[ 858](structnet__buf__simple__state.md#af0e544fe2b018a7ff0b30970e9de8253) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structnet__buf__simple__state.md#af0e544fe2b018a7ff0b30970e9de8253);

859};

860

[ 869](group__net__buf.md#ga5b891f335480830a71a5ee2d71f1a3db)static inline void [net\_buf\_simple\_save](group__net__buf.md#ga5b891f335480830a71a5ee2d71f1a3db)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

870 struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

871{

872 [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->offset = [net\_buf\_simple\_headroom](group__net__buf.md#gacfdef39367c6de8a1b4479c3647cca76)(buf);

873 [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->len = buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3);

874}

875

[ 885](group__net__buf.md#gaedd36481657a7a9d108659d56e131721)static inline void [net\_buf\_simple\_restore](group__net__buf.md#gaedd36481657a7a9d108659d56e131721)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

886 struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

887{

888 buf->[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) = buf->\_\_buf + [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->offset;

889 buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) = [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->len;

890}

891

[ 901](group__net__buf.md#gaaeacbdf3cfda12691c75253015e5c19a)#define NET\_BUF\_EXTERNAL\_DATA BIT(0)

902

[ 910](structnet__buf.md)struct [net\_buf](structnet__buf.md) {

[ 912](structnet__buf.md#a5cc70f57e5b776cfa12b2d556e5958f3) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__buf.md#a5cc70f57e5b776cfa12b2d556e5958f3);

913

[ 915](structnet__buf.md#a1fa032cc23854c35eae013020823fa88) struct [net\_buf](structnet__buf.md) \*[frags](structnet__buf.md#a1fa032cc23854c35eae013020823fa88);

916

[ 918](structnet__buf.md#a42da518a82f4c37c45814b4f8c5f2731) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ref](structnet__buf.md#a42da518a82f4c37c45814b4f8c5f2731);

919

[ 921](structnet__buf.md#aa4fcce2e2894fc5dbd9cc74fc020647e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structnet__buf.md#aa4fcce2e2894fc5dbd9cc74fc020647e);

922

[ 924](structnet__buf.md#a45f294bac054d64034bddcc4c6574d29) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pool\_id](structnet__buf.md#a45f294bac054d64034bddcc4c6574d29);

925

926 /\* Size of user data on this buffer \*/

[ 927](structnet__buf.md#a65db7bed62d7211114767e6ce58dad75) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [user\_data\_size](structnet__buf.md#a65db7bed62d7211114767e6ce58dad75);

928

929 /\* Union for convenience access to the net\_buf\_simple members, also

930 \* preserving the old API.

931 \*/

932 union {

933 /\* The ABI of this struct must match net\_buf\_simple \*/

934 struct {

[ 936](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

937

[ 939](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38);

940

[ 942](structnet__buf.md#a1522d81a002804223e25300a6961f527) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structnet__buf.md#a1522d81a002804223e25300a6961f527);

943

948 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\_\_buf;

949 };

950

[ 951](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750) struct [net\_buf\_simple](structnet__buf__simple.md) [b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750);

952 };

953

[ 955](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7)[] \_\_net\_buf\_align;

956};

957

[ 958](structnet__buf__data__cb.md)struct [net\_buf\_data\_cb](structnet__buf__data__cb.md) {

[ 959](structnet__buf__data__cb.md#a34bf941a262975eef4ff1c6e14a0c78f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* \_\_must\_check (\*[alloc](structnet__buf__data__cb.md#a34bf941a262975eef4ff1c6e14a0c78f))(struct [net\_buf](structnet__buf.md) \*buf, size\_t \*size,

960 [k\_timeout\_t](structk__timeout__t.md) timeout);

[ 961](structnet__buf__data__cb.md#a099e08c1dc2a48c821e381a8ce20cd51) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* \_\_must\_check (\*[ref](structnet__buf__data__cb.md#a099e08c1dc2a48c821e381a8ce20cd51))(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

[ 962](structnet__buf__data__cb.md#a80c307edcf878bde8d43813854185575) void (\*[unref](structnet__buf__data__cb.md#a80c307edcf878bde8d43813854185575))(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

963};

964

[ 965](structnet__buf__data__alloc.md)struct [net\_buf\_data\_alloc](structnet__buf__data__alloc.md) {

[ 966](structnet__buf__data__alloc.md#a5e69e95df9a975707d45f7682e5d7f56) const struct [net\_buf\_data\_cb](structnet__buf__data__cb.md) \*[cb](structnet__buf__data__alloc.md#a5e69e95df9a975707d45f7682e5d7f56);

[ 967](structnet__buf__data__alloc.md#adcc085065789af4a8e641c2ad7e670af) void \*[alloc\_data](structnet__buf__data__alloc.md#adcc085065789af4a8e641c2ad7e670af);

[ 968](structnet__buf__data__alloc.md#a7eadcd00a72ab69bd5c84f2adba10197) size\_t [max\_alloc\_size](structnet__buf__data__alloc.md#a7eadcd00a72ab69bd5c84f2adba10197);

969};

970

[ 976](structnet__buf__pool.md)struct [net\_buf\_pool](structnet__buf__pool.md) {

[ 978](structnet__buf__pool.md#a97e5b2e51238e859f93882a8008ba305) struct [k\_lifo](structk__lifo.md) [free](structnet__buf__pool.md#a97e5b2e51238e859f93882a8008ba305);

979

980 /\* to prevent concurrent access/modifications \*/

[ 981](structnet__buf__pool.md#ae92fc3f3f51be63ccdeee9614d21cc34) struct [k\_spinlock](structk__spinlock.md) [lock](structnet__buf__pool.md#ae92fc3f3f51be63ccdeee9614d21cc34);

982

[ 984](structnet__buf__pool.md#a55b57f4f573c7e752c3ccf2f92f25626) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buf\_count](structnet__buf__pool.md#a55b57f4f573c7e752c3ccf2f92f25626);

985

[ 987](structnet__buf__pool.md#a3fdf83b4c0b5acefbb761da285791ad2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [uninit\_count](structnet__buf__pool.md#a3fdf83b4c0b5acefbb761da285791ad2);

988

989 /\* Size of user data allocated to this pool \*/

[ 990](structnet__buf__pool.md#a4718ecec19d7e2ccaf04b6ff61120975) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [user\_data\_size](structnet__buf__pool.md#a4718ecec19d7e2ccaf04b6ff61120975);

991

992#if defined(CONFIG\_NET\_BUF\_POOL\_USAGE)

994 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) avail\_count;

995

997 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pool\_size;

998

1000 const char \*name;

1001#endif /\* CONFIG\_NET\_BUF\_POOL\_USAGE \*/

1002

[ 1004](structnet__buf__pool.md#a2a9141d7cd20cd98818a92dc5bc99f56) void (\*const [destroy](structnet__buf__pool.md#a2a9141d7cd20cd98818a92dc5bc99f56))(struct [net\_buf](structnet__buf.md) \*buf);

1005

[ 1007](structnet__buf__pool.md#a617bd8f77e55481d97183da8c0c62cc5) const struct [net\_buf\_data\_alloc](structnet__buf__data__alloc.md) \*[alloc](structnet__buf__pool.md#a617bd8f77e55481d97183da8c0c62cc5);

1008

1010 struct [net\_buf](structnet__buf.md) \* const \_\_bufs;

1011};

1012

1014#define NET\_BUF\_POOL\_USAGE\_INIT(\_pool, \_count) \

1015 IF\_ENABLED(CONFIG\_NET\_BUF\_POOL\_USAGE, (.avail\_count = ATOMIC\_INIT(\_count),)) \

1016 IF\_ENABLED(CONFIG\_NET\_BUF\_POOL\_USAGE, (.name = STRINGIFY(\_pool),))

1017

1018#define NET\_BUF\_POOL\_INITIALIZER(\_pool, \_alloc, \_bufs, \_count, \_ud\_size, \_destroy) \

1019 { \

1020 .free = Z\_LIFO\_INITIALIZER(\_pool.free), \

1021 .lock = { }, \

1022 .buf\_count = \_count, \

1023 .uninit\_count = \_count, \

1024 .user\_data\_size = \_ud\_size, \

1025 NET\_BUF\_POOL\_USAGE\_INIT(\_pool, \_count) \

1026 .destroy = \_destroy, \

1027 .alloc = \_alloc, \

1028 .\_\_bufs = (struct net\_buf \*)\_bufs, \

1029 }

1030

1031#define \_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size) \

1032 struct \_net\_buf\_##\_name { uint8\_t b[sizeof(struct net\_buf)]; \

1033 uint8\_t ud[\_ud\_size]; } \_\_net\_buf\_align; \

1034 BUILD\_ASSERT(\_ud\_size <= UINT8\_MAX); \

1035 BUILD\_ASSERT(offsetof(struct net\_buf, user\_data) == \

1036 offsetof(struct \_net\_buf\_##\_name, ud), "Invalid offset"); \

1037 BUILD\_ASSERT(\_\_alignof\_\_(struct net\_buf) == \

1038 \_\_alignof\_\_(struct \_net\_buf\_##\_name), "Invalid alignment"); \

1039 BUILD\_ASSERT(sizeof(struct \_net\_buf\_##\_name) == \

1040 ROUND\_UP(sizeof(struct net\_buf) + \_ud\_size, \_\_alignof\_\_(struct net\_buf)), \

1041 "Size cannot be determined"); \

1042 static struct \_net\_buf\_##\_name \_net\_buf\_##\_name[\_count] \_\_noinit

1043

1044extern const struct [net\_buf\_data\_alloc](structnet__buf__data__alloc.md) net\_buf\_heap\_alloc;

1046

[ 1074](group__net__buf.md#ga61671ac866081d31dfe9eddbf3b6f210)#define NET\_BUF\_POOL\_HEAP\_DEFINE(\_name, \_count, \_ud\_size, \_destroy) \

1075 \_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

1076 static STRUCT\_SECTION\_ITERABLE(net\_buf\_pool, \_name) = \

1077 NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_heap\_alloc, \

1078 \_net\_buf\_##\_name, \_count, \_ud\_size, \

1079 \_destroy)

1080

[ 1081](structnet__buf__pool__fixed.md)struct [net\_buf\_pool\_fixed](structnet__buf__pool__fixed.md) {

[ 1082](structnet__buf__pool__fixed.md#a6e17291c5aa8dfe8a478d9b5e4e74596) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_pool](structnet__buf__pool__fixed.md#a6e17291c5aa8dfe8a478d9b5e4e74596);

1083};

1084

1086extern const struct [net\_buf\_data\_cb](structnet__buf__data__cb.md) net\_buf\_fixed\_cb;

1088

[ 1117](group__net__buf.md#gacc53824e01db7935bcc9cad564b716cd)#define NET\_BUF\_POOL\_FIXED\_DEFINE(\_name, \_count, \_data\_size, \_ud\_size, \_destroy) \

1118 \_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

1119 static uint8\_t \_\_noinit net\_buf\_data\_##\_name[\_count][\_data\_size] \_\_net\_buf\_align; \

1120 static const struct net\_buf\_pool\_fixed net\_buf\_fixed\_##\_name = { \

1121 .data\_pool = (uint8\_t \*)net\_buf\_data\_##\_name, \

1122 }; \

1123 static const struct net\_buf\_data\_alloc net\_buf\_fixed\_alloc\_##\_name = { \

1124 .cb = &net\_buf\_fixed\_cb, \

1125 .alloc\_data = (void \*)&net\_buf\_fixed\_##\_name, \

1126 .max\_alloc\_size = \_data\_size, \

1127 }; \

1128 static STRUCT\_SECTION\_ITERABLE(net\_buf\_pool, \_name) = \

1129 NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_fixed\_alloc\_##\_name, \

1130 \_net\_buf\_##\_name, \_count, \_ud\_size, \

1131 \_destroy)

1132

1134extern const struct [net\_buf\_data\_cb](structnet__buf__data__cb.md) net\_buf\_var\_cb;

1136

[ 1161](group__net__buf.md#ga90e691e793c964847d737f5ecf7646ec)#define NET\_BUF\_POOL\_VAR\_DEFINE(\_name, \_count, \_data\_size, \_ud\_size, \_destroy) \

1162 \_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

1163 K\_HEAP\_DEFINE(net\_buf\_mem\_pool\_##\_name, \_data\_size); \

1164 static const struct net\_buf\_data\_alloc net\_buf\_data\_alloc\_##\_name = { \

1165 .cb = &net\_buf\_var\_cb, \

1166 .alloc\_data = &net\_buf\_mem\_pool\_##\_name, \

1167 .max\_alloc\_size = 0, \

1168 }; \

1169 static STRUCT\_SECTION\_ITERABLE(net\_buf\_pool, \_name) = \

1170 NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_data\_alloc\_##\_name, \

1171 \_net\_buf\_##\_name, \_count, \_ud\_size, \

1172 \_destroy)

1173

[ 1195](group__net__buf.md#ga810aba8ba321fd012edc238ea9fe19dc)#define NET\_BUF\_POOL\_DEFINE(\_name, \_count, \_size, \_ud\_size, \_destroy) \

1196 NET\_BUF\_POOL\_FIXED\_DEFINE(\_name, \_count, \_size, \_ud\_size, \_destroy)

1197

[ 1205](group__net__buf.md#ga145f4b2de7548814eaa7ba86fb123989)struct [net\_buf\_pool](structnet__buf__pool.md) \*[net\_buf\_pool\_get](group__net__buf.md#ga145f4b2de7548814eaa7ba86fb123989)(int id);

1206

[ 1219](group__net__buf.md#gad89e43832ff01c4b333a3d6fd34d0517)int [net\_buf\_id](group__net__buf.md#gad89e43832ff01c4b333a3d6fd34d0517)(struct [net\_buf](structnet__buf.md) \*buf);

1220

1235#if defined(CONFIG\_NET\_BUF\_LOG)

1236struct [net\_buf](structnet__buf.md) \* \_\_must\_check net\_buf\_alloc\_fixed\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1237 [k\_timeout\_t](structk__timeout__t.md) timeout,

1238 const char \*func,

1239 int line);

1240#define net\_buf\_alloc\_fixed(\_pool, \_timeout) \

1241 net\_buf\_alloc\_fixed\_debug(\_pool, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1242#else

[ 1243](group__net__buf.md#ga686df794ec6881625b54454a33587bab)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_alloc\_fixed](group__net__buf.md#ga686df794ec6881625b54454a33587bab)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1244 [k\_timeout\_t](structk__timeout__t.md) timeout);

1245#endif

1246

[ 1250](group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005)static inline struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_alloc](group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1251 [k\_timeout\_t](structk__timeout__t.md) timeout)

1252{

1253 return [net\_buf\_alloc\_fixed](group__net__buf.md#ga686df794ec6881625b54454a33587bab)(pool, timeout);

1254}

1255

1271#if defined(CONFIG\_NET\_BUF\_LOG)

1272struct [net\_buf](structnet__buf.md) \* \_\_must\_check net\_buf\_alloc\_len\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1273 size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527),

1274 [k\_timeout\_t](structk__timeout__t.md) timeout,

1275 const char \*func,

1276 int line);

1277#define net\_buf\_alloc\_len(\_pool, \_size, \_timeout) \

1278 net\_buf\_alloc\_len\_debug(\_pool, \_size, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1279#else

[ 1280](group__net__buf.md#ga11d489aedcca82117965fa6ba9d11ca5)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_alloc\_len](group__net__buf.md#ga11d489aedcca82117965fa6ba9d11ca5)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1281 size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527),

1282 [k\_timeout\_t](structk__timeout__t.md) timeout);

1283#endif

1284

1304#if defined(CONFIG\_NET\_BUF\_LOG)

1305struct [net\_buf](structnet__buf.md) \* \_\_must\_check net\_buf\_alloc\_with\_data\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1306 void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527),

1307 [k\_timeout\_t](structk__timeout__t.md) timeout,

1308 const char \*func, int line);

1309#define net\_buf\_alloc\_with\_data(\_pool, \_data\_, \_size, \_timeout) \

1310 net\_buf\_alloc\_with\_data\_debug(\_pool, \_data\_, \_size, \_timeout, \

1311 \_\_func\_\_, \_\_LINE\_\_)

1312#else

[ 1313](group__net__buf.md#ga8c24d0761d6d38facb6cca60c7c13c0c)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_alloc\_with\_data](group__net__buf.md#ga8c24d0761d6d38facb6cca60c7c13c0c)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1314 void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527),

1315 [k\_timeout\_t](structk__timeout__t.md) timeout);

1316#endif

1317

1331#if defined(CONFIG\_NET\_BUF\_LOG)

1332struct [net\_buf](structnet__buf.md) \* \_\_must\_check net\_buf\_get\_debug(struct [k\_fifo](structk__fifo.md) \*fifo,

1333 [k\_timeout\_t](structk__timeout__t.md) timeout,

1334 const char \*func, int line);

1335#define net\_buf\_get(\_fifo, \_timeout) \

1336 net\_buf\_get\_debug(\_fifo, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1337#else

[ 1338](group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_get](group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742)(struct [k\_fifo](structk__fifo.md) \*fifo,

1339 [k\_timeout\_t](structk__timeout__t.md) timeout);

1340#endif

1341

[ 1351](group__net__buf.md#ga739249547eb37b839b3c1ebdbcb88d28)static inline void [net\_buf\_destroy](group__net__buf.md#ga739249547eb37b839b3c1ebdbcb88d28)(struct [net\_buf](structnet__buf.md) \*buf)

1352{

1353 struct [net\_buf\_pool](structnet__buf__pool.md) \*pool = [net\_buf\_pool\_get](group__net__buf.md#ga145f4b2de7548814eaa7ba86fb123989)(buf->[pool\_id](structnet__buf.md#a45f294bac054d64034bddcc4c6574d29));

1354

1355 if (buf->\_\_buf) {

1356 if (!(buf->[flags](structnet__buf.md#aa4fcce2e2894fc5dbd9cc74fc020647e) & [NET\_BUF\_EXTERNAL\_DATA](group__net__buf.md#gaaeacbdf3cfda12691c75253015e5c19a))) {

1357 pool->[alloc](structnet__buf__pool.md#a617bd8f77e55481d97183da8c0c62cc5)->[cb](structnet__buf__data__alloc.md#a5e69e95df9a975707d45f7682e5d7f56)->[unref](structnet__buf__data__cb.md#a80c307edcf878bde8d43813854185575)(buf, buf->\_\_buf);

1358 }

1359 buf->\_\_buf = NULL;

1360 }

1361

1362 [k\_lifo\_put](group__lifo__apis.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)(&pool->[free](structnet__buf__pool.md#a97e5b2e51238e859f93882a8008ba305), buf);

1363}

1364

[ 1372](group__net__buf.md#ga1292f38b096fd80e31889aff44b0c021)void [net\_buf\_reset](group__net__buf.md#ga1292f38b096fd80e31889aff44b0c021)(struct [net\_buf](structnet__buf.md) \*buf);

1373

[ 1382](group__net__buf.md#ga0e5d3d938becfefc4f4b4d083cb467aa)void [net\_buf\_simple\_reserve](group__net__buf.md#ga0e5d3d938becfefc4f4b4d083cb467aa)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t reserve);

1383

[ 1393](group__net__buf.md#ga6d2dfc45e1e5acf21fe08359a4f92a18)void [net\_buf\_slist\_put](group__net__buf.md#ga6d2dfc45e1e5acf21fe08359a4f92a18)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, struct [net\_buf](structnet__buf.md) \*buf);

1394

[ 1405](group__net__buf.md#ga218d4a0c160c57a44946154478724cb3)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_slist\_get](group__net__buf.md#ga218d4a0c160c57a44946154478724cb3)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

1406

[ 1416](group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047)void [net\_buf\_put](group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047)(struct [k\_fifo](structk__fifo.md) \*fifo, struct [net\_buf](structnet__buf.md) \*buf);

1417

1425#if defined(CONFIG\_NET\_BUF\_LOG)

1426void net\_buf\_unref\_debug(struct [net\_buf](structnet__buf.md) \*buf, const char \*func, int line);

1427#define net\_buf\_unref(\_buf) \

1428 net\_buf\_unref\_debug(\_buf, \_\_func\_\_, \_\_LINE\_\_)

1429#else

[ 1430](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273)void [net\_buf\_unref](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273)(struct [net\_buf](structnet__buf.md) \*buf);

1431#endif

1432

[ 1440](group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_ref](group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f)(struct [net\_buf](structnet__buf.md) \*buf);

1441

[ 1455](group__net__buf.md#gaf4d80e2878e3c790fff206bec820f03f)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_clone](group__net__buf.md#gaf4d80e2878e3c790fff206bec820f03f)(struct [net\_buf](structnet__buf.md) \*buf,

1456 [k\_timeout\_t](structk__timeout__t.md) timeout);

1457

[ 1465](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)static inline void \* \_\_must\_check [net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)(const struct [net\_buf](structnet__buf.md) \*buf)

1466{

1467 return (void \*)buf->[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7);

1468}

1469

[ 1478](group__net__buf.md#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)static inline void [net\_buf\_reserve](group__net__buf.md#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)(struct [net\_buf](structnet__buf.md) \*buf, size\_t reserve)

1479{

1480 [net\_buf\_simple\_reserve](group__net__buf.md#ga0e5d3d938becfefc4f4b4d083cb467aa)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), reserve);

1481}

1482

[ 1494](group__net__buf.md#ga30776d2b21f06d244c083af5c25b0f3e)static inline void \*[net\_buf\_add](group__net__buf.md#ga30776d2b21f06d244c083af5c25b0f3e)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

1495{

1496 return [net\_buf\_simple\_add](group__net__buf.md#ga1906e637c848948f5780428a99b3341e)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

1497}

1498

[ 1511](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f)static inline void \*[net\_buf\_add\_mem](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f)(struct [net\_buf](structnet__buf.md) \*buf, const void \*mem,

1512 size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

1513{

1514 return [net\_buf\_simple\_add\_mem](group__net__buf.md#gac37209c1e5097e5610860943fb7d0115)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), mem, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

1515}

1516

[ 1528](group__net__buf.md#ga868ac2bea103fed568b461cbcd45eda2)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[net\_buf\_add\_u8](group__net__buf.md#ga868ac2bea103fed568b461cbcd45eda2)(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val)

1529{

1530 return [net\_buf\_simple\_add\_u8](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1531}

1532

[ 1543](group__net__buf.md#gadd6d01a3b1efd0de16f9bef975809404)static inline void [net\_buf\_add\_le16](group__net__buf.md#gadd6d01a3b1efd0de16f9bef975809404)(struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val)

1544{

1545 [net\_buf\_simple\_add\_le16](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1546}

1547

[ 1558](group__net__buf.md#ga61878a9bd7462ca925eac39181f2972c)static inline void [net\_buf\_add\_be16](group__net__buf.md#ga61878a9bd7462ca925eac39181f2972c)(struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val)

1559{

1560 [net\_buf\_simple\_add\_be16](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1561}

1562

[ 1573](group__net__buf.md#ga32b90364091ade229830686f03b25d4c)static inline void [net\_buf\_add\_le24](group__net__buf.md#ga32b90364091ade229830686f03b25d4c)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1574{

1575 [net\_buf\_simple\_add\_le24](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1576}

1577

[ 1588](group__net__buf.md#ga0f3cd9f9b364a2d2125aea19221d3e1e)static inline void [net\_buf\_add\_be24](group__net__buf.md#ga0f3cd9f9b364a2d2125aea19221d3e1e)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1589{

1590 [net\_buf\_simple\_add\_be24](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1591}

1592

[ 1603](group__net__buf.md#gae8ba33b6592ef7fd859b35d63b285d87)static inline void [net\_buf\_add\_le32](group__net__buf.md#gae8ba33b6592ef7fd859b35d63b285d87)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1604{

1605 [net\_buf\_simple\_add\_le32](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1606}

1607

[ 1618](group__net__buf.md#ga5543d00c96f83970f8dbf3670a9dc3fc)static inline void [net\_buf\_add\_be32](group__net__buf.md#ga5543d00c96f83970f8dbf3670a9dc3fc)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1619{

1620 [net\_buf\_simple\_add\_be32](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1621}

1622

[ 1633](group__net__buf.md#gaf19bf75c3d4d645b1eebf9254aa22790)static inline void [net\_buf\_add\_le48](group__net__buf.md#gaf19bf75c3d4d645b1eebf9254aa22790)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1634{

1635 [net\_buf\_simple\_add\_le48](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1636}

1637

[ 1648](group__net__buf.md#ga8fe6feb191ab338e91bd62f44e184deb)static inline void [net\_buf\_add\_be48](group__net__buf.md#ga8fe6feb191ab338e91bd62f44e184deb)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1649{

1650 [net\_buf\_simple\_add\_be48](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1651}

1652

[ 1663](group__net__buf.md#gac3f955f8fecc0e5971d2e5e8176e973e)static inline void [net\_buf\_add\_le64](group__net__buf.md#gac3f955f8fecc0e5971d2e5e8176e973e)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1664{

1665 [net\_buf\_simple\_add\_le64](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1666}

1667

[ 1678](group__net__buf.md#ga055f6eb7d5fbc9a3cf529a9ed00970c4)static inline void [net\_buf\_add\_be64](group__net__buf.md#ga055f6eb7d5fbc9a3cf529a9ed00970c4)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1679{

1680 [net\_buf\_simple\_add\_be64](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1681}

1682

[ 1693](group__net__buf.md#gace5ad98eac4772db3b0fa2181912f1f0)static inline void \*[net\_buf\_remove\_mem](group__net__buf.md#gace5ad98eac4772db3b0fa2181912f1f0)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

1694{

1695 return [net\_buf\_simple\_remove\_mem](group__net__buf.md#ga8473bdffadc05b22335a321df89f4b83)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

1696}

1697

[ 1708](group__net__buf.md#gad954b9f37790d5e7087db7db7bdedd41)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_buf\_remove\_u8](group__net__buf.md#gad954b9f37790d5e7087db7db7bdedd41)(struct [net\_buf](structnet__buf.md) \*buf)

1709{

1710 return [net\_buf\_simple\_remove\_u8](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1711}

1712

[ 1723](group__net__buf.md#gaaf654110fb6a8bdfc27433945d4d1308)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_remove\_le16](group__net__buf.md#gaaf654110fb6a8bdfc27433945d4d1308)(struct [net\_buf](structnet__buf.md) \*buf)

1724{

1725 return [net\_buf\_simple\_remove\_le16](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1726}

1727

[ 1738](group__net__buf.md#ga5da86c8ea703ab3f01c408cce73b0651)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_remove\_be16](group__net__buf.md#ga5da86c8ea703ab3f01c408cce73b0651)(struct [net\_buf](structnet__buf.md) \*buf)

1739{

1740 return [net\_buf\_simple\_remove\_be16](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1741}

1742

[ 1753](group__net__buf.md#ga6f346a9af570528d238592851240fd74)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_remove\_be24](group__net__buf.md#ga6f346a9af570528d238592851240fd74)(struct [net\_buf](structnet__buf.md) \*buf)

1754{

1755 return [net\_buf\_simple\_remove\_be24](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1756}

1757

[ 1768](group__net__buf.md#ga903f59c8dea1b2c54969b567fe315041)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_remove\_le24](group__net__buf.md#ga903f59c8dea1b2c54969b567fe315041)(struct [net\_buf](structnet__buf.md) \*buf)

1769{

1770 return [net\_buf\_simple\_remove\_le24](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1771}

1772

[ 1783](group__net__buf.md#gae9321a469cc751c58cfb532afd57d265)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_remove\_le32](group__net__buf.md#gae9321a469cc751c58cfb532afd57d265)(struct [net\_buf](structnet__buf.md) \*buf)

1784{

1785 return [net\_buf\_simple\_remove\_le32](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1786}

1787

[ 1798](group__net__buf.md#gacce707d646d7008ec3167af1a0b20da8)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_remove\_be32](group__net__buf.md#gacce707d646d7008ec3167af1a0b20da8)(struct [net\_buf](structnet__buf.md) \*buf)

1799{

1800 return [net\_buf\_simple\_remove\_be32](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1801}

1802

[ 1813](group__net__buf.md#ga0c147d9f95e2224696a8ace26f63a300)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_le48](group__net__buf.md#ga0c147d9f95e2224696a8ace26f63a300)(struct [net\_buf](structnet__buf.md) \*buf)

1814{

1815 return [net\_buf\_simple\_remove\_le48](group__net__buf.md#gac0628bbbe5d9c2b82766d5a17e767696)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1816}

1817

[ 1828](group__net__buf.md#gaab0e3bcc21c958c01ef076cd0efe087c)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_be48](group__net__buf.md#gaab0e3bcc21c958c01ef076cd0efe087c)(struct [net\_buf](structnet__buf.md) \*buf)

1829{

1830 return [net\_buf\_simple\_remove\_be48](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1831}

1832

[ 1843](group__net__buf.md#ga447b9c6be3fe04a50eb35dd29f190b6d)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_le64](group__net__buf.md#ga447b9c6be3fe04a50eb35dd29f190b6d)(struct [net\_buf](structnet__buf.md) \*buf)

1844{

1845 return [net\_buf\_simple\_remove\_le64](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1846}

1847

[ 1858](group__net__buf.md#ga8b9edd213da2d48dfb8d70a8d307ba13)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_be64](group__net__buf.md#ga8b9edd213da2d48dfb8d70a8d307ba13)(struct [net\_buf](structnet__buf.md) \*buf)

1859{

1860 return [net\_buf\_simple\_remove\_be64](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

1861}

1862

[ 1874](group__net__buf.md#ga96a2b1f07f3a7958057d9c7cc1f01b73)static inline void \*[net\_buf\_push](group__net__buf.md#ga96a2b1f07f3a7958057d9c7cc1f01b73)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

1875{

1876 return [net\_buf\_simple\_push](group__net__buf.md#ga64df9754665440370340c6dddde625d1)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

1877}

1878

[ 1891](group__net__buf.md#ga7e9daccec8cae1b9bfda52b0758adf0c)static inline void \*[net\_buf\_push\_mem](group__net__buf.md#ga7e9daccec8cae1b9bfda52b0758adf0c)(struct [net\_buf](structnet__buf.md) \*buf, const void \*mem,

1892 size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

1893{

1894 return [net\_buf\_simple\_push\_mem](group__net__buf.md#gaaa838083c610f7426c509efaae69a511)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), mem, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

1895}

1896

[ 1905](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186)static inline void [net\_buf\_push\_u8](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186)(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val)

1906{

1907 [net\_buf\_simple\_push\_u8](group__net__buf.md#ga0f19da70bfc8f597680ee02c21226a77)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1908}

1909

[ 1919](group__net__buf.md#gab6c84c6846c06c2b339bc88df35e2655)static inline void [net\_buf\_push\_le16](group__net__buf.md#gab6c84c6846c06c2b339bc88df35e2655)(struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val)

1920{

1921 [net\_buf\_simple\_push\_le16](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1922}

1923

[ 1933](group__net__buf.md#ga6dd756ff8332d076f5d37c69e6c534b5)static inline void [net\_buf\_push\_be16](group__net__buf.md#ga6dd756ff8332d076f5d37c69e6c534b5)(struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val)

1934{

1935 [net\_buf\_simple\_push\_be16](group__net__buf.md#ga827bd85eba0dbd098790d84d22e8e32d)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1936}

1937

[ 1947](group__net__buf.md#ga87524ac50e53ba59c6692af10cf001b9)static inline void [net\_buf\_push\_le24](group__net__buf.md#ga87524ac50e53ba59c6692af10cf001b9)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1948{

1949 [net\_buf\_simple\_push\_le24](group__net__buf.md#gabe52d6735d835edc361666bb3413b907)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1950}

1951

[ 1961](group__net__buf.md#ga87338399d8ecd64a894908ed4a2f710b)static inline void [net\_buf\_push\_be24](group__net__buf.md#ga87338399d8ecd64a894908ed4a2f710b)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1962{

1963 [net\_buf\_simple\_push\_be24](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1964}

1965

[ 1975](group__net__buf.md#ga97c9046185d6a1e9235bf6914c72dfc4)static inline void [net\_buf\_push\_le32](group__net__buf.md#ga97c9046185d6a1e9235bf6914c72dfc4)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1976{

1977 [net\_buf\_simple\_push\_le32](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1978}

1979

[ 1989](group__net__buf.md#gae4e64a23708ed910fb6c3ab8ba481a4c)static inline void [net\_buf\_push\_be32](group__net__buf.md#gae4e64a23708ed910fb6c3ab8ba481a4c)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1990{

1991 [net\_buf\_simple\_push\_be32](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

1992}

1993

[ 2003](group__net__buf.md#ga852654f7e59951bf3536e3f4e98761bf)static inline void [net\_buf\_push\_le48](group__net__buf.md#ga852654f7e59951bf3536e3f4e98761bf)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2004{

2005 [net\_buf\_simple\_push\_le48](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

2006}

2007

[ 2017](group__net__buf.md#gabfbcb051019ff210cc2b85adcf4bc821)static inline void [net\_buf\_push\_be48](group__net__buf.md#gabfbcb051019ff210cc2b85adcf4bc821)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2018{

2019 [net\_buf\_simple\_push\_be48](group__net__buf.md#ga1ea39c7d7e9ba4e10d31d818e45e192a)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

2020}

2021

[ 2031](group__net__buf.md#gad4ee42b023881f80211fbeca53a0f25d)static inline void [net\_buf\_push\_le64](group__net__buf.md#gad4ee42b023881f80211fbeca53a0f25d)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2032{

2033 [net\_buf\_simple\_push\_le64](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

2034}

2035

[ 2045](group__net__buf.md#ga43ff5faab0b099a355b9b96b7b0e3d8c)static inline void [net\_buf\_push\_be64](group__net__buf.md#ga43ff5faab0b099a355b9b96b7b0e3d8c)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2046{

2047 [net\_buf\_simple\_push\_be64](group__net__buf.md#gafea2201655955ab004b5f77106998ae9)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), val);

2048}

2049

[ 2061](group__net__buf.md#gaef433d92734dd8691c292abdb823ba0e)static inline void \*[net\_buf\_pull](group__net__buf.md#gaef433d92734dd8691c292abdb823ba0e)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

2062{

2063 return [net\_buf\_simple\_pull](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2064}

2065

[ 2077](group__net__buf.md#gaedc5ffe19bb0ec438e633023c3c5de74)static inline void \*[net\_buf\_pull\_mem](group__net__buf.md#gaedc5ffe19bb0ec438e633023c3c5de74)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

2078{

2079 return [net\_buf\_simple\_pull\_mem](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750), [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2080}

2081

[ 2092](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)(struct [net\_buf](structnet__buf.md) \*buf)

2093{

2094 return [net\_buf\_simple\_pull\_u8](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2095}

2096

[ 2107](group__net__buf.md#gaed64e9f2b969f2c0d99cd281e73c860a)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_pull\_le16](group__net__buf.md#gaed64e9f2b969f2c0d99cd281e73c860a)(struct [net\_buf](structnet__buf.md) \*buf)

2108{

2109 return [net\_buf\_simple\_pull\_le16](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2110}

2111

[ 2122](group__net__buf.md#ga97909a33c374a5c757fd2faf582139b7)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_pull\_be16](group__net__buf.md#ga97909a33c374a5c757fd2faf582139b7)(struct [net\_buf](structnet__buf.md) \*buf)

2123{

2124 return [net\_buf\_simple\_pull\_be16](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2125}

2126

[ 2137](group__net__buf.md#ga85c505321484a50ed9422f24934ed077)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_pull\_le24](group__net__buf.md#ga85c505321484a50ed9422f24934ed077)(struct [net\_buf](structnet__buf.md) \*buf)

2138{

2139 return [net\_buf\_simple\_pull\_le24](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2140}

2141

[ 2152](group__net__buf.md#ga8de937e8775879712ea0acbf60327a95)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_pull\_be24](group__net__buf.md#ga8de937e8775879712ea0acbf60327a95)(struct [net\_buf](structnet__buf.md) \*buf)

2153{

2154 return [net\_buf\_simple\_pull\_be24](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2155}

2156

[ 2167](group__net__buf.md#ga5f051078f1ffcc40e9ad40e7545a084f)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_pull\_le32](group__net__buf.md#ga5f051078f1ffcc40e9ad40e7545a084f)(struct [net\_buf](structnet__buf.md) \*buf)

2168{

2169 return [net\_buf\_simple\_pull\_le32](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2170}

2171

[ 2182](group__net__buf.md#ga5f8f2e2244eb574b3e57d09d85412967)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_pull\_be32](group__net__buf.md#ga5f8f2e2244eb574b3e57d09d85412967)(struct [net\_buf](structnet__buf.md) \*buf)

2183{

2184 return [net\_buf\_simple\_pull\_be32](group__net__buf.md#ga1a53892ed75f994bbbb3a2bcf1743d3c)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2185}

2186

[ 2197](group__net__buf.md#ga7eeee45b6639146d1492f92263ee4f51)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_le48](group__net__buf.md#ga7eeee45b6639146d1492f92263ee4f51)(struct [net\_buf](structnet__buf.md) \*buf)

2198{

2199 return [net\_buf\_simple\_pull\_le48](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2200}

2201

[ 2212](group__net__buf.md#ga68934e105c4b3a8e27aa61b3ec5526db)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_be48](group__net__buf.md#ga68934e105c4b3a8e27aa61b3ec5526db)(struct [net\_buf](structnet__buf.md) \*buf)

2213{

2214 return [net\_buf\_simple\_pull\_be48](group__net__buf.md#ga19bdefe740fe94a42fba76d71b4ef6e2)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2215}

2216

[ 2227](group__net__buf.md#ga9a3df35e2287cbcfe1b60e2efa52c64e)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_le64](group__net__buf.md#ga9a3df35e2287cbcfe1b60e2efa52c64e)(struct [net\_buf](structnet__buf.md) \*buf)

2228{

2229 return [net\_buf\_simple\_pull\_le64](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2230}

2231

[ 2242](group__net__buf.md#ga3c1e80741a49691e69e57c891d3edb05)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_be64](group__net__buf.md#ga3c1e80741a49691e69e57c891d3edb05)(struct [net\_buf](structnet__buf.md) \*buf)

2243{

2244 return [net\_buf\_simple\_pull\_be64](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2245}

2246

[ 2256](group__net__buf.md#ga605f725e051ddf153ad7f7d50340d812)static inline size\_t [net\_buf\_tailroom](group__net__buf.md#ga605f725e051ddf153ad7f7d50340d812)(struct [net\_buf](structnet__buf.md) \*buf)

2257{

2258 return [net\_buf\_simple\_tailroom](group__net__buf.md#ga59b2e4d1c5c5743ba20eba3bf35ac39e)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2259}

2260

[ 2270](group__net__buf.md#ga0962940eddb100072e075088629b5bb5)static inline size\_t [net\_buf\_headroom](group__net__buf.md#ga0962940eddb100072e075088629b5bb5)(struct [net\_buf](structnet__buf.md) \*buf)

2271{

2272 return [net\_buf\_simple\_headroom](group__net__buf.md#gacfdef39367c6de8a1b4479c3647cca76)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2273}

2274

[ 2284](group__net__buf.md#gaab5b7f481c8e31a3b6439cbc7bbe31e8)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_max\_len](group__net__buf.md#gaab5b7f481c8e31a3b6439cbc7bbe31e8)(struct [net\_buf](structnet__buf.md) \*buf)

2285{

2286 return [net\_buf\_simple\_max\_len](group__net__buf.md#ga7deeb4a89b90a3784e582abcb81d5126)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2287}

2288

[ 2298](group__net__buf.md#gac8271c56f28b68cc58ee9e7a062eebe0)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[net\_buf\_tail](group__net__buf.md#gac8271c56f28b68cc58ee9e7a062eebe0)(struct [net\_buf](structnet__buf.md) \*buf)

2299{

2300 return [net\_buf\_simple\_tail](group__net__buf.md#ga8d623415477ed880ceb1fb8861832309)(&buf->[b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750));

2301}

2302

[ 2308](group__net__buf.md#ga042ce3f2e7e3fd0948ca2623fff36746)struct [net\_buf](structnet__buf.md) \*[net\_buf\_frag\_last](group__net__buf.md#ga042ce3f2e7e3fd0948ca2623fff36746)(struct [net\_buf](structnet__buf.md) \*[frags](structnet__buf.md#a1fa032cc23854c35eae013020823fa88));

2309

[ 2321](group__net__buf.md#gac032b44db4a845dba8303fecfe1b63e7)void [net\_buf\_frag\_insert](group__net__buf.md#gac032b44db4a845dba8303fecfe1b63e7)(struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag);

2322

[ 2337](group__net__buf.md#ga0d7e310802a2bc7b2078f9310827535f)struct [net\_buf](structnet__buf.md) \*[net\_buf\_frag\_add](group__net__buf.md#ga0d7e310802a2bc7b2078f9310827535f)(struct [net\_buf](structnet__buf.md) \*head, struct [net\_buf](structnet__buf.md) \*frag);

2338

2348#if defined(CONFIG\_NET\_BUF\_LOG)

2349struct [net\_buf](structnet__buf.md) \*net\_buf\_frag\_del\_debug(struct [net\_buf](structnet__buf.md) \*parent,

2350 struct [net\_buf](structnet__buf.md) \*frag,

2351 const char \*func, int line);

2352#define net\_buf\_frag\_del(\_parent, \_frag) \

2353 net\_buf\_frag\_del\_debug(\_parent, \_frag, \_\_func\_\_, \_\_LINE\_\_)

2354#else

[ 2355](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff)struct [net\_buf](structnet__buf.md) \*[net\_buf\_frag\_del](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff)(struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag);

2356#endif

2357

[ 2373](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065)size\_t [net\_buf\_linearize](group__net__buf.md#gaf99e2d191233b285cef18aa43c828a86)(void \*dst, size\_t dst\_len,

2374 struct [net\_buf](structnet__buf.md) \*src, size\_t offset, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2375

2390typedef struct [net\_buf](structnet__buf.md) \* \_\_must\_check (\*[net\_buf\_allocator\_cb](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065))([k\_timeout\_t](structk__timeout__t.md) timeout,

2391 void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

2392

[ 2414](group__net__buf.md#ga646d680491753b3ed29fa83c26732d1a)size\_t [net\_buf\_append\_bytes](group__net__buf.md#ga646d680491753b3ed29fa83c26732d1a)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38),

2415 const void \*value, [k\_timeout\_t](structk__timeout__t.md) timeout,

2416 [net\_buf\_allocator\_cb](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065) allocate\_cb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

2417

[ 2432](group__net__buf.md#gaef938c3ab676a5bd5bf8338b8d7cb30c)size\_t [net\_buf\_data\_match](group__net__buf.md#gaef938c3ab676a5bd5bf8338b8d7cb30c)(const struct [net\_buf](structnet__buf.md) \*buf, size\_t offset, const void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2433

[ 2449](group__net__buf.md#ga2d7096280d4fa6f5e32c4674d542889b)static inline struct [net\_buf](structnet__buf.md) \*[net\_buf\_skip](group__net__buf.md#ga2d7096280d4fa6f5e32c4674d542889b)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

2450{

2451 while (buf && [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)--) {

2452 [net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)(buf);

2453 if (!buf->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)) {

2454 buf = [net\_buf\_frag\_del](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff)(NULL, buf);

2455 }

2456 }

2457

2458 return buf;

2459}

2460

[ 2471](group__net__buf.md#gaea38d8a418b739fa335e30ed91d9943d)static inline size\_t [net\_buf\_frags\_len](group__net__buf.md#gaea38d8a418b739fa335e30ed91d9943d)(struct [net\_buf](structnet__buf.md) \*buf)

2472{

2473 size\_t bytes = 0;

2474

2475 while (buf) {

2476 bytes += buf->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38);

2477 buf = buf->[frags](structnet__buf.md#a1fa032cc23854c35eae013020823fa88);

2478 }

2479

2480 return bytes;

2481}

2482

2486

2487#ifdef \_\_cplusplus

2488}

2489#endif

2490

2491#endif /\* ZEPHYR\_INCLUDE\_NET\_BUF\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[k\_lifo\_put](group__lifo__apis.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)

#define k\_lifo\_put(lifo, data)

Add an element to a LIFO queue.

**Definition** kernel.h:2667

[net\_buf\_get](group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742)

struct net\_buf \* net\_buf\_get(struct k\_fifo \*fifo, k\_timeout\_t timeout)

Get a buffer from a FIFO.

[net\_buf\_simple\_clone](group__net__buf.md#ga0186c153b72a379affdd3e2e3994b5a7)

void net\_buf\_simple\_clone(const struct net\_buf\_simple \*original, struct net\_buf\_simple \*clone)

Clone buffer state, using the same data buffer.

[net\_buf\_simple\_init](group__net__buf.md#ga040279b601191367dee013bab9916d8d)

static void net\_buf\_simple\_init(struct net\_buf\_simple \*buf, size\_t reserve\_head)

Initialize a net\_buf\_simple object.

**Definition** buf.h:140

[net\_buf\_frag\_last](group__net__buf.md#ga042ce3f2e7e3fd0948ca2623fff36746)

struct net\_buf \* net\_buf\_frag\_last(struct net\_buf \*frags)

Find the last fragment in the fragment list.

[net\_buf\_add\_be64](group__net__buf.md#ga055f6eb7d5fbc9a3cf529a9ed00970c4)

static void net\_buf\_add\_be64(struct net\_buf \*buf, uint64\_t val)

Add 64-bit value at the end of the buffer.

**Definition** buf.h:1678

[net\_buf\_headroom](group__net__buf.md#ga0962940eddb100072e075088629b5bb5)

static size\_t net\_buf\_headroom(struct net\_buf \*buf)

Check buffer headroom.

**Definition** buf.h:2270

[net\_buf\_simple\_pull\_u8](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7)

uint8\_t net\_buf\_simple\_pull\_u8(struct net\_buf\_simple \*buf)

Remove a 8-bit value from the beginning of the buffer.

[net\_buf\_simple\_remove\_le16](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c)

uint16\_t net\_buf\_simple\_remove\_le16(struct net\_buf\_simple \*buf)

Remove and convert 16 bits from the end of the buffer.

[net\_buf\_remove\_le48](group__net__buf.md#ga0c147d9f95e2224696a8ace26f63a300)

static uint64\_t net\_buf\_remove\_le48(struct net\_buf \*buf)

Remove and convert 48 bits from the end of the buffer.

**Definition** buf.h:1813

[net\_buf\_frag\_add](group__net__buf.md#ga0d7e310802a2bc7b2078f9310827535f)

struct net\_buf \* net\_buf\_frag\_add(struct net\_buf \*head, struct net\_buf \*frag)

Add a new fragment to the end of a chain of bufs.

[net\_buf\_simple\_reserve](group__net__buf.md#ga0e5d3d938becfefc4f4b4d083cb467aa)

void net\_buf\_simple\_reserve(struct net\_buf\_simple \*buf, size\_t reserve)

Initialize buffer with the given headroom.

[net\_buf\_simple\_push\_u8](group__net__buf.md#ga0f19da70bfc8f597680ee02c21226a77)

void net\_buf\_simple\_push\_u8(struct net\_buf\_simple \*buf, uint8\_t val)

Push 8-bit value to the beginning of the buffer.

[net\_buf\_add\_be24](group__net__buf.md#ga0f3cd9f9b364a2d2125aea19221d3e1e)

static void net\_buf\_add\_be24(struct net\_buf \*buf, uint32\_t val)

Add 24-bit value at the end of the buffer.

**Definition** buf.h:1588

[net\_buf\_alloc\_len](group__net__buf.md#ga11d489aedcca82117965fa6ba9d11ca5)

struct net\_buf \* net\_buf\_alloc\_len(struct net\_buf\_pool \*pool, size\_t size, k\_timeout\_t timeout)

Allocate a new variable length buffer from a pool.

[net\_buf\_reset](group__net__buf.md#ga1292f38b096fd80e31889aff44b0c021)

void net\_buf\_reset(struct net\_buf \*buf)

Reset buffer.

[net\_buf\_pool\_get](group__net__buf.md#ga145f4b2de7548814eaa7ba86fb123989)

struct net\_buf\_pool \* net\_buf\_pool\_get(int id)

Looks up a pool based on its ID.

[net\_buf\_simple\_add](group__net__buf.md#ga1906e637c848948f5780428a99b3341e)

void \* net\_buf\_simple\_add(struct net\_buf\_simple \*buf, size\_t len)

Prepare data to be added at the end of the buffer.

[net\_buf\_simple\_pull\_be48](group__net__buf.md#ga19bdefe740fe94a42fba76d71b4ef6e2)

uint64\_t net\_buf\_simple\_pull\_be48(struct net\_buf\_simple \*buf)

Remove and convert 48 bits from the beginning of the buffer.

[net\_buf\_simple\_pull\_be32](group__net__buf.md#ga1a53892ed75f994bbbb3a2bcf1743d3c)

uint32\_t net\_buf\_simple\_pull\_be32(struct net\_buf\_simple \*buf)

Remove and convert 32 bits from the beginning of the buffer.

[net\_buf\_simple\_push\_be48](group__net__buf.md#ga1ea39c7d7e9ba4e10d31d818e45e192a)

void net\_buf\_simple\_push\_be48(struct net\_buf\_simple \*buf, uint64\_t val)

Push 48-bit value to the beginning of the buffer.

[net\_buf\_slist\_get](group__net__buf.md#ga218d4a0c160c57a44946154478724cb3)

struct net\_buf \* net\_buf\_slist\_get(sys\_slist\_t \*list)

Get a buffer from a list.

[net\_buf\_ref](group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f)

struct net\_buf \* net\_buf\_ref(struct net\_buf \*buf)

Increment the reference count of a buffer.

[net\_buf\_skip](group__net__buf.md#ga2d7096280d4fa6f5e32c4674d542889b)

static struct net\_buf \* net\_buf\_skip(struct net\_buf \*buf, size\_t len)

Skip N number of bytes in a net\_buf.

**Definition** buf.h:2449

[net\_buf\_add](group__net__buf.md#ga30776d2b21f06d244c083af5c25b0f3e)

static void \* net\_buf\_add(struct net\_buf \*buf, size\_t len)

Prepare data to be added at the end of the buffer.

**Definition** buf.h:1494

[net\_buf\_add\_le24](group__net__buf.md#ga32b90364091ade229830686f03b25d4c)

static void net\_buf\_add\_le24(struct net\_buf \*buf, uint32\_t val)

Add 24-bit value at the end of the buffer.

**Definition** buf.h:1573

[net\_buf\_simple\_pull\_le32](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353)

uint32\_t net\_buf\_simple\_pull\_le32(struct net\_buf\_simple \*buf)

Remove and convert 32 bits from the beginning of the buffer.

[net\_buf\_simple\_add\_le32](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56)

void net\_buf\_simple\_add\_le32(struct net\_buf\_simple \*buf, uint32\_t val)

Add 32-bit value at the end of the buffer.

[net\_buf\_pull\_be64](group__net__buf.md#ga3c1e80741a49691e69e57c891d3edb05)

static uint64\_t net\_buf\_pull\_be64(struct net\_buf \*buf)

Remove and convert 64 bits from the beginning of the buffer.

**Definition** buf.h:2242

[net\_buf\_push\_be64](group__net__buf.md#ga43ff5faab0b099a355b9b96b7b0e3d8c)

static void net\_buf\_push\_be64(struct net\_buf \*buf, uint64\_t val)

Push 64-bit value to the beginning of the buffer.

**Definition** buf.h:2045

[net\_buf\_remove\_le64](group__net__buf.md#ga447b9c6be3fe04a50eb35dd29f190b6d)

static uint64\_t net\_buf\_remove\_le64(struct net\_buf \*buf)

Remove and convert 64 bits from the end of the buffer.

**Definition** buf.h:1843

[net\_buf\_simple\_reset](group__net__buf.md#ga4b537e913e132448cbf56976504ddddd)

static void net\_buf\_simple\_reset(struct net\_buf\_simple \*buf)

Reset buffer.

**Definition** buf.h:170

[net\_buf\_simple\_pull\_be24](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1)

uint32\_t net\_buf\_simple\_pull\_be24(struct net\_buf\_simple \*buf)

Remove and convert 24 bits from the beginning of the buffer.

[net\_buf\_simple\_pull\_le24](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9)

uint32\_t net\_buf\_simple\_pull\_le24(struct net\_buf\_simple \*buf)

Remove and convert 24 bits from the beginning of the buffer.

[net\_buf\_simple\_remove\_le24](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5)

uint32\_t net\_buf\_simple\_remove\_le24(struct net\_buf\_simple \*buf)

Remove and convert 24 bits from the end of the buffer.

[net\_buf\_simple\_push\_le16](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6)

void net\_buf\_simple\_push\_le16(struct net\_buf\_simple \*buf, uint16\_t val)

Push 16-bit value to the beginning of the buffer.

[net\_buf\_alloc](group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005)

static struct net\_buf \* net\_buf\_alloc(struct net\_buf\_pool \*pool, k\_timeout\_t timeout)

**Definition** buf.h:1250

[net\_buf\_add\_be32](group__net__buf.md#ga5543d00c96f83970f8dbf3670a9dc3fc)

static void net\_buf\_add\_be32(struct net\_buf \*buf, uint32\_t val)

Add 32-bit value at the end of the buffer.

**Definition** buf.h:1618

[net\_buf\_simple\_remove\_le64](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd)

uint64\_t net\_buf\_simple\_remove\_le64(struct net\_buf\_simple \*buf)

Remove and convert 64 bits from the end of the buffer.

[net\_buf\_simple\_tailroom](group__net__buf.md#ga59b2e4d1c5c5743ba20eba3bf35ac39e)

size\_t net\_buf\_simple\_tailroom(struct net\_buf\_simple \*buf)

Check buffer tailroom.

[net\_buf\_simple\_save](group__net__buf.md#ga5b891f335480830a71a5ee2d71f1a3db)

static void net\_buf\_simple\_save(struct net\_buf\_simple \*buf, struct net\_buf\_simple\_state \*state)

Save the parsing state of a buffer.

**Definition** buf.h:869

[net\_buf\_simple\_add\_le48](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25)

void net\_buf\_simple\_add\_le48(struct net\_buf\_simple \*buf, uint64\_t val)

Add 48-bit value at the end of the buffer.

[net\_buf\_remove\_be16](group__net__buf.md#ga5da86c8ea703ab3f01c408cce73b0651)

static uint16\_t net\_buf\_remove\_be16(struct net\_buf \*buf)

Remove and convert 16 bits from the end of the buffer.

**Definition** buf.h:1738

[net\_buf\_simple\_add\_be24](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8)

void net\_buf\_simple\_add\_be24(struct net\_buf\_simple \*buf, uint32\_t val)

Add 24-bit value at the end of the buffer.

[net\_buf\_pull\_le32](group__net__buf.md#ga5f051078f1ffcc40e9ad40e7545a084f)

static uint32\_t net\_buf\_pull\_le32(struct net\_buf \*buf)

Remove and convert 32 bits from the beginning of the buffer.

**Definition** buf.h:2167

[net\_buf\_pull\_be32](group__net__buf.md#ga5f8f2e2244eb574b3e57d09d85412967)

static uint32\_t net\_buf\_pull\_be32(struct net\_buf \*buf)

Remove and convert 32 bits from the beginning of the buffer.

**Definition** buf.h:2182

[net\_buf\_frag\_del](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff)

struct net\_buf \* net\_buf\_frag\_del(struct net\_buf \*parent, struct net\_buf \*frag)

Delete existing fragment from a chain of bufs.

[net\_buf\_simple\_remove\_be64](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932)

uint64\_t net\_buf\_simple\_remove\_be64(struct net\_buf\_simple \*buf)

Remove and convert 64 bits from the end of the buffer.

[net\_buf\_tailroom](group__net__buf.md#ga605f725e051ddf153ad7f7d50340d812)

static size\_t net\_buf\_tailroom(struct net\_buf \*buf)

Check buffer tailroom.

**Definition** buf.h:2256

[net\_buf\_add\_be16](group__net__buf.md#ga61878a9bd7462ca925eac39181f2972c)

static void net\_buf\_add\_be16(struct net\_buf \*buf, uint16\_t val)

Add 16-bit value at the end of the buffer.

**Definition** buf.h:1558

[net\_buf\_append\_bytes](group__net__buf.md#ga646d680491753b3ed29fa83c26732d1a)

size\_t net\_buf\_append\_bytes(struct net\_buf \*buf, size\_t len, const void \*value, k\_timeout\_t timeout, net\_buf\_allocator\_cb allocate\_cb, void \*user\_data)

Append data to a list of net\_buf.

[net\_buf\_simple\_push](group__net__buf.md#ga64df9754665440370340c6dddde625d1)

void \* net\_buf\_simple\_push(struct net\_buf\_simple \*buf, size\_t len)

Prepare data to be added to the start of the buffer.

[net\_buf\_simple\_push\_le48](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e)

void net\_buf\_simple\_push\_le48(struct net\_buf\_simple \*buf, uint64\_t val)

Push 48-bit value to the beginning of the buffer.

[net\_buf\_alloc\_fixed](group__net__buf.md#ga686df794ec6881625b54454a33587bab)

struct net\_buf \* net\_buf\_alloc\_fixed(struct net\_buf\_pool \*pool, k\_timeout\_t timeout)

Allocate a new fixed buffer from a pool.

[net\_buf\_pull\_be48](group__net__buf.md#ga68934e105c4b3a8e27aa61b3ec5526db)

static uint64\_t net\_buf\_pull\_be48(struct net\_buf \*buf)

Remove and convert 48 bits from the beginning of the buffer.

**Definition** buf.h:2212

[net\_buf\_simple\_pull\_le48](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46)

uint64\_t net\_buf\_simple\_pull\_le48(struct net\_buf\_simple \*buf)

Remove and convert 48 bits from the beginning of the buffer.

[net\_buf\_slist\_put](group__net__buf.md#ga6d2dfc45e1e5acf21fe08359a4f92a18)

void net\_buf\_slist\_put(sys\_slist\_t \*list, struct net\_buf \*buf)

Put a buffer into a list.

[net\_buf\_push\_be16](group__net__buf.md#ga6dd756ff8332d076f5d37c69e6c534b5)

static void net\_buf\_push\_be16(struct net\_buf \*buf, uint16\_t val)

Push 16-bit value to the beginning of the buffer.

**Definition** buf.h:1933

[net\_buf\_remove\_be24](group__net__buf.md#ga6f346a9af570528d238592851240fd74)

static uint32\_t net\_buf\_remove\_be24(struct net\_buf \*buf)

Remove and convert 24 bits from the end of the buffer.

**Definition** buf.h:1753

[net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)

static uint8\_t net\_buf\_pull\_u8(struct net\_buf \*buf)

Remove a 8-bit value from the beginning of the buffer.

**Definition** buf.h:2092

[net\_buf\_destroy](group__net__buf.md#ga739249547eb37b839b3c1ebdbcb88d28)

static void net\_buf\_destroy(struct net\_buf \*buf)

Destroy buffer from custom destroy callback.

**Definition** buf.h:1351

[net\_buf\_simple\_push\_le64](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85)

void net\_buf\_simple\_push\_le64(struct net\_buf\_simple \*buf, uint64\_t val)

Push 64-bit value to the beginning of the buffer.

[net\_buf\_simple\_add\_le64](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011)

void net\_buf\_simple\_add\_le64(struct net\_buf\_simple \*buf, uint64\_t val)

Add 64-bit value at the end of the buffer.

[net\_buf\_simple\_max\_len](group__net__buf.md#ga7deeb4a89b90a3784e582abcb81d5126)

uint16\_t net\_buf\_simple\_max\_len(struct net\_buf\_simple \*buf)

Check maximum net\_buf\_simple::len value.

[net\_buf\_simple\_pull\_le64](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e)

uint64\_t net\_buf\_simple\_pull\_le64(struct net\_buf\_simple \*buf)

Remove and convert 64 bits from the beginning of the buffer.

[net\_buf\_put](group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047)

void net\_buf\_put(struct k\_fifo \*fifo, struct net\_buf \*buf)

Put a buffer to the end of a FIFO.

[net\_buf\_push\_mem](group__net__buf.md#ga7e9daccec8cae1b9bfda52b0758adf0c)

static void \* net\_buf\_push\_mem(struct net\_buf \*buf, const void \*mem, size\_t len)

Copies the given number of bytes to the start of the buffer.

**Definition** buf.h:1891

[net\_buf\_pull\_le48](group__net__buf.md#ga7eeee45b6639146d1492f92263ee4f51)

static uint64\_t net\_buf\_pull\_le48(struct net\_buf \*buf)

Remove and convert 48 bits from the beginning of the buffer.

**Definition** buf.h:2197

[net\_buf\_simple\_init\_with\_data](group__net__buf.md#ga7fac47a2a25eaca39c5d14f1f55b485d)

void net\_buf\_simple\_init\_with\_data(struct net\_buf\_simple \*buf, void \*data, size\_t size)

Initialize a net\_buf\_simple object with data.

[net\_buf\_simple\_push\_be16](group__net__buf.md#ga827bd85eba0dbd098790d84d22e8e32d)

void net\_buf\_simple\_push\_be16(struct net\_buf\_simple \*buf, uint16\_t val)

Push 16-bit value to the beginning of the buffer.

[net\_buf\_simple\_remove\_mem](group__net__buf.md#ga8473bdffadc05b22335a321df89f4b83)

void \* net\_buf\_simple\_remove\_mem(struct net\_buf\_simple \*buf, size\_t len)

Remove data from the end of the buffer.

[net\_buf\_push\_le48](group__net__buf.md#ga852654f7e59951bf3536e3f4e98761bf)

static void net\_buf\_push\_le48(struct net\_buf \*buf, uint64\_t val)

Push 48-bit value to the beginning of the buffer.

**Definition** buf.h:2003

[net\_buf\_pull\_le24](group__net__buf.md#ga85c505321484a50ed9422f24934ed077)

static uint32\_t net\_buf\_pull\_le24(struct net\_buf \*buf)

Remove and convert 24 bits from the beginning of the buffer.

**Definition** buf.h:2137

[net\_buf\_simple\_push\_le32](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1)

void net\_buf\_simple\_push\_le32(struct net\_buf\_simple \*buf, uint32\_t val)

Push 32-bit value to the beginning of the buffer.

[net\_buf\_add\_u8](group__net__buf.md#ga868ac2bea103fed568b461cbcd45eda2)

static uint8\_t \* net\_buf\_add\_u8(struct net\_buf \*buf, uint8\_t val)

Add (8-bit) byte at the end of the buffer.

**Definition** buf.h:1528

[net\_buf\_push\_be24](group__net__buf.md#ga87338399d8ecd64a894908ed4a2f710b)

static void net\_buf\_push\_be24(struct net\_buf \*buf, uint32\_t val)

Push 24-bit value to the beginning of the buffer.

**Definition** buf.h:1961

[net\_buf\_push\_le24](group__net__buf.md#ga87524ac50e53ba59c6692af10cf001b9)

static void net\_buf\_push\_le24(struct net\_buf \*buf, uint32\_t val)

Push 24-bit value to the beginning of the buffer.

**Definition** buf.h:1947

[net\_buf\_reserve](group__net__buf.md#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)

static void net\_buf\_reserve(struct net\_buf \*buf, size\_t reserve)

Initialize buffer with the given headroom.

**Definition** buf.h:1478

[net\_buf\_remove\_be64](group__net__buf.md#ga8b9edd213da2d48dfb8d70a8d307ba13)

static uint64\_t net\_buf\_remove\_be64(struct net\_buf \*buf)

Remove and convert 64 bits from the end of the buffer.

**Definition** buf.h:1858

[net\_buf\_alloc\_with\_data](group__net__buf.md#ga8c24d0761d6d38facb6cca60c7c13c0c)

struct net\_buf \* net\_buf\_alloc\_with\_data(struct net\_buf\_pool \*pool, void \*data, size\_t size, k\_timeout\_t timeout)

Allocate a new buffer from a pool but with external data pointer.

[net\_buf\_simple\_tail](group__net__buf.md#ga8d623415477ed880ceb1fb8861832309)

static uint8\_t \* net\_buf\_simple\_tail(struct net\_buf\_simple \*buf)

Get the tail pointer for a buffer.

**Definition** buf.h:809

[net\_buf\_pull\_be24](group__net__buf.md#ga8de937e8775879712ea0acbf60327a95)

static uint32\_t net\_buf\_pull\_be24(struct net\_buf \*buf)

Remove and convert 24 bits from the beginning of the buffer.

**Definition** buf.h:2152

[net\_buf\_simple\_add\_be64](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0)

void net\_buf\_simple\_add\_be64(struct net\_buf\_simple \*buf, uint64\_t val)

Add 64-bit value at the end of the buffer.

[net\_buf\_add\_be48](group__net__buf.md#ga8fe6feb191ab338e91bd62f44e184deb)

static void net\_buf\_add\_be48(struct net\_buf \*buf, uint64\_t val)

Add 48-bit value at the end of the buffer.

**Definition** buf.h:1648

[net\_buf\_simple\_add\_u8](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c)

uint8\_t \* net\_buf\_simple\_add\_u8(struct net\_buf\_simple \*buf, uint8\_t val)

Add (8-bit) byte at the end of the buffer.

[net\_buf\_remove\_le24](group__net__buf.md#ga903f59c8dea1b2c54969b567fe315041)

static uint32\_t net\_buf\_remove\_le24(struct net\_buf \*buf)

Remove and convert 24 bits from the end of the buffer.

**Definition** buf.h:1768

[net\_buf\_push\_u8](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186)

static void net\_buf\_push\_u8(struct net\_buf \*buf, uint8\_t val)

Push 8-bit value to the beginning of the buffer.

**Definition** buf.h:1905

[net\_buf\_simple\_add\_be16](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa)

void net\_buf\_simple\_add\_be16(struct net\_buf\_simple \*buf, uint16\_t val)

Add 16-bit value at the end of the buffer.

[net\_buf\_simple\_remove\_be16](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee)

uint16\_t net\_buf\_simple\_remove\_be16(struct net\_buf\_simple \*buf)

Remove and convert 16 bits from the end of the buffer.

[net\_buf\_push](group__net__buf.md#ga96a2b1f07f3a7958057d9c7cc1f01b73)

static void \* net\_buf\_push(struct net\_buf \*buf, size\_t len)

Prepare data to be added at the start of the buffer.

**Definition** buf.h:1874

[net\_buf\_pull\_be16](group__net__buf.md#ga97909a33c374a5c757fd2faf582139b7)

static uint16\_t net\_buf\_pull\_be16(struct net\_buf \*buf)

Remove and convert 16 bits from the beginning of the buffer.

**Definition** buf.h:2122

[net\_buf\_push\_le32](group__net__buf.md#ga97c9046185d6a1e9235bf6914c72dfc4)

static void net\_buf\_push\_le32(struct net\_buf \*buf, uint32\_t val)

Push 32-bit value to the beginning of the buffer.

**Definition** buf.h:1975

[net\_buf\_pull\_le64](group__net__buf.md#ga9a3df35e2287cbcfe1b60e2efa52c64e)

static uint64\_t net\_buf\_pull\_le64(struct net\_buf \*buf)

Remove and convert 64 bits from the beginning of the buffer.

**Definition** buf.h:2227

[net\_buf\_simple\_remove\_be24](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd)

uint32\_t net\_buf\_simple\_remove\_be24(struct net\_buf\_simple \*buf)

Remove and convert 24 bits from the end of the buffer.

[net\_buf\_allocator\_cb](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065)

struct net\_buf \*(\* net\_buf\_allocator\_cb)(k\_timeout\_t timeout, void \*user\_data)

Network buffer allocator callback.

**Definition** buf.h:2390

[net\_buf\_simple\_pull\_mem](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c)

void \* net\_buf\_simple\_pull\_mem(struct net\_buf\_simple \*buf, size\_t len)

Remove data from the beginning of the buffer.

[net\_buf\_simple\_remove\_le32](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457)

uint32\_t net\_buf\_simple\_remove\_le32(struct net\_buf\_simple \*buf)

Remove and convert 32 bits from the end of the buffer.

[net\_buf\_simple\_add\_le16](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5)

void net\_buf\_simple\_add\_le16(struct net\_buf\_simple \*buf, uint16\_t val)

Add 16-bit value at the end of the buffer.

[net\_buf\_simple\_push\_mem](group__net__buf.md#gaaa838083c610f7426c509efaae69a511)

void \* net\_buf\_simple\_push\_mem(struct net\_buf\_simple \*buf, const void \*mem, size\_t len)

Copy given number of bytes from memory to the start of the buffer.

[net\_buf\_remove\_be48](group__net__buf.md#gaab0e3bcc21c958c01ef076cd0efe087c)

static uint64\_t net\_buf\_remove\_be48(struct net\_buf \*buf)

Remove and convert 48 bits from the end of the buffer.

**Definition** buf.h:1828

[net\_buf\_max\_len](group__net__buf.md#gaab5b7f481c8e31a3b6439cbc7bbe31e8)

static uint16\_t net\_buf\_max\_len(struct net\_buf \*buf)

Check maximum net\_buf::len value.

**Definition** buf.h:2284

[net\_buf\_simple\_add\_be32](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c)

void net\_buf\_simple\_add\_be32(struct net\_buf\_simple \*buf, uint32\_t val)

Add 32-bit value at the end of the buffer.

[NET\_BUF\_EXTERNAL\_DATA](group__net__buf.md#gaaeacbdf3cfda12691c75253015e5c19a)

#define NET\_BUF\_EXTERNAL\_DATA

Flag indicating that the buffer's associated data pointer, points to externally allocated memory.

**Definition** buf.h:901

[net\_buf\_remove\_le16](group__net__buf.md#gaaf654110fb6a8bdfc27433945d4d1308)

static uint16\_t net\_buf\_remove\_le16(struct net\_buf \*buf)

Remove and convert 16 bits from the end of the buffer.

**Definition** buf.h:1723

[net\_buf\_push\_le16](group__net__buf.md#gab6c84c6846c06c2b339bc88df35e2655)

static void net\_buf\_push\_le16(struct net\_buf \*buf, uint16\_t val)

Push 16-bit value to the beginning of the buffer.

**Definition** buf.h:1919

[net\_buf\_simple\_remove\_be48](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb)

uint64\_t net\_buf\_simple\_remove\_be48(struct net\_buf\_simple \*buf)

Remove and convert 48 bits from the end of the buffer.

[net\_buf\_simple\_push\_le24](group__net__buf.md#gabe52d6735d835edc361666bb3413b907)

void net\_buf\_simple\_push\_le24(struct net\_buf\_simple \*buf, uint32\_t val)

Push 24-bit value to the beginning of the buffer.

[net\_buf\_unref](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273)

void net\_buf\_unref(struct net\_buf \*buf)

Decrements the reference count of a buffer.

[net\_buf\_push\_be48](group__net__buf.md#gabfbcb051019ff210cc2b85adcf4bc821)

static void net\_buf\_push\_be48(struct net\_buf \*buf, uint64\_t val)

Push 48-bit value to the beginning of the buffer.

**Definition** buf.h:2017

[net\_buf\_simple\_push\_be24](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72)

void net\_buf\_simple\_push\_be24(struct net\_buf\_simple \*buf, uint32\_t val)

Push 24-bit value to the beginning of the buffer.

[net\_buf\_frag\_insert](group__net__buf.md#gac032b44db4a845dba8303fecfe1b63e7)

void net\_buf\_frag\_insert(struct net\_buf \*parent, struct net\_buf \*frag)

Insert a new fragment to a chain of bufs.

[net\_buf\_simple\_remove\_le48](group__net__buf.md#gac0628bbbe5d9c2b82766d5a17e767696)

uint64\_t net\_buf\_simple\_remove\_le48(struct net\_buf\_simple \*buf)

Remove and convert 48 bits from the end of the buffer.

[net\_buf\_simple\_add\_mem](group__net__buf.md#gac37209c1e5097e5610860943fb7d0115)

void \* net\_buf\_simple\_add\_mem(struct net\_buf\_simple \*buf, const void \*mem, size\_t len)

Copy given number of bytes from memory to the end of the buffer.

[net\_buf\_add\_le64](group__net__buf.md#gac3f955f8fecc0e5971d2e5e8176e973e)

static void net\_buf\_add\_le64(struct net\_buf \*buf, uint64\_t val)

Add 64-bit value at the end of the buffer.

**Definition** buf.h:1663

[net\_buf\_tail](group__net__buf.md#gac8271c56f28b68cc58ee9e7a062eebe0)

static uint8\_t \* net\_buf\_tail(struct net\_buf \*buf)

Get the tail pointer for a buffer.

**Definition** buf.h:2298

[net\_buf\_remove\_be32](group__net__buf.md#gacce707d646d7008ec3167af1a0b20da8)

static uint32\_t net\_buf\_remove\_be32(struct net\_buf \*buf)

Remove and convert 32 bits from the end of the buffer.

**Definition** buf.h:1798

[net\_buf\_remove\_mem](group__net__buf.md#gace5ad98eac4772db3b0fa2181912f1f0)

static void \* net\_buf\_remove\_mem(struct net\_buf \*buf, size\_t len)

Remove data from the end of the buffer.

**Definition** buf.h:1693

[net\_buf\_add\_mem](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f)

static void \* net\_buf\_add\_mem(struct net\_buf \*buf, const void \*mem, size\_t len)

Copies the given number of bytes to the end of the buffer.

**Definition** buf.h:1511

[net\_buf\_simple\_headroom](group__net__buf.md#gacfdef39367c6de8a1b4479c3647cca76)

size\_t net\_buf\_simple\_headroom(struct net\_buf\_simple \*buf)

Check buffer headroom.

[net\_buf\_simple\_pull\_be64](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712)

uint64\_t net\_buf\_simple\_pull\_be64(struct net\_buf\_simple \*buf)

Remove and convert 64 bits from the beginning of the buffer.

[net\_buf\_simple\_push\_be32](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426)

void net\_buf\_simple\_push\_be32(struct net\_buf\_simple \*buf, uint32\_t val)

Push 32-bit value to the beginning of the buffer.

[net\_buf\_push\_le64](group__net__buf.md#gad4ee42b023881f80211fbeca53a0f25d)

static void net\_buf\_push\_le64(struct net\_buf \*buf, uint64\_t val)

Push 64-bit value to the beginning of the buffer.

**Definition** buf.h:2031

[net\_buf\_simple\_pull\_le16](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba)

uint16\_t net\_buf\_simple\_pull\_le16(struct net\_buf\_simple \*buf)

Remove and convert 16 bits from the beginning of the buffer.

[net\_buf\_id](group__net__buf.md#gad89e43832ff01c4b333a3d6fd34d0517)

int net\_buf\_id(struct net\_buf \*buf)

Get a zero-based index for a buffer.

[net\_buf\_remove\_u8](group__net__buf.md#gad954b9f37790d5e7087db7db7bdedd41)

static uint8\_t net\_buf\_remove\_u8(struct net\_buf \*buf)

Remove a 8-bit value from the end of the buffer.

**Definition** buf.h:1708

[net\_buf\_simple\_add\_be48](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171)

void net\_buf\_simple\_add\_be48(struct net\_buf\_simple \*buf, uint64\_t val)

Add 48-bit value at the end of the buffer.

[net\_buf\_add\_le16](group__net__buf.md#gadd6d01a3b1efd0de16f9bef975809404)

static void net\_buf\_add\_le16(struct net\_buf \*buf, uint16\_t val)

Add 16-bit value at the end of the buffer.

**Definition** buf.h:1543

[net\_buf\_simple\_pull\_be16](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440)

uint16\_t net\_buf\_simple\_pull\_be16(struct net\_buf\_simple \*buf)

Remove and convert 16 bits from the beginning of the buffer.

[net\_buf\_push\_be32](group__net__buf.md#gae4e64a23708ed910fb6c3ab8ba481a4c)

static void net\_buf\_push\_be32(struct net\_buf \*buf, uint32\_t val)

Push 32-bit value to the beginning of the buffer.

**Definition** buf.h:1989

[net\_buf\_add\_le32](group__net__buf.md#gae8ba33b6592ef7fd859b35d63b285d87)

static void net\_buf\_add\_le32(struct net\_buf \*buf, uint32\_t val)

Add 32-bit value at the end of the buffer.

**Definition** buf.h:1603

[net\_buf\_simple\_remove\_be32](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)

uint32\_t net\_buf\_simple\_remove\_be32(struct net\_buf\_simple \*buf)

Remove and convert 32 bits from the end of the buffer.

[net\_buf\_remove\_le32](group__net__buf.md#gae9321a469cc751c58cfb532afd57d265)

static uint32\_t net\_buf\_remove\_le32(struct net\_buf \*buf)

Remove and convert 32 bits from the end of the buffer.

**Definition** buf.h:1783

[net\_buf\_frags\_len](group__net__buf.md#gaea38d8a418b739fa335e30ed91d9943d)

static size\_t net\_buf\_frags\_len(struct net\_buf \*buf)

Calculate amount of bytes stored in fragments.

**Definition** buf.h:2471

[net\_buf\_pull\_le16](group__net__buf.md#gaed64e9f2b969f2c0d99cd281e73c860a)

static uint16\_t net\_buf\_pull\_le16(struct net\_buf \*buf)

Remove and convert 16 bits from the beginning of the buffer.

**Definition** buf.h:2107

[net\_buf\_pull\_mem](group__net__buf.md#gaedc5ffe19bb0ec438e633023c3c5de74)

static void \* net\_buf\_pull\_mem(struct net\_buf \*buf, size\_t len)

Remove data from the beginning of the buffer.

**Definition** buf.h:2077

[net\_buf\_simple\_restore](group__net__buf.md#gaedd36481657a7a9d108659d56e131721)

static void net\_buf\_simple\_restore(struct net\_buf\_simple \*buf, struct net\_buf\_simple\_state \*state)

Restore the parsing state of a buffer.

**Definition** buf.h:885

[net\_buf\_pull](group__net__buf.md#gaef433d92734dd8691c292abdb823ba0e)

static void \* net\_buf\_pull(struct net\_buf \*buf, size\_t len)

Remove data from the beginning of the buffer.

**Definition** buf.h:2061

[net\_buf\_data\_match](group__net__buf.md#gaef938c3ab676a5bd5bf8338b8d7cb30c)

size\_t net\_buf\_data\_match(const struct net\_buf \*buf, size\_t offset, const void \*data, size\_t len)

Match data with a net\_buf's content.

[net\_buf\_add\_le48](group__net__buf.md#gaf19bf75c3d4d645b1eebf9254aa22790)

static void net\_buf\_add\_le48(struct net\_buf \*buf, uint64\_t val)

Add 48-bit value at the end of the buffer.

**Definition** buf.h:1633

[net\_buf\_simple\_add\_le24](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6)

void net\_buf\_simple\_add\_le24(struct net\_buf\_simple \*buf, uint32\_t val)

Add 24-bit value at the end of the buffer.

[net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)

static void \* net\_buf\_user\_data(const struct net\_buf \*buf)

Get a pointer to the user data of a buffer.

**Definition** buf.h:1465

[net\_buf\_clone](group__net__buf.md#gaf4d80e2878e3c790fff206bec820f03f)

struct net\_buf \* net\_buf\_clone(struct net\_buf \*buf, k\_timeout\_t timeout)

Clone buffer.

[net\_buf\_simple\_remove\_u8](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3)

uint8\_t net\_buf\_simple\_remove\_u8(struct net\_buf\_simple \*buf)

Remove a 8-bit value from the end of the buffer.

[net\_buf\_simple\_pull](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8)

void \* net\_buf\_simple\_pull(struct net\_buf\_simple \*buf, size\_t len)

Remove data from the beginning of the buffer.

[net\_buf\_linearize](group__net__buf.md#gaf99e2d191233b285cef18aa43c828a86)

size\_t net\_buf\_linearize(void \*dst, size\_t dst\_len, struct net\_buf \*src, size\_t offset, size\_t len)

Copy bytes from net\_buf chain starting at offset to linear buffer.

[net\_buf\_simple\_push\_be64](group__net__buf.md#gafea2201655955ab004b5f77106998ae9)

void net\_buf\_simple\_push\_be64(struct net\_buf\_simple \*buf, uint64\_t val)

Push 64-bit value to the beginning of the buffer.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_lifo](structk__lifo.md)

**Definition** kernel.h:2613

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf\_data\_alloc](structnet__buf__data__alloc.md)

**Definition** buf.h:965

[net\_buf\_data\_alloc::cb](structnet__buf__data__alloc.md#a5e69e95df9a975707d45f7682e5d7f56)

const struct net\_buf\_data\_cb \* cb

**Definition** buf.h:966

[net\_buf\_data\_alloc::max\_alloc\_size](structnet__buf__data__alloc.md#a7eadcd00a72ab69bd5c84f2adba10197)

size\_t max\_alloc\_size

**Definition** buf.h:968

[net\_buf\_data\_alloc::alloc\_data](structnet__buf__data__alloc.md#adcc085065789af4a8e641c2ad7e670af)

void \* alloc\_data

**Definition** buf.h:967

[net\_buf\_data\_cb](structnet__buf__data__cb.md)

**Definition** buf.h:958

[net\_buf\_data\_cb::ref](structnet__buf__data__cb.md#a099e08c1dc2a48c821e381a8ce20cd51)

uint8\_t \*(\* ref)(struct net\_buf \*buf, uint8\_t \*data)

**Definition** buf.h:961

[net\_buf\_data\_cb::alloc](structnet__buf__data__cb.md#a34bf941a262975eef4ff1c6e14a0c78f)

uint8\_t \*(\* alloc)(struct net\_buf \*buf, size\_t \*size, k\_timeout\_t timeout)

**Definition** buf.h:959

[net\_buf\_data\_cb::unref](structnet__buf__data__cb.md#a80c307edcf878bde8d43813854185575)

void(\* unref)(struct net\_buf \*buf, uint8\_t \*data)

**Definition** buf.h:962

[net\_buf\_pool\_fixed](structnet__buf__pool__fixed.md)

**Definition** buf.h:1081

[net\_buf\_pool\_fixed::data\_pool](structnet__buf__pool__fixed.md#a6e17291c5aa8dfe8a478d9b5e4e74596)

uint8\_t \* data\_pool

**Definition** buf.h:1082

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:976

[net\_buf\_pool::destroy](structnet__buf__pool.md#a2a9141d7cd20cd98818a92dc5bc99f56)

void(\*const destroy)(struct net\_buf \*buf)

Optional destroy callback when buffer is freed.

**Definition** buf.h:1004

[net\_buf\_pool::uninit\_count](structnet__buf__pool.md#a3fdf83b4c0b5acefbb761da285791ad2)

uint16\_t uninit\_count

Number of uninitialized buffers.

**Definition** buf.h:987

[net\_buf\_pool::user\_data\_size](structnet__buf__pool.md#a4718ecec19d7e2ccaf04b6ff61120975)

uint8\_t user\_data\_size

**Definition** buf.h:990

[net\_buf\_pool::buf\_count](structnet__buf__pool.md#a55b57f4f573c7e752c3ccf2f92f25626)

const uint16\_t buf\_count

Number of buffers in pool.

**Definition** buf.h:984

[net\_buf\_pool::alloc](structnet__buf__pool.md#a617bd8f77e55481d97183da8c0c62cc5)

const struct net\_buf\_data\_alloc \* alloc

Data allocation handlers.

**Definition** buf.h:1007

[net\_buf\_pool::free](structnet__buf__pool.md#a97e5b2e51238e859f93882a8008ba305)

struct k\_lifo free

LIFO to place the buffer into when free.

**Definition** buf.h:978

[net\_buf\_pool::lock](structnet__buf__pool.md#ae92fc3f3f51be63ccdeee9614d21cc34)

struct k\_spinlock lock

**Definition** buf.h:981

[net\_buf\_simple\_state](structnet__buf__simple__state.md)

Parsing state of a buffer.

**Definition** buf.h:854

[net\_buf\_simple\_state::offset](structnet__buf__simple__state.md#a4061f8e50e14289b1ec999ef490c8fbf)

uint16\_t offset

Offset of the data pointer from the beginning of the storage.

**Definition** buf.h:856

[net\_buf\_simple\_state::len](structnet__buf__simple__state.md#af0e544fe2b018a7ff0b30970e9de8253)

uint16\_t len

Length of data.

**Definition** buf.h:858

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

[net\_buf\_simple::data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** buf.h:89

[net\_buf\_simple::size](structnet__buf__simple.md#ae6dc4aa029a67d3911293618eb30caa6)

uint16\_t size

Amount of data that net\_buf\_simple::\_\_buf can store.

**Definition** buf.h:99

[net\_buf\_simple::len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:96

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** buf.h:942

[net\_buf::frags](structnet__buf.md#a1fa032cc23854c35eae013020823fa88)

struct net\_buf \* frags

Fragments associated with this buffer.

**Definition** buf.h:915

[net\_buf::ref](structnet__buf.md#a42da518a82f4c37c45814b4f8c5f2731)

uint8\_t ref

Reference count.

**Definition** buf.h:918

[net\_buf::pool\_id](structnet__buf.md#a45f294bac054d64034bddcc4c6574d29)

uint8\_t pool\_id

Where the buffer should go when freed up.

**Definition** buf.h:924

[net\_buf::node](structnet__buf.md#a5cc70f57e5b776cfa12b2d556e5958f3)

sys\_snode\_t node

Allow placing the buffer into sys\_slist\_t.

**Definition** buf.h:912

[net\_buf::user\_data\_size](structnet__buf.md#a65db7bed62d7211114767e6ce58dad75)

uint8\_t user\_data\_size

**Definition** buf.h:927

[net\_buf::flags](structnet__buf.md#aa4fcce2e2894fc5dbd9cc74fc020647e)

uint8\_t flags

Bit-field of buffer flags.

**Definition** buf.h:921

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** buf.h:936

[net\_buf::user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7)

uint8\_t user\_data[]

System metadata for this buffer.

**Definition** buf.h:955

[net\_buf::b](structnet__buf.md#ae0c5a1a6613fc2779cbb8c4fc1b25750)

struct net\_buf\_simple b

**Definition** buf.h:951

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:939

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [buf.h](net_2buf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
