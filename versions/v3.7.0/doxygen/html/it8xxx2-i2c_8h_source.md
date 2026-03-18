---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/it8xxx2-i2c_8h_source.html
original_path: doxygen/html/it8xxx2-i2c_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

it8xxx2-i2c.h

[Go to the documentation of this file.](it8xxx2-i2c_8h.md)

1/\*

2 \* Copyright (c) 2022 ITE Technology Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_I2C\_IT8XXX2\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_I2C\_IT8XXX2\_H\_

8

9

[ 10](it8xxx2-i2c_8h.md#a9f78924cf5b262f18222242fb9c95953)#define IT8XXX2\_ECPM\_CGCTRL4R\_OFF 0x09

11/\*

12 \* The clock gate offsets combine the register offset from ECPM\_BASE and the

13 \* mask within that register into one value. These are used for

14 \* clock\_enable\_peripheral() and clock\_disable\_peripheral()

15 \*/

[ 16](it8xxx2-i2c_8h.md#ad4ed6083b062932a8c9dd759b688f6de)#define CGC\_OFFSET\_SMBF ((IT8XXX2\_ECPM\_CGCTRL4R\_OFF << 8) | 0x80)

[ 17](it8xxx2-i2c_8h.md#a330c86262342d98ccb02ad13ae2f137d)#define CGC\_OFFSET\_SMBE ((IT8XXX2\_ECPM\_CGCTRL4R\_OFF << 8) | 0x40)

[ 18](it8xxx2-i2c_8h.md#a8e413daf97c14719910d2e662c0eca75)#define CGC\_OFFSET\_SMBD ((IT8XXX2\_ECPM\_CGCTRL4R\_OFF << 8) | 0x20)

[ 19](it8xxx2-i2c_8h.md#ab55d020323d4cd67f71e228913a567e6)#define CGC\_OFFSET\_SMBC ((IT8XXX2\_ECPM\_CGCTRL4R\_OFF << 8) | 0x10)

[ 20](it8xxx2-i2c_8h.md#a7e2921ab27adcdab5494194f41085f8d)#define CGC\_OFFSET\_SMBB ((IT8XXX2\_ECPM\_CGCTRL4R\_OFF << 8) | 0x08)

[ 21](it8xxx2-i2c_8h.md#ab6bf39556df2289991cc268d38cfb45c)#define CGC\_OFFSET\_SMBA ((IT8XXX2\_ECPM\_CGCTRL4R\_OFF << 8) | 0x04)

22

23/\* I2C channel switch selection \*/

[ 24](it8xxx2-i2c_8h.md#acbbd55b831e98ea4919e1fd13fedcb7a)#define I2C\_CHA\_LOCATE 0

[ 25](it8xxx2-i2c_8h.md#aebaf0e97ddd1e9e11495467c3553aba9)#define I2C\_CHB\_LOCATE 1

[ 26](it8xxx2-i2c_8h.md#a96de9ecb61d81496b247a90cad938761)#define I2C\_CHC\_LOCATE 2

[ 27](it8xxx2-i2c_8h.md#ae21cc6587cd40acd96c177e69b8c806d)#define I2C\_CHD\_LOCATE 3

[ 28](it8xxx2-i2c_8h.md#a9810b4bfaa5f1892fe9fe4aa05dce5c8)#define I2C\_CHE\_LOCATE 4

[ 29](it8xxx2-i2c_8h.md#ae488c1cf89f783e12f975b446bc90b23)#define I2C\_CHF\_LOCATE 5

30

31#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_I2C\_IT8XXX2\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [i2c](dir_fcc76e97acca71d0ab1d4f13f62b3078.md)
- [it8xxx2-i2c.h](it8xxx2-i2c_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
