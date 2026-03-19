---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gpio__pcal64xxa_8h.html
original_path: doxygen/html/gpio__pcal64xxa_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_pcal64xxa.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](gpio__pcal64xxa_8h_source.md)

| Functions | |
| --- | --- |
| int | [pcal64xxa\_reset](#a43c22f38602347e2e95f63fd9b31dc96) (const struct [device](structdevice.md) \*dev) |
|  | Manually reset a PCAL64XXA. |

## Function Documentation

## [◆ ](#a43c22f38602347e2e95f63fd9b31dc96)pcal64xxa\_reset()

| int pcal64xxa\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Manually reset a PCAL64XXA.

Resetting a PCAL64XXA manually is only necessary if the by default enabled automatic reset has been disabled.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_pcal64xxa.h](gpio__pcal64xxa_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
