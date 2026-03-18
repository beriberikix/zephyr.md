---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/uhc_8h_source.html
original_path: doxygen/html/uhc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uhc.h

[Go to the documentation of this file.](uhc_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_UHC\_H

13#define ZEPHYR\_INCLUDE\_UHC\_H

14

15#include <[zephyr/kernel.h](kernel_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/net/buf.h](net_2buf_8h.md)>

18#include <[zephyr/usb/usb\_ch9.h](usb__ch9_8h.md)>

19#include <[zephyr/sys/dlist.h](dlist_8h.md)>

20

27

[ 31](group__uhc__api.md#gaef9b0703714676c1f7bd1cad57f49bc8)enum [uhc\_control\_stage](group__uhc__api.md#gaef9b0703714676c1f7bd1cad57f49bc8) {

[ 32](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8) [UHC\_CONTROL\_STAGE\_SETUP](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8) = 0,

[ 33](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5) [UHC\_CONTROL\_STAGE\_DATA](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5),

[ 34](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f) [UHC\_CONTROL\_STAGE\_STATUS](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f),

35};

36

[ 47](structuhc__transfer.md)struct [uhc\_transfer](structuhc__transfer.md) {

[ 49](structuhc__transfer.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structuhc__transfer.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d);

[ 51](structuhc__transfer.md#af5e8080b91078a1c9f8ff269c72d70e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [setup\_pkt](structuhc__transfer.md#af5e8080b91078a1c9f8ff269c72d70e9)[8];

[ 53](structuhc__transfer.md#a170385b08171659f05ac7112faf8e587) struct [net\_buf](structnet__buf.md) \*[buf](structuhc__transfer.md#a170385b08171659f05ac7112faf8e587);

[ 55](structuhc__transfer.md#a3dbfba5c7d22b69c320fd91079797a2c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structuhc__transfer.md#a3dbfba5c7d22b69c320fd91079797a2c);

[ 57](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef);

[ 59](structuhc__transfer.md#ade24e9892c5c2d87f76cd3898c11304e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [attrib](structuhc__transfer.md#ade24e9892c5c2d87f76cd3898c11304e);

[ 61](structuhc__transfer.md#a61a6c74cc7c026404ccf42d1164765b8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mps](structuhc__transfer.md#a61a6c74cc7c026404ccf42d1164765b8);

[ 63](structuhc__transfer.md#a6219fe4fafb80e253d22b3a16faee230) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structuhc__transfer.md#a6219fe4fafb80e253d22b3a16faee230);

[ 65](structuhc__transfer.md#ad2b246c850c3b30f7d2b58fc9a47008b) unsigned int [queued](structuhc__transfer.md#ad2b246c850c3b30f7d2b58fc9a47008b) : 1;

[ 67](structuhc__transfer.md#a9983482be9724e281e56c978ce27d93f) unsigned int [stage](structuhc__transfer.md#a9983482be9724e281e56c978ce27d93f) : 2;

[ 69](structuhc__transfer.md#a00a20358e5ea4bab3d21c146cfb74737) void \*[udev](structuhc__transfer.md#a00a20358e5ea4bab3d21c146cfb74737);

[ 71](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287) void \*[cb](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287);

[ 73](structuhc__transfer.md#a11f002f91b1039c226b7c9feb8223e11) int [err](structuhc__transfer.md#a11f002f91b1039c226b7c9feb8223e11);

74};

75

[ 79](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb)enum [uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb) {

[ 81](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70) [UHC\_EVT\_DEV\_CONNECTED\_LS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70),

[ 83](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce) [UHC\_EVT\_DEV\_CONNECTED\_FS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce),

[ 85](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f) [UHC\_EVT\_DEV\_CONNECTED\_HS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f),

[ 87](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30) [UHC\_EVT\_DEV\_REMOVED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30),

[ 89](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3) [UHC\_EVT\_RESETED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3),

[ 91](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a) [UHC\_EVT\_SUSPENDED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a),

[ 93](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848) [UHC\_EVT\_RESUMED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848),

[ 95](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e) [UHC\_EVT\_RWUP](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e),

[ 97](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483) [UHC\_EVT\_EP\_REQUEST](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483),

[ 102](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7) [UHC\_EVT\_ERROR](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7),

103};

104

[ 113](structuhc__event.md)struct [uhc\_event](structuhc__event.md) {

[ 115](structuhc__event.md#acd04587fac14f9a8a91b75642f5b2e82) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structuhc__event.md#acd04587fac14f9a8a91b75642f5b2e82);

[ 117](structuhc__event.md#a30fddbbe0f15a16320fba3cb4fd81d84) enum [uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb) [type](structuhc__event.md#a30fddbbe0f15a16320fba3cb4fd81d84);

118 union {

[ 120](structuhc__event.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6) int [status](structuhc__event.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6);

[ 122](structuhc__event.md#a03f3cebee6edfaf620a98c198a70dbd0) struct [uhc\_transfer](structuhc__transfer.md) \*[xfer](structuhc__event.md#a03f3cebee6edfaf620a98c198a70dbd0);

123 };

[ 125](structuhc__event.md#a055be3fd47e16bc48498163be3e55d09) const struct [device](structdevice.md) \*[dev](structuhc__event.md#a055be3fd47e16bc48498163be3e55d09);

126};

127

[ 139](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9)typedef int (\*[uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9))(const struct [device](structdevice.md) \*dev,

140 const struct [uhc\_event](structuhc__event.md) \*const event);

141

[ 147](structuhc__device__caps.md)struct [uhc\_device\_caps](structuhc__device__caps.md) {

[ 149](structuhc__device__caps.md#ab526337af28d25728780cb48dc43e722) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hs](structuhc__device__caps.md#ab526337af28d25728780cb48dc43e722) : 1;

150};

151

[ 155](group__uhc__api.md#ga09ad6fc9251212fa0dffececb767ff9e)#define UHC\_STATUS\_INITIALIZED 0

[ 159](group__uhc__api.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)#define UHC\_STATUS\_ENABLED 1

160

[ 167](structuhc__data.md)struct [uhc\_data](structuhc__data.md) {

[ 169](structuhc__data.md#ac2a48d1d6692931807e8985799c5bdb0) struct [uhc\_device\_caps](structuhc__device__caps.md) [caps](structuhc__data.md#ac2a48d1d6692931807e8985799c5bdb0);

[ 171](structuhc__data.md#a08772cdd5b42bd11ca4a06a75df846e9) struct [k\_mutex](structk__mutex.md) [mutex](structuhc__data.md#a08772cdd5b42bd11ca4a06a75df846e9);

[ 173](structuhc__data.md#a32eec449ffbe5e6c262c907e6e6b475a) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [ctrl\_xfers](structuhc__data.md#a32eec449ffbe5e6c262c907e6e6b475a);

[ 175](structuhc__data.md#ac6214566324740c34a8bba42515d1d32) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [bulk\_xfers](structuhc__data.md#ac6214566324740c34a8bba42515d1d32);

[ 177](structuhc__data.md#afd1a0828a0ca3e397dba09fe38fd8050) [uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9) [event\_cb](structuhc__data.md#afd1a0828a0ca3e397dba09fe38fd8050);

[ 179](structuhc__data.md#a10852f2523cc733541cc9ea51706559f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [status](structuhc__data.md#a10852f2523cc733541cc9ea51706559f);

[ 181](structuhc__data.md#a294120f6cf8563cb9564c51fcf56d883) void \*[priv](structuhc__data.md#a294120f6cf8563cb9564c51fcf56d883);

182};

183

[ 191](group__uhc__api.md#ga3251967d36b67169d7892a615323c14e)static inline bool [uhc\_is\_initialized](group__uhc__api.md#ga3251967d36b67169d7892a615323c14e)(const struct [device](structdevice.md) \*dev)

192{

193 struct [uhc\_data](structuhc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

194

195 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&data->[status](structuhc__data.md#a10852f2523cc733541cc9ea51706559f), [UHC\_STATUS\_INITIALIZED](group__uhc__api.md#ga09ad6fc9251212fa0dffececb767ff9e));

196}

197

[ 205](group__uhc__api.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)static inline bool [uhc\_is\_enabled](group__uhc__api.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)(const struct [device](structdevice.md) \*dev)

206{

207 struct [uhc\_data](structuhc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

208

209 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&data->[status](structuhc__data.md#a10852f2523cc733541cc9ea51706559f), [UHC\_STATUS\_ENABLED](group__uhc__api.md#ga230e104bd7be1d4b83b2d31ee72ac3c4));

210}

211

215struct uhc\_api {

216 int (\*lock)(const struct device \*dev);

217 int (\*unlock)(const struct device \*dev);

218

219 int (\*init)(const struct device \*dev);

220 int (\*enable)(const struct device \*dev);

221 int (\*disable)(const struct device \*dev);

222 int (\*[shutdown](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf))(const struct device \*dev);

223

224 int (\*bus\_reset)(const struct device \*dev);

225 int (\*sof\_enable)(const struct device \*dev);

226 int (\*bus\_suspend)(const struct device \*dev);

227 int (\*bus\_resume)(const struct device \*dev);

228

229 int (\*ep\_enqueue)(const struct device \*dev,

230 struct uhc\_transfer \*const xfer);

231 int (\*ep\_dequeue)(const struct device \*dev,

232 struct uhc\_transfer \*const xfer);

233};

237

[ 249](group__uhc__api.md#ga4ceb0400168cd53201f0dde5f596452f)static inline int [uhc\_bus\_reset](group__uhc__api.md#ga4ceb0400168cd53201f0dde5f596452f)(const struct [device](structdevice.md) \*dev)

250{

251 const struct uhc\_api \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

252 int ret;

253

254 api->lock(dev);

255 ret = api->bus\_reset(dev);

256 api->unlock(dev);

257

258 return ret;

259}

260

[ 271](group__uhc__api.md#gafe55e97cbf31d163b10616c03da39414)static inline int [uhc\_sof\_enable](group__uhc__api.md#gafe55e97cbf31d163b10616c03da39414)(const struct [device](structdevice.md) \*dev)

272{

273 const struct uhc\_api \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

274 int ret;

275

276 api->lock(dev);

277 ret = api->sof\_enable(dev);

278 api->unlock(dev);

279

280 return ret;

281}

282

[ 294](group__uhc__api.md#ga897081ff02dab4377c68bcba343f492c)static inline int [uhc\_bus\_suspend](group__uhc__api.md#ga897081ff02dab4377c68bcba343f492c)(const struct [device](structdevice.md) \*dev)

295{

296 const struct uhc\_api \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

297 int ret;

298

299 api->lock(dev);

300 ret = api->bus\_suspend(dev);

301 api->unlock(dev);

302

303 return ret;

304}

305

[ 317](group__uhc__api.md#ga6669bc2ac56395b38292fa796b99bfd9)static inline int [uhc\_bus\_resume](group__uhc__api.md#ga6669bc2ac56395b38292fa796b99bfd9)(const struct [device](structdevice.md) \*dev)

318{

319 const struct uhc\_api \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

320 int ret;

321

322 api->lock(dev);

323 ret = api->bus\_resume(dev);

324 api->unlock(dev);

325

326 return ret;

327}

328

[ 347](group__uhc__api.md#ga14a5d093d97fc19c7d8e9ec9f0330eaa)struct [uhc\_transfer](structuhc__transfer.md) \*[uhc\_xfer\_alloc](group__uhc__api.md#ga14a5d093d97fc19c7d8e9ec9f0330eaa)(const struct [device](structdevice.md) \*dev,

348 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structuhc__transfer.md#a3dbfba5c7d22b69c320fd91079797a2c),

349 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef),

350 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [attrib](structuhc__transfer.md#ade24e9892c5c2d87f76cd3898c11304e),

351 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mps](structuhc__transfer.md#a61a6c74cc7c026404ccf42d1164765b8),

352 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structuhc__transfer.md#a6219fe4fafb80e253d22b3a16faee230),

353 void \*const [udev](structuhc__transfer.md#a00a20358e5ea4bab3d21c146cfb74737),

354 void \*const [cb](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287));

355

[ 373](group__uhc__api.md#ga520161e0e390c94b9c745edc83b32816)struct [uhc\_transfer](structuhc__transfer.md) \*[uhc\_xfer\_alloc\_with\_buf](group__uhc__api.md#ga520161e0e390c94b9c745edc83b32816)(const struct [device](structdevice.md) \*dev,

374 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structuhc__transfer.md#a3dbfba5c7d22b69c320fd91079797a2c),

375 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef),

376 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [attrib](structuhc__transfer.md#ade24e9892c5c2d87f76cd3898c11304e),

377 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mps](structuhc__transfer.md#a61a6c74cc7c026404ccf42d1164765b8),

378 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [timeout](structuhc__transfer.md#a6219fe4fafb80e253d22b3a16faee230),

379 void \*const [udev](structuhc__transfer.md#a00a20358e5ea4bab3d21c146cfb74737),

380 void \*const [cb](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287),

381 size\_t size);

382

[ 393](group__uhc__api.md#gab2f6328e8051559edccc05ae3552f4f9)int [uhc\_xfer\_free](group__uhc__api.md#gab2f6328e8051559edccc05ae3552f4f9)(const struct [device](structdevice.md) \*dev,

394 struct [uhc\_transfer](structuhc__transfer.md) \*const xfer);

395

[ 407](group__uhc__api.md#ga779dbd7ee8ac5fce487e087706791ea7)int [uhc\_xfer\_buf\_add](group__uhc__api.md#ga779dbd7ee8ac5fce487e087706791ea7)(const struct [device](structdevice.md) \*dev,

408 struct [uhc\_transfer](structuhc__transfer.md) \*const xfer,

409 struct [net\_buf](structnet__buf.md) \*[buf](structuhc__transfer.md#a170385b08171659f05ac7112faf8e587));

[ 421](group__uhc__api.md#gab4f7439fab8c57e203862bc408a6e46b)struct [net\_buf](structnet__buf.md) \*[uhc\_xfer\_buf\_alloc](group__uhc__api.md#gab4f7439fab8c57e203862bc408a6e46b)(const struct [device](structdevice.md) \*dev,

422 const size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

423

[ 432](group__uhc__api.md#gac4bd26a85f8abc2006ecf2622669d615)void [uhc\_xfer\_buf\_free](group__uhc__api.md#gac4bd26a85f8abc2006ecf2622669d615)(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf);

433

[ 446](group__uhc__api.md#ga7a07b598c00d53393e15f6dae5cf1c4a)int [uhc\_ep\_enqueue](group__uhc__api.md#ga7a07b598c00d53393e15f6dae5cf1c4a)(const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer);

447

[ 459](group__uhc__api.md#ga7c362cba29e0181ffcc8f70060100e62)int [uhc\_ep\_dequeue](group__uhc__api.md#ga7c362cba29e0181ffcc8f70060100e62)(const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer);

460

[ 473](group__uhc__api.md#gabfee9100a18fdf67c5d4f8f99928d530)int [uhc\_init](group__uhc__api.md#gabfee9100a18fdf67c5d4f8f99928d530)(const struct [device](structdevice.md) \*dev, [uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9) event\_cb);

474

[ 487](group__uhc__api.md#gafe94b7f9e32aada9634166ebb2115c2f)int [uhc\_enable](group__uhc__api.md#gafe94b7f9e32aada9634166ebb2115c2f)(const struct [device](structdevice.md) \*dev);

488

[ 499](group__uhc__api.md#ga9ec92df4497588adbf8da6f0777a4afd)int [uhc\_disable](group__uhc__api.md#ga9ec92df4497588adbf8da6f0777a4afd)(const struct [device](structdevice.md) \*dev);

500

[ 512](group__uhc__api.md#gac6d1feb9481882a711e58c3e55e915cb)int [uhc\_shutdown](group__uhc__api.md#gac6d1feb9481882a711e58c3e55e915cb)(const struct [device](structdevice.md) \*dev);

513

[ 524](group__uhc__api.md#ga8796569eba96260ce332e611fb520033)static inline struct [uhc\_device\_caps](structuhc__device__caps.md) [uhc\_caps](group__uhc__api.md#ga8796569eba96260ce332e611fb520033)(const struct [device](structdevice.md) \*dev)

525{

526 struct [uhc\_data](structuhc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

527

528 return data->[caps](structuhc__data.md#ac2a48d1d6692931807e8985799c5bdb0);

529}

530

534

535#endif /\* ZEPHYR\_INCLUDE\_UHC\_H \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[dlist.h](dlist_8h.md)

[atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)

static bool atomic\_test\_bit(const atomic\_t \*target, int bit)

Atomically test a bit.

**Definition** atomic.h:127

[shutdown](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf)

static int shutdown(int sock, int how)

POSIX wrapper for zsock\_shutdown.

**Definition** socket.h:885

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:50

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[UHC\_STATUS\_INITIALIZED](group__uhc__api.md#ga09ad6fc9251212fa0dffececb767ff9e)

#define UHC\_STATUS\_INITIALIZED

Controller is initialized by uhc\_init().

**Definition** uhc.h:155

[uhc\_is\_enabled](group__uhc__api.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)

static bool uhc\_is\_enabled(const struct device \*dev)

Checks whether the controller is enabled.

**Definition** uhc.h:205

[uhc\_xfer\_alloc](group__uhc__api.md#ga14a5d093d97fc19c7d8e9ec9f0330eaa)

struct uhc\_transfer \* uhc\_xfer\_alloc(const struct device \*dev, const uint8\_t addr, const uint8\_t ep, const uint8\_t attrib, const uint16\_t mps, const uint16\_t timeout, void \*const udev, void \*const cb)

Allocate UHC transfer.

[UHC\_STATUS\_ENABLED](group__uhc__api.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)

#define UHC\_STATUS\_ENABLED

Controller is enabled and all API functions are available.

**Definition** uhc.h:159

[uhc\_is\_initialized](group__uhc__api.md#ga3251967d36b67169d7892a615323c14e)

static bool uhc\_is\_initialized(const struct device \*dev)

Checks whether the controller is initialized.

**Definition** uhc.h:191

[uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9)

int(\* uhc\_event\_cb\_t)(const struct device \*dev, const struct uhc\_event \*const event)

Callback to submit UHC event to higher layer.

**Definition** uhc.h:139

[uhc\_bus\_reset](group__uhc__api.md#ga4ceb0400168cd53201f0dde5f596452f)

static int uhc\_bus\_reset(const struct device \*dev)

Reset USB bus.

**Definition** uhc.h:249

[uhc\_xfer\_alloc\_with\_buf](group__uhc__api.md#ga520161e0e390c94b9c745edc83b32816)

struct uhc\_transfer \* uhc\_xfer\_alloc\_with\_buf(const struct device \*dev, const uint8\_t addr, const uint8\_t ep, const uint8\_t attrib, const uint16\_t mps, const uint16\_t timeout, void \*const udev, void \*const cb, size\_t size)

Allocate UHC transfer with buffer.

[uhc\_bus\_resume](group__uhc__api.md#ga6669bc2ac56395b38292fa796b99bfd9)

static int uhc\_bus\_resume(const struct device \*dev)

Resume USB bus.

**Definition** uhc.h:317

[uhc\_xfer\_buf\_add](group__uhc__api.md#ga779dbd7ee8ac5fce487e087706791ea7)

int uhc\_xfer\_buf\_add(const struct device \*dev, struct uhc\_transfer \*const xfer, struct net\_buf \*buf)

Add UHC transfer buffer.

[uhc\_ep\_enqueue](group__uhc__api.md#ga7a07b598c00d53393e15f6dae5cf1c4a)

int uhc\_ep\_enqueue(const struct device \*dev, struct uhc\_transfer \*const xfer)

Queue USB host controller transfer.

[uhc\_ep\_dequeue](group__uhc__api.md#ga7c362cba29e0181ffcc8f70060100e62)

int uhc\_ep\_dequeue(const struct device \*dev, struct uhc\_transfer \*const xfer)

Remove a USB host controller transfers from queue.

[uhc\_caps](group__uhc__api.md#ga8796569eba96260ce332e611fb520033)

static struct uhc\_device\_caps uhc\_caps(const struct device \*dev)

Get USB host controller capabilities.

**Definition** uhc.h:524

[uhc\_bus\_suspend](group__uhc__api.md#ga897081ff02dab4377c68bcba343f492c)

static int uhc\_bus\_suspend(const struct device \*dev)

Suspend USB bus.

**Definition** uhc.h:294

[uhc\_disable](group__uhc__api.md#ga9ec92df4497588adbf8da6f0777a4afd)

int uhc\_disable(const struct device \*dev)

Disable USB host controller.

[uhc\_xfer\_free](group__uhc__api.md#gab2f6328e8051559edccc05ae3552f4f9)

int uhc\_xfer\_free(const struct device \*dev, struct uhc\_transfer \*const xfer)

Free UHC transfer and any buffers.

[uhc\_xfer\_buf\_alloc](group__uhc__api.md#gab4f7439fab8c57e203862bc408a6e46b)

struct net\_buf \* uhc\_xfer\_buf\_alloc(const struct device \*dev, const size\_t size)

Allocate UHC transfer buffer.

[uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb)

uhc\_event\_type

USB host controller event types.

**Definition** uhc.h:79

[uhc\_init](group__uhc__api.md#gabfee9100a18fdf67c5d4f8f99928d530)

int uhc\_init(const struct device \*dev, uhc\_event\_cb\_t event\_cb)

Initialize USB host controller.

[uhc\_xfer\_buf\_free](group__uhc__api.md#gac4bd26a85f8abc2006ecf2622669d615)

void uhc\_xfer\_buf\_free(const struct device \*dev, struct net\_buf \*const buf)

Free UHC request buffer.

[uhc\_shutdown](group__uhc__api.md#gac6d1feb9481882a711e58c3e55e915cb)

int uhc\_shutdown(const struct device \*dev)

Poweroff USB host controller.

[uhc\_control\_stage](group__uhc__api.md#gaef9b0703714676c1f7bd1cad57f49bc8)

uhc\_control\_stage

USB control transfer stage.

**Definition** uhc.h:31

[uhc\_sof\_enable](group__uhc__api.md#gafe55e97cbf31d163b10616c03da39414)

static int uhc\_sof\_enable(const struct device \*dev)

Enable Start of Frame generator.

**Definition** uhc.h:271

[uhc\_enable](group__uhc__api.md#gafe94b7f9e32aada9634166ebb2115c2f)

int uhc\_enable(const struct device \*dev)

Enable USB host controller.

[UHC\_EVT\_EP\_REQUEST](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483)

@ UHC\_EVT\_EP\_REQUEST

Endpoint request result event.

**Definition** uhc.h:97

[UHC\_EVT\_DEV\_CONNECTED\_HS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f)

@ UHC\_EVT\_DEV\_CONNECTED\_HS

High speed device connected.

**Definition** uhc.h:85

[UHC\_EVT\_DEV\_CONNECTED\_FS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce)

@ UHC\_EVT\_DEV\_CONNECTED\_FS

Full speed device connected.

**Definition** uhc.h:83

[UHC\_EVT\_RWUP](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e)

@ UHC\_EVT\_RWUP

Remote wakeup signal.

**Definition** uhc.h:95

[UHC\_EVT\_SUSPENDED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a)

@ UHC\_EVT\_SUSPENDED

Bus suspend operation finished.

**Definition** uhc.h:91

[UHC\_EVT\_DEV\_REMOVED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30)

@ UHC\_EVT\_DEV\_REMOVED

Device (peripheral) removed.

**Definition** uhc.h:87

[UHC\_EVT\_RESUMED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848)

@ UHC\_EVT\_RESUMED

Bus resume operation finished.

**Definition** uhc.h:93

[UHC\_EVT\_DEV\_CONNECTED\_LS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70)

@ UHC\_EVT\_DEV\_CONNECTED\_LS

Low speed device connected.

**Definition** uhc.h:81

[UHC\_EVT\_ERROR](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7)

@ UHC\_EVT\_ERROR

Non-correctable error event, requires attention from higher levels or application.

**Definition** uhc.h:102

[UHC\_EVT\_RESETED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3)

@ UHC\_EVT\_RESETED

Bus reset operation finished.

**Definition** uhc.h:89

[UHC\_CONTROL\_STAGE\_DATA](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5)

@ UHC\_CONTROL\_STAGE\_DATA

**Definition** uhc.h:33

[UHC\_CONTROL\_STAGE\_SETUP](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8)

@ UHC\_CONTROL\_STAGE\_SETUP

**Definition** uhc.h:32

[UHC\_CONTROL\_STAGE\_STATUS](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f)

@ UHC\_CONTROL\_STAGE\_STATUS

**Definition** uhc.h:34

[kernel.h](kernel_8h.md)

Public kernel APIs.

[buf.h](net_2buf_8h.md)

Buffer management.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2917

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:1004

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** buf.h:1036

[uhc\_data](structuhc__data.md)

Common UHC driver data structure.

**Definition** uhc.h:167

[uhc\_data::mutex](structuhc__data.md#a08772cdd5b42bd11ca4a06a75df846e9)

struct k\_mutex mutex

Driver access mutex.

**Definition** uhc.h:171

[uhc\_data::status](structuhc__data.md#a10852f2523cc733541cc9ea51706559f)

atomic\_t status

USB host controller status.

**Definition** uhc.h:179

[uhc\_data::priv](structuhc__data.md#a294120f6cf8563cb9564c51fcf56d883)

void \* priv

Driver private data.

**Definition** uhc.h:181

[uhc\_data::ctrl\_xfers](structuhc__data.md#a32eec449ffbe5e6c262c907e6e6b475a)

sys\_dlist\_t ctrl\_xfers

dlist for control transfers

**Definition** uhc.h:173

[uhc\_data::caps](structuhc__data.md#ac2a48d1d6692931807e8985799c5bdb0)

struct uhc\_device\_caps caps

Controller capabilities.

**Definition** uhc.h:169

[uhc\_data::bulk\_xfers](structuhc__data.md#ac6214566324740c34a8bba42515d1d32)

sys\_dlist\_t bulk\_xfers

dlist for bulk transfers

**Definition** uhc.h:175

[uhc\_data::event\_cb](structuhc__data.md#afd1a0828a0ca3e397dba09fe38fd8050)

uhc\_event\_cb\_t event\_cb

Callback to submit an UHC event to upper layer.

**Definition** uhc.h:177

[uhc\_device\_caps](structuhc__device__caps.md)

USB host controller capabilities.

**Definition** uhc.h:147

[uhc\_device\_caps::hs](structuhc__device__caps.md#ab526337af28d25728780cb48dc43e722)

uint32\_t hs

USB high speed capable controller.

**Definition** uhc.h:149

[uhc\_event](structuhc__event.md)

USB host controller event.

**Definition** uhc.h:113

[uhc\_event::xfer](structuhc__event.md#a03f3cebee6edfaf620a98c198a70dbd0)

struct uhc\_transfer \* xfer

Pointer to request used only for UHC\_EVT\_EP\_REQUEST.

**Definition** uhc.h:122

[uhc\_event::dev](structuhc__event.md#a055be3fd47e16bc48498163be3e55d09)

const struct device \* dev

Pointer to controller's device struct.

**Definition** uhc.h:125

[uhc\_event::type](structuhc__event.md#a30fddbbe0f15a16320fba3cb4fd81d84)

enum uhc\_event\_type type

Event type.

**Definition** uhc.h:117

[uhc\_event::status](structuhc__event.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6)

int status

Event status value, if any.

**Definition** uhc.h:120

[uhc\_event::node](structuhc__event.md#acd04587fac14f9a8a91b75642f5b2e82)

sys\_snode\_t node

slist node for the message queue

**Definition** uhc.h:115

[uhc\_transfer](structuhc__transfer.md)

UHC endpoint buffer info.

**Definition** uhc.h:47

[uhc\_transfer::udev](structuhc__transfer.md#a00a20358e5ea4bab3d21c146cfb74737)

void \* udev

Pointer to USB device (opaque for the UHC).

**Definition** uhc.h:69

[uhc\_transfer::err](structuhc__transfer.md#a11f002f91b1039c226b7c9feb8223e11)

int err

Transfer result, 0 on success, other values on error.

**Definition** uhc.h:73

[uhc\_transfer::buf](structuhc__transfer.md#a170385b08171659f05ac7112faf8e587)

struct net\_buf \* buf

Transfer data buffer.

**Definition** uhc.h:53

[uhc\_transfer::addr](structuhc__transfer.md#a3dbfba5c7d22b69c320fd91079797a2c)

uint8\_t addr

Device (peripheral) address.

**Definition** uhc.h:55

[uhc\_transfer::mps](structuhc__transfer.md#a61a6c74cc7c026404ccf42d1164765b8)

uint16\_t mps

Maximum packet size.

**Definition** uhc.h:61

[uhc\_transfer::timeout](structuhc__transfer.md#a6219fe4fafb80e253d22b3a16faee230)

uint16\_t timeout

Timeout in number of frames.

**Definition** uhc.h:63

[uhc\_transfer::stage](structuhc__transfer.md#a9983482be9724e281e56c978ce27d93f)

unsigned int stage

Control stage status, up to the driver to use it or not.

**Definition** uhc.h:67

[uhc\_transfer::ep](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef)

uint8\_t ep

Endpoint to which request is associated.

**Definition** uhc.h:57

[uhc\_transfer::queued](structuhc__transfer.md#ad2b246c850c3b30f7d2b58fc9a47008b)

unsigned int queued

Flag marks request buffer is queued.

**Definition** uhc.h:65

[uhc\_transfer::cb](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287)

void \* cb

Pointer to transfer completion callback (opaque for the UHC).

**Definition** uhc.h:71

[uhc\_transfer::attrib](structuhc__transfer.md#ade24e9892c5c2d87f76cd3898c11304e)

uint8\_t attrib

Endpoint attributes (TBD).

**Definition** uhc.h:59

[uhc\_transfer::node](structuhc__transfer.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d)

sys\_dnode\_t node

dlist node

**Definition** uhc.h:49

[uhc\_transfer::setup\_pkt](structuhc__transfer.md#af5e8080b91078a1c9f8ff269c72d70e9)

uint8\_t setup\_pkt[8]

Control transfer setup packet.

**Definition** uhc.h:51

[usb\_ch9.h](usb__ch9_8h.md)

USB Chapter 9 structures and definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [uhc.h](uhc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
