---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/gpio__mcux__lpc_8h.html
original_path: doxygen/html/gpio__mcux__lpc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_mcux\_lpc.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](gpio__mcux__lpc_8h_source.md)

| Functions | |
| --- | --- |
| void | [gpio\_mcux\_lpc\_trigger\_cb](#a6ce1efd70bb2996ac993f2a322d74ac3) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pins) |
|  | Trigger a callback for a given pin. |

## Function Documentation

## [◆ ](#a6ce1efd70bb2996ac993f2a322d74ac3)gpio\_mcux\_lpc\_trigger\_cb()

| void gpio\_mcux\_lpc\_trigger\_cb | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pins* ) |

Trigger a callback for a given pin.

This allows other drivers to fire callbacks for the pin.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pins | The actual pin mask that triggered the interrupt. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_mcux\_lpc.h](gpio__mcux__lpc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
