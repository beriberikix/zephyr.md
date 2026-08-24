---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/i2c__nrfx__twim_8h.html
original_path: doxygen/html/i2c__nrfx__twim_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_nrfx\_twim.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h_source.md)>`

[Go to the source code of this file.](i2c__nrfx__twim_8h_source.md)

| Functions | |
| --- | --- |
| int | [i2c\_nrfx\_twim\_exclusive\_access\_acquire](#a465c42f64eb7d2dd4c5e173f9ae11745) (const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Acquires exclusive access to the i2c bus controller. |
| void | [i2c\_nrfx\_twim\_exclusive\_access\_release](#a924fddc00479f92f98b05a91d08fa7da) (const struct [device](structdevice.md) \*dev) |
|  | Releases exclusive access to the i2c bus controller. |

## Function Documentation

## [◆ ](#a465c42f64eb7d2dd4c5e173f9ae11745)i2c\_nrfx\_twim\_exclusive\_access\_acquire()

| int i2c\_nrfx\_twim\_exclusive\_access\_acquire | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

Acquires exclusive access to the i2c bus controller.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver configured in controller mode. |
    | --- | --- |
    | timeout | Timeout for waiting to acquire exclusive access. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out, or the underlying semaphore was reset during the waiting period. |

## [◆ ](#a924fddc00479f92f98b05a91d08fa7da)i2c\_nrfx\_twim\_exclusive\_access\_release()

| void i2c\_nrfx\_twim\_exclusive\_access\_release | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Releases exclusive access to the i2c bus controller.

Parameters
:   | dev | Pointer to the device structure for an I2C controller driver on which [i2c\_nrfx\_twim\_exclusive\_access\_acquire](#a465c42f64eb7d2dd4c5e173f9ae11745) has been successfully called. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c](dir_d0e9f61c1b95aed307ec1c726ffb3f96.md)
- [i2c\_nrfx\_twim.h](i2c__nrfx__twim_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
