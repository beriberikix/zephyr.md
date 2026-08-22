---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ring__buffer_8h_source.html
original_path: doxygen/html/ring__buffer_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ring\_buffer.h

[Go to the documentation of this file.](ring__buffer_8h.md)

1/\*

2 \* Copyright (c) 2015 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_RING\_BUFFER\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_RING\_BUFFER\_H\_

9

10#include <[zephyr/sys/util.h](sys_2util_8h.md)>

11#include <[errno.h](errno_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

26

28

29/\* The limit is used by algorithm for distinguishing between empty and full

30 \* state.

31 \*/

32#ifdef CONFIG\_RING\_BUFFER\_LARGE

33typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_idx\_t;

34#define RING\_BUFFER\_MAX\_SIZE (UINT32\_MAX / 2)

35#else

36typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ring\_buf\_idx\_t;

37#define RING\_BUFFER\_MAX\_SIZE (UINT16\_MAX / 2)

38#endif

39

40#define RING\_BUFFER\_SIZE\_ASSERT\_MSG "Size too big"

41

42struct ring\_buf\_index { ring\_buf\_idx\_t head, tail, base; };

43

45

[ 49](structring__buf.md)struct [ring\_buf](structring__buf.md) {

51 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer;

52 struct ring\_buf\_index put;

53 struct ring\_buf\_index get;

54 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size;

56};

57

59

60[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_area\_claim(struct [ring\_buf](structring__buf.md) \*buf, struct ring\_buf\_index \*ring,

61 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

62int ring\_buf\_area\_finish(struct [ring\_buf](structring__buf.md) \*buf, struct ring\_buf\_index \*ring,

63 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

64

70static inline void ring\_buf\_internal\_reset(struct [ring\_buf](structring__buf.md) \*buf, ring\_buf\_idx\_t value)

71{

72 buf->put.head = buf->put.tail = buf->put.base = value;

73 buf->get.head = buf->get.tail = buf->get.base = value;

74}

75

77

[ 78](group__ring__buffer__apis.md#ga2ab4af6d5e79ed9ad8cfca22ec3a7107)#define RING\_BUF\_INIT(buf, size8) \

79{ \

80 .buffer = buf, \

81 .size = size8, \

82}

83

[ 98](group__ring__buffer__apis.md#ga803e45abf48ee207fc0ab4028726a82b)#define RING\_BUF\_DECLARE(name, size8) \

99 BUILD\_ASSERT(size8 <= RING\_BUFFER\_MAX\_SIZE,\

100 RING\_BUFFER\_SIZE\_ASSERT\_MSG); \

101 static uint8\_t \_\_noinit \_ring\_buffer\_data\_##name[size8]; \

102 struct ring\_buf name = RING\_BUF\_INIT(\_ring\_buffer\_data\_##name, size8)

103

[ 119](group__ring__buffer__apis.md#ga2fc2f4515121ac6bbf6aebf3e029bb5d)#define RING\_BUF\_ITEM\_DECLARE(name, size32) \

120 BUILD\_ASSERT((size32) <= RING\_BUFFER\_MAX\_SIZE / 4, \

121 RING\_BUFFER\_SIZE\_ASSERT\_MSG); \

122 static uint32\_t \_\_noinit \_ring\_buffer\_data\_##name[size32]; \

123 struct ring\_buf name = { \

124 .buffer = (uint8\_t \*) \_ring\_buffer\_data\_##name, \

125 .size = 4 \* (size32) \

126 }

127

[ 137](group__ring__buffer__apis.md#ga205e93b5431112da0d191526906c7e01)#define RING\_BUF\_ITEM\_DECLARE\_SIZE(name, size32) \

138 RING\_BUF\_ITEM\_DECLARE(name, size32)

139

[ 150](group__ring__buffer__apis.md#gaca98f407b222dff12e2bbfcf3746a9e3)#define RING\_BUF\_ITEM\_DECLARE\_POW2(name, pow) \

151 RING\_BUF\_ITEM\_DECLARE(name, BIT(pow))

152

[ 161](group__ring__buffer__apis.md#ga60451a56ed9b742abfa8e75ca320b004)#define RING\_BUF\_ITEM\_SIZEOF(expr) DIV\_ROUND\_UP(sizeof(expr), sizeof(uint32\_t))

162

[ 173](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)static inline void [ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)(struct [ring\_buf](structring__buf.md) \*buf,

174 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

175 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

176{

177 \_\_ASSERT(size <= RING\_BUFFER\_MAX\_SIZE, RING\_BUFFER\_SIZE\_ASSERT\_MSG);

178

179 buf->size = size;

180 buf->buffer = data;

181 ring\_buf\_internal\_reset(buf, 0);

182}

183

[ 197](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)static inline void [ring\_buf\_item\_init](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)(struct [ring\_buf](structring__buf.md) \*buf,

198 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

199 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data)

200{

201 \_\_ASSERT(size <= RING\_BUFFER\_MAX\_SIZE / 4, RING\_BUFFER\_SIZE\_ASSERT\_MSG);

202 [ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)(buf, 4 \* size, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)data);

203}

204

[ 212](group__ring__buffer__apis.md#gac1a8c9e4cc9c3485573082371a4d9574)static inline bool [ring\_buf\_is\_empty](group__ring__buffer__apis.md#gac1a8c9e4cc9c3485573082371a4d9574)(const struct [ring\_buf](structring__buf.md) \*buf)

213{

214 return buf->get.head == buf->put.tail;

215}

216

[ 222](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)static inline void [ring\_buf\_reset](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)(struct [ring\_buf](structring__buf.md) \*buf)

223{

224 ring\_buf\_internal\_reset(buf, 0);

225}

226

[ 234](group__ring__buffer__apis.md#ga5eee438bd5bf08eb3a2da4cf2289903c)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga5eee438bd5bf08eb3a2da4cf2289903c)(const struct [ring\_buf](structring__buf.md) \*buf)

235{

236 ring\_buf\_idx\_t allocated = buf->put.head - buf->get.tail;

237

238 return buf->size - allocated;

239}

240

[ 248](group__ring__buffer__apis.md#ga39c203f8e599098ce0d308e88d07d084)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_item\_space\_get](group__ring__buffer__apis.md#ga39c203f8e599098ce0d308e88d07d084)(const struct [ring\_buf](structring__buf.md) \*buf)

249{

250 return [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga5eee438bd5bf08eb3a2da4cf2289903c)(buf) / 4;

251}

252

[ 260](group__ring__buffer__apis.md#ga9589ff6b763eeafacb65a3af283db3cd)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_capacity\_get](group__ring__buffer__apis.md#ga9589ff6b763eeafacb65a3af283db3cd)(const struct [ring\_buf](structring__buf.md) \*buf)

261{

262 return buf->size;

263}

264

[ 272](group__ring__buffer__apis.md#ga5f0017eb22d84b9cb177adfe090e6a92)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_size\_get](group__ring__buffer__apis.md#ga5f0017eb22d84b9cb177adfe090e6a92)(const struct [ring\_buf](structring__buf.md) \*buf)

273{

274 ring\_buf\_idx\_t available = buf->put.tail - buf->get.head;

275

276 return available;

277}

278

[ 303](group__ring__buffer__apis.md#ga0381d9c6413d78b9226d32532ef523eb)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_put\_claim](group__ring__buffer__apis.md#ga0381d9c6413d78b9226d32532ef523eb)(struct [ring\_buf](structring__buf.md) \*buf,

304 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data,

305 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

306{

307 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) space = [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga5eee438bd5bf08eb3a2da4cf2289903c)(buf);

308 return ring\_buf\_area\_claim(buf, &buf->put, data,

309 [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(size, space));

310}

311

[ 334](group__ring__buffer__apis.md#gaf910aa666eac329813a55db732a21bd8)static inline int [ring\_buf\_put\_finish](group__ring__buffer__apis.md#gaf910aa666eac329813a55db732a21bd8)(struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

335{

336 return ring\_buf\_area\_finish(buf, &buf->put, size);

337}

338

[ 359](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_put](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)(struct [ring\_buf](structring__buf.md) \*buf, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

360

[ 385](group__ring__buffer__apis.md#gad7cd6e1fe8e47ab7f6d9c42b87581f19)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_get\_claim](group__ring__buffer__apis.md#gad7cd6e1fe8e47ab7f6d9c42b87581f19)(struct [ring\_buf](structring__buf.md) \*buf,

386 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data,

387 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

388{

389 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buf\_size = [ring\_buf\_size\_get](group__ring__buffer__apis.md#ga5f0017eb22d84b9cb177adfe090e6a92)(buf);

390 return ring\_buf\_area\_claim(buf, &buf->get, data,

391 [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(size, buf\_size));

392}

393

[ 416](group__ring__buffer__apis.md#ga8ea8ad9949bffd0d6f9b0785e18a6378)static inline int [ring\_buf\_get\_finish](group__ring__buffer__apis.md#ga8ea8ad9949bffd0d6f9b0785e18a6378)(struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

417{

418 return ring\_buf\_area\_finish(buf, &buf->get, size);

419}

420

[ 441](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_get](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)(struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

442

[ 469](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_peek](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1)(struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

470

[ 492](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599)int [ring\_buf\_item\_put](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599)(struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value,

493 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size32);

494

[ 519](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)int [ring\_buf\_item\_get](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)(struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value,

520 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*size32);

521

525

526#ifdef \_\_cplusplus

527}

528#endif

529

530#endif /\* ZEPHYR\_INCLUDE\_SYS\_RING\_BUFFER\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[ring\_buf\_put\_claim](group__ring__buffer__apis.md#ga0381d9c6413d78b9226d32532ef523eb)

static uint32\_t ring\_buf\_put\_claim(struct ring\_buf \*buf, uint8\_t \*\*data, uint32\_t size)

Allocate buffer for writing data to a ring buffer.

**Definition** ring\_buffer.h:303

[ring\_buf\_get](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)

uint32\_t ring\_buf\_get(struct ring\_buf \*buf, uint8\_t \*data, uint32\_t size)

Read data from a ring buffer.

[ring\_buf\_item\_space\_get](group__ring__buffer__apis.md#ga39c203f8e599098ce0d308e88d07d084)

static uint32\_t ring\_buf\_item\_space\_get(const struct ring\_buf \*buf)

Determine free space in an "item based" ring buffer.

**Definition** ring\_buffer.h:248

[ring\_buf\_space\_get](group__ring__buffer__apis.md#ga5eee438bd5bf08eb3a2da4cf2289903c)

static uint32\_t ring\_buf\_space\_get(const struct ring\_buf \*buf)

Determine free space in a ring buffer.

**Definition** ring\_buffer.h:234

[ring\_buf\_size\_get](group__ring__buffer__apis.md#ga5f0017eb22d84b9cb177adfe090e6a92)

static uint32\_t ring\_buf\_size\_get(const struct ring\_buf \*buf)

Determine size of available data in a ring buffer.

**Definition** ring\_buffer.h:272

[ring\_buf\_put](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)

uint32\_t ring\_buf\_put(struct ring\_buf \*buf, const uint8\_t \*data, uint32\_t size)

Write (copy) data to a ring buffer.

[ring\_buf\_item\_put](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599)

int ring\_buf\_item\_put(struct ring\_buf \*buf, uint16\_t type, uint8\_t value, uint32\_t \*data, uint8\_t size32)

Write a data item to a ring buffer.

[ring\_buf\_peek](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1)

uint32\_t ring\_buf\_peek(struct ring\_buf \*buf, uint8\_t \*data, uint32\_t size)

Peek at data from a ring buffer.

[ring\_buf\_get\_finish](group__ring__buffer__apis.md#ga8ea8ad9949bffd0d6f9b0785e18a6378)

static int ring\_buf\_get\_finish(struct ring\_buf \*buf, uint32\_t size)

Indicate number of bytes read from claimed buffer.

**Definition** ring\_buffer.h:416

[ring\_buf\_capacity\_get](group__ring__buffer__apis.md#ga9589ff6b763eeafacb65a3af283db3cd)

static uint32\_t ring\_buf\_capacity\_get(const struct ring\_buf \*buf)

Return ring buffer capacity.

**Definition** ring\_buffer.h:260

[ring\_buf\_reset](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)

static void ring\_buf\_reset(struct ring\_buf \*buf)

Reset ring buffer state.

**Definition** ring\_buffer.h:222

[ring\_buf\_item\_init](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)

static void ring\_buf\_item\_init(struct ring\_buf \*buf, uint32\_t size, uint32\_t \*data)

Initialize an "item based" ring buffer.

**Definition** ring\_buffer.h:197

[ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)

static void ring\_buf\_init(struct ring\_buf \*buf, uint32\_t size, uint8\_t \*data)

Initialize a ring buffer for byte data.

**Definition** ring\_buffer.h:173

[ring\_buf\_is\_empty](group__ring__buffer__apis.md#gac1a8c9e4cc9c3485573082371a4d9574)

static bool ring\_buf\_is\_empty(const struct ring\_buf \*buf)

Determine if a ring buffer is empty.

**Definition** ring\_buffer.h:212

[ring\_buf\_get\_claim](group__ring__buffer__apis.md#gad7cd6e1fe8e47ab7f6d9c42b87581f19)

static uint32\_t ring\_buf\_get\_claim(struct ring\_buf \*buf, uint8\_t \*\*data, uint32\_t size)

Get address of a valid data in a ring buffer.

**Definition** ring\_buffer.h:385

[ring\_buf\_item\_get](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)

int ring\_buf\_item\_get(struct ring\_buf \*buf, uint16\_t \*type, uint8\_t \*value, uint32\_t \*data, uint8\_t \*size32)

Read a data item from a ring buffer.

[ring\_buf\_put\_finish](group__ring__buffer__apis.md#gaf910aa666eac329813a55db732a21bd8)

static int ring\_buf\_put\_finish(struct ring\_buf \*buf, uint32\_t size)

Indicate number of bytes written to allocated buffers.

**Definition** ring\_buffer.h:334

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)

#define MIN(a, b)

Obtain the minimum of two values.

**Definition** util.h:402

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:49

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [ring\_buffer.h](ring__buffer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
