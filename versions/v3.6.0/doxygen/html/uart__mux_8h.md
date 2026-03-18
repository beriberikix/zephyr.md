---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/uart__mux_8h.html
original_path: doxygen/html/uart__mux_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_mux.h File Reference

Public APIs for UART MUX drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/uart.h](drivers_2uart_8h_source.md)>`  
`#include <syscalls/uart_mux.h>`

[Go to the source code of this file.](uart__mux_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uart\_mux\_driver\_api](structuart__mux__driver__api.md) |
|  | UART mux driver API structure. [More...](structuart__mux__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [uart\_mux\_attach\_cb\_t](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3)) (const struct [device](structdevice.md) \*mux, int dlci\_address, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) connected, void \*user\_data) |
|  | Define the user callback function which is called when the UART mux is attached properly. |
| typedef void(\* | [uart\_mux\_cb\_t](group__uart__mux__interface.md#ga018c77c05511ae829f4f9c64c197e52d)) (const struct [device](structdevice.md) \*uart, const struct [device](structdevice.md) \*dev, int dlci\_address, void \*user\_data) |
|  | Callback used while iterating over UART muxes. |

| Functions | |
| --- | --- |
| static int | [uart\_mux\_attach](group__uart__mux__interface.md#gaae2cc4e03f5e4536b945746cf689fe56) (const struct [device](structdevice.md) \*mux, const struct [device](structdevice.md) \*uart, int dlci\_address, [uart\_mux\_attach\_cb\_t](group__uart__mux__interface.md#ga9796bc90e4feca3b7e775e1107b74cf3) cb, void \*user\_data) |
|  | Attach physical/real UART to UART muxing device. |
| const struct [device](structdevice.md) \* | [uart\_mux\_find](group__uart__mux__interface.md#ga551b58a43626981af2be757f44206ccc) (int dlci\_address) |
|  | Get UART related to a specific DLCI channel. |
| const struct [device](structdevice.md) \* | [uart\_mux\_alloc](group__uart__mux__interface.md#gaac6d68c5f53f60b5dfb1191a85429144) (void) |
|  | Allocate muxing UART device. |
| void | [uart\_mux\_foreach](group__uart__mux__interface.md#gae7f1271a6fac1edd388bd8add3b01614) ([uart\_mux\_cb\_t](group__uart__mux__interface.md#ga018c77c05511ae829f4f9c64c197e52d) cb, void \*user\_data) |
|  | Go through all the UART muxes and call callback for each of them. |
| void | [uart\_mux\_disable](group__uart__mux__interface.md#ga3e9871415092eba11a7be262ae4da0a2) (const struct [device](structdevice.md) \*dev) |
|  | Disable the mux. |
| void | [uart\_mux\_enable](group__uart__mux__interface.md#gad832440ec0f4157fc895a1ec05081337) (const struct [device](structdevice.md) \*dev) |
|  | Enable the mux. |

## Detailed Description

Public APIs for UART MUX drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [uart\_mux.h](uart__mux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
