---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/wuc__ite__it51xxx_8h.html
original_path: doxygen/html/wuc__ite__it51xxx_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wuc\_ite\_it51xxx.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](wuc__ite__it51xxx_8h_source.md)

| Macros | |
| --- | --- |
| wakeup controller flags | |
| #define | [WUC\_TYPE\_EDGE\_RISING](#a679ab1940f920cfe6c0fa1d5ed14a468)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | WUC rising edge trigger mode. |
| #define | [WUC\_TYPE\_EDGE\_FALLING](#a21b4240f97f62e69f23ea614de699955)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | WUC falling edge trigger mode. |
| #define | [WUC\_TYPE\_EDGE\_BOTH](#a824c451f35efc9b287cd694a0c674095)   ([WUC\_TYPE\_EDGE\_RISING](#a679ab1940f920cfe6c0fa1d5ed14a468) | [WUC\_TYPE\_EDGE\_FALLING](#a21b4240f97f62e69f23ea614de699955)) |
|  | WUC both edge trigger mode. |
| #define | [WUC\_TYPE\_LEVEL\_TRIG](#ad8761c64e6c8463e679673269f719511)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [WUC\_TYPE\_LEVEL\_HIGH](#aca8e63896387e7119a4a3a021c920367)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | WUC level high trigger mode. |
| #define | [WUC\_TYPE\_LEVEL\_LOW](#a8f46aef09381a08af4bc4e88aff0fab3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | WUC level low trigger mode. |

| Functions | |
| --- | --- |
| void | [it51xxx\_wuc\_enable](#a5bea830b4eda87d1eca9a110cf4de495) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | A trigger condition on the corresponding input generates a wake-up signal to the power management control of EC. |
| void | [it51xxx\_wuc\_disable](#ab5e2a83d651b94b9e6dd376bc78c1781) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | A trigger condition on the corresponding input doesn't assert the wake-up signal (canceled not pending). |
| void | [it51xxx\_wuc\_clear\_status](#aac15ac209632efaf52b39dd7e95b364d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | Write-1-clear a trigger condition that occurs on the corresponding input. |
| void | [it51xxx\_wuc\_set\_polarity](#a2a493db8a468803196e2eb64430527df) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Select the trigger edge mode on the corresponding input. |

## Macro Definition Documentation

## [◆ ](#a824c451f35efc9b287cd694a0c674095)WUC\_TYPE\_EDGE\_BOTH

| #define WUC\_TYPE\_EDGE\_BOTH   ([WUC\_TYPE\_EDGE\_RISING](#a679ab1940f920cfe6c0fa1d5ed14a468) | [WUC\_TYPE\_EDGE\_FALLING](#a21b4240f97f62e69f23ea614de699955)) |
| --- |

WUC both edge trigger mode.

## [◆ ](#a21b4240f97f62e69f23ea614de699955)WUC\_TYPE\_EDGE\_FALLING

| #define WUC\_TYPE\_EDGE\_FALLING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

WUC falling edge trigger mode.

## [◆ ](#a679ab1940f920cfe6c0fa1d5ed14a468)WUC\_TYPE\_EDGE\_RISING

| #define WUC\_TYPE\_EDGE\_RISING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

WUC rising edge trigger mode.

## [◆ ](#aca8e63896387e7119a4a3a021c920367)WUC\_TYPE\_LEVEL\_HIGH

| #define WUC\_TYPE\_LEVEL\_HIGH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

WUC level high trigger mode.

## [◆ ](#a8f46aef09381a08af4bc4e88aff0fab3)WUC\_TYPE\_LEVEL\_LOW

| #define WUC\_TYPE\_LEVEL\_LOW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

WUC level low trigger mode.

## [◆ ](#ad8761c64e6c8463e679673269f719511)WUC\_TYPE\_LEVEL\_TRIG

| #define WUC\_TYPE\_LEVEL\_TRIG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## Function Documentation

## [◆ ](#aac15ac209632efaf52b39dd7e95b364d)it51xxx\_wuc\_clear\_status()

| void it51xxx\_wuc\_clear\_status | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

Write-1-clear a trigger condition that occurs on the corresponding input.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mask | Pin mask of WUC group |

## [◆ ](#ab5e2a83d651b94b9e6dd376bc78c1781)it51xxx\_wuc\_disable()

| void it51xxx\_wuc\_disable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

A trigger condition on the corresponding input doesn't assert the wake-up signal (canceled not pending).

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mask | Pin mask of WUC group |

## [◆ ](#a5bea830b4eda87d1eca9a110cf4de495)it51xxx\_wuc\_enable()

| void it51xxx\_wuc\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

A trigger condition on the corresponding input generates a wake-up signal to the power management control of EC.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mask | Pin mask of WUC group |

## [◆ ](#a2a493db8a468803196e2eb64430527df)it51xxx\_wuc\_set\_polarity()

| void it51xxx\_wuc\_set\_polarity | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

Select the trigger edge mode on the corresponding input.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mask | Pin mask of WUC group |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Select the trigger edge mode |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [wuc\_ite\_it51xxx.h](wuc__ite__it51xxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
