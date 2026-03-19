---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__pkt_8h_source.html
original_path: doxygen/html/net__pkt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

126#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

145 struct [net\_ptp\_time](structnet__ptp__time.md) timestamp;

146#endif

147

148#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS) || \

149 defined(CONFIG\_TRACING\_NET\_CORE)

150 struct {

152 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time;

153

154#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

155 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

161 struct {

162 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stat](structstat.md)[NET\_PKT\_DETAIL\_STATS\_COUNT];

163 int count;

164 } detail;

165#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

166 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

167 };

168#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS \*/

169

170#if defined(CONFIG\_NET\_PKT\_ALLOC\_STATS)

171 struct net\_pkt\_alloc\_stats\_slab \*alloc\_stats;

172#endif /\* CONFIG\_NET\_PKT\_ALLOC\_STATS \*/

173

175 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) atomic\_ref;

176

177 /\* Filled by layer 2 when network packet is received. \*/

178 struct net\_linkaddr lladdr\_src;

179 struct net\_linkaddr lladdr\_dst;

180 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ll\_proto\_type;

181

182#if defined(CONFIG\_NET\_IP)

183 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_hdr\_len; /\* pre-filled in order to avoid func call \*/

184#endif

185

186 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) overwrite : 1; /\* Is packet content being overwritten? \*/

187 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) eof : 1; /\* Last packet before EOF \*/

188 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ptp\_pkt : 1; /\* For outgoing packet: is this packet

189 \* a L2 PTP packet.

190 \* Used only if defined (CONFIG\_NET\_L2\_PTP)

191 \*/

192 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) forwarding : 1; /\* Are we forwarding this pkt

193 \* Used only if defined(CONFIG\_NET\_ROUTE)

194 \*/

195 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family : 3; /\* Address family, see net\_ip.h \*/

196

197 /\* bitfield byte alignment boundary \*/

198

199#if defined(CONFIG\_NET\_IPV4\_ACD)

200 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_acd\_arp\_msg : 1; /\* Is this pkt IPv4 conflict detection ARP

201 \* message.

202 \* Note: family needs to be

203 \* AF\_INET.

204 \*/

205#endif

206#if defined(CONFIG\_NET\_LLDP)

207 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lldp\_pkt : 1; /\* Is this pkt an LLDP message.

208 \* Note: family needs to be

209 \* AF\_UNSPEC.

210 \*/

211#endif

212 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ppp\_msg : 1; /\* This is a PPP message \*/

213 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) captured : 1; /\* Set to 1 if this packet is already being

214 \* captured

215 \*/

216 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) l2\_bridged : 1; /\* set to 1 if this packet comes from a bridge

217 \* and already contains its L2 header to be

218 \* preserved. Useful only if

219 \* defined(CONFIG\_NET\_ETHERNET\_BRIDGE).

220 \*/

221 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) l2\_processed : 1; /\* Set to 1 if this packet has already been

222 \* processed by the L2

223 \*/

224 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chksum\_done : 1; /\* Checksum has already been computed for

225 \* the packet.

226 \*/

227#if defined(CONFIG\_NET\_IP\_FRAGMENT)

228 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_reassembled : 1; /\* Packet is a reassembled IP packet. \*/

229#endif

230#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

231 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_timestamping : 1;

232 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rx\_timestamping : 1;

233#endif

234 /\* bitfield byte alignment boundary \*/

235

236#if defined(CONFIG\_NET\_IP)

237 union {

238 /\* IPv6 hop limit or IPv4 ttl for this network packet.

239 \* The value is shared between IPv6 and IPv4.

240 \*/

241#if defined(CONFIG\_NET\_IPV6)

242 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_hop\_limit;

243#endif

244#if defined(CONFIG\_NET\_IPV4)

245 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_ttl;

246#endif

247 };

248

249 union {

250#if defined(CONFIG\_NET\_IPV4)

251 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_opts\_len; /\* length of IPv4 header options \*/

252#endif

253#if defined(CONFIG\_NET\_IPV6)

254 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ipv6\_ext\_len; /\* length of extension headers \*/

255#endif

256 };

257

258#if defined(CONFIG\_NET\_IP\_FRAGMENT)

259 union {

260#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

261 struct {

262 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* Fragment offset and M (More Fragment) flag \*/

263 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id; /\* Fragment ID \*/

264 } ipv4\_fragment;

265#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

266#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

267 struct {

268 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* Fragment offset and M (More Fragment) flag \*/

269 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id; /\* Fragment id \*/

270 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_start; /\* Where starts the fragment header \*/

271 } ipv6\_fragment;

272#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

273 };

274#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

275

276#if defined(CONFIG\_NET\_IPV6)

277 /\* Where is the start of the last header before payload data

278 \* in IPv6 packet. This is offset value from start of the IPv6

279 \* packet. Note that this value should be updated by who ever

280 \* adds IPv6 extension headers to the network packet.

281 \*/

282 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ipv6\_prev\_hdr\_start;

283

284 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_ext\_opt\_len; /\* IPv6 ND option length \*/

285 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_next\_hdr; /\* What is the very first next header \*/

286#endif /\* CONFIG\_NET\_IPV6 \*/

287

288#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

290 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_dscp : 6;

291

293 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_ecn : 2;

294#endif /\* CONFIG\_NET\_IP\_DSCP\_ECN \*/

295#endif /\* CONFIG\_NET\_IP \*/

296

297#if defined(CONFIG\_NET\_VLAN)

298 /\* VLAN TCI (Tag Control Information). This contains the Priority

299 \* Code Point (PCP), Drop Eligible Indicator (DEI) and VLAN

300 \* Identifier (VID, called more commonly VLAN tag). This value is

301 \* kept in host byte order.

302 \*/

303 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vlan\_tci;

304#endif /\* CONFIG\_NET\_VLAN \*/

305

306#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

307 /\* TODO: Evolve this into a union of orthogonal

308 \* control block declarations if further L2

309 \* stacks require L2-specific attributes.

310 \*/

311#if defined(CONFIG\_IEEE802154)

312 /\* The following structure requires a 4-byte alignment

313 \* boundary to avoid padding.

314 \*/

315 struct net\_pkt\_cb\_ieee802154 cb;

316#endif /\* CONFIG\_IEEE802154 \*/

317#endif /\* NET\_PKT\_HAS\_CONTROL\_BLOCK \*/

318

322 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority;

323

324#if defined(CONFIG\_NET\_OFFLOAD) || defined(CONFIG\_NET\_L2\_IPIP)

325 /\* Remote address of the received packet. This is only used by

326 \* network interfaces with an offloaded TCP/IP stack, or if we

327 \* have network tunneling in use.

328 \*/

329 union {

330 struct sockaddr remote;

331

332 /\* This will make sure that there is enough storage to store

333 \* the address struct. The access to value is via remote

334 \* address.

335 \*/

336 struct sockaddr\_storage remote\_storage;

337 };

338#endif /\* CONFIG\_NET\_OFFLOAD \*/

339

340#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

341 /\* Tell the capture api that this is a captured packet \*/

342 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cooked\_mode\_pkt : 1;

343#endif /\* CONFIG\_NET\_CAPTURE\_COOKED\_MODE \*/

344

345#if defined(CONFIG\_NET\_IPV4\_PMTU)

346 /\* Path MTU needed for this destination address \*/

347 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_pmtu : 1;

348#endif /\* CONFIG\_NET\_IPV4\_PMTU \*/

349

350 /\* @endcond \*/

351};

352

354

355/\* The interface real ll address \*/

356static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_if(struct [net\_pkt](structnet__pkt.md) \*pkt)

357{

358 return [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

359}

360

361static inline struct [net\_context](structnet__context.md) \*net\_pkt\_context(struct [net\_pkt](structnet__pkt.md) \*pkt)

362{

363 return pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf);

364}

365

366static inline void net\_pkt\_set\_context(struct [net\_pkt](structnet__pkt.md) \*pkt,

367 struct [net\_context](structnet__context.md) \*ctx)

368{

369 pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf) = ctx;

370}

371

372static inline struct [net\_if](structnet__if.md) \*net\_pkt\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

373{

374 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

375}

376

377static inline void net\_pkt\_set\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_if](structnet__if.md) \*iface)

378{

379 pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) = iface;

380

381 /\* If the network interface is set in pkt, then also set the type of

382 \* the network address that is stored in pkt. This is done here so

383 \* that the address type is properly set and is not forgotten.

384 \*/

385 if (iface) {

386 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type = [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

387

388 pkt->lladdr\_src.type = type;

389 pkt->lladdr\_dst.type = type;

390 }

391}

392

393static inline struct [net\_if](structnet__if.md) \*net\_pkt\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

394{

395#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

396 return pkt->orig\_iface;

397#else

398 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

399#endif

400}

401

402static inline void net\_pkt\_set\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt,

403 struct [net\_if](structnet__if.md) \*iface)

404{

405#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

406 pkt->orig\_iface = iface;

407#else

408 ARG\_UNUSED(pkt);

409 ARG\_UNUSED(iface);

410#endif

411}

412

413static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_family(struct [net\_pkt](structnet__pkt.md) \*pkt)

414{

415 return pkt->family;

416}

417

418static inline void net\_pkt\_set\_family(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family)

419{

420 pkt->family = family;

421}

422

423static inline bool net\_pkt\_is\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt)

424{

425 return !!(pkt->ptp\_pkt);

426}

427

428static inline void net\_pkt\_set\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_ptp)

429{

430 pkt->ptp\_pkt = is\_ptp;

431}

432

433static inline bool net\_pkt\_is\_tx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt)

434{

435#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

436 return !!(pkt->tx\_timestamping);

437#else

438 ARG\_UNUSED(pkt);

439

440 return false;

441#endif

442}

443

444static inline void net\_pkt\_set\_tx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_timestamping)

445{

446#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

447 pkt->tx\_timestamping = is\_timestamping;

448#else

449 ARG\_UNUSED(pkt);

450 ARG\_UNUSED(is\_timestamping);

451#endif

452}

453

454static inline bool net\_pkt\_is\_rx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt)

455{

456#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

457 return !!(pkt->rx\_timestamping);

458#else

459 ARG\_UNUSED(pkt);

460

461 return false;

462#endif

463}

464

465static inline void net\_pkt\_set\_rx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_timestamping)

466{

467#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

468 pkt->rx\_timestamping = is\_timestamping;

469#else

470 ARG\_UNUSED(pkt);

471 ARG\_UNUSED(is\_timestamping);

472#endif

473}

474

475static inline bool net\_pkt\_is\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt)

476{

477 return !!(pkt->captured);

478}

479

480static inline void net\_pkt\_set\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_captured)

481{

482 pkt->captured = is\_captured;

483}

484

485static inline bool net\_pkt\_is\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt)

486{

487 return [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE) ? !!(pkt->l2\_bridged) : 0;

488}

489

490static inline void net\_pkt\_set\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_l2\_bridged)

491{

492 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE)) {

493 pkt->l2\_bridged = is\_l2\_bridged;

494 }

495}

496

497static inline bool net\_pkt\_is\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt)

498{

499 return !!(pkt->l2\_processed);

500}

501

502static inline void net\_pkt\_set\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt,

503 bool is\_l2\_processed)

504{

505 pkt->l2\_processed = is\_l2\_processed;

506}

507

508static inline bool net\_pkt\_is\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt)

509{

510 return !!(pkt->chksum\_done);

511}

512

513static inline void net\_pkt\_set\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt,

514 bool is\_chksum\_done)

515{

516 pkt->chksum\_done = is\_chksum\_done;

517}

518

519static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

520{

521#if defined(CONFIG\_NET\_IP)

522 return pkt->ip\_hdr\_len;

523#else

524 ARG\_UNUSED(pkt);

525

526 return 0;

527#endif

528}

529

530static inline void net\_pkt\_set\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

531{

532#if defined(CONFIG\_NET\_IP)

533 pkt->ip\_hdr\_len = len;

534#else

535 ARG\_UNUSED(pkt);

536 ARG\_UNUSED(len);

537#endif

538}

539

540static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt)

541{

542#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

543 return pkt->ip\_dscp;

544#else

545 ARG\_UNUSED(pkt);

546

547 return 0;

548#endif

549}

550

551static inline void net\_pkt\_set\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dscp)

552{

553#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

554 pkt->ip\_dscp = dscp;

555#else

556 ARG\_UNUSED(pkt);

557 ARG\_UNUSED(dscp);

558#endif

559}

560

561static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt)

562{

563#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

564 return pkt->ip\_ecn;

565#else

566 ARG\_UNUSED(pkt);

567

568 return 0;

569#endif

570}

571

572static inline void net\_pkt\_set\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ecn)

573{

574#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

575 pkt->ip\_ecn = ecn;

576#else

577 ARG\_UNUSED(pkt);

578 ARG\_UNUSED(ecn);

579#endif

580}

581

582static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt)

583{

584 return pkt->eof;

585}

586

587static inline void net\_pkt\_set\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt, bool eof)

588{

589 pkt->eof = eof;

590}

591

592static inline bool net\_pkt\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt)

593{

594 return !!(pkt->forwarding);

595}

596

597static inline void net\_pkt\_set\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt, bool forward)

598{

599 pkt->forwarding = forward;

600}

601

602#if defined(CONFIG\_NET\_IPV4)

603static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

604{

605 return pkt->ipv4\_ttl;

606}

607

608static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

609 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

610{

611 pkt->ipv4\_ttl = ttl;

612}

613

614static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

615{

616 return pkt->ipv4\_opts\_len;

617}

618

619static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

620 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

621{

622 pkt->ipv4\_opts\_len = opts\_len;

623}

624#else

625static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

626{

627 ARG\_UNUSED(pkt);

628

629 return 0;

630}

631

632static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

633 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

634{

635 ARG\_UNUSED(pkt);

636 ARG\_UNUSED(ttl);

637}

638

639static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

640{

641 ARG\_UNUSED(pkt);

642 return 0;

643}

644

645static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

646 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

647{

648 ARG\_UNUSED(pkt);

649 ARG\_UNUSED(opts\_len);

650}

651#endif

652

653#if defined(CONFIG\_NET\_IPV6)

654static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

655{

656 return pkt->ipv6\_ext\_opt\_len;

657}

658

659static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

660 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

661{

662 pkt->ipv6\_ext\_opt\_len = len;

663}

664

665static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

666{

667 return pkt->ipv6\_next\_hdr;

668}

669

670static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

671 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

672{

673 pkt->ipv6\_next\_hdr = next\_hdr;

674}

675

676static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

677{

678 return pkt->ipv6\_ext\_len;

679}

680

681static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

682{

683 pkt->ipv6\_ext\_len = len;

684}

685

686static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

687{

688 return pkt->ipv6\_prev\_hdr\_start;

689}

690

691static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

692 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

693{

694 pkt->ipv6\_prev\_hdr\_start = offset;

695}

696

697static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

698{

699 return pkt->ipv6\_hop\_limit;

700}

701

702static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

703 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

704{

705 pkt->ipv6\_hop\_limit = hop\_limit;

706}

707#else /\* CONFIG\_NET\_IPV6 \*/

708static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

709{

710 ARG\_UNUSED(pkt);

711

712 return 0;

713}

714

715static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

716 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

717{

718 ARG\_UNUSED(pkt);

719 ARG\_UNUSED(len);

720}

721

722static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

723{

724 ARG\_UNUSED(pkt);

725

726 return 0;

727}

728

729static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

730 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

731{

732 ARG\_UNUSED(pkt);

733 ARG\_UNUSED(next\_hdr);

734}

735

736static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

737{

738 ARG\_UNUSED(pkt);

739

740 return 0;

741}

742

743static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

744{

745 ARG\_UNUSED(pkt);

746 ARG\_UNUSED(len);

747}

748

749static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

750{

751 ARG\_UNUSED(pkt);

752

753 return 0;

754}

755

756static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

757 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

758{

759 ARG\_UNUSED(pkt);

760 ARG\_UNUSED(offset);

761}

762

763static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

764{

765 ARG\_UNUSED(pkt);

766

767 return 0;

768}

769

770static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

771 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

772{

773 ARG\_UNUSED(pkt);

774 ARG\_UNUSED(hop\_limit);

775}

776#endif /\* CONFIG\_NET\_IPV6 \*/

777

778static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ip\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

779{

780#if defined(CONFIG\_NET\_IPV6)

781 return pkt->ipv6\_ext\_len;

782#elif defined(CONFIG\_NET\_IPV4)

783 return pkt->ipv4\_opts\_len;

784#else

785 ARG\_UNUSED(pkt);

786

787 return 0;

788#endif

789}

790

791#if defined(CONFIG\_NET\_IPV4\_PMTU)

792static inline bool net\_pkt\_ipv4\_pmtu(struct [net\_pkt](structnet__pkt.md) \*pkt)

793{

794 return !!pkt->ipv4\_pmtu;

795}

796

797static inline void net\_pkt\_set\_ipv4\_pmtu(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

798{

799 pkt->ipv4\_pmtu = value;

800}

801#else

802static inline bool net\_pkt\_ipv4\_pmtu(struct [net\_pkt](structnet__pkt.md) \*pkt)

803{

804 ARG\_UNUSED(pkt);

805

806 return false;

807}

808

809static inline void net\_pkt\_set\_ipv4\_pmtu(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

810{

811 ARG\_UNUSED(pkt);

812 ARG\_UNUSED(value);

813}

814#endif /\* CONFIG\_NET\_IPV4\_PMTU \*/

815

816#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

817static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

818{

819 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_FRAGH\_OFFSET\_MASK) \* 8;

820}

821

822static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

823{

824 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_MORE\_FRAG\_MASK) != 0;

825}

826

827static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

828{

829 pkt->ipv4\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

830}

831

832static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

833{

834 return pkt->ipv4\_fragment.id;

835}

836

837static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

838{

839 pkt->ipv4\_fragment.id = id;

840}

841#else /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

842static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

843{

844 ARG\_UNUSED(pkt);

845

846 return 0;

847}

848

849static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

850{

851 ARG\_UNUSED(pkt);

852

853 return 0;

854}

855

856static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

857{

858 ARG\_UNUSED(pkt);

859 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

860}

861

862static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

863{

864 ARG\_UNUSED(pkt);

865

866 return 0;

867}

868

869static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

870{

871 ARG\_UNUSED(pkt);

872 ARG\_UNUSED(id);

873}

874#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

875

876#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

877static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

878{

879 return pkt->ipv6\_fragment.hdr\_start;

880}

881

882static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

883 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

884{

885 pkt->ipv6\_fragment.hdr\_start = start;

886}

887

888static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

889{

890 return pkt->ipv6\_fragment.flags & NET\_IPV6\_FRAGH\_OFFSET\_MASK;

891}

892static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

893{

894 return (pkt->ipv6\_fragment.flags & 0x01) != 0;

895}

896

897static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

898 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

899{

900 pkt->ipv6\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

901}

902

903static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

904{

905 return pkt->ipv6\_fragment.id;

906}

907

908static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

909 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

910{

911 pkt->ipv6\_fragment.id = id;

912}

913#else /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

914static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

915{

916 ARG\_UNUSED(pkt);

917

918 return 0;

919}

920

921static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

922 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

923{

924 ARG\_UNUSED(pkt);

925 ARG\_UNUSED(start);

926}

927

928static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

929{

930 ARG\_UNUSED(pkt);

931

932 return 0;

933}

934

935static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

936{

937 ARG\_UNUSED(pkt);

938

939 return 0;

940}

941

942static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

943 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

944{

945 ARG\_UNUSED(pkt);

946 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

947}

948

949static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

950{

951 ARG\_UNUSED(pkt);

952

953 return 0;

954}

955

956static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

957 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

958{

959 ARG\_UNUSED(pkt);

960 ARG\_UNUSED(id);

961}

962#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

963

964#if defined(CONFIG\_NET\_IP\_FRAGMENT)

965static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

966{

967 return !!(pkt->ip\_reassembled);

968}

969

970static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

971 bool reassembled)

972{

973 pkt->ip\_reassembled = reassembled;

974}

975#else /\* CONFIG\_NET\_IP\_FRAGMENT \*/

976static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

977{

978 ARG\_UNUSED(pkt);

979

980 return false;

981}

982

983static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

984 bool reassembled)

985{

986 ARG\_UNUSED(pkt);

987 ARG\_UNUSED(reassembled);

988}

989#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

990

991static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

992{

993 return pkt->priority;

994}

995

996static inline void net\_pkt\_set\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

997 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

998{

999 pkt->priority = priority;

1000}

1001

1002#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

1003static inline bool net\_pkt\_is\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt)

1004{

1005 return pkt->cooked\_mode\_pkt;

1006}

1007

1008static inline void net\_pkt\_set\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

1009{

1010 pkt->cooked\_mode\_pkt = value;

1011}

1012#else

1013static inline bool net\_pkt\_is\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt)

1014{

1015 ARG\_UNUSED(pkt);

1016

1017 return false;

1018}

1019

1020static inline void net\_pkt\_set\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

1021{

1022 ARG\_UNUSED(pkt);

1023 ARG\_UNUSED(value);

1024}

1025#endif /\* CONFIG\_NET\_CAPTURE\_COOKED\_MODE \*/

1026

1027#if defined(CONFIG\_NET\_VLAN)

1028static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

1029{

1030 return [net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)(pkt->vlan\_tci);

1031}

1032

1033static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

1034{

1035 pkt->vlan\_tci = [net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)(pkt->vlan\_tci, tag);

1036}

1037

1038static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

1039{

1040 return [net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)(pkt->vlan\_tci);

1041}

1042

1043static inline void net\_pkt\_set\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

1044 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

1045{

1046 pkt->vlan\_tci = [net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)(pkt->vlan\_tci, priority);

1047}

1048

1049static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

1050{

1051 return [net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)(pkt->vlan\_tci);

1052}

1053

1054static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

1055{

1056 pkt->vlan\_tci = [net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)(pkt->vlan\_tci, dei);

1057}

1058

1059static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

1060{

1061 pkt->vlan\_tci = tci;

1062}

1063

1064static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

1065{

1066 return pkt->vlan\_tci;

1067}

1068#else

1069static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

1070{

1071 ARG\_UNUSED(pkt);

1072

1073 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70);

1074}

1075

1076static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

1077{

1078 ARG\_UNUSED(pkt);

1079 ARG\_UNUSED(tag);

1080}

1081

1082static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

1083{

1084 ARG\_UNUSED(pkt);

1085

1086 return 0;

1087}

1088

1089static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

1090{

1091 ARG\_UNUSED(pkt);

1092

1093 return false;

1094}

1095

1096static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

1097{

1098 ARG\_UNUSED(pkt);

1099 ARG\_UNUSED(dei);

1100}

1101

1102static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

1103{

1104 ARG\_UNUSED(pkt);

1105

1106 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70); /\* assumes priority is 0 \*/

1107}

1108

1109static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

1110{

1111 ARG\_UNUSED(pkt);

1112 ARG\_UNUSED(tci);

1113}

1114#endif

1115

1116#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

1117static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1118{

1119 return &pkt->timestamp;

1120}

1121

1122static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1123 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1124{

1125 pkt->timestamp.second = timestamp->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04);

1126 pkt->timestamp.nanosecond = timestamp->[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

1127}

1128

1129static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1130{

1131 return [net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)(&pkt->timestamp);

1132}

1133

1134static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1135{

1136 pkt->timestamp = [ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)(timestamp);

1137}

1138#else

1139static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1140{

1141 ARG\_UNUSED(pkt);

1142

1143 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1144}

1145

1146static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1147 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1148{

1149 ARG\_UNUSED(pkt);

1150 ARG\_UNUSED(timestamp);

1151}

1152

1153static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1154{

1155 ARG\_UNUSED(pkt);

1156

1157 return 0;

1158}

1159

1160static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1161{

1162 ARG\_UNUSED(pkt);

1163 ARG\_UNUSED(timestamp);

1164}

1165#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP || CONFIG\_NET\_PKT\_TXTIME \*/

1166

1167#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS) || \

1168 defined(CONFIG\_TRACING\_NET\_CORE)

1169

1170static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1171{

1172 return pkt->create\_time;

1173}

1174

1175static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1176 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1177{

1178 pkt->create\_time = create\_time;

1179}

1180#else

1181static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1182{

1183 ARG\_UNUSED(pkt);

1184

1185 return 0U;

1186}

1187

1188static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1189 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1190{

1191 ARG\_UNUSED(pkt);

1192 ARG\_UNUSED(create\_time);

1193}

1194#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS ||

1195 \* CONFIG\_TRACING\_NET\_CORE

1196 \*/

1197

1198#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

1199 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

1200static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1201{

1202 return pkt->detail.stat;

1203}

1204

1205static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1206{

1207 return pkt->detail.count;

1208}

1209

1210static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1211{

1212 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&pkt->detail, 0, sizeof(pkt->detail));

1213}

1214

1215static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt,

1216 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1217{

1218 if (pkt->detail.count >= NET\_PKT\_DETAIL\_STATS\_COUNT) {

1219 NET\_ERR("Detail stats count overflow (%d >= %d)",

1220 pkt->detail.count, NET\_PKT\_DETAIL\_STATS\_COUNT);

1221 return;

1222 }

1223

1224 pkt->detail.stat[pkt->detail.count++] = tick;

1225}

1226

1227#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1228#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1229#else

1230static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1231{

1232 ARG\_UNUSED(pkt);

1233

1234 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1235}

1236

1237static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1238{

1239 ARG\_UNUSED(pkt);

1240

1241 return 0;

1242}

1243

1244static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1245{

1246 ARG\_UNUSED(pkt);

1247}

1248

1249static inline void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1250{

1251 ARG\_UNUSED(pkt);

1252 ARG\_UNUSED(tick);

1253}

1254

1255#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick)

1256#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick)

1257#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

1258 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

1259

1260static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1261{

1262 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1263}

1264

1265static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_ip\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1266{

1267 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1268}

1269

1270static inline bool net\_pkt\_is\_empty(struct [net\_pkt](structnet__pkt.md) \*pkt)

1271{

1272 return !pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b) || !net\_pkt\_data(pkt) || pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b)->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38) == 0;

1273}

1274

1275static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_src(struct [net\_pkt](structnet__pkt.md) \*pkt)

1276{

1277 return &pkt->lladdr\_src;

1278}

1279

1280static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_dst(struct [net\_pkt](structnet__pkt.md) \*pkt)

1281{

1282 return &pkt->lladdr\_dst;

1283}

1284

1285static inline void net\_pkt\_lladdr\_swap(struct [net\_pkt](structnet__pkt.md) \*pkt)

1286{

1287 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) = net\_pkt\_lladdr\_src(pkt)->addr;

1288

1289 net\_pkt\_lladdr\_src(pkt)->addr = net\_pkt\_lladdr\_dst(pkt)->addr;

1290 net\_pkt\_lladdr\_dst(pkt)->addr = [addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0);

1291}

1292

1293static inline void net\_pkt\_lladdr\_clear(struct [net\_pkt](structnet__pkt.md) \*pkt)

1294{

1295 net\_pkt\_lladdr\_src(pkt)->addr = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1296 net\_pkt\_lladdr\_src(pkt)->len = 0U;

1297}

1298

1299static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt)

1300{

1301 return pkt->ll\_proto\_type;

1302}

1303

1304static inline void net\_pkt\_set\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7))

1305{

1306 pkt->ll\_proto\_type = [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

1307}

1308

1309#if defined(CONFIG\_NET\_IPV4\_ACD)

1310static inline bool net\_pkt\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt)

1311{

1312 return !!(pkt->ipv4\_acd\_arp\_msg);

1313}

1314

1315static inline void net\_pkt\_set\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt,

1316 bool is\_acd\_arp\_msg)

1317{

1318 pkt->ipv4\_acd\_arp\_msg = is\_acd\_arp\_msg;

1319}

1320#else /\* CONFIG\_NET\_IPV4\_ACD \*/

1321static inline bool net\_pkt\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt)

1322{

1323 ARG\_UNUSED(pkt);

1324

1325 return false;

1326}

1327

1328static inline void net\_pkt\_set\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt,

1329 bool is\_acd\_arp\_msg)

1330{

1331 ARG\_UNUSED(pkt);

1332 ARG\_UNUSED(is\_acd\_arp\_msg);

1333}

1334#endif /\* CONFIG\_NET\_IPV4\_ACD \*/

1335

1336#if defined(CONFIG\_NET\_LLDP)

1337static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1338{

1339 return !!(pkt->lldp\_pkt);

1340}

1341

1342static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1343{

1344 pkt->lldp\_pkt = is\_lldp;

1345}

1346#else

1347static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1348{

1349 ARG\_UNUSED(pkt);

1350

1351 return false;

1352}

1353

1354static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1355{

1356 ARG\_UNUSED(pkt);

1357 ARG\_UNUSED(is\_lldp);

1358}

1359#endif /\* CONFIG\_NET\_LLDP \*/

1360

1361#if defined(CONFIG\_NET\_L2\_PPP)

1362static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1363{

1364 return !!(pkt->ppp\_msg);

1365}

1366

1367static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1368 bool is\_ppp\_msg)

1369{

1370 pkt->ppp\_msg = is\_ppp\_msg;

1371}

1372#else /\* CONFIG\_NET\_L2\_PPP \*/

1373static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1374{

1375 ARG\_UNUSED(pkt);

1376

1377 return false;

1378}

1379

1380static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1381 bool is\_ppp\_msg)

1382{

1383 ARG\_UNUSED(pkt);

1384 ARG\_UNUSED(is\_ppp\_msg);

1385}

1386#endif /\* CONFIG\_NET\_L2\_PPP \*/

1387

1388#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

1389static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1390{

1391 return &pkt->cb;

1392}

1393#else

1394static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1395{

1396 ARG\_UNUSED(pkt);

1397

1398 return [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

1399}

1400#endif

1401

1402#define NET\_IPV6\_HDR(pkt) ((struct net\_ipv6\_hdr \*)net\_pkt\_ip\_data(pkt))

1403#define NET\_IPV4\_HDR(pkt) ((struct net\_ipv4\_hdr \*)net\_pkt\_ip\_data(pkt))

1404

1405static inline void net\_pkt\_set\_src\_ipv6\_addr(struct [net\_pkt](structnet__pkt.md) \*pkt)

1406{

1407 [net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)([net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)(

1408 net\_pkt\_context(pkt)),

1409 (struct [in6\_addr](structin6__addr.md) \*)NET\_IPV6\_HDR(pkt)->src);

1410}

1411

1412static inline void net\_pkt\_set\_overwrite(struct [net\_pkt](structnet__pkt.md) \*pkt, bool overwrite)

1413{

1414 pkt->overwrite = overwrite;

1415}

1416

1417static inline bool net\_pkt\_is\_being\_overwritten(struct [net\_pkt](structnet__pkt.md) \*pkt)

1418{

1419 return !!(pkt->overwrite);

1420}

1421

1422#ifdef CONFIG\_NET\_PKT\_FILTER

1423

1424bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1425bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1426

1427#else

1428

1429static inline bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1430{

1431 ARG\_UNUSED(pkt);

1432

1433 return true;

1434}

1435

1436static inline bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1437{

1438 ARG\_UNUSED(pkt);

1439

1440 return true;

1441}

1442

1443#endif /\* CONFIG\_NET\_PKT\_FILTER \*/

1444

1445#if defined(CONFIG\_NET\_PKT\_FILTER) && \

1446 (defined(CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK) || defined(CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK))

1447

1448bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1449

1450#else

1451

1452static inline bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1453{

1454 ARG\_UNUSED(pkt);

1455

1456 return true;

1457}

1458

1459#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK || CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK \*/

1460

1461#if defined(CONFIG\_NET\_PKT\_FILTER) && defined(CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK)

1462

1463bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1464

1465#else

1466

1467static inline bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1468{

1469 ARG\_UNUSED(pkt);

1470

1471 return true;

1472}

1473

1474#endif /\* CONFIG\_NET\_PKT\_FILTER && CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK \*/

1475

1476#if defined(CONFIG\_NET\_OFFLOAD) || defined(CONFIG\_NET\_L2\_IPIP)

1477static inline struct [sockaddr](structsockaddr.md) \*net\_pkt\_remote\_address(struct [net\_pkt](structnet__pkt.md) \*pkt)

1478{

1479 return &pkt->remote;

1480}

1481

1482static inline void net\_pkt\_set\_remote\_address(struct [net\_pkt](structnet__pkt.md) \*pkt,

1483 struct [sockaddr](structsockaddr.md) \*address,

1484 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) len)

1485{

1486 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&pkt->remote, address, len);

1487}

1488#endif /\* CONFIG\_NET\_OFFLOAD || CONFIG\_NET\_L2\_IPIP \*/

1489

1490/\* @endcond \*/

1491

[ 1505](group__net__pkt.md#gafc7e98d5b64d816faabcbaa2ec22a2bb)#define NET\_PKT\_SLAB\_DEFINE(name, count) \

1506 K\_MEM\_SLAB\_DEFINE(name, sizeof(struct net\_pkt), count, 4); \

1507 NET\_PKT\_ALLOC\_STATS\_DEFINE(pkt\_alloc\_stats\_##name, name)

1508

1510

1511/\* Backward compatibility macro \*/

1512#define NET\_PKT\_TX\_SLAB\_DEFINE(name, count) NET\_PKT\_SLAB\_DEFINE(name, count)

1513

1515

[ 1529](group__net__pkt.md#ga94ab6300b59d739c4e3c5604d3fbe8a5)#define NET\_PKT\_DATA\_POOL\_DEFINE(name, count) \

1530 NET\_BUF\_POOL\_DEFINE(name, count, CONFIG\_NET\_BUF\_DATA\_SIZE, \

1531 0, NULL)

1532

1534

1535#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC) || \

1536 (CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG)

1537#define NET\_PKT\_DEBUG\_ENABLED

1538#endif

1539

1540#if defined(NET\_PKT\_DEBUG\_ENABLED)

1541

1542/\* Debug versions of the net\_pkt functions that are used when tracking

1543 \* buffer usage.

1544 \*/

1545

1546struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_data\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1547 size\_t min\_len,

1548 [k\_timeout\_t](structk__timeout__t.md) timeout,

1549 const char \*caller,

1550 int line);

1551

1552#define net\_pkt\_get\_reserve\_data(pool, min\_len, timeout) \

1553 net\_pkt\_get\_reserve\_data\_debug(pool, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1554

1555struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_rx\_data\_debug(size\_t min\_len,

1556 [k\_timeout\_t](structk__timeout__t.md) timeout,

1557 const char \*caller,

1558 int line);

1559#define net\_pkt\_get\_reserve\_rx\_data(min\_len, timeout) \

1560 net\_pkt\_get\_reserve\_rx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1561

1562struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_tx\_data\_debug(size\_t min\_len,

1563 [k\_timeout\_t](structk__timeout__t.md) timeout,

1564 const char \*caller,

1565 int line);

1566#define net\_pkt\_get\_reserve\_tx\_data(min\_len, timeout) \

1567 net\_pkt\_get\_reserve\_tx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1568

1569struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_frag\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1570 [k\_timeout\_t](structk__timeout__t.md) timeout,

1571 const char \*caller, int line);

1572#define net\_pkt\_get\_frag(pkt, min\_len, timeout) \

1573 net\_pkt\_get\_frag\_debug(pkt, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1574

1575void net\_pkt\_unref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller, int line);

1576#define net\_pkt\_unref(pkt) net\_pkt\_unref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1577

1578struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_ref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller,

1579 int line);

1580#define net\_pkt\_ref(pkt) net\_pkt\_ref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1581

1582struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_ref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1583 const char \*caller, int line);

1584#define net\_pkt\_frag\_ref(frag) net\_pkt\_frag\_ref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1585

1586void net\_pkt\_frag\_unref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1587 const char \*caller, int line);

1588#define net\_pkt\_frag\_unref(frag) \

1589 net\_pkt\_frag\_unref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1590

1591struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_del\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1592 struct [net\_buf](structnet__buf.md) \*parent,

1593 struct [net\_buf](structnet__buf.md) \*frag,

1594 const char \*caller, int line);

1595#define net\_pkt\_frag\_del(pkt, parent, frag) \

1596 net\_pkt\_frag\_del\_debug(pkt, parent, frag, \_\_func\_\_, \_\_LINE\_\_)

1597

1598void net\_pkt\_frag\_add\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1599 const char \*caller, int line);

1600#define net\_pkt\_frag\_add(pkt, frag) \

1601 net\_pkt\_frag\_add\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1602

1603void net\_pkt\_frag\_insert\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1604 const char \*caller, int line);

1605#define net\_pkt\_frag\_insert(pkt, frag) \

1606 net\_pkt\_frag\_insert\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1607#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC ||

1608 \* CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

1609 \*/

1611

1612#if defined(NET\_PKT\_DEBUG\_ENABLED)

1620void [net\_pkt\_print\_frags](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1621#else

[ 1622](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)#define net\_pkt\_print\_frags(pkt)

1623#endif

1624

1625#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1640](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_data](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1641 size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1642#endif

1643

1644#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1659](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1660#endif

1661

1662#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1677](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_tx\_data](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1678#endif

1679

1680#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1693](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_frag](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1694 [k\_timeout\_t](structk__timeout__t.md) timeout);

1695#endif

1696

1697#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1707](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)void [net\_pkt\_unref](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1708#endif

1709

1710#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1720](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_ref](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1721#endif

1722

1723#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1733](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_ref](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)(struct [net\_buf](structnet__buf.md) \*frag);

1734#endif

1735

1736#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1742](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)void [net\_pkt\_frag\_unref](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)(struct [net\_buf](structnet__buf.md) \*frag);

1743#endif

1744

1745#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1756](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_del](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1757 struct [net\_buf](structnet__buf.md) \*parent,

1758 struct [net\_buf](structnet__buf.md) \*frag);

1759#endif

1760

1761#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1768](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)void [net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1769#endif

1770

1771#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1778](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)void [net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1779#endif

1780

[ 1787](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)void [net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1788

[ 1797](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)void [net\_pkt\_get\_info](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)(struct k\_mem\_slab \*\*rx,

1798 struct k\_mem\_slab \*\*tx,

1799 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*rx\_data,

1800 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*tx\_data);

1801

1803

1804#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC)

1808void net\_pkt\_print(void);

1809

1810typedef void (\*net\_pkt\_allocs\_cb\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1811 struct [net\_buf](structnet__buf.md) \*buf,

1812 const char \*func\_alloc,

1813 int line\_alloc,

1814 const char \*func\_free,

1815 int line\_free,

1816 bool in\_use,

1817 void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1818

1819void net\_pkt\_allocs\_foreach(net\_pkt\_allocs\_cb\_t cb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1820

1821const char \*net\_pkt\_slab2str(struct k\_mem\_slab \*slab);

1822const char \*net\_pkt\_pool2str(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool);

1823

1824#else

1825#define net\_pkt\_print(...)

1826#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC \*/

1827

1828/\* New allocator, and API are defined below.

1829 \* This will be simpler when time will come to get rid of former API above.

1830 \*/

1831#if defined(NET\_PKT\_DEBUG\_ENABLED)

1832

1833struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1834 const char \*caller, int line);

1835#define net\_pkt\_alloc(\_timeout) \

1836 net\_pkt\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1837

1838struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_from\_slab\_debug(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1839 [k\_timeout\_t](structk__timeout__t.md) timeout,

1840 const char \*caller, int line);

1841#define net\_pkt\_alloc\_from\_slab(\_slab, \_timeout) \

1842 net\_pkt\_alloc\_from\_slab\_debug(\_slab, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1843

1844struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1845 const char \*caller, int line);

1846#define net\_pkt\_rx\_alloc(\_timeout) \

1847 net\_pkt\_rx\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1848

1849struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1850 [k\_timeout\_t](structk__timeout__t.md) timeout,

1851 const char \*caller,

1852 int line);

1853#define net\_pkt\_alloc\_on\_iface(\_iface, \_timeout) \

1854 net\_pkt\_alloc\_on\_iface\_debug(\_iface, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1855

1856struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1857 [k\_timeout\_t](structk__timeout__t.md) timeout,

1858 const char \*caller,

1859 int line);

1860#define net\_pkt\_rx\_alloc\_on\_iface(\_iface, \_timeout) \

1861 net\_pkt\_rx\_alloc\_on\_iface\_debug(\_iface, \_timeout, \

1862 \_\_func\_\_, \_\_LINE\_\_)

1863

1864int net\_pkt\_alloc\_buffer\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1865 size\_t size,

1866 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1867 [k\_timeout\_t](structk__timeout__t.md) timeout,

1868 const char \*caller, int line);

1869#define net\_pkt\_alloc\_buffer(\_pkt, \_size, \_proto, \_timeout) \

1870 net\_pkt\_alloc\_buffer\_debug(\_pkt, \_size, \_proto, \_timeout, \

1871 \_\_func\_\_, \_\_LINE\_\_)

1872

1873int net\_pkt\_alloc\_buffer\_raw\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

1874 [k\_timeout\_t](structk__timeout__t.md) timeout,

1875 const char \*caller, int line);

1876#define net\_pkt\_alloc\_buffer\_raw(\_pkt, \_size, \_timeout) \

1877 net\_pkt\_alloc\_buffer\_raw\_debug(\_pkt, \_size, \_timeout, \

1878 \_\_func\_\_, \_\_LINE\_\_)

1879

1880struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1881 size\_t size,

1882 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1883 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1884 [k\_timeout\_t](structk__timeout__t.md) timeout,

1885 const char \*caller,

1886 int line);

1887#define net\_pkt\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1888 \_proto, \_timeout) \

1889 net\_pkt\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1890 \_proto, \_timeout, \

1891 \_\_func\_\_, \_\_LINE\_\_)

1892

1893struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1894 size\_t size,

1895 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1896 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1897 [k\_timeout\_t](structk__timeout__t.md) timeout,

1898 const char \*caller,

1899 int line);

1900#define net\_pkt\_rx\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1901 \_proto, \_timeout) \

1902 net\_pkt\_rx\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1903 \_proto, \_timeout, \

1904 \_\_func\_\_, \_\_LINE\_\_)

1905

1906int net\_pkt\_alloc\_buffer\_with\_reserve\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1907 size\_t size,

1908 size\_t reserve,

1909 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1910 [k\_timeout\_t](structk__timeout__t.md) timeout,

1911 const char \*caller,

1912 int line);

1913#define net\_pkt\_alloc\_buffer\_with\_reserve(\_pkt, \_size, \_reserve, \_proto, \_timeout) \

1914 net\_pkt\_alloc\_buffer\_with\_reserve\_debug(\_pkt, \_size, \_reserve, \_proto, \

1915 \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1916

1917#endif /\* NET\_PKT\_DEBUG\_ENABLED \*/

1919

1920#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1931](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)([k\_timeout\_t](structk__timeout__t.md) timeout);

1932#endif

1933

1934#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1949](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_from\_slab](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1950 [k\_timeout\_t](structk__timeout__t.md) timeout);

1951#endif

1952

1953#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1964](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_alloc](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)([k\_timeout\_t](structk__timeout__t.md) timeout);

1965#endif

1966

1967#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1976](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_on\_iface](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1977 [k\_timeout\_t](structk__timeout__t.md) timeout);

1978

1980

1981/\* Same as above but specifically for RX packet \*/

1982struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1983 [k\_timeout\_t](structk__timeout__t.md) timeout);

1985

1986#endif

1987

1988#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2004](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)int [net\_pkt\_alloc\_buffer](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2005 size\_t size,

2006 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2007 [k\_timeout\_t](structk__timeout__t.md) timeout);

2008#endif

2009

2010#if !defined(NET\_PKT\_DEBUG\_ENABLED)

2028#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2029](group__net__pkt.md#ga0a292103ba0eacd62a15447e2765a485)int [net\_pkt\_alloc\_buffer\_with\_reserve](group__net__pkt.md#ga0a292103ba0eacd62a15447e2765a485)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2030 size\_t size,

2031 size\_t reserve,

2032 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2033 [k\_timeout\_t](structk__timeout__t.md) timeout);

2034#endif

2035

[ 2049](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)int [net\_pkt\_alloc\_buffer\_raw](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

2050 [k\_timeout\_t](structk__timeout__t.md) timeout);

2051#endif

2052

2053#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2065](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_with\_buffer](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2066 size\_t size,

2067 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

2068 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2069 [k\_timeout\_t](structk__timeout__t.md) timeout);

2070

2072

2073/\* Same as above but specifically for RX packet \*/

2074struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2075 size\_t size,

2076 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

2077 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2078 [k\_timeout\_t](structk__timeout__t.md) timeout);

2079

2081

2082#endif

2083

[ 2090](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)void [net\_pkt\_append\_buffer](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b));

2091

[ 2102](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)size\_t [net\_pkt\_available\_buffer](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2103

[ 2119](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)size\_t [net\_pkt\_available\_payload\_buffer](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2120 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto);

2121

[ 2130](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)void [net\_pkt\_trim\_buffer](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2131

[ 2146](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)int [net\_pkt\_remove\_tail](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2147

[ 2155](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)void [net\_pkt\_cursor\_init](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2156

[ 2163](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)static inline void [net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2164 struct net\_pkt\_cursor \*backup)

2165{

2166 backup->buf = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).buf;

2167 backup->pos = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos;

2168}

2169

[ 2176](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)static inline void [net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2177 struct net\_pkt\_cursor \*backup)

2178{

2179 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).buf = backup->buf;

2180 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos = backup->pos;

2181}

2182

[ 2190](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)static inline void \*[net\_pkt\_cursor\_get\_pos](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)(struct [net\_pkt](structnet__pkt.md) \*pkt)

2191{

2192 return pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos;

2193}

2194

[ 2215](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)int [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2216

[ 2231](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)int [net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)(struct [net\_pkt](structnet__pkt.md) \*pkt, int byte, size\_t length);

2232

[ 2246](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)int [net\_pkt\_copy](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)(struct [net\_pkt](structnet__pkt.md) \*pkt\_dst,

2247 struct [net\_pkt](structnet__pkt.md) \*pkt\_src,

2248 size\_t length);

2249

[ 2259](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_clone](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2260

[ 2270](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_clone](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2271

[ 2280](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_shallow\_clone](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2281 [k\_timeout\_t](structk__timeout__t.md) timeout);

2282

[ 2296](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)int [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(struct [net\_pkt](structnet__pkt.md) \*pkt, void \*data, size\_t length);

2297

[ 2310](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)static inline int [net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

2311{

2312 return [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(pkt, data, 1);

2313}

2314

[ 2327](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)int [net\_pkt\_read\_be16](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2328

[ 2341](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)int [net\_pkt\_read\_le16](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2342

[ 2355](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)int [net\_pkt\_read\_be32](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

2356

[ 2370](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)int [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(struct [net\_pkt](structnet__pkt.md) \*pkt, const void \*data, size\_t length);

2371

[ 2384](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)static inline int [net\_pkt\_write\_u8](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data)

2385{

2386 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data, sizeof([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)));

2387}

2388

[ 2401](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)static inline int [net\_pkt\_write\_be16](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2402{

2403 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_be16 = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(data);

2404

2405 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2406}

2407

[ 2420](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)static inline int [net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2421{

2422 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_be32 = [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(data);

2423

2424 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2425}

2426

[ 2439](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)static inline int [net\_pkt\_write\_le32](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2440{

2441 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_le32 = [sys\_cpu\_to\_le32](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)(data);

2442

2443 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2444}

2445

[ 2458](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)static inline int [net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2459{

2460 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_le16 = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)(data);

2461

2462 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2463}

2464

[ 2472](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)size\_t [net\_pkt\_remaining\_data](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2473

[ 2481](group__net__pkt.md#ga9401d109ba978087139436c8a79c9bb0)static inline size\_t [net\_pkt\_get\_len](group__net__pkt.md#ga9401d109ba978087139436c8a79c9bb0)(struct [net\_pkt](structnet__pkt.md) \*pkt)

2482{

2483 return [net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)(pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6));

2484}

2485

[ 2498](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)int [net\_pkt\_update\_length](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2499

[ 2512](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)int [net\_pkt\_pull](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2513

[ 2522](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_pkt\_get\_current\_offset](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2523

[ 2535](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)bool [net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size);

2536

[ 2545](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)size\_t [net\_pkt\_get\_contiguous\_len](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2546

2548

2549struct net\_pkt\_data\_access {

2550#if !defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2551 void \*data;

2552#endif

2553 const size\_t size;

2554};

2555

2556#if defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2557#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2558 struct net\_pkt\_data\_access \_name = { \

2559 .size = sizeof(\_type), \

2560 }

2561

2562#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2563 NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type)

2564

2565#else

2566#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2567 \_type \_hdr\_##\_name; \

2568 struct net\_pkt\_data\_access \_name = { \

2569 .data = &\_hdr\_##\_name, \

2570 .size = sizeof(\_type), \

2571 }

2572

2573#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2574 struct net\_pkt\_data\_access \_name = { \

2575 .data = NULL, \

2576 .size = sizeof(\_type), \

2577 }

2578

2579#endif /\* CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS \*/

2580

2582

[ 2596](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)void \*[net\_pkt\_get\_data](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2597 struct net\_pkt\_data\_access \*access);

2598

[ 2612](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)int [net\_pkt\_set\_data](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2613 struct net\_pkt\_data\_access \*access);

2614

[ 2619](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)static inline int [net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2620 struct net\_pkt\_data\_access \*access)

2621{

2622 return [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(pkt, access->size);

2623}

2624

2628

2629#ifdef \_\_cplusplus

2630}

2631#endif

2632

2633#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_PKT\_H\_ \*/

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

**Definition** net\_buf.h:2700

[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)

static struct net\_if \* net\_context\_get\_iface(struct net\_context \*context)

Get network interface for this context.

**Definition** net\_context.h:741

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:1125

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2109

[net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)

void net\_pkt\_frag\_add(struct net\_pkt \*pkt, struct net\_buf \*frag)

Add a fragment to a packet at the end of its fragment list.

[net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)

static int net\_pkt\_write\_be32(struct net\_pkt \*pkt, uint32\_t data)

Write a uint32\_t big endian data to a net\_pkt.

**Definition** net\_pkt.h:2420

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

**Definition** net\_pkt.h:1622

[net\_pkt\_update\_length](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)

int net\_pkt\_update\_length(struct net\_pkt \*pkt, size\_t length)

Update the overall length of a packet.

[net\_pkt\_pull](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)

int net\_pkt\_pull(struct net\_pkt \*pkt, size\_t length)

Remove data from the packet at current location.

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

**Definition** net\_pkt.h:2401

[net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)

struct net\_pkt \* net\_pkt\_alloc(k\_timeout\_t timeout)

Allocate an initialized net\_pkt.

[net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)

int net\_pkt\_read(struct net\_pkt \*pkt, void \*data, size\_t length)

Read some data from a net\_pkt.

[net\_pkt\_get\_len](group__net__pkt.md#ga9401d109ba978087139436c8a79c9bb0)

static size\_t net\_pkt\_get\_len(struct net\_pkt \*pkt)

Get the total amount of bytes stored in a packet.

**Definition** net\_pkt.h:2481

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

**Definition** net\_pkt.h:2384

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

**Definition** net\_pkt.h:2190

[net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)

void net\_pkt\_frag\_insert(struct net\_pkt \*pkt, struct net\_buf \*frag)

Insert a fragment to a packet at the beginning of its fragment list.

[net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)

int net\_pkt\_memset(struct net\_pkt \*pkt, int byte, size\_t length)

Memset some data in a net\_pkt.

[net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)

static void net\_pkt\_cursor\_backup(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Backup net\_pkt cursor.

**Definition** net\_pkt.h:2163

[net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)

void net\_pkt\_compact(struct net\_pkt \*pkt)

Compact the fragment list of a packet.

[net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)

static int net\_pkt\_acknowledge\_data(struct net\_pkt \*pkt, struct net\_pkt\_data\_access \*access)

Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrit...

**Definition** net\_pkt.h:2619

[net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)

static int net\_pkt\_write\_le16(struct net\_pkt \*pkt, uint16\_t data)

Write a uint16\_t little endian data to a net\_pkt.

**Definition** net\_pkt.h:2458

[net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)

static void net\_pkt\_cursor\_restore(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Restore net\_pkt cursor from a backup.

**Definition** net\_pkt.h:2176

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

**Definition** net\_pkt.h:2439

[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)

struct net\_buf \* net\_pkt\_get\_reserve\_rx\_data(size\_t min\_len, k\_timeout\_t timeout)

Get RX DATA buffer from pool.

[net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)

bool net\_pkt\_is\_contiguous(struct net\_pkt \*pkt, size\_t size)

Check if a data size could fit contiguously.

[net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)

static int net\_pkt\_read\_u8(struct net\_pkt \*pkt, uint8\_t \*data)

Read a byte (uint8\_t) from a net\_pkt.

**Definition** net\_pkt.h:2310

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

**Definition** common.h:129

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

**Definition** sys\_clock.h:65

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

**Definition** net\_context.h:207

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:69

[net\_linkaddr::addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)

uint8\_t \* addr

The array of byte representing the address.

**Definition** net\_linkaddr.h:71

[net\_linkaddr::type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:77

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

**Definition** net\_ip.h:408

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
