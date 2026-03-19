---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/i2c_2target_2eeprom_8h_source.html
original_path: doxygen/html/i2c_2target_2eeprom_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eeprom.h

[Go to the documentation of this file.](i2c_2target_2eeprom_8h.md)

1

6

7/\*

8 \* Copyright (c) 2017 BayLibre, SAS

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_TARGET\_EEPROM\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_TARGET\_EEPROM\_H\_

14

23

[ 34](group__i2c__eeprom__target__api.md#ga8585267ec85234c68a4434e72608b27e)int [eeprom\_target\_program](group__i2c__eeprom__target__api.md#ga8585267ec85234c68a4434e72608b27e)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*eeprom\_data,

35 unsigned int length);

36

[ 47](group__i2c__eeprom__target__api.md#gadeb18bef0484b2f6dcf91c0131884fc4)int [eeprom\_target\_read](group__i2c__eeprom__target__api.md#gadeb18bef0484b2f6dcf91c0131884fc4)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*eeprom\_data,

48 unsigned int offset);

49

[ 61](group__i2c__eeprom__target__api.md#ga802f5d779e9a837a81b8b617037dfce8)int [eeprom\_target\_set\_addr](group__i2c__eeprom__target__api.md#ga802f5d779e9a837a81b8b617037dfce8)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr);

62

66

67#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I2C\_TARGET\_EEPROM\_H\_ \*/

[eeprom\_target\_set\_addr](group__i2c__eeprom__target__api.md#ga802f5d779e9a837a81b8b617037dfce8)

int eeprom\_target\_set\_addr(const struct device \*dev, uint8\_t addr)

Change the address of eeprom target at runtime.

[eeprom\_target\_program](group__i2c__eeprom__target__api.md#ga8585267ec85234c68a4434e72608b27e)

int eeprom\_target\_program(const struct device \*dev, const uint8\_t \*eeprom\_data, unsigned int length)

Program memory of the virtual EEPROM.

[eeprom\_target\_read](group__i2c__eeprom__target__api.md#gadeb18bef0484b2f6dcf91c0131884fc4)

int eeprom\_target\_read(const struct device \*dev, uint8\_t \*eeprom\_data, unsigned int offset)

Read single byte of virtual EEPROM memory.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c](dir_d0e9f61c1b95aed307ec1c726ffb3f96.md)
- [target](dir_25ea520bf1ef1038fac9c410667bd932.md)
- [eeprom.h](i2c_2target_2eeprom_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
