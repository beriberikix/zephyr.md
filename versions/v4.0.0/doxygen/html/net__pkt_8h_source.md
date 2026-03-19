---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__pkt_8h_source.html
original_path: doxygen/html/net__pkt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

345 /\* @endcond \*/

346};

347

349

350/\* The interface real ll address \*/

351static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_if(struct [net\_pkt](structnet__pkt.md) \*pkt)

352{

353 return [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

354}

355

356static inline struct [net\_context](structnet__context.md) \*net\_pkt\_context(struct [net\_pkt](structnet__pkt.md) \*pkt)

357{

358 return pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf);

359}

360

361static inline void net\_pkt\_set\_context(struct [net\_pkt](structnet__pkt.md) \*pkt,

362 struct [net\_context](structnet__context.md) \*ctx)

363{

364 pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf) = ctx;

365}

366

367static inline struct [net\_if](structnet__if.md) \*net\_pkt\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

368{

369 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

370}

371

372static inline void net\_pkt\_set\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_if](structnet__if.md) \*iface)

373{

374 pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) = iface;

375

376 /\* If the network interface is set in pkt, then also set the type of

377 \* the network address that is stored in pkt. This is done here so

378 \* that the address type is properly set and is not forgotten.

379 \*/

380 if (iface) {

381 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type = [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

382

383 pkt->lladdr\_src.type = type;

384 pkt->lladdr\_dst.type = type;

385 }

386}

387

388static inline struct [net\_if](structnet__if.md) \*net\_pkt\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

389{

390#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

391 return pkt->orig\_iface;

392#else

393 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

394#endif

395}

396

397static inline void net\_pkt\_set\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt,

398 struct [net\_if](structnet__if.md) \*iface)

399{

400#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

401 pkt->orig\_iface = iface;

402#else

403 ARG\_UNUSED(pkt);

404 ARG\_UNUSED(iface);

405#endif

406}

407

408static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_family(struct [net\_pkt](structnet__pkt.md) \*pkt)

409{

410 return pkt->family;

411}

412

413static inline void net\_pkt\_set\_family(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family)

414{

415 pkt->family = family;

416}

417

418static inline bool net\_pkt\_is\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt)

419{

420 return !!(pkt->ptp\_pkt);

421}

422

423static inline void net\_pkt\_set\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_ptp)

424{

425 pkt->ptp\_pkt = is\_ptp;

426}

427

428static inline bool net\_pkt\_is\_tx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt)

429{

430#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

431 return !!(pkt->tx\_timestamping);

432#else

433 ARG\_UNUSED(pkt);

434

435 return false;

436#endif

437}

438

439static inline void net\_pkt\_set\_tx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_timestamping)

440{

441#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

442 pkt->tx\_timestamping = is\_timestamping;

443#else

444 ARG\_UNUSED(pkt);

445 ARG\_UNUSED(is\_timestamping);

446#endif

447}

448

449static inline bool net\_pkt\_is\_rx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt)

450{

451#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

452 return !!(pkt->rx\_timestamping);

453#else

454 ARG\_UNUSED(pkt);

455

456 return false;

457#endif

458}

459

460static inline void net\_pkt\_set\_rx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_timestamping)

461{

462#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

463 pkt->rx\_timestamping = is\_timestamping;

464#else

465 ARG\_UNUSED(pkt);

466 ARG\_UNUSED(is\_timestamping);

467#endif

468}

469

470static inline bool net\_pkt\_is\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt)

471{

472 return !!(pkt->captured);

473}

474

475static inline void net\_pkt\_set\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_captured)

476{

477 pkt->captured = is\_captured;

478}

479

480static inline bool net\_pkt\_is\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt)

481{

482 return [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE) ? !!(pkt->l2\_bridged) : 0;

483}

484

485static inline void net\_pkt\_set\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_l2\_bridged)

486{

487 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE)) {

488 pkt->l2\_bridged = is\_l2\_bridged;

489 }

490}

491

492static inline bool net\_pkt\_is\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt)

493{

494 return !!(pkt->l2\_processed);

495}

496

497static inline void net\_pkt\_set\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt,

498 bool is\_l2\_processed)

499{

500 pkt->l2\_processed = is\_l2\_processed;

501}

502

503static inline bool net\_pkt\_is\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt)

504{

505 return !!(pkt->chksum\_done);

506}

507

508static inline void net\_pkt\_set\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt,

509 bool is\_chksum\_done)

510{

511 pkt->chksum\_done = is\_chksum\_done;

512}

513

514static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

515{

516#if defined(CONFIG\_NET\_IP)

517 return pkt->ip\_hdr\_len;

518#else

519 ARG\_UNUSED(pkt);

520

521 return 0;

522#endif

523}

524

525static inline void net\_pkt\_set\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

526{

527#if defined(CONFIG\_NET\_IP)

528 pkt->ip\_hdr\_len = len;

529#else

530 ARG\_UNUSED(pkt);

531 ARG\_UNUSED(len);

532#endif

533}

534

535static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt)

536{

537#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

538 return pkt->ip\_dscp;

539#else

540 ARG\_UNUSED(pkt);

541

542 return 0;

543#endif

544}

545

546static inline void net\_pkt\_set\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dscp)

547{

548#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

549 pkt->ip\_dscp = dscp;

550#else

551 ARG\_UNUSED(pkt);

552 ARG\_UNUSED(dscp);

553#endif

554}

555

556static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt)

557{

558#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

559 return pkt->ip\_ecn;

560#else

561 ARG\_UNUSED(pkt);

562

563 return 0;

564#endif

565}

566

567static inline void net\_pkt\_set\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ecn)

568{

569#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

570 pkt->ip\_ecn = ecn;

571#else

572 ARG\_UNUSED(pkt);

573 ARG\_UNUSED(ecn);

574#endif

575}

576

577static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt)

578{

579 return pkt->eof;

580}

581

582static inline void net\_pkt\_set\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt, bool eof)

583{

584 pkt->eof = eof;

585}

586

587static inline bool net\_pkt\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt)

588{

589 return !!(pkt->forwarding);

590}

591

592static inline void net\_pkt\_set\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt, bool forward)

593{

594 pkt->forwarding = forward;

595}

596

597#if defined(CONFIG\_NET\_IPV4)

598static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

599{

600 return pkt->ipv4\_ttl;

601}

602

603static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

604 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

605{

606 pkt->ipv4\_ttl = ttl;

607}

608

609static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

610{

611 return pkt->ipv4\_opts\_len;

612}

613

614static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

615 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

616{

617 pkt->ipv4\_opts\_len = opts\_len;

618}

619#else

620static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

621{

622 ARG\_UNUSED(pkt);

623

624 return 0;

625}

626

627static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

628 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

629{

630 ARG\_UNUSED(pkt);

631 ARG\_UNUSED(ttl);

632}

633

634static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

635{

636 ARG\_UNUSED(pkt);

637 return 0;

638}

639

640static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

641 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

642{

643 ARG\_UNUSED(pkt);

644 ARG\_UNUSED(opts\_len);

645}

646#endif

647

648#if defined(CONFIG\_NET\_IPV6)

649static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

650{

651 return pkt->ipv6\_ext\_opt\_len;

652}

653

654static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

655 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

656{

657 pkt->ipv6\_ext\_opt\_len = len;

658}

659

660static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

661{

662 return pkt->ipv6\_next\_hdr;

663}

664

665static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

666 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

667{

668 pkt->ipv6\_next\_hdr = next\_hdr;

669}

670

671static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

672{

673 return pkt->ipv6\_ext\_len;

674}

675

676static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

677{

678 pkt->ipv6\_ext\_len = len;

679}

680

681static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

682{

683 return pkt->ipv6\_prev\_hdr\_start;

684}

685

686static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

687 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

688{

689 pkt->ipv6\_prev\_hdr\_start = offset;

690}

691

692static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

693{

694 return pkt->ipv6\_hop\_limit;

695}

696

697static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

698 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

699{

700 pkt->ipv6\_hop\_limit = hop\_limit;

701}

702#else /\* CONFIG\_NET\_IPV6 \*/

703static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

704{

705 ARG\_UNUSED(pkt);

706

707 return 0;

708}

709

710static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

711 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

712{

713 ARG\_UNUSED(pkt);

714 ARG\_UNUSED(len);

715}

716

717static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

718{

719 ARG\_UNUSED(pkt);

720

721 return 0;

722}

723

724static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

725 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

726{

727 ARG\_UNUSED(pkt);

728 ARG\_UNUSED(next\_hdr);

729}

730

731static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

732{

733 ARG\_UNUSED(pkt);

734

735 return 0;

736}

737

738static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

739{

740 ARG\_UNUSED(pkt);

741 ARG\_UNUSED(len);

742}

743

744static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

745{

746 ARG\_UNUSED(pkt);

747

748 return 0;

749}

750

751static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

752 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

753{

754 ARG\_UNUSED(pkt);

755 ARG\_UNUSED(offset);

756}

757

758static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

759{

760 ARG\_UNUSED(pkt);

761

762 return 0;

763}

764

765static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

766 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

767{

768 ARG\_UNUSED(pkt);

769 ARG\_UNUSED(hop\_limit);

770}

771#endif /\* CONFIG\_NET\_IPV6 \*/

772

773static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ip\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

774{

775#if defined(CONFIG\_NET\_IPV6)

776 return pkt->ipv6\_ext\_len;

777#elif defined(CONFIG\_NET\_IPV4)

778 return pkt->ipv4\_opts\_len;

779#else

780 ARG\_UNUSED(pkt);

781

782 return 0;

783#endif

784}

785

786#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

787static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

788{

789 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_FRAGH\_OFFSET\_MASK) \* 8;

790}

791

792static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

793{

794 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_MORE\_FRAG\_MASK) != 0;

795}

796

797static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

798{

799 pkt->ipv4\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

800}

801

802static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

803{

804 return pkt->ipv4\_fragment.id;

805}

806

807static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

808{

809 pkt->ipv4\_fragment.id = id;

810}

811#else /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

812static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

813{

814 ARG\_UNUSED(pkt);

815

816 return 0;

817}

818

819static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

820{

821 ARG\_UNUSED(pkt);

822

823 return 0;

824}

825

826static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

827{

828 ARG\_UNUSED(pkt);

829 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

830}

831

832static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

833{

834 ARG\_UNUSED(pkt);

835

836 return 0;

837}

838

839static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

840{

841 ARG\_UNUSED(pkt);

842 ARG\_UNUSED(id);

843}

844#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

845

846#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

847static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

848{

849 return pkt->ipv6\_fragment.hdr\_start;

850}

851

852static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

853 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

854{

855 pkt->ipv6\_fragment.hdr\_start = start;

856}

857

858static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

859{

860 return pkt->ipv6\_fragment.flags & NET\_IPV6\_FRAGH\_OFFSET\_MASK;

861}

862static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

863{

864 return (pkt->ipv6\_fragment.flags & 0x01) != 0;

865}

866

867static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

868 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

869{

870 pkt->ipv6\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

871}

872

873static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

874{

875 return pkt->ipv6\_fragment.id;

876}

877

878static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

879 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

880{

881 pkt->ipv6\_fragment.id = id;

882}

883#else /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

884static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

885{

886 ARG\_UNUSED(pkt);

887

888 return 0;

889}

890

891static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

892 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

893{

894 ARG\_UNUSED(pkt);

895 ARG\_UNUSED(start);

896}

897

898static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

899{

900 ARG\_UNUSED(pkt);

901

902 return 0;

903}

904

905static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

906{

907 ARG\_UNUSED(pkt);

908

909 return 0;

910}

911

912static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

913 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

914{

915 ARG\_UNUSED(pkt);

916 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

917}

918

919static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

920{

921 ARG\_UNUSED(pkt);

922

923 return 0;

924}

925

926static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

927 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

928{

929 ARG\_UNUSED(pkt);

930 ARG\_UNUSED(id);

931}

932#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

933

934#if defined(CONFIG\_NET\_IP\_FRAGMENT)

935static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

936{

937 return !!(pkt->ip\_reassembled);

938}

939

940static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

941 bool reassembled)

942{

943 pkt->ip\_reassembled = reassembled;

944}

945#else /\* CONFIG\_NET\_IP\_FRAGMENT \*/

946static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

947{

948 ARG\_UNUSED(pkt);

949

950 return false;

951}

952

953static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

954 bool reassembled)

955{

956 ARG\_UNUSED(pkt);

957 ARG\_UNUSED(reassembled);

958}

959#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

960

961static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

962{

963 return pkt->priority;

964}

965

966static inline void net\_pkt\_set\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

967 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

968{

969 pkt->priority = priority;

970}

971

972#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

973static inline bool net\_pkt\_is\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt)

974{

975 return pkt->cooked\_mode\_pkt;

976}

977

978static inline void net\_pkt\_set\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

979{

980 pkt->cooked\_mode\_pkt = value;

981}

982#else

983static inline bool net\_pkt\_is\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt)

984{

985 ARG\_UNUSED(pkt);

986

987 return false;

988}

989

990static inline void net\_pkt\_set\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

991{

992 ARG\_UNUSED(pkt);

993 ARG\_UNUSED(value);

994}

995#endif /\* CONFIG\_NET\_CAPTURE\_COOKED\_MODE \*/

996

997#if defined(CONFIG\_NET\_VLAN)

998static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

999{

1000 return [net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)(pkt->vlan\_tci);

1001}

1002

1003static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

1004{

1005 pkt->vlan\_tci = [net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)(pkt->vlan\_tci, tag);

1006}

1007

1008static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

1009{

1010 return [net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)(pkt->vlan\_tci);

1011}

1012

1013static inline void net\_pkt\_set\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

1014 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

1015{

1016 pkt->vlan\_tci = [net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)(pkt->vlan\_tci, priority);

1017}

1018

1019static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

1020{

1021 return [net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)(pkt->vlan\_tci);

1022}

1023

1024static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

1025{

1026 pkt->vlan\_tci = [net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)(pkt->vlan\_tci, dei);

1027}

1028

1029static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

1030{

1031 pkt->vlan\_tci = tci;

1032}

1033

1034static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

1035{

1036 return pkt->vlan\_tci;

1037}

1038#else

1039static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

1040{

1041 ARG\_UNUSED(pkt);

1042

1043 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70);

1044}

1045

1046static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

1047{

1048 ARG\_UNUSED(pkt);

1049 ARG\_UNUSED(tag);

1050}

1051

1052static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

1053{

1054 ARG\_UNUSED(pkt);

1055

1056 return 0;

1057}

1058

1059static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

1060{

1061 ARG\_UNUSED(pkt);

1062

1063 return false;

1064}

1065

1066static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

1067{

1068 ARG\_UNUSED(pkt);

1069 ARG\_UNUSED(dei);

1070}

1071

1072static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

1073{

1074 ARG\_UNUSED(pkt);

1075

1076 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70); /\* assumes priority is 0 \*/

1077}

1078

1079static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

1080{

1081 ARG\_UNUSED(pkt);

1082 ARG\_UNUSED(tci);

1083}

1084#endif

1085

1086#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

1087static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1088{

1089 return &pkt->timestamp;

1090}

1091

1092static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1093 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1094{

1095 pkt->timestamp.second = timestamp->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04);

1096 pkt->timestamp.nanosecond = timestamp->[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

1097}

1098

1099static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1100{

1101 return [net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)(&pkt->timestamp);

1102}

1103

1104static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1105{

1106 pkt->timestamp = [ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)(timestamp);

1107}

1108#else

1109static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1110{

1111 ARG\_UNUSED(pkt);

1112

1113 return NULL;

1114}

1115

1116static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1117 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1118{

1119 ARG\_UNUSED(pkt);

1120 ARG\_UNUSED(timestamp);

1121}

1122

1123static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1124{

1125 ARG\_UNUSED(pkt);

1126

1127 return 0;

1128}

1129

1130static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1131{

1132 ARG\_UNUSED(pkt);

1133 ARG\_UNUSED(timestamp);

1134}

1135#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP || CONFIG\_NET\_PKT\_TXTIME \*/

1136

1137#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS) || \

1138 defined(CONFIG\_TRACING\_NET\_CORE)

1139

1140static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1141{

1142 return pkt->create\_time;

1143}

1144

1145static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1146 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1147{

1148 pkt->create\_time = create\_time;

1149}

1150#else

1151static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1152{

1153 ARG\_UNUSED(pkt);

1154

1155 return 0U;

1156}

1157

1158static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1159 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1160{

1161 ARG\_UNUSED(pkt);

1162 ARG\_UNUSED(create\_time);

1163}

1164#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS ||

1165 \* CONFIG\_TRACING\_NET\_CORE

1166 \*/

1167

1168#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

1169 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

1170static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1171{

1172 return pkt->detail.stat;

1173}

1174

1175static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1176{

1177 return pkt->detail.count;

1178}

1179

1180static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1181{

1182 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&pkt->detail, 0, sizeof(pkt->detail));

1183}

1184

1185static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt,

1186 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1187{

1188 if (pkt->detail.count >= NET\_PKT\_DETAIL\_STATS\_COUNT) {

1189 NET\_ERR("Detail stats count overflow (%d >= %d)",

1190 pkt->detail.count, NET\_PKT\_DETAIL\_STATS\_COUNT);

1191 return;

1192 }

1193

1194 pkt->detail.stat[pkt->detail.count++] = tick;

1195}

1196

1197#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1198#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1199#else

1200static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1201{

1202 ARG\_UNUSED(pkt);

1203

1204 return NULL;

1205}

1206

1207static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1208{

1209 ARG\_UNUSED(pkt);

1210

1211 return 0;

1212}

1213

1214static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1215{

1216 ARG\_UNUSED(pkt);

1217}

1218

1219static inline void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1220{

1221 ARG\_UNUSED(pkt);

1222 ARG\_UNUSED(tick);

1223}

1224

1225#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick)

1226#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick)

1227#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

1228 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

1229

1230static inline size\_t net\_pkt\_get\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

1231{

1232 return [net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)(pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6));

1233}

1234

1235static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1236{

1237 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1238}

1239

1240static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_ip\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1241{

1242 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1243}

1244

1245static inline bool net\_pkt\_is\_empty(struct [net\_pkt](structnet__pkt.md) \*pkt)

1246{

1247 return !pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b) || !net\_pkt\_data(pkt) || pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b)->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38) == 0;

1248}

1249

1250static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_src(struct [net\_pkt](structnet__pkt.md) \*pkt)

1251{

1252 return &pkt->lladdr\_src;

1253}

1254

1255static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_dst(struct [net\_pkt](structnet__pkt.md) \*pkt)

1256{

1257 return &pkt->lladdr\_dst;

1258}

1259

1260static inline void net\_pkt\_lladdr\_swap(struct [net\_pkt](structnet__pkt.md) \*pkt)

1261{

1262 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) = net\_pkt\_lladdr\_src(pkt)->addr;

1263

1264 net\_pkt\_lladdr\_src(pkt)->addr = net\_pkt\_lladdr\_dst(pkt)->addr;

1265 net\_pkt\_lladdr\_dst(pkt)->addr = [addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0);

1266}

1267

1268static inline void net\_pkt\_lladdr\_clear(struct [net\_pkt](structnet__pkt.md) \*pkt)

1269{

1270 net\_pkt\_lladdr\_src(pkt)->addr = NULL;

1271 net\_pkt\_lladdr\_src(pkt)->len = 0U;

1272}

1273

1274static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt)

1275{

1276 return pkt->ll\_proto\_type;

1277}

1278

1279static inline void net\_pkt\_set\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7))

1280{

1281 pkt->ll\_proto\_type = [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

1282}

1283

1284#if defined(CONFIG\_NET\_IPV4\_ACD)

1285static inline bool net\_pkt\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt)

1286{

1287 return !!(pkt->ipv4\_acd\_arp\_msg);

1288}

1289

1290static inline void net\_pkt\_set\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt,

1291 bool is\_acd\_arp\_msg)

1292{

1293 pkt->ipv4\_acd\_arp\_msg = is\_acd\_arp\_msg;

1294}

1295#else /\* CONFIG\_NET\_IPV4\_ACD \*/

1296static inline bool net\_pkt\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt)

1297{

1298 ARG\_UNUSED(pkt);

1299

1300 return false;

1301}

1302

1303static inline void net\_pkt\_set\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt,

1304 bool is\_acd\_arp\_msg)

1305{

1306 ARG\_UNUSED(pkt);

1307 ARG\_UNUSED(is\_acd\_arp\_msg);

1308}

1309#endif /\* CONFIG\_NET\_IPV4\_ACD \*/

1310

1311#if defined(CONFIG\_NET\_LLDP)

1312static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1313{

1314 return !!(pkt->lldp\_pkt);

1315}

1316

1317static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1318{

1319 pkt->lldp\_pkt = is\_lldp;

1320}

1321#else

1322static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1323{

1324 ARG\_UNUSED(pkt);

1325

1326 return false;

1327}

1328

1329static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1330{

1331 ARG\_UNUSED(pkt);

1332 ARG\_UNUSED(is\_lldp);

1333}

1334#endif /\* CONFIG\_NET\_LLDP \*/

1335

1336#if defined(CONFIG\_NET\_L2\_PPP)

1337static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1338{

1339 return !!(pkt->ppp\_msg);

1340}

1341

1342static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1343 bool is\_ppp\_msg)

1344{

1345 pkt->ppp\_msg = is\_ppp\_msg;

1346}

1347#else /\* CONFIG\_NET\_L2\_PPP \*/

1348static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1349{

1350 ARG\_UNUSED(pkt);

1351

1352 return false;

1353}

1354

1355static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1356 bool is\_ppp\_msg)

1357{

1358 ARG\_UNUSED(pkt);

1359 ARG\_UNUSED(is\_ppp\_msg);

1360}

1361#endif /\* CONFIG\_NET\_L2\_PPP \*/

1362

1363#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

1364static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1365{

1366 return &pkt->cb;

1367}

1368#else

1369static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1370{

1371 ARG\_UNUSED(pkt);

1372

1373 return NULL;

1374}

1375#endif

1376

1377#define NET\_IPV6\_HDR(pkt) ((struct net\_ipv6\_hdr \*)net\_pkt\_ip\_data(pkt))

1378#define NET\_IPV4\_HDR(pkt) ((struct net\_ipv4\_hdr \*)net\_pkt\_ip\_data(pkt))

1379

1380static inline void net\_pkt\_set\_src\_ipv6\_addr(struct [net\_pkt](structnet__pkt.md) \*pkt)

1381{

1382 [net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)([net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)(

1383 net\_pkt\_context(pkt)),

1384 (struct [in6\_addr](structin6__addr.md) \*)NET\_IPV6\_HDR(pkt)->src);

1385}

1386

1387static inline void net\_pkt\_set\_overwrite(struct [net\_pkt](structnet__pkt.md) \*pkt, bool overwrite)

1388{

1389 pkt->overwrite = overwrite;

1390}

1391

1392static inline bool net\_pkt\_is\_being\_overwritten(struct [net\_pkt](structnet__pkt.md) \*pkt)

1393{

1394 return !!(pkt->overwrite);

1395}

1396

1397#ifdef CONFIG\_NET\_PKT\_FILTER

1398

1399bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1400bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1401

1402#else

1403

1404static inline bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1405{

1406 ARG\_UNUSED(pkt);

1407

1408 return true;

1409}

1410

1411static inline bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1412{

1413 ARG\_UNUSED(pkt);

1414

1415 return true;

1416}

1417

1418#endif /\* CONFIG\_NET\_PKT\_FILTER \*/

1419

1420#if defined(CONFIG\_NET\_PKT\_FILTER) && \

1421 (defined(CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK) || defined(CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK))

1422

1423bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1424

1425#else

1426

1427static inline bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1428{

1429 ARG\_UNUSED(pkt);

1430

1431 return true;

1432}

1433

1434#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK || CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK \*/

1435

1436#if defined(CONFIG\_NET\_PKT\_FILTER) && defined(CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK)

1437

1438bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1439

1440#else

1441

1442static inline bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1443{

1444 ARG\_UNUSED(pkt);

1445

1446 return true;

1447}

1448

1449#endif /\* CONFIG\_NET\_PKT\_FILTER && CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK \*/

1450

1451#if defined(CONFIG\_NET\_OFFLOAD) || defined(CONFIG\_NET\_L2\_IPIP)

1452static inline struct [sockaddr](structsockaddr.md) \*net\_pkt\_remote\_address(struct [net\_pkt](structnet__pkt.md) \*pkt)

1453{

1454 return &pkt->remote;

1455}

1456

1457static inline void net\_pkt\_set\_remote\_address(struct [net\_pkt](structnet__pkt.md) \*pkt,

1458 struct [sockaddr](structsockaddr.md) \*address,

1459 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) len)

1460{

1461 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&pkt->remote, address, len);

1462}

1463#endif /\* CONFIG\_NET\_OFFLOAD || CONFIG\_NET\_L2\_IPIP \*/

1464

1465/\* @endcond \*/

1466

[ 1480](group__net__pkt.md#gafc7e98d5b64d816faabcbaa2ec22a2bb)#define NET\_PKT\_SLAB\_DEFINE(name, count) \

1481 K\_MEM\_SLAB\_DEFINE(name, sizeof(struct net\_pkt), count, 4); \

1482 NET\_PKT\_ALLOC\_STATS\_DEFINE(pkt\_alloc\_stats\_##name, name)

1483

1485

1486/\* Backward compatibility macro \*/

1487#define NET\_PKT\_TX\_SLAB\_DEFINE(name, count) NET\_PKT\_SLAB\_DEFINE(name, count)

1488

1490

[ 1504](group__net__pkt.md#ga94ab6300b59d739c4e3c5604d3fbe8a5)#define NET\_PKT\_DATA\_POOL\_DEFINE(name, count) \

1505 NET\_BUF\_POOL\_DEFINE(name, count, CONFIG\_NET\_BUF\_DATA\_SIZE, \

1506 0, NULL)

1507

1509

1510#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC) || \

1511 (CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG)

1512#define NET\_PKT\_DEBUG\_ENABLED

1513#endif

1514

1515#if defined(NET\_PKT\_DEBUG\_ENABLED)

1516

1517/\* Debug versions of the net\_pkt functions that are used when tracking

1518 \* buffer usage.

1519 \*/

1520

1521struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_data\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1522 size\_t min\_len,

1523 [k\_timeout\_t](structk__timeout__t.md) timeout,

1524 const char \*caller,

1525 int line);

1526

1527#define net\_pkt\_get\_reserve\_data(pool, min\_len, timeout) \

1528 net\_pkt\_get\_reserve\_data\_debug(pool, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1529

1530struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_rx\_data\_debug(size\_t min\_len,

1531 [k\_timeout\_t](structk__timeout__t.md) timeout,

1532 const char \*caller,

1533 int line);

1534#define net\_pkt\_get\_reserve\_rx\_data(min\_len, timeout) \

1535 net\_pkt\_get\_reserve\_rx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1536

1537struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_tx\_data\_debug(size\_t min\_len,

1538 [k\_timeout\_t](structk__timeout__t.md) timeout,

1539 const char \*caller,

1540 int line);

1541#define net\_pkt\_get\_reserve\_tx\_data(min\_len, timeout) \

1542 net\_pkt\_get\_reserve\_tx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1543

1544struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_frag\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1545 [k\_timeout\_t](structk__timeout__t.md) timeout,

1546 const char \*caller, int line);

1547#define net\_pkt\_get\_frag(pkt, min\_len, timeout) \

1548 net\_pkt\_get\_frag\_debug(pkt, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1549

1550void net\_pkt\_unref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller, int line);

1551#define net\_pkt\_unref(pkt) net\_pkt\_unref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1552

1553struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_ref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller,

1554 int line);

1555#define net\_pkt\_ref(pkt) net\_pkt\_ref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1556

1557struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_ref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1558 const char \*caller, int line);

1559#define net\_pkt\_frag\_ref(frag) net\_pkt\_frag\_ref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1560

1561void net\_pkt\_frag\_unref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1562 const char \*caller, int line);

1563#define net\_pkt\_frag\_unref(frag) \

1564 net\_pkt\_frag\_unref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1565

1566struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_del\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1567 struct [net\_buf](structnet__buf.md) \*parent,

1568 struct [net\_buf](structnet__buf.md) \*frag,

1569 const char \*caller, int line);

1570#define net\_pkt\_frag\_del(pkt, parent, frag) \

1571 net\_pkt\_frag\_del\_debug(pkt, parent, frag, \_\_func\_\_, \_\_LINE\_\_)

1572

1573void net\_pkt\_frag\_add\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1574 const char \*caller, int line);

1575#define net\_pkt\_frag\_add(pkt, frag) \

1576 net\_pkt\_frag\_add\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1577

1578void net\_pkt\_frag\_insert\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1579 const char \*caller, int line);

1580#define net\_pkt\_frag\_insert(pkt, frag) \

1581 net\_pkt\_frag\_insert\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1582#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC ||

1583 \* CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

1584 \*/

1586

1587#if defined(NET\_PKT\_DEBUG\_ENABLED)

1595void [net\_pkt\_print\_frags](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1596#else

[ 1597](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)#define net\_pkt\_print\_frags(pkt)

1598#endif

1599

1600#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1615](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_data](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1616 size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1617#endif

1618

1619#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1634](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1635#endif

1636

1637#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1652](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_tx\_data](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1653#endif

1654

1655#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1668](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_frag](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1669 [k\_timeout\_t](structk__timeout__t.md) timeout);

1670#endif

1671

1672#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1682](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)void [net\_pkt\_unref](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1683#endif

1684

1685#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1695](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_ref](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1696#endif

1697

1698#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1708](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_ref](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)(struct [net\_buf](structnet__buf.md) \*frag);

1709#endif

1710

1711#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1717](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)void [net\_pkt\_frag\_unref](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)(struct [net\_buf](structnet__buf.md) \*frag);

1718#endif

1719

1720#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1731](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_del](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1732 struct [net\_buf](structnet__buf.md) \*parent,

1733 struct [net\_buf](structnet__buf.md) \*frag);

1734#endif

1735

1736#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1743](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)void [net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1744#endif

1745

1746#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1753](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)void [net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1754#endif

1755

[ 1762](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)void [net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1763

[ 1772](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)void [net\_pkt\_get\_info](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)(struct k\_mem\_slab \*\*rx,

1773 struct k\_mem\_slab \*\*tx,

1774 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*rx\_data,

1775 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*tx\_data);

1776

1778

1779#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC)

1783void net\_pkt\_print(void);

1784

1785typedef void (\*net\_pkt\_allocs\_cb\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1786 struct [net\_buf](structnet__buf.md) \*buf,

1787 const char \*func\_alloc,

1788 int line\_alloc,

1789 const char \*func\_free,

1790 int line\_free,

1791 bool in\_use,

1792 void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1793

1794void net\_pkt\_allocs\_foreach(net\_pkt\_allocs\_cb\_t cb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1795

1796const char \*net\_pkt\_slab2str(struct k\_mem\_slab \*slab);

1797const char \*net\_pkt\_pool2str(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool);

1798

1799#else

1800#define net\_pkt\_print(...)

1801#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC \*/

1802

1803/\* New allocator, and API are defined below.

1804 \* This will be simpler when time will come to get rid of former API above.

1805 \*/

1806#if defined(NET\_PKT\_DEBUG\_ENABLED)

1807

1808struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1809 const char \*caller, int line);

1810#define net\_pkt\_alloc(\_timeout) \

1811 net\_pkt\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1812

1813struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_from\_slab\_debug(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1814 [k\_timeout\_t](structk__timeout__t.md) timeout,

1815 const char \*caller, int line);

1816#define net\_pkt\_alloc\_from\_slab(\_slab, \_timeout) \

1817 net\_pkt\_alloc\_from\_slab\_debug(\_slab, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1818

1819struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1820 const char \*caller, int line);

1821#define net\_pkt\_rx\_alloc(\_timeout) \

1822 net\_pkt\_rx\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1823

1824struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1825 [k\_timeout\_t](structk__timeout__t.md) timeout,

1826 const char \*caller,

1827 int line);

1828#define net\_pkt\_alloc\_on\_iface(\_iface, \_timeout) \

1829 net\_pkt\_alloc\_on\_iface\_debug(\_iface, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1830

1831struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1832 [k\_timeout\_t](structk__timeout__t.md) timeout,

1833 const char \*caller,

1834 int line);

1835#define net\_pkt\_rx\_alloc\_on\_iface(\_iface, \_timeout) \

1836 net\_pkt\_rx\_alloc\_on\_iface\_debug(\_iface, \_timeout, \

1837 \_\_func\_\_, \_\_LINE\_\_)

1838

1839int net\_pkt\_alloc\_buffer\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1840 size\_t size,

1841 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1842 [k\_timeout\_t](structk__timeout__t.md) timeout,

1843 const char \*caller, int line);

1844#define net\_pkt\_alloc\_buffer(\_pkt, \_size, \_proto, \_timeout) \

1845 net\_pkt\_alloc\_buffer\_debug(\_pkt, \_size, \_proto, \_timeout, \

1846 \_\_func\_\_, \_\_LINE\_\_)

1847

1848int net\_pkt\_alloc\_buffer\_raw\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

1849 [k\_timeout\_t](structk__timeout__t.md) timeout,

1850 const char \*caller, int line);

1851#define net\_pkt\_alloc\_buffer\_raw(\_pkt, \_size, \_timeout) \

1852 net\_pkt\_alloc\_buffer\_raw\_debug(\_pkt, \_size, \_timeout, \

1853 \_\_func\_\_, \_\_LINE\_\_)

1854

1855struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1856 size\_t size,

1857 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1858 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1859 [k\_timeout\_t](structk__timeout__t.md) timeout,

1860 const char \*caller,

1861 int line);

1862#define net\_pkt\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1863 \_proto, \_timeout) \

1864 net\_pkt\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1865 \_proto, \_timeout, \

1866 \_\_func\_\_, \_\_LINE\_\_)

1867

1868struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1869 size\_t size,

1870 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1871 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1872 [k\_timeout\_t](structk__timeout__t.md) timeout,

1873 const char \*caller,

1874 int line);

1875#define net\_pkt\_rx\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1876 \_proto, \_timeout) \

1877 net\_pkt\_rx\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1878 \_proto, \_timeout, \

1879 \_\_func\_\_, \_\_LINE\_\_)

1880#endif /\* NET\_PKT\_DEBUG\_ENABLED \*/

1882

1883#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1894](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)([k\_timeout\_t](structk__timeout__t.md) timeout);

1895#endif

1896

1897#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1912](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_from\_slab](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1913 [k\_timeout\_t](structk__timeout__t.md) timeout);

1914#endif

1915

1916#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1927](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_alloc](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)([k\_timeout\_t](structk__timeout__t.md) timeout);

1928#endif

1929

1930#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1939](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_on\_iface](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1940 [k\_timeout\_t](structk__timeout__t.md) timeout);

1941

1943

1944/\* Same as above but specifically for RX packet \*/

1945struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1946 [k\_timeout\_t](structk__timeout__t.md) timeout);

1948

1949#endif

1950

1951#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1967](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)int [net\_pkt\_alloc\_buffer](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1968 size\_t size,

1969 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1970 [k\_timeout\_t](structk__timeout__t.md) timeout);

1971#endif

1972

1973#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1987](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)int [net\_pkt\_alloc\_buffer\_raw](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

1988 [k\_timeout\_t](structk__timeout__t.md) timeout);

1989#endif

1990

1991#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 2003](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_with\_buffer](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2004 size\_t size,

2005 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

2006 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2007 [k\_timeout\_t](structk__timeout__t.md) timeout);

2008

2010

2011/\* Same as above but specifically for RX packet \*/

2012struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2013 size\_t size,

2014 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

2015 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2016 [k\_timeout\_t](structk__timeout__t.md) timeout);

2017

2019

2020#endif

2021

[ 2028](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)void [net\_pkt\_append\_buffer](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b));

2029

[ 2040](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)size\_t [net\_pkt\_available\_buffer](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2041

[ 2057](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)size\_t [net\_pkt\_available\_payload\_buffer](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2058 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto);

2059

[ 2068](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)void [net\_pkt\_trim\_buffer](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2069

[ 2084](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)int [net\_pkt\_remove\_tail](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2085

[ 2093](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)void [net\_pkt\_cursor\_init](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2094

[ 2101](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)static inline void [net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2102 struct net\_pkt\_cursor \*backup)

2103{

2104 backup->buf = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).buf;

2105 backup->pos = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos;

2106}

2107

[ 2114](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)static inline void [net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2115 struct net\_pkt\_cursor \*backup)

2116{

2117 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).buf = backup->buf;

2118 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos = backup->pos;

2119}

2120

[ 2128](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)static inline void \*[net\_pkt\_cursor\_get\_pos](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)(struct [net\_pkt](structnet__pkt.md) \*pkt)

2129{

2130 return pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos;

2131}

2132

[ 2153](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)int [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2154

[ 2169](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)int [net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)(struct [net\_pkt](structnet__pkt.md) \*pkt, int byte, size\_t length);

2170

[ 2184](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)int [net\_pkt\_copy](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)(struct [net\_pkt](structnet__pkt.md) \*pkt\_dst,

2185 struct [net\_pkt](structnet__pkt.md) \*pkt\_src,

2186 size\_t length);

2187

[ 2197](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_clone](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2198

[ 2208](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_clone](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2209

[ 2218](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_shallow\_clone](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2219 [k\_timeout\_t](structk__timeout__t.md) timeout);

2220

[ 2234](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)int [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(struct [net\_pkt](structnet__pkt.md) \*pkt, void \*data, size\_t length);

2235

[ 2248](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)static inline int [net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

2249{

2250 return [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(pkt, data, 1);

2251}

2252

[ 2265](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)int [net\_pkt\_read\_be16](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2266

[ 2279](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)int [net\_pkt\_read\_le16](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2280

[ 2293](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)int [net\_pkt\_read\_be32](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

2294

[ 2308](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)int [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(struct [net\_pkt](structnet__pkt.md) \*pkt, const void \*data, size\_t length);

2309

[ 2322](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)static inline int [net\_pkt\_write\_u8](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data)

2323{

2324 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data, sizeof([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)));

2325}

2326

[ 2339](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)static inline int [net\_pkt\_write\_be16](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2340{

2341 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_be16 = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(data);

2342

2343 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2344}

2345

[ 2358](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)static inline int [net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2359{

2360 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_be32 = [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(data);

2361

2362 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2363}

2364

[ 2377](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)static inline int [net\_pkt\_write\_le32](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2378{

2379 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_le32 = [sys\_cpu\_to\_le32](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)(data);

2380

2381 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2382}

2383

[ 2396](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)static inline int [net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2397{

2398 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_le16 = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)(data);

2399

2400 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2401}

2402

[ 2410](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)size\_t [net\_pkt\_remaining\_data](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2411

[ 2424](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)int [net\_pkt\_update\_length](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2425

[ 2438](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)int [net\_pkt\_pull](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2439

[ 2448](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_pkt\_get\_current\_offset](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2449

[ 2461](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)bool [net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size);

2462

[ 2471](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)size\_t [net\_pkt\_get\_contiguous\_len](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2472

2474

2475struct net\_pkt\_data\_access {

2476#if !defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2477 void \*data;

2478#endif

2479 const size\_t size;

2480};

2481

2482#if defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2483#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2484 struct net\_pkt\_data\_access \_name = { \

2485 .size = sizeof(\_type), \

2486 }

2487

2488#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2489 NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type)

2490

2491#else

2492#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2493 \_type \_hdr\_##\_name; \

2494 struct net\_pkt\_data\_access \_name = { \

2495 .data = &\_hdr\_##\_name, \

2496 .size = sizeof(\_type), \

2497 }

2498

2499#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2500 struct net\_pkt\_data\_access \_name = { \

2501 .data = NULL, \

2502 .size = sizeof(\_type), \

2503 }

2504

2505#endif /\* CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS \*/

2506

2508

[ 2522](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)void \*[net\_pkt\_get\_data](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2523 struct net\_pkt\_data\_access \*access);

2524

[ 2538](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)int [net\_pkt\_set\_data](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2539 struct net\_pkt\_data\_access \*access);

2540

[ 2545](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)static inline int [net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2546 struct net\_pkt\_data\_access \*access)

2547{

2548 return [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(pkt, access->size);

2549}

2550

2554

2555#ifdef \_\_cplusplus

2556}

2557#endif

2558

2559#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_PKT\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[ethernet\_vlan.h](ethernet__vlan_8h.md)

VLAN specific definitions.

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:167

[htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)

#define htons(x)

Convert 16-bit value from host to network byte order.

**Definition** net\_ip.h:123

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:171

[htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)

#define htonl(x)

Convert 32-bit value from host to network byte order.

**Definition** net\_ip.h:131

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:64

[net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)

static size\_t net\_buf\_frags\_len(const struct net\_buf \*buf)

Calculate amount of bytes stored in fragments.

**Definition** net\_buf.h:2711

[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)

static struct net\_if \* net\_context\_get\_iface(struct net\_context \*context)

Get network interface for this context.

**Definition** net\_context.h:711

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:1078

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2045

[net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)

void net\_pkt\_frag\_add(struct net\_pkt \*pkt, struct net\_buf \*frag)

Add a fragment to a packet at the end of its fragment list.

[net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)

static int net\_pkt\_write\_be32(struct net\_pkt \*pkt, uint32\_t data)

Write a uint32\_t big endian data to a net\_pkt.

**Definition** net\_pkt.h:2358

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

**Definition** net\_pkt.h:1597

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

**Definition** net\_pkt.h:2339

[net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)

struct net\_pkt \* net\_pkt\_alloc(k\_timeout\_t timeout)

Allocate an initialized net\_pkt.

[net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)

int net\_pkt\_read(struct net\_pkt \*pkt, void \*data, size\_t length)

Read some data from a net\_pkt.

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

**Definition** net\_pkt.h:2322

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

**Definition** net\_pkt.h:2128

[net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)

void net\_pkt\_frag\_insert(struct net\_pkt \*pkt, struct net\_buf \*frag)

Insert a fragment to a packet at the beginning of its fragment list.

[net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)

int net\_pkt\_memset(struct net\_pkt \*pkt, int byte, size\_t length)

Memset some data in a net\_pkt.

[net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)

static void net\_pkt\_cursor\_backup(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Backup net\_pkt cursor.

**Definition** net\_pkt.h:2101

[net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)

void net\_pkt\_compact(struct net\_pkt \*pkt)

Compact the fragment list of a packet.

[net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)

static int net\_pkt\_acknowledge\_data(struct net\_pkt \*pkt, struct net\_pkt\_data\_access \*access)

Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrit...

**Definition** net\_pkt.h:2545

[net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)

static int net\_pkt\_write\_le16(struct net\_pkt \*pkt, uint16\_t data)

Write a uint16\_t little endian data to a net\_pkt.

**Definition** net\_pkt.h:2396

[net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)

static void net\_pkt\_cursor\_restore(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Restore net\_pkt cursor from a backup.

**Definition** net\_pkt.h:2114

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

**Definition** net\_pkt.h:2377

[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)

struct net\_buf \* net\_pkt\_get\_reserve\_rx\_data(size\_t min\_len, k\_timeout\_t timeout)

Get RX DATA buffer from pool.

[net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)

bool net\_pkt\_is\_contiguous(struct net\_pkt \*pkt, size\_t size)

Check if a data size could fit contiguously.

[net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)

static int net\_pkt\_read\_u8(struct net\_pkt \*pkt, uint8\_t \*data)

Read a byte (uint8\_t) from a net\_pkt.

**Definition** net\_pkt.h:2248

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

**Definition** util\_macro.h:140

[net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)

static uint16\_t net\_eth\_vlan\_set\_vid(uint16\_t tci, uint16\_t vid)

Set VLAN identifier to TCI.

**Definition** ethernet\_vlan.h:78

[net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)

static uint8\_t net\_eth\_vlan\_get\_dei(uint16\_t tci)

Get Drop Eligible Indicator from TCI.

**Definition** ethernet\_vlan.h:53

[NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70)

#define NET\_VLAN\_TAG\_UNSPEC

Unspecified VLAN tag value.

**Definition** ethernet\_vlan.h:32

[net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)

static uint16\_t net\_eth\_vlan\_set\_dei(uint16\_t tci, bool dei)

Set Drop Eligible Indicator to TCI.

**Definition** ethernet\_vlan.h:91

[net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)

static uint16\_t net\_eth\_vlan\_get\_vid(uint16\_t tci)

Get VLAN identifier from TCI.

**Definition** ethernet\_vlan.h:41

[net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)

static uint16\_t net\_eth\_vlan\_set\_pcp(uint16\_t tci, uint8\_t pcp)

Set Priority Code Point to TCI.

**Definition** ethernet\_vlan.h:104

[net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)

static uint8\_t net\_eth\_vlan\_get\_pcp(uint16\_t tci)

Get Priority Code Point from TCI.

**Definition** ethernet\_vlan.h:65

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

**Definition** parser.h:96

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

**Definition** net\_ip.h:142

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

**Definition** net\_if.h:680

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

**Definition** net\_ip.h:388

[stat](structstat.md)

**Definition** stat.h:57

[sys\_cpu\_to\_le32](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)

#define sys\_cpu\_to\_le32(val)

Convert 32-bit integer from host endianness to little-endian.

**Definition** byteorder.h:270

[sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)

#define sys\_cpu\_to\_le16(val)

Convert 16-bit integer from host endianness to little-endian.

**Definition** byteorder.h:266

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_pkt.h](net__pkt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
