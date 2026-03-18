---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rb_8h_source.html
original_path: doxygen/html/rb_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rb.h

[Go to the documentation of this file.](rb_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

36

37#ifndef ZEPHYR\_INCLUDE\_SYS\_RB\_H\_

38#define ZEPHYR\_INCLUDE\_SYS\_RB\_H\_

39

40#include <[stdbool.h](stdbool_8h.md)>

41#include <[stdint.h](stdint_8h.md)>

42

43/\* Our SDK/toolchains integration seems to be inconsistent about

44 \* whether they expose alloca.h or not. On gcc it's a moot point as

45 \* it's always builtin.

46 \*/

47#ifdef \_\_GNUC\_\_

48#ifndef alloca

49#define alloca \_\_builtin\_alloca

50#endif

51#else

52#include <alloca.h>

53#endif

54

[ 58](structrbnode.md)struct [rbnode](structrbnode.md) {

60 struct [rbnode](structrbnode.md) \*children[2];

62};

63

64/\* Theoretical maximum depth of tree based on pointer size. If memory

65 \* is filled with 2-pointer nodes, and the tree can be twice as a

66 \* packed binary tree, plus root... Works out to 59 entries for 32

67 \* bit pointers and 121 at 64 bits.

68 \*/

69#define Z\_TBITS(t) ((sizeof(t)) < 8 ? 2 : 3)

70#define Z\_PBITS(t) (8 \* sizeof(t))

71#define Z\_MAX\_RBTREE\_DEPTH (2 \* (Z\_PBITS(int \*) - Z\_TBITS(int \*) - 1) + 1)

72

[ 86](group__rbtree__apis.md#ga6c22a3d4a917b0a2e4328eb9df8e8615)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[rb\_lessthan\_t](group__rbtree__apis.md#ga6c22a3d4a917b0a2e4328eb9df8e8615))(struct [rbnode](structrbnode.md) \*a, struct [rbnode](structrbnode.md) \*b);

87

[ 91](structrbtree.md)struct [rbtree](structrbtree.md) {

[ 93](structrbtree.md#abd0a6e986acba39f103cb66fb1c3bd3b) struct [rbnode](structrbnode.md) \*[root](structrbtree.md#abd0a6e986acba39f103cb66fb1c3bd3b);

[ 95](structrbtree.md#aed5a31980a5cd818b91fd14ccf8bcd75) [rb\_lessthan\_t](group__rbtree__apis.md#ga6c22a3d4a917b0a2e4328eb9df8e8615) [lessthan\_fn](structrbtree.md#aed5a31980a5cd818b91fd14ccf8bcd75);

97 int max\_depth;

98#ifdef CONFIG\_MISRA\_SANE

99 struct [rbnode](structrbnode.md) \*iter\_stack[Z\_MAX\_RBTREE\_DEPTH];

100 unsigned char iter\_left[Z\_MAX\_RBTREE\_DEPTH];

101#endif

103};

104

[ 110](group__rbtree__apis.md#ga27e6996e6ed57aabb2791662960beca0)typedef void (\*[rb\_visit\_t](group__rbtree__apis.md#ga27e6996e6ed57aabb2791662960beca0))(struct [rbnode](structrbnode.md) \*node, void \*cookie);

111

112struct [rbnode](structrbnode.md) \*z\_rb\_child(struct [rbnode](structrbnode.md) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) side);

113int z\_rb\_is\_black(struct [rbnode](structrbnode.md) \*node);

114#ifndef CONFIG\_MISRA\_SANE

115void z\_rb\_walk(struct [rbnode](structrbnode.md) \*node, [rb\_visit\_t](group__rbtree__apis.md#ga27e6996e6ed57aabb2791662960beca0) visit\_fn, void \*cookie);

116#endif

117struct [rbnode](structrbnode.md) \*z\_rb\_get\_minmax(struct [rbtree](structrbtree.md) \*tree, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) side);

118

[ 122](group__rbtree__apis.md#ga6b2c6d796f333fb03e316afc42336ecf)void [rb\_insert](group__rbtree__apis.md#ga6b2c6d796f333fb03e316afc42336ecf)(struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node);

123

[ 127](group__rbtree__apis.md#ga8de6504411a0dbd8f4a43e9e18c53919)void [rb\_remove](group__rbtree__apis.md#ga8de6504411a0dbd8f4a43e9e18c53919)(struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node);

128

[ 132](group__rbtree__apis.md#ga2fe1a6028e972155acc0cc72429d8dec)static inline struct [rbnode](structrbnode.md) \*[rb\_get\_min](group__rbtree__apis.md#ga2fe1a6028e972155acc0cc72429d8dec)(struct [rbtree](structrbtree.md) \*tree)

133{

134 return z\_rb\_get\_minmax(tree, 0U);

135}

136

[ 140](group__rbtree__apis.md#ga031fd9abf8ae98fe0c7519465df522f6)static inline struct [rbnode](structrbnode.md) \*[rb\_get\_max](group__rbtree__apis.md#ga031fd9abf8ae98fe0c7519465df522f6)(struct [rbtree](structrbtree.md) \*tree)

141{

142 return z\_rb\_get\_minmax(tree, 1U);

143}

144

[ 154](group__rbtree__apis.md#ga918cb502c4b636f49a73906735612b91)bool [rb\_contains](group__rbtree__apis.md#ga918cb502c4b636f49a73906735612b91)(struct [rbtree](structrbtree.md) \*tree, struct [rbnode](structrbnode.md) \*node);

155

156#ifndef CONFIG\_MISRA\_SANE

[ 165](group__rbtree__apis.md#ga79e7c341ee876f1e6f6adaf8b1162995)static inline void [rb\_walk](group__rbtree__apis.md#ga79e7c341ee876f1e6f6adaf8b1162995)(struct [rbtree](structrbtree.md) \*tree, [rb\_visit\_t](group__rbtree__apis.md#ga27e6996e6ed57aabb2791662960beca0) visit\_fn,

166 void \*cookie)

167{

168 z\_rb\_walk(tree->[root](structrbtree.md#abd0a6e986acba39f103cb66fb1c3bd3b), visit\_fn, cookie);

169}

170#endif

171

172struct \_rb\_foreach {

173 struct rbnode \*\*stack;

174 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*is\_left;

175 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) top;

176};

177

178#ifdef CONFIG\_MISRA\_SANE

179#define \_RB\_FOREACH\_INIT(tree, node) { \

180 .stack = &(tree)->iter\_stack[0], \

181 .is\_left = &(tree)->iter\_left[0], \

182 .top = -1 \

183}

184#else

185#define \_RB\_FOREACH\_INIT(tree, node) { \

186 .stack = (struct rbnode \*\*) \

187 alloca((tree)->max\_depth \* sizeof(struct rbnode \*)), \

188 .is\_left = (uint8\_t \*)alloca((tree)->max\_depth \* sizeof(uint8\_t)),\

189 .top = -1 \

190}

191#endif

192

193struct [rbnode](structrbnode.md) \*z\_rb\_foreach\_next(struct [rbtree](structrbtree.md) \*tree, struct \_rb\_foreach \*f);

194

[ 216](group__rbtree__apis.md#gaa0a518139442a69865881f6b460b03df)#define RB\_FOR\_EACH(tree, node) \

217 for (struct \_rb\_foreach \_\_f = \_RB\_FOREACH\_INIT(tree, node); \

218 ((node) = z\_rb\_foreach\_next((tree), &\_\_f)); \

219 /\*\*/)

220

[ 231](group__rbtree__apis.md#gab03a8af066d5110cda6b7522f342b168)#define RB\_FOR\_EACH\_CONTAINER(tree, node, field) \

232 for (struct \_rb\_foreach \_\_f = \_RB\_FOREACH\_INIT(tree, node); \

233 ({struct rbnode \*n = z\_rb\_foreach\_next(tree, &\_\_f); \

234 (node) = n ? CONTAINER\_OF(n, \_\_typeof\_\_(\*(node)), \

235 field) : NULL; (node); }) != NULL; \

236 /\*\*/)

237

239

240#endif /\* ZEPHYR\_INCLUDE\_SYS\_RB\_H\_ \*/

[rb\_get\_max](group__rbtree__apis.md#ga031fd9abf8ae98fe0c7519465df522f6)

static struct rbnode \* rb\_get\_max(struct rbtree \*tree)

Returns the highest-sorted member of the tree.

**Definition** rb.h:140

[rb\_visit\_t](group__rbtree__apis.md#ga27e6996e6ed57aabb2791662960beca0)

void(\* rb\_visit\_t)(struct rbnode \*node, void \*cookie)

Prototype for node visitor callback.

**Definition** rb.h:110

[rb\_get\_min](group__rbtree__apis.md#ga2fe1a6028e972155acc0cc72429d8dec)

static struct rbnode \* rb\_get\_min(struct rbtree \*tree)

Returns the lowest-sorted member of the tree.

**Definition** rb.h:132

[rb\_insert](group__rbtree__apis.md#ga6b2c6d796f333fb03e316afc42336ecf)

void rb\_insert(struct rbtree \*tree, struct rbnode \*node)

Insert node into tree.

[rb\_lessthan\_t](group__rbtree__apis.md#ga6c22a3d4a917b0a2e4328eb9df8e8615)

bool(\* rb\_lessthan\_t)(struct rbnode \*a, struct rbnode \*b)

Red/black tree comparison predicate.

**Definition** rb.h:86

[rb\_walk](group__rbtree__apis.md#ga79e7c341ee876f1e6f6adaf8b1162995)

static void rb\_walk(struct rbtree \*tree, rb\_visit\_t visit\_fn, void \*cookie)

Walk/enumerate a rbtree.

**Definition** rb.h:165

[rb\_remove](group__rbtree__apis.md#ga8de6504411a0dbd8f4a43e9e18c53919)

void rb\_remove(struct rbtree \*tree, struct rbnode \*node)

Remove node from tree.

[rb\_contains](group__rbtree__apis.md#ga918cb502c4b636f49a73906735612b91)

bool rb\_contains(struct rbtree \*tree, struct rbnode \*node)

Returns true if the given node is part of the tree.

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[rbnode](structrbnode.md)

Balanced red/black tree node structure.

**Definition** rb.h:58

[rbtree](structrbtree.md)

Balanced red/black tree structure.

**Definition** rb.h:91

[rbtree::root](structrbtree.md#abd0a6e986acba39f103cb66fb1c3bd3b)

struct rbnode \* root

Root node of the tree.

**Definition** rb.h:93

[rbtree::lessthan\_fn](structrbtree.md#aed5a31980a5cd818b91fd14ccf8bcd75)

rb\_lessthan\_t lessthan\_fn

Comparison function for nodes in the tree.

**Definition** rb.h:95

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [rb.h](rb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
