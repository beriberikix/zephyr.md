---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structspi__cs__control.html
original_path: doxygen/html/structspi__cs__control.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_cs\_control Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SPI Interface](group__spi__interface.md)

SPI Chip Select control structure.
[More...](#details)

`#include <[spi.h](drivers_2spi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [gpio\_dt\_spec](structgpio__dt__spec.md) | [gpio](#a8ad907e168666c2ddca77e89f9b9f47f) |
|  | GPIO devicetree specification of CS GPIO. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [delay](#a04569d78ac7d6022ffee0c28f5d3b629) |
|  | Delay in microseconds to wait before starting the transmission and before releasing the CS line. |

## Detailed Description

SPI Chip Select control structure.

This can be used to control a CS line via a GPIO line, instead of using the controller inner CS logic.

## Field Documentation

## [◆ ](#a04569d78ac7d6022ffee0c28f5d3b629)delay

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spi\_cs\_control::delay |
| --- |

Delay in microseconds to wait before starting the transmission and before releasing the CS line.

## [◆ ](#a8ad907e168666c2ddca77e89f9b9f47f)gpio

| struct [gpio\_dt\_spec](structgpio__dt__spec.md) spi\_cs\_control::gpio |
| --- |

GPIO devicetree specification of CS GPIO.

The device pointer can be set to NULL to fully inhibit CS control if necessary. The GPIO flags GPIO\_ACTIVE\_LOW/GPIO\_ACTIVE\_HIGH should be equivalent to SPI\_CS\_ACTIVE\_HIGH/SPI\_CS\_ACTIVE\_LOW options in struct [spi\_config](structspi__config.md "SPI controller configuration structure.").

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[spi.h](drivers_2spi_8h_source.md)

- [spi\_cs\_control](structspi__cs__control.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
