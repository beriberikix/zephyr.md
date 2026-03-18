---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtio__mpsc_8h_source.html
original_path: doxygen/html/rtio__mpsc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_mpsc.h

[Go to the documentation of this file.](rtio__mpsc_8h.md)

1/\*

2 \* Copyright (c) 2010-2011 Dmitry Vyukov

3 \* Copyright (c) 2022 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_RTIO\_MPSC\_H\_

9#define ZEPHYR\_RTIO\_MPSC\_H\_

10

11#include <[stdint.h](stdint_8h.md)>

12#include <[stdbool.h](stdbool_8h.md)>

13#include <[zephyr/toolchain/common.h](common_8h.md)>

14#include <[zephyr/sys/atomic.h](atomic_8h.md)>

15#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

28/\*

29 \* On single core systems atomics are unnecessary

30 \* and cause a lot of unnecessary cache invalidation

31 \*

32 \* Using volatile to at least ensure memory is read/written

33 \* by the compiler generated op codes is enough.

34 \*

35 \* On SMP atomics \*must\* be used to ensure the pointers

36 \* are updated in the correct order and the values are

37 \* updated core caches correctly.

38 \*/

39#if defined(CONFIG\_SMP)

40

[ 41](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626)typedef [atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7) [mpsc\_ptr\_t](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626);

42

[ 43](group__rtio__mpsc.md#gab8d9c4ffe87940152156e90471b794a3)#define mpsc\_ptr\_get(ptr) atomic\_ptr\_get(&(ptr))

[ 44](group__rtio__mpsc.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)#define mpsc\_ptr\_set(ptr, val) atomic\_ptr\_set(&(ptr), val)

[ 45](group__rtio__mpsc.md#gaf008a0ceddef3c8bee343175199a2ddc)#define mpsc\_ptr\_set\_get(ptr, val) atomic\_ptr\_set(&(ptr), val)

46

47#else

48

49typedef struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*[mpsc\_ptr\_t](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626);

50

51#define mpsc\_ptr\_get(ptr) ptr

52#define mpsc\_ptr\_set(ptr, val) ptr = val

53#define mpsc\_ptr\_set\_get(ptr, val) \

54 ({ \

55 mpsc\_ptr\_t tmp = ptr; \

56 ptr = val; \

57 tmp; \

58 })

59

60#endif

61

77

[ 81](structrtio__mpsc__node.md)struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) {

[ 82](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b) [mpsc\_ptr\_t](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626) [next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b);

83};

84

[ 88](structrtio__mpsc.md)struct [rtio\_mpsc](structrtio__mpsc.md) {

[ 89](structrtio__mpsc.md#a428414dcd0cf037bb44a7adb2f5e457d) [mpsc\_ptr\_t](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626) [head](structrtio__mpsc.md#a428414dcd0cf037bb44a7adb2f5e457d);

[ 90](structrtio__mpsc.md#a82dee3ba37c8299adb68aac527696398) struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*[tail](structrtio__mpsc.md#a82dee3ba37c8299adb68aac527696398);

[ 91](structrtio__mpsc.md#a726de5d439073f63bf267788847bbfca) struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) [stub](structrtio__mpsc.md#a726de5d439073f63bf267788847bbfca);

92};

93

[ 101](group__rtio__mpsc.md#ga28bb135e2b2387928d8b1ece175c2387)#define RTIO\_MPSC\_INIT(symbol) \

102 { \

103 .head = (struct rtio\_mpsc\_node \*)&symbol.stub, \

104 .tail = (struct rtio\_mpsc\_node \*)&symbol.stub, \

105 .stub = { \

106 .next = NULL, \

107 }, \

108 }

109

[ 115](group__rtio__mpsc.md#ga8e10263b8b3897d57625e710de9abda3)static inline void [rtio\_mpsc\_init](group__rtio__mpsc.md#ga8e10263b8b3897d57625e710de9abda3)(struct [rtio\_mpsc](structrtio__mpsc.md) \*q)

116{

117 [mpsc\_ptr\_set](group__rtio__mpsc.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(q->[head](structrtio__mpsc.md#a428414dcd0cf037bb44a7adb2f5e457d), &q->[stub](structrtio__mpsc.md#a726de5d439073f63bf267788847bbfca));

118 q->[tail](structrtio__mpsc.md#a82dee3ba37c8299adb68aac527696398) = &q->[stub](structrtio__mpsc.md#a726de5d439073f63bf267788847bbfca);

119 [mpsc\_ptr\_set](group__rtio__mpsc.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(q->[stub](structrtio__mpsc.md#a726de5d439073f63bf267788847bbfca).[next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b), NULL);

120}

121

[ 128](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void [rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)(struct [rtio\_mpsc](structrtio__mpsc.md) \*q, struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*n)

129{

130 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*prev;

131 int key;

132

133 [mpsc\_ptr\_set](group__rtio__mpsc.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(n->[next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b), NULL);

134

135 key = [arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)();

136 prev = (struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*)[mpsc\_ptr\_set\_get](group__rtio__mpsc.md#gaf008a0ceddef3c8bee343175199a2ddc)(q->[head](structrtio__mpsc.md#a428414dcd0cf037bb44a7adb2f5e457d), n);

137 [mpsc\_ptr\_set](group__rtio__mpsc.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)(prev->[next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b), n);

138 [arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)(key);

139}

140

[ 147](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)static inline struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*[rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)(struct [rtio\_mpsc](structrtio__mpsc.md) \*q)

148{

149 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*head;

150 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*tail = q->[tail](structrtio__mpsc.md#a82dee3ba37c8299adb68aac527696398);

151 struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*[next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b) = (struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*)[mpsc\_ptr\_get](group__rtio__mpsc.md#gab8d9c4ffe87940152156e90471b794a3)(tail->[next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b));

152

153 /\* Skip over the stub/sentinel \*/

154 if (tail == &q->[stub](structrtio__mpsc.md#a726de5d439073f63bf267788847bbfca)) {

155 if ([next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b) == NULL) {

156 return NULL;

157 }

158

159 q->[tail](structrtio__mpsc.md#a82dee3ba37c8299adb68aac527696398) = [next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b);

160 tail = [next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b);

161 [next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b) = (struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*)[mpsc\_ptr\_get](group__rtio__mpsc.md#gab8d9c4ffe87940152156e90471b794a3)([next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b)->next);

162 }

163

164 /\* If next is non-NULL then a valid node is found, return it \*/

165 if ([next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b) != NULL) {

166 q->[tail](structrtio__mpsc.md#a82dee3ba37c8299adb68aac527696398) = [next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b);

167 return tail;

168 }

169

170 head = (struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*)[mpsc\_ptr\_get](group__rtio__mpsc.md#gab8d9c4ffe87940152156e90471b794a3)(q->[head](structrtio__mpsc.md#a428414dcd0cf037bb44a7adb2f5e457d));

171

172 /\* If next is NULL, and the tail != HEAD then the queue has pending

173 \* updates that can't yet be accessed.

174 \*/

175 if (tail != head) {

176 return NULL;

177 }

178

179 [rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)(q, &q->[stub](structrtio__mpsc.md#a726de5d439073f63bf267788847bbfca));

180

181 [next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b) = (struct [rtio\_mpsc\_node](structrtio__mpsc__node.md) \*)[mpsc\_ptr\_get](group__rtio__mpsc.md#gab8d9c4ffe87940152156e90471b794a3)(tail->[next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b));

182

183 if ([next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b) != NULL) {

184 q->[tail](structrtio__mpsc.md#a82dee3ba37c8299adb68aac527696398) = [next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b);

185 return tail;

186 }

187

188 return NULL;

189}

190

194

195#ifdef \_\_cplusplus

196}

197#endif

198

199#endif /\* ZEPHYR\_RTIO\_MPSC\_H\_ \*/

[atomic.h](atomic_8h.md)

[atomic\_ptr\_t](atomic__types_8h.md#acad6866fa4c844026cd9f8c3fb60ecd7)

void \* atomic\_ptr\_t

**Definition** atomic\_types.h:17

[common.h](common_8h.md)

Common toolchain abstraction.

[ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[arch\_irq\_lock](group__arch-irq.md#ga25bca3069cb999b6d4f924b87bf7de38)

static unsigned int arch\_irq\_lock(void)

Lock interrupts on the current CPU.

[arch\_irq\_unlock](group__arch-irq.md#gaa2b2745d8e99b8730b44805f4d3bbf05)

static void arch\_irq\_unlock(unsigned int key)

Unlock interrupts on the current CPU.

[rtio\_mpsc\_pop](group__rtio__mpsc.md#ga11697747c5377ccff4556d9d5dc96e56)

static struct rtio\_mpsc\_node \* rtio\_mpsc\_pop(struct rtio\_mpsc \*q)

Pop a node off of the list.

**Definition** rtio\_mpsc.h:147

[mpsc\_ptr\_t](group__rtio__mpsc.md#ga15b6ff032fa4602e72415cf95c69e626)

atomic\_ptr\_t mpsc\_ptr\_t

**Definition** rtio\_mpsc.h:41

[rtio\_mpsc\_push](group__rtio__mpsc.md#ga3ef9810ee938ecbc352a985baf60ade2)

static ALWAYS\_INLINE void rtio\_mpsc\_push(struct rtio\_mpsc \*q, struct rtio\_mpsc\_node \*n)

Push a node.

**Definition** rtio\_mpsc.h:128

[rtio\_mpsc\_init](group__rtio__mpsc.md#ga8e10263b8b3897d57625e710de9abda3)

static void rtio\_mpsc\_init(struct rtio\_mpsc \*q)

Initialize queue.

**Definition** rtio\_mpsc.h:115

[mpsc\_ptr\_set](group__rtio__mpsc.md#ga92c1bf9ee6d74bc9325e3d1f99bc66a9)

#define mpsc\_ptr\_set(ptr, val)

**Definition** rtio\_mpsc.h:44

[mpsc\_ptr\_get](group__rtio__mpsc.md#gab8d9c4ffe87940152156e90471b794a3)

#define mpsc\_ptr\_get(ptr)

**Definition** rtio\_mpsc.h:43

[mpsc\_ptr\_set\_get](group__rtio__mpsc.md#gaf008a0ceddef3c8bee343175199a2ddc)

#define mpsc\_ptr\_set\_get(ptr, val)

**Definition** rtio\_mpsc.h:45

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[rtio\_mpsc\_node](structrtio__mpsc__node.md)

Queue member.

**Definition** rtio\_mpsc.h:81

[rtio\_mpsc\_node::next](structrtio__mpsc__node.md#a8011a410834dbf66c33099fa99ee1f4b)

mpsc\_ptr\_t next

**Definition** rtio\_mpsc.h:82

[rtio\_mpsc](structrtio__mpsc.md)

MPSC Queue.

**Definition** rtio\_mpsc.h:88

[rtio\_mpsc::head](structrtio__mpsc.md#a428414dcd0cf037bb44a7adb2f5e457d)

mpsc\_ptr\_t head

**Definition** rtio\_mpsc.h:89

[rtio\_mpsc::stub](structrtio__mpsc.md#a726de5d439073f63bf267788847bbfca)

struct rtio\_mpsc\_node stub

**Definition** rtio\_mpsc.h:91

[rtio\_mpsc::tail](structrtio__mpsc.md#a82dee3ba37c8299adb68aac527696398)

struct rtio\_mpsc\_node \* tail

**Definition** rtio\_mpsc.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio\_mpsc.h](rtio__mpsc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
