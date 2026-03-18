---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/i2c_2target_2eeprom_8h.html
original_path: doxygen/html/i2c_2target_2eeprom_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eeprom.h File Reference

Public APIs for the I2C EEPROM Target driver.
[More...](#details)

[Go to the source code of this file.](i2c_2target_2eeprom_8h_source.md)

| Functions | |
| --- | --- |
| int | [eeprom\_target\_program](group__i2c__eeprom__target__api.md#ga8585267ec85234c68a4434e72608b27e) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*eeprom\_data, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int length) |
|  | Program memory of the virtual EEPROM. |
| int | [eeprom\_target\_read](group__i2c__eeprom__target__api.md#gadeb18bef0484b2f6dcf91c0131884fc4) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*eeprom\_data, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int offset) |
|  | Read single byte of virtual EEPROM memory. |
| int | [eeprom\_target\_set\_addr](group__i2c__eeprom__target__api.md#ga802f5d779e9a837a81b8b617037dfce8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Change the address of eeprom target at runtime. |

## Detailed Description

Public APIs for the I2C EEPROM Target driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c](dir_d0e9f61c1b95aed307ec1c726ffb3f96.md)
- [target](dir_25ea520bf1ef1038fac9c410667bd932.md)
- [eeprom.h](i2c_2target_2eeprom_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
