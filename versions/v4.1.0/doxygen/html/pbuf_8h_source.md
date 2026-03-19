---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pbuf_8h_source.html
original_path: doxygen/html/pbuf_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

38#if defined(CONFIG\_ARCH\_POSIX)

39/\* For the native simulated boards we need to modify some pointers at init \*/

40#define PBUF\_MAYBE\_CONST

41#else

[ 42](group__pbuf.md#gaba4cc55b02db047bc2e0ca5c873b1222)#define PBUF\_MAYBE\_CONST const

43#endif

44

[ 49](structpbuf__cfg.md)struct [pbuf\_cfg](structpbuf__cfg.md) {

[ 50](structpbuf__cfg.md#aaec17609d27ad086678dafab940e2ae1) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[rd\_idx\_loc](structpbuf__cfg.md#aaec17609d27ad086678dafab940e2ae1); /\* Address of the variable holding

51 \* index value of the first valid byte

52 \* in data[].

53 \*/

[ 54](structpbuf__cfg.md#a8be1cfcfeba47d8b4dd6ee1fa5bf4400) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[handshake\_loc](structpbuf__cfg.md#a8be1cfcfeba47d8b4dd6ee1fa5bf4400);/\* Address of the variable holding

55 \* handshake information.

56 \*/

[ 57](structpbuf__cfg.md#afb7da887c911f2530cd9168b0a00b3b6) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[wr\_idx\_loc](structpbuf__cfg.md#afb7da887c911f2530cd9168b0a00b3b6); /\* Address of the variable holding

58 \* index value of the first free byte

59 \* in data[].

60 \*/

[ 61](structpbuf__cfg.md#a8e6a0f423a4c2cab92b515246483e8b0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dcache\_alignment](structpbuf__cfg.md#a8e6a0f423a4c2cab92b515246483e8b0); /\* CPU data cache line size in bytes.

62 \* Used for validation - TODO: To be

63 \* replaced by flags.

64 \*/

[ 65](structpbuf__cfg.md#aad5a0bc4bdef7cec0496e15d75d131dc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structpbuf__cfg.md#aad5a0bc4bdef7cec0496e15d75d131dc); /\* Length of data[] in bytes. \*/

[ 66](structpbuf__cfg.md#a427cea0b6f83a0411ed251c0fa9cdad5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data\_loc](structpbuf__cfg.md#a427cea0b6f83a0411ed251c0fa9cdad5); /\* Location of the data[]. \*/

67};

68

[ 75](structpbuf__data.md)struct [pbuf\_data](structpbuf__data.md) {

[ 76](structpbuf__data.md#ae5d497c293f1b84e7a8e801c5349a0b9) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wr\_idx](structpbuf__data.md#ae5d497c293f1b84e7a8e801c5349a0b9); /\* Index of the first holding first

77 \* free byte in data[]. Used for

78 \* writing.

79 \*/

[ 80](structpbuf__data.md#aecb4e2462b1d308d43883b935e4648fe) volatile [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rd\_idx](structpbuf__data.md#aecb4e2462b1d308d43883b935e4648fe); /\* Index of the first holding first

81 \* valid byte in data[]. Used for

82 \* reading.

83 \*/

84};

85

86

[ 99](structpbuf.md)struct [pbuf](structpbuf.md) {

[ 100](structpbuf.md#aa69c940d23b73b1292f5e8a6e1537494) [PBUF\_MAYBE\_CONST](group__pbuf.md#gaba4cc55b02db047bc2e0ca5c873b1222) struct [pbuf\_cfg](structpbuf__cfg.md) \*const [cfg](structpbuf.md#aa69c940d23b73b1292f5e8a6e1537494); /\* Configuration of the

101 \* buffer.

102 \*/

[ 103](structpbuf.md#acbfdc9861d79dcd26bc73bfef5835e7e) struct [pbuf\_data](structpbuf__data.md) [data](structpbuf.md#acbfdc9861d79dcd26bc73bfef5835e7e); /\* Data used to read and write

104 \* to the buffer

105 \*/

106};

107

[ 120](group__pbuf.md#ga4e33dce801e591c9f319cc5682748920)#define PBUF\_CFG\_INIT(mem\_addr, size, dcache\_align, use\_handshake) \

121{ \

122 .rd\_idx\_loc = (uint32\_t \*)(mem\_addr), \

123 .handshake\_loc = use\_handshake ? (uint32\_t \*)((uint8\_t \*)(mem\_addr) + \

124 \_PBUF\_IDX\_SIZE) : NULL, \

125 .wr\_idx\_loc = (uint32\_t \*)((uint8\_t \*)(mem\_addr) + MAX(dcache\_align, \

126 (use\_handshake ? 2 : 1) \* \_PBUF\_IDX\_SIZE)), \

127 .data\_loc = (uint8\_t \*)((uint8\_t \*)(mem\_addr) + \

128 MAX(dcache\_align, (use\_handshake ? 2 : 1) \* \

129 \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE), \

130 .len = (uint32\_t)((uint32\_t)(size) - MAX(dcache\_align, \

131 (use\_handshake ? 2 : 1) \* \_PBUF\_IDX\_SIZE) - \_PBUF\_IDX\_SIZE), \

132 .dcache\_alignment = (dcache\_align), \

133}

134

[ 142](group__pbuf.md#ga00f201bb5e2e139272b2c32f9c3f6efc)#define PBUF\_HEADER\_OVERHEAD(dcache\_align) \

143 (MAX(dcache\_align, \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE)

144

[ 155](group__pbuf.md#gad167c69e7892f79060b07c6269699ae9)#define PBUF\_DEFINE(name, mem\_addr, size, dcache\_align, use\_handshake, compatibility) \

156 BUILD\_ASSERT(dcache\_align >= 0, \

157 "Cache line size must be non negative."); \

158 BUILD\_ASSERT((size) > 0 && IS\_PTR\_ALIGNED\_BYTES(size, \_PBUF\_IDX\_SIZE), \

159 "Incorrect size."); \

160 BUILD\_ASSERT(IS\_PTR\_ALIGNED\_BYTES(mem\_addr, MAX(dcache\_align, \_PBUF\_IDX\_SIZE)), \

161 "Misaligned memory."); \

162 BUILD\_ASSERT(size >= (MAX(dcache\_align, \_PBUF\_IDX\_SIZE) + \_PBUF\_IDX\_SIZE + \

163 \_PBUF\_MIN\_DATA\_LEN), "Insufficient size."); \

164 BUILD\_ASSERT(!(compatibility) || (dcache\_align) >= 8, \

165 "Data cache alignment must be at least 8 if compatibility is enabled.");\

166 static PBUF\_MAYBE\_CONST struct pbuf\_cfg cfg\_##name = \

167 PBUF\_CFG\_INIT(mem\_addr, size, dcache\_align, use\_handshake); \

168 static struct pbuf name = { \

169 .cfg = &cfg\_##name, \

170 }

171

[ 186](group__pbuf.md#ga05782e212932d84ba1192b4dbe1dfd42)int [pbuf\_tx\_init](group__pbuf.md#ga05782e212932d84ba1192b4dbe1dfd42)(struct [pbuf](structpbuf.md) \*pb);

187

[ 202](group__pbuf.md#ga9da1179f5fd3e5238244cd2f7664a928)int [pbuf\_rx\_init](group__pbuf.md#ga9da1179f5fd3e5238244cd2f7664a928)(struct [pbuf](structpbuf.md) \*pb);

203

217

[ 218](group__pbuf.md#ga9df9413dcd6268690a410c33126c081e)int [pbuf\_write](group__pbuf.md#ga9df9413dcd6268690a410c33126c081e)(struct [pbuf](structpbuf.md) \*pb, const char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

219

[ 236](group__pbuf.md#ga44cc22d33d4ec7b7c95459e96ef7d7d0)int [pbuf\_read](group__pbuf.md#ga44cc22d33d4ec7b7c95459e96ef7d7d0)(struct [pbuf](structpbuf.md) \*pb, char \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

237

[ 246](group__pbuf.md#ga9fc04394d6e029aa74c26ae974787483)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pbuf\_handshake\_read](group__pbuf.md#ga9fc04394d6e029aa74c26ae974787483)(struct [pbuf](structpbuf.md) \*pb);

247

[ 256](group__pbuf.md#ga97cb3608eaaa4f276d57c21150916938)void [pbuf\_handshake\_write](group__pbuf.md#ga97cb3608eaaa4f276d57c21150916938)(struct [pbuf](structpbuf.md) \*pb, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value);

257

[ 270](group__pbuf.md#gab31a49d00da9713170f4e63ba97191d9)int [pbuf\_get\_initial\_buf](group__pbuf.md#gab31a49d00da9713170f4e63ba97191d9)(struct [pbuf](structpbuf.md) \*pb, volatile char \*\*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*len);

271

275

276#ifdef \_\_cplusplus

277}

278#endif

279

280#endif /\* ZEPHYR\_INCLUDE\_IPC\_PBUF\_H\_ \*/

[cache.h](cache_8h.md)

cache API interface

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[pbuf\_tx\_init](group__pbuf.md#ga05782e212932d84ba1192b4dbe1dfd42)

int pbuf\_tx\_init(struct pbuf \*pb)

Initialize the Tx packet buffer.

[pbuf\_read](group__pbuf.md#ga44cc22d33d4ec7b7c95459e96ef7d7d0)

int pbuf\_read(struct pbuf \*pb, char \*buf, uint16\_t len)

Read specified amount of data from the packet buffer.

[pbuf\_handshake\_write](group__pbuf.md#ga97cb3608eaaa4f276d57c21150916938)

void pbuf\_handshake\_write(struct pbuf \*pb, uint32\_t value)

Write handshake word to pbuf.

[pbuf\_rx\_init](group__pbuf.md#ga9da1179f5fd3e5238244cd2f7664a928)

int pbuf\_rx\_init(struct pbuf \*pb)

Initialize the Rx packet buffer.

[pbuf\_write](group__pbuf.md#ga9df9413dcd6268690a410c33126c081e)

int pbuf\_write(struct pbuf \*pb, const char \*buf, uint16\_t len)

Write specified amount of data to the packet buffer.

[pbuf\_handshake\_read](group__pbuf.md#ga9fc04394d6e029aa74c26ae974787483)

uint32\_t pbuf\_handshake\_read(struct pbuf \*pb)

Read handshake word from pbuf.

[pbuf\_get\_initial\_buf](group__pbuf.md#gab31a49d00da9713170f4e63ba97191d9)

int pbuf\_get\_initial\_buf(struct pbuf \*pb, volatile char \*\*buf, uint16\_t \*len)

Get first buffer from pbuf.

[PBUF\_MAYBE\_CONST](group__pbuf.md#gaba4cc55b02db047bc2e0ca5c873b1222)

#define PBUF\_MAYBE\_CONST

**Definition** pbuf.h:42

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

**Definition** pbuf.h:49

[pbuf\_cfg::data\_loc](structpbuf__cfg.md#a427cea0b6f83a0411ed251c0fa9cdad5)

uint8\_t \* data\_loc

**Definition** pbuf.h:66

[pbuf\_cfg::handshake\_loc](structpbuf__cfg.md#a8be1cfcfeba47d8b4dd6ee1fa5bf4400)

volatile uint32\_t \* handshake\_loc

**Definition** pbuf.h:54

[pbuf\_cfg::dcache\_alignment](structpbuf__cfg.md#a8e6a0f423a4c2cab92b515246483e8b0)

uint32\_t dcache\_alignment

**Definition** pbuf.h:61

[pbuf\_cfg::len](structpbuf__cfg.md#aad5a0bc4bdef7cec0496e15d75d131dc)

uint32\_t len

**Definition** pbuf.h:65

[pbuf\_cfg::rd\_idx\_loc](structpbuf__cfg.md#aaec17609d27ad086678dafab940e2ae1)

volatile uint32\_t \* rd\_idx\_loc

**Definition** pbuf.h:50

[pbuf\_cfg::wr\_idx\_loc](structpbuf__cfg.md#afb7da887c911f2530cd9168b0a00b3b6)

volatile uint32\_t \* wr\_idx\_loc

**Definition** pbuf.h:57

[pbuf\_data](structpbuf__data.md)

Data block of the packed buffer.

**Definition** pbuf.h:75

[pbuf\_data::wr\_idx](structpbuf__data.md#ae5d497c293f1b84e7a8e801c5349a0b9)

volatile uint32\_t wr\_idx

**Definition** pbuf.h:76

[pbuf\_data::rd\_idx](structpbuf__data.md#aecb4e2462b1d308d43883b935e4648fe)

volatile uint32\_t rd\_idx

**Definition** pbuf.h:80

[pbuf](structpbuf.md)

Scure packed buffer.

**Definition** pbuf.h:99

[pbuf::cfg](structpbuf.md#aa69c940d23b73b1292f5e8a6e1537494)

const struct pbuf\_cfg \*const cfg

**Definition** pbuf.h:100

[pbuf::data](structpbuf.md#acbfdc9861d79dcd26bc73bfef5835e7e)

struct pbuf\_data data

**Definition** pbuf.h:103

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [pbuf.h](pbuf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
