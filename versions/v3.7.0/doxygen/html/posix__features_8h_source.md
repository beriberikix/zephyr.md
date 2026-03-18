---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/posix__features_8h_source.html
original_path: doxygen/html/posix__features_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

posix\_features.h

[Go to the documentation of this file.](posix__features_8h.md)

1/\*

2 \* Copyright (c) 2024 BayLibre SAS

3 \* Copyright (c) 2024 Tenstorrent AI ULC

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef INCLUDE\_ZEPHYR\_POSIX\_POSIX\_FEATURES\_H\_

9#define INCLUDE\_ZEPHYR\_POSIX\_POSIX\_FEATURES\_H\_

10

11#include <zephyr/autoconf.h> /\* CONFIG\_\* \*/

12#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)> /\* COND\_CODE\_1() \*/

13

14/\*

15 \* POSIX Application Environment Profiles (AEP - IEEE Std 1003.13-2003)

16 \*/

17

18#ifdef CONFIG\_POSIX\_AEP\_REALTIME\_MINIMAL

19#define \_POSIX\_AEP\_REALTIME\_MINIMAL 200312L

20#endif

21

22#ifdef CONFIG\_POSIX\_AEP\_REALTIME\_CONTROLLER

23#define \_POSIX\_AEP\_REALTIME\_CONTROLLER 200312L

24#endif

25

26#ifdef CONFIG\_POSIX\_AEP\_REALTIME\_DEDICATED

27#define \_POSIX\_AEP\_REALTIME\_DEDICATED 200312L

28#endif

29

30/\*

31 \* POSIX System Interfaces

32 \*/

33

34#define \_POSIX\_VERSION 200809L

35

36#define \_POSIX\_CHOWN\_RESTRICTED (0)

37#define \_POSIX\_NO\_TRUNC (0)

38#define \_POSIX\_VDISABLE ('\0')

39

40/\* #define \_POSIX\_ADVISORY\_INFO (-1L) \*/

41

42#ifdef CONFIG\_POSIX\_ASYNCHRONOUS\_IO

43#define \_POSIX\_ASYNCHRONOUS\_IO \_POSIX\_VERSION

44#endif

45

46#ifdef CONFIG\_POSIX\_BARRIERS

47#define \_POSIX\_BARRIERS \_POSIX\_VERSION

48#endif

49

50#ifdef CONFIG\_POSIX\_CLOCK\_SELECTION

51#define \_POSIX\_CLOCK\_SELECTION \_POSIX\_VERSION

52#endif

53

54#ifdef CONFIG\_POSIX\_CPUTIME

55#define \_POSIX\_CPUTIME \_POSIX\_VERSION

56#endif

57

58#ifdef CONFIG\_POSIX\_FSYNC

59#define \_POSIX\_FSYNC \_POSIX\_VERSION

60#endif

61

62#ifdef CONFIG\_NET\_IPV6

63#define \_POSIX\_IPV6 \_POSIX\_VERSION

64#endif

65

66/\* #define \_POSIX\_JOB\_CONTROL (-1L) \*/

67

68#ifdef CONFIG\_POSIX\_MAPPED\_FILES

69#define \_POSIX\_MAPPED\_FILES \_POSIX\_VERSION

70#endif

71

72#ifdef CONFIG\_POSIX\_MEMLOCK

73#define \_POSIX\_MEMLOCK \_POSIX\_VERSION

74#endif

75

76#ifdef CONFIG\_POSIX\_MEMLOCK\_RANGE

77#define \_POSIX\_MEMLOCK\_RANGE \_POSIX\_VERSION

78#endif

79

80#ifdef CONFIG\_POSIX\_MEMORY\_PROTECTION

81#define \_POSIX\_MEMORY\_PROTECTION \_POSIX\_VERSION

82#endif

83

84#ifdef CONFIG\_POSIX\_MESSAGE\_PASSING

85#define \_POSIX\_MESSAGE\_PASSING \_POSIX\_VERSION

86#endif

87

88#ifdef CONFIG\_POSIX\_MONOTONIC\_CLOCK

89#define \_POSIX\_MONOTONIC\_CLOCK \_POSIX\_VERSION

90#endif

91

92/\* #define \_POSIX\_PRIORITIZED\_IO (-1L) \*/

93

94#ifdef CONFIG\_POSIX\_PRIORITY\_SCHEDULING

95#define \_POSIX\_PRIORITY\_SCHEDULING \_POSIX\_VERSION

96#endif

97

98#ifdef CONFIG\_NET\_SOCKETS\_PACKET

99#define \_POSIX\_RAW\_SOCKETS \_POSIX\_VERSION

100#endif

101

102#ifdef CONFIG\_POSIX\_READER\_WRITER\_LOCKS

103#define \_POSIX\_READER\_WRITER\_LOCKS \_POSIX\_VERSION

104#endif

105

106/\* #define \_POSIX\_REALTIME\_SIGNALS (-1L) \*/

107/\* #define \_POSIX\_REGEXP (-1L) \*/

108/\* #define \_POSIX\_SAVED\_IDS (-1L) \*/

109

110#ifdef CONFIG\_POSIX\_SEMAPHORES

111#define \_POSIX\_SEMAPHORES \_POSIX\_VERSION

112#endif

113

114#ifdef CONFIG\_POSIX\_SHARED\_MEMORY\_OBJECTS

115#define \_POSIX\_SHARED\_MEMORY\_OBJECTS \_POSIX\_VERSION

116#endif

117

118/\* #define \_POSIX\_SHELL (-1L) \*/

119/\* #define \_POSIX\_SPAWN (-1L) \*/

120

121#ifdef CONFIG\_POSIX\_SPIN\_LOCKS

122#define \_POSIX\_SPIN\_LOCKS \_POSIX\_VERSION

123#endif

124

125/\* #define \_POSIX\_SPORADIC\_SERVER (-1L) \*/

126/\* #define \_POSIX\_SYNCHRONIZED\_IO (-1L) \*/

127

128#ifdef CONFIG\_POSIX\_THREAD\_ATTR\_STACKADDR

129#define \_POSIX\_THREAD\_ATTR\_STACKADDR \_POSIX\_VERSION

130#endif

131

132#ifdef CONFIG\_POSIX\_THREAD\_ATTR\_STACKSIZE

133#define \_POSIX\_THREAD\_ATTR\_STACKSIZE \_POSIX\_VERSION

134#endif

135

136#ifdef CONFIG\_POSIX\_THREAD\_CPUTIME

137#define \_POSIX\_THREAD\_CPUTIME \_POSIX\_VERSION

138#endif

139

140#ifdef CONFIG\_POSIX\_THREAD\_PRIO\_INHERIT

141#define \_POSIX\_THREAD\_PRIO\_INHERIT \_POSIX\_VERSION

142#endif

143

144#ifdef CONFIG\_POSIX\_THREAD\_PRIO\_PROTECT

145#define \_POSIX\_THREAD\_PRIO\_PROTECT \_POSIX\_VERSION

146#endif

147

148#ifdef CONFIG\_POSIX\_THREAD\_PRIORITY\_SCHEDULING

149#define \_POSIX\_THREAD\_PRIORITY\_SCHEDULING \_POSIX\_VERSION

150#endif

151

152/\* #define \_POSIX\_THREAD\_PROCESS\_SHARED (-1L) \*/

153/\* #define \_POSIX\_THREAD\_ROBUST\_PRIO\_INHERIT (-1L) \*/

154/\* #define \_POSIX\_THREAD\_ROBUST\_PRIO\_PROTECT (-1L) \*/

155

156#ifdef CONFIG\_POSIX\_THREAD\_SAFE\_FUNCTIONS

157#define \_POSIX\_THREAD\_SAFE\_FUNCTIONS \_POSIX\_VERSION

158#endif

159

160/\* #define \_POSIX\_THREAD\_SPORADIC\_SERVER (-1L) \*/

161

162#ifdef CONFIG\_POSIX\_THREADS

163#ifndef \_POSIX\_THREADS

164#define \_POSIX\_THREADS \_POSIX\_VERSION

165#endif

166#endif

167

168#ifdef CONFIG\_POSIX\_TIMEOUTS

169#define \_POSIX\_TIMEOUTS \_POSIX\_VERSION

170#endif

171

172#ifdef CONFIG\_POSIX\_TIMERS

173#define \_POSIX\_TIMERS \_POSIX\_VERSION

174#endif

175

176/\* #define \_POSIX\_TRACE (-1L) \*/

177/\* #define \_POSIX\_TRACE\_EVENT\_FILTER (-1L) \*/

178/\* #define \_POSIX\_TRACE\_INHERIT (-1L) \*/

179/\* #define \_POSIX\_TRACE\_LOG (-1L) \*/

180/\* #define \_POSIX\_TYPED\_MEMORY\_OBJECTS (-1L) \*/

181

182/\*

183 \* POSIX v6 Options

184 \*/

185/\* #define \_POSIX\_V6\_ILP32\_OFF32 (-1L) \*/

186/\* #define \_POSIX\_V6\_ILP32\_OFFBIG (-1L) \*/

187/\* #define \_POSIX\_V6\_LP64\_OFF64 (-1L) \*/

188/\* #define \_POSIX\_V6\_LPBIG\_OFFBIG (-1L) \*/

189

190/\*

191 \* POSIX v7 Options

192 \*/

193/\* #define \_POSIX\_V7\_ILP32\_OFF32 (-1L) \*/

194/\* #define \_POSIX\_V7\_ILP32\_OFFBIG (-1L) \*/

195/\* #define \_POSIX\_V7\_LP64\_OFF64 (-1L) \*/

196/\* #define \_POSIX\_V7\_LPBIG\_OFFBIG (-1L) \*/

197

198/\*

199 \* POSIX2 Options

200 \*/

201#define \_POSIX2\_VERSION \_POSIX\_VERSION

202#define \_POSIX2\_C\_BIND \_POSIX2\_VERSION

203#define \_POSIX2\_C\_DEV \_POSIX2\_VERSION

204/\* #define \_POSIX2\_CHAR\_TERM (-1L) \*/

205/\* #define \_POSIX2\_FORT\_DEV (-1L) \*/

206/\* #define \_POSIX2\_FORT\_RUN (-1L) \*/

207/\* #define \_POSIX2\_LOCALEDEF (-1L) \*/

208/\* #define \_POSIX2\_PBS (-1L) \*/

209/\* #define \_POSIX2\_PBS\_ACCOUNTING (-1L) \*/

210/\* #define \_POSIX2\_PBS\_CHECKPOINT (-1L) \*/

211/\* #define \_POSIX2\_PBS\_LOCATE (-1L) \*/

212/\* #define \_POSIX2\_PBS\_MESSAGE (-1L) \*/

213/\* #define \_POSIX2\_PBS\_TRACK (-1L) \*/

214/\* #define \_POSIX2\_SW\_DEV (-1L) \*/

215/\* #define \_POSIX2\_UPE (-1L) \*/

216

217/\*

218 \* X/Open System Interfaces

219 \*/

220#define \_XOPEN\_VERSION 700

221/\* #define \_XOPEN\_CRYPT (-1L) \*/

222/\* #define \_XOPEN\_ENH\_I18N (-1L) \*/

223/\* #define \_XOPEN\_REALTIME (-1L) \*/

224/\* #define \_XOPEN\_REALTIME\_THREADS (-1L) \*/

225/\* #define \_XOPEN\_SHM (-1L) \*/

226

227#ifdef CONFIG\_XOPEN\_STREAMS

228#define \_XOPEN\_STREAMS \_XOPEN\_VERSION

229#endif

230

231/\* #define \_XOPEN\_UNIX (-1L) \*/

232/\* #define \_XOPEN\_UUCP (-1L) \*/

233

234/\* Maximum values \*/

235#define \_POSIX\_CLOCKRES\_MIN (20000000L)

236

237/\* Minimum values \*/

238#define \_POSIX\_AIO\_LISTIO\_MAX (2)

239#define \_POSIX\_AIO\_MAX (1)

240#define \_POSIX\_ARG\_MAX (4096)

241#define \_POSIX\_CHILD\_MAX (25)

242#define \_POSIX\_DELAYTIMER\_MAX \

243 COND\_CODE\_1(CONFIG\_POSIX\_TIMERS, (CONFIG\_POSIX\_DELAYTIMER\_MAX), (0))

244#define \_POSIX\_HOST\_NAME\_MAX \

245 COND\_CODE\_1(CONFIG\_POSIX\_NETWORKING, (CONFIG\_POSIX\_HOST\_NAME\_MAX), (0))

246#define \_POSIX\_LINK\_MAX (8)

247#define \_POSIX\_LOGIN\_NAME\_MAX (9)

248#define \_POSIX\_MAX\_CANON (255)

249#define \_POSIX\_MAX\_INPUT (255)

250#define \_POSIX\_MQ\_OPEN\_MAX \

251 COND\_CODE\_1(CONFIG\_POSIX\_MESSAGE\_PASSING, (CONFIG\_POSIX\_MQ\_OPEN\_MAX), (0))

252#define \_POSIX\_MQ\_PRIO\_MAX (32)

253#define \_POSIX\_NAME\_MAX (14)

254#define \_POSIX\_NGROUPS\_MAX (8)

255#define \_POSIX\_OPEN\_MAX CONFIG\_POSIX\_OPEN\_MAX

256#define \_POSIX\_PATH\_MAX (256)

257#define \_POSIX\_PIPE\_BUF (512)

258#define \_POSIX\_RE\_DUP\_MAX (255)

259#define \_POSIX\_RTSIG\_MAX \

260 COND\_CODE\_1(CONFIG\_POSIX\_REALTIME\_SIGNALS, (CONFIG\_POSIX\_RTSIG\_MAX), (0))

261#define \_POSIX\_SEM\_NSEMS\_MAX \

262 COND\_CODE\_1(CONFIG\_POSIX\_SEMAPHORES, (CONFIG\_POSIX\_SEM\_NSEMS\_MAX), (0))

263#define \_POSIX\_SEM\_VALUE\_MAX \

264 COND\_CODE\_1(CONFIG\_POSIX\_SEMAPHORES, (CONFIG\_POSIX\_SEM\_VALUE\_MAX), (0))

265#define \_POSIX\_SIGQUEUE\_MAX (32)

266#define \_POSIX\_SSIZE\_MAX (32767)

267#define \_POSIX\_SS\_REPL\_MAX (4)

268#define \_POSIX\_STREAM\_MAX (8)

269#define \_POSIX\_SYMLINK\_MAX (255)

270#define \_POSIX\_SYMLOOP\_MAX (8)

271#define \_POSIX\_THREAD\_DESTRUCTOR\_ITERATIONS (4)

272#define \_POSIX\_THREAD\_KEYS\_MAX \

273 COND\_CODE\_1(CONFIG\_POSIX\_THREADS, (CONFIG\_POSIX\_THREAD\_KEYS\_MAX), (0))

274#define \_POSIX\_THREAD\_THREADS\_MAX \

275 COND\_CODE\_1(CONFIG\_POSIX\_THREADS, (CONFIG\_POSIX\_THREAD\_THREADS\_MAX), (0))

276#define \_POSIX\_TIMER\_MAX \

277 COND\_CODE\_1(CONFIG\_POSIX\_TIMERS, (CONFIG\_POSIX\_TIMER\_MAX), (0))

278#define \_POSIX\_TRACE\_EVENT\_NAME\_MAX (30)

279#define \_POSIX\_TRACE\_NAME\_MAX (8)

280#define \_POSIX\_TRACE\_SYS\_MAX (8)

281#define \_POSIX\_TRACE\_USER\_EVENT\_MAX (32)

282#define \_POSIX\_TTY\_NAME\_MAX (9)

283#define \_POSIX\_TZNAME\_MAX (6)

284#define \_POSIX2\_BC\_BASE\_MAX (99)

285#define \_POSIX2\_BC\_DIM\_MAX (2048)

286#define \_POSIX2\_BC\_SCALE\_MAX (99)

287#define \_POSIX2\_BC\_STRING\_MAX (1000)

288#define \_POSIX2\_CHARCLASS\_NAME\_MAX (14)

289#define \_POSIX2\_COLL\_WEIGHTS\_MAX (2)

290#define \_POSIX2\_EXPR\_NEST\_MAX (32)

291#define \_POSIX2\_LINE\_MAX (2048)

292#define \_XOPEN\_IOV\_MAX (16)

293#define \_XOPEN\_NAME\_MAX (255)

294#define \_XOPEN\_PATH\_MAX (1024)

295

296/\* Other invariant values \*/

[ 297](posix__features_8h.md#a82c429c39d68f08d56e4bfdb050fe54a)#define NL\_LANGMAX (14)

[ 298](posix__features_8h.md#a7e7a512ab4395a4bb0be4ff872764e45)#define NL\_MSGMAX (32767)

[ 299](posix__features_8h.md#a5dd5a06bde8cda4edb4dfda129375a1a)#define NL\_SETMAX (255)

[ 300](posix__features_8h.md#a934658c7b37ed12672f76ec304a5b460)#define NL\_TEXTMAX (\_POSIX2\_LINE\_MAX)

[ 301](posix__features_8h.md#a3b04cc1d4ce6930b578eede1f1c6ebfc)#define NZERO (20)

302

303/\* Runtime invariant values \*/

[ 304](posix__features_8h.md#a0b4029afb1dcaf401c08b7b147d00cec)#define AIO\_LISTIO\_MAX \_POSIX\_AIO\_LISTIO\_MAX

[ 305](posix__features_8h.md#a0889d4ed1489519e1e8a83ca6f212c5a)#define AIO\_MAX \_POSIX\_AIO\_MAX

[ 306](posix__features_8h.md#aa9d8b79923c4fc549c074fc387ef65c9)#define AIO\_PRIO\_DELTA\_MAX (0)

[ 307](posix__features_8h.md#a86025bd0a07f29a6ae97f310ff9c701c)#define DELAYTIMER\_MAX \_POSIX\_DELAYTIMER\_MAX

[ 308](posix__features_8h.md#ac956117a90023ec0971b8f9fce9dec75)#define HOST\_NAME\_MAX \_POSIX\_HOST\_NAME\_MAX

[ 309](posix__features_8h.md#af3b7f7833ae69cac7adf84f5973715fe)#define LOGIN\_NAME\_MAX \_POSIX\_LOGIN\_NAME\_MAX

[ 310](posix__features_8h.md#abea867e23b4ca9316a0a7511f1b783d3)#define MQ\_OPEN\_MAX \_POSIX\_MQ\_OPEN\_MAX

[ 311](posix__features_8h.md#ad1516b4f64b6dc890b1fa3bf576bfef9)#define MQ\_PRIO\_MAX \_POSIX\_MQ\_PRIO\_MAX

312

313#ifndef ATEXIT\_MAX

[ 314](posix__features_8h.md#abf407c2e796fa3e943acf18be72aa01d)#define ATEXIT\_MAX 8

315#endif

316

[ 317](posix__features_8h.md#a7d467c1d283fdfa1f2081ba1e0d01b6e)#define PAGE\_SIZE CONFIG\_POSIX\_PAGE\_SIZE

[ 318](posix__features_8h.md#a519adc2af3ba06a8f0548b6690050a89)#define PAGESIZE PAGE\_SIZE

319

[ 320](posix__features_8h.md#a1d96b13a4ba5975d724c5fe13788a957)#define PTHREAD\_DESTRUCTOR\_ITERATIONS \_POSIX\_THREAD\_DESTRUCTOR\_ITERATIONS

[ 321](posix__features_8h.md#a0a23e66e087bcf5c253b9b2746f19a64)#define PTHREAD\_KEYS\_MAX \_POSIX\_THREAD\_KEYS\_MAX

[ 322](posix__features_8h.md#ab8f25dec585d6255fcf40b67db66c1c5)#define PTHREAD\_THREADS\_MAX \_POSIX\_THREAD\_THREADS\_MAX

[ 323](posix__features_8h.md#ad7f754398cdc81462f3d626e74a41b69)#define RTSIG\_MAX \_POSIX\_RTSIG\_MAX

[ 324](posix__features_8h.md#a829c888ff8820c37384a5531577cea33)#define SEM\_NSEMS\_MAX \_POSIX\_SEM\_NSEMS\_MAX

[ 325](posix__features_8h.md#a2961bb23950351c6b10976674c27ddaf)#define SEM\_VALUE\_MAX \_POSIX\_SEM\_VALUE\_MAX

[ 326](posix__features_8h.md#a649781c35d0360b7d68ef6d55f2aa668)#define SIGQUEUE\_MAX \_POSIX\_SIGQUEUE\_MAX

[ 327](posix__features_8h.md#a238bb3d2a0e88f9ff3e46a6affd7f61d)#define STREAM\_MAX \_POSIX\_STREAM\_MAX

[ 328](posix__features_8h.md#a41170bbc4e205b3bc9c2b06033aecc17)#define SYMLOOP\_MAX \_POSIX\_SYMLOOP\_MAX

[ 329](posix__features_8h.md#a9cb39fc9fca65abcf086c5b293db3772)#define TIMER\_MAX \_POSIX\_TIMER\_MAX

[ 330](posix__features_8h.md#a8e87ff1f5de326c7161ef933ff2fb0f1)#define TTY\_NAME\_MAX \_POSIX\_TTY\_NAME\_MAX

[ 331](posix__features_8h.md#afb3fe48998f8d32cfb7047b917a8039e)#define TZNAME\_MAX \_POSIX\_TZNAME\_MAX

332

333/\* Pathname variable values \*/

[ 334](posix__features_8h.md#a34ef6afc1709d5686f1353804aa03e88)#define FILESIZEBITS (32)

[ 335](posix__features_8h.md#aa9c42ba60b7eac67360d9804a99e8bba)#define POSIX\_ALLOC\_SIZE\_MIN (256)

[ 336](posix__features_8h.md#a9d04829540462d79aa8751d230987d8b)#define POSIX\_REC\_INCR\_XFER\_SIZE (1024)

[ 337](posix__features_8h.md#a17269b771b87209b99c9698c782f0d9b)#define POSIX\_REC\_MAX\_XFER\_SIZE (32767)

[ 338](posix__features_8h.md#a3dae40a21514758cfd61dfb8f159c6f4)#define POSIX\_REC\_MIN\_XFER\_SIZE (1)

[ 339](posix__features_8h.md#a40069c33a92e401df7b3b09d1e65ce55)#define POSIX\_REC\_XFER\_ALIGN (4)

[ 340](posix__features_8h.md#af552b1b86caac064b8d74f73ac9d3f0c)#define SYMLINK\_MAX \_POSIX\_SYMLINK\_MAX

341

342#endif /\* INCLUDE\_ZEPHYR\_POSIX\_POSIX\_FEATURES\_H\_ \*/

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [posix\_features.h](posix__features_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
