---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__buf_8h_source.html
original_path: doxygen/html/net__buf_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_buf.h

[Go to the documentation of this file.](net__buf_8h.md)

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

15#include <[zephyr/sys/util.h](sys_2util_8h.md)>

16#include <[zephyr/kernel.h](kernel_8h.md)>

17#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

31

32/\* Alignment needed for various parts of the buffer definition \*/

33#if CONFIG\_NET\_BUF\_ALIGNMENT == 0

34#define \_\_net\_buf\_align \_\_aligned(sizeof(void \*))

35#else

36#define \_\_net\_buf\_align \_\_aligned(CONFIG\_NET\_BUF\_ALIGNMENT)

37#endif

38

[ 48](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501)#define NET\_BUF\_SIMPLE\_DEFINE(\_name, \_size) \

49 uint8\_t net\_buf\_data\_##\_name[\_size]; \

50 struct net\_buf\_simple \_name = { \

51 .data = net\_buf\_data\_##\_name, \

52 .len = 0, \

53 .size = \_size, \

54 .\_\_buf = net\_buf\_data\_##\_name, \

55 }

56

[ 67](group__net__buf.md#ga21ced8b3082d57bf071008de5fffc0f4)#define NET\_BUF\_SIMPLE\_DEFINE\_STATIC(\_name, \_size) \

68 static \_\_noinit uint8\_t net\_buf\_data\_##\_name[\_size]; \

69 static struct net\_buf\_simple \_name = { \

70 .data = net\_buf\_data\_##\_name, \

71 .len = 0, \

72 .size = \_size, \

73 .\_\_buf = net\_buf\_data\_##\_name, \

74 }

75

[ 89](structnet__buf__simple.md)struct [net\_buf\_simple](structnet__buf__simple.md) {

[ 91](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1);

92

[ 98](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3);

99

[ 101](structnet__buf__simple.md#ae6dc4aa029a67d3911293618eb30caa6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structnet__buf__simple.md#ae6dc4aa029a67d3911293618eb30caa6);

102

106 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\_\_buf;

107};

108

[ 125](group__net__buf.md#ga0b01dc80027d13b1895379d4d1397207)#define NET\_BUF\_SIMPLE(\_size) \

126 ((struct net\_buf\_simple \*)(&(struct { \

127 struct net\_buf\_simple buf; \

128 uint8\_t data[\_size]; \

129 }) { \

130 .buf.size = \_size, \

131 }))

132

[ 142](group__net__buf.md#ga040279b601191367dee013bab9916d8d)static inline void [net\_buf\_simple\_init](group__net__buf.md#ga040279b601191367dee013bab9916d8d)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

143 size\_t reserve\_head)

144{

145 if (!buf->\_\_buf) {

146 buf->\_\_buf = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)buf + sizeof(\*buf);

147 }

148

149 buf->[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) = buf->\_\_buf + reserve\_head;

150 buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) = 0U;

151}

152

[ 162](group__net__buf.md#ga7fac47a2a25eaca39c5d14f1f55b485d)void [net\_buf\_simple\_init\_with\_data](group__net__buf.md#ga7fac47a2a25eaca39c5d14f1f55b485d)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

163 void \*data, size\_t size);

164

[ 172](group__net__buf.md#ga4b537e913e132448cbf56976504ddddd)static inline void [net\_buf\_simple\_reset](group__net__buf.md#ga4b537e913e132448cbf56976504ddddd)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf)

173{

174 buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) = 0U;

175 buf->[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) = buf->\_\_buf;

176}

177

[ 188](group__net__buf.md#ga0186c153b72a379affdd3e2e3994b5a7)void [net\_buf\_simple\_clone](group__net__buf.md#ga0186c153b72a379affdd3e2e3994b5a7)(const struct [net\_buf\_simple](structnet__buf__simple.md) \*original,

189 struct [net\_buf\_simple](structnet__buf__simple.md) \*clone);

190

[ 202](group__net__buf.md#ga1906e637c848948f5780428a99b3341e)void \*[net\_buf\_simple\_add](group__net__buf.md#ga1906e637c848948f5780428a99b3341e)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

203

[ 216](group__net__buf.md#gac37209c1e5097e5610860943fb7d0115)void \*[net\_buf\_simple\_add\_mem](group__net__buf.md#gac37209c1e5097e5610860943fb7d0115)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, const void \*mem,

217 size\_t len);

218

[ 230](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[net\_buf\_simple\_add\_u8](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val);

231

[ 242](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5)void [net\_buf\_simple\_add\_le16](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

243

[ 254](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa)void [net\_buf\_simple\_add\_be16](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

255

[ 266](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6)void [net\_buf\_simple\_add\_le24](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

267

[ 278](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8)void [net\_buf\_simple\_add\_be24](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

279

[ 290](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56)void [net\_buf\_simple\_add\_le32](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

291

[ 302](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c)void [net\_buf\_simple\_add\_be32](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

303

[ 314](group__net__buf.md#ga67da71ba5942cc11e95aa5ba02cb8552)void [net\_buf\_simple\_add\_le40](group__net__buf.md#ga67da71ba5942cc11e95aa5ba02cb8552)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

315

[ 326](group__net__buf.md#ga69bdaf4373693bb468cf3876e9edf239)void [net\_buf\_simple\_add\_be40](group__net__buf.md#ga69bdaf4373693bb468cf3876e9edf239)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

327

[ 338](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25)void [net\_buf\_simple\_add\_le48](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

339

[ 350](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171)void [net\_buf\_simple\_add\_be48](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

351

[ 362](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011)void [net\_buf\_simple\_add\_le64](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

363

[ 374](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0)void [net\_buf\_simple\_add\_be64](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

375

[ 386](group__net__buf.md#ga8473bdffadc05b22335a321df89f4b83)void \*[net\_buf\_simple\_remove\_mem](group__net__buf.md#ga8473bdffadc05b22335a321df89f4b83)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

387

[ 398](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_buf\_simple\_remove\_u8](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

399

[ 410](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_remove\_le16](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

411

[ 422](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_remove\_be16](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

423

[ 434](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_remove\_le24](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

435

[ 446](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_remove\_be24](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

447

[ 458](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_remove\_le32](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

459

[ 470](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_remove\_be32](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

471

[ 482](group__net__buf.md#ga2c937164e648fe8b854cb1144051b6b9)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_le40](group__net__buf.md#ga2c937164e648fe8b854cb1144051b6b9)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

483

[ 494](group__net__buf.md#ga9abd2bccc90cf654556c18322888d131)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_be40](group__net__buf.md#ga9abd2bccc90cf654556c18322888d131)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

495

[ 506](group__net__buf.md#gac0628bbbe5d9c2b82766d5a17e767696)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_le48](group__net__buf.md#gac0628bbbe5d9c2b82766d5a17e767696)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

507

[ 518](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_be48](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

519

[ 530](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_le64](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

531

[ 542](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_remove\_be64](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

543

[ 555](group__net__buf.md#ga64df9754665440370340c6dddde625d1)void \*[net\_buf\_simple\_push](group__net__buf.md#ga64df9754665440370340c6dddde625d1)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

556

[ 569](group__net__buf.md#gaaa838083c610f7426c509efaae69a511)void \*[net\_buf\_simple\_push\_mem](group__net__buf.md#gaaa838083c610f7426c509efaae69a511)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, const void \*mem,

570 size\_t len);

571

[ 581](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6)void [net\_buf\_simple\_push\_le16](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

582

[ 592](group__net__buf.md#ga827bd85eba0dbd098790d84d22e8e32d)void [net\_buf\_simple\_push\_be16](group__net__buf.md#ga827bd85eba0dbd098790d84d22e8e32d)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

593

[ 602](group__net__buf.md#ga0f19da70bfc8f597680ee02c21226a77)void [net\_buf\_simple\_push\_u8](group__net__buf.md#ga0f19da70bfc8f597680ee02c21226a77)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val);

603

[ 613](group__net__buf.md#gabe52d6735d835edc361666bb3413b907)void [net\_buf\_simple\_push\_le24](group__net__buf.md#gabe52d6735d835edc361666bb3413b907)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

614

[ 624](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72)void [net\_buf\_simple\_push\_be24](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

625

[ 635](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1)void [net\_buf\_simple\_push\_le32](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

636

[ 646](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426)void [net\_buf\_simple\_push\_be32](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

647

[ 657](group__net__buf.md#ga745ab6f34138b506b42f78e0975a5d2e)void [net\_buf\_simple\_push\_le40](group__net__buf.md#ga745ab6f34138b506b42f78e0975a5d2e)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

658

[ 668](group__net__buf.md#gad65bcaf8401e6f5ffff81a998cfb8fe5)void [net\_buf\_simple\_push\_be40](group__net__buf.md#gad65bcaf8401e6f5ffff81a998cfb8fe5)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

669

[ 679](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e)void [net\_buf\_simple\_push\_le48](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

680

[ 690](group__net__buf.md#ga1ea39c7d7e9ba4e10d31d818e45e192a)void [net\_buf\_simple\_push\_be48](group__net__buf.md#ga1ea39c7d7e9ba4e10d31d818e45e192a)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

691

[ 701](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85)void [net\_buf\_simple\_push\_le64](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

702

[ 712](group__net__buf.md#gafea2201655955ab004b5f77106998ae9)void [net\_buf\_simple\_push\_be64](group__net__buf.md#gafea2201655955ab004b5f77106998ae9)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val);

713

[ 725](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8)void \*[net\_buf\_simple\_pull](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

726

[ 738](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c)void \*[net\_buf\_simple\_pull\_mem](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t len);

739

[ 750](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_buf\_simple\_pull\_u8](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

751

[ 762](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_pull\_le16](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

763

[ 774](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_pull\_be16](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

775

[ 786](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_pull\_le24](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

787

[ 798](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_pull\_be24](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

799

[ 810](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_pull\_le32](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

811

[ 822](group__net__buf.md#ga1a53892ed75f994bbbb3a2bcf1743d3c)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_simple\_pull\_be32](group__net__buf.md#ga1a53892ed75f994bbbb3a2bcf1743d3c)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

823

[ 834](group__net__buf.md#gad669c07efe5cb90ebffcc76d9c1029a1)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_le40](group__net__buf.md#gad669c07efe5cb90ebffcc76d9c1029a1)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

835

[ 846](group__net__buf.md#gaa665830dad59ac957f79c7f1cc84aed5)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_be40](group__net__buf.md#gaa665830dad59ac957f79c7f1cc84aed5)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

847

[ 858](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_le48](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

859

[ 870](group__net__buf.md#ga19bdefe740fe94a42fba76d71b4ef6e2)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_be48](group__net__buf.md#ga19bdefe740fe94a42fba76d71b4ef6e2)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

871

[ 882](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_le64](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

883

[ 894](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_simple\_pull\_be64](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

895

[ 905](group__net__buf.md#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[net\_buf\_simple\_tail](group__net__buf.md#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)(const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf)

906{

907 return buf->[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) + buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3);

908}

909

[ 919](group__net__buf.md#gaafcb52db2daf1c4451a600e7b647e55c)size\_t [net\_buf\_simple\_headroom](group__net__buf.md#gaafcb52db2daf1c4451a600e7b647e55c)(const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

920

[ 930](group__net__buf.md#ga23e85f8f681fd7617032b4ca40dc62c5)size\_t [net\_buf\_simple\_tailroom](group__net__buf.md#ga23e85f8f681fd7617032b4ca40dc62c5)(const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

931

[ 941](group__net__buf.md#gabfe255688a80c0abea866762ff4c5a6c)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_simple\_max\_len](group__net__buf.md#gabfe255688a80c0abea866762ff4c5a6c)(const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

942

[ 950](structnet__buf__simple__state.md)struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) {

[ 952](structnet__buf__simple__state.md#a4061f8e50e14289b1ec999ef490c8fbf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [offset](structnet__buf__simple__state.md#a4061f8e50e14289b1ec999ef490c8fbf);

[ 954](structnet__buf__simple__state.md#af0e544fe2b018a7ff0b30970e9de8253) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structnet__buf__simple__state.md#af0e544fe2b018a7ff0b30970e9de8253);

955};

956

[ 965](group__net__buf.md#gabf5b098aa0926d9b7fb88baff8a3e2d8)static inline void [net\_buf\_simple\_save](group__net__buf.md#gabf5b098aa0926d9b7fb88baff8a3e2d8)(const struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

966 struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

967{

968 [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->offset = ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))[net\_buf\_simple\_headroom](group__net__buf.md#gaafcb52db2daf1c4451a600e7b647e55c)(buf);

969 [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->len = buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3);

970}

971

[ 981](group__net__buf.md#gaedd36481657a7a9d108659d56e131721)static inline void [net\_buf\_simple\_restore](group__net__buf.md#gaedd36481657a7a9d108659d56e131721)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

982 struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

983{

984 buf->[data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1) = buf->\_\_buf + [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->offset;

985 buf->[len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3) = [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)->len;

986}

987

[ 997](group__net__buf.md#gaaeacbdf3cfda12691c75253015e5c19a)#define NET\_BUF\_EXTERNAL\_DATA BIT(0)

998

[ 1006](structnet__buf.md)struct [net\_buf](structnet__buf.md) {

[ 1008](structnet__buf.md#a5cc70f57e5b776cfa12b2d556e5958f3) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__buf.md#a5cc70f57e5b776cfa12b2d556e5958f3);

1009

[ 1011](structnet__buf.md#a1fa032cc23854c35eae013020823fa88) struct [net\_buf](structnet__buf.md) \*[frags](structnet__buf.md#a1fa032cc23854c35eae013020823fa88);

1012

[ 1014](structnet__buf.md#a42da518a82f4c37c45814b4f8c5f2731) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ref](structnet__buf.md#a42da518a82f4c37c45814b4f8c5f2731);

1015

[ 1017](structnet__buf.md#aa4fcce2e2894fc5dbd9cc74fc020647e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structnet__buf.md#aa4fcce2e2894fc5dbd9cc74fc020647e);

1018

[ 1020](structnet__buf.md#a45f294bac054d64034bddcc4c6574d29) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pool\_id](structnet__buf.md#a45f294bac054d64034bddcc4c6574d29);

1021

[ 1023](structnet__buf.md#a65db7bed62d7211114767e6ce58dad75) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [user\_data\_size](structnet__buf.md#a65db7bed62d7211114767e6ce58dad75);

1024

1028 union {

1029 /\* The ABI of this struct must match net\_buf\_simple \*/

1030 struct {

[ 1032](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1033

[ 1035](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38);

1036

[ 1038](structnet__buf.md#a1522d81a002804223e25300a6961f527) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [size](structnet__buf.md#a1522d81a002804223e25300a6961f527);

1039

1044 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\_\_buf;

1045 };

1046

1048 struct [net\_buf\_simple](structnet__buf__simple.md) b;

1050 };

1051

[ 1053](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7)[] \_\_net\_buf\_align;

1054};

1055

1057

1058struct net\_buf\_data\_cb {

1059 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* \_\_must\_check (\*alloc)(struct [net\_buf](structnet__buf.md) \*buf, size\_t \*size,

1060 [k\_timeout\_t](structk__timeout__t.md) timeout);

1061 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* \_\_must\_check (\*ref)(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

1062 void (\*unref)(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data);

1063};

1064

1065struct net\_buf\_data\_alloc {

1066 const struct net\_buf\_data\_cb \*cb;

1067 void \*alloc\_data;

1068 size\_t max\_alloc\_size;

1069};

1070

1072

[ 1078](structnet__buf__pool.md)struct [net\_buf\_pool](structnet__buf__pool.md) {

[ 1080](structnet__buf__pool.md#a97e5b2e51238e859f93882a8008ba305) struct [k\_lifo](structk__lifo.md) [free](structnet__buf__pool.md#a97e5b2e51238e859f93882a8008ba305);

1081

[ 1083](structnet__buf__pool.md#ae92fc3f3f51be63ccdeee9614d21cc34) struct [k\_spinlock](structk__spinlock.md) [lock](structnet__buf__pool.md#ae92fc3f3f51be63ccdeee9614d21cc34);

1084

[ 1086](structnet__buf__pool.md#a55b57f4f573c7e752c3ccf2f92f25626) const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buf\_count](structnet__buf__pool.md#a55b57f4f573c7e752c3ccf2f92f25626);

1087

[ 1089](structnet__buf__pool.md#a3fdf83b4c0b5acefbb761da285791ad2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [uninit\_count](structnet__buf__pool.md#a3fdf83b4c0b5acefbb761da285791ad2);

1090

[ 1092](structnet__buf__pool.md#a4718ecec19d7e2ccaf04b6ff61120975) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [user\_data\_size](structnet__buf__pool.md#a4718ecec19d7e2ccaf04b6ff61120975);

1093

1094#if defined(CONFIG\_NET\_BUF\_POOL\_USAGE)

1096 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) avail\_count;

1097

1099 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pool\_size;

1100

1102 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_used;

1103

1105 const char \*name;

1106#endif /\* CONFIG\_NET\_BUF\_POOL\_USAGE \*/

1107

[ 1109](structnet__buf__pool.md#a2a9141d7cd20cd98818a92dc5bc99f56) void (\*const [destroy](structnet__buf__pool.md#a2a9141d7cd20cd98818a92dc5bc99f56))(struct [net\_buf](structnet__buf.md) \*buf);

1110

[ 1112](structnet__buf__pool.md#a617bd8f77e55481d97183da8c0c62cc5) const struct net\_buf\_data\_alloc \*[alloc](structnet__buf__pool.md#a617bd8f77e55481d97183da8c0c62cc5);

1113

1115 struct [net\_buf](structnet__buf.md) \* const \_\_bufs;

1116};

1117

1119#define NET\_BUF\_POOL\_USAGE\_INIT(\_pool, \_count) \

1120 IF\_ENABLED(CONFIG\_NET\_BUF\_POOL\_USAGE, (.avail\_count = ATOMIC\_INIT(\_count),)) \

1121 IF\_ENABLED(CONFIG\_NET\_BUF\_POOL\_USAGE, (.max\_used = 0,)) \

1122 IF\_ENABLED(CONFIG\_NET\_BUF\_POOL\_USAGE, (.name = STRINGIFY(\_pool),))

1123

1124#define NET\_BUF\_POOL\_INITIALIZER(\_pool, \_alloc, \_bufs, \_count, \_ud\_size, \_destroy) \

1125 { \

1126 .free = Z\_LIFO\_INITIALIZER(\_pool.free), \

1127 .lock = { }, \

1128 .buf\_count = \_count, \

1129 .uninit\_count = \_count, \

1130 .user\_data\_size = \_ud\_size, \

1131 NET\_BUF\_POOL\_USAGE\_INIT(\_pool, \_count) \

1132 .destroy = \_destroy, \

1133 .alloc = \_alloc, \

1134 .\_\_bufs = (struct net\_buf \*)\_bufs, \

1135 }

1136

1137#define \_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size) \

1138 struct \_net\_buf\_##\_name { uint8\_t b[sizeof(struct net\_buf)]; \

1139 uint8\_t ud[\_ud\_size]; } \_\_net\_buf\_align; \

1140 BUILD\_ASSERT(\_ud\_size <= UINT8\_MAX); \

1141 BUILD\_ASSERT(offsetof(struct net\_buf, user\_data) == \

1142 offsetof(struct \_net\_buf\_##\_name, ud), "Invalid offset"); \

1143 BUILD\_ASSERT(\_\_alignof\_\_(struct net\_buf) == \

1144 \_\_alignof\_\_(struct \_net\_buf\_##\_name), "Invalid alignment"); \

1145 BUILD\_ASSERT(sizeof(struct \_net\_buf\_##\_name) == \

1146 ROUND\_UP(sizeof(struct net\_buf) + \_ud\_size, \_\_alignof\_\_(struct net\_buf)), \

1147 "Size cannot be determined"); \

1148 static struct \_net\_buf\_##\_name \_net\_buf\_##\_name[\_count] \_\_noinit

1149

1150extern const struct net\_buf\_data\_alloc net\_buf\_heap\_alloc;

1152

[ 1180](group__net__buf.md#ga61671ac866081d31dfe9eddbf3b6f210)#define NET\_BUF\_POOL\_HEAP\_DEFINE(\_name, \_count, \_ud\_size, \_destroy) \

1181 \_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

1182 static STRUCT\_SECTION\_ITERABLE(net\_buf\_pool, \_name) = \

1183 NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_heap\_alloc, \

1184 \_net\_buf\_##\_name, \_count, \_ud\_size, \

1185 \_destroy)

1186

1188

1189struct net\_buf\_pool\_fixed {

1190 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_pool;

1191};

1192

1193extern const struct net\_buf\_data\_cb net\_buf\_fixed\_cb;

1194

1196

[ 1225](group__net__buf.md#gacc53824e01db7935bcc9cad564b716cd)#define NET\_BUF\_POOL\_FIXED\_DEFINE(\_name, \_count, \_data\_size, \_ud\_size, \_destroy) \

1226 \_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

1227 static uint8\_t \_\_noinit net\_buf\_data\_##\_name[\_count][\_data\_size] \_\_net\_buf\_align; \

1228 static const struct net\_buf\_pool\_fixed net\_buf\_fixed\_##\_name = { \

1229 .data\_pool = (uint8\_t \*)net\_buf\_data\_##\_name, \

1230 }; \

1231 static const struct net\_buf\_data\_alloc net\_buf\_fixed\_alloc\_##\_name = { \

1232 .cb = &net\_buf\_fixed\_cb, \

1233 .alloc\_data = (void \*)&net\_buf\_fixed\_##\_name, \

1234 .max\_alloc\_size = \_data\_size, \

1235 }; \

1236 static STRUCT\_SECTION\_ITERABLE(net\_buf\_pool, \_name) = \

1237 NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_fixed\_alloc\_##\_name, \

1238 \_net\_buf\_##\_name, \_count, \_ud\_size, \

1239 \_destroy)

1240

1242extern const struct net\_buf\_data\_cb net\_buf\_var\_cb;

1244

[ 1269](group__net__buf.md#ga90e691e793c964847d737f5ecf7646ec)#define NET\_BUF\_POOL\_VAR\_DEFINE(\_name, \_count, \_data\_size, \_ud\_size, \_destroy) \

1270 \_NET\_BUF\_ARRAY\_DEFINE(\_name, \_count, \_ud\_size); \

1271 K\_HEAP\_DEFINE(net\_buf\_mem\_pool\_##\_name, \_data\_size); \

1272 static const struct net\_buf\_data\_alloc net\_buf\_data\_alloc\_##\_name = { \

1273 .cb = &net\_buf\_var\_cb, \

1274 .alloc\_data = &net\_buf\_mem\_pool\_##\_name, \

1275 .max\_alloc\_size = 0, \

1276 }; \

1277 static STRUCT\_SECTION\_ITERABLE(net\_buf\_pool, \_name) = \

1278 NET\_BUF\_POOL\_INITIALIZER(\_name, &net\_buf\_data\_alloc\_##\_name, \

1279 \_net\_buf\_##\_name, \_count, \_ud\_size, \

1280 \_destroy)

1281

[ 1303](group__net__buf.md#ga810aba8ba321fd012edc238ea9fe19dc)#define NET\_BUF\_POOL\_DEFINE(\_name, \_count, \_size, \_ud\_size, \_destroy) \

1304 NET\_BUF\_POOL\_FIXED\_DEFINE(\_name, \_count, \_size, \_ud\_size, \_destroy)

1305

[ 1313](group__net__buf.md#ga145f4b2de7548814eaa7ba86fb123989)struct [net\_buf\_pool](structnet__buf__pool.md) \*[net\_buf\_pool\_get](group__net__buf.md#ga145f4b2de7548814eaa7ba86fb123989)(int id);

1314

[ 1327](group__net__buf.md#gacdf048dc0afc7ef67027117e0d51d3a3)int [net\_buf\_id](group__net__buf.md#gacdf048dc0afc7ef67027117e0d51d3a3)(const struct [net\_buf](structnet__buf.md) \*buf);

1328

1343#if defined(CONFIG\_NET\_BUF\_LOG)

1344struct [net\_buf](structnet__buf.md) \* \_\_must\_check net\_buf\_alloc\_fixed\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1345 [k\_timeout\_t](structk__timeout__t.md) timeout,

1346 const char \*func,

1347 int line);

1348#define net\_buf\_alloc\_fixed(\_pool, \_timeout) \

1349 net\_buf\_alloc\_fixed\_debug(\_pool, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1350#else

[ 1351](group__net__buf.md#ga686df794ec6881625b54454a33587bab)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_alloc\_fixed](group__net__buf.md#ga686df794ec6881625b54454a33587bab)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1352 [k\_timeout\_t](structk__timeout__t.md) timeout);

1353#endif

1354

[ 1358](group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005)static inline struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_alloc](group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1359 [k\_timeout\_t](structk__timeout__t.md) timeout)

1360{

1361 return [net\_buf\_alloc\_fixed](group__net__buf.md#ga686df794ec6881625b54454a33587bab)(pool, timeout);

1362}

1363

1379#if defined(CONFIG\_NET\_BUF\_LOG)

1380struct [net\_buf](structnet__buf.md) \* \_\_must\_check net\_buf\_alloc\_len\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1381 size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527),

1382 [k\_timeout\_t](structk__timeout__t.md) timeout,

1383 const char \*func,

1384 int line);

1385#define net\_buf\_alloc\_len(\_pool, \_size, \_timeout) \

1386 net\_buf\_alloc\_len\_debug(\_pool, \_size, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1387#else

[ 1388](group__net__buf.md#ga11d489aedcca82117965fa6ba9d11ca5)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_alloc\_len](group__net__buf.md#ga11d489aedcca82117965fa6ba9d11ca5)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1389 size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527),

1390 [k\_timeout\_t](structk__timeout__t.md) timeout);

1391#endif

1392

1412#if defined(CONFIG\_NET\_BUF\_LOG)

1413struct [net\_buf](structnet__buf.md) \* \_\_must\_check net\_buf\_alloc\_with\_data\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1414 void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527),

1415 [k\_timeout\_t](structk__timeout__t.md) timeout,

1416 const char \*func, int line);

1417#define net\_buf\_alloc\_with\_data(\_pool, \_data\_, \_size, \_timeout) \

1418 net\_buf\_alloc\_with\_data\_debug(\_pool, \_data\_, \_size, \_timeout, \

1419 \_\_func\_\_, \_\_LINE\_\_)

1420#else

[ 1421](group__net__buf.md#ga8c24d0761d6d38facb6cca60c7c13c0c)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_alloc\_with\_data](group__net__buf.md#ga8c24d0761d6d38facb6cca60c7c13c0c)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1422 void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527),

1423 [k\_timeout\_t](structk__timeout__t.md) timeout);

1424#endif

1425

1438#if defined(CONFIG\_NET\_BUF\_LOG)

1439\_\_deprecated struct [net\_buf](structnet__buf.md) \* \_\_must\_check net\_buf\_get\_debug(struct [k\_fifo](structk__fifo.md) \*fifo,

1440 [k\_timeout\_t](structk__timeout__t.md) timeout,

1441 const char \*func, int line);

1442#define net\_buf\_get(\_fifo, \_timeout) \

1443 net\_buf\_get\_debug(\_fifo, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1444#else

[ 1445](group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742)\_\_deprecated struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_get](group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742)(struct [k\_fifo](structk__fifo.md) \*fifo,

1446 [k\_timeout\_t](structk__timeout__t.md) timeout);

1447#endif

1448

[ 1458](group__net__buf.md#ga739249547eb37b839b3c1ebdbcb88d28)static inline void [net\_buf\_destroy](group__net__buf.md#ga739249547eb37b839b3c1ebdbcb88d28)(struct [net\_buf](structnet__buf.md) \*buf)

1459{

1460 struct [net\_buf\_pool](structnet__buf__pool.md) \*pool = [net\_buf\_pool\_get](group__net__buf.md#ga145f4b2de7548814eaa7ba86fb123989)(buf->[pool\_id](structnet__buf.md#a45f294bac054d64034bddcc4c6574d29));

1461

1462 if (buf->\_\_buf) {

1463 if (!(buf->[flags](structnet__buf.md#aa4fcce2e2894fc5dbd9cc74fc020647e) & [NET\_BUF\_EXTERNAL\_DATA](group__net__buf.md#gaaeacbdf3cfda12691c75253015e5c19a))) {

1464 pool->[alloc](structnet__buf__pool.md#a617bd8f77e55481d97183da8c0c62cc5)->cb->unref(buf, buf->\_\_buf);

1465 }

1466 buf->\_\_buf = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1467 }

1468

1469 [k\_lifo\_put](group__lifo__apis.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)(&pool->[free](structnet__buf__pool.md#a97e5b2e51238e859f93882a8008ba305), buf);

1470}

1471

[ 1479](group__net__buf.md#ga1292f38b096fd80e31889aff44b0c021)void [net\_buf\_reset](group__net__buf.md#ga1292f38b096fd80e31889aff44b0c021)(struct [net\_buf](structnet__buf.md) \*buf);

1480

[ 1489](group__net__buf.md#ga0e5d3d938becfefc4f4b4d083cb467aa)void [net\_buf\_simple\_reserve](group__net__buf.md#ga0e5d3d938becfefc4f4b4d083cb467aa)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, size\_t reserve);

1490

[ 1497](group__net__buf.md#ga6d2dfc45e1e5acf21fe08359a4f92a18)void [net\_buf\_slist\_put](group__net__buf.md#ga6d2dfc45e1e5acf21fe08359a4f92a18)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, struct [net\_buf](structnet__buf.md) \*buf);

1498

[ 1506](group__net__buf.md#ga218d4a0c160c57a44946154478724cb3)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_slist\_get](group__net__buf.md#ga218d4a0c160c57a44946154478724cb3)([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list);

1507

[ 1516](group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047)\_\_deprecated void [net\_buf\_put](group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047)(struct [k\_fifo](structk__fifo.md) \*fifo, struct [net\_buf](structnet__buf.md) \*buf);

1517

1525#if defined(CONFIG\_NET\_BUF\_LOG)

1526void net\_buf\_unref\_debug(struct [net\_buf](structnet__buf.md) \*buf, const char \*func, int line);

1527#define net\_buf\_unref(\_buf) \

1528 net\_buf\_unref\_debug(\_buf, \_\_func\_\_, \_\_LINE\_\_)

1529#else

[ 1530](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273)void [net\_buf\_unref](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273)(struct [net\_buf](structnet__buf.md) \*buf);

1531#endif

1532

[ 1540](group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_ref](group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f)(struct [net\_buf](structnet__buf.md) \*buf);

1541

[ 1555](group__net__buf.md#gaf4d80e2878e3c790fff206bec820f03f)struct [net\_buf](structnet__buf.md) \* \_\_must\_check [net\_buf\_clone](group__net__buf.md#gaf4d80e2878e3c790fff206bec820f03f)(struct [net\_buf](structnet__buf.md) \*buf,

1556 [k\_timeout\_t](structk__timeout__t.md) timeout);

1557

[ 1565](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)static inline void \* \_\_must\_check [net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)(const struct [net\_buf](structnet__buf.md) \*buf)

1566{

1567 return (void \*)buf->[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7);

1568}

1569

[ 1579](group__net__buf.md#ga4d1dd56ca8d32d3cfda114fd36761d0d)int [net\_buf\_user\_data\_copy](group__net__buf.md#ga4d1dd56ca8d32d3cfda114fd36761d0d)(struct [net\_buf](structnet__buf.md) \*dst, const struct [net\_buf](structnet__buf.md) \*src);

1580

[ 1589](group__net__buf.md#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)static inline void [net\_buf\_reserve](group__net__buf.md#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)(struct [net\_buf](structnet__buf.md) \*buf, size\_t reserve)

1590{

1591 [net\_buf\_simple\_reserve](group__net__buf.md#ga0e5d3d938becfefc4f4b4d083cb467aa)(&buf->b, reserve);

1592}

1593

[ 1605](group__net__buf.md#ga30776d2b21f06d244c083af5c25b0f3e)static inline void \*[net\_buf\_add](group__net__buf.md#ga30776d2b21f06d244c083af5c25b0f3e)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

1606{

1607 return [net\_buf\_simple\_add](group__net__buf.md#ga1906e637c848948f5780428a99b3341e)(&buf->b, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

1608}

1609

[ 1622](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f)static inline void \*[net\_buf\_add\_mem](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f)(struct [net\_buf](structnet__buf.md) \*buf, const void \*mem,

1623 size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

1624{

1625 return [net\_buf\_simple\_add\_mem](group__net__buf.md#gac37209c1e5097e5610860943fb7d0115)(&buf->b, mem, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

1626}

1627

[ 1639](group__net__buf.md#ga868ac2bea103fed568b461cbcd45eda2)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[net\_buf\_add\_u8](group__net__buf.md#ga868ac2bea103fed568b461cbcd45eda2)(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val)

1640{

1641 return [net\_buf\_simple\_add\_u8](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c)(&buf->b, val);

1642}

1643

[ 1654](group__net__buf.md#gadd6d01a3b1efd0de16f9bef975809404)static inline void [net\_buf\_add\_le16](group__net__buf.md#gadd6d01a3b1efd0de16f9bef975809404)(struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val)

1655{

1656 [net\_buf\_simple\_add\_le16](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5)(&buf->b, val);

1657}

1658

[ 1669](group__net__buf.md#ga61878a9bd7462ca925eac39181f2972c)static inline void [net\_buf\_add\_be16](group__net__buf.md#ga61878a9bd7462ca925eac39181f2972c)(struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val)

1670{

1671 [net\_buf\_simple\_add\_be16](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa)(&buf->b, val);

1672}

1673

[ 1684](group__net__buf.md#ga32b90364091ade229830686f03b25d4c)static inline void [net\_buf\_add\_le24](group__net__buf.md#ga32b90364091ade229830686f03b25d4c)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1685{

1686 [net\_buf\_simple\_add\_le24](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6)(&buf->b, val);

1687}

1688

[ 1699](group__net__buf.md#ga0f3cd9f9b364a2d2125aea19221d3e1e)static inline void [net\_buf\_add\_be24](group__net__buf.md#ga0f3cd9f9b364a2d2125aea19221d3e1e)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1700{

1701 [net\_buf\_simple\_add\_be24](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8)(&buf->b, val);

1702}

1703

[ 1714](group__net__buf.md#gae8ba33b6592ef7fd859b35d63b285d87)static inline void [net\_buf\_add\_le32](group__net__buf.md#gae8ba33b6592ef7fd859b35d63b285d87)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1715{

1716 [net\_buf\_simple\_add\_le32](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56)(&buf->b, val);

1717}

1718

[ 1729](group__net__buf.md#ga5543d00c96f83970f8dbf3670a9dc3fc)static inline void [net\_buf\_add\_be32](group__net__buf.md#ga5543d00c96f83970f8dbf3670a9dc3fc)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1730{

1731 [net\_buf\_simple\_add\_be32](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c)(&buf->b, val);

1732}

1733

[ 1744](group__net__buf.md#ga62790f9644102f4952c250f6513a2ada)static inline void [net\_buf\_add\_le40](group__net__buf.md#ga62790f9644102f4952c250f6513a2ada)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1745{

1746 [net\_buf\_simple\_add\_le40](group__net__buf.md#ga67da71ba5942cc11e95aa5ba02cb8552)(&buf->b, val);

1747}

1748

[ 1759](group__net__buf.md#ga70cb98da91de098a92fbd69712c2bde7)static inline void [net\_buf\_add\_be40](group__net__buf.md#ga70cb98da91de098a92fbd69712c2bde7)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1760{

1761 [net\_buf\_simple\_add\_be40](group__net__buf.md#ga69bdaf4373693bb468cf3876e9edf239)(&buf->b, val);

1762}

1763

[ 1774](group__net__buf.md#gaf19bf75c3d4d645b1eebf9254aa22790)static inline void [net\_buf\_add\_le48](group__net__buf.md#gaf19bf75c3d4d645b1eebf9254aa22790)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1775{

1776 [net\_buf\_simple\_add\_le48](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25)(&buf->b, val);

1777}

1778

[ 1789](group__net__buf.md#ga8fe6feb191ab338e91bd62f44e184deb)static inline void [net\_buf\_add\_be48](group__net__buf.md#ga8fe6feb191ab338e91bd62f44e184deb)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1790{

1791 [net\_buf\_simple\_add\_be48](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171)(&buf->b, val);

1792}

1793

[ 1804](group__net__buf.md#gac3f955f8fecc0e5971d2e5e8176e973e)static inline void [net\_buf\_add\_le64](group__net__buf.md#gac3f955f8fecc0e5971d2e5e8176e973e)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1805{

1806 [net\_buf\_simple\_add\_le64](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011)(&buf->b, val);

1807}

1808

[ 1819](group__net__buf.md#ga055f6eb7d5fbc9a3cf529a9ed00970c4)static inline void [net\_buf\_add\_be64](group__net__buf.md#ga055f6eb7d5fbc9a3cf529a9ed00970c4)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

1820{

1821 [net\_buf\_simple\_add\_be64](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0)(&buf->b, val);

1822}

1823

[ 1834](group__net__buf.md#gace5ad98eac4772db3b0fa2181912f1f0)static inline void \*[net\_buf\_remove\_mem](group__net__buf.md#gace5ad98eac4772db3b0fa2181912f1f0)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

1835{

1836 return [net\_buf\_simple\_remove\_mem](group__net__buf.md#ga8473bdffadc05b22335a321df89f4b83)(&buf->b, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

1837}

1838

[ 1849](group__net__buf.md#gad954b9f37790d5e7087db7db7bdedd41)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_buf\_remove\_u8](group__net__buf.md#gad954b9f37790d5e7087db7db7bdedd41)(struct [net\_buf](structnet__buf.md) \*buf)

1850{

1851 return [net\_buf\_simple\_remove\_u8](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3)(&buf->b);

1852}

1853

[ 1864](group__net__buf.md#gaaf654110fb6a8bdfc27433945d4d1308)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_remove\_le16](group__net__buf.md#gaaf654110fb6a8bdfc27433945d4d1308)(struct [net\_buf](structnet__buf.md) \*buf)

1865{

1866 return [net\_buf\_simple\_remove\_le16](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c)(&buf->b);

1867}

1868

[ 1879](group__net__buf.md#ga5da86c8ea703ab3f01c408cce73b0651)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_remove\_be16](group__net__buf.md#ga5da86c8ea703ab3f01c408cce73b0651)(struct [net\_buf](structnet__buf.md) \*buf)

1880{

1881 return [net\_buf\_simple\_remove\_be16](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee)(&buf->b);

1882}

1883

[ 1894](group__net__buf.md#ga6f346a9af570528d238592851240fd74)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_remove\_be24](group__net__buf.md#ga6f346a9af570528d238592851240fd74)(struct [net\_buf](structnet__buf.md) \*buf)

1895{

1896 return [net\_buf\_simple\_remove\_be24](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd)(&buf->b);

1897}

1898

[ 1909](group__net__buf.md#ga903f59c8dea1b2c54969b567fe315041)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_remove\_le24](group__net__buf.md#ga903f59c8dea1b2c54969b567fe315041)(struct [net\_buf](structnet__buf.md) \*buf)

1910{

1911 return [net\_buf\_simple\_remove\_le24](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5)(&buf->b);

1912}

1913

[ 1924](group__net__buf.md#gae9321a469cc751c58cfb532afd57d265)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_remove\_le32](group__net__buf.md#gae9321a469cc751c58cfb532afd57d265)(struct [net\_buf](structnet__buf.md) \*buf)

1925{

1926 return [net\_buf\_simple\_remove\_le32](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457)(&buf->b);

1927}

1928

[ 1939](group__net__buf.md#gacce707d646d7008ec3167af1a0b20da8)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_remove\_be32](group__net__buf.md#gacce707d646d7008ec3167af1a0b20da8)(struct [net\_buf](structnet__buf.md) \*buf)

1940{

1941 return [net\_buf\_simple\_remove\_be32](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)(&buf->b);

1942}

1943

[ 1954](group__net__buf.md#ga57150a1ba09b28e5c3b04bdefce7ed8e)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_le40](group__net__buf.md#ga57150a1ba09b28e5c3b04bdefce7ed8e)(struct [net\_buf](structnet__buf.md) \*buf)

1955{

1956 return [net\_buf\_simple\_remove\_le40](group__net__buf.md#ga2c937164e648fe8b854cb1144051b6b9)(&buf->b);

1957}

1958

[ 1969](group__net__buf.md#gae2920eab3c56d0d462811b83961df466)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_be40](group__net__buf.md#gae2920eab3c56d0d462811b83961df466)(struct [net\_buf](structnet__buf.md) \*buf)

1970{

1971 return [net\_buf\_simple\_remove\_be40](group__net__buf.md#ga9abd2bccc90cf654556c18322888d131)(&buf->b);

1972}

1973

[ 1984](group__net__buf.md#ga0c147d9f95e2224696a8ace26f63a300)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_le48](group__net__buf.md#ga0c147d9f95e2224696a8ace26f63a300)(struct [net\_buf](structnet__buf.md) \*buf)

1985{

1986 return [net\_buf\_simple\_remove\_le48](group__net__buf.md#gac0628bbbe5d9c2b82766d5a17e767696)(&buf->b);

1987}

1988

[ 1999](group__net__buf.md#gaab0e3bcc21c958c01ef076cd0efe087c)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_be48](group__net__buf.md#gaab0e3bcc21c958c01ef076cd0efe087c)(struct [net\_buf](structnet__buf.md) \*buf)

2000{

2001 return [net\_buf\_simple\_remove\_be48](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb)(&buf->b);

2002}

2003

[ 2014](group__net__buf.md#ga447b9c6be3fe04a50eb35dd29f190b6d)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_le64](group__net__buf.md#ga447b9c6be3fe04a50eb35dd29f190b6d)(struct [net\_buf](structnet__buf.md) \*buf)

2015{

2016 return [net\_buf\_simple\_remove\_le64](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd)(&buf->b);

2017}

2018

[ 2029](group__net__buf.md#ga8b9edd213da2d48dfb8d70a8d307ba13)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_remove\_be64](group__net__buf.md#ga8b9edd213da2d48dfb8d70a8d307ba13)(struct [net\_buf](structnet__buf.md) \*buf)

2030{

2031 return [net\_buf\_simple\_remove\_be64](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932)(&buf->b);

2032}

2033

[ 2045](group__net__buf.md#ga96a2b1f07f3a7958057d9c7cc1f01b73)static inline void \*[net\_buf\_push](group__net__buf.md#ga96a2b1f07f3a7958057d9c7cc1f01b73)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

2046{

2047 return [net\_buf\_simple\_push](group__net__buf.md#ga64df9754665440370340c6dddde625d1)(&buf->b, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2048}

2049

[ 2062](group__net__buf.md#ga7e9daccec8cae1b9bfda52b0758adf0c)static inline void \*[net\_buf\_push\_mem](group__net__buf.md#ga7e9daccec8cae1b9bfda52b0758adf0c)(struct [net\_buf](structnet__buf.md) \*buf, const void \*mem,

2063 size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

2064{

2065 return [net\_buf\_simple\_push\_mem](group__net__buf.md#gaaa838083c610f7426c509efaae69a511)(&buf->b, mem, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2066}

2067

[ 2076](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186)static inline void [net\_buf\_push\_u8](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186)(struct [net\_buf](structnet__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val)

2077{

2078 [net\_buf\_simple\_push\_u8](group__net__buf.md#ga0f19da70bfc8f597680ee02c21226a77)(&buf->b, val);

2079}

2080

[ 2090](group__net__buf.md#gab6c84c6846c06c2b339bc88df35e2655)static inline void [net\_buf\_push\_le16](group__net__buf.md#gab6c84c6846c06c2b339bc88df35e2655)(struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val)

2091{

2092 [net\_buf\_simple\_push\_le16](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6)(&buf->b, val);

2093}

2094

[ 2104](group__net__buf.md#ga6dd756ff8332d076f5d37c69e6c534b5)static inline void [net\_buf\_push\_be16](group__net__buf.md#ga6dd756ff8332d076f5d37c69e6c534b5)(struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val)

2105{

2106 [net\_buf\_simple\_push\_be16](group__net__buf.md#ga827bd85eba0dbd098790d84d22e8e32d)(&buf->b, val);

2107}

2108

[ 2118](group__net__buf.md#ga87524ac50e53ba59c6692af10cf001b9)static inline void [net\_buf\_push\_le24](group__net__buf.md#ga87524ac50e53ba59c6692af10cf001b9)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

2119{

2120 [net\_buf\_simple\_push\_le24](group__net__buf.md#gabe52d6735d835edc361666bb3413b907)(&buf->b, val);

2121}

2122

[ 2132](group__net__buf.md#ga87338399d8ecd64a894908ed4a2f710b)static inline void [net\_buf\_push\_be24](group__net__buf.md#ga87338399d8ecd64a894908ed4a2f710b)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

2133{

2134 [net\_buf\_simple\_push\_be24](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72)(&buf->b, val);

2135}

2136

[ 2146](group__net__buf.md#ga97c9046185d6a1e9235bf6914c72dfc4)static inline void [net\_buf\_push\_le32](group__net__buf.md#ga97c9046185d6a1e9235bf6914c72dfc4)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

2147{

2148 [net\_buf\_simple\_push\_le32](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1)(&buf->b, val);

2149}

2150

[ 2160](group__net__buf.md#gae4e64a23708ed910fb6c3ab8ba481a4c)static inline void [net\_buf\_push\_be32](group__net__buf.md#gae4e64a23708ed910fb6c3ab8ba481a4c)(struct [net\_buf](structnet__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

2161{

2162 [net\_buf\_simple\_push\_be32](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426)(&buf->b, val);

2163}

2164

[ 2174](group__net__buf.md#gaefab4a755cf4fb7d2b4a142a9351c189)static inline void [net\_buf\_push\_le40](group__net__buf.md#gaefab4a755cf4fb7d2b4a142a9351c189)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2175{

2176 [net\_buf\_simple\_push\_le40](group__net__buf.md#ga745ab6f34138b506b42f78e0975a5d2e)(&buf->b, val);

2177}

2178

[ 2188](group__net__buf.md#ga512f84e686ff70a5589557575ccda1f8)static inline void [net\_buf\_push\_be40](group__net__buf.md#ga512f84e686ff70a5589557575ccda1f8)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2189{

2190 [net\_buf\_simple\_push\_be40](group__net__buf.md#gad65bcaf8401e6f5ffff81a998cfb8fe5)(&buf->b, val);

2191}

2192

[ 2202](group__net__buf.md#ga852654f7e59951bf3536e3f4e98761bf)static inline void [net\_buf\_push\_le48](group__net__buf.md#ga852654f7e59951bf3536e3f4e98761bf)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2203{

2204 [net\_buf\_simple\_push\_le48](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e)(&buf->b, val);

2205}

2206

[ 2216](group__net__buf.md#gabfbcb051019ff210cc2b85adcf4bc821)static inline void [net\_buf\_push\_be48](group__net__buf.md#gabfbcb051019ff210cc2b85adcf4bc821)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2217{

2218 [net\_buf\_simple\_push\_be48](group__net__buf.md#ga1ea39c7d7e9ba4e10d31d818e45e192a)(&buf->b, val);

2219}

2220

[ 2230](group__net__buf.md#gad4ee42b023881f80211fbeca53a0f25d)static inline void [net\_buf\_push\_le64](group__net__buf.md#gad4ee42b023881f80211fbeca53a0f25d)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2231{

2232 [net\_buf\_simple\_push\_le64](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85)(&buf->b, val);

2233}

2234

[ 2244](group__net__buf.md#ga43ff5faab0b099a355b9b96b7b0e3d8c)static inline void [net\_buf\_push\_be64](group__net__buf.md#ga43ff5faab0b099a355b9b96b7b0e3d8c)(struct [net\_buf](structnet__buf.md) \*buf, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val)

2245{

2246 [net\_buf\_simple\_push\_be64](group__net__buf.md#gafea2201655955ab004b5f77106998ae9)(&buf->b, val);

2247}

2248

[ 2260](group__net__buf.md#gaef433d92734dd8691c292abdb823ba0e)static inline void \*[net\_buf\_pull](group__net__buf.md#gaef433d92734dd8691c292abdb823ba0e)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

2261{

2262 return [net\_buf\_simple\_pull](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8)(&buf->b, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2263}

2264

[ 2276](group__net__buf.md#gaedc5ffe19bb0ec438e633023c3c5de74)static inline void \*[net\_buf\_pull\_mem](group__net__buf.md#gaedc5ffe19bb0ec438e633023c3c5de74)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

2277{

2278 return [net\_buf\_simple\_pull\_mem](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c)(&buf->b, [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2279}

2280

[ 2291](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)(struct [net\_buf](structnet__buf.md) \*buf)

2292{

2293 return [net\_buf\_simple\_pull\_u8](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7)(&buf->b);

2294}

2295

[ 2306](group__net__buf.md#gaed64e9f2b969f2c0d99cd281e73c860a)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_pull\_le16](group__net__buf.md#gaed64e9f2b969f2c0d99cd281e73c860a)(struct [net\_buf](structnet__buf.md) \*buf)

2307{

2308 return [net\_buf\_simple\_pull\_le16](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba)(&buf->b);

2309}

2310

[ 2321](group__net__buf.md#ga97909a33c374a5c757fd2faf582139b7)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_pull\_be16](group__net__buf.md#ga97909a33c374a5c757fd2faf582139b7)(struct [net\_buf](structnet__buf.md) \*buf)

2322{

2323 return [net\_buf\_simple\_pull\_be16](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440)(&buf->b);

2324}

2325

[ 2336](group__net__buf.md#ga85c505321484a50ed9422f24934ed077)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_pull\_le24](group__net__buf.md#ga85c505321484a50ed9422f24934ed077)(struct [net\_buf](structnet__buf.md) \*buf)

2337{

2338 return [net\_buf\_simple\_pull\_le24](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9)(&buf->b);

2339}

2340

[ 2351](group__net__buf.md#ga8de937e8775879712ea0acbf60327a95)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_pull\_be24](group__net__buf.md#ga8de937e8775879712ea0acbf60327a95)(struct [net\_buf](structnet__buf.md) \*buf)

2352{

2353 return [net\_buf\_simple\_pull\_be24](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1)(&buf->b);

2354}

2355

[ 2366](group__net__buf.md#ga5f051078f1ffcc40e9ad40e7545a084f)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_pull\_le32](group__net__buf.md#ga5f051078f1ffcc40e9ad40e7545a084f)(struct [net\_buf](structnet__buf.md) \*buf)

2367{

2368 return [net\_buf\_simple\_pull\_le32](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353)(&buf->b);

2369}

2370

[ 2381](group__net__buf.md#ga5f8f2e2244eb574b3e57d09d85412967)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [net\_buf\_pull\_be32](group__net__buf.md#ga5f8f2e2244eb574b3e57d09d85412967)(struct [net\_buf](structnet__buf.md) \*buf)

2382{

2383 return [net\_buf\_simple\_pull\_be32](group__net__buf.md#ga1a53892ed75f994bbbb3a2bcf1743d3c)(&buf->b);

2384}

2385

[ 2396](group__net__buf.md#ga36b27c6373eb245f777164065386d100)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_le40](group__net__buf.md#ga36b27c6373eb245f777164065386d100)(struct [net\_buf](structnet__buf.md) \*buf)

2397{

2398 return [net\_buf\_simple\_pull\_le40](group__net__buf.md#gad669c07efe5cb90ebffcc76d9c1029a1)(&buf->b);

2399}

2400

[ 2411](group__net__buf.md#ga050bdaccaec842482a02b096aa0c999f)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_be40](group__net__buf.md#ga050bdaccaec842482a02b096aa0c999f)(struct [net\_buf](structnet__buf.md) \*buf)

2412{

2413 return [net\_buf\_simple\_pull\_be40](group__net__buf.md#gaa665830dad59ac957f79c7f1cc84aed5)(&buf->b);

2414}

2415

[ 2426](group__net__buf.md#ga7eeee45b6639146d1492f92263ee4f51)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_le48](group__net__buf.md#ga7eeee45b6639146d1492f92263ee4f51)(struct [net\_buf](structnet__buf.md) \*buf)

2427{

2428 return [net\_buf\_simple\_pull\_le48](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46)(&buf->b);

2429}

2430

[ 2441](group__net__buf.md#ga68934e105c4b3a8e27aa61b3ec5526db)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_be48](group__net__buf.md#ga68934e105c4b3a8e27aa61b3ec5526db)(struct [net\_buf](structnet__buf.md) \*buf)

2442{

2443 return [net\_buf\_simple\_pull\_be48](group__net__buf.md#ga19bdefe740fe94a42fba76d71b4ef6e2)(&buf->b);

2444}

2445

[ 2456](group__net__buf.md#ga9a3df35e2287cbcfe1b60e2efa52c64e)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_le64](group__net__buf.md#ga9a3df35e2287cbcfe1b60e2efa52c64e)(struct [net\_buf](structnet__buf.md) \*buf)

2457{

2458 return [net\_buf\_simple\_pull\_le64](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e)(&buf->b);

2459}

2460

[ 2471](group__net__buf.md#ga3c1e80741a49691e69e57c891d3edb05)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [net\_buf\_pull\_be64](group__net__buf.md#ga3c1e80741a49691e69e57c891d3edb05)(struct [net\_buf](structnet__buf.md) \*buf)

2472{

2473 return [net\_buf\_simple\_pull\_be64](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712)(&buf->b);

2474}

2475

[ 2485](group__net__buf.md#gaecbc6adf16469e3366c88445ea7a553a)static inline size\_t [net\_buf\_tailroom](group__net__buf.md#gaecbc6adf16469e3366c88445ea7a553a)(const struct [net\_buf](structnet__buf.md) \*buf)

2486{

2487 return [net\_buf\_simple\_tailroom](group__net__buf.md#ga23e85f8f681fd7617032b4ca40dc62c5)(&buf->b);

2488}

2489

[ 2499](group__net__buf.md#gac9a09897f44e708f920064826aa2f703)static inline size\_t [net\_buf\_headroom](group__net__buf.md#gac9a09897f44e708f920064826aa2f703)(const struct [net\_buf](structnet__buf.md) \*buf)

2500{

2501 return [net\_buf\_simple\_headroom](group__net__buf.md#gaafcb52db2daf1c4451a600e7b647e55c)(&buf->b);

2502}

2503

[ 2513](group__net__buf.md#ga65924b8234c91dfc09069ba06242a6b7)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_buf\_max\_len](group__net__buf.md#ga65924b8234c91dfc09069ba06242a6b7)(const struct [net\_buf](structnet__buf.md) \*buf)

2514{

2515 return [net\_buf\_simple\_max\_len](group__net__buf.md#gabfe255688a80c0abea866762ff4c5a6c)(&buf->b);

2516}

2517

[ 2527](group__net__buf.md#gaedb10a84b352a3d7716bef979af2ab31)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[net\_buf\_tail](group__net__buf.md#gaedb10a84b352a3d7716bef979af2ab31)(const struct [net\_buf](structnet__buf.md) \*buf)

2528{

2529 return [net\_buf\_simple\_tail](group__net__buf.md#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)(&buf->b);

2530}

2531

[ 2537](group__net__buf.md#ga042ce3f2e7e3fd0948ca2623fff36746)struct [net\_buf](structnet__buf.md) \*[net\_buf\_frag\_last](group__net__buf.md#ga042ce3f2e7e3fd0948ca2623fff36746)(struct [net\_buf](structnet__buf.md) \*[frags](structnet__buf.md#a1fa032cc23854c35eae013020823fa88));

2538

[ 2550](group__net__buf.md#gac032b44db4a845dba8303fecfe1b63e7)void [net\_buf\_frag\_insert](group__net__buf.md#gac032b44db4a845dba8303fecfe1b63e7)(struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag);

2551

[ 2566](group__net__buf.md#ga0d7e310802a2bc7b2078f9310827535f)struct [net\_buf](structnet__buf.md) \*[net\_buf\_frag\_add](group__net__buf.md#ga0d7e310802a2bc7b2078f9310827535f)(struct [net\_buf](structnet__buf.md) \*head, struct [net\_buf](structnet__buf.md) \*frag);

2567

2577#if defined(CONFIG\_NET\_BUF\_LOG)

2578struct [net\_buf](structnet__buf.md) \*net\_buf\_frag\_del\_debug(struct [net\_buf](structnet__buf.md) \*parent,

2579 struct [net\_buf](structnet__buf.md) \*frag,

2580 const char \*func, int line);

2581#define net\_buf\_frag\_del(\_parent, \_frag) \

2582 net\_buf\_frag\_del\_debug(\_parent, \_frag, \_\_func\_\_, \_\_LINE\_\_)

2583#else

[ 2584](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff)struct [net\_buf](structnet__buf.md) \*[net\_buf\_frag\_del](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff)(struct [net\_buf](structnet__buf.md) \*parent, struct [net\_buf](structnet__buf.md) \*frag);

2585#endif

2586

[ 2602](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065)size\_t [net\_buf\_linearize](group__net__buf.md#gaffd49f2de8e72d5f7585b4e5167923d8)(void \*dst, size\_t dst\_len,

2603 const struct [net\_buf](structnet__buf.md) \*src, size\_t offset, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2604

2619typedef struct [net\_buf](structnet__buf.md) \* \_\_must\_check (\*[net\_buf\_allocator\_cb](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065))([k\_timeout\_t](structk__timeout__t.md) timeout,

2620 void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

2621

[ 2643](group__net__buf.md#ga646d680491753b3ed29fa83c26732d1a)size\_t [net\_buf\_append\_bytes](group__net__buf.md#ga646d680491753b3ed29fa83c26732d1a)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38),

2644 const void \*value, [k\_timeout\_t](structk__timeout__t.md) timeout,

2645 [net\_buf\_allocator\_cb](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065) allocate\_cb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

2646

[ 2661](group__net__buf.md#gaef938c3ab676a5bd5bf8338b8d7cb30c)size\_t [net\_buf\_data\_match](group__net__buf.md#gaef938c3ab676a5bd5bf8338b8d7cb30c)(const struct [net\_buf](structnet__buf.md) \*buf, size\_t offset, const void \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

2662

[ 2678](group__net__buf.md#ga2d7096280d4fa6f5e32c4674d542889b)static inline struct [net\_buf](structnet__buf.md) \*[net\_buf\_skip](group__net__buf.md#ga2d7096280d4fa6f5e32c4674d542889b)(struct [net\_buf](structnet__buf.md) \*buf, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38))

2679{

2680 while (buf && [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)--) {

2681 [net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)(buf);

2682 if (!buf->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)) {

2683 buf = [net\_buf\_frag\_del](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff)([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), buf);

2684 }

2685 }

2686

2687 return buf;

2688}

2689

[ 2700](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)static inline size\_t [net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)(const struct [net\_buf](structnet__buf.md) \*buf)

2701{

2702 size\_t bytes = 0;

2703

2704 while (buf) {

2705 bytes += buf->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38);

2706 buf = buf->[frags](structnet__buf.md#a1fa032cc23854c35eae013020823fa88);

2707 }

2708

2709 return bytes;

2710}

2711

2715

2716#ifdef \_\_cplusplus

2717}

2718#endif

2719

2720#endif /\* ZEPHYR\_INCLUDE\_NET\_BUF\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[k\_lifo\_put](group__lifo__apis.md#gad662e36b1df8b9013e2dc61f9dfe3a8b)

#define k\_lifo\_put(lifo, data)

Add an element to a LIFO queue.

**Definition** kernel.h:2790

[net\_buf\_get](group__net__buf.md#ga014a0e87afc143d06a7eaf6c2f04c742)

struct net\_buf \* net\_buf\_get(struct k\_fifo \*fifo, k\_timeout\_t timeout)

Get a buffer from a FIFO.

[net\_buf\_simple\_clone](group__net__buf.md#ga0186c153b72a379affdd3e2e3994b5a7)

void net\_buf\_simple\_clone(const struct net\_buf\_simple \*original, struct net\_buf\_simple \*clone)

Clone buffer state, using the same data buffer.

[net\_buf\_simple\_init](group__net__buf.md#ga040279b601191367dee013bab9916d8d)

static void net\_buf\_simple\_init(struct net\_buf\_simple \*buf, size\_t reserve\_head)

Initialize a net\_buf\_simple object.

**Definition** net\_buf.h:142

[net\_buf\_frag\_last](group__net__buf.md#ga042ce3f2e7e3fd0948ca2623fff36746)

struct net\_buf \* net\_buf\_frag\_last(struct net\_buf \*frags)

Find the last fragment in the fragment list.

[net\_buf\_pull\_be40](group__net__buf.md#ga050bdaccaec842482a02b096aa0c999f)

static uint64\_t net\_buf\_pull\_be40(struct net\_buf \*buf)

Remove and convert 40 bits from the beginning of the buffer.

**Definition** net\_buf.h:2411

[net\_buf\_add\_be64](group__net__buf.md#ga055f6eb7d5fbc9a3cf529a9ed00970c4)

static void net\_buf\_add\_be64(struct net\_buf \*buf, uint64\_t val)

Add 64-bit value at the end of the buffer.

**Definition** net\_buf.h:1819

[net\_buf\_simple\_pull\_u8](group__net__buf.md#ga09a261c615136fd39834cd301fc692e7)

uint8\_t net\_buf\_simple\_pull\_u8(struct net\_buf\_simple \*buf)

Remove a 8-bit value from the beginning of the buffer.

[net\_buf\_simple\_remove\_le16](group__net__buf.md#ga0b57f9ca2f3837e94cd7862e37efc01c)

uint16\_t net\_buf\_simple\_remove\_le16(struct net\_buf\_simple \*buf)

Remove and convert 16 bits from the end of the buffer.

[net\_buf\_remove\_le48](group__net__buf.md#ga0c147d9f95e2224696a8ace26f63a300)

static uint64\_t net\_buf\_remove\_le48(struct net\_buf \*buf)

Remove and convert 48 bits from the end of the buffer.

**Definition** net\_buf.h:1984

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

**Definition** net\_buf.h:1699

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

[net\_buf\_simple\_tailroom](group__net__buf.md#ga23e85f8f681fd7617032b4ca40dc62c5)

size\_t net\_buf\_simple\_tailroom(const struct net\_buf\_simple \*buf)

Check buffer tailroom.

[net\_buf\_ref](group__net__buf.md#ga29387b2a672bf2bb8739046a46f3601f)

struct net\_buf \* net\_buf\_ref(struct net\_buf \*buf)

Increment the reference count of a buffer.

[net\_buf\_simple\_remove\_le40](group__net__buf.md#ga2c937164e648fe8b854cb1144051b6b9)

uint64\_t net\_buf\_simple\_remove\_le40(struct net\_buf\_simple \*buf)

Remove and convert 40 bits from the end of the buffer.

[net\_buf\_skip](group__net__buf.md#ga2d7096280d4fa6f5e32c4674d542889b)

static struct net\_buf \* net\_buf\_skip(struct net\_buf \*buf, size\_t len)

Skip N number of bytes in a net\_buf.

**Definition** net\_buf.h:2678

[net\_buf\_add](group__net__buf.md#ga30776d2b21f06d244c083af5c25b0f3e)

static void \* net\_buf\_add(struct net\_buf \*buf, size\_t len)

Prepare data to be added at the end of the buffer.

**Definition** net\_buf.h:1605

[net\_buf\_add\_le24](group__net__buf.md#ga32b90364091ade229830686f03b25d4c)

static void net\_buf\_add\_le24(struct net\_buf \*buf, uint32\_t val)

Add 24-bit value at the end of the buffer.

**Definition** net\_buf.h:1684

[net\_buf\_pull\_le40](group__net__buf.md#ga36b27c6373eb245f777164065386d100)

static uint64\_t net\_buf\_pull\_le40(struct net\_buf \*buf)

Remove and convert 40 bits from the beginning of the buffer.

**Definition** net\_buf.h:2396

[net\_buf\_simple\_pull\_le32](group__net__buf.md#ga38df82e6ba9bc2c75133200f7fa75353)

uint32\_t net\_buf\_simple\_pull\_le32(struct net\_buf\_simple \*buf)

Remove and convert 32 bits from the beginning of the buffer.

[net\_buf\_simple\_add\_le32](group__net__buf.md#ga3bf1bcff840dddd721f2c49ef0ed7c56)

void net\_buf\_simple\_add\_le32(struct net\_buf\_simple \*buf, uint32\_t val)

Add 32-bit value at the end of the buffer.

[net\_buf\_pull\_be64](group__net__buf.md#ga3c1e80741a49691e69e57c891d3edb05)

static uint64\_t net\_buf\_pull\_be64(struct net\_buf \*buf)

Remove and convert 64 bits from the beginning of the buffer.

**Definition** net\_buf.h:2471

[net\_buf\_push\_be64](group__net__buf.md#ga43ff5faab0b099a355b9b96b7b0e3d8c)

static void net\_buf\_push\_be64(struct net\_buf \*buf, uint64\_t val)

Push 64-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2244

[net\_buf\_remove\_le64](group__net__buf.md#ga447b9c6be3fe04a50eb35dd29f190b6d)

static uint64\_t net\_buf\_remove\_le64(struct net\_buf \*buf)

Remove and convert 64 bits from the end of the buffer.

**Definition** net\_buf.h:2014

[net\_buf\_simple\_reset](group__net__buf.md#ga4b537e913e132448cbf56976504ddddd)

static void net\_buf\_simple\_reset(struct net\_buf\_simple \*buf)

Reset buffer.

**Definition** net\_buf.h:172

[net\_buf\_simple\_pull\_be24](group__net__buf.md#ga4c24d445d6b75c850a9e95fb242a50e1)

uint32\_t net\_buf\_simple\_pull\_be24(struct net\_buf\_simple \*buf)

Remove and convert 24 bits from the beginning of the buffer.

[net\_buf\_simple\_pull\_le24](group__net__buf.md#ga4c9d2ac72a176c49ec224353b5566eb9)

uint32\_t net\_buf\_simple\_pull\_le24(struct net\_buf\_simple \*buf)

Remove and convert 24 bits from the beginning of the buffer.

[net\_buf\_user\_data\_copy](group__net__buf.md#ga4d1dd56ca8d32d3cfda114fd36761d0d)

int net\_buf\_user\_data\_copy(struct net\_buf \*dst, const struct net\_buf \*src)

Copy user data from one to another buffer.

[net\_buf\_simple\_remove\_le24](group__net__buf.md#ga4e2fef883228f7de41af3cf90648c3c5)

uint32\_t net\_buf\_simple\_remove\_le24(struct net\_buf\_simple \*buf)

Remove and convert 24 bits from the end of the buffer.

[net\_buf\_simple\_push\_le16](group__net__buf.md#ga50cd64438d8f218e3d1ef8b53b7d41a6)

void net\_buf\_simple\_push\_le16(struct net\_buf\_simple \*buf, uint16\_t val)

Push 16-bit value to the beginning of the buffer.

[net\_buf\_push\_be40](group__net__buf.md#ga512f84e686ff70a5589557575ccda1f8)

static void net\_buf\_push\_be40(struct net\_buf \*buf, uint64\_t val)

Push 40-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2188

[net\_buf\_alloc](group__net__buf.md#ga534366f3b5c7f41a28372c12149ca005)

static struct net\_buf \* net\_buf\_alloc(struct net\_buf\_pool \*pool, k\_timeout\_t timeout)

**Definition** net\_buf.h:1358

[net\_buf\_add\_be32](group__net__buf.md#ga5543d00c96f83970f8dbf3670a9dc3fc)

static void net\_buf\_add\_be32(struct net\_buf \*buf, uint32\_t val)

Add 32-bit value at the end of the buffer.

**Definition** net\_buf.h:1729

[net\_buf\_simple\_remove\_le64](group__net__buf.md#ga560bd7b181c7f08599ae9241b6ce99fd)

uint64\_t net\_buf\_simple\_remove\_le64(struct net\_buf\_simple \*buf)

Remove and convert 64 bits from the end of the buffer.

[net\_buf\_remove\_le40](group__net__buf.md#ga57150a1ba09b28e5c3b04bdefce7ed8e)

static uint64\_t net\_buf\_remove\_le40(struct net\_buf \*buf)

Remove and convert 40 bits from the end of the buffer.

**Definition** net\_buf.h:1954

[net\_buf\_simple\_add\_le48](group__net__buf.md#ga5be8c9f33df5b31c15df193a7116ce25)

void net\_buf\_simple\_add\_le48(struct net\_buf\_simple \*buf, uint64\_t val)

Add 48-bit value at the end of the buffer.

[net\_buf\_remove\_be16](group__net__buf.md#ga5da86c8ea703ab3f01c408cce73b0651)

static uint16\_t net\_buf\_remove\_be16(struct net\_buf \*buf)

Remove and convert 16 bits from the end of the buffer.

**Definition** net\_buf.h:1879

[net\_buf\_simple\_add\_be24](group__net__buf.md#ga5eb09afeff062af577094d2d3f5fdec8)

void net\_buf\_simple\_add\_be24(struct net\_buf\_simple \*buf, uint32\_t val)

Add 24-bit value at the end of the buffer.

[net\_buf\_pull\_le32](group__net__buf.md#ga5f051078f1ffcc40e9ad40e7545a084f)

static uint32\_t net\_buf\_pull\_le32(struct net\_buf \*buf)

Remove and convert 32 bits from the beginning of the buffer.

**Definition** net\_buf.h:2366

[net\_buf\_pull\_be32](group__net__buf.md#ga5f8f2e2244eb574b3e57d09d85412967)

static uint32\_t net\_buf\_pull\_be32(struct net\_buf \*buf)

Remove and convert 32 bits from the beginning of the buffer.

**Definition** net\_buf.h:2381

[net\_buf\_frag\_del](group__net__buf.md#ga602a99833bd401a0ada5bd5defa7a2ff)

struct net\_buf \* net\_buf\_frag\_del(struct net\_buf \*parent, struct net\_buf \*frag)

Delete existing fragment from a chain of bufs.

[net\_buf\_simple\_remove\_be64](group__net__buf.md#ga602fae83e2ecf47552a11f9282619932)

uint64\_t net\_buf\_simple\_remove\_be64(struct net\_buf\_simple \*buf)

Remove and convert 64 bits from the end of the buffer.

[net\_buf\_add\_be16](group__net__buf.md#ga61878a9bd7462ca925eac39181f2972c)

static void net\_buf\_add\_be16(struct net\_buf \*buf, uint16\_t val)

Add 16-bit value at the end of the buffer.

**Definition** net\_buf.h:1669

[net\_buf\_add\_le40](group__net__buf.md#ga62790f9644102f4952c250f6513a2ada)

static void net\_buf\_add\_le40(struct net\_buf \*buf, uint64\_t val)

Add 40-bit value at the end of the buffer.

**Definition** net\_buf.h:1744

[net\_buf\_append\_bytes](group__net__buf.md#ga646d680491753b3ed29fa83c26732d1a)

size\_t net\_buf\_append\_bytes(struct net\_buf \*buf, size\_t len, const void \*value, k\_timeout\_t timeout, net\_buf\_allocator\_cb allocate\_cb, void \*user\_data)

Append data to a list of net\_buf.

[net\_buf\_simple\_push](group__net__buf.md#ga64df9754665440370340c6dddde625d1)

void \* net\_buf\_simple\_push(struct net\_buf\_simple \*buf, size\_t len)

Prepare data to be added to the start of the buffer.

[net\_buf\_max\_len](group__net__buf.md#ga65924b8234c91dfc09069ba06242a6b7)

static uint16\_t net\_buf\_max\_len(const struct net\_buf \*buf)

Check maximum net\_buf::len value.

**Definition** net\_buf.h:2513

[net\_buf\_simple\_push\_le48](group__net__buf.md#ga66b44897e336f31e3ecbf4717bec274e)

void net\_buf\_simple\_push\_le48(struct net\_buf\_simple \*buf, uint64\_t val)

Push 48-bit value to the beginning of the buffer.

[net\_buf\_simple\_add\_le40](group__net__buf.md#ga67da71ba5942cc11e95aa5ba02cb8552)

void net\_buf\_simple\_add\_le40(struct net\_buf\_simple \*buf, uint64\_t val)

Add 40-bit value at the end of the buffer.

[net\_buf\_alloc\_fixed](group__net__buf.md#ga686df794ec6881625b54454a33587bab)

struct net\_buf \* net\_buf\_alloc\_fixed(struct net\_buf\_pool \*pool, k\_timeout\_t timeout)

Allocate a new fixed buffer from a pool.

[net\_buf\_pull\_be48](group__net__buf.md#ga68934e105c4b3a8e27aa61b3ec5526db)

static uint64\_t net\_buf\_pull\_be48(struct net\_buf \*buf)

Remove and convert 48 bits from the beginning of the buffer.

**Definition** net\_buf.h:2441

[net\_buf\_simple\_add\_be40](group__net__buf.md#ga69bdaf4373693bb468cf3876e9edf239)

void net\_buf\_simple\_add\_be40(struct net\_buf\_simple \*buf, uint64\_t val)

Add 40-bit value at the end of the buffer.

[net\_buf\_simple\_pull\_le48](group__net__buf.md#ga69fbfbd72b17783c5ee12b4b2ac9af46)

uint64\_t net\_buf\_simple\_pull\_le48(struct net\_buf\_simple \*buf)

Remove and convert 48 bits from the beginning of the buffer.

[net\_buf\_slist\_put](group__net__buf.md#ga6d2dfc45e1e5acf21fe08359a4f92a18)

void net\_buf\_slist\_put(sys\_slist\_t \*list, struct net\_buf \*buf)

Put a buffer into a list.

[net\_buf\_push\_be16](group__net__buf.md#ga6dd756ff8332d076f5d37c69e6c534b5)

static void net\_buf\_push\_be16(struct net\_buf \*buf, uint16\_t val)

Push 16-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2104

[net\_buf\_remove\_be24](group__net__buf.md#ga6f346a9af570528d238592851240fd74)

static uint32\_t net\_buf\_remove\_be24(struct net\_buf \*buf)

Remove and convert 24 bits from the end of the buffer.

**Definition** net\_buf.h:1894

[net\_buf\_add\_be40](group__net__buf.md#ga70cb98da91de098a92fbd69712c2bde7)

static void net\_buf\_add\_be40(struct net\_buf \*buf, uint64\_t val)

Add 40-bit value at the end of the buffer.

**Definition** net\_buf.h:1759

[net\_buf\_pull\_u8](group__net__buf.md#ga71bb306d2ce459a60a8c3fc6dac54c90)

static uint8\_t net\_buf\_pull\_u8(struct net\_buf \*buf)

Remove a 8-bit value from the beginning of the buffer.

**Definition** net\_buf.h:2291

[net\_buf\_destroy](group__net__buf.md#ga739249547eb37b839b3c1ebdbcb88d28)

static void net\_buf\_destroy(struct net\_buf \*buf)

Destroy buffer from custom destroy callback.

**Definition** net\_buf.h:1458

[net\_buf\_simple\_push\_le40](group__net__buf.md#ga745ab6f34138b506b42f78e0975a5d2e)

void net\_buf\_simple\_push\_le40(struct net\_buf\_simple \*buf, uint64\_t val)

Push 40-bit value to the beginning of the buffer.

[net\_buf\_simple\_push\_le64](group__net__buf.md#ga771634e50e2bf7c291565ce6b2af7e85)

void net\_buf\_simple\_push\_le64(struct net\_buf\_simple \*buf, uint64\_t val)

Push 64-bit value to the beginning of the buffer.

[net\_buf\_simple\_add\_le64](group__net__buf.md#ga79dc411da328b847dcf1903d71eaf011)

void net\_buf\_simple\_add\_le64(struct net\_buf\_simple \*buf, uint64\_t val)

Add 64-bit value at the end of the buffer.

[net\_buf\_simple\_pull\_le64](group__net__buf.md#ga7e0e2d0adbe9062d08f5d8afc7acd89e)

uint64\_t net\_buf\_simple\_pull\_le64(struct net\_buf\_simple \*buf)

Remove and convert 64 bits from the beginning of the buffer.

[net\_buf\_put](group__net__buf.md#ga7e1bcc520b7bffcbd9c1d3d308100047)

void net\_buf\_put(struct k\_fifo \*fifo, struct net\_buf \*buf)

Put a buffer to the end of a FIFO.

[net\_buf\_push\_mem](group__net__buf.md#ga7e9daccec8cae1b9bfda52b0758adf0c)

static void \* net\_buf\_push\_mem(struct net\_buf \*buf, const void \*mem, size\_t len)

Copies the given number of bytes to the start of the buffer.

**Definition** net\_buf.h:2062

[net\_buf\_pull\_le48](group__net__buf.md#ga7eeee45b6639146d1492f92263ee4f51)

static uint64\_t net\_buf\_pull\_le48(struct net\_buf \*buf)

Remove and convert 48 bits from the beginning of the buffer.

**Definition** net\_buf.h:2426

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

**Definition** net\_buf.h:2202

[net\_buf\_pull\_le24](group__net__buf.md#ga85c505321484a50ed9422f24934ed077)

static uint32\_t net\_buf\_pull\_le24(struct net\_buf \*buf)

Remove and convert 24 bits from the beginning of the buffer.

**Definition** net\_buf.h:2336

[net\_buf\_simple\_push\_le32](group__net__buf.md#ga8662e6bada476c0d48cebea4661b2ac1)

void net\_buf\_simple\_push\_le32(struct net\_buf\_simple \*buf, uint32\_t val)

Push 32-bit value to the beginning of the buffer.

[net\_buf\_add\_u8](group__net__buf.md#ga868ac2bea103fed568b461cbcd45eda2)

static uint8\_t \* net\_buf\_add\_u8(struct net\_buf \*buf, uint8\_t val)

Add (8-bit) byte at the end of the buffer.

**Definition** net\_buf.h:1639

[net\_buf\_push\_be24](group__net__buf.md#ga87338399d8ecd64a894908ed4a2f710b)

static void net\_buf\_push\_be24(struct net\_buf \*buf, uint32\_t val)

Push 24-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2132

[net\_buf\_push\_le24](group__net__buf.md#ga87524ac50e53ba59c6692af10cf001b9)

static void net\_buf\_push\_le24(struct net\_buf \*buf, uint32\_t val)

Push 24-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2118

[net\_buf\_reserve](group__net__buf.md#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)

static void net\_buf\_reserve(struct net\_buf \*buf, size\_t reserve)

Initialize buffer with the given headroom.

**Definition** net\_buf.h:1589

[net\_buf\_remove\_be64](group__net__buf.md#ga8b9edd213da2d48dfb8d70a8d307ba13)

static uint64\_t net\_buf\_remove\_be64(struct net\_buf \*buf)

Remove and convert 64 bits from the end of the buffer.

**Definition** net\_buf.h:2029

[net\_buf\_alloc\_with\_data](group__net__buf.md#ga8c24d0761d6d38facb6cca60c7c13c0c)

struct net\_buf \* net\_buf\_alloc\_with\_data(struct net\_buf\_pool \*pool, void \*data, size\_t size, k\_timeout\_t timeout)

Allocate a new buffer from a pool but with external data pointer.

[net\_buf\_pull\_be24](group__net__buf.md#ga8de937e8775879712ea0acbf60327a95)

static uint32\_t net\_buf\_pull\_be24(struct net\_buf \*buf)

Remove and convert 24 bits from the beginning of the buffer.

**Definition** net\_buf.h:2351

[net\_buf\_simple\_add\_be64](group__net__buf.md#ga8e31a7b6537d7634e346236534d2a6d0)

void net\_buf\_simple\_add\_be64(struct net\_buf\_simple \*buf, uint64\_t val)

Add 64-bit value at the end of the buffer.

[net\_buf\_add\_be48](group__net__buf.md#ga8fe6feb191ab338e91bd62f44e184deb)

static void net\_buf\_add\_be48(struct net\_buf \*buf, uint64\_t val)

Add 48-bit value at the end of the buffer.

**Definition** net\_buf.h:1789

[net\_buf\_simple\_add\_u8](group__net__buf.md#ga8ff9344b8d8deba1b72b8fca048a525c)

uint8\_t \* net\_buf\_simple\_add\_u8(struct net\_buf\_simple \*buf, uint8\_t val)

Add (8-bit) byte at the end of the buffer.

[net\_buf\_remove\_le24](group__net__buf.md#ga903f59c8dea1b2c54969b567fe315041)

static uint32\_t net\_buf\_remove\_le24(struct net\_buf \*buf)

Remove and convert 24 bits from the end of the buffer.

**Definition** net\_buf.h:1909

[net\_buf\_push\_u8](group__net__buf.md#ga9093202ba0a22bfa519bbe32d4585186)

static void net\_buf\_push\_u8(struct net\_buf \*buf, uint8\_t val)

Push 8-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2076

[net\_buf\_simple\_add\_be16](group__net__buf.md#ga910f2b9df58fb0706aa40e3b80f235aa)

void net\_buf\_simple\_add\_be16(struct net\_buf\_simple \*buf, uint16\_t val)

Add 16-bit value at the end of the buffer.

[net\_buf\_simple\_remove\_be16](group__net__buf.md#ga93f9f84845601df4ffc118be1ffd2fee)

uint16\_t net\_buf\_simple\_remove\_be16(struct net\_buf\_simple \*buf)

Remove and convert 16 bits from the end of the buffer.

[net\_buf\_push](group__net__buf.md#ga96a2b1f07f3a7958057d9c7cc1f01b73)

static void \* net\_buf\_push(struct net\_buf \*buf, size\_t len)

Prepare data to be added at the start of the buffer.

**Definition** net\_buf.h:2045

[net\_buf\_pull\_be16](group__net__buf.md#ga97909a33c374a5c757fd2faf582139b7)

static uint16\_t net\_buf\_pull\_be16(struct net\_buf \*buf)

Remove and convert 16 bits from the beginning of the buffer.

**Definition** net\_buf.h:2321

[net\_buf\_push\_le32](group__net__buf.md#ga97c9046185d6a1e9235bf6914c72dfc4)

static void net\_buf\_push\_le32(struct net\_buf \*buf, uint32\_t val)

Push 32-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2146

[net\_buf\_pull\_le64](group__net__buf.md#ga9a3df35e2287cbcfe1b60e2efa52c64e)

static uint64\_t net\_buf\_pull\_le64(struct net\_buf \*buf)

Remove and convert 64 bits from the beginning of the buffer.

**Definition** net\_buf.h:2456

[net\_buf\_simple\_remove\_be40](group__net__buf.md#ga9abd2bccc90cf654556c18322888d131)

uint64\_t net\_buf\_simple\_remove\_be40(struct net\_buf\_simple \*buf)

Remove and convert 40 bits from the end of the buffer.

[net\_buf\_simple\_remove\_be24](group__net__buf.md#ga9b39384162a91d7d07e037a9ada782dd)

uint32\_t net\_buf\_simple\_remove\_be24(struct net\_buf\_simple \*buf)

Remove and convert 24 bits from the end of the buffer.

[net\_buf\_allocator\_cb](group__net__buf.md#ga9b74d094a45daf74cd230eaa4fcbc065)

struct net\_buf \*(\* net\_buf\_allocator\_cb)(k\_timeout\_t timeout, void \*user\_data)

Network buffer allocator callback.

**Definition** net\_buf.h:2619

[net\_buf\_simple\_pull\_mem](group__net__buf.md#ga9c676fdbd6e999a9eab26b13d3608e0c)

void \* net\_buf\_simple\_pull\_mem(struct net\_buf\_simple \*buf, size\_t len)

Remove data from the beginning of the buffer.

[net\_buf\_simple\_remove\_le32](group__net__buf.md#ga9e8d016ce384378142fdec6c8dde2457)

uint32\_t net\_buf\_simple\_remove\_le32(struct net\_buf\_simple \*buf)

Remove and convert 32 bits from the end of the buffer.

[net\_buf\_simple\_add\_le16](group__net__buf.md#gaa2daf3b20074ff1a23806ce88becebf5)

void net\_buf\_simple\_add\_le16(struct net\_buf\_simple \*buf, uint16\_t val)

Add 16-bit value at the end of the buffer.

[net\_buf\_simple\_pull\_be40](group__net__buf.md#gaa665830dad59ac957f79c7f1cc84aed5)

uint64\_t net\_buf\_simple\_pull\_be40(struct net\_buf\_simple \*buf)

Remove and convert 40 bits from the beginning of the buffer.

[net\_buf\_simple\_tail](group__net__buf.md#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)

static uint8\_t \* net\_buf\_simple\_tail(const struct net\_buf\_simple \*buf)

Get the tail pointer for a buffer.

**Definition** net\_buf.h:905

[net\_buf\_simple\_push\_mem](group__net__buf.md#gaaa838083c610f7426c509efaae69a511)

void \* net\_buf\_simple\_push\_mem(struct net\_buf\_simple \*buf, const void \*mem, size\_t len)

Copy given number of bytes from memory to the start of the buffer.

[net\_buf\_remove\_be48](group__net__buf.md#gaab0e3bcc21c958c01ef076cd0efe087c)

static uint64\_t net\_buf\_remove\_be48(struct net\_buf \*buf)

Remove and convert 48 bits from the end of the buffer.

**Definition** net\_buf.h:1999

[net\_buf\_simple\_add\_be32](group__net__buf.md#gaac5cd20776d8e7bb4db77cbe5366373c)

void net\_buf\_simple\_add\_be32(struct net\_buf\_simple \*buf, uint32\_t val)

Add 32-bit value at the end of the buffer.

[NET\_BUF\_EXTERNAL\_DATA](group__net__buf.md#gaaeacbdf3cfda12691c75253015e5c19a)

#define NET\_BUF\_EXTERNAL\_DATA

Flag indicating that the buffer's associated data pointer, points to externally allocated memory.

**Definition** net\_buf.h:997

[net\_buf\_remove\_le16](group__net__buf.md#gaaf654110fb6a8bdfc27433945d4d1308)

static uint16\_t net\_buf\_remove\_le16(struct net\_buf \*buf)

Remove and convert 16 bits from the end of the buffer.

**Definition** net\_buf.h:1864

[net\_buf\_simple\_headroom](group__net__buf.md#gaafcb52db2daf1c4451a600e7b647e55c)

size\_t net\_buf\_simple\_headroom(const struct net\_buf\_simple \*buf)

Check buffer headroom.

[net\_buf\_push\_le16](group__net__buf.md#gab6c84c6846c06c2b339bc88df35e2655)

static void net\_buf\_push\_le16(struct net\_buf \*buf, uint16\_t val)

Push 16-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2090

[net\_buf\_simple\_remove\_be48](group__net__buf.md#gab93d22797c3f406179c4c145241d6abb)

uint64\_t net\_buf\_simple\_remove\_be48(struct net\_buf\_simple \*buf)

Remove and convert 48 bits from the end of the buffer.

[net\_buf\_simple\_push\_le24](group__net__buf.md#gabe52d6735d835edc361666bb3413b907)

void net\_buf\_simple\_push\_le24(struct net\_buf\_simple \*buf, uint32\_t val)

Push 24-bit value to the beginning of the buffer.

[net\_buf\_unref](group__net__buf.md#gabedcb728bc2fc0c2b5319a8fd87e8273)

void net\_buf\_unref(struct net\_buf \*buf)

Decrements the reference count of a buffer.

[net\_buf\_simple\_save](group__net__buf.md#gabf5b098aa0926d9b7fb88baff8a3e2d8)

static void net\_buf\_simple\_save(const struct net\_buf\_simple \*buf, struct net\_buf\_simple\_state \*state)

Save the parsing state of a buffer.

**Definition** net\_buf.h:965

[net\_buf\_push\_be48](group__net__buf.md#gabfbcb051019ff210cc2b85adcf4bc821)

static void net\_buf\_push\_be48(struct net\_buf \*buf, uint64\_t val)

Push 48-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2216

[net\_buf\_simple\_push\_be24](group__net__buf.md#gabfddd4956ec1e356002a3122fea74b72)

void net\_buf\_simple\_push\_be24(struct net\_buf\_simple \*buf, uint32\_t val)

Push 24-bit value to the beginning of the buffer.

[net\_buf\_simple\_max\_len](group__net__buf.md#gabfe255688a80c0abea866762ff4c5a6c)

uint16\_t net\_buf\_simple\_max\_len(const struct net\_buf\_simple \*buf)

Check maximum net\_buf\_simple::len value.

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

**Definition** net\_buf.h:1804

[net\_buf\_headroom](group__net__buf.md#gac9a09897f44e708f920064826aa2f703)

static size\_t net\_buf\_headroom(const struct net\_buf \*buf)

Check buffer headroom.

**Definition** net\_buf.h:2499

[net\_buf\_remove\_be32](group__net__buf.md#gacce707d646d7008ec3167af1a0b20da8)

static uint32\_t net\_buf\_remove\_be32(struct net\_buf \*buf)

Remove and convert 32 bits from the end of the buffer.

**Definition** net\_buf.h:1939

[net\_buf\_id](group__net__buf.md#gacdf048dc0afc7ef67027117e0d51d3a3)

int net\_buf\_id(const struct net\_buf \*buf)

Get a zero-based index for a buffer.

[net\_buf\_remove\_mem](group__net__buf.md#gace5ad98eac4772db3b0fa2181912f1f0)

static void \* net\_buf\_remove\_mem(struct net\_buf \*buf, size\_t len)

Remove data from the end of the buffer.

**Definition** net\_buf.h:1834

[net\_buf\_add\_mem](group__net__buf.md#gacf4e2eba52975ba6728c79274a769d0f)

static void \* net\_buf\_add\_mem(struct net\_buf \*buf, const void \*mem, size\_t len)

Copies the given number of bytes to the end of the buffer.

**Definition** net\_buf.h:1622

[net\_buf\_simple\_pull\_be64](group__net__buf.md#gad07f0d49a7db99063077de493e7b0712)

uint64\_t net\_buf\_simple\_pull\_be64(struct net\_buf\_simple \*buf)

Remove and convert 64 bits from the beginning of the buffer.

[net\_buf\_simple\_push\_be32](group__net__buf.md#gad0c3b8fdeaad6437c3dfcbb03fa52426)

void net\_buf\_simple\_push\_be32(struct net\_buf\_simple \*buf, uint32\_t val)

Push 32-bit value to the beginning of the buffer.

[net\_buf\_push\_le64](group__net__buf.md#gad4ee42b023881f80211fbeca53a0f25d)

static void net\_buf\_push\_le64(struct net\_buf \*buf, uint64\_t val)

Push 64-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2230

[net\_buf\_simple\_pull\_le16](group__net__buf.md#gad59d180ae81b55f6d618565a37d25dba)

uint16\_t net\_buf\_simple\_pull\_le16(struct net\_buf\_simple \*buf)

Remove and convert 16 bits from the beginning of the buffer.

[net\_buf\_simple\_push\_be40](group__net__buf.md#gad65bcaf8401e6f5ffff81a998cfb8fe5)

void net\_buf\_simple\_push\_be40(struct net\_buf\_simple \*buf, uint64\_t val)

Push 40-bit value to the beginning of the buffer.

[net\_buf\_simple\_pull\_le40](group__net__buf.md#gad669c07efe5cb90ebffcc76d9c1029a1)

uint64\_t net\_buf\_simple\_pull\_le40(struct net\_buf\_simple \*buf)

Remove and convert 40 bits from the beginning of the buffer.

[net\_buf\_remove\_u8](group__net__buf.md#gad954b9f37790d5e7087db7db7bdedd41)

static uint8\_t net\_buf\_remove\_u8(struct net\_buf \*buf)

Remove a 8-bit value from the end of the buffer.

**Definition** net\_buf.h:1849

[net\_buf\_simple\_add\_be48](group__net__buf.md#gadb433fb4a1a61702c0615359a4340171)

void net\_buf\_simple\_add\_be48(struct net\_buf\_simple \*buf, uint64\_t val)

Add 48-bit value at the end of the buffer.

[net\_buf\_add\_le16](group__net__buf.md#gadd6d01a3b1efd0de16f9bef975809404)

static void net\_buf\_add\_le16(struct net\_buf \*buf, uint16\_t val)

Add 16-bit value at the end of the buffer.

**Definition** net\_buf.h:1654

[net\_buf\_remove\_be40](group__net__buf.md#gae2920eab3c56d0d462811b83961df466)

static uint64\_t net\_buf\_remove\_be40(struct net\_buf \*buf)

Remove and convert 40 bits from the end of the buffer.

**Definition** net\_buf.h:1969

[net\_buf\_simple\_pull\_be16](group__net__buf.md#gae36458ba05a4ab89e429be4cfd264440)

uint16\_t net\_buf\_simple\_pull\_be16(struct net\_buf\_simple \*buf)

Remove and convert 16 bits from the beginning of the buffer.

[net\_buf\_push\_be32](group__net__buf.md#gae4e64a23708ed910fb6c3ab8ba481a4c)

static void net\_buf\_push\_be32(struct net\_buf \*buf, uint32\_t val)

Push 32-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2160

[net\_buf\_add\_le32](group__net__buf.md#gae8ba33b6592ef7fd859b35d63b285d87)

static void net\_buf\_add\_le32(struct net\_buf \*buf, uint32\_t val)

Add 32-bit value at the end of the buffer.

**Definition** net\_buf.h:1714

[net\_buf\_simple\_remove\_be32](group__net__buf.md#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)

uint32\_t net\_buf\_simple\_remove\_be32(struct net\_buf\_simple \*buf)

Remove and convert 32 bits from the end of the buffer.

[net\_buf\_remove\_le32](group__net__buf.md#gae9321a469cc751c58cfb532afd57d265)

static uint32\_t net\_buf\_remove\_le32(struct net\_buf \*buf)

Remove and convert 32 bits from the end of the buffer.

**Definition** net\_buf.h:1924

[net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)

static size\_t net\_buf\_frags\_len(const struct net\_buf \*buf)

Calculate amount of bytes stored in fragments.

**Definition** net\_buf.h:2700

[net\_buf\_tailroom](group__net__buf.md#gaecbc6adf16469e3366c88445ea7a553a)

static size\_t net\_buf\_tailroom(const struct net\_buf \*buf)

Check buffer tailroom.

**Definition** net\_buf.h:2485

[net\_buf\_pull\_le16](group__net__buf.md#gaed64e9f2b969f2c0d99cd281e73c860a)

static uint16\_t net\_buf\_pull\_le16(struct net\_buf \*buf)

Remove and convert 16 bits from the beginning of the buffer.

**Definition** net\_buf.h:2306

[net\_buf\_tail](group__net__buf.md#gaedb10a84b352a3d7716bef979af2ab31)

static uint8\_t \* net\_buf\_tail(const struct net\_buf \*buf)

Get the tail pointer for a buffer.

**Definition** net\_buf.h:2527

[net\_buf\_pull\_mem](group__net__buf.md#gaedc5ffe19bb0ec438e633023c3c5de74)

static void \* net\_buf\_pull\_mem(struct net\_buf \*buf, size\_t len)

Remove data from the beginning of the buffer.

**Definition** net\_buf.h:2276

[net\_buf\_simple\_restore](group__net__buf.md#gaedd36481657a7a9d108659d56e131721)

static void net\_buf\_simple\_restore(struct net\_buf\_simple \*buf, struct net\_buf\_simple\_state \*state)

Restore the parsing state of a buffer.

**Definition** net\_buf.h:981

[net\_buf\_pull](group__net__buf.md#gaef433d92734dd8691c292abdb823ba0e)

static void \* net\_buf\_pull(struct net\_buf \*buf, size\_t len)

Remove data from the beginning of the buffer.

**Definition** net\_buf.h:2260

[net\_buf\_data\_match](group__net__buf.md#gaef938c3ab676a5bd5bf8338b8d7cb30c)

size\_t net\_buf\_data\_match(const struct net\_buf \*buf, size\_t offset, const void \*data, size\_t len)

Match data with a net\_buf's content.

[net\_buf\_push\_le40](group__net__buf.md#gaefab4a755cf4fb7d2b4a142a9351c189)

static void net\_buf\_push\_le40(struct net\_buf \*buf, uint64\_t val)

Push 40-bit value to the beginning of the buffer.

**Definition** net\_buf.h:2174

[net\_buf\_add\_le48](group__net__buf.md#gaf19bf75c3d4d645b1eebf9254aa22790)

static void net\_buf\_add\_le48(struct net\_buf \*buf, uint64\_t val)

Add 48-bit value at the end of the buffer.

**Definition** net\_buf.h:1774

[net\_buf\_simple\_add\_le24](group__net__buf.md#gaf1a89eb15eed79003412ba5a32a35cf6)

void net\_buf\_simple\_add\_le24(struct net\_buf\_simple \*buf, uint32\_t val)

Add 24-bit value at the end of the buffer.

[net\_buf\_user\_data](group__net__buf.md#gaf2df457abe3e56d47107b76bdc004756)

static void \* net\_buf\_user\_data(const struct net\_buf \*buf)

Get a pointer to the user data of a buffer.

**Definition** net\_buf.h:1565

[net\_buf\_clone](group__net__buf.md#gaf4d80e2878e3c790fff206bec820f03f)

struct net\_buf \* net\_buf\_clone(struct net\_buf \*buf, k\_timeout\_t timeout)

Clone buffer.

[net\_buf\_simple\_remove\_u8](group__net__buf.md#gaf508f74e5e050a7294e8a70bd3725fc3)

uint8\_t net\_buf\_simple\_remove\_u8(struct net\_buf\_simple \*buf)

Remove a 8-bit value from the end of the buffer.

[net\_buf\_simple\_pull](group__net__buf.md#gaf5ab4a5fe4a6226be72a510fea0ed8a8)

void \* net\_buf\_simple\_pull(struct net\_buf\_simple \*buf, size\_t len)

Remove data from the beginning of the buffer.

[net\_buf\_simple\_push\_be64](group__net__buf.md#gafea2201655955ab004b5f77106998ae9)

void net\_buf\_simple\_push\_be64(struct net\_buf\_simple \*buf, uint64\_t val)

Push 64-bit value to the beginning of the buffer.

[net\_buf\_linearize](group__net__buf.md#gaffd49f2de8e72d5f7585b4e5167923d8)

size\_t net\_buf\_linearize(void \*dst, size\_t dst\_len, const struct net\_buf \*src, size\_t offset, size\_t len)

Copy bytes from net\_buf chain starting at offset to linear buffer.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

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

**Definition** kernel.h:2495

[k\_lifo](structk__lifo.md)

**Definition** kernel.h:2736

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** net\_buf.h:1078

[net\_buf\_pool::destroy](structnet__buf__pool.md#a2a9141d7cd20cd98818a92dc5bc99f56)

void(\*const destroy)(struct net\_buf \*buf)

Optional destroy callback when buffer is freed.

**Definition** net\_buf.h:1109

[net\_buf\_pool::uninit\_count](structnet__buf__pool.md#a3fdf83b4c0b5acefbb761da285791ad2)

uint16\_t uninit\_count

Number of uninitialized buffers.

**Definition** net\_buf.h:1089

[net\_buf\_pool::user\_data\_size](structnet__buf__pool.md#a4718ecec19d7e2ccaf04b6ff61120975)

uint8\_t user\_data\_size

Size of user data allocated to this pool.

**Definition** net\_buf.h:1092

[net\_buf\_pool::buf\_count](structnet__buf__pool.md#a55b57f4f573c7e752c3ccf2f92f25626)

const uint16\_t buf\_count

Number of buffers in pool.

**Definition** net\_buf.h:1086

[net\_buf\_pool::alloc](structnet__buf__pool.md#a617bd8f77e55481d97183da8c0c62cc5)

const struct net\_buf\_data\_alloc \* alloc

Data allocation handlers.

**Definition** net\_buf.h:1112

[net\_buf\_pool::free](structnet__buf__pool.md#a97e5b2e51238e859f93882a8008ba305)

struct k\_lifo free

LIFO to place the buffer into when free.

**Definition** net\_buf.h:1080

[net\_buf\_pool::lock](structnet__buf__pool.md#ae92fc3f3f51be63ccdeee9614d21cc34)

struct k\_spinlock lock

To prevent concurrent access/modifications.

**Definition** net\_buf.h:1083

[net\_buf\_simple\_state](structnet__buf__simple__state.md)

Parsing state of a buffer.

**Definition** net\_buf.h:950

[net\_buf\_simple\_state::offset](structnet__buf__simple__state.md#a4061f8e50e14289b1ec999ef490c8fbf)

uint16\_t offset

Offset of the data pointer from the beginning of the storage.

**Definition** net\_buf.h:952

[net\_buf\_simple\_state::len](structnet__buf__simple__state.md#af0e544fe2b018a7ff0b30970e9de8253)

uint16\_t len

Length of data.

**Definition** net\_buf.h:954

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[net\_buf\_simple::data](structnet__buf__simple.md#ad232efff435f425d30ac78f5abf2d8b1)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** net\_buf.h:91

[net\_buf\_simple::size](structnet__buf__simple.md#ae6dc4aa029a67d3911293618eb30caa6)

uint16\_t size

Amount of data that net\_buf\_simple::\_\_buf can store.

**Definition** net\_buf.h:101

[net\_buf\_simple::len](structnet__buf__simple.md#ae8707c50d70c26b53281b40eb1720cf3)

uint16\_t len

Length of the data behind the data pointer.

**Definition** net\_buf.h:98

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** net\_buf.h:1038

[net\_buf::frags](structnet__buf.md#a1fa032cc23854c35eae013020823fa88)

struct net\_buf \* frags

Fragments associated with this buffer.

**Definition** net\_buf.h:1011

[net\_buf::ref](structnet__buf.md#a42da518a82f4c37c45814b4f8c5f2731)

uint8\_t ref

Reference count.

**Definition** net\_buf.h:1014

[net\_buf::pool\_id](structnet__buf.md#a45f294bac054d64034bddcc4c6574d29)

uint8\_t pool\_id

Where the buffer should go when freed up.

**Definition** net\_buf.h:1020

[net\_buf::node](structnet__buf.md#a5cc70f57e5b776cfa12b2d556e5958f3)

sys\_snode\_t node

Allow placing the buffer into sys\_slist\_t.

**Definition** net\_buf.h:1008

[net\_buf::user\_data\_size](structnet__buf.md#a65db7bed62d7211114767e6ce58dad75)

uint8\_t user\_data\_size

Size of user data on this buffer.

**Definition** net\_buf.h:1023

[net\_buf::flags](structnet__buf.md#aa4fcce2e2894fc5dbd9cc74fc020647e)

uint8\_t flags

Bit-field of buffer flags.

**Definition** net\_buf.h:1017

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** net\_buf.h:1032

[net\_buf::user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7)

uint8\_t user\_data[]

System metadata for this buffer.

**Definition** net\_buf.h:1053

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** net\_buf.h:1035

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net\_buf.h](net__buf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
