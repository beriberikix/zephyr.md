---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/eth__lan865x_8h_source.html
original_path: doxygen/html/eth__lan865x_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_lan865x.h

[Go to the documentation of this file.](eth__lan865x_8h.md)

1/\*

2 \* Copyright (c) 2024 Microchip Technology Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_LAN865X\_H\_\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_LAN865X\_H\_\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[zephyr/device.h](device_8h.md)>

13

[ 30](eth__lan865x_8h.md#a40e7b77347741d6f71fc2681900a997a)int [eth\_lan865x\_mdio\_c22\_read](eth__lan865x_8h.md#a40e7b77347741d6f71fc2681900a997a)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

31 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

32

[ 49](eth__lan865x_8h.md#a7b6bad30fa365b78d876d53e24c6a919)int [eth\_lan865x\_mdio\_c22\_write](eth__lan865x_8h.md#a7b6bad30fa365b78d876d53e24c6a919)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad,

50 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

51

[ 69](eth__lan865x_8h.md#a4580c639b8d4f36323ecc02cfa5bfd26)int [eth\_lan865x\_mdio\_c45\_read](eth__lan865x_8h.md#a4580c639b8d4f36323ecc02cfa5bfd26)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad,

70 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data);

71

[ 89](eth__lan865x_8h.md#a09613a11b8f59a3c3395a3257f494d17)int [eth\_lan865x\_mdio\_c45\_write](eth__lan865x_8h.md#a09613a11b8f59a3c3395a3257f494d17)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad,

90 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data);

91

92#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_ETH\_LAN865X\_H\_\_ \*/

[device.h](device_8h.md)

[eth\_lan865x\_mdio\_c45\_write](eth__lan865x_8h.md#a09613a11b8f59a3c3395a3257f494d17)

int eth\_lan865x\_mdio\_c45\_write(const struct device \*dev, uint8\_t prtad, uint8\_t devad, uint16\_t regad, uint16\_t data)

Write C45 registers using LAN865X MDIO Bus.

[eth\_lan865x\_mdio\_c22\_read](eth__lan865x_8h.md#a40e7b77347741d6f71fc2681900a997a)

int eth\_lan865x\_mdio\_c22\_read(const struct device \*dev, uint8\_t prtad, uint8\_t regad, uint16\_t \*data)

Read C22 registers using LAN865X MDIO Bus.

[eth\_lan865x\_mdio\_c45\_read](eth__lan865x_8h.md#a4580c639b8d4f36323ecc02cfa5bfd26)

int eth\_lan865x\_mdio\_c45\_read(const struct device \*dev, uint8\_t prtad, uint8\_t devad, uint16\_t regad, uint16\_t \*data)

Read C45 registers using LAN865X MDIO Bus.

[eth\_lan865x\_mdio\_c22\_write](eth__lan865x_8h.md#a7b6bad30fa365b78d876d53e24c6a919)

int eth\_lan865x\_mdio\_c22\_write(const struct device \*dev, uint8\_t prtad, uint8\_t regad, uint16\_t data)

Write C22 registers using LAN865X MDIO Bus.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

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
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_lan865x.h](eth__lan865x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
