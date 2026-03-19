---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shared__irq_8h.html
original_path: doxygen/html/shared__irq_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shared\_irq.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](shared__irq_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shared\_irq\_driver\_api](structshared__irq__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [isr\_t](#af6d98f7cd2cde7482b7276aa6e0b487c)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_number) |
| typedef int(\* | [shared\_irq\_register\_t](#ae400920b45bedf3da66831597ebca841)) (const struct [device](structdevice.md) \*dev, [isr\_t](#af6d98f7cd2cde7482b7276aa6e0b487c) isr\_func, const struct [device](structdevice.md) \*isr\_dev) |
| typedef int(\* | [shared\_irq\_enable\_t](#a0ff7a6ee448eb3e889aa9a7bd63e49bc)) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*isr\_dev) |
| typedef int(\* | [shared\_irq\_disable\_t](#a22cf2ce082fea27f2087cd1abd74934c)) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*isr\_dev) |

| Functions | |
| --- | --- |
| static int | [shared\_irq\_isr\_register](#a6ef6d536da13ebd8aa75830516dc0696) (const struct [device](structdevice.md) \*dev, [isr\_t](#af6d98f7cd2cde7482b7276aa6e0b487c) isr\_func, const struct [device](structdevice.md) \*isr\_dev) |
|  | Register a device ISR. |
| static int | [shared\_irq\_enable](#af36534589858c1e02ea50ed3cc888d41) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*isr\_dev) |
|  | Enable ISR for device. |
| static int | [shared\_irq\_disable](#adcdb9702c30ca0911103fc8b9857abb4) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*isr\_dev) |
|  | Disable ISR for device. |

## Typedef Documentation

## [◆ ](#af6d98f7cd2cde7482b7276aa6e0b487c)isr\_t

| typedef int(\* isr\_t) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq\_number) |
| --- |

## [◆ ](#a22cf2ce082fea27f2087cd1abd74934c)shared\_irq\_disable\_t

| typedef int(\* shared\_irq\_disable\_t) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*isr\_dev) |
| --- |

## [◆ ](#a0ff7a6ee448eb3e889aa9a7bd63e49bc)shared\_irq\_enable\_t

| typedef int(\* shared\_irq\_enable\_t) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*isr\_dev) |
| --- |

## [◆ ](#ae400920b45bedf3da66831597ebca841)shared\_irq\_register\_t

| typedef int(\* shared\_irq\_register\_t) (const struct [device](structdevice.md) \*dev, [isr\_t](#af6d98f7cd2cde7482b7276aa6e0b487c) isr\_func, const struct [device](structdevice.md) \*isr\_dev) |
| --- |

## Function Documentation

## [◆ ](#adcdb9702c30ca0911103fc8b9857abb4)shared\_irq\_disable()

| | int shared\_irq\_disable | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [device](structdevice.md) \* | *isr\_dev* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Disable ISR for device.

Parameters
:   | dev | Pointer to device structure for SHARED\_IRQ driver instance. |
    | --- | --- |
    | isr\_dev | Pointer to the device that will service the interrupt. |

## [◆ ](#af36534589858c1e02ea50ed3cc888d41)shared\_irq\_enable()

| | int shared\_irq\_enable | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [device](structdevice.md) \* | *isr\_dev* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Enable ISR for device.

Parameters
:   | dev | Pointer to device structure for SHARED\_IRQ driver instance. |
    | --- | --- |
    | isr\_dev | Pointer to the device that will service the interrupt. |

## [◆ ](#a6ef6d536da13ebd8aa75830516dc0696)shared\_irq\_isr\_register()

| | int shared\_irq\_isr\_register | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [isr\_t](#af6d98f7cd2cde7482b7276aa6e0b487c) | *isr\_func*, | |  |  | const struct [device](structdevice.md) \* | *isr\_dev* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Register a device ISR.

Parameters
:   | dev | Pointer to device structure for SHARED\_IRQ driver instance. |
    | --- | --- |
    | isr\_func | Pointer to the ISR function for the device. |
    | isr\_dev | Pointer to the device that will service the interrupt. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shared\_irq.h](shared__irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
