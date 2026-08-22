---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net__pkt_8h_source.html
original_path: doxygen/html/net__pkt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_pkt.h

[Go to the documentation of this file.](net__pkt_8h.md)

1

7

8/\*

9 \* Copyright (c) 2016 Intel Corporation

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14/\* Data buffer API - used for all data to/from net \*/

15

16#ifndef ZEPHYR\_INCLUDE\_NET\_NET\_PKT\_H\_

17#define ZEPHYR\_INCLUDE\_NET\_NET\_PKT\_H\_

18

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20#include <[stdbool.h](stdbool_8h.md)>

21

22#include <[zephyr/net\_buf.h](net__buf_8h.md)>

23

24#if defined(CONFIG\_IEEE802154)

25#include <[zephyr/net/ieee802154\_pkt.h](ieee802154__pkt_8h.md)>

26#endif

27#include <[zephyr/net/net\_core.h](net__core_8h.md)>

28#include <[zephyr/net/net\_linkaddr.h](net__linkaddr_8h.md)>

29#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

30#include <[zephyr/net/net\_if.h](net__if_8h.md)>

31#include <[zephyr/net/net\_context.h](net__context_8h.md)>

32#include <[zephyr/net/net\_time.h](net__time_8h.md)>

33#include <[zephyr/net/ethernet\_vlan.h](ethernet__vlan_8h.md)>

34#include <[zephyr/net/ptp\_time.h](ptp__time_8h.md)>

35

36#ifdef \_\_cplusplus

37extern "C" {

38#endif

39

48

49struct [net\_context](structnet__context.md);

50

52

53#if defined(CONFIG\_NET\_PKT\_ALLOC\_STATS)

54struct net\_pkt\_alloc\_stats {

55 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) alloc\_sum;

56 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) time\_sum;

57 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count;

58};

59

60struct net\_pkt\_alloc\_stats\_slab {

61 struct net\_pkt\_alloc\_stats ok;

62 struct net\_pkt\_alloc\_stats fail;

63 struct k\_mem\_slab \*slab;

64};

65

66#define NET\_PKT\_ALLOC\_STATS\_DEFINE(alloc\_name, slab\_name) \

67 STRUCT\_SECTION\_ITERABLE(net\_pkt\_alloc\_stats\_slab, alloc\_name) = { \

68 .slab = &slab\_name, \

69 }

70

71#else

72#define NET\_PKT\_ALLOC\_STATS\_DEFINE(name, slab)

73#endif /\* CONFIG\_NET\_PKT\_ALLOC\_STATS \*/

74

75/\* buffer cursor used in net\_pkt \*/

76struct net\_pkt\_cursor {

78 struct net\_buf \*buf;

80 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*pos;

81};

82

84

[ 91](structnet__pkt.md)struct [net\_pkt](structnet__pkt.md) {

[ 96](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22) [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) [fifo](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22);

97

[ 99](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54) struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54);

100

102 union {

[ 103](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6) struct [net\_buf](structnet__buf.md) \*[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6);

[ 104](structnet__pkt.md#ad319458430aa691b88e24776e843d30b) struct [net\_buf](structnet__buf.md) \*[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b);

105 };

106

[ 108](structnet__pkt.md#a52f155a86698a929fa2130b594630d06) struct net\_pkt\_cursor [cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06);

109

[ 111](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf) struct [net\_context](structnet__context.md) \*[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf);

112

[ 114](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

115

117

118#if defined(CONFIG\_NET\_TCP)

120 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) next;

121#endif

122#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

123 struct [net\_if](structnet__if.md) \*orig\_iface; /\* Original network interface \*/

124#endif

125

126#if defined(CONFIG\_NET\_VPN)

127 struct {

129 struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

131 union net\_ip\_header ip\_hdr;

133 union net\_proto\_header proto\_hdr;

135 int peer\_id;

136 } vpn;

137#endif

138

139#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

158 struct [net\_ptp\_time](structnet__ptp__time.md) timestamp;

159#endif

160

161#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS) || \

162 defined(CONFIG\_TRACING\_NET\_CORE)

163 struct {

165 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time;

166

167#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

168 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

174 struct {

175 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stat](structstat.md)[NET\_PKT\_DETAIL\_STATS\_COUNT];

176 int count;

177 } detail;

178#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

179 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

180 };

181#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS \*/

182

183#if defined(CONFIG\_NET\_PKT\_ALLOC\_STATS)

184 struct net\_pkt\_alloc\_stats\_slab \*alloc\_stats;

185#endif /\* CONFIG\_NET\_PKT\_ALLOC\_STATS \*/

186

188 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) atomic\_ref;

189

190 /\* Filled by layer 2 when network packet is received. \*/

191 struct net\_linkaddr lladdr\_src;

192 struct net\_linkaddr lladdr\_dst;

193 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ll\_proto\_type;

194

195#if defined(CONFIG\_NET\_IP)

196 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_hdr\_len; /\* pre-filled in order to avoid func call \*/

197#endif

198

199 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) overwrite : 1; /\* Is packet content being overwritten? \*/

200 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) eof : 1; /\* Last packet before EOF \*/

201 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ptp\_pkt : 1; /\* For outgoing packet: is this packet

202 \* a L2 PTP packet.

203 \* Used only if defined (CONFIG\_NET\_L2\_PTP)

204 \*/

205 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) forwarding : 1; /\* Are we forwarding this pkt

206 \* Used only if defined(CONFIG\_NET\_ROUTE)

207 \*/

208 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family : 3; /\* Address family, see net\_ip.h \*/

209

210 /\* bitfield byte alignment boundary \*/

211

212#if defined(CONFIG\_NET\_IPV4\_ACD)

213 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_acd\_arp\_msg : 1; /\* Is this pkt IPv4 conflict detection ARP

214 \* message.

215 \* Note: family needs to be

216 \* AF\_INET.

217 \*/

218#endif

219#if defined(CONFIG\_NET\_LLDP)

220 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lldp\_pkt : 1; /\* Is this pkt an LLDP message.

221 \* Note: family needs to be

222 \* AF\_UNSPEC.

223 \*/

224#endif

225 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ppp\_msg : 1; /\* This is a PPP message \*/

226 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) captured : 1; /\* Set to 1 if this packet is already being

227 \* captured

228 \*/

229 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) l2\_bridged : 1; /\* set to 1 if this packet comes from a bridge

230 \* and already contains its L2 header to be

231 \* preserved. Useful only if

232 \* defined(CONFIG\_NET\_ETHERNET\_BRIDGE).

233 \*/

234 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) l2\_processed : 1; /\* Set to 1 if this packet has already been

235 \* processed by the L2

236 \*/

237 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chksum\_done : 1; /\* Checksum has already been computed for

238 \* the packet.

239 \*/

240#if defined(CONFIG\_NET\_IP\_FRAGMENT)

241 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_reassembled : 1; /\* Packet is a reassembled IP packet. \*/

242#endif

243#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

244 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_timestamping : 1;

245 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rx\_timestamping : 1;

246#endif

247 /\* bitfield byte alignment boundary \*/

248

249#if defined(CONFIG\_NET\_IP)

250 union {

251 /\* IPv6 hop limit or IPv4 ttl for this network packet.

252 \* The value is shared between IPv6 and IPv4.

253 \*/

254#if defined(CONFIG\_NET\_IPV6)

255 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_hop\_limit;

256#endif

257#if defined(CONFIG\_NET\_IPV4)

258 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_ttl;

259#endif

260 };

261

262 union {

263#if defined(CONFIG\_NET\_IPV4)

264 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_opts\_len; /\* length of IPv4 header options \*/

265#endif

266#if defined(CONFIG\_NET\_IPV6)

267 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ipv6\_ext\_len; /\* length of extension headers \*/

268#endif

269 };

270

271#if defined(CONFIG\_NET\_IP\_FRAGMENT)

272 union {

273#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

274 struct {

275 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* Fragment offset and M (More Fragment) flag \*/

276 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id; /\* Fragment ID \*/

277 } ipv4\_fragment;

278#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

279#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

280 struct {

281 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* Fragment offset and M (More Fragment) flag \*/

282 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id; /\* Fragment id \*/

283 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_start; /\* Where starts the fragment header \*/

284 } ipv6\_fragment;

285#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

286 };

287#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

288

289#if defined(CONFIG\_NET\_IPV6)

290 /\* Where is the start of the last header before payload data

291 \* in IPv6 packet. This is offset value from start of the IPv6

292 \* packet. Note that this value should be updated by who ever

293 \* adds IPv6 extension headers to the network packet.

294 \*/

295 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ipv6\_prev\_hdr\_start;

296

297 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_ext\_opt\_len; /\* IPv6 ND option length \*/

298 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_next\_hdr; /\* What is the very first next header \*/

299#endif /\* CONFIG\_NET\_IPV6 \*/

300

301#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

303 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_dscp : 6;

304

306 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_ecn : 2;

307#endif /\* CONFIG\_NET\_IP\_DSCP\_ECN \*/

308#endif /\* CONFIG\_NET\_IP \*/

309

310#if defined(CONFIG\_NET\_VLAN)

311 /\* VLAN TCI (Tag Control Information). This contains the Priority

312 \* Code Point (PCP), Drop Eligible Indicator (DEI) and VLAN

313 \* Identifier (VID, called more commonly VLAN tag). This value is

314 \* kept in host byte order.

315 \*/

316 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vlan\_tci;

317#endif /\* CONFIG\_NET\_VLAN \*/

318

319#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

320 /\* TODO: Evolve this into a union of orthogonal

321 \* control block declarations if further L2

322 \* stacks require L2-specific attributes.

323 \*/

324#if defined(CONFIG\_IEEE802154)

325 /\* The following structure requires a 4-byte alignment

326 \* boundary to avoid padding.

327 \*/

328 struct net\_pkt\_cb\_ieee802154 cb;

329#endif /\* CONFIG\_IEEE802154 \*/

330#endif /\* NET\_PKT\_HAS\_CONTROL\_BLOCK \*/

331

335 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority;

336

337#if defined(CONFIG\_NET\_OFFLOAD) || defined(CONFIG\_NET\_L2\_IPIP)

338 /\* Remote address of the received packet. This is only used by

339 \* network interfaces with an offloaded TCP/IP stack, or if we

340 \* have network tunneling in use.

341 \*/

342 union {

343 struct sockaddr remote;

344

345 /\* This will make sure that there is enough storage to store

346 \* the address struct. The access to value is via remote

347 \* address.

348 \*/

349 struct sockaddr\_storage remote\_storage;

350 };

351#endif /\* CONFIG\_NET\_OFFLOAD \*/

352

353#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

354 /\* Tell the capture api that this is a captured packet \*/

355 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cooked\_mode\_pkt : 1;

356#endif /\* CONFIG\_NET\_CAPTURE\_COOKED\_MODE \*/

357

358#if defined(CONFIG\_NET\_IPV4\_PMTU)

359 /\* Path MTU needed for this destination address \*/

360 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_pmtu : 1;

361#endif /\* CONFIG\_NET\_IPV4\_PMTU \*/

362

363 /\* @endcond \*/

364};

365

367

368/\* The interface real ll address \*/

369static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_if(struct [net\_pkt](structnet__pkt.md) \*pkt)

370{

371 return [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

372}

373

374static inline struct [net\_context](structnet__context.md) \*net\_pkt\_context(struct [net\_pkt](structnet__pkt.md) \*pkt)

375{

376 return pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf);

377}

378

379static inline void net\_pkt\_set\_context(struct [net\_pkt](structnet__pkt.md) \*pkt,

380 struct [net\_context](structnet__context.md) \*ctx)

381{

382 pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf) = ctx;

383}

384

385static inline struct [net\_if](structnet__if.md) \*net\_pkt\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

386{

387 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

388}

389

390static inline void net\_pkt\_set\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_if](structnet__if.md) \*iface)

391{

392 pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) = iface;

393

394 /\* If the network interface is set in pkt, then also set the type of

395 \* the network address that is stored in pkt. This is done here so

396 \* that the address type is properly set and is not forgotten.

397 \*/

398 if (iface) {

399 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type = [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

400

401 pkt->lladdr\_src.type = type;

402 pkt->lladdr\_dst.type = type;

403 }

404}

405

406static inline struct [net\_if](structnet__if.md) \*net\_pkt\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

407{

408#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

409 return pkt->orig\_iface;

410#else

411 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

412#endif

413}

414

415static inline void net\_pkt\_set\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt,

416 struct [net\_if](structnet__if.md) \*iface)

417{

418#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

419 pkt->orig\_iface = iface;

420#else

421 ARG\_UNUSED(pkt);

422 ARG\_UNUSED(iface);

423#endif

424}

425

426#if defined(CONFIG\_NET\_VPN)

427static inline struct [net\_if](structnet__if.md) \*net\_pkt\_vpn\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

428{

429 return pkt->vpn.[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

430}

431

432static inline void net\_pkt\_set\_vpn\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt,

433 struct [net\_if](structnet__if.md) \*iface)

434{

435 pkt->vpn.[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) = iface;

436}

437

438static inline union net\_ip\_header \*net\_pkt\_vpn\_ip\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

439{

440 return &pkt->vpn.ip\_hdr;

441}

442

443static inline void net\_pkt\_set\_vpn\_ip\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

444 union net\_ip\_header \*ip\_hdr)

445{

446 pkt->vpn.ip\_hdr = \*ip\_hdr;

447}

448

449static inline union net\_proto\_header \*net\_pkt\_vpn\_udp\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

450{

451 return &pkt->vpn.proto\_hdr;

452}

453

454static inline void net\_pkt\_set\_vpn\_udp\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

455 union net\_proto\_header \*proto\_hdr)

456{

457 pkt->vpn.proto\_hdr = \*proto\_hdr;

458}

459

460static inline int net\_pkt\_vpn\_peer\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

461{

462 return pkt->vpn.peer\_id;

463}

464

465static inline void net\_pkt\_set\_vpn\_peer\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

466 int peer\_id)

467{

468 pkt->vpn.peer\_id = peer\_id;

469}

470#endif /\* CONFIG\_NET\_VPN \*/

471

472static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_family(struct [net\_pkt](structnet__pkt.md) \*pkt)

473{

474 return pkt->family;

475}

476

477static inline void net\_pkt\_set\_family(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family)

478{

479 pkt->family = family;

480}

481

482static inline bool net\_pkt\_is\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt)

483{

484 return !!(pkt->ptp\_pkt);

485}

486

487static inline void net\_pkt\_set\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_ptp)

488{

489 pkt->ptp\_pkt = is\_ptp;

490}

491

492static inline bool net\_pkt\_is\_tx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt)

493{

494#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

495 return !!(pkt->tx\_timestamping);

496#else

497 ARG\_UNUSED(pkt);

498

499 return false;

500#endif

501}

502

503static inline void net\_pkt\_set\_tx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_timestamping)

504{

505#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

506 pkt->tx\_timestamping = is\_timestamping;

507#else

508 ARG\_UNUSED(pkt);

509 ARG\_UNUSED(is\_timestamping);

510#endif

511}

512

513static inline bool net\_pkt\_is\_rx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt)

514{

515#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

516 return !!(pkt->rx\_timestamping);

517#else

518 ARG\_UNUSED(pkt);

519

520 return false;

521#endif

522}

523

524static inline void net\_pkt\_set\_rx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_timestamping)

525{

526#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

527 pkt->rx\_timestamping = is\_timestamping;

528#else

529 ARG\_UNUSED(pkt);

530 ARG\_UNUSED(is\_timestamping);

531#endif

532}

533

534static inline bool net\_pkt\_is\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt)

535{

536 return !!(pkt->captured);

537}

538

539static inline void net\_pkt\_set\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_captured)

540{

541 pkt->captured = is\_captured;

542}

543

544static inline bool net\_pkt\_is\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt)

545{

546 return [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE) ? !!(pkt->l2\_bridged) : 0;

547}

548

549static inline void net\_pkt\_set\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_l2\_bridged)

550{

551 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE)) {

552 pkt->l2\_bridged = is\_l2\_bridged;

553 }

554}

555

556static inline bool net\_pkt\_is\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt)

557{

558 return !!(pkt->l2\_processed);

559}

560

561static inline void net\_pkt\_set\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt,

562 bool is\_l2\_processed)

563{

564 pkt->l2\_processed = is\_l2\_processed;

565}

566

567static inline bool net\_pkt\_is\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt)

568{

569 return !!(pkt->chksum\_done);

570}

571

572static inline void net\_pkt\_set\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt,

573 bool is\_chksum\_done)

574{

575 pkt->chksum\_done = is\_chksum\_done;

576}

577

578static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

579{

580#if defined(CONFIG\_NET\_IP)

581 return pkt->ip\_hdr\_len;

582#else

583 ARG\_UNUSED(pkt);

584

585 return 0;

586#endif

587}

588

589static inline void net\_pkt\_set\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

590{

591#if defined(CONFIG\_NET\_IP)

592 pkt->ip\_hdr\_len = len;

593#else

594 ARG\_UNUSED(pkt);

595 ARG\_UNUSED(len);

596#endif

597}

598

599static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt)

600{

601#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

602 return pkt->ip\_dscp;

603#else

604 ARG\_UNUSED(pkt);

605

606 return 0;

607#endif

608}

609

610static inline void net\_pkt\_set\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dscp)

611{

612#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

613 pkt->ip\_dscp = dscp;

614#else

615 ARG\_UNUSED(pkt);

616 ARG\_UNUSED(dscp);

617#endif

618}

619

620static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt)

621{

622#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

623 return pkt->ip\_ecn;

624#else

625 ARG\_UNUSED(pkt);

626

627 return 0;

628#endif

629}

630

631static inline void net\_pkt\_set\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ecn)

632{

633#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

634 pkt->ip\_ecn = ecn;

635#else

636 ARG\_UNUSED(pkt);

637 ARG\_UNUSED(ecn);

638#endif

639}

640

641static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt)

642{

643 return pkt->eof;

644}

645

646static inline void net\_pkt\_set\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt, bool eof)

647{

648 pkt->eof = eof;

649}

650

651static inline bool net\_pkt\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt)

652{

653 return !!(pkt->forwarding);

654}

655

656static inline void net\_pkt\_set\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt, bool forward)

657{

658 pkt->forwarding = forward;

659}

660

661#if defined(CONFIG\_NET\_IPV4)

662static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

663{

664 return pkt->ipv4\_ttl;

665}

666

667static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

668 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

669{

670 pkt->ipv4\_ttl = ttl;

671}

672

673static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

674{

675 return pkt->ipv4\_opts\_len;

676}

677

678static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

679 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

680{

681 pkt->ipv4\_opts\_len = opts\_len;

682}

683#else

684static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

685{

686 ARG\_UNUSED(pkt);

687

688 return 0;

689}

690

691static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

692 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

693{

694 ARG\_UNUSED(pkt);

695 ARG\_UNUSED(ttl);

696}

697

698static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

699{

700 ARG\_UNUSED(pkt);

701 return 0;

702}

703

704static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

705 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

706{

707 ARG\_UNUSED(pkt);

708 ARG\_UNUSED(opts\_len);

709}

710#endif

711

712#if defined(CONFIG\_NET\_IPV6)

713static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

714{

715 return pkt->ipv6\_ext\_opt\_len;

716}

717

718static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

719 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

720{

721 pkt->ipv6\_ext\_opt\_len = len;

722}

723

724static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

725{

726 return pkt->ipv6\_next\_hdr;

727}

728

729static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

730 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

731{

732 pkt->ipv6\_next\_hdr = next\_hdr;

733}

734

735static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

736{

737 return pkt->ipv6\_ext\_len;

738}

739

740static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

741{

742 pkt->ipv6\_ext\_len = len;

743}

744

745static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

746{

747 return pkt->ipv6\_prev\_hdr\_start;

748}

749

750static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

751 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

752{

753 pkt->ipv6\_prev\_hdr\_start = offset;

754}

755

756static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

757{

758 return pkt->ipv6\_hop\_limit;

759}

760

761static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

762 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

763{

764 pkt->ipv6\_hop\_limit = hop\_limit;

765}

766#else /\* CONFIG\_NET\_IPV6 \*/

767static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

768{

769 ARG\_UNUSED(pkt);

770

771 return 0;

772}

773

774static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

775 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

776{

777 ARG\_UNUSED(pkt);

778 ARG\_UNUSED(len);

779}

780

781static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

782{

783 ARG\_UNUSED(pkt);

784

785 return 0;

786}

787

788static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

789 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

790{

791 ARG\_UNUSED(pkt);

792 ARG\_UNUSED(next\_hdr);

793}

794

795static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

796{

797 ARG\_UNUSED(pkt);

798

799 return 0;

800}

801

802static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

803{

804 ARG\_UNUSED(pkt);

805 ARG\_UNUSED(len);

806}

807

808static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

809{

810 ARG\_UNUSED(pkt);

811

812 return 0;

813}

814

815static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

816 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

817{

818 ARG\_UNUSED(pkt);

819 ARG\_UNUSED(offset);

820}

821

822static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

823{

824 ARG\_UNUSED(pkt);

825

826 return 0;

827}

828

829static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

830 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

831{

832 ARG\_UNUSED(pkt);

833 ARG\_UNUSED(hop\_limit);

834}

835#endif /\* CONFIG\_NET\_IPV6 \*/

836

837static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ip\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

838{

839#if defined(CONFIG\_NET\_IPV6)

840 return pkt->ipv6\_ext\_len;

841#elif defined(CONFIG\_NET\_IPV4)

842 return pkt->ipv4\_opts\_len;

843#else

844 ARG\_UNUSED(pkt);

845

846 return 0;

847#endif

848}

849

850#if defined(CONFIG\_NET\_IPV4\_PMTU)

851static inline bool net\_pkt\_ipv4\_pmtu(struct [net\_pkt](structnet__pkt.md) \*pkt)

852{

853 return !!pkt->ipv4\_pmtu;

854}

855

856static inline void net\_pkt\_set\_ipv4\_pmtu(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

857{

858 pkt->ipv4\_pmtu = value;

859}

860#else

861static inline bool net\_pkt\_ipv4\_pmtu(struct [net\_pkt](structnet__pkt.md) \*pkt)

862{

863 ARG\_UNUSED(pkt);

864

865 return false;

866}

867

868static inline void net\_pkt\_set\_ipv4\_pmtu(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

869{

870 ARG\_UNUSED(pkt);

871 ARG\_UNUSED(value);

872}

873#endif /\* CONFIG\_NET\_IPV4\_PMTU \*/

874

875#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

876static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

877{

878 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_FRAGH\_OFFSET\_MASK) \* 8;

879}

880

881static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

882{

883 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_MORE\_FRAG\_MASK) != 0;

884}

885

886static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

887{

888 pkt->ipv4\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

889}

890

891static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

892{

893 return pkt->ipv4\_fragment.id;

894}

895

896static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

897{

898 pkt->ipv4\_fragment.id = id;

899}

900#else /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

901static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

902{

903 ARG\_UNUSED(pkt);

904

905 return 0;

906}

907

908static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

909{

910 ARG\_UNUSED(pkt);

911

912 return 0;

913}

914

915static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

916{

917 ARG\_UNUSED(pkt);

918 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

919}

920

921static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

922{

923 ARG\_UNUSED(pkt);

924

925 return 0;

926}

927

928static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

929{

930 ARG\_UNUSED(pkt);

931 ARG\_UNUSED(id);

932}

933#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

934

935#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

936static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

937{

938 return pkt->ipv6\_fragment.hdr\_start;

939}

940

941static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

942 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

943{

944 pkt->ipv6\_fragment.hdr\_start = start;

945}

946

947static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

948{

949 return pkt->ipv6\_fragment.flags & NET\_IPV6\_FRAGH\_OFFSET\_MASK;

950}

951static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

952{

953 return (pkt->ipv6\_fragment.flags & 0x01) != 0;

954}

955

956static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

957 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

958{

959 pkt->ipv6\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

960}

961

962static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

963{

964 return pkt->ipv6\_fragment.id;

965}

966

967static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

968 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

969{

970 pkt->ipv6\_fragment.id = id;

971}

972#else /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

973static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

974{

975 ARG\_UNUSED(pkt);

976

977 return 0;

978}

979

980static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

981 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

982{

983 ARG\_UNUSED(pkt);

984 ARG\_UNUSED(start);

985}

986

987static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

988{

989 ARG\_UNUSED(pkt);

990

991 return 0;

992}

993

994static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

995{

996 ARG\_UNUSED(pkt);

997

998 return 0;

999}

1000

1001static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

1002 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1003{

1004 ARG\_UNUSED(pkt);

1005 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1006}

1007

1008static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

1009{

1010 ARG\_UNUSED(pkt);

1011

1012 return 0;

1013}

1014

1015static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

1016 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

1017{

1018 ARG\_UNUSED(pkt);

1019 ARG\_UNUSED(id);

1020}

1021#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

1022

1023#if defined(CONFIG\_NET\_IP\_FRAGMENT)

1024static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

1025{

1026 return !!(pkt->ip\_reassembled);

1027}

1028

1029static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

1030 bool reassembled)

1031{

1032 pkt->ip\_reassembled = reassembled;

1033}

1034#else /\* CONFIG\_NET\_IP\_FRAGMENT \*/

1035static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

1036{

1037 ARG\_UNUSED(pkt);

1038

1039 return false;

1040}

1041

1042static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

1043 bool reassembled)

1044{

1045 ARG\_UNUSED(pkt);

1046 ARG\_UNUSED(reassembled);

1047}

1048#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

1049

1050static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

1051{

1052 return pkt->priority;

1053}

1054

1055static inline void net\_pkt\_set\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

1056 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

1057{

1058 pkt->priority = priority;

1059}

1060

1061#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

1062static inline bool net\_pkt\_is\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt)

1063{

1064 return pkt->cooked\_mode\_pkt;

1065}

1066

1067static inline void net\_pkt\_set\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

1068{

1069 pkt->cooked\_mode\_pkt = value;

1070}

1071#else

1072static inline bool net\_pkt\_is\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt)

1073{

1074 ARG\_UNUSED(pkt);

1075

1076 return false;

1077}

1078

1079static inline void net\_pkt\_set\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

1080{

1081 ARG\_UNUSED(pkt);

1082 ARG\_UNUSED(value);

1083}

1084#endif /\* CONFIG\_NET\_CAPTURE\_COOKED\_MODE \*/

1085

1086#if defined(CONFIG\_NET\_VLAN)

1087static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

1088{

1089 return [net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)(pkt->vlan\_tci);

1090}

1091

1092static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

1093{

1094 pkt->vlan\_tci = [net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)(pkt->vlan\_tci, tag);

1095}

1096

1097static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

1098{

1099 return [net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)(pkt->vlan\_tci);

1100}

1101

1102static inline void net\_pkt\_set\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

1103 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

1104{

1105 pkt->vlan\_tci = [net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)(pkt->vlan\_tci, priority);

1106}

1107

1108static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

1109{

1110 return [net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)(pkt->vlan\_tci);

1111}

1112

1113static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

1114{

1115 pkt->vlan\_tci = [net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)(pkt->vlan\_tci, dei);

1116}

1117

1118static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

1119{

1120 pkt->vlan\_tci = tci;

1121}

1122

1123static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

1124{

1125 return pkt->vlan\_tci;

1126}

1127#else

1128static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

1129{

1130 ARG\_UNUSED(pkt);

1131

1132 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70);

1133}

1134

1135static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

1136{

1137 ARG\_UNUSED(pkt);

1138 ARG\_UNUSED(tag);

1139}

1140

1141static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

1142{

1143 ARG\_UNUSED(pkt);

1144

1145 return 0;

1146}

1147

1148static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

1149{

1150 ARG\_UNUSED(pkt);

1151

1152 return false;

1153}

1154

1155static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

1156{

1157 ARG\_UNUSED(pkt);

1158 ARG\_UNUSED(dei);

1159}

1160

1161static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

1162{

1163 ARG\_UNUSED(pkt);

1164

1165 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70); /\* assumes priority is 0 \*/

1166}

1167

1168static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

1169{

1170 ARG\_UNUSED(pkt);

1171 ARG\_UNUSED(tci);

1172}

1173#endif

1174

1175#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

1176static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1177{

1178 return &pkt->timestamp;

1179}

1180

1181static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1182 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1183{

1184 pkt->timestamp.second = timestamp->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04);

1185 pkt->timestamp.nanosecond = timestamp->[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

1186}

1187

1188static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1189{

1190 return [net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)(&pkt->timestamp);

1191}

1192

1193static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1194{

1195 pkt->timestamp = [ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)(timestamp);

1196}

1197#else

1198static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1199{

1200 ARG\_UNUSED(pkt);

1201

1202 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1203}

1204

1205static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1206 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1207{

1208 ARG\_UNUSED(pkt);

1209 ARG\_UNUSED(timestamp);

1210}

1211

1212static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1213{

1214 ARG\_UNUSED(pkt);

1215

1216 return 0;

1217}

1218

1219static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1220{

1221 ARG\_UNUSED(pkt);

1222 ARG\_UNUSED(timestamp);

1223}

1224#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP || CONFIG\_NET\_PKT\_TXTIME \*/

1225

1226#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS) || \

1227 defined(CONFIG\_TRACING\_NET\_CORE)

1228

1229static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1230{

1231 return pkt->create\_time;

1232}

1233

1234static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1235 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1236{

1237 pkt->create\_time = create\_time;

1238}

1239#else

1240static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1241{

1242 ARG\_UNUSED(pkt);

1243

1244 return 0U;

1245}

1246

1247static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1248 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1249{

1250 ARG\_UNUSED(pkt);

1251 ARG\_UNUSED(create\_time);

1252}

1253#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS ||

1254 \* CONFIG\_TRACING\_NET\_CORE

1255 \*/

1256

1257#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

1258 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

1259static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1260{

1261 return pkt->detail.stat;

1262}

1263

1264static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1265{

1266 return pkt->detail.count;

1267}

1268

1269static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1270{

1271 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&pkt->detail, 0, sizeof(pkt->detail));

1272}

1273

1274static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt,

1275 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1276{

1277 if (pkt->detail.count >= NET\_PKT\_DETAIL\_STATS\_COUNT) {

1278 NET\_ERR("Detail stats count overflow (%d >= %d)",

1279 pkt->detail.count, NET\_PKT\_DETAIL\_STATS\_COUNT);

1280 return;

1281 }

1282

1283 pkt->detail.stat[pkt->detail.count++] = tick;

1284}

1285

1286#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1287#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1288#else

1289static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1290{

1291 ARG\_UNUSED(pkt);

1292

1293 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1294}

1295

1296static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1297{

1298 ARG\_UNUSED(pkt);

1299

1300 return 0;

1301}

1302

1303static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1304{

1305 ARG\_UNUSED(pkt);

1306}

1307

1308static inline void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1309{

1310 ARG\_UNUSED(pkt);

1311 ARG\_UNUSED(tick);

1312}

1313

1314#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick)

1315#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick)

1316#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

1317 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

1318

1319static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1320{

1321 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1322}

1323

1324static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_ip\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1325{

1326 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1327}

1328

1329static inline bool net\_pkt\_is\_empty(struct [net\_pkt](structnet__pkt.md) \*pkt)

1330{

1331 return !pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b) || !net\_pkt\_data(pkt) || pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b)->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38) == 0;

1332}

1333

1334static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_src(struct [net\_pkt](structnet__pkt.md) \*pkt)

1335{

1336 return &pkt->lladdr\_src;

1337}

1338

1339static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_dst(struct [net\_pkt](structnet__pkt.md) \*pkt)

1340{

1341 return &pkt->lladdr\_dst;

1342}

1343

1344static inline void net\_pkt\_lladdr\_swap(struct [net\_pkt](structnet__pkt.md) \*pkt)

1345{

1346 struct [net\_linkaddr](structnet__linkaddr.md) tmp;

1347

1348 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(tmp.addr,

1349 net\_pkt\_lladdr\_src(pkt)->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881),

1350 net\_pkt\_lladdr\_src(pkt)->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0));

1351 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(net\_pkt\_lladdr\_src(pkt)->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881),

1352 net\_pkt\_lladdr\_dst(pkt)->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881),

1353 net\_pkt\_lladdr\_dst(pkt)->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0));

1354 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(net\_pkt\_lladdr\_dst(pkt)->[addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881),

1355 tmp.addr,

1356 net\_pkt\_lladdr\_src(pkt)->[len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0));

1357}

1358

1359static inline void net\_pkt\_lladdr\_clear(struct [net\_pkt](structnet__pkt.md) \*pkt)

1360{

1361 (void)[net\_linkaddr\_clear](group__net__linkaddr.md#ga4061ecaf3b1c4c06968ef6a744de0185)(net\_pkt\_lladdr\_src(pkt));

1362 (void)[net\_linkaddr\_clear](group__net__linkaddr.md#ga4061ecaf3b1c4c06968ef6a744de0185)(net\_pkt\_lladdr\_dst(pkt));

1363}

1364

1365static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt)

1366{

1367 return pkt->ll\_proto\_type;

1368}

1369

1370static inline void net\_pkt\_set\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7))

1371{

1372 pkt->ll\_proto\_type = [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

1373}

1374

1375#if defined(CONFIG\_NET\_IPV4\_ACD)

1376static inline bool net\_pkt\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt)

1377{

1378 return !!(pkt->ipv4\_acd\_arp\_msg);

1379}

1380

1381static inline void net\_pkt\_set\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt,

1382 bool is\_acd\_arp\_msg)

1383{

1384 pkt->ipv4\_acd\_arp\_msg = is\_acd\_arp\_msg;

1385}

1386#else /\* CONFIG\_NET\_IPV4\_ACD \*/

1387static inline bool net\_pkt\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt)

1388{

1389 ARG\_UNUSED(pkt);

1390

1391 return false;

1392}

1393

1394static inline void net\_pkt\_set\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt,

1395 bool is\_acd\_arp\_msg)

1396{

1397 ARG\_UNUSED(pkt);

1398 ARG\_UNUSED(is\_acd\_arp\_msg);

1399}

1400#endif /\* CONFIG\_NET\_IPV4\_ACD \*/

1401

1402#if defined(CONFIG\_NET\_LLDP)

1403static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1404{

1405 return !!(pkt->lldp\_pkt);

1406}

1407

1408static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1409{

1410 pkt->lldp\_pkt = is\_lldp;

1411}

1412#else

1413static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1414{

1415 ARG\_UNUSED(pkt);

1416

1417 return false;

1418}

1419

1420static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1421{

1422 ARG\_UNUSED(pkt);

1423 ARG\_UNUSED(is\_lldp);

1424}

1425#endif /\* CONFIG\_NET\_LLDP \*/

1426

1427#if defined(CONFIG\_NET\_L2\_PPP)

1428static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1429{

1430 return !!(pkt->ppp\_msg);

1431}

1432

1433static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1434 bool is\_ppp\_msg)

1435{

1436 pkt->ppp\_msg = is\_ppp\_msg;

1437}

1438#else /\* CONFIG\_NET\_L2\_PPP \*/

1439static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1440{

1441 ARG\_UNUSED(pkt);

1442

1443 return false;

1444}

1445

1446static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1447 bool is\_ppp\_msg)

1448{

1449 ARG\_UNUSED(pkt);

1450 ARG\_UNUSED(is\_ppp\_msg);

1451}

1452#endif /\* CONFIG\_NET\_L2\_PPP \*/

1453

1454#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

1455static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1456{

1457 return &pkt->cb;

1458}

1459#else

1460static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1461{

1462 ARG\_UNUSED(pkt);

1463

1464 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1465}

1466#endif

1467

1468#define NET\_IPV6\_HDR(pkt) ((struct net\_ipv6\_hdr \*)net\_pkt\_ip\_data(pkt))

1469#define NET\_IPV4\_HDR(pkt) ((struct net\_ipv4\_hdr \*)net\_pkt\_ip\_data(pkt))

1470

1471static inline void net\_pkt\_set\_src\_ipv6\_addr(struct [net\_pkt](structnet__pkt.md) \*pkt)

1472{

1473 [net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)([net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)(

1474 net\_pkt\_context(pkt)),

1475 (struct [in6\_addr](structin6__addr.md) \*)NET\_IPV6\_HDR(pkt)->src);

1476}

1477

1478static inline void net\_pkt\_set\_overwrite(struct [net\_pkt](structnet__pkt.md) \*pkt, bool overwrite)

1479{

1480 pkt->overwrite = overwrite;

1481}

1482

1483static inline bool net\_pkt\_is\_being\_overwritten(struct [net\_pkt](structnet__pkt.md) \*pkt)

1484{

1485 return !!(pkt->overwrite);

1486}

1487

1488#ifdef CONFIG\_NET\_PKT\_FILTER

1489

1490bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1491bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1492

1493#else

1494

1495static inline bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1496{

1497 ARG\_UNUSED(pkt);

1498

1499 return true;

1500}

1501

1502static inline bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1503{

1504 ARG\_UNUSED(pkt);

1505

1506 return true;

1507}

1508

1509#endif /\* CONFIG\_NET\_PKT\_FILTER \*/

1510

1511#if defined(CONFIG\_NET\_PKT\_FILTER) && \

1512 (defined(CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK) || defined(CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK))

1513

1514bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1515

1516#else

1517

1518static inline bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1519{

1520 ARG\_UNUSED(pkt);

1521

1522 return true;

1523}

1524

1525#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK || CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK \*/

1526

1527#if defined(CONFIG\_NET\_PKT\_FILTER) && defined(CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK)

1528

1529bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1530

1531#else

1532

1533static inline bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1534{

1535 ARG\_UNUSED(pkt);

1536

1537 return true;

1538}

1539

1540#endif /\* CONFIG\_NET\_PKT\_FILTER && CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK \*/

1541

1542#if defined(CONFIG\_NET\_OFFLOAD) || defined(CONFIG\_NET\_L2\_IPIP)

1543static inline struct [sockaddr](structsockaddr.md) \*net\_pkt\_remote\_address(struct [net\_pkt](structnet__pkt.md) \*pkt)

1544{

1545 return &pkt->remote;

1546}

1547

1548static inline void net\_pkt\_set\_remote\_address(struct [net\_pkt](structnet__pkt.md) \*pkt,

1549 struct [sockaddr](structsockaddr.md) \*address,

1550 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) len)

1551{

1552 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&pkt->remote, address, len);

1553}

1554#endif /\* CONFIG\_NET\_OFFLOAD || CONFIG\_NET\_L2\_IPIP \*/

1555

1556/\* @endcond \*/

1557

[ 1571](group__net__pkt.md#gafc7e98d5b64d816faabcbaa2ec22a2bb)#define NET\_PKT\_SLAB\_DEFINE(name, count) \

1572 K\_MEM\_SLAB\_DEFINE(name, sizeof(struct net\_pkt), count, 4); \

1573 NET\_PKT\_ALLOC\_STATS\_DEFINE(pkt\_alloc\_stats\_##name, name)

1574

1576

1577/\* Backward compatibility macro \*/

1578#define NET\_PKT\_TX\_SLAB\_DEFINE(name, count) NET\_PKT\_SLAB\_DEFINE(name, count)

1579

1581

[ 1595](group__net__pkt.md#ga94ab6300b59d739c4e3c5604d3fbe8a5)#define NET\_PKT\_DATA\_POOL\_DEFINE(name, count) \

1596 NET\_BUF\_POOL\_DEFINE(name, count, CONFIG\_NET\_BUF\_DATA\_SIZE, \

1597 0, NULL)

1598

1600

1601#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC) || \

1602 (CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG)

1603#define NET\_PKT\_DEBUG\_ENABLED

1604#endif

1605

1606#if defined(NET\_PKT\_DEBUG\_ENABLED)

1607

1608/\* Debug versions of the net\_pkt functions that are used when tracking

1609 \* buffer usage.

1610 \*/

1611

1612struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_data\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1613 size\_t min\_len,

1614 [k\_timeout\_t](structk__timeout__t.md) timeout,

1615 const char \*caller,

1616 int line);

1617

1618#define net\_pkt\_get\_reserve\_data(pool, min\_len, timeout) \

1619 net\_pkt\_get\_reserve\_data\_debug(pool, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1620

1621struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_rx\_data\_debug(size\_t min\_len,

1622 [k\_timeout\_t](structk__timeout__t.md) timeout,

1623 const char \*caller,

1624 int line);

1625#define net\_pkt\_get\_reserve\_rx\_data(min\_len, timeout) \

1626 net\_pkt\_get\_reserve\_rx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1627

1628struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_tx\_data\_debug(size\_t min\_len,

1629 [k\_timeout\_t](structk__timeout__t.md) timeout,

1630 const char \*caller,

1631 int line);

1632#define net\_pkt\_get\_reserve\_tx\_data(min\_len, timeout) \

1633 net\_pkt\_get\_reserve\_tx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1634

1635struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_frag\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1636 [k\_timeout\_t](structk__timeout__t.md) timeout,

1637 const char \*caller, int line);

1638#define net\_pkt\_get\_frag(pkt, min\_len, timeout) \

1639 net\_pkt\_get\_frag\_debug(pkt, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1640

1641void net\_pkt\_unref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller, int line);

1642#define net\_pkt\_unref(pkt) net\_pkt\_unref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1643

1644struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_ref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller,

1645 int line);

1646#define net\_pkt\_ref(pkt) net\_pkt\_ref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1647

1648struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_ref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1649 const char \*caller, int line);

1650#define net\_pkt\_frag\_ref(frag) net\_pkt\_frag\_ref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1651

1652void net\_pkt\_frag\_unref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1653 const char \*caller, int line);

1654#define net\_pkt\_frag\_unref(frag) \

1655 net\_pkt\_frag\_unref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1656

1657struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_del\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1658 struct [net\_buf](structnet__buf.md) \*parent,

1659 struct [net\_buf](structnet__buf.md) \*frag,

1660 const char \*caller, int line);

1661#define net\_pkt\_frag\_del(pkt, parent, frag) \

1662 net\_pkt\_frag\_del\_debug(pkt, parent, frag, \_\_func\_\_, \_\_LINE\_\_)

1663

1664void net\_pkt\_frag\_add\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1665 const char \*caller, int line);

1666#define net\_pkt\_frag\_add(pkt, frag) \

1667 net\_pkt\_frag\_add\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1668

1669void net\_pkt\_frag\_insert\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1670 const char \*caller, int line);

1671#define net\_pkt\_frag\_insert(pkt, frag) \

1672 net\_pkt\_frag\_insert\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1673#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC ||

1674 \* CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

1675 \*/

1677

1678#if defined(NET\_PKT\_DEBUG\_ENABLED)

1686void [net\_pkt\_print\_frags](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1687#else

[ 1688](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)#define net\_pkt\_print\_frags(pkt)

1689#endif

1690

1691#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1706](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_data](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1707 size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1708#endif

1709

1710#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1725](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1726#endif

1727

1728#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1743](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_tx\_data](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1744#endif

1745

1746#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1759](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_frag](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1760 [k\_timeout\_t](structk__timeout__t.md) timeout);

1761#endif

1762

1763#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1773](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)void [net\_pkt\_unref](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1774#endif

1775

1776#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1786](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_ref](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1787#endif

1788

1789#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1799](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_ref](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)(struct [net\_buf](structnet__buf.md) \*frag);

1800#endif

1801

1802#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1808](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)void [net\_pkt\_frag\_unref](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)(struct [net\_buf](structnet__buf.md) \*frag);

1809#endif

1810

1811#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1822](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_del](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1823 struct [net\_buf](structnet__buf.md) \*parent,

1824 struct [net\_buf](structnet__buf.md) \*frag);

1825#endif

1826

1827#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1834](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)void [net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1835#endif

1836

1837#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1844](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)void [net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1845#endif

1846

[ 1853](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)void [net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1854

[ 1863](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)void [net\_pkt\_get\_info](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)(struct k\_mem\_slab \*\*rx,

1864 struct k\_mem\_slab \*\*tx,

1865 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*rx\_data,

1866 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*tx\_data);

1867

1869

1870#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC)

1874void net\_pkt\_print(void);

1875

1876typedef void (\*net\_pkt\_allocs\_cb\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1877 struct [net\_buf](structnet__buf.md) \*buf,

1878 const char \*func\_alloc,

1879 int line\_alloc,

1880 const char \*func\_free,

1881 int line\_free,

1882 bool in\_use,

1883 void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1884

1885void net\_pkt\_allocs\_foreach(net\_pkt\_allocs\_cb\_t cb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1886

1887const char \*net\_pkt\_slab2str(struct k\_mem\_slab \*slab);

1888const char \*net\_pkt\_pool2str(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool);

1889

1890#else

1891#define net\_pkt\_print(...)

1892#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC \*/

1893

1894/\* New allocator, and API are defined below.

1895 \* This will be simpler when time will come to get rid of former API above.

1896 \*/

1897#if defined(NET\_PKT\_DEBUG\_ENABLED)

1898

1899struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1900 const char \*caller, int line);

1901#define net\_pkt\_alloc(\_timeout) \

1902 net\_pkt\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1903

1904struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_from\_slab\_debug(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1905 [k\_timeout\_t](structk__timeout__t.md) timeout,

1906 const char \*caller, int line);

1907#define net\_pkt\_alloc\_from\_slab(\_slab, \_timeout) \

1908 net\_pkt\_alloc\_from\_slab\_debug(\_slab, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1909

1910struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1911 const char \*caller, int line);

1912#define net\_pkt\_rx\_alloc(\_timeout) \

1913 net\_pkt\_rx\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1914

1915struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1916 [k\_timeout\_t](structk__timeout__t.md) timeout,

1917 const char \*caller,

1918 int line);

1919#define net\_pkt\_alloc\_on\_iface(\_iface, \_timeout) \

1920 net\_pkt\_alloc\_on\_iface\_debug(\_iface, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1921

1922struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1923 [k\_timeout\_t](structk__timeout__t.md) timeout,

1924 const char \*caller,

1925 int line);

1926#define net\_pkt\_rx\_alloc\_on\_iface(\_iface, \_timeout) \

1927 net\_pkt\_rx\_alloc\_on\_iface\_debug(\_iface, \_timeout, \

1928 \_\_func\_\_, \_\_LINE\_\_)

1929

1930int net\_pkt\_alloc\_buffer\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1931 size\_t size,

1932 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1933 [k\_timeout\_t](structk__timeout__t.md) timeout,

1934 const char \*caller, int line);

1935#define net\_pkt\_alloc\_buffer(\_pkt, \_size, \_proto, \_timeout) \

1936 net\_pkt\_alloc\_buffer\_debug(\_pkt, \_size, \_proto, \_timeout, \

1937 \_\_func\_\_, \_\_LINE\_\_)

1938

1939int net\_pkt\_alloc\_buffer\_raw\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

1940 [k\_timeout\_t](structk__timeout__t.md) timeout,

1941 const char \*caller, int line);

1942#define net\_pkt\_alloc\_buffer\_raw(\_pkt, \_size, \_timeout) \

1943 net\_pkt\_alloc\_buffer\_raw\_debug(\_pkt, \_size, \_timeout, \

1944 \_\_func\_\_, \_\_LINE\_\_)

1945

1946struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1947 size\_t size,

1948 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1949 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1950 [k\_timeout\_t](structk__timeout__t.md) timeout,

1951 const char \*caller,

1952 int line);

1953#define net\_pkt\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1954 \_proto, \_timeout) \

1955 net\_pkt\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1956 \_proto, \_timeout, \

1957 \_\_func\_\_, \_\_LINE\_\_)

1958

1959struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1960 size\_t size,

1961 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1962 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1963 [k\_timeout\_t](structk__timeout__t.md) timeout,

1964 const char \*caller,

1965 int line);

1966#define net\_pkt\_rx\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1967 \_proto, \_timeout) \

1968 net\_pkt\_rx\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1969 \_proto, \_timeout, \

1970 \_\_func\_\_, \_\_LINE\_\_)

1971

1972int net\_pkt\_alloc\_buffer\_with\_reserve\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1973 size\_t size,

1974 size\_t reserve,

1975 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1976 [k\_timeout\_t](structk__timeout__t.md) timeout,

1977 const char \*caller,

1978 int line);

1979#define net\_pkt\_alloc\_buffer\_with\_reserve(\_pkt, \_size, \_reserve, \_proto, \_timeout) \

1980 net\_pkt\_alloc\_buffer\_with\_reserve\_debug(\_pkt, \_size, \_reserve, \_proto, \

1981 \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1982

1983#endif /\* NET\_PKT\_DEBUG\_ENABLED \*/

1985

1986#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1997](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)([k\_timeout\_t](structk__timeout__t.md) timeout);

1998#endif

1999

2000#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2015](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_from\_slab](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

2016 [k\_timeout\_t](structk__timeout__t.md) timeout);

2017#endif

2018

2019#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2030](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_alloc](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)([k\_timeout\_t](structk__timeout__t.md) timeout);

2031#endif

2032

2033#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2042](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_on\_iface](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2043 [k\_timeout\_t](structk__timeout__t.md) timeout);

2044

2046

2047/\* Same as above but specifically for RX packet \*/

2048struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2049 [k\_timeout\_t](structk__timeout__t.md) timeout);

2051

2052#endif

2053

2054#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2070](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)int [net\_pkt\_alloc\_buffer](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2071 size\_t size,

2072 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2073 [k\_timeout\_t](structk__timeout__t.md) timeout);

2074#endif

2075

2076#if !defined(NET\_PKT\_DEBUG\_ENABLED)

2094#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2095](group__net__pkt.md#ga0a292103ba0eacd62a15447e2765a485)int [net\_pkt\_alloc\_buffer\_with\_reserve](group__net__pkt.md#ga0a292103ba0eacd62a15447e2765a485)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2096 size\_t size,

2097 size\_t reserve,

2098 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2099 [k\_timeout\_t](structk__timeout__t.md) timeout);

2100#endif

2101

[ 2115](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)int [net\_pkt\_alloc\_buffer\_raw](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

2116 [k\_timeout\_t](structk__timeout__t.md) timeout);

2117#endif

2118

2119#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2131](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_with\_buffer](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2132 size\_t size,

2133 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

2134 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2135 [k\_timeout\_t](structk__timeout__t.md) timeout);

2136

2138

2139/\* Same as above but specifically for RX packet \*/

2140struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2141 size\_t size,

2142 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

2143 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2144 [k\_timeout\_t](structk__timeout__t.md) timeout);

2145

2147

2148#endif

2149

[ 2156](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)void [net\_pkt\_append\_buffer](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b));

2157

[ 2168](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)size\_t [net\_pkt\_available\_buffer](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2169

[ 2185](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)size\_t [net\_pkt\_available\_payload\_buffer](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2186 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto);

2187

[ 2196](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)void [net\_pkt\_trim\_buffer](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2197

[ 2212](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)int [net\_pkt\_remove\_tail](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2213

[ 2221](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)void [net\_pkt\_cursor\_init](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2222

[ 2229](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)static inline void [net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2230 struct net\_pkt\_cursor \*backup)

2231{

2232 backup->buf = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).buf;

2233 backup->pos = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos;

2234}

2235

[ 2242](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)static inline void [net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2243 struct net\_pkt\_cursor \*backup)

2244{

2245 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).buf = backup->buf;

2246 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos = backup->pos;

2247}

2248

[ 2256](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)static inline void \*[net\_pkt\_cursor\_get\_pos](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)(struct [net\_pkt](structnet__pkt.md) \*pkt)

2257{

2258 return pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos;

2259}

2260

[ 2281](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)int [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2282

[ 2297](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)int [net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)(struct [net\_pkt](structnet__pkt.md) \*pkt, int byte, size\_t length);

2298

[ 2312](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)int [net\_pkt\_copy](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)(struct [net\_pkt](structnet__pkt.md) \*pkt\_dst,

2313 struct [net\_pkt](structnet__pkt.md) \*pkt\_src,

2314 size\_t length);

2315

[ 2325](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_clone](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2326

[ 2336](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_clone](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2337

[ 2346](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_shallow\_clone](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2347 [k\_timeout\_t](structk__timeout__t.md) timeout);

2348

[ 2362](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)int [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(struct [net\_pkt](structnet__pkt.md) \*pkt, void \*data, size\_t length);

2363

[ 2376](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)static inline int [net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

2377{

2378 return [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(pkt, data, 1);

2379}

2380

[ 2393](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)int [net\_pkt\_read\_be16](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2394

[ 2407](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)int [net\_pkt\_read\_le16](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2408

[ 2421](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)int [net\_pkt\_read\_be32](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

2422

[ 2436](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)int [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(struct [net\_pkt](structnet__pkt.md) \*pkt, const void \*data, size\_t length);

2437

[ 2450](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)static inline int [net\_pkt\_write\_u8](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data)

2451{

2452 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data, sizeof([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)));

2453}

2454

[ 2467](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)static inline int [net\_pkt\_write\_be16](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2468{

2469 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_be16 = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(data);

2470

2471 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2472}

2473

[ 2486](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)static inline int [net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2487{

2488 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_be32 = [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(data);

2489

2490 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2491}

2492

[ 2505](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)static inline int [net\_pkt\_write\_le32](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2506{

2507 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_le32 = [sys\_cpu\_to\_le32](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)(data);

2508

2509 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2510}

2511

[ 2524](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)static inline int [net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2525{

2526 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_le16 = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)(data);

2527

2528 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2529}

2530

[ 2538](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)size\_t [net\_pkt\_remaining\_data](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2539

[ 2547](group__net__pkt.md#ga9401d109ba978087139436c8a79c9bb0)static inline size\_t [net\_pkt\_get\_len](group__net__pkt.md#ga9401d109ba978087139436c8a79c9bb0)(struct [net\_pkt](structnet__pkt.md) \*pkt)

2548{

2549 return [net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)(pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6));

2550}

2551

[ 2564](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)int [net\_pkt\_update\_length](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2565

[ 2579](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)int [net\_pkt\_pull](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2580

[ 2589](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_pkt\_get\_current\_offset](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2590

[ 2602](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)bool [net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size);

2603

[ 2612](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)size\_t [net\_pkt\_get\_contiguous\_len](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2613

2615

2616struct net\_pkt\_data\_access {

2617#if !defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2618 void \*data;

2619#endif

2620 const size\_t size;

2621};

2622

2623#if defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2624#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2625 struct net\_pkt\_data\_access \_name = { \

2626 .size = sizeof(\_type), \

2627 }

2628

2629#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2630 NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type)

2631

2632#else

2633#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2634 \_type \_hdr\_##\_name; \

2635 struct net\_pkt\_data\_access \_name = { \

2636 .data = &\_hdr\_##\_name, \

2637 .size = sizeof(\_type), \

2638 }

2639

2640#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2641 struct net\_pkt\_data\_access \_name = { \

2642 .data = NULL, \

2643 .size = sizeof(\_type), \

2644 }

2645

2646#endif /\* CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS \*/

2647

2649

[ 2663](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)void \*[net\_pkt\_get\_data](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2664 struct net\_pkt\_data\_access \*access);

2665

[ 2679](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)int [net\_pkt\_set\_data](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2680 struct net\_pkt\_data\_access \*access);

2681

[ 2686](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)static inline int [net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2687 struct net\_pkt\_data\_access \*access)

2688{

2689 return [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(pkt, access->size);

2690}

2691

2695

2696#ifdef \_\_cplusplus

2697}

2698#endif

2699

2700#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_PKT\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[ethernet\_vlan.h](ethernet__vlan_8h.md)

VLAN specific definitions.

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)

#define htons(x)

Convert 16-bit value from host to network byte order.

**Definition** net\_ip.h:124

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)

#define htonl(x)

Convert 32-bit value from host to network byte order.

**Definition** net\_ip.h:132

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:64

[net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)

static size\_t net\_buf\_frags\_len(const struct net\_buf \*buf)

Calculate amount of bytes stored in fragments.

**Definition** net\_buf.h:2667

[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)

static struct net\_if \* net\_context\_get\_iface(struct net\_context \*context)

Get network interface for this context.

**Definition** net\_context.h:747

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:1205

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2213

[net\_linkaddr\_clear](group__net__linkaddr.md#ga4061ecaf3b1c4c06968ef6a744de0185)

static int net\_linkaddr\_clear(struct net\_linkaddr \*lladdr)

Clear link address.

**Definition** net\_linkaddr.h:196

[net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)

void net\_pkt\_frag\_add(struct net\_pkt \*pkt, struct net\_buf \*frag)

Add a fragment to a packet at the end of its fragment list.

[net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)

static int net\_pkt\_write\_be32(struct net\_pkt \*pkt, uint32\_t data)

Write a uint32\_t big endian data to a net\_pkt.

**Definition** net\_pkt.h:2486

[net\_pkt\_alloc\_buffer\_with\_reserve](group__net__pkt.md#ga0a292103ba0eacd62a15447e2765a485)

int net\_pkt\_alloc\_buffer\_with\_reserve(struct net\_pkt \*pkt, size\_t size, size\_t reserve, enum net\_ip\_protocol proto, k\_timeout\_t timeout)

Allocate buffer for a net\_pkt and reserve some space in the first net\_buf.

[net\_pkt\_cursor\_init](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)

void net\_pkt\_cursor\_init(struct net\_pkt \*pkt)

Initialize net\_pkt cursor.

[net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)

int net\_pkt\_skip(struct net\_pkt \*pkt, size\_t length)

Skip some data from a net\_pkt.

[net\_pkt\_shallow\_clone](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)

struct net\_pkt \* net\_pkt\_shallow\_clone(struct net\_pkt \*pkt, k\_timeout\_t timeout)

Clone pkt and increase the refcount of its buffer.

[net\_pkt\_append\_buffer](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)

void net\_pkt\_append\_buffer(struct net\_pkt \*pkt, struct net\_buf \*buffer)

Append a buffer in packet.

[net\_pkt\_print\_frags](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)

#define net\_pkt\_print\_frags(pkt)

**Definition** net\_pkt.h:1688

[net\_pkt\_update\_length](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)

int net\_pkt\_update\_length(struct net\_pkt \*pkt, size\_t length)

Update the overall length of a packet.

[net\_pkt\_pull](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)

int net\_pkt\_pull(struct net\_pkt \*pkt, size\_t length)

Remove data from the start of the packet.

[net\_pkt\_copy](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)

int net\_pkt\_copy(struct net\_pkt \*pkt\_dst, struct net\_pkt \*pkt\_src, size\_t length)

Copy data from a packet into another one.

[net\_pkt\_rx\_alloc](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)

struct net\_pkt \* net\_pkt\_rx\_alloc(k\_timeout\_t timeout)

Allocate an initialized net\_pkt for RX.

[net\_pkt\_ref](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)

struct net\_pkt \* net\_pkt\_ref(struct net\_pkt \*pkt)

Increase the packet ref count.

[net\_pkt\_read\_be16](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)

int net\_pkt\_read\_be16(struct net\_pkt \*pkt, uint16\_t \*data)

Read uint16\_t big endian data from a net\_pkt.

[net\_pkt\_alloc\_buffer\_raw](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)

int net\_pkt\_alloc\_buffer\_raw(struct net\_pkt \*pkt, size\_t size, k\_timeout\_t timeout)

Allocate buffer for a net\_pkt, of specified size, w/o any additional preconditions.

[net\_pkt\_alloc\_with\_buffer](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)

struct net\_pkt \* net\_pkt\_alloc\_with\_buffer(struct net\_if \*iface, size\_t size, sa\_family\_t family, enum net\_ip\_protocol proto, k\_timeout\_t timeout)

Allocate a network packet and buffer at once.

[net\_pkt\_frag\_unref](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)

void net\_pkt\_frag\_unref(struct net\_buf \*frag)

Decrease the packet fragment ref count.

[net\_pkt\_rx\_clone](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)

struct net\_pkt \* net\_pkt\_rx\_clone(struct net\_pkt \*pkt, k\_timeout\_t timeout)

Clone pkt and its buffer.

[net\_pkt\_get\_reserve\_data](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)

struct net\_buf \* net\_pkt\_get\_reserve\_data(struct net\_buf\_pool \*pool, size\_t min\_len, k\_timeout\_t timeout)

Get a data buffer from a given pool.

[net\_pkt\_trim\_buffer](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)

void net\_pkt\_trim\_buffer(struct net\_pkt \*pkt)

Trim net\_pkt buffer.

[net\_pkt\_alloc\_on\_iface](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)

struct net\_pkt \* net\_pkt\_alloc\_on\_iface(struct net\_if \*iface, k\_timeout\_t timeout)

Allocate a network packet for a specific network interface.

[net\_pkt\_get\_info](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)

void net\_pkt\_get\_info(struct k\_mem\_slab \*\*rx, struct k\_mem\_slab \*\*tx, struct net\_buf\_pool \*\*rx\_data, struct net\_buf\_pool \*\*tx\_data)

Get information about predefined RX, TX and DATA pools.

[net\_pkt\_unref](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)

void net\_pkt\_unref(struct net\_pkt \*pkt)

Place packet back into the available packets slab.

[net\_pkt\_write\_be16](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)

static int net\_pkt\_write\_be16(struct net\_pkt \*pkt, uint16\_t data)

Write a uint16\_t big endian data to a net\_pkt.

**Definition** net\_pkt.h:2467

[net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)

struct net\_pkt \* net\_pkt\_alloc(k\_timeout\_t timeout)

Allocate an initialized net\_pkt.

[net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)

int net\_pkt\_read(struct net\_pkt \*pkt, void \*data, size\_t length)

Read some data from a net\_pkt.

[net\_pkt\_get\_len](group__net__pkt.md#ga9401d109ba978087139436c8a79c9bb0)

static size\_t net\_pkt\_get\_len(struct net\_pkt \*pkt)

Get the total amount of bytes stored in a packet.

**Definition** net\_pkt.h:2547

[net\_pkt\_frag\_del](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)

struct net\_buf \* net\_pkt\_frag\_del(struct net\_pkt \*pkt, struct net\_buf \*parent, struct net\_buf \*frag)

Delete existing fragment from a packet.

[net\_pkt\_set\_data](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)

int net\_pkt\_set\_data(struct net\_pkt \*pkt, struct net\_pkt\_data\_access \*access)

Set contiguous data into a network packet.

[net\_pkt\_get\_data](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)

void \* net\_pkt\_get\_data(struct net\_pkt \*pkt, struct net\_pkt\_data\_access \*access)

Get data from a network packet in a contiguous way.

[net\_pkt\_write\_u8](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)

static int net\_pkt\_write\_u8(struct net\_pkt \*pkt, uint8\_t data)

Write a byte (uint8\_t) data to a net\_pkt.

**Definition** net\_pkt.h:2450

[net\_pkt\_available\_payload\_buffer](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)

size\_t net\_pkt\_available\_payload\_buffer(struct net\_pkt \*pkt, enum net\_ip\_protocol proto)

Get available buffer space for payload from a pkt.

[net\_pkt\_read\_le16](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)

int net\_pkt\_read\_le16(struct net\_pkt \*pkt, uint16\_t \*data)

Read uint16\_t little endian data from a net\_pkt.

[net\_pkt\_read\_be32](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)

int net\_pkt\_read\_be32(struct net\_pkt \*pkt, uint32\_t \*data)

Read uint32\_t big endian data from a net\_pkt.

[net\_pkt\_remove\_tail](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)

int net\_pkt\_remove\_tail(struct net\_pkt \*pkt, size\_t length)

Remove length bytes from tail of packet.

[net\_pkt\_get\_reserve\_tx\_data](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)

struct net\_buf \* net\_pkt\_get\_reserve\_tx\_data(size\_t min\_len, k\_timeout\_t timeout)

Get TX DATA buffer from pool.

[net\_pkt\_cursor\_get\_pos](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)

static void \* net\_pkt\_cursor\_get\_pos(struct net\_pkt \*pkt)

Returns current position of the cursor.

**Definition** net\_pkt.h:2256

[net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)

void net\_pkt\_frag\_insert(struct net\_pkt \*pkt, struct net\_buf \*frag)

Insert a fragment to a packet at the beginning of its fragment list.

[net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)

int net\_pkt\_memset(struct net\_pkt \*pkt, int byte, size\_t length)

Memset some data in a net\_pkt.

[net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)

static void net\_pkt\_cursor\_backup(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Backup net\_pkt cursor.

**Definition** net\_pkt.h:2229

[net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)

void net\_pkt\_compact(struct net\_pkt \*pkt)

Compact the fragment list of a packet.

[net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)

static int net\_pkt\_acknowledge\_data(struct net\_pkt \*pkt, struct net\_pkt\_data\_access \*access)

Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrit...

**Definition** net\_pkt.h:2686

[net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)

static int net\_pkt\_write\_le16(struct net\_pkt \*pkt, uint16\_t data)

Write a uint16\_t little endian data to a net\_pkt.

**Definition** net\_pkt.h:2524

[net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)

static void net\_pkt\_cursor\_restore(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Restore net\_pkt cursor from a backup.

**Definition** net\_pkt.h:2242

[net\_pkt\_get\_current\_offset](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)

uint16\_t net\_pkt\_get\_current\_offset(struct net\_pkt \*pkt)

Get the actual offset in the packet from its cursor.

[net\_pkt\_remaining\_data](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)

size\_t net\_pkt\_remaining\_data(struct net\_pkt \*pkt)

Get the amount of data which can be read from current cursor position.

[net\_pkt\_alloc\_buffer](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)

int net\_pkt\_alloc\_buffer(struct net\_pkt \*pkt, size\_t size, enum net\_ip\_protocol proto, k\_timeout\_t timeout)

Allocate buffer for a net\_pkt.

[net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)

int net\_pkt\_write(struct net\_pkt \*pkt, const void \*data, size\_t length)

Write data into a net\_pkt.

[net\_pkt\_frag\_ref](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)

struct net\_buf \* net\_pkt\_frag\_ref(struct net\_buf \*frag)

Increase the packet fragment ref count.

[net\_pkt\_available\_buffer](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)

size\_t net\_pkt\_available\_buffer(struct net\_pkt \*pkt)

Get available buffer space from a pkt.

[net\_pkt\_clone](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)

struct net\_pkt \* net\_pkt\_clone(struct net\_pkt \*pkt, k\_timeout\_t timeout)

Clone pkt and its buffer.

[net\_pkt\_alloc\_from\_slab](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)

struct net\_pkt \* net\_pkt\_alloc\_from\_slab(struct k\_mem\_slab \*slab, k\_timeout\_t timeout)

Allocate an initialized net\_pkt from a specific slab.

[net\_pkt\_write\_le32](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)

static int net\_pkt\_write\_le32(struct net\_pkt \*pkt, uint32\_t data)

Write a uint32\_t little endian data to a net\_pkt.

**Definition** net\_pkt.h:2505

[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)

struct net\_buf \* net\_pkt\_get\_reserve\_rx\_data(size\_t min\_len, k\_timeout\_t timeout)

Get RX DATA buffer from pool.

[net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)

bool net\_pkt\_is\_contiguous(struct net\_pkt \*pkt, size\_t size)

Check if a data size could fit contiguously.

[net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)

static int net\_pkt\_read\_u8(struct net\_pkt \*pkt, uint8\_t \*data)

Read a byte (uint8\_t) from a net\_pkt.

**Definition** net\_pkt.h:2376

[net\_pkt\_get\_frag](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)

struct net\_buf \* net\_pkt\_get\_frag(struct net\_pkt \*pkt, size\_t min\_len, k\_timeout\_t timeout)

Get a data fragment that might be from user specific buffer pool or from global DATA pool.

[net\_pkt\_get\_contiguous\_len](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)

size\_t net\_pkt\_get\_contiguous\_len(struct net\_pkt \*pkt)

Get the contiguous buffer space.

[net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)

int64\_t net\_time\_t

Any occurrence of net\_time\_t specifies a concept of nanosecond resolution scalar time span,...

**Definition** net\_time.h:103

[net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)

static net\_time\_t net\_ptp\_time\_to\_ns(struct net\_ptp\_time \*ts)

Convert a PTP timestamp to a nanosecond precision timestamp, both related to the local network refere...

**Definition** ptp\_time.h:210

[ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)

static struct net\_ptp\_time ns\_to\_net\_ptp\_time(net\_time\_t nsec)

Convert a nanosecond precision timestamp to a PTP timestamp, both related to the local network refere...

**Definition** ptp\_time.h:231

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

[net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)

static uint16\_t net\_eth\_vlan\_set\_vid(uint16\_t tci, uint16\_t vid)

Set VLAN identifier to TCI.

**Definition** ethernet\_vlan.h:81

[net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)

static uint8\_t net\_eth\_vlan\_get\_dei(uint16\_t tci)

Get Drop Eligible Indicator from TCI.

**Definition** ethernet\_vlan.h:56

[NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70)

#define NET\_VLAN\_TAG\_UNSPEC

Unspecified VLAN tag value.

**Definition** ethernet\_vlan.h:32

[net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)

static uint16\_t net\_eth\_vlan\_set\_dei(uint16\_t tci, bool dei)

Set Drop Eligible Indicator to TCI.

**Definition** ethernet\_vlan.h:94

[net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)

static uint16\_t net\_eth\_vlan\_get\_vid(uint16\_t tci)

Get VLAN identifier from TCI.

**Definition** ethernet\_vlan.h:44

[net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)

static uint16\_t net\_eth\_vlan\_set\_pcp(uint16\_t tci, uint8\_t pcp)

Set Priority Code Point to TCI.

**Definition** ethernet\_vlan.h:107

[net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)

static uint8\_t net\_eth\_vlan\_get\_pcp(uint16\_t tci)

Get Priority Code Point from TCI.

**Definition** ethernet\_vlan.h:68

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[ieee802154\_pkt.h](ieee802154__pkt_8h.md)

Packet data common to all IEEE 802.15.4 L2 layers.

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:160

[types.h](include_2zephyr_2types_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[net\_context.h](net__context_8h.md)

Network context definitions.

[net\_core.h](net__core_8h.md)

Network core definitions.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[net\_linkaddr.h](net__linkaddr_8h.md)

Public API for network link address.

[net\_time.h](net__time_8h.md)

Representation of nanosecond resolution elapsed time and timestamps in the network stack.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[ptp\_time.h](ptp__time_8h.md)

Public functions for the Precision Time Protocol time specification.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)

\_\_INTPTR\_TYPE\_\_ intptr\_t

**Definition** stdint.h:104

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)

void \* memset(void \*buf, int c, size\_t n)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:143

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** net\_buf.h:1078

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

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

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:208

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:726

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:70

[net\_linkaddr::addr](structnet__linkaddr.md#a58de2645f8c7d31c97026f0bd5262881)

uint8\_t addr[6]

The array of bytes representing the address.

**Definition** net\_linkaddr.h:78

[net\_linkaddr::type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:72

[net\_linkaddr::len](structnet__linkaddr.md#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)

uint8\_t len

The real length of the ll address.

**Definition** net\_linkaddr.h:75

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

[net\_pkt::frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)

struct net\_buf \* frags

buffer fragment

**Definition** net\_pkt.h:103

[net\_pkt::context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf)

struct net\_context \* context

Network connection context.

**Definition** net\_pkt.h:111

[net\_pkt::cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06)

struct net\_pkt\_cursor cursor

Internal buffer iterator used for reading/writing.

**Definition** net\_pkt.h:108

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:114

[net\_pkt::fifo](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22)

intptr\_t fifo

The fifo is used by RX/TX threads and by socket layer.

**Definition** net\_pkt.h:96

[net\_pkt::buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b)

struct net\_buf \* buffer

alias to a buffer fragment

**Definition** net\_pkt.h:104

[net\_pkt::slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54)

struct k\_mem\_slab \* slab

Slab pointer from where it belongs to.

**Definition** net\_pkt.h:99

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:111

[net\_ptp\_time::nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e)

uint32\_t nanosecond

Nanoseconds.

**Definition** ptp\_time.h:134

[net\_ptp\_time::second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04)

uint64\_t second

Second value.

**Definition** ptp\_time.h:130

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:410

[stat](structstat.md)

**Definition** stat.h:57

[sys\_cpu\_to\_le32](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)

#define sys\_cpu\_to\_le32(val)

Convert 32-bit integer from host endianness to little-endian.

**Definition** byteorder.h:272

[sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)

#define sys\_cpu\_to\_le16(val)

Convert 16-bit integer from host endianness to little-endian.

**Definition** byteorder.h:268

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_pkt.h](net__pkt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
