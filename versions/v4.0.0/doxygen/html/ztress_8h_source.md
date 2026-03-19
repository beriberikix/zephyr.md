---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ztress_8h_source.html
original_path: doxygen/html/ztress_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztress.h

[Go to the documentation of this file.](ztress_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef TESTSUITE\_ZTEST\_INCLUDE\_ZTRESS\_H\_\_

14#define TESTSUITE\_ZTEST\_INCLUDE\_ZTRESS\_H\_\_

15

16#include <[zephyr/sys/util.h](sys_2util_8h.md)>

17#include <[zephyr/kernel.h](kernel_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 24](ztress_8h.md#a8752d529cfc4d77b1dd71c4572fd63c3)#define ZTRESS\_ID\_THREAD 0

[ 25](ztress_8h.md#a937803e1398db7d0e10ea60c9c9ef642)#define ZTRESS\_ID\_K\_TIMER 1

26

35

[ 55](group__ztest__ztress.md#gabab05b8db44a7024ce23cb34bf999e42)#define ZTRESS\_TIMER(handler, user\_data, exec\_cnt, init\_timeout) \

56 (ZTRESS\_ID\_K\_TIMER, handler, user\_data, exec\_cnt, 0, init\_timeout)

57

[ 80](group__ztest__ztress.md#gaed561641541e8ced6866f2f1227f21c0)#define ZTRESS\_THREAD(handler, user\_data, exec\_cnt, preempt\_cnt, init\_timeout) \

81 (ZTRESS\_ID\_THREAD, handler, user\_data, exec\_cnt, preempt\_cnt, init\_timeout)

82

[ 97](group__ztest__ztress.md#ga633439263754bf08baee06c37dddab40)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[ztress\_handler](group__ztest__ztress.md#ga633439263754bf08baee06c37dddab40))(void \*user\_data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt, bool last, int prio);

98

[ 100](structztress__context__data.md)struct [ztress\_context\_data](structztress__context__data.md) {

101 /\* Handler. \*/

[ 102](structztress__context__data.md#abc27db12d2734fa35bee654b30497108) [ztress\_handler](group__ztest__ztress.md#ga633439263754bf08baee06c37dddab40) [handler](structztress__context__data.md#abc27db12d2734fa35bee654b30497108);

103

104 /\* User data \*/

[ 105](structztress__context__data.md#a871f79e1717137500d9ee4c1a2ad07ef) void \*[user\_data](structztress__context__data.md#a871f79e1717137500d9ee4c1a2ad07ef);

106

107 /\* Minimum number of executions to complete the test. \*/

[ 108](structztress__context__data.md#ae96b7b02d0c315bb126193a4f0ad2bdf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [exec\_cnt](structztress__context__data.md#ae96b7b02d0c315bb126193a4f0ad2bdf);

109

110 /\* Minimum number of preemptions to complete the test. Valid only for

111 \* thread context.

112 \*/

[ 113](structztress__context__data.md#a17b5f520522cd6fc7024f097f18261ba) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [preempt\_cnt](structztress__context__data.md#a17b5f520522cd6fc7024f097f18261ba);

114

115 /\* Initial timeout. \*/

[ 116](structztress__context__data.md#a1208baa35d4adc19126d85f45ed78c63) [k\_timeout\_t](structk__timeout__t.md) [t](structztress__context__data.md#a1208baa35d4adc19126d85f45ed78c63);

117};

118

[ 130](group__ztest__ztress.md#gab5e8bbcecd77db06e7a90631fc0c202b)#define ZTRESS\_CONTEXT\_INITIALIZER(\_handler, \_user\_data, \_exec\_cnt, \_preempt\_cnt, \_t) \

131 { \

132 .handler = (\_handler), \

133 .user\_data = (\_user\_data), \

134 .exec\_cnt = (\_exec\_cnt), \

135 .preempt\_cnt = (\_preempt\_cnt), \

136 .t = (\_t) \

137 }

138

140#define Z\_ZTRESS\_GET\_HANDLER\_DATA2(\_, ...) \

141 ZTRESS\_CONTEXT\_INITIALIZER(\_\_VA\_ARGS\_\_)

142

144#define Z\_ZTRESS\_GET\_HANDLER\_DATA(data) \

145 Z\_ZTRESS\_GET\_HANDLER\_DATA2 data

146

148#define Z\_ZTRESS\_HAS\_TIMER(data, ...) \

149 GET\_ARG\_N(1, \_\_DEBRACKET data)

150

154#define Z\_ZTRESS\_TIMER\_IDX(idx, data) \

155 ((GET\_ARG\_N(1, \_\_DEBRACKET data)) == ZTRESS\_ID\_K\_TIMER ? idx : 0)

156

160#define Z\_ZTRESS\_TIMER\_CONTEXT\_VALIDATE(...) \

161 BUILD\_ASSERT((FOR\_EACH\_IDX(Z\_ZTRESS\_TIMER\_IDX, (+), \_\_VA\_ARGS\_\_)) == 0, \

162 "There can only be up to one ZTRESS\_TIMER context and it must " \

163 "be the first in the list")

164

[ 176](group__ztest__ztress.md#ga6acc3a50e0eff7360873006482f5c8e9)#define ZTRESS\_EXECUTE(...) do { \

177 Z\_ZTRESS\_TIMER\_CONTEXT\_VALIDATE(\_\_VA\_ARGS\_\_); \

178 int has\_timer = Z\_ZTRESS\_HAS\_TIMER(\_\_VA\_ARGS\_\_); \

179 struct ztress\_context\_data \_ctx\_data1[] = { \

180 FOR\_EACH(Z\_ZTRESS\_GET\_HANDLER\_DATA, (,), \_\_VA\_ARGS\_\_) \

181 }; \

182 size\_t cnt = ARRAY\_SIZE(\_ctx\_data1) - has\_timer; \

183 static struct ztress\_context\_data \_ctx\_data[ARRAY\_SIZE(\_ctx\_data1)]; \

184 for (size\_t i = 0; i < ARRAY\_SIZE(\_ctx\_data1); i++) { \

185 \_ctx\_data[i] = \_ctx\_data1[i]; \

186 } \

187 int exec\_err = ztress\_execute(has\_timer ? &\_ctx\_data[0] : NULL, \

188 &\_ctx\_data[has\_timer], cnt); \

189 \

190 zassert\_equal(exec\_err, 0, "ztress\_execute failed (err: %d)", exec\_err); \

191} while (0)

192

[ 208](group__ztest__ztress.md#gaf706f1af4c42f5925d7545dadf5548fd)int [ztress\_execute](group__ztest__ztress.md#gaf706f1af4c42f5925d7545dadf5548fd)(struct [ztress\_context\_data](structztress__context__data.md) \*timer\_data,

209 struct [ztress\_context\_data](structztress__context__data.md) \*thread\_data,

210 size\_t cnt);

211

[ 213](group__ztest__ztress.md#ga57f171e230fba462b3dea6b2d3cf71f6)void [ztress\_abort](group__ztest__ztress.md#ga57f171e230fba462b3dea6b2d3cf71f6)(void);

214

[ 222](group__ztest__ztress.md#ga5b3069bb2aa35ddc64c46c18d2e30091)void [ztress\_set\_timeout](group__ztest__ztress.md#ga5b3069bb2aa35ddc64c46c18d2e30091)([k\_timeout\_t](structk__timeout__t.md) t);

223

[ 229](group__ztest__ztress.md#gaf4db2092eee17d863c9810333ba4c870)void [ztress\_report](group__ztest__ztress.md#gaf4db2092eee17d863c9810333ba4c870)(void);

230

[ 237](group__ztest__ztress.md#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b)int [ztress\_exec\_count](group__ztest__ztress.md#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

238

[ 245](group__ztest__ztress.md#ga4406b828d170bc19065aaf65aeb4613e)int [ztress\_preempt\_count](group__ztest__ztress.md#ga4406b828d170bc19065aaf65aeb4613e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

246

[ 256](group__ztest__ztress.md#gacbbdb8e7bad532d6dd20c486b3256e21)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ztress\_optimized\_ticks](group__ztest__ztress.md#gacbbdb8e7bad532d6dd20c486b3256e21)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id);

257

261

262#ifdef \_\_cplusplus

263}

264#endif

265

266#endif /\* TESTSUITE\_ZTEST\_INCLUDE\_ZTRESS\_H\_\_ \*/

[ztress\_preempt\_count](group__ztest__ztress.md#ga4406b828d170bc19065aaf65aeb4613e)

int ztress\_preempt\_count(uint32\_t id)

Get number of preemptions of a given context in the last test.

[ztress\_abort](group__ztest__ztress.md#ga57f171e230fba462b3dea6b2d3cf71f6)

void ztress\_abort(void)

Abort ongoing stress test.

[ztress\_set\_timeout](group__ztest__ztress.md#ga5b3069bb2aa35ddc64c46c18d2e30091)

void ztress\_set\_timeout(k\_timeout\_t t)

Set test timeout.

[ztress\_handler](group__ztest__ztress.md#ga633439263754bf08baee06c37dddab40)

bool(\* ztress\_handler)(void \*user\_data, uint32\_t cnt, bool last, int prio)

User handler called in one of the configured contexts.

**Definition** ztress.h:97

[ztress\_exec\_count](group__ztest__ztress.md#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b)

int ztress\_exec\_count(uint32\_t id)

Get number of executions of a given context in the last test.

[ztress\_optimized\_ticks](group__ztest__ztress.md#gacbbdb8e7bad532d6dd20c486b3256e21)

uint32\_t ztress\_optimized\_ticks(uint32\_t id)

Get optimized timeout base of a given context in the last test.

[ztress\_report](group__ztest__ztress.md#gaf4db2092eee17d863c9810333ba4c870)

void ztress\_report(void)

Print last test report.

[ztress\_execute](group__ztest__ztress.md#gaf706f1af4c42f5925d7545dadf5548fd)

int ztress\_execute(struct ztress\_context\_data \*timer\_data, struct ztress\_context\_data \*thread\_data, size\_t cnt)

Execute contexts.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[ztress\_context\_data](structztress__context__data.md)

**Definition** ztress.h:100

[ztress\_context\_data::t](structztress__context__data.md#a1208baa35d4adc19126d85f45ed78c63)

k\_timeout\_t t

**Definition** ztress.h:116

[ztress\_context\_data::preempt\_cnt](structztress__context__data.md#a17b5f520522cd6fc7024f097f18261ba)

uint32\_t preempt\_cnt

**Definition** ztress.h:113

[ztress\_context\_data::user\_data](structztress__context__data.md#a871f79e1717137500d9ee4c1a2ad07ef)

void \* user\_data

**Definition** ztress.h:105

[ztress\_context\_data::handler](structztress__context__data.md#abc27db12d2734fa35bee654b30497108)

ztress\_handler handler

**Definition** ztress.h:102

[ztress\_context\_data::exec\_cnt](structztress__context__data.md#ae96b7b02d0c315bb126193a4f0ad2bdf)

uint32\_t exec\_cnt

**Definition** ztress.h:108

[util.h](sys_2util_8h.md)

Misc utilities.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztress.h](ztress_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
