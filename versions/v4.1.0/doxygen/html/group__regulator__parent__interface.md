---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__regulator__parent__interface.html
original_path: doxygen/html/group__regulator__parent__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Regulator Parent Interface

[Device Driver APIs](group__io__interfaces.md) » [Regulator Interface](group__regulator__interface.md)

Regulator Parent Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [PCA9420 Utilities.](group__regulator__parent__pca9420.md) |

| Functions | |
| --- | --- |
| static int | [regulator\_parent\_dvs\_state\_set](#ga980feabe8415a9643eb66c8566d700bf) (const struct [device](structdevice.md) \*dev, [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set a DVS state. |
| static int | [regulator\_parent\_ship\_mode](#gaa65d0a8d792256818a2ba06ad67a4f02) (const struct [device](structdevice.md) \*dev) |
|  | Enter ship mode. |

## Detailed Description

Regulator Parent Interface.

## Function Documentation

## [◆ ](#ga980feabe8415a9643eb66c8566d700bf)regulator\_parent\_dvs\_state\_set()

| | int regulator\_parent\_dvs\_state\_set | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) | *state* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Set a DVS state.

Some PMICs feature DVS (Dynamic Voltage Scaling) by allowing to program the voltage level for multiple states. Such states may be automatically changed by hardware using GPIO pins. Certain MCUs even allow to automatically configure specific output pins when entering low-power modes so that PMIC state is changed without software intervention. This API can be used when state needs to be changed by software.

Parameters
:   | dev | Parent regulator device instance. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | DVS state (vendor specific identifier). |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If given state is not supported. |
    | -EPERM | If state can't be changed by software. |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

## [◆ ](#gaa65d0a8d792256818a2ba06ad67a4f02)regulator\_parent\_ship\_mode()

| | int regulator\_parent\_ship\_mode | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[regulator.h](regulator_8h.md)>`

Enter ship mode.

Some PMICs feature a ship mode, which allows the system to save power. Exit from low power is normally by pin transition.

This API can be used when ship mode needs to be entered.

Parameters
:   | dev | Parent regulator device instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If function is not implemented. |
    | -errno | In case of any other error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
