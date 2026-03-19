---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/conn__mgr__connectivity__impl_8h_source.html
original_path: doxygen/html/conn__mgr__connectivity__impl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn\_mgr\_connectivity\_impl.h

[Go to the documentation of this file.](conn__mgr__connectivity__impl_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_IMPL\_H\_

14#define ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_IMPL\_H\_

15

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/net/net\_if.h](net__if_8h.md)>

18#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

19#include <[zephyr/net/net\_mgmt.h](net__mgmt_8h.md)>

20#include <[zephyr/net/conn\_mgr\_connectivity.h](conn__mgr__connectivity_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

34

35/\* Forward declaration \*/

36struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md);

37

[ 43](structconn__mgr__conn__api.md)struct [conn\_mgr\_conn\_api](structconn__mgr__conn__api.md) {

[ 53](structconn__mgr__conn__api.md#a92064a4752f0c9621c5c6a745708a66e) int (\*[connect](structconn__mgr__conn__api.md#a92064a4752f0c9621c5c6a745708a66e))(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding);

54

[ 64](structconn__mgr__conn__api.md#aee0d0fc9ef3361c8859b69128a087ba5) int (\*[disconnect](structconn__mgr__conn__api.md#aee0d0fc9ef3361c8859b69128a087ba5))(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding);

65

[ 76](structconn__mgr__conn__api.md#ad2bb08d518e2f797002ca5257889a59e) void (\*[init](structconn__mgr__conn__api.md#ad2bb08d518e2f797002ca5257889a59e))(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding);

77

[ 96](structconn__mgr__conn__api.md#a5636cced185825bd6c6997b427fd6121) int (\*[set\_opt](structconn__mgr__conn__api.md#a5636cced185825bd6c6997b427fd6121))(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding,

97 int optname, const void \*optval, size\_t optlen);

98

[ 114](structconn__mgr__conn__api.md#a15d4bd909af1a2d3348fdec822bca7b7) int (\*[get\_opt](structconn__mgr__conn__api.md#a15d4bd909af1a2d3348fdec822bca7b7))(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*const binding,

115 int optname, void \*optval, size\_t \*optlen);

116};

117

119#define CONN\_MGR\_CONN\_IMPL\_GET\_NAME(conn\_id) \_\_conn\_mgr\_conn\_##conn\_id

120#define CONN\_MGR\_CONN\_IMPL\_GET\_CTX\_TYPE(conn\_id) conn\_id##\_CTX\_TYPE

122

[ 128](structconn__mgr__conn__impl.md)struct [conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md) {

[ 130](structconn__mgr__conn__impl.md#a1229707a1b919659647412cb1eecd61b) struct [conn\_mgr\_conn\_api](structconn__mgr__conn__api.md) \*[api](structconn__mgr__conn__impl.md#a1229707a1b919659647412cb1eecd61b);

131};

132

[ 139](group__conn__mgr__connectivity__impl.md#ga3c2b01efd38ecbb9fbb33ac0fc7c88f3)#define CONN\_MGR\_CONN\_DEFINE(conn\_id, conn\_api) \

140 const struct conn\_mgr\_conn\_impl CONN\_MGR\_CONN\_IMPL\_GET\_NAME(conn\_id) = { \

141 .api = conn\_api, \

142 };

143

[ 147](group__conn__mgr__connectivity__impl.md#ga519cfa66e1a1f0b769ce2bf61a61887f)#define CONN\_MGR\_CONN\_DECLARE\_PUBLIC(conn\_id) \

148 extern const struct conn\_mgr\_conn\_impl CONN\_MGR\_CONN\_IMPL\_GET\_NAME(conn\_id)

149

151#define CONN\_MGR\_CONN\_BINDING\_GET\_NAME(dev\_id, sfx) \_\_conn\_mgr\_bndg\_##dev\_id##\_##sfx

152#define CONN\_MGR\_CONN\_BINDING\_GET\_DATA(dev\_id, sfx) \_\_conn\_mgr\_bndg\_data\_##dev\_id##\_##sfx

153#define CONN\_MGR\_CONN\_BINDING\_GET\_MUTEX(dev\_id, sfx) \_\_conn\_mgr\_bndg\_mutex\_##dev\_id##\_##sfx

155

[ 162](structconn__mgr__conn__binding.md)struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) {

[ 164](structconn__mgr__conn__binding.md#a59bd71867b19e002c310d85496833e8f) struct [net\_if](structnet__if.md) \*[iface](structconn__mgr__conn__binding.md#a59bd71867b19e002c310d85496833e8f);

165

[ 167](structconn__mgr__conn__binding.md#a288749353194206b8d8766f8f17aff48) const struct [conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md) \*[impl](structconn__mgr__conn__binding.md#a288749353194206b8d8766f8f17aff48);

168

[ 170](structconn__mgr__conn__binding.md#ad9102e2cf44b5940b21b1d160fea7611) void \*[ctx](structconn__mgr__conn__binding.md#ad9102e2cf44b5940b21b1d160fea7611);

171

176

[ 183](structconn__mgr__conn__binding.md#a9b842340ebe872f30935b8f7e75d3605) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structconn__mgr__conn__binding.md#a9b842340ebe872f30935b8f7e75d3605);

184

[ 196](structconn__mgr__conn__binding.md#a8474461cf7b00132441227aae07511ab) int [timeout](structconn__mgr__conn__binding.md#a8474461cf7b00132441227aae07511ab);

197

199

201 /\* Internal-use mutex for protecting access to the binding and API functions. \*/

202 struct [k\_mutex](structk__mutex.md) \*mutex;

204};

205

[ 213](group__conn__mgr__connectivity__impl.md#ga1ac9fb870cd2d698451d896113b723d1)#define CONN\_MGR\_BIND\_CONN\_INST(dev\_id, inst, conn\_id) \

214 K\_MUTEX\_DEFINE(CONN\_MGR\_CONN\_BINDING\_GET\_MUTEX(dev\_id, inst)); \

215 static CONN\_MGR\_CONN\_IMPL\_GET\_CTX\_TYPE(conn\_id) \

216 CONN\_MGR\_CONN\_BINDING\_GET\_DATA(dev\_id, inst); \

217 static STRUCT\_SECTION\_ITERABLE(conn\_mgr\_conn\_binding, \

218 CONN\_MGR\_CONN\_BINDING\_GET\_NAME(dev\_id, inst)) = { \

219 .iface = NET\_IF\_GET(dev\_id, inst), \

220 .impl = &(CONN\_MGR\_CONN\_IMPL\_GET\_NAME(conn\_id)), \

221 .ctx = &(CONN\_MGR\_CONN\_BINDING\_GET\_DATA(dev\_id, inst)), \

222 .mutex = &(CONN\_MGR\_CONN\_BINDING\_GET\_MUTEX(dev\_id, inst)) \

223 };

224

[ 231](group__conn__mgr__connectivity__impl.md#ga16633bf29ebac6850b8c511b33bd189f)#define CONN\_MGR\_BIND\_CONN(dev\_id, conn\_id) \

232 CONN\_MGR\_BIND\_CONN\_INST(dev\_id, 0, conn\_id)

233

[ 245](group__conn__mgr__connectivity__impl.md#ga5fc0ba9d7bf365352e665d1c9a055889)static inline struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*[conn\_mgr\_if\_get\_binding](group__conn__mgr__connectivity__impl.md#ga5fc0ba9d7bf365352e665d1c9a055889)(struct [net\_if](structnet__if.md) \*[iface](structconn__mgr__conn__binding.md#a59bd71867b19e002c310d85496833e8f))

246{

247 [STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)([conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md), binding) {

248 if ([iface](structconn__mgr__conn__binding.md#a59bd71867b19e002c310d85496833e8f) == binding->iface) {

249 if (binding->impl->api) {

250 return binding;

251 }

252 return NULL;

253 }

254 }

255 return NULL;

256}

257

[ 270](group__conn__mgr__connectivity__impl.md#ga27be6dec40356facce7da18a31a2c12a)static inline void [conn\_mgr\_binding\_lock](group__conn__mgr__connectivity__impl.md#ga27be6dec40356facce7da18a31a2c12a)(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding)

271{

272 (void)[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)(binding->mutex, [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca));

273}

274

[ 286](group__conn__mgr__connectivity__impl.md#ga94a4930a6d7c4db4427dfdfad8f3c154)static inline void [conn\_mgr\_binding\_unlock](group__conn__mgr__connectivity__impl.md#ga94a4930a6d7c4db4427dfdfad8f3c154)(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding)

287{

288 (void)[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)(binding->mutex);

289}

290

[ 302](group__conn__mgr__connectivity__impl.md#ga4f0f3244f48c5e0204faf8278c2bd94f)static inline void [conn\_mgr\_binding\_set\_flag](group__conn__mgr__connectivity__impl.md#ga4f0f3244f48c5e0204faf8278c2bd94f)(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding,

303 enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag, bool value)

304{

305 [conn\_mgr\_binding\_lock](group__conn__mgr__connectivity__impl.md#ga27be6dec40356facce7da18a31a2c12a)(binding);

306

307 binding->[flags](structconn__mgr__conn__binding.md#a9b842340ebe872f30935b8f7e75d3605) &= [~BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(flag);

308 if (value) {

309 binding->[flags](structconn__mgr__conn__binding.md#a9b842340ebe872f30935b8f7e75d3605) |= [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(flag);

310 }

311

312 [conn\_mgr\_binding\_unlock](group__conn__mgr__connectivity__impl.md#ga94a4930a6d7c4db4427dfdfad8f3c154)(binding);

313}

314

[ 326](group__conn__mgr__connectivity__impl.md#ga128931a6fabce79829af5aebecd59985)static inline bool [conn\_mgr\_binding\_get\_flag](group__conn__mgr__connectivity__impl.md#ga128931a6fabce79829af5aebecd59985)(struct [conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md) \*binding,

327 enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag)

328{

329 bool value = false;

330

331 [conn\_mgr\_binding\_lock](group__conn__mgr__connectivity__impl.md#ga27be6dec40356facce7da18a31a2c12a)(binding);

332

333 value = !!(binding->[flags](structconn__mgr__conn__binding.md#a9b842340ebe872f30935b8f7e75d3605) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(flag));

334

335 [conn\_mgr\_binding\_unlock](group__conn__mgr__connectivity__impl.md#ga94a4930a6d7c4db4427dfdfad8f3c154)(binding);

336

337 return value;

338}

339

343

344#ifdef \_\_cplusplus

345}

346#endif

347

348#endif /\* ZEPHYR\_INCLUDE\_CONN\_MGR\_CONNECTIVITY\_IMPL\_H\_ \*/

[conn\_mgr\_connectivity.h](conn__mgr__connectivity_8h.md)

API for controlling generic network association routines on network devices that support it.

[device.h](device_8h.md)

[K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca)

#define K\_FOREVER

Generate infinite timeout delay.

**Definition** kernel.h:1440

[conn\_mgr\_binding\_get\_flag](group__conn__mgr__connectivity__impl.md#ga128931a6fabce79829af5aebecd59985)

static bool conn\_mgr\_binding\_get\_flag(struct conn\_mgr\_conn\_binding \*binding, enum conn\_mgr\_if\_flag flag)

Check the value of the specified connectivity flag for the provided binding.

**Definition** conn\_mgr\_connectivity\_impl.h:326

[conn\_mgr\_binding\_lock](group__conn__mgr__connectivity__impl.md#ga27be6dec40356facce7da18a31a2c12a)

static void conn\_mgr\_binding\_lock(struct conn\_mgr\_conn\_binding \*binding)

Lock the passed-in binding, making it safe to access.

**Definition** conn\_mgr\_connectivity\_impl.h:270

[conn\_mgr\_binding\_set\_flag](group__conn__mgr__connectivity__impl.md#ga4f0f3244f48c5e0204faf8278c2bd94f)

static void conn\_mgr\_binding\_set\_flag(struct conn\_mgr\_conn\_binding \*binding, enum conn\_mgr\_if\_flag flag, bool value)

Set the value of the specified connectivity flag for the provided binding.

**Definition** conn\_mgr\_connectivity\_impl.h:302

[conn\_mgr\_if\_get\_binding](group__conn__mgr__connectivity__impl.md#ga5fc0ba9d7bf365352e665d1c9a055889)

static struct conn\_mgr\_conn\_binding \* conn\_mgr\_if\_get\_binding(struct net\_if \*iface)

Retrieves the conn\_mgr binding struct for a provided iface if it exists.

**Definition** conn\_mgr\_connectivity\_impl.h:245

[conn\_mgr\_binding\_unlock](group__conn__mgr__connectivity__impl.md#ga94a4930a6d7c4db4427dfdfad8f3c154)

static void conn\_mgr\_binding\_unlock(struct conn\_mgr\_conn\_binding \*binding)

Unlocks the passed-in binding.

**Definition** conn\_mgr\_connectivity\_impl.h:286

[conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f)

conn\_mgr\_if\_flag

Per-iface connectivity flags.

**Definition** conn\_mgr\_connectivity.h:67

[STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)

#define STRUCT\_SECTION\_FOREACH(struct\_type, iterator)

Iterate over a specified iterable section.

**Definition** iterable\_sections.h:270

[k\_mutex\_unlock](group__mutex__apis.md#ga360f4c0e7258b0d7030cdb1f452b2c31)

int k\_mutex\_unlock(struct k\_mutex \*mutex)

Unlock a mutex.

[k\_mutex\_lock](group__mutex__apis.md#ga850549358645249c285669baa49c33b0)

int k\_mutex\_lock(struct k\_mutex \*mutex, k\_timeout\_t timeout)

Lock a mutex.

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[net\_if.h](net__if_8h.md)

Public API for network interface.

[net\_mgmt.h](net__mgmt_8h.md)

Network Management API public header.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[conn\_mgr\_conn\_api](structconn__mgr__conn__api.md)

Connectivity Manager Connectivity API structure.

**Definition** conn\_mgr\_connectivity\_impl.h:43

[conn\_mgr\_conn\_api::get\_opt](structconn__mgr__conn__api.md#a15d4bd909af1a2d3348fdec822bca7b7)

int(\* get\_opt)(struct conn\_mgr\_conn\_binding \*const binding, int optname, void \*optval, size\_t \*optlen)

Implementation callback for conn\_mgr\_if\_get\_opt.

**Definition** conn\_mgr\_connectivity\_impl.h:114

[conn\_mgr\_conn\_api::set\_opt](structconn__mgr__conn__api.md#a5636cced185825bd6c6997b427fd6121)

int(\* set\_opt)(struct conn\_mgr\_conn\_binding \*const binding, int optname, const void \*optval, size\_t optlen)

Implementation callback for conn\_mgr\_if\_set\_opt.

**Definition** conn\_mgr\_connectivity\_impl.h:96

[conn\_mgr\_conn\_api::connect](structconn__mgr__conn__api.md#a92064a4752f0c9621c5c6a745708a66e)

int(\* connect)(struct conn\_mgr\_conn\_binding \*const binding)

When called, the connectivity implementation should start attempting to establish connectivity (assoc...

**Definition** conn\_mgr\_connectivity\_impl.h:53

[conn\_mgr\_conn\_api::init](structconn__mgr__conn__api.md#ad2bb08d518e2f797002ca5257889a59e)

void(\* init)(struct conn\_mgr\_conn\_binding \*const binding)

Called once for each iface that has been bound to a connectivity implementation using this API.

**Definition** conn\_mgr\_connectivity\_impl.h:76

[conn\_mgr\_conn\_api::disconnect](structconn__mgr__conn__api.md#aee0d0fc9ef3361c8859b69128a087ba5)

int(\* disconnect)(struct conn\_mgr\_conn\_binding \*const binding)

When called, the connectivity implementation should disconnect (disassociate), or stop any in-progres...

**Definition** conn\_mgr\_connectivity\_impl.h:64

[conn\_mgr\_conn\_binding](structconn__mgr__conn__binding.md)

Connectivity Manager network interface binding structure.

**Definition** conn\_mgr\_connectivity\_impl.h:162

[conn\_mgr\_conn\_binding::impl](structconn__mgr__conn__binding.md#a288749353194206b8d8766f8f17aff48)

const struct conn\_mgr\_conn\_impl \* impl

The connectivity implementation the network device is bound to.

**Definition** conn\_mgr\_connectivity\_impl.h:167

[conn\_mgr\_conn\_binding::iface](structconn__mgr__conn__binding.md#a59bd71867b19e002c310d85496833e8f)

struct net\_if \* iface

The network interface the connectivity implementation is bound to.

**Definition** conn\_mgr\_connectivity\_impl.h:164

[conn\_mgr\_conn\_binding::timeout](structconn__mgr__conn__binding.md#a8474461cf7b00132441227aae07511ab)

int timeout

Timeout (seconds).

**Definition** conn\_mgr\_connectivity\_impl.h:196

[conn\_mgr\_conn\_binding::flags](structconn__mgr__conn__binding.md#a9b842340ebe872f30935b8f7e75d3605)

uint32\_t flags

Connectivity flags.

**Definition** conn\_mgr\_connectivity\_impl.h:183

[conn\_mgr\_conn\_binding::ctx](structconn__mgr__conn__binding.md#ad9102e2cf44b5940b21b1d160fea7611)

void \* ctx

Pointer to private, per-iface connectivity context.

**Definition** conn\_mgr\_connectivity\_impl.h:170

[conn\_mgr\_conn\_impl](structconn__mgr__conn__impl.md)

Connectivity Implementation struct.

**Definition** conn\_mgr\_connectivity\_impl.h:128

[conn\_mgr\_conn\_impl::api](structconn__mgr__conn__impl.md#a1229707a1b919659647412cb1eecd61b)

struct conn\_mgr\_conn\_api \* api

The connectivity API used by the implementation.

**Definition** conn\_mgr\_connectivity\_impl.h:130

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:680

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr\_connectivity\_impl.h](conn__mgr__connectivity__impl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
