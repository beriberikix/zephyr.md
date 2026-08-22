---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net__mgmt_8h_source.html
original_path: doxygen/html/net__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_mgmt.h

[Go to the documentation of this file.](net__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_MGMT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_NET\_MGMT\_H\_

14

15#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

16#include <[zephyr/net/net\_core.h](net__core_8h.md)>

17#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

31

32struct [net\_if](structnet__if.md);

33

38#define NET\_MGMT\_EVENT\_MASK GENMASK64(63, 63) /\* 0x8000000000000000 \*/

39#define NET\_MGMT\_ON\_IFACE\_MASK GENMASK64(62, 62) /\* 0x4000000000000000 \*/

40#define NET\_MGMT\_LAYER\_MASK GENMASK64(61, 60) /\* 0x3000000000000000 \*/

41#define NET\_MGMT\_SYNC\_EVENT\_MASK GENMASK64(59, 59) /\* 0x0800000000000000 \*/

42#define NET\_MGMT\_LAYER\_CODE\_MASK GENMASK64(58, 52) /\* 0x07F0000000000000 \*/

43#define NET\_MGMT\_COMMAND\_MASK GENMASK64(51, 0) /\* 0x000FFFFFFFFFFFFF \*/

44

45#define NET\_MGMT\_MAX\_COMMANDS 52 /\* TODO: figure out the value from mask \*/

46

47#define NET\_MGMT\_EVENT\_BIT BIT64(63)

48#define NET\_MGMT\_IFACE\_BIT BIT64(62)

49#define NET\_MGMT\_SYNC\_EVENT\_BIT BIT64(59)

50

51#define NET\_MGMT\_LAYER(\_layer) FIELD\_PREP(NET\_MGMT\_LAYER\_MASK, (\_layer))

52#define NET\_MGMT\_LAYER\_CODE(\_code) FIELD\_PREP(NET\_MGMT\_LAYER\_CODE\_MASK, (\_code))

53

54#define NET\_MGMT\_EVENT(mgmt\_request) FIELD\_GET(NET\_MGMT\_EVENT\_MASK, mgmt\_request)

55#define NET\_MGMT\_ON\_IFACE(mgmt\_request) FIELD\_GET(NET\_MGMT\_ON\_IFACE\_MASK, mgmt\_request)

56#define NET\_MGMT\_EVENT\_SYNCHRONOUS(mgmt\_request) FIELD\_GET(NET\_MGMT\_SYNC\_EVENT\_MASK, mgmt\_request)

57#define NET\_MGMT\_GET\_LAYER(mgmt\_request) FIELD\_GET(NET\_MGMT\_LAYER\_MASK, mgmt\_request)

58#define NET\_MGMT\_GET\_LAYER\_CODE(mgmt\_request) FIELD\_GET(NET\_MGMT\_LAYER\_CODE\_MASK, mgmt\_request)

59#define NET\_MGMT\_GET\_COMMAND(mgmt\_request) FIELD\_GET(NET\_MGMT\_COMMAND\_MASK, mgmt\_request)

60

61#define NET\_MGMT\_CMD(cmd) cmd = BIT64(cmd ##\_VAL)

62

63/\* Useful generic definitions \*/

64#define NET\_MGMT\_LAYER\_L2 1

65#define NET\_MGMT\_LAYER\_L3 2

66#define NET\_MGMT\_LAYER\_L4 3

67

69

[ 71](group__net__mgmt.md#ga5e6911455b9ab9f4c82780001459461a)enum [net\_mgmt\_layer\_code](group__net__mgmt.md#ga5e6911455b9ab9f4c82780001459461a) {

[ 72](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd) [NET\_MGMT\_LAYER\_CODE\_UNKNOWN](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd) = 0x00,

[ 73](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518) [NET\_MGMT\_LAYER\_CODE\_IFACE](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518) = 0x01,

[ 74](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7) [NET\_MGMT\_LAYER\_CODE\_CONN](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7) = 0x02,

[ 75](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2) [NET\_MGMT\_LAYER\_CODE\_IPV4](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2) = 0x03,

[ 76](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8) [NET\_MGMT\_LAYER\_CODE\_IPV6](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8) = 0x04,

[ 77](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e) [NET\_MGMT\_LAYER\_CODE\_L4](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e) = 0x05,

[ 78](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7) [NET\_MGMT\_LAYER\_CODE\_COAP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7) = 0x06,

[ 79](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6) [NET\_MGMT\_LAYER\_CODE\_STATS](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6) = 0x07,

[ 80](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc) [NET\_MGMT\_LAYER\_CODE\_HOSTAP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc) = 0x08,

[ 81](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4) [NET\_MGMT\_LAYER\_CODE\_ETHERNET](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4) = 0x09,

[ 82](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b) [NET\_MGMT\_LAYER\_CODE\_IEEE802514](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b) = 0x0A,

[ 83](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1) [NET\_MGMT\_LAYER\_CODE\_PPP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1) = 0x0B,

[ 84](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca) [NET\_MGMT\_LAYER\_CODE\_VIRTUAL](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca) = 0x0C,

[ 85](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789) [NET\_MGMT\_LAYER\_CODE\_WIFI](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789) = 0x0D,

86

87 /\* Out of tree code can use the following userX layer codes \*/

[ 88](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977) [NET\_MGMT\_LAYER\_CODE\_USER3](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977) = 0x7C,

[ 89](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4) [NET\_MGMT\_LAYER\_CODE\_USER2](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4) = 0x7D,

[ 90](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a) [NET\_MGMT\_LAYER\_CODE\_USER1](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a) = 0x7E,

91

92 /\* Reserved layer code for future use \*/

[ 93](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75) [NET\_MGMT\_LAYER\_CODE\_RESERVED](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75) = 0x7F

94};

95

96#include <[zephyr/net/net\_event.h](net__event_8h.md)>

97

[ 109](group__net__mgmt.md#ga78b9302193bd0c5cc35d81d298a5eb6b)typedef int (\*[net\_mgmt\_request\_handler\_t](group__net__mgmt.md#ga78b9302193bd0c5cc35d81d298a5eb6b))([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_request,

110 struct [net\_if](structnet__if.md) \*iface,

111 void \*data, size\_t len);

112

[ 121](group__net__mgmt.md#ga40e0f9fc86812ad9f6fe174b4c3804e6)#define net\_mgmt(\_mgmt\_request, \_iface, \_data, \_len) \

122 net\_mgmt\_##\_mgmt\_request(\_mgmt\_request, \_iface, \_data, \_len)

123

[ 129](group__net__mgmt.md#ga08bde8717fd8e12a338c517b22b87776)#define NET\_MGMT\_DEFINE\_REQUEST\_HANDLER(\_mgmt\_request) \

130 extern int net\_mgmt\_##\_mgmt\_request(uint64\_t mgmt\_request, \

131 struct net\_if \*iface, \

132 void \*data, size\_t len)

133

[ 140](group__net__mgmt.md#gab67d09d1e65b806ec1957451cbf60501)#define NET\_MGMT\_REGISTER\_REQUEST\_HANDLER(\_mgmt\_request, \_func) \

141 FUNC\_ALIAS(\_func, net\_mgmt\_##\_mgmt\_request, int)

142

143struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md);

144

[ 153](group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2)typedef void (\*[net\_mgmt\_event\_handler\_t](group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2))(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb,

154 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event,

155 struct [net\_if](structnet__if.md) \*iface);

156

[ 163](structnet__mgmt__event__callback.md)struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) {

[ 167](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea);

168

169 union {

[ 172](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2) [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2) [handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2);

[ 176](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3) struct [k\_sem](structk__sem.md) \*[sync\_call](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3);

177 };

178

179#ifdef CONFIG\_NET\_MGMT\_EVENT\_INFO

180 const void \*info;

181 size\_t info\_length;

182#endif

183

189 union {

[ 198](structnet__mgmt__event__callback.md#a99e3174c1052488877b3db6349de61e8) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [event\_mask](structnet__mgmt__event__callback.md#a99e3174c1052488877b3db6349de61e8);

[ 202](structnet__mgmt__event__callback.md#a555d868d6a0d6ecb04d09607fab06b79) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [raised\_event](structnet__mgmt__event__callback.md#a555d868d6a0d6ecb04d09607fab06b79);

203 };

204};

205

[ 217](group__net__mgmt.md#gaf3773f8e945c4ec05b2fab46cd8b1881)typedef void (\*[net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#gaf3773f8e945c4ec05b2fab46cd8b1881))([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event,

218 struct [net\_if](structnet__if.md) \*iface,

219 void \*info, size\_t info\_length,

220 void \*user\_data);

221

223

224/\* Structure for event handler registered at compile time \*/

225struct net\_mgmt\_event\_static\_handler {

226 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) event\_mask;

227 [net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#gaf3773f8e945c4ec05b2fab46cd8b1881) handler;

228 void \*user\_data;

229};

230

232

[ 246](group__net__mgmt.md#ga3a6ca8a72ab12afd4f9b0461253eaa12)#define NET\_MGMT\_REGISTER\_EVENT\_HANDLER(\_name, \_event\_mask, \_func, \_user\_data) \

247 const STRUCT\_SECTION\_ITERABLE(net\_mgmt\_event\_static\_handler, \_name) = { \

248 .event\_mask = \_event\_mask, \

249 .handler = \_func, \

250 .user\_data = (void \*)\_user\_data, \

251 }

252

259#ifdef CONFIG\_NET\_MGMT\_EVENT

260static inline

[ 261](group__net__mgmt.md#ga4e42b6d16b863ca374d032682e8c11fb)void [net\_mgmt\_init\_event\_callback](group__net__mgmt.md#ga4e42b6d16b863ca374d032682e8c11fb)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb,

262 [net\_mgmt\_event\_handler\_t](group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2) handler,

263 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event\_mask)

264{

265 \_\_ASSERT(cb, "Callback pointer should not be NULL");

266 \_\_ASSERT(handler, "Handler pointer should not be NULL");

267

268 cb->[handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2) = handler;

269 cb->[event\_mask](structnet__mgmt__event__callback.md#a99e3174c1052488877b3db6349de61e8) = mgmt\_event\_mask;

270};

271#else

272#define net\_mgmt\_init\_event\_callback(...)

273#endif

274

279#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 280](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)void [net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb);

281#else

282#define net\_mgmt\_add\_event\_callback(...)

283#endif

284

289#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 290](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)void [net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)(struct [net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md) \*cb);

291#else

292#define net\_mgmt\_del\_event\_callback(...)

293#endif

294

308#if defined(CONFIG\_NET\_MGMT\_EVENT)

[ 309](group__net__mgmt.md#ga6415ec1e2e7f477c8976022ac33b0654)void [net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga6415ec1e2e7f477c8976022ac33b0654)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event, struct [net\_if](structnet__if.md) \*iface,

310 const void \*info, size\_t length);

311#else

312#define net\_mgmt\_event\_notify\_with\_info(...)

313#endif

314

321#if defined(CONFIG\_NET\_MGMT\_EVENT)

[ 322](group__net__mgmt.md#gabf710692e596a2d98f37b82da884a82a)static inline void [net\_mgmt\_event\_notify](group__net__mgmt.md#gabf710692e596a2d98f37b82da884a82a)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event,

323 struct [net\_if](structnet__if.md) \*iface)

324{

325 [net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga6415ec1e2e7f477c8976022ac33b0654)(mgmt\_event, iface, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0);

326}

327#else

328#define net\_mgmt\_event\_notify(...)

329#endif

330

351#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 352](group__net__mgmt.md#ga7137c77c55ee2609941c88db79e22d1a)int [net\_mgmt\_event\_wait](group__net__mgmt.md#ga7137c77c55ee2609941c88db79e22d1a)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event\_mask,

353 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*raised\_event,

354 struct [net\_if](structnet__if.md) \*\*iface,

355 const void \*\*info,

356 size\_t \*info\_length,

357 [k\_timeout\_t](structk__timeout__t.md) timeout);

358#else

359static inline int [net\_mgmt\_event\_wait](group__net__mgmt.md#ga7137c77c55ee2609941c88db79e22d1a)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event\_mask,

360 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*raised\_event,

361 struct [net\_if](structnet__if.md) \*\*iface,

362 const void \*\*info,

363 size\_t \*info\_length,

364 [k\_timeout\_t](structk__timeout__t.md) timeout)

365{

366 ARG\_UNUSED(mgmt\_event\_mask);

367 ARG\_UNUSED(raised\_event);

368 ARG\_UNUSED(iface);

369 ARG\_UNUSED(info);

370 ARG\_UNUSED(info\_length);

371 ARG\_UNUSED(timeout);

372 return 0;

373}

374#endif

375

395#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 396](group__net__mgmt.md#ga3ab114106df41144c0fae8e6faad12cb)int [net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga3ab114106df41144c0fae8e6faad12cb)(struct [net\_if](structnet__if.md) \*iface,

397 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event\_mask,

398 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*raised\_event,

399 const void \*\*info,

400 size\_t \*info\_length,

401 [k\_timeout\_t](structk__timeout__t.md) timeout);

402#else

403static inline int [net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga3ab114106df41144c0fae8e6faad12cb)(struct [net\_if](structnet__if.md) \*iface,

404 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mgmt\_event\_mask,

405 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*raised\_event,

406 const void \*\*info,

407 size\_t \*info\_length,

408 [k\_timeout\_t](structk__timeout__t.md) timeout)

409{

410 ARG\_UNUSED(iface);

411 ARG\_UNUSED(mgmt\_event\_mask);

412 ARG\_UNUSED(raised\_event);

413 ARG\_UNUSED(info);

414 ARG\_UNUSED(info\_length);

415 ARG\_UNUSED(timeout);

416 return 0;

417}

418#endif

419

424#ifdef CONFIG\_NET\_MGMT\_EVENT

[ 425](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)void [net\_mgmt\_event\_init](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)(void);

426#else

427#define net\_mgmt\_event\_init(...)

428#endif /\* CONFIG\_NET\_MGMT\_EVENT \*/

429

433

434#ifdef \_\_cplusplus

435}

436#endif

437

438#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_MGMT\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[net\_mgmt\_event\_handler\_t](group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2)

void(\* net\_mgmt\_event\_handler\_t)(struct net\_mgmt\_event\_callback \*cb, uint64\_t mgmt\_event, struct net\_if \*iface)

Define the user's callback handler function signature.

**Definition** net\_mgmt.h:153

[net\_mgmt\_event\_wait\_on\_iface](group__net__mgmt.md#ga3ab114106df41144c0fae8e6faad12cb)

int net\_mgmt\_event\_wait\_on\_iface(struct net\_if \*iface, uint64\_t mgmt\_event\_mask, uint64\_t \*raised\_event, const void \*\*info, size\_t \*info\_length, k\_timeout\_t timeout)

Used to wait synchronously on an event mask for a specific iface.

[net\_mgmt\_del\_event\_callback](group__net__mgmt.md#ga4960bfb01ecd891da72c57f17587f946)

void net\_mgmt\_del\_event\_callback(struct net\_mgmt\_event\_callback \*cb)

Delete a user callback.

[net\_mgmt\_init\_event\_callback](group__net__mgmt.md#ga4e42b6d16b863ca374d032682e8c11fb)

static void net\_mgmt\_init\_event\_callback(struct net\_mgmt\_event\_callback \*cb, net\_mgmt\_event\_handler\_t handler, uint64\_t mgmt\_event\_mask)

Helper to initialize a struct net\_mgmt\_event\_callback properly.

**Definition** net\_mgmt.h:261

[net\_mgmt\_layer\_code](group__net__mgmt.md#ga5e6911455b9ab9f4c82780001459461a)

net\_mgmt\_layer\_code

Central place the definition of the layer codes (7 bit value).

**Definition** net\_mgmt.h:71

[net\_mgmt\_event\_notify\_with\_info](group__net__mgmt.md#ga6415ec1e2e7f477c8976022ac33b0654)

void net\_mgmt\_event\_notify\_with\_info(uint64\_t mgmt\_event, struct net\_if \*iface, const void \*info, size\_t length)

Used by the system to notify an event.

[net\_mgmt\_event\_wait](group__net__mgmt.md#ga7137c77c55ee2609941c88db79e22d1a)

int net\_mgmt\_event\_wait(uint64\_t mgmt\_event\_mask, uint64\_t \*raised\_event, struct net\_if \*\*iface, const void \*\*info, size\_t \*info\_length, k\_timeout\_t timeout)

Used to wait synchronously on an event mask.

[net\_mgmt\_request\_handler\_t](group__net__mgmt.md#ga78b9302193bd0c5cc35d81d298a5eb6b)

int(\* net\_mgmt\_request\_handler\_t)(uint64\_t mgmt\_request, struct net\_if \*iface, void \*data, size\_t len)

Signature which all Net MGMT request handler need to follow.

**Definition** net\_mgmt.h:109

[net\_mgmt\_event\_init](group__net__mgmt.md#gaab4fe2e9ea0657bf91fb1910af6729cc)

void net\_mgmt\_event\_init(void)

Used by the core of the network stack to initialize the network event processing.

[net\_mgmt\_event\_notify](group__net__mgmt.md#gabf710692e596a2d98f37b82da884a82a)

static void net\_mgmt\_event\_notify(uint64\_t mgmt\_event, struct net\_if \*iface)

Used by the system to notify an event without any additional information.

**Definition** net\_mgmt.h:322

[net\_mgmt\_add\_event\_callback](group__net__mgmt.md#gae53f5bbc973b0f414107eca75ac0c26f)

void net\_mgmt\_add\_event\_callback(struct net\_mgmt\_event\_callback \*cb)

Add a user callback.

[net\_mgmt\_event\_static\_handler\_t](group__net__mgmt.md#gaf3773f8e945c4ec05b2fab46cd8b1881)

void(\* net\_mgmt\_event\_static\_handler\_t)(uint64\_t mgmt\_event, struct net\_if \*iface, void \*info, size\_t info\_length, void \*user\_data)

Define the user's callback handler function signature.

**Definition** net\_mgmt.h:217

[NET\_MGMT\_LAYER\_CODE\_HOSTAP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc)

@ NET\_MGMT\_LAYER\_CODE\_HOSTAP

Hostap (wpa\_supplicant) layer code.

**Definition** net\_mgmt.h:80

[NET\_MGMT\_LAYER\_CODE\_USER1](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a)

@ NET\_MGMT\_LAYER\_CODE\_USER1

User layer code 1.

**Definition** net\_mgmt.h:90

[NET\_MGMT\_LAYER\_CODE\_IPV4](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2)

@ NET\_MGMT\_LAYER\_CODE\_IPV4

IPv4 layer code.

**Definition** net\_mgmt.h:75

[NET\_MGMT\_LAYER\_CODE\_IFACE](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518)

@ NET\_MGMT\_LAYER\_CODE\_IFACE

Network interface layer code.

**Definition** net\_mgmt.h:73

[NET\_MGMT\_LAYER\_CODE\_UNKNOWN](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd)

@ NET\_MGMT\_LAYER\_CODE\_UNKNOWN

Unknown layer code, do not use.

**Definition** net\_mgmt.h:72

[NET\_MGMT\_LAYER\_CODE\_STATS](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6)

@ NET\_MGMT\_LAYER\_CODE\_STATS

Statistics layer code.

**Definition** net\_mgmt.h:79

[NET\_MGMT\_LAYER\_CODE\_IEEE802514](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b)

@ NET\_MGMT\_LAYER\_CODE\_IEEE802514

IEEE 802.15.4 layer code.

**Definition** net\_mgmt.h:82

[NET\_MGMT\_LAYER\_CODE\_USER3](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977)

@ NET\_MGMT\_LAYER\_CODE\_USER3

User layer code 3.

**Definition** net\_mgmt.h:88

[NET\_MGMT\_LAYER\_CODE\_PPP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1)

@ NET\_MGMT\_LAYER\_CODE\_PPP

PPP layer code.

**Definition** net\_mgmt.h:83

[NET\_MGMT\_LAYER\_CODE\_COAP](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7)

@ NET\_MGMT\_LAYER\_CODE\_COAP

CoAP layer code.

**Definition** net\_mgmt.h:78

[NET\_MGMT\_LAYER\_CODE\_WIFI](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789)

@ NET\_MGMT\_LAYER\_CODE\_WIFI

Wi-Fi layer code.

**Definition** net\_mgmt.h:85

[NET\_MGMT\_LAYER\_CODE\_IPV6](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8)

@ NET\_MGMT\_LAYER\_CODE\_IPV6

IPv6 layer code.

**Definition** net\_mgmt.h:76

[NET\_MGMT\_LAYER\_CODE\_USER2](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4)

@ NET\_MGMT\_LAYER\_CODE\_USER2

User layer code 2.

**Definition** net\_mgmt.h:89

[NET\_MGMT\_LAYER\_CODE\_L4](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e)

@ NET\_MGMT\_LAYER\_CODE\_L4

L4 layer code.

**Definition** net\_mgmt.h:77

[NET\_MGMT\_LAYER\_CODE\_CONN](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7)

@ NET\_MGMT\_LAYER\_CODE\_CONN

Connectivity layer code.

**Definition** net\_mgmt.h:74

[NET\_MGMT\_LAYER\_CODE\_VIRTUAL](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca)

@ NET\_MGMT\_LAYER\_CODE\_VIRTUAL

Virtual network interface layer code.

**Definition** net\_mgmt.h:84

[NET\_MGMT\_LAYER\_CODE\_RESERVED](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75)

@ NET\_MGMT\_LAYER\_CODE\_RESERVED

Reserved layer code for future use.

**Definition** net\_mgmt.h:93

[NET\_MGMT\_LAYER\_CODE\_ETHERNET](group__net__mgmt.md#gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4)

@ NET\_MGMT\_LAYER\_CODE\_ETHERNET

Ethernet layer code.

**Definition** net\_mgmt.h:81

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_event.h](net__event_8h.md)

Network Events code public header.

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

[net\_mgmt\_event\_callback](structnet__mgmt__event__callback.md)

Network Management event callback structure Used to register a callback into the network management e...

**Definition** net\_mgmt.h:163

[net\_mgmt\_event\_callback::node](structnet__mgmt__event__callback.md#a05a4f445731f9f72209a652f2653e1ea)

sys\_snode\_t node

Meant to be used internally, to insert the callback into a list.

**Definition** net\_mgmt.h:167

[net\_mgmt\_event\_callback::raised\_event](structnet__mgmt__event__callback.md#a555d868d6a0d6ecb04d09607fab06b79)

uint64\_t raised\_event

Internal place holder when a synchronous event wait is successfully unlocked on a event.

**Definition** net\_mgmt.h:202

[net\_mgmt\_event\_callback::sync\_call](structnet__mgmt__event__callback.md#a7403d98fe528c492a4b1b449b43c10d3)

struct k\_sem \* sync\_call

Semaphore meant to be used internally for the synchronous net\_mgmt\_event\_wait() function.

**Definition** net\_mgmt.h:176

[net\_mgmt\_event\_callback::event\_mask](structnet__mgmt__event__callback.md#a99e3174c1052488877b3db6349de61e8)

uint64\_t event\_mask

A mask of network events on which the above handler should be called in case those events come.

**Definition** net\_mgmt.h:198

[net\_mgmt\_event\_callback::handler](structnet__mgmt__event__callback.md#ada57aabc8acc3e9be93fb2726321f1b2)

net\_mgmt\_event\_handler\_t handler

Actual callback function being used to notify the owner.

**Definition** net\_mgmt.h:172

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_mgmt.h](net__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
