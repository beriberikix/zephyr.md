---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mdf__interface__npm1300.html
original_path: doxygen/html/group__mdf__interface__npm1300.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MFD NPM1300 Interface

[Device Driver APIs](group__io__interfaces.md) » [Multi Function Device Drivers APIs](group__mfd__interfaces.md)

| Enumerations | |
| --- | --- |
| enum | [mfd\_npm1300\_event\_t](#gad15bf59ebf3c5572347e939c4c2e6989) {     [NPM1300\_EVENT\_CHG\_COMPLETED](#ggad15bf59ebf3c5572347e939c4c2e6989a04241a0410734d82aee28c515a0a92c0) , [NPM1300\_EVENT\_CHG\_ERROR](#ggad15bf59ebf3c5572347e939c4c2e6989a153a82c7f6bac3393267c4ca0f16b8e3) , [NPM1300\_EVENT\_BATTERY\_DETECTED](#ggad15bf59ebf3c5572347e939c4c2e6989a8524187e6aa6ef0683265b1340cc117f) , [NPM1300\_EVENT\_BATTERY\_REMOVED](#ggad15bf59ebf3c5572347e939c4c2e6989a98ff199ec155bd8ce7e42ede4aa90c78) ,     [NPM1300\_EVENT\_SHIPHOLD\_PRESS](#ggad15bf59ebf3c5572347e939c4c2e6989a70c303c4863161a086ddfe07fe315cd0) , [NPM1300\_EVENT\_SHIPHOLD\_RELEASE](#ggad15bf59ebf3c5572347e939c4c2e6989abb790b641b8d0a8d87b2fb5aabbc5bae) , [NPM1300\_EVENT\_WATCHDOG\_WARN](#ggad15bf59ebf3c5572347e939c4c2e6989a182e6c0806f1d21802a628ccdf92c018) , [NPM1300\_EVENT\_VBUS\_DETECTED](#ggad15bf59ebf3c5572347e939c4c2e6989aebe54d5f1704b81873ca2dce17e44a47) ,     [NPM1300\_EVENT\_VBUS\_REMOVED](#ggad15bf59ebf3c5572347e939c4c2e6989a94a3133140147f38e358ac97ed45ccaf) , [NPM1300\_EVENT\_MAX](#ggad15bf59ebf3c5572347e939c4c2e6989a28557da1ca76c99c0a646cb687ef6291)   } |

| Functions | |
| --- | --- |
| int | [mfd\_npm1300\_reg\_read\_burst](#ga021909959af74df2d324c7a98ce30c96) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read multiple registers from npm1300. |
| int | [mfd\_npm1300\_reg\_read](#gaf068cde6e9482ee498429f75ab30c851) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Read single register from npm1300. |
| int | [mfd\_npm1300\_reg\_write](#ga36e6db4a42e0ef3db7e63fcaad98d8cf) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write single register to npm1300. |
| int | [mfd\_npm1300\_reg\_write2](#ga9bc9a9ae79181004f1303c12e2158fc7) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data1, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data2) |
|  | Write two registers to npm1300. |
| int | [mfd\_npm1300\_reg\_update](#gade28611b9ee6caee19d62f4de6f428f9) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | Update selected bits in npm1300 register. |
| int | [mfd\_npm1300\_set\_timer](#gae009c00f3935a655631aef7b00efbffb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms) |
|  | Write npm1300 timer register. |
| int | [mfd\_npm1300\_reset](#ga470c32ccd5eb357bbf7578ceb57be686) (const struct [device](structdevice.md) \*dev) |
|  | npm1300 full power reset |
| int | [mfd\_npm1300\_hibernate](#ga8ebf64d5161863d8cf70179e5d9bc8e6) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms) |
|  | npm1300 hibernate |
| int | [mfd\_npm1300\_add\_callback](#ga2ea73b039df7ae7a26b67ffe96de8cf0) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add npm1300 event callback. |
| int | [mfd\_npm1300\_remove\_callback](#ga917ef06548659c0e447081ac475b4624) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove npm1300 event callback. |

## Detailed Description

## Enumeration Type Documentation

## [◆ ](#gad15bf59ebf3c5572347e939c4c2e6989)mfd\_npm1300\_event\_t

| enum [mfd\_npm1300\_event\_t](#gad15bf59ebf3c5572347e939c4c2e6989) |
| --- |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

| Enumerator | |
| --- | --- |
| NPM1300\_EVENT\_CHG\_COMPLETED |  |
| NPM1300\_EVENT\_CHG\_ERROR |  |
| NPM1300\_EVENT\_BATTERY\_DETECTED |  |
| NPM1300\_EVENT\_BATTERY\_REMOVED |  |
| NPM1300\_EVENT\_SHIPHOLD\_PRESS |  |
| NPM1300\_EVENT\_SHIPHOLD\_RELEASE |  |
| NPM1300\_EVENT\_WATCHDOG\_WARN |  |
| NPM1300\_EVENT\_VBUS\_DETECTED |  |
| NPM1300\_EVENT\_VBUS\_REMOVED |  |
| NPM1300\_EVENT\_MAX |  |

## Function Documentation

## [◆ ](#ga2ea73b039df7ae7a26b67ffe96de8cf0)mfd\_npm1300\_add\_callback()

| int mfd\_npm1300\_add\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

Add npm1300 event callback.

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | callback | callback |

Returns
:   0 on success, -errno on failure

## [◆ ](#ga8ebf64d5161863d8cf70179e5d9bc8e6)mfd\_npm1300\_hibernate()

| int mfd\_npm1300\_hibernate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *time\_ms* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

npm1300 hibernate

Enters low power state, and wakes after specified time

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | time\_ms | timer value in ms |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | if time value is too large |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#gaf068cde6e9482ee498429f75ab30c851)mfd\_npm1300\_reg\_read()

| int mfd\_npm1300\_reg\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

Read single register from npm1300.

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data | Pointer to buffer for received data |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_read\_dt()](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758 "Write then read data from an I2C device.")) |

## [◆ ](#ga021909959af74df2d324c7a98ce30c96)mfd\_npm1300\_reg\_read\_burst()

| int mfd\_npm1300\_reg\_read\_burst | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

Read multiple registers from npm1300.

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data | Pointer to buffer for received data |
    | len | Number of bytes to read |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_read\_dt()](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758 "Write then read data from an I2C device.")) |

## [◆ ](#gade28611b9ee6caee19d62f4de6f428f9)mfd\_npm1300\_reg\_update()

| int mfd\_npm1300\_reg\_update | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

Update selected bits in npm1300 register.

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data | data to write |
    | mask | mask of bits to be modified |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_read\_dt()](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758 "Write then read data from an I2C device."), [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#ga36e6db4a42e0ef3db7e63fcaad98d8cf)mfd\_npm1300\_reg\_write()

| int mfd\_npm1300\_reg\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

Write single register to npm1300.

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data | data to write |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#ga9bc9a9ae79181004f1303c12e2158fc7)mfd\_npm1300\_reg\_write2()

| int mfd\_npm1300\_reg\_write2 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data1*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data2* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

Write two registers to npm1300.

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data1 | first byte of data to write |
    | data2 | second byte of data to write |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#ga917ef06548659c0e447081ac475b4624)mfd\_npm1300\_remove\_callback()

| int mfd\_npm1300\_remove\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

Remove npm1300 event callback.

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | callback | callback |

Returns
:   0 on success, -errno on failure

## [◆ ](#ga470c32ccd5eb357bbf7578ceb57be686)mfd\_npm1300\_reset()

| int mfd\_npm1300\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

npm1300 full power reset

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#gae009c00f3935a655631aef7b00efbffb)mfd\_npm1300\_set\_timer()

| int mfd\_npm1300\_set\_timer | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *time\_ms* ) |

`#include <[npm1300.h](drivers_2mfd_2npm1300_8h.md)>`

Write npm1300 timer register.

Parameters
:   | dev | npm1300 mfd device |
    | --- | --- |
    | time\_ms | timer value in ms |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | if time value is too large |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
