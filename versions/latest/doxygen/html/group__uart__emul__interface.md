---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__uart__emul__interface.html
original_path: doxygen/html/group__uart__emul__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

UART Emulation Interface

[Testing](group__testing.md) » [Emulator interface](group__io__emulators.md)

UART Emulation Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [uart\_emul](structuart__emul.md) |
|  | Node in a linked list of emulators for UART devices. [More...](structuart__emul.md#details) |
| struct | [uart\_emul\_device\_api](structuart__emul__device__api.md) |
|  | Definition of the emulator API. [More...](structuart__emul__device__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [uart\_emul\_device\_tx\_data\_ready\_t](#gab4b5940f6e0c55c594a9ccddae04c8ae)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const struct [emul](structemul.md) \*target) |
|  | Define the emulation callback function signature. |

| Functions | |
| --- | --- |
| int | [uart\_emul\_register](#gaa457b7ca5ac20a588a6fce562221e824) (const struct [device](structdevice.md) \*dev, struct [uart\_emul](structuart__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |

## Detailed Description

UART Emulation Interface.

## Typedef Documentation

## [◆ ](#gab4b5940f6e0c55c594a9ccddae04c8ae)uart\_emul\_device\_tx\_data\_ready\_t

| typedef void(\* uart\_emul\_device\_tx\_data\_ready\_t) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const struct [emul](structemul.md) \*target) |
| --- |

`#include <[uart_emul.h](uart__emul_8h.md)>`

Define the emulation callback function signature.

Parameters
:   | dev | UART device instance |
    | --- | --- |
    | size | Number of available bytes in TX buffer |
    | target | pointer to emulation context |

## Function Documentation

## [◆ ](#gaa457b7ca5ac20a588a6fce562221e824)uart\_emul\_register()

| int uart\_emul\_register | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [uart\_emul](structuart__emul.md) \* | *emul* ) |

`#include <[uart_emul.h](uart__emul_8h.md)>`

Register an emulated device on the controller.

Parameters
:   | dev | Device that will use the emulator |
    | --- | --- |
    | [emul](structemul.md "An emulator instance - represents the target emulated device/peripheral that is interacted with throu...") | UART emulator to use |

Returns
:   0 indicating success

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
