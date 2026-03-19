---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mpsc__lockfree_8h_source.html
original_path: doxygen/html/mpsc__lockfree_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpsc\_lockfree.h

[Go to the documentation of this file.](mpsc__lockfree_8h.md)

1/\*

2 \* Copyright (c) 2010-2011 Dmitry Vyukov

3 \* Copyright (c) 2023 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_SYS\_MPSC\_LOCKFREE\_H\_

9#define ZEPHYR\_SYS\_MPSC\_LOCKFREE\_H\_

10

11#include <[stdint.h](stdint_8h.md)>

12#include <[stdbool.h](stdbool_8h.md)>

13#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

14#include <[zephyr/kernel.h](kernel_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

26

42

43/\*

44 \* On single core systems atomics are unnecessary

45 \* and cause a lot of unnecessary cache invalidation

46 \*

47 \* Using volatile to at least ensure memory is read/written

48 \* by the compiler generated op codes is enough.

49 \*

50 \* On SMP atomics \*must\* be used to ensure the pointers

51 \* are updated in the correct order.

52 \*/

53#if defined(CONFIG\_SMP)

54

[ 55](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626)typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) [mpsc\_ptr\_t](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626);

56

[ 57](group__mpsc__lockfree.md#gab8d9c4ffe87940152156e90471b794a3)#define mpsc\_ptr\_get(ptr) atomic\_ptr\_get(&(ptr))

[ 58](group__mpsc__lockfree.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)#define mpsc\_ptr\_set(ptr, val) atomic\_ptr\_set(&(ptr), val)

[ 59](group__mpsc__lockfree.md#gaf008a0ceddef3c8bee343175199a2ddc)#define mpsc\_ptr\_set\_get(ptr, val) atomic\_ptr\_set(&(ptr), val)

60

61#else /\* defined(CONFIG\_SMP) \*/

62

63typedef struct [mpsc\_node](structmpsc__node.md) \*[mpsc\_ptr\_t](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626);

64

65#define mpsc\_ptr\_get(ptr) ptr

66#define mpsc\_ptr\_set(ptr, val) ptr = val

67#define mpsc\_ptr\_set\_get(ptr, val) \

68 ({ \

69 mpsc\_ptr\_t tmp = ptr; \

70 ptr = val; \

71 tmp; \

72 })

73

74#endif /\* defined(CONFIG\_SMP) \*/

75

[ 79](structmpsc__node.md)struct [mpsc\_node](structmpsc__node.md) {

[ 80](structmpsc__node.md#a957c2906feb6135531a1167d153494f4) [mpsc\_ptr\_t](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626) [next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4);

81};

82

[ 86](structmpsc.md)struct [mpsc](structmpsc.md) {

[ 87](structmpsc.md#a39a19058689c20a0485cf5982e7fc833) [mpsc\_ptr\_t](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626) [head](structmpsc.md#a39a19058689c20a0485cf5982e7fc833);

[ 88](structmpsc.md#ac7046e3208693f0cc8937261679892df) struct [mpsc\_node](structmpsc__node.md) \*[tail](structmpsc.md#ac7046e3208693f0cc8937261679892df);

[ 89](structmpsc.md#a02e8a6d90efcb0838844f85244ca88dd) struct [mpsc\_node](structmpsc__node.md) [stub](structmpsc.md#a02e8a6d90efcb0838844f85244ca88dd);

90};

91

[ 99](group__mpsc__lockfree.md#ga378ad8e2b4cde0727996eb67b1751a2d)#define MPSC\_INIT(symbol) \

100 { \

101 .head = (struct mpsc\_node \*)&symbol.stub, \

102 .tail = (struct mpsc\_node \*)&symbol.stub, \

103 .stub = { \

104 .next = NULL, \

105 }, \

106 }

107

[ 113](group__mpsc__lockfree.md#gaf08a8c0094f998af98e4d1ec431fc490)static inline void [mpsc\_init](group__mpsc__lockfree.md#gaf08a8c0094f998af98e4d1ec431fc490)(struct [mpsc](structmpsc.md) \*q)

114{

115 [mpsc\_ptr\_set](group__mpsc__lockfree.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(q->[head](structmpsc.md#a39a19058689c20a0485cf5982e7fc833), &q->[stub](structmpsc.md#a02e8a6d90efcb0838844f85244ca88dd));

116 q->[tail](structmpsc.md#ac7046e3208693f0cc8937261679892df) = &q->[stub](structmpsc.md#a02e8a6d90efcb0838844f85244ca88dd);

117 [mpsc\_ptr\_set](group__mpsc__lockfree.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(q->[stub](structmpsc.md#a02e8a6d90efcb0838844f85244ca88dd).[next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4), NULL);

118}

119

[ 126](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(struct [mpsc](structmpsc.md) \*q, struct [mpsc\_node](structmpsc__node.md) \*n)

127{

128 struct [mpsc\_node](structmpsc__node.md) \*prev;

129 int key;

130

131 [mpsc\_ptr\_set](group__mpsc__lockfree.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(n->[next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4), NULL);

132

133 key = [arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)();

134 prev = (struct [mpsc\_node](structmpsc__node.md) \*)[mpsc\_ptr\_set\_get](group__mpsc__lockfree.md#gaf008a0ceddef3c8bee343175199a2ddc)(q->[head](structmpsc.md#a39a19058689c20a0485cf5982e7fc833), n);

135 [mpsc\_ptr\_set](group__mpsc__lockfree.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(prev->[next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4), n);

136 [arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)(key);

137}

138

[ 145](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)static inline struct [mpsc\_node](structmpsc__node.md) \*[mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)(struct [mpsc](structmpsc.md) \*q)

146{

147 struct [mpsc\_node](structmpsc__node.md) \*head;

148 struct [mpsc\_node](structmpsc__node.md) \*tail = q->[tail](structmpsc.md#ac7046e3208693f0cc8937261679892df);

149 struct [mpsc\_node](structmpsc__node.md) \*[next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4) = (struct [mpsc\_node](structmpsc__node.md) \*)[mpsc\_ptr\_get](group__mpsc__lockfree.md#gab8d9c4ffe87940152156e90471b794a3)(tail->[next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4));

150

151 /\* Skip over the stub/sentinel \*/

152 if (tail == &q->[stub](structmpsc.md#a02e8a6d90efcb0838844f85244ca88dd)) {

153 if ([next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4) == NULL) {

154 return NULL;

155 }

156

157 q->[tail](structmpsc.md#ac7046e3208693f0cc8937261679892df) = [next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4);

158 tail = [next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4);

159 [next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4) = (struct [mpsc\_node](structmpsc__node.md) \*)[mpsc\_ptr\_get](group__mpsc__lockfree.md#gab8d9c4ffe87940152156e90471b794a3)([next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4)->next);

160 }

161

162 /\* If next is non-NULL then a valid node is found, return it \*/

163 if ([next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4) != NULL) {

164 q->[tail](structmpsc.md#ac7046e3208693f0cc8937261679892df) = [next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4);

165 return tail;

166 }

167

168 head = (struct [mpsc\_node](structmpsc__node.md) \*)[mpsc\_ptr\_get](group__mpsc__lockfree.md#gab8d9c4ffe87940152156e90471b794a3)(q->[head](structmpsc.md#a39a19058689c20a0485cf5982e7fc833));

169

170 /\* If next is NULL, and the tail != HEAD then the queue has pending

171 \* updates that can't yet be accessed.

172 \*/

173 if (tail != head) {

174 return NULL;

175 }

176

177 [mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)(q, &q->[stub](structmpsc.md#a02e8a6d90efcb0838844f85244ca88dd));

178

179 [next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4) = (struct [mpsc\_node](structmpsc__node.md) \*)[mpsc\_ptr\_get](group__mpsc__lockfree.md#gab8d9c4ffe87940152156e90471b794a3)(tail->[next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4));

180

181 if ([next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4) != NULL) {

182 q->[tail](structmpsc.md#ac7046e3208693f0cc8937261679892df) = [next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4);

183 return tail;

184 }

185

186 return NULL;

187}

188

192

193#ifdef \_\_cplusplus

194}

195#endif

196

197#endif /\* ZEPHYR\_SYS\_MPSC\_LOCKFREE\_H\_ \*/

[arch\_irq\_lock](arch_2arc_2v2_2irq_8h.md#a1496f4f860a99f42e1aee15ce5c9b3e2)

static ALWAYS\_INLINE unsigned int arch\_irq\_lock(void)

Disable all interrupts on the local CPU.

**Definition** irq.h:168

[arch\_irq\_unlock](arch_2arc_2v2_2irq_8h.md#a203e02b994beba0d006dad9f6d797c27)

static ALWAYS\_INLINE void arch\_irq\_unlock(unsigned int key)

**Definition** irq.h:176

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

[mpsc\_ptr\_t](group__mpsc__lockfree.md#ga15b6ff032fa4602e72415cf95c69e626)

atomic\_ptr\_t mpsc\_ptr\_t

**Definition** mpsc\_lockfree.h:55

[mpsc\_push](group__mpsc__lockfree.md#ga403add133841ef88e10d74141e782b37)

static ALWAYS\_INLINE void mpsc\_push(struct mpsc \*q, struct mpsc\_node \*n)

Push a node.

**Definition** mpsc\_lockfree.h:126

[mpsc\_pop](group__mpsc__lockfree.md#ga823ec37b84ac43e46167aac954bce9d7)

static struct mpsc\_node \* mpsc\_pop(struct mpsc \*q)

Pop a node off of the list.

**Definition** mpsc\_lockfree.h:145

[mpsc\_ptr\_set](group__mpsc__lockfree.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)

#define mpsc\_ptr\_set(ptr, val)

**Definition** mpsc\_lockfree.h:58

[mpsc\_ptr\_get](group__mpsc__lockfree.md#gab8d9c4ffe87940152156e90471b794a3)

#define mpsc\_ptr\_get(ptr)

**Definition** mpsc\_lockfree.h:57

[mpsc\_ptr\_set\_get](group__mpsc__lockfree.md#gaf008a0ceddef3c8bee343175199a2ddc)

#define mpsc\_ptr\_set\_get(ptr, val)

**Definition** mpsc\_lockfree.h:59

[mpsc\_init](group__mpsc__lockfree.md#gaf08a8c0094f998af98e4d1ec431fc490)

static void mpsc\_init(struct mpsc \*q)

Initialize queue.

**Definition** mpsc\_lockfree.h:113

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[mpsc\_node](structmpsc__node.md)

Queue member.

**Definition** mpsc\_lockfree.h:79

[mpsc\_node::next](structmpsc__node.md#a957c2906feb6135531a1167d153494f4)

mpsc\_ptr\_t next

**Definition** mpsc\_lockfree.h:80

[mpsc](structmpsc.md)

MPSC Queue.

**Definition** mpsc\_lockfree.h:86

[mpsc::stub](structmpsc.md#a02e8a6d90efcb0838844f85244ca88dd)

struct mpsc\_node stub

**Definition** mpsc\_lockfree.h:89

[mpsc::head](structmpsc.md#a39a19058689c20a0485cf5982e7fc833)

mpsc\_ptr\_t head

**Definition** mpsc\_lockfree.h:87

[mpsc::tail](structmpsc.md#ac7046e3208693f0cc8937261679892df)

struct mpsc\_node \* tail

**Definition** mpsc\_lockfree.h:88

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [mpsc\_lockfree.h](mpsc__lockfree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
