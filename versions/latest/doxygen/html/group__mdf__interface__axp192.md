---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mdf__interface__axp192.html
original_path: doxygen/html/group__mdf__interface__axp192.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MFD AXP192 interface

[Device Driver APIs](group__io__interfaces.md) » [Multi Function Device Drivers APIs](group__mfd__interfaces.md)

| Functions | |
| --- | --- |
| int | [mfd\_axp192\_gpio\_func\_ctrl](#ga61c3f46791f4efa08ee45fc85dc32c81) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*client\_dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, enum [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249) func) |
|  | Request a GPIO pin to be configured to a specific function. |
| int | [mfd\_axp192\_gpio\_func\_get](#ga29db6e44c801fecfa1df2d9da93c2e0b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, enum [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249) \*func) |
|  | Read out current configuration of a specific GPIO pin. |
| int | [mfd\_axp192\_gpio\_pd\_ctrl](#ga8db91c44adbf8ca6f727e2deb0aa96dd) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable pull-down on specified GPIO pin. |
| int | [mfd\_axp192\_gpio\_pd\_get](#gabdacd1e10bacf9f0393beb65327eaeea) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*enabled) |
|  | Read out the current pull-down configuration of a specific GPIO. |
| int | [mfd\_axp192\_gpio\_read\_port](#gaa12241d0655122f05da06dc506d2a5c0) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read GPIO port. |
| int | [mfd\_axp192\_gpio\_write\_port](#ga7570c8657918c15c71fddca264bce10e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | Write GPIO port. |

## Detailed Description

## Function Documentation

## [◆ ](#ga61c3f46791f4efa08ee45fc85dc32c81)mfd\_axp192\_gpio\_func\_ctrl()

| int mfd\_axp192\_gpio\_func\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *client\_dev*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *gpio*, |
|  |  | enum [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249) | *func* ) |

`#include <[axp192.h](drivers_2mfd_2axp192_8h.md)>`

Request a GPIO pin to be configured to a specific function.

GPIO0..4 of AXP192 feature various functions (see [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249 "axp192_gpio_func") for details). A GPIO can only be used by one driver instance. Subsequential calls on the same GPIO will overwrite according function.

Parameters
:   | dev | axp192 mfd device |
    | --- | --- |
    | client\_dev | client device the gpio is used in |
    | gpio | GPIO to be configured (0..4) |
    | func | Function to be configured (see [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249 "axp192_gpio_func") for details) |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if an invalid GPIO number is passed |
    | -ENOTSUP | if the requested function is not supported by the given |
    | -errno | in case of any bus error |

## [◆ ](#ga29db6e44c801fecfa1df2d9da93c2e0b)mfd\_axp192\_gpio\_func\_get()

| int mfd\_axp192\_gpio\_func\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *gpio*, |
|  |  | enum [axp192\_gpio\_func](drivers_2mfd_2axp192_8h.md#ac92e5fa77591e02e49570d1a1c38e249) \* | *func* ) |

`#include <[axp192.h](drivers_2mfd_2axp192_8h.md)>`

Read out current configuration of a specific GPIO pin.

Parameters
:   | dev | axp192 mfd device |
    | --- | --- |
    | gpio | GPIO to read configuration from |
    | func | Pointer to store current function configuration in. |

Returns
:   0 on success

Return values
:   | -EINVAL | if an invalid GPIO number is passed |
    | --- | --- |
    | -errno | in case of any bus error |

## [◆ ](#ga8db91c44adbf8ca6f727e2deb0aa96dd)mfd\_axp192\_gpio\_pd\_ctrl()

| int mfd\_axp192\_gpio\_pd\_ctrl | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *gpio*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[axp192.h](drivers_2mfd_2axp192_8h.md)>`

Enable pull-down on specified GPIO pin.

AXP192 only supports pull-down on GPIO3..4. Pull-ups are not supprted.

Parameters
:   | dev | axp192 mfd device |
    | --- | --- |
    | gpio | GPIO to control pull-downs |
    | enable | true to enable, false to disable pull-down |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | if an invalid argument is given (e.g. invalid GPIO number) |
    | -ENOTSUP | if pull-down is not supported by the givenn GPIO |
    | -errno | in case of any bus error |

## [◆ ](#gabdacd1e10bacf9f0393beb65327eaeea)mfd\_axp192\_gpio\_pd\_get()

| int mfd\_axp192\_gpio\_pd\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *gpio*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *enabled* ) |

`#include <[axp192.h](drivers_2mfd_2axp192_8h.md)>`

Read out the current pull-down configuration of a specific GPIO.

Parameters
:   | dev | axp192 mfd device |
    | --- | --- |
    | gpio | GPIO to control pull-downs |
    | enabled | Pointer to current pull-down configuration (true: pull-down enabled/ false: pull-down disabled) |

Return values
:   | -EINVAL | if an invalid argument is given (e.g. invalid GPIO number) |
    | --- | --- |
    | -ENOTSUP | if pull-down is not supported by the givenn GPIO |
    | -errno | in case of any bus error |

## [◆ ](#gaa12241d0655122f05da06dc506d2a5c0)mfd\_axp192\_gpio\_read\_port()

| int mfd\_axp192\_gpio\_read\_port | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) |

`#include <[axp192.h](drivers_2mfd_2axp192_8h.md)>`

Read GPIO port.

Parameters
:   | dev | axp192 mfd device |
    | --- | --- |
    | value | Pointer to port value |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | in case of any bus error |

## [◆ ](#ga7570c8657918c15c71fddca264bce10e)mfd\_axp192\_gpio\_write\_port()

| int mfd\_axp192\_gpio\_write\_port | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

`#include <[axp192.h](drivers_2mfd_2axp192_8h.md)>`

Write GPIO port.

Parameters
:   | dev | axp192 mfd device |
    | --- | --- |
    | value | port value |
    | mask | pin mask within the port |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | in case of any bus error |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
