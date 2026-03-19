---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/p4wq_8h_source.html
original_path: doxygen/html/p4wq_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

p4wq.h

[Go to the documentation of this file.](p4wq_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYS\_P4WQ\_H\_

7#define ZEPHYR\_INCLUDE\_SYS\_P4WQ\_H\_

8

9#include <[zephyr/kernel.h](kernel_8h.md)>

10#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

11

12/\* Zephyr Pooled Parallel Preemptible Priority-based Work Queues \*/

13

14struct [k\_p4wq\_work](structk__p4wq__work.md);

15

[ 19](p4wq_8h.md#aa164250d00319b0d71670e95201e45b0)typedef void (\*[k\_p4wq\_handler\_t](p4wq_8h.md#aa164250d00319b0d71670e95201e45b0))(struct [k\_p4wq\_work](structk__p4wq__work.md) \*work);

20

[ 26](p4wq_8h.md#afa5f86d1b4679a2f07a9a7c7af71f12a)typedef void (\*[k\_p4wq\_done\_handler\_t](p4wq_8h.md#afa5f86d1b4679a2f07a9a7c7af71f12a))(struct [k\_p4wq\_work](structk__p4wq__work.md) \*work);

27

[ 36](structk__p4wq__work.md)struct [k\_p4wq\_work](structk__p4wq__work.md) {

37 /\* Filled out by submitting code \*/

[ 38](structk__p4wq__work.md#ac0420f86fea6302c6867d20705cda454) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [priority](structk__p4wq__work.md#ac0420f86fea6302c6867d20705cda454);

[ 39](structk__p4wq__work.md#a7d841cb4cd18d0a61c0eac7dd448f61c) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [deadline](structk__p4wq__work.md#a7d841cb4cd18d0a61c0eac7dd448f61c);

[ 40](structk__p4wq__work.md#ac1cc19646f95589ecfe8892c5666c5ef) [k\_p4wq\_handler\_t](p4wq_8h.md#aa164250d00319b0d71670e95201e45b0) [handler](structk__p4wq__work.md#ac1cc19646f95589ecfe8892c5666c5ef);

[ 41](structk__p4wq__work.md#a11eaae7aa6447baf732cf9060fbf70a4) bool [sync](structk__p4wq__work.md#a11eaae7aa6447baf732cf9060fbf70a4);

[ 42](structk__p4wq__work.md#a8dec82b6c03fab9316b7a96c99466920) struct k\_sem [done\_sem](structk__p4wq__work.md#a8dec82b6c03fab9316b7a96c99466920);

43

44 /\* reserved for implementation \*/

45 union {

[ 46](structk__p4wq__work.md#a6f02066d7035d0ffbd570395a65411e5) struct [rbnode](structk__p4wq__work.md#a6f02066d7035d0ffbd570395a65411e5) [rbnode](structk__p4wq__work.md#a6f02066d7035d0ffbd570395a65411e5);

[ 47](structk__p4wq__work.md#aadfa029b6833630ac9d4a3507452d278) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [dlnode](structk__p4wq__work.md#aadfa029b6833630ac9d4a3507452d278);

48 };

[ 49](structk__p4wq__work.md#aa767524655c69e35ef284b6de9af1f46) struct [k\_thread](structk__thread.md) \*[thread](structk__p4wq__work.md#aa767524655c69e35ef284b6de9af1f46);

[ 50](structk__p4wq__work.md#ac1ceadaf2e64eb13b1c89f7fb47efc38) struct [k\_p4wq](structk__p4wq.md) \*[queue](structk__p4wq__work.md#ac1ceadaf2e64eb13b1c89f7fb47efc38);

51};

52

[ 53](p4wq_8h.md#a8a2691219e517a0ac987aeb275b67487)#define K\_P4WQ\_QUEUE\_PER\_THREAD BIT(0)

[ 54](p4wq_8h.md#a8e0b60ac0b95772b5f5875669b8d6d01)#define K\_P4WQ\_DELAYED\_START BIT(1)

[ 55](p4wq_8h.md#a9e6b81f7c3ae916bde3048575cf9708d)#define K\_P4WQ\_USER\_CPU\_MASK BIT(2)

56

[ 62](structk__p4wq.md)struct [k\_p4wq](structk__p4wq.md) {

[ 63](structk__p4wq.md#abb4af1223997eb31ae7a17f3a933fb19) struct [k\_spinlock](structk__spinlock.md) [lock](structk__p4wq.md#abb4af1223997eb31ae7a17f3a933fb19);

64

65 /\* Pending threads waiting for work items

66 \*

67 \* FIXME: a waitq isn't really the right data structure here.

68 \* Wait queues are priority-sorted, but we don't want that

69 \* sorting overhead since we're effectively doing it ourselves

70 \* by directly mutating the priority when a thread is

71 \* unpended. We just want "blocked threads on a list", but

72 \* there's no clean scheduler API for that.

73 \*/

[ 74](structk__p4wq.md#a8cac5e806d2e432f50051db5a7d08c99) \_wait\_q\_t [waitq](structk__p4wq.md#a8cac5e806d2e432f50051db5a7d08c99);

75

76 /\* Work items waiting for processing \*/

[ 77](structk__p4wq.md#aa36eb7d19dd3da5be7668aee5231edf6) struct [rbtree](structrbtree.md) [queue](structk__p4wq.md#aa36eb7d19dd3da5be7668aee5231edf6);

78

79 /\* Work items in progress \*/

[ 80](structk__p4wq.md#afc1544bdca24633b3b30673686b93e9b) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [active](structk__p4wq.md#afc1544bdca24633b3b30673686b93e9b);

81

82 /\* K\_P4WQ\_\* flags above \*/

[ 83](structk__p4wq.md#a2f5cc7f74e4e46642ce3c5ef61555f94) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structk__p4wq.md#a2f5cc7f74e4e46642ce3c5ef61555f94);

84

85 /\* done handler which is called every time after work was successfully executed

86 \* and k\_p4wq\_work is not needed by p4wq anymore

87 \*/

[ 88](structk__p4wq.md#a02f45e9cee689e8d1bf092b4ffede65c) [k\_p4wq\_done\_handler\_t](p4wq_8h.md#afa5f86d1b4679a2f07a9a7c7af71f12a) [done\_handler](structk__p4wq.md#a02f45e9cee689e8d1bf092b4ffede65c);

89};

90

[ 91](structk__p4wq__initparam.md)struct [k\_p4wq\_initparam](structk__p4wq__initparam.md) {

[ 92](structk__p4wq__initparam.md#a399e8da451f26b06d2abf6a7a76b66b4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num](structk__p4wq__initparam.md#a399e8da451f26b06d2abf6a7a76b66b4);

[ 93](structk__p4wq__initparam.md#af317fe946a9a03e02608d521c46763ff) [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) [stack\_size](structk__p4wq__initparam.md#af317fe946a9a03e02608d521c46763ff);

[ 94](structk__p4wq__initparam.md#ac4c282b6fb6e343823d3ae68398df35a) struct [k\_p4wq](structk__p4wq.md) \*[queue](structk__p4wq__initparam.md#ac4c282b6fb6e343823d3ae68398df35a);

[ 95](structk__p4wq__initparam.md#a8dd0451e7bcc9819d4940db3cc7c0beb) struct [k\_thread](structk__thread.md) \*[threads](structk__p4wq__initparam.md#a8dd0451e7bcc9819d4940db3cc7c0beb);

[ 96](structk__p4wq__initparam.md#a50f2337a6597bfb9f2d74e5b49718217) struct z\_thread\_stack\_element \*[stacks](structk__p4wq__initparam.md#a50f2337a6597bfb9f2d74e5b49718217);

[ 97](structk__p4wq__initparam.md#a5962a73928834e1548ea8045945274c2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structk__p4wq__initparam.md#a5962a73928834e1548ea8045945274c2);

[ 98](structk__p4wq__initparam.md#ab9c606b36793301556c0af6cea41ce8b) [k\_p4wq\_done\_handler\_t](p4wq_8h.md#afa5f86d1b4679a2f07a9a7c7af71f12a) [done\_handler](structk__p4wq__initparam.md#ab9c606b36793301556c0af6cea41ce8b);

99};

100

[ 113](p4wq_8h.md#ac6e9c4e8e6236e97fb0d8a890b13a101)#define K\_P4WQ\_DEFINE\_WITH\_DONE\_HANDLER(name, n\_threads, stack\_sz, dn\_handler) \

114 static K\_THREAD\_STACK\_ARRAY\_DEFINE(\_p4stacks\_##name, \

115 n\_threads, stack\_sz); \

116 static struct k\_thread \_p4threads\_##name[n\_threads]; \

117 static struct k\_p4wq name; \

118 static const STRUCT\_SECTION\_ITERABLE(k\_p4wq\_initparam, \

119 \_init\_##name) = { \

120 .num = n\_threads, \

121 .stack\_size = stack\_sz, \

122 .threads = \_p4threads\_##name, \

123 .stacks = &(\_p4stacks\_##name[0][0]), \

124 .queue = &name, \

125 .flags = 0, \

126 .done\_handler = dn\_handler, \

127 }

128

[ 136](p4wq_8h.md#af37c37fe046571f9ed99e14325d7a321)#define K\_P4WQ\_DEFINE(name, n\_threads, stack\_sz) \

137 K\_P4WQ\_DEFINE\_WITH\_DONE\_HANDLER(name, n\_threads, stack\_sz, NULL)

138

[ 152](p4wq_8h.md#a409785d1aeaa3e6bd874bc8db1ef08e7)#define K\_P4WQ\_ARRAY\_DEFINE\_WITH\_DONE\_HANDLER(name, n\_threads, stack\_sz, flg, dn\_handler) \

153 static K\_THREAD\_STACK\_ARRAY\_DEFINE(\_p4stacks\_##name, \

154 n\_threads, stack\_sz); \

155 static struct k\_thread \_p4threads\_##name[n\_threads]; \

156 static struct k\_p4wq name[n\_threads]; \

157 static const STRUCT\_SECTION\_ITERABLE(k\_p4wq\_initparam, \

158 \_init\_##name) = { \

159 .num = n\_threads, \

160 .stack\_size = stack\_sz, \

161 .threads = \_p4threads\_##name, \

162 .stacks = &(\_p4stacks\_##name[0][0]), \

163 .queue = name, \

164 .flags = K\_P4WQ\_QUEUE\_PER\_THREAD | flg, \

165 .done\_handler = dn\_handler, \

166 }

167

[ 175](p4wq_8h.md#af4511892a31c6bb3c315ddacd869eb31)#define K\_P4WQ\_ARRAY\_DEFINE(name, n\_threads, stack\_sz, flg) \

176 K\_P4WQ\_ARRAY\_DEFINE\_WITH\_DONE\_HANDLER(name, n\_threads, stack\_sz, flg, NULL)

177

[ 187](p4wq_8h.md#aa67be80b892cbe9bf9eab475ac5c2eff)void [k\_p4wq\_init](p4wq_8h.md#aa67be80b892cbe9bf9eab475ac5c2eff)(struct [k\_p4wq](structk__p4wq.md) \*queue);

188

[ 201](p4wq_8h.md#a73397b7f22a3b1f0f7660081f9824527)void [k\_p4wq\_add\_thread](p4wq_8h.md#a73397b7f22a3b1f0f7660081f9824527)(struct [k\_p4wq](structk__p4wq.md) \*queue, struct [k\_thread](structk__thread.md) \*thread,

202 [k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1) \*stack,

203 size\_t stack\_size);

204

[ 226](p4wq_8h.md#a40e7660d999b94c517712d8b499dd157)void [k\_p4wq\_submit](p4wq_8h.md#a40e7660d999b94c517712d8b499dd157)(struct [k\_p4wq](structk__p4wq.md) \*queue, struct [k\_p4wq\_work](structk__p4wq__work.md) \*item);

227

[ 238](p4wq_8h.md#aede724dfe684f0a4e93845dee342f830)bool [k\_p4wq\_cancel](p4wq_8h.md#aede724dfe684f0a4e93845dee342f830)(struct [k\_p4wq](structk__p4wq.md) \*queue, struct [k\_p4wq\_work](structk__p4wq__work.md) \*item);

239

[ 243](p4wq_8h.md#a421ad1ac947495483b414ab89eb6996d)int [k\_p4wq\_wait](p4wq_8h.md#a421ad1ac947495483b414ab89eb6996d)(struct [k\_p4wq\_work](structk__p4wq__work.md) \*work, [k\_timeout\_t](structk__timeout__t.md) timeout);

244

[ 245](p4wq_8h.md#a6d22a84d473caff84684047e96ed70ac)void [k\_p4wq\_enable\_static\_thread](p4wq_8h.md#a6d22a84d473caff84684047e96ed70ac)(struct [k\_p4wq](structk__p4wq.md) \*queue, struct [k\_thread](structk__thread.md) \*thread,

246 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cpu\_mask);

247

248#endif /\* ZEPHYR\_INCLUDE\_SYS\_P4WQ\_H\_ \*/

[k\_thread\_stack\_t](arch__interface_8h.md#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)

struct z\_thread\_stack\_element k\_thread\_stack\_t

Typedef of struct z\_thread\_stack\_element.

**Definition** arch\_interface.h:46

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:50

[kernel.h](kernel_8h.md)

Public kernel APIs.

[k\_p4wq\_submit](p4wq_8h.md#a40e7660d999b94c517712d8b499dd157)

void k\_p4wq\_submit(struct k\_p4wq \*queue, struct k\_p4wq\_work \*item)

Submit work item to a P4 queue.

[k\_p4wq\_wait](p4wq_8h.md#a421ad1ac947495483b414ab89eb6996d)

int k\_p4wq\_wait(struct k\_p4wq\_work \*work, k\_timeout\_t timeout)

Regain ownership of the work item, wait for completion if it's synchronous.

[k\_p4wq\_enable\_static\_thread](p4wq_8h.md#a6d22a84d473caff84684047e96ed70ac)

void k\_p4wq\_enable\_static\_thread(struct k\_p4wq \*queue, struct k\_thread \*thread, uint32\_t cpu\_mask)

[k\_p4wq\_add\_thread](p4wq_8h.md#a73397b7f22a3b1f0f7660081f9824527)

void k\_p4wq\_add\_thread(struct k\_p4wq \*queue, struct k\_thread \*thread, k\_thread\_stack\_t \*stack, size\_t stack\_size)

Dynamically add a thread object to a P4 Queue pool.

[k\_p4wq\_handler\_t](p4wq_8h.md#aa164250d00319b0d71670e95201e45b0)

void(\* k\_p4wq\_handler\_t)(struct k\_p4wq\_work \*work)

P4 Queue handler callback.

**Definition** p4wq.h:19

[k\_p4wq\_init](p4wq_8h.md#aa67be80b892cbe9bf9eab475ac5c2eff)

void k\_p4wq\_init(struct k\_p4wq \*queue)

Initialize P4 Queue.

[k\_p4wq\_cancel](p4wq_8h.md#aede724dfe684f0a4e93845dee342f830)

bool k\_p4wq\_cancel(struct k\_p4wq \*queue, struct k\_p4wq\_work \*item)

Cancel submitted P4 work item.

[k\_p4wq\_done\_handler\_t](p4wq_8h.md#afa5f86d1b4679a2f07a9a7c7af71f12a)

void(\* k\_p4wq\_done\_handler\_t)(struct k\_p4wq\_work \*work)

Optional P4 Queue done callback.

**Definition** p4wq.h:26

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[k\_p4wq\_initparam](structk__p4wq__initparam.md)

**Definition** p4wq.h:91

[k\_p4wq\_initparam::num](structk__p4wq__initparam.md#a399e8da451f26b06d2abf6a7a76b66b4)

uint32\_t num

**Definition** p4wq.h:92

[k\_p4wq\_initparam::stacks](structk__p4wq__initparam.md#a50f2337a6597bfb9f2d74e5b49718217)

struct z\_thread\_stack\_element \* stacks

**Definition** p4wq.h:96

[k\_p4wq\_initparam::flags](structk__p4wq__initparam.md#a5962a73928834e1548ea8045945274c2)

uint32\_t flags

**Definition** p4wq.h:97

[k\_p4wq\_initparam::threads](structk__p4wq__initparam.md#a8dd0451e7bcc9819d4940db3cc7c0beb)

struct k\_thread \* threads

**Definition** p4wq.h:95

[k\_p4wq\_initparam::done\_handler](structk__p4wq__initparam.md#ab9c606b36793301556c0af6cea41ce8b)

k\_p4wq\_done\_handler\_t done\_handler

**Definition** p4wq.h:98

[k\_p4wq\_initparam::queue](structk__p4wq__initparam.md#ac4c282b6fb6e343823d3ae68398df35a)

struct k\_p4wq \* queue

**Definition** p4wq.h:94

[k\_p4wq\_initparam::stack\_size](structk__p4wq__initparam.md#af317fe946a9a03e02608d521c46763ff)

uintptr\_t stack\_size

**Definition** p4wq.h:93

[k\_p4wq\_work](structk__p4wq__work.md)

P4 Queue Work Item.

**Definition** p4wq.h:36

[k\_p4wq\_work::sync](structk__p4wq__work.md#a11eaae7aa6447baf732cf9060fbf70a4)

bool sync

**Definition** p4wq.h:41

[k\_p4wq\_work::rbnode](structk__p4wq__work.md#a6f02066d7035d0ffbd570395a65411e5)

struct rbnode rbnode

**Definition** p4wq.h:46

[k\_p4wq\_work::deadline](structk__p4wq__work.md#a7d841cb4cd18d0a61c0eac7dd448f61c)

int32\_t deadline

**Definition** p4wq.h:39

[k\_p4wq\_work::done\_sem](structk__p4wq__work.md#a8dec82b6c03fab9316b7a96c99466920)

struct k\_sem done\_sem

**Definition** p4wq.h:42

[k\_p4wq\_work::thread](structk__p4wq__work.md#aa767524655c69e35ef284b6de9af1f46)

struct k\_thread \* thread

**Definition** p4wq.h:49

[k\_p4wq\_work::dlnode](structk__p4wq__work.md#aadfa029b6833630ac9d4a3507452d278)

sys\_dlist\_t dlnode

**Definition** p4wq.h:47

[k\_p4wq\_work::priority](structk__p4wq__work.md#ac0420f86fea6302c6867d20705cda454)

int32\_t priority

**Definition** p4wq.h:38

[k\_p4wq\_work::handler](structk__p4wq__work.md#ac1cc19646f95589ecfe8892c5666c5ef)

k\_p4wq\_handler\_t handler

**Definition** p4wq.h:40

[k\_p4wq\_work::queue](structk__p4wq__work.md#ac1ceadaf2e64eb13b1c89f7fb47efc38)

struct k\_p4wq \* queue

**Definition** p4wq.h:50

[k\_p4wq](structk__p4wq.md)

P4 Queue.

**Definition** p4wq.h:62

[k\_p4wq::done\_handler](structk__p4wq.md#a02f45e9cee689e8d1bf092b4ffede65c)

k\_p4wq\_done\_handler\_t done\_handler

**Definition** p4wq.h:88

[k\_p4wq::flags](structk__p4wq.md#a2f5cc7f74e4e46642ce3c5ef61555f94)

uint32\_t flags

**Definition** p4wq.h:83

[k\_p4wq::waitq](structk__p4wq.md#a8cac5e806d2e432f50051db5a7d08c99)

\_wait\_q\_t waitq

**Definition** p4wq.h:74

[k\_p4wq::queue](structk__p4wq.md#aa36eb7d19dd3da5be7668aee5231edf6)

struct rbtree queue

**Definition** p4wq.h:77

[k\_p4wq::lock](structk__p4wq.md#abb4af1223997eb31ae7a17f3a933fb19)

struct k\_spinlock lock

**Definition** p4wq.h:63

[k\_p4wq::active](structk__p4wq.md#afc1544bdca24633b3b30673686b93e9b)

sys\_dlist\_t active

**Definition** p4wq.h:80

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[rbtree](structrbtree.md)

Balanced red/black tree structure.

**Definition** rb.h:91

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [p4wq.h](p4wq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
