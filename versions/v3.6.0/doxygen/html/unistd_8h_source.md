---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unistd_8h_source.html
original_path: doxygen/html/unistd_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

unistd.h

[Go to the documentation of this file.](unistd_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_UNISTD\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_UNISTD\_H\_

8

9#include "[posix\_types.h](posix__types_8h.md)"

10#include <[zephyr/posix/sys/stat.h](include_2zephyr_2posix_2sys_2stat_8h.md)>

11#ifdef CONFIG\_NETWORKING

12/\* For zsock\_gethostname() \*/

13#include <[zephyr/net/socket.h](net_2socket_8h.md)>

14#include <[zephyr/net/hostname.h](hostname_8h.md)>

15#endif

16

17#ifdef CONFIG\_POSIX\_API

18#include <[zephyr/fs/fs.h](fs_8h.md)>

19#endif

20

21#ifdef CONFIG\_POSIX\_SYSCONF

22#include <[zephyr/posix/signal.h](signal_8h.md)>

23#endif

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29/\* Version test macros \*/

30#define \_POSIX\_VERSION 200809L

31#define \_POSIX2\_VERSION (-1L)

32#define \_XOPEN\_VERSION (-1L)

33

34/\* Internal helper macro to set constant if required Kconfig symbol is enabled \*/

35#define Z\_SC\_VAL\_IFDEF(\_def, \_val) COND\_CODE\_1(\_def, (\_val), (-1L))

36

37/\* Constants for Opitions and Option Groups \*/

38#define \_POSIX\_ADVISORY\_INFO (-1L)

39#define \_POSIX\_ASYNCHRONOUS\_IO (-1L)

40#define \_POSIX\_BARRIERS Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_IPC, \_POSIX\_VERSION)

41#define \_POSIX\_CHOWN\_RESTRICTED (-1L)

42#define \_POSIX\_CLOCK\_SELECTION Z\_SC\_VAL\_IFDEF(CONFIG\_POSIX\_CLOCK, \_POSIX\_VERSION)

43#define \_POSIX\_CPUTIME (-1L)

44#define \_POSIX\_FSYNC (-1L)

45#define \_POSIX\_IPV6 Z\_SC\_VAL\_IFDEF(CONFIG\_NET\_IPV6, \_POSIX\_VERSION)

46#define \_POSIX\_JOB\_CONTROL (-1L)

47#define \_POSIX\_MAPPED\_FILES \_POSIX\_VERSION

48#define \_POSIX\_MEMLOCK (-1L)

49#define \_POSIX\_MEMLOCK\_RANGE (-1L)

50#define \_POSIX\_MEMORY\_PROTECTION (-1L)

51#define \_POSIX\_MESSAGE\_PASSING Z\_SC\_VAL\_IFDEF(CONFIG\_POSIX\_MQUEUE, \_POSIX\_VERSION)

52#define \_POSIX\_MONOTONIC\_CLOCK Z\_SC\_VAL\_IFDEF(CONFIG\_POSIX\_CLOCK, \_POSIX\_VERSION)

53#define \_POSIX\_NO\_TRUNC (-1L)

54#define \_POSIX\_PRIORITIZED\_IO (-1L)

55#define \_POSIX\_PRIORITY\_SCHEDULING (-1L)

56#define \_POSIX\_RAW\_SOCKETS Z\_SC\_VAL\_IFDEF(CONFIG\_NET\_SOCKETS\_PACKET, \_POSIX\_VERSION)

57#define \_POSIX\_READER\_WRITER\_LOCKS Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_IPC, \_POSIX\_VERSION)

58#define \_POSIX\_REALTIME\_SIGNALS (-1L)

59#define \_POSIX\_REGEXP (-1L)

60#define \_POSIX\_SAVED\_IDS (-1L)

61#define \_POSIX\_SEMAPHORES Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_IPC, \_POSIX\_VERSION)

62#define \_POSIX\_SHARED\_MEMORY\_OBJECTS (-1L)

63#define \_POSIX\_SHELL (-1L)

64#define \_POSIX\_SPAWN (-1L)

65#define \_POSIX\_SPIN\_LOCKS Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_SPINLOCK, \_POSIX\_VERSION)

66#define \_POSIX\_SPORADIC\_SERVER (-1L)

67#define \_POSIX\_SYNCHRONIZED\_IO (-1L)

68#define \_POSIX\_THREAD\_ATTR\_STACKADDR Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_IPC, \_POSIX\_VERSION)

69#define \_POSIX\_THREAD\_ATTR\_STACKSIZE Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_IPC, \_POSIX\_VERSION)

70#define \_POSIX\_THREAD\_CPUTIME (-1L)

71#define \_POSIX\_THREAD\_PRIO\_INHERIT \_POSIX\_VERSION

72#define \_POSIX\_THREAD\_PRIO\_PROTECT (-1L)

73#define \_POSIX\_THREAD\_PRIORITY\_SCHEDULING Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_IPC, \_POSIX\_VERSION)

74#define \_POSIX\_THREAD\_PROCESS\_SHARED (-1L)

75#define \_POSIX\_THREAD\_ROBUST\_PRIO\_INHERIT (-1L)

76#define \_POSIX\_THREAD\_ROBUST\_PRIO\_PROTECT (-1L)

77#define \_POSIX\_THREAD\_SAFE\_FUNCTIONS Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_IPC, \_POSIX\_VERSION)

78#define \_POSIX\_THREAD\_SPORADIC\_SERVER (-1L)

79

80#ifndef \_POSIX\_THREADS

81#define \_POSIX\_THREADS Z\_SC\_VAL\_IFDEF(CONFIG\_PTHREAD\_IPC, \_POSIX\_VERSION)

82#endif

83

84#define \_POSIX\_TIMEOUTS Z\_SC\_VAL\_IFDEF(CONFIG\_POSIX\_CLOCK, \_POSIX\_VERSION)

85#define \_POSIX\_TIMERS Z\_SC\_VAL\_IFDEF(CONFIG\_POSIX\_CLOCK, \_POSIX\_VERSION)

86#define \_POSIX\_TRACE (-1L)

87#define \_POSIX\_TRACE\_EVENT\_FILTER (-1L)

88#define \_POSIX\_TRACE\_INHERIT (-1L)

89#define \_POSIX\_TRACE\_LOG (-1L)

90#define \_POSIX\_TYPED\_MEMORY\_OBJECTS (-1L)

91#define \_POSIX\_V6\_ILP32\_OFF32 (-1L)

92#define \_POSIX\_V6\_ILP32\_OFFBIG (-1L)

93#define \_POSIX\_V6\_LP64\_OFF64 (-1L)

94#define \_POSIX\_V6\_LPBIG\_OFFBIG (-1L)

95#define \_POSIX\_V7\_ILP32\_OFF32 (-1L)

96#define \_POSIX\_V7\_ILP32\_OFFBIG (-1L)

97#define \_POSIX\_V7\_LP64\_OFF64 (-1L)

98#define \_POSIX\_V7\_LPBIG\_OFFBIG (-1L)

99#define \_POSIX2\_C\_BIND \_POSIX\_VERSION

100#define \_POSIX2\_C\_DEV (-1L)

101#define \_POSIX2\_CHAR\_TERM (-1L)

102#define \_POSIX2\_FORT\_DEV (-1L)

103#define \_POSIX2\_FORT\_RUN (-1L)

104#define \_POSIX2\_LOCALEDEF (-1L)

105#define \_POSIX2\_PBS (-1L)

106#define \_POSIX2\_PBS\_ACCOUNTING (-1L)

107#define \_POSIX2\_PBS\_CHECKPOINT (-1L)

108#define \_POSIX2\_PBS\_LOCATE (-1L)

109#define \_POSIX2\_PBS\_MESSAGE (-1L)

110#define \_POSIX2\_PBS\_TRACK (-1L)

111#define \_POSIX2\_SW\_DEV (-1L)

112#define \_POSIX2\_UPE (-1L)

113#define \_XOPEN\_CRYPT (-1L)

114#define \_XOPEN\_ENH\_I18N (-1L)

115#define \_XOPEN\_REALTIME (-1L)

116#define \_XOPEN\_REALTIME\_THREADS (-1L)

117#define \_XOPEN\_SHM (-1L)

118#define \_XOPEN\_STREAMS (-1L)

119#define \_XOPEN\_UNIX (-1L)

120#define \_XOPEN\_UUCP (-1L)

121

122/\* Maximum values \*/

123#define \_POSIX\_CLOCKRES\_MIN (20000000L)

124

125/\* Minimum values \*/

126#define \_POSIX\_AIO\_LISTIO\_MAX (2)

127#define \_POSIX\_AIO\_MAX (1)

128#define \_POSIX\_ARG\_MAX (4096)

129#define \_POSIX\_CHILD\_MAX (25)

130#define \_POSIX\_DELAYTIMER\_MAX (32)

131#define \_POSIX\_HOST\_NAME\_MAX (255)

132#define \_POSIX\_LINK\_MAX (8)

133#define \_POSIX\_LOGIN\_NAME\_MAX (9)

134#define \_POSIX\_MAX\_CANON (255)

135#define \_POSIX\_MAX\_INPUT (255)

136#define \_POSIX\_MQ\_OPEN\_MAX CONFIG\_MSG\_COUNT\_MAX

137#define \_POSIX\_MQ\_PRIO\_MAX (32)

138#define \_POSIX\_NAME\_MAX (14)

139#define \_POSIX\_NGROUPS\_MAX (8)

140#define \_POSIX\_OPEN\_MAX CONFIG\_POSIX\_MAX\_FDS

141#define \_POSIX\_PATH\_MAX (256)

142#define \_POSIX\_PIPE\_BUF (512)

143#define \_POSIX\_RE\_DUP\_MAX (255)

144#define \_POSIX\_RTSIG\_MAX CONFIG\_POSIX\_RTSIG\_MAX

145#define \_POSIX\_SEM\_NSEMS\_MAX CONFIG\_SEM\_NAMELEN\_MAX

146#define \_POSIX\_SEM\_VALUE\_MAX CONFIG\_SEM\_VALUE\_MAX

147#define \_POSIX\_SIGQUEUE\_MAX (32)

148#define \_POSIX\_SSIZE\_MAX (32767)

149#define \_POSIX\_SS\_REPL\_MAX (4)

150#define \_POSIX\_STREAM\_MAX (8)

151#define \_POSIX\_SYMLINK\_MAX (255)

152#define \_POSIX\_SYMLOOP\_MAX (8)

153#define \_POSIX\_THREAD\_DESTRUCTOR\_ITERATIONS (4)

154#define \_POSIX\_THREAD\_KEYS\_MAX (128)

155#define \_POSIX\_THREAD\_THREADS\_MAX (64)

156#define \_POSIX\_TIMER\_MAX (32)

157#define \_POSIX\_TRACE\_EVENT\_NAME\_MAX (30)

158#define \_POSIX\_TRACE\_NAME\_MAX (8)

159#define \_POSIX\_TRACE\_SYS\_MAX (8)

160#define \_POSIX\_TRACE\_USER\_EVENT\_MAX (32)

161#define \_POSIX\_TTY\_NAME\_MAX (9)

162#define \_POSIX\_TZNAME\_MAX (6)

163#define \_POSIX2\_BC\_BASE\_MAX (99)

164#define \_POSIX2\_BC\_DIM\_MAX (2048)

165#define \_POSIX2\_BC\_SCALE\_MAX (99)

166#define \_POSIX2\_BC\_STRING\_MAX (1000)

167#define \_POSIX2\_CHARCLASS\_NAME\_MAX (14)

168#define \_POSIX2\_COLL\_WEIGHTS\_MAX (2)

169#define \_POSIX2\_EXPR\_NEST\_MAX (32)

170#define \_POSIX2\_LINE\_MAX (2048)

171#define \_XOPEN\_IOV\_MAX (16)

172#define \_XOPEN\_NAME\_MAX (255)

173#define \_XOPEN\_PATH\_MAX (1024)

174

175/\* Other invariant values \*/

[ 176](unistd_8h.md#a82c429c39d68f08d56e4bfdb050fe54a)#define NL\_LANGMAX (14)

[ 177](unistd_8h.md#a7e7a512ab4395a4bb0be4ff872764e45)#define NL\_MSGMAX (32767)

[ 178](unistd_8h.md#a5dd5a06bde8cda4edb4dfda129375a1a)#define NL\_SETMAX (255)

[ 179](unistd_8h.md#a934658c7b37ed12672f76ec304a5b460)#define NL\_TEXTMAX (\_POSIX2\_LINE\_MAX)

[ 180](unistd_8h.md#a3b04cc1d4ce6930b578eede1f1c6ebfc)#define NZERO (20)

181

182/\* Runtime invariant values \*/

[ 183](unistd_8h.md#a0b4029afb1dcaf401c08b7b147d00cec)#define AIO\_LISTIO\_MAX \_POSIX\_AIO\_LISTIO\_MAX

[ 184](unistd_8h.md#a0889d4ed1489519e1e8a83ca6f212c5a)#define AIO\_MAX \_POSIX\_AIO\_MAX

[ 185](unistd_8h.md#aa9d8b79923c4fc549c074fc387ef65c9)#define AIO\_PRIO\_DELTA\_MAX (0)

[ 186](unistd_8h.md#a86025bd0a07f29a6ae97f310ff9c701c)#define DELAYTIMER\_MAX \_POSIX\_DELAYTIMER\_MAX

[ 187](unistd_8h.md#ac956117a90023ec0971b8f9fce9dec75)#define HOST\_NAME\_MAX COND\_CODE\_1(CONFIG\_NETWORKING, \

188 (NET\_HOSTNAME\_MAX\_LEN), \

189 (\_POSIX\_HOST\_NAME\_MAX))

[ 190](unistd_8h.md#af3b7f7833ae69cac7adf84f5973715fe)#define LOGIN\_NAME\_MAX \_POSIX\_LOGIN\_NAME\_MAX

[ 191](unistd_8h.md#abea867e23b4ca9316a0a7511f1b783d3)#define MQ\_OPEN\_MAX \_POSIX\_MQ\_OPEN\_MAX

[ 192](unistd_8h.md#ad1516b4f64b6dc890b1fa3bf576bfef9)#define MQ\_PRIO\_MAX \_POSIX\_MQ\_PRIO\_MAX

193

194#ifndef PAGE\_SIZE

[ 195](unistd_8h.md#a7d467c1d283fdfa1f2081ba1e0d01b6e)#define PAGE\_SIZE BIT(CONFIG\_POSIX\_PAGE\_SIZE\_BITS)

196#endif

197

198#ifndef PAGESIZE

[ 199](unistd_8h.md#a519adc2af3ba06a8f0548b6690050a89)#define PAGESIZE PAGE\_SIZE

200#endif

201

[ 202](unistd_8h.md#a1d96b13a4ba5975d724c5fe13788a957)#define PTHREAD\_DESTRUCTOR\_ITERATIONS \_POSIX\_THREAD\_DESTRUCTOR\_ITERATIONS

[ 203](unistd_8h.md#a0a23e66e087bcf5c253b9b2746f19a64)#define PTHREAD\_KEYS\_MAX COND\_CODE\_1(CONFIG\_PTHREAD\_IPC, \

204 (CONFIG\_MAX\_PTHREAD\_KEY\_COUNT), \

205 (\_POSIX\_THREAD\_KEYS\_MAX))

[ 206](unistd_8h.md#ab8f25dec585d6255fcf40b67db66c1c5)#define PTHREAD\_THREADS\_MAX COND\_CODE\_1(CONFIG\_PTHREAD\_IPC, \

207 (CONFIG\_MAX\_PTHREAD\_COUNT), \

208 (0))

[ 209](unistd_8h.md#a829c888ff8820c37384a5531577cea33)#define SEM\_NSEMS\_MAX \_POSIX\_SEM\_NSEMS\_MAX

[ 210](unistd_8h.md#a2961bb23950351c6b10976674c27ddaf)#define SEM\_VALUE\_MAX CONFIG\_SEM\_VALUE\_MAX

[ 211](unistd_8h.md#a649781c35d0360b7d68ef6d55f2aa668)#define SIGQUEUE\_MAX \_POSIX\_SIGQUEUE\_MAX

[ 212](unistd_8h.md#a238bb3d2a0e88f9ff3e46a6affd7f61d)#define STREAM\_MAX \_POSIX\_STREAM\_MAX

[ 213](unistd_8h.md#a41170bbc4e205b3bc9c2b06033aecc17)#define SYMLOOP\_MAX \_POSIX\_SYMLOOP\_MAX

[ 214](unistd_8h.md#a9cb39fc9fca65abcf086c5b293db3772)#define TIMER\_MAX CONFIG\_MAX\_TIMER\_COUNT

[ 215](unistd_8h.md#a8e87ff1f5de326c7161ef933ff2fb0f1)#define TTY\_NAME\_MAX \_POSIX\_TTY\_NAME\_MAX

[ 216](unistd_8h.md#afb3fe48998f8d32cfb7047b917a8039e)#define TZNAME\_MAX \_POSIX\_TZNAME\_MAX

217

218/\* Pathname variable values \*/

[ 219](unistd_8h.md#a34ef6afc1709d5686f1353804aa03e88)#define FILESIZEBITS (32)

[ 220](unistd_8h.md#aa9c42ba60b7eac67360d9804a99e8bba)#define POSIX\_ALLOC\_SIZE\_MIN (256)

[ 221](unistd_8h.md#a9d04829540462d79aa8751d230987d8b)#define POSIX\_REC\_INCR\_XFER\_SIZE (1024)

[ 222](unistd_8h.md#a17269b771b87209b99c9698c782f0d9b)#define POSIX\_REC\_MAX\_XFER\_SIZE (32767)

[ 223](unistd_8h.md#a3dae40a21514758cfd61dfb8f159c6f4)#define POSIX\_REC\_MIN\_XFER\_SIZE (1)

[ 224](unistd_8h.md#a40069c33a92e401df7b3b09d1e65ce55)#define POSIX\_REC\_XFER\_ALIGN (4)

[ 225](unistd_8h.md#af552b1b86caac064b8d74f73ac9d3f0c)#define SYMLINK\_MAX \_POSIX\_SYMLINK\_MAX

226

227#ifdef CONFIG\_POSIX\_API

228/\* File related operations \*/

229int [close](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086)(int file);

230[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) write(int file, const void \*buffer, size\_t count);

231[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) read(int file, void \*buffer, size\_t count);

232[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) lseek(int file, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, int whence);

233

234/\* File System related operations \*/

235int rename(const char \*old, const char \*newp);

236int unlink(const char \*path);

237int [stat](include_2zephyr_2posix_2sys_2stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)(const char \*path, struct [stat](structstat.md) \*buf);

238int [mkdir](include_2zephyr_2posix_2sys_2stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)(const char \*path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) mode);

239

240FUNC\_NORETURN void \_exit(int status);

241

242#ifdef CONFIG\_NETWORKING

243static inline int [gethostname](group__bsd__sockets.md#ga14fe74115e6133e1be596c327047b0ca)(char \*buf, size\_t len)

244{

245 return [zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)(buf, len);

246}

247#endif /\* CONFIG\_NETWORKING \*/

248

249#endif /\* CONFIG\_POSIX\_API \*/

250

251#ifdef CONFIG\_GETOPT

252int getopt(int argc, char \*const argv[], const char \*optstring);

253extern char \*optarg;

254extern int opterr, optind, optopt;

255#endif

256

[ 257](unistd_8h.md#ac61b207337ca21b3b309593fd1a0cb82)[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df) [getpid](unistd_8h.md#ac61b207337ca21b3b309593fd1a0cb82)(void);

[ 258](unistd_8h.md#aaa1de6debea33c41fbfaa909e813c2f4)unsigned [sleep](unistd_8h.md#aaa1de6debea33c41fbfaa909e813c2f4)(unsigned int seconds);

[ 259](unistd_8h.md#a59715f1a0a2ee4dc75e8343aca15c1dd)int [usleep](unistd_8h.md#a59715f1a0a2ee4dc75e8343aca15c1dd)([useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342) useconds);

260

261#ifdef CONFIG\_POSIX\_SYSCONF

262#define \_\_z\_posix\_sysconf\_SC\_ADVISORY\_INFO \_POSIX\_ADVISORY\_INFO

263#define \_\_z\_posix\_sysconf\_SC\_ASYNCHRONOUS\_IO \_POSIX\_ASYNCHRONOUS\_IO

264#define \_\_z\_posix\_sysconf\_SC\_BARRIERS \_POSIX\_BARRIERS

265#define \_\_z\_posix\_sysconf\_SC\_CLOCK\_SELECTION \_POSIX\_CLOCK\_SELECTION

266#define \_\_z\_posix\_sysconf\_SC\_CPUTIME \_POSIX\_CPUTIME

267#define \_\_z\_posix\_sysconf\_SC\_FSYNC \_POSIX\_FSYNC

268#define \_\_z\_posix\_sysconf\_SC\_IPV6 \_POSIX\_IPV6

269#define \_\_z\_posix\_sysconf\_SC\_JOB\_CONTROL \_POSIX\_JOB\_CONTROL

270#define \_\_z\_posix\_sysconf\_SC\_MAPPED\_FILE \_POSIX\_MAPPED\_FILES

271#define \_\_z\_posix\_sysconf\_SC\_MEMLOCK \_POSIX\_MEMLOCK

272#define \_\_z\_posix\_sysconf\_SC\_MEMLOCK\_RANGE \_POSIX\_MEMLOCK\_RANGE

273#define \_\_z\_posix\_sysconf\_SC\_MEMORY\_PROTECTION \_POSIX\_MEMORY\_PROTECTION

274#define \_\_z\_posix\_sysconf\_SC\_MESSAGE\_PASSING \_POSIX\_MESSAGE\_PASSING

275#define \_\_z\_posix\_sysconf\_SC\_MONOTONIC\_CLOCK \_POSIX\_MONOTONIC\_CLOCK

276#define \_\_z\_posix\_sysconf\_SC\_PRIORITIZED\_IO \_POSIX\_PRIORITIZED\_IO

277#define \_\_z\_posix\_sysconf\_SC\_PRIORITY\_SCHEDULING \_POSIX\_PRIORITY\_SCHEDULING

278#define \_\_z\_posix\_sysconf\_SC\_RAW\_SOCKETS \_POSIX\_RAW\_SOCKETS

279#define \_\_z\_posix\_sysconf\_SC\_RE\_DUP\_MAX \_POSIX\_RE\_DUP\_MAX

280#define \_\_z\_posix\_sysconf\_SC\_READER\_WRITER\_LOCKS \_POSIX\_READER\_WRITER\_LOCKS

281#define \_\_z\_posix\_sysconf\_SC\_REALTIME\_SIGNALS \_POSIX\_REALTIME\_SIGNALS

282#define \_\_z\_posix\_sysconf\_SC\_REGEXP \_POSIX\_REGEXP

283#define \_\_z\_posix\_sysconf\_SC\_SAVED\_IDS \_POSIX\_SAVED\_IDS

284#define \_\_z\_posix\_sysconf\_SC\_SEMAPHORES \_POSIX\_SEMAPHORES

285#define \_\_z\_posix\_sysconf\_SC\_SHARED\_MEMORY\_OBJECTS \_POSIX\_SHARED\_MEMORY\_OBJECTS

286#define \_\_z\_posix\_sysconf\_SC\_SHELL \_POSIX\_SHELL

287#define \_\_z\_posix\_sysconf\_SC\_SPAWN \_POSIX\_SPAWN

288#define \_\_z\_posix\_sysconf\_SC\_SPIN\_LOCKS \_POSIX\_SPIN\_LOCKS

289#define \_\_z\_posix\_sysconf\_SC\_SPORADIC\_SERVER \_POSIX\_SPORADIC\_SERVER

290#define \_\_z\_posix\_sysconf\_SC\_SS\_REPL\_MAX \_POSIX\_SS\_REPL\_MAX

291#define \_\_z\_posix\_sysconf\_SC\_SYNCHRONIZED\_IO \_POSIX\_SYNCHRONIZED\_IO

292#define \_\_z\_posix\_sysconf\_SC\_THREAD\_ATTR\_STACKADDR \_POSIX\_THREAD\_ATTR\_STACKADDR

293#define \_\_z\_posix\_sysconf\_SC\_THREAD\_ATTR\_STACKSIZE \_POSIX\_THREAD\_ATTR\_STACKSIZE

294#define \_\_z\_posix\_sysconf\_SC\_THREAD\_CPUTIME \_POSIX\_THREAD\_CPUTIME

295#define \_\_z\_posix\_sysconf\_SC\_THREAD\_PRIO\_INHERIT \_POSIX\_THREAD\_PRIO\_INHERIT

296#define \_\_z\_posix\_sysconf\_SC\_THREAD\_PRIO\_PROTECT \_POSIX\_THREAD\_PRIO\_PROTECT

297#define \_\_z\_posix\_sysconf\_SC\_THREAD\_PRIORITY\_SCHEDULING \_POSIX\_THREAD\_PRIORITY\_SCHEDULING

298#define \_\_z\_posix\_sysconf\_SC\_THREAD\_PROCESS\_SHARED \_POSIX\_THREAD\_PROCESS\_SHARED

299#define \_\_z\_posix\_sysconf\_SC\_THREAD\_ROBUST\_PRIO\_INHERIT \_POSIX\_THREAD\_ROBUST\_PRIO\_INHERIT

300#define \_\_z\_posix\_sysconf\_SC\_THREAD\_ROBUST\_PRIO\_PROTECT \_POSIX\_THREAD\_ROBUST\_PRIO\_PROTECT

301#define \_\_z\_posix\_sysconf\_SC\_THREAD\_SAFE\_FUNCTIONS \_POSIX\_THREAD\_SAFE\_FUNCTIONS

302#define \_\_z\_posix\_sysconf\_SC\_THREAD\_SPORADIC\_SERVER \_POSIX\_THREAD\_SPORADIC\_SERVER

303#define \_\_z\_posix\_sysconf\_SC\_THREADS \_POSIX\_THREADS

304#define \_\_z\_posix\_sysconf\_SC\_TIMEOUTS \_POSIX\_TIMEOUTS

305#define \_\_z\_posix\_sysconf\_SC\_TIMERS \_POSIX\_TIMERS

306#define \_\_z\_posix\_sysconf\_SC\_TRACE \_POSIX\_TRACE

307#define \_\_z\_posix\_sysconf\_SC\_TRACE\_EVENT\_FILTER \_POSIX\_TRACE\_EVENT\_FILTER

308#define \_\_z\_posix\_sysconf\_SC\_TRACE\_EVENT\_NAME\_MAX \_POSIX\_TRACE\_EVENT\_NAME\_MAX

309#define \_\_z\_posix\_sysconf\_SC\_TRACE\_INHERIT \_POSIX\_TRACE\_INHERIT

310#define \_\_z\_posix\_sysconf\_SC\_TRACE\_LOG \_POSIX\_TRACE\_LOG

311#define \_\_z\_posix\_sysconf\_SC\_TRACE\_NAME\_MAX \_POSIX\_TRACE\_NAME\_MAX

312#define \_\_z\_posix\_sysconf\_SC\_TRACE\_SYS\_MAX \_POSIX\_TRACE\_SYS\_MAX

313#define \_\_z\_posix\_sysconf\_SC\_TRACE\_USER\_EVENT\_MAX \_POSIX\_TRACE\_USER\_EVENT\_MAX

314#define \_\_z\_posix\_sysconf\_SC\_TYPED\_MEMORY\_OBJECTS \_POSIX\_TYPED\_MEMORY\_OBJECTS

315#define \_\_z\_posix\_sysconf\_SC\_VERSION \_POSIX\_VERSION

316#define \_\_z\_posix\_sysconf\_SC\_V7\_ILP32\_OFF32 \_POSIX\_V7\_ILP32\_OFF32

317#define \_\_z\_posix\_sysconf\_SC\_V7\_ILP32\_OFFBIG \_POSIX\_V7\_ILP32\_OFFBIG

318#define \_\_z\_posix\_sysconf\_SC\_V7\_LP64\_OFF64 \_POSIX\_V7\_LP64\_OFF64

319#define \_\_z\_posix\_sysconf\_SC\_V7\_LPBIG\_OFFBIG \_POSIX\_V7\_LPBIG\_OFFBIG

320#define \_\_z\_posix\_sysconf\_SC\_V6\_ILP32\_OFF32 \_POSIX\_V6\_ILP32\_OFF32

321#define \_\_z\_posix\_sysconf\_SC\_V6\_ILP32\_OFFBIG \_POSIX\_V6\_ILP32\_OFFBIG

322#define \_\_z\_posix\_sysconf\_SC\_V6\_LP64\_OFF64 \_POSIX\_V6\_LP64\_OFF64

323#define \_\_z\_posix\_sysconf\_SC\_V6\_LPBIG\_OFFBIG \_POSIX\_V6\_LPBIG\_OFFBIG

324#define \_\_z\_posix\_sysconf\_SC\_BC\_BASE\_MAX \_POSIX2\_BC\_BASE\_MAX

325#define \_\_z\_posix\_sysconf\_SC\_BC\_DIM\_MAX \_POSIX2\_BC\_DIM\_MAX

326#define \_\_z\_posix\_sysconf\_SC\_BC\_SCALE\_MAX \_POSIX2\_BC\_SCALE\_MAX

327#define \_\_z\_posix\_sysconf\_SC\_BC\_STRING\_MAX \_POSIX2\_BC\_STRING\_MAX

328#define \_\_z\_posix\_sysconf\_SC\_2\_C\_BIND \_POSIX2\_C\_BIND

329#define \_\_z\_posix\_sysconf\_SC\_2\_C\_DEV \_POSIX2\_C\_DEV

330#define \_\_z\_posix\_sysconf\_SC\_2\_CHAR\_TERM \_POSIX2\_CHAR\_TERM

331#define \_\_z\_posix\_sysconf\_SC\_COLL\_WEIGHTS\_MAX \_POSIX2\_COLL\_WEIGHTS\_MAX

332#define \_\_z\_posix\_sysconf\_SC\_DELAYTIMER\_MAX \_POSIX2\_DELAYTIMER\_MAX

333#define \_\_z\_posix\_sysconf\_SC\_EXPR\_NEST\_MAX \_POSIX2\_EXPR\_NEST\_MAX

334#define \_\_z\_posix\_sysconf\_SC\_2\_FORT\_DEV \_POSIX2\_FORT\_DEV

335#define \_\_z\_posix\_sysconf\_SC\_2\_FORT\_RUN \_POSIX2\_FORT\_RUN

336#define \_\_z\_posix\_sysconf\_SC\_LINE\_MAX \_POSIX2\_LINE\_MAX

337#define \_\_z\_posix\_sysconf\_SC\_2\_LOCALEDEF \_POSIX2\_LOCALEDEF

338#define \_\_z\_posix\_sysconf\_SC\_2\_PBS \_POSIX2\_PBS

339#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_ACCOUNTING \_POSIX2\_PBS\_ACCOUNTING

340#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_CHECKPOINT \_POSIX2\_PBS\_CHECKPOINT

341#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_LOCATE \_POSIX2\_PBS\_LOCATE

342#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_MESSAGE \_POSIX2\_PBS\_MESSAGE

343#define \_\_z\_posix\_sysconf\_SC\_2\_PBS\_TRACK \_POSIX2\_PBS\_TRACK

344#define \_\_z\_posix\_sysconf\_SC\_2\_SW\_DEV \_POSIX2\_SW\_DEV

345#define \_\_z\_posix\_sysconf\_SC\_2\_UPE \_POSIX2\_UPE

346#define \_\_z\_posix\_sysconf\_SC\_2\_VERSION \_POSIX2\_VERSION

347#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_CRYPT \_XOPEN\_CRYPT

348#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_ENH\_I18N \_XOPEN\_ENH\_I18N

349#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_REALTIME \_XOPEN\_REALTIME

350#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_REALTIME\_THREADS \_XOPEN\_REALTIME\_THREADS

351#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_SHM \_XOPEN\_SHM

352#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_STREAMS \_XOPEN\_STREAMS

353#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_UNIX \_XOPEN\_UNIX

354#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_UUCP \_XOPEN\_UUCP

355#define \_\_z\_posix\_sysconf\_SC\_XOPEN\_VERSION \_XOPEN\_VERSION

356#define \_\_z\_posix\_sysconf\_SC\_CLK\_TCK (100L)

357#define \_\_z\_posix\_sysconf\_SC\_GETGR\_R\_SIZE\_MAX (0L)

358#define \_\_z\_posix\_sysconf\_SC\_GETPW\_R\_SIZE\_MAX (0L)

359#define \_\_z\_posix\_sysconf\_SC\_AIO\_LISTIO\_MAX AIO\_LISTIO\_MAX

360#define \_\_z\_posix\_sysconf\_SC\_AIO\_MAX AIO\_MAX

361#define \_\_z\_posix\_sysconf\_SC\_AIO\_PRIO\_DELTA\_MAX AIO\_PRIO\_DELTA\_MAX

362#define \_\_z\_posix\_sysconf\_SC\_ARG\_MAX ARG\_MAX

363#define \_\_z\_posix\_sysconf\_SC\_ATEXIT\_MAX ATEXIT\_MAX

364#define \_\_z\_posix\_sysconf\_SC\_CHILD\_MAX CHILD\_MAX

365#define \_\_z\_posix\_sysconf\_SC\_HOST\_NAME\_MAX HOST\_NAME\_MAX

366#define \_\_z\_posix\_sysconf\_SC\_IOV\_MAX IOV\_MAX

367#define \_\_z\_posix\_sysconf\_SC\_LOGIN\_NAME\_MAX LOGIN\_NAME\_MAX

368#define \_\_z\_posix\_sysconf\_SC\_NGROUPS\_MAX \_POSIX\_NGROUPS\_MAX

369#define \_\_z\_posix\_sysconf\_SC\_MQ\_OPEN\_MAX MQ\_OPEN\_MAX

370#define \_\_z\_posix\_sysconf\_SC\_MQ\_PRIO\_MAX MQ\_PRIO\_MAX

371#define \_\_z\_posix\_sysconf\_SC\_OPEN\_MAX CONFIG\_POSIX\_MAX\_FDS

372#define \_\_z\_posix\_sysconf\_SC\_PAGE\_SIZE PAGE\_SIZE

373#define \_\_z\_posix\_sysconf\_SC\_PAGESIZE PAGESIZE

374#define \_\_z\_posix\_sysconf\_SC\_THREAD\_DESTRUCTOR\_ITERATIONS PTHREAD\_DESTRUCTOR\_ITERATIONS

375#define \_\_z\_posix\_sysconf\_SC\_THREAD\_KEYS\_MAX PTHREAD\_KEYS\_MAX

376#define \_\_z\_posix\_sysconf\_SC\_THREAD\_STACK\_MIN PTHREAD\_STACK\_MIN

377#define \_\_z\_posix\_sysconf\_SC\_THREAD\_THREADS\_MAX PTHREAD\_THREADS\_MAX

378#define \_\_z\_posix\_sysconf\_SC\_RTSIG\_MAX RTSIG\_MAX

379#define \_\_z\_posix\_sysconf\_SC\_SEM\_NSEMS\_MAX SEM\_NSEMS\_MAX

380#define \_\_z\_posix\_sysconf\_SC\_SEM\_VALUE\_MAX SEM\_VALUE\_MAX

381#define \_\_z\_posix\_sysconf\_SC\_SIGQUEUE\_MAX SIGQUEUE\_MAX

382#define \_\_z\_posix\_sysconf\_SC\_STREAM\_MAX STREAM\_MAX

383#define \_\_z\_posix\_sysconf\_SC\_SYMLOOP\_MAX SYMLOOP\_MAX

384#define \_\_z\_posix\_sysconf\_SC\_TIMER\_MAX TIMER\_MAX

385#define \_\_z\_posix\_sysconf\_SC\_TTY\_NAME\_MAX TTY\_NAME\_MAX

386#define \_\_z\_posix\_sysconf\_SC\_TZNAME\_MAX TZNAME\_MAX

387

388#define sysconf(x) (long)CONCAT(\_\_z\_posix\_sysconf, x)

389

390#endif /\* CONFIG\_POSIX\_SYSCONF \*/

391

392#ifdef \_\_cplusplus

393}

394#endif

395

396#endif /\* ZEPHYR\_INCLUDE\_POSIX\_UNISTD\_H\_ \*/

[fs.h](fs_8h.md)

[gethostname](group__bsd__sockets.md#ga14fe74115e6133e1be596c327047b0ca)

static int gethostname(char \*buf, size\_t len)

POSIX wrapper for zsock\_gethostname.

**Definition** socket.h:1020

[close](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086)

static int close(int sock)

POSIX wrapper for zsock\_close.

**Definition** socket.h:845

[zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)

int zsock\_gethostname(char \*buf, size\_t len)

Get local host name.

[hostname.h](hostname_8h.md)

Hostname configuration definitions.

[stat.h](include_2zephyr_2posix_2sys_2stat_8h.md)

[stat](include_2zephyr_2posix_2sys_2stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)

int stat(const char \*\_\_restrict \_\_path, struct stat \*\_\_restrict \_\_sbuf)

[mkdir](include_2zephyr_2posix_2sys_2stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)

int mkdir(const char \*\_path, mode\_t \_\_mode)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00)

unsigned int mode\_t

**Definition** types.h:14

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[posix\_types.h](posix__types_8h.md)

[useconds\_t](posix__types_8h.md#a1cf3c794977f92f3ccf2e041a68f3342)

unsigned long useconds\_t

**Definition** posix\_types.h:27

[pid\_t](posix__types_8h.md#a288e13e815d43b06e75819f8939524df)

int pid\_t

**Definition** posix\_types.h:24

[signal.h](signal_8h.md)

[stat](structstat.md)

**Definition** stat.h:92

[usleep](unistd_8h.md#a59715f1a0a2ee4dc75e8343aca15c1dd)

int usleep(useconds\_t useconds)

[sleep](unistd_8h.md#aaa1de6debea33c41fbfaa909e813c2f4)

unsigned sleep(unsigned int seconds)

[getpid](unistd_8h.md#ac61b207337ca21b3b309593fd1a0cb82)

pid\_t getpid(void)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [unistd.h](unistd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
