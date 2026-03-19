---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__haptics__interface.html
original_path: doxygen/html/group__haptics__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Haptics Interface

[Device Driver APIs](group__io__interfaces.md)

Haptics Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [haptics\_driver\_api](structhaptics__driver__api.md) |
|  | Haptic device API. [More...](structhaptics__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [haptics\_stop\_output\_t](#gae34e538c40e259967f5791cc5ebd2707)) (const struct [device](structdevice.md) \*dev) |
|  | Set the haptic device to stop output. |
| typedef int(\* | [haptics\_start\_output\_t](#gaa6c2ff4b8ed7ae83e4006eb735f61a46)) (const struct [device](structdevice.md) \*dev) |
|  | Set the haptic device to start output for a playback event. |

| Functions | |
| --- | --- |
| int | [haptics\_start\_output](#ga96e0b0fad35d6535adad7536a9411f44) (const struct [device](structdevice.md) \*dev) |
|  | Set the haptic device to start output for a playback event. |
| int | [haptics\_stop\_output](#ga42a5fc7e6b6247316cdf356573dbbb33) (const struct [device](structdevice.md) \*dev) |
|  | Set the haptic device to stop output for a playback event. |

## Detailed Description

Haptics Interface.

## Typedef Documentation

## [◆ ](#gaa6c2ff4b8ed7ae83e4006eb735f61a46)haptics\_start\_output\_t

| typedef int(\* haptics\_start\_output\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[haptics.h](haptics_8h.md)>`

Set the haptic device to start output for a playback event.

## [◆ ](#gae34e538c40e259967f5791cc5ebd2707)haptics\_stop\_output\_t

| typedef int(\* haptics\_stop\_output\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[haptics.h](haptics_8h.md)>`

Set the haptic device to stop output.

Parameters
:   | dev | Pointer to the device structure for haptic device instance |
    | --- | --- |

## Function Documentation

## [◆ ](#ga96e0b0fad35d6535adad7536a9411f44)haptics\_start\_output()

| int haptics\_start\_output | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[haptics.h](haptics_8h.md)>`

Set the haptic device to start output for a playback event.

Parameters
:   | dev | Pointer to the device structure for haptic device instance |
    | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |
    | <0 | if failed |

## [◆ ](#ga42a5fc7e6b6247316cdf356573dbbb33)haptics\_stop\_output()

| int haptics\_stop\_output | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[haptics.h](haptics_8h.md)>`

Set the haptic device to stop output for a playback event.

Parameters
:   | dev | Pointer to the device structure for haptic device instance |
    | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |
    | <0 | if failed |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
