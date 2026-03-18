---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/kobject__internal_8h_source.html
original_path: doxygen/html/kobject__internal_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kobject\_internal.h

[Go to the documentation of this file.](kobject__internal_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYS\_INTERNAL\_KOBJECT\_INTERNAL\_H

7#define ZEPHYR\_INCLUDE\_SYS\_INTERNAL\_KOBJECT\_INTERNAL\_H

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

18

19#if defined(CONFIG\_USERSPACE) || defined(\_\_DOXYGEN\_\_)

20#if defined(CONFIG\_GEN\_PRIV\_STACKS) || defined(\_\_DOXYGEN\_\_)

21/\* Metadata struct for K\_OBJ\_THREAD\_STACK\_ELEMENT \*/

22struct z\_stack\_data {

23 /\* Size of the entire stack object, including reserved areas \*/

24 size\_t size;

25

26 /\* Stack buffer for privilege mode elevations \*/

27 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*priv;

28};

29#endif /\* CONFIG\_GEN\_PRIV\_STACKS \*/

30

31/\* Object extra data. Only some objects use this, determined by object type \*/

[ 32](unionk__object__data.md)union [k\_object\_data](unionk__object__data.md) {

33 /\* Backing mutex for K\_OBJ\_SYS\_MUTEX \*/

[ 34](unionk__object__data.md#ab285ad5a6119657341be525276837fda) struct [k\_mutex](structk__mutex.md) \*[mutex](unionk__object__data.md#ab285ad5a6119657341be525276837fda);

35

36 /\* Numerical thread ID for K\_OBJ\_THREAD \*/

[ 37](unionk__object__data.md#ada581c427efa9e48b441b1a323bd57e6) unsigned int [thread\_id](unionk__object__data.md#ada581c427efa9e48b441b1a323bd57e6);

38

39#if defined(CONFIG\_GEN\_PRIV\_STACKS) || defined(\_\_DOXYGEN\_\_)

40 /\* Metadata for K\_OBJ\_THREAD\_STACK\_ELEMENT \*/

[ 41](unionk__object__data.md#ac8fdffd51c0b32ea262fa98a827a5bd4) const struct z\_stack\_data \*[stack\_data](unionk__object__data.md#ac8fdffd51c0b32ea262fa98a827a5bd4);

42#else

43 /\* Stack buffer size for K\_OBJ\_THREAD\_STACK\_ELEMENT \*/

44 size\_t stack\_size;

45#endif /\* CONFIG\_GEN\_PRIV\_STACKS \*/

46

47 /\* Futex wait queue and spinlock for K\_OBJ\_FUTEX \*/

[ 48](unionk__object__data.md#adc43cc4603b527b252e05df004cdbd64) struct z\_futex\_data \*[futex\_data](unionk__object__data.md#adc43cc4603b527b252e05df004cdbd64);

49

50 /\* All other objects \*/

[ 51](unionk__object__data.md#a2f95fd75c72a619e8c5224e64d1aacc0) int [unused](unionk__object__data.md#a2f95fd75c72a619e8c5224e64d1aacc0);

52};

53

[ 61](structk__object.md)struct [k\_object](structk__object.md) {

[ 62](structk__object.md#ad676d4edce580d351104fe09f174c323) void \*[name](structk__object.md#ad676d4edce580d351104fe09f174c323);

[ 63](structk__object.md#a9e32404b2259979e52b65983ad77ec58) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [perms](structk__object.md#a9e32404b2259979e52b65983ad77ec58)[CONFIG\_MAX\_THREAD\_BYTES];

[ 64](structk__object.md#a9c8686d9552cb48c24aef939c8a80057) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structk__object.md#a9c8686d9552cb48c24aef939c8a80057);

[ 65](structk__object.md#a351cbe565fef17ea75966085be3142c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structk__object.md#a351cbe565fef17ea75966085be3142c9);

[ 66](structk__object.md#aea0ad6871d88e2756ba0cbd482fa3aa7) union [k\_object\_data](unionk__object__data.md) [data](structk__object.md#aea0ad6871d88e2756ba0cbd482fa3aa7);

67} \_\_packed \_\_aligned(4);

68

[ 69](structk__object__assignment.md)struct [k\_object\_assignment](structk__object__assignment.md) {

[ 70](structk__object__assignment.md#aca82e8f65cfdcfb7497a4b9f3df4eb8d) struct [k\_thread](structk__thread.md) \*[thread](structk__object__assignment.md#aca82e8f65cfdcfb7497a4b9f3df4eb8d);

[ 71](structk__object__assignment.md#ad034fa126915ad604f1edc3b0a177d5a) void \* const \*[objects](structk__object__assignment.md#ad034fa126915ad604f1edc3b0a177d5a);

72};

73

74

[ 87](group__usermode__internal__apis.md#ga50528134a693d656cd60c001f50645ba)void [k\_object\_init](group__usermode__internal__apis.md#ga50528134a693d656cd60c001f50645ba)(const void \*obj);

88

89

90#else

91/\* LCOV\_EXCL\_START \*/

92static inline void [k\_object\_init](group__usermode__internal__apis.md#ga50528134a693d656cd60c001f50645ba)(const void \*obj)

93{

94 ARG\_UNUSED(obj);

95}

96/\* LCOV\_EXCL\_STOP \*/

97#endif /\* !CONFIG\_USERSPACE \*/

98

99#ifdef CONFIG\_DYNAMIC\_OBJECTS

123struct [k\_object](structk__object.md) \*[k\_object\_create\_dynamic\_aligned](group__usermode__internal__apis.md#gafc261408a120975732788b1bd9223036)(size\_t align, size\_t size);

124

147static inline struct [k\_object](structk__object.md) \*[k\_object\_create\_dynamic](group__usermode__internal__apis.md#ga3879ef0db97f968d82938da87698e359)(size\_t size)

148{

149 return [k\_object\_create\_dynamic\_aligned](group__usermode__internal__apis.md#gafc261408a120975732788b1bd9223036)(0, size);

150}

151

152#else

153

154/\* LCOV\_EXCL\_START \*/

[ 155](group__usermode__internal__apis.md#gafc261408a120975732788b1bd9223036)static inline struct [k\_object](structk__object.md) \*[k\_object\_create\_dynamic\_aligned](group__usermode__internal__apis.md#gafc261408a120975732788b1bd9223036)(size\_t align,

156 size\_t size)

157{

158 ARG\_UNUSED(align);

159 ARG\_UNUSED(size);

160

161 return NULL;

162}

163

[ 164](group__usermode__internal__apis.md#ga3879ef0db97f968d82938da87698e359)static inline struct [k\_object](structk__object.md) \*[k\_object\_create\_dynamic](group__usermode__internal__apis.md#ga3879ef0db97f968d82938da87698e359)(size\_t size)

165{

166 ARG\_UNUSED(size);

167

168 return NULL;

169}

170

171/\* LCOV\_EXCL\_STOP \*/

172#endif /\* CONFIG\_DYNAMIC\_OBJECTS \*/

173

175

176#ifdef \_\_cplusplus

177}

178#endif

179

180#endif

[k\_object\_create\_dynamic](group__usermode__internal__apis.md#ga3879ef0db97f968d82938da87698e359)

static struct k\_object \* k\_object\_create\_dynamic(size\_t size)

**Definition** kobject\_internal.h:164

[k\_object\_init](group__usermode__internal__apis.md#ga50528134a693d656cd60c001f50645ba)

void k\_object\_init(const void \*obj)

Lookup a kernel object and init its metadata if it exists.

[k\_object\_create\_dynamic\_aligned](group__usermode__internal__apis.md#gafc261408a120975732788b1bd9223036)

static struct k\_object \* k\_object\_create\_dynamic\_aligned(size\_t align, size\_t size)

**Definition** kobject\_internal.h:155

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[k\_object\_assignment](structk__object__assignment.md)

**Definition** kobject\_internal.h:69

[k\_object\_assignment::thread](structk__object__assignment.md#aca82e8f65cfdcfb7497a4b9f3df4eb8d)

struct k\_thread \* thread

**Definition** kobject\_internal.h:70

[k\_object\_assignment::objects](structk__object__assignment.md#ad034fa126915ad604f1edc3b0a177d5a)

void \*const \* objects

**Definition** kobject\_internal.h:71

[k\_object](structk__object.md)

Table generated by gperf, these objects are retrieved via k\_object\_find().

**Definition** kobject\_internal.h:61

[k\_object::flags](structk__object.md#a351cbe565fef17ea75966085be3142c9)

uint8\_t flags

**Definition** kobject\_internal.h:65

[k\_object::type](structk__object.md#a9c8686d9552cb48c24aef939c8a80057)

uint8\_t type

**Definition** kobject\_internal.h:64

[k\_object::perms](structk__object.md#a9e32404b2259979e52b65983ad77ec58)

uint8\_t perms[CONFIG\_MAX\_THREAD\_BYTES]

**Definition** kobject\_internal.h:63

[k\_object::name](structk__object.md#ad676d4edce580d351104fe09f174c323)

void \* name

**Definition** kobject\_internal.h:62

[k\_object::data](structk__object.md#aea0ad6871d88e2756ba0cbd482fa3aa7)

union k\_object\_data data

**Definition** kobject\_internal.h:66

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[k\_object\_data](unionk__object__data.md)

**Definition** kobject\_internal.h:32

[k\_object\_data::unused](unionk__object__data.md#a2f95fd75c72a619e8c5224e64d1aacc0)

int unused

**Definition** kobject\_internal.h:51

[k\_object\_data::mutex](unionk__object__data.md#ab285ad5a6119657341be525276837fda)

struct k\_mutex \* mutex

**Definition** kobject\_internal.h:34

[k\_object\_data::stack\_data](unionk__object__data.md#ac8fdffd51c0b32ea262fa98a827a5bd4)

const struct z\_stack\_data \* stack\_data

**Definition** kobject\_internal.h:41

[k\_object\_data::thread\_id](unionk__object__data.md#ada581c427efa9e48b441b1a323bd57e6)

unsigned int thread\_id

**Definition** kobject\_internal.h:37

[k\_object\_data::futex\_data](unionk__object__data.md#adc43cc4603b527b252e05df004cdbd64)

struct z\_futex\_data \* futex\_data

**Definition** kobject\_internal.h:48

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [internal](dir_2d80249c9e76d37bdecdf823a284a9b8.md)
- [kobject\_internal.h](kobject__internal_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
