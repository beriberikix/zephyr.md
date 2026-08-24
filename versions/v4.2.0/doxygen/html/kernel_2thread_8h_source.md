---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/kernel_2thread_8h_source.html
original_path: doxygen/html/kernel_2thread_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](kernel_2thread_8h.md)

1/\*

2 \* Copyright (c) 2016, Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_KERNEL\_THREAD\_H\_

8#define ZEPHYR\_INCLUDE\_KERNEL\_THREAD\_H\_

9

10#ifdef CONFIG\_DEMAND\_PAGING\_THREAD\_STATS

11#include <[zephyr/kernel/mm/demand\_paging.h](demand__paging_8h.md)>

12#endif /\* CONFIG\_DEMAND\_PAGING\_THREAD\_STATS \*/

13

14#include <[zephyr/kernel/stats.h](kernel_2stats_8h.md)>

15#include <[zephyr/arch/arch\_interface.h](arch__interface_8h.md)>

16

33

34#ifdef CONFIG\_THREAD\_MONITOR

35struct \_\_thread\_entry {

36 [k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717) pEntry;

37 void \*parameter1;

38 void \*parameter2;

39 void \*parameter3;

40};

41#endif /\* CONFIG\_THREAD\_MONITOR \*/

42

43struct [k\_thread](structk__thread.md);

44

45/\*

46 \* This \_pipe\_desc structure is used by the pipes kernel module when

47 \* CONFIG\_PIPES has been selected.

48 \*/

49

50struct \_pipe\_desc {

51 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) node;

52 unsigned char \*buffer; /\* Position in src/dest buffer \*/

53 size\_t bytes\_to\_xfer; /\* # bytes left to transfer \*/

54 struct k\_thread \*thread; /\* Back pointer to pended thread \*/

55};

56

57/\* can be used for creating 'dummy' threads, e.g. for pending on objects \*/

58struct \_thread\_base {

59

60 /\* this thread's entry in a ready/wait queue \*/

61 union {

62 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) qnode\_dlist;

63 struct rbnode qnode\_rb;

64 };

65

66 /\* wait queue on which the thread is pended (needed only for

67 \* trees, not dumb lists)

68 \*/

69 \_wait\_q\_t \*pended\_on;

70

71 /\* user facing 'thread options'; values defined in include/kernel.h \*/

72 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) user\_options;

73

74 /\* thread state \*/

75 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) thread\_state;

76

77 /\*

78 \* scheduler lock count and thread priority

79 \*

80 \* These two fields control the preemptibility of a thread.

81 \*

82 \* When the scheduler is locked, sched\_locked is decremented, which

83 \* means that the scheduler is locked for values from 0xff to 0x01. A

84 \* thread is coop if its prio is negative, thus 0x80 to 0xff when

85 \* looked at the value as unsigned.

86 \*

87 \* By putting them end-to-end, this means that a thread is

88 \* non-preemptible if the bundled value is greater than or equal to

89 \* 0x0080.

90 \*/

91 union {

92 struct {

93#ifdef CONFIG\_BIG\_ENDIAN

94 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sched\_locked;

95 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio;

96#else /\* Little Endian \*/

97 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) prio;

98 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sched\_locked;

99#endif /\* CONFIG\_BIG\_ENDIAN \*/

100 };

101 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) preempt;

102 };

103

104#ifdef CONFIG\_SCHED\_DEADLINE

105 int prio\_deadline;

106#endif /\* CONFIG\_SCHED\_DEADLINE \*/

107

108#if defined(CONFIG\_SCHED\_SCALABLE) || defined(CONFIG\_WAITQ\_SCALABLE)

109 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) order\_key;

110#endif

111

112#ifdef CONFIG\_SMP

113 /\* True for the per-CPU idle threads \*/

114 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) is\_idle;

115

116 /\* CPU index on which thread was last run \*/

117 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu;

118

119 /\* Recursive count of irq\_lock() calls \*/

120 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) global\_lock\_count;

121

122#endif /\* CONFIG\_SMP \*/

123

124#ifdef CONFIG\_SCHED\_CPU\_MASK

125 /\* "May run on" bits for each CPU \*/

126#if CONFIG\_MP\_MAX\_NUM\_CPUS <= 8

127 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu\_mask;

128#else

129 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cpu\_mask;

130#endif /\* CONFIG\_MP\_MAX\_NUM\_CPUS \*/

131#endif /\* CONFIG\_SCHED\_CPU\_MASK \*/

132

133 /\* data returned by APIs \*/

134 void \*swap\_data;

135

136#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

137 /\* this thread's entry in a timeout queue \*/

138 struct \_timeout timeout;

139#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

140

141#ifdef CONFIG\_TIMESLICE\_PER\_THREAD

142 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice\_ticks;

143 [k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f) slice\_expired;

144 void \*slice\_data;

145#endif /\* CONFIG\_TIMESLICE\_PER\_THREAD \*/

146

147#ifdef CONFIG\_SCHED\_THREAD\_USAGE

148 struct k\_cycle\_stats usage; /\* Track thread usage statistics \*/

149#endif /\* CONFIG\_SCHED\_THREAD\_USAGE \*/

150};

151

152typedef struct \_thread\_base \_thread\_base\_t;

153

154#if defined(CONFIG\_THREAD\_STACK\_INFO)

155/\* Contains the stack information of a thread \*/

156struct \_thread\_stack\_info {

157 /\* Stack start - Represents the start address of the thread-writable

158 \* stack area.

159 \*/

160 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start;

161

162 /\* Thread writable stack buffer size. Represents the size of the actual

163 \* buffer, starting from the 'start' member, that should be writable by

164 \* the thread. This comprises of the thread stack area, any area reserved

165 \* for local thread data storage, as well as any area left-out due to

166 \* random adjustments applied to the initial thread stack pointer during

167 \* thread initialization.

168 \*/

169 size\_t size;

170

171 /\* Adjustment value to the size member, removing any storage

172 \* used for TLS or random stack base offsets. (start + size - delta)

173 \* is the initial stack pointer for a thread. May be 0.

174 \*/

175 size\_t delta;

176

177#if defined(CONFIG\_THREAD\_STACK\_MEM\_MAPPED)

178 struct {

180 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*addr;

181

183 size\_t sz;

184 } mapped;

185#endif /\* CONFIG\_THREAD\_STACK\_MEM\_MAPPED \*/

186};

187

188typedef struct \_thread\_stack\_info \_thread\_stack\_info\_t;

189#endif /\* CONFIG\_THREAD\_STACK\_INFO \*/

190

191#if defined(CONFIG\_USERSPACE)

192struct \_mem\_domain\_info {

194 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) mem\_domain\_q\_node;

196 struct k\_mem\_domain \*mem\_domain;

197};

198

199typedef struct \_mem\_domain\_info \_mem\_domain\_info\_t;

200#endif /\* CONFIG\_USERSPACE \*/

201

202#ifdef CONFIG\_THREAD\_USERSPACE\_LOCAL\_DATA

203struct \_thread\_userspace\_local\_data {

204#if defined(CONFIG\_ERRNO) && !defined(CONFIG\_ERRNO\_IN\_TLS) && !defined(CONFIG\_LIBC\_ERRNO)

205 int errno\_var;

206#endif /\* CONFIG\_ERRNO && !CONFIG\_ERRNO\_IN\_TLS && !CONFIG\_LIBC\_ERRNO \*/

207};

208#endif /\* CONFIG\_THREAD\_USERSPACE\_LOCAL\_DATA \*/

209

[ 210](structk__thread__runtime__stats.md)typedef struct [k\_thread\_runtime\_stats](structk__thread__runtime__stats.md) {

211#ifdef CONFIG\_SCHED\_THREAD\_USAGE

212 /\*

213 \* For CPU stats, execution\_cycles is the sum of non-idle + idle cycles.

214 \* For thread stats, execution\_cycles = total\_cycles.

215 \*/

216 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) execution\_cycles; /\* total # of cycles (cpu: non-idle + idle) \*/

217 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) total\_cycles; /\* total # of non-idle cycles \*/

218#endif /\* CONFIG\_SCHED\_THREAD\_USAGE \*/

219

220#ifdef CONFIG\_SCHED\_THREAD\_USAGE\_ANALYSIS

221 /\*

222 \* For threads, the following fields refer to the time spent executing

223 \* as bounded by when the thread was scheduled in and scheduled out.

224 \* For CPUs, the same fields refer to the time spent executing

225 \* non-idle threads as bounded by the idle thread(s).

226 \*/

227

228 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) current\_cycles; /\* current # of non-idle cycles \*/

229 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) peak\_cycles; /\* peak # of non-idle cycles \*/

230 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) average\_cycles; /\* average # of non-idle cycles \*/

231#endif /\* CONFIG\_SCHED\_THREAD\_USAGE\_ANALYSIS \*/

232

233#ifdef CONFIG\_SCHED\_THREAD\_USAGE\_ALL

234 /\*

235 \* This field is always zero for individual threads. It only comes

236 \* into play when gathering statistics for the CPU. In that case it

237 \* represents the total number of cycles spent idling.

238 \*/

239

240 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) idle\_cycles;

241#endif /\* CONFIG\_SCHED\_THREAD\_USAGE\_ALL \*/

242

243#if defined(\_\_cplusplus) && !defined(CONFIG\_SCHED\_THREAD\_USAGE) && \

244 !defined(CONFIG\_SCHED\_THREAD\_USAGE\_ANALYSIS) && !defined(CONFIG\_SCHED\_THREAD\_USAGE\_ALL)

245 /\* If none of the above Kconfig values are defined, this struct will have a size 0 in C

246 \* which is not allowed in C++ (it'll have a size 1). To prevent this, we add a 1 byte dummy

247 \* variable when the struct would otherwise be empty.

248 \*/

249 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dummy;

250#endif

[ 251](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf)} [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf);

252

253struct z\_poller {

254 bool is\_polling;

255 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode;

256};

257

[ 262](structk__thread.md)struct [k\_thread](structk__thread.md) {

263

[ 264](structk__thread.md#a09a988f143ab5c4df887894920ff9df8) struct \_thread\_base [base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8);

265

[ 267](structk__thread.md#ae804efd7a191ed1022dd2cf5f588b0ef) struct \_callee\_saved [callee\_saved](structk__thread.md#ae804efd7a191ed1022dd2cf5f588b0ef);

268

[ 270](structk__thread.md#a315fe3ad42c5c4c15d4596e6ceaf0694) void \*[init\_data](structk__thread.md#a315fe3ad42c5c4c15d4596e6ceaf0694);

271

[ 273](structk__thread.md#aa8c560f5fbaf6cd551be99d491e654f6) \_wait\_q\_t [join\_queue](structk__thread.md#aa8c560f5fbaf6cd551be99d491e654f6);

274

275#if defined(CONFIG\_POLL)

276 struct z\_poller poller;

277#endif /\* CONFIG\_POLL \*/

278

279#if defined(CONFIG\_EVENTS)

280 struct [k\_thread](structk__thread.md) \*next\_event\_link;

281

282 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events;

283 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_options;

284

286 bool no\_wake\_on\_timeout;

287#endif /\* CONFIG\_EVENTS \*/

288

289#if defined(CONFIG\_THREAD\_MONITOR)

[ 291](structk__thread.md#a63d78888376893fe0bdb485c5f114e03) struct \_\_thread\_entry [entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03);

292

[ 294](structk__thread.md#a0f0bf272e21ad4709082631a34a8b240) struct [k\_thread](structk__thread.md) \*[next\_thread](structk__thread.md#a0f0bf272e21ad4709082631a34a8b240);

295#endif /\* CONFIG\_THREAD\_MONITOR \*/

296

297#if defined(CONFIG\_THREAD\_NAME)

299 char name[CONFIG\_THREAD\_MAX\_NAME\_LEN];

300#endif /\* CONFIG\_THREAD\_NAME \*/

301

302#ifdef CONFIG\_THREAD\_CUSTOM\_DATA

[ 304](structk__thread.md#a459150bfd58cfb97eca88730eab7f325) void \*[custom\_data](structk__thread.md#a459150bfd58cfb97eca88730eab7f325);

305#endif /\* CONFIG\_THREAD\_CUSTOM\_DATA \*/

306

307#ifdef CONFIG\_THREAD\_USERSPACE\_LOCAL\_DATA

308 struct \_thread\_userspace\_local\_data \*userspace\_local\_data;

309#endif /\* CONFIG\_THREAD\_USERSPACE\_LOCAL\_DATA \*/

310

311#if defined(CONFIG\_ERRNO) && !defined(CONFIG\_ERRNO\_IN\_TLS) && !defined(CONFIG\_LIBC\_ERRNO)

312#ifndef CONFIG\_USERSPACE

314 int errno\_var;

315#endif /\* CONFIG\_USERSPACE \*/

316#endif /\* CONFIG\_ERRNO && !CONFIG\_ERRNO\_IN\_TLS && !CONFIG\_LIBC\_ERRNO \*/

317

318#if defined(CONFIG\_THREAD\_STACK\_INFO)

[ 320](structk__thread.md#a8be452e7b016fc901adad8518d7fe518) struct \_thread\_stack\_info [stack\_info](structk__thread.md#a8be452e7b016fc901adad8518d7fe518);

321#endif /\* CONFIG\_THREAD\_STACK\_INFO \*/

322

323#if defined(CONFIG\_USERSPACE)

[ 325](structk__thread.md#ab2fe91c58940a2f9d9cb7a30aa91cc55) struct \_mem\_domain\_info [mem\_domain\_info](structk__thread.md#ab2fe91c58940a2f9d9cb7a30aa91cc55);

326

[ 333](structk__thread.md#a40103270ef1e99a43e544b9a6737e96c) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack\_obj](structk__thread.md#a40103270ef1e99a43e544b9a6737e96c);

334

[ 336](structk__thread.md#a7a6114f1bf7993ad7f80a26f71e7a230) void \*[syscall\_frame](structk__thread.md#a7a6114f1bf7993ad7f80a26f71e7a230);

337#endif /\* CONFIG\_USERSPACE \*/

338

339

340#if defined(CONFIG\_USE\_SWITCH)

341 /\* When using \_\_switch() a few previously arch-specific items

342 \* become part of the core OS

343 \*/

344

[ 346](structk__thread.md#ae4cbe01f267cc15663c84c03d80aa3c1) int [swap\_retval](structk__thread.md#ae4cbe01f267cc15663c84c03d80aa3c1);

347

[ 349](structk__thread.md#a351c093c8f32f66ab62f364b477128c4) void \*[switch\_handle](structk__thread.md#a351c093c8f32f66ab62f364b477128c4);

350#endif /\* CONFIG\_USE\_SWITCH \*/

[ 352](structk__thread.md#a35b859bded3a270f25ccc40efece7583) struct [k\_heap](structk__heap.md) \*[resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583);

353

354#if defined(CONFIG\_THREAD\_LOCAL\_STORAGE)

355 /\* Pointer to arch-specific TLS area \*/

356 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) tls;

357#endif /\* CONFIG\_THREAD\_LOCAL\_STORAGE \*/

358

359#ifdef CONFIG\_DEMAND\_PAGING\_THREAD\_STATS

361 struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) paging\_stats;

362#endif /\* CONFIG\_DEMAND\_PAGING\_THREAD\_STATS \*/

363

364#ifdef CONFIG\_PIPES

366 struct \_pipe\_desc pipe\_desc;

367#endif /\* CONFIG\_PIPES \*/

368

369#ifdef CONFIG\_OBJ\_CORE\_THREAD

370 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

371#endif /\* CONFIG\_OBJ\_CORE\_THREAD \*/

372

373#ifdef CONFIG\_SMP

[ 375](structk__thread.md#ab74f57fca0665fdd599f4f7c51a5d004) \_wait\_q\_t [halt\_queue](structk__thread.md#ab74f57fca0665fdd599f4f7c51a5d004);

376#endif /\* CONFIG\_SMP \*/

377

[ 379](structk__thread.md#a0fa3dd64d03f6eef06320b51b0623301) struct \_thread\_arch [arch](structk__thread.md#a0fa3dd64d03f6eef06320b51b0623301);

380};

381

382typedef struct [k\_thread](structk__thread.md) \_thread\_t;

[ 383](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)typedef struct [k\_thread](structk__thread.md) \*[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647);

384

385#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_THREAD\_H\_ \*/

[arch\_interface.h](arch__interface_8h.md)

[k\_thread\_entry\_t](arch__interface_8h.md#a3707e886593b0a8b4995309e4230b717)

void(\* k\_thread\_entry\_t)(void \*p1, void \*p2, void \*p3)

Thread entry point function type.

**Definition** arch\_interface.h:48

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[demand\_paging.h](demand__paging_8h.md)

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[stats.h](kernel_2stats_8h.md)

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:383

[k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf)

struct k\_thread\_runtime\_stats k\_thread\_runtime\_stats\_t

[k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f)

void(\* k\_thread\_timeslice\_fn\_t)(struct k\_thread \*thread, void \*data)

**Definition** kernel\_structs.h:310

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[k\_heap](structk__heap.md)

**Definition** kernel.h:5712

[k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md)

Paging Statistics.

**Definition** demand\_paging.h:37

[k\_obj\_core](structk__obj__core.md)

Object core structure.

**Definition** obj\_core.h:121

[k\_thread\_runtime\_stats](structk__thread__runtime__stats.md)

**Definition** thread.h:210

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:262

[k\_thread::base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8)

struct \_thread\_base base

**Definition** thread.h:264

[k\_thread::next\_thread](structk__thread.md#a0f0bf272e21ad4709082631a34a8b240)

struct k\_thread \* next\_thread

next item in list of all threads

**Definition** thread.h:294

[k\_thread::arch](structk__thread.md#a0fa3dd64d03f6eef06320b51b0623301)

struct \_thread\_arch arch

arch-specifics: must always be at the end

**Definition** thread.h:379

[k\_thread::init\_data](structk__thread.md#a315fe3ad42c5c4c15d4596e6ceaf0694)

void \* init\_data

static thread init data

**Definition** thread.h:270

[k\_thread::switch\_handle](structk__thread.md#a351c093c8f32f66ab62f364b477128c4)

void \* switch\_handle

Context handle returned via arch\_switch().

**Definition** thread.h:349

[k\_thread::resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583)

struct k\_heap \* resource\_pool

resource pool

**Definition** thread.h:352

[k\_thread::stack\_obj](structk__thread.md#a40103270ef1e99a43e544b9a6737e96c)

k\_thread\_stack\_t \* stack\_obj

Base address of thread stack.

**Definition** thread.h:333

[k\_thread::custom\_data](structk__thread.md#a459150bfd58cfb97eca88730eab7f325)

void \* custom\_data

crude thread-local storage

**Definition** thread.h:304

[k\_thread::entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03)

struct \_\_thread\_entry entry

thread entry and parameters description

**Definition** thread.h:291

[k\_thread::syscall\_frame](structk__thread.md#a7a6114f1bf7993ad7f80a26f71e7a230)

void \* syscall\_frame

current syscall frame pointer

**Definition** thread.h:336

[k\_thread::stack\_info](structk__thread.md#a8be452e7b016fc901adad8518d7fe518)

struct \_thread\_stack\_info stack\_info

Stack Info.

**Definition** thread.h:320

[k\_thread::join\_queue](structk__thread.md#aa8c560f5fbaf6cd551be99d491e654f6)

\_wait\_q\_t join\_queue

threads waiting in k\_thread\_join()

**Definition** thread.h:273

[k\_thread::mem\_domain\_info](structk__thread.md#ab2fe91c58940a2f9d9cb7a30aa91cc55)

struct \_mem\_domain\_info mem\_domain\_info

memory domain info of the thread

**Definition** thread.h:325

[k\_thread::halt\_queue](structk__thread.md#ab74f57fca0665fdd599f4f7c51a5d004)

\_wait\_q\_t halt\_queue

threads waiting in k\_thread\_suspend()

**Definition** thread.h:375

[k\_thread::swap\_retval](structk__thread.md#ae4cbe01f267cc15663c84c03d80aa3c1)

int swap\_retval

z\_swap() return value

**Definition** thread.h:346

[k\_thread::callee\_saved](structk__thread.md#ae804efd7a191ed1022dd2cf5f588b0ef)

struct \_callee\_saved callee\_saved

defined by the architecture, but all archs need these

**Definition** thread.h:267

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [thread.h](kernel_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
