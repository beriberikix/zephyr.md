---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ft8xx__common_8h_source.html
original_path: doxygen/html/ft8xx__common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_common.h

[Go to the documentation of this file.](ft8xx__common_8h.md)

1/\*

2 \* Copyright (c) 2020 Hubert Miś

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COMMON\_H\_

13#define ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COMMON\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

[ 36](group__ft8xx__common.md#ga2c8c5d06b09549ab041bbff4612b4620)void [ft8xx\_wr8](group__ft8xx__common.md#ga2c8c5d06b09549ab041bbff4612b4620)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data);

37

[ 45](group__ft8xx__common.md#gaa6d306b1e2701e0de415c64d33e575a4)void [ft8xx\_wr16](group__ft8xx__common.md#gaa6d306b1e2701e0de415c64d33e575a4)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

46

[ 54](group__ft8xx__common.md#gada8d996d58f0f46f3f56534ee0da4c68)void [ft8xx\_wr32](group__ft8xx__common.md#gada8d996d58f0f46f3f56534ee0da4c68)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

55

[ 64](group__ft8xx__common.md#gab8235ed0c0f7373628457fcf64e15fbd)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ft8xx\_rd8](group__ft8xx__common.md#gab8235ed0c0f7373628457fcf64e15fbd)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address);

65

[ 74](group__ft8xx__common.md#ga743c2d25f728451e98417b2ebcc9c722)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ft8xx\_rd16](group__ft8xx__common.md#ga743c2d25f728451e98417b2ebcc9c722)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address);

75

[ 84](group__ft8xx__common.md#gaed670a8410224f8f3970fad86705f513)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ft8xx\_rd32](group__ft8xx__common.md#gaed670a8410224f8f3970fad86705f513)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address);

85

89

90#ifdef \_\_cplusplus

91}

92#endif

93

94#endif /\* ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_COMMON\_H\_ \*/

[device.h](device_8h.md)

[ft8xx\_wr8](group__ft8xx__common.md#ga2c8c5d06b09549ab041bbff4612b4620)

void ft8xx\_wr8(const struct device \*dev, uint32\_t address, uint8\_t data)

Write 1 byte (8 bits) to FT8xx memory.

[ft8xx\_rd16](group__ft8xx__common.md#ga743c2d25f728451e98417b2ebcc9c722)

uint16\_t ft8xx\_rd16(const struct device \*dev, uint32\_t address)

Read 2 bytes (16 bits) from FT8xx memory.

[ft8xx\_wr16](group__ft8xx__common.md#gaa6d306b1e2701e0de415c64d33e575a4)

void ft8xx\_wr16(const struct device \*dev, uint32\_t address, uint16\_t data)

Write 2 bytes (16 bits) to FT8xx memory.

[ft8xx\_rd8](group__ft8xx__common.md#gab8235ed0c0f7373628457fcf64e15fbd)

uint8\_t ft8xx\_rd8(const struct device \*dev, uint32\_t address)

Read 1 byte (8 bits) from FT8xx memory.

[ft8xx\_wr32](group__ft8xx__common.md#gada8d996d58f0f46f3f56534ee0da4c68)

void ft8xx\_wr32(const struct device \*dev, uint32\_t address, uint32\_t data)

Write 4 bytes (32 bits) to FT8xx memory.

[ft8xx\_rd32](group__ft8xx__common.md#gaed670a8410224f8f3970fad86705f513)

uint32\_t ft8xx\_rd32(const struct device \*dev, uint32\_t address)

Read 4 bytes (32 bits) from FT8xx memory.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_common.h](ft8xx__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
