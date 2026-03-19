---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mspi__emul__interface.html
original_path: doxygen/html/group__mspi__emul__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MSPI Emulation Interface

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md)

MSPI Emulation Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [emul\_mspi\_device\_api](structemul__mspi__device__api.md) |
|  | Definition of the MSPI device emulator API. [More...](structemul__mspi__device__api.md#details) |
| struct | [mspi\_emul](structmspi__emul.md) |
|  | Node in a linked list of emulators for MSPI devices. [More...](structmspi__emul.md#details) |
| struct | [emul\_mspi\_driver\_api](structemul__mspi__driver__api.md) |
|  | Definition of the MSPI controller emulator API. [More...](structemul__mspi__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef struct [mspi\_emul](structmspi__emul.md) \*(\* | [mspi\_emul\_find\_emul](#gabecb33236ed3a6a93a28edef0a4c3ae7)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_idx) |
|  | Find an emulator present on a MSPI bus. |
| typedef int(\* | [mspi\_emul\_trigger\_event](#gaaa0c99ea6582cacba89f8630d8d554be)) (const struct [device](structdevice.md) \*dev, enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type) |
|  | Triggers an event on the emulator of MSPI controller side which causes calling specific callbacks. |
| typedef int(\* | [emul\_mspi\_dev\_api\_transceive](#ga15df8cc9ccc2831c5446002e864f1717)) (const struct [emul](structemul.md) \*target, const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) \*packets, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_packet, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) async, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout) |
|  | Loopback MSPI transceive request to the device emulator as no real hardware attached. |

| Functions | |
| --- | --- |
| int | [mspi\_emul\_register](#ga98c9a359f3385f49fbfe52b27254d261) (const struct [device](structdevice.md) \*dev, struct [mspi\_emul](structmspi__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |

## Detailed Description

MSPI Emulation Interface.

## Typedef Documentation

## [◆ ](#ga15df8cc9ccc2831c5446002e864f1717)emul\_mspi\_dev\_api\_transceive

| typedef int(\* emul\_mspi\_dev\_api\_transceive) (const struct [emul](structemul.md) \*target, const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) \*packets, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_packet, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) async, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout) |
| --- |

`#include <[mspi_emul.h](mspi__emul_8h.md)>`

Loopback MSPI transceive request to the device emulator as no real hardware attached.

Parameters
:   | target | The device Emulator instance |
    | --- | --- |
    | packets | Pointer to the buffers of command, addr, data and etc. |
    | num\_packet | The number of packets in packets. |
    | async | Indicate whether this is a asynchronous request. |
    | timeout | Maximum Time allowed for this request |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#gabecb33236ed3a6a93a28edef0a4c3ae7)mspi\_emul\_find\_emul

| typedef struct [mspi\_emul](structmspi__emul.md) \*(\* mspi\_emul\_find\_emul) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dev\_idx) |
| --- |

`#include <[mspi_emul.h](mspi__emul_8h.md)>`

Find an emulator present on a MSPI bus.

At present the function is used only to find an emulator of the host device. It may be useful in systems with the SPI flash chips.

Parameters
:   | dev | MSPI emulation controller device |
    | --- | --- |
    | dev\_idx | Device index from device tree. |

Returns
:   [mspi\_emul](structmspi__emul.md "Node in a linked list of emulators for MSPI devices.") to use
:   NULL if not found

## [◆ ](#gaaa0c99ea6582cacba89f8630d8d554be)mspi\_emul\_trigger\_event

| typedef int(\* mspi\_emul\_trigger\_event) (const struct [device](structdevice.md) \*dev, enum [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5) evt\_type) |
| --- |

`#include <[mspi_emul.h](mspi__emul_8h.md)>`

Triggers an event on the emulator of MSPI controller side which causes calling specific callbacks.

Parameters
:   | dev | MSPI emulation controller device |
    | --- | --- |
    | evt\_type | Event type to be triggered |

See also
:   [mspi\_bus\_event](group__mspi__interface.md#ga4cd05950729893e08ef0d4a12e2242d5 "MSPI bus event.")

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## Function Documentation

## [◆ ](#ga98c9a359f3385f49fbfe52b27254d261)mspi\_emul\_register()

| int mspi\_emul\_register | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [mspi\_emul](structmspi__emul.md) \* | *emul* ) |

`#include <[mspi_emul.h](mspi__emul_8h.md)>`

Register an emulated device on the controller.

Parameters
:   | dev | MSPI emulation controller device |
    | --- | --- |
    | [emul](structemul.md "An emulator instance - represents the target emulated device/peripheral that is interacted with throu...") | MSPI device emulator to be registered |

Returns
:   0 indicating success (always)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
