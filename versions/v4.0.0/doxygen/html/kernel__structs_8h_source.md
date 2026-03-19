---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/kernel__structs_8h_source.html
original_path: doxygen/html/kernel__structs_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kernel\_structs.h

[Go to the documentation of this file.](kernel__structs_8h.md)

1/\*

2 \* Copyright (c) 2016 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* The purpose of this file is to provide essential/minimal kernel structure

9 \* definitions, so that they can be used without including kernel.h.

10 \*

11 \* The following rules must be observed:

12 \* 1. kernel\_structs.h shall not depend on kernel.h both directly and

13 \* indirectly (i.e. it shall not include any header files that include

14 \* kernel.h in their dependency chain).

15 \* 2. kernel.h shall imply kernel\_structs.h, such that it shall not be

16 \* necessary to include kernel\_structs.h explicitly when kernel.h is

17 \* included.

18 \*/

19

20#ifndef ZEPHYR\_KERNEL\_INCLUDE\_KERNEL\_STRUCTS\_H\_

21#define ZEPHYR\_KERNEL\_INCLUDE\_KERNEL\_STRUCTS\_H\_

22

23#if !defined(\_ASMLANGUAGE)

24#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/sys/dlist.h](dlist_8h.md)>

27#include <[zephyr/sys/util.h](sys_2util_8h.md)>

28#include <[zephyr/sys/sys\_heap.h](sys__heap_8h.md)>

29#include <[zephyr/arch/structs.h](structs_8h.md)>

30#include <[zephyr/kernel/stats.h](kernel_2stats_8h.md)>

31#include <[zephyr/kernel/obj\_core.h](obj__core_8h.md)>

32#include <[zephyr/sys/rb.h](rb_8h.md)>

33#endif

34

[ 35](kernel__structs_8h.md#ae861b4805a52e8bd99d5481d3943dc5c)#define K\_NUM\_THREAD\_PRIO (CONFIG\_NUM\_PREEMPT\_PRIORITIES + CONFIG\_NUM\_COOP\_PRIORITIES + 1)

[ 36](kernel__structs_8h.md#a3fcfea2426c3da024f627c8ab9e754ad)#define PRIQ\_BITMAP\_SIZE (DIV\_ROUND\_UP(K\_NUM\_THREAD\_PRIO, BITS\_PER\_LONG))

37

38#ifdef \_\_cplusplus

39extern "C" {

40#endif

41

42/\*

43 \* Bitmask definitions for the struct k\_thread.thread\_state field.

44 \*

45 \* Must be before kernel\_arch\_data.h because it might need them to be already

46 \* defined.

47 \*/

48

49/\* states: common uses low bits, arch-specific use high bits \*/

50

51/\* Not a real thread \*/

52#define \_THREAD\_DUMMY (BIT(0))

53

54/\* Thread is waiting on an object \*/

55#define \_THREAD\_PENDING (BIT(1))

56

57/\* Thread has not yet started \*/

58#define \_THREAD\_PRESTART (BIT(2))

59

60/\* Thread has terminated \*/

61#define \_THREAD\_DEAD (BIT(3))

62

63/\* Thread is suspended \*/

64#define \_THREAD\_SUSPENDED (BIT(4))

65

66/\* Thread is in the process of aborting \*/

67#define \_THREAD\_ABORTING (BIT(5))

68

69/\* Thread is in the process of suspending \*/

70#define \_THREAD\_SUSPENDING (BIT(6))

71

72/\* Thread is present in the ready queue \*/

73#define \_THREAD\_QUEUED (BIT(7))

74

75/\* end - states \*/

76

77#ifdef CONFIG\_STACK\_SENTINEL

78/\* Magic value in lowest bytes of the stack \*/

79#define STACK\_SENTINEL 0xF0F0F0F0

80#endif

81

82/\* lowest value of \_thread\_base.preempt at which a thread is non-preemptible \*/

83#define \_NON\_PREEMPT\_THRESHOLD 0x0080U

84

85/\* highest value of \_thread\_base.preempt at which a thread is preemptible \*/

86#define \_PREEMPT\_THRESHOLD (\_NON\_PREEMPT\_THRESHOLD - 1U)

87

88#if !defined(\_ASMLANGUAGE)

89

90/\* Two abstractions are defined here for "thread priority queues".

91 \*

92 \* One is a "dumb" list implementation appropriate for systems with

93 \* small numbers of threads and sensitive to code size. It is stored

94 \* in sorted order, taking an O(N) cost every time a thread is added

95 \* to the list. This corresponds to the way the original \_wait\_q\_t

96 \* abstraction worked and is very fast as long as the number of

97 \* threads is small.

98 \*

99 \* The other is a balanced tree "fast" implementation with rather

100 \* larger code size (due to the data structure itself, the code here

101 \* is just stubs) and higher constant-factor performance overhead, but

102 \* much better O(logN) scaling in the presence of large number of

103 \* threads.

104 \*

105 \* Each can be used for either the wait\_q or system ready queue,

106 \* configurable at build time.

107 \*/

108

109struct \_priq\_rb {

110 struct [rbtree](structrbtree.md) tree;

111 int next\_order\_key;

112};

113

114

115/\* Traditional/textbook "multi-queue" structure. Separate lists for a

116 \* small number (max 32 here) of fixed priorities. This corresponds

117 \* to the original Zephyr scheduler. RAM requirements are

118 \* comparatively high, but performance is very fast. Won't work with

119 \* features like deadline scheduling which need large priority spaces

120 \* to represent their requirements.

121 \*/

122struct \_priq\_mq {

123 [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) queues[[K\_NUM\_THREAD\_PRIO](kernel__structs_8h.md#ae861b4805a52e8bd99d5481d3943dc5c)];

124 unsigned long bitmask[[PRIQ\_BITMAP\_SIZE](kernel__structs_8h.md#a3fcfea2426c3da024f627c8ab9e754ad)];

125};

126

127struct \_ready\_q {

128#ifndef CONFIG\_SMP

129 /\* always contains next thread to run: cannot be NULL \*/

130 struct [k\_thread](structk__thread.md) \*cache;

131#endif

132

133#if defined(CONFIG\_SCHED\_DUMB)

134 [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) runq;

135#elif defined(CONFIG\_SCHED\_SCALABLE)

136 struct \_priq\_rb runq;

137#elif defined(CONFIG\_SCHED\_MULTIQ)

138 struct \_priq\_mq runq;

139#endif

140};

141

142typedef struct \_ready\_q \_ready\_q\_t;

143

144struct \_cpu {

145 /\* nested interrupt count \*/

146 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nested;

147

148 /\* interrupt stack pointer base \*/

149 char \*irq\_stack;

150

151 /\* currently scheduled thread \*/

152 struct [k\_thread](structk__thread.md) \*current;

153

154 /\* one assigned idle thread per CPU \*/

155 struct [k\_thread](structk__thread.md) \*idle\_thread;

156

157#ifdef CONFIG\_SCHED\_CPU\_MASK\_PIN\_ONLY

158 struct \_ready\_q ready\_q;

159#endif

160

161#if (CONFIG\_NUM\_METAIRQ\_PRIORITIES > 0) && \

162 (CONFIG\_NUM\_COOP\_PRIORITIES > CONFIG\_NUM\_METAIRQ\_PRIORITIES)

163 /\* Coop thread preempted by current metairq, or NULL \*/

164 struct [k\_thread](structk__thread.md) \*metairq\_preempted;

165#endif

166

167 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id;

168

169#if defined(CONFIG\_FPU\_SHARING)

170 void \*fp\_ctx;

171#endif

172

173#ifdef CONFIG\_SMP

174 /\* True when \_current is allowed to context switch \*/

175 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) swap\_ok;

176#endif

177

178#ifdef CONFIG\_SCHED\_THREAD\_USAGE

179 /\*

180 \* [usage0] is used as a timestamp to mark the beginning of an

181 \* execution window. [0] is a special value indicating that it

182 \* has been stopped (but not disabled).

183 \*/

184

185 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usage0;

186

187#ifdef CONFIG\_SCHED\_THREAD\_USAGE\_ALL

188 struct [k\_cycle\_stats](structk__cycle__stats.md) \*usage;

189#endif

190#endif

191

192#ifdef CONFIG\_OBJ\_CORE\_SYSTEM

193 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

194#endif

195

196 /\* Per CPU architecture specifics \*/

197 struct \_cpu\_arch arch;

198};

199

200typedef struct \_cpu \_cpu\_t;

201

202struct z\_kernel {

203 struct \_cpu cpus[CONFIG\_MP\_MAX\_NUM\_CPUS];

204

205#ifdef CONFIG\_PM

206 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) idle; /\* Number of ticks for kernel idling \*/

207#endif

208

209 /\*

210 \* ready queue: can be big, keep after small fields, since some

211 \* assembly (e.g. ARC) are limited in the encoding of the offset

212 \*/

213#ifndef CONFIG\_SCHED\_CPU\_MASK\_PIN\_ONLY

214 struct \_ready\_q ready\_q;

215#endif

216

217#ifdef CONFIG\_FPU\_SHARING

218 /\*

219 \* A 'current\_sse' field does not exist in addition to the 'current\_fp'

220 \* field since it's not possible to divide the IA-32 non-integer

221 \* registers into 2 distinct blocks owned by differing threads. In

222 \* other words, given that the 'fxnsave/fxrstor' instructions

223 \* save/restore both the X87 FPU and XMM registers, it's not possible

224 \* for a thread to only "own" the XMM registers.

225 \*/

226

227 /\* thread that owns the FP regs \*/

228 struct [k\_thread](structk__thread.md) \*current\_fp;

229#endif

230

231#if defined(CONFIG\_THREAD\_MONITOR)

232 struct [k\_thread](structk__thread.md) \*threads; /\* singly linked list of ALL threads \*/

233#endif

234#ifdef CONFIG\_SCHED\_THREAD\_USAGE\_ALL

235 struct [k\_cycle\_stats](structk__cycle__stats.md) usage[CONFIG\_MP\_MAX\_NUM\_CPUS];

236#endif

237

238#ifdef CONFIG\_OBJ\_CORE\_SYSTEM

239 struct [k\_obj\_core](structk__obj__core.md) obj\_core;

240#endif

241

242#if defined(CONFIG\_SMP) && defined(CONFIG\_SCHED\_IPI\_SUPPORTED)

243 /\* Identify CPUs to send IPIs to at the next scheduling point \*/

244 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) pending\_ipi;

245#endif

246};

247

248typedef struct z\_kernel \_kernel\_t;

249

250extern struct z\_kernel \_kernel;

251

252extern [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \_cpus\_active;

253

254#ifdef CONFIG\_SMP

255

256/\* True if the current context can be preempted and migrated to

257 \* another SMP CPU.

258 \*/

259bool z\_smp\_cpu\_mobile(void);

260

261#define \_current\_cpu ({ \_\_ASSERT\_NO\_MSG(!z\_smp\_cpu\_mobile()); \

262 arch\_curr\_cpu(); })

263#define \_current k\_sched\_current\_thread\_query()

264

265#else

266#define \_current\_cpu (&\_kernel.cpus[0])

267#define \_current \_kernel.cpus[0].current

268#endif

269

270/\* kernel wait queue record \*/

271#ifdef CONFIG\_WAITQ\_SCALABLE

272

273typedef struct {

274 struct \_priq\_rb waitq;

275} \_wait\_q\_t;

276

277/\* defined in kernel/priority\_queues.c \*/

278bool z\_priq\_rb\_lessthan(struct [rbnode](structrbnode.md) \*a, struct [rbnode](structrbnode.md) \*b);

279

280#define Z\_WAIT\_Q\_INIT(wait\_q) { { { .lessthan\_fn = z\_priq\_rb\_lessthan } } }

281

282#else

283

284typedef struct {

285 [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) waitq;

286} \_wait\_q\_t;

287

288#define Z\_WAIT\_Q\_INIT(wait\_q) { SYS\_DLIST\_STATIC\_INIT(&(wait\_q)->waitq) }

289

290#endif /\* CONFIG\_WAITQ\_SCALABLE \*/

291

292/\* kernel timeout record \*/

293struct \_timeout;

294typedef void (\*\_timeout\_func\_t)(struct \_timeout \*t);

295

296struct \_timeout {

297 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) node;

298 \_timeout\_func\_t fn;

299#ifdef CONFIG\_TIMEOUT\_64BIT

300 /\* Can't use k\_ticks\_t for header dependency reasons \*/

301 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) dticks;

302#else

303 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) dticks;

304#endif

305};

306

[ 307](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f)typedef void (\*[k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f))(struct [k\_thread](structk__thread.md) \*thread, void \*data);

308

309#ifdef \_\_cplusplus

310}

311#endif

312

313#endif /\* \_ASMLANGUAGE \*/

314

315#endif /\* ZEPHYR\_KERNEL\_INCLUDE\_KERNEL\_STRUCTS\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[dlist.h](dlist_8h.md)

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:50

[types.h](include_2zephyr_2types_8h.md)

[stats.h](kernel_2stats_8h.md)

[PRIQ\_BITMAP\_SIZE](kernel__structs_8h.md#a3fcfea2426c3da024f627c8ab9e754ad)

#define PRIQ\_BITMAP\_SIZE

**Definition** kernel\_structs.h:36

[k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f)

void(\* k\_thread\_timeslice\_fn\_t)(struct k\_thread \*thread, void \*data)

**Definition** kernel\_structs.h:307

[K\_NUM\_THREAD\_PRIO](kernel__structs_8h.md#ae861b4805a52e8bd99d5481d3943dc5c)

#define K\_NUM\_THREAD\_PRIO

**Definition** kernel\_structs.h:35

[obj\_core.h](obj__core_8h.md)

[rb.h](rb_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[k\_cycle\_stats](structk__cycle__stats.md)

Structure used to track internal statistics about both thread and CPU usage.

**Definition** stats.h:18

[k\_obj\_core](structk__obj__core.md)

Object core structure.

**Definition** obj\_core.h:121

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[rbnode](structrbnode.md)

Balanced red/black tree node structure.

**Definition** rb.h:58

[rbtree](structrbtree.md)

Balanced red/black tree structure.

**Definition** rb.h:91

[structs.h](structs_8h.md)

[atomic.h](sys_2atomic_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[sys\_heap.h](sys__heap_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel\_structs.h](kernel__structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
