---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/target__device_8h.html
original_path: doxygen/html/target__device_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

target\_device.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](target__device_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i3c\_config\_target](structi3c__config__target.md) |
|  | Configuration parameters for I3C hardware to act as target device. [More...](structi3c__config__target.md#details) |
| struct | [i3c\_target\_config](structi3c__target__config.md) |
|  | Structure describing a device that supports the I3C target API. [More...](structi3c__target__config.md#details) |
| struct | [i3c\_target\_callbacks](structi3c__target__callbacks.md) |
| struct | [i3c\_target\_driver\_api](structi3c__target__driver__api.md) |

| Functions | |
| --- | --- |
| static int | [i3c\_target\_tx\_write](group__i3c__target__device.md#ga5d9e529f4c2eeccbedf491532dc209e2) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Writes to the target's TX FIFO. |
| static int | [i3c\_target\_register](group__i3c__target__device.md#gaf13d2b84a91e17d5ec49a41e9c553d42) (const struct [device](structdevice.md) \*dev, struct [i3c\_target\_config](structi3c__target__config.md) \*cfg) |
|  | Registers the provided config as target device of a controller. |
| static int | [i3c\_target\_unregister](group__i3c__target__device.md#ga3dc0e6451fb13fa063c5ec3e18fe22e4) (const struct [device](structdevice.md) \*dev, struct [i3c\_target\_config](structi3c__target__config.md) \*cfg) |
|  | Unregisters the provided config as target device. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [target\_device.h](target__device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
