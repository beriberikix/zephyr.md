---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mcux-lpadc_8h_source.html
original_path: doxygen/html/mcux-lpadc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcux-lpadc.h

[Go to the documentation of this file.](mcux-lpadc_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright 2023,2025 NXP

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_MCUX\_LPADC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_MCUX\_LPADC\_H\_

9

[ 10](mcux-lpadc_8h.md#acaf6f35068f36d37cc35d058a867641c)#define MCUX\_LPADC\_CH0A (0x0)

[ 11](mcux-lpadc_8h.md#a68ae1f8d64300d6995f2b026bfa5d098)#define MCUX\_LPADC\_CH0B (0x20)

[ 12](mcux-lpadc_8h.md#ab119aaac451adffede9223b20e455e76)#define MCUX\_LPADC\_CH1A (0x1)

[ 13](mcux-lpadc_8h.md#a6a6c761aad91bb5afe2ac666d3dbeb13)#define MCUX\_LPADC\_CH1B (0x21)

[ 14](mcux-lpadc_8h.md#a623284c21698336e415473b9e6306de1)#define MCUX\_LPADC\_CH2A (0x2)

[ 15](mcux-lpadc_8h.md#a7e9934ed4a29e6af5635a3dfcbc9cdee)#define MCUX\_LPADC\_CH2B (0x22)

[ 16](mcux-lpadc_8h.md#a0242052a5e970c62f938e8e7a38b31de)#define MCUX\_LPADC\_CH3A (0x3)

[ 17](mcux-lpadc_8h.md#a3c2631c2c1aa504ab933d9f0370e5ca9)#define MCUX\_LPADC\_CH3B (0x23)

[ 18](mcux-lpadc_8h.md#a1eade770037c1e424c0136657a5d1919)#define MCUX\_LPADC\_CH4A (0x4)

[ 19](mcux-lpadc_8h.md#ae481a7c29e27507fc9c5c06784d343cd)#define MCUX\_LPADC\_CH4B (0x24)

[ 20](mcux-lpadc_8h.md#af4d36b6a7f938a8d6813253fca7e8e3a)#define MCUX\_LPADC\_CH5A (0x5)

[ 21](mcux-lpadc_8h.md#aeecd165754382f47bd6b5d7127ac2713)#define MCUX\_LPADC\_CH5B (0x25)

[ 22](mcux-lpadc_8h.md#ab2da1fcd6a0c91e1a9555c6342d129f5)#define MCUX\_LPADC\_CH6A (0x6)

[ 23](mcux-lpadc_8h.md#aebc7d8f95c9d3258a29bc0ef13fe00c9)#define MCUX\_LPADC\_CH6B (0x26)

[ 24](mcux-lpadc_8h.md#a4aabe084e93dd5ec5517189b7e2de166)#define MCUX\_LPADC\_CH7A (0x7)

[ 25](mcux-lpadc_8h.md#ad2345007048eb3d47fd3f88679c3ce99)#define MCUX\_LPADC\_CH7B (0x27)

[ 26](mcux-lpadc_8h.md#a0dfdc3c5560b8dcfd3f02455110f5f78)#define MCUX\_LPADC\_CH8A (0x8)

[ 27](mcux-lpadc_8h.md#ac7487087358fd4b4d77320f107dff3d5)#define MCUX\_LPADC\_CH8B (0x28)

[ 28](mcux-lpadc_8h.md#a02a72ded4ad7f73bcc708b076ece0860)#define MCUX\_LPADC\_CH9A (0x9)

[ 29](mcux-lpadc_8h.md#adf7680352daa91d38325591a5acef6ad)#define MCUX\_LPADC\_CH9B (0x29)

[ 30](mcux-lpadc_8h.md#a6083fdf1abedb0001e7f3365e5326684)#define MCUX\_LPADC\_CH10A (0x0A)

[ 31](mcux-lpadc_8h.md#aa3656893670d7281102aeac1e33385c8)#define MCUX\_LPADC\_CH10B (0x2A)

[ 32](mcux-lpadc_8h.md#afaffd2413397010e3fc98eb1c9d0bf36)#define MCUX\_LPADC\_CH11A (0x0B)

[ 33](mcux-lpadc_8h.md#aaa0691a06f9cb40c53e92e95332de446)#define MCUX\_LPADC\_CH11B (0x2B)

[ 34](mcux-lpadc_8h.md#ab70f1dca689a369dc9c1a5d2b6db6f0e)#define MCUX\_LPADC\_CH12A (0x0C)

[ 35](mcux-lpadc_8h.md#a3609b8f71c66f0092626e3f5e2c93ecc)#define MCUX\_LPADC\_CH12B (0x2C)

[ 36](mcux-lpadc_8h.md#a2377741c86543ec738884190d4d4a2ed)#define MCUX\_LPADC\_CH13A (0x0D)

[ 37](mcux-lpadc_8h.md#a08f4c849aa8102fb119dbd479693c8ad)#define MCUX\_LPADC\_CH13B (0x2D)

[ 38](mcux-lpadc_8h.md#a42f4807ce5f74a44df3918c8098b0f16)#define MCUX\_LPADC\_CH14A (0x0E)

[ 39](mcux-lpadc_8h.md#ab99e75ef55608001d6b485bac7f94ef9)#define MCUX\_LPADC\_CH14B (0x2E)

[ 40](mcux-lpadc_8h.md#a869b4575ac2b0aff9575b64a3b7d97b8)#define MCUX\_LPADC\_CH15A (0x0F)

[ 41](mcux-lpadc_8h.md#ad4c4ac56ddc25acdd823bd0ef9f8600f)#define MCUX\_LPADC\_CH15B (0x2F)

[ 42](mcux-lpadc_8h.md#a25acb53d4d4188f66a6929a810c5b7a2)#define MCUX\_LPADC\_CH16A (0x10)

[ 43](mcux-lpadc_8h.md#a1717ef815d272601eef177e28cb1f396)#define MCUX\_LPADC\_CH16B (0x30)

[ 44](mcux-lpadc_8h.md#a4b35415cfae0a9e739b2589bbf21b798)#define MCUX\_LPADC\_CH17A (0x11)

[ 45](mcux-lpadc_8h.md#a0a8b307c19c72f6538fa5307d22cf0bf)#define MCUX\_LPADC\_CH17B (0x31)

[ 46](mcux-lpadc_8h.md#a02ecef6f939bf5d7c53b3cbafa50c036)#define MCUX\_LPADC\_CH18A (0x12)

[ 47](mcux-lpadc_8h.md#af46b4363d312669eeecceca81893e455)#define MCUX\_LPADC\_CH18B (0x32)

[ 48](mcux-lpadc_8h.md#a462dec0b5baecf4c7a1161879a3ceab7)#define MCUX\_LPADC\_CH19A (0x13)

[ 49](mcux-lpadc_8h.md#a2fe255b080796372760ffabfad260b1a)#define MCUX\_LPADC\_CH19B (0x33)

[ 50](mcux-lpadc_8h.md#ac6697cc5e17f756eb0bc44b063e94dd7)#define MCUX\_LPADC\_CH20A (0x14)

[ 51](mcux-lpadc_8h.md#a3c433dce614e61a37323feb123635e0c)#define MCUX\_LPADC\_CH20B (0x34)

[ 52](mcux-lpadc_8h.md#a67056ef012f0f926a63005369e41ce4d)#define MCUX\_LPADC\_CH21A (0x15)

[ 53](mcux-lpadc_8h.md#a84ab5f5d79a02f36054fe7f2b0265a09)#define MCUX\_LPADC\_CH21B (0x35)

[ 54](mcux-lpadc_8h.md#a1fe0e9c2ffd3c941815a4d6fed0ce233)#define MCUX\_LPADC\_CH22A (0x16)

[ 55](mcux-lpadc_8h.md#a3c28c51373cb481ca3eb7c0c31dafb33)#define MCUX\_LPADC\_CH22B (0x36)

[ 56](mcux-lpadc_8h.md#afa8b45b7d77dbc2ce93890fc5ca05f12)#define MCUX\_LPADC\_CH23A (0x17)

[ 57](mcux-lpadc_8h.md#a72607f0e984e34beb37a98650d037f50)#define MCUX\_LPADC\_CH23B (0x37)

[ 58](mcux-lpadc_8h.md#a4cbde5430d43ab899435aab4d3cd833f)#define MCUX\_LPADC\_CH24A (0x18)

[ 59](mcux-lpadc_8h.md#a8ae92abb32e4a96b55e9b58612331ada)#define MCUX\_LPADC\_CH24B (0x38)

[ 60](mcux-lpadc_8h.md#adff83db9a1e8d2b41e11909484737533)#define MCUX\_LPADC\_CH25A (0x19)

[ 61](mcux-lpadc_8h.md#a00f40b9ec19a91e28a78927a0457733a)#define MCUX\_LPADC\_CH25B (0x39)

[ 62](mcux-lpadc_8h.md#a087da89d395083d39c0354515cf5138a)#define MCUX\_LPADC\_CH26A (0x1A)

[ 63](mcux-lpadc_8h.md#aab25fad7eb3d0a732cb0de779281dd8c)#define MCUX\_LPADC\_CH26B (0x3A)

[ 64](mcux-lpadc_8h.md#aae521c996ef50eb0423e00cf3347fe71)#define MCUX\_LPADC\_CH27A (0x1B)

[ 65](mcux-lpadc_8h.md#ad203a1e248e5395654355402f8860d96)#define MCUX\_LPADC\_CH27B (0x3B)

[ 66](mcux-lpadc_8h.md#a494887a6475b41db4afbd0a382722098)#define MCUX\_LPADC\_CH28A (0x1C)

[ 67](mcux-lpadc_8h.md#a2a4a03515cbb58c1a45601e6133c45cc)#define MCUX\_LPADC\_CH28B (0x3C)

[ 68](mcux-lpadc_8h.md#a308a53f7001bcd816133e065e39afe27)#define MCUX\_LPADC\_CH29A (0x1D)

[ 69](mcux-lpadc_8h.md#a86f2b6b306581b18891cef5d5070798b)#define MCUX\_LPADC\_CH29B (0x3D)

[ 70](mcux-lpadc_8h.md#a9d1a416e88b600f18a0f7deb31d57462)#define MCUX\_LPADC\_CH30A (0x1E)

[ 71](mcux-lpadc_8h.md#abada287937fa7b66e0001257487825fa)#define MCUX\_LPADC\_CH30B (0x3E)

[ 72](mcux-lpadc_8h.md#a895f8fb3d5ad4e481912553f9dc107cd)#define MCUX\_LPADC\_CH31A (0x1F)

[ 73](mcux-lpadc_8h.md#a829dda615f966e4599e8c823234b4810)#define MCUX\_LPADC\_CH31B (0x3F)

74

75

76#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_MCUX\_LPADC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [mcux-lpadc.h](mcux-lpadc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
