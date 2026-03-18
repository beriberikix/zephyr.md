---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__i2c__eeprom__target__api.html
original_path: doxygen/html/group__i2c__eeprom__target__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I2C EEPROM Target Driver API

[Device Driver APIs](group__io__interfaces.md)

I2C EEPROM Target Driver API.
[More...](#details)

| Functions | |
| --- | --- |
| int | [eeprom\_target\_program](#ga8585267ec85234c68a4434e72608b27e) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*eeprom\_data, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int length) |
|  | Program memory of the virtual EEPROM. |
| int | [eeprom\_target\_read](#gadeb18bef0484b2f6dcf91c0131884fc4) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*eeprom\_data, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int offset) |
|  | Read single byte of virtual EEPROM memory. |
| int | [eeprom\_target\_set\_addr](#ga802f5d779e9a837a81b8b617037dfce8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Change the address of eeprom target at runtime. |

## Detailed Description

I2C EEPROM Target Driver API.

Since
:   1.13

Version
:   1.0.0

## Function Documentation

## [◆ ](#ga8585267ec85234c68a4434e72608b27e)eeprom\_target\_program()

| int eeprom\_target\_program | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *eeprom\_data*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *length* ) |

`#include <[eeprom.h](i2c_2target_2eeprom_8h.md)>`

Program memory of the virtual EEPROM.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | eeprom\_data | Pointer of data to program into the virtual eeprom memory |
    | length | Length of data to program into the virtual eeprom memory |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | Invalid data size |

## [◆ ](#gadeb18bef0484b2f6dcf91c0131884fc4)eeprom\_target\_read()

| int eeprom\_target\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *eeprom\_data*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *offset* ) |

`#include <[eeprom.h](i2c_2target_2eeprom_8h.md)>`

Read single byte of virtual EEPROM memory.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | eeprom\_data | Pointer of byte where to store the virtual eeprom memory |
    | offset | Offset into EEPROM memory where to read the byte |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | Invalid data pointer or offset |

## [◆ ](#ga802f5d779e9a837a81b8b617037dfce8)eeprom\_target\_set\_addr()

| int eeprom\_target\_set\_addr | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* ) |

`#include <[eeprom.h](i2c_2target_2eeprom_8h.md)>`

Change the address of eeprom target at runtime.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | addr | New address to assign to the eeprom target device |

Return values
:   | 0 | Is successful |
    | --- | --- |
    | -EINVAL | If parameters are invalid |
    | -EIO | General input / output error during i2c\_taget\_register |
    | -ENOSYS | If target mode is not implemented |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
