---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__backend_8h_source.html
original_path: doxygen/html/log__backend_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend.h

[Go to the documentation of this file.](log__backend_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_BACKEND\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_BACKEND\_H\_

8

9#include <[zephyr/logging/log\_msg.h](log__msg_8h.md)>

10#include <stdarg.h>

11#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

12#include <[zephyr/sys/util.h](sys_2util_8h.md)>

13#include <[zephyr/logging/log\_output.h](log__output_8h.md)>

14#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

26

27/\* Forward declaration of the log\_backend type. \*/

28struct [log\_backend](structlog__backend.md);

29

30

[ 34](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6)enum [log\_backend\_evt](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6) {

[ 46](group__log__backend.md#gga04ebbd4416c907e60e05f0364f3bd2f6a559c37c58daf13a14f7b43440556f3d3) [LOG\_BACKEND\_EVT\_PROCESS\_THREAD\_DONE](group__log__backend.md#gga04ebbd4416c907e60e05f0364f3bd2f6a559c37c58daf13a14f7b43440556f3d3),

47

[ 49](group__log__backend.md#gga04ebbd4416c907e60e05f0364f3bd2f6abbc925931ad8098f3cee651fadd5432a) [LOG\_BACKEND\_EVT\_MAX](group__log__backend.md#gga04ebbd4416c907e60e05f0364f3bd2f6abbc925931ad8098f3cee651fadd5432a),

50};

51

[ 55](unionlog__backend__evt__arg.md)union [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) {

[ 57](unionlog__backend__evt__arg.md#a15cdd9e9541fd0949e87255073bad60b) void \*[raw](unionlog__backend__evt__arg.md#a15cdd9e9541fd0949e87255073bad60b);

58};

59

[ 63](structlog__backend__api.md)struct [log\_backend\_api](structlog__backend__api.md) {

[ 64](structlog__backend__api.md#a5d2d50961d28d0e2d2fdaacf79e5e9c8) void (\*[process](structlog__backend__api.md#a5d2d50961d28d0e2d2fdaacf79e5e9c8))(const struct [log\_backend](structlog__backend.md) \*const backend,

65 union [log\_msg\_generic](unionlog__msg__generic.md) \*msg);

66

[ 67](structlog__backend__api.md#a849b25667c299c4a7a97f598a1b2fbd7) void (\*[dropped](structlog__backend__api.md#a849b25667c299c4a7a97f598a1b2fbd7))(const struct [log\_backend](structlog__backend.md) \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt);

[ 68](structlog__backend__api.md#a04bdb8030ad4e70000d8572a6b7e07b1) void (\*[panic](structlog__backend__api.md#a04bdb8030ad4e70000d8572a6b7e07b1))(const struct [log\_backend](structlog__backend.md) \*const backend);

[ 69](structlog__backend__api.md#addc850f99813854df8083a5ee93a36c8) void (\*[init](structlog__backend__api.md#addc850f99813854df8083a5ee93a36c8))(const struct [log\_backend](structlog__backend.md) \*const backend);

[ 70](structlog__backend__api.md#ac0b3ea89a08df5d4d81b75075c876a18) int (\*[is\_ready](structlog__backend__api.md#ac0b3ea89a08df5d4d81b75075c876a18))(const struct [log\_backend](structlog__backend.md) \*const backend);

[ 71](structlog__backend__api.md#ae23c17899721f8254a9f50bedd667226) int (\*[format\_set](structlog__backend__api.md#ae23c17899721f8254a9f50bedd667226))(const struct [log\_backend](structlog__backend.md) \*const backend,

72 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type);

73

[ 74](structlog__backend__api.md#a656e284fd28781a582072bf39ab2ea40) void (\*[notify](structlog__backend__api.md#a656e284fd28781a582072bf39ab2ea40))(const struct [log\_backend](structlog__backend.md) \*const backend,

75 enum [log\_backend\_evt](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6) event,

76 union [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) \*arg);

77};

78

[ 82](structlog__backend__control__block.md)struct [log\_backend\_control\_block](structlog__backend__control__block.md) {

[ 83](structlog__backend__control__block.md#afe83e2bdd97c544905b913eb81676eb4) void \*[ctx](structlog__backend__control__block.md#afe83e2bdd97c544905b913eb81676eb4);

[ 84](structlog__backend__control__block.md#a0024522b0ae3dd547f048752e7dd047e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structlog__backend__control__block.md#a0024522b0ae3dd547f048752e7dd047e);

[ 85](structlog__backend__control__block.md#a99528f4b8d70d7c882c7c1b81b62a168) bool [active](structlog__backend__control__block.md#a99528f4b8d70d7c882c7c1b81b62a168);

86

87 /\* Initialization level. \*/

[ 88](structlog__backend__control__block.md#aa024c78a507c89056cd634f3a190efec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [level](structlog__backend__control__block.md#aa024c78a507c89056cd634f3a190efec);

89};

90

[ 94](structlog__backend.md)struct [log\_backend](structlog__backend.md) {

[ 95](structlog__backend.md#a87067e427a94d3543c7c50b950649b33) const struct [log\_backend\_api](structlog__backend__api.md) \*[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33);

[ 96](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d) struct [log\_backend\_control\_block](structlog__backend__control__block.md) \*[cb](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d);

[ 97](structlog__backend.md#a22b343a8fc32b9aa05f5f4649d78f7d4) const char \*[name](structlog__backend.md#a22b343a8fc32b9aa05f5f4649d78f7d4);

[ 98](structlog__backend.md#afe5ce6ac891bef0264dabafe18db88a2) bool [autostart](structlog__backend.md#afe5ce6ac891bef0264dabafe18db88a2);

99};

100

[ 110](group__log__backend.md#ga3a4cc530530d1a8b33dc787842bba119)#define LOG\_BACKEND\_DEFINE(\_name, \_api, \_autostart, ...) \

111 static struct log\_backend\_control\_block UTIL\_CAT(backend\_cb\_, \_name) = \

112 { \

113 COND\_CODE\_0(NUM\_VA\_ARGS\_LESS\_1(\_, ##\_\_VA\_ARGS\_\_), \

114 (), (.ctx = \_\_VA\_ARGS\_\_,)) \

115 .id = 0, \

116 .active = false, \

117 }; \

118 static const STRUCT\_SECTION\_ITERABLE(log\_backend, \_name) = \

119 { \

120 .api = &\_api, \

121 .cb = &UTIL\_CAT(backend\_cb\_, \_name), \

122 .name = STRINGIFY(\_name), \

123 .autostart = \_autostart \

124 }

125

126

[ 137](group__log__backend.md#ga017a2b54d367db037cce31b2693af98c)static inline void [log\_backend\_init](group__log__backend.md#ga017a2b54d367db037cce31b2693af98c)(const struct [log\_backend](structlog__backend.md) \*const backend)

138{

139 \_\_ASSERT\_NO\_MSG(backend != NULL);

140 if (backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[init](structlog__backend__api.md#addc850f99813854df8083a5ee93a36c8)) {

141 backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[init](structlog__backend__api.md#addc850f99813854df8083a5ee93a36c8)(backend);

142 }

143}

144

[ 156](group__log__backend.md#gaf57e7a27a1337815338410db93603e0b)static inline int [log\_backend\_is\_ready](group__log__backend.md#gaf57e7a27a1337815338410db93603e0b)(const struct [log\_backend](structlog__backend.md) \*const backend)

157{

158 \_\_ASSERT\_NO\_MSG(backend != NULL);

159 if (backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[is\_ready](structlog__backend__api.md#ac0b3ea89a08df5d4d81b75075c876a18) != NULL) {

160 return backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[is\_ready](structlog__backend__api.md#ac0b3ea89a08df5d4d81b75075c876a18)(backend);

161 }

162

163 return 0;

164}

165

[ 175](group__log__backend.md#ga388b0f33208ef1389640836d0bc23d17)static inline void [log\_backend\_msg\_process](group__log__backend.md#ga388b0f33208ef1389640836d0bc23d17)(const struct [log\_backend](structlog__backend.md) \*const backend,

176 union [log\_msg\_generic](unionlog__msg__generic.md) \*msg)

177{

178 \_\_ASSERT\_NO\_MSG(backend != NULL);

179 \_\_ASSERT\_NO\_MSG(msg != NULL);

180 backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[process](structlog__backend__api.md#a5d2d50961d28d0e2d2fdaacf79e5e9c8)(backend, msg);

181}

182

[ 191](group__log__backend.md#gab300348c43168de1e7eaae8c770b6950)static inline void [log\_backend\_dropped](group__log__backend.md#gab300348c43168de1e7eaae8c770b6950)(const struct [log\_backend](structlog__backend.md) \*const backend,

192 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt)

193{

194 \_\_ASSERT\_NO\_MSG(backend != NULL);

195

196 if (backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[dropped](structlog__backend__api.md#a849b25667c299c4a7a97f598a1b2fbd7) != NULL) {

197 backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[dropped](structlog__backend__api.md#a849b25667c299c4a7a97f598a1b2fbd7)(backend, cnt);

198 }

199}

200

[ 206](group__log__backend.md#gad12906ffa810514c1d43cb26bba5ea4b)static inline void [log\_backend\_panic](group__log__backend.md#gad12906ffa810514c1d43cb26bba5ea4b)(const struct [log\_backend](structlog__backend.md) \*const backend)

207{

208 \_\_ASSERT\_NO\_MSG(backend != NULL);

209 backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[panic](structlog__backend__api.md#a04bdb8030ad4e70000d8572a6b7e07b1)(backend);

210}

211

[ 220](group__log__backend.md#ga8f263b24140229e5cf8e98b322501bca)static inline void [log\_backend\_id\_set](group__log__backend.md#ga8f263b24140229e5cf8e98b322501bca)(const struct [log\_backend](structlog__backend.md) \*const backend,

221 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id)

222{

223 \_\_ASSERT\_NO\_MSG(backend != NULL);

224 backend->[cb](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d)->[id](structlog__backend__control__block.md#a0024522b0ae3dd547f048752e7dd047e) = [id](structlog__backend__control__block.md#a0024522b0ae3dd547f048752e7dd047e);

225}

226

[ 235](group__log__backend.md#gae3e1d6eaf21dcc1d0961e85271d5e5f3)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [log\_backend\_id\_get](group__log__backend.md#gae3e1d6eaf21dcc1d0961e85271d5e5f3)(const struct [log\_backend](structlog__backend.md) \*const backend)

236{

237 \_\_ASSERT\_NO\_MSG(backend != NULL);

238 return backend->[cb](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d)->[id](structlog__backend__control__block.md#a0024522b0ae3dd547f048752e7dd047e);

239}

240

[ 248](group__log__backend.md#gaf419f3590f42893b7091beed57763c7c)static inline const struct [log\_backend](structlog__backend.md) \*[log\_backend\_get](group__log__backend.md#gaf419f3590f42893b7091beed57763c7c)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx)

249{

250 const struct [log\_backend](structlog__backend.md) \*backend;

251

252 [STRUCT\_SECTION\_GET](group__iterable__section__apis.md#ga583e57b527884034116bf0b27a942b50)([log\_backend](structlog__backend.md), idx, &backend);

253

254 return backend;

255}

256

[ 262](group__log__backend.md#gad055c1dc8e0236b604cb553df3e16a52)static inline int [log\_backend\_count\_get](group__log__backend.md#gad055c1dc8e0236b604cb553df3e16a52)(void)

263{

264 int cnt;

265

266 [STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)([log\_backend](structlog__backend.md), &cnt);

267

268 return cnt;

269}

270

[ 277](group__log__backend.md#ga3ef0b88b4118f7ee04749ace2646c99b)static inline void [log\_backend\_activate](group__log__backend.md#ga3ef0b88b4118f7ee04749ace2646c99b)(const struct [log\_backend](structlog__backend.md) \*const backend,

278 void \*ctx)

279{

280 \_\_ASSERT\_NO\_MSG(backend != NULL);

281 backend->[cb](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d)->[ctx](structlog__backend__control__block.md#afe83e2bdd97c544905b913eb81676eb4) = ctx;

282 backend->[cb](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d)->[active](structlog__backend__control__block.md#a99528f4b8d70d7c882c7c1b81b62a168) = true;

283}

284

[ 290](group__log__backend.md#ga1534fdfabce1e97c829aa79d57739589)static inline void [log\_backend\_deactivate](group__log__backend.md#ga1534fdfabce1e97c829aa79d57739589)(

291 const struct [log\_backend](structlog__backend.md) \*const backend)

292{

293 \_\_ASSERT\_NO\_MSG(backend != NULL);

294 backend->[cb](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d)->[active](structlog__backend__control__block.md#a99528f4b8d70d7c882c7c1b81b62a168) = false;

295}

296

[ 304](group__log__backend.md#ga54dd06d48edf92ef191dab946aead216)static inline bool [log\_backend\_is\_active](group__log__backend.md#ga54dd06d48edf92ef191dab946aead216)(

305 const struct [log\_backend](structlog__backend.md) \*const backend)

306{

307 \_\_ASSERT\_NO\_MSG(backend != NULL);

308 return backend->[cb](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d)->[active](structlog__backend__control__block.md#a99528f4b8d70d7c882c7c1b81b62a168);

309}

310

[ 320](group__log__backend.md#gac0a4dc476c3b641ab570ca2dd4f2096f)static inline int [log\_backend\_format\_set](group__log__backend.md#gac0a4dc476c3b641ab570ca2dd4f2096f)(const struct [log\_backend](structlog__backend.md) \*backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type)

321{

322 extern size\_t log\_format\_table\_size(void);

323

324 if ((size\_t)log\_type >= log\_format\_table\_size()) {

325 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

326 }

327

328 if ([log\_format\_func\_t\_get](group__log__output.md#gad4a212bb513f85aecb55b2ffcc3920eb)(log\_type) == NULL) {

329 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

330 }

331

332 if (backend == NULL) {

333 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

334 }

335

336 if (backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[format\_set](structlog__backend__api.md#ae23c17899721f8254a9f50bedd667226) == NULL) {

337 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

338 }

339

340 return backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[format\_set](structlog__backend__api.md#ae23c17899721f8254a9f50bedd667226)(backend, log\_type);

341}

342

[ 350](group__log__backend.md#gae8203fcde52fee405a4b2e973c989ec7)static inline void [log\_backend\_notify](group__log__backend.md#gae8203fcde52fee405a4b2e973c989ec7)(const struct [log\_backend](structlog__backend.md) \*const backend,

351 enum [log\_backend\_evt](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6) event,

352 union [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) \*arg)

353{

354 \_\_ASSERT\_NO\_MSG(backend != NULL);

355

356 if (backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[notify](structlog__backend__api.md#a656e284fd28781a582072bf39ab2ea40)) {

357 backend->[api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)->[notify](structlog__backend__api.md#a656e284fd28781a582072bf39ab2ea40)(backend, event, arg);

358 }

359}

360

364

365#ifdef \_\_cplusplus

366}

367#endif

368

369#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_BACKEND\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[STRUCT\_SECTION\_GET](group__iterable__section__apis.md#ga583e57b527884034116bf0b27a942b50)

#define STRUCT\_SECTION\_GET(struct\_type, i, dst)

Get element from section.

**Definition** iterable\_sections.h:282

[STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)

#define STRUCT\_SECTION\_COUNT(struct\_type, dst)

Count elements in a section.

**Definition** iterable\_sections.h:291

[log\_backend\_init](group__log__backend.md#ga017a2b54d367db037cce31b2693af98c)

static void log\_backend\_init(const struct log\_backend \*const backend)

Initialize or initiate the logging backend.

**Definition** log\_backend.h:137

[log\_backend\_evt](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6)

log\_backend\_evt

Backend events.

**Definition** log\_backend.h:34

[log\_backend\_deactivate](group__log__backend.md#ga1534fdfabce1e97c829aa79d57739589)

static void log\_backend\_deactivate(const struct log\_backend \*const backend)

Deactivate backend.

**Definition** log\_backend.h:290

[log\_backend\_msg\_process](group__log__backend.md#ga388b0f33208ef1389640836d0bc23d17)

static void log\_backend\_msg\_process(const struct log\_backend \*const backend, union log\_msg\_generic \*msg)

Process message.

**Definition** log\_backend.h:175

[log\_backend\_activate](group__log__backend.md#ga3ef0b88b4118f7ee04749ace2646c99b)

static void log\_backend\_activate(const struct log\_backend \*const backend, void \*ctx)

Activate backend.

**Definition** log\_backend.h:277

[log\_backend\_is\_active](group__log__backend.md#ga54dd06d48edf92ef191dab946aead216)

static bool log\_backend\_is\_active(const struct log\_backend \*const backend)

Check state of the backend.

**Definition** log\_backend.h:304

[log\_backend\_id\_set](group__log__backend.md#ga8f263b24140229e5cf8e98b322501bca)

static void log\_backend\_id\_set(const struct log\_backend \*const backend, uint8\_t id)

Set backend id.

**Definition** log\_backend.h:220

[log\_backend\_dropped](group__log__backend.md#gab300348c43168de1e7eaae8c770b6950)

static void log\_backend\_dropped(const struct log\_backend \*const backend, uint32\_t cnt)

Notify backend about dropped log messages.

**Definition** log\_backend.h:191

[log\_backend\_format\_set](group__log__backend.md#gac0a4dc476c3b641ab570ca2dd4f2096f)

static int log\_backend\_format\_set(const struct log\_backend \*backend, uint32\_t log\_type)

Set logging format.

**Definition** log\_backend.h:320

[log\_backend\_count\_get](group__log__backend.md#gad055c1dc8e0236b604cb553df3e16a52)

static int log\_backend\_count\_get(void)

Get number of backends.

**Definition** log\_backend.h:262

[log\_backend\_panic](group__log__backend.md#gad12906ffa810514c1d43cb26bba5ea4b)

static void log\_backend\_panic(const struct log\_backend \*const backend)

Reconfigure backend to panic mode.

**Definition** log\_backend.h:206

[log\_backend\_id\_get](group__log__backend.md#gae3e1d6eaf21dcc1d0961e85271d5e5f3)

static uint8\_t log\_backend\_id\_get(const struct log\_backend \*const backend)

Get backend id.

**Definition** log\_backend.h:235

[log\_backend\_notify](group__log__backend.md#gae8203fcde52fee405a4b2e973c989ec7)

static void log\_backend\_notify(const struct log\_backend \*const backend, enum log\_backend\_evt event, union log\_backend\_evt\_arg \*arg)

Notify a backend of an event.

**Definition** log\_backend.h:350

[log\_backend\_get](group__log__backend.md#gaf419f3590f42893b7091beed57763c7c)

static const struct log\_backend \* log\_backend\_get(uint32\_t idx)

Get backend.

**Definition** log\_backend.h:248

[log\_backend\_is\_ready](group__log__backend.md#gaf57e7a27a1337815338410db93603e0b)

static int log\_backend\_is\_ready(const struct log\_backend \*const backend)

Poll for backend readiness.

**Definition** log\_backend.h:156

[LOG\_BACKEND\_EVT\_PROCESS\_THREAD\_DONE](group__log__backend.md#gga04ebbd4416c907e60e05f0364f3bd2f6a559c37c58daf13a14f7b43440556f3d3)

@ LOG\_BACKEND\_EVT\_PROCESS\_THREAD\_DONE

Event when process thread finishes processing.

**Definition** log\_backend.h:46

[LOG\_BACKEND\_EVT\_MAX](group__log__backend.md#gga04ebbd4416c907e60e05f0364f3bd2f6abbc925931ad8098f3cee651fadd5432a)

@ LOG\_BACKEND\_EVT\_MAX

Maximum number of backend events.

**Definition** log\_backend.h:49

[log\_format\_func\_t\_get](group__log__output.md#gad4a212bb513f85aecb55b2ffcc3920eb)

log\_format\_func\_t log\_format\_func\_t\_get(uint32\_t log\_type)

Declaration of the get routine for function pointer table format\_table.

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[log\_msg.h](log__msg_8h.md)

[log\_output.h](log__output_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[log\_backend\_api](structlog__backend__api.md)

Logger backend API.

**Definition** log\_backend.h:63

[log\_backend\_api::panic](structlog__backend__api.md#a04bdb8030ad4e70000d8572a6b7e07b1)

void(\* panic)(const struct log\_backend \*const backend)

**Definition** log\_backend.h:68

[log\_backend\_api::process](structlog__backend__api.md#a5d2d50961d28d0e2d2fdaacf79e5e9c8)

void(\* process)(const struct log\_backend \*const backend, union log\_msg\_generic \*msg)

**Definition** log\_backend.h:64

[log\_backend\_api::notify](structlog__backend__api.md#a656e284fd28781a582072bf39ab2ea40)

void(\* notify)(const struct log\_backend \*const backend, enum log\_backend\_evt event, union log\_backend\_evt\_arg \*arg)

**Definition** log\_backend.h:74

[log\_backend\_api::dropped](structlog__backend__api.md#a849b25667c299c4a7a97f598a1b2fbd7)

void(\* dropped)(const struct log\_backend \*const backend, uint32\_t cnt)

**Definition** log\_backend.h:67

[log\_backend\_api::is\_ready](structlog__backend__api.md#ac0b3ea89a08df5d4d81b75075c876a18)

int(\* is\_ready)(const struct log\_backend \*const backend)

**Definition** log\_backend.h:70

[log\_backend\_api::init](structlog__backend__api.md#addc850f99813854df8083a5ee93a36c8)

void(\* init)(const struct log\_backend \*const backend)

**Definition** log\_backend.h:69

[log\_backend\_api::format\_set](structlog__backend__api.md#ae23c17899721f8254a9f50bedd667226)

int(\* format\_set)(const struct log\_backend \*const backend, uint32\_t log\_type)

**Definition** log\_backend.h:71

[log\_backend\_control\_block](structlog__backend__control__block.md)

Logger backend control block.

**Definition** log\_backend.h:82

[log\_backend\_control\_block::id](structlog__backend__control__block.md#a0024522b0ae3dd547f048752e7dd047e)

uint8\_t id

**Definition** log\_backend.h:84

[log\_backend\_control\_block::active](structlog__backend__control__block.md#a99528f4b8d70d7c882c7c1b81b62a168)

bool active

**Definition** log\_backend.h:85

[log\_backend\_control\_block::level](structlog__backend__control__block.md#aa024c78a507c89056cd634f3a190efec)

uint8\_t level

**Definition** log\_backend.h:88

[log\_backend\_control\_block::ctx](structlog__backend__control__block.md#afe83e2bdd97c544905b913eb81676eb4)

void \* ctx

**Definition** log\_backend.h:83

[log\_backend](structlog__backend.md)

Logger backend structure.

**Definition** log\_backend.h:94

[log\_backend::name](structlog__backend.md#a22b343a8fc32b9aa05f5f4649d78f7d4)

const char \* name

**Definition** log\_backend.h:97

[log\_backend::api](structlog__backend.md#a87067e427a94d3543c7c50b950649b33)

const struct log\_backend\_api \* api

**Definition** log\_backend.h:95

[log\_backend::cb](structlog__backend.md#ab8c377e796af0ef81dcf459eeee56a1d)

struct log\_backend\_control\_block \* cb

**Definition** log\_backend.h:96

[log\_backend::autostart](structlog__backend.md#afe5ce6ac891bef0264dabafe18db88a2)

bool autostart

**Definition** log\_backend.h:98

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[log\_backend\_evt\_arg](unionlog__backend__evt__arg.md)

Argument(s) for backend events.

**Definition** log\_backend.h:55

[log\_backend\_evt\_arg::raw](unionlog__backend__evt__arg.md#a15cdd9e9541fd0949e87255073bad60b)

void \* raw

Unspecified argument(s).

**Definition** log\_backend.h:57

[log\_msg\_generic](unionlog__msg__generic.md)

**Definition** log\_msg.h:117

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend.h](log__backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
