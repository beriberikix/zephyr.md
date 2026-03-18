---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl-rcar-common_8h_source.html
original_path: doxygen/html/pinctrl-rcar-common_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rcar-common.h

[Go to the documentation of this file.](pinctrl-rcar-common_8h.md)

1/\*

2 \* Copyright (c) 2021-2023 IoT.bzh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RCAR\_COMMON\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RCAR\_COMMON\_H\_

9

[ 25](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)#define IPSR(bank, shift, func) (((bank) << 10U) | ((shift) << 4U) | (func))

26

27/\* Arbitrary number to encode non capable gpio pin \*/

[ 28](pinctrl-rcar-common_8h.md#a165cdeba11c616c3c14e1d02e6c4d552)#define PIN\_NOGPSR\_START 1024U

29

[ 36](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)#define RCAR\_GP\_PIN(bank, pin) (((bank) \* 32U) + (pin))

37

[ 43](pinctrl-rcar-common_8h.md#a6e8b18f9578375cb325e9e5b204b6c66)#define RCAR\_NOGP\_PIN(pin) (PIN\_NOGPSR\_START + pin)

44

45/\* Renesas Gen4 has IPSR registers at different base address

46 \* reg is here an index for the base address.

47 \* Each base address has 4 IPSR banks.

48 \*/

[ 49](pinctrl-rcar-common_8h.md#a0d4d66df6e1565e2d9f3cfdca9aa5362)#define IPnSR(bank, reg, shift, func) \

50 IPSR(((reg) << 5U) | (bank), shift, func)

51

[ 52](pinctrl-rcar-common_8h.md#ab51addcdd30207beec6a6b407b03bda0)#define IP0SR0(shift, func) IPnSR(0, 0, shift, func)

[ 53](pinctrl-rcar-common_8h.md#a589208eb9220dbb7df9e69c3fcba2b81)#define IP1SR0(shift, func) IPnSR(1, 0, shift, func)

[ 54](pinctrl-rcar-common_8h.md#a051053920b8e6bf22e28411e1f6fc4c8)#define IP2SR0(shift, func) IPnSR(2, 0, shift, func)

[ 55](pinctrl-rcar-common_8h.md#a6ebd6c3699a13fd9e98d610c82a3df25)#define IP3SR0(shift, func) IPnSR(3, 0, shift, func)

[ 56](pinctrl-rcar-common_8h.md#ade8ab39b443828811cf43da560741d30)#define IP0SR1(shift, func) IPnSR(0, 1, shift, func)

[ 57](pinctrl-rcar-common_8h.md#a500166c8427d495d8811f51c19091738)#define IP1SR1(shift, func) IPnSR(1, 1, shift, func)

[ 58](pinctrl-rcar-common_8h.md#aee2ad7f7a43248b8d1fdc68cac741f00)#define IP2SR1(shift, func) IPnSR(2, 1, shift, func)

[ 59](pinctrl-rcar-common_8h.md#aa19b6f71f524cf0f68caeac0b90eee48)#define IP3SR1(shift, func) IPnSR(3, 1, shift, func)

[ 60](pinctrl-rcar-common_8h.md#aea6fa1ee9aa68fcbad9a7cad7df0534b)#define IP0SR2(shift, func) IPnSR(0, 2, shift, func)

[ 61](pinctrl-rcar-common_8h.md#a0e288300855fb369dcee23d96d372438)#define IP1SR2(shift, func) IPnSR(1, 2, shift, func)

[ 62](pinctrl-rcar-common_8h.md#a394520e1fcf63bf5f8943d0bea1cab24)#define IP2SR2(shift, func) IPnSR(2, 2, shift, func)

[ 63](pinctrl-rcar-common_8h.md#a0fa1dcfc6401dd2b00358651b38599b6)#define IP3SR2(shift, func) IPnSR(3, 2, shift, func)

[ 64](pinctrl-rcar-common_8h.md#ad965c683495fb478007f7b3cf990fb59)#define IP0SR3(shift, func) IPnSR(0, 3, shift, func)

[ 65](pinctrl-rcar-common_8h.md#a021e17a25abb44ce72945e36139a02c9)#define IP1SR3(shift, func) IPnSR(1, 3, shift, func)

[ 66](pinctrl-rcar-common_8h.md#ab159b7a4d4194011ce63fab0dada6074)#define IP2SR3(shift, func) IPnSR(2, 3, shift, func)

[ 67](pinctrl-rcar-common_8h.md#ad28172ec262b56b921c8b2236f9ab55a)#define IP3SR3(shift, func) IPnSR(3, 3, shift, func)

[ 68](pinctrl-rcar-common_8h.md#aaf9b88b2ff558f2656c283f95c788f28)#define IP0SR4(shift, func) IPnSR(0, 4, shift, func)

[ 69](pinctrl-rcar-common_8h.md#a1f27d51000a30d18a6036be7aa6aabd3)#define IP1SR4(shift, func) IPnSR(1, 4, shift, func)

[ 70](pinctrl-rcar-common_8h.md#af1e67326feb755694a68c688342ff72d)#define IP2SR4(shift, func) IPnSR(2, 4, shift, func)

[ 71](pinctrl-rcar-common_8h.md#a1a57c0446bc7384b14df6b27fc10ebaf)#define IP3SR4(shift, func) IPnSR(3, 4, shift, func)

[ 72](pinctrl-rcar-common_8h.md#a13a0b7d3677364aa239400adf7de4e80)#define IP0SR5(shift, func) IPnSR(0, 5, shift, func)

[ 73](pinctrl-rcar-common_8h.md#a5c60a8466fef3878180305153d81f070)#define IP1SR5(shift, func) IPnSR(1, 5, shift, func)

[ 74](pinctrl-rcar-common_8h.md#ac6f43f2973e0b423f3f739dfbf682c06)#define IP2SR5(shift, func) IPnSR(2, 5, shift, func)

[ 75](pinctrl-rcar-common_8h.md#a9d172a3cf5402e07487caf4c2e88a673)#define IP3SR5(shift, func) IPnSR(3, 5, shift, func)

[ 76](pinctrl-rcar-common_8h.md#a7e1583caf721967f93f862d846b62545)#define IP0SR6(shift, func) IPnSR(0, 6, shift, func)

[ 77](pinctrl-rcar-common_8h.md#a1a975de92d8a33ac57a26d71dd98ad9c)#define IP1SR6(shift, func) IPnSR(1, 6, shift, func)

[ 78](pinctrl-rcar-common_8h.md#a5b7e9ba907566b64cafd8d00f4eb6eaf)#define IP2SR6(shift, func) IPnSR(2, 6, shift, func)

[ 79](pinctrl-rcar-common_8h.md#a6a406638dadb4d7c99c999d5a6041174)#define IP3SR6(shift, func) IPnSR(3, 6, shift, func)

[ 80](pinctrl-rcar-common_8h.md#a70a6ae0173ed04d171d73b9d8673be30)#define IP0SR7(shift, func) IPnSR(0, 7, shift, func)

[ 81](pinctrl-rcar-common_8h.md#a75720c99b0d0e1406599ddca8480905d)#define IP1SR7(shift, func) IPnSR(1, 7, shift, func)

[ 82](pinctrl-rcar-common_8h.md#ac8914ec1a230d65ee43bac854e9825cd)#define IP2SR7(shift, func) IPnSR(2, 7, shift, func)

[ 83](pinctrl-rcar-common_8h.md#ac2287f3a881d97a63fcedd77bd649823)#define IP3SR7(shift, func) IPnSR(3, 7, shift, func)

84

[ 85](pinctrl-rcar-common_8h.md#a866ef498674c60a51c56decc15421e25)#define PIN\_VOLTAGE\_NONE 0

[ 86](pinctrl-rcar-common_8h.md#aeb4cb1a9f61be2a30c5b11bec746b839)#define PIN\_VOLTAGE\_1P8V 1

[ 87](pinctrl-rcar-common_8h.md#acc995ebea352dc5bf5042e29cd1e15d0)#define PIN\_VOLTAGE\_3P3V 2

88

89#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_RENESAS\_PINCTRL\_RCAR\_COMMON\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rcar-common.h](pinctrl-rcar-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
