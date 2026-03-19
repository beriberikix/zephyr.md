---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uart__emul_8h.html
original_path: doxygen/html/uart__emul_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_emul.h File Reference

Public APIs for the UART device emulation drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/emul.h](drivers_2emul_8h_source.md)>`  
`#include <[zephyr/drivers/uart.h](drivers_2uart_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](uart__emul_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uart\_emul](structuart__emul.md) |
|  | Node in a linked list of emulators for UART devices. [More...](structuart__emul.md#details) |
| struct | [uart\_emul\_device\_api](structuart__emul__device__api.md) |
|  | Definition of the emulator API. [More...](structuart__emul__device__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [uart\_emul\_device\_tx\_data\_ready\_t](group__uart__emul__interface.md#gab4b5940f6e0c55c594a9ccddae04c8ae)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const struct [emul](structemul.md) \*target) |
|  | Define the emulation callback function signature. |

| Functions | |
| --- | --- |
| int | [uart\_emul\_register](group__uart__emul__interface.md#gaa457b7ca5ac20a588a6fce562221e824) (const struct [device](structdevice.md) \*dev, struct [uart\_emul](structuart__emul.md) \*[emul](structemul.md)) |
|  | Register an emulated device on the controller. |

## Detailed Description

Public APIs for the UART device emulation drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart\_emul.h](uart__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
