---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ad7124-adc_8h.html
original_path: doxygen/html/ad7124-adc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ad7124-adc.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](ad7124-adc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [AD7124\_ADC\_AIN0](#a6312e3a816c008e05692389b5ba9fc25)   0 |
| #define | [AD7124\_ADC\_AIN1](#a33096ef41c79991e8ebfe82e05b018c9)   1 |
| #define | [AD7124\_ADC\_AIN2](#a9406531ce59dd4b13b759427a2eaeb49)   2 |
| #define | [AD7124\_ADC\_AIN3](#a828876987768deb0559d986e06c13649)   3 |
| #define | [AD7124\_ADC\_AIN4](#a2d221e304e19cf7c227d4174dc37c0c8)   4 |
| #define | [AD7124\_ADC\_AIN5](#a818fe0e9dbc9d684c892d7b02b5fe6ea)   5 |
| #define | [AD7124\_ADC\_AIN6](#a9122caa8b9d39995cfe4d677100e8850)   6 |
| #define | [AD7124\_ADC\_AIN7](#a671dad3baaec4b0e27222700bee2bb41)   7 |
| #define | [AD7124\_ADC\_AIN8](#a85ca84d4fe855583c1e8ffa59f2a8920)   8 |
| #define | [AD7124\_ADC\_AIN9](#a51cea76af6e456092ccaa0ad8da67106)   9 |
| #define | [AD7124\_ADC\_AIN10](#a46a6fef1b8c610f00ff128de0e17189e)   10 |
| #define | [AD7124\_ADC\_AIN11](#a1e85ee6b488ce5f0081c326096f9c52c)   11 |
| #define | [AD7124\_ADC\_AIN12](#af44fb3b346b6e71719ca0df21c007ca4)   12 |
| #define | [AD7124\_ADC\_AIN13](#a8fb7fe130ab2b303eafd94f6eb196962)   13 |
| #define | [AD7124\_ADC\_AIN14](#a2e4d52044732e9ecbb1653a6fc0c2a1a)   14 |
| #define | [AD7124\_ADC\_AIN15](#aa0218140489b3911b046c15998e51b67)   15 |
| #define | [AD7124\_ADC\_TEMP\_SENSOR](#a9cad5582baffdb6568f25a8657e38fd4)   16 |
| #define | [AD7124\_ADC\_AVSS](#aaeb3e70bcc817bea49d1a0673a56b053)   17 |
| #define | [AD7124\_ADC\_INTERNAL\_REF](#ac43403cccdf601dd48ab0e82295dd728)   18 |
| #define | [AD7124\_ADC\_DGND](#a76d9d6beb56c2818cf1ff6a2cd67c666)   19 |
| #define | [AD7124\_ADC\_AVDD\_AVSS\_DIV6\_PLUS](#ac37f8dc65d46cf1f3f37f35e367f6516)   20 |
| #define | [AD7124\_ADC\_AVDD\_AVSS\_DIV6\_MINUS](#ab4c95db10a382518ab538a7b40e8bad9)   21 |
| #define | [AD7124\_ADC\_IOVDD\_DGND\_DIV6\_PLUS](#af08eb2218a06687b1521ca77c7843b0a)   22 |
| #define | [AD7124\_ADC\_IOVDD\_DGND\_DIV6\_MINUS](#a8e5d9addfecdfb02657fa6df2b27dc7b)   23 |
| #define | [AD7124\_ADC\_ALDO\_AVSS\_DIV6\_PLUS](#a310abc9ea4b791ac6cf037b2a77002d7)   24 |
| #define | [AD7124\_ADC\_ALDO\_AVSS\_DIV6\_MINUS](#a9c8291212d59895bfbf489412f6690b0)   25 |
| #define | [AD7124\_ADC\_DLDO\_DGND\_DIV6\_PLUS](#a0020b1e0ad817c01040385bc94f13958)   26 |
| #define | [AD7124\_ADC\_DLDO\_DGND\_DIV6\_MINUS](#a4f075c2816b81a534bc61d40b756c644)   27 |
| #define | [AD7124\_ADC\_V\_20MV\_P](#a5944869f8e6c674d29d52cfa591e58cd)   28 |
| #define | [AD7124\_ADC\_V\_20MV\_M](#af516b0a3e49d8da22fd84687464ef668)   29 |
| #define | [AD7124\_IOUT0\_OFF](#a9c89788e48c0165b7ca7c4bc328c4e9d)   00 |
| #define | [AD7124\_IOUT0\_50\_UA](#abdcbfbdf8b740651d2e77773b248156e)   01 |
| #define | [AD7124\_IOUT0\_100\_UA](#a833ee271e53ee984c00880ead4c1aaf1)   02 |
| #define | [AD7124\_IOUT0\_250\_UA](#a912a68d6d9e029e77a6ab20eec7d2966)   03 |
| #define | [AD7124\_IOUT0\_500\_UA](#aee2744053b108a098c34b52c6591a79a)   04 |
| #define | [AD7124\_IOUT0\_750\_UA](#a69243128aa9e2c39e0a3754d13f1e149)   05 |
| #define | [AD7124\_IOUT0\_1000\_UA](#aa222160b1c51733f2276f2147d3105d8)   06 |
| #define | [AD7124\_IOUT0\_0\_1\_UA](#abd8d7f4951124177ba1e74d0813a30b5)   07 |
| #define | [AD7124\_IOUT1\_OFF](#a06e443e7375768ff81004e68dcf80ea7)   08 |
| #define | [AD7124\_IOUT1\_50\_UA](#a8cfde69a11e3fb1d4193a0a1ed3541c8)   09 |
| #define | [AD7124\_IOUT1\_100\_UA](#a3df72c9cdb96247b7b040aeab65d13b4)   0A |
| #define | [AD7124\_IOUT1\_250\_UA](#a11bfec89fdb9be6d0bcc63b191eb10dc)   0B |
| #define | [AD7124\_IOUT1\_500\_UA](#ac79e93e189415fa74db46bb47313770c)   0C |
| #define | [AD7124\_IOUT1\_750\_UA](#a123abd42f1d66190fe1b9035a9cccc4a)   0D |
| #define | [AD7124\_IOUT1\_1000\_UA](#afc2e95abbc0dc3dc1a73e11bb9d09486)   0E |
| #define | [AD7124\_IOUT1\_0\_1\_UA](#a18c909ae5f9c7f100cc279ef6f69e2a8)   0F |
| #define | [AD7124\_IOUT\_CH\_AIN0](#a3c0c2b2c6b01f18ad7eafd4f8a31facc)   00 |
| #define | [AD7124\_IOUT\_CH\_AIN1](#ac24f0366143cddd12689015395d603c6)   01 |
| #define | [AD7124\_IOUT\_CH\_AIN2](#a349dd891ee7426f444bc9d7bdbacb4a3)   04 |
| #define | [AD7124\_IOUT\_CH\_AIN3](#a4cf86f478e20b2373b0b725dbbea8d99)   05 |
| #define | [AD7124\_IOUT\_CH\_AIN4](#a1a83d7bfcb6b32d4cdcaf400044ce811)   0A |
| #define | [AD7124\_IOUT\_CH\_AIN5](#aaa31007f86b23b572c872432ecf2802e)   0B |
| #define | [AD7124\_IOUT\_CH\_AIN6](#a6d4790cedd6d434071bfbe18dcab311a)   0E |
| #define | [AD7124\_IOUT\_CH\_AIN7](#accdb5043de22b0a66c5982876cc23b92)   0F |

## Macro Definition Documentation

## [◆ ](#a6312e3a816c008e05692389b5ba9fc25)AD7124\_ADC\_AIN0

| #define AD7124\_ADC\_AIN0   0 |
| --- |

## [◆ ](#a33096ef41c79991e8ebfe82e05b018c9)AD7124\_ADC\_AIN1

| #define AD7124\_ADC\_AIN1   1 |
| --- |

## [◆ ](#a46a6fef1b8c610f00ff128de0e17189e)AD7124\_ADC\_AIN10

| #define AD7124\_ADC\_AIN10   10 |
| --- |

## [◆ ](#a1e85ee6b488ce5f0081c326096f9c52c)AD7124\_ADC\_AIN11

| #define AD7124\_ADC\_AIN11   11 |
| --- |

## [◆ ](#af44fb3b346b6e71719ca0df21c007ca4)AD7124\_ADC\_AIN12

| #define AD7124\_ADC\_AIN12   12 |
| --- |

## [◆ ](#a8fb7fe130ab2b303eafd94f6eb196962)AD7124\_ADC\_AIN13

| #define AD7124\_ADC\_AIN13   13 |
| --- |

## [◆ ](#a2e4d52044732e9ecbb1653a6fc0c2a1a)AD7124\_ADC\_AIN14

| #define AD7124\_ADC\_AIN14   14 |
| --- |

## [◆ ](#aa0218140489b3911b046c15998e51b67)AD7124\_ADC\_AIN15

| #define AD7124\_ADC\_AIN15   15 |
| --- |

## [◆ ](#a9406531ce59dd4b13b759427a2eaeb49)AD7124\_ADC\_AIN2

| #define AD7124\_ADC\_AIN2   2 |
| --- |

## [◆ ](#a828876987768deb0559d986e06c13649)AD7124\_ADC\_AIN3

| #define AD7124\_ADC\_AIN3   3 |
| --- |

## [◆ ](#a2d221e304e19cf7c227d4174dc37c0c8)AD7124\_ADC\_AIN4

| #define AD7124\_ADC\_AIN4   4 |
| --- |

## [◆ ](#a818fe0e9dbc9d684c892d7b02b5fe6ea)AD7124\_ADC\_AIN5

| #define AD7124\_ADC\_AIN5   5 |
| --- |

## [◆ ](#a9122caa8b9d39995cfe4d677100e8850)AD7124\_ADC\_AIN6

| #define AD7124\_ADC\_AIN6   6 |
| --- |

## [◆ ](#a671dad3baaec4b0e27222700bee2bb41)AD7124\_ADC\_AIN7

| #define AD7124\_ADC\_AIN7   7 |
| --- |

## [◆ ](#a85ca84d4fe855583c1e8ffa59f2a8920)AD7124\_ADC\_AIN8

| #define AD7124\_ADC\_AIN8   8 |
| --- |

## [◆ ](#a51cea76af6e456092ccaa0ad8da67106)AD7124\_ADC\_AIN9

| #define AD7124\_ADC\_AIN9   9 |
| --- |

## [◆ ](#a9c8291212d59895bfbf489412f6690b0)AD7124\_ADC\_ALDO\_AVSS\_DIV6\_MINUS

| #define AD7124\_ADC\_ALDO\_AVSS\_DIV6\_MINUS   25 |
| --- |

## [◆ ](#a310abc9ea4b791ac6cf037b2a77002d7)AD7124\_ADC\_ALDO\_AVSS\_DIV6\_PLUS

| #define AD7124\_ADC\_ALDO\_AVSS\_DIV6\_PLUS   24 |
| --- |

## [◆ ](#ab4c95db10a382518ab538a7b40e8bad9)AD7124\_ADC\_AVDD\_AVSS\_DIV6\_MINUS

| #define AD7124\_ADC\_AVDD\_AVSS\_DIV6\_MINUS   21 |
| --- |

## [◆ ](#ac37f8dc65d46cf1f3f37f35e367f6516)AD7124\_ADC\_AVDD\_AVSS\_DIV6\_PLUS

| #define AD7124\_ADC\_AVDD\_AVSS\_DIV6\_PLUS   20 |
| --- |

## [◆ ](#aaeb3e70bcc817bea49d1a0673a56b053)AD7124\_ADC\_AVSS

| #define AD7124\_ADC\_AVSS   17 |
| --- |

## [◆ ](#a76d9d6beb56c2818cf1ff6a2cd67c666)AD7124\_ADC\_DGND

| #define AD7124\_ADC\_DGND   19 |
| --- |

## [◆ ](#a4f075c2816b81a534bc61d40b756c644)AD7124\_ADC\_DLDO\_DGND\_DIV6\_MINUS

| #define AD7124\_ADC\_DLDO\_DGND\_DIV6\_MINUS   27 |
| --- |

## [◆ ](#a0020b1e0ad817c01040385bc94f13958)AD7124\_ADC\_DLDO\_DGND\_DIV6\_PLUS

| #define AD7124\_ADC\_DLDO\_DGND\_DIV6\_PLUS   26 |
| --- |

## [◆ ](#ac43403cccdf601dd48ab0e82295dd728)AD7124\_ADC\_INTERNAL\_REF

| #define AD7124\_ADC\_INTERNAL\_REF   18 |
| --- |

## [◆ ](#a8e5d9addfecdfb02657fa6df2b27dc7b)AD7124\_ADC\_IOVDD\_DGND\_DIV6\_MINUS

| #define AD7124\_ADC\_IOVDD\_DGND\_DIV6\_MINUS   23 |
| --- |

## [◆ ](#af08eb2218a06687b1521ca77c7843b0a)AD7124\_ADC\_IOVDD\_DGND\_DIV6\_PLUS

| #define AD7124\_ADC\_IOVDD\_DGND\_DIV6\_PLUS   22 |
| --- |

## [◆ ](#a9cad5582baffdb6568f25a8657e38fd4)AD7124\_ADC\_TEMP\_SENSOR

| #define AD7124\_ADC\_TEMP\_SENSOR   16 |
| --- |

## [◆ ](#af516b0a3e49d8da22fd84687464ef668)AD7124\_ADC\_V\_20MV\_M

| #define AD7124\_ADC\_V\_20MV\_M   29 |
| --- |

## [◆ ](#a5944869f8e6c674d29d52cfa591e58cd)AD7124\_ADC\_V\_20MV\_P

| #define AD7124\_ADC\_V\_20MV\_P   28 |
| --- |

## [◆ ](#abd8d7f4951124177ba1e74d0813a30b5)AD7124\_IOUT0\_0\_1\_UA

| #define AD7124\_IOUT0\_0\_1\_UA   07 |
| --- |

## [◆ ](#aa222160b1c51733f2276f2147d3105d8)AD7124\_IOUT0\_1000\_UA

| #define AD7124\_IOUT0\_1000\_UA   06 |
| --- |

## [◆ ](#a833ee271e53ee984c00880ead4c1aaf1)AD7124\_IOUT0\_100\_UA

| #define AD7124\_IOUT0\_100\_UA   02 |
| --- |

## [◆ ](#a912a68d6d9e029e77a6ab20eec7d2966)AD7124\_IOUT0\_250\_UA

| #define AD7124\_IOUT0\_250\_UA   03 |
| --- |

## [◆ ](#aee2744053b108a098c34b52c6591a79a)AD7124\_IOUT0\_500\_UA

| #define AD7124\_IOUT0\_500\_UA   04 |
| --- |

## [◆ ](#abdcbfbdf8b740651d2e77773b248156e)AD7124\_IOUT0\_50\_UA

| #define AD7124\_IOUT0\_50\_UA   01 |
| --- |

## [◆ ](#a69243128aa9e2c39e0a3754d13f1e149)AD7124\_IOUT0\_750\_UA

| #define AD7124\_IOUT0\_750\_UA   05 |
| --- |

## [◆ ](#a9c89788e48c0165b7ca7c4bc328c4e9d)AD7124\_IOUT0\_OFF

| #define AD7124\_IOUT0\_OFF   00 |
| --- |

## [◆ ](#a18c909ae5f9c7f100cc279ef6f69e2a8)AD7124\_IOUT1\_0\_1\_UA

| #define AD7124\_IOUT1\_0\_1\_UA   0F |
| --- |

## [◆ ](#afc2e95abbc0dc3dc1a73e11bb9d09486)AD7124\_IOUT1\_1000\_UA

| #define AD7124\_IOUT1\_1000\_UA   0E |
| --- |

## [◆ ](#a3df72c9cdb96247b7b040aeab65d13b4)AD7124\_IOUT1\_100\_UA

| #define AD7124\_IOUT1\_100\_UA   0A |
| --- |

## [◆ ](#a11bfec89fdb9be6d0bcc63b191eb10dc)AD7124\_IOUT1\_250\_UA

| #define AD7124\_IOUT1\_250\_UA   0B |
| --- |

## [◆ ](#ac79e93e189415fa74db46bb47313770c)AD7124\_IOUT1\_500\_UA

| #define AD7124\_IOUT1\_500\_UA   0C |
| --- |

## [◆ ](#a8cfde69a11e3fb1d4193a0a1ed3541c8)AD7124\_IOUT1\_50\_UA

| #define AD7124\_IOUT1\_50\_UA   09 |
| --- |

## [◆ ](#a123abd42f1d66190fe1b9035a9cccc4a)AD7124\_IOUT1\_750\_UA

| #define AD7124\_IOUT1\_750\_UA   0D |
| --- |

## [◆ ](#a06e443e7375768ff81004e68dcf80ea7)AD7124\_IOUT1\_OFF

| #define AD7124\_IOUT1\_OFF   08 |
| --- |

## [◆ ](#a3c0c2b2c6b01f18ad7eafd4f8a31facc)AD7124\_IOUT\_CH\_AIN0

| #define AD7124\_IOUT\_CH\_AIN0   00 |
| --- |

## [◆ ](#ac24f0366143cddd12689015395d603c6)AD7124\_IOUT\_CH\_AIN1

| #define AD7124\_IOUT\_CH\_AIN1   01 |
| --- |

## [◆ ](#a349dd891ee7426f444bc9d7bdbacb4a3)AD7124\_IOUT\_CH\_AIN2

| #define AD7124\_IOUT\_CH\_AIN2   04 |
| --- |

## [◆ ](#a4cf86f478e20b2373b0b725dbbea8d99)AD7124\_IOUT\_CH\_AIN3

| #define AD7124\_IOUT\_CH\_AIN3   05 |
| --- |

## [◆ ](#a1a83d7bfcb6b32d4cdcaf400044ce811)AD7124\_IOUT\_CH\_AIN4

| #define AD7124\_IOUT\_CH\_AIN4   0A |
| --- |

## [◆ ](#aaa31007f86b23b572c872432ecf2802e)AD7124\_IOUT\_CH\_AIN5

| #define AD7124\_IOUT\_CH\_AIN5   0B |
| --- |

## [◆ ](#a6d4790cedd6d434071bfbe18dcab311a)AD7124\_IOUT\_CH\_AIN6

| #define AD7124\_IOUT\_CH\_AIN6   0E |
| --- |

## [◆ ](#accdb5043de22b0a66c5982876cc23b92)AD7124\_IOUT\_CH\_AIN7

| #define AD7124\_IOUT\_CH\_AIN7   0F |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [ad7124-adc.h](ad7124-adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
