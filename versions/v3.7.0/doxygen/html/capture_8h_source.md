---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/capture_8h_source.html
original_path: doxygen/html/capture_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

29

31

32struct [net\_if](structnet__if.md);

33struct [net\_pkt](structnet__pkt.md);

34struct [device](structdevice.md);

35

36struct net\_capture\_interface\_api {

40 int (\*cleanup)(const struct device \*dev);

41

43 int (\*enable)(const struct device \*dev, struct net\_if \*iface);

44

46 int (\*disable)(const struct device \*dev);

47

50 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*is\_enabled)(const struct device \*dev);

51

53 int (\*[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d))(const struct device \*dev, struct net\_if \*iface, struct net\_pkt \*pkt);

54};

55

57

[ 73](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)int [net\_capture\_setup](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)(const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr,

74 const struct [device](structdevice.md) \*\*dev);

75

[ 87](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)static inline int [net\_capture\_cleanup](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)(const struct [device](structdevice.md) \*dev)

88{

89#if defined(CONFIG\_NET\_CAPTURE)

90 const struct net\_capture\_interface\_api \*api =

91 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

92

93 return api->cleanup(dev);

94#else

95 ARG\_UNUSED(dev);

96

97 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

98#endif

99}

100

[ 113](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)static inline int [net\_capture\_enable](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)(const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface)

114{

115#if defined(CONFIG\_NET\_CAPTURE)

116 const struct net\_capture\_interface\_api \*api =

117 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

118

119 return api->enable(dev, iface);

120#else

121 ARG\_UNUSED(dev);

122 ARG\_UNUSED(iface);

123

124 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

125#endif

126}

127

[ 136](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)static inline bool [net\_capture\_is\_enabled](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)(const struct [device](structdevice.md) \*dev)

137{

138#if defined(CONFIG\_NET\_CAPTURE)

139 const struct net\_capture\_interface\_api \*api;

140

141 if (dev == NULL) {

142 /\* TODO: Go through all capture devices instead of one \*/

143 dev = [device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)("NET\_CAPTURE0");

144 if (dev == NULL) {

145 return false;

146 }

147 }

148

149 api = (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

150

151 return api->is\_enabled(dev);

152#else

153 ARG\_UNUSED(dev);

154

155 return false;

156#endif

157}

158

[ 166](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)static inline int [net\_capture\_disable](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)(const struct [device](structdevice.md) \*dev)

167{

168#if defined(CONFIG\_NET\_CAPTURE)

169 const struct net\_capture\_interface\_api \*api =

170 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

171

172 return api->disable(dev);

173#else

174 ARG\_UNUSED(dev);

175

176 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

177#endif

178}

179

181

191static inline int net\_capture\_send(const struct [device](structdevice.md) \*dev, struct [net\_if](structnet__if.md) \*iface,

192 struct [net\_pkt](structnet__pkt.md) \*pkt)

193{

194#if defined(CONFIG\_NET\_CAPTURE)

195 const struct net\_capture\_interface\_api \*api =

196 (const struct net\_capture\_interface\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

197

198 return api->send(dev, iface, pkt);

199#else

200 ARG\_UNUSED(dev);

201 ARG\_UNUSED(iface);

202 ARG\_UNUSED(pkt);

203

204 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

205#endif

206}

207

215#if defined(CONFIG\_NET\_CAPTURE)

216void net\_capture\_pkt(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

217#else

218static inline void net\_capture\_pkt(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt)

219{

220 ARG\_UNUSED(iface);

221 ARG\_UNUSED(pkt);

222}

223#endif

224

226

236#if defined(CONFIG\_NET\_CAPTURE)

237int net\_capture\_pkt\_with\_status(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt);

238#else

239static inline int net\_capture\_pkt\_with\_status(struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt)

240{

241 ARG\_UNUSED(iface);

242 ARG\_UNUSED(pkt);

243

244 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

245}

246#endif

247

249

251enum net\_capture\_packet\_type {

252 NET\_CAPTURE\_HOST,

253 NET\_CAPTURE\_BROADCAST,

254 NET\_CAPTURE\_MULTICAST,

255 NET\_CAPTURE\_OTHERHOST,

256 NET\_CAPTURE\_OUTGOING,

257};

258

259#define NET\_CAPTURE\_LL\_ADDRLEN 8

260

262struct net\_capture\_cooked {

264 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hatype;

266 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) halen;

268 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr[NET\_CAPTURE\_LL\_ADDRLEN];

269};

270

281#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

282int net\_capture\_cooked\_setup(struct net\_capture\_cooked \*ctx,

283 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hatype,

284 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) halen,

285 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr);

286#else

287static inline int net\_capture\_cooked\_setup(struct net\_capture\_cooked \*ctx,

288 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hatype,

289 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) halen,

290 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr)

291{

292 ARG\_UNUSED(ctx);

293 ARG\_UNUSED(hatype);

294 ARG\_UNUSED(halen);

295 ARG\_UNUSED(addr);

296

297 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

298}

299#endif

300

315#if defined(CONFIG\_NET\_CAPTURE\_COOKED\_MODE)

316void net\_capture\_data(struct net\_capture\_cooked \*ctx,

317 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

318 enum net\_capture\_packet\_type type,

319 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ptype);

320#else

321static inline void net\_capture\_data(struct net\_capture\_cooked \*ctx,

322 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len,

323 enum net\_capture\_packet\_type type,

324 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ptype)

325{

326 ARG\_UNUSED(ctx);

327 ARG\_UNUSED(data);

328 ARG\_UNUSED(len);

329 ARG\_UNUSED(type);

330 ARG\_UNUSED(ptype);

331}

332#endif

333

334struct net\_capture\_info {

335 const struct device \*capture\_dev;

336 struct net\_if \*capture\_iface;

337 struct net\_if \*tunnel\_iface;

338 struct sockaddr \*peer;

339 struct sockaddr \*local;

340 bool is\_enabled;

341};

342

350typedef void (\*net\_capture\_cb\_t)(struct net\_capture\_info \*info, void \*user\_data);

351

361#if defined(CONFIG\_NET\_CAPTURE)

362void net\_capture\_foreach(net\_capture\_cb\_t cb, void \*user\_data);

363#else

364static inline void net\_capture\_foreach(net\_capture\_cb\_t cb, void \*user\_data)

365{

366 ARG\_UNUSED(cb);

367 ARG\_UNUSED(user\_data);

368}

369#endif

370

372

376

377#ifdef \_\_cplusplus

378}

379#endif

380

381#endif /\* ZEPHYR\_INCLUDE\_NET\_CAPTURE\_H\_ \*/

[device.h](device_8h.md)

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:916

[device\_get\_binding](group__device__model.md#ga15386ca9ab38f3e30183c18f604fa835)

const struct device \* device\_get\_binding(const char \*name)

Get a device reference from its device::name field.

[net\_capture\_disable](group__net__capture.md#ga32c66260fc888dcd38b6a3cffca3b951)

static int net\_capture\_disable(const struct device \*dev)

Disable network packet capturing support.

**Definition** capture.h:166

[net\_capture\_is\_enabled](group__net__capture.md#ga651987b8b1e713865cff01412934f3cc)

static bool net\_capture\_is\_enabled(const struct device \*dev)

Is network packet capture enabled or disabled.

**Definition** capture.h:136

[net\_capture\_cleanup](group__net__capture.md#ga7a56719068938c34c9c6149296074d01)

static int net\_capture\_cleanup(const struct device \*dev)

Cleanup network packet capturing support.

**Definition** capture.h:87

[net\_capture\_setup](group__net__capture.md#gab280c0c6cc607bdb07211a9450eae262)

int net\_capture\_setup(const char \*remote\_addr, const char \*my\_local\_addr, const char \*peer\_addr, const struct device \*\*dev)

Setup network packet capturing support.

[net\_capture\_enable](group__net__capture.md#gaf449c308080dc126e2e7c03b38d2a0aa)

static int net\_capture\_enable(const struct device \*dev, struct net\_if \*iface)

Enable network packet capturing support.

**Definition** capture.h:113

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[kernel.h](kernel_8h.md)

Public kernel APIs.

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

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:678

[net\_pkt](structnet__pkt.md)

Network packet.

**Definition** net\_pkt.h:67

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [capture.h](capture_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
