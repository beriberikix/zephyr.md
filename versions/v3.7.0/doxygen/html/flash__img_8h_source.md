---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/flash__img_8h_source.html
original_path: doxygen/html/flash__img_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_img.h

[Go to the documentation of this file.](flash__img_8h.md)

1/\*

2 \* Copyright (c) 2017 Nordic Semiconductor ASA

3 \* Copyright (c) 2017 Linaro Limited

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

14

15#ifndef ZEPHYR\_INCLUDE\_DFU\_FLASH\_IMG\_H\_

16#define ZEPHYR\_INCLUDE\_DFU\_FLASH\_IMG\_H\_

17

18#include <[zephyr/storage/stream\_flash.h](stream__flash_8h.md)>

19

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 32](structflash__img__context.md)struct [flash\_img\_context](structflash__img__context.md) {

[ 33](structflash__img__context.md#a80fb0afaa391d3242c7de9ffe0f10675) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf](structflash__img__context.md#a80fb0afaa391d3242c7de9ffe0f10675)[CONFIG\_IMG\_BLOCK\_BUF\_SIZE];

[ 34](structflash__img__context.md#ae98e6408fe707543f30094f89ae43bdd) const struct [flash\_area](structflash__img__context.md#ae98e6408fe707543f30094f89ae43bdd) \*[flash\_area](structflash__img__context.md#ae98e6408fe707543f30094f89ae43bdd);

[ 35](structflash__img__context.md#a9bdb531f92f32957ab78e6cfcced6a3b) struct [stream\_flash\_ctx](structstream__flash__ctx.md) [stream](structflash__img__context.md#a9bdb531f92f32957ab78e6cfcced6a3b);

36};

37

[ 44](structflash__img__check.md)struct [flash\_img\_check](structflash__img__check.md) {

[ 45](structflash__img__check.md#a6c4aebe9974ddebf0ceafe7f61af8ae9) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[match](structflash__img__check.md#a6c4aebe9974ddebf0ceafe7f61af8ae9);

[ 46](structflash__img__check.md#abac05d254f5fc46093808083c86be379) size\_t [clen](structflash__img__check.md#abac05d254f5fc46093808083c86be379);

47};

48

[ 57](group__flash__img__api.md#ga1b194edcb7e4ae34717d011f08d93e0c)int [flash\_img\_init\_id](group__flash__img__api.md#ga1b194edcb7e4ae34717d011f08d93e0c)(struct [flash\_img\_context](structflash__img__context.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id);

58

[ 66](group__flash__img__api.md#gac6d1d7811516493242b318be2ecd82df)int [flash\_img\_init](group__flash__img__api.md#gac6d1d7811516493242b318be2ecd82df)(struct [flash\_img\_context](structflash__img__context.md) \*ctx);

67

[ 75](group__flash__img__api.md#gac1ef017d400bda921ca894d13126b390)size\_t [flash\_img\_bytes\_written](group__flash__img__api.md#gac1ef017d400bda921ca894d13126b390)(struct [flash\_img\_context](structflash__img__context.md) \*ctx);

76

[ 94](group__flash__img__api.md#gae3cb2d6be9f993bcf5a97931475d9a6d)int [flash\_img\_buffered\_write](group__flash__img__api.md#gae3cb2d6be9f993bcf5a97931475d9a6d)(struct [flash\_img\_context](structflash__img__context.md) \*ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

95 size\_t len, bool flush);

96

[ 110](group__flash__img__api.md#ga5a025255d8bf4a94f9e8d315d5502e88)int [flash\_img\_check](group__flash__img__api.md#ga5a025255d8bf4a94f9e8d315d5502e88)(struct [flash\_img\_context](structflash__img__context.md) \*ctx,

111 const struct [flash\_img\_check](structflash__img__check.md) \*fic,

112 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id);

113

114#ifdef \_\_cplusplus

115}

116#endif

117

121

122#endif /\* ZEPHYR\_INCLUDE\_DFU\_FLASH\_IMG\_H\_ \*/

[flash\_img\_init\_id](group__flash__img__api.md#ga1b194edcb7e4ae34717d011f08d93e0c)

int flash\_img\_init\_id(struct flash\_img\_context \*ctx, uint8\_t area\_id)

Initialize context needed for writing the image to the flash.

[flash\_img\_check](group__flash__img__api.md#ga5a025255d8bf4a94f9e8d315d5502e88)

int flash\_img\_check(struct flash\_img\_context \*ctx, const struct flash\_img\_check \*fic, uint8\_t area\_id)

Verify flash memory length bytes integrity from a flash area.

[flash\_img\_bytes\_written](group__flash__img__api.md#gac1ef017d400bda921ca894d13126b390)

size\_t flash\_img\_bytes\_written(struct flash\_img\_context \*ctx)

Read number of bytes of the image written to the flash.

[flash\_img\_init](group__flash__img__api.md#gac6d1d7811516493242b318be2ecd82df)

int flash\_img\_init(struct flash\_img\_context \*ctx)

Initialize context needed for writing the image to the flash.

[flash\_img\_buffered\_write](group__flash__img__api.md#gae3cb2d6be9f993bcf5a97931475d9a6d)

int flash\_img\_buffered\_write(struct flash\_img\_context \*ctx, const uint8\_t \*data, size\_t len, bool flush)

Process input buffers to be written to the image slot 1.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[stream\_flash.h](stream__flash_8h.md)

Public API for stream writes to flash.

[flash\_img\_check](structflash__img__check.md)

Structure for verify flash region integrity.

**Definition** flash\_img.h:44

[flash\_img\_check::match](structflash__img__check.md#a6c4aebe9974ddebf0ceafe7f61af8ae9)

const uint8\_t \* match

**Definition** flash\_img.h:45

[flash\_img\_check::clen](structflash__img__check.md#abac05d254f5fc46093808083c86be379)

size\_t clen

Match vector data.

**Definition** flash\_img.h:46

[flash\_img\_context](structflash__img__context.md)

**Definition** flash\_img.h:32

[flash\_img\_context::buf](structflash__img__context.md#a80fb0afaa391d3242c7de9ffe0f10675)

uint8\_t buf[CONFIG\_IMG\_BLOCK\_BUF\_SIZE]

**Definition** flash\_img.h:33

[flash\_img\_context::stream](structflash__img__context.md#a9bdb531f92f32957ab78e6cfcced6a3b)

struct stream\_flash\_ctx stream

**Definition** flash\_img.h:35

[flash\_img\_context::flash\_area](structflash__img__context.md#ae98e6408fe707543f30094f89ae43bdd)

const struct flash\_area \* flash\_area

**Definition** flash\_img.h:34

[stream\_flash\_ctx](structstream__flash__ctx.md)

Structure for stream flash context.

**Definition** stream\_flash.h:56

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dfu](dir_b8bb0fd55a94366ea1f20beca08b160d.md)
- [flash\_img.h](flash__img_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
