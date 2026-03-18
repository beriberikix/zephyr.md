---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__pkt_8h_source.html
original_path: doxygen/html/net__pkt_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

49/\* buffer cursor used in net\_pkt \*/

[ 50](structnet__pkt__cursor.md)struct [net\_pkt\_cursor](structnet__pkt__cursor.md) {

[ 52](structnet__pkt__cursor.md#af81267720cf13d06b90ddaa87fb7ad67) struct [net\_buf](structnet__buf.md) \*[buf](structnet__pkt__cursor.md#af81267720cf13d06b90ddaa87fb7ad67);

[ 54](structnet__pkt__cursor.md#a0901a4cc727e55b94e2dcb60f3c54caf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[pos](structnet__pkt__cursor.md#a0901a4cc727e55b94e2dcb60f3c54caf);

55};

56

[ 63](structnet__pkt.md)struct [net\_pkt](structnet__pkt.md) {

[ 68](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22) [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) [fifo](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22);

69

[ 71](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54) struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54);

72

74 union {

[ 75](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6) struct [net\_buf](structnet__buf.md) \*[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6);

[ 76](structnet__pkt.md#ad319458430aa691b88e24776e843d30b) struct [net\_buf](structnet__buf.md) \*[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b);

77 };

78

[ 80](structnet__pkt.md#a52f155a86698a929fa2130b594630d06) struct [net\_pkt\_cursor](structnet__pkt__cursor.md) [cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06);

81

[ 83](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf) struct [net\_context](structnet__context.md) \*[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf);

84

[ 86](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

87

89

90#if defined(CONFIG\_NET\_TCP)

92 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) next;

93#endif

94#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

95 struct [net\_if](structnet__if.md) \*orig\_iface; /\* Original network interface \*/

96#endif

97

98#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

117 struct [net\_ptp\_time](structnet__ptp__time.md) timestamp;

118#endif

119

120#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

121 struct {

123 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time;

124

125#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

126 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

132 struct {

133 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [stat](structstat.md)[NET\_PKT\_DETAIL\_STATS\_COUNT];

134 int count;

135 } detail;

136#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

137 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

138 };

139#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS \*/

140

142 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) atomic\_ref;

143

144 /\* Filled by layer 2 when network packet is received. \*/

145 struct net\_linkaddr lladdr\_src;

146 struct net\_linkaddr lladdr\_dst;

147 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ll\_proto\_type;

148

149#if defined(CONFIG\_NET\_IP)

150 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_hdr\_len; /\* pre-filled in order to avoid func call \*/

151#endif

152

153 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) overwrite : 1; /\* Is packet content being overwritten? \*/

154 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) eof : 1; /\* Last packet before EOF \*/

155 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ptp\_pkt : 1; /\* For outgoing packet: is this packet

156 \* a L2 PTP packet.

157 \* Used only if defined (CONFIG\_NET\_L2\_PTP)

158 \*/

159 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) forwarding : 1; /\* Are we forwarding this pkt

160 \* Used only if defined(CONFIG\_NET\_ROUTE)

161 \*/

162 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family : 3; /\* Address family, see net\_ip.h \*/

163

164 /\* bitfield byte alignment boundary \*/

165

166#if defined(CONFIG\_NET\_IPV4\_AUTO)

167 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_auto\_arp\_msg : 1; /\* Is this pkt IPv4 autoconf ARP

168 \* message.

169 \* Note: family needs to be

170 \* AF\_INET.

171 \*/

172#endif

173#if defined(CONFIG\_NET\_LLDP)

174 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lldp\_pkt : 1; /\* Is this pkt an LLDP message.

175 \* Note: family needs to be

176 \* AF\_UNSPEC.

177 \*/

178#endif

179 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ppp\_msg : 1; /\* This is a PPP message \*/

180#if defined(CONFIG\_NET\_TCP)

181 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tcp\_first\_msg : 1; /\* Is this the first time this pkt is

182 \* sent, or is this a resend of a TCP

183 \* segment.

184 \*/

185#endif

186 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) captured : 1; /\* Set to 1 if this packet is already being

187 \* captured

188 \*/

189 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) l2\_bridged : 1; /\* set to 1 if this packet comes from a bridge

190 \* and already contains its L2 header to be

191 \* preserved. Useful only if

192 \* defined(CONFIG\_NET\_ETHERNET\_BRIDGE).

193 \*/

194 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) l2\_processed : 1; /\* Set to 1 if this packet has already been

195 \* processed by the L2

196 \*/

197 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) chksum\_done : 1; /\* Checksum has already been computed for

198 \* the packet.

199 \*/

200#if defined(CONFIG\_NET\_IP\_FRAGMENT)

201 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_reassembled : 1; /\* Packet is a reassembled IP packet. \*/

202#endif

203 /\* bitfield byte alignment boundary \*/

204

205#if defined(CONFIG\_NET\_IP)

206 union {

207 /\* IPv6 hop limit or IPv4 ttl for this network packet.

208 \* The value is shared between IPv6 and IPv4.

209 \*/

210#if defined(CONFIG\_NET\_IPV6)

211 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_hop\_limit;

212#endif

213#if defined(CONFIG\_NET\_IPV4)

214 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_ttl;

215#endif

216 };

217

218 union {

219#if defined(CONFIG\_NET\_IPV4)

220 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv4\_opts\_len; /\* length of IPv4 header options \*/

221#endif

222#if defined(CONFIG\_NET\_IPV6)

223 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ipv6\_ext\_len; /\* length of extension headers \*/

224#endif

225 };

226

227#if defined(CONFIG\_NET\_IP\_FRAGMENT)

228 union {

229#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

230 struct {

231 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* Fragment offset and M (More Fragment) flag \*/

232 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id; /\* Fragment ID \*/

233 } ipv4\_fragment;

234#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

235#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

236 struct {

237 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9); /\* Fragment offset and M (More Fragment) flag \*/

238 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id; /\* Fragment id \*/

239 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_start; /\* Where starts the fragment header \*/

240 } ipv6\_fragment;

241#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

242 };

243#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

244

245#if defined(CONFIG\_NET\_IPV6)

246 /\* Where is the start of the last header before payload data

247 \* in IPv6 packet. This is offset value from start of the IPv6

248 \* packet. Note that this value should be updated by who ever

249 \* adds IPv6 extension headers to the network packet.

250 \*/

251 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ipv6\_prev\_hdr\_start;

252

253 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_ext\_opt\_len; /\* IPv6 ND option length \*/

254 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ipv6\_next\_hdr; /\* What is the very first next header \*/

255#endif /\* CONFIG\_NET\_IPV6 \*/

256

257#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

259 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_dscp : 6;

260

262 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ip\_ecn : 2;

263#endif /\* CONFIG\_NET\_IP\_DSCP\_ECN \*/

264#endif /\* CONFIG\_NET\_IP \*/

265

266#if defined(CONFIG\_NET\_VLAN)

267 /\* VLAN TCI (Tag Control Information). This contains the Priority

268 \* Code Point (PCP), Drop Eligible Indicator (DEI) and VLAN

269 \* Identifier (VID, called more commonly VLAN tag). This value is

270 \* kept in host byte order.

271 \*/

272 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vlan\_tci;

273#endif /\* CONFIG\_NET\_VLAN \*/

274

275#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

276 /\* TODO: Evolve this into a union of orthogonal

277 \* control block declarations if further L2

278 \* stacks require L2-specific attributes.

279 \*/

280#if defined(CONFIG\_IEEE802154)

281 /\* The following structure requires a 4-byte alignment

282 \* boundary to avoid padding.

283 \*/

284 struct net\_pkt\_cb\_ieee802154 cb;

285#endif /\* CONFIG\_IEEE802154 \*/

286#endif /\* NET\_PKT\_HAS\_CONTROL\_BLOCK \*/

287

291 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority;

292

293#if defined(CONFIG\_NET\_OFFLOAD)

294 /\* Remote address of the recived packet. This is only used by

295 \* network interfaces with an offloaded TCP/IP stack.

296 \*/

297 struct sockaddr remote;

298#endif /\* CONFIG\_NET\_OFFLOAD \*/

299

300 /\* @endcond \*/

301};

302

304

305/\* The interface real ll address \*/

306static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_if(struct [net\_pkt](structnet__pkt.md) \*pkt)

307{

308 return [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2));

309}

310

311static inline struct [net\_context](structnet__context.md) \*net\_pkt\_context(struct [net\_pkt](structnet__pkt.md) \*pkt)

312{

313 return pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf);

314}

315

316static inline void net\_pkt\_set\_context(struct [net\_pkt](structnet__pkt.md) \*pkt,

317 struct [net\_context](structnet__context.md) \*ctx)

318{

319 pkt->[context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf) = ctx;

320}

321

322static inline struct [net\_if](structnet__if.md) \*net\_pkt\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

323{

324 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

325}

326

327static inline void net\_pkt\_set\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_if](structnet__if.md) \*iface)

328{

329 pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2) = iface;

330

331 /\* If the network interface is set in pkt, then also set the type of

332 \* the network address that is stored in pkt. This is done here so

333 \* that the address type is properly set and is not forgotten.

334 \*/

335 if (iface) {

336 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type = [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)(iface)->[type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

337

338 pkt->lladdr\_src.type = type;

339 pkt->lladdr\_dst.type = type;

340 }

341}

342

343static inline struct [net\_if](structnet__if.md) \*net\_pkt\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt)

344{

345#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

346 return pkt->orig\_iface;

347#else

348 return pkt->[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2);

349#endif

350}

351

352static inline void net\_pkt\_set\_orig\_iface(struct [net\_pkt](structnet__pkt.md) \*pkt,

353 struct [net\_if](structnet__if.md) \*iface)

354{

355#if defined(CONFIG\_NET\_ROUTING) || defined(CONFIG\_NET\_ETHERNET\_BRIDGE)

356 pkt->orig\_iface = iface;

357#endif

358}

359

360static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_family(struct [net\_pkt](structnet__pkt.md) \*pkt)

361{

362 return pkt->family;

363}

364

365static inline void net\_pkt\_set\_family(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) family)

366{

367 pkt->family = family;

368}

369

370static inline bool net\_pkt\_is\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt)

371{

372 return !!(pkt->ptp\_pkt);

373}

374

375static inline void net\_pkt\_set\_ptp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_ptp)

376{

377 pkt->ptp\_pkt = is\_ptp;

378}

379

380static inline bool net\_pkt\_is\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt)

381{

382 return !!(pkt->captured);

383}

384

385static inline void net\_pkt\_set\_captured(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_captured)

386{

387 pkt->captured = is\_captured;

388}

389

390static inline bool net\_pkt\_is\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt)

391{

392 return [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE) ? !!(pkt->l2\_bridged) : 0;

393}

394

395static inline void net\_pkt\_set\_l2\_bridged(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_l2\_bridged)

396{

397 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_ETHERNET\_BRIDGE)) {

398 pkt->l2\_bridged = is\_l2\_bridged;

399 }

400}

401

402static inline bool net\_pkt\_is\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt)

403{

404 return !!(pkt->l2\_processed);

405}

406

407static inline void net\_pkt\_set\_l2\_processed(struct [net\_pkt](structnet__pkt.md) \*pkt,

408 bool is\_l2\_processed)

409{

410 pkt->l2\_processed = is\_l2\_processed;

411}

412

413static inline bool net\_pkt\_is\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt)

414{

415 return !!(pkt->chksum\_done);

416}

417

418static inline void net\_pkt\_set\_chksum\_done(struct [net\_pkt](structnet__pkt.md) \*pkt,

419 bool is\_chksum\_done)

420{

421 pkt->chksum\_done = is\_chksum\_done;

422}

423

424static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

425{

426#if defined(CONFIG\_NET\_IP)

427 return pkt->ip\_hdr\_len;

428#else

429 return 0;

430#endif

431}

432

433static inline void net\_pkt\_set\_ip\_hdr\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

434{

435#if defined(CONFIG\_NET\_IP)

436 pkt->ip\_hdr\_len = len;

437#endif

438}

439

440static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt)

441{

442#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

443 return pkt->ip\_dscp;

444#else

445 return 0;

446#endif

447}

448

449static inline void net\_pkt\_set\_ip\_dscp(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dscp)

450{

451#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

452 pkt->ip\_dscp = dscp;

453#endif

454}

455

456static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt)

457{

458#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

459 return pkt->ip\_ecn;

460#else

461 return 0;

462#endif

463}

464

465static inline void net\_pkt\_set\_ip\_ecn(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ecn)

466{

467#if defined(CONFIG\_NET\_IP\_DSCP\_ECN)

468 pkt->ip\_ecn = ecn;

469#endif

470}

471

472static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_tcp\_1st\_msg(struct [net\_pkt](structnet__pkt.md) \*pkt)

473{

474#if defined(CONFIG\_NET\_TCP)

475 return pkt->tcp\_first\_msg;

476#else

477 return true;

478#endif

479}

480

481static inline void net\_pkt\_set\_tcp\_1st\_msg(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_1st)

482{

483#if defined(CONFIG\_NET\_TCP)

484 pkt->tcp\_first\_msg = is\_1st;

485#else

486 ARG\_UNUSED(pkt);

487 ARG\_UNUSED(is\_1st);

488#endif

489}

490

491static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt)

492{

493 return pkt->eof;

494}

495

496static inline void net\_pkt\_set\_eof(struct [net\_pkt](structnet__pkt.md) \*pkt, bool eof)

497{

498 pkt->eof = eof;

499}

500

501static inline bool net\_pkt\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt)

502{

503 return !!(pkt->forwarding);

504}

505

506static inline void net\_pkt\_set\_forwarding(struct [net\_pkt](structnet__pkt.md) \*pkt, bool forward)

507{

508 pkt->forwarding = forward;

509}

510

511#if defined(CONFIG\_NET\_IPV4)

512static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

513{

514 return pkt->ipv4\_ttl;

515}

516

517static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

518 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

519{

520 pkt->ipv4\_ttl = ttl;

521}

522

523static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

524{

525 return pkt->ipv4\_opts\_len;

526}

527

528static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

529 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

530{

531 pkt->ipv4\_opts\_len = opts\_len;

532}

533#else

534static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt)

535{

536 ARG\_UNUSED(pkt);

537

538 return 0;

539}

540

541static inline void net\_pkt\_set\_ipv4\_ttl(struct [net\_pkt](structnet__pkt.md) \*pkt,

542 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl)

543{

544 ARG\_UNUSED(pkt);

545 ARG\_UNUSED(ttl);

546}

547

548static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

549{

550 ARG\_UNUSED(pkt);

551 return 0;

552}

553

554static inline void net\_pkt\_set\_ipv4\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

555 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opts\_len)

556{

557 ARG\_UNUSED(pkt);

558 ARG\_UNUSED(opts\_len);

559}

560#endif

561

562#if defined(CONFIG\_NET\_IPV6)

563static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

564{

565 return pkt->ipv6\_ext\_opt\_len;

566}

567

568static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

569 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

570{

571 pkt->ipv6\_ext\_opt\_len = len;

572}

573

574static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

575{

576 return pkt->ipv6\_next\_hdr;

577}

578

579static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

580 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

581{

582 pkt->ipv6\_next\_hdr = next\_hdr;

583}

584

585static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

586{

587 return pkt->ipv6\_ext\_len;

588}

589

590static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

591{

592 pkt->ipv6\_ext\_len = len;

593}

594

595static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

596{

597 return pkt->ipv6\_prev\_hdr\_start;

598}

599

600static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

601 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

602{

603 pkt->ipv6\_prev\_hdr\_start = offset;

604}

605

606static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

607{

608 return pkt->ipv6\_hop\_limit;

609}

610

611static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

612 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

613{

614 pkt->ipv6\_hop\_limit = hop\_limit;

615}

616#else /\* CONFIG\_NET\_IPV6 \*/

617static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

618{

619 ARG\_UNUSED(pkt);

620

621 return 0;

622}

623

624static inline void net\_pkt\_set\_ipv6\_ext\_opt\_len(struct [net\_pkt](structnet__pkt.md) \*pkt,

625 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len)

626{

627 ARG\_UNUSED(pkt);

628 ARG\_UNUSED(len);

629}

630

631static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt)

632{

633 ARG\_UNUSED(pkt);

634

635 return 0;

636}

637

638static inline void net\_pkt\_set\_ipv6\_next\_hdr(struct [net\_pkt](structnet__pkt.md) \*pkt,

639 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) next\_hdr)

640{

641 ARG\_UNUSED(pkt);

642 ARG\_UNUSED(next\_hdr);

643}

644

645static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

646{

647 ARG\_UNUSED(pkt);

648

649 return 0;

650}

651

652static inline void net\_pkt\_set\_ipv6\_ext\_len(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

653{

654 ARG\_UNUSED(pkt);

655 ARG\_UNUSED(len);

656}

657

658static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt)

659{

660 ARG\_UNUSED(pkt);

661

662 return 0;

663}

664

665static inline void net\_pkt\_set\_ipv6\_hdr\_prev(struct [net\_pkt](structnet__pkt.md) \*pkt,

666 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset)

667{

668 ARG\_UNUSED(pkt);

669 ARG\_UNUSED(offset);

670}

671

672static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt)

673{

674 ARG\_UNUSED(pkt);

675

676 return 0;

677}

678

679static inline void net\_pkt\_set\_ipv6\_hop\_limit(struct [net\_pkt](structnet__pkt.md) \*pkt,

680 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit)

681{

682 ARG\_UNUSED(pkt);

683 ARG\_UNUSED(hop\_limit);

684}

685#endif /\* CONFIG\_NET\_IPV6 \*/

686

687static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ip\_opts\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

688{

689#if defined(CONFIG\_NET\_IPV6)

690 return pkt->ipv6\_ext\_len;

691#elif defined(CONFIG\_NET\_IPV4)

692 return pkt->ipv4\_opts\_len;

693#else

694 ARG\_UNUSED(pkt);

695

696 return 0;

697#endif

698}

699

700#if defined(CONFIG\_NET\_IPV4\_FRAGMENT)

701static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

702{

703 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_FRAGH\_OFFSET\_MASK) \* 8;

704}

705

706static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

707{

708 return (pkt->ipv4\_fragment.flags & NET\_IPV4\_MORE\_FRAG\_MASK) != 0;

709}

710

711static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

712{

713 pkt->ipv4\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

714}

715

716static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

717{

718 return pkt->ipv4\_fragment.id;

719}

720

721static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

722{

723 pkt->ipv4\_fragment.id = id;

724}

725#else /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

726static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv4\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

727{

728 ARG\_UNUSED(pkt);

729

730 return 0;

731}

732

733static inline bool net\_pkt\_ipv4\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

734{

735 ARG\_UNUSED(pkt);

736

737 return 0;

738}

739

740static inline void net\_pkt\_set\_ipv4\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

741{

742 ARG\_UNUSED(pkt);

743 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

744}

745

746static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

747{

748 ARG\_UNUSED(pkt);

749

750 return 0;

751}

752

753static inline void net\_pkt\_set\_ipv4\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

754{

755 ARG\_UNUSED(pkt);

756 ARG\_UNUSED(id);

757}

758#endif /\* CONFIG\_NET\_IPV4\_FRAGMENT \*/

759

760#if defined(CONFIG\_NET\_IPV6\_FRAGMENT)

761static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

762{

763 return pkt->ipv6\_fragment.hdr\_start;

764}

765

766static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

767 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

768{

769 pkt->ipv6\_fragment.hdr\_start = start;

770}

771

772static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

773{

774 return pkt->ipv6\_fragment.flags & NET\_IPV6\_FRAGH\_OFFSET\_MASK;

775}

776static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

777{

778 return (pkt->ipv6\_fragment.flags & 0x01) != 0;

779}

780

781static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

782 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

783{

784 pkt->ipv6\_fragment.flags = [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

785}

786

787static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

788{

789 return pkt->ipv6\_fragment.id;

790}

791

792static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

793 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

794{

795 pkt->ipv6\_fragment.id = id;

796}

797#else /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

798static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt)

799{

800 ARG\_UNUSED(pkt);

801

802 return 0;

803}

804

805static inline void net\_pkt\_set\_ipv6\_fragment\_start(struct [net\_pkt](structnet__pkt.md) \*pkt,

806 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start)

807{

808 ARG\_UNUSED(pkt);

809 ARG\_UNUSED(start);

810}

811

812static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ipv6\_fragment\_offset(struct [net\_pkt](structnet__pkt.md) \*pkt)

813{

814 ARG\_UNUSED(pkt);

815

816 return 0;

817}

818

819static inline bool net\_pkt\_ipv6\_fragment\_more(struct [net\_pkt](structnet__pkt.md) \*pkt)

820{

821 ARG\_UNUSED(pkt);

822

823 return 0;

824}

825

826static inline void net\_pkt\_set\_ipv6\_fragment\_flags(struct [net\_pkt](structnet__pkt.md) \*pkt,

827 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

828{

829 ARG\_UNUSED(pkt);

830 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

831}

832

833static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt)

834{

835 ARG\_UNUSED(pkt);

836

837 return 0;

838}

839

840static inline void net\_pkt\_set\_ipv6\_fragment\_id(struct [net\_pkt](structnet__pkt.md) \*pkt,

841 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id)

842{

843 ARG\_UNUSED(pkt);

844 ARG\_UNUSED(id);

845}

846#endif /\* CONFIG\_NET\_IPV6\_FRAGMENT \*/

847

848#if defined(CONFIG\_NET\_IP\_FRAGMENT)

849static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

850{

851 return !!(pkt->ip\_reassembled);

852}

853

854static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

855 bool reassembled)

856{

857 pkt->ip\_reassembled = reassembled;

858}

859#else /\* CONFIG\_NET\_IP\_FRAGMENT \*/

860static inline bool net\_pkt\_is\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt)

861{

862 ARG\_UNUSED(pkt);

863

864 return false;

865}

866

867static inline void net\_pkt\_set\_ip\_reassembled(struct [net\_pkt](structnet__pkt.md) \*pkt,

868 bool reassembled)

869{

870 ARG\_UNUSED(pkt);

871 ARG\_UNUSED(reassembled);

872}

873#endif /\* CONFIG\_NET\_IP\_FRAGMENT \*/

874

875static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

876{

877 return pkt->priority;

878}

879

880static inline void net\_pkt\_set\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

881 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

882{

883 pkt->priority = priority;

884}

885

886#if defined(CONFIG\_NET\_VLAN)

887static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

888{

889 return [net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6)(pkt->vlan\_tci);

890}

891

892static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

893{

894 pkt->vlan\_tci = [net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd)(pkt->vlan\_tci, tag);

895}

896

897static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

898{

899 return [net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a)(pkt->vlan\_tci);

900}

901

902static inline void net\_pkt\_set\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt,

903 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) priority)

904{

905 pkt->vlan\_tci = [net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10)(pkt->vlan\_tci, priority);

906}

907

908static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

909{

910 return [net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b)(pkt->vlan\_tci);

911}

912

913static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

914{

915 pkt->vlan\_tci = [net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab)(pkt->vlan\_tci, dei);

916}

917

918static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

919{

920 pkt->vlan\_tci = tci;

921}

922

923static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

924{

925 return pkt->vlan\_tci;

926}

927#else

928static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt)

929{

930 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70);

931}

932

933static inline void net\_pkt\_set\_vlan\_tag(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag)

934{

935 ARG\_UNUSED(pkt);

936 ARG\_UNUSED(tag);

937}

938

939static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_pkt\_vlan\_priority(struct [net\_pkt](structnet__pkt.md) \*pkt)

940{

941 ARG\_UNUSED(pkt);

942 return 0;

943}

944

945static inline bool net\_pkt\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt)

946{

947 return false;

948}

949

950static inline void net\_pkt\_set\_vlan\_dei(struct [net\_pkt](structnet__pkt.md) \*pkt, bool dei)

951{

952 ARG\_UNUSED(pkt);

953 ARG\_UNUSED(dei);

954}

955

956static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt)

957{

958 return [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70); /\* assumes priority is 0 \*/

959}

960

961static inline void net\_pkt\_set\_vlan\_tci(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci)

962{

963 ARG\_UNUSED(pkt);

964 ARG\_UNUSED(tci);

965}

966#endif

967

968#if defined(CONFIG\_NET\_PKT\_TIMESTAMP) || defined(CONFIG\_NET\_PKT\_TXTIME)

969static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

970{

971 return &pkt->timestamp;

972}

973

974static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

975 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

976{

977 pkt->timestamp.second = timestamp->[second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04);

978 pkt->timestamp.nanosecond = timestamp->[nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e);

979}

980

981static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

982{

983 return [net\_ptp\_time\_to\_ns](group__ptp__time.md#gaf9f253990e644e161e1b3cc317e8e9e9)(&pkt->timestamp);

984}

985

986static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

987{

988 pkt->timestamp = [ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)(timestamp);

989}

990#else

991static inline struct [net\_ptp\_time](structnet__ptp__time.md) \*net\_pkt\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt)

992{

993 ARG\_UNUSED(pkt);

994

995 return NULL;

996}

997

998static inline void net\_pkt\_set\_timestamp(struct [net\_pkt](structnet__pkt.md) \*pkt,

999 struct [net\_ptp\_time](structnet__ptp__time.md) \*timestamp)

1000{

1001 ARG\_UNUSED(pkt);

1002 ARG\_UNUSED(timestamp);

1003}

1004

1005static inline [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) net\_pkt\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt)

1006{

1007 ARG\_UNUSED(pkt);

1008

1009 return 0;

1010}

1011

1012static inline void net\_pkt\_set\_timestamp\_ns(struct [net\_pkt](structnet__pkt.md) \*pkt, [net\_time\_t](group__net__time.md#gaf1da332e3909fca30de991cc2f950e56) timestamp)

1013{

1014 ARG\_UNUSED(pkt);

1015 ARG\_UNUSED(timestamp);

1016}

1017#endif /\* CONFIG\_NET\_PKT\_TIMESTAMP || CONFIG\_NET\_PKT\_TXTIME \*/

1018

1019#if defined(CONFIG\_NET\_PKT\_RXTIME\_STATS) || defined(CONFIG\_NET\_PKT\_TXTIME\_STATS)

1020static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1021{

1022 return pkt->create\_time;

1023}

1024

1025static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1026 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1027{

1028 pkt->create\_time = create\_time;

1029}

1030#else

1031static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_pkt\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt)

1032{

1033 ARG\_UNUSED(pkt);

1034

1035 return 0U;

1036}

1037

1038static inline void net\_pkt\_set\_create\_time(struct [net\_pkt](structnet__pkt.md) \*pkt,

1039 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) create\_time)

1040{

1041 ARG\_UNUSED(pkt);

1042 ARG\_UNUSED(create\_time);

1043}

1044#endif /\* CONFIG\_NET\_PKT\_RXTIME\_STATS || CONFIG\_NET\_PKT\_TXTIME\_STATS \*/

1045

1049static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) net\_pkt\_txtime(struct [net\_pkt](structnet__pkt.md) \*pkt)

1050{

1051#if defined(CONFIG\_NET\_PKT\_TXTIME)

1052 return pkt->timestamp.second \* [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc) + pkt->timestamp.nanosecond;

1053#else

1054 ARG\_UNUSED(pkt);

1055

1056 return 0;

1057#endif /\* CONFIG\_NET\_PKT\_TXTIME \*/

1058}

1059

1064static inline void net\_pkt\_set\_txtime(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) txtime)

1065{

1066#if defined(CONFIG\_NET\_PKT\_TXTIME)

1067 pkt->timestamp.second = txtime / [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

1068 pkt->timestamp.nanosecond = txtime % [NSEC\_PER\_SEC](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc);

1069#else

1070 ARG\_UNUSED(pkt);

1071 ARG\_UNUSED(txtime);

1072#endif /\* CONFIG\_NET\_PKT\_TXTIME \*/

1073}

1074

1075#if defined(CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL) || \

1076 defined(CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL)

1077static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1078{

1079 return pkt->detail.stat;

1080}

1081

1082static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1083{

1084 return pkt->detail.count;

1085}

1086

1087static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1088{

1089 [memset](string_8h.md#a4137694174d4ca2fad886a1db355015c)(&pkt->detail, 0, sizeof(pkt->detail));

1090}

1091

1092static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt,

1093 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1094{

1095 if (pkt->detail.count >= NET\_PKT\_DETAIL\_STATS\_COUNT) {

1096 NET\_ERR("Detail stats count overflow (%d >= %d)",

1097 pkt->detail.count, NET\_PKT\_DETAIL\_STATS\_COUNT);

1098 return;

1099 }

1100

1101 pkt->detail.stat[pkt->detail.count++] = tick;

1102}

1103

1104#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1105#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick) net\_pkt\_set\_stats\_tick(pkt, tick)

1106#else

1107static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*net\_pkt\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt)

1108{

1109 ARG\_UNUSED(pkt);

1110

1111 return NULL;

1112}

1113

1114static inline int net\_pkt\_stats\_tick\_count(struct [net\_pkt](structnet__pkt.md) \*pkt)

1115{

1116 ARG\_UNUSED(pkt);

1117

1118 return 0;

1119}

1120

1121static inline void net\_pkt\_stats\_tick\_reset(struct [net\_pkt](structnet__pkt.md) \*pkt)

1122{

1123 ARG\_UNUSED(pkt);

1124}

1125

1126static inline void net\_pkt\_set\_stats\_tick(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tick)

1127{

1128 ARG\_UNUSED(pkt);

1129 ARG\_UNUSED(tick);

1130}

1131

1132#define net\_pkt\_set\_tx\_stats\_tick(pkt, tick)

1133#define net\_pkt\_set\_rx\_stats\_tick(pkt, tick)

1134#endif /\* CONFIG\_NET\_PKT\_TXTIME\_STATS\_DETAIL ||

1135 CONFIG\_NET\_PKT\_RXTIME\_STATS\_DETAIL \*/

1136

1137static inline size\_t net\_pkt\_get\_len(struct [net\_pkt](structnet__pkt.md) \*pkt)

1138{

1139 return [net\_buf\_frags\_len](group__net__buf.md#gaea38d8a418b739fa335e30ed91d9943d)(pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6));

1140}

1141

1142static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1143{

1144 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1145}

1146

1147static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*net\_pkt\_ip\_data(struct [net\_pkt](structnet__pkt.md) \*pkt)

1148{

1149 return pkt->[frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)->[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56);

1150}

1151

1152static inline bool net\_pkt\_is\_empty(struct [net\_pkt](structnet__pkt.md) \*pkt)

1153{

1154 return !pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b) || !net\_pkt\_data(pkt) || pkt->[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b)->[len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38) == 0;

1155}

1156

1157static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_src(struct [net\_pkt](structnet__pkt.md) \*pkt)

1158{

1159 return &pkt->lladdr\_src;

1160}

1161

1162static inline struct [net\_linkaddr](structnet__linkaddr.md) \*net\_pkt\_lladdr\_dst(struct [net\_pkt](structnet__pkt.md) \*pkt)

1163{

1164 return &pkt->lladdr\_dst;

1165}

1166

1167static inline void net\_pkt\_lladdr\_swap(struct [net\_pkt](structnet__pkt.md) \*pkt)

1168{

1169 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0) = net\_pkt\_lladdr\_src(pkt)->addr;

1170

1171 net\_pkt\_lladdr\_src(pkt)->addr = net\_pkt\_lladdr\_dst(pkt)->addr;

1172 net\_pkt\_lladdr\_dst(pkt)->addr = [addr](structnet__linkaddr.md#a2176a9f7a444ac3b0108102d8cf852f0);

1173}

1174

1175static inline void net\_pkt\_lladdr\_clear(struct [net\_pkt](structnet__pkt.md) \*pkt)

1176{

1177 net\_pkt\_lladdr\_src(pkt)->addr = NULL;

1178 net\_pkt\_lladdr\_src(pkt)->len = 0U;

1179}

1180

1181static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_pkt\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt)

1182{

1183 return pkt->ll\_proto\_type;

1184}

1185

1186static inline void net\_pkt\_set\_ll\_proto\_type(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7))

1187{

1188 pkt->ll\_proto\_type = [type](structnet__linkaddr.md#a5f5b4c3d353261d0fab8011aa09f00d7);

1189}

1190

1191#if defined(CONFIG\_NET\_IPV4\_AUTO)

1192static inline bool net\_pkt\_ipv4\_auto(struct [net\_pkt](structnet__pkt.md) \*pkt)

1193{

1194 return !!(pkt->ipv4\_auto\_arp\_msg);

1195}

1196

1197static inline void net\_pkt\_set\_ipv4\_auto(struct [net\_pkt](structnet__pkt.md) \*pkt,

1198 bool is\_auto\_arp\_msg)

1199{

1200 pkt->ipv4\_auto\_arp\_msg = is\_auto\_arp\_msg;

1201}

1202#else /\* CONFIG\_NET\_IPV4\_AUTO \*/

1203static inline bool net\_pkt\_ipv4\_auto(struct [net\_pkt](structnet__pkt.md) \*pkt)

1204{

1205 ARG\_UNUSED(pkt);

1206

1207 return false;

1208}

1209

1210static inline void net\_pkt\_set\_ipv4\_auto(struct [net\_pkt](structnet__pkt.md) \*pkt,

1211 bool is\_auto\_arp\_msg)

1212{

1213 ARG\_UNUSED(pkt);

1214 ARG\_UNUSED(is\_auto\_arp\_msg);

1215}

1216#endif /\* CONFIG\_NET\_IPV4\_AUTO \*/

1217

1218#if defined(CONFIG\_NET\_LLDP)

1219static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1220{

1221 return !!(pkt->lldp\_pkt);

1222}

1223

1224static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1225{

1226 pkt->lldp\_pkt = is\_lldp;

1227}

1228#else

1229static inline bool net\_pkt\_is\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1230{

1231 ARG\_UNUSED(pkt);

1232

1233 return false;

1234}

1235

1236static inline void net\_pkt\_set\_lldp(struct [net\_pkt](structnet__pkt.md) \*pkt, bool is\_lldp)

1237{

1238 ARG\_UNUSED(pkt);

1239 ARG\_UNUSED(is\_lldp);

1240}

1241#endif /\* CONFIG\_NET\_LLDP \*/

1242

1243#if defined(CONFIG\_NET\_L2\_PPP)

1244static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1245{

1246 return !!(pkt->ppp\_msg);

1247}

1248

1249static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1250 bool is\_ppp\_msg)

1251{

1252 pkt->ppp\_msg = is\_ppp\_msg;

1253}

1254#else /\* CONFIG\_NET\_L2\_PPP \*/

1255static inline bool net\_pkt\_is\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt)

1256{

1257 ARG\_UNUSED(pkt);

1258

1259 return false;

1260}

1261

1262static inline void net\_pkt\_set\_ppp(struct [net\_pkt](structnet__pkt.md) \*pkt,

1263 bool is\_ppp\_msg)

1264{

1265 ARG\_UNUSED(pkt);

1266 ARG\_UNUSED(is\_ppp\_msg);

1267}

1268#endif /\* CONFIG\_NET\_L2\_PPP \*/

1269

1270#if defined(NET\_PKT\_HAS\_CONTROL\_BLOCK)

1271static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1272{

1273 return &pkt->cb;

1274}

1275#else

1276static inline void \*net\_pkt\_cb(struct [net\_pkt](structnet__pkt.md) \*pkt)

1277{

1278 ARG\_UNUSED(pkt);

1279

1280 return NULL;

1281}

1282#endif

1283

1284#define NET\_IPV6\_HDR(pkt) ((struct net\_ipv6\_hdr \*)net\_pkt\_ip\_data(pkt))

1285#define NET\_IPV4\_HDR(pkt) ((struct net\_ipv4\_hdr \*)net\_pkt\_ip\_data(pkt))

1286

1287static inline void net\_pkt\_set\_src\_ipv6\_addr(struct [net\_pkt](structnet__pkt.md) \*pkt)

1288{

1289 [net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)([net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)(

1290 net\_pkt\_context(pkt)),

1291 (struct [in6\_addr](structin6__addr.md) \*)NET\_IPV6\_HDR(pkt)->src);

1292}

1293

1294static inline void net\_pkt\_set\_overwrite(struct [net\_pkt](structnet__pkt.md) \*pkt, bool overwrite)

1295{

1296 pkt->overwrite = overwrite;

1297}

1298

1299static inline bool net\_pkt\_is\_being\_overwritten(struct [net\_pkt](structnet__pkt.md) \*pkt)

1300{

1301 return !!(pkt->overwrite);

1302}

1303

1304#ifdef CONFIG\_NET\_PKT\_FILTER

1305

1306bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1307bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1308

1309#else

1310

1311static inline bool net\_pkt\_filter\_send\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1312{

1313 ARG\_UNUSED(pkt);

1314

1315 return true;

1316}

1317

1318static inline bool net\_pkt\_filter\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1319{

1320 ARG\_UNUSED(pkt);

1321

1322 return true;

1323}

1324

1325#endif /\* CONFIG\_NET\_PKT\_FILTER \*/

1326

1327#if defined(CONFIG\_NET\_PKT\_FILTER) && \

1328 (defined(CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK) || defined(CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK))

1329

1330bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1331

1332#else

1333

1334static inline bool net\_pkt\_filter\_ip\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1335{

1336 ARG\_UNUSED(pkt);

1337

1338 return true;

1339}

1340

1341#endif /\* CONFIG\_NET\_PKT\_FILTER\_IPV4\_HOOK || CONFIG\_NET\_PKT\_FILTER\_IPV6\_HOOK \*/

1342

1343#if defined(CONFIG\_NET\_PKT\_FILTER) && defined(CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK)

1344

1345bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt);

1346

1347#else

1348

1349static inline bool net\_pkt\_filter\_local\_in\_recv\_ok(struct [net\_pkt](structnet__pkt.md) \*pkt)

1350{

1351 ARG\_UNUSED(pkt);

1352

1353 return true;

1354}

1355

1356#endif /\* CONFIG\_NET\_PKT\_FILTER && CONFIG\_NET\_PKT\_FILTER\_LOCAL\_IN\_HOOK \*/

1357

1358/\* @endcond \*/

1359

[ 1373](group__net__pkt.md#gafc7e98d5b64d816faabcbaa2ec22a2bb)#define NET\_PKT\_SLAB\_DEFINE(name, count) \

1374 K\_MEM\_SLAB\_DEFINE(name, sizeof(struct net\_pkt), count, 4)

1375

1376/\* Backward compatibility macro \*/

[ 1377](group__net__pkt.md#gacb3bb7347aa5dccb902531a1d6fbd190)#define NET\_PKT\_TX\_SLAB\_DEFINE(name, count) NET\_PKT\_SLAB\_DEFINE(name, count)

1378

[ 1392](group__net__pkt.md#ga94ab6300b59d739c4e3c5604d3fbe8a5)#define NET\_PKT\_DATA\_POOL\_DEFINE(name, count) \

1393 NET\_BUF\_POOL\_DEFINE(name, count, CONFIG\_NET\_BUF\_DATA\_SIZE, \

1394 0, NULL)

1395

1397

1398#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC) || \

1399 (CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG)

1400#define NET\_PKT\_DEBUG\_ENABLED

1401#endif

1402

1403#if defined(NET\_PKT\_DEBUG\_ENABLED)

1404

1405/\* Debug versions of the net\_pkt functions that are used when tracking

1406 \* buffer usage.

1407 \*/

1408

1409struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_data\_debug(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool,

1410 size\_t min\_len,

1411 [k\_timeout\_t](structk__timeout__t.md) timeout,

1412 const char \*caller,

1413 int line);

1414

1415#define net\_pkt\_get\_reserve\_data(pool, min\_len, timeout) \

1416 net\_pkt\_get\_reserve\_data\_debug(pool, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1417

1418struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_rx\_data\_debug(size\_t min\_len,

1419 [k\_timeout\_t](structk__timeout__t.md) timeout,

1420 const char \*caller,

1421 int line);

1422#define net\_pkt\_get\_reserve\_rx\_data(min\_len, timeout) \

1423 net\_pkt\_get\_reserve\_rx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1424

1425struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_reserve\_tx\_data\_debug(size\_t min\_len,

1426 [k\_timeout\_t](structk__timeout__t.md) timeout,

1427 const char \*caller,

1428 int line);

1429#define net\_pkt\_get\_reserve\_tx\_data(min\_len, timeout) \

1430 net\_pkt\_get\_reserve\_tx\_data\_debug(min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1431

1432struct [net\_buf](structnet__buf.md) \*net\_pkt\_get\_frag\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1433 [k\_timeout\_t](structk__timeout__t.md) timeout,

1434 const char \*caller, int line);

1435#define net\_pkt\_get\_frag(pkt, min\_len, timeout) \

1436 net\_pkt\_get\_frag\_debug(pkt, min\_len, timeout, \_\_func\_\_, \_\_LINE\_\_)

1437

1438void net\_pkt\_unref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller, int line);

1439#define net\_pkt\_unref(pkt) net\_pkt\_unref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1440

1441struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_ref\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, const char \*caller,

1442 int line);

1443#define net\_pkt\_ref(pkt) net\_pkt\_ref\_debug(pkt, \_\_func\_\_, \_\_LINE\_\_)

1444

1445struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_ref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1446 const char \*caller, int line);

1447#define net\_pkt\_frag\_ref(frag) net\_pkt\_frag\_ref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1448

1449void net\_pkt\_frag\_unref\_debug(struct [net\_buf](structnet__buf.md) \*frag,

1450 const char \*caller, int line);

1451#define net\_pkt\_frag\_unref(frag) \

1452 net\_pkt\_frag\_unref\_debug(frag, \_\_func\_\_, \_\_LINE\_\_)

1453

1454struct [net\_buf](structnet__buf.md) \*net\_pkt\_frag\_del\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1455 struct [net\_buf](structnet__buf.md) \*parent,

1456 struct [net\_buf](structnet__buf.md) \*frag,

1457 const char \*caller, int line);

1458#define net\_pkt\_frag\_del(pkt, parent, frag) \

1459 net\_pkt\_frag\_del\_debug(pkt, parent, frag, \_\_func\_\_, \_\_LINE\_\_)

1460

1461void net\_pkt\_frag\_add\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1462 const char \*caller, int line);

1463#define net\_pkt\_frag\_add(pkt, frag) \

1464 net\_pkt\_frag\_add\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1465

1466void net\_pkt\_frag\_insert\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag,

1467 const char \*caller, int line);

1468#define net\_pkt\_frag\_insert(pkt, frag) \

1469 net\_pkt\_frag\_insert\_debug(pkt, frag, \_\_func\_\_, \_\_LINE\_\_)

1470#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC ||

1471 \* CONFIG\_NET\_PKT\_LOG\_LEVEL >= LOG\_LEVEL\_DBG

1472 \*/

1474

1482#if defined(NET\_PKT\_DEBUG\_ENABLED)

1483void [net\_pkt\_print\_frags](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1484#else

[ 1485](group__net__pkt.md#ga2b2d0900ae76674d418918ec955bad48)#define net\_pkt\_print\_frags(pkt)

1486#endif

1487

1502#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1503](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1504#endif

1505

1520#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1521](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_reserve\_tx\_data](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)(size\_t min\_len, [k\_timeout\_t](structk__timeout__t.md) timeout);

1522#endif

1523

1536#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1537](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_get\_frag](group__net__pkt.md#gafa7d666bddb182149d5f540880c46b4e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t min\_len,

1538 [k\_timeout\_t](structk__timeout__t.md) timeout);

1539#endif

1540

1550#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1551](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)void [net\_pkt\_unref](group__net__pkt.md#ga893d1660fd18ad5842224fda78466099)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1552#endif

1553

1563#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1564](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_ref](group__net__pkt.md#ga4e83d4f60b46db8f57798c0e96d6cd7a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1565#endif

1566

1576#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1577](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_ref](group__net__pkt.md#gaea5e1045d188b3abbd85717ff09d563a)(struct [net\_buf](structnet__buf.md) \*frag);

1578#endif

1579

1585#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1586](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)void [net\_pkt\_frag\_unref](group__net__pkt.md#ga5c75ef2149d2ba5ff07525988e0fb7cc)(struct [net\_buf](structnet__buf.md) \*frag);

1587#endif

1588

1599#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1600](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)struct [net\_buf](structnet__buf.md) \*[net\_pkt\_frag\_del](group__net__pkt.md#ga956c784f5417f0f79976c6e106ad0d76)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1601 struct [net\_buf](structnet__buf.md) \*parent,

1602 struct [net\_buf](structnet__buf.md) \*frag);

1603#endif

1604

1611#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1612](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)void [net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1613#endif

1614

1621#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1622](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)void [net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*frag);

1623#endif

1624

[ 1631](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)void [net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1632

[ 1641](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)void [net\_pkt\_get\_info](group__net__pkt.md#ga7b02b95838b928febfd4970de5e9c9f9)(struct k\_mem\_slab \*\*rx,

1642 struct k\_mem\_slab \*\*tx,

1643 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*rx\_data,

1644 struct [net\_buf\_pool](structnet__buf__pool.md) \*\*tx\_data);

1645

1647

1648#if defined(CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC)

1652void net\_pkt\_print(void);

1653

1654typedef void (\*net\_pkt\_allocs\_cb\_t)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1655 struct [net\_buf](structnet__buf.md) \*buf,

1656 const char \*func\_alloc,

1657 int line\_alloc,

1658 const char \*func\_free,

1659 int line\_free,

1660 bool in\_use,

1661 void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1662

1663void net\_pkt\_allocs\_foreach(net\_pkt\_allocs\_cb\_t cb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

1664

1665const char \*net\_pkt\_slab2str(struct k\_mem\_slab \*slab);

1666const char \*net\_pkt\_pool2str(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool);

1667

1668#else

1669#define net\_pkt\_print(...)

1670#endif /\* CONFIG\_NET\_DEBUG\_NET\_PKT\_ALLOC \*/

1671

1672/\* New allocator, and API are defined below.

1673 \* This will be simpler when time will come to get rid of former API above.

1674 \*/

1675#if defined(NET\_PKT\_DEBUG\_ENABLED)

1676

1677struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1678 const char \*caller, int line);

1679#define net\_pkt\_alloc(\_timeout) \

1680 net\_pkt\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1681

1682struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_from\_slab\_debug(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1683 [k\_timeout\_t](structk__timeout__t.md) timeout,

1684 const char \*caller, int line);

1685#define net\_pkt\_alloc\_from\_slab(\_slab, \_timeout) \

1686 net\_pkt\_alloc\_from\_slab\_debug(\_slab, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1687

1688struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_debug([k\_timeout\_t](structk__timeout__t.md) timeout,

1689 const char \*caller, int line);

1690#define net\_pkt\_rx\_alloc(\_timeout) \

1691 net\_pkt\_rx\_alloc\_debug(\_timeout, \_\_func\_\_, \_\_LINE\_\_)

1692

1693struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1694 [k\_timeout\_t](structk__timeout__t.md) timeout,

1695 const char \*caller,

1696 int line);

1697#define net\_pkt\_alloc\_on\_iface(\_iface, \_timeout) \

1698 net\_pkt\_alloc\_on\_iface\_debug(\_iface, \_timeout, \_\_func\_\_, \_\_LINE\_\_)

1699

1700struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_on\_iface\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1701 [k\_timeout\_t](structk__timeout__t.md) timeout,

1702 const char \*caller,

1703 int line);

1704#define net\_pkt\_rx\_alloc\_on\_iface(\_iface, \_timeout) \

1705 net\_pkt\_rx\_alloc\_on\_iface\_debug(\_iface, \_timeout, \

1706 \_\_func\_\_, \_\_LINE\_\_)

1707

1708int net\_pkt\_alloc\_buffer\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt,

1709 size\_t size,

1710 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1711 [k\_timeout\_t](structk__timeout__t.md) timeout,

1712 const char \*caller, int line);

1713#define net\_pkt\_alloc\_buffer(\_pkt, \_size, \_proto, \_timeout) \

1714 net\_pkt\_alloc\_buffer\_debug(\_pkt, \_size, \_proto, \_timeout, \

1715 \_\_func\_\_, \_\_LINE\_\_)

1716

1717int net\_pkt\_alloc\_buffer\_raw\_debug(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

1718 [k\_timeout\_t](structk__timeout__t.md) timeout,

1719 const char \*caller, int line);

1720#define net\_pkt\_alloc\_buffer\_raw(\_pkt, \_size, \_timeout) \

1721 net\_pkt\_alloc\_buffer\_raw\_debug(\_pkt, \_size, \_timeout, \

1722 \_\_func\_\_, \_\_LINE\_\_)

1723

1724struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1725 size\_t size,

1726 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1727 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1728 [k\_timeout\_t](structk__timeout__t.md) timeout,

1729 const char \*caller,

1730 int line);

1731#define net\_pkt\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1732 \_proto, \_timeout) \

1733 net\_pkt\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1734 \_proto, \_timeout, \

1735 \_\_func\_\_, \_\_LINE\_\_)

1736

1737struct [net\_pkt](structnet__pkt.md) \*net\_pkt\_rx\_alloc\_with\_buffer\_debug(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1738 size\_t size,

1739 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1740 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1741 [k\_timeout\_t](structk__timeout__t.md) timeout,

1742 const char \*caller,

1743 int line);

1744#define net\_pkt\_rx\_alloc\_with\_buffer(\_iface, \_size, \_family, \

1745 \_proto, \_timeout) \

1746 net\_pkt\_rx\_alloc\_with\_buffer\_debug(\_iface, \_size, \_family, \

1747 \_proto, \_timeout, \

1748 \_\_func\_\_, \_\_LINE\_\_)

1749#endif /\* NET\_PKT\_DEBUG\_ENABLED \*/

1751

1762#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1763](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc](group__net__pkt.md#ga90d97ba913a875b3ee438e0ea8a970fd)([k\_timeout\_t](structk__timeout__t.md) timeout);

1764#endif

1765

1780#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1781](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_from\_slab](group__net__pkt.md#gaf1edbaab59576262647089fa1751d9e3)(struct k\_mem\_slab \*[slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54),

1782 [k\_timeout\_t](structk__timeout__t.md) timeout);

1783#endif

1784

1795#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1796](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_alloc](group__net__pkt.md#ga4cec027a0de4807879fd3bd3aed4f12a)([k\_timeout\_t](structk__timeout__t.md) timeout);

1797#endif

1798

1807#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1808](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_on\_iface](group__net__pkt.md#ga770ffe22fc797691b1fc89954d60b2e6)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1809 [k\_timeout\_t](structk__timeout__t.md) timeout);

1810

1811/\* Same as above but specifically for RX packet \*/

[ 1812](group__net__pkt.md#gab64f7551b1995c301232ab4cd39b9efc)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_alloc\_on\_iface](group__net__pkt.md#gab64f7551b1995c301232ab4cd39b9efc)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1813 [k\_timeout\_t](structk__timeout__t.md) timeout);

1814#endif

1815

1831#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1832](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)int [net\_pkt\_alloc\_buffer](group__net__pkt.md#gae31b4afd510bce346f7d00a9ec5d190d)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1833 size\_t size,

1834 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1835 [k\_timeout\_t](structk__timeout__t.md) timeout);

1836#endif

1837

1851#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1852](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)int [net\_pkt\_alloc\_buffer\_raw](group__net__pkt.md#ga53819889ad86bc2c43407f12f113bb94)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size,

1853 [k\_timeout\_t](structk__timeout__t.md) timeout);

1854#endif

1855

1867#if !defined(NET\_PKT\_DEBUG\_ENABLED)

[ 1868](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_alloc\_with\_buffer](group__net__pkt.md#ga57e2f5138acd92ad49864e3d709d9419)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1869 size\_t size,

1870 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1871 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1872 [k\_timeout\_t](structk__timeout__t.md) timeout);

1873

1874/\* Same as above but specifically for RX packet \*/

[ 1875](group__net__pkt.md#ga623794964a35e0e24c1f41a75bfba626)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_alloc\_with\_buffer](group__net__pkt.md#ga623794964a35e0e24c1f41a75bfba626)(struct [net\_if](structnet__if.md) \*[iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2),

1876 size\_t size,

1877 [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family,

1878 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto,

1879 [k\_timeout\_t](structk__timeout__t.md) timeout);

1880#endif

1881

[ 1888](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)void [net\_pkt\_append\_buffer](group__net__pkt.md#ga2b11492ae3c16368aa6a0ab8f47b67e7)(struct [net\_pkt](structnet__pkt.md) \*pkt, struct [net\_buf](structnet__buf.md) \*[buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b));

1889

[ 1900](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)size\_t [net\_pkt\_available\_buffer](group__net__pkt.md#gaeed119d192e3a14ea3eea6e623334519)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1901

[ 1917](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)size\_t [net\_pkt\_available\_payload\_buffer](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1918 enum [net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31) proto);

1919

[ 1928](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)void [net\_pkt\_trim\_buffer](group__net__pkt.md#ga71d1c49f68afab07324cebd835f08a29)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1929

[ 1944](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)int [net\_pkt\_remove\_tail](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

1945

[ 1953](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)void [net\_pkt\_cursor\_init](group__net__pkt.md#ga1b7da39f62dfc8b8948d7689e2dd114a)(struct [net\_pkt](structnet__pkt.md) \*pkt);

1954

[ 1961](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)static inline void [net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1962 struct [net\_pkt\_cursor](structnet__pkt__cursor.md) \*backup)

1963{

1964 backup->[buf](structnet__pkt__cursor.md#af81267720cf13d06b90ddaa87fb7ad67) = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).[buf](structnet__pkt__cursor.md#af81267720cf13d06b90ddaa87fb7ad67);

1965 backup->[pos](structnet__pkt__cursor.md#a0901a4cc727e55b94e2dcb60f3c54caf) = pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).[pos](structnet__pkt__cursor.md#a0901a4cc727e55b94e2dcb60f3c54caf);

1966}

1967

[ 1974](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)static inline void [net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)(struct [net\_pkt](structnet__pkt.md) \*pkt,

1975 struct [net\_pkt\_cursor](structnet__pkt__cursor.md) \*backup)

1976{

1977 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).[buf](structnet__pkt__cursor.md#af81267720cf13d06b90ddaa87fb7ad67) = backup->[buf](structnet__pkt__cursor.md#af81267720cf13d06b90ddaa87fb7ad67);

1978 pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).[pos](structnet__pkt__cursor.md#a0901a4cc727e55b94e2dcb60f3c54caf) = backup->[pos](structnet__pkt__cursor.md#a0901a4cc727e55b94e2dcb60f3c54caf);

1979}

1980

[ 1988](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)static inline void \*[net\_pkt\_cursor\_get\_pos](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)(struct [net\_pkt](structnet__pkt.md) \*pkt)

1989{

1990 return pkt->[cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06).[pos](structnet__pkt__cursor.md#a0901a4cc727e55b94e2dcb60f3c54caf);

1991}

1992

[ 2013](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)int [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2014

[ 2029](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)int [net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)(struct [net\_pkt](structnet__pkt.md) \*pkt, int byte, size\_t length);

2030

[ 2044](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)int [net\_pkt\_copy](group__net__pkt.md#ga4648828ca353c8c0ecf00ae2648e963a)(struct [net\_pkt](structnet__pkt.md) \*pkt\_dst,

2045 struct [net\_pkt](structnet__pkt.md) \*pkt\_src,

2046 size\_t length);

2047

[ 2057](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_clone](group__net__pkt.md#gaefefe50d0c68fb4997abc7b309740959)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2058

[ 2068](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_rx\_clone](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)(struct [net\_pkt](structnet__pkt.md) \*pkt, [k\_timeout\_t](structk__timeout__t.md) timeout);

2069

[ 2078](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)struct [net\_pkt](structnet__pkt.md) \*[net\_pkt\_shallow\_clone](group__net__pkt.md#ga26ae9d1286cb98d255f1bfb65201f1e2)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2079 [k\_timeout\_t](structk__timeout__t.md) timeout);

2080

[ 2094](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)int [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(struct [net\_pkt](structnet__pkt.md) \*pkt, void \*data, size\_t length);

2095

2096/\* Read uint8\_t data data a net\_pkt \*/

[ 2097](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)static inline int [net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

2098{

2099 return [net\_pkt\_read](group__net__pkt.md#ga914be010ddd225a4fc2d6ab521ee7b64)(pkt, data, 1);

2100}

2101

[ 2114](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)int [net\_pkt\_read\_be16](group__net__pkt.md#ga500a318977cfecd4ec7c60cea01db2fc)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2115

[ 2128](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)int [net\_pkt\_read\_le16](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

2129

[ 2142](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)int [net\_pkt\_read\_be32](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

2143

[ 2157](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)int [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(struct [net\_pkt](structnet__pkt.md) \*pkt, const void \*data, size\_t length);

2158

2159/\* Write uint8\_t data into a net\_pkt. \*/

[ 2160](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)static inline int [net\_pkt\_write\_u8](group__net__pkt.md#gaa5129f661075c13d9b59627ae9110bd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data)

2161{

2162 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data, sizeof([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)));

2163}

2164

2165/\* Write uint16\_t big endian data into a net\_pkt. \*/

[ 2166](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)static inline int [net\_pkt\_write\_be16](group__net__pkt.md#ga8e5083388ccb0333fdcf745bc60ad260)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2167{

2168 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_be16 = [htons](group__ip__4__6.md#ga51799f5ebb4c7228ef7e95c247030f42)(data);

2169

2170 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2171}

2172

2173/\* Write uint32\_t big endian data into a net\_pkt. \*/

[ 2174](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)static inline int [net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2175{

2176 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_be32 = [htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)(data);

2177

2178 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_be32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2179}

2180

2181/\* Write uint32\_t little endian data into a net\_pkt. \*/

[ 2182](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)static inline int [net\_pkt\_write\_le32](group__net__pkt.md#gaf2388032e4e0b76fe32e4618ef3ea548)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

2183{

2184 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_le32 = [sys\_cpu\_to\_le32](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)(data);

2185

2186 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le32, sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)));

2187}

2188

2189/\* Write uint16\_t little endian data into a net\_pkt. \*/

[ 2190](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)static inline int [net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)(struct [net\_pkt](structnet__pkt.md) \*pkt, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

2191{

2192 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_le16 = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)(data);

2193

2194 return [net\_pkt\_write](group__net__pkt.md#gae99eadd977b7f66ecc91d2ccba34c6fa)(pkt, &data\_le16, sizeof([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)));

2195}

2196

[ 2204](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)size\_t [net\_pkt\_remaining\_data](group__net__pkt.md#gadee5307216b6b3b725a2fd7584a224c9)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2205

[ 2218](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)int [net\_pkt\_update\_length](group__net__pkt.md#ga2e7a0f9348a623c5160124da188445ee)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2219

[ 2232](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)int [net\_pkt\_pull](group__net__pkt.md#ga434c347a32600ee113c0e1cc13f70cd4)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t length);

2233

[ 2242](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_pkt\_get\_current\_offset](group__net__pkt.md#gadb3b705a0431b3bb98fb2e8193c3b510)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2243

[ 2255](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)bool [net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)(struct [net\_pkt](structnet__pkt.md) \*pkt, size\_t size);

2256

[ 2265](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)size\_t [net\_pkt\_get\_contiguous\_len](group__net__pkt.md#gafbd6c0ab33139b134f67a8f8c0096445)(struct [net\_pkt](structnet__pkt.md) \*pkt);

2266

[ 2267](structnet__pkt__data__access.md)struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) {

2268#if !defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

[ 2269](structnet__pkt__data__access.md#ae65969f19c334bc998fafc72ef20e95f) void \*[data](structnet__pkt__data__access.md#ae65969f19c334bc998fafc72ef20e95f);

2270#endif

[ 2271](structnet__pkt__data__access.md#a8638004d4629eff48f85f61900c04034) const size\_t [size](structnet__pkt__data__access.md#a8638004d4629eff48f85f61900c04034);

2272};

2273

2274#if defined(CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS)

2275#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2276 struct net\_pkt\_data\_access \_name = { \

2277 .size = sizeof(\_type), \

2278 }

2279

2280#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2281 NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type)

2282

2283#else

[ 2284](group__net__pkt.md#gafd11f2d4f773bf247296eb08b7006c27)#define NET\_PKT\_DATA\_ACCESS\_DEFINE(\_name, \_type) \

2285 \_type \_hdr\_##\_name; \

2286 struct net\_pkt\_data\_access \_name = { \

2287 .data = &\_hdr\_##\_name, \

2288 .size = sizeof(\_type), \

2289 }

2290

[ 2291](group__net__pkt.md#gaa6a48974656755dcc0979683b8431c37)#define NET\_PKT\_DATA\_ACCESS\_CONTIGUOUS\_DEFINE(\_name, \_type) \

2292 struct net\_pkt\_data\_access \_name = { \

2293 .data = NULL, \

2294 .size = sizeof(\_type), \

2295 }

2296

2297#endif /\* CONFIG\_NET\_HEADERS\_ALWAYS\_CONTIGUOUS \*/

2298

[ 2312](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)void \*[net\_pkt\_get\_data](group__net__pkt.md#gaa00da4276fd4a01faf80a92796f78e70)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2313 struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \*access);

2314

[ 2328](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)int [net\_pkt\_set\_data](group__net__pkt.md#ga98df84477b35e203b11029fc4ddec1cc)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2329 struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \*access);

2330

[ 2335](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)static inline int [net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)(struct [net\_pkt](structnet__pkt.md) \*pkt,

2336 struct [net\_pkt\_data\_access](structnet__pkt__data__access.md) \*access)

2337{

2338 return [net\_pkt\_skip](group__net__pkt.md#ga223a79baa1e740a53c4ed0f083d62185)(pkt, access->[size](structnet__pkt__data__access.md#a8638004d4629eff48f85f61900c04034));

2339}

2340

2344

2345#ifdef \_\_cplusplus

2346}

2347#endif

2348

2349#endif /\* ZEPHYR\_INCLUDE\_NET\_NET\_PKT\_H\_ \*/

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

[htonl](group__ip__4__6.md#gae4027a6ad07f13aa12eab285a1b46019)

#define htonl(x)

Convert 32-bit value from host to network byte order.

**Definition** net\_ip.h:128

[net\_ip\_protocol](group__ip__4__6.md#gaf06819bf427cc58be1229b27b373ca31)

net\_ip\_protocol

Protocol numbers from IANA/BSD.

**Definition** net\_ip.h:62

[net\_buf\_frags\_len](group__net__buf.md#gaea38d8a418b739fa335e30ed91d9943d)

static size\_t net\_buf\_frags\_len(struct net\_buf \*buf)

Calculate amount of bytes stored in fragments.

**Definition** buf.h:2471

[net\_context\_get\_iface](group__net__context.md#gafe6b8c9af4464cd471285817d6d61087)

static struct net\_if \* net\_context\_get\_iface(struct net\_context \*context)

Get network interface for this context.

**Definition** net\_context.h:690

[net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872)

static struct net\_linkaddr \* net\_if\_get\_link\_addr(struct net\_if \*iface)

Get an network interface's link address.

**Definition** net\_if.h:991

[net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438)

static const struct in6\_addr \* net\_if\_ipv6\_select\_src\_addr(struct net\_if \*iface, const struct in6\_addr \*dst)

Get a IPv6 source address that should be used when sending network data to destination.

**Definition** net\_if.h:1836

[net\_pkt\_frag\_add](group__net__pkt.md#ga03a53365cfc2b6c3448763d81f56c2c0)

void net\_pkt\_frag\_add(struct net\_pkt \*pkt, struct net\_buf \*frag)

Add a fragment to a packet at the end of its fragment list.

[net\_pkt\_write\_be32](group__net__pkt.md#ga053aff4ff0a501f336132c35b7fb2022)

static int net\_pkt\_write\_be32(struct net\_pkt \*pkt, uint32\_t data)

**Definition** net\_pkt.h:2174

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

**Definition** net\_pkt.h:1485

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

[net\_pkt\_rx\_alloc\_with\_buffer](group__net__pkt.md#ga623794964a35e0e24c1f41a75bfba626)

struct net\_pkt \* net\_pkt\_rx\_alloc\_with\_buffer(struct net\_if \*iface, size\_t size, sa\_family\_t family, enum net\_ip\_protocol proto, k\_timeout\_t timeout)

[net\_pkt\_rx\_clone](group__net__pkt.md#ga66aec729118e4d927c921b872df82dda)

struct net\_pkt \* net\_pkt\_rx\_clone(struct net\_pkt \*pkt, k\_timeout\_t timeout)

Clone pkt and its buffer.

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

**Definition** net\_pkt.h:2166

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

**Definition** net\_pkt.h:2160

[net\_pkt\_available\_payload\_buffer](group__net__pkt.md#gaa9f63047b7945a4a155e5d88eac5203b)

size\_t net\_pkt\_available\_payload\_buffer(struct net\_pkt \*pkt, enum net\_ip\_protocol proto)

Get available buffer space for payload from a pkt.

[net\_pkt\_read\_le16](group__net__pkt.md#gab1735ef4f6a2e538a2692358295dd8d1)

int net\_pkt\_read\_le16(struct net\_pkt \*pkt, uint16\_t \*data)

Read uint16\_t little endian data from a net\_pkt.

[net\_pkt\_read\_be32](group__net__pkt.md#gab38c99947d02982073df65c0d5893d2c)

int net\_pkt\_read\_be32(struct net\_pkt \*pkt, uint32\_t \*data)

Read uint32\_t big endian data from a net\_pkt.

[net\_pkt\_rx\_alloc\_on\_iface](group__net__pkt.md#gab64f7551b1995c301232ab4cd39b9efc)

struct net\_pkt \* net\_pkt\_rx\_alloc\_on\_iface(struct net\_if \*iface, k\_timeout\_t timeout)

[net\_pkt\_remove\_tail](group__net__pkt.md#gab657c80669733a4afefaf1be6310107e)

int net\_pkt\_remove\_tail(struct net\_pkt \*pkt, size\_t length)

Remove length bytes from tail of packet.

[net\_pkt\_get\_reserve\_tx\_data](group__net__pkt.md#gaba26ee929f154978afbd007f7f2b0bc9)

struct net\_buf \* net\_pkt\_get\_reserve\_tx\_data(size\_t min\_len, k\_timeout\_t timeout)

Get TX DATA buffer from pool.

[net\_pkt\_cursor\_get\_pos](group__net__pkt.md#gabc42ba1bcd0801a116651d965e65b9cd)

static void \* net\_pkt\_cursor\_get\_pos(struct net\_pkt \*pkt)

Returns current position of the cursor.

**Definition** net\_pkt.h:1988

[net\_pkt\_frag\_insert](group__net__pkt.md#gabcd375d9dbdca21855abe27d7b5a0a7e)

void net\_pkt\_frag\_insert(struct net\_pkt \*pkt, struct net\_buf \*frag)

Insert a fragment to a packet at the beginning of its fragment list.

[net\_pkt\_memset](group__net__pkt.md#gabd241a539bf1290f3d45610fd15b2c1f)

int net\_pkt\_memset(struct net\_pkt \*pkt, int byte, size\_t length)

Memset some data in a net\_pkt.

[net\_pkt\_cursor\_backup](group__net__pkt.md#gabd352b66cdeaff2fb45361a0fae62876)

static void net\_pkt\_cursor\_backup(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Backup net\_pkt cursor.

**Definition** net\_pkt.h:1961

[net\_pkt\_compact](group__net__pkt.md#gabf85446fb8000574b180d00c5db65a44)

void net\_pkt\_compact(struct net\_pkt \*pkt)

Compact the fragment list of a packet.

[net\_pkt\_acknowledge\_data](group__net__pkt.md#gac7226cbfa2da28408f9691d375bc8f9f)

static int net\_pkt\_acknowledge\_data(struct net\_pkt \*pkt, struct net\_pkt\_data\_access \*access)

Acknowledge previously contiguous data taken from a network packet Packet needs to be set to overwrit...

**Definition** net\_pkt.h:2335

[net\_pkt\_write\_le16](group__net__pkt.md#gac8a6ea1b0dc1bcd7b6a3f15869027dd1)

static int net\_pkt\_write\_le16(struct net\_pkt \*pkt, uint16\_t data)

**Definition** net\_pkt.h:2190

[net\_pkt\_cursor\_restore](group__net__pkt.md#gad5ab788f01b4bb3640755e8c4a2c612e)

static void net\_pkt\_cursor\_restore(struct net\_pkt \*pkt, struct net\_pkt\_cursor \*backup)

Restore net\_pkt cursor from a backup.

**Definition** net\_pkt.h:1974

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

**Definition** net\_pkt.h:2182

[net\_pkt\_get\_reserve\_rx\_data](group__net__pkt.md#gaf48f4aac4d16a367d46ca76bf038a485)

struct net\_buf \* net\_pkt\_get\_reserve\_rx\_data(size\_t min\_len, k\_timeout\_t timeout)

Get RX DATA buffer from pool.

[net\_pkt\_is\_contiguous](group__net__pkt.md#gaf4ee5a8903b495e000a3a4c8a8493160)

bool net\_pkt\_is\_contiguous(struct net\_pkt \*pkt, size\_t size)

Check if a data size could fit contiguously.

[net\_pkt\_read\_u8](group__net__pkt.md#gaf9b2753cb514804a77d9494c9f070089)

static int net\_pkt\_read\_u8(struct net\_pkt \*pkt, uint8\_t \*data)

**Definition** net\_pkt.h:2097

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

**Definition** ptp\_time.h:193

[ns\_to\_net\_ptp\_time](group__ptp__time.md#gafd9d45cca3d630ce51109537165d53df)

static struct net\_ptp\_time ns\_to\_net\_ptp\_time(net\_time\_t nsec)

Convert a nanosecond precision timestamp to a PTP timestamp, both related to the local network refere...

**Definition** ptp\_time.h:214

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

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:976

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** buf.h:936

[net\_buf::user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7)

uint8\_t user\_data[]

System metadata for this buffer.

**Definition** buf.h:955

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:939

[net\_context](structnet__context.md)

Note that we do not store the actual source IP address in the context because the address is already ...

**Definition** net\_context.h:201

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:615

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

[net\_pkt\_cursor](structnet__pkt__cursor.md)

**Definition** net\_pkt.h:50

[net\_pkt\_cursor::pos](structnet__pkt__cursor.md#a0901a4cc727e55b94e2dcb60f3c54caf)

uint8\_t \* pos

Current position in the data buffer of the net\_buf.

**Definition** net\_pkt.h:54

[net\_pkt\_cursor::buf](structnet__pkt__cursor.md#af81267720cf13d06b90ddaa87fb7ad67)

struct net\_buf \* buf

Current net\_buf pointer by the cursor.

**Definition** net\_pkt.h:52

[net\_pkt\_data\_access](structnet__pkt__data__access.md)

**Definition** net\_pkt.h:2267

[net\_pkt\_data\_access::size](structnet__pkt__data__access.md#a8638004d4629eff48f85f61900c04034)

const size\_t size

**Definition** net\_pkt.h:2271

[net\_pkt\_data\_access::data](structnet__pkt__data__access.md#ae65969f19c334bc998fafc72ef20e95f)

void \* data

**Definition** net\_pkt.h:2269

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:63

[net\_pkt::frags](structnet__pkt.md#a1c27e50656b8c2713704d979b902c5d6)

struct net\_buf \* frags

**Definition** net\_pkt.h:75

[net\_pkt::context](structnet__pkt.md#a4b9c3f62209f4d7748070224654360cf)

struct net\_context \* context

Network connection context.

**Definition** net\_pkt.h:83

[net\_pkt::cursor](structnet__pkt.md#a52f155a86698a929fa2130b594630d06)

struct net\_pkt\_cursor cursor

Internal buffer iterator used for reading/writing.

**Definition** net\_pkt.h:80

[net\_pkt::iface](structnet__pkt.md#a7590eeacf06469206cb7e7949acfa7b2)

struct net\_if \* iface

Network interface.

**Definition** net\_pkt.h:86

[net\_pkt::fifo](structnet__pkt.md#a96e82461f6786814de708049f2bc0b22)

intptr\_t fifo

The fifo is used by RX/TX threads and by socket layer.

**Definition** net\_pkt.h:68

[net\_pkt::buffer](structnet__pkt.md#ad319458430aa691b88e24776e843d30b)

struct net\_buf \* buffer

**Definition** net\_pkt.h:76

[net\_pkt::slab](structnet__pkt.md#add4540bddb5c549a5ae61b99b14b0b54)

struct k\_mem\_slab \* slab

Slab pointer from where it belongs to.

**Definition** net\_pkt.h:71

[net\_ptp\_time](structnet__ptp__time.md)

(Generalized) Precision Time Protocol Timestamp format.

**Definition** ptp\_time.h:109

[net\_ptp\_time::nanosecond](structnet__ptp__time.md#a31af3f0b8f924336c17585ee1b15ee0e)

uint32\_t nanosecond

Nanoseconds.

**Definition** ptp\_time.h:127

[net\_ptp\_time::second](structnet__ptp__time.md#a8d61359ca53147d2da761edeb9e1ab04)

uint64\_t second

**Definition** ptp\_time.h:123

[stat](structstat.md)

**Definition** stat.h:92

[sys\_cpu\_to\_le32](sys_2byteorder_8h.md#a8cdffcb0ce27f2871e1f1d05dcc31b7b)

#define sys\_cpu\_to\_le32(val)

Convert 32-bit integer from host endianness to little-endian.

**Definition** byteorder.h:261

[sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)

#define sys\_cpu\_to\_le16(val)

Convert 16-bit integer from host endianness to little-endian.

**Definition** byteorder.h:257

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_pkt.h](net__pkt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
