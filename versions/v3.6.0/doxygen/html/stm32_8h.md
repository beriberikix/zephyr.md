---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/stm32_8h.html
original_path: doxygen/html/stm32_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](stm32_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [i2c\_stm32\_mode](#a1e3b0af0114531103001ffac5dc10730) { [I2CSTM32MODE\_I2C](#a1e3b0af0114531103001ffac5dc10730af4173c801cc5a4aeddd8bb1e01e74250) , [I2CSTM32MODE\_SMBUSHOST](#a1e3b0af0114531103001ffac5dc10730a7a56a445c59c7fe860945a2e4a11c61b) , [I2CSTM32MODE\_SMBUSDEVICE](#a1e3b0af0114531103001ffac5dc10730ac8a7757cd18406545dbfb72df6c6162b) , [I2CSTM32MODE\_SMBUSDEVICEARP](#a1e3b0af0114531103001ffac5dc10730aec2ff625d8a070fbd7ffe9246eb6bf07) } |

| Functions | |
| --- | --- |
| void | [i2c\_stm32\_set\_smbus\_mode](#ae82dc3ada1276b676169c95c6d239d82) (const struct [device](structdevice.md) \*dev, enum [i2c\_stm32\_mode](#a1e3b0af0114531103001ffac5dc10730) mode) |

## Enumeration Type Documentation

## [◆ ](#a1e3b0af0114531103001ffac5dc10730)i2c\_stm32\_mode

| enum [i2c\_stm32\_mode](#a1e3b0af0114531103001ffac5dc10730) |
| --- |

| Enumerator | |
| --- | --- |
| I2CSTM32MODE\_I2C |  |
| I2CSTM32MODE\_SMBUSHOST |  |
| I2CSTM32MODE\_SMBUSDEVICE |  |
| I2CSTM32MODE\_SMBUSDEVICEARP |  |

## Function Documentation

## [◆ ](#ae82dc3ada1276b676169c95c6d239d82)i2c\_stm32\_set\_smbus\_mode()

| void i2c\_stm32\_set\_smbus\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [i2c\_stm32\_mode](#a1e3b0af0114531103001ffac5dc10730) | *mode* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c](dir_d0e9f61c1b95aed307ec1c726ffb3f96.md)
- [stm32.h](stm32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
