---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mdf__interface__npm2100.html
original_path: doxygen/html/group__mdf__interface__npm2100.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MFD NPM2100 Interface

[Device Driver APIs](group__io__interfaces.md) » [Multi Function Device Drivers APIs](group__mfd__interfaces.md)

| Enumerations | |
| --- | --- |
| enum | [mfd\_npm2100\_event](#gae7433fd9cb33e7b3ac0b364d29dc6e32) {     [NPM2100\_EVENT\_SYS\_DIETEMP\_WARN](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a40949e797419f2e317d49aad99ea5a88) , [NPM2100\_EVENT\_SYS\_SHIPHOLD\_FALL](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a51417298380c8aa90363d42370da3eff) , [NPM2100\_EVENT\_SYS\_SHIPHOLD\_RISE](#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae70e607cc5cab890f3ee0388d192cd8d) , [NPM2100\_EVENT\_SYS\_PGRESET\_FALL](#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac16dbc92e22bfe720f00c7accd310443) ,     [NPM2100\_EVENT\_SYS\_PGRESET\_RISE](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a15406e035cadb7b3db4ffdcbc5b0dd4b) , [NPM2100\_EVENT\_SYS\_TIMER\_EXPIRY](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1cc0fb1202d777d1d15f866ef28eae4a) , [NPM2100\_EVENT\_ADC\_VBAT\_READY](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b7adcddff5f20f35c421c9a0e296878) , [NPM2100\_EVENT\_ADC\_DIETEMP\_READY](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a3508143e9a6cc45aab022cb1d41c1f68) ,     [NPM2100\_EVENT\_ADC\_DROOP\_DETECT](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1760e35770442b55a82176fbf8e18b49) , [NPM2100\_EVENT\_ADC\_VOUT\_READY](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a739b885852e147e69b3bf638fd41f11c) , [NPM2100\_EVENT\_GPIO0\_FALL](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a5685e6db1ae012bf52fe84564e6d1333) , [NPM2100\_EVENT\_GPIO0\_RISE](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b942a768806d76a82dfcdb5e657f60f) ,     [NPM2100\_EVENT\_GPIO1\_FALL](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a66f462631778912d296b94639be9e453) , [NPM2100\_EVENT\_GPIO1\_RISE](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a244e3e287d8657bfde5696b9a59d0a25) , [NPM2100\_EVENT\_BOOST\_VBAT\_WARN](#ggae7433fd9cb33e7b3ac0b364d29dc6e32ada55f1aadb3d0159ca93512fa8ca37e6) , [NPM2100\_EVENT\_BOOST\_VOUT\_MIN](#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae903153d89f42a509fb2c12e5d58d948) ,     [NPM2100\_EVENT\_BOOST\_VOUT\_WARN](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a523b2a318b7d0217d52fc460b9d90687) , [NPM2100\_EVENT\_BOOST\_VOUT\_DPS](#ggae7433fd9cb33e7b3ac0b364d29dc6e32ad61a6868a4eaf9ae53270da2f617a4d8) , [NPM2100\_EVENT\_BOOST\_VOUT\_OK](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a764671a05e6d92b140c7ac216ca3b883) , [NPM2100\_EVENT\_LDOSW\_OCP](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a6303f8860213e5de6514b483060354f2) ,     [NPM2100\_EVENT\_LDOSW\_VINTFAIL](#ggae7433fd9cb33e7b3ac0b364d29dc6e32a0bbb9e1c1a73735c734e17527a424f7f) , [NPM2100\_EVENT\_MAX](#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac6f32faf88a0d8f5cf951c00900aca81)   } |
| enum | [mfd\_npm2100\_timer\_mode](#ga6a89922f19450ace9d83a4e110625cfb) { [NPM2100\_TIMER\_MODE\_GENERAL\_PURPOSE](#gga6a89922f19450ace9d83a4e110625cfba421611694d6f42d3e0e8ae1bbafbb03d) , [NPM2100\_TIMER\_MODE\_WDT\_RESET](#gga6a89922f19450ace9d83a4e110625cfbad84e4df7668b904c2af3c537775354c6) , [NPM2100\_TIMER\_MODE\_WDT\_POWER\_CYCLE](#gga6a89922f19450ace9d83a4e110625cfbad110b2ee5d1007416dce11faf71ae34c) , [NPM2100\_TIMER\_MODE\_WAKEUP](#gga6a89922f19450ace9d83a4e110625cfbad3c74cd6c665f5cc49c57d83f873f276) } |

| Functions | |
| --- | --- |
| int | [mfd\_npm2100\_set\_timer](#gaa684cdb822e0e36fefc74b59bfd2b706) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms, enum [mfd\_npm2100\_timer\_mode](#ga6a89922f19450ace9d83a4e110625cfb) mode) |
|  | Write npm2100 timer register. |
| int | [mfd\_npm2100\_start\_timer](#ga085bc3c2d5d775c55ae598a464c9d265) (const struct [device](structdevice.md) \*dev) |
|  | Start npm2100 timer. |
| int | [mfd\_npm2100\_reset](#gac87a33389dfbf30e7f0059bd6aede7dc) (const struct [device](structdevice.md) \*dev) |
|  | npm2100 full power reset |
| int | [mfd\_npm2100\_hibernate](#ga4d34ac6e2c185976bc696ce0091b375a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pass\_through) |
|  | npm2100 hibernate |
| int | [mfd\_npm2100\_add\_callback](#ga137976d9909ad6ec179dce5722c4b865) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add npm2100 event callback. |
| int | [mfd\_npm2100\_remove\_callback](#ga342de8853f0afd2cdab08d2d42883b47) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove npm2100 event callback. |

## Detailed Description

## Enumeration Type Documentation

## [◆ ](#gae7433fd9cb33e7b3ac0b364d29dc6e32)mfd\_npm2100\_event

| enum [mfd\_npm2100\_event](#gae7433fd9cb33e7b3ac0b364d29dc6e32) |
| --- |

`#include <[npm2100.h](drivers_2mfd_2npm2100_8h.md)>`

| Enumerator | |
| --- | --- |
| NPM2100\_EVENT\_SYS\_DIETEMP\_WARN |  |
| NPM2100\_EVENT\_SYS\_SHIPHOLD\_FALL |  |
| NPM2100\_EVENT\_SYS\_SHIPHOLD\_RISE |  |
| NPM2100\_EVENT\_SYS\_PGRESET\_FALL |  |
| NPM2100\_EVENT\_SYS\_PGRESET\_RISE |  |
| NPM2100\_EVENT\_SYS\_TIMER\_EXPIRY |  |
| NPM2100\_EVENT\_ADC\_VBAT\_READY |  |
| NPM2100\_EVENT\_ADC\_DIETEMP\_READY |  |
| NPM2100\_EVENT\_ADC\_DROOP\_DETECT |  |
| NPM2100\_EVENT\_ADC\_VOUT\_READY |  |
| NPM2100\_EVENT\_GPIO0\_FALL |  |
| NPM2100\_EVENT\_GPIO0\_RISE |  |
| NPM2100\_EVENT\_GPIO1\_FALL |  |
| NPM2100\_EVENT\_GPIO1\_RISE |  |
| NPM2100\_EVENT\_BOOST\_VBAT\_WARN |  |
| NPM2100\_EVENT\_BOOST\_VOUT\_MIN |  |
| NPM2100\_EVENT\_BOOST\_VOUT\_WARN |  |
| NPM2100\_EVENT\_BOOST\_VOUT\_DPS |  |
| NPM2100\_EVENT\_BOOST\_VOUT\_OK |  |
| NPM2100\_EVENT\_LDOSW\_OCP |  |
| NPM2100\_EVENT\_LDOSW\_VINTFAIL |  |
| NPM2100\_EVENT\_MAX |  |

## [◆ ](#ga6a89922f19450ace9d83a4e110625cfb)mfd\_npm2100\_timer\_mode

| enum [mfd\_npm2100\_timer\_mode](#ga6a89922f19450ace9d83a4e110625cfb) |
| --- |

`#include <[npm2100.h](drivers_2mfd_2npm2100_8h.md)>`

| Enumerator | |
| --- | --- |
| NPM2100\_TIMER\_MODE\_GENERAL\_PURPOSE |  |
| NPM2100\_TIMER\_MODE\_WDT\_RESET |  |
| NPM2100\_TIMER\_MODE\_WDT\_POWER\_CYCLE |  |
| NPM2100\_TIMER\_MODE\_WAKEUP |  |

## Function Documentation

## [◆ ](#ga137976d9909ad6ec179dce5722c4b865)mfd\_npm2100\_add\_callback()

| int mfd\_npm2100\_add\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) |

`#include <[npm2100.h](drivers_2mfd_2npm2100_8h.md)>`

Add npm2100 event callback.

Parameters
:   | dev | npm2100 mfd device |
    | --- | --- |
    | callback | callback |

Returns
:   0 on success, -errno on failure

## [◆ ](#ga4d34ac6e2c185976bc696ce0091b375a)mfd\_npm2100\_hibernate()

| int mfd\_npm2100\_hibernate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *time\_ms*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *pass\_through* ) |

`#include <[npm2100.h](drivers_2mfd_2npm2100_8h.md)>`

npm2100 hibernate

Enters low power state, and wakes after specified time or "shphld" pin signal. Pass-through mode can be used when the battery voltage is high enough to supply the pmic directly without boosting. This lowers the power consumption of the pmic when hibernate mode is active.

Parameters
:   | dev | npm2100 mfd device |
    | --- | --- |
    | time\_ms | timer value in ms. Set to 0 to disable timer. |
    | pass\_through | set to use pass-through hibernate mode. |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | if time value is too large |
    | -EBUSY | if the timer is already in use. |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#ga342de8853f0afd2cdab08d2d42883b47)mfd\_npm2100\_remove\_callback()

| int mfd\_npm2100\_remove\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) |

`#include <[npm2100.h](drivers_2mfd_2npm2100_8h.md)>`

Remove npm2100 event callback.

Parameters
:   | dev | npm2100 mfd device |
    | --- | --- |
    | callback | callback |

Returns
:   0 on success, -errno on failure

## [◆ ](#gac87a33389dfbf30e7f0059bd6aede7dc)mfd\_npm2100\_reset()

| int mfd\_npm2100\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[npm2100.h](drivers_2mfd_2npm2100_8h.md)>`

npm2100 full power reset

Parameters
:   | dev | npm2100 mfd device |
    | --- | --- |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#gaa684cdb822e0e36fefc74b59bfd2b706)mfd\_npm2100\_set\_timer()

| int mfd\_npm2100\_set\_timer | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *time\_ms*, |
|  |  | enum [mfd\_npm2100\_timer\_mode](#ga6a89922f19450ace9d83a4e110625cfb) | *mode* ) |

`#include <[npm2100.h](drivers_2mfd_2npm2100_8h.md)>`

Write npm2100 timer register.

The timer tick resolution is 1/64 seconds. This function does not start the timer (see [mfd\_npm2100\_start\_timer()](#ga085bc3c2d5d775c55ae598a464c9d265)).

Parameters
:   | dev | npm2100 mfd device |
    | --- | --- |
    | time\_ms | timer value in ms |
    | mode | timer mode |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | if time value is too large |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#ga085bc3c2d5d775c55ae598a464c9d265)mfd\_npm2100\_start\_timer()

| int mfd\_npm2100\_start\_timer | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[npm2100.h](drivers_2mfd_2npm2100_8h.md)>`

Start npm2100 timer.

Parameters
:   | dev | npm2100 mfd device |
    | --- | --- |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
