---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi2c__dt__spec.html
original_path: doxygen/html/structi2c__dt__spec.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I2C Interface](group__i2c__interface.md)

Complete I2C DT information.
[More...](#details)

`#include <[i2c.h](drivers_2i2c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [bus](#a40d5c17c04910927c34eb69b173cbb85) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#a85242ab56b1e8633b7001353990392fa) |

## Detailed Description

Complete I2C DT information.

Parameters
:   | [bus](#a40d5c17c04910927c34eb69b173cbb85) | is the I2C bus |
    | --- | --- |
    | [addr](#a85242ab56b1e8633b7001353990392fa) | is the target address |

## Field Documentation

## [◆ ](#a85242ab56b1e8633b7001353990392fa)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i2c\_dt\_spec::addr |
| --- |

## [◆ ](#a40d5c17c04910927c34eb69b173cbb85)bus

| const struct [device](structdevice.md)\* i2c\_dt\_spec::bus |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i2c.h](drivers_2i2c_8h_source.md)

- [i2c\_dt\_spec](structi2c__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
