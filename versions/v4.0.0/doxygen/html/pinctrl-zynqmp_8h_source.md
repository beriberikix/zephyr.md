---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/pinctrl-zynqmp_8h_source.html
original_path: doxygen/html/pinctrl-zynqmp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-zynqmp.h

[Go to the documentation of this file.](pinctrl-zynqmp_8h.md)

1/\*

2 \* Copyright (c) 2024 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ZYNQMP\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_ZYNQMP\_PINCTRL\_H\_

9

10/\*

11 \* The offset is defined at `pictrl\_soc.h` for the ZynqMP platform

12 \*/

[ 13](pinctrl-zynqmp_8h.md#a53faf9f7be70b2c114ad20e212e8620f)#define FUNCTION\_OFFSET 8

[ 14](pinctrl-zynqmp_8h.md#a66ff19498534d4dd91a63dab163f4273)#define UART\_FUNCTION 0x1

15

16/\*

17 \* For functions that can be selected for a subset of MIO pins,

18 \* specific macro identifiers were generated to avoid complex checking

19 \* logic at compile time. For more generalized applications existing on

20 \* every pin (eg. GPIO), a generic macro function to generate a driver-compliant

21 \* selector value can be used.

22 \*/

23

[ 24](pinctrl-zynqmp_8h.md#ae3b05cf3307ba4427320cd92a999b63e)#define UART0\_RX\_2 (2U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 25](pinctrl-zynqmp_8h.md#ac11ea9c2605b98161852a308278db324)#define UART0\_RX\_6 (6U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 26](pinctrl-zynqmp_8h.md#a4fc7b024f70bbae43f2c3cab64575b2f)#define UART0\_RX\_10 (10U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 27](pinctrl-zynqmp_8h.md#ac51c9c43c25162a8986a895b0e766430)#define UART0\_RX\_14 (14U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 28](pinctrl-zynqmp_8h.md#a94bafac8daee9e349986b145a24d485c)#define UART0\_RX\_18 (18U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 29](pinctrl-zynqmp_8h.md#a0553289cf5c7c148b1a93b9021eecf6d)#define UART0\_RX\_22 (22U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 30](pinctrl-zynqmp_8h.md#ab21d419ca0aeb772692cb6fc8df439ef)#define UART0\_RX\_26 (26U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 31](pinctrl-zynqmp_8h.md#a64ef9671aca9b854bb1bdb14c9eabff7)#define UART0\_RX\_30 (30U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 32](pinctrl-zynqmp_8h.md#a4d97ffbc37fbb00c0dce85ba02fbc160)#define UART0\_RX\_34 (34U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 33](pinctrl-zynqmp_8h.md#a5b405d032cdd29e8374a8dcacf098a11)#define UART0\_RX\_38 (38U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 34](pinctrl-zynqmp_8h.md#a876fcba49abdc5f2837011a7a7bf5adc)#define UART0\_RX\_42 (42U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 35](pinctrl-zynqmp_8h.md#a0eb8b08818c5536bfcd0c69750efdbf0)#define UART0\_RX\_46 (46U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 36](pinctrl-zynqmp_8h.md#a9d0b8da00645795d168350a6fcf75acc)#define UART0\_RX\_50 (50U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 37](pinctrl-zynqmp_8h.md#a03b12d0b221bcd69d2cde06c809b473e)#define UART0\_RX\_54 (54U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 38](pinctrl-zynqmp_8h.md#a18d89b9fcdda2efac3b85bdb6fc2300d)#define UART0\_RX\_58 (58U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 39](pinctrl-zynqmp_8h.md#a73a0eebda596fa885b625753a130388d)#define UART0\_RX\_62 (62U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 40](pinctrl-zynqmp_8h.md#a3ee4c2f00d77bd0488c0dcf64929ae2b)#define UART0\_RX\_66 (66U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 41](pinctrl-zynqmp_8h.md#a859dd61e4bba83affb5cd267dda62e1c)#define UART0\_RX\_70 (70U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 42](pinctrl-zynqmp_8h.md#ad0c049a883bb4eb2f825fc88cdfa988f)#define UART0\_RX\_74 (74U | (UART\_FUNCTION << FUNCTION\_OFFSET))

43

[ 44](pinctrl-zynqmp_8h.md#a5f20ede1f80dc455700541095d741a2b)#define UART0\_TX\_3 (3U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 45](pinctrl-zynqmp_8h.md#a3f1bfd6f1e71a04365480025caf70ada)#define UART0\_TX\_7 (7U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 46](pinctrl-zynqmp_8h.md#a03f1df6ed6e160fe5c12b0b224726365)#define UART0\_TX\_11 (11U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 47](pinctrl-zynqmp_8h.md#a24f0e8a01437ef398f979f9e2caa0610)#define UART0\_TX\_15 (15U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 48](pinctrl-zynqmp_8h.md#aab1363a433f7b3ab0b50058986959ec6)#define UART0\_TX\_19 (19U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 49](pinctrl-zynqmp_8h.md#a7017bf0a1bd815c383d6543d5b691715)#define UART0\_TX\_23 (23U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 50](pinctrl-zynqmp_8h.md#a275af0b7b0a2499b122585721cf3e952)#define UART0\_TX\_27 (27U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 51](pinctrl-zynqmp_8h.md#a390ff60b5e538d16508f5c4528c62289)#define UART0\_TX\_31 (31U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 52](pinctrl-zynqmp_8h.md#ac2246f632065d04d173e8fa32a99920d)#define UART0\_TX\_35 (35U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 53](pinctrl-zynqmp_8h.md#a24325ec75563c9d3a0eac0131a9e470c)#define UART0\_TX\_39 (39U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 54](pinctrl-zynqmp_8h.md#a6b2183af29f97dbc75fc34dc836db3cf)#define UART0\_TX\_43 (43U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 55](pinctrl-zynqmp_8h.md#a3f8cbb1e443fc46d454c3f8c6c7efb18)#define UART0\_TX\_47 (47U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 56](pinctrl-zynqmp_8h.md#aeb2759f0f41457673c382d5b5d19a1f6)#define UART0\_TX\_51 (51U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 57](pinctrl-zynqmp_8h.md#adcbdd40e5bbe0270622af50e69142f0f)#define UART0\_TX\_55 (55U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 58](pinctrl-zynqmp_8h.md#ad6fe9d50e598be94c647198a10cadd67)#define UART0\_TX\_59 (59U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 59](pinctrl-zynqmp_8h.md#a186764e58e34a2ac02ffc7901385d6d5)#define UART0\_TX\_63 (63U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 60](pinctrl-zynqmp_8h.md#a86ec25b538b48337d76be9665976d346)#define UART0\_TX\_67 (67U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 61](pinctrl-zynqmp_8h.md#a3bd3add575e491325113296e5fd4077b)#define UART0\_TX\_71 (71U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 62](pinctrl-zynqmp_8h.md#a15b2ff8f1cea88c33a1392856ee8c19d)#define UART0\_TX\_75 (75U | (UART\_FUNCTION << FUNCTION\_OFFSET))

63

[ 64](pinctrl-zynqmp_8h.md#aba32a8118cbd277fdf2199baa2b18689)#define UART1\_RX\_1 (1U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 65](pinctrl-zynqmp_8h.md#a0b15040770c968874f0cce27baa34f36)#define UART1\_RX\_5 (5U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 66](pinctrl-zynqmp_8h.md#a1d65c19b30514a96b1d30c6e4b247942)#define UART1\_RX\_9 (9U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 67](pinctrl-zynqmp_8h.md#a0b7ff741f9e3adfcb52645cf3c48aefb)#define UART1\_RX\_13 (13U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 68](pinctrl-zynqmp_8h.md#adbb61b6019c618cd19696f9988379c52)#define UART1\_RX\_17 (17U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 69](pinctrl-zynqmp_8h.md#aa875d776984716ba276abcfc566d66ba)#define UART1\_RX\_21 (21U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 70](pinctrl-zynqmp_8h.md#a8b3995a5f3964c612b38ee7dc63466bd)#define UART1\_RX\_25 (25U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 71](pinctrl-zynqmp_8h.md#a803c7cd9da95fb5bd45da2692bfa3353)#define UART1\_RX\_29 (29U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 72](pinctrl-zynqmp_8h.md#a23b8475700f5000642e21761eb348daa)#define UART1\_RX\_33 (33U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 73](pinctrl-zynqmp_8h.md#af5066291353d29b31379a0bc03c51baf)#define UART1\_RX\_37 (37U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 74](pinctrl-zynqmp_8h.md#ab6fe8abc64c0efbf1359922cdb5e1ac2)#define UART1\_RX\_41 (41U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 75](pinctrl-zynqmp_8h.md#a930cb710ab9cdf9c5e87f8abbc6f75ff)#define UART1\_RX\_45 (45U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 76](pinctrl-zynqmp_8h.md#ab38faddb3e676dd4957bebb294e226ee)#define UART1\_RX\_49 (49U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 77](pinctrl-zynqmp_8h.md#af41c512a2899a3ecba52d04d1191ba60)#define UART1\_RX\_53 (53U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 78](pinctrl-zynqmp_8h.md#a69240a2dc36df4c8402028fa7e0be1e9)#define UART1\_RX\_57 (57U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 79](pinctrl-zynqmp_8h.md#ac739b0cc0710eae1157d367f754abb4b)#define UART1\_RX\_61 (61U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 80](pinctrl-zynqmp_8h.md#a2511e68fb1e3f238da9fcc910f88bc40)#define UART1\_RX\_65 (65U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 81](pinctrl-zynqmp_8h.md#aadb4d413fc9de0f2ae83c94de71561d7)#define UART1\_RX\_69 (69U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 82](pinctrl-zynqmp_8h.md#a95edf3d75fc8c8135e3d3002318702d6)#define UART1\_RX\_73 (73U | (UART\_FUNCTION << FUNCTION\_OFFSET))

83

[ 84](pinctrl-zynqmp_8h.md#a3f11b070f7c8bba83a1217695e16cb1f)#define UART1\_TX\_0 (0U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 85](pinctrl-zynqmp_8h.md#a67761aee291eeaa6abd3d77b6b2e6f6d)#define UART1\_TX\_4 (4U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 86](pinctrl-zynqmp_8h.md#ae3695f574de1574ea6c2ba554762626b)#define UART1\_TX\_8 (8U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 87](pinctrl-zynqmp_8h.md#a0c42d153f18c42b6f0b716aed6761bca)#define UART1\_TX\_12 (12U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 88](pinctrl-zynqmp_8h.md#a35a49b80752440596828c7a3bdfc2e87)#define UART1\_TX\_16 (16U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 89](pinctrl-zynqmp_8h.md#af5c1a691e3471608e532abfe98ea1d11)#define UART1\_TX\_20 (20U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 90](pinctrl-zynqmp_8h.md#a7ec4a3035515c478a4dc093cebc60eb8)#define UART1\_TX\_24 (24U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 91](pinctrl-zynqmp_8h.md#a1f0e76a42da8163c7e7bff86612e366b)#define UART1\_TX\_28 (28U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 92](pinctrl-zynqmp_8h.md#a781dd511c3a1e601a44f60f80479debf)#define UART1\_TX\_32 (32U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 93](pinctrl-zynqmp_8h.md#aa290345d3cedc8f1299fe2d3d9e014ee)#define UART1\_TX\_36 (36U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 94](pinctrl-zynqmp_8h.md#a214f1e36e970e36250130cfa81f5b06c)#define UART1\_TX\_40 (40U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 95](pinctrl-zynqmp_8h.md#a37b24d04f0ea4cc6153d9ec452d080e4)#define UART1\_TX\_44 (44U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 96](pinctrl-zynqmp_8h.md#a492a80c613d0506480cd854b56bf70ea)#define UART1\_TX\_48 (28U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 97](pinctrl-zynqmp_8h.md#ae6715ff78b6d27cbc1450ec819cf500b)#define UART1\_TX\_52 (52U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 98](pinctrl-zynqmp_8h.md#a047d0806a17e386b7eb3d68360069f43)#define UART1\_TX\_56 (56U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 99](pinctrl-zynqmp_8h.md#a672a312e2dcaa2dcdf3c5c0dc3eebbd1)#define UART1\_TX\_60 (60U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 100](pinctrl-zynqmp_8h.md#ac478a9ec2b9a73b19ecf238737c0d258)#define UART1\_TX\_64 (64U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 101](pinctrl-zynqmp_8h.md#a6908a697731ededdd82f9c4fa2a752f4)#define UART1\_TX\_68 (28U | (UART\_FUNCTION << FUNCTION\_OFFSET))

[ 102](pinctrl-zynqmp_8h.md#af7a60ed86a32f60a38ee6738777ce179)#define UART1\_TX\_72 (72U | (UART\_FUNCTION << FUNCTION\_OFFSET))

103

104#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [pinctrl-zynqmp.h](pinctrl-zynqmp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
