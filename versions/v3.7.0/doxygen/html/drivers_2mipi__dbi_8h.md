---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2mipi__dbi_8h.html
original_path: doxygen/html/drivers_2mipi__dbi_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dbi.h File Reference

Public APIs for MIPI-DBI drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/display.h](display_8h_source.md)>`  
`#include <[zephyr/display/mipi_display.h](mipi__display_8h_source.md)>`  
`#include <[zephyr/drivers/spi.h](drivers_2spi_8h_source.md)>`  
`#include <[zephyr/dt-bindings/mipi_dbi/mipi_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h_source.md)>`

[Go to the source code of this file.](drivers_2mipi__dbi_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mipi\_dbi\_config](structmipi__dbi__config.md) |
|  | MIPI DBI controller configuration. [More...](structmipi__dbi__config.md#details) |
| struct | [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) |
|  | MIPI-DBI host driver API. [More...](structmipi__dbi__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [MIPI\_DBI\_SPI\_CONFIG\_DT](group__mipi__dbi__interface.md#ga9e05938ce1cd2b647cb00a77b773ad1d)(node\_id, operation\_, delay\_) |
|  | initialize a MIPI DBI SPI configuration struct from devicetree |
| #define | [MIPI\_DBI\_SPI\_CONFIG\_DT\_INST](group__mipi__dbi__interface.md#ga93d0c043dc9022bbe42c21a13bc46091)(inst, operation\_, delay\_) |
|  | Initialize a MIPI DBI SPI configuration from devicetree instance. |
| #define | [MIPI\_DBI\_CONFIG\_DT](group__mipi__dbi__interface.md#ga94aed5adf0dc393556b2c8c9976aeddf)(node\_id, operation\_, delay\_) |
|  | Initialize a MIPI DBI configuration from devicetree. |
| #define | [MIPI\_DBI\_CONFIG\_DT\_INST](group__mipi__dbi__interface.md#ga658456683f895d3b44ea44d9bf8b0558)(inst, operation\_, delay\_) |
|  | Initialize a MIPI DBI configuration from device instance. |

| Functions | |
| --- | --- |
| static int | [mipi\_dbi\_command\_write](group__mipi__dbi__interface.md#gad36e3d57fd931236c4ed4e58dfef1cca) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write a command to the display controller. |
| static int | [mipi\_dbi\_command\_read](group__mipi__dbi__interface.md#gafac64feca9fdee3803154bacb58e8e47) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_cmd, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read a command response from the display controller. |
| static int | [mipi\_dbi\_write\_display](group__mipi__dbi__interface.md#ga62aa7b9677da010a678580d956f7d0e3) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf, struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc, enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt) |
|  | Write a display buffer to the display controller. |
| static int | [mipi\_dbi\_reset](group__mipi__dbi__interface.md#ga2d04bcd271ba2fd6338f8ac9e787e114) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay) |
|  | Resets attached display controller. |
| static int | [mipi\_dbi\_release](group__mipi__dbi__interface.md#gade0b635bcd4f16fb3ec5d122d1b09161) (const struct [device](structdevice.md) \*dev, const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config) |
|  | Releases a locked MIPI DBI device. |

## Detailed Description

Public APIs for MIPI-DBI drivers.

MIPI-DBI defines the following 3 interfaces: Type A: Motorola 6800 type parallel bus Type B: Intel 8080 type parallel bus Type C: SPI Type (1 bit bus) with 3 options:

1. 9 write clocks per byte, final bit is command/data selection bit
2. Same as above, but 16 write clocks per byte
3. 8 write clocks per byte. Command/data selected via GPIO pin The current driver interface only supports type C modes 1 and 3

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mipi\_dbi.h](drivers_2mipi__dbi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
