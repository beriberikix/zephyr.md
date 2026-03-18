---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__uart__mux__interface.html
original_path: doxygen/html/group__uart__mux__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

UART Mux Interface

[Device Driver APIs](group__io__interfaces.md)

UART Mux Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [uart\_mux\_driver\_api](structuart__mux__driver__api.md) |
|  | UART mux driver API structure. [More...](structuart__mux__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [uart\_mux\_attach\_cb\_t](#ga9796bc90e4feca3b7e775e1107b74cf3)) (const struct [device](structdevice.md) \*mux, int dlci\_address, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) connected, void \*user\_data) |
|  | Define the user callback function which is called when the UART mux is attached properly. |
| typedef void(\* | [uart\_mux\_cb\_t](#ga018c77c05511ae829f4f9c64c197e52d)) (const struct [device](structdevice.md) \*uart, const struct [device](structdevice.md) \*dev, int dlci\_address, void \*user\_data) |
|  | Callback used while iterating over UART muxes. |

| Functions | |
| --- | --- |
| static int | [uart\_mux\_attach](#gaae2cc4e03f5e4536b945746cf689fe56) (const struct [device](structdevice.md) \*mux, const struct [device](structdevice.md) \*uart, int dlci\_address, [uart\_mux\_attach\_cb\_t](#ga9796bc90e4feca3b7e775e1107b74cf3) cb, void \*user\_data) |
|  | Attach physical/real UART to UART muxing device. |
| const struct [device](structdevice.md) \* | [uart\_mux\_find](#ga551b58a43626981af2be757f44206ccc) (int dlci\_address) |
|  | Get UART related to a specific DLCI channel. |
| const struct [device](structdevice.md) \* | [uart\_mux\_alloc](#gaac6d68c5f53f60b5dfb1191a85429144) (void) |
|  | Allocate muxing UART device. |
| void | [uart\_mux\_foreach](#gae7f1271a6fac1edd388bd8add3b01614) ([uart\_mux\_cb\_t](#ga018c77c05511ae829f4f9c64c197e52d) cb, void \*user\_data) |
|  | Go through all the UART muxes and call callback for each of them. |
| void | [uart\_mux\_disable](#ga3e9871415092eba11a7be262ae4da0a2) (const struct [device](structdevice.md) \*dev) |
|  | Disable the mux. |
| void | [uart\_mux\_enable](#gad832440ec0f4157fc895a1ec05081337) (const struct [device](structdevice.md) \*dev) |
|  | Enable the mux. |

## Detailed Description

UART Mux Interface.

## Typedef Documentation

## [◆ ](#ga9796bc90e4feca3b7e775e1107b74cf3)uart\_mux\_attach\_cb\_t

| typedef void(\* uart\_mux\_attach\_cb\_t) (const struct [device](structdevice.md) \*mux, int dlci\_address, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) connected, void \*user\_data) |
| --- |

`#include <[uart_mux.h](uart__mux_8h.md)>`

Define the user callback function which is called when the UART mux is attached properly.

Parameters
:   | mux | UART mux device |
    | --- | --- |
    | dlci\_address | DLCI id for the virtual muxing channel |
    | connected | True if DLCI is connected, false otherwise. |
    | user\_data | Arbitrary user data. |

## [◆ ](#ga018c77c05511ae829f4f9c64c197e52d)uart\_mux\_cb\_t

| typedef void(\* uart\_mux\_cb\_t) (const struct [device](structdevice.md) \*uart, const struct [device](structdevice.md) \*dev, int dlci\_address, void \*user\_data) |
| --- |

`#include <[uart_mux.h](uart__mux_8h.md)>`

Callback used while iterating over UART muxes.

Parameters
:   | uart | Pointer to UART device where the mux is running |
    | --- | --- |
    | dev | Pointer to UART mux device |
    | dlci\_address | DLCI channel id this UART is muxed |
    | user\_data | A valid pointer to user data or NULL |

## Function Documentation

## [◆ ](#gaac6d68c5f53f60b5dfb1191a85429144)uart\_mux\_alloc()

| const struct [device](structdevice.md) \* uart\_mux\_alloc | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart_mux.h](uart__mux_8h.md)>`

Allocate muxing UART device.

This will return next available uart mux driver that will mux the data when read or written. This device corresponds to one DLCI channel. User must first call this to allocate the DLCI and then call the attach function to fully enable the muxing.

Return values
:   | [device](structdevice.md "Runtime device structure (in ROM) per driver instance.") | New UART device that will automatically mux data sent to it. |
    | --- | --- |
    | NULL | if error |

## [◆ ](#gaae2cc4e03f5e4536b945746cf689fe56)uart\_mux\_attach()

| | int uart\_mux\_attach | ( | const struct [device](structdevice.md) \* | *mux*, | | --- | --- | --- | --- | |  |  | const struct [device](structdevice.md) \* | *uart*, | |  |  | int | *dlci\_address*, | |  |  | [uart\_mux\_attach\_cb\_t](#ga9796bc90e4feca3b7e775e1107b74cf3) | *cb*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[uart_mux.h](uart__mux_8h.md)>`

Attach physical/real UART to UART muxing device.

Parameters
:   | mux | UART mux device structure. |
    | --- | --- |
    | uart | Real UART device structure. |
    | dlci\_address | DLCI id for the virtual muxing channel |
    | cb | Callback is called when the DLCI is ready and connected |
    | user\_data | Caller supplied optional data |

Return values
:   | 0 | No errors, the attachment was successful |
    | --- | --- |
    | <0 | Error |

## [◆ ](#ga3e9871415092eba11a7be262ae4da0a2)uart\_mux\_disable()

| void uart\_mux\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart_mux.h](uart__mux_8h.md)>`

Disable the mux.

Disable does not re-instate whatever ISRs and configs were present before the mux was enabled. This must be done by the user.

Parameters
:   | dev | UART mux device pointer |
    | --- | --- |

## [◆ ](#gad832440ec0f4157fc895a1ec05081337)uart\_mux\_enable()

| void uart\_mux\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart_mux.h](uart__mux_8h.md)>`

Enable the mux.

Enables the correct ISRs for the UART mux.

Parameters
:   | dev | UART mux device pointer |
    | --- | --- |

## [◆ ](#ga551b58a43626981af2be757f44206ccc)uart\_mux\_find()

| const struct [device](structdevice.md) \* uart\_mux\_find | ( | int | *dlci\_address* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[uart_mux.h](uart__mux_8h.md)>`

Get UART related to a specific DLCI channel.

Parameters
:   | dlci\_address | DLCI address, value >0 and <63 |
    | --- | --- |

Returns
:   UART device if found, NULL otherwise

## [◆ ](#gae7f1271a6fac1edd388bd8add3b01614)uart\_mux\_foreach()

| void uart\_mux\_foreach | ( | [uart\_mux\_cb\_t](#ga018c77c05511ae829f4f9c64c197e52d) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[uart_mux.h](uart__mux_8h.md)>`

Go through all the UART muxes and call callback for each of them.

Parameters
:   | cb | User-supplied callback function to call |
    | --- | --- |
    | user\_data | User specified data |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
