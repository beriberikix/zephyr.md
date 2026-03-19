---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/kscan_8h.html
original_path: doxygen/html/kscan_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kscan.h File Reference

Public API for Keyboard scan matrix devices.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/kscan.h>`

[Go to the source code of this file.](kscan_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) row, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) column, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pressed) |
|  | Keyboard scan callback called when user press/release a key on a matrix keyboard. |

| Functions | |
| --- | --- |
| int | [kscan\_config](group__kscan__interface.md#ga9caf0c1e798d610befcb9bdd4a50ddc5) (const struct [device](structdevice.md) \*dev, [kscan\_callback\_t](group__kscan__interface.md#gab65d45708dba142da2c71aa3debd9480) callback) |
|  | Configure a Keyboard scan instance. |
| int | [kscan\_enable\_callback](group__kscan__interface.md#gaa1d46198ea2b36526671b0c32b3b6eab) (const struct [device](structdevice.md) \*dev) |
|  | Enables callback. |
| int | [kscan\_disable\_callback](group__kscan__interface.md#ga183471b229ec08d827952c7515625e28) (const struct [device](structdevice.md) \*dev) |
|  | Disables callback. |

## Detailed Description

Public API for Keyboard scan matrix devices.

The scope of this API is simply to report which key event was triggered and users can later decode keys using their desired scan code tables in their application. In addition, typematic rate and delay can easily be implemented using a timer if desired.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [kscan.h](kscan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
