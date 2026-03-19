---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stream__flash_8h_source.html
original_path: doxygen/html/stream__flash_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

25

26#include <[stdbool.h](stdbool_8h.md)>

27#include <[zephyr/drivers/flash.h](flash_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 48](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705)typedef int (\*[stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len, size\_t offset);

49

[ 56](structstream__flash__ctx.md)struct [stream\_flash\_ctx](structstream__flash__ctx.md) {

[ 57](structstream__flash__ctx.md#a5d7dd0c4a0687e566deb8bd6af3f0c8d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structstream__flash__ctx.md#a5d7dd0c4a0687e566deb8bd6af3f0c8d); /\* Write buffer \*/

[ 58](structstream__flash__ctx.md#aff53c741cf5141338206d89274c508c0) size\_t [buf\_len](structstream__flash__ctx.md#aff53c741cf5141338206d89274c508c0); /\* Length of write buffer \*/

[ 59](structstream__flash__ctx.md#a6fcef2130672bea3b9e5170c80e6e56a) size\_t [buf\_bytes](structstream__flash__ctx.md#a6fcef2130672bea3b9e5170c80e6e56a); /\* Number of bytes currently stored in write buf \*/

[ 60](structstream__flash__ctx.md#a8d959157df9da6907d6d90ac12f762f8) const struct [device](structdevice.md) \*[fdev](structstream__flash__ctx.md#a8d959157df9da6907d6d90ac12f762f8); /\* Flash device \*/

[ 61](structstream__flash__ctx.md#a694774f427f3a93057f0365867d3d90a) size\_t [bytes\_written](structstream__flash__ctx.md#a694774f427f3a93057f0365867d3d90a); /\* Number of bytes written to flash \*/

[ 62](structstream__flash__ctx.md#a66596293929b734b3132cc0a02674e3f) size\_t [offset](structstream__flash__ctx.md#a66596293929b734b3132cc0a02674e3f); /\* Offset from base of flash device to write area \*/

[ 63](structstream__flash__ctx.md#afbaf8abad7ff12865863dc4108ee8ad2) size\_t [available](structstream__flash__ctx.md#afbaf8abad7ff12865863dc4108ee8ad2); /\* Available bytes in write area \*/

[ 64](structstream__flash__ctx.md#a230924b0451fa21cefc87f01e0cbf84b) [stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705) [callback](structstream__flash__ctx.md#a230924b0451fa21cefc87f01e0cbf84b); /\* Callback invoked after write op \*/

65#ifdef CONFIG\_STREAM\_FLASH\_ERASE

66 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) last\_erased\_page\_start\_offset; /\* Last erased offset \*/

67#endif

[ 68](structstream__flash__ctx.md#a97f9820d77882b0e1679d35fc5ca3579) size\_t [write\_block\_size](structstream__flash__ctx.md#a97f9820d77882b0e1679d35fc5ca3579); /\* Offset/size device write alignment \*/

[ 69](structstream__flash__ctx.md#ae640958e28fa1b4a065b7a322e00d57b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [erase\_value](structstream__flash__ctx.md#ae640958e28fa1b4a065b7a322e00d57b);

70};

71

[ 88](group__stream__flash.md#ga63e6418e220136a9a0ab2992d9d8f937)int [stream\_flash\_init](group__stream__flash.md#ga63e6418e220136a9a0ab2992d9d8f937)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const struct [device](structdevice.md) \*fdev,

89 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buf\_len, size\_t offset, size\_t size,

90 [stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705) cb);

[ 100](group__stream__flash.md#gaece0b1df3d2bf4f46df588e409c3664b)size\_t [stream\_flash\_bytes\_written](group__stream__flash.md#gaece0b1df3d2bf4f46df588e409c3664b)(const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx);

101

[ 123](group__stream__flash.md#gaa23d33939f344fcd42a281afa5e6f1db)int [stream\_flash\_buffered\_write](group__stream__flash.md#gaa23d33939f344fcd42a281afa5e6f1db)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

124 size\_t len, bool flush);

125

[ 138](group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d)int [stream\_flash\_erase\_page](group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394));

139

[ 155](group__stream__flash.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)int [stream\_flash\_progress\_load](group__stream__flash.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)(struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx,

156 const char \*settings\_key);

157

[ 167](group__stream__flash.md#ga44d5791cc2e8f9bacba723d6645b0d46)int [stream\_flash\_progress\_save](group__stream__flash.md#ga44d5791cc2e8f9bacba723d6645b0d46)(const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx,

168 const char \*settings\_key);

169

[ 179](group__stream__flash.md#ga94d230f73434e90eb692b02f3fbf9ff8)int [stream\_flash\_progress\_clear](group__stream__flash.md#ga94d230f73434e90eb692b02f3fbf9ff8)(const struct [stream\_flash\_ctx](structstream__flash__ctx.md) \*ctx,

180 const char \*settings\_key);

181

182#ifdef \_\_cplusplus

183}

184#endif

185

189

190#endif /\* ZEPHYR\_INCLUDE\_STORAGE\_STREAM\_FLASH\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[flash.h](flash_8h.md)

Public API for FLASH drivers.

[stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705)

int(\* stream\_flash\_callback\_t)(uint8\_t \*buf, size\_t len, size\_t offset)

Signature for callback invoked after flash write completes.

**Definition** stream\_flash.h:48

[stream\_flash\_progress\_load](group__stream__flash.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)

int stream\_flash\_progress\_load(struct stream\_flash\_ctx \*ctx, const char \*settings\_key)

Load persistent stream write progress stored with key settings\_key .

[stream\_flash\_progress\_save](group__stream__flash.md#ga44d5791cc2e8f9bacba723d6645b0d46)

int stream\_flash\_progress\_save(const struct stream\_flash\_ctx \*ctx, const char \*settings\_key)

Save persistent stream write progress using key settings\_key .

[stream\_flash\_init](group__stream__flash.md#ga63e6418e220136a9a0ab2992d9d8f937)

int stream\_flash\_init(struct stream\_flash\_ctx \*ctx, const struct device \*fdev, uint8\_t \*buf, size\_t buf\_len, size\_t offset, size\_t size, stream\_flash\_callback\_t cb)

Initialize context needed for stream writes to flash.

[stream\_flash\_erase\_page](group__stream__flash.md#ga75711b22789724c2d8629e1202dcb48d)

int stream\_flash\_erase\_page(struct stream\_flash\_ctx \*ctx, off\_t off)

Erase the flash page to which a given offset belongs.

[stream\_flash\_progress\_clear](group__stream__flash.md#ga94d230f73434e90eb692b02f3fbf9ff8)

int stream\_flash\_progress\_clear(const struct stream\_flash\_ctx \*ctx, const char \*settings\_key)

Clear persistent stream write progress stored with key settings\_key .

[stream\_flash\_buffered\_write](group__stream__flash.md#gaa23d33939f344fcd42a281afa5e6f1db)

int stream\_flash\_buffered\_write(struct stream\_flash\_ctx \*ctx, const uint8\_t \*data, size\_t len, bool flush)

Process input buffers to be written to flash device in single blocks.

[stream\_flash\_bytes\_written](group__stream__flash.md#gaece0b1df3d2bf4f46df588e409c3664b)

size\_t stream\_flash\_bytes\_written(const struct stream\_flash\_ctx \*ctx)

Read number of bytes written to the flash.

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[stdbool.h](stdbool_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:422

[stream\_flash\_ctx](structstream__flash__ctx.md)

Structure for stream flash context.

**Definition** stream\_flash.h:56

[stream\_flash\_ctx::callback](structstream__flash__ctx.md#a230924b0451fa21cefc87f01e0cbf84b)

stream\_flash\_callback\_t callback

**Definition** stream\_flash.h:64

[stream\_flash\_ctx::buf](structstream__flash__ctx.md#a5d7dd0c4a0687e566deb8bd6af3f0c8d)

uint8\_t \* buf

**Definition** stream\_flash.h:57

[stream\_flash\_ctx::offset](structstream__flash__ctx.md#a66596293929b734b3132cc0a02674e3f)

size\_t offset

**Definition** stream\_flash.h:62

[stream\_flash\_ctx::bytes\_written](structstream__flash__ctx.md#a694774f427f3a93057f0365867d3d90a)

size\_t bytes\_written

**Definition** stream\_flash.h:61

[stream\_flash\_ctx::buf\_bytes](structstream__flash__ctx.md#a6fcef2130672bea3b9e5170c80e6e56a)

size\_t buf\_bytes

**Definition** stream\_flash.h:59

[stream\_flash\_ctx::fdev](structstream__flash__ctx.md#a8d959157df9da6907d6d90ac12f762f8)

const struct device \* fdev

**Definition** stream\_flash.h:60

[stream\_flash\_ctx::write\_block\_size](structstream__flash__ctx.md#a97f9820d77882b0e1679d35fc5ca3579)

size\_t write\_block\_size

**Definition** stream\_flash.h:68

[stream\_flash\_ctx::erase\_value](structstream__flash__ctx.md#ae640958e28fa1b4a065b7a322e00d57b)

uint8\_t erase\_value

**Definition** stream\_flash.h:69

[stream\_flash\_ctx::available](structstream__flash__ctx.md#afbaf8abad7ff12865863dc4108ee8ad2)

size\_t available

**Definition** stream\_flash.h:63

[stream\_flash\_ctx::buf\_len](structstream__flash__ctx.md#aff53c741cf5141338206d89274c508c0)

size\_t buf\_len

**Definition** stream\_flash.h:58

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [storage](dir_9ae83148a5180e4d77f53cf673d8ea1c.md)
- [stream\_flash.h](stream__flash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
