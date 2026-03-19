---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/i2c__emul_8h.html
original_path: doxygen/html/i2c__emul_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_emul.h File Reference

Public APIs for the I2C emulation drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/emul.h](drivers_2emul_8h_source.md)>`  
`#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](i2c__emul_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i2c\_emul](structi2c__emul.md) |
|  | Node in a linked list of emulators for I2C devices. [More...](structi2c__emul.md#details) |
| struct | [i2c\_emul\_api](structi2c__emul__api.md) |
|  | Definition of the emulator API. [More...](structi2c__emul__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [i2c\_emul\_transfer\_t](group__i2c__emul__interface.md#ga1b27ff11534eeac47cf50ffb2a1c7cca)) (const struct [emul](structemul.md) \*target, struct [i2c\_msg](structi2c__msg.md) \*msgs, int num\_msgs, int addr) |
|  | Passes I2C messages to the emulator. |

| Functions | |
| --- | --- |
| int | [i2c\_emul\_register](group__i2c__emul__interface.md#ga92851f09c23531bbaea25301dc2607ce) (const struct [device](structdevice.md) \*dev, struct [i2c\_emul](structi2c__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |

## Detailed Description

Public APIs for the I2C emulation drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c\_emul.h](i2c__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
