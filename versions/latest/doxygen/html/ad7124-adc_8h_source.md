---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ad7124-adc_8h_source.html
original_path: doxygen/html/ad7124-adc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ad7124-adc.h

[Go to the documentation of this file.](ad7124-adc_8h.md)

1/\*

2 \* Copyright (c) 2025 Analog Devices, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_AD7124\_ADC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_AD7124\_ADC\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

[ 12](ad7124-adc_8h.md#a6312e3a816c008e05692389b5ba9fc25)#define AD7124\_ADC\_AIN0 0

[ 13](ad7124-adc_8h.md#a33096ef41c79991e8ebfe82e05b018c9)#define AD7124\_ADC\_AIN1 1

[ 14](ad7124-adc_8h.md#a9406531ce59dd4b13b759427a2eaeb49)#define AD7124\_ADC\_AIN2 2

[ 15](ad7124-adc_8h.md#a828876987768deb0559d986e06c13649)#define AD7124\_ADC\_AIN3 3

[ 16](ad7124-adc_8h.md#a2d221e304e19cf7c227d4174dc37c0c8)#define AD7124\_ADC\_AIN4 4

[ 17](ad7124-adc_8h.md#a818fe0e9dbc9d684c892d7b02b5fe6ea)#define AD7124\_ADC\_AIN5 5

[ 18](ad7124-adc_8h.md#a9122caa8b9d39995cfe4d677100e8850)#define AD7124\_ADC\_AIN6 6

[ 19](ad7124-adc_8h.md#a671dad3baaec4b0e27222700bee2bb41)#define AD7124\_ADC\_AIN7 7

[ 20](ad7124-adc_8h.md#a85ca84d4fe855583c1e8ffa59f2a8920)#define AD7124\_ADC\_AIN8 8

[ 21](ad7124-adc_8h.md#a51cea76af6e456092ccaa0ad8da67106)#define AD7124\_ADC\_AIN9 9

[ 22](ad7124-adc_8h.md#a46a6fef1b8c610f00ff128de0e17189e)#define AD7124\_ADC\_AIN10 10

[ 23](ad7124-adc_8h.md#a1e85ee6b488ce5f0081c326096f9c52c)#define AD7124\_ADC\_AIN11 11

[ 24](ad7124-adc_8h.md#af44fb3b346b6e71719ca0df21c007ca4)#define AD7124\_ADC\_AIN12 12

[ 25](ad7124-adc_8h.md#a8fb7fe130ab2b303eafd94f6eb196962)#define AD7124\_ADC\_AIN13 13

[ 26](ad7124-adc_8h.md#a2e4d52044732e9ecbb1653a6fc0c2a1a)#define AD7124\_ADC\_AIN14 14

[ 27](ad7124-adc_8h.md#aa0218140489b3911b046c15998e51b67)#define AD7124\_ADC\_AIN15 15

[ 28](ad7124-adc_8h.md#a9cad5582baffdb6568f25a8657e38fd4)#define AD7124\_ADC\_TEMP\_SENSOR 16

[ 29](ad7124-adc_8h.md#aaeb3e70bcc817bea49d1a0673a56b053)#define AD7124\_ADC\_AVSS 17

[ 30](ad7124-adc_8h.md#ac43403cccdf601dd48ab0e82295dd728)#define AD7124\_ADC\_INTERNAL\_REF 18

[ 31](ad7124-adc_8h.md#a76d9d6beb56c2818cf1ff6a2cd67c666)#define AD7124\_ADC\_DGND 19

[ 32](ad7124-adc_8h.md#ac37f8dc65d46cf1f3f37f35e367f6516)#define AD7124\_ADC\_AVDD\_AVSS\_DIV6\_PLUS 20

[ 33](ad7124-adc_8h.md#ab4c95db10a382518ab538a7b40e8bad9)#define AD7124\_ADC\_AVDD\_AVSS\_DIV6\_MINUS 21

[ 34](ad7124-adc_8h.md#af08eb2218a06687b1521ca77c7843b0a)#define AD7124\_ADC\_IOVDD\_DGND\_DIV6\_PLUS 22

[ 35](ad7124-adc_8h.md#a8e5d9addfecdfb02657fa6df2b27dc7b)#define AD7124\_ADC\_IOVDD\_DGND\_DIV6\_MINUS 23

[ 36](ad7124-adc_8h.md#a310abc9ea4b791ac6cf037b2a77002d7)#define AD7124\_ADC\_ALDO\_AVSS\_DIV6\_PLUS 24

[ 37](ad7124-adc_8h.md#a9c8291212d59895bfbf489412f6690b0)#define AD7124\_ADC\_ALDO\_AVSS\_DIV6\_MINUS 25

[ 38](ad7124-adc_8h.md#a0020b1e0ad817c01040385bc94f13958)#define AD7124\_ADC\_DLDO\_DGND\_DIV6\_PLUS 26

[ 39](ad7124-adc_8h.md#a4f075c2816b81a534bc61d40b756c644)#define AD7124\_ADC\_DLDO\_DGND\_DIV6\_MINUS 27

[ 40](ad7124-adc_8h.md#a5944869f8e6c674d29d52cfa591e58cd)#define AD7124\_ADC\_V\_20MV\_P 28

[ 41](ad7124-adc_8h.md#af516b0a3e49d8da22fd84687464ef668)#define AD7124\_ADC\_V\_20MV\_M 29

42

[ 43](ad7124-adc_8h.md#a9c89788e48c0165b7ca7c4bc328c4e9d)#define AD7124\_IOUT0\_OFF 00

[ 44](ad7124-adc_8h.md#abdcbfbdf8b740651d2e77773b248156e)#define AD7124\_IOUT0\_50\_UA 01

[ 45](ad7124-adc_8h.md#a833ee271e53ee984c00880ead4c1aaf1)#define AD7124\_IOUT0\_100\_UA 02

[ 46](ad7124-adc_8h.md#a912a68d6d9e029e77a6ab20eec7d2966)#define AD7124\_IOUT0\_250\_UA 03

[ 47](ad7124-adc_8h.md#aee2744053b108a098c34b52c6591a79a)#define AD7124\_IOUT0\_500\_UA 04

[ 48](ad7124-adc_8h.md#a69243128aa9e2c39e0a3754d13f1e149)#define AD7124\_IOUT0\_750\_UA 05

[ 49](ad7124-adc_8h.md#aa222160b1c51733f2276f2147d3105d8)#define AD7124\_IOUT0\_1000\_UA 06

[ 50](ad7124-adc_8h.md#abd8d7f4951124177ba1e74d0813a30b5)#define AD7124\_IOUT0\_0\_1\_UA 07

[ 51](ad7124-adc_8h.md#a06e443e7375768ff81004e68dcf80ea7)#define AD7124\_IOUT1\_OFF 08

[ 52](ad7124-adc_8h.md#a8cfde69a11e3fb1d4193a0a1ed3541c8)#define AD7124\_IOUT1\_50\_UA 09

[ 53](ad7124-adc_8h.md#a3df72c9cdb96247b7b040aeab65d13b4)#define AD7124\_IOUT1\_100\_UA 0A

[ 54](ad7124-adc_8h.md#a11bfec89fdb9be6d0bcc63b191eb10dc)#define AD7124\_IOUT1\_250\_UA 0B

[ 55](ad7124-adc_8h.md#ac79e93e189415fa74db46bb47313770c)#define AD7124\_IOUT1\_500\_UA 0C

[ 56](ad7124-adc_8h.md#a123abd42f1d66190fe1b9035a9cccc4a)#define AD7124\_IOUT1\_750\_UA 0D

[ 57](ad7124-adc_8h.md#afc2e95abbc0dc3dc1a73e11bb9d09486)#define AD7124\_IOUT1\_1000\_UA 0E

[ 58](ad7124-adc_8h.md#a18c909ae5f9c7f100cc279ef6f69e2a8)#define AD7124\_IOUT1\_0\_1\_UA 0F

59

[ 60](ad7124-adc_8h.md#a3c0c2b2c6b01f18ad7eafd4f8a31facc)#define AD7124\_IOUT\_CH\_AIN0 00

[ 61](ad7124-adc_8h.md#ac24f0366143cddd12689015395d603c6)#define AD7124\_IOUT\_CH\_AIN1 01

[ 62](ad7124-adc_8h.md#a349dd891ee7426f444bc9d7bdbacb4a3)#define AD7124\_IOUT\_CH\_AIN2 04

[ 63](ad7124-adc_8h.md#a4cf86f478e20b2373b0b725dbbea8d99)#define AD7124\_IOUT\_CH\_AIN3 05

[ 64](ad7124-adc_8h.md#a1a83d7bfcb6b32d4cdcaf400044ce811)#define AD7124\_IOUT\_CH\_AIN4 0A

[ 65](ad7124-adc_8h.md#aaa31007f86b23b572c872432ecf2802e)#define AD7124\_IOUT\_CH\_AIN5 0B

[ 66](ad7124-adc_8h.md#a6d4790cedd6d434071bfbe18dcab311a)#define AD7124\_IOUT\_CH\_AIN6 0E

[ 67](ad7124-adc_8h.md#accdb5043de22b0a66c5982876cc23b92)#define AD7124\_IOUT\_CH\_AIN7 0F

68

69#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_AD7124\_ADC\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [ad7124-adc.h](ad7124-adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
