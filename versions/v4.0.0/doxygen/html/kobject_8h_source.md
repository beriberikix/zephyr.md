---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/kobject_8h_source.html
original_path: doxygen/html/kobject_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kobject.h

[Go to the documentation of this file.](kobject_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYS\_KOBJECT\_H

7#define ZEPHYR\_INCLUDE\_SYS\_KOBJECT\_H

8

9#include <[stdint.h](stdint_8h.md)>

10#include <stddef.h>

11

12#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

13#include <[zephyr/sys/internal/kobject\_internal.h](kobject__internal_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19struct [k\_thread](structk__thread.md);

20struct [k\_mutex](structk__mutex.md);

21struct z\_futex\_data;

22

[ 30](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1)enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) {

[ 31](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1a51b9ec845f71832ad8fbb35d0cb3e5f6) [K\_OBJ\_ANY](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1a51b9ec845f71832ad8fbb35d0cb3e5f6),

32

39#include <zephyr/kobj-types-enum.h>

42

[ 43](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1a7aecd777175f519ce8240e337e1cf430) [K\_OBJ\_LAST](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1a7aecd777175f519ce8240e337e1cf430)

44};

45

50

51#ifdef CONFIG\_USERSPACE

52

[ 65](group__usermode__apis.md#ga6a2dae4c6dc6959d8785ff1924b1b424)#define K\_THREAD\_ACCESS\_GRANT(name\_, ...) \

66 static void \* const \_CONCAT(\_object\_list\_, name\_)[] = \

67 { \_\_VA\_ARGS\_\_, NULL }; \

68 static const STRUCT\_SECTION\_ITERABLE(k\_object\_assignment, \

69 \_CONCAT(\_object\_access\_, name\_)) = \

70 { (&\_k\_thread\_obj\_ ## name\_), \

71 (\_CONCAT(\_object\_list\_, name\_)) }

72

[ 74](group__usermode__apis.md#ga1418482d67c7964855570fd0ac79628d)#define K\_OBJ\_FLAG\_INITIALIZED BIT(0)

[ 76](group__usermode__apis.md#ga8892f9343266ec24abf25e29f3f6bc9b)#define K\_OBJ\_FLAG\_PUBLIC BIT(1)

[ 78](group__usermode__apis.md#ga1bf7c8c1d5fe0a7358dd70c4663a5a7a)#define K\_OBJ\_FLAG\_ALLOC BIT(2)

[ 80](group__usermode__apis.md#ga82d3a7242074db70130415201d3d0fd6)#define K\_OBJ\_FLAG\_DRIVER BIT(3)

81

[ 92](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)\_\_syscall void [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)(const void \*object,

93 struct [k\_thread](structk__thread.md) \*thread);

94

[ 105](group__usermode__apis.md#gab70fe65497da1347cc4b7bf7ca2daf22)void [k\_object\_access\_revoke](group__usermode__apis.md#gab70fe65497da1347cc4b7bf7ca2daf22)(const void \*object, struct [k\_thread](structk__thread.md) \*thread);

106

[ 116](group__usermode__apis.md#ga3cb1a024c0178918def2dd0186e565b3)\_\_syscall void [k\_object\_release](group__usermode__apis.md#ga3cb1a024c0178918def2dd0186e565b3)(const void \*object);

117

[ 135](group__usermode__apis.md#gababc731e98a6378323c0d633b2abaa6a)void [k\_object\_access\_all\_grant](group__usermode__apis.md#gababc731e98a6378323c0d633b2abaa6a)(const void \*object);

136

[ 148](group__usermode__apis.md#gaacd9b4b517db99b3b027dd717e6746b4)bool [k\_object\_is\_valid](group__usermode__apis.md#gaacd9b4b517db99b3b027dd717e6746b4)(const void \*obj, enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype);

149

150#else

151/\* LCOV\_EXCL\_START \*/

152#define K\_THREAD\_ACCESS\_GRANT(thread, ...)

153

157static inline void z\_impl\_k\_object\_access\_grant(const void \*object,

158 struct [k\_thread](structk__thread.md) \*thread)

159{

160 ARG\_UNUSED(object);

161 ARG\_UNUSED(thread);

162}

163

167static inline void [k\_object\_access\_revoke](group__usermode__apis.md#gab70fe65497da1347cc4b7bf7ca2daf22)(const void \*object,

168 struct [k\_thread](structk__thread.md) \*thread)

169{

170 ARG\_UNUSED(object);

171 ARG\_UNUSED(thread);

172}

173

177static inline void z\_impl\_k\_object\_release(const void \*object)

178{

179 ARG\_UNUSED(object);

180}

181

182static inline void [k\_object\_access\_all\_grant](group__usermode__apis.md#gababc731e98a6378323c0d633b2abaa6a)(const void \*object)

183{

184 ARG\_UNUSED(object);

185}

186

187static inline bool [k\_object\_is\_valid](group__usermode__apis.md#gaacd9b4b517db99b3b027dd717e6746b4)(const void \*obj, enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype)

188{

189 ARG\_UNUSED(obj);

190 ARG\_UNUSED(otype);

191

192 return true;

193}

194

195/\* LCOV\_EXCL\_STOP \*/

196#endif /\* !CONFIG\_USERSPACE \*/

197

198#if defined(CONFIG\_DYNAMIC\_OBJECTS) || defined(\_\_DOXYGEN\_\_)

[ 217](group__usermode__apis.md#ga5bba3a354fbc63673c76c9815db40812)\_\_syscall void \*[k\_object\_alloc](group__usermode__apis.md#ga5bba3a354fbc63673c76c9815db40812)(enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype);

218

[ 238](group__usermode__apis.md#gab99a640325f14a6505a85218dcba5446)\_\_syscall void \*[k\_object\_alloc\_size](group__usermode__apis.md#gab99a640325f14a6505a85218dcba5446)(enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype, size\_t size);

239

[ 252](group__usermode__apis.md#ga9cc15e8fd7df9cb81c3d7b6c79917aab)void [k\_object\_free](group__usermode__apis.md#ga9cc15e8fd7df9cb81c3d7b6c79917aab)(void \*obj);

253#else

254

255/\* LCOV\_EXCL\_START \*/

256static inline void \*z\_impl\_k\_object\_alloc(enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype)

257{

258 ARG\_UNUSED(otype);

259

260 return NULL;

261}

262

263static inline void \*z\_impl\_k\_object\_alloc\_size(enum [k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1) otype,

264 size\_t size)

265{

266 ARG\_UNUSED(otype);

267 ARG\_UNUSED(size);

268

269 return NULL;

270}

271

277static inline void [k\_object\_free](group__usermode__apis.md#ga9cc15e8fd7df9cb81c3d7b6c79917aab)(void \*obj)

278{

279 ARG\_UNUSED(obj);

280}

281/\* LCOV\_EXCL\_STOP \*/

282#endif /\* CONFIG\_DYNAMIC\_OBJECTS \*/

283

285

286#include <zephyr/syscalls/kobject.h>

287#ifdef \_\_cplusplus

288}

289#endif

290

291#endif

[k\_object\_release](group__usermode__apis.md#ga3cb1a024c0178918def2dd0186e565b3)

void k\_object\_release(const void \*object)

Release an object.

[k\_object\_alloc](group__usermode__apis.md#ga5bba3a354fbc63673c76c9815db40812)

void \* k\_object\_alloc(enum k\_objects otype)

Allocate a kernel object of a designated type.

[k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22)

void k\_object\_access\_grant(const void \*object, struct k\_thread \*thread)

Grant a thread access to a kernel object.

[k\_object\_free](group__usermode__apis.md#ga9cc15e8fd7df9cb81c3d7b6c79917aab)

void k\_object\_free(void \*obj)

Free a kernel object previously allocated with k\_object\_alloc().

[k\_object\_is\_valid](group__usermode__apis.md#gaacd9b4b517db99b3b027dd717e6746b4)

bool k\_object\_is\_valid(const void \*obj, enum k\_objects otype)

Check if a kernel object is of certain type and is valid.

[k\_object\_access\_revoke](group__usermode__apis.md#gab70fe65497da1347cc4b7bf7ca2daf22)

void k\_object\_access\_revoke(const void \*object, struct k\_thread \*thread)

Revoke a thread's access to a kernel object.

[k\_object\_alloc\_size](group__usermode__apis.md#gab99a640325f14a6505a85218dcba5446)

void \* k\_object\_alloc\_size(enum k\_objects otype, size\_t size)

Allocate a kernel object of a designated type and a given size.

[k\_object\_access\_all\_grant](group__usermode__apis.md#gababc731e98a6378323c0d633b2abaa6a)

void k\_object\_access\_all\_grant(const void \*object)

Grant all present and future threads access to an object.

[k\_objects](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1)

k\_objects

Kernel Object Types.

**Definition** kobject.h:30

[K\_OBJ\_ANY](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1a51b9ec845f71832ad8fbb35d0cb3e5f6)

@ K\_OBJ\_ANY

**Definition** kobject.h:31

[K\_OBJ\_LAST](kobject_8h.md#af3a248c0e3b05c84b1dd38642f7cf2a1a7aecd777175f519ce8240e337e1cf430)

@ K\_OBJ\_LAST

**Definition** kobject.h:43

[kobject\_internal.h](kobject__internal_8h.md)

[stdint.h](stdint_8h.md)

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [kobject.h](kobject_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
