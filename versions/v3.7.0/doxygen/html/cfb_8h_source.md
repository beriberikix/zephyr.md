---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cfb_8h_source.html
original_path: doxygen/html/cfb_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cfb.h

[Go to the documentation of this file.](cfb_8h.md)

1/\*

2 \* Copyright (c) 2018 PHYTEC Messtechnik GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_\_CFB\_H\_\_

13#define \_\_CFB\_H\_\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/drivers/display.h](display_8h.md)>

17#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

[ 30](group__monochrome__character__framebuffer.md#ga32e8edb517093dbc1b612a1bef24c7af)enum [cfb\_display\_param](group__monochrome__character__framebuffer.md#ga32e8edb517093dbc1b612a1bef24c7af) {

[ 31](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afaab99f7b44bcfca4e49a71df82ad3b3e1) [CFB\_DISPLAY\_HEIGH](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afaab99f7b44bcfca4e49a71df82ad3b3e1) = 0,

[ 32](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a) [CFB\_DISPLAY\_WIDTH](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a),

[ 33](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630) [CFB\_DISPLAY\_PPT](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630),

[ 34](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c) [CFB\_DISPLAY\_ROWS](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c),

[ 35](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f) [CFB\_DISPLAY\_COLS](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f),

36};

37

[ 38](group__monochrome__character__framebuffer.md#gae98337479a5339d4171797e96313fee5)enum [cfb\_font\_caps](group__monochrome__character__framebuffer.md#gae98337479a5339d4171797e96313fee5) {

[ 39](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6) [CFB\_FONT\_MONO\_VPACKED](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 40](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c) [CFB\_FONT\_MONO\_HPACKED](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 41](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b) [CFB\_FONT\_MSB\_FIRST](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

42};

43

[ 44](structcfb__font.md)struct [cfb\_font](structcfb__font.md) {

[ 45](structcfb__font.md#abe8771187455817e8085a42820079aea) const void \*[data](structcfb__font.md#abe8771187455817e8085a42820079aea);

[ 46](structcfb__font.md#a4ac3e8578e577909058fdcd8bce62f3b) enum [cfb\_font\_caps](group__monochrome__character__framebuffer.md#gae98337479a5339d4171797e96313fee5) [caps](structcfb__font.md#a4ac3e8578e577909058fdcd8bce62f3b);

[ 47](structcfb__font.md#ab58695cca74151c86f442366bd80a039) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [width](structcfb__font.md#ab58695cca74151c86f442366bd80a039);

[ 48](structcfb__font.md#ad50168c069d5cda8e924ba336875ef85) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [height](structcfb__font.md#ad50168c069d5cda8e924ba336875ef85);

[ 49](structcfb__font.md#a204e414d8b0add418fb92914402d14e2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [first\_char](structcfb__font.md#a204e414d8b0add418fb92914402d14e2);

[ 50](structcfb__font.md#a79ca54ef1b7928c9bde7bc4d730aa417) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [last\_char](structcfb__font.md#a79ca54ef1b7928c9bde7bc4d730aa417);

51};

52

[ 53](structcfb__position.md)struct [cfb\_position](structcfb__position.md) {

[ 54](structcfb__position.md#ab185e5d2e053e69a9f214daad2276b18) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [x](structcfb__position.md#ab185e5d2e053e69a9f214daad2276b18);

[ 55](structcfb__position.md#ac93902b6eb27dedbb2190071fafad271) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [y](structcfb__position.md#ac93902b6eb27dedbb2190071fafad271);

56};

57

[ 69](group__monochrome__character__framebuffer.md#ga1fe25d7d6b057a40715ad44db7bc9249)#define FONT\_ENTRY\_DEFINE(\_name, \_width, \_height, \_caps, \_data, \_fc, \_lc) \

70 static const STRUCT\_SECTION\_ITERABLE(cfb\_font, \_name) = { \

71 .data = \_data, \

72 .caps = \_caps, \

73 .width = \_width, \

74 .height = \_height, \

75 .first\_char = \_fc, \

76 .last\_char = \_lc, \

77 }

78

[ 89](group__monochrome__character__framebuffer.md#ga8c55d057b1efcbcd667ad4fbc1c856d5)int [cfb\_print](group__monochrome__character__framebuffer.md#ga8c55d057b1efcbcd667ad4fbc1c856d5)(const struct [device](structdevice.md) \*dev, const char \*const str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y);

90

[ 103](group__monochrome__character__framebuffer.md#ga496b3b161fa0bc2e42e3d5de83c4f544)int [cfb\_draw\_text](group__monochrome__character__framebuffer.md#ga496b3b161fa0bc2e42e3d5de83c4f544)(const struct [device](structdevice.md) \*dev, const char \*const str, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y);

104

[ 113](group__monochrome__character__framebuffer.md#gae1943e8d138f5e612f6508dd0f510134)int [cfb\_draw\_point](group__monochrome__character__framebuffer.md#gae1943e8d138f5e612f6508dd0f510134)(const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*pos);

114

[ 124](group__monochrome__character__framebuffer.md#ga81af74d2831d5a4fc1338da693401958)int [cfb\_draw\_line](group__monochrome__character__framebuffer.md#ga81af74d2831d5a4fc1338da693401958)(const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*start,

125 const struct [cfb\_position](structcfb__position.md) \*end);

126

[ 136](group__monochrome__character__framebuffer.md#ga0b26cd0d9e2de71f754f85849ccba001)int [cfb\_draw\_rect](group__monochrome__character__framebuffer.md#ga0b26cd0d9e2de71f754f85849ccba001)(const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*start,

137 const struct [cfb\_position](structcfb__position.md) \*end);

138

[ 147](group__monochrome__character__framebuffer.md#gac9a957b5dd6e99377d9c070085df3252)int [cfb\_framebuffer\_clear](group__monochrome__character__framebuffer.md#gac9a957b5dd6e99377d9c070085df3252)(const struct [device](structdevice.md) \*dev, bool clear\_display);

148

[ 156](group__monochrome__character__framebuffer.md#ga8e86d48a0c6d951de34089f5d6cf5fb1)int [cfb\_framebuffer\_invert](group__monochrome__character__framebuffer.md#ga8e86d48a0c6d951de34089f5d6cf5fb1)(const struct [device](structdevice.md) \*dev);

157

[ 169](group__monochrome__character__framebuffer.md#gadc802c8fc630fd9dfb445c0f1fa81ab4)int [cfb\_invert\_area](group__monochrome__character__framebuffer.md#gadc802c8fc630fd9dfb445c0f1fa81ab4)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y,

170 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) width, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) height);

171

[ 180](group__monochrome__character__framebuffer.md#ga9d0b3f63c2b52458ab040993b3c3b97d)int [cfb\_framebuffer\_finalize](group__monochrome__character__framebuffer.md#ga9d0b3f63c2b52458ab040993b3c3b97d)(const struct [device](structdevice.md) \*dev);

181

[ 190](group__monochrome__character__framebuffer.md#gaeb46dfb72c31474c1acbc46d2f08803e)int [cfb\_get\_display\_parameter](group__monochrome__character__framebuffer.md#gaeb46dfb72c31474c1acbc46d2f08803e)(const struct [device](structdevice.md) \*dev,

191 enum [cfb\_display\_param](group__monochrome__character__framebuffer.md#ga32e8edb517093dbc1b612a1bef24c7af));

192

[ 201](group__monochrome__character__framebuffer.md#ga29343c61a7a9e28c50cb384ba4f383cf)int [cfb\_framebuffer\_set\_font](group__monochrome__character__framebuffer.md#ga29343c61a7a9e28c50cb384ba4f383cf)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx);

202

[ 211](group__monochrome__character__framebuffer.md#gac0918644cb24a39ef578e54acac46d64)int [cfb\_set\_kerning](group__monochrome__character__framebuffer.md#gac0918644cb24a39ef578e54acac46d64)(const struct [device](structdevice.md) \*dev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) kerning);

212

[ 223](group__monochrome__character__framebuffer.md#ga63ea5f559391ed735da8afa78745e458)int [cfb\_get\_font\_size](group__monochrome__character__framebuffer.md#ga63ea5f559391ed735da8afa78745e458)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*width,

224 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*height);

225

[ 233](group__monochrome__character__framebuffer.md#ga5ef3b84b6169eaef398cf47b3583c827)int [cfb\_get\_numof\_fonts](group__monochrome__character__framebuffer.md#ga5ef3b84b6169eaef398cf47b3583c827)(const struct [device](structdevice.md) \*dev);

234

[ 242](group__monochrome__character__framebuffer.md#ga2bbe913d7f0a10b4ba543d83ef6fac95)int [cfb\_framebuffer\_init](group__monochrome__character__framebuffer.md#ga2bbe913d7f0a10b4ba543d83ef6fac95)(const struct [device](structdevice.md) \*dev);

243

[ 249](group__monochrome__character__framebuffer.md#ga981f062bb314c107230e068f575f81ef)void [cfb\_framebuffer\_deinit](group__monochrome__character__framebuffer.md#ga981f062bb314c107230e068f575f81ef)(const struct [device](structdevice.md) \*dev);

250

251#ifdef \_\_cplusplus

252}

253#endif

254

258

259#endif /\* \_\_CFB\_H\_\_ \*/

[device.h](device_8h.md)

[display.h](display_8h.md)

Public API for display drivers and applications.

[cfb\_draw\_rect](group__monochrome__character__framebuffer.md#ga0b26cd0d9e2de71f754f85849ccba001)

int cfb\_draw\_rect(const struct device \*dev, const struct cfb\_position \*start, const struct cfb\_position \*end)

Draw a rectangle.

[cfb\_framebuffer\_set\_font](group__monochrome__character__framebuffer.md#ga29343c61a7a9e28c50cb384ba4f383cf)

int cfb\_framebuffer\_set\_font(const struct device \*dev, uint8\_t idx)

Set font.

[cfb\_framebuffer\_init](group__monochrome__character__framebuffer.md#ga2bbe913d7f0a10b4ba543d83ef6fac95)

int cfb\_framebuffer\_init(const struct device \*dev)

Initialize Character Framebuffer.

[cfb\_display\_param](group__monochrome__character__framebuffer.md#ga32e8edb517093dbc1b612a1bef24c7af)

cfb\_display\_param

**Definition** cfb.h:30

[cfb\_draw\_text](group__monochrome__character__framebuffer.md#ga496b3b161fa0bc2e42e3d5de83c4f544)

int cfb\_draw\_text(const struct device \*dev, const char \*const str, int16\_t x, int16\_t y)

Print a string into the framebuffer.

[cfb\_get\_numof\_fonts](group__monochrome__character__framebuffer.md#ga5ef3b84b6169eaef398cf47b3583c827)

int cfb\_get\_numof\_fonts(const struct device \*dev)

Get number of fonts.

[cfb\_get\_font\_size](group__monochrome__character__framebuffer.md#ga63ea5f559391ed735da8afa78745e458)

int cfb\_get\_font\_size(const struct device \*dev, uint8\_t idx, uint8\_t \*width, uint8\_t \*height)

Get font size.

[cfb\_draw\_line](group__monochrome__character__framebuffer.md#ga81af74d2831d5a4fc1338da693401958)

int cfb\_draw\_line(const struct device \*dev, const struct cfb\_position \*start, const struct cfb\_position \*end)

Draw a line.

[cfb\_print](group__monochrome__character__framebuffer.md#ga8c55d057b1efcbcd667ad4fbc1c856d5)

int cfb\_print(const struct device \*dev, const char \*const str, uint16\_t x, uint16\_t y)

Print a string into the framebuffer.

[cfb\_framebuffer\_invert](group__monochrome__character__framebuffer.md#ga8e86d48a0c6d951de34089f5d6cf5fb1)

int cfb\_framebuffer\_invert(const struct device \*dev)

Invert Pixels.

[cfb\_framebuffer\_deinit](group__monochrome__character__framebuffer.md#ga981f062bb314c107230e068f575f81ef)

void cfb\_framebuffer\_deinit(const struct device \*dev)

Deinitialize Character Framebuffer.

[cfb\_framebuffer\_finalize](group__monochrome__character__framebuffer.md#ga9d0b3f63c2b52458ab040993b3c3b97d)

int cfb\_framebuffer\_finalize(const struct device \*dev)

Finalize framebuffer and write it to display RAM, invert or reorder pixels if necessary.

[cfb\_set\_kerning](group__monochrome__character__framebuffer.md#gac0918644cb24a39ef578e54acac46d64)

int cfb\_set\_kerning(const struct device \*dev, int8\_t kerning)

Set font kerning (spacing between individual letters).

[cfb\_framebuffer\_clear](group__monochrome__character__framebuffer.md#gac9a957b5dd6e99377d9c070085df3252)

int cfb\_framebuffer\_clear(const struct device \*dev, bool clear\_display)

Clear framebuffer.

[cfb\_invert\_area](group__monochrome__character__framebuffer.md#gadc802c8fc630fd9dfb445c0f1fa81ab4)

int cfb\_invert\_area(const struct device \*dev, uint16\_t x, uint16\_t y, uint16\_t width, uint16\_t height)

Invert Pixels in selected area.

[cfb\_draw\_point](group__monochrome__character__framebuffer.md#gae1943e8d138f5e612f6508dd0f510134)

int cfb\_draw\_point(const struct device \*dev, const struct cfb\_position \*pos)

Draw a point.

[cfb\_font\_caps](group__monochrome__character__framebuffer.md#gae98337479a5339d4171797e96313fee5)

cfb\_font\_caps

**Definition** cfb.h:38

[cfb\_get\_display\_parameter](group__monochrome__character__framebuffer.md#gaeb46dfb72c31474c1acbc46d2f08803e)

int cfb\_get\_display\_parameter(const struct device \*dev, enum cfb\_display\_param)

Get display parameter.

[CFB\_DISPLAY\_PPT](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630)

@ CFB\_DISPLAY\_PPT

**Definition** cfb.h:33

[CFB\_DISPLAY\_ROWS](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c)

@ CFB\_DISPLAY\_ROWS

**Definition** cfb.h:34

[CFB\_DISPLAY\_HEIGH](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afaab99f7b44bcfca4e49a71df82ad3b3e1)

@ CFB\_DISPLAY\_HEIGH

**Definition** cfb.h:31

[CFB\_DISPLAY\_COLS](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f)

@ CFB\_DISPLAY\_COLS

**Definition** cfb.h:35

[CFB\_DISPLAY\_WIDTH](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a)

@ CFB\_DISPLAY\_WIDTH

**Definition** cfb.h:32

[CFB\_FONT\_MONO\_HPACKED](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c)

@ CFB\_FONT\_MONO\_HPACKED

**Definition** cfb.h:40

[CFB\_FONT\_MONO\_VPACKED](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6)

@ CFB\_FONT\_MONO\_VPACKED

**Definition** cfb.h:39

[CFB\_FONT\_MSB\_FIRST](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b)

@ CFB\_FONT\_MSB\_FIRST

**Definition** cfb.h:41

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[cfb\_font](structcfb__font.md)

**Definition** cfb.h:44

[cfb\_font::first\_char](structcfb__font.md#a204e414d8b0add418fb92914402d14e2)

uint8\_t first\_char

**Definition** cfb.h:49

[cfb\_font::caps](structcfb__font.md#a4ac3e8578e577909058fdcd8bce62f3b)

enum cfb\_font\_caps caps

**Definition** cfb.h:46

[cfb\_font::last\_char](structcfb__font.md#a79ca54ef1b7928c9bde7bc4d730aa417)

uint8\_t last\_char

**Definition** cfb.h:50

[cfb\_font::width](structcfb__font.md#ab58695cca74151c86f442366bd80a039)

uint8\_t width

**Definition** cfb.h:47

[cfb\_font::data](structcfb__font.md#abe8771187455817e8085a42820079aea)

const void \* data

**Definition** cfb.h:45

[cfb\_font::height](structcfb__font.md#ad50168c069d5cda8e924ba336875ef85)

uint8\_t height

**Definition** cfb.h:48

[cfb\_position](structcfb__position.md)

**Definition** cfb.h:53

[cfb\_position::x](structcfb__position.md#ab185e5d2e053e69a9f214daad2276b18)

uint16\_t x

**Definition** cfb.h:54

[cfb\_position::y](structcfb__position.md#ac93902b6eb27dedbb2190071fafad271)

uint16\_t y

**Definition** cfb.h:55

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [display](dir_dbe0bbdb2da2eed929c1e8ee8e4a99ef.md)
- [cfb.h](cfb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
