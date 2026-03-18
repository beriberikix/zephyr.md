---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2sys__clock_8h_source.html
original_path: doxygen/html/include_2zephyr_2sys__clock_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sys\_clock.h

[Go to the documentation of this file.](include_2zephyr_2sys__clock_8h.md)

1/\*

2 \* Copyright (c) 2014-2015 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

15

16#ifndef ZEPHYR\_INCLUDE\_SYS\_CLOCK\_H\_

17#define ZEPHYR\_INCLUDE\_SYS\_CLOCK\_H\_

18

19#include <[zephyr/sys/util.h](util_8h.md)>

20#include <[zephyr/sys/dlist.h](dlist_8h.md)>

21

22#include <[zephyr/toolchain.h](toolchain_8h.md)>

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

25#include <[zephyr/sys/time\_units.h](time__units_8h.md)>

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

[ 51](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)#define K\_TICKS\_FOREVER ((k\_ticks\_t) -1)

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

[ 98](group__clock__apis.md#gaa6094c8f66b81269ce912804b796d2c7)#define MIN\_PER\_HOUR 60U

99

[ 101](group__clock__apis.md#gafcbf34dc5c48a91fe5f6efe4c1bae745)#define HOUR\_PER\_DAY 24U

102

[ 104](group__clock__apis.md#ga6a69d6cbdab5f24c2e66959293f210c1)#define USEC\_PER\_SEC ((USEC\_PER\_MSEC) \* (MSEC\_PER\_SEC))

105

[ 107](group__clock__apis.md#ga0501e82515b2bdf36453c4cc80f5e0cc)#define NSEC\_PER\_SEC ((NSEC\_PER\_USEC) \* (USEC\_PER\_MSEC) \* (MSEC\_PER\_SEC))

108

110

112#define Z\_TIMEOUT\_NO\_WAIT ((k\_timeout\_t) {0})

113#if defined(\_\_cplusplus) && ((\_\_cplusplus - 0) < 202002L)

114#define Z\_TIMEOUT\_TICKS(t) ((k\_timeout\_t) { (t) })

115#else

116#define Z\_TIMEOUT\_TICKS(t) ((k\_timeout\_t) { .ticks = (t) })

117#endif

118#define Z\_FOREVER Z\_TIMEOUT\_TICKS(K\_TICKS\_FOREVER)

119

120#ifdef CONFIG\_TIMEOUT\_64BIT

121# define Z\_TIMEOUT\_MS(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_ms\_to\_ticks\_ceil64(MAX(t, 0)))

122# define Z\_TIMEOUT\_US(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_us\_to\_ticks\_ceil64(MAX(t, 0)))

123# define Z\_TIMEOUT\_NS(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_ns\_to\_ticks\_ceil64(MAX(t, 0)))

124# define Z\_TIMEOUT\_CYC(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_cyc\_to\_ticks\_ceil64(MAX(t, 0)))

125# define Z\_TIMEOUT\_MS\_TICKS(t) ((k\_ticks\_t)k\_ms\_to\_ticks\_ceil64(MAX(t, 0)))

126#else

127# define Z\_TIMEOUT\_MS(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_ms\_to\_ticks\_ceil32(MAX(t, 0)))

128# define Z\_TIMEOUT\_US(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_us\_to\_ticks\_ceil32(MAX(t, 0)))

129# define Z\_TIMEOUT\_NS(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_ns\_to\_ticks\_ceil32(MAX(t, 0)))

130# define Z\_TIMEOUT\_CYC(t) Z\_TIMEOUT\_TICKS((k\_ticks\_t)k\_cyc\_to\_ticks\_ceil32(MAX(t, 0)))

131# define Z\_TIMEOUT\_MS\_TICKS(t) ((k\_ticks\_t)k\_ms\_to\_ticks\_ceil32(MAX(t, 0)))

132#endif

133

134/\* Converts between absolute timeout expiration values (packed into

135 \* the negative space below K\_TICKS\_FOREVER) and (non-negative) delta

136 \* timeout values. If the result of Z\_TICK\_ABS(t) is >= 0, then the

137 \* value was an absolute timeout with the returned expiration time.

138 \* Note that this macro is bidirectional: Z\_TICK\_ABS(Z\_TICK\_ABS(t)) ==

139 \* t for all inputs, and that the representation of K\_TICKS\_FOREVER is

140 \* the same value in both spaces! Clever, huh?

141 \*/

142#define Z\_TICK\_ABS(t) (K\_TICKS\_FOREVER - 1 - (t))

143

144/\* added tick needed to account for tick in progress \*/

145#define \_TICK\_ALIGN 1

146

148

149#if defined(CONFIG\_SYS\_CLOCK\_EXISTS) && \

150 (CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC == 0)

151#error "SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC must be non-zero!"

152#endif

153

154

155/\* kernel clocks \*/

156

157/\*

158 \* We default to using 64-bit intermediates in timescale conversions,

159 \* but if the HW timer cycles/sec, ticks/sec and ms/sec are all known

160 \* to be nicely related, then we can cheat with 32 bits instead.

161 \*/

166

167#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

168

169#if defined(CONFIG\_TIMER\_READS\_ITS\_FREQUENCY\_AT\_RUNTIME) || \

170 (MSEC\_PER\_SEC % CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC) || \

171 (CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC % CONFIG\_SYS\_CLOCK\_TICKS\_PER\_SEC)

172#define \_NEED\_PRECISE\_TICK\_MS\_CONVERSION

173#endif

174

175#endif

176

[ 181](group__clock__apis.md#ga59d9bd47b0caa662f0e289cf3df83a82)#define SYS\_CLOCK\_HW\_CYCLES\_TO\_NS\_AVG(X, NCYCLES) \

182 (uint32\_t)(k\_cyc\_to\_ns\_floor64(X) / NCYCLES)

183

[ 191](group__clock__apis.md#ga38f64e34c3f5b179e1f65d96911823cd)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_clock\_tick\_get\_32](group__clock__apis.md#ga38f64e34c3f5b179e1f65d96911823cd)(void);

192

[ 200](group__clock__apis.md#ga53e768db46e328e433848c62739c82e0)[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sys\_clock\_tick\_get](group__clock__apis.md#ga53e768db46e328e433848c62739c82e0)(void);

201

202#ifndef CONFIG\_SYS\_CLOCK\_EXISTS

203#define sys\_clock\_tick\_get() (0)

204#define sys\_clock\_tick\_get\_32() (0)

205#endif

206

207#ifdef CONFIG\_SYS\_CLOCK\_EXISTS

208

[ 219](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe)typedef struct { [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe); } [k\_timepoint\_t](structk__timepoint__t.md);

220

[ 237](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)[k\_timepoint\_t](structk__timepoint__t.md) [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)([k\_timeout\_t](structk__timeout__t.md) timeout);

238

[ 252](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)[k\_timeout\_t](structk__timeout__t.md) [sys\_timepoint\_timeout](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)([k\_timepoint\_t](structk__timepoint__t.md) timepoint);

253

261\_\_deprecated

[ 262](group__clock__apis.md#ga2bc4243022dba41becfd37a47aabe837)static inline [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [sys\_clock\_timeout\_end\_calc](group__clock__apis.md#ga2bc4243022dba41becfd37a47aabe837)([k\_timeout\_t](structk__timeout__t.md) timeout)

263{

264 [k\_timepoint\_t](structk__timepoint__t.md) tp = [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)(timeout);

265

266 return tp.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe);

267}

268

[ 279](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998)static inline int [sys\_timepoint\_cmp](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998)([k\_timepoint\_t](structk__timepoint__t.md) a, [k\_timepoint\_t](structk__timepoint__t.md) b)

280{

281 if (a.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe) == b.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe)) {

282 return 0;

283 }

284 return a.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe) < b.[tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe) ? -1 : 1;

285}

286

287#else

288

289/\*

290 \* When timers are configured out, timepoints can't relate to anything.

291 \* The best we can do is to preserve whether or not they are derived from

292 \* K\_NO\_WAIT. Anything else will translate back to K\_FOREVER.

293 \*/

294typedef struct { bool wait; } [k\_timepoint\_t](structk__timepoint__t.md);

295

296static inline [k\_timepoint\_t](structk__timepoint__t.md) [sys\_timepoint\_calc](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33)([k\_timeout\_t](structk__timeout__t.md) timeout)

297{

298 [k\_timepoint\_t](structk__timepoint__t.md) timepoint;

299

300 timepoint.wait = ![K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)(timeout, Z\_TIMEOUT\_NO\_WAIT);

301 return timepoint;

302}

303

304static inline [k\_timeout\_t](structk__timeout__t.md) [sys\_timepoint\_timeout](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)([k\_timepoint\_t](structk__timepoint__t.md) timepoint)

305{

306 return timepoint.wait ? Z\_FOREVER : Z\_TIMEOUT\_NO\_WAIT;

307}

308

309static inline int [sys\_timepoint\_cmp](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998)([k\_timepoint\_t](structk__timepoint__t.md) a, [k\_timepoint\_t](structk__timepoint__t.md) b)

310{

311 if (a.wait == b.wait) {

312 return 0;

313 }

314 return b.wait ? -1 : 1;

315}

316

317#endif

318

[ 327](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)static inline bool [sys\_timepoint\_expired](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985)([k\_timepoint\_t](structk__timepoint__t.md) timepoint)

328{

329 return [K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)([sys\_timepoint\_timeout](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa)(timepoint), Z\_TIMEOUT\_NO\_WAIT);

330}

331

333

334#ifdef \_\_cplusplus

335}

336#endif

337

338#endif /\* ZEPHYR\_INCLUDE\_SYS\_CLOCK\_H\_ \*/

[dlist.h](dlist_8h.md)

[sys\_clock\_timeout\_end\_calc](group__clock__apis.md#ga2bc4243022dba41becfd37a47aabe837)

static uint64\_t sys\_clock\_timeout\_end\_calc(k\_timeout\_t timeout)

Provided for backward compatibility.

**Definition** sys\_clock.h:262

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

**Definition** sys\_clock.h:327

[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)

uint32\_t k\_ticks\_t

Tick precision used in timeout APIs.

**Definition** sys\_clock.h:48

[K\_TIMEOUT\_EQ](group__clock__apis.md#ga9abf00b34e16ab7ad0883603b6778b1b)

#define K\_TIMEOUT\_EQ(a, b)

Compare timeouts for equality.

**Definition** sys\_clock.h:80

[sys\_timepoint\_cmp](group__clock__apis.md#gaba264a00149527cd70aea717f3b3a998)

static int sys\_timepoint\_cmp(k\_timepoint\_t a, k\_timepoint\_t b)

Compare two timepoint values.

**Definition** sys\_clock.h:279

[types.h](include_2zephyr_2types_8h.md)

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

**Definition** sys\_clock.h:65

[k\_timeout\_t::ticks](structk__timeout__t.md#a492605d3a8c76f0ce2ef129b9f4d40fa)

k\_ticks\_t ticks

**Definition** sys\_clock.h:66

[k\_timepoint\_t](structk__timepoint__t.md)

Kernel timepoint type.

**Definition** sys\_clock.h:219

[k\_timepoint\_t::tick](structk__timepoint__t.md#a33e68c86f68dad539d7c2a70e6f80fbe)

uint64\_t tick

**Definition** sys\_clock.h:219

[time\_units.h](time__units_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys\_clock.h](include_2zephyr_2sys__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
