---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gpio__sx1509b_8h.html
original_path: doxygen/html/gpio__sx1509b_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_sx1509b.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](gpio__sx1509b_8h_source.md)

| Functions | |
| --- | --- |
| int | [sx1509b\_led\_intensity\_pin\_configure](#ac2ed2f915a7e507e49abc82b6f4f09d5) (const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Configure a pin for LED intensity. |
| int | [sx1509b\_led\_intensity\_pin\_set](#a5fe77cf7261b831b4cb010c48da982bf) (const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) intensity\_val) |
|  | Set LED intensity of selected pin. |

## Function Documentation

## [◆ ](#ac2ed2f915a7e507e49abc82b6f4f09d5)sx1509b\_led\_intensity\_pin\_configure()

| int sx1509b\_led\_intensity\_pin\_configure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) |

Configure a pin for LED intensity.

Configure a pin to be controlled by SX1509B LED driver using the LED intensity functionality. To get back normal GPIO functionality, configure the pin using the standard GPIO API.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EWOULDBLOCK | if function is called from an ISR. |
    | -ERANGE | if pin number is out of range. |
    | -EIO | if I2C fails. |

## [◆ ](#a5fe77cf7261b831b4cb010c48da982bf)sx1509b\_led\_intensity\_pin\_set()

| int sx1509b\_led\_intensity\_pin\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) | *pin*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *intensity\_val* ) |

Set LED intensity of selected pin.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number. |
    | intensity\_val | Intensity value. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | if I2C fails. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_sx1509b.h](gpio__sx1509b_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
