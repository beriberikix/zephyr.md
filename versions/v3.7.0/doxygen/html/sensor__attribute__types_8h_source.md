---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sensor__attribute__types_8h_source.html
original_path: doxygen/html/sensor__attribute__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_attribute\_types.h

[Go to the documentation of this file.](sensor__attribute__types_8h.md)

1/\*

2 \* Copyright (c) 2023 Google LLC

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ATTRIBUTE\_TYPES\_H

7#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ATTRIBUTE\_TYPES\_H

8

9#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h.md)>

10#include <[zephyr/dsp/print\_format.h](print__format_8h.md)>

11

12#include <[inttypes.h](inttypes_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 27](structsensor__three__axis__attribute.md)struct [sensor\_three\_axis\_attribute](structsensor__three__axis__attribute.md) {

[ 28](structsensor__three__axis__attribute.md#a230f8021356406c3225868d43e39be18) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensor__three__axis__attribute.md#a230f8021356406c3225868d43e39be18);

29 union {

30 struct {

[ 31](structsensor__three__axis__attribute.md#a82ee018216949a3132fcdf165e63d2be) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [x](structsensor__three__axis__attribute.md#a82ee018216949a3132fcdf165e63d2be);

[ 32](structsensor__three__axis__attribute.md#a5c1bd40fb615aa6515c10ff249bae0c2) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [y](structsensor__three__axis__attribute.md#a5c1bd40fb615aa6515c10ff249bae0c2);

[ 33](structsensor__three__axis__attribute.md#afee1c9c4fc2b18fb5ae7f6a69af6e2e9) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [z](structsensor__three__axis__attribute.md#afee1c9c4fc2b18fb5ae7f6a69af6e2e9);

34 };

[ 35](structsensor__three__axis__attribute.md#a88cb3f5259b9dde34c5b26daae4ed270) [q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0) [values](structsensor__three__axis__attribute.md#a88cb3f5259b9dde34c5b26daae4ed270)[3];

36 };

37};

38

39#ifdef \_\_cplusplus

40}

41#endif

42

43#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_ATTRIBUTE\_TYPES\_H \*/

[q31\_t](group__math__dsp.md#gadc89a3547f5324b7b3b95adec3806bc0)

int32\_t q31\_t

32-bit fractional data type in 1.31 format.

**Definition** types.h:35

[types.h](include_2zephyr_2dsp_2types_8h.md)

[inttypes.h](inttypes_8h.md)

[print\_format.h](print__format_8h.md)

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[sensor\_three\_axis\_attribute](structsensor__three__axis__attribute.md)

Used by the following channel/attribute pairs:

**Definition** sensor\_attribute\_types.h:27

[sensor\_three\_axis\_attribute::shift](structsensor__three__axis__attribute.md#a230f8021356406c3225868d43e39be18)

int8\_t shift

**Definition** sensor\_attribute\_types.h:28

[sensor\_three\_axis\_attribute::y](structsensor__three__axis__attribute.md#a5c1bd40fb615aa6515c10ff249bae0c2)

q31\_t y

**Definition** sensor\_attribute\_types.h:32

[sensor\_three\_axis\_attribute::x](structsensor__three__axis__attribute.md#a82ee018216949a3132fcdf165e63d2be)

q31\_t x

**Definition** sensor\_attribute\_types.h:31

[sensor\_three\_axis\_attribute::values](structsensor__three__axis__attribute.md#a88cb3f5259b9dde34c5b26daae4ed270)

q31\_t values[3]

**Definition** sensor\_attribute\_types.h:35

[sensor\_three\_axis\_attribute::z](structsensor__three__axis__attribute.md#afee1c9c4fc2b18fb5ae7f6a69af6e2e9)

q31\_t z

**Definition** sensor\_attribute\_types.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor\_attribute\_types.h](sensor__attribute__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
