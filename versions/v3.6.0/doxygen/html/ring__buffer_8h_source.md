---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ring__buffer_8h_source.html
original_path: doxygen/html/ring__buffer_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

10#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

11#include <[zephyr/sys/util.h](util_8h.md)>

12#include <[errno.h](errno_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

19/\* The limit is used by algorithm for distinguishing between empty and full

20 \* state.

21 \*/

22#define RING\_BUFFER\_MAX\_SIZE 0x80000000U

23

24#define RING\_BUFFER\_SIZE\_ASSERT\_MSG \

25 "Size too big"

27

37

[ 41](structring__buf.md)struct [ring\_buf](structring__buf.md) {

43 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer;

44 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) put\_head;

45 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) put\_tail;

46 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) put\_base;

47 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) get\_head;

48 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) get\_tail;

49 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) get\_base;

50 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size;

52};

53

[ 59](group__ring__buffer__apis.md#ga1f746bff362119621081694aaa190add)static inline void [ring\_buf\_internal\_reset](group__ring__buffer__apis.md#ga1f746bff362119621081694aaa190add)(struct [ring\_buf](structring__buf.md) \*buf, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) value)

60{

61 buf->put\_head = buf->put\_tail = buf->put\_base = value;

62 buf->get\_head = buf->get\_tail = buf->get\_base = value;

63}

64

[ 79](group__ring__buffer__apis.md#ga803e45abf48ee207fc0ab4028726a82b)#define RING\_BUF\_DECLARE(name, size8) \

80 BUILD\_ASSERT(size8 < RING\_BUFFER\_MAX\_SIZE,\

81 RING\_BUFFER\_SIZE\_ASSERT\_MSG); \

82 static uint8\_t \_\_noinit \_ring\_buffer\_data\_##name[size8]; \

83 struct ring\_buf name = { \

84 .buffer = \_ring\_buffer\_data\_##name, \

85 .size = size8 \

86 }

87

[ 103](group__ring__buffer__apis.md#ga2fc2f4515121ac6bbf6aebf3e029bb5d)#define RING\_BUF\_ITEM\_DECLARE(name, size32) \

104 BUILD\_ASSERT((size32) < RING\_BUFFER\_MAX\_SIZE / 4,\

105 RING\_BUFFER\_SIZE\_ASSERT\_MSG); \

106 static uint32\_t \_\_noinit \_ring\_buffer\_data\_##name[size32]; \

107 struct ring\_buf name = { \

108 .buffer = (uint8\_t \*) \_ring\_buffer\_data\_##name, \

109 .size = 4 \* (size32) \

110 }

111

[ 121](group__ring__buffer__apis.md#ga205e93b5431112da0d191526906c7e01)#define RING\_BUF\_ITEM\_DECLARE\_SIZE(name, size32) \

122 RING\_BUF\_ITEM\_DECLARE(name, size32)

123

[ 134](group__ring__buffer__apis.md#gaca98f407b222dff12e2bbfcf3746a9e3)#define RING\_BUF\_ITEM\_DECLARE\_POW2(name, pow) \

135 RING\_BUF\_ITEM\_DECLARE(name, BIT(pow))

136

[ 145](group__ring__buffer__apis.md#ga60451a56ed9b742abfa8e75ca320b004)#define RING\_BUF\_ITEM\_SIZEOF(expr) DIV\_ROUND\_UP(sizeof(expr), sizeof(uint32\_t))

146

[ 157](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)static inline void [ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)(struct [ring\_buf](structring__buf.md) \*buf,

158 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

159 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data)

160{

161 \_\_ASSERT(size < RING\_BUFFER\_MAX\_SIZE, RING\_BUFFER\_SIZE\_ASSERT\_MSG);

162

163 buf->size = size;

164 buf->buffer = data;

165 [ring\_buf\_internal\_reset](group__ring__buffer__apis.md#ga1f746bff362119621081694aaa190add)(buf, 0);

166}

167

[ 184](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)static inline void [ring\_buf\_item\_init](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)(struct [ring\_buf](structring__buf.md) \*buf,

185 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

186 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data)

187{

188 \_\_ASSERT(size < RING\_BUFFER\_MAX\_SIZE / 4, RING\_BUFFER\_SIZE\_ASSERT\_MSG);

189 [ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)(buf, 4 \* size, ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)data);

190}

191

[ 199](group__ring__buffer__apis.md#gabb7006d786b1ddc640b5fd2338d1d01c)static inline bool [ring\_buf\_is\_empty](group__ring__buffer__apis.md#gabb7006d786b1ddc640b5fd2338d1d01c)(struct [ring\_buf](structring__buf.md) \*buf)

200{

201 return buf->get\_head == buf->put\_tail;

202}

203

[ 209](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)static inline void [ring\_buf\_reset](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)(struct [ring\_buf](structring__buf.md) \*buf)

210{

211 [ring\_buf\_internal\_reset](group__ring__buffer__apis.md#ga1f746bff362119621081694aaa190add)(buf, 0);

212}

213

[ 221](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)(struct [ring\_buf](structring__buf.md) \*buf)

222{

223 return buf->size - (buf->put\_head - buf->get\_tail);

224}

225

[ 233](group__ring__buffer__apis.md#gab58be76e8d3fc5542fb7b03717b89544)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_item\_space\_get](group__ring__buffer__apis.md#gab58be76e8d3fc5542fb7b03717b89544)(struct [ring\_buf](structring__buf.md) \*buf)

234{

235 return [ring\_buf\_space\_get](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)(buf) / 4;

236}

237

[ 245](group__ring__buffer__apis.md#ga9c06a3c6f77584ce8317a236cc2de35c)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_capacity\_get](group__ring__buffer__apis.md#ga9c06a3c6f77584ce8317a236cc2de35c)(struct [ring\_buf](structring__buf.md) \*buf)

246{

247 return buf->size;

248}

249

[ 257](group__ring__buffer__apis.md#gade647873dd72c04a54f51b8d9d335107)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_size\_get](group__ring__buffer__apis.md#gade647873dd72c04a54f51b8d9d335107)(struct [ring\_buf](structring__buf.md) \*buf)

258{

259 return buf->put\_tail - buf->get\_head;

260}

261

[ 286](group__ring__buffer__apis.md#gae15934b40fd208a63eba98b2382e8ad1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_put\_claim](group__ring__buffer__apis.md#gae15934b40fd208a63eba98b2382e8ad1)(struct [ring\_buf](structring__buf.md) \*buf,

287 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data,

288 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

289

[ 312](group__ring__buffer__apis.md#ga465feaf6cf5312e75060ecf65db963ad)int [ring\_buf\_put\_finish](group__ring__buffer__apis.md#ga465feaf6cf5312e75060ecf65db963ad)(struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

313

[ 334](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_put](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)(struct [ring\_buf](structring__buf.md) \*buf, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

335

[ 360](group__ring__buffer__apis.md#ga7ab4fea7b19b1ffa58a7d3a581396b1c)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_get\_claim](group__ring__buffer__apis.md#ga7ab4fea7b19b1ffa58a7d3a581396b1c)(struct [ring\_buf](structring__buf.md) \*buf,

361 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data,

362 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

363

[ 386](group__ring__buffer__apis.md#ga36177459f4e352b52a6f2046a33c3aa1)int [ring\_buf\_get\_finish](group__ring__buffer__apis.md#ga36177459f4e352b52a6f2046a33c3aa1)(struct [ring\_buf](structring__buf.md) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

387

[ 408](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_get](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)(struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

409

[ 436](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ring\_buf\_peek](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1)(struct [ring\_buf](structring__buf.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

437

[ 459](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599)int [ring\_buf\_item\_put](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599)(struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value,

460 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size32);

461

[ 486](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)int [ring\_buf\_item\_get](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)(struct [ring\_buf](structring__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value,

487 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*size32);

488

492

493#ifdef \_\_cplusplus

494}

495#endif

496

497#endif /\* ZEPHYR\_INCLUDE\_SYS\_RING\_BUFFER\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[ring\_buf\_space\_get](group__ring__buffer__apis.md#ga0db0b939d2be3d3fb0688f55780379bb)

static uint32\_t ring\_buf\_space\_get(struct ring\_buf \*buf)

Determine free space in a ring buffer.

**Definition** ring\_buffer.h:221

[ring\_buf\_internal\_reset](group__ring__buffer__apis.md#ga1f746bff362119621081694aaa190add)

static void ring\_buf\_internal\_reset(struct ring\_buf \*buf, int32\_t value)

Function to force ring\_buf internal states to given value.

**Definition** ring\_buffer.h:59

[ring\_buf\_get](group__ring__buffer__apis.md#ga209bef22c47f3938a36d7eb6c3b3dbc7)

uint32\_t ring\_buf\_get(struct ring\_buf \*buf, uint8\_t \*data, uint32\_t size)

Read data from a ring buffer.

[ring\_buf\_get\_finish](group__ring__buffer__apis.md#ga36177459f4e352b52a6f2046a33c3aa1)

int ring\_buf\_get\_finish(struct ring\_buf \*buf, uint32\_t size)

Indicate number of bytes read from claimed buffer.

[ring\_buf\_put\_finish](group__ring__buffer__apis.md#ga465feaf6cf5312e75060ecf65db963ad)

int ring\_buf\_put\_finish(struct ring\_buf \*buf, uint32\_t size)

Indicate number of bytes written to allocated buffers.

[ring\_buf\_put](group__ring__buffer__apis.md#ga6c7e76e3ca798e994f738d114cb9a7e3)

uint32\_t ring\_buf\_put(struct ring\_buf \*buf, const uint8\_t \*data, uint32\_t size)

Write (copy) data to a ring buffer.

[ring\_buf\_item\_put](group__ring__buffer__apis.md#ga6cb71d7c1a36b6e142b251f08ed40599)

int ring\_buf\_item\_put(struct ring\_buf \*buf, uint16\_t type, uint8\_t value, uint32\_t \*data, uint8\_t size32)

Write a data item to a ring buffer.

[ring\_buf\_get\_claim](group__ring__buffer__apis.md#ga7ab4fea7b19b1ffa58a7d3a581396b1c)

uint32\_t ring\_buf\_get\_claim(struct ring\_buf \*buf, uint8\_t \*\*data, uint32\_t size)

Get address of a valid data in a ring buffer.

[ring\_buf\_peek](group__ring__buffer__apis.md#ga8ba75a313b2ad7d55e390fa3f1fcadc1)

uint32\_t ring\_buf\_peek(struct ring\_buf \*buf, uint8\_t \*data, uint32\_t size)

Peek at data from a ring buffer.

[ring\_buf\_capacity\_get](group__ring__buffer__apis.md#ga9c06a3c6f77584ce8317a236cc2de35c)

static uint32\_t ring\_buf\_capacity\_get(struct ring\_buf \*buf)

Return ring buffer capacity.

**Definition** ring\_buffer.h:245

[ring\_buf\_reset](group__ring__buffer__apis.md#ga9cc0cd445eeeeba7183c3ac0778c7e18)

static void ring\_buf\_reset(struct ring\_buf \*buf)

Reset ring buffer state.

**Definition** ring\_buffer.h:209

[ring\_buf\_item\_init](group__ring__buffer__apis.md#ga9d10210160544af25c9a67680aff578d)

static void ring\_buf\_item\_init(struct ring\_buf \*buf, uint32\_t size, uint32\_t \*data)

Initialize an "item based" ring buffer.

**Definition** ring\_buffer.h:184

[ring\_buf\_item\_space\_get](group__ring__buffer__apis.md#gab58be76e8d3fc5542fb7b03717b89544)

static uint32\_t ring\_buf\_item\_space\_get(struct ring\_buf \*buf)

Determine free space in an "item based" ring buffer.

**Definition** ring\_buffer.h:233

[ring\_buf\_is\_empty](group__ring__buffer__apis.md#gabb7006d786b1ddc640b5fd2338d1d01c)

static bool ring\_buf\_is\_empty(struct ring\_buf \*buf)

Determine if a ring buffer is empty.

**Definition** ring\_buffer.h:199

[ring\_buf\_init](group__ring__buffer__apis.md#gac06bc272bf99843c65bf28d851bffd55)

static void ring\_buf\_init(struct ring\_buf \*buf, uint32\_t size, uint8\_t \*data)

Initialize a ring buffer for byte data.

**Definition** ring\_buffer.h:157

[ring\_buf\_size\_get](group__ring__buffer__apis.md#gade647873dd72c04a54f51b8d9d335107)

static uint32\_t ring\_buf\_size\_get(struct ring\_buf \*buf)

Determine used space in a ring buffer.

**Definition** ring\_buffer.h:257

[ring\_buf\_item\_get](group__ring__buffer__apis.md#gae0c62af11cab8a661638e50b312b58f8)

int ring\_buf\_item\_get(struct ring\_buf \*buf, uint16\_t \*type, uint8\_t \*value, uint32\_t \*data, uint8\_t \*size32)

Read a data item from a ring buffer.

[ring\_buf\_put\_claim](group__ring__buffer__apis.md#gae15934b40fd208a63eba98b2382e8ad1)

uint32\_t ring\_buf\_put\_claim(struct ring\_buf \*buf, uint8\_t \*\*data, uint32\_t size)

Allocate buffer for writing data to a ring buffer.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

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

**Definition** ring\_buffer.h:41

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [ring\_buffer.h](ring__buffer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
