---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ps2__interface.html
original_path: doxygen/html/group__ps2__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PS/2 Driver APIs

[Device Driver APIs](group__io__interfaces.md)

PS/2 Driver APIs.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [ps2\_callback\_t](#gad7cf29301681fac0d2a359d425a13b5f)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | PS/2 callback called when user types or click a mouse. |

| Functions | |
| --- | --- |
| int | [ps2\_config](#ga8d6da9b966432defb0cd482003c11f15) (const struct [device](structdevice.md) \*dev, [ps2\_callback\_t](#gad7cf29301681fac0d2a359d425a13b5f) callback\_isr) |
|  | Configure a ps2 instance. |
| int | [ps2\_write](#gae291cb991ae9525552fdb52c2fa4ac5e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write to PS/2 device. |
| int | [ps2\_read](#gab91b1efe1f07d409607922f4eb87b221) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read slave-to-host values from PS/2 device. |
| int | [ps2\_enable\_callback](#ga9568487018f4ef972eb463ea2098e254) (const struct [device](structdevice.md) \*dev) |
|  | Enables callback. |
| int | [ps2\_disable\_callback](#gade1a470c3583e465d6a8f24a28611397) (const struct [device](structdevice.md) \*dev) |
|  | Disables callback. |

## Detailed Description

PS/2 Driver APIs.

## Typedef Documentation

## [◆ ](#gad7cf29301681fac0d2a359d425a13b5f)ps2\_callback\_t

| typedef void(\* ps2\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
| --- |

`#include <[ps2.h](ps2_8h.md)>`

PS/2 callback called when user types or click a mouse.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | data | Data byte passed pack to the user. |

## Function Documentation

## [◆ ](#ga8d6da9b966432defb0cd482003c11f15)ps2\_config()

| int ps2\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [ps2\_callback\_t](#gad7cf29301681fac0d2a359d425a13b5f) | *callback\_isr* ) |

`#include <[ps2.h](ps2_8h.md)>`

Configure a ps2 instance.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback\_isr | called when PS/2 devices reply to a configuration command or when a mouse/keyboard send data to the client application. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#gade1a470c3583e465d6a8f24a28611397)ps2\_disable\_callback()

| int ps2\_disable\_callback | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ps2.h](ps2_8h.md)>`

Disables callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#ga9568487018f4ef972eb463ea2098e254)ps2\_enable\_callback()

| int ps2\_enable\_callback | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ps2.h](ps2_8h.md)>`

Enables callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#gab91b1efe1f07d409607922f4eb87b221)ps2\_read()

| int ps2\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) |

`#include <[ps2.h](ps2_8h.md)>`

Read slave-to-host values from PS/2 device.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | value | Pointer used for reading the PS/2 device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#gae291cb991ae9525552fdb52c2fa4ac5e)ps2\_write()

| int ps2\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

`#include <[ps2.h](ps2_8h.md)>`

Write to PS/2 device.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | value | Data for the PS2 device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
