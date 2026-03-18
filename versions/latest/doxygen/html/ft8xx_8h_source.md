---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ft8xx_8h_source.html
original_path: doxygen/html/ft8xx_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

27

[ 34](structft8xx__touch__transform.md)struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) {

[ 35](structft8xx__touch__transform.md#aebc5352e00847e41b2d239a9265b5e45) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [a](structft8xx__touch__transform.md#aebc5352e00847e41b2d239a9265b5e45);

[ 36](structft8xx__touch__transform.md#a307e6438e32a36ac78c76979925e5e1c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [b](structft8xx__touch__transform.md#a307e6438e32a36ac78c76979925e5e1c);

[ 37](structft8xx__touch__transform.md#ab86ed8962e01945c63751912c622b623) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [c](structft8xx__touch__transform.md#ab86ed8962e01945c63751912c622b623);

[ 38](structft8xx__touch__transform.md#aeee5e2153eca64f1c5a6196d910c3d3e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [d](structft8xx__touch__transform.md#aeee5e2153eca64f1c5a6196d910c3d3e);

[ 39](structft8xx__touch__transform.md#a8c31db728937a0b69f01b9c3e265287a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [e](structft8xx__touch__transform.md#a8c31db728937a0b69f01b9c3e265287a);

[ 40](structft8xx__touch__transform.md#aa72829a35d054aa88fc8fd494e5eecbe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [f](structft8xx__touch__transform.md#aa72829a35d054aa88fc8fd494e5eecbe);

41};

42

[ 49](group__ft8xx__interface.md#ga3841a8c74d795b14b7fbdd6115410217)typedef void (\*[ft8xx\_int\_callback](group__ft8xx__interface.md#ga3841a8c74d795b14b7fbdd6115410217))(void);

50

[ 64](group__ft8xx__interface.md#gaa563d0378314c304277e5bf54ab90c47)void [ft8xx\_calibrate](group__ft8xx__interface.md#gaa563d0378314c304277e5bf54ab90c47)(struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data);

65

[ 75](group__ft8xx__interface.md#gae45273c4617b565b4712a286f4f77c9c)void [ft8xx\_touch\_transform\_set](group__ft8xx__interface.md#gae45273c4617b565b4712a286f4f77c9c)(const struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data);

76

[ 82](group__ft8xx__interface.md#ga532142aba69b418b1d8f19ca954ba3bf)int [ft8xx\_get\_touch\_tag](group__ft8xx__interface.md#ga532142aba69b418b1d8f19ca954ba3bf)(void);

83

[ 96](group__ft8xx__interface.md#ga02bded8612961be5ff72c8cf3bf4afe3)void [ft8xx\_register\_int](group__ft8xx__interface.md#ga02bded8612961be5ff72c8cf3bf4afe3)([ft8xx\_int\_callback](group__ft8xx__interface.md#ga3841a8c74d795b14b7fbdd6115410217) callback);

97

101

102#ifdef \_\_cplusplus

103}

104#endif

105

106#endif /\* ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_H\_ \*/

[ft8xx\_register\_int](group__ft8xx__interface.md#ga02bded8612961be5ff72c8cf3bf4afe3)

void ft8xx\_register\_int(ft8xx\_int\_callback callback)

Set callback executed when FT8xx triggers interrupt.

[ft8xx\_int\_callback](group__ft8xx__interface.md#ga3841a8c74d795b14b7fbdd6115410217)

void(\* ft8xx\_int\_callback)(void)

Callback API to inform API user that FT8xx triggered interrupt.

**Definition** ft8xx.h:49

[ft8xx\_get\_touch\_tag](group__ft8xx__interface.md#ga532142aba69b418b1d8f19ca954ba3bf)

int ft8xx\_get\_touch\_tag(void)

Get tag of recently touched element.

[ft8xx\_calibrate](group__ft8xx__interface.md#gaa563d0378314c304277e5bf54ab90c47)

void ft8xx\_calibrate(struct ft8xx\_touch\_transform \*data)

Calibrate touchscreen.

[ft8xx\_touch\_transform\_set](group__ft8xx__interface.md#gae45273c4617b565b4712a286f4f77c9c)

void ft8xx\_touch\_transform\_set(const struct ft8xx\_touch\_transform \*data)

Set touchscreen calibration data.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[ft8xx\_touch\_transform](structft8xx__touch__transform.md)

Structure holding touchscreen calibration data.

**Definition** ft8xx.h:34

[ft8xx\_touch\_transform::b](structft8xx__touch__transform.md#a307e6438e32a36ac78c76979925e5e1c)

uint32\_t b

**Definition** ft8xx.h:36

[ft8xx\_touch\_transform::e](structft8xx__touch__transform.md#a8c31db728937a0b69f01b9c3e265287a)

uint32\_t e

**Definition** ft8xx.h:39

[ft8xx\_touch\_transform::f](structft8xx__touch__transform.md#aa72829a35d054aa88fc8fd494e5eecbe)

uint32\_t f

**Definition** ft8xx.h:40

[ft8xx\_touch\_transform::c](structft8xx__touch__transform.md#ab86ed8962e01945c63751912c622b623)

uint32\_t c

**Definition** ft8xx.h:37

[ft8xx\_touch\_transform::a](structft8xx__touch__transform.md#aebc5352e00847e41b2d239a9265b5e45)

uint32\_t a

**Definition** ft8xx.h:35

[ft8xx\_touch\_transform::d](structft8xx__touch__transform.md#aeee5e2153eca64f1c5a6196d910c3d3e)

uint32\_t d

**Definition** ft8xx.h:38

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx.h](ft8xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
