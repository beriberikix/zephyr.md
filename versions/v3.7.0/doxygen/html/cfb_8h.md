---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cfb_8h.html
original_path: doxygen/html/cfb_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cfb.h File Reference

Public Monochrome Character Framebuffer API.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/display.h](display_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](cfb_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [cfb\_font](structcfb__font.md) |
| struct | [cfb\_position](structcfb__position.md) |

| Macros | |
| --- | --- |
| #define | [FONT\_ENTRY\_DEFINE](group__monochrome__character__framebuffer.md#ga1fe25d7d6b057a40715ad44db7bc9249)(\_name, \_width, \_height, \_caps, \_data, \_fc, \_lc) |
|  | Macro for creating a font entry. |

| Enumerations | |
| --- | --- |
| enum | [cfb\_display\_param](group__monochrome__character__framebuffer.md#ga32e8edb517093dbc1b612a1bef24c7af) {     [CFB\_DISPLAY\_HEIGH](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afaab99f7b44bcfca4e49a71df82ad3b3e1) = 0 , [CFB\_DISPLAY\_WIDTH](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afae3709eb7028aa574528a7035f5f4f43a) , [CFB\_DISPLAY\_PPT](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afa3cc81a52aac17be5f1e3787c20ffe630) , [CFB\_DISPLAY\_ROWS](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afa594c2dcc2987ff448e265a18e163d22c) ,     [CFB\_DISPLAY\_COLS](group__monochrome__character__framebuffer.md#gga32e8edb517093dbc1b612a1bef24c7afac64b7d912d7f53ff111a64a96f8d977f)   } |
| enum | [cfb\_font\_caps](group__monochrome__character__framebuffer.md#gae98337479a5339d4171797e96313fee5) { [CFB\_FONT\_MONO\_VPACKED](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a5f679876161e14616d5342806578e3e6) = BIT(0) , [CFB\_FONT\_MONO\_HPACKED](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a36d4664fb2460600d5dbe85a76ac974c) = BIT(1) , [CFB\_FONT\_MSB\_FIRST](group__monochrome__character__framebuffer.md#ggae98337479a5339d4171797e96313fee5a837f2231088d93be083dda79095ac82b) = BIT(2) } |

| Functions | |
| --- | --- |
| int | [cfb\_print](group__monochrome__character__framebuffer.md#ga8c55d057b1efcbcd667ad4fbc1c856d5) (const struct [device](structdevice.md) \*dev, const char \*const str, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y) |
|  | Print a string into the framebuffer. |
| int | [cfb\_draw\_text](group__monochrome__character__framebuffer.md#ga496b3b161fa0bc2e42e3d5de83c4f544) (const struct [device](structdevice.md) \*dev, const char \*const str, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y) |
|  | Print a string into the framebuffer. |
| int | [cfb\_draw\_point](group__monochrome__character__framebuffer.md#gae1943e8d138f5e612f6508dd0f510134) (const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*pos) |
|  | Draw a point. |
| int | [cfb\_draw\_line](group__monochrome__character__framebuffer.md#ga81af74d2831d5a4fc1338da693401958) (const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*start, const struct [cfb\_position](structcfb__position.md) \*end) |
|  | Draw a line. |
| int | [cfb\_draw\_rect](group__monochrome__character__framebuffer.md#ga0b26cd0d9e2de71f754f85849ccba001) (const struct [device](structdevice.md) \*dev, const struct [cfb\_position](structcfb__position.md) \*start, const struct [cfb\_position](structcfb__position.md) \*end) |
|  | Draw a rectangle. |
| int | [cfb\_framebuffer\_clear](group__monochrome__character__framebuffer.md#gac9a957b5dd6e99377d9c070085df3252) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) clear\_display) |
|  | Clear framebuffer. |
| int | [cfb\_framebuffer\_invert](group__monochrome__character__framebuffer.md#ga8e86d48a0c6d951de34089f5d6cf5fb1) (const struct [device](structdevice.md) \*dev) |
|  | Invert Pixels. |
| int | [cfb\_invert\_area](group__monochrome__character__framebuffer.md#gadc802c8fc630fd9dfb445c0f1fa81ab4) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) y, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) width, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) height) |
|  | Invert Pixels in selected area. |
| int | [cfb\_framebuffer\_finalize](group__monochrome__character__framebuffer.md#ga9d0b3f63c2b52458ab040993b3c3b97d) (const struct [device](structdevice.md) \*dev) |
|  | Finalize framebuffer and write it to display RAM, invert or reorder pixels if necessary. |
| int | [cfb\_get\_display\_parameter](group__monochrome__character__framebuffer.md#gaeb46dfb72c31474c1acbc46d2f08803e) (const struct [device](structdevice.md) \*dev, enum [cfb\_display\_param](group__monochrome__character__framebuffer.md#ga32e8edb517093dbc1b612a1bef24c7af)) |
|  | Get display parameter. |
| int | [cfb\_framebuffer\_set\_font](group__monochrome__character__framebuffer.md#ga29343c61a7a9e28c50cb384ba4f383cf) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx) |
|  | Set font. |
| int | [cfb\_set\_kerning](group__monochrome__character__framebuffer.md#gac0918644cb24a39ef578e54acac46d64) (const struct [device](structdevice.md) \*dev, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) kerning) |
|  | Set font kerning (spacing between individual letters). |
| int | [cfb\_get\_font\_size](group__monochrome__character__framebuffer.md#ga63ea5f559391ed735da8afa78745e458) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*width, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*height) |
|  | Get font size. |
| int | [cfb\_get\_numof\_fonts](group__monochrome__character__framebuffer.md#ga5ef3b84b6169eaef398cf47b3583c827) (const struct [device](structdevice.md) \*dev) |
|  | Get number of fonts. |
| int | [cfb\_framebuffer\_init](group__monochrome__character__framebuffer.md#ga2bbe913d7f0a10b4ba543d83ef6fac95) (const struct [device](structdevice.md) \*dev) |
|  | Initialize Character Framebuffer. |
| void | [cfb\_framebuffer\_deinit](group__monochrome__character__framebuffer.md#ga981f062bb314c107230e068f575f81ef) (const struct [device](structdevice.md) \*dev) |
|  | Deinitialize Character Framebuffer. |

## Detailed Description

Public Monochrome Character Framebuffer API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [display](dir_dbe0bbdb2da2eed929c1e8ee8e4a99ef.md)
- [cfb.h](cfb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
