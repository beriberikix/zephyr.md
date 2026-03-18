---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ztest__assert_8h_source.html
original_path: doxygen/html/ztest__assert_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

21#include <[zephyr/ztest.h](ztest_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 27](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)const char \*[ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(const char \*file);

[ 28](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)void [ztest\_test\_fail](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)(void);

[ 29](ztest__assert_8h.md#ada3b1fcfa71db1bf7787c03ff45256d5)void [ztest\_test\_skip](ztest__assert_8h.md#ada3b1fcfa71db1bf7787c03ff45256d5)(void);

[ 30](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)void [ztest\_test\_expect\_fail](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)(void);

[ 31](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)void [ztest\_skip\_failed\_assumption](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)(void);

32#if CONFIG\_ZTEST\_ASSERT\_VERBOSE == 0

33

34static inline bool z\_zassert\_(bool cond, const char \*file, int line)

35{

36 if (cond == false) {

37 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Assertion failed at %s:%d\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line);

38 [ztest\_test\_fail](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)();

39 return false;

40 }

41

42 return true;

43}

44

45#define z\_zassert(cond, default\_msg, file, line, func, msg, ...) z\_zassert\_(cond, file, line)

46

47static inline bool z\_zassume\_(bool cond, const char \*file, int line)

48{

49 if (cond == false) {

50 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Assumption failed at %s:%d\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line);

51 [ztest\_skip\_failed\_assumption](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)();

52 return false;

53 }

54

55 return true;

56}

57

58#define z\_zassume(cond, default\_msg, file, line, func, msg, ...) z\_zassume\_(cond, file, line)

59

60static inline bool z\_zexpect\_(bool cond, const char \*file, int line)

61{

62 if (cond == false) {

63 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Expectation failed at %s:%d\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file), line);

64 [ztest\_test\_expect\_fail](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)();

65 return false;

66 }

67

68 return true;

69}

70

71#define z\_zexpect(cond, default\_msg, file, line, func, msg, ...) z\_zexpect\_(cond, file, line)

72

73#else /\* CONFIG\_ZTEST\_ASSERT\_VERBOSE != 0 \*/

74

75static inline bool z\_zassert(bool cond, const char \*default\_msg, const char \*file, int line,

76 const char \*func, const char \*msg, ...)

77{

78 if (cond == false) {

79 va\_list vargs;

80

81 va\_start(vargs, msg);

82 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Assertion failed at %s:%d: %s: %s\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

83 line, func, default\_msg);

84 [vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)(msg, vargs);

85 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("\n");

86 va\_end(vargs);

87 [ztest\_test\_fail](ztest__assert_8h.md#acd6eb423f54dce8544f7c3b1618c0374)();

88 return false;

89 }

90#if CONFIG\_ZTEST\_ASSERT\_VERBOSE == 2

91 else {

92 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Assertion succeeded at %s:%d (%s)\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

93 line, func);

94 }

95#endif

96 return true;

97}

98

99static inline bool z\_zassume(bool cond, const char \*default\_msg, const char \*file, int line,

100 const char \*func, const char \*msg, ...)

101{

102 if (cond == false) {

103 va\_list vargs;

104

105 va\_start(vargs, msg);

106 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Assumption failed at %s:%d: %s: %s\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

107 line, func, default\_msg);

108 [vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)(msg, vargs);

109 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("\n");

110 va\_end(vargs);

111 [ztest\_skip\_failed\_assumption](ztest__assert_8h.md#a17537c79021fbc12e56b72ccec4b99c5)();

112 return false;

113 }

114#if CONFIG\_ZTEST\_ASSERT\_VERBOSE == 2

115 else {

116 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Assumption succeeded at %s:%d (%s)\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

117 line, func);

118 }

119#endif

120 return true;

121}

122

123static inline bool z\_zexpect(bool cond, const char \*default\_msg, const char \*file, int line,

124 const char \*func, const char \*msg, ...)

125{

126 if (cond == false) {

127 va\_list vargs;

128

129 va\_start(vargs, msg);

130 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Expectation failed at %s:%d: %s: %s\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

131 line, func, default\_msg);

132 [vprintk](printk_8h.md#a23609ef1acea586b44f71d32283fea23)(msg, vargs);

133 [printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("\n");

134 va\_end(vargs);

135 [ztest\_test\_expect\_fail](ztest__assert_8h.md#a5c6bb493c88f7426a827889526dc0772)();

136 return false;

137 }

138#if CONFIG\_ZTEST\_ASSERT\_VERBOSE == 2

139 else {

140 [PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)("\n Expectation succeeded at %s:%d (%s)\n", [ztest\_relative\_filename](ztest__assert_8h.md#a06a081e3d716be7e024973cbf305c14b)(file),

141 line, func);

142 }

143#endif

144 return true;

145}

146

147#endif /\* CONFIG\_ZTEST\_ASSERT\_VERBOSE \*/

148

157

172#define \_zassert\_base(cond, default\_msg, msg, ...) \

173 do { \

174 bool \_msg = (msg != NULL); \

175 bool \_ret = z\_zassert(cond, \_msg ? ("(" default\_msg ")") : (default\_msg), \_\_FILE\_\_,\

176 \_\_LINE\_\_, \_\_func\_\_, \_msg ? msg : "", ##\_\_VA\_ARGS\_\_); \

177 (void)\_msg; \

178 if (!\_ret) { \

179 /\* If kernel but without multithreading return. \*/ \

180 COND\_CODE\_1(KERNEL, (COND\_CODE\_1(CONFIG\_MULTITHREADING, (), (return;))), \

181 ()) \

182 } \

183 } while (0)

184

185#define \_zassert\_va(cond, default\_msg, msg, ...) \

186 \_zassert\_base(cond, default\_msg, msg, ##\_\_VA\_ARGS\_\_)

187

[ 188](group__ztest__assert.md#ga0911ad9e94cdf1fe011d21316683ee7f)#define zassert(cond, default\_msg, ...) \

189 \_zassert\_va(cond, default\_msg, COND\_CODE\_1(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

190

209#define \_zassume\_base(cond, default\_msg, msg, ...) \

210 do { \

211 bool \_msg = (msg != NULL); \

212 bool \_ret = z\_zassume(cond, \_msg ? ("(" default\_msg ")") : (default\_msg), \_\_FILE\_\_,\

213 \_\_LINE\_\_, \_\_func\_\_, \_msg ? msg : "", ##\_\_VA\_ARGS\_\_); \

214 (void)\_msg; \

215 if (!\_ret) { \

216 /\* If kernel but without multithreading return. \*/ \

217 COND\_CODE\_1(KERNEL, (COND\_CODE\_1(CONFIG\_MULTITHREADING, (), (return;))), \

218 ()) \

219 } \

220 } while (0)

221

222#define \_zassume\_va(cond, default\_msg, msg, ...) \

223 \_zassume\_base(cond, default\_msg, msg, ##\_\_VA\_ARGS\_\_)

224

[ 225](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)#define zassume(cond, default\_msg, ...) \

226 \_zassume\_va(cond, default\_msg, COND\_CODE\_1(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

227

238#define \_zexpect\_base(cond, default\_msg, msg, ...) \

239 do { \

240 bool \_msg = (msg != NULL); \

241 bool \_ret = \

242 z\_zexpect(cond, \_msg ? ("(" default\_msg ")") : (default\_msg), \_\_FILE\_\_, \

243 \_\_LINE\_\_, \_\_func\_\_, \_msg ? msg : "", ##\_\_VA\_ARGS\_\_); \

244 (void)\_msg; \

245 if (!\_ret) { \

246 /\* If kernel but without multithreading return. \*/ \

247 COND\_CODE\_1(KERNEL, (COND\_CODE\_1(CONFIG\_MULTITHREADING, (), (return;))), \

248 ()) \

249 } \

250 } while (0)

251

252#define \_zexpect\_va(cond, default\_msg, msg, ...) \

253 \_zexpect\_base(cond, default\_msg, msg, ##\_\_VA\_ARGS\_\_)

254

[ 255](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)#define zexpect(cond, default\_msg, ...) \

256 \_zexpect\_va(cond, default\_msg, COND\_CODE\_1(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

257

[ 262](group__ztest__assert.md#ga300684a6b56e73e2cad6fd7458541129)#define zassert\_unreachable(...) zassert(0, "Reached unreachable code", ##\_\_VA\_ARGS\_\_)

263

[ 269](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)#define zassert\_true(cond, ...) zassert(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

270

[ 276](group__ztest__assert.md#ga7330d1794fb961e07ee40294019dead0)#define zassert\_false(cond, ...) zassert(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

277

[ 283](group__ztest__assert.md#gade40e2ec78ec813739e7725524fae7f0)#define zassert\_ok(cond, ...) zassert(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

284

[ 290](group__ztest__assert.md#gafe0e2609f77906ab0caddc31448a4fc8)#define zassert\_not\_ok(cond, ...) zassert(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

291

[ 297](group__ztest__assert.md#gac0839891fd8bb7313b98551465e04c19)#define zassert\_is\_null(ptr, ...) zassert((ptr) == NULL, #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

298

[ 304](group__ztest__assert.md#ga849adad4afe893a7ae3dc2fbe750dc00)#define zassert\_not\_null(ptr, ...) zassert((ptr) != NULL, #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

305

[ 315](group__ztest__assert.md#gacd075c7ee4dc2d64701bd3098a31b673)#define zassert\_equal(a, b, ...) zassert((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

316

[ 326](group__ztest__assert.md#ga43f306bf33d5e837b8927df16b82a363)#define zassert\_not\_equal(a, b, ...) zassert((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

327

[ 337](group__ztest__assert.md#gabf20273fcba9cc45939a9f7db77f0bfc)#define zassert\_equal\_ptr(a, b, ...) \

338 zassert((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

339

[ 348](group__ztest__assert.md#gacc930af1a66e8533c5eca9526e198b4b)#define zassert\_within(a, b, d, ...) \

349 zassert(((a) >= ((b) - (d))) && ((a) <= ((b) + (d))), #a " not within " #b " +/- " #d, \

350 ##\_\_VA\_ARGS\_\_)

351

[ 361](group__ztest__assert.md#ga2b6b41de3e4856b21458febab3261b91)#define zassert\_between\_inclusive(a, l, u, ...) \

362 zassert(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive", \

363 ##\_\_VA\_ARGS\_\_)

364

[ 376](group__ztest__assert.md#gabbfcf6345172387326d35b5d0e2bb051)#define zassert\_mem\_equal(...) zassert\_mem\_equal\_\_(\_\_VA\_ARGS\_\_)

377

[ 389](group__ztest__assert.md#ga30e5fefa185944d3e949d4023c2eea27)#define zassert\_mem\_equal\_\_(buf, exp, size, ...) \

390 zassert(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

391

395

404

[ 413](group__ztest__assume.md#ga6f5778ed8c1205126f7dcafb6eb26905)#define zassume\_true(cond, ...) zassume(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

414

[ 423](group__ztest__assume.md#ga5acf4256e5af3afaed06da7400dc3ad5)#define zassume\_false(cond, ...) zassume(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

424

[ 433](group__ztest__assume.md#ga9c6d1c701dd2d50027bf5e24b7567ae4)#define zassume\_ok(cond, ...) zassume(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

434

[ 443](group__ztest__assume.md#ga539831d2f42cc991a8295b388ec12846)#define zassume\_not\_ok(cond, ...) zassume(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

444

[ 453](group__ztest__assume.md#ga3c5b1814deb5974e8ba0af961b516fa0)#define zassume\_is\_null(ptr, ...) zassume((ptr) == NULL, #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

454

[ 463](group__ztest__assume.md#ga24f4144edf5cef493c88872c7d56900e)#define zassume\_not\_null(ptr, ...) zassume((ptr) != NULL, #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

464

[ 475](group__ztest__assume.md#ga88c2a3153568a6f621b88dd6ceeb48d6)#define zassume\_equal(a, b, ...) zassume((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

476

[ 487](group__ztest__assume.md#ga0d90bb874c3135ffee870a4b61607853)#define zassume\_not\_equal(a, b, ...) zassume((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

488

[ 499](group__ztest__assume.md#ga78d6fbbf5eb13b32a5164053811b6cca)#define zassume\_equal\_ptr(a, b, ...) \

500 zassume((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

501

[ 512](group__ztest__assume.md#gad808c91e07e6c27b2e28ec7e04e03854)#define zassume\_within(a, b, d, ...) \

513 zassume(((a) >= ((b) - (d))) && ((a) <= ((b) + (d))), #a " not within " #b " +/- " #d, \

514 ##\_\_VA\_ARGS\_\_)

515

[ 527](group__ztest__assume.md#gacff02eeba8dd334b3727dbe2036617e3)#define zassume\_between\_inclusive(a, l, u, ...) \

528 zassume(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive", \

529 ##\_\_VA\_ARGS\_\_)

530

[ 542](group__ztest__assume.md#ga62be45256399530167745e71226e4a37)#define zassume\_mem\_equal(...) zassume\_mem\_equal\_\_(\_\_VA\_ARGS\_\_)

543

[ 557](group__ztest__assume.md#gaaed6045f194ead4ffe1dd72a6fa5175d)#define zassume\_mem\_equal\_\_(buf, exp, size, ...) \

558 zassume(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

559

563

572

[ 579](group__ztest__expect.md#gaef66b2764b6086dfbe8cbc933a8cfdc3)#define zexpect\_true(cond, ...) zexpect(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

580

[ 587](group__ztest__expect.md#ga619bd320e39799414383a228dc2d8299)#define zexpect\_false(cond, ...) zexpect(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

588

[ 596](group__ztest__expect.md#gaab325ee22058252c6a1c3243f3226657)#define zexpect\_ok(cond, ...) zexpect(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

597

[ 605](group__ztest__expect.md#gabde5406775f05d5fcd135eb926969004)#define zexpect\_not\_ok(cond, ...) zexpect(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

606

[ 613](group__ztest__expect.md#ga10b2c904f1c68b816eae2ad53e2b9f90)#define zexpect\_is\_null(ptr, ...) zexpect((ptr) == NULL, #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

614

[ 621](group__ztest__expect.md#gaa51053fe2a07c6417db7952d7a594798)#define zexpect\_not\_null(ptr, ...) zexpect((ptr) != NULL, #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

622

[ 631](group__ztest__expect.md#ga5ba65dbf95c204ed60694c5757db247f)#define zexpect\_equal(a, b, ...) zexpect((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

632

[ 643](group__ztest__expect.md#ga31d83ab89828a03aebe0d0dc003f5232)#define zexpect\_not\_equal(a, b, ...) zexpect((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

644

[ 654](group__ztest__expect.md#gabf791d13c5781fc2215289d6dd925b3e)#define zexpect\_equal\_ptr(a, b, ...) \

655 zexpect((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

656

[ 666](group__ztest__expect.md#ga907afb07269bbc444a3d8ffee46839b5)#define zexpect\_within(a, b, delta, ...) \

667 zexpect(((a) >= ((b) - (delta))) && ((a) <= ((b) + (delta))), \

668 #a " not within " #b " +/- " #delta, ##\_\_VA\_ARGS\_\_)

669

[ 679](group__ztest__expect.md#gac37ebea6a9c71e3666a4911ceea5c913)#define zexpect\_between\_inclusive(a, lower, upper, ...) \

680 zexpect(((a) >= (lower)) && ((a) <= (upper)), \

681 #a " not between " #lower " and " #upper " inclusive", ##\_\_VA\_ARGS\_\_)

682

[ 692](group__ztest__expect.md#gaee52264e5f92a606a2a85f5fbb0a85fb)#define zexpect\_mem\_equal(buf, exp, size, ...) \

693 zexpect(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

694

698

699#ifdef \_\_cplusplus

700}

701#endif

702

703#endif /\* ZEPHYR\_TESTSUITE\_ZTEST\_ASSERT\_H\_ \*/

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

[ztest.h](ztest_8h.md)

Zephyr Testsuite.

[PRINT](ztest_8h.md#a8b43bafee90b30676faae508c21cb8d7)

#define PRINT

**Definition** ztest.h:39

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
