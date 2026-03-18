---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mb__display_8h_source.html
original_path: doxygen/html/mb__display_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mb\_display.h

[Go to the documentation of this file.](mb__display_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_DISPLAY\_MB\_DISPLAY\_H\_

12#define ZEPHYR\_INCLUDE\_DISPLAY\_MB\_DISPLAY\_H\_

13

20

21#include <[stdio.h](stdio_8h.md)>

22#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

23#include <[stdbool.h](stdbool_8h.md)>

24#include <[zephyr/sys/util.h](util_8h.md)>

25#include <[zephyr/toolchain.h](toolchain_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 37](structmb__image.md)struct [mb\_image](structmb__image.md) {

38 union {

39 struct {

[ 40](structmb__image.md#a044fee7be7fb1e5b3e2c2dab74011d9a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c1](structmb__image.md#a044fee7be7fb1e5b3e2c2dab74011d9a):1,

[ 41](structmb__image.md#ad7eb096bb15a0bb8378bae32804fe6c6) [c2](structmb__image.md#ad7eb096bb15a0bb8378bae32804fe6c6):1,

[ 42](structmb__image.md#a88455e59017a73533e727671019f6ea0) [c3](structmb__image.md#a88455e59017a73533e727671019f6ea0):1,

[ 43](structmb__image.md#a506e5ac82c7229ba7e89f67de8fbcbe2) [c4](structmb__image.md#a506e5ac82c7229ba7e89f67de8fbcbe2):1,

[ 44](structmb__image.md#a2af8f97c0ddc8cf463cf83a483e3025b) [c5](structmb__image.md#a2af8f97c0ddc8cf463cf83a483e3025b):1;

[ 45](structmb__image.md#a93ec1bb1c0cdc09de75d00976bd23eeb) } [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)[5];

[ 46](structmb__image.md#a158f0bdbb7d135da0dcf5c6b997d0ff5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [row](structmb__image.md#a158f0bdbb7d135da0dcf5c6b997d0ff5)[5];

47 };

48};

49

[ 55](group__mb__display.md#ga750a177cffbb90ab38392d9ebad9a8eb)enum [mb\_display\_mode](group__mb__display.md#ga750a177cffbb90ab38392d9ebad9a8eb) {

[ 57](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5) [MB\_DISPLAY\_MODE\_DEFAULT](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5),

58

[ 60](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a) [MB\_DISPLAY\_MODE\_SINGLE](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a),

61

[ 63](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69) [MB\_DISPLAY\_MODE\_SCROLL](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69),

64

65 /\* Display flags, i.e. modifiers to the chosen mode \*/

66

[ 68](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc) [MB\_DISPLAY\_FLAG\_LOOP](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

69};

70

[ 96](group__mb__display.md#ga529a5650acaf699b23b4b4234127cf2c)#define MB\_IMAGE(\_rows...) { .r = { \_rows } }

97

107struct mb\_display;

108

[ 114](group__mb__display.md#ga94e3eadd1cf386b8d9494ccfa8afaa40)struct mb\_display \*[mb\_display\_get](group__mb__display.md#ga94e3eadd1cf386b8d9494ccfa8afaa40)(void);

115

[ 132](group__mb__display.md#ga2a6e20d57d0d65033281dd7c3ea19126)void [mb\_display\_image](group__mb__display.md#ga2a6e20d57d0d65033281dd7c3ea19126)(struct mb\_display \*disp, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration,

133 const struct [mb\_image](structmb__image.md) \*img, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_count);

134

[ 152](group__mb__display.md#ga993a6a0225206f53170d25d9177c1225)\_\_printf\_like(4, 5) void [mb\_display\_print](group__mb__display.md#ga993a6a0225206f53170d25d9177c1225)(struct mb\_display \*disp,

153 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration,

154 const char \*fmt, ...);

155

[ 161](group__mb__display.md#gad15b3635993007d8aad9364cbe29311b)void [mb\_display\_stop](group__mb__display.md#gad15b3635993007d8aad9364cbe29311b)(struct mb\_display \*disp);

162

163#ifdef \_\_cplusplus

164}

165#endif

166

170

171#endif /\* ZEPHYR\_INCLUDE\_DISPLAY\_MB\_DISPLAY\_H\_ \*/

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[mb\_display\_image](group__mb__display.md#ga2a6e20d57d0d65033281dd7c3ea19126)

void mb\_display\_image(struct mb\_display \*disp, uint32\_t mode, int32\_t duration, const struct mb\_image \*img, uint8\_t img\_count)

Display one or more images on the BBC micro:bit LED display.

[mb\_display\_mode](group__mb__display.md#ga750a177cffbb90ab38392d9ebad9a8eb)

mb\_display\_mode

Display mode.

**Definition** mb\_display.h:55

[mb\_display\_get](group__mb__display.md#ga94e3eadd1cf386b8d9494ccfa8afaa40)

struct mb\_display \* mb\_display\_get(void)

Get a pointer to the BBC micro:bit display object.

[mb\_display\_print](group__mb__display.md#ga993a6a0225206f53170d25d9177c1225)

void mb\_display\_print(struct mb\_display \*disp, uint32\_t mode, int32\_t duration, const char \*fmt,...)

Print a string of characters on the BBC micro:bit LED display.

[mb\_display\_stop](group__mb__display.md#gad15b3635993007d8aad9364cbe29311b)

void mb\_display\_stop(struct mb\_display \*disp)

Stop the ongoing display of an image.

[MB\_DISPLAY\_MODE\_SINGLE](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a)

@ MB\_DISPLAY\_MODE\_SINGLE

Display images sequentially, one at a time.

**Definition** mb\_display.h:60

[MB\_DISPLAY\_MODE\_DEFAULT](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5)

@ MB\_DISPLAY\_MODE\_DEFAULT

Default mode ("single" for images, "scroll" for text).

**Definition** mb\_display.h:57

[MB\_DISPLAY\_MODE\_SCROLL](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69)

@ MB\_DISPLAY\_MODE\_SCROLL

Display images by scrolling.

**Definition** mb\_display.h:63

[MB\_DISPLAY\_FLAG\_LOOP](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc)

@ MB\_DISPLAY\_FLAG\_LOOP

Loop back to the beginning when reaching the last image.

**Definition** mb\_display.h:68

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[types.h](include_2zephyr_2types_8h.md)

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[stdio.h](stdio_8h.md)

[mb\_image](structmb__image.md)

Representation of a BBC micro:bit display image.

**Definition** mb\_display.h:37

[mb\_image::c1](structmb__image.md#a044fee7be7fb1e5b3e2c2dab74011d9a)

uint8\_t c1

**Definition** mb\_display.h:40

[mb\_image::row](structmb__image.md#a158f0bdbb7d135da0dcf5c6b997d0ff5)

uint8\_t row[5]

**Definition** mb\_display.h:46

[mb\_image::c5](structmb__image.md#a2af8f97c0ddc8cf463cf83a483e3025b)

uint8\_t c5

**Definition** mb\_display.h:44

[mb\_image::c4](structmb__image.md#a506e5ac82c7229ba7e89f67de8fbcbe2)

uint8\_t c4

**Definition** mb\_display.h:43

[mb\_image::c3](structmb__image.md#a88455e59017a73533e727671019f6ea0)

uint8\_t c3

**Definition** mb\_display.h:42

[mb\_image::c2](structmb__image.md#ad7eb096bb15a0bb8378bae32804fe6c6)

uint8\_t c2

**Definition** mb\_display.h:41

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [display](dir_dbe0bbdb2da2eed929c1e8ee8e4a99ef.md)
- [mb\_display.h](mb__display_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
