---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dns__resolve_8h_source.html
original_path: doxygen/html/dns__resolve_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

16#include <[zephyr/kernel.h](kernel_8h.md)>

17#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

18#include <[zephyr/net/net\_if.h](net__if_8h.md)>

19#include <[zephyr/net/socket\_poll.h](socket__poll_8h.md)>

20#include <[zephyr/net/net\_core.h](net__core_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

34

[ 38](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0)enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) {

[ 40](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134) [DNS\_QUERY\_TYPE\_A](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134) = 1,

[ 42](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049) [DNS\_QUERY\_TYPE\_AAAA](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049) = 28

43};

44

46#ifndef DNS\_MAX\_NAME\_SIZE

[ 47](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db)#define DNS\_MAX\_NAME\_SIZE 20

48#endif

49

51

52#define DNS\_BUF\_TIMEOUT K\_MSEC(500) /\* ms \*/

53

54/\* This value is recommended by RFC 1035 \*/

55#define DNS\_RESOLVER\_MAX\_BUF\_SIZE 512

56

57/\* Make sure that we can compile things even if CONFIG\_DNS\_RESOLVER

58 \* is not enabled.

59 \*/

60#if defined(CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS)

61#define DNS\_RESOLVER\_MAX\_SERVERS CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS

62#else

63#define DNS\_RESOLVER\_MAX\_SERVERS 0

64#endif

65

66#if defined(CONFIG\_DNS\_NUM\_CONCUR\_QUERIES)

67#define DNS\_NUM\_CONCUR\_QUERIES CONFIG\_DNS\_NUM\_CONCUR\_QUERIES

68#else

69#define DNS\_NUM\_CONCUR\_QUERIES 1

70#endif

71

72#if defined(CONFIG\_NET\_IF\_MAX\_IPV6\_COUNT)

73#define MAX\_IPV6\_IFACE\_COUNT CONFIG\_NET\_IF\_MAX\_IPV6\_COUNT

74#else

75#define MAX\_IPV6\_IFACE\_COUNT 1

76#endif

77

78#if defined(CONFIG\_NET\_IF\_MAX\_IPV4\_COUNT)

79#define MAX\_IPV4\_IFACE\_COUNT CONFIG\_NET\_IF\_MAX\_IPV4\_COUNT

80#else

81#define MAX\_IPV4\_IFACE\_COUNT 1

82#endif

83

84/\* If mDNS is enabled, then add some extra well known multicast servers to the

85 \* server list.

86 \*/

87#if defined(CONFIG\_MDNS\_RESOLVER)

88#if defined(CONFIG\_NET\_IPV6) && defined(CONFIG\_NET\_IPV4)

89#define MDNS\_SERVER\_COUNT 2

90#else

91#define MDNS\_SERVER\_COUNT 1

92#endif /\* CONFIG\_NET\_IPV6 && CONFIG\_NET\_IPV4 \*/

93#else

94#define MDNS\_SERVER\_COUNT 0

95#endif /\* CONFIG\_MDNS\_RESOLVER \*/

96

97/\* If LLMNR is enabled, then add some extra well known multicast servers to the

98 \* server list.

99 \*/

100#if defined(CONFIG\_LLMNR\_RESOLVER)

101#if defined(CONFIG\_NET\_IPV6) && defined(CONFIG\_NET\_IPV4)

102#define LLMNR\_SERVER\_COUNT 2

103#else

104#define LLMNR\_SERVER\_COUNT 1

105#endif /\* CONFIG\_NET\_IPV6 && CONFIG\_NET\_IPV4 \*/

106#else

107#define LLMNR\_SERVER\_COUNT 0

108#endif /\* CONFIG\_MDNS\_RESOLVER \*/

109

110#define DNS\_MAX\_MCAST\_SERVERS (MDNS\_SERVER\_COUNT + LLMNR\_SERVER\_COUNT)

111

112#if defined(CONFIG\_MDNS\_RESPONDER)

113#if defined(CONFIG\_NET\_IPV6)

114#define MDNS\_MAX\_IPV6\_IFACE\_COUNT CONFIG\_NET\_IF\_MAX\_IPV6\_COUNT

115#else

116#define MDNS\_MAX\_IPV6\_IFACE\_COUNT 0

117#endif /\* CONFIG\_NET\_IPV6 \*/

118

119#if defined(CONFIG\_NET\_IPV4)

120#define MDNS\_MAX\_IPV4\_IFACE\_COUNT CONFIG\_NET\_IF\_MAX\_IPV4\_COUNT

121#else

122#define MDNS\_MAX\_IPV4\_IFACE\_COUNT 0

123#endif /\* CONFIG\_NET\_IPV4 \*/

124

125#define MDNS\_MAX\_POLL (MDNS\_MAX\_IPV4\_IFACE\_COUNT + MDNS\_MAX\_IPV6\_IFACE\_COUNT)

126#else

127#define MDNS\_MAX\_POLL 0

128#endif /\* CONFIG\_MDNS\_RESPONDER \*/

129

130#if defined(CONFIG\_LLMNR\_RESPONDER)

131#if defined(CONFIG\_NET\_IPV6) && defined(CONFIG\_NET\_IPV4)

132#define LLMNR\_MAX\_POLL 2

133#else

134#define LLMNR\_MAX\_POLL 1

135#endif

136#else

137#define LLMNR\_MAX\_POLL 0

138#endif /\* CONFIG\_LLMNR\_RESPONDER \*/

139

140#define DNS\_RESOLVER\_MAX\_POLL (DNS\_RESOLVER\_MAX\_SERVERS + DNS\_MAX\_MCAST\_SERVERS)

141

143#define DNS\_DISPATCHER\_MAX\_POLL (DNS\_RESOLVER\_MAX\_POLL + MDNS\_MAX\_POLL + LLMNR\_MAX\_POLL)

144

145#if defined(CONFIG\_ZVFS\_POLL\_MAX)

146BUILD\_ASSERT(CONFIG\_ZVFS\_POLL\_MAX >= DNS\_DISPATCHER\_MAX\_POLL,

147 "CONFIG\_ZVFS\_POLL\_MAX must be larger than " [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(DNS\_DISPATCHER\_MAX\_POLL));

148#endif

149

153enum dns\_socket\_type {

154 DNS\_SOCKET\_RESOLVER = 1,

155 DNS\_SOCKET\_RESPONDER = 2

156};

157

158struct [dns\_resolve\_context](structdns__resolve__context.md);

159struct mdns\_responder\_context;

160struct dns\_socket\_dispatcher;

161

176typedef int (\*dns\_socket\_dispatcher\_cb)(struct dns\_socket\_dispatcher \*ctx, int sock,

177 struct [sockaddr](structsockaddr.md) \*addr, size\_t addrlen,

178 struct [net\_buf](structnet__buf.md) \*buf, size\_t data\_len);

179

181struct dns\_socket\_dispatcher {

183 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

185 const struct net\_socket\_service\_desc \*svc;

189 union {

190 void \*ctx;

191 struct dns\_resolve\_context \*resolve\_ctx;

192 struct mdns\_responder\_context \*mdns\_ctx;

193 };

194

196 enum dns\_socket\_type type;

198 struct sockaddr local\_addr;

200 dns\_socket\_dispatcher\_cb cb;

202 struct zsock\_pollfd \*fds;

204 int fds\_len;

206 int sock;

208 int ifindex;

212 struct dns\_socket\_dispatcher \*pair;

214 struct k\_mutex lock;

216 k\_timeout\_t buf\_timeout;

217};

218

228int dns\_dispatcher\_register(struct dns\_socket\_dispatcher \*ctx);

229

239int dns\_dispatcher\_unregister(struct dns\_socket\_dispatcher \*ctx);

240

242

[ 246](structdns__addrinfo.md)struct [dns\_addrinfo](structdns__addrinfo.md) {

[ 248](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37) struct [sockaddr](structsockaddr.md) [ai\_addr](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37);

[ 250](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [ai\_addrlen](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799);

[ 252](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ai\_family](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558);

[ 254](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce) char [ai\_canonname](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce)[[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db) + 1];

255};

256

[ 260](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e)enum [dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) {

262 DNS\_EAI\_BADFLAGS = -1,

[ 264](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) = -2,

[ 266](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) = -3,

[ 268](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) = -4,

[ 270](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) = -5,

272 DNS\_EAI\_FAMILY = -6,

274 DNS\_EAI\_SOCKTYPE = -7,

276 DNS\_EAI\_SERVICE = -8,

[ 278](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d) [DNS\_EAI\_ADDRFAMILY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d) = -9,

[ 280](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) = -10,

282 DNS\_EAI\_SYSTEM = -11,

[ 284](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) [DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) = -12,

[ 286](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3) [DNS\_EAI\_INPROGRESS](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3) = -100,

[ 288](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3) [DNS\_EAI\_CANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3) = -101,

[ 290](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f) [DNS\_EAI\_NOTCANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f) = -102,

[ 292](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836) [DNS\_EAI\_ALLDONE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836) = -103,

[ 294](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4) [DNS\_EAI\_IDN\_ENCODE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4) = -105,

295};

296

[ 316](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722)typedef void (\*[dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722))(enum [dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) status,

317 struct [dns\_addrinfo](structdns__addrinfo.md) \*info,

318 void \*user\_data);

319

321

322enum dns\_resolve\_context\_state {

323 DNS\_RESOLVE\_CONTEXT\_ACTIVE,

324 DNS\_RESOLVE\_CONTEXT\_DEACTIVATING,

325 DNS\_RESOLVE\_CONTEXT\_INACTIVE,

326};

327

329

[ 333](structdns__resolve__context.md)struct [dns\_resolve\_context](structdns__resolve__context.md) {

[ 335](structdns__resolve__context_1_1dns__server.md) struct [dns\_server](structdns__resolve__context_1_1dns__server.md#a266b91e051fd7c1b1e434e1a3ab4b5dc) {

[ 337](structdns__resolve__context_1_1dns__server.md#a266b91e051fd7c1b1e434e1a3ab4b5dc) struct [sockaddr](structsockaddr.md) [dns\_server](structdns__resolve__context_1_1dns__server.md#a266b91e051fd7c1b1e434e1a3ab4b5dc);

338

[ 340](structdns__resolve__context_1_1dns__server.md#a762f6cbc4fabe1809966f62d7aa760a6) int [sock](structdns__resolve__context_1_1dns__server.md#a762f6cbc4fabe1809966f62d7aa760a6);

341

[ 345](structdns__resolve__context_1_1dns__server.md#a6b544dc78ee42cd51d2a9404bf69ca06) int [if\_index](structdns__resolve__context_1_1dns__server.md#a6b544dc78ee42cd51d2a9404bf69ca06);

346

[ 348](structdns__resolve__context_1_1dns__server.md#aaa3606fb80fa171a3b4b91fa0441129f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_mdns](structdns__resolve__context_1_1dns__server.md#aaa3606fb80fa171a3b4b91fa0441129f) : 1;

349

[ 351](structdns__resolve__context_1_1dns__server.md#af60096f20c95a112caf4f946d898ec70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_llmnr](structdns__resolve__context_1_1dns__server.md#af60096f20c95a112caf4f946d898ec70) : 1;

352

355 struct dns\_socket\_dispatcher dispatcher;

[ 357](structdns__resolve__context.md#a81becba86317bbd32d384ff2e677c829) } [servers](structdns__resolve__context.md#a81becba86317bbd32d384ff2e677c829)[DNS\_RESOLVER\_MAX\_POLL];

358

361 struct [zsock\_pollfd](structzsock__pollfd.md) fds[DNS\_RESOLVER\_MAX\_POLL];

363

[ 365](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7) struct [k\_mutex](structk__mutex.md) [lock](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7);

366

[ 370](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6) [k\_timeout\_t](structk__timeout__t.md) [buf\_timeout](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6);

371

[ 378](structdns__resolve__context_1_1dns__pending__query.md) struct [dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) {

[ 380](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230) struct [k\_work\_delayable](structk__work__delayable.md) [timer](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230);

381

[ 383](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae) struct [dns\_resolve\_context](structdns__resolve__context.md) \*[ctx](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae);

384

[ 389](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0) [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) [cb](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0);

390

[ 392](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343) void \*[user\_data](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343);

393

[ 395](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5) [k\_timeout\_t](structk__timeout__t.md) [timeout](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5);

396

[ 408](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b) const char \*[query](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b);

409

[ 411](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78) enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) [query\_type](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78);

412

[ 414](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173);

415

[ 422](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [query\_hash](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1);

[ 423](structdns__resolve__context.md#a596053473b44be4977947632a1abb51e) } [queries](structdns__resolve__context.md#a596053473b44be4977947632a1abb51e)[DNS\_NUM\_CONCUR\_QUERIES];

424

[ 426](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a) enum dns\_resolve\_context\_state [state](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a);

427};

428

430

431struct mdns\_probe\_user\_data {

432 struct mdns\_responder\_context \*ctx;

433 char query[[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db) + 1];

434 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id;

435};

436

437struct mdns\_responder\_context {

438 struct sockaddr server\_addr;

439 struct dns\_socket\_dispatcher dispatcher;

440 struct zsock\_pollfd fds[1];

441 int sock;

442 struct net\_if \*iface;

443#if defined(CONFIG\_MDNS\_RESPONDER\_PROBE)

444 struct k\_work\_delayable probe\_timer;

445 struct dns\_resolve\_context probe\_ctx;

446 struct mdns\_probe\_user\_data probe\_data;

447#endif

448};

449

451

[ 479](group__dns__resolve.md#ga74e2be49894100fe5da641331ef083de)int [dns\_resolve\_init](group__dns__resolve.md#ga74e2be49894100fe5da641331ef083de)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

480 const char \*dns\_servers\_str[],

481 const struct [sockaddr](structsockaddr.md) \*dns\_servers\_sa[]);

482

[ 490](group__dns__resolve.md#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)int [dns\_resolve\_init\_default](group__dns__resolve.md#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx);

491

[ 502](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc)int [dns\_resolve\_close](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx);

503

[ 523](group__dns__resolve.md#ga9da2d7299cfafcdea7d6bfe0e4a2223c)int [dns\_resolve\_reconfigure](group__dns__resolve.md#ga9da2d7299cfafcdea7d6bfe0e4a2223c)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

524 const char \*servers\_str[],

525 const struct [sockaddr](structsockaddr.md) \*servers\_sa[]);

526

[ 537](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)int [dns\_resolve\_cancel](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

538 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id);

539

[ 552](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)int [dns\_resolve\_cancel\_with\_name](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

553 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id,

554 const char \*query\_name,

555 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) query\_type);

556

[ 584](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)int [dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

585 const char \*query,

586 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) type,

587 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id,

588 [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb,

589 void \*user\_data,

590 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

591

[ 602](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)struct [dns\_resolve\_context](structdns__resolve__context.md) \*[dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(void);

603

[ 631](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)static inline int [dns\_get\_addr\_info](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)(const char \*query,

632 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) type,

633 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id,

634 [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb,

635 void \*user\_data,

636 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

637{

638 return [dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)([dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(),

639 query,

640 type,

641 dns\_id,

642 cb,

643 user\_data,

644 timeout);

645}

646

[ 656](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)static inline int [dns\_cancel\_addr\_info](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id)

657{

658 return [dns\_resolve\_cancel](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)([dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(), dns\_id);

659}

660

664

666

670#if defined(CONFIG\_DNS\_RESOLVER\_AUTO\_INIT)

671void dns\_init\_resolver(void);

672

673#else

674#define dns\_init\_resolver(...)

675#endif /\* CONFIG\_DNS\_RESOLVER\_AUTO\_INIT \*/

676

678

679#ifdef \_\_cplusplus

680}

681#endif

682

683#endif /\* ZEPHYR\_INCLUDE\_NET\_DNS\_RESOLVE\_H\_ \*/

[dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)

int dns\_resolve\_name(struct dns\_resolve\_context \*ctx, const char \*query, enum dns\_query\_type type, uint16\_t \*dns\_id, dns\_resolve\_cb\_t cb, void \*user\_data, int32\_t timeout)

Resolve DNS name.

[dns\_cancel\_addr\_info](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)

static int dns\_cancel\_addr\_info(uint16\_t dns\_id)

Cancel a pending DNS query.

**Definition** dns\_resolve.h:656

[dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e)

dns\_resolve\_status

Status values for the callback.

**Definition** dns\_resolve.h:260

[dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0)

dns\_query\_type

DNS query type enum.

**Definition** dns\_resolve.h:38

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

**Definition** dns\_resolve.h:47

[dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)

struct dns\_resolve\_context \* dns\_resolve\_get\_default(void)

Get default DNS context.

[dns\_resolve\_cancel\_with\_name](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)

int dns\_resolve\_cancel\_with\_name(struct dns\_resolve\_context \*ctx, uint16\_t dns\_id, const char \*query\_name, enum dns\_query\_type query\_type)

Cancel a pending DNS query using id, name and type.

[dns\_get\_addr\_info](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)

static int dns\_get\_addr\_info(const char \*query, enum dns\_query\_type type, uint16\_t \*dns\_id, dns\_resolve\_cb\_t cb, void \*user\_data, int32\_t timeout)

Get IP address info from DNS.

**Definition** dns\_resolve.h:631

[dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722)

void(\* dns\_resolve\_cb\_t)(enum dns\_resolve\_status status, struct dns\_addrinfo \*info, void \*user\_data)

DNS resolve callback.

**Definition** dns\_resolve.h:316

[DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)

@ DNS\_EAI\_MEMORY

Memory allocation failure.

**Definition** dns\_resolve.h:280

[DNS\_EAI\_NOTCANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f)

@ DNS\_EAI\_NOTCANCELED

Request not canceled.

**Definition** dns\_resolve.h:290

[DNS\_EAI\_IDN\_ENCODE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4)

@ DNS\_EAI\_IDN\_ENCODE

IDN encoding failed.

**Definition** dns\_resolve.h:294

[DNS\_EAI\_ADDRFAMILY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d)

@ DNS\_EAI\_ADDRFAMILY

ai\_family' not supported \*/ DNS\_EAI\_FAMILY = -6, /\*\* ai\_socktype' not supported \*/ DNS\_EAI\_SOCKTYPE =...

**Definition** dns\_resolve.h:278

[DNS\_EAI\_INPROGRESS](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3)

@ DNS\_EAI\_INPROGRESS

Processing request in progress.

**Definition** dns\_resolve.h:286

[DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)

@ DNS\_EAI\_FAIL

Non-recoverable failure in name res.

**Definition** dns\_resolve.h:268

[DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)

@ DNS\_EAI\_AGAIN

Temporary failure in name resolution.

**Definition** dns\_resolve.h:266

[DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)

@ DNS\_EAI\_NODATA

No address associated with NAME.

**Definition** dns\_resolve.h:270

[DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)

@ DNS\_EAI\_NONAME

Invalid value for `ai\_flags' field \*/ DNS\_EAI\_BADFLAGS = -1, /\*\* NAME or SERVICE is unknown.

**Definition** dns\_resolve.h:264

[DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)

@ DNS\_EAI\_OVERFLOW

System error returned in `errno' \*/ DNS\_EAI\_SYSTEM = -11, /\*\* Argument buffer overflow.

**Definition** dns\_resolve.h:284

[DNS\_EAI\_CANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3)

@ DNS\_EAI\_CANCELED

Request canceled.

**Definition** dns\_resolve.h:288

[DNS\_EAI\_ALLDONE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836)

@ DNS\_EAI\_ALLDONE

All requests done.

**Definition** dns\_resolve.h:292

[DNS\_QUERY\_TYPE\_A](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134)

@ DNS\_QUERY\_TYPE\_A

IPv4 query.

**Definition** dns\_resolve.h:40

[DNS\_QUERY\_TYPE\_AAAA](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049)

@ DNS\_QUERY\_TYPE\_AAAA

IPv6 query.

**Definition** dns\_resolve.h:42

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[socket\_poll.h](socket__poll_8h.md)

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

**Definition** dns\_resolve.h:246

[dns\_addrinfo::ai\_canonname](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce)

char ai\_canonname[20+1]

Canonical name of the address.

**Definition** dns\_resolve.h:254

[dns\_addrinfo::ai\_addr](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37)

struct sockaddr ai\_addr

IP address information.

**Definition** dns\_resolve.h:248

[dns\_addrinfo::ai\_addrlen](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799)

socklen\_t ai\_addrlen

Length of the ai\_addr field.

**Definition** dns\_resolve.h:250

[dns\_addrinfo::ai\_family](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558)

uint8\_t ai\_family

Address family of the address information.

**Definition** dns\_resolve.h:252

[dns\_resolve\_context::dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md)

Result callbacks.

**Definition** dns\_resolve.h:378

[dns\_resolve\_context::dns\_pending\_query::query](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b)

const char \* query

String containing the thing to resolve like www.example.com.

**Definition** dns\_resolve.h:408

[dns\_resolve\_context::dns\_pending\_query::query\_hash](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1)

uint16\_t query\_hash

Hash of the DNS name + query type we are querying.

**Definition** dns\_resolve.h:422

[dns\_resolve\_context::dns\_pending\_query::ctx](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae)

struct dns\_resolve\_context \* ctx

Back pointer to ctx, needed in timeout handler.

**Definition** dns\_resolve.h:383

[dns\_resolve\_context::dns\_pending\_query::user\_data](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343)

void \* user\_data

User data.

**Definition** dns\_resolve.h:392

[dns\_resolve\_context::dns\_pending\_query::timer](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230)

struct k\_work\_delayable timer

Timeout timer.

**Definition** dns\_resolve.h:380

[dns\_resolve\_context::dns\_pending\_query::id](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173)

uint16\_t id

DNS id of this query.

**Definition** dns\_resolve.h:414

[dns\_resolve\_context::dns\_pending\_query::timeout](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5)

k\_timeout\_t timeout

TX timeout.

**Definition** dns\_resolve.h:395

[dns\_resolve\_context::dns\_pending\_query::cb](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0)

dns\_resolve\_cb\_t cb

Result callback.

**Definition** dns\_resolve.h:389

[dns\_resolve\_context::dns\_pending\_query::query\_type](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78)

enum dns\_query\_type query\_type

Query type.

**Definition** dns\_resolve.h:411

[dns\_resolve\_context::dns\_server::dns\_server](structdns__resolve__context_1_1dns__server.md#a266b91e051fd7c1b1e434e1a3ab4b5dc)

struct sockaddr dns\_server

DNS server information.

**Definition** dns\_resolve.h:337

[dns\_resolve\_context::dns\_server::if\_index](structdns__resolve__context_1_1dns__server.md#a6b544dc78ee42cd51d2a9404bf69ca06)

int if\_index

Network interface index if the DNS resolving should be done via this interface.

**Definition** dns\_resolve.h:345

[dns\_resolve\_context::dns\_server::sock](structdns__resolve__context_1_1dns__server.md#a762f6cbc4fabe1809966f62d7aa760a6)

int sock

Connection to the DNS server.

**Definition** dns\_resolve.h:340

[dns\_resolve\_context::dns\_server::is\_mdns](structdns__resolve__context_1_1dns__server.md#aaa3606fb80fa171a3b4b91fa0441129f)

uint8\_t is\_mdns

Is this server mDNS one.

**Definition** dns\_resolve.h:348

[dns\_resolve\_context::dns\_server::is\_llmnr](structdns__resolve__context_1_1dns__server.md#af60096f20c95a112caf4f946d898ec70)

uint8\_t is\_llmnr

Is this server LLMNR one.

**Definition** dns\_resolve.h:351

[dns\_resolve\_context](structdns__resolve__context.md)

DNS resolve context structure.

**Definition** dns\_resolve.h:333

[dns\_resolve\_context::buf\_timeout](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6)

k\_timeout\_t buf\_timeout

This timeout is also used when a buffer is required from the buffer pools.

**Definition** dns\_resolve.h:370

[dns\_resolve\_context::queries](structdns__resolve__context.md#a596053473b44be4977947632a1abb51e)

struct dns\_resolve\_context::dns\_pending\_query queries[DNS\_NUM\_CONCUR\_QUERIES]

[dns\_resolve\_context::servers](structdns__resolve__context.md#a81becba86317bbd32d384ff2e677c829)

struct dns\_resolve\_context::dns\_server servers[DNS\_RESOLVER\_MAX\_POLL]

[dns\_resolve\_context::state](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a)

enum dns\_resolve\_context\_state state

Is this context in use.

**Definition** dns\_resolve.h:426

[dns\_resolve\_context::lock](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7)

struct k\_mutex lock

Prevent concurrent access.

**Definition** dns\_resolve.h:365

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4034

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:408

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dns\_resolve.h](dns__resolve_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
