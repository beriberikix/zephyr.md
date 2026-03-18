---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/spsc__lockfree_8h_source.html
original_path: doxygen/html/spsc__lockfree_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spsc\_lockfree.h

[Go to the documentation of this file.](spsc__lockfree_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_SYS\_SPSC\_LOCKFREE\_H\_

8#define ZEPHYR\_SYS\_SPSC\_LOCKFREE\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[zephyr/toolchain/common.h](common_8h.md)>

13#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

14#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

15

22

52

59struct spsc {

60 /\* private value only the producer thread should mutate \*/

61 unsigned long acquire;

62

63 /\* private value only the consumer thread should mutate \*/

64 unsigned long consume;

65

66 /\* producer mutable, consumer readable \*/

67 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) in;

68

69 /\* consumer mutable, producer readable \*/

70 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) out;

71

72 /\* mask used to automatically wrap values \*/

73 const unsigned long mask;

74};

75

[ 82](group__spsc__lockfree.md#ga18aecd57468b7e6b3779c86952647238)#define SPSC\_INITIALIZER(sz, buf) \

83 { \

84 .\_spsc = \

85 { \

86 .acquire = 0, \

87 .consume = 0, \

88 .in = ATOMIC\_INIT(0), \

89 .out = ATOMIC\_INIT(0), \

90 .mask = sz - 1, \

91 }, \

92 .buffer = buf, \

93 }

94

[ 101](group__spsc__lockfree.md#gaef8a80e3a9bc0d30e1e3b29ff7b6ba85)#define SPSC\_DECLARE(name, type) \

102 static struct spsc\_##name { \

103 struct spsc \_spsc; \

104 type \* const buffer; \

105 }

106

[ 114](group__spsc__lockfree.md#ga8d1ccd780f9e0656fffc59ffc828fd1f)#define SPSC\_DEFINE(name, type, sz) \

115 BUILD\_ASSERT(IS\_POWER\_OF\_TWO(sz)); \

116 static type \_\_spsc\_buf\_##name[sz]; \

117 SPSC\_DECLARE(name, type) name = SPSC\_INITIALIZER(sz, \_\_spsc\_buf\_##name);

118

[ 124](group__spsc__lockfree.md#ga4b191cf95a0fdae8a197037ab252a58c)#define spsc\_size(spsc) ((spsc)->\_spsc.mask + 1)

125

133#define z\_spsc\_mask(spsc, i) ((i) & (spsc)->\_spsc.mask)

134

139#define z\_spsc\_in(spsc) (unsigned long)atomic\_get(&(spsc)->\_spsc.in)

140

145#define z\_spsc\_out(spsc) (unsigned long)atomic\_get(&(spsc)->\_spsc.out)

146

[ 155](group__spsc__lockfree.md#gaca6733f19cd9d05ff27176d3ef813490)#define spsc\_reset(spsc) \

156 ({ \

157 (spsc)->\_spsc.consume = 0; \

158 (spsc)->\_spsc.acquire = 0; \

159 atomic\_set(&(spsc)->\_spsc.in, 0); \

160 atomic\_set(&(spsc)->\_spsc.out, 0); \

161 })

162

[ 170](group__spsc__lockfree.md#gaa9e6c12ab0d83759b1387be9d299462d)#define spsc\_acquire(spsc) \

171 ({ \

172 unsigned long idx = z\_spsc\_in(spsc) + (spsc)->\_spsc.acquire; \

173 bool spsc\_acq = (idx - z\_spsc\_out(spsc)) < spsc\_size(spsc); \

174 if (spsc\_acq) { \

175 (spsc)->\_spsc.acquire += 1; \

176 } \

177 spsc\_acq ? &((spsc)->buffer[z\_spsc\_mask(spsc, idx)]) : NULL; \

178 })

179

[ 187](group__spsc__lockfree.md#ga8f3308d2e1ef28d29f9eabd46ed90bde)#define spsc\_produce(spsc) \

188 ({ \

189 if ((spsc)->\_spsc.acquire > 0) { \

190 (spsc)->\_spsc.acquire -= 1; \

191 atomic\_add(&(spsc)->\_spsc.in, 1); \

192 } \

193 })

194

[ 203](group__spsc__lockfree.md#ga971fea8aa902ccaac6a3ac787046d0cd)#define spsc\_produce\_all(spsc) \

204 ({ \

205 if ((spsc)->\_spsc.acquire > 0) { \

206 unsigned long acquired = (spsc)->\_spsc.acquire; \

207 (spsc)->\_spsc.acquire = 0; \

208 atomic\_add(&(spsc)->\_spsc.in, acquired); \

209 } \

210 })

211

[ 219](group__spsc__lockfree.md#ga30f61cd259725e8a06b920517d23df01)#define spsc\_drop\_all(spsc) \

220 do { \

221 (spsc)->\_spsc.acquire = 0; \

222 } while (false)

223

[ 231](group__spsc__lockfree.md#gacca4ce3da7128ecadb861b47bd55bf9b)#define spsc\_consume(spsc) \

232 ({ \

233 unsigned long idx = z\_spsc\_out(spsc) + (spsc)->\_spsc.consume; \

234 bool has\_consumable = (idx != z\_spsc\_in(spsc)); \

235 if (has\_consumable) { \

236 (spsc)->\_spsc.consume += 1; \

237 } \

238 has\_consumable ? &((spsc)->buffer[z\_spsc\_mask(spsc, idx)]) : NULL; \

239 })

240

[ 246](group__spsc__lockfree.md#ga4d20e781b0f811a08334375664d74726)#define spsc\_release(spsc) \

247 ({ \

248 if ((spsc)->\_spsc.consume > 0) { \

249 (spsc)->\_spsc.consume -= 1; \

250 atomic\_add(&(spsc)->\_spsc.out, 1); \

251 } \

252 })

253

[ 259](group__spsc__lockfree.md#ga624be14173fbb26c8b09e50e9e0d46a2)#define spsc\_release\_all(spsc) \

260 ({ \

261 if ((spsc)->\_spsc.consume > 0) { \

262 unsigned long consumed = (spsc)->\_spsc.consume; \

263 (spsc)->\_spsc.consume = 0; \

264 atomic\_add(&(spsc)->\_spsc.out, consumed); \

265 } \

266 })

267

[ 273](group__spsc__lockfree.md#ga2bed9808d75ed0617e4442fd6d69244c)#define spsc\_acquirable(spsc) \

274 ({ (((spsc)->\_spsc.in + (spsc)->\_spsc.acquire) - (spsc)->\_spsc.out) - spsc\_size(spsc); })

275

[ 281](group__spsc__lockfree.md#gae2b68434c49078b1a55930b4a99aacdf)#define spsc\_consumable(spsc) ({ (spsc)->\_spsc.in - (spsc)->\_spsc.out - (spsc)->\_spsc.consume; })

282

[ 290](group__spsc__lockfree.md#gac382c3a75dbc1df5d6d40df8c7d54266)#define spsc\_peek(spsc) \

291 ({ \

292 unsigned long idx = z\_spsc\_out(spsc) + (spsc)->\_spsc.consume; \

293 bool has\_consumable = (idx != z\_spsc\_in(spsc)); \

294 has\_consumable ? &((spsc)->buffer[z\_spsc\_mask(spsc, idx)]) : NULL; \

295 })

296

[ 306](group__spsc__lockfree.md#gaba7acaae1e0a8a9b82b73ed15acf89a9)#define spsc\_next(spsc, item) \

307 ({ \

308 unsigned long idx = ((item) - (spsc)->buffer); \

309 bool has\_next = \

310 z\_spsc\_mask(spsc, (idx + 1)) != (z\_spsc\_mask(spsc, z\_spsc\_in(spsc))); \

311 has\_next ? &((spsc)->buffer[z\_spsc\_mask((spsc), idx + 1)]) : NULL; \

312 })

313

[ 322](group__spsc__lockfree.md#gabdcbd5a0dc5ea88811967494361c0bfc)#define spsc\_prev(spsc, item) \

323 ({ \

324 unsigned long idx = ((item) - &(spsc)->buffer[0]) / sizeof((spsc)->buffer[0]); \

325 bool has\_prev = idx != z\_spsc\_mask(spsc, z\_spsc\_out(spsc)); \

326 has\_prev ? &((spsc)->buffer[z\_spsc\_mask(spsc, idx - 1)]) : NULL; \

327 })

328

332

333#endif /\* ZEPHYR\_SYS\_SPSC\_LOCKFREE\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[common.h](common_8h.md)

Common toolchain abstraction.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[atomic.h](sys_2atomic_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [spsc\_lockfree.h](spsc__lockfree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
