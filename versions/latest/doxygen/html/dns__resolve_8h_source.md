---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dns__resolve_8h_source.html
original_path: doxygen/html/dns__resolve_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_resolve.h

[Go to the documentation of this file.](dns__resolve_8h.md)

1

6

7/\*

8 \* Copyright (c) 2017 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_DNS\_RESOLVE\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_DNS\_RESOLVE\_H\_

15

16#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

17#include <[zephyr/net/net\_context.h](net__context_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

[ 33](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0)enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) {

[ 35](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134) [DNS\_QUERY\_TYPE\_A](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134) = 1,

[ 37](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049) [DNS\_QUERY\_TYPE\_AAAA](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049) = 28

38};

39

41#ifndef DNS\_MAX\_NAME\_SIZE

[ 42](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db)#define DNS\_MAX\_NAME\_SIZE 20

43#endif

44

46

47/\* Make sure that we can compile things even if CONFIG\_DNS\_RESOLVER

48 \* is not enabled.

49 \*/

50#if !defined(CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS)

51#define CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS 1

52#endif

53#if !defined(CONFIG\_DNS\_NUM\_CONCUR\_QUERIES)

54#define CONFIG\_DNS\_NUM\_CONCUR\_QUERIES 1

55#endif

56

57/\* If mDNS is enabled, then add some extra well known multicast servers to the

58 \* server list.

59 \*/

60#if defined(CONFIG\_MDNS\_RESOLVER)

61#if defined(CONFIG\_NET\_IPV6) && defined(CONFIG\_NET\_IPV4)

62#define MDNS\_SERVER\_COUNT 2

63#else

64#define MDNS\_SERVER\_COUNT 1

65#endif /\* CONFIG\_NET\_IPV6 && CONFIG\_NET\_IPV4 \*/

66#else

67#define MDNS\_SERVER\_COUNT 0

68#endif /\* CONFIG\_MDNS\_RESOLVER \*/

69

70/\* If LLMNR is enabled, then add some extra well known multicast servers to the

71 \* server list.

72 \*/

73#if defined(CONFIG\_LLMNR\_RESOLVER)

74#if defined(CONFIG\_NET\_IPV6) && defined(CONFIG\_NET\_IPV4)

75#define LLMNR\_SERVER\_COUNT 2

76#else

77#define LLMNR\_SERVER\_COUNT 1

78#endif /\* CONFIG\_NET\_IPV6 && CONFIG\_NET\_IPV4 \*/

79#else

80#define LLMNR\_SERVER\_COUNT 0

81#endif /\* CONFIG\_MDNS\_RESOLVER \*/

82

83#define DNS\_MAX\_MCAST\_SERVERS (MDNS\_SERVER\_COUNT + LLMNR\_SERVER\_COUNT)

84

86

[ 90](structdns__addrinfo.md)struct [dns\_addrinfo](structdns__addrinfo.md) {

[ 91](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37) struct [sockaddr](structsockaddr.md) [ai\_addr](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37);

[ 92](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [ai\_addrlen](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799);

[ 93](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ai\_family](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558);

[ 94](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce) char [ai\_canonname](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce)[[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db) + 1];

95};

96

[ 100](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e)enum [dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) {

102 DNS\_EAI\_BADFLAGS = -1,

[ 104](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) = -2,

[ 106](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) = -3,

[ 108](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) = -4,

[ 110](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) = -5,

112 DNS\_EAI\_FAMILY = -6,

114 DNS\_EAI\_SOCKTYPE = -7,

116 DNS\_EAI\_SERVICE = -8,

[ 118](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d) [DNS\_EAI\_ADDRFAMILY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d) = -9,

[ 120](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) = -10,

122 DNS\_EAI\_SYSTEM = -11,

[ 124](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) [DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) = -12,

[ 126](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3) [DNS\_EAI\_INPROGRESS](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3) = -100,

[ 128](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3) [DNS\_EAI\_CANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3) = -101,

[ 130](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f) [DNS\_EAI\_NOTCANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f) = -102,

[ 132](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836) [DNS\_EAI\_ALLDONE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836) = -103,

[ 134](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4) [DNS\_EAI\_IDN\_ENCODE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4) = -105,

135};

136

[ 156](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722)typedef void (\*[dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722))(enum [dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) status,

157 struct [dns\_addrinfo](structdns__addrinfo.md) \*info,

158 void \*user\_data);

159

[ 160](group__dns__resolve.md#gaf190da074df1b14130c0af6370bbd56c)enum [dns\_resolve\_context\_state](group__dns__resolve.md#gaf190da074df1b14130c0af6370bbd56c) {

[ 161](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56cab4bde91ceae9786f84712e7bd20ab994) [DNS\_RESOLVE\_CONTEXT\_ACTIVE](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56cab4bde91ceae9786f84712e7bd20ab994),

[ 162](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56ca776ec347989a1bb2cee6242720a321fa) [DNS\_RESOLVE\_CONTEXT\_DEACTIVATING](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56ca776ec347989a1bb2cee6242720a321fa),

[ 163](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56ca2ff3849fda38c36c3859b08562f35708) [DNS\_RESOLVE\_CONTEXT\_INACTIVE](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56ca2ff3849fda38c36c3859b08562f35708),

164};

165

[ 169](structdns__resolve__context.md)struct [dns\_resolve\_context](structdns__resolve__context.md) {

170 struct {

[ 172](structdns__resolve__context.md#ae54aa9bc3b76924193c0846976ee089b) struct [sockaddr](structsockaddr.md) [dns\_server](structdns__resolve__context.md#ae54aa9bc3b76924193c0846976ee089b);

173

[ 175](structdns__resolve__context.md#abdc166e878040d90362366251730e6df) struct [net\_context](structnet__context.md) \*[net\_ctx](structdns__resolve__context.md#abdc166e878040d90362366251730e6df);

176

[ 178](structdns__resolve__context.md#aa6c01844428450cf96c306feb35d491e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_mdns](structdns__resolve__context.md#aa6c01844428450cf96c306feb35d491e) : 1;

179

[ 181](structdns__resolve__context.md#a503502ac58538d54fddce34e7ae71f2e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_llmnr](structdns__resolve__context.md#a503502ac58538d54fddce34e7ae71f2e) : 1;

[ 182](structdns__resolve__context.md#aade0d00fa46d1567b94491733b268d99) } [servers](structdns__resolve__context.md#aade0d00fa46d1567b94491733b268d99)[CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS + DNS\_MAX\_MCAST\_SERVERS];

183

[ 185](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7) struct [k\_mutex](structk__mutex.md) [lock](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7);

186

[ 190](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6) [k\_timeout\_t](structk__timeout__t.md) [buf\_timeout](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6);

191

[ 198](structdns__resolve__context_1_1dns__pending__query.md) struct [dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) {

[ 200](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230) struct [k\_work\_delayable](structk__work__delayable.md) [timer](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230);

201

[ 203](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae) struct [dns\_resolve\_context](structdns__resolve__context.md) \*[ctx](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae);

204

[ 209](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0) [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) [cb](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0);

210

[ 212](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343) void \*[user\_data](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343);

213

[ 215](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5) [k\_timeout\_t](structk__timeout__t.md) [timeout](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5);

216

[ 228](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b) const char \*[query](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b);

229

[ 231](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78) enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) [query\_type](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78);

232

[ 234](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173);

235

[ 242](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [query\_hash](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1);

[ 243](structdns__resolve__context.md#a3bec79837b0bce3fd99b29bfbe1da40d) } [queries](structdns__resolve__context.md#a3bec79837b0bce3fd99b29bfbe1da40d)[CONFIG\_DNS\_NUM\_CONCUR\_QUERIES];

244

[ 246](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a) enum [dns\_resolve\_context\_state](group__dns__resolve.md#gaf190da074df1b14130c0af6370bbd56c) [state](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a);

247};

248

[ 276](group__dns__resolve.md#ga74e2be49894100fe5da641331ef083de)int [dns\_resolve\_init](group__dns__resolve.md#ga74e2be49894100fe5da641331ef083de)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

277 const char \*dns\_servers\_str[],

278 const struct [sockaddr](structsockaddr.md) \*dns\_servers\_sa[]);

279

[ 287](group__dns__resolve.md#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)int [dns\_resolve\_init\_default](group__dns__resolve.md#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx);

288

[ 299](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc)int [dns\_resolve\_close](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx);

300

[ 320](group__dns__resolve.md#ga9da2d7299cfafcdea7d6bfe0e4a2223c)int [dns\_resolve\_reconfigure](group__dns__resolve.md#ga9da2d7299cfafcdea7d6bfe0e4a2223c)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

321 const char \*servers\_str[],

322 const struct [sockaddr](structsockaddr.md) \*servers\_sa[]);

323

[ 334](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)int [dns\_resolve\_cancel](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

335 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id);

336

[ 349](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)int [dns\_resolve\_cancel\_with\_name](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

350 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id,

351 const char \*query\_name,

352 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) query\_type);

353

[ 381](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)int [dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

382 const char \*query,

383 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) type,

384 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id,

385 [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb,

386 void \*user\_data,

387 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

388

[ 399](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)struct [dns\_resolve\_context](structdns__resolve__context.md) \*[dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(void);

400

[ 428](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)static inline int [dns\_get\_addr\_info](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)(const char \*query,

429 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) type,

430 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id,

431 [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb,

432 void \*user\_data,

433 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

434{

435 return [dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)([dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(),

436 query,

437 type,

438 dns\_id,

439 cb,

440 user\_data,

441 timeout);

442}

443

[ 453](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)static inline int [dns\_cancel\_addr\_info](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id)

454{

455 return [dns\_resolve\_cancel](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)([dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(), dns\_id);

456}

457

461

463

467#if defined(CONFIG\_DNS\_RESOLVER\_AUTO\_INIT)

468void dns\_init\_resolver(void);

469

470#else

471#define dns\_init\_resolver(...)

472#endif /\* CONFIG\_DNS\_RESOLVER\_AUTO\_INIT \*/

473

475

476#ifdef \_\_cplusplus

477}

478#endif

479

480#endif /\* ZEPHYR\_INCLUDE\_NET\_DNS\_RESOLVE\_H\_ \*/

[dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)

int dns\_resolve\_name(struct dns\_resolve\_context \*ctx, const char \*query, enum dns\_query\_type type, uint16\_t \*dns\_id, dns\_resolve\_cb\_t cb, void \*user\_data, int32\_t timeout)

Resolve DNS name.

[dns\_cancel\_addr\_info](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)

static int dns\_cancel\_addr\_info(uint16\_t dns\_id)

Cancel a pending DNS query.

**Definition** dns\_resolve.h:453

[dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e)

dns\_resolve\_status

Status values for the callback.

**Definition** dns\_resolve.h:100

[dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0)

dns\_query\_type

DNS query type enum.

**Definition** dns\_resolve.h:33

[dns\_resolve\_init\_default](group__dns__resolve.md#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)

int dns\_resolve\_init\_default(struct dns\_resolve\_context \*ctx)

Init DNS resolving context with default Kconfig options.

[dns\_resolve\_init](group__dns__resolve.md#ga74e2be49894100fe5da641331ef083de)

int dns\_resolve\_init(struct dns\_resolve\_context \*ctx, const char \*dns\_servers\_str[], const struct sockaddr \*dns\_servers\_sa[])

Init DNS resolving context.

[dns\_resolve\_cancel](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)

int dns\_resolve\_cancel(struct dns\_resolve\_context \*ctx, uint16\_t dns\_id)

Cancel a pending DNS query.

[dns\_resolve\_reconfigure](group__dns__resolve.md#ga9da2d7299cfafcdea7d6bfe0e4a2223c)

int dns\_resolve\_reconfigure(struct dns\_resolve\_context \*ctx, const char \*servers\_str[], const struct sockaddr \*servers\_sa[])

Reconfigure DNS resolving context.

[dns\_resolve\_close](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc)

int dns\_resolve\_close(struct dns\_resolve\_context \*ctx)

Close DNS resolving context.

[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db)

#define DNS\_MAX\_NAME\_SIZE

Max size of the resolved name.

**Definition** dns\_resolve.h:42

[dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)

struct dns\_resolve\_context \* dns\_resolve\_get\_default(void)

Get default DNS context.

[dns\_resolve\_context\_state](group__dns__resolve.md#gaf190da074df1b14130c0af6370bbd56c)

dns\_resolve\_context\_state

**Definition** dns\_resolve.h:160

[dns\_resolve\_cancel\_with\_name](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)

int dns\_resolve\_cancel\_with\_name(struct dns\_resolve\_context \*ctx, uint16\_t dns\_id, const char \*query\_name, enum dns\_query\_type query\_type)

Cancel a pending DNS query using id, name and type.

[dns\_get\_addr\_info](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)

static int dns\_get\_addr\_info(const char \*query, enum dns\_query\_type type, uint16\_t \*dns\_id, dns\_resolve\_cb\_t cb, void \*user\_data, int32\_t timeout)

Get IP address info from DNS.

**Definition** dns\_resolve.h:428

[dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722)

void(\* dns\_resolve\_cb\_t)(enum dns\_resolve\_status status, struct dns\_addrinfo \*info, void \*user\_data)

DNS resolve callback.

**Definition** dns\_resolve.h:156

[DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)

@ DNS\_EAI\_MEMORY

Memory allocation failure.

**Definition** dns\_resolve.h:120

[DNS\_EAI\_NOTCANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f)

@ DNS\_EAI\_NOTCANCELED

Request not canceled.

**Definition** dns\_resolve.h:130

[DNS\_EAI\_IDN\_ENCODE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4)

@ DNS\_EAI\_IDN\_ENCODE

IDN encoding failed.

**Definition** dns\_resolve.h:134

[DNS\_EAI\_ADDRFAMILY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d)

@ DNS\_EAI\_ADDRFAMILY

ai\_family' not supported \*/ DNS\_EAI\_FAMILY = -6, /\*\* ai\_socktype' not supported \*/ DNS\_EAI\_SOCKTYPE =...

**Definition** dns\_resolve.h:118

[DNS\_EAI\_INPROGRESS](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3)

@ DNS\_EAI\_INPROGRESS

Processing request in progress.

**Definition** dns\_resolve.h:126

[DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)

@ DNS\_EAI\_FAIL

Non-recoverable failure in name res.

**Definition** dns\_resolve.h:108

[DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)

@ DNS\_EAI\_AGAIN

Temporary failure in name resolution.

**Definition** dns\_resolve.h:106

[DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)

@ DNS\_EAI\_NODATA

No address associated with NAME.

**Definition** dns\_resolve.h:110

[DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)

@ DNS\_EAI\_NONAME

Invalid value for `ai\_flags' field \*/ DNS\_EAI\_BADFLAGS = -1, /\*\* NAME or SERVICE is unknown.

**Definition** dns\_resolve.h:104

[DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)

@ DNS\_EAI\_OVERFLOW

System error returned in `errno' \*/ DNS\_EAI\_SYSTEM = -11, /\*\* Argument buffer overflow.

**Definition** dns\_resolve.h:124

[DNS\_EAI\_CANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3)

@ DNS\_EAI\_CANCELED

Request canceled.

**Definition** dns\_resolve.h:128

[DNS\_EAI\_ALLDONE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836)

@ DNS\_EAI\_ALLDONE

All requests done.

**Definition** dns\_resolve.h:132

[DNS\_QUERY\_TYPE\_A](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134)

@ DNS\_QUERY\_TYPE\_A

IPv4 query.

**Definition** dns\_resolve.h:35

[DNS\_QUERY\_TYPE\_AAAA](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049)

@ DNS\_QUERY\_TYPE\_AAAA

IPv6 query.

**Definition** dns\_resolve.h:37

[DNS\_RESOLVE\_CONTEXT\_INACTIVE](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56ca2ff3849fda38c36c3859b08562f35708)

@ DNS\_RESOLVE\_CONTEXT\_INACTIVE

**Definition** dns\_resolve.h:163

[DNS\_RESOLVE\_CONTEXT\_DEACTIVATING](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56ca776ec347989a1bb2cee6242720a321fa)

@ DNS\_RESOLVE\_CONTEXT\_DEACTIVATING

**Definition** dns\_resolve.h:162

[DNS\_RESOLVE\_CONTEXT\_ACTIVE](group__dns__resolve.md#ggaf190da074df1b14130c0af6370bbd56cab4bde91ceae9786f84712e7bd20ab994)

@ DNS\_RESOLVE\_CONTEXT\_ACTIVE

**Definition** dns\_resolve.h:161

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[net\_context.h](net__context_8h.md)

Network context definitions.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[dns\_addrinfo](structdns__addrinfo.md)

Address info struct is passed to callback that gets all the results.

**Definition** dns\_resolve.h:90

[dns\_addrinfo::ai\_canonname](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce)

char ai\_canonname[20+1]

**Definition** dns\_resolve.h:94

[dns\_addrinfo::ai\_addr](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37)

struct sockaddr ai\_addr

**Definition** dns\_resolve.h:91

[dns\_addrinfo::ai\_addrlen](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799)

socklen\_t ai\_addrlen

**Definition** dns\_resolve.h:92

[dns\_addrinfo::ai\_family](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558)

uint8\_t ai\_family

**Definition** dns\_resolve.h:93

[dns\_resolve\_context::dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md)

Result callbacks.

**Definition** dns\_resolve.h:198

[dns\_resolve\_context::dns\_pending\_query::query](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b)

const char \* query

String containing the thing to resolve like www.example.com.

**Definition** dns\_resolve.h:228

[dns\_resolve\_context::dns\_pending\_query::query\_hash](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1)

uint16\_t query\_hash

Hash of the DNS name + query type we are querying.

**Definition** dns\_resolve.h:242

[dns\_resolve\_context::dns\_pending\_query::ctx](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae)

struct dns\_resolve\_context \* ctx

Back pointer to ctx, needed in timeout handler.

**Definition** dns\_resolve.h:203

[dns\_resolve\_context::dns\_pending\_query::user\_data](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343)

void \* user\_data

User data.

**Definition** dns\_resolve.h:212

[dns\_resolve\_context::dns\_pending\_query::timer](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230)

struct k\_work\_delayable timer

Timeout timer.

**Definition** dns\_resolve.h:200

[dns\_resolve\_context::dns\_pending\_query::id](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173)

uint16\_t id

DNS id of this query.

**Definition** dns\_resolve.h:234

[dns\_resolve\_context::dns\_pending\_query::timeout](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5)

k\_timeout\_t timeout

TX timeout.

**Definition** dns\_resolve.h:215

[dns\_resolve\_context::dns\_pending\_query::cb](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0)

dns\_resolve\_cb\_t cb

Result callback.

**Definition** dns\_resolve.h:209

[dns\_resolve\_context::dns\_pending\_query::query\_type](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78)

enum dns\_query\_type query\_type

Query type.

**Definition** dns\_resolve.h:231

[dns\_resolve\_context](structdns__resolve__context.md)

DNS resolve context structure.

**Definition** dns\_resolve.h:169

[dns\_resolve\_context::queries](structdns__resolve__context.md#a3bec79837b0bce3fd99b29bfbe1da40d)

struct dns\_resolve\_context::dns\_pending\_query queries[CONFIG\_DNS\_NUM\_CONCUR\_QUERIES]

[dns\_resolve\_context::buf\_timeout](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6)

k\_timeout\_t buf\_timeout

This timeout is also used when a buffer is required from the buffer pools.

**Definition** dns\_resolve.h:190

[dns\_resolve\_context::is\_llmnr](structdns__resolve__context.md#a503502ac58538d54fddce34e7ae71f2e)

uint8\_t is\_llmnr

Is this server LLMNR one.

**Definition** dns\_resolve.h:181

[dns\_resolve\_context::state](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a)

enum dns\_resolve\_context\_state state

Is this context in use.

**Definition** dns\_resolve.h:246

[dns\_resolve\_context::lock](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7)

struct k\_mutex lock

Prevent concurrent access.

**Definition** dns\_resolve.h:185

[dns\_resolve\_context::is\_mdns](structdns__resolve__context.md#aa6c01844428450cf96c306feb35d491e)

uint8\_t is\_mdns

Is this server mDNS one.

**Definition** dns\_resolve.h:178

[dns\_resolve\_context::servers](structdns__resolve__context.md#aade0d00fa46d1567b94491733b268d99)

struct dns\_resolve\_context::@055260037137365310177266015141315371120104012124 servers[CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS+DNS\_MAX\_MCAST\_SERVERS]

[dns\_resolve\_context::net\_ctx](structdns__resolve__context.md#abdc166e878040d90362366251730e6df)

struct net\_context \* net\_ctx

Connection to the DNS server.

**Definition** dns\_resolve.h:175

[dns\_resolve\_context::dns\_server](structdns__resolve__context.md#ae54aa9bc3b76924193c0846976ee089b)

struct sockaddr dns\_server

DNS server information.

**Definition** dns\_resolve.h:172

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3889

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:201

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dns\_resolve.h](dns__resolve_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
