---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ztest__assert_8h_source.html
original_path: doxygen/html/ztest__assert_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_assert.h

[Go to the documentation of this file.](ztest__assert_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_TESTSUITE\_ZTEST\_ASSERT\_H\_

14#define ZEPHYR\_TESTSUITE\_ZTEST\_ASSERT\_H\_

15

16#include <stdarg.h>

17#include <[stdbool.h](stdbool_8h.md)>

18#include <[stdio.h](stdio_8h.md)>

19#include <[string.h](string_8h.md)>

20

21#include <[zephyr/tc\_util.h](tc__util_8h.md)>

22#include <[zephyr/ztest.h](ztest_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 28](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)const char \*[ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(const char \*file);

[ 29](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)void [ztest\_test\_fail](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)(void);

[ 30](ztest__assert_8h.md#ada3b1fcfa71db1bf7787c03ff45256d5)void [ztest\_test\_skip](ztest__assert_8h.md#ada3b1fcfa71db1bf7787c03ff45256d5)(void);

[ 31](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)void [ztest\_test\_expect\_fail](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)(void);

[ 32](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)void [ztest\_skip\_failed\_assumption](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)(void);

33#if CONFIG\_ZTEST\_ASSERT\_VERBOSE == 0

34

35static inline bool z\_zassert\_(bool cond, const char \*file, int line)

36{

37 if (cond == false) {

38 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Assertion failed at %s:%d\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

39 line);

40 [ztest\_test\_fail](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)();

41 return false;

42 }

43

44 return true;

45}

46

47#define z\_zassert(cond, default\_msg, file, line, func, msg, ...) z\_zassert\_(cond, file, line)

48

49static inline bool z\_zassume\_(bool cond, const char \*file, int line)

50{

51 if (cond == false) {

52 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Assumption failed at %s:%d\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

53 line);

54 [ztest\_skip\_failed\_assumption](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)();

55 return false;

56 }

57

58 return true;

59}

60

61#define z\_zassume(cond, default\_msg, file, line, func, msg, ...) z\_zassume\_(cond, file, line)

62

63static inline bool z\_zexpect\_(bool cond, const char \*file, int line)

64{

65 if (cond == false) {

66 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Expectation failed at %s:%d\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

67 line);

68 [ztest\_test\_expect\_fail](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)();

69 return false;

70 }

71

72 return true;

73}

74

75#define z\_zexpect(cond, default\_msg, file, line, func, msg, ...) z\_zexpect\_(cond, file, line)

76

77#else /\* CONFIG\_ZTEST\_ASSERT\_VERBOSE != 0 \*/

78

79static inline bool z\_zassert(bool cond, const char \*default\_msg, const char \*file, int line,

80 const char \*func, const char \*msg, ...)

81{

82 if (cond == false) {

83 va\_list vargs;

84

85 va\_start(vargs, msg);

86 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Assertion failed at %s:%d: %s: %s\n",

87 [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line, func, default\_msg);

88 [vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)(msg, vargs);

89 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("\n");

90 va\_end(vargs);

91 [ztest\_test\_fail](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)();

92 return false;

93 }

94#if CONFIG\_ZTEST\_ASSERT\_VERBOSE == 2

95 else {

96 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Assertion succeeded at %s:%d (%s)\n",

97 [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line, func);

98 }

99#endif

100 return true;

101}

102

103static inline bool z\_zassume(bool cond, const char \*default\_msg, const char \*file, int line,

104 const char \*func, const char \*msg, ...)

105{

106 if (cond == false) {

107 va\_list vargs;

108

109 va\_start(vargs, msg);

110 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Assumption failed at %s:%d: %s: %s\n",

111 [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line, func, default\_msg);

112 [vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)(msg, vargs);

113 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("\n");

114 va\_end(vargs);

115 [ztest\_skip\_failed\_assumption](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)();

116 return false;

117 }

118#if CONFIG\_ZTEST\_ASSERT\_VERBOSE == 2

119 else {

120 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Assumption succeeded at %s:%d (%s)\n",

121 [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line, func);

122 }

123#endif

124 return true;

125}

126

127static inline bool z\_zexpect(bool cond, const char \*default\_msg, const char \*file, int line,

128 const char \*func, const char \*msg, ...)

129{

130 if (cond == false) {

131 va\_list vargs;

132

133 va\_start(vargs, msg);

134 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Expectation failed at %s:%d: %s: %s\n",

135 [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line, func, default\_msg);

136 [vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)(msg, vargs);

137 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("\n");

138 va\_end(vargs);

139 [ztest\_test\_expect\_fail](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)();

140 return false;

141 }

142#if CONFIG\_ZTEST\_ASSERT\_VERBOSE == 2

143 else {

144 [PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)("\n Expectation succeeded at %s:%d (%s)\n",

145 [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line, func);

146 }

147#endif

148 return true;

149}

150

151#endif /\* CONFIG\_ZTEST\_ASSERT\_VERBOSE \*/

152

161

176#define \_zassert\_base(cond, default\_msg, msg, ...) \

177 do { \

178 bool \_msg = (msg != NULL); \

179 bool \_ret = \

180 z\_zassert(cond, \_msg ? ("(" default\_msg ")") : (default\_msg), \_\_FILE\_\_, \

181 \_\_LINE\_\_, \_\_func\_\_, \_msg ? msg : "", ##\_\_VA\_ARGS\_\_); \

182 (void)\_msg; \

183 if (!\_ret) { \

184 /\* If kernel but without multithreading return. \*/ \

185 COND\_CODE\_1(KERNEL, (COND\_CODE\_1(CONFIG\_MULTITHREADING, (), (return;))), \

186 ()) \

187 } \

188 } while (0)

189

190#define \_zassert\_va(cond, default\_msg, msg, ...) \

191 \_zassert\_base(cond, default\_msg, msg, ##\_\_VA\_ARGS\_\_)

192

[ 193](group__ztest__assert.md#ga0911ad9e94cdf1fe011d21316683ee7f)#define zassert(cond, default\_msg, ...) \

194 \_zassert\_va(cond, default\_msg, COND\_CODE\_1(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

195

214#define \_zassume\_base(cond, default\_msg, msg, ...) \

215 do { \

216 bool \_msg = (msg != NULL); \

217 bool \_ret = \

218 z\_zassume(cond, \_msg ? ("(" default\_msg ")") : (default\_msg), \_\_FILE\_\_, \

219 \_\_LINE\_\_, \_\_func\_\_, \_msg ? msg : "", ##\_\_VA\_ARGS\_\_); \

220 (void)\_msg; \

221 if (!\_ret) { \

222 /\* If kernel but without multithreading return. \*/ \

223 COND\_CODE\_1(KERNEL, (COND\_CODE\_1(CONFIG\_MULTITHREADING, (), (return;))), \

224 ()) \

225 } \

226 } while (0)

227

228#define \_zassume\_va(cond, default\_msg, msg, ...) \

229 \_zassume\_base(cond, default\_msg, msg, ##\_\_VA\_ARGS\_\_)

230

[ 231](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)#define zassume(cond, default\_msg, ...) \

232 \_zassume\_va(cond, default\_msg, COND\_CODE\_1(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

233

244#define \_zexpect\_base(cond, default\_msg, msg, ...) \

245 do { \

246 bool \_msg = (msg != NULL); \

247 bool \_ret = \

248 z\_zexpect(cond, \_msg ? ("(" default\_msg ")") : (default\_msg), \_\_FILE\_\_, \

249 \_\_LINE\_\_, \_\_func\_\_, \_msg ? msg : "", ##\_\_VA\_ARGS\_\_); \

250 (void)\_msg; \

251 if (!\_ret) { \

252 /\* If kernel but without multithreading return. \*/ \

253 COND\_CODE\_1(KERNEL, (COND\_CODE\_1(CONFIG\_MULTITHREADING, (), (return;))), \

254 ()) \

255 } \

256 } while (0)

257

258#define \_zexpect\_va(cond, default\_msg, msg, ...) \

259 \_zexpect\_base(cond, default\_msg, msg, ##\_\_VA\_ARGS\_\_)

260

[ 261](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)#define zexpect(cond, default\_msg, ...) \

262 \_zexpect\_va(cond, default\_msg, COND\_CODE\_1(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

263

[ 268](group__ztest__assert.md#ga300684a6b56e73e2cad6fd7458541129)#define zassert\_unreachable(...) zassert(0, "Reached unreachable code", ##\_\_VA\_ARGS\_\_)

269

[ 275](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)#define zassert\_true(cond, ...) zassert(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

276

[ 282](group__ztest__assert.md#ga7330d1794fb961e07ee40294019dead0)#define zassert\_false(cond, ...) zassert(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

283

[ 289](group__ztest__assert.md#gade40e2ec78ec813739e7725524fae7f0)#define zassert\_ok(cond, ...) zassert(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

290

[ 296](group__ztest__assert.md#gafe0e2609f77906ab0caddc31448a4fc8)#define zassert\_not\_ok(cond, ...) zassert(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

297

[ 303](group__ztest__assert.md#gac0839891fd8bb7313b98551465e04c19)#define zassert\_is\_null(ptr, ...) zassert((ptr) == NULL, #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

304

[ 310](group__ztest__assert.md#ga849adad4afe893a7ae3dc2fbe750dc00)#define zassert\_not\_null(ptr, ...) zassert((ptr) != NULL, #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

311

[ 321](group__ztest__assert.md#gacd075c7ee4dc2d64701bd3098a31b673)#define zassert\_equal(a, b, ...) zassert((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

322

[ 332](group__ztest__assert.md#ga43f306bf33d5e837b8927df16b82a363)#define zassert\_not\_equal(a, b, ...) zassert((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

333

[ 343](group__ztest__assert.md#gabf20273fcba9cc45939a9f7db77f0bfc)#define zassert\_equal\_ptr(a, b, ...) \

344 zassert((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

345

[ 354](group__ztest__assert.md#gacc930af1a66e8533c5eca9526e198b4b)#define zassert\_within(a, b, d, ...) \

355 zassert(((a) >= ((b) - (d))) && ((a) <= ((b) + (d))), #a " not within " #b " +/- " #d, \

356 ##\_\_VA\_ARGS\_\_)

357

[ 367](group__ztest__assert.md#ga2b6b41de3e4856b21458febab3261b91)#define zassert\_between\_inclusive(a, l, u, ...) \

368 zassert(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive", \

369 ##\_\_VA\_ARGS\_\_)

370

[ 382](group__ztest__assert.md#gabbfcf6345172387326d35b5d0e2bb051)#define zassert\_mem\_equal(...) zassert\_mem\_equal\_\_(\_\_VA\_ARGS\_\_)

383

[ 395](group__ztest__assert.md#ga30e5fefa185944d3e949d4023c2eea27)#define zassert\_mem\_equal\_\_(buf, exp, size, ...) \

396 zassert(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

397

[ 405](group__ztest__assert.md#ga382017945a8c409e885cad8d0909b197)#define zassert\_str\_equal(s1, s2, ...) \

406 zassert(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##\_\_VA\_ARGS\_\_)

407

411

420

[ 429](group__ztest__assume.md#ga6f5778ed8c1205126f7dcafb6eb26905)#define zassume\_true(cond, ...) zassume(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

430

[ 439](group__ztest__assume.md#ga5acf4256e5af3afaed06da7400dc3ad5)#define zassume\_false(cond, ...) zassume(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

440

[ 449](group__ztest__assume.md#ga9c6d1c701dd2d50027bf5e24b7567ae4)#define zassume\_ok(cond, ...) zassume(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

450

[ 459](group__ztest__assume.md#ga539831d2f42cc991a8295b388ec12846)#define zassume\_not\_ok(cond, ...) zassume(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

460

[ 469](group__ztest__assume.md#ga3c5b1814deb5974e8ba0af961b516fa0)#define zassume\_is\_null(ptr, ...) zassume((ptr) == NULL, #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

470

[ 479](group__ztest__assume.md#ga24f4144edf5cef493c88872c7d56900e)#define zassume\_not\_null(ptr, ...) zassume((ptr) != NULL, #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

480

[ 491](group__ztest__assume.md#ga88c2a3153568a6f621b88dd6ceeb48d6)#define zassume\_equal(a, b, ...) zassume((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

492

[ 503](group__ztest__assume.md#ga0d90bb874c3135ffee870a4b61607853)#define zassume\_not\_equal(a, b, ...) zassume((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

504

[ 515](group__ztest__assume.md#ga78d6fbbf5eb13b32a5164053811b6cca)#define zassume\_equal\_ptr(a, b, ...) \

516 zassume((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

517

[ 528](group__ztest__assume.md#gad808c91e07e6c27b2e28ec7e04e03854)#define zassume\_within(a, b, d, ...) \

529 zassume(((a) >= ((b) - (d))) && ((a) <= ((b) + (d))), #a " not within " #b " +/- " #d, \

530 ##\_\_VA\_ARGS\_\_)

531

[ 543](group__ztest__assume.md#gacff02eeba8dd334b3727dbe2036617e3)#define zassume\_between\_inclusive(a, l, u, ...) \

544 zassume(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive", \

545 ##\_\_VA\_ARGS\_\_)

546

[ 558](group__ztest__assume.md#ga62be45256399530167745e71226e4a37)#define zassume\_mem\_equal(...) zassume\_mem\_equal\_\_(\_\_VA\_ARGS\_\_)

559

[ 573](group__ztest__assume.md#gaaed6045f194ead4ffe1dd72a6fa5175d)#define zassume\_mem\_equal\_\_(buf, exp, size, ...) \

574 zassume(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

575

[ 583](group__ztest__assume.md#ga33a9cd37d321f1a421a1328e67b04788)#define zassume\_str\_equal(s1, s2, ...) \

584 zassume(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##\_\_VA\_ARGS\_\_)

585

589

598

[ 605](group__ztest__expect.md#gaef66b2764b6086dfbe8cbc933a8cfdc3)#define zexpect\_true(cond, ...) zexpect(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

606

[ 613](group__ztest__expect.md#ga619bd320e39799414383a228dc2d8299)#define zexpect\_false(cond, ...) zexpect(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

614

[ 622](group__ztest__expect.md#gaab325ee22058252c6a1c3243f3226657)#define zexpect\_ok(cond, ...) zexpect(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

623

[ 631](group__ztest__expect.md#gabde5406775f05d5fcd135eb926969004)#define zexpect\_not\_ok(cond, ...) zexpect(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

632

[ 639](group__ztest__expect.md#ga10b2c904f1c68b816eae2ad53e2b9f90)#define zexpect\_is\_null(ptr, ...) zexpect((ptr) == NULL, #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

640

[ 647](group__ztest__expect.md#gaa51053fe2a07c6417db7952d7a594798)#define zexpect\_not\_null(ptr, ...) zexpect((ptr) != NULL, #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

648

[ 656](group__ztest__expect.md#ga5ba65dbf95c204ed60694c5757db247f)#define zexpect\_equal(a, b, ...) zexpect((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

657

[ 668](group__ztest__expect.md#ga31d83ab89828a03aebe0d0dc003f5232)#define zexpect\_not\_equal(a, b, ...) zexpect((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

669

[ 679](group__ztest__expect.md#gabf791d13c5781fc2215289d6dd925b3e)#define zexpect\_equal\_ptr(a, b, ...) \

680 zexpect((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

681

[ 691](group__ztest__expect.md#ga907afb07269bbc444a3d8ffee46839b5)#define zexpect\_within(a, b, delta, ...) \

692 zexpect(((a) >= ((b) - (delta))) && ((a) <= ((b) + (delta))), \

693 #a " not within " #b " +/- " #delta, ##\_\_VA\_ARGS\_\_)

694

[ 704](group__ztest__expect.md#gac37ebea6a9c71e3666a4911ceea5c913)#define zexpect\_between\_inclusive(a, lower, upper, ...) \

705 zexpect(((a) >= (lower)) && ((a) <= (upper)), \

706 #a " not between " #lower " and " #upper " inclusive", ##\_\_VA\_ARGS\_\_)

707

[ 717](group__ztest__expect.md#gaee52264e5f92a606a2a85f5fbb0a85fb)#define zexpect\_mem\_equal(buf, exp, size, ...) \

718 zexpect(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

719

[ 728](group__ztest__expect.md#gacd5ef284610ca2027fc2e892243dfd38)#define zexpect\_str\_equal(s1, s2, ...) \

729 zexpect(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##\_\_VA\_ARGS\_\_)

730

734

735#ifdef \_\_cplusplus

736}

737#endif

738

739#endif /\* ZEPHYR\_TESTSUITE\_ZTEST\_ASSERT\_H\_ \*/

[vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)

static void vprintk(const char \*fmt, va\_list ap)

**Definition** printk.h:56

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

[stdbool.h](stdbool_8h.md)

[stdio.h](stdio_8h.md)

[string.h](string_8h.md)

[tc\_util.h](tc__util_8h.md)

[PRINT\_DATA](tc__util_8h.md#aec98e66470b575771ed484118095b692)

#define PRINT\_DATA(fmt,...)

**Definition** tc\_util.h:25

[ztest.h](ztest_8h.md)

Zephyr Testsuite.

[ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)

const char \* ztest\_relative\_filename(const char \*file)

[ztest\_skip\_failed\_assumption](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)

void ztest\_skip\_failed\_assumption(void)

[ztest\_test\_expect\_fail](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)

void ztest\_test\_expect\_fail(void)

[ztest\_test\_fail](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)

void ztest\_test\_fail(void)

[ztest\_test\_skip](ztest__assert_8h.md#ada3b1fcfa71db1bf7787c03ff45256d5)

void ztest\_test\_skip(void)

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest\_assert.h](ztest__assert_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
