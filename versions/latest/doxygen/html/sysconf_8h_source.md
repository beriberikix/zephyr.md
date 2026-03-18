---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sysconf_8h_source.html
original_path: doxygen/html/sysconf_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sysconf.h

[Go to the documentation of this file.](sysconf_8h.md)

1/\*

2 \* Copyright (c) 2024, Meta

3 \* Copyright (c) 2024, Tenstorrent AI ULC

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_SYSCONF\_H\_

8#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_SYSCONF\_H\_

9

10#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

16enum {

17 \_SC\_ADVISORY\_INFO,

18 \_SC\_ASYNCHRONOUS\_IO,

19 \_SC\_BARRIERS,

20 \_SC\_CLOCK\_SELECTION,

21 \_SC\_CPUTIME,

22 \_SC\_FSYNC,

23 \_SC\_IPV6,

24 \_SC\_JOB\_CONTROL,

25 \_SC\_MAPPED\_FILES,

26 \_SC\_MEMLOCK,

27 \_SC\_MEMLOCK\_RANGE,

28 \_SC\_MEMORY\_PROTECTION,

29 \_SC\_MESSAGE\_PASSING,

30 \_SC\_MONOTONIC\_CLOCK,

31 \_SC\_PRIORITIZED\_IO,

32 \_SC\_PRIORITY\_SCHEDULING,

33 \_SC\_RAW\_SOCKETS,

34 \_SC\_RE\_DUP\_MAX,

35 \_SC\_READER\_WRITER\_LOCKS,

36 \_SC\_REALTIME\_SIGNALS,

37 \_SC\_REGEXP,

38 \_SC\_SAVED\_IDS,

39 \_SC\_SEMAPHORES,

40 \_SC\_SHARED\_MEMORY\_OBJECTS,

41 \_SC\_SHELL,

42 \_SC\_SPAWN,

43 \_SC\_SPIN\_LOCKS,

44 \_SC\_SPORADIC\_SERVER,

45 \_SC\_SS\_REPL\_MAX,

46 \_SC\_SYNCHRONIZED\_IO,

47 \_SC\_THREAD\_ATTR\_STACKADDR,

48 \_SC\_THREAD\_ATTR\_STACKSIZE,

49 \_SC\_THREAD\_CPUTIME,

50 \_SC\_THREAD\_PRIO\_INHERIT,

51 \_SC\_THREAD\_PRIO\_PROTECT,

52 \_SC\_THREAD\_PRIORITY\_SCHEDULING,

53 \_SC\_THREAD\_PROCESS\_SHARED,

54 \_SC\_THREAD\_ROBUST\_PRIO\_INHERIT,

55 \_SC\_THREAD\_ROBUST\_PRIO\_PROTECT,

56 \_SC\_THREAD\_SAFE\_FUNCTIONS,

57 \_SC\_THREAD\_SPORADIC\_SERVER,

58 \_SC\_THREADS,

59 \_SC\_TIMEOUTS,

60 \_SC\_TIMERS,

61 \_SC\_TRACE,

62 \_SC\_TRACE\_EVENT\_FILTER,

63 \_SC\_TRACE\_EVENT\_NAME\_MAX,

64 \_SC\_TRACE\_INHERIT,

65 \_SC\_TRACE\_LOG,

66 \_SC\_TRACE\_NAME\_MAX,

67 \_SC\_TRACE\_SYS\_MAX,

68 \_SC\_TRACE\_USER\_EVENT\_MAX,

69 \_SC\_TYPED\_MEMORY\_OBJECTS,

70 \_SC\_VERSION,

71 \_SC\_V7\_ILP32\_OFF32,

72 \_SC\_V7\_ILP32\_OFFBIG,

73 \_SC\_V7\_LP64\_OFF64,

74 \_SC\_V7\_LPBIG\_OFFBIG,

75 \_SC\_V6\_ILP32\_OFF32,

76 \_SC\_V6\_ILP32\_OFFBIG,

77 \_SC\_V6\_LP64\_OFF64,

78 \_SC\_V6\_LPBIG\_OFFBIG,

79 \_SC\_BC\_BASE\_MAX,

80 \_SC\_BC\_DIM\_MAX,

81 \_SC\_BC\_SCALE\_MAX,

82 \_SC\_BC\_STRING\_MAX,

83 \_SC\_2\_C\_BIND,

84 \_SC\_2\_C\_DEV,

85 \_SC\_2\_CHAR\_TERM,

86 \_SC\_COLL\_WEIGHTS\_MAX,

87 \_SC\_DELAYTIMER\_MAX,

88 \_SC\_EXPR\_NEST\_MAX,

89 \_SC\_2\_FORT\_DEV,

90 \_SC\_2\_FORT\_RUN,

91 \_SC\_LINE\_MAX,

92 \_SC\_2\_LOCALEDEF,

93 \_SC\_2\_PBS,

94 \_SC\_2\_PBS\_ACCOUNTING,

95 \_SC\_2\_PBS\_CHECKPOINT,

96 \_SC\_2\_PBS\_LOCATE,

97 \_SC\_2\_PBS\_MESSAGE,

98 \_SC\_2\_PBS\_TRACK,

99 \_SC\_2\_SW\_DEV,

100 \_SC\_2\_UPE,

101 \_SC\_2\_VERSION,

102 \_SC\_XOPEN\_CRYPT,

103 \_SC\_XOPEN\_ENH\_I18N,

104 \_SC\_XOPEN\_REALTIME,

105 \_SC\_XOPEN\_REALTIME\_THREADS,

106 \_SC\_XOPEN\_SHM,

107 \_SC\_XOPEN\_STREAMS,

108 \_SC\_XOPEN\_UNIX,

109 \_SC\_XOPEN\_UUCP,

110 \_SC\_XOPEN\_VERSION,

111 \_SC\_CLK\_TCK,

112 \_SC\_GETGR\_R\_SIZE\_MAX,

113 \_SC\_GETPW\_R\_SIZE\_MAX,

114 \_SC\_AIO\_LISTIO\_MAX,

115 \_SC\_AIO\_MAX,

116 \_SC\_AIO\_PRIO\_DELTA\_MAX,

117 \_SC\_ARG\_MAX,

118 \_SC\_ATEXIT\_MAX,

119 \_SC\_CHILD\_MAX,

120 \_SC\_HOST\_NAME\_MAX,

121 \_SC\_IOV\_MAX,

122 \_SC\_LOGIN\_NAME\_MAX,

123 \_SC\_NGROUPS\_MAX,

124 \_SC\_MQ\_OPEN\_MAX,

125 \_SC\_MQ\_PRIO\_MAX,

126 \_SC\_OPEN\_MAX,

127 \_SC\_PAGE\_SIZE,

128 \_SC\_PAGESIZE,

129 \_SC\_THREAD\_DESTRUCTOR\_ITERATIONS,

130 \_SC\_THREAD\_KEYS\_MAX,

131 \_SC\_THREAD\_STACK\_MIN,

132 \_SC\_THREAD\_THREADS\_MAX,

133 \_SC\_RTSIG\_MAX,

134 \_SC\_SEM\_NSEMS\_MAX,

135 \_SC\_SEM\_VALUE\_MAX,

136 \_SC\_SIGQUEUE\_MAX,

137 \_SC\_STREAM\_MAX,

138 \_SC\_SYMLOOP\_MAX,

139 \_SC\_TIMER\_MAX,

140 \_SC\_TTY\_NAME\_MAX,

141 \_SC\_TZNAME\_MAX,

142};

143

144#define \_\_z\_posix\_sysconf\_SC\_ADVISORY\_INFO (-1L)

145#define \_\_z\_posix\_sysconf\_SC\_ASYNCHRONOUS\_IO \

146 COND\_CODE\_1(CONFIG\_POSIX\_ASYNCHRONOUS\_IO, (\_POSIX\_ASYNCHRONOUS\_IO), (-1L))

147#define \_\_z\_posix\_sysconf\_SC\_BARRIERS COND\_CODE\_1(CONFIG\_POSIX\_BARRIERS, (\_POSIX\_BARRIERS), (-1L))

148#define \_\_z\_posix\_sysconf\_SC\_CLOCK\_SELECTION \

149 COND\_CODE\_1(CONFIG\_POSIX\_CLOCK\_SELECTION, (\_POSIX\_CLOCK\_SELECTION), (-1L))

150#define \_\_z\_posix\_sysconf\_SC\_CPUTIME \

151 COND\_CODE\_1(CONFIG\_POSIX\_CPUTIME, (\_POSIX\_CPUTIME), (-1L))

152#define \_\_z\_posix\_sysconf\_SC\_FSYNC \

153 COND\_CODE\_1(CONFIG\_POSIX\_FSYNC, (\_POSIX\_FSYNC), (-1L))

154#define \_\_z\_posix\_sysconf\_SC\_IPV6 COND\_CODE\_1(CONFIG\_NET\_IPV6, (\_POSIX\_IPV6), (-1L))

155#define \_\_z\_posix\_sysconf\_SC\_JOB\_CONTROL (-1L)

156#define \_\_z\_posix\_sysconf\_SC\_MAPPED\_FILES \

157 COND\_CODE\_1(CONFIG\_POSIX\_MAPPED\_FILES, (\_POSIX\_MAPPED\_FILES), (-1L))

158#define \_\_z\_posix\_sysconf\_SC\_MEMLOCK \

159 COND\_CODE\_1(CONFIG\_POSIX\_MEMLOCK, (\_POSIX\_MEMLOCK), (-1L))

160#define \_\_z\_posix\_sysconf\_SC\_MEMLOCK\_RANGE \

161 COND\_CODE\_1(CONFIG\_POSIX\_MEMLOCK\_RANGE, (\_POSIX\_MEMLOCK\_RANGE), (-1L))

162#define \_\_z\_posix\_sysconf\_SC\_MEMORY\_PROTECTION \

163 COND\_CODE\_1(CONFIG\_POSIX\_MEMORY\_PROTECTION, (\_POSIX\_MEMORY\_PROTECTION), (-1L))

164#define \_\_z\_posix\_sysconf\_SC\_MESSAGE\_PASSING \

165 COND\_CODE\_1(CONFIG\_POSIX\_MESSAGE\_PASSING, (\_POSIX\_MESSAGE\_PASSING), (-1L))

166#define \_\_z\_posix\_sysconf\_SC\_MONOTONIC\_CLOCK \

167 COND\_CODE\_1(CONFIG\_POSIX\_MONOTONIC\_CLOCK, (\_POSIX\_MONOTONIC\_CLOCK), (-1L))

168#define \_\_z\_posix\_sysconf\_SC\_PRIORITIZED\_IO (-1L)

169#define \_\_z\_posix\_sysconf\_SC\_PRIORITY\_SCHEDULING \

170 COND\_CODE\_1(CONFIG\_POSIX\_PRIORITY\_SCHEDULING, (\_POSIX\_PRIORITY\_SCHEDULING), (-1L))

171#define \_\_z\_posix\_sysconf\_SC\_RAW\_SOCKETS \

172 COND\_CODE\_1(CONFIG\_NET\_SOCKETS\_PACKET, (\_POSIX\_RAW\_SOCKETS), (-1L))

173#define \_\_z\_posix\_sysconf\_SC\_RE\_DUP\_MAX \_POSIX\_RE\_DUP\_MAX

174#define \_\_z\_posix\_sysconf\_SC\_READER\_WRITER\_LOCKS \

175 COND\_CODE\_1(CONFIG\_POSIX\_READER\_WRITER\_LOCKS, (\_POSIX\_READER\_WRITER\_LOCKS), (-1L))

176#define \_\_z\_posix\_sysconf\_SC\_REALTIME\_SIGNALS (-1L)

177#define \_\_z\_posix\_sysconf\_SC\_REGEXP (-1L)

178#define \_\_z\_posix\_sysconf\_SC\_SAVED\_IDS (-1L)

179#define \_\_z\_posix\_sysconf\_SC\_SEMAPHORES \

180 COND\_CODE\_1(CONFIG\_POSIX\_SEMAPHORES, (\_POSIX\_SEMAPHORES), (-1L))

181#define \_\_z\_posix\_sysconf\_SC\_SHARED\_MEMORY\_OBJECTS \

182 COND\_CODE\_1(CONFIG\_POSIX\_SHARED\_MEMORY\_OBJECTS, (\_POSIX\_SHARED\_MEMORY\_OBJECTS), (-1L))

183#define \_\_z\_posix\_sysconf\_SC\_SHELL (-1L)

184#define \_\_z\_posix\_sysconf\_SC\_SPAWN (-1L)

185#define \_\_z\_posix\_sysconf\_SC\_SPIN\_LOCKS \

186 COND\_CODE\_1(CONFIG\_POSIX\_SPIN\_LOCKS, (\_POSIX\_SPIN\_LOCKS), (-1L))

187#define \_\_z\_posix\_sysconf\_SC\_SPORADIC\_SERVER (-1L)

188#define \_\_z\_posix\_sysconf\_SC\_SS\_REPL\_MAX \_POSIX\_SS\_REPL\_MAX

189#define \_\_z\_posix\_sysconf\_SC\_SYNCHRONIZED\_IO (-1L)

190#define \_\_z\_posix\_sysconf\_SC\_THREAD\_ATTR\_STACKADDR \

191 COND\_CODE\_1(CONFIG\_POSIX\_THREAD\_ATTR\_STACKADDR, (\_POSIX\_THREAD\_ATTR\_STACKADDR), (-1))

192#define \_\_z\_posix\_sysconf\_SC\_THREAD\_ATTR\_STACKSIZE \

193 COND\_CODE\_1(CONFIG\_POSIX\_THREAD\_ATTR\_STACKSIZE, (\_POSIX\_THREAD\_ATTR\_STACKSIZE), (-1L))

194#define \_\_z\_posix\_sysconf\_SC\_THREAD\_CPUTIME (-1L)

195#define \_\_z\_posix\_sysconf\_SC\_THREAD\_PRIO\_INHERIT \

196 COND\_CODE\_1(CONFIG\_POSIX\_THREAD\_PRIO\_INHERIT, (\_POSIX\_THREAD\_PRIO\_INHERIT), (-1L))

197#define \_\_z\_posix\_sysconf\_SC\_THREAD\_PRIO\_PROTECT (-1L)

198#define \_\_z\_posix\_sysconf\_SC\_THREAD\_PRIORITY\_SCHEDULING \

199 COND\_CODE\_1(CONFIG\_POSIX\_THREAD\_PRIORITY\_SCHEDULING, (\_POSIX\_THREAD\_PRIORITY\_SCHEDULING), \

200 (-1L))

201#define \_\_z\_posix\_sysconf\_SC\_THREAD\_PROCESS\_SHARED (-1L)

202#define \_\_z\_posix\_sysconf\_SC\_THREAD\_ROBUST\_PRIO\_INHERIT (-1L)

203#define \_\_z\_posix\_sysconf\_SC\_THREAD\_ROBUST\_PRIO\_PROTECT (-1L)

204#define \_\_z\_posix\_sysconf\_SC\_THREAD\_SAFE\_FUNCTIONS \

205 COND\_CODE\_1(CONFIG\_POSIX\_THREAD\_SAFE\_FUNCTIONS, (\_POSIX\_THREAD\_SAFE\_FUNCTIONS), (-1L))

206#define \_\_z\_posix\_sysconf\_SC\_THREAD\_SPORADIC\_SERVER (-1L)

207#define \_\_z\_posix\_sysconf\_SC\_THREADS \

208 COND\_CODE\_1(CONFIG\_POSIX\_THREADS, (\_POSIX\_THREADS), (-1L))

209#define \_\_z\_posix\_sysconf\_SC\_TIMEOUTS \

210 COND\_CODE\_1(CONFIG\_POSIX\_TIMEOUTS, (\_POSIX\_TIMEOUTS), (-1L))

211#define \_\_z\_posix\_sysconf\_SC\_TIMERS \

212 COND\_CODE\_1(CONFIG\_POSIX\_TIMEOUTS, (\_POSIX\_TIMERS), (-1))

213#define \_\_z\_posix\_sysconf\_SC\_TRACE (-1L)

214#define \_\_z\_posix\_sysconf\_SC\_TRACE\_EVENT\_FILTER (-1L)

215#define \_\_z\_posix\_sysconf\_SC\_TRACE\_EVENT\_NAME\_MAX \_POSIX\_TRACE\_NAME\_MAX

216#define \_\_z\_posix\_sysconf\_SC\_TRACE\_INHERIT (-1L)

217#define \_\_z\_posix\_sysconf\_SC\_TRACE\_LOG (-1L)

218#define \_\_z\_posix\_sysconf\_SC\_TRACE\_NAME\_MAX \_POSIX\_TRACE\_NAME\_MAX

219#define \_\_z\_posix\_sysconf\_SC\_TRACE\_SYS\_MAX \_POSIX\_TRACE\_SYS\_MAX

220#define \_\_z\_posix\_sysconf\_SC\_TRACE\_USER\_EVENT\_MAX \_POSIX\_TRACE\_USER\_EVENT\_MAX

221#define \_\_z\_posix\_sysconf\_SC\_TYPED\_MEMORY\_OBJECTS (-1L)

222#define \_\_z\_posix\_sysconf\_SC\_VERSION \_POSIX\_VERSION

223#define \_\_z\_posix\_sysconf\_SC\_V6\_ILP32\_OFF32 (-1L)

224#define \_\_z\_posix\_sysconf\_SC\_V6\_ILP32\_OFFBIG (-1L)

225#define \_\_z\_posix\_sysconf\_SC\_V6\_LP64\_OFF64 (-1L)

226#define \_\_z\_posix\_sysconf\_SC\_V6\_LPBIG\_OFFBIG (-1L)

227#define \_\_z\_posix\_sysconf\_SC\_V7\_ILP32\_OFF32 (-1L)

228#define \_\_z\_posix\_sysconf\_SC\_V7\_ILP32\_OFFBIG (-1L)

229#define \_\_z\_posix\_sysconf\_SC\_V7\_LP64\_OFF64 (-1L)

230#define \_\_z\_posix\_sysconf\_SC\_V7\_LPBIG\_OFFBIG (-1L)

231#define \_\_z\_posix\_sysconf\_SC\_BC\_BASE\_MAX \_POSIX2\_BC\_BASE\_MAX

232#define \_\_z\_posix\_sysconf\_SC\_BC\_DIM\_MAX \_POSIX2\_BC\_DIM\_MAX

233#define \_\_z\_posix\_sysconf\_SC\_BC\_SCALE\_MAX \_POSIX2\_BC\_SCALE\_MAX

234#define \_\_z\_posix\_sysconf\_SC\_BC\_STRING\_MAX \_POSIX2\_BC\_STRING\_MAX

235#define \_\_z\_posix\_sysconf\_SC\_2\_C\_BIND \_POSIX2\_C\_BIND

236#define \_\_z\_posix\_sysconf\_SC\_2\_C\_DEV \_POSIX2\_C\_DEV

237#define \_\_z\_posix\_sysconf\_SC\_2\_CHAR\_TERM (-1L)

238#define \_\_z\_posix\_sysconf\_SC\_COLL\_WEIGHTS\_MAX \_POSIX2\_COLL\_WEIGHTS\_MAX

239#define \_\_z\_posix\_sysconf\_SC\_DELAYTIMER\_MAX \_POSIX\_DELAYTIMER\_MAX

240#define \_\_z\_posix\_sysconf\_SC\_EXPR\_NEST\_MAX \_POSIX2\_EXPR\_NEST\_MAX

241#define \_\_z\_posix\_sysconf\_SC\_2\_FORT\_DEV (-1L)

242#define \_\_z\_posix\_sysconf\_SC\_2\_FORT\_RUN (-1L)

243#define \_\_z\_posix\_sysconf\_SC\_LINE\_MAX (-1L)

244#define \_\_z\_posix\_sysconf\_SC\_2\_LOCALEDEF (-1L)

245#define \_\_z\_posix\_sysconf\_SC\_2\_PBS (-1L)

246#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_ACCOUNTING (-1L)

247#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_CHECKPOINT (-1L)

248#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_LOCATE (-1L)

249#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_MESSAGE (-1L)

250#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_TRACK (-1L)

251#define \_\_z\_posix\_sysconf\_SC\_2\_SW\_DEV (-1L)

252#define \_\_z\_posix\_sysconf\_SC\_2\_UPE (-1L)

253#define \_\_z\_posix\_sysconf\_SC\_2\_VERSION \_POSIX2\_VERSION

254#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_CRYPT (-1L)

255#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_ENH\_I18N (-1L)

256#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_REALTIME (-1L)

257#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_REALTIME\_THREADS (-1L)

258#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_SHM (-1L)

259#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_STREAMS \

260 COND\_CODE\_1(CONFIG\_XOPEN\_STREAMS, (\_XOPEN\_STREAMS), (-1))

261#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_UNIX (-1L)

262#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_UUCP (-1L)

263#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_VERSION \_XOPEN\_VERSION

264#define \_\_z\_posix\_sysconf\_SC\_CLK\_TCK (100L)

265#define \_\_z\_posix\_sysconf\_SC\_GETGR\_R\_SIZE\_MAX (0L)

266#define \_\_z\_posix\_sysconf\_SC\_GETPW\_R\_SIZE\_MAX (0L)

267#define \_\_z\_posix\_sysconf\_SC\_AIO\_LISTIO\_MAX AIO\_LISTIO\_MAX

268#define \_\_z\_posix\_sysconf\_SC\_AIO\_MAX AIO\_MAX

269#define \_\_z\_posix\_sysconf\_SC\_AIO\_PRIO\_DELTA\_MAX AIO\_PRIO\_DELTA\_MAX

270#define \_\_z\_posix\_sysconf\_SC\_ARG\_MAX ARG\_MAX

271#define \_\_z\_posix\_sysconf\_SC\_ATEXIT\_MAX ATEXIT\_MAX

272#define \_\_z\_posix\_sysconf\_SC\_CHILD\_MAX CHILD\_MAX

273#define \_\_z\_posix\_sysconf\_SC\_HOST\_NAME\_MAX HOST\_NAME\_MAX

274#define \_\_z\_posix\_sysconf\_SC\_IOV\_MAX IOV\_MAX

275#define \_\_z\_posix\_sysconf\_SC\_LOGIN\_NAME\_MAX LOGIN\_NAME\_MAX

276#define \_\_z\_posix\_sysconf\_SC\_NGROUPS\_MAX \_POSIX\_NGROUPS\_MAX

277#define \_\_z\_posix\_sysconf\_SC\_MQ\_OPEN\_MAX MQ\_OPEN\_MAX

278#define \_\_z\_posix\_sysconf\_SC\_MQ\_PRIO\_MAX MQ\_PRIO\_MAX

279#define \_\_z\_posix\_sysconf\_SC\_OPEN\_MAX CONFIG\_ZVFS\_OPEN\_MAX

280#define \_\_z\_posix\_sysconf\_SC\_PAGE\_SIZE PAGE\_SIZE

281#define \_\_z\_posix\_sysconf\_SC\_PAGESIZE PAGESIZE

282#define \_\_z\_posix\_sysconf\_SC\_THREAD\_DESTRUCTOR\_ITERATIONS PTHREAD\_DESTRUCTOR\_ITERATIONS

283#define \_\_z\_posix\_sysconf\_SC\_THREAD\_KEYS\_MAX PTHREAD\_KEYS\_MAX

284#define \_\_z\_posix\_sysconf\_SC\_THREAD\_STACK\_MIN PTHREAD\_STACK\_MIN

285#define \_\_z\_posix\_sysconf\_SC\_THREAD\_THREADS\_MAX PTHREAD\_THREADS\_MAX

286#define \_\_z\_posix\_sysconf\_SC\_RTSIG\_MAX RTSIG\_MAX

287#define \_\_z\_posix\_sysconf\_SC\_SEM\_NSEMS\_MAX SEM\_NSEMS\_MAX

288#define \_\_z\_posix\_sysconf\_SC\_SEM\_VALUE\_MAX SEM\_VALUE\_MAX

289#define \_\_z\_posix\_sysconf\_SC\_SIGQUEUE\_MAX SIGQUEUE\_MAX

290#define \_\_z\_posix\_sysconf\_SC\_STREAM\_MAX STREAM\_MAX

291#define \_\_z\_posix\_sysconf\_SC\_SYMLOOP\_MAX SYMLOOP\_MAX

292#define \_\_z\_posix\_sysconf\_SC\_TIMER\_MAX TIMER\_MAX

293#define \_\_z\_posix\_sysconf\_SC\_TTY\_NAME\_MAX TTY\_NAME\_MAX

294#define \_\_z\_posix\_sysconf\_SC\_TZNAME\_MAX TZNAME\_MAX

295

296#ifdef CONFIG\_POSIX\_SYSCONF\_IMPL\_MACRO

297#define sysconf(x) (long)CONCAT(\_\_z\_posix\_sysconf, x)

298#endif

299

300#ifdef \_\_cplusplus

301}

302#endif

303

304#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_SYSCONF\_H\_ \*/

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [sysconf.h](sysconf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
