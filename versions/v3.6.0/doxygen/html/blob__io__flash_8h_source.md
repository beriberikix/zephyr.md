---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/blob__io__flash_8h_source.html
original_path: doxygen/html/blob__io__flash_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

blob\_io\_flash.h

[Go to the documentation of this file.](blob__io__flash_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_IO\_FLASH\_H\_\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_IO\_FLASH\_H\_\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 23](structbt__mesh__blob__io__flash.md)struct [bt\_mesh\_blob\_io\_flash](structbt__mesh__blob__io__flash.md) {

[ 25](structbt__mesh__blob__io__flash.md#a3b506d86d9cc7fb7206f96cbdd2cd3fe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [area\_id](structbt__mesh__blob__io__flash.md#a3b506d86d9cc7fb7206f96cbdd2cd3fe);

[ 27](structbt__mesh__blob__io__flash.md#a511648b9e653993aee99eda5efe3b1e9) enum [bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962) [mode](structbt__mesh__blob__io__flash.md#a511648b9e653993aee99eda5efe3b1e9);

[ 29](structbt__mesh__blob__io__flash.md#ac4eb40a7e53adce60c2fcd11eb0b6b57) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [offset](structbt__mesh__blob__io__flash.md#ac4eb40a7e53adce60c2fcd11eb0b6b57);

30

31

32 /\* Internal flash area pointer. \*/

[ 33](structbt__mesh__blob__io__flash.md#a99227cd93d2b6230be7bd5cef9fb8232) const struct [flash\_area](structflash__area.md) \*[area](structbt__mesh__blob__io__flash.md#a99227cd93d2b6230be7bd5cef9fb8232);

34 /\* BLOB stream. \*/

[ 35](structbt__mesh__blob__io__flash.md#a24abc17719dd627e3e3d7c8e61d4c96f) struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) [io](structbt__mesh__blob__io__flash.md#a24abc17719dd627e3e3d7c8e61d4c96f);

36};

37

[ 46](group__bt__mesh__blob__io__flash.md#ga8d99fd3dc35230447f7e7ef9f2c4bc81)int [bt\_mesh\_blob\_io\_flash\_init](group__bt__mesh__blob__io__flash.md#ga8d99fd3dc35230447f7e7ef9f2c4bc81)(struct [bt\_mesh\_blob\_io\_flash](structbt__mesh__blob__io__flash.md) \*flash,

47 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset);

48

50

51#ifdef \_\_cplusplus

52}

53#endif

54

55#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BLOB\_IO\_FLASH\_H\_\_ \*/

[bt\_mesh\_blob\_io\_flash\_init](group__bt__mesh__blob__io__flash.md#ga8d99fd3dc35230447f7e7ef9f2c4bc81)

int bt\_mesh\_blob\_io\_flash\_init(struct bt\_mesh\_blob\_io\_flash \*flash, uint8\_t area\_id, off\_t offset)

Initialize a flash stream.

[bt\_mesh\_blob\_io\_mode](group__bt__mesh__blob.md#ga2618fb7365f180a73a7eecd11cf2f962)

bt\_mesh\_blob\_io\_mode

BLOB stream interaction mode.

**Definition** blob.h:137

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_mesh\_blob\_io\_flash](structbt__mesh__blob__io__flash.md)

BLOB flash stream.

**Definition** blob\_io\_flash.h:23

[bt\_mesh\_blob\_io\_flash::io](structbt__mesh__blob__io__flash.md#a24abc17719dd627e3e3d7c8e61d4c96f)

struct bt\_mesh\_blob\_io io

**Definition** blob\_io\_flash.h:35

[bt\_mesh\_blob\_io\_flash::area\_id](structbt__mesh__blob__io__flash.md#a3b506d86d9cc7fb7206f96cbdd2cd3fe)

uint8\_t area\_id

Flash area ID to write the BLOB to.

**Definition** blob\_io\_flash.h:25

[bt\_mesh\_blob\_io\_flash::mode](structbt__mesh__blob__io__flash.md#a511648b9e653993aee99eda5efe3b1e9)

enum bt\_mesh\_blob\_io\_mode mode

Active stream mode.

**Definition** blob\_io\_flash.h:27

[bt\_mesh\_blob\_io\_flash::area](structbt__mesh__blob__io__flash.md#a99227cd93d2b6230be7bd5cef9fb8232)

const struct flash\_area \* area

**Definition** blob\_io\_flash.h:33

[bt\_mesh\_blob\_io\_flash::offset](structbt__mesh__blob__io__flash.md#ac4eb40a7e53adce60c2fcd11eb0b6b57)

off\_t offset

Offset into the flash area to place the BLOB at (in bytes).

**Definition** blob\_io\_flash.h:29

[bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)

BLOB stream.

**Definition** blob.h:145

[flash\_area](structflash__area.md)

Flash partition.

**Definition** flash\_map.h:57

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [blob\_io\_flash.h](blob__io__flash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
