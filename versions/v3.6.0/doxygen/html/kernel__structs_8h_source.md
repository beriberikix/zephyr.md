---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kernel__structs_8h_source.html
original_path: doxygen/html/kernel__structs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

24#include <[zephyr/sys/atomic.h](atomic_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/kernel/internal/sched\_priq.h](sched__priq_8h.md)>

27#include <[zephyr/sys/dlist.h](dlist_8h.md)>

28#include <[zephyr/sys/util.h](util_8h.md)>

29#include <[zephyr/sys/sys\_heap.h](sys__heap_8h.md)>

30#include <[zephyr/arch/structs.h](structs_8h.md)>

31#include <[zephyr/kernel/stats.h](kernel_2stats_8h.md)>

32#include <[zephyr/kernel/obj\_core.h](obj__core_8h.md)>

33#endif

34

35#ifdef \_\_cplusplus

36extern "C" {

37#endif

38

39/\*

40 \* Bitmask definitions for the struct k\_thread.thread\_state field.

41 \*

42 \* Must be before kernel\_arch\_data.h because it might need them to be already

43 \* defined.

44 \*/

45

46/\* states: common uses low bits, arch-specific use high bits \*/

47

48/\* Not a real thread \*/

49#define \_THREAD\_DUMMY (BIT(0))

50

51/\* Thread is waiting on an object \*/

52#define \_THREAD\_PENDING (BIT(1))

53

54/\* Thread has not yet started \*/

55#define \_THREAD\_PRESTART (BIT(2))

56

57/\* Thread has terminated \*/

58#define \_THREAD\_DEAD (BIT(3))

59

60/\* Thread is suspended \*/

61#define \_THREAD\_SUSPENDED (BIT(4))

62

63/\* Thread is in the process of aborting \*/

64#define \_THREAD\_ABORTING (BIT(5))

65

66/\* Thread is in the process of suspending \*/

67#define \_THREAD\_SUSPENDING (BIT(6))

68

69/\* Thread is present in the ready queue \*/

70#define \_THREAD\_QUEUED (BIT(7))

71

72/\* end - states \*/

73

74#ifdef CONFIG\_STACK\_SENTINEL

75/\* Magic value in lowest bytes of the stack \*/

76#define STACK\_SENTINEL 0xF0F0F0F0

77#endif

78

79/\* lowest value of \_thread\_base.preempt at which a thread is non-preemptible \*/

80#define \_NON\_PREEMPT\_THRESHOLD 0x0080U

81

82/\* highest value of \_thread\_base.preempt at which a thread is preemptible \*/

83#define \_PREEMPT\_THRESHOLD (\_NON\_PREEMPT\_THRESHOLD - 1U)

84

85#if !defined(\_ASMLANGUAGE)

86

87struct \_ready\_q {

88#ifndef CONFIG\_SMP

89 /\* always contains next thread to run: cannot be NULL \*/

90 struct k\_thread \*cache;

91#endif

92

93#if defined(CONFIG\_SCHED\_DUMB)

94 [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) runq;

95#elif defined(CONFIG\_SCHED\_SCALABLE)

96 struct \_priq\_rb runq;

97#elif defined(CONFIG\_SCHED\_MULTIQ)

98 struct \_priq\_mq runq;

99#endif

100};

101

102typedef struct \_ready\_q \_ready\_q\_t;

103

104struct \_cpu {

105 /\* nested interrupt count \*/

106 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nested;

107

108 /\* interrupt stack pointer base \*/

109 char \*irq\_stack;

110

111 /\* currently scheduled thread \*/

112 struct k\_thread \*current;

113

114 /\* one assigned idle thread per CPU \*/

115 struct k\_thread \*idle\_thread;

116

117#ifdef CONFIG\_SCHED\_CPU\_MASK\_PIN\_ONLY

118 struct \_ready\_q ready\_q;

119#endif

120

121#if (CONFIG\_NUM\_METAIRQ\_PRIORITIES > 0) && \

122 (CONFIG\_NUM\_COOP\_PRIORITIES > CONFIG\_NUM\_METAIRQ\_PRIORITIES)

123 /\* Coop thread preempted by current metairq, or NULL \*/

124 struct k\_thread \*metairq\_preempted;

125#endif

126

127 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id;

128

129#if defined(CONFIG\_FPU\_SHARING)

130 void \*fp\_ctx;

131#endif

132

133#ifdef CONFIG\_SMP

134 /\* True when \_current is allowed to context switch \*/

135 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) swap\_ok;

136#endif

137

138#ifdef CONFIG\_SCHED\_THREAD\_USAGE

139 /\*

140 \* [usage0] is used as a timestamp to mark the beginning of an

141 \* execution window. [0] is a special value indicating that it

142 \* has been stopped (but not disabled).

143 \*/

144

145 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usage0;

146

147#ifdef CONFIG\_SCHED\_THREAD\_USAGE\_ALL

148 struct k\_cycle\_stats \*usage;

149#endif

150#endif

151

152#ifdef CONFIG\_OBJ\_CORE\_SYSTEM

153 struct k\_obj\_core obj\_core;

154#endif

155

156 /\* Per CPU architecture specifics \*/

157 struct \_cpu\_arch arch;

158};

159

160typedef struct \_cpu \_cpu\_t;

161

162struct z\_kernel {

163 struct \_cpu cpus[CONFIG\_MP\_MAX\_NUM\_CPUS];

164

165#ifdef CONFIG\_PM

166 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) idle; /\* Number of ticks for kernel idling \*/

167#endif

168

169 /\*

170 \* ready queue: can be big, keep after small fields, since some

171 \* assembly (e.g. ARC) are limited in the encoding of the offset

172 \*/

173#ifndef CONFIG\_SCHED\_CPU\_MASK\_PIN\_ONLY

174 struct \_ready\_q ready\_q;

175#endif

176

177#ifdef CONFIG\_FPU\_SHARING

178 /\*

179 \* A 'current\_sse' field does not exist in addition to the 'current\_fp'

180 \* field since it's not possible to divide the IA-32 non-integer

181 \* registers into 2 distinct blocks owned by differing threads. In

182 \* other words, given that the 'fxnsave/fxrstor' instructions

183 \* save/restore both the X87 FPU and XMM registers, it's not possible

184 \* for a thread to only "own" the XMM registers.

185 \*/

186

187 /\* thread that owns the FP regs \*/

188 struct k\_thread \*current\_fp;

189#endif

190

191#if defined(CONFIG\_THREAD\_MONITOR)

192 struct k\_thread \*threads; /\* singly linked list of ALL threads \*/

193#endif

194#ifdef CONFIG\_SCHED\_THREAD\_USAGE\_ALL

195 struct k\_cycle\_stats usage[CONFIG\_MP\_MAX\_NUM\_CPUS];

196#endif

197

198#ifdef CONFIG\_OBJ\_CORE\_SYSTEM

199 struct k\_obj\_core obj\_core;

200#endif

201

202#if defined(CONFIG\_SMP) && defined(CONFIG\_SCHED\_IPI\_SUPPORTED)

203 /\* Need to signal an IPI at the next scheduling point \*/

204 bool pending\_ipi;

205#endif

206};

207

208typedef struct z\_kernel \_kernel\_t;

209

210extern struct z\_kernel \_kernel;

211

212extern [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \_cpus\_active;

213

214#ifdef CONFIG\_SMP

215

216/\* True if the current context can be preempted and migrated to

217 \* another SMP CPU.

218 \*/

219bool z\_smp\_cpu\_mobile(void);

220

221#define \_current\_cpu ({ \_\_ASSERT\_NO\_MSG(!z\_smp\_cpu\_mobile()); \

222 arch\_curr\_cpu(); })

223#define \_current k\_sched\_current\_thread\_query()

224

225#else

226#define \_current\_cpu (&\_kernel.cpus[0])

227#define \_current \_kernel.cpus[0].current

228#endif

229

230/\* kernel wait queue record \*/

231

232#ifdef CONFIG\_WAITQ\_SCALABLE

233

234typedef struct {

235 struct \_priq\_rb waitq;

236} \_wait\_q\_t;

237

238bool z\_priq\_rb\_lessthan(struct [rbnode](structrbnode.md) \*a, struct [rbnode](structrbnode.md) \*b);

239

240#define Z\_WAIT\_Q\_INIT(wait\_q) { { { .lessthan\_fn = z\_priq\_rb\_lessthan } } }

241

242#else

243

244typedef struct {

245 [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) waitq;

246} \_wait\_q\_t;

247

248#define Z\_WAIT\_Q\_INIT(wait\_q) { SYS\_DLIST\_STATIC\_INIT(&(wait\_q)->waitq) }

249

250#endif

251

252/\* kernel timeout record \*/

253

254struct \_timeout;

255typedef void (\*\_timeout\_func\_t)(struct \_timeout \*t);

256

257struct \_timeout {

258 [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) node;

259 \_timeout\_func\_t fn;

260#ifdef CONFIG\_TIMEOUT\_64BIT

261 /\* Can't use k\_ticks\_t for header dependency reasons \*/

262 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) dticks;

263#else

264 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) dticks;

265#endif

266};

267

[ 268](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f)typedef void (\*[k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f))(struct [k\_thread](structk__thread.md) \*thread, void \*data);

269

270#ifdef \_\_cplusplus

271}

272#endif

273

274#endif /\* \_ASMLANGUAGE \*/

275

276#endif /\* ZEPHYR\_KERNEL\_INCLUDE\_KERNEL\_STRUCTS\_H\_ \*/

[atomic.h](atomic_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[dlist.h](dlist_8h.md)

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:55

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:51

[types.h](include_2zephyr_2types_8h.md)

[stats.h](kernel_2stats_8h.md)

[k\_thread\_timeslice\_fn\_t](kernel__structs_8h.md#a44c6f88a879877ad8da28706e274064f)

void(\* k\_thread\_timeslice\_fn\_t)(struct k\_thread \*thread, void \*data)

**Definition** kernel\_structs.h:268

[obj\_core.h](obj__core_8h.md)

[sched\_priq.h](sched__priq_8h.md)

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

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[rbnode](structrbnode.md)

Balanced red/black tree node structure.

**Definition** rb.h:58

[structs.h](structs_8h.md)

[sys\_heap.h](sys__heap_8h.md)

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel\_structs.h](kernel__structs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
