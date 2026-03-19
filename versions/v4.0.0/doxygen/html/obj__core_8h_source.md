---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/obj__core_8h_source.html
original_path: doxygen/html/obj__core_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

obj\_core.h

[Go to the documentation of this file.](obj__core_8h.md)

1/\*

2 \* Copyright (c) 2023, Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_KERNEL\_OBJ\_CORE\_H\_\_

8#define \_\_KERNEL\_OBJ\_CORE\_H\_\_

9

10#include <[zephyr/sys/slist.h](slist_8h.md)>

11

17

[ 21](group__obj__core__apis.md#ga2bd0c2c121afc09448926a3648c7d814)#define K\_OBJ\_CORE(kobj) (&((kobj)->obj\_core))

22

[ 26](group__obj__core__apis.md#gaa02f30cae43a209c0c71a52d52354d3f)#define K\_OBJ\_TYPE\_ID\_GEN(s) ((s[0] << 24) | (s[1] << 16) | (s[2] << 8) | (s[3]))

27

28/\* Known kernel object types \*/

29

[ 31](group__obj__core__apis.md#gab8d2838ae8064facda465bb9db88e948)#define K\_OBJ\_TYPE\_CONDVAR\_ID K\_OBJ\_TYPE\_ID\_GEN("COND")

[ 33](group__obj__core__apis.md#ga59c569e93e1301903618fa0c53f642ec)#define K\_OBJ\_TYPE\_CPU\_ID K\_OBJ\_TYPE\_ID\_GEN("CPU\_")

[ 35](group__obj__core__apis.md#gac6fdf29f93b81f4a868ce39f3ae50c8c)#define K\_OBJ\_TYPE\_EVENT\_ID K\_OBJ\_TYPE\_ID\_GEN("EVNT")

[ 37](group__obj__core__apis.md#ga4eadc00416f1da919c5f49fea028b79f)#define K\_OBJ\_TYPE\_FIFO\_ID K\_OBJ\_TYPE\_ID\_GEN("FIFO")

[ 39](group__obj__core__apis.md#gad2b7452f304d6e27c612941a578cc651)#define K\_OBJ\_TYPE\_KERNEL\_ID K\_OBJ\_TYPE\_ID\_GEN("KRNL")

[ 41](group__obj__core__apis.md#ga956d61f2af839077adeb67ccd2e15d28)#define K\_OBJ\_TYPE\_LIFO\_ID K\_OBJ\_TYPE\_ID\_GEN("LIFO")

[ 43](group__obj__core__apis.md#ga83a03cfe8485b3e005ea2dc20a291115)#define K\_OBJ\_TYPE\_MEM\_BLOCK\_ID K\_OBJ\_TYPE\_ID\_GEN("MBLK")

[ 45](group__obj__core__apis.md#ga6ee0890bc9e22a381440a3e156c54f2e)#define K\_OBJ\_TYPE\_MBOX\_ID K\_OBJ\_TYPE\_ID\_GEN("MBOX")

[ 47](group__obj__core__apis.md#ga0d84b7ac3f48e2e2d0fcd3bfbeed2519)#define K\_OBJ\_TYPE\_MEM\_SLAB\_ID K\_OBJ\_TYPE\_ID\_GEN("SLAB")

[ 49](group__obj__core__apis.md#ga8bf245e4f25c61bb4ec8267b15384feb)#define K\_OBJ\_TYPE\_MSGQ\_ID K\_OBJ\_TYPE\_ID\_GEN("MSGQ")

[ 51](group__obj__core__apis.md#gab109845d59689ce64523786ccce9b8c6)#define K\_OBJ\_TYPE\_MUTEX\_ID K\_OBJ\_TYPE\_ID\_GEN("MUTX")

[ 53](group__obj__core__apis.md#ga36eb538a1bd7f8454a9da42de170d2a9)#define K\_OBJ\_TYPE\_PIPE\_ID K\_OBJ\_TYPE\_ID\_GEN("PIPE")

[ 55](group__obj__core__apis.md#gad08de0f2f76ad2fe368ed82524bd8335)#define K\_OBJ\_TYPE\_SEM\_ID K\_OBJ\_TYPE\_ID\_GEN("SEM4")

[ 57](group__obj__core__apis.md#gacb41863cbd89368e1204080e6f7f14c2)#define K\_OBJ\_TYPE\_STACK\_ID K\_OBJ\_TYPE\_ID\_GEN("STCK")

[ 59](group__obj__core__apis.md#gaf7adb45984ccfb2bbe64b1f8e559f24b)#define K\_OBJ\_TYPE\_THREAD\_ID K\_OBJ\_TYPE\_ID\_GEN("THRD")

[ 61](group__obj__core__apis.md#ga583ff6ce85756d9aa1b2baf7ac19574f)#define K\_OBJ\_TYPE\_TIMER\_ID K\_OBJ\_TYPE\_ID\_GEN("TIMR")

62

63struct [k\_obj\_type](structk__obj__type.md);

64struct [k\_obj\_core](structk__obj__core.md);

65

69

70#ifdef CONFIG\_OBJ\_CORE

71#define K\_OBJ\_CORE\_INIT(\_objp, \_obj\_type) \

72 extern struct k\_obj\_type \_obj\_type; \

73 k\_obj\_core\_init(\_objp, &\_obj\_type)

74

75#define K\_OBJ\_CORE\_LINK(objp) k\_obj\_core\_link(objp)

76#else

77#define K\_OBJ\_CORE\_INIT(objp, type) do { } while (0)

78#define K\_OBJ\_CORE\_LINK(objp) do { } while (0)

79#endif /\* CONFIG\_OBJ\_CORE \*/

80

84

89extern [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) z\_obj\_type\_list;

90

[ 92](structk__obj__core__stats__desc.md)struct [k\_obj\_core\_stats\_desc](structk__obj__core__stats__desc.md) {

[ 93](structk__obj__core__stats__desc.md#a2e81dccd36b1355f9e685917cbd8eed8) size\_t [raw\_size](structk__obj__core__stats__desc.md#a2e81dccd36b1355f9e685917cbd8eed8);

[ 94](structk__obj__core__stats__desc.md#a9d0757daab439142711e3866e6dabb8d) size\_t [query\_size](structk__obj__core__stats__desc.md#a9d0757daab439142711e3866e6dabb8d);

95

[ 97](structk__obj__core__stats__desc.md#a0b206ae290639095e722c1705a122c2f) int (\*[raw](structk__obj__core__stats__desc.md#a0b206ae290639095e722c1705a122c2f))(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats);

[ 99](structk__obj__core__stats__desc.md#a94723e6cd5c03769e9cc1be9f0ec784f) int (\*[query](structk__obj__core__stats__desc.md#a94723e6cd5c03769e9cc1be9f0ec784f))(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats);

[ 101](structk__obj__core__stats__desc.md#a2ab464c373aa3830eaf15e46de2e9370) int (\*[reset](structk__obj__core__stats__desc.md#a2ab464c373aa3830eaf15e46de2e9370))(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

[ 103](structk__obj__core__stats__desc.md#ab2959fb71fc5750d1a2ad71519f354b3) int (\*[disable](structk__obj__core__stats__desc.md#ab2959fb71fc5750d1a2ad71519f354b3))(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

[ 105](structk__obj__core__stats__desc.md#aabc9df81e93aa0ff0ec84983dd07f58f) int (\*[enable](structk__obj__core__stats__desc.md#aabc9df81e93aa0ff0ec84983dd07f58f))(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

106};

107

[ 109](structk__obj__type.md)struct [k\_obj\_type](structk__obj__type.md) {

[ 110](structk__obj__type.md#a96995171db1f9e3927058b2f4f22fb41) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structk__obj__type.md#a96995171db1f9e3927058b2f4f22fb41);

[ 111](structk__obj__type.md#ac00f591b7d19a0e2d43b167793ef0f29) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [list](structk__obj__type.md#ac00f591b7d19a0e2d43b167793ef0f29);

[ 112](structk__obj__type.md#acf48ce26b12ef2f1584b4d32f2b2b712) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structk__obj__type.md#acf48ce26b12ef2f1584b4d32f2b2b712);

[ 113](structk__obj__type.md#a39824fdc4dd042e1742c4d966b068a61) size\_t [obj\_core\_offset](structk__obj__type.md#a39824fdc4dd042e1742c4d966b068a61);

114#ifdef CONFIG\_OBJ\_CORE\_STATS

116 struct [k\_obj\_core\_stats\_desc](structk__obj__core__stats__desc.md) \*stats\_desc;

117#endif /\* CONFIG\_OBJ\_CORE\_STATS \*/

118};

119

[ 121](structk__obj__core.md)struct [k\_obj\_core](structk__obj__core.md) {

[ 122](structk__obj__core.md#a3ef8e436efe8b8daefef44c649222407) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structk__obj__core.md#a3ef8e436efe8b8daefef44c649222407);

[ 123](structk__obj__core.md#ad08bd00d9d7f4d331ed0775514e766b5) struct [k\_obj\_type](structk__obj__type.md) \*[type](structk__obj__core.md#ad08bd00d9d7f4d331ed0775514e766b5);

124#ifdef CONFIG\_OBJ\_CORE\_STATS

125 void \*stats;

126#endif /\* CONFIG\_OBJ\_CORE\_STATS \*/

127};

128

141struct [k\_obj\_type](structk__obj__type.md) \*z\_obj\_type\_init(struct [k\_obj\_type](structk__obj__type.md) \*type,

142 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id, size\_t [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394));

143

[ 155](group__obj__core__apis.md#ga325c21774af7d3f092dcab17d8f260fd)struct [k\_obj\_type](structk__obj__type.md) \*[k\_obj\_type\_find](group__obj__core__apis.md#ga325c21774af7d3f092dcab17d8f260fd)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type\_id);

156

[ 174](group__obj__core__apis.md#ga1e9a331ca6f3f7bf1f0e3b144b964b9b)int [k\_obj\_type\_walk\_locked](group__obj__core__apis.md#ga1e9a331ca6f3f7bf1f0e3b144b964b9b)(struct [k\_obj\_type](structk__obj__type.md) \*type,

175 int (\*func)(struct [k\_obj\_core](structk__obj__core.md) \*, void \*),

176 void \*data);

177

[ 196](group__obj__core__apis.md#ga4d3da7db72063699b66a54e56cf75e2e)int [k\_obj\_type\_walk\_unlocked](group__obj__core__apis.md#ga4d3da7db72063699b66a54e56cf75e2e)(struct [k\_obj\_type](structk__obj__type.md) \*type,

197 int (\*func)(struct [k\_obj\_core](structk__obj__core.md) \*, void \*),

198 void \*data);

199

[ 209](group__obj__core__apis.md#gaf00bc2c3bfa0420f00fe5bf49796b3a0)void [k\_obj\_core\_init](group__obj__core__apis.md#gaf00bc2c3bfa0420f00fe5bf49796b3a0)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, struct [k\_obj\_type](structk__obj__type.md) \*type);

210

[ 221](group__obj__core__apis.md#ga6b4a21304216582d7cc16088b00e69bf)void [k\_obj\_core\_link](group__obj__core__apis.md#ga6b4a21304216582d7cc16088b00e69bf)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

222

[ 232](group__obj__core__apis.md#gab1563101ae5f163fcbc06dc17660f9bc)void [k\_obj\_core\_init\_and\_link](group__obj__core__apis.md#gab1563101ae5f163fcbc06dc17660f9bc)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core,

233 struct [k\_obj\_type](structk__obj__type.md) \*type);

234

[ 244](group__obj__core__apis.md#ga7cb5b22d776880313c91a14583bb5d62)void [k\_obj\_core\_unlink](group__obj__core__apis.md#ga7cb5b22d776880313c91a14583bb5d62)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

245

247

253

254#ifdef CONFIG\_OBJ\_CORE\_STATS

263static inline void k\_obj\_type\_stats\_init(struct [k\_obj\_type](structk__obj__type.md) \*type,

264 struct [k\_obj\_core\_stats\_desc](structk__obj__core__stats__desc.md) \*stats\_desc)

265{

266 type->stats\_desc = stats\_desc;

267}

268

278static inline void k\_obj\_core\_stats\_init(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core,

279 void \*stats)

280{

281 obj\_core->stats = stats;

282}

283#endif /\* CONFIG\_OBJ\_CORE\_STATS \*/

284

[ 299](group__obj__core__stats__apis.md#gae3fda75cf0b9e3c91bfb5ba57239621d)int [k\_obj\_core\_stats\_register](group__obj__core__stats__apis.md#gae3fda75cf0b9e3c91bfb5ba57239621d)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats,

300 size\_t stats\_len);

301

[ 314](group__obj__core__stats__apis.md#gab2b23cf62d89e0bc21d89a0b77b01a21)int [k\_obj\_core\_stats\_deregister](group__obj__core__stats__apis.md#gab2b23cf62d89e0bc21d89a0b77b01a21)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

315

[ 331](group__obj__core__stats__apis.md#ga9c5f91bd221b9086ccaea7347ac357ab)int [k\_obj\_core\_stats\_raw](group__obj__core__stats__apis.md#ga9c5f91bd221b9086ccaea7347ac357ab)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats,

332 size\_t stats\_len);

333

[ 350](group__obj__core__stats__apis.md#ga52afc700fb116acfaa4dd5e1ca49a782)int [k\_obj\_core\_stats\_query](group__obj__core__stats__apis.md#ga52afc700fb116acfaa4dd5e1ca49a782)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats,

351 size\_t stats\_len);

352

[ 364](group__obj__core__stats__apis.md#ga0b4d2270e968e2c694290c0f90f208c4)int [k\_obj\_core\_stats\_reset](group__obj__core__stats__apis.md#ga0b4d2270e968e2c694290c0f90f208c4)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

365

[ 378](group__obj__core__stats__apis.md#ga547b121e75aeafc2f54dba2d58ca62db)int [k\_obj\_core\_stats\_disable](group__obj__core__stats__apis.md#ga547b121e75aeafc2f54dba2d58ca62db)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

379

[ 391](group__obj__core__stats__apis.md#ga079df60c5ba6dd08a2270362490553fa)int [k\_obj\_core\_stats\_enable](group__obj__core__stats__apis.md#ga079df60c5ba6dd08a2270362490553fa)(struct [k\_obj\_core](structk__obj__core.md) \*obj\_core);

392

394#endif /\* \_\_KERNEL\_OBJ\_CORE\_H\_\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[k\_obj\_type\_walk\_locked](group__obj__core__apis.md#ga1e9a331ca6f3f7bf1f0e3b144b964b9b)

int k\_obj\_type\_walk\_locked(struct k\_obj\_type \*type, int(\*func)(struct k\_obj\_core \*, void \*), void \*data)

Walk the object type's list of object cores.

[k\_obj\_type\_find](group__obj__core__apis.md#ga325c21774af7d3f092dcab17d8f260fd)

struct k\_obj\_type \* k\_obj\_type\_find(uint32\_t type\_id)

Find a specific object type by ID.

[k\_obj\_type\_walk\_unlocked](group__obj__core__apis.md#ga4d3da7db72063699b66a54e56cf75e2e)

int k\_obj\_type\_walk\_unlocked(struct k\_obj\_type \*type, int(\*func)(struct k\_obj\_core \*, void \*), void \*data)

Walk the object type's list of object cores.

[k\_obj\_core\_link](group__obj__core__apis.md#ga6b4a21304216582d7cc16088b00e69bf)

void k\_obj\_core\_link(struct k\_obj\_core \*obj\_core)

Link the kernel object to the kernel object type list.

[k\_obj\_core\_unlink](group__obj__core__apis.md#ga7cb5b22d776880313c91a14583bb5d62)

void k\_obj\_core\_unlink(struct k\_obj\_core \*obj\_core)

Unlink the kernel object from the kernel object type list.

[k\_obj\_core\_init\_and\_link](group__obj__core__apis.md#gab1563101ae5f163fcbc06dc17660f9bc)

void k\_obj\_core\_init\_and\_link(struct k\_obj\_core \*obj\_core, struct k\_obj\_type \*type)

Automatically link the kernel object after initializing it.

[k\_obj\_core\_init](group__obj__core__apis.md#gaf00bc2c3bfa0420f00fe5bf49796b3a0)

void k\_obj\_core\_init(struct k\_obj\_core \*obj\_core, struct k\_obj\_type \*type)

Initialize the core of the kernel object.

[k\_obj\_core\_stats\_enable](group__obj__core__stats__apis.md#ga079df60c5ba6dd08a2270362490553fa)

int k\_obj\_core\_stats\_enable(struct k\_obj\_core \*obj\_core)

Reset the stats associated with the kernel object.

[k\_obj\_core\_stats\_reset](group__obj__core__stats__apis.md#ga0b4d2270e968e2c694290c0f90f208c4)

int k\_obj\_core\_stats\_reset(struct k\_obj\_core \*obj\_core)

Reset the stats associated with the kernel object.

[k\_obj\_core\_stats\_query](group__obj__core__stats__apis.md#ga52afc700fb116acfaa4dd5e1ca49a782)

int k\_obj\_core\_stats\_query(struct k\_obj\_core \*obj\_core, void \*stats, size\_t stats\_len)

Retrieve the statistics associated with the kernel object.

[k\_obj\_core\_stats\_disable](group__obj__core__stats__apis.md#ga547b121e75aeafc2f54dba2d58ca62db)

int k\_obj\_core\_stats\_disable(struct k\_obj\_core \*obj\_core)

Stop gathering the stats associated with the kernel object.

[k\_obj\_core\_stats\_raw](group__obj__core__stats__apis.md#ga9c5f91bd221b9086ccaea7347ac357ab)

int k\_obj\_core\_stats\_raw(struct k\_obj\_core \*obj\_core, void \*stats, size\_t stats\_len)

Retrieve the raw statistics associated with the kernel object.

[k\_obj\_core\_stats\_deregister](group__obj__core__stats__apis.md#gab2b23cf62d89e0bc21d89a0b77b01a21)

int k\_obj\_core\_stats\_deregister(struct k\_obj\_core \*obj\_core)

Deregister kernel object from gathering statistics.

[k\_obj\_core\_stats\_register](group__obj__core__stats__apis.md#gae3fda75cf0b9e3c91bfb5ba57239621d)

int k\_obj\_core\_stats\_register(struct k\_obj\_core \*obj\_core, void \*stats, size\_t stats\_len)

Register kernel object for gathering statistics.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_obj\_core\_stats\_desc](structk__obj__core__stats__desc.md)

Object core statistics descriptor.

**Definition** obj\_core.h:92

[k\_obj\_core\_stats\_desc::raw](structk__obj__core__stats__desc.md#a0b206ae290639095e722c1705a122c2f)

int(\* raw)(struct k\_obj\_core \*obj\_core, void \*stats)

Function pointer to retrieve internal representation of stats.

**Definition** obj\_core.h:97

[k\_obj\_core\_stats\_desc::reset](structk__obj__core__stats__desc.md#a2ab464c373aa3830eaf15e46de2e9370)

int(\* reset)(struct k\_obj\_core \*obj\_core)

Function pointer to reset object's statistics.

**Definition** obj\_core.h:101

[k\_obj\_core\_stats\_desc::raw\_size](structk__obj__core__stats__desc.md#a2e81dccd36b1355f9e685917cbd8eed8)

size\_t raw\_size

Internal representation stats buffer size.

**Definition** obj\_core.h:93

[k\_obj\_core\_stats\_desc::query](structk__obj__core__stats__desc.md#a94723e6cd5c03769e9cc1be9f0ec784f)

int(\* query)(struct k\_obj\_core \*obj\_core, void \*stats)

Function pointer to retrieve reported statistics.

**Definition** obj\_core.h:99

[k\_obj\_core\_stats\_desc::query\_size](structk__obj__core__stats__desc.md#a9d0757daab439142711e3866e6dabb8d)

size\_t query\_size

Stats buffer size used for reporting.

**Definition** obj\_core.h:94

[k\_obj\_core\_stats\_desc::enable](structk__obj__core__stats__desc.md#aabc9df81e93aa0ff0ec84983dd07f58f)

int(\* enable)(struct k\_obj\_core \*obj\_core)

Function pointer to enable object's statistics gathering.

**Definition** obj\_core.h:105

[k\_obj\_core\_stats\_desc::disable](structk__obj__core__stats__desc.md#ab2959fb71fc5750d1a2ad71519f354b3)

int(\* disable)(struct k\_obj\_core \*obj\_core)

Function pointer to disable object's statistics gathering.

**Definition** obj\_core.h:103

[k\_obj\_core](structk__obj__core.md)

Object core structure.

**Definition** obj\_core.h:121

[k\_obj\_core::node](structk__obj__core.md#a3ef8e436efe8b8daefef44c649222407)

sys\_snode\_t node

Object node within object type's list.

**Definition** obj\_core.h:122

[k\_obj\_core::type](structk__obj__core.md#ad08bd00d9d7f4d331ed0775514e766b5)

struct k\_obj\_type \* type

Object type to which object belongs.

**Definition** obj\_core.h:123

[k\_obj\_type](structk__obj__type.md)

Object type structure.

**Definition** obj\_core.h:109

[k\_obj\_type::obj\_core\_offset](structk__obj__type.md#a39824fdc4dd042e1742c4d966b068a61)

size\_t obj\_core\_offset

Offset to obj\_core field.

**Definition** obj\_core.h:113

[k\_obj\_type::node](structk__obj__type.md#a96995171db1f9e3927058b2f4f22fb41)

sys\_snode\_t node

Node within list of object types.

**Definition** obj\_core.h:110

[k\_obj\_type::list](structk__obj__type.md#ac00f591b7d19a0e2d43b167793ef0f29)

sys\_slist\_t list

List of objects of this object type.

**Definition** obj\_core.h:111

[k\_obj\_type::id](structk__obj__type.md#acf48ce26b12ef2f1584b4d32f2b2b712)

uint32\_t id

Unique type ID.

**Definition** obj\_core.h:112

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [obj\_core.h](obj__core_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
