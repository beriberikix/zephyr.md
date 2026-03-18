---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/spi__emul_8h.html
original_path: doxygen/html/spi__emul_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi\_emul.h File Reference

Public APIs for the SPI emulation drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/emul.h](drivers_2emul_8h_source.md)>`  
`#include <[zephyr/drivers/spi.h](drivers_2spi_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](spi__emul_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [spi\_emul](structspi__emul.md) |
|  | Node in a linked list of emulators for SPI devices. [More...](structspi__emul.md#details) |
| struct | [spi\_emul\_api](structspi__emul__api.md) |
|  | Definition of the emulator API. [More...](structspi__emul__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [spi\_emul\_io\_t](group__spi__emul__interface.md#ga034da8d578cd4facdff61ce3afb19487)) (const struct [emul](structemul.md) \*target, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Passes SPI messages to the emulator. |

| Functions | |
| --- | --- |
| int | [spi\_emul\_register](group__spi__emul__interface.md#ga6c782e1c480a9bf4640c82360e562703) (const struct [device](structdevice.md) \*dev, struct [spi\_emul](structspi__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [spi\_emul\_get\_config](group__spi__emul__interface.md#ga8b872edd18ec2911618919cc68229362) (const struct [device](structdevice.md) \*dev) |
|  | Back door to allow an emulator to retrieve the host configuration. |

## Detailed Description

Public APIs for the SPI emulation drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [spi\_emul.h](spi__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
