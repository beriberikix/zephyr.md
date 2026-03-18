---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kernel_2thread_8h_source.html
original_path: doxygen/html/kernel_2thread_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

108 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) order\_key;

109

110#ifdef CONFIG\_SMP

111 /\* True for the per-CPU idle threads \*/

112 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) is\_idle;

113

114 /\* CPU index on which thread was last run \*/

115 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu;

116

117 /\* Recursive count of irq\_lock() calls \*/

118 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) global\_lock\_count;

119

120#endif /\* CONFIG\_SMP \*/

121

122#ifdef CONFIG\_SCHED\_CPU\_MASK

123 /\* "May run on" bits for each CPU \*/

124#if CONFIG\_MP\_MAX\_NUM\_CPUS <= 8

125 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cpu\_mask;

126#else

127 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cpu\_mask;

128#endif /\* CONFIG\_MP\_MAX\_NUM\_CPUS \*/

129#endif /\* CONFIG\_SCHED\_CPU\_MASK \*/

130

131 /\* data returned by APIs \*/

132 void \*swap\_data;

133

134#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

135 /\* this thread's entry in a timeout queue \*/

136 struct \_timeout timeout;

137#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

138

139#ifdef CONFIG\_TIMESLICE\_PER\_THREAD

140 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) slice\_ticks;

141 [k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f) slice\_expired;

142 void \*slice\_data;

143#endif /\* CONFIG\_TIMESLICE\_PER\_THREAD \*/

144

145#ifdef CONFIG\_SCHED\_THREAD\_USAGE

146 struct k\_cycle\_stats usage; /\* Track thread usage statistics \*/

147#endif /\* CONFIG\_SCHED\_THREAD\_USAGE \*/

148};

149

150typedef struct \_thread\_base \_thread\_base\_t;

151

152#if defined(CONFIG\_THREAD\_STACK\_INFO)

153/\* Contains the stack information of a thread \*/

154struct \_thread\_stack\_info {

155 /\* Stack start - Represents the start address of the thread-writable

156 \* stack area.

157 \*/

158 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start;

159

160 /\* Thread writable stack buffer size. Represents the size of the actual

161 \* buffer, starting from the 'start' member, that should be writable by

162 \* the thread. This comprises of the thread stack area, any area reserved

163 \* for local thread data storage, as well as any area left-out due to

164 \* random adjustments applied to the initial thread stack pointer during

165 \* thread initialization.

166 \*/

167 size\_t size;

168

169 /\* Adjustment value to the size member, removing any storage

170 \* used for TLS or random stack base offsets. (start + size - delta)

171 \* is the initial stack pointer for a thread. May be 0.

172 \*/

173 size\_t delta;

174

175#if defined(CONFIG\_THREAD\_STACK\_MEM\_MAPPED)

176 struct {

178 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*addr;

179

181 size\_t sz;

182 } mapped;

183#endif /\* CONFIG\_THREAD\_STACK\_MEM\_MAPPED \*/

184};

185

186typedef struct \_thread\_stack\_info \_thread\_stack\_info\_t;

187#endif /\* CONFIG\_THREAD\_STACK\_INFO \*/

188

189#if defined(CONFIG\_USERSPACE)

190struct \_mem\_domain\_info {

192 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) mem\_domain\_q\_node;

194 struct k\_mem\_domain \*mem\_domain;

195};

196

197#endif /\* CONFIG\_USERSPACE \*/

198

199#ifdef CONFIG\_THREAD\_USERSPACE\_LOCAL\_DATA

200struct \_thread\_userspace\_local\_data {

201#if defined(CONFIG\_ERRNO) && !defined(CONFIG\_ERRNO\_IN\_TLS) && !defined(CONFIG\_LIBC\_ERRNO)

202 int errno\_var;

203#endif /\* CONFIG\_ERRNO && !CONFIG\_ERRNO\_IN\_TLS && !CONFIG\_LIBC\_ERRNO \*/

204};

205#endif /\* CONFIG\_THREAD\_USERSPACE\_LOCAL\_DATA \*/

206

[ 207](structk__thread__runtime__stats.md)typedef struct [k\_thread\_runtime\_stats](structk__thread__runtime__stats.md) {

208#ifdef CONFIG\_SCHED\_THREAD\_USAGE

209 /\*

210 \* For CPU stats, execution\_cycles is the sum of non-idle + idle cycles.

211 \* For thread stats, execution\_cycles = total\_cycles.

212 \*/

213 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) execution\_cycles; /\* total # of cycles (cpu: non-idle + idle) \*/

214 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) total\_cycles; /\* total # of non-idle cycles \*/

215#endif /\* CONFIG\_SCHED\_THREAD\_USAGE \*/

216

217#ifdef CONFIG\_SCHED\_THREAD\_USAGE\_ANALYSIS

218 /\*

219 \* For threads, the following fields refer to the time spent executing

220 \* as bounded by when the thread was scheduled in and scheduled out.

221 \* For CPUs, the same fields refer to the time spent executing

222 \* non-idle threads as bounded by the idle thread(s).

223 \*/

224

225 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) current\_cycles; /\* current # of non-idle cycles \*/

226 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) peak\_cycles; /\* peak # of non-idle cycles \*/

227 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) average\_cycles; /\* average # of non-idle cycles \*/

228#endif /\* CONFIG\_SCHED\_THREAD\_USAGE\_ANALYSIS \*/

229

230#ifdef CONFIG\_SCHED\_THREAD\_USAGE\_ALL

231 /\*

232 \* This field is always zero for individual threads. It only comes

233 \* into play when gathering statistics for the CPU. In that case it

234 \* represents the total number of cycles spent idling.

235 \*/

236

237 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) idle\_cycles;

238#endif /\* CONFIG\_SCHED\_THREAD\_USAGE\_ALL \*/

239

240#if defined(\_\_cplusplus) && !defined(CONFIG\_SCHED\_THREAD\_USAGE) && \

241 !defined(CONFIG\_SCHED\_THREAD\_USAGE\_ANALYSIS) && !defined(CONFIG\_SCHED\_THREAD\_USAGE\_ALL)

242 /\* If none of the above Kconfig values are defined, this struct will have a size 0 in C

243 \* which is not allowed in C++ (it'll have a size 1). To prevent this, we add a 1 byte dummy

244 \* variable when the struct would otherwise be empty.

245 \*/

246 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dummy;

247#endif

[ 248](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf)} [k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf);

249

250struct z\_poller {

251 bool is\_polling;

252 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode;

253};

254

[ 259](structk__thread.md)struct [k\_thread](structk__thread.md) {

260

[ 261](structk__thread.md#a09a988f143ab5c4df887894920ff9df8) struct \_thread\_base [base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8);

262

[ 264](structk__thread.md#ae804efd7a191ed1022dd2cf5f588b0ef) struct \_callee\_saved [callee\_saved](structk__thread.md#ae804efd7a191ed1022dd2cf5f588b0ef);

265

[ 267](structk__thread.md#a315fe3ad42c5c4c15d4596e6ceaf0694) void \*[init\_data](structk__thread.md#a315fe3ad42c5c4c15d4596e6ceaf0694);

268

[ 270](structk__thread.md#aa8c560f5fbaf6cd551be99d491e654f6) \_wait\_q\_t [join\_queue](structk__thread.md#aa8c560f5fbaf6cd551be99d491e654f6);

271

272#if defined(CONFIG\_POLL)

273 struct z\_poller poller;

274#endif /\* CONFIG\_POLL \*/

275

276#if defined(CONFIG\_EVENTS)

277 struct [k\_thread](structk__thread.md) \*next\_event\_link;

278

279 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) events;

280 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_options;

281

283 bool no\_wake\_on\_timeout;

284#endif /\* CONFIG\_EVENTS \*/

285

286#if defined(CONFIG\_THREAD\_MONITOR)

[ 288](structk__thread.md#a63d78888376893fe0bdb485c5f114e03) struct \_\_thread\_entry [entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03);

289

[ 291](structk__thread.md#a0f0bf272e21ad4709082631a34a8b240) struct [k\_thread](structk__thread.md) \*[next\_thread](structk__thread.md#a0f0bf272e21ad4709082631a34a8b240);

292#endif /\* CONFIG\_THREAD\_MONITOR \*/

293

294#if defined(CONFIG\_THREAD\_NAME)

296 char name[CONFIG\_THREAD\_MAX\_NAME\_LEN];

297#endif /\* CONFIG\_THREAD\_NAME \*/

298

299#ifdef CONFIG\_THREAD\_CUSTOM\_DATA

[ 301](structk__thread.md#a459150bfd58cfb97eca88730eab7f325) void \*[custom\_data](structk__thread.md#a459150bfd58cfb97eca88730eab7f325);

302#endif /\* CONFIG\_THREAD\_CUSTOM\_DATA \*/

303

304#ifdef CONFIG\_THREAD\_USERSPACE\_LOCAL\_DATA

305 struct \_thread\_userspace\_local\_data \*userspace\_local\_data;

306#endif /\* CONFIG\_THREAD\_USERSPACE\_LOCAL\_DATA \*/

307

308#if defined(CONFIG\_ERRNO) && !defined(CONFIG\_ERRNO\_IN\_TLS) && !defined(CONFIG\_LIBC\_ERRNO)

309#ifndef CONFIG\_USERSPACE

311 int errno\_var;

312#endif /\* CONFIG\_USERSPACE \*/

313#endif /\* CONFIG\_ERRNO && !CONFIG\_ERRNO\_IN\_TLS && !CONFIG\_LIBC\_ERRNO \*/

314

315#if defined(CONFIG\_THREAD\_STACK\_INFO)

[ 317](structk__thread.md#a8be452e7b016fc901adad8518d7fe518) struct \_thread\_stack\_info [stack\_info](structk__thread.md#a8be452e7b016fc901adad8518d7fe518);

318#endif /\* CONFIG\_THREAD\_STACK\_INFO \*/

319

320#if defined(CONFIG\_USERSPACE)

[ 322](structk__thread.md#ab2fe91c58940a2f9d9cb7a30aa91cc55) struct \_mem\_domain\_info [mem\_domain\_info](structk__thread.md#ab2fe91c58940a2f9d9cb7a30aa91cc55);

323

[ 330](structk__thread.md#a40103270ef1e99a43e544b9a6737e96c) [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*[stack\_obj](structk__thread.md#a40103270ef1e99a43e544b9a6737e96c);

331

[ 333](structk__thread.md#a7a6114f1bf7993ad7f80a26f71e7a230) void \*[syscall\_frame](structk__thread.md#a7a6114f1bf7993ad7f80a26f71e7a230);

334#endif /\* CONFIG\_USERSPACE \*/

335

336

337#if defined(CONFIG\_USE\_SWITCH)

338 /\* When using \_\_switch() a few previously arch-specific items

339 \* become part of the core OS

340 \*/

341

[ 343](structk__thread.md#ae4cbe01f267cc15663c84c03d80aa3c1) int [swap\_retval](structk__thread.md#ae4cbe01f267cc15663c84c03d80aa3c1);

344

[ 346](structk__thread.md#a351c093c8f32f66ab62f364b477128c4) void \*[switch\_handle](structk__thread.md#a351c093c8f32f66ab62f364b477128c4);

347#endif /\* CONFIG\_USE\_SWITCH \*/

[ 349](structk__thread.md#a35b859bded3a270f25ccc40efece7583) struct [k\_heap](structk__heap.md) \*[resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583);

350

351#if defined(CONFIG\_THREAD\_LOCAL\_STORAGE)

352 /\* Pointer to arch-specific TLS area \*/

353 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) tls;

354#endif /\* CONFIG\_THREAD\_LOCAL\_STORAGE \*/

355

356#ifdef CONFIG\_DEMAND\_PAGING\_THREAD\_STATS

358 struct [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md) paging\_stats;

359#endif /\* CONFIG\_DEMAND\_PAGING\_THREAD\_STATS \*/

360

361#ifdef CONFIG\_PIPES

363 struct \_pipe\_desc pipe\_desc;

364#endif /\* CONFIG\_PIPES \*/

365

366#ifdef CONFIG\_OBJ\_CORE\_THREAD

367 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

368#endif /\* CONFIG\_OBJ\_CORE\_THREAD \*/

369

370#ifdef CONFIG\_SMP

[ 372](structk__thread.md#ab74f57fca0665fdd599f4f7c51a5d004) \_wait\_q\_t [halt\_queue](structk__thread.md#ab74f57fca0665fdd599f4f7c51a5d004);

373#endif /\* CONFIG\_SMP \*/

374

[ 376](structk__thread.md#a0fa3dd64d03f6eef06320b51b0623301) struct \_thread\_arch [arch](structk__thread.md#a0fa3dd64d03f6eef06320b51b0623301);

377};

378

379typedef struct [k\_thread](structk__thread.md) \_thread\_t;

[ 380](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)typedef struct [k\_thread](structk__thread.md) \*[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647);

381

382#endif /\* ZEPHYR\_INCLUDE\_KERNEL\_THREAD\_H\_ \*/

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

**Definition** thread.h:380

[k\_thread\_runtime\_stats\_t](kernel_2thread_8h.md#a887f70695cd229ea8f30ea3e1faf45cf)

struct k\_thread\_runtime\_stats k\_thread\_runtime\_stats\_t

[k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f)

void(\* k\_thread\_timeslice\_fn\_t)(struct k\_thread \*thread, void \*data)

**Definition** kernel\_structs.h:307

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

**Definition** kernel.h:5320

[k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md)

Paging Statistics.

**Definition** demand\_paging.h:37

[k\_obj\_core](structk__obj__core.md)

Object core structure.

**Definition** obj\_core.h:121

[k\_thread\_runtime\_stats](structk__thread__runtime__stats.md)

**Definition** thread.h:207

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[k\_thread::base](structk__thread.md#a09a988f143ab5c4df887894920ff9df8)

struct \_thread\_base base

**Definition** thread.h:261

[k\_thread::next\_thread](structk__thread.md#a0f0bf272e21ad4709082631a34a8b240)

struct k\_thread \* next\_thread

next item in list of all threads

**Definition** thread.h:291

[k\_thread::arch](structk__thread.md#a0fa3dd64d03f6eef06320b51b0623301)

struct \_thread\_arch arch

arch-specifics: must always be at the end

**Definition** thread.h:376

[k\_thread::init\_data](structk__thread.md#a315fe3ad42c5c4c15d4596e6ceaf0694)

void \* init\_data

static thread init data

**Definition** thread.h:267

[k\_thread::switch\_handle](structk__thread.md#a351c093c8f32f66ab62f364b477128c4)

void \* switch\_handle

Context handle returned via arch\_switch().

**Definition** thread.h:346

[k\_thread::resource\_pool](structk__thread.md#a35b859bded3a270f25ccc40efece7583)

struct k\_heap \* resource\_pool

resource pool

**Definition** thread.h:349

[k\_thread::stack\_obj](structk__thread.md#a40103270ef1e99a43e544b9a6737e96c)

k\_thread\_stack\_t \* stack\_obj

Base address of thread stack.

**Definition** thread.h:330

[k\_thread::custom\_data](structk__thread.md#a459150bfd58cfb97eca88730eab7f325)

void \* custom\_data

crude thread-local storage

**Definition** thread.h:301

[k\_thread::entry](structk__thread.md#a63d78888376893fe0bdb485c5f114e03)

struct \_\_thread\_entry entry

thread entry and parameters description

**Definition** thread.h:288

[k\_thread::syscall\_frame](structk__thread.md#a7a6114f1bf7993ad7f80a26f71e7a230)

void \* syscall\_frame

current syscall frame pointer

**Definition** thread.h:333

[k\_thread::stack\_info](structk__thread.md#a8be452e7b016fc901adad8518d7fe518)

struct \_thread\_stack\_info stack\_info

Stack Info.

**Definition** thread.h:317

[k\_thread::join\_queue](structk__thread.md#aa8c560f5fbaf6cd551be99d491e654f6)

\_wait\_q\_t join\_queue

threads waiting in k\_thread\_join()

**Definition** thread.h:270

[k\_thread::mem\_domain\_info](structk__thread.md#ab2fe91c58940a2f9d9cb7a30aa91cc55)

struct \_mem\_domain\_info mem\_domain\_info

memory domain info of the thread

**Definition** thread.h:322

[k\_thread::halt\_queue](structk__thread.md#ab74f57fca0665fdd599f4f7c51a5d004)

\_wait\_q\_t halt\_queue

threads waiting in k\_thread\_suspend()

**Definition** thread.h:372

[k\_thread::swap\_retval](structk__thread.md#ae4cbe01f267cc15663c84c03d80aa3c1)

int swap\_retval

z\_swap() return value

**Definition** thread.h:343

[k\_thread::callee\_saved](structk__thread.md#ae804efd7a191ed1022dd2cf5f588b0ef)

struct \_callee\_saved callee\_saved

defined by the architecture, but all archs need these

**Definition** thread.h:264

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [thread.h](kernel_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
