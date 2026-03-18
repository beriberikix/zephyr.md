---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__spi__emul__interface.html
original_path: doxygen/html/group__spi__emul__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SPI Emulation Interface

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md)

SPI Emulation Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [spi\_emul](structspi__emul.md) |
|  | Node in a linked list of emulators for SPI devices. [More...](structspi__emul.md#details) |
| struct | [spi\_emul\_api](structspi__emul__api.md) |
|  | Definition of the emulator API. [More...](structspi__emul__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [spi\_emul\_io\_t](#ga034da8d578cd4facdff61ce3afb19487)) (const struct [emul](structemul.md) \*target, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Passes SPI messages to the emulator. |

| Functions | |
| --- | --- |
| int | [spi\_emul\_register](#ga6c782e1c480a9bf4640c82360e562703) (const struct [device](structdevice.md) \*dev, struct [spi\_emul](structspi__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [spi\_emul\_get\_config](#ga8b872edd18ec2911618919cc68229362) (const struct [device](structdevice.md) \*dev) |
|  | Back door to allow an emulator to retrieve the host configuration. |

## Detailed Description

SPI Emulation Interface.

## Typedef Documentation

## [◆ ](#ga034da8d578cd4facdff61ce3afb19487)spi\_emul\_io\_t

| typedef int(\* spi\_emul\_io\_t) (const struct [emul](structemul.md) \*target, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
| --- |

`#include <[spi_emul.h](spi__emul_8h.md)>`

Passes SPI messages to the emulator.

The emulator updates the data with what was read back.

Parameters
:   | target | The device Emulator instance |
    | --- | --- |
    | config | Pointer to a valid [spi\_config](structspi__config.md "SPI controller configuration structure.") structure instance. Pointer-comparison may be used to detect changes from previous operations. |
    | tx\_bufs | Buffer array where data to be sent originates from, or NULL if none. |
    | rx\_bufs | Buffer array where data to be read will be written to, or NULL if none. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## Function Documentation

## [◆ ](#ga8b872edd18ec2911618919cc68229362)spi\_emul\_get\_config()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) spi\_emul\_get\_config | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[spi_emul.h](spi__emul_8h.md)>`

Back door to allow an emulator to retrieve the host configuration.

Parameters
:   | dev | SPI device associated with the emulator |
    | --- | --- |

Returns
:   Bit-packed 32-bit value containing the device's runtime configuration

## [◆ ](#ga6c782e1c480a9bf4640c82360e562703)spi\_emul\_register()

| int spi\_emul\_register | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [spi\_emul](structspi__emul.md) \* | *emul* ) |

`#include <[spi_emul.h](spi__emul_8h.md)>`

Register an emulated device on the controller.

Parameters
:   | dev | Device that will use the emulator |
    | --- | --- |
    | [emul](structemul.md "An emulator instance - represents the target emulated device/peripheral that is interacted with throu...") | SPI emulator to use |

Returns
:   0 indicating success (always)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
