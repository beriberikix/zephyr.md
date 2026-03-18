---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pbuf_8h_source.html
original_path: doxygen/html/pbuf_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pbuf.h

[Go to the documentation of this file.](pbuf_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_IPC\_PBUF\_H\_

8#define ZEPHYR\_INCLUDE\_IPC\_PBUF\_H\_

9

10#include <[zephyr/cache.h](cache_8h.md)>

11#include <[zephyr/devicetree.h](devicetree_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

23

[ 25](group__pbuf.md#gaa57dc50fdf97af6690ac784f0a4450be)#define PBUF\_PACKET\_LEN\_SZ sizeof(uint32\_t)

26

27/\* Amount of data that is left unused to distinguish between empty and full. \*/

28#define \_PBUF\_IDX\_SIZE sizeof(uint32\_t)

29

30/\* Minimal length of the data field in the buffer to store the smalest packet

31 \* possible.

32 \* (+1) for at least one byte of data.

33 \* (+\_PBUF\_IDX\_SIZE) to distinguish buffer full and buffer empty.

34 \* Rounded up to keep wr/rd indexes pointing to aligned address.

35 \*/

36#define \_PBUF\_MIN\_DATA\_LEN ROUND\_UP(PBUF\_PACKET\_LEN\_SZ + 1 + \_PBUF\_IDX\_SIZE, \_PBUF\_IDX\_SIZE)

37

[ 42](structpbuf__cfg.md)struct [pbuf\_cfg](structpbuf__cfg.md) {

[ 43](structpbuf__cfg.md#aaec17609d27ad086678dafab940e2ae1) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[rd\_idx\_loc](structpbuf__cfg.md#aaec17609d27ad086678dafab940e2ae1); /\* Address of the variable holding

44 \* index value of the first valid byte

45 \* in data[].

46 \*/

[ 47](structpbuf__cfg.md#afb7da887c911f2530cd9168b0a00b3b6) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[wr\_idx\_loc](structpbuf__cfg.md#afb7da887c911f2530cd9168b0a00b3b6); /\* Address of the variable holding

48 \* index value of the first free byte

49 \* in data[].

50 \*/

[ 51](structpbuf__cfg.md#a8e6a0f423a4c2cab92b515246483e8b0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dcache\_alignment](structpbuf__cfg.md#a8e6a0f423a4c2cab92b515246483e8b0); /\* CPU data cache line size in bytes.

52 \* Used for validation - TODO: To be

53 \* replaced by flags.

54 \*/

[ 55](structpbuf__cfg.md#aad5a0bc4bdef7cec0496e15d75d131dc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structpbuf__cfg.md#aad5a0bc4bdef7cec0496e15d75d131dc); /\* Length of data[] in bytes. \*/

[ 56](structpbuf__cfg.md#a427cea0b6f83a0411ed251c0fa9cdad5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_loc](structpbuf__cfg.md#a427cea0b6f83a0411ed251c0fa9cdad5); /\* Location of the data[]. \*/

57};

58

[ 65](structpbuf__data.md)struct [pbuf\_data](structpbuf__data.md) {

[ 66](structpbuf__data.md#ae5d497c293f1b84e7a8e801c5349a0b9) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wr\_idx](structpbuf__data.md#ae5d497c293f1b84e7a8e801c5349a0b9); /\* Index of the first holding first

67 \* free byte in data[]. Used for

68 \* writing.

69 \*/

[ 70](structpbuf__data.md#aecb4e2462b1d308d43883b935e4648fe) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rd\_idx](structpbuf__data.md#aecb4e2462b1d308d43883b935e4648fe); /\* Index of the first holding first

71 \* valid byte in data[]. Used for

72 \* reading.

73 \*/

74};

75

76

[ 89](structpbuf.md)struct [pbuf](structpbuf.md) {

[ 90](structpbuf.md#aa69c940d23b73b1292f5e8a6e1537494) const struct [pbuf\_cfg](structpbuf__cfg.md) \*const [cfg](structpbuf.md#aa69c940d23b73b1292f5e8a6e1537494); /\* Configuration of the

91 \* buffer.

92 \*/

[ 93](structpbuf.md#acbfdc9861d79dcd26bc73bfef5835e7e) struct [pbuf\_data](structpbuf__data.md) [data](structpbuf.md#acbfdc9861d79dcd26bc73bfef5835e7e); /\* Data used to read and write

94 \* to the buffer

95 \*/

96};

97

[ 108](group__pbuf.md#gafc65e8f044930fbd51dd6178302d75e1)#define PBUF\_CFG\_INIT(mem\_addr, size, dcache\_align) \

109{ \

110 .rd\_idx\_loc = (uint32\_t \*)(mem\_addr), \

111 .wr\_idx\_loc = (uint32\_t \*)((uint8\_t \*)(mem\_addr) + \

112 MAX(dcache\_align, \_PBUF\_IDX\_SIZE)), \

113 .data\_loc = (uint8\_t \*)((uint8\_t \*)(mem\_addr) + \

114 MAX(dcache\_align, \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE), \

115 .len = (uint32\_t)((uint32\_t)(size) - MAX(dcache\_align, \_PBUF\_IDX\_SIZE) - \

116 \_PBUF\_IDX\_SIZE), \

117 .dcache\_alignment = (dcache\_align), \

118}

119

[ 127](group__pbuf.md#ga00f201bb5e2e139272b2c32f9c3f6efc)#define PBUF\_HEADER\_OVERHEAD(dcache\_align) \

128 (MAX(dcache\_align, \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE)

129

[ 138](group__pbuf.md#gafc988125a3c06d0ecdc948cab3a3d23a)#define PBUF\_DEFINE(name, mem\_addr, size, dcache\_align) \

139 BUILD\_ASSERT(dcache\_align >= 0, \

140 "Cache line size must be non negative."); \

141 BUILD\_ASSERT((size) > 0 && IS\_PTR\_ALIGNED\_BYTES(size, \_PBUF\_IDX\_SIZE), \

142 "Incorrect size."); \

143 BUILD\_ASSERT(IS\_PTR\_ALIGNED\_BYTES(mem\_addr, MAX(dcache\_align, \_PBUF\_IDX\_SIZE)), \

144 "Misaligned memory."); \

145 BUILD\_ASSERT(size >= (MAX(dcache\_align, \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE + \

146 \_PBUF\_MIN\_DATA\_LEN), "Insufficient size."); \

147 \

148 static const struct pbuf\_cfg cfg\_##name = \

149 PBUF\_CFG\_INIT(mem\_addr, size, dcache\_align); \

150 static struct pbuf name = { \

151 .cfg = &cfg\_##name, \

152 }

153

[ 168](group__pbuf.md#ga651cf4ad3dc69e5dc1a0cea9f06a084e)int [pbuf\_init](group__pbuf.md#ga651cf4ad3dc69e5dc1a0cea9f06a084e)(struct [pbuf](structpbuf.md) \*pb);

169

183

[ 184](group__pbuf.md#ga9df9413dcd6268690a410c33126c081e)int [pbuf\_write](group__pbuf.md#ga9df9413dcd6268690a410c33126c081e)(struct [pbuf](structpbuf.md) \*pb, const char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

185

[ 202](group__pbuf.md#ga44cc22d33d4ec7b7c95459e96ef7d7d0)int [pbuf\_read](group__pbuf.md#ga44cc22d33d4ec7b7c95459e96ef7d7d0)(struct [pbuf](structpbuf.md) \*pb, char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

203

207

208#ifdef \_\_cplusplus

209}

210#endif

211

212#endif /\* ZEPHYR\_INCLUDE\_IPC\_PBUF\_H\_ \*/

[cache.h](cache_8h.md)

cache API interface

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[pbuf\_read](group__pbuf.md#ga44cc22d33d4ec7b7c95459e96ef7d7d0)

int pbuf\_read(struct pbuf \*pb, char \*buf, uint16\_t len)

Read specified amount of data from the packet buffer.

[pbuf\_init](group__pbuf.md#ga651cf4ad3dc69e5dc1a0cea9f06a084e)

int pbuf\_init(struct pbuf \*pb)

Initialize the packet buffer.

[pbuf\_write](group__pbuf.md#ga9df9413dcd6268690a410c33126c081e)

int pbuf\_write(struct pbuf \*pb, const char \*buf, uint16\_t len)

Write specified amount of data to the packet buffer.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[pbuf\_cfg](structpbuf__cfg.md)

Control block of packet buffer.

**Definition** pbuf.h:42

[pbuf\_cfg::data\_loc](structpbuf__cfg.md#a427cea0b6f83a0411ed251c0fa9cdad5)

uint8\_t \* data\_loc

**Definition** pbuf.h:56

[pbuf\_cfg::dcache\_alignment](structpbuf__cfg.md#a8e6a0f423a4c2cab92b515246483e8b0)

uint32\_t dcache\_alignment

**Definition** pbuf.h:51

[pbuf\_cfg::len](structpbuf__cfg.md#aad5a0bc4bdef7cec0496e15d75d131dc)

uint32\_t len

**Definition** pbuf.h:55

[pbuf\_cfg::rd\_idx\_loc](structpbuf__cfg.md#aaec17609d27ad086678dafab940e2ae1)

volatile uint32\_t \* rd\_idx\_loc

**Definition** pbuf.h:43

[pbuf\_cfg::wr\_idx\_loc](structpbuf__cfg.md#afb7da887c911f2530cd9168b0a00b3b6)

volatile uint32\_t \* wr\_idx\_loc

**Definition** pbuf.h:47

[pbuf\_data](structpbuf__data.md)

Data block of the packed buffer.

**Definition** pbuf.h:65

[pbuf\_data::wr\_idx](structpbuf__data.md#ae5d497c293f1b84e7a8e801c5349a0b9)

volatile uint32\_t wr\_idx

**Definition** pbuf.h:66

[pbuf\_data::rd\_idx](structpbuf__data.md#aecb4e2462b1d308d43883b935e4648fe)

volatile uint32\_t rd\_idx

**Definition** pbuf.h:70

[pbuf](structpbuf.md)

Scure packed buffer.

**Definition** pbuf.h:89

[pbuf::cfg](structpbuf.md#aa69c940d23b73b1292f5e8a6e1537494)

const struct pbuf\_cfg \*const cfg

**Definition** pbuf.h:90

[pbuf::data](structpbuf.md#acbfdc9861d79dcd26bc73bfef5835e7e)

struct pbuf\_data data

**Definition** pbuf.h:93

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [pbuf.h](pbuf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
