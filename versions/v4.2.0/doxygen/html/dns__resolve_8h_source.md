---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/dns__resolve_8h_source.html
original_path: doxygen/html/dns__resolve_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

[ 42](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa) [DNS\_QUERY\_TYPE\_PTR](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa) = 12,

[ 44](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049) [DNS\_QUERY\_TYPE\_AAAA](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049) = 28

45};

46

[ 50](group__dns__resolve.md#gaeda02f82b12e9b7b4dea9fd66be123a7)enum [dns\_server\_source](group__dns__resolve.md#gaeda02f82b12e9b7b4dea9fd66be123a7) {

[ 52](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9) [DNS\_SOURCE\_UNKNOWN](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9) = 0,

[ 54](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33) [DNS\_SOURCE\_MANUAL](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33),

[ 56](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b) [DNS\_SOURCE\_DHCPV4](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b),

[ 58](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b) [DNS\_SOURCE\_DHCPV6](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b),

[ 60](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9) [DNS\_SOURCE\_IPV6\_RA](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9),

[ 62](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902) [DNS\_SOURCE\_PPP](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902),

63};

64

66#if defined(CONFIG\_DNS\_RESOLVER\_MAX\_NAME\_LEN)

67#define DNS\_MAX\_NAME\_SIZE CONFIG\_DNS\_RESOLVER\_MAX\_NAME\_LEN

68#else

[ 69](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db)#define DNS\_MAX\_NAME\_SIZE 20

70#endif /\* CONFIG\_DNS\_RESOLVER\_MAX\_NAME\_LEN \*/

71

73

74#define DNS\_BUF\_TIMEOUT K\_MSEC(500) /\* ms \*/

75

76/\* This value is recommended by RFC 1035 \*/

77#if defined(CONFIG\_DNS\_RESOLVER\_MAX\_ANSWER\_SIZE)

78#define DNS\_RESOLVER\_MAX\_BUF\_SIZE CONFIG\_DNS\_RESOLVER\_MAX\_ANSWER\_SIZE

79#else

80#define DNS\_RESOLVER\_MAX\_BUF\_SIZE 512

81#endif /\* CONFIG\_DNS\_RESOLVER\_MAX\_ANSWER\_SIZE \*/

82

83/\* Make sure that we can compile things even if CONFIG\_DNS\_RESOLVER

84 \* is not enabled.

85 \*/

86#if defined(CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS)

87#define DNS\_RESOLVER\_MAX\_SERVERS CONFIG\_DNS\_RESOLVER\_MAX\_SERVERS

88#else

89#define DNS\_RESOLVER\_MAX\_SERVERS 0

90#endif

91

92#if defined(CONFIG\_DNS\_NUM\_CONCUR\_QUERIES)

93#define DNS\_NUM\_CONCUR\_QUERIES CONFIG\_DNS\_NUM\_CONCUR\_QUERIES

94#else

95#define DNS\_NUM\_CONCUR\_QUERIES 1

96#endif

97

98#if defined(CONFIG\_NET\_IF\_MAX\_IPV6\_COUNT)

99#define MAX\_IPV6\_IFACE\_COUNT CONFIG\_NET\_IF\_MAX\_IPV6\_COUNT

100#else

101#define MAX\_IPV6\_IFACE\_COUNT 1

102#endif

103

104#if defined(CONFIG\_NET\_IF\_MAX\_IPV4\_COUNT)

105#define MAX\_IPV4\_IFACE\_COUNT CONFIG\_NET\_IF\_MAX\_IPV4\_COUNT

106#else

107#define MAX\_IPV4\_IFACE\_COUNT 1

108#endif

109

110/\* If mDNS is enabled, then add some extra well known multicast servers to the

111 \* server list.

112 \*/

113#if defined(CONFIG\_MDNS\_RESOLVER)

114#if defined(CONFIG\_NET\_IPV6) && defined(CONFIG\_NET\_IPV4)

115#define MDNS\_SERVER\_COUNT 2

116#else

117#define MDNS\_SERVER\_COUNT 1

118#endif /\* CONFIG\_NET\_IPV6 && CONFIG\_NET\_IPV4 \*/

119#else

120#define MDNS\_SERVER\_COUNT 0

121#endif /\* CONFIG\_MDNS\_RESOLVER \*/

122

123/\* If LLMNR is enabled, then add some extra well known multicast servers to the

124 \* server list.

125 \*/

126#if defined(CONFIG\_LLMNR\_RESOLVER)

127#if defined(CONFIG\_NET\_IPV6) && defined(CONFIG\_NET\_IPV4)

128#define LLMNR\_SERVER\_COUNT 2

129#else

130#define LLMNR\_SERVER\_COUNT 1

131#endif /\* CONFIG\_NET\_IPV6 && CONFIG\_NET\_IPV4 \*/

132#else

133#define LLMNR\_SERVER\_COUNT 0

134#endif /\* CONFIG\_MDNS\_RESOLVER \*/

135

136#define DNS\_MAX\_MCAST\_SERVERS (MDNS\_SERVER\_COUNT + LLMNR\_SERVER\_COUNT)

137

138#if defined(CONFIG\_MDNS\_RESPONDER)

139#if defined(CONFIG\_NET\_IPV6)

140#define MDNS\_MAX\_IPV6\_IFACE\_COUNT CONFIG\_NET\_IF\_MAX\_IPV6\_COUNT

141#else

142#define MDNS\_MAX\_IPV6\_IFACE\_COUNT 0

143#endif /\* CONFIG\_NET\_IPV6 \*/

144

145#if defined(CONFIG\_NET\_IPV4)

146#define MDNS\_MAX\_IPV4\_IFACE\_COUNT CONFIG\_NET\_IF\_MAX\_IPV4\_COUNT

147#else

148#define MDNS\_MAX\_IPV4\_IFACE\_COUNT 0

149#endif /\* CONFIG\_NET\_IPV4 \*/

150

151#define MDNS\_MAX\_POLL (MDNS\_MAX\_IPV4\_IFACE\_COUNT + MDNS\_MAX\_IPV6\_IFACE\_COUNT)

152#else

153#define MDNS\_MAX\_POLL 0

154#endif /\* CONFIG\_MDNS\_RESPONDER \*/

155

156#if defined(CONFIG\_LLMNR\_RESPONDER)

157#if defined(CONFIG\_NET\_IPV6) && defined(CONFIG\_NET\_IPV4)

158#define LLMNR\_MAX\_POLL 2

159#else

160#define LLMNR\_MAX\_POLL 1

161#endif

162#else

163#define LLMNR\_MAX\_POLL 0

164#endif /\* CONFIG\_LLMNR\_RESPONDER \*/

165

166#define DNS\_RESOLVER\_MAX\_POLL (DNS\_RESOLVER\_MAX\_SERVERS + DNS\_MAX\_MCAST\_SERVERS)

167

169#define DNS\_DISPATCHER\_MAX\_POLL (DNS\_RESOLVER\_MAX\_POLL + MDNS\_MAX\_POLL + LLMNR\_MAX\_POLL)

170

171#if defined(CONFIG\_ZVFS\_POLL\_MAX)

172BUILD\_ASSERT(CONFIG\_ZVFS\_POLL\_MAX >= DNS\_DISPATCHER\_MAX\_POLL,

173 "CONFIG\_ZVFS\_POLL\_MAX must be larger than " [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(DNS\_DISPATCHER\_MAX\_POLL));

174#endif

175

179enum dns\_socket\_type {

180 DNS\_SOCKET\_RESOLVER = 1,

181 DNS\_SOCKET\_RESPONDER = 2

182};

183

184struct [dns\_resolve\_context](structdns__resolve__context.md);

185struct mdns\_responder\_context;

186struct dns\_socket\_dispatcher;

187

202typedef int (\*dns\_socket\_dispatcher\_cb)(struct dns\_socket\_dispatcher \*ctx, int sock,

203 struct [sockaddr](structsockaddr.md) \*addr, size\_t addrlen,

204 struct [net\_buf](structnet__buf.md) \*buf, size\_t data\_len);

205

207struct dns\_socket\_dispatcher {

209 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

211 const struct net\_socket\_service\_desc \*svc;

215 union {

216 void \*ctx;

217 struct dns\_resolve\_context \*resolve\_ctx;

218 struct mdns\_responder\_context \*mdns\_ctx;

219 };

220

222 enum dns\_socket\_type type;

224 struct sockaddr local\_addr;

226 dns\_socket\_dispatcher\_cb cb;

228 struct zsock\_pollfd \*fds;

230 int fds\_len;

232 int sock;

234 int ifindex;

238 struct dns\_socket\_dispatcher \*pair;

240 struct k\_mutex lock;

242 k\_timeout\_t buf\_timeout;

243};

244

254int dns\_dispatcher\_register(struct dns\_socket\_dispatcher \*ctx);

255

265int dns\_dispatcher\_unregister(struct dns\_socket\_dispatcher \*ctx);

266

268

[ 272](structdns__addrinfo.md)struct [dns\_addrinfo](structdns__addrinfo.md) {

[ 274](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37) struct [sockaddr](structsockaddr.md) [ai\_addr](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37);

[ 276](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [ai\_addrlen](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799);

[ 278](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ai\_family](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558);

[ 280](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce) char [ai\_canonname](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce)[[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db) + 1];

281};

282

[ 286](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e)enum [dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) {

288 DNS\_EAI\_BADFLAGS = -1,

[ 290](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) = -2,

[ 292](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) = -3,

[ 294](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) = -4,

[ 296](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) = -5,

298 DNS\_EAI\_FAMILY = -6,

300 DNS\_EAI\_SOCKTYPE = -7,

302 DNS\_EAI\_SERVICE = -8,

[ 304](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d) [DNS\_EAI\_ADDRFAMILY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d) = -9,

[ 306](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) = -10,

308 DNS\_EAI\_SYSTEM = -11,

[ 310](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) [DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) = -12,

[ 312](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3) [DNS\_EAI\_INPROGRESS](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3) = -100,

[ 314](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3) [DNS\_EAI\_CANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3) = -101,

[ 316](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f) [DNS\_EAI\_NOTCANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f) = -102,

[ 318](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836) [DNS\_EAI\_ALLDONE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836) = -103,

[ 320](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4) [DNS\_EAI\_IDN\_ENCODE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4) = -105,

321};

322

[ 342](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722)typedef void (\*[dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722))(enum [dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e) status,

343 struct [dns\_addrinfo](structdns__addrinfo.md) \*info,

344 void \*user\_data);

345

347

348enum dns\_resolve\_context\_state {

349 DNS\_RESOLVE\_CONTEXT\_UNINITIALIZED = 0,

350 DNS\_RESOLVE\_CONTEXT\_ACTIVE,

351 DNS\_RESOLVE\_CONTEXT\_DEACTIVATING,

352 DNS\_RESOLVE\_CONTEXT\_INACTIVE,

353};

354

356

[ 360](structdns__resolve__context.md)struct [dns\_resolve\_context](structdns__resolve__context.md) {

[ 362](structdns__resolve__context_1_1dns__server.md) struct [dns\_server](structdns__resolve__context_1_1dns__server.md#a266b91e051fd7c1b1e434e1a3ab4b5dc) {

[ 364](structdns__resolve__context_1_1dns__server.md#a266b91e051fd7c1b1e434e1a3ab4b5dc) struct [sockaddr](structsockaddr.md) [dns\_server](structdns__resolve__context_1_1dns__server.md#a266b91e051fd7c1b1e434e1a3ab4b5dc);

365

[ 367](structdns__resolve__context_1_1dns__server.md#a762f6cbc4fabe1809966f62d7aa760a6) int [sock](structdns__resolve__context_1_1dns__server.md#a762f6cbc4fabe1809966f62d7aa760a6);

368

[ 372](structdns__resolve__context_1_1dns__server.md#a6b544dc78ee42cd51d2a9404bf69ca06) int [if\_index](structdns__resolve__context_1_1dns__server.md#a6b544dc78ee42cd51d2a9404bf69ca06);

373

[ 375](structdns__resolve__context_1_1dns__server.md#a5d6003855511e8754372a9189c3bfbec) enum [dns\_server\_source](group__dns__resolve.md#gaeda02f82b12e9b7b4dea9fd66be123a7) [source](structdns__resolve__context_1_1dns__server.md#a5d6003855511e8754372a9189c3bfbec);

376

[ 378](structdns__resolve__context_1_1dns__server.md#aaa3606fb80fa171a3b4b91fa0441129f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_mdns](structdns__resolve__context_1_1dns__server.md#aaa3606fb80fa171a3b4b91fa0441129f) : 1;

379

[ 381](structdns__resolve__context_1_1dns__server.md#af60096f20c95a112caf4f946d898ec70) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_llmnr](structdns__resolve__context_1_1dns__server.md#af60096f20c95a112caf4f946d898ec70) : 1;

382

385 struct dns\_socket\_dispatcher dispatcher;

[ 387](structdns__resolve__context.md#a81becba86317bbd32d384ff2e677c829) } [servers](structdns__resolve__context.md#a81becba86317bbd32d384ff2e677c829)[DNS\_RESOLVER\_MAX\_POLL];

388

391 struct [zsock\_pollfd](structzsock__pollfd.md) fds[DNS\_RESOLVER\_MAX\_POLL];

393

[ 395](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7) struct [k\_mutex](structk__mutex.md) [lock](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7);

396

[ 400](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6) [k\_timeout\_t](structk__timeout__t.md) [buf\_timeout](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6);

401

[ 408](structdns__resolve__context_1_1dns__pending__query.md) struct [dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md) {

[ 410](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230) struct [k\_work\_delayable](structk__work__delayable.md) [timer](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230);

411

[ 413](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae) struct [dns\_resolve\_context](structdns__resolve__context.md) \*[ctx](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae);

414

[ 419](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0) [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) [cb](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0);

420

[ 422](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343) void \*[user\_data](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343);

423

[ 425](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5) [k\_timeout\_t](structk__timeout__t.md) [timeout](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5);

426

[ 438](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b) const char \*[query](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b);

439

[ 441](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78) enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) [query\_type](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78);

442

[ 444](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [id](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173);

445

[ 452](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [query\_hash](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1);

[ 453](structdns__resolve__context.md#a596053473b44be4977947632a1abb51e) } [queries](structdns__resolve__context.md#a596053473b44be4977947632a1abb51e)[DNS\_NUM\_CONCUR\_QUERIES];

454

[ 456](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a) enum dns\_resolve\_context\_state [state](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a);

457};

458

460

461struct mdns\_probe\_user\_data {

462 struct mdns\_responder\_context \*ctx;

463 char query[[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db) + 1];

464 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id;

465};

466

467struct mdns\_responder\_context {

468 struct sockaddr server\_addr;

469 struct dns\_socket\_dispatcher dispatcher;

470 struct zsock\_pollfd fds[1];

471 int sock;

472 struct net\_if \*iface;

473#if defined(CONFIG\_MDNS\_RESPONDER\_PROBE)

474 struct k\_work\_delayable probe\_timer;

475 struct dns\_resolve\_context probe\_ctx;

476 struct mdns\_probe\_user\_data probe\_data;

477#endif

478};

479

481

[ 509](group__dns__resolve.md#ga74e2be49894100fe5da641331ef083de)int [dns\_resolve\_init](group__dns__resolve.md#ga74e2be49894100fe5da641331ef083de)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

510 const char \*dns\_servers\_str[],

511 const struct [sockaddr](structsockaddr.md) \*dns\_servers\_sa[]);

512

[ 520](group__dns__resolve.md#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)int [dns\_resolve\_init\_default](group__dns__resolve.md#ga71eab0f9dd0bc7c02c0d55e7dc6741f3)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx);

521

[ 532](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc)int [dns\_resolve\_close](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx);

533

[ 554](group__dns__resolve.md#ga54dc319f118e6a8e1e78435539c8f039)int [dns\_resolve\_reconfigure](group__dns__resolve.md#ga54dc319f118e6a8e1e78435539c8f039)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

555 const char \*servers\_str[],

556 const struct [sockaddr](structsockaddr.md) \*servers\_sa[],

557 enum [dns\_server\_source](group__dns__resolve.md#gaeda02f82b12e9b7b4dea9fd66be123a7) source);

558

[ 581](group__dns__resolve.md#ga211f9c8a5588186607e9257c4451f64d)int [dns\_resolve\_reconfigure\_with\_interfaces](group__dns__resolve.md#ga211f9c8a5588186607e9257c4451f64d)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

582 const char \*servers\_str[],

583 const struct [sockaddr](structsockaddr.md) \*servers\_sa[],

584 int interfaces[],

585 enum [dns\_server\_source](group__dns__resolve.md#gaeda02f82b12e9b7b4dea9fd66be123a7) source);

586

[ 595](group__dns__resolve.md#ga54c85b9c69c9a44f2e7bb78165cebfcb)int [dns\_resolve\_remove](group__dns__resolve.md#ga54c85b9c69c9a44f2e7bb78165cebfcb)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, int if\_index);

596

[ 607](group__dns__resolve.md#gae292786587c511c223481f77a4f43017)int [dns\_resolve\_remove\_source](group__dns__resolve.md#gae292786587c511c223481f77a4f43017)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx, int if\_index,

608 enum [dns\_server\_source](group__dns__resolve.md#gaeda02f82b12e9b7b4dea9fd66be123a7) source);

609

[ 620](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)int [dns\_resolve\_cancel](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

621 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id);

622

[ 635](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)int [dns\_resolve\_cancel\_with\_name](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

636 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id,

637 const char \*query\_name,

638 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) query\_type);

639

[ 667](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)int [dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

668 const char \*query,

669 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) type,

670 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id,

671 [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb,

672 void \*user\_data,

673 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

674

[ 702](group__dns__resolve.md#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)static inline int [dns\_resolve\_service](group__dns__resolve.md#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)(struct [dns\_resolve\_context](structdns__resolve__context.md) \*ctx,

703 const char \*query,

704 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id,

705 [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb,

706 void \*user\_data,

707 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

708{

709 return [dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)(ctx, query, [DNS\_QUERY\_TYPE\_PTR](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa),

710 dns\_id, cb, user\_data, timeout);

711}

712

[ 723](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)struct [dns\_resolve\_context](structdns__resolve__context.md) \*[dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(void);

724

[ 752](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)static inline int [dns\_get\_addr\_info](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)(const char \*query,

753 enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) type,

754 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dns\_id,

755 [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) cb,

756 void \*user\_data,

757 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

758{

759 return [dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)([dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(),

760 query,

761 type,

762 dns\_id,

763 cb,

764 user\_data,

765 timeout);

766}

767

[ 777](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)static inline int [dns\_cancel\_addr\_info](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_id)

778{

779 return [dns\_resolve\_cancel](group__dns__resolve.md#ga7701ddd6b6c5923f0d122a2bcf898cbf)([dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)(), dns\_id);

780}

781

785

787

795const char \*dns\_get\_source\_str(enum [dns\_server\_source](group__dns__resolve.md#gaeda02f82b12e9b7b4dea9fd66be123a7) source);

796

800#if defined(CONFIG\_DNS\_RESOLVER\_AUTO\_INIT)

801void dns\_init\_resolver(void);

802

803#else

804#define dns\_init\_resolver(...)

805#endif /\* CONFIG\_DNS\_RESOLVER\_AUTO\_INIT \*/

806

808

809#ifdef \_\_cplusplus

810}

811#endif

812

813#endif /\* ZEPHYR\_INCLUDE\_NET\_DNS\_RESOLVE\_H\_ \*/

[dns\_resolve\_reconfigure\_with\_interfaces](group__dns__resolve.md#ga211f9c8a5588186607e9257c4451f64d)

int dns\_resolve\_reconfigure\_with\_interfaces(struct dns\_resolve\_context \*ctx, const char \*servers\_str[], const struct sockaddr \*servers\_sa[], int interfaces[], enum dns\_server\_source source)

Reconfigure DNS resolving context with new server list and allowing servers to be specified to a spec...

[dns\_resolve\_name](group__dns__resolve.md#ga24f9bc24e2021b6b528bb15e4fcca49b)

int dns\_resolve\_name(struct dns\_resolve\_context \*ctx, const char \*query, enum dns\_query\_type type, uint16\_t \*dns\_id, dns\_resolve\_cb\_t cb, void \*user\_data, int32\_t timeout)

Resolve DNS name.

[dns\_cancel\_addr\_info](group__dns__resolve.md#ga54ae7aaf53b36951b27f09e1cc82df55)

static int dns\_cancel\_addr\_info(uint16\_t dns\_id)

Cancel a pending DNS query.

**Definition** dns\_resolve.h:777

[dns\_resolve\_remove](group__dns__resolve.md#ga54c85b9c69c9a44f2e7bb78165cebfcb)

int dns\_resolve\_remove(struct dns\_resolve\_context \*ctx, int if\_index)

Remove servers from the DNS resolving context.

[dns\_resolve\_reconfigure](group__dns__resolve.md#ga54dc319f118e6a8e1e78435539c8f039)

int dns\_resolve\_reconfigure(struct dns\_resolve\_context \*ctx, const char \*servers\_str[], const struct sockaddr \*servers\_sa[], enum dns\_server\_source source)

Reconfigure DNS resolving context.

[dns\_resolve\_status](group__dns__resolve.md#ga5baf1fea0482fb3a940b4f5350a3c58e)

dns\_resolve\_status

Status values for the callback.

**Definition** dns\_resolve.h:286

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

[dns\_resolve\_close](group__dns__resolve.md#gab04f3b2347e9c59346c10180c6c9ffbc)

int dns\_resolve\_close(struct dns\_resolve\_context \*ctx)

Close DNS resolving context.

[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db)

#define DNS\_MAX\_NAME\_SIZE

Max size of the resolved name.

**Definition** dns\_resolve.h:69

[dns\_resolve\_remove\_source](group__dns__resolve.md#gae292786587c511c223481f77a4f43017)

int dns\_resolve\_remove\_source(struct dns\_resolve\_context \*ctx, int if\_index, enum dns\_server\_source source)

Remove servers from the DNS resolving context that were added by a specific source.

[dns\_resolve\_get\_default](group__dns__resolve.md#gae69cd758e99ea93ef8aac28366918b87)

struct dns\_resolve\_context \* dns\_resolve\_get\_default(void)

Get default DNS context.

[dns\_server\_source](group__dns__resolve.md#gaeda02f82b12e9b7b4dea9fd66be123a7)

dns\_server\_source

Entity that added the DNS server.

**Definition** dns\_resolve.h:50

[dns\_resolve\_cancel\_with\_name](group__dns__resolve.md#gaf2854ca9b839e7cba073e75202ac7e38)

int dns\_resolve\_cancel\_with\_name(struct dns\_resolve\_context \*ctx, uint16\_t dns\_id, const char \*query\_name, enum dns\_query\_type query\_type)

Cancel a pending DNS query using id, name and type.

[dns\_resolve\_service](group__dns__resolve.md#gaf28f6f8baa97d0b2341e1bdc02b6cb8c)

static int dns\_resolve\_service(struct dns\_resolve\_context \*ctx, const char \*query, uint16\_t \*dns\_id, dns\_resolve\_cb\_t cb, void \*user\_data, int32\_t timeout)

Resolve DNS service.

**Definition** dns\_resolve.h:702

[dns\_get\_addr\_info](group__dns__resolve.md#gaf891d7e21bddc8fbd029209b4339c01d)

static int dns\_get\_addr\_info(const char \*query, enum dns\_query\_type type, uint16\_t \*dns\_id, dns\_resolve\_cb\_t cb, void \*user\_data, int32\_t timeout)

Get IP address info from DNS.

**Definition** dns\_resolve.h:752

[dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722)

void(\* dns\_resolve\_cb\_t)(enum dns\_resolve\_status status, struct dns\_addrinfo \*info, void \*user\_data)

DNS resolve callback.

**Definition** dns\_resolve.h:342

[DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673)

@ DNS\_EAI\_MEMORY

Memory allocation failure.

**Definition** dns\_resolve.h:306

[DNS\_EAI\_NOTCANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea2839d8cf68a4d668ccfdb38898a2414f)

@ DNS\_EAI\_NOTCANCELED

Request not canceled.

**Definition** dns\_resolve.h:316

[DNS\_EAI\_IDN\_ENCODE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea3f7d3cecbaf3b7ca061f163f7769cda4)

@ DNS\_EAI\_IDN\_ENCODE

IDN encoding failed.

**Definition** dns\_resolve.h:320

[DNS\_EAI\_ADDRFAMILY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4092e3cb6e36bba4ea8fce4bc0352e5d)

@ DNS\_EAI\_ADDRFAMILY

ai\_family' not supported \*/ DNS\_EAI\_FAMILY = -6, /\*\* ai\_socktype' not supported \*/ DNS\_EAI\_SOCKTYPE =...

**Definition** dns\_resolve.h:304

[DNS\_EAI\_INPROGRESS](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea4281a05dd374dc24758896fb8d4000f3)

@ DNS\_EAI\_INPROGRESS

Processing request in progress.

**Definition** dns\_resolve.h:312

[DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455)

@ DNS\_EAI\_FAIL

Non-recoverable failure in name res.

**Definition** dns\_resolve.h:294

[DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9)

@ DNS\_EAI\_AGAIN

Temporary failure in name resolution.

**Definition** dns\_resolve.h:292

[DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2)

@ DNS\_EAI\_NODATA

No address associated with NAME.

**Definition** dns\_resolve.h:296

[DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f)

@ DNS\_EAI\_NONAME

Invalid value for `ai\_flags' field \*/ DNS\_EAI\_BADFLAGS = -1, /\*\* NAME or SERVICE is unknown.

**Definition** dns\_resolve.h:290

[DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f)

@ DNS\_EAI\_OVERFLOW

System error returned in `errno' \*/ DNS\_EAI\_SYSTEM = -11, /\*\* Argument buffer overflow.

**Definition** dns\_resolve.h:310

[DNS\_EAI\_CANCELED](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea935a23488ff9e1f51f91ac3598a4cbc3)

@ DNS\_EAI\_CANCELED

Request canceled.

**Definition** dns\_resolve.h:314

[DNS\_EAI\_ALLDONE](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58eac9a19751ef16468e8f46b9f59bc8d836)

@ DNS\_EAI\_ALLDONE

All requests done.

**Definition** dns\_resolve.h:318

[DNS\_QUERY\_TYPE\_PTR](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a69676b0e82ee456e5faa935e39c1c3fa)

@ DNS\_QUERY\_TYPE\_PTR

PTR query.

**Definition** dns\_resolve.h:42

[DNS\_QUERY\_TYPE\_A](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0a96b4b4e07f1560cd046cac010ac32134)

@ DNS\_QUERY\_TYPE\_A

IPv4 query.

**Definition** dns\_resolve.h:40

[DNS\_QUERY\_TYPE\_AAAA](group__dns__resolve.md#gga7169c5a920fb1b0d77910a6ab922e3f0aad661f3510af499212143370a81b9049)

@ DNS\_QUERY\_TYPE\_AAAA

IPv6 query.

**Definition** dns\_resolve.h:44

[DNS\_SOURCE\_MANUAL](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a53fc14584c90542121f4b1cd61658c33)

@ DNS\_SOURCE\_MANUAL

Server information is added manually, for example by an application.

**Definition** dns\_resolve.h:54

[DNS\_SOURCE\_IPV6\_RA](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a687bf289d220cfaffbf8c89d9ce5b4c9)

@ DNS\_SOURCE\_IPV6\_RA

Server information is from IPv6 SLAAC (router advertisement).

**Definition** dns\_resolve.h:60

[DNS\_SOURCE\_DHCPV4](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b)

@ DNS\_SOURCE\_DHCPV4

Server information is from DHCPv4 server.

**Definition** dns\_resolve.h:56

[DNS\_SOURCE\_UNKNOWN](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a8e2e0f2cf2997d9519a52dfa9052fdf9)

@ DNS\_SOURCE\_UNKNOWN

Source is unknown.

**Definition** dns\_resolve.h:52

[DNS\_SOURCE\_PPP](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7aa6df19967b1ac123c79c5812ec62a902)

@ DNS\_SOURCE\_PPP

Server information is from PPP.

**Definition** dns\_resolve.h:62

[DNS\_SOURCE\_DHCPV6](group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7ad12f850b810647113633234ae818b84b)

@ DNS\_SOURCE\_DHCPV6

Server information is from DHCPv6 server.

**Definition** dns\_resolve.h:58

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

**Definition** common.h:165

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

**Definition** dns\_resolve.h:272

[dns\_addrinfo::ai\_canonname](structdns__addrinfo.md#a21db6675aef2f8bafb83846343eae9ce)

char ai\_canonname[20+1]

Canonical name of the address.

**Definition** dns\_resolve.h:280

[dns\_addrinfo::ai\_addr](structdns__addrinfo.md#a254fcceb59e65cb425c19825b28c3d37)

struct sockaddr ai\_addr

IP address information.

**Definition** dns\_resolve.h:274

[dns\_addrinfo::ai\_addrlen](structdns__addrinfo.md#ad70149a624f91ec49ac4121aba5d3799)

socklen\_t ai\_addrlen

Length of the ai\_addr field.

**Definition** dns\_resolve.h:276

[dns\_addrinfo::ai\_family](structdns__addrinfo.md#af9a9458751ddb65219f3b5f6730df558)

uint8\_t ai\_family

Address family of the address information.

**Definition** dns\_resolve.h:278

[dns\_resolve\_context::dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md)

Result callbacks.

**Definition** dns\_resolve.h:408

[dns\_resolve\_context::dns\_pending\_query::query](structdns__resolve__context_1_1dns__pending__query.md#a106464bda8d56283b06251c37964906b)

const char \* query

String containing the thing to resolve like www.example.com.

**Definition** dns\_resolve.h:438

[dns\_resolve\_context::dns\_pending\_query::query\_hash](structdns__resolve__context_1_1dns__pending__query.md#a168fea99e8c6760cab49611ceb5a6fc1)

uint16\_t query\_hash

Hash of the DNS name + query type we are querying.

**Definition** dns\_resolve.h:452

[dns\_resolve\_context::dns\_pending\_query::ctx](structdns__resolve__context_1_1dns__pending__query.md#a4260371a741b3c2e752848955eee5cae)

struct dns\_resolve\_context \* ctx

Back pointer to ctx, needed in timeout handler.

**Definition** dns\_resolve.h:413

[dns\_resolve\_context::dns\_pending\_query::user\_data](structdns__resolve__context_1_1dns__pending__query.md#a6a1c93f3eab8f9aa55dbb26e704bb343)

void \* user\_data

User data.

**Definition** dns\_resolve.h:422

[dns\_resolve\_context::dns\_pending\_query::timer](structdns__resolve__context_1_1dns__pending__query.md#a6f76b200b8c421399987be83b72b9230)

struct k\_work\_delayable timer

Timeout timer.

**Definition** dns\_resolve.h:410

[dns\_resolve\_context::dns\_pending\_query::id](structdns__resolve__context_1_1dns__pending__query.md#a773e2ad2bedb2d1030df3590e9a14173)

uint16\_t id

DNS id of this query.

**Definition** dns\_resolve.h:444

[dns\_resolve\_context::dns\_pending\_query::timeout](structdns__resolve__context_1_1dns__pending__query.md#aa2b1f1db21ab4a05240ebb62512c24d5)

k\_timeout\_t timeout

TX timeout.

**Definition** dns\_resolve.h:425

[dns\_resolve\_context::dns\_pending\_query::cb](structdns__resolve__context_1_1dns__pending__query.md#aacf4003ce035658038ae44773091f2d0)

dns\_resolve\_cb\_t cb

Result callback.

**Definition** dns\_resolve.h:419

[dns\_resolve\_context::dns\_pending\_query::query\_type](structdns__resolve__context_1_1dns__pending__query.md#af5796eb469e2fe3bcebea2ad55a8fd78)

enum dns\_query\_type query\_type

Query type.

**Definition** dns\_resolve.h:441

[dns\_resolve\_context::dns\_server::dns\_server](structdns__resolve__context_1_1dns__server.md#a266b91e051fd7c1b1e434e1a3ab4b5dc)

struct sockaddr dns\_server

DNS server information.

**Definition** dns\_resolve.h:364

[dns\_resolve\_context::dns\_server::source](structdns__resolve__context_1_1dns__server.md#a5d6003855511e8754372a9189c3bfbec)

enum dns\_server\_source source

Source of the DNS server, e.g., manual, DHCPv4/6, etc.

**Definition** dns\_resolve.h:375

[dns\_resolve\_context::dns\_server::if\_index](structdns__resolve__context_1_1dns__server.md#a6b544dc78ee42cd51d2a9404bf69ca06)

int if\_index

Network interface index if the DNS resolving should be done via this interface.

**Definition** dns\_resolve.h:372

[dns\_resolve\_context::dns\_server::sock](structdns__resolve__context_1_1dns__server.md#a762f6cbc4fabe1809966f62d7aa760a6)

int sock

Connection to the DNS server.

**Definition** dns\_resolve.h:367

[dns\_resolve\_context::dns\_server::is\_mdns](structdns__resolve__context_1_1dns__server.md#aaa3606fb80fa171a3b4b91fa0441129f)

uint8\_t is\_mdns

Is this server mDNS one.

**Definition** dns\_resolve.h:378

[dns\_resolve\_context::dns\_server::is\_llmnr](structdns__resolve__context_1_1dns__server.md#af60096f20c95a112caf4f946d898ec70)

uint8\_t is\_llmnr

Is this server LLMNR one.

**Definition** dns\_resolve.h:381

[dns\_resolve\_context](structdns__resolve__context.md)

DNS resolve context structure.

**Definition** dns\_resolve.h:360

[dns\_resolve\_context::buf\_timeout](structdns__resolve__context.md#a402a4a2adfe3859f8dab749b44b7d8e6)

k\_timeout\_t buf\_timeout

This timeout is also used when a buffer is required from the buffer pools.

**Definition** dns\_resolve.h:400

[dns\_resolve\_context::queries](structdns__resolve__context.md#a596053473b44be4977947632a1abb51e)

struct dns\_resolve\_context::dns\_pending\_query queries[DNS\_NUM\_CONCUR\_QUERIES]

[dns\_resolve\_context::servers](structdns__resolve__context.md#a81becba86317bbd32d384ff2e677c829)

struct dns\_resolve\_context::dns\_server servers[DNS\_RESOLVER\_MAX\_POLL]

[dns\_resolve\_context::state](structdns__resolve__context.md#a88f6600061cdb8e9f34802fe2a0a7d5a)

enum dns\_resolve\_context\_state state

Is this context in use.

**Definition** dns\_resolve.h:456

[dns\_resolve\_context::lock](structdns__resolve__context.md#a9d1ada3ab20399f750acfee94e8e6cd7)

struct k\_mutex lock

Prevent concurrent access.

**Definition** dns\_resolve.h:395

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3070

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4101

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:410

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dns\_resolve.h](dns__resolve_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
