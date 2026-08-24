---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/clock_8h_source.html
original_path: doxygen/html/clock_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock.h

[Go to the documentation of this file.](clock_8h.md)

1/\*

2 \* Copyright (c) 2014-2015 Wind River Systems, Inc.

3 \* Copyright (c) 2025 Tenstorrent AI ULC

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

17

18#ifndef ZEPHYR\_INCLUDE\_SYS\_CLOCK\_H\_

19#define ZEPHYR\_INCLUDE\_SYS\_CLOCK\_H\_

20

21#include <[zephyr/sys/dlist.h](dlist_8h.md)>

22#include <[zephyr/sys/time\_units.h](time__units_8h.md)>

23#include <[zephyr/sys/util.h](sys_2util_8h.md)>

24#include <[zephyr/toolchain.h](toolchain_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

35

45#ifdef CONFIG\_TIMEOUT\_64BIT

46typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2);

47#else

[ 48](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2);

49#endif

50

[ 51](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)#define K\_TICKS\_FOREVER ((k\_ticks\_t)(-1))

52

[ 65](structk__timeout__t.md)typedef struct {

[ 66](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa) [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) [ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa);

67} [k\_timeout\_t](structk__timeout__t.md);

68

[ 80](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)#define K\_TIMEOUT\_EQ(a, b) ((a).ticks == (b).ticks)

81

[ 83](group__clock__apis.md#ga2180f263d149841a7c1fde663edb84c5)#define NSEC\_PER\_USEC 1000U

84

[ 86](group__clock__apis.md#gad16e9029e202d2dfb4cfae8f09131f8f)#define NSEC\_PER\_MSEC 1000000U

87

[ 89](group__clock__apis.md#ga2d66311052e2bddf914610fb7345ff27)#define USEC\_PER\_MSEC 1000U

90

[ 92](group__clock__apis.md#ga222f9dff749accf8de62bc4b52c7bdcd)#define MSEC\_PER\_SEC 1000U

93

[ 95](group__clock__apis.md#gac47b302f1b8d2a7a9c035c417247be76)#define SEC\_PER\_MIN 60U

96

[ 98](group__clock__apis.md#ga2d540510d5860d7f190d13124956bc57)#define SEC\_PER\_HOUR 3600U

99

[ 101](group__clock__apis.md#ga3aaee30ddedb3f6675aac341a66e39e2)#define SEC\_PER\_DAY 86400U

102

[ 104](group__clock__apis.md#gaa6094c8f66b81269ce912804b796d2c7)#define MIN\_PER\_HOUR 60U

105

[ 107](group__clock__apis.md#gafcbf34dc5c48a91fe5f6efe4c1bae745)#define HOUR\_PER\_DAY 24U

108

[ 110](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)#define USEC\_PER\_SEC ((USEC\_PER\_MSEC) \* (MSEC\_PER\_SEC))

111

[ 113](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)#define NSEC\_PER\_SEC ((NSEC\_PER\_USEC) \* (USEC\_PER\_MSEC) \* (MSEC\_PER\_SEC))

114

116

118#define Z\_TIMEOUT\_NO\_WAIT\_INIT {0}

119#define Z\_TIMEOUT\_NO\_WAIT ((k\_timeout\_t)Z\_TIMEOUT\_NO\_WAIT\_INIT)

120#if defined(\_\_cplusplus) && ((\_\_cplusplus - 0) < 202002L)

121#define Z\_TIMEOUT\_TICKS\_INIT(t) {(t)}

122#else

123#define Z\_TIMEOUT\_TICKS\_INIT(t) {.ticks = (t)}

124#endif

125#define Z\_TIMEOUT\_TICKS(t) ((k\_timeout\_t)Z\_TIMEOUT\_TICKS\_INIT(t))

126#define Z\_FOREVER Z\_TIMEOUT\_TICKS(K\_TICKS\_FOREVER)

127

128#ifdef CONFIG\_TIMEOUT\_64BIT

129#define Z\_TIMEOUT\_MS(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_ms\_to\_ticks\_ceil64(MAX(t, 0)))

130#define Z\_TIMEOUT\_US(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_us\_to\_ticks\_ceil64(MAX(t, 0)))

131#define Z\_TIMEOUT\_NS(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_ns\_to\_ticks\_ceil64(MAX(t, 0)))

132#define Z\_TIMEOUT\_CYC(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_cyc\_to\_ticks\_ceil64(MAX(t, 0)))

133#define Z\_TIMEOUT\_MS\_TICKS(t) ((k\_ticks\_t)k\_ms\_to\_ticks\_ceil64(MAX(t, 0)))

134#else

135#define Z\_TIMEOUT\_MS(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_ms\_to\_ticks\_ceil32(MAX(t, 0)))

136#define Z\_TIMEOUT\_US(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_us\_to\_ticks\_ceil32(MAX(t, 0)))

137#define Z\_TIMEOUT\_NS(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_ns\_to\_ticks\_ceil32(MAX(t, 0)))

138#define Z\_TIMEOUT\_CYC(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_cyc\_to\_ticks\_ceil32(MAX(t, 0)))

139#define Z\_TIMEOUT\_MS\_TICKS(t) ((k\_ticks\_t)k\_ms\_to\_ticks\_ceil32(MAX(t, 0)))

140#endif

141

142/\* Converts between absolute timeout expiration values (packed into

143 \* the negative space below K\_TICKS\_FOREVER) and (non-negative) delta

144 \* timeout values. If the result of Z\_TICK\_ABS(t) is >= 0, then the

145 \* value was an absolute timeout with the returned expiration time.

146 \* Note that this macro is bidirectional: Z\_TICK\_ABS(Z\_TICK\_ABS(t)) ==

147 \* t for all inputs, and that the representation of K\_TICKS\_FOREVER is

148 \* the same value in both spaces! Clever, huh?

149 \*/

150#define Z\_TICK\_ABS(t) (K\_TICKS\_FOREVER - 1 - (t))

151

152/\* Test for relative timeout \*/

153#if CONFIG\_TIMEOUT\_64BIT

154/\* Positive values are relative/delta timeouts and negative values are absolute

155 \* timeouts, except -1 which is reserved for K\_TIMEOUT\_FOREVER. 0 is K\_NO\_WAIT,

156 \* which is historically considered a relative timeout.

157 \* K\_TIMEOUT\_FOREVER is not considered a relative timeout and neither is it

158 \* considerd an absolute timeouts (so !Z\_IS\_TIMEOUT\_RELATIVE() does not

159 \* necessarily mean it is an absolute timeout if ticks == -1);

160 \*/

161#define Z\_IS\_TIMEOUT\_RELATIVE(timeout) (((timeout).ticks) >= 0)

162#else

163#define Z\_IS\_TIMEOUT\_RELATIVE(timeout) true

164#endif

165

166/\* added tick needed to account for tick in progress \*/

167#define \_TICK\_ALIGN 1

168

170

171#ifndef CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME

172#if defined(CONFIG\_SYS\_CLOCK\_EXISTS)

173#if CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC == 0

174#error "SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC must be non-zero!"

175#endif /\* CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC == 0 \*/

176#endif /\* CONFIG\_SYS\_CLOCK\_EXISTS \*/

177#endif /\* CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME \*/

178

179/\* kernel clocks \*/

180

181/\*

182 \* We default to using 64-bit intermediates in timescale conversions,

183 \* but if the HW timer cycles/sec, ticks/sec and ms/sec are all known

184 \* to be nicely related, then we can cheat with 32 bits instead.

185 \*/

190

191#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

192

193#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME) || \

194 (MSEC\_PER\_SEC % CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC) || \

195 (CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC % CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC)

196#define \_NEED\_PRECISE\_TICK\_MS\_CONVERSION

197#endif

198

199#endif

200

[ 205](group__clock__apis.md#ga59d9bd47b0caa662f0e289cf3df83a82)#define SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG(X, NCYCLES) (uint32\_t)(k\_cyc\_to\_ns\_floor64(X) / NCYCLES)

206

[ 214](group__clock__apis.md#ga38f64e34c3f5b179e1f65d96911823cd)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_tick\_get\_32](group__clock__apis.md#ga38f64e34c3f5b179e1f65d96911823cd)(void);

215

[ 223](group__clock__apis.md#ga53e768db46e328e433848c62739c82e0)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sys\_clock\_tick\_get](group__clock__apis.md#ga53e768db46e328e433848c62739c82e0)(void);

224

225#ifndef CONFIG\_SYS\_CLOCK\_EXISTS

226#define sys\_clock\_tick\_get() (0)

227#define sys\_clock\_tick\_get\_32() (0)

228#endif

229

230#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

231

[ 242](structk__timepoint__t.md)typedef struct {

[ 243](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe);

244} [k\_timepoint\_t](structk__timepoint__t.md);

245

[ 262](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)[k\_timepoint\_t](structk__timepoint__t.md) [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)([k\_timeout\_t](structk__timeout__t.md) timeout);

263

[ 277](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)[k\_timeout\_t](structk__timeout__t.md) [sys\_timepoint\_timeout](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)([k\_timepoint\_t](structk__timepoint__t.md) timepoint);

278

[ 289](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998)static inline int [sys\_timepoint\_cmp](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998)([k\_timepoint\_t](structk__timepoint__t.md) a, [k\_timepoint\_t](structk__timepoint__t.md) b)

290{

291 if (a.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe) == b.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe)) {

292 return 0;

293 }

294 return a.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe) < b.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe) ? -1 : 1;

295}

296

297#else

298

299/\*

300 \* When timers are configured out, timepoints can't relate to anything.

301 \* The best we can do is to preserve whether or not they are derived from

302 \* K\_NO\_WAIT. Anything else will translate back to K\_FOREVER.

303 \*/

304typedef struct {

305 bool wait;

306} [k\_timepoint\_t](structk__timepoint__t.md);

307

308static inline [k\_timepoint\_t](structk__timepoint__t.md) [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)([k\_timeout\_t](structk__timeout__t.md) timeout)

309{

310 [k\_timepoint\_t](structk__timepoint__t.md) timepoint;

311

312 timepoint.wait = ![K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, Z\_TIMEOUT\_NO\_WAIT);

313 return timepoint;

314}

315

316static inline [k\_timeout\_t](structk__timeout__t.md) [sys\_timepoint\_timeout](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)([k\_timepoint\_t](structk__timepoint__t.md) timepoint)

317{

318 return timepoint.wait ? Z\_FOREVER : Z\_TIMEOUT\_NO\_WAIT;

319}

320

321static inline int [sys\_timepoint\_cmp](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998)([k\_timepoint\_t](structk__timepoint__t.md) a, [k\_timepoint\_t](structk__timepoint__t.md) b)

322{

323 if (a.wait == b.wait) {

324 return 0;

325 }

326 return b.wait ? -1 : 1;

327}

328

329#endif

330

[ 339](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)static inline bool [sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)([k\_timepoint\_t](structk__timepoint__t.md) timepoint)

340{

341 return [K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)([sys\_timepoint\_timeout](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)(timepoint), Z\_TIMEOUT\_NO\_WAIT);

342}

343

345

350

[ 360](group__clock__apis.md#gac88ce6c820c962691fdc6e0b344bd887)#define SYS\_CLOCK\_REALTIME 1

361

[ 368](group__clock__apis.md#gab8a1a7e619c67e9a86e773097ce3a8e5)#define SYS\_CLOCK\_MONOTONIC 4

369

[ 376](group__clock__apis.md#ga647bea5f74dcf7f6f6fed2c1b78b540f)#define SYS\_TIMER\_ABSTIME 4

377

379/\* forward declaration as workaround for time.h \*/

380struct [timespec](structtimespec.md);

382

[ 399](group__clock__apis.md#gab40851eb5eebbdfdba211eea6967f1ce)\_\_syscall void [sys\_clock\_getrtoffset](group__clock__apis.md#gab40851eb5eebbdfdba211eea6967f1ce)(struct [timespec](structtimespec.md) \*tp);

400

[ 409](group__clock__apis.md#ga92bad374219a4cd32299569c94907877)int [sys\_clock\_gettime](group__clock__apis.md#ga92bad374219a4cd32299569c94907877)(int clock\_id, struct [timespec](structtimespec.md) \*tp);

410

[ 420](group__clock__apis.md#ga297e885a8a95c762ae882e61f7d381b4)\_\_syscall int [sys\_clock\_settime](group__clock__apis.md#ga297e885a8a95c762ae882e61f7d381b4)(int clock\_id, const struct [timespec](structtimespec.md) \*tp);

421

[ 447](group__clock__apis.md#ga01ca6f2ad006ed530ffec06c262ae380)\_\_syscall int [sys\_clock\_nanosleep](group__clock__apis.md#ga01ca6f2ad006ed530ffec06c262ae380)(int clock\_id, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [timespec](structtimespec.md) \*rqtp,

448 struct [timespec](structtimespec.md) \*rmtp);

449

453

454#ifndef CONFIG\_BOARD\_UNIT\_TESTING

455#include <zephyr/syscalls/clock.h>

456#endif

457

458#ifdef \_\_cplusplus

459}

460#endif

461

462#endif /\* ZEPHYR\_INCLUDE\_SYS\_CLOCK\_H\_ \*/

[dlist.h](dlist_8h.md)

[sys\_clock\_nanosleep](group__clock__apis.md#ga01ca6f2ad006ed530ffec06c262ae380)

int sys\_clock\_nanosleep(int clock\_id, int flags, const struct timespec \*rqtp, struct timespec \*rmtp)

Sleep for the specified amount of time with respect to the specified clock.

[sys\_clock\_settime](group__clock__apis.md#ga297e885a8a95c762ae882e61f7d381b4)

int sys\_clock\_settime(int clock\_id, const struct timespec \*tp)

Set the current time for the specified clock.

[sys\_clock\_tick\_get\_32](group__clock__apis.md#ga38f64e34c3f5b179e1f65d96911823cd)

uint32\_t sys\_clock\_tick\_get\_32(void)

Return the lower part of the current system tick count.

[sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)

k\_timepoint\_t sys\_timepoint\_calc(k\_timeout\_t timeout)

Calculate a timepoint value.

[sys\_clock\_tick\_get](group__clock__apis.md#ga53e768db46e328e433848c62739c82e0)

int64\_t sys\_clock\_tick\_get(void)

Return the current system tick count.

[sys\_timepoint\_timeout](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)

k\_timeout\_t sys\_timepoint\_timeout(k\_timepoint\_t timepoint)

Remaining time to given timepoint.

[sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)

static bool sys\_timepoint\_expired(k\_timepoint\_t timepoint)

Indicates if timepoint is expired.

**Definition** clock.h:339

[sys\_clock\_gettime](group__clock__apis.md#ga92bad374219a4cd32299569c94907877)

int sys\_clock\_gettime(int clock\_id, struct timespec \*tp)

Get the current time from the specified clock.

[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)

uint32\_t k\_ticks\_t

Tick precision used in timeout APIs.

**Definition** clock.h:48

[K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)

#define K\_TIMEOUT\_EQ(a, b)

Compare timeouts for equality.

**Definition** clock.h:80

[sys\_clock\_getrtoffset](group__clock__apis.md#gab40851eb5eebbdfdba211eea6967f1ce)

void sys\_clock\_getrtoffset(struct timespec \*tp)

INTERNAL\_HIDDEN.

[sys\_timepoint\_cmp](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998)

static int sys\_timepoint\_cmp(k\_timepoint\_t a, k\_timepoint\_t b)

Compare two timepoint values.

**Definition** clock.h:289

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[k\_timeout\_t::ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa)

k\_ticks\_t ticks

**Definition** clock.h:66

[k\_timepoint\_t](structk__timepoint__t.md)

Kernel timepoint type.

**Definition** clock.h:242

[k\_timepoint\_t::tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe)

uint64\_t tick

**Definition** clock.h:243

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[util.h](sys_2util_8h.md)

Misc utilities.

[time\_units.h](time__units_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [clock.h](clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
