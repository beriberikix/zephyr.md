---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tc__util_8h_source.html
original_path: doxygen/html/tc__util_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tc\_util.h

[Go to the documentation of this file.](tc__util_8h.md)

1/\* tc\_utilities.h - testcase utilities header file \*/

2

3/\*

4 \* Copyright (c) 2012-2015 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_TESTSUITE\_INCLUDE\_TC\_UTIL\_H\_

10#define ZEPHYR\_TESTSUITE\_INCLUDE\_TC\_UTIL\_H\_

11

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

14#include <[string.h](string_8h.md)>

15#ifdef CONFIG\_SHELL

16#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

17#endif

18#include <[zephyr/sys/printk.h](printk_8h.md)>

19

20#if defined CONFIG\_ZTEST\_TC\_UTIL\_USER\_OVERRIDE

21#include <tc\_util\_user\_override.h>

22#endif

23

24#ifndef PRINT\_DATA

[ 25](tc__util_8h.md#aec98e66470b575771ed484118095b692)#define PRINT\_DATA(fmt, ...) printk(fmt, ##\_\_VA\_ARGS\_\_)

26#endif

27

28#if defined CONFIG\_ARCH\_POSIX

29#include "posix\_board\_if.h"

30#endif

31

[ 47](tc__util_8h.md#a91250f31fc327df207018b9c66493677)#define TC\_STR\_HELPER(x) #x

[ 48](tc__util_8h.md#acd142b5f39b0d6fe5216440432ef2c72)#define TC\_STR(x) TC\_STR\_HELPER(x)

49#ifdef TC\_RUNID

50#define TC\_PRINT\_RUNID PRINT\_DATA("RunID: " TC\_STR(TC\_RUNID) "\n")

51#else

[ 52](tc__util_8h.md#a82cdb6d03f070075b576cbe1dab5e71a)#define TC\_PRINT\_RUNID do {} while (false)

53#endif

54

55#ifndef PRINT\_LINE

[ 56](tc__util_8h.md#af72c5654279b3d1e227e8dec30411944)#define PRINT\_LINE \

57 PRINT\_DATA( \

58 "============================================================" \

59 "=======\n")

60#endif

61

62/\* stack size and priority for test suite task \*/

[ 63](tc__util_8h.md#a5486258f1f34d3baeda92a74b63c27c3)#define TASK\_STACK\_SIZE (1024 \* 2)

64

[ 65](tc__util_8h.md#a8e446c4d4b1517a80c371ca370c56ac3)#define FMT\_ERROR "%s - %s@%d. "

66

[ 67](tc__util_8h.md#afb66a88e5d1e781aeb5aa9739a8fe868)#define TC\_PASS 0

[ 68](tc__util_8h.md#a196c300c18de32c79d757131b579a3a5)#define TC\_FAIL 1

[ 69](tc__util_8h.md#abafb6d8cf1e1a3bb2247d5384d1d5461)#define TC\_SKIP 2

[ 70](tc__util_8h.md#ac0108c70de44b3186c7ead1c1430b3d1)#define TC\_FLAKY 3

71

72#ifndef TC\_PASS\_STR

[ 73](tc__util_8h.md#a991995992ef5c23b7c6cf7138b394437)#define TC\_PASS\_STR "PASS"

74#endif

75#ifndef TC\_FAIL\_STR

[ 76](tc__util_8h.md#ac5103b154fa450c478c2bf3f520cb8ff)#define TC\_FAIL\_STR "FAIL"

77#endif

78#ifndef TC\_SKIP\_STR

[ 79](tc__util_8h.md#a586f060684ebfc5db4105a30370a41d0)#define TC\_SKIP\_STR "SKIP"

80#endif

81#ifndef TC\_FLAKY\_STR

[ 82](tc__util_8h.md#a584cf09eac3d2fa3758924cb843cdbf5)#define TC\_FLAKY\_STR "FLAKY"

83#endif

84

[ 85](tc__util_8h.md#a9e2302e8d62cfefe7df86e62489efe29)static inline const char \*[TC\_RESULT\_TO\_STR](tc__util_8h.md#a9e2302e8d62cfefe7df86e62489efe29)(int result)

86{

87 switch (result) {

88 case [TC\_PASS](tc__util_8h.md#afb66a88e5d1e781aeb5aa9739a8fe868):

89 return [TC\_PASS\_STR](tc__util_8h.md#a991995992ef5c23b7c6cf7138b394437);

90 case [TC\_FAIL](tc__util_8h.md#a196c300c18de32c79d757131b579a3a5):

91 return [TC\_FAIL\_STR](tc__util_8h.md#ac5103b154fa450c478c2bf3f520cb8ff);

92 case [TC\_SKIP](tc__util_8h.md#abafb6d8cf1e1a3bb2247d5384d1d5461):

93 return [TC\_SKIP\_STR](tc__util_8h.md#a586f060684ebfc5db4105a30370a41d0);

94 case [TC\_FLAKY](tc__util_8h.md#ac0108c70de44b3186c7ead1c1430b3d1):

95 return [TC\_FLAKY\_STR](tc__util_8h.md#a584cf09eac3d2fa3758924cb843cdbf5);

96 default:

97 return "?";

98 }

99}

100

[ 101](tc__util_8h.md#ad3aec479c61df7656ae28f68aa4dc4a5)static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tc\_start\_time](tc__util_8h.md#ad3aec479c61df7656ae28f68aa4dc4a5);

[ 102](tc__util_8h.md#a9bb8eafa6af5b875097421ba21a8dfc8)static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tc\_spend\_time](tc__util_8h.md#a9bb8eafa6af5b875097421ba21a8dfc8);

103

[ 104](tc__util_8h.md#a497dd92db8a77681994baee1ba3f0847)static inline void [get\_start\_time\_cyc](tc__util_8h.md#a497dd92db8a77681994baee1ba3f0847)(void)

105{

106 [tc\_start\_time](tc__util_8h.md#ad3aec479c61df7656ae28f68aa4dc4a5) = [k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)();

107}

108

[ 109](tc__util_8h.md#ab6f8f2a5ffd8240715e1eef0dfd27907)static inline void [get\_test\_duration\_ms](tc__util_8h.md#ab6f8f2a5ffd8240715e1eef0dfd27907)(void)

110{

111 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spend\_cycle = [k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)() - [tc\_start\_time](tc__util_8h.md#ad3aec479c61df7656ae28f68aa4dc4a5);

112

113 [tc\_spend\_time](tc__util_8h.md#a9bb8eafa6af5b875097421ba21a8dfc8) = [k\_cyc\_to\_ms\_ceil32](group__timeutil__unit__apis.md#ga40bf11b01ba76673c67569e8d1e55d92)(spend\_cycle);

114}

115

116#ifndef TC\_ERROR

[ 117](tc__util_8h.md#a6fcd0e6c5448a9198cdaed1e88e86e1b)#define TC\_ERROR(fmt, ...) \

118 do { \

119 PRINT\_DATA(FMT\_ERROR, "FAIL", \_\_func\_\_, \_\_LINE\_\_); \

120 PRINT\_DATA(fmt, ##\_\_VA\_ARGS\_\_); \

121 } while (false)

122#endif

123

[ 124](tc__util_8h.md#a30c304c5caa2145085e83fdbd5fa24e4)static inline void [print\_nothing](tc__util_8h.md#a30c304c5caa2145085e83fdbd5fa24e4)(const char \*fmt, ...)

125{

126 ARG\_UNUSED(fmt);

127}

128

129#ifndef TC\_PRINT

130#if defined(CONFIG\_ZTEST\_VERBOSE\_OUTPUT)

131#define TC\_PRINT(fmt, ...) PRINT\_DATA(fmt, ##\_\_VA\_ARGS\_\_)

132#else

[ 133](tc__util_8h.md#a31562104efbbaec65655dc0b661c0164)#define TC\_PRINT(fmt, ...) print\_nothing(fmt, ##\_\_VA\_ARGS\_\_)

134#endif /\* CONFIG\_ZTEST\_VERBOSE\_OUTPUT \*/

135#endif /\* TC\_PRINT \*/

136

137#ifndef TC\_SUMMARY\_PRINT

[ 138](tc__util_8h.md#a21b72e847828bb33f121df1f49d6049b)#define TC\_SUMMARY\_PRINT(fmt, ...) PRINT\_DATA(fmt, ##\_\_VA\_ARGS\_\_)

139#endif

140

141#ifndef TC\_START\_PRINT

142#if defined(CONFIG\_ZTEST\_VERBOSE\_OUTPUT)

143#define TC\_START\_PRINT(name) PRINT\_DATA("START - %s\n", name);

144#else

[ 145](tc__util_8h.md#a84a358e0dffa73ee8008c082863b0019)#define TC\_START\_PRINT(name) print\_nothing(name)

146#endif /\* CONFIG\_ZTEST\_VERBOSE\_OUTPUT \*/

147#endif /\* TC\_START\_PRINT \*/

148

149#ifndef TC\_START

[ 150](tc__util_8h.md#aa090341b412763239ae09ba1f7a52b3e)#define TC\_START(name) \

151 do { \

152 TC\_START\_PRINT(name); \

153 } while (0)

154#endif

155

156#ifndef TC\_END

[ 157](tc__util_8h.md#a8efc6e62889487dc919facca8ec42ecf)#define TC\_END(result, fmt, ...) PRINT\_DATA(fmt, ##\_\_VA\_ARGS\_\_)

158#endif

159

160#ifndef TC\_END\_PRINT

161#if defined(CONFIG\_ZTEST\_VERBOSE\_OUTPUT)

162#define TC\_END\_PRINT(result, fmt, ...) PRINT\_DATA(fmt, ##\_\_VA\_ARGS\_\_); PRINT\_LINE

163#else

[ 164](tc__util_8h.md#a257c3ffdd1721ca67ec44f6b9e8d9641)#define TC\_END\_PRINT(result, fmt, ...) print\_nothing(fmt)

165#endif /\* CONFIG\_ZTEST\_VERBOSE\_OUTPUT \*/

166#endif /\* TC\_END\_PRINT \*/

167

168/\* prints result and the function name \*/

169#ifndef Z\_TC\_END\_RESULT

170#define Z\_TC\_END\_RESULT(result, func) \

171 do { \

172 TC\_END\_PRINT(result, " %s - %s in %u.%03u seconds\n", \

173 TC\_RESULT\_TO\_STR(result), func, tc\_spend\_time/1000, \

174 tc\_spend\_time%1000); \

175 } while (0)

176#endif

177

178#ifndef TC\_END\_RESULT

[ 179](tc__util_8h.md#a51a8593a108ecdec4e29cbe2169d3a6b)#define TC\_END\_RESULT(result) \

180 Z\_TC\_END\_RESULT((result), \_\_func\_\_)

181#endif

182

183#ifndef TC\_END\_RESULT\_CUSTOM

[ 184](tc__util_8h.md#ada1b9d646eb10dd40f23667a19a57714)#define TC\_END\_RESULT\_CUSTOM(result, func) \

185 Z\_TC\_END\_RESULT((result), func)

186#endif

187

188#ifndef TC\_SUITE\_PRINT

[ 189](tc__util_8h.md#a342b3d937894dfa380580b96b73664a4)#define TC\_SUITE\_PRINT(fmt, ...) PRINT\_DATA(fmt, ##\_\_VA\_ARGS\_\_)

190#endif

191

192#ifndef TC\_SUITE\_START

[ 193](tc__util_8h.md#a175563de07188c1cc549cf88b0e78575)#define TC\_SUITE\_START(name) \

194 do { \

195 TC\_SUITE\_PRINT("Running TESTSUITE %s\n", name); \

196 PRINT\_LINE; \

197 } while (false)

198#endif

199

200#ifndef TC\_SUITE\_END

[ 201](tc__util_8h.md#af972f5db041628380c3f8a66c1513bdc)#define TC\_SUITE\_END(name, result) \

202 do { \

203 if (result != TC\_FAIL) { \

204 TC\_SUITE\_PRINT("TESTSUITE %s succeeded\n", name); \

205 } else { \

206 TC\_SUITE\_PRINT("TESTSUITE %s failed.\n", name); \

207 } \

208 } while (false)

209#endif

210

211#if defined(CONFIG\_ARCH\_POSIX)

212#include <[zephyr/logging/log\_ctrl.h](log__ctrl_8h.md)>

213#define TC\_END\_POST(result) do { \

214 LOG\_PANIC(); \

215 posix\_exit(result); \

216} while (0)

217#else

[ 218](tc__util_8h.md#a4aa57b8a67f3d67de8aec48a268a12ae)#define TC\_END\_POST(result)

219#endif /\* CONFIG\_ARCH\_POSIX \*/

220

221#ifndef TC\_END\_REPORT

[ 222](tc__util_8h.md#a3a7161b4346dd5e84a4a86d6ebdc0b9e)#define TC\_END\_REPORT(result) \

223 do { \

224 PRINT\_LINE; \

225 TC\_PRINT\_RUNID; \

226 TC\_END(result, \

227 "PROJECT EXECUTION %s\n", \

228 (result) == TC\_PASS ? "SUCCESSFUL" : "FAILED"); \

229 TC\_END\_POST(result); \

230 } while (false)

231#endif

232

233#if defined(CONFIG\_SHELL)

234#define TC\_CMD\_DEFINE(name) \

235 static int cmd\_##name(const struct shell \*sh, size\_t argc, \

236 char \*\*argv) \

237 { \

238 TC\_START(\_\_func\_\_); \

239 name(); \

240 TC\_END\_RESULT(TC\_PASS); \

241 return 0; \

242 }

243#define TC\_CMD\_ITEM(name) cmd\_##name

244#else

[ 245](tc__util_8h.md#aeae77e3905136ee851f1907cae75b9d9)#define TC\_CMD\_DEFINE(name) \

246 int cmd\_##name(int argc, char \*argv[]) \

247 { \

248 TC\_START(\_\_func\_\_); \

249 name(); \

250 TC\_END\_RESULT(TC\_PASS); \

251 return 0; \

252 }

[ 253](tc__util_8h.md#a44c72e8abf49266ead1bd1c97121e76b)#define TC\_CMD\_ITEM(name) {STRINGIFY(name), cmd\_##name, "none"}

254#endif

255

256#endif /\* ZEPHYR\_TESTSUITE\_INCLUDE\_TC\_UTIL\_H\_ \*/

[k\_cycle\_get\_32](group__clock__apis.md#ga208687de625e0036558343b4e66143d3)

static uint32\_t k\_cycle\_get\_32(void)

Read the hardware clock.

**Definition** kernel.h:1927

[k\_cyc\_to\_ms\_ceil32](group__timeutil__unit__apis.md#ga40bf11b01ba76673c67569e8d1e55d92)

#define k\_cyc\_to\_ms\_ceil32(t)

Convert hardware cycles to milliseconds.

**Definition** time\_units.h:1291

[kernel.h](kernel_8h.md)

Public kernel APIs.

[log\_ctrl.h](log__ctrl_8h.md)

[printk.h](printk_8h.md)

[shell.h](shell_2shell_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[string.h](string_8h.md)

[TC\_FAIL](tc__util_8h.md#a196c300c18de32c79d757131b579a3a5)

#define TC\_FAIL

**Definition** tc\_util.h:68

[print\_nothing](tc__util_8h.md#a30c304c5caa2145085e83fdbd5fa24e4)

static void print\_nothing(const char \*fmt,...)

**Definition** tc\_util.h:124

[get\_start\_time\_cyc](tc__util_8h.md#a497dd92db8a77681994baee1ba3f0847)

static void get\_start\_time\_cyc(void)

**Definition** tc\_util.h:104

[TC\_FLAKY\_STR](tc__util_8h.md#a584cf09eac3d2fa3758924cb843cdbf5)

#define TC\_FLAKY\_STR

**Definition** tc\_util.h:82

[TC\_SKIP\_STR](tc__util_8h.md#a586f060684ebfc5db4105a30370a41d0)

#define TC\_SKIP\_STR

**Definition** tc\_util.h:79

[TC\_PASS\_STR](tc__util_8h.md#a991995992ef5c23b7c6cf7138b394437)

#define TC\_PASS\_STR

**Definition** tc\_util.h:73

[tc\_spend\_time](tc__util_8h.md#a9bb8eafa6af5b875097421ba21a8dfc8)

static uint32\_t tc\_spend\_time

**Definition** tc\_util.h:102

[TC\_RESULT\_TO\_STR](tc__util_8h.md#a9e2302e8d62cfefe7df86e62489efe29)

static const char \* TC\_RESULT\_TO\_STR(int result)

**Definition** tc\_util.h:85

[get\_test\_duration\_ms](tc__util_8h.md#ab6f8f2a5ffd8240715e1eef0dfd27907)

static void get\_test\_duration\_ms(void)

**Definition** tc\_util.h:109

[TC\_SKIP](tc__util_8h.md#abafb6d8cf1e1a3bb2247d5384d1d5461)

#define TC\_SKIP

**Definition** tc\_util.h:69

[TC\_FLAKY](tc__util_8h.md#ac0108c70de44b3186c7ead1c1430b3d1)

#define TC\_FLAKY

**Definition** tc\_util.h:70

[TC\_FAIL\_STR](tc__util_8h.md#ac5103b154fa450c478c2bf3f520cb8ff)

#define TC\_FAIL\_STR

**Definition** tc\_util.h:76

[tc\_start\_time](tc__util_8h.md#ad3aec479c61df7656ae28f68aa4dc4a5)

static uint32\_t tc\_start\_time

**Definition** tc\_util.h:101

[TC\_PASS](tc__util_8h.md#afb66a88e5d1e781aeb5aa9739a8fe868)

#define TC\_PASS

**Definition** tc\_util.h:67

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [tc\_util.h](tc__util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
