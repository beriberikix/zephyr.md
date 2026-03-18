---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/atomic_8h_source.html
original_path: doxygen/html/atomic_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atomic.h

[Go to the documentation of this file.](atomic_8h.md)

1/\*

2 \* Copyright (c) 1997-2015, Wind River Systems, Inc.

3 \* Copyright (c) 2021 Intel Corporation

4 \* Copyright (c) 2023 Nordic Semiconductor ASA

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_H\_

10#define ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_H\_

11

12#include <[stdbool.h](stdbool_8h.md)>

13#include <[zephyr/toolchain.h](toolchain_8h.md)>

14#include <stddef.h>

15

16#include <[zephyr/sys/atomic\_types.h](atomic__types_8h.md)> /\* IWYU pragma: export \*/

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

24/\* Low-level primitives come in several styles: \*/

25

26#if defined(CONFIG\_ATOMIC\_OPERATIONS\_C)

27/\* Generic-but-slow implementation based on kernel locking and syscalls \*/

28#include <[zephyr/sys/atomic\_c.h](atomic__c_8h.md)>

29#elif defined(CONFIG\_ATOMIC\_OPERATIONS\_ARCH)

30/\* Some architectures need their own implementation \*/

31# ifdef CONFIG\_XTENSA

32/\* Not all Xtensa toolchains support GCC-style atomic intrinsics \*/

33# include <[zephyr/arch/xtensa/atomic\_xtensa.h](atomic__xtensa_8h.md)>

34# else

35/\* Other arch specific implementation \*/

36# include <[zephyr/sys/atomic\_arch.h](atomic__arch_8h.md)>

37# endif /\* CONFIG\_XTENSA \*/

38#else

39/\* Default. See this file for the Doxygen reference: \*/

40#include <[zephyr/sys/atomic\_builtin.h](atomic__builtin_8h.md)>

41#endif

42

43/\* Portable higher-level utilities: \*/

44

50

[ 59](group__atomic__apis.md#gaadfbba86627ee7eeb07e04f712550f73)#define ATOMIC\_INIT(i) (i)

60

[ 70](group__atomic__apis.md#ga7366802f7b11d3c5f9487f4fea9fc4d7)#define ATOMIC\_PTR\_INIT(p) (p)

71

75

76#define ATOMIC\_BITS (sizeof(atomic\_val\_t) \* 8)

77#define ATOMIC\_MASK(bit) BIT((unsigned long)(bit) & (ATOMIC\_BITS - 1U))

78#define ATOMIC\_ELEM(addr, bit) ((addr) + ((bit) / ATOMIC\_BITS))

79

83

[ 90](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)#define ATOMIC\_BITMAP\_SIZE(num\_bits) (ROUND\_UP(num\_bits, ATOMIC\_BITS) / ATOMIC\_BITS)

91

[ 111](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)#define ATOMIC\_DEFINE(name, num\_bits) \

112 atomic\_t name[ATOMIC\_BITMAP\_SIZE(num\_bits)]

113

[ 127](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)static inline bool [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit)

128{

129 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) val = [atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(ATOMIC\_ELEM(target, bit));

130

131 return (1 & (val >> (bit & (ATOMIC\_BITS - 1)))) != 0;

132}

133

[ 147](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472)static inline bool [atomic\_test\_and\_clear\_bit](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit)

148{

149 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) mask = ATOMIC\_MASK(bit);

150 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old;

151

152 old = [atomic\_and](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d)(ATOMIC\_ELEM(target, bit), ~mask);

153

154 return (old & mask) != 0;

155}

156

[ 170](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)static inline bool [atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit)

171{

172 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) mask = ATOMIC\_MASK(bit);

173 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old;

174

175 old = [atomic\_or](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764)(ATOMIC\_ELEM(target, bit), mask);

176

177 return (old & mask) != 0;

178}

179

[ 191](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)static inline void [atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit)

192{

193 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) mask = ATOMIC\_MASK(bit);

194

195 (void)[atomic\_and](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d)(ATOMIC\_ELEM(target, bit), ~mask);

196}

197

[ 209](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0)static inline void [atomic\_set\_bit](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit)

210{

211 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) mask = ATOMIC\_MASK(bit);

212

213 (void)[atomic\_or](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764)(ATOMIC\_ELEM(target, bit), mask);

214}

215

[ 228](group__atomic__apis.md#gad749f16ca51ffc26e7303988de1b8dbf)static inline void [atomic\_set\_bit\_to](group__atomic__apis.md#gad749f16ca51ffc26e7303988de1b8dbf)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, int bit, bool val)

229{

230 [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) mask = ATOMIC\_MASK(bit);

231

232 if (val) {

233 (void)[atomic\_or](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764)(ATOMIC\_ELEM(target, bit), mask);

234 } else {

235 (void)[atomic\_and](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d)(ATOMIC\_ELEM(target, bit), ~mask);

236 }

237}

238

[ 254](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)bool [atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) old\_value, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) new\_value);

255

[ 271](group__atomic__apis.md#ga98f03db5ef2b36ff3412506a7f6d9558)bool [atomic\_ptr\_cas](group__atomic__apis.md#ga98f03db5ef2b36ff3412506a7f6d9558)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) old\_value,

272 [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) new\_value);

273

[ 286](group__atomic__apis.md#ga518c07595daaca29a9e53071ed59c9c0)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_add](group__atomic__apis.md#ga518c07595daaca29a9e53071ed59c9c0)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

287

[ 300](group__atomic__apis.md#ga84ab58fd0a6dbbf1bf675722b5900bd7)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_sub](group__atomic__apis.md#ga84ab58fd0a6dbbf1bf675722b5900bd7)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

301

[ 313](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

314

[ 326](group__atomic__apis.md#gac260f0efbd970717eae4ac3bb493a0c4)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_dec](group__atomic__apis.md#gac260f0efbd970717eae4ac3bb493a0c4)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

327

[ 339](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)(const [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

340

[ 352](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2)[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2)(const [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target);

353

[ 367](group__atomic__apis.md#ga5f0555245d8932c2e7f7e94575e1a095)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_set](group__atomic__apis.md#ga5f0555245d8932c2e7f7e94575e1a095)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

368

[ 382](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target, [atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) value);

383

[ 396](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_clear](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target);

397

[ 410](group__atomic__apis.md#ga587e3134cd8176e7b1c00361711ee2df)[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4) [atomic\_ptr\_clear](group__atomic__apis.md#ga587e3134cd8176e7b1c00361711ee2df)([atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) \*target);

411

[ 425](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_or](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

426

[ 440](group__atomic__apis.md#ga18592bcf38d667fb9b428f81ea691bd4)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_xor](group__atomic__apis.md#ga18592bcf38d667fb9b428f81ea691bd4)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

441

[ 455](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_and](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

456

[ 470](group__atomic__apis.md#ga3e954286e40de73e45598a00a0a2b864)[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) [atomic\_nand](group__atomic__apis.md#ga3e954286e40de73e45598a00a0a2b864)([atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*target, [atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1) value);

471

475

476#ifdef \_\_cplusplus

477} /\* extern "C" \*/

478#endif

479

480#endif /\* ZEPHYR\_INCLUDE\_SYS\_ATOMIC\_H\_ \*/

[atomic\_arch.h](atomic__arch_8h.md)

[atomic\_builtin.h](atomic__builtin_8h.md)

[atomic\_c.h](atomic__c_8h.md)

[atomic\_types.h](atomic__types_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[atomic\_val\_t](atomic__types_8h.md#a2df48927d9883550372b6e209b1997b1)

atomic\_t atomic\_val\_t

**Definition** atomic\_types.h:16

[atomic\_ptr\_val\_t](atomic__types_8h.md#a374deb49b6dab1420a835b01433eb2f4)

atomic\_ptr\_t atomic\_ptr\_val\_t

**Definition** atomic\_types.h:18

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

[atomic\_xtensa.h](atomic__xtensa_8h.md)

[atomic\_or](group__atomic__apis.md#ga1564a44a260e7d0d02e30ae045a99764)

atomic\_val\_t atomic\_or(atomic\_t \*target, atomic\_val\_t value)

Atomic bitwise inclusive OR.

[atomic\_set\_bit](group__atomic__apis.md#ga17a3961ba7610ad6e595e602f70344a0)

static void atomic\_set\_bit(atomic\_t \*target, int bit)

Atomically set a bit.

**Definition** atomic.h:209

[atomic\_xor](group__atomic__apis.md#ga18592bcf38d667fb9b428f81ea691bd4)

atomic\_val\_t atomic\_xor(atomic\_t \*target, atomic\_val\_t value)

Atomic bitwise exclusive OR (XOR).

[atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)

static bool atomic\_test\_bit(const atomic\_t \*target, int bit)

Atomically test a bit.

**Definition** atomic.h:127

[atomic\_clear\_bit](group__atomic__apis.md#ga1c1693d524c49d11fd32b323a39d718e)

static void atomic\_clear\_bit(atomic\_t \*target, int bit)

Atomically clear a bit.

**Definition** atomic.h:191

[atomic\_ptr\_get](group__atomic__apis.md#ga250c4672ce7749261bdb8b2f0c767da2)

atomic\_ptr\_val\_t atomic\_ptr\_get(const atomic\_ptr\_t \*target)

Atomic get a pointer value.

[atomic\_get](group__atomic__apis.md#ga33bb426a17535bd1022895a7e44b32fa)

atomic\_val\_t atomic\_get(const atomic\_t \*target)

Atomic get.

[atomic\_ptr\_set](group__atomic__apis.md#ga3a57fd7f76f84e0f5800878b8f81fc35)

atomic\_ptr\_val\_t atomic\_ptr\_set(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t value)

Atomic get-and-set for pointer values.

[atomic\_nand](group__atomic__apis.md#ga3e954286e40de73e45598a00a0a2b864)

atomic\_val\_t atomic\_nand(atomic\_t \*target, atomic\_val\_t value)

Atomic bitwise NAND.

[atomic\_and](group__atomic__apis.md#ga4bc1f6a6f5d98eef742b4541d235811d)

atomic\_val\_t atomic\_and(atomic\_t \*target, atomic\_val\_t value)

Atomic bitwise AND.

[atomic\_add](group__atomic__apis.md#ga518c07595daaca29a9e53071ed59c9c0)

atomic\_val\_t atomic\_add(atomic\_t \*target, atomic\_val\_t value)

Atomic addition.

[atomic\_test\_and\_clear\_bit](group__atomic__apis.md#ga53159437721084da0ec8ee70ec212472)

static bool atomic\_test\_and\_clear\_bit(atomic\_t \*target, int bit)

Atomically test and clear a bit.

**Definition** atomic.h:147

[atomic\_ptr\_clear](group__atomic__apis.md#ga587e3134cd8176e7b1c00361711ee2df)

atomic\_ptr\_val\_t atomic\_ptr\_clear(atomic\_ptr\_t \*target)

Atomic clear of a pointer value.

[atomic\_set](group__atomic__apis.md#ga5f0555245d8932c2e7f7e94575e1a095)

atomic\_val\_t atomic\_set(atomic\_t \*target, atomic\_val\_t value)

Atomic get-and-set.

[atomic\_test\_and\_set\_bit](group__atomic__apis.md#ga7ff45e13aa5f8be5d7a550e49f5c720b)

static bool atomic\_test\_and\_set\_bit(atomic\_t \*target, int bit)

Atomically set a bit.

**Definition** atomic.h:170

[atomic\_sub](group__atomic__apis.md#ga84ab58fd0a6dbbf1bf675722b5900bd7)

atomic\_val\_t atomic\_sub(atomic\_t \*target, atomic\_val\_t value)

Atomic subtraction.

[atomic\_clear](group__atomic__apis.md#ga879b5f540c25fd09f1b84563e3dc8a91)

atomic\_val\_t atomic\_clear(atomic\_t \*target)

Atomic clear.

[atomic\_ptr\_cas](group__atomic__apis.md#ga98f03db5ef2b36ff3412506a7f6d9558)

bool atomic\_ptr\_cas(atomic\_ptr\_t \*target, atomic\_ptr\_val\_t old\_value, atomic\_ptr\_val\_t new\_value)

Atomic compare-and-set with pointer values.

[atomic\_inc](group__atomic__apis.md#gaae47a9cbe5a6534967b417f602b37ac2)

atomic\_val\_t atomic\_inc(atomic\_t \*target)

Atomic increment.

[atomic\_cas](group__atomic__apis.md#gab879da5aa1ffcc317adc664c016586f7)

bool atomic\_cas(atomic\_t \*target, atomic\_val\_t old\_value, atomic\_val\_t new\_value)

Atomic compare-and-set.

[atomic\_dec](group__atomic__apis.md#gac260f0efbd970717eae4ac3bb493a0c4)

atomic\_val\_t atomic\_dec(atomic\_t \*target)

Atomic decrement.

[atomic\_set\_bit\_to](group__atomic__apis.md#gad749f16ca51ffc26e7303988de1b8dbf)

static void atomic\_set\_bit\_to(atomic\_t \*target, int bit, bool val)

Atomically set a bit to a given value.

**Definition** atomic.h:228

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [atomic.h](atomic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
