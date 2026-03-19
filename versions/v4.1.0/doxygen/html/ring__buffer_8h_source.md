---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ring__buffer_8h_source.html
original_path: doxygen/html/ring__buffer_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

32#define RING\_BUFFER\_MAX\_SIZE 0x80000000U

33#define RING\_BUFFER\_SIZE\_ASSERT\_MSG \

34 "Size too big"

35

36struct ring\_buf\_index { [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) head, tail, base; };

37

39

[ 43](structring__buf.md)struct [ring\_buf](structring__buf.md) {

45 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer;

46 struct ring\_buf\_index put;

47 struct ring\_buf\_index get;

48 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size;

50};

51

53

54[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ring\_buf\_area\_claim(struct [ring\_buf](structring__buf.md) \*buf, struct ring\_buf\_index \*ring,

55 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

56int ring\_buf\_area\_finish(struct [ring\_buf](structring__buf.md) \*buf, struct ring\_buf\_index \*ring,

57 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

58

64static inline void ring\_buf\_internal\_reset(struct [ring\_buf](structring__buf.md) \*buf, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value)

65{

66 buf->put.head = buf->put.tail = buf->put.base = value;

67 buf->get.head = buf->get.tail = buf->get.base = value;

68}

69

71

[ 72](group__ring__buffer__apis.md#ga2ab4af6d5e79ed9ad8cfca22ec3a7107)#define RING\_BUF\_INIT(buf, size8) \

73{ \

74 .buffer = buf, \

75 .size = size8, \

76}

77

[ 92](group__ring__buffer__apis.md#ga803e45abf48ee207fc0ab4028726a82b)#define RING\_BUF\_DECLARE(name, size8) \

93 BUILD\_ASSERT(size8 < RING\_BUFFER\_MAX\_SIZE,\

94 RING\_BUFFER\_SIZE\_ASSERT\_MSG); \

95 static uint8\_t \_\_noinit \_ring\_buffer\_data\_##name[size8]; \

96 struct ring\_buf name = RING\_BUF\_INIT(\_ring\_buffer\_data\_##name, size8)

97

[ 113](group__ring__buffer__apis.md#ga2fc2f4515121ac6bbf6aebf3e029bb5d)#define RING\_BUF\_ITEM\_DECLARE(name, size32) \

114 BUILD\_ASSERT((size32) < RING\_BUFFER\_MAX\_SIZE / 4,\

115 RING\_BUFFER\_SIZE\_ASSERT\_MSG); \

116 static uint32\_t \_\_noinit \_ring\_buffer\_data\_##name[size32]; \

117 struct ring\_buf name = { \

118 .buffer = (uint8\_t \*) \_ring\_buffer\_data\_##name, \

119 .size = 4 \* (size32) \

120 }

121

[ 131](group__ring__buffer__apis.md#ga205e93b5431112da0d191526906c7e01)#define RING\_BUF\_ITEM\_DECLARE\_SIZE(name, size32) \

132 RING\_BUF\_ITEM\_DECLARE(name, size32)

133

[ 144](group__ring__buffer__apis.md#gaca98f407b222dff12e2bbfcf3746a9e3)#define RING\_BUF\_ITEM\_DECLARE\_POW2(name, pow) \

145 RING\_BUF\_ITEM\_DECLARE(name, BIT(pow))

146

[ 155](group__ring__buffer__apis.md#ga60451a56ed9b742abfa8e75ca320b004)#define RING\_BUF\_ITEM\_SIZEOF(expr) DIV\_ROUND\_UP(sizeof(expr), sizeof(uint32\_t))

156

[ 167](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)static inline void [ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)(struct [ring\_buf](structring__buf.md) \*buf,

168 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

169 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

170{

171 \_\_ASSERT(size < RING\_BUFFER\_MAX\_SIZE, RING\_BUFFER\_SIZE\_ASSERT\_MSG);

172

173 buf->size = size;

174 buf->buffer = data;

175 ring\_buf\_internal\_reset(buf, 0);

176}

177

[ 191](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)static inline void [ring\_buf\_item\_init](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)(struct [ring\_buf](structring__buf.md) \*buf,

192 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

193 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data)

194{

195 \_\_ASSERT(size < RING\_BUFFER\_MAX\_SIZE / 4, RING\_BUFFER\_SIZE\_ASSERT\_MSG);

196 [ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)(buf, 4 \* size, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)data);

197}

198

[ 206](group__ring__buffer__apis.md#gabb7006d786b1ddc640b5fd2338d1d01c)static inline bool [ring\_buf\_is\_empty](group__ring__buffer__apis.md#gabb7006d786b1ddc640b5fd2338d1d01c)(struct [ring\_buf](structring__buf.md) \*buf)

207{

208 return buf->get.head == buf->put.tail;

209}

210

[ 216](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)static inline void [ring\_buf\_reset](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)(struct [ring\_buf](structring__buf.md) \*buf)

217{

218 ring\_buf\_internal\_reset(buf, 0);

219}

220

[ 228](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)(struct [ring\_buf](structring__buf.md) \*buf)

229{

230 return buf->size - (buf->put.head - buf->get.tail);

231}

232

[ 240](group__ring__buffer__apis.md#gab58be76e8d3fc5542fb7b03717b89544)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_item\_space\_get](group__ring__buffer__apis.md#gab58be76e8d3fc5542fb7b03717b89544)(struct [ring\_buf](structring__buf.md) \*buf)

241{

242 return [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)(buf) / 4;

243}

244

[ 252](group__ring__buffer__apis.md#ga9c06a3c6f77584ce8317a236cc2de35c)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_capacity\_get](group__ring__buffer__apis.md#ga9c06a3c6f77584ce8317a236cc2de35c)(struct [ring\_buf](structring__buf.md) \*buf)

253{

254 return buf->size;

255}

256

[ 264](group__ring__buffer__apis.md#gade647873dd72c04a54f51b8d9d335107)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_size\_get](group__ring__buffer__apis.md#gade647873dd72c04a54f51b8d9d335107)(struct [ring\_buf](structring__buf.md) \*buf)

265{

266 return buf->put.tail - buf->get.head;

267}

268

[ 293](group__ring__buffer__apis.md#ga0381d9c6413d78b9226d32532ef523eb)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_put\_claim](group__ring__buffer__apis.md#ga0381d9c6413d78b9226d32532ef523eb)(struct [ring\_buf](structring__buf.md) \*buf,

294 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data,

295 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

296{

297 return ring\_buf\_area\_claim(buf, &buf->put, data,

298 [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(size, [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)(buf)));

299}

300

[ 323](group__ring__buffer__apis.md#gaf910aa666eac329813a55db732a21bd8)static inline int [ring\_buf\_put\_finish](group__ring__buffer__apis.md#gaf910aa666eac329813a55db732a21bd8)(struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

324{

325 return ring\_buf\_area\_finish(buf, &buf->put, size);

326}

327

[ 348](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_put](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)(struct [ring\_buf](structring__buf.md) \*buf, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

349

[ 374](group__ring__buffer__apis.md#gad7cd6e1fe8e47ab7f6d9c42b87581f19)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_get\_claim](group__ring__buffer__apis.md#gad7cd6e1fe8e47ab7f6d9c42b87581f19)(struct [ring\_buf](structring__buf.md) \*buf,

375 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data,

376 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

377{

378 return ring\_buf\_area\_claim(buf, &buf->get, data,

379 [MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)(size, [ring\_buf\_size\_get](group__ring__buffer__apis.md#gade647873dd72c04a54f51b8d9d335107)(buf)));

380}

381

[ 404](group__ring__buffer__apis.md#ga8ea8ad9949bffd0d6f9b0785e18a6378)static inline int [ring\_buf\_get\_finish](group__ring__buffer__apis.md#ga8ea8ad9949bffd0d6f9b0785e18a6378)(struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size)

405{

406 return ring\_buf\_area\_finish(buf, &buf->get, size);

407}

408

[ 429](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_get](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)(struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

430

[ 457](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_peek](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1)(struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

458

[ 480](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599)int [ring\_buf\_item\_put](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599)(struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value,

481 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size32);

482

[ 507](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)int [ring\_buf\_item\_get](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)(struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value,

508 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*size32);

509

513

514#ifdef \_\_cplusplus

515}

516#endif

517

518#endif /\* ZEPHYR\_INCLUDE\_SYS\_RING\_BUFFER\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[ring\_buf\_put\_claim](group__ring__buffer__apis.md#ga0381d9c6413d78b9226d32532ef523eb)

static uint32\_t ring\_buf\_put\_claim(struct ring\_buf \*buf, uint8\_t \*\*data, uint32\_t size)

Allocate buffer for writing data to a ring buffer.

**Definition** ring\_buffer.h:293

[ring\_buf\_space\_get](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)

static uint32\_t ring\_buf\_space\_get(struct ring\_buf \*buf)

Determine free space in a ring buffer.

**Definition** ring\_buffer.h:228

[ring\_buf\_get](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)

uint32\_t ring\_buf\_get(struct ring\_buf \*buf, uint8\_t \*data, uint32\_t size)

Read data from a ring buffer.

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

**Definition** ring\_buffer.h:404

[ring\_buf\_capacity\_get](group__ring__buffer__apis.md#ga9c06a3c6f77584ce8317a236cc2de35c)

static uint32\_t ring\_buf\_capacity\_get(struct ring\_buf \*buf)

Return ring buffer capacity.

**Definition** ring\_buffer.h:252

[ring\_buf\_reset](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)

static void ring\_buf\_reset(struct ring\_buf \*buf)

Reset ring buffer state.

**Definition** ring\_buffer.h:216

[ring\_buf\_item\_init](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)

static void ring\_buf\_item\_init(struct ring\_buf \*buf, uint32\_t size, uint32\_t \*data)

Initialize an "item based" ring buffer.

**Definition** ring\_buffer.h:191

[ring\_buf\_item\_space\_get](group__ring__buffer__apis.md#gab58be76e8d3fc5542fb7b03717b89544)

static uint32\_t ring\_buf\_item\_space\_get(struct ring\_buf \*buf)

Determine free space in an "item based" ring buffer.

**Definition** ring\_buffer.h:240

[ring\_buf\_is\_empty](group__ring__buffer__apis.md#gabb7006d786b1ddc640b5fd2338d1d01c)

static bool ring\_buf\_is\_empty(struct ring\_buf \*buf)

Determine if a ring buffer is empty.

**Definition** ring\_buffer.h:206

[ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)

static void ring\_buf\_init(struct ring\_buf \*buf, uint32\_t size, uint8\_t \*data)

Initialize a ring buffer for byte data.

**Definition** ring\_buffer.h:167

[ring\_buf\_get\_claim](group__ring__buffer__apis.md#gad7cd6e1fe8e47ab7f6d9c42b87581f19)

static uint32\_t ring\_buf\_get\_claim(struct ring\_buf \*buf, uint8\_t \*\*data, uint32\_t size)

Get address of a valid data in a ring buffer.

**Definition** ring\_buffer.h:374

[ring\_buf\_size\_get](group__ring__buffer__apis.md#gade647873dd72c04a54f51b8d9d335107)

static uint32\_t ring\_buf\_size\_get(struct ring\_buf \*buf)

Determine used space in a ring buffer.

**Definition** ring\_buffer.h:264

[ring\_buf\_item\_get](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)

int ring\_buf\_item\_get(struct ring\_buf \*buf, uint16\_t \*type, uint8\_t \*value, uint32\_t \*data, uint8\_t \*size32)

Read a data item from a ring buffer.

[ring\_buf\_put\_finish](group__ring__buffer__apis.md#gaf910aa666eac329813a55db732a21bd8)

static int ring\_buf\_put\_finish(struct ring\_buf \*buf, uint32\_t size)

Indicate number of bytes written to allocated buffers.

**Definition** ring\_buffer.h:323

[MIN](group__sys-util.md#ga3acffbd305ee72dcd4593c0d8af64a4f)

#define MIN(a, b)

Obtain the minimum of two values.

**Definition** util.h:401

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:43

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [ring\_buffer.h](ring__buffer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
