---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mfd__maxq10xx_8h.html
original_path: doxygen/html/mfd__maxq10xx_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mfd\_maxq10xx.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](mfd__maxq10xx_8h_source.md)

| Functions | |
| --- | --- |
| struct [k\_sem](structk__sem.md) \* | [mfd\_maxq10xx\_get\_lock](#afab2fb34feb7d84e42caea6021dd1ed9) (const struct [device](structdevice.md) \*dev) |
|  | Get the semaphore reference for a MAXQ1xx instance. |

## Function Documentation

## [◆ ](#afab2fb34feb7d84e42caea6021dd1ed9)mfd\_maxq10xx\_get\_lock()

| struct [k\_sem](structk__sem.md) \* mfd\_maxq10xx\_get\_lock | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the semaphore reference for a MAXQ1xx instance.

Callers should pass the return value to k\_sem\_take/k\_sem\_give

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |

Returns
:   Address of the semaphore

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mfd](dir_1bf5b7f6eba6ffa1b2ffa53a350028d6.md)
- [mfd\_maxq10xx.h](mfd__maxq10xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
