---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rza2m_8h_source.html
original_path: doxygen/html/pinctrl-rza2m_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rza2m.h

[Go to the documentation of this file.](pinctrl-rza2m_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZA2M\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZA2M\_H\_

8

[ 9](pinctrl-rza2m_8h.md#a60489d9b02b45ebc8fd95f0a7f9bcbe4)#define RZA2M\_PIN\_NUM\_IN\_PORT 8

10

11/\* Port names as labeled in the Hardware Manual \*/

[ 12](pinctrl-rza2m_8h.md#a1b0292747e92dff43d6760d9e2258869)#define PORT\_00 0

[ 13](pinctrl-rza2m_8h.md#a9de415830a2b3484dd33d5d08258dde5)#define PORT\_01 1

[ 14](pinctrl-rza2m_8h.md#a7db623b2ec3816113a8f3fb07d5428ef)#define PORT\_02 2

[ 15](pinctrl-rza2m_8h.md#a71478a4563d986886410618bc130b0d9)#define PORT\_03 3

[ 16](pinctrl-rza2m_8h.md#aed73b97fc12615ac1dec9daad9537647)#define PORT\_04 4

[ 17](pinctrl-rza2m_8h.md#a590020a2e6577d74d89bdee0989812c4)#define PORT\_05 5

[ 18](pinctrl-rza2m_8h.md#ab2912aeb54c92971e0590ff3282e775b)#define PORT\_06 6

[ 19](pinctrl-rza2m_8h.md#acabb0398db58703c47e718f899018410)#define PORT\_07 7

[ 20](pinctrl-rza2m_8h.md#a5f4d0cfbea4e649fa0863d4a8d409c5e)#define PORT\_08 8

[ 21](pinctrl-rza2m_8h.md#a5e8d840d1a1bd421615b2cc90ce0b90f)#define PORT\_09 9

[ 22](pinctrl-rza2m_8h.md#aa2513ef1f868cdfe813ba2f3cf5ae27e)#define PORT\_A 10

[ 23](pinctrl-rza2m_8h.md#ab67535e80c86be4dabdcae0f6028511d)#define PORT\_B 11

[ 24](pinctrl-rza2m_8h.md#a8b1f19a91c7a14a40f9633985d330e40)#define PORT\_C 12

[ 25](pinctrl-rza2m_8h.md#ae256d5f69ef8fdfab967632ad7b753df)#define PORT\_D 13

[ 26](pinctrl-rza2m_8h.md#a193fd9b28005073562257edd69a294e0)#define PORT\_E 14

[ 27](pinctrl-rza2m_8h.md#a2d4c473d5829b4eda4197ac6d002745f)#define PORT\_F 15

[ 28](pinctrl-rza2m_8h.md#adfd1d5035050cce1f992e24d5332f3da)#define PORT\_G 16

[ 29](pinctrl-rza2m_8h.md#a89df76f2646bce730cbe3f8d1ed89033)#define PORT\_H 17

30/\* No I \*/

[ 31](pinctrl-rza2m_8h.md#a3b384cd114f5bd23d09b8045a6ca0382)#define PORT\_J 18

[ 32](pinctrl-rza2m_8h.md#a68bfbd51d7044344dde5e1609ac7abc9)#define PORT\_K 19

[ 33](pinctrl-rza2m_8h.md#ad72ce2e5a1c36ef26b9e59a5783a0283)#define PORT\_L 20

[ 34](pinctrl-rza2m_8h.md#a1e6a0b150bcfc100a021b0376309a507)#define PORT\_M 21 /\* Pins PM\_0/1 are labeled JP\_0/1 in HW manual \*/

35

[ 36](pinctrl-rza2m_8h.md#a8e970780df1c26fc643fe5c2054ce6d6)#define PORT\_CKIO 22

[ 37](pinctrl-rza2m_8h.md#ae52bacf2b97464f6ea58f6d04c05d858)#define PORT\_PPOC 23 /\* Select between 1.8V and 3.3V for SPI and SD/MMC \*/

38

[ 39](pinctrl-rza2m_8h.md#a0b5fd24b1d023cca04915baafeb9ef43)#define PIN\_POSEL 0 /\* Sets function for POSEL0 bits. 00, 01, 10 - 1.8v, 11 - 3.3v \*/

[ 40](pinctrl-rza2m_8h.md#abd7fbd7ee1c52a0668952f7fa9317449)#define PIN\_POC2 1 /\* Sets function for SSD host 0, 0 - 1.8v 1 - 3.3v \*/

[ 41](pinctrl-rza2m_8h.md#a3aa1eb7c5a2e3fa5c8b3d2d352a40c89)#define PIN\_POC3 2 /\* Sets function for SSD host 1, 0 - 1.8v 1 - 3.3v \*/

42

43/\*

44 \* Create the pin index from its bank and position numbers and store in

45 \* the upper 16 bits the alternate function identifier

46 \*/

[ 47](pinctrl-rza2m_8h.md#a40b2ad5eef6bf7984d65b6daa89fdba6)#define RZA2M\_PINMUX(b, p, f) ((b) \* RZA2M\_PIN\_NUM\_IN\_PORT + (p) | (f << 16))

48

[ 49](pinctrl-rza2m_8h.md#a38f5c083c8df51eb5e33399041f3f071)#define CKIO\_DRV RZA2M\_PINMUX(PORT\_CKIO, 0, 0)

50

51#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RZA2M\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rza2m.h](pinctrl-rza2m_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
