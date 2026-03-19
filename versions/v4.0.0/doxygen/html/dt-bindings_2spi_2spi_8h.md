---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dt-bindings_2spi_2spi_8h.html
original_path: doxygen/html/dt-bindings_2spi_2spi_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi.h File Reference

[Go to the source code of this file.](dt-bindings_2spi_2spi_8h_source.md)

| Macros | |
| --- | --- |
| SPI duplex mode | |
| Some controllers support half duplex transfer, which results in 3-wire usage.  By default, full duplex will prevail. | |
| #define | [SPI\_FULL\_DUPLEX](group__spi__interface.md#ga5585d5e81dec606b605f31b6745c35d3)   (0U << 11) |
| #define | [SPI\_HALF\_DUPLEX](group__spi__interface.md#ga602a7804b7434d7ebc1ebe6cb9b47a2f)   (1U << 11) |
| SPI Frame Format | |
| 2 frame formats are exposed: Motorola and TI.  The main difference is the behavior of the CS line. In Motorola it stays active the whole transfer. In TI, it's active only one serial clock period prior to actually make the transfer, it is thus inactive during the transfer, which ends when the clocks ends as well. By default, as it is the most commonly used, the Motorola frame format will prevail. | |
| #define | [SPI\_FRAME\_FORMAT\_MOTOROLA](group__spi__interface.md#ga6a1b4ba33900165b6e09706903a6e6ee)   (0U << 15) |
| #define | [SPI\_FRAME\_FORMAT\_TI](group__spi__interface.md#ga22801357a9682371e3d8a10e522de388)   (1U << 15) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [spi](dir_e8bda77a9a98fea6a6fc6d1fc5fef4b9.md)
- [spi.h](dt-bindings_2spi_2spi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
