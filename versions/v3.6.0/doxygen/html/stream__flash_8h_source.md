---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stream__flash_8h_source.html
original_path: doxygen/html/stream__flash_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stream\_flash.h

[Go to the documentation of this file.](stream__flash_8h.md)

1/\*

2 \* Copyright (c) 2017, 2020 Nordic Semiconductor ASA

3 \* Copyright (c) 2017 Linaro Limited

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_STORAGE\_STREAM\_FLASH\_H\_

14#define ZEPHYR\_INCLUDE\_STORAGE\_STREAM\_FLASH\_H\_

15

23

24#include <[stdbool.h](stdbool_8h.md)>

25#include <[zephyr/drivers/flash.h](flash_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 46](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705)typedef int (\*[stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len, size\_t offset);

47

[ 54](structstream__flash__ctx.md)struct [stream\_flash\_ctx](structstream__flash__ctx.md) {

[ 55](structstream__flash__ctx.md#a5d7dd0c4a0687e566deb8bd6af3f0c8d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structstream__flash__ctx.md#a5d7dd0c4a0687e566deb8bd6af3f0c8d); /\* Write buffer \*/

[ 56](structstream__flash__ctx.md#aff53c741cf5141338206d89274c508c0) size\_t [buf\_len](structstream__flash__ctx.md#aff53c741cf5141338206d89274c508c0); /\* Length of write buffer \*/

[ 57](structstream__flash__ctx.md#a6fcef2130672bea3b9e5170c80e6e56a) size\_t [buf\_bytes](structstream__flash__ctx.md#a6fcef2130672bea3b9e5170c80e6e56a); /\* Number of bytes currently stored in write buf \*/

[ 58](structstream__flash__ctx.md#a8d959157df9da6907d6d90ac12f762f8) const struct [device](structdevice.md) \*[fdev](structstream__flash__ctx.md#a8d959157df9da6907d6d90ac12f762f8); /\* Flash device \*/

[ 59](structstream__flash__ctx.md#a694774f427f3a93057f0365867d3d90a) size\_t [bytes\_written](structstream__flash__ctx.md#a694774f427f3a93057f0365867d3d90a); /\* Number of bytes written to flash \*/

[ 60](structstream__flash__ctx.md#a66596293929b734b3132cc0a02674e3f) size\_t [offset](structstream__flash__ctx.md#a66596293929b734b3132cc0a02674e3f); /\* Offset from base of flash device to write area \*/

[ 61](structstream__flash__ctx.md#afbaf8abad7ff12865863dc4108ee8ad2) size\_t [available](structstream__flash__ctx.md#afbaf8abad7ff12865863dc4108ee8ad2); /\* Available bytes in write area \*/

[ 62](structstream__flash__ctx.md#a230924b0451fa21cefc87f01e0cbf84b) [stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705) [callback](structstream__flash__ctx.md#a230924b0451fa21cefc87f01e0cbf84b); /\* Callback invoked after write op \*/

63#ifdef CONFIG\_STREAM\_FLASH\_ERASE

64 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) last\_erased\_page\_start\_offset; /\* Last erased offset \*/

65#endif

66};

67

[ 84](group__stream__flash.md#ga63e6418e220136a9a0ab2992d9d8f937)int [stream\_flash\_init](group__stream__flash.md#ga63e6418e220136a9a0ab2992d9d8f937)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const struct [device](structdevice.md) \*fdev,

85 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buf\_len, size\_t offset, size\_t size,

86 [stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705) cb);

[ 96](group__stream__flash.md#gadcff5388f54e0e784619c706795fe7a8)size\_t [stream\_flash\_bytes\_written](group__stream__flash.md#gadcff5388f54e0e784619c706795fe7a8)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx);

97

[ 115](group__stream__flash.md#gaa23d33939f344fcd42a281afa5e6f1db)int [stream\_flash\_buffered\_write](group__stream__flash.md#gaa23d33939f344fcd42a281afa5e6f1db)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

116 size\_t len, bool flush);

117

[ 130](group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d)int [stream\_flash\_erase\_page](group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394));

131

[ 146](group__stream__flash.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)int [stream\_flash\_progress\_load](group__stream__flash.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx,

147 const char \*settings\_key);

148

[ 158](group__stream__flash.md#ga6965ef8973f281fd0507e208d1645483)int [stream\_flash\_progress\_save](group__stream__flash.md#ga6965ef8973f281fd0507e208d1645483)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx,

159 const char \*settings\_key);

160

[ 170](group__stream__flash.md#gafd736d9014a3c5060d5c43383d07ac59)int [stream\_flash\_progress\_clear](group__stream__flash.md#gafd736d9014a3c5060d5c43383d07ac59)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx,

171 const char \*settings\_key);

172

173#ifdef \_\_cplusplus

174}

175#endif

176

180

181#endif /\* ZEPHYR\_INCLUDE\_STORAGE\_STREAM\_FLASH\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[flash.h](flash_8h.md)

Public API for FLASH drivers.

[stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705)

int(\* stream\_flash\_callback\_t)(uint8\_t \*buf, size\_t len, size\_t offset)

Signature for callback invoked after flash write completes.

**Definition** stream\_flash.h:46

[stream\_flash\_progress\_load](group__stream__flash.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)

int stream\_flash\_progress\_load(struct stream\_flash\_ctx \*ctx, const char \*settings\_key)

Load persistent stream write progress stored with key settings\_key .

[stream\_flash\_init](group__stream__flash.md#ga63e6418e220136a9a0ab2992d9d8f937)

int stream\_flash\_init(struct stream\_flash\_ctx \*ctx, const struct device \*fdev, uint8\_t \*buf, size\_t buf\_len, size\_t offset, size\_t size, stream\_flash\_callback\_t cb)

Initialize context needed for stream writes to flash.

[stream\_flash\_progress\_save](group__stream__flash.md#ga6965ef8973f281fd0507e208d1645483)

int stream\_flash\_progress\_save(struct stream\_flash\_ctx \*ctx, const char \*settings\_key)

Save persistent stream write progress using key settings\_key .

[stream\_flash\_erase\_page](group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d)

int stream\_flash\_erase\_page(struct stream\_flash\_ctx \*ctx, off\_t off)

Erase the flash page to which a given offset belongs.

[stream\_flash\_buffered\_write](group__stream__flash.md#gaa23d33939f344fcd42a281afa5e6f1db)

int stream\_flash\_buffered\_write(struct stream\_flash\_ctx \*ctx, const uint8\_t \*data, size\_t len, bool flush)

Process input buffers to be written to flash device in single blocks.

[stream\_flash\_bytes\_written](group__stream__flash.md#gadcff5388f54e0e784619c706795fe7a8)

size\_t stream\_flash\_bytes\_written(struct stream\_flash\_ctx \*ctx)

Read number of bytes written to the flash.

[stream\_flash\_progress\_clear](group__stream__flash.md#gafd736d9014a3c5060d5c43383d07ac59)

int stream\_flash\_progress\_clear(struct stream\_flash\_ctx \*ctx, const char \*settings\_key)

Clear persistent stream write progress stored with key settings\_key .

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[stream\_flash\_ctx](structstream__flash__ctx.md)

Structure for stream flash context.

**Definition** stream\_flash.h:54

[stream\_flash\_ctx::callback](structstream__flash__ctx.md#a230924b0451fa21cefc87f01e0cbf84b)

stream\_flash\_callback\_t callback

**Definition** stream\_flash.h:62

[stream\_flash\_ctx::buf](structstream__flash__ctx.md#a5d7dd0c4a0687e566deb8bd6af3f0c8d)

uint8\_t \* buf

**Definition** stream\_flash.h:55

[stream\_flash\_ctx::offset](structstream__flash__ctx.md#a66596293929b734b3132cc0a02674e3f)

size\_t offset

**Definition** stream\_flash.h:60

[stream\_flash\_ctx::bytes\_written](structstream__flash__ctx.md#a694774f427f3a93057f0365867d3d90a)

size\_t bytes\_written

**Definition** stream\_flash.h:59

[stream\_flash\_ctx::buf\_bytes](structstream__flash__ctx.md#a6fcef2130672bea3b9e5170c80e6e56a)

size\_t buf\_bytes

**Definition** stream\_flash.h:57

[stream\_flash\_ctx::fdev](structstream__flash__ctx.md#a8d959157df9da6907d6d90ac12f762f8)

const struct device \* fdev

**Definition** stream\_flash.h:58

[stream\_flash\_ctx::available](structstream__flash__ctx.md#afbaf8abad7ff12865863dc4108ee8ad2)

size\_t available

**Definition** stream\_flash.h:61

[stream\_flash\_ctx::buf\_len](structstream__flash__ctx.md#aff53c741cf5141338206d89274c508c0)

size\_t buf\_len

**Definition** stream\_flash.h:56

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [storage](dir_9ae83148a5180e4d77f53cf673d8ea1c.md)
- [stream\_flash.h](stream__flash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
