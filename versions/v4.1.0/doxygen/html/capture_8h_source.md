---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/capture_8h_source.html
original_path: doxygen/html/capture_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

capture.h

[Go to the documentation of this file.](capture_8h.md)

1

6

7/\*

8 \* Copyright (c) 2021 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_CAPTURE\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_CAPTURE\_H\_

15

16#include <[zephyr/kernel.h](kernel_8h.md)>

17#include <[zephyr/device.h](device_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

31

33

34struct [net\_if](structnet__if.md);

35struct [net\_pkt](structnet__pkt.md);

36struct [device](structdevice.md);

37

38struct net\_capture\_interface\_api {

42 int (\*cleanup)(const struct device \*dev);

43

45 int (\*enable)(const struct device \*dev, struct net\_if \*iface);

46

48 int (\*disable)(const struct device \*dev);

49

52 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*is\_enabled)(const struct device \*dev);

53

55 int (\*[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f))(const struct device \*dev, struct net\_if \*iface, struct net\_pkt \*pkt);

56};

57

59

[ 75](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)int [net\_capture\_setup](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)(const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr,

76 const struct [device](structdevice.md) \*\*dev);

77

[ 89](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)static inline int [net\_capture\_cleanup](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)(const struct [device](structdevice.md) \*dev)

90{

91#if defined(CONFIG\_NET\_CAPTURE)

92 const struct net\_capture\_interface\_api \*api =

93 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

94

95 return api->cleanup(dev);

96#else

97 ARG\_UNUSED(dev);

98

99 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

100#endif

101}

102

[ 115](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)static inline int [net\_capture\_enable](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)(const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface)

116{

117#if defined(CONFIG\_NET\_CAPTURE)

118 const struct net\_capture\_interface\_api \*api =

119 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

120

121 return api->enable(dev, iface);

122#else

123 ARG\_UNUSED(dev);

124 ARG\_UNUSED(iface);

125

126 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

127#endif

128}

129

[ 138](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)static inline bool [net\_capture\_is\_enabled](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)(const struct [device](structdevice.md) \*dev)

139{

140#if defined(CONFIG\_NET\_CAPTURE)

141 const struct net\_capture\_interface\_api \*api;

142

143 if (dev == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

144 /\* TODO: Go through all capture devices instead of one \*/

145 dev = [device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)("NET\_CAPTURE0");

146 if (dev == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

147 return false;

148 }

149 }

150

151 api = (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

152

153 return api->is\_enabled(dev);

154#else

155 ARG\_UNUSED(dev);

156

157 return false;

158#endif

159}

160

[ 168](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)static inline int [net\_capture\_disable](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)(const struct [device](structdevice.md) \*dev)

169{

170#if defined(CONFIG\_NET\_CAPTURE)

171 const struct net\_capture\_interface\_api \*api =

172 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

173

174 return api->disable(dev);

175#else

176 ARG\_UNUSED(dev);

177

178 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

179#endif

180}

181

183

193static inline int net\_capture\_send(const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface,

194 struct [net\_pkt](structnet__pkt.md) \*pkt)

195{

196#if defined(CONFIG\_NET\_CAPTURE)

197 const struct net\_capture\_interface\_api \*api =

198 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

199

200 return api->send(dev, iface, pkt);

201#else

202 ARG\_UNUSED(dev);

203 ARG\_UNUSED(iface);

204 ARG\_UNUSED(pkt);

205

206 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

207#endif

208}

209

217#if defined(CONFIG\_NET\_CAPTURE)

218void net\_capture\_pkt(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

219#else

220static inline void net\_capture\_pkt(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt)

221{

222 ARG\_UNUSED(iface);

223 ARG\_UNUSED(pkt);

224}

225#endif

226

228

238#if defined(CONFIG\_NET\_CAPTURE)

239int net\_capture\_pkt\_with\_status(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

240#else

241static inline int net\_capture\_pkt\_with\_status(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt)

242{

243 ARG\_UNUSED(iface);

244 ARG\_UNUSED(pkt);

245

246 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

247}

248#endif

249

251

253enum net\_capture\_packet\_type {

254 NET\_CAPTURE\_HOST,

255 NET\_CAPTURE\_BROADCAST,

256 NET\_CAPTURE\_MULTICAST,

257 NET\_CAPTURE\_OTHERHOST,

258 NET\_CAPTURE\_OUTGOING,

259};

260

261#define NET\_CAPTURE\_LL\_ADDRLEN 8

262

264struct net\_capture\_cooked {

266 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hatype;

268 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) halen;

270 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr[NET\_CAPTURE\_LL\_ADDRLEN];

271};

272

283#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

284int net\_capture\_cooked\_setup(struct net\_capture\_cooked \*ctx,

285 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hatype,

286 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) halen,

287 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr);

288#else

289static inline int net\_capture\_cooked\_setup(struct net\_capture\_cooked \*ctx,

290 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hatype,

291 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) halen,

292 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr)

293{

294 ARG\_UNUSED(ctx);

295 ARG\_UNUSED(hatype);

296 ARG\_UNUSED(halen);

297 ARG\_UNUSED(addr);

298

299 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

300}

301#endif

302

317#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

318void net\_capture\_data(struct net\_capture\_cooked \*ctx,

319 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

320 enum net\_capture\_packet\_type type,

321 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ptype);

322#else

323static inline void net\_capture\_data(struct net\_capture\_cooked \*ctx,

324 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

325 enum net\_capture\_packet\_type type,

326 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ptype)

327{

328 ARG\_UNUSED(ctx);

329 ARG\_UNUSED(data);

330 ARG\_UNUSED(len);

331 ARG\_UNUSED(type);

332 ARG\_UNUSED(ptype);

333}

334#endif

335

336struct net\_capture\_info {

337 const struct device \*capture\_dev;

338 struct net\_if \*capture\_iface;

339 struct net\_if \*tunnel\_iface;

340 struct sockaddr \*peer;

341 struct sockaddr \*local;

342 bool is\_enabled;

343};

344

352typedef void (\*net\_capture\_cb\_t)(struct net\_capture\_info \*info, void \*user\_data);

353

363#if defined(CONFIG\_NET\_CAPTURE)

364void net\_capture\_foreach(net\_capture\_cb\_t cb, void \*user\_data);

365#else

366static inline void net\_capture\_foreach(net\_capture\_cb\_t cb, void \*user\_data)

367{

368 ARG\_UNUSED(cb);

369 ARG\_UNUSED(user\_data);

370}

371#endif

372

374

378

379#ifdef \_\_cplusplus

380}

381#endif

382

383#endif /\* ZEPHYR\_INCLUDE\_NET\_CAPTURE\_H\_ \*/

[device.h](device_8h.md)

[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)

const struct device \* device\_get\_binding(const char \*name)

Get a device reference from its device::name field.

[net\_capture\_disable](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)

static int net\_capture\_disable(const struct device \*dev)

Disable network packet capturing support.

**Definition** capture.h:168

[net\_capture\_is\_enabled](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)

static bool net\_capture\_is\_enabled(const struct device \*dev)

Is network packet capture enabled or disabled.

**Definition** capture.h:138

[net\_capture\_cleanup](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)

static int net\_capture\_cleanup(const struct device \*dev)

Cleanup network packet capturing support.

**Definition** capture.h:89

[net\_capture\_setup](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)

int net\_capture\_setup(const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr, const struct device \*\*dev)

Setup network packet capturing support.

[net\_capture\_enable](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)

static int net\_capture\_enable(const struct device \*dev, struct net\_if \*iface)

Enable network packet capturing support.

**Definition** capture.h:115

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[kernel.h](kernel_8h.md)

Public kernel APIs.

[send](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f)

ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [capture.h](capture_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
