---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ad5592_8h_source.html
original_path: doxygen/html/ad5592_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ad5592.h

[Go to the documentation of this file.](ad5592_8h.md)

1/\*

2 \* Copyright (c) 2023 Grinn

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AD5592\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AD5592\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13#include <[zephyr/device.h](device_8h.md)>

14

[ 15](ad5592_8h.md#ab464cbfaf207ba8cefed656d9001cc7a)#define AD5592\_REG\_SEQ\_ADC 0x02U

[ 16](ad5592_8h.md#a61528964ca453fec022313787cb0d8ef)#define AD5592\_REG\_ADC\_CONFIG 0x04U

[ 17](ad5592_8h.md#ad5a6741c8f87771fb431a722edabbe0e)#define AD5592\_REG\_LDAC\_EN 0x05U

[ 18](ad5592_8h.md#ab843487e61aae28f1852e22411c7bf4b)#define AD5592\_REG\_GPIO\_PULLDOWN 0x06U

[ 19](ad5592_8h.md#aa5cc607bfa36bd95be46333d58c0c374)#define AD5592\_REG\_READ\_AND\_LDAC 0x07U

[ 20](ad5592_8h.md#aef8611ed40e105e7446b481c398d4320)#define AD5592\_REG\_GPIO\_OUTPUT\_EN 0x08U

[ 21](ad5592_8h.md#ab8cf8a8bcd89b73fa0c37185e53103de)#define AD5592\_REG\_GPIO\_SET 0x09U

[ 22](ad5592_8h.md#a0b8cdef657c29604cceb042505325d65)#define AD5592\_REG\_GPIO\_INPUT\_EN 0x0AU

[ 23](ad5592_8h.md#a2873c8e7ba88032eb176482f0102fe06)#define AD5592\_REG\_PD\_REF\_CTRL 0x0BU

24

[ 25](ad5592_8h.md#a1a24ad5e1768679acbde7913002cbe47)#define AD5592\_EN\_REF BIT(9)

26

[ 27](ad5592_8h.md#a4673da83673116b3f9fac2ac67423ebd)#define AD5592\_PIN\_MAX 8U

28

34

[ 44](group__mdf__interface__ad5592.md#ga85c63928ac0e2a0966d292edb17de70c)int [mfd\_ad5592\_read\_raw](group__mdf__interface__ad5592.md#ga85c63928ac0e2a0966d292edb17de70c)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*val);

45

[ 56](group__mdf__interface__ad5592.md#ga5368dbb3180785dde223f8cab9e6726b)int [mfd\_ad5592\_write\_raw](group__mdf__interface__ad5592.md#ga5368dbb3180785dde223f8cab9e6726b)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

57

[ 69](group__mdf__interface__ad5592.md#ga316fdc2bd9cedfd07b3f2ed8adada373)int [mfd\_ad5592\_read\_reg](group__mdf__interface__ad5592.md#ga316fdc2bd9cedfd07b3f2ed8adada373)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*val);

70

[ 81](group__mdf__interface__ad5592.md#gad5b20b7dc34092701a464c27382a55ed)int [mfd\_ad5592\_write\_reg](group__mdf__interface__ad5592.md#gad5b20b7dc34092701a464c27382a55ed)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val);

82

86

87#ifdef \_\_cplusplus

88}

89#endif

90

91#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MFD\_AD5952\_H\_ \*/

[device.h](device_8h.md)

[mfd\_ad5592\_read\_reg](group__mdf__interface__ad5592.md#ga316fdc2bd9cedfd07b3f2ed8adada373)

int mfd\_ad5592\_read\_reg(const struct device \*dev, uint8\_t reg, uint8\_t reg\_data, uint16\_t \*val)

Read data from provided register.

[mfd\_ad5592\_write\_raw](group__mdf__interface__ad5592.md#ga5368dbb3180785dde223f8cab9e6726b)

int mfd\_ad5592\_write\_raw(const struct device \*dev, uint16\_t val)

Write raw data to chip.

[mfd\_ad5592\_read\_raw](group__mdf__interface__ad5592.md#ga85c63928ac0e2a0966d292edb17de70c)

int mfd\_ad5592\_read\_raw(const struct device \*dev, uint16\_t \*val)

Read raw data from the chip.

[mfd\_ad5592\_write\_reg](group__mdf__interface__ad5592.md#gad5b20b7dc34092701a464c27382a55ed)

int mfd\_ad5592\_write\_reg(const struct device \*dev, uint8\_t reg, uint16\_t val)

Write data to provided register.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [ad5592.h](ad5592_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
