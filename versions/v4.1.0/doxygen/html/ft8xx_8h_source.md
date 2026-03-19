---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ft8xx_8h_source.html
original_path: doxygen/html/ft8xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx.h

[Go to the documentation of this file.](ft8xx_8h.md)

1/\*

2 \* Copyright (c) 2020 Hubert Miś

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_H\_

13#define ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

[ 35](structft8xx__touch__transform.md)struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) {

[ 36](structft8xx__touch__transform.md#aebc5352e00847e41b2d239a9265b5e45) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [a](structft8xx__touch__transform.md#aebc5352e00847e41b2d239a9265b5e45);

[ 37](structft8xx__touch__transform.md#a307e6438e32a36ac78c76979925e5e1c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b](structft8xx__touch__transform.md#a307e6438e32a36ac78c76979925e5e1c);

[ 38](structft8xx__touch__transform.md#ab86ed8962e01945c63751912c622b623) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [c](structft8xx__touch__transform.md#ab86ed8962e01945c63751912c622b623);

[ 39](structft8xx__touch__transform.md#aeee5e2153eca64f1c5a6196d910c3d3e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [d](structft8xx__touch__transform.md#aeee5e2153eca64f1c5a6196d910c3d3e);

[ 40](structft8xx__touch__transform.md#a8c31db728937a0b69f01b9c3e265287a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [e](structft8xx__touch__transform.md#a8c31db728937a0b69f01b9c3e265287a);

[ 41](structft8xx__touch__transform.md#aa72829a35d054aa88fc8fd494e5eecbe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [f](structft8xx__touch__transform.md#aa72829a35d054aa88fc8fd494e5eecbe);

42};

43

[ 53](group__ft8xx__interface.md#ga846a90d72b56f388d5b4f60cf6d658b0)typedef void (\*[ft8xx\_int\_callback](group__ft8xx__interface.md#ga846a90d72b56f388d5b4f60cf6d658b0))(const struct [device](structdevice.md) \*dev, void \*user\_data);

54

[ 69](group__ft8xx__interface.md#ga586f6ff1eddd5b596d2e35fb5fdd8148)void [ft8xx\_calibrate](group__ft8xx__interface.md#ga586f6ff1eddd5b596d2e35fb5fdd8148)(const struct [device](structdevice.md) \*dev,

70 struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

71

[ 82](group__ft8xx__interface.md#ga1d74a13782c6ab9f8b07a28503058356)void [ft8xx\_touch\_transform\_set](group__ft8xx__interface.md#ga1d74a13782c6ab9f8b07a28503058356)(const struct [device](structdevice.md) \*dev,

83 const struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

84

[ 92](group__ft8xx__interface.md#gaea3589b5a0aa34a09a81ea15c1595219)int [ft8xx\_get\_touch\_tag](group__ft8xx__interface.md#gaea3589b5a0aa34a09a81ea15c1595219)(const struct [device](structdevice.md) \*dev);

93

[ 108](group__ft8xx__interface.md#gaf392199312ddb82451a4f31e2955079d)void [ft8xx\_register\_int](group__ft8xx__interface.md#gaf392199312ddb82451a4f31e2955079d)(const struct [device](structdevice.md) \*dev,

109 [ft8xx\_int\_callback](group__ft8xx__interface.md#ga846a90d72b56f388d5b4f60cf6d658b0) callback,

110 void \*user\_data);

111

115

116#ifdef \_\_cplusplus

117}

118#endif

119

120#endif /\* ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_H\_ \*/

[device.h](device_8h.md)

[ft8xx\_touch\_transform\_set](group__ft8xx__interface.md#ga1d74a13782c6ab9f8b07a28503058356)

void ft8xx\_touch\_transform\_set(const struct device \*dev, const struct ft8xx\_touch\_transform \*data)

Set touchscreen calibration data.

[ft8xx\_calibrate](group__ft8xx__interface.md#ga586f6ff1eddd5b596d2e35fb5fdd8148)

void ft8xx\_calibrate(const struct device \*dev, struct ft8xx\_touch\_transform \*data)

Calibrate touchscreen.

[ft8xx\_int\_callback](group__ft8xx__interface.md#ga846a90d72b56f388d5b4f60cf6d658b0)

void(\* ft8xx\_int\_callback)(const struct device \*dev, void \*user\_data)

Callback API to inform API user that FT8xx triggered interrupt.

**Definition** ft8xx.h:53

[ft8xx\_get\_touch\_tag](group__ft8xx__interface.md#gaea3589b5a0aa34a09a81ea15c1595219)

int ft8xx\_get\_touch\_tag(const struct device \*dev)

Get tag of recently touched element.

[ft8xx\_register\_int](group__ft8xx__interface.md#gaf392199312ddb82451a4f31e2955079d)

void ft8xx\_register\_int(const struct device \*dev, ft8xx\_int\_callback callback, void \*user\_data)

Set callback executed when FT8xx triggers interrupt.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[ft8xx\_touch\_transform](structft8xx__touch__transform.md)

Structure holding touchscreen calibration data.

**Definition** ft8xx.h:35

[ft8xx\_touch\_transform::b](structft8xx__touch__transform.md#a307e6438e32a36ac78c76979925e5e1c)

uint32\_t b

**Definition** ft8xx.h:37

[ft8xx\_touch\_transform::e](structft8xx__touch__transform.md#a8c31db728937a0b69f01b9c3e265287a)

uint32\_t e

**Definition** ft8xx.h:40

[ft8xx\_touch\_transform::f](structft8xx__touch__transform.md#aa72829a35d054aa88fc8fd494e5eecbe)

uint32\_t f

**Definition** ft8xx.h:41

[ft8xx\_touch\_transform::c](structft8xx__touch__transform.md#ab86ed8962e01945c63751912c622b623)

uint32\_t c

**Definition** ft8xx.h:38

[ft8xx\_touch\_transform::a](structft8xx__touch__transform.md#aebc5352e00847e41b2d239a9265b5e45)

uint32\_t a

**Definition** ft8xx.h:36

[ft8xx\_touch\_transform::d](structft8xx__touch__transform.md#aeee5e2153eca64f1c5a6196d910c3d3e)

uint32\_t d

**Definition** ft8xx.h:39

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx.h](ft8xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
