---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ps2_8h.html
original_path: doxygen/html/ps2_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ps2.h File Reference

Public API for PS/2 devices such as keyboard and mouse.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/ps2.h>`

[Go to the source code of this file.](ps2_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [ps2\_callback\_t](group__ps2__interface.md#gad7cf29301681fac0d2a359d425a13b5f)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | PS/2 callback called when user types or click a mouse. |

| Functions | |
| --- | --- |
| int | [ps2\_config](group__ps2__interface.md#ga8d6da9b966432defb0cd482003c11f15) (const struct [device](structdevice.md) \*dev, [ps2\_callback\_t](group__ps2__interface.md#gad7cf29301681fac0d2a359d425a13b5f) callback\_isr) |
|  | Configure a ps2 instance. |
| int | [ps2\_write](group__ps2__interface.md#gae291cb991ae9525552fdb52c2fa4ac5e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write to PS/2 device. |
| int | [ps2\_read](group__ps2__interface.md#gab91b1efe1f07d409607922f4eb87b221) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read slave-to-host values from PS/2 device. |
| int | [ps2\_enable\_callback](group__ps2__interface.md#ga9568487018f4ef972eb463ea2098e254) (const struct [device](structdevice.md) \*dev) |
|  | Enables callback. |
| int | [ps2\_disable\_callback](group__ps2__interface.md#gade1a470c3583e465d6a8f24a28611397) (const struct [device](structdevice.md) \*dev) |
|  | Disables callback. |

## Detailed Description

Public API for PS/2 devices such as keyboard and mouse.

Callers of this API are responsible for setting the typematic rate and decode keys using their desired scan code tables.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ps2.h](ps2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
