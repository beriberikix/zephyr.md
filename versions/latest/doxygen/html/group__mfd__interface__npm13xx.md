---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__mfd__interface__npm13xx.html
original_path: doxygen/html/group__mfd__interface__npm13xx.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MFD NPM13XX Interface

[Device Driver APIs](group__io__interfaces.md) » [Multi Function Device Drivers APIs](group__mfd__interfaces.md)

| Enumerations | |
| --- | --- |
| enum | [mfd\_npm13xx\_event\_t](#ga4ac9f47283f10ea1d847cbd0038aad7a) {     [NPM13XX\_EVENT\_CHG\_COMPLETED](#gga4ac9f47283f10ea1d847cbd0038aad7aa713b4881ca37b1b536fb32dbbb45f858) , [NPM13XX\_EVENT\_CHG\_ERROR](#gga4ac9f47283f10ea1d847cbd0038aad7aa7c34f84901995115cf03399a7c0cf0a6) , [NPM13XX\_EVENT\_BATTERY\_DETECTED](#gga4ac9f47283f10ea1d847cbd0038aad7aa81b8d1ebbebd90a6c80063cfcd52983c) , [NPM13XX\_EVENT\_BATTERY\_REMOVED](#gga4ac9f47283f10ea1d847cbd0038aad7aa0e3ee9c58a2cd04e105c829faf72a50d) ,     [NPM13XX\_EVENT\_SHIPHOLD\_PRESS](#gga4ac9f47283f10ea1d847cbd0038aad7aa958cb58b437567915ccf9c54b20fe646) , [NPM13XX\_EVENT\_SHIPHOLD\_RELEASE](#gga4ac9f47283f10ea1d847cbd0038aad7aa285ae1257239be4145f7ff036cfd88e5) , [NPM13XX\_EVENT\_WATCHDOG\_WARN](#gga4ac9f47283f10ea1d847cbd0038aad7aa044e675f8f58f27318071be0cc315ba7) , [NPM13XX\_EVENT\_VBUS\_DETECTED](#gga4ac9f47283f10ea1d847cbd0038aad7aaed62a7ab4cab4ae1110fe08bf425fa6b) ,     [NPM13XX\_EVENT\_VBUS\_REMOVED](#gga4ac9f47283f10ea1d847cbd0038aad7aab2d73d88655a4a3cf0803bc4ac40179e) , [NPM13XX\_EVENT\_GPIO0\_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aa04af5688f6422ed5f7e37285f0fa98e8) , [NPM13XX\_EVENT\_GPIO1\_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aae0fad2bbb85cca6b6e5a3cb43d859e9c) , [NPM13XX\_EVENT\_GPIO2\_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aa4216711d8a06182068932fef1d542e25) ,     [NPM13XX\_EVENT\_GPIO3\_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aa439a506f9314c64f78c87244edf8c15b) , [NPM13XX\_EVENT\_GPIO4\_EDGE](#gga4ac9f47283f10ea1d847cbd0038aad7aa66c1f49b682bc96fdb186f24834cdb35) , [NPM13XX\_EVENT\_MAX](#gga4ac9f47283f10ea1d847cbd0038aad7aa7b92b922aedb16e55c330254e6df0cfa)   } |

| Functions | |
| --- | --- |
| int | [mfd\_npm13xx\_reg\_read\_burst](#gabba0559ce29b71e1ce7065bf5d36f8d8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read multiple registers from npm13xx. |
| int | [mfd\_npm13xx\_reg\_read](#ga154c4c48888ff1587d157b16e38d2584) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Read single register from npm13xx. |
| int | [mfd\_npm13xx\_reg\_write](#gac1c7815a4bcfb2262fd4f02d28f2f781) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write single register to npm13xx. |
| int | [mfd\_npm13xx\_reg\_write2](#gaeb317a7b4aa2ad37e69c2fda77dbbd0e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data1, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data2) |
|  | Write two registers to npm13xx. |
| int | [mfd\_npm13xx\_reg\_update](#ga239cfcef1ab91e3ccc8fb7f39f11dfd2) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | Update selected bits in npm13xx register. |
| int | [mfd\_npm13xx\_set\_timer](#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms) |
|  | Write npm13xx timer register. |
| int | [mfd\_npm13xx\_reset](#ga43c5a5225a0cc2738506d5556ecb06ba) (const struct [device](structdevice.md) \*dev) |
|  | npm13xx full power reset |
| int | [mfd\_npm13xx\_hibernate](#gaf23758d56ac58f814bc2f093ebfa1282) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) time\_ms) |
|  | npm13xx hibernate |
| int | [mfd\_npm13xx\_add\_callback](#ga3cac4a85cee20242d3a988d9830ea547) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add npm13xx event callback. |
| int | [mfd\_npm13xx\_remove\_callback](#ga35fbc854545b9113f6ec36677491b151) (const struct [device](structdevice.md) \*dev, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove npm13xx event callback. |

## Detailed Description

## Enumeration Type Documentation

## [◆ ](#ga4ac9f47283f10ea1d847cbd0038aad7a)mfd\_npm13xx\_event\_t

| enum [mfd\_npm13xx\_event\_t](#ga4ac9f47283f10ea1d847cbd0038aad7a) |
| --- |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

| Enumerator | |
| --- | --- |
| NPM13XX\_EVENT\_CHG\_COMPLETED |  |
| NPM13XX\_EVENT\_CHG\_ERROR |  |
| NPM13XX\_EVENT\_BATTERY\_DETECTED |  |
| NPM13XX\_EVENT\_BATTERY\_REMOVED |  |
| NPM13XX\_EVENT\_SHIPHOLD\_PRESS |  |
| NPM13XX\_EVENT\_SHIPHOLD\_RELEASE |  |
| NPM13XX\_EVENT\_WATCHDOG\_WARN |  |
| NPM13XX\_EVENT\_VBUS\_DETECTED |  |
| NPM13XX\_EVENT\_VBUS\_REMOVED |  |
| NPM13XX\_EVENT\_GPIO0\_EDGE |  |
| NPM13XX\_EVENT\_GPIO1\_EDGE |  |
| NPM13XX\_EVENT\_GPIO2\_EDGE |  |
| NPM13XX\_EVENT\_GPIO3\_EDGE |  |
| NPM13XX\_EVENT\_GPIO4\_EDGE |  |
| NPM13XX\_EVENT\_MAX |  |

## Function Documentation

## [◆ ](#ga3cac4a85cee20242d3a988d9830ea547)mfd\_npm13xx\_add\_callback()

| int mfd\_npm13xx\_add\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

Add npm13xx event callback.

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | callback | callback |

Returns
:   0 on success, -errno on failure

## [◆ ](#gaf23758d56ac58f814bc2f093ebfa1282)mfd\_npm13xx\_hibernate()

| int mfd\_npm13xx\_hibernate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *time\_ms* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

npm13xx hibernate

Enters low power state, and wakes after specified time

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | time\_ms | timer value in ms |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | if time value is too large |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#ga154c4c48888ff1587d157b16e38d2584)mfd\_npm13xx\_reg\_read()

| int mfd\_npm13xx\_reg\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

Read single register from npm13xx.

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data | Pointer to buffer for received data |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_read\_dt()](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758 "Write then read data from an I2C device.")) |

## [◆ ](#gabba0559ce29b71e1ce7065bf5d36f8d8)mfd\_npm13xx\_reg\_read\_burst()

| int mfd\_npm13xx\_reg\_read\_burst | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

Read multiple registers from npm13xx.

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data | Pointer to buffer for received data |
    | len | Number of bytes to read |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_read\_dt()](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758 "Write then read data from an I2C device.")) |

## [◆ ](#ga239cfcef1ab91e3ccc8fb7f39f11dfd2)mfd\_npm13xx\_reg\_update()

| int mfd\_npm13xx\_reg\_update | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

Update selected bits in npm13xx register.

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data | data to write |
    | mask | mask of bits to be modified |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_read\_dt()](group__i2c__interface.md#ga301733586dcc2a353bdf149b49df5758 "Write then read data from an I2C device."), [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#gac1c7815a4bcfb2262fd4f02d28f2f781)mfd\_npm13xx\_reg\_write()

| int mfd\_npm13xx\_reg\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

Write single register to npm13xx.

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data | data to write |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#gaeb317a7b4aa2ad37e69c2fda77dbbd0e)mfd\_npm13xx\_reg\_write2()

| int mfd\_npm13xx\_reg\_write2 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data1*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data2* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

Write two registers to npm13xx.

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | base | Register base address (bits 15..8 of 16-bit address) |
    | offset | Register offset address (bits 7..0 of 16-bit address) |
    | data1 | first byte of data to write |
    | data2 | second byte of data to write |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#ga35fbc854545b9113f6ec36677491b151)mfd\_npm13xx\_remove\_callback()

| int mfd\_npm13xx\_remove\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

Remove npm13xx event callback.

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | callback | callback |

Returns
:   0 on success, -errno on failure

## [◆ ](#ga43c5a5225a0cc2738506d5556ecb06ba)mfd\_npm13xx\_reset()

| int mfd\_npm13xx\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

npm13xx full power reset

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

## [◆ ](#ga3fe7d1f34e373bd6a4b8ab2bb3ae85f9)mfd\_npm13xx\_set\_timer()

| int mfd\_npm13xx\_set\_timer | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *time\_ms* ) |

`#include <[zephyr/drivers/mfd/npm13xx.h](drivers_2mfd_2npm13xx_8h.md)>`

Write npm13xx timer register.

Parameters
:   | dev | npm13xx mfd device |
    | --- | --- |
    | time\_ms | timer value in ms |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -EINVAL | if time value is too large |
    | -errno | In case of any bus error (see [i2c\_write\_dt()](group__i2c__interface.md#ga2d17b714ba6ebe47d7bdfcb1cf97e44f "Write a set amount of data to an I2C device.")) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
