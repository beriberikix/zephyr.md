---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__uart__polling.html
original_path: doxygen/html/group__uart__polling.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Polling UART API

[Device Driver APIs](group__io__interfaces.md) » [UART Interface](group__uart__interface.md)

| Functions | |
| --- | --- |
| int | [uart\_poll\_in](#gae81ac8cc976a20d774cfbda09e9c983d) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*p\_char) |
|  | Read a character from the device for input. |
| int | [uart\_poll\_in\_u16](#gaad39c1358019bfdcb919da7982743553) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16) |
|  | Read a 16-bit datum from the device for input. |
| void | [uart\_poll\_out](#ga06ba27ba772a7a18462b8cdbc7f9353c) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char out\_char) |
|  | Write a character to the device for output. |
| void | [uart\_poll\_out\_u16](#ga8faa3f58b9098c97e288e9c5f3367fd9) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16) |
|  | Write a 16-bit datum to the device for output. |

## Detailed Description

## Function Documentation

## [◆ ](#gae81ac8cc976a20d774cfbda09e9c983d)uart\_poll\_in()

| int uart\_poll\_in | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \* | *p\_char* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Read a character from the device for input.

This routine checks if the receiver has valid data. When the receiver has valid data, it reads a character from the device, stores to the location pointed to by p\_char, and returns 0 to the calling thread. It returns -1, otherwise. This function is a non-blocking call.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | p\_char | Pointer to character. |

Return values
:   | 0 | If a character arrived. |
    | --- | --- |
    | -1 | If no character was available to read (i.e. the UART input buffer was empty). |
    | -ENOSYS | If the operation is not implemented. |
    | -EBUSY | If async reception was enabled using [uart\_rx\_enable](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8 "uart_rx_enable") |

## [◆ ](#gaad39c1358019bfdcb919da7982743553)uart\_poll\_in\_u16()

| int uart\_poll\_in\_u16 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *p\_u16* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Read a 16-bit datum from the device for input.

This routine checks if the receiver has valid data. When the receiver has valid data, it reads a 16-bit datum from the device, stores to the location pointed to by p\_u16, and returns 0 to the calling thread. It returns -1, otherwise. This function is a non-blocking call.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | p\_u16 | Pointer to 16-bit data. |

Return values
:   | 0 | If data arrived. |
    | --- | --- |
    | -1 | If no data was available to read (i.e., the UART input buffer was empty). |
    | -ENOTSUP | If API is not enabled. |
    | -ENOSYS | If the function is not implemented. |
    | -EBUSY | If async reception was enabled using [uart\_rx\_enable](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8 "uart_rx_enable") |

## [◆ ](#ga06ba27ba772a7a18462b8cdbc7f9353c)uart\_poll\_out()

| void uart\_poll\_out | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | *out\_char* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Write a character to the device for output.

This routine checks if the transmitter is full. When the transmitter is not full, it writes a character to the data register. It waits and blocks the calling thread, otherwise. This function is a blocking call.

To send a character when hardware flow control is enabled, the handshake signal CTS must be asserted.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | out\_char | Character to send. |

## [◆ ](#ga8faa3f58b9098c97e288e9c5f3367fd9)uart\_poll\_out\_u16()

| void uart\_poll\_out\_u16 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *out\_u16* ) |

`#include <[uart.h](drivers_2uart_8h.md)>`

Write a 16-bit datum to the device for output.

This routine checks if the transmitter is full. When the transmitter is not full, it writes a 16-bit datum to the data register. It waits and blocks the calling thread, otherwise. This function is a blocking call.

To send a datum when hardware flow control is enabled, the handshake signal CTS must be asserted.

Parameters
:   | dev | UART device instance. |
    | --- | --- |
    | out\_u16 | Wide data to send. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
