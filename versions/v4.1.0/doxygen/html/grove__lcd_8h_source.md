---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/grove__lcd_8h_source.html
original_path: doxygen/html/grove__lcd_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grove\_lcd.h

[Go to the documentation of this file.](grove__lcd_8h.md)

1/\* grove\_lcd.h - Public API for the Grove RGB LCD device \*/

2/\*

3 \* Copyright (c) 2015 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7#ifndef ZEPHYR\_INCLUDE\_DISPLAY\_GROVE\_LCD\_H\_

8#define ZEPHYR\_INCLUDE\_DISPLAY\_GROVE\_LCD\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/device.h](device_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

[ 32](group__grove__display.md#gaecd7b73186d110fa4bd2c47bbb7d63a2)void [glcd\_print](group__grove__display.md#gaecd7b73186d110fa4bd2c47bbb7d63a2)(const struct [device](structdevice.md) \*dev, char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

33

34

[ 42](group__grove__display.md#ga8272c8c1ff41835306908a0f6932feae)void [glcd\_cursor\_pos\_set](group__grove__display.md#ga8272c8c1ff41835306908a0f6932feae)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) col, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) row);

43

[ 49](group__grove__display.md#ga10929139f1632247968ccdd4fdd79dcd)void [glcd\_clear](group__grove__display.md#ga10929139f1632247968ccdd4fdd79dcd)(const struct [device](structdevice.md) \*dev);

50

51/\* Defines for the GLCD\_CMD\_DISPLAY\_SWITCH options \*/

[ 52](group__grove__display.md#ga4fe4ad1bc603fa658247ea2f7dbf7f31)#define GLCD\_DS\_DISPLAY\_ON (1 << 2)

[ 53](group__grove__display.md#ga66bc1e76fcda544f619d02ecbdcb368f)#define GLCD\_DS\_DISPLAY\_OFF (0 << 2)

[ 54](group__grove__display.md#gaa40ba9872b397a1daa26f68f17d7e28d)#define GLCD\_DS\_CURSOR\_ON (1 << 1)

[ 55](group__grove__display.md#gaac73ba0ea95d570493485212ce704691)#define GLCD\_DS\_CURSOR\_OFF (0 << 1)

[ 56](group__grove__display.md#ga62f05f0aa279c530bb96153efd2a36da)#define GLCD\_DS\_BLINK\_ON (1 << 0)

[ 57](group__grove__display.md#gaca5ebc6bff0db636ff8767f7c225143f)#define GLCD\_DS\_BLINK\_OFF (0 << 0)

[ 69](group__grove__display.md#ga103c6edb0b5ed37f34c12694338acc70)void [glcd\_display\_state\_set](group__grove__display.md#ga103c6edb0b5ed37f34c12694338acc70)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt);

70

[ 78](group__grove__display.md#gac3139bf68d1acbb27905a2346da13b17)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [glcd\_display\_state\_get](group__grove__display.md#gac3139bf68d1acbb27905a2346da13b17)(const struct [device](structdevice.md) \*dev);

79

80/\* Defines for the GLCD\_CMD\_INPUT\_SET to change text direction \*/

[ 81](group__grove__display.md#ga460a887aaa11dbe4461226a55bcae951)#define GLCD\_IS\_SHIFT\_INCREMENT (1 << 1)

[ 82](group__grove__display.md#ga2258570aac3ed680739324a2daf5f626)#define GLCD\_IS\_SHIFT\_DECREMENT (0 << 1)

[ 83](group__grove__display.md#ga5e136501ffbde18b34163bc1a7948c9a)#define GLCD\_IS\_ENTRY\_LEFT (1 << 0)

[ 84](group__grove__display.md#ga6c9cee5b9f86efcc2073f60dc204fc2a)#define GLCD\_IS\_ENTRY\_RIGHT (0 << 0)

[ 95](group__grove__display.md#gae73554047414529e5e7957a5d394e4a2)void [glcd\_input\_state\_set](group__grove__display.md#gae73554047414529e5e7957a5d394e4a2)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt);

96

[ 104](group__grove__display.md#ga3c590c83b2f1c8ea0fe301daa7a40198)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [glcd\_input\_state\_get](group__grove__display.md#ga3c590c83b2f1c8ea0fe301daa7a40198)(const struct [device](structdevice.md) \*dev);

105

106/\* Defines for the LCD\_FUNCTION\_SET \*/

[ 107](group__grove__display.md#ga726ae92e51500c82a202164edb706cd4)#define GLCD\_FS\_8BIT\_MODE (1 << 4)

[ 108](group__grove__display.md#ga7007ac8d919421d34e4dff4e97503cb6)#define GLCD\_FS\_ROWS\_2 (1 << 3)

[ 109](group__grove__display.md#ga2ebedc80c40c35ea57ebcb3968bc1052)#define GLCD\_FS\_ROWS\_1 (0 << 3)

[ 110](group__grove__display.md#gabcfa7abdd0834ee469a6693a0aa7f883)#define GLCD\_FS\_DOT\_SIZE\_BIG (1 << 2)

[ 111](group__grove__display.md#gae47fb073bb30f1fab7171a6bad55fc22)#define GLCD\_FS\_DOT\_SIZE\_LITTLE (0 << 2)

112/\* Bits 0, 1 are not defined for this register \*/

113

[ 123](group__grove__display.md#ga5e9fb362faf9c040eaa16addbfad2b6d)void [glcd\_function\_set](group__grove__display.md#ga5e9fb362faf9c040eaa16addbfad2b6d)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt);

124

[ 132](group__grove__display.md#gad660824e481428b811c914d6bf4634f5)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [glcd\_function\_get](group__grove__display.md#gad660824e481428b811c914d6bf4634f5)(const struct [device](structdevice.md) \*dev);

133

134

135/\* Available color selections \*/

[ 136](group__grove__display.md#gaca2204b331e88203b05d0382d80cc5de)#define GROVE\_RGB\_WHITE 0

[ 137](group__grove__display.md#gad391aa4262d4fd7e93052e7dafc5daa4)#define GROVE\_RGB\_RED 1

[ 138](group__grove__display.md#ga6e9faff3c1a708d6c5d509a85e1dd1f4)#define GROVE\_RGB\_GREEN 2

[ 139](group__grove__display.md#gaf754fe5b8b20bca5ae9768833e045ef8)#define GROVE\_RGB\_BLUE 3

[ 145](group__grove__display.md#gabd119208e05f9f878b7f24a62da08db2)void [glcd\_color\_select](group__grove__display.md#gabd119208e05f9f878b7f24a62da08db2)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) color);

146

147

[ 156](group__grove__display.md#gaf99aa37f71396baaf523348a3ea9cbbe)void [glcd\_color\_set](group__grove__display.md#gaf99aa37f71396baaf523348a3ea9cbbe)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) g,

157 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) b);

158

159

163

164#ifdef \_\_cplusplus

165}

166#endif

167

168#endif /\* ZEPHYR\_INCLUDE\_DISPLAY\_GROVE\_LCD\_H\_ \*/

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[device.h](device_8h.md)

[glcd\_display\_state\_set](group__grove__display.md#ga103c6edb0b5ed37f34c12694338acc70)

void glcd\_display\_state\_set(const struct device \*dev, uint8\_t opt)

Function to change the display state.

[glcd\_clear](group__grove__display.md#ga10929139f1632247968ccdd4fdd79dcd)

void glcd\_clear(const struct device \*dev)

Clear the current display.

[glcd\_input\_state\_get](group__grove__display.md#ga3c590c83b2f1c8ea0fe301daa7a40198)

uint8\_t glcd\_input\_state\_get(const struct device \*dev)

return the input set associated with the device

[glcd\_function\_set](group__grove__display.md#ga5e9fb362faf9c040eaa16addbfad2b6d)

void glcd\_function\_set(const struct device \*dev, uint8\_t opt)

Function to set the functional state of the display.

[glcd\_cursor\_pos\_set](group__grove__display.md#ga8272c8c1ff41835306908a0f6932feae)

void glcd\_cursor\_pos\_set(const struct device \*dev, uint8\_t col, uint8\_t row)

Set text cursor position for next additions.

[glcd\_color\_select](group__grove__display.md#gabd119208e05f9f878b7f24a62da08db2)

void glcd\_color\_select(const struct device \*dev, uint8\_t color)

Set LCD background to a predefined color.

[glcd\_display\_state\_get](group__grove__display.md#gac3139bf68d1acbb27905a2346da13b17)

uint8\_t glcd\_display\_state\_get(const struct device \*dev)

return the display feature set associated with the device

[glcd\_function\_get](group__grove__display.md#gad660824e481428b811c914d6bf4634f5)

uint8\_t glcd\_function\_get(const struct device \*dev)

return the function set associated with the device

[glcd\_input\_state\_set](group__grove__display.md#gae73554047414529e5e7957a5d394e4a2)

void glcd\_input\_state\_set(const struct device \*dev, uint8\_t opt)

Function to change the input state.

[glcd\_print](group__grove__display.md#gaecd7b73186d110fa4bd2c47bbb7d63a2)

void glcd\_print(const struct device \*dev, char \*data, uint32\_t size)

Send text to the screen.

[glcd\_color\_set](group__grove__display.md#gaf99aa37f71396baaf523348a3ea9cbbe)

void glcd\_color\_set(const struct device \*dev, uint8\_t r, uint8\_t g, uint8\_t b)

Set LCD background to custom RGB color value.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [grove\_lcd](dir_d49f155e905fd7f5a0736c6379c7db83.md)
- [grove\_lcd.h](grove__lcd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
