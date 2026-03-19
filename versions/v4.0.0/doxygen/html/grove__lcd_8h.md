---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/grove__lcd_8h.html
original_path: doxygen/html/grove__lcd_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grove\_lcd.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](grove__lcd_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GLCD\_DS\_DISPLAY\_ON](group__grove__display.md#ga4fe4ad1bc603fa658247ea2f7dbf7f31)   (1 << 2) |
| #define | [GLCD\_DS\_DISPLAY\_OFF](group__grove__display.md#ga66bc1e76fcda544f619d02ecbdcb368f)   (0 << 2) |
| #define | [GLCD\_DS\_CURSOR\_ON](group__grove__display.md#gaa40ba9872b397a1daa26f68f17d7e28d)   (1 << 1) |
| #define | [GLCD\_DS\_CURSOR\_OFF](group__grove__display.md#gaac73ba0ea95d570493485212ce704691)   (0 << 1) |
| #define | [GLCD\_DS\_BLINK\_ON](group__grove__display.md#ga62f05f0aa279c530bb96153efd2a36da)   (1 << 0) |
| #define | [GLCD\_DS\_BLINK\_OFF](group__grove__display.md#gaca5ebc6bff0db636ff8767f7c225143f)   (0 << 0) |
| #define | [GLCD\_IS\_SHIFT\_INCREMENT](group__grove__display.md#ga460a887aaa11dbe4461226a55bcae951)   (1 << 1) |
| #define | [GLCD\_IS\_SHIFT\_DECREMENT](group__grove__display.md#ga2258570aac3ed680739324a2daf5f626)   (0 << 1) |
| #define | [GLCD\_IS\_ENTRY\_LEFT](group__grove__display.md#ga5e136501ffbde18b34163bc1a7948c9a)   (1 << 0) |
| #define | [GLCD\_IS\_ENTRY\_RIGHT](group__grove__display.md#ga6c9cee5b9f86efcc2073f60dc204fc2a)   (0 << 0) |
| #define | [GLCD\_FS\_8BIT\_MODE](group__grove__display.md#ga726ae92e51500c82a202164edb706cd4)   (1 << 4) |
| #define | [GLCD\_FS\_ROWS\_2](group__grove__display.md#ga7007ac8d919421d34e4dff4e97503cb6)   (1 << 3) |
| #define | [GLCD\_FS\_ROWS\_1](group__grove__display.md#ga2ebedc80c40c35ea57ebcb3968bc1052)   (0 << 3) |
| #define | [GLCD\_FS\_DOT\_SIZE\_BIG](group__grove__display.md#gabcfa7abdd0834ee469a6693a0aa7f883)   (1 << 2) |
| #define | [GLCD\_FS\_DOT\_SIZE\_LITTLE](group__grove__display.md#gae47fb073bb30f1fab7171a6bad55fc22)   (0 << 2) |
| #define | [GROVE\_RGB\_WHITE](group__grove__display.md#gaca2204b331e88203b05d0382d80cc5de)   0 |
| #define | [GROVE\_RGB\_RED](group__grove__display.md#gad391aa4262d4fd7e93052e7dafc5daa4)   1 |
| #define | [GROVE\_RGB\_GREEN](group__grove__display.md#ga6e9faff3c1a708d6c5d509a85e1dd1f4)   2 |
| #define | [GROVE\_RGB\_BLUE](group__grove__display.md#gaf754fe5b8b20bca5ae9768833e045ef8)   3 |

| Functions | |
| --- | --- |
| void | [glcd\_print](group__grove__display.md#gaecd7b73186d110fa4bd2c47bbb7d63a2) (const struct [device](structdevice.md) \*dev, char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Send text to the screen. |
| void | [glcd\_cursor\_pos\_set](group__grove__display.md#ga8272c8c1ff41835306908a0f6932feae) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) col, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) row) |
|  | Set text cursor position for next additions. |
| void | [glcd\_clear](group__grove__display.md#ga10929139f1632247968ccdd4fdd79dcd) (const struct [device](structdevice.md) \*dev) |
|  | Clear the current display. |
| void | [glcd\_display\_state\_set](group__grove__display.md#ga103c6edb0b5ed37f34c12694338acc70) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt) |
|  | Function to change the display state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [glcd\_display\_state\_get](group__grove__display.md#gac3139bf68d1acbb27905a2346da13b17) (const struct [device](structdevice.md) \*dev) |
|  | return the display feature set associated with the device |
| void | [glcd\_input\_state\_set](group__grove__display.md#gae73554047414529e5e7957a5d394e4a2) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt) |
|  | Function to change the input state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [glcd\_input\_state\_get](group__grove__display.md#ga3c590c83b2f1c8ea0fe301daa7a40198) (const struct [device](structdevice.md) \*dev) |
|  | return the input set associated with the device |
| void | [glcd\_function\_set](group__grove__display.md#ga5e9fb362faf9c040eaa16addbfad2b6d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opt) |
|  | Function to set the functional state of the display. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [glcd\_function\_get](group__grove__display.md#gad660824e481428b811c914d6bf4634f5) (const struct [device](structdevice.md) \*dev) |
|  | return the function set associated with the device |
| void | [glcd\_color\_select](group__grove__display.md#gabd119208e05f9f878b7f24a62da08db2) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) color) |
|  | Set LCD background to a predefined color. |
| void | [glcd\_color\_set](group__grove__display.md#gaf99aa37f71396baaf523348a3ea9cbbe) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) g, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) b) |
|  | Set LCD background to custom RGB color value. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [grove\_lcd](dir_d49f155e905fd7f5a0736c6379c7db83.md)
- [grove\_lcd.h](grove__lcd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
