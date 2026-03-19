---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__kscan__interface.html
original_path: doxygen/html/group__kscan__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Keyboard Scan Driver APIs

[Device Driver APIs](group__io__interfaces.md)

KSCAN APIs.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [kscan\_callback\_t](#gab65d45708dba142da2c71aa3debd9480)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) row, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) column, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pressed) |
|  | Keyboard scan callback called when user press/release a key on a matrix keyboard. |

| Functions | |
| --- | --- |
| int | [kscan\_config](#ga9caf0c1e798d610befcb9bdd4a50ddc5) (const struct [device](structdevice.md) \*dev, [kscan\_callback\_t](#gab65d45708dba142da2c71aa3debd9480) callback) |
|  | Configure a Keyboard scan instance. |
| int | [kscan\_enable\_callback](#gaa1d46198ea2b36526671b0c32b3b6eab) (const struct [device](structdevice.md) \*dev) |
|  | Enables callback. |
| int | [kscan\_disable\_callback](#ga183471b229ec08d827952c7515625e28) (const struct [device](structdevice.md) \*dev) |
|  | Disables callback. |

## Detailed Description

KSCAN APIs.

Since
:   2.1

Version
:   1.0.0

**[Deprecated](deprecated.md#_deprecated000021)**

## Typedef Documentation

## [◆ ](#gab65d45708dba142da2c71aa3debd9480)kscan\_callback\_t

| typedef void(\* kscan\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) row, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) column, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pressed) |
| --- |

`#include <[kscan.h](kscan_8h.md)>`

Keyboard scan callback called when user press/release a key on a matrix keyboard.

**[Deprecated](deprecated.md#_deprecated000022)**

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | row | Describes row change. |
    | column | Describes column change. |
    | pressed | Describes the kind of key event. |

## Function Documentation

## [◆ ](#ga9caf0c1e798d610befcb9bdd4a50ddc5)kscan\_config()

| int kscan\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [kscan\_callback\_t](#gab65d45708dba142da2c71aa3debd9480) | *callback* ) |

`#include <[kscan.h](kscan_8h.md)>`

Configure a Keyboard scan instance.

**[Deprecated](deprecated.md#_deprecated000023)**

**[Deprecated](deprecated.md#_deprecated000024)**

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | called when keyboard devices reply to a keyboard event such as key pressed/released. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#ga183471b229ec08d827952c7515625e28)kscan\_disable\_callback()

| int kscan\_disable\_callback | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kscan.h](kscan_8h.md)>`

Disables callback.

**[Deprecated](deprecated.md#_deprecated000026)**

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

## [◆ ](#gaa1d46198ea2b36526671b0c32b3b6eab)kscan\_enable\_callback()

| int kscan\_enable\_callback | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kscan.h](kscan_8h.md)>`

Enables callback.

**[Deprecated](deprecated.md#_deprecated000025)**

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | Negative | errno code if failure. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
