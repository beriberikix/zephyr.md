---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/emul__bc12_8h.html
original_path: doxygen/html/emul__bc12_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_bc12.h File Reference

Backend APIs for the BC1.2 emulators.
[More...](#details)

`#include <[zephyr/drivers/emul.h](drivers_2emul_8h_source.md)>`  
`#include <[zephyr/drivers/usb/usb_bc12.h](usb__bc12_8h_source.md)>`

[Go to the source code of this file.](emul__bc12_8h_source.md)

| Functions | |
| --- | --- |
| static int | [bc12\_emul\_set\_charging\_partner](group__b12__emulator__backend.md#gaca0e62f2f8a5ec3135523fa3a1308034) (const struct [emul](structemul.md) \*target, enum [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) partner\_type) |
|  | Set the charging partner type connected to the BC1.2 device. |
| static int | [bc12\_emul\_set\_pd\_partner](group__b12__emulator__backend.md#gaa71771a3199aef043fe313f09f3bb4f2) (const struct [emul](structemul.md) \*target, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) connected) |
|  | Set the portable device partner state. |

## Detailed Description

Backend APIs for the BC1.2 emulators.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [emul\_bc12.h](emul__bc12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
