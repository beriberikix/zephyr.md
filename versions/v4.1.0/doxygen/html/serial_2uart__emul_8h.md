---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/serial_2uart__emul_8h.html
original_path: doxygen/html/serial_2uart__emul_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_emul.h File Reference

Backend API for emulated UART.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](serial_2uart__emul_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [uart\_emul\_callback\_tx\_data\_ready\_t](#ad31912ff18e7c7faf9849322d9c8a55b)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*user\_data) |
|  | Define the application callback function signature for [uart\_emul\_callback\_tx\_data\_ready\_set()](#af3abd76a768e8031a1bba533f74044be) function. |

| Functions | |
| --- | --- |
| void | [uart\_emul\_callback\_tx\_data\_ready\_set](#af3abd76a768e8031a1bba533f74044be) (const struct [device](structdevice.md) \*dev, [uart\_emul\_callback\_tx\_data\_ready\_t](#ad31912ff18e7c7faf9849322d9c8a55b) cb, void \*user\_data) |
|  | Set the TX data ready callback. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [uart\_emul\_put\_rx\_data](#ad0a91bf5b91639c912f41bd93aeacd69) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write (copy) data to RX buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [uart\_emul\_get\_tx\_data](#ae8aba3de78a625318524abfd46da1daa) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Read data from TX buffer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [uart\_emul\_flush\_rx\_data](#a33278a5d083c2bb26cbd11088a1cba2e) (const struct [device](structdevice.md) \*dev) |
|  | Clear RX buffer content. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [uart\_emul\_flush\_tx\_data](#a1b7ee65706693f0489e6464bc04f689b) (const struct [device](structdevice.md) \*dev) |
|  | Clear TX buffer content. |
| void | [uart\_emul\_set\_errors](#a305c155ed8a824e7ddec0ad078669aa0) (const struct [device](structdevice.md) \*dev, int errors) |
|  | Sets one or more driver errors. |
| void | [uart\_emul\_set\_release\_buffer\_on\_timeout](#af15ff078214f0c7a96fc8c0091a8f922) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) release\_on\_timeout) |
|  | Configures if rx buffer should be released on timeout, even when only partially filled. |

## Detailed Description

Backend API for emulated UART.

## Typedef Documentation

## [◆ ](#ad31912ff18e7c7faf9849322d9c8a55b)uart\_emul\_callback\_tx\_data\_ready\_t

| typedef void(\* uart\_emul\_callback\_tx\_data\_ready\_t) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*user\_data) |
| --- |

Define the application callback function signature for [uart\_emul\_callback\_tx\_data\_ready\_set()](#af3abd76a768e8031a1bba533f74044be) function.

Parameters
:   | dev | UART device instance |
    | --- | --- |
    | size | Number of available bytes in TX buffer |
    | user\_data | Arbitrary user data |

## Function Documentation

## [◆ ](#af3abd76a768e8031a1bba533f74044be)uart\_emul\_callback\_tx\_data\_ready\_set()

| void uart\_emul\_callback\_tx\_data\_ready\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uart\_emul\_callback\_tx\_data\_ready\_t](#ad31912ff18e7c7faf9849322d9c8a55b) | *cb*, |
|  |  | void \* | *user\_data* ) |

Set the TX data ready callback.

This sets up the callback that is called every time data was appended to the TX buffer.

Parameters
:   | dev | The emulated UART device instance |
    | --- | --- |
    | cb | Pointer to the callback function |
    | user\_data | Data to pass to callback function |

## [◆ ](#a33278a5d083c2bb26cbd11088a1cba2e)uart\_emul\_flush\_rx\_data()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uart\_emul\_flush\_rx\_data | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Clear RX buffer content.

Parameters
:   | dev | The emulated UART device instance |
    | --- | --- |

Returns
:   Number of cleared bytes

## [◆ ](#a1b7ee65706693f0489e6464bc04f689b)uart\_emul\_flush\_tx\_data()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uart\_emul\_flush\_tx\_data | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Clear TX buffer content.

Parameters
:   | dev | The emulated UART device instance |
    | --- | --- |

Returns
:   Number of cleared bytes

## [◆ ](#ae8aba3de78a625318524abfd46da1daa)uart\_emul\_get\_tx\_data()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uart\_emul\_get\_tx\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

Read data from TX buffer.

Parameters
:   | dev | The emulated UART device instance |
    | --- | --- |
    | data | The address of the output buffer |
    | size | Number of bytes to read |

Returns
:   Number of bytes written to the output buffer

## [◆ ](#ad0a91bf5b91639c912f41bd93aeacd69)uart\_emul\_put\_rx\_data()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uart\_emul\_put\_rx\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

Write (copy) data to RX buffer.

Parameters
:   | dev | The emulated UART device instance |
    | --- | --- |
    | data | The data to append |
    | size | Number of bytes to append |

Returns
:   Number of bytes appended

## [◆ ](#a305c155ed8a824e7ddec0ad078669aa0)uart\_emul\_set\_errors()

| void uart\_emul\_set\_errors | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *errors* ) |

Sets one or more driver errors.

Parameters
:   | dev | The emulated UART device instance |
    | --- | --- |
    | errors | The [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88 "uart_rx_stop_reason") errors to set |

## [◆ ](#af15ff078214f0c7a96fc8c0091a8f922)uart\_emul\_set\_release\_buffer\_on\_timeout()

| void uart\_emul\_set\_release\_buffer\_on\_timeout | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *release\_on\_timeout* ) |

Configures if rx buffer should be released on timeout, even when only partially filled.

Parameters
:   | dev | The emulated UART device instance |
    | --- | --- |
    | release\_on\_timeout | When true, buffer will be released on timeout |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [serial](dir_19e6ea47bd3dc215ff4232c3392e0b57.md)
- [uart\_emul.h](serial_2uart__emul_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
