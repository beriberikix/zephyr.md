---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/devicetree_2spi_8h.html
original_path: doxygen/html/devicetree_2spi_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi.h File Reference

SPI Devicetree macro public API header file.
[More...](#details)

[Go to the source code of this file.](devicetree_2spi_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_SPI\_HAS\_CS\_GPIOS](group__devicetree-spi.md#gae8db0ce095bdd0066a845bc6a9bf329d)(spi) |
|  | Does a SPI controller node have chip select GPIOs configured? |
| #define | [DT\_SPI\_NUM\_CS\_GPIOS](group__devicetree-spi.md#gafe2bddd961fe08672e131cfbd73eb466)(spi) |
|  | Number of chip select GPIOs in a SPI controller's cs-gpios property. |
| #define | [DT\_SPI\_DEV\_HAS\_CS\_GPIOS](group__devicetree-spi.md#gad66b759d6aa4826f2c68a94e8708ad4f)(spi\_dev) |
|  | Does a SPI device have a chip select line configured? |
| #define | [DT\_SPI\_DEV\_CS\_GPIOS\_CTLR](group__devicetree-spi.md#ga0eaad9de680b5ac7cd8950957560c199)(spi\_dev) |
|  | Get a SPI device's chip select GPIO controller's node identifier. |
| #define | [DT\_SPI\_DEV\_CS\_GPIOS\_PIN](group__devicetree-spi.md#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)(spi\_dev) |
|  | Get a SPI device's chip select GPIO pin number. |
| #define | [DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS](group__devicetree-spi.md#ga49fd9c174931b44584a7dbbc18f7c644)(spi\_dev) |
|  | Get a SPI device's chip select GPIO flags. |
| #define | [DT\_INST\_SPI\_DEV\_HAS\_CS\_GPIOS](group__devicetree-spi.md#ga830f87f79c297c090a1929a288edc7ba)(inst) |
|  | Equivalent to [DT\_SPI\_DEV\_HAS\_CS\_GPIOS(DT\_DRV\_INST(inst))](group__devicetree-spi.md#gad66b759d6aa4826f2c68a94e8708ad4f "Does a SPI device have a chip select line configured?"). |
| #define | [DT\_INST\_SPI\_DEV\_CS\_GPIOS\_CTLR](group__devicetree-spi.md#ga0ffb7729cd90dc7bf4a1c33ead96a3d8)(inst) |
|  | Get GPIO controller node identifier for a SPI device instance This is equivalent to [DT\_SPI\_DEV\_CS\_GPIOS\_CTLR(DT\_DRV\_INST(inst))](group__devicetree-spi.md#ga0eaad9de680b5ac7cd8950957560c199 "Get a SPI device's chip select GPIO controller's node identifier."). |
| #define | [DT\_INST\_SPI\_DEV\_CS\_GPIOS\_PIN](group__devicetree-spi.md#ga1ce1031b612257718fbab08139db44cf)(inst) |
|  | Equivalent to [DT\_SPI\_DEV\_CS\_GPIOS\_PIN(DT\_DRV\_INST(inst))](group__devicetree-spi.md#ga8c1dd6a65c6f7fdf67291be1ed47fc9f "Get a SPI device's chip select GPIO pin number."). |
| #define | [DT\_INST\_SPI\_DEV\_CS\_GPIOS\_FLAGS](group__devicetree-spi.md#ga6f42b7305ec5373ae14cad220a3196da)(inst) |
|  | [DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS(DT\_DRV\_INST(inst))](group__devicetree-spi.md#ga49fd9c174931b44584a7dbbc18f7c644 "Get a SPI device's chip select GPIO flags."). |

## Detailed Description

SPI Devicetree macro public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [spi.h](devicetree_2spi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
