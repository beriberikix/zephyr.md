---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__i2c__emul__interface.html
original_path: doxygen/html/group__i2c__emul__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I2C Emulation Interface

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md)

I2C Emulation Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [i2c\_emul](structi2c__emul.md) |
|  | Node in a linked list of emulators for I2C devices. [More...](structi2c__emul.md#details) |
| struct | [i2c\_emul\_api](structi2c__emul__api.md) |
|  | Definition of the emulator API. [More...](structi2c__emul__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [i2c\_emul\_transfer\_t](#ga1b27ff11534eeac47cf50ffb2a1c7cca)) (const struct [emul](structemul.md) \*target, struct [i2c\_msg](structi2c__msg.md) \*msgs, int num\_msgs, int addr) |
|  | Passes I2C messages to the emulator. |

| Functions | |
| --- | --- |
| int | [i2c\_emul\_register](#ga92851f09c23531bbaea25301dc2607ce) (const struct [device](structdevice.md) \*dev, struct [i2c\_emul](structi2c__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |

## Detailed Description

I2C Emulation Interface.

## Typedef Documentation

## [◆ ](#ga1b27ff11534eeac47cf50ffb2a1c7cca)i2c\_emul\_transfer\_t

| typedef int(\* i2c\_emul\_transfer\_t) (const struct [emul](structemul.md) \*target, struct [i2c\_msg](structi2c__msg.md) \*msgs, int num\_msgs, int addr) |
| --- |

`#include <[i2c_emul.h](i2c__emul_8h.md)>`

Passes I2C messages to the emulator.

The emulator updates the data with what was read back.

Parameters
:   | target | The device Emulator instance. |
    | --- | --- |
    | msgs | Array of messages to transfer. For 'read' messages, this function updates the 'buf' member with the data that was read. |
    | num\_msgs | Number of messages to transfer. |
    | addr | Address of the I2C target device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## Function Documentation

## [◆ ](#ga92851f09c23531bbaea25301dc2607ce)i2c\_emul\_register()

| int i2c\_emul\_register | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [i2c\_emul](structi2c__emul.md) \* | *emul* ) |

`#include <[i2c_emul.h](i2c__emul_8h.md)>`

Register an emulated device on the controller.

Parameters
:   | dev | Device that will use the emulator |
    | --- | --- |
    | [emul](structemul.md "An emulator instance - represents the target emulated device/peripheral that is interacted with throu...") | I2C emulator to use |

Returns
:   0 indicating success (always)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
