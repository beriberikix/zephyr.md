---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/net__pkt_8h_source.html
original_path: doxygen/html/net__pkt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

22#include <[zephyr/net/buf.h](net_2buf_8h.md)>

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

46

47struct [net\_context](structnet__context.md);

48

50

51/\* buffer cursor used in net\_pkt \*/

52struct net\_pkt\_cursor {

54 struct net\_buf \*buf;

56 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*pos;

57};

58

60

[ 67](structnet__pkt.md)struct [net\_pkt](structnet__pkt.md) {

[ 72](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22) [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) [fifo](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22);

73

[ 75](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54) struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54);

76

78 union {

[ 79](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6) struct [net\_buf](structnet__buf.md) \*[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6);

[ 80](structnet__pkt.md#ad319458430aa691b88e24776e843d30b) struct [net\_buf](structnet__buf.md) \*[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b);

81 };

82

[ 84](structnet__pkt.md#a52f155a86698a929fa2130b594630d06) struct net\_pkt\_cursor [cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06);

85

[ 87](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf) struct [net\_context](structnet__context.md) \*[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf);

88

[ 90](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

91

93

94#if defined(CONFIG\_NET\_TCP)

96 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) next;

97#endif

98#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

99 struct [net\_if](structnet__if.md) \*orig\_iface; /\* Original network interface \*/

100#endif

101

102#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

121 struct [net\_ptp\_time](structnet__ptp__time.md) timestamp;

122#endif

123

124#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

125 struct {

127 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time;

128

129#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

130 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

136 struct {

137 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stat](structstat.md)[NET\_PKT\_DETAIL\_STATS\_COUNT];

138 int count;

139 } detail;

140#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

141 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

142 };

143#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS \*/

144

146 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) atomic\_ref;

147

148 /\* Filled by layer 2 when network packet is received. \*/

149 struct net\_linkaddr lladdr\_src;

150 struct net\_linkaddr lladdr\_dst;

151 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ll\_proto\_type;

152

153#if defined(CONFIG\_NET\_IP)

154 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_hdr\_len; /\* pre-filled in order to avoid func call \*/

155#endif

156

157 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) overwrite : 1; /\* Is packet content being overwritten? \*/

158 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) eof : 1; /\* Last packet before EOF \*/

159 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ptp\_pkt : 1; /\* For outgoing packet: is this packet

160 \* a L2 PTP packet.

161 \* Used only if defined (CONFIG\_NET\_L2\_PTP)

162 \*/

163 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) forwarding : 1; /\* Are we forwarding this pkt

164 \* Used only if defined(CONFIG\_NET\_ROUTE)

165 \*/

166 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family : 3; /\* Address family, see net\_ip.h \*/

167

168 /\* bitfield byte alignment boundary \*/

169

170#if defined(CONFIG\_NET\_IPV4\_ACD)

171 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_acd\_arp\_msg : 1; /\* Is this pkt IPv4 conflict detection ARP

172 \* message.

173 \* Note: family needs to be

174 \* AF\_INET.

175 \*/

176#endif

177#if defined(CONFIG\_NET\_LLDP)

178 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lldp\_pkt : 1; /\* Is this pkt an LLDP message.

179 \* Note: family needs to be

180 \* AF\_UNSPEC.

181 \*/

182#endif

183 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ppp\_msg : 1; /\* This is a PPP message \*/

184 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) captured : 1; /\* Set to 1 if this packet is already being

185 \* captured

186 \*/

187 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) l2\_bridged : 1; /\* set to 1 if this packet comes from a bridge

188 \* and already contains its L2 header to be

189 \* preserved. Useful only if

190 \* defined(CONFIG\_NET\_ETHERNET\_BRIDGE).

191 \*/

192 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) l2\_processed : 1; /\* Set to 1 if this packet has already been

193 \* processed by the L2

194 \*/

195 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chksum\_done : 1; /\* Checksum has already been computed for

196 \* the packet.

197 \*/

198#if defined(CONFIG\_NET\_IP\_FRAGMENT)

199 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_reassembled : 1; /\* Packet is a reassembled IP packet. \*/

200#endif

201#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

202 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_timestamping : 1;

203 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rx\_timestamping : 1;

204#endif

205 /\* bitfield byte alignment boundary \*/

206

207#if defined(CONFIG\_NET\_IP)

208 union {

209 /\* IPv6 hop limit or IPv4 ttl for this network packet.

210 \* The value is shared between IPv6 and IPv4.

211 \*/

212#if defined(CONFIG\_NET\_IPV6)

213 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_hop\_limit;

214#endif

215#if defined(CONFIG\_NET\_IPV4)

216 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_ttl;

217#endif

218 };

219

220 union {

221#if defined(CONFIG\_NET\_IPV4)

222 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_opts\_len; /\* length of IPv4 header options \*/

223#endif

224#if defined(CONFIG\_NET\_IPV6)

225 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ipv6\_ext\_len; /\* length of extension headers \*/

226#endif

227 };

228

229#if defined(CONFIG\_NET\_IP\_FRAGMENT)

230 union {

231#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

232 struct {

233 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* Fragment offset and M (More Fragment) flag \*/

234 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id; /\* Fragment ID \*/

235 } ipv4\_fragment;

236#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

237#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

238 struct {

239 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* Fragment offset and M (More Fragment) flag \*/

240 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id; /\* Fragment id \*/

241 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_start; /\* Where starts the fragment header \*/

242 } ipv6\_fragment;

243#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

244 };

245#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

246

247#if defined(CONFIG\_NET\_IPV6)

248 /\* Where is the start of the last header before payload data

249 \* in IPv6 packet. This is offset value from start of the IPv6

250 \* packet. Note that this value should be updated by who ever

251 \* adds IPv6 extension headers to the network packet.

252 \*/

253 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ipv6\_prev\_hdr\_start;

254

255 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_ext\_opt\_len; /\* IPv6 ND option length \*/

256 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_next\_hdr; /\* What is the very first next header \*/

257#endif /\* CONFIG\_NET\_IPV6 \*/

258

259#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

261 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_dscp : 6;

262

264 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_ecn : 2;

265#endif /\* CONFIG\_NET\_IP\_DSCP\_ECN \*/

266#endif /\* CONFIG\_NET\_IP \*/

267

268#if defined(CONFIG\_NET\_VLAN)

269 /\* VLAN TCI (Tag Control Information). This contains the Priority

270 \* Code Point (PCP), Drop Eligible Indicator (DEI) and VLAN

271 \* Identifier (VID, called more commonly VLAN tag). This value is

272 \* kept in host byte order.

273 \*/

274 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vlan\_tci;

275#endif /\* CONFIG\_NET\_VLAN \*/

276

277#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

278 /\* TODO: Evolve this into a union of orthogonal

279 \* control block declarations if further L2

280 \* stacks require L2-specific attributes.

281 \*/

282#if defined(CONFIG\_IEEE802154)

283 /\* The following structure requires a 4-byte alignment

284 \* boundary to avoid padding.

285 \*/

286 struct net\_pkt\_cb\_ieee802154 cb;

287#endif /\* CONFIG\_IEEE802154 \*/

288#endif /\* NET\_PKT\_HAS\_CONTROL\_BLOCK \*/

289

293 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority;

294

295#if defined(CONFIG\_NET\_OFFLOAD) || defined(CONFIG\_NET\_L2\_IPIP)

296 /\* Remote address of the received packet. This is only used by

297 \* network interfaces with an offloaded TCP/IP stack, or if we

298 \* have network tunneling in use.

299 \*/

300 union {

301 struct sockaddr remote;

302

303 /\* This will make sure that there is enough storage to store

304 \* the address struct. The access to value is via remote

305 \* address.

306 \*/

307 struct sockaddr\_storage remote\_storage;

308 };

309#endif /\* CONFIG\_NET\_OFFLOAD \*/

310

311#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

312 /\* Tell the capture api that this is a captured packet \*/

313 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cooked\_mode\_pkt : 1;

314#endif /\* CONFIG\_NET\_CAPTURE\_COOKED\_MODE \*/

315

316 /\* @endcond \*/

317};

318

320

321/\* The interface real ll address \*/

322static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_if(struct [net\_pkt](structnet__pkt.md) \*pkt)

323{

324 return [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

325}

326

327static inline struct [net\_context](structnet__context.md) \*net\_pkt\_context(struct [net\_pkt](structnet__pkt.md) \*pkt)

328{

329 return pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf);

330}

331

332static inline void net\_pkt\_set\_context(struct [net\_pkt](structnet__pkt.md) \*pkt,

333 struct [net\_context](structnet__context.md) \*ctx)

334{

335 pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf) = ctx;

336}

337

338static inline struct [net\_if](structnet__if.md) \*net\_pkt\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

339{

340 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

341}

342

343static inline void net\_pkt\_set\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_if](structnet__if.md) \*iface)

344{

345 pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) = iface;

346

347 /\* If the network interface is set in pkt, then also set the type of

348 \* the network address that is stored in pkt. This is done here so

349 \* that the address type is properly set and is not forgotten.

350 \*/

351 if (iface) {

352 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type = [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

353

354 pkt->lladdr\_src.type = type;

355 pkt->lladdr\_dst.type = type;

356 }

357}

358

359static inline struct [net\_if](structnet__if.md) \*net\_pkt\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

360{

361#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

362 return pkt->orig\_iface;

363#else

364 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

365#endif

366}

367

368static inline void net\_pkt\_set\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt,

369 struct [net\_if](structnet__if.md) \*iface)

370{

371#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

372 pkt->orig\_iface = iface;

373#else

374 ARG\_UNUSED(pkt);

375 ARG\_UNUSED(iface);

376#endif

377}

378

379static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_family(struct [net\_pkt](structnet__pkt.md) \*pkt)

380{

381 return pkt->family;

382}

383

384static inline void net\_pkt\_set\_family(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family)

385{

386 pkt->family = family;

387}

388

389static inline bool net\_pkt\_is\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt)

390{

391 return !!(pkt->ptp\_pkt);

392}

393

394static inline void net\_pkt\_set\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_ptp)

395{

396 pkt->ptp\_pkt = is\_ptp;

397}

398

399static inline bool net\_pkt\_is\_tx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt)

400{

401#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

402 return !!(pkt->tx\_timestamping);

403#else

404 ARG\_UNUSED(pkt);

405

406 return false;

407#endif

408}

409

410static inline void net\_pkt\_set\_tx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_timestamping)

411{

412#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

413 pkt->tx\_timestamping = is\_timestamping;

414#else

415 ARG\_UNUSED(pkt);

416 ARG\_UNUSED(is\_timestamping);

417#endif

418}

419

420static inline bool net\_pkt\_is\_rx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt)

421{

422#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

423 return !!(pkt->rx\_timestamping);

424#else

425 ARG\_UNUSED(pkt);

426

427 return false;

428#endif

429}

430

431static inline void net\_pkt\_set\_rx\_timestamping(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_timestamping)

432{

433#if defined(CONFIG\_NET\_PKT\_TIMESTAMP)

434 pkt->rx\_timestamping = is\_timestamping;

435#else

436 ARG\_UNUSED(pkt);

437 ARG\_UNUSED(is\_timestamping);

438#endif

439}

440

441static inline bool net\_pkt\_is\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt)

442{

443 return !!(pkt->captured);

444}

445

446static inline void net\_pkt\_set\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_captured)

447{

448 pkt->captured = is\_captured;

449}

450

451static inline bool net\_pkt\_is\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt)

452{

453 return [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE) ? !!(pkt->l2\_bridged) : 0;

454}

455

456static inline void net\_pkt\_set\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_l2\_bridged)

457{

458 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE)) {

459 pkt->l2\_bridged = is\_l2\_bridged;

460 }

461}

462

463static inline bool net\_pkt\_is\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt)

464{

465 return !!(pkt->l2\_processed);

466}

467

468static inline void net\_pkt\_set\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt,

469 bool is\_l2\_processed)

470{

471 pkt->l2\_processed = is\_l2\_processed;

472}

473

474static inline bool net\_pkt\_is\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt)

475{

476 return !!(pkt->chksum\_done);

477}

478

479static inline void net\_pkt\_set\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt,

480 bool is\_chksum\_done)

481{

482 pkt->chksum\_done = is\_chksum\_done;

483}

484

485static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

486{

487#if defined(CONFIG\_NET\_IP)

488 return pkt->ip\_hdr\_len;

489#else

490 ARG\_UNUSED(pkt);

491

492 return 0;

493#endif

494}

495

496static inline void net\_pkt\_set\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

497{

498#if defined(CONFIG\_NET\_IP)

499 pkt->ip\_hdr\_len = len;

500#else

501 ARG\_UNUSED(pkt);

502 ARG\_UNUSED(len);

503#endif

504}

505

506static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt)

507{

508#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

509 return pkt->ip\_dscp;

510#else

511 ARG\_UNUSED(pkt);

512

513 return 0;

514#endif

515}

516

517static inline void net\_pkt\_set\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dscp)

518{

519#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

520 pkt->ip\_dscp = dscp;

521#else

522 ARG\_UNUSED(pkt);

523 ARG\_UNUSED(dscp);

524#endif

525}

526

527static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt)

528{

529#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

530 return pkt->ip\_ecn;

531#else

532 ARG\_UNUSED(pkt);

533

534 return 0;

535#endif

536}

537

538static inline void net\_pkt\_set\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ecn)

539{

540#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

541 pkt->ip\_ecn = ecn;

542#else

543 ARG\_UNUSED(pkt);

544 ARG\_UNUSED(ecn);

545#endif

546}

547

548static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt)

549{

550 return pkt->eof;

551}

552

553static inline void net\_pkt\_set\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt, bool eof)

554{

555 pkt->eof = eof;

556}

557

558static inline bool net\_pkt\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt)

559{

560 return !!(pkt->forwarding);

561}

562

563static inline void net\_pkt\_set\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt, bool forward)

564{

565 pkt->forwarding = forward;

566}

567

568#if defined(CONFIG\_NET\_IPV4)

569static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

570{

571 return pkt->ipv4\_ttl;

572}

573

574static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

575 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

576{

577 pkt->ipv4\_ttl = ttl;

578}

579

580static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

581{

582 return pkt->ipv4\_opts\_len;

583}

584

585static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

586 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

587{

588 pkt->ipv4\_opts\_len = opts\_len;

589}

590#else

591static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

592{

593 ARG\_UNUSED(pkt);

594

595 return 0;

596}

597

598static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

599 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

600{

601 ARG\_UNUSED(pkt);

602 ARG\_UNUSED(ttl);

603}

604

605static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

606{

607 ARG\_UNUSED(pkt);

608 return 0;

609}

610

611static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

612 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

613{

614 ARG\_UNUSED(pkt);

615 ARG\_UNUSED(opts\_len);

616}

617#endif

618

619#if defined(CONFIG\_NET\_IPV6)

620static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

621{

622 return pkt->ipv6\_ext\_opt\_len;

623}

624

625static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

626 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

627{

628 pkt->ipv6\_ext\_opt\_len = len;

629}

630

631static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

632{

633 return pkt->ipv6\_next\_hdr;

634}

635

636static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

637 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

638{

639 pkt->ipv6\_next\_hdr = next\_hdr;

640}

641

642static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

643{

644 return pkt->ipv6\_ext\_len;

645}

646

647static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

648{

649 pkt->ipv6\_ext\_len = len;

650}

651

652static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

653{

654 return pkt->ipv6\_prev\_hdr\_start;

655}

656

657static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

658 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

659{

660 pkt->ipv6\_prev\_hdr\_start = offset;

661}

662

663static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

664{

665 return pkt->ipv6\_hop\_limit;

666}

667

668static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

669 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

670{

671 pkt->ipv6\_hop\_limit = hop\_limit;

672}

673#else /\* CONFIG\_NET\_IPV6 \*/

674static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

675{

676 ARG\_UNUSED(pkt);

677

678 return 0;

679}

680

681static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

682 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

683{

684 ARG\_UNUSED(pkt);

685 ARG\_UNUSED(len);

686}

687

688static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

689{

690 ARG\_UNUSED(pkt);

691

692 return 0;

693}

694

695static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

696 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

697{

698 ARG\_UNUSED(pkt);

699 ARG\_UNUSED(next\_hdr);

700}

701

702static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

703{

704 ARG\_UNUSED(pkt);

705

706 return 0;

707}

708

709static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

710{

711 ARG\_UNUSED(pkt);

712 ARG\_UNUSED(len);

713}

714

715static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

716{

717 ARG\_UNUSED(pkt);

718

719 return 0;

720}

721

722static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

723 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

724{

725 ARG\_UNUSED(pkt);

726 ARG\_UNUSED(offset);

727}

728

729static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

730{

731 ARG\_UNUSED(pkt);

732

733 return 0;

734}

735

736static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

737 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

738{

739 ARG\_UNUSED(pkt);

740 ARG\_UNUSED(hop\_limit);

741}

742#endif /\* CONFIG\_NET\_IPV6 \*/

743

744static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ip\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

745{

746#if defined(CONFIG\_NET\_IPV6)

747 return pkt->ipv6\_ext\_len;

748#elif defined(CONFIG\_NET\_IPV4)

749 return pkt->ipv4\_opts\_len;

750#else

751 ARG\_UNUSED(pkt);

752

753 return 0;

754#endif

755}

756

757#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

758static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

759{

760 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_FRAGH\_OFFSET\_MASK) \* 8;

761}

762

763static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

764{

765 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_MORE\_FRAG\_MASK) != 0;

766}

767

768static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

769{

770 pkt->ipv4\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

771}

772

773static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

774{

775 return pkt->ipv4\_fragment.id;

776}

777

778static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

779{

780 pkt->ipv4\_fragment.id = id;

781}

782#else /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

783static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

784{

785 ARG\_UNUSED(pkt);

786

787 return 0;

788}

789

790static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

791{

792 ARG\_UNUSED(pkt);

793

794 return 0;

795}

796

797static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

798{

799 ARG\_UNUSED(pkt);

800 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

801}

802

803static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

804{

805 ARG\_UNUSED(pkt);

806

807 return 0;

808}

809

810static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

811{

812 ARG\_UNUSED(pkt);

813 ARG\_UNUSED(id);

814}

815#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

816

817#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

818static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

819{

820 return pkt->ipv6\_fragment.hdr\_start;

821}

822

823static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

824 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

825{

826 pkt->ipv6\_fragment.hdr\_start = start;

827}

828

829static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

830{

831 return pkt->ipv6\_fragment.flags & NET\_IPV6\_FRAGH\_OFFSET\_MASK;

832}

833static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

834{

835 return (pkt->ipv6\_fragment.flags & 0x01) != 0;

836}

837

838static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

839 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

840{

841 pkt->ipv6\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

842}

843

844static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

845{

846 return pkt->ipv6\_fragment.id;

847}

848

849static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

850 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

851{

852 pkt->ipv6\_fragment.id = id;

853}

854#else /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

855static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

856{

857 ARG\_UNUSED(pkt);

858

859 return 0;

860}

861

862static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

863 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

864{

865 ARG\_UNUSED(pkt);

866 ARG\_UNUSED(start);

867}

868

869static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

870{

871 ARG\_UNUSED(pkt);

872

873 return 0;

874}

875

876static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

877{

878 ARG\_UNUSED(pkt);

879

880 return 0;

881}

882

883static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

884 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

885{

886 ARG\_UNUSED(pkt);

887 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

888}

889

890static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

891{

892 ARG\_UNUSED(pkt);

893

894 return 0;

895}

896

897static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

898 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

899{

900 ARG\_UNUSED(pkt);

901 ARG\_UNUSED(id);

902}

903#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

904

905#if defined(CONFIG\_NET\_IP\_FRAGMENT)

906static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

907{

908 return !!(pkt->ip\_reassembled);

909}

910

911static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

912 bool reassembled)

913{

914 pkt->ip\_reassembled = reassembled;

915}

916#else /\* CONFIG\_NET\_IP\_FRAGMENT \*/

917static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

918{

919 ARG\_UNUSED(pkt);

920

921 return false;

922}

923

924static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

925 bool reassembled)

926{

927 ARG\_UNUSED(pkt);

928 ARG\_UNUSED(reassembled);

929}

930#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

931

932static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

933{

934 return pkt->priority;

935}

936

937static inline void net\_pkt\_set\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

938 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

939{

940 pkt->priority = priority;

941}

942

943#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

944static inline bool net\_pkt\_is\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt)

945{

946 return pkt->cooked\_mode\_pkt;

947}

948

949static inline void net\_pkt\_set\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

950{

951 pkt->cooked\_mode\_pkt = value;

952}

953#else

954static inline bool net\_pkt\_is\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt)

955{

956 ARG\_UNUSED(pkt);

957

958 return false;

959}

960

961static inline void net\_pkt\_set\_cooked\_mode(struct [net\_pkt](structnet__pkt.md) \*pkt, bool value)

962{

963 ARG\_UNUSED(pkt);

964 ARG\_UNUSED(value);

965}

966#endif /\* CONFIG\_NET\_CAPTURE\_COOKED\_MODE \*/

967

968#if defined(CONFIG\_NET\_VLAN)

969static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

970{

971 return [net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)(pkt->vlan\_tci);

972}

973

974static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

975{

976 pkt->vlan\_tci = [net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)(pkt->vlan\_tci, tag);

977}

978

979static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

980{

981 return [net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)(pkt->vlan\_tci);

982}

983

984static inline void net\_pkt\_set\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

985 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

986{

987 pkt->vlan\_tci = [net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)(pkt->vlan\_tci, priority);

988}

989

990static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

991{

992 return [net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)(pkt->vlan\_tci);

993}

994

995static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

996{

997 pkt->vlan\_tci = [net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)(pkt->vlan\_tci, dei);

998}

999

1000static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

1001{

1002 pkt->vlan\_tci = tci;

1003}

1004

1005static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

1006{

1007 return pkt->vlan\_tci;

1008}

1009#else

1010static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

1011{

1012 ARG\_UNUSED(pkt);

1013

1014 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70);

1015}

1016

1017static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

1018{

1019 ARG\_UNUSED(pkt);

1020 ARG\_UNUSED(tag);

1021}

1022

1023static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

1024{

1025 ARG\_UNUSED(pkt);

1026

1027 return 0;

1028}

1029

1030static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

1031{

1032 ARG\_UNUSED(pkt);

1033

1034 return false;

1035}

1036

1037static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

1038{

1039 ARG\_UNUSED(pkt);

1040 ARG\_UNUSED(dei);

1041}

1042

1043static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

1044{

1045 ARG\_UNUSED(pkt);

1046

1047 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70); /\* assumes priority is 0 \*/

1048}

1049

1050static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

1051{

1052 ARG\_UNUSED(pkt);

1053 ARG\_UNUSED(tci);

1054}

1055#endif

1056

1057#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

1058static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1059{

1060 return &pkt->timestamp;

1061}

1062

1063static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1064 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1065{

1066 pkt->timestamp.second = timestamp->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04);

1067 pkt->timestamp.nanosecond = timestamp->[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

1068}

1069

1070static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1071{

1072 return [net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)(&pkt->timestamp);

1073}

1074

1075static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1076{

1077 pkt->timestamp = [ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)(timestamp);

1078}

1079#else

1080static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1081{

1082 ARG\_UNUSED(pkt);

1083

1084 return NULL;

1085}

1086

1087static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1088 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1089{

1090 ARG\_UNUSED(pkt);

1091 ARG\_UNUSED(timestamp);

1092}

1093

1094static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1095{

1096 ARG\_UNUSED(pkt);

1097

1098 return 0;

1099}

1100

1101static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1102{

1103 ARG\_UNUSED(pkt);

1104 ARG\_UNUSED(timestamp);

1105}

1106#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP || CONFIG\_NET\_PKT\_TXTIME \*/

1107

1108#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

1109static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1110{

1111 return pkt->create\_time;

1112}

1113

1114static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1115 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1116{

1117 pkt->create\_time = create\_time;

1118}

1119#else

1120static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1121{

1122 ARG\_UNUSED(pkt);

1123

1124 return 0U;

1125}

1126

1127static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1128 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1129{

1130 ARG\_UNUSED(pkt);

1131 ARG\_UNUSED(create\_time);

1132}

1133#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS \*/

1134

1138static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_pkt\_txtime(struct [net\_pkt](structnet__pkt.md) \*pkt)

1139{

1140#if defined(CONFIG\_NET\_PKT\_TXTIME)

1141 return pkt->timestamp.second \* [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) + pkt->timestamp.nanosecond;

1142#else

1143 ARG\_UNUSED(pkt);

1144

1145 return 0;

1146#endif /\* CONFIG\_NET\_PKT\_TXTIME \*/

1147}

1148

1153static inline void net\_pkt\_set\_txtime(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) txtime)

1154{

1155#if defined(CONFIG\_NET\_PKT\_TXTIME)

1156 pkt->timestamp.second = txtime / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

1157 pkt->timestamp.nanosecond = txtime % [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

1158#else

1159 ARG\_UNUSED(pkt);

1160 ARG\_UNUSED(txtime);

1161#endif /\* CONFIG\_NET\_PKT\_TXTIME \*/

1162}

1163

1164#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

1165 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

1166static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1167{

1168 return pkt->detail.stat;

1169}

1170

1171static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1172{

1173 return pkt->detail.count;

1174}

1175

1176static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1177{

1178 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&pkt->detail, 0, sizeof(pkt->detail));

1179}

1180

1181static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt,

1182 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1183{

1184 if (pkt->detail.count >= NET\_PKT\_DETAIL\_STATS\_COUNT) {

1185 NET\_ERR("Detail stats count overflow (%d >= %d)",

1186 pkt->detail.count, NET\_PKT\_DETAIL\_STATS\_COUNT);

1187 return;

1188 }

1189

1190 pkt->detail.stat[pkt->detail.count++] = tick;

1191}

1192

1193#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1194#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1195#else

1196static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1197{

1198 ARG\_UNUSED(pkt);

1199

1200 return NULL;

1201}

1202

1203static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1204{

1205 ARG\_UNUSED(pkt);

1206

1207 return 0;

1208}

1209

1210static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1211{

1212 ARG\_UNUSED(pkt);

1213}

1214

1215static inline void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1216{

1217 ARG\_UNUSED(pkt);

1218 ARG\_UNUSED(tick);

1219}

1220

1221#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick)

1222#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick)

1223#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

1224 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

1225

1226static inline size\_t net\_pkt\_get\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

1227{

1228 return [net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)(pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6));

1229}

1230

1231static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1232{

1233 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1234}

1235

1236static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_ip\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1237{

1238 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1239}

1240

1241static inline bool net\_pkt\_is\_empty(struct [net\_pkt](structnet__pkt.md) \*pkt)

1242{

1243 return !pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b) || !net\_pkt\_data(pkt) || pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b)->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38) == 0;

1244}

1245

1246static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_src(struct [net\_pkt](structnet__pkt.md) \*pkt)

1247{

1248 return &pkt->lladdr\_src;

1249}

1250

1251static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_dst(struct [net\_pkt](structnet__pkt.md) \*pkt)

1252{

1253 return &pkt->lladdr\_dst;

1254}

1255

1256static inline void net\_pkt\_lladdr\_swap(struct [net\_pkt](structnet__pkt.md) \*pkt)

1257{

1258 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) = net\_pkt\_lladdr\_src(pkt)->addr;

1259

1260 net\_pkt\_lladdr\_src(pkt)->addr = net\_pkt\_lladdr\_dst(pkt)->addr;

1261 net\_pkt\_lladdr\_dst(pkt)->addr = [addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0);

1262}

1263

1264static inline void net\_pkt\_lladdr\_clear(struct [net\_pkt](structnet__pkt.md) \*pkt)

1265{

1266 net\_pkt\_lladdr\_src(pkt)->addr = NULL;

1267 net\_pkt\_lladdr\_src(pkt)->len = 0U;

1268}

1269

1270static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt)

1271{

1272 return pkt->ll\_proto\_type;

1273}

1274

1275static inline void net\_pkt\_set\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7))

1276{

1277 pkt->ll\_proto\_type = [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

1278}

1279

1280#if defined(CONFIG\_NET\_IPV4\_ACD)

1281static inline bool net\_pkt\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt)

1282{

1283 return !!(pkt->ipv4\_acd\_arp\_msg);

1284}

1285

1286static inline void net\_pkt\_set\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt,

1287 bool is\_acd\_arp\_msg)

1288{

1289 pkt->ipv4\_acd\_arp\_msg = is\_acd\_arp\_msg;

1290}

1291#else /\* CONFIG\_NET\_IPV4\_ACD \*/

1292static inline bool net\_pkt\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt)

1293{

1294 ARG\_UNUSED(pkt);

1295

1296 return false;

1297}

1298

1299static inline void net\_pkt\_set\_ipv4\_acd(struct [net\_pkt](structnet__pkt.md) \*pkt,

1300 bool is\_acd\_arp\_msg)

1301{

1302 ARG\_UNUSED(pkt);

1303 ARG\_UNUSED(is\_acd\_arp\_msg);

1304}

1305#endif /\* CONFIG\_NET\_IPV4\_ACD \*/

1306

1307#if defined(CONFIG\_NET\_LLDP)

1308static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1309{

1310 return !!(pkt->lldp\_pkt);

1311}

1312

1313static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1314{

1315 pkt->lldp\_pkt = is\_lldp;

1316}

1317#else

1318static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1319{

1320 ARG\_UNUSED(pkt);

1321

1322 return false;

1323}

1324

1325static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1326{

1327 ARG\_UNUSED(pkt);

1328 ARG\_UNUSED(is\_lldp);

1329}

1330#endif /\* CONFIG\_NET\_LLDP \*/

1331

1332#if defined(CONFIG\_NET\_L2\_PPP)

1333static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1334{

1335 return !!(pkt->ppp\_msg);

1336}

1337

1338static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1339 bool is\_ppp\_msg)

1340{

1341 pkt->ppp\_msg = is\_ppp\_msg;

1342}

1343#else /\* CONFIG\_NET\_L2\_PPP \*/

1344static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1345{

1346 ARG\_UNUSED(pkt);

1347

1348 return false;

1349}

1350

1351static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1352 bool is\_ppp\_msg)

1353{

1354 ARG\_UNUSED(pkt);

1355 ARG\_UNUSED(is\_ppp\_msg);

1356}

1357#endif /\* CONFIG\_NET\_L2\_PPP \*/

1358

1359#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

1360static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1361{

1362 return &pkt->cb;

1363}

1364#else

1365static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1366{

1367 ARG\_UNUSED(pkt);

1368

1369 return NULL;

1370}

1371#endif

1372

1373#define NET\_IPV6\_HDR(pkt) ((struct net\_ipv6\_hdr \*)net\_pkt\_ip\_data(pkt))

1374#define NET\_IPV4\_HDR(pkt) ((struct net\_ipv4\_hdr \*)net\_pkt\_ip\_data(pkt))

1375

1376static inline void net\_pkt\_set\_src\_ipv6\_addr(struct [net\_pkt](structnet__pkt.md) \*pkt)

1377{

1378 [net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)([net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)(

1379 net\_pkt\_context(pkt)),

1380 (struct [in6\_addr](structin6__addr.md) \*)NET\_IPV6\_HDR(pkt)->src);

1381}

1382

1383static inline void net\_pkt\_set\_overwrite(struct [net\_pkt](structnet__pkt.md) \*pkt, bool overwrite)

1384{

1385 pkt->overwrite = overwrite;

1386}

1387

1388static inline bool net\_pkt\_is\_being\_overwritten(struct [net\_pkt](structnet__pkt.md) \*pkt)

1389{

1390 return !!(pkt->overwrite);

1391}

1392

1393#ifdef CONFIG\_NET\_PKT\_FILTER

1394

1395bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1396bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1397

1398#else

1399

1400static inline bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1401{

1402 ARG\_UNUSED(pkt);

1403

1404 return true;

1405}

1406

1407static inline bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1408{

1409 ARG\_UNUSED(pkt);

1410

1411 return true;

1412}

1413

1414#endif /\* CONFIG\_NET\_PKT\_FILTER \*/

1415

1416#if defined(CONFIG\_NET\_PKT\_FILTER) && \

1417 (defined(CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK) || defined(CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK))

1418

1419bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1420

1421#else

1422

1423static inline bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1424{

1425 ARG\_UNUSED(pkt);

1426

1427 return true;

1428}

1429

1430#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK || CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK \*/

1431

1432#if defined(CONFIG\_NET\_PKT\_FILTER) && defined(CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK)

1433

1434bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1435

1436#else

1437

1438static inline bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1439{

1440 ARG\_UNUSED(pkt);

1441

1442 return true;

1443}

1444

1445#endif /\* CONFIG\_NET\_PKT\_FILTER && CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK \*/

1446

1447#if defined(CONFIG\_NET\_OFFLOAD) || defined(CONFIG\_NET\_L2\_IPIP)

1448static inline struct [sockaddr](structsockaddr.md) \*net\_pkt\_remote\_address(struct [net\_pkt](structnet__pkt.md) \*pkt)

1449{

1450 return &pkt->remote;

1451}

1452

1453static inline void net\_pkt\_set\_remote\_address(struct [net\_pkt](structnet__pkt.md) \*pkt,

1454 struct [sockaddr](structsockaddr.md) \*address,

1455 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) len)

1456{

1457 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(&pkt->remote, address, len);

1458}

1459#endif /\* CONFIG\_NET\_OFFLOAD || CONFIG\_NET\_L2\_IPIP \*/

1460

1461/\* @endcond \*/

1462

[ 1476](group__net__pkt.md#gafc7e98d5b64d816faabcbaa2ec22a2bb)#define NET\_PKT\_SLAB\_DEFINE(name, count) \

1477 K\_MEM\_SLAB\_DEFINE(name, sizeof(struct net\_pkt), count, 4)

1478

1480

1481/\* Backward compatibility macro \*/

1482#define NET\_PKT\_TX\_SLAB\_DEFINE(name, count) NET\_PKT\_SLAB\_DEFINE(name, count)

1483

1485

[ 1499](group__net__pkt.md#ga94ab6300b59d739c4e3c5604d3fbe8a5)#define NET\_PKT\_DATA\_POOL\_DEFINE(name, count) \

1500 NET\_BUF\_POOL\_DEFINE(name, count, CONFIG\_NET\_BUF\_DATA\_SIZE, \

1501 0, NULL)

1502

1504

1505#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC) || \

1506 (CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG)

1507#define NET\_PKT\_DEBUG\_ENABLED

1508#endif

1509

1510#if defined(NET\_PKT\_DEBUG\_ENABLED)

1511

1512/\* Debug versions of the net\_pkt functions that are used when tracking

1513 \* buffer usage.

1514 \*/

1515

1516struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_data\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1517 size\_t min\_len,

1518 [k\_timeout\_t](structk__timeout__t.md) timeout,

1519 const char \*caller,

1520 int line);

1521

1522#define net\_pkt\_get\_reserve\_data(pool, min\_len, timeout) \

1523 net\_pkt\_get\_reserve\_data\_debug(pool, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1524

1525struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_rx\_data\_debug(size\_t min\_len,

1526 [k\_timeout\_t](structk__timeout__t.md) timeout,

1527 const char \*caller,

1528 int line);

1529#define net\_pkt\_get\_reserve\_rx\_data(min\_len, timeout) \

1530 net\_pkt\_get\_reserve\_rx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1531

1532struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_tx\_data\_debug(size\_t min\_len,

1533 [k\_timeout\_t](structk__timeout__t.md) timeout,

1534 const char \*caller,

1535 int line);

1536#define net\_pkt\_get\_reserve\_tx\_data(min\_len, timeout) \

1537 net\_pkt\_get\_reserve\_tx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1538

1539struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_frag\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1540 [k\_timeout\_t](structk__timeout__t.md) timeout,

1541 const char \*caller, int line);

1542#define net\_pkt\_get\_frag(pkt, min\_len, timeout) \

1543 net\_pkt\_get\_frag\_debug(pkt, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1544

1545void net\_pkt\_unref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller, int line);

1546#define net\_pkt\_unref(pkt) net\_pkt\_unref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1547

1548struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_ref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller,

1549 int line);

1550#define net\_pkt\_ref(pkt) net\_pkt\_ref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1551

1552struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_ref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1553 const char \*caller, int line);

1554#define net\_pkt\_frag\_ref(frag) net\_pkt\_frag\_ref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1555

1556void net\_pkt\_frag\_unref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1557 const char \*caller, int line);

1558#define net\_pkt\_frag\_unref(frag) \

1559 net\_pkt\_frag\_unref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1560

1561struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_del\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1562 struct [net\_buf](structnet__buf.md) \*parent,

1563 struct [net\_buf](structnet__buf.md) \*frag,

1564 const char \*caller, int line);

1565#define net\_pkt\_frag\_del(pkt, parent, frag) \

1566 net\_pkt\_frag\_del\_debug(pkt, parent, frag, \_\_func\_\_, \_\_LINE\_\_)

1567

1568void net\_pkt\_frag\_add\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1569 const char \*caller, int line);

1570#define net\_pkt\_frag\_add(pkt, frag) \

1571 net\_pkt\_frag\_add\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1572

1573void net\_pkt\_frag\_insert\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1574 const char \*caller, int line);

1575#define net\_pkt\_frag\_insert(pkt, frag) \

1576 net\_pkt\_frag\_insert\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1577#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC ||

1578 \* CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

1579 \*/

1581

1589#if defined(NET\_PKT\_DEBUG\_ENABLED)

1590void [net\_pkt\_print\_frags](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1591#else

[ 1592](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)#define net\_pkt\_print\_frags(pkt)

1593#endif

1594

1609#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1610](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_data](group__net__pkt.md#ga6f697a97dd09e24663cbddc332ec5f7c)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1611 size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1612#endif

1613

1628#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1629](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1630#endif

1631

1646#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1647](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_tx\_data](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1648#endif

1649

1662#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1663](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_frag](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1664 [k\_timeout\_t](structk__timeout__t.md) timeout);

1665#endif

1666

1676#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1677](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)void [net\_pkt\_unref](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1678#endif

1679

1689#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1690](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_ref](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1691#endif

1692

1702#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1703](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_ref](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)(struct [net\_buf](structnet__buf.md) \*frag);

1704#endif

1705

1711#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1712](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)void [net\_pkt\_frag\_unref](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)(struct [net\_buf](structnet__buf.md) \*frag);

1713#endif

1714

1725#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1726](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_del](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1727 struct [net\_buf](structnet__buf.md) \*parent,

1728 struct [net\_buf](structnet__buf.md) \*frag);

1729#endif

1730

1737#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1738](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)void [net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1739#endif

1740

1747#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1748](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)void [net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1749#endif

1750

[ 1757](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)void [net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1758

[ 1767](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)void [net\_pkt\_get\_info](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)(struct k\_mem\_slab \*\*rx,

1768 struct k\_mem\_slab \*\*tx,

1769 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*rx\_data,

1770 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*tx\_data);

1771

1773

1774#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC)

1778void net\_pkt\_print(void);

1779

1780typedef void (\*net\_pkt\_allocs\_cb\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1781 struct [net\_buf](structnet__buf.md) \*buf,

1782 const char \*func\_alloc,

1783 int line\_alloc,

1784 const char \*func\_free,

1785 int line\_free,

1786 bool in\_use,

1787 void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1788

1789void net\_pkt\_allocs\_foreach(net\_pkt\_allocs\_cb\_t cb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1790

1791const char \*net\_pkt\_slab2str(struct k\_mem\_slab \*slab);

1792const char \*net\_pkt\_pool2str(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool);

1793

1794#else

1795#define net\_pkt\_print(...)

1796#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC \*/

1797

1798/\* New allocator, and API are defined below.

1799 \* This will be simpler when time will come to get rid of former API above.

1800 \*/

1801#if defined(NET\_PKT\_DEBUG\_ENABLED)

1802

1803struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1804 const char \*caller, int line);

1805#define net\_pkt\_alloc(\_timeout) \

1806 net\_pkt\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1807

1808struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_from\_slab\_debug(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1809 [k\_timeout\_t](structk__timeout__t.md) timeout,

1810 const char \*caller, int line);

1811#define net\_pkt\_alloc\_from\_slab(\_slab, \_timeout) \

1812 net\_pkt\_alloc\_from\_slab\_debug(\_slab, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1813

1814struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1815 const char \*caller, int line);

1816#define net\_pkt\_rx\_alloc(\_timeout) \

1817 net\_pkt\_rx\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1818

1819struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1820 [k\_timeout\_t](structk__timeout__t.md) timeout,

1821 const char \*caller,

1822 int line);

1823#define net\_pkt\_alloc\_on\_iface(\_iface, \_timeout) \

1824 net\_pkt\_alloc\_on\_iface\_debug(\_iface, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1825

1826struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1827 [k\_timeout\_t](structk__timeout__t.md) timeout,

1828 const char \*caller,

1829 int line);

1830#define net\_pkt\_rx\_alloc\_on\_iface(\_iface, \_timeout) \

1831 net\_pkt\_rx\_alloc\_on\_iface\_debug(\_iface, \_timeout, \

1832 \_\_func\_\_, \_\_LINE\_\_)

1833

1834int net\_pkt\_alloc\_buffer\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1835 size\_t size,

1836 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1837 [k\_timeout\_t](structk__timeout__t.md) timeout,

1838 const char \*caller, int line);

1839#define net\_pkt\_alloc\_buffer(\_pkt, \_size, \_proto, \_timeout) \

1840 net\_pkt\_alloc\_buffer\_debug(\_pkt, \_size, \_proto, \_timeout, \

1841 \_\_func\_\_, \_\_LINE\_\_)

1842

1843int net\_pkt\_alloc\_buffer\_raw\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

1844 [k\_timeout\_t](structk__timeout__t.md) timeout,

1845 const char \*caller, int line);

1846#define net\_pkt\_alloc\_buffer\_raw(\_pkt, \_size, \_timeout) \

1847 net\_pkt\_alloc\_buffer\_raw\_debug(\_pkt, \_size, \_timeout, \

1848 \_\_func\_\_, \_\_LINE\_\_)

1849

1850struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1851 size\_t size,

1852 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1853 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1854 [k\_timeout\_t](structk__timeout__t.md) timeout,

1855 const char \*caller,

1856 int line);

1857#define net\_pkt\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1858 \_proto, \_timeout) \

1859 net\_pkt\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1860 \_proto, \_timeout, \

1861 \_\_func\_\_, \_\_LINE\_\_)

1862

1863struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1864 size\_t size,

1865 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1866 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1867 [k\_timeout\_t](structk__timeout__t.md) timeout,

1868 const char \*caller,

1869 int line);

1870#define net\_pkt\_rx\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1871 \_proto, \_timeout) \

1872 net\_pkt\_rx\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1873 \_proto, \_timeout, \

1874 \_\_func\_\_, \_\_LINE\_\_)

1875#endif /\* NET\_PKT\_DEBUG\_ENABLED \*/

1877

1888#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1889](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)([k\_timeout\_t](structk__timeout__t.md) timeout);

1890#endif

1891

1906#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1907](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_from\_slab](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1908 [k\_timeout\_t](structk__timeout__t.md) timeout);

1909#endif

1910

1921#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1922](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_alloc](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)([k\_timeout\_t](structk__timeout__t.md) timeout);

1923#endif

1924

1933#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1934](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_on\_iface](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1935 [k\_timeout\_t](structk__timeout__t.md) timeout);

1936

1938

1939/\* Same as above but specifically for RX packet \*/

1940struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1941 [k\_timeout\_t](structk__timeout__t.md) timeout);

1943

1944#endif

1945

1961#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1962](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)int [net\_pkt\_alloc\_buffer](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1963 size\_t size,

1964 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1965 [k\_timeout\_t](structk__timeout__t.md) timeout);

1966#endif

1967

1981#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1982](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)int [net\_pkt\_alloc\_buffer\_raw](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

1983 [k\_timeout\_t](structk__timeout__t.md) timeout);

1984#endif

1985

1997#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1998](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_with\_buffer](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1999 size\_t size,

2000 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

2001 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2002 [k\_timeout\_t](structk__timeout__t.md) timeout);

2003

2005

2006/\* Same as above but specifically for RX packet \*/

2007struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

2008 size\_t size,

2009 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

2010 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

2011 [k\_timeout\_t](structk__timeout__t.md) timeout);

2012

2014

2015#endif

2016

[ 2023](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)void [net\_pkt\_append\_buffer](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b));

2024

[ 2035](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)size\_t [net\_pkt\_available\_buffer](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2036

[ 2052](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)size\_t [net\_pkt\_available\_payload\_buffer](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2053 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto);

2054

[ 2063](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)void [net\_pkt\_trim\_buffer](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2064

[ 2079](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)int [net\_pkt\_remove\_tail](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2080

[ 2088](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)void [net\_pkt\_cursor\_init](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2089

[ 2096](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)static inline void [net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2097 struct net\_pkt\_cursor \*backup)

2098{

2099 backup->buf = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).buf;

2100 backup->pos = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos;

2101}

2102

[ 2109](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)static inline void [net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2110 struct net\_pkt\_cursor \*backup)

2111{

2112 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).buf = backup->buf;

2113 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos = backup->pos;

2114}

2115

[ 2123](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)static inline void \*[net\_pkt\_cursor\_get\_pos](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)(struct [net\_pkt](structnet__pkt.md) \*pkt)

2124{

2125 return pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).pos;

2126}

2127

[ 2148](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)int [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2149

[ 2164](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)int [net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)(struct [net\_pkt](structnet__pkt.md) \*pkt, int byte, size\_t length);

2165

[ 2179](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)int [net\_pkt\_copy](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)(struct [net\_pkt](structnet__pkt.md) \*pkt\_dst,

2180 struct [net\_pkt](structnet__pkt.md) \*pkt\_src,

2181 size\_t length);

2182

[ 2192](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_clone](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2193

[ 2203](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_clone](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2204

[ 2213](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_shallow\_clone](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2214 [k\_timeout\_t](structk__timeout__t.md) timeout);

2215

[ 2229](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)int [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(struct [net\_pkt](structnet__pkt.md) \*pkt, void \*data, size\_t length);

2230

[ 2243](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)static inline int [net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

2244{

2245 return [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(pkt, data, 1);

2246}

2247

[ 2260](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)int [net\_pkt\_read\_be16](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2261

[ 2274](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)int [net\_pkt\_read\_le16](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2275

[ 2288](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)int [net\_pkt\_read\_be32](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

2289

[ 2303](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)int [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(struct [net\_pkt](structnet__pkt.md) \*pkt, const void \*data, size\_t length);

2304

[ 2317](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)static inline int [net\_pkt\_write\_u8](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data)

2318{

2319 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data, sizeof([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)));

2320}

2321

[ 2334](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)static inline int [net\_pkt\_write\_be16](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2335{

2336 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_be16 = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(data);

2337

2338 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2339}

2340

[ 2353](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)static inline int [net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2354{

2355 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_be32 = [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(data);

2356

2357 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2358}

2359

[ 2372](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)static inline int [net\_pkt\_write\_le32](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2373{

2374 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_le32 = [sys\_cpu\_to\_le32](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)(data);

2375

2376 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2377}

2378

[ 2391](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)static inline int [net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2392{

2393 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_le16 = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)(data);

2394

2395 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2396}

2397

[ 2405](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)size\_t [net\_pkt\_remaining\_data](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2406

[ 2419](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)int [net\_pkt\_update\_length](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2420

[ 2433](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)int [net\_pkt\_pull](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2434

[ 2443](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_pkt\_get\_current\_offset](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2444

[ 2456](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)bool [net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size);

2457

[ 2466](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)size\_t [net\_pkt\_get\_contiguous\_len](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2467

2469

2470struct net\_pkt\_data\_access {

2471#if !defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2472 void \*data;

2473#endif

2474 const size\_t size;

2475};

2476

2477#if defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2478#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2479 struct net\_pkt\_data\_access \_name = { \

2480 .size = sizeof(\_type), \

2481 }

2482

2483#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2484 NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type)

2485

2486#else

2487#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2488 \_type \_hdr\_##\_name; \

2489 struct net\_pkt\_data\_access \_name = { \

2490 .data = &\_hdr\_##\_name, \

2491 .size = sizeof(\_type), \

2492 }

2493

2494#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2495 struct net\_pkt\_data\_access \_name = { \

2496 .data = NULL, \

2497 .size = sizeof(\_type), \

2498 }

2499

2500#endif /\* CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS \*/

2501

2503

[ 2517](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)void \*[net\_pkt\_get\_data](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2518 struct net\_pkt\_data\_access \*access);

2519

[ 2533](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)int [net\_pkt\_set\_data](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2534 struct net\_pkt\_data\_access \*access);

2535

[ 2540](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)static inline int [net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2541 struct net\_pkt\_data\_access \*access)

2542{

2543 return [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(pkt, access->size);

2544}

2545

2549

2550#ifdef \_\_cplusplus

2551}

2552#endif

2553

2554#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_PKT\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[ethernet\_vlan.h](ethernet__vlan_8h.md)

VLAN specific definitions.

[NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

#define NSEC\_PER\_SEC

number of nanoseconds per second

**Definition** sys\_clock.h:107

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)

#define htons(x)

Convert 16-bit value from host to network byte order.

**Definition** net\_ip.h:120

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)

#define htonl(x)

Convert 32-bit value from host to network byte order.

**Definition** net\_ip.h:128

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:62

[net\_buf\_frags\_len](group__net__buf.md#gaebb95f08dbd4d38a250170aa78ddeb44)

static size\_t net\_buf\_frags\_len(const struct net\_buf \*buf)

Calculate amount of bytes stored in fragments.

**Definition** buf.h:2717

[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)

static struct net\_if \* net\_context\_get\_iface(struct net\_context \*context)

Get network interface for this context.

**Definition** net\_context.h:709

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:1075

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:2006

[net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)

void net\_pkt\_frag\_add(struct net\_pkt \*pkt, struct net\_buf \*frag)

Add a fragment to a packet at the end of its fragment list.

[net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)

static int net\_pkt\_write\_be32(struct net\_pkt \*pkt, uint32\_t data)

Write a uint32\_t big endian data to a net\_pkt.

**Definition** net\_pkt.h:2353

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

Print fragment list and the fragment sizes.

**Definition** net\_pkt.h:1592

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

**Definition** net\_pkt.h:2334

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

**Definition** net\_pkt.h:2317

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

**Definition** net\_pkt.h:2123

[net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)

void net\_pkt\_frag\_insert(struct net\_pkt \*pkt, struct net\_buf \*frag)

Insert a fragment to a packet at the beginning of its fragment list.

[net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)

int net\_pkt\_memset(struct net\_pkt \*pkt, int byte, size\_t length)

Memset some data in a net\_pkt.

[net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)

static void net\_pkt\_cursor\_backup(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Backup net\_pkt cursor.

**Definition** net\_pkt.h:2096

[net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)

void net\_pkt\_compact(struct net\_pkt \*pkt)

Compact the fragment list of a packet.

[net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)

static int net\_pkt\_acknowledge\_data(struct net\_pkt \*pkt, struct net\_pkt\_data\_access \*access)

Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrit...

**Definition** net\_pkt.h:2540

[net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)

static int net\_pkt\_write\_le16(struct net\_pkt \*pkt, uint16\_t data)

Write a uint16\_t little endian data to a net\_pkt.

**Definition** net\_pkt.h:2391

[net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)

static void net\_pkt\_cursor\_restore(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Restore net\_pkt cursor from a backup.

**Definition** net\_pkt.h:2109

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

**Definition** net\_pkt.h:2372

[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)

struct net\_buf \* net\_pkt\_get\_reserve\_rx\_data(size\_t min\_len, k\_timeout\_t timeout)

Get RX DATA buffer from pool.

[net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)

bool net\_pkt\_is\_contiguous(struct net\_pkt \*pkt, size\_t size)

Check if a data size could fit contiguously.

[net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)

static int net\_pkt\_read\_u8(struct net\_pkt \*pkt, uint8\_t \*data)

Read a byte (uint8\_t) from a net\_pkt.

**Definition** net\_pkt.h:2243

[net\_pkt\_get\_frag](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)

struct net\_buf \* net\_pkt\_get\_frag(struct net\_pkt \*pkt, size\_t min\_len, k\_timeout\_t timeout)

Get a data fragment that might be from user specific buffer pool or from global DATA pool.

[net\_pkt\_get\_contiguous\_len](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)

size\_t net\_pkt\_get\_contiguous\_len(struct net\_pkt \*pkt)

Get the contiguous buffer space.

[net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56)

int64\_t net\_time\_t

Any occurrence of net\_time\_t specifies a concept of nanosecond resolution scalar time span,...

**Definition** net\_time.h:101

[net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)

static net\_time\_t net\_ptp\_time\_to\_ns(struct net\_ptp\_time \*ts)

Convert a PTP timestamp to a nanosecond precision timestamp, both related to the local network refere...

**Definition** ptp\_time.h:208

[ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)

static struct net\_ptp\_time ns\_to\_net\_ptp\_time(net\_time\_t nsec)

Convert a nanosecond precision timestamp to a PTP timestamp, both related to the local network refere...

**Definition** ptp\_time.h:229

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)

static uint16\_t net\_eth\_vlan\_set\_vid(uint16\_t tci, uint16\_t vid)

Set VLAN identifier to TCI.

**Definition** ethernet\_vlan.h:76

[net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)

static uint8\_t net\_eth\_vlan\_get\_dei(uint16\_t tci)

Get Drop Eligible Indicator from TCI.

**Definition** ethernet\_vlan.h:51

[NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70)

#define NET\_VLAN\_TAG\_UNSPEC

Unspecified VLAN tag value.

**Definition** ethernet\_vlan.h:30

[net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)

static uint16\_t net\_eth\_vlan\_set\_dei(uint16\_t tci, bool dei)

Set Drop Eligible Indicator to TCI.

**Definition** ethernet\_vlan.h:89

[net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)

static uint16\_t net\_eth\_vlan\_get\_vid(uint16\_t tci)

Get VLAN identifier from TCI.

**Definition** ethernet\_vlan.h:39

[net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)

static uint16\_t net\_eth\_vlan\_set\_pcp(uint16\_t tci, uint8\_t pcp)

Set Priority Code Point to TCI.

**Definition** ethernet\_vlan.h:102

[net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)

static uint8\_t net\_eth\_vlan\_get\_pcp(uint16\_t tci)

Get Priority Code Point from TCI.

**Definition** ethernet\_vlan.h:63

[ieee802154\_pkt.h](ieee802154__pkt_8h.md)

Packet data common to all IEEE 802.15.4 L2 layers.

[types.h](include_2zephyr_2types_8h.md)

[buf.h](net_2buf_8h.md)

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

**Definition** net\_ip.h:139

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:1076

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:1004

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** buf.h:1030

[net\_buf::user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7)

uint8\_t user\_data[]

System metadata for this buffer.

**Definition** buf.h:1051

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:1033

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:205

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_linkaddr](structnet__linkaddr.md)

Hardware link address structure.

**Definition** net\_linkaddr.h:67

[net\_linkaddr::addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0)

uint8\_t \* addr

The array of byte representing the address.

**Definition** net\_linkaddr.h:69

[net\_linkaddr::type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7)

uint8\_t type

What kind of address is this for.

**Definition** net\_linkaddr.h:75

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

[net\_pkt::frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)

struct net\_buf \* frags

buffer fragment

**Definition** net\_pkt.h:79

[net\_pkt::context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf)

struct net\_context \* context

Network connection context.

**Definition** net\_pkt.h:87

[net\_pkt::cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06)

struct net\_pkt\_cursor cursor

Internal buffer iterator used for reading/writing.

**Definition** net\_pkt.h:84

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:90

[net\_pkt::fifo](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22)

intptr\_t fifo

The fifo is used by RX/TX threads and by socket layer.

**Definition** net\_pkt.h:72

[net\_pkt::buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b)

struct net\_buf \* buffer

alias to a buffer fragment

**Definition** net\_pkt.h:80

[net\_pkt::slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54)

struct k\_mem\_slab \* slab

Slab pointer from where it belongs to.

**Definition** net\_pkt.h:75

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:109

[net\_ptp\_time::nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e)

uint32\_t nanosecond

Nanoseconds.

**Definition** ptp\_time.h:132

[net\_ptp\_time::second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04)

uint64\_t second

Second value.

**Definition** ptp\_time.h:128

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

[stat](structstat.md)

**Definition** stat.h:92

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
