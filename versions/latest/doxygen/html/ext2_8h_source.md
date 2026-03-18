---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ext2_8h_source.html
original_path: doxygen/html/ext2_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ext2.h

[Go to the documentation of this file.](ext2_8h.md)

1/\*

2 \* Copyright (c) 2023 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_FS\_EXT2\_H\_

8#define ZEPHYR\_INCLUDE\_FS\_EXT2\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

[ 26](structext2__cfg.md)struct [ext2\_cfg](structext2__cfg.md) {

[ 27](structext2__cfg.md#a3eb5587725f3fee4dd8ea86a7077e662) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [block\_size](structext2__cfg.md#a3eb5587725f3fee4dd8ea86a7077e662);

[ 28](structext2__cfg.md#ab8b546e8256994362261085fb4e826df) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fs\_size](structext2__cfg.md#ab8b546e8256994362261085fb4e826df); /\* Number of blocks that we want to take. \*/

[ 29](structext2__cfg.md#a04309de819dc1b31a7578667c82678b6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bytes\_per\_inode](structext2__cfg.md#a04309de819dc1b31a7578667c82678b6);

[ 30](structext2__cfg.md#ad11fad3e7fd7088263b578babd60c77d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](structext2__cfg.md#ad11fad3e7fd7088263b578babd60c77d)[16];

[ 31](structext2__cfg.md#a2f0bbc643995eb206f59625dff84b4e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [volume\_name](structext2__cfg.md#a2f0bbc643995eb206f59625dff84b4e9)[17]; /\* If first byte is 0 then name ext2" is given. \*/

[ 32](structext2__cfg.md#a63d3fca7ab9c60da4457569c51e3a511) bool [set\_uuid](structext2__cfg.md#a63d3fca7ab9c60da4457569c51e3a511);

33};

34

[ 35](ext2_8h.md#a06e57a8a022d06a32a1bda2ae6747c54)#define FS\_EXT2\_DECLARE\_DEFAULT\_CONFIG(name) \

36 static struct ext2\_cfg name = { \

37 .block\_size = 1024, \

38 .fs\_size = 0x800000, \

39 .bytes\_per\_inode = 4096, \

40 .volume\_name = {'e', 'x', 't', '2', '\0'}, \

41 .set\_uuid = false, \

42 }

43

44

45#endif /\* ZEPHYR\_INCLUDE\_FS\_EXT2\_H\_ \*/

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[ext2\_cfg](structext2__cfg.md)

Configuration used to format ext2 file system.

**Definition** ext2.h:26

[ext2\_cfg::bytes\_per\_inode](structext2__cfg.md#a04309de819dc1b31a7578667c82678b6)

uint32\_t bytes\_per\_inode

**Definition** ext2.h:29

[ext2\_cfg::volume\_name](structext2__cfg.md#a2f0bbc643995eb206f59625dff84b4e9)

uint8\_t volume\_name[17]

**Definition** ext2.h:31

[ext2\_cfg::block\_size](structext2__cfg.md#a3eb5587725f3fee4dd8ea86a7077e662)

uint32\_t block\_size

**Definition** ext2.h:27

[ext2\_cfg::set\_uuid](structext2__cfg.md#a63d3fca7ab9c60da4457569c51e3a511)

bool set\_uuid

**Definition** ext2.h:32

[ext2\_cfg::fs\_size](structext2__cfg.md#ab8b546e8256994362261085fb4e826df)

uint32\_t fs\_size

**Definition** ext2.h:28

[ext2\_cfg::uuid](structext2__cfg.md#ad11fad3e7fd7088263b578babd60c77d)

uint8\_t uuid[16]

**Definition** ext2.h:30

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [ext2.h](ext2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
