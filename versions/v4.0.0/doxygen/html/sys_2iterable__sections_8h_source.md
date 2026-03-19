---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sys_2iterable__sections_8h_source.html
original_path: doxygen/html/sys_2iterable__sections_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iterable\_sections.h

[Go to the documentation of this file.](sys_2iterable__sections_8h.md)

1/\*

2 \* Copyright (C) 2020, Intel Corporation

3 \* Copyright (C) 2023, Nordic Semiconductor ASA

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef INCLUDE\_ZEPHYR\_SYS\_ITERABLE\_SECTIONS\_H\_

8#define INCLUDE\_ZEPHYR\_SYS\_ITERABLE\_SECTIONS\_H\_

9

10#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

11#include <[zephyr/toolchain.h](toolchain_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 42](group__iterable__section__apis.md#gac5177fefd615bdd3025fac742d414808)#define TYPE\_SECTION\_ITERABLE(type, varname, secname, section\_postfix) \

43 Z\_DECL\_ALIGN(type) varname \

44 \_\_in\_section(\_##secname, static, \_CONCAT(section\_postfix, \_)) \_\_used \_\_noasan

45

[ 55](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)#define TYPE\_SECTION\_START(secname) \_CONCAT(\_##secname, \_list\_start)

56

[ 65](group__iterable__section__apis.md#ga14d6bc375423775e5484183eeadd1fad)#define TYPE\_SECTION\_END(secname) \_CONCAT(\_##secname, \_list\_end)

66

[ 78](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)#define TYPE\_SECTION\_START\_EXTERN(type, secname) \

79 extern type TYPE\_SECTION\_START(secname)[]

80

[ 92](group__iterable__section__apis.md#gaf009fe4b90f7b338c3bf85bb4cd682e5)#define TYPE\_SECTION\_END\_EXTERN(type, secname) \

93 extern type TYPE\_SECTION\_END(secname)[]

94

[ 105](group__iterable__section__apis.md#gac74c8d3f92304a7082d5c5c7c62dace7)#define TYPE\_SECTION\_FOREACH(type, secname, iterator) \

106 TYPE\_SECTION\_START\_EXTERN(type, secname); \

107 TYPE\_SECTION\_END\_EXTERN(type, secname); \

108 for (type \* iterator = TYPE\_SECTION\_START(secname); ({ \

109 \_\_ASSERT(iterator <= TYPE\_SECTION\_END(secname),\

110 "unexpected list end location"); \

111 iterator < TYPE\_SECTION\_END(secname); \

112 }); \

113 iterator++)

114

[ 125](group__iterable__section__apis.md#gae0f61156fa152ff5604087e2849caeb0)#define TYPE\_SECTION\_GET(type, secname, i, dst) do { \

126 TYPE\_SECTION\_START\_EXTERN(type, secname); \

127 \*(dst) = &TYPE\_SECTION\_START(secname)[i]; \

128} while (0)

129

[ 137](group__iterable__section__apis.md#ga0c3da72ee4432a94242aaccf5cd5e9fb)#define TYPE\_SECTION\_COUNT(type, secname, dst) do { \

138 TYPE\_SECTION\_START\_EXTERN(type, secname); \

139 TYPE\_SECTION\_END\_EXTERN(type, secname); \

140 \*(dst) = ((uintptr\_t)TYPE\_SECTION\_END(secname) - \

141 (uintptr\_t)TYPE\_SECTION\_START(secname)) / sizeof(type); \

142} while (0)

143

[ 149](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)#define STRUCT\_SECTION\_START(struct\_type) \

150 TYPE\_SECTION\_START(struct\_type)

151

[ 159](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)#define STRUCT\_SECTION\_START\_EXTERN(struct\_type) \

160 TYPE\_SECTION\_START\_EXTERN(struct struct\_type, struct\_type)

161

[ 167](group__iterable__section__apis.md#ga3170a115129c683811181615661bc298)#define STRUCT\_SECTION\_END(struct\_type) \

168 TYPE\_SECTION\_END(struct\_type)

169

[ 177](group__iterable__section__apis.md#ga190b01770f323bfc7acfd50312b83a91)#define STRUCT\_SECTION\_END\_EXTERN(struct\_type) \

178 TYPE\_SECTION\_END\_EXTERN(struct struct\_type, struct\_type)

179

[ 188](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)#define STRUCT\_SECTION\_ITERABLE\_ALTERNATE(secname, struct\_type, varname) \

189 TYPE\_SECTION\_ITERABLE(struct struct\_type, varname, secname, varname)

190

[ 197](group__iterable__section__apis.md#ga2013cfe23c77c472f6fc43ccc99ac228)#define STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE(secname, struct\_type, varname, \

198 size) \

199 TYPE\_SECTION\_ITERABLE(struct struct\_type, varname[size], secname, \

200 varname)

201

[ 216](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname) \

217 STRUCT\_SECTION\_ITERABLE\_ALTERNATE(struct\_type, struct\_type, varname)

218

[ 224](group__iterable__section__apis.md#ga1d9ed5b5006579e7c452a6f15418849b)#define STRUCT\_SECTION\_ITERABLE\_ARRAY(struct\_type, varname, size) \

225 STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE(struct\_type, struct\_type, \

226 varname, size)

227

[ 234](group__iterable__section__apis.md#gada3ff915b4ed4881a61b79d8877131e2)#define STRUCT\_SECTION\_ITERABLE\_NAMED(struct\_type, name, varname) \

235 TYPE\_SECTION\_ITERABLE(struct struct\_type, varname, struct\_type, name)

236

[ 244](group__iterable__section__apis.md#ga5c2441634885ac7c5c15e5cfe159b2fd)#define STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE(struct\_type, secname, name, varname) \

245 TYPE\_SECTION\_ITERABLE(struct struct\_type, varname, secname, name)

246

[ 257](group__iterable__section__apis.md#ga06fb73cfb2dd5036a6e0f7098105ccd4)#define STRUCT\_SECTION\_FOREACH\_ALTERNATE(secname, struct\_type, iterator) \

258 TYPE\_SECTION\_FOREACH(struct struct\_type, secname, iterator)

259

[ 270](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)#define STRUCT\_SECTION\_FOREACH(struct\_type, iterator) \

271 STRUCT\_SECTION\_FOREACH\_ALTERNATE(struct\_type, struct\_type, iterator)

272

[ 282](group__iterable__section__apis.md#ga583e57b527884034116bf0b27a942b50)#define STRUCT\_SECTION\_GET(struct\_type, i, dst) \

283 TYPE\_SECTION\_GET(struct struct\_type, struct\_type, i, dst)

284

[ 291](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)#define STRUCT\_SECTION\_COUNT(struct\_type, dst) \

292 TYPE\_SECTION\_COUNT(struct struct\_type, struct\_type, dst);

293 /\* end of struct\_section\_apis \*/

297

298#ifdef \_\_cplusplus

299}

300#endif

301

302#endif /\* INCLUDE\_ZEPHYR\_SYS\_ITERABLE\_SECTIONS\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [iterable\_sections.h](sys_2iterable__sections_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
