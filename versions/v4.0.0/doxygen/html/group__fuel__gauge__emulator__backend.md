---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__fuel__gauge__emulator__backend.html
original_path: doxygen/html/group__fuel__gauge__emulator__backend.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Fuel gauge backend emulator APIs

[Device Driver APIs](group__io__interfaces.md)

Fuel gauge backend emulator APIs.
[More...](#details)

| Functions | |
| --- | --- |
| int | [emul\_fuel\_gauge\_set\_battery\_charging](#gab6493138c35191a58e6f28c24b97715e) (const struct [emul](structemul.md) \*target, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uV, int uA) |
|  | Set charging for fuel gauge associated battery. |
| int | [emul\_fuel\_gauge\_is\_battery\_cutoff](#gaf8326331c7470b41aa542f828b20a828) (const struct [emul](structemul.md) \*target, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*cutoff) |
|  | Check if the battery has been cut off. |

## Detailed Description

Fuel gauge backend emulator APIs.

## Function Documentation

## [◆ ](#gaf8326331c7470b41aa542f828b20a828)emul\_fuel\_gauge\_is\_battery\_cutoff()

| int emul\_fuel\_gauge\_is\_battery\_cutoff | ( | const struct [emul](structemul.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *cutoff* ) |

`#include <[emul_fuel_gauge.h](emul__fuel__gauge_8h.md)>`

Check if the battery has been cut off.

Parameters
:   | target | Pointer to the emulator structure for the fuel gauge emulator instance. |
    | --- | --- |
    | cutoff | Pointer to bool storing variable. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if not supported by emulator. |

## [◆ ](#gab6493138c35191a58e6f28c24b97715e)emul\_fuel\_gauge\_set\_battery\_charging()

| int emul\_fuel\_gauge\_set\_battery\_charging | ( | const struct [emul](structemul.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *uV*, |
|  |  | int | *uA* ) |

`#include <[emul_fuel_gauge.h](emul__fuel__gauge_8h.md)>`

Set charging for fuel gauge associated battery.

Set how much the battery associated with a fuel gauge IC is charging or discharging. Where voltage is always positive and a positive or negative current denotes charging or discharging, respectively.

Parameters
:   | target | Pointer to the emulator structure for the fuel gauge emulator instance. |
    | --- | --- |
    | uV | Microvolts describing the battery voltage. |
    | uA | Microamps describing the battery current where negative is discharging. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | if mV or mA are 0. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
