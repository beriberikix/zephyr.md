---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__espi__emul__interface.html
original_path: doxygen/html/group__espi__emul__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eSPI Emulation Interface

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md)

eSPI Emulation Interface
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [emul\_espi\_device\_api](structemul__espi__device__api.md) |
|  | Definition of the eSPI device emulator API. [More...](structemul__espi__device__api.md#details) |
| struct | [espi\_emul](structespi__emul.md) |
|  | Node in a linked list of emulators for eSPI devices. [More...](structespi__emul.md#details) |
| struct | [emul\_espi\_driver\_api](structemul__espi__driver__api.md) |
|  | Definition of the eSPI controller emulator API. [More...](structemul__espi__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [EMUL\_ESPI\_HOST\_CHIPSEL](#ga18fb55455f95a7f7ba93fdc49de2b9c0)   0 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [emul\_espi\_api\_set\_vw](#gab1068f48bf931fbc86668fb9108e07c7)) (const struct [emul](structemul.md) \*target, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Passes eSPI virtual wires set request (virtual wire packet) to the emulator. |
| typedef int(\* | [emul\_espi\_api\_get\_vw](#ga06c214788ceff221e776394318517f91)) (const struct [emul](structemul.md) \*target, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level) |
|  | Passes eSPI virtual wires get request (virtual wire packet) to the emulator. |
| typedef struct [espi\_emul](structespi__emul.md) \*(\* | [emul\_find\_emul](#gaa9e27e6a744a73a13415e01fa2c09bca)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chipsel) |
|  | Find an emulator present on a eSPI bus. |
| typedef int(\* | [emul\_trigger\_event](#ga2abff7d857738254cc4a8a939264924f)) (const struct [device](structdevice.md) \*dev, struct [espi\_event](structespi__event.md) \*evt) |
|  | Triggers an event on the emulator of eSPI controller side which causes calling specific callbacks. |

| Functions | |
| --- | --- |
| int | [espi\_emul\_register](#gaaccb8ef6060c0477151001af52310769) (const struct [device](structdevice.md) \*dev, struct [espi\_emul](structespi__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |
| int | [emul\_espi\_host\_send\_vw](#ga67deaf77a17682671ec28488ed3113fc) (const struct [device](structdevice.md) \*espi\_dev, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Sets the eSPI virtual wire on the host side, which will trigger a proper event(and callbacks) on the emulated eSPI controller. |
| int | [emul\_espi\_host\_port80\_write](#ga16c67d1d52f94b7062144e2c2f45d15a) (const struct [device](structdevice.md) \*espi\_dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Perform port80 write on the emulated host side, which will trigger a proper event(and callbacks) on the emulated eSPI controller. |

## Detailed Description

eSPI Emulation Interface

## Macro Definition Documentation

## [◆ ](#ga18fb55455f95a7f7ba93fdc49de2b9c0)EMUL\_ESPI\_HOST\_CHIPSEL

| #define EMUL\_ESPI\_HOST\_CHIPSEL   0 |
| --- |

`#include <[espi_emul.h](espi__emul_8h.md)>`

## Typedef Documentation

## [◆ ](#ga06c214788ceff221e776394318517f91)emul\_espi\_api\_get\_vw

| typedef int(\* emul\_espi\_api\_get\_vw) (const struct [emul](structemul.md) \*target, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level) |
| --- |

`#include <[espi_emul.h](espi__emul_8h.md)>`

Passes eSPI virtual wires get request (virtual wire packet) to the emulator.

The emulator returns the state (level) of its virtual wire.

Parameters
:   | target | The device Emulator instance |
    | --- | --- |
    | vw | The signal to be get. |
    | level | The level of the signal to be get. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#gab1068f48bf931fbc86668fb9108e07c7)emul\_espi\_api\_set\_vw

| typedef int(\* emul\_espi\_api\_set\_vw) (const struct [emul](structemul.md) \*target, enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
| --- |

`#include <[espi_emul.h](espi__emul_8h.md)>`

Passes eSPI virtual wires set request (virtual wire packet) to the emulator.

The emulator updates the state (level) of its virtual wire.

Parameters
:   | target | The device Emulator instance |
    | --- | --- |
    | vw | The signal to be set. |
    | level | The level of signal requested LOW(0) or HIGH(1). |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#gaa9e27e6a744a73a13415e01fa2c09bca)emul\_find\_emul

| typedef struct [espi\_emul](structespi__emul.md) \*(\* emul\_find\_emul) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int chipsel) |
| --- |

`#include <[espi_emul.h](espi__emul_8h.md)>`

Find an emulator present on a eSPI bus.

At present the function is used only to find an emulator of the host device. It may be useful in systems with the SPI flash chips.

Parameters
:   | dev | eSPI emulation controller device |
    | --- | --- |
    | chipsel | Chip-select value |

Returns
:   [espi\_emul](structespi__emul.md "Node in a linked list of emulators for eSPI devices.") to use
:   NULL if not found

## [◆ ](#ga2abff7d857738254cc4a8a939264924f)emul\_trigger\_event

| typedef int(\* emul\_trigger\_event) (const struct [device](structdevice.md) \*dev, struct [espi\_event](structespi__event.md) \*evt) |
| --- |

`#include <[espi_emul.h](espi__emul_8h.md)>`

Triggers an event on the emulator of eSPI controller side which causes calling specific callbacks.

Parameters
:   | dev | Device instance of emulated eSPI controller |
    | --- | --- |
    | evt | Event to be triggered |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## Function Documentation

## [◆ ](#ga16c67d1d52f94b7062144e2c2f45d15a)emul\_espi\_host\_port80\_write()

| int emul\_espi\_host\_port80\_write | ( | const struct [device](structdevice.md) \* | *espi\_dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) |

`#include <[espi_emul.h](espi__emul_8h.md)>`

Perform port80 write on the emulated host side, which will trigger a proper event(and callbacks) on the emulated eSPI controller.

Parameters
:   | espi\_dev | eSPI emulation controller device |
    | --- | --- |
    | data | The date to be written. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga67deaf77a17682671ec28488ed3113fc)emul\_espi\_host\_send\_vw()

| int emul\_espi\_host\_send\_vw | ( | const struct [device](structdevice.md) \* | *espi\_dev*, |
| --- | --- | --- | --- |
|  |  | enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) | *vw*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level* ) |

`#include <[espi_emul.h](espi__emul_8h.md)>`

Sets the eSPI virtual wire on the host side, which will trigger a proper event(and callbacks) on the emulated eSPI controller.

Parameters
:   | espi\_dev | eSPI emulation controller device |
    | --- | --- |
    | vw | The signal to be set. |
    | level | The level of the signal to be set. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#gaaccb8ef6060c0477151001af52310769)espi\_emul\_register()

| int espi\_emul\_register | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [espi\_emul](structespi__emul.md) \* | *emul* ) |

`#include <[espi_emul.h](espi__emul_8h.md)>`

Register an emulated device on the controller.

Parameters
:   | dev | Device that will use the emulator |
    | --- | --- |
    | [emul](structemul.md "An emulator instance - represents the target emulated device/peripheral that is interacted with throu...") | eSPI emulator to use |

Returns
:   0 indicating success (always)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
