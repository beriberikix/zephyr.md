---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nct38xx_8h.html
original_path: doxygen/html/nct38xx_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nct38xx.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](nct38xx_8h_source.md)

| Functions | |
| --- | --- |
| struct k\_sem \* | [mfd\_nct38xx\_get\_lock\_reference](#a14924372c0c4ffb5cb5d7f69cf22df7d) (const struct [device](structdevice.md) \*dev) |
|  | Get the semaphore reference for a NCT38xx instance. |
| const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* | [mfd\_nct38xx\_get\_i2c\_dt\_spec](#af32ad6d2c437c5a1ebb4abe660903bde) (const struct [device](structdevice.md) \*dev) |
|  | Get the I2C DT spec reference for a NCT38xx instance. |

## Function Documentation

## [◆ ](#af32ad6d2c437c5a1ebb4abe660903bde)mfd\_nct38xx\_get\_i2c\_dt\_spec()

| const struct [i2c\_dt\_spec](structi2c__dt__spec.md) \* mfd\_nct38xx\_get\_i2c\_dt\_spec | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the I2C DT spec reference for a NCT38xx instance.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   Address of the I2C DT spec

## [◆ ](#a14924372c0c4ffb5cb5d7f69cf22df7d)mfd\_nct38xx\_get\_lock\_reference()

| struct k\_sem \* mfd\_nct38xx\_get\_lock\_reference | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the semaphore reference for a NCT38xx instance.

Callers should pass the return value to k\_sem\_take/k\_sem\_give

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   Address of the semaphore

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [nct38xx.h](nct38xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
